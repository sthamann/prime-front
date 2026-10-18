#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zolotarev_ks_dual_probe -- PRIME.ONEBADMODE.KS.DUAL.01 probe B
(EXPLORATION ONLY, experiments/.  NO RH claim.  2026-08-12.)

THE FINITE ROBUST EXTREMAL PROBLEM THAT WOULD BE THE PROOF CONTRACT.
CCLIII built the exact bridge: every 8x8 wall step matrix M_h has a
Jacobi form J = J(a, b) (Lanczos of (M_h, e_0), 15 real parameters:
8 diagonal b_1..b_8, 7 positive off-diagonal a_1..a_7) with the SAME
spectrum and the SAME reads, and the KS/l2 currency of the ladder is
the Hilbert-Schmidt distance of consecutive Jacobi data.  CCXLVII/
CCXXV give the frozen rational separator R (fixed global m = 8
Zolotarev filter on [c_B, L]) with the machine-certified separator
facts R(x) >= 1 for x <= 0, R >= 0 on all of R, 0 <= R <= delta on
[c_B, L]; hence tr R(M) < 1 is an UNCONDITIONAL positivity
certificate.  This probe poses the dual question that would collapse
the h-quantifier to a single finite optimization:

    sup_{J in C_KS} tr R(J)  <  1 ?

where C_KS is a truth-envelope constraint class in the 15 Jacobi
parameters, frozen BEFORE the optimization.  If the supremum over the
WHOLE class is < 1 with fixed reserve, then EVERY wall matrix whose
Jacobi data lies in C_KS is positive-certified, and the remaining
all-h input is only 'wall Jacobi data stays in the frozen box' --
whose measured h-laws are flat (CCLIII: reserve h^+0.0215, carriers
h-flat, D ~ h^-0.278 +/- 0.277 compatible with flat).

THE CLASS C_KS (source-only; every constant's provenance printed at
freeze time; envelopes over ALL 68 truth steps = 40 surface + 1
bridge + 27 deep, so surface and deep are covered by ONE box).
 (i)   FROZEN BOX: for each of the 15 coordinates theta_i,
       theta_i in [min_truth - MARGIN_FRAC*w, max_truth +
       MARGIN_FRAC*w], w = truth envelope width (a-coordinates
       clipped at 0 from below).
 (ii)  KS/SUM-RULE ENVELOPES -- HONEST TRANSLATION, DISCLOSED: the
       mission names KS_bulk (1.830) and the three carriers COEF/GAP/
       SPREAD (CCXLV/CCLIII).  Those are functionals of the MEASURE
       chain of a rung (length h/2), NOT functions of the 15 wall
       parameters, and CCLIII K4(iii) measured the measure->wall link
       NULL (corr -0.022).  The source-only translation used here
       evaluates the SAME functional forms on the wall Jacobi data
       over the separator's own certified domain [0, L] (affine map
       x -> (2x - L)/L, Jacobi normalization A_k = 4 a_k / L,
       B_k = (4 b_k - 2L)/L, free reference A = 1, B = 0; c_B and L
       are the frozen CCXXV filter constants):
         KS_wall   = sum (A_k - 1)^2 + sum B_k^2      <= max*(1+MARGIN)
         COEF_wall = sum log A_k - (1/2) log 2         in truth band
         SPREAD_wall = -(1/2) <log(8 w_k)>_k           in truth band
       with w_k the spectral weights of J at e_0 (the 8-atom wall
       measure).  GAP_wall = (1/2) f log f is IDENTICALLY 0 at 8
       atoms (all 8 eigenvalues present, f = 1) and is dropped as
       vacuous -- disclosed, not hidden.  All bands are truth
       envelopes widened by MARGIN_FRAC.
 (iii) STRUCTURE: a_k > 0 (Jacobi positivity); the certified B-floor
       TRANSLATES EXACTLY: the Lanczos frame has first vector e_0, so
       the trailing 7x7 Jacobi block J_B = J(a_2..a_7, b_2..b_8) is
       the compression of M onto e_0-perp -- orthogonally similar to
       the CCVII B-part -- hence lambda_min(J_B) = lamB1 exactly
       (warded per step) and the premise floor becomes
       lambda_min(J_B) >= c_B = 5523/10000 (CITED CLIII; if any truth
       rung sat below it the floor would be widened to the measured
       minimum and disclosed); spectral radius: spec(J) in [-L, L]
       with the source-only L = max_h L_src (CCVII
       min(Gershgorin, Frobenius)*(1+2^-40), global max = the frozen
       CCXXV filter L).
 ANTI-CIRCULARITY: the class is built from truth ENVELOPES only,
 never per-h data; the objective and every constraint are functions
 of theta alone (AC-scanned: no tau / reserve / margin / read / h
 identifier in the class functions); the optimizer never sees h.
 The class deliberately does NOT constrain the Schur gap
 s = b_1 - a_1^2 [J_B^-1]_11 or any positivity surrogate: encoding
 s > 0 would assume exactly what tr R < 1 is supposed to prove.

MEMBERSHIP WARDS (the class's reason to exist).
 N1 all 68 truth Jacobi data lie IN C_KS (census; the box is built
    from them, so the informative content is the B-floor / radius /
    functional-cap slacks, printed per constraint).
 X  the falsifying worlds lie OUTSIDE: per CCLIII C2 coordinates
    M_world = sym(Q_truth^T (S_world / tau_truth) Q_truth) for smooth
    and scramble (seed 1), census per world with the EXCLUDING
    constraint named per rung; a rung whose aligned matrix leaves
    float64 is typed REPRESENTATION-BREAK (counts as excluded,
    disclosed separately).  THE DECISIVE HONESTY CHECK: if a control
    world sits INSIDE the class AND has tr R >= 1, the class is
    USELESS as a proof vehicle -> verdict CLASS-USELESS, reported
    prominently, dominating every other outcome.

THE OPTIMIZATION.
 O0 OPT-POWER CONTROL (controls-must-fire for the machinery): on a
    DECLARED control box with the b_1 interval extended to include
    OPT_CTRL_B1 = -1 (all other constraints unchanged), the optimizer
    MUST reach tr R >= 1 (a matrix with a diagonal entry <= 0 is not
    PD, so the target provably exists there).  Silence -> the search
    is too weak to trust a CLOSES answer -> kill.
 O1 STAGE 1, numeric global: multi-start SLSQP (N_MS starts: truth
    points, one-bad-mode corner seeds b_1 -> box-low / a_1 -> box-
    high, and seeded uniform box samples) plus differential evolution
    on the penalized objective (declared seed, penalty weight PEN_W
    on squared normalized constraint violations), DE incumbent
    polished by SLSQP.  THE NUMBER: sup tr R (best feasible found;
    a numeric maximum is a LOWER bound on the true supremum -- typed
    honestly) and the reserve 1 - sup.
 O2 STAGE 2, rigor tier at the incumbent: the incumbent is rounded to
    the dyadic grid 2^-QBITS and re-verified -- box/a>0/B-floor/
    radius by EXACT rational arithmetic (Fraction pivots of the
    leading-minor elimination; c_B = 5523/10000 exact), the three
    functional caps by float evaluation with declared pad FUNC_PAD
    (typed FLOAT-PADDED); if the rounded incumbent is exactly NOT
    positive-definite (some leading principal minor <= 0, Sylvester),
    then by the CCXXV-certified separator facts tr R >= 1 EXACTLY:
    rigor type WITNESS-RATIONAL-EXACT.  If the incumbent stays PD,
    the stage-2 type is NUMERIC(point) -- no 15-dimensional interval
    branch-and-bound fits the budget, and a CLOSES verdict is
    therefore typed NUMERIC-GLOBAL, never certified.
 O3 STAGE 3, reported-only next-constraint preview: if the verdict is
    GAP, the named next source-only constraint candidate is the truth
    envelope of the SCHUR QUOTIENT sigma = a_1^2 [J_B^-1]_11 / b_1
    (measured on truth, cap max*(1+MARGIN)); the optimization is
    re-run with the sigma-cap added and the new best is REPORTED ONLY
    (typed MECHANISM-IMPORTING: a sigma-cap < 1 encodes the Schur
    positivity engine quantitatively, so it must be flagged, not
    silently adopted).

EXTERNAL-CITED (facts consumed, warded numerically, never proved
here).
 E1 Killip-Simon l2 class / sum rules: Killip & Simon, Ann. Math. 158
    (2003) 253-321.  Used as the name and the l2 norm of the wall
    currency (inherited from CCXLV/CCLIII); no spectral claim.
 E2 compression / Schur / Sylvester facts: for orthogonal Q with
    first column e_0, (Q^T M Q)[1:,1:] and M[1:,1:] are orthogonally
    similar compressions of M onto e_0-perp; a symmetric matrix is PD
    iff all leading principal minors are positive (Sylvester); Cauchy
    interlacing.  [Horn & Johnson, Matrix Analysis, 2nd ed., CUP
    2013, Sec. 4.3, 7.2, 0.8.5.]
 E3 the Zolotarev separator facts (R >= 1 on x <= 0, R >= 0 on R,
    R <= delta on [c_B, L]) are the CCXXV in-repo outward-rounded
    interval certificates of zolotarev_phase_filter_probe.build_filter,
    re-consumed READ-ONLY (pedigree: Akhiezer, Theory of
    Approximation, Dover 1992, Ch. 9).
 E4 SLSQP / differential evolution are numerical search tools (SciPy);
    nothing rigorous is consumed from them -- rigor lives only in O2.

FROZEN PROTOCOL.
 S0 FIREWALL.  AST scan (banned zetazero / zetazeros / nzeros /
    primerange / isprime / primepi / nextprime / prevprime /
    factorint / primefactors); all predecessor probes READ-ONLY; RNG
    seats: the corpus scramble seed (inherited SCR_SEED = 1) and the
    DECLARED optimizer seed OPT_SEED (multistart + DE), nothing else.
    AC scan: the class functions (theta_matrices / ks_wall_functionals
    / class_slack_vector / sigma_quotient / tr_r_of_theta) contain no
    ladder or read identifier (tau, reserve, margin, trace_r, lu_read,
    assemble_step, build_rung, artifact, h).
 W  ladder rebuilt read-only (42 surface rungs, 68 = 40 + 1 + 27
    steps), fixed CCXXV global m=8 filter rebuilt from the source-only
    L and warded against the stored artifact (poles, residues, L);
    per-step LU partial-fraction trace_R / margin warded against the
    stored 68x8 artifact; eigen-route trace == LU trace; the scalar
    partial-fraction form == product form R at declared sample points;
    REPRO: reserve med vs CCXLVII 0.9195 and min vs 2.730e-2.
 B  the Jacobi translation warded per step: Lanczos form exists;
    b_1 == M[0,0], a_1 == ||M[1:,0]||; lambda_min(J_B) == lamB1 (the
    E2 exact translation); [J^-1]_00 * gap == 1 (CCLIII B5); the
    sigma identity b_1 (1 - sigma) == gap.
 G  class freeze: all constants printed with provenance + SHA-256 of
    the frozen box bytes BEFORE any optimization.
 N/X membership censuses as above.
 O  optimization as above.
 S  screens: per-step truth reserve and per-step minimal normalized
    class slack against step tau and CCXVII c_h (CCXLVII relocation
    bands inherited verbatim: PASS <= 0.30, RELOC >= 0.70).

KILLS: K1 pipeline -> PIPELINE-BROKEN; K2 ward/identity ->
WARD-BROKEN; K3 tier reproduction -> REPRO-BROKEN; K4 a required
control silent -> CONTROL-SILENT.

VERDICT (frozen enum, in dominance order):
 CLASS-USELESS(world; a control inside the class with tr R >= 1)
 KSDUAL-GAP(sup, maximizer anatomy: WHERE the class allows tr R >= 1,
   wall-like vs unphysical typing by KS distance to the truth ladder,
   active constraints, rigor type, named next constraint + preview)
 KSDUAL-CLOSES(reserve = 1 - sup >= RESERVE_FLOOR, rigor type
   NUMERIC-GLOBAL(...) -- the composed proof contract is then stated:
   every J in C_KS is positive-certified, truth lies in C_KS on all
   tested rungs, the remaining all-h input is 'wall Jacobi data stays
   in the frozen box', whose measured h-laws are flat)
 KSDUAL-MARGINAL(0 < reserve < RESERVE_FLOOR).
Every enum is a finite float64/rational statement about the deployed
ladder and the frozen class; NEVER an all-h statement, NEVER an RH
claim.

FROZEN BARS.  NDIM = 8; SURF_EXP = 42; STEPS_EXP = 68; LU_TIE = 2e-9;
PF_TIE = 2e-8; TRANSLATE_TIE = 1e-8; MZERO_TIE = 1e-7;
REPRO_RTOL = 5e-2; RES_MED_REF = 0.9195; RES_MIN_REF = 2.730e-2;
MARGIN_FRAC = 0.10; FEAS_TOL = 1e-9 (normalized slacks);
RESERVE_FLOOR = 1e-2; N_MS = 48 (16 truth + 16 corner + 16 random;
smoke 8); SLSQP_MAXIT = 150; DE_POP = 20; DE_MAXITER = 350 (smoke
40); OPT_SEED = 20260812; PEN_W = 1e4; QBITS = 12; FUNC_PAD = 1e-6;
OPT_CTRL_B1 = -1.0; OPT_CTRL_BAR = 1.0; R_SAMPLE_TIE = 2e-8;
SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; CTRL_MAJORITY = 0.5;
PREVIEW_MS = 16; PREVIEW_DE_MAXITER = 120; runtime cap 25 min.

SMOKE DISCLOSURE (2026-08-12, one smoke pass before the freeze;
 nothing below is a bar, and no bar, control, screen, enum or
 success rule was changed after the smoke).
 SMOKE-1 (contiguous 10-rung surface subset + 3 lowest deep rungs,
 19.4 s) ran 26/26 GREEN with no kills.  Honest readings:
 (i)   the smoke subset necessarily contains steps that are NOT
       steps of the fixed 68-step artifact (its own fake bridge,
       CCLIII's identical smoke phenomenon), one with NEGATIVE
       reserve -3.85 and lambda_min(J_B) = 0.0059 -- this single
       fake step drove BOTH the disclosed B-floor widening AND the
       smoke 'sup' of 4.8506 (a truth point of the subset ladder,
       not an optimizer discovery); T5 REPRO is smoke-bypassed by
       design and decides only on the frozen ladder, where CCXLVII's
       reserve minimum is 2.730e-2 > 0.
 (ii)  every translation ward sat at machine precision (b_1/a_1
       2.1e-18, lambda_min(J_B) == lamB1 9.0e-14 rel, m(0) gap
       2.0e-15, sigma identity 2.0e-16), and the artifact/eigen/
       partial-fraction ties were 0.0 / 1.2e-15 / 6.7e-16.
 (iii) the smoke box already shows the decisive geometry: the b_1
       truth envelope crosses zero after the margin (box-low -0.28),
       so the box alone admits a nonpositive diagonal entry; the
       smoke optimizer reached 3.078 inside the class (OPT-POWER
       control fired at 3.057), both control worlds were excluded on
       every aligned rung (excluders B_floor / KS_wall), the smoke
       sigma-cap preview did NOT close (1.0073), and the smoke
       verdict was KSDUAL-GAP with stage-2 NUMERIC(point) (the
       incumbent, being a genuine subset-truth step, is PD).
 No code change was needed after SMOKE-1; the only edit between the
 smoke and the freeze is this disclosure text (SPEC SHA moves
 accordingly, disclosed).  The frozen run below is the run of
 record.

NO RH claim.  No marker moves; no paper, ledger, website, manifest or
verification file is touched; the only edit outside this file is the
German CCLXI line prepended to experiments/next.txt AFTER the frozen
summary.

Sources (read-only): onebadmode_moments_probe (CCVII ladder),
zolotarev_phase_filter_probe (CCXXV filter + artifact),
zolotarev_complex_tau_probe (CCXLVII reserve),
rhp_tier2_polecontrol_probe (CCLIII bridge; machinery reproduced
locally, cited), euler_phase_identity_probe (CCXVII c_h).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/zolotarev_ks_dual_probe.py --smoke
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/zolotarev_ks_dual_probe.py
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

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob         # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol    # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul      # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
NDIM = 8
SURF_EXP = 42
STEPS_EXP = 68
LU_TIE = 2.0e-9
PF_TIE = 2.0e-8
TRANSLATE_TIE = 1.0e-8
MZERO_TIE = 1.0e-7
REPRO_RTOL = 5.0e-2
RES_MED_REF = 0.9195
RES_MIN_REF = 2.730e-2
MARGIN_FRAC = 0.10
FEAS_TOL = 1.0e-9
RESERVE_FLOOR = 1.0e-2
N_MS = 48
SLSQP_MAXIT = 150
DE_POP = 20
DE_MAXITER = 350
OPT_SEED = 20260812
PEN_W = 1.0e4
QBITS = 12
FUNC_PAD = 1.0e-6
OPT_CTRL_B1 = -1.0
OPT_CTRL_BAR = 1.0
R_SAMPLE_TIE = 2.0e-8
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_MAJORITY = 0.5
PREVIEW_MS = 16
PREVIEW_DE_MAXITER = 120
CB_F = float(ob.CB_CITED)
SCRAMBLE_SEED = ob.SCR_SEED
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
# AC: identifiers that mark a construction as ladder/read-derived.
CLASS_BANNED = ("tau", "reserve", "margin", "trace_r", "trace_R",
                "lu_read", "assemble_step", "build_rung", "artifact",
                "h")

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
    """Lanczos tridiagonalization of (M, e_0) -- CCLIII machinery
    reproduced verbatim.  Returns (a, b, Q) or None."""
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


def ks_distance(a1, b1, a2, b2):
    """CCLIII KS l2 distance of two Jacobi data sets (verbatim)."""
    da = np.asarray(a2, float) - np.asarray(a1, float)
    db = np.asarray(b2, float) - np.asarray(b1, float)
    return math.sqrt(float(np.sum(db ** 2))
                     + 2.0 * float(np.sum(da ** 2)))


# ============================== the class functions (AC-scanned)
def theta_matrices(theta):
    """theta = (b_1..b_8, a_1..a_7) -> (J, J_B).  theta only."""
    bd = np.asarray(theta[:NDIM], float)
    ad = np.asarray(theta[NDIM:], float)
    jm = np.diag(bd)
    idx = np.arange(NDIM - 1)
    jm[idx, idx + 1] = ad
    jm[idx + 1, idx] = ad
    return jm, jm[1:, 1:]


def ks_wall_functionals(theta, cls):
    """Wall-side sum-rule functionals on [0, L] (disclosed
    translation; theta and frozen class constants only)."""
    bd = np.asarray(theta[:NDIM], float)
    ad = np.asarray(theta[NDIM:], float)
    ll = cls["L"]
    aa = 4.0 * ad / ll
    bb = (4.0 * bd - 2.0 * ll) / ll
    ks = float(np.sum((aa - 1.0) ** 2) + np.sum(bb ** 2))
    if np.any(aa <= 0.0):
        coef = -float("inf")
    else:
        coef = float(np.sum(np.log(aa))) - 0.5 * math.log(2.0)
    jm, _jb = theta_matrices(theta)
    try:
        evals, evecs = np.linalg.eigh(jm)
    except np.linalg.LinAlgError:
        return ks, coef, float("inf")
    ww = np.maximum(evecs[0, :] ** 2, 1e-300)
    spread = -0.5 * float(np.mean(np.log(NDIM * ww)))
    return ks, coef, spread


def class_slack_vector(theta, cls):
    """Normalized slack vector of C_KS at theta (>= 0 iff inside).
    theta and frozen class constants only; the optimizer and the
    censuses share this single definition."""
    theta = np.asarray(theta, float)
    lo, hi, wd = cls["lo"], cls["hi"], cls["wd"]
    out = []
    names = []
    for i in range(len(theta)):
        out.append((theta[i] - lo[i]) / wd[i])
        names.append("box_lo[%s]" % cls["coord"][i])
        out.append((hi[i] - theta[i]) / wd[i])
        names.append("box_hi[%s]" % cls["coord"][i])
    ad = theta[NDIM:]
    for k in range(NDIM - 1):
        out.append(ad[k] / wd[NDIM + k])
        names.append("a_pos[a%d]" % (k + 1))
    jm, jb = theta_matrices(theta)
    if np.all(np.isfinite(jm)):
        evj = np.linalg.eigvalsh(jm)
        evb = np.linalg.eigvalsh(jb)
        out.append((float(evb[0]) - cls["cb"]) / cls["cb"])
        names.append("B_floor")
        out.append((cls["L"] - float(evj[-1])) / cls["L"])
        names.append("radius_hi")
        out.append((float(evj[0]) + cls["L"]) / cls["L"])
        names.append("radius_lo")
    else:
        out.extend([-1.0, -1.0, -1.0])
        names.extend(["B_floor", "radius_hi", "radius_lo"])
    ks, coef, spread = ks_wall_functionals(theta, cls)
    out.append((cls["ks_cap"] - ks) / max(cls["ks_cap"], 1.0))
    names.append("KS_wall")
    out.append((coef - cls["coef_lo"]) / cls["coef_w"])
    names.append("COEF_lo")
    out.append((cls["coef_hi"] - coef) / cls["coef_w"])
    names.append("COEF_hi")
    out.append((spread - cls["spr_lo"]) / cls["spr_w"])
    names.append("SPREAD_lo")
    out.append((cls["spr_hi"] - spread) / cls["spr_w"])
    names.append("SPREAD_hi")
    return np.asarray(out, float), names


def sigma_quotient(theta):
    """Schur quotient sigma = a_1^2 [J_B^-1]_11 / b_1 (stage-3
    candidate; theta only)."""
    jm, jb = theta_matrices(theta)
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


def tr_r_of_theta(theta, fdata):
    """tr R(J(theta)) by the eigenvalue route (spectral function of
    theta; the frozen filter is a constant)."""
    jm, _jb = theta_matrices(theta)
    if not np.all(np.isfinite(jm)):
        return float("nan")
    evals = np.linalg.eigvalsh(jm)
    return math.fsum(zol.scalar_r(fdata, float(v)) for v in evals)


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
    return zones, steps


def get_filter(steps, artifact):
    poles_art = np.asarray([complex(*p)
                            for p in artifact["filter"]["poles"]],
                           complex)
    res_art = np.asarray(artifact["filter"]["residues"], float)
    l_art = float(artifact["filter"]["L"])
    global_l = (l_art if SMOKE
                else max(st["L_src"] for st in steps))
    fdata = zol.build_filter(CB_F, global_l, NDIM)
    dev_l = abs(global_l - l_art) / max(1.0, abs(global_l))
    dev_p = float(np.max(np.abs(fdata["poles"] - poles_art)
                         / np.maximum(1.0, np.abs(poles_art))))
    dev_r = float(np.max(np.abs(fdata["residues"] - res_art)
                         / np.maximum(1.0, np.abs(res_art))))
    check("T1 fixed CCXXV GLOBAL m=8 filter %s: L rel %.2e, poles "
          "%.2e, residues %.2e <= %.0e"
          % ("rebuilt from stored L (SMOKE)" if SMOKE
             else "rebuilt from source-only L",
             dev_l, dev_p, dev_r, LU_TIE),
          (artifact["filter"]["m"] == NDIM and dev_l <= LU_TIE
           and dev_p <= LU_TIE and dev_r <= LU_TIE), kill="K2")
    print("    separator facts (CCXXV interval certificates, "
          "re-consumed): global R lower %.3e >= 0 (outward), bulk "
          "delta %.6e on [c_B, L] = [%.6f, %.6g]"
          % (fdata["global_R_lower"], fdata["delta"], CB_F,
             fdata["L"]))
    return fdata


def translation(steps, artifact, fdata):
    section("T -- per-step reads: LU partial fractions vs artifact "
            "vs eigen route")
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]), int(r["kz"])):
              r for r in artifact["rungs"]}
    rows = []
    d_tr = d_marg = d_eig = 0.0
    n_match = 0
    for idx, st in enumerate(steps):
        key = (int(st["r1"]["h"]), int(st["r1"]["kz"]),
               int(st["r2"]["h"]), int(st["r2"]["kz"]))
        src = stored.get(key)
        trace_lu = zol.trace_filter_lu(st["Mt"], fdata)
        trace_eig = math.fsum(zol.scalar_r(fdata, float(v))
                              for v in st["eigs"])
        d_eig = max(d_eig, abs(trace_lu - trace_eig))
        if src is not None:
            n_match += 1
            d_tr = max(d_tr, abs(trace_lu - float(src["trace_R"])))
            d_marg = max(d_marg, abs((1.0 - trace_lu)
                                     - float(src["margin"])))
        rows.append(dict(index=idx, step=st, seg=ob.seg_of(st),
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]),
                         gap=float(st["gap"]),
                         trace_r=trace_lu,
                         reserve=1.0 - trace_lu,
                         matched=src is not None))
    check("T2 LU trace_R / margin reproduce the stored artifact on "
          "%d matched steps: %.2e / %.2e <= %.0e"
          % (n_match, d_tr, d_marg, LU_TIE),
          n_match >= 1 and d_tr <= LU_TIE and d_marg <= LU_TIE
          and (SMOKE or n_match == STEPS_EXP), kill="K2")
    check("T3 eigen-route trace == LU partial-fraction trace on all "
          "%d steps: max dev %.2e <= %.0e"
          % (len(rows), d_eig, PF_TIE), d_eig <= PF_TIE, kill="K2")
    xs_test = [-fdata["L"], -math.sqrt(CB_F * fdata["L"]), -CB_F,
               CB_F, math.sqrt(CB_F * fdata["L"]), fdata["L"]]
    d_pf = 0.0
    for x in xs_test:
        pf = 1.0 + 2.0 * math.fsum(
            float(rr) * x / (x * x + float(zz.imag) ** 2)
            for rr, zz in zip(fdata["residues"], fdata["poles"]))
        d_pf = max(d_pf, abs(pf - zol.scalar_r(fdata, x))
                   / max(1.0, abs(pf)))
    check("T4 scalar partial-fraction form == product form R at %d "
          "declared sample points: max rel %.2e <= %.0e"
          % (len(xs_test), d_pf, R_SAMPLE_TIE),
          d_pf <= R_SAMPLE_TIE, kill="K2")
    reserves = np.asarray([r["reserve"] for r in rows], float)
    med, mn = float(np.median(reserves)), float(np.min(reserves))
    ok_rep = (abs(med / RES_MED_REF - 1.0) <= REPRO_RTOL
              and abs(mn / RES_MIN_REF - 1.0) <= REPRO_RTOL)
    check("T5 REPRO CCXLVII: reserve med %.4f (ref %.4f), min %.4e "
          "(ref %.3e), rtol %.0e" % (med, RES_MED_REF, mn,
                                     RES_MIN_REF, REPRO_RTOL),
          SMOKE or ok_rep, kill="K3")
    print("    reserve = 1 - tr R: %s" % e3(reserves))
    return rows


# ============================= B: the Jacobi translation, warded
def jacobi_translation(rows):
    section("B -- the Jacobi translation of every step (the 15 "
            "coordinates), warded")
    d_b1 = d_a1 = d_bfl = d_m0 = d_sig = 0.0
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
        jm, jb = theta_matrices(theta)
        scale = max(1.0, float(np.max(np.abs(st["Mt"]))))
        d_b1 = max(d_b1, abs(b[0] - st["n0"]) / scale)
        d_a1 = max(d_a1, abs(a[0] - float(np.linalg.norm(st["bvec"])))
                   / scale)
        lamb = float(np.linalg.eigvalsh(jb)[0])
        d_bfl = max(d_bfl, abs(lamb - st["lamB1"])
                    / max(1.0, abs(st["lamB1"])))
        e0 = np.zeros(NDIM)
        e0[0] = 1.0
        m0 = float(np.linalg.solve(jm, e0)[0])
        d_m0 = max(d_m0, abs(m0 * row["gap"] - 1.0))
        sig = sigma_quotient(theta)
        d_sig = max(d_sig, abs(b[0] * (1.0 - sig) - row["gap"])
                    / max(1.0, abs(row["gap"])))
        row["sigma"] = sig
    check("B1 Lanczos form of (M_h, e_0) exists on all %d steps"
          % len(rows), n_bad == 0, "breakdowns %d" % n_bad,
          kill="K2")
    check("B2 TRANSLATE b_1 == M[0,0] and a_1 == ||M[1:,0]||: "
          "%.2e / %.2e <= %.0e" % (d_b1, d_a1, TRANSLATE_TIE),
          d_b1 <= TRANSLATE_TIE and d_a1 <= TRANSLATE_TIE, kill="K2")
    check("B3 TRANSLATE lambda_min(J_B) == lamB1 (E2 compression "
          "similarity; the certified B-floor lives in the Jacobi "
          "coordinates): max rel %.2e <= %.0e"
          % (d_bfl, TRANSLATE_TIE), d_bfl <= TRANSLATE_TIE,
          kill="K2")
    check("B4 WARD m(0) * gap == 1 (CCLIII B5): max %.2e <= %.0e"
          % (d_m0, MZERO_TIE), d_m0 <= MZERO_TIE, kill="K2")
    check("B5 WARD sigma identity b_1 (1 - sigma) == gap: max rel "
          "%.2e <= %.0e" % (d_sig, MZERO_TIE), d_sig <= MZERO_TIE,
          kill="K2")
    return [r for r in rows if r["theta"] is not None]


# ================================== G: freeze the class C_KS
COORD = tuple(["b%d" % (i + 1) for i in range(NDIM)]
              + ["a%d" % (i + 1) for i in range(NDIM - 1)])


def freeze_class(rows, fdata):
    section("G -- FREEZE the class C_KS (truth envelopes; every "
            "constant's provenance printed BEFORE the optimization)")
    thetas = np.asarray([r["theta"] for r in rows], float)
    t_lo = thetas.min(axis=0)
    t_hi = thetas.max(axis=0)
    width = np.maximum(t_hi - t_lo, 1e-12 * np.maximum(1.0,
                                                       np.abs(t_hi)))
    lo = t_lo - MARGIN_FRAC * width
    hi = t_hi + MARGIN_FRAC * width
    lo[NDIM:] = np.maximum(lo[NDIM:], 0.0)  # structural a > 0
    cb_use = CB_F
    lamb_min = min(float(np.linalg.eigvalsh(
        theta_matrices(r["theta"])[1])[0]) for r in rows)
    widened = False
    if lamb_min < CB_F:
        cb_use = lamb_min * (1.0 - MARGIN_FRAC)
        widened = True
        print("    WIDENED (disclosed): measured truth "
              "lambda_min(J_B) = %.6f < cited c_B = %.6f; floor "
              "honestly widened to %.6f" % (lamb_min, CB_F, cb_use))
    cls = dict(lo=lo, hi=hi, wd=hi - lo, cb=cb_use, L=fdata["L"],
               coord=COORD)
    funcs = np.asarray([ks_wall_functionals(r["theta"], cls)
                        for r in rows], float)
    ks_max = float(np.max(funcs[:, 0]))
    coef_lo_t, coef_hi_t = float(np.min(funcs[:, 1])), \
        float(np.max(funcs[:, 1]))
    spr_lo_t, spr_hi_t = float(np.min(funcs[:, 2])), \
        float(np.max(funcs[:, 2]))
    coef_w = max(coef_hi_t - coef_lo_t, 1e-12)
    spr_w = max(spr_hi_t - spr_lo_t, 1e-12)
    cls.update(ks_cap=ks_max * (1.0 + MARGIN_FRAC),
               coef_lo=coef_lo_t - MARGIN_FRAC * coef_w,
               coef_hi=coef_hi_t + MARGIN_FRAC * coef_w,
               coef_w=coef_w,
               spr_lo=spr_lo_t - MARGIN_FRAC * spr_w,
               spr_hi=spr_hi_t + MARGIN_FRAC * spr_w,
               spr_w=spr_w)
    print("    PROVENANCE: box = per-coordinate truth envelope over "
          "%d steps +/- %.2f * width; c_B = 5523/10000 CITED CLIII "
          "(%s); L = %.8g = CCXXV frozen filter L (source-only "
          "max L_src); KS_wall/COEF/SPREAD = wall-side sum-rule "
          "functionals on [0, L] (disclosed translation; GAP_wall "
          "vacuous at 8 atoms, dropped); caps = truth envelopes "
          "+/- %.2f * width." % (len(rows), MARGIN_FRAC,
                                 "WIDENED" if widened else
                                 "holds on all steps",
                                 fdata["L"], MARGIN_FRAC))
    print("    coord        truth_min      truth_max       box_lo"
          "         box_hi")
    for i, cn in enumerate(COORD):
        print("    %-5s %14.6g %14.6g %14.6g %14.6g"
              % (cn, t_lo[i], t_hi[i], lo[i], hi[i]))
    print("    KS_wall truth max %.6f -> cap %.6f" % (ks_max,
                                                      cls["ks_cap"]))
    print("    COEF_wall truth [%.6f, %.6f] -> box [%.6f, %.6f]"
          % (coef_lo_t, coef_hi_t, cls["coef_lo"], cls["coef_hi"]))
    print("    SPREAD_wall truth [%.6f, %.6f] -> box [%.6f, %.6f]"
          % (spr_lo_t, spr_hi_t, cls["spr_lo"], cls["spr_hi"]))
    frozen = np.concatenate([lo, hi,
                             [cls["cb"], cls["L"], cls["ks_cap"],
                              cls["coef_lo"], cls["coef_hi"],
                              cls["spr_lo"], cls["spr_hi"]]])
    box_sha = hashlib.sha256(frozen.tobytes()).hexdigest()
    check("G1 class frozen BEFORE optimization (box SHA-256 %s%s)"
          % (box_sha[:16], "; B-floor WIDENED, disclosed"
             if widened else ""), True)
    cls["box_sha"] = box_sha
    cls["widened"] = widened
    return cls


def membership_census(rows, cls):
    section("N -- membership census: all truth steps IN the class")
    slack_rows = []
    n_in = 0
    worst = {}
    for r in rows:
        sl, names = class_slack_vector(r["theta"], cls)
        r["slack_min"] = float(np.min(sl))
        slack_rows.append(sl)
        if r["slack_min"] >= -FEAS_TOL:
            n_in += 1
        j = int(np.argmin(sl))
        worst.setdefault(names[j], 0)
        worst[names[j]] += 1
    slack_rows = np.asarray(slack_rows, float)
    _sl, names = class_slack_vector(rows[0]["theta"], cls)
    per_min = slack_rows.min(axis=0)
    order = np.argsort(per_min)
    print("    tightest constraints across the truth ladder "
          "(min normalized slack):")
    for j in order[:6]:
        print("      %-14s %.6e" % (names[j], per_min[j]))
    check("N1 truth membership %d/%d steps IN C_KS (min slack %s)"
          % (n_in, len(rows), e3([r["slack_min"] for r in rows])),
          n_in == len(rows), kill="K2")
    return names


def control_census(zones, rows, cls, fdata):
    section("X -- the falsifying worlds must lie OUTSIDE the class")
    truth_by_kz = {r["kz"]: r for r in rows if r["seg"] == "surf"}
    useless = []
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
        if world == "smooth":
            check("X1 C1 SMOOTH violates the wall target (negA > 0) "
                  "on %d/%d surface rungs" % (wall_fire, len(ladder)),
                  wall_fire == len(ladder), kill="K4")
        n_align = n_out = n_break = n_in = 0
        excl = {}
        inside_tr = []
        for kz, ctl in ladder:
            tr = truth_by_kz.get(kz)
            if tr is None or ctl is None or not ctl.get("core_ok"):
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
            theta_w = np.concatenate([jf[1], jf[0]])
            sl, names = class_slack_vector(theta_w, cls)
            if float(np.min(sl)) >= -FEAS_TOL:
                n_in += 1
                trw = tr_r_of_theta(theta_w, fdata)
                inside_tr.append((kz, trw))
                if trw >= 1.0:
                    useless.append((world, kz, trw))
            else:
                n_out += 1
                j = int(np.argmin(sl))
                excl.setdefault(names[j], 0)
                excl[names[j]] += 1
        fire = (n_out + n_break) > CTRL_MAJORITY * max(n_align, 1)
        fired.append(fire)
        top = sorted(excl.items(), key=lambda kv: -kv[1])[:4]
        print("    %-9s aligned %d = OUT %d + REPRESENTATION-BREAK "
              "%d + INSIDE %d; excluding constraint census: %s"
              % (world, n_align, n_out, n_break, n_in,
                 ", ".join("%s x%d" % kv for kv in top) or "none"))
        for kz, trw in inside_tr:
            print("      INSIDE rung kz %d: tr R = %.6f %s"
                  % (kz, trw, "<- tr R >= 1, CLASS-USELESS SEAT"
                     if trw >= 1.0 else "(tr R < 1)"))
        check("X2 class-exclusion census %s: OUT+BREAK %d/%d aligned "
              "(majority bar) -> %s"
              % (world, n_out + n_break, n_align,
                 "FIRE" if fire else "SILENT"), fire, kill="K4")
    return useless


# ============================== O: the optimization (stage 1-3)
def make_objective(cls, fdata, extra_con=None):
    def neg_f(theta):
        v = tr_r_of_theta(theta, fdata)
        return -v if math.isfinite(v) else 1e12

    def slacks(theta):
        sl, _names = class_slack_vector(theta, cls)
        if extra_con is not None:
            sl = np.concatenate([sl, [extra_con(theta)]])
        return sl

    def penalized(theta):
        v = tr_r_of_theta(theta, fdata)
        if not math.isfinite(v):
            return 1e12
        sl = slacks(theta)
        viol = float(np.sum(np.clip(-sl, 0.0, None)))
        return -v + PEN_W * viol * viol
    return neg_f, slacks, penalized


def run_stage1(rows, cls, fdata, label, n_ms, de_maxiter,
               extra_con=None, box=None):
    lo = cls["lo"] if box is None else box[0]
    hi = cls["hi"] if box is None else box[1]
    bounds = list(zip(lo, hi))
    neg_f, slacks, penalized = make_objective(cls, fdata, extra_con)
    rng = np.random.default_rng(OPT_SEED)
    thetas = [r["theta"] for r in rows]
    seeds = []
    idx = np.linspace(0, len(thetas) - 1,
                      max(2, n_ms // 3)).astype(int)
    for i in sorted(set(idx.tolist())):
        seeds.append(np.clip(thetas[i], lo, hi))
    for i in sorted(set(idx.tolist())):
        cn = np.clip(thetas[i], lo, hi).copy()
        cn[0] = lo[0] + 1e-9 * (hi[0] - lo[0])       # b_1 -> low
        cn[NDIM] = hi[NDIM] - 1e-9 * (hi[NDIM] - lo[NDIM])  # a_1 hi
        seeds.append(cn)
    while len(seeds) < n_ms:
        seeds.append(rng.uniform(lo, hi))
    cons = [dict(type="ineq", fun=slacks)]
    best_v, best_t = -float("inf"), None
    n_conv = 0
    for sd in seeds[:n_ms]:
        try:
            res = optimize.minimize(neg_f, sd, method="SLSQP",
                                    bounds=bounds, constraints=cons,
                                    options=dict(maxiter=SLSQP_MAXIT,
                                                 ftol=1e-12))
        except (ValueError, OverflowError):
            continue
        th = np.clip(res.x, lo, hi)
        if float(np.min(slacks(th))) >= -FEAS_TOL:
            n_conv += 1
            v = tr_r_of_theta(th, fdata)
            if v > best_v:
                best_v, best_t = v, th
    de = optimize.differential_evolution(
        penalized, bounds=bounds, seed=OPT_SEED, maxiter=de_maxiter,
        popsize=DE_POP, polish=False, tol=1e-10, init="sobol")
    th_de = np.clip(de.x, lo, hi)
    try:
        res = optimize.minimize(neg_f, th_de, method="SLSQP",
                                bounds=bounds, constraints=cons,
                                options=dict(maxiter=SLSQP_MAXIT,
                                             ftol=1e-12))
        th_pol = np.clip(res.x, lo, hi)
    except (ValueError, OverflowError):
        th_pol = th_de
    for th in (th_de, th_pol):
        if float(np.min(slacks(th))) >= -FEAS_TOL:
            v = tr_r_of_theta(th, fdata)
            if v > best_v:
                best_v, best_t = v, th
    print("    %s: best feasible tr R = %.6f (feasible SLSQP "
          "starts %d/%d; DE best penalized %.6f) [%.1f s]"
          % (label, best_v, n_conv, n_ms, -de.fun,
             time.time() - T0), flush=True)
    return best_v, best_t, slacks


# --------------------------- stage 2: rational witness machinery
def frac_first_bad_pivot(mfrac):
    """Pivot-free Gaussian elimination over Q.  Returns None if all
    pivots > 0 (matrix PD, Sylvester), else the 1-based index of the
    first nonpositive pivot (leading minor <= 0 -> not PD)."""
    n = len(mfrac)
    m = [row[:] for row in mfrac]
    for k in range(n):
        if m[k][k] <= 0:
            return k + 1
        for i in range(k + 1, n):
            f = m[i][k] / m[k][k]
            for j in range(k, n):
                m[i][j] -= f * m[k][j]
    return None


def rational_witness(theta, cls, fdata):
    """Round to dyadic 2^-QBITS; exact class membership for box /
    a>0 / B-floor / radius; float-padded functional caps; exact
    not-PD test.  Returns (type_string, details)."""
    scale = 2 ** QBITS
    th_r = np.round(np.asarray(theta, float) * scale) / scale
    exact_ok = True
    reasons = []
    lo, hi = cls["lo"], cls["hi"]
    for i in range(len(th_r)):
        if not (Fraction(float(lo[i])) <= Fraction(float(th_r[i]))
                <= Fraction(float(hi[i]))):
            exact_ok = False
            reasons.append("box[%s]" % COORD[i])
    if any(Fraction(float(v)) <= 0 for v in th_r[NDIM:]):
        exact_ok = False
        reasons.append("a>0")
    bf = [Fraction(float(v)) for v in th_r[:NDIM]]
    af = [Fraction(float(v)) for v in th_r[NDIM:]]
    cbf = (Fraction(5523, 10000) if not cls["widened"]
           else Fraction(float(cls["cb"])))
    lf = Fraction(float(cls["L"]))

    def jac_frac(bd, ad, shift, sign):
        n = len(bd)
        m = [[Fraction(0)] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = sign * bd[i] + shift
            if i + 1 < n:
                m[i][i + 1] = sign * ad[i]
                m[i + 1][i] = sign * ad[i]
        return m
    if frac_first_bad_pivot(jac_frac(bf[1:], af[1:], -cbf, 1)) \
            is not None:
        exact_ok = False
        reasons.append("B_floor")
    if frac_first_bad_pivot(jac_frac(bf, af, lf, -1)) is not None:
        exact_ok = False
        reasons.append("radius_hi")
    if frac_first_bad_pivot(jac_frac(bf, af, lf, 1)) is not None:
        exact_ok = False
        reasons.append("radius_lo")
    ks, coef, spread = ks_wall_functionals(th_r, cls)
    for nm, val, lo_v, hi_v in (
            ("KS_wall", ks, None, cls["ks_cap"]),
            ("COEF", coef, cls["coef_lo"], cls["coef_hi"]),
            ("SPREAD", spread, cls["spr_lo"], cls["spr_hi"])):
        if hi_v is not None and val > hi_v - FUNC_PAD * abs(hi_v):
            exact_ok = False
            reasons.append(nm + "_pad")
        if lo_v is not None and val < lo_v + FUNC_PAD * abs(lo_v):
            exact_ok = False
            reasons.append(nm + "_pad")
    bad = frac_first_bad_pivot(jac_frac(bf, af, Fraction(0), 1))
    tr_r = tr_r_of_theta(th_r, fdata)
    if exact_ok and bad is not None:
        return ("WITNESS-RATIONAL-EXACT", dict(
            theta=th_r, minor=bad, tr=tr_r,
            note="rounded incumbent IN C_KS (box/a>0/B-floor/radius "
                 "RATIONAL-EXACT, functional caps FLOAT-PADDED) and "
                 "leading minor %d <= 0 -> not PD -> tr R >= 1 by "
                 "the certified separator facts" % bad))
    return ("NUMERIC(point)", dict(
        theta=th_r, minor=bad, tr=tr_r,
        note=("rounded incumbent %s; not-PD witness %s"
              % ("IN class" if exact_ok
                 else "leaves class at " + ",".join(reasons[:4]),
                 "found (minor %s)" % bad if bad is not None
                 else "absent (matrix PD)"))))


def maximizer_anatomy(theta, rows, cls, fdata, names):
    jm, jb = theta_matrices(theta)
    evj = np.linalg.eigvalsh(jm)
    rv = [zol.scalar_r(fdata, float(v)) for v in evj]
    sl, _ = class_slack_vector(theta, cls)
    active = [names[j] for j in range(len(sl)) if sl[j] <= 1e-6]
    dks = [ks_distance(theta[NDIM:], theta[:NDIM],
                       r["theta"][NDIM:], r["theta"][:NDIM])
           for r in rows]
    d_near = float(np.min(dks))
    d_cons = [ks_distance(rows[i]["theta"][NDIM:],
                          rows[i]["theta"][:NDIM],
                          rows[i + 1]["theta"][NDIM:],
                          rows[i + 1]["theta"][:NDIM])
              for i in range(len(rows) - 1)]
    d_env = float(np.max(d_cons))
    typing = ("WALL-LIKE" if d_near <= d_env else
              "UNPHYSICAL-CORNER")
    print("    maximizer anatomy:")
    print("      eigenvalues: %s" % "  ".join("%+.5g" % v
                                              for v in evj))
    print("      R(lambda_i): %s" % "  ".join("%.4g" % v
                                              for v in rv))
    print("      lambda_min(J_B) = %.6f (floor %.6f); b_1 = %.6g; "
          "a_1 = %.6g; sigma = %.6g"
          % (float(np.linalg.eigvalsh(jb)[0]), cls["cb"],
             theta[0], theta[NDIM], sigma_quotient(theta)))
    print("      active constraints (slack <= 1e-6): %s"
          % (", ".join(active[:10]) or "none"))
    print("      KS distance to nearest truth step %.4g vs max "
          "consecutive truth D %.4g -> %s" % (d_near, d_env, typing))
    return typing, active, d_near, d_env


def ch_surface_map(rows):
    """CCXVII c_h on matched surface terminators (CCLIII verbatim,
    labelled screen currency only)."""
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
    return out


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
        print("\n  VERDICT: %s" % " ; ".join(labels))
        print("""
  HONEST FRAME.  Finite float64/rational measurements on the deployed
  68-step ladder and ONE frozen truth-envelope class in the 15 wall
  Jacobi parameters.  A numeric maximum is a lower bound on the true
  supremum; only the rational witness tier is exact.  The class, the
  filter and every constant are frozen before the optimization; the
  optimizer never sees h.  No marker moves; no paper, ledger,
  website, manifest or verification file is touched; NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.KS.DUAL.01 probe B -- the finite "
            "robust extremal problem sup_{J in C_KS} tr R(J) "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac = ast_scan_functions(("theta_matrices", "ks_wall_functionals",
                             "class_slack_vector", "sigma_quotient",
                             "tr_r_of_theta"), CLASS_BANNED)
    check("S0.2 AC the class/objective functions contain no ladder "
          "or read identifier (class from envelopes; optimizer "
          "never sees h)", not ac, ",".join(sorted(set(ac))),
          kill="K2")
    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    check("S0.3 CCXLVII artifact schema/dimensions fixed",
          (artifact["schema"] == "tfpt.zolotarev_phase_filter.v1"
           and len(artifact["rungs"]) == STEPS_EXP
           and artifact["filter"]["m"] == NDIM), kill="K1")

    zones, steps = build_ladder()
    if KILLS:
        return finish([])
    fdata = get_filter(steps, artifact)
    rows = translation(steps, artifact, fdata)
    if KILLS:
        return finish([])
    rows = jacobi_translation(rows)
    if KILLS:
        return finish([])

    cls = freeze_class(rows, fdata)
    names = membership_census(rows, cls)
    if KILLS:
        return finish([])
    useless = control_census(zones, rows, cls, fdata)
    if KILLS:
        return finish([])

    # ---- O0 the OPT-POWER control
    section("O -- THE OPTIMIZATION: sup tr R over C_KS")
    n_ms = 8 if SMOKE else N_MS
    de_it = 40 if SMOKE else DE_MAXITER
    ctrl_lo = cls["lo"].copy()
    ctrl_lo[0] = min(ctrl_lo[0], OPT_CTRL_B1)
    ctrl_cls = dict(cls)
    ctrl_cls["lo"] = ctrl_lo
    ctrl_cls["wd"] = cls["hi"] - ctrl_lo
    v_ctrl, _t_ctrl, _ = run_stage1(
        rows, ctrl_cls, fdata, "O0 OPT-POWER control (b_1 extended "
        "to %.1f)" % OPT_CTRL_B1, max(8, n_ms // 2), max(40, de_it // 4))
    check("O0 CONTROL the optimizer reaches tr R >= %.1f on the "
          "declared control box: best %.4f" % (OPT_CTRL_BAR, v_ctrl),
          v_ctrl >= OPT_CTRL_BAR, kill="K4")
    if KILLS:
        return finish([])

    # ---- O1 stage 1
    sup1, theta1, _sl = run_stage1(rows, cls, fdata,
                                   "O1 stage 1 (class)", n_ms, de_it)
    truth_best = max(r["trace_r"] for r in rows)
    sup = max(sup1, truth_best)
    if theta1 is None or truth_best >= sup1:
        theta1 = rows[int(np.argmax([r["trace_r"]
                                     for r in rows]))]["theta"]
    reserve = 1.0 - sup
    check("O1 stage-1 supremum measured: sup tr R = %.6f, reserve "
          "1 - sup = %+.6f (truth ladder best %.6f)"
          % (sup, reserve, truth_best), True)
    typing, active, d_near, d_env = maximizer_anatomy(
        theta1, rows, cls, fdata, names)

    # ---- O2 stage 2 rigor
    rigor, details = rational_witness(theta1, cls, fdata)
    print("    stage-2 rigor: %s -- %s (tr R at rounded point "
          "%.6f)" % (rigor, details["note"], details["tr"]))
    check("O2 rigor tier typed %s" % rigor, True)

    # ---- O3 preview (reported-only)
    preview_txt = "not-run"
    if sup >= 1.0:
        sig_truth = [r["sigma"] for r in rows]
        sig_cap = float(np.max(sig_truth)) * (1.0 + MARGIN_FRAC)
        print("    O3 next-constraint candidate: SCHUR-QUOTIENT "
              "envelope sigma <= %.6f (truth %s; MECHANISM-"
              "IMPORTING, flagged)" % (sig_cap, e3(sig_truth)))

        def sig_con(theta):
            s = sigma_quotient(theta)
            if not math.isfinite(s) or theta[0] <= 0.0:
                return -1.0
            return (sig_cap - s) / max(abs(sig_cap), 1e-6)
        v_prev, t_prev, _ = run_stage1(
            rows, cls, fdata, "O3 preview (sigma-cap added)",
            PREVIEW_MS if not SMOKE else 6,
            PREVIEW_DE_MAXITER if not SMOKE else 30,
            extra_con=sig_con)
        preview_txt = ("sigma-cap %.4f -> best tr R %.6f (%s)"
                       % (sig_cap, v_prev,
                          "still >= 1, cap does NOT close"
                          if v_prev >= 1.0 else
                          "closes numerically under the cap"))
        print("    O3 REPORTED-ONLY: %s" % preview_txt)
    check("O3 next-constraint preview typed (reported-only): %s"
          % preview_txt, True)

    # ---- S screens
    section("S -- relocation screens (CCXLVII bars inherited)")
    taus = np.asarray([r["tau_scale"] for r in rows], float)
    ch_map = ch_surface_map(rows)
    chs = np.asarray([ch_map.get(r["kz"], float("nan"))
                      for r in rows], float)
    reloc = []
    for label, arr in (("reserve", np.asarray([r["reserve"]
                                               for r in rows])),
                       ("class-slack-min",
                        np.asarray([r["slack_min"] for r in rows]))):
        t1, v1 = screen(arr, taus, "%s vs step tau" % label)
        mask = np.isfinite(chs)
        t2, v2 = screen(arr[mask], chs[mask],
                        "%s vs CCXVII c_h" % label)
        print("      " + t1 + " | " + t2)
        if "RELOC" in (v1, v2):
            reloc.append(label)
    check("S1 tau/c_h relocation screens: relocation seats %s"
          % (",".join(reloc) or "none"), not reloc)

    # ---- verdict
    if useless:
        w, kz, trw = useless[0]
        labels = ["CLASS-USELESS(%s world INSIDE the class at kz %d "
                  "with tr R = %.4f >= 1 -- the class cannot be the "
                  "proof vehicle)" % (w, kz, trw)]
    elif sup >= 1.0:
        labels = [
            "KSDUAL-GAP(sup tr R = %.4f >= 1; maximizer %s, "
            "KS-dist to truth %.3g vs envelope %.3g; active: %s; "
            "rigor %s; NEXT-CONSTRAINT sigma-envelope: %s)"
            % (sup, typing, d_near, d_env,
               ",".join(active[:6]) or "interior", rigor,
               preview_txt)]
    elif reserve >= RESERVE_FLOOR:
        labels = [
            "KSDUAL-CLOSES(reserve %.4f, rigor NUMERIC-GLOBAL("
            "multistart+DE, %d starts) -- COMPOSED PROOF CONTRACT: "
            "every J in C_KS is positive-certified by the frozen "
            "separator, truth lies in C_KS on all %d tested rungs, "
            "and the remaining all-h input is 'wall Jacobi data "
            "stays in the frozen box', whose measured h-laws are "
            "flat (CCLIII); NOT interval-certified over the class)"
            % (reserve, n_ms, len(rows))]
    else:
        labels = ["KSDUAL-MARGINAL(reserve %.4e < floor %.0e)"
                  % (reserve, RESERVE_FLOOR)]
    return finish(labels)


if __name__ == "__main__":
    raise SystemExit(main())
