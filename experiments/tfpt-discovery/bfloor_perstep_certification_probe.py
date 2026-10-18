#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bfloor_perstep_certification_probe -- PRIME.ONEBADMODE.BFLOOR.PERSTEP.01
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE ONE MISSING INPUT OF THE SIGMA CHAIN, CERTIFIED.  CCLXV
(sigma_coupling_pivot_probe) proved the seam identity sigma = q/n =
1 - s/n exactly on the deployed ladder and typed the closure
SIGMA-CONDITIONAL(X): with the source-only entry fact n > 0 (68/68)
the pivot-positive map closes at t*_pos = 0.8828, and the source-only
Gauss-Radau moment bound on sigma FAILS with the widened cited global
B-floor 0.3146 (deepest K = 7 ladder max 2.1609) but CLEARS with the
MEASURED per-step floor lambda_min(B) (K = 4 ladder max 0.6481) --
the LP extremal measure sits exactly on the too-coarse floor, so X is
floor QUALITY, not moment depth.  CCLXIX (sigma_stress_battery_probe)
registered SIGMA_ENV = 0.7809 and found the wall-legal F0
surface-off-ladder zone (h in (900, 1450], excluded from the register
only by the H_LADDER_MAX = 900 cut) where sigma rises to 0.709925.
THE B-BLOCK IS THE PROGRAM'S PROVEN-TRACTABLE HALF: the P_G chain
certified B >= 0.5523 I exact-rationally on the 39 surface rungs
(pg_chain_interval_rollout_probe round 62 LDL machine; the CCXLI
mu1-weak interval tier reached the full surface).  THIS PROBE
supplies X: a CERTIFIED per-step B-floor on the FULL 68-step ladder
(surface + bridge + deep) AND the F0 off-ladder cells, at the
per-step quality the Gauss-Radau bound needs, and composes the chain.

 (a) THE TARGET TABLE.  Per step (68 registered + the F0 cells), the
     REQUIRED floor: the smallest c such that the depth-K = 4
     Gauss-Radau bound with prescribed node c gives
         sigma_bound(c) = RADAU_4(nu_0..nu_6; c) / n
                        <= TARGET
                         = min(t*_pos - 0.05, t_close_pos - 0.05,
                               SIGMA_ENV) = 0.7809
     (the bound is monotone DECREASING in c, so the requirement is a
     lower threshold; amendment A1 discloses the mission-sketch
     wording).  Reported against the measured lambda_min(B) per step:
     the feasibility census.  The bridge step (lambda_min(B) = 0.3496,
     the ladder dip) is the declared risk point.
 (b) THE CERTIFICATION.  Per step, the exact-rational LDL machine of
     the P_G chain (round 62, verbatim: Sylvester/LDL in Fraction
     arithmetic on the dyadic float64 entries; a dyadic bisection
     whose every accepted shift is re-proved, never rounded inward)
     certifies
         lambda_min(B_step) >= c_step
     with c_step the largest certified dyadic floor (BIS_ITERS = 40).
     On top, the Radau bound itself is lifted to the EXACT-RATIONAL
     tier: the b-weighted moments nu_k = b^T B^k b are exact dyadic
     rationals of the wall entries (CCVII v897 class), the monic
     three-term recurrence comes from the exact Chebyshev algorithm
     (E4), the Radau modification and the rule value
     q_R = nu_0 [T~^{-1}]_{11} are rational linear algebra, and the
     census comparison sigma_bound = q_R / n <= TARGET is an exact
     Fraction comparison.  The float route (CCLXV machinery verbatim)
     is kept as a cross-ward, and E3's upper-bound property is warded
     per step against the truth q (RB1), never consumed on faith.
     A directed-rounding interval-Cholesky cross-tier (outward
     float64, refuse-only: it can CONFIRM a floor or REFUSE on width,
     never deny) is run at the required floor -- the pg_chain refusal
     discipline honored at the cheap end.  Refusal typing: a cell
     with no certifiable floor is REFUSED and carried, never
     repaired.
 (c) THE COMPOSED CHAIN.  If the census closes: for every step of the
     deployed ladder (and every tested F0 cell), the composed
     statement with every premise typed --
       P1 n > 0                      (exact-rational entry theorem)
       P2 lambda_min(B) >= c_step    (exact-rational LDL theorem)
       P3 q <= RADAU_4(nu; c_step)   (E3, hypothesis spec(B) in
                                      [c_step, inf) DISCHARGED by P2;
                                      remainder sign warded RB1)
       P4 sigma = q/n <= bound       (exact rational arithmetic)
       => sigma <= bound <= TARGET = 0.7809 < t*_pos = 0.8828
       => s = (1 - sigma) n >= (1 - bound) n > 0
       => M is positive definite (E2 Schur, using P2's B > 0),
     with the honest pedigree flags: t*_pos is a NUMERIC supremum
     (an optimizer maximum is a LOWER bound of the true sup, so
     t*_num is an UPPER bound of the true closing threshold; the
     rigor lane d7a7e574 is certifying it separately), SIGMA_ENV is
     a REGISTERED numeric envelope, and the scope is the deployed
     ladder plus the tested F0 cells -- NO cofinal claim, no
     registration/edge question settled here.
 (d) GATES.  Reproduce CCLXV's Gauss-Radau ladder-max numbers (K =
     1..7 at the widened cited floor, K = 1..4 at the measured
     per-step floor) and print 3 spot steps; controls-must-fire (a
     claimed floor ABOVE the true lambda_min must be refused by the
     exact LDL and by the interval tier; a synthetic
     inflated-coupling step must FAIL the census -- the certification
     is not vacuous); tau / CCXVII c_h relocation screens on the
     certified margins; anti-circularity scanned (floors and moments
     from B's entries forward; NO eigendata in the certificate path,
     eig only as truth reference).

EXTERNAL-CITED (facts consumed, warded numerically, never proved
here).
 E2 Schur / Sylvester: M = [[n, b^T], [b, B]] symmetric is PD iff
    B is PD and s = n - b^T B^{-1} b > 0; a symmetric matrix is PD
    iff the LDL pivots are all positive.  [Horn & Johnson, Matrix
    Analysis, 2nd ed., CUP 2013, Sec. 4.3, 7.2.]
 E3 MATRICES, MOMENTS AND QUADRATURE: for symmetric A with spec(A)
    in [c, inf), the K-node Gauss-Radau rule with the node prescribed
    at c is an UPPER bound for u^T A^{-1} u (f(x) = 1/x completely
    monotone).  [Golub & Meurant, Matrices, Moments and Quadrature,
    PUP 2010, Ch. 6-7.]  THE SIGN IS WARDED PER STEP (RB1).
 E4 the Chebyshev algorithm: the monic three-term recurrence
    coefficients of the orthogonal polynomials of a positive measure
    are rational functions of its power moments (the sigma-table
    recursion); the map is exact in exact arithmetic.  [Gautschi,
    Orthogonal Polynomials: Computation and Approximation, OUP 2004,
    Sec. 2.1; Golub & Meurant op. cit. Ch. 4.]
 E5 interval Cholesky: if the outward-rounded interval Cholesky of a
    symmetric interval matrix completes with all pivot lower bounds
    positive, every symmetric matrix in the interval is PD.  [Rump,
    Acta Numerica 19 (2010) 287-449.]
 E6 the diagonal-similarity fact [J^{-1}]_{11} = [T^{-1}]_{11} for a
    symmetric Jacobi matrix J and its monic (unit-subdiagonal) form
    T = D J D^{-1}: diagonal entries of the inverse are invariant
    under diagonal similarity.  [Horn & Johnson op. cit. Sec. 1.3.]

FROZEN PROTOCOL.
 S0 firewall: AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); predecessors READ-ONLY; no RNG seat.
    AC scans: the CERTIFICATE-path functions (exact_wall_data /
    chebyshev_monic / radau_exact / fr_solve / pd_exact /
    cert_floor_exact / chol_iv) and the float bound-path functions
    (wall_moments / lanczos_pair / radau_upper / sigma_bound_source /
    required_floor) carry no read, no eigensolver, no pivot read, no
    ladder identifier -- entries and frozen constants only (CCLXV
    ban list verbatim).
 W  ladder rebuilt read-only (42 surface rungs -> 68 = 40 + 1 + 27
    steps); step keys warded against the stored CCXLVII artifact;
    the CCLXIX F0 family rebuilt verbatim (off-ladder frame-A zones,
    descending h, cap 12; chain + nearest-anchor bridge steps).
 B/I Jacobi translation and the CCLXV identity wards per cell
    (sigma == q/n == 1 - s/n at IDENT_TIE); P1 pivot sign n > 0
    warded per cell in float AND exact rational.
 SR repro anchors: ladder sigma max 0.604556 (CCLXV/CCLXIX), ladder
    lambda_min(B) min 0.3496, ladder pivot min 0.082730, F0 sigma
    max 0.709925 (CCLXIX).
 G  the CCLXV Gauss-Radau reproduction: ladder-max curve at the
    widened cited floor (K = 7 value 2.1609) and at the measured
    per-step floor (K = 4 value 0.6481); RB1 sign + node wards at
    both floor choices, zero violations.
 R  the required-floor table (a) and the feasibility census.
 C  the certification (b): exact LDL floors (quality ward: the
    certified floor never exceeds the float truth and sits within
    CERT_GAP_RTOL of it), exact Chebyshev coefficients vs float
    Lanczos, exact Radau value vs float route, RB1 exact-vs-truth,
    node ward, interval cross-tier census, the closing census
    against TARGET (exact Fraction comparison) and against t*_pos.
 X  controls-must-fire: inflated floor claim refused (exact + also
    not certified by the interval tier); exact-machine sanity on a
    synthetic diagonal matrix with known rational spectrum (floor
    bracket exact, PD refused exactly AT the spectrum edge); RB1 in
    EXACT arithmetic on a synthetic diagonal measure; a synthetic
    inflated-coupling step must FAIL the census.
 S  screens: tau and CCXVII c_h relocation screens (CCXLVII bars
    verbatim: PASS <= 0.30, RELOC >= 0.70) on the certified bound,
    on TARGET - bound, on t*_pos - bound and on the floor slack
    c_cert - c_req; h-slopes with 2SE.

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 tier reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

VERDICT (frozen enum, in dominance order):
 BFLOOR-CERT-COMPOSED(all 68 ladder steps AND all F0 cells close
   against TARGET; the composed chain stated loudly with premise
   typing)
 BFLOOR-CERT-LADDER(all 68 ladder steps close; the F0 shortfall
   listed precisely)
 BFLOOR-CERT-PARTIAL(the ladder shortfall listed precisely: which
   step, required vs certified floor, bound vs TARGET).
Every enum is a finite statement about the deployed ladder artifact
and the tested F0 cells; NEVER an all-h statement, NEVER an RH claim.

FROZEN BARS.  NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; IDENT_TIE =
1e-12; TRANSLATE_TIE = 1e-8; MZERO_TIE = 1e-7; REPRO_RTOL = 5e-2;
SIGMA_MAX_REF = 0.604556; SIGMA_RTOL = 2e-3; F0_SIGMA_REF = 0.709925;
F0_RTOL = 2e-3; LAMB_MIN_REF = 0.3496; PIV_MIN_REF = 0.082730;
RADAU7_CITED_REF = 2.1609; RADAU4_MEAS_REF = 0.6481; KDEG = 4;
KMAX = 7; WIDEN_FRAC = 0.10 (CCLXV widening rule verbatim);
TSTAR_POS = 8828/10000; TCLOSE_POS = 8812/10000; T_MARGIN = 5/100;
SIGMA_ENV = 7809/10000 (CCLXIX registration, consumed at the cited
4-digit truncation -- truncation direction makes the bar HARDER);
TARGET = min(TSTAR_POS - T_MARGIN, TCLOSE_POS - T_MARGIN, SIGMA_ENV)
= 7809/10000; BIS_ITERS = 40 (round 62); REQ_ITERS = 60; REQ_LO =
1e-12; RADAU_SIGN_TIE = 1e-12; XR_TIE = 1e-6; COEF_TIE = 1e-6;
CERT_GAP_RTOL = 1e-6; NODE_TIE = 1e-9; F0_CAP = 12; CTRL_STEPS = 3;
CTRL_INFLATE = 1.01; CTRL_COUPLE = 10.0; SLOPE_PASS = 0.30;
SLOPE_RELOC = 0.70; runtime cap 25 min.

HONEST AMENDMENTS (declared before the frozen run).
 A1 the mission sketch asks for 'the largest c such that the bound
    with floor c clears the target'.  The Radau bound is monotone
    DECREASING in the prescribed node c (a larger certified floor
    excludes more b-weighted mass near zero), so the set of clearing
    floors is an upper interval [c_req, lambda_min(B)] and the
    meaningful REQUIRED quantity is its lower threshold c_req --
    the smallest clearing floor.  Disclosed, not hidden.
 A2 the exact-rational Radau tier is an UPGRADE over CCLXV's float
    tier (CCLXV computed the bound in float64 and warded RB1).  The
    upgrade direction only strengthens the certificate; the float
    route is kept and the two tiers are cross-warded per step at
    XR_TIE, and RB1 is still warded against the float truth q.
 A3 the certificate object is the ASSEMBLED float64 wall matrix of
    the deployed ladder (dyadic-rational entries, the CCVII v897
    class) -- the same object CCLXV's sigma chain consumes.  The
    separate question 'do the float64 entries enclose the IDEAL
    real-analytic quantities' is the pg_chain interval program
    (round 63 refused the O(1)-strong deep form; CCXLI's mu1-weak
    interval tier reached the full surface) and is NOT retried here;
    it is typed as the known scope edge of the composed chain.
 A4 the census target consumes t_close_pos - T_MARGIN = 0.8312
    alongside t*_pos - T_MARGIN (CCLXV amendment A5 verbatim: a t*
    above the measured grid must never inflate the bar) and the
    registered SIGMA_ENV; the minimum 0.7809 is the binding bar.
 A5 the F0 cells are OFF-REGISTER by construction (CCLXIX: excluded
    only by the H_LADDER_MAX = 900 registration cut), so the F0 part
    of the census extends the tested scope and can only ADD failure
    modes, never repair a ladder failure.

SMOKE DISCLOSURE (2026-08-12, ONE smoke pass before this freeze;
 everything that changed between the smoke and this freeze is listed
 here, and NO change makes a positive verdict easier).
 SMOKE-1 (SPEC_SHA 78ed678b, 10 contiguous surface rungs + 3 lowest
 deep rungs + 2 F0 zones = 12 cells, 7.1 s, 39 checks, 0 failed, no
 kills) measured: every identity ward at machine precision (I1/I2
 6.9e-16 / 3.3e-16, I3 2.7e-16), the exact Chebyshev monic
 coefficients against float Lanczos at 2.1e-15, the exact-rational
 Radau value against the float route at 2.6e-15, RB1 zero violations
 at every depth and both floor modes, the exact LDL floor within
 4.3e-13 (rel) of the float truth on every cell with zero
 refusals, the interval cross-tier confirming 12/12 required floors
 with zero REFUSED-WIDTH, and all five controls firing (inflated
 claims refused by BOTH tiers on 3/3 cells; the synthetic-diagonal
 floor bracket exact with PD refused exactly AT the spectrum edge;
 exact RB1 9.2918 >= 9 as a Fraction comparison; the x10-coupling
 census control FAILED the census at bound 13.09 as designed).  The
 smoke subset shows the known CCLIII/CCLXI fake-bridge phenomenon
 (its bridge kz 177, h 1219 is NOT a step of the frozen 68-step
 artifact; lambda_min(B) = 5.9e-3 there) -- notable honest reading:
 even that fake cell CLOSED the census (bound 0.5860), because the
 per-step floor tracks the per-step matrix.  The smoke-bypassed
 gates (W4b key match 5/11 on the subset, SR1-SR4, G1/G2) printed
 their subset values and decide only on the frozen ladder, exactly
 like CCLXV's T5.
 CHANGES made after SMOKE-1: NONE in code, bars, controls, screens
 or verdict enums -- the only edit is this disclosure text itself.
 The SPEC SHA moves with this text, as disclosed.

NO RH claim.  No marker moves; no paper, ledger, website, manifest or
verification file is touched; the only edit outside this file is the
German CCLXXVII line prepended to experiments/next.txt AFTER the
frozen summary.

Sources (read-only): onebadmode_moments_probe (CCVII ladder + wall
blocks), zolotarev_phase_filter_probe (CCXXV step assembly),
sigma_coupling_pivot_probe (CCLXV machinery, reproduced locally,
cited), sigma_stress_battery_probe (CCLXIX F0 family, reproduced
locally, cited), pg_chain_interval_rollout_probe (round 62 exact LDL
machine, reproduced verbatim, cited), euler_phase_identity_probe
(CCXVII c_h), v563_paper2_readouts (deployed generators, READ-ONLY).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/bfloor_perstep_certification_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/bfloor_perstep_certification_probe.py
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

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob         # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol    # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul      # noqa: E402 (READ-ONLY)
import v563_paper2_readouts as core           # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
NDIM = 8
SURF_EXP = 42
STEPS_EXP = 68
IDENT_TIE = 1.0e-12
TRANSLATE_TIE = 1.0e-8
MZERO_TIE = 1.0e-7
REPRO_RTOL = 5.0e-2
SIGMA_MAX_REF = 0.604556
SIGMA_RTOL = 2.0e-3
F0_SIGMA_REF = 0.709925
F0_RTOL = 2.0e-3
LAMB_MIN_REF = 0.3496
PIV_MIN_REF = 0.082730
RADAU7_CITED_REF = 2.1609
RADAU4_MEAS_REF = 0.6481
KDEG = 4
KMAX = 7
WIDEN_FRAC = 0.10
TSTAR_POS = Fraction(8828, 10000)
TCLOSE_POS = Fraction(8812, 10000)
T_MARGIN = Fraction(5, 100)
SIGMA_ENV = Fraction(7809, 10000)
TARGET = min(TSTAR_POS - T_MARGIN, TCLOSE_POS - T_MARGIN, SIGMA_ENV)
BIS_ITERS = 40
REQ_ITERS = 60
REQ_LO = 1.0e-12
RADAU_SIGN_TIE = 1.0e-12
XR_TIE = 1.0e-6
COEF_TIE = 1.0e-6
CERT_GAP_RTOL = 1.0e-6
NODE_TIE = 1.0e-9
F0_CAP = 12
CTRL_STEPS = 3
CTRL_INFLATE = 1.01
CTRL_COUPLE = 10.0
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CB_F = float(ob.CB_CITED)
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
# AC: the bound/certificate path may see wall ENTRIES and frozen
# constants only -- no read, no pivot read, no eigensolver, no ladder
# identifier (CCLXV DERIV ban list verbatim).
DERIV_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
                "lu_read", "assemble_step", "build_rung", "artifact",
                "h", "gap", "lamB1", "sigma", "sigma_quotient",
                "eigs", "eigvalsh", "eigvals", "eigh", "eig", "inv",
                "pinv", "theta", "row", "rows", "step", "steps")
CERT_FUNCS = ("exact_wall_data", "chebyshev_monic", "radau_exact",
              "fr_solve", "pd_exact", "cert_floor_exact", "chol_iv")
FLOAT_FUNCS = ("wall_moments", "lanczos_pair", "radau_upper",
               "sigma_bound_source", "required_floor")

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
                elif isinstance(sub, ast.arg):
                    nm = sub.arg
                if nm and nm in banned:
                    bad.append("%s:%s" % (node.name, nm))
    return bad


def trio(values):
    v = np.asarray(values, float)
    v = v[np.isfinite(v)]
    if len(v) == 0:
        return (float("nan"),) * 3
    return (float(np.min(v)), float(np.median(v)), float(np.max(v)))


def e3(values):
    return "%.3e/%.3e/%.3e" % trio(values)


def f4(values):
    return "%.4f/%.4f/%.4f" % trio(values)


def linfit(x, y):
    """OLS y = a + s x (CCLIII verbatim); returns s, 2SE, R^2, a."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    xm, ym = x.mean(), y.mean()
    sxx = float(np.sum((x - xm) ** 2))
    if sxx == 0.0 or n < 3:
        return 0.0, float("inf"), float("nan"), float(ym)
    s = float(np.sum((x - xm) * (y - ym)) / sxx)
    a = ym - s * xm
    res = y - (a + s * x)
    se = math.sqrt(float(np.sum(res ** 2)) / max(n - 2, 1) / sxx)
    sst = float(np.sum((y - ym) ** 2))
    r2 = 1.0 - float(np.sum(res ** 2)) / sst if sst > 0 else 1.0
    return s, 2.0 * se, r2, a


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


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


# =========================================== Jacobi form (CCLIII)
def jacobi_form(matrix):
    """Lanczos tridiagonalization of (M, e_0) -- CCLIII/CCLXI/CCLXV
    machinery reproduced verbatim.  Returns (a, b, Q) or None."""
    if not np.all(np.isfinite(matrix)):
        return None
    n = NDIM
    qq = np.zeros((n, n))
    qq[0, 0] = 1.0
    a = np.zeros(n - 1)
    b = np.zeros(n)
    for k in range(n):
        z = matrix @ qq[:, k]
        b[k] = float(qq[:, k] @ z)
        z = z - b[k] * qq[:, k]
        if k > 0:
            z = z - a[k - 1] * qq[:, k - 1]
        for _ in range(2):
            z = z - qq[:, :k + 1] @ (qq[:, :k + 1].T @ z)
        if k == n - 1:
            break
        nz = float(np.linalg.norm(z))
        if not math.isfinite(nz) or nz <= 1e-13 * max(1.0, abs(b[k])):
            return None
        a[k] = nz
        qq[:, k + 1] = z / nz
    return a, b, qq


def theta_matrices(theta):
    """theta = (b_1..b_8, a_1..a_7) -> (J, J_B) (CCLXI verbatim)."""
    bd = np.asarray(theta[:NDIM], float)
    ad = np.asarray(theta[NDIM:], float)
    jm = np.diag(bd)
    idx = np.arange(NDIM - 1)
    jm[idx, idx + 1] = ad
    jm[idx + 1, idx] = ad
    return jm, jm[1:, 1:]


def sigma_quotient(theta):
    """sigma = a_1^2 [J_B^-1]_11 / b_1 (CCLXI verbatim)."""
    _jm, jb = theta_matrices(theta)
    b1 = float(theta[0])
    a1 = float(theta[NDIM])
    if b1 == 0.0:
        return float("inf")
    try:
        e1 = np.zeros(NDIM - 1)
        e1[0] = 1.0
        mb = float(np.linalg.solve(jb, e1)[0])
    except np.linalg.LinAlgError:
        return float("inf")
    return a1 * a1 * mb / b1


# ============= float bound path (CCLXV verbatim, AC-scanned)
def wall_moments(matrix, kdeg):
    """nu_k = b^T B^k b, k = 0..kdeg, from the ENTRIES of the wall
    matrix.  No eigensolver, no inverse, no pivot read."""
    vec = np.asarray(matrix, float)[1:, 0]
    blk = np.asarray(matrix, float)[1:, 1:]
    out = []
    cur = vec.copy()
    for _k in range(kdeg + 1):
        out.append(float(vec @ cur))
        cur = blk @ cur
    return np.asarray(out, float)


def lanczos_pair(matrix, kdeg):
    """Lanczos data of (B, b/||b||) from the wall ENTRIES (CCLXV
    verbatim); forward recursion only."""
    vec = np.asarray(matrix, float)[1:, 0]
    blk = np.asarray(matrix, float)[1:, 1:]
    dim = blk.shape[0]
    nrm = float(np.linalg.norm(vec))
    if not math.isfinite(nrm) or nrm <= 0.0:
        return None
    frame = np.zeros((dim, kdeg))
    frame[:, 0] = vec / nrm
    alp = []
    bet = []
    for j in range(kdeg):
        zvec = blk @ frame[:, j]
        aj = float(frame[:, j] @ zvec)
        alp.append(aj)
        zvec = zvec - aj * frame[:, j]
        if j > 0:
            zvec = zvec - bet[j - 1] * frame[:, j - 1]
        for _ in range(2):
            zvec = zvec - frame[:, :j + 1] @ (frame[:, :j + 1].T
                                              @ zvec)
        if j == kdeg - 1:
            break
        nz = float(np.linalg.norm(zvec))
        if not math.isfinite(nz) or nz <= 1e-13 * max(1.0, abs(aj)):
            return None
        bet.append(nz)
        frame[:, j + 1] = zvec / nz
    return np.asarray(alp, float), np.asarray(bet, float), nrm * nrm


def radau_upper(alp, bet, floor_c, mass):
    """E3 Gauss-Radau upper bound for b^T B^{-1} b at depth
    K = len(alp) with the node prescribed at floor_c (CCLXV
    verbatim); the node ward is done by the CALLER."""
    kdeg = len(alp)
    jac = np.diag(np.asarray(alp, float)).copy()
    for i in range(kdeg - 1):
        jac[i, i + 1] = jac[i + 1, i] = float(bet[i])
    if kdeg > 1:
        shifted = jac[:kdeg - 1, :kdeg - 1] - floor_c * np.eye(
            kdeg - 1)
        rhs = np.zeros(kdeg - 1)
        rhs[-1] = float(bet[kdeg - 2]) ** 2
        try:
            sol = np.linalg.solve(shifted, rhs)
        except np.linalg.LinAlgError:
            return float("nan"), None
        jac[kdeg - 1, kdeg - 1] = floor_c + float(sol[-1])
    else:
        jac[0, 0] = floor_c
    unit = np.zeros(kdeg)
    unit[0] = 1.0
    try:
        val = float(np.linalg.solve(jac, unit)[0]) * mass
    except np.linalg.LinAlgError:
        return float("nan"), None
    return val, jac


def sigma_bound_source(matrix, floor_c, kdeg):
    """THE SOURCE-ONLY BOUND (CCLXV verbatim): sigma <=
    RADAU_K(nu; floor_c) / n from the wall ENTRIES and the floor."""
    piv = float(np.asarray(matrix, float)[0, 0])
    lan = lanczos_pair(matrix, kdeg)
    if lan is None or piv <= 0.0:
        return float("nan"), None
    alp, bet, mass = lan
    val, jac = radau_upper(alp, bet, floor_c, mass)
    if not math.isfinite(val):
        return float("nan"), None
    return val / piv, jac


def required_floor(matrix, tgt, kdeg, flo_hi):
    """(a) THE REQUIRED FLOOR: the smallest c in [REQ_LO, flo_hi]
    with sigma_bound(c) <= tgt (the bound is monotone decreasing in
    c, amendment A1).  Returns (c_req, status): status FEAS / ANY
    (already clears at REQ_LO) / INFEAS (fails even at flo_hi)."""
    val_hi, _ = sigma_bound_source(matrix, flo_hi, kdeg)
    if not math.isfinite(val_hi) or val_hi > tgt:
        return float("nan"), "INFEAS"
    val_lo, _ = sigma_bound_source(matrix, REQ_LO, kdeg)
    if math.isfinite(val_lo) and val_lo <= tgt:
        return REQ_LO, "ANY"
    lo, hi = REQ_LO, flo_hi
    for _ in range(REQ_ITERS):
        mid = 0.5 * (lo + hi)
        val, _ = sigma_bound_source(matrix, mid, kdeg)
        if math.isfinite(val) and val <= tgt:
            hi = mid
        else:
            lo = mid
    return hi, "FEAS"


# ============ the exact-rational tier (round 62 + E4, AC-scanned)
def exact_wall_data(matrix, kdeg):
    """Pivot n, b-weighted moments nu_0..nu_kdeg and the co-block,
    ALL as exact Fractions of the dyadic float64 ENTRIES (CCVII v897
    class).  No eigensolver, no inverse, no read."""
    mm = np.asarray(matrix, float)
    dim = mm.shape[0] - 1
    piv = Fraction(float(mm[0, 0]))
    vec = [Fraction(float(v)) for v in mm[1:, 0]]
    blk = [[Fraction(float(mm[i + 1, j + 1])) for j in range(dim)]
           for i in range(dim)]
    cur = list(vec)
    momv = []
    for _k in range(kdeg + 1):
        momv.append(sum(a * c for a, c in zip(vec, cur)))
        cur = [sum(blk[i][j] * cur[j] for j in range(dim))
               for i in range(dim)]
    return piv, momv, blk


def chebyshev_monic(momv, kdeg):
    """E4 Chebyshev algorithm, EXACT: monic recurrence al_1..al_{k-1},
    be_1..be_{k-1} (be = squared symmetric betas) of the measure with
    power moments momv[0..2k-2].  None on degeneracy (a be <= 0)."""
    need = 2 * kdeg - 1
    if len(momv) < need or momv[0] <= 0:
        return None
    tab = {-1: [Fraction(0)] * need, 0: list(momv[:need])}
    al = [momv[1] / momv[0]]
    be = []
    for k in range(1, kdeg):
        prev = tab[k - 1]
        pprev = tab[k - 2]
        cur = [Fraction(0)] * need
        for pos in range(k, 2 * kdeg - 1 - k):
            cur[pos] = (prev[pos + 1] - al[k - 1] * prev[pos]
                        - (be[k - 2] * pprev[pos] if k >= 2
                           else Fraction(0)))
        tab[k] = cur
        if prev[k - 1] <= 0 or cur[k] <= 0:
            return None
        be.append(cur[k] / prev[k - 1])
        if 2 * kdeg - 1 - k > k + 1:
            al.append(cur[k + 1] / cur[k] - prev[k] / prev[k - 1])
    if len(al) != kdeg - 1 or len(be) != kdeg - 1:
        return None
    return al, be


def fr_solve(amat, rhs):
    """Exact Gaussian elimination with partial (nonzero) pivoting on
    Fractions; returns the solution list or None if singular."""
    dim = len(amat)
    aa = [list(r) + [rhs[i]] for i, r in enumerate(amat)]
    for k in range(dim):
        pr = None
        for i in range(k, dim):
            if aa[i][k] != 0:
                pr = i
                break
        if pr is None:
            return None
        aa[k], aa[pr] = aa[pr], aa[k]
        pv = aa[k][k]
        for i in range(k + 1, dim):
            f = aa[i][k] / pv
            if f == 0:
                continue
            for j in range(k, dim + 1):
                aa[i][j] = aa[i][j] - f * aa[k][j]
    out = [Fraction(0)] * dim
    for k in range(dim - 1, -1, -1):
        acc = aa[k][dim]
        for j in range(k + 1, dim):
            acc = acc - aa[k][j] * out[j]
        out[k] = acc / aa[k][k]
    return out


def radau_exact(al, be, flo, mass):
    """EXACT-RATIONAL Gauss-Radau upper-bound value for the 1/x
    integral at depth K = len(al)+1 with the node prescribed at flo:
    monic form (E6: diagonal entries of the inverse are invariant
    under the diagonal similarity to the symmetric Jacobi form).
    None on a singular solve."""
    kdeg = len(al) + 1
    dim = kdeg - 1
    tm = [[Fraction(0)] * dim for _ in range(dim)]
    for i in range(dim):
        tm[i][i] = al[i] - flo
        if i + 1 < dim:
            tm[i][i + 1] = be[i]
            tm[i + 1][i] = Fraction(1)
    rhs = [Fraction(0)] * dim
    rhs[dim - 1] = Fraction(1)
    sol = fr_solve(tm, rhs)
    if sol is None:
        return None
    alr = flo + be[kdeg - 2] * sol[dim - 1]
    tt = [[Fraction(0)] * kdeg for _ in range(kdeg)]
    for i in range(kdeg):
        tt[i][i] = al[i] if i < kdeg - 1 else alr
        if i + 1 < kdeg:
            tt[i][i + 1] = be[i]
            tt[i + 1][i] = Fraction(1)
    rhs2 = [Fraction(0)] * kdeg
    rhs2[0] = Fraction(1)
    sol2 = fr_solve(tt, rhs2)
    if sol2 is None:
        return None
    return mass * sol2[0]


def pd_exact(afr, shift=Fraction(0)):
    """Exact Sylvester/LDL decision (round 62 verbatim): is
    A - shift I PD?"""
    dim = len(afr)
    aa = [[afr[i][j] - (shift if i == j else 0) for j in range(dim)]
          for i in range(dim)]
    for k in range(dim):
        p = aa[k][k]
        if p <= 0:
            return False, k
        for i in range(k + 1, dim):
            f = aa[i][k] / p
            for j in range(k + 1, dim):
                aa[i][j] = aa[i][j] - f * aa[k][j]
    return True, -1


def cert_floor_exact(afr, lo, hi, iters=BIS_ITERS):
    """Largest certified c in [lo, hi] with A - c I PD (round 62
    verbatim: dyadic bisection; the final decision re-run exactly;
    NEVER rounded inward).  None if even lo is refused."""
    lo = Fraction(lo)
    hi = Fraction(hi)
    if hi < lo:
        hi = lo
    ok, _ = pd_exact(afr, lo)
    if not ok:
        return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        ok, _ = pd_exact(afr, mid)
        if ok:
            lo = mid
        else:
            hi = mid
    ok, _ = pd_exact(afr, lo)
    assert ok
    return lo


def chol_iv(blk, shift):
    """Directed-rounding float64 interval Cholesky/LDL of
    (blk - shift I): returns True iff EVERY symmetric matrix within
    one outward ulp of the exact elimination is PD (E5), None on a
    pivot interval touching <= 0 (REFUSED -- never a denial)."""
    nxt = np.nextafter

    def i_sub(alo, ahi, blo, bhi):
        return nxt(alo - bhi, -np.inf), nxt(ahi - blo, np.inf)

    def i_mul(alo, ahi, blo, bhi):
        cand = (alo * blo, alo * bhi, ahi * blo, ahi * bhi)
        return nxt(min(cand), -np.inf), nxt(max(cand), np.inf)

    def i_div(alo, ahi, blo, bhi):
        cand = (alo / blo, alo / bhi, ahi / blo, ahi / bhi)
        return nxt(min(cand), -np.inf), nxt(max(cand), np.inf)

    dim = blk.shape[0]
    alo = np.array(blk, float)
    ahi = np.array(blk, float)
    for i in range(dim):
        alo[i, i], ahi[i, i] = i_sub(alo[i, i], ahi[i, i],
                                     shift, shift)
    for k in range(dim):
        plo, phi = alo[k, k], ahi[k, k]
        if not (plo > 0.0):
            return None
        for i in range(k + 1, dim):
            flo, fhi = i_div(alo[i, k], ahi[i, k], plo, phi)
            for j in range(k + 1, dim):
                qlo, qhi = i_mul(flo, fhi, alo[k, j], ahi[k, j])
                alo[i, j], ahi[i, j] = i_sub(alo[i, j], ahi[i, j],
                                             qlo, qhi)
    return True


# ====================================================== wall ladder
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
    return zones, steps, combined


def artifact_key_ward(steps):
    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    check("W4a CCXLVII artifact schema/dimensions fixed",
          (artifact["schema"] == "tfpt.zolotarev_phase_filter.v1"
           and len(artifact["rungs"]) == STEPS_EXP
           and artifact["filter"]["m"] == NDIM), kill="K1")
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]), int(r["kz"]))
              for r in artifact["rungs"]}
    ours = {(int(st["r1"]["h"]), int(st["r1"]["kz"]),
             int(st["r2"]["h"]), int(st["r2"]["kz"]))
            for st in steps}
    n_match = len(stored & ours)
    check("W4b ladder identity: %d/%d step keys match the stored "
          "CCXLVII artifact" % (n_match, len(ours)),
          SMOKE or (n_match == STEPS_EXP and len(ours) == STEPS_EXP),
          kill="K2")


def build_f0(anchors):
    """The CCLXIX F0 family verbatim: off-ladder frame-A zones
    (descending h, cap F0_CAP), chain steps + one bridge step per
    rung from the nearest registered truth predecessor."""
    section("F0 -- the CCLXIX off-ladder zone, rebuilt verbatim")
    f0_cap = 2 if SMOKE else F0_CAP
    reg = set(ob.ladder_zones())
    f0_zones = [kz for kz in core.frame_a_zones() if kz not in reg]
    f0_pick = sorted(f0_zones,
                     key=lambda kz: -ob.window_of(kz)["h"])[:f0_cap]
    f0_rungs = []
    for kz in f0_pick:
        rr = ob.build_rung("surf", kz, with_split=False)
        if rr is not None:
            f0_rungs.append(rr)
        print("    F0 surf kz %-4d h %-5s %s [%.1f s]"
              % (kz, ob.window_of(kz)["h"],
                 "OK" if rr is not None else "SHORT",
                 time.time() - T0), flush=True)
    fam = sorted([r for r in f0_rungs if r.get("core_ok")],
                 key=lambda r: (r["h"], r["kz"]))
    pairs = list(zip(fam, fam[1:]))
    anc = sorted(anchors, key=lambda r: r["h"])
    for r2 in fam:
        below = [a for a in anc if a["h"] <= r2["h"]]
        r1 = below[-1] if below else anc[0]
        pairs.append((r1, r2))
    out = []
    n_ref = 0
    for r1, r2 in pairs:
        sts = ob.make_steps([r1, r2])
        if not sts:
            n_ref += 1
            continue
        st = sts[0]
        zol.assemble_step(st)
        if st["status"] != "OK":
            n_ref += 1
            continue
        kind = ("chain" if r1.get("kind") == r2.get("kind")
                and r1 in fam else "bridge")
        out.append((st, kind))
    print("    F0 census: %d zones off-ladder, %d picked, %d built, "
          "%d steps admitted (%d chain, %d bridge), %d step-refused"
          % (len(f0_zones), len(f0_pick), len(f0_rungs), len(out),
             sum(1 for _s, k in out if k == "chain"),
             sum(1 for _s, k in out if k == "bridge"), n_ref))
    check("F0.1 the CCLXIX F0 family admitted %d wall-legal cells"
          % len(out), len(out) >= (1 if SMOKE else 8), kill="K1")
    return out, len(f0_pick)


def make_rows(steps, f0_cells):
    rows = []
    for st in steps:
        rows.append(dict(step=st, seg=ob.seg_of(st),
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         schur=float(st["gap"]),
                         n_piv=float(st["n0"]),
                         lam_b=float(st["lamB1"]),
                         l_src=float(st["L_src"]),
                         mode="ladder"))
    for st, kind in f0_cells:
        rows.append(dict(step=st, seg="F0",
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         schur=float(st["gap"]),
                         n_piv=float(st["n0"]),
                         lam_b=float(st["lamB1"]),
                         l_src=float(st["L_src"]),
                         mode=kind))
    for i, r in enumerate(rows):
        r["index"] = i
    return rows


# ============================= B/I: translation + identity wards
def jacobi_identity_wards(rows):
    section("B/I -- Jacobi translation + the CCLXV identity wards "
            "on every cell")
    d_b1 = d_a1 = d_bfl = d_m0 = d_q = d_sig = d_gap = 0.0
    n_bad = 0
    for row in rows:
        st = row["step"]
        jf = jacobi_form(st["Mt"])
        if jf is None:
            n_bad += 1
            row["theta"] = None
            continue
        a, b, _qq = jf
        theta = np.concatenate([b, a])
        row["theta"] = theta
        _jm, jb = theta_matrices(theta)
        scale = max(1.0, float(np.max(np.abs(st["Mt"]))))
        d_b1 = max(d_b1, abs(b[0] - st["n0"]) / scale)
        d_a1 = max(d_a1, abs(a[0] - float(np.linalg.norm(st["bvec"])))
                   / scale)
        lamb = float(np.linalg.eigvalsh(jb)[0])
        d_bfl = max(d_bfl, abs(lamb - st["lamB1"])
                    / max(1.0, abs(st["lamB1"])))
        e0 = np.zeros(NDIM)
        e0[0] = 1.0
        m0 = float(np.linalg.solve(_jm, e0)[0])
        d_m0 = max(d_m0, abs(m0 * row["schur"] - 1.0))
        piv = float(st["n0"])
        vec = np.asarray(st["bvec"], float)
        blk = np.asarray(st["Bblk"], float)
        q_wall = float(vec @ np.linalg.solve(blk, vec))
        sig = sigma_quotient(theta)
        row["sigma"] = sig
        row["q_wall"] = q_wall
        d_q = max(d_q, abs(sig * piv - q_wall) / max(1.0, abs(q_wall)))
        d_sig = max(d_sig, abs(sig - q_wall / piv)
                    / max(1.0, abs(sig)))
        d_gap = max(d_gap, abs(sig - (1.0 - row["schur"] / piv))
                    / max(1.0, abs(sig)))
    check("B1 Lanczos form of (M, e_0) exists on all %d cells"
          % len(rows), n_bad == 0, "breakdowns %d" % n_bad, kill="K2")
    check("B2 TRANSLATE b_1 == M[0,0], a_1 == ||M[1:,0]||: %.2e / "
          "%.2e <= %.0e" % (d_b1, d_a1, TRANSLATE_TIE),
          d_b1 <= TRANSLATE_TIE and d_a1 <= TRANSLATE_TIE, kill="K2")
    check("B3 TRANSLATE lambda_min(J_B) == lamB1 (E2 compression): "
          "max rel %.2e <= %.0e" % (d_bfl, TRANSLATE_TIE),
          d_bfl <= TRANSLATE_TIE, kill="K2")
    check("B4 WARD m(0) * gap == 1: max %.2e <= %.0e"
          % (d_m0, MZERO_TIE), d_m0 <= MZERO_TIE, kill="K2")
    check("I1/I2 IDENTITY sigma * n == q == b^T B^-1 b: max rel "
          "%.2e / %.2e <= %.0e" % (d_q, d_sig, IDENT_TIE),
          d_q <= IDENT_TIE and d_sig <= IDENT_TIE, kill="K2")
    check("I3 IDENTITY sigma == 1 - s/n: max rel %.2e <= %.0e"
          % (d_gap, IDENT_TIE), d_gap <= IDENT_TIE, kill="K2")
    return [r for r in rows if r["theta"] is not None]


def pivot_ward(rows):
    n_pos = 0
    n_pos_exact = 0
    for row in rows:
        if row["n_piv"] > 0.0:
            n_pos += 1
        if Fraction(float(row["step"]["Mt"][0, 0])) > 0:
            n_pos_exact += 1
    pivs = [r["n_piv"] for r in rows]
    check("P1 PIVOT SIGN n = M[0,0] > 0 on all %d cells (float AND "
          "exact rational): %d / %d positive, min %.6f"
          % (len(rows), n_pos, n_pos_exact, min(pivs)),
          n_pos == len(rows) and n_pos_exact == len(rows), kill="K2")


def repro_anchors(rows, n_f0_pick):
    section("SR -- repro anchors against CCLXV/CCLXIX")
    lad = [r for r in rows if r["seg"] != "F0"]
    f0 = [r for r in rows if r["seg"] == "F0"]
    sig_max = max(r["sigma"] for r in lad)
    lam_min = min(r["lam_b"] for r in lad)
    piv_min = min(r["n_piv"] for r in lad)
    check("SR1 ladder sigma max %.6f reproduces %.6f (rtol %.0e)"
          % (sig_max, SIGMA_MAX_REF, SIGMA_RTOL),
          SMOKE or abs(sig_max / SIGMA_MAX_REF - 1.0) <= SIGMA_RTOL,
          kill="K3")
    check("SR2 ladder lambda_min(B) min %.4f reproduces %.4f "
          "(rtol %.0e)" % (lam_min, LAMB_MIN_REF, REPRO_RTOL),
          SMOKE or abs(lam_min / LAMB_MIN_REF - 1.0) <= REPRO_RTOL,
          kill="K3")
    check("SR3 ladder pivot min %.6f reproduces %.6f (rtol %.0e)"
          % (piv_min, PIV_MIN_REF, REPRO_RTOL),
          SMOKE or abs(piv_min / PIV_MIN_REF - 1.0) <= REPRO_RTOL,
          kill="K3")
    if f0:
        f0_max = max(r["sigma"] for r in f0)
        i_mx = max(f0, key=lambda r: r["sigma"])
        print("    F0 sigma max %.6f at kz %d h %.0f mode %s "
              "(CCLXIX 0.709925 at kz 45 h 1359)"
              % (f0_max, i_mx["kz"], i_mx["h"], i_mx["mode"]))
        check("SR4 F0 sigma max %.6f reproduces %.6f (rtol %.0e; "
              "conditioned on the full %d-zone build)"
              % (f0_max, F0_SIGMA_REF, F0_RTOL, F0_CAP),
              SMOKE or (n_f0_pick == F0_CAP
                        and abs(f0_max / F0_SIGMA_REF - 1.0)
                        <= F0_RTOL), kill="K3")
    for seg in ("surf", "bridge", "deep", "F0"):
        sub = [r["sigma"] for r in rows if r["seg"] == seg]
        if sub:
            print("      sigma %-6s (%2d): %s" % (seg, len(sub),
                                                  f4(sub)))


# ================== G: the CCLXV Gauss-Radau reproduction gates
def radau_repro(rows):
    section("G -- reproduce CCLXV's Gauss-Radau ladder maxima "
            "(cited-widened floor K=1..7; measured floor K=1..4)")
    lad = [r for r in rows if r["seg"] != "F0"]
    lam_min = min(r["lam_b"] for r in lad)
    cb_wid = min(CB_F, lam_min * (1.0 - WIDEN_FRAC))
    print("    widened cited floor (CCLXV rule verbatim): "
          "min(c_B = %.4f, %.4f * %.2f) = %.6f"
          % (CB_F, lam_min, 1.0 - WIDEN_FRAC, cb_wid))
    sign_fail = node_fail = 0
    cited_max = {}
    for kdeg in range(1, KMAX + 1):
        vals = []
        for row in lad:
            val, jac = sigma_bound_source(row["step"]["Mt"], cb_wid,
                                          kdeg)
            vals.append(val)
            if math.isfinite(val) and jac is not None:
                if val * row["n_piv"] < row["q_wall"] \
                        - RADAU_SIGN_TIE * max(1.0, row["q_wall"]):
                    sign_fail += 1
                node = float(np.linalg.eigvalsh(jac)[0])
                if node < cb_wid - NODE_TIE * max(1.0, cb_wid):
                    node_fail += 1
        cited_max[kdeg] = float(np.max(np.asarray(vals, float)))
        print("      cited-widened K = %d: ladder max %.4f"
              % (kdeg, cited_max[kdeg]))
    meas_max = {}
    for kdeg in range(1, KDEG + 1):
        vals = []
        for row in lad:
            val, jac = sigma_bound_source(row["step"]["Mt"],
                                          row["lam_b"], kdeg)
            vals.append(val)
            if math.isfinite(val) and jac is not None:
                if val * row["n_piv"] < row["q_wall"] \
                        - RADAU_SIGN_TIE * max(1.0, row["q_wall"]):
                    sign_fail += 1
        meas_max[kdeg] = float(np.max(np.asarray(vals, float)))
        print("      measured-floor K = %d: ladder max %.4f"
              % (kdeg, meas_max[kdeg]))
    check("G1 REPRO CCLXV cited-widened floor, K = %d ladder max "
          "%.4f vs 2.1609 (rtol %.0e)"
          % (KMAX, cited_max[KMAX], REPRO_RTOL),
          SMOKE or abs(cited_max[KMAX] / RADAU7_CITED_REF - 1.0)
          <= REPRO_RTOL, kill="K3")
    check("G2 REPRO CCLXV measured per-step floor, K = %d ladder "
          "max %.4f vs 0.6481 (rtol %.0e)"
          % (KDEG, meas_max[KDEG], REPRO_RTOL),
          SMOKE or abs(meas_max[KDEG] / RADAU4_MEAS_REF - 1.0)
          <= REPRO_RTOL, kill="K3")
    check("G3 RB1 sign ward + node ward across both floor modes and "
          "all depths: %d sign violations, %d node violations"
          % (sign_fail, node_fail),
          sign_fail == 0 and node_fail == 0, kill="K2")
    for i in [0, len(lad) // 2, len(lad) - 1]:
        row = lad[i]
        val, _ = sigma_bound_source(row["step"]["Mt"], row["lam_b"],
                                    KDEG)
        print("    spot step %d (%s kz %d h %.0f): measured-floor "
              "K=%d bound %.6f vs truth sigma %.6f"
              % (row["index"], row["seg"], row["kz"], row["h"],
                 KDEG, val, row["sigma"]))


# ==================== R: (a) the required-floor / target table
def required_table(rows):
    section("R -- (a) THE TARGET TABLE: required floor c_req vs "
            "measured lambda_min(B), TARGET = %.4f (= min(t*_pos - "
            "%.2f, t_close_pos - %.2f, SIGMA_ENV))"
          % (float(TARGET), float(T_MARGIN), float(T_MARGIN)))
    tgt = float(TARGET)
    n_feas = n_any = n_infeas = 0
    for row in rows:
        c_req, status = required_floor(row["step"]["Mt"], tgt, KDEG,
                                       row["lam_b"])
        row["c_req"] = c_req
        row["req_status"] = status
        if status == "INFEAS":
            n_infeas += 1
        elif status == "ANY":
            n_any += 1
        else:
            n_feas += 1
    check("R1 required floor computed on all %d cells: %d threshold "
          "(FEAS), %d clear at any positive floor (ANY), %d "
          "INFEASIBLE at the measured floor"
          % (len(rows), n_feas, n_any, n_infeas), True)
    ratios = [row["c_req"] / row["lam_b"] for row in rows
              if row["req_status"] == "FEAS"]
    print("    required/measured floor ratio (FEAS cells): %s"
          % f4(ratios))
    bad = [r for r in rows if r["req_status"] == "INFEAS"]
    for r in bad:
        val, _ = sigma_bound_source(r["step"]["Mt"], r["lam_b"], KDEG)
        print("      INFEASIBLE cell: %s kz %d h %.0f -- bound at "
              "the measured floor %.4f > TARGET %.4f"
              % (r["seg"], r["kz"], r["h"], val, tgt))
    brg = [r for r in rows if r["seg"] == "bridge"]
    for r in brg:
        print("    THE DECLARED RISK POINT (bridge): lambda_min(B) "
              "= %.6f, c_req = %.6f, ratio %.3f, status %s"
              % (r["lam_b"], r["c_req"], r["c_req"] / r["lam_b"]
                 if math.isfinite(r["c_req"]) else float("nan"),
                 r["req_status"]))
    check("R2 FEASIBILITY census: the measured per-step floor is "
          "sufficient on %d/%d cells (INFEASIBLE cells listed above "
          "and carried into the census)"
          % (len(rows) - n_infeas, len(rows)), n_infeas == 0)
    return n_infeas


# ==================== C: (b) THE CERTIFICATION per step
def certification(rows):
    section("C -- (b) THE CERTIFICATION: exact-rational LDL floor + "
            "exact-rational Gauss-Radau bound per cell")
    d_gapc = 0.0
    n_exceed = 0
    d_coef = 0.0
    d_xr = 0.0
    sign_fail = node_fail = 0
    n_refused = 0
    n_degen = 0
    iv_conf = iv_ref = 0
    n_close_t = 0
    n_close_ts = 0
    for row in rows:
        mat = row["step"]["Mt"]
        pivf, momv, blkf = exact_wall_data(mat, 2 * KDEG - 2)
        hi_hint = Fraction(float(row["lam_b"])) * (Fraction(1)
                                                   + Fraction(1, 10**6))
        c_cert = cert_floor_exact(blkf, Fraction(0), hi_hint)
        if c_cert is None:
            n_refused += 1
            row["c_cert"] = None
            row["bound_fr"] = None
            row["closes_t"] = False
            row["closes_ts"] = False
            continue
        row["c_cert"] = c_cert
        c_f = float(c_cert)
        row["c_cert_f"] = c_f
        if c_f > row["lam_b"] * (1.0 + 1e-9):
            n_exceed += 1
        d_gapc = max(d_gapc, (row["lam_b"] - c_f)
                     / max(1.0, row["lam_b"]))
        cheb = chebyshev_monic(momv, KDEG)
        if cheb is None:
            n_degen += 1
            row["bound_fr"] = None
            row["closes_t"] = False
            row["closes_ts"] = False
            continue
        al_fr, be_fr = cheb
        lan = lanczos_pair(mat, KDEG)
        if lan is not None:
            alp, bet, _mass = lan
            for k in range(KDEG - 1):
                sc = max(1.0, abs(alp[k]))
                d_coef = max(d_coef, abs(float(al_fr[k]) - alp[k])
                             / sc)
                sc2 = max(1.0, bet[k] ** 2)
                d_coef = max(d_coef, abs(float(be_fr[k])
                                         - bet[k] ** 2) / sc2)
        val_fr = radau_exact(al_fr, be_fr, c_cert, momv[0])
        if val_fr is None:
            n_degen += 1
            row["bound_fr"] = None
            row["closes_t"] = False
            row["closes_ts"] = False
            continue
        bound_fr = val_fr / pivf
        row["bound_fr"] = bound_fr
        row["bound_f"] = float(bound_fr)
        # float cross-route at the same certified floor
        val_f, jac = sigma_bound_source(mat, c_f, KDEG)
        if math.isfinite(val_f):
            d_xr = max(d_xr, abs(float(bound_fr) - val_f)
                       / max(1.0, abs(val_f)))
        if jac is not None:
            node = float(np.linalg.eigvalsh(jac)[0])
            if node < c_f - NODE_TIE * max(1.0, c_f):
                node_fail += 1
        # RB1 against the float truth q
        if float(val_fr) < row["q_wall"] \
                - RADAU_SIGN_TIE * max(1.0, row["q_wall"]):
            sign_fail += 1
        # interval cross-tier at the required floor (refuse-only)
        if row["req_status"] == "FEAS":
            got = chol_iv(np.asarray(row["step"]["Bblk"], float),
                          row["c_req"])
            if got:
                iv_conf += 1
            else:
                iv_ref += 1
        row["closes_t"] = bound_fr <= TARGET
        row["closes_ts"] = bound_fr < TSTAR_POS
        if row["closes_t"]:
            n_close_t += 1
        if row["closes_ts"]:
            n_close_ts += 1
    check("C1 exact-rational LDL floor certified on %d/%d cells "
          "(%d REFUSED, carried)" % (len(rows) - n_refused,
                                     len(rows), n_refused),
          n_refused == 0, kill="K2")
    check("C2 floor quality: certified floor never exceeds the "
          "float truth (%d exceed) and sits within rel %.2e <= %.0e "
          "of it" % (n_exceed, d_gapc, CERT_GAP_RTOL),
          n_exceed == 0 and d_gapc <= CERT_GAP_RTOL, kill="K2")
    check("C3 exact Chebyshev monic coefficients == float Lanczos "
          "(al, be = bet^2): max rel %.2e <= %.0e"
          % (d_coef, COEF_TIE), d_coef <= COEF_TIE, kill="K2")
    check("C4 exact-rational Radau value == float route at the "
          "certified floor: max rel %.2e <= %.0e (%d degenerate)"
          % (d_xr, XR_TIE, n_degen),
          d_xr <= XR_TIE and n_degen == 0, kill="K2")
    check("C5 RB1 the EXACT Radau value is an upper bound for the "
          "truth q on every cell: %d violations" % sign_fail,
          sign_fail == 0, kill="K2")
    check("C6 node ward at the certified floor: %d rules with a "
          "node below the floor" % node_fail, node_fail == 0,
          kill="K2")
    check("C7 interval cross-tier (E5, refuse-only) at the required "
          "floor: %d confirmed, %d REFUSED-WIDTH, 0 denials possible"
          % (iv_conf, iv_ref), True)
    check("C8 CLOSING CENSUS: certified sigma-bound <= TARGET %.4f "
          "on %d/%d cells; < t*_pos %.4f on %d/%d cells"
          % (float(TARGET), n_close_t, len(rows), float(TSTAR_POS),
             n_close_ts, len(rows)), True)
    return n_close_t, n_close_ts


def print_table(rows):
    print("\n    THE CERTIFIED FLOOR TABLE (68 ladder + F0 cells):")
    print("    idx seg    kz    h      n_pivot   lamB_meas  "
          "c_req      c_cert     slack      bound_cert  vs TARGET")
    for row in rows:
        creq = row.get("c_req", float("nan"))
        cc = row.get("c_cert_f", float("nan"))
        bf = row.get("bound_f", float("nan"))
        slack = (cc - creq if math.isfinite(creq)
                 and math.isfinite(cc) else float("nan"))
        print("    %3d %-6s %-4d %6.0f %9.4f %10.6f %10.6f %10.6f "
              "%10.6f %11.6f  %s"
              % (row["index"], row["seg"], row["kz"], row["h"],
                 row["n_piv"], row["lam_b"], creq, cc, slack, bf,
                 "CLOSE" if row.get("closes_t") else "FAIL"))


# ================================================ X: the controls
def controls(rows):
    section("X -- controls-must-fire (the certification is not "
            "vacuous)")
    idxs = [0, len(rows) // 2, len(rows) - 1][:CTRL_STEPS]
    n_fire = 0
    n_iv_ok = 0
    for i in idxs:
        row = rows[i]
        _p, _m, blkf = exact_wall_data(row["step"]["Mt"], 0)
        claim = Fraction(float(row["lam_b"] * CTRL_INFLATE))
        ok, piv_k = pd_exact(blkf, claim)
        if not ok:
            n_fire += 1
        got = chol_iv(np.asarray(row["step"]["Bblk"], float),
                      float(claim))
        if got is not True:
            n_iv_ok += 1
        print("    X1 cell %d: claimed floor %.6f > true "
              "lambda_min %.6f -> exact LDL %s (pivot %d), interval "
              "tier %s" % (row["index"], float(claim), row["lam_b"],
                           "REFUSED" if not ok else "ACCEPTED(!)",
                           piv_k,
                           "not certified" if got is not True
                           else "certified(!)"))
    check("X1 inflated floor claim REFUSED by the exact LDL on "
          "%d/%d declared cells" % (n_fire, len(idxs)),
          n_fire == len(idxs), kill="K4")
    check("X2 inflated floor claim NOT certified by the interval "
          "tier on %d/%d declared cells" % (n_iv_ok, len(idxs)),
          n_iv_ok == len(idxs), kill="K4")
    # exact-machine sanity on a synthetic diagonal with known spectrum
    dvals = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3),
             Fraction(1), Fraction(3, 2), Fraction(2), Fraction(3)]
    dfr = [[dvals[i] if i == j else Fraction(0) for j in range(7)]
           for i in range(7)]
    ok_at, _ = pd_exact(dfr, Fraction(1, 3))
    ok_below, _ = pd_exact(dfr, Fraction(1, 3) - Fraction(1, 2 ** 50))
    cert = cert_floor_exact(dfr, Fraction(0), Fraction(1, 2))
    gap = Fraction(1, 3) - cert
    check("X3 exact-machine sanity (known rational spectrum, min "
          "1/3): PD refused exactly AT 1/3 (%s), accepted just "
          "below (%s), certified floor gap %.3e in (0, 2^-30]"
          % (not ok_at, ok_below, float(gap)),
          (not ok_at) and ok_below and Fraction(0) < gap
          <= Fraction(1, 2 ** 30), kill="K4")
    # exact RB1 sanity: diagonal measure, q known exactly
    momv = [sum(dv ** k for dv in dvals) for k in range(2 * KDEG - 1)]
    q_true = sum(Fraction(1) / dv for dv in dvals)
    cheb = chebyshev_monic(momv, KDEG)
    val = (radau_exact(cheb[0], cheb[1], Fraction(1, 4), momv[0])
           if cheb else None)
    check("X4 exact RB1 sanity: Radau_%d at node 1/4 on the "
          "synthetic diagonal measure gives %.6f >= q = %.6f "
          "(EXACT Fraction comparison)"
          % (KDEG, float(val) if val is not None else float("nan"),
             float(q_true)),
          val is not None and val >= q_true, kill="K4")
    # census-can-fire: inflated coupling must FAIL the census
    row = rows[idxs[0]]
    mt2 = np.array(row["step"]["Mt"], float)
    mt2[0, 1:] *= CTRL_COUPLE
    mt2[1:, 0] *= CTRL_COUPLE
    pivf, momv2, blkf2 = exact_wall_data(mt2, 2 * KDEG - 2)
    c2 = cert_floor_exact(blkf2, Fraction(0),
                          Fraction(float(row["lam_b"])))
    cheb2 = chebyshev_monic(momv2, KDEG)
    v2 = (radau_exact(cheb2[0], cheb2[1], c2, momv2[0]) / pivf
          if (cheb2 and c2 is not None) else None)
    check("X5 census-can-fire: synthetic coupling x%.0f on cell %d "
          "gives certified bound %.4f > TARGET %.4f -> census FAILS "
          "there" % (CTRL_COUPLE, row["index"],
                     float(v2) if v2 is not None else float("nan"),
                     float(TARGET)),
          v2 is not None and v2 > TARGET, kill="K4")


# ============================================ S: the screens
def ch_surface_map(rows):
    """CCXVII c_h on matched surface terminators (CCLIII verbatim,
    labelled screen currency only)."""
    out = {}
    for kz in sorted({r["kz"] for r in rows
                      if r["seg"] in ("surf", "F0")}):
        rung = eul.level_rung(kz)
        if rung is None:
            continue
        dens = eul.grid_density(rung["c"])
        pos = eul.gram_from_dens(np.where(dens > 0.0, dens, 0.0),
                                 rung["M"])
        neg = eul.gram_from_dens(np.where(dens > 0.0, 0.0, -dens),
                                 rung["M"])
        last = pos.shape[0] - 1
        import scipy.linalg as sla
        top = float(sla.eigh(neg, pos, eigvals_only=True,
                             subset_by_index=[last, last])[0])
        out[int(kz)] = 1.0 - top
    return out


def screens(rows):
    section("S -- relocation screens (CCXLVII bars verbatim): are "
            "the certified margins tau or c_h in disguise?")
    ok_rows = [r for r in rows if r.get("bound_fr") is not None]
    taus = np.asarray([r["tau_scale"] for r in ok_rows], float)
    ch_map = ch_surface_map(ok_rows)
    chs = np.asarray([ch_map.get(r["kz"], float("nan"))
                      for r in ok_rows], float)
    bnd = np.asarray([r["bound_f"] for r in ok_rows], float)
    creq = np.asarray([r.get("c_req", float("nan"))
                       for r in ok_rows], float)
    ccrt = np.asarray([r["c_cert_f"] for r in ok_rows], float)
    series = (("certified bound", bnd),
              ("TARGET - bound (the census margin)",
               float(TARGET) - bnd),
              ("t*_pos - bound", float(TSTAR_POS) - bnd),
              ("floor slack c_cert - c_req", ccrt - creq))
    reloc = []
    for label, arr in series:
        t1, v1 = screen(arr, taus, "%s vs tau" % label)
        mask = np.isfinite(chs)
        t2, v2 = screen(arr[mask], chs[mask],
                        "%s vs CCXVII c_h" % label)
        print("      " + t1 + " | " + t2)
        if "RELOC" in (v1, v2):
            reloc.append(label)
    check("S1 tau / c_h relocation screens: relocation seats %s"
          % (",".join(reloc) or "none"), not reloc)
    hs = np.asarray([r["h"] for r in ok_rows], float)
    for label, arr in (("certified bound", bnd),
                       ("census margin", float(TARGET) - bnd)):
        pos = arr > 0
        if int(np.sum(pos)) >= 3:
            slope, two_se, r2, _a = linfit(np.log(hs[pos]),
                                           np.log(arr[pos]))
            print("    h-law of %s: log-log slope %+.4f +/- %.4f "
                  "(2SE), R^2 %.3f" % (label, slope, two_se, r2))


# =============================================================== main
def finish(rows, n_close_t, n_close_ts, n_infeas):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    lad = [r for r in rows if r["seg"] != "F0"]
    f0 = [r for r in rows if r["seg"] == "F0"]
    lad_close = sum(1 for r in lad if r.get("closes_t"))
    f0_close = sum(1 for r in f0 if r.get("closes_t"))
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    else:
        bmax_lad = max((r["bound_f"] for r in lad
                        if r.get("bound_fr") is not None),
                       default=float("nan"))
        bmax_f0 = max((r["bound_f"] for r in f0
                       if r.get("bound_fr") is not None),
                      default=float("nan"))
        if lad_close == len(lad) and f0_close == len(f0):
            v = ("BFLOOR-CERT-COMPOSED(%d/%d ladder + %d/%d F0 "
                 "cells close; ladder bound max %.4f, F0 bound max "
                 "%.4f, TARGET %.4f)"
                 % (lad_close, len(lad), f0_close, len(f0),
                    bmax_lad, bmax_f0, float(TARGET)))
        elif lad_close == len(lad):
            miss = [r for r in f0 if not r.get("closes_t")]
            v = ("BFLOOR-CERT-LADDER(%d/%d ladder cells close; F0 "
                 "shortfall on %d cells: %s)"
                 % (lad_close, len(lad), len(miss),
                    "; ".join("kz %d h %.0f bound %.4f"
                              % (r["kz"], r["h"],
                                 r.get("bound_f", float("nan")))
                              for r in miss[:4])))
        else:
            miss = [r for r in lad if not r.get("closes_t")]
            v = ("BFLOOR-CERT-PARTIAL(ladder shortfall on %d/%d "
                 "cells: %s)"
                 % (len(miss), len(lad),
                    "; ".join("%s kz %d h %.0f bound %.4f req %.4f "
                              "cert %.4f"
                              % (r["seg"], r["kz"], r["h"],
                                 r.get("bound_f", float("nan")),
                                 r.get("c_req", float("nan")),
                                 r.get("c_cert_f", float("nan")))
                              for r in miss[:4])))
        print("\n  VERDICT: %s" % v)
        if lad_close == len(lad):
            print("""
  THE COMPOSED CHAIN (stated loudly, premises typed).  For EVERY
  step of the deployed 68-step ladder%s:
    P1  n = M[0,0] > 0            EXACT-RATIONAL entry theorem
                                  (per step, this run)
    P2  lambda_min(B) >= c_step   EXACT-RATIONAL LDL theorem
                                  (round-62 machine, per step,
                                  this run; c_step in the table)
    P3  q <= RADAU_4(nu_0..nu_6; c_step)
                                  E3 theorem (Golub-Meurant,
                                  EXTERNAL-CITED); its hypothesis
                                  spec(B) in [c_step, inf) is
                                  DISCHARGED BY P2; the remainder
                                  sign is warded per cell (C5)
    P4  sigma = q/n <= bound      exact rational arithmetic
    =>  sigma <= %.6f (ladder max of the certified bounds)
        <= TARGET = %.4f < t*_pos = %.4f
    =>  s = (1 - sigma) n >= (1 - bound) n > 0
    =>  M is positive definite (E2 Schur, with B > 0 from P2).
  PEDIGREES, honestly typed: t*_pos = 0.8828 is a NUMERIC supremum
  (CCLXV pivot-positive map; an optimizer maximum is a LOWER bound
  of the true sup, so t*_num is an UPPER bound of the true closing
  threshold -- the rigor lane d7a7e574 is certifying it); SIGMA_ENV
  = 0.7809 is the CCLXIX REGISTERED numeric envelope; the moments
  and floors are exact dyadic rationals of the ASSEMBLED float64
  wall matrices (amendment A3: the float64-vs-ideal enclosure is
  the pg_chain interval program's open half, round 63 / CCXLI).
  SCOPE: the deployed ladder plus the tested F0 off-ladder cells;
  the cofinal claim is NOT included (registration/edge questions
  open); NO RH claim.""" % (
                (" AND every tested F0 cell"
                 if f0_close == len(f0) and f0 else ""),
                max((r["bound_f"] for r in lad
                     if r.get("bound_fr") is not None),
                    default=float("nan")),
                float(TARGET), float(TSTAR_POS)))
        else:
            print("""
  THE PRECISE SHORTFALL: the cells listed in the verdict fail the
  census -- for each, the certified floor c_cert (the best the
  exact tier can prove, within 2^-40 of the true lambda_min) is
  below the required floor c_req, i.e. the obstruction is the
  MATRIX (its true lambda_min is too small for the K = %d moment
  bound at TARGET %.4f), not the certification machinery.  %d
  cells are INFEASIBLE even at the measured floor.""" % (
                KDEG, float(TARGET), n_infeas))
    print("""
  HONEST FRAME.  Finite exact-rational and float64 statements about
  the deployed 68-step ladder artifact and the CCLXIX F0 off-ladder
  cells; the certified floors and bounds are per-step theorems about
  the ASSEMBLED float64 wall matrices; E3's remainder sign and E5's
  interval-Cholesky facts are external-cited and warded, never
  proved here.  NEVER an all-h statement.  No marker moves; no
  paper, ledger, website, manifest or verification file is touched;
  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.BFLOOR.PERSTEP.01 -- the certified "
            "per-step B-floor (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))
    print("    TARGET = min(%.4f - %.2f, %.4f - %.2f, %.4f) = %.4f"
          % (float(TSTAR_POS), float(T_MARGIN), float(TCLOSE_POS),
             float(T_MARGIN), float(SIGMA_ENV), float(TARGET)))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac1 = ast_scan_functions(CERT_FUNCS, DERIV_BANNED)
    check("S0.2 AC certificate-path functions carry no read, no "
          "eigensolver, no pivot read, no ladder identifier",
          not ac1, ",".join(sorted(set(ac1))), kill="K2")
    ac2 = ast_scan_functions(FLOAT_FUNCS, DERIV_BANNED)
    check("S0.3 AC float bound-path functions clean (CCLXV ban list "
          "verbatim)", not ac2, ",".join(sorted(set(ac2))),
          kill="K2")

    zones, steps, combined = build_ladder()
    if KILLS:
        return finish([], 0, 0, 0)
    artifact_key_ward(steps)
    f0_cells, n_f0_pick = build_f0(combined)
    if KILLS:
        return finish([], 0, 0, 0)
    rows = make_rows(steps, f0_cells)
    rows = jacobi_identity_wards(rows)
    if KILLS:
        return finish(rows, 0, 0, 0)
    pivot_ward(rows)
    repro_anchors(rows, n_f0_pick)
    if KILLS:
        return finish(rows, 0, 0, 0)
    radau_repro(rows)
    if KILLS:
        return finish(rows, 0, 0, 0)
    n_infeas = required_table(rows)
    n_close_t, n_close_ts = certification(rows)
    print_table(rows)
    controls(rows)
    screens(rows)
    return finish(rows, n_close_t, n_close_ts, n_infeas)


if __name__ == "__main__":
    sys.exit(main())
