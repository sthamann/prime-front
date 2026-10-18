#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cofinal_package_probe -- PRIME.COFINAL.PACKAGE.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-13.)

THE REGIONAL POSITIVITY CERTIFICATE BECOMES A THEOREM PACKAGE.  The
CCXCIII run turned the Radau class statement into rational SOS
certificates (census 151/151 at eta = 273/1000, largest passing
eta* = 273091/1000000, proof object radau_sos_certificate_proof.json)
-- but the shipped object persists only the 5 global certificates
plus one worst-cell exhibit, its per-cell tier lives in the run log,
the joint relation is verified on DATA rather than symbolically, and
nobody has said exactly WHAT REGION the certificates cover.  THIS
PROBE hardens the result into THREE SEPARATE, SEPARATELY AUDITABLE
PARTS plus a TINY INDEPENDENT CHECKER:

 (a) PART 1 -- THE RELATION CERTIFICATE (symbolic, NO numeric
     input).  The joint relation is promoted from data-level to a
     chain of sympy-verified symbolic statements, frozen verbatim as
     module constants R1_TEXT..R4_TEXT (their joint sha is printed
     and stored in the package):
       R1 elimination soundness -- z^T (V D V^T) z =
          sum_k d_k ((V^T z)_k)^2 for unit-lower-triangular V at
          EVERY deployed dimension, the triangular-structure identity
          (V^T z)_i = z_i + sum_{j>i} V_ji z_j (so the last nonzero
          index of z survives), and the rank-form expansion
          z^T (sum_r c_r u_r u_r^T) z = sum_r c_r (u_r . z)^2 --
          positive pivots mean positive definite, rank-positive means
          positive semidefinite, and the checker only ever checks
          pivots and reconstructions;
       R2 the Schur pivot (CCLXV sigma = 1 - s/n) -- with b
          eliminated via b = B y at the deployed dimension 8:
          C M C^T = diag(n - y^T B y, B) for unit-triangular
          C = [[1, -y^T], [0, I_7]], the explicit inverse identity
          C Cinv = I_8, the reassembly M = Cinv diag(.) Cinv^T, the
          quotient identity s/n = 1 - sigma, the reserve arithmetic
          n - q = eta n + r > 0, and the floor-shift identity
          z^T B z = z^T (B - c I) z + c z^T z;
       R3 the majorant (interval-SOS soundness) -- the Gram
          evaluation identity u(x)^T G u(x) = sum_ij G_ij x^{i+j} at
          every deployed Gram dimension plus the assumption-verified
          sign chain: the certificate identity x p(x) - 1 =
          s_0 + (x-beta)(L-x) s_1 with PSD Grams gives p(x) >= 1/x
          on [beta, L] for beta > 0;
       R4 moment domination -- on the diagonal form (7 atoms, the
          spectral theorem E2 being the SINGLE external-cited
          reduction): nu_k = sum_i g_i^2 d_i^k (k = 0..9),
          q = sum_i g_i^2 / d_i, and the rearrangement
          sum_j c_j nu_j - q = sum_i g_i^2 (p(d_i) - 1/d_i), so
          p >= 1/x on the certified support gives
          q <= sum_j c_j nu_j.
     Every identity is verified by sympy expand on free symbols
     (28 symmetric-B entries, y, n, g, d, generic coefficients); a
     dedicated AST ward (S0.2) proves the relation functions contain
     NO float literal.  Sign steps are sympy assumption queries on
     positive/nonnegative symbols, frozen in the statement texts.
 (b) PART 2 -- THE POSITIVITY CERTIFICATE (per-cell schema).  The
     CCLXXIX universe (151 built wall-legal cells) and the CCXCIII
     certificate machinery are imported READ-ONLY and re-run
     deterministically to RE-MATERIALIZE the per-cell tier that
     CCXCIII verified but never persisted (amendment A1 -- reuse of
     the frozen machinery, not a new derivation; the run is warded
     digit-identical against the stored proof object: same source
     SPEC-SHA, eta* EXACTLY equal, worst bound EXACTLY equal, census
     151/151).  The 5 GLOBAL certificates are NOT recomputed: they
     are loaded verbatim from radau_sos_certificate_proof.json,
     re-verified exactly (identity + PSD + sympy) and their hashes
     required EQUAL to the stored ones.  The package stores per cell:
     the cell coordinates (seg, kz, h), the full wall matrix M as
     exact dyadic rationals, the region (certified floor c_i and
     ceiling L_i), the exact moments nu_0..nu_9, the pivot n, the
     CONSUMED certificate (kind, degree, interval, exact rational
     p-coefficients, both Gram matrices, rank certificates where
     PSD-by-structure, lift, verification hash), the exact bound
     sum_j c_j nu_j / n and the rational moment-box radius rho_i
     (see (c)).  One sound witness per cell -- a minimum of sound
     bounds is sound, so persisting the consumed minimum loses
     nothing.  The F5X deep-extension cells are stored SEPARATELY
     typed and never gate the 151 census.
 (c) PART 3 -- THE COVERAGE CERTIFICATE (the honest new piece).
     What region do the certificates actually cover?  EXACTLY THIS:
     R_cert = union over the census cells of
       E_i = {M = [[n, b^T],[b, B]] symmetric 8x8 : n > 0,
              B - c_i I reconstructs with positive pivots,
              L_i I - B reconstructs with positive pivots,
              sum_j c_j^(i) nu_j(b, B) <= (1 - eta) n},
     a FULL-dimensional explicitly described region -- every point
     of E_i is certified M > 0 (positive definite) with Schur
     reserve >= eta n by certificate i alone, so R_cert is fully
     covered BY CONSTRUCTION (overlaps harmless: each E_i is
     individually sound).  The probe computes and the package
     stores: (i) the exact 1-D union of the cell spectral intervals
     [c_i, L_i] with its gap list inside the covering interval;
     (ii) the per-cell rational RELATIVE MOMENT-BOX radius rho_i
     (|delta nu_j| <= rho_i nu_j keeps the census inequality, from
     the linear margin -- the honest 'local boxes around the 151
     members'); (iii) the cross-coverage census (which cells fall
     inside which other cells' certificates -- exact interval
     inclusion plus exact linear bound); (iv) the reused global-tier
     coverage (honestly weak, measured).  THE HONEST VERDICT IS
     TYPED: the declared ambient region K -- the frozen C_KS class
     box (CCLXI box-SHA 224a2737, CCLXXXV frame 6dfe799c) under the
     joint Radau relation -- is NOT fully certificate-covered;
     covered are R_cert, the rho-boxes and the sampled members; the
     class-box level remains CCLXXXV's conditional theorem chain
     plus a NUMERIC extremal (sup tr R = 0.972698), NOT a
     certificate.  Coverage enum: FULL-COVERAGE(R_cert, by
     construction) AND PARTIAL(K, gaps named verbatim) -- no
     overclaim: the honest answer is 'the class box modulo the
     relation, plus the 151 sampled cells with explicit rational
     neighborhoods', and that is exactly what the package says.
 (d) THE CHECKER.  experiments/tfpt-discovery/tiny_checker.py --
     stdlib-only (json, sys, hashlib, fractions, itertools; NO
     numpy, NO sympy), about 200 lines, fail-fast -- reads the
     package and verifies ONLY rational polynomial identities (exact
     expansion), elimination/rank reconstructions with pivot SIGN
     conditions, order comparisons, and sha256 integrity: per cell
     it re-derives the moments from M, re-runs the floor/ceiling
     eliminations, re-expands the SOS identity, re-computes the
     linear bound and the census inequality, re-checks rho_i, and
     re-merges the coverage intervals.  Its axiom surface is python
     integer/Fraction arithmetic plus the package file -- it never
     sees an eigensolver, a float, or this probe.  The probe gates:
     import surface (S0.3), line count (S0.4), full-package census
     100% (X7), and three DOCTORED packages that MUST fail (X8
     flipped p-coefficient with re-forged hash -> SOS identity
     residual; X9 pivot n scaled down with consistently forged
     bound -> census sign gate; X10 tampered statement text ->
     hash integrity).
 (e) GATES.  Inherited wards routed into this run (CCLXXXV
     registry pattern): the CCLXXIX universe identity/pivot/repro
     wards, CCXCIII E1-E4 (exact floors/ceilings/Radau anchors),
     P1-P5 (per-cell tier), T1-T4 (eta census), X1-X6
     (controls-must-fire, re-run against the RELOADED global
     certificates).  New wards: G3 stored global certificates
     re-verified with EQUAL hashes 5/5; G4 source SPEC-SHA equality;
     G5/G6 (frozen only) census/eta*/worst-bound EXACT equality with
     the stored proof object; R0-R4 relation certificates; C1-C3
     coverage (own-cell coverage 100% required); W1 package written
     + sha frozen; X7-X10 checker census + doctored controls.
     tau / c_h relocation screens are NOT re-run: this probe
     introduces NO new measured margin -- every bound is CCXCIII's,
     repackaged; the screens of record are CCXCIII's (PASS,
     |slope| <= 0.071), cited not re-measured.

EXTERNAL-CITED (consumed, never proved here).
 E2 spectral theorem / Schur-Sylvester (Horn & Johnson, Matrix
    Analysis 2nd ed., CUP 2013, Sec. 4.1, 4.3, 7.2): real symmetric
    B = V diag(d) V^T with V orthogonal -- consumed ONLY as the
    reduction of R4 to the diagonal form and the eigenvalue reading
    of the floor/ceiling certificates; the congruence, elimination
    and sign logic is machine-verified in R1-R3.
 E8 Markov-Lukacs completeness (Powers & Reznick, JPAA 164 (2001)
    221-229): certificates of the used form EXIST; soundness as
    consumed here is the elementary R3 chain.

FROZEN PROTOCOL.
 S0 firewall: AST scan of THIS file (banned zetazero / zetazeros /
    nzeros / primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; no RNG seat;
    S0.2 the relation functions rel_r1..rel_r4 contain NO float
    literal (AST-scanned); S0.3 tiny_checker.py imports ONLY
    {json, sys, hashlib, fractions, itertools} (AST-scanned);
    S0.4 tiny_checker.py line count <= CHK_MAX_LINES.
 U  the CCLXXIX universe rebuilt via the K5 probe's builders
    imported READ-ONLY (CCXCIII U verbatim): 42 surface rungs -> 68
    ladder steps (artifact-key warded), 17 F0 cells, F1/F2/F4/F5
    sweeps -> 151 built wall-legal cells; F5X deep-extension slice
    (frozen only, separate, never gating).
 E/P/T CCXCIII's exact_cell_data, percell_tier and eta_census run
    UNCHANGED (imported read-only; their checks route into this
    registry).
 G  the stored proof object: parse, re-verify all 5 global
    certificates exactly, require hash equality; require stored
    spec_sha == the CCXCIII module's current SPEC-SHA; frozen only:
    census_cells == 151, eta_star == this run's eta*, worst_bound ==
    this run's worst bound, both EXACT Fraction equality.
 R  the relation certificates R1-R4 verified symbolically; the
    statement texts frozen verbatim; joint statement sha printed.
 C  coverage: exact interval union + gaps; per-cell rho_i > 0 on
    every census cell; own-cell cross-coverage 151/151; global-tier
    coverage counted honestly.
 W  the package cofinal_package.json written (frozen run; the smoke
    writes and then removes cofinal_package_smoke.json), sha256
    printed; package cells == census cells, extension separate.
 X  controls: CCXCIII X1-X6 re-run against the reloaded global
    certificates; checker X7 (census 100%, exit 0); doctored
    packages X8/X9/X10 MUST fail with the named gate.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 repro/anchor -> REPRO-BROKEN; K4 a required control
silent -> CONTROL-SILENT.

VERDICT (frozen enum, in dominance order):
 PACKAGE-SEALED(relation 4/4 symbolic; positivity census N/N at
   eta = 273/1000 (+extension, separate); coverage typed
   FULL-COVERAGE(R_cert) AND PARTIAL(K, gaps named); checker census
   100% with 3/3 doctored controls fired)
 PACKAGE-PARTIAL(the failing part named precisely)
Every enum is a finite statement about the deployed ladder artifact
and the built wall-legal cells; NEVER an all-h statement, NEVER an
RH claim.

FROZEN BARS.  ETA = 273/1000 (CCXCIII ETA_TARGET verbatim);
CELL_EXP = 151; ETA_STAR_REF = 273091/1000000 (exact, frozen only);
GLOB_DEGS = (4,5,6,7,8); CHK_MAX_LINES = 210 (measured count
printed); CHK_ALLOWED = {json, sys, hashlib, fractions, itertools};
R4_ATOMS = 7; R4_KMAX = 9; DOCTOR_SCALE = 10^9 (the X9 pivot
doctor); checker timeouts 900 s (real) / 600 s (doctored); runtime
cap 25 min.  Smoke: the CCXCIII smoke subsets verbatim (via the K5
probe's SMOKE flag: 10 contiguous surface rungs + 3 lowest deep,
F0 cap 2, F1 cap 3, F2 (6,)x1, F4 1, F5/F5X skipped); count /
anchor / census gates decide only on the frozen build and print
their subset values.

HONEST AMENDMENTS (declared before the frozen run).
 A1 CCXCIII never persisted its per-cell certificates -- the package
    run re-materializes them with the IDENTICAL frozen machinery
    (radau_sos_certificate_probe imported READ-ONLY, its functions
    called unchanged) and wards the result digit-identical against
    the stored proof object (G4-G6).  Reuse, not recomputation of
    anything already persisted: the 5 stored global certificates are
    loaded verbatim and re-verified, never rebuilt.
 A2 the package stores ONE consumed certificate per cell (the
    minimum over verified bounds), not all 1106 in-run certificates:
    a minimum of sound bounds is sound, and one witness per cell is
    the theorem's need.  The in-run counts are printed.
 A3 the coverage part introduces NO new positivity claim: E_i
    membership of arbitrary M is decided by exactly the checks the
    checker performs; the probe only DESCRIBES the covered region
    and measures the cross-coverage/gap structure of the deployed
    151 samples.
 A4 sigma-side screens are not re-run (no new measured margin; see
    (e)); the CCXCIII screens of record are cited.

SMOKE DISCLOSURE (2026-08-13; TWO smoke invocations of the ONE
declared smoke configuration (the CCXCIII/K5 subsets verbatim, 17
cells) were run during construction; every defect is listed with
the repair; NO census rule, bar or verdict enum was weakened).
 SMOKE-1 (SPEC 2ab72c6f, 22.2 s) CRASHED at the coverage stage --
   a pipeline defect, not a gate: the moment-box radius rho was
   computed inside the package serializer but consumed earlier by
   the coverage part (KeyError).  REPAIR: rho is computed once for
   all census+extension rows at the head of the coverage part; no
   formula, bar or gate changed.  Every check that ran before the
   crash was green (S0, U, E1-E4, G1/G2, P1-P5, T1-T3, G3-G6,
   R0-R4, C1, C2).
 SMOKE-2 (SPEC 2ab72c6f, 25.7 s) FULLY GREEN: 61/61 checks, no
   kills; relation 4/4 symbolic (R1/R3 at dims 5..10, R2 at dim 8,
   R4 at degree 8); subset census 17/17 at eta = 0.273; stored
   global certificates 5/5 re-verified hash-EQUAL; smoke package
   written (1.2 MB, 17 cells), checker census 100% on it (1.0 s,
   exit 0), all THREE doctored packages failed at exactly the named
   gates (SOS identity residual / census bound > 1 - eta /
   statement hash R1); smoke package and doctor temp files removed.
 THE ONLY changes after SMOKE-2 are one cosmetic verdict-format
 line (the covering interval prints as floats in the verdict TEXT;
 the exact rational endpoints stay in the package fields) and this
 disclosure text.
 SMOKE-3 (SPEC 07de0ee5, 25.8 s, the final spec line) FULLY GREEN:
   61/61, no kills, checker census 100%, 3/3 doctors fired -- the
   SPEC SHA then moves ONLY by this sentence, as disclosed.

NO RH claim.  No marker moves; no paper, ledger, website, manifest
or verification file is touched; the only artifacts outside this
file are cofinal_package.json (frozen run only,
experiments/tfpt-discovery/), tiny_checker.py (written by the
mission, gated here), and the German CCCIX line prepended to
experiments/next.txt AFTER the frozen summary.

Sources (read-only): radau_sos_certificate_probe (CCXCIII machinery
+ proof object, imported READ-ONLY), bfloor_k5_closure_probe
(CCLXXIX universe builders, via CCXCIII), zolotarev_ks_dual_probe /
radau_class_close_probe (CCLXI / CCLXXXV class box, cited),
sigma_coupling_pivot_probe (CCLXV sigma identity, cited),
v563_paper2_readouts (deployed generators, READ-ONLY).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cofinal_package_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cofinal_package_probe.py
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

import radau_sos_certificate_probe as rs      # noqa: E402 (READ-ONLY)
import bfloor_k5_closure_probe as k5          # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
ETA = rs.ETA_TARGET                     # 273/1000 verbatim
CELL_EXP = rs.CELL_EXP                  # 151
ETA_STAR_REF = Fraction(273091, 10 ** 6)
GLOB_DEGS = rs.DEGREES
CHK_MAX_LINES = 210
CHK_ALLOWED = {"json", "sys", "hashlib", "fractions", "itertools"}
R4_ATOMS = 7
R4_KMAX = 9
DOCTOR_SCALE = 10 ** 9
CHK_TIMEOUT_REAL = 900
CHK_TIMEOUT_DOC = 600
PKG_JSON = os.path.join(_HERE, "cofinal_package.json")
PKG_SMOKE = os.path.join(_HERE, "cofinal_package_smoke.json")
CHK_PATH = os.path.join(_HERE, "tiny_checker.py")
PROOF_JSON = rs.PROOF_JSON

SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0 = time.time()

# route the check registries (CCLXXXV pattern): ONE registry for the
# K5 builders, the CCXCIII machinery and this probe
k5.CHECKS = []
k5.KILLS = []
k5.SMOKE = SMOKE
k5.T0 = T0
rs.CHECKS = k5.CHECKS
rs.KILLS = k5.KILLS
rs.SMOKE = SMOKE
rs.T0 = T0
CHECKS = k5.CHECKS
KILLS = k5.KILLS
check = k5.check
section = k5.section

FR0 = Fraction(0)
FR1 = Fraction(1)

# ================================ the frozen relation statements
R1_TEXT = """R1 (ELIMINATION SOUNDNESS -- what positive pivots mean).
Let G be a symmetric m x m rational matrix and suppose the checker's
elimination reconstructs G = sum_{k=1..m} d_k v_k v_k^T exactly (v_k
the k-th column of a unit lower triangular V), with every pivot
d_k > 0 -- a pure rational identity plus sign conditions.  Then for
every real z: z^T G z = sum_k d_k ((V^T z)_k)^2 (machine-verified
symbolic identity at every deployed dimension m); the triangular
structure gives (V^T z)_i = z_i + sum_{j>i} V_ji z_j
(machine-verified), so the LAST nonzero index i* of z has
(V^T z)_{i*} = z_{i*} != 0; hence z^T G z >= d_{i*} z_{i*}^2 > 0 and
G is positive definite.  For a rank-form reconstruction
G = sum_r c_r u_r u_r^T with every c_r > 0 the same expansion gives
z^T G z = sum_r c_r (u_r . z)^2 >= 0 (machine-verified), i.e. G is
positive semidefinite -- all R3 needs to make s_0, s_1 pointwise
nonnegative."""

R2_TEXT = """R2 (THE JOINT RELATION -- Schur pivot, CCLXV
sigma = 1 - s/n).  Let M = [[n, b^T],[b, B]] be symmetric of the
deployed dimension 8 with B invertible, y := B^{-1} b,
q := b^T B^{-1} b = y^T B y, sigma := q/n, s := n - q.
Machine-verified sympy identities with b eliminated via b = B y
(free symbols only -- 28 symmetric-B entries, 7 y entries, n; NO
numeric input): (i) C M C^T = diag(n - y^T B y, B) for the
unit-triangular C = [[1, -y^T],[0, I_7]]; (ii) C Cinv = I_8 for the
explicit inverse Cinv = [[1, y^T],[0, I_7]]; (iii) M =
Cinv diag(n - y^T B y, B) Cinv^T; (iv) s/n = 1 - sigma; (v) if
q = (1 - eta) n - r then n - q = eta n + r, and eta > 0, n > 0,
r >= 0 make eta n + r > 0 (assumption-verified); (vi) z^T B z =
z^T (B - c I) z + c z^T z (dimension 7), so B - c I positive
definite (R1) with c > 0 gives B positive definite.  Hence per cell:
B > 0 (floor pivots + (vi)), n > 0 (sign), and q <= (1 - eta) n
(R3/R4 + the checker's census) give s >= eta n > 0; by (iii) every
z != 0 has z^T M z = w^T diag(s, B) w with w = Cinv^T z != 0 (Cinv
invertible by (ii)), so M is positive definite with Schur reserve
sigma <= 1 - eta."""

R3_TEXT = """R3 (THE MAJORANT -- interval-SOS soundness).  For
u(x) = (1, x, ..., x^{m-1}) and symmetric G:
u(x)^T G u(x) = sum_{ij} G_ij x^{i+j} -- machine-verified at every
deployed Gram dimension m; so the checker's gram-polynomials
s_0, s_1 are exactly the quadratic forms u^T G_0 u, u^T G_1 u,
pointwise >= 0 by R1 (positive pivots or positive rank
coefficients).  The certificate identity x p(x) - 1 = s_0(x) +
(x - beta)(L - x) s_1(x) -- verified per certificate by the
checker's exact rational expansion -- then gives, for
beta <= x <= L with beta > 0: (x - beta) >= 0 and (L - x) >= 0, so
(x - beta)(L - x) s_1(x) >= 0 and x p(x) - 1 >= 0
(assumption-verified sign chain), and division by x >= beta > 0
gives p(x) >= 1/x on [beta, L]."""

R4_TEXT = """R4 (MOMENT DOMINATION -- the linear bound consumes only
moments).  Spectral theorem (E2, the SINGLE external-cited
reduction): B = V diag(d) V^T with V orthogonal, g := V^T b, so
b^T B^k b = g^T diag(d)^k g; the floor/ceiling reconstructions (R1,
R2(vi)) place every atom d_i strictly inside (c, L), and the
checker's domain gate puts [c, L] inside the certificate interval
[beta, L_cert].  Machine-verified sympy identities on the diagonal
form (7 atoms, generic coefficients, NO numeric input):
(i) nu_k = g^T diag(d)^k g = sum_i g_i^2 d_i^k for k = 0..9;
(ii) q = g^T diag(d)^{-1} g = sum_i g_i^2 / d_i;
(iii) sum_j c_j nu_j - q = sum_i g_i^2 (p(d_i) - 1/d_i).
With p >= 1/x on [beta, L_cert] (R3) every term of (iii) is >= 0
(assumption-verified), hence q <= sum_j c_j nu_j.  ONE-LINE THEOREM
(per cell, every step exact): for the wall matrix
M = [[n, b^T],[b, B]] with certified floor c, certified ceiling L
and verified certificate (beta, L_cert, p, G_0, G_1) covering
[c, L]: sum_j c_j nu_j <= (1 - eta) n implies sigma = q/n <= 1 - eta
implies M positive definite with Schur reserve s >= eta n."""

STATEMENTS = (("R1", R1_TEXT), ("R2", R2_TEXT), ("R3", R3_TEXT),
              ("R4", R4_TEXT))


def sha16(txt):
    return hashlib.sha256(txt.encode("utf-8")).hexdigest()[:16]


# ============================================= S0: firewall wards
def ast_scan_self(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


def ast_scan_floats(func_names):
    """Relation functions must contain NO float literal (R0)."""
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef) \
                and node.name in func_names:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, float):
                    bad.append("%s:%r" % (node.name, sub.value))
    return bad


def ast_scan_checker():
    """The checker's import surface (S0.3) and line count (S0.4)."""
    src = open(CHK_PATH, encoding="utf-8").read()
    mods = set()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Import):
            mods.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            mods.add((node.module or "").split(".")[0])
    n_lines = src.count("\n") + (0 if src.endswith("\n") else 1)
    return mods, n_lines


# ==================================== R: the relation certificates
def rel_r1(dims):
    """R1: elimination + rank-form soundness, symbolically."""
    for m in dims:
        zv = sp.Matrix(sp.symbols("z0:%d" % m, real=True))
        low = sp.Matrix(m, m, lambda i, j:
                        sp.Symbol("l_%d_%d" % (i, j), real=True)
                        if i > j else (sp.Integer(1) if i == j
                                       else sp.Integer(0)))
        dvs = sp.symbols("d0:%d" % m, positive=True)
        gm = low * sp.diag(*dvs) * low.T
        quad = sp.expand((zv.T * gm * zv)[0, 0])
        wv = low.T * zv
        tgt = sp.expand(sum(dvs[i] * wv[i] ** 2 for i in range(m)))
        if sp.expand(quad - tgt) != 0:
            return False
        for i in range(m):
            tri = zv[i] + sum(low[j, i] * zv[j]
                              for j in range(i + 1, m))
            if sp.expand(wv[i] - tri) != 0:
                return False
    # rank form at the largest deployed dimension, two terms
    m = max(dims)
    zv = sp.Matrix(sp.symbols("z0:%d" % m, real=True))
    ranks = []
    for r in range(2):
        cf = sp.Symbol("c%d" % r, positive=True)
        uv = sp.Matrix(sp.symbols("u%d_0:%d" % (r, m), real=True))
        ranks.append((cf, uv))
    gm = sum((cf * uv * uv.T for cf, uv in ranks),
             sp.zeros(m, m))
    quad = sp.expand((zv.T * gm * zv)[0, 0])
    tgt = sp.expand(sum(cf * (uv.T * zv)[0, 0] ** 2
                        for cf, uv in ranks))
    if sp.expand(quad - tgt) != 0:
        return False
    # the sign steps of the statement (assumption queries)
    dpos = sp.Symbol("d", positive=True)
    tnz = sp.Symbol("t", real=True, nonzero=True)
    cpos = sp.Symbol("c", positive=True)
    snn = sp.Symbol("s", real=True)
    return bool((dpos * tnz ** 2).is_positive) \
        and bool((cpos * snn ** 2).is_nonnegative)


def rel_r2():
    """R2: the Schur pivot chain at the deployed dimension 8."""
    dim = 7
    nn = sp.Symbol("n", real=True)
    yv = sp.Matrix(sp.symbols("y0:%d" % dim, real=True))
    bb = sp.Matrix(dim, dim, lambda i, j: sp.Symbol(
        "B_%d_%d" % (min(i, j), max(i, j)), real=True))
    bvec = bb * yv
    mm = sp.zeros(dim + 1, dim + 1)
    mm[0, 0] = nn
    for i in range(dim):
        mm[0, i + 1] = bvec[i]
        mm[i + 1, 0] = bvec[i]
        for j in range(dim):
            mm[i + 1, j + 1] = bb[i, j]
    cc = sp.eye(dim + 1)
    cinv = sp.eye(dim + 1)
    for i in range(dim):
        cc[0, i + 1] = -yv[i]
        cinv[0, i + 1] = yv[i]
    sexpr = nn - (yv.T * bb * yv)[0, 0]
    dg = sp.zeros(dim + 1, dim + 1)
    dg[0, 0] = sexpr
    for i in range(dim):
        for j in range(dim):
            dg[i + 1, j + 1] = bb[i, j]
    if sp.expand(cc * mm * cc.T - dg) != sp.zeros(dim + 1, dim + 1):
        return False
    if sp.expand(cc * cinv) != sp.eye(dim + 1):
        return False
    if sp.expand(cinv * dg * cinv.T - mm) \
            != sp.zeros(dim + 1, dim + 1):
        return False
    qq = sp.Symbol("q", real=True)
    if sp.simplify((nn - qq) / nn - (1 - qq / nn)) != 0:
        return False
    eta = sp.Symbol("eta", positive=True)
    npos = sp.Symbol("np", positive=True)
    rnn = sp.Symbol("r", nonnegative=True)
    qdef = (1 - eta) * npos - rnn
    if sp.expand((npos - qdef) - (eta * npos + rnn)) != 0:
        return False
    if not bool((eta * npos + rnn).is_positive):
        return False
    zv = sp.Matrix(sp.symbols("w0:%d" % dim, real=True))
    cfl = sp.Symbol("c", real=True)
    shifted = bb - cfl * sp.eye(dim)
    lhs = (zv.T * bb * zv)[0, 0]
    rhs = (zv.T * shifted * zv)[0, 0] \
        + cfl * sum(zv[i] ** 2 for i in range(dim))
    return sp.expand(lhs - rhs) == 0


def rel_r3(dims):
    """R3: Gram evaluation identity + the sign chain."""
    xx = sp.Symbol("x", real=True)
    for m in dims:
        gm = sp.Matrix(m, m, lambda i, j: sp.Symbol(
            "G_%d_%d" % (min(i, j), max(i, j)), real=True))
        uv = sp.Matrix([xx ** i for i in range(m)])
        quad = sp.expand((uv.T * gm * uv)[0, 0])
        tgt = sp.expand(sum(gm[i, j] * xx ** (i + j)
                            for i in range(m) for j in range(m)))
        if sp.expand(quad - tgt) != 0:
            return False
    ann = sp.Symbol("a", nonnegative=True)   # x - beta
    cnn = sp.Symbol("cn", nonnegative=True)  # L - x
    s0n = sp.Symbol("s0", nonnegative=True)
    s1n = sp.Symbol("s1", nonnegative=True)
    xpos = sp.Symbol("xp", positive=True)
    tno = s0n + ann * cnn * s1n
    return bool((ann * cnn * s1n).is_nonnegative) \
        and bool(tno.is_nonnegative) \
        and bool((tno / xpos).is_nonnegative)


def rel_r4(deg_max):
    """R4: moment identities on the diagonal form + domination."""
    na = R4_ATOMS
    gvs = sp.symbols("g0:%d" % na, real=True)
    dvs = sp.symbols("dd0:%d" % na, positive=True)
    gv = sp.Matrix(gvs)
    dg = sp.diag(*dvs)
    for k in range(R4_KMAX + 1):
        lhs = sp.expand((gv.T * dg ** k * gv)[0, 0])
        rhs = sp.expand(sum(gvs[i] ** 2 * dvs[i] ** k
                            for i in range(na)))
        if sp.expand(lhs - rhs) != 0:
            return False
    qlhs = sp.expand((gv.T * dg.inv() * gv)[0, 0])
    qrhs = sum(gvs[i] ** 2 / dvs[i] for i in range(na))
    if sp.expand(qlhs - qrhs) != 0:
        return False
    cfs = sp.symbols("cf0:%d" % (deg_max + 1), real=True)
    nus = [sum(gvs[i] ** 2 * dvs[i] ** k for i in range(na))
           for k in range(deg_max + 1)]
    lin = sum(cfs[k] * nus[k] for k in range(deg_max + 1))
    qq = sum(gvs[i] ** 2 / dvs[i] for i in range(na))
    pofd = [sum(cfs[k] * dvs[i] ** k for k in range(deg_max + 1))
            for i in range(na)]
    rear = sum(gvs[i] ** 2 * (pofd[i] - 1 / dvs[i])
               for i in range(na))
    dprod = sp.prod(dvs)
    if sp.expand(((lin - qq) - rear) * dprod) != 0:
        return False
    wnn = sp.Symbol("w", nonnegative=True)
    mnn = sp.Symbol("m0", nonnegative=True)
    return bool((wnn * mnn).is_nonnegative)


def relation_part(gram_dims, deg_max):
    section("R -- PART 1: THE RELATION CERTIFICATE (symbolic, no "
            "numeric input)")
    bad = ast_scan_floats(("rel_r1", "rel_r2", "rel_r3", "rel_r4"))
    check("R0 relation functions contain NO float literal "
          "(AST-scanned)", not bad, ",".join(bad), kill="K2")
    dims_r1 = sorted(set(gram_dims) | {7, 8})
    t_r = time.time()
    ok1 = rel_r1(dims_r1)
    check("R1 elimination/rank-form soundness identities at dims %s "
          "[%.1f s]" % (dims_r1, time.time() - t_r), ok1, kill="K2")
    t_r = time.time()
    ok2 = rel_r2()
    check("R2 Schur pivot chain (congruence, inverse, reassembly, "
          "sigma = 1 - s/n, reserve arithmetic, floor shift) at "
          "dim 8 [%.1f s]" % (time.time() - t_r), ok2, kill="K2")
    t_r = time.time()
    ok3 = rel_r3(sorted(set(gram_dims)))
    check("R3 Gram evaluation identity at dims %s + sign chain "
          "[%.1f s]" % (sorted(set(gram_dims)), time.time() - t_r),
          ok3, kill="K2")
    t_r = time.time()
    ok4 = rel_r4(deg_max)
    check("R4 moment identities (%d atoms, degree <= %d) + "
          "domination rearrangement [%.1f s]"
          % (R4_ATOMS, deg_max, time.time() - t_r), ok4, kill="K2")
    joint = sha16("\n\n".join(txt for _i, txt in STATEMENTS))
    print("    frozen statements: %s; joint statement sha %s"
          % (", ".join(i for i, _t in STATEMENTS), joint))
    for sid, txt in STATEMENTS:
        print("\n  --- %s (verbatim, sha %s) ---\n%s"
              % (sid, sha16(txt), txt))
    return [dict(id=sid, text=txt, hash=sha16(txt),
                 verified="sympy-symbolic, no numeric input")
            for sid, txt in STATEMENTS], joint


# ================================ G: the stored global certificates
def load_stored_proof():
    section("G -- PART 2 (global tier): the stored CCXCIII proof "
            "object, reused verbatim and re-verified")
    raw = open(PROOF_JSON, "rb").read()
    proof_sha = hashlib.sha256(raw).hexdigest()[:16]
    stored = json.loads(raw)
    print("    %s: sha %s, schema %s, census_cells %s"
          % (os.path.basename(PROOF_JSON), proof_sha,
             stored.get("schema"), stored.get("census_cells")))
    certs = {}
    n_ok = 0
    n_hash = 0
    for deg in GLOB_DEGS:
        cj = stored["global_certificates"][str(deg)]
        cert = dict(kind=cj["kind"], deg=cj["deg"],
                    beta=Fraction(cj["beta"]), L=Fraction(cj["L"]),
                    c_x=[Fraction(v) for v in cj["p_coeffs_x"]],
                    G0=[[Fraction(v) for v in row]
                        for row in cj["G0"]],
                    G1=[[Fraction(v) for v in row]
                        for row in cj["G1"]],
                    lift=Fraction(cj["lift"]))
        okv, hh = rs.verify_cert_exact(cert)
        if okv:
            n_ok += 1
            cert["hash"] = hh
            cert["verified"] = True
            certs[deg] = cert
            if hh == cj["hash"]:
                n_hash += 1
        print("    K = %d: re-verified %s, hash %s (stored %s) "
              "[%.1f s]" % (deg, "OK" if okv else "FAIL", hh,
                            cj["hash"], time.time() - T0),
              flush=True)
    check("G3 stored global certificates re-verified (identity + "
          "sympy + exact PSD) with EQUAL hashes: %d/%d verified, "
          "%d/%d hash-equal" % (n_ok, len(GLOB_DEGS), n_hash,
                                len(GLOB_DEGS)),
          n_ok == len(GLOB_DEGS) and n_hash == len(GLOB_DEGS),
          kill="K2")
    check("G4 source pedigree: stored spec_sha == the CCXCIII "
          "module's SPEC-SHA (%s...)" % stored["spec_sha"][:8],
          stored["spec_sha"] == rs.SPEC_SHA, kill="K3")
    return stored, certs, proof_sha


def stored_anchors(stored, uni, eta_trunc, worst):
    check("G5 stored census_cells %s == built census %d == expected "
          "%d" % (stored["census_cells"], len(uni), CELL_EXP),
          SMOKE or (int(stored["census_cells"]) == len(uni)
                    == CELL_EXP), kill="K3")
    eta_stored = Fraction(stored["eta_star"])
    worst_stored = Fraction(stored["worst_bound"])
    check("G6 digit-identical repro: eta* == stored (%s == %s: %s) "
          "AND worst bound EXACTLY equal (%.9f: %s) AND eta* == "
          "frozen bar %s"
          % (eta_trunc, stored["eta_star"], eta_trunc == eta_stored,
             float(worst), worst == worst_stored,
             ETA_STAR_REF),
          SMOKE or (eta_trunc == eta_stored == ETA_STAR_REF
                    and worst == worst_stored), kill="K3")


# ======================================= the package cell records
def cert_to_json(cert):
    out = dict(kind=cert["kind"], deg=cert["deg"],
               beta=str(cert["beta"]), L=str(cert["L"]),
               p_coeffs_x=[str(v) for v in cert["c_x"]],
               G0=[[str(v) for v in row] for row in cert["G0"]],
               G1=[[str(v) for v in row] for row in cert["G1"]],
               lift=str(cert["lift"]), hash=cert["hash"])
    for key in ("G0_rank", "G1_rank"):
        if cert.get(key) is not None:
            out[key] = [[str(cf), [str(v) for v in vec]]
                        for cf, vec in cert[key]]
    return out


def compute_rho(rows_list):
    """The rational relative moment-box radius per cell: perturbing
    every moment by |delta nu_j| <= rho nu_j keeps the census
    inequality (linear margin over the absolute-coefficient mass)."""
    for row in rows_list:
        cxs = row["best_cert"]["c_x"]
        den = sum(abs(cf) * mv
                  for cf, mv in zip(cxs, row["momv"]))
        row["rho"] = (((FR1 - ETA) - row["best_fr"])
                      * row["piv_fr"] / den if den > 0 else FR0)


def cell_record(row):
    mat = np.asarray(row["step"]["Mt"], float)
    m_fr = [[str(Fraction(float(mat[i, j])))
             for j in range(mat.shape[1])]
            for i in range(mat.shape[0])]
    cert = row["best_cert"]
    momv = row["momv"]
    piv = row["piv_fr"]
    bound = row["best_fr"]
    rho = row["rho"]
    return dict(
        id=int(row["index"]), seg=row["seg"], kz=int(row["kz"]),
        h=float(row["h"]), M=m_fr,
        region=dict(floor=str(row["c_cert"]),
                    ceiling=str(row["l_fr"])),
        moments=[str(v) for v in momv], n=str(piv),
        certificate=cert_to_json(cert),
        bound=str(bound), rho=str(rho))


# ================================== C: PART 3 -- the coverage map
def coverage_part(uni, ext, certs_glob):
    section("C -- PART 3: THE COVERAGE CERTIFICATE (the honest "
            "region)")
    compute_rho(uni + ext)
    ivals = sorted((r["c_cert"], r["l_fr"]) for r in uni)
    merged = []
    for lo, hi in ivals:
        if merged and lo <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    gaps = [[merged[i][1], merged[i + 1][0]]
            for i in range(len(merged) - 1)]
    cov_lo, cov_hi = merged[0][0], merged[-1][1]
    print("    1-D spectral union: %d cell intervals -> %d merged "
          "segment(s), %d gap(s) inside [%.6f, %.4f]"
          % (len(ivals), len(merged), len(gaps), float(cov_lo),
             float(cov_hi)))
    for glo, ghi in gaps[:8]:
        print("      gap: (%.6f, %.6f)" % (float(glo), float(ghi)))
    check("C1 coverage union computed exactly: %d segment(s), %d "
          "gap(s) (reported honestly, no bar)"
          % (len(merged), len(gaps)), True)

    # cross-coverage: cert i covers cell j (interval inclusion +
    # exact linear bound)
    bar = (FR1 - ETA)
    counts = []
    self_only = 0
    for rj in uni:
        cnt = 0
        for ri in uni:
            ci = ri["best_cert"]
            if ci["beta"] <= rj["c_cert"] and ci["L"] >= rj["l_fr"]:
                acc = sum(cf * mv for cf, mv
                          in zip(ci["c_x"], rj["momv"]))
                if acc <= bar * rj["piv_fr"]:
                    cnt += 1
        counts.append(cnt)
        if cnt == 1:
            self_only += 1
    check("C2 own-cell coverage: every census cell is covered by "
          "its own certificate (%d/%d; cross-coverage min/med/max "
          "%d/%d/%d, %d cells covered only by themselves)"
          % (sum(1 for c in counts if c >= 1), len(uni),
             min(counts), int(statistics.median(counts)),
             max(counts), self_only),
          all(c >= 1 for c in counts), kill="K2")

    # the reused global tier, honestly weak
    n_g1 = 0
    n_ge = 0
    for rj in uni:
        best = None
        for deg in GLOB_DEGS:
            bb = rs.bound_from_cert(certs_glob.get(deg), rj["momv"],
                                    rj["piv_fr"], rj["c_cert"],
                                    rj["l_fr"])
            if bb is not None and (best is None or bb < best):
                best = bb
        if best is not None and best < FR1:
            n_g1 += 1
        if best is not None and best <= bar:
            n_ge += 1
    print("    global tier (reused): bound < 1 on %d/%d cells, <= "
          "1 - eta on %d/%d -- the per-cell tier is needed, exactly "
          "as CCXCIII measured" % (n_g1, len(uni), n_ge, len(uni)))

    rhos = [float(r["rho"]) for r in uni]
    check("C3 rational moment-box radius rho_i > 0 on every census "
          "cell: %d/%d (min/med/max %.3e/%.3e/%.3e)"
          % (sum(1 for r in uni if r["rho"] > 0), len(uni),
             min(rhos), statistics.median(rhos), max(rhos)),
          all(r["rho"] > 0 for r in uni), kill="K2")

    verdict = (
        "COVERAGE VERDICT: FULL-COVERAGE(R_cert) AND PARTIAL(K). "
        "R_cert = union over the %d census cells of E_i = "
        "{M = [[n, b^T],[b, B]] symmetric 8x8 : n > 0, B - c_i I "
        "reconstructs with positive pivots, L_i I - B reconstructs "
        "with positive pivots, sum_j c_j^(i) nu_j(b, B) <= "
        "(1 - eta) n}, eta = %s -- every point of E_i is certified "
        "M positive definite with Schur reserve >= eta n by "
        "certificate i alone, so R_cert is fully covered BY "
        "CONSTRUCTION (overlaps harmless, each E_i individually "
        "sound); around every member the explicit rational relative "
        "moment box |delta nu_j| <= rho_i nu_j holds with rho "
        "min/med/max %.3e/%.3e/%.3e; the 1-D spectral union of the "
        "cell intervals has %d segment(s) and %d gap(s) inside "
        "[%.6f, %.4f] (exact rational endpoints in the package "
        "fields).  THE DECLARED AMBIENT REGION K -- the frozen "
        "C_KS class box (CCLXI box-SHA 224a2737, CCLXXXV frame "
        "6dfe799c) under the joint Radau relation -- is NOT fully "
        "certificate-covered: not covered are class-box points "
        "whose co-block spectrum fits no single certified "
        "[c_i, L_i], moment vectors outside all %d half-spaces, "
        "the unbuilt h > 1450 flank and the CCLXXXVII "
        "deep-membership lane, and the all-h quantifier; the "
        "class-box level remains CCLXXXV's conditional theorem "
        "chain plus a NUMERIC extremal (sup tr R = 0.972698), NOT "
        "a certificate.  The global tier (reused) reaches bound < 1 "
        "on %d/%d cells and <= 1 - eta on %d/%d.  The honest "
        "answer: the class box modulo the relation, plus %d sampled "
        "cells with explicit rational neighborhoods (and %d "
        "separately typed deep-extension cells)."
        % (len(uni), ETA, min(rhos), statistics.median(rhos),
           max(rhos), len(merged), len(gaps), float(cov_lo),
           float(cov_hi), len(uni), n_g1, len(uni), n_ge, len(uni),
           len(uni), len(ext)))
    print("\n  " + verdict)
    part3 = dict(
        declared_region=(
            "the frozen C_KS class box (CCLXI box-SHA 224a2737, "
            "CCLXXXV frame 6dfe799c) under the joint Radau "
            "relation"),
        covering_interval=[str(cov_lo), str(cov_hi)],
        union_segments=[[str(a), str(b)] for a, b in merged],
        gaps=[[str(a), str(b)] for a, b in gaps],
        cross_coverage=dict(min=min(counts),
                            median=int(statistics.median(counts)),
                            max=max(counts), self_only=self_only),
        global_tier=dict(below_1=n_g1, below_1_minus_eta=n_ge),
        rho_stats=dict(min=min(rhos),
                       median=statistics.median(rhos),
                       max=max(rhos)),
        verdict=verdict, verdict_sha=sha16(verdict))
    return part3, verdict


# ============================================ W: write the package
def build_package(uni, ext, certs_glob, stored, proof_sha,
                  statements, joint_sha, part3, eta_trunc,
                  chk_lines, chk_mods):
    section("W -- THE PACKAGE: cofinal_package.json")
    cells = [cell_record(r) for r in uni]
    ext_cells = [cell_record(r) for r in ext]
    kinds = {}
    for r in uni:
        kinds[r["best_kind"]] = kinds.get(r["best_kind"], 0) + 1
    print("    consumed certificate kinds: %s"
          % ", ".join("%s x%d" % kv for kv in sorted(kinds.items())))
    blob = dict(
        schema="tfpt.cofinal_package.v1",
        mission="PRIME.COFINAL.PACKAGE.01",
        spec_sha=SPEC_SHA,
        source=dict(probe="radau_sos_certificate_probe (CCXCIII)",
                    spec_sha=rs.SPEC_SHA,
                    proof_json_sha=proof_sha),
        eta=str(ETA),
        eta_star=str(eta_trunc),
        census=dict(cells=len(cells),
                    pass_at_eta=len(cells),
                    extension_cells=len(ext_cells)),
        part1_relation=dict(
            statements=statements,
            joint_sha=joint_sha,
            external_cited=[
                "E2 spectral theorem (Horn & Johnson 2013): the "
                "reduction of R4 to the diagonal form and the "
                "eigenvalue reading of the floor/ceiling "
                "certificates"]),
        part2_positivity=dict(
            schema_note=(
                "per cell: wall matrix M (exact dyadic rationals), "
                "region = certified floor/ceiling, exact moments "
                "nu_0..nu_9, pivot n, the consumed certificate "
                "(interval-SOS, rational Grams, rank certificates "
                "where PSD-by-structure), exact bound "
                "sum c_j nu_j / n and moment-box radius rho"),
            cells=cells,
            extension_cells=ext_cells,
            global_certificates={
                str(deg): stored["global_certificates"][str(deg)]
                for deg in GLOB_DEGS},
            worst_cell_exhibit=stored["worst_cell_exhibit"]),
        part3_coverage=part3,
        checker=dict(
            file="tiny_checker.py", lines=chk_lines,
            imports=sorted(chk_mods),
            trusts=("python stdlib integer/Fraction arithmetic and "
                    "this package file; the matrix-theoretic "
                    "implications live in part1_relation")))
    path = PKG_SMOKE if SMOKE else PKG_JSON
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(blob, fh, indent=1)
    fsha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    size = os.path.getsize(path)
    check("W1 package written: %s (%.1f MB, sha256 %s...%s), %d "
          "census cells + %d extension + %d global certificates"
          % (os.path.basename(path), size / 1048576.0, fsha[:12],
             fsha[-4:], len(cells), len(ext_cells), len(GLOB_DEGS)),
          len(cells) == len(uni) and len(ext_cells) == len(ext))
    return path, fsha


# =========================================== X: the checker gates
def run_checker(path, timeout):
    try:
        res = subprocess.run(
            [sys.executable, CHK_PATH, path], capture_output=True,
            text=True, timeout=timeout)
        return res.returncode, (res.stdout + res.stderr).strip()
    except subprocess.TimeoutExpired:
        return -1, "TIMEOUT"


def _doctor(path, mutate, tag):
    blob = json.load(open(path, encoding="utf-8"))
    mutate(blob)
    tmp = os.path.join(_HERE, "_doctor_%s.tmp.json" % tag)
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(blob, fh, indent=1)
    rc, out = run_checker(tmp, CHK_TIMEOUT_DOC)
    os.remove(tmp)
    return rc, out


def _forge_hash(cj):
    blob = "|".join(
        [str(Fraction(cj["beta"])), str(Fraction(cj["L"]))]
        + [str(Fraction(v)) for v in cj["p_coeffs_x"]]
        + [str(Fraction(v)) for row in cj["G0"] for v in row]
        + [str(Fraction(v)) for row in cj["G1"] for v in row])
    return hashlib.sha256(blob.encode()).hexdigest()[:16]


def doc_coeff(blob):
    cj = blob["part2_positivity"]["cells"][0]["certificate"]
    cj["p_coeffs_x"][0] = str(Fraction(cj["p_coeffs_x"][0]) + 1)
    cj["hash"] = _forge_hash(cj)     # hash re-forged: only the
    # exact identity expansion can catch this doctor


def doc_pivot(blob):
    cell = blob["part2_positivity"]["cells"][0]
    piv = Fraction(cell["n"]) / DOCTOR_SCALE
    cell["n"] = str(piv)
    cell["M"][0][0] = str(piv)
    cell["bound"] = str(Fraction(cell["bound"]) * DOCTOR_SCALE)


def doc_stmt(blob):
    blob["part1_relation"]["statements"][0]["text"] += " DOCTORED"


def checker_gates(pkg_path, n_cells, n_ext):
    section("X2 -- THE CHECKER: full-package census + doctored "
            "controls")
    t_c = time.time()
    rc, out = run_checker(pkg_path, CHK_TIMEOUT_REAL)
    tail = out.splitlines()[-1] if out else "(no output)"
    print("    checker says: %s [%.1f s]" % (tail, time.time() - t_c))
    want = "cells %d/%d" % (n_cells, n_cells)
    check("X7 checker census 100%%: exit 0, ALL PASS, %s, "
          "extension %d/%d" % (want, n_ext, n_ext),
          rc == 0 and "ALL PASS" in out and want in out
          and "extension %d/%d" % (n_ext, n_ext) in out, kill="K2")
    doctors = (
        ("X8", doc_coeff, "SOS identity residual",
         "flipped p-coefficient with re-forged hash"),
        ("X9", doc_pivot, "census bound > 1 - eta",
         "pivot n scaled by 1/%d with forged bound" % DOCTOR_SCALE),
        ("X10", doc_stmt, "statement hash",
         "tampered relation statement text"))
    for cid, mut, expect, label in doctors:
        rc_d, out_d = _doctor(pkg_path, mut, cid)
        line = out_d.splitlines()[-1] if out_d else "(no output)"
        check("%s doctored package (%s) FAILS at the named gate "
              "('%s'): exit %d, '%s'"
              % (cid, label, expect, rc_d, line[:70]),
              rc_d != 0 and expect in out_d, kill="K4")


# =============================================================== V
def finish(n_cells, n_ext, verdict_cov, chk_lines):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif n_pass == n_tot:
        v = ("PACKAGE-SEALED(relation 4/4 symbolic; positivity "
             "%d/%d cells at eta = %.3f (+%d extension, separate); "
             "coverage typed FULL-COVERAGE(R_cert) AND PARTIAL(K); "
             "checker %d lines, census 100%%, 3/3 doctored controls "
             "fired)" % (n_cells, n_cells, float(ETA), n_ext,
                         chk_lines))
        print("\n  VERDICT: %s" % v)
        print("\n  THE THREE PARTS, one line each:")
        print("  (1) RELATION: R1-R4 frozen verbatim above, every "
              "identity sympy-verified on free symbols only.")
        print("  (2) POSITIVITY: one verified rational certificate "
              "per cell, %d/%d at eta = %.3f, digit-identical to "
              "the CCXCIII proof object." % (n_cells, n_cells,
                                             float(ETA)))
        print("  (3) COVERAGE: %s" % verdict_cov[:200] + "...")
    else:
        bad = [nm for nm, ok in CHECKS if not ok]
        v = "PACKAGE-PARTIAL(%s)" % "; ".join(bad[:4])
        print("\n  VERDICT: %s" % v)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


# =============================================================== main
def main():
    section("PRIME.COFINAL.PACKAGE.01 -- the theorem package "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))
    print("    bars: eta %s, cells %d, checker <= %d lines, "
          "imports %s" % (ETA, CELL_EXP, CHK_MAX_LINES,
                          sorted(CHK_ALLOWED)))

    print("\nS0 -- firewall / scope wards")
    bad = ast_scan_self(k5.BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    chk_mods, chk_lines = ast_scan_checker()
    check("S0.3 checker import surface == %s (found %s)"
          % (sorted(CHK_ALLOWED), sorted(chk_mods)),
          chk_mods <= CHK_ALLOWED, kill="K2")
    check("S0.4 checker size %d lines <= %d (stdlib-only, "
          "fail-fast)" % (chk_lines, CHK_MAX_LINES),
          chk_lines <= CHK_MAX_LINES, kill="K2")

    # U -- the CCLXXIX universe via the CCXCIII/K5 builders
    _zones, steps, census, combined = k5.build_ladder()
    if KILLS:
        return finish(0, 0, "", chk_lines)
    k5.artifact_key_ward(steps)
    f0_cells = k5.build_f0(combined)
    if KILLS:
        return finish(0, 0, "", chk_lines)
    families = k5.build_families(census, combined)
    if KILLS:
        return finish(0, 0, "", chk_lines)
    n_sweep = len(f0_cells) + sum(len(v) for v in families.values())
    n_cells = len(steps) + n_sweep
    check("U1 wall-legal universe: %d ladder + %d sweep = %d cells "
          "(CCLXXIX frozen expectation %d)"
          % (len(steps), n_sweep, n_cells, CELL_EXP),
          SMOKE or n_cells == CELL_EXP, kill="K3")
    f5x_cells = rs.build_f5x(combined)
    rows = k5.make_rows(steps, f0_cells, families)
    for dd in f5x_cells:
        st = dd["step"]
        rows.append(dict(step=st, seg="F5X",
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         schur=float(st["gap"]),
                         n_piv=float(st["n0"]),
                         lam_b=float(st["lamB1"]),
                         mode=dd.get("mode", "deep-ext")))
    for i, row in enumerate(rows):
        row["index"] = i
    rows = k5.jacobi_identity_wards(rows)
    if KILLS:
        return finish(0, 0, "", chk_lines)
    k5.pivot_ward(rows)
    k5.repro_anchors([r for r in rows if r["seg"] != "F5X"])
    if KILLS:
        return finish(0, 0, "", chk_lines)

    # E/P/T -- the CCXCIII machinery, unchanged
    rs.exact_cell_data(rows)
    if KILLS:
        return finish(0, 0, "", chk_lines)
    rs.percell_tier(rows)
    if KILLS:
        return finish(0, 0, "", chk_lines)
    uni, eta_trunc, worst = rs.eta_census(rows)
    ext = [r for r in rows if r["seg"] == "F5X"
           and r.get("best_fr") is not None]

    # G -- the stored proof object, reused + anchored
    stored, certs_glob, proof_sha = load_stored_proof()
    if KILLS:
        return finish(len(uni), len(ext), "", chk_lines)
    stored_anchors(stored, uni, eta_trunc, worst)
    if KILLS:
        return finish(len(uni), len(ext), "", chk_lines)

    # R -- the relation certificates (dims read off the built data)
    gram_dims = sorted(
        {len(c["G0"]) for r in uni + ext for c in (r["best_cert"],)}
        | {len(c["G1"]) for r in uni + ext
           for c in (r["best_cert"],)}
        | {len(c["G0"]) for c in certs_glob.values()}
        | {len(c["G1"]) for c in certs_glob.values()})
    deg_max = max(len(r["best_cert"]["c_x"]) - 1 for r in uni + ext)
    statements, joint_sha = relation_part(gram_dims, deg_max)
    if KILLS:
        return finish(len(uni), len(ext), "", chk_lines)

    # C -- the coverage certificate
    part3, verdict_cov = coverage_part(uni, ext, certs_glob)
    if KILLS:
        return finish(len(uni), len(ext), verdict_cov, chk_lines)

    # W -- the package
    pkg_path, _fsha = build_package(
        uni, ext, certs_glob, stored, proof_sha, statements,
        joint_sha, part3, eta_trunc, chk_lines, chk_mods)

    # X -- CCXCIII controls re-run + the checker gates
    section("X1 -- inherited controls-must-fire (CCXCIII X1-X6, "
            "against the RELOADED global certificates)")
    rs.controls(rows, certs_glob)
    checker_gates(pkg_path, len(uni), len(ext))
    if SMOKE and os.path.exists(PKG_SMOKE):
        os.remove(PKG_SMOKE)
        print("    smoke package removed (frozen artifact only)")

    return finish(len(uni), len(ext), verdict_cov, chk_lines)


if __name__ == "__main__":
    sys.exit(main())
