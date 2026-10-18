#!/usr/bin/env python3
"""v759 -- PRIME.HANDOFFRES.01: Gate 1 of the diagonal Gram round -- fixed window, growing frequency resolution: E_total is q-invariant under Nf = q(2M+1), q in {1,2,4,8}, to ~1e-13 on all three fixed windows; the remaining handoff error is a genuine boundary/cutoff/object-gluing error, not a quadrature error (RESOLUTION-BOUNDARY, Fall B).

PROVENANCE: discovery probe handoff_fixed_window_resolution_probe.py (2026-08-04, 8/8 guards, verdict RESOLUTION-BOUNDARY).  Promoted verbatim (sibling imports point at v716/v767); numbers unchanged.
GLOBAL-HANDOFF Gate-1 classifier: fixed window, growing frequency
resolution (target module v759_handoff_fixed_window_resolution).

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  It never reads a zero ordinate and never
factors, diagonalizes, or tests the target before every source object
is built and SHA-256 frozen (same discipline as the parent probes).

QUESTION (Gate 1 of the diagonal Gram closure round): is the current
handoff error a frequency-quadrature error, or a genuine boundary /
cutoff / object-gluing error?  The tail decider
(handoff_tail_weil_probe) already measured tail(2M+1 -> 4M+1) =
2.4e-13 uniform in window, so Fall B is the EXPECTED outcome; this
probe decides it cleanly under preregistered numeric gates instead of
assuming it.

DESIGN (everything reused verbatim from handoff_frequency_gram_probe:
frozen 24-function battery with its SHA-256 spec hash, frozen source
formula p = c_arch + c_atom + c_pole -> Fejer symbol -> positive-part
frequency columns + closed rank-one pole column, source_gram with its
internal Q byte hash, target_gram, error_metrics; comb / heat-trace /
pole-block builders from moonshot_arch_glue_probe; nothing invented):
  *  THREE windows held FIXED: the smallest (h = 184, M = 368), the
     middle (h = 606, M = 1212) and the largest (h = 1433, M = 2866)
     of the declared five-window ladder (family indices 0 / 2 / 4).
  *  ONLY the frequency count varies: Nf = q * (2M + 1) with
     q in {1, 2, 4, 8}.  Source formula, battery, normalization
     (1/Nf cell weight is part of the frozen formula and rescales
     with Nf) and all ingredients unchanged.
  *  Reported per (window, q): E_total (spectral relative error of
     G_source vs the deployed Weil target), E_arch (arch layer,
     relative to the same target spectral scale), E_paired (atom +
     pole/cutoff combined as ONE renormalized object -- never two
     separate absolute estimates), E_alias (the q-increment
     rel2(G(q), G(q_prev)) on the target spectral scale) and
     lambda_min(G_source).

PREREGISTERED DECISION (all numbers frozen HERE before the first run):
  FALL A (frequency-quadrature route): on the LARGEST window
      (h = 1433) there exists q in {2, 4, 8} with
      E_total(q) <= FALL_A_DROP * E_total(q=1), FALL_A_DROP = 0.80
      (i.e. the error falls by more than a factor 1.25 with pure
      frequency refinement).
  FALL B (anti-alias already exact): on ALL three windows and for
      every q in {2, 4, 8},
      |E_total(q) - E_total(q=1)| <= CONST_TOL = 1e-7  AND
      every alias increment E_alias(q) <= ALIAS_TOL = 1e-7
      (increments at rounding level) -- then the remaining error is
      purely boundary / cutoff / object-gluing.
  Per-window class: QUAD (drop gate holds), BOUND (constancy gate
      holds), INDET (neither).
  VERDICT ENUM (checked in this frozen order):
      RESOLUTION-QUADRATURE  = largest window is QUAD (Fall A);
      RESOLUTION-BOUNDARY    = all three windows are BOUND (Fall B);
      RESOLUTION-MIXED       = anything else; the per-window
                               QUAD/BOUND/INDET split is spelled out.

GUARDS (must pass or the run is invalid): AST firewall; battery spec
SHA-256 and the full Q ladder specification (windows, q ladder, Nf
formula, decision bars) SHA-256-frozen BEFORE any comb/deployed data;
ingredient wiring <= 2e-10; true-source Fejer symbol >= -2e-9 on every
frequency grid (source PSD convention, checked on every cell); source
PSD lmin >= -1e-9 on every cell; all 12 Q byte hashes pairwise
distinct; layer-sum residual <= 1e-9 relative.  Negative controls are
not the point of this classifier (the parent probes' controls fire on
this exact construction); the AST firewall is kept.

COST (predeclared before the first run): total frequency cells
sum_w sum_q q*(2M_w+1) = 15 * (737 + 2425 + 5733) = 133,425 over 12
cells; the tail decider processed ~98k cells of the same kernel in
8.9 s, so the full grid is estimated at well under 5 minutes.  NO cell
cap is invoked; the full preregistered grid runs.

STOP-LIST (binding, inherited from the round): no separate absolute
atom/pole estimates; no target decomposition, no Cholesky of the Weil
matrix, no target resolvent; no Riemann zeros anywhere in the
construction path; no fits inside any proof-grade inequality; no bare
A^{-1}; no local layer positivity; every battery / parameter sequence
/ kill bar hashed before evaluation.  NO RH claim.

CONSEQUENCE MAP (frozen): Fall A => a quantitative trapezoid/DFT
error-bound theorem is the round's priority.  Fall B => anti-alias
closes as exact; only the paired boundary/cutoff remainder is attacked
next.  MIXED => the window split localizes which regime each window
sits in and both fronts stay open.

RESULTS (2026-08-04, first and only preregistered run, 8.3 s;
GUARDS 8/8, verdict RESOLUTION-BOUNDARY = FALL B on all three
windows):
  *  E_total is constant in q to 15 digits on every window:
     h = 184: 0.0854628851 (max |dE_total| = 2.3e-15),
     h = 606: 0.0457474733 (max |dE_total| = 5.1e-14),
     h = 1433: 0.0376902394 (max |dE_total| = 7.0e-14) --
     all far below the frozen CONST_TOL = 1e-7.
  *  Alias increments are pure rounding: max 2.5e-14 / 1.5e-13 /
     1.8e-13 per window (frozen bar 1e-7).  E_arch (0.0317 / 0.0171 /
     0.0141) and E_paired (0.0852 / 0.0456 / 0.0376) are q-invariant
     to the same level; lambda_min(G_source) = +6.0e-3 / +5.7e-3 /
     +5.5e-3, stable in q.
  *  The Fall A drop gate never comes close on any window
     (E_total(q=8)/E_total(q=1) = 1 to rounding); the largest window
     is BOUND, not QUAD.
  *  CONSEQUENCE FOR THE ROUND: the anti-alias quadrature Nf = 2M+1
     closes as EXACT on the frozen battery (confirming the tail
     decider's tail = 2.4e-13 under the fixed-window classifier
     gates); NO quantitative trapezoid/DFT error theorem is needed.
     The entire remaining handoff error (E_total 0.0377 at the top
     window, carried by E_paired 0.0376) is a genuine boundary /
     cutoff / object-gluing error: the paired atom+pole boundary
     remainder is the only object attacked next.  NO RH claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/handoff_fixed_window_resolution_probe.py
"""


import ast
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

_HERE_DISC = os.path.abspath(os.path.join(_HERE, "..",
    "experiments", "tfpt-discovery"))
sys.path.insert(0, _HERE_DISC)

import v716_moonshot_arch_glue as glue  # noqa: E402
import v767_handoff_frequency_gram as gp  # noqa: E402

T_START = time.time()

# ------------------------------------------------ preregistered bars
WINDOW_HS = (184, 606, 1433)   # fixed windows (h = M//2), family 0/2/4
Q_LADDER = (1, 2, 4, 8)        # Nf = q * (2M + 1)
FALL_A_DROP = 0.80             # Fall A: E_total drop gate, top window
CONST_TOL = 1.0e-7             # Fall B: |E_total(q) - E_total(1)| bar
ALIAS_TOL = 1.0e-7             # Fall B: alias-increment rounding bar
SOURCE_NEG_TOL = 2.0e-9
WIRE_TOL = 2.0e-10
PSD_TOL = -1.0e-9
LAYER_RESID_TOL = 1.0e-9

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def ast_firewall():
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
                if any(b in token.lower() for b in BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in BANNED):
            hits.add(name)
    return sorted(hits)


def freeze_q_specification():
    """SHA-256-freeze the full ladder specification (windows, q ladder,
    Nf formula, every decision bar) BEFORE any comb/deployed data."""
    spec = dict(version="fixed-window-resolution-v1",
                windows_h=list(WINDOW_HS),
                q_ladder=list(Q_LADDER),
                nf_formula="Nf = q * (2M + 1), uniform midpoint cells",
                source_formula="Fejer-positive-frequency-v1+closed-pole",
                battery_hash=gp.BATTERY_SPEC_HASH,
                fall_a_drop=FALL_A_DROP,
                const_tol=CONST_TOL,
                alias_tol=ALIAS_TOL,
                verdict_order=["RESOLUTION-QUADRATURE",
                               "RESOLUTION-BOUNDARY",
                               "RESOLUTION-MIXED"])
    blob = json.dumps(spec, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def rel2(A, B, scale):
    return float(sla.norm(A - B, 2)) / max(scale, 1.0e-300)


def window_cells(window, layers):
    """All q cells for one fixed window.  Every Q is built and byte-
    hashed inside gp.source_gram BEFORE the target is constructed."""
    M = window["M"]
    free, full, bat_hash = gp.sampled_battery(M, window["D"])
    sources = {}
    for q in Q_LADDER:
        count = q * (2 * M + 1)
        sources[q] = gp.source_gram(window, layers, full, count,
                                    "RESOLUTION-q%d" % q)
    # target construction strictly after every Q hash is complete
    target = gp.target_gram(window, free)
    tscale = max(float(sla.norm(target["gram"], 2)), 1.0e-300)
    pair_target = target["layers"]["atom"] + target["layers"]["pole"]
    cells = []
    for index, q in enumerate(Q_LADDER):
        source = sources[q]
        e_total = gp.error_metrics(source["gram"],
                                   target["gram"])["spectral"]
        e_arch = gp.error_metrics(source["layers"]["arch"],
                                  target["layers"]["arch"],
                                  reference=target["gram"])["spectral"]
        pair_source = source["layers"]["atom"] + source["layers"]["pole"]
        e_paired = gp.error_metrics(pair_source, pair_target,
                                    reference=target["gram"])["spectral"]
        e_alias = 0.0 if index == 0 else rel2(
            source["gram"], sources[Q_LADDER[index - 1]]["gram"], tscale)
        lam_min = float(sla.eigvalsh(source["gram"],
                                     subset_by_index=[0, 0])[0])
        cells.append(dict(q=q, count=source["dimension"] - 1,
                          e_total=e_total, e_arch=e_arch,
                          e_paired=e_paired, e_alias=e_alias,
                          lam_min=lam_min,
                          min_sym=source["minimum_symbol"],
                          resid=source["layer_residual"] / tscale,
                          q_hash=source["q_hash"]))
    return dict(window=window, cells=cells, tscale=tscale,
                bat_hash=bat_hash)


def classify_window(cells):
    """Frozen per-window class: QUAD / BOUND / INDET."""
    base = cells[0]["e_total"]
    quad = any(cell["e_total"] <= FALL_A_DROP * base
               for cell in cells[1:])
    bound = all(abs(cell["e_total"] - base) <= CONST_TOL
                for cell in cells[1:]) \
        and all(cell["e_alias"] <= ALIAS_TOL for cell in cells[1:])
    if quad:
        return "QUAD"
    if bound:
        return "BOUND"
    return "INDET"


def run():
    print("=" * 78)
    print("GLOBAL HANDOFF -- Gate-1 classifier: fixed window, growing "
          "frequency resolution")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    q_spec_hash = freeze_q_specification()
    check("G0.2 battery + Q ladder specification frozen BEFORE any "
          "comb/deployed data", len(gp.BATTERY_SPEC) == gp.BATTERY_SIZE,
          "battery SHA256 %s..., Q-spec SHA256 %s..."
          % (gp.BATTERY_SPEC_HASH[:16], q_spec_hash[:16]))

    # ---- deployed windows + source comb (first target-side touch)
    family = glue.declared_family()
    windows = [w for w in family if w["M"] // 2 in WINDOW_HS]
    check("G0.3 declared fixed windows found",
          tuple(w["M"] // 2 for w in windows) == WINDOW_HS,
          "h = %s, M = %s"
          % ("/".join(str(w["M"] // 2) for w in windows),
             "/".join(str(w["M"]) for w in windows)))
    maximum = int(max(math.exp(2.0 * w["alpha"]) for w in windows) + 0.5)
    comb, metadata = gp.source_comb(maximum)
    true_layers = [gp.build_true_source_layers(w, comb) for w in windows]
    wiring = 0.0
    for window, layers in zip(windows, true_layers):
        assembled = layers["arch"] + layers["atom"] + layers["pole"]
        wiring = max(wiring, float(np.max(np.abs(assembled - window["p"]))
                                   / np.max(np.abs(window["p"]))))
    check("G0.4 ingredient wiring before Q", wiring <= WIRE_TOL,
          "comb slots=%d, Gaussian irreducibles=%d, max rel deployed "
          "deviation %.3e"
          % (len(comb), metadata["n_irred"], wiring))

    # ---- the (window x q) grid
    rows = []
    print("\n-- E-table: fixed window x frequency resolution "
          "(Nf = q*(2M+1))")
    for window, layers in zip(windows, true_layers):
        row = window_cells(window, layers)
        rows.append(row)
        h = window["M"] // 2
        for cell in row["cells"]:
            print("  h=%4d q=%d Nf=%5d E_total=%.10f E_arch=%.10f "
                  "E_paired=%.10f E_alias=%.3e lmin=%+.3e hash=%s"
                  % (h, cell["q"], cell["count"], cell["e_total"],
                     cell["e_arch"], cell["e_paired"], cell["e_alias"],
                     cell["lam_min"], cell["q_hash"][:16]))

    # ---- guards on every cell
    all_cells = [cell for row in rows for cell in row["cells"]]
    hashes = [cell["q_hash"] for cell in all_cells]
    check("G1.1 all %d Q byte hashes pairwise distinct" % len(hashes),
          len(set(hashes)) == len(hashes))
    check("G1.2 true-source symbol >= %.0e on every frequency grid"
          % -SOURCE_NEG_TOL,
          all(cell["min_sym"] >= -SOURCE_NEG_TOL for cell in all_cells),
          "min %.2e" % min(cell["min_sym"] for cell in all_cells))
    check("G1.3 source PSD on every cell (lmin >= %.0e)" % PSD_TOL,
          all(cell["lam_min"] >= PSD_TOL for cell in all_cells),
          "min %.2e" % min(cell["lam_min"] for cell in all_cells))
    check("G1.4 layer-sum residual <= %.0e relative" % LAYER_RESID_TOL,
          all(cell["resid"] <= LAYER_RESID_TOL for cell in all_cells),
          "max %.2e" % max(cell["resid"] for cell in all_cells))

    # ---- preregistered decision
    classes = {row["window"]["M"] // 2: classify_window(row["cells"])
               for row in rows}
    print("\n-- per-window class (frozen gates: drop <= %.2f x base on "
          "some q > 1 => QUAD; |dE_total| <= %.0e and alias <= %.0e on "
          "all q => BOUND)" % (FALL_A_DROP, CONST_TOL, ALIAS_TOL))
    for row in rows:
        h = row["window"]["M"] // 2
        base = row["cells"][0]["e_total"]
        drift = max(abs(cell["e_total"] - base)
                    for cell in row["cells"][1:])
        alias = max(cell["e_alias"] for cell in row["cells"][1:])
        print("  h=%4d class=%s  E_total(q=1)=%.10f  max|dE_total|=%.3e"
              "  max alias increment=%.3e"
              % (h, classes[h], base, drift, alias))

    top_h = WINDOW_HS[-1]
    if classes[top_h] == "QUAD":
        verdict = "RESOLUTION-QUADRATURE"
    elif all(value == "BOUND" for value in classes.values()):
        verdict = "RESOLUTION-BOUNDARY"
    else:
        verdict = "RESOLUTION-MIXED"

    guards_ok = all(ok for (_name, ok) in CHECKS)
    print("\nVERDICT: %s%s" % (verdict, "" if guards_ok
                               else "  (INVALID RUN: guard failure)"))
    print("SPLIT: %s" % ", ".join("h=%d:%s" % (h, classes[h])
                                  for h in WINDOW_HS))
    if verdict == "RESOLUTION-QUADRATURE":
        print("CONSEQUENCE: the handoff error is (at least partly) a "
              "frequency-quadrature error -- the round's priority is a "
              "quantitative trapezoid/DFT error-bound theorem.")
    elif verdict == "RESOLUTION-BOUNDARY":
        print("CONSEQUENCE: anti-alias Nf = 2M+1 closes as EXACT on the "
              "frozen battery; frequency refinement buys nothing beyond "
              "rounding.  The remaining handoff error is purely "
              "boundary / cutoff / object-gluing: only the paired "
              "atom+pole boundary remainder is attacked next.  "
              "NO RH claim.")
    else:
        print("CONSEQUENCE: the regimes are window-dependent as split "
              "above; both the quadrature theorem and the paired "
              "boundary remainder stay open fronts.")

    n_ok = sum(1 for (_name, ok) in CHECKS if ok)
    elapsed = time.time() - T_START
    if not guards_ok:
        print("RESULT: %d/%d GUARDS PASSED; FAILURES %s (%.1fs)"
              % (n_ok, len(CHECKS),
                 ",".join(name.split()[0] for (name, ok) in CHECKS
                          if not ok), elapsed))
        return 1
    print("RESULT: ALL %d GUARDS PASSED (%.1fs)" % (len(CHECKS), elapsed))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
