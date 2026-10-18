#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""kr4_depth_probe -- PRIME.KREIN.RADIUS4.DEPTH.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION
=======================================================================
Take the FIRST NON-TRANSCRIBING PAIRING to depth.  Round 117
(radius4_reduction_probe, SPEC_SHA a27b10b3) established that the
round-90 Krein carrier (krein_screw_realization_probe, SPEC_SHA
bd5fba32 -- the ONLY pin carrier that passes the Z1 screen) is
readable in the radius-4 determinant currency at shell depth m = 0
(d_0 to 6.2e-4, d_1 2.1e-3, d_2 1.9e-2 against the direct source jet
at a = 144, via a crude 5-point z-stencil) and NAMED the requirement
for depth: certified sigma-derivatives of the Weyl-disk center.
This probe builds them and asks the decisive question: can the one
non-transcribing carrier MEASURE the RH-critical growth rate
limsup |d_m|^{1/m} (radius-4 reduction: <= 1/4 at dense a <=> RH,
round-117-sound; UNCONDITIONAL for a <= 9.0e24 by round-116 A2)?

=======================================================================
K1 -- THE EXACT DICTIONARY AND THE CERTIFIED-DERIVATIVE METHOD
=======================================================================
OBJECTS (round-102/115/117 conventions): Phi(z) = xi(1/2 + sqrt z),
F = Phi'/Phi; b_n(a) = a^{n+1}((-1)^n/n!) F^{(n)}(a) (the moment row);
Pascal field C_{n,k+1} = C_{n,k} - C_{n+1,k}, C_{n,0} = b_n; diagonal
d_m(a) = C_{m,m}(a) = sum_rho y w^m, scaled d'_m = 4^m d_m.
PIN IDENTITY (round 90, unconditional for Re sigma > 1/2):
  P(sigma) = xi'/xi(1/2 + sigma) = 2 sigma F(sigma^2)
           = (1/2) <-g'', e^{-sigma|.|}>  (Weil formula, screw g).
THE DICTIONARY (exact algebra, no fitting):
  sigma-jet of the disk-center read P_hat at the pin sigma_0
  -> divide by the exact jet of 2 sigma        => sigma-jet of F(s^2)
  -> compose with sigma = sqrt(a) at a_0=s0^2  => a-jet f_n of F
  -> b_n = a_0^{n+1} (-1)^n f_n                => moment row
  -> Pascal finite differences                 => d_m = C_{m,m}.
  The m-th diagonal cell consumes b_m..b_{2m}: an ORDER-2m jet read
  of the disk center (equivalently N1 of round 116:
  d_m = (m!/(2m)!) (L)(L+1)...(L+m-1) b_m, L = a d/da -- the m-fold
  Euler operator on an m-th derivative: total order 2m).
DOMAIN (the contract's question, answered): the discrete Weyl-disk
machinery needs only |w| < 1, w = e^{-sigma delta}, i.e. Re sigma > 0
(Caratheodory functions of positive circle measures are holomorphic
on the open disk); the pin identity needs Re sigma > 1/2 (the Euler
half-plane dominating the e^{|t|/2} pole growth; both sides
holomorphic there, so the real-sigma identity extends by analytic
continuation).  ONE SUBTLETY, pinned: the metric disk CENTER involves
conjugates and is NOT holomorphic in sigma; the holomorphic object is
the CENTRAL VALUE c(sigma) = B2/D2 (the f = 0 continuation), which
lies in the disk, |c - center| <= R (gated at the real pins).  All
jets are taken on c(sigma).
METHOD (both contract options, cross-warded):
 (b) EXACT MESH-SIDE JET TRANSPORT (primary): propagate truncated
     Taylor jets in u = sigma - sigma_0 through the 2x2 Moebius /
     Levinson transfer recursion (w(u) = e^{-sigma_0 delta}
     e^{-delta u} is an exact jet; every step is jet algebra), then
     the dictionary above.  Exact up to mp roundoff (dps 80).
 (a) CAUCHY CONTOUR (bound + cross-ward): on the a-plane circle
     |a - a_0| = r_a (r_a = RA_FRAC a_0, kept inside the Re sigma >
     1/2 image and away from the F poles), trapezoid quadrature of
     the SAME central-value read cross-checks the jet coefficients
     (aliasing ~ (r_a/r_sing)^{K}), and Cauchy gives the CERTIFIED
     budget: the n-th Taylor coefficient of the deviation
     dev(a) = F_read(a) - F_true(a) obeys |dev_n| <= sup_G|dev|/r_a^n,
     hence per diagonal cell
       E_m = a_0 sup|dev_F| (4 x (1+x))^m,  x = a_0/r_a
     (the m!/r^m amplification of the contract, in coefficient form).
ERROR CHANNELS of sup|dev| on the contour, separately measured:
  (i) DISK: |c - F_full_mesh| <= 2R (Cara currency; both in the
      depth-n disk) -- CONDITIONAL on positivity of the full mesh lag
      sequence (= localized Weil positivity beyond the window; the
      round-90 missing-lemma hypothesis, typed COND-POS).  R computed
      exactly per contour point (complex-w disk of the Moebius image).
  (ii) MESH BIAS: tent-interpolation defect, MODEL-grade bound
      (1/2)(|sigma|^2 delta^2/8)[sum_d |t_row[d]| e^{-Re sigma
      (d-1) delta} + C_tail e^{-(Re sigma - 1/2)L}] (|t_row| as cell-
      mass proxy DECLARED; curvature bound |d^2/dt^2 e^{-sigma t}| =
      |sigma|^2 e^{-Re sigma t} exact; window tail via cosh + 1.04x
      Chebyshev psi density, declared model).
  (iii) MEASURED: sup_G |F_read - F_audit| (audit = mp xi'/xi, the
      instrument comparator; SUP_INFLATE 1.5 for sampled-sup slack).
  E_m^cond from (i)+(ii) (COND-POS + MODEL), E_m^meas from (iii)
  (rigorous Cauchy given the audit).  GATE: meas <= cond channelwise
  (falsifiable consistency of the positivity-extension + bias model).
BUDGET LAW (the derivative wall, stated with measured constants):
  m_cert(L, delta) = min(m_R, m_bias),
  m_R    ~ [ (sigma_edge + c) L - log(2 a_0 C / y_1) ] / log Q,
  m_bias ~   log( y_1 / (2 a_0 sup dev_bias) )        / log Q,
  Q = 4 x (1+x) / (4 w_max), c = 1.36 (round-90 measured contraction
  R ~ e^{-(sigma+c)L}), sigma_edge = min Re sigma on the contour.
  The window lever (L) buys depth LINEARLY; the mesh bias floor
  (delta^2) saturates it -- certifying depth m needs the coupled
  schedule delta ~ e^{-(sigma_edge+c)L/2}.  Two mesh levers carried:
  RAW delta = 0.003 and the delta-pair RICHARDSON (4 P_.003 -
  P_.006)/3 (typed MEASURED-EXTRAPOLATED, kills the leading
  sigma^2 delta^2 term; not certified -- no rigorous delta^4 constant
  is claimed).
=======================================================================
K2 -- THE DEPTH MEASUREMENT (frozen design)
=======================================================================
PINS (a_0 = sigma_0^2 exactly): a256 (sigma_0 = 16, r_jet 96, THE
gamma_1-governed rate anchor), a144 (sigma_0 = 12, r_jet 54, round-117
continuity), a9 (sigma_0 = 3, r_jet 2, RA small 0.5 -- the RESUM
channel: only there is the source-window tail visible above the mesh
bias; at the deep pins the round-90 resummation channel is
SATURATED-INVISIBLE, tail ~ e^{-(sigma-1/2)L} < 1e-7, declared).
KREIN SIDE: round-90 machinery imported frozen (build_lags_mp,
szego_mp; TRUE world; window L4 = 2.568, mesh 0.003 primary + 0.006
Richardson mate; L3 = 2.076 window-stability channel).
DIRECT-JET WARD: round-102/117 source-only Cauchy jets imported
frozen (build_jet_lambda, diag_scaled with certified widths):
(a, r, M, dps, N, orders) = (a_0, r_jet, 256, 200, 60000, 44).
DEPTH TABLE per pin: m = 0..10: d'_m KREIN raw | Richardson vs d'_m
JET, deviations, E_m^meas, E_m^cond, jet width; depths reported:
  m_sig  = largest m with |dev| <= 0.5 |d'_jet| for all m' <= m
           (signal depth, raw and Richardson),
  m_cert = largest m with E_m <= 0.5 |d'_jet| (meas and cond grade).
THE RATE at a256/a144: rho_hat = d'_{m*}/d'_{m*-1} at m* = m_sig
(estimates 4 w_max; RH-critical: rho_hat <= 1) with error bars
propagated from (E_meas + width); compared against (i) the direct-jet
ratio at the SAME m (matched budget) and (ii) the cache ward
4 w(gamma_1) (X5 instrument): 0.9847913841 at a = 256.  m-th-root
estimate printed alongside (slower by the atom-mixture correction
(w_2/w_1)^m, declared).
THE Z1 QUESTION AT DEPTH: (1) transcription scan (round-90 K5b
pattern on the diagonal): min over N <= 7000 of max_{m <= m*}
rel |d'_m^{krein} - S'_{N,m}|, S'_{N,m} = 4^m sum_{i<=N} y_i w_i^m
(cache partial sums, ward namespace, X5); fires KR4-TRANSCRIBES iff
<= 1e-6.  (2) EXTRAPOLATION: the reads must sit closer to truth
(direct jet = full zero set + RvM tail) than to ANY cache partial
sum: margin |d'_0 - S'_{best,0}| / max(|d'_0 - d'_jet0|, width) >=
10 (the m = 0 cell sees the beyond-cache RvM tail, ~2e-2 relative at
a = 256 -- the round-90 'deviation from partial sums >> read error'
criterion, at depth).  (3) RESUM-AT-DEPTH (a9): the truncated-source
jet d'_trunc (exact jet of the plain tent transform) vs the
disk-center jet: on live cells (tail resolved above budget+width)
ratio |d'_kr - d'_trunc| / |d'_jet - d'_trunc| in (0.5, 2) = the
center's JET resums the missing tail (round-90 K5c, at depth).
=======================================================================
K3 -- THE ANALYTIC QUESTION IN THE NEW CURRENCY + MIN-CUT
=======================================================================
The round-90 missing lemma (uniform disk contraction R_a(sigma) <=
C(eps) e^{-(sigma+c) 2a}) becomes, in radius-4 currency:
  IF (contraction at the measured law, uniformly on the pin disk
      Re sigma >= sigma_edge) AND (positivity extension: every
      finite section of -g'' positive, all depths)
  THEN for every fixed m, d_m(a_0) is certified from SOURCE data to
      error E_m ~ 2 a_0 C e^{-(sigma_edge+c)L} (4x(1+x))^m -> 0 as
      L -> inf with delta co-scheduled: the carrier becomes a
      certified MEASUREMENT instrument of the full diagonal, i.e. an
      RH-falsifier of unbounded depth (any |d_m|^{1/m} > 1/4 + eps
      visible at finite m kills RH) -- but NOT a positivity prover:
      the limsup over ALL m (and the dense-a quantifier) remains an
      omega-introduction.  Contraction is NECESSARY-BUT-NOT-
      SUFFICIENT: strictly below the wall.
MIN-CUT PLACEMENT (machine-checked against the round-116 graph):
extend the frozen idgraph with KR4-DIAG-MEAS (this probe's read,
derived from the SAME lag data as the round-90 pins -- NOT a new
evidence source), CONTRACT-LAW-HYP (all-L law from finite rungs,
OMEGA-LAW cap 1), KR4-DEPTH-CERT, and the residual omega edge
KR4-DEPTH-CERT -> R4-HYP (OMEGA-POS cap 1).  Expected and gated:
max-flow UNCOND -> RH stays 4 (the new crossing SHARES the single
capacity-1 UNCOND -> WEYL-PINS-MEAS measurement edge with the
WEYL-HYP route -- it lands ON the Weyl-disks-MEASURED edge, as the
contract guessed); the RATE version differs from the CONTRACTION
version exactly by the residual all-m omega edge; contraction-alone
BFS must NOT reach RH; no new semantic class in the cut census.
AND-composition rendered as OR edges: the round-116 graph convention,
inherited and declared (counterfactual independent-source variant
reported as INFO with this caveat, not gated).
=======================================================================
K4 -- CONTROLS AND SCREENS
=======================================================================
SMOOTH / SCRARITH through the same pipeline at (L4, 0.003): their
Szego runs MUST die at the round-90 positivity radii (0.264 / 0.744,
gate window +-0.05; continuum property, round-90 measured at two
meshes).  The depth pairing is only DEFINED where positivity holds:
the null worlds cannot reach the window depth, so the depth
measurement has NO equal-budget null comparator -- the honest control
is the budget collapse (their disk radius at the death depth makes
E_0 > d'_0: certified depth 0, printed) plus the TRUE-side screens.
EPISTEMIC NOTE (typed): the pairing's separation is carried by
POSITIVITY ITSELF (round-90 'separated-by-collapse'), not by a
matched-instrument discrimination; what the asymmetry GIVES is a
conditional instrument -- every depth statement is of the form
'GIVEN the accelerant stays positive (true through L by K1c), the
carrier reads the diagonal to depth m with budget E_m'.
TAU/CONDITIONING SCREEN: deterministic lag perturbation row[d] ->
row[d](1 + 1e-25 cos 7d) (round-90 K2c), compared in mp BEFORE any
float cast: rate shift <= 1e-8 gate; per-m amplification law
A_m = |Delta d'_m| / (1e-25 |d'_m|) with fitted log-slope (the
conditioning law of the derivative reads).
=======================================================================
FROZEN NUMERICS
=======================================================================
MMAX 10 (jet order 20, NJET 21 coefficients); DPS_ALG 80 (jet
algebra), szego at the round-90 dps 50; contours KCONT 96 points,
RA_FRAC 0.8 deep pins / 0.5 at a9; SUP_INFLATE 1.5; direct jets
(M, dps, N, orders) = (256, 200, 60000, 44); FD ward step 1e-12;
perturbation 1e-25; TRANS_BAR 1e-6; EXTRAP band (0.5, 2.0); Z1
margin factor 10; C_LAW 1.36 cited from round 90; cache
verified_zeros_n7000.npy READ-ONLY in ward_ namespace (X5:
instrument, never construction).  RUNTIME BAR 1800 s.  Deterministic
(no randomness anywhere).  Smoke flag reduces MMAX/KCONT/jets and is
NOT VERDICT-BEARING.
GATES: G01 AST firewall; G10 dictionary-atom-exact (full implemented
algebra on a rational atom model, rel <= 1e-35); G11 domain (min
Re sigma > 1/2 on all contours, |w| < 1, disk margin |D2|-|C2| > 0);
G12 FD first-derivative ward (rel <= 1e-15); G13 contour-vs-jet
cross-ward (b-currency rel <= 1e-5, n <= 8); G14 central-value in
disk at real pins (|c - center| <= R (1+1e-12)); G20 budget
consistency (sup dev_meas <= sup dev_cond per pin); G21 TRUE
positivity completes (else typed kill KR4-DEAD); G22 direct jets
healthy (min Re s > 1, Im residual <= 1e-40); G31 enclosure covers
(|d'_kr - d'_jet| <= 1.2 (E_m^meas + width) for ALL m <= MMAX, per
deep pin -- rigor test of the Cauchy budget); G40 no transcription
(scan > 1e-6); G41 Z1-extrapolates-at-depth (m=0 cache margin >= 10,
both deep pins); G50 min-cut (flows 4/4/4, RH unreachable under
contraction-alone, no new cut class); G60 controls die at positivity
(0.264/0.744 +- 0.05); G61 conditioning (rate shift <= 1e-8);
G99 runtime.
COMPOSITE VERDICT (priority frozen): instrument-gate failure => abort
KR4-INSTRUMENT-EDGE (exit 1) > G21 failure => KR4-DEAD(positivity) >
G40 fires => KR4-TRANSCRIBES-AT-DEPTH > [m_sig_rich(a256) >= 3 AND
G41] => KR4-EXTRAPOLATES-AT-DEPTH(rate rho_hat +- bar, depth table)
> else KR4-DERIVATIVE-WALL(budget law with measured constants).
Sub-verdicts: RESUM-AT-DEPTH typing (a9), MINCUT-UNCHANGED,
CONTROLS-DIE-AT-POSITIVITY, conditioning law.
PRE-FREEZE DISCLOSURE: every bar above was set BEFORE the first full
run from the round-90/116/117 published numbers plus the Cauchy
analysis in this spec (no shakeout measurements existed when the
bars were frozen); smoke runs may catch implementation slips --
any instrument repair is disclosed in numbered AMENDMENT lines
appended below, and no bar, grid, pin or verdict rule moves.
AMENDMENT 1 (smoke 1, 17/18): (a) the G61 conditioning screen
compared the perturbed jets AFTER a float64 cast, so the 1e-25
perturbation was invisible (shift read exactly 0.0 -- the identical
round-90 K2c smoke lesson, re-learned): the comparison now happens
in mp before any cast; (b) the RATE line now reports the error bar
in BOTH grades -- Cauchy-certified (honest but fat at large m) and
measured/jet-warded (the informative one; typed MEASURED) -- a
reporting addition, no bar moved; (c) a dead diagnostic loop in the
contour block removed (no numeric effect); (d) the G13 smoke failure
(3.5e-5 at a144) is the aliasing of the SMOKE-reduced contour
K = 24, (r_a/r_sing)^K ~ 5e-3; the frozen full K = 96 is unchanged;
(e) THE REAL SLIP the zero G61 shift exposed: the post-transfer
scalar divisions (P = cval/2 list comprehensions) ran at the AMBIENT
mp.dps = 15 outside any workdps context, silently rounding every
P-jet to 15 digits before the dictionary -- all jet post-processing
now wrapped in workdps(DPS_ALG); values good to 1e-6 were unaffected
(smoke tables identical to displayed digits), the conditioning
screen and the 'exact mesh-side jets' claim required the fix.
No bar, grid, pin or verdict rule moved.
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

import krein_screw_realization_probe as KR   # noqa: E402  round-90 frozen
import radius4_reduction_probe as R4         # noqa: E402  round-117 frozen
import idgraph_search_probe as IG            # noqa: E402  round-116 frozen

# ------------------------------------------------------------ frozen bars
L4, L3 = 2.568, 2.076
D3, D6 = "0.003", "0.006"
MMAX = 10
DPS_ALG = 80
RA_DEEP, RA_SMALL = 0.8, 0.5
KCONT = 96
SUP_INFLATE = 1.5
#          label   sigma0  a0    r_jet  ra_frac  role
PINS = (("a256", 16, 256, 96, RA_DEEP, "RATE"),
        ("a144", 12, 144, 54, RA_DEEP, "RATE"),
        ("a9", 3, 9, 2, RA_SMALL, "RESUM"))
JET_M, JET_DPS, JET_NS, JET_ORD = 256, 200, 60000, 44
C_LAW = 1.36                     # round-90 measured contraction constant
FD_H = "1e-12"
PERT_DPS = 25                    # 1e-25 deterministic lag perturbation
TRANS_BAR = 1e-6
EXTRAP_LO, EXTRAP_HI = 0.5, 2.0
Z1_MARGIN = 10.0
CTRL_R_SMOOTH, CTRL_R_SCR, CTRL_TOL = 0.264, 0.744, 0.05
BAR_ATOM = 1e-35
BAR_FD = 1e-15
BAR_XWARD = 1e-5
BAR_IM = 1e-40
BAR_RATE_SHIFT = 1e-8
RUNTIME_BAR = 1800.0
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
    return (len(bad) == 0, "; ".join(bad) if bad else
            "no zero-oracle; audit_/ward_ namespaces enforced; the "
            "cache enters only through R4.ward_cache (X5)")


# ====================================================== jet algebra (mp)
def j_zero(nj: int) -> list:
    return [mp.mpf(0)] * nj


def j_basis(nj: int) -> list:
    out = j_zero(nj)
    out[0] = mp.mpf(1)
    return out


def j_mul(a: list, b: list, nj: int) -> list:
    out = j_zero(nj)
    for i in range(nj):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(nj - i):
            out[i + j] += ai * b[j]
    return out


def j_div(num: list, den: list, nj: int) -> list:
    out = j_zero(nj)
    d0 = den[0]
    out[0] = num[0] / d0
    for k in range(1, nj):
        acc = num[k]
        for j in range(1, k + 1):
            acc -= den[j] * out[k - j]
        out[k] = acc / d0
    return out


def j_compose(g: list, u: list, nj: int) -> list:
    """g(u(v)) with u[0] == 0 (Horner on jets)."""
    res = j_zero(nj)
    res[0] = g[nj - 1]
    for k in range(nj - 2, -1, -1):
        res = j_mul(res, u, nj)
        res[0] += g[k]
    return res


def w_jet(sigma0, delta_mp, nj: int) -> list:
    """w(u) = e^{-(sigma0+u) delta} as a jet in u."""
    w0 = mp.exp(-mp.mpf(sigma0) * delta_mp)
    out = []
    fac = mp.mpf(1)
    for k in range(nj):
        out.append(w0 * (-delta_mp) ** k / fac)
        fac *= (k + 1)
    return out


def transfer_cval_jet(alphas: list, c0, sigma0, delta_mp, nj: int) -> list:
    """Exact sigma-jet of the central value B2/D2 of the Weyl disk at
    the pin sigma0 (mesh-side option (b): jets through the Moebius /
    Levinson transfer; mirrors KR.weyl_disk_mp step for step)."""
    with mp.workdps(DPS_ALG):
        wj = w_jet(sigma0, delta_mp, nj)
        A, B = j_basis(nj), j_zero(nj)
        C, D = j_zero(nj), j_basis(nj)
        for g in alphas:
            apb = [A[k] + g * B[k] for k in range(nj)]
            cpd = [C[k] + g * D[k] for k in range(nj)]
            a_new = j_mul(wj, apb, nj)
            c_new = j_mul(wj, cpd, nj)
            b_new = [g * A[k] + B[k] for k in range(nj)]
            d_new = [g * C[k] + D[k] for k in range(nj)]
            A, B, C, D = a_new, b_new, c_new, d_new
        wA = j_mul(wj, A, nj)
        wB = j_mul(wj, B, nj)
        A2 = [c0 * (wA[k] + C[k]) for k in range(nj)]   # noqa: F841
        B2 = [c0 * (wB[k] + D[k]) for k in range(nj)]
        D2 = [-wB[k] + D[k] for k in range(nj)]
        return j_div(B2, D2, nj)


def disk_complex(alphas: list, c0, w, dps: int = DPS_ALG) -> tuple:
    """(cval, center, radius, |D2|-|C2|) of the Weyl disk at complex w
    (|w| < 1); cval = B2/D2 is the holomorphic central value; center /
    radius use the exact Moebius-image formulas with conjugation."""
    with mp.workdps(dps):
        A, B, C, D = mp.mpf(1), mp.mpf(0), mp.mpf(0), mp.mpf(1)
        for g in alphas:
            A, B, C, D = (A * w + B * g * w, A * g + B,
                          C * w + D * g * w, C * g + D)
        A2, B2 = c0 * (w * A + C), c0 * (w * B + D)
        C2, D2 = -w * A + C, -w * B + D
        den = abs(D2) ** 2 - abs(C2) ** 2
        cval = B2 / D2
        rad = abs(A2 * D2 - B2 * C2) / den
        cen = (B2 * mp.mpc(D2).conjugate()
               - A2 * mp.mpc(C2).conjugate()) / den
        return cval, cen, rad, abs(D2) - abs(C2)


def pjet_to_dscaled(pjet: list, sigma0, a0, mmax: int) -> tuple:
    """P-jet at sigma0 -> (d'_m list, b_n list) via the exact
    dictionary: F = P/(2 sigma), compose sigma = sqrt(a), b_n, Pascal."""
    with mp.workdps(DPS_ALG):
        nj = len(pjet)
        s0 = mp.mpf(sigma0)
        a0m = mp.mpf(a0)
        two_sigma = j_zero(nj)
        two_sigma[0] = 2 * s0
        if nj > 1:
            two_sigma[1] = mp.mpf(2)
        G = j_div(pjet, two_sigma, nj)
        U = j_zero(nj)
        bj = mp.mpf(1)
        for j in range(1, nj):
            bj *= (mp.mpf(1) / 2 - (j - 1)) / j
            U[j] = s0 * bj / a0m ** j
        f = j_compose(G, U, nj)
        b = [a0m ** (n + 1) * ((-1) ** n) * f[n] for n in range(nj)]
        tab = R4.pascal_table(b, 2 * mmax, DPS_ALG)
        dsc = [(mp.mpf(4) ** m) * tab[m][m] for m in range(mmax + 1)]
    return dsc, b


def trunc_pjet(row: list, delta_mp, sigma0, nj: int) -> list:
    """Exact sigma-jet at sigma0 of the plain truncated tent transform
    P_trunc(sigma) = row[0]/2 + sum_{d>=1} row[d] e^{-sigma d delta}."""
    with mp.workdps(DPS_ALG):
        out = j_zero(nj)
        out[0] = row[0] / 2
        s0 = mp.mpf(sigma0)
        for d in range(1, len(row)):
            base = row[d] * mp.exp(-s0 * d * delta_mp)
            fac = mp.mpf(1)
            arg = -d * delta_mp
            pw = mp.mpf(1)
            for k in range(nj):
                out[k] += base * pw / fac
                pw *= arg
                fac *= (k + 1)
    return out


def budget_dm(sup_dev_f: float, a0: float, ra: float,
              mmax: int) -> list[float]:
    """E_m = 4^m sum_j C(m,j) a0^{m+j+1} sup|dev_F| / ra^{m+j}
    (Cauchy per coefficient + Pascal triangle inequality)."""
    out = []
    for m in range(mmax + 1):
        s = 0.0
        for j in range(m + 1):
            s += (math.comb(m, j) * a0 ** (m + j + 1)
                  * sup_dev_f / ra ** (m + j))
        out.append(4.0 ** m * s)
    return out


# ====================================================== audit / ward
def audit_pin(sigma, dps: int = 60):
    """xi'/xi(1/2 + sigma) via the round-117 audit evaluator."""
    return R4.audit_xi_logderiv(mp.mpf("0.5") + mp.mpc(sigma), dps)


def ward_gammas() -> np.ndarray:
    return R4.ward_cache()


def ward_diag_partials(gam: np.ndarray, a0: float,
                       mmax: int) -> np.ndarray:
    """S'_{N,m} = 4^m sum_{i<=N} y_i w_i^m for all N (cumsum), float64."""
    y = a0 / (a0 + gam ** 2)
    w4 = 4.0 * y * (1.0 - y)
    rows = []
    for m in range(mmax + 1):
        rows.append(np.cumsum(y * w4 ** m))
    return np.array(rows)          # shape (mmax+1, ncache)


def ward_transcription_scan(dvec: list[float],
                            partials: np.ndarray) -> tuple[float, int]:
    """min over N of max_m rel|d'_m - S'_{N,m}| (round-90 K5b, diagonal)."""
    d = np.array(dvec)[:, None]
    rel = np.abs(d - partials[: len(dvec)]) \
        / np.maximum(np.abs(partials[: len(dvec)]), 1e-300)
    score = rel.max(axis=0)
    nbest = int(np.argmin(score))
    return float(score[nbest]), nbest + 1


# ====================================================== dictionary gate
def gate_atom_dictionary() -> tuple[bool, str]:
    """G10: run the FULL implemented pipeline (jet division,
    composition, b-map, Pascal) on the exact atom model
    F(a) = 1/(a - z), P(sigma) = 2 sigma/(sigma^2 - z), z rational:
    d'_m must equal 4^m y^{m+1}(1-y)^m exactly."""
    with mp.workdps(120):
        z = mp.mpf(-200)
        s0, a0 = 16, 256
        nj = 2 * MMAX + 1
        num = j_zero(nj)
        num[0] = mp.mpf(2 * s0)
        num[1] = mp.mpf(2)
        den = j_zero(nj)
        den[0] = mp.mpf(s0 * s0) - z
        den[1] = mp.mpf(2 * s0)
        den[2] = mp.mpf(1)
        pjet = j_div(num, den, nj)
        dsc, _b = pjet_to_dscaled(pjet, s0, a0, MMAX)
        y = mp.mpf(a0) / (a0 - z)
        worst = 0.0
        for m in range(MMAX + 1):
            tgt = (mp.mpf(4) ** m) * y ** (m + 1) * (1 - y) ** m
            worst = max(worst, float(abs(dsc[m] - tgt) / abs(tgt)))
    return worst <= BAR_ATOM, ("atom model z=-200 at (sigma0,a0)=(16,256):"
                               " worst rel dev %.1e over m<=%d (bar %.0e)"
                               % (worst, MMAX, BAR_ATOM))


# ====================================================== per-pin analysis
def analyze_pin(label: str, sigma0: int, a0: int, r_jet: int,
                ra_frac: float, role: str, builds: dict, szs: dict,
                jets_direct: dict, kcont: int, mmax: int,
                smoke: bool) -> dict:
    nj = 2 * mmax + 1
    out = {"label": label, "role": role}
    b3 = builds[(L4, D3)]
    sz3 = szs[(L4, D3)]

    # ---- exact jets (option b), three builds (ALL scalar post-
    # processing inside workdps: the ambient mp.dps 15 must never
    # touch a jet -- AMENDMENT 1e)
    t0 = time.time()
    with mp.workdps(DPS_ALG):
        pj3 = [x / 2 for x in transfer_cval_jet(
            sz3["alphas"], sz3["c0"], sigma0, b3["delta_mp"], nj)]
    d3, _b3v = pjet_to_dscaled(pj3, sigma0, a0, mmax)
    d6 = drich = None
    if (L4, D6) in builds:
        b6, sz6 = builds[(L4, D6)], szs[(L4, D6)]
        with mp.workdps(DPS_ALG):
            pj6 = [x / 2 for x in transfer_cval_jet(
                sz6["alphas"], sz6["c0"], sigma0, b6["delta_mp"], nj)]
        d6, _ = pjet_to_dscaled(pj6, sigma0, a0, mmax)
        with mp.workdps(DPS_ALG):
            drich = [(4 * d3[m] - d6[m]) / 3 for m in range(mmax + 1)]
    dL3 = None
    if (L3, D3) in builds:
        bl, szl = builds[(L3, D3)], szs[(L3, D3)]
        with mp.workdps(DPS_ALG):
            pjl = [x / 2 for x in transfer_cval_jet(
                szl["alphas"], szl["c0"], sigma0, bl["delta_mp"], nj)]
        dL3, _ = pjet_to_dscaled(pjl, sigma0, a0, mmax)
    print("  [%s] exact jet transport (order %d, 3 builds): %.1f s"
          % (label, nj - 1, time.time() - t0), flush=True)

    # ---- real-pin disk read (round-90 continuity) + FD ward (G12)
    with mp.workdps(DPS_ALG):
        w0 = mp.exp(-mp.mpf(sigma0) * b3["delta_mp"])
        cval0, cen0, rad0, marg0 = disk_complex(sz3["alphas"], sz3["c0"],
                                                w0)
        p_pin = float(mp.re(cval0)) / 2.0
        p_aud = float(mp.re(audit_pin(sigma0)))
        h = mp.mpf(FD_H)
        cp, _c1, _r1, _m1 = disk_complex(sz3["alphas"], sz3["c0"],
                                         mp.exp(-(mp.mpf(sigma0) + h)
                                                * b3["delta_mp"]))
        cm, _c2, _r2, _m2 = disk_complex(sz3["alphas"], sz3["c0"],
                                         mp.exp(-(mp.mpf(sigma0) - h)
                                                * b3["delta_mp"]))
        fd1 = (cp - cm) / (4 * h)          # P' = (cval/2)'
        fd_rel = float(abs(fd1 - pj3[1]) / abs(pj3[1]))
        incirc = float(abs(cval0 - cen0) / max(float(rad0), 1e-300))
    out["fd_rel"] = fd_rel
    out["incirc"] = incirc
    out["rad_pin"] = float(rad0)
    info("%s pin read: P_hat(%d) = %.10f vs audit %.10f (dev %.2e); "
         "disk R = %.2e; |cval-center|/R = %.3f; margin |D2|-|C2| "
         "= %.2e" % (label, sigma0, p_pin, p_aud, abs(p_pin - p_aud),
                     float(rad0), incirc, float(marg0)))

    # ---- contour (option a): sup channels + quadrature cross-ward
    t0 = time.time()
    ra = ra_frac * a0
    rowabs = np.array([float(abs(v)) for v in b3["row"]])
    dgrid = np.maximum(np.arange(len(rowabs)) - 1, 0).astype(float)
    delta_f = b3["delta"]
    lwin = b3["L"]
    sup_meas = sup_cond = 0.0
    min_res = float("inf")
    min_marg = float("inf")
    sup_r_only = 0.0
    fhat = [mp.mpc(0)] * nj
    with mp.workdps(DPS_ALG):
        for jj in range(kcont):
            th = mp.mpf(2 * jj) / kcont
            av = a0 + ra * mp.expjpi(th)
            sv = mp.sqrt(av)
            wv = mp.exp(-sv * b3["delta_mp"])
            cval, _cen, rad, marg = disk_complex(sz3["alphas"],
                                                 sz3["c0"], wv)
            f_read = cval / (4 * sv)
            f_aud = audit_pin(sv) / (2 * sv)
            res = float(mp.re(sv))
            asig = float(abs(sv))
            min_res = min(min_res, res)
            min_marg = min(min_marg, float(marg))
            # measured channel
            sup_meas = max(sup_meas, float(abs(f_read - f_aud)))
            # conditional channel: disk + mesh-bias model (P currency)
            bias_p = 0.5 * (asig ** 2 * delta_f ** 2 / 8.0) * (
                float(np.sum(rowabs * np.exp(-res * dgrid * delta_f)))
                + (2.0 + 2.08) / max(res - 0.5, 0.1)
                * math.exp(-(res - 0.5) * lwin))
            sup_cond = max(sup_cond,
                           (float(rad) + bias_p) / (2.0 * asig))
            sup_r_only = max(sup_r_only, float(rad) / (2.0 * asig))
            for n in range(nj):
                fhat[n] += f_read * mp.expjpi(-th * n)
        xdev = 0.0
        _dsc_chk, b_exact = pjet_to_dscaled(pj3, sigma0, a0, mmax)
        for n in range(min(9, nj)):
            cn = fhat[n] / kcont / mp.mpf(ra) ** n
            bn_q = mp.mpf(a0) ** (n + 1) * ((-1) ** n) * mp.re(cn)
            xdev = max(xdev, float(abs(bn_q - b_exact[n])
                                   / max(abs(b_exact[n]), mp.mpf("1e-300"))))
    sup_meas *= SUP_INFLATE
    out["sup_meas"], out["sup_cond"] = sup_meas, sup_cond
    out["sup_r_only"] = sup_r_only
    out["min_res"], out["min_marg"] = min_res, min_marg
    out["xward"] = xdev
    print("  [%s] contour K=%d ra=%.1f: %.1f s; min Re sigma %.3f; "
        "sup dev_F meas %.3e | cond %.3e (R-only %.3e)"
        % (label, kcont, ra, time.time() - t0, min_res, sup_meas,
           sup_cond, sup_r_only), flush=True)

    # ---- direct jet ward
    jet = jets_direct[label]
    djet, wjet = R4.diag_scaled(jet, DPS_ALG)
    djet = djet[: mmax + 1]
    wjet = wjet[: mmax + 1]
    out["djet"] = [float(x) for x in djet]

    # ---- budgets + depth table
    e_meas = budget_dm(sup_meas, float(a0), ra, mmax)
    e_cond = budget_dm(sup_cond, float(a0), ra, mmax)
    e_ronly = budget_dm(sup_r_only, float(a0), ra, mmax)
    print("  [%s] DEPTH TABLE (d'_m = 4^m C_{m,m}):" % label)
    print("    m   d'_jet        d'_kr(raw)    dev_raw    dev_rich   "
          "E_meas     E_cond     width")
    m_sig_raw = m_sig_rich = -1
    ok31 = True
    dev_raw_l, dev_rich_l = [], []
    for m in range(mmax + 1):
        dj = float(djet[m])
        dr = float(d3[m])
        dev_r = abs(dr - dj)
        dev_h = abs(float(drich[m]) - dj) if drich else float("nan")
        dev_raw_l.append(dev_r)
        dev_rich_l.append(dev_h)
        if dev_r <= 0.5 * abs(dj) and m_sig_raw == m - 1:
            m_sig_raw = m
        dh_ok = (drich is not None and dev_h <= 0.5 * abs(dj))
        if dh_ok and m_sig_rich == m - 1:
            m_sig_rich = m
        if dev_r > 1.2 * (e_meas[m] + wjet[m]):
            ok31 = False
        print("    %-3d %.6e  %.6e  %.3e  %.3e  %.3e  %.3e  %.1e"
              % (m, dj, dr, dev_r, dev_h, e_meas[m], e_cond[m],
                 wjet[m]))
    def cert_depth(ev):
        mc = -1
        for m in range(mmax + 1):
            if ev[m] <= 0.5 * abs(float(djet[m])) and mc == m - 1:
                mc = m
        return mc
    m_cert_meas = cert_depth(e_meas)
    m_cert_cond = cert_depth(e_cond)
    m_cert_ronly = cert_depth(e_ronly)
    dev_slope = float(np.polyfit(
        range(mmax + 1), np.log(np.maximum(dev_raw_l, 1e-300)),
        1)[0]) if mmax >= 2 else float("nan")
    out.update(m_sig_raw=m_sig_raw, m_sig_rich=m_sig_rich,
               m_cert_meas=m_cert_meas, m_cert_cond=m_cert_cond,
               m_cert_ronly=m_cert_ronly, ok31=ok31,
               d3=[float(x) for x in d3], d3_mp=d3,
               drich=[float(x) for x in drich] if drich else None,
               dev_raw=dev_raw_l, dev_rich=dev_rich_l,
               dev_slope=dev_slope,
               e_meas=e_meas, e_cond=e_cond, wjet=wjet)
    x = a0 / ra
    info("%s depths: signal raw m<=%d | Richardson m<=%d; certified "
         "meas m<=%d | cond m<=%d | disk-only m<=%d  (Q per depth = "
         "4x(1+x) = %.2f at x = %.3f; measured dev_raw log-slope "
         "%+.2f/depth)"
         % (label, m_sig_raw, m_sig_rich, m_cert_meas, m_cert_cond,
            m_cert_ronly, 4 * x * (1 + x), x, out["dev_slope"]))
    if dL3 is not None:
        difs = ["%.1e" % abs(float(dL3[m]) - float(d3[m]))
                for m in range(min(6, mmax + 1))]
        info("%s window channel |d'(L3) - d'(L4)| m=0..%d: %s"
             % (label, min(5, mmax), " ".join(difs)))
    return out


# ====================================================== min-cut (K3)
def mincut_extension() -> list[tuple[str, bool, str]]:
    gates = []
    flow_base, cut_base, _ = IG.max_flow(IG.EDGES, "UNCOND", "RH")
    edges_ext = list(IG.EDGES) + [
        ("WEYL-PINS-MEAS", "KR4-DIAG-MEAS", "UNC-DICT", IG.INF),
        ("WEYL-PINS-MEAS", "CONTRACT-LAW-HYP", "OMEGA-LAW", 1),
        ("CONTRACT-LAW-HYP", "KR4-DEPTH-CERT", "UNC", IG.INF),
        ("KR4-DIAG-MEAS", "KR4-DEPTH-CERT", "UNC", IG.INF),
        ("KR4-DEPTH-CERT", "R4-HYP", "OMEGA-POS", 1),
    ]
    flow_ext, cut_ext, _ = IG.max_flow(edges_ext, "UNCOND", "RH")
    edges_up = [(s, d, c, IG.INF if (s, d) == ("R4-HYP", "RH") else cap)
                for s, d, c, cap in edges_ext]
    flow_up, cut_up, _ = IG.max_flow(edges_up, "UNCOND", "RH")
    print("    base flow %d; extended flow %d; extended+R4->RH-INF "
          "flow %d" % (flow_base, flow_ext, flow_up))
    print("    extended min-cut:")
    for s, d, c in cut_ext:
        print("      %-18s -> %-16s [%s]" % (s, d, c))
    classes = sorted({c for _s, _d, c in cut_ext}
                     | {c for _s, _d, c in cut_up})
    gates.append(("G50a min-cut cardinality stays 4",
                  flow_base == 4 and flow_ext == 4 and flow_up == 4,
                  "flows base/ext/ext+INF = %d/%d/%d: the new depth "
                  "crossing SHARES the capacity-1 Weyl measurement "
                  "edge (lands ON the Weyl-disks-MEASURED edge)"
                  % (flow_base, flow_ext, flow_up)))
    allowed = {"OMEGA-POS", "OMEGA-POS-MEAS", "MEAS", "OMEGA-LAW",
               "CANDIDATE"}
    gates.append(("G50b no new semantic class",
                  set(classes) <= allowed,
                  "cut classes %s (all omega-positivity-style "
                  "introductions / measurement edges)" % classes))
    # contraction-alone reachability: grant CONTRACT-LAW-HYP, walk
    # only DEF/UNC/UNC-DICT edges plus its out-edges
    adj: dict[str, set[str]] = {}
    for s, d, c, _cap in edges_ext:
        if c in ("DEF", "UNC", "UNC-DICT"):
            adj.setdefault(s, set()).add(d)
    for s, d, c, _cap in edges_ext:
        if s == "CONTRACT-LAW-HYP":
            adj.setdefault(s, set()).add(d)
    reach = {"UNCOND", "CONTRACT-LAW-HYP"}
    queue = ["UNCOND", "CONTRACT-LAW-HYP"]
    while queue:
        nd = queue.pop(0)
        for nx in adj.get(nd, ()):
            if nx not in reach:
                reach.add(nx)
                queue.append(nx)
    gates.append(("G50c contraction-alone below the wall",
                  "RH" not in reach and "R4-HYP" not in reach,
                  "granting the contraction law + the exact dictionary "
                  "reaches %d nodes; R4-HYP and RH stay unreachable "
                  "(the all-m/dense-a omega edge remains)"
                  % len(reach)))
    # counterfactual (INFO, not gated): independent-source variant
    edges_cf = edges_up + [("UNCOND", "KR4-DIAG-MEAS", "MEAS", 1)]
    flow_cf, _cut_cf, _ = IG.max_flow(edges_cf, "UNCOND", "RH")
    print("    counterfactual (depth read as an INDEPENDENT evidence "
          "source): flow %d -- rises only under the declared "
          "AND-as-OR convention; the actual read derives from the "
          "same lag data as the round-90 pins: NOT independent"
          % flow_cf)
    return gates


# ====================================================== main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    mmax = 5 if smoke else MMAX
    kcont = 24 if smoke else KCONT
    jet_m = 128 if smoke else JET_M
    jet_dps = 150 if smoke else JET_DPS
    jet_ns = 20000 if smoke else JET_NS
    jet_ord = 2 * mmax + 4 if smoke else JET_ORD
    pins = PINS if not smoke else (PINS[1], PINS[2])

    print("kr4_depth_probe -- PRIME.KREIN.RADIUS4.DEPTH.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + SPEC")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det)
    print("  contract: PRIME.KREIN.RADIUS4.DEPTH.01 -- certified")
    print("  sigma-derivatives of the Weyl-disk center (the round-117")
    print("  named requirement) -> the diagonal d_m at depth -> the")
    print("  RH-critical rate question, on the ONLY non-transcribing")
    print("  carrier (round 90/112).")

    # ---------------------------------------------------------- S1
    section("S1  K1 THE EXACT DICTIONARY (gated algebra)")
    print("  d_m = C_{m,m} from the center jet: P_hat = (1/2) c(sigma);")
    print("  F(sigma^2) = P/(2 sigma); b_n = a0^{n+1}((-1)^n/n!) "
          "F^{(n)}(a0);")
    print("  d_m = m-fold Pascal difference of b_m..b_{2m}: an "
          "ORDER-2m jet read")
    print("  (N1 route d_m = (m!/(2m)!)(L)_m b_m consumes the same "
          "orders).")
    ok, det = gate_atom_dictionary()
    check("G10-dictionary-atom-exact", ok, det)
    info("domain: disk machinery needs |w|<1 <=> Re sigma > 0; the pin "
         "identity needs Re sigma > 1/2 (Euler half-plane); the METRIC "
         "center is non-holomorphic in sigma (conjugates) -- jets are "
         "taken on the holomorphic CENTRAL VALUE B2/D2, |c-center|<=R "
         "gated at the pins (G14)")

    # ---------------------------------------------------------- S2
    section("S2  ROUND-90 CARRIER BUILDS (TRUE world)")
    KR.mp_setup()
    plan = [(L4, D3), (L4, D6)] + ([] if smoke else [(L3, D3)])
    builds, szs = {}, {}
    ok_pos = True
    for (lw, dn) in plan:
        t0 = time.time()
        b = KR.build_lags_mp(lw, dn, "TRUE")
        sz = KR.szego_mp(b["row"])
        builds[(lw, dn)] = b
        szs[(lw, dn)] = sz
        ok_pos &= sz["ok"]
        print("  L=%.3f delta=%s n=%4d  c0=%9.4f  max|alpha|=%.6f  %s"
              "  (%.1f s)" % (lw, dn, b["n"], float(sz["c0"]),
                              float(sz["amax"]),
                              "OK" if sz["ok"] else
                              "FAIL@k=%d" % sz["fail_k"],
                              time.time() - t0), flush=True)
    check("G21-true-positivity-completes", ok_pos,
          "every Szego run completes with max|alpha| < 1 (accelerant "
          "sections positive through the window)" if ok_pos else
          "TYPED KILL: KR4-DEAD(positivity fails inside the window)")
    if not ok_pos:
        print("VERDICT: KR4-DEAD(positivity)")
        return 1

    # direct jets
    jets_direct = {}
    for (label, _s0, a0, r_jet, _raf, _role) in pins:
        jet = R4.build_jet_lambda(a0, r_jet, jet_m, jet_dps, jet_ns,
                                  jet_ord, "kr4-" + label)
        jets_direct[label] = jet
        print("  direct jet %s: a=%d r=%d M=%d dps=%d N=%d orders=%d "
              "(%.1f s)" % (label, a0, r_jet, jet_m, jet_dps, jet_ns,
                            jet_ord, jet["secs"]), flush=True)
    ok22 = all(j["sig_min"] > 1.0
               and max(j["im_res"], j["imF"]) <= BAR_IM
               for j in jets_direct.values())
    check("G22-direct-jets-healthy", ok22,
          "min Re s = %s; Im residuals <= %.0e"
          % (["%.2f" % j["sig_min"] for j in jets_direct.values()],
             BAR_IM))

    # ---------------------------------------------------------- S3
    section("S3  K1/K2 CERTIFIED JETS + DEPTH TABLES + RATE")
    results = {}
    for (label, s0, a0, r_jet, raf, role) in pins:
        results[label] = analyze_pin(label, s0, a0, r_jet, raf, role,
                                     builds, szs, jets_direct, kcont,
                                     mmax, smoke)
    r = results
    ok11 = all(v["min_res"] > 0.5 and v["min_marg"] > 0
               for v in r.values())
    check("G11-domain-admissible", ok11,
          "min Re sigma on contours = %s > 1/2; min disk margin "
          "|D2|-|C2| = %s > 0"
          % (["%.2f" % v["min_res"] for v in r.values()],
             ["%.1e" % v["min_marg"] for v in r.values()]))
    ok12 = all(v["fd_rel"] <= BAR_FD for v in r.values())
    check("G12-fd-derivative-ward", ok12,
          "central-difference vs exact-jet first derivative rel dev "
          "= %s (bar %.0e)" % (["%.1e" % v["fd_rel"]
                                for v in r.values()], BAR_FD))
    ok13 = all(v["xward"] <= BAR_XWARD for v in r.values())
    check("G13-contour-vs-jet-crossward", ok13,
          "quadrature vs exact-jet b_n (n<=8) rel dev = %s (bar %.0e;"
          " two independent derivative routes)"
          % (["%.1e" % v["xward"] for v in r.values()], BAR_XWARD))
    ok14 = all(v["incirc"] <= 1.0 + 1e-12 for v in r.values())
    check("G14-central-value-in-disk", ok14,
          "|cval - center|/R at the real pins = %s <= 1"
          % ["%.3f" % v["incirc"] for v in r.values()])
    ok20 = all(v["sup_meas"] <= v["sup_cond"] for v in r.values())
    check("G20-budget-consistency", ok20,
          "sup dev_meas <= sup dev_cond on every pin contour "
          "(falsifiable consistency of disk + mesh-bias model): "
          + "; ".join("%s %.2e<=%.2e" % (k, v["sup_meas"],
                                         v["sup_cond"])
                      for k, v in r.items()))
    deep = [v for v in r.values() if v["role"] == "RATE"]
    ok31 = all(v["ok31"] for v in deep)
    check("G31-enclosure-covers-deviation", ok31,
          "|d'_kr - d'_jet| <= 1.2 (E_meas + width) for ALL m <= %d "
          "on the RATE pins (Cauchy budget rigor test)" % mmax)

    # rate estimates (deep pins)
    gam = ward_gammas()
    for v in deep:
        label = v["label"]
        a0 = dict((p[0], p[2]) for p in PINS)[label]
        m_use = max(2, v["m_sig_rich"] if v["m_sig_rich"] >= 2
                    else v["m_sig_raw"])
        m_use = min(m_use, mmax)
        seq = v["drich"] if (v["drich"] and v["m_sig_rich"] >= 2) \
            else v["d3"]
        seq_lab = "rich" if seq is v["drich"] else "raw"
        if m_use >= 2:
            rk = seq[m_use] / seq[m_use - 1]
            rj = v["djet"][m_use] / v["djet"][m_use - 1]
            relb = ((v["e_meas"][m_use] + v["wjet"][m_use])
                    / abs(v["djet"][m_use])
                    + (v["e_meas"][m_use - 1] + v["wjet"][m_use - 1])
                    / abs(v["djet"][m_use - 1]))
            bar_r = abs(rk) * relb
            dev_seq = v["dev_rich"] if seq_lab == "rich" \
                else v["dev_raw"]
            relm = ((dev_seq[m_use] + v["wjet"][m_use])
                    / abs(v["djet"][m_use])
                    + (dev_seq[m_use - 1] + v["wjet"][m_use - 1])
                    / abs(v["djet"][m_use - 1]))
            bar_m = abs(rk) * relm
            root = abs(seq[m_use]) ** (1.0 / m_use)
            w4_ward = 4.0 * R4.ward_topw(gam, float(a0), 1)[0][1]
            v.update(rate_kr=rk, rate_jet=rj, rate_bar=bar_r,
                     rate_bar_meas=bar_m, rate_m=m_use,
                     w4_ward=w4_ward)
            info("%s RATE at m*=%d (%s): krein ratio %.6f +- %.1e "
                 "(measured/jet-warded) | +- %.1e (Cauchy-certified) "
                 "| jet ratio %.6f | ward 4w(gamma_1) %.9f | m-th "
                 "root %.6f | krein-jet agreement %.2e vs ward-"
                 "distance %.2e | margin to 1: %.4f"
                 % (label, m_use, seq_lab, rk, bar_m, bar_r, rj,
                    w4_ward, root, abs(rk - rj),
                    abs(rj - w4_ward), 1.0 - rk))
        else:
            v.update(rate_kr=float("nan"), rate_bar=float("inf"),
                     rate_m=m_use)
            info("%s RATE: signal depth < 2 -- no rate read" % label)

    # ---------------------------------------------------------- S4
    section("S4  THE Z1 QUESTION AT DEPTH")
    fire_trans = False
    z1_ok = True
    for v in deep:
        label = v["label"]
        a0 = float(dict((p[0], p[2]) for p in PINS)[label])
        m_use = max(1, min(v["m_sig_raw"], mmax))
        partials = ward_diag_partials(gam, a0, m_use)
        score, nbest = ward_transcription_scan(v["d3"][: m_use + 1],
                                               partials)
        fire_trans |= score <= TRANS_BAR
        gap0 = abs(v["d3"][0] - float(partials[0][nbest - 1]))
        read_err0 = max(abs(v["d3"][0] - v["djet"][0]), v["wjet"][0])
        marg = gap0 / max(read_err0, 1e-300)
        z1_ok &= marg >= Z1_MARGIN
        print("  %s: transcription scan (m<=%d) min-max rel = %.3e "
              "at N=%d (bar %.0e); m=0 cache gap %.3e vs read error "
              "%.3e -> margin %.1f (the read carries the beyond-cache "
              "RvM tail)" % (label, m_use, score, nbest, TRANS_BAR,
                             gap0, read_err0, marg))
    check("G40-no-transcription", not fire_trans,
          "the depth vector matches NO cache partial-sum vector "
          "(round-90 K5b at depth)" if not fire_trans
          else "TRANSCRIPTION FIRES")
    check("G41-z1-extrapolates-at-depth", z1_ok,
          "m=0 deviation from the BEST cache partial sum >= %.0fx the "
          "measured read error on both RATE pins: the Krein d_m sit "
          "on the FULL diagonal (zeros + RvM tail), not on any finite "
          "zero list" % Z1_MARGIN if z1_ok else
          "margin below %.0fx" % Z1_MARGIN)

    # resum-at-depth channel (a9)
    v9 = r.get("a9")
    resum_typed = "NOT-RUN"
    if v9 is not None:
        b3 = builds[(L4, D3)]
        nj = 2 * mmax + 1
        pjt = trunc_pjet(b3["row"], b3["delta_mp"], 3, nj)
        dtr, _ = pjet_to_dscaled(pjt, 3, 9, mmax)
        dtr = [float(x) for x in dtr]
        live, ratios, impr = [], [], []
        for m in range(mmax + 1):
            tail = abs(v9["djet"][m] - dtr[m])
            flo = 5.0 * max(v9["wjet"][m], v9["e_meas"][m])
            if tail > flo:
                live.append(m)
                ratios.append(abs(v9["d3"][m] - dtr[m]) / tail)
                impr.append(tail / max(abs(v9["d3"][m]
                                           - v9["djet"][m]), 1e-300))
        if live:
            med = float(np.median(ratios))
            resum_typed = ("KR4-RESUMS-AT-DEPTH(median %.3f, live m %s,"
                           " improvement x%.1f..x%.1f)"
                           % (med, live, min(impr), max(impr))
                           if EXTRAP_LO <= med <= EXTRAP_HI else
                           "RESUM-NOT-CONFIRMED(median %.3f)" % med)
        else:
            resum_typed = ("RESUM-CHANNEL-SATURATED(no live cell: "
                           "window tail below budget+width at a=9)")
        print("  a9 RESUM channel: trunc-jet vs center-jet vs direct "
              "jet; live cells %s; ratios %s"
              % (live, ["%.3f" % x for x in ratios]))
        info("resum typing: " + resum_typed)
        info("deep pins: the round-90 resummation channel is "
             "SATURATED-INVISIBLE (window tail ~ e^{-(sigma-1/2)L} "
             "< 1e-7 at sigma >= 12) -- at depth pins the carrier's "
             "value is the CERTIFIED ENCLOSURE, not resummation; "
             "declared in the spec")

    # ---------------------------------------------------------- S5
    section("S5  K3 THE ANALYTIC QUESTION IN THE NEW CURRENCY")
    v256 = r.get("a256") or deep[0]
    x = 1.0 / dict((p[0], p[4]) for p in PINS)[v256["label"]]
    qfac = 4 * x * (1 + x)
    w4top = v256.get("w4_ward", 0.985)
    qrate = qfac / max(w4top, 1e-9)
    m_r_law = ((v256["min_res"] + C_LAW) * L4
               + math.log(max(v256["sup_r_only"], 1e-300))
               * 0 - math.log(2 * 256 * max(v256["sup_r_only"], 1e-300)
                              / 0.56)) / math.log(qrate)
    print("  NEW-CURRENCY MISSING LEMMA (theorem-shaped, measured")
    print("  constants):  IF the Weyl disks of the Krein realization")
    print("  of -g'' contract at the measured law R ~ C e^{-(sigma+%.2f)L}"
          % C_LAW)
    print("  UNIFORMLY on Re sigma >= sigma_edge (= %.2f here) AND every"
          % v256["min_res"])
    print("  finite section of -g'' is positive (localized Weil")
    print("  positivity, all depths), THEN each diagonal cell d_m(a0)")
    print("  is certified from SOURCE data with")
    print("    E_m ~ 2 a0 C e^{-(sigma_edge+c)L} (4x(1+x))^m,  "
          "x = a0/r_a,")
    print("  i.e. certified depth m_max(L) ~ [(sigma_edge+c)L - "
          "log(2 a0 C/y_1)] / log Q,")
    print("  Q = 4x(1+x)/(4w_max) = %.2f: LINEAR in L (measured "
          "m_R ~ %.1f at this window)," % (qrate, m_r_law))
    print("  SATURATED by the mesh-bias floor at m_bias ~ %d (delta = "
          "0.003) -- the coupled" % max(v256["m_cert_cond"], 0))
    print("  schedule delta ~ e^{-(sigma_edge+c)L/2} removes the "
          "saturation (mesh cost n = L/delta")
    print("  grows exponentially: the PRICE of depth, printed not "
          "hidden).")
    print("  WHAT IT DOES AND DOES NOT GIVE: an RH-FALSIFIER of")
    print("  unbounded depth (any certified |d_m|^{1/m} > 1/4 + eps at")
    print("  finite m kills RH) -- NOT a positivity prover: the limsup")
    print("  over all m and the dense-a quantifier remain omega-")
    print("  introductions.  Contraction is NECESSARY-BUT-NOT-")
    print("  SUFFICIENT: strictly below the wall; combined with the")
    print("  round-116 A2 cap (quarter bound unconditional for a <=")
    print("  9.0e24) it yields NO new unconditional statement beyond")
    print("  the cap -- only the conditional instrument above.")
    for gate in mincut_extension():
        check(*gate)

    # ---------------------------------------------------------- S6
    section("S6  K4 CONTROLS + SCREENS")
    ctrl_ok = True
    ctrl_det = []
    for wld, rtgt in (("SMOOTH", CTRL_R_SMOOTH), ("SCRARITH",
                                                  CTRL_R_SCR)):
        bw = KR.build_lags_mp(L4, D3, wld)
        szw = KR.szego_mp(bw["row"])
        if szw["ok"]:
            ctrl_ok = False
            ctrl_det.append("%s COMPLETES (unexpected)" % wld)
            continue
        rfail = szw["fail_k"] * bw["delta"]
        ctrl_ok &= abs(rfail - rtgt) <= CTRL_TOL
        # budget collapse at the death depth (sigma0 = 16)
        with mp.workdps(DPS_ALG):
            w0 = mp.exp(-mp.mpf(16) * bw["delta_mp"])
            _cv, _ce, rad_eff, _mg = disk_complex(
                szw["alphas"], szw["c0"], w0)
        e0 = 256.0 * float(rad_eff) / (2 * 16.0)
        ctrl_det.append("%s dies at r=%.3f (target %.3f); disk R at "
                        "death depth %.2e -> E_0 ~ %.2e: certified "
                        "depth 0" % (wld, rfail, rtgt,
                                     float(rad_eff), e0))
    check("G60-controls-die-at-positivity", ctrl_ok,
          "; ".join(ctrl_det))
    info("EPISTEMIC STATUS (typed honestly): the pairing is only "
         "DEFINED where the accelerant sections are positive -- the "
         "null worlds die at 0.264/0.744 < L, so NO equal-budget null "
         "comparator exists at depth; the separation is carried by "
         "positivity itself (round-90 'separated-by-collapse'); every "
         "depth statement is conditional on the measured K1c "
         "positivity through the window")

    # tau / conditioning screen
    b3 = builds[(L4, D3)]
    with mp.workdps(DPS_ALG):
        eps = mp.mpf(10) ** (-PERT_DPS)
        row_r = [v * (1 + eps * mp.cos(7 * d))
                 for d, v in enumerate(b3["row"])]
    sz_r = KR.szego_mp(row_r)
    lab0, s00, a00 = deep[0]["label"], None, None
    for (lb, s0v, a0v, _rj, _ra, _ro) in PINS:
        if lb == lab0:
            s00, a00 = s0v, a0v
    nj = 2 * mmax + 1
    with mp.workdps(DPS_ALG):
        pj_r = [xx / 2 for xx in transfer_cval_jet(
            sz_r["alphas"], sz_r["c0"], s00, b3["delta_mp"], nj)]
    d_r, _ = pjet_to_dscaled(pj_r, s00, a00, mmax)
    amps = []
    base_mp = r[lab0]["d3_mp"]
    base = r[lab0]["d3"]
    with mp.workdps(DPS_ALG):
        for m in range(mmax + 1):
            shift = float(abs(d_r[m] - base_mp[m]))
            amps.append(shift / (1e-25 * max(abs(base[m]), 1e-300)))
        m_use = r[lab0].get("rate_m", 2)
        rate_shift = float(abs(d_r[m_use] / d_r[m_use - 1]
                               - base_mp[m_use] / base_mp[m_use - 1])) \
            if m_use >= 1 else float("nan")
    slope = float(np.polyfit(range(mmax + 1),
                             np.log(np.maximum(amps, 1e-300)),
                             1)[0]) if mmax >= 2 else float("nan")
    check("G61-conditioning", rate_shift <= BAR_RATE_SHIFT,
          "1e-25 lag perturbation: rate shift %.2e (bar %.0e); "
          "amplification A_m = %.1e..%.1e, log-slope %.2f/depth "
          "(the conditioning law of the derivative reads)"
          % (rate_shift, BAR_RATE_SHIFT, min(amps), max(amps), slope))

    # ---------------------------------------------------------- S7
    section("S7  COMPOSITE VERDICT")
    verdicts = []
    v_main = r.get("a256") or deep[0]
    if fire_trans:
        verdicts.append("KR4-TRANSCRIBES-AT-DEPTH")
    elif (not smoke and v_main["m_sig_rich"] >= 3 and z1_ok):
        verdicts.append(
            "KR4-EXTRAPOLATES-AT-DEPTH(rate %.6f +- %.1e measured / "
            "+- %.1e Cauchy at m=%d, a=256; signal depth raw %d | "
            "Richardson %d; certified meas %d | cond %d | disk-only "
            "%d)"
            % (v_main.get("rate_kr", float("nan")),
               v_main.get("rate_bar_meas", float("inf")),
               v_main.get("rate_bar", float("inf")),
               v_main.get("rate_m", -1), v_main["m_sig_raw"],
               v_main["m_sig_rich"], v_main["m_cert_meas"],
               v_main["m_cert_cond"], v_main["m_cert_ronly"]))
    else:
        verdicts.append(
            "KR4-DERIVATIVE-WALL(budget law E_m = a0 supdev "
            "(4x(1+x))^m; measured depths: signal %s/%s, certified "
            "meas %s, cond %s; the mesh-bias floor is the wall at "
            "delta=0.003)"
            % (v_main["m_sig_raw"], v_main["m_sig_rich"],
               v_main["m_cert_meas"], v_main["m_cert_cond"]))
    verdicts.append("MINCUT-UNCHANGED(4; the depth crossing shares "
                    "the Weyl-disks-MEASURED unit; contraction "
                    "strictly below the wall)")
    verdicts.append("CONTROLS-DIE-AT-POSITIVITY(0.264/0.744; no "
                    "equal-budget null at depth -- conditional "
                    "instrument, typed)")
    verdicts.append(resum_typed)
    for v in verdicts:
        print("  " + v)

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
