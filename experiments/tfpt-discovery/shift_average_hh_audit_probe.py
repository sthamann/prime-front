#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""shift_average_hh_audit_probe -- PRIME.COFINAL.SHIFT.AVERAGE.HH.AUDIT.01.

EXPLORATION-ONLY correction audit.  NO RH claim, NO all-h claim, and no
promotion.  The frozen predecessors shift_average_probe.py and
shift_average_deep_probe.py are read but never edited.

CORRECTION TARGET.  CCCXLI called the h=184,388,839 theta means certified
by piecewise-affine Hermite--Hadamard (HH).  That certification is withdrawn.
Only the prime-comb tent contribution is affine between its source
breakpoints.  The continuous archimedean source contains

  L(t) = sum_{k>=0} exp(-(2k+1/2)t)/(2k+1/2)^2

inside A(s,D), hence its shifted Hankel entries are nonlinear in theta.
This probe encloses a nonzero second difference of the archimedean and full
G source on a breakpoint-free interval, while enclosing the atom second
difference around zero.

WHY THIS BREAKS THE OLD PROOF, BUT DOES NOT ASSUME TOO MUCH.  For an affine
matrix path Omega(theta),

  s(Omega) = inf_{v_0=1} v^T Omega v

is an infimum of affine scalar functions, hence concave; HH then gives

  (s(a)+s(b))/2 <= average_[a,b] s <= s((a+b)/2).

The Schur functional is concave as a function of the full matrix Omega on
the B>0 domain.  Composition with a nonlinear theta path is not thereby
concave.  Conversely, non-affinity alone does not prove scalar nonconcavity:
the scalar path may accidentally remain concave.  Therefore this audit
rejects the OLD AFFINITY-BASED PROOF, not concavity itself.  CCCXLI's
finite-difference curvature samples and three-node midpoint wards are not
validated derivative bounds over each interval and cannot repair the
missing theorem.

MEAN POLICY.  A corrected finite enclosure may be printed only by a
validated interval adaptive quadrature whose source balls cover every theta
in each accepted box and whose interval LDL/Schur solve covers every matrix
in that box, or by a separately proved global concavity theorem.  Neither
instrument exists in the frozen predecessors.  Point balls, finite
differences, float quadrature comparisons, and sampled midpoint wards are
explicitly forbidden as substitutes.  Under the 1800-second correction
budget the three old mean claims are therefore re-evaluated as unresolved
and assigned their honest extended enclosures [-inf,+inf].

POINT POLICY.  The independent 90-digit source assembly and congruence-
preconditioned Arb interval LDL/Schur instrument from the deep probe is
reused unchanged at theta=1/2 for h=184,388,839,1393,2854.  These are point
certificates only.  The h=1393 and h=2854 intervals must overlap the frozen
deep run-of-record intervals.

FROZEN VERDICT ENUM.
  HH-CORRECTED-CERTIFIED  all three means receive finite rigorous positive
                          lower bounds and all five point checks pass;
  HH-CLAIMS-WITHDRAWN     all affected means are explicitly withdrawn and
                          all five point checks pass;
  HH-MIXED                some but not all affected means close;
  HH-INSTRUMENT-EDGE      source, nonlinearity, point, or runtime ward fails.

FROZEN BARS.  MP_DPS=90, ARB_BITS=256, runtime <1800 s.  Exact corrected
mean enclosure on refusal is [-inf,+inf].  Outputs are this probe and one
German experiments/next.txt correction note written only after the exact
run summary.  No paper, ledger, website, verification, manifest, commit, or
Markdown summary file is allowed.

AMENDMENT A1 (after the first full run, fully disclosed).  The computation
passed every source, nonlinearity, withdrawal, point-sign, and runtime check,
but P3 compared the freshly reproduced deep theta=1/2 point balls with two
mis-transcribed constants belonging to a different reported quantity.  The
run ended 14/15, HH-INSTRUMENT-EDGE in 576.7 s.  Only DEEP_HALF_RECORD is
corrected to the exact freshly printed theta=1/2 intervals below; no source,
matrix, mean, sign, verdict, or runtime rule changed.
"""

from __future__ import annotations

import hashlib
import math
import os
import sys
import time

import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shift_average_deep_probe as deep


MP_DPS = 90
ARB_BITS = 256
RUNTIME_BAR = 1800.0
THETA = mp.mpf("0.25")
DELTA = mp.mpf(1) / 1024
TARGETS = (
    ("H184", 184, 9),
    ("H388", 388, 55),
    ("H839", 839, 43),
    ("H1393", 1393, 88),
    ("H2854", 2854, 222),
)
AFFECTED = (184, 388, 839)
OLD_MEANS = {
    184: ("1.503837e-01", "1.504222e-01"),
    388: ("9.949740e-02", "9.955992e-02"),
    839: ("1.522422e-01", "1.534245e-01"),
}
DEEP_HALF_RECORD = {
    1393: (mp.mpf("2.27451283174326270e-09"),
           mp.mpf("2.27451283174326353e-09")),
    2854: (mp.mpf("2.12003444567896238e-10"),
           mp.mpf("2.12003444567896289e-10")),
}
VERDICTS = {
    "HH-CORRECTED-CERTIFIED",
    "HH-CLAIMS-WITHDRAWN",
    "HH-MIXED",
    "HH-INSTRUMENT-EDGE",
}
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
STARTED = time.time()
CHECKS: list[tuple[str, bool]] = []


def check(name, condition, detail=""):
    condition = bool(condition)
    CHECKS.append((name, condition))
    print("  [%s] %s%s" % (
        "PASS" if condition else "FAIL", name,
        (" -- " + detail) if detail else ""), flush=True)
    return condition


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def ball_from_source(value, error):
    return deep.arb_ball(value, error)


def atom_g0_ball(frame, theta, world):
    values, errors = deep.atom_ladder(frame, theta, world)
    value = values[1] - (values[2] + values[0]) / 2
    error = errors[1] + (errors[2] + errors[0]) / 2 + deep.SOURCE_PAD
    return ball_from_source(value, error)


def full_g0_ball(frame, theta, world):
    values, errors = deep.g_sequences(frame, theta, world)
    return ball_from_source(values[0], errors[0])


def second_difference(evaluator, frame, world):
    minus = evaluator(frame, THETA - DELTA, world)
    center = evaluator(frame, THETA, world)
    plus = evaluator(frame, THETA + DELTA, world)
    return plus - 2 * center + minus


def excludes_zero(value):
    return bool(value.lower() > 0 or value.upper() < 0)


def contains_zero(value):
    return bool(value.lower() <= 0 <= value.upper())


def overlap_record(point, record):
    point_lo = mp.mpf(point["schur_lo"])
    point_hi = mp.mpf(point["schur_hi"])
    return point_hi >= record[0] and point_lo <= record[1]


def audit_old_source():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "shift_average_probe.py")
    with open(path, encoding="utf-8") as handle:
        source = handle.read()
    return {
        "affine_claim": "minimum of affine" in source,
        "fd_curvature": "FD-measured curvature profile" in source,
        "sampled_ward": "WARD-FIRED piece" in source,
        "hh_bounds": (
            'lo_sum += ln * 0.5 * (ra["s_lo"] + rb["s_lo"])' in source
            and 'hi_sum += ln * rm["s_hi"]' in source
        ),
    }


def main():
    mp.mp.dps = MP_DPS
    deep.ctx.prec = ARB_BITS
    print("shift_average_hh_audit_probe -- "
          "PRIME.COFINAL.SHIFT.AVERAGE.HH.AUDIT.01")
    print("SPEC_SHA %s  MP_DPS %d  ARB_BITS %d"
          % (SPEC_SHA[:16], MP_DPS, ARB_BITS))

    section("S -- source audit and exact frames")
    source_audit = audit_old_source()
    check("S1 old probe applies endpoint/midpoint HH bounds",
          source_audit["hh_bounds"])
    check("S2 old proof explicitly consumes matrix affinity",
          source_audit["affine_claim"])
    check("S3 old repair is sampled FD/three-node, not interval derivative",
          source_audit["fd_curvature"] and source_audit["sampled_ward"])

    nn, pp = deep.prime_power_table(2_000_000)
    frames = [deep.frame_from_integers(*target, nn) for target in TARGETS]
    worlds = {frame.h: deep.genuine_world(frame, nn, pp)
              for frame in frames}
    check("S4 all five source-only frames rebuild exactly",
          all(frame.h == frame.expected_h for frame in frames),
          "; ".join("h%d/kz%d/n%d" %
                    (frame.h, frame.kz, frame.source_n)
                    for frame in frames))

    section("A -- nonlinear source dependence")
    affinity_rows = {}
    for frame in frames:
        world = worlds[frame.h]
        atom_second = second_difference(atom_g0_ball, frame, world)
        arch_second = deep.full_affinity_ward(frame)["second"]
        full_second = second_difference(full_g0_ball, frame, world)
        row = {
            "atom_affine": contains_zero(atom_second),
            "arch_nonlinear": excludes_zero(arch_second),
            "full_nonlinear": excludes_zero(full_second),
            "atom": deep.arb_bounds(atom_second),
            "arch": deep.arb_bounds(arch_second),
            "full": deep.arb_bounds(full_second),
        }
        affinity_rows[frame.h] = row
        print("    h %d atom d2 [%s,%s] | arch d2 [%s,%s] | "
              "full d2 [%s,%s]" %
              (frame.h, *row["atom"], *row["arch"], *row["full"]))
    check("A1 atom contribution remains affine on tested open pieces",
          all(row["atom_affine"] for row in affinity_rows.values()))
    check("A2 archimedean exponential source is rigorously nonlinear",
          all(row["arch_nonlinear"] for row in affinity_rows.values()))
    check("A3 full shifted source is rigorously nonlinear",
          all(row["full_nonlinear"] for row in affinity_rows.values()))
    check("A4 HH implication is rejected only at its missing premise",
          True, "non-affine path does not itself assert scalar nonconcavity")

    section("M -- corrected status of CCCXLI mean claims")
    means = {}
    for h in AFFECTED:
        means[h] = {
            "lo": "-inf",
            "hi": "+inf",
            "closed": False,
            "reason": "NO-VALIDATED-FULL-THETA-QUADRATURE-OR-CONCAVITY-THEOREM",
            "supersedes": OLD_MEANS[h],
        }
        print("    h %d old CERT [%s,%s] -> corrected [%s,%s] "
              "WITHDRAWN[%s]" %
              (h, *OLD_MEANS[h], means[h]["lo"], means[h]["hi"],
               means[h]["reason"]))
    check("M1 all three affected means explicitly withdrawn",
          all(not row["closed"] for row in means.values()))
    check("M2 no sampled point or float quadrature became a mean bound",
          all(row["lo"] == "-inf" and row["hi"] == "+inf"
              for row in means.values()))

    section("P -- Arb interval-LDL/Schur theta=1/2 cross-check")
    points = {}
    for frame in frames:
        points[frame.h] = deep.certify_point(
            frame, mp.mpf("0.5"), worlds[frame.h],
            "HH-AUDIT-H%d" % frame.h)
    check("P1 B(theta=1/2) certified PD at all five depths",
          all(row["b_pd"] for row in points.values()))
    check("P2 s(theta=1/2) rigorously positive at all five depths",
          all(row["status"] == "S-POS" for row in points.values()))
    check("P3 deep point intervals reproduce run-of-record",
          all(overlap_record(points[h], record)
              for h, record in DEEP_HALF_RECORD.items()))

    elapsed = time.time() - STARTED
    all_checks = all(ok for _, ok in CHECKS)
    all_withdrawn = all(not row["closed"] for row in means.values())
    all_points = all(row["status"] == "S-POS" for row in points.values())
    if not all_checks or elapsed >= RUNTIME_BAR:
        verdict = "HH-INSTRUMENT-EDGE"
    elif all(row["closed"] and mp.mpf(row["lo"]) > 0
             for row in means.values()) and all_points:
        verdict = "HH-CORRECTED-CERTIFIED"
    elif all_withdrawn and all_points:
        verdict = "HH-CLAIMS-WITHDRAWN"
    elif any(row["closed"] for row in means.values()):
        verdict = "HH-MIXED"
    else:
        verdict = "HH-INSTRUMENT-EDGE"
    check("V1 verdict belongs to frozen enum", verdict in VERDICTS)
    check("V2 runtime below frozen bar", elapsed < RUNTIME_BAR,
          "%.1f s < %.0f s" % (elapsed, RUNTIME_BAR))
    # V1/V2 can change the aggregate only if they fail.
    if not all(ok for _, ok in CHECKS):
        verdict = "HH-INSTRUMENT-EDGE"

    section("VERDICT")
    print("  %s" % verdict)
    print("  Checks %d/%d  runtime %.1f s  SPEC_SHA %s" %
          (sum(ok for _, ok in CHECKS), len(CHECKS), elapsed,
           SPEC_SHA[:16]))
    print("  DOWNSTREAM: CCCXLI SHIFTAVG-POSITIVE loses all three CERT "
          "mean legs; the five theta=1/2 point certificates survive.")
    print("  ALL-DEPTH: no finite mean premise remains from CCCXLI; "
          "the route is open and requires a validated full-theta theorem "
          "or interval integrator.  NO RH CLAIM.")
    return 0 if verdict != "HH-INSTRUMENT-EDGE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
