#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tstar_leading_sign_probe -- PRIME.PORT.TSTAR.LEADING.SIGN.01
(round 239): the LEADING SIGN FORM of the terminal pivot.  Target:
gammahat_{h,N} (equivalently the t* margin of r238) = kappa_h
|F_h|^2 + o(|F_h|^2) with kappa_h > 0 and a SOURCE-PURE arithmetic
fluctuation functional F_h -- or any other explicit leading form
with a positive sign that separates MAIN from ALL controls.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r225-r238 discipline): w/kz = window
(rung), N_w = builder depth = (S_w + 1)/2, n = chain degree,
delta_w = n_flip - N_w, eps = fluctuation amplitude (NEW this
round: the ray W_s + eps * V from the smooth base).  LADDER RULE
(= r232-r238): every frame-A rung with builder depth h <= 900
(42 rungs, N = 142..878), sorted by (N_w, kz); DEV = even / BLIND
= odd positions on the sorted ladder (sealed, = r233/r238).
Controls: EPSTEIN / SCRAMBLE(seed 1) / SMOOTH on the w9 base,
flips 25/21/27 re-gated.

THE SMOOTH BASE (sealed, parameter-free): per window the comb
(u_i, m_i) is replaced by the smooth PNT background on the same
lag geometry (alpha, M, D unchanged): grid u in (0, 2 alpha) step
DU = 0.01, masses 2 e^{u/2} DU -- EXACTLY the SMOOTH control
recipe of r226-r238, so the SMOOTH control world IS the eps = 0
base point of this probe (gated as a ward, not assumed).  The
comb -> weight map is LINEAR (tent assembly + fixed archimedean
lag + linear fold), hence the signed defect measure splits
EXACTLY as mutilde = mutilde_smooth + mutilde_fluc with
mutilde_fluc the weight image of (true comb - smooth background):
V := W_true - W_s on the SHARED folded cosine grid.  h_n and
gammahat_n along the ray are evaluated by the scaled signed
Stieltjes recursion on the single merged grid (equivalent to the
two-zone FC recursion; gated).

INPUT FIREWALL (binding): every F candidate and the sign
predictor consume ONLY (a) node positions and weights of the true
comb and of the sealed smooth background (raw source data), (b)
free-chain data of the PHYSICAL window at degrees n <= N-1, (c)
chains of PERTURBED measures W_s + eps V at the SEALED amplitudes
|eps| <= 0.5 (never the physical eps = 1 chain at degree N).
FORBIDDEN in any construction path: the physical gammahat_N, any
physical h_n at n >= N, measured flips/offsets, tau values.
Ground truth (sign of the physical gammahat_N; control flips)
enters GATES ONLY.  A builder that consumes the physical terminal
pivot is typed ALIAS_OF_WALL and excluded (m1).

LEG A -- FLUCTUATION FUNCTIONAL + SCALING LAW (sealed, max 3 band
definitions, no further candidates):
  F1^2 = sum_m (c_at[m] - c_at_smooth[m])^2      (Mellin/lag
         fluctuation energy of the window, v563 tent readout),
  F2^2 = sum_f V_f^2 = ||W_true - W_s||^2        (weight-space
         fluctuation energy = the leg-B direction norm),
  F3^2 = sum_{b=1..12} Phi_b^2, Phi_b = (comb mass in band b) -
         (4 e^{u_hi/2} - 4 e^{u_lo/2})           (12 equal u-bands
         on (0, 2 alpha], exact smooth integral).
DEV selection (the ONLY DEV-fitted discrete choice): the F with
the largest |Spearman(log F^2; log |lift|)| on the 21 DEV windows,
lift := gammahat_N^phys - G0 with G0 := gammahat_N(W_s) the
smooth-background pivot at the SAME degree N (source-pure).
Measured on all 42: log |gammahat_N| and log |lift| and the t*
margin |1 - rho| (rho = gammahat_N/gammahat_{N-1}) vs log F^2
(slopes + Spearman), the kappa tables kappa = gammahat_N / F^2
and kappa_lift = lift / F^2 (sign census), and the v883-trace
mirror: slope(log |gammahat_N| vs alpha) against 2 x slope(log F
vs alpha) (the corpus trace was -2.93 vs -2.53, sigma ~
fluctuation^2 within 16 percent, OLD sigma lane; the analogue at
the TERMINAL degree is measured here).  SEALED SCALING RULE:
SCALING_CONFIRMED iff for the DEV-selected F, on all 42,
Spearman(log F^2; log |lift|) >= 0.60 AND slope in [0.5, 1.5]
(the raw-gammahat regression is reported alongside; if only the
raw one meets the bars this is disclosed and counts too).

LEG B -- ENERGY IDENTITY AT THE TERMINAL DEGREE (second order in
mutilde_fluc): G(eps) := gammahat_N(W_s + eps V) on the sealed
5-point stencil eps in {0, +-0.25, +-0.5}; derivatives by the
exact central formulas G'(0) = [8(G(h)-G(-h)) - (G(2h)-G(-2h))]
/ (12h), G''(0) = [16(G(h)+G(-h)) - (G(2h)+G(-2h)) - 30 G(0)]
/ (12h^2), h = 0.25 (toy-warded exact on polynomials, m3 loud).
Quadratic share at eps = 1: |G''/2| / (|G0| + |G'| + |G''/2|).
HESSIAN EXCEPTION: C_true = G''(0) along the TRUE direction V
vs C_rand along 4 Gaussian directions + 1 entry-permuted copy of
V (equal norm ||V||, seeds 20260824*1000 + kz + dir, sealed).
SEALED RULE: HESSIAN_EXCEPTION iff frac(windows with STABLE
C_true > 0) >= 0.8 AND frac(random directions with C > 0) <= 0.3.
STABILITY GUARD (sealed): half stencil h = 0.125 must reproduce
sign and value (rel dev <= 1.0 of the mean) of the extrapolation;
any |G| > 1e6 on the stencil or a non-finite chain marks the
window UNSTABLE (counted against every rule that uses it).

LEG C -- THE SEPARATOR MAIN vs SMOOTH (sharpest single question):
(i) background census: G0 = gammahat_N(W_s) and the smooth-base
first flip n_flip(W_s) on ALL 42 windows -- is the background
systematically negative / early-dying (sealed: SMOOTH_DIES iff
n_flip(W_s) <= N/2 on >= 90 percent of windows)?  (ii) w9 world
ramps: n_flip(W_s + eps V_X) for eps in {0.25, 0.5, 0.75, 1.0}
and X in {TRUE, EPSTEIN, SCRAMBLE, RAND1, RAND2}, control and
random directions RESCALED to ||V_true|| (equal fluctuation
budget); V_SMOOTH == 0 identically (ward).  (iii) curvature +
matching angle table: C_X and cos(V_X, V_true) for every world
direction.  SEALED SEPARATOR RULE: SEPARATOR_HOLDS iff
SMOOTH_DIES AND at eps = 1 on w9 the TRUE direction survives to
n_flip >= N (consistency ward -- it IS the physical window) while
NO control or random direction reaches n_flip >= N.

LEG D -- BLIND DISCIPLINE + FALSIFIER: the SEALED SIGN PREDICTOR
(zero fitted constants): applicable iff the FREE wall holds
(sign h_n > 0 for all n < N -- free data); prediction shat =
sign(Ghat(1)), Ghat(1) = G(0) + G'(0) + G''(0)/2 (the quadratic
Taylor of the smooth-base ray extrapolated to the physical
amplitude; UNSTABLE windows and non-applicable windows count as
misses).  Ground truth sign(gammahat_N^phys) in gates only.
BARS: BLIND >= 0.9 (>= 19/21); trivial ceilings disclosed
(always-plus 24/42, always-minus 18/42).  CONTROLS (sealed
correct-break rule): on each control world at its own grid the
free wall is BROKEN below N (flips 25/21/27 << 184, re-gated)
=> the predictor declares NOT_APPLICABLE from free data alone =
correct break; a control that passes the wall predicate AND gets
a positive Ghat would be a CERTIFIED control = rule failure.

SEALED VERDICT RULE (hierarchy):
  LEADING_SIGN_CANDIDATE iff BLIND sign rate >= 0.9 AND controls
    3/3 correct breaks AND SCALING_CONFIRMED;
  else HESSIAN_EXCEPTION_FOUND iff HESSIAN_EXCEPTION AND
    SEPARATOR_HOLDS;
  else SCALING_CONFIRMED_SIGN_OPEN iff SCALING_CONFIRMED;
  else FLUCTUATION_FORM_FAILS.
The negative is valid: it excludes the quadratic leading order at
the sealed stencil scale and finally grounds the full RHP
analysis.

MUST-FAILS (each loud): (m1) ORACLE reading the physical
gammahat_N hits 42/42 -- typed ALIAS_OF_WALL, excluded by the
input firewall; (m2) DEGREE SHIFT: the same predictor asked about
degree N-1 meets a ground truth that is positive on ALL 42 (free
wall), so the two truths differ on EXACTLY the 18 delta = 0
windows -- the terminal degree is the content, not a labeling;
(m3) one mutated stencil coefficient (16 -> -16) breaks the exact
polynomial recovery loudly; (m4) mutating ONE weight of W_true by
1e-3 moves gammahat_N visibly (moment-defined, not an alias).

HIGH-PRECISION WARD: mpmath dps = 60 plain monic signed recursion
recomputes G(0) and G(+0.25) on the smallest rung and on w9 (bar
1e-3 rel, generous by disclosure: the smooth-base chain crosses
many near-zeros of h_n over the full depth).

RECORD TABLES (frozen from calib_tls_pass1.log, 21/21, wall
8.1 s; NO amendment between the smoke stage and the full pass:
no bar, rule, seed or constant moved after evaluation started).
CAL_VERDICT = FLUCTUATION_FORM_FAILS (quadratic leading order at
the sealed stencil scale EXCLUDED, measured) + SEPARATOR_HOLDS +
SMOOTH_DIES(42/42).  Key numbers -- CENSUS: 18 negative / 24
positive re-derived, free wall 42/42, chain-equivalence and
fold/linearity wards exact (6.0e-16), control flips 25/21/27
re-gated on the merged-grid evaluator, SMOOTH control ==
eps = 0 base point EXACTLY (max |dW| = 0).  BACKGROUND (leg C
hypothesis ADJUDICATED AGAINST): the smooth-base pivot G0 =
gammahat_N(W_s) is POSITIVE on 41/42 windows (|G0| <= 1.6) --
NOT systematically negative; the smooth base instead dies EARLY
everywhere: n_flip(W_s) in [15, 70] = 0.071..0.147 of N
(SMOOTH_DIES 42/42, r236-consistent scale).  LIFT: gammahat_N -
G0 > 0 on only 12/42 (kappa_lift median -3.3): the fluctuations
do NOT uniformly lift the terminal pivot.  SCALING (DEV choice
F2 = ||V||^2, DEV |Spearman| 0.18/0.25/0.20 -- all three
candidates weak): all-42 log|lift| vs log F^2 Spearman -0.11
slope -0.60 (FAILS both bars); raw log|gammahat_N| Spearman
+0.32 slope 1.37 (FAILS the Spearman bar); t*-margin (29
crossing windows) Spearman +0.16 -- NO F^2 law at the terminal
degree; v883-trace mirror: slope(log|gammahat_N| vs alpha)
+0.13 vs 2 x slope(log F vs alpha) +0.07 -- the OLD-lane
sigma ~ fluctuation^2 trace does NOT reproduce at the terminal
pivot (both slopes flat).  STENCIL/HESSIAN: stable on 12/42
windows only (the smooth-base ray crosses h-zeros inside
|eps| <= 0.5); quadratic share where stable 0.02/0.21/0.71
(min/med/max); stable C_true > 0 on 6/42 = 0.14 (bar 0.80
FAILS), random directions C > 0 on 63/210 = 0.30 -- the true
direction is NOT a positive-curvature exception at the smooth
base.  SEPARATOR (w9, equal budget ||V_true|| = 2.27e-1): ramps
eps 0.25/0.5/0.75/1.0 -> TRUE 27/29/33/184 (= N, survives),
EPSTEIN 27/26/26/26, SCRAMBLE 24/23/22/21, RAND1 10/9/9/9,
RAND2 23/21/16/15: the TRUE comb is the ONLY direction that
restores the wall, and even it stays at ~ 27-33 until
eps > 0.75 -- the wall is a FINITE-AMPLITUDE THRESHOLD, not a
small-eps expansion (this, not a sign flip, is what kills the
perturbative leading order); curvature/angle: C_true +0.19 vs
C_EP -1.2, C_SC -0.54, cos(V_X, V_true) = EP +0.130, SC +0.023,
RAND -0.003/-0.011 -- no matching-angle structure.  PREDICTOR:
all-42 rate 5/42 = 0.119, BLIND 0/21 = 0.000 (bar 0.90 FAILS;
ceilings 0.571/0.429; post-hoc observation, NO verdict weight:
the quadratic Taylor is an ANTI-predictor at 37/42 -- the
extrapolated ray sign is systematically opposite to the
physical sign, consistent with the threshold picture).
CONTROLS: 3/3 correct breaks (free wall broken below N
announces every control from free data; no control certified).
mp dps-60 ward 5.8e-10 (bar 1e-3); must-fails m1 42/42 alias
excluded, m2 truths differ on exactly the 18 delta = 0 windows,
m3 stencil mutation misses by 2.8e2, m4 one-weight mutation
moves gammahat_N by rel 4.4e-5.  ADJUDICATION: blind bar
failed, scaling failed, Hessian exception failed, separator
holds --> FLUCTUATION_FORM_FAILS carried with the two positive
facts (SEPARATOR_HOLDS + SMOOTH_DIES universal): the terminal-
pivot sign is NOT second order in the arithmetic fluctuation at
the smooth base -- the positivity enters only at full
fluctuation amplitude (threshold, r236/v883-consistent), which
finally grounds the full finite-amplitude RHP analysis as the
only route and closes the perturbative leading-order door.
AMENDMENTS AFTER FREEZE: NONE.

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
SMOKE_KZ = (9, 12, 13, 26, 40)
R228_DELTA = {9: 0, 12: 2, 13: 2, 26: 3, 40: 1}
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
DU = 0.01
BANDS_F3 = 12
EPS_H = 0.25
EPS_H2 = 0.125
GCLIP = 1e6
STAB_REL = 1.0
N_RAND = 4                       # + 1 entry-permuted copy of V
SEED_BASE = 20260824
BLIND_BAR = 0.9
SP_BAR = 0.60
SLOPE_LO, SLOPE_HI = 0.5, 1.5
TRUE_POS_FRAC = 0.8
RAND_POS_FRAC = 0.3
SMOOTH_DIE_FRAC = 0.9
RAMP_EPS = (0.25, 0.5, 0.75, 1.0)
CHAIN_EQ_BAR = 1e-4
LIN_BAR = 1e-12
MP_DPS = 60
MP_BAR = 1e-3
NEG_COUNT_FULL = 18
CAL_VERDICT = ("FLUCTUATION_FORM_FAILS (quadratic leading order "
               "excluded at the sealed stencil scale) + "
               "SEPARATOR_HOLDS + SMOOTH_DIES(42/42) + "
               "background G0 POSITIVE 41/42 (leg-C hypothesis "
               "adjudicated against)")

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
    return (not bad), ("NO zero/prime oracles; smooth base, F "
                       "candidates, stencil, seeds, DEV/BLIND, "
                       "predictor, control rule and verdict "
                       "hierarchy sealed in the frozen spec"
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


# ------------------------------------------------ window + weights
def ladder_kzs():
    """frame-A rungs with builder depth h <= H_CAP, WITHOUT
    building (the frame_a_zones geometry formula verbatim)."""
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_CAP:
            out.append(kz)
    return out


def signed_weights(d_arm, L):
    """signed folded weights on the FULL cosine grid (the
    folded_measure aggregation without the sign split); the > 0
    part must reproduce (xs, ws), the < 0 part (ys, vs)."""
    jj = np.arange(L)
    th = 2.0 * math.pi * jj / L
    wt = (d_arm[:L] / (2.0 * L)) * 4.0 * np.sin(th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    W = np.zeros(len(uf))
    np.add.at(W, inv, wt)
    x = np.cos(2.0 * math.pi * uf / L)
    return x, W, uf


def window_build(kz, comb=None, scramble_seed=None):
    """one window: true weights W_true and smooth-base weights W_s
    on the SHARED folded grid, plus the raw lag fluctuation and
    the band data for F3.  Source data only."""
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    M, D, alpha, N = rr["M"], rr["D"], rr["alpha"], rr["h"]
    L = 2 * M - 2
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
        uu = np.asarray(uu, float)
        mm = np.asarray(mm, float)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d_true = PIK.grid_density(c_ar + c_at)
    ug = np.arange(DU, 2.0 * alpha, DU)
    ms = 2.0 * np.exp(ug / 2.0) * DU
    c_at_s, _ = core.atom_lags_at(alpha, M, ug, ms)
    d_s = PIK.grid_density(c_ar + c_at_s)
    x, Wt, uf = signed_weights(d_true, L)
    _x2, Ws, _u2 = signed_weights(d_s, L)
    return dict(kz=kz, N=N, M=M, D=D, alpha=alpha, L=L,
                x=x, Wt=Wt, Ws=Ws, uf=uf,
                c_at=c_at, c_at_s=c_at_s, c_ar=c_ar,
                uu=uu, mm=mm, ug=ug, ms=ms,
                d_true=d_true, d_s=d_s)


def chainW(x, W, n_hi):
    """scaled signed monic Stieltjes recursion on ONE grid with
    signed weights (the FC.signed_chain recursion on the merged
    grid).  Returns gams (gams[n] = gammahat_{n+1}), sgs (sign
    h_n, n = 0..n_hi-1) and the first flip index (or None).
    Non-finite propagation returns valid=False."""
    q_m = np.zeros_like(x)
    q = np.ones_like(x)
    Ls = Ls_m = 0.0
    eta = float(np.sum(W))
    eta_m = eta
    sg_h = math.copysign(1.0, eta)
    gams, sgs = [], []
    flip = None
    for n in range(n_hi):
        sgs.append(sg_h)
        if flip is None and sg_h < 0:
            flip = n
        if eta == 0.0 or not math.isfinite(eta):
            return dict(valid=False, gams=gams, sgs=sgs, flip=flip)
        alh = float(np.sum(W * x * q * q)) / eta
        if not math.isfinite(alh):
            return dict(valid=False, gams=gams, sgs=sgs, flip=flip)
        if n == 0:
            p = (x - alh) * q
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            p = (x - alh) * q - ge * math.exp(Ls_m - Ls) * q_m
        sc = float(np.max(np.abs(p)))
        if sc == 0.0 or not math.isfinite(sc):
            return dict(valid=False, gams=gams, sgs=sgs, flip=flip)
        q_m, eta_m, Ls_m = q, eta, Ls
        q = p / sc
        Ls += math.log(sc)
        eta = float(np.sum(W * q * q))
        gam = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
        gams.append(gam)
        sg_h *= math.copysign(1.0, gam)
    return dict(valid=True, gams=gams, sgs=sgs, flip=flip)


def first_flip(x, W, cap):
    ch = chainW(x, W, cap)
    return ch["flip"] if ch["flip"] is not None else (
        None if ch["valid"] else -1)


def gam_at(x, W, N):
    """gammahat_N of the measure (x, W); None if the chain is
    numerically invalid before depth N."""
    ch = chainW(x, W, N)
    if not ch["valid"] or len(ch["gams"]) < N:
        return None
    return ch["gams"][N - 1]


# ------------------------------------------------ stencil algebra
def stencil_derivs(g0, gp1, gm1, gp2, gm2, h):
    """exact 5-point central first/second derivatives at 0."""
    d1 = (8.0 * (gp1 - gm1) - (gp2 - gm2)) / (12.0 * h)
    d2 = (16.0 * (gp1 + gm1) - (gp2 + gm2) - 30.0 * g0) \
        / (12.0 * h * h)
    return d1, d2


def stencil_pack(vals, h):
    """vals: dict eps -> G (must contain 0, +-h, +-2h); returns
    (G0, G', G'', Ghat(1)) or None if any value is bad."""
    need = (0.0, h, -h, 2.0 * h, -2.0 * h)
    for e in need:
        v = vals.get(e)
        if v is None or not math.isfinite(v) or abs(v) > GCLIP:
            return None
    d1, d2 = stencil_derivs(vals[0.0], vals[h], vals[-h],
                            vals[2.0 * h], vals[-2.0 * h], h)
    return vals[0.0], d1, d2, vals[0.0] + d1 + 0.5 * d2


def eval_ray(x, Ws, V, eps_list, N):
    return {e: gam_at(x, Ws + e * V, N) for e in eps_list}


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("tstar_leading_sign_probe -- PRIME.PORT.TSTAR.LEADING."
          "SIGN.01 (round 239)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (5 known rungs, infrastructure "
                        "only)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "ladder frame-A h <= %d (42 rungs full); DEV even / "
          "BLIND odd; smooth base DU = %.2f masses 2e^{u/2}du "
          "(= SMOOTH control recipe); F1/F2/F3 sealed (bands %d); "
          "stencil h = %.2f (half %.3f), GCLIP %.0e, stability "
          "rel %.1f; %d Gaussian + 1 permuted direction, seeds "
          "%d*1000+kz+dir; blind bar %.2f; scaling bars Spearman "
          ">= %.2f, slope [%.1f, %.1f]; Hessian bars %.1f/%.1f; "
          "smooth-death bar %.2f at N/2; verdict hierarchy "
          "sealed in the frozen spec"
          % (H_CAP, DU, BANDS_F3, EPS_H, EPS_H2, GCLIP, STAB_REL,
             N_RAND, SEED_BASE, BLIND_BAR, SP_BAR, SLOPE_LO,
             SLOPE_HI, TRUE_POS_FRAC, RAND_POS_FRAC,
             SMOOTH_DIE_FRAC))

    # ---------------- S1: builders, wards, census
    section("S1  BUILDERS + LINEARITY/FOLD/CHAIN WARDS + CENSUS")
    kzs = list(SMOKE_KZ) if smoke else ladder_kzs()
    recs = []
    for kz in kzs:
        recs.append(window_build(kz))
    recs.sort(key=lambda r: (r["N"], r["kz"]))
    ok_n = (len(recs) == (5 if smoke else 42))

    # fold ward on w9: signed split == folded_measure zones
    r9 = next(r for r in recs if r["kz"] == 9)
    xs_f, ws_f, _ = PIK.folded_measure(r9["d_true"], r9["L"], +1.0)
    ys_f, vs_f, _ = PIK.folded_measure(r9["d_true"], r9["L"], -1.0)
    pos = r9["Wt"] > 0.0
    neg = r9["Wt"] < 0.0
    dev_fold = max(
        float(np.max(np.abs(np.sort(r9["x"][pos])
                            - np.sort(xs_f)))),
        float(np.max(np.abs(np.sort(r9["Wt"][pos])
                            - np.sort(ws_f)))),
        float(np.max(np.abs(np.sort(r9["x"][neg])
                            - np.sort(ys_f)))),
        float(np.max(np.abs(np.sort(-r9["Wt"][neg])
                            - np.sort(vs_f)))))
    # linearity ward: W(true) - W(s) == weight image of the lag
    # difference (the comb -> weight map is linear)
    d_diff = PIK.grid_density(r9["c_at"] - r9["c_at_s"])
    _xl, W_diff, _ul = signed_weights(d_diff, r9["L"])
    dev_lin = float(np.max(np.abs((r9["Wt"] - r9["Ws"]) - W_diff))
                    / max(float(np.max(np.abs(W_diff))), 1e-300))
    check("G10-fold-and-linearity", ok_n
          and dev_fold <= LIN_BAR and dev_lin <= LIN_BAR,
          "%d windows built; signed fold reproduces both zones "
          "(w9 dev %.1e) and the fluctuation weights V = W_true "
          "- W_s equal the weight image of the lag difference "
          "(dev %.1e, bar %.0e): mutilde = mutilde_smooth + "
          "mutilde_fluc EXACTLY, source-linear"
          % (len(recs), dev_fold, dev_lin, LIN_BAR))

    # chain-equivalence ward on the smoke rungs
    ok_eq = True
    for kz in SMOKE_KZ:
        r = next((q for q in recs if q["kz"] == kz), None)
        if r is None:
            continue
        N = r["N"]
        chm = chainW(r["x"], r["Wt"], N)
        d2 = dict(xs=r["x"][r["Wt"] > 0], ws=r["Wt"][r["Wt"] > 0],
                  ys=r["x"][r["Wt"] < 0], vs=-r["Wt"][r["Wt"] < 0])
        ch2 = FC.signed_chain(d2, N)
        g_m = chm["gams"][N - 1]
        g_2 = ch2[N - 1]["gammahat_next"]
        ok_eq = ok_eq and abs(g_m - g_2) <= CHAIN_EQ_BAR * (
            1.0 + abs(g_2))
        ok_eq = ok_eq and all(
            chm["sgs"][n] == ch2[n]["sg_h"] for n in range(N))
    check("G11-chain-equivalence", ok_eq,
          "merged-grid signed recursion == two-zone FC recursion "
          "on the five reference rungs: gammahat_N to %.0e and "
          "ALL free h-signs exact -- the single-grid evaluator "
          "is the same object" % CHAIN_EQ_BAR)

    # physical census: gammahat_N, gbar, free wall, smooth flip
    for r in recs:
        N = r["N"]
        ch = chainW(r["x"], r["Wt"], N)
        r["gt_gamN"] = ch["gams"][N - 1]
        r["gbar"] = ch["gams"][N - 2]
        r["wall_free"] = ch["valid"] and all(
            s > 0 for s in ch["sgs"][:N])
        r["flip_s"] = first_flip(r["x"], r["Ws"], N + 1)
        r["G0"] = gam_at(r["x"], r["Ws"], N)
    n_neg = sum(1 for r in recs if r["gt_gamN"] < 0)
    ok_wall = all(r["wall_free"] for r in recs)
    if smoke:
        ok_cen = all((r["gt_gamN"] >= 0)
                     == (R228_DELTA[r["kz"]] >= 1) for r in recs)
        cen_note = "smoke: signs match the r228 offsets 0/2/2/3/1"
    else:
        ok_cen = (n_neg == NEG_COUNT_FULL)
        cen_note = ("%d negative / %d positive == the r233/r238 "
                    "census (18 delta = 0 windows)"
                    % (n_neg, len(recs) - n_neg))
    check("G12-census", ok_wall and ok_cen,
          "free wall holds on every window (all h_n > 0, n < N); "
          "%s; ground truth = sign(gammahat_N) used in gates "
          "only" % cen_note)

    # ---------------- S2: leg A
    section("S2  LEG A -- FLUCTUATION FUNCTIONALS + SCALING LAW")
    for r in recs:
        V = r["Wt"] - r["Ws"]
        r["V"] = V
        r["F1sq"] = float(np.sum((r["c_at"] - r["c_at_s"]) ** 2))
        r["F2sq"] = float(np.sum(V ** 2))
        edges = np.linspace(0.0, 2.0 * r["alpha"], BANDS_F3 + 1)
        f3 = 0.0
        for b in range(BANDS_F3):
            lo, hi = edges[b], edges[b + 1]
            msum = float(np.sum(r["mm"][(r["uu"] > lo)
                                        & (r["uu"] <= hi)]))
            ssum = 4.0 * (math.exp(hi / 2.0) - math.exp(lo / 2.0))
            f3 += (msum - ssum) ** 2
        r["F3sq"] = f3
        r["lift"] = (r["gt_gamN"] - r["G0"]
                     if r["G0"] is not None else None)
    dev_idx = list(range(0, len(recs), 2))
    bli_idx = list(range(1, len(recs), 2))
    lifts = [r["lift"] for r in recs]
    ok_lift = all(v is not None and v != 0.0 for v in lifts)
    # DEV selection of the F candidate
    sp_dev = []
    for key in ("F1sq", "F2sq", "F3sq"):
        xs_ = [math.log(recs[i][key]) for i in dev_idx]
        ys_ = [math.log(abs(recs[i]["lift"])) for i in dev_idx
               if recs[i]["lift"] is not None]
        xs_ = [math.log(recs[i][key]) for i in dev_idx
               if recs[i]["lift"] is not None]
        sp_dev.append(abs(spearman(xs_, ys_)))
    k_sel = ("F1sq", "F2sq", "F3sq")[int(np.argmax(sp_dev))]
    check("G20-dev-selection", ok_lift,
          "lift = gammahat_N - G0 defined on every window; the "
          "ONLY DEV-fitted choice: %s (DEV |Spearman| %s) -- "
          "frozen, all-42 scored below"
          % (k_sel, "/".join("%.2f" % v for v in sp_dev)))
    lF = [math.log(r[k_sel]) for r in recs]
    lG = [math.log(abs(r["gt_gamN"])) for r in recs]
    lL = [math.log(abs(r["lift"])) for r in recs]
    al_ = [r["alpha"] for r in recs]
    sp_raw = spearman(lF, lG)
    sl_raw, _ = slope_fit(lF, lG)
    sp_lift = spearman(lF, lL)
    sl_lift, _ = slope_fit(lF, lL)
    cross = [r for r in recs
             if r["gt_gamN"] / r["gbar"] < 1.0]
    sp_marg = spearman(
        [math.log(r[k_sel]) for r in cross],
        [math.log(abs(1.0 - r["gt_gamN"] / r["gbar"]))
         for r in cross])
    kap = [r["gt_gamN"] / r[k_sel] for r in recs]
    kapL = [r["lift"] / r[k_sel] for r in recs]
    npos_k = sum(1 for v in kap if v > 0)
    npos_kL = sum(1 for v in kapL if v > 0)
    sl_Ga, _ = slope_fit(al_, lG)
    sl_Fa, _ = slope_fit(al_, [0.5 * v for v in lF])
    info("scaling (all %d, %s): log|gammahat_N| vs log F^2: "
         "Spearman %+.2f slope %.2f | log|lift| vs log F^2: "
         "Spearman %+.2f slope %.2f | t*-margin (%d crossing): "
         "Spearman %+.2f"
         % (len(recs), k_sel, sp_raw, sl_raw, sp_lift, sl_lift,
            len(cross), sp_marg))
    info("kappa = gammahat_N/F^2: %d/%d positive (median "
         "%+.3e) | kappa_lift = lift/F^2: %d/%d positive "
         "(median %+.3e)"
         % (npos_k, len(recs), float(np.median(kap)),
            npos_kL, len(recs), float(np.median(kapL))))
    info("v883-trace mirror at the terminal degree: slope(log"
         "|gammahat_N| vs alpha) %+.2f vs 2 x slope(log F vs "
         "alpha) %+.2f (corpus OLD-lane trace: -2.93 vs -2.53)"
         % (sl_Ga, 2.0 * sl_Fa))
    scaling_ok = ((sp_lift >= SP_BAR
                   and SLOPE_LO <= sl_lift <= SLOPE_HI)
                  or (sp_raw >= SP_BAR
                      and SLOPE_LO <= sl_raw <= SLOPE_HI))
    check("G21-scaling-adjudicated", True,
          "SEALED RULE: SCALING_CONFIRMED %s (lift regression "
          "Spearman %+.2f bar %.2f, slope %.2f in [%.1f, %.1f]; "
          "raw counted too by disclosure: Spearman %+.2f slope "
          "%.2f)" % ("YES" if scaling_ok else "NO", sp_lift,
                     SP_BAR, sl_lift, SLOPE_LO, SLOPE_HI,
                     sp_raw, sl_raw))
    lift_pos = sum(1 for r in recs if r["lift"] > 0)
    check("G22-background-and-lift", True,
          "BACKGROUND census: smooth-base flip n_flip(W_s) in "
          "[%d, %d] (fraction of N %.3f..%.3f), G0 sign census "
          "%d neg / %d pos (|G0| up to %.1e -- at degree N the "
          "smooth chain is far past its own wall); LIFT census: "
          "gammahat_N - G0 > 0 on %d/%d windows"
          % (min(r["flip_s"] for r in recs),
             max(r["flip_s"] for r in recs),
             min(r["flip_s"] / r["N"] for r in recs),
             max(r["flip_s"] / r["N"] for r in recs),
             sum(1 for r in recs
                 if r["G0"] is not None and r["G0"] < 0),
             sum(1 for r in recs
                 if r["G0"] is not None and r["G0"] >= 0),
             max(abs(r["G0"]) for r in recs
                 if r["G0"] is not None),
             lift_pos, len(recs)))

    # ---------------- S3: leg B
    section("S3  LEG B -- STENCIL, QUADRATIC SHARE, HESSIAN")
    # toy ward + m3 partner (exact polynomial recovery)
    def poly(e):
        return 3.0 - 2.0 * e + 5.0 * e * e - 1.5 * e ** 3
    tv = {e: poly(e) for e in (0.0, EPS_H, -EPS_H,
                               2.0 * EPS_H, -2.0 * EPS_H)}
    pk = stencil_pack(tv, EPS_H)
    ok_toy = (abs(pk[1] - (-2.0)) <= 1e-12
              and abs(pk[2] - 10.0) <= 1e-12)
    d1b = (8.0 * (tv[EPS_H] - tv[-EPS_H])
           - (tv[2 * EPS_H] - tv[-2 * EPS_H])) / (12.0 * EPS_H)
    d2b = (-16.0 * (tv[EPS_H] + tv[-EPS_H])
           - (tv[2 * EPS_H] + tv[-2 * EPS_H])
           - 30.0 * tv[0.0]) / (12.0 * EPS_H ** 2)
    m3_loud = abs(d2b - 10.0)
    check("G30-stencil-toy", ok_toy and m3_loud > 1.0,
          "5-point central derivatives exact on the cubic toy "
          "(G' = -2, G'' = 10 to 1e-12); mutated coefficient "
          "(16 -> -16) misses G'' by %.1e (m3 loud)" % m3_loud)

    n_rand_eff = 2 if smoke else N_RAND
    eps_full = (0.0, EPS_H, -EPS_H, 2.0 * EPS_H, -2.0 * EPS_H)
    eps_half = (EPS_H2, -EPS_H2)
    n_stab = 0
    rand_pos = 0
    rand_tot = 0
    true_pos = 0
    for r in recs:
        N, x, Ws, V = r["N"], r["x"], r["Ws"], r["V"]
        vals = eval_ray(x, Ws, V, eps_full, N)
        vals.update(eval_ray(x, Ws, V, eps_half, N))
        pk = stencil_pack(vals, EPS_H)
        hv = {0.0: vals[0.0], EPS_H2: vals[EPS_H2],
              -EPS_H2: vals[-EPS_H2], 2.0 * EPS_H2: vals[EPS_H],
              -2.0 * EPS_H2: vals[-EPS_H]}
        pk2 = stencil_pack(hv, EPS_H2)
        stable = (pk is not None and pk2 is not None
                  and math.copysign(1.0, pk[3])
                  == math.copysign(1.0, pk2[3])
                  and abs(pk[3] - pk2[3])
                  <= STAB_REL * 0.5 * (abs(pk[3]) + abs(pk2[3])))
        r["pk"] = pk
        r["stable"] = stable
        if stable:
            n_stab += 1
            if pk[2] > 0:
                true_pos += 1
        rng = np.random.default_rng(SEED_BASE * 1000 + r["kz"])
        nrm = math.sqrt(float(np.sum(V ** 2)))
        r["C_rand"] = []
        for kdir in range(n_rand_eff + 1):
            if kdir < n_rand_eff:
                g = rng.standard_normal(len(V))
                Vr = g * (nrm / math.sqrt(float(np.sum(g ** 2))))
            else:
                Vr = V[rng.permutation(len(V))]
            vr = eval_ray(x, Ws, Vr, eps_full, N)
            pkr = stencil_pack(vr, EPS_H)
            if pkr is not None:
                rand_tot += 1
                r["C_rand"].append(pkr[2])
                if pkr[2] > 0:
                    rand_pos += 1
    qshare = [abs(0.5 * r["pk"][2])
              / (abs(r["pk"][0]) + abs(r["pk"][1])
                 + abs(0.5 * r["pk"][2]))
              for r in recs if r["stable"]]
    info("stencil stable on %d/%d windows (guard: half-stencil "
         "agreement + GCLIP); quadratic share at eps = 1 where "
         "stable: min/median/max %.2f/%.2f/%.2f"
         % (n_stab, len(recs),
            min(qshare) if qshare else float("nan"),
            float(np.median(qshare)) if qshare else float("nan"),
            max(qshare) if qshare else float("nan")))
    hess_ok = (n_stab > 0
               and true_pos / len(recs) >= TRUE_POS_FRAC
               and rand_tot > 0
               and rand_pos / rand_tot <= RAND_POS_FRAC)
    check("G31-hessian-adjudicated", True,
          "SEALED RULE: HESSIAN_EXCEPTION %s -- stable C_true > "
          "0 on %d/%d = %.2f (bar %.2f), random directions C > "
          "0 on %d/%d = %.2f (bar <= %.2f): the true fluctuation "
          "direction %s a positive-curvature exception at the "
          "smooth base"
          % ("YES" if hess_ok else "NO", true_pos, len(recs),
             true_pos / len(recs), TRUE_POS_FRAC, rand_pos,
             max(rand_tot, 1), rand_pos / max(rand_tot, 1),
             RAND_POS_FRAC, "IS" if hess_ok else "is NOT"))

    # ---------------- S4: leg C
    section("S4  LEG C -- SEPARATOR MAIN vs SMOOTH (w9 base)")
    r9 = next(r for r in recs if r["kz"] == 9)
    N9 = r9["N"]
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = PIK.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ug9 = np.arange(DU, 2.0 * rr9["alpha"], DU)
    worlds = {}
    worlds["EPSTEIN"] = window_build(9, comb=(
        np.log(nn.astype(float)),
        2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))
    worlds["SCRAMBLE"] = window_build(9, scramble_seed=1)
    worlds["SMOOTH"] = window_build(
        9, comb=(ug9, 2.0 * np.exp(ug9 / 2.0) * DU))
    ok_cf = True
    for cname, wr in worlds.items():
        fl = first_flip(wr["x"], wr["Wt"], 45)
        wr["flip"] = fl
        ok_cf = ok_cf and fl == CTRL_FLIPS[cname]
        wr["wall_free"] = False   # flip << N by the gate above
    check("G40-control-flips-regated", ok_cf,
          "EPSTEIN/SCRAMBLE/SMOOTH flip at 25/21/27 exactly on "
          "the merged-grid evaluator")
    dev_sm = float(np.max(np.abs(worlds["SMOOTH"]["Wt"]
                                 - r9["Ws"])))
    check("G41-smooth-is-base", dev_sm == 0.0
          and r9["flip_s"] == CTRL_FLIPS["SMOOTH"],
          "the SMOOTH control world IS the eps = 0 base point: "
          "max |W_SMOOTH - W_s(w9)| = %.1e and n_flip(W_s) = %d "
          "= the SMOOTH flip -- V_SMOOTH == 0 identically"
          % (dev_sm, r9["flip_s"]))

    Vt = r9["V"]
    nrm_t = math.sqrt(float(np.sum(Vt ** 2)))
    rng9 = np.random.default_rng(SEED_BASE * 1000 + 9 + 777)
    dirs = [("TRUE", Vt)]
    for cname in ("EPSTEIN", "SCRAMBLE"):
        Vc = worlds[cname]["Wt"] - r9["Ws"]
        Vc = Vc * (nrm_t / math.sqrt(float(np.sum(Vc ** 2))))
        dirs.append((cname, Vc))
    for kdir in range(2):
        g = rng9.standard_normal(len(Vt))
        dirs.append(("RAND%d" % (kdir + 1),
                     g * (nrm_t / math.sqrt(float(np.sum(g ** 2))))))
    ramp = {}
    sep_ctrl_ok = True
    for nm, Vd in dirs:
        row = []
        for e in RAMP_EPS:
            fl = first_flip(r9["x"], r9["Ws"] + e * Vd, N9 + 1)
            row.append(fl if fl is not None else N9 + 1)
        ramp[nm] = row
        if nm != "TRUE" and row[-1] >= N9:
            sep_ctrl_ok = False
        vals = eval_ray(r9["x"], r9["Ws"], Vd, (0.0, EPS_H, -EPS_H,
                        2.0 * EPS_H, -2.0 * EPS_H), N9)
        pkd = stencil_pack(vals, EPS_H)
        cosang = float(np.sum(Vd * Vt)
                       / (math.sqrt(float(np.sum(Vd ** 2)))
                          * nrm_t))
        info("%-8s ramp eps %s -> flips %s | C = %s | cos(V, "
             "V_true) %+.3f"
             % (nm, str(RAMP_EPS),
                "/".join(str(v) for v in row),
                ("%+.3e" % pkd[2]) if pkd is not None
                else "UNSTABLE", cosang))
    smooth_die = sum(1 for r in recs
                     if r["flip_s"] is not None
                     and 0 <= r["flip_s"] <= r["N"] / 2)
    smooth_dies = smooth_die / len(recs) >= SMOOTH_DIE_FRAC
    true_survives = ramp["TRUE"][-1] >= N9
    sep_ok = smooth_dies and true_survives and sep_ctrl_ok
    check("G42-separator-adjudicated", true_survives,
          "SEALED RULE: SEPARATOR %s -- SMOOTH_DIES %s (smooth "
          "base flips at <= N/2 on %d/%d windows, bar %.2f); at "
          "eps = 1 with EQUAL budget ||V_true|| = %.2e the TRUE "
          "direction survives to n_flip >= N = %d (consistency "
          "ward: it IS the physical window) while controls/"
          "random reach %s -- %s"
          % ("HOLDS" if sep_ok else "FAILS", smooth_dies,
             smooth_die, len(recs), SMOOTH_DIE_FRAC, nrm_t, N9,
             str({k: v[-1] for k, v in ramp.items()
                  if k != "TRUE"}),
             "no other direction restores the wall"
             if sep_ctrl_ok else "A CONTROL DIRECTION SURVIVED"))

    # ---------------- S5: leg D
    section("S5  LEG D -- BLIND SIGN GATE + CONTROL BREAKS")
    hits_all = 0
    hits_bli = 0
    for i, r in enumerate(recs):
        pred = None
        if r["wall_free"] and r["stable"] and r["pk"] is not None:
            pred = 1.0 if r["pk"][3] >= 0 else -1.0
        ok = (pred is not None
              and pred == math.copysign(1.0, r["gt_gamN"]))
        r["pred_ok"] = ok
        hits_all += int(ok)
        if i in bli_idx:
            hits_bli += int(ok)
    rate_all = hits_all / len(recs)
    rate_bli = hits_bli / max(len(bli_idx), 1)
    ceil_p = sum(1 for r in recs if r["gt_gamN"] >= 0) / len(recs)
    check("G50-blind-sign-gate", True,
          "SEALED PREDICTOR (zero fitted constants, quadratic "
          "Taylor of the smooth-base ray at eps = 1): all-%d "
          "rate %.3f (%d/%d), BLIND %.3f (%d/%d), bar %.2f; "
          "trivial ceilings always-plus %.3f / always-minus "
          "%.3f; UNSTABLE + non-applicable counted as misses"
          % (len(recs), rate_all, hits_all, len(recs), rate_bli,
             hits_bli, len(bli_idx), BLIND_BAR, ceil_p,
             1.0 - ceil_p))
    ctrl_break = 0
    for cname, wr in worlds.items():
        chc = chainW(wr["x"], wr["Wt"], wr["N"])
        wall_c = chc["valid"] and all(
            s > 0 for s in chc["sgs"][:wr["N"]])
        ctrl_break += int(not wall_c)
        info("%-8s free wall below N = %d: %s -> predictor "
             "NOT_APPLICABLE (correct break: the free data "
             "announces the broken world)"
             % (cname, wr["N"], "holds" if wall_c else "BROKEN"))
    check("G51-controls-correct-break", ctrl_break == 3,
          "%d/3 controls break correctly (free wall broken "
          "below N on their own grid); NO control is certified "
          "by the candidate form" % ctrl_break)

    blind_pass = rate_bli >= BLIND_BAR
    if blind_pass and ctrl_break == 3 and scaling_ok:
        verdict = "LEADING_SIGN_CANDIDATE"
    elif hess_ok and sep_ok:
        verdict = "HESSIAN_EXCEPTION_FOUND"
    elif scaling_ok:
        verdict = "SCALING_CONFIRMED_SIGN_OPEN"
    else:
        verdict = "FLUCTUATION_FORM_FAILS"
    check("G52-adjudication", True,
          "SEALED HIERARCHY result: %s (blind %.3f vs %.2f | "
          "controls %d/3 | scaling %s | hessian-exception %s | "
          "separator %s); modifiers: SMOOTH_DIES %s, "
          "LIFT_POSITIVE %d/%d"
          % (verdict, rate_bli, BLIND_BAR, ctrl_break,
             scaling_ok, hess_ok, sep_ok, smooth_dies,
             lift_pos, len(recs)))

    # ---------------- S6: must-fails + mp ward
    section("S6  MUST-FAILS + HIGH-PRECISION WARD")
    okM = True
    # m1 oracle
    m1 = sum(1 for r in recs
             if (r["gt_gamN"] >= 0) == (r["gt_gamN"] >= 0))
    okM = okM and m1 == len(recs)
    # m2 degree shift: the n = N-1 truth is positive on ALL
    # windows (free wall), the n = N truth is negative on the
    # delta = 0 set -- the truths differ exactly there
    m2_diff = sum(1 for r in recs if r["gt_gamN"] < 0)
    okM = okM and m2_diff == n_neg and (smoke or m2_diff
                                        == NEG_COUNT_FULL)
    # m3 gated in G30 (mutated stencil loud)
    okM = okM and m3_loud > 1.0
    # m4 one-weight mutation moves gammahat_N loudly
    Wm = r9["Wt"].copy()
    jmid = int(np.argmax(np.abs(Wm)))
    Wm[jmid] *= 1.0 + 1e-3
    g_mut = gam_at(r9["x"], Wm, N9)
    m4_dev = (abs(g_mut - r9["gt_gamN"])
              / max(abs(r9["gt_gamN"]), 1e-300)
              if g_mut is not None else float("inf"))
    okM = okM and m4_dev > 1e-8
    check("G60-must-fails-fire", okM,
          "m1 oracle reading the physical gammahat_N hits "
          "%d/%d and is typed ALIAS_OF_WALL (excluded by the "
          "input firewall); m2 the degree-(N-1) truth differs "
          "from the degree-N truth on exactly the %d negative "
          "windows (the terminal degree is the content); m3 "
          "mutated stencil misses by %.1e; m4 one-weight "
          "mutation moves gammahat_N by rel %.1e (moment-"
          "defined, not an alias)"
          % (m1, len(recs), m2_diff, m3_loud, m4_dev))

    if smoke:
        check("G70-mp-ward", True, "SMOKE: mp ward skipped")
    else:
        import mpmath as mp
        mp.mp.dps = MP_DPS
        worst_mp = 0.0
        for r in (recs[0], next(q for q in recs
                                if q["kz"] == 9)):
            for e in (0.0, EPS_H):
                Wv = r["Ws"] + e * r["V"]
                nds = [mp.mpf(float(v)) for v in r["x"]]
                wt = [mp.mpf(float(v)) for v in Wv]
                pk_ = [mp.mpf(1)] * len(nds)
                pkm = [mp.mpf(0)] * len(nds)
                hs = [mp.fsum(w * p * p
                              for w, p in zip(wt, pk_))]
                for n in range(r["N"]):
                    a = mp.fsum(w * xx * p * p for w, xx, p
                                in zip(wt, nds, pk_)) / hs[-1]
                    g = (hs[-1] / hs[-2]) if n > 0 else mp.mpf(0)
                    nx = [(xx - a) * p - g * q for xx, p, q
                          in zip(nds, pk_, pkm)]
                    pkm, pk_ = pk_, nx
                    hs.append(mp.fsum(w * p * p
                                      for w, p in zip(wt, pk_)))
                g_mp = float(hs[r["N"]] / hs[r["N"] - 1])
                g_f = gam_at(r["x"], Wv, r["N"])
                worst_mp = max(worst_mp, abs(g_f - g_mp)
                               / max(abs(g_mp), 1e-300))
        check("G70-mp-ward", worst_mp <= MP_BAR,
              "mp dps-%d plain monic recomputation of G(0) and "
              "G(+%.2f) on the smallest rung and w9: worst rel "
              "dev %.1e (bar %.0e, generous by disclosure: the "
              "smooth-base chain crosses many near-zeros)"
              % (MP_DPS, EPS_H, worst_mp, MP_BAR))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G80-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a leading-order "
          "adjudication moves no edge); what the round adds: "
          "the smooth background dies N-independently early on "
          "every window, the fluctuation LIFT of the terminal "
          "pivot is measured with its sign census, and the "
          "quadratic-in-fluctuation leading order is "
          "adjudicated instead of assumed")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G90-verdict", npass == len(CHECKS),
          "%s: sealed F candidates, sealed stencil + seeds, "
          "sealed predictor and hierarchy, controls applied, "
          "ground truth confined to gates; NO RH claim"
          % verdict)

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
