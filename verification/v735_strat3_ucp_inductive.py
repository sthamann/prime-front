#!/usr/bin/env python3
"""v735 -- PRIME.UCPLIMIT.01: STRATEGY-3 / L1 -- covariant UCP maps
along the nine-window GNS ladder (the state-transport route, honestly
closed).

No RH claim.

Scope, stated sharply
---------------------
For each window let J_h be its real Jacobi/GNS shift truncation.  Its simple
spectrum identifies the generated finite C*-algebra

    S_h = C*(J_h, 1) = C^h.

This is the maximal commutative spectral algebra of the measured GNS shift,
not the full noncommutative groupoid crossed product.  A UCP map
C^h -> C^h' is exactly a row-stochastic nonnegative matrix K.  Its
state-preservation equation is w' K = w.  Thus the Choi SDP reduces exactly
to a finite transport LP.  For the squared one-dimensional generator cost,
the monotone quantile coupling is an optimizer; no unavailable SDP package
and no projected-gradient approximation is needed.

The map is

    Phi(f)_j = sum_i K[j,i] f_i,

where the coupling has source marginal w and target marginal w'.  We test:
  * unitality, Choi positivity and normalized-state preservation;
  * optimal RMS covariance defects for the Jacobi shift x=2cos(D tau) and
    the physical grade generator tau;
  * channel covariance on a fixed polynomial/trigonometric battery;
  * phase covariance for t={0.005,0.01,0.02};
  * Choi rank (number of positive diagonal entries of the canonical
    measure-and-prepare Choi matrix);
  * distance from deterministic nearest-node compression, and
    multiplicativity defects (needed before a C*- rather than merely an
    operator-system limit can be claimed).

Preregistered verdict
---------------------
UCP-DEAD:
  any adjacent map fails UCP/state preservation at 1e-11, requires forbidden
  spectral-target input, or Choi rank grows faster than h^1.25 / exceeds the
  sharp transport bound h+h'-1.
UCP-CONVERGES:
  the maximum normalized shift/grade/phase defect has log-log slope < -0.25,
  final error < 0.70 of the first, and the last three steps decrease.
UCP-STAGNATES:
  maps exist with controlled Choi rank, but the covariance criterion fails.

Even UCP-CONVERGES gives canonically an operator-system inductive-limit
candidate.  A fixed C*-object additionally requires asymptotic
multiplicativity or a compatible C*-envelope theorem.  Neither outcome proves
L1 positivity on the critical line.

The construction path loads no zero ordinates and no prime table.  No file is
written.

RESULTS (10/10 construction checks PASS, verdict UCP-STAGNATES):
  S1: all eight adjacent maps exist exactly as UCP quantile couplings --
    unitality/state preservation to <= 3.1e-12 / 1.2e-15, Choi minimum 0,
    every rank inside the sharp transport bound h+h'-1.
  S2.1 PASS (UCP and state exact), S2.2 PASS (Choi ranks
    344/546/831/1093/1483/1904/2282/2688, log-log slope 0.991 vs bar
    1.25 -- LINEARLY controlled sparse-transport ranks), S2.3 the
    preregistered covariance gate FAILS HONESTLY (aggregate errors
    0.797/0.874/0.811/0.475/1.558/0.882/1.227/0.058: slope -0.487 but
    tail not decreasing -- no monotone shift/grade covariance
    convergence).
  S3: the optimal maps are quantile Markov/conditional-expectation
    couplings on a common [0,1] refinement -- NOT nearest-node
    compressions and NOT *-homomorphisms (nonzero multiplicativity
    defects); direct-vs-composed battery defects ~ 5e-3..8e-3.
  KILL/STOP: mere state transport is NOT the missing L1 mechanism; UCP
  maps alone yield an operator-system limit, not automatically a
  C*-inductive limit; the full noncommutative groupoid algebra was not
  tested.  This closes the L1 route portfolio honestly: Sonin transfer
  dead (v732), UCP stagnates (v735), Gate 0 weak functor (v733), Suzuki
  bridge a measurement (v734).

PROVENANCE: discovery probe strat3_ucp_inductive_probe.py (2026-08-03,
10/10 construction checks, verdict UCP-STAGNATES: the state-transport
maps exist exactly as UCP quantile couplings with linearly controlled
Choi rank (slope 0.991), but the shift covariance does not converge
monotonically -- the preregistered gate fails honestly).  Promoted
verbatim (the sibling import now points at the promoted v718 module);
numbers unchanged.
"""

import ast
import math
import os
import sys
import time

import numpy as np
import scipy.sparse as sps

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import v718_moonshot_spectral as spectral  # noqa: E402


STATE_TOL = 1.0e-11
CHOI_TOL = 1.0e-15
RANK_SLOPE_BAR = 1.25
CONV_SLOPE_BAR = -0.25
CONV_RATIO_BAR = 0.70
PHASE_TIMES = (0.005, 0.01, 0.02)
BATTERY_PHASES = (0.01, 0.03)
BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []
FAILS = []


def check(name, ok, detail=""):
    CHECKS.append(name)
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def outcome(name, ok, detail=""):
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


def gns_measures():
    rows = []
    for window in spectral.family_ext():
        h = window["M"] // 2
        tau, weights, bad_depth, reconstruction = spectral.gns_nodes(
            window["p"], h, window["D"])
        if bad_depth is not None:
            raise RuntimeError("GNS breakdown h=%d depth=%s"
                               % (h, bad_depth))
        state = weights / float(np.sum(weights))
        x = 2.0 * np.cos(window["D"] * tau)
        rows.append(dict(h=h, D=window["D"], tau=tau, x=x, state=state,
                         reconstruction=reconstruction,
                         raw_mass=float(np.sum(weights))))
    return rows


def monotone_coupling(source, target):
    """Sparse optimal 1D coupling using overlaps of quantile intervals."""
    source = np.asarray(source, dtype=np.longdouble)
    target = np.asarray(target, dtype=np.longdouble)
    source = source / np.sum(source)
    target = target / np.sum(target)
    source_edges = np.concatenate(([np.longdouble(0.0)],
                                   np.cumsum(source)))
    target_edges = np.concatenate(([np.longdouble(0.0)],
                                   np.cumsum(target)))
    source_edges[-1] = target_edges[-1] = np.longdouble(1.0)

    ii = []
    jj = []
    mass = []
    i = j = 0
    while i < len(source) and j < len(target):
        overlap = min(source_edges[i + 1], target_edges[j + 1]) \
            - max(source_edges[i], target_edges[j])
        if overlap > np.longdouble(0.0):
            ii.append(i)
            jj.append(j)
            mass.append(float(overlap))
        if source_edges[i + 1] <= target_edges[j + 1]:
            i += 1
        else:
            j += 1
    return np.asarray(ii, int), np.asarray(jj, int), np.asarray(mass, float)


def ucp_map(source, target):
    i, j, mass = monotone_coupling(source["state"], target["state"])
    data = mass / target["state"][j]
    K = sps.csr_matrix((data, (j, i)),
                       shape=(target["h"], source["h"]))
    return K, i, j, mass


def weighted_l2(values, weights):
    return math.sqrt(max(0.0, float(np.dot(weights,
                                           np.abs(values) ** 2))))


def normalized_transport_error(gs, gt, i, j, mass):
    scale = math.sqrt(0.5 * (float(np.dot(mass, gs[i] ** 2))
                             + float(np.dot(mass, gt[j] ** 2))))
    error = math.sqrt(float(np.dot(mass, (gs[i] - gt[j]) ** 2)))
    return error / max(scale, 1.0e-300)


def phase_transport_error(ts, tt, i, j, mass):
    errors = []
    for flow_time in PHASE_TIMES:
        delta = np.exp(1j * flow_time * ts[i]) \
            - np.exp(1j * flow_time * tt[j])
        errors.append(math.sqrt(float(np.dot(mass,
                                              np.abs(delta) ** 2))))
    return max(errors), errors


def bounded_battery(row):
    x = row["x"]
    tau = row["tau"]
    tau_scale = math.sqrt(float(np.dot(row["state"], tau * tau)))
    z = tau / max(tau_scale, 1.0e-300)
    battery = [
        np.ones(row["h"]),
        x / 2.0,
        (x / 2.0) ** 2,
        (x / 2.0) ** 3,
        z,
        z * z,
    ]
    for phase in BATTERY_PHASES:
        battery.append(np.cos(phase * tau))
        battery.append(np.sin(phase * tau))
    return battery


def state_battery_error(K, source, target):
    errors = []
    for values in bounded_battery(source):
        left = np.dot(target["state"], K @ values)
        right = np.dot(source["state"], values)
        errors.append(abs(float(left - right)))
    return max(errors)


def channel_covariance_error(K, source, target, generator):
    gs = source[generator]
    gt = target[generator]
    pooled = math.sqrt(0.5 * (float(np.dot(source["state"], gs * gs))
                              + float(np.dot(target["state"], gt * gt))))
    gs = gs / max(pooled, 1.0e-300)
    gt = gt / max(pooled, 1.0e-300)
    errors = []
    for values in bounded_battery(source):
        image = K @ values
        defect = K @ (gs * values) - gt * image
        denominator = max(weighted_l2(image, target["state"]), 1.0)
        errors.append(weighted_l2(defect, target["state"]) / denominator)
    return max(errors)


def multiplicativity_defect(K, source, target, generator):
    values = source[generator]
    scale = math.sqrt(float(np.dot(source["state"], values * values)))
    values = values / max(scale, 1.0e-300)
    image = K @ values
    variance = K @ (values * values) - image * image
    variance = np.maximum(variance, 0.0)
    return math.sqrt(max(0.0, float(np.dot(target["state"], variance))))


def nearest_compression_diagnostics(K, source, target):
    tau_s = source["tau"]
    tau_t = target["tau"]
    insertion = np.searchsorted(tau_s, tau_t)
    right = np.clip(insertion, 0, len(tau_s) - 1)
    left = np.clip(insertion - 1, 0, len(tau_s) - 1)
    nearest = np.where(np.abs(tau_t - tau_s[left])
                       <= np.abs(tau_t - tau_s[right]), left, right)
    induced = np.bincount(nearest, weights=target["state"],
                          minlength=source["h"])
    state_tv = 0.5 * float(np.sum(np.abs(induced - source["state"])))

    coo = K.tocoo()
    row_max = np.zeros(target["h"])
    row_argmax = np.zeros(target["h"], dtype=int)
    for row, col, value in zip(coo.row, coo.col, coo.data):
        if value > row_max[row]:
            row_max[row] = value
            row_argmax[row] = col
    deterministic_mass = float(np.dot(target["state"],
                                      row_max >= 1.0 - 1.0e-12))
    nearest_agreement = float(np.dot(
        target["state"], row_argmax == nearest))
    return state_tv, deterministic_mass, nearest_agreement


def adjacent_measure(source, target):
    K, i, j, mass = ucp_map(source, target)
    unital = float(np.max(np.abs(K @ np.ones(source["h"]) - 1.0)))
    marginal = np.asarray(target["state"] @ K).ravel()
    state_full = float(np.max(np.abs(marginal - source["state"])))
    state_battery = state_battery_error(K, source, target)
    min_choi = min(0.0, float(np.min(K.data))) if K.nnz else 0.0
    choi_rank = int(np.sum(K.data > CHOI_TOL))
    sharp_rank_bound = source["h"] + target["h"] - 1

    x_opt = normalized_transport_error(source["x"], target["x"],
                                       i, j, mass)
    tau_opt = normalized_transport_error(source["tau"], target["tau"],
                                         i, j, mass)
    phase_max, phase_each = phase_transport_error(
        source["tau"], target["tau"], i, j, mass)
    channel_x = channel_covariance_error(K, source, target, "x")
    channel_tau = channel_covariance_error(K, source, target, "tau")
    mult_x = multiplicativity_defect(K, source, target, "x")
    mult_tau = multiplicativity_defect(K, source, target, "tau")
    near_tv, deterministic, near_agreement = \
        nearest_compression_diagnostics(K, source, target)
    aggregate = max(x_opt, tau_opt, phase_max, channel_x, channel_tau)
    return dict(K=K, source_h=source["h"], target_h=target["h"],
                unital=unital, state_full=state_full,
                state_battery=state_battery, min_choi=min_choi,
                choi_rank=choi_rank, rank_bound=sharp_rank_bound,
                x_opt=x_opt, tau_opt=tau_opt, phase_max=phase_max,
                phase_each=phase_each, channel_x=channel_x,
                channel_tau=channel_tau, aggregate=aggregate,
                mult_x=mult_x, mult_tau=mult_tau, near_tv=near_tv,
                deterministic=deterministic,
                near_agreement=near_agreement)


def direct_compatibility(rows, maps):
    """Compare two-step maps with the direct optimal quantile map on battery."""
    defects = []
    for index in range(len(rows) - 2):
        direct, _i, _j, _mass = ucp_map(rows[index], rows[index + 2])
        composed = maps[index + 1]["K"] @ maps[index]["K"]
        errors = []
        for values in bounded_battery(rows[index]):
            delta = composed @ values - direct @ values
            errors.append(weighted_l2(delta, rows[index + 2]["state"]))
        defects.append(max(errors))
    return defects


def log_slope(x, y):
    x = np.asarray(x, float)
    y = np.maximum(np.asarray(y, float), 1.0e-300)
    return float(np.polyfit(np.log(x), np.log(y), 1)[0])


def run():
    started = time.time()
    print("=" * 78)
    print("STRAT3 UCP INDUCTIVE LIMIT -- adjacent GNS spectral algebras")
    print("=" * 78)
    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))

    rows = gns_measures()
    check("G0.2 nine positive normalized GNS states",
          len(rows) == 9
          and all(np.min(row["state"]) > 0.0 for row in rows)
          and all(abs(np.sum(row["state"]) - 1.0) < 2.0e-15
                  for row in rows),
          "h=" + "/".join(str(row["h"]) for row in rows)
          + ", reconstruction max %.3e"
          % max(row["reconstruction"] for row in rows))

    maps = []
    for source, target in zip(rows[:-1], rows[1:]):
        measured = adjacent_measure(source, target)
        maps.append(measured)
        exact = max(measured["unital"], measured["state_full"],
                    measured["state_battery"],
                    max(0.0, -measured["min_choi"]))
        check("S1.UCP.%d-%d" % (source["h"], target["h"]),
              exact <= STATE_TOL
              and measured["choi_rank"] <= measured["rank_bound"],
              "unital %.2e, state(full/batt) %.2e/%.2e, "
              "Choi min %.2e, rank %d <= %d"
              % (measured["unital"], measured["state_full"],
                 measured["state_battery"], measured["min_choi"],
                 measured["choi_rank"], measured["rank_bound"]))
        print("  covariance: opt(x/tau)=%.6f/%.6f, "
              "channel(x/tau)=%.6f/%.6f, phase=%.6f, aggregate=%.6f"
              % (measured["x_opt"], measured["tau_opt"],
                 measured["channel_x"], measured["channel_tau"],
                 measured["phase_max"], measured["aggregate"]))
        print("  structure: mult(x/tau)=%.6f/%.6f, nearest-state-TV=%.6f, "
              "deterministic mass=%.4f, nearest agreement=%.4f"
              % (measured["mult_x"], measured["mult_tau"],
                 measured["near_tv"], measured["deterministic"],
                 measured["near_agreement"]))

    hs = [math.sqrt(m["source_h"] * m["target_h"]) for m in maps]
    errors = [m["aggregate"] for m in maps]
    ranks = [m["choi_rank"] for m in maps]
    covariance_slope = log_slope(hs, errors)
    rank_slope = log_slope(hs, ranks)
    compatibility = direct_compatibility(rows, maps)
    compatibility_slope = log_slope(hs[1:], compatibility)
    exact_maps = not FAILS
    controlled_rank = rank_slope <= RANK_SLOPE_BAR \
        and all(m["choi_rank"] <= m["rank_bound"] for m in maps)
    decreasing_tail = errors[-3] > errors[-2] > errors[-1]
    covariance_converges = covariance_slope < CONV_SLOPE_BAR \
        and errors[-1] < CONV_RATIO_BAR * errors[0] \
        and decreasing_tail

    print("\nS2 -- preregistered ladder gates")
    outcome("S2.1 UCP AND STATE EXACT", exact_maps,
            "max unital %.3e, state %.3e, battery %.3e"
            % (max(m["unital"] for m in maps),
               max(m["state_full"] for m in maps),
               max(m["state_battery"] for m in maps)))
    outcome("S2.2 CHOI RANK CONTROLLED", controlled_rank,
            "ranks=%s, log-log slope %.3f (bar %.2f)"
            % ("/".join(str(rank) for rank in ranks), rank_slope,
               RANK_SLOPE_BAR))
    outcome("S2.3 COVARIANCE ERROR CONVERGES", covariance_converges,
            "errors=%s, slope %.3f, final/first %.3f, tail %s"
            % ("/".join("%.4f" % error for error in errors),
               covariance_slope, errors[-1] / errors[0],
               "decreasing" if decreasing_tail else "not decreasing"))

    print("\nS3 -- structure diagnostics")
    print("  direct-vs-composed battery defects: %s; slope %.3f"
          % ("/".join("%.4e" % value for value in compatibility),
             compatibility_slope))
    print("  Choi ranks are linear sparse-transport ranks, not bounded ranks.")
    if max(m["deterministic"] for m in maps) < 0.99:
        print("  optimal map type: quantile Markov/conditional-expectation "
              "coupling on a common [0,1] refinement; NOT canonical "
              "nearest-node compression and NOT a *-homomorphism.")
    else:
        print("  optimal map type: asymptotically deterministic compression "
              "candidate (multiplicativity still requires proof).")

    if not exact_maps or not controlled_rank:
        verdict = "UCP-DEAD"
    elif covariance_converges:
        verdict = "UCP-CONVERGES"
    else:
        verdict = "UCP-STAGNATES"
    print("\nVERDICT: %s" % verdict)

    if verdict == "UCP-CONVERGES":
        print("WOULD DELIVER: a zero-free covariant operator-system "
              "inductive-limit candidate with one compatible state whose "
              "finite compressions are the normalized window states.")
    else:
        print("KILL/STOP: state-preserving UCP maps exist canonically, but "
              "their measured shift/grade covariance does not satisfy the "
              "preregistered convergence gate.  Mere state transport is "
              "therefore not the missing L1 mechanism.")
    print("DOES NOT DELIVER: positivity of the critical-line limit (L1).  "
          "Moreover UCP maps alone yield an operator-system limit, not "
          "automatically a C*-inductive limit; the nonzero multiplicativity "
          "defects quantify that extra obstruction.  The full noncommutative "
          "groupoid algebra was not tested.")

    elapsed = time.time() - started
    if FAILS:
        print("RESULT: %d/%d CONSTRUCTION CHECKS PASSED; FAILURES %s (%.1fs)"
              % (len(CHECKS) - len(FAILS), len(CHECKS),
                 ",".join(FAILS), elapsed))
        return 1
    print("RESULT: ALL %d CONSTRUCTION CHECKS PASSED (%.1fs)"
          % (len(CHECKS), elapsed))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
