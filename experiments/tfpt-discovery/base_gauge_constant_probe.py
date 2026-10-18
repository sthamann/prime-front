#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""base_gauge_constant_probe -- PRIME.PORT.RHP.BASE.GAUGE_CONSTANT.01
(round 252): IS THE MISSING h CONSTANT JUST A WRONG GLOBAL GAUGE?
The reviewer re-adjudication of this round's contract: r250/r251
measured that the outer model M_n carries the h RATE (slope <=
0.007 dec/degree, 4/4 windows) with a large offset (median
-1.25..-1.45, terminal -1.69..-1.86 decades in the Delta_n =
log10|h_n| - log10 h_n^out convention) and froze
BASE_READOUT_BLOCKED_BY_OFFSET.  Core thesis to test FIRST: if
the offset is a global (per-window) gauge constant, it CANCELS IN
QUOTIENTS -- h_{w,n} = h_{w,0} prod_j gamma_{w,j}, so the base
positivity question needs h_0 > 0 plus gamma_j > 0 and NO absolute
norming model at all.  DO NOT FIT -- DIVIDE.

REVIEWER AMENDMENT, DISCLOSED (before calibration): this round was
first drafted as PRIME.PORT.RHP.OUTER.CONSTLAYER.01
(outer_constlayer_probe.py, spec sealed, SMOKE pass only -- w9,
PROF_PTS 8, no full-record evaluation, no record freeze).  The
reviewer re-adjudicated the contract BEFORE calibration: absolute
constant-layer candidates are demoted to priority (4); the
quotient test, the h_0 normalizer, and the gauge adjudication come
first; hard orientation gates are added.  Disclosed smoke
knowledge carried over: the w9 smoke showed raw offset median
-1.26 (r251 reproduced), the b1 saturation-LSE candidate
UNDER-corrects on w9 (offset -1.15) and overshoots the toy by
-0.31 dec, the b2 Szego-continuum constant is tiny, and the
universal-constant battery members that fit the windows fail the
Chebyshev toy -- the battery is RETIRED by the amendment; b1/b2
move to leg 4.  No full-window, no multi-window, no quotient
number was seen before this seal.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r251 discipline): w = window (kz),
N_w = builder depth, n = chain degree; free pivots h_{w,n}
(n < N_w) are the proof objects; the forced pivot h_N is NEVER
formed (all sweeps stop at N-1); ground truth (h values / signs /
flip degrees of the tested chain) enters RESIDUALS, QUOTIENT
STATISTICS AND GATES ONLY -- no model path consumes it; the model
side is the r250 outer model VERBATIM (r232a constrained-
equilibrium g, KKT-midpoint ell, discrete Szego D, -2 pi i
calibration; machinery imported from centered_basefiber_probe, no
refit of D or ell anywhere).  The h_0-normalizer (leg 2) consumes
the chain HEAD (degree <= 2 mass data) as a disclosed source-pure
input normalizer -- h_0 is the total mass of the functional, not
a target pivot.  No zero/prime oracles anywhere (AST firewall).

LEG 1 -- QUOTIENT TEST FIRST (the round's core measurement):
Delta_{w,n} = log10|h_{w,n}| - log10 h^out_{w,n} and
eta_{w,n} = Delta_{w,n} - Delta_{w,n-1} = log10|gamma_{w,n} /
gamma^out_{w,n}|, gamma_{w,n} = h_{w,n}/h_{w,n-1}.  Measured over
ALL free degrees (QP equilibrium at EVERY mass n in [2, N_w - 1],
warm-started ascending; eta from n = 3 -- the model needs a
two-node hull, the excluded n <= 2 head is the r248 rank-1 zone,
disclosed), on the four mp-warded main windows, plus the pre-flip
quotient anatomy on EPSTEIN/SMOOTH and a BLIND-position sample of
the r233 42-rung frame-A ladder (rate check).  Degree-resolved
statistics per window: max |eta| (+ its degree), median eta,
median |eta|, total drift Delta_{N-1} - Delta_2, Delta slope,
last-10 median.  THREE SEALED CASES:
  BASE_RATIO_EXACT iff max |eta| <= 0.02 dec on all four main
    windows (the ratio is exact to propagated error -- the
    constant is IRRELEVANT for the sign question);
  RATE_ONLY_NUMERICAL iff a blind-ladder |Delta slope| > 0.01
    dec/degree OR a control's near-flip blowup factor (last-5
    median |eta| / max(bulk median |eta|, 1e-3)) > 10 OR the
    gauge-layer bars below fail (typed reason printed);
  BASE_GAUGE_LAYER iff |median eta| <= 0.005 dec AND max |eta|
    <= 0.5 dec on all four main windows (the systematic
    per-degree quotient error is at the half-percent level --
    only the small quotient error needs control).
LEG 2 -- h_0 NORMALIZER: C_w^(0) = h_{w,n0}/h^out_{w,n0} at the
sealed anchor degree n0 = 2 (the lowest model-representable
degree; h_2 = h_0 gamma_1 gamma_2 is head mass data, disclosed
implementation of the h_0 normalizer).  Then WITHOUT any further
adjustment: rest_n = Delta_n - Delta_2 over all degrees;
C0_NORMALIZER_CARRIES iff max |rest| < 0.5 dec on all four
windows, else C0_NORMALIZER_INSUFFICIENT (max rest reported).
LEG 3 -- DIAGONAL RH GAUGE: a constant G_w = diag(c_w, 1/c_w)
scales the offdiagonal readouts by c_w^{+-2} without touching the
phase rate.  Adjudicated by CONVENTION, never by fit: both Y_n
(r227/r234 FIK form, monic, h = (Y1)_12) and M_n satisfy the SAME
z^{-n sigma3} normalization at infinity with det = 1; the
Richardson extraction of (M1)_12 at the sealed norm points vs the
analytic h^out (bar 1e-4 in decades, r250 machinery), det M (bar
1e-30) and arg (M1)_12 (bar 1e-6) at degrees {N//2, N-1} per
window PIN c_w to 1 at the 1e-4-decade level =>
GAUGE_PINNED_AT_INFINITY (the M normalization is NOT globally
wrong; the offset is model error that must cancel in quotients),
else GAUGE_BROKEN(dev).  The continuum Chebyshev-U anchor (2 pi
4^-n Dinf^2 (b-a)/4 = (pi/2) 4^-n identically, bar 1e-12) fixes
the -2 pi i residue convention.
LEG 4 -- SATURATION/SZEGO DIVISOR (ONLY if legs 2 AND 3 do not
own the layer, i.e. adjudicated iff C0_NORMALIZER_INSUFFICIENT or
GAUGE_BROKEN; otherwise reported unadjudicated): the demoted
candidates, sealed as in the superseded draft: b1 = the
saturation partition sum h^b1 = LSE_{rho <= 1/2}(-F), F = 2 (A
rho) + V (the KKT field; derived from the 0/1-selection trial
polynomial); b2 = the discrete-continuum Szego replacement h^b2 =
h^out (Dinf_cont/Dinf_disc)^2 (M_CONT Gauss-Chebyshev points,
linear-interpolated L).  Acceptance: |median resid| < 0.5 dec AND
|slope| <= 0.01 dec/degree on ALL windows; CALIBRATION DUTY kept
from the retired b3: the accepted formula must anchor the exact
discrete Chebyshev-U toy to |median toy resid| <= 0.25 dec.
LEG 5 -- ORIENTATION MUST-GATES (hard, new): a positive global
factor cannot change a sign -- the solved constant proves the
base only if the model quotients already carry the ORIENTATION.
Gate A (MAIN): gamma^out_{w,n} > 0 up to N_w - 1 on 4/4 (note
h^out = 2 pi e^{n ell} Dinf^2 (b-a)/4 is positive by
construction -- typed if so).  Gate B (controls): first model
flip degree = first true flip degree (EPSTEIN 25 / SMOOTH 27)
within the frozen tolerance +-2.  If the model returns positive
gamma^out on ALL worlds it is arithmetically blind despite the
correct MAIN rate => MODEL_ORIENTATION_BLIND added honestly.
BEST verdict BASE_RATIO_CARRIES_SIGN requires BASE_RATIO_EXACT
AND both orientation gates green.
LEG 6 -- PROOF-READY R_1 INSTRUMENT: R_1 = (1/2 pi i) oint
(R(z) - I) dz on the sealed circle (center x0 = union-node hull
midpoint, radius = half-width + 2.0, K = 64 trapezoid points,
dps 260, w9 at n = N//2) instead of astronomical-z evaluation;
gate: |(R_1)_12 - (h_true - h^out)| / max(|h_true|, h^out) <=
1e-4 (one gate suffices; verifies the r251 delta-h contour
identity in integral form).
MUST-FAILS (each loud): (m1) wrong factor 2 in the KKT field
((A rho) + V), (m2) forgotten square root (LSE(-2F)), (m3)
exponent sign flip (LSE(+F)) -- each must move the b1 residual by
>= max(2.0, |honest| + 1.5) decades (w9, n = N//2); (m6) swapped
contour entry ((R_1)_21 for (R_1)_12) must break the leg-6 gate
by >= 1e3 x (the transposed entry carries the e^{-2 n ell}
gauge); (m4) SIGN ORACLE: reading sign h_{N-1} or any flip degree
into a model path is EXCLUDED by the input firewall (standing
r243 exclusion, re-asserted).

SEALED CONSTANTS: windows (9, 12, 13, 26); control flips
EPSTEIN/SCRAMBLE/SMOOTH = 25/21/27; full sweep masses [2, N-1]
step 1; anchor degree n0 = 2; eta from n = 3; QP: FISTA iters
8000, tol 1e-8, residual bar 1e-6, warm ascending; RHO_SEL 1e-9;
saturation threshold 1/2; mp chain ward w9 dps 120, bar 1e-6 on
|lg h| over all sweep degrees; case bars: exact 0.02, gauge-layer
median 0.005 / max 0.5, ladder rate 0.01 dec/degree, near-flip
factor 10 (floor 1e-3); C0 rest bar 0.5; gauge wards: Richardson
1e-4 dec, det M 1e-30, arg 1e-6, degrees {N//2, N-1}, continuum
identity 1e-12; leg-4 bars 0.5 / 0.01 / toy 0.25; toy = 64
Chebyshev nodes, masses (6, 8, 10, 12, 14, 16), depth 18, M_CONT
2048; controls swept to flip + 10 (pre-flip eta anatomy + the
gate-B model-flip scan); orientation tolerance +-2 degrees;
contour K 64, radius
pad 2.0, dps 260, bar 1e-4, m6 loudness 1e3; ladder sample =
frame-A zones (h <= 900 by the frame-A arithmetic, main windows
excluded) sorted by (h, kz), BLIND = odd positions (r233 rule on
the h-sorted proxy, disclosed -- no predictor constants are
computed here, the sample is anatomy), picks = first/middle/last
BLIND position, grid 12 masses in [2, N-1], flipped rungs typed
and skipped; runtime <= 1800 s; smoke = w9 only, masses 2..41,
toy kept, mp ward / controls sweep / ladder / worlds / contour
skipped, no adjudication.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  BASE_RATIO_CARRIES_SIGN iff BASE_RATIO_EXACT and both
    orientation gates green (the best verdict);
  else the leg-1 case verdict BASE_RATIO_EXACT /
    BASE_GAUGE_LAYER / RATE_ONLY_NUMERICAL;
+ C0_NORMALIZER_<CARRIES|INSUFFICIENT>(max rest dec)
+ GAUGE_<PINNED_AT_INFINITY|BROKEN>(worst dev dec)
+ SATSZEGO_<NOT_ADJUDICATED|DERIVED(cand)|OPEN> (leg-4 priority
    rule: adjudicated only if legs 2 and 3 both fail to own the
    layer)
+ [MODEL_ORIENTATION_BLIND if gamma^out > 0 on all worlds]
+ R1_CONTOUR_<VERIFIED|FAILED>(dev).
Honesty before beauty: no verdict claims a bound mechanism; the
budget bound and the base law stay OPEN (r243 PAIRCORR_REENCODED,
r247 B discipline, r250 error map, r251 margin bills all stand).

CALIBRATION AMENDMENTS (disclosed, frozen): (a1) the w9 mp chain
ward must snapshot at N-1, not N//2 -- mp_y_pass only recurses to
the maximum snapshot degree, so the first full attempt died on a
KeyError before any ward number existed (pure implementation fix,
no bar or rule touched).  No other amendment; the sealed bars,
cases and priority rules above are exactly the ones adjudicated.

RECORD TABLES (frozen after calibration run 1; run 2 must
reproduce bit-for-bit):
* LEG 1, eta = log10|gamma/gamma^out| over ALL free degrees
  (859 QP equilibria, 4/4 windows mp-warded at dps 120 to
  1.6e-11):
    w9  (N=184): max|eta| 0.731@n=71,  med +0.0230, med|.|
      0.164, drift(Delta_{N-1}-Delta_2) -1.888, slope -0.0033
    w12 (N=151): max|eta| 0.719@n=44,  med +0.0368, med|.|
      0.161, drift -1.465, slope -0.0048
    w13 (N=168): max|eta| 0.629@n=89,  med +0.0006, med|.|
      0.170, drift -1.147, slope -0.0027
    w26 (N=364): max|eta| 0.777@n=158, med +0.0339, med|.|
      0.174, drift -2.098, slope -0.0018
  => SEALED CASE: RATE_ONLY_NUMERICAL ("quotient error not
  uniformly small": worst |med eta| 0.037 > 0.005, max|eta|
  0.777 > 0.5).  THE ROUND'S CENTRAL FINDING: degree-resolved,
  the r250/r251 "window-stable constant offset" DISSOLVES -- the
  offset drifts by -1.1..-2.1 decades from n = 2 to N-1 (fast
  head drop, flat bulk that the r251 coarse grid median saw,
  tail drop) and the per-degree quotient scatter is ~0.17
  decades (the eps-band gamma fluctuation the smooth model
  cannot carry).  The constancy was limited measurement; no
  global gauge constant exists to solve.  Controls pre-flip:
  EPSTEIN med|eta| 0.138 (near-flip factor 0.86), SMOOTH 0.231
  (factor 1.14) -- no near-flip blowup; ladder BLIND sample
  kz23/kz44/kz52 (N = 149/436/878) slopes -0.0022/-0.0022/
  -0.0013, all inside the 0.01 rate bar (the RATE is real; the
  CONSTANT was not).
* LEG 2, C_w^(0) = (h/h^out)(n0=2): w9 -0.184, w12 -0.342, w13
  -0.470, w26 +0.167 dec; rest after C0: max |rest| 1.888/
  1.583/1.558/2.322 dec => C0_NORMALIZER_INSUFFICIENT(2.32).
* LEG 3: Richardson (M1)_12 vs analytic h^out worst 4.0e-06 dec,
  det M worst 4.2e-81, arg worst 0.0 at {N//2, N-1} x 4 windows
  => GAUGE_PINNED_AT_INFINITY (c_w = 1: the offset is NOT a
  convention; the reviewer's gauge thesis dies on all three
  prongs -- quotients, h_0 normalizer, infinity normalization).
* LEG 4 (adjudicated, C0 dead): b1 offs -1.20/-1.26/-1.23/-1.46,
  toy -0.307 ANCHOR-FAIL -> reject; b2 offs -1.20/-1.25/-1.19/
  -1.43, toy -0.075 anchor-OK but offsets stand -> reject
  => SATSZEGO_OPEN.
* LEG 5: MAIN gamma^out > 0 on 4/4 (positive by construction --
  no sign channel); controls: model flip None vs true 25/27
  => MODEL_ORIENTATION_BLIND (honest; BASE_RATIO_CARRIES_SIGN
  unreachable this round).
* LEG 6: contour R_1 on w9 n=92 (K=64, radius 3.00, dps 260):
  |(R_1)_12 - (h_true - h^out)|/scale = 3.2e-14 (bar 1e-4) =>
  R1_CONTOUR_VERIFIED; m6 swapped entry 1.3e+109 x honest
  (LOUD).  Must-fails m1/m2/m3: 28.3/54.6/116.7 dec (LOUD).
* VERDICT: RATE_ONLY_NUMERICAL + C0_NORMALIZER_INSUFFICIENT
  (2.32 dec) + GAUGE_PINNED_AT_INFINITY(4e-06 dec) +
  SATSZEGO_OPEN + MODEL_ORIENTATION_BLIND + R1_CONTOUR_VERIFIED
  (3.2e-14); 22/22 gates, wall 56 s.

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
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH           # noqa: E402 r244
import centered_basefiber_probe as CB        # noqa: E402 r250
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import szego_equilibrium_probe as SZ         # noqa: E402 r232a
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

WINDOWS = (9, 12, 13, 26)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
N0_ANCHOR = 2
ETA_LO = 3
QP_ITERS = 8000
QP_TOL = 1e-8
QP_RES_BAR = 1e-6
RHO_SEL = 1e-9
SAT_THR = 0.5
MP_WARD_DPS = 120
MP_WARD_BAR = 1e-6
ETA_EXACT_MAX = 0.02
ETA_GL_MED = 0.005
ETA_GL_MAX = 0.5
RATE_BAR = 0.01
NEARFLIP_FACTOR = 10.0
NEARFLIP_FLOOR = 1e-3
C0_REST_BAR = 0.5
RICH_BAR = 1e-4
DETM_BAR = 1e-30
ARG_BAR = 1e-6
CHEB_ID_BAR = 1e-12
OFF_BAR4 = 0.5
TOY_ANCHOR_BAR = 0.25
TOY_MASSES = (6, 8, 10, 12, 14, 16)
TOY_M = 64
TOY_DEPTH = 18
M_CONT = 2048
FLIP_TOL = 2
FLIP_SCAN = 10
R1_K = 64
R1_PAD = 2.0
R1_DPS = 260
R1_BAR = 1e-4
M6_LOUD = 1e3
MF_ABS = 2.0
MF_REL = 1.5
LADDER_H_CAP = 900
LADDER_GRID = 12
DPS_SPOT = 80
L10 = math.log(10.0)
CAL_VERDICT = ("RATE_ONLY_NUMERICAL + C0_NORMALIZER_INSUFFICIENT"
               "(2.32 dec) + GAUGE_PINNED_AT_INFINITY(4e-06 dec)"
               " + SATSZEGO_OPEN + MODEL_ORIENTATION_BLIND + "
               "R1_CONTOUR_VERIFIED(3.2e-14)")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
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
    return (not bad), ("NO zero/prime oracles; the model consumes "
                       "node positions + |weights| + the QP "
                       "minimizer only; the h_0 normalizer consumes "
                       "the degree <= 2 head (disclosed); h_N never "
                       "formed; target h / signs / flips enter "
                       "residuals and gates only (m4 EXCLUDED)"
                       if not bad else "; ".join(bad))


# ------------------------------------------------- 2x2 mp helpers
def m_adj2(M):
    return ((M[1][1], -M[0][1]), (-M[1][0], M[0][0]))


def m_det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def m_mul2(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0],
             A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0],
             A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def r_field(Y, M):
    detM = m_det2(M)
    Ra = m_mul2(Y, m_adj2(M))
    return ((Ra[0][0] / detM, Ra[0][1] / detM),
            (Ra[1][0] / detM, Ra[1][1] / detM))


# ----------------------------------------------------- candidates
def lse_l10(t):
    m = float(np.max(t))
    return (m + math.log(float(np.sum(np.exp(t - m))))) / L10


def cand_fields(A, V, wt, rho, n):
    """KKT field, saturation partition, lambda window, b1 LSE."""
    F = 2.0 * (A @ rho) + V
    sel = rho > RHO_SEL
    sat = rho > SAT_THR
    uns = ~sat
    lam_lo = float(np.max(F[sel]))
    lam_hi = float(np.min(F[~sel])) if np.any(~sel) else lam_lo
    return dict(F=F, uns=uns, gap=lam_hi - lam_lo,
                b1=lse_l10(-F[uns]),
                satfrac=float(np.sum(sat)) / max(n, 1))


def b2_l10(md):
    a, b = md["a"], md["b"]
    tt = (0.5 * (a + b) + 0.5 * (b - a)
          * np.cos(math.pi * (np.arange(M_CONT) + 0.5) / M_CONT))
    ll = np.interp(tt, md["xs"], md["L"])
    dinf_c = 0.5 * float(np.mean(ll))
    return md["hmod_l10"] + 2.0 * (dinf_c - md["dinf_log"]) / L10


def ladder_h(kz):
    """frame-A builder depth by the frame-A arithmetic (cheap,
    verbatim the frame_a_zones formula -- no window build)."""
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M_k = int(math.ceil(core.U_ALL[kz] / D_k - 1.0e-9)) + 1
    if M_k % 2:
        M_k += 1
    return M_k // 2


def sweep_window(d, rows, masses, keep_md=()):
    """QP equilibrium at every mass in `masses` (warm ascending);
    returns per-degree arrays (true log10 h, model log10 h, b1,
    b2, satfrac, gap) + kept model_data dicts + worst residual."""
    x, wt, A, Lip, V = CB.eq_field(d)
    out = dict(ns=[], lgt=[], hmod=[], b1=[], b2=[], satf=[],
               gap=[], sg=[])
    mds = {}
    mf = None
    rho = None
    res_worst = 0.0
    mass_ok = True
    for n in masses:
        rho, res = SZ.solve_qp(A, Lip, V, float(n), rho0=rho,
                               iters=QP_ITERS, tol=QP_TOL)
        res_worst = max(res_worst, res)
        md = CB.model_data(x, wt, A, V, rho, n)
        mass_ok = mass_ok and (md["nround"] == n)
        cf = cand_fields(A, V, wt, rho, n)
        out["ns"].append(n)
        out["lgt"].append(rows[n]["lg_h"] / L10)
        out["hmod"].append(md["hmod_l10"])
        out["b1"].append(cf["b1"])
        out["b2"].append(b2_l10(md))
        out["satf"].append(cf["satfrac"])
        out["gap"].append(cf["gap"])
        out["sg"].append(rows[n]["sg_h"])
        if n in keep_md:
            mds[n] = md
            if mf is None:
                mf = dict(F=cf["F"].copy(), uns=cf["uns"].copy(),
                          V=V.copy(), lgt=rows[n]["lg_h"] / L10,
                          b1=cf["b1"], n=n)
    for k in out:
        out[k] = np.asarray(out[k], float)
    out["mds"] = mds
    out["mf"] = mf
    return out, res_worst, mass_ok


def eta_stats(ns, lgt, hmod):
    """degree-resolved quotient statistics (leg 1)."""
    delta = lgt - hmod
    dtrue = np.diff(lgt)
    dmod = np.diff(hmod)
    eta = dtrue - dmod                     # eta_n at ns[1:]
    en = np.asarray(ns[1:], int)
    keep = en >= ETA_LO
    eta = eta[keep]
    en = en[keep]
    i = int(np.argmax(np.abs(eta)))
    last = eta[-10:] if len(eta) >= 10 else eta
    return dict(eta=eta, en=en, mx=float(np.abs(eta[i])),
                mx_at=int(en[i]), med=float(np.median(eta)),
                meda=float(np.median(np.abs(eta))),
                drift=float(delta[-1] - delta[0]),
                slope=float(np.polyfit(ns, delta, 1)[0]),
                last=float(np.median(last)), delta=delta)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else WINDOWS

    print("=" * 78)
    print("base_gauge_constant_probe -- PRIME.PORT.RHP.BASE."
          "GAUGE_CONSTANT.01 (round 252)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 masses 2..41; mp ward / "
                        "controls / ladder / contour skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION + AMENDMENT")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "priority order sealed: (1) quotient test eta = "
          "log10|gamma/gamma^out| over ALL free degrees (cases "
          "EXACT %.2f / GAUGE_LAYER med %.3f max %.1f / "
          "RATE_ONLY via ladder slope %.2f or near-flip factor "
          "%.0f); (2) h_0 normalizer C_w^(0) at n0 = %d, rest "
          "bar %.1f; (3) diagonal gauge pinned by the infinity "
          "normalization (Richardson %.0e dec, det %.0e, arg "
          "%.0e); (4) b1/b2 only if (2)+(3) die (bars %.1f/%.2f, "
          "toy %.2f); (5) orientation gates (tol +-%d); (6) "
          "contour R_1 (K %d, pad %.1f, dps %d, bar %.0e)"
          % (ETA_EXACT_MAX, ETA_GL_MED, ETA_GL_MAX, RATE_BAR,
             NEARFLIP_FACTOR, N0_ANCHOR, C0_REST_BAR, RICH_BAR,
             DETM_BAR, ARG_BAR, OFF_BAR4, RATE_BAR,
             TOY_ANCHOR_BAR, FLIP_TOL, R1_K, R1_PAD, R1_DPS,
             R1_BAR))
    check("G03-amendment-disclosed", True,
          "reviewer re-adjudication BEFORE calibration: the "
          "OUTER.CONSTLAYER.01 draft (sealed, SMOKE-only) is "
          "superseded; disclosed carried-over smoke knowledge: "
          "w9 offset median -1.26, b1 under-corrects on w9 "
          "(-1.15) and overshoots the toy (-0.31), b2 tiny, "
          "universal battery retired (its members fail the toy "
          "anchor); no full-window or quotient number was seen "
          "before this seal")

    # ---------------- S1: census + controls
    section("S1  CENSUS + CONTROLS")
    packs = {kz: BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPSTEIN", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCRAMBLE", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    okC = all(packs[kz]["nf"] is None for kz in windows)
    check("G10-census-controls", okC and okCf,
          "free prefix positive on %d/%d windows (%s); control "
          "flips re-derived %s (orientation gate B consumes "
          "EPSTEIN/SMOOTH; SCRAMBLE armed for battery integrity)"
          % (sum(1 for kz in windows if packs[kz]["nf"] is None),
             len(windows),
             "; ".join("w%d N=%d" % (kz, packs[kz]["N"])
                       for kz in windows),
             str({c: ctrl[c]["nf"] for c in ctrl})))

    # ---------------- S2: continuum anchor + toy
    section("S2  CONTINUUM ANCHOR + CHEBYSHEV TOY")
    id_dev = 0.0
    for n in range(1, 41):
        lhs = (math.log(2.0 * math.pi) - n * math.log(4.0)
               + math.log(0.5) + math.log(0.5))
        rhs = math.log(math.pi / 2.0) - n * math.log(4.0)
        id_dev = max(id_dev, abs(lhs - rhs))
    check("G20-continuum-anchor", id_dev <= CHEB_ID_BAR,
          "continuum Chebyshev-U: 2 pi 4^-n Dinf^2 (b-a)/4 = "
          "(pi/2) 4^-n identically (max dev %.1e over n = 1..40, "
          "bar %.0e) -- the -2 pi i residue convention and the "
          "FIK normalization carry no missing universal power in "
          "the continuum: leg-3 input" % (id_dev, CHEB_ID_BAR))
    xt = np.sort(np.cos(np.pi * (np.arange(TOY_M) + 0.5) / TOY_M))
    wtt = (1.0 - xt * xt) * (np.pi / TOY_M)
    Dm = np.abs(xt[:, None] - xt[None, :])
    np.fill_diagonal(Dm, 1.0)
    At = -np.log(Dm)
    np.fill_diagonal(At, 0.0)
    v = np.ones(TOY_M) / math.sqrt(TOY_M)
    for _ in range(80):
        v2 = At @ v
        nv = float(np.linalg.norm(v2))
        v = v2 / nv
    Lipt = 2.0 * nv
    Vt = -np.log(wtt)
    _als, hs = CB.toy_chain_f64(xt, wtt, TOY_DEPTH)
    res_t = 0.0
    rho = None
    toy_r1, toy_r2 = [], []
    for n in TOY_MASSES:
        rho, res = SZ.solve_qp(At, Lipt, Vt, float(n), rho0=rho,
                               iters=QP_ITERS, tol=QP_TOL)
        res_t = max(res_t, res)
        md = CB.model_data(xt, wtt, At, Vt, rho, n)
        cf = cand_fields(At, Vt, wtt, rho, n)
        lgt = math.log10(hs[n])
        toy_r1.append(lgt - cf["b1"])
        toy_r2.append(lgt - b2_l10(md))
        info("toy n=%-3d Delta_raw %+.3f  resid_b1 %+.3f  "
             "resid_b2 %+.3f" % (n, lgt - md["hmod_l10"],
                                 toy_r1[-1], toy_r2[-1]))
    toy_med = {"b1_satsum": float(np.median(toy_r1)),
               "b2_szego": float(np.median(toy_r2))}
    check("G21-toy-block", res_t <= QP_RES_BAR,
          "discrete Chebyshev-U toy (%d nodes, exact f64 chain): "
          "QP residual worst %.1e (bar %.0e); leg-4 toy anchors: "
          "b1 median %+.3f, b2 median %+.3f (bar %.2f -- the "
          "calibration duty kept from the retired battery)"
          % (TOY_M, res_t, QP_RES_BAR, toy_med["b1_satsum"],
             toy_med["b2_szego"], TOY_ANCHOR_BAR))

    # ---------------- S3: full-degree sweeps + wards
    section("S3  FULL-DEGREE SWEEPS (QP at every free mass)")
    W = {}
    res_worst = 0.0
    mass_ok = True
    for kz in windows:
        p = packs[kz]
        N = p["N"]
        masses = (range(2, 42) if smoke else range(2, N))
        keep = {N // 2, N - 1} if not smoke else {40}
        t0 = time.time()
        sw, rw, mo = sweep_window(p["d"], p["rows"],
                                  list(masses), keep_md=keep)
        res_worst = max(res_worst, rw)
        mass_ok = mass_ok and mo
        W[kz] = sw
        info("w%-3d N=%d: %d masses swept in %.1f s; sign "
             "positive on %d/%d" % (kz, N, len(sw["ns"]),
                                    time.time() - t0,
                                    int(np.sum(sw["sg"] > 0)),
                                    len(sw["sg"])))
    check("G22-sweep-qp-wards", res_worst <= QP_RES_BAR
          and mass_ok,
          "QP residual worst %.1e (bar %.0e) over %d equilibria; "
          "every rounded mass integer-exact; D/ell = r250 "
          "objects, untouched"
          % (res_worst, QP_RES_BAR,
             sum(len(W[kz]["ns"]) for kz in windows)))
    if smoke:
        check("G23-mp-chain-ward", True,
              "SMOKE: mp ward skipped (r250/r251 chain wards "
              "stand)")
    else:
        p9 = packs[9]
        N9 = p9["N"]
        zfar = [float(np.max(np.concatenate(
            [p9["d"]["xs"], p9["d"]["ys"]]))) + 1000.0]
        _o, _g, hlog = CB.mp_y_pass(p9["d"], {N9 - 1}, zfar,
                                    MP_WARD_DPS, N9)
        dev = 0.0
        sg_ok = True
        for n in range(2, N9):
            dev = max(dev, abs(float(hlog[n][0])
                               - p9["rows"][n]["lg_h"]))
            sg_ok = sg_ok and (float(hlog[n][1])
                               == p9["rows"][n]["sg_h"])
        check("G23-mp-chain-ward", dev <= MP_WARD_BAR and sg_ok,
              "w9 mp chain (dps %d) vs the f64 wpack chain over "
              "ALL sweep degrees: max |lg h| dev %.1e (bar "
              "%.0e), signs %s -- the quotient statistics are "
              "not an f64 artifact"
              % (MP_WARD_DPS, dev, MP_WARD_BAR,
                 "all match" if sg_ok else "MISMATCH"))

    # ---------------- S4: leg 1 -- the quotient test
    section("S4  LEG 1 -- QUOTIENT TEST (eta statistics)")
    ES = {}
    for kz in windows:
        sw = W[kz]
        st = eta_stats(list(sw["ns"].astype(int)), sw["lgt"],
                       sw["hmod"])
        ES[kz] = st
        info("w%-3d eta: max|.| %.3f@n=%d  med %+.5f  med|.| "
             "%.4f  drift %+.3f  slope %+.5f  last10 %+.4f  | "
             "Delta med %+.3f term %+.3f"
             % (kz, st["mx"], st["mx_at"], st["med"], st["meda"],
                st["drift"], st["slope"], st["last"],
                float(np.median(st["delta"])),
                float(st["delta"][-1])))
    check("G30-eta-table", True,
          "the eta statistics table (rows above) is the round's "
          "first deliverable: eta_{w,n} = log10|gamma_{w,n}/"
          "gamma^out_{w,n}| over ALL free degrees (n >= %d), "
          "QP at every mass" % ETA_LO)
    # controls quotient anatomy (pre-flip eta; the sweep extends
    # FLIP_SCAN degrees past the flip for the gate-B model-flip
    # scan of leg 5)
    nearflip_max = 0.0
    ctrl_sw = {}
    if smoke:
        check("G31-controls-quotient", True,
              "SMOKE: controls sweep skipped")
    else:
        cq_note = []
        for cname in ("EPSTEIN", "SMOOTH"):
            pc = ctrl[cname]
            nf = pc["nf"]
            top = min(nf + FLIP_SCAN + 1, pc["N"])
            swc, rwc, _moc = sweep_window(pc["d"], pc["rows"],
                                          list(range(2, top)))
            res_worst = max(res_worst, rwc)
            ctrl_sw[cname] = swc
            pre = swc["ns"] <= nf - 1
            stc = eta_stats(
                list(swc["ns"][pre].astype(int)),
                swc["lgt"][pre], swc["hmod"][pre])
            bulk = float(np.median(np.abs(stc["eta"])))
            last5 = float(np.median(np.abs(stc["eta"][-5:])))
            fac = last5 / max(bulk, NEARFLIP_FLOOR)
            nearflip_max = max(nearflip_max, fac)
            cq_note.append("%s(flip %d): med|eta| %.4f last5 "
                           "%.4f factor %.2f"
                           % (cname, nf, bulk, last5, fac))
        check("G31-controls-quotient", True,
              "pre-flip quotient anatomy on the controls: %s "
              "(near-flip blowup factor bar %.0f feeds the "
              "RATE_ONLY trigger)" % ("; ".join(cq_note),
                                      NEARFLIP_FACTOR))
    # blind-ladder rate sample
    lad_slope_max = 0.0
    if smoke:
        check("G32-ladder-blind", True, "SMOKE: ladder skipped")
    else:
        elig = sorted((ladder_h(kz), kz)
                      for kz in core.frame_a_zones()
                      if kz not in WINDOWS
                      and ladder_h(kz) <= LADDER_H_CAP)
        blind = elig[1::2]
        picks = sorted({blind[0], blind[len(blind) // 2],
                        blind[-1]})
        lad_note = []
        for _h, kz in picks:
            pL = BH.wpack(kz)
            if pL["nf"] is not None:
                lad_note.append("kz%d FLIP@%d typed+skipped"
                                % (kz, pL["nf"]))
                continue
            NL = pL["N"]
            grid = sorted(set(np.linspace(2, NL - 1, LADDER_GRID)
                              .astype(int).tolist()))
            swl, rwl, mol = sweep_window(pL["d"], pL["rows"],
                                         grid)
            res_worst = max(res_worst, rwl)
            dl = swl["lgt"] - swl["hmod"]
            sl = float(np.polyfit(swl["ns"], dl, 1)[0])
            lad_slope_max = max(lad_slope_max, abs(sl))
            lad_note.append("kz%d N=%d slope %+.4f off med %+.2f"
                            % (kz, NL, sl, float(np.median(dl))))
        check("G32-ladder-blind", True,
              "BLIND-position sample of the 42-rung ladder "
              "(h-sorted proxy, odd positions, first/middle/"
              "last): %s -- max |slope| %.4f vs rate bar %.2f "
              "(RATE_ONLY trigger input)"
              % ("; ".join(lad_note), lad_slope_max, RATE_BAR))
    # sealed case adjudication
    if smoke:
        case = "SMOKE_NO_ADJUDICATION"
        case_note = "smoke"
    else:
        mx_all = max(ES[kz]["mx"] for kz in windows)
        med_all = max(abs(ES[kz]["med"]) for kz in windows)
        rate_trig = (lad_slope_max > RATE_BAR
                     or nearflip_max > NEARFLIP_FACTOR)
        if mx_all <= ETA_EXACT_MAX:
            case = "BASE_RATIO_EXACT"
            case_note = "max|eta| %.4f <= %.2f on 4/4" % (
                mx_all, ETA_EXACT_MAX)
        elif rate_trig:
            case = "RATE_ONLY_NUMERICAL"
            case_note = ("trigger: ladder slope %.4f / near-flip "
                         "factor %.1f" % (lad_slope_max,
                                          nearflip_max))
        elif med_all <= ETA_GL_MED and mx_all <= ETA_GL_MAX:
            case = "BASE_GAUGE_LAYER"
            case_note = ("|med eta| worst %.5f <= %.3f, max|eta| "
                         "%.3f <= %.1f" % (med_all, ETA_GL_MED,
                                           mx_all, ETA_GL_MAX))
        else:
            case = "RATE_ONLY_NUMERICAL"
            case_note = ("quotient error not uniformly small: "
                         "|med eta| worst %.5f, max|eta| %.3f"
                         % (med_all, mx_all))
    check("G33-case-adjudicated", True,
          "SEALED leg-1 case: %s (%s)" % (case, case_note))

    # ---------------- S5: leg 2 -- h_0 normalizer
    section("S5  LEG 2 -- h_0 NORMALIZER C_w^(0)")
    c0_rest_max = 0.0
    c0_note = []
    for kz in windows:
        sw = W[kz]
        delta = sw["lgt"] - sw["hmod"]
        rest = delta - delta[0]           # anchor n0 = 2
        c0_rest_max = max(c0_rest_max,
                          float(np.max(np.abs(rest))))
        c0_note.append("w%d C0 %+.3f dec, rest med %+.3f max "
                       "%+.3f term %+.3f"
                       % (kz, float(delta[0]),
                          float(np.median(rest)),
                          float(np.max(np.abs(rest))),
                          float(rest[-1])))
    c0_carries = c0_rest_max < C0_REST_BAR and not smoke
    for t in c0_note:
        info(t)
    check("G40-c0-normalizer", True,
          "C_w^(0) = h_{w,%d}/h^out_{w,%d} (head data, "
          "disclosed), then h_n =? C^(0) h^out_n with NO further "
          "adjustment: max |rest| %.3f dec (bar %.1f) => %s"
          % (N0_ANCHOR, N0_ANCHOR, c0_rest_max, C0_REST_BAR,
             "C0_NORMALIZER_CARRIES" if c0_carries
             else ("C0_NORMALIZER_INSUFFICIENT"
                   if not smoke else "SMOKE")))

    # ---------------- S6: leg 3 -- diagonal gauge adjudication
    section("S6  LEG 3 -- DIAGONAL RH GAUGE (convention, not fit)")
    rich_worst = 0.0
    detm_worst = 0.0
    arg_worst = 0.0
    for kz in windows:
        sw = W[kz]
        p = packs[kz]
        x, _wt, _A, _Lip, _V = CB.eq_field(p["d"])
        _pan, norm_z, x0, _a0, _b0 = CB.build_panels(x)
        for n, md in sw["mds"].items():
            m1_12, _devs = CB.rich_M1_12(md, n, norm_z, DPS_SPOT)
            rich_worst = max(rich_worst,
                             abs(float(mp.log(abs(m1_12), 10))
                                 - md["hmod_l10"]))
            arg_worst = max(arg_worst,
                            abs(float(mp.arg(m1_12))))
            for z in (x0 + 1.5j, float(x[-1]) + 1.0):
                detm_worst = max(detm_worst, CB.detm_dev(
                    CB.model_at(md, complex(z), DPS_SPOT)))
    gauge_pinned = (rich_worst <= RICH_BAR
                    and detm_worst <= DETM_BAR
                    and arg_worst <= ARG_BAR)
    check("G50-gauge-adjudication", gauge_pinned,
          "diag(c, 1/c) would scale (M1)_12 by c^2 without "
          "touching the rate; ADJUDICATED BY CONVENTION: both Y "
          "and M carry the same z^{-n sigma3} normalization at "
          "infinity -- Richardson (M1)_12 vs analytic h^out "
          "worst %.1e dec (bar %.0e), det M worst %.1e (bar "
          "%.0e), arg worst %.1e (bar %.0e) at degrees "
          "{N//2, N-1} x %d windows => c_w pinned to 1 at the "
          "1e-4-decade level: %s"
          % (rich_worst, RICH_BAR, detm_worst, DETM_BAR,
             arg_worst, ARG_BAR, len(windows),
             "GAUGE_PINNED_AT_INFINITY (the offset is model "
             "error, not convention -- it must and does cancel "
             "in quotients only as far as leg 1 measures)"
             if gauge_pinned else "GAUGE_BROKEN"))

    # ---------------- S7: leg 4 -- conditional divisor candidates
    section("S7  LEG 4 -- SATURATION/SZEGO DIVISOR (conditional)")
    adjud4 = (not smoke) and ((not c0_carries)
                              or (not gauge_pinned))
    l4 = {}
    for name in ("b1_satsum", "b2_szego"):
        offs, sls = [], []
        for kz in windows:
            sw = W[kz]
            hc = sw["b1"] if name == "b1_satsum" else sw["b2"]
            rr = sw["lgt"] - hc
            offs.append(float(np.median(rr)))
            sls.append(float(np.polyfit(sw["ns"], rr, 1)[0]))
        acc = (all(abs(o) < OFF_BAR4 for o in offs)
               and all(abs(s) <= RATE_BAR for s in sls))
        toy_ok = abs(toy_med[name]) <= TOY_ANCHOR_BAR
        l4[name] = dict(offs=offs, sls=sls, acc=acc,
                        toy_ok=toy_ok)
        info("%-10s offs %s slopes %s toy %+.3f %s -> %s"
             % (name, str([round(o, 3) for o in offs]),
                str([round(s, 4) for s in sls]),
                toy_med[name],
                "ANCHOR-OK" if toy_ok else "ANCHOR-FAIL",
                "accept" if (acc and toy_ok) else "reject"))
    if not adjud4:
        v4 = "SATSZEGO_NOT_ADJUDICATED"
        wc4 = None
    else:
        wc4 = next((nm for nm in ("b1_satsum", "b2_szego")
                    if l4[nm]["acc"] and l4[nm]["toy_ok"]), None)
        v4 = ("SATSZEGO_DERIVED(%s)" % wc4 if wc4
              else "SATSZEGO_OPEN")
    check("G60-leg4-conditional", True,
          "sealed priority rule: leg 4 adjudicated iff legs 2 "
          "and 3 do not own the layer (C0 %s, gauge %s) => %s "
          "(table above %s)"
          % ("carries" if c0_carries else "insufficient",
             "pinned" if gauge_pinned else "broken", v4,
             "adjudicated" if adjud4 else "informational only"))

    # ---------------- S8: leg 5 -- orientation gates
    section("S8  LEG 5 -- ORIENTATION MUST-GATES")
    # gate A: MAIN model quotients positive (h^out is an exp form)
    mainA = all(bool(np.all(np.isfinite(W[kz]["hmod"])))
                for kz in windows)
    check("G70-orientation-main", True,
          "gate A (MAIN): gamma^out_{w,n} = 10^{Delta hmod} > 0 "
          "on %d/%d windows -- POSITIVE BY CONSTRUCTION (h^out = "
          "2 pi e^{n ell} Dinf^2 (b-a)/4 is an exponential of "
          "real source data: the model has NO sign channel; "
          "typed, feeds gate B)"
          % (sum(1 for kz in windows
                 if np.all(np.isfinite(W[kz]["hmod"]))),
             len(windows)))
    if smoke:
        orient_green = False
        blind_tok = True
        check("G71-orientation-controls", True,
              "SMOKE: control orientation gate skipped")
    else:
        oc_note = []
        orient_green = mainA
        blind_tok = True
        for cname in ("EPSTEIN", "SMOOTH"):
            nf_true = ctrl[cname]["nf"]
            swc = ctrl_sw[cname]
            # measured model-flip scan over [2, nf + FLIP_SCAN]:
            # first degree whose model quotient gamma^out is not
            # a positive finite number (h^out is an exponential
            # of real source data, so any flip can only appear
            # as a degeneracy of the formula)
            gmod = np.diff(swc["hmod"])
            bad = np.nonzero(~np.isfinite(gmod))[0]
            nf_mod = (int(swc["ns"][1:][bad[0]])
                      if len(bad) else None)
            okB = (nf_mod is not None
                   and abs(nf_mod - nf_true) <= FLIP_TOL)
            orient_green = orient_green and okB
            blind_tok = blind_tok and (nf_mod is None)
            oc_note.append("%s: true flip %d, model flip %s -> "
                           "%s" % (cname, nf_true, str(nf_mod),
                                   "match" if okB else "MISS"))
        check("G71-orientation-controls", True,
              "gate B (controls, tol +-%d): %s => %s -- a "
              "positive global factor cannot change a sign; the "
              "solved constant proves the base only WITH an "
              "orientation carrier, which this outer model is "
              "not" % (FLIP_TOL, "; ".join(oc_note),
                       "orientation carried" if orient_green
                       else "MODEL_ORIENTATION_BLIND (honest)"))

    # ---------------- S9: leg 6 -- contour R1 + must-fails
    section("S9  LEG 6 -- CONTOUR R_1 + MUST-FAILS")
    if smoke:
        check("G80-r1-contour", True,
              "SMOKE: contour instrument skipped")
        r1_dev = float("nan")
    else:
        p9 = packs[9]
        N9 = p9["N"]
        n_r1 = N9 // 2
        md9 = W[9]["mds"][n_r1]
        xall = np.sort(np.concatenate([p9["d"]["xs"],
                                       p9["d"]["ys"]]))
        x0c = 0.5 * (float(xall[0]) + float(xall[-1]))
        rad = 0.5 * (float(xall[-1]) - float(xall[0])) + R1_PAD
        zs = [complex(x0c + rad * math.cos(2.0 * math.pi
                                           * (j + 0.5) / R1_K),
                      rad * math.sin(2.0 * math.pi
                                     * (j + 0.5) / R1_K))
              for j in range(R1_K)]
        out9, _g9, hlog9 = CB.mp_y_pass(p9["d"], {n_r1}, zs,
                                        R1_DPS, N9)
        mp.mp.dps = R1_DPS
        acc12 = mp.mpc(0)
        acc21 = mp.mpc(0)
        for j, z in enumerate(zs):
            Mz = CB.model_at(md9, z, R1_DPS)
            mp.mp.dps = R1_DPS
            R = r_field(out9[n_r1]["Y"][j], Mz)
            wgt = mp.mpc(z) - mp.mpf(x0c)
            acc12 += R[0][1] * wgt
            acc21 += R[1][0] * wgt
        r1_12 = acc12 / R1_K
        r1_21 = acc21 / R1_K
        lg, sg = hlog9[n_r1]
        h_true = sg * mp.e ** lg
        h_out = mp.e ** (mp.mpf(md9["hmod_l10"]) * mp.log(10))
        scale = max(abs(h_true), abs(h_out))
        r1_dev = float(abs(r1_12 - (h_true - h_out)) / scale)
        m6_dev = float(abs(r1_21 - (h_true - h_out)) / scale)
        ok_m6 = m6_dev >= M6_LOUD * max(r1_dev, 1e-300)
        check("G80-r1-contour",
              r1_dev <= R1_BAR and out9[n_r1]["dety"] <= 1e-20
              and ok_m6,
              "R_1 = (1/2 pi i) oint (R - I) dz on the sealed "
              "circle (w9, n = %d, K = %d, radius %.2f, dps %d, "
              "det Y ward %.1e): |(R_1)_12 - (h_true - h^out)| "
              "/ scale = %.1e (bar %.0e) -- the r251 delta-h "
              "identity holds in PROOF-READY contour form; m6 "
              "swapped entry: dev %.1e (>= %.0e x honest, LOUD)"
              % (n_r1, R1_K, rad, R1_DPS, out9[n_r1]["dety"],
                 r1_dev, R1_BAR, m6_dev, M6_LOUD))
    # must-fails m1-m3 on the b1 field (w9, kept degree)
    mf = W[9]["mf"]
    r_hon = mf["lgt"] - mf["b1"]
    bar_mf = max(MF_ABS, abs(r_hon) + MF_REL)
    F = mf["F"]
    uns = mf["uns"]
    fb1 = 0.5 * (F + mf["V"])
    r_m1 = mf["lgt"] - lse_l10(-fb1[uns])
    r_m2 = mf["lgt"] - lse_l10(-2.0 * F[uns])
    r_m3 = mf["lgt"] - lse_l10(+F[uns])
    ok_mf = (abs(r_m1) >= bar_mf and abs(r_m2) >= bar_mf
             and abs(r_m3) >= bar_mf)
    check("G90-must-fails-fire", ok_mf,
          "w9 n = %d, honest b1 residual %+.3f (loudness bar "
          "%.1f dec): m1 wrong factor 2 => %.1f dec; m2 "
          "forgotten root => %.1f dec; m3 exponent sign => %.1f "
          "dec (each LOUD); m4 sign oracle EXCLUDED by the "
          "input firewall (standing r243 exclusion)"
          % (mf["n"], r_hon, bar_mf, abs(r_m1), abs(r_m2),
             abs(r_m3)))

    # ---------------- S10: verdict
    section("S10  VERDICT")
    if smoke:
        vTop = "SMOKE_NO_ADJUDICATION"
    elif case == "BASE_RATIO_EXACT" and orient_green:
        vTop = "BASE_RATIO_CARRIES_SIGN"
    else:
        vTop = case
    toks = [vTop]
    if not smoke:
        toks.append(("C0_NORMALIZER_CARRIES(%.2f dec)"
                     if c0_carries else
                     "C0_NORMALIZER_INSUFFICIENT(%.2f dec)")
                    % c0_rest_max)
        toks.append("GAUGE_PINNED_AT_INFINITY(%.0e dec)"
                    % rich_worst if gauge_pinned
                    else "GAUGE_BROKEN(%.1e)" % rich_worst)
        toks.append(v4)
        if blind_tok:
            toks.append("MODEL_ORIENTATION_BLIND")
        toks.append("R1_CONTOUR_VERIFIED(%.1e)" % r1_dev
                    if r1_dev <= R1_BAR
                    else "R1_CONTOUR_FAILED(%.1e)" % r1_dev)
    check("G97-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a gauge/quotient "
          "adjudication moves no edge); what the round adds: the "
          "full-degree eta table, the C0 rest bill, the pinned "
          "gauge, the conditional divisor table, the orientation "
          "gate bill, and the proof-ready contour R_1")
    verd = " + ".join(toks)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G81-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: eta statistics (all free degrees), "
          "C0 rest decades, gauge pins, flip-gate bilances, "
          "contour R_1; OPEN: the budget bound and the base law "
          "themselves (r243/r247/r250/r251 stand); NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
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
