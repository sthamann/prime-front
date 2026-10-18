#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wedge_scale_law_probe -- PRIME.PORT.WEDGE.SCALE.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS PROBE EXISTS.  exterior_pg_schur_probe (CLXVII, SPEC-SHA
084c9689) established on the 39-step surface: the positive CD-Gram
exterior quotient s_P = det(P)/det(P_G) is exact to 7.8e-16 and
s_P >= mu1(h) on 39/39, but the MATRIX Loewner lemma M >= P/2 fails
13/39 (Schur-seated).  exterior_pg_renormalized_probe (CLXVIII,
SPEC-SHA 2cce6c1d) killed the canonical renormalization as pure
relocation (raw slope +0.707).  NOT yet tested: the SCALAR
comparison s vs s_P, where s = n - b*B^{-1}b is the true tangent
Schur scalar of the step end-form.  This probe freezes the candidate
two-lemma scale-law shape and measures everything that decides
whether it is live:

  [Satz W1]  s_P >= c1 mu1(h)   for all h
             (a statement about the POSITIVE chain only --
              potentially classical Christoffel-function content);
  [Satz W2]  s   >= c2 s_P      for all h
             (the arithmetic comparison -- the wall in a new
              currency; the scalar weakening of the killed matrix
              L1, whose target constant is the frozen 1/2).

Together they give s >= c1 c2 mu1: the half-gap SCALE from a
classical lemma plus a bounded arithmetic comparison.  HONESTY
(frozen a priori): the deployed step currency has slack ~1e3 over
(1/2) mu1, so the chain proves the mu1 SCALE, not the registered
constant, unless c2 >= 1/2 uniformly; the count of steps with
s/s_P >= 1/2 is RECORDED against the frozen 1/2, never adjusted.

CURRENCY DECLARATION (frozen): the deployed step end-form is
M = Q* S(r2) Q / tau(r1) (v901), while P = Q* G_core Q carries NO
tau normalization.  The primary ladder r_W = s/s_P is therefore the
deployed-currency comparison (exactly the scalar seat of the killed
L1); the RAW ladder r_W_raw = tau(r1) s / s_P removes the
normalization and is the DECLARED RELOCATION DETECTOR (the CLXVIII
lesson: raw slope >= 0.70 vs tau = the wall relocated, not
compared).

THE CHRISTOFFEL IDENTIFICATION OF W1 (derived a priori, classical).
With G_core[i,j] = sqrt(v_i v_j) K_h(y_i, y_j) the positive CD-Gram
at the 8 core nodes and v0 the backward frame direction (Q e0 = v0),
frame invariance gives the EXACT identity
    s_P = 1 / (v0* G_core^{-1} v0)
        = [ min { ||p||^2_{mu+} : deg p < h,
                  sqrt(v_i) p(y_i) = (v0)_i, i = 1..8 } ]^{-1},
i.e. s_P is the reciprocal of a PRESCRIBED-NODE CHRISTOFFEL
FUNCTIONAL of the positive folded measure: the minimal mu+-energy of
a degree-(h-1) polynomial interpolating the frame direction at the
core nodes.  This is the same object family as the Radau finding
(wall_gram_radau_probe: the prescribed-node Gauss--Radau weight IS
numerically the Christoffel function, w*/lam_h med 0.9978,
tau-decorrelated +0.138) -- there at the single classical drift
node, here at the 8 core nodes with the frame direction as data.
The probe verifies the identity by TWO independent numerical routes
(inverse-Gram quadratic form; LAPACK min-norm least squares on the
underdetermined interpolation system) and then measures whether s_P
is LITERALLY a single-node Christoffel value (dominant-node
candidates chi_i = v_i K_h(y_i, y_i) and single-node pivots
1/(G^{-1})_{ii}) or only Christoffel-FORM.  The classical scale:
mu1(h) = 4 sin^2(pi/(2h+1)) ~ pi^2/h^2 is exactly the edge
Christoffel decay scale on [-1, 1]; the probe fits the s_P exponent
in h and reports the measured constant band c1 = s_P/mu1.

FROZEN PROTOCOL:

 W  REPRODUCTION (kill -> PIPELINE-BROKEN / WARD-BROKEN): parent
    census 42/41/39; v901 minB/gap ledger; four-route exterior
    identity <= EXT_WARD and P exact-PD (exact-rational LDL) on
    39/39; CLXVII reproduction s_P >= mu1 on 39/39; registered
    half-gap s >= mu1/2 on 39/39 (measurement); product identity
    (s/s_P)(s_P/mu1) == s/mu1 <= PROD_WARD (transcription ward).

 L  THE THREE LADDERS on the 39 surface steps (typed, never kill):
    L1 r_P = s_P/mu1: band, log-log trend vs h, tau-screen;
    L2 r_W = s/s_P: band (normalized AND raw), trend vs h,
       tau-screens BOTH currencies, count r_W >= 1/2 (recorded);
    L3 the upper side: is s_P <= C mu1 too -- band ratio
       max(r_P)/min(r_P) <= 10^O1_DECADES types TWO-SIDED-O1,
       else ONE-SIDED(ratio).

 B  W1's CLASSICAL CONTENT (kill -> WARD-BROKEN on B1/B2):
    B1 frame-invariance identity s_P == 1/(v0* G_core^{-1} v0)
       rel <= INV_WARD on every step;
    B2 the Christoffel-form route: min-norm lstsq solution g of
       H0 g = v0 (H0 = sqrt(v) P_chain, 8 x h) must satisfy
       s_P == 1/||g||^2 rel <= LSTSQ_WARD -- this EXHIBITS s_P as
       the prescribed-node Christoffel functional, numerically;
    B3 literalness (typed): dominant node i* = argmax (v0)_i^2;
       candidates chi_{i*} = v_{i*} K_h(y_{i*}, y_{i*}),
       piv_{i*} = 1/(G^{-1})_{i*,i*}, min_i piv_i, and the
       diagonal approximation 1/sum_i (v0)_i^2 (G^{-1})_{ii};
       CHRISTOFFEL-NODE-IDENTITY iff med |s_P/cand - 1| <= NODE_ID
       for some candidate; CHRISTOFFEL-NODE-TRACK iff corr(log s_P,
       log cand) >= TRACK_CORR with slope in TRACK_SLO; else
       CHRISTOFFEL-FORM-ONLY (the identity holds, no single node
       carries it);
    B4 the classical scale (measured): OLS exponent of log s_P vs
       log h (+R^2), same for the dominant chi ladder; mu1 h^2 vs
       pi^2 printed; the measured constant c1 = min r_P.

 A  W2's ANATOMY (typed): the 5 smallest-r_W seats (kz, h, |b|,
    tau, s/mu1); univariate R^2 table of log r_W vs log h, alpha,
    log |b|, log(|b|/tau), log tau, log(s/mu1) (the last is
    partially tautological -- log(s/mu1) = log r_W + log r_P
    exactly -- DECLARED); corr(log r_P, log r_W) (the declared
    expectation is strong anti-correlation, since their product
    s/mu1 varies less than the factors -- measured, first-class);
    agreement census between the scalar event {r_W < 1/2} and the
    exact matrix event {M - P/2 not PD} (the CLXVII 13/39 seat).

 D  DEEP HOLDOUT (typed; kill K1 iff census < MIN_DEEP, K2 on
    fidelity): 4e6 von Mangoldt table via the deployed generator;
    W-wards: table overlap byte-exact on [0, ATOM_MAX], prefix
    arrays bitwise (deep_blind_holdout W1/W2 verbatim; kappa and
    registry reproduction carried by the upstream CLXIII/CLXIV
    deep probes, DECLARED not re-run); the new-rung census (28
    expected, h 1219..2854), steps = consecutive usable pairs (r1
    all-PSD, lamS > 0); per deep step s, s_P, mu1, r_W (both
    currencies) at FLOAT LEVEL (declared).  Typed DEEP-CONTINUES
    iff s_P >= mu1 AND s >= mu1/2 on every deep step AND deep r_W
    inside [min_surf/OOB_FAC, max_surf x OOB_FAC]; else
    DEEP-BREAKS(named seat).  Combined (surface+deep) h-trends of
    log r_P and log r_W reported.

 C  CONTROLS (kill -> WARD-BROKEN if silent): C1 smooth world must
    refuse the certificate ladder (parent rule: refusals > 0 and
    usable core-PD < 39); C2 Epstein x^2+5y^2 and C3
    position-scramble seed 1 at kz 9 must fire (parent
    control_fires verbatim).  C4 THE DISCRIMINATION TABLE (typed,
    the wall-blindness measurement): on every mechanically
    buildable smooth-world step, compute s_raw (RAW currency --
    the smooth tau is negative, so the raw Schur pivot of
    Q* S(r2) Q is the sign-meaningful object) and s_P; typed
    W2-CARRIES-WALL iff the wall is broken on every smooth step
    (negA > 0 at r1 or r2) AND s_P stays > 0 on every computable
    smooth step (the positive chain's scalar is world-blind
    classical algebra, the SIGN of s carries the wall); else
    W2-BLIND(counts).  The smooth s_P/mu1 band is printed next to
    the truth band.

ANTI-CIRCULARITY (frozen): s_P consumes ONLY r2's positive-chain CD
data (chain, core nodes, core weights) and the backward r1
Householder frame -- no sigma_h, no forward pivot sign, no target
eigendata of r2 in any construction; mu1 is parity geometry; the
frozen 1/2 is registered upstream (NO-ADJUST verbatim).  The target
s enters only as the measured comparandum.  Exact-rational LDL is
the declared v897 decision class (W-block only).

ANTHROPIC NO-GO DECLARATION: inputs are the full degree-(h-1)
positive CD evaluation matrix, an 8-row exterior quotient, and the
tangent Schur scalar -- strictly beyond two scalar moments plus
bandwidth-1 pair correlation; no contradiction with the two-moment
no-go.

VERDICT (frozen enum, decided by the rules below and nothing else):
  WEDGE-SCALE-DEAD iff any surface or deep step has s_P < mu1, or
    any truth step has s <= 0, or the deep r_W band breaks
    (outside [min_surf/OOB_FAC, max_surf x OOB_FAC]);
  else WEDGE-SCALE-RELOC iff the normalized r_W tau-screen slope
    >= SLOPE_RELOC (AMENDMENT A1, disclosed below: the originally
    spec'd RAW trigger is removed as mathematically tautological
    -- r_W_raw = tau r_W identically, so slope_raw == slope_norm
    + 1 and the raw trigger would fire whenever the normalized
    screen passes with slope > -0.30; the raw band and screen stay
    printed as measurements);
  else WEDGE-SCALE-LIVE iff the normalized r_W tau-screen is PASS
    (|slope| <= SLOPE_PASS), the combined h-trend |slope| of
    log r_W <= HTREND_BAR, both ladders are O(1) (band ratios
    <= 10^O1_DECADES), and B1/B2 hold (they are wards anyway);
  else WEDGE-SCALE-AMBIG(named reasons).

FROZEN BARS: EXT_WARD = 1e-8; PROD_WARD = 1e-12; INV_WARD = 1e-9;
LSTSQ_WARD = 1e-6; NODE_ID = 1e-6; TRACK_CORR = 0.90; TRACK_SLO =
(0.7, 1.3); SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; HTREND_BAR =
0.50; O1_DECADES = 3.0; OOB_FAC = 3.0; MIN_DEEP = 10; HALF = 1/2
EXACT; N_SEATS = 5; parent bars (MINB_REF 0.679, GAP 0.052/0.888,
rtol as parent) inherited verbatim; parent SPEC-SHA warded ==
084c9689..; renormalized SPEC-SHA prefix warded == 2cce6c1d.
Runtime cap declared: 15 min.  Smoke mode WEDGE_SMOKE=1 restricts
the deep block to the 4 shallowest new rungs (surface + controls
always full); any smoke run is disclosed here before the freeze.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke run
(WEDGE_SMOKE=1, 22/22 on the first passage, 6.2 s; deep block on
the 4 shallowest new rungs -> 3 deep steps).  It exposed ONE SPEC
DEFECT, not a wall fact: the originally spec'd RAW relocation
trigger is a tautology -- r_W_raw = tau r_W identically, hence
slope_raw == slope_norm + 1 EXACTLY (measured +0.707 == -0.293 +
1.000), so the raw trigger fires RELOC precisely when the
normalized screen is NOT strongly tau-anti-correlated, i.e. it can
never distinguish relocation from decorrelation.  AMENDMENT A1
(disclosed): the verdict RELOC rule now reads the NORMALIZED r_W
screen only (bar SLOPE_RELOC unchanged); the raw ladder and its
screen remain printed as measurements.  No other bar, band, count,
rule or enum was moved.  Measured smoke context the frozen run
must confirm: W green (minB 0.6790, gap 0.0520/0.8875, exterior
identity 7.77e-16, P exact-PD 39/39, s_P >= mu1 39/39, s >= mu1/2
39/39, product ward 2e-16); L1 r_P = 2264.6..78195 (med 19125),
h-trend +1.997 with R^2 1.000 -- r_P is a PURE h^2 law, i.e. s_P
itself is h-FLAT O(1) (p(s_P) = +0.000, R^2 0.123) and tends to 1
at depth; L2 r_W = 0.0520..19.79 (med 0.887), h-flat (slope
+0.009, R^2 0.000), normalized screen PASS(-0.293, R^2 0.154),
raw screen RELOCATION(+0.707) = the tautology above; r_W >= 1/2
on 26/39; L3 TWO-SIDED-O1(ratio 34.5); B1/B2 identities 5.6e-16 /
4.8e-15; B3 CHRISTOFFEL-FORM-ONLY (best single-node candidate
chi_i* med dev 0.0205, corr +0.712 -- close but neither identity
nor track); B4 mu1 h^2 = 9.803..9.858 vs pi^2 = 9.8696; frame
concentration max(v0^2) med 0.665; A: the smallest-r_W seats are
the known |b|-outliers (kz 44/436 r_W 0.0520, |b| 1.61; kz 59/363
|b| 6.09), organizer log |b| R^2 0.731 beats everything; the
declared anti-correlation expectation FAILED honestly
(corr(log r_P, log r_W) = +0.003 -- r_W is a genuinely new
number); scalar/matrix event agreement 39/39 (13 fails each); D
wards green (overlap 0.0, prefixes bitwise, census 28), smoke
deep steps 3/3 pass with r_W 0.405..1.859 inside [0.0173, 59.4];
C fires 3/3, discrimination: 36 smooth steps built, wall broken
36/36, s_P > 0 on 36/36, smooth r_P band 745..1.24e5 straddles
the truth band -> W2-CARRIES-WALL.  Under the amended (A1) rule
the smoke verdict would be WEDGE-SCALE-LIVE; under the defective
v1 rule it was RELOC by tautology -- disclosed in full.

NO RH claim.  Even a full LIVE verdict is a finite-surface + finite
-holdout measurement: all-h uniformity of W1 (a classical
Christoffel statement), all-h uniformity of W2, and interval
enclosure of the pipeline remain open.  A DEAD or RELOC verdict
kills this scale-law shape; it says nothing about RH.  No marker
moves.  Stdout only.
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import bfloor_pg_dominance_probe as base  # noqa: E402  (READ-ONLY)
import exterior_pg_schur_probe as parent  # noqa: E402  (READ-ONLY)
import exterior_pg_renormalized_probe as renorm  # noqa: E402 (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
RENORM_SHA8 = "2cce6c1d"
EXT_WARD = 1.0e-8
PROD_WARD = 1.0e-12
INV_WARD = 1.0e-9
LSTSQ_WARD = 1.0e-6
NODE_ID = 1.0e-6
TRACK_CORR = 0.90
TRACK_SLO = (0.7, 1.3)
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
HTREND_BAR = 0.50
O1_DECADES = 3.0
OOB_FAC = 3.0
MIN_DEEP = 10
HALF = 0.5
N_SEATS = 5
SMOKE = os.environ.get("WEDGE_SMOKE", "") == "1"
BANNED_IDS = parent.BANNED_IDS

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def ols(x, y):
    """slope, R^2 (parent convention)."""
    return parent.ols_line(x, y)


def screen(values, taus):
    return parent.screen(values, taus)


def band(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def wedge_step(r1, r2):
    """One step's (s, s_P, mu1, |b|, tau) -- the parent E-block
    construction, shared by the deep ladder.  Returns None if the
    co-blocks are not usable (counted by the caller)."""
    _w, VS = np.linalg.eigh(r1["S"])
    v0 = VS[:, 0]
    Q = base.householder_frame(v0)
    Mn = Q.T @ (r2["S"] / r1["tau"]) @ Q
    Mn = 0.5 * (Mn + Mn.T)
    b = Mn[1:, 0]
    B = Mn[1:, 1:]
    if float(np.linalg.eigvalsh(B)[0]) <= 0.0:
        return None
    s = float(Mn[0, 0]) - float(b @ np.linalg.solve(B, b))
    al, be, m0 = r2["chain"]
    Pc = base.eval_chain(al, be, m0, r2["y_core"], r2["h"])
    H0 = np.sqrt(r2["v_core"])[:, None] * Pc
    Gc = H0 @ H0.T
    Gc = 0.5 * (Gc + Gc.T)
    P = Q.T @ Gc @ Q
    P = 0.5 * (P + P.T)
    PG = P[1:, 1:]
    if float(np.linalg.eigvalsh(PG)[0]) <= 0.0:
        return None
    sP = float(P[0, 0]) - float(P[1:, 0] @ np.linalg.solve(PG, P[1:, 0]))
    return dict(kz=r2["kz"], h=r2["h"], s=s, sP=sP,
                mu1=parent.mu1_of(r2["h"]), tau=r1["tau"],
                bnorm=float(np.linalg.norm(b)), v0=v0, Gc=Gc, H0=H0,
                alpha=r2.get("alpha", float("nan")))


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
    else:
        verdict = ("WEDGESCALE-MEASURED / %s / %s / %s / %s / %s"
                   % (labels.get("l", "-"), labels.get("b", "-"),
                      labels.get("d", "-"), labels.get("c", "-"),
                      labels.get("head", "-")))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: W1 is exhibited as a prescribed-node Christoffel
  functional of the positive folded measure -- classical in FORM,
  but its uniform-in-h lower bound is unproven; W2 is a finite
  measured band, not a theorem.  All deep objects are float-level.
  A LIVE verdict names two open lemmas; DEAD/RELOC kills this
  shape.  NO RH claim; no marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.WEDGE.SCALE.01 -- the wedge/Christoffel "
            "scale law: s >= c2 s_P >= c1 c2 mu1 (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    parent_sha = hashlib.sha256(
        parent.__doc__.encode("utf-8")).hexdigest()
    renorm_sha = hashlib.sha256(
        renorm.__doc__.encode("utf-8")).hexdigest()
    print("    parent SPEC SHA-256   = %s" % parent_sha)
    print("    renorm SPEC SHA-256   = %s" % renorm_sha)
    print("    NO RH claim.  HALF = 1/2 frozen upstream; NO-ADJUST.")
    if SMOKE:
        print("    *** SMOKE MODE: deep block on 4 shallowest new "
              "rungs only ***")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced", parent_sha == PARENT_SHA,
          kill="K2")
    check("S0c renorm SPEC prefix reproduced",
          renorm_sha[:8] == RENORM_SHA8, renorm_sha[:8], kill="K2")

    # ------------------------------------------------------------ W
    section("W -- parent ladder, exterior identity, CLXVII "
            "reproduction")
    zones, truth, full, rows = parent.build_truth_rows()
    check("W1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41 and len(rows) == 39,
          "%d/%d/%d" % (len(zones), len(full), len(rows)), kill="K1")
    if KILLS:
        return finish({})
    minb = min(float(np.linalg.eigvalsh(w["B"])[0]) for w in rows)
    gaps = np.array([w["gap"] for w in rows])
    check("W2 v901 reproduction",
          abs(minb / parent.MINB_REF - 1.0) <= parent.MINB_RTOL
          and abs(float(np.min(gaps)) / parent.GAPMIN_REF - 1.0)
          <= parent.GAP_RTOL
          and abs(float(np.median(gaps)) / parent.GAPMED_REF - 1.0)
          <= parent.GAP_RTOL,
          "minB %.4f gap %.4f/%.4f"
          % (minb, float(np.min(gaps)), float(np.median(gaps))),
          kill="K2")
    max_ext = max(
        max(abs(w["sP"] - w["sP_projection"]),
            abs(w["sP"] - w["sP_inverse"]),
            abs(w["sP"] - w["sP_det"])) / max(abs(w["sP"]), 1e-300)
        for w in rows)
    p_pd = sum(parent.exact_pd(w["P"]) for w in rows)
    check("W3 exterior identity + P exact-PD",
          max_ext <= EXT_WARD and p_pd == len(rows),
          "max dev %.2e; exact-PD %d/%d" % (max_ext, p_pd, len(rows)),
          kill="K2")
    l2 = sum(w["sP"] >= w["mu1"] for w in rows)
    check("W4 CLXVII reproduction s_P >= mu1",
          l2 == len(rows), "%d/%d" % (l2, len(rows)), kill="K2")
    hg = sum(w["gap"] >= HALF * w["mu1"] for w in rows)
    check("W5 registered half-gap s >= mu1/2 (measurement)",
          hg == len(rows), "%d/%d" % (hg, len(rows)), kill="K2")
    prod_dev = max(
        abs((w["gap"] / w["sP"]) * (w["sP"] / w["mu1"])
            - w["gap"] / w["mu1"]) / max(abs(w["gap"] / w["mu1"]),
                                         1e-300) for w in rows)
    check("W6 product identity r_W r_P == s/mu1",
          prod_dev <= PROD_WARD, "max rel dev %.2e" % prod_dev,
          kill="K2")

    hs = np.array([float(w["r2"]["h"]) for w in rows])
    taus = np.array([w["tau"] for w in rows])
    s_arr = np.array([w["gap"] for w in rows])
    sP_arr = np.array([w["sP"] for w in rows])
    mu_arr = np.array([w["mu1"] for w in rows])
    bn_arr = np.array([float(np.linalg.norm(w["b"])) for w in rows])
    rP = sP_arr / mu_arr
    rW = s_arr / sP_arr
    rWraw = s_arr * taus / sP_arr
    shat = s_arr / mu_arr

    # ------------------------------------------------------------ L
    section("L -- THE THREE LADDERS (39 surface steps)")
    sl_p, r2_p = ols(np.log(hs), np.log(rP))
    scr_p, _ = screen(rP, taus)
    print("    L1  r_P = s_P/mu1: min/med/max %.6g / %.6g / %.6g"
          % band(rP))
    print("        h-trend slope %+.3f (R^2 %.3f); tau-screen %s"
          % (sl_p, r2_p, scr_p))
    sl_w, r2_w = ols(np.log(hs), np.log(rW))
    scr_wn, slope_wn = screen(rW, taus)
    scr_wr, slope_wr = screen(rWraw, taus)
    n_half = int(np.sum(rW >= HALF))
    print("    L2  r_W = s/s_P (NORMALIZED): min/med/max "
          "%.6g / %.6g / %.6g" % band(rW))
    print("        r_W_raw = tau s/s_P:      min/med/max "
          "%.6g / %.6g / %.6g" % band(rWraw))
    print("        h-trend slope %+.3f (R^2 %.3f)" % (sl_w, r2_w))
    print("        tau-screen normalized %s" % scr_wn)
    print("        tau-screen RAW (measurement; A1: slope_raw == "
          "slope_norm + 1 identically) %s" % scr_wr)
    print("        r_W >= 1/2 on %d/%d (recorded vs the frozen "
          "1/2, NO-ADJUST)" % (n_half, len(rows)))
    ratio_p = float(np.max(rP) / np.min(rP))
    ratio_w = float(np.max(rW) / np.min(rW))
    two_sided = ratio_p <= 10.0 ** O1_DECADES
    l3 = ("TWO-SIDED-O1(ratio=%.1f)" % ratio_p if two_sided
          else "ONE-SIDED(ratio=%.1f)" % ratio_p)
    print("    L3  upper side: s_P <= %.4g mu1; band ratio %.1f "
          "(bar 10^%.0f) -> %s"
          % (float(np.max(rP)), ratio_p, O1_DECADES, l3))
    check("L typed ladders recorded", True,
          "rP[%0.3g..%0.3g] rW[%0.3g..%0.3g]"
          % (float(np.min(rP)), float(np.max(rP)),
             float(np.min(rW)), float(np.max(rW))))

    # ------------------------------------------------------------ B
    section("B -- W1's classical content: the prescribed-node "
            "Christoffel functional")
    inv_dev = 0.0
    ls_dev = 0.0
    cands = {"chi_i*": [], "piv_i*": [], "min_piv": [],
             "diag_approx": []}
    for w in rows:
        v0 = w["Q"][:, 0]
        Gc = w["Q"] @ w["P"] @ w["Q"].T
        Gc = 0.5 * (Gc + Gc.T)
        Ginv = np.linalg.inv(Gc)
        s_inv = 1.0 / float(v0 @ Ginv @ v0)
        inv_dev = max(inv_dev, abs(s_inv - w["sP"]) / abs(w["sP"]))
        g = np.linalg.lstsq(w["H"], v0, rcond=None)[0]
        s_ls = 1.0 / float(g @ g)
        ls_dev = max(ls_dev, abs(s_ls - w["sP"]) / abs(w["sP"]))
        istar = int(np.argmax(v0 ** 2))
        cands["chi_i*"].append(float(Gc[istar, istar]))
        cands["piv_i*"].append(1.0 / float(Ginv[istar, istar]))
        cands["min_piv"].append(
            1.0 / float(np.max(np.diag(Ginv))))
        cands["diag_approx"].append(
            1.0 / float(v0 ** 2 @ np.diag(Ginv)))
        w["istar"] = istar
        w["v0max2"] = float(np.max(v0 ** 2))
    check("B1 frame-invariance identity s_P == 1/(v0* G^{-1} v0)",
          inv_dev <= INV_WARD, "max rel dev %.2e" % inv_dev,
          kill="K2")
    check("B2 min-norm interpolation route (Christoffel form)",
          ls_dev <= LSTSQ_WARD, "max rel dev %.2e" % ls_dev,
          kill="K2")
    b3 = "CHRISTOFFEL-FORM-ONLY"
    for name, vals in cands.items():
        vals = np.array(vals)
        med_dev = float(np.median(np.abs(sP_arr / vals - 1.0)))
        co = float(np.corrcoef(np.log(sP_arr), np.log(vals))[0, 1])
        sl_c, _ = ols(np.log(vals), np.log(sP_arr))
        print("    B3 candidate %-12s: med|s_P/cand - 1| %.3g; "
              "corr(log) %+.3f; slope %+.3f; ratio band "
              "%.3g..%.3g"
              % (name, med_dev, co, sl_c,
                 float(np.min(sP_arr / vals)),
                 float(np.max(sP_arr / vals))))
        if med_dev <= NODE_ID:
            b3 = "CHRISTOFFEL-NODE-IDENTITY(%s)" % name
        elif (b3 == "CHRISTOFFEL-FORM-ONLY" and co >= TRACK_CORR
              and TRACK_SLO[0] <= sl_c <= TRACK_SLO[1]):
            b3 = "CHRISTOFFEL-NODE-TRACK(%s, corr=%+.3f)" % (name, co)
    check("B3 typed: %s" % b3, True)
    sl_sp, r2_sp = ols(np.log(hs), np.log(sP_arr))
    sl_chi, r2_chi = ols(np.log(hs),
                         np.log(np.array(cands["chi_i*"])))
    mu_h2 = mu_arr * hs ** 2
    v0m = np.array([w["v0max2"] for w in rows])
    print("    B4 exponents: p(s_P) = %+.3f (R^2 %.3f); "
          "p(chi_i*) = %+.3f (R^2 %.3f); p(mu1) = -2 exactly "
          "(mu1 h^2 = %.4f..%.4f vs pi^2 = %.4f)"
          % (sl_sp, r2_sp, sl_chi, r2_chi,
             float(np.min(mu_h2)), float(np.max(mu_h2)),
             math.pi ** 2))
    print("    B4 measured W1 constant: c1 = min s_P/mu1 = %.6g "
          "(med %.6g); frame concentration max(v0^2) "
          "min/med/max %.3f/%.3f/%.3f"
          % (float(np.min(rP)), float(np.median(rP)),
             float(np.min(v0m)), float(np.median(v0m)),
             float(np.max(v0m))))
    check("B4 classical scale recorded", True)

    # ------------------------------------------------------------ A
    section("A -- W2's anatomy")
    order = np.argsort(rW)
    print("    the %d smallest r_W seats:" % N_SEATS)
    print("    kz    h     r_W        |b|       tau        s/mu1")
    for i in order[:N_SEATS]:
        w = rows[i]
        print("    %-5d %-5d %.6f   %.4g   %.4g   %.4g"
              % (w["r2"]["kz"], w["r2"]["h"], rW[i], bn_arr[i],
                 taus[i], shat[i]))
    alphas = np.array([w["r2"]["alpha"] for w in rows])
    print("\n    univariate R^2 of log r_W vs:")
    for name, xv in (("log h", np.log(hs)),
                     ("alpha", alphas),
                     ("log |b|", np.log(bn_arr)),
                     ("log(|b|/tau)", np.log(bn_arr / taus)),
                     ("log tau", np.log(taus)),
                     ("log(s/mu1) [tautology declared]",
                      np.log(shat))):
        sl_a, r2_a = ols(xv, np.log(rW))
        print("      %-34s slope %+.3f  R^2 %.3f"
              % (name, sl_a, r2_a))
    co_pw = float(np.corrcoef(np.log(rP), np.log(rW))[0, 1])
    print("    corr(log r_P, log r_W) = %+.3f (declared "
          "expectation: strong anti-correlation)" % co_pw)
    l1_exact = [parent.exact_pd(w["Lhalf"]) for w in rows]
    scalar_ev = [r < HALF for r in rW]
    agree = sum(1 for a, b_ in zip(l1_exact, scalar_ev)
                if a == (not b_))
    print("    agreement {r_W < 1/2} == {M - P/2 not exact-PD}: "
          "%d/%d (matrix fails %d, scalar fails %d)"
          % (agree, len(rows),
             sum(1 for a in l1_exact if not a),
             sum(scalar_ev)))
    check("A anatomy recorded", True)

    # ------------------------------------------------------------ D
    section("D -- deep holdout (4e6 table, float level declared)")
    lam_ext = deep.build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    nP = len(core.U_ALL)
    ok_pref = (np.array_equal(deep.EXT["NN"][:nP], core._NN)
               and np.array_equal(deep.EXT["U"][:nP], core.U_ALL)
               and np.array_equal(deep.EXT["MU"][:nP], core.MU_ALL)
               and np.array_equal(deep.EXT["G"][:nP - 1],
                                  core.G_ALL[:nP - 1]))
    check("D1 deep-table fidelity: overlap dev %.1e == 0.0, "
          "prefixes bitwise" % dev, dev == 0.0 and ok_pref,
          kill="K2")
    new_kz = []
    for kz in range(2, min(deep.KZ_SCAN_MAX,
                           len(deep.EXT["NN"]) - 2)):
        alpha = float(deep.EXT["U"][kz])
        X = math.exp(2.0 * alpha)
        if X > deep.TAB_EXT:
            break
        if X <= core.ATOM_MAX:
            continue
        h = deep.ext_frame(kz)[2]
        if not (deep.H_HOLD[0] <= h <= deep.H_HOLD[1]):
            continue
        new_kz.append(kz)
    order_kz = sorted(new_kz, key=lambda k: (deep.ext_frame(k)[2], k))
    check("D2 new-rung census %d (>= %d), kappa/registry fidelity "
          "carried by upstream deep probes (declared)"
          % (len(order_kz), MIN_DEEP), len(order_kz) >= MIN_DEEP,
          kill="K1")
    if KILLS:
        return finish({})
    if SMOKE:
        order_kz = order_kz[:4]
    grams = []
    for kz in order_kz:
        g = deep.ext_gram(kz)
        tag = ("chain-short" if g is None else
               "core-missing" if not g["core_ok"] else "ok")
        print("    deep gram kz %3d: %s  [%.1f s]"
              % (kz, tag, time.time() - T0), flush=True)
        if isinstance(g, dict) and g.get("core_ok"):
            grams.append(g)
    grams.sort(key=lambda g: (g["h"], g["kz"]))
    dsteps = []
    for g1, g2 in zip(grams, grams[1:]):
        if g1["negA"] > 0 or g1["negS"] > 0 or g1["lamS"] <= 0.0:
            continue
        st = wedge_step(g1, g2)
        if st is not None:
            dsteps.append(st)
    print("    %d deep steps (h %s..%s)"
          % (len(dsteps),
             dsteps[0]["h"] if dsteps else "-",
             dsteps[-1]["h"] if dsteps else "-"))
    print("    kz(r2) h      s          s_P        r_W       "
          "r_P        s>=mu1/2  sP>=mu1")
    d_ok_l2 = d_ok_hg = 0
    d_rW, d_rP, d_h, d_tau, d_rWraw = [], [], [], [], []
    for st in dsteps:
        okl2 = st["sP"] >= st["mu1"]
        okhg = st["s"] >= HALF * st["mu1"]
        d_ok_l2 += okl2
        d_ok_hg += okhg
        d_rW.append(st["s"] / st["sP"])
        d_rWraw.append(st["s"] * st["tau"] / st["sP"])
        d_rP.append(st["sP"] / st["mu1"])
        d_h.append(float(st["h"]))
        d_tau.append(st["tau"])
        print("    %-6d %-6d %.4e %.4e %.6f  %.4e  %-9s %s"
              % (st["kz"], st["h"], st["s"], st["sP"],
                 st["s"] / st["sP"], st["sP"] / st["mu1"],
                 "PASS" if okhg else "FAIL",
                 "PASS" if okl2 else "FAIL"), flush=True)
    d_rW = np.array(d_rW)
    d_rP = np.array(d_rP)
    lo_band = float(np.min(rW)) / OOB_FAC
    hi_band = float(np.max(rW)) * OOB_FAC
    in_band = (int(np.sum((d_rW >= lo_band) & (d_rW <= hi_band)))
               if len(d_rW) else 0)
    deep_ok = (len(dsteps) > 0 and d_ok_l2 == len(dsteps)
               and d_ok_hg == len(dsteps) and in_band == len(dsteps))
    if deep_ok:
        dlab = ("DEEP-CONTINUES(%d/%d, r_W %.3g..%.3g in "
                "[%.3g, %.3g])"
                % (len(dsteps), len(dsteps), float(np.min(d_rW)),
                   float(np.max(d_rW)), lo_band, hi_band))
    else:
        dlab = ("DEEP-BREAKS(l2 %d/%d, halfgap %d/%d, band %d/%d)"
                % (d_ok_l2, len(dsteps), d_ok_hg, len(dsteps),
                   in_band, len(dsteps)))
    if len(dsteps) >= 3:
        h_all = np.concatenate([hs, np.array(d_h)])
        rP_all = np.concatenate([rP, d_rP])
        rW_all = np.concatenate([rW, d_rW])
        sl_pc, r2_pc = ols(np.log(h_all), np.log(rP_all))
        sl_wc, r2_wc = ols(np.log(h_all), np.log(rW_all))
        scr_dw, _ = screen(np.concatenate([rWraw,
                                           np.array(d_rWraw)]),
                           np.concatenate([taus,
                                           np.array(d_tau)]))
        print("    combined h-trends: log r_P slope %+.3f (R^2 "
              "%.3f); log r_W slope %+.3f (R^2 %.3f); combined "
              "raw screen %s"
              % (sl_pc, r2_pc, sl_wc, r2_wc, scr_dw))
    else:
        sl_wc = sl_w
    check("D typed: %s" % dlab, True)

    # ------------------------------------------------------------ C
    section("C -- controls + the discrimination table")
    sm = {}
    refused = usable_sm = 0
    for kz in zones:
        r = base.gram_anatomy(kz, world_fn=base.world_smooth,
                              keep_chain=True)
        if r is None or not r.get("core_ok") or r.get("negA", 1) > 0 \
                or r.get("negS", 1) > 0:
            refused += 1
        else:
            usable_sm += 1
        if isinstance(r, dict):
            sm[kz] = r
    check("C1 smooth world refuses the certificate ladder",
          refused > 0 and usable_sm < 39,
          "refused=%d usable-core-PD=%d" % (refused, usable_sm),
          kill="K2")
    for kind in ("epstein", "scramble"):
        fired, detail = parent.control_fires(kind)
        check("C %s world fires" % kind, fired, detail, kill="K2")
    smooth = sorted((r for r in sm.values()
                     if r.get("core_ok") and "S" in r),
                    key=lambda r: (r["h"], r["kz"]))
    n_pos_sp = n_broken = n_built = n_dead = 0
    sm_rp = []
    for r1, r2 in zip(smooth, smooth[1:]):
        _w, VS = np.linalg.eigh(r1["S"])
        Q = base.householder_frame(VS[:, 0])
        Mr = Q.T @ r2["S"] @ Q
        Mr = 0.5 * (Mr + Mr.T)
        try:
            s_raw = (float(Mr[0, 0])
                     - float(Mr[1:, 0]
                             @ np.linalg.solve(Mr[1:, 1:],
                                               Mr[1:, 0])))
            al, be, m0 = r2["chain"]
            Pc = base.eval_chain(al, be, m0, r2["y_core"], r2["h"])
            H0 = np.sqrt(r2["v_core"])[:, None] * Pc
            Gc = H0 @ H0.T
            P = Q.T @ (0.5 * (Gc + Gc.T)) @ Q
            sP_sm = (float(P[0, 0])
                     - float(P[1:, 0]
                             @ np.linalg.solve(P[1:, 1:],
                                               P[1:, 0])))
        except np.linalg.LinAlgError:
            n_dead += 1
            continue
        n_built += 1
        if sP_sm > 0.0:
            n_pos_sp += 1
            sm_rp.append(sP_sm / parent.mu1_of(r2["h"]))
        if r1["negA"] > 0 or r2["negA"] > 0 or s_raw <= 0.0:
            n_broken += 1
    if sm_rp:
        print("    smooth steps built %d (dead %d); wall broken "
              "on %d; s_P > 0 on %d; smooth r_P band "
              "%.3g / %.3g / %.3g (truth %.3g / %.3g / %.3g)"
              % (n_built, n_dead, n_broken, n_pos_sp,
                 *band(np.array(sm_rp)), *band(rP)))
    carries = (n_built > 0 and n_broken == n_built
               and n_pos_sp == n_built)
    c4 = ("W2-CARRIES-WALL(%d/%d)" % (n_built, n_built) if carries
          else "W2-BLIND(built=%d, broken=%d, sP>0=%d)"
          % (n_built, n_broken, n_pos_sp))
    check("C4 typed: %s (s_P is world-blind classical algebra; "
          "the SIGN of s carries the wall)" % c4, True)

    # ------------------------------------------------------- verdict
    dead = []
    if l2 != len(rows) or d_ok_l2 != len(dsteps):
        dead.append("sP<mu1")
    if float(np.min(s_arr)) <= 0.0:
        dead.append("s<=0")
    if not deep_ok:
        dead.append("deep-band")
    # AMENDMENT A1 (disclosed in the spec): normalized screen only;
    # the raw trigger is tautological (slope_raw == slope_norm + 1).
    reloc = np.isfinite(slope_wn) and slope_wn >= SLOPE_RELOC
    o1_both = (ratio_p <= 10.0 ** O1_DECADES
               and ratio_w <= 10.0 ** O1_DECADES)
    live = (not dead and not reloc
            and np.isfinite(slope_wn) and abs(slope_wn) <= SLOPE_PASS
            and abs(sl_wc) <= HTREND_BAR and o1_both
            and inv_dev <= INV_WARD and ls_dev <= LSTSQ_WARD)
    if dead:
        head = "WEDGE-SCALE-DEAD(%s)" % ",".join(dead)
    elif reloc:
        head = "WEDGE-SCALE-RELOC(norm=%+.3f)" % slope_wn
    elif live:
        head = "WEDGE-SCALE-LIVE"
    else:
        reasons = []
        if not (np.isfinite(slope_wn)
                and abs(slope_wn) <= SLOPE_PASS):
            reasons.append("norm-screen=%+.3f" % slope_wn)
        if abs(sl_wc) > HTREND_BAR:
            reasons.append("h-trend=%+.3f" % sl_wc)
        if not o1_both:
            reasons.append("band-ratio")
        head = "WEDGE-SCALE-AMBIG(%s)" % ",".join(reasons)
    labels = dict(
        l=("L1[%.3g..%.3g,%s] L2[%.3g..%.3g,norm%+.2f,raw%+.2f,"
           "half %d/39] L3[%s]"
           % (float(np.min(rP)), float(np.max(rP)), l3.split("(")[0],
              float(np.min(rW)), float(np.max(rW)), slope_wn,
              slope_wr, n_half, l3.split("(")[0])),
        b="%s" % b3, d=dlab, c=c4, head=head)
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
