#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wpd_proof_probe -- PRIME.WPD.INTERLACING.PROOF.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (proof lane on WPD/PD, round-128 serial pair {L1, WPD})
=======================================================================
Round 128 (doublelimit_proof_probe, 28/28) proved Theorem R: L1 + WPD
==> (H-conv)+(H-trace) on the full Euler interval, and with the cited
round-122 NF-closure: L1 + WPD on dense a ==> RH.  It also proved
LEMMA S (positive defect measure ==> PD exactly, with the sharper
edge law) and MEASURED PD everywhere tested (worst C 0.0202, C
falling per rung, PD floor -0.0000: tiny NEGATIVE defects at high k
on the deep rung).  This probe is the maximal proof attempt on
WPD/PD itself for the round-114 operator family: identify the exact
structural mechanism (compression/interlacing vs Gauss quadrature),
prove what is provable with explicit constants, machine-pin the
exact obstruction where it is not, and adjudicate the arithmetic
content on the control worlds.

NOTATION (round-128 conventions).  a > 1/4; w_a(t) = a t^2/(a+t^2)^2
on real t (w in [0, 1/4]); nodes mu_1 <= ... <= mu_n = the positive
finite spectrum of the round-114 block operator at rung lambda
(= the mp-certified census zeros of the band-limited secular
function E_lambda; operator cross-warded on admissible rungs);
gamma_1 <= gamma_2 <= ... = true zero ordinates.  Pair-counted
moments Tr B^k = sum_i w(mu_i)^k, C0k(a) = sum_j w(gamma_j)^k (from
the log-Phi Cauchy jet, source currency), defect jets d_k = C0k -
Tr B^k.  PD: 0 <= d_k <= 4^{1-k} d_1.  WPD: |d_k| <= C 4^{1-k} d_1.

=======================================================================
THE MECHANISM ADJUDICATION (T1) -- what this probe establishes
=======================================================================
QUADRATURE ROUTE (Markov/Gauss error signs) is DEAD, machine-gated:
(a) the finite trace formula has NO polynomial exactness degree at
all -- d_1 > 0 at every rung and battery a (a Gauss/Chebyshev-type
rule of the true zero-counting measure would integrate degree-1
w-currency exactly; the round-112 from-below fact is itself the
witness); (b) the Markov error calculus additionally requires fixed
derivative signs: w''(t) (a+t^2)^4/(2a) = 3t^4 - 8at^2 + a^2 exactly,
with sign flip at t^2 = a(4+sqrt 13)/3 (exact roots) -- no fixed
sign on the branch (√a, inf); both halves S1/S3-gated.

COMPRESSION/INTERLACING ROUTE CARRIES, in counting currency: there
is NO exact rung-to-rung operator compression (the mode frames are
non-nested: L = log(x)/2 and K both move), but the operative
one-sided relation is COUNTING DOMINANCE against the true zero set:
with nodes and zeros sorted, mu_i >= gamma_i (equivalently
N_fin(T) <= N_true(T) for every T).  Pre-freeze calibration
(disclosed below): dominance holds NODE-BY-NODE at x = 3 and x = 5
(0 undershoots; mismatch positive and growing toward the band edge);
at x = 8 a NEAR-EDGE BOUNDARY LAYER undershoots (certified
undershoots at i = 11/12/13 of -8.6e-5/-4.7e-4/-6.1e-3; interior
sub-1e-9 signs are below the census certification floor), with
wrong-sign w-mass M- / d_1 ~ 8e-6.  The boundary layer is the EXACT
obstruction to sub-multiset PD (Lemma S's hypothesis) and explains
the round-128 measured PD floor -0.0000 (negative d_k at high k on
deep rungs).  Rung-to-rung matched-prefix node descent (compression
evidence) is measured as its own gate.

=======================================================================
THE THEOREMS (T2; all inequalities elementary, sympy-gated for
general k via factorization identities + exact rational instances)
=======================================================================
Fix a > 1/4 and t0 > sqrt(a).  All spectra below live in [t0, inf)
(BRANCH CONDITION; on the battery t0 = min(mu_1, gamma_1) >= 14.13
and sqrt(a) <= 4, margins gated).  Put W = w_a(t0) (so every
w-value <= W by monotone decrease on the branch, G10), and let the
SORTED PAIRING pair node mu_i with zero gamma_i (i <= n), tail =
{gamma_j : j > n}, wedge = w_a(gamma_{n+1}),
   M+ = sum_i max(0, w(gamma_i) - w(mu_i)),
   M- = sum_i max(0, w(mu_i) - w(gamma_i)),
   tail1 = sum_{j>n} w(gamma_j)   (so d_1 = M+ - M- + tail1).

THEOREM D (two-sided defect bounds; PROVEN: G12 power-difference
factorization v^k - u^k = (v-u) sum_{j<k} u^j v^{k-1-j} for all k
[symbolic k = 2..12 + geometric identity], G13 tail domination
w^k <= wedge^{k-1} w on w <= wedge, G14/G16 exact rational
instances):  for every k >= 1,
   - k W^{k-1} M-   <=   d_k   <=   k W^{k-1} M+  +  wedge^{k-1} tail1.
COROLLARY W1 (explicit WPD constant; PROVEN):  with q = 4W < 1 and
K(q) = max_{k>=2} k q^{k-1}  (= 2q if q <= 1/2, exact G15; in
general attained at k <= ceil(q/(1-q)) + 1, exact),
   |d_k| <= C_pred * 4^{1-k} * d_1   for all k >= 2,   with
   C_pred = [ K(q) (M+ + M-) + tail1 ] / d_1
(4*wedge <= 1 used on the tail; d_1 > 0 required).  C_pred depends
on lambda only through the mass ratios (M+ + M-)/d_1 and tail1/d_1
<= 1 + M-/d_1: WPD with a UNIFORM constant reduces to the single
statement  sup_lambda (M+ + M- )/d_1 < inf  (mass-ratio bound, MRB).
COROLLARY P1 (PD sub-case; PROVEN): if M- = 0 (node upshift,
dominance one-sided) then 0 <= d_k and the sharp edge law
d_k <= k W^{k-1} M+ + wedge^{k-1} tail1 holds; if moreover
q <= 1/2 and K(q) M+ + tail1 <= d_1 (tail-dominated regime,
measured), the strong round-128 PD form d_k <= 4^{1-k} d_1 follows.
THEOREM B (branch theorem; exact): w' = 2at(a - t^2)/(a + t^2)^3,
so w_a is strictly decreasing on (sqrt a, inf): the single-branch
reduction is available exactly for a < gamma_1^2 = 199.79; the
battery (a <= 16) has margin sqrt(a) <= 4 < 14.13.  For a >
gamma_1^2 the matched two-branch decomposition is REQUIRED (typed;
not built here) and for a inside an off-line violation window WPD's
k-tail is window positivity itself (round 128 G26, cited): the
theorem family CANNOT close those a unconditionally -- that residue
is stated, not claimed.
OFF-LINE TAIL SAFETY (exact + cited): |w_a(z)| <= a|z|/(|z|-a)^2
for |z| > a (G17; |a+z| >= |z|-a), decreasing in |z|; with the
cited classical verification (all zeros to height H = 3e12 on the
line, Platt-Trudgian 2021, corpus v914 input) every hypothetical
off-line pair has |z| >= H^2, total |w|-mass <= eps_off(a) =
2a(log H + 1)/H (crude RvM-density integral bound, closed form)
~ 3e-10 and per-k (a/(H^2-a))-geometric: all gates carry eps_off
explicitly; nothing below assumes RH.

WHAT IS AND IS NOT PROVEN, typed without euphemism: THEOREM D /
W1 / P1 / B are unconditional statements about sorted real
multisets on the branch -- they consume (i) round-114 block
realness (cited theorem) for the node side, (ii) the classical
zero verification for the tail side, (iii) the branch gate (exact
battery margins).  The MASS DATA (M+, M-, tail1, d_1 > 0) are
MEASURED per rung against the X5 zero cache (ward currency): the
sign census and mass ladders are instrument reads, not theorems.
The residue after this round is therefore exact: WPD(a) for
a < gamma_1^2 <== MRB + d_1 > 0 (both one-sided node-law
statements, strictly weaker than the node convergence that L1
needs); WPD(a) at window scale a ~ gamma^2 of a hypothetical
off-line zero REMAINS RH-equivalent at the k-tail (round 128).
No RH claim in either direction.

=======================================================================
CONTROLS (T4; the arithmetic-content adjudication)
=======================================================================
Pre-freeze calibration (disclosed): PD is FALSE in ALL THREE control
worlds -- SMOOTH x=5 (arch-only PNT density): all 10 nodes undershoot
(first node 4.84 < gamma_1: the control fills the arithmetic
zero-free gap (0, 14.13)), d_1 = -0.048/-0.154/-0.297 at a = 1/4/16,
all d_k < 0; SCRARITH x=5 (golden-scrambled Lambda): all nodes
undershoot (first node 2.01), d_1 < 0 everywhere, branch condition
ITSELF fails at a = 16 (mu_1 = 2.01 < 4); EPSTEIN x=8 (conductor-20
lattice, off-line world): all 20 nodes undershoot (first node 1.23),
d_1 < 0 everywhere, branch fails at a = 4 and 16.  VERDICT
PD-WORLD-SEPARATING: the mechanism proves PD exactly where its
hypotheses hold and its hypotheses FAIL in every control -- WPD's
arithmetic content at battery a is NOT zero: it is precisely the
one-sided node law (d_1 > 0 from-below + dominance), i.e. "the
finite operator never overcounts the true zero-counting function",
which the prime block builds and every control destroys.  The omega
does NOT concentrate in L1 alone; the honest split is stated in S5.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  firewall (AST: no zero-oracle names; zeta attribute only inside
    audit_*; np.load only inside ward_*; no verification/ import);
    cache health (X5 READ-ONLY, ward namespace).
S1  exact layer (sympy): G10 branch derivative factorization;
    G11 w'' numerator 3t^4-8at^2+a^2 with exact roots a(4±sqrt13)/3
    (Markov sign flip); G12 power-difference factorization k=2..12
    + geometric identity (general k); G13 tail domination; G14
    THEOREM D pure-dominance exact rational instance (a=4, 10 true
    atoms, 4 dominating nodes, k<=12: 0 <= d_k <= kW^{k-1}M+ +
    wedge^{k-1}tail1, all exact in Q); G15 K(q) closed form: for
    q <= 1/2 max_{k>=2} k q^{k-1} = 2q (exact monotone-chain
    inequality) + far instance verifying the strong PD form
    d_k <= 4^{1-k} d_1; G16 THEOREM D mixed instance (one
    undershooting node): two-sided bounds exact in Q; G17 off-line
    modulus bound |w_a(z)| <= a|z|/(|z|-a)^2 exact + monotone;
    G18 y-coordinate bridge y = a/(a+t^2), w = y(1-y) exact +
    partner identity y(z) + y(a^2/z) = 1 (round-127 Lean anchor).
S2  targets (round-128 jet machinery imported): G20 EM audit at the
    battery/jet points (bar 1e-30); G21 jet cross-ward c1/C01 vs
    mp.diff (bar 1e-18 rel); G22 C0k jet vs cache+RvM ward:
    k=1 via ward_c01 (bar 1e-4 rel), k=2..12 vs direct cache sums
    (bar 1e-3 rel; cache-complete for k >= 2 at the battery).
S3  structure on the ladder x = (3, 5, 8, 13), KFAC 1.25, MAIN:
    census node source (SL.hp_zero_data, mp path) with G30 operator
    cross-ward at x=3 (R4 vs SL build, bar 1e-8) and x=3/5
    (spec+(M_eta) vs census, bar 1e-4; realness bar 1e-6; deeper
    rungs eta-degenerate by the round-122/128 pattern, census
    carries via the exterior-determinant identity, disclosed);
    G31 branch gate: min(mu_1, gamma_1) > sqrt(a) margins;
    G32 SIGN CENSUS (headline): sorted pairing, certification floor
    SIGN_FLOOR = 1e-8 rel (below it signs are typed UNCERTIFIED),
    certified undershoot table printed (expected: 0 at x=3/5, the
    near-edge boundary layer at x=8/13), dominance verdicts;
    G33 mass split ladder: M+, M-, tail1, d_1 recomposition vs jet
    C01 (bar: ward dev), theta- = M-/d_1 <= THETA_BAR = 1e-3
    (measured 8e-6 at x=8) and the theta- ladder printed;
    G34 THEOREM D PREDICTION GATE: for every (rung, a, k = 2..12)
    the measured jet d_k obeys  -kW^{k-1}M- - FLOOR <= d_k <=
    kW^{k-1}M+ + wedge^{k-1}tail1 + eps_off + FLOOR  (FLOOR =
    1e-13(C0k + TrB^k) + 1e-40, disclosed numeric floor);
    G35 WPD constant gate: C_meas (k<=8, round-128 convention) <=
    C_pred = [K(q)(M+ + M-) + tail1]/d_1 at every rung/a, C_pred
    ladder printed (uniformity-in-lambda evidence, MRB read);
    G36 rung-to-rung matched-prefix node descent (compression
    evidence): descent violations counted, law printed;
    G37 quadrature adjudication: d_1 > 0 at every rung/a (no
    degree-1 exactness) -- with G11: MECHANISM = COMPRESSION-TYPE
    COUNTING DOMINANCE, NOT QUADRATURE;
    G38 Z1/ward typing: the sign census and masses consume the X5
    cache -- typed WARD-CURRENCY evidence (the round-122/128
    transcription conviction repeated, not hidden: a source-side
    DOM proof is the remaining wall, but only ONE-SIDEDNESS is
    needed, strictly weaker than node convergence);
    G39 perturbation screen 1e-25 on Q[0,0] at x=5 (response in
    (1e-40, 1e-10), round-118 exact-zero red flag).
S4  controls: SMOOTH x=5, SCRARITH x=5, EPSTEIN x=8 (KFAC 1.25):
    G40/G41/G42 per world: d_1 <= -0.01 at every battery a (PD
    false), undershoot fraction >= 0.9 (dominance false), branch
    failures printed at the named (world, a); G43 mechanism
    consistency: no control satisfies the THEOREM-D hypothesis set
    (the mechanism never claims PD where PD is false).
S5  chain + min-cut: G50 round-116 replica + round-128 series
    refinement with WPDN split into DOMN (= MRB + d_1 > 0, battery
    a) in series with WPDWIN (window-scale a): flows base 4,
    extended 5, counterfactual parallel 6 printed NOT REAL; census
    {MEAS, OMEGA-POS} cardinality 4 unchanged; the exact residue
    printed.
S9  composite verdict + runtime bar.

=======================================================================
FROZEN NUMERICS
=======================================================================
LADDER = ((3,45),(5,60),(8,80),(13,120)) at KFAC 1.25 (round-128
currency); operator wards at x=3 (even+odd SL cross) and x=5
(spec vs census; mpM for the perturbation screen).  A_BAT =
(1, 4, 16).  K_MOM = 8 (C_meas, round-128 convention), K_PRED = 12
(prediction gate), JET_NC = 29 (>= 2*K_PRED + 1), JET_M = 256,
JET_DPS = 80.  EM zeta N = 80, J = 14 (round-128), audit bar 1e-30.
SIGN_FLOOR = 1e-8 (relative).  THETA_BAR = 1e-3.  BAR_C01_WARD =
1e-4 rel, BAR_C0K_WARD = 1e-3 rel.  CPRED_BAR = 1.5.  FLOOR_K =
1e-13*(C0k + TrB^k) + 1e-40 (disclosed).  H_VERIF = 3e12 (cited,
v914 corpus input); eps_off(a) = 2a(log H + 1)/H.  Controls bars:
D1_CTRL = -0.01, UNDER_FRAC = 0.9.  Exact instances (all rational):
INSTANCE 1 (pure dominance, a = 4): true t = (3, 7/2, 4, 5, 6, 8,
12, 20, 40, 100), nodes = (3+1/7, 7/2+1/9, 4+1/11, 5+1/13);
INSTANCE 2 (far branch, strong PD, a = 4): true t = (8, 9, 10, 12,
15, 20, 30, 60), nodes = (8+1/7, 9+1/9, 10+1/11); INSTANCE 3
(mixed, a = 4): nodes = (3+1/7, 7/2-1/9, 4+1/11, 5+1/13).
BAR_WARD_X3 = 1e-8, BAR_SPEC_CENSUS = 1e-4, BAR_REAL = 1e-6.
GAMMA1_LIT = 14.134725141734694 (ward only).  RUNTIME_BAR = 2400 s.
Deterministic: NO randomness anywhere (no RNG; all literals
frozen).  Cache verified_zeros_n7000.npy READ-ONLY in ward_
namespace (X5).  All mpf/mpc arithmetic inside explicit mp.workdps
blocks (round-118 ambient-precision negation trap).

VERDICT ENUMS (frozen): THMD-PROVEN(instances + general-k algebra);
WPD-EXPLICIT-CONSTANT(C_pred table; C_meas <= C_pred gated);
DOM-ONE-SIDED(rung list) / DOM-BOUNDARY-LAYER(rung list, wrong-sign
mass law); PD-EXACT-OBSTRUCTED(boundary layer = the machine-pinned
obstruction to Lemma-S sub-multiset PD; explains the round-128
negative high-k floor); MECHANISM-COMPRESSION-NOT-QUADRATURE;
BRANCH-THEOREM(a < gamma_1^2; battery margins); CONTROLS-SEPARATE
(PD false in all three; arithmetic content of WPD = the one-sided
node law, NOT zero) / CONTROLS-BLIND(if any control passes PD:
typed structural/archimedean honestly); MRB-MEASURED(C_pred
ladder); MINCUT-REFINED(flows, census unchanged); WARD-CURRENCY
typing always stated.  Composite priority: INSTRUMENT-EDGE (any
ward/audit gate fails, exit 1) > EXACT-LAYER-OBSTRUCTED (any S1
gate fails) > adjudicated verdicts as measured.

CALIBRATION DISCLOSURE (pre-freeze, two scratch scripts, deleted;
all numbers measured there are quoted above verbatim where used):
(a) sign census x=3/5/8 as quoted (0/0/10-of-20 sorted undershoots;
x=8 certified undershoots only in the near-edge layer i=11..13,
max depth -6.1e-3; interior negatives at 1e-14..1e-9 are census-
floor artifacts, hence SIGN_FLOOR); (b) mass ladders: M-/d_1 = 0 at
x=3/5, 7.8e-6 at x=8; M+/d_1 ~ 6-7 %; tail1/d_1 ~ 0.93; (c) the
THEOREM-D prediction bound held at every (x, a, k<=8) with margins
>= 4x in the scratch (cache-target currency there; jet currency
here); (d) w1 = w_a(gamma_1) = 0.00496/0.01924/0.06865 at a=1/4/16,
q = 4w1 <= 0.2746 on the battery, K(q) = 2q <= 0.5492, so the
strong-PD criterion q <= 1/2 holds on the whole battery; (e) the
control table quoted in the CONTROLS block; (f) build costs from
the round-128 run of record (x=13 even ~181 s).  Amendments after
the frozen run, if any, are appended as numbered AMENDMENT blocks.

AST FIREWALL: no zetazero/siegelz/siegeltheta/nzeros/grampoint
anywhere; the zeta attribute only inside audit_* functions; np.load
only inside ward_* functions; no import of verification/.
NO RH CLAIM.  EXPLORATION ONLY.

=======================================================================
AMENDMENT 1 (after frozen run 1: 29/31 at SPEC 9d206e5f4bb9688d,
runtime 224.3 s, log wpd_proof_probe.run1.log kept as disclosure;
fails G32-sign-census + G36-node-descent at x = 13).  INSTRUMENT
DEFECT FOUND AND REPAIRED; the two failed gates were testing a
corrupted instrument, not the operators.
DIAGNOSIS (scratch script, deleted; numbers quoted verbatim):
SL.hp_zero_data refines the mp-certified numerator-polynomial roots
by BISECTION ON THE FLOAT64 E-PROFILE inside a +-1e-3*z window.  At
deep rungs the E-values near mid-band zeros lie far below the f64
noise floor, so the refine walks away from the certified root:
at x = 13 the refined census deviates from the cache by up to
7.3e-2 mid-band (i = 24) with mp residual |E| ~ 1e-17..1e-28, while
the RAW mp polynomial roots match the cache to <= 3.5e-8 for ALL
in-band indices i <= 29 with mp residuals |E| ~ 1e-24..1e-42 (6-14
orders smaller).  At x = 8 the run-1 'certified undershoots'
-8.6e-5/-4.7e-4/-6.1e-3 (i = 11/12/13) become +1.7e-6/+2.1e-4/
+1.5e-3 in raw currency: OVERSHOOTS.  Every certified deviation of
the raw census is an overshoot, growing toward the band edge (the
x = 3/5 pattern, now at every rung).  The 'near-edge boundary
layer' of the pre-freeze calibration (which used the refined
census) was the SAME artifact; the round-128 measured PD floor
-0.0000 (tiny negative d_k at high k, deep rung) is explained by
it as well -- an instrument finding for the corpus: the r122/r128
census currencies carry an f64-refine node error up to ~7e-2
mid-band at x = 13 (harmless for their tail-dominated gates,
visible exactly in the PD floor).
REPAIR (this amendment; no bar, no battery, no ladder, no verdict
rule moved except the two gates re-specified as stated): (i) the
node source is the RAW mp polynomial census raw_mp_census() (the
SL.hp_zero_data mp path VERBATIM minus the f64 refine), certified
per root by an mp evaluation of E: new gate G30c requires the same
census cardinality as SL and max_root |E_mp(root)| <= RES_BAR =
1e-12 at every rung, and prints the refine-artifact exhibit
max|raw - refined| per rung; (ii) G32 is re-specified to the
raw-currency expectation: ZERO certified undershoots at EVERY rung
(DOM-ONE-SIDED; the boundary-layer clause of run 1 is retired with
this disclosure -- if any certified undershoot appears the gate
FAILS and the layer verdict path re-engages); (iii) G36 criterion
unchanged (descent expected to hold in raw currency).  All other
gates, bars and frozen numerics are untouched; run 1 remains part
of the record.
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
import doublelimit_proof_probe as DL          # round-128 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
LADDER = ((3, 45), (5, 60), (8, 80), (13, 120))
A_BAT = (1, 4, 16)
K_MOM = 8
K_PRED = 12
JET_NC = 29
SIGN_FLOOR = 1e-8
THETA_BAR = 1e-3
BAR_C01_WARD = 1e-4
BAR_C0K_WARD = 1e-3
CPRED_BAR = 1.5
H_VERIF = 3.0e12
D1_CTRL = -0.01
UNDER_FRAC = 0.9
BAR_WARD_X3 = 1e-8
BAR_SPEC_CENSUS = 1e-4
BAR_REAL = 1e-6
BAR_EM_AUDIT = 1e-30
BAR_JET_XW = 1e-18
RES_BAR = 1e-12            # AMENDMENT 1: raw-census mp residual bar
GAMMA1_LIT = 14.134725141734693790   # ward only
RUNTIME_BAR = 2400.0

INST1_TRUE = ((3, 1), (7, 2), (4, 1), (5, 1), (6, 1), (8, 1),
              (12, 1), (20, 1), (40, 1), (100, 1))
INST1_NODE = ((22, 7), (65, 18), (45, 11), (66, 13))
INST2_TRUE = ((8, 1), (9, 1), (10, 1), (12, 1), (15, 1), (20, 1),
              (30, 1), (60, 1))
INST2_NODE = ((57, 7), (82, 9), (111, 11))
INST3_NODE = ((22, 7), (61, 18), (45, 11), (66, 13))
A_INST = 4

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


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# ------------------------------------------------------- audit evaluators
def audit_em_dev(pts) -> float:
    worst = 0.0
    with mp.workdps(DL.JET_DPS):
        for s in pts:
            zt = mp.zeta(mp.mpc(s))
            worst = max(worst, float(abs(DL.em_zeta(s) - zt) / abs(zt)))
    return worst


# --------------------------------------------------------- exact layer
def kq_exact(q):
    """K(q) = max_{k>=2} k q^{k-1} for exact rational 0 < q < 1:
    terms increase while (k+1)q > k, i.e. k < q/(1-q); evaluate to
    ceil(q/(1-q)) + 2 (exact)."""
    import sympy as sp
    q = sp.Rational(q)
    khi = max(3, int(sp.ceiling(q / (1 - q))) + 2)
    return max((k * q ** (k - 1) for k in range(2, khi + 1)),
               key=lambda v: sp.Rational(v))


def instance_masses(a, true_ts, node_ts):
    """Exact rational masses for a sorted-pairing instance."""
    import sympy as sp

    def w(t):
        return a * t ** 2 / (a + t ** 2) ** 2

    tv = [sp.Rational(p, qd) for p, qd in true_ts]
    nv = [sp.Rational(p, qd) for p, qd in node_ts]
    n = len(nv)
    Mp = sp.Integer(0)
    Mm = sp.Integer(0)
    for i in range(n):
        dwi = w(tv[i]) - w(nv[i])
        if dwi >= 0:
            Mp += dwi
        else:
            Mm += -dwi
    tail1 = sum((w(t) for t in tv[n:]), sp.Integer(0))
    wedge = w(tv[n]) if len(tv) > n else sp.Integer(0)
    t0 = min(tv[0], nv[0])
    W = w(t0)
    dks = []
    for k in range(1, 13):
        dk = (sum((w(t) ** k for t in tv), sp.Integer(0))
              - sum((w(t) ** k for t in nv), sp.Integer(0)))
        dks.append(dk)
    return dict(Mp=Mp, Mm=Mm, tail1=tail1, wedge=wedge, W=W, dks=dks)


def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    a, t, u, v, wv = sp.symbols("a t u v w", positive=True)

    # G10 branch derivative factorization
    wexpr = a * t ** 2 / (a + t ** 2) ** 2
    dev10 = sp.simplify(sp.diff(wexpr, t)
                        - 2 * a * t * (a - t ** 2) / (a + t ** 2) ** 3)
    out.append(("G10-branch-derivative", dev10 == 0,
                "w' == 2at(a-t^2)/(a+t^2)^3 exact: w strictly "
                "decreasing on (sqrt a, inf) -- single-branch "
                "reduction exact for a < gamma_1^2"))

    # G11 second-derivative sign flip (Markov calculus dies)
    num11 = sp.simplify(sp.diff(wexpr, t, 2) * (a + t ** 2) ** 4
                        / (2 * a))
    dev11 = sp.expand(num11 - (3 * t ** 4 - 8 * a * t ** 2 + a ** 2))
    r11 = sp.solve(3 * u ** 2 - 8 * a * u + a ** 2, u)
    targ = [a * (4 - sp.sqrt(13)) / 3, a * (4 + sp.sqrt(13)) / 3]
    roots_ok = (len(r11) == 2
                and all(any(sp.simplify(r - tg) == 0 for tg in targ)
                        for r in r11))
    out.append(("G11-wpp-signflip", dev11 == 0 and roots_ok,
                "w'' (a+t^2)^4/(2a) == 3t^4 - 8at^2 + a^2 with exact "
                "roots t^2 = a(4 +- sqrt 13)/3: no fixed derivative "
                "sign on the branch -- the Markov/Gauss error "
                "calculus has no unconditional sign here"))

    # G12 power-difference factorization (general k mechanism)
    ok12 = True
    for kk in range(2, 13):
        fac = sp.expand(v ** kk - u ** kk
                        - (v - u) * sum(u ** j * v ** (kk - 1 - j)
                                        for j in range(kk)))
        ok12 = ok12 and fac == 0
    geo = sp.expand((1 - u) * sum(u ** i for i in range(11))
                    - (1 - u ** 11))
    out.append(("G12-power-difference", ok12 and geo == 0,
                "v^k - u^k == (v-u) sum_{j<k} u^j v^{k-1-j} exact "
                "k=2..12 (+ geometric identity): 0 <= u <= v <= W "
                "==> |v^k - u^k| <= k W^{k-1} |v-u|"))

    # G13 tail domination
    ok13 = all(sp.expand(wv ** kk - wv * wv ** (kk - 1)) == 0
               for kk in range(2, 13))
    out.append(("G13-tail-domination", ok13,
                "w^k = w * w^{k-1} <= wedge^{k-1} w on 0 <= w <= "
                "wedge (exact; the sharp round-128 Lemma-S edge law)"))

    # G14 THEOREM D pure-dominance instance (exact rationals)
    m1 = instance_masses(sp.Integer(A_INST), INST1_TRUE, INST1_NODE)
    ok14 = m1["Mm"] == 0
    for k in range(1, 13):
        lo = -k * m1["W"] ** (k - 1) * m1["Mm"]
        hi = (k * m1["W"] ** (k - 1) * m1["Mp"]
              + m1["wedge"] ** (k - 1) * m1["tail1"])
        ok14 = ok14 and (m1["dks"][k - 1] >= lo) \
            and (m1["dks"][k - 1] <= hi) and (m1["dks"][k - 1] >= 0)
    out.append(("G14-thmD-pure-instance", ok14,
                "INSTANCE 1 (a=4, 10 true, 4 dominating nodes): "
                "M- = 0 and 0 <= d_k <= kW^{k-1}M+ + wedge^{k-1}"
                "tail1 exact in Q, k=1..12 (THEOREM D, PD half)"))

    # G15 K(q) closed form + strong-PD far instance
    q = sp.symbols("q", positive=True)
    k = sp.symbols("k", positive=True, integer=True)
    chain = k * q ** (k - 1) - (k + 1) * q ** k
    dec_ok = sp.simplify(sp.powsimp(sp.expand(
        chain - q ** (k - 1) * (k - (k + 1) * q)))) == 0
    kq_half = kq_exact(sp.Rational(1, 2)) == 1  # 2q at q=1/2
    kq_small = kq_exact(sp.Rational(1, 5)) == sp.Rational(2, 5)
    m2 = instance_masses(sp.Integer(A_INST), INST2_TRUE, INST2_NODE)
    q2 = 4 * m2["W"]
    ok15b = bool(q2 <= sp.Rational(1, 2)) and m2["Mm"] == 0
    d1_2 = m2["dks"][0]
    for k2 in range(2, 13):
        ok15b = ok15b and (m2["dks"][k2 - 1]
                           <= sp.Rational(4) ** (1 - k2) * d1_2)
    out.append(("G15-kq-strongPD", dec_ok and kq_half and kq_small
                and ok15b,
                "k q^{k-1} - (k+1)q^k == q^{k-1}(k - (k+1)q) exact "
                "(decreasing for q <= k/(k+1); K(q) = 2q for q <= "
                "1/2); INSTANCE 2 (far branch, q = %s <= 1/2): "
                "STRONG PD d_k <= 4^{1-k} d_1 exact k=2..12"
                % str(q2)))

    # G16 THEOREM D mixed instance (one undershoot)
    m3 = instance_masses(sp.Integer(A_INST), INST1_TRUE, INST3_NODE)
    ok16 = m3["Mm"] > 0
    for k3 in range(1, 13):
        lo = -k3 * m3["W"] ** (k3 - 1) * m3["Mm"]
        hi = (k3 * m3["W"] ** (k3 - 1) * m3["Mp"]
              + m3["wedge"] ** (k3 - 1) * m3["tail1"])
        ok16 = ok16 and (m3["dks"][k3 - 1] >= lo) \
            and (m3["dks"][k3 - 1] <= hi)
    out.append(("G16-thmD-mixed-instance", ok16,
                "INSTANCE 3 (one undershooting node, M- = %s > 0): "
                "two-sided -kW^{k-1}M- <= d_k <= kW^{k-1}M+ + "
                "wedge^{k-1}tail1 exact in Q, k=1..12 (THEOREM D)"
                % ("%.2e" % float(m3["Mm"]))))

    # G17 off-line modulus bound: |a+z|^2 - (|z|-a)^2 = 2a(x + |z|)
    x_, y_ = sp.symbols("x y", real=True)
    modz = sp.sqrt(x_ ** 2 + y_ ** 2)
    mod_az2 = (a + x_) ** 2 + y_ ** 2
    dev17 = sp.simplify(sp.expand(mod_az2 - (modz - a) ** 2
                                  - 2 * a * (x_ + modz)))
    R = sp.symbols("R", positive=True)
    mono = sp.simplify(sp.diff(a * R / (R - a) ** 2, R)
                       + a * (R + a) / (R - a) ** 3)
    out.append(("G17-offline-modulus", dev17 == 0 and mono == 0,
                "|a+z|^2 - (|z|-a)^2 == 2a(Re z + |z|) >= 0 ==> "
                "|w_a(z)| <= a|z|/(|z|-a)^2, decreasing in |z| for "
                "|z| > a (exact): hypothetical off-line pairs above "
                "the cited verification height are eps_off-bounded"))

    # G18 y-coordinate bridge (round-127 anchor)
    yb = a / (a + t ** 2)
    ok18 = (sp.simplify(yb * (1 - yb) - wexpr) == 0)
    zz = sp.symbols("z")
    ypart = sp.simplify(a / (a - zz) + a / (a - a ** 2 / zz) - 1)
    out.append(("G18-y-bridge", ok18 and ypart == 0,
                "y = a/(a+t^2): w == y(1-y) exact on the line; "
                "partner identity y(z) + y(a^2/z) == 1 exact "
                "(round-127 Lean anchor)"))
    return out


# --------------------------------------------------------- structure
def mp_E_eval(cell: dict, tval: float):
    """E(t) in mp at the cell's working precision (SL.trig_profile
    formula, mp coefficients)."""
    with mp.workdps(cell["dps"]):
        aa_mp = mp.log(cell["x"]) / 2
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]
        t = mp.mpf(repr(float(tval)))
        tot = mp.mpf(0)
        for k in range(cell["K"]):
            o = k * mp.pi / aa_mp

            def snc(u):
                return mp.sin(u) / u if u != 0 else mp.mpf(1)
            tot += cs[k] * aa_mp * (snc(aa_mp * (t - o))
                                    + snc(aa_mp * (t + o)))
        return tot


def raw_mp_census(cell: dict) -> np.ndarray:
    """AMENDMENT 1 node source: the SL.hp_zero_data mp path VERBATIM
    minus the f64 bisection refine (which damages deep-rung roots;
    see AMENDMENT 1 diagnosis)."""
    K = cell["K"]
    with mp.workdps(cell["dps"]):
        aa_mp = mp.log(cell["x"]) / 2
        b = [(k * mp.pi / aa_mp) ** 2 for k in range(1, K)]
        s_mp = b[-1] + 1
        b = [v / s_mp for v in b]
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]

        def pmul(p, q):
            out = [mp.mpf(0)] * (len(p) + len(q) - 1)
            for i, pv in enumerate(p):
                for j, qv in enumerate(q):
                    out[i + j] += pv * qv
            return out

        def padd(p, q):
            if len(p) < len(q):
                p, q = q, p
            out = list(p)
            off = len(p) - len(q)
            for j, qv in enumerate(q):
                out[off + j] += qv
            return out

        def deflate(p, root):
            out = [p[0]]
            for c in p[1:-1]:
                out.append(c + out[-1] * root)
            return out

        prod_all = [mp.mpf(1)]
        for bj in b:
            prod_all = pmul(prod_all, [mp.mpf(1), -bj])
        poly = [2 * cs[0] * c for c in prod_all]
        for i, k in enumerate(range(1, K)):
            q = deflate(prod_all, b[i])
            term = [2 * cs[k] * ((-1) ** k) * c for c in q] \
                + [mp.mpf(0)]
            poly = padd(poly, term)
        rts = mp.polyroots(poly, maxsteps=300,
                           extraprec=cell["dps"])
        roots = np.array([complex(r) for r in rts]) * float(s_mp)
    real_y = roots[(np.abs(roots.imag) <= 1e-10 * float(s_mp))
                   & (roots.real > 0)]
    return np.sort(np.sqrt(real_y.real))


def eps_off(a: float) -> float:
    return 2.0 * a * (math.log(H_VERIF) + 1.0) / H_VERIF


def w_of(a: float, ts: np.ndarray) -> np.ndarray:
    return a * ts ** 2 / (a + ts ** 2) ** 2


def kq_float(q: float) -> float:
    if q >= 1.0:
        return float("inf")
    khi = max(3, int(math.ceil(q / (1.0 - q))) + 2)
    return max(k * q ** (k - 1) for k in range(2, khi + 1))


def rung_masses(mus: np.ndarray, gam: np.ndarray, a: float) -> dict:
    """Sorted-pairing masses (ward currency: cache gammas)."""
    n = len(mus)
    wmu = w_of(a, mus)
    wga = w_of(a, gam[:n])
    dw = wga - wmu
    Mp = float(np.sum(np.clip(dw, 0.0, None)))
    Mm = float(np.sum(np.clip(-dw, 0.0, None)))
    t0 = min(float(mus[0]), float(gam[0]))
    W = float(w_of(a, np.array([t0]))[0])
    wedge = float(w_of(a, np.array([float(gam[n])]))[0])
    tail1 = R4.ward_c01(gam, float(a)) \
        - float(np.sum(w_of(a, gam[:n])))
    return dict(Mp=Mp, Mm=Mm, W=W, wedge=wedge, tail1=tail1, t0=t0,
                n=n)


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("wpd_proof_probe -- PRIME.WPD.INTERLACING.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    ladder = LADDER[:2] if smoke else LADDER
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

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
    section("S1  EXACT LAYER (THEOREM D / W1 / P1 / B inputs)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("THEOREM D stated: sorted real multisets on the branch "
         "[t0, inf), t0 > sqrt a: -kW^{k-1}M- <= d_k <= kW^{k-1}M+ "
         "+ wedge^{k-1}tail1 for all k (W = w(t0)); COROLLARY W1: "
         "|d_k| <= C_pred 4^{1-k} d_1 with C_pred = [K(4W)(M+ + M-)"
         " + tail1]/d_1 -- WPD with uniform C reduces to the mass-"
         "ratio bound (MRB); COROLLARY P1: M- = 0 ==> PD; q = 4W "
         "<= 1/2 + tail-dominance ==> strong round-128 PD form")
    info("consumed, cited: round-114 block realness (node side); "
         "classical verification to H = 3e12 (tail realness; "
         "corpus v914 input); round-128 Theorem R + round-122 "
         "NF-closure (the chain in S5)")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS (round-128 jet machinery)")
    pts = []
    with mp.workdps(DL.JET_DPS):
        for a in A_BAT:
            am = mp.mpf(a)
            for j in (0, DL.JET_M // 4, DL.JET_M // 2):
                th = 2 * mp.pi * j / DL.JET_M
                pts.append(mp.mpf("0.5")
                           + mp.sqrt(am + am / 2 * mp.exp(1j * th)))
    demA = audit_em_dev(pts)
    check("G20-em-audit", demA <= BAR_EM_AUDIT,
          "own EM zeta vs audit mp.zeta at %d jet points: max rel "
          "%.1e (bar %.0e)" % (len(pts), demA, BAR_EM_AUDIT),
          kind="edge")

    jets = {}
    ok21 = True
    det21 = []
    for a in A_BAT:
        t0j = time.time()
        jets[a] = DL.cauchy_jet(DL.em_log_phi, a, JET_NC)
        with mp.workdps(DL.JET_DPS):
            am = mp.mpf(a)
            F = mp.diff(DL.em_log_phi, am)
            Fp = mp.diff(DL.em_log_phi, am, 2)
            c01_diff = mp.re(am * F + am * am * Fp)
            c01_jet = am * jets[a][1] + 2 * am * am * jets[a][2]
            dev_c1 = float(abs(jets[a][1] - mp.re(F)) / abs(mp.re(F)))
            dev_c01 = float(abs(c01_jet - c01_diff) / abs(c01_diff))
        det21.append("a=%d: c1 %.1e C01 %.1e (%.0f s)"
                     % (a, dev_c1, dev_c01, time.time() - t0j))
        ok21 = ok21 and dev_c1 <= BAR_JET_XW and dev_c01 <= BAR_JET_XW
    check("G21-jet-cross-ward", ok21,
          "Cauchy jet vs mp.diff: " + "; ".join(det21), kind="edge")

    c0k = {a: DL.c0k_from_jet(a, jets[a], K_PRED) for a in A_BAT}
    c01 = {a: float(c0k[a][0]) for a in A_BAT}
    ok22 = True
    det22 = []
    for a in A_BAT:
        wc = R4.ward_c01(gam, float(a))
        dev1 = abs(c01[a] - wc) / abs(wc)
        worst_k = 0.0
        for k in range(2, K_PRED + 1):
            cs = float(np.sum(w_of(float(a), gam) ** k))
            worst_k = max(worst_k,
                          abs(float(c0k[a][k - 1]) - cs)
                          / max(abs(cs), 1e-300))
        ok22 = ok22 and dev1 <= BAR_C01_WARD and worst_k <= BAR_C0K_WARD
        det22.append("a=%d: C01 %.1e, C0k(k<=%d) %.1e"
                     % (a, dev1, K_PRED, worst_k))
    check("G22-c0k-cache-ward", ok22,
          "jet targets vs cache(+RvM tail at k=1): "
          + "; ".join(det22), kind="edge")

    # ---------------------------------------------------------- S3
    section("S3  STRUCTURE (sign census, masses, THEOREM-D gates)")
    t0b = time.time()
    ce3 = R4.build_cell(3, KFAC, "MAIN", 45, want_mp=False)
    sl3 = SL.build_trig_cell_hp(3, KFAC, "MAIN", 45)
    dev_e = float(np.max(np.abs(ce3["m_tilde"] - sl3["m_tilde"])))
    check("G30a-ward-x3", dev_e <= BAR_WARD_X3,
          "own(R4) vs SL build x=3 even: %.1e (%.0f s)"
          % (dev_e, time.time() - t0b), kind="edge")

    cells = {3: ce3}
    for x, dps in ladder:
        if x in cells:
            continue
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=(x == 5))
        cells[x] = ce
        print("  x=%d built (K=%d, %.0f s)" % (x, ce["K"],
                                               ce["build_s"]),
              flush=True)

    # census (AMENDMENT 1: raw mp roots) + operator cross-ward
    ok30b = True
    ok30c = True
    det30 = []
    det30c = []
    nodes = {}
    for x, dps in ladder:
        ce = cells[x]
        if "zeros" not in ce:
            SL.hp_zero_data(ce)
        refined = np.asarray(ce["zeros"], float)
        mus = raw_mp_census(ce)
        nodes[x] = mus
        res = max(float(abs(mp_E_eval(ce, m))) for m in mus)
        shift = (float(np.max(np.abs(mus - refined)))
                 if len(mus) == len(refined) else float("nan"))
        ok30c = ok30c and len(mus) == len(refined) and res <= RES_BAR
        det30c.append("x%d: n %d==%d, max|E(root)| %.0e, refine-"
                      "artifact max shift %.1e"
                      % (x, len(mus), len(refined), res, shift))
        if x in (3, 5):
            co = R4.build_cell(x, KFAC, "MAIN", dps, sector="odd")
            ops = R4.build_ops(ce, co)
            if ops["Meta"] is not None:
                pos, imrel = R4.spec_pos(ops["Meta"])
                nn = min(len(pos), len(mus))
                cdev = float(np.max(np.abs(pos[:nn] - mus[:nn])
                                    / mus[:nn]))
                ok30b = ok30b and imrel <= BAR_REAL \
                    and cdev <= BAR_SPEC_CENSUS
                det30.append("x%d: im %.0e specVcensus %.0e"
                             % (x, imrel, cdev))
            else:
                det30.append("x%d: eta-degenerate" % x)
        else:
            det30.append("x%d: census-only (eta-degenerate, "
                         "r122/r128 pattern)" % x)
    check("G30b-spec-census", ok30b, "; ".join(det30))
    check("G30c-raw-census-residual", ok30c,
          "AMENDMENT 1 node source: raw mp polynomial roots, "
          "certified by mp E-evaluation (bar %.0e); the f64-refine "
          "artifact exhibited: %s" % (RES_BAR, "; ".join(det30c)))

    xs = [x for x, _d in ladder]
    # G31 branch gate
    ok31 = True
    det31 = []
    for x in xs:
        t0x = min(float(nodes[x][0]), float(gam[0]))
        marg = t0x - math.sqrt(max(A_BAT))
        ok31 = ok31 and marg > 0
        det31.append("x%d: t0 %.4f - sqrt(%d) = %.4f" %
                     (x, t0x, max(A_BAT), marg))
    check("G31-branch-gate", ok31,
          "min(mu_1, gamma_1) > sqrt(a) for every battery a: "
          + "; ".join(det31)
          + " -- single-branch theorem valid for a < gamma_1^2 = "
          "%.2f" % (float(gam[0]) ** 2))

    # G32 sign census
    dom_onesided = []
    dom_layer = []
    ok32 = True
    for x in xs:
        mus = nodes[x]
        n = len(mus)
        gs = gam[:n]
        diffs = mus - gs
        cert = np.abs(diffs) / np.maximum(mus, 1.0) >= SIGN_FLOOR
        cu = int(np.sum((diffs < 0) & cert))
        co_ = int(np.sum((diffs > 0) & cert))
        un = int(n - cu - co_)
        print("  x=%-2d sign census: certified over %d, certified "
              "UNDER %d, uncertified(|d|<%.0e rel) %d of %d"
              % (x, co_, cu, SIGN_FLOOR, un, n))
        under_rows = [(i, mus[i], gs[i], diffs[i]) for i in range(n)
                      if diffs[i] < 0 and cert[i]]
        for i, mu, g, d in under_rows:
            print("    UNDERSHOOT i=%2d mu=%12.6f gamma=%12.6f "
                  "diff=%+.3e" % (i, mu, g, d))
        if cu == 0:
            dom_onesided.append(x)
        else:
            dom_layer.append(x)
            ok32 = False
    check("G32-sign-census", ok32,
          "AMENDMENT 1 criterion (raw currency): ZERO certified "
          "undershoots at every rung -- DOM-ONE-SIDED at x=%s%s: "
          "every certified node deviation is an OVERSHOOT, growing "
          "toward the band edge (counting dominance mu_i >= "
          "gamma_i at every certified site; Lemma-S sub-multiset "
          "hypothesis carried at the certification floor)"
          % (dom_onesided,
             ("; certified undershoots at x=%s (layer verdict "
              "path re-engaged)" % dom_layer) if dom_layer else ""))

    # G33 masses + theta ladder + recomposition
    masses = {}
    ok33 = True
    det33 = []
    for x in xs:
        for a in A_BAT:
            m = rung_masses(nodes[x], gam, float(a))
            masses[(x, a)] = m
            d1_jet = c01[a] - float(np.sum(w_of(float(a), nodes[x])))
            recomp = m["Mp"] - m["Mm"] + m["tail1"]
            dev = abs(recomp - d1_jet) / abs(d1_jet)
            th = m["Mm"] / d1_jet
            ok33 = ok33 and dev <= 10 * BAR_C01_WARD \
                and th <= THETA_BAR and d1_jet > 0
            m["d1"] = d1_jet
        det33.append("x%d: theta-(a=4) %.1e" %
                     (x, masses[(x, 4)]["Mm"] / masses[(x, 4)]["d1"]))
    for a in A_BAT:
        info("mass ladder a=%d: " % a + "; ".join(
            "x%d: d1 %.5f M+ %.1e M- %.1e tail1 %.5f" %
            (x, masses[(x, a)]["d1"], masses[(x, a)]["Mp"],
             masses[(x, a)]["Mm"], masses[(x, a)]["tail1"])
            for x in xs))
    check("G33-mass-split", ok33,
          "d1(jet) == M+ - M- + tail1 (ward recomposition, bar "
          "%.0e); theta- = M-/d1 <= %.0e at every rung/a (%s); "
          "d1 > 0 everywhere (no degree-1 exactness: the "
          "quadrature mechanism's death certificate)"
          % (10 * BAR_C01_WARD, THETA_BAR, "; ".join(det33)))

    # G34 THEOREM-D prediction gate
    ok34 = True
    worst34 = 0.0
    npred = 0
    for x in xs:
        mus = nodes[x]
        for a in A_BAT:
            m = masses[(x, a)]
            eo = eps_off(float(a))
            for k in range(2, K_PRED + 1):
                trk = float(math.fsum(w_of(float(a), mus) ** k))
                dk = float(c0k[a][k - 1]) - trk
                floor = 1e-13 * (abs(float(c0k[a][k - 1])) + trk) \
                    + 1e-40
                hi = (k * m["W"] ** (k - 1) * m["Mp"]
                      + m["wedge"] ** (k - 1) * m["tail1"]
                      + eo + floor)
                lo = -(k * m["W"] ** (k - 1) * m["Mm"] + eo + floor)
                okk = lo <= dk <= hi
                ok34 = ok34 and okk
                npred += 1
                if hi > 0:
                    worst34 = max(worst34, dk / hi)
    check("G34-thmD-prediction", ok34,
          "measured jet d_k inside [-kW^{k-1}M- - eps, kW^{k-1}M+ "
          "+ wedge^{k-1}tail1 + eps] at all %d (rung, a, k<=%d) "
          "cells; worst upper-bound saturation %.3f"
          % (npred, K_PRED, worst34))

    # G35 WPD constant gate + MRB ladder
    ok35 = True
    cpred_tab = {a: [] for a in A_BAT}
    worst_cm = 0.0
    for x in xs:
        mus = nodes[x]
        for a in A_BAT:
            m = masses[(x, a)]
            q = 4.0 * m["W"]
            cpred = (kq_float(q) * (m["Mp"] + m["Mm"])
                     + m["tail1"]) / m["d1"]
            cpred_tab[a].append(cpred)
            cms = 0.0
            for k in range(2, K_MOM + 1):
                trk = float(math.fsum(w_of(float(a), mus) ** k))
                dk = float(c0k[a][k - 1]) - trk
                cms = max(cms, abs(dk) * 4.0 ** (k - 1) / m["d1"])
            worst_cm = max(worst_cm, cms)
            ok35 = ok35 and cms <= cpred and cpred <= CPRED_BAR
    for a in A_BAT:
        info("C_pred ladder a=%d: %s (q = 4 w_a(t0) = %.4f <= 1/2: "
             "strong-PD criterion holds on the battery)"
             % (a, ["%.4f" % c for c in cpred_tab[a]],
                4.0 * masses[(xs[-1], a)]["W"]))
    check("G35-wpd-constant", ok35,
          "C_meas (k<=%d, r128 convention) <= C_pred = [K(q)(M+ + "
          "M-) + tail1]/d1 <= %.1f at every rung/a (worst C_meas "
          "%.4f) -- WPD with an EXPLICIT uniform constant, modulo "
          "the measured mass ratios (MRB)"
          % (K_MOM, CPRED_BAR, worst_cm))

    # G36 rung-to-rung matched-prefix descent (compression evidence)
    ok36 = True
    det36 = []
    for i in range(len(xs) - 1):
        m_sh, m_dp = nodes[xs[i]], nodes[xs[i + 1]]
        npfx = 0
        for j in range(min(len(m_sh), len(m_dp))):
            if (abs(m_sh[j] - gam[j]) < 0.5 * gam[j]
                    and abs(m_dp[j] - gam[j]) < 0.5 * gam[j]):
                npfx = j + 1
            else:
                break
        asc = int(np.sum(m_dp[:npfx] > m_sh[:npfx] + 1e-12))
        ok36 = ok36 and asc == 0
        det36.append("x%d->x%d: prefix %d, ascents %d"
                     % (xs[i], xs[i + 1], npfx, asc))
    check("G36-node-descent", ok36,
          "matched-prefix nodes DESCEND rung-to-rung (%s): the "
          "compression-type evidence -- nodes approach the true "
          "zeros from above (raw currency, AMENDMENT 1)"
          % "; ".join(det36))

    # G37 quadrature adjudication verdict
    check("G37-quadrature-dead", all(masses[(x, a)]["d1"] > 0
                                     for x in xs for a in A_BAT),
          "no polynomial exactness at ANY degree (d_1 > 0 at every "
          "rung/a) + G11 sign flip: the finite trace formula is "
          "NOT a Gauss/Markov quadrature of the true measure -- "
          "MECHANISM-COMPRESSION-NOT-QUADRATURE")

    # G38 Z1 / ward typing
    check("G38-ward-typing", True,
          "the sign census, masses and dominance reads consume the "
          "X5 cache (ward currency): DOM evidence is TRANSCRIPTION-"
          "ADJACENT by construction (r122/r128 conviction); the "
          "residual wall is the SOURCE-SIDE one-sided node law -- "
          "strictly weaker than L1's node convergence (only "
          "one-sidedness + mass ratio needed)")

    # G39 perturbation screen
    ce5 = cells[5]
    with mp.workdps(ce5["dps"]):
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G39-perturbation-screen", 1e-40 < d_eps < 1e-10,
          "1e-25 shift on Q[0,0] at x=5 moves eps by %.1e (nonzero "
          "and bounded; round-118 red flag; all mp under workdps)"
          % d_eps, kind="edge")

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS (arithmetic-content adjudication)")
    ctrl_ok = True
    ctrl_rows = []
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw,
                           want_mp=(world != "EPSTEIN"))
        musw = raw_mp_census(cw)   # AMENDMENT 1 currency
        nW = len(musw)
        under = int(np.sum(musw < gam[:nW]))
        frac = under / max(nW, 1)
        d1s = []
        branch_fail = []
        for a in A_BAT:
            d1w = c01[a] - float(np.sum(w_of(float(a), musw)))
            d1s.append(d1w)
            if musw[0] <= math.sqrt(a):
                branch_fail.append(a)
        pd_false = all(d < D1_CTRL for d in d1s)
        dom_false = frac >= UNDER_FRAC
        ctrl_ok = ctrl_ok and pd_false and dom_false
        ctrl_rows.append("%s x=%d: mu_1 %.3f, undershoot %d/%d, "
                         "d1 %s, branch FAILS at a=%s"
                         % (world, xw, musw[0], under, nW,
                            ["%.3f" % d for d in d1s], branch_fail))
        okw = check("G40-%s" % world.lower(), pd_false and dom_false,
                    ctrl_rows[-1])
        ctrl_ok = ctrl_ok and okw
    check("G43-mechanism-consistency", ctrl_ok,
          "PD is FALSE in every control world (d1 < %.2f at every "
          "battery a) AND the THEOREM-D hypothesis set (dominance; "
          "branch) FAILS there: the mechanism never claims PD "
          "where PD is false -- PD-WORLD-SEPARATING: WPD's "
          "arithmetic content at battery a IS the one-sided node "
          "law (from-below + dominance), NOT zero; the omega does "
          "NOT concentrate in L1 alone" % D1_CTRL)

    # ---------------------------------------------------------- S5
    section("S5  CHAIN + MIN-CUT")
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
                ("NFCLOS", "L1N"): 1, ("L1N", "DOMN"): 1,
                ("DOMN", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "L1N"): 1, ("L1N", "R4HYP"): INF,
               ("NFCLOS", "DOMN"): 1, ("DOMN", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G50-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach and "NFCLOS" in reach,
          "flows: base 4, series-refined 5 (the round-128 WPDN "
          "node REFINED: at battery a WPD is carried by DOMN = "
          "{d_1 > 0, MRB} via THEOREM D/W1; the window-scale part "
          "WPDWIN stays RH-equivalent-at-the-tail and rides the "
          "same series edge), counterfactual parallel 6 (NOT "
          "REAL); census {MEAS, OMEGA-POS} unchanged, cardinality "
          "4; RH unreachable without an omega edge")
    info("EXACT RESIDUE after this round: RH <== [r122 NF-closure, "
         "cited] + [r128 Theorem R, cited] + {L1(a), WPD(a)} dense; "
         "THIS ROUND: WPD(a) for a < gamma_1^2 <== THEOREM D/W1 "
         "(proven, explicit C_pred) + {d_1 > 0, mass-ratio bound "
         "MRB} (measured, ward currency, one-sided node law -- "
         "strictly weaker than node convergence); WPD(a) at window "
         "scale (a ~ gamma^2 of a hypothetical off-line zero, "
         "beyond a = H^2 ~ 9e24 given the cited verification) "
         "remains window positivity itself (r128 G26).  PD is "
         "world-separating (S4): its content is arithmetic.")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "THMD-PROVEN(two-sided defect bounds, exact: G12/G13 "
        "general-k algebra + G14/G15/G16 rational instances; "
        "COROLLARY W1 explicit WPD constant C_pred = [K(4W)(M+ + "
        "M-) + tail1]/d_1; COROLLARY P1 PD under one-sided "
        "dominance; strong-PD criterion 4W <= 1/2 holds on the "
        "whole battery)",
        "BRANCH-THEOREM(w strictly decreasing on (sqrt a, inf), "
        "exact; single-branch valid for a < gamma_1^2 = 199.79; "
        "battery margin 10.13)",
        "MECHANISM-COMPRESSION-NOT-QUADRATURE(G33/G37: d_1 > 0 = "
        "no polynomial exactness; G11 Markov sign flip exact; "
        "G36 node descent = compression-type evidence)",
        ("DOM-ONE-SIDED(x=%s%s; AMENDMENT 1: the run-1 'boundary "
         "layer' and the r128 negative high-k PD floor are the "
         "SAME f64-refine instrument artifact, exhibited and "
         "retired -- in raw mp currency every certified deviation "
         "is an overshoot)" % (dom_onesided,
                               "; UNDER at x=%s" % dom_layer
                               if dom_layer else "")),
        "WPD-EXPLICIT-CONSTANT(C_meas worst %.4f <= C_pred <= %.1f "
        "at every rung/a; MRB ladder printed)" % (worst_cm,
                                                  CPRED_BAR),
        "CONTROLS-SEPARATE(PD false in SMOOTH/SCRARITH/EPSTEIN at "
        "every battery a; dominance and branch hypotheses fail "
        "exactly there: WPD's arithmetic content at battery a is "
        "the one-sided node law, NOT zero)",
        "WARD-CURRENCY(sign census + masses consume the X5 cache; "
        "source-side one-sidedness is the remaining wall, weaker "
        "than L1's node convergence)",
        "MINCUT-REFINED(4 -> 5, WPDN split into DOMN -> WPDWIN in "
        "series, census {MEAS, OMEGA-POS} unchanged)"]
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
        print("COMPOSITE: THMD-PROVEN + BRANCH-THEOREM + "
              "MECHANISM-COMPRESSION-NOT-QUADRATURE + "
              "DOM-ONE-SIDED(raw currency, AMENDMENT 1) + "
              "WPD-EXPLICIT-CONSTANT + CONTROLS-SEPARATE + "
              "WARD-CURRENCY + MINCUT-REFINED")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
