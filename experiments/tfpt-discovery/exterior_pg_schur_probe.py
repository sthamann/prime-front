#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""exterior_pg_schur_probe -- PRIME.PORT.EXTERIOR.PG.SCHUR.01
(EXPLORATION ONLY, experiments/; round 64, 2026-08-11).

THEORY FIRST -- THE CANDIDATE MECHANISM.  On every reachable fixed-core
step, write the exact tangent end-form and the positive-chain CD Gram in
the SAME frozen Householder frame:

    M = [[n, b*], [b, B]],             P = V V* =
        [[p00, p*], [p, P_G]].

Here M = Q* S(r2) Q / tau(r1) is the v901 end-form, while

    V = Q* [sqrt(v_i) p_k(y_i)]_{i=1..8, k<h}

uses only the positive folded measure and its orthonormal-polynomial
chain at rung r2.  Thus P is a source-only positive Gram object and its
Schur pivot has the EXACT exterior-square interpretation

    s_P = p00 - p* P_G^{-1} p
        = ||v0 - Proj_span(v1,...,v7) v0||^2
        = det(P) / det(P_G)
        = ||v0 wedge ... wedge v7||^2
          / ||v1 wedge ... wedge v7||^2 >= 0.

This is the sought positive exterior currency: not a fitted identity,
and not target positivity in disguise.  It uses the FULL CD-Gram,
whereas v905 used only its co-block P_G.

THE PROPOSED TWO-LEMMA CERTIFICATE (frozen before the run):

  L1  M >= (1/2) P  in Loewner order;
  L2  s_P >= mu1(h),  mu1(h) = 4 sin^2(pi/(2h+1)).

If L1 and L2 hold, inversion reverses Loewner order and the directional
Schur pivot obeys

    s_M = 1/(e0* M^{-1} e0)
        >= (1/2)/(e0* P^{-1} e0)
         = (1/2) s_P >= (1/2) mu1.

This would derive the registered half-gap constant 1/2 from the
canonical v905 half-dominance and a positive exterior quotient.  The
implication is a theorem of finite-dimensional linear algebra.  THE
OPEN MATHEMATICS would then be uniform L1/L2 for all h and interval
enclosure of the construction; this probe only decides whether the
candidate even survives the 39-step surface.

THE SCHUR LOCALIZATION OF L1 (also exact).  Since v905 certifies the
co-block D_B := B - P_G/2 > 0 on the surface,

    M - P/2 > 0
      iff ell_ext := n - p00/2
                    - (b-p/2)* D_B^{-1} (b-p/2) > 0.

So a failure has one named seat: the exterior Schur scalar, not the
already-closed B-half.  The generalized Loewner radius

    c_star = lambda_min(P^{-1/2} M P^{-1/2})

is measured only as anatomy.  c_star >= 1/2 is exactly L1; c_star,
target eigendata, and all eigensolves are NEVER construction inputs.

FROZEN PROTOCOL:

 W  REPRODUCTION (kill -> PIPELINE-BROKEN / WARD-BROKEN): the
    bfloor_pg_dominance machinery is imported read-only; 42 rungs,
    >=30 full-core rungs, >=20 consecutive steps, truth A/R/S PSD;
    39 step rows; min eig(B) = 0.679 (2 percent), Schur gap min/med
    = 0.052/0.888 (5 percent); P_G PD and B-P_G/2 PD on all steps.

 E1 EXTERIOR IDENTITY (kill -> WARD-BROKEN): on every step P = V V*
    and P_G is its 7x7 co-block; s_P agrees by four routes -- Schur,
    row-space projection residual, determinant quotient, and
    1/(P^{-1})00 -- to EXT_WARD relative.  P and P_G must be PD.
    This proves the finite computed identity, not an all-h bound.

 E2 THE TWO LEMMAS (typed, never kill):
    L1 exact-rational LDL census of M-P/2 and D_B = B-P_G/2;
    L2 census s_P >= mu1.  Headline EXTERIOR-HALFGAP-CLOSES-SURFACE
    iff both are all/all; otherwise EXTERIOR-HALFGAP-REFUSED with
    exact failing lists.  On every L1 pass, the implication
    s_M >= s_P/2 is numerically warded (a theorem, the ward catches
    transcription errors).  The registered target itself is only a
    reproduction measurement, never an input.

 E3 FAILURE / SCALE ANATOMY (typed): c_star ladder; ell_ext ladder;
    failure eigenvector e0-overlap (SCHUR-SEATED iff median >= 1/2);
    s_P/mu1; and tau screens of positive c_star, c_star-1/2,
    ell_ext, and s_P/mu1.  Bands: PASS |slope| <= 0.30, RELOCATION
    slope >= 0.70, else AMBIG.  A slope near +1 for the decisive
    margin is a relocation kill, not progress.

 C  CONTROLS (kill -> WARD-BROKEN if silent): smooth world must
    refuse before or at the full certificate (wall A/S not PSD or
    L1/L2 fails); Epstein x^2+5y^2 and position-scramble seed 1 at
    kz 9 must break the wall/frame and therefore refuse.  The exact
    exterior identity may survive controls -- it is algebra; the
    certificate must not.

ANTI-CIRCULARITY: P and V use only r2's positive-chain CD data and
the backward r1 Householder frame.  The frozen coefficient 1/2 and
mu1 are source-only.  No sigma_h, forward pivot sign, target
eigenvector, or target eigendata enters a construction.  Exact LDL
of the target difference is a decision procedure, as in v905.

ANTHROPIC NO-GO DECLARATION: this route uses information strictly
beyond two scalar moments plus bandwidth-1 pair correlation: the
entire degree-(h-1) positive CD evaluation matrix, its matrix Loewner
order against M, and an eight-row exterior/Cauchy-Binet quotient.
It does not contradict a two-moment positive-proportion no-go.

SPEC v1 (2026-08-11, frozen and SHA-hashed before the first run):
everything above.  Constants: CORE_J=(2,...,16), H_MAX=900,
N_RUNGS=42, N_STEPS=39, HALF=1/2 exactly, EXT_WARD=1e-8,
IMPL_WARD=1e-8, MINB_REF=.679, GAP_REF=(.052,.888), screen bands
.30/.70.  No smoke run.  Any amendment will be recorded here
without deleting this v1 history.

NO RH claim.  A success would be a finite-surface experiment, not an
all-h theorem; a refusal is a clean kill of this exterior-square
mechanism.  No marker moves.  Stdout only.
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import bfloor_pg_dominance_probe as base  # noqa: E402  (READ-ONLY machinery)

HALF = Fraction(1, 2)
N_RUNGS_EXP = 42
N_STEPS_EXP = 39
MIN_CORE_RUNGS = 30
MIN_STEPS = 20
MINB_REF = 0.679
MINB_RTOL = 2.0e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5.0e-2
EXT_WARD = 1.0e-8
IMPL_WARD = 1.0e-8
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return 0.0, float("nan")
    slope = float(np.cov(x, y, bias=True)[0, 1] / vx)
    intercept = float(np.mean(y) - slope * np.mean(x))
    residual = y - intercept - slope * x
    ss = float(residual @ residual)
    centered = y - float(np.mean(y))
    st = float(centered @ centered)
    return slope, (1.0 - ss / st if st > 0.0 else float("nan"))


def screen(values, taus):
    values = np.asarray(values, float)
    taus = np.asarray(taus, float)
    mask = np.isfinite(values) & (values > 0.0) & (taus > 0.0)
    if int(np.sum(mask)) < 3:
        return "VACUOUS(n=%d)" % int(np.sum(mask)), float("nan")
    slope, r2 = ols_line(np.log(taus[mask]), np.log(values[mask]))
    label = ("PASS" if abs(slope) <= SLOPE_PASS
             else "RELOCATION" if slope >= SLOPE_RELOC else "AMBIG")
    return "%s(slope=%+.3f,R2=%.3f,n=%d)" % (
        label, slope, r2, int(np.sum(mask))), slope


def exact_pd(matrix):
    return base.pd_exact(base.mat_fr(np.asarray(matrix, float)))[0]


def build_truth_rows():
    zones = base.ladder_zones()
    truth = []
    for kz in zones:
        rung = base.gram_anatomy(kz, keep_chain=True)
        truth.append(rung)
    if any(r is None for r in truth):
        return zones, truth, [], []
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    full = [r for r in truth if r.get("core_ok")]
    rows = []
    for r1, r2 in zip(truth, truth[1:]):
        if not (r1.get("core_ok") and r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
        _w, vectors = np.linalg.eigh(r1["S"])
        Q = base.householder_frame(vectors[:, 0])
        M = Q.T @ (r2["S"] / r1["tau"]) @ Q
        M = 0.5 * (M + M.T)
        n = float(M[0, 0])
        b = M[1:, 0].copy()
        B = M[1:, 1:].copy()
        gap = n - float(b @ np.linalg.solve(B, b))

        al, be, m0 = r2["chain"]
        Pc = base.eval_chain(al, be, m0, r2["y_core"], r2["h"])
        H = np.sqrt(r2["v_core"])[:, None] * Pc
        V = Q.T @ H
        P = V @ V.T
        P = 0.5 * (P + P.T)
        PG = P[1:, 1:].copy()
        p = P[1:, 0].copy()
        p00 = float(P[0, 0])
        sP = p00 - float(p @ np.linalg.solve(PG, p))
        coeff = np.linalg.solve(PG, p)
        residual = V[0] - coeff @ V[1:]
        sP_projection = float(residual @ residual)
        sP_inverse = 1.0 / float(np.linalg.inv(P)[0, 0])
        signP, logP = np.linalg.slogdet(P)
        signPG, logPG = np.linalg.slogdet(PG)
        sP_det = float(math.exp(logP - logPG)) \
            if signP > 0 and signPG > 0 else float("nan")

        Lhalf = M - 0.5 * P
        DB = B - 0.5 * PG
        db = b - 0.5 * p
        ell_ext = (n - 0.5 * p00
                   - float(db @ np.linalg.solve(DB, db)))

        chol = np.linalg.cholesky(P)
        inv_chol = np.linalg.inv(chol)
        congruent = inv_chol @ M @ inv_chol.T
        congruent = 0.5 * (congruent + congruent.T)
        c_star = float(np.linalg.eigvalsh(congruent)[0])

        eigL, vecL = np.linalg.eigh(0.5 * (Lhalf + Lhalf.T))
        fail_overlap = float(vecL[0, 0] ** 2)
        rows.append(dict(r1=r1, r2=r2, Q=Q, M=M, n=n, b=b, B=B,
                         gap=gap, H=H, V=V, P=P, PG=PG, p=p, p00=p00,
                         sP=sP, sP_projection=sP_projection,
                         sP_inverse=sP_inverse, sP_det=sP_det,
                         Lhalf=Lhalf, DB=DB, ell_ext=ell_ext,
                         c_star=c_star, minL=float(eigL[0]),
                         fail_overlap=fail_overlap, tau=r1["tau"],
                         mu1=mu1_of(r2["h"])))
    return zones, truth, full, rows


def control_fires(kind):
    if kind == "smooth":
        usable = 0
        refused = 0
        smooth = []
        for kz in base.ladder_zones():
            r = base.gram_anatomy(kz, world_fn=base.world_smooth,
                                  keep_chain=True)
            if r is None or not r.get("core_ok") or r.get("negA", 1) > 0 \
                    or r.get("negS", 1) > 0:
                refused += 1
            else:
                usable += 1
                smooth.append(r)
        return refused > 0 and usable < N_STEPS_EXP, \
            "refused=%d usable-core-PD=%d" % (refused, usable)
    if kind == "scramble":
        r = base.gram_anatomy(CTRL_KZ, scramble_seed=1, keep_chain=True)
        fired = r is None or r.get("negA", 1) > 0 or not r.get("core_ok")
        return fired, ("chain-dead" if r is None else
                       "negA=%d core=%s" % (r.get("negA", -1),
                                            r.get("core_ok", False)))
    rr = base.window_of(CTRL_KZ)
    nmax = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lam = base.lambda_eps(nmax)
    nn = np.nonzero(np.abs(lam) > 1.0e-12)[0]
    comb = (np.log(nn.astype(float)),
            2.0 * lam[nn] / np.sqrt(nn.astype(float)))
    r = base.gram_anatomy(CTRL_KZ, comb=comb, keep_chain=True)
    fired = r is None or r.get("negA", 1) > 0 or not r.get("core_ok")
    return fired, ("chain-dead" if r is None else
                   "negA=%d core=%s" % (r.get("negA", -1),
                                        r.get("core_ok", False)))


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _name, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
    else:
        verdict = ("EXTERIORPG-MEASURED / %s / %s / %s / %s"
                   % (labels["l1"], labels["l2"], labels["headline"],
                      labels["seat"]))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: the exterior quotient is exact finite linear algebra
  for the computed CD-Gram.  Even a full surface pass would leave
  all-h uniformity and ideal-object interval enclosure open.  A
  refusal kills this proposed mechanism; it says nothing about RH.
  NO RH claim; no marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.EXTERIOR.PG.SCHUR.01 -- positive CD exterior "
            "quotient versus the half-gap (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim.  HALF=1/2 is frozen; no adjustment.")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")

    section("W -- deployed ladder and v901/v905 reproduction")
    zones, truth, full, rows = build_truth_rows()
    check("W1 frozen rung census", len(zones) == N_RUNGS_EXP,
          "found %d" % len(zones), kill="K1")
    check("W2 all truth chains complete",
          len(truth) == len(zones) and all(r is not None for r in truth),
          kill="K1")
    check("W3 full-core/step census",
          len(full) >= MIN_CORE_RUNGS and len(rows) >= MIN_STEPS,
          "full=%d steps=%d" % (len(full), len(rows)), kill="K1")
    check("W3b truth A/R/S PSD",
          all(r["negA"] == 0 and r["negR"] == 0 and r["negS"] == 0
              for r in full), kill="K1")
    if len(rows) != N_STEPS_EXP:
        check("W3c exact step census %d" % N_STEPS_EXP, False,
              "found %d" % len(rows), kill="K1")
        return finish(dict(l1="-", l2="-", headline="-", seat="-"))
    minB = min(float(np.linalg.eigvalsh(w["B"])[0]) for w in rows)
    gaps = np.array([w["gap"] for w in rows])
    repro = (abs(minB / MINB_REF - 1.0) <= MINB_RTOL
             and abs(float(np.min(gaps)) / GAPMIN_REF - 1.0) <= GAP_RTOL
             and abs(float(np.median(gaps)) / GAPMED_REF - 1.0) <= GAP_RTOL)
    check("W4 v901 end-form reproduction", repro,
          "minB=%.4f gap min/med=%.4f/%.4f"
          % (minB, float(np.min(gaps)), float(np.median(gaps))),
          kill="K2")
    pg_pd = sum(exact_pd(w["PG"]) for w in rows)
    db_pd = sum(exact_pd(w["DB"]) for w in rows)
    check("W5 v905 P_G and half co-block dominance exact",
          pg_pd == len(rows) and db_pd == len(rows),
          "PG=%d/%d DB=%d/%d" % (pg_pd, len(rows), db_pd, len(rows)),
          kill="K2")

    section("E1 -- the exterior/Cauchy-Binet identity")
    ext_devs = []
    p_pd = 0
    gram_devs = []
    for w in rows:
        scale = max(abs(w["sP"]), 1.0e-300)
        ext_devs.extend([
            abs(w["sP"] - w["sP_projection"]) / scale,
            abs(w["sP"] - w["sP_inverse"]) / scale,
            abs(w["sP"] - w["sP_det"]) / scale,
        ])
        gram_devs.append(float(np.linalg.norm(w["P"] - w["V"] @ w["V"].T))
                         / max(float(np.linalg.norm(w["P"])), 1.0e-300))
        p_pd += int(exact_pd(w["P"]))
    max_ext = max(ext_devs)
    max_gram = max(gram_devs)
    check("E1.1 P=VV* and P/P_G exact-PD on every step",
          max_gram <= EXT_WARD and p_pd == len(rows),
          "gram dev %.2e; P exact-PD %d/%d"
          % (max_gram, p_pd, len(rows)), kill="K2")
    check("E1.2 four-route exterior quotient identity",
          max_ext <= EXT_WARD,
          "max relative deviation %.2e" % max_ext, kill="K2")

    section("E2 -- frozen lemmas L1/L2")
    l1_exact = [exact_pd(w["Lhalf"]) for w in rows]
    l2 = [w["sP"] >= w["mu1"] for w in rows]
    l1_fail = [(w["r2"]["kz"], w["r2"]["h"])
               for w, ok in zip(rows, l1_exact) if not ok]
    l2_fail = [(w["r2"]["kz"], w["r2"]["h"])
               for w, ok in zip(rows, l2) if not ok]
    implication_dev = 0.0
    for w, ok in zip(rows, l1_exact):
        if ok:
            implication_dev = max(
                implication_dev,
                max(0.0, 0.5 * w["sP"] - w["gap"])
                / max(abs(w["gap"]), abs(0.5 * w["sP"]), 1.0e-300))
    check("E2.1 Loewner implication ward on every L1 pass",
          implication_dev <= IMPL_WARD,
          "one-sided relative violation %.2e" % implication_dev,
          kill="K2")
    half_actual = [w["gap"] >= 0.5 * w["mu1"] for w in rows]
    check("E2.2 registered half-gap reproduced (measurement only)",
          all(half_actual), "%d/%d" % (sum(half_actual), len(rows)),
          kill="K2")
    print("    L1 exact M-P/2 PD: %d/%d; failures %s"
          % (sum(l1_exact), len(rows), l1_fail))
    print("    L2 exterior pivot >= mu1: %d/%d; failures %s"
          % (sum(l2), len(rows), l2_fail))
    closes = all(l1_exact) and all(l2)
    labels = {
        "l1": "L1-DOM(%d/%d)" % (sum(l1_exact), len(rows)),
        "l2": "L2-EXTMU(%d/%d)" % (sum(l2), len(rows)),
        "headline": ("EXTERIOR-HALFGAP-CLOSES-SURFACE"
                     if closes else
                     "EXTERIOR-HALFGAP-REFUSED"),
    }

    section("E3 -- failure seat, scales, and mandatory tau screens")
    cstar = np.array([w["c_star"] for w in rows])
    ell = np.array([w["ell_ext"] for w in rows])
    spmu = np.array([w["sP"] / w["mu1"] for w in rows])
    minl = np.array([w["minL"] for w in rows])
    overlaps = np.array([w["fail_overlap"] for w in rows if w["minL"] <= 0])
    seat = ("SCHUR-SEATED" if len(overlaps) and float(np.median(overlaps)) >= 0.5
            else "MIXED-SEAT" if len(overlaps) else "NO-FAIL-SEAT")
    labels["seat"] = "%s(med=%.3f)" % (
        seat, float(np.median(overlaps)) if len(overlaps) else float("nan"))
    print("    c_star min/med/max %.6g / %.6g / %.6g"
          % (float(np.min(cstar)), float(np.median(cstar)),
             float(np.max(cstar))))
    print("    ell_ext min/med/max %+.6g / %+.6g / %+.6g"
          % (float(np.min(ell)), float(np.median(ell)),
             float(np.max(ell))))
    print("    s_P/mu1 min/med/max %.6g / %.6g / %.6g"
          % (float(np.min(spmu)), float(np.median(spmu)),
             float(np.max(spmu))))
    print("    min eig(M-P/2) min/med/max %+.6g / %+.6g / %+.6g; "
          "failure e0-overlap median %.4f"
          % (float(np.min(minl)), float(np.median(minl)),
             float(np.max(minl)),
             float(np.median(overlaps)) if len(overlaps) else float("nan")))
    taus = np.array([w["tau"] for w in rows])
    for name, values in (
            ("c_star", cstar),
            ("c_star-1/2", cstar - 0.5),
            ("ell_ext", ell),
            ("sP/mu1", spmu)):
        label, _slope = screen(values, taus)
        print("    TAU-SCREEN %-12s %s" % (name, label))

    section("C -- controls must refuse the certificate")
    for kind in ("smooth", "epstein", "scramble"):
        fired, detail = control_fires(kind)
        check("C %s world refuses" % kind, fired, detail, kill="K2")

    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
