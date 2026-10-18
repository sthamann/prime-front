#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cert_mine_probe -- PRIME.CERT.MINE.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-13.)

THE 1111 CERTIFICATES STOP BEING COUNTED AND START BEING READ.
CCXCIII generated 1106 exact per-cell certificates (seven for each
of 151 census plus seven F5X extension cells); CCCIX deliberately
persisted only the consumed minimum per cell in cofinal_package.json,
plus the five global certificates.  This probe rematerializes the
omitted candidates with the frozen CCXCIII machinery, checks that
the persisted witness of every cell occurs hash-identically among
the seven, and mines the resulting 1106 + 5 = 1111 objects for a
common symbolic form.

 (a) EXTRACTION AND NORMALIZATION.  For a cell of height h set
       mu = mu1(h) = 4 sin^2(pi/(2h+1)),
     and use both dimensionally natural coordinates:
       y = x/mu,
       t = (x-m)/w,  m=(beta+L)/2, w=(L-beta)/2.
     Thus the dimensionless majorant coefficients are
       chat_j = c_j mu^(j+1),
     the moments are
       nuhat_j = nu_j/(n mu^(j+1)),
     spectral coordinates and exact LDL pivots are divided by mu,
     while unit-lower LDL multipliers are unchanged.  In the interval
     coordinate the dimensionless majorant is m p(m+wt), and the SOS
     Grams are transported exactly:
       G0_t = C^T G0_x C,  G1_t = w^2 C^T G1_x C,
     where (1,x,...)=C(1,t,...).  The compact JSON stores these
     normalized vectors, upper triangles and active patterns; exact
     objects are regenerated from the package and their hashes.
 (b) CLUSTER CENSUS.  Certificates are clustered by family, degree,
     exact Gram sparsity, rank/zero activity and Radau endpoint
     activity.  Per fixed-length cluster the full normalized vector
     includes the cell LDL data, coordinates, moments, majorant,
     interval Grams and (for Radau) nodes/weights.  Exact-constant
     component counts, relative spans and log-h drift slopes decide
     CONSTANT / STABLE / DRIFT; singleton globals remain SINGLETON,
     never evidence for stability.
 (c) RATIONAL RECONSTRUCTION.  Continued-fraction reconstruction is
     admitted only after exact Fraction equality on train, held-out
     and blind cells.  A second exact affine search uses only the
     rational subset {1,h,nu_0/n,...,nu_3/n} of the allowed variables;
     cos(pi/(2h+1)) and mu1(h) are NEVER numerically fitted because an
     approximate algebraic equality cannot pass an exact gate.  They
     enter only through the symbolically verified identity
     mu1=4(1-cos^2).  Nonlinear source-moment identities are derived
     from the exact Chebyshev/Radau recurrence and checked exactly.
 (d) THE COMMON FORM.  The Radau-dual certificates have one exact
     Newton-Hermite formula and one of two exact rank-one
     Markov-Lukacs forms.  The Chebyshev certificates share the
     interval-SOS schema but their normalized coefficients and dense
     Gram LDL multipliers are measured for drift.  The sharp partial
     matrix form is printed:
       M = C_s^{-1} diag(r+delta,B) C_s^{-T},
       r=n-sum c_j nu_j >= eta n,
       delta=b^T(p(B)-B^{-1})b >= 0,
     with delta expanded by the SOS identity and B by its exact
     floor LDL.  It is NOT called an all-h closed form.
 (e) GATES.  Every regenerated certificate is exact-verified; every
     x-to-t transport is an exact polynomial identity; the persisted
     witness hash must be found for every cell; all dual Newton and
     rank forms are exact; continued-fraction candidates pass only by
     exact equality; F5 plus F5X are blind and excluded from
     reconstruction; a perturbed certificate must fail; the exact
     path is AST-scanned against eigensolvers/truth reads.  No new
     positivity margin is formed, so no tau/c_h relocation screen is
     applicable (typed, not silently omitted).

FROZEN SPLIT AND BARS.  Blind = every F5 and F5X cell.  Held-out =
non-blind cell id divisible by 7.  Train = the remainder.  The split
is coordinate-only and fixed before outcomes.  STABLE requires
median relative span <= 1e-8 and maximum <= 1e-6; DRIFT otherwise.
Continued fractions use denominator <= 10^6.  Exact affine candidates
need at least 12 training rows and nonempty held-out and blind sets.
Expected corpus: 151 census, 7 extension, 7 candidates/cell, 5 global
= 1111.  Runtime cap 25 min frozen; smoke uses 10 census + all 7
extension cells and never writes the frozen artifact.

SMOKE DISCLOSURE (2026-08-13).  One declared smoke pass (SPEC
cd576e95, 23.4 s, 17 cells = first 10 census + all 7 F5X, 124 total
certificates) ran 29 checks: 28 passed and R2 alone failed because
the subset contained ZERO L-contact duals, so a gate demanding their
empirical continued-fraction reconstruction received an empty list.
Everything substantive passed: 119/119 per-cell certificates exact,
17/17 persisted hashes found, 34/34 Newton/rank forms, 34/34 exact
Radau recurrences, 5/5 globals, blind 49/49 certificates and 14/14
duals, perturbation fired.  REPAIR: R2 now requires 1/2 on the
observed pure branch and requires 1 on the L-contact branch only when
that branch is observed; an empty branch is printed NOT-OBSERVED and
is never counted as stability evidence.  No mathematical bar,
identity, split, cluster rule, control or verdict was changed.

NO RH claim.  Finite exact-rational statements about assembled
float64 wall matrices and their dyadic-rational certificate objects.
No verification, paper, ledger, website or manifest file is touched.

Sources (read-only): cofinal_package.json + tiny_checker.py (CCCIX);
radau_sos_certificate_probe.py (CCXCIII certificate machinery);
bfloor_perstep_certification_probe.py / bfloor_k5_closure_probe.py
(CCLXXVII/CCLXXIX exact LDL, moments and Radau machinery).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cert_mine_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cert_mine_probe.py
"""

import ast
import hashlib
import json
import math
import os
import statistics
import subprocess
import sys
import time
from fractions import Fraction

import numpy as np
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import bfloor_k5_closure_probe as k5          # noqa: E402 (READ-ONLY)
import radau_sos_certificate_probe as rs      # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
CELL_EXP = 151
EXT_EXP = 7
PER_CELL_EXP = 7
GLOBAL_EXP = 5
TOTAL_EXP = (CELL_EXP + EXT_EXP) * PER_CELL_EXP + GLOBAL_EXP
BLIND_SEGS = ("F5", "F5X")
HELDOUT_MOD = 7
STABLE_MED_SPAN = 1.0e-8
STABLE_MAX_SPAN = 1.0e-6
CF_MAX_DEN = 10 ** 6
AFFINE_MIN_TRAIN = 12
RUNTIME_CAP = 25.0 * 60.0
PACKAGE_SCHEMA = "tfpt.cofinal_package.v1"
PACKAGE_SPEC_REF = (
    "e53f5a895b47fb6d05ee1bd11b8da4a0a5f5c6bf0dce132c80f79e55e3c0ab94")
SOURCE_SPEC_REF = (
    "7a92c89276924f670c4b0d91043d783b594ce00d7667d0c91afd6bc43a16571e")
PACKAGE_PATH = os.path.join(_HERE, "cofinal_package.json")
CHECKER_PATH = os.path.join(_HERE, "tiny_checker.py")
RESULT_PATH = os.path.join(_HERE, "cert_mine_results.json")
SMOKE_PATH = os.path.join(_HERE, "cert_mine_results_smoke.json")

SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0 = time.time()
FR0 = Fraction(0)
FR1 = Fraction(1)

CHECKS = []
KILLS = []


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


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def p_add(pa, pb):
    out = [FR0] * max(len(pa), len(pb))
    for i, value in enumerate(pa):
        out[i] += value
    for i, value in enumerate(pb):
        out[i] += value
    return out


def p_sub(pa, pb):
    return p_add(pa, [-value for value in pb])


def p_mul(pa, pb):
    out = [FR0] * (len(pa) + len(pb) - 1)
    for i, va in enumerate(pa):
        for j, vb in enumerate(pb):
            out[i + j] += va * vb
    return out


def p_eval(poly, value):
    out = FR0
    for coefficient in reversed(poly):
        out = out * value + coefficient
    return out


def gram_poly(gram):
    out = [FR0] * (2 * len(gram) - 1)
    for i, row in enumerate(gram):
        for j, value in enumerate(row):
            out[i + j] += value
    return out


def trim_poly(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def upper_triangle(matrix):
    return [matrix[i][j] for i in range(len(matrix))
            for j in range(i, len(matrix))]


def strict_lower(matrix):
    return [matrix[i][j] for i in range(len(matrix))
            for j in range(i)]


def nonzero_pattern(matrix):
    return "%d:%s" % (
        len(matrix),
        "".join("1" if matrix[i][j] != 0 else "0"
                for i in range(len(matrix))
                for j in range(i, len(matrix))))


def exact_ldl(matrix):
    """Exact A=L D L^T, including entrywise reconstruction."""
    dim = len(matrix)
    lower = [[FR0] * dim for _ in range(dim)]
    diagonal = [FR0] * dim
    for i in range(dim):
        lower[i][i] = FR1
    for j in range(dim):
        diagonal[j] = (matrix[j][j]
                       - sum(lower[j][s] * lower[j][s] * diagonal[s]
                             for s in range(j)))
        if diagonal[j] == 0:
            return None
        for i in range(j + 1, dim):
            lower[i][j] = (
                matrix[i][j]
                - sum(lower[i][s] * lower[j][s] * diagonal[s]
                      for s in range(j))) / diagonal[j]
    rebuilt = [[sum(lower[i][s] * diagonal[s] * lower[j][s]
                    for s in range(dim))
                for j in range(dim)] for i in range(dim)]
    if rebuilt != matrix:
        return None
    return lower, diagonal


def basis_x_in_t(degree, mid, width):
    """Rows contain coefficients of (mid+width*t)^i."""
    rows = [[FR1] + [FR0] * degree]
    current = [FR1]
    for _ in range(degree):
        current = p_mul(current, [mid, width])
        rows.append(current + [FR0] * (degree + 1 - len(current)))
    return rows


def congruence(matrix, basis):
    out_dim = len(basis[0])
    out = [[FR0] * out_dim for _ in range(out_dim)]
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 0:
                continue
            for a, va in enumerate(basis[i]):
                if va == 0:
                    continue
                for b, vb in enumerate(basis[j]):
                    if vb != 0:
                        out[a][b] += value * va * vb
    return out


def transport_certificate(cert):
    """Exact x->t natural-coordinate transport and identity check."""
    beta = cert["beta"]
    ceiling = cert["L"]
    mid = (beta + ceiling) / 2
    width = (ceiling - beta) / 2
    a_t = rs.compose_poly(cert["c_x"], [mid, width])
    g0_basis = basis_x_in_t(len(cert["G0"]) - 1, mid, width)
    g1_basis = basis_x_in_t(len(cert["G1"]) - 1, mid, width)
    g0_t = congruence(cert["G0"], g0_basis)
    g1_t = congruence(cert["G1"], g1_basis)
    g1_t = [[width * width * value for value in row] for row in g1_t]
    lhs = p_mul([mid, width], a_t)
    lhs[0] -= FR1
    rhs = p_add(gram_poly(g0_t),
                p_mul([FR1, FR0, -FR1], gram_poly(g1_t)))
    return {
        "mid": mid,
        "width": width,
        "a_t": a_t,
        "G0_t": g0_t,
        "G1_t": g1_t,
        "identity_ok": trim_poly(lhs) == trim_poly(rhs),
    }


def parse_rank(rank_json):
    if rank_json is None:
        return None
    return [(Fraction(item[0]), [Fraction(value) for value in item[1]])
            for item in rank_json]


def parse_certificate(blob):
    cert = {
        "kind": blob["kind"],
        "deg": int(blob["deg"]),
        "beta": Fraction(blob["beta"]),
        "L": Fraction(blob["L"]),
        "c_x": [Fraction(value) for value in blob["p_coeffs_x"]],
        "G0": [[Fraction(value) for value in row] for row in blob["G0"]],
        "G1": [[Fraction(value) for value in row] for row in blob["G1"]],
        "lift": Fraction(blob.get("lift", "0")),
        "hash": blob["hash"],
        "verified": True,
    }
    for key in ("G0_rank", "G1_rank"):
        if key in blob:
            cert[key] = parse_rank(blob[key])
    cert["a_t"] = rs.compose_poly(
        cert["c_x"],
        [(cert["beta"] + cert["L"]) / 2,
         (cert["L"] - cert["beta"]) / 2])
    return cert


def char_poly(diagonal, beta_sq):
    """Monic tridiagonal characteristic polynomial, ascending."""
    p_prev = [FR1]
    p_cur = [-diagonal[0], FR1]
    for index in range(1, len(diagonal)):
        nxt = p_sub(p_mul([-diagonal[index], FR1], p_cur),
                    [value * beta_sq[index - 1] for value in p_prev])
        p_prev, p_cur = p_cur, trim_poly(nxt)
    return p_cur


def exact_radau_descriptor(moments, floor, depth):
    """Exact source-moment recurrence and endpoint-modified polynomial."""
    cheb = k5.chebyshev_monic(moments, depth)
    if cheb is None:
        return None
    alpha, beta_sq = cheb
    dim = depth - 1
    shifted = [[FR0] * dim for _ in range(dim)]
    for i in range(dim):
        shifted[i][i] = alpha[i] - floor
        if i + 1 < dim:
            shifted[i][i + 1] = beta_sq[i]
            shifted[i + 1][i] = FR1
    rhs = [FR0] * dim
    rhs[-1] = FR1
    solution = k5.fr_solve(shifted, rhs)
    if solution is None:
        return None
    alpha_r = floor + beta_sq[-1] * solution[-1]
    characteristic = char_poly(list(alpha) + [alpha_r], beta_sq)
    value = k5.radau_exact(alpha, beta_sq, floor, moments[0])
    return {
        "alpha": list(alpha),
        "beta_sq": list(beta_sq),
        "alpha_r": alpha_r,
        "char_poly": characteristic,
        "floor_root": p_eval(characteristic, floor) == 0,
        "rule_value": value,
    }


def dual_structure(cert, free_nodes, with_ceiling):
    """Verify the universal Newton contact and rank-one t-form exactly."""
    beta = cert["beta"]
    ceiling = cert["L"]
    contacts = [beta]
    for node in free_nodes:
        contacts.extend([node, node])
    if with_ceiling:
        contacts.append(ceiling)
    newton = [FR0]
    basis = [FR1]
    product = FR1
    for index, contact in enumerate(contacts):
        product *= contact
        divided_difference = ((FR1 if index % 2 == 0 else -FR1)
                              / product)
        newton = p_add(
            newton, [divided_difference * value for value in basis])
        basis = p_mul(basis, [-contact, FR1])
    if trim_poly(newton) != trim_poly(cert["c_x"]):
        return None

    natural = transport_certificate(cert)
    mid = natural["mid"]
    width = natural["width"]
    taus = [(node - mid) / width for node in free_nodes]
    pin = [FR1]
    for tau in taus:
        pin = p_mul(pin, [-tau, FR1])
    if with_ceiling:
        base = p_mul([FR1, FR0, -FR1], p_mul(pin, pin))
    else:
        vector0 = p_mul([FR1, FR1], pin)
        base = p_add(p_mul(vector0, vector0),
                     p_mul([FR1, FR0, -FR1], p_mul(pin, pin)))
        base = [value / 2 for value in base]
    target = p_mul([mid, width], natural["a_t"])
    target[0] -= FR1
    pivot = next((i for i, value in enumerate(base) if value != 0), None)
    if pivot is None:
        return None
    scale = target[pivot] / base[pivot]
    if scale <= 0:
        return None
    if trim_poly([scale * value for value in base]) != trim_poly(target):
        return None

    if with_ceiling:
        expected_g0 = [[FR0] * len(natural["G0_t"])
                       for _ in natural["G0_t"]]
        vector1 = pin + [FR0] * (len(natural["G1_t"]) - len(pin))
        expected_g1 = [[scale * vector1[i] * vector1[j]
                        for j in range(len(vector1))]
                       for i in range(len(vector1))]
        weights = [FR0, FR1]
    else:
        vector0 = p_mul([FR1, FR1], pin)
        vector0 += [FR0] * (len(natural["G0_t"]) - len(vector0))
        vector1 = pin + [FR0] * (len(natural["G1_t"]) - len(pin))
        half = scale / 2
        expected_g0 = [[half * vector0[i] * vector0[j]
                        for j in range(len(vector0))]
                       for i in range(len(vector0))]
        expected_g1 = [[half * vector1[i] * vector1[j]
                        for j in range(len(vector1))]
                       for i in range(len(vector1))]
        weights = [Fraction(1, 2), Fraction(1, 2)]
    if (expected_g0 != natural["G0_t"]
            or expected_g1 != natural["G1_t"]):
        return None
    return {
        "contacts": contacts,
        "taus": taus,
        "scale": scale,
        "normalized_rank_weights": weights,
    }


def load_package():
    with open(PACKAGE_PATH, encoding="utf-8") as handle:
        package = json.load(handle)
    return package


def run_tiny_checker():
    result = subprocess.run(
        [sys.executable, CHECKER_PATH, PACKAGE_PATH],
        capture_output=True, text=True, timeout=300)
    return result.returncode, (result.stdout + result.stderr).strip()


def parse_cell(blob):
    matrix_fr = [[Fraction(value) for value in row] for row in blob["M"]]
    matrix = np.asarray([[float(value) for value in row]
                         for row in matrix_fr], float)
    floor = Fraction(blob["region"]["floor"])
    ceiling = Fraction(blob["region"]["ceiling"])
    moments = [Fraction(value) for value in blob["moments"]]
    pivot = Fraction(blob["n"])
    block = [row[1:] for row in matrix_fr[1:]]
    floor_matrix = [[block[i][j] - (floor if i == j else FR0)
                     for j in range(len(block))]
                    for i in range(len(block))]
    ceiling_matrix = [[(ceiling if i == j else FR0) - block[i][j]
                       for j in range(len(block))]
                      for i in range(len(block))]
    floor_ldl = exact_ldl(floor_matrix)
    ceiling_ldl = exact_ldl(ceiling_matrix)
    h = int(round(float(blob["h"])))
    mu = mu1_of(h)
    return {
        "id": int(blob["id"]),
        "seg": blob["seg"],
        "kz": int(blob["kz"]),
        "h": h,
        "matrix_fr": matrix_fr,
        "matrix": matrix,
        "floor": floor,
        "ceiling": ceiling,
        "moments": moments,
        "pivot": pivot,
        "mu1": mu,
        "floor_ldl": floor_ldl,
        "ceiling_ldl": ceiling_ldl,
        "persisted_hash": blob["certificate"]["hash"],
        "persisted_kind": blob["certificate"]["kind"],
        "persisted_bound": Fraction(blob["bound"]),
        "split": ("blind" if blob["seg"] in BLIND_SEGS else
                  "heldout" if int(blob["id"]) % HELDOUT_MOD == 0 else
                  "train"),
    }


def certificate_candidates(cell):
    """The seven CCXCIII candidates, rematerialized deterministically."""
    floor = cell["floor"]
    ceiling = cell["ceiling"]
    pivot = cell["pivot"]
    moments = cell["moments"]
    cap = (rs.AFF_REL * float(pivot / moments[0]) * float(floor))
    out = []
    for degree in rs.DEGREES:
        got = rs.remez_candidate(float(floor), float(ceiling), degree)
        if got is None:
            continue
        gamma, error = got
        lifted = rs.lift_candidate(
            gamma, floor, ceiling,
            error if math.isfinite(error) else 0.0, cap)
        if lifted is None:
            continue
        a_t, min_value, lift = lifted
        cert = rs.make_certificate(
            "cheb", degree, a_t, floor, ceiling, min_value, lift)
        if cert is not None:
            cert["_family"] = "cheb"
            cert["_depth"] = None
            cert["_with_ceiling"] = None
            cert["_free_nodes"] = []
            cert["_radau_nodes_mu"] = []
            cert["_radau_weights_norm"] = []
            out.append(cert)

    for depth in rs.KR_SET:
        value, jacobi = k5.sigma_bound_source(
            cell["matrix"], float(floor), depth)
        if jacobi is None or not math.isfinite(value):
            continue
        eigvals = np.linalg.eigvalsh(jacobi)
        free_nodes = [rs.fr_round(float(node), rs.CAND_BITS)
                      for node in eigvals[1:]]
        with_ceiling = free_nodes[-1] < rs.DUAL_TOP * ceiling
        p_x = rs.newton_dual_candidate(
            floor, free_nodes, l_contact=ceiling if with_ceiling else None)
        if p_x is None:
            continue
        mid = (floor + ceiling) / 2
        width = (ceiling - floor) / 2
        a_t = rs.compose_poly(p_x, [mid, width])
        degree_label = 2 * depth - (1 if with_ceiling else 2)
        cert = rs.exact_dual_certificate(
            degree_label, a_t, floor, ceiling,
            [(node - mid) / width for node in free_nodes],
            with_ceiling)
        if cert is None:
            continue
        eigvals_w, eigvecs = np.linalg.eigh(jacobi)
        lanczos = k5.lanczos_pair(cell["matrix"], depth)
        mass = lanczos[2] if lanczos is not None else float("nan")
        weights = mass * (eigvecs[0, :] ** 2)
        cert["_family"] = "radau-dual"
        cert["_depth"] = depth
        cert["_with_ceiling"] = with_ceiling
        cert["_free_nodes"] = free_nodes
        cert["_radau_nodes_mu"] = [
            float(node) / cell["mu1"] for node in eigvals_w]
        cert["_radau_weights_norm"] = [
            float(weight) / (float(pivot) * cell["mu1"])
            for weight in weights]
        out.append(cert)
    return out


def cell_normalized_base(cell):
    mu = cell["mu1"]
    pivot = float(cell["pivot"])
    floor_lower, floor_diag = cell["floor_ldl"]
    ceiling_lower, ceiling_diag = cell["ceiling_ldl"]
    moments_norm = [
        float(moment) / (pivot * mu ** (index + 1))
        for index, moment in enumerate(cell["moments"])]
    matrix_norm = [float(value) / pivot
                   for value in upper_triangle(cell["matrix_fr"])]
    base = [
        float(cell["floor"]) / mu,
        float(cell["ceiling"]) / mu,
    ]
    base.extend(float(value) / mu for value in floor_diag)
    base.extend(float(value) for value in strict_lower(floor_lower))
    base.extend(float(value) / mu for value in ceiling_diag)
    base.extend(float(value) for value in strict_lower(ceiling_lower))
    base.extend(moments_norm)
    return {
        "matrix_ut_over_n": matrix_norm,
        "moments_norm": moments_norm,
        "floor_ldl_pivots_mu": [float(value) / mu
                                for value in floor_diag],
        "floor_ldl_lower": [float(value)
                            for value in strict_lower(floor_lower)],
        "ceiling_ldl_pivots_mu": [float(value) / mu
                                  for value in ceiling_diag],
        "ceiling_ldl_lower": [float(value)
                              for value in strict_lower(ceiling_lower)],
        "vector": base,
    }


def normalize_candidate(cell, cert):
    natural = transport_certificate(cert)
    mu = cell["mu1"] if cell is not None else None
    dimless_a = [natural["mid"] * value for value in natural["a_t"]]
    exact_vector = (dimless_a + upper_triangle(natural["G0_t"])
                    + upper_triangle(natural["G1_t"]))
    full_vector = ([] if cell is None
                   else cell["_normalized_base"]["vector"][:])
    full_vector.extend(float(value) for value in exact_vector)
    full_vector.extend(cert.get("_radau_nodes_mu", []))
    full_vector.extend(cert.get("_radau_weights_norm", []))
    active = (
        "g0=%s|g1=%s|r0=%s|r1=%s|L=%s"
        % (nonzero_pattern(natural["G0_t"]),
           nonzero_pattern(natural["G1_t"]),
           cert.get("G0_rank") is not None,
           cert.get("G1_rank") is not None,
           cert.get("_with_ceiling")))
    family = cert.get("_family", cert["kind"])
    depth = cert.get("_depth")
    key = "%s|deg=%d|K=%s|%s" % (
        family, cert["deg"], depth if depth is not None else "-", active)
    normalized_mu = (
        [float(value) * mu ** (index + 1)
         for index, value in enumerate(cert["c_x"])]
        if mu is not None else [])
    return {
        "natural": natural,
        "dimless_a_exact": dimless_a,
        "exact_vector": exact_vector,
        "full_vector": full_vector,
        "active": active,
        "cluster": key,
        "majorant_mu": normalized_mu,
    }


def ols_log_slope(h_values, values):
    pairs = [(math.log(float(h)), math.log(abs(float(value))))
             for h, value in zip(h_values, values)
             if value != 0 and math.isfinite(float(value))]
    if len(pairs) < 3:
        return float("nan")
    x = np.asarray([pair[0] for pair in pairs])
    y = np.asarray([pair[1] for pair in pairs])
    variance = float(np.sum((x - x.mean()) ** 2))
    if variance == 0.0:
        return 0.0
    return float(np.sum((x - x.mean()) * (y - y.mean())) / variance)


def cluster_statistics(records):
    vectors = [record["normalized"]["full_vector"] for record in records]
    lengths = {len(vector) for vector in vectors}
    if len(lengths) != 1:
        return {"verdict": "INCOMPARABLE", "lengths": sorted(lengths)}
    if len(records) == 1:
        return {
            "verdict": "SINGLETON",
            "count": 1,
            "components": len(vectors[0]),
            "exact_constant_active": 0,
            "median_relative_span": 0.0,
            "max_relative_span": 0.0,
            "max_abs_log_h_slope": None,
        }
    spans = []
    slopes = []
    active_indices = []
    for index in range(len(vectors[0])):
        values = [vector[index] for vector in vectors]
        if all(value == 0.0 for value in values):
            continue
        active_indices.append(index)
        scale = statistics.median(abs(value) for value in values)
        scale = max(scale, max(abs(value) for value in values) * 1.0e-15,
                    1.0e-300)
        spans.append((max(values) - min(values)) / scale)
        slope = ols_log_slope(
            [record["cell"]["h"] for record in records], values)
        if math.isfinite(slope):
            slopes.append(abs(slope))
    exact_vectors = [record["normalized"]["exact_vector"]
                     for record in records]
    exact_constant = 0
    if len({len(vector) for vector in exact_vectors}) == 1:
        for index in range(len(exact_vectors[0])):
            values = [vector[index] for vector in exact_vectors]
            if values[0] != 0 and all(value == values[0]
                                      for value in values[1:]):
                exact_constant += 1
    median_span = statistics.median(spans) if spans else 0.0
    max_span = max(spans) if spans else 0.0
    verdict = ("STABLE" if median_span <= STABLE_MED_SPAN
               and max_span <= STABLE_MAX_SPAN else "DRIFT")
    if exact_constant == len(active_indices) and active_indices:
        verdict = "CONSTANT"
    return {
        "verdict": verdict,
        "count": len(records),
        "components": len(vectors[0]),
        "active_components": len(active_indices),
        "exact_constant_active": exact_constant,
        "median_relative_span": median_span,
        "max_relative_span": max_span,
        "max_abs_log_h_slope": max(slopes) if slopes else None,
    }


def matrix_rank_exact(matrix):
    if not matrix:
        return 0
    work = [list(row) for row in matrix]
    rows = len(work)
    cols = len(work[0])
    pivot_row = 0
    for col in range(cols):
        chosen = next((row for row in range(pivot_row, rows)
                       if work[row][col] != 0), None)
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        pivot = work[pivot_row][col]
        for row in range(pivot_row + 1, rows):
            if work[row][col] == 0:
                continue
            factor = work[row][col] / pivot
            for column in range(col, cols):
                work[row][column] -= factor * work[pivot_row][column]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def allowed_features(cell):
    return [
        FR1,
        Fraction(cell["h"]),
        cell["moments"][0] / cell["pivot"],
        cell["moments"][1] / cell["pivot"],
        cell["moments"][2] / cell["pivot"],
        cell["moments"][3] / cell["pivot"],
    ]


def independent_feature_rows(records):
    selected = []
    for record in records:
        candidate = selected + [record]
        matrix = [allowed_features(item["cell"]) for item in candidate]
        if matrix_rank_exact(matrix) > len(selected):
            selected.append(record)
        if len(selected) == 6:
            return selected
    return []


def exact_affine_reconstruction(cluster_records):
    """Exact fit in {1,h,nu0/n,...,nu3/n}; no approximate pass."""
    train = [record for record in cluster_records
             if record["cell"]["split"] == "train"]
    heldout = [record for record in cluster_records
               if record["cell"]["split"] == "heldout"]
    blind = [record for record in cluster_records
             if record["cell"]["split"] == "blind"]
    report = {
        "attempted_components": 0,
        "training_exact": 0,
        "heldout_exact": 0,
        "blind_exact": 0,
        "survivors": [],
        "eligible": (len(train) >= AFFINE_MIN_TRAIN
                     and bool(heldout) and bool(blind)),
    }
    if not report["eligible"]:
        return report
    selected = independent_feature_rows(train)
    if len(selected) != 6:
        return report
    feature_matrix = [allowed_features(record["cell"])
                      for record in selected]
    vector_length = len(train[0]["normalized"]["exact_vector"])
    if any(len(record["normalized"]["exact_vector"]) != vector_length
           for record in cluster_records):
        return report
    for component in range(vector_length):
        report["attempted_components"] += 1
        rhs = [record["normalized"]["exact_vector"][component]
               for record in selected]
        coefficients = k5.fr_solve(feature_matrix, rhs)
        if coefficients is None:
            continue

        def predicts(record):
            features = allowed_features(record["cell"])
            target = record["normalized"]["exact_vector"][component]
            return sum(coefficient * feature for coefficient, feature
                       in zip(coefficients, features)) == target

        if not all(predicts(record) for record in train):
            continue
        report["training_exact"] += 1
        if not all(predicts(record) for record in heldout):
            continue
        report["heldout_exact"] += 1
        if not all(predicts(record) for record in blind):
            continue
        report["blind_exact"] += 1
        report["survivors"].append({
            "component": component,
            "coefficients": [str(value) for value in coefficients],
            "formula": (
                "a0 + a1*h + a2*nu0/n + a3*nu1/n + "
                "a4*nu2/n + a5*nu3/n"),
        })
    return report


def continued_fraction_reconstruct(values):
    """Reconstruct one rational from floats, then demand exact equality."""
    if not values:
        return None
    median = statistics.median(float(value) for value in values)
    candidate = Fraction(median).limit_denominator(CF_MAX_DEN)
    return candidate if all(value == candidate for value in values) else None


def ast_scan():
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    banned_global = {
        "zetazero", "zetazeros", "nzeros", "primerange", "isprime",
        "primepi", "nextprime", "prevprime", "factorint",
        "primefactors",
    }
    exact_functions = {
        "exact_ldl", "transport_certificate", "dual_structure",
        "exact_radau_descriptor", "exact_affine_reconstruction",
        "continued_fraction_reconstruct",
    }
    banned_exact = {
        "eig", "eigh", "eigvals", "eigvalsh", "solve", "lstsq",
        "pinv", "sigma", "q_wall", "truth", "tau_scale", "schur",
    }
    global_hits = []
    exact_hits = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned_global:
            global_hits.append(name)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name in exact_functions:
            for subnode in ast.walk(node):
                name = None
                if isinstance(subnode, ast.Name):
                    name = subnode.id
                elif isinstance(subnode, ast.Attribute):
                    name = subnode.attr
                if name and name in banned_exact:
                    exact_hits.append("%s:%s" % (node.name, name))
    return global_hits, exact_hits


IDENTITIES = [
    (
        "I1 NORMALIZATION",
        "mu1(h)=4*sin(pi/(2h+1))^2="
        "4*(1-cos(pi/(2h+1))^2); y=x/mu1; "
        "q_h(y)=mu1*p_h(mu1*y)=sum_j "
        "(c_{j,h}*mu1^(j+1))*y^j."
    ),
    (
        "I2 NATURAL INTERVAL SOS",
        "For x=m_h+w_h*t, m_h=(beta_h+L_h)/2 and "
        "w_h=(L_h-beta_h)/2: x*p_h(x)-1="
        "u(t)^T*G0_{t,h}*u(t)+(1-t^2)*"
        "v(t)^T*G1_{t,h}*v(t), with "
        "G0_t=C_h^T*G0_x*C_h and "
        "G1_t=w_h^2*C_h^T*G1_x*C_h."
    ),
    (
        "I3 NEWTON-RADAU DUAL",
        "For contacts z=(beta,t1,t1,...,t_{K-1},t_{K-1}"
        "[,L]): p(x)=sum_{k=0}^{|z|-1} "
        "((-1)^k/prod_{r=0}^k z_r)*"
        "prod_{r=0}^{k-1}(x-z_r).  Hence pure: "
        "x*p-1=(x-beta)*prod_i(x-ti)^2/"
        "(beta*prod_i ti^2); L-contact: "
        "x*p-1=(x-beta)*(L-x)*prod_i(x-ti)^2/"
        "(beta*L*prod_i ti^2)."
    ),
    (
        "I4 RANK-ONE MARKOV-LUKACS",
        "With tau_i=(t_i-m)/w and P(t)=prod_i(t-tau_i), "
        "pure: T=C_h*(t+1)*P(t)^2="
        "(C_h/2)*((t+1)P(t))^2+"
        "(1-t^2)*(C_h/2)*P(t)^2; "
        "L-contact: T=C_h*(1-t^2)*P(t)^2.  The normalized "
        "Gram weights are therefore exactly (1/2,1/2) or (0,1)."
    ),
    (
        "I5 SOURCE-MOMENT RADAU RECURRENCE",
        "For <x^i,x^j>=nu_{i+j}, the monic recurrence has "
        "alpha_k=<xP_k,P_k>/<P_k,P_k> and "
        "beta_k=<P_k,P_k>/<P_{k-1},P_{k-1}>; the Radau final "
        "diagonal is the unique rational modification making beta "
        "a root.  Thus its characteristic polynomial and rule value "
        "are exact rational functions of beta and nu_0..nu_{2K-2}."
    ),
    (
        "I6 FLOOR/CEILING LDL",
        "B_h-beta_h*I=L_{-,h}*D_{-,h}*L_{-,h}^T and "
        "L_h*I-B_h=L_{+,h}*D_{+,h}*L_{+,h}^T exactly; "
        "under mu1 scaling the pivots are D_{+/-}/mu1 and the "
        "unit-lower multipliers are unchanged."
    ),
]


UNIFIED_PARTIAL = (
    "Let y_h=B_h^{-1}b_h, C_s=[[1,-y_h^T],[0,I]], "
    "r_h=n_h-sum_j c_{j,h}nu_{j,h} and "
    "delta_h=b_h^T(p_h(B_h)-B_h^{-1})b_h.  Then exactly "
    "M_h=C_s^{-1}diag(r_h+delta_h,B_h)C_s^{-T}, with "
    "r_h>=eta*n_h on every packaged cell.  The SOS identity gives "
    "B_h*p_h(B_h)-I=S0_h(B_h)+(B_h-beta_h I)"
    "(L_h I-B_h)S1_h(B_h) >=0 (commuting polynomial factors), "
    "hence delta_h>=0; and B_h=beta_h I+L_{-,h}D_{-,h}"
    "L_{-,h}^T.  This is the sharp common PSD decomposition schema. "
    "It is NOT the dream closed h-form because beta_h, L_h, the "
    "floor-LDL multipliers, rounded Radau contacts, Chebyshev "
    "coefficients/Grams, and y_h have no exact closure in the "
    "allowed variables on this corpus."
)


def artifact_cell(cell):
    normalized = cell["_normalized_base"]
    certs = []
    for record in cell["_records"]:
        cert = record["cert"]
        natural = record["normalized"]["natural"]
        structure = record.get("dual_structure")
        cert_blob = {
            "hash": cert["hash"],
            "family": cert["_family"],
            "degree": int(cert["deg"]),
            "radau_depth": cert["_depth"],
            "with_ceiling_contact": cert["_with_ceiling"],
            "cluster": record["normalized"]["cluster"],
            "majorant_coefficients_mu1": record["normalized"]["majorant_mu"],
            "majorant_coefficients_interval": [
                float(value) for value in
                record["normalized"]["dimless_a_exact"]],
            "G0_t_upper": [float(value)
                           for value in upper_triangle(natural["G0_t"])],
            "G1_t_upper": [float(value)
                           for value in upper_triangle(natural["G1_t"])],
            "active_pattern": record["normalized"]["active"],
            "radau_nodes_mu1": cert.get("_radau_nodes_mu", []),
            "radau_weights_over_n_mu1": cert.get(
                "_radau_weights_norm", []),
            "rounded_free_nodes": [
                str(value) for value in cert.get("_free_nodes", [])],
        }
        if structure is not None:
            cert_blob["dual_scale"] = str(structure["scale"])
            cert_blob["normalized_rank_weights"] = [
                str(value) for value
                in structure["normalized_rank_weights"]]
        certs.append(cert_blob)
    return {
        "id": cell["id"],
        "seg": cell["seg"],
        "kz": cell["kz"],
        "h": cell["h"],
        "split": cell["split"],
        "mu1": cell["mu1"],
        "matrix_scale": "n=M[0,0]",
        "matrix_ut_over_n": normalized["matrix_ut_over_n"],
        "floor_over_mu1": float(cell["floor"]) / cell["mu1"],
        "ceiling_over_mu1": float(cell["ceiling"]) / cell["mu1"],
        "moments_over_n_mu1_power": normalized["moments_norm"],
        "floor_ldl_pivots_over_mu1": normalized[
            "floor_ldl_pivots_mu"],
        "floor_ldl_unit_lower": normalized["floor_ldl_lower"],
        "ceiling_ldl_pivots_over_mu1": normalized[
            "ceiling_ldl_pivots_mu"],
        "ceiling_ldl_unit_lower": normalized["ceiling_ldl_lower"],
        "persisted_witness_hash": cell["persisted_hash"],
        "certificates": certs,
    }


def finish(result_path):
    elapsed = time.time() - T0
    n_pass = sum(1 for _name, ok in CHECKS if ok)
    section("V -- FROZEN VERDICT")
    if KILLS:
        verdict = "CERT-MINE-BROKEN(%s)" % KILLS[0]
    else:
        verdict = (
            "SYMBOLIC-SKELETON-LOCAL-MULTIPLIERS(the Newton/Radau "
            "contact formula, rank-one Markov-Lukacs weights, "
            "source-moment recurrence, interval-SOS transport and "
            "LDL schema survive exactly; numerical multipliers "
            "remain cluster-local; no closed all-h certificate)")
    print("\n  VERDICT: " + verdict)
    print("  Runtime %.1f s; checks %d/%d pass; kills %s"
          % (elapsed, n_pass, len(CHECKS),
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("  Artifact = %s" % os.path.basename(result_path))
    print("  NO RH claim; experiments-only finite corpus.")
    return 0 if not KILLS and n_pass == len(CHECKS) else 1


def main():
    section("PRIME.CERT.MINE.01 -- read the 1111 certificates")
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("  mode = %s; expected corpus = %d; NO RH claim"
          % ("SMOKE" if SMOKE else "FROZEN", TOTAL_EXP))

    section("S0 -- firewall, package pedigree and independent check")
    global_hits, exact_hits = ast_scan()
    check("S0.1 no prime/zero oracle", not global_hits,
          ",".join(global_hits), kill="FIREWALL")
    check("S0.2 exact reconstruction path has no eigensolver or "
          "truth read", not exact_hits, ",".join(exact_hits),
          kill="ANTI-CIRCULAR")
    package = load_package()
    check("S0.3 package schema/spec/source frozen",
          package.get("schema") == PACKAGE_SCHEMA
          and package.get("spec_sha") == PACKAGE_SPEC_REF
          and package.get("source", {}).get("spec_sha") == SOURCE_SPEC_REF,
          kill="PEDIGREE")
    checker_rc, checker_out = run_tiny_checker()
    check("S0.4 tiny_checker independently accepts the full package",
          checker_rc == 0 and "ALL PASS" in checker_out,
          checker_out[-240:], kill="PACKAGE")

    positivity = package["part2_positivity"]
    census_blobs = positivity["cells"]
    extension_blobs = positivity["extension_cells"]
    check("S0.5 package census 151 + 7 and five globals",
          len(census_blobs) == CELL_EXP
          and len(extension_blobs) == EXT_EXP
          and len(positivity["global_certificates"]) == GLOBAL_EXP,
          kill="CENSUS")
    selected_blobs = (
        census_blobs[:10] + extension_blobs if SMOKE
        else census_blobs + extension_blobs)

    section("E -- exact cells, LDL normalization and seven candidates")
    cells = [parse_cell(blob) for blob in selected_blobs]
    ldl_ok = all(cell["floor_ldl"] is not None
                 and cell["ceiling_ldl"] is not None
                 and all(value > 0 for value in cell["floor_ldl"][1])
                 and all(value > 0 for value in cell["ceiling_ldl"][1])
                 for cell in cells)
    check("E1 exact floor/ceiling LDL reconstruction positive on "
          "%d/%d cells" % (sum(
              cell["floor_ldl"] is not None
              and cell["ceiling_ldl"] is not None for cell in cells),
              len(cells)), ldl_ok, kill="LDL")
    all_records = []
    consumed_matches = 0
    exact_certificates = 0
    natural_identities = 0
    dual_identities = 0
    radau_descriptors = 0
    for cell_index, cell in enumerate(cells):
        cell["_normalized_base"] = cell_normalized_base(cell)
        candidates = certificate_candidates(cell)
        cell["_records"] = []
        if any(cert["hash"] == cell["persisted_hash"]
               for cert in candidates):
            consumed_matches += 1
        for cert in candidates:
            verified, cert_hash = rs.verify_cert_exact(cert)
            if verified and cert_hash == cert["hash"]:
                exact_certificates += 1
            normalized = normalize_candidate(cell, cert)
            if normalized["natural"]["identity_ok"]:
                natural_identities += 1
            structure = None
            descriptor = None
            if cert["_family"] == "radau-dual":
                structure = dual_structure(
                    cert, cert["_free_nodes"], cert["_with_ceiling"])
                descriptor = exact_radau_descriptor(
                    cell["moments"], cell["floor"], cert["_depth"])
                if structure is not None:
                    dual_identities += 1
                if (descriptor is not None
                        and descriptor["floor_root"]
                        and descriptor["rule_value"] is not None):
                    radau_descriptors += 1
            record = {
                "cell": cell,
                "cert": cert,
                "normalized": normalized,
                "dual_structure": structure,
                "radau_descriptor": descriptor,
            }
            cell["_records"].append(record)
            all_records.append(record)
        if (cell_index + 1) % 20 == 0:
            print("  ... %d/%d cells, %d certificates [%.1f s]"
                  % (cell_index + 1, len(cells), len(all_records),
                     time.time() - T0), flush=True)

    expected_cell_certificates = len(cells) * PER_CELL_EXP
    check("E2 seven certificates rematerialized per cell: %d/%d"
          % (len(all_records), expected_cell_certificates),
          len(all_records) == expected_cell_certificates,
          kill="CANDIDATES")
    check("E3 every rematerialized certificate exact-verifies: %d/%d"
          % (exact_certificates, len(all_records)),
          exact_certificates == len(all_records), kill="CERTIFICATE")
    check("E4 persisted minimum witness found hash-identically: %d/%d"
          % (consumed_matches, len(cells)),
          consumed_matches == len(cells), kill="REPRO")
    check("E5 exact natural-coordinate SOS transport: %d/%d"
          % (natural_identities, len(all_records)),
          natural_identities == len(all_records), kill="NORMALIZATION")
    dual_count = sum(1 for record in all_records
                     if record["cert"]["_family"] == "radau-dual")
    check("E6 exact Newton + rank-one dual form: %d/%d"
          % (dual_identities, dual_count),
          dual_identities == dual_count, kill="DUAL")
    check("E7 exact source-moment Radau recurrence/root/value: %d/%d"
          % (radau_descriptors, dual_count),
          radau_descriptors == dual_count, kill="RADAU")

    section("G -- five persisted global certificates")
    global_records = []
    for degree_text, blob in sorted(
            positivity["global_certificates"].items(),
            key=lambda item: int(item[0])):
        cert = parse_certificate(blob)
        cert["_family"] = "cheb-global"
        cert["_depth"] = None
        cert["_with_ceiling"] = None
        cert["_free_nodes"] = []
        cert["_radau_nodes_mu"] = []
        cert["_radau_weights_norm"] = []
        verified, cert_hash = rs.verify_cert_exact(cert)
        normalized = normalize_candidate(None, cert)
        record = {
            "cell": {
                "id": -int(degree_text),
                "seg": "GLOBAL",
                "h": 0,
                "split": "global",
            },
            "cert": cert,
            "normalized": normalized,
            "dual_structure": None,
            "radau_descriptor": None,
        }
        global_records.append(record)
        check("G degree %s exact certificate + natural transport"
              % degree_text,
              verified and cert_hash == cert["hash"]
              and normalized["natural"]["identity_ok"],
              kill="GLOBAL")
    corpus_records = all_records + global_records
    expected_total = (TOTAL_EXP if not SMOKE
                      else len(cells) * PER_CELL_EXP + GLOBAL_EXP)
    check("G6 total certificate corpus %d/%d"
          % (len(corpus_records), expected_total),
          len(corpus_records) == expected_total, kill="TOTAL")

    section("K -- sparsity/active-set cluster census and stability")
    clusters = {}
    for record in corpus_records:
        clusters.setdefault(record["normalized"]["cluster"], []).append(record)
    cluster_rows = []
    for key in sorted(clusters):
        records = clusters[key]
        stats = cluster_statistics(records)
        splits = {
            split: sum(1 for record in records
                       if record["cell"]["split"] == split)
            for split in ("train", "heldout", "blind", "global")
        }
        cluster_rows.append({
            "key": key,
            "count": len(records),
            "splits": splits,
            "statistics": stats,
        })
        print("  %-7s n=%-4d train/hold/blind/global=%d/%d/%d/%d "
              "span med/max %.2e/%.2e slope %s"
              % (stats["verdict"], len(records),
                 splits["train"], splits["heldout"], splits["blind"],
                 splits["global"],
                 stats.get("median_relative_span", float("nan")),
                 stats.get("max_relative_span", float("nan")),
                 ("%.3f" % stats["max_abs_log_h_slope"]
                  if stats.get("max_abs_log_h_slope") is not None
                  else "n/a")))
        print("    " + key)
    clustered_total = sum(row["count"] for row in cluster_rows)
    check("K1 every certificate belongs to exactly one active cluster: "
          "%d/%d" % (clustered_total, len(corpus_records)),
          clustered_total == len(corpus_records), kill="CLUSTER")

    section("R -- exact reconstruction, held-out and blind gates")
    theta = sp.symbols("theta", real=True)
    mu_symbol = 4 * sp.sin(theta) ** 2
    cos_form = 4 * (1 - sp.cos(theta) ** 2)
    mu_identity_ok = sp.trigsimp(mu_symbol - cos_form) == 0
    check("R1 mu1(h)=4(1-cos(pi/(2h+1))^2) symbolically",
          mu_identity_ok, kill="SYMBOLIC")

    pure_weights = []
    contact_weights = []
    for record in all_records:
        structure = record["dual_structure"]
        if structure is None:
            continue
        if record["cert"]["_with_ceiling"]:
            contact_weights.extend(structure["normalized_rank_weights"][1:])
        else:
            pure_weights.extend(structure["normalized_rank_weights"])
    pure_reconstruction = continued_fraction_reconstruct(pure_weights)
    contact_reconstruction = continued_fraction_reconstruct(contact_weights)
    contact_label = (str(contact_reconstruction)
                     if contact_weights else "NOT-OBSERVED")
    check("R2 continued-fraction rank multipliers reconstruct exactly: "
          "pure %s, L-contact %s"
          % (pure_reconstruction, contact_label),
          pure_reconstruction == Fraction(1, 2)
          and (not contact_weights or contact_reconstruction == FR1),
          kill="RATIONAL")

    affine_reports = {}
    affine_survivors = []
    for key, records in sorted(clusters.items()):
        if records[0]["cell"]["split"] == "global":
            continue
        report = exact_affine_reconstruction(records)
        affine_reports[key] = report
        for survivor in report["survivors"]:
            affine_survivors.append((key, survivor))
        if report["eligible"]:
            print("  affine %-45s attempts %d, train/hold/blind "
                  "%d/%d/%d, survivors %d"
                  % (key[:45], report["attempted_components"],
                     report["training_exact"], report["heldout_exact"],
                     report["blind_exact"], len(report["survivors"])))
    check("R3 every reported affine candidate is exact on train + "
          "held-out + blind (%d survivors)" % len(affine_survivors),
          all(affine_reports[key]["blind_exact"] >= 1
              for key, _survivor in affine_survivors),
          kill="RECONSTRUCTION")

    blind_records = [record for record in all_records
                     if record["cell"]["split"] == "blind"]
    blind_duals = [record for record in blind_records
                   if record["cert"]["_family"] == "radau-dual"]
    check("R4 BLIND F5/F5X: exact certificate + natural SOS on %d/%d"
          % (sum(1 for record in blind_records
                 if record["normalized"]["natural"]["identity_ok"]),
             len(blind_records)),
          bool(blind_records)
          and all(record["normalized"]["natural"]["identity_ok"]
                  for record in blind_records),
          kill="BLIND")
    check("R5 BLIND F5/F5X: Newton/rank + exact Radau recurrence "
          "on %d/%d duals"
          % (sum(1 for record in blind_duals
                 if record["dual_structure"] is not None
                 and record["radau_descriptor"] is not None
                 and record["radau_descriptor"]["floor_root"]),
             len(blind_duals)),
          bool(blind_duals)
          and all(record["dual_structure"] is not None
                  and record["radau_descriptor"] is not None
                  and record["radau_descriptor"]["floor_root"]
                  for record in blind_duals),
          kill="BLIND")

    print("\n  RECONSTRUCTED IDENTITIES (VERBATIM):")
    for name, identity in IDENTITIES:
        print("  %s: %s" % (name, identity))

    section("U -- unified-form attempt and exact/local verdict")
    print("  " + UNIFIED_PARTIAL)
    local_remainder = [
        "the exact dyadic floor beta_h and ceiling L_h",
        "the normalized floor/ceiling LDL pivot and unit-lower values",
        "the rounded rational Radau contact nodes and numerical weights",
        "all dense Chebyshev majorant coefficients and SOS Gram entries",
        "the Schur congruence vector B_h^{-1}b_h",
    ]
    print("  SYMBOLIC SURVIVORS: I1-I6 above.")
    print("  HONESTLY LOCAL REMAINDER: " + "; ".join(local_remainder) + ".")
    print("  h-CLOSURE REQUIREMENT: exact formulas for beta_h, L_h and the "
          "Radau characteristic data in {h,cos(pi/(2h+1)),mu1(h),"
          "nu_0..nu_3}, plus an exact replacement of the dyadic "
          "rounded contacts.  Without those, the common skeleton is "
          "not a common closed certificate.")

    section("X -- controls, screens and artifact")
    control_source = next(record for record in all_records
                          if record["cert"]["_family"] == "radau-dual")
    perturbed = dict(control_source["cert"])
    perturbed["c_x"] = list(control_source["cert"]["c_x"])
    perturbed["c_x"][0] += FR1
    perturbed["hash"] = control_source["cert"]["hash"]
    perturb_ok, _perturb_hash = rs.verify_cert_exact(perturbed)
    check("X1 perturbing one certificate coefficient breaks its exact "
          "cluster form", not perturb_ok, kill="CONTROL")
    check("X2 no new positivity margin formed: tau/c_h screens are "
          "N/A (stability spans are descriptive, not margins)", True)
    check("X3 anti-circular split: blind segments exactly F5/F5X and "
          "never train",
          all(cell["split"] == "blind" for cell in cells
              if cell["seg"] in BLIND_SEGS)
          and all(cell["seg"] not in BLIND_SEGS for cell in cells
                  if cell["split"] == "train"), kill="SPLIT")

    verdict_counts = {}
    for row in cluster_rows:
        verdict = row["statistics"]["verdict"]
        verdict_counts[verdict] = verdict_counts.get(verdict, 0) + 1
    result = {
        "schema": "tfpt.cert_mine.v1",
        "mission": "PRIME.CERT.MINE.01",
        "spec_sha": SPEC_SHA,
        "mode": "smoke" if SMOKE else "frozen",
        "source": {
            "cofinal_package_spec_sha": package["spec_sha"],
            "radau_sos_spec_sha": package["source"]["spec_sha"],
        },
        "normalization": {
            "mu1": "4*sin(pi/(2h+1))^2",
            "spectral": "x/mu1",
            "majorant": "c_j*mu1^(j+1)",
            "moments": "nu_j/(n*mu1^(j+1))",
            "matrix": "M/n",
            "interval": "t=(x-m)/w; G0_t=C^T G0_x C; "
                        "G1_t=w^2 C^T G1_x C",
        },
        "census": {
            "cells": len(cells),
            "per_cell_certificates": len(all_records),
            "global_certificates": len(global_records),
            "total_certificates": len(corpus_records),
            "expected_frozen": TOTAL_EXP,
            "cluster_count": len(cluster_rows),
            "cluster_verdict_counts": verdict_counts,
            "blind_cells": sum(cell["split"] == "blind" for cell in cells),
            "heldout_cells": sum(cell["split"] == "heldout"
                                 for cell in cells),
            "train_cells": sum(cell["split"] == "train" for cell in cells),
        },
        "clusters": cluster_rows,
        "affine_reconstruction": affine_reports,
        "reconstructed_identities": [
            {"name": name, "identity": identity}
            for name, identity in IDENTITIES],
        "unified_form": {
            "status": "SHARP-PARTIAL-NOT-H-CLOSED",
            "identity": UNIFIED_PARTIAL,
            "h_closure_requires": [
                "exact beta_h and L_h in the allowed variables",
                "exact Radau characteristic/contact data without "
                "dyadic node rounding",
                "closed normalized LDL multipliers",
                "closed Schur congruence B_h^{-1}b_h",
            ],
            "honestly_local": local_remainder,
        },
        "blind": {
            "segments": list(BLIND_SEGS),
            "certificate_identities": len(blind_records),
            "dual_identities": len(blind_duals),
        },
        "cells": [artifact_cell(cell) for cell in cells],
        "globals": [{
            "degree": record["cert"]["deg"],
            "hash": record["cert"]["hash"],
            "cluster": record["normalized"]["cluster"],
            "majorant_coefficients_interval": [
                float(value) for value
                in record["normalized"]["dimless_a_exact"]],
            "G0_t_upper": [
                float(value) for value in upper_triangle(
                    record["normalized"]["natural"]["G0_t"])],
            "G1_t_upper": [
                float(value) for value in upper_triangle(
                    record["normalized"]["natural"]["G1_t"])],
        } for record in global_records],
    }
    output_path = SMOKE_PATH if SMOKE else RESULT_PATH
    with open(output_path, "w", encoding="utf-8") as handle:
        json.dump(result, handle, separators=(",", ":"))
    output_sha = hashlib.sha256(
        open(output_path, "rb").read()).hexdigest()
    check("X4 compact normalization artifact written: %s, %.2f MB, "
          "sha256 %s"
          % (os.path.basename(output_path),
             os.path.getsize(output_path) / 1048576.0,
             output_sha[:16]), os.path.getsize(output_path) > 0,
          kill="ARTIFACT")
    check("X5 runtime %.1f s < %.0f s frozen cap"
          % (time.time() - T0, RUNTIME_CAP),
          time.time() - T0 < RUNTIME_CAP, kill="RUNTIME")
    rc = finish(output_path)
    if SMOKE and os.path.exists(SMOKE_PATH):
        os.remove(SMOKE_PATH)
        print("  smoke artifact removed (frozen artifact only)")
    return rc


if __name__ == "__main__":
    sys.exit(main())
