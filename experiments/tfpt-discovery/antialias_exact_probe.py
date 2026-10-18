#!/usr/bin/env python3
"""GLOBAL-HANDOFF anti-alias EXACTNESS theorem probe (intended
promotion target v760_antialias_exact).

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, and this probe writes no files.  Pure quadrature theory + the
frozen source symbol; no target matrix (car/cat) is ever built or
compared here.  All random coefficient specifications are SHA-256
frozen BEFORE any array is drawn, and every drawn array is hashed
BEFORE the first evaluation.

QUESTION.  Gate 1 (handoff_fixed_window_resolution_probe) returned
RESOLUTION-BOUNDARY: E_total is invariant under Nf = q(2M+1),
q in {1,2,4,8}, to ~1e-13 on all three fixed windows.  That was an
empirical statement about the 24-function battery.  This probe turns
the anti-alias claim into an EXACT identity valid for ARBITRARY
coefficient vectors of the M-cell space, states the exact degree
arithmetic, and derives the exact minimal frequency count.

SETUP (verbatim from handoff_frequency_gram_probe):
  lattice j in {0..M-1}, test vector u, F_u(theta) = sum_j u_j e^{ij
  theta}; Fejer symbol s(theta) = p_0 + 2 sum_{d=1}^{M-1} (1-d/M) p_d
  cos(d theta), i.e. Fourier coefficients shat(+-d) = (1-d/M) p_d
  (the Fejer map p -> shat is diagonal with strictly positive weights
  (1-d/M) >= 1/M, hence bijective: "arbitrary p" = "arbitrary shat");
  midpoint frequency grid theta_k = 2 pi (k+1/2)/Nf, k = 0..Nf-1;
  Q[k,i] = sqrt(max(s(theta_k),0)/Nf) F_{u_i}(theta_k).  The
  positive-part clip is a PSD convention of the deployed formula; the
  exact identities below concern the UNCLIPPED bilinear quadrature
  (for the true source symbol the measured negative part is numerical
  only, ~ -2e-9, reported).

DERIVATION (frozen BEFORE the first run -- the theorem the probe
tests, with the exact degree arithmetic):
  Discrete orthogonality of the midpoint grid:
    (1/Nf) sum_k e^{i m theta_k} = (-1)^{m/Nf} if Nf | m else 0.
  Every identity below reduces to it.
  (1) DISCRETE PARSEVAL.  (1/Nf) sum_k conj(F_u) F_v at the grid
      equals sum_j u_j v_j (the exact integral) for ARBITRARY u, v
      supported on {0..M-1} iff no nonzero multiple of Nf lies in
      the correlation budget |j'-j| <= M-1, i.e. iff Nf >= M.
  (2) MOMENT RECONSTRUCTION.  The Gram construction needs EXACTLY
      the moments t_d = (1/Nf) sum_k s(theta_k) e^{i d theta_k} for
      |d| <= M-1 (from Q*Q: entries are sums over j, j' of
      u_i[j] u_i'[j'] t_{j'-j}).  The integrand s(theta) e^{i d
      theta} has frequencies m + d, |m| <= M-1 (symbol degree),
      |d| <= M-1 (lattice spread): total budget 2M-2.  Exact alias
      formula (measured must equal it at EVERY Nf):
        t_d = sum_r (-1)^r shat(r Nf - d),
      so t_d = shat(d) exactly iff Nf >= M + |d|.
  (3) NO-ALIAS BOUND.  All Gram cross products are exact for
      arbitrary coefficient vectors iff
        Nf >= (symbol degree) + (max lattice spread) + 1
            = (M-1) + (M-1) + 1 = 2M - 1.
      With restricted test-vector spread S the bound is Nf >= M + S
      (that is why the 24-function battery, spread 209..725 << M-1,
      is comfortably inside at every deployed count).
  (4) EXACT MINIMAL COUNT.  The sharp minimal uniform count for the
      full M-cell coefficient space is Nf_min = 2M - 1, NOT the
      deployed 2M+1: at Nf = 2M-2 the explicit witness p = M e_{M-1}
      (i.e. shat(M-1) = 1), u = e_0, v = e_{M-1} aliases the
      frequency (M-1)+(M-1) = 2M-2 = Nf onto the constant with
      midpoint sign (-1)^1, so the measured moment is
      shat(M-1) - shat(M-1) = 0 instead of 1 (error of magnitude
      exactly |shat(M-1)| = 1).  Every Nf <= 2M-2 admits such a
      witness (choose m + d = Nf with |m|,|d| <= M-1); every
      Nf >= 2M-1 admits none.  The deployed 2M+1 is therefore EXACT
      but NOT minimal -- a DOWNWARD correction of the minimality
      claim, which the frozen enum classifies as ANTIALIAS-CORRECTED
      (kill rule: correct the formula, never patch windows; here the
      correction direction is harmless -- 2M+1 stays exact).

PREREGISTERED GATES (all numbers frozen HERE before the first run):
  G0.1 AST firewall (banned zero/prime tokens);
  G0.2 full specification (windows, Nf ladder, seeds, scan tuples,
       tolerances, verdict order) SHA-256 frozen before any draw or
       comb construction;
  G0.3 every random array hashed before the first evaluation;
  G0.4 frozen source symbol wiring <= WIRE_TOL = 2e-10 (same guard
       as the parent probes);
  I1.1 Parseval exact at Nf in {M, 2M+1}: max rel dev <= EXACT_TOL;
  I1.2 Parseval witness at Nf = M-1 (u = e_0, v = e_{M-1}) fires:
       |measured - exact| >= WITNESS_MIN and equals the alias
       prediction to PREDICT_TOL;
  I2.1 all M-1 moments exact at Nf in {2M-1, 2M, 2M+1}, for the
       random symbol AND the frozen source symbol: <= EXACT_TOL;
  I2.2 exact alias formula: measured moments equal the analytic
       prediction sum_r (-1)^r shat(r Nf - d) at EVERY ladder Nf
       (including the must-fail counts) to PREDICT_TOL;
  I3.1 Gram identity: unclipped quadrature Gram equals the exact
       Toeplitz form U^T T U (T[j,j'] = shat(j-j')) at Nf in
       {2M-1, 2M+1}, for random symbol x 24 arbitrary random vectors
       AND source symbol x frozen 24-function battery: <= EXACT_TOL;
  I3.2 Gram invariance across Nf in {2M-1, 2M, 2M+1} <= EXACT_TOL
       (the exact-identity explanation of Gate 1's q-invariance);
  I4.1 designed must-fail witness at Nf = 2M-2 fires: error
       magnitude >= WITNESS_MIN (designed value 1) and matches the
       prediction to PREDICT_TOL;
  I4.2 the SAME designed configuration is exact at Nf = 2M-1
       (threshold boundary passes): <= EXACT_TOL;
  I4.3 deep-fail Nf = M (random symbol): max moment deviation
       >= WITNESS_MIN and matches the prediction;
  I4.4 budget-formula scan over frozen (ds, S) tuples: exact at
       Nf = ds+S+1 (<= EXACT_TOL, random coefficients with spread
       exactly S), designed witness fires at Nf = ds+S (error
       = -c_ds to PREDICT_TOL).
  Tolerances (frozen): EXACT_TOL = 1e-11 (relative), PREDICT_TOL =
  1e-11 (relative), WITNESS_MIN = 1e-3 (relative).

VERDICT ENUM (frozen order, decided after all gates):
  ANTIALIAS-EXACT      = all identity gates pass, witnesses fire,
                         AND the derived minimal count equals the
                         claimed 2M+1;
  ANTIALIAS-CORRECTED  = all identity gates pass, witnesses fire,
                         but the derived sharp minimal count differs
                         from 2M+1 -- the corrected count is stated
                         (expected from the derivation: 2M-1; the
                         deployed 2M+1 remains exact/sufficient);
  ANTIALIAS-DEAD       = some exactness identity fails at every
                         finite tested count or a must-fail witness
                         does not fire (not expected, but frozen).

STOP-LIST (binding, inherited from the round): no fits; no target
data (no car/cat/Weil matrix anywhere); no Riemann zeros; every
random specification hashed before evaluation; NO RH claim; probe
writes no files; runtime minutes.

RESULTS (2026-08-04, first preregistered run, 7.8 s; ALL 14 GUARDS
PASSED, verdict ANTIALIAS-CORRECTED):
  *  Exactness for ARBITRARY coefficients at the sharp count 2M-1 and
     the deployed 2M+1 on all three windows: Parseval <= 2.0e-14, all
     2M-1 lattice moments (random + frozen source symbol) <= 3.5e-13
     relative, Gram identity vs the exact Toeplitz form <= 5.9e-13
     relative, Gram invariance across {2M-1, 2M, 2M+1} <= 7.3e-13 --
     the exact-identity explanation of Gate 1's q-invariance.
  *  Exact alias formula t_d = sum_r (-1)^r shat(r Nf - d) verified at
     EVERY ladder count including the must-fail ones: max deviation
     6.4e-13 relative over all 30 (window, Nf, symbol) grids.
  *  Witnesses fire exactly as derived: the designed witness at
     Nf = 2M-2 measures ~1e-24 instead of 1 (error 1.000000, matching
     the alias prediction 0) on all three windows, and the SAME
     configuration is exact at 2M-1 (<= 2.2e-13); the Parseval witness
     at Nf = M-1 measures -1 (error 1.0); deep-fail Nf = M has max
     moment error 1.0 (random) and 0.24/0.20/0.17 (source symbol),
     all matching the alias formula.
  *  Budget formula Nf_min = ds + S + 1 confirmed on all four frozen
     (ds, S) tuples: exact at ds+S+1 (<= 4.9e-14), witness error
     exactly |c_ds| = 1 at ds+S.
  *  The frozen source symbol is strictly positive on every tested
     grid (min +1.7e-2 / +8.7e-3 / +7.4e-3), so the positive-part
     clip is inactive here and the unclipped identity IS the deployed
     construction on these windows.
  *  DERIVED DEGREE BUDGET for the Gram construction: symbol degree
     (M-1) + lattice spread (M-1) = 2M-2, sharp minimal count
     Nf_min = 2M-1 (spread-S version: Nf_min = M+S; measured battery
     spreads 209/371/725 give battery-sufficient counts
     577/1583/3591).  The deployed 2M+1 is EXACT but NOT minimal:
     the minimality claim is corrected DOWNWARD by 2; every deployed
     number is untouched, no window is patched.  Lean counterpart:
     experiments/lean4-carrier-rigidity/TfptCarrier/AntiAliasExact.lean
     (discrete orthogonality, offset-invariant exact quadrature,
     Parseval, moment reconstruction, threshold witness, midpoint
     alias sign).  NO RH claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/antialias_exact_probe.py
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

import moonshot_arch_glue_probe as glue  # noqa: E402
import handoff_frequency_gram_probe as gp  # noqa: E402

T_START = time.time()
TWO_PI = 2.0 * math.pi

# ------------------------------------------------ preregistered bars
WINDOW_HS = (184, 606, 1433)      # fixed windows (h = M//2), family 0/2/4
N_VECTORS = 24                    # arbitrary random coefficient vectors
RNG_SEED = 76001
EXACT_TOL = 1.0e-11               # relative exactness bar
PREDICT_TOL = 1.0e-11             # measured-vs-alias-formula bar
WITNESS_MIN = 1.0e-3              # relative witness floor (designed: 1)
WIRE_TOL = 2.0e-10                # source-symbol wiring (parent guard)
BUDGET_SCAN = ((7, 4), (16, 16), (33, 10), (95, 60))   # (ds, S) tuples
CHUNK = 256

# Nf ladder per window: label -> Nf(M).  Frozen order.
NF_LADDER = (("2M+1", lambda M: 2 * M + 1),   # deployed count
             ("2M",   lambda M: 2 * M),       # sufficient
             ("2M-1", lambda M: 2 * M - 1),   # derived sharp minimum
             ("2M-2", lambda M: 2 * M - 2),   # one below: must fail
             ("M",    lambda M: M))           # deep fail: generic alias
EXACT_LABELS = ("2M+1", "2M", "2M-1")
VERDICT_ORDER = ("ANTIALIAS-EXACT", "ANTIALIAS-CORRECTED",
                 "ANTIALIAS-DEAD")

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


def freeze_specification():
    """SHA-256-freeze the full probe specification BEFORE any draw."""
    spec = dict(version="antialias-exact-v1",
                windows_h=list(WINDOW_HS),
                n_vectors=N_VECTORS,
                rng_seed=RNG_SEED,
                nf_ladder=[label for (label, _fn) in NF_LADDER],
                nf_formula="midpoint theta_k = 2pi(k+1/2)/Nf",
                budget_scan=[list(t) for t in BUDGET_SCAN],
                draw_order="per window ascending h: p_random(M), "
                           "U(M,%d) unit columns; then per (ds,S): "
                           "c(ds+1) with c[ds]:=1, u(S+1), v(S+1); "
                           "all standard_normal" % N_VECTORS,
                designed_witness="p = M*e_{M-1} (shat(M-1)=1), "
                                 "u=e_0, v=e_{M-1}, at Nf=2M-2",
                exact_tol=EXACT_TOL, predict_tol=PREDICT_TOL,
                witness_min=WITNESS_MIN, wire_tol=WIRE_TOL,
                battery_hash=gp.BATTERY_SPEC_HASH,
                claimed_min="2M+1", derived_min="2M-1",
                verdict_order=list(VERDICT_ORDER))
    blob = json.dumps(spec, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def draw_random(windows):
    """Draw all random arrays in the frozen order; hash BEFORE use."""
    rng = np.random.default_rng(RNG_SEED)
    digest = hashlib.sha256()
    per_window = []
    for window in windows:
        M = window["M"]
        p_random = rng.standard_normal(M)
        U = rng.standard_normal((M, N_VECTORS))
        U /= np.linalg.norm(U, axis=0, keepdims=True)
        digest.update(np.ascontiguousarray(p_random).tobytes())
        digest.update(np.ascontiguousarray(U).tobytes())
        per_window.append((p_random, U))
    scan_draws = []
    for (ds, S) in BUDGET_SCAN:
        c = rng.standard_normal(ds + 1)
        c[ds] = 1.0                      # frozen: exact witness coefficient
        u = rng.standard_normal(S + 1)
        v = rng.standard_normal(S + 1)
        digest.update(np.ascontiguousarray(c).tobytes())
        digest.update(np.ascontiguousarray(u).tobytes())
        digest.update(np.ascontiguousarray(v).tobytes())
        scan_draws.append((c, u, v))
    return per_window, scan_draws, digest.hexdigest()


# ---------------------------------------------------- quadrature core
def midpoint_grid(count):
    return TWO_PI * (np.arange(count) + 0.5) / count


def fejer_coefficients(p):
    """shat(d) = (1-d/M) p_d, shat(0) = p_0 (real even symbol)."""
    M = len(p)
    weights = 1.0 - np.arange(M) / M
    coefficients = weights * np.asarray(p, float)
    coefficients[0] = float(p[0])
    return coefficients


def symbol_on_grid(coefficients, theta):
    """s(theta) = c_0 + 2 sum_{d>=1} c_d cos(d theta), chunked."""
    degree = np.arange(1, len(coefficients))
    out = np.full(len(theta), float(coefficients[0]))
    for start in range(0, len(theta), CHUNK):
        block = theta[start:start + CHUNK]
        out[start:start + CHUNK] += 2.0 * (
            np.cos(np.outer(block, degree)) @ coefficients[1:])
    return out


def measured_moments(coefficients, count, dmax):
    """t_d = (1/Nf) sum_k s(theta_k) e^{i d theta_k}, d=-dmax..dmax,
    by the literal quadrature sum (chunked)."""
    theta = midpoint_grid(count)
    values = symbol_on_grid(coefficients, theta)
    d_vec = np.arange(-dmax, dmax + 1)
    moments = np.zeros(len(d_vec), dtype=complex)
    for start in range(0, count, CHUNK):
        block = theta[start:start + CHUNK]
        moments += np.exp(1j * np.outer(d_vec, block)) \
            @ values[start:start + CHUNK]
    return d_vec, moments / count


def predicted_moments(coefficients, count, d_vec):
    """Exact alias formula t_d = sum_r (-1)^r shat(r Nf - d)."""
    degree = len(coefficients) - 1

    def shat(m):
        m = abs(int(m))
        return float(coefficients[m]) if m <= degree else 0.0

    r_max = (degree + int(np.max(np.abs(d_vec)))) // count + 1
    out = np.zeros(len(d_vec))
    for index, d in enumerate(d_vec):
        total = 0.0
        for r in range(-r_max, r_max + 1):
            total += (-1.0) ** r * shat(r * count - int(d))
        out[index] = total
    return out


def gram_quadrature(coefficients, vectors, count):
    """Unclipped quadrature Gram sum_k (s_k/Nf) conj(F_i) F_i'."""
    M = vectors.shape[0]
    theta = midpoint_grid(count)
    values = symbol_on_grid(coefficients, theta)
    lattice = np.arange(M)
    gram = np.zeros((vectors.shape[1], vectors.shape[1]), dtype=complex)
    for start in range(0, count, CHUNK):
        block = theta[start:start + CHUNK]
        fourier = np.exp(1j * np.outer(block, lattice)) @ vectors
        gram += (fourier.conj().T
                 * (values[start:start + CHUNK] / count)) @ fourier
    return gram


def gram_exact(coefficients, vectors):
    """Exact integral Gram = U^T T U, T[j,j'] = shat(j-j')."""
    toeplitz = sla.toeplitz(coefficients)
    return vectors.T @ toeplitz @ vectors


def parseval_quadrature(vectors, count):
    return gram_quadrature(np.array([1.0]), vectors, count)


def moment_single(coefficients, count, d):
    theta = midpoint_grid(count)
    values = symbol_on_grid(coefficients, theta)
    return complex(np.mean(values * np.exp(1j * d * theta)))


def battery_spread(full_battery):
    """Max lattice spread max_j - min_j over nonzero battery support."""
    nonzero = np.abs(full_battery) > 0.0
    rows = np.where(nonzero.any(axis=1))[0]
    return int(rows.max() - rows.min())


# --------------------------------------------------------------- run
def run():
    print("=" * 78)
    print("GLOBAL HANDOFF -- anti-alias EXACTNESS theorem probe "
          "(target v760_antialias_exact)")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    spec_hash = freeze_specification()
    check("G0.2 full specification frozen BEFORE any draw",
          len(spec_hash) == 64,
          "spec SHA256 %s..., battery SHA256 %s..."
          % (spec_hash[:16], gp.BATTERY_SPEC_HASH[:16]))

    # ---- windows + frozen source symbol (source side only)
    family = glue.declared_family()
    windows = [w for w in family if w["M"] // 2 in WINDOW_HS]
    maximum = int(max(math.exp(2.0 * w["alpha"]) for w in windows) + 0.5)
    comb, _metadata = gp.source_comb(maximum)
    true_layers = [gp.build_true_source_layers(w, comb) for w in windows]
    wiring = 0.0
    for window, layers in zip(windows, true_layers):
        assembled = layers["arch"] + layers["atom"] + layers["pole"]
        wiring = max(wiring, float(np.max(np.abs(assembled - window["p"]))
                                   / np.max(np.abs(window["p"]))))
    check("G0.4 frozen source symbol wiring", wiring <= WIRE_TOL,
          "max rel deviation %.3e" % wiring)

    per_window, scan_draws, draw_hash = draw_random(windows)
    check("G0.3 all random draws hashed before evaluation", True,
          "draw SHA256 %s..." % draw_hash[:16])

    gate = {key: True for key in
            ("I1.1", "I1.2", "I2.1", "I2.2", "I3.1", "I3.2",
             "I4.1", "I4.2", "I4.3", "I4.4")}
    stats = dict(parseval_exact=0.0, parseval_witness=[],
                 moment_exact=0.0, predict_dev=0.0, gram_exact=0.0,
                 gram_invariance=0.0, witness_designed=[],
                 witness_boundary=0.0, deep_fail=[], scan_exact=0.0,
                 scan_witness=[], battery_spreads=[])

    for (window, layers, (p_random, U)) in zip(windows, true_layers,
                                               per_window):
        M = window["M"]
        h = M // 2
        p_source = layers["arch"] + layers["atom"] + layers["pole"]
        c_random = fejer_coefficients(p_random)
        c_source = fejer_coefficients(p_source)
        _free, full_battery, _bhash = gp.sampled_battery(M, window["D"])
        spread = battery_spread(full_battery)
        stats["battery_spreads"].append(spread)
        print("\n-- window h=%d M=%d: battery spread=%d "
              "(battery-sufficient count M+S=%d), derived sharp "
              "minimum 2M-1=%d, deployed 2M+1=%d"
              % (h, M, spread, M + spread, 2 * M - 1, 2 * M + 1))
        print("   source symbol min on 2M+1 grid: %.3e (clip "
              "convention affects only this numerical negativity)"
              % float(np.min(symbol_on_grid(
                  c_source, midpoint_grid(2 * M + 1)))))

        # ---- I1 discrete Parseval (s == 1), arbitrary vectors
        exact_pars = U.T @ U
        scale_pars = float(np.max(np.abs(exact_pars)))
        for count in (M, 2 * M + 1):
            quad = parseval_quadrature(U, count)
            dev = float(np.max(np.abs(quad - exact_pars))) / scale_pars
            stats["parseval_exact"] = max(stats["parseval_exact"], dev)
            gate["I1.1"] &= dev <= EXACT_TOL
            print("   I1.1 Parseval Nf=%-5d max rel dev = %.3e"
                  % (count, dev))
        # Parseval witness at Nf = M-1: u=e_0, v=e_{M-1} -> the
        # correlation frequency M-1 = Nf aliases to the constant with
        # midpoint sign -1: measured -1, exact 0.
        witness = moment_single(np.array([1.0]), M - 1, M - 1)
        w_err = abs(witness - 0.0)
        w_dev = abs(witness - (-1.0))
        stats["parseval_witness"].append((h, witness.real, w_dev))
        gate["I1.2"] &= (w_err >= WITNESS_MIN and w_dev <= PREDICT_TOL)
        print("   I1.2 Parseval witness Nf=M-1: measured %+.6f "
              "(predicted -1), |dev| = %.3e" % (witness.real, w_dev))

        # ---- I2 moment reconstruction + exact alias formula
        for label, nf_of in NF_LADDER:
            count = nf_of(M)
            for tag, coefficients in (("random", c_random),
                                      ("source", c_source)):
                d_vec, measured = measured_moments(coefficients, count,
                                                   M - 1)
                predicted = predicted_moments(coefficients, count, d_vec)
                scale = float(np.max(np.abs(coefficients)))
                dev_pred = float(np.max(np.abs(measured - predicted))) \
                    / scale
                stats["predict_dev"] = max(stats["predict_dev"], dev_pred)
                gate["I2.2"] &= dev_pred <= PREDICT_TOL
                exact = np.array([coefficients[abs(int(d))]
                                  for d in d_vec])
                dev_exact = float(np.max(np.abs(measured - exact))) \
                    / scale
                if label in EXACT_LABELS:
                    stats["moment_exact"] = max(stats["moment_exact"],
                                                dev_exact)
                    gate["I2.1"] &= dev_exact <= EXACT_TOL
                if label == "M" and tag == "random":
                    stats["deep_fail"].append((h, dev_exact, dev_pred))
                    gate["I4.3"] &= (dev_exact >= WITNESS_MIN
                                     and dev_pred <= PREDICT_TOL)
                print("   I2  %-6s Nf=%-5d (%s): |t_d - shat(d)| max "
                      "= %.3e rel, |t_d - alias formula| max = %.3e rel"
                      % (label, count, tag, dev_exact, dev_pred))

        # ---- I3 Gram identity + invariance, arbitrary vectors
        grams = {}
        for tag, coefficients, vectors in (
                ("random-U", c_random, U),
                ("source-battery", c_source, full_battery)):
            exact = gram_exact(coefficients, vectors)
            scale = max(float(sla.norm(exact, 2)), 1.0e-300)
            collected = {}
            for label in EXACT_LABELS:
                count = dict((lab, fn) for lab, fn in NF_LADDER)[
                    label](M)
                quad = gram_quadrature(coefficients, vectors, count)
                dev = float(sla.norm(quad - exact, 2)) / scale
                collected[label] = quad
                if label in ("2M-1", "2M+1"):
                    stats["gram_exact"] = max(stats["gram_exact"], dev)
                    gate["I3.1"] &= dev <= EXACT_TOL
                print("   I3.1 Gram %-14s Nf=%-5s rel spectral dev "
                      "= %.3e" % (tag, label, dev))
            inv = max(float(sla.norm(collected[a] - collected[b], 2))
                      / scale
                      for a in EXACT_LABELS for b in EXACT_LABELS)
            stats["gram_invariance"] = max(stats["gram_invariance"], inv)
            gate["I3.2"] &= inv <= EXACT_TOL
            grams[tag] = inv
        print("   I3.2 Gram invariance across {2M-1,2M,2M+1}: "
              "max rel %.3e" % max(grams.values()))

        # ---- I4 designed must-fail witness at Nf = 2M-2 and its
        #      boundary at 2M-1 (p = M e_{M-1} -> shat(M-1) = 1;
        #      Gram entry (e_0, e_{M-1}) IS the moment t_{M-1})
        c_witness = np.zeros(M)
        c_witness[M - 1] = 1.0            # shat after the Fejer map
        measured_fail = moment_single(c_witness, 2 * M - 2, M - 1)
        err_fail = abs(measured_fail - 1.0)      # exact value is 1
        dev_fail = abs(measured_fail - 0.0)      # alias prediction: 0
        stats["witness_designed"].append((h, err_fail, dev_fail))
        gate["I4.1"] &= (err_fail >= WITNESS_MIN
                         and dev_fail <= PREDICT_TOL)
        measured_ok = moment_single(c_witness, 2 * M - 1, M - 1)
        err_ok = abs(measured_ok - 1.0)
        stats["witness_boundary"] = max(stats["witness_boundary"],
                                        err_ok)
        gate["I4.2"] &= err_ok <= EXACT_TOL
        print("   I4  designed witness shat(M-1)=1: Nf=2M-2 measured "
              "%+.3e (exact 1, alias-predicted 0, error %.6f); "
              "Nf=2M-1 measured %+.6f (dev %.3e)"
              % (measured_fail.real, err_fail, measured_ok.real,
                 err_ok))

    # ---- I4.4 budget-formula scan: Nf_min(ds, S) = ds + S + 1
    print("\n-- budget-formula scan Nf_min = ds + S + 1 "
          "(frozen tuples, arbitrary coefficients)")
    for ((ds, S), (c, u, v)) in zip(BUDGET_SCAN, scan_draws):
        vectors = np.column_stack([u, v])            # lattice 0..S
        column = np.array([float(c[d]) if d <= ds else 0.0
                           for d in range(S + 1)])
        exact = vectors.T @ sla.toeplitz(column) @ vectors
        scale = max(float(sla.norm(exact, 2)), 1.0e-300)
        quad = gram_quadrature(c, vectors, ds + S + 1)
        dev = float(sla.norm(quad - exact, 2)) / scale
        stats["scan_exact"] = max(stats["scan_exact"], dev)
        gate["I4.4"] &= dev <= EXACT_TOL
        # designed witness at Nf = ds + S: u=e_0, v=e_S -> the Gram
        # entry is the moment t_S; frequency ds + S = Nf aliases with
        # midpoint sign -1 and coefficient c[ds] = 1:
        # measured = shat(-S)|_{S<=ds} - c[ds].
        witness = moment_single(c, ds + S, S)
        true_value = float(c[S]) if S <= ds else 0.0
        predicted = true_value - float(c[ds])
        w_err = abs(witness - true_value)
        w_dev = abs(witness - predicted)
        stats["scan_witness"].append((ds, S, w_err, w_dev))
        gate["I4.4"] &= (w_err >= WITNESS_MIN and w_dev <= PREDICT_TOL)
        print("   (ds=%-3d S=%-3d) exact at Nf=%-4d: rel dev %.3e; "
              "witness at Nf=%-4d: error %.6f (predicted %.6f, dev "
              "%.3e)" % (ds, S, ds + S + 1, dev, ds + S, w_err,
                         abs(predicted - true_value), w_dev))

    # ---- gates
    print()
    check("I1.1 discrete Parseval exact at Nf in {M, 2M+1}",
          gate["I1.1"], "max rel dev %.3e" % stats["parseval_exact"])
    check("I1.2 Parseval witness fires at Nf = M-1", gate["I1.2"],
          "errors %s" % "/".join("%.3f" % abs(w[1])
                                 for w in stats["parseval_witness"]))
    check("I2.1 all M-1 moments exact at Nf in {2M-1, 2M, 2M+1}",
          gate["I2.1"], "max rel dev %.3e" % stats["moment_exact"])
    check("I2.2 exact alias formula at EVERY ladder Nf", gate["I2.2"],
          "max rel dev %.3e" % stats["predict_dev"])
    check("I3.1 Gram identity exact at Nf in {2M-1, 2M+1}",
          gate["I3.1"], "max rel spectral dev %.3e"
          % stats["gram_exact"])
    check("I3.2 Gram invariance across {2M-1, 2M, 2M+1}",
          gate["I3.2"], "max rel %.3e" % stats["gram_invariance"])
    check("I4.1 designed must-fail witness fires at Nf = 2M-2",
          gate["I4.1"], "errors %s"
          % "/".join("%.6f" % w[1] for w in stats["witness_designed"]))
    check("I4.2 designed configuration exact at Nf = 2M-1",
          gate["I4.2"], "max dev %.3e" % stats["witness_boundary"])
    check("I4.3 deep-fail Nf = M fires and matches prediction",
          gate["I4.3"], "errors %s"
          % "/".join("%.3f" % w[1] for w in stats["deep_fail"]))
    check("I4.4 budget formula Nf_min = ds + S + 1 on all tuples",
          gate["I4.4"], "max exact dev %.3e, witness errors %s"
          % (stats["scan_exact"],
             "/".join("%.3f" % w[2] for w in stats["scan_witness"])))

    # ---- preregistered verdict
    guards_ok = all(ok for (_name, ok) in CHECKS)
    identities_ok = all(gate.values())
    derived_equals_claimed = False        # derived 2M-1 != claimed 2M+1
    if guards_ok and identities_ok and derived_equals_claimed:
        verdict = "ANTIALIAS-EXACT"
    elif guards_ok and identities_ok:
        verdict = "ANTIALIAS-CORRECTED"
    else:
        verdict = "ANTIALIAS-DEAD"

    print("\nVERDICT: %s" % verdict)
    print("DERIVED DEGREE BUDGET: symbol degree (M-1) + lattice spread "
          "(M-1) = 2M-2; sharp minimal uniform count Nf_min = 2M-1; "
          "spread-S version Nf_min = M+S (battery spreads %s -> "
          "battery-sufficient counts %s)."
          % ("/".join(str(s) for s in stats["battery_spreads"]),
             "/".join(str(w["M"] + s) for w, s in
                      zip(windows, stats["battery_spreads"]))))
    if verdict == "ANTIALIAS-CORRECTED":
        print("CONSEQUENCE: the anti-alias identity is EXACT for "
              "ARBITRARY coefficient vectors at every Nf >= 2M-1 -- "
              "this upgrades Gate 1's battery-level q-invariance to an "
              "exact theorem of the M-cell space.  The minimality claim "
              "'Nf = 2M+1 is minimal' is corrected DOWNWARD: the sharp "
              "minimum is Nf_min = 2M-1, and Nf = 2M-2 admits the "
              "explicit witness p = M e_{M-1}, u = e_0, v = e_{M-1}.  "
              "The deployed count 2M+1 stays exact; no deployed number "
              "changes; no window is patched.  NO RH claim.")
    elif verdict == "ANTIALIAS-EXACT":
        print("CONSEQUENCE: all four identities proved and 2M+1 is the "
              "sharp minimum.  NO RH claim.")
    else:
        print("KILL: an exactness identity or witness failed; the "
              "anti-alias closure does NOT hold for arbitrary "
              "coefficients as derived.  NO RH claim.")

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
