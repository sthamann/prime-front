#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zolotarev_phase_filter_probe -- PRIME.ONEBADMODE.ZOLOTAREV.PHASE.01
(EXPLORATION ONLY, experiments/; rational determinant-phase form of
the finite ONEBADMODE wall certificate.  2026-08-12.)

MISSION.  Replace the order-r Chebyshev polynomial separator of CCVII
(r* = 14/30/119 on 68 finite wall steps) by a proper Zolotarev
rational sign separator with m conjugate pole pairs.  For c > 0 and
L > c, put eps = c/L and

  f_m(t) = t prod_{j=1}^{m-1}(t^2 + c_{2j})
                 / prod_{j=1}^{m}(t^2 + c_{2j-1}),
  c_j = eps^2 sn^2(j K(k')/(2m), k') /
                    cn^2(j K(k')/(2m), k'),  k'^2 = 1-eps^2.

The c_j are the classical Zolotarev elliptic nodes.  A ONE-SIDED
normalization D_m = 1 / sup_{t>=0} f_m(t), enclosed by outward-rounded
interval boxes below, gives

  R_m(x) = 1 - D_m f_m(x/L).

The construction has three exact sign facts.  All c_j and D_m are
positive; hence R_m(x) >= 1 for every x <= 0.  The interval enclosure
certifies D_m f_m(t) <= 1 for every t >= 0, hence R_m >= 0 on the whole
real axis.  On [c,L], the same enclosure gives
0 <= R_m <= delta_m = 1 - D_m inf_[eps,1] f_m.  Therefore
tr R_m(M) < 1 is an UNCONDITIONAL positivity certificate: a
nonpositive eigenvalue contributes at least one and every other
eigenvalue contributes nonnegatively.  The B-floor/interlacing premise
is used only to explain feasibility, never soundness.

PROPER PARTIAL-FRACTION / PHASE FORM.  Since f_m has type
(2m-1,2m), no polynomial tail occurs.  With poles
z_j = i L sqrt(c_{2j-1}) and real residues a_j,

  R_m(x) = 1 + sum_j [a_j/(x-z_j) + a_j/(x-conj(z_j))],
  tr R_m(M) = 8 + 2 Re sum_j a_j tr(M-z_j I)^-1,
  tr(M-zI)^-1 = -d/dz log det(M-zI).

The CERTIFICATE PATH evaluates only these resolvent traces by pivoted
LU solves.  Eigenvalues occur only in truth-reference, soundness and
interlacing wards.  Each frozen truth rung stores det(M-z_j I), its
principal log phase, an h-unwrapped phase, the resolvent trace and the
finite-difference log-det derivative ward in the compact JSON artifact
zolotarev_phase_filter_phases.json.

FROZEN QUESTIONS.
 A  FILTER.  Build both per-rung filters [c_B,L_src(h)] and one GLOBAL
    filter [c_B,max_h L_src(h)] for m=1..M_MAX.  Separator facts are
    certified over the ENTIRE real axis by interval boxes: [0,eps],
    [eps,1], and the reciprocal tail t=1/u, u in [0,1].  Each factor is
    monotone inside a box, so endpoint products give an enclosure;
    ROUND_PAD expands every box outward.  Dense samples are diagnostics.
 B  CENSUS.  The per-rung m*(h), the minimal GLOBAL m per rung, and the
    minimal FIXED m whose single pole set certifies all 68 steps are
    measured.  Margins 1-tr R in dex, h trend, source-only L looseness
    and segment census are printed.  Partial fractions tie the
    eigensum truth reference; only the former enters decisions.
 C  CONTROLS.  Reuse CCVII verbatim: smooth, scramble seed 1, Epstein
    x^2+5y^2 at kz 9 (rung fire; step ladder remains the predecessor's
    declared O(X^2) skip), and cosh injection A=.01.  Every indefinite
    step must have zero raw certificates.  Genuinely positive cosh
    cores are listed and eig-confirmed, never hidden.
 D  DISGUISE.  Repeat CCVII's rational counterparts: tau screens of
    per-rung and fixed-global margins; n-read sensitivity
    dn*=(1-trR)/|d trR/dM_00| from squared resolvents, normalized by the
    Schur gap s.  No target eigendatum enters either diagnostic.
 E  PHASE.  Store the determinant values/phases at the fixed filter
    poles and ward the resolvent/log-det identity on every rung/pole.
    If an Euler-phase artifact exists, match by (h,kz) and compare
    unwrapped h-dependence; otherwise print and store the exact
    follow-up matching specification.

ANTI-CIRCULARITY / EXACTNESS MODEL.  The deployed finite ladder,
Householder frames, three-way source split, controls and source-only
L_src=min(Gershgorin,Frobenius)*(1+2^-40) are imported READ-ONLY from
onebadmode_moments_probe (CCVII).  c_B=0.5523 is CITED from CLIII for
the certified surface range; the deep floor and deep ladder are
FLOAT-LEVEL (CLIV).  The bridge exception is typed honestly.  Elliptic
nodes use scipy.special; separator statements are machine-certified
for the float-committed nodes and outward-padded interval arithmetic.
LU is float64 with route/identity wards.  Positivity on these finitely
many float64-computed rungs proves nothing at other h.

EXTERNAL-CITED PEDIGREE.  The minimax rational sign construction and
its elliptic nodes are Zolotarev (1877), as presented in N. I.
Akhiezer, Theory of Approximation, Dover (1992), Ch. 9, and in van den
Eshof et al., Comput. Phys. Commun. 146 (2002) 203-224.  CONSUMED:
the elliptic-node product giving logarithmic-in-accuracy rational
order.  NOT CONSUMED: any asymptotic wall claim.  The one-sided
normalization and all separator inequalities used here are re-certified
directly, rather than borrowed from the citation.

GATES (kill -> WARD-BROKEN unless pipeline count failure).
 W1  CCVII reproduction: 42 surface rungs; 28 deep rungs; combined
     steps exactly 68 = 40 surface + 1 bridge + 27 deep; P2/P3 and
     deep B-floor reference values reproduce.
 M1  every constructed filter has certified global R>=0, R>=1 on
     x<=0, and bulk 0<=R<=delta; diagnostic-grid defect <= 2e-10.
 M2  partial-fraction trace vs eigensum truth reference <= PF_TIE on
     every truth decision at local m* and every fixed-global decision.
 M3  interlacing and source-only L soundness reproduce CCVII.
 M4  resolvent/log-det derivative identity <= LOGDET_WARD on every
     stored rung/pole; phase expression equals the certificate trace.
 E1-E4 controls fire at rung level; E5 has zero certificates on every
     eig-indefinite control step.

FROZEN BARS.  NDIM=8; c_B=5523/10000; M_MAX=20; interval boxes
LEFT/TARGET/TAIL=1024/8192/4096; ROUND_PAD=512 eps per factor;
GRID_WARD=2e-10; PF_TIE=2e-8; LOGDET_WARD=2e-6;
ILACE_TOL=1e-10; SOUND_TOL=1e-9; SLOPE_PASS=.30,
SLOPE_RELOC=.70; SUPPLY_GRADE=[.1,10]; runtime cap 25 min.

SMOKE DISCLOSURE (mandatory; pre-freeze history preserved).
 SMOKE-1 (SPEC v0, artifact suppressed, 101.6 s) reproduced the whole
 ladder exactly (42 surface, 28/28 deep, 68 = 40+1+27 steps; P2/P3
 .6790/.0520/.8875; deep floor 1.6610).  Nine of ten reached checks
 passed, then the passage stopped at truth step 20/68.  Two purely
 mechanical defects were exposed: the DIAGNOSTIC (not certificate)
 grid evaluated the artificial t=1e8 tail by raw products and
 overflowed to inf; and Python dictionary equality compared embedded
 arrays while collecting filter objects, raising the ambiguous-array
 ValueError.  The first 20 uncensored measurements were local m=3..5,
 global-family m=4..7.
 AMENDMENT A1 (numerical representation only): evaluate f_m by paired
 interlacing ratios and the far tail through f(1/u).  The interval
 certificate is algebraically unchanged; pairing removes dependency
 blow-up at high m and overflow in the diagnostic scalar evaluator.
 AMENDMENT A2 (bookkeeping only): validate local filters from the
 cache after construction instead of testing dictionary membership.
 No filter, node, pole, residue, bar, enum, success rule, control,
 screen band, ladder definition or certificate decision changed.
 SMOKE-2 (post-A1/A2, artifact suppressed, 108.0 s) ran 24/24 GREEN,
 no kills.  Full uncensored headline: per-rung m min/med/max 3/4/5;
 one GLOBAL family 4/5/8; a single FIXED m=8 filter certifies 68/68
 (census by m 1..8: 0/0/0/3/53/65/67/68).  Local-margin dex
 -1.867/-0.370/-0.170; fixed-margin dex -1.564/-0.036/-0.022 with
 h-slope +.009 +/- .037.  LU partial-fraction/eigensum tie 1.38e-14;
 interlacing worst +7.75e-7; source L sound 68/68.  Both margin
 tau-screens PASS; dn*/s median 28.023 OUT-OF-GRADE.  Controls fire
 4/4, zero indefinite leaks, min indefinite trace 2.0092, and the two
 genuinely-PD cosh cores are kz 23/13 (lambda_min +.530/+1.041).
 The phase ward covers 544 rung-pole pairs at 1.02e-11; no Euler
 artifact existed, so comparison was correctly deferred.  The frozen
 run below changes only this disclosure/SPEC SHA and enables the JSON
 write.

SPEC v1 (2026-08-12, frozen after the two disclosed smokes): everything
above.  No post-freeze numerical amendment is permitted without a new
disclosed SPEC version.

NO RH claim.  No marker move, no verification/paper/ledger/website/
manifest edit.  The only frozen-run write is the phase JSON beside this
probe; the German CCXXV line is prepended to experiments/next.txt only
after the frozen-run summary.

Run:
  TFPT_ZOLO_SMOKE=1 experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/zolotarev_phase_filter_probe.py
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/zolotarev_phase_filter_probe.py
"""

import ast
import glob
import hashlib
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla
from scipy import special

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import onebadmode_moments_probe as ob  # noqa: E402, READ-ONLY CCVII

NDIM = 8
CB_CITED = Fraction(5523, 10000)
CB_F = float(CB_CITED)
M_MAX = 20
N_LEFT = 1024
N_TARGET = 8192
N_TAIL = 4096
ROUND_PAD = 512.0 * np.finfo(float).eps
GRID_WARD = 2e-10
PF_TIE = 2e-8
LOGDET_WARD = 2e-6
ILACE_TOL = 1e-10
SOUND_TOL = 1e-9
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
SUPPLY_GRADE = (0.1, 10.0)
PHASE_ARTIFACT = os.path.join(_HERE,
                              "zolotarev_phase_filter_phases.json")
SMOKE = os.environ.get("TFPT_ZOLO_SMOKE", "0") == "1"
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


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
    bad = []
    for node in ast.walk(ast.parse(source)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


def trio(values):
    vals = np.asarray(values, float)
    return float(np.min(vals)), float(np.median(vals)), float(np.max(vals))


def f3(values, fmt="%.3f"):
    return "/".join(fmt % value for value in trio(values))


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    variance = float(np.var(x))
    if variance == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    slope = float(np.cov(x, y, bias=True)[0, 1] / variance)
    intercept = float(np.mean(y) - slope * np.mean(x))
    residual = float(np.sum((y - intercept - slope * x) ** 2))
    total = float(np.sum((y - np.mean(y)) ** 2))
    return intercept, slope, 1.0 - residual / total if total > 0 else float("nan")


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _intercept, slope, r2 = ols_line(x, y)
    leave_one_out = []
    for index in range(len(x)):
        keep = np.ones(len(x), bool)
        keep[index] = False
        leave_one_out.append(ols_line(x[keep], y[keep])[1])
    leave_one_out = np.asarray(leave_one_out)
    error = math.sqrt((len(x) - 1) / len(x)
                      * float(np.sum((leave_one_out
                                      - leave_one_out.mean()) ** 2)))
    return slope, error, r2


def screen(values, taus):
    values = np.asarray(values, float)
    taus = np.asarray(taus, float)
    positive = (values > 0.0) & (taus > 0.0) & np.isfinite(values)
    if int(np.sum(positive)) < 3:
        return "vacuous(pos=%d)" % int(np.sum(positive)), float("nan")
    _intercept, slope, r2 = ols_line(np.log(taus[positive]),
                                     np.log(values[positive]))
    label = ("PASS" if abs(slope) <= SLOPE_PASS
             else "RELOC" if slope >= SLOPE_RELOC else "AMBIG")
    return ("%s(slope=%+.3f,R2=%.3f,%d excluded)"
            % (label, slope, r2, int(np.sum(~positive)))), slope


# ---------------------------------------------------------------- filters
def elliptic_nodes(epsilon, m):
    """Classical proper Zolotarev nodes c_1,...,c_{2m-1}."""
    complement_parameter = 1.0 - epsilon * epsilon
    complete_k = float(special.ellipk(complement_parameter))
    nodes = []
    for index in range(1, 2 * m):
        sn, cn, _dn, _phase = special.ellipj(
            index * complete_k / (2.0 * m), complement_parameter)
        nodes.append(epsilon * epsilon * (sn / cn) ** 2)
    return np.asarray(nodes, float), complete_k


def product_interval(edges, numerator_nodes, denominator_nodes,
                     reciprocal=False):
    """Outward-padded enclosure of f on every positive interval.

    reciprocal=False encloses
      t prod(t^2+a)/prod(t^2+b).
    reciprocal=True encloses f(1/u) =
      u prod(1+a u^2)/prod(1+b u^2).
    Every factor used in the separate numerator/denominator products
    is monotone, so endpoint substitution is rigorous for positive
    float-committed coefficients; ROUND_PAD expands roundoff outward.
    """
    low = np.asarray(edges[:-1], float)
    high = np.asarray(edges[1:], float)
    low2, high2 = low * low, high * high
    # Pair the interlacing factors before interval multiplication.  This
    # is the same exact product, but avoids the dependency blow-up from
    # separately enclosing two large products at higher m.
    final_denominator = float(denominator_nodes[-1])
    if reciprocal:
        # f(1/u) = u/(1+b_last*u^2)
        base_low = low / (1.0 + final_denominator * low2)
        base_high = high / (1.0 + final_denominator * high2)
        critical = 1.0 / math.sqrt(final_denominator)
    else:
        # f(t) = t/(t^2+b_last)
        base_low = low / (low2 + final_denominator)
        base_high = high / (high2 + final_denominator)
        critical = math.sqrt(final_denominator)
    lower = np.minimum(base_low, base_high)
    upper = np.maximum(base_low, base_high)
    contains_critical = (low <= critical) & (critical <= high)
    if np.any(contains_critical):
        critical_value = (critical / (1.0 + final_denominator
                                       * critical * critical)
                          if reciprocal
                          else critical / (critical * critical
                                           + final_denominator))
        upper[contains_critical] = np.maximum(
            upper[contains_critical], critical_value)
    for numerator_node, denominator_node in zip(
            numerator_nodes, denominator_nodes[:-1]):
        if reciprocal:
            ratio_low = ((1.0 + numerator_node * low2)
                         / (1.0 + denominator_node * low2))
            ratio_high = ((1.0 + numerator_node * high2)
                          / (1.0 + denominator_node * high2))
        else:
            ratio_low = ((low2 + numerator_node)
                         / (low2 + denominator_node))
            ratio_high = ((high2 + numerator_node)
                          / (high2 + denominator_node))
        lower *= np.minimum(ratio_low, ratio_high)
        upper *= np.maximum(ratio_low, ratio_high)
    pad = ROUND_PAD * (2 + len(numerator_nodes) + len(denominator_nodes))
    lower = np.maximum(0.0, lower * (1.0 - pad))
    upper = upper * (1.0 + pad)
    lower = np.nextafter(lower, -np.inf)
    upper = np.nextafter(upper, np.inf)
    return lower, upper


def scalar_f(t, numerator_nodes, denominator_nodes):
    value = np.longdouble(t)
    square = value * value
    for numerator_node, denominator_node in zip(
            numerator_nodes, denominator_nodes[:-1]):
        value *= ((square + np.longdouble(numerator_node))
                  / (square + np.longdouble(denominator_node)))
    value /= square + np.longdouble(denominator_nodes[-1])
    return float(value)


def build_filter(c_value, l_value, m):
    """Build and certify the one-sided proper Zolotarev filter."""
    if not (0.0 < c_value < l_value and m >= 1):
        raise ValueError("filter requires 0 < c < L and m >= 1")
    epsilon = c_value / l_value
    nodes, complete_k = elliptic_nodes(epsilon, m)
    numerator_nodes = nodes[1::2]
    denominator_nodes = nodes[0::2]

    left_edges = np.linspace(0.0, epsilon, N_LEFT + 1)
    target_edges = np.geomspace(epsilon, 1.0, N_TARGET + 1)
    tail_edges = np.concatenate(([0.0], np.geomspace(1e-14, 1.0,
                                                      N_TAIL + 1)))
    left_lower, left_upper = product_interval(
        left_edges, numerator_nodes, denominator_nodes)
    target_lower, target_upper = product_interval(
        target_edges, numerator_nodes, denominator_nodes)
    _tail_lower, tail_upper = product_interval(
        tail_edges, numerator_nodes, denominator_nodes, reciprocal=True)
    global_upper = max(float(np.max(left_upper)),
                       float(np.max(target_upper)),
                       float(np.max(tail_upper)))
    bulk_lower = float(np.min(target_lower))
    bulk_upper = float(np.max(target_upper))
    normalization = 1.0 / global_upper
    delta = max(0.0, 1.0 - normalization * bulk_lower)
    global_r_lower = 1.0 - normalization * global_upper
    bulk_r_lower = 1.0 - normalization * bulk_upper

    # Residues in t, then transform t=x/L and negate for R=1-Df.
    residues = []
    poles = []
    for index, pole_square in enumerate(denominator_nodes):
        numerator = np.longdouble(1.0)
        for node in numerator_nodes:
            numerator *= np.longdouble(node - pole_square)
        denominator = np.longdouble(2.0)
        for other_index, other_square in enumerate(denominator_nodes):
            if other_index != index:
                denominator *= np.longdouble(other_square - pole_square)
        residue_t = np.longdouble(normalization) * numerator / denominator
        poles.append(1j * l_value * math.sqrt(pole_square))
        residues.append(-l_value * float(residue_t))
    return dict(c=float(c_value), L=float(l_value), m=int(m),
                eps=float(epsilon), Kp=complete_k,
                nodes=nodes, num=numerator_nodes, den=denominator_nodes,
                D=float(normalization), delta=float(delta),
                global_upper=global_upper, bulk_lower=bulk_lower,
                bulk_upper=bulk_upper,
                global_R_lower=float(global_r_lower),
                bulk_R_lower=float(bulk_r_lower),
                poles=np.asarray(poles, complex),
                residues=np.asarray(residues, float))


def scalar_r(filter_data, x_value):
    scaled = x_value / filter_data["L"]
    return 1.0 - filter_data["D"] * scalar_f(
        scaled, filter_data["num"], filter_data["den"])


def resolvent_data(matrix, pole, want_inverse=False):
    shifted = matrix.astype(complex) - pole * np.eye(NDIM, dtype=complex)
    lu_and_piv = sla.lu_factor(shifted)
    inverse = sla.lu_solve(lu_and_piv, np.eye(NDIM, dtype=complex))
    trace = complex(np.trace(inverse))
    return (trace, inverse) if want_inverse else trace


def trace_filter_lu(matrix, filter_data, want_gradient=False):
    terms = []
    gradient_terms = []
    for residue, pole in zip(filter_data["residues"],
                             filter_data["poles"]):
        trace, inverse = resolvent_data(matrix, pole, want_inverse=True)
        terms.append(2.0 * residue * trace.real)
        if want_gradient:
            inverse_square_00 = complex((inverse @ inverse)[0, 0])
            gradient_terms.append(-2.0 * residue
                                  * inverse_square_00.real)
    value = NDIM + math.fsum(terms)
    if want_gradient:
        return value, math.fsum(gradient_terms)
    return value


def trace_filter_eigs(eigenvalues, filter_data):
    return math.fsum(scalar_r(filter_data, float(value))
                     for value in eigenvalues)


def diagnostic_grid_defect(filter_data):
    c_value, l_value = filter_data["c"], filter_data["L"]
    positive = np.concatenate((
        np.geomspace(max(c_value * 1e-8, 1e-14), c_value, 401),
        np.geomspace(c_value, l_value, 1201),
        np.geomspace(l_value, l_value * 1e8, 401)))
    negative = -np.geomspace(max(c_value * 1e-8, 1e-14),
                             l_value * 1e8, 601)
    rp = np.asarray([scalar_r(filter_data, x) for x in positive])
    rn = np.asarray([scalar_r(filter_data, x) for x in negative])
    bulk = np.asarray([scalar_r(filter_data, x)
                       for x in np.geomspace(c_value, l_value, 1601)])
    return max(float(np.max(-rp)), float(np.max(1.0 - rn)),
               float(np.max(bulk - filter_data["delta"])))


# ------------------------------------------------------------- ladder
def assemble_step(step):
    tau = step["tau"]
    if tau <= 0.0:
        step["status"] = "REFUSED-TAU"
        return step
    matrix = sym(step["Q"].T @ (step["r2"]["S"] / tau) @ step["Q"])
    step["Mt"] = matrix
    pivot, coupling, block = ob.split_parts(matrix)
    step["n0"], step["bvec"], step["Bblk"] = pivot, coupling, block
    block_eigenvalues = np.linalg.eigvalsh(block)
    step["lamB1"] = float(block_eigenvalues[0])
    try:
        step["gap"] = pivot - float(coupling
                                    @ np.linalg.solve(block, coupling))
    except np.linalg.LinAlgError:
        step["gap"] = float("nan")
    step["eigs"] = np.linalg.eigvalsh(matrix)  # truth reference only
    gershgorin = ob.gersh_bound(matrix)
    frobenius = ob.fro_bound(matrix)
    step["L_src"] = min(gershgorin, frobenius) * ob.L_INFLATE
    step["L_win"] = "G" if gershgorin <= frobenius else "F"
    if step["L_src"] <= CB_F * (1.0 + 1e-6):
        step["status"] = "REFUSED-L"
        return step
    step["status"] = "OK"
    return step


def build_truth_ladder():
    section("W -- CCVII ladder reproduction (read-only machinery)")
    zones = ob.ladder_zones()
    check("W1 surface rung census %d == %d" % (len(zones),
                                                ob.N_RUNGS_EXP),
          len(zones) == ob.N_RUNGS_EXP, kill="K1")
    surface = [ob.build_rung("surf", kz, with_split=True)
               for kz in zones]
    check("W1b all surface chains complete",
          all(rung is not None for rung in surface), kill="K1")
    if KILLS:
        return zones, []
    surface_h = sorted(surface, key=lambda rung: (rung["h"], rung["kz"]))
    surface_steps = ob.make_steps(surface_h)
    for step in surface_steps:
        assemble_step(step)
    surface_ok = [step for step in surface_steps
                  if step["status"] == "OK"]
    min_b_surface = min(step["lamB1"] for step in surface_ok)
    gaps = np.asarray([step["gap"] for step in surface_ok])
    check("W2 P2/P3 reproduction minB %.4f, gap min/med %.4f/%.4f"
          % (min_b_surface, float(np.min(gaps)),
             float(np.median(gaps))),
          (abs(min_b_surface / ob.MINB_REF - 1.0) <= ob.MINB_RTOL
           and abs(float(np.min(gaps)) / ob.GAPMIN_REF - 1.0)
           <= ob.GAP_RTOL
           and abs(float(np.median(gaps)) / ob.GAPMED_REF - 1.0)
           <= ob.GAP_RTOL), kill="K2")

    extension = ob.build_ext_tables()
    overlap_deviation = float(np.max(np.abs(
        extension[:ob.core.ATOM_MAX + 1] - ob.core.LAM_TAB)))
    deep_zones = ob.deep_zone_census()
    check("W3 deep table overlap %.1e == 0; rung census %d == %d"
          % (overlap_deviation, len(deep_zones), ob.N_DEEP_EXP),
          overlap_deviation == 0.0 and len(deep_zones) == ob.N_DEEP_EXP,
          kill="K1")
    deep = []
    for kz, expected_h in sorted(deep_zones, key=lambda pair:
                                  (pair[1], pair[0])):
        if time.time() - T0 > ob.SOFT_BUDGET_S:
            break
        rung = ob.build_rung("deep", kz, with_split=True)
        if rung is not None:
            deep.append(rung)
        print("    deep kz %-4d h %-5d %s [%.0f s]"
              % (kz, expected_h, "OK" if rung is not None else "SHORT",
                 time.time() - T0), flush=True)
    deep_ok = [rung for rung in deep
               if rung["core_ok"] and rung["negA"] == 0
               and rung.get("lamS", -1.0) > 0.0]
    check("W4 deep truth rungs %d == %d" % (len(deep_ok),
                                             ob.N_DEEP_EXP),
          len(deep_ok) == ob.N_DEEP_EXP, kill="K1")
    if KILLS:
        return zones, []
    deep_h = sorted(deep_ok, key=lambda rung: (rung["h"], rung["kz"]))
    deep_steps = ob.make_steps(deep_h)
    for step in deep_steps:
        assemble_step(step)
    deep_step_ok = [step for step in deep_steps
                    if step["status"] == "OK"]
    min_b_deep = min(step["lamB1"] for step in deep_step_ok)
    check("W5 CLIV deep own-frame floor %.4f == %.4f"
          % (min_b_deep, ob.DEEP_MINB_REF),
          abs(min_b_deep / ob.DEEP_MINB_REF - 1.0)
          <= ob.DEEP_MINB_RTOL, kill="K2")

    combined_rungs = sorted(
        [rung for rung in surface_h if rung["core_ok"]] + deep_h,
        key=lambda rung: (rung["h"], rung["kz"]))
    combined_steps = ob.make_steps(combined_rungs)
    for step in combined_steps:
        assemble_step(step)
    ok_steps = [step for step in combined_steps if step["status"] == "OK"]
    segments = [ob.seg_of(step) for step in ok_steps]
    expected = (segments.count("surf") == 40
                and segments.count("bridge") == 1
                and segments.count("deep") == 27
                and len(ok_steps) == 68)
    check("W6 combined ladder 68 = surface %d + bridge %d + deep %d"
          % (segments.count("surf"), segments.count("bridge"),
             segments.count("deep")), expected, kill="K1")
    return zones, ok_steps


# ------------------------------------------------------- phase identity
def complex_logdet(matrix, pole, reference_phase=None):
    shifted = matrix.astype(complex) - pole * np.eye(NDIM, dtype=complex)
    sign, log_abs = np.linalg.slogdet(shifted)
    phase = float(np.angle(sign))
    if reference_phase is not None:
        phase = reference_phase + math.atan2(
            math.sin(phase - reference_phase),
            math.cos(phase - reference_phase))
    return complex(float(log_abs), phase)


def logdet_derivative_ward(matrix, pole, resolvent_trace):
    center = complex_logdet(matrix, pole)
    best = float("inf")
    best_derivative = complex(float("nan"), float("nan"))
    for relative_step in (1e-3, 3e-4, 1e-4, 3e-5):
        step = relative_step * max(1.0, abs(pole))
        values = [
            complex_logdet(matrix, pole - 2.0 * step, center.imag),
            complex_logdet(matrix, pole - step, center.imag),
            complex_logdet(matrix, pole + step, center.imag),
            complex_logdet(matrix, pole + 2.0 * step, center.imag),
        ]
        derivative = (values[0] - 8.0 * values[1]
                      + 8.0 * values[2] - values[3]) / (12.0 * step)
        relative = abs(resolvent_trace + derivative) / max(
            1.0, abs(resolvent_trace))
        if relative < best:
            best = float(relative)
            best_derivative = derivative
    return best, best_derivative


def determinant_phase_row(step, filter_data):
    pole_rows = []
    expression_terms = []
    worst_identity = 0.0
    for pole_index, (residue, pole) in enumerate(zip(
            filter_data["residues"], filter_data["poles"])):
        resolvent_trace = resolvent_data(step["Mt"], pole)
        expression_terms.append(2.0 * residue * resolvent_trace.real)
        shifted = step["Mt"].astype(complex) \
            - pole * np.eye(NDIM, dtype=complex)
        determinant = complex(np.linalg.det(shifted))
        logdet = complex_logdet(step["Mt"], pole)
        identity_deviation, derivative = logdet_derivative_ward(
            step["Mt"], pole, resolvent_trace)
        worst_identity = max(worst_identity, identity_deviation)
        pole_rows.append(dict(
            j=pole_index,
            z=[float(pole.real), float(pole.imag)],
            a=float(residue),
            resolvent_trace=[float(resolvent_trace.real),
                              float(resolvent_trace.imag)],
            determinant=[float(determinant.real), float(determinant.imag)],
            log_abs_det=float(logdet.real),
            phase=float(logdet.imag),
            phase_unwrapped=None,
            minus_dlogdet=[float((-derivative).real),
                           float((-derivative).imag)],
            identity_rel=float(identity_deviation)))
    expression = NDIM + math.fsum(expression_terms)
    return dict(
        segment=ob.seg_of(step),
        h1=int(step["r1"]["h"]), h=int(step["r2"]["h"]),
        kz1=int(step["r1"]["kz"]), kz=int(step["r2"]["kz"]),
        tau=float(step["tau"]), L_src=float(step["L_src"]),
        m_local=int(step["m_local"]), m_global=int(step["m_global"]),
        trace_R=float(expression), margin=float(1.0 - expression),
        poles=pole_rows), worst_identity


def unwrap_phase_rows(rows):
    if not rows:
        return
    pole_count = len(rows[0]["poles"])
    for pole_index in range(pole_count):
        principal = np.asarray(
            [row["poles"][pole_index]["phase"] for row in rows], float)
        unwrapped = np.unwrap(principal)
        for row, value in zip(rows, unwrapped):
            row["poles"][pole_index]["phase_unwrapped"] = float(value)


def extract_euler_rows(payload):
    if isinstance(payload, dict):
        for key in ("rungs", "rows", "phases"):
            if isinstance(payload.get(key), list):
                return payload[key]
    return payload if isinstance(payload, list) else []


def compare_euler_artifact(our_rows):
    candidates = []
    for pattern in ("euler_phase_identity_phases.json",
                    "euler_phase_identity_results.json",
                    "euler_phase_artifact.json"):
        candidates.extend(glob.glob(os.path.join(_HERE, pattern)))
    specification = {
        "match": ["h", "kz"],
        "our_quantity": ("phase_unwrapped[j] = unwrap_h arg det("
                         "M_h - z_j I), fixed global pole j"),
        "euler_quantity": ("completed Euler phase Theta_X evaluated "
                           "on the same ordered (h,kz) rungs"),
        "comparison": ("for each fixed pole j: Pearson correlation, "
                       "OLS affine residual and first-difference "
                       "correlation versus Theta_X(h); phases unwrapped "
                       "in increasing (h,kz), global additive phase free"),
    }
    if not candidates:
        return dict(status="DEFERRED-NO-EULER-ARTIFACT",
                    specification=specification)
    path = sorted(set(candidates))[0]
    try:
        payload = json.load(open(path, encoding="utf-8"))
        euler_rows = extract_euler_rows(payload)
        euler_map = {}
        for row in euler_rows:
            if not isinstance(row, dict) or "h" not in row:
                continue
            phase = None
            for key in ("Theta_X", "theta_x", "theta", "phase"):
                if isinstance(row.get(key), (int, float)):
                    phase = float(row[key])
                    break
            if phase is not None:
                euler_map[(int(row["h"]), int(row.get("kz", -1)))] = phase
        matched = []
        for row in our_rows:
            key_exact = (row["h"], row["kz"])
            key_h = (row["h"], -1)
            if key_exact in euler_map or key_h in euler_map:
                matched.append((row, euler_map.get(
                    key_exact, euler_map.get(key_h))))
        if len(matched) < 3:
            return dict(status="DEFERRED-SCHEMA-OR-MATCH",
                        artifact=os.path.basename(path),
                        matched=len(matched), specification=specification)
        theta = np.unwrap(np.asarray([pair[1] for pair in matched], float))
        correlations = []
        for pole_index in range(len(matched[0][0]["poles"])):
            phase = np.asarray([
                pair[0]["poles"][pole_index]["phase_unwrapped"]
                for pair in matched], float)
            corr = float(np.corrcoef(phase, theta)[0, 1])
            diff_corr = (float(np.corrcoef(np.diff(phase),
                                           np.diff(theta))[0, 1])
                         if len(phase) >= 4 else float("nan"))
            intercept, slope, r2 = ols_line(theta, phase)
            correlations.append(dict(j=pole_index, corr=corr,
                                     diff_corr=diff_corr,
                                     affine_slope=slope,
                                     affine_intercept=intercept,
                                     affine_r2=r2))
        return dict(status="COMPARED", artifact=os.path.basename(path),
                    matched=len(matched), correlations=correlations,
                    specification=specification)
    except (OSError, ValueError, TypeError) as error:
        return dict(status="DEFERRED-READ-ERROR", error=str(error),
                    artifact=os.path.basename(path),
                    specification=specification)


# ---------------------------------------------------------------- main
def main():
    section("PRIME.ONEBADMODE.ZOLOTAREV.PHASE.01 -- rational "
            "determinant-phase ONEBADMODE certificate (EXPLORATION ONLY)")
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
    parent_sha = hashlib.sha256(ob.__doc__.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % spec_sha)
    print("    CCVII imported-spec SHA-256 = %s" % parent_sha)
    print("    mode = %s; NO RH claim; finite float ladder only"
          % ("SMOKE (artifact suppressed)" if SMOKE else "FROZEN"))
    bad = ast_scan()
    check("S0 AST firewall clean", not bad,
          ",".join(sorted(set(bad))) if bad else "", kill="K2")
    zones, steps = build_truth_ladder()
    if KILLS or not steps:
        return finish({})

    section("A -- elliptic filters + certified separator facts")
    global_l = max(step["L_src"] for step in steps)
    global_filters = {m: build_filter(CB_F, global_l, m)
                      for m in range(1, M_MAX + 1)}
    local_cache = {}

    def local_filter(step, m):
        key = (float(step["L_src"]), int(m))
        if key not in local_cache:
            local_cache[key] = build_filter(CB_F, step["L_src"], m)
        return local_cache[key]

    interval_ok = all(
        filt["global_R_lower"] >= -1e-12
        and filt["bulk_R_lower"] >= -1e-10
        and 0.0 <= filt["delta"] <= 1.0
        and np.all(filt["nodes"] > 0.0)
        for filt in global_filters.values())
    sample_defect = max(diagnostic_grid_defect(filt)
                        for filt in global_filters.values())
    check("M1a global separator interval certificate: R>=1 on x<=0 "
          "by sign; R>=0 on R; bulk R<=delta for m=1..%d"
          % M_MAX, interval_ok, kill="K2")
    check("M1b diagnostic real-axis grid defect %.2e <= %.0e"
          % (sample_defect, GRID_WARD),
          sample_defect <= GRID_WARD, kill="K2")
    print("    EXTERNAL-CITED: Zolotarev/Akhiezer/van den Eshof "
          "elliptic minimax nodes; scipy K/sn/cn.")
    print("    DIRECTLY CERTIFIED: one-sided normalization on %d/%d/%d "
          "outward-padded boxes [0,eps]/[eps,1]/reciprocal tail."
          % (N_LEFT, N_TARGET, N_TAIL))
    print("    GLOBAL interval c=%.4f L=%.6g width L/c=%.3g"
          % (CB_F, global_l, global_l / CB_F))
    print("    m : " + " ".join("%2d" % m for m in range(1, M_MAX + 1)))
    print("    delta: " + " ".join("%.2e" % global_filters[m]["delta"]
                                  for m in range(1, M_MAX + 1)))

    section("B -- certificate census (LU partial fractions only)")
    worst_pf_tie = 0.0
    for index, step in enumerate(steps):
        step["local_traces"] = {}
        step["global_traces"] = {}
        step["m_local"] = None
        step["m_global"] = None
        for m in range(1, M_MAX + 1):
            local = local_filter(step, m)
            local_trace = trace_filter_lu(step["Mt"], local)
            global_trace = trace_filter_lu(step["Mt"], global_filters[m])
            step["local_traces"][m] = local_trace
            step["global_traces"][m] = global_trace
            if step["m_local"] is None and np.isfinite(local_trace) \
                    and local_trace < 1.0:
                step["m_local"] = m
            if step["m_global"] is None and np.isfinite(global_trace) \
                    and global_trace < 1.0:
                step["m_global"] = m
        if step["m_local"] is not None:
            chosen = local_filter(step, step["m_local"])
            truth_trace = trace_filter_eigs(step["eigs"], chosen)
            worst_pf_tie = max(worst_pf_tie, abs(
                step["local_traces"][step["m_local"]] - truth_trace)
                / max(1.0, abs(truth_trace)))
        print("    %2d/%d h %-5d %-6s m_local %-2s m_global %-2s [%.0f s]"
              % (index + 1, len(steps), step["r2"]["h"],
                 ob.seg_of(step), step["m_local"], step["m_global"],
                 time.time() - T0), flush=True)
    local_interval_ok = all(
        filt["global_R_lower"] >= -1e-12
        and filt["bulk_R_lower"] >= -1e-10
        and 0.0 <= filt["delta"] <= 1.0
        and np.all(filt["nodes"] > 0.0)
        for filt in local_cache.values())
    check("M1c all %d per-rung filters carry the same certified "
          "global/bulk separator bounds" % len(local_cache),
          local_interval_ok, kill="K2")

    fixed_m = None
    fixed_counts = {}
    for m in range(1, M_MAX + 1):
        fixed_counts[m] = sum(step["global_traces"][m] < 1.0
                              for step in steps)
        if fixed_m is None and fixed_counts[m] == len(steps):
            fixed_m = m
    check("B1 per-rung rational certificates on %d/%d"
          % (sum(step["m_local"] is not None for step in steps),
             len(steps)),
          all(step["m_local"] is not None for step in steps))
    check("B2 one GLOBAL fixed filter exists by m<=%d: %s"
          % (M_MAX, "m=%d" % fixed_m if fixed_m else "NO"),
          fixed_m is not None)
    if fixed_m is None:
        return finish(dict(head="ZOLOTAREV-BLOCKED(no fixed m<=%d)"
                           % M_MAX))
    fixed_filter = global_filters[fixed_m]
    for step in steps:
        step["trace_local"] = step["local_traces"][step["m_local"]]
        step["margin_local"] = 1.0 - step["trace_local"]
        step["trace_fixed"] = step["global_traces"][fixed_m]
        step["margin_fixed"] = 1.0 - step["trace_fixed"]
        truth_trace = trace_filter_eigs(step["eigs"], fixed_filter)
        worst_pf_tie = max(worst_pf_tie, abs(
            step["trace_fixed"] - truth_trace)
            / max(1.0, abs(truth_trace)))
    check("M2 partial-fraction LU trace == eigensum truth reference: "
          "worst rel %.2e <= %.0e" % (worst_pf_tie, PF_TIE),
          worst_pf_tie <= PF_TIE, kill="K2")

    local_m = np.asarray([step["m_local"] for step in steps], float)
    global_m = np.asarray([step["m_global"] for step in steps], float)
    local_margin_dex = np.log10(
        np.asarray([step["margin_local"] for step in steps]))
    fixed_margin_dex = np.log10(
        np.asarray([step["margin_fixed"] for step in steps]))
    print("    fixed-global census by m: "
          + " ".join("%d:%d" % (m, fixed_counts[m])
                     for m in range(1, fixed_m + 1)))
    print("    minimal m per-rung  min/med/max %s"
          % f3(local_m, "%.0f"))
    print("    minimal m under GLOBAL pole family min/med/max %s; "
          "FIXED m=%d certifies %d/%d"
          % (f3(global_m, "%.0f"), fixed_m, len(steps), len(steps)))
    print("    local margins dex min/med/max %s"
          % f3(local_margin_dex))
    print("    fixed margins dex min/med/max %s"
          % f3(fixed_margin_dex))
    slope_margin, error_margin, r2_margin = jack_slope(
        np.log([step["r2"]["h"] for step in steps]), fixed_margin_dex)
    print("    fixed-margin h-trend dlog10(margin)/dln(h) "
          "%+.3f +/- 2SE %.3f (R2 %.3f)"
          % (slope_margin, 2 * error_margin, r2_margin))

    # M3: premise and source-only bounds, never construction inputs.
    interlace_worst = min(
        (float(step["eigs"][1]) - step["lamB1"])
        / max(1.0, abs(step["lamB1"])) for step in steps)
    l_sound = sum(step["L_src"] >= float(step["eigs"][-1])
                  for step in steps)
    premise = {}
    for segment in ("surf", "bridge", "deep"):
        subset = [step for step in steps if ob.seg_of(step) == segment]
        premise[segment] = (
            sum(step["lamB1"] >= CB_F for step in subset), len(subset))
    check("M3 interlacing worst %+0.2e >= -%.0e; source-only "
          "L>=lam_max %d/%d" % (interlace_worst, ILACE_TOL,
                                l_sound, len(steps)),
          interlace_worst >= -ILACE_TOL and l_sound == len(steps),
          kill="K2")
    print("    PREMISE lam1(B)>=cB: surface %d/%d [CLIII cited], "
          "bridge %d/%d [float exception], deep %d/%d [float]"
          % (premise["surf"] + premise["bridge"] + premise["deep"]))

    section("D -- disguise diagnostics (tau screens + n-read supply)")
    local_screen, _ = screen(
        [step["margin_local"] for step in steps],
        [step["tau"] for step in steps])
    fixed_screen, _ = screen(
        [step["margin_fixed"] for step in steps],
        [step["tau"] for step in steps])
    n_ratios = []
    dn_values = []
    for step in steps:
        trace_value, gradient = trace_filter_lu(
            step["Mt"], fixed_filter, want_gradient=True)
        step["gradient_n"] = gradient
        step["dnstar"] = (step["margin_fixed"] / abs(gradient)
                          if gradient != 0.0 else float("inf"))
        if np.isfinite(step["dnstar"]) and step["gap"] > 0.0:
            step["dn_ratio"] = step["dnstar"] / step["gap"]
            n_ratios.append(step["dn_ratio"])
            dn_values.append(step["dnstar"])
        else:
            step["dn_ratio"] = None
        if abs(trace_value - step["trace_fixed"]) > PF_TIE:
            KILLS.append("K2")
    dn_screen, _ = screen(
        dn_values,
        [step["tau"] for step in steps
         if np.isfinite(step["dnstar"]) and step["gap"] > 0.0])
    median_ratio = float(np.median(n_ratios))
    supply_label = ("HALFGAP-GRADE"
                    if SUPPLY_GRADE[0] <= median_ratio <= SUPPLY_GRADE[1]
                    else "OUT-OF-GRADE")
    print("    margin local-m*: %s" % local_screen)
    print("    margin fixed-global m=%d: %s" % (fixed_m, fixed_screen))
    print("    dn*/s dex min/med/max %s; med %.3f -> %s"
          % (f3(np.log10(n_ratios)), median_ratio, supply_label))
    print("    dn* tau-screen: %s" % dn_screen)
    check("D1 typed rational disguise diagnostics complete", True)

    section("C -- controls (CCVII battery; controls must fire)")
    worlds = {}
    smooth = [ob.build_rung("surf", kz, world="smooth") for kz in zones]
    smooth_fire = sum(isinstance(rung, dict) and rung["negA"] > 0
                      for rung in smooth)
    check("E1 smooth fires on %d rungs" % smooth_fire,
          smooth_fire > 0, kill="K2")
    worlds["smooth"] = smooth
    scramble = [ob.build_rung("surf", kz, scramble_seed=ob.SCR_SEED)
                for kz in zones]
    scramble_fire = sum(rung is None or (
        isinstance(rung, dict) and rung["negA"] > 0)
        for rung in scramble)
    check("E2 scramble seed %d fires on %d rungs"
          % (ob.SCR_SEED, scramble_fire),
          scramble_fire > 0, kill="K2")
    worlds["scramble"] = scramble
    rung9 = ob.window_of(ob.CTRL_KZ)
    epstein_n = int(math.floor(math.exp(2.0 * rung9["alpha"]))) + 1
    epstein_lambda = ob.lambda_eps(epstein_n)
    epstein_indices = np.nonzero(np.abs(epstein_lambda) > 1e-12)[0]
    epstein = ob.build_rung(
        "surf", ob.CTRL_KZ,
        comb=(np.log(epstein_indices.astype(float)),
              2.0 * epstein_lambda[epstein_indices]
              / np.sqrt(epstein_indices.astype(float))))
    epstein_fire = epstein is None or epstein["negA"] > 0
    check("E3 Epstein x^2+5y^2 fires at kz %d; step ladder "
          "DECLARED SKIPPED O(X^2)" % ob.CTRL_KZ,
          epstein_fire, kill="K2")

    def cosh_injection(rung):
        times = np.arange(rung["M"]) * rung["D"]
        return (ob.INJ_A * np.cos(ob.INJ_GAMMA0 * times)
                * (np.cosh(ob.INJ_DELTA * times) - 1.0))

    cosh = [ob.build_rung("surf", kz, lag_fn=cosh_injection)
            for kz in zones]
    cosh_fire = sum(rung is None or (
        isinstance(rung, dict) and rung["negA"] > 0) for rung in cosh)
    check("E4 cosh A=%.3g fires on %d rungs" % (ob.INJ_A, cosh_fire),
          cosh_fire > 0, kill="K2")
    worlds["cosh"] = cosh

    control_rows = []
    indefinite_leaks = 0
    sound_min = float("inf")
    for world_name, ladder in worlds.items():
        control_rungs = sorted(
            [rung for rung in ladder if isinstance(rung, dict)],
            key=lambda rung: (rung["h"], rung["kz"]))
        control_steps = ob.make_steps(control_rungs, relax=True)
        n_indefinite = n_raw = n_composed = 0
        positive_cores = []
        for step in control_steps:
            assemble_step(step)
            if step["status"] != "OK":
                continue
            mstar = None
            trace_at_mstar = None
            for m in range(1, M_MAX + 1):
                control_filter = build_filter(CB_F, step["L_src"], m)
                trace_value = trace_filter_lu(step["Mt"], control_filter)
                if trace_value < 1.0:
                    mstar, trace_at_mstar = m, trace_value
                    break
            lambda_min = float(step["eigs"][0])
            lambda_scale = max(1.0, float(step["eigs"][-1]))
            indefinite = lambda_min <= -1e-10 * lambda_scale
            if indefinite:
                n_indefinite += 1
                # Evaluate the minimum finite rational trace as a ward.
                ward_values = []
                for m in range(1, M_MAX + 1):
                    control_filter = build_filter(
                        CB_F, step["L_src"], m)
                    ward_values.append(trace_filter_lu(
                        step["Mt"], control_filter))
                sound_min = min(sound_min, min(ward_values))
                if mstar is not None:
                    indefinite_leaks += 1
            if mstar is not None:
                n_raw += 1
                if step["lamB1"] >= CB_F:
                    n_composed += 1
            if not indefinite and lambda_min > 0.0:
                positive_cores.append(dict(
                    kz=int(step["r2"]["kz"]),
                    h=int(step["r2"]["h"]),
                    lambda_min=lambda_min,
                    certified=mstar is not None,
                    m=mstar,
                    trace=trace_at_mstar))
        control_rows.append(dict(
            world=world_name, steps=len(control_steps),
            indefinite=n_indefinite, raw_certificates=n_raw,
            composed_certificates=n_composed,
            positive_cores=positive_cores))
        print("    %-9s steps %2d indefinite %2d RAW %2d COMPOSED %2d "
              "PD cores %d" % (world_name, len(control_steps),
                               n_indefinite, n_raw, n_composed,
                               len(positive_cores)))
        for core in positive_cores:
            print("      PD core kz %(kz)d h %(h)d lam_min "
                  "%(lambda_min)+.3e cert=%(certified)s m=%(m)s"
                  % core)
    check("E5 soundness: zero rational certificates on indefinite "
          "controls (%d leaks); min trace %.6g >= 1-%.0e"
          % (indefinite_leaks, sound_min, SOUND_TOL),
          indefinite_leaks == 0 and sound_min >= 1.0 - SOUND_TOL,
          kill="K2")
    cosh_row = next(row for row in control_rows
                    if row["world"] == "cosh")
    check("E6 typed genuinely-PD cosh exceptions: %d cores"
          % len(cosh_row["positive_cores"]),
          len(cosh_row["positive_cores"]) == 2)

    section("E -- determinant phases and resolvent identity")
    phase_rows = []
    worst_identity = 0.0
    expression_tie = 0.0
    for step in steps:
        row, identity_deviation = determinant_phase_row(
            step, fixed_filter)
        phase_rows.append(row)
        worst_identity = max(worst_identity, identity_deviation)
        expression_tie = max(expression_tie,
                             abs(row["trace_R"] - step["trace_fixed"]))
    unwrap_phase_rows(phase_rows)
    check("M4a resolvent trace == -d logdet/dz: worst rel %.2e <= %.0e "
          "on %d rung-pole pairs"
          % (worst_identity, LOGDET_WARD,
             len(phase_rows) * fixed_m),
          worst_identity <= LOGDET_WARD, kill="K2")
    check("M4b phase partial-fraction expression == certificate trace: "
          "max abs %.2e <= %.0e" % (expression_tie, PF_TIE),
          expression_tie <= PF_TIE, kill="K2")
    comparison = compare_euler_artifact(phase_rows)
    if comparison["status"] == "COMPARED":
        best = max(comparison["correlations"],
                   key=lambda row: abs(row["corr"]))
        print("    EULER COMPARISON: matched %d; best pole j=%d "
              "corr=%+.3f diff-corr=%+.3f affine R2=%.3f"
              % (comparison["matched"], best["j"], best["corr"],
                 best["diff_corr"], best["affine_r2"]))
    else:
        print("    EULER COMPARISON: %s" % comparison["status"])
        print("      follow-up: match (h,kz); compare each fixed-pole "
              "unwrapped phase with Theta_X by correlation, affine "
              "residual and first differences.")

    artifact = dict(
        schema="tfpt.zolotarev_phase_filter.v1",
        mission="PRIME.ONEBADMODE.ZOLOTAREV.PHASE.01",
        spec_sha256=spec_sha,
        parent_onebadmode_spec_sha256=parent_sha,
        no_rh_claim=True,
        finite_float_ladder=True,
        filter=dict(scope="GLOBAL", c=CB_F, L=global_l, m=fixed_m,
                    delta=fixed_filter["delta"],
                    poles=[[float(z.real), float(z.imag)]
                           for z in fixed_filter["poles"]],
                    residues=[float(value)
                              for value in fixed_filter["residues"]]),
        comparison=comparison,
        rungs=phase_rows)
    if SMOKE:
        print("    SMOKE: phase artifact write suppressed")
    else:
        with open(PHASE_ARTIFACT, "w", encoding="utf-8") as handle:
            json.dump(artifact, handle, ensure_ascii=False,
                      separators=(",", ":"), sort_keys=True)
            handle.write("\n")
        print("    phase artifact written: %s (%d rungs, %d poles/rung)"
              % (os.path.basename(PHASE_ARTIFACT), len(phase_rows),
                 fixed_m))

    head = ("ZOLOTAREV-PHASE-CERTIFY(per-rung m %s; GLOBAL per-rung "
            "m %s; FIXED m=%d certifies 68/68)"
            % (f3(local_m, "%.0f"), f3(global_m, "%.0f"), fixed_m))
    labels = dict(
        head=head,
        margins="MARGINS(local dex %s; fixed dex %s; h-slope %+.3f+-%.3f)"
        % (f3(local_margin_dex), f3(fixed_margin_dex),
           slope_margin, 2 * error_margin),
        premise=("PREMISE(surface %d/%d; bridge %d/%d; deep %d/%d; "
                 "source-L %d/%d)"
                 % (premise["surf"] + premise["bridge"]
                    + premise["deep"] + (l_sound, len(steps)))),
        controls=("CONTROLS(indefinite leaks %d; cosh PD cores %d)"
                  % (indefinite_leaks,
                     len(cosh_row["positive_cores"]))),
        disguise=("DISGUISE(local %s; fixed %s; dn/s med %.3f %s)"
                  % (local_screen.split("(")[0],
                     fixed_screen.split("(")[0],
                     median_ratio, supply_label)),
        phase=("PHASE(poles %d; identity %.2e; Euler %s)"
               % (fixed_m, worst_identity, comparison["status"])))
    return finish(labels)


def finish(labels):
    section("V -- VERDICT")
    passed = sum(ok for _name, ok in CHECKS)
    if KILLS:
        verdict = ("PIPELINE-BROKEN" if KILLS[0] == "K1"
                   else "WARD-BROKEN")
    elif labels:
        verdict = " / ".join(labels[key] for key in
                             ("head", "margins", "premise", "controls",
                              "disguise", "phase") if key in labels)
    else:
        verdict = "INCOMPLETE"
    print("  VERDICT: %s" % verdict)
    print("  [EXTERNAL-CITED] Zolotarev elliptic rational sign "
          "construction; separator inequalities re-certified here.")
    print("  HONEST FRAME: finite float64 ladder only; c_B surface "
          "CITED, deep FLOAT-LEVEL, bridge exception typed; source-only "
          "L; eigenvalues truth-reference only; NO RH claim.")
    print("  [TIME] %.1f s  [CHECKS] %d/%d passed  [KILLS] %s"
          % (time.time() - T0, passed, len(CHECKS),
             ",".join(KILLS) if KILLS else "none"))
    return 0 if passed == len(CHECKS) and not KILLS else 1


if __name__ == "__main__":
    raise SystemExit(main())
