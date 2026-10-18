#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""highpole_relative_ks_radius_probe
PRIME.ONEBADMODE.KS.DUAL.01 -- Probe A (the simple radius check)

EXPLORATION ONLY.  NO RH claim.  Finite float64 measurements on the
deployed 68-step wall ladder; nothing here is an all-h statement.

THE CANDIDATE THEOREM (lead-derived; every step is re-derived and
warded below, nothing is trusted).  Let R be the frozen CCXXV m=8
rational separator

  R(x) = 1 + sum_j [a_j/(x - z_j) + a_j/(x - conj z_j)],
  z_j = i y_j purely imaginary, a_j real,

with the certified separator facts R >= 1 on x <= 0 and R >= 0 on all
of R (CCXXV interval enclosure), so that Phi := tr R(M) < 1 is an
unconditional positivity certificate for a symmetric 8x8 M.  Let J_h
be the Jacobi (Lanczos) form of (M~_h, e_0) on the ladder -- the
CCLIII bridge: Q orthogonal, Q^T M~_h Q = J_h, hence
tr R(J_h) = tr R(M~_h) =: Phi_h exactly.

STEP 1 (resolvent identity, exact and non-perturbative).  For
symmetric A, B and G_A = (A - z)^{-1}, G_B = (B - z)^{-1}:
  G_A - G_B = -G_A (A - B) G_B.
STEP 2 (trace bound).  With E = A - B,
  |tr(G_A E G_B)| = |tr(E G_B G_A)|
                  <= ||E||_HS ||G_B G_A||_HS
                  <= ||E||_HS ||G_B||_HS ||G_A||_op
                  <= ||E||_HS * (sqrt(8)/|Im z|) * (1/|Im z|).
The sqrt(8) is the dimensional conversion ||X||_HS <= sqrt(n)||X||_op
on n = 8, applied to ONE of the two resolvents; the op-norm bound
||(sym - z)^{-1}||_op <= 1/|Im z| needs self-adjointness.  This factor
is warded numerically: it must HOLD on random symmetric perturbations
across scales, and the deterministic family A = eps I, B = 0 attains
it in the eps -> 0 limit, so the factor-sqrt(8)-free variant MUST be
violated (a controls-must-fire ward on the constant itself).
STEP 3 (summation over the filter).  Phi_A - Phi_B =
2 sum_j a_j Re tr(G_A(z_j) - G_B(z_j)), hence

  |Phi_A - Phi_B| <= C_R ||A - B||_HS,
  C_R = 2 sqrt(8) sum_j |a_j| / y_j^2.

HIGH-POLE CLOSURE STATEMENT (the object under test).  Fix a frozen
reference J_star with delta_star := 1 - tr R(J_star) > 0.  If

  sup_h ||J_h - J_star||_HS < delta_star / C_R

then Phi_h < 1 for every such h, hence M~_h > 0 on the ladder.  The
ONE NUMBER per rung is Gamma_h := C_R D_h / delta_star with
D_h := ||J_h - J_star||_HS; the gate is max Gamma_h < 1 on the truth
census plus all deployed blind/deep rungs.

FROZEN QUESTIONS.

D  THE CONSTANT (mission a).
   D1 C_R computed from the frozen filter; per-pole shares printed
      (the low poles are CCLIII's known loose seat).
   D2 random ward: N_WARD symmetric 8x8 pairs across mixed scales;
      the bound |Delta Phi| <= C_R ||E||_HS and the per-pole bound
      |Delta tr G(z_j)| <= sqrt(8) ||E||_HS / y_j^2 must hold on
      every sample (tolerance BOUND_TOL); the honest looseness
      distributions bound/actual are printed.
   D3 tightness fire: at A = eps I, B = 0, eps = 1e-6 y_j, the
      measured per-pole ratio actual*y_j^2/(sqrt(8)||E||_HS) must
      reach >= TIGHT_MIN (the sqrt(8) is attained), and the
      dimensional-factor-free constant must be VIOLATED by a factor
      >= SQRT8_FIRE.

W  THE LADDER + FILTER (wards).
   W* rebuild the complete 68-step CCVII/CCXXV ladder read-only;
      rebuild the GLOBAL m=8 filter from cited c_B and source-only L
      and match the stored artifact (poles/residues/L at FILTER_TIE).
   T* per step: LU partial fractions reproduce the stored artifact
      reserve at LU_TIE on all matched steps; the Lanczos form J_h
      exists on all steps and tr R(J_h) == tr R(M~_h) at SIM_TIE
      relative; ks_distance == ||J1 - J2||_HS (matrix route) at
      DKS_TIE on every census cell.

J  J_STAR SELECTION (mission b; all frozen BEFORE the census, no
   per-h tuning).
   ARC  source-only: the arcsine chain (b = 0, a_1 = 1/sqrt 2,
        a_n = 1/2 -- the CCLIII SR-FREE/E4 reference) placed
        affinely on the certified window [c_B, L_art] by
        x -> (L+c)/2 + ((L-c)/2) t, with c_B CITED (CLIII) and L
        from the frozen CCXXV artifact.  DECLARED HONESTY: the
        arcsine object is natural in the measure coordinate
        x in [-1,1]; this affine placement is the one declared
        source-only embedding into the wall coordinate, chosen
        before any census read.
   MED  ladder-median: entrywise median of the Jacobi data (a, b)
        over the PREFIX = first PREFIX_N steps in ladder (h, kz)
        order; these steps are EXCLUDED from the MED/EXT gate
        census (anti-circularity by exclusion, documented).
   EXT  deep-limit extrapolant: per Jacobi entry, OLS of entry vs
        1/h over the SAME excluded prefix; J_star entry = the
        1/h -> 0 intercept.
   For each candidate: delta_star = 1 - tr R(J_star) printed and
   typed FEASIBLE (>= DELTA_FLOOR) / THIN-DELTA / NONPOSITIVE-DELTA.
   ARC keeps the full 68-step census (it consumes no ladder data);
   MED/EXT use the 56 post-prefix steps.

G  THE GATE (mission c).
   Per candidate: D_h, Gamma_h = C_R D_h / delta_star on the census
   (segment-resolved min/med/max), max Gamma_h, the D_h h-law
   (leave-one-out 2SE), and the in-situ theorem ward
   |Phi_h - Phi_star| <= C_R D_h on every census cell (kill K3 if
   violated -- that would falsify the derivation itself).
   VERDICT per candidate:
     RADIUS-CLOSES(J_star)  iff delta_star >= DELTA_FLOOR, max
       census Gamma < 1, both screens non-relocating, controls fire.
       Then the composed HIGH-POLE CLOSURE statement is printed
       LOUDLY with the typed residue: the all-h bound
       sup_h D_h <= D_star < delta_star/C_R is the SINGLE remaining
       input, and its measured finite-ladder h-law is reported.
     RADIUS-FAILS(factor)  otherwise, with the missing factor
       max Gamma and the decomposed seat:
       DELTA            delta_star < DELTA_FLOOR;
       DISTANCE-GROWING the D_h h-law slope - 2SE > SLOPE_PASS
                        (the KS-dual extremal route is needed);
       CONSTANT(C_R)    otherwise (D_h O(1)-bounded but C_R too
                        big -- the filter's low poles; the
                        high-pole variant is the fix).
       The needed constant C_need = delta_star / max D_h and the
       ratio C_R / C_need are printed, plus the low-pole share of
       C_R (j <= 4).

C  CONTROLS (mission d).  The five inherited falsifying worlds
   (smooth, scramble seed 1, cosh A=.01, mass rescale 1.1, Epstein
   x^2+5y^2 at kz 9) in the frozen aligned convention
   M_w = sym(Q_truth^T (S_world / tau_truth) Q_truth) on matched
   surface rungs.  Per aligned cell the three seats are read:
   KS-membership (Lanczos form exists, D_w finite), radius bound
   (Gamma_w < 1, REF candidate = MED), filter reserve
   (1 - tr R(M_w) > 0).  REQUIREMENTS: C1 every world fires on its
   own rung target (negA > 0 somewhere); C2 every eig-indefinite
   aligned cell loses at least one seat, and NO indefinite cell
   keeps membership + radius + reserve simultaneously (that would
   contradict the certified separator, kill K4); genuinely PD cosh
   cores are disclosed, never hidden.  Eigenvalues are used ONLY to
   type control cells (truth-reference), never in any certificate.

S  SCREENS (the corridor currency check).  Gamma_h against the
   inherited step tau and against independently recomputed CCXVII
   c_h on the matched surface subset (labelled diagnostic
   eigensolver as in CCLIII), bars SLOPE_PASS/.RELOC inherited.
   A tau- or c_h-relocation blocks RADIUS-CLOSES.

H  HIGH-POLE DUAL (conditional).  If the concurrent
   highpole_filter_tradeoff_results.json exists at frozen-run time,
   its best-point certificate (eta, alpha, beta, threshold;
   tr f(M) = sum_j eta_j [alpha_j Im + beta_j Re] tr(M - i eta_j)^{-1},
   certificate tr f(M) < threshold) is consumed VERBATIM and the
   analogous constant C' = sqrt(8) sum_j eta_j(|alpha_j|+|beta_j|) /
   eta_j^2, margin' = threshold - tr f(J_star) and Gamma' ladder are
   reported for the same candidates.  Absent -> HIGHPOLE-ABSENT;
   schema mismatch -> HIGHPOLE-INCOMPATIBLE(reason), nothing is
   fabricated.

ANTI-CIRCULARITY.  The ladder, controls, filter, poles and residues
are imported READ-ONLY from CCVII/CCXXV artifacts and code; J_star is
source-only (ARC) or prefix-only with the prefix excluded from the
gate census (MED/EXT); there is no per-h tuning anywhere; no
zero/prime oracle (AST-scanned); RNG only in the declared D2 ward
seed and the inherited scramble seed 1.

FROZEN BARS / CONSTANTS.
  NDIM=8; M_FIXED=8; c_B=5523/10000; PREFIX_N=12; N_WARD=300;
  WARD_SEED=20260812; BOUND_TOL=1e-9; TIGHT_MIN=0.99;
  SQRT8_FIRE=2.5; LU_TIE=2e-9; FILTER_TIE=2e-10; SIM_TIE=1e-8;
  DKS_TIE=1e-10; DELTA_FLOOR=1e-2; GAMMA_BAR=1.0; SLOPE_PASS=.30;
  SLOPE_RELOC=.70; RSC_FAC=1.1; runtime cap 20 min.

VERDICT ENUMS (frozen before smoke):
  constant ward: CR-SOUND / CR-BROKEN
  candidate:     FEASIBLE / THIN-DELTA / NONPOSITIVE-DELTA
  gate:          RADIUS-CLOSES(cand) / RADIUS-FAILS(factor; seats)
  seats:         DELTA / DISTANCE-GROWING / CONSTANT(C_R)
  high-pole:     HIGHPOLE-DUAL / HIGHPOLE-ABSENT /
                 HIGHPOLE-INCOMPATIBLE(reason)
  controls:      CONTROLS-FIRE / CONTROL-SILENT(world)
The gate enum is a finite-ladder theorem-engineering diagnostic,
never an RH statement and never an all-h result.

SMOKE DISCLOSURE.
  SMOKE-1 (SPEC v0, 2.5 s, 10 surface + 3 deep rungs, N_WARD=60,
  prefix 4) ran 22/22 GREEN, no kills, and required NO amendment of
  any kind (no code, bar, enum or convention change).  Uncensored
  smoke numbers: C_R = 1.007085e+01 with low-pole share j<=4 =
  0.999788 (j=0 alone 0.8785); random ward 60/60 full-filter
  (looseness min 5.74) and 480/480 per-pole (looseness min 2.31);
  deterministic eps-I family attained the sqrt(8) factor at ratio
  0.99999999999950 and violated the factor-free constant by 2.828;
  delta_star ARC +0.9268 / MED +0.9449 FEASIBLE, EXT -10.94
  NONPOSITIVE-DELTA on the 4-step smoke prefix; max census Gamma
  8.21e5 (ARC) / 3.33e4 (MED); D_h h-laws flat within 2SE; in-situ
  ward held on every cell (max bound use 2.49e-4); all five controls
  fired own-rung, every indefinite aligned cell lost reserve (and
  radius), zero contradictions; both screens PASS for ARC/MED; the
  smoke subset contains 6 unmatched pseudo-steps (subset boundary
  pairs), whose reserves (min -3.85) are typed as pseudo and absent
  from the full 68-step frozen ladder.
  SPEC v1 (2026-08-12, frozen after this one disclosed smoke):
  everything above; the frozen run below changes only this
  disclosure paragraph and hence the SPEC SHA.  No post-freeze
  numerical amendment is permitted without a new disclosed SPEC
  version.

NO RH claim.  No marker move, no verification/paper/ledger/website/
manifest edit.  This probe writes NOTHING to disk; the German CCLIX
line is prepended to experiments/next.txt only after the frozen-run
summary.

Run:
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/highpole_relative_ks_radius_probe.py --smoke
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/highpole_relative_ks_radius_probe.py
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

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob        # noqa: E402 (READ-ONLY)
import zolotarev_phase_filter_probe as zol   # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul     # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
NDIM = 8
M_FIXED = 8
CB_CITED = Fraction(5523, 10000)
CB_F = float(CB_CITED)
SURF_EXP = 42
STEPS_EXP = 68
PREFIX_N = 12
N_WARD = 300
WARD_SEED = 20260812
BOUND_TOL = 1.0e-9
TIGHT_MIN = 0.99
SQRT8_FIRE = 2.5
LU_TIE = 2.0e-9
FILTER_TIE = 2.0e-10
SIM_TIE = 1.0e-8
DKS_TIE = 1.0e-10
DELTA_FLOOR = 1.0e-2
GAMMA_BAR = 1.0
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
RSC_FAC = 1.1
SQRT_N = math.sqrt(NDIM)
ARTIFACT = os.path.join(_HERE, "zolotarev_phase_filter_phases.json")
HIGHPOLE_ARTIFACT = os.path.join(
    _HERE, "highpole_filter_tradeoff_results.json")
REF_CANDIDATE = "MED"

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name, ok, kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s" % ("PASS" if ok else "FAIL", name), flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
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
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    xm, ym = x.mean(), y.mean()
    sxx = float(np.sum((x - xm) ** 2))
    if sxx == 0.0 or n < 3:
        return 0.0, float("inf"), float("nan")
    s = float(np.sum((x - xm) * (y - ym)) / sxx)
    a = ym - s * x.mean()
    res = y - (a + s * x)
    se = math.sqrt(float(np.sum(res ** 2)) / max(n - 2, 1) / sxx)
    sst = float(np.sum((y - ym) ** 2))
    r2 = 1.0 - float(np.sum(res ** 2)) / sst if sst > 0 else 1.0
    return s, se, r2


def jack_slope(x, y):
    """OLS slope with leave-one-out jackknife 2SE and R^2."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    n = len(x)
    slope, _se, r2 = linfit(x, y)
    if n < 4:
        return slope, float("inf"), r2
    pseudo = []
    for i in range(n):
        keep = np.arange(n) != i
        s_i, _e, _r = linfit(x[keep], y[keep])
        pseudo.append(n * slope - (n - 1) * s_i)
    pseudo = np.asarray(pseudo, float)
    se = float(np.std(pseudo, ddof=1) / math.sqrt(n))
    return slope, se, r2


def screen(values, scales, label):
    """CCXLVII relocation screen, bars inherited verbatim."""
    v = np.asarray(values, float)
    s = np.asarray(scales, float)
    pos = (v > 0.0) & (s > 0.0) & np.isfinite(v) & np.isfinite(s)
    if int(np.sum(pos)) < 3:
        return ("%s: VACUOUS(pos=%d)" % (label, int(np.sum(pos))),
                "VAC")
    slope, _2se, r2 = linfit(np.log(s[pos]), np.log(v[pos]))
    verd = ("PASS" if abs(slope) <= SLOPE_PASS
            else "RELOC" if slope >= SLOPE_RELOC else "AMBIG")
    return ("%s: %s(slope=%+.3f, R2=%.3f, %d excl)"
            % (label, verd, slope, r2, int(np.sum(~pos))), verd)


def sym(matrix):
    return 0.5 * (matrix + matrix.T)


def lu_read_q(matrix, pole):
    """LU-only resolvent-trace read (no eigensolver, no determinant;
    the CCXLVII A2 representation, q-only caller)."""
    shifted = matrix.astype(complex) - pole * np.eye(NDIM,
                                                     dtype=complex)
    lum, piv = sla.lu_factor(shifted)
    inv = sla.lu_solve((lum, piv), np.eye(NDIM, dtype=complex))
    return complex(np.trace(inv))


def trace_r_of(matrix, poles, residues):
    """tr R(M) = 8 + 2 Re sum_j a_j tr(M - z_j)^{-1}, LU only."""
    contribs = [2.0 * float(a) * lu_read_q(matrix, z).real
                for z, a in zip(poles, residues)]
    return NDIM + math.fsum(contribs), contribs


def jacobi_form(matrix):
    """Lanczos tridiagonalization of (M, e_0) -- the CCVII n-read
    direction (CCLIII bridge, verbatim convention).  Returns
    (a, b) or None."""
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
    return a, b


def jacobi_matrix(a, b):
    jm = np.diag(np.asarray(b, float))
    idx = np.arange(len(a))
    jm[idx, idx + 1] = a
    jm[idx + 1, idx] = a
    return jm


def ks_distance(a1, b1, a2, b2):
    """The Killip-Simon l2 = Hilbert-Schmidt distance of two Jacobi
    data sets (== ||J1 - J2||_HS for tridiagonal symmetric)."""
    da = np.asarray(a2, float) - np.asarray(a1, float)
    db = np.asarray(b2, float) - np.asarray(b1, float)
    return math.sqrt(float(np.sum(db ** 2))
                     + 2.0 * float(np.sum(da ** 2)))


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
    if SMOKE:
        check("W4 SMOKE: fixed CCXXV filter taken from the stored "
              "artifact (a subset ladder cannot reproduce global L)",
              True)
        return poles_art, res_art
    global_l = max(st["L_src"] for st in steps)
    fd = zol.build_filter(CB_F, global_l, M_FIXED)
    dev_l = abs(global_l - float(artifact["filter"]["L"])) \
        / max(1.0, abs(global_l))
    dev_p = float(np.max(np.abs(fd["poles"] - poles_art)
                         / np.maximum(1.0, np.abs(poles_art))))
    dev_r = float(np.max(np.abs(fd["residues"] - res_art)
                         / np.maximum(1.0, np.abs(res_art))))
    check("W4 fixed CCXXV GLOBAL m=8 filter rebuilt from source-only "
          "L: L rel %.2e, poles %.2e, residues %.2e <= %.0e"
          % (dev_l, dev_p, dev_r, FILTER_TIE),
          (artifact["filter"]["m"] == M_FIXED and dev_l <= FILTER_TIE
           and dev_p <= FILTER_TIE and dev_r <= FILTER_TIE),
          kill="K2")
    return np.asarray(fd["poles"], complex), \
        np.asarray(fd["residues"], float)


# ================================== D: the constant, derived + warded
def constant_ward(poles, residues):
    section("D -- THE CONSTANT C_R: derivation restated, then warded "
            "against direct computation")
    y = np.asarray([abs(p.imag) for p in poles], float)
    a_abs = np.asarray([abs(r) for r in residues], float)
    terms = 2.0 * SQRT_N * a_abs / y ** 2
    c_r = float(np.sum(terms))
    shares = terms / c_r
    print("    derivation: resolvent identity G_A - G_B = "
          "-G_A E G_B (exact);")
    print("    |tr(E G_B G_A)| <= ||E||_HS ||G_B||_HS ||G_A||_op "
          "<= sqrt(8) ||E||_HS / y^2;")
    print("    Phi_A - Phi_B = 2 sum_j a_j Re tr(DG(z_j)) => "
          "C_R = 2 sqrt(8) sum_j |a_j| / y_j^2.")
    print("    j      y_j          |a_j|        term         share")
    for j in range(NDIM):
        print("    %-2d %12.6g %12.6g %12.6g %9.4f"
              % (j, y[j], a_abs[j], terms[j], shares[j]))
    low_share = float(np.sum(shares[:5]))
    print("    C_R = %.6e; low-pole share (j <= 4) %.6f" % (c_r,
                                                            low_share))

    n_ward = 60 if SMOKE else N_WARD
    rng = np.random.default_rng(WARD_SEED)
    full_loose = []
    pole_loose = []
    n_full = n_pole = 0
    for _ in range(n_ward):
        scale_j = 10.0 ** rng.uniform(-1.0, 5.0)
        scale_e = 10.0 ** rng.uniform(-6.0, 4.0)
        j0 = sym(rng.standard_normal((NDIM, NDIM))) * scale_j
        pert = sym(rng.standard_normal((NDIM, NDIM))) * scale_e
        j1 = j0 + pert
        e_hs = float(np.linalg.norm(pert))
        phi0, _ = trace_r_of(j0, poles, residues)
        phi1, _ = trace_r_of(j1, poles, residues)
        actual = abs(phi1 - phi0)
        bound = c_r * e_hs
        n_full += int(actual <= bound * (1.0 + BOUND_TOL))
        full_loose.append(bound / max(actual, 1e-300))
        for j in range(NDIM):
            da = abs(lu_read_q(j1, poles[j]) - lu_read_q(j0, poles[j]))
            bp = SQRT_N * e_hs / y[j] ** 2
            n_pole += int(da <= bp * (1.0 + BOUND_TOL))
            pole_loose.append(bp / max(da, 1e-300))
    check("D2 full-filter bound holds on %d/%d random symmetric "
          "pairs; looseness bound/actual %s"
          % (n_full, n_ward, e3(full_loose)),
          n_full == n_ward, kill="K3")
    check("D2 per-pole bound sqrt(8)||E||/y^2 holds on %d/%d cells; "
          "looseness %s" % (n_pole, n_ward * NDIM, e3(pole_loose)),
          n_pole == n_ward * NDIM, kill="K3")

    ratios = []
    for j in range(NDIM):
        eps = 1.0e-6 * y[j]
        j0 = np.zeros((NDIM, NDIM))
        j1 = eps * np.eye(NDIM)
        e_hs = SQRT_N * eps
        da = abs(lu_read_q(j1, poles[j]) - lu_read_q(j0, poles[j]))
        ratios.append(da * y[j] ** 2 / (SQRT_N * e_hs))
    tight = float(np.max(ratios))
    fire = tight * SQRT_N
    check("D3 tightness fire at A = eps I: attained per-pole ratio "
          "%.17f >= %.2f; the sqrt(8)-free constant is violated by "
          "%.3f >= %.2f" % (tight, TIGHT_MIN, fire, SQRT8_FIRE),
          tight >= TIGHT_MIN and fire >= SQRT8_FIRE, kill="K3")
    cr_sound = (n_full == n_ward and n_pole == n_ward * NDIM
                and tight >= TIGHT_MIN and fire >= SQRT8_FIRE)
    print("    CONSTANT VERDICT: %s"
          % ("CR-SOUND" if cr_sound else "CR-BROKEN"))
    return dict(c_r=c_r, y=y, a_abs=a_abs, shares=shares,
                low_share=low_share, sound=cr_sound,
                full_loose=trio(full_loose),
                pole_loose=trio(pole_loose), tight=tight, fire=fire)


# =========================================== T: per-step wall reads
def step_key(st):
    return (int(st["r1"]["h"]), int(st["r1"]["kz"]),
            int(st["r2"]["h"]), int(st["r2"]["kz"]))


def wall_rows(steps, artifact, poles, residues):
    section("T -- per-step reads: reserve ward, Lanczos form, "
            "similarity invariance")
    stored = {(int(r["h1"]), int(r["kz1"]), int(r["h"]),
               int(r["kz"])): r for r in artifact["rungs"]}
    rows = []
    d_marg = d_sim = d_rep = 0.0
    n_match = 0
    for idx, st in enumerate(steps):
        trace_m, _ = trace_r_of(st["Mt"], poles, residues)
        reserve = 1.0 - trace_m
        src = stored.get(step_key(st))
        if src is not None:
            n_match += 1
            d_marg = max(d_marg, abs(reserve - float(src["margin"])))
        jf = jacobi_form(st["Mt"])
        if jf is None:
            rows.append(None)
            continue
        a, b = jf
        jm = jacobi_matrix(a, b)
        trace_j, _ = trace_r_of(jm, poles, residues)
        d_sim = max(d_sim, abs(trace_j - trace_m)
                    / max(1.0, abs(trace_m)))
        d_rep = max(d_rep, abs(
            ks_distance(a, b, np.zeros(NDIM - 1), np.zeros(NDIM))
            - float(np.linalg.norm(jm))))
        rows.append(dict(index=idx, step=st, seg=ob.seg_of(st),
                         h=float(st["r2"]["h"]),
                         kz=int(st["r2"]["kz"]),
                         tau_scale=float(st["tau"]), a=a, b=b,
                         trace_r=trace_m, reserve=reserve, phi=trace_m))
    n_jac = sum(1 for r in rows if r is not None)
    check("T1 LU partial fractions reproduce the stored artifact "
          "reserve on %d matched steps: %.2e <= %.0e"
          % (n_match, d_marg, LU_TIE),
          n_match >= 1 and d_marg <= LU_TIE, kill="K2")
    check("T2 the Lanczos form of (M~_h, e_0) exists on %d/%d steps "
          "(CCLIII B0)" % (n_jac, len(rows)),
          n_jac == len(rows), kill="K2")
    check("T3 similarity invariance tr R(J_h) == tr R(M~_h): worst "
          "rel %.2e <= %.0e" % (d_sim, SIM_TIE),
          d_sim <= SIM_TIE, kill="K2")
    check("T4 ks_distance == matrix HS norm representation: worst "
          "%.2e <= %.0e" % (d_rep, DKS_TIE),
          d_rep <= DKS_TIE, kill="K2")
    out = [r for r in rows if r is not None]
    print("    reserve = 1 - tr R(M~_h) level min/med/max %s"
          % e3([r["reserve"] for r in out]))
    return out


# ================================= J: the frozen J_star candidates
def build_candidates(rows, artifact, poles, residues):
    section("J -- the three frozen J_star candidates (source-only / "
            "excluded-prefix; no per-h tuning)")
    l_art = float(artifact["filter"]["L"])
    center = 0.5 * (l_art + CB_F)
    half = 0.5 * (l_art - CB_F)
    a_arc = np.full(NDIM - 1, 0.5 * half)
    a_arc[0] = half / math.sqrt(2.0)
    b_arc = np.full(NDIM, center)

    n_prefix = 4 if SMOKE else PREFIX_N
    prefix = rows[:n_prefix]
    rest = rows[n_prefix:]
    a_med = np.median(np.asarray([r["a"] for r in prefix]), axis=0)
    b_med = np.median(np.asarray([r["b"] for r in prefix]), axis=0)

    inv_h = np.asarray([1.0 / r["h"] for r in prefix], float)
    a_ext = np.zeros(NDIM - 1)
    b_ext = np.zeros(NDIM)
    for k in range(NDIM - 1):
        s, _se, _r2 = linfit(inv_h,
                             np.asarray([r["a"][k] for r in prefix]))
        a_ext[k] = float(np.mean([r["a"][k] for r in prefix])
                         - s * np.mean(inv_h))
    for k in range(NDIM):
        s, _se, _r2 = linfit(inv_h,
                             np.asarray([r["b"][k] for r in prefix]))
        b_ext[k] = float(np.mean([r["b"][k] for r in prefix])
                         - s * np.mean(inv_h))

    print("    prefix: first %d steps (h %s..%s, all excluded from "
          "the MED/EXT gate census of %d steps)"
          % (n_prefix, int(prefix[0]["h"]), int(prefix[-1]["h"]),
             len(rest)))
    print("    ARC affine window [c_B, L_art] = [%.4f, %.6g] "
          "(c_B CITED, L from the frozen CCXXV artifact)"
          % (CB_F, l_art))
    cands = {}
    for name, a_s, b_s, census in (
            ("ARC", a_arc, b_arc, rows),
            ("MED", a_med, b_med, rest),
            ("EXT", a_ext, b_ext, rest)):
        jm = jacobi_matrix(a_s, b_s)
        phi_star, _ = trace_r_of(jm, poles, residues)
        delta_star = 1.0 - phi_star
        typ = ("FEASIBLE" if delta_star >= DELTA_FLOOR
               else "THIN-DELTA" if delta_star > 0.0
               else "NONPOSITIVE-DELTA")
        print("    %-3s tr R(J_star) = %.6f  delta_star = %+.6f  "
              "-> %s" % (name, phi_star, delta_star, typ))
        cands[name] = dict(name=name, a=a_s, b=b_s, phi=phi_star,
                           delta=delta_star, typ=typ, census=census)
    check("J1 all three candidates constructed; delta_star values "
          "reported (ARC %+.4f, MED %+.4f, EXT %+.4f)"
          % (cands["ARC"]["delta"], cands["MED"]["delta"],
             cands["EXT"]["delta"]),
          all(math.isfinite(c["delta"]) for c in cands.values()),
          kill="K2")
    check("J2 at least one candidate FEASIBLE (delta_star >= %.0e)"
          % DELTA_FLOOR,
          any(c["typ"] == "FEASIBLE" for c in cands.values()))
    return cands


# ======================================= G: THE GAMMA TABLE / gate
def gamma_census(cands, c_r_pack, label=""):
    c_r = c_r_pack["c_r"]
    section("G%s -- THE GAMMA TABLE: Gamma_h = C_R D_h / delta_star "
            "(C_R = %.4e)" % (label, c_r))
    results = {}
    worst_insitu = 0.0
    insitu_ok = True
    for name, cand in cands.items():
        census = cand["census"]
        d_vals = np.asarray([
            ks_distance(cand["a"], cand["b"], r["a"], r["b"])
            for r in census], float)
        if cand["delta"] > 0.0:
            g_vals = c_r * d_vals / cand["delta"]
        else:
            g_vals = np.full(len(census), float("inf"))
        for r, d in zip(census, d_vals):
            gap = abs(r["phi"] - cand["phi"])
            ok = gap <= c_r * d * (1.0 + BOUND_TOL)
            insitu_ok = insitu_ok and ok
            worst_insitu = max(worst_insitu,
                               gap / max(c_r * d, 1e-300))
        h_vals = np.asarray([r["h"] for r in census], float)
        slope, se, r2 = jack_slope(np.log(h_vals), np.log(d_vals))
        segs = {}
        for seg in ("surf", "bridge", "deep"):
            idx = [i for i, r in enumerate(census) if r["seg"] == seg]
            segs[seg] = (e3(d_vals[idx]) if idx else "-",
                         e3(g_vals[idx]) if idx else "-", len(idx))
        max_gamma = float(np.max(g_vals))
        print("    %-3s delta %+9.4f  census %2d  D_h %s  "
              "max Gamma %.4e"
              % (name, cand["delta"], len(census), e3(d_vals),
                 max_gamma))
        for seg in ("surf", "bridge", "deep"):
            dtxt, gtxt, n = segs[seg]
            print("        %-6s n=%2d  D %s  Gamma %s"
                  % (seg, n, dtxt, gtxt))
        print("        D_h h-law ~ h^%+.4f +/- 2SE %.4f (R2 %.3f); "
              "C_need = delta/maxD = %.4e; C_R/C_need = %.4e"
              % (slope, 2.0 * se, r2,
                 cand["delta"] / float(np.max(d_vals))
                 if cand["delta"] > 0 else float("nan"),
                 c_r * float(np.max(d_vals)) / cand["delta"]
                 if cand["delta"] > 0 else float("nan")))
        results[name] = dict(cand=cand, d=d_vals, g=g_vals,
                             h=h_vals, max_gamma=max_gamma,
                             d_slope=slope, d_2se=2.0 * se,
                             d_r2=r2)
    check("G1%s in-situ theorem ward |Phi_h - Phi_star| <= C_R D_h "
          "holds on every census cell of every candidate (worst "
          "use %.3e of the bound)" % (label, worst_insitu),
          insitu_ok, kill="K3")
    return results


def gate_verdicts(results, screens_by_cand, controls_fire):
    section("V -- THE GATE VERDICTS")
    out = {}
    for name, res in results.items():
        cand = res["cand"]
        seats = []
        if cand["delta"] < DELTA_FLOOR:
            seats.append("DELTA")
        growing = (res["d_slope"] - res["d_2se"]) > SLOPE_PASS
        closes = (cand["delta"] >= DELTA_FLOOR
                  and res["max_gamma"] < GAMMA_BAR
                  and screens_by_cand.get(name, ("", ""))[1]
                  not in ("RELOC",)
                  and controls_fire)
        if not closes and cand["delta"] >= DELTA_FLOOR:
            if growing:
                seats.append("DISTANCE-GROWING")
            if res["max_gamma"] >= GAMMA_BAR and not growing:
                seats.append("CONSTANT(C_R)")
            if res["max_gamma"] >= GAMMA_BAR and growing:
                seats.append("CONSTANT(C_R)-AND-DISTANCE")
        if closes:
            verdict = "RADIUS-CLOSES(%s)" % name
            print("    %-3s %s  max Gamma %.4e < 1" % (name, verdict,
                                                       res["max_gamma"]))
            print("    ================================================")
            print("    HIGH-POLE CLOSURE (finite-ladder statement): ON")
            print("    EVERY census step, D_h <= %.4e < delta_star/C_R"
                  % float(np.max(res["d"])))
            print("    = %.4e, hence Phi_h < 1 and M~_h > 0 on the")
            print("    whole deployed census INCLUDING the blind/deep")
            print("    segment.  TYPED RESIDUE: the single remaining")
            print("    input for an all-h theorem is the all-h bound")
            print("    sup_h D_h <= D_star < delta_star/C_R; the")
            print("    measured finite-ladder h-law of D_h is")
            print("    h^%+.4f +/- %.4f (R2 %.3f).  NO RH CLAIM."
                  % (res["d_slope"], res["d_2se"], res["d_r2"]))
            print("    ================================================")
        else:
            factor = res["max_gamma"]
            verdict = ("RADIUS-FAILS(factor %.3e; %s)"
                       % (factor, "+".join(seats) if seats
                          else "SCREEN/CONTROL"))
            print("    %-3s %s" % (name, verdict))
        out[name] = dict(verdict=verdict, seats=seats,
                         closes=closes)
    check("V1 gate evaluated for all candidates with frozen "
          "decomposition rule", len(out) == len(results))
    return out


# =========================================== S: relocation screens
def ch_surface_map(rows):
    section("S0 -- CCXVII c_h diagnostic on matched surface "
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
        out[(int(rung["h"]), int(kz))] = 1.0 - top
    vals = list(out.values())
    check("S0 c_h matched on %d surface steps; band %s inside cited "
          "[1.4e-8, 1.7e-4] up to 2x" % (len(out), e3(vals)),
          len(out) >= 1 and min(vals) >= 0.5 * 1.4e-8
          and max(vals) <= 2.0 * 1.7e-4, kill="K2")
    return out


def run_screens(results, ch_map):
    section("S -- tau- and c_h-relocation screens on Gamma_h (the "
            "corridor currency check)")
    labels = {}
    for name, res in results.items():
        census = res["cand"]["census"]
        g = res["g"]
        taus = [r["tau_scale"] for r in census]
        t_txt, t_lab = screen(g, taus,
                              "%s Gamma vs inherited step tau" % name)
        matched = [(gi, ch_map[(int(r["h"]), r["kz"])])
                   for gi, r in zip(g, census)
                   if (int(r["h"]), r["kz"]) in ch_map]
        if matched:
            c_txt, c_lab = screen([m[0] for m in matched],
                                  [m[1] for m in matched],
                                  "%s Gamma vs CCXVII c_h (surface)"
                                  % name)
        else:
            c_txt, c_lab = "%s Gamma vs c_h: VACUOUS" % name, "VAC"
        print("    " + t_txt)
        print("    " + c_txt)
        worst = ("RELOC" if "RELOC" in (t_lab, c_lab)
                 else "AMBIG" if "AMBIG" in (t_lab, c_lab)
                 else "VAC" if "VAC" in (t_lab, c_lab) else "PASS")
        labels[name] = ("tau=%s,c_h=%s" % (t_lab, c_lab), worst)
    check("S1 both screens evaluated per candidate (non-crashing; "
          "VAC typed honestly on small censuses)", True)
    return labels


# ================================================= C: the controls
def control_worlds(zones):
    def cosh_injection(rung):
        times = np.arange(rung["M"]) * rung["D"]
        return (ob.INJ_A * np.cos(ob.INJ_GAMMA0 * times)
                * (np.cosh(ob.INJ_DELTA * times) - 1.0))

    worlds = {
        "smooth": [(kz, ob.build_rung("surf", kz, world="smooth"))
                   for kz in zones],
        "scramble": [(kz, ob.build_rung("surf", kz,
                                        scramble_seed=ob.SCR_SEED))
                     for kz in zones],
        "cosh": [(kz, ob.build_rung("surf", kz,
                                    lag_fn=cosh_injection))
                 for kz in zones],
    }
    rescale = []
    for kz in zones:
        src = ob.window_of(kz)
        rescale.append((kz, ob.build_rung(
            "surf", kz, comb=(src["uu"].copy(),
                              RSC_FAC * 2.0 * src["lam"].copy()))))
    worlds["rescale"] = rescale
    if ob.CTRL_KZ in zones or not SMOKE:
        src9 = ob.window_of(ob.CTRL_KZ)
        n_eps = int(math.floor(math.exp(2.0 * src9["alpha"]))) + 1
        lam = ob.lambda_eps(n_eps)
        idx = np.nonzero(np.abs(lam) > 1e-12)[0]
        worlds["epstein"] = [(ob.CTRL_KZ, ob.build_rung(
            "surf", ob.CTRL_KZ,
            comb=(np.log(idx.astype(float)),
                  2.0 * lam[idx] / np.sqrt(idx.astype(float)))))]
    else:
        worlds["epstein"] = []
    return worlds


def controls(zones, rows, cands, c_r_pack, poles, residues):
    section("C -- CONTROLS: each falsifying world must lose at least "
            "one of {KS membership, radius bound, filter reserve}")
    ref = cands[REF_CANDIDATE]
    c_r = c_r_pack["c_r"]
    worlds = control_worlds(zones)
    fire = {}
    for name, ladder in worlds.items():
        fire[name] = sum(1 for _kz, r in ladder
                         if r is None or (isinstance(r, dict)
                                          and r["negA"] > 0))
        print("    %-9s own-rung wall target fires %d/%d"
              % (name, fire[name], max(len(ladder), 1)))
    have_eps = len(worlds["epstein"]) > 0
    check("C1 all inherited controls fire on their own rung target: "
          "%s" % ", ".join("%s=%d" % (n, fire[n]) for n in worlds
                           if worlds[n]),
          all(fire[n] > 0 for n in worlds if worlds[n]) and
          (have_eps or SMOKE), kill="K4")

    truth_by_kz = {r["kz"]: r for r in rows if r["seg"] == "surf"}
    print("    aligned convention: fixed Q_truth, tau_truth; "
          "terminating S_truth replaced by S_world; REF candidate "
          "%s (delta %+0.4f)" % (REF_CANDIDATE, ref["delta"]))
    contradiction = False
    world_rows = []
    for name, ladder in worlds.items():
        n_align = n_indef = n_pd = 0
        lost_mem = lost_rad = lost_res = n_all_kept = 0
        for kz, ctl in ladder:
            tr = truth_by_kz.get(kz)
            if (tr is None or ctl is None
                    or not ctl.get("core_ok")):
                continue
            n_align += 1
            with np.errstate(over="ignore", invalid="ignore"):
                mw = sym(tr["step"]["Q"].T
                         @ (ctl["S"] / tr["tau_scale"])
                         @ tr["step"]["Q"])
            indef = (not np.all(np.isfinite(mw))
                     or float(np.min(np.linalg.eigvalsh(
                         np.where(np.isfinite(mw), mw, 0.0)))) <= 0.0)
            n_indef += int(indef)
            n_pd += int(not indef)
            jf = jacobi_form(mw)
            member = jf is not None
            if member:
                d_w = ks_distance(ref["a"], ref["b"], jf[0], jf[1])
                member = math.isfinite(d_w)
            if not member:
                lost_mem += 1
                lost_rad += 1
                lost_res += 1
                continue
            gamma_w = (c_r * d_w / ref["delta"]
                       if ref["delta"] > 0 else float("inf"))
            trace_w, _ = trace_r_of(mw, poles, residues)
            reserve_w = 1.0 - trace_w
            rad_ok = gamma_w < GAMMA_BAR
            res_ok = reserve_w > 0.0
            lost_rad += int(not rad_ok)
            lost_res += int(not res_ok)
            if indef and rad_ok and res_ok:
                n_all_kept += 1
                contradiction = True
        world_rows.append((name, n_align, n_indef, n_pd, lost_mem,
                           lost_rad, lost_res, n_all_kept))
        print("    %-9s aligned %2d (indef %2d, PD %2d disclosed): "
              "lost membership %2d, lost radius %2d, lost reserve "
              "%2d, indefinite-with-all-seats %d"
              % (name, n_align, n_indef, n_pd, lost_mem, lost_rad,
                 lost_res, n_all_kept))
    check("C2 no eig-indefinite aligned cell keeps membership + "
          "radius + reserve simultaneously (separator soundness "
          "composed with the radius theorem)",
          not contradiction, kill="K4")
    check("C3 every aligned world with indefinite cells loses at "
          "least one seat on every such cell",
          all(w[7] == 0 for w in world_rows), kill="K4")
    return world_rows, fire


# ================================ H: conditional high-pole dual read
def highpole_dual(cands, rows):
    section("H -- the concurrent high-pole filter (conditional dual "
            "read)")
    if not os.path.exists(HIGHPOLE_ARTIFACT):
        check("H1 high-pole artifact absent on disk -> "
              "HIGHPOLE-ABSENT (typed, nothing fabricated)", True)
        return "HIGHPOLE-ABSENT"
    try:
        art = json.load(open(HIGHPOLE_ARTIFACT, encoding="utf-8"))
        bp = art["best_point"]
        eta = np.asarray(bp["eta"], float)
        alpha = np.asarray(bp["alpha"], float)
        beta = np.asarray(bp["beta"], float)
        threshold = float(bp["threshold"])
    except (KeyError, ValueError, TypeError) as exc:
        check("H1 high-pole artifact present but schema-incompatible "
              "(%s) -> HIGHPOLE-INCOMPATIBLE, nothing fabricated"
              % type(exc).__name__, True)
        return "HIGHPOLE-INCOMPATIBLE(%s)" % type(exc).__name__
    c_hp = float(SQRT_N * np.sum(eta * (np.abs(alpha) + np.abs(beta))
                                 / eta ** 2))
    print("    consumed VERBATIM: m' = %d poles i*eta, eta in "
          "[%.4g, %.4g]; threshold %.6g; C' = sqrt(8) sum "
          "eta(|alpha|+|beta|)/eta^2 = %.6e"
          % (len(eta), float(np.min(eta)), float(np.max(eta)),
             threshold, c_hp))

    def f_read(matrix):
        total = 0.0
        for e_j, a_j, b_j in zip(eta, alpha, beta):
            q = lu_read_q(matrix, 1j * e_j)
            total += e_j * (a_j * q.imag + b_j * q.real)
        return total

    for name, cand in cands.items():
        jm = jacobi_matrix(cand["a"], cand["b"])
        margin = threshold - f_read(jm)
        if margin <= 0.0:
            print("    %-3s margin' = %+.6g <= 0 -> NONPOSITIVE "
                  "high-pole delta for this candidate" % (name,
                                                          margin))
            continue
        d_vals = np.asarray([
            ks_distance(cand["a"], cand["b"], r["a"], r["b"])
            for r in cand["census"]], float)
        g_vals = c_hp * d_vals / margin
        print("    %-3s margin' %+9.4g  Gamma' %s  max %.4e"
              % (name, margin, e3(g_vals), float(np.max(g_vals))))
    check("H1 high-pole dual Gamma ladder reported from the on-disk "
          "artifact (consumed verbatim, finiteness-warded only)",
          math.isfinite(c_hp) and c_hp > 0.0)
    return "HIGHPOLE-DUAL"


# ============================================================ main
def finish(labels):
    section("FINISH")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("    checks %d/%d passed; kills: %s"
          % (n_pass, len(CHECKS),
             ",".join(sorted(set(KILLS))) if KILLS else "none"))
    for line in labels:
        print("    " + line)
    print("    runtime %.1f s; SPEC-SHA %s" % (time.time() - T0,
                                               SPEC_SHA[:8]))
    print("    %s" % ("ALL GREEN" if n_pass == len(CHECKS)
                      else "RED"))


def main():
    section("G0 -- scope + anti-circularity scans")
    print("    mode: %s; SPEC-SHA %s"
          % ("SMOKE" if SMOKE else "FROZEN", SPEC_SHA[:8]))
    bad = ast_scan()
    check("G0 no zero/prime oracle identifiers in this probe: %s"
          % (bad if bad else "clean"), not bad, kill="K0")

    artifact = json.load(open(ARTIFACT, encoding="utf-8"))
    zones, steps = build_ladder()
    poles, residues = get_filter(steps, artifact)
    c_r_pack = constant_ward(poles, residues)
    rows = wall_rows(steps, artifact, poles, residues)
    cands = build_candidates(rows, artifact, poles, residues)
    results = gamma_census(cands, c_r_pack)
    ch_map = ch_surface_map(rows)
    screen_labels = run_screens(results, ch_map)
    world_rows, fire = controls(zones, rows, cands, c_r_pack,
                                poles, residues)
    controls_ok = (not KILLS or all(k not in ("K4",) for k in KILLS))
    verdicts = gate_verdicts(results, screen_labels, controls_ok)
    hp_label = highpole_dual(cands, rows)

    labels = ["CONSTANT: %s C_R=%.4e low-pole-share=%.3f "
              "tight=%.4f fire=%.3f"
              % ("CR-SOUND" if c_r_pack["sound"] else "CR-BROKEN",
                 c_r_pack["c_r"], c_r_pack["low_share"],
                 c_r_pack["tight"], c_r_pack["fire"])]
    for name in ("ARC", "MED", "EXT"):
        labels.append("%s: %s delta=%+.4f maxGamma=%.4e D-law "
                      "h^%+.3f+/-%.3f screens[%s] -> %s"
                      % (name, cands[name]["typ"],
                         cands[name]["delta"],
                         results[name]["max_gamma"],
                         results[name]["d_slope"],
                         results[name]["d_2se"],
                         screen_labels[name][0],
                         verdicts[name]["verdict"]))
    labels.append("CONTROLS: %s"
                  % ("CONTROLS-FIRE" if controls_ok
                     else "CONTROL-SILENT"))
    labels.append("HIGH-POLE: %s" % hp_label)
    labels.append("NO-RH-CLAIM: finite float64 ladder only")
    finish(labels)


if __name__ == "__main__":
    main()
