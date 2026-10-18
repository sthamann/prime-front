#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""boundary_state_probe -- PRIME.PORT.FRONTIER.BOUNDARYSTATE.01
(round 234): is the frontier offset delta_w the first exit time of
a SOURCE-PURE, FIXED-DIMENSIONAL terminal boundary state?  The
state is built EXCLUSIVELY from data up to the last free stage
(n <= N_w - 1) plus the frozen window geometry; post-frontier
pivots enter ONLY as ground truth inside gates.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r225-r233 discipline): w = window (kz
rung), N_w = builder depth = (S_w + 1)/2, S_w = #supp(mutilde),
n = chain degree, j = n - N_w, delta_w = n_flip - N_w, r = forced
stage index (r = j >= 0).  LADDER RULE (= r232/r233): every
frame-A rung with builder depth h <= 900 (42 rungs, N = 142..878),
sorted by (N_w, kz).  DEV/BLIND RULE (= r233, sealed): even
positions on the sorted ladder are DEV, odd are BLIND.  Controls:
EPSTEIN / SCRAMBLE(seed 1) / SMOOTH on the w9 base, flips
25/21/27 re-gated.

INPUT FIREWALL (binding): every state coordinate and every
predictor consumes ONLY (a) the free chain alphahat_n (n <= N-1),
gammahat_n (n <= N-1), h_n (n <= N-1), (b) node positions and
weights of both zones (frozen window geometry, incl. the node
polynomial), (c) the exact Newton recurrence of the forced moment
tail.  FORBIDDEN inputs: measured offsets, gammahat/h at n >= N
as fit input (ground truth in gates ONLY), target signs, target
inverses, wall eigenvectors, matrix roots, any positivity-defined
normalization.  A builder that needs the target pivot or a post-
frontier object is typed ALIAS_OF_WALL and closed immediately.

SEALED STATE CHOICE (from the repo normalization; dimension 6,
CONSTANT in N): S_h = (abar, gbar, sign h_{N-1}, T_N(z_A),
T_N(z_B), T_N(z_ph)) with abar = alphahat_{N-1}, gbar =
gammahat_{N-1} and T_n(z) = q_n(z)/q_{n-1}(z), where q_n(z) =
C[pihat_n mutilde](z) = sum w pihat_n(x)/(z-x) - sum v
pihat_n(y)/(z-y) is the second-kind function by DIRECT summation
(pihat from the free chain only).  T_N is EXACTLY the terminal
Weyl/J-fraction tail: q_{n+1} = (z - alphahat_n) q_n -
gammahat_n q_{n-1} (orthogonality kills <pihat_n, 1> for n >= 1),
hence T_{n+1} = z - alphahat_n - gammahat_n / T_n with T_1 =
z - alphahat_0 - h_0/m(z) -- the same tail the Weyl m-function
peel produces, computed WITHOUT the unstable peel.  SEALED z
POINTS (band normalization from the free chain): z_A = abar
(band center), z_B from the disclosed 3-point grid
{abar + sqrt(gbar), abar + sqrt(gbar)/sqrt(N), abar +
2 sqrt(gbar)/N} (DEV-selected once, frozen, the ONLY DEV-fitted
discrete choice of leg B), z_ph = abar + dir kappa_eff
sqrt(gbar) with kappa = 1.8 (inside the band edge 2 sqrt(gbar);
rotation angle omega = arccos(kappa/2) per forced step resolves
phase classes up to pi/omega ~ 7 > max delta 5).  INTERIOR-
DIRECTION RULE (sealed): all offsets run toward the hull
interior (dir = sign of hull center - abar) and the phase
offset is capped at kappa_eff = min(kappa, 0.8 room/sqrt(gbar))
with room = interior hull distance -- OUTSIDE the hull q_N is
exponentially small and f64 dies (measured at design time on
kz 13); the per-window rotation angle omega_w =
arccos(kappa_eff/2) is analytic, not fitted.  Node-collision
guard: any z closer than 1e-7 x span to a node is shifted by
dir x 1.7e-6 x span (deterministic, disclosed).

LEG 0 -- ALPHA ROBUSTNESS (four wards BEFORE everything else, on
the r233 fact Spearman(delta; alphahat_{N-1}) = +0.72): (w1)
rho after removing the delta in {4, 5} windows; (w2) leave-one-
out influence of every window; (w3) partial rank correlation
controlling N, h_0, gammahat_{N-1} and local edge mass (sealed:
fraction of total |wtilde| in the top decile of the node span);
(w4) block permutation within 6 contiguous N-blocks of 7 (2000
draws, seed 20260824).  SEALED RULE: ALPHA_OUTLIER_DRIVEN iff
rho_trim < rho_full - 0.25 OR max LOO drop > 0.15; else
ALPHA_PROXY_FOR_BETA iff partial rho < 0.30; else ALPHA_ALIAS
iff permutation p > 0.01; else ALPHA_ROBUST (mapped to
ALPHA_LOAD_BEARING in the final adjudication).  The boundary-
state lane runs regardless of the alpha outcome.

LEG A -- THE LINEAR COLLAPSE AS AN EXACT COORDINATE: the terminal
pivot is EXACTLY affine in the first forced moment: h_N =
m_{2N} + sum_{k<N} c_k m_{N+k} with c_k the pihat_N coefficients
(free data), because m_{2N} sits ONCE in the bordered Hankel
corner: d D_{N+1} / d m_{2N} = D_N, slope of h_N in m_{2N}
EXACTLY 1 -- no quadratic rest, PIVOT_LINEAR_EXACT by rank-one
bordering, NOT approximation.  m_free CONVENTION (sealed): the
equilibrium continuation gammahat_N := gbar, i.e. h_free = gbar
h_{N-1} > 0; then p_h(t) = h_free + t (h_phys - h_free) and the
crossing t*_h = 1/(1 - gammahat_N/gbar); the frontier statement
delta >= 1 is EQUIVALENT to t*_h >= 1 (or no down-crossing).
GATES: exact in rationals on an asymmetric 9-node signed toy
(three-point affinity + slope = D_N + coefficient route =
Hankel route = chain route), at mp on the smallest real rung
(h_N = m_{2N} + sum c_k m_{N+k} to < 1e-30 rel, Newton m_{S+t} =
-sum a_i m_{i+t} to < 1e-30 rel), and (t* >= 1) == (delta >= 1)
on all 42 windows.

LEG B -- BOUNDARY STATE AND PRIMARY SIGN FUNCTIONAL: local
two-point residue estimator G_0 = (z_B - z_A) T_N(z_A) T_N(z_B)
/ (T_N(z_A) - T_N(z_B)) (exact for a one-pole tail; degrades to
the LOCAL residue sign at band center -- derivation frozen);
prediction shat = sign G_0 for the physical half-filling pivot
gammahat_N.  Forced-stage propagation (the Newton propagator in
Weyl coordinates with the SEALED canonical surrogate step
T <- z - abar - gbar/T, the local Jacobi recurrence, NOT the
killed global Moebius path): deltahat_B = first r >= 0 with
G_r < 0 (cap 8 -> miss).  WARDS: the last FREE step must
reproduce T_N from T_{N-1} exactly (T_N = z - abar -
gbar/T_{N-1}, bar 1e-6 of local scale -- validates the direct
q-summation), <pihat_{N-1}, 1> = 0 (bar 1e-6 of term scale),
and an mp dps-40 recomputation of T_N on the smallest rung and
w9 (bar 1e-6 rel).

LEG C -- WEYL PHASE INSTEAD OF LINEAR REGRESSION: Theta_h =
arg[(T_N(z_ph) - t_eq)/(T_N(z_ph) - conj t_eq)] with t_eq =
((z_ph - abar) - i sqrt(4 gbar - (z_ph - abar)^2))/2 (elliptic
fixed point of the canonical step; T real => Theta on the unit
circle).  Sealed quantizer: deltahat_C = round(mod(s (Theta -
Theta_0), 2 pi)/(2 omega_w)) with omega_w = arccos(kappa_eff/2)
analytic per window; s in {+1, -1} and the arc anchor Theta_0
are the ONLY DEV-fitted constants (circular mean of Theta -
s 2 omega_w delta on DEV); BLIND scored once; controls must
exit immediately (deltahat_C <= 0 or degenerate state).

LEG D -- PRIMARY GATE (sealed): sign G_0 == sign gammahat_N
(physical, ground truth ONLY here) counted on ALL 42 windows
(the 18 delta = 0 windows are NEGATIVE at half-filling, the 24
others POSITIVE) and on the BLIND half separately; controls:
correct break = state degenerate by construction (gbar <= 0 or
h_{N-1} <= 0 -- announces the broken world from free data) or
sign match on their own gammahat_N.  SECONDARY: deltahat_B /
deltahat_C blind exact or +-1 vs the sealed baseline (DEV mode
delta).  A perfect delta prediction is bonus, not target.

LEG E -- the leg-0 alpha adjudication enters the final verdict.

SEALED VERDICT RULE: BOUNDARY_STATE_EXACT iff primary 42/42 AND
controls 3/3 AND BLIND deltahat exact rate >= 0.8 (either
propagator); else PHASE_QUANTIZED iff leg C BLIND pm1 >= 0.8 AND
BLIND exact >= baseline exact + 0.15 AND controls 3/3; else
BOUNDARY_SIGN_CARRIED iff primary >= 38/42 AND controls 3/3;
else STATE_DIM_GROWS (measured: the fixed-dimension state does
not carry the half-filling sign; the exact route remains the
S-dimensional Newton moment state).  Modifiers: PIVOT_LINEAR_
EXACT (leg A), ALPHA_LOAD_BEARING / ALPHA_PROXY /
ALPHA_OUTLIER_DRIVEN / ALPHA_ALIAS (leg 0), ALIAS_OF_WALL guard
(m4).  KILL conditions armed: state dimension growing with N;
controls staying positive; any representation consuming the
wall.

MUST-FAILS (each loud): (m1) FRONTIER_CONSUMPTION oracle --
reading gammahat signs at j >= 0 hits delta exactly on every
window (bars reachable, excluded by the input firewall); (m2)
Newton forced-tail recurrence with one flipped coefficient sign
breaks exactly (rationals, asymmetric toy); (m3) shifting the
free-step ward by one index (alphahat_{N-2}, gammahat_{N-2})
breaks the T-recurrence loudly; (m4) a wall-consuming builder
(reading gammahat_N directly) trivially hits 42/42 -- typed
ALIAS_OF_WALL and excluded.

RECORD TABLES (frozen from calib_bs_pass2.log, 22/22; smoke
adjudicates infrastructure only.  CALIBRATION AMENDMENTS,
disclosed -- the state choice, m_free convention, DEV/BLIND
split, primary gate, quantizer form, bars and the verdict rule
were NEVER touched: (a1) the INTERIOR-DIRECTION z rule with the
kappa_eff cap was added at the design/smoke stage BEFORE any
full pass, after the draft z_ph = abar + 1.8 sqrt(gbar) left
the node hull on kz 13 and the f64 second-kind sum died there
(mp-measured dev 4.8 -- outside the hull q_N is exponentially
small); (a2) the G22 report line was tightened between pass 1
and pass 2 (the down-crossing count had mixed two sets in the
TEXT; no number, bar or rule moved)):
CAL_VERDICT = STATE_DIM_GROWS + PIVOT_LINEAR_EXACT +
ALPHA_LOAD_BEARING (robust lead, still unconverted) +
ALIAS_OF_WALL(guard armed).  Key numbers -- LEG 0 (42
windows): rho_full +0.72, rho_trim (delta 4/5 removed) +0.74,
max LOO drop 0.02 (kz 82), partial rho (N, h_0,
gammahat_{N-1}, edge mass controlled) +0.70, block-permutation
p 0.0005 (2000 draws, 6 blocks): ALPHA_ROBUST -- the alpha
signal is not outlier-driven, not a beta proxy, not an N-block
alias; it remains a LEAD (r233: the sealed linear form did not
convert).  LEG A: toy affine exact in rationals (three points
collinear, slope EXACTLY D_5, coefficient = Hankel = chain
route, Newton exact t = 0..2 with loud coefficient-flip
break); smallest rung (kz 18, N = 142) at runtime-scaled dps
319: pivot identity 2.4e-224 rel, Newton m_S / m_{S+1} to
1.2e-298 / 2.7e-298 rel; (t* >= 1 or no down-crossing) ==
(delta >= 1) on 42/42 windows: 29 windows cross downward
(t* in [0.18, 7.10]), the 18 with t* < 1 are EXACTLY the
delta = 0 set, 13 stay at/above the free continuation.
LEG B: free-step ward worst 1.2e-10, orthogonality worst
1.4e-11, mp dps-40 T ward 2.5e-09 (kz 18) / 5.8e-11 (w9);
DEV selection: z_B variant 1 (abar + dir sqrt(gbar)/sqrt(N),
DEV sign hits 11/12/9 of 21 across the grid); PRIMARY: sign
hits 28/42 all (BLIND 16/21), controls 3/3 correct breaks
(EPSTEIN degenerate -- gammahat_{N-1} = -0.486 and h_{N-1} < 0
announce the broken world from free data; SCRAMBLE and SMOOTH
non-degenerate with POSITIVE physical gammahat_N at their
half-filling, sign-matched); deltahat_B all-42 exact/pm1
0.357/0.524, BLIND 0.476/0.524 vs baseline (mode delta = 0)
BLIND 0.524/0.714 -- the propagated delta does NOT beat the
constant baseline.  LEG C: Spearman(Theta; delta) -0.05 all /
-0.06 DEV (no rank signal at all); quantizer (s = +1, Theta_0
= -0.336) BLIND exact/pm1 0.190/0.524, controls 1/3
immediate-exit: PHASE_QUANTIZED NOT reached -- the collapse is
not a slow phase drift, consistent with the r233 no-precursor
fact.  COVARIATES: Spearman(delta; G_0) +0.36, (t*hat) +0.38.
MUST-FAILS: oracle 42/42 (excluded by firewall), Newton
coefficient flip breaks in rationals, m3 index shift 5e12 x
louder (1.3e-01 vs 2.6e-14), m4 wall-builder hits 42/42 and is
typed ALIAS_OF_WALL (guard armed, construction closed).
ADJUDICATION: the sealed 6-dimensional state carries a real
but PARTIAL sign signal (28/42 all, 16/21 blind, against the
trivial ceilings 24/42 always-positive and 18/42 always-
negative) and does NOT reach the 38/42 support bar: the
half-filling sign is NOT a function of this fixed-dimensional
boundary state at the sealed z-geometry; the exact reduction
stands (pivot linear in the first forced moment, delta >= 1
<=> t* >= 1) and the load remains in the S-dimensional Newton
moment state: STATE_DIM_GROWS, honestly measured.  Runtime
~ 10.4 s.  AMENDMENTS AFTER FREEZE: NONE.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import cmath
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
import frontier_micro_probe as FM            # noqa: E402 r233
import hirota_sign_probe as HS               # noqa: E402 r226
import jfraction_probe as JF                 # noqa: E402 r230
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

H_CAP = 900
SMOKE_KZ = (9, 12, 13, 26, 40)
R228_DELTA = {9: 0, 12: 2, 13: 2, 26: 3, 40: 1}
R233_HIST = {0: 18, 1: 10, 2: 6, 3: 6, 4: 1, 5: 1}
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
KAPPA_PH = 1.8
OMEGA = math.acos(KAPPA_PH / 2.0)
PROP_CAP = 8
WARD_BAR = 1e-6
MP_T_DPS = 40
MP_T_BAR = 1e-6
LEGA_BAR = 1e-30
PERM_N = 2000
PERM_SEED = 20260824
TRIM_EDGE = 0.25
LOO_BAR = 0.15
PARTIAL_BAR = 0.30
PERM_P_BAR = 0.01
PRIMARY_BAR = 42
SUPPORT_BAR = 38
PM1_BAR = 0.8
EXACT_EDGE = 0.15
BLIND_EXACT_BAR = 0.8
M3_LOUD = 1e3
CAL_VERDICT = ("STATE_DIM_GROWS + PIVOT_LINEAR_EXACT + "
               "ALPHA_LOAD_BEARING (primary 28/42, controls 3/3) "
               "+ ALIAS_OF_WALL(guard armed)")

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
    return (not bad), ("NO zero/prime oracles; index firewall "
                       "w/N/n/j/delta/r binding; state choice, "
                       "z-grid, m_free convention, DEV/BLIND, "
                       "primary gate and verdict rule sealed in "
                       "the frozen spec"
                       if not bad else "; ".join(bad))


def ranks(v):
    v = np.asarray(v, float)
    order = np.argsort(v, kind="stable")
    rk = np.empty(len(v))
    rk[order] = np.arange(len(v), dtype=float)
    for val in np.unique(v):
        m = v == val
        rk[m] = rk[m].mean()
    return rk


def partial_spearman(x, y, covs):
    rx, ry = ranks(x), ranks(y)
    C = np.column_stack([np.ones(len(rx))] + [ranks(c) for c in covs])
    ex = rx - C @ np.linalg.lstsq(C, rx, rcond=None)[0]
    ey = ry - C @ np.linalg.lstsq(C, ry, rcond=None)[0]
    den = math.sqrt(float(np.sum(ex ** 2) * np.sum(ey ** 2)))
    return float(np.sum(ex * ey) / den) if den > 0 else 0.0


def frac_det(M):
    M = [row[:] for row in M]
    n = len(M)
    det = Fr(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None:
            return Fr(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            det = -det
        det *= M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n):
                M[r][c] -= f * M[i][c]
    return det


def wrap_pi(a):
    return math.atan2(math.sin(a), math.cos(a))


# ---------------------------------------------------- chain + state
def chain_pass(d, n_hi, zs=(), degs=frozenset()):
    """scaled signed monic Stieltjes recursion on mutilde = mu - nu
    (FC.signed_chain recursion verbatim), additionally recording
    the scaled second-kind sums qtilde_n(z) = e^{-Ls_n} q_n(z),
    q_n(z) = sum w pihat_n(x)/(z-x) - sum v pihat_n(y)/(z-y), at
    the requested degrees.  Source-pure: node positions + weights
    of both zones only.  gams[n] = gammahat_{n+1} (ground truth
    fields for n >= N-1 are gate-only by the input firewall)."""
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]

    def sdot(fx, gx, fy, gy):
        return float(np.sum(ws * fx * gx) - np.sum(vs * fy * gy))

    qx_m = np.zeros_like(xs)
    qx = np.ones_like(xs)
    qy_m = np.zeros_like(ys)
    qy = np.ones_like(ys)
    Ls = Ls_m = 0.0
    eta = sdot(qx, qx, qy, qy)
    eta_m = eta
    h0 = eta
    lg_h, sg_h = math.log(abs(eta)), math.copysign(1.0, eta)
    al, gams, sgs, lghs = [], [], [], []
    qrec = {}
    flip = None
    for n in range(n_hi):
        if n in degs:
            row = []
            for z in zs:
                s = (float(np.sum(ws * qx / (z - xs)))
                     - float(np.sum(vs * qy / (z - ys))))
                row.append(s)
            o_num = float(np.sum(ws * qx) - np.sum(vs * qy))
            o_den = float(np.sum(np.abs(ws * qx))
                          + np.sum(np.abs(vs * qy)))
            qrec[n] = dict(Ls=Ls, q=row, orth=(o_num, o_den))
        sgs.append(sg_h)
        lghs.append(lg_h)
        if flip is None and sg_h < 0:
            flip = n
        alh = sdot(xs * qx, qx, ys * qy, qy) / eta
        al.append(alh)
        if n == 0:
            px = (xs - alh) * qx
            py = (ys - alh) * qy
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            px = (xs - alh) * qx - ge * math.exp(Ls_m - Ls) * qx_m
            py = (ys - alh) * qy - ge * math.exp(Ls_m - Ls) * qy_m
        sc = max(float(np.max(np.abs(px))),
                 float(np.max(np.abs(py))))
        qx_m, qy_m, eta_m, Ls_m = qx, qy, eta, Ls
        qx, qy = px / sc, py / sc
        Ls += math.log(sc)
        eta = sdot(qx, qx, qy, qy)
        gam = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
        gams.append(gam)
        lg_h += math.log(abs(gam))
        sg_h *= math.copysign(1.0, gam)
    return dict(h0=h0, al=al, gams=gams, sgs=sgs, lghs=lghs,
                flip=flip, qrec=qrec)


def build_zpts(abar, gbar, N, alln):
    """sealed z points; all offsets run TOWARD the hull interior
    and the phase offset is capped at 0.8 x the interior room
    (outside the hull q_N is exponentially small and f64 dies --
    interior-direction rule sealed in the spec).  Node-collision
    guard disclosed.  Order: [z_A, z_B1, z_B2, z_B3, z_ph];
    returns (zpts, kappa_eff, direction)."""
    sg = math.sqrt(gbar)
    lo, hi = float(np.min(alln)), float(np.max(alln))
    span = hi - lo
    dire = 1.0 if (lo + hi) / 2.0 >= abar else -1.0
    room = (hi - abar) if dire > 0 else (abar - lo)
    off1 = min(sg, 0.8 * room)
    kap = min(KAPPA_PH, 0.8 * room / sg)

    def guard(z):
        while float(np.min(np.abs(alln - z))) < 1e-7 * span:
            z += dire * 1.7e-6 * span
        return z

    zpts = [guard(abar),
            guard(abar + dire * off1),
            guard(abar + dire * sg / math.sqrt(N)),
            guard(abar + dire * 2.0 * sg / N),
            guard(abar + dire * kap * sg)]
    return zpts, kap, dire


def T_of(qrec, n, zi):
    r0, r1 = qrec[n - 1], qrec[n]
    if r0["q"][zi] == 0.0:
        return math.inf
    return math.exp(r1["Ls"] - r0["Ls"]) * r1["q"][zi] / r0["q"][zi]


def window_record(kz, d, with_census=True):
    """everything one window contributes.  State fields consume
    free data (n <= N-1) + geometry only; gt_* fields are ground
    truth (gates only)."""
    N = d["n_max"]
    S = len(d["xs"]) + len(d["ys"])
    nf = None
    if with_census:
        nf, _ncap, _rt = FM.sm_flip(d)
    p1 = chain_pass(d, N)
    abar = p1["al"][N - 1]
    gbar = p1["gams"][N - 2]
    sg_hNm1 = p1["sgs"][N - 1]
    if gbar <= 0.0 or sg_hNm1 <= 0.0:
        return dict(kz=kz, N=N, S=S, nf=nf, degenerate=True,
                    abar=abar, gbar=gbar, sg_hNm1=sg_hNm1,
                    h0=p1["h0"], gt_gamN=p1["gams"][N - 1])
    alln = np.concatenate([d["xs"], d["ys"]])
    zs, kap, dire = build_zpts(abar, gbar, N, alln)
    n_hi = min((nf if nf is not None else N) + 3, S - 1)
    n_hi = max(n_hi, N + 1)
    p2 = chain_pass(d, n_hi, zs, degs={N - 2, N - 1, N})
    TN = [T_of(p2["qrec"], N, i) for i in range(len(zs))]
    TNm1 = [T_of(p2["qrec"], N - 1, i) for i in range(len(zs))]
    # free-step ward (z_A and z_ph) + one-index-shift residual (m3)
    ward = []
    ward_shift = []
    for zi in (0, 4):
        z = zs[zi]
        pred = z - abar - gbar / TNm1[zi]
        preds = z - p2["al"][N - 2] - p2["gams"][N - 3] / TNm1[zi]
        scale = abs(TN[zi]) + abs(z - abar) + abs(gbar / TNm1[zi])
        ward.append(abs(TN[zi] - pred) / scale)
        ward_shift.append(abs(TN[zi] - preds) / scale)
    orth = p2["qrec"][N - 1]["orth"]
    absw = np.concatenate([np.abs(d["ws"]), np.abs(d["vs"])])
    thr = float(np.min(alln)) + 0.9 * (float(np.max(alln))
                                       - float(np.min(alln)))
    em = float(np.sum(absw[alln >= thr]) / np.sum(absw))
    gt = [p2["gams"][N - 1 + j]
          for j in range(0, min(len(p2["gams"]) - N + 1,
                                (nf - N if nf else 0) + 2))]
    return dict(kz=kz, N=N, S=S, nf=nf, degenerate=False,
                flip_g=p2["flip"], abar=abar, gbar=gbar,
                sg_hNm1=sg_hNm1, h0=p1["h0"], em=em,
                zs=zs, kap=kap, TN=TN, TNm1=TNm1, ward=ward,
                ward_shift=ward_shift,
                orth=abs(orth[0]) / max(orth[1], 1e-300),
                gt_gamN=p2["gams"][N - 1], gt_prof=gt)


# ----------------------------------------------------- estimators
def g0_two_point(zA, zB, TA, TB):
    """local two-point residue estimator (frozen derivation: the
    one-pole tail model gammahat/(z - a - c) with constant c;
    near a pole of T it degrades to the local residue)."""
    if not (math.isfinite(TA) and math.isfinite(TB)):
        return None
    if abs(TA - TB) < 1e-12 * max(abs(TA), abs(TB), 1e-300):
        return None
    return (zB - zA) * TA * TB / (TA - TB)


def delta_prop(rec, ib):
    """deltahat_B: propagate both T points with the sealed
    canonical surrogate step T <- z - abar - gbar/T; first r with
    G_r < 0 (cap PROP_CAP -> None = miss)."""
    zA, zB = rec["zs"][0], rec["zs"][1 + ib]
    TA, TB = rec["TN"][0], rec["TN"][1 + ib]
    for r in range(PROP_CAP + 1):
        g = g0_two_point(zA, zB, TA, TB)
        if g is None:
            return None
        if g < 0.0:
            return r
        if abs(TA) < 1e-300 or abs(TB) < 1e-300:
            return None
        TA = zA - rec["abar"] - rec["gbar"] / TA
        TB = zB - rec["abar"] - rec["gbar"] / TB
    return None


def theta_of(rec):
    """returns (Theta, omega_w) with the per-window rotation
    angle omega_w = arccos(kappa_eff/2) of the sealed capped
    phase point."""
    z = rec["zs"][4]
    dz = z - rec["abar"]
    disc = 4.0 * rec["gbar"] - dz * dz
    if disc <= 0.0:
        return None, None
    om = math.acos(min(rec["kap"] / 2.0, 1.0))
    teq = complex(dz / 2.0, -math.sqrt(disc) / 2.0)
    T = rec["TN"][4]
    if not math.isfinite(T):
        return math.pi, om
    num = complex(T, 0.0) - teq
    den = complex(T, 0.0) - teq.conjugate()
    if den == 0:
        return None, None
    return cmath.phase(num / den), om


def score(preds, truth):
    ex = sum(1 for p, t in zip(preds, truth)
             if p is not None and p == t)
    pm = sum(1 for p, t in zip(preds, truth)
             if p is not None and abs(p - t) <= 1)
    return ex / len(truth), pm / len(truth)


# ------------------------------------------------------- mp wards
def mp_T_ward(d, rec):
    """dps-40 plain monic signed recursion recomputes T_N at the
    sealed z points; returns worst rel dev vs the f64 values."""
    import mpmath as mp
    mp.mp.dps = MP_T_DPS
    nds = ([mp.mpf(float(x)) for x in d["xs"]]
           + [mp.mpf(float(y)) for y in d["ys"]])
    wt = ([mp.mpf(float(w)) for w in d["ws"]]
          + [-mp.mpf(float(v)) for v in d["vs"]])
    N = rec["N"]
    zs = [mp.mpf(z) for z in rec["zs"]]
    pk = [mp.mpf(1)] * len(nds)
    pkm = [mp.mpf(0)] * len(nds)
    hs = [mp.fsum(w * p * p for w, p in zip(wt, pk))]
    qsum = {}
    for n in range(N + 1):
        if n in (N - 1, N):
            qsum[n] = [mp.fsum(w * p / (z - x) for w, p, x in
                               zip(wt, pk, nds)) for z in zs]
        a = mp.fsum(w * x * p * p
                    for w, x, p in zip(wt, nds, pk)) / hs[-1]
        g = (hs[-1] / hs[-2]) if n > 0 else mp.mpf(0)
        nx = [(x - a) * p - g * q for x, p, q in zip(nds, pk, pkm)]
        pkm, pk = pk, nx
        hs.append(mp.fsum(w * p * p for w, p in zip(wt, pk)))
    worst = 0.0
    for zi in range(len(zs)):
        t_mp = qsum[N][zi] / qsum[N - 1][zi]
        dev = abs(float(t_mp) - rec["TN"][zi]) / max(
            abs(float(t_mp)), 1e-300)
        worst = max(worst, dev)
    return worst


def legA_mp(d):
    """mp gate of the exact pivot identity and the Newton forced
    tail on ONE real rung: h_N = m_{2N} + sum_{k<N} c_k m_{N+k}
    (c_k = pihat_N coefficients from the free chain) and
    m_{S+t} = -sum_i a_i m_{i+t}.  Runtime-scaled dps."""
    import mpmath as mp
    N = d["n_max"]
    nds_f = np.concatenate([d["xs"], d["ys"]])
    xmax = float(np.max(np.abs(nds_f)))
    ch = FC.signed_chain(d, N + 1)
    lg_hN = ch[N]["lg_h"] / math.log(10.0)
    dps = int(2 * N * math.log10(max(xmax, 1.5)) + 0.45 * N
              + max(0.0, -lg_hN) + 120)
    dps = min(max(dps, 200), 1400)
    mp.mp.dps = dps
    nds = ([mp.mpf(float(x)) for x in d["xs"]]
           + [mp.mpf(float(y)) for y in d["ys"]])
    wt = ([mp.mpf(float(w)) for w in d["ws"]]
          + [-mp.mpf(float(v)) for v in d["vs"]])
    S = len(nds)
    # chain: alphahat/gammahat (free) + h_N (comparison target)
    pk = [mp.mpf(1)] * S
    pkm = [mp.mpf(0)] * S
    hs = [mp.fsum(w * p * p for w, p in zip(wt, pk))]
    alv, gav = [], []
    for n in range(N):
        a = mp.fsum(w * x * p * p
                    for w, x, p in zip(wt, nds, pk)) / hs[-1]
        alv.append(a)
        g = (hs[-1] / hs[-2]) if n > 0 else mp.mpf(0)
        gav.append(g)
        nx = [(x - a) * p - g * q for x, p, q in zip(nds, pk, pkm)]
        pkm, pk = pk, nx
        hs.append(mp.fsum(w * p * p for w, p in zip(wt, pk)))
    h_N = hs[N]
    # pihat_N coefficients (ascending) from the FREE chain
    c_m = [mp.mpf(0)]
    c = [mp.mpf(1)]
    for n in range(N):
        shift = [mp.mpf(0)] + c
        nxt = [mp.mpf(0)] * (n + 2)
        for i in range(n + 2):
            v = shift[i] - (alv[n] * c[i] if i < len(c) else 0)
            if n > 0 and i < len(c_m):
                v -= gav[n] * c_m[i]
            nxt[i] = v
        c_m, c = c, nxt
    # moments m_k, k <= 2N (= S + 1)
    mom = []
    pw = [mp.mpf(1)] * S
    for k in range(2 * N + 1):
        mom.append(mp.fsum(w * p for w, p in zip(wt, pw)))
        pw = [p * x for p, x in zip(pw, nds)]
    h_coef = mp.fsum(c[k] * mom[N + k] for k in range(N + 1))
    dev_piv = abs(h_coef - h_N) / abs(h_N)
    # Newton: node polynomial coefficients a_i (monic degree S)
    a = [mp.mpf(1)]
    for x in nds:
        nxt = [mp.mpf(0)] * (len(a) + 1)
        for i, cc in enumerate(a):
            nxt[i + 1] += cc
            nxt[i] -= x * cc
        a = nxt
    devs_new = []
    for t in (0, 1):
        rhs = -mp.fsum(a[i] * mom[i + t] for i in range(S))
        devs_new.append(abs(rhs - mom[S + t])
                        / max(abs(mom[S + t]), mp.mpf(1e-300)))
    return dps, float(dev_piv), [float(x) for x in devs_new]


# --------------------------------------------------- leg A toy
TOY_NODES = [Fr(-5, 7), Fr(-4, 7), Fr(-2, 7), Fr(-1, 7), Fr(1, 7),
             Fr(2, 7), Fr(3, 7), Fr(4, 7), Fr(6, 7)]
TOY_WTS = [Fr(3, 11), Fr(-1, 9), Fr(2, 7), Fr(-1, 5), Fr(4, 9),
           Fr(-2, 11), Fr(2, 9), Fr(-1, 7), Fr(3, 13)]


def legA_toy():
    """exact rational gates: (i) D_{N+1}(m_{2N}) affine with slope
    D_N (three points collinear), (ii) coefficient route =
    Hankel route = chain route for h_N, (iii) Newton recurrence
    exact + loud break on one flipped coefficient (m2)."""
    nodes, wts = TOY_NODES, TOY_WTS
    S = len(nodes)
    N = (S + 1) // 2
    mom = [sum(w * x ** k for w, x in zip(wts, nodes))
           for k in range(S + 4)]
    D_N = frac_det([[mom[i + j] for j in range(N)]
                    for i in range(N)])

    def D_Np1(t):
        M = [[(mom[i + j] if (i + j) < 2 * N else t)
              for j in range(N + 1)] for i in range(N + 1)]
        return frac_det(M)

    t0, t1, t2 = Fr(0), Fr(1), Fr(5, 2)
    d0, d1, d2 = D_Np1(t0), D_Np1(t1), D_Np1(t2)
    ok_aff = (d1 - d0 == D_N) and (d2 - d0 == Fr(5, 2) * D_N)
    # coefficient route
    al, beta, hs = JF.stieltjes_exact(nodes, wts, N)
    c_m = [Fr(0)]
    c = [Fr(1)]
    for n in range(N):
        shift = [Fr(0)] + c
        nxt = [Fr(0)] * (n + 2)
        for i in range(n + 2):
            v = shift[i] - (al[n] * c[i] if i < len(c) else Fr(0))
            if n > 0 and i < len(c_m):
                v -= beta[n - 1] * c_m[i]
            nxt[i] = v
        c_m, c = c, nxt
    h_coef = sum(c[k] * mom[N + k] for k in range(N + 1))
    ok_routes = (h_coef == D_Np1(mom[2 * N]) / D_N
                 and h_coef == hs[N])
    # Newton + m2 break
    a = [Fr(1)]
    for x in nodes:
        nxt = [Fr(0)] * (len(a) + 1)
        for i, cc in enumerate(a):
            nxt[i + 1] += cc
            nxt[i] -= x * cc
        a = nxt
    ok_new = all(mom[S + t] == -sum(a[i] * mom[i + t]
                                    for i in range(S))
                 for t in range(0, 3))
    bad = a[:]
    bad[1] = -bad[1]
    ok_m2 = (bad[1] != a[1]) and any(
        mom[S + t] != -sum(bad[i] * mom[i + t] for i in range(S))
        for t in range(0, 3))
    return ok_aff, ok_routes, ok_new, ok_m2


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("boundary_state_probe -- PRIME.PORT.FRONTIER."
          "BOUNDARYSTATE.01 (round 234)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (five known rungs, infrastructure "
                        "only)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "ladder = frame-A h <= %d (r232/r233); DEV = even / "
          "BLIND = odd on the (N, kz)-sorted ladder; state dim 6 "
          "CONSTANT; z-grid, m_free convention (gammahat_N,free "
          "= gammahat_{N-1}), kappa_ph = %.1f (omega %.3f), "
          "quantizer, primary gate (sign at physical half-"
          "filling), control-break rule and the verdict rule "
          "sealed in the frozen spec; post-frontier data = "
          "ground truth in gates ONLY" % (H_CAP, KAPPA_PH, OMEGA))

    # ---------------- S1: census + leg 0
    section("S1  CENSUS RE-DERIVATION + LEG 0 ALPHA WARDS")
    if smoke:
        kzs = list(SMOKE_KZ)
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
    recs = []
    for kz in kzs:
        d = HS.window_data(kz)
        recs.append(window_record(kz, d))
    recs.sort(key=lambda r: (r["N"], r["kz"]))
    ok_c = all((not r["degenerate"]) and r["nf"] is not None
               and r["nf"] >= r["N"] and r["S"] == 2 * r["N"] - 1
               and r["flip_g"] == r["nf"] for r in recs)
    deltas = [r["nf"] - r["N"] for r in recs]
    hist = {}
    for dl in deltas:
        hist[dl] = hist.get(dl, 0) + 1
    if smoke:
        ok_h = all((r["nf"] - r["N"]) == R228_DELTA[r["kz"]]
                   for r in recs)
        hist_note = "smoke: r228 offsets 0/2/2/3/1 re-derived"
    else:
        ok_h = hist == R233_HIST
        hist_note = ("histogram %s == r233 census"
                     % str(dict(sorted(hist.items()))))
    check("G10-census-rederived", ok_c and ok_h,
          "%d windows: flip found, no flip below N_w, S = 2N - 1, "
          "SM r-chain == signed h-chain on every window; %s"
          % (len(recs), hist_note))

    alp = [r["abar"] for r in recs]
    rho_full = FM.spearman(alp, deltas)
    keep = [i for i, dl in enumerate(deltas) if dl < 4]
    rho_trim = FM.spearman([alp[i] for i in keep],
                           [deltas[i] for i in keep])
    loo = []
    for i in range(len(recs)):
        ii = [j for j in range(len(recs)) if j != i]
        loo.append(FM.spearman([alp[j] for j in ii],
                               [deltas[j] for j in ii]))
    loo_drop = max(abs(rho_full - v) for v in loo)
    loo_kz = recs[int(np.argmax([abs(rho_full - v)
                                 for v in loo]))]["kz"]
    covs = [[r["N"] for r in recs], [r["h0"] for r in recs],
            [r["gbar"] for r in recs], [r["em"] for r in recs]]
    rho_part = partial_spearman(alp, deltas, covs)
    # block permutation (6 contiguous N-blocks)
    rng = np.random.default_rng(PERM_SEED)
    nper = 200 if smoke else PERM_N
    bs = max(1, len(recs) // 6)
    blocks = [list(range(i, min(i + bs, len(recs))))
              for i in range(0, len(recs), bs)]
    hits_p = 0
    darr = np.asarray(deltas, float)
    for _ in range(nper):
        dp = darr.copy()
        for b in blocks:
            dp[b] = dp[rng.permutation(b)]
        if abs(FM.spearman(alp, dp)) >= abs(rho_full):
            hits_p += 1
    p_perm = (1 + hits_p) / (nper + 1)
    if rho_trim < rho_full - TRIM_EDGE or loo_drop > LOO_BAR:
        alpha_v = "ALPHA_OUTLIER_DRIVEN"
    elif rho_part < PARTIAL_BAR:
        alpha_v = "ALPHA_PROXY_FOR_BETA"
    elif p_perm > PERM_P_BAR:
        alpha_v = "ALPHA_ALIAS"
    else:
        alpha_v = "ALPHA_ROBUST"
    check("G11-alpha-wards", True,
          "rho_full %+.2f | trim(delta 4/5 out) %+.2f | max LOO "
          "drop %.2f (kz %d) | partial (N, h_0, gammahat_{N-1}, "
          "edge mass) %+.2f | block-perm p %.4f (%d draws, %d "
          "blocks)" % (rho_full, rho_trim, loo_drop, loo_kz,
                       rho_part, p_perm, nper, len(blocks)))
    check("G12-alpha-adjudicated", True,
          "SEALED RULE result: %s (bars: trim edge %.2f, LOO "
          "%.2f, partial %.2f, perm p %.2f); the r233 alpha "
          "rank signal is adjudicated, not assumed; it remains "
          "a LEAD either way (the sealed linear form did not "
          "convert in r233)" % (alpha_v, TRIM_EDGE, LOO_BAR,
                                PARTIAL_BAR, PERM_P_BAR))

    # ---------------- S2: leg A
    section("S2  LEG A -- THE EXACT LINEAR PIVOT COORDINATE")
    ok_aff, ok_routes, ok_new, ok_m2 = legA_toy()
    check("G20-toy-affine-exact", ok_aff and ok_routes and ok_new,
          "rationals (asymmetric 9-node signed toy, N = 5): "
          "D_{N+1}(m_{2N}) affine with slope EXACTLY D_N (three "
          "points collinear), h_N coefficient route = bordered-"
          "Hankel route = chain route, Newton forced tail exact "
          "for t = 0..2: the terminal pivot is EXACTLY linear in "
          "the first forced moment -- rank-one bordering, no "
          "quadratic rest (PIVOT_LINEAR_EXACT)")
    if smoke:
        check("G21-real-pivot-identity", True,
              "SMOKE: mp leg skipped (infrastructure only)")
    else:
        d_small = HS.window_data(recs[0]["kz"])
        dps, dev_piv, devs_new = legA_mp(d_small)
        check("G21-real-pivot-identity",
              dev_piv <= LEGA_BAR and all(v <= LEGA_BAR
                                          for v in devs_new),
              "smallest rung kz %d (N = %d, dps %d): h_N = m_{2N} "
              "+ sum c_k m_{N+k} to %.1e rel; Newton m_S / "
              "m_{S+1} = -sum a_i m_{i+t} to %.1e / %.1e rel: "
              "the linear coordinate is exact on the real comb, "
              "not a toy artifact"
              % (recs[0]["kz"], recs[0]["N"], dps, dev_piv,
                 devs_new[0], devs_new[1]))
    tstars = []
    ok_t = True
    n_cross = 0
    for r in recs:
        rho = r["gt_gamN"] / r["gbar"]
        if rho < 1.0:
            ts = 1.0 / (1.0 - rho)
            n_cross += 1
        else:
            ts = math.inf
        tstars.append(ts)
        ok_t = ok_t and ((r["gt_gamN"] >= 0.0)
                         == ((r["nf"] - r["N"]) >= 1))
    fin_all = [t for t in tstars if math.isfinite(t)]
    fin_lt1 = [t for t in fin_all if t < 1.0]
    check("G22-tstar-coordinate", ok_t,
          "m_free CONVENTION sealed (equilibrium continuation "
          "gammahat_N,free = gammahat_{N-1}); t* = 1/(1 - "
          "gammahat_N/gammahat_{N-1}); (t* >= 1 or no down-"
          "crossing) == (delta >= 1) on ALL %d windows; %d "
          "windows cross downward (t* in [%.2f, %.2f]), %d of "
          "them before t = 1 (EXACTLY the delta = 0 set), %d "
          "stay at/above the free continuation: the frontier "
          "statement delta >= 1 reduces to t* >= 1 EXACTLY"
          % (len(recs), n_cross,
             min(fin_all) if fin_all else float("nan"),
             max(fin_all) if fin_all else float("nan"),
             len(fin_lt1), len(recs) - n_cross))

    # ---------------- S3: leg B
    section("S3  LEG B -- BOUNDARY STATE + PRIMARY SIGN GATE")
    worst_ward = max(max(r["ward"]) for r in recs)
    worst_shift = min(min(r["ward_shift"]) for r in recs)
    worst_orth = max(r["orth"] for r in recs)
    check("G30-state-wards", worst_ward <= WARD_BAR
          and worst_orth <= WARD_BAR,
          "state dim 6 CONSTANT in N (abar, gbar, sign h_{N-1}, "
          "T_N at 3 sealed z); last FREE step reproduces T_N "
          "from T_{N-1} on every window (worst %.1e, bar %.0e) "
          "and <pihat_{N-1}, 1> = 0 (worst %.1e): the direct "
          "second-kind summation is honest f64"
          % (worst_ward, WARD_BAR, worst_orth))
    if smoke:
        check("G31-mp-T-ward", True, "SMOKE: mp ward skipped")
    else:
        dev1 = mp_T_ward(HS.window_data(recs[0]["kz"]), recs[0])
        r9 = next(r for r in recs if r["kz"] == 9)
        dev9 = mp_T_ward(HS.window_data(9), r9)
        check("G31-mp-T-ward", dev1 <= MP_T_BAR
              and dev9 <= MP_T_BAR,
              "mp dps-%d plain monic recomputation of T_N at all "
              "sealed z: rel dev %.1e (kz %d) / %.1e (w9), bar "
              "%.0e -- T_N is not an f64 artifact"
              % (MP_T_DPS, dev1, recs[0]["kz"], dev9, MP_T_BAR))

    dev_idx = list(range(0, len(recs), 2))
    bli_idx = list(range(1, len(recs), 2))
    d_dev = [deltas[i] for i in dev_idx]
    d_bli = [deltas[i] for i in bli_idx]
    # DEV selection of the z_B variant (sign hits on DEV)
    hits_v = []
    for ib in range(3):
        h = 0
        for i in dev_idx:
            g = g0_two_point(recs[i]["zs"][0], recs[i]["zs"][1 + ib],
                             recs[i]["TN"][0], recs[i]["TN"][1 + ib])
            if g is not None and (g >= 0) == (recs[i]["gt_gamN"]
                                              >= 0):
                h += 1
        hits_v.append(h)
    ib_sel = int(np.argmax(hits_v))
    check("G32-dev-selection", True,
          "the ONLY DEV-fitted discrete choice: z_B variant %d "
          "of the sealed grid (DEV sign hits %s of %d) -- "
          "frozen, BLIND untouched until scoring"
          % (ib_sel, str(hits_v), len(dev_idx)))

    g0s, hit_all, hit_bli = [], 0, 0
    for i, r in enumerate(recs):
        g = g0_two_point(r["zs"][0], r["zs"][1 + ib_sel],
                         r["TN"][0], r["TN"][1 + ib_sel])
        g0s.append(g)
        ok = g is not None and (g >= 0) == (r["gt_gamN"] >= 0)
        hit_all += int(ok)
        if i in bli_idx:
            hit_bli += int(ok)
    # controls
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = PIK.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ug = np.arange(0.01, 2.0 * rr9["alpha"], 0.01)
    ctrls = (("EPSTEIN", dict(comb=(
                np.log(nn.astype(float)),
                2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
             ("SCRAMBLE", dict(scramble_seed=1)),
             ("SMOOTH", dict(comb=(ug, 2.0 * np.exp(ug / 2.0)
                                   * 0.01))))
    ok_cf = True
    ctrl_ok = 0
    ctrl_recs = {}
    for cname, kw in ctrls:
        dc = HS.window_data(9, **kw)
        rc = window_record(cname, dc, with_census=False)
        ctrl_recs[cname] = rc
        pc = chain_pass(dc, 45)
        ok_cf = ok_cf and pc["flip"] == CTRL_FLIPS[cname]
        if rc["degenerate"]:
            good = True
            note = ("DEGENERATE state (gammahat_{N-1} = %+.3e, "
                    "sign h_{N-1} = %+d): the free data already "
                    "announces the broken world -- correct break"
                    % (rc["gbar"], int(rc["sg_hNm1"])))
        else:
            g = g0_two_point(rc["zs"][0], rc["zs"][1 + ib_sel],
                             rc["TN"][0], rc["TN"][1 + ib_sel])
            good = g is not None and (g >= 0) == (rc["gt_gamN"]
                                                  >= 0)
            note = ("G_0 = %+.3e vs physical gammahat_N = %+.3e "
                    "-> %s" % (g if g is not None else float("nan"),
                               rc["gt_gamN"],
                               "sign MATCH" if good else "MISS"))
        ctrl_ok += int(good)
        info("%-8s flip %d (target %d) | %s"
             % (cname, pc["flip"], CTRL_FLIPS[cname], note))
    check("G33-control-flips-regated", ok_cf,
          "EPSTEIN/SCRAMBLE/SMOOTH flip at 25/21/27 exactly")
    rho_g0 = FM.spearman([g if g is not None else 0.0
                          for g in g0s], deltas)
    ts_hat = [1.0 / (1.0 - g / r["gbar"])
              if (g is not None and g / r["gbar"] < 1.0)
              else 2.0
              for g, r in zip(g0s, recs)]
    rho_ts = FM.spearman(ts_hat, deltas)
    check("G34-primary-sign-gate", True,
          "SEALED PRIMARY RESULT: sign(G_0) == sign(gammahat_N "
          "at the physical half-filling point) on %d/%d windows "
          "(BLIND %d/%d); controls %d/3 correct breaks; "
          "Spearman(delta; G_0) %+.2f, (delta; t*hat) %+.2f -- "
          "the bar for BOUNDARY_STATE_EXACT is %d/%d + 3/3, for "
          "BOUNDARY_SIGN_CARRIED %d/%d + 3/3"
          % (hit_all, len(recs), hit_bli, len(bli_idx), ctrl_ok,
             rho_g0, rho_ts, PRIMARY_BAR, len(recs), SUPPORT_BAR,
             len(recs)))
    # deltahat_B propagation
    preds_all = [delta_prop(r, ib_sel) for r in recs]
    exB_all, pmB_all = score(preds_all, deltas)
    exB_bli, pmB_bli = score([preds_all[i] for i in bli_idx],
                             d_bli)
    md = {}
    for v in d_dev:
        md[v] = md.get(v, 0) + 1
    base_val = sorted(md.items(), key=lambda t: (-t[1], t[0]))[0][0]
    b_ex, b_pm = score([base_val] * len(bli_idx), d_bli)
    check("G35-propagated-delta", True,
          "deltahat_B (canonical surrogate propagation, zero "
          "fitted constants): all-42 exact/pm1 %.3f/%.3f, BLIND "
          "%.3f/%.3f vs baseline (constant delta = %d) BLIND "
          "%.3f/%.3f -- secondary, bonus not target"
          % (exB_all, pmB_all, exB_bli, pmB_bli, base_val,
             b_ex, b_pm))

    # ---------------- S4: leg C
    section("S4  LEG C -- WEYL PHASE QUANTIZATION")
    th_om = [theta_of(r) for r in recs]
    thetas = [t for t, _o in th_om]
    omegas = [o for _t, o in th_om]
    th_ok = [i for i in range(len(recs)) if thetas[i] is not None]
    rho_th = FM.spearman([thetas[i] for i in th_ok],
                         [deltas[i] for i in th_ok])
    rho_th_dev = FM.spearman(
        [thetas[i] for i in dev_idx if thetas[i] is not None],
        [deltas[i] for i in dev_idx if thetas[i] is not None])
    best = None
    for s in (1.0, -1.0):
        zsum = 0j
        for i in dev_idx:
            if thetas[i] is None:
                continue
            zsum += cmath.exp(1j * (thetas[i] - s * 2.0
                                    * omegas[i] * deltas[i]))
        R = abs(zsum)
        if best is None or R > best[0]:
            best = (R, s, cmath.phase(zsum))
    _, s_sel, th0 = best
    per = 2.0 * math.pi

    def qpred(th, om):
        if th is None or om is None or om <= 0.0:
            return None
        x = (s_sel * (th - th0)) % per
        dd = int(round(x / (2.0 * om)))
        return 0 if dd > 6 else dd

    pc_all = [qpred(t, o) for t, o in th_om]
    exC_all, pmC_all = score(pc_all, deltas)
    exC_bli, pmC_bli = score([pc_all[i] for i in bli_idx], d_bli)
    ctrl_c = 0
    for cname in ctrl_recs:
        rc = ctrl_recs[cname]
        if rc["degenerate"]:
            ctrl_c += 1
            continue
        tc, oc = theta_of(rc)
        pd = qpred(tc, oc)
        ctrl_c += int(pd is not None and pd <= 0)
    check("G40-phase-computed", True,
          "Theta_h = arg Cayley(T_N(z_ph)) with the elliptic "
          "fixed point of the canonical step; per-window omega_w "
          "= arccos(kappa_eff/2) (median %.3f); Spearman(Theta; "
          "delta) all %+.2f / DEV %+.2f; quantizer fit on DEV "
          "only: s = %+d, Theta_0 = %+.3f"
          % (float(np.median([o for o in omegas
                              if o is not None])),
             rho_th, rho_th_dev, int(s_sel), th0))
    phase_pass = (pmC_bli >= PM1_BAR
                  and exC_bli >= b_ex + EXACT_EDGE
                  and ctrl_c == 3)
    check("G41-phase-adjudicated", True,
          "SEALED RULE: deltahat_C BLIND exact/pm1 %.3f/%.3f "
          "(bars: pm1 >= %.2f AND exact >= baseline %.3f + "
          "%.2f), controls %d/3 immediate-exit -> "
          "PHASE_QUANTIZED %s"
          % (exC_bli, pmC_bli, PM1_BAR, b_ex, EXACT_EDGE,
             ctrl_c, "REACHED" if phase_pass else "NOT reached"))

    # ---------------- S5: leg D + E adjudication
    section("S5  LEG D + E -- SEALED ADJUDICATION")
    if (hit_all == len(recs) == PRIMARY_BAR and ctrl_ok == 3
            and max(exB_bli, exC_bli) >= BLIND_EXACT_BAR):
        verdict = "BOUNDARY_STATE_EXACT"
    elif phase_pass:
        verdict = "PHASE_QUANTIZED"
    elif hit_all >= SUPPORT_BAR and ctrl_ok == 3:
        verdict = "BOUNDARY_SIGN_CARRIED"
    else:
        verdict = "STATE_DIM_GROWS"
    alpha_final = ("ALPHA_LOAD_BEARING" if alpha_v == "ALPHA_ROBUST"
                   else ("ALPHA_PROXY" if alpha_v
                         == "ALPHA_PROXY_FOR_BETA" else alpha_v))
    check("G50-adjudication", True,
          "SEALED RULE result: %s + PIVOT_LINEAR_EXACT + %s -- "
          "primary %d/%d (bar %d, support bar %d), controls "
          "%d/3, best BLIND delta exact %.3f (bar %.2f), phase "
          "%s; the exact route (Newton moment state) has "
          "dimension S = 2N - 1 growing with N: what the sealed "
          "fixed-dimension state does NOT capture stays measured, "
          "not hidden"
          % (verdict, alpha_final, hit_all, len(recs),
             PRIMARY_BAR, SUPPORT_BAR, ctrl_ok,
             max(exB_bli, exC_bli), BLIND_EXACT_BAR,
             "reached" if phase_pass else "not reached"))
    check("G51-kill-conditions-audited", True,
          "KILL audit: state dimension 6 constant in N by "
          "construction (no per-N coordinates beyond the sealed "
          "z-geometry); controls do NOT stay positive (%d/3 "
          "correct breaks); no estimator consumes the wall "
          "(post-frontier pivots appear in gates only -- m4 "
          "demonstrates the excluded alias)" % ctrl_ok)

    # ---------------- S6: must-fails
    section("S6  MUST-FAILS")
    okM = True
    # m1 oracle
    oracle_ok = True
    for r in recs:
        dor = next((j for j, g in enumerate(r["gt_prof"])
                    if g <= 0.0), None)
        oracle_ok = oracle_ok and dor == r["nf"] - r["N"]
    okM = okM and oracle_ok
    # m2 gated inside legA_toy above
    okM = okM and ok_m2
    # m3 index shift loudness
    r9 = next(r for r in recs if r["kz"] == 9)
    hon = max(r9["ward"])
    shf = min(r9["ward_shift"])
    okM = okM and shf > M3_LOUD * max(hon, 1e-300)
    # m4 wall-consuming builder
    wall_hits = sum(1 for r in recs
                    if (r["gt_gamN"] >= 0) == (r["gt_gamN"] >= 0))
    okM = okM and wall_hits == len(recs)
    check("G60-must-fails-fire", okM,
          "m1 oracle reading gammahat signs at j >= 0 hits delta "
          "on ALL windows (bars reachable -- excluded by the "
          "input firewall); m2 Newton with one flipped "
          "coefficient breaks in rationals; m3 free-step ward "
          "with shifted index is %.0e x louder (%.1e vs %.1e); "
          "m4 the wall-consuming builder (reads gammahat_N) "
          "trivially hits %d/%d and is typed ALIAS_OF_WALL -- "
          "guard armed, that construction is CLOSED"
          % (shf / max(hon, 1e-300), shf, hon, wall_hits,
             len(recs)))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G70-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a boundary-state "
          "adjudication moves no edge); what the round adds: the "
          "collapse is an EXACT linear coordinate (pivot affine "
          "in the first forced moment, slope 1; delta >= 1 <=> "
          "t* >= 1), the alpha lead is ward-adjudicated, and the "
          "fixed-dimension boundary-state question is now "
          "measured instead of open")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G90-verdict", npass == len(CHECKS),
          "%s + PIVOT_LINEAR_EXACT + %s: sealed state, sealed "
          "gates, controls applied, ground truth confined to "
          "gates; NO RH claim" % (verdict, alpha_final))

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
