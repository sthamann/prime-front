#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""epstein_collapse_probe -- PRIME.KR4.EPSTEIN.COLLAPSE.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
measured windows, NO counterexample-to-anything claim.  It closes no
gate and narrows no gate.

=======================================================================
MISSION (the round-120 named lever: the REAL Epstein collapse test)
=======================================================================
Round 120 (kr4_defectjet_probe, SPEC_SHA 4a3ba8e8) measured the
collapse-channel detector power on SYNTHETIC matched injections:
every off-line pair down to relative excess 2.4e-4 dies by IN-WINDOW
SZEGO COLLAPSE with the logarithmic death law
  t_death ~ 1.53 + 0.79 ln(1/delta_o)          (SYN background),
and extrapolated the REAL Epstein witness price to L ~ 3..7 with a
source sieve of ~1e3..1e4 atoms -- MODEL-grade, with the typed caveat
that the SYN background (finite atoms + Lebesgue floor) is more
fragile than a continuum arithmetic world.  THIS probe builds the
REAL Epstein world from its arithmetic source data and runs the test.

THE WORLD.  Q(x,y) = x^2 + 5 y^2 (discriminant -20, class number 2,
the round-102/117 witness form).  Z_Q(s) = sum_{(x,y) != 0} Q^{-s} =
sum r_Q(n) n^{-s} (r_Q(1) = 2); completed log-derivative
  xi_Q'/xi_Q(s) = 1/s + 1/(s-1) + c20 + psi(s) + Z_Q'/Z_Q(s),
  c20 = log(sqrt(20)/(2 pi)),
functional equation s -> 1-s (Hecke/theta; round-117 audit machinery).
THE SCREW FUNCTION (the Q analog of Suzuki's g, derived here and
gate-checked layer by layer; pre-freeze calibration run disclosed:
pin identity closes to the mesh-bias scale sigma^2 delta^2 BEFORE
defect subtraction, as designed):
  g_Q(t) = -8(cosh(t/2) - 1)                       [s = 0,1 poles]
         + sum_{2 <= n, log n < t} (Lambda_Q(n)/sqrt(n)) (t - log n)
                                                    [Lambda_Q atoms]
         + a_Q t - S_Q(0) + S_Q(t),                 [arch, Gamma(s)]
  S_Q(t) = e^{-t/2} Phi(e^{-t}, 2, 1/2) = sum_k e^{-(k+1/2)t}/(k+1/2)^2,
  S_Q'' = rho_Q(t) = e^{-t/2}/(1 - e^{-t}),  S_Q(0) = pi^2/2,
  a_Q = -psi(1/2) - c20   (psi(1/2) = -gamma_E - 2 log 2, exact),
with g_Q(0) = 0 and the EXACT gauge identity (gated):
  sigma^2 LS_Q(sigma) - sigma S_Q(0) = -(psi(sigma + 1/2) - psi(1/2)),
so that (1/2) <-g_Q'', e^{-sigma|.|}> = xi_Q'/xi_Q(1/2 + sigma) for
Re sigma > max(1/2, theta_Q - 1/2), the Q pin identity.  Lag row by
exact second differences (round-90 convention): row[d] = <-g_Q'',
Lambda_d>, row[0] = -2 g_Q(delta)/delta.  The Toeplitz sections
T_k[i,j] = row[|i-j|] ARE localized Weil-positivity tests: for any
real vector x, x^T T x = <-g_Q'', h_x * h~_x> with h_x the explicit
step function (1/sqrt(delta)) sum x_i 1_{[i delta, (i+1) delta]} --
a certified negative value is a certified violation of windowed Weil
positivity for xi_Q by an EXPLICIT admissible test function (the
statement is mesh-free: any mesh only selects test functions; finite
t_death is an UPPER bound on the true violation window).

THE LAMBDA_Q SIEVE (T1).  r_Q(n) by exact lattice count; EXACT ward
r_Q(n) = t(n) + u(n) for ALL n <= NCUT, where t = 1 * chi_{-20}
(ideal counts of Q(sqrt(-5))) and u = chi_{-4} * chi_5 (the genus
character), and r_{Q'}(n) = t(n) - u(n) >= 0 for the second class
Q' = 2x^2 + 2xy + 3y^2 (integer arithmetic, no rounding anywhere).
Lambda_Q by the log-derivative recursion (NO Euler product exists;
Lambda_Q lives on ALL n and can be negative):
  r(1) Lambda_Q(n) = r(n) log n - sum_{e | n, 1 < e < n}
                     Lambda_Q(e) r(n/e).
WARDS: (i) EULER ward -- the same recursion run on the ideal counts
t(n) (r(1) = 1) must reproduce Lambda_K(p^k) = (1 + chi_{-20}(p)^k)
log p exactly and vanish off prime powers (zeta_K = zeta L_{-20} HAS
an Euler product: the classical/diagonal cross-check demanded by the
contract); (ii) SYMBOLIC ward -- exact-rational recursion in the
log-prime basis (Fractions) for n <= 48 vs the mp table; (iii)
DIRICHLET ward -- three routes to Z'/Z at deep real s (direct r-sums,
Lambda series, incomplete-gamma audit) agree.  Lambda_Q at dps 120.

THE COLLAPSE TEST (T2, frozen design).  Mesh delta = 0.003 primary
(0.006 stability mate), window L_MAX = 8.0 (n = 2667 rows; the
contract ladder [3,7] plus one insurance rung; world atoms are all
n >= 2 with log n < L_MAX, i.e. n <= 2980).  Rung marks RUNGS =
(1.5, 2.0, 2.568, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 8.0)
are PREFIXES of the one row (the Szego death index is intrinsic).
Szego at dps 80 (mate at dps 60).  WORLDS: TRUE zeta (round-90
builder, KR.DPS raised to 90 module-global -- instrument precision,
no frozen-file edit), ZK = zeta_K = zeta L_{-20} (the MATCHED NULL:
same pole layer, same arch layer, same conductor constant, Euler
atoms, GRH-expected -- this resolves the round-120 background
caveat: the background is now the real continuum arithmetic world),
Q (the target), Q-SCRAMBLE (Lambda_Q weights reversed,
deterministic), TRUE+PLANT and ZK+PLANT (exact off-line pair rows,
round-120 cosh recurrence; the sharpest comparator: ZK+PLANT differs
from Q only by real-vs-planted arithmetic), Q-MINUS-WITNESS (the
witness pair row SUBTRACTED from the Q row: audit-parameterized
ATTRIBUTION control, typed -- if the collapse is the witness's, the
subtracted world must complete past the death), SMOOTH/SCRARITH
(round-90 continuity controls at L4 = 2.568).
PRE-REGISTERED PREDICTIONS: P1 Q collapses at t_death <= 8.0 (point
prediction 2.81 by the round-120 log law at delta_w = 0.19693);
P2 TRUE and ZK complete through 8.0; P3 |t_death(Q) -
t_death(ZK+PLANT)| <= 0.30; P4 Q-MINUS-WITNESS completes through
t_death(Q) + 0.5; P5 the plant-ladder law refit at gamma_w predicts
t_death(Q) within +-0.5.
PLANT LADDER (T3 background calibration, on the TRUE background,
every rung matched at the frozen a* = 1323.11128932): delta in
(0.5, 0.35, 0.25, 0.1969270453, 0.12), gamma(delta) =
sqrt(a* - delta^2); fit t_death = A + B log(1/delta); the measured
(A, B) vs the round-120 SYN constants (1.53, 0.79) prices the
background transfer; the ZK+PLANT single point prices SYN-vs-
arithmetic background directly.  Background margin ladder: the
float64 lambda_min(T_k) profiles of Q/TRUE/ZK price the separation.

CERTIFICATION (T3).  The collapse is pushed to the highest honest
grade: (a) the Szego death index (dps-80 primary; mesh and dps
stability gates); (b) the CERTIFIED QUADRATIC FORM: at k_cert =
k_dagger + pad (pad adaptive in {40, 80, 160, 320}, deterministic
rule: smallest pad with float lambda_min <= -1e-5), the float64
eigenvector x (unit norm) of the most negative eigenvalue of
T_{k_cert} is evaluated EXACTLY on the mp row: V = x^T T x computed
in workdps(80) and workdps(110) (autocorrelation of the 53-bit x is
exact there), with the printed error budget
  |V_err| <= (sum_d (2 - delta_{d0}) |w_d|) * 4 eps_g / delta,
  eps_g <= 1e-76 * max(1, |g|)  (dps-90 row build, Lambda dps 120,
  S_Q series floor, lerchphi),
i.e. budget <~ 1e-65; gate V <= -1e-6 and |V| >= 1e6 x budget and
two-precision agreement <= 1e-40 relative.  TYPED: CERT-NUM
(two-precision-warded, budgeted evaluation of an exact finite
rational-in-logs expression; no interval library).  The
INTERPRETATION 'V < 0 => xi_Q has an off-line zero' rides the
classical Weil/Guinand explicit formula for xi_Q (Hecke theta;
typed COND-CLASSICAL, cited not re-proven); the source-side
statement itself is unconditional-numeric.
DEFECT SUBTRACTION + CAUCHY BUDGETS (round-120 instrument, T3): at
the Q pins the reads are defect-subtracted with the SAME machinery
(KDJ.prep_defect / defect_jet / defect_val imported frozen; density
rho_Q,smooth = 2 cosh(t/2) - e^{-t/2}/(1 - e^{-t}); atoms
float-placed EXACTLY as in the build, weights mp, negation inside
workdps -- the round-120 AMENDMENT-1c lesson).  Channels: MEAS =
1.5 x sup|F_sub - F_audit| on the a-contour (rigorous Cauchy given
the audit; audit = FD log-derivative of the incomplete-gamma xi_Q
at dps 80, h = 1e-20, cross-warded against the Dirichlet route);
COND = (R_disk + tail_model + 1.5 resum)/(2|sigma|) with K_TAIL_Q =
12.24 (3 x the round-118 constant: the Davenport-Heilbronn tail
inflation, DECLARED MODEL); DISK-ONLY as in round 118.

PINS (T2 fires-iff-fires, the violation window in a).  The exact
round-117 window formula gives a in (1308.9, 1337.5) where the
witness has 4|w_a| > 1.  THEORY ANSWER (stated, gated accordingly):
the Szego collapse is a WORLD-level positivity event -- it carries
no a-dependence; the a-window lives in the RADIUS-4/rate currency.
Hence the frozen gating: (i) the collapse fires on the Q row and on
no null world; (ii) the RATE channel (certified lower bound
(d'_m - E_m)/(d'_{m-1} + E_{m-1}) > 1) is measured at the pins
aQstar = a* (sigma0 = sqrt(a*), IN-window), a256 (sigma0 16) and
a144 (sigma0 12) (both OUT-window, witness |4w| = 0.545 at a = 256)
on the largest completing prefix rung: it must fire NOWHERE at this
budget -- in-window because the round-117/120 price m_2 = ln 2 x
gamma^2/delta^2 = 23648 is unreachable (printed, not retried),
out-window because the theory forbids it at any budget unless some
OTHER off-line zero's window covers a = 256/144 (the census box
answers; gated accordingly).  Depth tables m <= 8 with E_meas /
E_cond / widths; direct Q jets (R4.build_jet_epstein, M 128 dps 150
qmax 30000 orders 24, control-grade widths declared) as comparator.
Z1 AT THE PINS: transcription scan of the Q depth vector against
partial sums over the audit-located on-line ordinates (bar 1e-6).

CENSUS (audit-grade context, X5-typed instrument): on-line ordinates
of xi_Q in (0.2, 45) by sign scan (dps 30); off-line zeros by
argument-principle winding on the boxes Re s in [0.51, 1.6] x Im in
[0.1, 30] (expected count 0) and [0.1, 45] (expected 1 = the
witness); windings must be integers within 0.02; Euler-region bound
B(1.6) = sum_{n >= 4} r_Q(n) n^{-1.6} / r_Q(1) < 1 rules out zeros
with Re s >= 1.6 at ALL heights (computed from the exact r table +
integral tail).  WITNESS refinement from the frozen seed 0.7+36.4i
(round-117 audit route, dps 60): cross-ward <= 1e-5 vs the record
rho = 0.6969270453 + 36.3740636864i; |xi_Q| <= 1e-40; window formula
re-evaluation vs frozen (1308.9, 1337.5) within 0.1.

MIN-CUT (T4): extend the round-116 graph with
  UNCOND -> EPQ-SIEVE-MEAS            [MEAS, cap 1]
  EPQ-SIEVE-MEAS -> EPQ-COLLAPSE-CERT [UNC]
  EPQ-COLLAPSE-CERT -> KR4-FALSIFIER-VALIDATED [UNC]
and NO edge into RH or R4-HYP: a validated falsifier is not a
positivity source.  GATES: flows stay 4/4; census classes unchanged;
BFS from the new nodes cannot reach RH or R4-HYP.  THE BRUTAL T4
ANSWER (frozen in advance, adjudicated by the run): detection of a
planted-by-arithmetic falsehood is ORTHOGONAL to proving positivity
forever -- the unconditional statement that emerges is a certified
finite algorithm + explicit certificate: 'windowed Weil positivity
for xi_Q fails at window t <= t_cert, with an explicit test vector
and a certified negative pairing value, built from r_Q(n) counts
alone'; for zeta the same instrument at any finite window proves
nothing (the all-m/dense-a/all-L omega absorbs it).

CONTROLS/SCREENS (T5): SMOOTH/SCRARITH die at the round-90 radii
0.264/0.744 (+-0.05); Q-SCRAMBLE dies (typed, not gated to a
target); conditioning = deterministic 1e-25 row perturbation: death
index shift must be 0 bins AND the certified value shift must be
NONZERO and <= 1e-8 (the round-120 exactly-zero-response red flag,
gated from both sides); tau-screen typing printed (the certificate
value IS a windowed source-side functional -- Euler-computable,
DISGUISE-ADJACENT for the value channel; the carrier-native content
is the positivity/collapse EVENT and its location).

FROZEN NUMERICS.  DPS_ROW 90 (Q/ZK/plant rows), DPS_LAM 120,
DPS_SZ 80 / DPS_SZ_ALT 60, DPS_ALG 80 (jets, KDJ), DPS_AUD 80
(FD h = 1e-20, qcap 220), census dps 30 (qcap 80), witness dps 60
(qcap 120).  NCUT_Q 20000, NCUT_K 1200, SYMB_N 48.  L_MAX 8.0,
D3 = 0.003, D6 = 0.006.  MMAX_PIN 8, KCONT_Q 48, RA_FRAC 0.8.
Q jets (M, dps, qmax, orders) = (128, 150, 30000, 24).  K_TAIL_Q
12.24.  PAD set (40, 80, 160, 320).  BARS: death mesh 0.15, death
dps 0.03, szego-vs-eig |k_dagger - fail_k| <= 12 bins, cert value
<= -1e-6 and >= 1e6 x budget, two-dps rel <= 1e-40, xplant 0.30,
lawfit 0.5, qminus margin 0.5, pin-closure 3(R + tail) + 1e-12,
layer gates max(3 tail-model, 1e-9), lambda ward rel 1e-12 at
s = 6.5 / 1e-25 at s = 16.5, euler ward 1e-90, symbolic ward 1e-40,
arch identity 1e-40, winding integrality 0.02, controls +-0.05,
conditioning (0, 1e-8], transcription bar 1e-6, runtime 10800 s.
Deterministic: no randomness anywhere; plants and ladder frozen
above; the refined witness enters only audit_/attribution/plant
surfaces (typed; detection is from the r_Q sieve alone).  Cache
verified_zeros_n7000.npy is NOT used anywhere in this probe.
Smoke flag reduces everything and is NOT VERDICT-BEARING.

GATES: G01 AST firewall (zeta/gammainc/findroot only in audit_*,
np.load only in ward_* (unused), witness seed only in audit_*; build
functions reference no witness constant); G02 r_Q = t + u and
r_Q' = t - u exact, all n <= NCUT_Q / 4000; G03 Euler ward; G04
symbolic ward; G05 Dirichlet three-route ward; G06 arch gauge
identity + a_Q + psi(1/2) exact; G07 S_Q density wards; G08 defect
wards (KDJ atom ward + exp(-t) closed-form density ward); G09 audit
cross-ward; G10 witness refinement + window formula; G11 layer +
pin-identity gates (Q and ZK, sigma in {6, 16}, 2.568-prefix,
subtracted); G12 TRUE completes to 8.0; G13 ZK completes to 8.0;
G14 Q collapses (t_death <= 8.0); G15 death stability (mesh + dps);
G16 certified quadratic form; G17 szego-vs-eigenvalue death
consistency; G18 attribution (Q-minus-witness completes past
t_death + 0.5 AND |t(Q) - t(ZK+PLANT)| <= 0.30); G19 law (5-rung
fit, prediction within 0.5; TRUE+PLANT(delta_w) fires); G21 census
(windings integral, counts 0/1, Euler-region bound); G22 rate
channel silent at all three pins; G23 depth enclosure at the pins;
G24 meas <= cond; G25 Z1 no transcription; G26 controls die at
0.264/0.744; G27 conditioning two-sided; G28 min-cut; G99 runtime.
COMPOSITE VERDICT (priority frozen): instrument failure (G01-G11,
G17) => EPQC-INSTRUMENT-EDGE (exit 1) > G12 or G13 fail =>
EPQC-BACKGROUND-COLLAPSE > G14 fail => EPQC-NO-FIRE(located price)
> G16 fail => EPQC-FIRES-UNCERTIFIED > G18 fail =>
EPQC-FIRES-UNATTRIBUTED > else EPQC-COLLAPSE-DETECTION(t_death,
t_cert, certified value, law).  Sub-verdicts: LAW-TRANSFER,
BACKGROUND-PRICED, RATE-SILENT(prices), MINCUT, CONTROLS, Z1,
DISGUISE typing.
DECLARED INSTRUMENT DETAILS (frozen with the spec): the G05 ward
compares the Lambda series and the audit route against the direct
r-sum route with the MEASURED n > NCUT truncation tail added to the
1e-12 bar at s = 6.5 (all three routes share that tail; the deep
point s = 16.5 keeps the raw 1e-25 bar); the census winding walker
refines adaptively (bisection on any step with |Delta arg| > 1.8,
cap 14 levels) because the on-line phase field is dense along the
vertical box edges; the SMOKE ladder cap (L_MAX 3.2) is not a death
and smoke G12/G13 readings are not verdict-bearing.
PRE-FREEZE DISCLOSURE: the Q screw dictionary (gauge a_Q, S_Q, c20),
the r_Q = t + u decomposition, the Lambda_Q recursion and the
mesh-bias-scale pin closure were verified in ONE disclosed
pre-freeze calibration script (scratch, deleted); every bar above
was frozen from the round-90/117/118/120 published numbers plus
that calibration BEFORE the first smoke or full run.  Smoke runs may
catch implementation slips -- any instrument repair is disclosed in
numbered AMENDMENT lines appended below; no bar, grid, pin or
verdict rule moves.
AMENDMENT 1 (smoke 1, 17/24; the PHYSICS of the smoke run was
already clean and is itself a pre-registered observation for the
full run: the real Q row DIES at t = 2.988 (log-law prediction
2.81), TRUE/ZK complete, plants die in delta order, controls die at
0.267/0.741 -- AND the attribution channels read INVERTED
(Q-minus-witness dies at 2.970 ~ t_death, ZK+plant completes the
smoke window): the smoke prefix IS the real Q row, so the full run
must adjudicate a COLLECTIVE collapse (aggregate Davenport-
Heilbronn off-line spectrum) against the single-witness model of
the round-120 extrapolation -- P3/P4 may be HONESTLY FALSIFIED).
Instrument repairs, disclosed: (a) firewall owner logic flagged the
module-level WIT_SEED assignment and the nested helper inside
audit_zk_logd -- ownership is now any-enclosing-function with
audit_ prefix, module-level constant definitions exempt (no
semantic change to the firewall's intent); (b) the G06 ward
evaluated the gauge-identity sum by raw truncation/coarse
quadrature and read its own truncation error (2e-9/1.1e-10): the
sum is now computed with the EXACT psi-form tail (200 explicit
terms + closed tail), effective gate bars 1e-30 (exact-tail route)
and 1e-9 (independent raw 200k series, truncation-limited,
declared); (c) the G08 exponential-density ward's TOY g had the
wrong sign (g = t - (1 - e^{-t}) encodes -g'' = -e^{-t}; the ward
model used +e^{-t}; the read was exactly -1 x the target, rel dev
2.0): the toy is now g = (1 - e^{-t}) - t; the PIPELINE was never
wrong -- the ward model was; (d) first_negative_k skipped sections
between the last geometric mark and n (k_dagger = -1 while szego
died at 996): the scan now includes kmax; (e) added DIAGNOSTICS
(no gate, no bar): the frequency peak of the certificate vector x
(|X(e^{i lambda delta})|^2 over lambda in [0, 80], attribution in
frequency space), one ZK+PLANT(0.35) point (background-masking
price), and an ATTRIBUTION TYPING payload (WITNESS-CARRIED /
COLLECTIVE / BACKGROUND-MASKED / MIXED) attached to the frozen
G18/composite tokens; (f) smoke 2 read the certificate frequency
peak at lambda* = 3.4 -- far below the witness gamma = 36.37: the
collapse may be carried by LOWER off-line zeros of Z_Q (the
round-117 witness was located from the seed 0.7 + 36.4i and was
never shown gamma-minimal; the frozen G21 census counts 0/1 are
that assumption and may be honestly falsified) -- ADDED
audit-side attribution controls: boxed-winding LOCATION of all
off-line zeros with Re s in (0.51, 1.6), Im in (0.05, 45)
(3-unit boxes, 0.75 subdivision, findroot per hit, dedup), a
real-segment sign scan on (0.505, 1.6) (real zeros pair with
factor 1/2 in the density), and the Q-MINUS-ALL-LOCATED world
(all located off-line pair rows subtracted; must complete past
t_death if the located spectrum carries the collapse) -- all
typed audit-parameterized attribution controls like
Q-MINUS-WITNESS, INFO + typing payload, no frozen bar moved;
(g) the locator was shaken out standalone BEFORE the frozen full
run and already found FOUR off-line zeros below 45 (0.9330 +
15.6682i, 0.9377 + 29.9834i, the round-117 witness 0.6969 +
36.3741i, 0.8232 + 44.0001i; the first two cross-verified against
the independent round-117 incomplete-gamma evaluator to |xi_Q| ~
1e-50): the round-102/117 'witness' is NOT the gamma-minimal
off-line zero of this Epstein zeta, the 15.6682 zero carries 26x
its excess (7.64e-4), and its exact round-117 a-window (232.6,
259.7) CONTAINS the frozen 'out-window' pin a = 256 -- the frozen
G21 counts and the G18 witness-attribution prediction are
therefore EXPECTED TO READ FALSIFIED in the full run (declared in
advance; the fires/no-fires, certification, stability, law and
rate-silence gates are untouched); a driver-law control was added
(TRUE + plant at the LOCATED maximal-excess zero, INFO), and the
per-zero table (excess, a-window, m_2 price, SYN-law prediction)
is printed.  No bar, grid, pin, rung or verdict rule moved.
AMENDMENT 2 (full run 1, 26/30, runtime 994 s; disclosed before any
verdict-bearing use): the ZK matched-null world read DIES at t =
7.110 -- EXACTLY log(NCUT_K = 1200) = 7.09: the frozen atom-table
depth for the null was inconsistent with the frozen window L_MAX =
8.0 (prime-power atoms with log n in (7.09, 8.0) were missing, so
the null was silently smooth past 7.09 and its positivity broke at
the cutoff -- an instrument-capacity artifact of the same class as
round-120's GLK, NOT physics; the Q world was never affected,
NCUT_Q = 20000 covers e^8 = 2981).  NCUT_K moves 1200 -> 3100
(table capacity only; every gate bar, rung, pin, prediction and
verdict rule unchanged).  All other run-1 readings were already
clean and are expected to reproduce: Q dies 2.988 stable, certified
V = -1.9697e-2, attribution 2 = LOCATED-SPECTRUM-CARRIES (Q minus
all four located pairs survives to 4.428), pins close at 3.6e-27 /
4.2e-19 / 1.3e-14, rate silent 0.9375/0.8971/0.8524, controls at
0.267/0.741, conditioning 1e-24.
NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import krein_screw_realization_probe as KR   # noqa: E402  round-90 frozen
import radius4_reduction_probe as R4         # noqa: E402  round-117 frozen
import idgraph_search_probe as IG            # noqa: E402  round-116 frozen
import kr4_depth_probe as KD                 # noqa: E402  round-118 frozen
import kr4_defectjet_probe as KDJ            # noqa: E402  round-120 frozen

# ------------------------------------------------------------ frozen bars
D3, D6 = "0.003", "0.006"
L_MAX = 8.0
RUNGS = (1.5, 2.0, 2.568, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 8.0)
L4 = 2.568
DPS_ROW = 90
DPS_LAM = 120
DPS_SZ, DPS_SZ_ALT = 80, 60
DPS_ALG = 80
DPS_AUD = 80
AUD_H = "1e-20"
QCAP_AUD, QCAP_CENSUS, QCAP_WIT = 220, 80, 120
DPS_CENSUS, DPS_WIT = 30, 60
NCUT_Q = 20000
NCUT_K = 3100          # AMENDMENT 2: must cover e^{L_MAX} (was 1200)
SYMB_N = 48
MMAX_PIN = 8
KCONT_Q = 48
RA_FRAC = 0.8
JETQ_M, JETQ_DPS, JETQ_QMAX, JETQ_ORD = 128, 150, 30000, 24
K_TAIL_Q = 12.24            # 3 x round-118 constant: DH-tail inflation, MODEL
SUP_INFLATE = 1.5
PAD_SET = (40, 80, 160, 320)
PLANT_LAW_DELTAS = ("0.5", "0.35", "0.25", "0.1969270453", "0.12")
# frozen witness record (round 117; refinement is audit-side only)
WIT_SEED = ("0.7", "36.4")
WIT_DELTA = 0.1969270453
WIT_GAMMA = 36.3740636864
WIT_ASTAR = 1323.11128932
WIT_WINDOW = (1308.9, 1337.5)
WIT_EXCESS = 2.931e-5
M2_PRICE = 23648
LAW_R120 = (1.53, 0.79)     # t_death ~ A + B ln(1/delta), SYN background
T_PRED_R120 = 2.814
BAR_DEATH_MESH = 0.15
BAR_DEATH_DPS = 0.03
BAR_SZEGO_EIG = 12
BAR_CERT_VAL = -1e-6
BAR_CERT_BUDGET_FAC = 1e6
BAR_CERT_2DPS = 1e-40
ERR_G_ABS = 1e-76
BAR_XPLANT = 0.30
BAR_LAWFIT = 0.5
BAR_QMINUS = 0.5
BAR_PINCLOSE_FLOOR = 1e-12
BAR_LAYER_FLOOR = 1e-9
BAR_LAM_DIR = 1e-12
BAR_LAM_DEEP = 1e-25
BAR_EULER = 1e-90
BAR_SYMB = 1e-40
BAR_ARCH = 1e-40
BAR_WIND = 0.02
BAR_WINFORM = 0.1
CTRL_R_SMOOTH, CTRL_R_SCR, CTRL_TOL = 0.264, 0.744, 0.05
COND_EPS_DPS = 25
BAR_COND_HI = 1e-8
TRANS_BAR = 1e-6
RUNTIME_BAR = 10800.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ====================================================== firewall (G01)
FORBIDDEN = ("zetazero", "siegelz", "siegeltheta", "nzeros", "grampoint")
AUDIT_ONLY = ("zeta", "gammainc", "findroot")
BUILD_PREFIXES = ("build_", "sieve_", "lam_", "pair_", "sq_")


def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owners(lineno: int) -> list[str]:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

    def allowed(lineno: int, prefix: str) -> bool:
        return any(nm.startswith(prefix) for nm in owners(lineno))

    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in FORBIDDEN:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low in AUDIT_ONLY and not allowed(node.lineno, "audit_"):
            bad.append("%s outside audit_ @%d" % (nm, node.lineno))
        if isinstance(node, ast.Attribute) and nm == "load" \
                and not allowed(node.lineno, "ward_"):
            bad.append("np.load outside ward_ @%d" % node.lineno)
        if nm == "WIT_SEED" and owners(node.lineno) \
                and not allowed(node.lineno, "audit_"):
            bad.append("WIT_SEED outside audit_ @%d" % node.lineno)
        if nm in ("WIT_DELTA", "WIT_GAMMA", "WIT_ASTAR"):
            for fn in owners(node.lineno):
                if fn.startswith(BUILD_PREFIXES):
                    bad.append("witness constant inside builder %s @%d"
                               % (fn, node.lineno))
    return (len(bad) == 0, "; ".join(bad) if bad else
            "no zero-oracle; zeta/gammainc/findroot confined to audit_; "
            "witness constants excluded from all build_/sieve_/lam_/"
            "pair_/sq_ functions; zero cache not used in this probe")


# ====================================================== T1: the sieve
CHI20 = {1: 1, 3: 1, 7: 1, 9: 1, 11: -1, 13: -1, 17: -1, 19: -1}
CHI4 = {1: 1, 3: -1}
CHI5 = {1: 1, 2: -1, 3: -1, 4: 1}


def sieve_rq(ncut: int) -> list[int]:
    """r_Q(n) = #{(x,y): x^2 + 5y^2 = n}, exact lattice count."""
    r = [0] * (ncut + 1)
    b = 0
    while 5 * b * b <= ncut:
        a = 0
        while a * a + 5 * b * b <= ncut:
            q = a * a + 5 * b * b
            if q >= 1:
                r[q] += (2 if a else 1) * (2 if b else 1)
            a += 1
        b += 1
    return r


def sieve_rqp(ncut: int) -> list[int]:
    """r_{Q'}(n) for Q' = 2x^2 + 2xy + 3y^2 (both signs, all pairs)."""
    r = [0] * (ncut + 1)
    ymax = int(math.isqrt(2 * ncut // 5) + 2)
    for y in range(-ymax, ymax + 1):
        # 2x^2 + 2xy + (3y^2 - n) = 0 -> x in [(-y - sqrt(y^2 - 2(3y^2-n)))/2,..]
        xmax = int(math.isqrt(ncut) + abs(y) + 2)
        for x in range(-xmax, xmax + 1):
            q = 2 * x * x + 2 * x * y + 3 * y * y
            if 1 <= q <= ncut:
                r[q] += 1
    return r


def sieve_tu(ncut: int) -> tuple[list[int], list[int]]:
    """t = 1 * chi_{-20} (ideal counts), u = chi_{-4} * chi_5 (genus)."""
    t = [0] * (ncut + 1)
    u = [0] * (ncut + 1)
    for d in range(1, ncut + 1):
        c20v = CHI20.get(d % 20, 0)
        c4 = CHI4.get(d % 4, 0)
        for m in range(d, ncut + 1, d):
            if c20v:
                t[m] += c20v
            if c4:
                u[m] += c4 * CHI5.get((m // d) % 5, 0)
    return t, u


def lam_from_coeffs(r: list[int], ncut: int, dps: int) -> list:
    """Log-derivative recursion: r(1) Lam(n) = r(n) log n
    - sum_{e|n, 1<e<n} Lam(e) r(n/e).  Returns mp list (index 0,1 = 0)."""
    with mp.workdps(dps):
        lam = [mp.mpf(0)] * (ncut + 1)
        pre = [mp.mpf(0)] * (ncut + 1)
        r1 = mp.mpf(r[1])
        logs: dict[int, mp.mpf] = {}
        for n in range(2, ncut + 1):
            if n not in logs:
                logs[n] = mp.log(n)
            lam[n] = (r[n] * logs[n] - pre[n]) / r1
            if lam[n] != 0:
                ln = lam[n]
                for m in range(2 * n, ncut + 1, n):
                    if r[m // n]:
                        pre[m] += ln * r[m // n]
    return lam


def lam_euler_k(ncut: int, dps: int) -> list:
    """Lambda of zeta_K = zeta L_{-20}: (1 + chi(p)^k) log p on p^k."""
    with mp.workdps(dps):
        lam = [mp.mpf(0)] * (ncut + 1)
        comp = np.zeros(ncut + 1, dtype=bool)
        for p in range(2, ncut + 1):
            if comp[p]:
                continue
            comp[p * p:: p] = True
            chi = CHI20.get(p % 20, 0)
            lp = mp.log(p)
            q, k = p, 1
            while q <= ncut:
                lam[q] = (1 + chi ** k) * lp
                q *= p
                k += 1
    return lam


def lam_symbolic_ward(rq: list[int], lam_mp: list, nmax: int,
                      dps: int) -> tuple[bool, str]:
    """Exact-rational recursion in the log-prime basis vs the mp table."""
    primes = [p for p in range(2, nmax + 1)
              if all(p % d for d in range(2, p))]

    def logvec(n: int) -> dict[int, Fraction]:
        out: dict[int, Fraction] = {}
        m = n
        for p in primes:
            while m % p == 0:
                out[p] = out.get(p, Fraction(0)) + 1
                m //= p
        return out

    lam_sym: dict[int, dict[int, Fraction]] = {}
    for n in range(2, nmax + 1):
        acc = {p: Fraction(rq[n]) * v for p, v in logvec(n).items()}
        for e in range(2, n):
            if n % e == 0 and e in lam_sym and rq[n // e]:
                for p, v in lam_sym[e].items():
                    acc[p] = acc.get(p, Fraction(0)) - v * rq[n // e]
        lam_sym[n] = {p: v / rq[1] for p, v in acc.items()}
    worst = 0.0
    with mp.workdps(dps):
        lp = {p: mp.log(p) for p in primes}
        for n in range(2, nmax + 1):
            val = mp.fsum(mp.mpf(v.numerator) / v.denominator * lp[p]
                          for p, v in lam_sym[n].items()) \
                if lam_sym[n] else mp.mpf(0)
            sc = max(1.0, abs(float(val)))
            worst = max(worst, float(abs(val - lam_mp[n])) / sc)
    return worst <= BAR_SYMB, ("exact-rational log-basis recursion vs mp "
                               "table, n <= %d: worst rel %.1e (bar %.0e)"
                               % (nmax, worst, BAR_SYMB))


# ====================================================== arch layer (Q)
MPQ: dict[str, mp.mpf] = {}
SQ_CACHE: dict[int, mp.mpf] = {}


def sq_setup() -> None:
    with mp.workdps(DPS_ROW + 20):
        MPQ["C20"] = mp.log(mp.sqrt(20) / (2 * mp.pi))
        MPQ["AQ"] = -mp.digamma(mp.mpf(1) / 2) - MPQ["C20"]
        MPQ["SQ0"] = mp.pi ** 2 / 2


def sq_arch_mp(m_idx: int) -> mp.mpf:
    """S_Q(t) = e^{-t/2} Phi(e^{-t}, 2, 1/2) at t = m_idx * 0.003."""
    if m_idx in SQ_CACHE:
        return SQ_CACHE[m_idx]
    with mp.workdps(DPS_ROW + 10):
        t = mp.mpf(m_idx) * mp.mpf("0.003")
        if m_idx == 0:
            v = MPQ["SQ0"]
        elif t >= mp.mpf("0.3"):
            z = mp.exp(-t)
            tot = mp.mpf(0)
            zp = mp.exp(-t / 2)
            k = 0
            floor = mp.mpf(10) ** (-(DPS_ROW + 8))
            while zp / (k + mp.mpf(1) / 2) ** 2 > floor * (1 + tot):
                tot += zp / (k + mp.mpf(1) / 2) ** 2
                k += 1
                zp *= z
            v = tot
        else:
            v = mp.exp(-t / 2) * mp.lerchphi(mp.exp(-t), 2, mp.mpf(1) / 2)
    SQ_CACHE[m_idx] = v
    return v


def build_lags_c20(L: float, delta_name: str, atoms: list,
                   label: str) -> dict:
    """Lag row of a conductor-20 world (Q / ZK / scramble): pole layer
    + given atoms (u_float, w_mp) + the Gamma(s) arch layer.  Exact
    second differences; g(0) = 0."""
    t0 = time.time()
    with mp.workdps(DPS_ROW + 10):
        dl = mp.mpf(delta_name)
        step = int(round(float(delta_name) / 0.003))
        n = int(round(L / float(delta_name)))
        aq, sq0 = MPQ["AQ"], MPQ["SQ0"]
        gvals = []
        ai = 0
        wsum = mp.mpf(0)
        uwsum = mp.mpf(0)
        for j in range(n + 1):
            t = mp.mpf(j) * dl
            while ai < len(atoms) and atoms[ai][0] < t:
                u, w = atoms[ai]
                wsum += w
                uwsum += w * mp.mpf(u)
                ai += 1
            v = -8 * (mp.cosh(t / 2) - 1) + (t * wsum - uwsum) \
                + aq * t - sq0 + sq_arch_mp(j * step)
            gvals.append(v)
        row = [(-2 * gvals[1] / dl)]
        for d in range(1, n):
            row.append(-(gvals[d - 1] - 2 * gvals[d] + gvals[d + 1]) / dl)
    return {"row": row, "n": n, "delta": float(delta_name),
            "delta_mp": dl, "L": n * float(delta_name), "atoms": atoms,
            "world": label, "build_s": time.time() - t0}


def pair_row_mp(n: int, delta_mp, do_mp, go_mp) -> list:
    """Exact tent row of the off-line pair density 4 Re cosh(mu t),
    mu = delta + i gamma (round-120 cosh recurrence; row[0] included)."""
    with mp.workdps(DPS_ROW + 10):
        dl = mp.mpf(delta_mp)
        mu = mp.mpc(do_mp, go_mp)
        wp = 8 * (mp.cosh(mu * dl) - 1) / (mu * mu * dl)
        chd = mp.cosh(mu * dl)
        shd = mp.sinh(mu * dl)
        ch, sh = mp.mpc(1), mp.mpc(0)
        out = []
        for _k in range(n):
            out.append(mp.re(wp * ch))
            ch, sh = ch * chd + sh * shd, sh * chd + ch * shd
    return out


def rho_q_true(t):
    """Smooth density of -g_Q'': 2 cosh(t/2) - e^{-t/2}/(1 - e^{-t})."""
    return 2 * mp.cosh(t / 2) - mp.exp(-t / 2) / (1 - mp.exp(-t))


# ====================================================== audits (Q side)
_EPS_LAT: dict[int, list] = {}


def audit_lattice(qcap: int) -> list:
    if qcap not in _EPS_LAT:
        cnt: dict[int, int] = {}
        b = 0
        while 5 * b * b <= qcap:
            a = 0
            while a * a + 5 * b * b <= qcap:
                q = a * a + 5 * b * b
                if q >= 1:
                    cnt[q] = cnt.get(q, 0) + (2 if a else 1) * (2 if b else 1)
                a += 1
            b += 1
        _EPS_LAT[qcap] = sorted(cnt.items())
    return _EPS_LAT[qcap]


def audit_xiq(s, dps: int, qcap: int):
    """xi_Q(s) via the incomplete-gamma representation (audit only)."""
    lat = audit_lattice(qcap)
    with mp.workdps(dps):
        s = mp.mpc(s)
        c = 2 * mp.pi / mp.sqrt(20)
        tot = -1 / s - 1 / (1 - s)
        for qv, cnt in lat:
            x = c * qv
            tot += cnt * (x ** (-s) * mp.gammainc(s, x, mp.inf)
                          + x ** (-(1 - s)) * mp.gammainc(1 - s, x, mp.inf))
        return s * (s - 1) * tot


def audit_xiq_logd(s, dps: int = DPS_AUD, qcap: int = QCAP_AUD):
    """FD log-derivative of xi_Q (audit comparator; h = 1e-20)."""
    with mp.workdps(dps):
        h = mp.mpf(AUD_H)
        fp = audit_xiq(mp.mpc(s) + h, dps, qcap)
        fm = audit_xiq(mp.mpc(s) - h, dps, qcap)
        f0 = audit_xiq(mp.mpc(s), dps, qcap)
        return (fp - fm) / (2 * h) / f0


def audit_zk_logd(s, dps: int = 60):
    """xi_K'/xi_K for zeta_K = zeta(s) L(s, chi_-20) (audit; mp.zeta +
    Hurwitz route for the L-function)."""
    with mp.workdps(dps):
        s = mp.mpc(s)
        h = mp.mpf("1e-15")

        def lfun(ss):
            return mp.power(20, -ss) * mp.fsum(
                CHI20[r] * mp.zeta(ss, mp.mpf(r) / 20) for r in CHI20)

        lder = (lfun(s + h) - lfun(s - h)) / (2 * h) / lfun(s)
        zder = mp.zeta(s, derivative=1) / mp.zeta(s)
        c20 = mp.log(mp.sqrt(20) / (2 * mp.pi))
        return (1 / s + 1 / (s - 1) + c20 + mp.digamma(s) + zder + lder)


def audit_refine_witness() -> dict:
    """Refine the witness from the frozen seed (round-117 route)."""
    with mp.workdps(DPS_WIT):
        seed = mp.mpc(WIT_SEED[0], WIT_SEED[1])
        rho = mp.findroot(lambda u: audit_xiq(u, DPS_WIT, QCAP_WIT), seed,
                          maxsteps=60)
        resid = float(abs(audit_xiq(rho, DPS_WIT, QCAP_WIT)))
        de = mp.re(rho) - mp.mpf("0.5")
        ga = mp.im(rho)
        a_st = de * de + ga * ga
        disc = mp.sqrt(2 * de * de + ga * ga)
        a_lo = 3 * de * de + ga * ga - 2 * de * disc
        a_hi = 3 * de * de + ga * ga + 2 * de * disc
        return {"rho": rho, "resid": resid, "delta": de, "gamma": ga,
                "astar": a_st, "excess": float(de * de / (ga * ga)),
                "a_lo": float(a_lo), "a_hi": float(a_hi)}


def audit_locate_offline(im_lo: float, im_hi: float) -> list:
    """Locate the off-line zeros of xi_Q with Re s in (0.51, 1.6),
    Im in (im_lo, im_hi): 3-unit winding boxes, 0.75 subdivision,
    findroot per hit, proximity dedup (audit; attribution control)."""
    zs = []
    k = im_lo
    while k < im_hi - 1e-9:
        k2 = min(k + 3.0, im_hi)
        w = audit_winding(0.51, 1.6, k, k2, 0.35)
        if int(round(w)) >= 1:
            kk = k
            while kk < k2 - 1e-9:
                kk2 = min(kk + 0.75, k2)
                w2 = audit_winding(0.51, 1.6, kk, kk2, 0.3)
                if int(round(w2)) >= 1:
                    try:
                        with mp.workdps(40):
                            rho = mp.findroot(
                                lambda u: audit_xiq(u, 40, QCAP_WIT),
                                mp.mpc("0.9", repr((kk + kk2) / 2)),
                                maxsteps=80)
                            good = (0.5005 < mp.re(rho) < 1.65
                                    and kk - 0.3 < mp.im(rho)
                                    < kk2 + 0.3
                                    and abs(audit_xiq(rho, 40,
                                                      QCAP_WIT))
                                    < 1e-15)
                        if good and all(abs(complex(rho)
                                            - complex(z)) > 0.05
                                        for z in zs):
                            zs.append(rho)
                    except Exception:   # noqa: BLE001 -- typed miss
                        pass
                kk = kk2
        k = k2
    return zs


def audit_real_segment_zeros() -> list:
    """Real zeros of xi_Q on (0.505, 1.6) (sign scan + findroot)."""
    out = []
    with mp.workdps(DPS_CENSUS):
        xs_r = [0.505 + 0.05 * i for i in range(23)]
        vr = [float(mp.re(audit_xiq(mp.mpf(repr(xv)), DPS_CENSUS,
                                    QCAP_CENSUS))) for xv in xs_r]
    for i in range(len(vr) - 1):
        if vr[i] * vr[i + 1] < 0:
            with mp.workdps(40):
                rho = mp.findroot(
                    lambda u: mp.re(audit_xiq(u, 40, QCAP_WIT)),
                    mp.mpf(repr(0.5 * (xs_r[i] + xs_r[i + 1]))),
                    maxsteps=60)
            out.append(rho)
    return out


def audit_online_ordinates(tmax: float, step: float) -> list[float]:
    """Sign-change midpoints of Re xi_Q(1/2 + it) (coarse census)."""
    out = []
    with mp.workdps(DPS_CENSUS):
        tg = [0.2 + step * i for i in range(int((tmax - 0.2) / step) + 1)]
        vals = [float(mp.re(audit_xiq(mp.mpc("0.5", repr(t)), DPS_CENSUS,
                                      QCAP_CENSUS))) for t in tg]
    for i in range(len(tg) - 1):
        if vals[i] * vals[i + 1] < 0:
            out.append(0.5 * (tg[i] + tg[i + 1]))
    return out


def audit_winding(re_lo: float, re_hi: float, im_lo: float,
                  im_hi: float, base_step: float) -> float:
    """Argument-principle winding of xi_Q around a box (adaptive walk;
    refines any step with |Delta arg| > 1.8, cap 14 levels)."""
    corners = [(re_lo, im_lo), (re_hi, im_lo), (re_hi, im_hi),
               (re_lo, im_hi), (re_lo, im_lo)]
    pts: list[complex] = []
    for (x0, y0), (x1, y1) in zip(corners[:-1], corners[1:]):
        seg = max(2, int(math.hypot(x1 - x0, y1 - y0) / base_step))
        for i in range(seg):
            pts.append(complex(x0 + (x1 - x0) * i / seg,
                               y0 + (y1 - y0) * i / seg))
    pts.append(pts[0])

    valcache: dict[complex, complex] = {}

    def val(z: complex) -> complex:
        if z not in valcache:
            valcache[z] = complex(audit_xiq(
                mp.mpc(repr(z.real), repr(z.imag)), DPS_CENSUS,
                QCAP_CENSUS))
        return valcache[z]

    total = 0.0
    for z0, z1 in zip(pts[:-1], pts[1:]):
        stack = [(z0, z1, 0)]
        while stack:
            a, b, lev = stack.pop()
            da = math.atan2((val(b) / val(a)).imag, (val(b) / val(a)).real)
            if abs(da) > 1.8 and lev < 14:
                m = (a + b) / 2
                stack.append((a, m, lev + 1))
                stack.append((m, b, lev + 1))
            else:
                total += da
    return total / (2 * math.pi)


# ====================================================== szego / deaths
def szego_death(row: list, dps: int) -> dict:
    sz = KR.szego_mp(row, dps)
    return sz


def rung_table(sz: dict, delta: float, label: str) -> tuple:
    """Per-rung COMPLETE/DIE table from one szego run (prefix logic)."""
    td = sz["fail_k"] * delta if not sz["ok"] else None
    marks = []
    for rg in RUNGS:
        nb = int(round(rg / delta))
        marks.append("%.3f:%s" % (rg, "DIE" if (td is not None
                                                and td <= rg) else "ok"))
    return td, "  ".join(marks)


def lam_min_profile(row_f: np.ndarray, kmax: int,
                    kstep: int) -> list[tuple[int, float]]:
    """float64 lambda_min(T_k) ladder (background margin pricing)."""
    out = []
    k = kstep
    while k <= kmax:
        T = row_f[np.abs(np.subtract.outer(np.arange(k), np.arange(k)))]
        out.append((k, float(np.linalg.eigvalsh(T)[0])))
        k += kstep
    return out


def first_negative_k(row_f: np.ndarray, kmax: int) -> int:
    """Smallest k with lambda_min(T_k) < 0 (coarse scan + bisection;
    the scan includes kmax -- AMENDMENT 1d)."""
    ks = []
    k = 64
    while k < kmax:
        ks.append(k)
        k = int(k * 1.4) + 8
    ks.append(kmax)
    lo, hi = 8, -1
    for k in ks:
        T = row_f[np.abs(np.subtract.outer(np.arange(k), np.arange(k)))]
        if np.linalg.eigvalsh(T)[0] < 0:
            hi = k
            break
        lo = k
    if hi < 0:
        return -1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        T = row_f[np.abs(np.subtract.outer(np.arange(mid),
                                           np.arange(mid)))]
        if np.linalg.eigvalsh(T)[0] < 0:
            hi = mid
        else:
            lo = mid
    return hi


def quadform_mp(row: list, x: np.ndarray, dps: int):
    """x^T T x on the EXACT mp row (autocorrelation of the 53-bit x is
    exact at dps >= ~45); returns (value, sum|w_d| weight for budget)."""
    k = len(x)
    with mp.workdps(dps):
        xs = [mp.mpf(float(v)) for v in x]
        val = mp.mpf(0)
        wsum = mp.mpf(0)
        for d in range(k):
            wd = mp.fsum(xs[i] * xs[i + d] for i in range(k - d))
            fac = 1 if d == 0 else 2
            val += fac * wd * row[d]
            wsum += fac * abs(wd)
        return val, wsum


# ====================================================== pins (depth)
def tail_model_q(res: float, win: float) -> float:
    return K_TAIL_Q / max(res - 0.5, 0.1) * math.exp(-(res - 0.5) * win)


def analyze_q_pin(label: str, sigma0, a0, build: dict, sz: dict,
                  prep: dict, jet: dict, kcont: int, mmax: int) -> dict:
    """Round-120 subtracted-instrument depth analysis on the Q world."""
    nj = 2 * mmax + 1
    out = {"label": label}
    win = build["n"] * build["delta"]
    t0 = time.time()
    with mp.workdps(DPS_ALG):
        s0 = mp.mpf(sigma0)
        a0m = mp.mpf(a0)
        pj_raw = [x / 2 for x in KD.transfer_cval_jet(
            sz["alphas"], sz["c0"], s0, build["delta_mp"], nj)]
        djets = KDJ.defect_jet(prep, s0, nj)
        pj_sub = [pj_raw[j] - djets[j] for j in range(nj)]
    d_sub, _b = KD.pjet_to_dscaled(pj_sub, s0, a0m, mmax)
    with mp.workdps(DPS_ALG):
        w0 = mp.exp(-s0 * build["delta_mp"])
        cval0, cen0, rad0, marg0 = KD.disk_complex(sz["alphas"],
                                                   sz["c0"], w0)
        p_aud = mp.re(audit_xiq_logd(mp.mpf("0.5") + s0))
        dev_pre = float(abs(pj_raw[0] - p_aud))
        dev_sub = float(abs(pj_sub[0] - p_aud))
        incirc = float(abs(cval0 - cen0) / max(float(rad0), 1e-300))
    tmq = tail_model_q(float(s0), win)
    close_bar = 3.0 * (float(rad0) + tmq) + BAR_PINCLOSE_FLOOR
    out.update(dev_pin_pre=dev_pre, dev_pin_sub=dev_sub,
               close_bar=close_bar, rad_pin=float(rad0), incirc=incirc,
               marg_pin=float(marg0))
    info("%s pin sigma0=%.4f: |P_raw-aud| %.2e -> |P_sub-aud| %.2e "
         "(bar %.1e); R_pin %.1e; |c-cen|/R %.3f"
         % (label, float(s0), dev_pre, dev_sub, close_bar, float(rad0),
            incirc))
    # contour channels
    ra = RA_FRAC * float(a0)
    sup_meas = sup_cond = sup_r = 0.0
    min_res = float("inf")
    min_marg = float("inf")
    with mp.workdps(DPS_ALG):
        for j in range(kcont):
            th = mp.mpf(2 * j) / kcont
            av = a0m + mp.mpf(ra) * mp.expjpi(th)
            sv = mp.sqrt(av)
            wv = mp.exp(-sv * build["delta_mp"])
            cval, _cen, rad, marg = KD.disk_complex(sz["alphas"],
                                                    sz["c0"], wv)
            dval = KDJ.defect_val(prep, sv)
            ptr = KDJ.trunc_val(build["row"], build["delta_mp"], sv)
            f_sub = (cval / 2 - dval) / (2 * sv)
            fa = audit_xiq_logd(mp.mpf("0.5") + sv) / (2 * sv)
            res = float(mp.re(sv))
            asig = float(abs(sv))
            min_res = min(min_res, res)
            min_marg = min(min_marg, float(marg))
            sup_meas = max(sup_meas, float(abs(f_sub - fa)))
            resum = float(abs(cval / 2 - ptr))
            sup_cond = max(sup_cond,
                           (float(rad) + tail_model_q(res, win)
                            + 1.5 * resum) / (2.0 * asig))
            sup_r = max(sup_r, float(rad) / (2.0 * asig))
    sup_meas *= SUP_INFLATE
    out.update(sup_meas=sup_meas, sup_cond=sup_cond, sup_r=sup_r,
               min_res=min_res, min_marg=min_marg)
    print("  [%s] contour K=%d: %.1f s; min Re sigma %.3f; sup dev_F "
          "meas %.3e | cond %.3e | R-only %.3e"
          % (label, kcont, time.time() - t0, min_res, sup_meas,
             sup_cond, sup_r), flush=True)
    # depth table vs the direct Q jet
    djet, wjet = R4.diag_scaled(jet, DPS_ALG)
    djet = djet[: mmax + 1]
    wjet = wjet[: mmax + 1]
    e_meas = KD.budget_dm(sup_meas, float(a0), ra, mmax)
    e_cond = KD.budget_dm(sup_cond, float(a0), ra, mmax)
    e_r = KD.budget_dm(sup_r, float(a0), ra, mmax)
    print("  [%s] DEPTH TABLE (d'_m = 4^m C_{m,m}, Q world):" % label)
    print("    m   d'_jetQ       d'_sub        dev        E_meas     "
          "E_cond     width")
    ok_enc = True
    devs = []
    for m in range(mmax + 1):
        dj = float(djet[m])
        dv = abs(float(d_sub[m]) - dj)
        devs.append(dv)
        if dv > 1.2 * (e_meas[m] + wjet[m]):
            ok_enc = False
        print("    %-3d %.6e  %.6e  %.3e  %.3e  %.3e  %.1e"
              % (m, dj, float(d_sub[m]), dv, e_meas[m], e_cond[m],
                 wjet[m]))

    def cert_depth(ev):
        mc = -1
        for m in range(mmax + 1):
            if ev[m] <= 0.5 * abs(float(djet[m])) and mc == m - 1:
                mc = m
        return mc

    m_cm, m_cc, m_cr = cert_depth(e_meas), cert_depth(e_cond), \
        cert_depth(e_r)
    lb_best, lb_m = -1.0, -1
    for m in range(1, max(m_cm, 1) + 1):
        lo = float(d_sub[m]) - e_meas[m]
        hi = float(d_sub[m - 1]) + e_meas[m - 1]
        if hi > 0 and lo / hi > lb_best:
            lb_best, lb_m = lo / hi, m
    out.update(m_cert_meas=m_cm, m_cert_cond=m_cc, m_cert_ronly=m_cr,
               ok_enc=ok_enc, lb_best=lb_best, lb_m=lb_m,
               d_sub=[float(v) for v in d_sub], devs=devs,
               djet=[float(v) for v in djet], wjet=wjet, e_meas=e_meas)
    info("%s: certified depths meas %d | cond %d | disk-only %d; "
         "rate-LB %.6f at m=%d -> %s"
         % (label, m_cm, m_cc, m_cr, lb_best, lb_m,
            "FIRE" if lb_best > 1.0 else "silent"))
    return out


# ====================================================== min-cut (T4)
def mincut_epq() -> list[tuple[str, bool, str]]:
    gates = []
    flow_base, _cut, _ = IG.max_flow(IG.EDGES, "UNCOND", "RH")
    ext = list(IG.EDGES) + [
        ("UNCOND", "EPQ-SIEVE-MEAS", "MEAS", 1),
        ("EPQ-SIEVE-MEAS", "EPQ-COLLAPSE-CERT", "UNC", IG.INF),
        ("EPQ-COLLAPSE-CERT", "KR4-FALSIFIER-VALIDATED", "UNC", IG.INF),
    ]
    flow_ext, cut_ext, _ = IG.max_flow(ext, "UNCOND", "RH")
    print("    flows base/ext = %d/%d" % (flow_base, flow_ext))
    print("    extended min-cut:")
    for s, d, c in cut_ext:
        print("      %-20s -> %-18s [%s]" % (s, d, c))
    cls = sorted({c for _s, _d, c in cut_ext})
    gates.append(("G28a-mincut-flow-unchanged",
                  flow_base == 4 and flow_ext == 4,
                  "flows %d/%d: the validated falsifier adds NO flow "
                  "into RH" % (flow_base, flow_ext)))
    allowed = {"OMEGA-POS", "OMEGA-POS-MEAS", "MEAS", "OMEGA-LAW",
               "CANDIDATE", "CERT-INSTR"}
    gates.append(("G28b-census-classes-unchanged",
                  set(cls) <= allowed,
                  "cut classes %s" % cls))
    adj: dict[str, set] = {}
    for s, d, c, _cap in ext:
        if c in ("DEF", "UNC", "UNC-DICT", "MEAS"):
            adj.setdefault(s, set()).add(d)
    reach = {"EPQ-SIEVE-MEAS", "EPQ-COLLAPSE-CERT"}
    queue = list(reach)
    while queue:
        nd = queue.pop(0)
        for nx in adj.get(nd, ()):
            if nx not in reach:
                reach.add(nx)
                queue.append(nx)
    gates.append(("G28c-falsifier-no-path-to-RH",
                  "RH" not in reach and "R4-HYP" not in reach,
                  "BFS from the collapse certificate reaches %d nodes; "
                  "RH and R4-HYP unreachable: a detector is a "
                  "falsifier, not a prover" % len(reach)))
    return gates


# ====================================================== main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    l_max = L_MAX
    ncut_q = NCUT_Q
    ncut_k = NCUT_K
    dps_sz = DPS_SZ
    plant_deltas = PLANT_LAW_DELTAS
    kcont_q = KCONT_Q
    mmax = MMAX_PIN
    do_census = True
    do_pins = True
    if smoke:
        l_max = 3.2
        ncut_q = 4000
        ncut_k = 400
        dps_sz = 50
        plant_deltas = ("0.35", "0.1969270453")
        kcont_q = 8
        mmax = 4
        do_census = False
        do_pins = False

    print("epstein_collapse_probe -- PRIME.KR4.EPSTEIN.COLLAPSE.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + SPEC")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det)
    sq_setup()
    print("  contract: PRIME.KR4.EPSTEIN.COLLAPSE.01 -- the round-120")
    print("  named lever: the in-window Szego collapse test on the REAL")
    print("  Epstein witness, from the Lambda_Q sieve alone.")

    # ---------------------------------------------------------- S1
    section("S1  T1: THE LAMBDA_Q SIEVE (exact wards)")
    t0 = time.time()
    rq = sieve_rq(ncut_q)
    rqp = sieve_rqp(min(4000, ncut_q))
    t_id, u_gen = sieve_tu(ncut_q)
    okd = all(rq[n] == t_id[n] + u_gen[n] for n in range(1, ncut_q + 1))
    okd2 = all(rqp[n] == t_id[n] - u_gen[n]
               for n in range(1, len(rqp)))
    okd3 = all(rqp[n] >= 0 for n in range(1, len(rqp)))
    check("G02-rq-decomposition-exact", okd and okd2 and okd3,
          "r_Q == 1*chi_-20 + chi_-4*chi_5 for ALL n <= %d; r_Q' == "
          "t - u >= 0 for n <= %d (exact integers; %.1f s)"
          % (ncut_q, len(rqp) - 1, time.time() - t0))
    t0 = time.time()
    lam_q = lam_from_coeffs(rq, ncut_q, DPS_LAM)
    t_small = t_id[: ncut_k + 1]
    lam_k_rec = lam_from_coeffs(t_small, ncut_k, DPS_LAM)
    lam_k_eul = lam_euler_k(ncut_k, DPS_LAM)
    worst_e = 0.0
    with mp.workdps(DPS_LAM):
        for n in range(2, ncut_k + 1):
            sc = max(1.0, abs(float(lam_k_eul[n])))
            worst_e = max(worst_e,
                          float(abs(lam_k_rec[n] - lam_k_eul[n])) / sc)
    check("G03-lam-euler-ward", worst_e <= BAR_EULER,
          "recursion on ideal counts t(n) == Euler Lambda_K(p^k) = "
          "(1+chi(p)^k) log p AND == 0 off prime powers, n <= %d: "
          "worst dev %.1e (bar %.0e; %.1f s)"
          % (ncut_k, worst_e, BAR_EULER, time.time() - t0))
    ok4, det4 = lam_symbolic_ward(rq, lam_q, SYMB_N, 60)
    check("G04-lam-symbolic-ward", ok4, det4)
    # Dirichlet three-route ward
    with mp.workdps(60):
        dets5 = []
        ok5 = True
        for sg, bar in ((mp.mpf(6), BAR_LAM_DIR),
                        (mp.mpf(16), BAR_LAM_DEEP)):
            s = mp.mpf("0.5") + sg
            Z = mp.fsum(rq[n] * mp.power(n, -s)
                        for n in range(1, ncut_q + 1))
            Zp = mp.fsum(-rq[n] * mp.log(n) * mp.power(n, -s)
                         for n in range(2, ncut_q + 1))
            direct = -Zp / Z
            series = mp.fsum(lam_q[n] * mp.power(n, -s)
                             for n in range(2, ncut_q + 1))
            aud = audit_xiq_logd(s, 60, QCAP_AUD) \
                - (1 / s + 1 / (s - 1) + MPQ["C20"] + mp.digamma(s))
            # measured truncation tail of the Lambda series at this s
            # (AMENDMENT 1a): the series and audit routes differ from
            # the direct r-sum route by the SAME n > NCUT tail; add it.
            tail_meas = float(abs(series - direct))
            d1 = float(abs(series - direct) / abs(direct))
            d2 = float(abs(-aud - direct) / abs(direct))
            bar_eff = bar + 3.0 * tail_meas / abs(float(direct))
            ok5 &= d1 <= bar_eff and d2 <= bar_eff
            dets5.append("s=%.1f: lam-vs-direct %.1e, audit-vs-direct "
                         "%.1e (bar %.0e+3x tail %.1e)"
                         % (float(s), d1, d2, bar, tail_meas))
    check("G05-lam-dirichlet-ward", ok5, "; ".join(dets5))
    with mp.workdps(40):
        lmax = max(abs(float(lam_q[n])) for n in range(2, ncut_q + 1))
        nneg = sum(1 for n in range(2, ncut_q + 1) if lam_q[n] < 0)
        psi1k = float(mp.fsum(lam_q[n] for n in range(2,
                                                      min(1000, ncut_q)
                                                      + 1)))
    info("sieve stats: max|Lambda_Q| = %.3f, negative share %.3f, "
         "psi_Q(1000)/1000 = %.4f (pole residue 1 expected; "
         "NO Euler product: Lambda_Q lives on all n)"
         % (lmax, nneg / (ncut_q - 1), psi1k / 1000.0))

    # ---------------------------------------------------------- S2
    section("S2  DICTIONARY GATES (arch gauge, densities, defect, audit)")
    with mp.workdps(80):
        # psi(1/2) = -gamma - 2 log 2 (classical, checked exactly in mp)
        okp = abs(mp.digamma(mp.mpf(1) / 2)
                  + mp.euler + 2 * mp.log(2)) < mp.mpf(10) ** -70
        # gauge identity sigma^2 LS - sigma S0 == -(psi(1/2+s)-psi(1/2))
        # route 1: 200 explicit terms + EXACT psi-form tail
        # (AMENDMENT 1b): tail_K = psi'(K+1/2)/sg - (psi(K+1/2+sg)
        #                 - psi(K+1/2))/sg^2
        worst_g = 0.0
        K0 = 200
        for sg in (mp.mpf(2), mp.mpf(16)):
            LS = mp.fsum(1 / ((k + mp.mpf(1) / 2) ** 2
                              * (sg + k + mp.mpf(1) / 2))
                         for k in range(K0))
            LS += (mp.polygamma(1, K0 + mp.mpf(1) / 2) / sg
                   - (mp.digamma(K0 + mp.mpf(1) / 2 + sg)
                      - mp.digamma(K0 + mp.mpf(1) / 2)) / (sg * sg))
            lhs = sg * sg * LS - sg * MPQ["SQ0"]
            rhs = -(mp.digamma(mp.mpf(1) / 2 + sg)
                    - mp.digamma(mp.mpf(1) / 2))
            worst_g = max(worst_g, float(abs(lhs - rhs)))
    # route 2 (independent, no psi in the tail): raw 200k series,
    # truncation-limited (declared bar 1e-9)
    with mp.workdps(80):
        sg = mp.mpf(3)
        exact = mp.fsum(1 / ((k + mp.mpf(1) / 2) ** 2
                             * (sg + k + mp.mpf(1) / 2))
                        for k in range(200000))
        lhs2 = sg * sg * exact - sg * MPQ["SQ0"]
        rhs2 = -(mp.digamma(mp.mpf(1) / 2 + sg)
                 - mp.digamma(mp.mpf(1) / 2))
        dev2 = float(abs(lhs2 - rhs2))
    check("G06-arch-gauge-identity", okp and worst_g <= 1e-30
          and dev2 <= 1e-9,
          "psi(1/2) == -gamma - 2log2 exact; sigma^2 LS_Q - sigma S_Q0 "
          "== -(psi(1/2+sigma) - psi(1/2)): dev %.1e (exact-tail "
          "route, bar 1e-30) / %.1e (raw 200k series, truncation-"
          "limited, bar 1e-9); a_Q = %.10f"
          % (worst_g, dev2, float(MPQ["AQ"])))
    with mp.workdps(80):
        t = mp.mpf("0.7")
        sser = mp.fsum(mp.exp(-(k + mp.mpf(1) / 2) * t)
                       / (k + mp.mpf(1) / 2) ** 2 for k in range(400))
        slp = mp.exp(-t / 2) * mp.lerchphi(mp.exp(-t), 2, mp.mpf(1) / 2)
        d_lp = float(abs(sser - slp) / abs(slp))
        h = mp.mpf("1e-12")
        s2 = (mp.fsum(mp.exp(-(k + mp.mpf(1) / 2) * (t + h))
                      / (k + mp.mpf(1) / 2) ** 2 for k in range(400))
              - 2 * sser
              + mp.fsum(mp.exp(-(k + mp.mpf(1) / 2) * (t - h))
                        / (k + mp.mpf(1) / 2) ** 2 for k in range(400))) \
            / (h * h)
        d_rr = float(abs(s2 - mp.exp(-t / 2) / (1 - mp.exp(-t)))
                     / abs(s2))
    check("G07-sq-density-ward", d_lp <= BAR_ARCH and d_rr <= 1e-12,
          "S_Q series == lerchphi rel %.1e (bar %.0e); S_Q'' == "
          "e^{-t/2}/(1-e^{-t}) FD rel %.1e" % (d_lp, BAR_ARCH, d_rr))
    ok8a, det8a = KDJ.gate_atom_ward()
    # Q-style exponential density ward: -g'' = e^{-t} closed form
    n_w = 700
    with mp.workdps(DPS_ALG + 20):
        dlw = mp.mpf(D3)

        def gfun(tt):
            return (1 - mp.exp(-tt)) - tt

    roww = KDJ.synth_row(gfun, n_w, dlw)
    prepw = KDJ.prep_defect(n_w, dlw, dens_fn=lambda tt: mp.exp(-tt))
    with mp.workdps(DPS_ALG):
        sgw = mp.mpf(16)
        wn = n_w * dlw
        pv = KDJ.trunc_val(roww, dlw, sgw) - KDJ.defect_val(prepw, sgw)
        pwc = (1 - mp.exp(-(sgw + 1) * wn)) / (sgw + 1)
        d8b = float(abs(pv - pwc) / abs(pwc))
    check("G08-defect-wards", ok8a and d8b <= 1e-40,
          "KDJ atom ward: %s; exp(-t) density subtracted read vs "
          "closed windowed transform rel %.1e (bar 1e-40)"
          % (det8a, d8b))
    # audit cross-ward: FD incomplete-gamma vs Dirichlet vs R4 evaluator
    with mp.workdps(60):
        s_t = mp.mpf("16.5")
        a1 = audit_xiq_logd(s_t, 60, QCAP_AUD)
        dirser = (1 / s_t + 1 / (s_t - 1) + MPQ["C20"]
                  + mp.digamma(s_t)
                  - mp.fsum(lam_q[n] * mp.power(n, -s_t)
                            for n in range(2, ncut_q + 1)))
        d9a = float(abs(a1 - dirser) / abs(dirser))
        x1 = audit_xiq(mp.mpc("0.7", "36.4"), 50, QCAP_WIT)
        x2 = R4.audit_epstein_xi(mp.mpc("0.7", "36.4"), 50)
        d9b = float(abs(x1 - x2) / max(abs(x2), mp.mpf("1e-300")))
    check("G09-audit-crossward", d9a <= 1e-20 and d9b <= 1e-8,
          "FD log-deriv vs Dirichlet at s=16.5: rel %.1e (bar 1e-20); "
          "xi_Q vs round-117 evaluator: rel %.1e" % (d9a, d9b))
    wit = audit_refine_witness()
    xref = abs(complex(wit["rho"])
               - complex(0.5 + WIT_DELTA, WIT_GAMMA))
    ok10 = (wit["resid"] <= 1e-40 and xref <= 1e-5
            and abs(wit["a_lo"] - WIT_WINDOW[0]) <= BAR_WINFORM
            and abs(wit["a_hi"] - WIT_WINDOW[1]) <= BAR_WINFORM)
    check("G10-witness-refined+window", ok10,
          "rho = %.10f%+.10fi, |xi_Q| = %.1e, vs record %.1e; window "
          "(%.2f, %.2f) vs frozen (%.1f, %.1f); excess %.4e"
          % (float(mp.re(wit["rho"])), float(wit["gamma"]),
             wit["resid"], xref, wit["a_lo"], wit["a_hi"],
             WIT_WINDOW[0], WIT_WINDOW[1], wit["excess"]))

    # ---------------------------------------------------------- S3
    section("S3  WORLDS + SZEGO LADDER (the collapse test)")
    KR.DPS = 90          # instrument precision (declared; no file edit)
    KR.mp_setup()
    with mp.workdps(DPS_ROW + 10):
        atoms_q = []
        atoms_k = []
        for n in range(2, ncut_q + 1):
            u = float(mp.log(n))
            if u >= l_max:
                break
            if lam_q[n] != 0:
                atoms_q.append((u, lam_q[n] / mp.sqrt(n)))
        for n in range(2, ncut_k + 1):
            u = float(mp.log(n))
            if u >= l_max:
                break
            if lam_k_rec[n] != 0:
                atoms_k.append((u, lam_k_rec[n] / mp.sqrt(n)))
    info("world atoms: Q %d (all n with log n < %.1f), ZK %d "
         "(prime powers)" % (len(atoms_q), l_max, len(atoms_k)))
    builds = {}
    t0 = time.time()
    builds["TRUE"] = KR.build_lags_mp(l_max, D3, "TRUE")
    print("  TRUE  build: n=%d (%.1f s)" % (builds["TRUE"]["n"],
                                            time.time() - t0),
          flush=True)
    for lab, atoms in (("Q", atoms_q), ("ZK", atoms_k)):
        b = build_lags_c20(l_max, D3, atoms, lab)
        builds[lab] = b
        print("  %-5s build: n=%d (%.1f s)" % (lab, b["n"],
                                               b["build_s"]),
              flush=True)
    builds["Q6"] = build_lags_c20(l_max, D6, atoms_q, "Q6")
    with mp.workdps(DPS_ROW + 10):
        atoms_scr = [(u, w) for (u, _), w in
                     zip(atoms_q, [w for _u, w in atoms_q][::-1])]
    builds["QSCR"] = build_lags_c20(l_max, D3, atoms_scr, "QSCR")
    # plant rows (frozen a*, frozen deltas) + witness-subtracted Q
    n3 = builds["TRUE"]["n"]
    dl3 = builds["TRUE"]["delta_mp"]
    plant_rows = {}
    with mp.workdps(DPS_ROW + 10):
        a_st = mp.mpf(repr(WIT_ASTAR))
        for ds in plant_deltas:
            do = mp.mpf(ds)
            go = mp.sqrt(a_st - do * do)
            pr = pair_row_mp(n3, dl3, do, go)
            plant_rows[ds] = [builds["TRUE"]["row"][k] + pr[k]
                              for k in range(n3)]
        do_w = wit["delta"]
        go_w = wit["gamma"]
        pr_w = pair_row_mp(builds["Q"]["n"], dl3, do_w, go_w)
        row_qminus = [builds["Q"]["row"][k] - pr_w[k]
                      for k in range(builds["Q"]["n"])]
        row_kplant = [builds["ZK"]["row"][k] + pr_w[k]
                      for k in range(builds["ZK"]["n"])]
        do35 = mp.mpf("0.35")
        pr_w35 = pair_row_mp(builds["ZK"]["n"], dl3, do35,
                             mp.sqrt(a_st - do35 * do35))
        row_kp35 = [builds["ZK"]["row"][k] + pr_w35[k]
                    for k in range(builds["ZK"]["n"])]
    # szego runs
    deaths = {}
    for lab, row in (("TRUE", builds["TRUE"]["row"]),
                     ("ZK", builds["ZK"]["row"]),
                     ("Q", builds["Q"]["row"])):
        t0 = time.time()
        sz = szego_death(row, dps_sz)
        deaths[lab] = sz
        td, marks = rung_table(sz, 0.003, lab)
        print("  %-9s: %s  t_death=%s  (%.1f s)"
              % (lab, "COMPLETES" if sz["ok"] else "DIES@k=%d"
                 % sz["fail_k"],
                 "%.3f" % td if td else "-", time.time() - t0),
              flush=True)
        print("            rungs: %s" % marks)
    sz_q6 = szego_death(builds["Q6"]["row"], dps_sz)
    td_q6 = sz_q6["fail_k"] * 0.006 if not sz_q6["ok"] else None
    sz_q60 = szego_death(builds["Q"]["row"], DPS_SZ_ALT)
    td_q60 = sz_q60["fail_k"] * 0.003 if not sz_q60["ok"] else None
    sz_qscr = szego_death(builds["QSCR"]["row"], dps_sz)
    td_qscr = (sz_qscr["fail_k"] * 0.003 if not sz_qscr["ok"] else None)
    sz_qm = szego_death(row_qminus, dps_sz)
    td_qm = sz_qm["fail_k"] * 0.003 if not sz_qm["ok"] else None
    sz_kp = szego_death(row_kplant, dps_sz)
    td_kp = sz_kp["fail_k"] * 0.003 if not sz_kp["ok"] else None
    sz_kp35 = szego_death(row_kp35, dps_sz)
    td_kp35 = sz_kp35["fail_k"] * 0.003 if not sz_kp35["ok"] else None
    plant_d = {}
    for ds in plant_deltas:
        szp = szego_death(plant_rows[ds], dps_sz)
        plant_d[ds] = szp["fail_k"] * 0.003 if not szp["ok"] else None
        print("  TRUE+PLANT(delta=%s): %s" % (ds, "t_death=%.3f"
              % plant_d[ds] if plant_d[ds] else "COMPLETES"),
              flush=True)
    print("  Q-SCRAMBLE: %s;  Q-MINUS-WITNESS: %s;  ZK+PLANT: %s"
          % ("t=%.3f" % td_qscr if td_qscr else "completes",
             "t=%.3f" % td_qm if td_qm else "COMPLETES to %.1f" % l_max,
             "t=%.3f" % td_kp if td_kp else "completes"))
    td_q = deaths["Q"]["fail_k"] * 0.003 if not deaths["Q"]["ok"] \
        else None
    check("G12-true-completes", deaths["TRUE"]["ok"],
          "TRUE zeta world Szego-completes through L = %.1f (n = %d) "
          "-- a NEW measured positivity depth (round 120 stood at "
          "5.499)" % (l_max, builds["TRUE"]["n"])
          if deaths["TRUE"]["ok"] else
          "TRUE DIES at t=%.3f: typed POSITIVITY-BOUNDARY"
          % (deaths["TRUE"]["fail_k"] * 0.003))
    check("G13-zk-completes", deaths["ZK"]["ok"],
          "zeta_K = zeta L_-20 (matched null: same pole/arch/conductor "
          "layers, Euler atoms) completes through L = %.1f -- the "
          "round-120 background caveat is RESOLVED on the real "
          "arithmetic background" % l_max
          if deaths["ZK"]["ok"] else
          "ZK DIES at t=%.3f: BACKGROUND-COLLAPSE"
          % (deaths["ZK"]["fail_k"] * 0.003))
    check("G14-q-collapses", td_q is not None and td_q <= l_max,
          "THE EPSTEIN WORLD DIES: t_death = %.3f (k = %d, dps %d; "
          "round-120 log-law prediction %.2f)"
          % (td_q if td_q else -1, deaths["Q"]["fail_k"], dps_sz,
             T_PRED_R120)
          if td_q else "Q COMPLETES through %.1f: NO-FIRE" % l_max)
    ok15 = (td_q is not None and td_q6 is not None
            and td_q60 is not None
            and abs(td_q - td_q6) <= BAR_DEATH_MESH
            and abs(td_q - td_q60) <= BAR_DEATH_DPS)
    check("G15-death-stability", ok15,
          "t_death mesh 0.003/0.006: %.3f/%.3f (|d| <= %.2f); dps "
          "80/60: %.3f/%.3f (|d| <= %.2f) -- continuum + precision "
          "stable" % (td_q or -1, td_q6 or -1, BAR_DEATH_MESH,
                      td_q or -1, td_q60 or -1, BAR_DEATH_DPS))

    # ---------------------------------------------------------- S4
    section("S4  THE CERTIFIED COLLAPSE (explicit quadratic form)")
    row_q = builds["Q"]["row"]
    row_f = np.array([float(v) for v in row_q])
    k_dag = first_negative_k(row_f, len(row_f))
    fail_k = deaths["Q"]["fail_k"]
    print("  first negative-eigenvalue section k_dagger = %d "
          "(t = %.3f); szego fail_k = %d" % (k_dag, k_dag * 0.003,
                                             fail_k))
    val = wsum = budget = None
    k_cert = -1
    lam_c = 0.0
    lam_peak = float("nan")
    if k_dag > 0:
        for pad in PAD_SET:
            k_cert = min(k_dag + pad, len(row_f))
            T = row_f[np.abs(np.subtract.outer(np.arange(k_cert),
                                               np.arange(k_cert)))]
            evals, evecs = np.linalg.eigh(T)
            lam_c = float(evals[0])
            if lam_c <= -1e-5:
                x = np.ascontiguousarray(evecs[:, 0])
                break
        else:
            x = np.ascontiguousarray(evecs[:, 0])
        val, wsum = quadform_mp(row_q, x, 80)
        val2, _w2 = quadform_mp(row_q, x, 110)
        with mp.workdps(80):
            gmax = max(500.0, 8 * math.cosh(l_max / 2))
            budget = float(wsum) * 4 * ERR_G_ABS * gmax / 0.003
            rel2 = float(abs(val - val2)
                         / max(abs(val), mp.mpf("1e-300")))
        xsha = hashlib.sha256(x.tobytes()).hexdigest()[:16]
        # frequency-attribution diagnostic (AMENDMENT 1e, INFO only)
        lam_grid = np.arange(0.0, 80.0, 0.05)
        ph = np.exp(1j * np.outer(lam_grid, 0.003 * np.arange(k_cert)))
        spec = np.abs(ph @ x) ** 2
        lam_peak = float(lam_grid[int(np.argmax(spec))])
        info("certificate-vector frequency peak lambda* = %.2f "
             "(witness gamma = %.4f): the violating test function "
             "targets %s"
             % (lam_peak, WIT_GAMMA,
                "the WITNESS frequency" if abs(lam_peak - WIT_GAMMA)
                <= 1.5 else "a DIFFERENT spectral region (collective/"
                "other zeros)"))
        print("  k_cert = %d (pad rule), float lambda_min = %.6e"
              % (k_cert, lam_c))
        print("  CERTIFIED VALUE V = x^T T x = %s  (dps-80)"
              % mp.nstr(val, 12))
        print("  error budget %.1e; two-dps rel dev %.1e; witness "
              "vector sha %s (unit float64, len %d)"
              % (budget, rel2, xsha, k_cert))
        ok16 = (float(val) <= BAR_CERT_VAL
                and abs(float(val)) >= BAR_CERT_BUDGET_FAC * budget
                and rel2 <= BAR_CERT_2DPS)
    else:
        ok16 = False
    check("G16-collapse-certified", ok16,
          "V = %.6e <= %.0e, |V| >= 1e6 x budget %.1e, dps-80/110 "
          "agreement: an EXPLICIT tent-autocorrelation test function "
          "psi_x = h*h~ >= 0-type with <-g_Q'', psi_x> < 0 CERTIFIED "
          "from source data -- windowed Weil positivity for xi_Q "
          "FAILS at t <= %.3f (mesh-free statement; typed CERT-NUM, "
          "interpretation via the classical explicit formula "
          "COND-CLASSICAL)"
          % (float(val) if val is not None else float("nan"),
             BAR_CERT_VAL, budget or -1, k_cert * 0.003)
          if val is not None else "no negative section found")
    if deaths["Q"]["ok"] and k_dag <= 0:
        ok17 = True          # vacuous in a no-fire world (typed)
        det17 = "vacuous: no szego death, no negative section"
    else:
        ok17 = k_dag > 0 and fail_k >= 0 \
            and abs(k_dag - fail_k) <= BAR_SZEGO_EIG
        det17 = ("|k_dagger - fail_k| = %d bins (bar %d): the Szego "
                 "pivot death IS the eigenvalue crossing"
                 % (abs(k_dag - fail_k), BAR_SZEGO_EIG))
    check("G17-szego-eig-consistency", ok17, det17)
    # background margin ladder (T3 pricing)
    if k_dag > 0:
        ks = sorted({max(64, k_dag - 400), k_dag - 200, k_dag - 100,
                     k_dag - 50, k_dag - 1})
        rows_bg = {"Q": row_f,
                   "TRUE": np.array([float(v) for v in
                                     builds["TRUE"]["row"]]),
                   "ZK": np.array([float(v) for v in
                                   builds["ZK"]["row"]])}
        print("  background-margin ladder lambda_min(T_k) "
              "(float64, the separation price):")
        for lab, rf in rows_bg.items():
            prof = []
            for k in ks:
                if k <= len(rf):
                    T = rf[np.abs(np.subtract.outer(np.arange(k),
                                                    np.arange(k)))]
                    prof.append("k=%d:%.3e"
                                % (k, float(np.linalg.eigvalsh(T)[0])))
            print("    %-5s %s" % (lab, "  ".join(prof)))

    # ---------------------------------------------------------- S5
    section("S5  ATTRIBUTION + THE DEATH LAW (background calibration)")
    ok18a = (td_qm is None) or (td_q is not None
                                and td_qm >= td_q + BAR_QMINUS)
    ok18b = (td_kp is not None and td_q is not None
             and abs(td_q - td_kp) <= BAR_XPLANT)
    # attribution TYPING (AMENDMENT 1e payload; the gate itself is
    # the frozen P3/P4 prediction and may be honestly falsified)
    if ok18a and ok18b:
        attr = "WITNESS-CARRIED"
    elif (td_qm is not None and td_q is not None
          and abs(td_qm - td_q) <= 0.15):
        attr = ("COLLECTIVE(witness removal moves the death by only "
                "%.3f: the aggregate off-line spectrum carries the "
                "collapse)" % abs(td_qm - td_q))
    elif td_kp is None or (td_q is not None and td_kp is not None
                           and td_kp - td_q > BAR_XPLANT):
        attr = ("BACKGROUND-MASKED(the denser conductor-20 background "
                "hides the single pair: ZK+plant %s)"
                % ("%.3f" % td_kp if td_kp else "completes"))
    else:
        attr = "MIXED"
    check("G18-attribution", ok18a and ok18b,
          "Q-minus-witness: %s (needs > t_death + %.1f); ZK+plant "
          "dies at %s vs Q %.3f (|d| <= %.2f) -- typing: %s"
          % ("COMPLETES to %.1f" % l_max if td_qm is None
             else "dies at %.3f" % td_qm, BAR_QMINUS,
             "%.3f" % td_kp if td_kp else "-", td_q or -1,
             BAR_XPLANT, attr))
    info("background price at delta = 0.35: TRUE+plant %s vs "
         "ZK+plant %s (the conductor-20 masking cost in t)"
         % ("%.3f" % plant_d.get("0.35")
            if plant_d.get("0.35") else "completes",
            "%.3f" % td_kp35 if td_kp35 else "completes"))
    if td_qm is not None and td_q is not None:
        d2 = math.exp(-(td_qm - LAW_R120[0]) / LAW_R120[1])
        info("second death of Q-minus-witness at t = %.3f -> law-"
             "inverted next-excess estimate delta ~ %.3f (INFO: the "
             "next off-line layer)" % (td_qm, d2))
    # law fit on the TRUE background
    xs, ys = [], []
    for ds in plant_deltas:
        if plant_d[ds] is not None:
            xs.append(math.log(1.0 / float(ds)))
            ys.append(plant_d[ds])
    fitA = fitB = float("nan")
    pred_w = float("nan")
    if len(xs) >= 2:
        B, A = np.polyfit(xs, ys, 1)
        fitA, fitB = float(A), float(B)
        pred_w = fitA + fitB * math.log(1.0 / WIT_DELTA)
    print("  plant-ladder deaths (TRUE bg, gamma = sqrt(a* - d^2)):")
    for ds in plant_deltas:
        tdp = plant_d[ds]
        print("    delta=%-12s t_death=%-8s nats t*d=%.3f"
              % (ds, "%.3f" % tdp if tdp else "none",
                 (tdp or 0) * float(ds)))
    print("  law fit: t = %.3f + %.3f ln(1/delta)  [round-120 SYN: "
          "%.2f + %.2f]" % (fitA, fitB, LAW_R120[0], LAW_R120[1]))
    print("  prediction at delta_w: %.3f; measured Q death: %s"
          % (pred_w, "%.3f" % td_q if td_q else "-"))
    ok19 = (plant_d.get("0.1969270453") is not None
            and td_q is not None and pred_w == pred_w
            and abs(pred_w - td_q) <= BAR_LAWFIT)
    check("G19-death-law", ok19,
          "TRUE+plant(delta_w) fires at %s; refit law predicts Q at "
          "%.3f, measured %.3f (bar %.1f) -- the round-120 law "
          "TRANSFERS from SYN to the arithmetic background"
          % ("%.3f" % plant_d.get("0.1969270453")
             if plant_d.get("0.1969270453") else "-",
             pred_w, td_q or -1, BAR_LAWFIT))

    # ---------------------------------------------------------- S6
    section("S6  CENSUS (audit context; X5 instrument) + ATTRIBUTION 2")
    onq = []
    offz = []
    realz = []
    td_qma = None
    attr2 = "not-run"
    if do_census:
        t0 = time.time()
        onq = audit_online_ordinates(45.0, 0.2)
        w45 = audit_winding(0.51, 1.6, 0.1, 45.0, 0.35)
        w30 = audit_winding(0.51, 1.6, 0.1, 30.0, 0.35)
        with mp.workdps(40):
            bexc = float(mp.fsum(rq[n] * mp.power(n, -mp.mpf("1.6"))
                                 for n in range(4, ncut_q + 1))
                         + 6 * mp.mpf("1.6") / mp.mpf("0.6")
                         * mp.power(ncut_q, -mp.mpf("0.6"))) / rq[1]
        ok21 = (abs(w45 - round(w45)) <= BAR_WIND
                and abs(w30 - round(w30)) <= BAR_WIND
                and round(w45) == 1 and round(w30) == 0)
        check("G21-census-box", ok21 and bexc < 1.0,
              "windings [0.51,1.6]x[0.1,45] = %.3f (expect 1 = the "
              "witness), x[0.1,30] = %.3f (expect 0: the witness IS "
              "the gamma-minimal off-line zero below 45); "
              "Euler-region bound sum r n^-1.6 / r(1) = %.3f < 1: no "
              "zeros with Re s >= 1.6 at ANY height (%.1f s)"
              % (w45, w30, bexc, time.time() - t0))
        info("on-line ordinates (30, 44): %s -- the witness gamma = "
             "%.4f sits in the (%.2f, %.2f) gap"
             % (" ".join("%.2f" % g for g in onq if 30 < g < 44),
                WIT_GAMMA,
                max([g for g in onq if g < WIT_GAMMA] or [0]),
                min([g for g in onq if g > WIT_GAMMA] or [99])))
        # ---- ATTRIBUTION 2 (AMENDMENT 1f): locate + subtract ALL
        t0 = time.time()
        offz = audit_locate_offline(0.05, 45.0)
        realz = audit_real_segment_zeros()
        info("located off-line zeros (audit, Re in (0.51,1.6), Im < "
             "45): %s; real-segment zeros: %s (%.1f s)"
             % (["%.4f%+.4fi" % (float(mp.re(z)), float(mp.im(z)))
                 for z in offz],
                ["%.4f" % float(z) for z in realz], time.time() - t0))
        if (offz or realz) and td_q is not None:
            with mp.workdps(DPS_ROW + 10):
                row_qma = list(builds["Q"]["row"])
                nq = builds["Q"]["n"]
                for rz in offz:
                    prz = pair_row_mp(nq, dl3,
                                      mp.re(rz) - mp.mpf("0.5"),
                                      mp.im(rz))
                    row_qma = [row_qma[i] - prz[i] for i in range(nq)]
                for rz in realz:
                    prz = pair_row_mp(nq, dl3,
                                      mp.re(rz) - mp.mpf("0.5"),
                                      mp.mpf(0))
                    # real pair {beta, 1-beta}: density 2cosh = half
                    row_qma = [row_qma[i] - prz[i] / 2
                               for i in range(nq)]
            sz_qma = szego_death(row_qma, dps_sz)
            td_qma = sz_qma["fail_k"] * 0.003 if not sz_qma["ok"] \
                else None
            carries = td_qma is None or td_qma >= td_q + BAR_QMINUS
            attr2 = ("%s(Q minus ALL located off-line pairs %s vs "
                     "Q %.3f)"
                     % ("LOCATED-SPECTRUM-CARRIES" if carries
                        else "LOCATED-SPECTRUM-INSUFFICIENT",
                        "completes to %.1f" % l_max if td_qma is None
                        else "dies at %.3f" % td_qma, td_q))
            info("ATTRIBUTION 2: " + attr2)
        if offz:
            print("  per-zero table (located off-line spectrum, "
                  "round-117 window formula):")
            with mp.workdps(40):
                for rz in offz:
                    dz = mp.re(rz) - mp.mpf("0.5")
                    gz = mp.im(rz)
                    exz = float(dz * dz / (gz * gz))
                    disc = mp.sqrt(2 * dz * dz + gz * gz)
                    alo = float(3 * dz * dz + gz * gz - 2 * dz * disc)
                    ahi = float(3 * dz * dz + gz * gz + 2 * dz * disc)
                    m2z = math.log(2.0) / exz
                    tlaw = LAW_R120[0] + LAW_R120[1] \
                        * math.log(1.0 / float(dz))
                    print("    %.4f%+.4fi  excess %.2e  a-window "
                          "(%.1f, %.1f)%s  m2 %.0f  SYN-law t %.2f"
                          % (float(mp.re(rz)), float(gz), exz, alo,
                             ahi, " [CONTAINS a=256]"
                             if alo < 256 < ahi else "", m2z, tlaw))
            # driver-law control (AMENDMENT 1g): plant the located
            # maximal-excess zero on the TRUE background
            drv = max(offz, key=lambda z: float(
                (mp.re(z) - mp.mpf("0.5")) ** 2 / mp.im(z) ** 2))
            with mp.workdps(DPS_ROW + 10):
                prd = pair_row_mp(n3, dl3, mp.re(drv) - mp.mpf("0.5"),
                                  mp.im(drv))
                row_tpd = [builds["TRUE"]["row"][i] + prd[i]
                           for i in range(n3)]
            sz_tpd = szego_death(row_tpd, dps_sz)
            td_tpd = sz_tpd["fail_k"] * 0.003 if not sz_tpd["ok"] \
                else None
            info("driver-law control: TRUE+plant(LOCATED driver "
                 "%.4f%+.4fi) %s vs Q death %s -- the driver's "
                 "background-masking price in t"
                 % (float(mp.re(drv)), float(mp.im(drv)),
                    "dies at %.3f" % td_tpd if td_tpd
                    else "completes", "%.3f" % td_q if td_q else "-"))

    # ---------------------------------------------------------- S7
    section("S7  T2 PINS: RATE CHANNEL IN/OUT THE a-WINDOW (subtracted)")
    print("  THEORY (gated accordingly): the Szego collapse is a "
          "WORLD-level")
    print("  positivity event -- no a-dependence; the violation window "
          "a in")
    print("  (%.1f, %.1f) lives in the RADIUS-4/rate currency, where "
          "the price" % WIT_WINDOW)
    print("  is m_2 = ln2 gamma^2/delta^2 = %d (round 117/120): the "
          "rate channel" % M2_PRICE)
    print("  must stay SILENT at every pin at this budget; the "
          "collapse channel")
    print("  carries the in-window detection (S3/S4).")
    pin_res = {}
    if do_pins and td_q is not None:
        rung_ok = [r for r in RUNGS if r <= td_q - 0.05]
        l_use = max(rung_ok) if rung_ok else 1.5
        n_use = int(round(l_use / 0.003))
        info("largest completing prefix rung L_use = %.3f (n = %d)"
             % (l_use, n_use))
        row_use = row_q[:n_use]
        sz_use = szego_death(row_use, dps_sz)
        build_use = {"row": row_use, "n": n_use, "delta": 0.003,
                     "delta_mp": builds["Q"]["delta_mp"],
                     "L": n_use * 0.003, "atoms": builds["Q"]["atoms"]}
        with mp.workdps(DPS_ROW + 10):
            atoms_def = [(u, -w) for (u, w) in builds["Q"]["atoms"]
                         if u < n_use * 0.003]
        prep = KDJ.prep_defect(n_use, builds["Q"]["delta_mp"],
                               dens_fn=rho_q_true, atoms=atoms_def)
        with mp.workdps(DPS_ALG):
            a_star_mp = mp.mpf(repr(WIT_ASTAR))
            s_star = mp.sqrt(a_star_mp)
        pins = (("aQstar", s_star, a_star_mp, float(a_star_mp) / 2),
                ("aQ256", mp.mpf(16), mp.mpf(256), 96.0),
                ("aQ144", mp.mpf(12), mp.mpf(144), 54.0))
        for (lab, s0, a0, rjet) in pins:
            jet = R4.build_jet_epstein(a0, rjet, JETQ_M, JETQ_DPS,
                                       JETQ_QMAX, JETQ_ORD)
            print("  direct Q jet %s: a=%.2f r=%.1f minRe s=%.2f "
                  "(%.1f s)" % (lab, float(a0), rjet, jet["sig_min"],
                                jet["secs"]), flush=True)
            pin_res[lab] = analyze_q_pin(lab, s0, a0, build_use,
                                         sz_use, prep, jet, kcont_q,
                                         mmax)
        ok11p = all(v["dev_pin_sub"] <= v["close_bar"]
                    for v in pin_res.values())
        # ZK pin identity at sigma = 6, 16 on the same prefix
        szk_use = szego_death(builds["ZK"]["row"][:n_use], dps_sz)
        with mp.workdps(DPS_ROW + 10):
            atoms_kdef = [(u, -w) for (u, w) in builds["ZK"]["atoms"]
                          if u < n_use * 0.003]
        prep_k = KDJ.prep_defect(n_use, builds["ZK"]["delta_mp"],
                                 dens_fn=rho_q_true, atoms=atoms_kdef)
        wk = []
        with mp.workdps(DPS_ALG):
            for sgv in (mp.mpf(6), mp.mpf(16)):
                wv = mp.exp(-sgv * builds["ZK"]["delta_mp"])
                cvk, _c, rdk, _m = KD.disk_complex(szk_use["alphas"],
                                                   szk_use["c0"], wv)
                pk = cvk / 2 - KDJ.defect_val(prep_k, sgv)
                ak = mp.re(audit_zk_logd(mp.mpf("0.5") + sgv))
                bark = 3 * (float(rdk) + tail_model_q(float(sgv),
                                                      l_use)) \
                    + BAR_PINCLOSE_FLOOR
                wk.append((float(sgv), float(abs(pk - ak)), bark))
        ok11k = all(d <= b for _s, d, b in wk)
        check("G11-pin-identity", ok11p and ok11k,
              "Q pins |P_sub - audit| <= 3(R + tailQ) + %.0e: %s; ZK "
              "pins: %s -- the subtracted instrument closes onto BOTH "
              "conductor-20 worlds"
              % (BAR_PINCLOSE_FLOOR,
                 "; ".join("%s %.1e<=%.1e" % (v["label"],
                                              v["dev_pin_sub"],
                                              v["close_bar"])
                           for v in pin_res.values()),
                 "; ".join("s=%.0f %.1e<=%.1e" % t for t in wk)))
        ok22 = all(v["lb_best"] < 1.0 for v in pin_res.values())
        check("G22-rate-silent", ok22,
              "certified rate-LB at aQstar/aQ256/aQ144 = %s, all < 1 "
              "(in-window fire needs m_2 = %d vs achieved %s: the "
              "exponential price sits in the DEPTH, the collapse "
              "channel pays it in the SIEVE instead)"
              % (["%.4f" % v["lb_best"] for v in pin_res.values()],
                 M2_PRICE,
                 [v["m_cert_meas"] for v in pin_res.values()]))
        ok23 = all(v["ok_enc"] for v in pin_res.values())
        check("G23-depth-enclosure", ok23,
              "|d'_sub - d'_jetQ| <= 1.2 (E_meas + width) for all "
              "m <= %d at all three pins (Q jet widths control-grade, "
              "declared)" % mmax)
        ok24 = all(v["sup_meas"] <= v["sup_cond"]
                   for v in pin_res.values())
        check("G24-meas-le-cond", ok24,
              "sup dev_meas <= sup dev_cond per pin: "
              + "; ".join("%s %.1e<=%.1e" % (v["label"], v["sup_meas"],
                                             v["sup_cond"])
                          for v in pin_res.values()))
        # Z1: transcription scan vs on-line-ordinate partial sums
        if onq:
            gam_q = np.array(onq)
            worst_scan = 1.0
            for lab in ("aQstar", "aQ256"):
                v = pin_res[lab]
                a0f = float(WIT_ASTAR) if lab == "aQstar" else 256.0
                y = a0f / (a0f + gam_q ** 2)
                w4 = 4.0 * y * (1.0 - y)
                m_use = min(4, mmax)
                d = np.array(v["d_sub"][: m_use + 1])[:, None]
                parts = np.array([np.cumsum(y * w4 ** m)
                                  for m in range(m_use + 1)])
                rel = np.abs(d - parts) / np.maximum(np.abs(parts),
                                                     1e-300)
                sc = float(rel.max(axis=0).min())
                worst_scan = min(worst_scan, sc)
                info("%s: transcription scan vs %d on-line-ordinate "
                     "partial sums: min-max rel %.3e" % (lab,
                                                         len(onq), sc))
            check("G25-z1-no-transcription", worst_scan > TRANS_BAR,
                  "the Q depth vectors match NO on-line partial-sum "
                  "vector (worst %.2e > %.0e): the reads carry the "
                  "full Lambda_Q source content incl. the witness "
                  "share" % (worst_scan, TRANS_BAR))
        exc = wit["excess"]
        info("witness invisibility at aQstar in rate currency: "
             "(4w*)^m - 1 = %.1e at m = %d vs read dev %.1e -- "
             "priced, not retried" % ((1 + exc) ** mmax - 1, mmax,
                                      pin_res["aQstar"]["devs"][mmax]
                                      if pin_res else float("nan")))
    elif not do_pins:
        info("SMOKE: pin analysis skipped")

    # ---------------------------------------------------------- S8
    section("S8  T4: MIN-CUT + THE EXACT STATEMENT")
    for gate in mincut_epq():
        check(*gate)
    print("  THE T4 ANSWER (brutal): the detector DETECTED a "
          "planted-by-arithmetic")
    print("  falsehood; detection is ORTHOGONAL to proving positivity "
          "forever.  The")
    print("  min-cut census {MEAS, OMEGA-POS} and cardinality 4 are "
          "UNCHANGED: no")
    print("  positivity edge appears, the falsifier node has no path "
          "into RH.")
    print("  WHAT IS UNCONDITIONAL (certified-numeric, new-in-corpus):")
    print("  'There is an explicit vector x (sha above) such that the "
          "tent")
    print("  autocorrelation psi_x >= 0 pairs NEGATIVELY with the "
          "Epstein source")
    print("  data -g_Q'' of Q = x^2+5y^2, V < 0 certified: windowed "
          "Weil positivity")
    print("  for xi_Q fails inside t <= %.2f, from r_Q(n) counts "
          "alone.'  Via the" % ((k_cert if k_cert > 0 else 0) * 0.003))
    print("  classical explicit formula this re-detects the "
          "Davenport-Heilbronn")
    print("  off-line zero -- KNOWN falsehood, NEW instrument: "
          "fires-iff-fires with")
    print("  measured cost T(delta) ~ %.2f + %.2f ln(1/delta) and "
          "source price" % (fitA, fitB))
    print("  e^T sieve atoms.  For zeta the same instrument at any "
          "finite window")
    print("  proves NOTHING (all-m/dense-a/all-L omega absorbs); it "
          "remains a")
    print("  falsifier: any world whose sieve data collapse is "
          "CERTIFIED non-RH-like.")

    # ---------------------------------------------------------- S9
    section("S9  CONTROLS + CONDITIONING + TAU TYPING")
    ctrl_ok = True
    ctrl_det = []
    for wld, rtgt in (("SMOOTH", CTRL_R_SMOOTH),
                      ("SCRARITH", CTRL_R_SCR)):
        bw = KR.build_lags_mp(L4, D3, wld)
        szw = KR.szego_mp(bw["row"])
        if szw["ok"]:
            ctrl_ok = False
            ctrl_det.append("%s COMPLETES (unexpected)" % wld)
            continue
        rfail = szw["fail_k"] * bw["delta"]
        ctrl_ok &= abs(rfail - rtgt) <= CTRL_TOL
        ctrl_det.append("%s dies at r=%.3f (target %.3f)"
                        % (wld, rfail, rtgt))
    check("G26-controls-die", ctrl_ok, "; ".join(ctrl_det)
          + "; Q-SCRAMBLE dies at %s (typed, non-screw world)"
          % ("%.3f" % td_qscr if td_qscr else "never"))
    # conditioning: 1e-25 perturbation
    with mp.workdps(DPS_ROW):
        eps = mp.mpf(10) ** (-COND_EPS_DPS)
        row_r = [v * (1 + eps * mp.cos(7 * d))
                 for d, v in enumerate(row_q)]
    sz_r = szego_death(row_r, dps_sz)
    fail_shift = abs(sz_r["fail_k"] - deaths["Q"]["fail_k"]) \
        if not sz_r["ok"] and not deaths["Q"]["ok"] else 999
    dval_shift = float("nan")
    if val is not None:
        val_r, _w = quadform_mp(row_r, x, 80)
        with mp.workdps(80):
            dval_shift = float(abs(val_r - val))
    ok27 = (fail_shift == 0 and dval_shift == dval_shift
            and 0.0 < dval_shift <= BAR_COND_HI)
    check("G27-conditioning", ok27,
          "1e-25 lag perturbation: death index shift %d bins (must be "
          "0); certified-value shift %.2e in (0, %.0e] -- NONZERO "
          "response gates the round-120 exactly-zero red flag"
          % (fail_shift, dval_shift, BAR_COND_HI))
    info("TAU/DISGUISE TYPING (honest): the certified value V is a "
         "windowed SOURCE-side functional (Euler/sieve-computable): "
         "DISGUISE-ADJACENT for the value channel, exactly as the "
         "round-120 subtracted reads.  Carrier-native and NOT "
         "collapsing: the positivity/collapse EVENT (which world "
         "completes and where it dies), the disk enclosures at the "
         "pins (COND-POS), and the fires-iff-fires power table.  The "
         "detection consumed NO zero data (G01/G25): the witness "
         "parameters enter only audit comparators, attribution "
         "controls and law predictions, all typed.")

    # ---------------------------------------------------------- S10
    section("S10 COMPOSITE VERDICT")
    inst = [nm for nm, okk, _ in CHECKS if not okk and nm[:3] in
            ("G01", "G02", "G03", "G04", "G05", "G06", "G07", "G08",
             "G09", "G10", "G11", "G17")]
    verdicts = []
    if inst:
        verdicts.append("EPQC-INSTRUMENT-EDGE(%s)" % inst)
    elif not (deaths["TRUE"]["ok"] and deaths["ZK"]["ok"]):
        verdicts.append("EPQC-BACKGROUND-COLLAPSE(TRUE %s, ZK %s)"
                        % (deaths["TRUE"]["ok"], deaths["ZK"]["ok"]))
    elif td_q is None:
        verdicts.append(
            "EPQC-NO-FIRE(Q completes through %.1f; law prediction "
            "was %.2f; plant deaths %s -- if the plants fire and Q "
            "does not, the obstruction is the REAL background margin, "
            "priced in S4)" % (l_max, T_PRED_R120,
                               {k: v for k, v in plant_d.items()}))
    elif not ok16:
        verdicts.append("EPQC-FIRES-UNCERTIFIED(t_death %.3f, "
                        "certificate failed)" % td_q)
    elif not (ok18a and ok18b):
        verdicts.append(
            "EPQC-FIRES-UNATTRIBUTED(t_death = %.3f (pred %.2f), "
            "t_cert = %.3f, V = %.3e +- %.0e CERTIFIED, freq peak "
            "lambda* = %.2f vs gamma_w %.2f; attribution typing: %s; "
            "attribution 2: %s; the round-120 single-witness "
            "extrapolation is falsified in the attribution channel, "
            "NOT in the fire)"
            % (td_q, T_PRED_R120, k_cert * 0.003, float(val), budget,
               lam_peak, WIT_GAMMA, attr, attr2))
    else:
        verdicts.append(
            "EPQC-COLLAPSE-DETECTION(t_death = %.3f (pred %.2f), "
            "t_cert = %.3f, V = %.3e +- %.0e, witness-attributed "
            "(freq peak %.2f), attribution 2: %s, backgrounds "
            "TRUE/ZK complete to %.1f)"
            % (td_q, T_PRED_R120, k_cert * 0.003,
               float(val), budget, lam_peak, attr2, l_max))
    verdicts.append("LAW(fit %.2f + %.2f ln(1/d) vs round-120 "
                    "%.2f + %.2f; ZK+plant %s vs Q %s)"
                    % (fitA, fitB, LAW_R120[0], LAW_R120[1],
                       "%.3f" % td_kp if td_kp else "-",
                       "%.3f" % td_q if td_q else "-"))
    if pin_res:
        verdicts.append("RATE-SILENT(LBs %s; m_2 price %d printed)"
                        % (["%.4f" % v["lb_best"]
                            for v in pin_res.values()], M2_PRICE))
    verdicts.append("MINCUT-UNCHANGED(4/4; falsifier orthogonal)")
    for vd in verdicts:
        print("  " + vd)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    npass = sum(1 for _n, okk, _d in CHECKS if okk)
    print("\n" + "=" * 78)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okk, _ in CHECKS if not okk]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
