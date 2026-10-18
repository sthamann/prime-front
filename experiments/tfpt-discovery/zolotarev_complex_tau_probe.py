#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zolotarev_complex_tau_probe
PRIME.ONEBADMODE.ZOLOTAREV.TAU.01 +
PRIME.ONEBADMODE.COMPLEXFLOW.01

EXPLORATION ONLY.  NO RH claim.  This probe asks whether CCXXV's one
fixed m=8 Zolotarev certificate really moves the theorem-engineering
target away from a critical real-axis read and onto eight uniformly
off-axis tau reads, or merely hides the same small residue there.

THE FROZEN TRANSLATION.  For the fixed CCXXV filter

  R(x) = 1 + sum_j [a_j/(x-z_j) + a_j/(x-conj(z_j))],

  tr R(M_h) = 8 + 2 Re sum_j a_j tr(M_h-z_j I)^-1,
  tau_h(z) = det(M_h-zI),
  d_z log tau_h(z) = -tr(M_h-zI)^-1.

The certificate path below obtains shifted determinants and inverse
traces from pivoted LU only.  No eigensolver enters a certificate or
reserve decision.  Eigen/SVD reads are confined to explicitly marked
conditioning, c_h-screen and control-typing diagnostics.

QUESTIONS FROZEN BEFORE SMOKE.

T  TRANSLATION WARDS.
   T1 rebuild the complete 68-step CCVII ladder (40 surface + one
      bridge + 27 deep), and rebuild CCXXV's GLOBAL m=8 filter from its
      cited c_B and source-only global L; poles and residues must match
      the stored artifact.
   T2 per rung/pole, LU tau, principal log tau and
      d_z log tau = -tr resolvent must reproduce all 68x8 stored
      determinants/phases/traces.  The partial-fraction expression
      must reproduce both the direct LU trace and the stored reserve.
   T3 the real-axis determinant lemma is warded in the CCVII n-read
      direction E_00: det(M-delta E_00)/det(M) = 1-delta/s, where
      s=n-b^T B^-1 b and delta=SUPPLY_FRACTION*s.

R  THE RESERVE CENSUS -- THE HEADLINE.
   reserve_h := 1-tr R(M_h), on all 68 steps.  Print level, variance,
   segment census and the h-law reserve ~ h^beta with leave-one-out
   2SE.  O1-RESERVE iff every reserve is at least RESERVE_FLOOR, the
   h-law is flat at the standing SLOPE_PASS bar including 2SE, and the
   tau- and c_h-screens are PASS.  Otherwise COLLAPSING, with the scale
   that carries the collapse named.  "Bounded away" is only a statement
   about this finite deployed ladder.

A  PER-POLE ANATOMY.
   A1 q_j(h):=d_z log tau_h(z_j) and its consecutive increments on the
      complete ladder; use the natural dimensionless normalization
      y_j |Delta q_j|/NDIM.  COMPLEX-STABLE means every pole's maximum
      normalized increment is at most INCREMENT_BAR.  Surface and deep
      medians and h-laws are printed separately.
   A2 conditioning: ||(M-iyI)^-1||_2 <= 1/y.  Measure the actual SVD
      norm only as [DIAG] and the safety factor (1/y)/||resolvent||.
   A3 decompose tr R pole by pole through C_j=2a_j Re tr resolvent.
      Report median absolute decision share, leave-one-pole certificate
      necessity count, and h-laws.  A hidden c_h-sized seat requires
      BOTH a c_h-sized median contribution on the matched CCXVII
      surface subset and at least one percent decision share (or a
      nonzero necessity count); scale coincidence alone is not called
      load-bearing.
   A4 compare truth with the five inherited falsifying controls in frozen
      truth coordinates: Q_truth and tau_truth are held fixed while
      the terminating Schur core S_world is substituted.  This is an
      aligned response read, NOT a control-world certificate.  Smooth,
      scramble seed 1, cosh A=.01, mass rescale 1.1 use the full surface
      rung set; Epstein x^2+5y^2 is the inherited single-rung kz=9
      control.  CCXXV already declares its step ladder skipped O(X^2);
      if kz=9 is not a terminating step of the fixed 68-step artifact,
      its complex read is typed STEP-UNAVAILABLE rather than fabricated
      from a different predecessor.  Each control must independently
      fire on its own rung target.  Natural read separation is
      y_j |q_world-q_truth|/NDIM: O1 at >= O1_SEPARATION_BAR, RESOLVED
      at >= RESOLVED_SEPARATION_BAR, otherwise SMALL.

S  THE SENSITIVITY LAW.
   The n-read direction is exactly E_00, inherited from CCVII.
   For A=M-zI and G=A^-1,

     d_n log tau(z) = G_00,
     d_n d_z log tau(z) = (G^2)_00,
     d_n log tau(0) = 1/s.

   Hence the actual derivative sensitivity ratio of the shifted
   log-tau read to the same matrix's z=0 log-tau read is
     rho_j = s |G_00(z_j)| <= s/y_j.
   The finite response uses M -> M-SUPPLY_FRACTION*s E_00 and divides
   |Delta log tau(z_j)| by |log(1-SUPPLY_FRACTION)|.  Also print the
   natural log-derivative move y_j|Delta q_j|/(NDIM|log(1-f)|).
   CCXVII's c_h is NOT s and is never relabelled as s.  On the matched
   surface subset the lead's external critical-currency comparison is
     rho_c,j := c_h |G_00(z_j)| <= c_h/y_j.
   Every rho and finite ratio is screened separately against the
   inherited step tau and against independently recomputed CCXVII c_h.
   COMPLEXFLOW-EASIER iff reserve is O1, reads are COMPLEX-STABLE, and
   no sensitivity screen relocates against tau or c_h.  Otherwise the
   exact relocation seat is printed.

C  CONTROLS / ANTI-CIRCULARITY.
   The filter, poles, residues, ladder and controls are fixed by CCVII,
   CCXXV and CCXXVI; there is no per-rung filter or pole retuning.
   The B-floor/interlacing premise is cited exactly as CCXXV (surface
   certified, deep float, bridge exception) and used for feasibility,
   never for soundness.  The source-only L is rebuilt and warded.
   No zero/prime oracle; RNG only in scramble seed 1.  The CCXVII c_h
   read uses a generalized eigensolver only in a labelled screen
   diagnostic and only on the 40 terminating surface rungs for which
   the level object exists; bridge/deep are honestly outside that
   c_h-screen, while all 68 steps remain in every tau/reserve/LU test.

FROZEN BARS / CONSTANTS.
  NDIM=8; M_FIXED=8; c_B=5523/10000; RESERVE_FLOOR=1e-2;
  SLOPE_PASS=.30; SLOPE_RELOC=.70; INCREMENT_BAR=.50;
  SUPPLY_FRACTION=.10; O1_SEPARATION_BAR=.10;
  RESOLVED_SEPARATION_BAR=1e-3; C_H_SCALE_BAND=[.1,10];
  DECISION_SHARE_FLOOR=.01; LU_TIE=2e-9; FILTER_TIE=2e-10;
  DET_LEMMA_TIE=2e-9; CONDITION_TIE=2e-10; runtime cap 25 min.

VERDICT ENUMS (frozen before smoke):
  reserve: O1-RESERVE / COLLAPSING
  increments: COMPLEX-STABLE / COMPLEX-UNSTABLE
  pole seat: NO-C_H-SIZED-POLE-SEAT / HIDDEN-C_H-POLE-SEAT(j...)
  route: COMPLEXFLOW-EASIER / COMPLEXFLOW-RELOCATION(scale,poles)
The route enum is a finite-ladder theorem-engineering diagnostic, never
an RH statement and never an all-h result.

SMOKE DISCLOSURE.
  SMOKE-1 (SPEC v0, 103.2 s) reached 11/11 checks GREEN: the complete
  68-step ladder rebuilt; fixed poles/residues matched exactly; all
  68x8 LU translations reproduced the stored determinant at 1.68e-14
  relative, phase at 4.44e-16 and trace exactly; partial fractions and
  reserve matched exactly; the z=0 determinant lemma held at 8.44e-15.
  It then stopped before any reserve/anatomy/sensitivity verdict at the
  first c_h diagnostic.  The diagnostic matrix returned by
  gram_from_dens is the odd block (151x151 on that rung), while the
  code requested the parent lag length index (301); scipy correctly
  rejected the out-of-range subset index.
  AMENDMENT A1 (mechanical dimension only): request the final
  generalized eigenvalue using positive.shape[0]-1, the dimension of
  the actual matrices passed to eigh.  No matrix, control, filter,
  pole, coefficient, scale, bar, screen, or verdict rule changed.
  SMOKE-2 (post-A1, 109.2 s) ran 19/19 GREEN with no kills.  The full
  uncensored result was: reserve 2.730e-2/9.195e-1/9.511e-1,
  h^+0.0215 +/- 2SE .0843, PASS against tau (-.027) and c_h (+.070),
  hence O1-RESERVE.  Natural q-increment maxima reached .6807 against
  the predeclared .50 bar, hence COMPLEX-UNSTABLE and the route verdict
  COMPLEXFLOW-RELOCATION(increments); this bar is NOT moved.  Every
  sensitivity screen against tau and c_h passed, no pole relocated,
  rho_j respected s/y at max bound-use .999999999564, and fixed-filter
  dn*/s was .1342/28.02/619.4.  Pole decision shares peaked at j=3
  (.216 median); necessity counts were 28/37/62/68/68/42/8/1; no
  c_h-sized load-bearing pole seat.  Controls fired 42/42, 42/42,
  39/42, 42/42 and 1/1; smooth/scramble/rescale separated O1, cosh
  RESOLVED.  Two reporting defects appeared: unused aligned-control
  determinant products overflowed although the inverse traces were
  finite, and Epstein's absent CCXXV step produced an all-NaN median
  that was incorrectly printed SMALL.
  AMENDMENT A2 (numerical representation only): LU log tau is formed
  as the sum of diagonal log magnitudes plus phases; callers that need
  only q suppress reconstruction of the raw determinant.  Truth tau
  and every identity are unchanged.
  AMENDMENT A3 (typing only): an empty complex-response set is printed
  STEP-UNAVAILABLE, exactly matching CCXXV's inherited O(X^2) Epstein
  step-ladder skip; its 1/1 own-rung control fire remains mandatory.
  No response is invented from a different predecessor.
  SPEC v1 (2026-08-12, frozen after the two disclosed smokes):
  everything above.  No post-freeze numerical amendment is permitted
  without a new disclosed SPEC version.

Run:
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/zolotarev_complex_tau_probe.py --smoke
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/zolotarev_complex_tau_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import euler_phase_identity_probe as eul  # noqa: E402, read-only
import onebadmode_moments_probe as ob  # noqa: E402, read-only CCVII
import zolotarev_phase_filter_probe as zol  # noqa: E402, read-only CCXXV

SMOKE = "--smoke" in sys.argv

NDIM = 8
M_FIXED = 8
CB_CITED = Fraction(5523, 10000)
CB_F = float(CB_CITED)
RESERVE_FLOOR = 1e-2
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
INCREMENT_BAR = 0.50
SUPPLY_FRACTION = 0.10
O1_SEPARATION_BAR = 0.10
RESOLVED_SEPARATION_BAR = 1e-3
CH_SCALE_BAND = (0.1, 10.0)
DECISION_SHARE_FLOOR = 0.01
LU_TIE = 2e-9
FILTER_TIE = 2e-10
DET_LEMMA_TIE = 2e-9
CONDITION_TIE = 2e-10
RSC_FAC = 1.1
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


def ast_scan():
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = set()
    for node in ast.walk(ast.parse(source)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.add(name)
    return sorted(bad)


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


def trio(values):
    values = np.asarray(values, float)
    return (float(np.min(values)), float(np.median(values)),
            float(np.max(values)))


def e3(values):
    return "%.3e/%.3e/%.3e" % trio(values)


def f3(values):
    return "%+.4f/%+.4f/%+.4f" % trio(values)


def ols_line(x_values, y_values):
    x_values = np.asarray(x_values, float)
    y_values = np.asarray(y_values, float)
    variance = float(np.var(x_values))
    if variance == 0.0:
        return float(np.mean(y_values)), 0.0, float("nan")
    slope = float(np.cov(x_values, y_values, bias=True)[0, 1] / variance)
    intercept = float(np.mean(y_values) - slope * np.mean(x_values))
    residual = float(np.sum(
        (y_values - intercept - slope * x_values) ** 2))
    total = float(np.sum((y_values - np.mean(y_values)) ** 2))
    return (intercept, slope,
            1.0 - residual / total if total > 0.0 else float("nan"))


def jack_slope(x_values, y_values):
    x_values = np.asarray(x_values, float)
    y_values = np.asarray(y_values, float)
    _intercept, slope, r2_value = ols_line(x_values, y_values)
    leave_one_out = []
    for index in range(len(x_values)):
        keep = np.ones(len(x_values), bool)
        keep[index] = False
        leave_one_out.append(ols_line(x_values[keep],
                                      y_values[keep])[1])
    leave_one_out = np.asarray(leave_one_out, float)
    error = math.sqrt((len(x_values) - 1) / len(x_values)
                      * float(np.sum((leave_one_out
                                      - leave_one_out.mean()) ** 2)))
    return slope, error, r2_value


def screen(values, scales, label):
    values = np.asarray(values, float)
    scales = np.asarray(scales, float)
    positive = ((values > 0.0) & (scales > 0.0)
                & np.isfinite(values) & np.isfinite(scales))
    if int(np.sum(positive)) < 3:
        return ("%s: VACUOUS(pos=%d)" % (label, int(np.sum(positive))),
                "VAC", float("nan"))
    _intercept, slope, r2_value = ols_line(
        np.log(scales[positive]), np.log(values[positive]))
    verdict = ("PASS" if abs(slope) <= SLOPE_PASS
               else "RELOC" if slope >= SLOPE_RELOC else "AMBIG")
    text = ("%s: %s(slope=%+.3f,R2=%.3f,%d excluded)"
            % (label, verdict, slope, r2_value,
               int(np.sum(~positive))))
    return text, verdict, slope


def wrap(angle):
    return float(math.atan2(math.sin(angle), math.cos(angle)))


def complex_rel(left, right):
    return abs(left - right) / max(1.0, abs(left), abs(right))


def step_key(step):
    return (int(step["r1"]["h"]), int(step["r1"]["kz"]),
            int(step["r2"]["h"]), int(step["r2"]["kz"]))


def row_key(row):
    return (int(row["h1"]), int(row["kz1"]),
            int(row["h"]), int(row["kz"]))


def lu_read(matrix, pole, want_condition=False, want_tau=True):
    """LU-only shifted tau and logarithmic-derivative read.

    The optional 2-norm is an explicitly diagnostic SVD read and does
    not enter tau, q, trace_R, reserve, or any certificate decision.
    """
    shifted = matrix.astype(complex) - pole * np.eye(NDIM, dtype=complex)
    lu_matrix, pivots = sla.lu_factor(shifted)
    inverse = sla.lu_solve(
        (lu_matrix, pivots), np.eye(NDIM, dtype=complex))
    parity = -1.0 if int(np.sum(
        pivots != np.arange(NDIM))) % 2 else 1.0
    diagonal = np.diag(lu_matrix)
    log_abs = float(np.sum(np.log(np.abs(diagonal))))
    phase = float(np.sum(np.angle(diagonal))
                  + (math.pi if parity < 0.0 else 0.0))
    phase = wrap(phase)
    log_tau = complex(log_abs, phase)
    determinant = None
    if want_tau:
        magnitude = math.exp(log_abs)
        determinant = complex(magnitude * math.cos(phase),
                              magnitude * math.sin(phase))
    resolvent_trace = complex(np.trace(inverse))
    q_value = -resolvent_trace
    norm2 = None
    if want_condition:
        singular_values = sla.svdvals(shifted)
        norm2 = 1.0 / float(singular_values[-1])
    return dict(tau=determinant, log_tau=log_tau,
                inverse=inverse, resolvent_trace=resolvent_trace,
                q=q_value, norm2=norm2)


def build_truth_ladder():
    section("W -- complete CCVII ladder, rebuilt read-only")
    zones = ob.ladder_zones()
    check("W1 surface rung census %d == %d"
          % (len(zones), ob.N_RUNGS_EXP),
          len(zones) == ob.N_RUNGS_EXP, kill="PIPELINE")
    surface = [ob.build_rung("surf", kz, with_split=False)
               for kz in zones]
    check("W2 all surface chains complete",
          all(rung is not None for rung in surface), kill="PIPELINE")
    ob.build_ext_tables()
    deep = []
    for kz, expected_h in sorted(ob.deep_zone_census(),
                                 key=lambda pair: (pair[1], pair[0])):
        rung = ob.build_rung("deep", kz, with_split=False)
        if rung is not None:
            deep.append(rung)
        print("    deep kz %-4d h %-5d %s [%.1f s]"
              % (kz, expected_h, "OK" if rung is not None else "SHORT",
                 time.time() - T0), flush=True)
    deep_ok = [rung for rung in deep
               if rung["core_ok"] and rung["negA"] == 0
               and rung.get("lamS", -1.0) > 0.0]
    check("W3 deep truth rung census %d == %d"
          % (len(deep_ok), ob.N_DEEP_EXP),
          len(deep_ok) == ob.N_DEEP_EXP, kill="PIPELINE")
    combined = sorted(
        [rung for rung in surface if rung["core_ok"]] + deep_ok,
        key=lambda rung: (rung["h"], rung["kz"]))
    steps = ob.make_steps(combined)
    for step in steps:
        zol.assemble_step(step)
    steps = [step for step in steps if step["status"] == "OK"]
    segments = [ob.seg_of(step) for step in steps]
    census_ok = (len(steps) == 68 and segments.count("surf") == 40
                 and segments.count("bridge") == 1
                 and segments.count("deep") == 27)
    check("W4 combined steps %d = surface %d + bridge %d + deep %d"
          % (len(steps), segments.count("surf"),
             segments.count("bridge"), segments.count("deep")),
          census_ok, kill="PIPELINE")
    l_sound = sum(step["L_src"] >= float(step["eigs"][-1])
                  for step in steps)
    interlace = min(
        (float(step["eigs"][1]) - step["lamB1"])
        / max(1.0, abs(step["lamB1"])) for step in steps)
    check("W5 CCXXV feasibility wards: source L sound %d/%d; "
          "interlacing worst %+.2e"
          % (l_sound, len(steps), interlace),
          l_sound == len(steps) and interlace >= -zol.ILACE_TOL,
          kill="WARD")
    return zones, steps


def rebuild_filter(steps, artifact):
    global_l = max(step["L_src"] for step in steps)
    filter_data = zol.build_filter(CB_F, global_l, M_FIXED)
    artifact_poles = np.asarray(
        [complex(*pair) for pair in artifact["filter"]["poles"]],
        complex)
    artifact_residues = np.asarray(artifact["filter"]["residues"], float)
    pole_deviation = float(np.max(np.abs(
        filter_data["poles"] - artifact_poles)
        / np.maximum(1.0, np.abs(artifact_poles))))
    residue_deviation = float(np.max(np.abs(
        filter_data["residues"] - artifact_residues)
        / np.maximum(1.0, np.abs(artifact_residues))))
    l_deviation = abs(global_l - float(artifact["filter"]["L"])) \
        / max(1.0, abs(global_l))
    check("T1 fixed CCXXV GLOBAL m=8 filter rebuilt: L rel %.2e, "
          "poles %.2e, residues %.2e <= %.0e"
          % (l_deviation, pole_deviation, residue_deviation,
             FILTER_TIE),
          (artifact["filter"]["m"] == M_FIXED
           and l_deviation <= FILTER_TIE
           and pole_deviation <= FILTER_TIE
           and residue_deviation <= FILTER_TIE),
          kill="WARD")
    return filter_data


def translation_and_reads(steps, artifact, filter_data):
    section("T -- shifted tau translation (LU certificate path)")
    stored = {row_key(row): row for row in artifact["rungs"]}
    max_tau = max_phase = max_trace = max_expression = 0.0
    max_stored_margin = max_det_lemma = 0.0
    rows = []
    for index, step in enumerate(steps):
        source = stored.get(step_key(step))
        if source is None:
            continue
        pole_rows = []
        contributions = []
        for pole_index, (pole, residue) in enumerate(zip(
                filter_data["poles"], filter_data["residues"])):
            read = lu_read(step["Mt"], pole, want_condition=True)
            stored_pole = source["poles"][pole_index]
            stored_tau = complex(*stored_pole["determinant"])
            stored_trace = complex(*stored_pole["resolvent_trace"])
            max_tau = max(max_tau,
                          complex_rel(read["tau"], stored_tau))
            max_phase = max(max_phase, abs(wrap(
                read["log_tau"].imag - stored_pole["phase"])))
            max_trace = max(max_trace, complex_rel(
                read["resolvent_trace"], stored_trace))
            contribution = 2.0 * float(residue) \
                * read["resolvent_trace"].real
            contributions.append(contribution)
            y_value = float(pole.imag)
            condition_safety = (1.0 / y_value) / read["norm2"]
            pole_rows.append(dict(
                j=pole_index, pole=pole, y=y_value,
                residue=float(residue), tau=read["tau"],
                log_tau=read["log_tau"], q=read["q"],
                inverse=read["inverse"], norm2=read["norm2"],
                condition_safety=condition_safety,
                contribution=contribution))
        trace_value = NDIM + math.fsum(contributions)
        reserve = 1.0 - trace_value
        max_expression = max(
            max_expression,
            abs(trace_value - float(source["trace_R"])))
        max_stored_margin = max(
            max_stored_margin,
            abs(reserve - float(source["margin"])))

        gap = float(step["gap"])
        delta = SUPPLY_FRACTION * gap
        perturbed = step["Mt"].copy()
        perturbed[0, 0] -= delta
        sign0, logdet0 = np.linalg.slogdet(step["Mt"])
        sign1, logdet1 = np.linalg.slogdet(perturbed)
        actual_ratio = (sign1 / sign0) * math.exp(logdet1 - logdet0)
        expected_ratio = 1.0 - SUPPLY_FRACTION
        max_det_lemma = max(
            max_det_lemma, abs(actual_ratio - expected_ratio)
            / max(1.0, abs(expected_ratio)))
        rows.append(dict(
            index=index, step=step, source=source,
            segment=ob.seg_of(step), h=float(step["r2"]["h"]),
            kz=int(step["r2"]["kz"]), tau_scale=float(step["tau"]),
            gap=gap, delta_n=delta, trace_R=trace_value,
            reserve=reserve, contributions=contributions,
            poles=pole_rows))
    check("T2 LU tau/log-tau/q reproduces stored 68x8 artifact: "
          "det rel %.2e, phase %.2e, trace rel %.2e <= %.0e"
          % (max_tau, max_phase, max_trace, LU_TIE),
          (len(rows) == 68 and max_tau <= LU_TIE
           and max_phase <= LU_TIE and max_trace <= LU_TIE),
          kill="WARD")
    check("T3 partial fractions reproduce stored trace/reserve: "
          "trace %.2e, reserve %.2e <= %.0e"
          % (max_expression, max_stored_margin, LU_TIE),
          max_expression <= LU_TIE and max_stored_margin <= LU_TIE,
          kill="WARD")
    check("T4 z=0 determinant lemma in n-read direction at "
          "delta=%.2f s: worst rel %.2e <= %.0e"
          % (SUPPLY_FRACTION, max_det_lemma, DET_LEMMA_TIE),
          max_det_lemma <= DET_LEMMA_TIE, kill="WARD")
    print("    translation: tau_h(z)=det(M_h-zI), "
          "d_z log tau_h(z)=-tr(M_h-zI)^-1; LU only.")
    print("    fixed pole y band %.6g .. %.6g; no pole approaches "
          "the real axis." % (filter_data["poles"][0].imag,
                              filter_data["poles"][-1].imag))
    return rows


def c_h_surface_map(rows):
    section("H -- CCXVII c_h diagnostic on matched surface terminators")
    surface_kz = sorted({row["kz"] for row in rows
                         if row["segment"] == "surf"})
    out = {}
    for kz in surface_kz:
        rung = eul.level_rung(kz)
        if rung is None:
            continue
        density = eul.grid_density(rung["c"])
        positive = eul.gram_from_dens(
            np.where(density > 0.0, density, 0.0), rung["M"])
        negative = eul.gram_from_dens(
            np.where(density > 0.0, 0.0, -density), rung["M"])
        final_index = positive.shape[0] - 1
        top = float(sla.eigh(
            negative, positive, eigvals_only=True,
            subset_by_index=[final_index, final_index])[0])
        out[(int(rung["h"]), int(kz))] = 1.0 - top
        print("    c_h diagnostic kz %-4d h %-5d %.4e [%.1f s]"
              % (kz, rung["h"], out[(int(rung["h"]), int(kz))],
                 time.time() - T0), flush=True)
    matched = [row for row in rows
               if (int(row["h"]), row["kz"]) in out]
    values = [out[(int(row["h"]), row["kz"])] for row in matched]
    check("H1 CCXVII c_h matched %d/40 surface steps; band %s lies "
          "inside cited [1.4e-8,1.7e-4] up to 2x reproduction tolerance"
          % (len(matched), e3(values)),
          (len(matched) == 40 and min(values) >= 0.5 * 1.4e-8
           and max(values) <= 2.0 * 1.7e-4),
          kill="WARD")
    print("    HONEST DOMAIN: c_h is a separate level-wall "
          "near-cancellation currency, not the 8x8 Schur margin s.")
    print("    bridge + 27 deep steps remain outside this c_h screen "
          "and inside all 68-step LU/reserve/tau tests.")
    return out


def reserve_census(rows, c_h_map):
    section("R -- THE RESERVE CENSUS")
    reserve = np.asarray([row["reserve"] for row in rows], float)
    h_values = np.asarray([row["h"] for row in rows], float)
    tau_values = np.asarray([row["tau_scale"] for row in rows], float)
    beta, beta_error, beta_r2 = jack_slope(
        np.log(h_values), np.log(reserve))
    variance = float(np.var(reserve))
    coefficient_variation = float(np.std(reserve) / np.mean(reserve))
    print("    reserve = 1-tr R(M_h) level min/med/max %s"
          % e3(reserve))
    print("    mean %.6f variance %.6e coefficient-of-variation %.4f"
          % (float(np.mean(reserve)), variance, coefficient_variation))
    print("    h-law reserve ~ h^%+.4f +/- 2SE %.4f (R2 %.4f)"
          % (beta, 2.0 * beta_error, beta_r2))
    for segment in ("surf", "bridge", "deep"):
        values = [row["reserve"] for row in rows
                  if row["segment"] == segment]
        print("    %-6s n=%2d reserve %s"
              % (segment, len(values), e3(values)))
    tau_text, tau_label, _tau_slope = screen(
        reserve, tau_values, "reserve vs inherited step tau")
    matched = [row for row in rows
               if (int(row["h"]), row["kz"]) in c_h_map]
    ch_values = [c_h_map[(int(row["h"]), row["kz"])]
                 for row in matched]
    ch_text, ch_label, _ch_slope = screen(
        [row["reserve"] for row in matched], ch_values,
        "reserve vs CCXVII c_h (surface 40/68)")
    print("    " + tau_text)
    print("    " + ch_text)
    flat_h = abs(beta) + 2.0 * beta_error <= SLOPE_PASS
    reserve_o1 = (float(np.min(reserve)) >= RESERVE_FLOOR
                  and flat_h and tau_label == "PASS"
                  and ch_label == "PASS")
    reserve_verdict = "O1-RESERVE" if reserve_o1 else "COLLAPSING"
    print("    RESERVE VERDICT: %s(min %.3e, floor %.0e, "
          "h-flat-with-2SE %s, tau %s, c_h %s)"
          % (reserve_verdict, float(np.min(reserve)), RESERVE_FLOOR,
             flat_h, tau_label, ch_label))
    check("R1 reserve census and both relocation screens non-vacuous",
          tau_label != "VAC" and ch_label != "VAC")
    return dict(verdict=reserve_verdict, o1=reserve_o1,
                beta=beta, beta_error=beta_error,
                tau_label=tau_label, ch_label=ch_label,
                reserve=reserve)


def pole_anatomy(rows, c_h_map):
    section("A -- PER-POLE ANATOMY")
    h_values = np.asarray([row["h"] for row in rows], float)
    q_values = np.asarray(
        [[pole["q"] for pole in row["poles"]] for row in rows],
        complex)
    contributions = np.asarray(
        [row["contributions"] for row in rows], float)
    reserves = np.asarray([row["reserve"] for row in rows], float)
    y_values = np.asarray([pole["y"] for pole in rows[0]["poles"]],
                          float)
    increments = np.abs(np.diff(q_values, axis=0))
    normalized_increments = increments * y_values[None, :] / NDIM
    increment_h = np.sqrt(h_values[:-1] * h_values[1:])
    absolute_sum = np.sum(np.abs(contributions), axis=1)
    decision_shares = np.abs(contributions) / absolute_sum[:, None]
    max_normalized = []
    hidden = []
    matched_indices = [
        index for index, row in enumerate(rows)
        if (int(row["h"]), row["kz"]) in c_h_map]
    matched_ch = np.asarray([
        c_h_map[(int(rows[index]["h"]), rows[index]["kz"])]
        for index in matched_indices], float)

    print("    j       y_j   |Dq|nat min/med/max   beta_inc  "
          "cond-safety min/med/max  share_med  necessary  C_j med")
    for pole_index, y_value in enumerate(y_values):
        inc = normalized_increments[:, pole_index]
        beta_inc, _error_inc, _r2_inc = jack_slope(
            np.log(increment_h), np.log(np.maximum(inc, 1e-300)))
        safety = [row["poles"][pole_index]["condition_safety"]
                  for row in rows]
        necessary = int(np.sum(
            reserves + contributions[:, pole_index] <= 0.0))
        share_median = float(np.median(
            decision_shares[:, pole_index]))
        contribution_median = float(np.median(
            np.abs(contributions[:, pole_index])))
        max_normalized.append(float(np.max(inc)))

        matched_contribution = np.abs(
            contributions[matched_indices, pole_index])
        ratio_to_ch = float(np.median(
            matched_contribution / matched_ch))
        ch_sized = CH_SCALE_BAND[0] <= ratio_to_ch <= CH_SCALE_BAND[1]
        load_bearing = (share_median >= DECISION_SHARE_FLOOR
                        or necessary > 0)
        if ch_sized and load_bearing:
            hidden.append(pole_index)
        print("    %-2d %9.3g   %-22s %+8.3f  %-25s %9.3f "
              "%5d/68 %10.3e"
              % (pole_index, y_value, e3(inc), beta_inc,
                 e3(safety), share_median, necessary,
                 contribution_median))
        print("       segments: normalized |Dq| surface med %.3e, "
              "deep med %.3e; median |C_j|/c_h %.3e%s"
              % (float(np.median([
                    normalized_increments[index - 1, pole_index]
                    for index in range(1, len(rows))
                    if rows[index]["segment"] == "surf"])),
                 float(np.median([
                    normalized_increments[index - 1, pole_index]
                    for index in range(1, len(rows))
                    if rows[index]["segment"] == "deep"])),
                 ratio_to_ch,
                 " [scale match but non-load-bearing]"
                 if ch_sized and not load_bearing else ""))
    condition_worst = min(
        pole["condition_safety"] for row in rows for pole in row["poles"])
    check("A1 resolvent condition bound ||(M-iyI)^-1||2 <= 1/y: "
          "minimum safety %.12f >= 1-%.0e on 68x8 [DIAG SVD]"
          % (condition_worst, CONDITION_TIE),
          condition_worst >= 1.0 - CONDITION_TIE, kill="WARD")
    stable = max(max_normalized) <= INCREMENT_BAR
    stability_verdict = ("COMPLEX-STABLE" if stable
                         else "COMPLEX-UNSTABLE")
    seat_verdict = ("NO-C_H-SIZED-POLE-SEAT" if not hidden
                    else "HIDDEN-C_H-POLE-SEAT(%s)"
                    % ",".join(str(value) for value in hidden))
    dominant = int(np.argmax(np.median(decision_shares, axis=0)))
    necessary_counts = [
        int(np.sum(reserves + contributions[:, index] <= 0.0))
        for index in range(NDIM)]
    print("    wall-decision location: dominant median absolute share "
          "pole j=%d (%.3f); leave-one-pole necessity counts %s"
          % (dominant,
             float(np.median(decision_shares[:, dominant])),
             "/".join(str(value) for value in necessary_counts)))
    print("    STABILITY VERDICT: %s(max natural increment %.3e, bar %.2f)"
          % (stability_verdict, max(max_normalized), INCREMENT_BAR))
    print("    POLE-SEAT VERDICT: %s" % seat_verdict)
    return dict(stable=stable, stability=stability_verdict,
                seat=seat_verdict, hidden=hidden,
                y_values=y_values, q_values=q_values,
                contributions=contributions,
                decision_shares=decision_shares)


def control_rungs(zones):
    def cosh_injection(rung):
        times = np.arange(rung["M"]) * rung["D"]
        return (ob.INJ_A * np.cos(ob.INJ_GAMMA0 * times)
                * (np.cosh(ob.INJ_DELTA * times) - 1.0))

    worlds = {
        "smooth": [ob.build_rung("surf", kz, world="smooth")
                   for kz in zones],
        "scramble": [ob.build_rung("surf", kz,
                                   scramble_seed=ob.SCR_SEED)
                     for kz in zones],
        "cosh": [ob.build_rung("surf", kz, lag_fn=cosh_injection)
                 for kz in zones],
    }
    rescale = []
    for kz in zones:
        source = ob.window_of(kz)
        rescale.append(ob.build_rung(
            "surf", kz,
            comb=(source["uu"].copy(),
                  RSC_FAC * 2.0 * source["lam"].copy())))
    worlds["rescale"] = rescale

    source9 = ob.window_of(ob.CTRL_KZ)
    epstein_n = int(math.floor(math.exp(
        2.0 * source9["alpha"]))) + 1
    epstein_lambda = ob.lambda_eps(epstein_n)
    epstein_indices = np.nonzero(
        np.abs(epstein_lambda) > 1e-12)[0]
    epstein = ob.build_rung(
        "surf", ob.CTRL_KZ,
        comb=(np.log(epstein_indices.astype(float)),
              2.0 * epstein_lambda[epstein_indices]
              / np.sqrt(epstein_indices.astype(float))))
    worlds["epstein"] = [epstein]
    return worlds


def control_comparison(rows, zones):
    section("C -- truth versus five controls at the fixed poles")
    worlds = control_rungs(zones)
    maps = {
        name: {int(rung["kz"]): rung for rung in ladder
               if isinstance(rung, dict)}
        for name, ladder in worlds.items()
    }
    fire = {}
    for name, ladder in worlds.items():
        count = sum(
            rung is None or (isinstance(rung, dict)
                             and rung["negA"] > 0)
            for rung in ladder)
        fire[name] = count
        print("    %-9s own-rung wall target fires %d/%d"
              % (name, count, len(ladder)))
    check("C1 all five inherited controls fire on their own rung "
          "target: %s"
          % ", ".join("%s=%d" % (name, fire[name])
                      for name in ("smooth", "scramble", "cosh",
                                   "rescale", "epstein")),
          all(fire[name] > 0 for name in worlds), kill="WARD")

    truth_by_kz = {
        row["kz"]: row for row in rows if row["segment"] == "surf"}
    print("    aligned-response convention: fixed Q_truth, tau_truth; "
          "replace terminating S_truth by S_world.")
    labels = {}
    for name in ("smooth", "scramble", "cosh", "rescale", "epstein"):
        response_by_pole = [[] for _ in range(NDIM)]
        comparable = 0
        for kz, control in maps[name].items():
            truth = truth_by_kz.get(kz)
            if truth is None or not control.get("core_ok"):
                continue
            matrix = sym(truth["step"]["Q"].T
                         @ (control["S"] / truth["tau_scale"])
                         @ truth["step"]["Q"])
            comparable += 1
            for pole_index, truth_pole in enumerate(truth["poles"]):
                read = lu_read(matrix, truth_pole["pole"],
                               want_tau=False)
                separation = (truth_pole["y"] / NDIM
                              * abs(read["q"] - truth_pole["q"]))
                response_by_pole[pole_index].append(separation)
        medians = np.asarray([
            float(np.median(values)) if values else float("nan")
            for values in response_by_pole], float)
        if comparable == 0:
            best = float("nan")
            label = "STEP-UNAVAILABLE"
        else:
            best = float(np.nanmax(medians))
            label = ("O1" if best >= O1_SEPARATION_BAR
                     else "RESOLVED"
                     if best >= RESOLVED_SEPARATION_BAR else "SMALL")
        labels[name] = label
        print("    %-9s comparable %2d; natural separation per pole "
              "medians %s; best %.3e -> %s"
              % (name, comparable,
                 "/".join("%.2e" % value for value in medians),
                 best, label))
    check("C2 aligned pole responses computed for four full controls; "
          "Epstein typed %s under inherited CCXXV O(X^2) step skip"
          % labels["epstein"],
          (all(labels[name] in ("O1", "RESOLVED", "SMALL")
               for name in ("smooth", "scramble", "cosh", "rescale"))
           and labels["epstein"] == "STEP-UNAVAILABLE"))
    return labels


def sensitivity_law(rows, c_h_map):
    section("S -- n-read sensitivity: z=0 versus eight complex reads")
    finite_denominator = abs(math.log(1.0 - SUPPLY_FRACTION))
    derivative_ratios = np.zeros((len(rows), NDIM))
    finite_ratios = np.zeros((len(rows), NDIM))
    qmove_ratios = np.zeros((len(rows), NDIM))
    bound_fractions = np.zeros((len(rows), NDIM))
    critical_ratios = np.full((len(rows), NDIM), np.nan)
    filter_dn_ratios = []
    max_gradient_tie = 0.0

    for row_index, row in enumerate(rows):
        gradient_terms = []
        perturbed = row["step"]["Mt"].copy()
        perturbed[0, 0] -= row["delta_n"]
        ch_key = (int(row["h"]), row["kz"])
        for pole_index, pole_row in enumerate(row["poles"]):
            inverse = pole_row["inverse"]
            inverse_square_00 = complex((inverse @ inverse)[0, 0])
            gradient_terms.append(
                -2.0 * pole_row["residue"]
                * inverse_square_00.real)
            ratio = row["gap"] * abs(complex(inverse[0, 0]))
            derivative_ratios[row_index, pole_index] = ratio
            expected_bound = row["gap"] / pole_row["y"]
            bound_fractions[row_index, pole_index] = (
                ratio / expected_bound)

            perturbed_read = lu_read(
                perturbed, pole_row["pole"], want_tau=False)
            delta_log = complex(
                perturbed_read["log_tau"].real
                - pole_row["log_tau"].real,
                wrap(perturbed_read["log_tau"].imag
                     - pole_row["log_tau"].imag))
            finite_ratios[row_index, pole_index] = (
                abs(delta_log) / finite_denominator)
            qmove_ratios[row_index, pole_index] = (
                pole_row["y"] / NDIM
                * abs(perturbed_read["q"] - pole_row["q"])
                / finite_denominator)
            if ch_key in c_h_map:
                critical_ratios[row_index, pole_index] = (
                    c_h_map[ch_key]
                    * abs(complex(inverse[0, 0])))

        gradient = math.fsum(gradient_terms)
        parent_trace, parent_gradient = zol.trace_filter_lu(
            row["step"]["Mt"],
            dict(residues=np.asarray([
                pole["residue"] for pole in row["poles"]], float),
                 poles=np.asarray([
                     pole["pole"] for pole in row["poles"]], complex)),
            want_gradient=True)
        max_gradient_tie = max(
            max_gradient_tie, abs(gradient - parent_gradient),
            abs(parent_trace - row["trace_R"]))
        dn_star = (row["reserve"] / abs(gradient)
                   if gradient != 0.0 else float("inf"))
        filter_dn_ratios.append(dn_star / row["gap"])
    check("S1 analytic n-gradients reproduce CCXXV fixed-filter "
          "gradient/trace route: max abs %.2e <= %.0e"
          % (max_gradient_tie, LU_TIE),
          max_gradient_tie <= LU_TIE, kill="WARD")

    matched_mask = np.asarray([
        (int(row["h"]), row["kz"]) in c_h_map for row in rows], bool)
    tau_values = np.asarray([row["tau_scale"] for row in rows], float)
    ch_values = np.asarray([
        c_h_map[(int(row["h"]), row["kz"])]
        for row in rows if (int(row["h"]), row["kz"]) in c_h_map],
        float)
    relocation = []
    print("    j      y_j  rho=s|G00| min/med/max  finite min/med/max  "
          "bound-use max  tau/c_h screens")
    for pole_index in range(NDIM):
        tau_text, tau_label, _tau_slope = screen(
            derivative_ratios[:, pole_index], tau_values,
            "rho_%d vs tau" % pole_index)
        ch_text, ch_label, _ch_slope = screen(
            derivative_ratios[matched_mask, pole_index], ch_values,
            "rho_%d vs c_h" % pole_index)
        finite_tau_text, finite_tau_label, _ = screen(
            finite_ratios[:, pole_index], tau_values,
            "finite_%d vs tau" % pole_index)
        finite_ch_text, finite_ch_label, _ = screen(
            finite_ratios[matched_mask, pole_index], ch_values,
            "finite_%d vs c_h" % pole_index)
        labels = (tau_label, ch_label,
                  finite_tau_label, finite_ch_label)
        if "RELOC" in labels:
            relocation.append(pole_index)
        print("    %-2d %9.3g  %-24s %-21s %12.3e  "
              "rho %s/%s finite %s/%s"
              % (pole_index, rows[0]["poles"][pole_index]["y"],
                 e3(derivative_ratios[:, pole_index]),
                 e3(finite_ratios[:, pole_index]),
                 float(np.max(bound_fractions[:, pole_index])),
                 tau_label, ch_label,
                 finite_tau_label, finite_ch_label))
        print("       external critical currency rho_c=c_h|G00| "
              "%s; natural q-move %s"
              % (e3(critical_ratios[matched_mask, pole_index]),
                 e3(qmove_ratios[:, pole_index])))
        print("       " + tau_text + " | " + ch_text)
        print("       " + finite_tau_text + " | " + finite_ch_text)

    print("    fixed-filter n tolerance dn*/s min/med/max %s "
          "(CCXXV direction; no c_h-sized residual required)"
          % e3(filter_dn_ratios))
    check("S2 off-axis derivative bound rho_j <= s/y_j: "
          "max bound use %.12f <= 1+%.0e"
          % (float(np.max(bound_fractions)), CONDITION_TIE),
          float(np.max(bound_fractions)) <= 1.0 + CONDITION_TIE,
          kill="WARD")
    check("S3 all reserve/sensitivity tau and c_h screens computed",
          np.all(np.isfinite(critical_ratios[matched_mask])))
    return dict(relocation=relocation,
                derivative_ratios=derivative_ratios,
                finite_ratios=finite_ratios,
                qmove_ratios=qmove_ratios,
                filter_dn_ratios=np.asarray(filter_dn_ratios))


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(ok for _name, ok in CHECKS)
    if KILLS:
        verdict = ("PIPELINE-BROKEN" if KILLS[0] == "PIPELINE"
                   else "WARD-BROKEN")
    else:
        verdict = " / ".join(labels)
    print("  VERDICT: " + verdict)
    print("  HONEST FRAME: finite float64 deployed ladder only; fixed "
          "CCXXV m=8 pole family; surface c_B cited, deep float, bridge "
          "exception; c_h diagnostic on 40 surface terminators only; "
          "no all-h result and NO RH claim.")
    print("  [TIME] %.1f s  [CHECKS] %d/%d PASS  [KILLS] %s"
          % (time.time() - T0, passed, len(CHECKS),
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if passed == len(CHECKS) and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.ZOLOTAREV.TAU.01 + "
            "PRIME.ONEBADMODE.COMPLEXFLOW.01")
    print("    SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; EXPLORATION ONLY; NO RH claim"
          % ("SMOKE" if SMOKE else "FROZEN"))
    bad = ast_scan()
    check("S0 AST firewall clean", not bad,
          ",".join(bad) if bad else "", kill="WARD")
    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    check("S0b CCXXV artifact schema and dimensions fixed",
          (artifact["schema"] == "tfpt.zolotarev_phase_filter.v1"
           and len(artifact["rungs"]) == 68
           and artifact["filter"]["m"] == M_FIXED),
          kill="PIPELINE")
    zones, steps = build_truth_ladder()
    if KILLS:
        return finish([])
    filter_data = rebuild_filter(steps, artifact)
    rows = translation_and_reads(steps, artifact, filter_data)
    if KILLS:
        return finish([])
    c_h_map = c_h_surface_map(rows)
    reserve = reserve_census(rows, c_h_map)
    anatomy = pole_anatomy(rows, c_h_map)
    controls = control_comparison(rows, zones)
    sensitivity = sensitivity_law(rows, c_h_map)

    if (reserve["o1"] and anatomy["stable"]
            and not sensitivity["relocation"]):
        route = "COMPLEXFLOW-EASIER"
    else:
        seats = []
        if not reserve["o1"]:
            seats.append("reserve")
        if not anatomy["stable"]:
            seats.append("increments")
        if sensitivity["relocation"]:
            seats.append("sensitivity-poles-%s"
                         % ",".join(str(value)
                                    for value
                                    in sensitivity["relocation"]))
        route = "COMPLEXFLOW-RELOCATION(%s)" % ",".join(seats)
    labels = [
        reserve["verdict"],
        anatomy["stability"],
        anatomy["seat"],
        "CONTROLS(%s)" % ",".join(
            "%s:%s" % (name, controls[name])
            for name in ("smooth", "scramble", "cosh",
                         "rescale", "epstein")),
        "SENSITIVITY(dn*/s %s; relocation poles %s)"
        % (e3(sensitivity["filter_dn_ratios"]),
           ",".join(str(value)
                    for value in sensitivity["relocation"]) or "none"),
        route,
    ]
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
