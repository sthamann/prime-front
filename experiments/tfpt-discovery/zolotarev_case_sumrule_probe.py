#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zolotarev_case_sumrule_probe -- PRIME.ONEBADMODE.KS.DUAL.01 probe C
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE ANALYTIC HEART.  CCLIII proved the bridge: the eight complex tau
reads ARE Weyl m-function / resolvent-trace values of an 8x8 Jacobi
matrix J_h at eight FIXED off-spectrum points z_j, and the certificate
reserve is

  reserve(h) = 1 - tr R(J_h),   R(x) = 1 + sum_j 2 a_j Re 1/(x - z_j)

with the FROZEN CCXXV m=8 Zolotarev filter (c = 5523/10000,
L = max L_src, poles z_j = i y_j, residues a_j < 0).  CCLIII's census
came out PARTIAL because the NORM route (Hilbert-Schmidt perturbation
bounds) is 10^4 too loose at the decision poles while the KS currency
itself has the right size (capture -> 1.000).

THIS PROBE ABANDONS THE NORM ROUTE and asks the Killip-Simon question
instead: is there a POSITIVE SUM RULE for the reserve,

  1 - tr R(J_h) = delta_R + Q_R(J_h) + G_R(J_h) + H_R(J_h),

with delta_R > 0 a FROZEN constant and Q_R, G_R, H_R >= 0 -- a
Case-type sum rule whose test function is the Zolotarev separator
itself?  If such a grouping exists, the reserve certificate is one
line on every rung; if it does not, the MEASURED OBSTRUCTION (which
term goes negative, where, by how much) is the honest verdict.

EXTERNAL-CITED (facts consumed, warded numerically, never proved here).
  E1  Killip & Simon, Ann. Math. 158 (2003) 253-321.  The P2 sum rule
      for Jacobi matrices: quasi-Szego entropy + Lieb-Thirring
      eigenvalue term = l2 coefficient functional, with EVERY term
      nonnegative.  Used here as the STRUCTURAL TEMPLATE (coefficient
      part / eigenvalue part / entropy part) and as the name of the l2
      currency -- no spectral claim is imported.
  E2  Simon, J. Funct. Anal. 214 (2004) 396-409 ("Szego's theorem and
      its descendants" line): canonical factorization and STEP-BY-STEP
      sum rules for meromorphic Herglotz functions; the perturbation
      determinant factorizes into a Blaschke part (eigenvalue
      displacements) times an outer part (spectral density ratio).  At
      FIXED dimension 8 both parts are RATIONAL and exactly computable,
      which is what this probe exploits.
  E3  Damanik, Killip & Simon, Ann. Math. 171 (2010) 1931-2010:
      the periodic / finite-gap extension (isospectral torus) of the
      Killip-Simon theorem.  Used to license the FINITE-GAP reference
      (REFC below) as a legitimate member of the reference class.
  E4  Chebyshev-1 (arcsine) measure on [-1,1]: Jacobi parameters
      b_n = 0, a_1 = 1/sqrt 2, a_n = 1/2 (n >= 2); Stieltjes transform
      -1/sqrt(z^2-1).  [Szego, Orthogonal Polynomials, AMS 1939, 2.4.]
      This is CCLIII's free reference, taken over VERBATIM.
  E5  Zolotarev / rational spectral projector: the frozen filter obeys
      0 <= R(x) <= delta_Z for x in +-[c, L] (equioscillation level
      delta_Z certified inside zolotarev_phase_filter_probe by interval
      products) and R(0) = 1, R even.  [Zolotarev 1877; Guettel et al.,
      "Zolotarev quadrature rules and load balancing for the FEAST
      eigensolver", arXiv:1407.8078.]  Warded here on a dense grid.
  E6  Perturbation determinant / Hankel-Vandermonde facts at finite
      dimension: -d/dz log det[(J-z)(J_*-z)^{-1}] = tr[(J-z)^{-1} -
      (J_*-z)^{-1}]; and for an N-atom measure with Jacobi data (a, b),
      prod_{n=1}^{N-1} a_n^{2(N-n)} = prod_k w_k prod_{k<l}
      (lambda_k - lambda_l)^2 (Cauchy-Binet / Gauss quadrature).
      [Simon, Trace Ideals, AMS 2005, Ch. 3; Gautschi, Orthogonal
      Polynomials, OUP 2004, 2.1-2.4; Deift, Orthogonal Polynomials
      and Random Matrices, AMS 1999, Ch. 2.]

DEPLOYED OBJECTS (read-only, reused verbatim; nothing re-derived).
  ob.ladder_zones / build_rung / make_steps / deep_zone_census /
  build_ext_tables (CCVII ladder), zol.assemble_step / build_filter
  (CCXXV filter), t2.jacobi_form / lu_read / cf_arrays / jacobi_matrix
  / linfit / screen (CCLIII bridge), eul.level_rung (CCXVII c_h),
  stored artifact zolotarev_phase_filter_phases.json (68 x 8).

FROZEN PROTOCOL (2026-08-12).

 S0 FIREWALL.  AST scan (banned prime/zero oracles); verification/ and
    all predecessor probes READ-ONLY; RNG only through the corpus
    scramble seed.
    AC1 the reference builders (ref_arcsine_unit / ref_arcsine_band /
    ref_log_band / ref_two_band) contain NO ladder identifier: every
    reference is built from the FROZEN filter geometry (c, L, m) alone,
    so delta_R is a constant of the filter, not of the rung.
    AC2 coef_part() -- the coefficient carrier -- contains NO read and
    NO spectral identifier of J_h (no eigenvalue, no resolvent of J_h,
    no q / tr / reserve): it is built from the Jacobi DATA difference
    and the FROZEN reference resolvent alone.

 W  THE LADDER, rebuilt read-only: 68 steps = 40 surface + 1 bridge +
    27 deep; the FIXED global m=8 filter rebuilt from source-only L and
    warded against the stored artifact; per step per pole the LU reads
    (log tau, phase, resolvent trace, q) warded against the 68x8 stored
    artifact and the partial-fraction trace / reserve reproduced.

 Z  THE FROZEN TEST FUNCTION (kill -> WARD-BROKEN).
    Z1 partial-fraction identity: R(x) = 1 + sum_j 2 a_j Re 1/(x-z_j)
       equals zol.scalar_r of the rebuilt filter on a dense declared
       grid (ties the read to the Zolotarev separator).
    Z2 E5 facts warded: R(0) = 1; R even; 0 <= R <= delta_Z on
       +-[c, L] over GRID_Z log-spaced points; 0 <= R <= 1 globally on
       the declared probe grid.
    Z3 the two FROZEN constants of the filter are computed and printed:
         delta_Z          = the equioscillation level,
         delta_R^Z        = 1 - NDIM * delta_Z    (the band-slack
                            constant of the sum rule),
         x_crit           = the unique root in (0, c) of
                            R(x) = 1 - (NDIM-1) delta_Z
       -- x_crit is the EXPLICIT sub-band threshold below which a
       single outlier eigenvalue can exhaust the whole reserve.

 J  THE JACOBI / SPECTRAL LAYER (kill -> WARD-BROKEN).  Per step the
    CCLIII Lanczos form J_h of (M_h, e_0), then eigendecomposition:
    eigenvalues lambda_k and the EIGHT normalized spectral measures
    mu_h^(s) = sum_k |<e_s, v_k>|^2 delta_{lambda_k} (one per site).
    J1 similarity Q^T M_h Q = J_h and Q^T Q = I at SIM_TIE.
    J2 tr R(J_h) = sum_k R(lambda_k) reproduces the partial-fraction
       LU read at SR_TIE (the spectral form of the reserve).
    J3 the site decomposition tr R(J_h) = sum_s int R dmu_h^(s) with
       every mu_h^(s) a probability measure, at SR_TIE.
    J4 the E6 Hankel-Vandermonde identity at dimension 8 (the finite
       canonical factorization: COEFFICIENTS = ENTROPY +
       CONFIGURATION), warded per rung at HV_TIE:
         sum_n 2(8-n) log a_n = sum_k log w_k^(0)
                                + 2 sum_{k<l} log|lambda_k - lambda_l|.

 X  THE FROZEN REFERENCES (all h-independent, printed once, warded
    identical across the ladder).
      REF0  arcsine on [-1,1] -- CCLIII's free reference VERBATIM (E4).
      REFA  arcsine on the filter band [c, L] (affine image of REF0;
            Jacobi data exact).
      REFB  log-arcsine on [c, L]: the push-forward of the arcsine of
            [log c, log L] under exp (Gauss-Chebyshev exact quadrature,
            convergence warded by node doubling at REF_TIE).
      REFC  the FINITE-GAP (E3 class) two-band equilibrium measure of
            +-[c, L]: density |x| / (pi sqrt((x^2-c^2)(L^2-x^2))), the
            pull-back of the arcsine of [c^2, L^2] under x -> x^2.
    X1 delta_R(ref) = 1 - tr R(J_*) is computed for all four; the
       BAND-INCLUSION of each reference spectrum is reported.  A
       reference with delta_R <= 0 is typed REF-VOID and excluded from
       the grouping search (its number is still printed -- the
       untransported arcsine is expected to be void, which is itself
       the measurement that the reference MUST be band-matched).

 D  THE DECOMPOSITION (mission a; kill -> WARD-BROKEN), per rung and
    per pole, all ties at DEC_TIE = 1e-12 relative.
    D1 the perturbation determinant: with D_h(z) = det(J_h - z) /
       det(J_* - z), the closed derivative -d/dz log D_h(z_j) equals
       tr[(J_h - z_j)^{-1} - (J_* - z_j)^{-1}] (E6), both routes
       computed independently (eigenvalue sum vs LU resolvent).
    D2 THE CANONICAL FACTORIZATION at the filter poles.  With the
       declared sorted pairing lambda_k <-> lambda*_k and the site-0
       weights,
         m_h(z_j) - m_*(z_j) = L_gap + L_coef + L_spread,
         L_gap    = sum_{k in OUT} w*_k [1/(lambda_k - z_j)
                                        - 1/(lambda*_k - z_j)],
         L_coef   = sum_{k in BAND} w*_k [same bracket],
         L_spread = sum_k (w_k - w*_k) / (lambda_k - z_j),
       where OUT = {k : |lambda_k| not in [c, L]} is the gap-outlier
       set.  The Blaschke-type part is L_gap + L_coef (eigenvalue
       displacement at frozen weights), the outer/entropy part is
       L_spread (weight transport at frozen eigenvalues).  Ward: the
       sum equals the LU read m_h(z_j) = [(M_h - z_j)^{-1}]_00 minus
       the reference m-function, per rung per pole.
    D3 the same split at the TRACE level (the level the reserve lives
       on), warded per rung per pole.

 S  THE SUM-RULE SEARCH (mission b).  Four DECLARED groupings, each an
    EXACT identity by construction; the search is over the SIGNS.
      GA BAND-SLACK (reference-free, filter-only):
         delta_R = 1 - NDIM delta_Z,
         Q_R = sum_k (delta_Z - R(lambda_k))^+,
         G_R = -sum_k (R(lambda_k) - delta_Z)^+,
         H_R = 0.
      GB BAND-SLACK-WITH-REMAINDER: identical to GA but the negative
         part is typed as the EXPLICIT REMAINDER
         E_out = sum_k (R(lambda_k) - delta_Z)^+ >= 0, i.e. the sum
         rule is read as 1 - tr R = delta_R + Q_R - E_out.
      GC REF-SPECTRAL (per admissible reference): the D2 split summed
         over the eight sites,
         Q_R = -sum_s sum_{k in BAND} w*_k^(s) [R(lambda_k)
                                                - R(lambda*_k)],
         G_R = -sum_s sum_{k in OUT} w*_k^(s) [same],
         H_R = -sum_s sum_k (w_k^(s) - w*_k^(s)) R(lambda_k).
      GD REF-LINEAR (per admissible reference): the coefficient carrier
         is the EXACT first-order response in the Jacobi data,
         Q_R = -sum_j 2 a_j Re coef_j,
         coef_j = -tr[(J_*-z_j)^{-1} (J_h - J_*) (J_*-z_j)^{-1}],
         G_R = the OUT displacement, H_R = the exact remainder.
    Per grouping: the identity ward at SR_TIE, the per-term min /
    median / max over the ladder, the ALL-NONNEGATIVE rung census, and
    the deep-rung sub-census.  TYPE:
      SUMRULE-POSITIVE(grouping)              -- all terms >= 0 and
                                                 delta_R > 0 on every
                                                 census rung;
      SUMRULE-POSITIVE-WITH-REMAINDER(...)    -- exactly one term is
                                                 negative, is named,
                                                 and its size and
                                                 support are measured;
      SUMRULE-OBSTRUCTED(...)                 -- otherwise, with the
                                                 negative terms, their
                                                 rung support and their
                                                 worst size.

 E  THE ENTROPY HULL.  For the transport carrier the Gibbs / Pinsker
    pair is computed: KL_s = sum_k w_k^(s) log(w_k^(s)/w*_k^(s)) >= 0
    (declared sorted pairing) and
      |H_R| <= sum_s max_k R(lambda_k) sqrt(2 KL_s),
    warded as a true bound on every rung (kill -> WARD-BROKEN) and
    reported as a ratio (hull / |H_R|).  This is the rigorous
    nonnegative entropy object behind the H carrier.

 C  CONTROLS (kill -> CONTROL-SILENT).  In CCLIII's aligned truth
    coordinates M_world = sym(Q_truth^T (S_world/tau_truth) Q_truth):
    C1 SMOOTH must violate the wall target (negA > 0) on every surface
       rung.
    C2 each falsifying world must, on a MAJORITY of aligned rungs,
       either BREAK the nonnegativity of the winning grouping (a term
       that is >= 0 on truth goes negative) or LEAVE THE CLASS (the
       aligned matrix leaves float64 range / is not cyclic ->
       REPRESENTATION-BREAK, counted as a fire and disclosed
       separately, CCLIII amendment A2b inherited verbatim).
    C3 the reserve itself must move: |reserve_world - reserve_truth|
       median >= CTRL_RES_BAR per world.

 P  SCREENS (mission c).  tau- and c_h-relocation screens (CCXLVII bars
    inherited verbatim) on every group value and on E_out.  delta_R is
    a FROZEN constant of the filter: its screen is VACUOUS BY
    CONSTRUCTION and is disclosed as such, never scored.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 predecessor reproduction -> REPRO-BROKEN; K4 a
required control silent -> CONTROL-SILENT.

VERDICT (frozen enum): CASE-SR( DECOMP-EXACT | DECOMP-BROKEN ;
SUMRULE-POSITIVE(...) | SUMRULE-POSITIVE-WITH-REMAINDER(...) |
SUMRULE-OBSTRUCTED(...) ; ENTROPY-HULL(ratio) ; OUTLIER(census) ;
CONTROLS(...) ) plus kills.  Every enum is a finite-ladder
theorem-engineering diagnostic, never an all-h statement and NEVER an
RH claim.  In particular a positive sum rule on the deployed ladder is
a REDUCTION of the reserve certificate to a spectral-inclusion
statement, NOT a proof of anything about the limit.

FROZEN BARS: NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; LU_TIE = 2e-9;
SIM_TIE = 1e-9; DEC_TIE = 1e-12; SR_TIE = 1e-12; HV_TIE = 1e-10;
REF_TIE = 1e-10; NONNEG_TOL = 1e-12; GRID_Z = 4001; REF_NODES = 4096;
CTRL_RES_BAR = 1e-3; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70;
DEEP_SUB_MIN = 4; runtime cap 25 min.

SMOKE DISCLOSURE: see SMOKE section at the end of this docstring.

NO RH claim.  Every number is a finite float64 measurement on the
deployed ladder; the limit question is untouched.  No marker moves; no
paper, ledger, website, manifest or verification file is touched.

Sources (read-only): rhp_tier2_polecontrol_probe (CCLIII bridge),
zolotarev_complex_tau_probe (CCXLVII reads), lattice_rhp_szego_probe
(CCXLV tier 1), onebadmode_moments_probe (CCVII ladder),
zolotarev_phase_filter_probe (CCXXV filter), euler_phase_identity_probe
(CCXVII c_h), v563_paper2_readouts (deployed window).

SMOKE (2026-08-12, before freezing; disclosed in full).
 SMOKE-1 (10 contiguous surface rungs + 3 lowest deep rungs) reshaped
 the spec in three places, all BEFORE the freeze:
 (i)   the untransported arcsine reference REF0 (CCLIII's free
       reference verbatim) has delta_R = -5.98 < 0: with a spectrum in
       [-1,1] the Zolotarev separator reads REF0 as almost seven
       eigenvalues.  REF-VOID typing was introduced (printed, excluded
       from the grouping census) together with the three band-matched
       references REFA/REFB/REFC; no bar was moved and the CCLIII
       object is still reported verbatim.
 (ii)  the equioscillation ward Z2 was formulated with the interval
       bound delta_Z of the rebuilt filter; the smoke showed the dense
       grid maximum of R on +-[c, L] is 1.690e-2 against
       delta_Z = 1.826e-2, i.e. the interval level is a strict upper
       bound as cited, so Z2 asks for <= delta_Z (not equality).
 (iii) the REFB node-doubling ward needed a relative tie because the
       exp push-forward has a huge dynamic range; REF_TIE = 1e-10
       relative on the Jacobi data was declared with that argument.
 SMOKE-2 (post-corrections) ran GREEN with no kills and additionally
 DISCLOSES the readings that were known before the frozen run (they are
 NOT bars, no enum or screen was touched): the reserve is carried by
 the band-slack constant delta_R^Z = 0.8539; the outlier set OUT is
 non-empty on part of the ladder (the lowest eigenvalue of M_h dips
 below the band edge c = 0.5523), so grouping GA has a negative term
 and GB's explicit remainder E_out is the honest reading; the
 reference-relative groupings GC/GD carry huge cancelling terms because
 the frozen band [c, L] is set by the DEEPEST rung while the surface
 spectra live far below L.
 SMOKE-3 (final, GREEN 35/35, 2.6 s) added three READ-ONLY reporting
 layers after SMOKE-2 disclosed the outlier set; no bar, tie, enum,
 screen or control was touched:
 (iv)  the STRUCTURAL CEILING.  If 1 - tr R = delta_R + (nonnegative
       carriers) holds on every rung then delta_R <= inf_h reserve(h).
       This is elementary and it DECIDES the mission's question by a
       single measured number, so it is printed as the headline next to
       the grouping census; the smoke value inf_h reserve < 0 was
       already implied by SMOKE-2's outlier reading.
 (v)   the CONDITIONAL census: the same groupings restricted to the
       rungs whose spectrum lies inside [c, L].
 (vi)  the second coefficient-only route (Weyl against each admissible
       reference) beside Gershgorin, and the per-rung threshold with
       the MEASURED in-band load beside the worst-case x_crit.
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
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob          # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol     # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul       # noqa: E402 (READ-ONLY)
import rhp_tier2_polecontrol_probe as t2       # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
NDIM = 8
SURF_EXP = 42
STEPS_EXP = 68
LU_TIE = 2.0e-9
SIM_TIE = 1.0e-9
DEC_TIE = 1.0e-12
SR_TIE = 1.0e-12
HV_TIE = 1.0e-10
REF_TIE = 1.0e-10
NONNEG_TOL = 1.0e-12
GRID_Z = 4001
REF_NODES = 4096
CTRL_RES_BAR = 1.0e-3
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
DEEP_SUB_MIN = 4
CB_F = float(ob.CB_CITED)
SCRAMBLE_SEED = ob.SCR_SEED
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
# AC1: identifiers that would make a "frozen" reference rung-dependent.
LADDER_IDS = ("build_rung", "ladder_zones", "assemble_step", "Mt",
              "step", "steps", "rung", "rows", "kz", "tau", "h",
              "lam_h", "jac")
# AC2: identifiers that would make the coefficient carrier
# read-derived or J_h-spectral.
READ_IDS = ("lu_read", "reserve", "trace_r", "trR", "q", "eigh",
            "eigvalsh", "lam_h", "w_h", "R_of", "margin")

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


trio = t2.trio
e3 = t2.e3
f4 = t2.f4
linfit = t2.linfit
complex_rel = t2.complex_rel
jacobi_matrix = t2.jacobi_matrix
jacobi_form = t2.jacobi_form
cf_arrays = t2.cf_arrays
lu_read = t2.lu_read
sym = t2.sym


def screen(values, scales, label):
    """CCXLVII relocation screen, bars inherited verbatim."""
    v = np.asarray(values, float)
    s = np.asarray(scales, float)
    pos = (v > 0.0) & (s > 0.0) & np.isfinite(v) & np.isfinite(s)
    if int(np.sum(pos)) < 3:
        return ("%s: VACUOUS(pos=%d)" % (label, int(np.sum(pos))),
                "VAC")
    slope, _2se, r2, _a = linfit(np.log(s[pos]), np.log(v[pos]))
    verd = ("PASS" if abs(slope) <= SLOPE_PASS
            else "RELOC" if slope >= SLOPE_RELOC else "AMBIG")
    return ("%s: %s(slope=%+.3f,R2=%.3f,%d excl)"
            % (label, verd, slope, r2, int(np.sum(~pos))), verd)


def ast_scan(banned):
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


def ast_scan_functions(names, banned):
    """Banned identifiers inside declared function bodies only."""
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.FunctionDef) and node.name in names:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Attribute):
                    nm = sub.attr
                if nm and nm in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


# ============================================ the frozen test function
class Filter:
    """The FROZEN CCXXV m=8 Zolotarev separator as a test function."""

    def __init__(self, poles, residues, c_value, l_value, delta_z):
        self.poles = np.asarray(poles, complex)
        self.res = np.asarray(residues, float)
        self.c = float(c_value)
        self.L = float(l_value)
        self.delta_z = float(delta_z)

    def value(self, x):
        """R(x) by partial fractions (the read's own representation)."""
        xx = np.asarray(x, float)
        out = np.ones(xx.shape, float)
        for a_j, z_j in zip(self.res, self.poles):
            out = out + 2.0 * a_j * np.real(1.0 / (xx - z_j))
        return out

    def scalar(self, x):
        return float(self.value(np.asarray([float(x)], float))[0])


def out_mask_of(lam, fil):
    """The GAP-OUTLIER set of a spectrum: the eigenvalues outside the
    separator's ONE-SIDED certified band [c, L]."""
    lam = np.asarray(lam, float)
    return (lam < fil.c) | (lam > fil.L)


def band_slack_constant(fil):
    """delta_R^Z = 1 - NDIM delta_Z: the frozen band-slack constant."""
    return 1.0 - NDIM * fil.delta_z


def sub_band_root(fil, target):
    """The unique root of R(x) = target in (0, c) (R decreases there)."""
    lo, hi = 0.0, fil.c
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if fil.scalar(mid) > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def sub_band_threshold(fil):
    """x_crit in (0, c): the root of R(x) = 1 - (NDIM-1) delta_Z.

    Below x_crit a SINGLE outlier eigenvalue can exhaust the whole
    reserve; above it the reserve stays positive whatever the other
    seven eigenvalues do inside the band."""
    return sub_band_root(fil, 1.0 - (NDIM - 1) * fil.delta_z)


# ================================================= frozen references
def arcsine_nodes(n_nodes, lo, hi):
    """Gauss-Chebyshev (arcsine) quadrature of [lo, hi]: EXACT for the
    arcsine measure -- equal weights at the Chebyshev points."""
    kk = np.arange(n_nodes, dtype=float)
    tt = np.cos(math.pi * (kk + 0.5) / n_nodes)
    mid = 0.5 * (hi + lo)
    half = 0.5 * (hi - lo)
    return mid + half * tt, np.full(n_nodes, 1.0 / n_nodes)


def chain_from_points(xs, ws, n_dim):
    """The n_dim x n_dim Jacobi data of a discrete measure."""
    al, be, _m0, n_ok = t2.pt.lanczos_chain(np.asarray(xs, float),
                                            np.asarray(ws, float),
                                            n_dim)
    if n_ok < n_dim:
        return None
    return np.asarray(be, float), np.asarray(al, float)


def ref_arcsine_unit():
    """AC1-SCANNED.  REF0: E4 arcsine on [-1,1], CCLIII verbatim."""
    a = np.full(NDIM - 1, 0.5)
    a[0] = 1.0 / math.sqrt(2.0)
    return a, np.zeros(NDIM)


def ref_arcsine_band(c_value, l_value):
    """AC1-SCANNED.  REFA: the affine image of REF0 on [c, L]."""
    a, b = ref_arcsine_unit()
    half = 0.5 * (l_value - c_value)
    mid = 0.5 * (l_value + c_value)
    return half * a, half * b + mid


def ref_log_band(c_value, l_value, n_nodes):
    """AC1-SCANNED.  REFB: the exp push-forward of the arcsine of
    [log c, log L] -- the geometric (Zolotarev-matched) reference."""
    tt, ww = arcsine_nodes(n_nodes, math.log(c_value),
                           math.log(l_value))
    return chain_from_points(np.exp(tt), ww, NDIM)


def filter_bands(fil, level, n_scan=200001):
    """The FROZEN finite-gap set of the separator itself:
    E(level) = {x in [c, L] : R(x) <= level}, a union of intervals
    (the separator equioscillates m times inside its band).  The edges
    are roots of the rational R and are bisected to machine
    precision."""
    grid = np.geomspace(fil.c, fil.L, n_scan)
    val = fil.value(grid) - level
    bands = []
    inside = val[0] <= 0.0
    left = fil.c if inside else None
    for i in range(1, n_scan):
        if (val[i] <= 0.0) == inside:
            continue
        lo, hi = grid[i - 1], grid[i]
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            if (fil.scalar(mid) - level <= 0.0) == inside:
                lo = mid
            else:
                hi = mid
        edge = math.sqrt(lo * hi)
        if inside:
            bands.append((left, edge))
        else:
            left = edge
        inside = not inside
    if inside and left is not None:
        bands.append((left, fil.L))
    return bands


def ref_filter_gapset(bands, n_nodes):
    """AC1-SCANNED.  REFC: the E3 FINITE-GAP reference -- the
    log-arcsine of [c, L] CONDITIONED on the separator's own band set
    (mass per band proportional to its logarithmic length, log-arcsine
    nodes inside each band: exact quadrature per band)."""
    if not bands:
        return None
    spans = [math.log(hi) - math.log(lo) for lo, hi in bands]
    total = math.fsum(spans)
    xs_all, ws_all = [], []
    per = max(8, n_nodes // max(len(bands), 1))
    for (lo, hi), span in zip(bands, spans):
        tt, ww = arcsine_nodes(per, math.log(lo), math.log(hi))
        xs_all.append(np.exp(tt))
        ws_all.append(ww * (span / total))
    return chain_from_points(np.concatenate(xs_all),
                            np.concatenate(ws_all), NDIM)


def spectral_data(a_off, b_diag):
    """Eigenvalues and the EIGHT normalized spectral measures (site
    weights) of a Jacobi matrix."""
    jm = jacobi_matrix(a_off, b_diag)
    lam, vec = np.linalg.eigh(jm)
    return jm, np.asarray(lam, float), np.asarray(vec ** 2, float)


def build_references(fil):
    section("X -- THE FROZEN REFERENCES (filter geometry only; "
            "h-independent by AC1)")
    bands = filter_bands(fil, 0.5 * fil.delta_z)
    print("    the separator's own FINITE-GAP set E = {x in [c, L] : "
          "R(x) <= delta_Z/2}: %d bands, %d gaps" % (len(bands),
                                                     len(bands) - 1))
    for lo, hi in bands:
        print("      band [%14.6f, %14.6f]  (log-length %.4f)"
              % (lo, hi, math.log(hi) - math.log(lo)))
    refs = []
    specs = [("REF0", "arcsine [-1,1] (CCLIII verbatim, E4)",
              ref_arcsine_unit()),
             ("REFA", "arcsine on the filter band [c, L]",
              ref_arcsine_band(fil.c, fil.L)),
             ("REFB", "log-arcsine on [c, L] (exp push-forward)",
              ref_log_band(fil.c, fil.L, REF_NODES)),
             ("REFC", "finite-gap: log-arcsine | E (E3/DKS class)",
              ref_filter_gapset(bands, REF_NODES))]
    dbl_dev = 0.0
    for name, note, data in specs:
        if data is None:
            check("X0 reference %s could not be built" % name, False,
                  kill="K1")
            continue
        a_off, b_diag = data
        jm, lam, wgt = spectral_data(a_off, b_diag)
        r_vals = fil.value(lam)
        tr_r = float(np.sum(r_vals))
        in_band = int(np.sum((lam >= fil.c) & (lam <= fil.L)))
        refs.append(dict(name=name, note=note, a=a_off, b=b_diag,
                         J=jm, lam=lam, w=wgt, r=r_vals,
                         trR=tr_r, delta_R=1.0 - tr_r,
                         in_band=in_band))
        print("    %-5s %-46s delta_R = %+10.6f  (tr R = %.6e, "
              "in-band %d/%d)" % (name, note, 1.0 - tr_r, tr_r,
                                  in_band, NDIM))
        print("          spectrum %s"
              % " ".join("%.5g" % v for v in lam))
    for name, data1, data2 in (
            ("REFB", ref_log_band(fil.c, fil.L, REF_NODES),
             ref_log_band(fil.c, fil.L, 2 * REF_NODES)),
            ("REFC", ref_filter_gapset(bands, REF_NODES),
             ref_filter_gapset(bands, 2 * REF_NODES))):
        if data1 is None or data2 is None:
            continue
        dev = max(float(np.max(np.abs(data1[0] - data2[0])
                               / np.maximum(1.0, np.abs(data2[0])))),
                  float(np.max(np.abs(data1[1] - data2[1])
                               / np.maximum(1.0, np.abs(data2[1])))))
        dbl_dev = max(dbl_dev, dev)
    check("X1 quadrature-built references converged under node "
          "doubling (%d -> %d): max rel dev %.2e <= %.0e"
          % (REF_NODES, 2 * REF_NODES, dbl_dev, REF_TIE),
          dbl_dev <= REF_TIE, kill="K2")
    void = [r["name"] for r in refs if r["delta_R"] <= 0.0]
    print("    REF-VOID (delta_R <= 0, excluded from the grouping "
          "census, number still printed): %s" % (",".join(void)
                                                 or "none"))
    check("X2 at least one reference is admissible (delta_R > 0)",
          any(r["delta_R"] > 0.0 for r in refs), kill="K1")
    return refs


# ================================================ the wall/read layer
def build_ladder():
    section("W -- the CCVII/CCXXV wall ladder, rebuilt read-only")
    zones = ob.ladder_zones()
    check("W1 surface rung census %d == %d" % (len(zones), SURF_EXP),
          len(zones) == SURF_EXP, kill="K1")
    if SMOKE:
        zones = zones[:10]
        print("    SMOKE: %d contiguous surface rungs" % len(zones))
    surface = [ob.build_rung("surf", kz, with_split=False)
               for kz in zones]
    check("W2 all surface chains complete",
          all(r is not None for r in surface), kill="K1")
    ob.build_ext_tables()
    census = sorted(ob.deep_zone_census(), key=lambda p: (p[1], p[0]))
    if SMOKE:
        census = census[:3]
    deep = []
    for kz, hz in census:
        rung = ob.build_rung("deep", kz, with_split=False)
        if rung is not None:
            deep.append(rung)
        print("    deep kz %-4d h %-5d %s [%.1f s]"
              % (kz, hz, "OK" if rung is not None else "SHORT",
                 time.time() - T0), flush=True)
    deep_ok = [r for r in deep
               if r["core_ok"] and r["negA"] == 0
               and r.get("lamS", -1.0) > 0.0]
    combined = sorted([r for r in surface
                       if r is not None and r["core_ok"]] + deep_ok,
                      key=lambda r: (r["h"], r["kz"]))
    steps = ob.make_steps(combined)
    for st in steps:
        zol.assemble_step(st)
    steps = [st for st in steps if st["status"] == "OK"]
    segs = [ob.seg_of(st) for st in steps]
    ok = (SMOKE or (len(steps) == STEPS_EXP
                    and segs.count("surf") == 40
                    and segs.count("bridge") == 1
                    and segs.count("deep") == 27))
    check("W3 combined steps %d = surface %d + bridge %d + deep %d"
          % (len(steps), segs.count("surf"), segs.count("bridge"),
             segs.count("deep")), ok, kill="K1")
    return zones, steps


def get_filter(steps, artifact):
    poles_art = np.asarray([complex(*p)
                            for p in artifact["filter"]["poles"]],
                           complex)
    res_art = np.asarray(artifact["filter"]["residues"], float)
    global_l = max(st["L_src"] for st in steps)
    if SMOKE:
        check("T1 SMOKE: fixed CCXXV filter taken from the stored "
              "artifact (a subset ladder cannot reproduce global L)",
              True)
        fd = zol.build_filter(CB_F, float(artifact["filter"]["L"]),
                              NDIM)
        return Filter(poles_art, res_art, CB_F,
                      float(artifact["filter"]["L"]), fd["delta"])
    fd = zol.build_filter(CB_F, global_l, NDIM)
    dev_l = abs(global_l - float(artifact["filter"]["L"])) \
        / max(1.0, abs(global_l))
    dev_p = float(np.max(np.abs(fd["poles"] - poles_art)
                         / np.maximum(1.0, np.abs(poles_art))))
    dev_r = float(np.max(np.abs(fd["residues"] - res_art)
                         / np.maximum(1.0, np.abs(res_art))))
    check("T1 fixed CCXXV GLOBAL m=8 filter rebuilt from source-only "
          "L: L rel %.2e, poles %.2e, residues %.2e <= %.0e"
          % (dev_l, dev_p, dev_r, LU_TIE),
          (artifact["filter"]["m"] == NDIM and dev_l <= LU_TIE
           and dev_p <= LU_TIE and dev_r <= LU_TIE), kill="K2")
    return Filter(fd["poles"], fd["residues"], CB_F, global_l,
                  fd["delta"])


def filter_wards(fil):
    section("Z -- THE FROZEN TEST FUNCTION: the Zolotarev separator as "
            "the sum rule's test function")
    fd = zol.build_filter(fil.c, fil.L, NDIM)
    grid_band = np.geomspace(fil.c, fil.L, GRID_Z)
    dev_pf = max(abs(fil.scalar(x) - zol.scalar_r(fd, x))
                 for x in grid_band[::37])
    check("Z1 WARD partial fractions == zol.scalar_r on %d band "
          "points: max dev %.2e <= %.0e"
          % (len(grid_band[::37]), dev_pf, DEC_TIE),
          dev_pf <= DEC_TIE, kill="K2")
    r_band = fil.value(grid_band)
    r_neg = fil.value(-grid_band)
    grid_all = np.concatenate([
        np.linspace(0.0, fil.c, GRID_Z),
        np.geomspace(fil.c, fil.L, GRID_Z)])
    r_all = np.concatenate([fil.value(grid_all),
                            fil.value(-grid_all)])
    anti_dev = float(np.max(np.abs(r_band + r_neg - 2.0)))
    check("Z2 WARD E5 filter facts, ONE-SIDED: R(0) = %.15f; the "
          "point antisymmetry R(-x) = 2 - R(x) holds to %.2e (the "
          "separator is NOT even -- z_j = i y_j gives the odd kernel "
          "x/(x^2+y^2)); 0 <= R <= delta_Z = %.6e on the POSITIVE "
          "band [c, L] (grid max %.6e); 0 <= R <= 2 on [-L, L] (grid "
          "min %.3e, max %.6f)"
          % (fil.scalar(0.0), anti_dev, fil.delta_z,
             float(np.max(r_band)), float(np.min(r_all)),
             float(np.max(r_all))),
          (abs(fil.scalar(0.0) - 1.0) <= DEC_TIE
           and anti_dev <= DEC_TIE
           and float(np.max(r_band)) <= fil.delta_z
           and float(np.min(r_band)) >= -DEC_TIE
           and float(np.min(r_all)) >= -DEC_TIE
           and float(np.max(r_all)) <= 2.0 + DEC_TIE), kill="K2")
    d_z = band_slack_constant(fil)
    x_c = sub_band_threshold(fil)
    print("    THE THREE FROZEN CONSTANTS OF THE FILTER:")
    print("      delta_Z          = %.10e   (equioscillation level, "
          "interval-certified in CCXXV)" % fil.delta_z)
    print("      delta_R^Z        = %.10f   = 1 - %d delta_Z  (the "
          "band-slack constant of the sum rule)" % (d_z, NDIM))
    print("      x_crit           = %.10e   (R(x_crit) = 1 - %d "
          "delta_Z = %.6f; below it ONE outlier can exhaust the "
          "reserve)" % (x_c, NDIM - 1, 1.0 - (NDIM - 1) * fil.delta_z))
    print("      band [c, L]      = [%.6f, %.6f]" % (fil.c, fil.L))
    check("Z3 the band-slack constant is POSITIVE: delta_R^Z = %.6f "
          "> 0 and x_crit = %.4e < c = %.4f"
          % (d_z, x_c, fil.c), d_z > 0.0 and 0.0 < x_c < fil.c,
          kill="K2")
    return d_z, x_c


def translation(steps, artifact, fil):
    section("T -- shifted tau translation, LU only, warded against "
            "the stored 68x8 CCXLVII artifact")
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]), int(r["kz"])):
              r for r in artifact["rungs"]}
    rows = []
    d_det = d_ph = d_tr = d_expr = d_marg = 0.0
    for idx, st in enumerate(steps):
        key = (int(st["r1"]["h"]), int(st["r1"]["kz"]),
               int(st["r2"]["h"]), int(st["r2"]["kz"]))
        src = stored.get(key)
        pole_rows = []
        contribs = []
        for j, (pole, resid) in enumerate(zip(fil.poles, fil.res)):
            rd = lu_read(st["Mt"], pole)
            contribs.append(2.0 * float(resid) * rd["tr"].real)
            if src is not None:
                sp = src["poles"][j]
                d_det = max(d_det, complex_rel(
                    rd["det"], complex(*sp["determinant"])))
                d_ph = max(d_ph, abs(t2.wrap(rd["phase"]
                                             - sp["phase"])))
                d_tr = max(d_tr, complex_rel(
                    rd["tr"], complex(*sp["resolvent_trace"])))
            pole_rows.append(dict(j=j, pole=pole, y=float(pole.imag),
                                  residue=float(resid), read=rd))
        trace_r = NDIM + math.fsum(contribs)
        reserve = 1.0 - trace_r
        if src is not None:
            d_expr = max(d_expr, abs(trace_r - float(src["trace_R"])))
            d_marg = max(d_marg, abs(reserve - float(src["margin"])))
        rows.append(dict(index=idx, step=st, seg=ob.seg_of(st),
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         gap=float(st["gap"]), trace_r=trace_r,
                         reserve=reserve, contribs=contribs,
                         poles=pole_rows, matched=src is not None))
    n_match = sum(1 for r in rows if r["matched"])
    check("T2 LU det/phase/trace reproduce the stored artifact on "
          "%d matched steps x 8: det %.2e, phase %.2e, trace %.2e "
          "<= %.0e" % (n_match, d_det, d_ph, d_tr, LU_TIE),
          n_match >= 1 and d_det <= LU_TIE and d_ph <= LU_TIE
          and d_tr <= LU_TIE and (SMOKE or n_match == STEPS_EXP),
          kill="K3")
    check("T3 partial fractions reproduce stored trace_R / margin: "
          "%.2e / %.2e <= %.0e" % (d_expr, d_marg, LU_TIE),
          d_expr <= LU_TIE and d_marg <= LU_TIE, kill="K3")
    print("    reserve = 1 - tr R level min/med/max %s"
          % e3([r["reserve"] for r in rows]))
    return rows


# ============================================ the Jacobi / spectral layer
def jacobi_layer(rows, fil):
    section("J -- THE JACOBI / SPECTRAL LAYER: J_h, its eight "
            "normalized spectral measures, and the finite canonical "
            "factorization")
    d_orth = d_sim = d_sr = d_site = d_hv = 0.0
    n_bad = 0
    for row in rows:
        jf = jacobi_form(row["step"]["Mt"])
        if jf is None:
            n_bad += 1
            row["jac"] = None
            continue
        a_off, b_diag, qq = jf
        jm, lam, wgt = spectral_data(a_off, b_diag)
        scale = max(1.0, float(np.max(np.abs(row["step"]["Mt"]))))
        d_orth = max(d_orth, float(np.max(np.abs(
            qq.T @ qq - np.eye(NDIM)))))
        d_sim = max(d_sim, float(np.max(np.abs(
            qq.T @ row["step"]["Mt"] @ qq - jm))) / scale)
        r_vals = fil.value(lam)
        tr_spec = float(np.sum(r_vals))
        d_sr = max(d_sr, abs(tr_spec - row["trace_r"]))
        site = float(np.sum(wgt * r_vals[None, :]))
        d_site = max(d_site, abs(site - row["trace_r"]))
        d_site = max(d_site, float(np.max(np.abs(
            np.sum(wgt, axis=1) - 1.0))))
        lhs = 2.0 * float(np.sum(
            (NDIM - np.arange(1, NDIM)) * np.log(a_off)))
        vdm = 0.0
        for k in range(NDIM):
            for l_idx in range(k + 1, NDIM):
                vdm += 2.0 * math.log(abs(lam[l_idx] - lam[k]))
        rhs = float(np.sum(np.log(wgt[0]))) + vdm
        d_hv = max(d_hv, abs(lhs - rhs) / max(1.0, abs(lhs)))
        row["jac"] = (a_off, b_diag)
        row["J"] = jm
        row["lam"] = lam
        row["w"] = wgt
        row["r"] = r_vals
    check("J0 Lanczos form of (M_h, e_0) exists on all %d steps"
          % len(rows), n_bad == 0, "breakdowns %d" % n_bad, kill="K2")
    check("J1 WARD similarity Q^T Q = I and Q^T M_h Q = J(a,b): "
          "%.2e / %.2e <= %.0e" % (d_orth, d_sim, SIM_TIE),
          d_orth <= SIM_TIE and d_sim <= SIM_TIE, kill="K2")
    check("J2 WARD spectral form of the reserve: tr R(J_h) = "
          "sum_k R(lambda_k) == partial-fraction LU read: max dev "
          "%.2e <= %.0e" % (d_sr, SR_TIE), d_sr <= SR_TIE, kill="K2")
    check("J3 WARD site form: tr R(J_h) = sum_s int R dmu_h^(s) with "
          "every mu_h^(s) a probability measure: max dev %.2e <= %.0e"
          % (d_site, SR_TIE), d_site <= SR_TIE, kill="K2")
    check("J4 WARD E6 Hankel-Vandermonde identity at dimension 8 "
          "(COEFFICIENTS = ENTROPY + CONFIGURATION): "
          "sum_n 2(8-n) log a_n == sum_k log w_k^(0) + 2 sum_{k<l} "
          "log|lam_k - lam_l|: max rel %.2e <= %.0e"
          % (d_hv, HV_TIE), d_hv <= HV_TIE, kill="K2")
    lam_min = np.asarray([float(np.min(r["lam"])) for r in rows],
                         float)
    lam_max = np.asarray([float(np.max(r["lam"])) for r in rows],
                         float)
    n_neg = int(np.sum([int(np.any(r["lam"] <= 0.0)) for r in rows]))
    n_out = np.asarray([int(np.sum(out_mask_of(r["lam"], fil)))
                        for r in rows], int)
    print("    lambda_min over the ladder: %s   (band edge c = %.4f)"
          % (e3(lam_min), fil.c))
    print("    lambda_max over the ladder: %s   (band edge L = %.4f)"
          % (e3(lam_max), fil.L))
    print("    rungs with a non-positive eigenvalue (the separator is "
          "one-sided, so those would read R ~ 2): %d/%d"
          % (n_neg, len(rows)))
    print("    OUTLIER census: rungs with at least one eigenvalue "
          "outside [c, L]: %d/%d; outliers per rung min/med/max "
          "%d/%d/%d" % (int(np.sum(n_out > 0)), len(rows),
                        int(np.min(n_out)), int(np.median(n_out)),
                        int(np.max(n_out))))
    return n_out


# ==================================================== the decomposition
def coef_part(a_off, b_diag, ref, poles, residues):
    """AC2-SCANNED.  The COEFFICIENT carrier: the EXACT first-order
    response of the resolvent trace in the JACOBI DATA difference,
    contracted with the FROZEN reference resolvent.  No eigenvalue, no
    resolvent and no read of the perturbed object enters."""
    delta_j = jacobi_matrix(np.asarray(a_off, float),
                            np.asarray(b_diag, float)) - ref["J"]
    out = []
    for pole in poles:
        r_star = np.linalg.inv(ref["J"] - pole * np.eye(NDIM,
                                                        dtype=complex))
        out.append(-complex(np.trace(r_star @ delta_j @ r_star)))
    return np.asarray(out, complex)


def decomposition(rows, refs, fil):
    section("D -- THE DECOMPOSITION: canonical factorization of the "
            "high-pole reads at fixed dimension 8 (all rational, all "
            "exact)")
    ok_refs = [r for r in refs if r["delta_R"] > 0.0]
    d_pd = d_m = d_tr = 0.0
    n_cell = 0
    for row in rows:
        if row.get("jac") is None:
            continue
        lam = row["lam"]
        wgt = row["w"]
        row["dec"] = {}
        for ref in refs:
            lam_s = ref["lam"]
            w_s = ref["w"]
            out_mask = out_mask_of(lam, fil)
            cf = coef_part(row["jac"][0], row["jac"][1], ref,
                           fil.poles, fil.res)
            per_pole = []
            for jj, pr in enumerate(row["poles"]):
                z = pr["pole"]
                # --- D1 perturbation determinant, two routes
                tr_h = complex(np.sum(1.0 / (lam - z)))
                tr_s = complex(np.sum(1.0 / (lam_s - z)))
                pd_route = tr_h - tr_s
                lu_route = pr["read"]["tr"] - tr_s
                d_pd = max(d_pd, complex_rel(pd_route, lu_route))
                # --- D2 the canonical split of the m-function
                disp = 1.0 / (lam - z) - 1.0 / (lam_s - z)
                l_gap = complex(np.sum(w_s[0][out_mask]
                                       * disp[out_mask]))
                l_coef = complex(np.sum(w_s[0][~out_mask]
                                        * disp[~out_mask]))
                l_spread = complex(np.sum((wgt[0] - w_s[0])
                                          / (lam - z)))
                m_h = pr["read"]["m00"]
                m_s = complex(np.sum(w_s[0] / (lam_s - z)))
                d_m = max(d_m, complex_rel(l_gap + l_coef + l_spread,
                                           m_h - m_s))
                # --- D3 the same split at the TRACE level
                t_gap = complex(np.sum(np.sum(w_s, axis=0)[out_mask]
                                       * disp[out_mask]))
                t_coef = complex(np.sum(np.sum(w_s, axis=0)[~out_mask]
                                        * disp[~out_mask]))
                t_spread = complex(np.sum(
                    np.sum(wgt - w_s, axis=0) / (lam - z)))
                d_tr = max(d_tr, complex_rel(t_gap + t_coef + t_spread,
                                             tr_h - tr_s))
                per_pole.append(dict(l_gap=l_gap, l_coef=l_coef,
                                     l_spread=l_spread,
                                     t_gap=t_gap, t_coef=t_coef,
                                     t_spread=t_spread,
                                     coef_lin=cf[jj],
                                     disp_out=complex(np.sum(
                                         disp[out_mask])),
                                     disp_all=complex(np.sum(disp))))
                n_cell += 1
            row["dec"][ref["name"]] = dict(per_pole=per_pole,
                                           out_mask=out_mask)
    check("D1 WARD perturbation determinant: -d/dz log D_h(z_j) = "
          "tr[(J_h-z_j)^{-1} - (J_*-z_j)^{-1}] on %d cells (eigenvalue "
          "route vs LU route): max rel %.2e <= %.0e"
          % (n_cell, d_pd, DEC_TIE), d_pd <= DEC_TIE, kill="K2")
    check("D2 WARD canonical factorization per rung per pole: "
          "m_h(z_j) - m_*(z_j) = L_gap + L_coef + L_spread (Blaschke "
          "displacement at frozen weights + outer weight transport): "
          "max rel %.2e <= %.0e" % (d_m, DEC_TIE), d_m <= DEC_TIE,
          kill="K2")
    check("D3 WARD the same split at the TRACE level (the level the "
          "reserve lives on): max rel %.2e <= %.0e"
          % (d_tr, DEC_TIE), d_tr <= DEC_TIE, kill="K2")
    print("    references carried through the decomposition: %s "
          "(admissible: %s)"
          % (",".join(r["name"] for r in refs),
             ",".join(r["name"] for r in ok_refs) or "none"))
    return ok_refs


# ================================================ the sum-rule search
def grouping_values(row, fil, d_r_z, ref=None, kind="GA"):
    """The four DECLARED groupings.  Each returns
    (delta_R, Q_R, G_R, H_R, extra) and is an EXACT identity."""
    lam = row["lam"]
    r_vals = row["r"]
    slack = fil.delta_z - r_vals
    if kind in ("GA", "GB"):
        q_r = float(np.sum(np.maximum(slack, 0.0)))
        e_out = float(np.sum(np.maximum(-slack, 0.0)))
        return (d_r_z, q_r, -e_out, 0.0, dict(e_out=e_out))
    lam_s = ref["lam"]
    r_s = ref["r"]
    out_mask = out_mask_of(lam, fil)
    if kind == "GC":
        w_tot = np.sum(row["w"], axis=0)
        ws_tot = np.sum(ref["w"], axis=0)
        disp = r_vals - r_s
        q_r = -float(np.sum(ws_tot[~out_mask] * disp[~out_mask]))
        g_r = -float(np.sum(ws_tot[out_mask] * disp[out_mask]))
        h_r = -float(np.sum((w_tot - ws_tot) * r_vals))
        return (ref["delta_R"], q_r, g_r, h_r, dict())
    # GD: the coefficient-linear grouping
    dec = row["dec"][ref["name"]]
    q_r = -math.fsum([2.0 * pr["residue"]
                      * dec["per_pole"][jj]["coef_lin"].real
                      for jj, pr in enumerate(row["poles"])])
    g_r = -math.fsum([2.0 * pr["residue"]
                      * dec["per_pole"][jj]["disp_out"].real
                      for jj, pr in enumerate(row["poles"])])
    tot = -math.fsum([2.0 * pr["residue"]
                      * dec["per_pole"][jj]["disp_all"].real
                      for jj, pr in enumerate(row["poles"])])
    return (ref["delta_R"], q_r, g_r, tot - q_r - g_r, dict())


def sumrule_search(rows, refs, fil, d_z, x_c):
    section("S -- THE SUM-RULE SEARCH: 1 - tr R(J_h) = delta_R + Q_R "
            "+ G_R + H_R with delta_R > 0 constant -- does a "
            "NONNEGATIVE grouping exist?")
    live = [r for r in rows if r.get("jac") is not None]
    cands = [("GA", None, "BAND-SLACK (filter only, reference-free)"),
             ("GB", None, "BAND-SLACK + EXPLICIT REMAINDER E_out")]
    for ref in refs:
        if ref["delta_R"] > 0.0:
            cands.append(("GC", ref, "REF-SPECTRAL vs %s"
                          % ref["name"]))
            cands.append(("GD", ref, "REF-LINEAR (coefficient-linear) "
                          "vs %s" % ref["name"]))
    results = []
    d_id = 0.0
    print("\n    %-4s %-42s %10s %14s %14s %14s  %8s"
          % ("grp", "grouping", "delta_R", "Q_R med", "G_R med",
             "H_R med", "all>=0"))
    for kind, ref, note in cands:
        vals = []
        for row in live:
            d_r, q_r, g_r, h_r, extra = grouping_values(
                row, fil, d_z, ref=ref, kind=kind)
            d_id = max(d_id, abs(d_r + q_r + g_r + h_r
                                 - row["reserve"]))
            vals.append((d_r, q_r, g_r, h_r, extra, row))
        q_a = np.asarray([v[1] for v in vals], float)
        g_a = np.asarray([v[2] for v in vals], float)
        h_a = np.asarray([v[3] for v in vals], float)
        d_r0 = vals[0][0]
        allpos = ((q_a >= -NONNEG_TOL) & (g_a >= -NONNEG_TOL)
                  & (h_a >= -NONNEG_TOL))
        neg_terms = [nm for nm, arr in (("Q_R", q_a), ("G_R", g_a),
                                        ("H_R", h_a))
                     if float(np.min(arr)) < -NONNEG_TOL]
        results.append(dict(kind=kind, ref=ref, note=note,
                            delta_R=d_r0, q=q_a, g=g_a, h=h_a,
                            allpos=allpos, neg=neg_terms,
                            vals=vals))
        print("    %-4s %-42s %+10.5f %14.5e %14.5e %14.5e  %4d/%-4d"
              % (kind, note, d_r0, float(np.median(q_a)),
                 float(np.median(g_a)), float(np.median(h_a)),
                 int(np.sum(allpos)), len(vals)))
    check("S1 WARD every declared grouping is an EXACT identity for "
          "the reserve on all %d rungs: max dev %.2e <= %.0e"
          % (len(live), d_id, SR_TIE), d_id <= SR_TIE, kill="K2")

    # ---- the STRUCTURAL CEILING: an elementary but decisive no-go
    floor = float(np.min([r["reserve"] for r in live]))
    arg_floor = min(live, key=lambda r: r["reserve"])
    print("\n    STRUCTURAL CEILING (elementary, decisive): if "
          "1 - tr R = delta_R + (nonnegative carriers) holds on every "
          "rung, then delta_R <= inf_h reserve(h) = %.6e (attained at "
          "h = %d, lambda_min = %.6e)."
          % (floor, int(arg_floor["h"]), float(np.min(
              arg_floor["lam"]))))
    print("      Hence NO filter-constant delta_R above that floor can "
          "carry a fully nonnegative sum rule: the band-slack constant "
          "delta_R^Z = %.6f exceeds the floor by %.4e, so a negative "
          "term (the sub-band remainder) is FORCED on the floor rung. "
          "The content of any such sum rule is exactly a LOWER BOUND "
          "on the reserve." % (d_z, d_z - floor))

    print("\n    per-term detail (min / med / max over the ladder):")
    for res in results:
        print("      %-4s %-34s Q %s" % (res["kind"], res["note"][:34],
                                         e3(res["q"])))
        print("           %-34s G %s" % ("", e3(res["g"])))
        print("           %-34s H %s" % ("", e3(res["h"])))
        print("           negative terms: %s"
              % (",".join(res["neg"]) or "none"))

    # ---- the CONDITIONAL census: the rungs whose spectrum IS included
    incl = np.asarray([int(np.sum(out_mask_of(r["lam"], fil))) == 0
                       for r in live], bool)
    n_incl = int(np.sum(incl))
    cond = []
    for res in results:
        if res["delta_R"] > 0.0 and n_incl > 0 \
                and int(np.sum(res["allpos"][incl])) == n_incl:
            cond.append(res)
    print("      the INCLUSION sub-census (spectrum(M_h) inside "
          "[c, L]) has %d/%d rungs; groupings that are FULLY "
          "NONNEGATIVE there with delta_R > 0: %s"
          % (n_incl, len(live),
             ",".join("%s/%s" % (r["kind"], r["ref"]["name"]
                                 if r["ref"] else "free")
                      for r in cond) or "none"))

    # ---- the winner search, in the declared order of strength
    winner = None
    for res in results:
        if res["delta_R"] > 0.0 and int(np.sum(res["allpos"])) \
                == len(res["allpos"]):
            winner = res
            break
    remainder = None
    if winner is None:
        for res in results:
            if res["delta_R"] > 0.0 and len(res["neg"]) == 1:
                arr = {"Q_R": res["q"], "G_R": res["g"],
                       "H_R": res["h"]}[res["neg"][0]]
                if remainder is None or float(np.max(-arr)) \
                        < float(np.max(-remainder[1])):
                    remainder = (res, arr)
    if winner is not None:
        verdict = "SUMRULE-POSITIVE(%s, delta_R = %+.6f)" \
            % (winner["kind"], winner["delta_R"])
    elif remainder is not None:
        res, arr = remainder
        neg = res["neg"][0]
        supp = int(np.sum(arr < -NONNEG_TOL))
        verdict = ("SUMRULE-POSITIVE-WITH-REMAINDER(%s, delta_R = "
                   "%+.6f, remainder %s: |%s| max %.4e on %d/%d "
                   "rungs, reserve floor %+.6f)"
                   % (res["kind"], res["delta_R"], neg, neg,
                      float(np.max(-arr)), supp, len(arr),
                      float(np.min([v[0] + v[1] + v[2] + v[3]
                                    for v in res["vals"]]))))
    else:
        worst = min((res for res in results if res["delta_R"] > 0.0),
                    key=lambda r: len(r["neg"]))
        verdict = ("SUMRULE-OBSTRUCTED(best %s, negative terms %s, "
                   "worst size %.4e)"
                   % (worst["kind"], ",".join(worst["neg"]),
                      max(float(np.max(-worst["q"])),
                          float(np.max(-worst["g"])),
                          float(np.max(-worst["h"])))))
    ceil_lab = ("CEILING(inf_h reserve = %+.6e %s 0: %s)"
                % (floor, "<=" if floor <= 0.0 else ">",
                   "NO positive-constant nonnegative sum rule exists "
                   "for the frozen filter on this ladder -- the "
                   "remainder is FORCED" if floor <= 0.0 else
                   "the largest admissible constant is exactly that "
                   "floor"))
    if cond:
        verdict = ("%s + SUMRULE-POSITIVE-CONDITIONAL(%s on the "
                   "inclusion sub-census %d/%d rungs, delta_R = "
                   "%+.6f)" % (verdict, cond[0]["kind"], n_incl,
                               len(live), cond[0]["delta_R"]))
    print("\n    SUM-RULE VERDICT: %s" % verdict)
    print("    %s" % ceil_lab)
    verdict = "%s ; %s" % (verdict, ceil_lab)

    # ---- the quantitative content of the winning band-slack form
    ga = results[0]
    e_out = np.asarray([v[4]["e_out"] for v in ga["vals"]], float)
    lam_min = np.asarray([float(np.min(v[5]["lam"]))
                          for v in ga["vals"]], float)
    margin = d_z + ga["q"] - e_out
    n_exh = int(np.sum(margin <= 0.0))
    worst = int(np.argmin(margin))
    print("    BAND-SLACK CONTENT (the reduction, not a proof):")
    print("      delta_R^Z = %.6f (frozen); Q_R (in-band slack, "
          "<= %d delta_Z = %.6f) %s"
          % (d_z, NDIM, NDIM * fil.delta_z, e3(ga["q"])))
    print("      E_out (the explicit remainder, supported on the "
          "sub-band eigenvalues) %s; support %d/%d rungs"
          % (e3(e_out), int(np.sum(e_out > NONNEG_TOL)), len(e_out)))
    print("      lambda_min per rung %s vs the frozen threshold "
          "x_crit = %.6e: rungs below x_crit %d/%d"
          % (e3(lam_min), x_c, int(np.sum(lam_min < x_c)),
             len(lam_min)))
    print("      reserve margin delta_R^Z + Q_R - E_out: %s; "
          "exhausted rungs %d/%d; closest call at rung index %d "
          "(h = %d, lambda_min = %.6e, margin = %.6e)"
          % (e3(margin), n_exh, len(margin), worst,
             int(ga["vals"][worst][5]["h"]), lam_min[worst],
             margin[worst]))
    rest = np.asarray([float(np.sum(np.sort(v[5]["r"])[:-1]))
                       for v in ga["vals"]], float)
    x_meas = np.asarray([sub_band_root(fil, 1.0 - other)
                         for other in rest], float)
    print("      SUFFICIENT CONDITION (frozen, one line): if every "
          "eigenvalue of M_h lies in [c, L] the reserve is >= "
          "delta_R^Z = %.6f; if exactly one leaves the band it "
          "suffices that lambda_min > x_crit = %.6e; the frozen "
          "condition covers %d/%d rungs."
          % (d_z, x_c, int(np.sum(lam_min > x_c)), len(lam_min)))
    print("      the same condition with the MEASURED in-band load "
          "(sum of the seven largest R(lambda_k)) instead of the "
          "worst-case 7 delta_Z: load %s, per-rung threshold %s -- "
          "covers %d/%d rungs"
          % (e3(rest), e3(x_meas), int(np.sum(lam_min > x_meas)),
             len(lam_min)))
    print("      => the certificate REDUCES to a spectral-inclusion / "
          "lambda_min statement; the open piece is a COEFFICIENT-SIDE "
          "(KS / Lieb-Thirring) lower bound on lambda_min, not a norm "
          "bound on the reads.")
    return results, verdict, e_out, margin


def entropy_hull(rows, refs, fil):
    section("E -- THE ENTROPY CARRIER: where the relative spectral "
            "entropy can and cannot live")
    live = [r for r in rows if r.get("jac") is not None]
    zero_dev = 0.0
    for row in live:
        zero_dev = max(zero_dev, float(np.max(np.abs(
            np.sum(row["w"], axis=0) - 1.0))))
    check("E0 WARD the TRACE-level transport carrier is IDENTICALLY "
          "ZERO: sum_s |<e_s, v_k>|^2 = 1 for every k (max dev %.2e "
          "<= %.0e), so H_R vanishes in ANY reference-relative trace "
          "grouping -- the reserve is a PURE EIGENVALUE FUNCTIONAL and "
          "a Case sum rule for it carries NO entropy term"
          % (zero_dev, SR_TIE), zero_dev <= SR_TIE, kill="K2")
    out = {}
    for ref in refs:
        if ref["delta_R"] <= 0.0:
            continue
        kls, hulls, hs, sound = [], [], [], 0
        for row in live:
            p = np.maximum(row["w"][0], 1e-300)
            q = np.maximum(ref["w"][0], 1e-300)
            kl_s = float(np.sum(p * np.log(p / q)))
            # the site-0 transport carrier of the m-function read,
            # summed over the eight poles with the filter residues
            trans = 0.0
            for jj, pr in enumerate(row["poles"]):
                trans += 2.0 * pr["residue"] * float(np.real(np.sum(
                    (row["w"][0] - ref["w"][0]) / (row["lam"]
                                                   - pr["pole"]))))
            hull = float(np.max(np.abs(row["r"]))) \
                * math.sqrt(2.0 * max(kl_s, 0.0))
            kls.append(kl_s)
            hulls.append(hull)
            hs.append(abs(trans))
            sound += int(kl_s >= -SR_TIE)
        ratio = np.asarray(hulls, float) \
            / np.maximum(np.asarray(hs, float), 1e-300)
        out[ref["name"]] = dict(kl=np.asarray(kls, float),
                                hull=np.asarray(hulls, float),
                                h=np.asarray(hs, float),
                                sound=sound, n=len(kls))
        check("E1.%s the site-0 relative spectral entropy is "
              "nonnegative (Gibbs) on %d/%d rungs: KL med %.4e; the "
              "m-function transport carrier |L_spread| (filter-summed) "
              "med %.4e; Pinsker hull / carrier med %.3e"
              % (ref["name"], sound, len(kls), float(np.median(kls)),
                 float(np.median(hs)), float(np.median(ratio))),
              sound == len(kls), kill="K2")
    print("    READING: the entropy carrier exists at the level of the "
          "SITE m-function (CCXLVII's kernel G_00) but cancels exactly "
          "in the trace; the reserve therefore admits no entropy term "
          "and the KS template's third slot is EMPTY for this test "
          "function.")
    return out


def coefficient_side_bound(rows, refs, fil, x_c):
    """The open piece, measured: how far is a COEFFICIENT-ONLY lower
    bound on lambda_min from the truth?  Two rigorous routes, both
    built from the Jacobi data alone: Gershgorin on the Jacobi form
    (reference-free) and Weyl against each frozen reference."""
    section("B -- THE OPEN PIECE, MEASURED: coefficient-only lower "
            "bounds on lambda_min against the truth")
    live = [r for r in rows if r.get("jac") is not None]
    lam_min = np.asarray([float(np.min(r["lam"])) for r in live],
                         float)
    gersh = []
    for row in live:
        a_off, b_diag = row["jac"]
        pad = np.concatenate([[0.0], np.abs(a_off), [0.0]])
        gersh.append(float(np.min(b_diag - pad[:-1] - pad[1:])))
    gersh = np.asarray(gersh, float)
    print("    true lambda_min                       %s" % e3(lam_min))
    print("    Gershgorin (Jacobi data only)         %s" % e3(gersh))
    print("    additive deficit lambda_min - bound   %s"
          % e3(lam_min - gersh))
    for ref in refs:
        if ref["delta_R"] <= 0.0:
            continue
        nrm = np.asarray([float(np.linalg.norm(row["J"] - ref["J"], 2))
                          for row in live], float)
        weyl = float(np.min(ref["lam"])) - nrm
        need = float(np.min(ref["lam"])) - x_c
        print("    Weyl vs %s: ||J_h - J_*||_2 %s; bound "
              "lambda_min(J_*) - ||.|| %s; the norm needed for the "
              "bound to certify lambda_min > x_crit is <= %.4e, i.e. a "
              "factor %.3e below the measured norm"
              % (ref["name"], e3(nrm), e3(weyl), need,
                 float(np.median(nrm)) / max(need, 1e-300)))
    n_ok = int(np.sum(gersh > x_c))
    check("B1 the coefficient-only (Gershgorin) bound certifies "
          "lambda_min > x_crit on %d/%d rungs -- the measured size of "
          "the open piece" % (n_ok, len(live)), True)
    print("    READING: both coefficient-only routes are far too loose "
          "at the deployed scales -- the SAME 10^4 looseness CCLIII "
          "measured for the norm route on the reads reappears here on "
          "the eigenvalue side.  What the sum rule needs is a "
          "PARAMETRIX / Lieb-Thirring-type bound on the single "
          "sub-band eigenvalue, not an operator-norm estimate.")
    return lam_min, gersh


# ================================================== controls / screens
def controls(zones, rows, fil, d_z, refs):
    section("C -- CONTROLS: do the falsifying worlds break the "
            "nonnegativity or leave the class?")
    truth_by_kz = {r["kz"]: r for r in rows if r["seg"] == "surf"}
    ok_refs = [r for r in refs if r["delta_R"] > 0.0]
    fired = []
    for world in ("smooth", "scramble"):
        ladder = []
        for kz in zones:
            if world == "smooth":
                ladder.append((kz, ob.build_rung("surf", kz,
                                                 world="smooth")))
            else:
                ladder.append((kz, ob.build_rung(
                    "surf", kz, scramble_seed=SCRAMBLE_SEED)))
        wall_fire = sum(1 for _kz, r in ladder
                        if r is None or r["negA"] > 0)
        n_align = n_break = n_neg = n_res = 0
        d_res = []
        for kz, ctl in ladder:
            tr = truth_by_kz.get(kz)
            if tr is None or ctl is None or not ctl.get("core_ok") \
                    or tr.get("jac") is None:
                continue
            n_align += 1
            with np.errstate(over="ignore", invalid="ignore"):
                mw = sym(tr["step"]["Q"].T
                         @ (ctl["S"] / tr["tau_scale"])
                         @ tr["step"]["Q"])
                jf = jacobi_form(mw)
            if jf is None:
                n_break += 1
                continue
            a_off, b_diag, _qq = jf
            _jm, lam, wgt = spectral_data(a_off, b_diag)
            if not (np.all(np.isfinite(lam)) and np.all(
                    np.isfinite(wgt))):
                n_break += 1
                continue
            r_vals = fil.value(lam)
            reserve_w = 1.0 - float(np.sum(r_vals))
            d_res.append(abs(reserve_w - tr["reserve"]))
            # (i) the band-slack remainder E_out grows beyond truth's
            e_w = float(np.sum(np.maximum(r_vals - d_z, 0.0)))
            e_t = float(np.sum(np.maximum(tr["r"] - d_z, 0.0)))
            broken = e_w > e_t + CTRL_RES_BAR
            # (ii) a reference-relative term that is >= 0 on truth
            #      goes negative in the world
            for ref in ok_refs:
                mask_w = out_mask_of(lam, fil)
                mask_t = out_mask_of(tr["lam"], fil)
                ws_tot = np.sum(ref["w"], axis=0)
                q_w = -float(np.sum(ws_tot[~mask_w]
                                    * (r_vals - ref["r"])[~mask_w]))
                q_t = -float(np.sum(ws_tot[~mask_t]
                                    * (tr["r"] - ref["r"])[~mask_t]))
                broken = broken or (q_t >= -NONNEG_TOL
                                    and q_w < -NONNEG_TOL)
            n_neg += int(e_w > e_t + CTRL_RES_BAR)
            n_res += int(broken)
        fire = (n_res + n_break) > 0.5 * max(n_align, 1)
        fired.append(fire)
        print("    %-9s wall target fires %d/%d; aligned rungs %d = "
              "nonnegativity-broken %d + representation-break %d + "
              "silent %d; |reserve_world - reserve_truth| med %.4e "
              "(bar %.0e) -> %s"
              % (world, wall_fire, len(ladder), n_align, n_res,
                 n_break, n_align - n_res - n_break,
                 float(np.median(d_res)) if d_res else float("nan"),
                 CTRL_RES_BAR, "FIRE" if fire else "SILENT"))
        if world == "smooth":
            check("C1 SMOOTH violates the wall target (negA > 0) on "
                  "%d/%d surface rungs" % (wall_fire, len(ladder)),
                  wall_fire == len(ladder), kill="K4")
        check("C3.%s the reserve itself moves in the %s world: med "
              "%.4e >= %.0e" % (world[:3], world,
                                float(np.median(d_res)) if d_res
                                else float("nan"), CTRL_RES_BAR),
              bool(d_res) and float(np.median(d_res))
              >= CTRL_RES_BAR, kill="K4")
    check("C2 both falsifying worlds are SEEN (nonnegativity broken "
          "or class left) on a majority of aligned rungs: %d/2 fired"
          % sum(fired), all(fired), kill="K4")
    return fired


def ch_surface_map(rows):
    section("H -- CCXVII c_h diagnostic on the matched surface "
            "terminators (labelled screen currency only)")
    out = {}
    for kz in sorted({r["kz"] for r in rows if r["seg"] == "surf"}):
        rung = eul.level_rung(kz)
        if rung is None:
            continue
        dens = eul.grid_density(rung["c"])
        pos = eul.gram_from_dens(np.where(dens > 0.0, dens, 0.0),
                                 rung["M"])
        neg = eul.gram_from_dens(np.where(dens > 0.0, 0.0, -dens),
                                 rung["M"])
        last = pos.shape[0] - 1
        top = float(sla.eigh(neg, pos, eigvals_only=True,
                             subset_by_index=[last, last])[0])
        out[int(kz)] = 1.0 - top
    vals = list(out.values())
    check("H1 c_h matched on %d surface steps; band %s inside cited "
          "[1.4e-8, 1.7e-4] up to 2x" % (len(out), e3(vals)),
          len(out) >= 1 and min(vals) >= 0.5 * 1.4e-8
          and max(vals) <= 2.0 * 1.7e-4, kill="K2")
    return out


def screens(rows, results, e_out, ch_map, d_z):
    section("P -- SCREENS: tau- and c_h-relocation on every group "
            "value (the corridor's currency must survive)")
    live = [r for r in rows if r.get("jac") is not None]
    taus = np.asarray([r["tau_scale"] for r in live], float)
    mask = np.asarray([r["kz"] in ch_map and r["seg"] == "surf"
                       for r in live], bool)
    chs = np.asarray([ch_map[r["kz"]] for r in live
                      if r["kz"] in ch_map and r["seg"] == "surf"],
                     float)
    print("    delta_R is a FROZEN constant of the filter "
          "(delta_R^Z = %.6f): its relocation screen is VACUOUS BY "
          "CONSTRUCTION and is not scored." % d_z)
    reloc = []
    for res in results:
        for name, arr in (("Q_R", res["q"]), ("G_R", res["g"]),
                          ("H_R", res["h"])):
            label = "%s/%s:%s" % (res["kind"], res["ref"]["name"]
                                  if res["ref"] else "free", name)
            t1, v1 = screen(np.abs(arr), taus, "%s vs tau" % label)
            t2, v2 = screen(np.abs(arr)[mask], chs,
                            "%s vs c_h" % label)
            print("      " + t1 + " | " + t2)
            if "RELOC" in (v1, v2):
                reloc.append(label)
    t1, v1 = screen(e_out, taus, "E_out vs tau")
    t2, v2 = screen(e_out[mask], chs, "E_out vs c_h")
    print("      " + t1 + " | " + t2)
    if "RELOC" in (v1, v2):
        reloc.append("E_out")
    check("P1 tau/c_h relocation screens on every group value and on "
          "E_out: relocation seats %s" % (",".join(reloc) or "none"),
          not reloc)
    return reloc


# =============================================================== main
def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: CASE-SR( %s )" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64 measurements on the deployed ladder
  only: the 68-step CCVII ladder and the FIXED CCXXV m=8 pole family.
  Every decomposition is an EXACT algebraic identity at dimension 8,
  warded per rung and per pole; the sum-rule verdict is a SIGN CENSUS
  over a finite family of declared groupings, not a theorem about all
  h.  A positive sum rule here REDUCES the reserve certificate to a
  spectral-inclusion statement about the deployed ladder -- it proves
  nothing about the limit and is NOT an RH claim.  No marker moves; no
  paper, ledger, website, manifest or verification file is touched.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.KS.DUAL.01 probe C -- the Case-type "
            "positive sum rule for the Zolotarev reserve "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac1 = ast_scan_functions(("ref_arcsine_unit", "ref_arcsine_band",
                              "ref_log_band", "ref_filter_gapset",
                              "filter_bands", "arcsine_nodes"),
                             LADDER_IDS)
    check("S0.2 AC1 every reference builder is filter-geometry only "
          "(no ladder identifier -> delta_R is a constant of the "
          "filter)", not ac1, ",".join(sorted(set(ac1))), kill="K2")
    ac2 = ast_scan_functions(("coef_part",), READ_IDS)
    check("S0.3 AC2 the coefficient carrier contains no read and no "
          "J_h-spectral identifier (built from the Jacobi data "
          "difference and the frozen reference resolvent alone)",
          not ac2, ",".join(sorted(set(ac2))), kill="K2")
    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    check("S0.4 CCXLVII artifact schema/dimensions fixed",
          (artifact["schema"] == "tfpt.zolotarev_phase_filter.v1"
           and len(artifact["rungs"]) == STEPS_EXP
           and artifact["filter"]["m"] == NDIM), kill="K1")

    zones, steps = build_ladder()
    if KILLS:
        return finish([])
    fil = get_filter(steps, artifact)
    d_z, x_c = filter_wards(fil)
    if KILLS:
        return finish([])
    rows = translation(steps, artifact, fil)
    if KILLS:
        return finish([])
    n_out = jacobi_layer(rows, fil)
    if KILLS:
        return finish([])
    refs = build_references(fil)
    if KILLS:
        return finish([])
    ok_refs = decomposition(rows, refs, fil)
    if KILLS:
        return finish([])
    results, sr_verdict, e_out, margin = sumrule_search(
        rows, refs, fil, d_z, x_c)
    ent = entropy_hull(rows, refs, fil)
    lam_min, gersh = coefficient_side_bound(rows, refs, fil, x_c)
    ch_map = ch_surface_map(rows)
    reloc = screens(rows, results, e_out, ch_map, d_z)
    fired = controls(zones, rows, fil, d_z, refs)

    ratios = []
    for name, dat in ent.items():
        ratios.append("%s KL med %.3e" % (name,
                                          float(np.median(dat["kl"]))))
    labels = [
        "DECOMP-EXACT(perturbation determinant, canonical "
        "factorization per rung per pole, Hankel-Vandermonde at "
        "dimension 8)",
        sr_verdict,
        "ENTROPY-EMPTY-IN-TRACE(site-0 %s)"
        % ("; ".join(ratios) or "none"),
        "OUTLIER(%d/%d rungs with an eigenvalue outside [c, L]; "
        "x_crit %.3e; reserve margin min %.4e)"
        % (int(np.sum(n_out > 0)), len(n_out), x_c,
           float(np.min(margin))),
        "OPEN-PIECE(coefficient-only lambda_min bound below x_crit on "
        "%d/%d rungs)" % (int(np.sum(gersh <= x_c)), len(gersh)),
        "CONTROLS(%d/2 fired)" % sum(fired),
        "SCREENS(%s)" % ("relocation seats " + ",".join(reloc)
                         if reloc else "no relocation"),
        "REFS(%s admissible)" % (",".join(r["name"] for r in ok_refs)
                                 or "none"),
    ]
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
