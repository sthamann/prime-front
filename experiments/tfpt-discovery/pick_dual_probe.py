#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pick_dual_probe -- PRIME.ONEBADMODE.PICK.DUAL.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

MISSION.  Test the high-pole-supported Stieltjes/Nevanlinna-Pick
extremal route for the frozen CCXXV low-pole Zolotarev filter without
using the wall margin, sigma, or moved filter poles.

CORRECTED INTERLACING CLASS.  The trace measure is split as

  nu = nu_good + delta_t,
  nu_good >= 0, supp(nu_good) subset [c_B,L], nu_good(R)=7,
  t in [-L,L].

The seven-unit good mass is the interlacing consequence of the
certified B-floor.  The one bad atom is deliberately allowed on the
whole signed interval; constraining t>0 would assume the conclusion.
For fixed source-only high points w_l=iY_l, impose

  |m_nu(w_l)-m_star(w_l)| <= eps_l,
  m_nu(z)=int dnu(x)/(x-z).

The objective is Phi(nu)=int R(x)dnu(x), where the filter itself is
the frozen CCXXV m=8 filter and is never moved.

SEPARATOR LOGIC.  CCXXV directly certifies R>=0 on R and R>=1 on
x<=0.  Therefore a certified supremum U<1 over the corrected class
forces t>0 for every measure meeting the high-pole disks: if t<=0,
its one-unit atom contributes R(t)>=1 and the good measure contributes
nonnegatively.  More sharply, R(t)<=Phi(nu)<=U because the good
contribution is nonnegative.  This is non-circular: [-L,0] remains in
the primal support and is excluded only by the high-read constraints
plus the extremal certificate.

DISK LADDER (frozen source geometry, no per-h tuning).  The
admissibility scale D=2.1e3 is the rounded CCLIII KS median scale and
the final point is the deployed top CCXXV pole:

  Y = (2100,4200,8400,16800,33600,49743.176671938345).

Two radii are tested around the prefix-MED J_star of CCLIX (the first
prefix is excluded in CCLIX's own radius gate, but here J_star is only
a fixed disk centre).

 MEASURED: 1.25 times the maximum deployed-ladder trace-Weyl
   deviation at each Y.  This is a finite-ladder measured premise.
 KS-DERIVED: 1.25 times the maximum of the exact first response
   |-tr(G_star D_h G_star)| plus the resolvent remainder
   ||D_h||_HS^2/Y^3.  The latter follows from the second resolvent
   identity and |tr(AB)|<=||A||_HS||B||_HS.  This is a conditional
   all-h premise whose missing input is the corresponding all-h KS
   radius/response bound; it is not inferred from the low reads.
Each disk's pedigree and truth membership are printed separately.

PRIMAL.  A source-grid semi-infinite measure relaxation is used only
as a diagnostic.  Certified feasible lower witnesses preserve the
required one bad atom: each truth spectrum is tested together with
its reflected bad atom, then the seven good locations/weights and the
single bad location are refined by constrained SLSQP.  Every retained
witness is rechecked against the exact complex disks.

DUAL.  For beta_l complex, define

  q_beta(x)=R(x)+2 Re sum_l beta_l/(x-w_l).

Find c_g,c_b with q_beta<=c_g on [c_B,L] and q_beta<=c_b on [-L,L].
For every primal-feasible measure,

  Phi <= 7c_g+c_b - 2 Re sum beta_l m_star(w_l)
                    + 2 sum |beta_l| eps_l =: U.

The disk-radius term is mandatory.  Candidate multipliers come from a
fine-grid conic polygon LP.  The pointwise bounds are then certified
independently: all float coefficients are committed as exact binary
rationals, positive denominators are cleared, and SymPy's exact Sturm
root count proves the resulting polynomial strictly positive on each
closed interval.  The |beta| terms are upper-rounded by exact integer
square-root arithmetic, so the final U accounting is rational.

GATES / WARDS.
 G1 corrected support census: bad eigenvalue in [-L,L], seven good
    eigenvalues in [c_B,L], on every truth step.
 G2 trace-Weyl convention is TRACE, not (1,1); LU trace equals direct
    eigensum at every high point and Phi linearity equals eigensum.
 G3 disk truth membership, separately for both pedigrees.
 G4 primal witnesses have mass 7+1, correct supports and exact disks.
 G5 dual polynomials pass exact Sturm positivity; exact accounting is
    no smaller than all diagnostic-grid evaluations.
 G6 controls must fire: every inherited indefinite world is censused
    for support and both disk classes; exclusions and any survivors
    are reported, never hidden.
 G7 anti-circularity: high points/radii are frozen before the extremal
    solve; disk construction contains no low-filter objective read;
    the extremal problem never sees h.
 G8 tau/c_h screens are applied to normalized disk slack; a global
    nonpositive closure reserve is typed VACUOUS rather than fitted.

TRIVIALIZATION SUB-RESULT.  If all eight units were incorrectly put
on [c_B,L], CCXXV already gives Phi<=8 delta.  The script reports this
number and 7 delta for the actual good block.  This is why the signed
one-atom component is the entire decision.

VERDICTS.
 PICK-CLOSES(tier,delta) iff the exact dual U<=1-delta with delta>0,
   truth membership is complete and wards pass.
 PICK-DEAD(tier,witness) iff an exact one-bad-atom feasible witness has
   Phi>=1 (the requested kill criterion).
 PICK-GAP(tier,lower,upper,anatomy) otherwise.

FROZEN BARS. NDIM=8; MASS_GOOD=7; MASS_BAD=1; c_B=5523/10000;
MEASURED_SAFETY=1.25; KS_INFLATION=1.25; HIGH_Y as above;
N_DUAL_GOOD=6000; N_DUAL_BAD=12000; N_NORM_ANGLES=128;
DUAL_GRID_PAD=2e-8; STURM_PAD_START=2e-8; WITNESS_STARTS=10;
DISK_TOL=2e-9; IDENT_TIE=2e-9; SLOPE_PASS=.30; SLOPE_RELOC=.70;
runtime cap 25 min.

SMOKE DISCLOSURE (mandatory, before freeze).
 SMOKE-1 (SPEC v0, 199.9 s) ran 13/14 checks with kill K2.  Both disk
 tiers had 11/11 read membership; the all-good bound was 0.146060525;
 both exact degree-28 Sturm certificates passed and the zero-multiplier
 dual read U=2.116961285104.  Two mechanical defects were exposed.
 (A1) The inherited subset ladder creates six subset-boundary
 pseudo-steps absent from the frozen 68-step artifact (the same
 phenomenon disclosed by CCLIX).  One pseudo-step violates the
 interlacing support, giving 10/11 rather than a meaningful smoke
 census.  Amendment: in SMOKE only, retain rows matched to the frozen
 artifact.  The full run remains the unfiltered 68-step ladder.
 (A2) The initial feasible-seed collector checked disks but omitted
 its own [c_B,L] support test before retaining a truth/reflection seed.
 It therefore printed an INVALID Phi=4.85778 witness whose seven
 listed "good" atoms included values below c_B.  Amendment: require
 mass, good support, bad support and disks at seed admission, matching
 the already-present post-SLSQP recheck.  The invalid number is
 suppressed and is not evidence.
 No high point, radius formula, safety/inflation factor, optimization
 bar, dual equation, exact-accounting rule, screen, control or verdict
 enum changed.

SPEC v1 (FROZEN after SMOKE-1, 2026-08-12).  Everything above,
including A1/A2.  No post-freeze numerical amendment is permitted
without a new disclosed SPEC version.

NO RH claim.  No verification/paper/ledger/website/manifest edits.
This probe writes nothing.  The German CCLXXV line is prepended to
experiments/next.txt only after the frozen-run summary.

Run:
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/pick_dual_probe.py --smoke
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/pick_dual_probe.py
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
from scipy import optimize
from scipy.sparse import csr_matrix
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import highpole_relative_ks_radius_probe as hp  # noqa: E402, read-only

NDIM = 8
MASS_GOOD = 7.0
MASS_BAD = 1.0
CB_Q = Fraction(5523, 10000)
CB = float(CB_Q)
HIGH_Y = np.asarray((2100.0, 4200.0, 8400.0, 16800.0, 33600.0,
                     49743.176671938345), float)
MEASURED_SAFETY = 1.25
KS_INFLATION = 1.25
N_DUAL_GOOD = 6000
N_DUAL_BAD = 12000
N_NORM_ANGLES = 128
DUAL_GRID_PAD = 2.0e-8
STURM_PAD_START = 2.0e-8
WITNESS_STARTS = 10
DISK_TOL = 2.0e-9
IDENT_TIE = 2.0e-9
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0 = time.time()
CHECKS = []
KILLS = []
BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
DISK_BUILDERS = ("build_disk_ladder",)
LOW_READ_IDS = ("scalar_r", "r_values", "trace_r_of", "phi",
                "margin", "reserve", "residues", "filter_poles")


def section(title):
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


def check(name, ok, kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s" % ("PASS" if ok else "FAIL", name), flush=True)
    return bool(ok)


def trio(values):
    arr = np.asarray(values, float)
    arr = arr[np.isfinite(arr)]
    if len(arr) == 0:
        return (float("nan"),) * 3
    return float(np.min(arr)), float(np.median(arr)), float(np.max(arr))


def e3(values):
    return "%.3e/%.3e/%.3e" % trio(values)


def ast_scan():
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    bad = []
    ac = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
        if isinstance(node, ast.FunctionDef) and node.name in DISK_BUILDERS:
            for sub in ast.walk(node):
                sub_name = None
                if isinstance(sub, ast.Name):
                    sub_name = sub.id
                elif isinstance(sub, ast.Attribute):
                    sub_name = sub.attr
                if sub_name in LOW_READ_IDS:
                    ac.append("%s:%s" % (node.name, sub_name))
    return bad, ac


def jacobi_matrix(a_values, b_values):
    matrix = np.diag(np.asarray(b_values, float))
    idx = np.arange(len(a_values))
    matrix[idx, idx + 1] = a_values
    matrix[idx + 1, idx] = a_values
    return matrix


def trace_read_from_eigs(eigenvalues, y_value):
    values = np.asarray(eigenvalues, float)
    return complex(np.sum(1.0 / (values - 1j * y_value)))


def trace_read_matrix(matrix, y_value):
    shifted = matrix.astype(complex) - 1j * y_value * np.eye(NDIM)
    return complex(np.trace(sla.solve(shifted, np.eye(NDIM),
                                      assume_a="gen")))


def filter_values(x_values, filter_poles, filter_residues):
    x = np.asarray(x_values, float)
    out = np.ones_like(x)
    for pole, residue in zip(filter_poles, filter_residues):
        y_value = float(abs(pole.imag))
        out += 2.0 * float(residue) * x / (x * x + y_value * y_value)
    return out


def screen(values, scales):
    values = np.asarray(values, float)
    scales = np.asarray(scales, float)
    mask = ((values > 0.0) & (scales > 0.0)
            & np.isfinite(values) & np.isfinite(scales))
    if int(np.sum(mask)) < 3:
        return "VACUOUS(pos=%d)" % int(np.sum(mask))
    x = np.log(scales[mask])
    y = np.log(values[mask])
    xm, ym = float(np.mean(x)), float(np.mean(y))
    slope = float(np.sum((x - xm) * (y - ym))
                  / np.sum((x - xm) ** 2))
    fit = ym + slope * (x - xm)
    den = float(np.sum((y - ym) ** 2))
    r2 = 1.0 - float(np.sum((y - fit) ** 2)) / den if den else 1.0
    label = ("PASS" if abs(slope) <= SLOPE_PASS
             else "RELOC" if slope >= SLOPE_RELOC else "AMBIG")
    return "%s(slope=%+.3f,R2=%.3f)" % (label, slope, r2)


def build_disk_ladder(rows, star_matrix):
    """High-read disks only: no low-filter objective enters here."""
    star_reads = np.asarray(
        [trace_read_matrix(star_matrix, y) for y in HIGH_Y], complex)
    measured = np.zeros(len(HIGH_Y))
    ks_derived = np.zeros(len(HIGH_Y))
    measured_raw = np.zeros((len(rows), len(HIGH_Y)))
    ks_raw = np.zeros((len(rows), len(HIGH_Y)))
    gstar = [np.linalg.inv(star_matrix.astype(complex)
                           - 1j * y * np.eye(NDIM)) for y in HIGH_Y]
    for i, row in enumerate(rows):
        matrix = jacobi_matrix(row["a"], row["b"])
        dmat = matrix - star_matrix
        d_hs = float(np.linalg.norm(dmat))
        for j, y_value in enumerate(HIGH_Y):
            read = trace_read_matrix(matrix, y_value)
            measured_raw[i, j] = abs(read - star_reads[j])
            first = -complex(np.trace(gstar[j] @ dmat @ gstar[j]))
            remainder = d_hs * d_hs / (y_value ** 3)
            ks_raw[i, j] = abs(first) + remainder
    measured[:] = MEASURED_SAFETY * np.max(measured_raw, axis=0)
    ks_derived[:] = KS_INFLATION * np.max(ks_raw, axis=0)
    return star_reads, {
        "MEASURED": dict(eps=measured, raw=measured_raw,
                         pedigree="MEASURED finite-ladder max x1.25"),
        "KS-DERIVED": dict(
            eps=ks_derived, raw=measured_raw, ks_bound=ks_raw,
            pedigree=("KS-DERIVED first response + D_HS^2/Y^3 "
                      "remainder x1.25")),
    }


def corrected_support_census(rows, big_l):
    details = []
    for row in rows:
        eigs = np.linalg.eigvalsh(jacobi_matrix(row["a"], row["b"]))
        ok = (eigs[0] >= -big_l and eigs[0] <= big_l
              and eigs[1] >= CB and eigs[-1] <= big_l)
        details.append((ok, eigs))
    return details


def make_good_grid(big_l, n_points):
    geom = np.geomspace(CB, big_l, n_points)
    low = np.linspace(CB, min(big_l, 100.0), max(400, n_points // 3))
    return np.unique(np.concatenate((geom, low, [CB, big_l])))


def make_bad_grid(big_l, n_points):
    half = max(1000, n_points // 2)
    pos = np.geomspace(1e-10, big_l, half)
    near = np.linspace(-10.0, 10.0, max(1000, n_points // 3))
    return np.unique(np.concatenate((-pos[::-1], [0.0], pos, near,
                                     [-big_l, big_l])))


def kernel_coefficients(x_values):
    x = np.asarray(x_values, float)
    real = np.empty((len(x), len(HIGH_Y)))
    imag = np.empty_like(real)
    for j, y_value in enumerate(HIGH_Y):
        den = x * x + y_value * y_value
        real[:, j] = x / den
        imag[:, j] = y_value / den
    return real, imag


def solve_dual(filter_poles, filter_residues, star_reads, eps, big_l):
    n_good = 1200 if SMOKE else N_DUAL_GOOD
    n_bad = 2400 if SMOKE else N_DUAL_BAD
    n_angles = 32 if SMOKE else N_NORM_ANGLES
    good_x = make_good_grid(big_l, n_good)
    bad_x = make_bad_grid(big_l, n_bad)
    rg = filter_values(good_x, filter_poles, filter_residues)
    rb = filter_values(bad_x, filter_poles, filter_residues)
    kg_r, kg_i = kernel_coefficients(good_x)
    kb_r, kb_i = kernel_coefficients(bad_x)
    n = len(HIGH_Y)
    nvar = 3 * n + 2
    rows = []
    rhs = []
    for values_r, values_i, r_value, which in (
            (kg_r, kg_i, rg, 0), (kb_r, kb_i, rb, 1)):
        block = np.zeros((len(r_value), nvar))
        block[:, :n] = 2.0 * values_r
        block[:, n:2 * n] = -2.0 * values_i
        block[:, 3 * n + which] = -1.0
        rows.append(block)
        rhs.append(-r_value)
    for theta in np.linspace(0.0, 2.0 * math.pi, n_angles,
                             endpoint=False):
        block = np.zeros((n, nvar))
        block[np.arange(n), np.arange(n)] = math.cos(theta)
        block[np.arange(n), n + np.arange(n)] = math.sin(theta)
        block[np.arange(n), 2 * n + np.arange(n)] = -1.0
        rows.append(block)
        rhs.append(np.zeros(n))
    aub = csr_matrix(np.vstack(rows))
    bub = np.concatenate(rhs)
    objective = np.zeros(nvar)
    objective[:n] = -2.0 * star_reads.real
    objective[n:2 * n] = 2.0 * star_reads.imag
    objective[2 * n:3 * n] = 2.0 * eps
    objective[3 * n] = MASS_GOOD
    objective[3 * n + 1] = MASS_BAD
    bounds = [(None, None)] * (2 * n) + [(0.0, None)] * n \
        + [(None, None), (None, None)]
    result = optimize.linprog(
        objective, A_ub=aub, b_ub=bub, bounds=bounds, method="highs",
        options=dict(dual_feasibility_tolerance=1e-9,
                     primal_feasibility_tolerance=1e-9))
    if not result.success:
        return dict(success=False, message=result.message)
    beta = result.x[:n] + 1j * result.x[n:2 * n]
    # Recompute true norms and support maxima; polygon norms only seed.
    qg = rg + 2.0 * (kg_r @ beta.real - kg_i @ beta.imag)
    qb = rb + 2.0 * (kb_r @ beta.real - kb_i @ beta.imag)
    cg = float(np.max(qg)) + DUAL_GRID_PAD
    cb = float(np.max(qb)) + DUAL_GRID_PAD
    diagnostic = (MASS_GOOD * cg + cb
                  - 2.0 * float(np.real(np.sum(beta * star_reads)))
                  + 2.0 * float(np.sum(np.abs(beta) * eps)))
    return dict(success=True, beta=beta, cg=cg, cb=cb,
                diagnostic=diagnostic, good_grid=good_x,
                bad_grid=bad_x, qg=qg, qb=qb,
                lp_objective=float(result.fun),
                polygon_norm=result.x[2 * n:3 * n])


def fq(value):
    return Fraction.from_float(float(value))


def exact_polynomial(beta, gamma, filter_poles, filter_residues):
    x = sp.Symbol("x")
    entries = []
    for pole, residue in zip(filter_poles, filter_residues):
        yq = fq(abs(pole.imag))
        entries.append(("filter", yq, fq(residue), Fraction(0)))
    for y_value, beta_value in zip(HIGH_Y, beta):
        entries.append(("dual", fq(y_value), fq(beta_value.real),
                        fq(beta_value.imag)))
    denoms = []
    for _kind, yq, _u, _v in entries:
        denoms.append(sp.Poly(x * x + sp.Rational(yq.numerator,
                                                  yq.denominator) ** 2,
                             x, domain=sp.QQ))
    denominator = sp.Poly(1, x, domain=sp.QQ)
    for den in denoms:
        denominator *= den
    gq = fq(gamma)
    polynomial = (sp.Rational(gq.numerator, gq.denominator) - 1) \
        * denominator
    for entry, den in zip(entries, denoms):
        kind, yq, u, v = entry
        quotient = denominator.exquo(den)
        if kind == "filter":
            numerator = 2 * sp.Rational(u.numerator, u.denominator) * x
        else:
            numerator = 2 * (
                sp.Rational(u.numerator, u.denominator) * x
                - sp.Rational(v.numerator, v.denominator)
                * sp.Rational(yq.numerator, yq.denominator))
        polynomial -= quotient.mul_ground(numerator) \
            if not isinstance(numerator, sp.Expr) \
            else sp.Poly(numerator, x, domain=sp.QQ) * quotient
    return sp.Poly(polynomial, x, domain=sp.QQ), denominator


def certify_interval(beta, gamma_seed, lo_value, hi_value,
                     filter_poles, filter_residues, label):
    pad = STURM_PAD_START
    attempts = 0
    while attempts < 8:
        gamma = float(gamma_seed + pad)
        polynomial, denominator = exact_polynomial(
            beta, gamma, filter_poles, filter_residues)
        loq = (sp.Rational(lo_value.numerator, lo_value.denominator)
               if isinstance(lo_value, Fraction) else
               sp.Rational(*float(lo_value).as_integer_ratio()))
        hiq = (sp.Rational(hi_value.numerator, hi_value.denominator)
               if isinstance(hi_value, Fraction) else
               sp.Rational(*float(hi_value).as_integer_ratio()))
        p_lo = polynomial.eval(loq)
        p_hi = polynomial.eval(hiq)
        roots = int(polynomial.count_roots(loq, hiq))
        if p_lo > 0 and p_hi > 0 and roots == 0:
            return dict(ok=True, gamma=gamma, roots=roots,
                        degree=polynomial.degree(),
                        den_degree=denominator.degree(), attempts=attempts,
                        label=label)
        pad *= 10.0
        attempts += 1
    return dict(ok=False, gamma=gamma, roots=roots,
                degree=polynomial.degree(),
                den_degree=denominator.degree(), attempts=attempts,
                label=label)


def sqrt_fraction_upper(value, digits=30):
    if value < 0:
        raise ValueError("negative square")
    scale = 10 ** digits
    numerator = value.numerator * scale * scale
    denominator = value.denominator
    root = math.isqrt(numerator // denominator)
    if root * root * denominator < numerator:
        root += 1
    return Fraction(root, scale)


def exact_dual_accounting(beta, cg, cb, star_reads, eps):
    total = MASS_GOOD * fq(cg) + MASS_BAD * fq(cb)
    total_q = fq(total)
    for beta_value, center, radius in zip(beta, star_reads, eps):
        u, v = fq(beta_value.real), fq(beta_value.imag)
        mr, mi = fq(center.real), fq(center.imag)
        total_q -= 2 * (u * mr - v * mi)
        norm_up = sqrt_fraction_upper(u * u + v * v)
        total_q += 2 * fq(radius) * norm_up
    return total_q


def measure_read(weights, good_x, bad_x):
    out = np.zeros(len(HIGH_Y), complex)
    for j, y_value in enumerate(HIGH_Y):
        out[j] = (np.sum(weights / (good_x - 1j * y_value))
                  + 1.0 / (bad_x - 1j * y_value))
    return out


def witness_value(weights, good_x, bad_x, filter_poles,
                  filter_residues):
    return (float(np.sum(weights * filter_values(
        good_x, filter_poles, filter_residues)))
            + float(filter_values([bad_x], filter_poles,
                                  filter_residues)[0]))


def refine_witnesses(rows, star_reads, eps, big_l, filter_poles,
                     filter_residues):
    seeds = []
    for row in rows:
        eigs = np.linalg.eigvalsh(jacobi_matrix(row["a"], row["b"]))
        good = eigs[1:].copy()
        for bad in (float(eigs[0]), -abs(float(eigs[0]))):
            weights = np.ones(7)
            reads = measure_read(weights, good, bad)
            feasible = bool(
                abs(float(np.sum(weights)) - 7.0) <= 1e-12
                and np.all((good >= CB) & (good <= big_l))
                and -big_l <= bad <= big_l
                and np.all(np.abs(reads - star_reads)
                           <= eps * (1.0 + DISK_TOL)))
            value = witness_value(weights, good, bad, filter_poles,
                                  filter_residues)
            if feasible:
                seeds.append((value, weights, good, bad, "truth/reflection"))
    seeds.sort(key=lambda item: item[0], reverse=True)
    best = seeds[0] if seeds else None
    for seed in seeds[:(3 if SMOKE else WITNESS_STARTS)]:
        _value, w0, x0, t0, _kind = seed
        z0 = np.concatenate((w0, x0, [t0]))

        def objective(z):
            return -witness_value(z[:7], z[7:14], z[14],
                                  filter_poles, filter_residues)

        def disk_constraints(z):
            reads = measure_read(z[:7], z[7:14], z[14])
            return eps * eps - np.abs(reads - star_reads) ** 2

        constraints = [
            dict(type="eq", fun=lambda z: float(np.sum(z[:7]) - 7.0)),
            dict(type="ineq", fun=disk_constraints),
        ]
        bounds = ([(0.0, 7.0)] * 7 + [(CB, big_l)] * 7
                  + [(-big_l, big_l)])
        result = optimize.minimize(
            objective, z0, method="SLSQP", bounds=bounds,
            constraints=constraints,
            options=dict(maxiter=1200, ftol=1e-12, disp=False))
        z = result.x
        reads = measure_read(z[:7], z[7:14], z[14])
        feasible = (abs(float(np.sum(z[:7])) - 7.0) <= 1e-7
                    and np.all(np.abs(reads - star_reads)
                               <= eps * (1.0 + DISK_TOL))
                    and np.all(z[:7] >= -1e-10)
                    and np.all((z[7:14] >= CB - 1e-9)
                               & (z[7:14] <= big_l + 1e-9))
                    and -big_l - 1e-9 <= z[14] <= big_l + 1e-9)
        value = -float(result.fun)
        if feasible and (best is None or value > best[0]):
            best = (value, z[:7].copy(), z[7:14].copy(),
                    float(z[14]), "SLSQP")
    return best, seeds


def controls_census(zones, rows, disk_packs, star_reads, big_l):
    truth = {row["kz"]: row for row in rows if row["seg"] == "surf"}
    worlds = hp.control_worlds(zones)
    summary = {}
    for name, ladder in worlds.items():
        indef = support_out = 0
        disk_out = {tier: 0 for tier in disk_packs}
        survivors = {tier: 0 for tier in disk_packs}
        for kz, control in ladder:
            row = truth.get(kz)
            if row is None or control is None or not control.get("core_ok"):
                continue
            with np.errstate(over="ignore", invalid="ignore"):
                matrix = hp.sym(row["step"]["Q"].T
                                @ (control["S"] / row["tau_scale"])
                                @ row["step"]["Q"])
            if not np.all(np.isfinite(matrix)):
                support_out += 1
                continue
            eigs = np.linalg.eigvalsh(matrix)
            is_indef = eigs[0] <= 0.0
            indef += int(is_indef)
            support_ok = (eigs[0] >= -big_l and eigs[-1] <= big_l
                          and eigs[1] >= CB)
            support_out += int(is_indef and not support_ok)
            reads = np.asarray([trace_read_from_eigs(eigs, y)
                                for y in HIGH_Y])
            for tier, pack in disk_packs.items():
                disk_ok = bool(np.all(np.abs(reads - star_reads)
                                      <= pack["eps"]
                                      * (1.0 + DISK_TOL)))
                disk_out[tier] += int(is_indef and not disk_ok)
                survivors[tier] += int(is_indef and support_ok and disk_ok)
        summary[name] = dict(indef=indef, support_out=support_out,
                             disk_out=disk_out, survivors=survivors)
    return summary


def main():
    section("PRIME.ONEBADMODE.PICK.DUAL.01 -- corrected interlacing "
            "Stieltjes/Pick extremal (EXPLORATION ONLY)")
    print("    mode %s; SPEC-SHA %s; TRACE-WEYL convention; NO RH claim"
          % ("SMOKE" if SMOKE else "FROZEN", SPEC_SHA[:8]))
    bad, ac = ast_scan()
    check("S0 AST firewall clean", not bad, kill="K2")
    check("S1 anti-circularity: disk builder contains no low-filter "
          "objective identifier", not ac, kill="K2")

    hp.SMOKE = SMOKE
    hp.CHECKS.clear()
    hp.KILLS.clear()
    artifact = json.load(open(hp.ARTIFACT, encoding="utf-8"))
    zones, steps = hp.build_ladder()
    filter_poles, filter_residues = hp.get_filter(steps, artifact)
    rows = hp.wall_rows(steps, artifact, filter_poles, filter_residues)
    if SMOKE:
        n_before = len(rows)
        rows = [row for row in rows if hp.step_key(row["step"]) in {
            (int(src["h1"]), int(src["kz1"]), int(src["h"]),
             int(src["kz"])) for src in artifact["rungs"]}]
        print("    SMOKE A1: retained %d/%d genuine artifact-matched "
              "steps; subset-boundary pseudo-steps excluded"
              % (len(rows), n_before))
    candidates = hp.build_candidates(rows, artifact, filter_poles,
                                     filter_residues)
    star = candidates["MED"]
    star_matrix = jacobi_matrix(star["a"], star["b"])
    big_l = float(artifact["filter"]["L"])

    section("A -- corrected support + trace-Weyl identity wards")
    support = corrected_support_census(rows, big_l)
    eig_min = min(float(item[1][0]) for item in support)
    good_min = min(float(item[1][1]) for item in support)
    eig_max = max(float(item[1][-1]) for item in support)
    n_support = sum(item[0] for item in support)
    check("G1 corrected interlacing support truth census %d/%d: "
          "bad min %.6g in [-L,L], lambda2 min %.6g >= c_B %.4f, "
          "max %.6g <= L %.6g"
          % (n_support, len(rows), eig_min, good_min, CB, eig_max,
             big_l), n_support == len(rows), kill="K2")
    worst_trace = 0.0
    worst_phi = 0.0
    for row, (_ok, eigs) in zip(rows, support):
        matrix = jacobi_matrix(row["a"], row["b"])
        for y_value in HIGH_Y:
            worst_trace = max(worst_trace, abs(
                trace_read_matrix(matrix, y_value)
                - trace_read_from_eigs(eigs, y_value)))
        phi_eig = float(np.sum(filter_values(
            eigs, filter_poles, filter_residues)))
        worst_phi = max(worst_phi, abs(phi_eig - row["phi"]))
    check("G2 TRACE-WEYL LU trace == eight-eigenvalue Stieltjes sum: "
          "worst %.2e <= %.0e" % (worst_trace, IDENT_TIE),
          worst_trace <= IDENT_TIE, kill="K2")
    check("G2b Phi linearity partial fractions == eigensum: worst "
          "%.2e <= %.0e" % (worst_phi, IDENT_TIE),
          worst_phi <= IDENT_TIE, kill="K2")

    star_reads, disk_packs = build_disk_ladder(rows, star_matrix)
    section("B -- THE DISK LADDER (TRACE-WEYL, two typed pedigrees)")
    print("    w_l = iY_l; Y = " + ", ".join("%.9g" % y for y in HIGH_Y))
    print("    centre = CCLIX prefix-MED J_star; spectrum %s"
          % e3(np.linalg.eigvalsh(star_matrix)))
    phi_dev = [abs(row["phi"] - star["phi"]) for row in rows]
    print("    CCLIX in-situ Phi deviation min/med/max %s "
          "(diagnostic only; disks use TRACE reads)" % e3(phi_dev))
    for tier, pack in disk_packs.items():
        eps = pack["eps"]
        deviations = pack["raw"]
        member = np.all(deviations <= eps[None, :]
                        * (1.0 + DISK_TOL), axis=1)
        pack["member"] = member
        print("\n    %s -- %s" % (tier, pack["pedigree"]))
        print("      j       Y_l         eps_l       measured max   "
              "membership")
        for j, y_value in enumerate(HIGH_Y):
            print("      %-2d %11.5g %12.5e %12.5e   %d/%d"
                  % (j, y_value, eps[j], np.max(deviations[:, j]),
                     int(np.sum(deviations[:, j] <= eps[j]
                                * (1.0 + DISK_TOL))), len(rows)))
        check("G3 %s truth disk membership %d/%d"
              % (tier, int(np.sum(member)), len(rows)),
              int(np.sum(member)) == len(rows), kill="K2")

    delta_filter = float(artifact["filter"]["delta"])
    trivial8 = 8.0 * delta_filter
    trivial7 = 7.0 * delta_filter
    print("\n    TRIVIALIZATION: all-good mass 8 => Phi <= 8 delta = "
          "%.9f; corrected good block => <= 7 delta = %.9f."
          % (trivial8, trivial7))
    print("    The signed one-unit bad atom is the entire decision.")

    results = {}
    for tier, pack in disk_packs.items():
        section("P/D -- %s PRIMAL + DUAL" % tier)
        witness, seeds = refine_witnesses(
            rows, star_reads, pack["eps"], big_l,
            filter_poles, filter_residues)
        check("G4 %s at least one exact one-bad-atom feasible witness"
              % tier, witness is not None, kill="K2")
        if witness is None:
            continue
        lower, weights, good_x, bad_x, witness_kind = witness
        reads = measure_read(weights, good_x, bad_x)
        disk_use = np.max(np.abs(reads - star_reads) / pack["eps"])
        print("    THE PRIMAL feasible lower = %.12f; reserve "
              "1-lower = %+.12f; witness %s; disk use %.9f"
              % (lower, 1.0 - lower, witness_kind, disk_use))
        print("    extremal anatomy: bad atom x = %+.12g, R(x)=%.9f; "
              "good contribution %.9f; active good atoms:"
              % (bad_x, filter_values([bad_x], filter_poles,
                                     filter_residues)[0],
                 lower - filter_values([bad_x], filter_poles,
                                       filter_residues)[0]))
        order = np.argsort(weights)[::-1]
        print("      " + ", ".join("(x=%.6g,m=%.6g)" %
                                   (good_x[i], weights[i])
                                   for i in order if weights[i] > 1e-7))

        dual = solve_dual(filter_poles, filter_residues, star_reads,
                          pack["eps"], big_l)
        check("D0 %s fine-grid conic-polygon dual solved: %s"
              % (tier, dual.get("message", "optimal")),
              dual["success"], kill="K2")
        if not dual["success"]:
            continue
        print("    dual diagnostic before Sturm: U_grid = %.12f; "
              "LP polygon objective %.12f"
              % (dual["diagnostic"], dual["lp_objective"]))
        cert_g = certify_interval(
            dual["beta"], dual["cg"], CB_Q, big_l,
            filter_poles, filter_residues, "good")
        cert_b = certify_interval(
            dual["beta"], dual["cb"], -big_l, big_l,
            filter_poles, filter_residues, "bad")
        check("G5 %s exact Sturm positivity: good=%s degree %d "
              "roots %d; bad=%s degree %d roots %d"
              % (tier, cert_g["ok"], cert_g["degree"],
                 cert_g["roots"], cert_b["ok"], cert_b["degree"],
                 cert_b["roots"]),
              cert_g["ok"] and cert_b["ok"], kill="K2")
        upper_q = exact_dual_accounting(
            dual["beta"], cert_g["gamma"], cert_b["gamma"],
            star_reads, pack["eps"])
        upper = float(upper_q)
        gap = upper - lower
        print("    DUAL CERTIFICATE: c_good = %.12f, c_bad = %.12f"
              % (cert_g["gamma"], cert_b["gamma"]))
        print("      U = 7*c_good + c_bad - 2 Re sum(beta*m_star)"
              " + 2 sum(|beta|*eps)")
        print("      exact-rational outward U = %.12f; closure reserve "
              "1-U = %+.12f; primal-dual gap %.3e"
              % (upper, 1.0 - upper, gap))
        print("      beta = " + ", ".join("%+.6e%+.6ei"
                                          % (z.real, z.imag)
                                          for z in dual["beta"]))
        results[tier] = dict(lower=lower, upper=upper, gap=gap,
                             witness=witness, dual=dual,
                             cert_g=cert_g, cert_b=cert_b)

    section("C/S -- controls and screens")
    control_summary = controls_census(
        zones, rows, disk_packs, star_reads, big_l)
    all_worlds_fire = True
    for name, summary in control_summary.items():
        print("    %-9s indefinite %2d; support-excluded %2d; "
              "MEASURED disk-excluded %2d survivors %2d; "
              "KS disk-excluded %2d survivors %2d"
              % (name, summary["indef"], summary["support_out"],
                 summary["disk_out"]["MEASURED"],
                 summary["survivors"]["MEASURED"],
                 summary["disk_out"]["KS-DERIVED"],
                 summary["survivors"]["KS-DERIVED"]))
        if summary["indef"] > 0:
            fire = (summary["support_out"]
                    + max(summary["disk_out"].values())) > 0
            all_worlds_fire = all_worlds_fire and fire
    check("G6 controls-must-fire: every world with indefinite cells "
          "has a support or disk exclusion", all_worlds_fire,
          kill="K4")

    ch_map = hp.ch_surface_map(rows)
    for tier, pack in disk_packs.items():
        normalized_slack = np.min(
            1.0 - pack["raw"] / pack["eps"][None, :], axis=1)
        tau_text = screen(normalized_slack,
                          [row["tau_scale"] for row in rows])
        matched = [(slack, ch_map[(int(row["h"]), row["kz"])])
                   for slack, row in zip(normalized_slack, rows)
                   if (int(row["h"]), row["kz"]) in ch_map]
        ch_text = (screen([v[0] for v in matched],
                          [v[1] for v in matched])
                   if matched else "VACUOUS(no match)")
        reserve_text = ("VACUOUS(nonpositive closure reserve)"
                        if tier not in results
                        or results[tier]["upper"] >= 1.0
                        else "PASS(delta=%.3e)"
                        % (1.0 - results[tier]["upper"]))
        print("    %-10s disk-slack vs tau %s; vs c_h %s; "
              "reserve screen %s"
              % (tier, tau_text, ch_text, reserve_text))

    section("V -- VERDICT")
    for tier in ("MEASURED", "KS-DERIVED"):
        if tier not in results:
            print("    %s: PICK-GAP(no certified dual result)" % tier)
            continue
        result = results[tier]
        lower, upper = result["lower"], result["upper"]
        bad_x = result["witness"][3]
        if lower >= 1.0:
            verdict = ("PICK-DEAD(%s; feasible one-bad-atom witness "
                       "Phi=%.9f at x_bad=%+.6g >= 1)"
                       % (tier, lower, bad_x))
        elif upper < 1.0:
            verdict = "PICK-CLOSES(%s, delta=%.9f)" \
                % (tier, 1.0 - upper)
        else:
            verdict = ("PICK-GAP(%s; lower %.9f, upper %.9f; "
                       "bad atom %+.6g)" % (tier, lower, upper, bad_x))
        print("    " + verdict)
        if upper < 1.0:
            print("      COMPOSED THEOREM: every J with one interlacing "
                  "bad mode, seven eigenvalues in [c_B,L], mass 8, "
                  "and TRACE-WEYL reads in these disks has tr R(J)<1; "
                  "since R>=1 on x<=0 and R>=0 globally, its bad "
                  "eigenvalue is strictly positive.")
        else:
            print("      No all-h closure: the high-point disk premise "
                  "does not force the bad atom positive at this tier.")

    n_pass = sum(ok for _name, ok in CHECKS)
    print("\n    [TIME] %.1f s  [CHECKS] %d/%d  [KILLS] %s"
          % (time.time() - T0, n_pass, len(CHECKS),
             ",".join(sorted(set(KILLS))) if KILLS else "none"))
    print("    Scope: experiments/tfpt-discovery probe only; no output "
          "artifact; NO RH claim.")
    return 0 if n_pass == len(CHECKS) and not KILLS else 1


if __name__ == "__main__":
    raise SystemExit(main())
