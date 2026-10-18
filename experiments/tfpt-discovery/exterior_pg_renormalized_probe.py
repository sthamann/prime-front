#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""exterior_pg_renormalized_probe --
PRIME.PORT.EXTERIOR.PG.RENORMALIZED.01
(EXPLORATION ONLY, experiments/; round 64 iteration, 2026-08-11).

WHY THIS ITERATION EXISTS.  exterior_pg_schur_probe (SPEC v1, run
before this file was written) established two facts on the 39-step
surface:

  * the CD-Gram exterior quotient s_P is exact to 7.77e-16 and
    s_P >= mu1 on 39/39, with s_P/mu1 = 2.26e3..7.82e4;
  * the unscaled Loewner lemma M >= P/2 fails on 13/39, all failures
    Schur-seated (median e0 overlap 0.9959).

Thus the positive exterior object survives, but its natural size is
far too large.  This frozen iteration tests the unique geometric
renormalization that makes its Schur pivot equal the target geometry:

    rho_h := mu1(h) / s_P(h) > 0,       Pbar_h := rho_h P_h,
    s(Pbar_h) = rho_h s_P(h) = mu1(h)       EXACTLY.

rho is source-only: mu1 is parity geometry and s_P is the positive
CD-Gram exterior quotient.  It uses no target margin, target
eigenvalue, or target eigendata.  The coefficient 1/2 is unchanged.

THE CANDIDATE CERTIFICATE:

    R := M - Pbar/2 >= 0
      ==> s(M) >= s(Pbar/2) = mu1/2.

The implication is exact by Loewner inversion.  But success on the
finite surface is NOT enough.  The decisive anti-relocation test is
the exact Schur-addition ledger.  Put A=Pbar/2 and R=M-A.  If their
co-blocks A_B,R_B are PD, then

  s(M) - mu1/2 = s(R) + J,
  J = (z_A-z_R)^T (A_B^{-1}+R_B^{-1})^{-1} (z_A-z_R) >= 0,
  z_A=A_B^{-1}a, z_R=R_B^{-1}r.

This is the exact superadditivity defect of the Schur complement.  If
s(R) is merely the original half-gap margin with negligible J, then
R>=0 is the wall relocated.  If J carries a substantial, independently
positive part and s(R) has an O(1) reserve, the exterior normalization
has created new certificate currency.

FROZEN PROTOCOL:
 W  import and reproduce the first probe's 42/41/39 ladder, v901
    minB/gap, exact P/P_G positivity, and exterior identity.
 E1 verify rho>0 and s(Pbar)=mu1 by Schur, determinant, and inverse
    routes to ID_WARD=1e-8.
 E2 exact-rational LDL census R>0 and co-block R_B>0.  A surface
    pass is typed RENORM-SURFACE-PASS, never proof.
 E3 exact Schur-addition identity on every R-pass; report s(R),
    J, J/(target margin), s(R)/(target margin), and the mandatory
    tau screens in BOTH normalized and raw coordinates.  Raw means
    multiplication by tau(r1), explicitly exposing any normalization
    relocation.  RELOCATION is declared if either (i) raw s(R) has
    log-log slope >=0.70 versus tau, or (ii) median s(R)/halfmargin
    >=0.90 (the new remainder is >=90 percent the target itself).
    PASS bands otherwise use |slope|<=0.30.
 C  smooth/Epstein/scramble controls must refuse as upstream.

ANTI-CIRCULARITY: rho depends only on the source CD exterior quotient
and mu1.  Target M enters only the exact LDL decision and anatomy.

ANTHROPIC NO-GO: as in the parent, the input is the full degree-h CD
evaluation matrix and an exterior quotient, not two scalar moments.

SPEC v1 (2026-08-11, frozen before the first run): all constants and
rules above.  Parent SPEC SHA is reproduced at runtime.  No smoke run.

NO RH claim.  Even a 39/39 pass can be classified as relocation and
therefore mathematical non-progress.  No marker moves.  Stdout only.
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

import exterior_pg_schur_probe as parent  # noqa: E402 (READ-ONLY)

PARENT_SPEC_SHA = "084c968964f0ab6e0e852b29c75c210e324bcf63106d68583048910992d92da4"
ID_WARD = 1.0e-8
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
RELOC_SHARE = 0.90
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


def screen(values, taus):
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


def schur(matrix):
    return (float(matrix[0, 0])
            - float(matrix[1:, 0]
                    @ np.linalg.solve(matrix[1:, 1:], matrix[1:, 0])))


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _name, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
    else:
        verdict = ("EXTERIORPGRENORM-MEASURED / %s / %s / %s"
                   % (labels["surface"], labels["currency"],
                      labels["controls"]))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: rho is canonical and source-only, but a source-only
  normalization can still hide the target in the residual order
  statement.  The Schur-addition and raw-coordinate screens decide
  that issue explicitly.  No all-h result and NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.EXTERIOR.PG.RENORMALIZED.01 -- canonical "
            "exterior-pivot normalization (EXPLORATION ONLY)")
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
    parent_sha = hashlib.sha256(parent.__doc__.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % spec_sha)
    print("    parent SPEC SHA-256 = %s" % parent_sha)
    print("    NO RH claim; coefficient 1/2 unchanged.")
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent frozen spec reproduced",
          parent_sha == PARENT_SPEC_SHA, kill="K2")

    section("W -- parent ladder and exterior reproduction")
    zones, truth, full, rows = parent.build_truth_rows()
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
    max_ext = max(
        abs(w["sP"] - w["sP_projection"]) / max(abs(w["sP"]), 1.0e-300)
        for w in rows)
    check("W3 parent exterior identity and exact P positivity",
          max_ext <= ID_WARD and all(parent.exact_pd(w["P"]) for w in rows),
          "max dev %.2e" % max_ext, kill="K2")

    section("E1 -- canonical renormalization s(Pbar)=mu1")
    renorm = []
    id_devs = []
    for w in rows:
        rho = w["mu1"] / w["sP"]
        Pbar = rho * w["P"]
        A = 0.5 * Pbar
        R = w["M"] - A
        RB = R[1:, 1:]
        sPbar = schur(Pbar)
        signP, logP = np.linalg.slogdet(Pbar)
        signPG, logPG = np.linalg.slogdet(Pbar[1:, 1:])
        sdet = (math.exp(logP - logPG)
                if signP > 0.0 and signPG > 0.0 else float("nan"))
        sinv = 1.0 / float(np.linalg.inv(Pbar)[0, 0])
        scale = max(w["mu1"], 1.0e-300)
        id_devs.extend([abs(sPbar - w["mu1"]) / scale,
                        abs(sdet - w["mu1"]) / scale,
                        abs(sinv - w["mu1"]) / scale])
        row = dict(w=w, rho=rho, Pbar=Pbar, A=A, R=R, RB=RB,
                   sPbar=sPbar)
        renorm.append(row)
    check("E1 three-route s(Pbar)=mu1 identity",
          max(id_devs) <= ID_WARD,
          "max relative deviation %.2e; rho range %.3e..%.3e"
          % (max(id_devs), min(r["rho"] for r in renorm),
             max(r["rho"] for r in renorm)), kill="K2")

    section("E2 -- exact-rational residual Loewner census")
    rb_pd = [parent.exact_pd(r["RB"]) for r in renorm]
    r_pd = [parent.exact_pd(r["R"]) for r in renorm]
    fail = [(r["w"]["r2"]["kz"], r["w"]["r2"]["h"])
            for r, ok in zip(renorm, r_pd) if not ok]
    print("    residual co-block exact-PD %d/%d"
          % (sum(rb_pd), len(rb_pd)))
    print("    full residual exact-PD %d/%d; failures %s"
          % (sum(r_pd), len(r_pd), fail))
    surface_pass = all(rb_pd) and all(r_pd)

    section("E3 -- exact Schur-addition ledger and relocation screens")
    identity_devs = []
    sR_values = []
    j_values = []
    target_values = []
    shares = []
    for r, okb in zip(renorm, rb_pd):
        w = r["w"]
        target = w["gap"] - 0.5 * w["mu1"]
        target_values.append(target)
        if not okb:
            sR_values.append(float("nan"))
            j_values.append(float("nan"))
            shares.append(float("nan"))
            continue
        A = r["A"]
        R = r["R"]
        AB = A[1:, 1:]
        RB = R[1:, 1:]
        za = np.linalg.solve(AB, A[1:, 0])
        zr = np.linalg.solve(RB, R[1:, 0])
        parallel = np.linalg.inv(np.linalg.inv(AB) + np.linalg.inv(RB))
        dz = za - zr
        J = float(dz @ parallel @ dz)
        sR = schur(R)
        identity_devs.append(
            abs(target - sR - J) / max(abs(target), abs(sR), abs(J),
                                       1.0e-300))
        sR_values.append(sR)
        j_values.append(J)
        shares.append(sR / target)
    check("E3.1 exact Schur-addition identity",
          max(identity_devs) <= ID_WARD,
          "max relative deviation %.2e" % max(identity_devs), kill="K2")
    sR_values = np.array(sR_values)
    j_values = np.array(j_values)
    target_values = np.array(target_values)
    shares = np.array(shares)
    finite = np.isfinite(shares)
    med_share = float(np.median(shares[finite]))
    med_j = float(np.median(j_values[finite] / target_values[finite]))
    print("    target half-margin min/med/max %.6g / %.6g / %.6g"
          % (float(np.min(target_values)), float(np.median(target_values)),
             float(np.max(target_values))))
    print("    s(R)/target min/med/max %.6f / %.6f / %.6f"
          % (float(np.min(shares[finite])), med_share,
             float(np.max(shares[finite]))))
    print("    J/target min/med/max %.6f / %.6f / %.6f"
          % (float(np.min(j_values[finite] / target_values[finite])),
             med_j,
             float(np.max(j_values[finite] / target_values[finite]))))
    taus = np.array([r["w"]["tau"] for r in renorm])
    normalized_screen, normalized_slope = screen(sR_values, taus)
    raw_screen, raw_slope = screen(sR_values * taus, taus)
    target_screen, _ = screen(target_values, taus)
    print("    TAU-SCREEN s(R) normalized: %s" % normalized_screen)
    print("    TAU-SCREEN tau*s(R) raw:    %s" % raw_screen)
    print("    TAU-SCREEN target margin:   %s" % target_screen)
    relocation = (raw_slope >= SLOPE_RELOC or med_share >= RELOC_SHARE)
    currency = ("RENORM-RELOCATION(raw=%+.3f,share=%.3f)"
                % (raw_slope, med_share) if relocation else
                "RENORM-CURRENCY-SURVIVES(raw=%+.3f,share=%.3f)"
                % (raw_slope, med_share))

    section("C -- controls")
    control_labels = []
    for kind in ("smooth", "epstein", "scramble"):
        fired, detail = parent.control_fires(kind)
        check("C %s world refuses" % kind, fired, detail, kill="K2")
        control_labels.append("%s:%s" % (kind, "FIRE" if fired else "SILENT"))

    labels = {
        "surface": ("RENORM-SURFACE-PASS(39/39)" if surface_pass else
                    "RENORM-SURFACE-REFUSED(%d/39)" % sum(r_pd)),
        "currency": currency,
        "controls": "CONTROLS(" + ",".join(control_labels) + ")",
    }
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
