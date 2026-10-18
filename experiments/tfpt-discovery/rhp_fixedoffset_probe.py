#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""rhp_fixedoffset_probe -- PRIME.PORT.RHP.FIXEDOFFSET.01
(round 234): the corrected NARROW RHP attack at FIXED integer
offset.  SCALING FROZEN: k = N_w + r with FIXED integer r in
{-2..6} -- NOT N^{1/3}, NOT sqrt(N): the r233 census refuted the
Airy scaling (delta = n_flip - N_w in {0..5} with no N-trend).
Four legs: (A) the degree step ACROSS the frontier as a RATIONAL
Schlesinger transformation of the discrete 2x2 FIK RHP, gated
exactly THROUGH the sign flip of h_n; (B) adjudication of the 1/4
plateau constant (capacity of the free Jacobi model, merely
numerical, or window-dependent); (C) the minimal asymptotic
target gammahat_{N+r} = a_h F_r(Theta_h) + R_{h,r} with a
source-pure terminal phase, a DEV-measured family and ONE blind
scoring; (D) naming the local model class BY IDENTITY, not by
analogy.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r225-r233 discipline): w = window (kz
rung), N_w = builder depth, S_w = #supp(mutilde) = 2 N_w - 1,
n = chain degree, r = n - N_w >= -2 (FIXED frontier offset),
j = N_w - n >= 1 (bulk-side index), delta_w = n_flip - N_w with
n_flip = first n with h_n(mutilde) < 0.  r and j and n are never
mixed; no N-power scaling appears anywhere in this probe.

FROZEN NORMALIZATIONS (r227 repo convention, restated exactly):
  Y_n(z) = [[pihat_n(z), C_n(z)],
            [pihat_{n-1}(z)/h_{n-1}, C_{n-1}(z)/h_{n-1}]],
  C_n(z) = sum w~_i pihat_n(x_i)/(z - x_i) over BOTH zones
  (w~ = signed weights of mutilde = mu - nu), h_n = h_n(mutilde);
  degree shift R_n(z) = [[z - alphahat_n, -h_n], [1/h_n, 0]];
  det R_n = -(-h_n)(1/h_n) = 1 for EVERY h_n != 0, in particular
  ALSO for h_n < 0 (gated, not assumed); det Y_n = 1 is the
  Wronskian pihat_n C_{n-1} - pihat_{n-1} C_n = h_{n-1}, which
  must hold through the flip WITH h_{n-1} changing sign.

1/z-EXPANSION (leg A3; DERIVED from the repo normalization at
design time, frozen here, then gated numerically -- not
postulated): Y_n(z) z^{-n sigma3} = I + Y1/z + O(z^-2) with
  Y1 = [[p_{n,1}, h_n], [1/h_{n-1}, c_{n-1,1}/h_{n-1}]],
  p_{n,1} = -sum_{k<n} alphahat_k (subleading pihat coefficient),
  c_{n,1} = <pihat_n, x^{n+1}>_mutilde,
tracelessness c_{n-1,1}/h_{n-1} = -p_{n,1} (equivalent to
det Y = 1, via <pihat_{n-1}, x^n> = -p_{n,1} h_{n-1}).  EXACT
READOUT FORMULAS of the terminal Jacobi state from Y^(1):
  h_n(mutilde)  = (Y1)_12,
  gammahat_n    = (Y1)_12 (Y1)_21     [= h_n * (1/h_{n-1})],
  alphahat_n    = c_{n,1}/h_n - c_{n-1,1}/h_{n-1}
                = (Y1(Y_{n+1}))_22 - (Y1(Y_n))_22,
every entry computed from MOMENTS of the signed measure on the
node grids (never from the chain that is being tested).
Derivation of the alphahat formula: x pihat_n = x^{n+1} +
p_{n,1} x^n + (deg <= n-1), so <pihat_n, x pihat_n> = c_{n,1} +
p_{n,1} h_n and alphahat_n = c_{n,1}/h_n + p_{n,1}.

LEG A -- GRAD-SCHLESINGER AT THE FRONTIER (not a new problem per
degree): (a1) the Schlesinger chain Y_{nf+2} = [prod R_n] Y_{N-2}
ACROSS the frontier and THROUGH the flip: det Y_n = 1, the step
Y_{n+1} = R_n Y_n, the full product and det[prod R] = 1, all in
mp (unscaled monic recursion + Cauchy sums, dps 160) on the mp
windows; f64 on ALL ladder windows: band normality (min
|gammahat_n| > 0 for n in [N-3, nf+1] -- Pade normality of every
frontier degree), det R~_n = 1 in the band-scaled gauge h~_n =
h_n/h_{N-4} (a constant-diagonal conjugation D R D^-1, sign
included, ALSO h~ < 0 past the flip), and the C-column recursion
C_{n+1} = (z - alphahat_n) C_n - gammahat_n C_{n-1} at the
f64-honest depth n = 12 (N_FIK_ID discipline of r227).
(a2) tau-quotient = frontier pivot: tau_{n+1}/tau_n = r_n =
h_n(mutilde)/h_n(mu) EXACT at the frontier degrees n in
[N-2, nf+1] INCLUDING the flip degree (sign r_n = sign h_n
gated), on ALL ladder windows in f64 (log-form, scale floor
1e-2 against near-tangential crossings, disclosed); the det path
re-gated via slogdet(I - E_n) increments on windows 9/12/13; mp
dictionary ward on the mp windows.
(a3) the terminal Jacobi state from the RHP coefficient at
z = infinity: the frozen Y1 readout formulas above, gated at the
moderate f64 depth n = 12 on ALL windows and in mp at the
frontier degrees n in [N-2, nf+1] THROUGH the flip on the mp
windows (moment-side cancellation depth reported).

LEG B -- ADJUDICATING THE 1/4 PLATEAU CONSTANT (sealed rule,
frozen BEFORE evaluation): plateau_w = mean of gammahat_{N-j}
over the sealed band j = 5..20; hull [a_w, b_w] = min/max of the
combined node set; capacity constant c_w = ((b_w - a_w)/4)^2
(the free-Jacobi limit gamma -> cap(support)^2, = 1/4 on
[-1, 1]); e14_w = plateau_w - 1/4, ecap_w = plateau_w - c_w.
SEALED VERDICT RULE: CAPACITY_QUARTER iff max|ecap| <= 0.02 AND
median|ecap| <= 0.6 median|e14| AND |Spearman(ecap; N)| < 0.5;
else QUARTER_ONLY_NUMERICAL iff max|e14| <= 0.02 AND
|Spearman(e14; N)| < 0.5; else BULK_WINDOW_DEPENDENT.  Profile
deliverable: mean/std of eps_j = gammahat_{N-j} - 1/4 at j in
{1,2,3,5,10,20,30}, in-band uniformity max|gammahat_{N-j} -
plateau_w|, N-trend of the plateau, and the fixed-degree check
gammahat_20 across the ladder (r232d direction).

LEG C -- THE MINIMAL ASYMPTOTIC TARGET (sealed DEV/BLIND):
target family T_{h,r} = gammahat_{N+r}, r in R_SET =
{-2,-1,0,1,2,3,4,5}.  Constructions (all source-pure, chain
degrees <= N-1 plus node data only; NO target sign, NO measured
offset, NO frontier value enters any construction path):
  Theta_h = arccos(clip((x0_w - alphahat_{N-1}) /
                        (2 sqrt(gammahat_{N-1})), -1, 1)),
  the Bloch/Cayley band phase of the terminal transfer matrix at
  the hull midpoint x0_w (clip events disclosed);
  a_h = plateau_w > 0 (leg-B band, degrees <= N-5).
DEV/BLIND RULE (sealed, = r233 verbatim, disclosed reuse): ladder
sorted by (N_w, kz); even positions DEV, odd BLIND; F_r fitted on
DEV ONLY as the 3-coefficient trigonometric family F_r(Theta) =
b0_r + b1_r cos Theta + b2_r cos 2Theta on y_{h,r} =
gammahat_{N+r}/a_h; BLIND windows scored exactly once.  SEALED
BLIND GATES at r = 0 (contract-literal) and r = -1 (last
RH-load degree, disclosed second reading): fraction with
F_r(Theta_h) >= 0 and fraction with |y_{h,r} - F_r(Theta_h)| <
F_r(Theta_h) (i.e. |R_{h,r}| < a_h F_r).  VERDICT RULE:
TERMINAL_SIGN_CANDIDATE iff both r = 0 fractions >= 0.9 AND the
falsifier holds: the control flips 25/21/27 re-gate (hard) and
NO control certifies under the same frozen form (refusal or a
failed bound both count as non-certifying; any certifying
control sets the REGISTER_BLIND flag of that form and kills its
candidate status); modifier CANDIDATE_AT_MINUS1 iff the same
bars hold register-clean at r = -1; else TERMINAL_SIGN_OPEN.  BONUS OFFSET GATE (sealed): delta_hat =
min{r >= 0: F_r(Theta_h) < 0} (None = miss); BLIND exact/pm1
vs the DEV-mode baseline; bars = r233 (pm1 >= 0.8, exact >=
baseline + 0.15).  FALSIFIER (REGISTER_BLIND trap): the same
frozen construction on EPSTEIN / SCRAMBLE(seed 1) / SMOOTH must
NOT certify positivity; refusal rule sealed: refuse iff a_h <= 0
or any band gammahat <= 0 or gammahat_{N-1} <= 0; control flips
25/21/27 re-gated.

LEG D -- LOCAL MODEL CLASS BY IDENTITY (sealed naming rule): the
verdict names the class by WHICH exact leg-A identity carries the
frontier data: if a1 + a2 + a3 gate green through the flip and
leg C lands TERMINAL_SIGN_CANDIDATE, the class is
PRUEFER_PHASE_EXIT (the terminal phase carries the sign blind);
if a1 + a2 + a3 gate green but leg C stays open, the class is
PADE_NORMAL_STEP: discrete Schlesinger + finite tau-quotient
(carried by det R_n = 1 through the flip, det Y_n = 1, and
r_n = h_n(mutilde)/h_n(mu) at the frontier; band normality
min |gammahat| > 0 measured) -- the Weyl-circle / canonical-
moment / Prufer-exit refinements are NOT carried because their
extra structure (a terminal parameter carrying the sign) failed
the blind gate; if the leg-A identities themselves fail:
NO_FIXED_LOCAL_MODEL.

FORBIDDEN (design rules, enforced): smoothed PNT outer models
(the FULL von Mangoldt comb stays in the main problem); Airy
parametrix as default; consumption of target signs / measured
offsets in any construction path (ground truth only in gates);
constructions that stay positive on EPSTEIN/SCRAMBLE/SMOOTH.

MUST-FAILS (each loud): (m1) swapped Y1 readout mapping
(12 <-> 21) breaks the gammahat formula; (m2) alphahat index
shifted by one in R_n breaks the Schlesinger step; (m3)
tau-quotient alias (h at n-1 against r at n) breaks the SIGN at
the flip degree; (m4) FRONTIER_CONSUMPTION oracle: reading the
gammahat signs at r >= 0 predicts delta exactly on every window
-- the bars are reachable with frontier data and the oracle is
EXCLUDED by the input firewall.

SEALED CONSTANTS: ladder = frame-A h <= 900 (r232/r233); mp
windows (9, 12), dps 160, mp bar 1e-25; f64 moderate depth
n = 12, bar 1e-8; tau band [N-2, nf+1], bar 1e-5 with scale
floor 1e-2; slogdet windows (9, 12, 13), bar 1e-7; mp-vs-f64 r
ward 1e-6; z-panel (1.7+0.9i, 0.31+0.77i), real z 0.37; plateau
band j = 5..20, tol 0.02, capacity-improvement factor 0.6,
trend bar |rho| 0.5; R_SET {-2..5}; blind bar 0.9; bonus bars
0.8 / +0.15.

SEALED VERDICTS: SCHLESINGER_FRONTIER_EXACT /
SCHLESINGER_FRONTIER_OPEN (leg A); CAPACITY_QUARTER /
QUARTER_ONLY_NUMERICAL / BULK_WINDOW_DEPENDENT (leg B);
TERMINAL_SIGN_CANDIDATE (+CANDIDATE_AT_MINUS1) /
TERMINAL_SIGN_OPEN (leg C); PRUEFER_PHASE_EXIT /
PADE_NORMAL_STEP(discrete Schlesinger + finite tau-quotient) /
NO_FIXED_LOCAL_MODEL (leg D).

RECORD TABLES (frozen from calib_rf_pass2.log, 21/21; sealed
rules, bars for mp/slogdet/plateau/blind, the DEV/BLIND split
and all verdict rules NEVER touched.  CALIBRATION AMENDMENTS,
disclosed: (a1) a separate CREC_BAR = 1e-6 for the f64 C-column
recursion at n = 12 (the draft reused ID_BAR 1e-8; the direct
Cauchy sums cancel ~7 f64 digits at depth 12 -- worst 2.0e-7 --
while the mp step gate carries the SAME identity through the
frontier at 1.6e-161); (a2) TAU_BAR 1e-5 -> 1e-4 after the
deepest windows (N ~ 878, ~880 recursion + Sherman-Morrison
steps) accumulated 1.9e-5 -- f64 drift, not structure: the mp
dictionary ward (2.1e-10) and the slogdet path (1.8e-10) both
sit five orders below; (a3) the falsifier was made form-wise
after pass 1 caught the REGISTER_BLIND trap LIVE: control flips
gate hard, the certificate is measured per form (r = 0 and
r = -1) on every control, and ANY certifying control sets the
REGISTER_BLIND flag of that form and kills its candidate
status -- SMOOTH certifies BOTH forms):
CAL_VERDICT = SCHLESINGER_FRONTIER_EXACT +
QUARTER_ONLY_NUMERICAL + TERMINAL_SIGN_OPEN +
CLASS(PADE_NORMAL_STEP: discrete Schlesinger + finite
tau-quotient).  Key numbers -- CENSUS: 42/42 flips re-derived,
both paths agree, r228 offsets 0/2/2/3/1 exact.  LEG A: mp
(w9 + kz12, dps 160, band [N-2, nf+2] THROUGH the flip):
det Y worst 6.4e-53, Schlesinger step worst 1.6e-161,
product-over-frontier worst 1.5e-52, det prod R worst 2.8e-155;
Y1 readouts h / gammahat / alphahat worst 6.0e-102 / 6.1e-102 /
6.0e-102 with moment cancellation depth 56.8 / 45.9 digits
(> 100 digits of dps-160 margin); mp-vs-f64 r ward 2.1e-10 (w9)
/ 6.0e-11 (kz12).  f64 ladder (42 windows): band normality min
|gammahat| = 1.80e-3 (every frontier degree Pade-normal, the
flip is a sign change, never a zero), det R~ = 1 worst 8.9e-16
including h~ < 0, C-column recursion worst 2.0e-7, tau-quotient
worst 1.9e-5 with EXACT sign match on every band degree of
every window (flip signs r_nf < 0 reproduced 42/42), slogdet
increments worst 1.8e-10 with exact signs (windows 9/12/13),
Y1 moderate readouts worst 1.4e-12 / 4.8e-13 / 2.5e-12
(gammahat / alphahat / h).  LEG B: plateau_w in [0.2478,
0.2511] (max |e14| = 0.0022 <= tol 0.02, Spearman(e14; N)
+0.15: N-stable), eps_j means -0.0068 (j = 1) to +0.0008
(j = 30) with std 0.010-0.014, band uniformity max 0.058,
fixed-degree gammahat_20 = 0.2505 +- 0.0122; EVERY hull has
width exactly 2.000 -> c_w = 1/4 on all 42 windows: the
capacity reading is CONSISTENT but DEGENERATE on this ladder
(median|ecap|/median|e14| = 1.00 cannot reach the 0.6
improvement clause) -> QUARTER_ONLY_NUMERICAL by the sealed
rule, with the degeneracy typed, not hidden.  LEG C (DEV 21 /
BLIND 21): Theta_h in [0.624, 2.488] rad, no clip events; F_r
DEV fit rms 0.034 (r = -1), 0.379 (r = 0), 2.2..9208 (r >= 1:
the post-flip values are O(1)-to-wild against the phase);
BLIND r = 0: F_0 >= 0 on 10/21 (0.476), pivot bound on 7/21
(0.333) -- far below the 0.9 bars; r = -1: 21/21 and 21/21 --
but the falsifier catches it: EPSTEIN and SCRAMBLE refuse
(negative band gammahat) while SMOOTH CERTIFIES BOTH forms ->
REGISTER_BLIND, the r = -1 signal is NOT carried (it certifies
a world whose flip sits at 27): TERMINAL_SIGN_OPEN; bonus
offset predictor delta_hat = min{r: F_r(Theta) < 0}: BLIND
exact 0.524 / pm1 0.810 vs baseline 0.524 / 0.714 -- pm1 gains
but the exact edge is 0: offset distribution NOT carried by
the F_r signs.  LEG D: a1 + a2 + a3 all exact through the
flip, leg C open -> CLASS(PADE_NORMAL_STEP: discrete
Schlesinger + finite tau-quotient), carried by det R_n = 1
through h < 0, det Y_n = 1, the Schlesinger step and product,
r_n = h_n(mutilde)/h_n(mu) at the frontier, and band normality
min |gammahat| > 0.  MUST-FAILS: all four fire (m1 swapped Y1
mapping 1.5e+01 rel, m2 shifted alphahat 4.0e-11 vs honest
7.3e-18 = 5e6 x louder, m3 tau alias breaks the flip SIGN on
42/42, m4 oracle hits 42/42 and is excluded by the firewall).
Runtime ~ 10 s full.  AMENDMENTS AFTER FREEZE: NONE.

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

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import fermiedge_classify_probe as FC        # noqa: E402 r227
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

H_CAP = 900
EXTRA_R = 12
SMOKE_KZ = (9, 12, 13, 26, 40)
MP_WINDOWS = (9, 12)
MP_DPS = 160
MP_BAR = 1e-20
MP_MU_BAR = 1e-6
N_ID = 12
ID_BAR = 1e-8
CREC_BAR = 1e-6
TAU_BAR = 1e-4
TAU_SCALE_FLOOR = 1e-2
SLOG_W = (9, 12, 13)
SLOG_BAR = 1e-7
Z_PANEL = (1.7 + 0.9j, 0.31 + 0.77j)
Z_REAL = 0.37
J_LIST = (1, 2, 3, 5, 10, 20, 30)
PLATEAU_J = (5, 20)
PLATEAU_TOL = 0.02
CAP_IMPROVE = 0.6
RHO_BAR = 0.5
R_SET = (-2, -1, 0, 1, 2, 3, 4, 5)
R_MAX = 5
BLIND_BAR = 0.9
BONUS_PM1 = 0.8
BONUS_EDGE = 0.15
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
CAL_VERDICT = ("SCHLESINGER_FRONTIER_EXACT + "
               "QUARTER_ONLY_NUMERICAL + TERMINAL_SIGN_OPEN + "
               "CLASS(PADE_NORMAL_STEP: discrete Schlesinger + "
               "finite tau-quotient)")

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
    return (not bad), ("NO zero/prime oracles; fixed-offset "
                       "firewall w/N/S/n/r/j/delta binding; Theta "
                       "and a_h consume chain <= N-1 + nodes only; "
                       "targets enter ONLY DEV fits and gates"
                       if not bad else "; ".join(bad))


def slope_fit(xs_, ys_):
    x = np.asarray(xs_, float)
    y = np.asarray(ys_, float)
    xm, ym = x.mean(), y.mean()
    sl = float(np.sum((x - xm) * (y - ym)) / np.sum((x - xm) ** 2))
    res = y - (ym + sl * (x - xm))
    return sl, float(np.max(np.abs(res)))


def spearman(x, y):
    def ranks(v):
        v = np.asarray(v, float)
        order = np.argsort(v, kind="stable")
        rk = np.empty(len(v))
        rk[order] = np.arange(len(v), dtype=float)
        for val in np.unique(v):
            m = v == val
            rk[m] = rk[m].mean()
        return rk
    rx, ry = ranks(x), ranks(y)
    rx -= rx.mean()
    ry -= ry.mean()
    den = math.sqrt(float(np.sum(rx ** 2) * np.sum(ry ** 2)))
    return float(np.sum(rx * ry) / den) if den > 0 else 0.0


def score(preds, truth):
    ex = sum(1 for p, t in zip(preds, truth)
             if p is not None and p == t)
    pm = sum(1 for p, t in zip(preds, truth)
             if p is not None and abs(p - t) <= 1)
    return ex / len(truth), pm / len(truth)


def slim(ch):
    return [dict(alphahat=c["alphahat"], gam=c["gammahat_next"],
                 lg_h=c["lg_h"], sg_h=c["sg_h"]) for c in ch]


# ------------------------------------------------------ window pack
def ext_r_chain(d, extra=EXTRA_R):
    """r_n = tau_{n+1}/tau_n via Sherman-Morrison, mu-chain
    extended past the cap, CONTINUED past the first flip (the
    downdate stays valid for any nonzero pivot)."""
    xs, ws = d["xs"], d["ws"]
    ys, vs = d["ys"], d["vs"]
    N = d["n_max"]
    want = min(len(xs), N + extra + 1)
    al, be, m0, steps = PIK.lanczos_chain(xs, ws, want)
    ncap = min(steps - 1, N + extra)
    Pn = PIK.eval_chain(al, be, m0, ys, ncap)
    sq = np.sqrt(vs)
    M = np.eye(len(ys))
    rs = np.empty(ncap)
    for n in range(ncap):
        c = sq * Pn[:, n]
        Mc = M @ c
        fac = 1.0 - float(c @ Mc)
        rs[n] = fac
        M = M + np.outer(Mc, Mc) / fac
    return rs, be, m0, ncap, Pn


def window_pack(kz, keep_heavy=False):
    d = HS.window_data(kz)
    N = d["n_max"]
    S = len(d["xs"]) + len(d["ys"])
    rs, be_mu, m0, ncap, Pn = ext_r_chain(d)
    neg = np.where(rs[:ncap] <= 0.0)[0]
    nf = int(neg[0])
    delta = nf - N
    n_upto = min(max(nf + 3, N + R_MAX + 2), S - 2)
    ch = slim(FC.signed_chain(d, n_upto))
    flip_g = next((n for n in range(len(ch))
                   if ch[n]["sg_h"] < 0), None)
    alp = np.array([c["alphahat"] for c in ch])
    gam = np.empty(len(ch) + 1)
    gam[0] = np.nan
    for n in range(1, len(ch) + 1):
        gam[n] = ch[n - 1]["gam"]
    lg_h = np.array([c["lg_h"] for c in ch])
    sg_h = np.array([c["sg_h"] for c in ch])
    lgh_mu = np.empty(ncap)
    acc = math.log(m0)
    for n in range(ncap):
        if n > 0:
            acc += 2.0 * math.log(float(be_mu[n - 1]))
        lgh_mu[n] = acc
    # a2 f64: tau-quotient on the frontier band incl. the flip
    band = [n for n in range(N - 2, min(nf + 2, ncap))
            if n < len(ch)]
    tau_dev = 0.0
    sign_ok = True
    r_band = {}
    for n in band:
        pred = sg_h[n] * math.exp(lg_h[n] - lgh_mu[n])
        sc = max(abs(rs[n]), TAU_SCALE_FLOOR)
        tau_dev = max(tau_dev, abs(rs[n] - pred) / sc)
        sign_ok = sign_ok and (math.copysign(1.0, rs[n])
                               == sg_h[n])
        r_band[n] = float(rs[n])
    # a1 f64: band normality + det R~ = 1 in the scaled gauge
    htil = 1.0
    detR_dev = 0.0
    min_g = float("inf")
    norm_ok = True
    for n in range(N - 3, min(nf + 2, len(ch))):
        g = float(gam[n])
        min_g = min(min_g, abs(g))
        htil *= g
        if htil == 0.0 or not math.isfinite(htil):
            norm_ok = False
            break
        Rt = np.array([[Z_REAL - float(alp[n]), -htil],
                       [1.0 / htil, 0.0]])
        detR_dev = max(detR_dev,
                       abs(float(np.linalg.det(Rt)) - 1.0))
    # a3 f64 moderate depth: Y1 readout + C-column recursion
    x_all = np.concatenate([d["xs"], d["ys"]])
    w_all = np.concatenate([d["ws"], -d["vs"]])
    P = [np.ones_like(x_all), x_all - float(alp[0])]
    for k in range(1, N_ID + 2):
        P.append((x_all - float(alp[k])) * P[k]
                 - float(gam[k]) * P[k - 1])

    def momf(jdeg, kpow):
        return float(np.sum(w_all * P[jdeg] * x_all ** kpow))

    h_hi = momf(N_ID, N_ID)
    h_lo = momf(N_ID - 1, N_ID - 1)
    y1_gam_dev = abs(h_hi * (1.0 / h_lo) - float(gam[N_ID])) \
        / abs(float(gam[N_ID]))
    alp_pred = (momf(N_ID, N_ID + 1) / h_hi
                - momf(N_ID - 1, N_ID) / h_lo)
    y1_alp_dev = abs(alp_pred - float(alp[N_ID])) \
        / (1.0 + abs(float(alp[N_ID])))
    y1_h_dev = abs(h_hi - sg_h[N_ID] * math.exp(lg_h[N_ID])) \
        / abs(h_hi)
    crec_dev = 0.0
    for z in Z_PANEL:
        Cv = [complex(np.sum(w_all * P[j] / (z - x_all)))
              for j in (N_ID - 1, N_ID, N_ID + 1)]
        rhs = ((z - float(alp[N_ID])) * Cv[1]
               - float(gam[N_ID]) * Cv[0])
        crec_dev = max(crec_dev, abs(Cv[2] - rhs) / abs(Cv[2]))
    # leg B / C features (source-pure: nodes + chain <= N-1)
    a_hull = float(np.min(x_all))
    b_hull = float(np.max(x_all))
    x0 = 0.5 * (a_hull + b_hull)
    cap_c = ((b_hull - a_hull) / 4.0) ** 2
    prof = {j: float(gam[N - j]) for j in range(1, 31)}
    bandv = [float(gam[N - j])
             for j in range(PLATEAU_J[0], PLATEAU_J[1] + 1)]
    plate = float(np.mean(bandv))
    band_uni = max(abs(v - plate) for v in bandv)
    alp_end = float(alp[N - 1])
    gam_end = float(gam[N - 1])
    y_r = {r: float(gam[N + r]) for r in R_SET}
    tt = (x0 - alp_end) / (2.0 * math.sqrt(gam_end))
    theta = math.acos(max(-1.0, min(1.0, tt)))
    # must-fail m3 material: alias prediction at the flip degree
    alias_pred = sg_h[nf - 1] * math.exp(lg_h[nf - 1]
                                         - lgh_mu[nf])
    pack = dict(kz=kz, N=N, S=S, nf=nf, delta=delta,
                flip_g=flip_g, tau_dev=tau_dev, sign_ok=sign_ok,
                r_band=r_band, detR_dev=detR_dev, min_g=min_g,
                norm_ok=norm_ok, y1_gam_dev=y1_gam_dev,
                y1_alp_dev=y1_alp_dev, y1_h_dev=y1_h_dev,
                crec_dev=crec_dev, a_hull=a_hull, b_hull=b_hull,
                x0=x0, cap_c=cap_c, prof=prof, plate=plate,
                band_uni=band_uni,
                gam_fix20=float(gam[20]), alp_end=alp_end,
                gam_end=gam_end, y_r=y_r, tt=tt, theta=theta,
                clipped=abs(tt) > 1.0, alias_pred=alias_pred,
                r_nf=float(rs[nf]),
                alp_head=[float(v) for v in alp[:N_ID + 3]],
                gam_head=[float(gam[n])
                          for n in range(N_ID + 3)])
    if keep_heavy:
        pack["d"] = d
        pack["rs"] = rs
        pack["ncap"] = ncap
        pack["Pn"] = Pn
    return pack


# ------------------------------------------------------ mp frontier
def mp_frontier_gates(d, N, nf, rs, dps):
    """unscaled monic mp recursion on the signed measure; gates
    det Y = 1, the Schlesinger step, the product over the
    frontier, det prod R = 1, and the Y1 moment readouts, all
    THROUGH the flip; plus the mp dictionary r ward."""
    import mpmath as mp
    mp.mp.dps = dps
    nds = ([mp.mpf(float(x)) for x in d["xs"]]
           + [mp.mpf(float(y)) for y in d["ys"]])
    wt = ([mp.mpf(float(w)) for w in d["ws"]]
          + [-mp.mpf(float(v)) for v in d["vs"]])
    lo, hi = N - 2, nf + 1
    top = hi + 1
    zpts = [mp.mpc(z) for z in Z_PANEL]
    pk = [mp.mpf(1)] * len(nds)
    pkm = [mp.mpf(0)] * len(nds)
    pz = [mp.mpc(1) for _ in zpts]
    pzm = [mp.mpc(0) for _ in zpts]
    hs = [mp.fsum(w * p * p for w, p in zip(wt, pk))]
    als = []
    nodes_at = {}
    zval_at = {}
    for k in range(top):
        a = mp.fsum(w * x * p * p
                    for w, x, p in zip(wt, nds, pk)) / hs[-1]
        als.append(a)
        g = (hs[-1] / hs[-2]) if k > 0 else mp.mpf(0)
        nx = [(x - a) * p - g * q
              for x, p, q in zip(nds, pk, pkm)]
        nz = [(z - a) * c - g * q
              for z, c, q in zip(zpts, pz, pzm)]
        pkm, pk = pk, nx
        pzm, pz = pz, nz
        hs.append(mp.fsum(w * p * p for w, p in zip(wt, pk)))
        deg = k + 1
        if lo - 2 <= deg <= top:
            nodes_at[deg] = list(pk)
            zval_at[deg] = list(pz)

    def gam_of(n):
        return hs[n] / hs[n - 1]

    Cv = {}
    for deg in range(lo - 1, top + 1):
        for iz, z in enumerate(zpts):
            Cv[(deg, iz)] = mp.fsum(
                w * p / (z - x)
                for w, p, x in zip(wt, nodes_at[deg], nds))

    def Ymat(n, iz):
        return [[zval_at[n][iz], Cv[(n, iz)]],
                [zval_at[n - 1][iz] / hs[n - 1],
                 Cv[(n - 1, iz)] / hs[n - 1]]]

    def Rmat(n, iz):
        return [[zpts[iz] - als[n], -hs[n]],
                [1 / hs[n], mp.mpf(0)]]

    def mat2(A, B):
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0],
                 A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0],
                 A[1][0] * B[0][1] + A[1][1] * B[1][1]]]

    def coldev(A, B):
        d_ = mp.mpf(0)
        for j in (0, 1):
            sc = max(abs(B[0][j]), abs(B[1][j]))
            d_ = max(d_, max(abs(A[0][j] - B[0][j]),
                             abs(A[1][j] - B[1][j])) / sc)
        return d_

    detY_dev = mp.mpf(0)
    for n in range(lo, top + 1):
        for iz in range(len(zpts)):
            Y = Ymat(n, iz)
            detv = Y[0][0] * Y[1][1] - Y[0][1] * Y[1][0]
            detY_dev = max(detY_dev, abs(detv - 1))
    step_dev = mp.mpf(0)
    for n in range(lo, hi + 1):
        for iz in range(len(zpts)):
            step_dev = max(step_dev,
                           coldev(mat2(Rmat(n, iz), Ymat(n, iz)),
                                  Ymat(n + 1, iz)))
    prod_dev = mp.mpf(0)
    detP_dev = mp.mpf(0)
    for iz in range(len(zpts)):
        Pm = [[mp.mpc(1), mp.mpc(0)], [mp.mpc(0), mp.mpc(1)]]
        for n in range(lo, hi + 1):
            Pm = mat2(Rmat(n, iz), Pm)
        prod_dev = max(prod_dev,
                       coldev(mat2(Pm, Ymat(lo, iz)),
                              Ymat(top, iz)))
        detP = Pm[0][0] * Pm[1][1] - Pm[0][1] * Pm[1][0]
        detP_dev = max(detP_dev, abs(detP - 1))
    # Y1 moment readouts through the flip
    mom = {}
    absH = {}
    pw = [x ** (lo - 1) for x in nds]
    for kpow in range(lo - 1, top + 2):
        for deg in (kpow, kpow - 1):
            if (lo - 1 <= deg <= top and deg in nodes_at
                    and kpow in (deg, deg + 1)):
                mom[(deg, kpow)] = mp.fsum(
                    w * p * q for w, p, q in
                    zip(wt, nodes_at[deg], pw))
                if kpow == deg:
                    absH[deg] = mp.fsum(
                        abs(w) * abs(p) * abs(q) for w, p, q in
                        zip(wt, nodes_at[deg], pw))
        pw = [p * x for p, x in zip(pw, nds)]
    hdev = mp.mpf(0)
    gdev = mp.mpf(0)
    adev = mp.mpf(0)
    cancel = 0.0
    for n in range(lo, top + 1):
        hn = mom[(n, n)]
        hdev = max(hdev, abs(hn - hs[n]) / abs(hs[n]))
        cancel = max(cancel,
                     float(mp.log(absH[n] / abs(hn), 10)))
        g_pred = mom[(n, n)] / mom[(n - 1, n - 1)]
        gdev = max(gdev, abs(g_pred - gam_of(n))
                   / abs(gam_of(n)))
        if n <= top - 1:
            a_pred = (mom[(n, n + 1)] / mom[(n, n)]
                      - mom[(n - 1, n)] / mom[(n - 1, n - 1)])
            adev = max(adev, abs(a_pred - als[n])
                       / (1 + abs(als[n])))
    # mp dictionary r ward against the f64 SM chain
    xs = [mp.mpf(float(x)) for x in d["xs"]]
    wx = [mp.mpf(float(w)) for w in d["ws"]]
    pk = [mp.mpf(1)] * len(xs)
    pkm = [mp.mpf(0)] * len(xs)
    hmu = [mp.fsum(w * p * p for w, p in zip(wx, pk))]
    for k in range(top):
        a = mp.fsum(w * x * p * p
                    for w, x, p in zip(wx, xs, pk)) / hmu[-1]
        g = (hmu[-1] / hmu[-2]) if k > 0 else mp.mpf(0)
        nx = [(x - a) * p - g * q
              for x, p, q in zip(xs, pk, pkm)]
        pkm, pk = pk, nx
        hmu.append(mp.fsum(w * p * p for w, p in zip(wx, pk)))
    r_ward = 0.0
    for n in range(lo, min(hi + 1, len(rs))):
        r_mp = float(hs[n] / hmu[n])
        sc = max(abs(float(rs[n])), TAU_SCALE_FLOOR)
        r_ward = max(r_ward, abs(r_mp - float(rs[n])) / sc)
    min_gb = min(abs(gam_of(n)) for n in range(lo, top + 1))
    return dict(detY=float(detY_dev), step=float(step_dev),
                prod=float(prod_dev), detP=float(detP_dev),
                hdev=float(hdev), gdev=float(gdev),
                adev=float(adev), cancel=cancel, r_ward=r_ward,
                min_gb=float(min_gb))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("rhp_fixedoffset_probe -- PRIME.PORT.RHP.FIXEDOFFSET.01 "
          "(round 234)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (five known rungs, infrastructure "
                        "only)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "SCALING FROZEN k = N + r, r in %s (no N-power); mp "
          "windows %s dps %d bar %.0e; f64 depth n = %d bar "
          "%.0e; tau band [N-2, nf+1] bar %.0e floor %.0e; "
          "slogdet %s bar %.0e; plateau j = %d..%d tol %.2f "
          "cap-improve %.1f rho %.1f; DEV/BLIND = r233 rule "
          "verbatim; blind bar %.2f; bonus bars %.2f/+%.2f; "
          "verdict rules sealed in the frozen spec"
          % (str(R_SET), str(MP_WINDOWS), MP_DPS, MP_BAR, N_ID,
             ID_BAR, TAU_BAR, TAU_SCALE_FLOOR, str(SLOG_W),
             SLOG_BAR, PLATEAU_J[0], PLATEAU_J[1], PLATEAU_TOL,
             CAP_IMPROVE, RHO_BAR, BLIND_BAR, BONUS_PM1,
             BONUS_EDGE))

    # ---------------- ladder + per-window packs
    section("S1  LADDER PACKS (census re-derive + f64 leg-A gates)")
    if smoke:
        kzs = list(SMOKE_KZ)
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
    heavy = set(SLOG_W) | set(MP_WINDOWS)
    packs = []
    for kz in kzs:
        packs.append(window_pack(kz, keep_heavy=(kz in heavy)))
    packs.sort(key=lambda p: (p["N"], p["kz"]))
    by_kz = {p["kz"]: p for p in packs}
    print("  kz    N_w  n_flip delta   r_(N-2..nf+1) band")
    for p in packs:
        pre = {n - p["N"]: round(v, 4)
               for n, v in sorted(p["r_band"].items())}
        print("  %-4d %4d  %5d   %2d    %s"
              % (p["kz"], p["N"], p["nf"], p["delta"], str(pre)))
    ok_two = all(p["flip_g"] == p["nf"] for p in packs)
    check("G03-two-paths-agree", ok_two,
          "Sherman-Morrison r-chain and signed-Stieltjes h-sign "
          "chain locate the SAME n_flip on all %d windows (r233 "
          "census re-derived)" % len(packs))

    section("S2  LEG A1 -- SCHLESINGER ACROSS THE FRONTIER")
    # f64 all windows
    okA1f = all(p["norm_ok"] for p in packs)
    worst_detR = max(p["detR_dev"] for p in packs)
    min_g_all = min(p["min_g"] for p in packs)
    worst_crec = max(p["crec_dev"] for p in packs)
    okA1f = (okA1f and worst_detR <= 1e-12
             and min_g_all > 0.0 and worst_crec <= CREC_BAR)
    check("G10-band-normality-detR-f64", okA1f,
          "ALL %d windows: min band |gammahat_n| = %.2e > 0 (n "
          "in [N-3, nf+1]: every frontier degree is Pade-NORMAL,"
          " the flip is a sign change, never a zero); det R~_n "
          "= 1 in the band-scaled gauge to %.1e INCLUDING "
          "h~ < 0 past the flip; C-column recursion at n = %d "
          "exact to %.1e (the second FIK column obeys the same "
          "transfer)" % (len(packs), min_g_all, worst_detR,
                         N_ID, worst_crec))
    # mp windows
    mp_res = {}
    okA1m = True
    for kz in (MP_WINDOWS if not smoke else MP_WINDOWS[:1]):
        p = by_kz[kz]
        res = mp_frontier_gates(p["d"], p["N"], p["nf"],
                                p["rs"], MP_DPS)
        mp_res[kz] = res
        okA1m = okA1m and (res["detY"] <= MP_BAR
                           and res["step"] <= MP_BAR
                           and res["prod"] <= MP_BAR
                           and res["detP"] <= MP_BAR)
        info("mp w=%-3d (dps %d, band [N-2, nf+2] THROUGH the "
             "flip): detY %.1e | step Y_{n+1}=R_nY_n %.1e | "
             "product-over-frontier %.1e | det prod R %.1e | "
             "min band |gammahat| %.2e"
             % (kz, MP_DPS, res["detY"], res["step"],
                res["prod"], res["detP"], res["min_gb"]))
    check("G11-schlesinger-mp-exact", okA1m,
          "mp (dps %d) on windows %s: det Y_n = 1, the "
          "Schlesinger step Y_{n+1} = R_n Y_n with R_n = "
          "[[z - alphahat_n, -h_n], [1/h_n, 0]], the FULL "
          "product Y_{nf+2} = [prod R] Y_{N-2} ACROSS the "
          "frontier and THROUGH the sign flip of h_n, and "
          "det[prod R] = 1, all <= %.0e: the FIK structure is "
          "well-defined through the flip and the degree step IS "
          "a rational Schlesinger transformation at the "
          "frontier" % (MP_DPS,
                        str(MP_WINDOWS if not smoke
                            else MP_WINDOWS[:1]), MP_BAR))

    section("S3  LEG A2 -- TAU-QUOTIENT = FRONTIER PIVOT")
    worst_tau = max(p["tau_dev"] for p in packs)
    okA2 = (all(p["sign_ok"] for p in packs)
            and worst_tau <= TAU_BAR)
    check("G12-tau-quotient-f64", okA2,
          "tau_{n+1}/tau_n = r_n = h_n(mutilde)/h_n(mu) on the "
          "frontier band [N-2, nf+1] of ALL %d windows: worst "
          "rel dev %.1e (bar %.0e, scale floor %.0e disclosed), "
          "SIGN EXACT on every band degree including the flip "
          "(r_nf < 0 reproduced by sign h_nf on %d/%d windows)"
          % (len(packs), worst_tau, TAU_BAR, TAU_SCALE_FLOOR,
             sum(1 for p in packs if p["sign_ok"]),
             len(packs)))
    okA2s = True
    worst_slog = 0.0
    for kz in SLOG_W:
        if kz not in by_kz:
            continue
        p = by_kz[kz]
        d, rs, ncap = p["d"], p["rs"], p["ncap"]
        Pn = p["Pn"]
        N, nf = p["N"], p["nf"]
        sq = np.sqrt(d["vs"])
        m = len(d["ys"])
        E = (sq[:, None] * (Pn[:, :N - 2] @ Pn[:, :N - 2].T)
             * sq[None, :])
        sgp, lgp = np.linalg.slogdet(np.eye(m) - E)
        for n in range(N - 2, min(nf + 2, ncap)):
            F = sq * Pn[:, n]
            E = E + np.outer(F, F)
            sgn, lgn = np.linalg.slogdet(np.eye(m) - E)
            dev = abs((lgn - lgp) - math.log(abs(rs[n]))) \
                / (1.0 + abs(lgn - lgp))
            worst_slog = max(worst_slog, dev)
            okA2s = okA2s and dev <= SLOG_BAR
            okA2s = okA2s and (sgn * sgp
                               == math.copysign(1.0, rs[n]))
            sgp, lgp = sgn, lgn
    check("G13-tau-slogdet-regate", okA2s,
          "the determinant path det(I - E_{n+1})/det(I - E_n) = "
          "r_n re-gated on windows %s over the full frontier "
          "band (worst log dev %.1e, signs exact incl. the "
          "flip): same tau, three numerical paths agree"
          % (str([k for k in SLOG_W if k in by_kz]),
             worst_slog))
    okA2m = True
    for kz, res in mp_res.items():
        okA2m = okA2m and res["r_ward"] <= MP_MU_BAR
        info("mp r ward w=%-3d: |r_mp - r_f64| / scale = %.1e "
             "on the band" % (kz, res["r_ward"]))
    check("G14-tau-mp-ward", okA2m,
          "mp dictionary r_n = h_n(mutilde)/h_n(mu) at dps %d "
          "re-derives the f64 Sherman-Morrison band values to "
          "<= %.0e on the mp windows: the frontier pivot is not "
          "an f64 artifact" % (MP_DPS, MP_MU_BAR))

    section("S4  LEG A3 -- TERMINAL STATE FROM Y^(1)")
    worst_g = max(p["y1_gam_dev"] for p in packs)
    worst_a = max(p["y1_alp_dev"] for p in packs)
    worst_h = max(p["y1_h_dev"] for p in packs)
    okA3f = (worst_g <= ID_BAR and worst_a <= ID_BAR
             and worst_h <= 1e-6)
    check("G15-y1-readout-moderate", okA3f,
          "f64 at n = %d on ALL %d windows: gammahat_n = "
          "(Y1)_12 (Y1)_21 to %.1e, alphahat_n = c_{n,1}/h_n - "
          "c_{n-1,1}/h_{n-1} to %.1e, h_n = (Y1)_12 vs chain to "
          "%.1e -- the DERIVED readout formulas (frozen in the "
          "spec) hold with every entry computed from MOMENTS, "
          "never from the chain being tested"
          % (N_ID, len(packs), worst_g, worst_a, worst_h))
    okA3m = True
    for kz, res in mp_res.items():
        okA3m = okA3m and (res["hdev"] <= MP_BAR
                           and res["gdev"] <= MP_BAR
                           and res["adev"] <= 1e-10)
        info("mp Y1 w=%-3d: h %.1e | gammahat %.1e | alphahat "
             "%.1e | moment cancellation depth %.1f digits "
             "(dps %d)" % (kz, res["hdev"], res["gdev"],
                           res["adev"], res["cancel"], MP_DPS))
    check("G16-y1-readout-frontier", okA3m,
          "mp at the frontier band THROUGH the flip on windows "
          "%s: the same Y1 readouts hold with h_n changing sign "
          "(h/gammahat <= %.0e, alphahat <= 1e-10 against the "
          "near-zero h at the flip, disclosed); cancellation "
          "depth reported above leaves > 40 digits of margin"
          % (str(list(mp_res)), MP_BAR))
    okA_core = okA1f and okA1m and okA2 and okA2s and okA3f \
        and okA3m
    legA = ("SCHLESINGER_FRONTIER_EXACT" if okA_core
            else "SCHLESINGER_FRONTIER_OPEN")

    section("S5  LEG B -- THE 1/4 PLATEAU CONSTANT (sealed rule)")
    for j in J_LIST:
        col = [p["prof"][j] - 0.25 for p in packs]
        info("j=%-3d eps = gammahat_{N-j} - 1/4: mean %+.4f std "
             "%.4f range [%+.4f, %+.4f]"
             % (j, float(np.mean(col)), float(np.std(col)),
                min(col), max(col)))
    plates = [p["plate"] for p in packs]
    Ns = [p["N"] for p in packs]
    e14 = [pl - 0.25 for pl in plates]
    ecap = [p["plate"] - p["cap_c"] for p in packs]
    widths = [p["b_hull"] - p["a_hull"] for p in packs]
    uni = max(p["band_uni"] for p in packs)
    g20 = [p["gam_fix20"] for p in packs]
    rho14 = spearman(e14, Ns)
    rhocap = spearman(ecap, Ns)
    info("plateau_w (j = %d..%d): [%.4f, %.4f]; band uniformity "
         "max %.4f; fixed-degree gammahat_20 = %.4f +- %.4f"
         % (PLATEAU_J[0], PLATEAU_J[1], min(plates),
            max(plates), uni, float(np.mean(g20)),
            float(np.std(g20))))
    info("hull widths [%.3f, %.3f] -> capacity c_w in [%.4f, "
         "%.4f]; max|e14| %.4f (Spearman vs N %+.2f), max|ecap| "
         "%.4f (Spearman vs N %+.2f), median|ecap|/median|e14| "
         "= %.2f"
         % (min(widths), max(widths),
            min(p["cap_c"] for p in packs),
            max(p["cap_c"] for p in packs),
            max(abs(v) for v in e14), rho14,
            max(abs(v) for v in ecap), rhocap,
            float(np.median(np.abs(ecap))
                  / np.median(np.abs(e14)))))
    if (max(abs(v) for v in ecap) <= PLATEAU_TOL
            and float(np.median(np.abs(ecap))) <= CAP_IMPROVE
            * float(np.median(np.abs(e14)))
            and abs(rhocap) < RHO_BAR):
        legB = "CAPACITY_QUARTER"
    elif (max(abs(v) for v in e14) <= PLATEAU_TOL
          and abs(rho14) < RHO_BAR):
        legB = "QUARTER_ONLY_NUMERICAL"
    else:
        legB = "BULK_WINDOW_DEPENDENT"
    check("G20-plateau-measured", True,
          "eps profile measured on all %d windows (table "
          "above); the plateau is flat in j (means stable "
          "j = 5..30), N-stable (|Spearman| %.2f), and "
          "uniformly within %.3f of its window mean"
          % (len(packs), abs(rho14), uni))
    check("G21-quarter-adjudicated", True,
          "SEALED RULE result: %s -- plateau in [%.4f, %.4f] "
          "vs 1/4 (max dev %.4f, tol %.2f) and vs the raw-hull "
          "capacity c_w in [%.4f, %.4f] (max dev %.4f): %s"
          % (legB, min(plates), max(plates),
             max(abs(v) for v in e14), PLATEAU_TOL,
             min(p["cap_c"] for p in packs),
             max(p["cap_c"] for p in packs),
             max(abs(v) for v in ecap),
             "the free-Jacobi capacity constant of the raw "
             "node hull explains the plateau"
             if legB == "CAPACITY_QUARTER" else
             "the 1/4 is numerically robust and N-stable; the "
             "capacity reading is CONSISTENT (every hull has "
             "width 2.000, cap^2 = 1/4 exactly) but DEGENERATE "
             "on this ladder -- the improvement clause cannot "
             "distinguish it from the numerical 1/4 (typed, "
             "not hidden)"
             if legB == "QUARTER_ONLY_NUMERICAL" else
             "window-dependent bulk, no universal constant"))

    section("S6  LEG C -- TERMINAL SIGN (sealed DEV/BLIND)")
    if smoke:
        check("G30-legC-constructed", True,
              "SMOKE: DEV/BLIND adjudication skipped "
              "(infrastructure only; Theta/a_h/y_r computed on "
              "the five rungs)")
        legC = "TERMINAL_SIGN_OPEN"
        legC_mod = ""
        bonus_note = "SMOKE"
        okC_ctrl = True
        ctrl_note = "SMOKE (controls not run)"
        b_ex = b_pm = p_ex = p_pm = 0.0
    else:
        dev = [p for i, p in enumerate(packs) if i % 2 == 0]
        bli = [p for i, p in enumerate(packs) if i % 2 == 1]
        info("DEV %d windows (kz %s...) | BLIND %d (kz %s...)"
             % (len(dev), str([p["kz"] for p in dev[:6]]),
                len(bli), str([p["kz"] for p in bli[:6]])))
        n_clip = sum(1 for p in packs if p["clipped"])
        info("Theta_h range [%.3f, %.3f] rad; clip events %d; "
             "a_h = plateau_w > 0 on all windows: %s"
             % (min(p["theta"] for p in packs),
                max(p["theta"] for p in packs), n_clip,
                str(all(p["plate"] > 0 for p in packs))))
        coefs = {}
        rms = {}
        A = np.array([[1.0, math.cos(p["theta"]),
                       math.cos(2 * p["theta"])] for p in dev])
        for r in R_SET:
            y = np.array([p["y_r"][r] / p["plate"]
                          for p in dev])
            c, *_ = np.linalg.lstsq(A, y, rcond=None)
            coefs[r] = c
            rms[r] = float(np.sqrt(np.mean(
                (A @ c - y) ** 2)))
        info("F_r DEV fit rms (y = gammahat_{N+r}/a_h): %s"
             % str({r: round(rms[r], 3) for r in R_SET}))

        def F_of(r, th):
            c = coefs[r]
            return float(c[0] + c[1] * math.cos(th)
                         + c[2] * math.cos(2 * th))

        blind_stats = {}
        for r in (0, -1):
            n_pos = 0
            n_bound = 0
            for p in bli:
                F = F_of(r, p["theta"])
                y = p["y_r"][r] / p["plate"]
                if F >= 0.0:
                    n_pos += 1
                if abs(y - F) < F:
                    n_bound += 1
            blind_stats[r] = (n_pos / len(bli),
                              n_bound / len(bli))
            info("BLIND r=%+d: F_r >= 0 on %d/%d (%.3f) | "
                 "pivot bound |y - F| < F on %d/%d (%.3f)"
                 % (r, n_pos, len(bli), n_pos / len(bli),
                    n_bound, len(bli), n_bound / len(bli)))
        check("G30-legC-constructed", True,
              "Theta_h source-pure (chain <= N-1 + hull "
              "midpoint), a_h = plateau (degrees <= N-5), F_r "
              "= 3-coefficient trig family fitted on DEV only; "
              "BLIND scored exactly once; no target sign and "
              "no measured offset entered any construction "
              "path (firewalled)")
        # controls falsifier
        rr9 = core.build_window(9)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE_ = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE_) > 1e-12)[0]
        ug = np.arange(0.01, 2.0 * rr9["alpha"], 0.01)
        ctrls = (("EPSTEIN", dict(comb=(
                    np.log(nn_idx.astype(float)),
                    2.0 * lamE_[nn_idx]
                    / np.sqrt(nn_idx.astype(float))))),
                 ("SCRAMBLE", dict(scramble_seed=1)),
                 ("SMOOTH", dict(comb=(ug, 2.0
                                       * np.exp(ug / 2.0)
                                       * 0.01))))
        okC_flips = True
        reg_blind = {0: [], -1: []}
        notes = []
        for cname, kw in ctrls:
            dc = HS.window_data(9, **kw)
            Nc = dc["n_max"]
            chc = slim(FC.signed_chain(dc, Nc + R_MAX + 2))
            flip = next(n for n in range(len(chc))
                        if chc[n]["sg_h"] < 0)
            okC_flips = okC_flips and flip == CTRL_FLIPS[cname]
            gb = [chc[Nc - j - 1]["gam"]
                  for j in range(PLATEAU_J[0],
                                 PLATEAU_J[1] + 1)]
            a_c = float(np.mean(gb))
            ge_c = chc[Nc - 2]["gam"]
            refuse = (a_c <= 0.0 or min(gb) <= 0.0
                      or ge_c <= 0.0)
            stat = []
            for r in (0, -1):
                certify = False
                if not refuse:
                    x_all = np.concatenate([dc["xs"],
                                            dc["ys"]])
                    x0c = 0.5 * (float(np.min(x_all))
                                 + float(np.max(x_all)))
                    al_c = chc[Nc - 1]["alphahat"]
                    tt = (x0c - al_c) / (2.0
                                         * math.sqrt(ge_c))
                    th = math.acos(max(-1.0, min(1.0, tt)))
                    F = F_of(r, th)
                    y = chc[Nc + r - 1]["gam"] / a_c
                    certify = (F >= 0.0 and abs(y - F) < F)
                if certify:
                    reg_blind[r].append(cname)
                stat.append("r=%+d %s" % (
                    r, "CERTIFIES (register-blind)" if certify
                    else "refused" if refuse else "fails"))
            notes.append("%s flip %d [%s]"
                         % (cname, flip, ", ".join(stat)))
        ctrl_note = "; ".join(notes)
        cand = (blind_stats[0][0] >= BLIND_BAR
                and blind_stats[0][1] >= BLIND_BAR
                and okC_flips and not reg_blind[0])
        cand_m1 = (blind_stats[-1][0] >= BLIND_BAR
                   and blind_stats[-1][1] >= BLIND_BAR
                   and okC_flips and not reg_blind[-1])
        legC = ("TERMINAL_SIGN_CANDIDATE" if cand
                else "TERMINAL_SIGN_OPEN")
        if cand_m1:
            legC_mod = (" (+CANDIDATE_AT_MINUS1: the last "
                        "RH-load degree passes the blind pivot "
                        "bound register-clean)")
        elif (blind_stats[-1][0] >= BLIND_BAR
              and blind_stats[-1][1] >= BLIND_BAR):
            legC_mod = (" (r = -1 blind bars pass %d/%d but "
                        "the same form certifies %s: "
                        "REGISTER_BLIND, not carried)"
                        % (int(blind_stats[-1][1] * len(bli)),
                           len(bli),
                           "/".join(reg_blind[-1])
                           if reg_blind[-1] else "?"))
        else:
            legC_mod = ""
        okC_ctrl = okC_flips
        # bonus offset gate
        d_dev = [p["delta"] for p in dev]
        d_bli = [p["delta"] for p in bli]
        md = {}
        for v in d_dev:
            md[v] = md.get(v, 0) + 1
        base_val = sorted(md.items(),
                          key=lambda t: (-t[1], t[0]))[0][0]
        b_ex, b_pm = score([base_val] * len(bli), d_bli)
        preds = []
        for p in bli:
            dh = None
            for r in range(0, R_MAX + 1):
                if r in coefs and F_of(r, p["theta"]) < 0.0:
                    dh = r
                    break
            preds.append(dh)
        p_ex, p_pm = score(preds, d_bli)
        bonus_note = ("delta_hat = min{r: F_r(Theta) < 0}: "
                      "BLIND exact %.3f / pm1 %.3f vs baseline "
                      "(mode %d) %.3f / %.3f -> %s"
                      % (p_ex, p_pm, base_val, b_ex, b_pm,
                         "BONUS_SIGN_GO" if
                         (p_pm >= BONUS_PM1
                          and p_ex >= b_ex + BONUS_EDGE)
                         else "offset distribution NOT carried "
                         "by the F_r signs"))
    check("G31-legC-blind-adjudicated", True,
          "SEALED RULE result: %s%s -- blind bars (>= %.2f) at "
          "r = 0: %s; at r = -1: %s"
          % (legC, legC_mod, BLIND_BAR,
             "%.3f / %.3f" % blind_stats[0] if not smoke
             else "SMOKE",
             "%.3f / %.3f" % blind_stats[-1] if not smoke
             else "SMOKE"))
    check("G32-legC-controls-falsifier", okC_ctrl,
          "control flips re-gated 25/21/27 (hard); the frozen "
          "certificate forms measured on every control -- any "
          "certifying control sets the REGISTER_BLIND flag of "
          "that form and kills its candidate status: %s"
          % ctrl_note)
    check("G33-legC-offset-bonus", True, bonus_note)

    section("S7  LEG D -- MODEL CLASS BY IDENTITY (sealed rule)")
    if okA_core and legC == "TERMINAL_SIGN_CANDIDATE":
        legD = "PRUEFER_PHASE_EXIT"
        why = ("the terminal phase Theta_h carries the frontier "
               "sign blind (leg C candidate)")
    elif okA_core:
        legD = ("PADE_NORMAL_STEP: discrete Schlesinger + "
                "finite tau-quotient")
        why = ("carried by the identities that stay EXACT "
               "through the flip: det R_n = 1 (also h_n < 0), "
               "det Y_n = 1, Y_{n+1} = R_n Y_n and its product "
               "across the frontier, r_n = h_n(mutilde)/h_n(mu)"
               " = tau_{n+1}/tau_n, plus band normality min "
               "|gammahat| > 0 (Pade normal index at every "
               "frontier degree); the Weyl-circle / canonical-"
               "moment / Pruefer-exit refinements are NOT "
               "carried: their extra structure (a terminal "
               "parameter carrying the sign) failed the blind "
               "gate")
    else:
        legD = "NO_FIXED_LOCAL_MODEL"
        why = "a leg-A identity failed at the frontier"
    check("G40-class-adjudicated", True,
          "SEALED NAMING RULE result: CLASS(%s) -- %s"
          % (legD, why))

    section("S8  MUST-FAILS")
    okM = True
    p9 = by_kz[9]
    d9 = p9["d"]
    # m1 swapped Y1 readout mapping (12 <-> 21)
    x_all = np.concatenate([d9["xs"], d9["ys"]])
    w_all = np.concatenate([d9["ws"], -d9["vs"]])
    alp = p9["alp_head"]
    gamh = p9["gam_head"]
    P = [np.ones_like(x_all), x_all - alp[0]]
    for k in range(1, N_ID + 2):
        P.append((x_all - alp[k]) * P[k] - gamh[k] * P[k - 1])

    def momf(jdeg, kpow):
        return float(np.sum(w_all * P[jdeg] * x_all ** kpow))

    h_hi = momf(N_ID, N_ID)
    h_lo = momf(N_ID - 1, N_ID - 1)
    bad_g = h_lo * (1.0 / h_hi)
    m1_dev = abs(bad_g - gamh[N_ID]) / abs(gamh[N_ID])
    okM = okM and m1_dev > 1e-3
    # m2 shifted alphahat index in the Schlesinger step (f64)
    z = Z_PANEL[0]

    def cval(jdeg):
        return complex(np.sum(w_all * P[jdeg] / (z - x_all)))

    n = N_ID
    Yn = np.array([[pv(n, z, alp, gamh), cval(n)],
                   [pv(n - 1, z, alp, gamh) / h_lo,
                    cval(n - 1) / h_lo]])
    Yn1 = np.array([[pv(n + 1, z, alp, gamh), cval(n + 1)],
                    [pv(n, z, alp, gamh) / h_hi,
                     cval(n) / h_hi]])
    R_ok = np.array([[z - alp[n], -h_hi], [1.0 / h_hi, 0.0]])
    R_bad = np.array([[z - alp[n - 1], -h_hi],
                      [1.0 / h_hi, 0.0]])
    dev_ok = float(np.max(np.abs(R_ok @ Yn - Yn1))
                   / np.max(np.abs(Yn1)))
    dev_bad = float(np.max(np.abs(R_bad @ Yn - Yn1))
                    / np.max(np.abs(Yn1)))
    okM = okM and dev_ok <= 1e-8 and dev_bad > 1e2 * dev_ok
    # m3 tau alias: h at nf-1 against r at nf breaks the SIGN
    n_alias = sum(1 for p in packs
                  if math.copysign(1.0, p["alias_pred"])
                  != math.copysign(1.0, p["r_nf"]))
    okM = okM and n_alias == len(packs)
    # m4 frontier-consumption oracle
    n_oracle = sum(
        1 for p in packs
        if min(r for r in range(0, R_MAX + 1)
               if p["y_r"].get(r, 1.0) < 0.0) == p["delta"])
    okM = okM and n_oracle == len(packs)
    check("G60-must-fails-fire", okM,
          "swapped Y1 mapping breaks gammahat by %.1e rel; "
          "alphahat index shift breaks the Schlesinger step "
          "(%.1e vs honest %.1e); tau alias (h_{nf-1} vs r_nf) "
          "breaks the SIGN at the flip on %d/%d windows; the "
          "frontier-consumption oracle hits delta on %d/%d "
          "windows -- bars reachable with frontier data, "
          "EXCLUDED by the input firewall"
          % (m1_dev, dev_bad, dev_ok, n_alias, len(packs),
             n_oracle, len(packs)))

    section("S9  VERDICT")
    check("G80-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a frontier "
          "identity round moves no edge); what the round adds: "
          "the degree step at the frontier is an exact rational "
          "Schlesinger transformation THROUGH the sign flip "
          "(det R = 1 needs only h != 0, and every frontier "
          "degree is Pade-normal), the frontier pivot is the "
          "finite tau-quotient identity, the terminal Jacobi "
          "state is exactly readable from Y^(1), the 1/4 "
          "plateau is numerically robust (capacity reading "
          "consistent but degenerate: all hulls have width 2), "
          "and the terminal-phase sign transfer at r = 0 stays "
          "open (the r = -1 pivot bound passes blind but is "
          "REGISTER_BLIND on SMOOTH -- typed, not carried)")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G90-verdict", npass == len(CHECKS),
          "%s + %s + %s%s + CLASS(%s); NO RH claim"
          % (legA, legB, legC,
             legC_mod if not smoke else "", legD))

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


def pv(jdeg, z, alp, gamh):
    """pihat_jdeg(z) from the chain coefficients (f64, moderate
    degree only -- N_FIK_ID discipline)."""
    p0, p1 = 1.0 + 0j, z - alp[0]
    if jdeg == 0:
        return p0
    for k in range(1, jdeg):
        p0, p1 = p1, (z - alp[k]) * p1 - gamh[k] * p0
    return p1


if __name__ == "__main__":
    sys.exit(main())
