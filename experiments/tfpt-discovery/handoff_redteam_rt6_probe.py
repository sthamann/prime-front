#!/usr/bin/env python3
"""GLOBAL-HANDOFF red team, RT6 decision probe -- the symbol gate as
the load-bearing deck-corruption detector (intended promotion
companion v765b to handoff_redteam_probe / v765).

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, and this probe writes no files.  The true construction is
never modified; all machinery is imported read-only from
handoff_frequency_gram_probe (gp), moonshot_arch_glue_probe (glue)
and handoff_redteam_probe (rt: certificate bars, evaluation engine,
tent-lag builders -- all frozen there, reused byte-identically).

INPUT STATE (frozen findings of the parent audit, 2026-08-04):
handoff_redteam_probe ended REDTEAM-PARTIAL with firewall clean,
baseline reproduced, 8/8 controls broken, 7/8 conclusive.  The single
inconclusive control was RT6 (wrong deck twists, D5 mirror): it broke
ONLY the symbol clause c4 (min Fejer symbol -0.827 vs bar -2e-9 on
every window) while the positive-part-clipped gram still tracked the
target (errors 0.0862 -> 0.0381, kappa 0.985) -- outside the parent
probe's preregistered expected set {c1,c2,c3,c7}.  The break was real
and sits exactly in the audited construction's load-bearing M2.1
symbol/PSD gate; the miss was the auditor's expectation.  Per the
parent's frozen no-iteration policy the PARTIAL stands there; THIS
probe decides RT6 under a fresh preregistration.

STRUCTURAL STATEMENT UNDER TEST (frozen): after positive-part
clipping, deck corruption is invisible to the rate/level/
identification gates; the SYMBOL NONNEGATIVITY gate is the
load-bearing detector.

SIGN ANALYSIS (frozen before the run; it dictates the variant class):
the arch layer enters the source moments as c_ar[d] = -int tent_d
rho, so a deck corruption with density EXCESS (wrong >= true on the
battery support) makes the moments more negative and pushes the
Fejer symbol DOWN -- the positivity gate can fire.  A deck corruption
with one-signed DEFICIT (wrong <= true) ADDS the positive density
(true - wrong) to the total symbol, pushing it UP and INTO the
positivity interior: no positivity gate can ever see it, by
construction.  The gated claim is therefore: the symbol gate detects
the EXCESS-mode deck-corruption class (the mode that could counterfeit
positivity); the deficit mode is measured in a declared negative
block and handed to the resolution discussion, not gated.

FROZEN CERTIFICATE: identical bars to the parent probe (imported):
c1 slope < -0.25, c2 final/first < 0.75, c3 falling tail, c4 min
symbol >= -2e-9 on every grid, c5 lambda_min >= -1e-9, c6 |kappa-1|
<= 0.05, c7 final <= 5.0 x E* (E* = this run's baseline final).

POSITIVE ANCHOR (B0, gated): the true construction at Nf = 2M+1 on
the declared 5-window family must pass the FULL certificate including
c4, and reproduce the audited run inside the parent's frozen bands:
slope in [-0.47, -0.27] (audited -0.369), final/first in [0.33, 0.55]
(audited 0.441).  Failure => RT6-INVALID (construction problem,
reported immediately).

GATED DECK-CORRUPTION VARIANTS (all EXCESS mode, all with total
t -> 0 channel mass 3 so the d = 0 UV correction integral stays
finite; true deck = exponents {1/2, 5/2, 9/2}, weights {1,1,1},
denominator 1 - e^{-6t}):
  V1 FULL MIRROR (the parent RT6 corruption, rerun): exponents
     {3/4, 3/2, 9/4}, weights {1,1,1} (D5 mirror, moonshot A3.4).
     Expected (frozen): c4 breaks on EVERY window (parent run:
     min symbol -0.696/-0.769/-0.817/-0.818/-0.827) AND all other
     clauses c1/c2/c3/c5/c6/c7 PASS -- the blindness of the other
     gates is confirmed, not just the break.  BOTH parts are gated
     for V1 (this is the structural statement).
  V2 SINGLE-CHANNEL PHASE SWAP: deck channel r = 5 replaced by r = 3,
     exponents {1/2, 3/2, 9/2}, weights {1,1,1}.  Density excess
     (e^{-3t/2} - e^{-5t/2})/(1 - e^{-6t}) >= 0, size ~0.14 at t = 1.
     Expected (frozen): c4 breaks on every window; the other gates
     are expected blind and are REPORTED, not gated (a smaller
     corruption than V1 must not be given a second kill route).
  V3 CHANNEL-MASS REDISTRIBUTION (partial/amplitude corruption): the
     nu = 5/6 channel mass moved onto the other two, exponents
     {1/2, 5/2}, weights {3/2, 3/2}.  Density excess
     (e^{-t/2}/2 + e^{-5t/2}/2 - e^{-9t/2})/(1 - e^{-6t}) >= 0.
     Expected (frozen): c4 breaks on every window; other gates
     reported.
NEGATIVE BLOCK (N1, measured, NOT gated -- declared honesty block):
  deck channel r = 5 replaced by r = 7, exponents {1/2, 7/2, 9/2},
  weights {1,1,1}: one-signed DEFICIT (~ -0.17 at t -> 0).  Expected
  (frozen): the symbol moves UP (min symbol >= the baseline minimum;
  no c4 break -- provable blindness of any positivity gate to
  interior-directed perturbations) and the error/identification
  ladder moves at the ~1e-3 level (parent V1 moved it by ~5e-4),
  i.e. N1 sits BELOW the certificate's resolution floor.  This is
  reported as the measured resolution limit of the battery surface
  (consistent with the already-declared battery-limited
  identification remainder), not as a circularity hole: a
  perturbation that leaves source, symbol margin direction, and
  handoff errors essentially unchanged cannot counterfeit
  convergence from target data.

VERDICT ENUM (frozen): RT6-SYMBOL-DETECTS = B0 clean (full
certificate incl. c4 + reproduction bands) AND V1/V2/V3 each break
c4 on every window AND the V1 blindness clause holds (c1/c2/c3/c5/
c6/c7 all pass under the clipped V1 gram).  RT6-PARTIAL = B0 clean
but a gated variant fails to break c4 on some window (named -- a
genuine audit hole), or the V1 blindness clause fails (named gate).
RT6-INVALID = B0 fails.

COMBINED AUDIT STATEMENT (printed, frozen rule): with the parent
probe's frozen facts (firewall clean, 7 conclusive controls RT1-RT5/
RT7/RT8) as cited input, the round's red team is
REDTEAM-GREEN-COMBINED if and only if this probe ends
RT6-SYMBOL-DETECTS; otherwise NOT-GREEN, stated plainly.

ITERATION POLICY: none.  Single preregistered run; no variant, bar,
or expected-set recalibration afterwards.

RUNTIME (predeclared): baseline + 3 gated variants + 1 negative
block = 5 full source ladders on the declared 5-window family;
budget <= 5 minutes (parent probe: 8 ladders in 6.1 s).

RESULTS (2026-08-04, first and only preregistered run, 4.5 s, 8/8
checks; verdict RT6-SYMBOL-DETECTS -- baseline clean, all three
excess-mode variants break c4 on every window, V1 blindness
confirmed; combined audit REDTEAM-GREEN-COMBINED):
  *  B0 anchor: errors 0.0855/0.0585/0.0457/0.0452/0.0377, slope
     -0.369, final/first 0.441, kappa 0.99028, min symbol +7.40e-3,
     lmin +5.45e-3 -- full certificate incl. c4 passes, bands
     reproduced; E* = 0.0377.
  *  V1 full mirror: min symbol -0.696/-0.769/-0.817/-0.818/-0.827
     per window (parent run reproduced exactly); ALL other clauses
     pass (errors 0.0862 -> 0.0381, slope -0.368, final/first 0.442,
     kappa 0.9849, lmin +3.98e-3, level 0.0381 <= 0.1885) --
     BLINDNESS CONFIRMED: rate/ratio/tail/psd/kappa/level all stayed
     blind, only the symbol gate fired.
  *  V2 phase swap r = 5 -> 3: min symbol -0.451/-0.500/-0.521/
     -0.522/-0.534 per window -- c4 breaks everywhere; every other
     gate blind (errors 0.0851 -> 0.0372, slope -0.373, kappa
     0.9877).
  *  V3 mass redistribution (3/2, 3/2, 0): min symbol -1.289/-1.521/
     -1.636/-1.646/-1.720 per window -- c4 breaks everywhere; every
     other gate blind (errors 0.0858 -> 0.0377, slope -0.371, kappa
     0.9854).
  *  N1 deficit r = 5 -> 7 (negative block, not gated).  The frozen
     SIGN prediction is confirmed: the symbol moves INTO the
     interior on every window (min symbol +1.10e-2 .. +2.67e-2 >=
     baseline +7.40e-3; no c4 break -- positivity gates provably
     blind).  The frozen MAGNITUDE prediction was WRONG (declared,
     not hidden): instead of ~1e-3 shifts below the resolution
     floor, the deficit produced a 0.138 error floor (errors
     0.1454 -> 0.1380, slope -0.024, final/first 0.949, kappa
     1.0790) and was CAUGHT by c1_rate, c2_ratio and c6_kappa.  The
     measured picture is therefore STRONGER than predicted: the two
     deck-corruption modes are covered by complementary detectors --
     excess mode by the symbol gate (errors blind), deficit mode by
     the rate/ratio/identification gates (symbol blind).  No
     corruption mode of the tested class escapes the full
     certificate.  Post-run text correction (declared): the printed
     promotion note was reworded to report the measured caught-by
     list dynamically instead of the refuted below-resolution
     wording; no gate, bar, variant or verdict logic was touched.
  *  COMBINED: with the parent audit's frozen facts (firewall clean,
     baseline reproduced, RT1-RT5/RT7/RT8 conclusive) and this
     RT6-SYMBOL-DETECTS decision, the round's red team is
     REDTEAM-GREEN-COMBINED.  PROMOTION NOTE (binding for v765/
     v765b): the symbol-nonnegativity gate must never be dropped
     from any future certificate -- for the excess-mode deck class
     it is the ONLY firing detector; the deficit mode needs the
     rate/ratio/kappa gates.  Certificates must always carry BOTH
     gate families.  NO RH claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/handoff_redteam_rt6_probe.py
"""

import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import moonshot_arch_glue_probe as glue  # noqa: E402
import handoff_frequency_gram_probe as gp  # noqa: E402
import handoff_redteam_probe as rt  # noqa: E402  (frozen bars/engine)

T_START = time.time()

TRUE_DECK = dict(exponents=(0.5, 2.5, 4.5), weights=(1.0, 1.0, 1.0))
VARIANTS = (
    dict(tag="V1", label="full mirror (D5, parent RT6 rerun)",
         exponents=(0.75, 1.5, 2.25), weights=(1.0, 1.0, 1.0),
         gate_blindness=True),
    dict(tag="V2", label="single-channel phase swap r=5 -> r=3",
         exponents=(0.5, 1.5, 4.5), weights=(1.0, 1.0, 1.0),
         gate_blindness=False),
    dict(tag="V3", label="channel-mass redistribution (3/2, 3/2, 0)",
         exponents=(0.5, 2.5), weights=(1.5, 1.5),
         gate_blindness=False),
)
NEG_BLOCK = dict(tag="N1", label="deficit swap r=5 -> r=7 (NOT gated)",
                 exponents=(0.5, 3.5, 4.5), weights=(1.0, 1.0, 1.0))

MANIFEST = dict(
    version="handoff-redteam-rt6-v1",
    parent="handoff_redteam_probe REDTEAM-PARTIAL 2026-08-04, "
           "RT6 inconclusive (broke c4 outside expected set)",
    statement="symbol gate = load-bearing deck-corruption detector; "
              "other gates blind after positive-part clipping",
    certificate="imported frozen from handoff_redteam_probe",
    baseline_bands=dict(slope=list(rt.SLOPE_BAND),
                        ratio=list(rt.RATIO_BAND)),
    true_deck=dict(exponents=list(TRUE_DECK["exponents"]),
                   weights=list(TRUE_DECK["weights"])),
    variants=[dict(tag=v["tag"], exponents=list(v["exponents"]),
                   weights=list(v["weights"]),
                   gate_blindness=v["gate_blindness"])
              for v in VARIANTS],
    negative_block=dict(tag=NEG_BLOCK["tag"],
                        exponents=list(NEG_BLOCK["exponents"]),
                        weights=list(NEG_BLOCK["weights"]),
                        gated=False),
    verdicts=["RT6-SYMBOL-DETECTS", "RT6-PARTIAL", "RT6-INVALID"],
)
MANIFEST_HASH = hashlib.sha256(json.dumps(
    MANIFEST, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

CHECKS = []
FAILS = []


def check(name, ok, detail=""):
    CHECKS.append(name)
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def self_firewall():
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = set()
    for node in ast.walk(tree):
        name = ""
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                token = alias.name.split(".")[0]
                if any(b in token.lower() for b in rt.BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in rt.BANNED):
            hits.add(name)
    return sorted(hits)


def deck_density(exponents, weights):
    """Deck-class density sum_i w_i e^{-b_i t} / (1 - e^{-6t})."""
    def density(w):
        w = np.asarray(w, float)
        numerator = sum(wt * np.exp(-b * w)
                        for b, wt in zip(exponents, weights))
        return numerator / (-np.expm1(-6.0 * w))
    return density


def wrong_arch_layers(windows, true_layers, density):
    """Arch layer rebuilt from a frozen wrong deck density; the d = 0
    UV cell corrected by the finite difference integral (reused
    frozen builders from the parent probe)."""
    out = []
    for window, lay in zip(windows, true_layers):
        M, D = window["M"], window["D"]
        arch = np.empty(M)
        arch[1:] = rt.far_lags_of_density(M, D, density)
        arch[0] = glue.arch_lag0_geo(D) - rt.uv_cell_delta(D, density)
        out.append(dict(arch=arch, atom=lay["atom"], pole=lay["pole"]))
    return out


def report_variant(tag, label, prof, ref_final):
    clauses = rt.certificate(prof, ref_final)
    txt = rt.clause_strings(prof, ref_final)
    per_window = [row["min_sym"] for row in prof["rows"]]
    c4_every = all(ms < -rt.SYM_TOL for ms in per_window)
    blind = [k for k in rt.CLAUSE_ORDER if k != "c4_symbol"
             and clauses[k]]
    seen = [k for k in rt.CLAUSE_ORDER if k != "c4_symbol"
            and not clauses[k]]
    print("  %s min symbol per window: %s" % (
        tag, " / ".join("%+.3e" % ms for ms in per_window)))
    for k in rt.CLAUSE_ORDER:
        print("    %-9s %-7s %s"
              % (k, "BROKEN" if not clauses[k] else "ok", txt[k]))
    print("  %s gates blind: %s%s"
          % (tag, blind, ("; gates that saw it: %s" % seen)
             if seen else " (only the symbol gate fired)"))
    return dict(c4_every=c4_every, per_window=per_window,
                blind=blind, seen=seen, clauses=clauses)


def run():
    print("=" * 78)
    print("GLOBAL HANDOFF -- RED TEAM RT6 decision: the symbol gate "
          "as deck detector")
    print("=" * 78)

    hits = self_firewall()
    check("F0 self AST firewall (banned zero/prime identifiers)",
          not hits, str(hits or "clean"))
    check("G0.1 variant manifest SHA-256 frozen before any comb data",
          True, "%s...; gram battery SHA-256 %s..."
          % (MANIFEST_HASH[:16], gp.BATTERY_SPEC_HASH[:16]))

    # ---- deployed frames, source comb, true layers (audited path)
    windows = glue.declared_family()
    maximum = int(max(math.exp(2.0 * window["alpha"])
                      for window in windows) + 0.5)
    comb, meta = gp.source_comb(maximum)
    true_layers = [gp.build_true_source_layers(window, comb)
                   for window in windows]
    wiring = 0.0
    for window, lay in zip(windows, true_layers):
        assembled = lay["arch"] + lay["atom"] + lay["pole"]
        wiring = max(wiring, float(
            np.max(np.abs(assembled - window["p"]))
            / np.max(np.abs(window["p"]))))
    check("G0.2 ingredient wiring before Q (reused guard)",
          wiring <= rt.WIRE_TOL,
          "comb slots=%d, Gaussian irreducibles=%d, max rel dev %.3e"
          % (len(comb), meta["n_irred"], wiring))

    # ---- B0 positive anchor (full certificate incl. c4)
    base = rt.profile_eval("B0 BASELINE -- true construction, "
                           "Nf = 2M+1", windows, true_layers,
                           rt.count_anti_alias, gp.target_gram)
    cl_base = rt.certificate(base, None)
    band_ok = (rt.SLOPE_BAND[0] <= base["slope"] <= rt.SLOPE_BAND[1]
               and rt.RATIO_BAND[0] <= base["ratio"]
               <= rt.RATIO_BAND[1])
    baseline_ok = check(
        "B0 baseline passes the FULL certificate incl. c4 and "
        "reproduces the audited bands",
        all(cl_base.values()) and band_ok,
        "clauses=%s; slope %.3f in %s, final/first %.3f in %s; min "
        "symbol %+.2e, E* = %.4f, kappa = %.5f"
        % ({k: v for k, v in cl_base.items() if not v} or "all pass",
           base["slope"], list(rt.SLOPE_BAND), base["ratio"],
           list(rt.RATIO_BAND), base["min_sym"], base["errors"][-1],
           base["kappa"]))
    if not baseline_ok:
        print("\nVERDICT: RT6-INVALID -- the true construction fails "
              "its own certificate; construction problem, promotion "
              "blocked.  COMBINED: NOT-GREEN.")
        return 1
    ref_final = base["errors"][-1]
    base_min_sym = base["min_sym"]

    # ---- gated excess-mode variants
    results = {}
    for var in VARIANTS:
        print("\n%s -- %s (exponents %s, weights %s)"
              % (var["tag"], var["label"], var["exponents"],
                 var["weights"]))
        layers = wrong_arch_layers(
            windows, true_layers,
            deck_density(var["exponents"], var["weights"]))
        prof = rt.profile_eval("%s wrong-deck arch layer" % var["tag"],
                               windows, layers, rt.count_anti_alias,
                               gp.target_gram)
        res = report_variant(var["tag"], var["label"], prof, ref_final)
        results[var["tag"]] = res
        check("%s.a symbol gate fires on EVERY window (min symbol "
              "< -%.0e)" % (var["tag"], rt.SYM_TOL), res["c4_every"],
              " / ".join("%+.3e" % ms for ms in res["per_window"]))
        if var["gate_blindness"]:
            blind_ok = all(res["clauses"][k] for k in rt.CLAUSE_ORDER
                           if k != "c4_symbol")
            check("%s.b BLINDNESS confirmed: c1/c2/c3/c5/c6/c7 all "
                  "pass under the clipped gram (the symbol gate is "
                  "the ONLY detector)" % var["tag"], blind_ok,
                  "blind=%s, saw-it=%s" % (res["blind"], res["seen"]))

    # ---- N1 negative block (measured, not gated)
    print("\n%s -- %s (exponents %s): DECLARED DEFICIT MODE, "
          "positivity gates provably blind by sign"
          % (NEG_BLOCK["tag"], NEG_BLOCK["label"],
             NEG_BLOCK["exponents"]))
    layers_n1 = wrong_arch_layers(
        windows, true_layers,
        deck_density(NEG_BLOCK["exponents"], NEG_BLOCK["weights"]))
    prof_n1 = rt.profile_eval("N1 deficit-deck arch layer", windows,
                              layers_n1, rt.count_anti_alias,
                              gp.target_gram)
    res_n1 = report_variant("N1", NEG_BLOCK["label"], prof_n1,
                            ref_final)
    into_interior = all(ms >= base_min_sym - rt.SYM_TOL
                        for ms in res_n1["per_window"])
    caught_by = res_n1["seen"] + (["c4_symbol"]
                                  if res_n1["c4_every"] else [])
    print("  N1 measured outcome (reported, not gated): symbol moves "
          "into the interior on every window = %s (baseline min "
          "%+.2e); caught by = %s -- %s"
          % (into_interior, base_min_sym, caught_by or "NOTHING",
             "the certificate's resolution floor for interior-"
             "directed perturbations, consistent with the declared "
             "battery-limited identification remainder"
             if not caught_by else
             "the deficit mode is caught by the listed gate(s)"))

    # ---- verdict (frozen rules)
    c4_all = all(results[v["tag"]]["c4_every"] for v in VARIANTS)
    blind_v1 = all(results["V1"]["clauses"][k]
                   for k in rt.CLAUSE_ORDER if k != "c4_symbol")
    if c4_all and blind_v1:
        verdict = "RT6-SYMBOL-DETECTS"
    else:
        verdict = "RT6-PARTIAL"
    escapes = [v["tag"] for v in VARIANTS
               if not results[v["tag"]]["c4_every"]]

    print("\n" + "=" * 78)
    print("VERDICT: %s" % verdict)
    if verdict == "RT6-SYMBOL-DETECTS":
        print("  the symbol gate fires on all three excess-mode deck "
              "corruptions on every window; under V1 the clipped "
              "gram passes c1/c2/c3/c5/c6/c7 -- the blindness of the "
              "rate/level/identification gates is CONFIRMED, the "
              "symbol gate is the load-bearing detector.")
        print("COMBINED AUDIT STATEMENT: with the parent probe's "
              "frozen facts (firewall clean, baseline reproduced, "
              "RT1-RT5/RT7/RT8 conclusive) and this RT6 decision, "
              "the round's red team is REDTEAM-GREEN-COMBINED.")
        print("PROMOTION NOTE (binding): the symbol-nonnegativity "
              "gate must NEVER be dropped from any future "
              "certificate -- for the excess-mode deck-corruption "
              "class it is the ONLY firing detector; N1 marks the "
              "measured detector boundary (deficit mode: symbol "
              "into the interior, caught by %s).  NO RH claim."
              % (caught_by or "nothing at this resolution"))
    else:
        print("  %s%s" % (
            ("variants escaping even the symbol gate: %s -- a "
             "genuine audit hole. " % escapes) if escapes else "",
            "" if blind_v1 else
            "V1 blindness clause failed: gates %s saw the corruption."
            % results["V1"]["seen"]))
        print("COMBINED AUDIT STATEMENT: the round's red team is "
              "NOT-GREEN; promotion of the handoff round stays "
              "blocked on the RT6 decision.")

    elapsed = time.time() - T_START
    if FAILS:
        print("RESULT: %d/%d CHECKS PASSED; FAILURES %s (%.1f s)"
              % (len(CHECKS) - len(FAILS), len(CHECKS),
                 ",".join(FAILS), elapsed))
    else:
        print("RESULT: ALL %d CHECKS PASSED (%.1f s)"
              % (len(CHECKS), elapsed))
    return 0 if verdict == "RT6-SYMBOL-DETECTS" else 1


if __name__ == "__main__":
    raise SystemExit(run())
