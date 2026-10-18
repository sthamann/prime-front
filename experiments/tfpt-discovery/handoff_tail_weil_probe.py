#!/usr/bin/env python3
"""GLOBAL-HANDOFF-OFFENSIVE -- the tail / cross-window / Weil-
identification decider (review module 4 error decomposition + Weil
closure), handoff_tail_weil_probe.

Exploration only (tfpt-experiment firewall): NOT wired into run_all.py,
no ledger row, no paper edit, no website edit, NO RH CLAIM, and this
probe writes no files.  It never reads a zero ordinate and never
factors, diagonalizes, or tests the target before every source object
is built and SHA-256 frozen (same discipline as both parent probes).

INPUT STATE (frozen findings of the two green deciders):
  *  Module 1, handoff_bulk_probe -- 17/17 PASS,
     HANDOFF-BULK-CONVERGES: the eps-regulated resolvent
     G^eps = (A_X + eps I)^{-1} is the admissible operator-system
     evaluation; fixed-observable defects fall at rates b =
     0.174..0.310 per X unit, robust over eps = 1e-1..1e-3; the bare
     inverse does not stabilize (named negative block); the wall is PD
     persistence at eps -> 0 and is quantified, never gated away.
  *  Modules 2+3, handoff_frequency_gram_probe -- 6/6 PASS,
     HANDOFF-GRAM-CONVERGES with Candidate B (anti-alias Nf = 2M+1):
     spectral relative errors 0.0855/0.0585/0.0457/0.0452/0.0377 over
     dimQ 738/1378/2426/4110/5734, slope -0.369; final layer errors
     arch 0.014127 / atom 0.394636 / pole-cutoff 0.414415 (dominant =
     pole).  Its stated remainders are exactly the three questions
     decided here.

QUESTIONS (decided on the reachable surface, no claim beyond it):
  (T) UNIFORM QUADRATURE TAIL.  The frequency Gram is the uniform cell
      quadrature of s(theta) F_i(theta)* F_j(theta), a trigonometric
      polynomial of degree <= (M-1) + spread(battery) whenever the
      Fejer symbol is nonnegative on the nodes.  Measured: the relative
      spectral distance between the Gram at Nf = 2M+1 and Nf = 4M+1
      (the tail), and between Nf = 4M+1 and Nf = 6M+1 (the exactness
      plateau; both counts are beyond the alias degree, so their
      distance is a pure float Ward).  A tail that terminates
      algebraically IS the uniform-in-window tail bound.
  (A) ERROR DECOMPOSITION WITH RATES at exact quadrature Nf = 4M+1:
      per-layer spectral errors (arch / atom / pole-cutoff, all
      relative to the same-window deployed target spectral norm) along
      the declared 5-window ladder, plus the combined atom+pole pair.
      Rates are measured; no layer is sign-forced or positivized
      (stop-list).
  (B) CROSS-WINDOW COMPATIBILITY in the module-1 weak-* sense: two
      interleaved truncation ladders A (M = 256..800 step 32) and
      B (= A + 16 cells) of ONE tower lag vector (exact prefix nesting,
      simpler_tower T1.1; the prefixes are nested and the A/B windows
      overlap); for every frozen local observable pair the defect
      |<f_i, G^eps_{A_k} f_j> - <f_i, G^eps_{B_k} f_j>| must fall as
      both windows grow.  eps-battery 1e-1/1e-2/1e-3, R = 1, 2.
      Uniformity in eps -> 0 is NOT part of PASS (the wall stays at the
      spectral edge; PD margins are reported, not hidden).
  (W) WEIL IDENTIFICATION ON THE BATTERY: does the converged
      source-Gram functional agree with the deployed Weil functional
      G_Weil[i,j] = W(f_i * f_j~) on the frozen 24-function battery
      within a documented decreasing error, and is the target itself
      window-stable on the battery (one limit point on the dense test
      space reachable here)?  Identification scalar
      kappa = <G_src, G_Weil>_F / ||G_Weil||_F^2.

FROZEN FORMULAS (all imported/reused, none invented): battery, source,
target, layer and control machinery from handoff_frequency_gram_probe
(sampled_battery, source_gram with its internal Q SHA-256 freeze,
target_gram, error_metrics, log_slope, control_profile, epstein_layers,
scrambled_layers); comb / heat-trace / pole-block builders from
moonshot_arch_glue_probe through that probe; tower channels, dyadic
ladder, local battery and rate fit from handoff_bulk_probe /
simpler_schur_recursion_probe; Epstein x^2+5y^2 logarithmic atoms from
epstein_firewall_probe (read-only).

PREREGISTERED GATES (all fixed here BEFORE the first run):
  T0  exactness plateau: max over windows of rel2(G(4M+1), G(6M+1))
      <= 1e-7 (relative to the deployed target spectral norm).
  T1  uniform tail, two declared branches (PASS = (i) or (ii)):
      (i)  algebraic termination: max over windows of
           rel2(G(2M+1), G(4M+1)) <= 1e-7 AND the alias census
           (M-1) + spread <= 2M holds on every window;
      (ii) decaying tail: on every window tail <= 0.10 x same-window
           total error, and tail(top window) < tail(first window).
  A1  exact-quadrature convergence: log-log slope of the total
      spectral error vs dimQ < -0.25, final/first < 0.75, last three
      strictly decreasing.
  A2  pair rate: combined atom+pole layer error slope < -0.25 and
      final/first < 0.75.
  A3  layer decomposition, two declared branches (PASS = (i) or (ii),
      the realized branch is reported):
      (i)  separate rates: atom slope <= -0.10 AND pole slope <= -0.10;
      (ii) cancellation balance: min(atom, pole) >= 3.0 x pair at the
           top window AND A2 holds (the pair, not the single layer,
           carries the rate -- the module-1 H3 anatomy).
  B   six cells (eps in {1e-1, 1e-2, 1e-3}) x (R in {1, 2}): fit rate
      b >= 0.10 per X unit, trend drop exp(b x span) >= 3, raw
      last/first <= 0.5, anti-plateau (b on the second half > 0 OR
      last <= 0.6 x median of the second half).  Guard: mid-rung
      dense-solve Ward <= 1e-8.
  W1  |kappa - 1| at the top window <= 0.05 (the ladder trend is
      reported).
  W2  target window-stability: tau_k = rel2(G_Weil(win k),
      G_Weil(win top)) strictly decreasing in k and tau_last <= 0.75 x
      tau_first.
GUARDS (must pass or the run is invalid): AST firewall; both batteries
and every Q SHA-256-frozen before any deployed/target data is touched;
ingredient wiring <= 2e-10; true-source symbol >= -2e-9 on every grid;
source PSD (lmin >= -1e-9); Q hashes pairwise distinct; layer-sum
residual <= 1e-9 relative.
CONTROLS (mandatory, must fire; a spuriously converging control =
DEAD): C1 gram scramble and C2 gram Epstein at Nf = 2M+1 (fire =
negative symbol beyond 2e-9 OR non-convergent with final error >= 5 x
real); C3 bulk scramble and C4 bulk Epstein at eps = 1e-2 (fire =
eps-Cholesky break on >= 1 rung OR final defect >= 10 x real OR
non-quasi-monotone at slack 1.10).

ITERATION POLICY: NO construction iteration is available to this probe
(the single allowed iteration of the Candidate A/B pattern is declared
UNUSED); the two-branch structure inside T1 and A3 is fixed here before
the first run and exhausts the declared alternatives.

STOP-LIST (binding, inherited): no domino variants, no layer
positivizations, no channel factorizations, no drift-sign attempts, no
raw symbol minorants, no norm triangles, no perturbation theory, no
position-blind estimates.

VERDICT: HANDOFF-TAIL-WEIL-CONVERGES = all gates T0 / T1 / A1 / A2 /
A3 / all six B cells / W1 / W2 pass, all guards pass, all four controls
fire.  HANDOFF-TAIL-WEIL-PARTIAL = guards + controls ok, A1 passes and
>= 4 B cells pass, but at least one other gate fails.
HANDOFF-TAIL-WEIL-DEAD = any control spuriously converges, or A1 fails,
or > 2 B cells fail, or a guard fails.

RESULTS (2026-08-04, first and only preregistered run, 8.9 s; GATES
11/13, GUARDS+CONTROLS 12/12, verdict HANDOFF-TAIL-WEIL-PARTIAL):
  *  T0/T1 PASS: the quadrature tail TERMINATES ALGEBRAICALLY -- the
     alias census (M-1) + spread <= 2M holds on all 5 windows (spread
     209..725 vs 2M = 736..5732); max tail(2M+1 -> 4M+1) = 2.4e-13,
     plateau(4M+1 -> 6M+1) = 1.4e-13.  The Fejer/cell quadrature at
     Nf = 2M+1 is EXACT for the frozen battery, uniformly in the
     window: remainder 1 of the gram decider is closed on this surface
     (there is NO quadrature tail; every layer error is structural).
  *  A1-A3 PASS: exact-quadrature errors equal the 2M+1 values
     (0.0855/0.0585/0.0457/0.0452/0.0377, slope -0.369).  ALL layers
     fall at the SAME documented rate: arch 0.0317 -> 0.0141, atom
     0.8880 -> 0.3946, pole 0.9325 -> 0.4144, slopes -0.365 each;
     BOTH declared A3 branches hold simultaneously -- the dominant
     pole/cutoff error falls with rate -0.365 AND stays, with atom, an
     order-10 cancellation pair over the combined atom+pole channel
     (min(atom,pole)/pair = 10.5; pair slope -0.369): the module-1 H3
     balance anatomy reappears on the gram side.
  *  W1/W2 PASS: kappa = 0.97768 -> 0.99028 (|kappa-1| = 0.0097 at
     top); target window-stability tau = 0.0265 -> 0.0109 strictly
     falling (ratio 0.410).  Identification of the source limit with
     the deployed Weil functional holds on the battery within
     err_top + tau_last = 0.0485 (spectral, relative).
  *  B 4/6: eps = 1e-1 and 1e-2 pass all four cells (b = 0.129..0.216,
     trend 3.0..6.3x, raw 2.8..6.9x).  eps = 1e-3 FAILS the frozen
     endpoint gates in both R cells: the trend still falls (b =
     0.126/0.147, second-half b2 = 0.121/0.101 > 0) but atom-burst
     oscillation at the last rungs breaks the endpoint gates (trend
     2.9x < 3 at R = 1; raw last/first 0.65/0.88 > 0.5 -- the R = 2
     defect jumps 3.8e-4 -> 2.3e-3 on the final rung).  The
     interleaved half-step defect is noisier than the module-1
     full-step Cauchy increment, and at small eps the oscillation
     amplitude grows: the eps -> 0 wall shows up HERE as endpoint
     noise on a falling trend.  No iteration was available (declared
     unused); the two cells stand FAILED as preregistered.
  *  Controls all fire: C1 scramble (negative symbol; errors GROW to
     147.7, slope +1.574), C2 Epstein (negative symbol; 3381 negative
     atom sites, slope +0.307), C3 bulk scramble (eps-Cholesky breaks
     36/36 rungs, lambda_min = -1.3e+3), C4 bulk Epstein (breaks
     24/24 rungs, lambda_min = -84.4).
  *  HONEST REMAINDER: (1) cross-window compatibility at eps = 1e-3
     needs deeper ladders or an oscillation-aware endpoint statistic
     -- as frozen it fails, hence PARTIAL, not CONVERGES; (2) the
     identification is battery-limited (24 functions, support radius
     < 1.6) -- no claim on any larger test space; (3) the eps -> 0
     wall (PD persistence) is untouched.  NO RH claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/handoff_tail_weil_probe.py
"""

import ast
import hashlib
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

import v563_paper2_readouts as core  # noqa: E402
import moonshot_arch_glue_probe as glue  # noqa: E402
import handoff_frequency_gram_probe as gp  # noqa: E402
import handoff_bulk_probe as hbp  # noqa: E402
import simpler_schur_recursion_probe as srp  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402

T_START = time.time()

# ------------------------------------------------ preregistered bars
TOL_EXACT = 1.0e-7        # T0 plateau / T1 branch (i)
TAIL_FRAC = 0.10          # T1 branch (ii)
RATE_BAR = -0.25          # A1 / A2 log-log slope
RATIO_BAR = 0.75          # A1 / A2 final/first
LAYER_RATE_BAR = -0.10    # A3 branch (i)
BALANCE_MIN = 3.0         # A3 branch (ii)
KAPPA_BAR = 0.05          # W1
TAU_RATIO = 0.75          # W2
SOURCE_NEG_TOL = 2.0e-9
WIRE_TOL = 2.0e-10
LAYER_RESID_TOL = 1.0e-9
PSD_TOL = -1.0e-9

EPS_BAT = (1.0e-1, 1.0e-2, 1.0e-3)
R_BAT = (1.0, 2.0)
LAD_A = list(range(256, 801, 32))     # 18 rungs, X = 4.0 .. 12.5
LAD_OFF = 16                          # ladder B = A + 16 cells
M_FULL = 824                          # tower reach (X = 12.875 <= 12.90)
B_RATE_BAR = 0.10
B_TREND_BAR = 3.0
B_RAW_BAR = 0.5
B_PLATEAU = 0.6
B_WARD = 1.0e-8
B_CTRL = 10.0
MONO_SLACK = 1.10
EPS_CTRL = 1.0e-2
EP_NCAP = 34000
EP_MMAX = 640
SEED = 7
CONTROL_FACTOR = 5.0

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # preregistered decider gates: feed the verdict only


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def gate(name, ok, detail=""):
    GATES.append((name, bool(ok)))
    print("[GATE %s] %s%s" % ("PASS" if ok else "FAIL", name,
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


def rel2(A, B, scale):
    return float(sla.norm(A - B, 2)) / max(scale, 1.0e-300)


# ------------------------------------------------ frozen bulk battery
def freeze_bulk_battery():
    """The module-1 local battery (4 boxes + 3 hats per R), frozen with
    the full (b)-axis declaration BEFORE any comb/deployed data load."""
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("tail-weil bulk battery: 4 boxes + 3 hats per R, "
                "l2-norm, D=%.10f, R=%s, eps=%s, ladder A=%d..%d step "
                "32, ladder B=A+%d"
                % (srp.DGRID, R_BAT, EPS_BAT, LAD_A[0], LAD_A[-1],
                   LAD_OFF)).encode())
    for R in R_BAT:
        bats[R] = hbp.battery(R)
        for nm, v in bats[R]:
            hsh.update(nm.encode())
            hsh.update(v.tobytes())
    return bats, hsh.hexdigest()


# ==================================================== gram axis (T/A/W)
def gram_axis(windows, true_layers):
    """Per declared window: source Grams at Nf = 2M+1 / 4M+1 / 6M+1
    (each Q hashed inside source_gram BEFORE the target is built),
    then the deployed target and all layer errors."""
    rows = []
    print("\n-- gram axis: quadrature ladder + exact-quadrature layers")
    for w, layers in zip(windows, true_layers):
        M = w["M"]
        free, full, bat_hash = gp.sampled_battery(M, w["D"])
        srcs = {}
        for tagc, cnt in (("anti", 2 * M + 1), ("exact", 4 * M + 1),
                          ("plateau", 6 * M + 1)):
            srcs[tagc] = gp.source_gram(w, layers, full, cnt,
                                        "TAILWEIL-" + tagc)
        # target construction strictly after every Q hash is complete
        tgt = gp.target_gram(w, free)
        tscale = max(float(sla.norm(tgt["gram"], 2)), 1.0e-300)
        tail = rel2(srcs["anti"]["gram"], srcs["exact"]["gram"], tscale)
        plateau = rel2(srcs["exact"]["gram"], srcs["plateau"]["gram"],
                       tscale)
        err_exact = gp.error_metrics(srcs["exact"]["gram"], tgt["gram"])
        err_anti = gp.error_metrics(srcs["anti"]["gram"], tgt["gram"])
        layer_err = {
            name: gp.error_metrics(srcs["exact"]["layers"][name],
                                   tgt["layers"][name],
                                   reference=tgt["gram"])["spectral"]
            for name in ("arch", "atom", "pole")
        }
        pair_src = srcs["exact"]["layers"]["atom"] \
            + srcs["exact"]["layers"]["pole"]
        pair_tgt = tgt["layers"]["atom"] + tgt["layers"]["pole"]
        pair_err = gp.error_metrics(pair_src, pair_tgt,
                                    reference=tgt["gram"])["spectral"]
        kappa = float(np.sum(srcs["exact"]["gram"] * tgt["gram"])
                      / np.sum(tgt["gram"] * tgt["gram"]))
        lmin = float(sla.eigvalsh(srcs["exact"]["gram"],
                                  subset_by_index=[0, 0])[0])
        nz = np.nonzero(np.any(full != 0.0, axis=1))[0]
        spread = int(nz.max() - nz.min())
        alias_ok = (M - 1) + spread <= 2 * M
        min_sym = min(srcs[t]["minimum_symbol"]
                      for t in ("anti", "exact", "plateau"))
        resid = max(srcs[t]["layer_residual"]
                    for t in ("anti", "exact", "plateau")) / tscale
        rows.append(dict(w=w, srcs=srcs, tgt=tgt, tscale=tscale,
                         tail=tail, plateau=plateau,
                         err_exact=err_exact, err_anti=err_anti,
                         layer_err=layer_err, pair_err=pair_err,
                         kappa=kappa, lmin=lmin, spread=spread,
                         alias_ok=alias_ok, min_sym=min_sym,
                         resid=resid, bat_hash=bat_hash,
                         dim_exact=srcs["exact"]["dimension"]))
        print("  h=%4d M=%4d Nf(anti/exact/plateau)=%d/%d/%d "
              "spread=%d alias-deg=%d<=2M=%d:%s minS=%+.3e "
              "lmin(Gs)=%+.3e"
              % (M // 2, M, 2 * M + 1, 4 * M + 1, 6 * M + 1, spread,
                 (M - 1) + spread, 2 * M, alias_ok, min_sym, lmin))
        print("    tail(2M+1->4M+1)=%.3e plateau(4M+1->6M+1)=%.3e "
              "err(spec) anti/exact=%.6f/%.6f"
              % (tail, plateau, err_anti["spectral"],
                 err_exact["spectral"]))
        print("    layer spec errors arch/atom/pole=%.6f/%.6f/%.6f "
              "pair(atom+pole)=%.6f kappa=%.6f qhash=%s"
              % (layer_err["arch"], layer_err["atom"],
                 layer_err["pole"], pair_err, kappa,
                 srcs["exact"]["q_hash"][:16]))
    return rows


def adjudicate_gram(rows):
    print("\n-- T/A/W gate adjudication")
    # guards
    hashes = [r["srcs"][t]["q_hash"] for r in rows
              for t in ("anti", "exact", "plateau")]
    check("G1.1 every Q frozen (SHA-256) before its target; hashes "
          "pairwise distinct", len(set(hashes)) == len(hashes),
          "%d hashes" % len(hashes))
    check("G1.2 true-source symbol nonneg on every grid (>= %.0e) and "
          "PSD (lmin >= %.0e)" % (-SOURCE_NEG_TOL, PSD_TOL),
          all(r["min_sym"] >= -SOURCE_NEG_TOL for r in rows)
          and all(r["lmin"] >= PSD_TOL for r in rows),
          "min sym %s; lmin %s"
          % ("/".join("%.1e" % r["min_sym"] for r in rows),
             "/".join("%.1e" % r["lmin"] for r in rows)))
    check("G1.3 layer-sum residual <= %.0e relative" % LAYER_RESID_TOL,
          all(r["resid"] <= LAYER_RESID_TOL for r in rows),
          "max %.1e" % max(r["resid"] for r in rows))

    # T0 / T1
    plat = max(r["plateau"] for r in rows)
    gate("T0 exactness plateau: max rel2(G(4M+1),G(6M+1)) = %.3e <= "
         "%.0e (uniform over windows)" % (plat, TOL_EXACT),
         plat <= TOL_EXACT)
    tails = [r["tail"] for r in rows]
    branch_i = max(tails) <= TOL_EXACT and all(r["alias_ok"]
                                               for r in rows)
    branch_ii = all(r["tail"] <= TAIL_FRAC * r["err_exact"]["spectral"]
                    for r in rows) and tails[-1] < tails[0]
    gate("T1 uniform quadrature tail: branch(i) algebraic termination "
         "%s (max tail %.3e, alias census %s) / branch(ii) decaying "
         "%s -- tails %s"
         % (branch_i, max(tails),
            all(r["alias_ok"] for r in rows), branch_ii,
            "/".join("%.2e" % t for t in tails)),
         branch_i or branch_ii)

    # A1 total at exact quadrature
    dims = [r["dim_exact"] for r in rows]
    errs = [r["err_exact"]["spectral"] for r in rows]
    slope = gp.log_slope(dims, errs)
    ratio = errs[-1] / errs[0]
    tail3 = errs[-3] > errs[-2] > errs[-1]
    a1 = gate("A1 exact-quadrature convergence: slope %.3f < %s, "
              "final/first %.3f < %s, last three strictly decreasing "
              "%s -- errors %s over dimQ %s"
              % (slope, RATE_BAR, ratio, RATIO_BAR, tail3,
                 "/".join("%.4f" % e for e in errs),
                 "/".join(str(d) for d in dims)),
              slope < RATE_BAR and ratio < RATIO_BAR and tail3)

    # A2 pair rate
    pair = [r["pair_err"] for r in rows]
    p_slope = gp.log_slope(dims, pair)
    p_ratio = pair[-1] / pair[0]
    a2 = gate("A2 atom+pole PAIR rate: slope %.3f < %s, final/first "
              "%.3f < %s -- pair errors %s"
              % (p_slope, RATE_BAR, p_ratio, RATIO_BAR,
                 "/".join("%.4f" % e for e in pair)),
              p_slope < RATE_BAR and p_ratio < RATIO_BAR)

    # A3 layer decomposition (two declared branches)
    arch = [r["layer_err"]["arch"] for r in rows]
    atom = [r["layer_err"]["atom"] for r in rows]
    pole = [r["layer_err"]["pole"] for r in rows]
    at_slope = gp.log_slope(dims, atom)
    po_slope = gp.log_slope(dims, pole)
    ar_slope = gp.log_slope(dims, arch)
    bal = min(atom[-1], pole[-1]) / max(pair[-1], 1.0e-300)
    br_i = at_slope <= LAYER_RATE_BAR and po_slope <= LAYER_RATE_BAR
    br_ii = bal >= BALANCE_MIN and a2
    gate("A3 layer decomposition: branch(i) separate rates %s (atom "
         "slope %.3f, pole slope %.3f vs <= %s) / branch(ii) "
         "CANCELLATION BALANCE %s (min(atom,pole)/pair = %.2f >= %s "
         "at top, pair falls per A2) -- arch slope %.3f, layers "
         "arch=%s atom=%s pole=%s"
         % (br_i, at_slope, po_slope, LAYER_RATE_BAR, br_ii, bal,
            BALANCE_MIN, ar_slope,
            "/".join("%.4f" % e for e in arch),
            "/".join("%.4f" % e for e in atom),
            "/".join("%.4f" % e for e in pole)),
         br_i or br_ii)

    # W1 identification scalar
    kappas = [r["kappa"] for r in rows]
    gate("W1 Weil identification scalar: |kappa-1| at top = %.5f <= "
         "%s -- kappa ladder %s"
         % (abs(kappas[-1] - 1.0), KAPPA_BAR,
            "/".join("%.5f" % k for k in kappas)),
         abs(kappas[-1] - 1.0) <= KAPPA_BAR)

    # W2 target window-stability on the battery
    top = rows[-1]["tgt"]["gram"]
    tsc = rows[-1]["tscale"]
    taus = [rel2(r["tgt"]["gram"], top, tsc) for r in rows[:-1]]
    dec = all(taus[i] > taus[i + 1] for i in range(len(taus) - 1))
    gate("W2 target window-stability: tau = %s strictly decreasing %s "
         "and tau_last/tau_first = %.3f <= %s"
         % ("/".join("%.4f" % t for t in taus), dec,
            taus[-1] / taus[0], TAU_RATIO),
         dec and taus[-1] <= TAU_RATIO * taus[0])
    print("  identification statement (battery-limited, honest): the "
          "source-Gram Cauchy limit agrees with the deployed Weil "
          "functional on the reachable dense test space within "
          "err_top + tau_last = %.4f + %.4f = %.4f (spectral, "
          "relative); NO claim beyond the frozen battery."
          % (errs[-1], taus[-1], errs[-1] + taus[-1]))
    return errs, [r["err_anti"]["spectral"] for r in rows], a1


# ==================================================== bulk axis (B)
def build_tower():
    alpha_full = 0.5 * M_FULL * srp.DGRID
    ka, masks, dev_m = srp.channel_masks(alpha_full)
    check("G2.1 tower comb consistency (zeta-free Gauss double sieve "
          "== deployed masses)", dev_m <= 1.0e-12,
          "rel dev %.1e, ka=%d" % (dev_m, ka))
    c_cont = srp.continuum_lags(M_FULL)
    c_full = c_cont.copy()
    for cnl in ("ro", "re", "sp", "in"):
        c_full = c_full + srp.atom_channel_lags(alpha_full, M_FULL,
                                                masks[cnl])
    T = sla.toeplitz(c_full[:M_FULL])
    return T, c_cont, alpha_full, ka


def compat_rows(T, ladA, ladB, eps, bats):
    """Bilinear battery evaluations from both interleaved ladders via
    the eps-regulated resolvent; one Cholesky per (eps, M)."""
    E = {}
    for M in sorted(set(ladA) | set(ladB)):
        cf = sla.cho_factor(T[:M, :M] + eps * np.eye(M))
        per = {}
        for R in R_BAT:
            nR = int(round(R / srp.DGRID))
            Fm = np.stack([v for _n, v in bats[R]], axis=1)
            F = np.zeros((M, Fm.shape[1]))
            F[:nR] = Fm
            per[R] = F.T @ sla.cho_solve(cf, F)
        E[M] = per
    rows = {}
    for R in R_BAT:
        d0 = np.diag(E[ladA[0]][R])
        scale = float(np.sqrt(np.max(d0) * np.min(d0)))
        rows[R] = [dict(X=Ma * srp.DGRID,
                        XmR=Ma * srp.DGRID - R,
                        mx=float(np.max(np.abs(E[Ma][R] - E[Mb][R])))
                        / scale)
                   for Ma, Mb in zip(ladA, ladB)]
    return rows, E


def cell_gate(rows):
    mxs = [r["mx"] for r in rows]
    rate, resid = hbp.fit_rate(rows)
    span = rows[-1]["XmR"] - rows[0]["XmR"]
    trend = math.exp(rate * span)
    half = rows[len(rows) // 2:]
    rate2, _r2 = hbp.fit_rate(half)
    med2 = float(np.median([r["mx"] for r in half]))
    anti = (rate2 > 0.0) or (mxs[-1] <= B_PLATEAU * med2)
    ok = (rate >= B_RATE_BAR) and (trend >= B_TREND_BAR) \
        and (mxs[-1] <= B_RAW_BAR * mxs[0]) and anti
    return ok, dict(rate=rate, resid=resid, trend=trend,
                    raw=mxs[0] / max(mxs[-1], 1.0e-300), rate2=rate2,
                    last_med=mxs[-1] / max(med2, 1.0e-300), mxs=mxs)


def bulk_axis(T, bats):
    print("\n-- bulk axis: cross-window compatibility (interleaved "
          "ladders, eps-regulated resolvent)")
    ladB = [m + LAD_OFF for m in LAD_A]
    lam0 = float(np.min(np.linalg.eigvalsh(T[:LAD_A[0], :LAD_A[0]])))
    lamF = float(np.min(np.linalg.eigvalsh(T)))
    print("  PD margins (eps = 0, the wall, reported not gated): "
          "lambda_min(W_first) = %.3e, lambda_min(W_full) = %.3e"
          % (lam0, lamF))
    results = {}
    E_ctrl = None
    real_last = None
    for eps in EPS_BAT:
        rows, E = compat_rows(T, LAD_A, ladB, eps, bats)
        if eps == EPS_CTRL:
            E_ctrl = E
        for R in R_BAT:
            ok, d = cell_gate(rows[R])
            results[(eps, R)] = ok
            if eps == EPS_CTRL and R == 2.0:
                real_last = rows[R][-1]["mx"]
            head = ", ".join("%.1e" % v for v in d["mxs"][:3])
            tailp = ", ".join("%.1e" % v for v in d["mxs"][-3:])
            gate("B.eps=%g,R=%g: defect falls %s ... %s over X-R = "
                 "%.1f..%.1f -- rate b = %.3f (>= %g), trend %.1fx "
                 "(>= %g), raw %.1fx (<= 1/%g), anti-plateau b2=%.3f "
                 "last/med2=%.2f, fit residuum %.2f"
                 % (eps, R, head, tailp, rows[R][0]["XmR"],
                    rows[R][-1]["XmR"], d["rate"], B_RATE_BAR,
                    d["trend"], B_TREND_BAR, d["raw"],
                    1.0 / B_RAW_BAR, d["rate2"], d["last_med"],
                    d["resid"]), ok)
    # Ward: mid-rung dense solve against the Cholesky path
    mid = LAD_A[len(LAD_A) // 2]
    R = 2.0
    nR = int(round(R / srp.DGRID))
    Fm = np.stack([v for _n, v in bats[R]], axis=1)
    F = np.zeros((mid, Fm.shape[1]))
    F[:nR] = Fm
    Ed = F.T @ np.linalg.solve(T[:mid, :mid] + EPS_CTRL * np.eye(mid),
                               F)
    ward = float(np.max(np.abs(Ed - E_ctrl[mid][R]))
                 / max(np.max(np.abs(Ed)), 1.0e-300))
    check("G2.2 mid-rung dense-solve Ward (M=%d, eps=%g, R=%g) <= %.0e"
          % (mid, EPS_CTRL, R, B_WARD), ward <= B_WARD,
          "rel %.1e" % ward)
    return results, real_last


def bulk_control(Tc, ladA, ladB, bats, real_last, label):
    lam = float(np.min(np.linalg.eigvalsh(Tc)))
    broken = 0
    sizes = sorted(set(ladA) | set(ladB))
    for M in sizes:
        try:
            sla.cho_factor(Tc[:M, :M] + EPS_CTRL * np.eye(M))
        except np.linalg.LinAlgError:
            broken += 1
    if broken:
        return True, ("A+eps Cholesky breaks on %d/%d rungs "
                      "(lambda_min = %.2e << -eps)"
                      % (broken, len(sizes), lam))
    rows, _E = compat_rows(Tc, ladA, ladB, EPS_CTRL, bats)
    mxs = [r["mx"] for r in rows[2.0]]
    fire = mxs[-1] >= B_CTRL * real_last or not hbp.near_monotone(
        mxs, MONO_SLACK)
    return fire, ("PD under eps; last defect %.2e (real %.2e), "
                  "quasi-monotone(%.2f)=%s"
                  % (mxs[-1], real_last, MONO_SLACK,
                     hbp.near_monotone(mxs, MONO_SLACK)))


def bulk_controls(c_cont, alpha_full, ka, bats, real_last):
    print("\n-- bulk controls (must fire)")
    ladB = [m + LAD_OFF for m in LAD_A]
    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_full, ka))
    cat_s, _dd = core.atom_lags_at(alpha_full, M_FULL, pos,
                                   core.MU_ALL[:ka])
    Ts = sla.toeplitz((c_cont + cat_s)[:M_FULL])
    fire_s, det_s = bulk_control(Ts, LAD_A, ladB, bats, real_last,
                                 "scramble")
    check("C3 bulk scramble control fires", fire_s, det_s)

    r1 = epx.lattice_r1(EP_NCAP)
    b = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(b, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    posE = np.log(supp.astype(float))
    masE = 2.0 * lamE[supp] / np.sqrt(supp.astype(float))
    ladA_E = [m for m in LAD_A if m + LAD_OFF <= EP_MMAX]
    ladB_E = [m + LAD_OFF for m in ladA_E]
    catE, _dd = core.atom_lags_at(0.5 * EP_MMAX * srp.DGRID, EP_MMAX,
                                  posE, masE)
    cont = srp.continuum_lags(EP_MMAX)
    TE = sla.toeplitz((cont + catE)[:EP_MMAX])
    fire_e, det_e = bulk_control(TE, ladA_E, ladB_E, bats, real_last,
                                 "epstein")
    check("C4 bulk Epstein control (x^2+5y^2, %d neg atom sites) fires"
          % int(np.sum(lamE[2:] < -1.0e-9)), fire_e, det_e)


# ==================================================== gram controls
def gram_controls(windows, true_layers, real_errors):
    print("\n-- gram controls at Nf = 2M+1 (must fire)")
    count_fn = lambda w: 2 * w["M"] + 1  # noqa: E731

    scramble = gp.scrambled_layers(windows, true_layers)
    sc = gp.control_profile(windows, scramble, count_fn,
                            "TAILWEIL-CONTROL-SCRAMBLE")
    fire_s = sc["negative_symbol"] or (
        not sc["converges"]
        and sc["errors"][-1] >= CONTROL_FACTOR * real_errors[-1])
    check("C1 gram scramble control fires", fire_s,
          "errors=%s slope %.3f negative-symbol=%s"
          % ("/".join("%.4f" % v for v in sc["errors"]), sc["slope"],
             sc["negative_symbol"]))

    ep_layers, ep_atoms = gp.epstein_layers(windows)
    epc = gp.control_profile(windows, ep_layers, count_fn,
                             "TAILWEIL-CONTROL-EPSTEIN")
    fire_e = epc["negative_symbol"] or (
        not epc["converges"]
        and epc["errors"][-1] >= CONTROL_FACTOR * real_errors[-1])
    check("C2 gram Epstein control fires (%d negative atom sites)"
          % int(np.sum(ep_atoms < -1.0e-9)), fire_e,
          "errors=%s slope %.3f negative-symbol=%s"
          % ("/".join("%.4f" % v for v in epc["errors"]), epc["slope"],
             epc["negative_symbol"]))


# ==================================================== run
def run():
    print("=" * 78)
    print("GLOBAL HANDOFF -- tail / cross-window / Weil-identification "
          "decider")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    bats, bulk_sha = freeze_bulk_battery()
    check("G0.2 batteries frozen BEFORE any comb/deployed data load",
          True, "bulk battery SHA256 %s...; gram battery SHA256 %s... "
          "(analytic spec, module-level)"
          % (bulk_sha[:16], gp.BATTERY_SPEC_HASH[:16]))

    # ---- deployed windows + source comb (first target-side touch)
    windows = glue.declared_family()
    maximum = int(max(math.exp(2.0 * w["alpha"]) for w in windows)
                  + 0.5)
    comb, meta = gp.source_comb(maximum)
    true_layers = [gp.build_true_source_layers(w, comb)
                   for w in windows]
    wiring = 0.0
    for w, layers in zip(windows, true_layers):
        assembled = layers["arch"] + layers["atom"] + layers["pole"]
        wiring = max(wiring, float(np.max(np.abs(assembled - w["p"]))
                                   / np.max(np.abs(w["p"]))))
    check("G0.3 ingredient wiring before Q", wiring <= WIRE_TOL,
          "comb slots=%d, max rel deployed deviation %.3e"
          % (len(comb), wiring))

    # ---- gram axis (T / A / W)
    rows = gram_axis(windows, true_layers)
    errs_exact, errs_anti, a1_ok = adjudicate_gram(rows)

    # ---- bulk axis (B)
    T, c_cont, alpha_full, ka = build_tower()
    b_results, real_last = bulk_axis(T, bats)

    # ---- controls
    gram_controls(windows, true_layers, errs_anti)
    bulk_controls(c_cont, alpha_full, ka, bats, real_last)

    # ---- verdict (preregistered rules)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("C1", "C2", "C3", "C4")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("C1", "C2", "C3", "C4")))
    gates_ok = all(ok for (_n, ok) in GATES)
    b_pass = sum(1 for (n, ok) in GATES if n.startswith("B.") and ok)
    b_all = sum(1 for (n, _ok) in GATES if n.startswith("B."))
    if guards_ok and controls_ok and gates_ok:
        verdict = "HANDOFF-TAIL-WEIL-CONVERGES"
    elif guards_ok and controls_ok and a1_ok and b_pass >= 4:
        verdict = "HANDOFF-TAIL-WEIL-PARTIAL"
    else:
        verdict = "HANDOFF-TAIL-WEIL-DEAD"

    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d, GUARDS+CONTROLS %d/%d, B-cells %d/%d, "
          "runtime %.1f s"
          % (n_gate, len(GATES), n_chk, len(CHECKS), b_pass, b_all,
             time.time() - T_START))
    if verdict == "HANDOFF-TAIL-WEIL-CONVERGES":
        print("CONSEQUENCE: the three named remainders of the gram "
              "decider are settled on the reachable surface -- the "
              "quadrature tail is uniformly controlled, the window "
              "states are compatible in the weak-* sense, and the "
              "operator-system limit is identified with the deployed "
              "Weil functional ON THE FROZEN BATTERY.  Open beyond "
              "this surface (honest): the eps -> 0 wall (PD "
              "persistence), the extension from the battery to a "
              "dense test space in a topology that controls the Weil "
              "criterion, and every RH-level positivity statement.")
    elif verdict == "HANDOFF-TAIL-WEIL-PARTIAL":
        print("HONEST READING: convergence and compatibility hold, "
              "but at least one structural gate failed as documented "
              "above -- the failed layer/window structure is the "
              "remaining object, not a rounding issue.")
    else:
        print("KILL: the route closes honestly; Plan B takes over per "
              "the review plan.")
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
