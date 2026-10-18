#!/usr/bin/env python3
"""v767 -- PRIME.HANDOFFGRAM.01: Modules 2+3 of the global-handoff offensive -- the growing-frequency PSD source Gram: Candidate A (review count) missed honestly (slope +0.471 territory), the predeclared iteration to Candidate B (anti-alias Nf = 2M+1) converges -- spectral errors 0.0855 -> 0.0377 over dimQ 738 -> 5734, slope -0.369, final/first 0.441; PSD by construction (min symbol 7.4e-3); final layer errors arch 0.0141 / atom 0.3946 / pole 0.4144 (pole dominant); both controls fire (HANDOFF-GRAM-CONVERGES).

PROVENANCE: discovery probe handoff_frequency_gram_probe.py (2026-08-04, 6/6 construction/control checks, verdict HANDOFF-GRAM-CONVERGES).  Promoted verbatim (sibling imports point at v563/v716; epstein_firewall_probe stays a read-only discovery import); numbers unchanged.
GLOBAL-HANDOFF modules 2+3: growing-frequency positive source Gram.

Exploration only.  This probe never reads a zero ordinate and never factors,
diagonalizes, or tests the target before constructing Q.

Frozen battery
--------------
Twenty-four real odd test functions are specified analytically in physical
u-coordinates, independent of every window: twelve hats and twelve boxes,
all supported in 0<u<1.55.  The JSON specification and sampled battery are
SHA-256 hashed.

Frozen source formula
---------------------
For each deployed window, independently rebuild

  p = c_arch + c_atom + c_pole

from (i) the Gaussian-E8 Hecke sigma-descended orbit comb (the output of the
internal log generator), (ii) the cover-lift heat trace rho, and (iii) the
closed pole block.  Its Fejer density is

  s(theta)=p0+2 sum_{d=1}^{M-1}(1-d/M) p_d cos(d theta).

For each frozen frequency cell theta_k and full odd lattice test vector u_i,

  Q[k,i] = sqrt(max(s(theta_k),0)/Nf) sum_j u_i[j] exp(i j theta_k).

The positive-part convention is part of the formula before any comparison;
for the true BC source the measured negative part must be numerical only.
The closed rank-one pole amplitude is appended as one extra column using the
exact formula from the pole block.  Therefore G_source=Q*Q is PSD by
construction.  Code labels only grade these columns; they do not bound their
number.

Candidate A uses the review dimension ceil(2 N(pi/D)), with the closed
Gamma-side counting main term.  If and only if it fails the preregistered
handoff convergence gate, one documented construction iteration is allowed:
Candidate B uses Nf=2M+1, the minimal uniform quadrature resolving all
products of degree-(M-1) trigonometric polynomials without aliasing.  This
iteration is fixed here before the first run and is not a fit.

Only after Q and its byte hash are frozen do we build the deployed target

  G_Weil[i,j] = W(f_i * f_j~)

with the existing odd Toeplitz window evaluation.  Layer errors are reported
for arch, atom, and pole/cutoff terms.

Preregistered convergence:
  spectral relative-error log-log slope < -0.25,
  final/first < 0.75, and the last three errors strictly decrease.
CONVERGES requires this plus PSD and both negative controls firing.  PARTIAL
means a positive source improves but misses the rate gate.  DEAD means no
improvement, a construction guard fails, or a control spuriously converges.

Controls: fixed position scramble and the Epstein x^2+5y^2 logarithmic atoms.
No file is written.
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

import v563_paper2_readouts as core  # noqa: E402
import epstein_firewall_probe as ep_control  # noqa: E402
import v716_moonshot_arch_glue as glue  # noqa: E402


TWO_PI = 2.0 * math.pi
BATTERY_SIZE = 24
CHUNK = 256
SOURCE_NEG_TOL = 2.0e-9
WIRE_TOL = 2.0e-10
RATE_BAR = -0.25
RATIO_BAR = 0.75
CONTROL_FACTOR = 5.0
RNG_SEED = 16023
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


def battery_specification():
    hats = []
    for index in range(12):
        center = 0.12 + 0.11 * index
        width = 0.20 + 0.025 * (index % 3)
        hats.append(dict(kind="hat", center=round(center, 12),
                         width=round(width, 12)))
    boxes = []
    for index in range(12):
        left = 0.05 + 0.10 * index
        width = 0.22 + 0.03 * (index % 4)
        boxes.append(dict(kind="box", left=round(left, 12),
                          right=round(left + width, 12)))
    return hats + boxes


BATTERY_SPEC = battery_specification()
BATTERY_SPEC_JSON = json.dumps(
    dict(version="physical-odd-box-hat-v1", functions=BATTERY_SPEC),
    sort_keys=True, separators=(",", ":"))
BATTERY_SPEC_HASH = hashlib.sha256(
    BATTERY_SPEC_JSON.encode("utf-8")).hexdigest()


def odd_extension(free):
    return np.concatenate((free, -free[::-1]))


def sampled_battery(M, D):
    h = M // 2
    coordinates = (np.arange(h) - 0.5 * (M - 1)) * D
    radius = np.abs(coordinates)
    columns = []
    for specification in BATTERY_SPEC:
        if specification["kind"] == "hat":
            values = np.maximum(
                1.0 - np.abs(radius - specification["center"])
                / specification["width"], 0.0)
        else:
            values = ((radius >= specification["left"])
                      & (radius <= specification["right"])).astype(float)
        values *= math.sqrt(D)
        norm = float(np.linalg.norm(values))
        if norm == 0.0:
            raise RuntimeError("battery function vanished")
        columns.append(values / norm)
    free = np.column_stack(columns)
    full = np.column_stack([odd_extension(free[:, index])
                            for index in range(free.shape[1])])
    digest = hashlib.sha256()
    digest.update(BATTERY_SPEC_HASH.encode("ascii"))
    digest.update(np.ascontiguousarray(free).tobytes())
    return free, full, digest.hexdigest()


def n_of_T(value):
    if value <= TWO_PI:
        return 0.0
    return (value / TWO_PI) * math.log(
        value / (TWO_PI * math.e)) + 7.0 / 8.0


def requested_frequency_count(window):
    return max(1, int(math.ceil(2.0 * n_of_T(math.pi / window["D"]))))


def source_comb(maximum):
    comb, metadata = glue.geo_comb(maximum)
    return comb, metadata


def atom_lags_from_comb(window, comb):
    reach = int(math.exp(2.0 * window["alpha"]) + 0.5)
    sites = np.array(sorted(number for number in comb if number <= reach),
                     dtype=int)
    positions = np.log(sites.astype(float))
    masses = np.array([2.0 * comb[int(number)] / math.sqrt(float(number))
                       for number in sites])
    return glue.atom_tent_geo(window["alpha"], window["M"],
                              positions, masses), sites, masses


def arch_lags_from_cover(window):
    lags = np.empty(window["M"])
    lags[0] = glue.arch_lag0_geo(window["D"])
    lags[1:] = glue.arch_lags_far_geo(window["M"], window["D"])
    return lags


def build_true_source_layers(window, comb):
    atom, sites, masses = atom_lags_from_comb(window, comb)
    arch = arch_lags_from_cover(window)
    pole = glue.pole_lags_closed(window["M"], window["D"])
    return dict(arch=arch, atom=atom, pole=pole,
                sites=sites, masses=masses)


def fejer_symbol(theta, moments):
    moments = np.asarray(moments, float)
    degree = np.arange(1, len(moments))
    coefficients = (1.0 - degree / len(moments)) * moments[1:]
    return moments[0] + 2.0 * (
        np.cos(np.outer(theta, degree)) @ coefficients)


def pole_amplitudes(window, full_battery):
    M, D = window["M"], window["D"]
    coefficient = (4.0 / D) * (2.0 * math.cosh(0.5 * D) - 2.0)
    boundary = np.exp(0.5 * D * np.arange(M))
    scale = math.sqrt(
        2.0 * coefficient * math.exp(-0.5 * (M - 1) * D))
    return scale * (boundary @ full_battery)


def source_gram(window, layers, full_battery, frequency_count, tag):
    """Build and hash Q before any target matrix is constructed."""
    M = window["M"]
    total_moments = layers["arch"] + layers["atom"] + layers["pole"]
    grams = {name: np.zeros((BATTERY_SIZE, BATTERY_SIZE))
             for name in ("arch", "atom", "pole")}
    gram_frequency = np.zeros((BATTERY_SIZE, BATTERY_SIZE))
    minimum_symbol = math.inf
    negative_mass = 0.0
    q_digest = hashlib.sha256()
    manifest = dict(tag=tag, M=M, D=window["D"],
                    frequency_count=frequency_count,
                    battery_hash=BATTERY_SPEC_HASH,
                    formula="Fejer-positive-frequency-v1+closed-pole")
    q_digest.update(json.dumps(manifest, sort_keys=True,
                               separators=(",", ":")).encode("utf-8"))

    lattice_indices = np.arange(M)
    for start in range(0, frequency_count, CHUNK):
        stop = min(start + CHUNK, frequency_count)
        indices = np.arange(start, stop)
        theta = TWO_PI * (indices + 0.5) / frequency_count
        fourier = np.exp(1j * np.outer(theta, lattice_indices)) \
            @ full_battery
        symbol = fejer_symbol(theta, total_moments)
        minimum_symbol = min(minimum_symbol, float(np.min(symbol)))
        negative_mass += float(np.sum(np.maximum(-symbol, 0.0))) \
            / frequency_count
        amplitude = np.sqrt(np.maximum(symbol, 0.0)
                            / frequency_count)[:, None] * fourier
        q_digest.update(np.ascontiguousarray(amplitude).tobytes())
        gram_frequency += (amplitude.T.conj() @ amplitude).real

        for name in ("arch", "atom", "pole"):
            layer_symbol = fejer_symbol(theta, layers[name])
            grams[name] += (
                fourier.T.conj()
                @ ((layer_symbol / frequency_count)[:, None] * fourier)
            ).real

    pole_column = pole_amplitudes(window, full_battery)
    q_digest.update(np.ascontiguousarray(pole_column).tobytes())
    pole_gram = np.outer(pole_column, pole_column)
    source = gram_frequency + pole_gram
    grams["pole"] += pole_gram
    layer_residual = float(np.max(np.abs(
        source - sum(grams.values(), np.zeros_like(source)))))
    return dict(gram=0.5 * (source + source.T), layers=grams,
                q_hash=q_digest.hexdigest(),
                minimum_symbol=minimum_symbol,
                negative_mass=negative_mass,
                layer_residual=layer_residual,
                dimension=frequency_count + 1)


def target_gram(window, free_battery):
    arch_form = core.odd_toeplitz(window["car"], window["M"])
    atom_form = core.odd_toeplitz(window["cat"], window["M"])
    arch_target = 2.0 * free_battery.T @ arch_form @ free_battery
    atom_target = 2.0 * free_battery.T @ atom_form @ free_battery
    target = arch_target + atom_target
    return dict(gram=0.5 * (target + target.T),
                layers=dict(arch=arch_target, atom=atom_target,
                            pole=np.zeros_like(target)))


def error_metrics(source, target, reference=None):
    difference = source - target
    scale_matrix = target if reference is None else reference
    target_scale = max(float(np.max(np.abs(scale_matrix))), 1.0e-300)
    target_spectral = max(float(sla.norm(scale_matrix, 2)), 1.0e-300)
    target_frobenius = max(float(sla.norm(scale_matrix, "fro")), 1.0e-300)
    return dict(entry=float(np.max(np.abs(difference))) / target_scale,
                spectral=float(sla.norm(difference, 2)) / target_spectral,
                frobenius=float(sla.norm(difference, "fro"))
                / target_frobenius)


def log_slope(values_x, values_y):
    x = np.asarray(values_x, float)
    y = np.maximum(np.asarray(values_y, float), 1.0e-300)
    return float(np.polyfit(np.log(x), np.log(y), 1)[0])


def convergence_profile(rows):
    errors = [row["error"]["spectral"] for row in rows]
    dimensions = [row["source"]["dimension"] for row in rows]
    slope = log_slope(dimensions, errors)
    tail = len(errors) >= 3 and errors[-3] > errors[-2] > errors[-1]
    converges = slope < RATE_BAR and errors[-1] < RATIO_BAR * errors[0] \
        and tail
    return dict(errors=errors, dimensions=dimensions, slope=slope,
                ratio=errors[-1] / errors[0], tail=tail,
                converges=converges)


def evaluate_candidate(windows, layers_by_window, tag, count_function):
    rows = []
    print("\n%s" % tag)
    for window, layers in zip(windows, layers_by_window):
        free, full, battery_hash = sampled_battery(window["M"], window["D"])
        count = int(count_function(window))
        source = source_gram(window, layers, full, count, tag)
        # Target construction happens only after Q and q_hash are complete.
        target = target_gram(window, free)
        error = error_metrics(source["gram"], target["gram"])
        layer_errors = {
            name: error_metrics(source["layers"][name],
                                target["layers"][name],
                                reference=target["gram"])
            for name in ("arch", "atom", "pole")
        }
        eigen_min = float(sla.eigvalsh(
            source["gram"], subset_by_index=[0, 0])[0])
        row = dict(window=window, source=source, target=target,
                   error=error, layer_errors=layer_errors,
                   eigen_min=eigen_min, battery_hash=battery_hash)
        rows.append(row)
        print("  h=%4d Nf=%5d dimQ=%5d minS=%+.3e lmin(Gs)=%+.3e "
              "err(entry/spec/frob)=%.4f/%.4f/%.4f hash=%s"
              % (window["M"] // 2, count, source["dimension"],
                 source["minimum_symbol"], eigen_min, error["entry"],
                 error["spectral"], error["frobenius"],
                 source["q_hash"][:16]))
        print("    layer spec errors arch/atom/pole = %.4f/%.4f/%.4f"
              % tuple(layer_errors[name]["spectral"]
                      for name in ("arch", "atom", "pole")))
    profile = convergence_profile(rows)
    print("  profile: errors=%s slope=%.3f final/first=%.3f tail=%s"
          % ("/".join("%.4f" % value for value in profile["errors"]),
             profile["slope"], profile["ratio"],
             "fallend" if profile["tail"] else "nicht fallend"))
    return rows, profile


def epstein_layers(windows):
    horizon = int(max(math.exp(2.0 * window["alpha"])
                      for window in windows) + 0.5)
    chi4, chi5, chi20 = ep_control.chi_arrays(horizon)
    coefficients = (ep_control.divisor_transform(chi20, horizon)
                    + ep_control.convolution_45(chi4, chi5, horizon))
    lattice = ep_control.lattice_r1(horizon)
    if int(np.max(np.abs(lattice[1:] - coefficients[1:]))) != 0:
        raise RuntimeError("Epstein coefficient identity failed")
    series = np.zeros(horizon + 1)
    series[1:] = lattice[1:].astype(float) / float(lattice[1])
    logarithmic_atoms = ep_control.dirichlet_vonmangoldt(series, horizon)
    output = []
    for window in windows:
        reach = int(math.exp(2.0 * window["alpha"]))
        sites = np.where(np.abs(logarithmic_atoms[:reach + 1])
                         > 1.0e-9)[0]
        positions = np.log(sites.astype(float))
        masses = 2.0 * logarithmic_atoms[sites] \
            / np.sqrt(sites.astype(float))
        atom = glue.atom_tent_geo(window["alpha"], window["M"],
                                  positions, masses)
        output.append(dict(arch=arch_lags_from_cover(window), atom=atom,
                           pole=glue.pole_lags_closed(
                               window["M"], window["D"])))
    return output, logarithmic_atoms


def scrambled_layers(windows, true_layers):
    rng = np.random.default_rng(RNG_SEED)
    output = []
    for window, layers in zip(windows, true_layers):
        positions = np.sort(rng.uniform(
            0.5, 2.0 * window["alpha"], len(layers["sites"])))
        atom = glue.atom_tent_geo(window["alpha"], window["M"],
                                  positions, layers["masses"])
        output.append(dict(arch=layers["arch"], atom=atom,
                           pole=layers["pole"]))
    return output


def control_profile(windows, layers_by_window, count_function, tag):
    rows = []
    negative = False
    for window, layers in zip(windows, layers_by_window):
        free, full, _battery_hash = sampled_battery(
            window["M"], window["D"])
        source = source_gram(window, layers, full,
                             int(count_function(window)), tag)
        target = target_gram(window, free)
        error = error_metrics(source["gram"], target["gram"])
        rows.append(dict(window=window, source=source,
                         target=target, error=error))
        negative |= source["minimum_symbol"] < -SOURCE_NEG_TOL
    profile = convergence_profile(rows)
    profile["negative_symbol"] = negative
    return profile


def run():
    started = time.time()
    print("=" * 78)
    print("GLOBAL HANDOFF -- growing-frequency BC source Gram")
    print("=" * 78)
    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    check("G0.2 frozen battery", len(BATTERY_SPEC) == BATTERY_SIZE,
          "SHA256 %s, 12 hats + 12 boxes" % BATTERY_SPEC_HASH)

    windows = glue.declared_family()
    maximum = int(max(math.exp(2.0 * window["alpha"])
                      for window in windows) + 0.5)
    comb, metadata = source_comb(maximum)
    true_layers = [build_true_source_layers(window, comb)
                   for window in windows]
    wiring = 0.0
    for window, layers in zip(windows, true_layers):
        assembled = layers["arch"] + layers["atom"] + layers["pole"]
        wiring = max(wiring, float(np.max(np.abs(assembled - window["p"]))
                                   / np.max(np.abs(window["p"]))))
    check("G0.3 ingredient wiring before Q", wiring <= WIRE_TOL,
          "comb slots=%d, Gaussian irreducibles=%d, split=%d, inert=%d, "
          "max rel deployed deviation %.3e"
          % (len(comb), metadata["n_irred"], metadata["n_split"],
             metadata["n_inert"], wiring))

    rows_a, profile_a = evaluate_candidate(
        windows, true_layers, "CANDIDATE A -- review frequency count",
        requested_frequency_count)
    true_nonnegative_a = all(
        row["source"]["minimum_symbol"] >= -SOURCE_NEG_TOL
        for row in rows_a)

    if profile_a["converges"]:
        chosen_rows, chosen_profile = rows_a, profile_a
        chosen_tag = "A"
        count_function = requested_frequency_count
        iteration_used = False
    else:
        print("\nITERATION 1/1: Candidate A misses the frozen rate gate.  "
              "Reason: its cell count is below the anti-alias degree of "
              "s(theta)|F(theta)|^2.  Switching to the predeclared exact "
              "uniform quadrature Nf=2M+1; no target-derived parameter.")
        rows_b, profile_b = evaluate_candidate(
            windows, true_layers,
            "CANDIDATE B -- anti-alias quadrature 2M+1",
            lambda window: 2 * window["M"] + 1)
        chosen_rows, chosen_profile = rows_b, profile_b
        chosen_tag = "B"
        count_function = lambda window: 2 * window["M"] + 1
        iteration_used = True

    true_nonnegative = all(
        row["source"]["minimum_symbol"] >= -SOURCE_NEG_TOL
        for row in chosen_rows)
    psd = all(row["eigen_min"] >= -1.0e-9 for row in chosen_rows)
    hash_unique = len({row["source"]["q_hash"]
                       for row in chosen_rows}) == len(chosen_rows)
    check("M2.1 source Q frozen and PSD",
          true_nonnegative and psd and hash_unique,
          "chosen=%s iteration=%s, min symbols=%s, lmin=%s"
          % (chosen_tag, iteration_used,
             "/".join("%.2e" % row["source"]["minimum_symbol"]
                      for row in chosen_rows),
             "/".join("%.2e" % row["eigen_min"]
                      for row in chosen_rows)))
    outcome("M2.2 HANDOFF ERROR CONVERGES", chosen_profile["converges"],
            "dimensions=%s, errors=%s, slope %.3f, final/first %.3f, "
            "tail %s"
            % ("/".join(str(value)
                        for value in chosen_profile["dimensions"]),
               "/".join("%.4f" % value
                        for value in chosen_profile["errors"]),
               chosen_profile["slope"], chosen_profile["ratio"],
               "fallend" if chosen_profile["tail"]
               else "nicht fallend"))

    scramble = scrambled_layers(windows, true_layers)
    scramble_profile = control_profile(
        windows, scramble, count_function, "CONTROL-SCRAMBLE")
    ep_layers, ep_atoms = epstein_layers(windows)
    ep_profile = control_profile(
        windows, ep_layers, count_function, "CONTROL-EPSTEIN")
    ep_negative_sites = np.where(ep_atoms < -1.0e-9)[0]

    scramble_fires = scramble_profile["negative_symbol"] \
        or (not scramble_profile["converges"]
            and scramble_profile["errors"][-1]
            >= CONTROL_FACTOR * chosen_profile["errors"][-1])
    ep_fires = ep_profile["negative_symbol"] \
        or (not ep_profile["converges"]
            and ep_profile["errors"][-1]
            >= CONTROL_FACTOR * chosen_profile["errors"][-1])
    check("C1 SCRAMBLE SOURCE DOES NOT CONVERGE", scramble_fires,
          "errors=%s slope %.3f negative-symbol=%s"
          % ("/".join("%.4f" % value
                      for value in scramble_profile["errors"]),
             scramble_profile["slope"],
             scramble_profile["negative_symbol"]))
    check("C2 EPSTEIN SOURCE DOES NOT CONVERGE", ep_fires,
          "%d negative atom sites, first %d; errors=%s slope %.3f "
          "negative-symbol=%s"
          % (len(ep_negative_sites),
             int(ep_negative_sites[0]) if len(ep_negative_sites) else -1,
             "/".join("%.4f" % value
                      for value in ep_profile["errors"]),
             ep_profile["slope"], ep_profile["negative_symbol"]))

    guards = not FAILS
    if guards and chosen_profile["converges"] \
            and scramble_fires and ep_fires:
        verdict = "HANDOFF-GRAM-CONVERGES"
    elif guards and chosen_profile["errors"][-1] \
            < chosen_profile["errors"][0] \
            and scramble_fires and ep_fires:
        verdict = "HANDOFF-GRAM-PARTIAL"
    else:
        verdict = "HANDOFF-GRAM-DEAD"
    print("\nVERDICT: %s" % verdict)
    layer_final = {
        name: chosen_rows[-1]["layer_errors"][name]["spectral"]
        for name in ("arch", "atom", "pole")
    }
    print("FINAL LAYER ERRORS (spectral relative): arch %.6f, atom %.6f, "
          "pole/cutoff %.6f; dominant=%s"
          % (layer_final["arch"], layer_final["atom"],
             layer_final["pole"], max(layer_final, key=layer_final.get)))
    if verdict == "HANDOFF-GRAM-CONVERGES":
        print("CONSEQUENCE: a target-independent growing-frequency "
              "Stinespring source has passed the finite ladder.  What remains "
              "is a uniform tail bound for the Fejer/cell quadrature, "
              "compatibility across windows, and identification of the "
              "operator-system limit with the full Weil functional.")
    elif verdict == "HANDOFF-GRAM-PARTIAL":
        print("HONEST READING: growing the frequency space improves the "
              "handoff but does not satisfy the frozen convergence rate.  "
              "This is a numerical approximation scheme, not yet a "
              "categorical/global handoff.")
    else:
        print("KILL: neither frozen frequency construction yields a "
              "controlled handoff distinct from the negative controls.")

    elapsed = time.time() - started
    if FAILS:
        print("RESULT: %d/%d CONSTRUCTION/CONTROL CHECKS PASSED; FAILURES %s "
              "(%.1fs)" % (len(CHECKS) - len(FAILS), len(CHECKS),
                           ",".join(FAILS), elapsed))
        return 1
    print("RESULT: ALL %d CONSTRUCTION/CONTROL CHECKS PASSED (%.1fs)"
          % (len(CHECKS), elapsed))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
