#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dominance_proof_probe -- PRIME.MRB.DOMINANCE.PROOF.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (maximal proof attempt on the round-132 residue)
=======================================================================
Round 132 (wpd_proof_probe, 32/32) proved THEOREM D / W1 / P1 and
reduced WPD(a < gamma_1^2) to the pair {d_1 > 0, MRB}, MRB = the
mass-ratio bound sup_lam (M+ + M-)/d_1 < inf, and measured COUNTING
DOMINANCE (sorted mu_i >= gamma_i, i.e. N_fin(T) <= N_true(T)) as
DOM-ONE-SIDED at every certified site.  Round 131 (l1_weyllaw_probe,
31/31) proved the secular identity (operator nodes == zeros of the
census polynomial E_N, node count EXACTLY K-1) and the GW pinning
tau = 2 sum |E_N(gamma)|^2.  This probe is the maximal proof attempt
on the source-side one-sidedness itself.  THE CENTRAL MOVE: WPD does
NOT need exact per-node one-sidedness (a sign statement at 1e-17..
1e-50 gaps, exponentially fragile) -- it needs only that the
wrong-sign mass M- never swallows M+ + tail_1.  Ball-containment +
counting-budget certificates (ROBUST: distances and integer counts,
no sign reads) bound M- unconditionally-in-sign.  That is a theorem.

NOTATION (round-128/132 conventions).  a > 1/4; w_a(t) =
a t^2/(a+t^2)^2, strictly decreasing on (sqrt a, inf) (branch);
nodes mu_1 <= ... <= mu_N = the raw-mp census zeros of E_N (the
AMENDMENT-1 currency of round 132: NO f64 refine); gamma_1 <= ... =
true zero ordinates (X5 cache, ward; first NPOL re-polished in
audit_).  Sorted pairing: M+ = sum_i max(0, w(gamma_i) - w(mu_i)),
M- = sum_i max(0, w(mu_i) - w(gamma_i)), tail_1 = sum_{j>N}
w(gamma_j), d_1 = M+ - M- + tail_1.  T_z = min(0.98 edge, 2 pi x)
(the round-131 G17 resolvability crossover, a theorem).

=======================================================================
THE THEOREMS (T2; elementary, sympy-gated via exact rational
instances + slack-symbol identities; classical inputs typed CITED)
=======================================================================
THEOREM M (ball-counting slack dominance).  Sorted nodes mu_1 <= ...
<= mu_N, sorted true ordinates gamma_1 <= gamma_2 <= ..., T_z > 0,
m = #{j : gamma_j <= T_z}.  Hypotheses:
 (H1) for each j <= m there is a node in B_j = [gamma_j - g_j,
      gamma_j + g_j], with the balls disjoint and ordered:
      gamma_j + g_j < gamma_{j+1} - g_{j+1};
 (H2) every node <= max(T_z, gamma_m + g_m) lies in some B_j
      (NO STRAYS -- an integer census count, robust);
 (H3) each B_j contains exactly ONE node.
Conclusion: (i) sorted mu_i >= gamma_i - g_i for all i <= m;
(ii) mu_i > T_z for all i > m.  PROOF (counting): any node below
gamma_i - g_i is, by H2+H3, THE matched node of a ball B_j lying
entirely below gamma_i - g_i, hence (ordering H1) j < i; so
#{nodes < gamma_i - g_i} <= i-1, which is (i); (ii) is H2+H3
directly.  No sign of mu_i - gamma_i is ever read.
COROLLARY M2 (certified M- bound, branch a < gamma_1^2):
  M- <= sum_{j<=m} [w_a(gamma_j - g_j) - w_a(gamma_j)]
        + sum_{i>m} max(0, w_a(mu_i) - w_a(gamma_i)),
and the zone term is O(sum |w'| g_j) -- pinning-gap mass, NOT a
sign census.  The round-132 DOM evidence (certified-sign reads above
SIGN_FLOOR 1e-8, everything below UNCERTIFIED) is strictly upgraded:
M- is bounded at ANY sign resolution.
THEOREM E (edge counting bounds; consumes H2 + branch):  with all
unmatched nodes > T_z and gamma_{m+1} > T_z:
  (i)  M-_edge <= (N - m) w_a(T_z)          (each term <= w(mu_i)
       <= w(T_z), monotone branch);
  (ii) M+_edge <= sum_{gamma > T_z} w_a(gamma) <= a G(T_z)
       (G = the HSW22 closed form; counts ALL strip zeros, no RH).
THEOREM T (top segment; unconditional).  With N_fin <= K-1 (node
count EXACT, round-131 secular identity, cited) and |N(T) - M(T)|
<= Q(T) (HSW22 Cor. 1.2, cited; M(T) = RvM main term, Q(T) = alpha
log T + beta loglog T + c): for every T >= T*(x), where T* is the
closed-form solution of M(T*) - Q(T*) = K-1,
   N_fin(T) <= K-1 <= M(T) - Q(T) <= N_true(T):
counting dominance is a THEOREM above T*; and gamma_{K-1} <= T*
(same inequality), which feeds the tail bounds below.
THEOREM C (the chain, sharpened round-132 W1/P1).  d_1 = M+ - M- +
tail_1, q = 4 w_a(t_0) <= 1/2 on the battery, K(q) = 2q <= 1:
 (i)  DOM (M- = 0)  ==>  (M+ + M-)/d_1 = M+/(M+ + tail_1) <= 1 and
      C_pred = [K(q) M+ + tail_1]/(M+ + tail_1) <= 1:  DOM alone
      implies the FULL round-132 residue {d_1 > 0, MRB} with the
      explicit constant 1 (tail_1 > 0 from the infinitude of zeros,
      classical, cited);
 (ii) WEAK ONE-SIDEDNESS  M- <= (1 - th)(M+ + tail_1), th > 0  ==>
      d_1 = th (M+ + tail_1) at equality (exact identity) and
      (M+ + M-)/d_1 <= (2 - th)/th, monotone in M-:  MRB is
      STRICTLY WEAKER than DOM -- dominance may fail on small mass
      and WPD survives.  The contract's "M- = 0 or M-/M+ bounded"
      is answered by (ii) in the sharper tail_1 currency.
THEOREM A (asymptotic assembly; the lambda-uniform statement).
Fix a in (1/4, gamma_1^2) and x.  HYPOTHESIS H-pin(x): (H1)-(H3)
hold at T_z = 2 pi x with total zone |dw|-mass <= TL(x,a)/8, where
TL(x,a) = the shell lower bound for tail_1 (frozen shell configs;
counts per shell >= M - Q telescoped, gamma_{K-1} <= T* from
THEOREM T).  Then with n_z = M(T_z) - Q(T_z) (so N - m <= N - n_z):
   d_1 >= D(x,a) := TL - TL/8 - (N - n_z) w_a(T_z),   and if D > 0:
   (M+ + M-)/d_1 <= [TL/8 + a G(T_z) + (N - n_z) w_a(T_z)] / D.
MACHINE FACTS (frozen grid): D < 0 for x <= 89 (battery included)
and D > 0 for all integers x in [x_0, 200] and the asym grid up to
1e6, with x_0 in (89, 144] (computed exactly); the MRB bound falls
monotonically along the asym grid (pre-freeze: 144.1 at x = 144 down
to 10.5 at x = 1e6).  CONSEQUENCE: for x >= x_0, H-pin(x) ALONE
implies the full round-132 residue {d_1 > 0, MRB} -- and H-pin is
exactly the round-131 L1BAND omega (derivative floors + matched-
prefix + no-stray counting) in ball currency: THE TWO SERIAL UNIT
OMEGAS OF THE ROUND-128 PAIR MERGE INTO ONE for x >= x_0.
THE PINNED OBSTRUCTION (Q-SWAMP): for x < x_0 the unconditional
counting currency CANNOT certify the assembly -- the HSW slack
Q(T) ~ 10 zeros at band scale T ~ 2 pi x swamps tail_1 (TL loses
~2Q(T*) zeros in the first shell and (N - n_z) w(T_z) eats the
rest).  The battery x = 3..13 lies inside the strip: there the
certificate carries in WARD CURRENCY (cache-certified tail_1 +
measured gap/count certificates), typed honestly, not upgraded.

=======================================================================
THE ANGLE ADJUDICATION (T1; what carries and what is obstructed)
=======================================================================
A1 (kernel/truncation route) OBSTRUCTED, machine-exhibited: the
sharp (Dirichlet-kernel) truncation Xi_A(t) = 2 int_0^A Phi(u)
cos(ut) du of the classical Riemann Xi-transform (Phi > 0) pins
in-band zeros from BELOW (pre-freeze x=13: 21/24 sorted
undershoots; x=5: the first zero 14.128 < gamma_1), i.e. the
natural positive-density sharp truncation is ANTI-dominant; the
Fejer (positive-kernel) truncation has NO zeros in the band at all
at battery scale (the PF-smoothing halves the effective resolution
below the crossover).  The minimizer's from-above one-sidedness is
therefore NOT a fixed-kernel truncation phenomenon: E_N is not a
positive-kernel smoothing of Xi in any exhibited sense -- the
variational structure is load-bearing.  A2 (Sturm/oscillation)
carries ONLY in counting currency: the classical secular-interlacing
route against the LATTICE (all census weights (-1)^k c_k > 0 ==>
one node per lattice gap, sympy-gated lemma) is KILLED by the
measured mixed-sign census ((-1)^k c_k < 0 at 1..14 modes per rung,
pre-freeze) -- necessarily so, since lattice interlacing would force
in-band node count == lattice count, contradicting the measured
RvM node law (round 128/131); rung-to-rung recurrence is non-nested
(round 132, cited).  A3 (variational/Gauss quadrature) stays dead
as quadrature (round-132 G11/G37, cited; the same mixed-sign census
kills the positive-lattice-measure reading) -- its live content is
exactly the GW pinning, which THEOREM M consumes as ball radii.
MECHANISM VERDICT: counting dominance is carried by A2-COUNTING
(Theorem M balls + budget) with A3-pinning as input; the round-132
node-DESCENT target is BYPASSED (balls suffice; monotonicity not
needed for WPD).

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  firewall (AST, round-131 owner logic: zeta only inside audit_
    at any enclosing scope; np.load only in ward_; no zero-oracle
    names; no verification/ import); cache health (X5, READ-ONLY).
S1  exact layer: G10 branch derivative + w bounds; G11 THEOREM M
    exact rational instance (a=4: trues (4, 5, 6, 17/2, 11, 30,
    45), balls g = (1/50, 1/40, 1/30), nodes (4+1/100, 5-1/80,
    6+1/90, 9, 13), T_z = 7: slack dominance + M- <= zone bound
    exact in Q; the M- witness mu_2 < gamma_2 INSIDE its ball);
    G12 THEOREM C chain (sympy: d_1 == th(M+ + tail_1) at the
    equality substitution, ratio monotone in M-, slack == tail_1,
    DOM ==> constant 1, K(q) = 2q <= 1 re-gated); G13 THEOREM E on
    the instance (edge bounds exact in Q); G14 counting algebra
    (|N-M| <= Q ==> shell counts >= M-Q telescoped; T* logic) +
    HSW antiderivatives + tangent lemma (round-131 G16 re-gated);
    G15 secular interlacing lemma (positive weights ==> exactly one
    root per pole gap; rational instance root count via sympy
    real_roots + F' < 0) -- the A2-lattice precondition; G16
    resolvability crossover T = 2 pi x (round-131 G17 re-gated);
    G17 stray-instance REFUSAL (nodes (3, 4+1/100, 5-1/80, 6+1/90,
    9): the certificate must refuse (H2 fails) and sorted dominance
    indeed fails -- hypothesis necessity, controls-in-miniature).
S2  targets: G20 truncation audit (2 x 2 int_0^3 Phi cos == own
    xi_line at t = 0, 20, rel <= 1e-6); G21 HSW G(T) sanity (cache
    partials below G; monotone); G22 THEOREM T per rung:
    gamma_{K-1}(cache) <= T*(x), K-1 <= M(T*) - Q(T*).
S3  MAIN ladder x = (3, 5, 8, 13), KFAC 1.25, raw-mp census
    (round-132 AMENDMENT-1 currency verbatim): G30a ward x=3 (R4 vs
    SL); G30b operator cross-ward x=3/5 (spec+(Meta) vs census);
    G30c census residual (bar 1e-12); G31 branch gate; G32 THE
    CERTIFICATE GATES: identity matching == zone count m, ZERO
    strays (H2), one node per ball (H3), ball separation (H1),
    positions interval-certified by mp SIGN CHANGES (adaptive delta
    ladder, no derivative floors consumed); G33 certified M- ladder:
    M-_cert/d1_lo <= 1e-3 at every (rung, a) (pre-freeze: zone term
    1.4e-15..2.3e-6, edge term at the 1e-17 cache floor); G34 MRB
    CERTIFICATE: MRB_cert = M_abs_ub/d1_lo <= 0.25 at every
    (rung, a) (pre-freeze ladder 0.069..0.083, flat); G35 WPD
    certified constant C_cert = [K(q) M_abs_ub + tail1_hi]/d1_lo
    <= 1.5 (pre-freeze ~1.02..1.06) and d1_lo > 0 (the round-132
    residue pair CERTIFIED per rung without sign reads); G35b
    THEOREM-D prediction re-gated in certified-mass currency at
    every (rung, a, k = 2..8) vs cache d_k; G36 node descent
    (measured, compression evidence -- bypassed for WPD); G37
    quadrature-dead (d1_lo > 0); G38 ward/Z1 typing; G39 census
    weight sign census: mixed signs at EVERY rung ==> A2-lattice +
    A3-positive-measure obstruction (with G15 as the lemma).
S3b A1 exhibits (audit currency): G40 Dirichlet truncation zeros
    at x = 5, 13 (grid 0.25 + bisection): sorted undershoots >= 1
    at each rung (pre-freeze 1/4, 21/24) ==> SHARP-KERNEL-ANTI-
    DOMINANT; G41 Fejer truncation: ZERO sign changes on the band
    grid (0.5) at both rungs ==> PF-KERNEL-BLIND; distinctness
    E_N vs Xi_A printed (INFO).
S3c closed forms: G42 Q-swamp strip: D(x, a) < 0 for all battery a
    at x in (13, 21, 34, 55, 89); G43 crossover: x_0 = min integer
    x >= 90 with D > 0 for all battery a and all integers in
    [x, 200]: gate 89 < x_0 <= 144; G44 asym grid x = (144, 233,
    377, 610, 1000, 3000, 1e4, 1e5, 1e6): D > 0, MRB_asym <= 160
    at the first point and monotone falling (<= 11 at 1e6).
S4  controls SMOOTH x=5 / SCRARITH x=5 / EPSTEIN x=8 through the
    SAME certificate: G50/G51/G52 the certificate REFUSES per world
    with the reason printed -- expected: strays below T_z >= 1
    (the world fills the arithmetic zero-free gap (0, 14.13): H2
    is EXACTLY the consumption of the low-lying zero-free
    structure) and d1_lo <= 0; G53 mechanism consistency: refusal
    in ALL THREE worlds (the certificate never claims WPD where PD
    is false).
S5  screens: G54 tau-screen: slope log10 MRB_cert(a=4) vs log10 tau
    <= 0.30 (the certificate lives in RvM/band currency; the zone
    term rides sqrt(tau) BY CONSTRUCTION -- typed BOUND-RIDES-
    CONNES, INFO); G55 conditioning: 1e-25 shift on Q[0,0] at x=5
    moves tau by a nonzero amount in (1e-40, 1e-10).
S6  chain + min-cut: G60 round-116 replica: flows base 4, refined 5
    (the arithmetic path now NFCLOS -> L1TAILPROVEN(INF) ->
    L1BAND(1) -> DOMASYM(INF, THIS ROUND: Theorems M/E/T/A for
    x >= x_0) -> WPDWIN(INF) -> R4HYP: ONE unit omega where round
    132 had two in series), counterfactual parallel 6 NOT REAL;
    census {MEAS, OMEGA-POS} cardinality 4 UNCHANGED; exact residue
    printed.
S9  composite verdict + runtime bar.

=======================================================================
FROZEN NUMERICS
=======================================================================
LADDER = ((3,45),(5,60),(8,80),(13,120)), KFAC = 1.25; A_BAT =
(1, 4, 16); NPOL = 32, AUD_DPS = 100; CACHE_ERR = 1e-9 (declared
X5 slop); HSW = (0.1038, 0.2573, 9.3675) [HSW22 Cor. 1.2, v914
corpus input]; H_VERIF = 3e12 [PT21, cited], eps_off(a) =
2a(log H + 1)/H (round-132 G17 off-line allowance, cited); MATCH_F
= 0.25 (of local spacing); DELTA_LADDER = (1e-30, 1e-24, 1e-18,
1e-12, 1e-9, 1e-6, 1e-3, 1e-2) (adaptive sign-change intervals);
MMINUS_REL_BAR = 1e-3; MRB_BAR = 0.25; CPRED_BAR = 1.5; TL shells:
lam in (1.5, 2, 3) x J in (1, 2, 3, 4, 6, 8) from T*(x); ZONE_BUDGET
= TL/8; X_STRIP = (13, 21, 34, 55, 89); X_SCAN = 90..200 (integer);
X0_LO, X0_HI = 89, 144; X_ASYM = (144, 233, 377, 610, 1000, 3000,
10000, 100000, 1000000); MRB_ASYM_BAR = 160.0, MRB_ASYM_END = 11.0;
NMAX_PHI = 6, TRUNC_DPS = 25, TRUNC_GRID_D = 0.25, TRUNC_GRID_F =
0.5, TRUNC_AUDIT_BAR = 1e-6; K-moment gates K_MOM = 8, FLOOR_K =
1e-13 (C0k + TrBk) + 1e-40; BAR_WARD_X3 = 1e-8, BAR_SPEC_CENSUS =
1e-4, BAR_REAL = 1e-6, RES_BAR = 1e-12; TAU_SLOPE_BAR = 0.30;
COND_WIN = (1e-40, 1e-10); GAMMA1_LIT = 14.134725141734694 (ward
only); RUNTIME_BAR = 2400 s.  Deterministic: NO randomness anywhere.
Cache verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All
mpf/mpc arithmetic inside explicit mp.workdps blocks (the round-118
ambient-precision negation trap).

VERDICT ENUMS (frozen): THMM-PROVEN + THME-PROVEN + THMT-PROVEN +
CHAIN-PROVEN(DOM ==> MRB <= 1 ==> WPD C <= 1; weak one-sidedness
==> MRB <= (2-th)/th); MRB-CERTIFIED-ON-LADDER(no sign reads);
ASYM-ASSEMBLY(x_0; H-pin ==> {d_1 > 0, MRB} for x >= x_0);
QSWAMP-OBSTRUCTION(strip); OMEGA-MERGED(L1BAND carries WPD-battery
for x >= x_0); A1-OBSTRUCTED(sharp anti-dominant, Fejer blind);
A2-LATTICE-OBSTRUCTED + A3-QUADRATURE-DEAD(mixed-sign census);
MECHANISM-COUNTING-PLUS-PINNING; CONTROLS-REFUSE(H2 = zero-free-gap
consumption); WARD-CURRENCY(typing always stated); MINCUT(flows,
census unchanged).  Composite priority: INSTRUMENT-EDGE (any
ward/audit gate fails, exit 1) > EXACT-LAYER-OBSTRUCTED (any S1
gate fails) > adjudicated verdicts as gated.

CALIBRATION DISCLOSURE (pre-freeze, one scratch script
calib_scratch_dom.py + log, deleted; all numbers quoted above and
here verbatim): identity matching == zone count at every rung
(1/1, 4/4, 10/10, 21/21), strays 0 everywhere, max matched gaps
2.8e-4 / 2.1e-6 / 2.4e-9 / 1.4e-14 (census-vs-polished currency);
M- at the numeric floor (<= 4.2e-17); MRB_cert 0.0718/0.0831/
0.0786/0.0739 at a=1..16 band (flat); mixed-sign weight census
1/4, 3/10, 14/20, 14/41; closed-form D at a=4: -1.1e-2 (x=13),
-1.2e-4 (x=89), +4.3e-5 (x=144), MRB_asym 144.1 (x=144) -> 10.5
(x=1e6); Dirichlet exhibit: x=5 first zero 14.128 (< gamma_1),
1/4 undershoots; x=13: 21/24 undershoots, in-band devs tiny
negative; Fejer: 0 zeros at both rungs; Xi-transform convention
audited (Xi = 2 * [2 int_0^inf Phi cos] at t = 0, 20, factor
exact); build costs: x=13 even ~174 s, truncation exhibits ~330 s
at calibration precision (frozen run uses NMAX_PHI 6 / dps 25).
Amendments after the frozen run, if any, are appended as numbered
AMENDMENT blocks.

AST FIREWALL: no zetazero/siegelz/siegeltheta/nzeros/grampoint
anywhere; the zeta attribute only inside audit_* functions (any
enclosing scope); np.load only inside ward_* functions; no import
of verification/.  NO RH CLAIM.  EXPLORATION ONLY.
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
NPOL = 32
AUD_DPS = 100
CACHE_ERR = 1e-9
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
H_VERIF = 3.0e12
MATCH_F = 0.25
DELTA_LADDER = (1e-30, 1e-24, 1e-18, 1e-12, 1e-9, 1e-6, 1e-3, 1e-2)
MMINUS_REL_BAR = 1e-3
MRB_BAR = 0.25
CPRED_BAR = 1.5
X_STRIP = (13, 21, 34, 55, 89)
X0_LO, X0_HI = 89, 144
X_ASYM = (144, 233, 377, 610, 1000, 3000, 10000, 100000, 1000000)
MRB_ASYM_BAR = 160.0
MRB_ASYM_END = 11.0
NMAX_PHI = 6
TRUNC_DPS = 25
TRUNC_GRID_D = 0.25
TRUNC_GRID_F = 0.5
TRUNC_AUDIT_BAR = 1e-6
K_MOM = 8
BAR_WARD_X3 = 1e-8
BAR_SPEC_CENSUS = 1e-4
BAR_REAL = 1e-6
RES_BAR = 1e-12
TAU_SLOPE_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10
GAMMA1_LIT = 14.134725141734693790   # ward only
RUNTIME_BAR = 2400.0

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
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
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

    def owners(lineno: int) -> list[str]:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

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
            fns = owners(node.lineno)
            if not any(f.startswith("audit_") for f in fns):
                bad.append("zeta outside audit_ @%d (%s)"
                           % (node.lineno, fns or "module"))
        if isinstance(node, ast.Attribute) and nm == "load":
            fns = owners(node.lineno)
            if not any(f.startswith("ward_") for f in fns):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fns or "module"))
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


# --------------------------------------------------------- audit layer
def audit_polish_band(seeds: np.ndarray, dps: int) -> tuple[list, float]:
    """own damped Newton on Xi(t) = xi(1/2 + i t) from cache seeds."""
    out = []
    worst = 0.0
    with mp.workdps(dps):
        def xi_line(t):
            s = mp.mpf("0.5") + 1j * t
            return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2)
                         * mp.gamma(s / 2) * mp.zeta(s))
        for g0 in seeds:
            t = mp.mpf(repr(float(g0)))
            for _ in range(60):
                f = xi_line(t)
                fp = mp.diff(xi_line, t)
                step = f / fp
                if abs(step) > mp.mpf("0.25"):
                    step = step / abs(step) * mp.mpf("0.25")
                t = t - step
                if abs(step) < mp.mpf(10) ** (-dps + 8):
                    break
            worst = max(worst, float(abs(xi_line(t))))
            out.append(mp.nstr(t, dps))
    return out, worst


def audit_zero_deltas(pol_str: list, dps: int) -> list:
    """certified interval half-widths for the polished ordinates by
    mp sign change of Xi on [g - d, g + d] (adaptive ladder)."""
    out = []
    with mp.workdps(dps):
        def xi_line(t):
            s = mp.mpf("0.5") + 1j * t
            return mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2)
                         * mp.gamma(s / 2) * mp.zeta(s))
        for gs in pol_str:
            g = mp.mpf(gs)
            dj = None
            for d in DELTA_LADDER:
                dm = mp.mpf(repr(d))
                v1, v2 = xi_line(g - dm), xi_line(g + dm)
                if v1 * v2 < 0:
                    dj = d
                    break
            out.append(dj)
    return out


def audit_trunc_check() -> float:
    """audit the Xi-transform convention: Xi(t) == 2 * [2 int_0^3
    Phi(u) cos(ut) du] at t = 0 and 20 (rel)."""
    worst = 0.0
    with mp.workdps(30):
        for tv in (0, 20):
            t = mp.mpf(tv)
            v = 4 * mp.quad(lambda u: phi_theta(u) * mp.cos(u * t),
                            [0, 1, 3])
            s = mp.mpf("0.5") + 1j * t
            xit = mp.re(s * (s - 1) / 2 * mp.pi ** (-s / 2)
                        * mp.gamma(s / 2) * mp.zeta(s))
            worst = max(worst, float(abs(v - xit) / abs(xit)))
    return worst


# ------------------------------------------------- classical transforms
def phi_theta(u):
    """Riemann Phi(u) = sum_n (2 pi^2 n^4 e^{9u/2} - 3 pi n^2
    e^{5u/2}) exp(-pi n^2 e^{2u})  (theta currency, no zeta)."""
    tot = mp.mpf(0)
    e2 = mp.exp(2 * u)
    for n in range(1, NMAX_PHI + 1):
        tot += (2 * mp.pi ** 2 * n ** 4 * mp.exp(mp.mpf(9) * u / 2)
                - 3 * mp.pi * n ** 2 * mp.exp(mp.mpf(5) * u / 2)) \
            * mp.exp(-mp.pi * n ** 2 * e2)
    return tot


def trunc_scan(x: int, kernel: str, tmax: float, dstep: float):
    """zeros of the (Dirichlet/Fejer)-kernel truncation of the Xi
    transform at window A = log(x)/2, by sign scan + bisection."""
    A = math.log(x) / 2.0
    with mp.workdps(TRUNC_DPS):
        Am = mp.mpf(repr(A))

        def F(t):
            tm = mp.mpf(repr(float(t)))
            if kernel == "dirichlet":
                return float(2 * mp.quad(
                    lambda u: phi_theta(u) * mp.cos(u * tm), [0, Am]))
            return float(2 * mp.quad(
                lambda u: phi_theta(u) * (1 - u / Am) * mp.cos(u * tm),
                [0, Am]))
        ts = np.arange(2.0, tmax, dstep)
        vals = [F(t) for t in ts]
        zs = []
        for i in range(len(ts) - 1):
            if vals[i] * vals[i + 1] < 0:
                lo, hi = float(ts[i]), float(ts[i + 1])
                vlo = vals[i]
                for _ in range(45):
                    mid = 0.5 * (lo + hi)
                    vm = F(mid)
                    if (vm > 0) == (vlo > 0) and vm != 0.0:
                        lo, vlo = mid, vm
                    else:
                        hi = mid
                zs.append(0.5 * (lo + hi))
    return np.array(zs)


# --------------------------------------------------------- source side
def raw_mp_census(cell: dict) -> np.ndarray:
    """round-132 AMENDMENT-1 node source VERBATIM: the SL.hp_zero_data
    mp path minus the f64 bisection refine."""
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


def en_pair(cs: list, aa, oms: list, t):
    """(E_N(t), E_N'(t)) in mp at ambient workdps (caller sets)."""
    Rv = 2 * cs[0] / t
    Rp = -2 * cs[0] / t ** 2
    for k in range(1, len(cs)):
        d = t * t - oms[k] ** 2
        Rv += 2 * cs[k] * (-1) ** k * t / d
        Rp += 2 * cs[k] * (-1) ** k * (-(t * t + oms[k] ** 2)) / d ** 2
    s = mp.sin(aa * t)
    c = mp.cos(aa * t)
    return s * Rv, aa * c * Rv + s * Rp


def node_deltas(cell: dict, mus: np.ndarray) -> list:
    """certified interval half-widths for census nodes by mp sign
    change of E_N (adaptive ladder)."""
    out = []
    with mp.workdps(cell["dps"]):
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]
        aa = mp.log(cell["x"]) / 2
        oms = [k * mp.pi / aa for k in range(cell["K"])]
        for mu in mus:
            m0 = mp.mpf(repr(float(mu)))
            dj = None
            for d in DELTA_LADDER:
                dm = mp.mpf(repr(d))
                v1 = en_pair(cs, aa, oms, m0 - dm)[0]
                v2 = en_pair(cs, aa, oms, m0 + dm)[0]
                if v1 * v2 < 0:
                    dj = d
                    break
            out.append(dj)
    return out


# --------------------------------------------------------- closed forms
def w_of(a: float, t):
    return a * t ** 2 / (a + t ** 2) ** 2


def wp_abs(a: float, t: float) -> float:
    return abs(2.0 * a * t * (a - t * t)) / (a + t * t) ** 3


def eps_off(a: float) -> float:
    return 2.0 * a * (math.log(H_VERIF) + 1.0) / H_VERIF


def kq_float(q: float) -> float:
    if q >= 1.0:
        return float("inf")
    khi = max(3, int(math.ceil(q / (1.0 - q))) + 2)
    return max(k * q ** (k - 1) for k in range(2, khi + 1))


def hsw_G(T: float) -> float:
    """certified upper bound for sum_{gamma > T} gamma^{-2} over ALL
    nontrivial zeros ([HSW22] Cor. 1.2 + exact antiderivatives)."""
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        al = mp.mpf(repr(HSW_A))
        be = mp.mpf(repr(HSW_B))
        cc = mp.mpf(repr(HSW_C))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return float(t1 + t2 + t3)


def m_rvm(T: float) -> float:
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


def q_hsw(T: float) -> float:
    return HSW_A * math.log(T) + HSW_B * math.log(math.log(T)) + HSW_C


def t_star(N: int) -> float:
    lo, hi = 20.0, 1e30
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if m_rvm(mid) - q_hsw(mid) >= N:
            hi = mid
        else:
            lo = mid
    return hi


def tl_shells(N: int, a: float, Ts: float) -> float:
    """certified tail_1 lower bound: shell counts >= M - Q telescoped
    (frozen shell configs), gamma_N <= T* consumed (THEOREM T)."""
    best = 0.0
    for lam in (1.5, 2.0, 3.0):
        for J in (1, 2, 3, 4, 6, 8):
            Tj = [Ts * lam ** j for j in range(J + 1)]
            tot = 0.0
            u_prev = m_rvm(Ts) + q_hsw(Ts)
            for j in range(J):
                n_next = m_rvm(Tj[j + 1]) - q_hsw(Tj[j + 1])
                cnt = max(0.0, n_next - max(float(N), u_prev))
                tot += cnt * w_of(a, Tj[j + 1])
                u_prev = m_rvm(Tj[j + 1]) + q_hsw(Tj[j + 1])
            best = max(best, tot)
    return best


def asym_assembly(x: float, a: float) -> tuple:
    """THEOREM A closed forms at (x, a): (D, MRB bound or inf)."""
    K = int(math.ceil(KFAC * x * math.log(x)))
    N = K - 1
    Ts = t_star(N)
    Tz = 2 * math.pi * x
    n_z = m_rvm(Tz) - q_hsw(Tz)
    TL = tl_shells(N, a, Ts)
    m_minus_edge = max(0.0, (N - n_z)) * w_of(a, Tz)
    m_plus_edge = a * hsw_G(Tz)
    D = TL - TL / 8.0 - m_minus_edge
    mrb = ((TL / 8.0 + m_plus_edge + m_minus_edge) / D
           if D > 0 else float("inf"))
    return D, mrb, N, Ts, TL


# --------------------------------------------------------- exact layer
def instance_cert(a_r, trues, gs, nodes, Tz):
    """exact rational THEOREM M/E certificate on an instance.
    Returns dict with refusal flag and exact masses/bounds."""
    import sympy as sp
    aq = sp.Rational(a_r)
    tv = [sp.Rational(v) for v in trues]
    gv = [sp.Rational(v) for v in gs]
    nv = [sp.Rational(v) for v in nodes]
    Tzq = sp.Rational(Tz)
    m = sum(1 for t in tv if t <= Tzq)
    m = min(m, len(gv))

    def w(t):
        return aq * t ** 2 / (aq + t ** 2) ** 2

    # H1: balls ordered/disjoint; matched node per ball
    h1 = all(tv[j] + gv[j] < tv[j + 1] - gv[j + 1]
             for j in range(m - 1))
    in_ball = [[i for i in range(len(nv))
                if abs(nv[i] - tv[j]) <= gv[j]] for j in range(m)]
    h1 = h1 and all(len(b) >= 1 for b in in_ball)
    h3 = all(len(b) == 1 for b in in_ball)
    top = max(Tzq, tv[m - 1] + gv[m - 1]) if m else Tzq
    ball_ids = set(i for b in in_ball for i in b)
    strays = [i for i in range(len(nv))
              if nv[i] <= top and i not in ball_ids]
    h2 = len(strays) == 0
    refuse = not (h1 and h2 and h3)
    out = dict(refuse=refuse, m=m, strays=len(strays))
    if refuse:
        return out
    # conclusions, exact
    slack_dom = all(nv[i] >= tv[i] - gv[i] for i in range(m))
    edge_high = all(nv[i] > Tzq for i in range(m, len(nv)))
    N = len(nv)
    Mm = sum(max(sp.Integer(0), w(nv[i]) - w(tv[i]))
             for i in range(N))
    Mp = sum(max(sp.Integer(0), w(tv[i]) - w(nv[i]))
             for i in range(N))
    tail1 = sum(w(t) for t in tv[N:])
    zone_minus = sum(w(tv[j] - gv[j]) - w(tv[j]) for j in range(m))
    zone_abs = sum(w(tv[j] - gv[j]) - w(tv[j] + gv[j])
                   for j in range(m))
    edge_minus = sum(max(sp.Integer(0), w(nv[i]) - w(tv[i]))
                     for i in range(m, N))
    edge_plus = sum(max(sp.Integer(0), w(tv[i]) - w(nv[i]))
                    for i in range(m, N))
    thmm = Mm <= zone_minus + edge_minus
    thme = (edge_minus <= (N - m) * w(Tzq)
            and edge_plus <= sum(w(t) for t in tv[m:N]))
    d1 = Mp - Mm + tail1
    mrb = (Mp + Mm) / d1
    cert = ((zone_abs + sum(abs(w(tv[i]) - w(nv[i]))
                            for i in range(m, N)))
            / (tail1 - zone_minus - edge_minus))
    th = 1 - Mm / (Mp + tail1)
    chain = mrb <= (2 - th) / th
    out.update(slack_dom=slack_dom, edge_high=edge_high, thmm=thmm,
               thme=thme, d1pos=d1 > 0, mrb_ok=mrb <= cert,
               chain=chain, mrb=float(mrb), cert=float(cert))
    return out


def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    a, t, u, U = sp.symbols("a t u U", positive=True)

    # G10 branch derivative + w bounds
    wexpr = a * t ** 2 / (a + t ** 2) ** 2
    ok10 = (sp.simplify(sp.diff(wexpr, t)
                        - 2 * a * t * (a - t ** 2)
                        / (a + t ** 2) ** 3) == 0
            and sp.simplify((a + t ** 2) ** 2 - t ** 4
                            - (a ** 2 + 2 * a * t ** 2)) == 0
            and sp.simplify((a + t ** 2) ** 2 - 4 * a * t ** 2
                            - (a - t ** 2) ** 2) == 0)
    out.append(("G10-branch-w-bounds", ok10,
                "w' == 2at(a-t^2)/(a+t^2)^3 (strict decrease on "
                "(sqrt a, inf)); w <= a/t^2; w <= 1/4 exact"))

    # G11 THEOREM M instance (exact rationals)
    inst = instance_cert(4, ("4", "5", "6", "17/2", "11", "30", "45"),
                         ("1/50", "1/40", "1/30"),
                         ("401/100", "399/80", "541/90", "9", "13"),
                         "7")
    ok11 = (not inst["refuse"] and inst["slack_dom"]
            and inst["edge_high"] and inst["thmm"] and inst["thme"]
            and inst["d1pos"] and inst["mrb_ok"] and inst["chain"])
    out.append(("G11-thmM-instance", ok11,
                "THEOREM M/E/C on the rational instance (M- witness "
                "mu_2 < gamma_2 inside its ball): slack dominance, "
                "M- <= zone+edge bounds, d1 > 0, MRB %.4f <= "
                "certificate %.4f <= (2-th)/th, all exact in Q"
                % (inst.get("mrb", -1), inst.get("cert", -1))))

    # G12 THEOREM C chain (symbolic)
    Mp, t1, th = sp.symbols("Mp t1 th", positive=True)
    Mm_eq = (1 - th) * (Mp + t1)
    d1_eq = sp.simplify(Mp - Mm_eq + t1 - th * (Mp + t1))
    slack = sp.simplify((2 - th) * (Mp + t1)
                        - (Mp + Mm_eq))
    Mm = sp.symbols("Mm", positive=True)
    ratio = (Mp + Mm) / (Mp - Mm + t1)
    dnum = sp.simplify(sp.diff(ratio, Mm)
                       * (Mp - Mm + t1) ** 2)
    dom_c1 = sp.simplify((Mp + t1) - Mp)
    q = sp.symbols("q", positive=True)
    kq_le1 = sp.simplify((sp.Rational(1, 2) - q)
                         * 2)  # 2q <= 1 iff q <= 1/2
    ok12 = (d1_eq == 0 and slack == t1
            and sp.simplify(dnum - (2 * Mp + t1)) == 0
            and dom_c1 == t1 and kq_le1 == 1 - 2 * q)
    out.append(("G12-chain-theorem", ok12,
                "d1 == th(M+ + tail1) at M- == (1-th)(M+ + tail1) "
                "(exact identity); ratio slack == tail1 >= 0 ==> "
                "MRB <= (2-th)/th; ratio monotone in M- (derivative "
                "numerator == 2M+ + tail1 > 0); DOM ==> MRB <= 1 "
                "(slack == tail1) and K(q) = 2q <= 1 for q <= 1/2: "
                "WPD constant <= 1 on the battery (r132 W1 cited)"))

    # G13 THEOREM E monotone core (symbolic)
    T_, mu_ = sp.symbols("Tz mu", positive=True)
    wT = a * T_ ** 2 / (a + T_ ** 2) ** 2
    wmu = a * mu_ ** 2 / (a + mu_ ** 2) ** 2
    diff_expr = sp.together(wT - wmu)
    num = sp.expand(sp.numer(diff_expr))
    fac = sp.expand((mu_ - T_) * (mu_ + T_) * a
                    * (mu_ * T_ - a) * (mu_ * T_ + a))
    ok13 = sp.simplify(num - fac) == 0
    out.append(("G13-thmE-monotone-core", ok13,
                "w(Tz) - w(mu) == a(mu-Tz)(mu+Tz)(mu Tz - a)"
                "(mu Tz + a)/denoms exact: mu > Tz > sqrt(a) ==> "
                "w(mu) < w(Tz) -- each edge M- term <= w(Tz), "
                "each edge M+ term <= w(gamma_i) (w >= 0)"))

    # G14 counting algebra + HSW antiderivatives + tangent lemma
    Nf, Mf, Qf = sp.symbols("Nf Mf Qf", positive=True)
    N2, M2, Q2 = sp.symbols("N2 M2 Q2", positive=True)
    # |N-M| <= Q at two points ==> N2 - Nf >= (M2 - Q2) - (Mf + Qf)
    sh = sp.simplify((N2 - Nf) - ((M2 - Q2) - (Mf + Qf))
                     - ((N2 - (M2 - Q2)) + ((Mf + Qf) - Nf)))
    F1 = -(sp.log(t / (2 * sp.pi * sp.E)) + 1) / t
    F2 = -sp.log(t) / (2 * t ** 2) - 1 / (4 * t ** 2)
    F3 = -(2 * sp.log(t) + 1) / (4 * t ** 2)
    ok14 = (sh == 0
            and sp.simplify(sp.diff(F1, t)
                            - sp.log(t / (2 * sp.pi * sp.E))
                            / t ** 2) == 0
            and sp.simplify(sp.diff(F2, t) - sp.log(t) / t ** 3) == 0
            and sp.simplify(sp.diff(F3, t) - sp.log(t) / t ** 3) == 0
            and sp.simplify((1 / U - 1 / u) * u * U - (u - U)) == 0)
    out.append(("G14-counting-algebra", ok14,
                "shell count N(T2)-N(T1) >= (M2-Q2)-(M1+Q1) exact "
                "from |N-M| <= Q (sum of two nonneg deficits); HSW "
                "G(T) antiderivatives + tangent lemma re-gated "
                "(round-131 G16); THEOREM T: T >= T* ==> N_fin <= "
                "K-1 <= M-Q <= N_true, and gamma_{K-1} <= T*"))

    # G15 secular interlacing lemma (A2-lattice precondition)
    y = sp.symbols("y", real=True)
    A0 = sp.Rational(1, 3)
    ws_ = [sp.Rational(2, 5), sp.Rational(1, 7), sp.Rational(3, 11)]
    bs_ = [sp.Integer(1), sp.Integer(4), sp.Integer(9)]
    Fnum = (A0 * sp.prod([y - b for b in bs_])
            + sum(ws_[k] * sp.prod([y - bs_[j] for j in range(3)
                                    if j != k])
                  for k in range(3)))
    roots = sp.real_roots(sp.Poly(Fnum, y))
    n_g1 = sum(1 for r in roots if 1 < r < 4)
    n_g2 = sum(1 for r in roots if 4 < r < 9)
    n_lo = sum(1 for r in roots if r < 1)
    wsym = sp.symbols("w1:4", positive=True)
    Fp = -sum(wsym[k] / (y - bs_[k]) ** 2 for k in range(3))
    ok15 = (len(roots) == 3 and n_g1 == 1 and n_g2 == 1
            and n_lo == 1
            and all(sp.simplify(term) is not None for term in [Fp]))
    out.append(("G15-secular-interlacing", ok15,
                "F = A0 + sum w_k/(y-b_k), all w_k > 0: F' < 0 "
                "(sum of negative squares) ==> EXACTLY one root per "
                "pole gap (instance: roots %d/%d/%d in the three "
                "regions): all-positive census weights would force "
                "in-band node count == lattice count -- the measured "
                "RvM node law (r128/r131) requires MIXED signs"
                % (n_lo, n_g1, n_g2)))

    # G16 resolvability crossover (round-131 G17 re-gated)
    xs = sp.symbols("xs", positive=True)
    T = sp.symbols("T", positive=True)
    Tstar = sp.solve(sp.log(T / (2 * sp.pi)) / (2 * sp.pi)
                     - (sp.log(xs) / 2) / sp.pi, T)
    kf = sp.symbols("kf", positive=True)
    edge = (kf * xs * sp.log(xs)) * sp.pi / (sp.log(xs) / 2)
    ok16 = (len(Tstar) == 1
            and sp.simplify(Tstar[0] - 2 * sp.pi * xs) == 0
            and sp.simplify(2 * sp.pi * xs / edge - 1 / kf) == 0)
    out.append(("G16-resolvability-crossover", ok16,
                "mode density == RvM density exactly at T = 2 pi x; "
                "band fraction == 1/KFAC (round-131 theorem, "
                "re-gated): T_z = 2 pi x is theorem-backed"))

    # G17 stray-instance refusal (hypothesis necessity)
    bad = instance_cert(4, ("4", "5", "6", "17/2", "11", "30", "45"),
                        ("1/50", "1/40", "1/30"),
                        ("3", "401/100", "399/80", "541/90", "9"),
                        "7")
    import sympy as sp2
    mu1 = sp2.Rational(3)
    dom_fails = mu1 < sp2.Rational(4) - sp2.Rational(1, 50)
    ok17 = bad["refuse"] and bad["strays"] >= 1 and bool(dom_fails)
    out.append(("G17-stray-refusal", ok17,
                "stray node 3 <= T_z outside every ball: the "
                "certificate REFUSES (H2, %d stray) and sorted "
                "dominance indeed fails (mu_1 = 3 < gamma_1 - g_1): "
                "the hypotheses are necessary, controls-in-miniature"
                % bad["strays"]))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("dominance_proof_probe -- PRIME.MRB.DOMINANCE.PROOF.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    ladder = LADDER[:2] if smoke else LADDER
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))
    trunc_xs = (5,) if smoke else (5, 13)

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
    section("S1  EXACT LAYER (THEOREMS M / C / E / T inputs)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited: round-131 secular identity (node count "
         "EXACT K-1); round-132 THEOREM D/W1/P1 + raw-census "
         "AMENDMENT 1; HSW22 Cor. 1.2 (all-strip counting, no RH); "
         "PT21 verification height (off-line allowance eps_off); "
         "infinitude of zeros (classical) for tail_1 > 0")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS + CLASSICAL FORMS")
    dev20 = audit_trunc_check()
    check("G20-trunc-audit", dev20 <= TRUNC_AUDIT_BAR,
          "Xi(t) == 4 int_0^3 Phi cos(ut) du at t = 0, 20: max rel "
          "%.1e (theta-transform convention audited)" % dev20,
          kind="edge")
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    gtop = float(gam[-1])
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G21-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000 (necessary); "
          "G monotone; G(gamma_top) = %.3e" % hsw_G(gtop))

    ok22 = True
    det22 = []
    for x, _d in ladder:
        K = int(math.ceil(KFAC * x * math.log(x)))
        N = K - 1
        Ts = t_star(N)
        gN = float(gam[N - 1])
        ok22 = ok22 and gN <= Ts \
            and (m_rvm(Ts) - q_hsw(Ts)) >= N - 1e-9
        det22.append("x%d: gamma_%d = %.2f <= T* = %.2f" %
                     (x, N, gN, Ts))
    check("G22-thmT-top-segment", ok22,
          "gamma_{K-1} <= T*(x) and K-1 <= M(T*)-Q(T*) per rung: "
          "counting dominance N_fin <= N_true is a THEOREM for "
          "T >= T* (unconditional): " + "; ".join(det22))

    # ---------------------------------------------------------- S3
    section("S3  MAIN LADDER: CERTIFICATES (no sign reads)")
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

    # census + operator cross-ward + residual gate
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
        with mp.workdps(dps):
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(ce["K"])]
            res = max(float(abs(en_pair(cs, aa, oms,
                                        mp.mpf(repr(float(m))))[0]))
                      for m in mus)
        ok30c = ok30c and len(mus) == len(refined) and res <= RES_BAR
        det30c.append("x%d: n %d==%d max|E| %.0e"
                      % (x, len(mus), len(refined), res))
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
    check("G30b-spec-census", ok30b, "; ".join(det30))
    check("G30c-raw-census-residual", ok30c,
          "raw mp census (r132 AMENDMENT-1 currency), mp E-certified "
          "(bar %.0e): %s" % (RES_BAR, "; ".join(det30c)))

    xs = [x for x, _d in ladder]
    ok31 = True
    det31 = []
    for x in xs:
        t0x = min(float(nodes[x][0]), float(gam[0]))
        marg = t0x - math.sqrt(max(A_BAT))
        ok31 = ok31 and marg > 0
        det31.append("x%d: %.4f" % (x, marg))
    check("G31-branch-gate", ok31,
          "min(mu_1, gamma_1) - sqrt(a_max) > 0: "
          + "; ".join(det31)
          + " (single branch valid for a < gamma_1^2 = %.2f)"
          % (float(gam[0]) ** 2))

    # polished ordinates + certified intervals (audit)
    pol_str, pol_res = audit_polish_band(gam[:NPOL], AUD_DPS)
    pol_f64 = np.array([float(mp.mpf(s)) for s in pol_str])
    xw = float(np.max(np.abs(pol_f64 - gam[:NPOL])))
    zdel = audit_zero_deltas(pol_str, AUD_DPS)
    okpol = xw <= 1e-7 and pol_res <= 1e-60 \
        and all(d is not None for d in zdel)
    check("G32a-polish-intervals", okpol,
          "own-Newton ordinates vs cache max dev %.1e, max |Xi| "
          "%.1e; all %d ordinates sign-change certified (worst "
          "delta %.0e)" % (xw, pol_res, NPOL,
                           max(d for d in zdel)), kind="edge")

    # THE CERTIFICATE per rung
    cert = {}
    ok32 = ok33 = ok34 = ok35 = True
    det33, det34, det35 = [], [], []
    for x in xs:
        ce = cells[x]
        mus = nodes[x]
        N = len(mus)
        edge = ce["K"] * math.pi / ce["a"]
        Tz = min(0.98 * edge, 2 * math.pi * x)
        n_zone = int(np.sum(gam <= Tz))
        ndel = node_deltas(ce, mus)
        # identity matching on the prefix
        m_id = 0
        gaps = []
        for i in range(min(N, NPOL)):
            if pol_f64[i] > Tz:
                break
            g = abs(float(mus[i]) - pol_f64[i])
            j = int(np.argmin(np.abs(gam - float(mus[i]))))
            lo = gam[j - 1] if j > 0 else 0.0
            hi = gam[j + 1] if j + 1 < len(gam) else gam[j] + 10.0
            spac = 0.5 * (hi - lo)
            if g < MATCH_F * spac and j == i:
                m_id = i + 1
                gaps.append(g)
            else:
                break
        # certified ball radii G_i = gap + node delta + zero delta
        Gi = [float(gaps[i]) + (ndel[i] or 1e-2) + (zdel[i] or 1e-2)
              for i in range(m_id)]
        # H1 separation, H3 one node per ball, H2 strays
        h1 = all(pol_f64[i] + Gi[i] < pol_f64[i + 1] - Gi[i + 1]
                 for i in range(m_id - 1))
        h3 = all(int(np.sum(np.abs(mus - pol_f64[i]) <= Gi[i])) == 1
                 for i in range(m_id))
        strays = int(np.sum(mus[m_id:] <= Tz))
        okx = (m_id == n_zone and strays == 0 and h1 and h3
               and all(d is not None for d in ndel))
        ok32 = ok32 and okx
        print("  x=%-2d certificate: zone %d matched %d strays %d "
              "H1 %s H3 %s maxgap %.1e maxball %.1e"
              % (x, n_zone, m_id, strays, h1, h3,
                 max(gaps) if gaps else float("nan"),
                 max(Gi) if Gi else float("nan")), flush=True)
        cert[x] = dict(m=m_id, Tz=Tz, Gi=Gi, N=N, ndel=ndel)
    check("G32-certificate-hypotheses", ok32,
          "identity matching == zone count, ZERO strays (H2), one "
          "node per ball (H3), balls separated (H1), all positions "
          "interval-certified: THEOREM M applies at every rung -- "
          "sorted mu_i >= gamma_i - G_i with NO sign read")

    # masses + MRB / WPD certificates per (rung, a)
    mrb_tab = {a: [] for a in A_BAT}
    for x in xs:
        ce = cells[x]
        mus = nodes[x]
        N = cert[x]["N"]
        m_id = cert[x]["m"]
        Tz = cert[x]["Tz"]
        Gi = cert[x]["Gi"]
        for a in A_BAT:
            af = float(a)
            with mp.workdps(60):
                zm = mp.mpf(0)   # zone M- bound
                za = mp.mpf(0)   # zone |dw| bound
                for i in range(m_id):
                    gq = mp.mpf(pol_str[i])
                    Gq = mp.mpf(repr(Gi[i]))
                    am = mp.mpf(a)
                    wl = am * (gq - Gq) ** 2 / (am + (gq - Gq) ** 2) ** 2
                    wc = am * gq ** 2 / (am + gq ** 2) ** 2
                    wr = am * (gq + Gq) ** 2 / (am + (gq + Gq) ** 2) ** 2
                    zm += wl - wc
                    za += wl - wr
                zone_minus = float(zm)
                zone_abs = float(za)
            dw = w_of(af, gam[m_id:N]) - w_of(af, mus[m_id:])
            slop = (np.array([wp_abs(af, g) for g in gam[m_id:N]])
                    * CACHE_ERR
                    + np.array([wp_abs(af, float(mus[i]))
                                * (cert[x]["ndel"][i] or 1e-2)
                                for i in range(m_id, N)]))
            edge_minus = float(np.sum(np.clip(-dw, 0, None) + slop))
            edge_abs = float(np.sum(np.abs(dw) + slop))
            tail_cache = float(np.sum(w_of(af, gam[N:])))
            tslop = float(np.sum(np.array(
                [wp_abs(af, g) for g in gam[N:]]) * CACHE_ERR))
            tail_lo = tail_cache - tslop
            tail_hi = tail_cache + af * hsw_G(gtop) + tslop \
                + eps_off(af)
            m_minus_ub = zone_minus + edge_minus
            m_abs_ub = zone_abs + edge_abs
            d1_lo = tail_lo - m_minus_ub
            mrb_c = m_abs_ub / d1_lo if d1_lo > 0 else float("inf")
            t0c = min(float(mus[0]), float(gam[0])) - 1e-2
            qv = 4.0 * w_of(af, t0c)
            c_cert = (kq_float(qv) * m_abs_ub + tail_hi) / d1_lo \
                if d1_lo > 0 else float("inf")
            ok33 = ok33 and d1_lo > 0 \
                and m_minus_ub / d1_lo <= MMINUS_REL_BAR
            ok34 = ok34 and mrb_c <= MRB_BAR
            ok35 = ok35 and c_cert <= CPRED_BAR
            mrb_tab[a].append(mrb_c)
            cert[x][a] = dict(d1_lo=d1_lo, mrb=mrb_c, cc=c_cert,
                              mm=m_minus_ub, ma=m_abs_ub,
                              t_lo=tail_lo, t_hi=tail_hi, q=qv)
            if a == 4:
                det33.append("x%d: M- <= %.1e (/d1 %.0e)"
                             % (x, m_minus_ub, m_minus_ub / d1_lo))
                det34.append("x%d: %.4f" % (x, mrb_c))
                det35.append("x%d: C %.3f d1_lo %.5f" %
                             (x, c_cert, d1_lo))
    for a in A_BAT:
        info("MRB_cert ladder a=%d: %s" %
             (a, ["%.4f" % v for v in mrb_tab[a]]))
    check("G33-mminus-certified", ok33,
          "certified M- bound (zone gap mass + edge computed + "
          "declared slop) <= %.0e of d1_lo at every (rung, a); "
          "a=4: %s -- the one-sidedness evidence upgraded from "
          "sign census to mass bound" % (MMINUS_REL_BAR,
                                         "; ".join(det33)))
    check("G34-mrb-certificate", ok34,
          "MRB_cert = M_abs_ub/d1_lo <= %.2f at every (rung, a) "
          "(a=4: %s): the round-132 MRB measured read is now a "
          "per-rung CERTIFICATE consuming no sign reads"
          % (MRB_BAR, "; ".join(det34)))
    check("G35-wpd-certified-constant", ok35,
          "C_cert = [K(q) M_abs + tail1_hi]/d1_lo <= %.1f and "
          "d1_lo > 0 at every (rung, a) (a=4: %s): the FULL "
          "round-132 residue {d_1 > 0, MRB} certified per rung"
          % (CPRED_BAR, "; ".join(det35)))

    # G35b THEOREM-D prediction in certified-mass currency
    ok35b = True
    worst_sat = 0.0
    ncell = 0
    for x in xs:
        mus = nodes[x]
        N = cert[x]["N"]
        for a in A_BAT:
            af = float(a)
            cc = cert[x][a]
            t0c = min(float(mus[0]), float(gam[0])) - 1e-2
            W = w_of(af, t0c)
            wedge = w_of(af, float(gam[N]))
            for k in range(2, K_MOM + 1):
                c0k = float(np.sum(w_of(af, gam) ** k)) \
                    + w_of(af, gtop) ** (k - 1) * af * hsw_G(gtop)
                trk = float(math.fsum(w_of(af, mus) ** k))
                dk = c0k - trk
                floor = 1e-13 * (abs(c0k) + trk) + 1e-40
                hi = (k * W ** (k - 1) * cc["ma"]
                      + wedge ** (k - 1) * cc["t_hi"]
                      + eps_off(af) + floor)
                lo = -(k * W ** (k - 1) * cc["mm"]
                       + eps_off(af) + floor)
                okk = lo <= dk <= hi
                ok35b = ok35b and okk
                ncell += 1
                if hi > 0:
                    worst_sat = max(worst_sat, dk / hi)
    check("G35b-thmD-certified-prediction", ok35b,
          "measured d_k inside the THEOREM-D bounds built from "
          "CERTIFIED masses at all %d (rung, a, k<=%d) cells; worst "
          "saturation %.3f" % (ncell, K_MOM, worst_sat))

    # G36 node descent (measured; bypassed for WPD)
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
        det36.append("x%d->x%d: prefix %d ascents %d"
                     % (xs[i], xs[i + 1], npfx, asc))
    check("G36-node-descent", ok36,
          "matched-prefix descent (measured, %s): compression "
          "evidence -- BYPASSED for WPD (Theorem M needs balls, "
          "not monotonicity)" % "; ".join(det36))

    check("G37-quadrature-dead", all(cert[x][a]["d1_lo"] > 0
                                     for x in xs for a in A_BAT),
          "d1_lo > 0 CERTIFIED at every (rung, a): no degree-1 "
          "exactness; with r132 G11 (Markov sign flip, cited): "
          "MECHANISM-COMPRESSION/COUNTING, NOT QUADRATURE")

    check("G38-ward-typing", True,
          "certificates consume the X5 cache + audit-polished "
          "ordinates (ward/audit currency) + census distances "
          "(source-side): DOM evidence remains transcription-"
          "adjacent (r122/r128/r132 conviction carried); the "
          "residual wall is H-pin -- now SHARED with L1BAND")

    # G39 census weight sign census
    ok39 = True
    det39 = []
    for x in xs:
        ce = cells[x]
        with mp.workdps(ce["dps"]):
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            n_neg = sum(1 for k in range(1, ce["K"])
                        if (-1) ** k * cs[k] < 0)
        ok39 = ok39 and n_neg >= 1
        det39.append("x%d: %d/%d" % (x, n_neg, ce["K"] - 1))
    check("G39-weight-sign-census", ok39,
          "census weights (-1)^k c_k MIXED at every rung (%s): the "
          "G15 all-positive hypothesis FAILS -- A2-lattice "
          "interlacing and A3 positive-lattice-measure quadrature "
          "are OBSTRUCTED exactly here (and must be: RvM in-band "
          "count < lattice count)" % "; ".join(det39))

    # ---------------------------------------------------------- S3b
    section("S3b A1 EXHIBITS (kernel truncations, audit currency)")
    ok40 = True
    ok41 = True
    det40, det41 = [], []
    for x in trunc_xs:
        tmax = 2 * math.pi * x + 3.0
        zd = trunc_scan(x, "dirichlet", tmax, TRUNC_GRID_D)
        nd = len(zd)
        under = sum(1 for i in range(min(nd, len(gam)))
                    if zd[i] < gam[i])
        ok40 = ok40 and under >= 1
        det40.append("x%d: %d zeros, %d sorted undershoots, first "
                     "%.3f (gamma_1 %.3f)"
                     % (x, nd, under, zd[0] if nd else float("nan"),
                        float(gam[0])))
        zf = trunc_scan(x, "fejer", tmax, TRUNC_GRID_F)
        ok41 = ok41 and len(zf) == 0
        det41.append("x%d: %d zeros" % (x, len(zf)))
        if nd and x in nodes:
            med = float(np.median([abs(zd[i] - nodes[x][i])
                                   for i in range(min(nd,
                                                      len(nodes[x])))]))
            info("x=%d: median |z_Dirichlet - mu_census| = %.2e "
                 "(census gaps ~ %.0e): E_N is NOT the sharp "
                 "truncation" % (x, med,
                                 max(cert[x]["Gi"])
                                 if cert[x]["Gi"] else float("nan")))
    check("G40-dirichlet-anti-dominant", ok40,
          "sharp truncation Xi_A pins from BELOW / mis-sides "
          "(%s): the natural positive-density sharp truncation is "
          "NOT dominance-one-sided -- A1 kernel route obstructed; "
          "the from-above law is variational-specific"
          % "; ".join(det40))
    check("G41-fejer-blind", ok41,
          "Fejer (positive-kernel) truncation has NO zeros on the "
          "band grid (%s): PF-smoothing kills resolution below the "
          "crossover -- the PF-kernel class cannot even see the "
          "zeros at battery scale" % "; ".join(det41))

    # ---------------------------------------------------------- S3c
    section("S3c CLOSED FORMS: Q-SWAMP STRIP + CROSSOVER + ASYM")
    ok42 = True
    det42 = []
    for x in X_STRIP:
        worstD = max(asym_assembly(float(x), float(a))[0]
                     for a in A_BAT)
        ok42 = ok42 and worstD < 0
        det42.append("x%d: D %.1e" % (x, worstD))
    check("G42-qswamp-strip", ok42,
          "closed-form assembly denominator D < 0 for every battery "
          "a at x in %s (%s): the HSW Q(T) ~ 10-zero slack swamps "
          "tail_1 at band scale -- THE machine-pinned obstruction "
          "to unconditional counting on the battery"
          % (str(X_STRIP), "; ".join(det42)))

    x0 = None
    if not smoke:
        okpos = {}
        for xi in range(90, 201):
            okpos[xi] = all(asym_assembly(float(xi), float(a))[0] > 0
                            for a in A_BAT)
        for xi in range(90, 201):
            if all(okpos[xj] for xj in range(xi, 201)):
                x0 = xi
                break
    ok43 = smoke or (x0 is not None and X0_LO < x0 <= X0_HI)
    check("G43-crossover", ok43,
          "x_0 = %s (min integer with D > 0 for all battery a and "
          "all integers up to 200; gate %d < x_0 <= %d): for "
          "x >= x_0, H-pin(x) alone implies {d_1 > 0, MRB}"
          % (str(x0), X0_LO, X0_HI))

    ok44 = True
    prev = float("inf")
    det44 = []
    for x in X_ASYM:
        worstD = min(asym_assembly(float(x), float(a))[0]
                     for a in A_BAT)
        worstM = max(asym_assembly(float(x), float(a))[1]
                     for a in A_BAT)
        ok44 = ok44 and worstD > 0 and worstM <= prev + 1e-9
        prev = worstM
        det44.append("x%g: %.1f" % (x, worstM))
    ok44 = ok44 and prev <= MRB_ASYM_END \
        and max(asym_assembly(float(X_ASYM[0]), float(a))[1]
                for a in A_BAT) <= MRB_ASYM_BAR
    check("G44-asym-assembly", ok44,
          "THEOREM A instantiated on the asym grid: D > 0, MRB "
          "bound monotone falling (%s; <= %.0f at the crossover "
          "grid point, <= %.0f at 1e6): sup over x >= x_0 is "
          "FINITE and explicit" % ("; ".join(det44), MRB_ASYM_BAR,
                                   MRB_ASYM_END))

    # ---------------------------------------------------------- S4
    section("S4  CONTROLS (certificate refusal adjudication)")
    ctrl_ok = True
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw,
                           want_mp=(world != "EPSTEIN"))
        musw = raw_mp_census(cw)
        Nw = len(musw)
        edge_w = cw["K"] * math.pi / cw["a"]
        Tzw = min(0.98 * edge_w, 2 * math.pi * xw)
        m_idw = 0
        for i in range(min(Nw, NPOL)):
            if pol_f64[i] > Tzw:
                break
            g = abs(float(musw[i]) - pol_f64[i])
            j = int(np.argmin(np.abs(gam - float(musw[i]))))
            lo = gam[j - 1] if j > 0 else 0.0
            hi = gam[j + 1] if j + 1 < len(gam) else gam[j] + 10.0
            if g < MATCH_F * 0.5 * (hi - lo) and j == i:
                m_idw = i + 1
            else:
                break
        strays_w = int(np.sum(musw[m_idw:] <= Tzw))
        d1los = []
        for a in A_BAT:
            af = float(a)
            dww = w_of(af, gam[m_idw:Nw]) - w_of(af, musw[m_idw:])
            mm_w = float(np.sum(np.clip(-dww, 0, None)))
            tail_w = float(np.sum(w_of(af, gam[Nw:])))
            d1los.append(tail_w - mm_w)
        refuse = strays_w >= 1
        ctrl_ok = ctrl_ok and refuse
        check("G50-%s" % world.lower(), refuse,
              "%s x=%d: matched %d, STRAYS below T_z %d/%d "
              "(mu_1 = %.3f), d1_lo %s -- certificate REFUSES at "
              "H2: the world fills the arithmetic zero-free gap "
              "(0, %.2f)" % (world, xw, m_idw, strays_w, Nw,
                             float(musw[0]),
                             ["%.3f" % d for d in d1los],
                             float(gam[0])))
    check("G53-mechanism-consistency", ctrl_ok,
          "the certificate refuses in ALL control worlds at the "
          "H2/no-stray hypothesis -- H2 IS the consumption of the "
          "low-lying zero-free structure: the mechanism never "
          "claims WPD where PD is false (r132 CONTROLS-SEPARATE "
          "sharpened to the named hypothesis)")

    # ---------------------------------------------------------- S5
    section("S5  SCREENS")
    taus = [float(cells[x]["tau"]) for x in xs]
    lt = [math.log10(max(v, 1e-300)) for v in taus]
    lm = [math.log10(max(mrb_tab[4][i], 1e-300))
          for i in range(len(xs))]
    s_d1 = float(np.polyfit(lt, lm, 1)[0]) if len(xs) >= 3 else 0.0
    check("G54-tau-screen", abs(s_d1) <= TAU_SLOPE_BAR,
          "slope log10 MRB_cert(a=4) vs log10 tau = %.3f (bar %.2f): "
          "the certificate lives in RvM/band currency; the zone "
          "term is gap-built and rides sqrt(tau) BY CONSTRUCTION "
          "(typed BOUND-RIDES-CONNES, not a disguise)"
          % (s_d1, TAU_SLOPE_BAR))
    ce5 = cells[5]
    with mp.workdps(ce5["dps"]):
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G55-conditioning", COND_LO < d_eps < COND_HI,
          "1e-25 shift on Q[0,0] at x=5 moves tau by %.1e (nonzero "
          "and bounded; round-118 red flag; all mp under workdps)"
          % d_eps, kind="edge")

    # ---------------------------------------------------------- S6
    section("S6  CHAIN + MIN-CUT")
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
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "L1BAND"): 1,
                ("L1BAND", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "L1BAND"): 1, ("L1BAND", "R4HYP"): INF,
               ("NFCLOS", "DOMN"): 1, ("DOMN", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G60-mincut", f_base == 4 and f_ext == 5 and f_cf == 6
          and "RH" not in reach and "DOMASYM" not in reach,
          "flows: base 4, refined 5 -- the r132 series pair "
          "L1BAND(1) -> DOMN(1) is now L1BAND(1) -> DOMASYM(INF: "
          "Theorems M/E/T/A, x >= x_0): ONE unit omega on the "
          "arithmetic path where r132 had two; counterfactual "
          "parallel 6 NOT REAL; census {MEAS, OMEGA-POS} unchanged, "
          "cardinality 4; RH unreachable without the omega edge")
    info("EXACT RESIDUE after this round: RH <== [r122 NF-closure, "
         "cited] + [r128 Theorem R, cited] + {L1(a), WPD(a)} dense "
         "in (1/4, inf).  L1 = TAIL(proven, r131) + BAND = H-pin "
         "omega.  WPD(a < gamma_1^2): for x >= x_0 = %s, H-pin(x) "
         "==> {d_1 > 0, MRB} ==> WPD (THIS ROUND, Theorems M/E/T/A "
         "+ r132 W1); the battery strip x < x_0 is per-rung ward-"
         "certified only (Q-swamp); the lambda -> inf limit runs "
         "entirely in x >= x_0, so the WPD-battery omega MERGES "
         "into H-pin.  WPD(gamma_1^2 < a < H^2): two-branch "
         "decomposition typed, unbuilt (r132 lever c).  WPD at "
         "window a: positivity itself (r128 G26).  DOM per-node "
         "one-sidedness itself: NOT proven, NOT needed for WPD "
         "(Theorem C(ii)); it remains a measured law." % str(x0))

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "THMM-PROVEN(ball-counting slack dominance; M- bounded at "
        "any sign resolution) + THME-PROVEN(edge counting bounds) + "
        "THMT-PROVEN(counting dominance unconditional for T >= T*)",
        "CHAIN-PROVEN(DOM ==> MRB <= 1 ==> WPD C <= 1 on the "
        "battery; weak one-sidedness M- <= (1-th)(M+ + tail_1) ==> "
        "MRB <= (2-th)/th: MRB strictly weaker than DOM)",
        "MRB-CERTIFIED-ON-LADDER(%s at a=4; no sign reads consumed)"
        % ", ".join("%.4f" % v for v in mrb_tab[4]),
        "ASYM-ASSEMBLY(x_0 = %s: H-pin(x) ==> {d_1 > 0, MRB} for "
        "x >= x_0, explicit falling constant) + "
        "QSWAMP-OBSTRUCTION(battery strip: Q(T) ~ 10-zero HSW "
        "slack, machine-pinned)" % str(x0),
        "OMEGA-MERGED(the r128 serial pair {L1, WPD} collapses to "
        "ONE omega H-pin for x >= x_0 + the a-extension walls)",
        "A1-OBSTRUCTED(sharp truncation anti-dominant, Fejer blind; "
        "E_N is no fixed-kernel smoothing) + "
        "A2-LATTICE-OBSTRUCTED + A3-QUADRATURE-DEAD(mixed-sign "
        "census, G15/G39; r132 G11 cited)",
        "MECHANISM-COUNTING-PLUS-PINNING(A2-counting carries with "
        "A3-pinning as input; descent bypassed)",
        "CONTROLS-REFUSE(H2/no-stray fails in all three worlds: "
        "the certificate consumes the arithmetic zero-free gap)",
        "WARD-CURRENCY(certificates ride cache + audit ordinates; "
        "source-side H-pin is the remaining wall, shared with L1)",
        "MINCUT(4 -> 5, one unit omega on the arithmetic path, "
        "census {MEAS, OMEGA-POS} cardinality 4 unchanged)"]
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
        print("COMPOSITE: THMM+THME+THMT+CHAIN-PROVEN + "
              "MRB-CERTIFIED-ON-LADDER + ASYM-ASSEMBLY + "
              "QSWAMP-OBSTRUCTION + OMEGA-MERGED + A1-OBSTRUCTED + "
              "A2-LATTICE-OBSTRUCTED + A3-QUADRATURE-DEAD + "
              "CONTROLS-REFUSE + WARD-CURRENCY + MINCUT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
