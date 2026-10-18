#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""directional_floor_density_probe --
PRIME.PORT.DIRECTIONAL.FLOOR.DENSITY.01
(EXPLORATION ONLY, experiments/; round 64, 2026-08-11).

THEORY FIRST.  On the fixed Schur end-form

    M = [[n,b*],[b,B]],       q = b* B^{-1} b,

let nu_b be the directional spectral measure of B:

    nu_b = sum_i |<u_i,b>|^2 delta_{lambda_i},  B u_i=lambda_i u_i.

Then q = int lambda^{-1} dnu_b.  The v905 certificate gives a
source-constructed floor

    B >= D := P_G/2 + c_dom I >= c_B I,
    c_B := c_G/2 + c_dom > 0.

The floor-only estimate q <= ||b||^2/c_B is known to be about 91x
too large.  The genuinely additional datum proposed here is
QUADRATIC DEPLETION of the directional mass near that certified
floor.  With

    lambda_R := (b* B b)/||b||^2,
    t_delta := c_B + delta (lambda_R-c_B),
    F(delta) := nu_b([c_B,t_delta]) / ||b||^2,

the frozen candidate is

    F(delta) <= C_DENS delta^2,   C_DENS=4,
    delta in {1/64,1/32,1/16,1/8,1/4,1/2}.

This is a density statement, not a pointwise prime assertion.  If it
holds at a delta, spectral splitting gives the rigorous implication

  q <= ||b||^2 [ f/c_B + (1-f)/t_delta ],
  f = min(1,C_DENS delta^2).

The minimum over the frozen delta grid is the proposed inverse bound.
If it also obeys n-q_bound >= mu1/2, the density statement is
quantitatively competent for the registered half-gap on this surface.

WHY BETA=2 / C=4 ARE FROZEN: beta=2 is the second-order/exterior-area
candidate suggested by the h^-2 margin and wedge-square mechanism;
4 is a one-dyadic-cell safety factor.  Neither is fit to this ladder.
No constant adjustment is allowed after the run.  Failure is final
for this candidate.

FROZEN PROTOCOL:
 W  reproduce the parent 42/41/39 ladder and v901 minB/gap.
 F  rebuild c_G and c_dom by the v905 exact-rational LDL/bisection
    class; certify c_B>0 and c_B<=lambda_min(B) on all 39.
 D1 materialize nu_b only for MEASUREMENT: weights nonnegative,
    mass/first moment/inverse moment agree with direct source reads
    to MOM_WARD=1e-10.  Also reconstruct moments m_j=b*B^j b for
    j=0..13; their spectral agreement is the high-moment ward.
 D2 test the frozen quadratic density inequality at every grid point
    and report C_emp=max F/delta^2 per rung and globally.
 D3 evaluate the conditional q_bound and half-gap closure census.
    Mandatory tau screen of a positive certificate margin; a slope
    >=+0.70 is relocation, |slope|<=0.30 pass, else ambiguous.
 C  smooth/Epstein/scramble must refuse the prerequisite or density
    certificate exactly as in the parent battery.

ANTI-CIRCULARITY.  The construction of c_B, lambda_R, thresholds,
and q_bound uses B through matrix products and exact LDL decisions,
but no target eigenvalue/eigenvector, q, sigma_h, or wall sign.
Eigendecomposition is used only to score the proposed density
statement and moment wards.  A future proof must establish D2 without
spectral target data.

ANTHROPIC NO-GO DECLARATION.  D2 explicitly uses information beyond
two moments plus bandwidth-1 pair correlation: a family of spectral
projector masses, equivalently (on this fixed 7-dimensional block)
the directional moments through degree 13 / the full Krylov measure.
The two-moment no-go is not contradicted.  The price is explicit:
proving the projector inequality uniformly in h is the named gap.

NO POINTWISE PRIME STATEMENT, no endpoint envelope, no transition-only
barrier.  The object is a state-level directional spectral measure.

SPEC v1 (2026-08-11, frozen before first run): C_DENS=4 exactly,
beta=2, DELTAS as above, BIS_ITERS inherited from v905, screen bands
.30/.70, no smoke run.  Parent exterior SPEC SHA is warded.

NO RH claim.  A surface pass would only identify a competent theorem
shape; it would not prove D2 for all h or enclose the ideal pipeline.
No marker moves.  Stdout only.
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

import exterior_pg_schur_probe as parent  # noqa: E402 (READ-ONLY)
import bfloor_pg_dominance_probe as base  # noqa: E402 (READ-ONLY)

PARENT_SPEC_SHA = "084c968964f0ab6e0e852b29c75c210e324bcf63106d68583048910992d92da4"
C_DENS = Fraction(4, 1)
DELTAS = (Fraction(1, 64), Fraction(1, 32), Fraction(1, 16),
          Fraction(1, 8), Fraction(1, 4), Fraction(1, 2))
MOM_WARD = 1.0e-10
FLOOR_WARD = 1.0e-10
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
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


def exact_floor_components(B, PG):
    """The v905 exact-rational chain, with each float treated as its
    exact dyadic rational and every final lower endpoint re-decided."""
    Bfr = base.mat_fr(B)
    PGfr = base.mat_fr(PG)
    half_pg = [[Fraction(float(0.5 * PG[i, j]))
                for j in range(7)] for i in range(7)]
    remainder = [[Bfr[i][j] - half_pg[i][j] for j in range(7)]
                 for i in range(7)]
    if not base.pd_exact(PGfr)[0] or not base.pd_exact(remainder)[0]:
        return None
    c_g = base.cert_floor_exact(
        PGfr, Fraction(0), min(PGfr[i][i] for i in range(7)))
    c_dom = base.cert_floor_exact(
        remainder, Fraction(0), min(remainder[i][i] for i in range(7)))
    if c_g is None or c_dom is None:
        return None
    return c_g, c_dom, HALF * c_g + c_dom


HALF = Fraction(1, 2)


def ols_screen(values, taus):
    values = np.asarray(values, float)
    taus = np.asarray(taus, float)
    mask = np.isfinite(values) & (values > 0.0) & (taus > 0.0)
    if int(np.sum(mask)) < 3:
        return "VACUOUS(n=%d)" % int(np.sum(mask)), float("nan")
    slope, r2 = parent.ols_line(np.log(taus[mask]), np.log(values[mask]))
    label = ("PASS" if abs(slope) <= SLOPE_PASS
             else "RELOCATION" if slope >= SLOPE_RELOC else "AMBIG")
    return "%s(slope=%+.3f,R2=%.3f,n=%d)" % (
        label, slope, r2, int(np.sum(mask))), slope


def measure_row(row):
    B = row["B"]
    b = row["b"]
    norm2 = float(b @ b)
    eig, vectors = np.linalg.eigh(B)
    weights = (vectors.T @ b) ** 2
    probs = weights / norm2
    lambda_r = float(b @ (B @ b)) / norm2
    q_direct = float(b @ np.linalg.solve(B, b))
    q_spectral = float(np.sum(weights / eig))

    floor_parts = exact_floor_components(B, row["PG"])
    if floor_parts is None:
        return None
    c_g, c_dom, c_b = floor_parts
    c_bf = float(c_b)

    direct_moments = []
    spectral_moments = []
    vector = b.copy()
    for degree in range(14):
        direct_moments.append(float(b @ vector))
        spectral_moments.append(float(np.sum(weights * eig ** degree)))
        vector = B @ vector
    moment_dev = max(
        abs(a - z) / max(abs(a), abs(z), 1.0)
        for a, z in zip(direct_moments, spectral_moments))

    mass_dev = abs(float(np.sum(weights)) - norm2) / max(norm2, 1.0)
    first_dev = abs(float(np.sum(weights * eig)) - norm2 * lambda_r) \
        / max(abs(norm2 * lambda_r), 1.0)
    inverse_dev = abs(q_spectral - q_direct) / max(abs(q_direct), 1.0)

    density = []
    c_emp = 0.0
    for delta_fr in DELTAS:
        delta = float(delta_fr)
        threshold = c_bf + delta * (lambda_r - c_bf)
        f_actual = float(np.sum(probs[eig <= threshold]))
        f_model = min(1.0, float(C_DENS * delta_fr * delta_fr))
        holds = f_actual <= f_model + 1.0e-15
        c_emp = max(c_emp, f_actual / (delta * delta))
        q_bound = norm2 * (
            f_model / c_bf + (1.0 - f_model) / threshold)
        density.append(dict(delta=delta, threshold=threshold,
                            f=f_actual, f_model=f_model, holds=holds,
                            q_bound=q_bound))
    best = min(density, key=lambda item: item["q_bound"])
    margin_bound = row["n"] - best["q_bound"] - 0.5 * row["mu1"]
    margin_true = row["gap"] - 0.5 * row["mu1"]
    return dict(row=row, eig=eig, weights=weights, probs=probs,
                norm2=norm2, lambda_r=lambda_r, q_direct=q_direct,
                q_spectral=q_spectral, c_g=c_g, c_dom=c_dom, c_b=c_b,
                c_bf=c_bf, moment_dev=moment_dev, mass_dev=mass_dev,
                first_dev=first_dev, inverse_dev=inverse_dev,
                density=density, c_emp=c_emp, best=best,
                margin_bound=margin_bound, margin_true=margin_true)


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _name, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
    else:
        verdict = ("DIRFLOORDENS-MEASURED / %s / %s / %s / %s"
                   % (labels["density"], labels["bound"],
                      labels["screen"], labels["controls"]))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: spectral eigendata scored the density hypothesis but
  did not construct it.  A numerical pass would still require an
  all-h proof from the degree-13 directional moments/CD structure and
  ideal-object interval enclosure.  A failure kills C=4,beta=2.
  NO RH claim; no marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.DIRECTIONAL.FLOOR.DENSITY.01 -- directional "
            "mass depletion near the certified B-floor")
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
    parent_sha = hashlib.sha256(parent.__doc__.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % spec_sha)
    print("    parent SPEC SHA-256 = %s" % parent_sha)
    print("    C_DENS=4, beta=2, deltas=%s; NO ADJUSTMENT; NO RH claim."
          % ([float(d) for d in DELTAS],))
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent frozen spec reproduced",
          parent_sha == PARENT_SPEC_SHA, kill="K2")

    section("W/F -- ladder reproduction and exact certified floors")
    zones, _truth, full, rows = parent.build_truth_rows()
    check("W1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41 and len(rows) == 39,
          "%d/%d/%d" % (len(zones), len(full), len(rows)), kill="K1")
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
    measured = [measure_row(row) for row in rows]
    check("F1 exact v905 floor chain available",
          all(item is not None for item in measured),
          "%d/%d" % (sum(item is not None for item in measured), len(rows)),
          kill="K2")
    if any(item is None for item in measured):
        return finish(dict(density="-", bound="-", screen="-", controls="-"))
    floor_ok = all(
        item["c_bf"] > 0.0
        and item["c_bf"] <= float(item["eig"][0]) + FLOOR_WARD
        for item in measured)
    check("F2 c_B positive and below measured floor",
          floor_ok,
          "c_B min/med %.4f/%.4f; survival min %.6f"
          % (min(item["c_bf"] for item in measured),
             float(np.median([item["c_bf"] for item in measured])),
             min(float(item["eig"][0]) - item["c_bf"]
                 for item in measured)), kill="K2")

    section("D1 -- directional measure and degree-13 moment wards")
    max_mass = max(item["mass_dev"] for item in measured)
    max_first = max(item["first_dev"] for item in measured)
    max_inverse = max(item["inverse_dev"] for item in measured)
    max_moment = max(item["moment_dev"] for item in measured)
    check("D1 mass/first/inverse spectral identities",
          max(max_mass, max_first, max_inverse) <= MOM_WARD,
          "max dev mass %.2e first %.2e inverse %.2e"
          % (max_mass, max_first, max_inverse), kill="K2")
    check("D1b moments degree 0..13 agree",
          max_moment <= MOM_WARD,
          "max relative deviation %.2e" % max_moment, kill="K2")

    section("D2 -- frozen quadratic density statement")
    density_pass = [
        all(point["holds"] for point in item["density"])
        for item in measured
    ]
    fail_rows = [
        (item["row"]["r2"]["kz"], item["row"]["r2"]["h"],
         [(point["delta"], point["f"], point["f_model"])
          for point in item["density"] if not point["holds"]])
        for item, ok in zip(measured, density_pass) if not ok
    ]
    c_emp = np.array([item["c_emp"] for item in measured])
    print("    F(delta)<=4 delta^2: %d/%d rungs; failures:"
          % (sum(density_pass), len(density_pass)))
    for failure in fail_rows:
        print("      kz=%d h=%d %s" % failure)
    print("    C_emp=max_delta F/delta^2 min/med/max "
          "%.4f / %.4f / %.4f"
          % (float(np.min(c_emp)), float(np.median(c_emp)),
             float(np.max(c_emp))))
    print("    aggregate F(delta) max vs frozen model:")
    for index, delta_fr in enumerate(DELTAS):
        fmax = max(item["density"][index]["f"] for item in measured)
        model = measured[0]["density"][index]["f_model"]
        print("      delta=%7.5f Fmax=%.6f model=%.6f"
              % (float(delta_fr), fmax, model))

    section("D3 -- conditional inverse bound and half-gap competence")
    bound_close = [item["margin_bound"] >= 0.0 for item in measured]
    q_ratios = np.array(
        [item["best"]["q_bound"] / item["q_direct"] for item in measured])
    floor_ratios = np.array(
        [(item["norm2"] / item["c_bf"]) / item["q_direct"]
         for item in measured])
    best_deltas = [item["best"]["delta"] for item in measured]
    margins = np.array([item["margin_bound"] for item in measured])
    print("    best frozen-density q_bound/q true min/med/max "
          "%.3f / %.3f / %.3f"
          % (float(np.min(q_ratios)), float(np.median(q_ratios)),
             float(np.max(q_ratios))))
    print("    floor-only qbar/q true min/med/max %.3f / %.3f / %.3f"
          % (float(np.min(floor_ratios)), float(np.median(floor_ratios)),
             float(np.max(floor_ratios))))
    unique_delta, counts = np.unique(best_deltas, return_counts=True)
    print("    chosen delta census %s"
          % dict(zip([float(x) for x in unique_delta],
                     [int(x) for x in counts])))
    print("    conditional half-gap bound closes %d/%d; margin min/med/max "
          "%+.4g / %+.4g / %+.4g"
          % (sum(bound_close), len(bound_close), float(np.min(margins)),
             float(np.median(margins)), float(np.max(margins))))
    taus = np.array([item["row"]["tau"] for item in measured])
    screen_label, _slope = ols_screen(margins, taus)
    print("    TAU-SCREEN conditional margin: %s" % screen_label)

    section("C -- controls")
    controls = []
    for kind in ("smooth", "epstein", "scramble"):
        fired, detail = parent.control_fires(kind)
        check("C %s world refuses" % kind, fired, detail, kill="K2")
        controls.append("%s:%s" % (kind, "FIRE" if fired else "SILENT"))

    all_density = all(density_pass)
    all_bound = all(bound_close)
    labels = {
        "density": ("QDENS-PASS(39/39)" if all_density else
                    "QDENS-FAIL(%d/39)" % sum(density_pass)),
        "bound": ("QBOUND-CLOSES(39/39)" if all_density and all_bound else
                  "QBOUND-INSUFFICIENT(%d/39)" % sum(bound_close)),
        "screen": "SCREEN(%s)" % screen_label,
        "controls": "CONTROLS(" + ",".join(controls) + ")",
    }
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
