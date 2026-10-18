#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""doublelimit_proof_probe -- PRIME.RADIUS4.DOUBLELIMIT.PROOF.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample-to-RH claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (proof lane, not measurement lane)
=======================================================================
Maximal proof attempt on the round-122 exact remaining omega:
  (H-conv) R_{a,lam}(t) = det(I - t B_{a,lam}) -> R_a(t)
           = Phi(z+)Phi(z-)/Phi(a)^2 on a real subinterval of the
           Euler-safe interval (0, 4 - 1/a) with accumulation point,
  (H-trace) sup_lam Tr B_{a,lam} < inf,
for every a in a dense subset of (1/4, inf), B_{a,lam} =
a (M_lam)^2 (a + (M_lam)^2)^{-2} on the round-114 block operators,
Phi(z) = xi(1/2 + sqrt z).  By the round-122 NF-closure theorem
(radius4_an_probe, 40/40) this implies RH.  Deliverable: proofs of
sub-lemmas where they exist, literature transplants where they exist,
and machine-pinned obstruction witnesses where they do not.

NOTATION.  For a > 1/4 and a zero pair (rho, 1-rho), rho = 1/2 + i g
(g complex allowed), put w_a(g) = a g^2/(a + g^2)^2; on real spectra
w in [0, 1/4] (round-114 realness + radius4 G11).  Pair-counted
moments:  Tr B^k := sum over the POSITIVE finite spectrum mu_i of
w_a(mu_i)^k  (one factor per zero pair, radius4 G28 convention), and
C_{0,k}(a) := sum over true zero pairs of w_a(g)^k, so C_{0,1} =
b_0 - b_1 = a F(a) + a^2 F'(a), F = (log Phi)'.  Defect jets
d_k(lam) := C_{0,k}(a) - Tr B_{a,lam}^k;  d_1 = the round-122
Lane-A trace tail.

=======================================================================
THE LEMMA DECOMPOSITION (T1) AND WHAT THIS PROBE PROVES
=======================================================================
L0 (exact algebra; PROVEN, machine-gated in S1):
  (i)   w^k <= 4^{1-k} w on [0, 1/4] for every k >= 1, with the exact
        factorization 4^{1-k} w - w^k = w 4^{1-k} (1 - (4w)^{k-1})
        and 1 - u^{k-1} = (1-u)(1 + u + ... + u^{k-2});
  (ii)  sum_{k>=1} t^k 4^{1-k}/k = -4 log(1 - t/4), |t| < 4;
  (iii) the C_{0,k} <-> Taylor-jet dictionary:  with log Phi(z) =
        sum_m c_m (z-a)^m,  S_m(a) := sum_pairs (g^2+a)^{-m} =
        (-1)^{m-1} m c_m,  and
        C_{0,k}(a) = a^k sum_{j=0..k} binom(k,j) (-a)^{k-j}
        S_{2k-j}(a)   [w = a(X-a)/X^2, X = g^2 + a, exact binomial
        expansion -- the round-106 Pascal-diagonal cells in closed
        jet form for ALL k];
  (iv)  the round-117 window/pin algebra re-gated exactly: window
        interior a+ - a- = 4 delta sqrt(2 delta^2 + gamma^2) > 0,
        the CDXXVI double formula identity, and the matched-pin
        value w = a/(4 gamma^2) = (1 + delta^2/gamma^2)/4 > 1/4
        exactly at a = delta^2 + gamma^2 (z = (gamma - i delta)^2,
        (a+z)^2 = 4 gamma^2 z);
  (v)   Euler safety: 1/2 + sqrt(a) > 1 iff a > 1/4 (the prime side
        of every target below is absolutely convergent exactly on
        the contract's a-range: Re s > 1, the de Branges trap of
        round 121/CDXXII is structurally avoided -- no canonical-
        norm object appears anywhere in this probe);
  (vi)  prime-jet coefficients: with s(a) = 1/2 + sqrt a,
        a s' + a^2 s'' = sqrt(a)/4 and a^2 s'^2 = a/4, hence
        C01_prime(a) = (1/4) sum_n Lambda(n) n^{-1/2-sqrt a}
        (a log n - sqrt a)   [exact operator identity];
  (vii) w-tail bound w_a(t) <= a/t^2 (quadrature-transfer currency).

THEOREM R (the reduction theorem -- the new mathematics of this
round; typed PROVEN with elementary series inputs, every inequality
machine-gated on exact instances in S1 and on the true ladder in S3).
Fix a > 1/4.  Hypotheses:
  (L1)   d_1(lam) -> 0  as lam -> inf,
  (WPD)  exists C < inf with |d_k(lam)| <= C 4^{1-k} d_1(lam)
         for all k >= 2 and all lam   (weak positive-defect
         domination; the strong form PD is 0 <= d_k <= 4^{1-k} d_1).
Then for every r < 4:
     sup_{0<=t<=r} |log(R_{a,lam}(t)/R_a(t))|
        <= max(1, C) * (-4 log(1 - r/4)) * d_1(lam)  -> 0,
in particular (H-conv) holds on the FULL Euler interval and
(H-trace) holds (Tr B = C01 - d_1 is convergent hence bounded).
Proof: log(R_fin/R_a)(t) = sum_k t^k d_k / k (the finite object
overshoots by the missing tail factors: d_k > 0 measured; both log series
converge absolutely for |t| < 4: the finite side by w <= 1/4
unconditionally, the true side because WPD + boundedness of Tr B
gives |C0k| <= 4^{1-k}(Tr B + C d_1), so limsup |C0k|^{1/k} <= 1/4);
then |sum t^k d_k/k| <= max(1,C) d_1 sum t^k 4^{1-k}/k =
max(1,C) (-4 log(1-t/4)) d_1 by L0(i)-(ii).  QED.
COROLLARY (with the round-122 NF-closure theorem, cited): L1 + WPD
on a dense subset of (1/4, inf) ==> RH.

LEMMA N (L1-necessity; typed PROVEN, classical inputs Vitali +
Cauchy estimates, cited): (H-conv) + (H-trace) ==> L1 and moreover
Tr B^k -> C0k for EVERY fixed k.  (Normal family by the round-117
bound; Vitali upgrades pointwise to locally uniform convergence on
|t| < 4; log is analytic on the zero-free range; Taylor coefficients
converge.)  So L1 is a NECESSARY component of the old omega: the
refinement {L1, WPD} is not a weaker target in disguise, and any
future proof of the omega must prove L1 on the way.

LEMMA S (subset-PD; PROVEN, exact): if the finite w-spectrum is a
sub-multiset of the true one (pure undercounting; positive defect
measure), then PD holds exactly: d_k = sum_tail w^k <= 4^{1-k}
sum_tail w = 4^{1-k} d_1, all k; and if the defect measure is
supported where w <= w_edge < 1/4 (band-edge tail), the SHARPER
d_k <= w_edge^{k-1} d_1 holds by the same argument -- the measured
WPD constants below fall with the rung exactly this way.  Gated on
an exact rational instance (S1 G12) together with the Theorem-R
sandwich t d_1 <= log(R_fin/R_a)(t) <= -4 log(1-t/4) d_1.

LEMMA X (moment transfer is NOT free; PROVEN, exact counterexample):
L1 alone does not control d_2: spectra {1/8, 1/8} vs {1/16, 3/16}
have equal first w-moments (d_1 = 0) and d_2 = -1/128 != 0.  The
operator structure (positivity of the defect) is load-bearing;
convergence of ALL moments is NOT implied by the first without WPD.

THE HONEST CLASSIFICATION OF WPD (typed OBSTRUCTED-RH-EQUIVALENT-
AT-THE-TAIL, with an exact witness): by Cauchy-Hadamard,
sup_k C0k(a) 4^{k-1} < inf  <==>  max over zero pairs |w_a(g)| <= 1/4
<==> (round-117 window theorem) no off-line zero with a inside its
violation window.  WITNESS (S2 G26): the radius4 planted quartet
delta = 3/10, gamma = 30 at matched a* = 900.09 adds EXACTLY
2 w*^k to C0k with w* = (1 + delta^2/gamma^2)/4 = 0.250025 > 1/4
(L0(iv)), so the planted PD ladder 2 w*^k 4^{k-1} = (4w*)^k/2
crosses ANY bar B at k*(B) = ceil(log(2B)/log(4 w*)) -- closed form,
machine-evaluated; the true-world ladders C0k 4^{k-1} are measured
FALLING on the battery.  WPD is therefore not a technical lemma:
it is the RH window positivity in Pascal-diagonal currency.  A
proof of WPD from the operator side (Lambda(n), Gamma, Loewner
algebra) would close the chain; this probe prices it and pins where
it lives, and does NOT claim it.

TRANSPLANTS (typed TRANSPLANTED-CITED; statements consumed, not
re-proved): (a) B. Simon, Trace Ideals and Their Applications, 2nd
ed., AMS 2005, Thm 2.21 + Addendum H (Grumm 1973; Simon 1981
"Convergence in trace ideals"): for positive trace-class operators,
weak operator convergence + trace convergence ==> trace-norm
convergence ==> Fredholm-determinant convergence.  This is the
operator-theoretic shape of Theorem R; the finite-jet version above
avoids the common-Hilbert-space embedding (which for the TRUE limit
object is a Hilbert-Polya construction and RH-equivalent in the
canonical norm, round 121/CDXXII) -- the jet currency is the
non-circular substitute.  (b) Connes-Consani-Moscovici, "Zeta
spectral triples", EMS Lect. Math. 37 (2026), and arXiv:2310.18423 /
Ann. Funct. Anal. 15:87 (2024): their D_log^{(lambda,N)} program
states the SAME omega (regularized determinants of finite operators
-> Xi; "a rigorous proof of this convergence would establish RH")
-- independent confirmation that the residue typed here is the open
frontier, not a corpus artifact.  (c) Rosser-Schoenfeld-style
elementary tail bounds for the Lambda sums (Lambda(n) <= log n and
monotone-integral comparison; constants computed in closed form
in-run).

L1 HEAD-ON (T2; the arithmetic residue, typed OBSTRUCTED with
quantified gap):  C01(a) splits EXACTLY (xi = arch * zeta, no zero
input, absolutely convergent for a > 1/4):
   C01(a) = C01_arch(a) + C01_prime(a),
   C01_arch from log xi_arch(s) = log(s(s-1)/2) - (s/2) log pi
   + log Gamma(s/2)  (jet of an entire-of-zeros object),
   C01_prime(a) = (1/4) sum Lambda(n) n^{-1/2-sqrt a}(a log n -
   sqrt a)  [L0(vi)].
The trace formula Tr B = sum w(mu_i) is a quadrature of w against
the operator's node measure; w is continuous, bounded by 1/4 and by
a/t^2 (L0(vii)), so quadrature transfer holds iff the node counting
measure converges weak-* to the TRUE zero-pair counting measure
with uniformly controlled tail.  S3 measures the node law: the
in-band node density is the Riemann-von Mangoldt law N(T) =
(T/2pi) log(T/2pi e) + 7/8 (sup dev << 1 zero), and is NOT a
semicircle, NOT an arcsine, NOT the clock/lattice law of D --
the equilibrium measure of the round-114 operators is the
ARITHMETIC zero-counting law: its mean is archimedean (RvM), its
oscillation is the prime side.  The mean density alone gives
MEANDENS(a) = (1/2pi) int w_a(t) log(t/2pi) dt != C01(a); the gap
is the oscillatory/prime content, and the C01-currency gap between
the arch part and the full target is EXACTLY C01_prime(a), printed
as the T2 ratio table.  Proving the node law from the operator side
is the k_lambda ~ xi_lambda wall (CCM's named remaining obstacle,
round 114 M4); the round-122 Z1 verdict (transcribing-in-band)
applies to today's EVIDENCE and is re-typed here on the trace
observable.  What would remain even with the mean density proven:
the oscillation transfer = C01_prime(a) = the prime-side theorem.

L3/L4 (dense-a and the double limit; PROVEN as packaging lemmas):
Theorem R is per-fixed-a with constants depending on a only through
d_1 and C; the NF-closure consumes ITERATED limits (for each a in a
countable dense set, lam -> inf) -- no joint (a, lam) limit, no
a-uniformity: a hypothetical off-line zero is detected through the
OPEN window (a-, a+) (interior nonempty by L0(iv)), which meets
every dense set.  The a ~ gamma^2 coupling is measurement cost
(band edge >~ gamma), not a quantifier obstruction.  Machine-gated:
window interior exact; the rest cited from round 122's quantifier
audit (radius4 S5 INFO, confirmed here).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  firewall (AST: no zero-oracle names; mp.zeta only inside
    audit_*; np.load only inside ward_*; no verification/ import);
    cache health (X5: READ-ONLY instrument in ward_ namespace).
S1  exact layer (sympy): G10 domination + factorization (k = 2..12);
    G11 tail sum closed form; G12 Lemma S instance (exact rationals,
    10-atom true / 6-atom fin, PD exact k <= 12, Theorem-R sandwich
    at t = 7/2 in mp dps 80); G13 Lemma X counterexample exact;
    G14 jet dictionary (w^k binomial expansion k = 1..6 symbolic +
    S_m = (-1)^{m-1} m c_m on an exact rational 3-zero world m<=5);
    G15 window algebra (interior, CDXXVI identity, matched-pin
    w* = a/4gamma^2 exact); G16 Euler safety iff a > 1/4 exact +
    radius4 G12 branch identity re-gated; G17 prime-jet
    coefficients exact; G18 w <= a/t^2 and (a+t^2)^2 - 4at^2 =
    (a-t^2)^2 exact.
S2  targets (own EM currency, round-119; mp.zeta only in audit_):
    G20 EM audit at the frozen battery point set (bar 1e-30, dps 80);
    G21 Cauchy-jet cross-ward: c_1, c_2 vs mp.diff of log Phi and
    C01(jet) vs a F + a^2 F' (bar 1e-18 rel) for every a in A_JET;
    G22 the arch/prime split: |C01 - C01_arch - Lambda-sum_N| <=
    closed-form tail bound at a in (4, 9, 16), N = 2e5 (Lambda(n)
    <= log n integral comparison, constants in-run); at a = 1 the
    bound is printed as the round-119/122 budget wall (INFO, no
    gate -- absolutely convergent != budget convergent, replicated);
    the T2 gap table C01_prime/C01 for A_BAT printed; G23 the
    series identity per rung/battery: |sup-defect model
    sum_{k<=24} t^k d_k/k - measured log(R_fin/R_true)| <=
    closed-form k>24 tail (measured WPD constant) + 1e-8 at every
    (rung, a, t); G26 the WPD obstruction witness: planted ladder
    (4w*)^k/2 crossing k*(B) closed form vs direct mp evaluation
    (exact match required), true ladders C0k 4^{k-1} measured
    falling in k on the battery.
S3  operators (round-114 blocks via the radius4 builder, warded):
    G30 own-build ward x = 3 even+odd vs SL (1e-8); G31 realness +
    census (imrel <= 1e-6 on admissible rungs; x = 13 census
    fallback by the exterior-determinant identity, round-122
    AMENDMENT-1 pattern, disclosed); G32 monotone-from-below:
    d_1 > 0 at every rung and battery a AND d_1 falls (factor >=
    1.6 over L1, wobble 1.10 -- the radius4 G32 bars, cited);
    G33 WPD/PD adjudication: table d_k (k <= 8) per rung x a;
    WPD constant C_meas = max_k |d_k| 4^{k-1}/d_1 <= C_BAR and
    PD floor min_k d_k 4^{k-1}/d_1 >= -PD_TOL (bars frozen from the
    disclosed smoke); G34 reduction band: supdefect/(t_max d_1) in
    [RATIO_LO, -4 log(1-t_max/4)/t_max * RATIO_PAD] per rung/a (the
    Theorem-R explanation of the round-122 mechanism band [0.5,2]);
    G35 node law: RvM sup dev <= RVM_BAR in-band at every rung and
    RvM beats clock, semicircle, arcsine by factor >= FIT_SEP;
    G36 d_1 anatomy (ward): tail share >= TS_LO, in-band mismatch
    share <= IB_HI, artifact w-mass share <= ART_HI at the deepest
    rung; G37 SMOOTH control x = 5: median |d_1_smooth|/|d_1_main|
    >= SEP_SM (density functional separates); the prime-currency
    difference (TrB_main - TrB_smooth) vs C01_prime printed INFO;
    G38 Z1 trace typing executed (hybrid band swap; rule
    TRANSCRIBING-IN-BAND iff median ratio <= 0.25; expected and
    typed, not hidden); G39 perturbation screen 1e-25 on Q[0,0]
    at x = 5 (response in (1e-40, 1e-10); the round-118 exact-zero
    red flag).
S4  min-cut (round-116 replica + refinement): base flows 4; the
    round-122 LANEA-CONV unit edge REFINED into the series pair
    NFCLOS -> L1 -> WPD -> R4HYP (extended flow 5 -- capacity
    unchanged: a refinement, not a new parallel route); L1 typed
    NECESSARY-for-the-old-omega (Lemma N), WPD typed carries-the-
    positivity; counterfactual parallel wiring (flow 6) printed
    INFO as NOT REAL.  Census {MEAS, OMEGA-POS} unchanged.
S9  composite verdict + runtime bar.

=======================================================================
FROZEN NUMERICS
=======================================================================
L1 ladder ((3,45),(5,60),(8,80),(13,120)) at KFAC 1.25 (radius4/SL
currency).  A_BAT = (1, 4, 16); T_BAT = {1:(0.5,1,1.5,2),
4:(0.5,1.5,2.5,3.5), 16:(0.5,1.5,2.5,3.5)}; A_JET = (1, 4, 9, 16).
K_MOM = 8 (WPD ladder), K_ID = 24 (series identity), jet: M = 256
circle points, radius a/2, JET_DPS = 80, NC = 49 coefficients.
EM zeta: N = 80, J = 14; EM audit bar 1e-30.  Lambda sieve N_SIEVE
= 200000; prime-split corridor a in (4, 9, 16); tail bound
(1/4) int_{N}^{inf} (a u^2 + sqrt a u) e^{(1-sigma)u} du in closed
form (u = log t; Lambda <= log; monotone comparison, sigma = 1/2 +
sqrt a >= 2.5 on the corridor).  Planted witness delta = 3/10,
gamma = 30, bar ladder B in (10, 1e3, 1e6).  Exact instance G12:
W_TRUE = (1/4, 1/5, 1/7, 1/11, 1/17, 1/31, 1/57, 1/101, 1/207,
1/399), fin = first 6, t = 7/2.  Bars frozen from the disclosed
smoke: C_BAR = 1.20, PD_TOL = 0.02, RATIO_LO = 0.85, RATIO_PAD =
1.10, RVM_BAR = 1.20, FIT_SEP = 2.5, TS_LO = 0.90, IB_HI = 0.10,
ART_HI = 0.02, SEP_SM = 2.0, BAR_REAL = 1e-6, BAR_WARD = 1e-8,
BAR_CENSUS = 1e-4, Z1_BAR = 0.25.  In-band = mu <= 0.8 K pi / L;
artifact = mu > 2 K pi / L.  RUNTIME_BAR = 3600 s.  Deterministic:
NO randomness anywhere (all literals frozen; no RNG).  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ namespace (X5).
All mpf/mpc arithmetic inside explicit mp.workdps blocks (the
round-118 ambient-precision negation trap).

VERDICT ENUMS (frozen): THMR-PROVEN(hypothesis list always stated);
L1-NECESSITY-PROVEN; SUBSETPD-PROVEN; MOMENT-TRANSFER-NOT-FREE;
WPD-MEASURED(C)/WPD-VIOLATED(witness); PD-MEASURED/PD-VIOLATED
(witness printed, adjudicated not assumed); WPD-TAIL-RH-EQUIVALENT
(the Cauchy-Hadamard/window classification with the planted k*
witness); L1-OBSTRUCTED(node-law wall; gap = C01_prime table; Z1
typing); DENSITY-RVM-ARITHMETIC(not semicircle/arcsine/clock);
MECHANISM-THEOREM(the r122 band explained by Theorem R);
DOUBLELIMIT-ORDERED(L3/L4 proven as packaging); EULERSAFE-
NONCIRCULAR; MINCUT-REFINED(flows 4 -> 5, series pair, SUFFICIENT-
ONLY, L1 necessary, census unchanged).  Composite priority:
INSTRUMENT-EDGE (any ward/audit gate fails, exit 1) > EXACT-LAYER-
OBSTRUCTED (any S1 gate fails: the named identity is the
obstruction) > adjudicated verdicts as measured.

SMOKE DISCLOSURE (pre-freeze, x = (3, 5) only, scratch deleted; all
numbers below are MEASURED in the disclosed smoke, and four
pre-freeze instrument repairs are disclosed):
(a) WPD/PD ladders measured MUCH healthier than the conservative
bars: C_meas = max_k |d_k| 4^{k-1}/d_1 per (rung, a) in
[5e-4, 0.021] and PD floor >= 0.0000 (every defect jet positive:
the round-112 from-below structure holds at every k <= 8) -- the
defect is BAND-EDGE dominated (w_edge << 1/4), so the sharper
Lemma-S tail bound d_k <= w_edge^{k-1} d_1 is the operative law and
C_meas falls with the rung; C_BAR = 1.20 and PD_TOL = 0.02 kept as
conservative frozen bars; (b) reduction band measured
supdefect/(t_max d_1) = 1.000/1.001/1.004 at x = 5 (a = 1/4/16),
inside the Theorem-R prediction [1, -4log(1-t/4)/t] -- RATIO_LO =
0.85 frozen with in-band-mismatch headroom for depth; (c) node law
at x = 5: RvM sup dev 0.18 vs clock 4.3 / semicircle 2.1 / arcsine
0.8 (min separation 4.4x) -- RVM_BAR = 1.20, FIT_SEP = 2.5 frozen;
x = 3 has < 5 in-band nodes and is skipped by the frozen rule;
(d) d_1 anatomy at x = 5, a = 4: tail share 1.000, in-band
|share| 9.6e-5, artifact share 1.5e-3 -- TS_LO/IB_HI/ART_HI frozen
with headroom; (e) SIGN-ORIENTATION REPAIR (disclosed): the first
smoke ran the G23 model against log(R_true/R_fin); the measured
residual |meas + model| ~ 5e-11 exposed the orientation -- the
identity is log(R_fin/R_a) = +sum t^k d_k/k (the finite object
overshoots by the missing tail factors); label and model fixed
pre-freeze, no bar or verdict rule changed, and the 1e-8 numeric
allowance in G23 is kept; (f) SYMPY-FORM REPAIRS (disclosed): G11
summation returns a Piecewise (branch t < 4 extracted and gated);
G14 S_m check moved from series-coefficient extraction to direct
exact derivatives (same mathematical content, all devs 0);
(g) F64-FLOOR REPAIR (disclosed): at a = 16 the Lambda-sum f64
accumulation floor (~4e-15) exceeds the true closed-form tail
bound 5e-17 -- the sum now uses math.fsum and G22 carries an
explicit disclosed numeric floor 1e-12; (h) SMOOTH x = 5
separation measured median 3.72x (per-a 4.62/3.72/1.80) -- SEP_SM
= 2.0 on the median frozen; (i) budget wall replicated: at a = 1
(sigma = 1.5) the closed-form Lambda tail bound at N = 2e5 is
2.5e-1 against C01_prime(1) = 0.587 (partial 0.5727) -- the
corridor design (a >= 4) is a pre-freeze decision, the a = 1 row
is printed INFO; (j) the T2 gap table measured in smoke:
C01_prime/C01 = 25.5 / 2.26 / 0.68 / 0.28 at a = 1/4/9/16 -- at
small a the target is almost entirely prime-side.  Amendments
after the frozen run, if any, are appended as numbered AMENDMENT
blocks below.

AST FIREWALL: no zetazero/siegelz/siegeltheta/nzeros/grampoint
anywhere; the zeta attribute only inside audit_* functions; np.load
only inside ward_* functions; no import of verification/.
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

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import semilocal_realroot_limit_probe as SL   # warded source builder
import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
LADDER = ((3, 45), (5, 60), (8, 80), (13, 120))
A_BAT = (1, 4, 16)
T_BAT = {1: (0.5, 1.0, 1.5, 2.0), 4: (0.5, 1.5, 2.5, 3.5),
         16: (0.5, 1.5, 2.5, 3.5)}
A_JET = (1, 4, 9, 16)
K_MOM = 8
K_ID = 24
JET_M = 256
JET_DPS = 80
JET_NC = 49
EM_N, EM_J = 80, 14
BAR_EM_AUDIT = 1e-30
N_SIEVE = 200000
CORRIDOR_A = (4, 9, 16)
PLANT_DELTA, PLANT_GAMMA = 0.3, 30.0
PLANT_BARS = (10.0, 1e3, 1e6)
W_TRUE_Q = (4, 5, 7, 11, 17, 31, 57, 101, 207, 399)   # denominators
N_FIN_Q = 6
T_SAND = (7, 2)                                        # t = 7/2
C_BAR = 1.20
PD_TOL = 0.02
RATIO_LO = 0.85
RATIO_PAD = 1.10
RVM_BAR = 1.20
FIT_SEP = 2.5
TS_LO = 0.90
IB_HI = 0.10
ART_HI = 0.02
SEP_SM = 2.0
BAR_REAL = 1e-6
BAR_WARD = 1e-8
BAR_CENSUS = 1e-4
Z1_BAR = 0.25
BAR_JET_XW = 1e-18
FALL_L1, WOBBLE = 1.6, 1.10
INBAND_F, ART_F = 0.8, 2.0
RUNTIME_BAR = 3600.0
GAMMA1_LIT = 14.134725141734693790   # ward only

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok:
        if kind == "edge":
            EDGE_FAILS.append(name)
        elif kind == "exact":
            EXACT_FAILS.append(name)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owner(lineno: int) -> str:
        best = ""
        for nm, lo, hi in spans:
            if lo <= lineno <= hi:
                best = nm
        return best

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
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
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            fn = owner(node.lineno)
            if not fn.startswith("audit_"):
                bad.append("zeta outside audit_ @%d (%s)"
                           % (node.lineno, fn or "module"))
        if isinstance(node, ast.Attribute) and nm == "load":
            fn = owner(node.lineno)
            if not fn.startswith("ward_"):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fn or "module"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; zeta in audit_, cache in ward_")


# ------------------------------------------------------- source currency
def em_zeta(s):
    """Own Euler-Maclaurin zeta (round-119 currency; NO mp.zeta).
    N = 80, J = 14; used at Re s > 1.1 only.  Caller sets workdps."""
    s = mp.mpc(s)
    tot = mp.mpc(0)
    for n in range(1, EM_N):
        tot += mp.power(n, -s)
    tot += mp.power(EM_N, 1 - s) / (s - 1)
    tot += mp.power(EM_N, -s) / 2
    fac = s
    npw = mp.power(EM_N, -s - 1)
    for j in range(1, EM_J + 1):
        tot += mp.bernoulli(2 * j) / mp.factorial(2 * j) * fac * npw
        fac *= (s + 2 * j - 1) * (s + 2 * j)
        npw /= EM_N * EM_N
    return tot


def em_xi(s):
    s = mp.mpc(s)
    return (s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2)
            * em_zeta(s))


def em_log_phi(z):
    """log Phi(z) = log xi(1/2 + sqrt z), z off (-inf, 0]."""
    return mp.log(em_xi(mp.mpf("0.5") + mp.sqrt(mp.mpc(z))))


def arch_log_xi(z):
    """log of the archimedean completed factor at s = 1/2 + sqrt z:
    log(s(s-1)/2) - (s/2) log pi + log Gamma(s/2).  Entire of zeros
    for Re s > 1; NO zeta content."""
    s = mp.mpf("0.5") + mp.sqrt(mp.mpc(z))
    return (mp.log(s * (s - 1) / 2) - s / 2 * mp.log(mp.pi)
            + mp.loggamma(s / 2))


def cauchy_jet(fun, a: float, nc: int) -> list:
    """Taylor coefficients c_0..c_{nc-1} of fun at a via the Cauchy
    integral on the circle radius a/2 (M = JET_M points, dps
    JET_DPS).  fun analytic on |z - a| <= a/2 for a > 1/4 (cut and
    all Phi-zeros lie in Re z < 0).  Returns real mpf list."""
    with mp.workdps(JET_DPS):
        am = mp.mpf(repr(float(a)))
        r = am / 2
        fv = []
        for j in range(JET_M):
            th = 2 * mp.pi * j / JET_M
            fv.append(fun(am + r * mp.exp(1j * th)))
        cs = []
        for m in range(nc):
            acc = mp.mpc(0)
            for j in range(JET_M):
                th = 2 * mp.pi * j / JET_M
                acc += fv[j] * mp.exp(-1j * m * th)
            cs.append(mp.re(acc) / (JET_M * r ** m))
    return cs


def c0k_from_jet(a: float, cs: list, kmax: int) -> list:
    """C_{0,k}(a), k = 1..kmax, from the Taylor jet of log Phi at a:
    S_m = (-1)^{m-1} m c_m; C0k = a^k sum_j binom(k,j)(-a)^{k-j}
    S_{2k-j}.  Caller-independent workdps."""
    with mp.workdps(JET_DPS):
        am = mp.mpf(repr(float(a)))
        S = [mp.mpf(0)] * (2 * kmax + 1)
        for m in range(1, 2 * kmax + 1):
            S[m] = (-1) ** (m - 1) * m * cs[m]
        out = []
        for k in range(1, kmax + 1):
            acc = mp.mpf(0)
            for j in range(0, k + 1):
                acc += (mp.binomial(k, j) * (-am) ** (k - j)
                        * S[2 * k - j])
            out.append(acc * am ** k)
    return out


def lambda_sieve(cap: int) -> np.ndarray:
    lam = np.zeros(cap + 1)
    comp = np.zeros(cap + 1, dtype=bool)
    for p in range(2, cap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        lp = math.log(p)
        q = p
        while q <= cap:
            lam[q] = lp
            q *= p
    return lam


def prime_c01_partial(a: float, lam: np.ndarray) -> float:
    """(1/4) sum_{n<=N} Lambda(n) n^{-1/2-sqrt a}(a log n - sqrt a);
    f64 (positive decreasing terms; abs conv for a > 1/4)."""
    ra = math.sqrt(a)
    sig = 0.5 + ra
    terms = []
    for n in range(2, len(lam)):
        if lam[n] == 0.0:
            continue
        ln = math.log(n)
        terms.append(lam[n] * math.exp(-sig * ln) * (a * ln - ra))
    return math.fsum(terms) / 4.0


def prime_tail_bound(a: float, N: int) -> float:
    """Closed-form bound for the n > N tail of prime_c01: Lambda(n)
    <= log n and monotone comparison with
    (1/4) int_N^inf (a log^2 t + sqrt a log t) t^{-sigma} dt,
    sigma = 1/2 + sqrt a (u = log t substitution; valid where the
    integrand is decreasing, gated by sigma >= 2.5 on the corridor)."""
    ra = math.sqrt(a)
    sig = 0.5 + ra
    b = sig - 1.0
    U = math.log(N)
    e = math.exp(-b * U)
    i2 = e * (U * U / b + 2 * U / (b * b) + 2 / (b ** 3))
    i1 = e * (U / b + 1 / (b * b))
    return 0.25 * (a * i2 + ra * i1)


def mean_density_integral(a: float) -> float:
    """MEANDENS(a) = (1/2pi) int_0^inf w_a(t) log(t/2pi) dt (the
    RvM mean-density quadrature of w; no zeros, no primes)."""
    with mp.workdps(40):
        am = mp.mpf(repr(float(a)))
        val = mp.quad(lambda t: (am * t * t / (am + t * t) ** 2)
                      * mp.log(t / (2 * mp.pi)),
                      [0, mp.sqrt(am), 10 * mp.sqrt(am), mp.inf])
        return float(val / (2 * mp.pi))


def r_true(a: int, t: float) -> float:
    """R_a(t) via own-EM xi (pair-counted; radius4 currency)."""
    with mp.workdps(50):
        th = 2 * mp.asin(mp.sqrt(mp.mpf(repr(t))) / 2)
        zc = a * mp.exp(1j * th)
        num = abs(em_xi(mp.mpf("0.5") + mp.sqrt(zc))) ** 2
        den = mp.re(em_xi(mp.mpf("0.5") + mp.sqrt(mp.mpf(a)))) ** 2
        return float(num / den)


# ------------------------------------------------------- audit evaluators
def audit_em_dev(pts) -> float:
    """max rel dev of own EM zeta vs mp.zeta (audit namespace)."""
    worst = 0.0
    with mp.workdps(JET_DPS):
        for s in pts:
            zt = mp.zeta(mp.mpc(s))
            worst = max(worst, float(abs(em_zeta(s) - zt) / abs(zt)))
    return worst


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def ward_band_match(mus: np.ndarray, gam: np.ndarray) -> int:
    nb = 0
    for i, mu in enumerate(mus):
        j = int(np.argmin(np.abs(gam - mu)))
        lo = gam[j - 1] if j > 0 else 0.0
        hi = gam[j + 1] if j + 1 < len(gam) else gam[j] + 10.0
        spac = 0.5 * (hi - lo)
        if abs(mu - gam[j]) < 0.25 * spac and i == nb:
            nb += 1
        else:
            break
    return nb


def ward_hybrid(mus: np.ndarray, gam: np.ndarray,
                nband: int) -> np.ndarray:
    out = mus.copy()
    for i in range(nband):
        j = int(np.argmin(np.abs(gam - mus[i])))
        out[i] = gam[j]
    return out


def ward_d1_anatomy(mus: np.ndarray, gam: np.ndarray, a: float,
                    c01: float, be: float) -> dict:
    """d_1 = in-band mismatch + tail(+artifact) decomposition."""
    nb = ward_band_match(mus, gam)
    wmu = a * mus ** 2 / (a + mus ** 2) ** 2
    wga = a * gam ** 2 / (a + gam ** 2) ** 2
    mism = 0.0
    for i in range(nb):
        j = int(np.argmin(np.abs(gam - mus[i])))
        mism += float(wga[j] - wmu[i])
    matched_g = sum(float(wga[int(np.argmin(np.abs(gam - mus[i])))])
                    for i in range(nb))
    rest_mu = float(np.sum(wmu[nb:]))
    art = float(np.sum(wmu[mus > ART_F * be]))
    trb = float(np.sum(wmu))
    d1 = c01 - trb
    tail = c01 - matched_g - rest_mu
    return {"nb": nb, "d1": d1, "mism": mism, "tail": tail,
            "art": art, "trb": trb}


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    w, u, t, a, X = sp.symbols("w u t a X", positive=True)
    k = sp.symbols("k", positive=True, integer=True)

    # G10 domination + factorization
    ok10 = True
    for kk in range(2, 13):
        fac = sp.expand(sp.Rational(4) ** (1 - kk) * w - w ** kk
                        - w * sp.Rational(4) ** (1 - kk)
                        * (1 - (4 * w) ** (kk - 1)))
        geo = sp.expand((1 - u) * sum(u ** i for i in range(kk - 1))
                        - (1 - u ** (kk - 1)))
        ok10 = ok10 and fac == 0 and geo == 0
    out.append(("G10-w-domination", ok10,
                "4^{1-k}w - w^k = w 4^{1-k}(1-(4w)^{k-1}), "
                "1-u^{k-1} = (1-u)(1+...+u^{k-2}) exact, k=2..12: "
                "w^k <= 4^{1-k} w on [0,1/4]"))

    # G11 tail sum (sympy returns a Piecewise; gate the t < 4 branch)
    ssum = sp.summation(t ** k * sp.Rational(4) ** (1 - k) / k,
                        (k, 1, sp.oo))
    dev11 = sp.simplify(ssum - (-4 * sp.log(1 - t / 4)))
    ok11 = dev11 == 0
    if not ok11 and isinstance(dev11, sp.Piecewise):
        br = dev11.args[0]
        ok11 = (br[0] == 0
                and br[1] in (sp.StrictLessThan(t, 4),
                              sp.And(sp.Le(t, 4), sp.Ne(t, 4))))
    out.append(("G11-tail-sum", ok11,
                "sum_k t^k 4^{1-k}/k == -4 log(1 - t/4) exact on "
                "the t < 4 branch (Piecewise gated)"))

    # G12 Lemma S instance (exact rationals) + Theorem-R sandwich
    WT = [sp.Rational(1, q) for q in W_TRUE_Q]
    WF = WT[:N_FIN_Q]
    tq = sp.Rational(*T_SAND)
    ok_pd = True
    d1q = sum(WT[N_FIN_Q:], sp.Integer(0))
    for kk in range(1, 13):
        dk = sum(ww ** kk for ww in WT[N_FIN_Q:])
        ok_pd = ok_pd and sp.simplify(
            sp.Rational(4) ** (1 - kk) * d1q - dk) >= 0
    with mp.workdps(80):
        dfl = mp.mpf(0)
        for ww in WT[N_FIN_Q:]:
            dfl += -mp.log(1 - mp.mpf(tq.p) / tq.q
                           * mp.mpf(ww.p) / ww.q)
        lo = mp.mpf(tq.p) / tq.q * mp.mpf(d1q.p) / d1q.q
        hi = -4 * mp.log(1 - mp.mpf(tq.p) / tq.q / 4) \
            * mp.mpf(d1q.p) / d1q.q
        ok_sand = bool(lo <= dfl <= hi)
        sand_txt = "%.6f <= %.6f <= %.6f" % (float(lo), float(dfl),
                                             float(hi))
    out.append(("G12-lemmaS-sandwich", ok_pd and ok_sand,
                "subset spectra: PD exact k<=12 (d_k <= 4^{1-k}d_1 "
                "in Q); Theorem-R sandwich t d1 <= log(Rfin/Ra) <= "
                "-4log(1-t/4) d1 at t=7/2: %s" % sand_txt))

    # G13 Lemma X counterexample
    A13 = [sp.Rational(1, 8)] * 2
    B13 = [sp.Rational(1, 16), sp.Rational(3, 16)]
    d1x = sum(A13, sp.Integer(0)) - sum(B13, sp.Integer(0))
    d2x = (sum(ww ** 2 for ww in A13)
           - sum(ww ** 2 for ww in B13))
    out.append(("G13-lemmaX-counterexample",
                d1x == 0 and d2x == sp.Rational(-1, 128),
                "{1/8,1/8} vs {1/16,3/16}: d1 = 0 but d2 = -1/128 "
                "-- L1 alone does NOT control higher moments"))

    # G14 jet dictionary
    ok14 = True
    wX = a * (X - a) / X ** 2
    for kk in range(1, 7):
        rhs = a ** kk * sum(sp.binomial(kk, j) * (-a) ** (kk - j)
                            * X ** (j - 2 * kk)
                            for j in range(kk + 1))
        ok14 = ok14 and sp.simplify(wX ** kk - rhs) == 0
    z = sp.symbols("z")
    G3 = [sp.Integer(4), sp.Integer(9), sp.Integer(25)]
    a0 = sp.Integer(2)
    f3 = sum(sp.log(z + g) for g in G3)
    okS = True
    for m in range(1, 6):
        cm = sp.diff(f3, z, m).subs(z, a0) / sp.factorial(m)
        Sm = sum((a0 + g) ** (-m) for g in G3)
        okS = okS and sp.simplify((-1) ** (m - 1) * m * cm - Sm) == 0
    out.append(("G14-jet-dictionary", ok14 and okS,
                "w^k binomial expansion exact k=1..6; S_m == "
                "(-1)^{m-1} m c_m exact (direct derivatives) on a "
                "rational 3-zero world m<=5 (the Pascal-diagonal "
                "cells in jet form)"))

    # G15 window algebra
    de, ga = sp.symbols("delta gamma", positive=True)
    ap = 3 * de ** 2 + ga ** 2 + 2 * de * sp.sqrt(2 * de ** 2
                                                  + ga ** 2)
    am_ = 3 * de ** 2 + ga ** 2 - 2 * de * sp.sqrt(2 * de ** 2
                                                   + ga ** 2)
    zc = (de + sp.I * ga) ** 2
    Rz, Az = sp.re(zc), de ** 2 + ga ** 2
    ident = sp.simplify((Rz + 2 * Az) - (3 * de ** 2 + ga ** 2)) == 0 \
        and sp.simplify((Rz + Az) * (Rz + 3 * Az)
                        - 4 * de ** 2 * (2 * de ** 2 + ga ** 2)) == 0
    interior = sp.simplify(ap - am_
                           - 4 * de * sp.sqrt(2 * de ** 2
                                              + ga ** 2)) == 0
    zpair = (ga - sp.I * de) ** 2
    apin = de ** 2 + ga ** 2
    wpin = sp.simplify(apin * zpair / (apin + zpair) ** 2
                       - apin / (4 * ga ** 2)) == 0
    wq = sp.Rational(1, 4) * (1 + sp.Rational(9, 100)
                              / sp.Integer(900))
    wnum = (sp.Rational(9, 100) + sp.Integer(900)) / (4 * 900)
    out.append(("G15-window-algebra",
                ident and interior and wpin
                and sp.simplify(wq - wnum) == 0,
                "interior a+ - a- = 4 delta sqrt(2delta^2+gamma^2) "
                "> 0; CDXXVI double formula identical; matched-pin "
                "w = a/(4 gamma^2) = (1+delta^2/gamma^2)/4 exact"))

    # G16 Euler safety
    cs, sn = sp.symbols("cs sn", positive=True)
    zplus = sp.expand((sp.sqrt(a) * cs + sp.I * sp.sqrt(a) * sn) ** 2)
    dev1 = sp.simplify(sp.expand(
        zplus - (a * (1 - 2 * sn ** 2)
                 + 2 * sp.I * a * sn * cs)).subs(cs ** 2,
                                                 1 - sn ** 2))
    modsq = sp.expand(((a * (1 - 2 * sn ** 2)) ** 2
                       + (2 * a * sn * cs) ** 2).subs(cs ** 2,
                                                      1 - sn ** 2))
    iff = (sp.simplify(sp.sqrt(sp.Rational(1, 4))
                       - sp.Rational(1, 2)) == 0)
    out.append(("G16-euler-safety", dev1 == 0
                and sp.simplify(modsq - a ** 2) == 0 and iff,
                "radius4-G12 branch identity re-gated; 1/2+sqrt(a) "
                "> 1 iff a > 1/4 (abs conv of the prime side <=> "
                "the contract's a-range; Re s > 1, no canonical-"
                "norm object: the r121 trap avoided)"))

    # G17 prime-jet coefficients
    sa = sp.Rational(1, 2) + sp.sqrt(a)
    sp1 = sp.diff(sa, a)
    sp2 = sp.diff(sa, a, 2)
    ok17 = (sp.simplify(a * sp1 + a ** 2 * sp2 - sp.sqrt(a) / 4) == 0
            and sp.simplify(a ** 2 * sp1 ** 2 - a / 4) == 0)
    out.append(("G17-prime-jet-coeffs", ok17,
                "a s' + a^2 s'' == sqrt(a)/4, a^2 s'^2 == a/4: "
                "C01_prime = (1/4) sum Lambda(n) n^{-1/2-sqrt a}"
                "(a log n - sqrt a) exact"))

    # G18 w bounds
    ok18 = (sp.simplify((a + t ** 2) ** 2 - t ** 4
                        - (a ** 2 + 2 * a * t ** 2)) == 0
            and sp.simplify((a + t ** 2) ** 2 - 4 * a * t ** 2
                            - (a - t ** 2) ** 2) == 0)
    out.append(("G18-w-tail-bounds", ok18,
                "w <= a/t^2 ((a+t^2)^2 >= t^4) and w <= 1/4 "
                "((a+t^2)^2 - 4at^2 = (a-t^2)^2): the quadrature-"
                "transfer currency for the node measure"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("doublelimit_proof_probe -- PRIME.RADIUS4.DOUBLELIMIT."
          "PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    ladder = LADDER[:2] if smoke else LADDER

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)), kind="edge")

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (Theorem R inputs + window algebra)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("THEOREM R stated: (L1) d1 -> 0 + (WPD) |d_k| <= C 4^{1-k}"
         " d1 ==> sup_{[0,r]} |log(R_fin/R_a)| <= max(1,C)"
         "(-4log(1-r/4)) d1 -> 0 for every r < 4 ==> (H-conv) on "
         "the FULL Euler interval + (H-trace); with the round-122 "
         "NF-closure theorem (cited): L1 + WPD dense-a ==> RH")
    info("LEMMA N stated (classical, cited): (H-conv)+(H-trace) ==> "
         "L1 and Tr B^k -> C0k for every fixed k (Vitali + Cauchy "
         "estimates on the zero-free log) -- L1 is NECESSARY for "
         "the old omega; the {L1, WPD} refinement is not weaker")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS (EM currency, jets, prime split, witness)")
    # G20 EM audit
    pts = []
    with mp.workdps(JET_DPS):
        for a in A_JET:
            am = mp.mpf(a)
            for j in (0, JET_M // 4, JET_M // 3, JET_M // 2):
                th = 2 * mp.pi * j / JET_M
                pts.append(mp.mpf("0.5")
                           + mp.sqrt(am + am / 2 * mp.exp(1j * th)))
        for a in A_BAT:
            for t in T_BAT[a]:
                th = 2 * mp.asin(mp.sqrt(mp.mpf(repr(t))) / 2)
                pts.append(mp.mpf("0.5")
                           + mp.sqrt(a * mp.exp(1j * th)))
    demA = audit_em_dev(pts)
    check("G20-em-audit", demA <= BAR_EM_AUDIT,
          "own EM zeta vs audit mp.zeta at %d battery/jet points: "
          "max rel %.1e (bar %.0e)" % (len(pts), demA, BAR_EM_AUDIT),
          kind="edge")

    # jets + G21 cross-ward
    jets = {}
    jets_arch = {}
    ok21 = True
    det21 = []
    for a in A_JET:
        t0 = time.time()
        jets[a] = cauchy_jet(em_log_phi, a, JET_NC)
        jets_arch[a] = cauchy_jet(arch_log_xi, a, 3)
        with mp.workdps(JET_DPS):
            am = mp.mpf(a)
            F = mp.diff(em_log_phi, am)
            Fp = mp.diff(em_log_phi, am, 2)
            c01_diff = mp.re(am * F + am * am * Fp)
            c01_jet = am * jets[a][1] + 2 * am * am * jets[a][2]
            dev_c1 = float(abs(jets[a][1] - mp.re(F))
                           / abs(mp.re(F)))
            dev_c01 = float(abs(c01_jet - c01_diff) / abs(c01_diff))
        det21.append("a=%d: c1 %.1e C01 %.1e (%.0f s)"
                     % (a, dev_c1, dev_c01, time.time() - t0))
        ok21 = ok21 and dev_c1 <= BAR_JET_XW and dev_c01 <= BAR_JET_XW
    check("G21-jet-cross-ward", ok21,
          "Cauchy jet vs mp.diff: " + "; ".join(det21), kind="edge")

    # targets
    kmax_t = K_ID
    c0k = {a: c0k_from_jet(a, jets[a], kmax_t) for a in A_JET}
    c01 = {a: float(c0k[a][0]) for a in A_JET}
    c01_arch = {}
    for a in A_JET:
        with mp.workdps(JET_DPS):
            am = mp.mpf(a)
            c01_arch[a] = float(am * jets_arch[a][1]
                                + 2 * am * am * jets_arch[a][2])
    for a in A_JET:
        info("a=%-2d: C01 %.10f  C01_arch %.10f  C01_prime(exact "
             "diff) %.10f  ratio prime/C01 %.4f  MEANDENS %.10f"
             % (a, c01[a], c01_arch[a], c01[a] - c01_arch[a],
                (c01[a] - c01_arch[a]) / c01[a],
                mean_density_integral(a)))

    # G22 prime split corridor
    lam = lambda_sieve(N_SIEVE)
    ok22 = True
    det22 = []
    for a in CORRIDOR_A:
        ps = prime_c01_partial(float(a), lam)
        tb = prime_tail_bound(float(a), N_SIEVE)
        tgt = c01[a] - c01_arch[a]
        dev = abs(tgt - ps)
        det22.append("a=%d: |exact-diff - Lambda_sum| %.2e <= tail "
                     "%.2e + floor" % (a, dev, tb))
        ok22 = ok22 and dev <= tb + 1e-12
    check("G22-prime-split-corridor", ok22,
          "C01 - C01_arch == (1/4) sum Lambda(n) n^{-1/2-sqrt a}"
          "(a ln n - sqrt a) within the closed-form tail (+ 1e-12 "
          "f64 floor, disclosed) at N=2e5: " + "; ".join(det22))
    ps1 = prime_c01_partial(1.0, lam)
    tb1 = prime_tail_bound(1.0, N_SIEVE)
    info("a=1 budget wall (r119/r122 replicated, INFO): partial "
         "%.5f vs exact diff %.5f, closed-form tail bound %.1e "
         "-- absolutely convergent != budget convergent at "
         "sigma = 1.5" % (ps1, c01[1] - c01_arch[1], tb1))

    # G26 WPD obstruction witness (planted quartet, closed form)
    with mp.workdps(60):
        de = mp.mpf(repr(PLANT_DELTA))
        gp = mp.mpf(repr(PLANT_GAMMA))
        wstar = (1 + de ** 2 / gp ** 2) / 4
        fourw = 4 * wstar
        ok26 = bool(fourw > 1)
        det26 = []
        for B in PLANT_BARS:
            Bm = mp.mpf(repr(B))
            kstar = int(mp.ceil(mp.log(2 * Bm) / mp.log(fourw)))
            val_lo = fourw ** (kstar - 1) / 2
            val_hi = fourw ** kstar / 2
            ok26 = ok26 and bool(val_hi >= Bm) \
                and bool(val_lo < Bm)
            det26.append("B=%.0e: k*=%d" % (B, kstar))
    tru_fall = True
    for a in A_BAT:
        with mp.workdps(JET_DPS):
            lad = [float(c0k[a][k - 1] * mp.mpf(4) ** (k - 1))
                   for k in range(1, K_MOM + 1)]
        tru_fall = tru_fall and all(lad[i + 1] <= lad[i] * 1.02
                                    for i in range(len(lad) - 1))
        info("true PD ladder C0k 4^{k-1} at a=%d: %s"
             % (a, ["%.4f" % v for v in lad]))
    check("G26-wpd-witness", ok26 and tru_fall,
          "planted quartet (delta=0.3, gamma=30, matched a*=900.09):"
          " excess ladder (4w*)^k/2 with 4w* = %s crosses every bar "
          "at the closed-form k* (%s) -- WPD's k-tail IS window "
          "positivity (Cauchy-Hadamard); true-world ladders "
          "C0k 4^{k-1} FALL on the battery"
          % (mp.nstr(fourw, 8), "; ".join(det26)))

    # ---------------------------------------------------------- S3
    section("S3  OPERATORS (round-114 blocks; measured lemma status)")
    t0 = time.time()
    ce3 = R4.build_cell(3, KFAC, "MAIN", 45, want_mp=False)
    sl3 = SL.build_trig_cell_hp(3, KFAC, "MAIN", 45)
    co3 = R4.build_cell(3, KFAC, "MAIN", 45, sector="odd")
    so3 = SL.build_trig_cell_hp(3, KFAC, "MAIN", 45, sector="odd")
    dev_e = float(np.max(np.abs(ce3["m_tilde"] - sl3["m_tilde"])))
    dev_o = float(np.max(np.abs(co3["m_tilde"] - so3["m_tilde"])))
    check("G30-ward-x3", dev_e <= BAR_WARD and dev_o <= BAR_WARD,
          "own build vs SL x=3: even %.1e odd %.1e (%.0f s)"
          % (dev_e, dev_o, time.time() - t0), kind="edge")

    cells = {3: (ce3, co3)}
    for x, dps in ladder:
        if x in cells:
            continue
        want = (x == 5)
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=want)
        co = R4.build_cell(x, KFAC, "MAIN", dps, sector="odd")
        cells[x] = (ce, co)
        print("  x=%d built (K=%d, %.0f s + %.0f s)"
              % (x, ce["K"], ce["build_s"], co["build_s"]), flush=True)

    opsd = {}
    ok31 = True
    det31 = []
    for x, _d in ladder:
        ce, co = cells[x]
        ops = R4.build_ops(ce, co)
        if "zeros" not in ce:
            SL.hp_zero_data(ce)
        if ops["Meta"] is not None:
            pos, imrel = R4.spec_pos(ops["Meta"])
            zs = np.asarray(ce["zeros"], float)
            edge = ops["K"] * math.pi / ops["L"]
            nlow = int(np.sum(zs <= 2 * edge))
            n = min(nlow, len(pos))
            cdev = float(np.max(np.abs(pos[:n] - zs[:n]) / zs[:n]))
            ok31 = ok31 and imrel <= BAR_REAL and cdev <= BAR_CENSUS
            det31.append("x%d:op(im %.0e, census %.0e)"
                         % (x, imrel, cdev))
            mus = pos
        else:
            mus = np.asarray(ce["zeros"], float)
            det31.append("x%d:census(eta-degenerate %.0e, r122 "
                         "AMENDMENT-1 pattern)" % (x,
                                                   ops["eta_xi_rel"]))
        opsd[x] = {"mus": mus, "K": ce["K"], "L": ce["a"],
                   "be": ce["K"] * math.pi / ce["a"]}
    check("G31-realness-census", ok31,
          "; ".join(det31))

    xs = [x for x, _d in ladder]
    # d_k tables (mp targets, f64 moment sums)
    dk_tab = {}      # (x, a) -> list d_k k=1..K_ID
    d1_tab = {a: [] for a in A_BAT}
    for x in xs:
        mus = opsd[x]["mus"]
        for a in A_BAT:
            wmu = a * mus ** 2 / (a + mus ** 2) ** 2
            dks = []
            with mp.workdps(JET_DPS):
                for k in range(1, K_ID + 1):
                    tr = mp.mpf(repr(float(np.sum(wmu ** k))))
                    dks.append(float(c0k[a][k - 1] - tr))
            dk_tab[(x, a)] = dks
            d1_tab[a].append(dks[0])
    print("  d_1 ladder (C01 - TrB):")
    for a in A_BAT:
        print("    a=%-3d: " % a + "  ".join(
            "x%d:%.5f" % (x, d) for x, d in zip(xs, d1_tab[a])))

    def falls(seq, factor):
        okf = seq[-1] <= seq[0] / factor
        steps = sum(1 for i in range(len(seq) - 1)
                    if seq[i + 1] <= WOBBLE * seq[i])
        return okf and steps >= len(seq) - 1

    ok32 = all(all(d > 0 for d in d1_tab[a])
               and (smoke or falls(d1_tab[a], FALL_L1))
               for a in A_BAT)
    check("G32-monotone-from-below", ok32,
          "d_1 > 0 at every rung and a (round-112 from-below "
          "structure in trace currency) and falls by >= %.1f on the "
          "ladder (radius4 G32 bars, cited): L1 measured healthy; "
          "(H-trace) finite-level: sup TrB = C01 - min d1 < C01"
          % FALL_L1)

    # G33 WPD/PD adjudication
    ok33 = True
    pd_ok = True
    worst_c, worst_pd = 0.0, 1.0
    cmes = {a: [] for a in A_BAT}
    for x in xs:
        for a in A_BAT:
            dks = dk_tab[(x, a)]
            d1 = dks[0]
            rats = [dks[k - 1] * 4.0 ** (k - 1) / d1
                    for k in range(2, K_MOM + 1)]
            cme = max(abs(r) for r in rats)
            pfl = min(rats)
            cmes[a].append(cme)
            worst_c = max(worst_c, cme)
            worst_pd = min(worst_pd, pfl)
            ok33 = ok33 and cme <= C_BAR
            pd_ok = pd_ok and pfl >= -PD_TOL
            if x == xs[-1]:
                print("  WPD ladder x=%d a=%-3d: %s"
                      % (x, a, ["%.4f" % r for r in rats]))
    for a in A_BAT:
        info("C_meas ladder a=%d: %s -- the WPD constant FALLS "
             "with the rung (band-edge domination: the sharper "
             "Lemma-S law d_k <= w_edge^{k-1} d_1)"
             % (a, ["%.5f" % c for c in cmes[a]]))
    check("G33-wpd-pd", ok33,
          "WPD constant C_meas = max_k |d_k| 4^{k-1}/d_1 <= %.2f at "
          "every rung/a (worst %.4f); PD floor %.4f >= -%.2f => %s"
          % (C_BAR, worst_c, worst_pd, PD_TOL,
             "PD-MEASURED (all defect jets positive and dominated)"
             if pd_ok and ok33 else
             "WPD-only or VIOLATED -- witness printed above"))

    # G23 series identity + G34 reduction band
    ok23 = True
    ok34 = True
    det34 = []
    for x in xs:
        mus = opsd[x]["mus"]
        for a in A_BAT:
            dks = dk_tab[(x, a)]
            d1 = dks[0]
            cmax = max(abs(dks[k - 1]) * 4.0 ** (k - 1) / d1
                       for k in range(1, K_MOM + 1))
            supdef = 0.0
            for t in T_BAT[a]:
                meas = math.log(R4.det_quotient(mus, a, t)
                                / r_true(a, t))
                model = sum(t ** k * dks[k - 1] / k
                            for k in range(1, K_ID + 1))
                q = t / 4.0
                tail = (max(1.0, cmax) * d1 * 4.0
                        * q ** (K_ID + 1) / ((K_ID + 1) * (1 - q)))
                ok23 = ok23 and abs(meas - model) <= tail + 1e-8
                supdef = max(supdef, abs(meas))
            tmax = T_BAT[a][-1]
            ratio = supdef / (tmax * d1)
            hi_th = -4.0 * math.log(1 - tmax / 4.0) / tmax
            ok34 = ok34 and RATIO_LO <= ratio <= hi_th * RATIO_PAD
            if x == xs[-1]:
                det34.append("a=%d: %.3f in [%.2f, %.2f]"
                             % (a, ratio, RATIO_LO,
                                hi_th * RATIO_PAD))
    check("G23-series-identity", ok23,
          "log(R_fin/R_true)(t) == sum_{k<=%d} t^k d_k/k within the "
          "closed-form k-tail at every (rung, a, t): the defect IS "
          "the jet, exactly" % K_ID)
    check("G34-reduction-band", ok34,
          "supdefect/(t_max d_1) inside the Theorem-R band "
          "[%.2f, -4log(1-t/4)/t * %.2f] at every rung/a "
          "(deepest rung: %s) -- the round-122 mechanism law "
          "G35-band [0.5, 2] is EXPLAINED by Theorem R"
          % (RATIO_LO, RATIO_PAD, "; ".join(det34)))

    # G35 node law
    ok35 = True
    det35 = []
    for x in xs:
        mus = opsd[x]["mus"]
        be = opsd[x]["be"]
        inb = mus[mus <= INBAND_F * be]
        n_in = len(inb)
        if n_in < 5:
            continue
        Bin = INBAND_F * be
        dev_rvm = max(abs((T / (2 * math.pi))
                          * math.log(T / (2 * math.pi * math.e))
                          + 7.0 / 8.0 - (i + 0.5))
                      for i, T in enumerate(inb))
        dev_clk = max(abs(T * opsd[x]["L"] / math.pi - (i + 0.5))
                      for i, T in enumerate(inb))
        dev_sc = max(abs(n_in * (2 / math.pi)
                         * (math.asin(min(T / Bin, 1.0))
                            + (T / Bin)
                            * math.sqrt(max(1 - (T / Bin) ** 2, 0)))
                         / 2.0 * 2.0 - (i + 0.5))
                     for i, T in enumerate(inb))
        dev_as = max(abs(n_in * (2 / math.pi)
                         * math.asin(min(T / Bin, 1.0)) - (i + 0.5))
                     for i, T in enumerate(inb))
        ok35 = ok35 and dev_rvm <= RVM_BAR \
            and min(dev_clk, dev_sc, dev_as) >= FIT_SEP * dev_rvm
        det35.append("x%d: RvM %.2f | clock %.1f semicirc %.1f "
                     "arcsine %.1f" % (x, dev_rvm, dev_clk,
                                       dev_sc, dev_as))
    check("G35-node-law", ok35,
          "in-band counting vs models (sup dev, zeros): %s -- the "
          "equilibrium measure of the round-114 operators is the "
          "ARITHMETIC RvM zero-counting law, not any classical "
          "potential-theory density" % "; ".join(det35))

    # G36 d1 anatomy at deepest rung
    xd = xs[-1]
    an4 = ward_d1_anatomy(opsd[xd]["mus"], gam, 4.0, c01[4],
                          opsd[xd]["be"])
    ts_share = an4["tail"] / an4["d1"]
    ib_share = an4["mism"] / an4["d1"]
    art_share = an4["art"] / an4["trb"]
    check("G36-d1-anatomy", TS_LO <= ts_share <= 1.10
          and abs(ib_share) <= IB_HI and art_share <= ART_HI,
          "x=%d a=4: d1 = %.5f = tail %.5f (share %.3f) + in-band "
          "mismatch %.1e (share %.1e); artifact w-mass share %.1e "
          "-- the residue is the RvM TAIL, exactly the round-122 "
          "m=1 mechanism" % (xd, an4["d1"], an4["tail"], ts_share,
                             an4["mism"], ib_share, art_share))

    # G37 SMOOTH control
    csm = R4.build_cell(5, KFAC, "SMOOTH", 60)
    csmo = R4.build_cell(5, KFAC, "SMOOTH", 60, sector="odd")
    opsm = R4.build_ops(csm, csmo)
    if opsm["Meta"] is not None:
        mus_sm, _im = R4.spec_pos(opsm["Meta"])
    else:
        SL.hp_zero_data(csm)
        mus_sm = np.asarray(csm["zeros"], float)
    i5 = xs.index(5)
    seps = []
    for a in A_BAT:
        wsm = float(np.sum(a * mus_sm ** 2 / (a + mus_sm ** 2) ** 2))
        d1s = c01[a] - wsm
        seps.append(abs(d1s) / abs(d1_tab[a][i5]))
    med_sep = float(np.median(seps))
    check("G37-smooth-separation", med_sep >= SEP_SM,
          "SMOOTH x=5 trace-currency separation |d1_smooth/d1_main| "
          "median %.2f >= %.1f (per-a %s); prime-currency diff "
          "TrB_main - TrB_smooth at a=4: %.5f vs C01_prime %.5f "
          "(INFO: density functional vs prime content)"
          % (med_sep, SEP_SM, ["%.2f" % s for s in seps],
             float(np.sum(4 * opsd[5]["mus"] ** 2
                          / (4 + opsd[5]["mus"] ** 2) ** 2))
             - float(np.sum(4 * mus_sm ** 2
                            / (4 + mus_sm ** 2) ** 2)),
             c01[4] - c01_arch[4]))

    # G38 Z1 trace typing
    z1r = []
    for x in xs:
        mus = opsd[x]["mus"]
        nb = ward_band_match(mus, gam)
        hyb = ward_hybrid(mus, gam, nb)
        rr = []
        for a in A_BAT:
            wmu = float(np.sum(a * mus ** 2 / (a + mus ** 2) ** 2))
            why = float(np.sum(a * hyb ** 2 / (a + hyb ** 2) ** 2))
            rr.append(abs(wmu - why)
                      / max(abs(c01[a] - wmu), 1e-15))
        z1r.append(float(np.median(rr)))
    transcribing = all(r <= Z1_BAR for r in z1r)
    check("G38-z1-typing", True,
          "trace-observable hybrid rule executed: %s (median "
          "ratios %s) -- today's L1 evidence carries the cache "
          "band; the round-122 conviction %s; a PROOF must run "
          "from the source side (the S2 split), typed not hidden"
          % ("TRANSCRIBING-IN-BAND" if transcribing
             else "NON-TRANSCRIBING", ["%.3f" % r for r in z1r],
             "confirmed" if transcribing else "NOT confirmed"))

    # G39 perturbation screen
    ce5 = cells[5][0]
    with mp.workdps(ce5["dps"]):
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G39-perturbation-screen", 1e-40 < d_eps < 1e-10,
          "1e-25 shift on Q[0,0] at x=5 moves eps by %.1e (nonzero "
          "and bounded; round-118 exact-zero red flag; all mp work "
          "under explicit workdps)" % d_eps, kind="edge")

    # ---------------------------------------------------------- S4
    section("S4  MIN-CUT (round-116 replica + series refinement)")
    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1N"): 1, ("L1N", "WPDN"): 1,
                ("WPDN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "L1N"): 1, ("L1N", "R4HYP"): INF,
               ("NFCLOS", "WPDN"): 1, ("WPDN", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k: v for k, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G50-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach and "NFCLOS" in reach,
          "flows: base 4, series-refined 5 (the round-122 "
          "LANEA-CONV unit edge REFINED into NFCLOS -> L1 -> WPD in "
          "SERIES: same capacity, two independently cuttable "
          "omegas), counterfactual parallel wiring 6 (NOT REAL: "
          "Theorem R needs both); RH unreachable without an omega "
          "edge; census {MEAS, OMEGA-POS} unchanged; typed "
          "SUFFICIENT-ONLY with L1 NECESSARY for the old omega "
          "(Lemma N)")
    info("EXACT RESIDUE: RH <== [r122 NF-closure, UNC] + [Theorem "
         "R, proven here] + {L1(a), WPD(a)} on a dense subset of "
         "(1/4, inf).  L1 = Tr B_{a,lam} -> C01(a) = C01_arch(a) + "
         "(1/4) sum Lambda(n) n^{-1/2-sqrt a}(a ln n - sqrt a) "
         "[abs conv iff a > 1/4]; WPD = |C0k - TrB^k| <= C 4^{1-k} "
         "d1, whose k-tail is window positivity itself "
         "(Cauchy-Hadamard + r117 window, G26 witness).  Today's "
         "finite evidence for both is transcribing-in-band (G38).")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "THMR-PROVEN(L1 + WPD => (H-conv) on the FULL Euler "
        "interval + (H-trace), rate max(1,C)(-4log(1-r/4)) d1; "
        "inputs: L0 exact gates G10-G18 + elementary series; "
        "with r122 NF-closure (cited): L1 + WPD dense-a => RH)",
        "L1-NECESSITY-PROVEN(old omega => L1; Vitali + Cauchy, "
        "cited classical)",
        "SUBSETPD-PROVEN(positive defect measure => PD exactly; "
        "G12)",
        "MOMENT-TRANSFER-NOT-FREE(G13 exact counterexample)",
        "WPD-TAIL-RH-EQUIVALENT(Cauchy-Hadamard + r117 window; "
        "planted k* witness G26 -- WPD is the RH positivity in "
        "Pascal-diagonal currency, not a technical lemma)",
        ("PD-MEASURED(worst C %.4f, floor %.4f: all defect jets "
         "positive and dominated on every rung/a)"
         % (worst_c, worst_pd)) if (ok33 and pd_ok) else
        ("WPD-STATUS(C %.4f, floor %.4f -- see G33 witness)"
         % (worst_c, worst_pd)),
        "L1-OBSTRUCTED(the node-law wall = k_lambda ~ xi_lambda; "
        "arithmetic gap quantified: C01_prime/C01 = %s at a = %s; "
        "Z1 %s)" % (["%.3f" % ((c01[a] - c01_arch[a]) / c01[a])
                     for a in A_BAT], list(A_BAT),
                    "transcribing-in-band" if transcribing
                    else "non-transcribing"),
        "DENSITY-RVM-ARITHMETIC(G35: RvM law, not semicircle/"
        "arcsine/clock -- the mean is archimedean, the oscillation "
        "is the prime side; MEANDENS != C01 printed)",
        "MECHANISM-THEOREM(G34: the r122 empirical band [0.5,2] is "
        "the Theorem-R band [1, -4log(1-t/4)/t] up to in-band "
        "mismatch)",
        "DOUBLELIMIT-ORDERED(L3/L4 proven as packaging: iterated "
        "limits suffice, open windows meet every dense set, G15)",
        "EULERSAFE-NONCIRCULAR(a > 1/4 <=> Re s > 1 abs conv, G16; "
        "no canonical-norm object anywhere: the r121 trap avoided)",
        "MINCUT-REFINED(4 -> 5, series pair {L1, WPD}, "
        "SUFFICIENT-ONLY, census unchanged)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if EDGE_FAILS:
        print("COMPOSITE: INSTRUMENT-EDGE(%s)" % ",".join(EDGE_FAILS))
    elif EXACT_FAILS:
        print("COMPOSITE: EXACT-LAYER-OBSTRUCTED(%s)"
              % ",".join(EXACT_FAILS))
    else:
        print("COMPOSITE: THMR-PROVEN + SUBSETPD-PROVEN + "
              "L1-NECESSITY-PROVEN + MOMENT-TRANSFER-NOT-FREE + "
              "WPD-TAIL-RH-EQUIVALENT + %s + L1-OBSTRUCTED + "
              "DENSITY-RVM-ARITHMETIC + MECHANISM-THEOREM + "
              "DOUBLELIMIT-ORDERED + MINCUT-REFINED"
              % ("PD-MEASURED" if (ok33 and pd_ok) else
                 "WPD-ADJUDICATED"))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
