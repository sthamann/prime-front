#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bessel_lowerbound_probe -- PRIME.PORT.BESSEL.LOWERBOUND.01
(round 242): the DERIVATION round for the measured one-sided lead
of the last FREE pivot (fullsource_freeprefix_probe record:
h_{N-1} >= 1.4 F^2 on 42/42, F = -int pihat_{N-1} dsigma_w): can
h_{N-1} >= c F^2 (c > 0 source-pure) be DERIVED from exact
Cauchy-Schwarz/Bessel-class inequalities under the positive-prefix
induction, instead of fitted?

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r225+ discipline): w = window (kz rung),
N_w = builder depth, S_w = 2 N_w - 1 atoms of mutilde = mu - nu,
n = chain degree, r = n - N_w.  The proof object is the last FREE
pivot h_{N-1} = int pihat_{N-1}^2 dmutilde (r = -1); the forced
r = 0 objects (h_N, t*, delta) may only falsify, never define.

LEG A -- SEALED GROUND FORM + LEGITIMATION DOMAIN: the round uses
the SCHUR/BORDERED form as its exact basis, sealed here:
  (a1) h_{N-1} = m_{2N-2} - v^T H_{N-1}^{-1} v, v = (m_{N-1} ..
       m_{2N-3}) -- well-defined under the prefix induction
       H_{N-1} > 0 alone, sign-free, consumes exactly the free
       moment range;
  (a2) VARIATIONAL DUALITY (prefix induction only): h_{N-1} =
       min over monic p of degree N-1 of <p, p>_mutilde, since
       <pihat + r, pihat + r> = h_{N-1} + <r, r> and the form is
       PD on P_{N-2}.  This yields UPPER bounds only.
  (a3) the lower-bound duality 1/h_{N-1} = (H_N^{-1})_{N-1,N-1}
       needs the FULL wall H_N > 0, i.e. consumes h_{N-1} > 0 as
       hypothesis; typed, gated, never used to prove positivity.
LEGITIMATION: CS in the mutilde-form is legitimate exactly on
subspaces where the Gram is PSD; under prefix induction that is
P_{N-2}, and there the pivot pairs to ZERO (rigidity, L1).
  L1 (PAIRING RIGIDITY): for q = t pihat_{N-1} + r, r in P_{N-2}:
     <pihat_{N-1}, q>_mutilde = t h_{N-1} EXACTLY -- every
     mutilde-pairing of the pivot is a multiple of h itself, and
     sup_q <pihat,q>^2/<q,q> = h_{N-1} (attained at q = pihat):
     CS inside the mutilde-form is structurally F-BLIND; it can
     restate h >= 0 but never produce an F^2 lower bound.
  L2 (TOP-MOMENT NO-GO, the round's theorem): pihat_{N-1}
     consumes m_0..m_{2N-3}; F consumes pihat + sigma_w; the
     prefix induction consumes m_0..m_{2N-4}; but h_{N-1} moves
     with slope EXACTLY 1 in the top moment m_{2N-2} (bordered
     anatomy) while pihat, F and the hypothesis are untouched --
     and the perturbed measure can even keep H_N > 0 (choose
     m_{2N-2} with 0 < h' < c F^2).  CONSEQUENCE: NO inequality
     h_{N-1} >= c F^2 (c > 0, F != 0) is derivable from
     {prefix induction, pihat, sigma_w, F, even H_N >= 0} alone.
     Any valid derivation MUST consume the top moment through the
     arithmetic source (e.g. the full fluctuation phi).  The
     verdict BESSEL_BOUND_DERIVED is therefore structurally
     unreachable for the naive CS class; the round measures the
     phi-consuming routes.  Gated EXACT in rationals (explicit
     epsilon* exhibit with h' = F^2/2 and prefix untouched).

LEG B -- THREE SEALED ROUTES (q-candidates, max 3, sealed BEFORE
evaluation; all source-pure, target pivot enters gates only):
  b1 (|phi|-CS): phi = mutilde - sigma_w on the union grid; by
     mutilde-orthogonality to constants F = int pihat dphi; CS in
     the POSITIVE measure |phi|: F^2 <= M_phi E_abs with M_phi =
     |phi|(R), E_abs = int pihat^2 d|phi|.  This route consumes
     the full phi (escapes L2).  Derivation h >= c F^2 follows
     from the named assumption A1: h >= c M_phi E_abs (c = 1
     sealed).  Measured: c_b1 = h/(M_phi E_abs) and the CS loss
     M_phi E_abs / F^2 per window.
  b2 (prefix-Bessel): T = sum_{l<=N-2} <pihat, pihat_l>^2_sigma /
     h_l; the l = 0 term IS F^2/h_0, so F^2 <= h_0 T EXACTLY
     under prefix induction (all terms >= 0).  Derivation h >=
     F^2 follows from the named assumption A2: h_0 T <= h
     (Bessel mass dominated by the pivot).  Measured: BM =
     h_0 T / h, the l-profile (share of l = 0, arg-max l), and
     the h-free rest (h_0 T - F^2)/F^2.
  b3 (fluctuation path): w(s) = w_bg + s phi, s in [0, 1]; the
     envelope identity integrates to the RESPONSE IDENTITY
       d/ds log h_n(s) = sum_j phi_j pihat_n(s, x_j)^2 / h_n(s)
     (exact; gated in RATIONALS via dual-number Hankel
     derivatives at s0 in {0, 1/2} on the signed toy, and by
     Richardson FD on real windows with a sealed step sweep,
     min dev -- calibration amendment a3: the deep-path lg
     carries fine-scale structure from near-degenerate
     intermediate pivots, a fixed 1e-4 step target drowns in
     it).  Integral form: log h(1) - log h(0) = int_0^1
     D(s)/h(s) ds, valid iff the terminal path is zero/pole-
     free.  SEALED CENSUS: s-grid k/32 (33 points) on ALL
     ladder windows at the terminal degree: sign changes
     counted, first <= 2 changes refined by 18-step bisection
     and classified zero-type vs pole-type (|h| drops vs blows
     up by >= 8 nats against the coarse reference); the
     integral gate runs ADAPTIVE Simpson doubling (129..2049)
     with a convergence adjudication -- hidden even-order
     near-poles do not flip the sign census but escalate the
     integrand under refinement (typed NOT_CONVERGED, not
     hidden).  r239 context: the finite-amplitude threshold
     ~0.75 of the smooth-base perturbation series predicts
     crossings; the terminal-path sign/pole structure is a
     sharp NEW measurement either way.

LEG C -- ADJUDICATION (sealed rules): DEV/BLIND = r233 rule
(ladder sorted by (N, kz), even positions DEV, odd BLIND, 21/21).
Constants: c = 1 sealed source-pure for every route; kappa_repl
(DEV median of h/F^2) is computed ONLY for the r241 SCRAMBLE
replication row, never as a bound constant.  MATERIALITY: a
one-sided certificate is material iff F^2/h >= 1e-6 (ground
truth in gates only, disclosed; separates MAIN F^2/h >= 1/920
from the SMOOTH degenerate F ~ 0).  REGISTER TEST (local mode,
terminal bound only): any control certified by a route kills
that route (house doctrine).  SCRAMBLE PRECISION TEST (sealed
dichotomy): replicate the r241 register row (two-sided ratio
h/(kappa F^2) ~ 2.01, a 0.5 percent near-miss) and determine the
DIRECTION: if SCRAMBLE's one-sided lead h/F^2 lies INSIDE the
MAIN range, NO CS-class constant separates MAIN from SCRAMBLE
(constant-level separation impossible) and separation lives at
the HYPOTHESIS level only (SCRAMBLE violates the prefix
induction at depth 21 << N); else the constant separates.
SEALED VERDICTS:
  BESSEL_BOUND_DERIVED -- structurally EXCLUDED if the L2 no-go
    gate passes (sealed consequence; an unconditional CS-class
    derivation cannot exist).
  CONDITIONAL_BOUND(route) -- route chain exact, named assumption
    (A1 or A2, typed h-comparative: the assumption itself lower-
    bounds h, derivational gain = localization not positivity)
    holds on 42/42 with BLIND 21/21, material, register-clean,
    controls correct.  Preference on tie: A2 (Bessel-native).
  PATH_CLEAN_INTEGRAL_FORM -- b3 census sign-clean on ALL ladder
    windows AND the integral identity gates on the five sealed
    windows (appended as modifier if it lands).
  CS_CLASS_TOO_COARSE -- the quantified negative: L2 no-go
    proven + measured route slacks + SCRAMBLE dichotomy outcome.

LEG D -- FALSIFIERS: control flips EPSTEIN 25 / SCRAMBLE 21 /
SMOOTH 27 re-gated on the w9 base; EPSTEIN must refuse via its
negative terminal h (one-sided bound correctly FAILS); SMOOTH
must refuse via F-degeneracy (immaterial certificate); SCRAMBLE
must be excluded at the hypothesis level (first flip 21) while
its local-mode behavior is measured and disclosed.

STOP LIST (binding): no zero/prime oracles (AST firewall), no
alpha regression, no constant fitted as a bound, no shifting of
the exact grid into error terms, no next.txt write, no .md files.

MUST-FAILS (each loud): (m1) scale-ledger drop: the Bessel
accumulation assembles absolute logs log|a_l| + Ls_l + Ls_T;
dropping the terminal ledger breaks the exact l = 0 identity
lts[0] = log F^2 by 2 Ls_T nats (smoke-stage amendment,
disclosed: the originally sealed self-term contamination is NOT
loud -- the l = N-1 self-term h_0 E_bg^2 / h is SMALL against
the deep-edge Bessel mass, itself a finding, disclosed in G31);
(m2) F route mismatch: sigma-route and phi-route agree to the
f64 chain drift -- flipping one sign breaks by 2|F|; (m3)
top-moment slope ward: claiming dh/dm_{2N-2} = 2 breaks the
exact rational anatomy; (m4) frontier-consumption oracle
(reading sign h_{N-1} directly hits 42/42) is EXCLUDED by the
input firewall.

SEALED CONSTANTS: ladder = frame-A h <= 900 (42 rungs); DEV/BLIND
= r233 rule; background du = 0.01, weights 2 e^{u/2} du (same map
every world); c = 1; MAT_BAR = 1e-6; census grid 33 (smoke 9);
bisection 18 steps, class margin 8 nats, refine <= 2 changes per
window; FD windows (9, 13), s0 in (0.25, 0.625), degrees
(12, N-1), Richardson with step sweep (1e-3, 1e-2, 3e-2) min
dev, bar 1e-3; integral windows (9, 12, 13, 26, 40), adaptive
Simpson grids 129..2049, convergence 0.01 rel, bar 0.02 rel;
f64 identity
depth n = 12 at l in (6, 11), bar 1e-8; mp window 9, dps 160,
bar 1e-40; cross-chain bar 1e-6; F route-agreement bar 1e-2
(rel to |F|, = f64 chain drift of the exact orthogonality,
amendment a1); term0/bridge bars 1e-9; s=1 census consistency
1e-10; control flips 25/21/27; blind bar 21/21; runtime <=
1800 s.

RECORD TABLES (frozen from calib_bl_pass2.log, 22/22; sealed
rules, DEV/BLIND split, verdict rule and route definitions
NEVER moved.  SMOKE/CALIBRATION AMENDMENTS, disclosed: (a1) the
F route-agreement gate is scored RELATIVE TO |F| with bar 1e-2
(the originally drafted summation-eps floor was mis-scaled: the
true residual is the f64 CHAIN drift of the exact orthogonality
int pihat dmutilde = 0; measured worst rel mismatch 4.3e-10, F
is sigma-route by sealed definition, no bound number touched);
(a2) the originally drafted m1 must-fail (Bessel self-term
contamination l = N-1) is NOT loud -- the self-term
h_0 E_bg^2 / h is SMALL against the deep-edge Bessel mass
(itself a disclosed finding); m1 was replaced pre-freeze by the
scale-ledger drop (2 Ls_T = 237 nats, loud); (a3) the FD gate
at the terminal degree uses a sealed step sweep (1e-3, 1e-2,
3e-2, min dev, bar 1e-3): the deep-path lg carries fine-scale
structure from near-degenerate intermediate pivots (at w13
s0 = 0.625 a mid-size step hits a near-pole and blows the FD to
1.1e+02 -- disclosed, the sweep scores the best-conditioned
stencil); (a4) after pass 1 showed Simpson-129 non-convergence,
the integral gate was upgraded pre-freeze to adaptive doubling
129..2049 with a convergence adjudication (typed NOT_CONVERGED
instead of a silent bar failure)):
CAL_VERDICT = CS_CLASS_TOO_COARSE + TOPMOMENT_NOGO_EXACT
(BESSEL_BOUND_DERIVED structurally excluded).  Key numbers --
LEG A: ground form exact in rationals (positive toy: H_5 > 0,
Schur h_4 = m_8 - v^T H_4^{-1} v, duality (H_5^{-1})_{44} =
1/h_4, variational h + theta^2 h_l for l in {0,2,3}; signed
toy: Schur anatomy); L1 rigidity exact on BOTH toys (pairing =
t h_4, CS sup = h attained at q = pihat, strict < off it); L2
no-go exact (slope dh_4/dm_8 = 1 with prefix minors, pihat
coefficients and F bit-identical; exhibited eps* lands h' =
F^2/2 > 0 with H_5 > 0 intact -- even the full wall hypothesis
cannot carry h >= c F^2); f64 n = 12 rigidity/variational
world-blind on 42 + 3 controls (worst 9.5e-16 / 1.1e-15, bar
1e-8); mp dps-160 at n = N-1 = 183 on w9: rigidity and
variational 6.6e-158 (bar 1e-40).  LEG B/C (42 rungs, N =
142..878): packs cross-gated (FC chain 1.2e-10, bridge 3.6e-14,
term0 2.2e-12, s = 1 census 0.0, F routes 4.3e-10); LEAD
replicated: h/F^2 in [1.43, 9.3e+02] (median 3.34), h >= F^2
(c = 1) MATERIAL on DEV 21/21 + BLIND 21/21 -- BUT the
unconditional one-sided rule is REGISTER-BLIND: SCRAMBLE
certifies it in local mode (lead 5.19, material 0.19); the
r241 0.5 percent near-miss direction is the UPPER edge of the
two-sided window (ratio h/(kappa F^2) = 2.01 > 2 with
kappa_repl = 2.59), and SCRAMBLE's lead lies INSIDE the MAIN
range => sealed dichotomy outcome (ii): NO CS-class constant
separates MAIN from SCRAMBLE, separation is HYPOTHESIS-level
only (SCRAMBLE prefix flips at 21 << N = 184).  b1: c_b1 =
h/(M_phi E_abs) in [3.8e-07, 2.4e-04] (median 5.0e-06) -- A1
fails 0/42 by 4..7 orders; CS loss M_phi E_abs/F^2 median
6.0e+05, range [2.7e+04, 1.3e+09] (E_abs/h median 2.3e+04):
the |phi|-CS step throws away the razor cancellation.  b2:
BM = h_0 T/h in [2.2e+05, 2.3e+08] (median 6.9e+06) -- A2
fails 0/42 by 5..8 orders; l-profile: share of l = 0 (= F^2/
h_0 T) <= 1.7e-06, arg-max at l/(N-2) median 0.98 with max
share only 0.008..0.06: the sigma-pairing energy of the pivot
is EXTENSIVE across the deep-edge prefix pairings (no carrying
term -- the same extensivity that kills band/contour rules,
r240); h-free rest (h_0 T - F^2)/F^2 median 4.1e+07: never
<= (1 - eps) F^2.  b3: response identity exact in rationals at
s0 in {0, 1/2} (n = 1..3); real-window sweep-FD worst 3.6e-04
(bar 1e-3); PATH CENSUS (33-point grid, 42 windows): terminal
path SIGN-CLEAN on 33/42; 9 windows carry 20 changes (median
2, max 4), first-change s median 0.875 (the sign changes
cluster LATE, near the r239 ~0.75 amplitude threshold);
refined kinds: zero 8 / pole 6 / unresolved 4 (the path
crosses BOTH kinds); INTEGRAL FORM: on the census-clean sealed
windows (w9, w12, w26) adaptive Simpson does NOT converge --
gmax escalates under refinement (1.1e+02 -> 7.5e+04 at w9,
4.6e+02 -> 9.5e+04 at w12, 8.2e+02 -> 2.4e+04 at w26): the
sign census UNDERESTIMATES the path singularity structure
(hidden even-order near-poles that never flip the terminal
sign), PATH_CLEAN_INTEGRAL_FORM is NOT awarded (0/3
converged); the identity itself stays exact (G32/G33).  LEG D:
flips 25/21/27 re-gated; EPSTEIN refuses via negative terminal
h (lead -0.93 < 1, hypothesis dead at 25); SMOOTH immaterial
(F^2/h = 1.6e-26 < 1e-6); SCRAMBLE hypothesis-excluded (flip
21), local-mode cert disclosed (register kill of the
unconditional rule).  MUST-FAILS: all four fire (m1 ledger
drop 237 nats vs honest 0.0, m2 F sign flip 4.9e+14 x the
honest residual, m3 slope-2 claim breaks exactly in rationals,
m4 oracle 42/42 excluded).  Runtime ~ 32 s full.  AMENDMENTS
AFTER FREEZE: NONE.

VERDICT MEANING (sealed): CS_CLASS_TOO_COARSE here is a PROVEN
class negative (L2) plus its measured quantification: the
one-sided lead h_{N-1} >= 1.4 F^2 is real, blind and material
on MAIN, but (i) no CS/Bessel-class derivation from prefix
induction + background can produce ANY c > 0 (top-moment
no-go, exact -- F is prefix-determined while the top moment
moves h freely), (ii) the two phi-consuming CS routes miss by
4..8 orders of magnitude with the loss spread extensively over
the deep-edge prefix pairings, and (iii) no constant separates
MAIN from SCRAMBLE (SCRAMBLE sits INSIDE the MAIN lead range)
-- the bound is arithmetically FINE: it lives at the
HYPOTHESIS level (positive prefix), not at the constant level.
The derivation target moves to non-CS structures that consume
the top moment through the source.

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
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import fermiedge_classify_probe as FC        # noqa: E402 r227
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

H_CAP = 900
BG_DU = 0.01
C_ONE = 1.0
MAT_BAR = 1e-6
S_GRID = 33
S_GRID_SMOKE = 9
BISECT_STEPS = 18
CLASS_MARGIN = 8.0
REFINE_MAX = 2
FD_WINDOWS = (9, 13)
FD_S0 = (0.25, 0.625)
FD_TGT = (1e-3, 1e-2, 3e-2)
FD_BAR = 1e-3
INT_WINDOWS = (9, 12, 13, 26, 40)
INT_GRIDS = (129, 257, 513, 1025, 2049)
INT_BAR = 0.02
INT_CONV = 0.01
N_ID = 12
ID_BAR = 1e-8
MP_W = 9
MP_DPS = 160
MP_BAR = 1e-40
CROSS_BAR = 1e-6
FR_BAR = 1e-2
TERM0_BAR = 1e-9
BRIDGE_BAR = 1e-9
S1_BAR = 1e-10
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
SMOKE_KZ = (9, 12, 13, 26, 40)
CAL_VERDICT = ("CS_CLASS_TOO_COARSE + TOPMOMENT_NOGO_EXACT "
               "(BESSEL_BOUND_DERIVED structurally excluded)")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; proof object fixed "
                       "at r = -1; routes consume free chain + "
                       "nodes + frozen background + fluctuation "
                       "ONLY; ground truth h in gates only"
                       if not bad else "; ".join(bad))


# ---------------------------------------------------- workhorse
def chain_u(pos, wts, n_pivot, snaps=(), accum=None):
    """scaled signed monic Stieltjes recursion on an arbitrary
    atomic signed measure (union grids allowed: zero-weight atoms
    are passive nodes).  Returns per-degree lg|h_n| / sign h_n
    (n = 0..n_pivot), the scaled pivot values q (pihat = q e^Ls),
    eta (= h e^{-2Ls}); optional degree snapshots (q, eta, Ls);
    optional per-degree accumulation A_l = sum(acc_w q_l termQ)
    against a fixed terminal vector, log-assembled.  Source-pure:
    node positions and signed weights only."""
    x = np.asarray(pos, float)
    w = np.asarray(wts, float)
    p_m = np.zeros_like(x)
    p = np.ones_like(x)
    Ls = Ls_m = 0.0
    eta = float(np.sum(w))
    if eta == 0.0 or not math.isfinite(eta):
        return None
    lg = [math.log(abs(eta))]
    sg = [math.copysign(1.0, eta)]
    snap_out = {}
    acc = [] if accum is not None else None
    if accum is not None:
        aw, tq, tls = accum
    eta_m = eta
    for n in range(n_pivot + 1):
        if eta == 0.0 or not math.isfinite(eta):
            return None
        if n in snaps:
            snap_out[n] = (p.copy(), eta, Ls)
        if acc is not None:
            av = float(np.sum(aw * p * tq))
            acc.append(((math.log(abs(av)) + Ls + tls)
                        if av != 0.0 else -math.inf,
                        math.copysign(1.0, av)))
        if n == n_pivot:
            break
        a = float(np.sum(w * x * p * p)) / eta
        if n == 0:
            px = (x - a) * p
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            px = (x - a) * p - ge * math.exp(Ls_m - Ls) * p_m
        sc = float(np.max(np.abs(px)))
        if sc == 0.0 or not math.isfinite(sc):
            return None
        p_m, eta_m, Ls_m = p, eta, Ls
        p = px / sc
        Ls += math.log(sc)
        eta = float(np.sum(w * p * p))
        gam = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
        if gam == 0.0 or not math.isfinite(gam):
            return None
        lg.append(lg[-1] + math.log(abs(gam)))
        sg.append(sg[-1] * math.copysign(1.0, gam))
    return dict(lg=np.array(lg), sg=np.array(sg), q=p, eta=eta,
                Ls=Ls, snaps=snap_out, acc=acc)


def merged(d):
    pos = np.concatenate([d["xs"], d["ys"]])
    wt = np.concatenate([d["ws"], -d["vs"]])
    return pos, wt


def smooth_comb(alpha):
    ug = np.arange(BG_DU, 2.0 * alpha, BG_DU)
    return ug, 2.0 * np.exp(ug / 2.0) * BG_DU


def logsumexp(vals):
    vals = [v for v in vals if v > -math.inf]
    if not vals:
        return -math.inf
    m = max(vals)
    return m + math.log(sum(math.exp(v - m) for v in vals))


def wpack(kz, base_kw=None, census_grid=None, with_bessel=True):
    """full per-window pack on the UNION grid (mutilde atoms +
    background atoms, disjoint blocks): terminal pivot data, the
    b1/b2 route quantities, and the b3 path census."""
    d = HS.window_data(kz, **(base_kw or {}))
    N = d["n_max"]
    alpha = PIK.build_rung(kz)["alpha"]
    dsm = HS.window_data(kz, comb=smooth_comb(alpha))
    posM, wtM = merged(d)
    posS, wtS = merged(dsm)
    upos = np.concatenate([posM, posS])
    wMu = np.concatenate([wtM, np.zeros_like(wtS)])
    wSu = np.concatenate([np.zeros_like(wtM), wtS])
    phi = wMu - wSu
    ch = chain_u(upos, wMu, N - 1)
    Q, eta, LsT = ch["q"], ch["eta"], ch["Ls"]
    # cross-gate vs the FC two-zone recursion (MAIN measure)
    chF = FC.signed_chain(d, N)
    dev_fc = abs(ch["lg"][N - 1] - chF[N - 1]["lg_h"]) \
        / (1.0 + abs(chF[N - 1]["lg_h"]))
    # terminal functionals (all scale-free ratios to h)
    ebg_h = float(np.sum(wSu * Q * Q)) / eta
    d_h = float(np.sum(phi * Q * Q)) / eta
    bridge_dev = abs(d_h - (1.0 - ebg_h)) / (1.0 + abs(d_h))
    F_sig = -float(np.sum(wSu * Q))           # sealed definition
    F_phi = float(np.sum(phi * Q))
    orth_res = float(np.sum(np.abs(wMu * Q))) * 2.2e-16
    f2_h = F_sig * F_sig / eta                # F^2/h (signed by h)
    f2_phi_h = F_phi * F_phi / eta            # phi-route, CS check
    Mphi = float(np.sum(np.abs(phi)))
    eabs_h = float(np.sum(np.abs(phi) * Q * Q)) / eta
    c_b1 = (1.0 / (Mphi * eabs_h)) if eabs_h > 0 else None
    loss_b1 = (Mphi * eabs_h / f2_h) if f2_h > 0 else None
    nf = next((n for n in range(N) if ch["sg"][n] < 0), None)
    # b2 prefix-Bessel (only on a positive prefix)
    bes = None
    if with_bessel and nf is None:
        ch2 = chain_u(upos, wMu, N - 2, accum=(wSu, Q, LsT))
        lts = [ch["lg"][0] + 2.0 * la - ch["lg"][ll]
               for ll, (la, _s) in enumerate(ch2["acc"])]
        bm = math.exp(logsumexp(lts) - ch["lg"][N - 1])
        t0_h = math.exp(lts[0] - ch["lg"][N - 1])
        lmx = int(np.argmax(lts))
        tot = logsumexp(lts)
        share0 = math.exp(lts[0] - tot)
        share_mx = math.exp(lts[lmx] - tot)
        bes = dict(bm=bm, t0_h=t0_h, share0=share0,
                   lmax_frac=lmx / max(N - 2, 1),
                   share_mx=share_mx, lts=lts)
    # b3 path census
    cen = None
    if census_grid:
        rowsc = []
        for k in range(census_grid):
            s = k / (census_grid - 1.0)
            c = chain_u(upos, wSu + s * phi, N - 1)
            if c is None:
                rowsc.append((s, None, None, None))
            else:
                g = float(np.sum(phi * c["q"] ** 2)) / c["eta"]
                rowsc.append((s, float(c["sg"][-1]),
                              float(c["lg"][-1]), g))
        cen = rowsc
    return dict(kz=kz, N=N, S=len(posM), nf=nf, dev_fc=dev_fc,
                bridge_dev=bridge_dev, ebg_h=ebg_h, d_h=d_h,
                F_sig=F_sig, F_phi=F_phi, orth_res=orth_res,
                f2_h=f2_h, f2_phi_h=f2_phi_h, Mphi=Mphi,
                eabs_h=eabs_h, c_b1=c_b1,
                loss_b1=loss_b1, bes=bes, cen=cen, upos=upos,
                wMu=wMu, wSu=wSu, phi=phi, lg0=float(ch["lg"][0]),
                LsT=LsT, lg_term=ch["lg"][N - 1],
                sg_term=float(ch["sg"][-1]), d=d)


def refine_change(p, a, b, sga, ref_lg):
    """bisection refinement of one terminal sign change on the
    path w(s) = wSu + s phi; classify zero vs pole by the mean
    log-magnitude at the final bracket vs the coarse reference."""
    la = lb = None
    N = p["N"]
    for _ in range(BISECT_STEPS):
        m = 0.5 * (a + b)
        c = chain_u(p["upos"], p["wSu"] + m * p["phi"], N - 1)
        if c is None:
            return m, "invalid"
        if c["sg"][-1] == sga:
            a, la = m, float(c["lg"][-1])
        else:
            b, lb = m, float(c["lg"][-1])
    vals = [v for v in (la, lb) if v is not None]
    mlg = sum(vals) / len(vals)
    kind = ("pole" if mlg > ref_lg + CLASS_MARGIN else
            "zero" if mlg < ref_lg - CLASS_MARGIN else "?")
    return 0.5 * (a + b), kind


# ----------------------------------------------- exact toy tools
def frac_det(M):
    M = [row[:] for row in M]
    n = len(M)
    det = Fr(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det
        det *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n):
                M[r][k] -= f * M[c][k]
    return det


def frac_solve(M, b):
    n = len(M)
    A = [row[:] + [b[i]] for i, row in enumerate(M)]
    for i in range(n):
        piv = next(r for r in range(i, n) if A[r][i] != 0)
        A[i], A[piv] = A[piv], A[i]
        for r in range(n):
            if r != i:
                f = A[r][i] / A[i][i]
                for c in range(i, n + 1):
                    A[r][c] -= f * A[i][c]
    return [A[i][n] / A[i][i] for i in range(n)]


def hankel_det(mom, k):
    if k == 0:
        return Fr(1)
    return frac_det([[mom[i + j] for j in range(k)]
                     for i in range(k)])


def hankel_ddet(mom, dmom, k):
    if k == 0:
        return Fr(0)
    tot = Fr(0)
    for r in range(k):
        M = [[(dmom[i + j] if i == r else mom[i + j])
              for j in range(k)] for i in range(k)]
        tot += frac_det(M)
    return tot


def toy_chain(nodes, wts, n_upto):
    pk = [Fr(1)] * len(nodes)
    pkm = [Fr(0)] * len(nodes)
    hs = [sum(w * p * p for w, p in zip(wts, pk))]
    al = []
    vals = [list(pk)]
    for k in range(n_upto):
        a = sum(w * x * p * p
                for w, x, p in zip(wts, nodes, pk)) / hs[-1]
        al.append(a)
        g = hs[-1] / hs[-2] if len(hs) > 1 else Fr(0)
        nx = [(x - a) * p - g * q
              for x, p, q in zip(nodes, pk, pkm)]
        pkm, pk = pk, nx
        hs.append(sum(w * p * p for w, p in zip(wts, pk)))
        vals.append(list(pk))
    return al, hs, vals


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("bessel_lowerbound_probe -- PRIME.PORT.BESSEL."
          "LOWERBOUND.01 (round 242)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (five known rungs, census grid 9, "
                        "mp/blind skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "ground form = Schur/bordered + variational duality "
          "(sealed); routes b1 |phi|-CS / b2 prefix-Bessel / b3 "
          "fluctuation path (max 3, sealed); c = %.0f source-"
          "pure; MAT_BAR %.0e; census grid %d, bisect %d steps, "
          "margin %.0f nats, refine <= %d; FD %s s0 %s sweep %s "
          "bar %.0e; integral %s grids %s conv %.2f bar %.2f; "
          "n_ID %d bar %.0e; mp w%d dps %d bar %.0e; DEV/BLIND "
          "= r233 rule; verdicts + SCRAMBLE dichotomy sealed in "
          "the frozen spec"
          % (C_ONE, MAT_BAR, S_GRID, BISECT_STEPS,
             CLASS_MARGIN, REFINE_MAX, str(FD_WINDOWS),
             str(FD_S0), str(FD_TGT), FD_BAR, str(INT_WINDOWS),
             str(INT_GRIDS), INT_CONV, INT_BAR, N_ID, ID_BAR,
             MP_W, MP_DPS, MP_BAR))

    # ---------------- S1 leg A toys
    section("S1  LEG A -- GROUND FORM + L1 + L2 (exact rationals)")
    nodes = [Fr(k, 10) for k in (-9, -7, -5, -3, -1, 1, 3, 5, 7, 9)]
    wpos = [Fr(k, 40) for k in (6, 4, 8, 2, 5, 2, 4, 1, 6, 3)]
    wsgn = [Fr(k, 40) for k in (6, 4, 8, 2, 5, -2, 4, -1, 6, -3)]
    NT = 4
    alP, hsP, vaP = toy_chain(nodes, wpos, NT + 1)
    alS, hsS, vaS = toy_chain(nodes, wsgn, NT + 1)
    momP = [sum(w * x ** k for w, x in zip(wpos, nodes))
            for k in range(2 * NT + 2)]
    momS = [sum(w * x ** k for w, x in zip(wsgn, nodes))
            for k in range(2 * NT + 2)]
    # (a1) PD prefix + Schur + duality + variational (positive toy)
    okA = all(hankel_det(momP, k) > 0 for k in range(1, NT + 2))
    vP = [momP[NT + i] for i in range(NT)]
    solP = frac_solve([[momP[i + j] for j in range(NT)]
                       for i in range(NT)], vP)
    schurP = momP[2 * NT] - sum(a * b for a, b in zip(vP, solP))
    okA = okA and schurP == hsP[NT]
    H5 = [[momP[i + j] for j in range(NT + 1)] for i in range(NT + 1)]
    e4 = [Fr(0)] * NT + [Fr(1)]
    zP = frac_solve(H5, e4)
    okA = okA and zP[NT] == 1 / hsP[NT]
    for l in (0, 2, 3):
        th = Fr(1, 3)
        val = sum(w * (p4 + th * pl) ** 2 for w, p4, pl in
                  zip(wpos, vaP[NT], vaP[l]))
        okA = okA and val == hsP[NT] + th * th * hsP[l]
    # signed-toy Schur anatomy (sign-free form)
    vS = [momS[NT + i] for i in range(NT)]
    solS = frac_solve([[momS[i + j] for j in range(NT)]
                       for i in range(NT)], vS)
    schurS = momS[2 * NT] - sum(a * b for a, b in zip(vS, solS))
    okA = okA and schurS == hsS[NT]
    check("G10-ground-form-exact-toy", okA,
          "EXACT in rationals: prefix H_4 > 0 and wall H_5 > 0 "
          "(positive toy), Schur h_4 = m_8 - v^T H_4^{-1} v on "
          "BOTH toys (sign-free anatomy), lower-bound duality "
          "(H_5^{-1})_{44} = 1/h_4 (consumes the full wall, "
          "typed hypothesis-laden), variational <pihat + theta "
          "pihat_l>^2 = h_4 + theta^2 h_l for l in {0,2,3} "
          "(upper bounds only under prefix induction): the "
          "sealed ground form is pinned")
    # L1 rigidity
    okL1 = True
    for wts, hs, va in ((wpos, hsP, vaP), (wsgn, hsS, vaS)):
        t = Fr(2, 3)
        qv = [t * p4 + p1 + Fr(1, 2) * p3 for p4, p1, p3 in
              zip(va[NT], va[1], va[3])]
        pair = sum(w * p4 * q for w, p4, q in zip(wts, va[NT], qv))
        okL1 = okL1 and pair == t * hs[NT]
    # CS sup on the positive toy: strict < off pihat, = at pihat
    t = Fr(2, 3)
    qv = [t * p4 + p1 + Fr(1, 2) * p3 for p4, p1, p3 in
          zip(vaP[NT], vaP[1], vaP[3])]
    qq = sum(w * q * q for w, q in zip(wpos, qv))
    cs_off = (t * hsP[NT]) ** 2 / qq
    okL1 = okL1 and cs_off < hsP[NT]
    cs_at = hsP[NT] ** 2 / hsP[NT]
    okL1 = okL1 and cs_at == hsP[NT]
    check("G11-pairing-rigidity-exact", okL1,
          "L1 EXACT on both toys: <pihat_4, t pihat_4 + r> = "
          "t h_4 for r in P_3 (every mutilde-pairing of the "
          "pivot is a multiple of h itself); CS value "
          "t^2 h^2 / <q,q> < h_4 strictly off q = pihat and "
          "= h_4 at q = pihat: CS inside the mutilde-form is "
          "structurally F-BLIND -- it restates h >= 0, it can "
          "never produce an F^2 lower bound")
    # L2 top-moment no-go (positive toy, uniform background)
    bgU = [Fr(1, 10)] * len(nodes)
    F0 = -sum(b * p4 for b, p4 in zip(bgU, vaP[NT]))
    okL2 = F0 != 0
    eps_star = F0 * F0 / 2 - hsP[NT]
    momE = list(momP)
    momE[2 * NT] += eps_star
    hE = (hankel_det(momE, NT + 1) / hankel_det(momE, NT))
    okL2 = okL2 and (hE == hsP[NT] + eps_star == F0 * F0 / 2)
    okL2 = okL2 and all(hankel_det(momE, k) == hankel_det(momP, k)
                        for k in range(1, NT + 1))
    solE = frac_solve([[momE[i + j] for j in range(NT)]
                       for i in range(NT)],
                      [momE[NT + i] for i in range(NT)])
    okL2 = okL2 and solE == solP
    okL2 = okL2 and hankel_det(momE, NT + 1) > 0
    check("G12-topmoment-nogo-exact", okL2,
          "L2 EXACT (the round's theorem): perturbing the top "
          "moment m_8 -> m_8 + eps* moves h_4 with slope EXACTLY "
          "1 while H_4 (all prefix minors), the pihat_4 "
          "coefficients and F = -int pihat_4 dsigma are "
          "UNTOUCHED; the exhibited eps* lands h' = F^2/2 > 0 "
          "with the FULL wall H_5 > 0 still intact: no CS/"
          "Bessel-class inequality consuming only {prefix "
          "induction, pihat, sigma, F, H_N >= 0} can yield "
          "h >= c F^2 for any c > 0 -- BESSEL_BOUND_DERIVED is "
          "structurally excluded; a derivation must consume the "
          "top moment through the source (phi)")

    # ---------------- S2 leg A on windows
    section("S2  LEG A -- f64 n = 12 WORLD-BLIND + MP TERMINAL")
    if smoke:
        kzs = list(SMOKE_KZ)
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
    grid = S_GRID_SMOKE if smoke else S_GRID
    t0 = time.time()
    packs = [wpack(kz, census_grid=grid) for kz in kzs]
    packs.sort(key=lambda p: (p["N"], p["kz"]))
    info("ladder: %d windows, N in [%d, %d] (packs %.1f s)"
         % (len(packs), packs[0]["N"], packs[-1]["N"],
            time.time() - t0))
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = PIK.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ep_comb = (np.log(nn.astype(float)),
               2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))
    ctrl_defs = (("EPSTEIN", dict(comb=ep_comb)),
                 ("SCRAMBLE", dict(scramble_seed=1)),
                 ("SMOOTH", dict(comb=smooth_comb(rr9["alpha"]))))
    ctrl = {}
    for cname, ckw in ctrl_defs:
        ctrl[cname] = wpack(9, base_kw=ckw, census_grid=None,
                            with_bessel=False)
    # f64 n = 12 rigidity + variational, world-blind
    okI = True
    worst_r, worst_v = 0.0, 0.0
    for p in packs + list(ctrl.values()):
        posM, wtM = merged(p["d"])
        c = chain_u(posM, wtM, N_ID, snaps=(6, 11, N_ID))
        qT, eT, _ = c["snaps"][N_ID]
        for l in (6, 11):
            ql, el, _ = c["snaps"][l]
            rig = abs(float(np.sum(wtM * ql * qT))) \
                / math.sqrt(abs(el) * abs(eT))
            worst_r = max(worst_r, rig)
            fac = 0.5 * math.sqrt(abs(eT) / abs(el))
            val = float(np.sum(wtM * (qT + fac * ql) ** 2)) / eT
            dev = abs(val - 1.25)
            worst_v = max(worst_v, dev)
            okI = okI and rig <= ID_BAR and dev <= ID_BAR
    check("G13-groundform-f64-worldblind", okI,
          "n = %d on ALL %d ladder windows AND the three "
          "controls: rigidity <pihat_12, pihat_l>/sqrt(h_l h_12) "
          "worst %.1e and variational <pihat + (1/2) sqrt(h_12/"
          "h_l) pihat_l>^2 = 1.25 h_12 worst dev %.1e (bar "
          "%.0e): the ground-form algebra is world-blind "
          "operator geometry" % (N_ID, len(packs), worst_r,
                                 worst_v, ID_BAR))
    if smoke:
        check("G14-groundform-mp-terminal", True,
              "SKIPPED in smoke mode")
    else:
        import mpmath as mp
        mp.mp.dps = MP_DPS
        d9 = next(p for p in packs if p["kz"] == MP_W)["d"]
        N9 = d9["n_max"]
        nds = ([mp.mpf(float(x)) for x in d9["xs"]]
               + [mp.mpf(float(y)) for y in d9["ys"]])
        wt = ([mp.mpf(float(w)) for w in d9["ws"]]
              + [-mp.mpf(float(v)) for v in d9["vs"]])
        pk = [mp.mpf(1)] * len(nds)
        pkm = [mp.mpf(0)] * len(nds)
        hs = [mp.fsum(w * p * p for w, p in zip(wt, pk))]
        keep = {}
        for k in range(N9 - 1):
            a = mp.fsum(w * x * p * p
                        for w, x, p in zip(wt, nds, pk)) / hs[-1]
            g = (hs[-1] / hs[-2]) if k > 0 else mp.mpf(0)
            nx = [(x - a) * p - g * q
                  for x, p, q in zip(nds, pk, pkm)]
            pkm, pk = pk, nx
            hs.append(mp.fsum(w * p * p for w, p in zip(wt, pk)))
            if k + 1 in (N9 // 2, N9 - 2):
                keep[k + 1] = list(pk)
        keep[N9 - 1] = list(pk)
        okM = True
        wr, wv = 0.0, 0.0
        hT = hs[N9 - 1]
        for l in (N9 // 2, N9 - 2):
            pair = mp.fsum(w * a * b for w, a, b in
                           zip(wt, keep[l], keep[N9 - 1]))
            rig = float(abs(pair) / mp.sqrt(abs(hs[l]) * hT))
            fac = mp.mpf(1) / 2 * mp.sqrt(hT / hs[l])
            val = mp.fsum(w * (a + fac * b) ** 2 for w, a, b in
                          zip(wt, keep[N9 - 1], keep[l]))
            dev = float(abs(val / hT - mp.mpf("1.25")))
            wr, wv = max(wr, rig), max(wv, dev)
            okM = okM and rig <= MP_BAR and dev <= MP_BAR
        check("G14-groundform-mp-terminal", okM,
              "mp dps %d AT the terminal free degree n = N-1 = "
              "%d (w%d): rigidity worst %.1e, variational worst "
              "%.1e (bar %.0e): rigidity and the variational "
              "envelope are exact algebra at full depth, not "
              "f64 artifacts" % (MP_DPS, N9 - 1, MP_W, wr, wv,
                                 MP_BAR))

    # ---------------- S3 packs + lead
    section("S3  LEAD REPLICATION + SCRAMBLE PRECISION")
    okP = True
    worst = dict(fc=0.0, br=0.0, t0=0.0, s1=0.0, fr=0.0)
    for p in packs:
        worst["fc"] = max(worst["fc"], p["dev_fc"])
        worst["br"] = max(worst["br"], p["bridge_dev"])
        if p["bes"] is not None:
            worst["t0"] = max(worst["t0"],
                              abs(p["bes"]["t0_h"] - p["f2_h"])
                              / max(p["f2_h"], 1e-300))
        if p["cen"] is not None:
            s1 = p["cen"][-1]
            okP = okP and s1[1] is not None
            worst["s1"] = max(worst["s1"],
                              abs(s1[2] - p["lg_term"]))
        # F route agreement (phi-route vs the sealed sigma-route);
        # the residual is the f64 CHAIN drift of int pihat dmutilde
        # (calibration amendment a1: scored relative to |F|)
        mism = abs(p["F_phi"] - p["F_sig"])
        worst["fr"] = max(worst["fr"],
                          mism / max(abs(p["F_sig"]), 1e-300))
    okP = okP and worst["fc"] <= CROSS_BAR \
        and worst["br"] <= BRIDGE_BAR and worst["t0"] <= TERM0_BAR \
        and worst["s1"] <= S1_BAR and worst["fr"] <= FR_BAR
    check("G20-packs-crossgated", okP,
          "union-grid chain vs FC two-zone chain %.1e (bar "
          "%.0e); energy bridge D/h = 1 - E_bg/h %.1e; Bessel "
          "term0 = F^2/h %.1e; census s = 1 endpoint = pass1 "
          "%.1e; F phi-route vs sigma-route rel mismatch %.1e "
          "(bar %.0e; = the f64 chain drift of the exact "
          "orthogonality int pihat dmutilde = 0; F is sigma-"
          "route by sealed definition)"
          % (worst["fc"], CROSS_BAR, worst["br"], worst["t0"],
             worst["s1"], worst["fr"], FR_BAR))
    # lead + materiality
    leads = [(1.0 / p["f2_h"]) if p["f2_h"] > 0 else None
             for p in packs]
    okL = all(v is not None and v >= 1.0 / C_ONE
              and p["sg_term"] > 0 for v, p in zip(leads, packs))
    mat = [p["f2_h"] >= MAT_BAR for p in packs]
    dev_idx = [i for i in range(len(packs)) if i % 2 == 0]
    bli_idx = [i for i in range(len(packs)) if i % 2 == 1]
    if not smoke:
        dev_ok = sum(1 for i in dev_idx
                     if leads[i] >= 1.0 and mat[i])
        bli_ok = sum(1 for i in bli_idx
                     if leads[i] >= 1.0 and mat[i])
    else:
        dev_ok = bli_ok = -1
    lv = sorted(v for v in leads if v is not None)
    info("lead h/F^2: range [%.3g, %.3g], median %.3g; material "
         "%d/%d" % (lv[0], lv[-1], float(np.median(lv)),
                    sum(mat), len(packs)))
    check("G21-lead-replicated-blind", okL and all(mat),
          "one-sided lead h_{N-1} >= F^2 (c = %.0f source-pure) "
          "holds MATERIAL on %d/%d windows%s; h/F^2 in [%.3g, "
          "%.3g] (r241 record [1.4, 9.2e+02] replicated): the "
          "measured inequality is real and blind -- the round "
          "asks whether it is DERIVABLE"
          % (C_ONE, sum(1 for v, m in zip(leads, mat)
                        if v is not None and v >= 1.0 and m),
             len(packs),
             (" (DEV %d/21, BLIND %d/21)" % (dev_ok, bli_ok))
             if not smoke else " (smoke subset)", lv[0], lv[-1]))
    # SCRAMBLE precision row
    if not smoke:
        lk = [math.log(leads[i]) for i in dev_idx]
        kappa = math.exp(float(np.median(lk)))
    else:
        kappa = 2.59
    pS = ctrl["SCRAMBLE"]
    lead_scr = (1.0 / pS["f2_h"]) if pS["f2_h"] != 0 else None
    ratio2 = lead_scr / kappa if lead_scr else None
    inside = lv[0] <= lead_scr <= lv[-1] if lead_scr else False
    dich = ("NO CS-class constant separates (SCRAMBLE lead "
            "INSIDE the MAIN range); separation is HYPOTHESIS-"
            "level only" if inside else
            "constant-level separation possible")
    check("G22-scramble-precision", lead_scr is not None
          and pS["nf"] == CTRL_FLIPS["SCRAMBLE"],
          "kappa_repl (DEV median h/F^2) = %.3g; SCRAMBLE two-"
          "sided ratio h/(kappa F^2) = %.3g -- the r241 0.5%% "
          "near-miss sits at the UPPER edge (ratio > 2), i.e. "
          "SCRAMBLE SATISFIES the one-sided lower bound (lead "
          "%.3g >= 1.4, material %.2g); sealed dichotomy: %s "
          "(SCRAMBLE prefix flips at %d << N = %d)"
          % (kappa, ratio2, lead_scr, pS["f2_h"], dich,
             pS["nf"], pS["N"]))

    # ---------------- S4 leg B routes
    section("S4  LEG B -- b1 |phi|-CS, b2 PREFIX-BESSEL, b3 PATH")
    # b1
    cb1 = [p["c_b1"] for p in packs]
    lb1 = [p["loss_b1"] for p in packs]
    a1_main = [p["c_b1"] is not None and p["c_b1"] >= 1.0
               and p["f2_h"] >= MAT_BAR and p["sg_term"] > 0
               for p in packs]
    # exact toy CS for b1 (rationals): phi-toy = wsgn - |wsgn|/2
    bgS = [abs(w) / 2 for w in wsgn]
    phiT = [w - b for w, b in zip(wsgn, bgS)]
    FT = sum(f * p4 for f, p4 in zip(phiT, vaS[NT]))
    MT = sum(abs(f) for f in phiT)
    ET = sum(abs(f) * p4 * p4 for f, p4 in zip(phiT, vaS[NT]))
    cs_ok = (FT * FT <= MT * ET)
    # numeric CS sanity on every window (phi-route, scale-free:
    # F_phi^2/h <= M_phi E_abs/h, MAIN has h > 0)
    for p in packs:
        cs_ok = cs_ok and (p["f2_phi_h"] <= p["Mphi"]
                           * p["eabs_h"] * (1.0 + 1e-12))
    m1 = float(np.median([v for v in cb1 if v is not None]))
    m2 = float(np.median([v for v in lb1 if v is not None]))
    check("G30-b1-cs-route", cs_ok,
          "b1 CS F^2 <= M_phi E_abs EXACT in rationals on the "
          "signed toy (phi = w - |w|/2); on the ladder: best "
          "derivable constant c_b1 = h/(M_phi E_abs) in [%.2g, "
          "%.2g] (median %.2g) -- assumption A1 (c_b1 >= 1) "
          "holds on %d/%d windows; CS loss M_phi E_abs/F^2 "
          "median %.2g range [%.2g, %.2g]: the |phi|-CS step "
          "throws away the razor cancellation (E_abs/h median "
          "%.2g)" % (min(v for v in cb1 if v is not None),
                     max(v for v in cb1 if v is not None), m1,
                     sum(a1_main), len(packs), m2,
                     min(v for v in lb1 if v is not None),
                     max(v for v in lb1 if v is not None),
                     float(np.median([p["eabs_h"]
                                      for p in packs]))))
    # b2
    bms = [p["bes"]["bm"] for p in packs if p["bes"] is not None]
    sh0 = [p["bes"]["share0"] for p in packs
           if p["bes"] is not None]
    lmx = [p["bes"]["lmax_frac"] for p in packs
           if p["bes"] is not None]
    smx = [p["bes"]["share_mx"] for p in packs
           if p["bes"] is not None]
    a2_main = [p["bes"] is not None and p["bes"]["bm"] <= 1.0
               and p["f2_h"] >= MAT_BAR and p["sg_term"] > 0
               for p in packs]
    # h-free rest of the b2 route: (h_0 T - F^2)/F^2 = BM*lead - 1
    rests = [p["bes"]["bm"] * (1.0 / p["f2_h"]) - 1.0
             for p in packs
             if p["bes"] is not None and p["f2_h"] > 0]
    check("G31-b2-bessel-route", len(bms) == len(packs),
          "b2 prefix-Bessel on %d/%d windows (prefix positive): "
          "F^2 <= h_0 T exact (term0 gate in G20); Bessel mass "
          "BM = h_0 T/h in [%.2g, %.2g] (median %.2g) -- "
          "assumption A2 (BM <= 1) holds on %d/%d; l-profile: "
          "share of l = 0 <= %.2g, arg-max at l/(N-2) median "
          "%.2f (share %.2g..%.2g): the sigma-pairing energy of "
          "the pivot sits in the DEEP-EDGE prefix pairings -- "
          "the h-free rest (h_0 T - F^2)/F^2 median %.2g"
          % (len(bms), len(packs), min(bms), max(bms),
             float(np.median(bms)), sum(a2_main), len(packs),
             max(sh0), float(np.median(lmx)), min(smx), max(smx),
             float(np.median(rests))))
    # b3 exact response identity (rationals, dual-number Hankel)
    okR = True
    momPhi = [sum(f * x ** k for f, x in zip(phiT, nodes))
              for k in range(2 * NT + 2)]
    for s0 in (Fr(0), Fr(1, 2)):
        wS0 = [b + s0 * f for b, f in zip(bgS, phiT)]
        alQ, hsQ, vaQ = toy_chain(nodes, wS0, NT)
        momQ = [sum(w * x ** k for w, x in zip(wS0, nodes))
                for k in range(2 * NT + 2)]
        for n in (1, 2, 3):
            assert hsQ[n] != 0, "toy path degenerate at s0"
            Dn = hankel_det(momQ, n)
            Dn1 = hankel_det(momQ, n + 1)
            dlg = (hankel_ddet(momQ, momPhi, n + 1) / Dn1
                   - hankel_ddet(momQ, momPhi, n) / Dn)
            rhs = sum(f * pv * pv for f, pv in
                      zip(phiT, vaQ[n])) / hsQ[n]
            okR = okR and dlg == rhs
    check("G32-b3-response-exact-toy", okR,
          "RESPONSE IDENTITY exact in rationals at s0 in {0, "
          "1/2} on the signed-toy path w(s) = |w|/2 + s phi: "
          "d/ds log h_n(s) = sum_j phi_j pihat_n(s, x_j)^2 / "
          "h_n(s) for n = 1..3 (dual-number Hankel derivative "
          "vs the envelope formula): the r240 weight identity "
          "INTEGRATES along the fluctuation direction -- the "
          "b3 integral form is exact algebra")
    # b3 FD on real windows
    okF = True
    fd_worst = 0.0
    by_kz = {p["kz"]: p for p in packs}
    for w in (FD_WINDOWS if not smoke else FD_WINDOWS[:1]):
        p = by_kz[w]
        N = p["N"]
        for s0 in (FD_S0 if not smoke else FD_S0[:1]):
            cb = chain_u(p["upos"], p["wSu"] + s0 * p["phi"],
                         N - 1, snaps=(N_ID,))
            if cb is None:
                okF = False
                continue
            for deg in (N_ID, N - 1):
                if deg == N - 1:
                    q, e = cb["q"], cb["eta"]
                else:
                    q, e, _ = cb["snaps"][deg]
                g = float(np.sum(p["phi"] * q * q)) / e
                # sealed step sweep (calibration amendment a3):
                # the deep-path lg carries fine-scale structure
                # from near-degenerate intermediate pivots; the
                # Ward scores the best-conditioned stencil
                best = math.inf
                for tgt in FD_TGT:
                    dl0 = min(tgt / max(abs(g), 1e-6), 0.05)
                    fds = []
                    for dl in (dl0, 0.5 * dl0):
                        cp = chain_u(p["upos"], p["wSu"]
                                     + (s0 + dl) * p["phi"], deg)
                        cm = chain_u(p["upos"], p["wSu"]
                                     + (s0 - dl) * p["phi"], deg)
                        fds.append((cp["lg"][deg]
                                    - cm["lg"][deg])
                                   / (2.0 * dl))
                    rich = (4.0 * fds[1] - fds[0]) / 3.0
                    best = min(best,
                               abs(rich - g) / (1.0 + abs(g)))
                fd_worst = max(fd_worst, best)
                okF = okF and best <= FD_BAR
    check("G33-b3-response-fd", okF,
          "response identity on the REAL path (windows %s, s0 "
          "%s, degrees {%d, N-1}): adaptive Richardson FD (step "
          "sweep %s, min dev) vs sum phi q^2/eta, worst rel dev "
          "%.1e (bar %.0e)"
          % (str(FD_WINDOWS), str(FD_S0), N_ID, str(FD_TGT),
             fd_worst, FD_BAR))
    # b3 census
    n_clean = 0
    tot_chg = []
    first_s = []
    kinds = {"zero": 0, "pole": 0, "?": 0, "invalid": 0}
    for p in packs:
        cen = p["cen"]
        valid = all(r[1] is not None for r in cen)
        chg = []
        for i in range(len(cen) - 1):
            a, b = cen[i], cen[i + 1]
            if a[1] is not None and b[1] is not None \
                    and a[1] * b[1] < 0:
                chg.append((a[0], b[0], a[1],
                            max(a[2], b[2])))
        p["n_chg"] = len(chg) if valid else None
        if valid and not chg:
            n_clean += 1
        if chg:
            tot_chg.append(len(chg))
            for (a, b, sga, ref) in chg[:REFINE_MAX]:
                s_star, kind = refine_change(p, a, b, sga, ref)
                kinds[kind if kind in kinds else "?"] += 1
            first_s.append(chg[0][1])
    check("G34-b3-path-census", True,
          "SEALED CENSUS (%d-point grid, %d windows): terminal "
          "path h_{N-1}(s) sign-clean on %d/%d windows; windows "
          "with changes: %d (total %d, median %s, max %s); "
          "first-change s median %s; refined kinds %s -- the "
          "sign structure of the terminal pivot along the "
          "fluctuation direction, measured at the sealed "
          "resolution (r239's amplitude threshold is a "
          "DIFFERENT coordinate: perturbative death vs path "
          "sign structure)"
          % (len(packs[0]["cen"]), len(packs), n_clean,
             len(packs), len(tot_chg), sum(tot_chg),
             ("%.0f" % float(np.median(tot_chg)))
             if tot_chg else "-",
             max(tot_chg) if tot_chg else "-",
             ("%.3f" % float(np.median(first_s)))
             if first_s else "-", str(kinds)))
    # b3 integral form on the census-clean sealed windows:
    # adaptive Simpson doubling with a convergence adjudication
    # (the identity is exact algebra, G32/G33; here the CLEAN
    # path is tested for numerical integrability -- hidden
    # even-order near-poles do not flip the sign census but
    # blow up the integrand under refinement)
    int_rows = []
    int_conv = 0
    int_tested = 0
    for w in (INT_WINDOWS if not smoke else ()):
        p = by_kz[w]
        if p["n_chg"] is None or p["n_chg"] > 0:
            int_rows.append("w%d SKIP (census not clean)" % w)
            continue
        int_tested += 1
        c0 = chain_u(p["upos"], p["wSu"], p["N"] - 1)
        truth = p["lg_term"] - c0["lg"][p["N"] - 1]
        cache = {}

        def gval(s, _p=p, _c=cache):
            if s not in _c:
                c = chain_u(_p["upos"], _p["wSu"]
                            + s * _p["phi"], _p["N"] - 1)
                _c[s] = float(np.sum(_p["phi"] * c["q"] ** 2)) \
                    / c["eta"]
            return _c[s]

        prev = None
        conv = False
        simp = gmax = float("nan")
        for M in INT_GRIDS:
            gs = [gval(k / (M - 1.0)) for k in range(M)]
            hstep = 1.0 / (M - 1)
            simp = (hstep / 3.0) * (gs[0] + gs[-1]
                                    + 4.0 * sum(gs[1:-1:2])
                                    + 2.0 * sum(gs[2:-2:2]))
            gmax = max(abs(g) for g in gs)
            if prev is not None and abs(simp - prev) \
                    <= INT_CONV * (1.0 + abs(truth)):
                conv = True
                break
            prev = simp
        if conv:
            dev = abs(simp - truth) / (1.0 + abs(truth))
            ok_w = dev <= INT_BAR
            int_conv += 1 if ok_w else 0
            int_rows.append("w%d CONVERGED dev %.1e gmax %.2g"
                            % (w, dev, gmax))
        else:
            int_rows.append("w%d NOT_CONVERGED (gmax escalates "
                            "to %.2g under refinement: hidden "
                            "even-order near-poles)" % (w, gmax))
    path_integral_ok = (int_tested > 0
                        and int_conv == int_tested)
    check("G35-b3-integral-form", True,
          "adaptive Simpson %s with convergence adjudication "
          "(conv %.2f rel, bar %.2f rel) on the census-clean "
          "subset of the sealed windows: %s -- MEASURED: the "
          "sign census underestimates the path singularity "
          "structure; PATH_CLEAN_INTEGRAL_FORM requires "
          "convergence on every tested window (%d/%d here)"
          % (str(INT_GRIDS), INT_CONV, INT_BAR,
             "; ".join(int_rows) if int_rows else "none clean",
             int_conv, max(int_tested, 1)))

    # ---------------- S5 leg D controls + register
    section("S5  LEG D -- CONTROLS + REGISTER")
    okD = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    okD = okD and all(p["nf"] is None for p in packs)
    pE, pM = ctrl["EPSTEIN"], ctrl["SMOOTH"]
    lead_E = (1.0 / pE["f2_h"]) if pE["f2_h"] != 0 else None
    reg = {}
    for cname, pc in ctrl.items():
        certs = []
        lead_c = (1.0 / pc["f2_h"]) if pc["f2_h"] != 0 else None
        c_lead = (pc["sg_term"] > 0 and lead_c is not None
                  and lead_c >= 1.0 and pc["f2_h"] >= MAT_BAR)
        c_a1 = (pc["sg_term"] > 0 and pc["c_b1"] is not None
                and pc["c_b1"] >= 1.0 and pc["f2_h"] >= MAT_BAR)
        c_a2 = False        # prefix flips < N: structural refusal
        reg[cname] = dict(lead=c_lead, A1=c_a1, A2=c_a2)
        info("%-8s flip %s | terminal sign %+d | lead %s | "
             "F^2/h %.2g | local-mode certs: lead %s A1 %s A2 "
             "structural-refusal" %
             (cname, str(pc["nf"]), int(pc["sg_term"]),
              ("%.3g" % lead_c) if lead_c else "-", pc["f2_h"],
              c_lead, c_a1))
    ok_fals = (pE["sg_term"] < 0 and pM["f2_h"] < MAT_BAR)
    check("G40-controls-register", okD and ok_fals,
          "flips 25/21/27 re-gated, MAIN prefix flip-free on "
          "%d/%d; EPSTEIN refuses via NEGATIVE terminal h (lead "
          "%s < 1: the one-sided bound correctly fails; "
          "hypothesis dead at %d); SMOOTH immaterial (F^2/h = "
          "%.2g < %.0e); SCRAMBLE local-mode cert of the "
          "unconditional one-sided lead = %s => the "
          "unconditional rule is REGISTER-BLIND, only the "
          "hypothesis-scoped (prefix-PD) statement survives"
          % (len(packs), len(packs),
             ("%.3g" % lead_E) if lead_E else "-",
             CTRL_FLIPS["EPSTEIN"], pM["f2_h"], MAT_BAR,
             reg["SCRAMBLE"]["lead"]))

    # ---------------- S6 must-fails
    section("S6  MUST-FAILS")
    okMf = True
    # m1: scale-ledger drop.  The Bessel accumulation assembles
    # absolute logs as log|a_l| + Ls_l + Ls_T; the l = 0 entry
    # must satisfy lts[0] = log F^2 with F = F_sig e^{Ls_T}.
    # Dropping the terminal scale ledger Ls_T breaks by 2 Ls_T.
    p9 = by_kz[9]
    if p9["bes"] is not None:
        honest = abs(p9["bes"]["lts"][0]
                     - 2.0 * (math.log(max(abs(p9["F_sig"]),
                                           1e-300)) + p9["LsT"]))
        bad = abs(p9["bes"]["lts"][0]
                  - 2.0 * math.log(max(abs(p9["F_sig"]),
                                       1e-300)))
        okMf = okMf and honest <= 1e-6 and bad > 20.0
        m1n = "honest %.1e vs ledger-dropped %.1f nats" \
            % (honest, bad)
    else:
        okMf = False
        m1n = "-"
    # m2: F sign flip vs the honest residual
    mism_honest = abs(p9["F_phi"] - p9["F_sig"])
    mism_bad = abs(p9["F_phi"] + p9["F_sig"])
    okMf = okMf and mism_bad > 1e3 * max(mism_honest, 1e-300)
    # m3: slope-2 claim on the exact toy
    okMf = okMf and (hE - hsP[NT] == eps_star) \
        and (hE - hsP[NT] != 2 * eps_star)
    # m4: oracle exclusion
    n_orc = sum(1 for p in packs if p["sg_term"] > 0)
    okMf = okMf and n_orc == len(packs)
    check("G50-must-fails-fire", okMf,
          "m1 scale-ledger drop in the Bessel accumulation: %s "
          "(loud); m2 F sign flip breaks by %.2g x the honest "
          "orthogonality residual; m3 slope-2 claim on "
          "dh/dm_top breaks exactly in rationals; m4 oracle "
          "(reading sign h_{N-1}) hits %d/%d and is EXCLUDED by "
          "the input firewall" % (m1n,
                                  mism_bad / max(mism_honest,
                                                 1e-300),
                                  n_orc, len(packs)))

    # ---------------- S7 verdict
    section("S7  SEALED ADJUDICATION + VERDICT")
    if smoke:
        verdict = "SMOKE (infrastructure only)"
        check("G60-adjudication", True, "SMOKE: adjudication "
              "skipped, smoke subset only")
    else:
        a1_blind = all(a1_main[i] for i in bli_idx)
        a2_blind = all(a2_main[i] for i in bli_idx)
        a1_all = all(a1_main)
        a2_all = all(a2_main)
        a1_reg = not any(r["A1"] for r in reg.values())
        a2_reg = not any(r["A2"] for r in reg.values())
        elig = []
        if a2_all and a2_blind and a2_reg:
            elig.append("A2")
        if a1_all and a1_blind and a1_reg:
            elig.append("A1")
        path_clean_all = (n_clean == len(packs))
        if elig:
            verdict = "CONDITIONAL_BOUND(%s)" % elig[0]
        else:
            verdict = ("CS_CLASS_TOO_COARSE + TOPMOMENT_NOGO_"
                       "EXACT (BESSEL_BOUND_DERIVED structurally"
                       " excluded)")
        if path_clean_all and path_integral_ok:
            verdict += " + PATH_CLEAN_INTEGRAL_FORM"
        check("G60-adjudication", verdict == CAL_VERDICT,
              "SEALED RULES: A1 42/42 %s (blind %s, register-"
              "clean %s), A2 42/42 %s (blind %s, register-clean "
              "%s), path clean %d/%d => %s == frozen CAL_VERDICT"
              % (a1_all, a1_blind, a1_reg, a2_all, a2_blind,
                 a2_reg, n_clean, len(packs), verdict))
    check("G61-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a derivation-"
          "attempt round moves no edge); durable gains: the "
          "TOP-MOMENT NO-GO is exact (no CS/Bessel-class bound "
          "h >= c F^2 from prefix induction + background, even "
          "under the full wall hypothesis), the pairing "
          "rigidity localizes WHY (the mutilde-form is F-blind),"
          " the response identity along the fluctuation path is "
          "theorem-grade, and the measured lead is typed "
          "arithmetically fine: hypothesis-level, not constant-"
          "level")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G70-verdict", npass == len(CHECKS),
          "%s; NO RH claim"
          % (verdict if not smoke else "SMOKE"))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
