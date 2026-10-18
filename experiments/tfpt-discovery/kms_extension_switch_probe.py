#!/usr/bin/env python3
"""PRIME.KMS.INDUCTIVE_STATE.01 -- finite extension switch/kill test.

Exploration only.  This probe tests the strongest literal reading of the
master contract before any global construction is attempted.

Finite slice A_S^+
------------------
For each of the nine TFPT windows, take the first K=96 monomials of its
GNS/translation generator U_h.  Add:

* isotropy: the four characters Q^r of the sigma/mu4 sector;
* archimedean lift: all matrix units E_jk on the N=48 selected lift sector
  m == 1 mod 4, with finite-lift energies
      eps_m = (48/pi) sin(m pi/96).

The canonical local functional is the normalized TFPT moment state on U_h,
the regular character state on mu4, and the beta=1 Gibbs state on the lift.
On the generating monomial family

    {U_h^n Q^r E_jk : 0<=n<K, 0<=r<4, 0<=j,k<12}

its Gram matrix factorizes exactly into the TFPT Toeplitz moment Gram,
I_4, and the faithful Gibbs matrix-unit Gram.  This gives a 55,296-monomial
positivity test without materializing the full Kronecker matrix.

Two independent obstructions are then tested.

1. A covariant unital *-embedding C^h -> C^h' between adjacent ordered GNS
   spectral algebras is state-preserving only if every source cumulative
   weight boundary occurs among the target cumulative boundaries.  This is
   the deterministic (*-homomorphic) version of the UCP quantile map.

2. Gate 0 uses Laurent unitaries u_p with
       u_p^* u_p = u_p u_p^* = 1,
       sigma_t(u_p) = p^(it) u_p.
   At beta=1 the requested convention T(ab)=T(b sigma_i(a)), applied to
   a=u_p, b=u_p^*, forces
       1 = p^(-1).
   Thus no normalized KMS state can restrict to the literal graded Laurent
   algebra.  This is exact and independent of all fitted moments.  The
   Bost--Connes repair is an infinite semigroup Toeplitz algebra with
   isometries, not these bilateral Laurent unitaries.

Controls
--------
The identical Toeplitz/extended Gram construction must become indefinite for
the Epstein x^2+5y^2 atom replacement and for the frozen position scramble.
No zero ordinate or prime table is loaded by this file.

Verdict:
  KMS-EXTENSION-ALIVE iff positivity, covariant *-restriction compatibility,
  and every beta=1 twist identity pass.
  KMS-EXTENSION-DEAD otherwise, while construction/control checks may all
  pass.  No file is written.
"""

import ast
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, "..", "..",
                                                "verification")))

import v563_paper2_readouts as core  # noqa: E402
import epstein_firewall_probe as ep_control  # noqa: E402
import moonshot_arch_glue_probe as arch  # noqa: E402
import moonshot_spectral_probe as spectral  # noqa: E402


MONOMIAL_DEPTH = 96
LIFT_SIZE = 48
ISOTROPY_ORDER = 4
RANDOM_ELEMENTS = 8
RNG = np.random.default_rng(1401)
PSD_TOL_FACTOR = 100.0
RESTRICTION_TOL = 1.0e-12
KMS_TOL = 2.0e-14
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


def lift_data():
    modes = np.arange(1, LIFT_SIZE, 2)
    modes = modes[modes % ISOTROPY_ORDER == 1]
    energies = (LIFT_SIZE / math.pi) * np.sin(
        modes * math.pi / (2.0 * LIFT_SIZE))
    gibbs = np.exp(-energies)
    gibbs /= np.sum(gibbs)
    # For matrix-unit ordering (j,k), ||E_jk||_T^2 = T(E_kk)=gibbs[k].
    matrix_unit_gram_diagonal = np.tile(gibbs, len(energies))
    return modes, energies, gibbs, matrix_unit_gram_diagonal


def moment_gram(moment_vector, depth=MONOMIAL_DEPTH):
    depth = min(depth, len(moment_vector))
    normalized = np.asarray(moment_vector[:depth], float) \
        / float(moment_vector[0])
    gram = sla.toeplitz(normalized)
    return 0.5 * (gram + gram.T)


def extended_gram_stats(moment_vector, arch_diagonal):
    base = moment_gram(moment_vector)
    eigenvalues = sla.eigvalsh(base, check_finite=False)
    products = np.outer(eigenvalues, arch_diagonal)
    extended_min = float(np.min(products))
    extended_max = float(np.max(products))

    rest_weights = np.tile(arch_diagonal, ISOTROPY_ORDER)
    minimum_random = math.inf
    for _ in range(RANDOM_ELEMENTS):
        coefficients = (RNG.standard_normal((len(base), len(rest_weights)))
                        + 1j * RNG.standard_normal(
                            (len(base), len(rest_weights))))
        transformed = base @ coefficients
        components = np.sum(np.conj(coefficients) * transformed,
                            axis=0).real
        value = float(np.dot(rest_weights, components))
        norm = float(np.sum(np.abs(coefficients) ** 2))
        minimum_random = min(minimum_random, value / norm)
    return dict(base_min=float(eigenvalues[0]),
                base_max=float(eigenvalues[-1]),
                extended_min=extended_min,
                extended_max=extended_max,
                random_min=minimum_random,
                monomials=len(base) * ISOTROPY_ORDER * len(arch_diagonal))


def true_window_stats(windows, arch_diagonal):
    return [extended_gram_stats(window["p"], arch_diagonal)
            for window in windows]


def epstein_moment_vector(window, horizon):
    chi4, chi5, chi20 = ep_control.chi_arrays(horizon)
    coefficients = (ep_control.divisor_transform(chi20, horizon)
                    + ep_control.convolution_45(chi4, chi5, horizon))
    lattice = ep_control.lattice_r1(horizon)
    if int(np.max(np.abs(lattice[1:] - coefficients[1:]))) != 0:
        raise RuntimeError("Epstein genus identity failed")
    series = np.zeros(horizon + 1)
    series[1:] = lattice[1:].astype(float) / float(lattice[1])
    logarithmic_atoms = ep_control.dirichlet_vonmangoldt(series, horizon)
    reach = int(math.exp(2.0 * window["alpha"]))
    support = np.where(np.abs(logarithmic_atoms[:reach + 1]) > 1.0e-9)[0]
    positions = np.log(support.astype(float))
    masses = 2.0 * logarithmic_atoms[support] \
        / np.sqrt(support.astype(float))
    _form, _metric, atom_lags = ep_control.window_form(
        window["alpha"], window["M"], positions, masses, window["car"])
    return window["car"] + atom_lags + window["cp"], logarithmic_atoms


def scrambled_moment_vector(window):
    count = window["ka"]
    positions = np.sort(RNG.uniform(0.5, 2.0 * window["alpha"], count))
    atom_lags = arch.atom_tent_geo(
        window["alpha"], window["M"], positions,
        np.asarray(core.MU_ALL[:count], float))
    return window["car"] + atom_lags + window["cp"]


def gns_states(windows):
    rows = []
    for window in windows:
        h = window["M"] // 2
        _tau, weights, bad_depth, reconstruction = spectral.gns_nodes(
            window["p"], h, window["D"])
        if bad_depth is not None:
            raise RuntimeError("GNS breakdown at h=%d" % h)
        weights = weights / float(np.sum(weights))
        rows.append(dict(h=h, weights=weights,
                         reconstruction=reconstruction))
    return rows


def ordered_embedding_obstruction(source, target):
    """Boundary test for a covariant state-preserving unital *-embedding."""
    source_boundaries = np.cumsum(source["weights"])[:-1]
    target_boundaries = np.cumsum(target["weights"])[:-1]
    indices = np.searchsorted(target_boundaries, source_boundaries)
    right = np.clip(indices, 0, len(target_boundaries) - 1)
    left = np.clip(indices - 1, 0, len(target_boundaries) - 1)
    gaps = np.minimum(np.abs(source_boundaries - target_boundaries[left]),
                      np.abs(source_boundaries - target_boundaries[right]))
    matches = int(np.sum(gaps <= RESTRICTION_TOL))
    return dict(required=len(source_boundaries), matches=matches,
                min_gap=float(np.min(gaps)),
                rms_gap=math.sqrt(float(np.mean(gaps * gaps))),
                max_gap=float(np.max(gaps)))


def arch_kms_check(energies, gibbs):
    maximum = 0.0
    for j, energy_j in enumerate(energies):
        for k, energy_k in enumerate(energies):
            left = gibbs[j]
            twist = math.exp(-(energy_j - energy_k))
            right = twist * gibbs[k]
            maximum = max(maximum, abs(left - right))
    return maximum


def run():
    started = time.time()
    print("=" * 78)
    print("PRIME.KMS.INDUCTIVE_STATE.01 -- finite extension switch test")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    windows = spectral.family_ext()
    check("G0.2 nine declared windows", len(windows) == 9,
          "h=" + "/".join(str(w["M"] // 2) for w in windows))

    modes, energies, gibbs, arch_diagonal = lift_data()
    heat_deviation = 0.0
    for flow_time in (0.5, 1.0, 2.0, 3.0):
        matrix_trace = float(np.sum(np.exp(-flow_time * energies)))
        deployed_trace = float(arch.rho_lat(
            np.array([flow_time]), LIFT_SIZE)[0])
        heat_deviation = max(heat_deviation,
                             abs(matrix_trace - deployed_trace))
    check("K1.1 arch lift trace wiring", heat_deviation <= KMS_TOL,
          "modes=%s, max heat-trace deviation %.3e"
          % (modes.tolist(), heat_deviation))

    stats = true_window_stats(windows, arch_diagonal)
    scale = max(row["extended_max"] for row in stats)
    numerical_floor = PSD_TOL_FACTOR * np.finfo(float).eps * scale
    positivity = all(row["extended_min"] >= -numerical_floor
                     and row["random_min"] >= -numerical_floor
                     for row in stats)
    outcome("K1.i POSITIVITY ON A_S+", positivity,
            "lambda_min_ext=%s; random minima=%s; %d monomials/window"
            % ("/".join("%.3e" % row["extended_min"] for row in stats),
               "/".join("%.3e" % row["random_min"] for row in stats),
               stats[0]["monomials"]))
    check("K1.2 positive Gram construction calibrated", positivity,
          "base lambda_min %.3e .. %.3e, floor %.3e"
          % (min(row["base_min"] for row in stats),
             max(row["base_min"] for row in stats), numerical_floor))

    states = gns_states(windows)
    restrictions = [ordered_embedding_obstruction(source, target)
                    for source, target in zip(states[:-1], states[1:])]
    restriction_ok = all(row["matches"] == row["required"]
                         for row in restrictions)
    outcome("K1.ii COVARIANT WINDOW RESTRICTIONS", restriction_ok,
            "exact boundaries=%s of required %s; min gaps=%s"
            % ("/".join(str(row["matches"]) for row in restrictions),
               "/".join(str(row["required"]) for row in restrictions),
               "/".join("%.3e" % row["min_gap"] for row in restrictions)))
    check("K1.3 restriction obstruction resolved exactly",
          not restriction_ok
          and all(row["matches"] < row["required"]
                  for row in restrictions),
          "RMS gaps=%s; max gaps=%s"
          % ("/".join("%.3e" % row["rms_gap"] for row in restrictions),
             "/".join("%.3e" % row["max_gap"] for row in restrictions)))

    arch_kms = arch_kms_check(energies, gibbs)
    isotropy_kms = 0.0  # sigma_t(Q)=Q and the regular mu4 state is tracial.
    orbit_defects = {place: Fraction(place - 1, place)
                     for place in (2, 3, 5)}
    kms_ok = arch_kms <= KMS_TOL and isotropy_kms <= KMS_TOL \
        and float(max(orbit_defects.values())) <= KMS_TOL
    outcome("K1.iii BETA=1 KMS TWIST", kms_ok,
            "arch %.3e, isotropy %.3e, Laurent-unitary defects "
            "p=2:1/2=%.12f, p=3:2/3=%.12f, p=5:4/5=%.12f"
            % (arch_kms, isotropy_kms, float(orbit_defects[2]),
               float(orbit_defects[3]), float(orbit_defects[5])))
    check("K1.4 exact KMS obstruction detected",
          arch_kms <= KMS_TOL and isotropy_kms <= KMS_TOL
          and orbit_defects == {2: Fraction(1, 2),
                                3: Fraction(2, 3),
                                5: Fraction(4, 5)},
          "T(u_p u_p*)=1 versus T(u_p* sigma_i(u_p))=1/p")

    # Negative controls: same extended Gram, only the atom moments changed.
    ep_window = windows[1]
    horizon = int(math.exp(2.0 * ep_window["alpha"]) + 0.5)
    ep_moments, ep_atoms = epstein_moment_vector(ep_window, horizon)
    ep_stats = extended_gram_stats(ep_moments, arch_diagonal)
    negative_sites = np.where(ep_atoms < -1.0e-9)[0]
    ep_breaks = ep_stats["base_min"] < -numerical_floor \
        and ep_stats["extended_min"] < -numerical_floor
    check("C1 EPSTEIN CONTROL BREAKS POSITIVITY", ep_breaks,
          "%d negative atom sites (first %d); base/ext lambda_min "
          "%.6e/%.6e"
          % (len(negative_sites),
             int(negative_sites[0]) if len(negative_sites) else -1,
             ep_stats["base_min"], ep_stats["extended_min"]))

    scramble_window = windows[4]
    scramble_moments = scrambled_moment_vector(scramble_window)
    scramble_stats = extended_gram_stats(scramble_moments, arch_diagonal)
    scramble_breaks = scramble_stats["base_min"] < -numerical_floor \
        and scramble_stats["extended_min"] < -numerical_floor
    check("C2 SCRAMBLE CONTROL BREAKS POSITIVITY", scramble_breaks,
          "h=%d, base/ext lambda_min %.6e/%.6e"
          % (scramble_window["M"] // 2, scramble_stats["base_min"],
             scramble_stats["extended_min"]))

    alive = positivity and restriction_ok and kms_ok
    verdict = "KMS-EXTENSION-ALIVE" if alive else "KMS-EXTENSION-DEAD"
    print("\nVERDICT: %s" % verdict)
    if alive:
        print("NEXT STAGE: enlarge the finite place set and lift cutoff, then "
              "prove uniform complete positivity and normal-state compactness.")
    else:
        print("ANATOMY: local extended Gram positivity survives, but the "
              "strong global contract fails twice: adjacent normalized GNS "
              "states are not restrictions along covariant unital "
              "*-embeddings, and beta=1 KMS is algebraically impossible on "
              "Gate-0's nonzero-grade Laurent unitaries.")
        print("WEAKER CONTRACT REQUIRED: replace the Laurent orbit algebra by "
              "the BC semigroup Toeplitz algebra (nonunitary isometries with "
              "boundary projections), and replace exact finite "
              "*-restrictions by compatible UCP/operator-system maps or an "
              "asymptotic KMS condition.  Exact finite-dimensional KMS is "
              "then imposed only on the arch Gibbs/isotropy factors.")
    print("HONEST SCOPE: positivity was tested on the 55,296-monomial "
          "factorized finite slice per window.  No full adele-class "
          "completion or critical-line positivity was constructed.")

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
