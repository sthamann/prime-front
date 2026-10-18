#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""rho_margin_derivation_probe -- PRIME.PORT.PSI4.RHOALLH.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS PROBE EXISTS -- THE ALL-H ATTEMPT, RHO HALF.
psi4_block_model_probe (CLXXVI, SPEC-SHA 1fbbc0c8..) reduced the
skeleton half of the Psi_4 tower to ONE one-parameter law: the
trajectory margin 1 - rho_h with rho_h = mean(|r_12|, |r_13|,
|r_23|) of R = corr(Mt) on the alternating x1-x2-x3 triple
(measured rho_h max 0.957, margin >= 0.043, flat over 20x in h;
the skeleton certification region is EXACTLY {rho < 1, u > 0}).
THE QUESTION OF THIS PROBE (frozen): does 1 - rho_h admit a lower
bound DERIVED from global/structural inputs -- and does the
derivation connect to the SAME Christoffel machinery as W1?  The
answer is attempted as an explicit inequality chain, every step
with an explicit constant, verified per rung on 39 core + 27 deep
steps with the honest slack ladder.  HONESTLY: even a full
derivation covers only the skeleton condition (i); the background
admittance condition (ii) and W2 / background cancellation remain
RH-hard and untouched -- stated in every verdict path.

(a) THE OBJECTS.  Per consecutive full-core step (r1, r2): Mt =
Q^T (S_2/tau_1) Q (P2/P3 frame, head x0, co-block x1..x7), B =
Mt[1:,1:], the CLXXVI triple = coordinates (1,2),(1,3),(2,3) of
Mt.  Mt is PSD (S_2 PSD warded), so Mt = Z Z^T (Cholesky) and each
correlation is an ANGLE between named chain vectors z_i (the
rotated rows of the equilibrated core):
    r_ij = cos angle(z_i, z_j),
    1 - r_ij^2 = det(Mt_{ij}) / (Mt_ii Mt_jj)
               = ||zhat_i wedge zhat_j||^2          (exact),
Mt_{ij} the 2x2 principal submatrix.  A collinearity of the triple
vectors (rho -> 1) is EXACTLY a degeneracy of a 2x2 principal
minor of the co-block -- which the positive-chain floor forbids.

(b) THE DERIVATION CHAIN (each step an inequality with an explicit
constant, verified per rung):
 R1  WEDGE IDENTITY (exact): 1 - r_ij^2 == det2/(Mt_ii Mt_jj) ==
     ||zhat_i wedge zhat_j||^2; and det2 == lam2 (T_ij - lam2)
     with lam2 = lam_min(Mt_{ij}), T_ij = Mt_ii + Mt_jj.
 R2  INTERLACING (global linear algebra): lam2 >= lam_min(B) for
     triple pairs (principal submatrix of the co-block); the map
     x -> x (T_ij - x) is increasing on x <= T_ij/2, so
       1 - r_ij^2 >= c (T_ij - c) / (Mt_ii Mt_jj)
     for ANY floor 0 < c <= lam_min(B).
 R3  THE FLOOR -- THE SAME CHRISTOFFEL MACHINERY AS W1 (explicit):
     (i)  H1/H2 ROUTE: the CLXXVII Gershgorin statement on the
          UNROTATED core CD-Gram G_core gives G_core >= (a-b) I_8;
          rotation invariance + principal submatrix give
          P_G >= (a-b) I_7 (warded); with the v905/bfloor
          half-dominance B - P_G/2 >= 0 (decided EXACT-RATIONALLY
          per step, base.pd_exact -- the declared v897 decision
          class, a certificate not a construction):
            lam_min(B) >= (a-b)/2 =: c_h12.
     (ii) BATTERY ROUTE: c_cls := best_cert(P_G)/2 (the round-62
          G-battery on P_G directly) under the same exact
          half-dominance.
     Both floors are source-only constructions + exact decisions;
     their all-h grounding is EXACTLY the W1 hypotheses H1/H2 --
     the named reduction.
 R4  THE SCALE RUNG (the denominators), three variants per pair:
     (i)   DIAG-MEAS: Mt_ii, Mt_jj measured (anatomy; all-h law
           OPEN, named);
     (ii)  COND-B: max(Mt_ii, Mt_jj) <= lam_max(B) (interlacing
           up, warded) -- the bound becomes 1 - r^2 >=
           c/cond-type; lam_max(B)'s all-h law OPEN, named;
     (iii) TAU-GLOBAL: S_2 <= I (exact GIVEN the complement-block
           positivity R >= 0 of A = I - G -- WALL-ADJACENT input,
           declared and typed honestly, never silent), so
           Mt <= (1/tau_1) I and max diag <= 1/tau_1.
 R5  COMPOSE (per step): 1 - rho_h >= 1 - max_ij |r_ij|
     >= min_ij (1 - r_ij^2)/2 >= min_ij c (T_ij - c) /
     (2 Mt_ii Mt_jj) =: marg_der(route), for each floor route x
     denominator variant.  SOUNDNESS WARD: marg_der <= measured
     margin on every step (transcription ward; the chain is a
     proven inequality).  Slack ladder printed per rung; bands +
     h-trends over 39 + 27 deep.

(c) VERDICT (frozen enum, decided by the rules below and nothing
else):
  RHO-DERIVED(route, min marg) iff every R1-R5 ward passes AND
    marg_der(route) > 0 on ALL 39 + 27 steps for route = (H1/H2
    floor, DIAG-MEAS) -- the canonical route -- AND the combined
    h-trend |slope(log marg_der)| <= HTREND_FLAT AND the soundness
    ward holds; the verdict names every remaining gap explicitly:
    all-h H1/H2 (== the W1 gap, same seat), the all-h diagonal law
    of Mt, the half-dominance uniformity.  This is the
    RHO-REDUCES-TO-W1 headline: the rho margin is carried by the
    SAME Christoffel floor.
  RHO-SLACK-FAILS(rung) with rung = the FIRST failing step of the
    chain in the order R3-floor-nonpositive (a-b <= 0 or dominance
    refused anywhere), R5-composed-nonpositive, R5-trend, plus the
    deficit band and what stronger-but-still-global input would
    fix it.
  The TAU-GLOBAL variant is always typed separately (expected to
    lose the tau scale -- measured, not assumed).
DEAD overrides (kill anyway): parent reproduction fails, CLXXVI
rho census fails to reproduce, any R1/R2/R4(ii)/soundness ward
breaks, backstop PD of Mt fails.

(d) GATES.  TAU-SCREENS (parent bands): measured margin, derived
margin (canonical route).  CONTROLS (kill if silent): C1 smooth
world refuses (B0 not PD / dominance dies -- the chain refuses at
R3; census); C2 Epstein + scramble fire (parent verbatim); C3
CONSTRUCTION SENSITIVITY (kill): weight-reversal on the positive
chain (v -> reversed v, CLXXVII control) must move the R3 floor:
med |dlog max(c_cls', eps)/...| computed as med |c_cls' - c_cls|
/ |c_cls| >= MOVE_BAR.  ANTI-CIRCULARITY (frozen): rho, Mt, B
consume only matrix ENTRIES of the framed step form (CLXXVI
convention); the floors are source-only constructions (positive
chain CD data + r1 Householder frame) with exact-rational
DECISIONS on the target difference (declared v897/v905 class); no
sigma_h, no forward pivot sign, no target eigendata in any
construction; float eigensolves appear only as measured anatomy
(lam_min/max(B), lam2) next to the warded inequalities; R4(iii)'s
wall-adjacent input is declared at its seat.

ANTHROPIC NO-GO DECLARATION: the chain reads 2x2 principal minors,
a 7x7 Loewner half-dominance and an 8-node CD-kernel Gram --
strictly beyond two scalar moments plus bandwidth-1 pair
correlation; no contradiction with the two-moment no-go.

FROZEN BARS: WEDGE_WARD = 1e-9 (rel, R1); INTER_TOL = 1e-12 (R2);
PGSHIFT_TOL = 1e-9 (P_G >= (a-b) I ward); SOUND_TOL = 1e-12 (R5);
RHO_MED_REF = 0.918, RHO_MAX_REF = 0.957, RHO_RTOL = 5e-2 (CLXXVI
reproduction); MARGIN_MIN_REF = 0.043 (context print);
HTREND_FLAT = 0.30; slope bands 0.30/0.70 (parent verbatim);
MOVE_BAR = 0.05; MIN_DEEP = 10; parent bars (MINB_REF 0.679, GAP
0.052/0.888, rtol as parent) inherited verbatim; parent SPEC-SHA
warded == 084c9689..; wedge SPEC-SHA prefix warded == 26855819.
Runtime cap declared: 20 min.  Smoke mode RHO_SMOKE=1 restricts
the deep block to the 4 shallowest new rungs (surface + controls
always full); any smoke run is disclosed here before the freeze.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke run
(RHO_SMOKE=1, 23/23 on the FIRST passage, 6.9 s; deep block on
the 4 shallowest new rungs -> 3 deep steps).  NO bar, band, count,
rule or enum was moved after it; the only post-smoke change is
this disclosure block itself.  Measured smoke context the frozen
run must confirm: W green (42/41/39, minB 0.6790, gap 0.0520/
0.8875); CLXXVI rho census reproduced (rho_h med 0.9196, max
0.9567, band 0.8127..0.9567, margin min 0.0433; top-pair census
x1-x2:30, x1-x3:8, x2-x3:1 == the CLXXV census EXACTLY); R1 wedge
identity max rel dev 9.2e-15 incl. det2 == lam2(T-lam2); R2
interlacing 39/39 (min slack +0.0314); R3 floors: P_G >= (a-b) I
ward 39/39, exact half-dominance B - P_G/2 PD 39/39, c_h12 band
0.2101/0.3834/0.4632, c_cls band 0.1658/0.3774/0.4627; R4 diag
anatomy: triple diagonals Mt_ii band 3.98/188/8.4e+03 (LARGE),
lam_max(B) interlacing ward 39/39, 1/tau_1 med 7.1e+05 -- the
TAU-GLOBAL route loses 3.6 dex (typed, measured); R5 composed
canonical marg_der band 6.93e-05 / 1.79e-03 / 1.98e-02, POSITIVE
on 39/39, sound 39/39, slack measured/derived 6.4/40.0/1328 x;
battery route band 6.66e-05/1.72e-03/1.98e-02, COND-B route
8.47e-06/2.67e-04/3.38e-03; deep smoke 3/3: derived positive 3/3
(min 9.59e-04), sound, rho 0.9001/0.9148/0.9180; C1 smooth
refuses at R3 on 39/39, C2 Epstein + scramble fire, C3
weight-reversal moves the floor med rel 0.341 >= 0.05; screens
measured margin PASS(+0.018, R2 0.008), derived margin
PASS(+0.226, R2 0.080).  THE KNIFE-EDGE, disclosed: on the smoke
set (39 + 3 points) the combined h-trend of the canonical derived
margin read slope +0.302 (R2 0.017) against the frozen flat bar
0.30 -- a 0.002 miss with an R2 that explains nothing; the frozen
rule types this R5-trend SLACK-FAILS.  THE BAR IS NOT MOVED (no
post-smoke upgrade, CLXXVII precedent); the frozen run's FULL
27-step deep block re-measures the slope and the enum moves only
as the full data says.

NO RH claim.  Even RHO-DERIVED is a conditional reduction: the
skeleton margin follows from the SAME (unproven-for-all-h) H1/H2
Christoffel hypotheses plus named diagonal/dominance laws; the
background admittance half of CLXXVI and W2 / background
cancellation (the wall) remain RH-hard and untouched.  No marker
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
import wedge_scale_law_probe as wedge  # noqa: E402  (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
WEDGE_SHA8 = "26855819"
WEDGE_WARD = 1.0e-9
INTER_TOL = 1.0e-12
PGSHIFT_TOL = 1.0e-9
SOUND_TOL = 1.0e-12
RHO_MED_REF = 0.918
RHO_MAX_REF = 0.957
RHO_RTOL = 5.0e-2
MARGIN_MIN_REF = 0.043
HTREND_FLAT = 0.30
MOVE_BAR = 0.05
MIN_DEEP = 10
TRIPLE_IDX = ((1, 2), (1, 3), (2, 3))
SMOKE = os.environ.get("RHO_SMOKE", "") == "1"
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


def band(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def battery_split(Gc):
    a = float(np.min(np.diag(Gc)))
    off = np.sum(np.abs(Gc), axis=1) - np.abs(np.diag(Gc))
    return a, float(np.max(off))


def step_objects(Mt, Gc, Q):
    """The per-step chain objects (Mt 8x8, Gc unrotated CD-Gram)."""
    B = Mt[1:, 1:]
    P = Q.T @ Gc @ Q
    P = 0.5 * (P + P.T)
    PG = P[1:, 1:].copy()
    a, b = battery_split(Gc)
    return B, PG, a, b


def chain_eval(Mt, B, PG, a, b):
    """Evaluate the R1-R5 chain on one step.  Returns dict."""
    out = dict()
    # rho census
    dg = np.sqrt(np.diag(Mt))
    R = Mt / np.outer(dg, dg)
    rs = [R[i, j] for i, j in TRIPLE_IDX]
    out["rho"] = float(np.mean(np.abs(rs)))
    out["rmax"] = float(np.max(np.abs(rs)))
    out["top"] = TRIPLE_IDX[int(np.argmax(np.abs(rs)))]
    out["margin"] = 1.0 - out["rho"]
    # R1 wedge identity
    Z = np.linalg.cholesky(0.5 * (Mt + Mt.T))
    wdev = 0.0
    lamB = float(np.linalg.eigvalsh(B)[0])
    lamBmax = float(np.linalg.eigvalsh(B)[-1])
    out["lamB"] = lamB
    out["lamBmax"] = lamBmax
    inter_min = float("inf")
    pair = []
    for i, j in TRIPLE_IDX:
        M2 = Mt[np.ix_((i, j), (i, j))]
        det2 = float(np.linalg.det(M2))
        one_r2 = 1.0 - R[i, j] ** 2
        v1 = det2 / (Mt[i, i] * Mt[j, j])
        zi, zj = Z[i] / np.linalg.norm(Z[i]), Z[j] / np.linalg.norm(Z[j])
        wnorm = 1.0 - float(zi @ zj) ** 2
        wdev = max(wdev, abs(one_r2 - v1) / max(one_r2, 1e-300),
                   abs(one_r2 - wnorm) / max(one_r2, 1e-300))
        lam2 = float(np.linalg.eigvalsh(M2)[0])
        det_id = lam2 * (M2[0, 0] + M2[1, 1] - lam2)
        wdev = max(wdev, abs(det2 - det_id) / max(abs(det2), 1e-300))
        inter_min = min(inter_min, lam2 - lamB)
        pair.append((i, j, Mt[i, i], Mt[j, j], one_r2))
    out["wdev"] = wdev
    out["inter_min"] = inter_min
    out["pair"] = pair
    # R3 floors
    c_h12 = 0.5 * (a - b)
    c_cls = 0.5 * base.best_cert(PG)
    lamPG = float(np.linalg.eigvalsh(PG)[0])
    out["pg_shift_ok"] = lamPG >= (a - b) - PGSHIFT_TOL
    Dfr = base.mat_fr(B - 0.5 * PG)
    out["dom_ok"] = base.pd_exact(Dfr)[0]
    out["c_h12"] = c_h12
    out["c_cls"] = c_cls
    # R4 diag interlacing ward
    dmax = max(Mt[i, i] for i, j in TRIPLE_IDX for i in (i, j))
    out["diag_ok"] = dmax <= lamBmax + INTER_TOL
    # R5 compose per route
    def compose(c, den_fn):
        if c <= 0.0:
            return 0.0
        vals = []
        for i, j, mii, mjj, _ in pair:
            di, dj = den_fn(mii, mjj)
            T = di + dj
            cc = min(c, T / 2.0)
            vals.append(cc * (T - cc) / (2.0 * di * dj))
        return min(vals)
    out["m_h12"] = compose(c_h12 if out["dom_ok"] else 0.0,
                           lambda x, y: (x, y))
    out["m_cls"] = compose(c_cls if out["dom_ok"] else 0.0,
                           lambda x, y: (x, y))
    out["m_cond"] = compose(c_h12 if out["dom_ok"] else 0.0,
                            lambda x, y: (lamBmax, lamBmax))
    return out


def deep_step(g1, g2):
    """Mt/Gc for a deep step (CLXXVI = bfloor conventions)."""
    _w, VS = np.linalg.eigh(g1["S"])
    Q = base.householder_frame(VS[:, 0])
    Mt = Q.T @ (g2["S"] / g1["tau"]) @ Q
    Mt = 0.5 * (Mt + Mt.T)
    al, be, m0 = g2["chain"]
    Pc = base.eval_chain(al, be, m0, g2["y_core"], g2["h"])
    H0 = np.sqrt(g2["v_core"])[:, None] * Pc
    Gc = H0 @ H0.T
    Gc = 0.5 * (Gc + Gc.T)
    if float(np.linalg.eigvalsh(Mt)[0]) <= 0.0:
        return None
    return dict(kz=g2["kz"], h=g2["h"], Mt=Mt, Gc=Gc, Q=Q,
                tau=g1["tau"])


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
    else:
        verdict = ("RHOALLH-MEASURED / %s / %s / %s"
                   % (labels.get("r", "-"), labels.get("t", "-"),
                      labels.get("head", "-")))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: every derived margin is an explicit inequality
  chain on the float64-computed step matrices, with the exact-
  rational half-dominance decision per step (v897/v905 class); a
  DERIVED verdict is a conditional reduction to the named inputs
  (H1/H2 Christoffel floor == the W1 gap, diagonal law, dominance
  uniformity), NOT an all-h theorem; the background admittance
  half of CLXXVI and W2 / background cancellation remain RH-hard.
  NO RH claim; no marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.PSI4.RHOALLH.01 -- the rho margin as a "
            "wedge/Gram-determinant of the positive chain "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    parent_sha = hashlib.sha256(
        parent.__doc__.encode("utf-8")).hexdigest()
    wedge_sha = hashlib.sha256(
        wedge.__doc__.encode("utf-8")).hexdigest()
    print("    parent SPEC SHA-256 = %s" % parent_sha)
    print("    wedge  SPEC SHA-256 = %s" % wedge_sha)
    print("    NO RH claim.  The floors are source-only; exact "
          "decisions are float-entry level (declared).")
    if SMOKE:
        print("    *** SMOKE MODE: deep on 4 shallowest new rungs ***")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced", parent_sha == PARENT_SHA,
          kill="K2")
    check("S0c wedge SPEC prefix reproduced",
          wedge_sha[:8] == WEDGE_SHA8, wedge_sha[:8], kill="K2")

    # ------------------------------------------------------------ W
    section("W -- parent ladder + reproduction")
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

    # ------------------------------------------------------------ A
    section("A -- surface chain (39 steps)")
    res = []
    for w in rows:
        Gc = w["H"] @ w["H"].T
        Gc = 0.5 * (Gc + Gc.T)
        B, PG, a, b = step_objects(w["M"], Gc, w["Q"])
        r = chain_eval(w["M"], B, PG, a, b)
        r["h"] = float(w["r2"]["h"])
        r["kz"] = w["r2"]["kz"]
        r["tau"] = w["tau"]
        r["a"] = a
        r["b"] = b
        r["PG"] = PG
        r["B"] = B
        r["Q"] = w["Q"]
        r["w"] = w
        res.append(r)
    rho_arr = np.array([r["rho"] for r in res])
    marg_arr = np.array([r["margin"] for r in res])
    rmax_arr = np.array([r["rmax"] for r in res])
    tops = {}
    for r in res:
        key = "x%d-x%d" % r["top"]
        tops[key] = tops.get(key, 0) + 1
    check("W3 CLXXVI rho census reproduced (med %.4f == %.3f, max "
          "%.4f == %.3f)" % (float(np.median(rho_arr)), RHO_MED_REF,
                             float(np.max(rho_arr)), RHO_MAX_REF),
          abs(float(np.median(rho_arr)) / RHO_MED_REF - 1.0)
          <= RHO_RTOL
          and abs(float(np.max(rho_arr)) / RHO_MAX_REF - 1.0)
          <= RHO_RTOL, kill="K2")
    print("    rho_h band %.4f / %.4f / %.4f; margin 1-rho min "
          "%.4f (CLXXVI: %.3f); top-pair census %s"
          % (band(rho_arr) + (float(np.min(marg_arr)),
                              MARGIN_MIN_REF, tops)))
    wdev = max(r["wdev"] for r in res)
    check("A1 R1 wedge/Gram-determinant identity",
          wdev <= WEDGE_WARD, "max rel dev %.2e" % wdev, kill="K2")
    inter = min(r["inter_min"] for r in res)
    check("A2 R2 interlacing lam_min(pair) >= lam_min(B)",
          inter >= -INTER_TOL, "min slack %+.4f" % inter, kill="K2")
    n_pg = sum(r["pg_shift_ok"] for r in res)
    n_dom = sum(r["dom_ok"] for r in res)
    check("A3 R3 wards: P_G >= (a-b) I on %d/%d; exact half-"
          "dominance B - P_G/2 PD on %d/%d"
          % (n_pg, len(res), n_dom, len(res)),
          n_pg == len(res), kill="K2")
    ch12 = np.array([r["c_h12"] for r in res])
    ccls = np.array([r["c_cls"] for r in res])
    print("    floors: c_h12 = (a-b)/2 band %.4f / %.4f / %.4f; "
          "c_cls = best_cert(P_G)/2 band %.4f / %.4f / %.4f"
          % (band(ch12) + band(ccls)))
    n_diag = sum(r["diag_ok"] for r in res)
    check("A4 R4 diag interlacing max Mt_ii <= lam_max(B) on "
          "%d/%d" % (n_diag, len(res)), n_diag == len(res),
          kill="K2")
    dvals = np.array([x for r in res
                      for _i, _j, mii, mjj, _o in r["pair"]
                      for x in (mii, mjj)])
    print("    triple diagonals Mt_ii band %.3g / %.3g / %.3g; "
          "lam_max(B) band %.3g / %.3g / %.3g; 1/tau_1 med %.3g "
          "(TAU-GLOBAL scale)"
          % (band(dvals) + band(np.array([r["lamBmax"]
                                          for r in res]))
             + (float(np.median([1.0 / r["tau"] for r in res])),)))
    m_h12 = np.array([r["m_h12"] for r in res])
    m_cls = np.array([r["m_cls"] for r in res])
    m_cond = np.array([r["m_cond"] for r in res])
    sound = all(r["m_h12"] <= r["margin"] + SOUND_TOL
                and r["m_cls"] <= r["margin"] + SOUND_TOL
                for r in res)
    check("A5 R5 soundness: derived <= measured margin on every "
          "step", sound, kill="K2")
    n_pos = int(np.sum(m_h12 > 0.0))
    print("    composed canonical (H1/H2 x DIAG-MEAS) marg_der "
          "band %.3g / %.3g / %.3g (> 0 on %d/%d)"
          % (band(m_h12) + (n_pos, len(res))))
    print("    composed battery route band %.3g / %.3g / %.3g; "
          "COND-B route band %.3g / %.3g / %.3g"
          % (band(m_cls) + band(m_cond)))
    slack = marg_arr / np.maximum(m_h12, 1e-300)
    print("    slack measured/derived band %.1f / %.1f / %.1f x"
          % band(slack[m_h12 > 0]))
    check("A6 surface slack ladder recorded", True)

    # ------------------------------------------------------------ D
    section("D -- deep holdout (4e6 table, float level declared)")
    lam_ext = deep.build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("D1 deep-table fidelity: overlap dev %.1e == 0.0" % dev,
          dev == 0.0, kill="K2")
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
    check("D2 new-rung census %d (>= %d)"
          % (len(order_kz), MIN_DEEP), len(order_kz) >= MIN_DEEP,
          kill="K1")
    if KILLS:
        return finish({})
    if SMOKE:
        order_kz = order_kz[:4]
    grams = []
    for kz in order_kz:
        g = deep.ext_gram(kz)
        if isinstance(g, dict) and g.get("core_ok"):
            grams.append(g)
        print("    deep gram kz %3d: %s  [%.1f s]"
              % (kz, "ok" if isinstance(g, dict)
             and g.get("core_ok") else "unusable",
             time.time() - T0), flush=True)
    grams.sort(key=lambda g: (g["h"], g["kz"]))
    dres = []
    d_wdev = 0.0
    d_inter = float("inf")
    d_pg = d_dom = d_diag = 0
    d_sound = True
    for g1, g2 in zip(grams, grams[1:]):
        if g1["negA"] > 0 or g1["negS"] > 0 or g1["lamS"] <= 0.0:
            continue
        st = deep_step(g1, g2)
        if st is None:
            continue
        B, PG, a, b = step_objects(st["Mt"], st["Gc"], st["Q"])
        r = chain_eval(st["Mt"], B, PG, a, b)
        r["h"] = float(st["h"])
        r["tau"] = st["tau"]
        d_wdev = max(d_wdev, r["wdev"])
        d_inter = min(d_inter, r["inter_min"])
        d_pg += r["pg_shift_ok"]
        d_dom += r["dom_ok"]
        d_diag += r["diag_ok"]
        d_sound &= (r["m_h12"] <= r["margin"] + SOUND_TOL)
        dres.append(r)
        print("    deep kz %-4d h %-5d rho %.4f margin %.4f "
              "c_h12 %+.4f m_der %.3g  [%.1f s]"
              % (st["kz"], st["h"], r["rho"], r["margin"],
                 r["c_h12"], r["m_h12"], time.time() - T0),
              flush=True)
    n_d = len(dres)
    print("    %d deep steps" % n_d)
    check("D3 deep wards: wedge %.1e, interlacing %+.4f, P_G-shift "
          "%d/%d, dominance %d/%d, diag %d/%d, sound %s"
          % (d_wdev, d_inter, d_pg, n_d, d_dom, n_d, d_diag, n_d,
             d_sound),
          d_wdev <= WEDGE_WARD and d_inter >= -INTER_TOL
          and d_pg == n_d and d_diag == n_d and d_sound,
          kill="K2")
    dm = np.array([r["m_h12"] for r in dres])
    dmarg = np.array([r["margin"] for r in dres])
    d_pos = int(np.sum(dm > 0.0))
    dlab = ("DEEP(rho med %.4f, margin min %.4f, derived > 0 on "
            "%d/%d, min %.3g)"
            % (float(np.median([r["rho"] for r in dres]))
               if dres else float("nan"),
               float(np.min(dmarg)) if n_d else float("nan"),
               d_pos, n_d, float(np.min(dm)) if n_d else
               float("nan")))
    check("D4 typed: %s" % dlab, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    n_ref = 0
    n_use = 0
    for w in rows:
        if w.get("r2") is None:
            continue
        B0 = None
        rs2 = base.gram_anatomy(w["r2"]["kz"],
                                world_fn=base.world_smooth,
                                keep_chain=True)
        if isinstance(rs2, dict) and "S" in rs2:
            M0 = w["Q"].T @ (rs2["S"] / w["r1"]["tau"]) @ w["Q"]
            M0 = 0.5 * (M0 + M0.T)
            B0 = M0[1:, 1:]
        if B0 is None:
            n_ref += 1
            continue
        n_use += 1
        if not base.pd_exact(base.mat_fr(0.5 * (B0 + B0.T)))[0]:
            n_ref += 1
    check("C1 smooth world refuses the chain at R3 (B0 not PD / "
          "frame dead on %d of %d)" % (n_ref, len(rows)),
          n_ref >= 30, kill="K2")
    for kind in ("epstein", "scramble"):
        fired, detail = parent.control_fires(kind)
        check("C2 %s world fires" % kind, fired, detail, kill="K2")
    moves = []
    for r in res:
        w = r["w"]
        v = w["r2"]["v_core"]
        Pc = w["H"] / np.sqrt(v)[:, None]
        vr = v[::-1]
        Gp = (np.sqrt(vr)[:, None] * (Pc @ Pc.T)
              * np.sqrt(vr)[None, :])
        Gp = 0.5 * (Gp + Gp.T)
        PGp = (w["Q"].T @ Gp @ w["Q"])[1:, 1:]
        c2 = 0.5 * base.best_cert(0.5 * (PGp + PGp.T))
        moves.append(abs(c2 - r["c_cls"])
                     / max(abs(r["c_cls"]), 1e-300))
    med_mv = float(np.median(moves))
    check("C3 weight-reversal moves the R3 floor: med rel move "
          "%.3f >= %.2f" % (med_mv, MOVE_BAR), med_mv >= MOVE_BAR,
          kill="K2")

    # ---------------------------------------------------- screens
    section("S -- mandatory tau screens")
    taus = np.array([r["tau"] for r in res])
    scr_m, _ = parent.screen(marg_arr, taus)
    scr_d, _ = parent.screen(m_h12, taus)
    print("    TAU-SCREEN measured margin %s" % scr_m)
    print("    TAU-SCREEN derived margin  %s" % scr_d)
    check("S screens recorded", True)

    # ---------------------------------------------------- verdict
    all_m = np.concatenate([m_h12, dm]) if n_d else m_h12
    all_h = np.concatenate([np.array([r["h"] for r in res]),
                            np.array([r["h"] for r in dres])]) \
        if n_d else np.array([r["h"] for r in res])
    n_all = len(all_m)
    n_posall = int(np.sum(all_m > 0.0))
    floor_ok = (n_dom + d_dom == n_all
                and float(np.min(np.concatenate(
                    [ch12, np.array([r["c_h12"] for r in dres])])
                    if n_d else ch12)) > 0.0)
    if n_posall == n_all:
        sl, r2f = parent.ols_line(np.log(all_h), np.log(all_m))
        flat = np.isfinite(sl) and abs(sl) <= HTREND_FLAT
    else:
        sl, r2f, flat = float("nan"), float("nan"), False
    reloc = "RELOCATION" in scr_d
    if not floor_ok:
        rv = ("RHO-SLACK-FAILS(R3-floor: a-b <= 0 or dominance "
              "refused on %d steps; fix: the W1 H1/H2 floor "
              "itself)" % (n_all - n_posall))
    elif n_posall != n_all:
        rv = ("RHO-SLACK-FAILS(R5-composed: nonpositive on %d/%d; "
              "deficit at the diagonal scale; fix: an O(1) "
              "diagonal law for the equilibrated core)"
              % (n_all - n_posall, n_all))
    elif not flat or reloc:
        rv = ("RHO-SLACK-FAILS(R5-trend: slope %+.3f R2 %.3f, "
              "reloc=%s; the derived margin is not h-flat)"
              % (sl, r2f, reloc))
    else:
        rv = ("RHO-DERIVED(canonical H1/H2 x DIAG-MEAS, min marg "
              "%.3g, trend %+.3f R2 %.3f; GAPS NAMED: all-h H1/H2 "
              "== the W1 gap, all-h diagonal law of Mt, half-"
              "dominance uniformity)"
              % (float(np.min(all_m)), sl, r2f))
    tglob = ("TAU-GLOBAL(1/tau med %.2g vs diag med %.2g: the "
             "unconditional denominator loses %.1f dex)"
             % (float(np.median([1.0 / r["tau"] for r in res])),
                float(np.median(dvals)),
                math.log10(float(np.median([1.0 / r["tau"]
                                            for r in res]))
                           / max(float(np.median(dvals)), 1e-300))))
    if rv.startswith("RHO-DERIVED"):
        head = ("RHO-REDUCES-TO-W1(the skeleton margin is carried "
                "by the SAME Christoffel floor: 1 - rho >= "
                "(a-b)(T-c)/(4 Mt_ii Mt_jj); skeleton only, W2/"
                "background remain RH-hard)")
    else:
        head = "RHO-ALLH-BLOCKED(%s)" % rv.split("(")[0]
    check("V1 typed: %s" % rv, True)
    check("V2 typed: %s" % tglob, True)
    labels = dict(r=rv, t=tglob, head=head)
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
