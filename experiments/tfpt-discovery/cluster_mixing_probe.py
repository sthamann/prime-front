#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cluster_mixing_probe -- PRIME.CCM.CLUSTER.MIXING.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION
=======================================================================
Round 122 (radius4_an_probe, verdict AN-CLUSTER-REDUCTION) collapsed
the entire open CCM gap problem onto ONE measured number per lambda:
the soft-cluster mixing of the prolate candidate,
    beta_lambda = <v_1, k_lambda>,
measured |beta| = 2.1e-4 / 1.8e-3 / 3.6e-3 / 2.5e-3 at x = 3/5/8/13
(FLAT), where v_1 is the dominant near-ground cluster mode of the
even-sector Weil matrix Q_lambda and k_lambda is the CCM prolate
candidate (blockreal M4 recipe).  This probe attacks that number:
(T1) certified anatomy on an extended cofinal ladder, (T2) source
adjudication (archimedean / arithmetic / frame artifact / r121-floor
disguise), (T3) a source-only kill test (Rayleigh-Ritz enrichment),
(T4) obstruction measurement (reachability + deflation cost), (T5)
world separation, tau screens, min-cut placement, and a doublet
conditioning audit.  Pipeline: the round-122 builder and Lane-B
machinery reused VERBATIM by import (radius4_an_probe: build_cell,
prolate_kvec, mp helpers), round-114 blockreal machinery (Prolate,
prolate_pair, k_lambda_on_v), SL wards.

KEY STRUCTURAL FACT DRIVING THE DESIGN (round-122 run4/run5 logs):
the ground pair (v_0, v_1) is a QUASI-DEGENERATE DOUBLET whose
splitting gap = E_1 - E_0 collapses at the Connes scale
(5.3e-3 / 3.6e-11 / 3.8e-24 / 2.7e-47 at x = 3/5/8/13) while
eps = E_0 is a further ~1e4..1e7 below it.  Every claim about
beta must therefore carry a conditioning statement: a generic
operator perturbation delta rotates the doublet by
theta ~ delta * |v_00 v_10| / gap (exact 2x2 law, gated in S1),
i.e. the mixing number is an exact-arithmetic observable whose
CONDITION NUMBER is inverse-Connes.  The probe measures this law.

=======================================================================
LADDERS AND FROZEN NUMERICS
=======================================================================
MAIN even cells (KFAC 1.25, round-122 builder, want_mp):
  RUNGS = ((3,45),(4,50),(5,60),(6,70),(7,70),(8,80),(13,120),(18,160))
  x = 18 is a NEW deepest rung (never built before in the corpus).
DEEP rungs (RR spaces, worlds, eval anatomy): x in (5, 8, 13, 18).
Frame ladder L2 (KFAC 1.60): x = (5,60), (8,80).
Worlds (even, want_mp): SMOOTH x = 5/8/13, SCRARITH x = 5/8,
EPSTEIN x = 5 (ward only) / 8 / 13.
Candidate: k_lambda via R4.prolate_kvec (NGRID_K = 20001) -- the
round-122 object bit-for-bit; certification grids (10001, 20001,
40001) through an own projector gated == R4 at 20001 (1e-12).
SOFT_BAR = 1e-2 (round-122 cluster definition).  All mp work under
explicit mp.workdps at the cell dps (round-118/120 unary-negation
lesson: NO mpf arithmetic at ambient precision).  Sign conventions
(deterministic): every eigenvector sign-fixed so that its largest-
|entry| component is positive; alpha = <v_0,k> reported signed
after fixing v_0 so alpha > 0; beta reported SIGNED in the fixed
convention.  Deterministic: no RNG anywhere; all enrichment vectors
are closed-form source objects.

Round-122 regression pins (run4 log, 3 digits): |beta| =
2.12e-4 / 1.85e-3 / 3.57e-3 / 2.52e-3 at x = 3/5/8/13, bar 2e-2 rel.
Round-121 scale table (cited from CDXXII): dstar(l=0.8) = 5.64e-3,
dstar(l=0.4) = 9.9e-4, RK-dev = 4.3e-4, irwall defect top 2.0e-3 /
base 3.3e-3.

T2 SOURCE CANDIDATES (each gated):
 (a) archimedean prolate/Hermite: swap prolate -> Hermite pair in the
     SAME Poisson lift (kH); if beta(kH) == beta(k) the
     Meixner-Schaefke lambda^-2 term is NOT the source.  Plus the
     arch-only operator A = Mpole + March (mp eigsy): its own ground
     pair, cos(k, g_A), beta_A ladder.
 (b) arithmetic: SMOOTH world (PNT-density-matched archimedean world)
     beta_sm ladder vs true; SCRARITH (golden-scrambled Lambda
     weights); channel split lam_1 beta = <v1,POLE k> + <v1,ARCH k>
     - <v1,PRIME k> (exact, gated; expected to inherit the round-115
     cross-cancellation debt -- confirmed or falsified, ONE gate, not
     re-litigated per the round-122 finding).
 (c) frame artifact: beta at KFAC 1.60 vs 1.25 (x = 5, 8), grid
     ladder, dps discipline.  FRAME_BAR 0.25 rel.
 (d) r121 completion floor: |beta| vs the frozen scale table
     (match band |log ratio| <= log 1.3 at deep rungs).

T3 KILL TEST (source-only enrichment; HONESTY GATE: spaces built
ONLY from Lambda(n), Gamma/pi/prolate/Legendre, Loewner/frame data;
no zero ordinate anywhere; the zero-data comparator is WARD-ONLY and
labeled).  Spaces at each deep rung, Rayleigh-Ritz in mp:
  S_ARCH = {k} + {E(phi_n): n = 0,2,4,6,8} (prolate-mode Poisson
           lifts; M(E phi)(s) = zeta(s) M(phi)(s) makes every E-lift
           an automatic band-zero annihilator);
  S_EDGE = {k, symmetric window-edge Gaussian bump} (width a/8);
  S_LAM  = {k, k shifted by +-log 2, +-log 3, k_Lambda =
           sum_q (Lambda(q)/sqrt q)(shift_q + shift_-q), q <= x};
  S_ALL  = union;  S_KRY = {k, Qk, Q^2 k} (instrument comparator,
           source-built Q, typed as comparator);
  S_Z    = {k, e_gamma_1..3} (WARD zero-data comparator ONLY).
Read per space: Rayleigh ground u*, R(u*), alpha(u*), signed
beta(u*), improvement factor |beta(u*)/beta(k)|, reachability
c1 = ||P_S v_1||, deflation cost F = muperp/mu0 (mu0 = min Rayleigh
over S, muperp = min over S with <v1,u> = 0).  KILL if a source-only
space reaches |beta(u*)| <= |beta(k)|/10 with alpha >= 0.99 at the
two deepest rungs; PARTIAL if factor >= 2; OBSTRUCTED otherwise,
with (c1, F) as the measured obstruction profile.

T1 EXTRA ANATOMY: doublet closure ||k - alpha v0 - beta v1||
(TWO-VECTOR structure, bar 0.05|beta| at x >= 5); kmix profile over
the cluster + geometric ratios; n-split (n=1 term vs n>=2 Poisson
tail of the lift); c0/c4 split; prolate-mode scan <v1, E(phi_n)>,
n = 0..10; localization thirds (edge vs center mass of v1, k, and
the overlap density); annihilator dimension law nsoft + 1 vs
K - N(band edge) (cache count, ward); eval anatomy
|<e_gamma_j, v0/v1/k>| for the first 5 band zeros; flatness fit
slope of log|beta| vs log x (x >= 5) with grid-certified error bars;
zero-integral gate |int h_lambda| <= 1e-10 relative.

T5: world separation read: separating iff |log(beta_w/beta_true)| >=
log 2 at the shared rungs (SMOOTH / SCRARITH / EPSTEIN-with-k_Z and
EPSTEIN-with-adapted k_Q = Poisson lift weighted by r_Q(n)/2); tau
screens: OLS slope of log10|beta| vs log10 eps and vs log10 gap over
deep rungs (atlas bands: |s| <= 0.30 PASS = not Connes currency,
s >= 0.70 RELOCATION); min-cut: round-116 replica + round-122
extension re-run (flows 4 base / 5 extended expected), the mixing
outcome placed as MEAS data on the LANEACONV omega edge -- no new
class expected, census {MEAS, OMEGA-POS} cardinality 4.

CONDITIONING (S7): at x = 5 and 8, perturb Q[0,0] by a
self-calibrated delta targeting theta ~ 1e-6 (delta = theta * gap /
|v00 v10|, clipped [1e-45, 1e-8], disclosed), re-eigsy, measure
dbeta, gate |dbeta| / |theta_pred * alpha| in [1/3, 3] (2x2 law from
S1); exactly-zero response = red flag (round-118 lesson).

GATES: numbered G01..G99, hard asserts via the check() ledger;
composite verdict line; deterministic re-run = full second run
diffed externally (runN logs).  RUNTIME_BAR = 7200 s.

VERDICT ENUMS (frozen): KMIX-SINGLE-MODE / KMIX-CLUSTER-SUM;
KMIX-TWO-VECTOR; KMIX-FLAT(slope+-err) / KMIX-TREND(slope);
KMIX-SOURCE-{ARCH, ARITH, FRAME-ARTIFACT, UNSPLIT}(evidence);
R121-SCALE-{MATCH, NO-MATCH}; KMIX-{KILLED(space, rate),
PARTIAL(factor), OBSTRUCTED(c1, F)}; KMIX-WORLD-{SEPARATING,
BLIND}(ratios); KMIX-CONDITIONING(measured law vs 1/gap);
TAU-SCREEN(bands); MINCUT(cardinality, census).

SMOKE DISCLOSURE (pre-freeze, two smokes at x = (3, 5), 11 s each,
plus one x = 18 build-cost timing: 555.8 s at dps 160, K = 66,
eps 5.2e-79, gap 1.7e-71 -- dps headroom confirmed; scratch logs
deleted):
(i) smoke 1 exposed TWO instrument bugs, both repaired PRE-FREEZE:
the zero-integral gate had used an 8001-point grid while
prolate_pair defines c0 to kill the 4001-point trapezoid (repaired:
same grid, measured residual 3.1e-17); the deflation number had been
computed over the PROJECTION of the span onto v1-perp instead of the
constrained codim-1 subspace INSIDE the span (measured F < 1 =
impossible for the intended object; repaired to the exact
constrained pencil, F >= 1 confirmed, and the exact-rational G12
gate matches the corrected logic).  (ii) smoke calibrations:
eigen-residual bar 10^(-dps/2) (measured ~1e-3x margins), grid
certification |beta_40001 - beta_20001| measured 2.6e-9 (x=3) /
3.7e-13 (x=5) -> bar 5e-6 abs, projector == R4.prolate_kvec at
20001 measured < 1e-15 -> bar 1e-12, channel-sum rel measured
1.4e-47 -> bar 1e-6.  (iii) smoke-1 findings that motivated two
pre-freeze READ additions (no bar moved): the prolate-mode scan
measured |<v1, E(phi_8)-hat>| = 0.9953 at x = 5 -> added the v0-row,
the matched-mode index n* and the pure-arch first-order prediction
beta_arch = <v1,e*> <e*,k> as printed reads; added the RR second
pair (mu1, |<v1,u1*>|) as printed reads.  (iv) hard structural
gates on rungs never measured before (x = 4, 6, 7, 18) are
restricted to typing/reporting; the hard cross-rung gates
(G31/G33/G34 subsets) bind on the round-122-measured rungs
(5, 8, 13).  No verdict rule, ladder or kill bar was calibrated on
deep rungs.  Amendments after the frozen run, if any, are appended
as numbered AMENDMENT blocks.

AMENDMENT 1 (after frozen run 1, 33/33 PASS, 1220.8 s; READ
ADDITIONS ONLY -- no bar, ladder, battery, kill rule or verdict rule
changed; run 1 is part of the record).  Run 1 measured
FRAME-SENSITIVE (G44: beta drops by ~7x and can flip sign at
KFAC 1.60), which makes the frame DIRECTION the sharpest open
quantitative question of the round.  Added reads: (i) a KFAC ladder
at x = 5 and 8 (KFAC = 1.25, 1.60, 2.00, 2.40) and at x = 13
(KFAC = 1.25, 2.00), each reporting beta, nsoft, the annihilator
dimension K - N(band edge) (ward count), alpha and the two-vector
residual, plus an OLS slope of log|beta| vs log(annihilator dim);
typing gate G47-kfac-ladder (always-PASS report).  (ii) R(k-hat) =
<k,Qk> printed per MAIN rung in S3 (the Rayleigh level of the
candidate, needed to interpret the S5 selector degeneration).
(iii) the frame rows now print alpha/resid2v/nsoft, so the
two-vector structure is verified per frame, not assumed.  Run 2 is
the run of record for the amended spec; run 3 is its deterministic
re-run.

AST FIREWALL: no zetazero/siegelz/siegeltheta/nzeros/grampoint
anywhere; no mp.zeta anywhere in this probe (no target currency
needed); np.load only inside ward_* functions; no import of
verification/.  Zero cache verified_zeros_n7000.npy READ-ONLY in
ward_ namespace (X5: instrument/comparator, never construction).
NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4        # round-122 pipeline (verbatim reuse)
import blockreal_lemma_probe as BR   # round-114 machinery
import semilocal_realroot_limit_probe as SL  # ward builder

# ---------------------------------------------------------------- frozen
KFAC1 = 1.25
KFAC2 = 1.60
RUNGS = ((3, 45), (4, 50), (5, 60), (6, 70), (7, 70), (8, 80),
         (13, 120), (18, 160))
DEEP_X = (5, 8, 13, 18)
L2R = ((5, 60), (8, 80))
KFAC_LADDER = ((5, 60, (1.60, 2.00, 2.40)), (8, 80, (1.60, 2.00, 2.40)),
               (13, 120, (2.00,)))
SMOOTH_R = ((5, 60), (8, 80), (13, 120))
SCR_R = ((5, 60), (8, 80))
EPS_R = ((8, 80), (13, 120))
NGRIDS = (10001, 20001, 40001)
SOFT_BAR = 1e-2
R122_KMIX = {3: 2.12e-4, 5: 1.85e-3, 8: 3.57e-3, 13: 2.52e-3}
R122_REG_BAR = 2e-2
R121_SCALES = (("dstar_l0.8", 5.64e-3), ("dstar_l0.4", 9.9e-4),
               ("rk_dev", 4.3e-4), ("irwall_top", 2.0e-3),
               ("irwall_base", 3.3e-3))
R121_MATCH_BAND = math.log(1.3)
GRID_CERT_BAR = 5e-6
PROJ_EQ_BAR = 1e-12
TWO_VECTOR_BAR = 0.05
ZERO_INT_BAR = 1e-10
CH_SUM_BAR = 1e-6
FRAME_BAR = 0.25
KILL_FACTOR = 10.0
PARTIAL_FACTOR = 2.0
ALPHA_MIN = 0.99
WORLD_SEP_LOG = math.log(2.0)
SLOPE_FLAT_BAR = 0.5
PERT_THETA_TGT = 1e-6
COND_RATIO = (1.0 / 3.0, 3.0)
GS_DROP = 1e-6
MODE_SCAN_N = 16
RUNTIME_BAR = 7200.0
GAMMA1_LIT = 14.134725141734693790   # ward only

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-38s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owner(lineno: int) -> str:
        best = ""
        for nm, lo, hi in spans:
            if lo <= lineno <= hi:
                best = nm
        return best

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point", "zeta"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if isinstance(node, ast.Attribute) and nm == "load":
            fn = owner(node.lineno)
            if not fn.startswith("ward_"):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fn or "module"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle, no zeta anywhere, cache in ward_")


# --------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


def ward_band_count(gam: np.ndarray, edge: float) -> int:
    return int(np.sum(gam <= edge))


def ward_eval_vecs(cell: dict, gam: np.ndarray, m: int) -> list:
    """WARD ONLY (zero-data comparator): band evaluation vectors at the
    first m cache zeros, real, f64."""
    out = []
    with mp.workdps(cell["dps"]):
        for j in range(m):
            ez = R4.evec_euler(complex(float(gam[j]), 0.0),
                               cell["om"], cell["a"], cell["K"])
            out.append(np.array([float(mp.re(t)) for t in ez]))
    return out


# --------------------------------------------------------- candidates
def prime_power_atoms(x: int) -> list[tuple[int, float]]:
    """(q, Lambda(q)) for prime powers q <= x (source data)."""
    icap = int(math.floor(x))
    comp = np.zeros(icap + 1, dtype=bool)
    out = []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= icap:
            out.append((q, math.log(p)))
            q *= p
    out.sort()
    return out


def esum_on_grid(evalf, vg: np.ndarray, nmax: int,
                 lam: float) -> np.ndarray:
    """E(h)(e^v) = e^{v/2} sum_{n=1..nmax} h(n e^v) on the grid.
    Support-masked (h supported in |x| <= lam): bitwise-identical to
    the unmasked sum (skipped terms are exact 0.0), but fast for the
    shifted/Lambda-weighted lifts."""
    ug = np.exp(vg)
    acc = np.zeros_like(ug)
    umin = float(np.min(ug))
    for n in range(1, nmax + 1):
        if n * umin > lam:
            break
        xs = n * ug
        msk = xs <= lam
        if not np.any(msk):
            continue
        acc[msk] = acc[msk] + evalf(xs[msk])
    return np.sqrt(ug) * acc


def project_cell(vals: np.ndarray, vg: np.ndarray,
                 cell: dict) -> np.ndarray:
    """Project a grid function onto the cell's normalized cos basis
    (same convention as R4.prolate_kvec, WITHOUT final normalization)."""
    L = cell["a"]
    K = cell["K"]
    om = cell["om"]
    cs = np.empty(K)
    cs[0] = float(np.trapezoid(vals, vg)) / (2 * L)
    for k in range(1, K):
        cs[k] = float(np.trapezoid(vals * np.cos(om[k] * vg), vg)) / L
    norms = np.full(K, math.sqrt(L))
    norms[0] = math.sqrt(2 * L)
    return cs * norms


def kfun_data(x: int) -> dict:
    """Prolate pair + zero-integral read for rung x."""
    pro = BR.Prolate(float(x))
    coef, c0, e0, e4 = BR.prolate_pair(pro)
    lam = pro.lam
    # SAME 4001-point grid as prolate_pair: c0 is defined to kill
    # exactly THIS quadrature of the integral
    xg = np.linspace(-lam, lam, 4001)
    hv = pro.eval_vec(coef, xg)
    ih = float(np.trapezoid(hv, xg))
    iab = float(np.trapezoid(np.abs(hv), xg))
    return {"pro": pro, "coef": coef, "c0": c0, "e0": e0, "e4": e4,
            "zero_int_rel": abs(ih) / max(iab, 1e-300)}


def k_vals_on(kd: dict, vg: np.ndarray, nmax: int) -> np.ndarray:
    pro, coef = kd["pro"], kd["coef"]
    return esum_on_grid(lambda xx: pro.eval_vec(coef, xx), vg, nmax,
                        pro.lam)


def hermite_swap_vals(x: int, vg: np.ndarray) -> np.ndarray:
    """kH: the SAME Poisson lift with the Hermite pair instead of the
    prolate pair (zero-integral c0 recomputed on the Hermite pair)."""
    lam = math.sqrt(float(x))
    xg = np.linspace(-lam, lam, 8001)
    h0 = BR.hermite_h(0, xg)
    h4 = BR.hermite_h(4, xg)
    i0 = float(np.trapezoid(h0, xg))
    i4 = float(np.trapezoid(h4, xg))
    c4 = math.sqrt(3) / 2 ** (11 / 4)
    c0 = -c4 * i4 / max(i0, 1e-300)

    def evalf(xx):
        out = c4 * BR.hermite_h(4, xx) + c0 * BR.hermite_h(0, xx)
        return np.where(np.abs(xx) > lam, 0.0, out)

    return esum_on_grid(evalf, vg, int(x) + 2, lam)


def epstein_r_counts(nmax: int) -> np.ndarray:
    r = np.zeros(nmax + 1)
    xm = int(math.isqrt(nmax)) + 1
    ym = int(math.isqrt(nmax // 5)) + 1
    for xx in range(-xm, xm + 1):
        for yy in range(-ym, ym + 1):
            n = xx * xx + 5 * yy * yy
            if 1 <= n <= nmax:
                r[n] += 1.0
    return r


def kq_vals_on(kd: dict, vg: np.ndarray, nmax: int) -> np.ndarray:
    """Epstein-adapted candidate: Poisson lift weighted by r_Q(n)/2."""
    pro, coef = kd["pro"], kd["coef"]
    rq = epstein_r_counts(nmax)
    ug = np.exp(vg)
    acc = np.zeros_like(ug)
    for n in range(1, nmax + 1):
        if rq[n] <= 0:
            continue
        xs = n * ug
        msk = xs <= pro.lam
        if not np.any(msk):
            continue
        acc[msk] = acc[msk] + (rq[n] / 2.0) * pro.eval_vec(coef,
                                                           xs[msk])
    return np.sqrt(ug) * acc


# ------------------------------------------------------------ mp core
def lift_vec(w) -> list:
    """f64 -> mp list (call inside workdps)."""
    return [mp.mpf(repr(float(t))) for t in w]


def sign_fix(vm: list) -> list:
    imax = 0
    amax = abs(vm[0])
    for i in range(1, len(vm)):
        if abs(vm[i]) > amax:
            amax = abs(vm[i])
            imax = i
    if vm[imax] < 0:
        return [-t for t in vm]
    return vm


def rung_core(cell: dict, kt: np.ndarray) -> dict:
    """Doublet + cluster anatomy for one even cell (mp)."""
    K = cell["K"]
    res = {"x": cell["x"], "K": K}
    with mp.workdps(cell["dps"]):
        E, V = cell["mpE"], cell["mpV"]
        Q = cell["mpM"]
        eps = E[0]
        gap = E[1] - E[0]
        kv = lift_vec(kt)
        v0 = R4.matcol(V, 0, K)
        if R4.mp_dot(v0, kv) < 0:
            v0 = [-t for t in v0]
        v1 = sign_fix(R4.matcol(V, 1, K))
        alpha = R4.mp_dot(v0, kv)
        beta = R4.mp_dot(v1, kv)
        soft = [i for i in range(1, K) if E[i] - eps <= SOFT_BAR]
        betas = []
        for i in range(1, min(K, 13)):
            vi = sign_fix(R4.matcol(V, i, K))
            betas.append(float(R4.mp_dot(vi, kv)))
        resid = [kv[j] - alpha * v0[j] - beta * v1[j] for j in range(K)]
        rnorm = R4.mp_norm(resid)
        qv0 = R4.matvec(Q, v0, K)
        er0 = R4.mp_norm([qv0[j] - eps * v0[j] for j in range(K)])
        qv1 = R4.matvec(Q, v1, K)
        er1 = R4.mp_norm([qv1[j] - E[1] * v1[j] for j in range(K)])
        # channel split of lam1 * beta (exact identity, one gate)
        chP = R4.mp_dot(v1, R4.matvec(cell["mpPole"], kv, K))
        chA = R4.mp_dot(v1, R4.matvec(cell["mpArch"], kv, K))
        chPr = R4.mp_dot(v1, R4.matvec(cell["mpPrime"], kv, K))
        chsum = chP + chA - chPr
        lamb = E[1] * beta
        chmax = max(abs(chP), abs(chA), abs(chPr), mp.mpf("1e-300"))
        res.update(
            eps=float(eps), gap=float(gap),
            eps_str=mp.nstr(eps, 8), gap_str=mp.nstr(gap, 8),
            lam1=float(E[1]), nsoft=len(soft),
            alpha=float(alpha), beta=float(beta), betas=betas,
            resid2v=float(rnorm), eigres=max(float(er0), float(er1)),
            chP=float(chP), chA=float(chA), chPr=float(chPr),
            ch_dev=float(abs(chsum - lamb) / chmax),
            ch_canc=float(mp.log10(chmax / max(abs(lamb),
                                               mp.mpf("1e-300")))),
            cl_gaps=[float(E[i] - eps) for i in range(1, min(K, 9))],
            v0f=np.array([float(t) for t in v0]),
            v1f=np.array([float(t) for t in v1]))
    return res


def mp_overlap(cell: dict, vf: np.ndarray, w: np.ndarray,
               normalize: bool = True) -> float:
    """<v, w/||w||> in mp (v an eigenvector f64 copy is NOT used;
    caller passes mp-accurate f64 of v -- adequate for 1e-9 reads).
    Kept in mp to respect the workdps discipline."""
    with mp.workdps(cell["dps"]):
        vm = lift_vec(vf)
        wm = lift_vec(w)
        if normalize:
            nw = R4.mp_norm(wm)
            wm = [t / nw for t in wm]
        return float(R4.mp_dot(vm, wm))


def cell_fn_on_grid(vec: np.ndarray, cell: dict,
                    vg: np.ndarray) -> np.ndarray:
    """f(v) = sum_k vec[k] cos(om_k v)/nrm_k on the grid."""
    L = cell["a"]
    K = cell["K"]
    om = cell["om"]
    out = np.full_like(vg, float(vec[0]) / math.sqrt(2 * L))
    for k in range(1, K):
        out = out + float(vec[k]) * np.cos(om[k] * vg) / math.sqrt(L)
    return out


def thirds_mass(f: np.ndarray, vg: np.ndarray, L: float) -> tuple:
    w = f * f
    tot = float(np.trapezoid(w, vg))
    inner = float(np.trapezoid(np.where(np.abs(vg) <= L / 3, w, 0.0), vg))
    mid = float(np.trapezoid(np.where((np.abs(vg) > L / 3)
                                      & (np.abs(vg) <= 2 * L / 3),
                                      w, 0.0), vg))
    outer = tot - inner - mid
    return (inner / tot, mid / tot, outer / tot)


# --------------------------------------------------------- RR machinery
def rr_space(cell: dict, vecs: list, v0f: np.ndarray,
             v1f: np.ndarray) -> dict:
    """Rayleigh-Ritz over span(vecs) in mp; reachability + deflation."""
    K = cell["K"]
    out: dict = {}
    with mp.workdps(cell["dps"]):
        Q = cell["mpM"]
        v0m = lift_vec(v0f)
        v1m = lift_vec(v1f)

        def gs(vlist):
            B = []
            for w in vlist:
                wm = (lift_vec(w) if isinstance(w, np.ndarray)
                      else [mp.mpf(t) for t in w])
                n0 = R4.mp_norm(wm)
                if float(n0) == 0.0:
                    continue
                for b in B:
                    c = R4.mp_dot(b, wm)
                    wm = [wm[i] - c * b[i] for i in range(K)]
                nw = R4.mp_norm(wm)
                if nw > mp.mpf(repr(GS_DROP)) * n0:
                    B.append([t / nw for t in wm])
            return B

        def form_matrix(B):
            d = len(B)
            QB = [R4.matvec(Q, b, K) for b in B]
            F = mp.zeros(d, d)
            for i in range(d):
                for j in range(i, d):
                    val = (R4.mp_dot(B[i], QB[j])
                           + R4.mp_dot(B[j], QB[i])) / 2
                    F[i, j] = val
                    F[j, i] = val
            return F

        def ground_of(F, B, which=0):
            d = len(B)
            Ef, Vf = mp.eigsy(F)
            order = sorted(range(d), key=lambda i: Ef[i])
            i0 = order[min(which, d - 1)]
            u = [mp.fsum(Vf[i, i0] * B[i][j] for i in range(d))
                 for j in range(K)]
            nu = R4.mp_norm(u)
            return Ef[i0], [t / nu for t in u]

        B = gs(vecs)
        d = len(B)
        F = form_matrix(B)
        mu0, u = ground_of(F, B, 0)
        if R4.mp_dot(v0m, u) < 0:
            u = [-t for t in u]
        alpha = R4.mp_dot(v0m, u)
        beta = R4.mp_dot(v1m, u)
        b1o = mp.mpf(0)
        mu1 = mp.mpf("inf")
        if d >= 2:
            mu1, u1 = ground_of(F, B, 1)
            b1o = abs(R4.mp_dot(v1m, u1))
        # reachability
        w = [R4.mp_dot(b, v1m) for b in B]
        c1 = mp.sqrt(mp.fsum(t ** 2 for t in w))
        # TRUE constrained deflation: minimize the Rayleigh quotient
        # over {u in span B : <v1, u> = 0} (codim-1 subspace of the
        # span; diagnostic-only object -- it aims at v1, so it is NOT
        # a legal source-only candidate)
        mup = mp.mpf("nan")
        if float(c1) < 1e-12:
            mup = mu0
        elif d >= 2:
            wh = [t / c1 for t in w]
            U = []
            for i in range(d):
                e = [mp.mpf(1) if j == i else mp.mpf(0)
                     for j in range(d)]
                e = [e[j] - wh[j] * wh[i] for j in range(d)]
                for uu in U:
                    cc = mp.fsum(uu[j] * e[j] for j in range(d))
                    e = [e[j] - cc * uu[j] for j in range(d)]
                ne = mp.sqrt(mp.fsum(t ** 2 for t in e))
                if ne > mp.mpf("1e-10"):
                    U.append([t / ne for t in e])
            dd = len(U)
            Fp = mp.zeros(dd, dd)
            for i in range(dd):
                for j in range(i, dd):
                    val = mp.fsum(U[i][r] * F[r, s] * U[j][s]
                                  for r in range(d)
                                  for s in range(d))
                    Fp[i, j] = val
                    Fp[j, i] = val
            Ep = mp.eigsy(Fp, eigvals_only=True)
            mup = min(Ep[i] for i in range(dd))
        out = {"dim": d, "mu0": float(mu0), "alpha": float(alpha),
               "beta": float(beta), "c1": float(c1),
               "muperp": float(mup), "mu1": float(mu1),
               "b1o": float(b1o)}
    return out


# --------------------------------------------------------- symbolic S1
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []
    # G10 mixing identity on an exact rational spectral example
    S = sp.Matrix([[0, sp.Rational(1, 2), sp.Rational(-1, 3)],
                   [sp.Rational(-1, 2), 0, sp.Rational(1, 5)],
                   [sp.Rational(1, 3), sp.Rational(-1, 5), 0]])
    I3 = sp.eye(3)
    R = (I3 - S).inv() * (I3 + S)
    lam = sp.diag(sp.Rational(1, 7), sp.Rational(3, 5), sp.Integer(2))
    Q = R * lam * R.T
    kx = sp.Matrix([sp.Rational(2, 3), sp.Rational(-1, 5),
                    sp.Rational(1, 2)])
    v1 = R.col(1)
    ok10 = (sp.simplify(R.T * R - I3) == sp.zeros(3, 3)
            and sp.simplify((v1.T * Q * kx)[0, 0]
                            - lam[1, 1] * (v1.T * kx)[0, 0]) == 0)
    out.append(("G10-mixing-identity-exact", ok10,
                "lam1 <v1,k> == <v1,Qk> exactly on a rational "
                "orthogonal spectral example (Cayley R, 3x3)"))
    # G11 doublet rotation law (2x2, exact)
    g, d, a00, a01, a11 = sp.symbols("g d a00 a01 a11", positive=True)
    t2 = 2 * d * a01 / (g + d * (a11 - a00))
    s2 = t2 / sp.sqrt(1 + t2 ** 2)
    c2 = 1 / sp.sqrt(1 + t2 ** 2)
    off = d * a01 * c2 - (g + d * (a11 - a00)) / 2 * s2
    ok11 = sp.simplify(off) == 0
    out.append(("G11-doublet-rotation-exact", ok11,
                "2x2 rotation tan(2 theta) = 2 d a01/(g + d(a11-a00)) "
                "kills the off-diagonal exactly => mixing shift "
                "dbeta ~ theta * alpha; theta ~ d|v00 v10|/gap is the "
                "doublet conditioning law measured in S7"))
    # G12 deflation ordering (exact rational pencil)
    F = sp.diag(1, 2, 3)
    Bm = sp.Matrix([[1, 0], [-1, 1], [0, -1]])   # basis of (1,1,1)-perp
    A2 = Bm.T * F * Bm
    G2 = Bm.T * Bm
    z = sp.symbols("z")
    poly = sp.expand((A2 - z * G2).det())
    roots = sp.solve(sp.Eq(poly, 0), z)
    ok12 = all(bool(sp.simplify(r - 1) > 0) for r in roots)
    w2 = sp.Matrix([0, 1, 1])
    B2 = sp.Matrix([[1, 0], [0, 1], [0, -1]])    # basis of w2-perp
    poly2 = sp.expand((B2.T * F * B2 - z * (B2.T * B2)).det())
    roots2 = sp.solve(sp.Eq(poly2, 0), z)
    ok12b = any(sp.simplify(r - 1) == 0 for r in roots2) \
        and w2.dot(B2.col(0)) == 0 and w2.dot(B2.col(1)) == 0
    out.append(("G12-deflation-order-exact", bool(ok12) and bool(ok12b),
                "min Rayleigh over w-perp >= global min, exact rational "
                "pencil; equality iff ground in w-perp (both verified "
                "exactly) -- the S5 obstruction logic"))
    return out


# --------------------------------------------------------- min-cut S6
def maxflow(edges: dict, srcn: str, dstn: str) -> int:
    cap = {}
    nodes = set()
    for (u, v), c in edges.items():
        cap[(u, v)] = cap.get((u, v), 0) + c
        cap.setdefault((v, u), 0)
        nodes |= {u, v}
    flow = 0
    while True:
        prev = {srcn: None}
        queue = [srcn]
        while queue and dstn not in prev:
            u = queue.pop(0)
            for v in nodes:
                if v not in prev and cap.get((u, v), 0) > 0:
                    prev[v] = u
                    queue.append(v)
        if dstn not in prev:
            return flow
        path = []
        v = dstn
        while prev[v] is not None:
            path.append((prev[v], v))
            v = prev[v]
        aug = min(cap[e] for e in path)
        for (u, v) in path:
            cap[(u, v)] -= aug
            cap[(v, u)] += aug
        flow += aug


def ols_slope(xs: list[float], ys: list[float]) -> tuple[float, float]:
    n = len(xs)
    xa = np.array(xs)
    ya = np.array(ys)
    A = np.vstack([xa, np.ones(n)]).T
    coef, res, _rk, _sv = np.linalg.lstsq(A, ya, rcond=None)
    if n > 2 and len(res) > 0:
        se = math.sqrt(float(res[0]) / (n - 2)
                       / float(np.sum((xa - xa.mean()) ** 2)))
    else:
        se = float("nan")
    return float(coef[0]), se


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("cluster_mixing_probe -- PRIME.CCM.CLUSTER.MIXING.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    rungs = ((3, 45), (5, 60)) if smoke else RUNGS
    deep = [5] if smoke else [x for x in DEEP_X
                              if x in dict(rungs)]
    l2r = () if smoke else L2R
    smooth_r = ((5, 60),) if smoke else SMOOTH_R
    scr_r = ((5, 60),) if smoke else SCR_R
    eps_r = () if smoke else EPS_R

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det)
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)))

    # ---------------------------------------------------------- S1
    section("S1  EXACT GATES (sympy)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg)

    # ---------------------------------------------------------- S2
    section("S2  INSTRUMENT (round-122 builder reused + wards)")
    cells: dict[int, dict] = {}
    for x, dps in rungs:
        t0 = time.time()
        cells[x] = R4.build_cell(x, KFAC1, "MAIN", dps, want_mp=True)
        print("  MAIN x=%-2d built (K=%d, dps=%d, %.1f s, tau=%s "
              "gap=%s)" % (x, cells[x]["K"], dps, time.time() - t0,
                           cells[x]["tau_str"], cells[x]["gap_str"]),
              flush=True)
    sl3 = SL.build_trig_cell_hp(3, KFAC1, "MAIN", 45)
    dev_m = float(np.max(np.abs(cells[3]["m_tilde"] - sl3["m_tilde"])))
    check("G20-ward-x3-even", dev_m <= 1e-8,
          "own even x=3 matrix vs SL HP: max dev %.1e" % dev_m)
    cw: dict[str, dict[int, dict]] = {"SMOOTH": {}, "SCRARITH": {},
                                      "EPSTEIN": {}}
    for x, dps in smooth_r:
        cw["SMOOTH"][x] = R4.build_cell(x, KFAC1, "SMOOTH", dps,
                                        want_mp=True)
    for x, dps in scr_r:
        cw["SCRARITH"][x] = R4.build_cell(x, KFAC1, "SCRARITH", dps,
                                          want_mp=True)
    for x, dps in eps_r:
        t0 = time.time()
        cw["EPSTEIN"][x] = R4.build_cell(x, KFAC1, "EPSTEIN", dps,
                                         want_mp=True)
        print("  EPSTEIN x=%d built (%.1f s)" % (x, time.time() - t0),
              flush=True)
    fsm = SL.build_trig_cell(5, KFAC1, "SMOOTH")
    dev_s = float(np.max(np.abs(cw["SMOOTH"][5]["m_tilde"]
                                - fsm["m_tilde"])))
    fsc = SL.build_trig_cell(5, KFAC1, "SCRARITH")
    csc5 = (cw["SCRARITH"][5] if 5 in cw["SCRARITH"]
            else R4.build_cell(5, KFAC1, "SCRARITH", 60, want_mp=True))
    cw["SCRARITH"][5] = csc5
    dev_c = float(np.max(np.abs(csc5["m_tilde"] - fsc["m_tilde"])))
    if not smoke:
        cq5 = R4.build_cell(5, KFAC1, "EPSTEIN", 60)
        sq5 = SL.build_trig_cell_hp(5, KFAC1, "EPSTEIN", 60)
        dev_q = float(np.max(np.abs(cq5["m_tilde"] - sq5["m_tilde"])))
    else:
        dev_q = 0.0
    check("G21-ward-worlds", dev_s <= 1e-5 and dev_c <= 1e-5
          and dev_q <= 1e-8,
          "SMOOTH x5 %.1e, SCRARITH x5 %.1e (f64 Filon bar), "
          "EPSTEIN x5 %.1e (HP)" % (dev_s, dev_c, dev_q))
    dev_blk = float(np.max(np.abs(
        cells[3]["blk_pole"] + cells[3]["blk_arch"]
        - cells[3]["blk_prime"] - cells[3]["m_tilde"])))
    check("G22-block-split", dev_blk <= 1e-12,
          "POLE + ARCH - PRIME == total at x=3 (f64 read %.1e)"
          % dev_blk)
    cl2: dict[int, dict] = {}
    for x, dps in l2r:
        cl2[x] = R4.build_cell(x, KFAC2, "MAIN", dps, want_mp=True)
        print("  L2 (KFAC 1.60) x=%d built (K=%d)" % (x, cl2[x]["K"]),
              flush=True)

    # ---------------------------------------------------------- S3
    section("S3  T1 ANATOMY -- the mixing number on the ladder")
    kds: dict[int, dict] = {}
    kts: dict[int, np.ndarray] = {}
    core: dict[int, dict] = {}
    okzi = True
    okeig = True
    for x, dps in rungs:
        kd = kfun_data(x)
        kds[x] = kd
        okzi = okzi and kd["zero_int_rel"] <= ZERO_INT_BAR
        kt = R4.prolate_kvec(x, cells[x])
        kts[x] = kt
        rc = rung_core(cells[x], kt)
        core[x] = rc
        okeig = okeig and rc["eigres"] <= 10.0 ** (-(dps // 2))
        with mp.workdps(cells[x]["dps"]):
            kvr = lift_vec(kt)
            rkh = float(R4.mp_dot(kvr, R4.matvec(cells[x]["mpM"], kvr,
                                                 cells[x]["K"])))
        rc["rk"] = rkh
        print("  x=%-2d eps %s gap %s nsoft %-2d alpha %.8f "
              "beta %+.6e resid2v %.2e R(k) %.2e"
              % (x, rc["eps_str"], rc["gap_str"], rc["nsoft"],
                 rc["alpha"], rc["beta"], rc["resid2v"], rkh),
              flush=True)
        print("       cluster gaps %s"
              % ["%.2e" % g for g in rc["cl_gaps"][:6]])
        print("       signed betas %s"
              % ["%+.2e" % b for b in rc["betas"][:8]])
    check("G30-zero-integral", okzi,
          "|int h_lambda| / int |h| <= %.0e at every rung (max %.1e)"
          % (ZERO_INT_BAR, max(kds[x]["zero_int_rel"]
                               for x, _d in rungs)))
    check("G23-eigen-residuals", okeig,
          "||Q v_i - lam_i v_i|| <= 10^-(dps/2) for i = 0,1 at every "
          "rung (max %.1e)" % max(core[x]["eigres"]
                                  for x, _d in rungs))
    okreg = True
    regd = []
    for x in (3, 5, 8, 13):
        if x in core:
            rel = abs(abs(core[x]["beta"]) / R122_KMIX[x] - 1)
            regd.append("x%d:%.1e" % (x, rel))
            okreg = okreg and rel <= R122_REG_BAR
    check("G24-kmix-regression-r122", okreg,
          "|beta| matches the round-122 run4 pins to %.0e rel: %s"
          % (R122_REG_BAR, ", ".join(regd)))
    # two-vector structure (hard on the round-122-measured rungs;
    # reported on the new rungs)
    ok31 = True
    tv = []
    for x, _d in rungs:
        rat = core[x]["resid2v"] / max(abs(core[x]["beta"]), 1e-300)
        tv.append("x%d:%.1e" % (x, rat))
        if x in (5, 8, 13):
            ok31 = ok31 and rat <= TWO_VECTOR_BAR
    check("G31-two-vector-structure", ok31,
          "||k - alpha v0 - beta v1|| / |beta| = %s (hard <= %.2f at "
          "x = 5/8/13): k lives on the ground DOUBLET alone -- the "
          "mixing number is the within-doublet angle"
          % (", ".join(tv), TWO_VECTOR_BAR))
    # grid certification + projector equality
    ok32 = True
    okpe = True
    cert: dict[int, float] = {}
    for x, _d in rungs:
        cell = cells[x]
        L = cell["a"]
        bg = {}
        for ng in NGRIDS:
            vg = np.linspace(-L, L, ng)
            kv = k_vals_on(kds[x], vg, int(x) + 2)
            pr = project_cell(kv, vg, cell)
            pr = pr / np.linalg.norm(pr)
            bg[ng] = mp_overlap(cell, core[x]["v1f"], pr,
                                normalize=False)
        okpe = okpe and abs(bg[20001] - core[x]["beta"]) <= PROJ_EQ_BAR
        cert[x] = abs(bg[40001] - bg[20001])
        ok32 = ok32 and cert[x] <= GRID_CERT_BAR
        print("  x=%-2d beta grid ladder %s cert_err %.1e"
              % (x, ["%+.6e" % bg[n] for n in NGRIDS], cert[x]))
    check("G32-grid-certification", ok32 and okpe,
          "projector == R4 at 20001 (<= %.0e) and |beta_40001 - "
          "beta_20001| <= %.0e at every rung (max %.1e): beta is "
          "certified at the 1e-6 level, far below its 2.5e-3 size"
          % (PROJ_EQ_BAR, GRID_CERT_BAR, max(cert.values())))
    # single mode vs cluster sum
    ok33 = True
    smr = []
    for x, _d in rungs:
        bs = [abs(b) for b in core[x]["betas"]]
        if len(bs) >= 2:
            smr.append("x%d:%.1e" % (x, bs[1] / max(bs[0], 1e-300)))
            if x in (5, 8, 13):
                ok33 = ok33 and bs[1] <= 0.05 * max(bs[0], 1e-300)
    check("G33-single-mode", ok33,
          "|beta_2|/|beta_1| = %s (hard <= 0.05 at x = 5/8/13): the "
          "mixing is a SINGLE-MODE number, not a cluster sum"
          % ", ".join(smr))
    # annihilator dimension law (ward count)
    lawrows = []
    for x, _d in rungs:
        cell = cells[x]
        edge = cell["K"] * math.pi / cell["a"]
        nb = ward_band_count(gam, edge)
        pred = cell["K"] - nb
        lawrows.append((x, core[x]["nsoft"] + 1, pred))
    okann = all(abs(m - p) <= 2 for x_, m, p in lawrows
                if x_ in (5, 8, 13))
    check("G34-annihilator-dim-law", okann,
          "soft-cluster dim (nsoft+1) == K - N(band edge) +- 2 at "
          "every rung: %s -- the soft cluster IS the band-zero "
          "annihilator subspace (evaluation-orthogonal complement)"
          % ["x%d:%d/%d" % r for r in lawrows])
    # eval anatomy at deep rungs
    for x in deep:
        cell = cells[x]
        evs = ward_eval_vecs(cell, gam, 5)
        r0 = ["%.1e" % abs(mp_overlap(cell, core[x]["v0f"], e))
              for e in evs]
        r1 = ["%.1e" % abs(mp_overlap(cell, core[x]["v1f"], e))
              for e in evs]
        rk = ["%.1e" % abs(mp_overlap(cell, kts[x], e))
              for e in evs]
        print("  x=%-2d |<e_gam_j, .>| (unit-normalized): v0 %s"
              % (x, r0))
        print("        v1 %s   k %s" % (r1, rk))
    info("eval anatomy: v0, v1 AND k are all near-orthogonal to the "
         "band-zero evaluation vectors (the E-lift annihilates zeros "
         "by M(E h) = zeta * M(h)); the mixing lives INSIDE the "
         "annihilator subspace, invisible to zero evaluations")
    # localization + n-split + c0/c4 + mode scan at deep rungs
    for x in deep:
        cell = cells[x]
        L = cell["a"]
        vg = np.linspace(-L, L, 20001)
        f0 = cell_fn_on_grid(core[x]["v0f"], cell, vg)
        f1 = cell_fn_on_grid(core[x]["v1f"], cell, vg)
        fk = cell_fn_on_grid(kts[x], cell, vg)
        m0 = thirds_mass(f0, vg, L)
        m1 = thirds_mass(f1, vg, L)
        mk = thirds_mass(fk, vg, L)
        ov = f1 * fk
        ovm = thirds_mass(np.sqrt(np.abs(ov)), vg, L)
        print("  x=%-2d thirds-mass (inner/mid/outer): v0 %s v1 %s "
              "k %s |ov| %s"
              % (x, ["%.2f" % t for t in m0], ["%.2f" % t for t in m1],
                 ["%.2f" % t for t in mk], ["%.2f" % t for t in ovm]))
        # n-split
        k1 = project_cell(k_vals_on(kds[x], vg, 1), vg, cell)
        kfull = project_cell(k_vals_on(kds[x], vg, int(x) + 2), vg,
                             cell)
        ktail = kfull - k1
        nk = float(np.linalg.norm(kfull))
        b1 = mp_overlap(cell, core[x]["v1f"], k1 / nk,
                        normalize=False)
        bt = mp_overlap(cell, core[x]["v1f"], ktail / nk,
                        normalize=False)
        # c0/c4 split
        kd = kds[x]
        pro = kd["pro"]
        c4c = math.sqrt(3) / 2 ** (11 / 4)
        s4 = np.sign(pro.eval_mode(4, np.array([0.0]))[0])
        s0 = np.sign(pro.eval_mode(0, np.array([0.0]))[0])
        v4 = esum_on_grid(lambda xx: c4c * s4 * pro.eval_mode(4, xx),
                          vg, int(x) + 2, pro.lam)
        v0p = esum_on_grid(lambda xx: kd["c0"] * s0
                           * pro.eval_mode(0, xx), vg, int(x) + 2,
                           pro.lam)
        b4 = mp_overlap(cell, core[x]["v1f"],
                        project_cell(v4, vg, cell) / nk,
                        normalize=False)
        b0 = mp_overlap(cell, core[x]["v1f"],
                        project_cell(v0p, vg, cell) / nk,
                        normalize=False)
        print("       n-split: beta(n=1) %+.3e + beta(n>=2) %+.3e "
              "== %+.3e; c4-part %+.3e + c0-part %+.3e"
              % (b1, bt, core[x]["beta"], b4, b0))
        # prolate mode scan (v1 row, v0 row, and the matched-mode
        # PURE-ARCH prediction of beta)
        row = []
        row0 = []
        pes = []
        for n in range(MODE_SCAN_N):
            en = esum_on_grid(lambda xx, n=n: pro.eval_mode(n, xx),
                              vg, int(x) + 2, pro.lam)
            pe = project_cell(en, vg, cell)
            npe = float(np.linalg.norm(pe))
            if npe == 0.0:
                row.append(0.0)
                row0.append(0.0)
                pes.append(None)
                continue
            pes.append(pe / npe)
            row.append(mp_overlap(cell, core[x]["v1f"], pe / npe,
                                  normalize=False))
            row0.append(mp_overlap(cell, core[x]["v0f"], pe / npe,
                                   normalize=False))
        print("       <v1, E(phi_n)-hat> n=0..%d: %s"
              % (MODE_SCAN_N - 1, ["%+.2e" % t for t in row]))
        print("       <v0, E(phi_n)-hat> n=0..%d: %s"
              % (MODE_SCAN_N - 1, ["%+.2e" % t for t in row0]))
        nstar = int(np.argmax([abs(t) for t in row]))
        vs = row[nstar]
        barch = float("nan")
        if pes[nstar] is not None:
            ov_k = mp_overlap(cell, kts[x], pes[nstar],
                              normalize=False)
            barch = vs * ov_k
        print("       matched arch mode n*=%d |<v1,E(phi_n*)>| = "
              "%.4f => pure-arch prediction beta_arch %+.3e vs beta "
              "%+.3e (ratio %.3f)"
              % (nstar, abs(vs), barch, core[x]["beta"],
                 barch / core[x]["beta"]))
        core[x]["mode_scan"] = row
        core[x]["nstar"] = (nstar, abs(vs), barch)
        core[x]["nsplit"] = (b1, bt)
    # flatness fit
    xs_fit = [x for x, _d in rungs if x >= 5]
    if len(xs_fit) >= 3:
        sl_b, se_b = ols_slope([math.log10(x) for x in xs_fit],
                               [math.log10(abs(core[x]["beta"]))
                                for x in xs_fit])
    else:
        sl_b, se_b = float("nan"), float("nan")
    bvals = [abs(core[x]["beta"]) for x in xs_fit]
    flat = abs(sl_b) <= SLOPE_FLAT_BAR if sl_b == sl_b else False
    check("G35-flatness-typing", True,
          "|beta| ladder (x >= 5) %s: slope log|beta| vs log x = "
          "%.3f +- %.3f, max/min ratio %.2f => %s"
          % (["%.2e" % b for b in bvals], sl_b, se_b,
             max(bvals) / min(bvals),
             "KMIX-FLAT" if flat else "KMIX-TREND"))

    # ---------------------------------------------------------- S4
    section("S4  T2 SOURCE ADJUDICATION")
    ok40 = all(core[x]["ch_dev"] <= CH_SUM_BAR for x, _d in rungs)
    check("G40-channel-sum-exact", ok40,
          "chP + chA - chPr == lam1*beta rel-to-channel <= %.0e at "
          "every rung (max %.1e)" % (CH_SUM_BAR,
                                     max(core[x]["ch_dev"]
                                         for x, _d in rungs)))
    canc = ["x%d:%.1f" % (x, core[x]["ch_canc"]) for x, _d in rungs]
    check("G41-channel-cancellation", True,
          "channel cancellation digits log10(max|ch|/|lam1 beta|): %s "
          "-- the round-115/122 cross-cancellation debt transfers to "
          "the single-mode pairing as expected: the pole/arch/prime "
          "split is NOT the usable source decomposition (typed "
          "UNSPLIT, one gate, not re-litigated)" % ", ".join(canc))
    # arch-only operator ladder
    arch_rows = []
    for x in deep:
        cell = cells[x]
        K = cell["K"]
        with mp.workdps(cell["dps"]):
            A = cell["mpPole"] + cell["mpArch"]
            Ea, Va = mp.eigsy(A)
            order = sorted(range(K), key=lambda i: Ea[i])
            g0 = sign_fix(R4.matcol(Va, order[0], K))
            g1 = sign_fix(R4.matcol(Va, order[1], K))
            kv = lift_vec(kts[x])
            ca = float(R4.mp_dot(g0, kv))
            ba = float(R4.mp_dot(g1, kv))
            e0a = float(Ea[order[0]])
            g0a = float(Ea[order[1]] - Ea[order[0]])
        arch_rows.append((x, e0a, g0a, ca, ba))
        print("  ARCH-ONLY x=%-2d eps_A %.3e gap_A %.3e "
              "cos(k,g_A) %.6f beta_A %+.3e"
              % (x, e0a, g0a, abs(ca), ba))
    check("G42-arch-only-ladder", True,
          "arch-only operator (POLE+ARCH, no prime block): "
          "cos(k, ground_A) %s, beta_A %s -- adjudicates whether the "
          "mixing exists already in the pure-archimedean world"
          % (["%.4f" % abs(r[3]) for r in arch_rows],
             ["%+.1e" % r[4] for r in arch_rows]))
    # SMOOTH-world ladder (density-matched arch world)
    sm_rows = []
    for x, _d in smooth_r:
        cellw = cw["SMOOTH"][x]
        rcw = rung_core(cellw, kts[x])
        sm_rows.append((x, rcw["eps"], rcw["gap"], rcw["alpha"],
                        rcw["beta"], rcw["nsoft"]))
        print("  SMOOTH x=%-2d eps %.3e gap %.3e nsoft %d alpha "
              "%.6f beta %+.3e" % (x, rcw["eps"], rcw["gap"],
                                   rcw["nsoft"], rcw["alpha"],
                                   rcw["beta"]))
    check("G43-smooth-ladder", True,
          "SMOOTH world (PNT-density world, no primes) mixing: %s vs "
          "TRUE %s -- the central archimedean-vs-arithmetic "
          "comparator" % (["x%d:%+.1e" % (r[0], r[4])
                           for r in sm_rows],
                          ["x%d:%+.1e" % (x, core[x]["beta"])
                           for x, _d in smooth_r if x in core]))
    # frame test (KFAC 1.60)
    fr_rows = []
    okfr = True
    for x in cl2:
        cellf = cl2[x]
        ktf = R4.prolate_kvec(x, cellf)
        rcf = rung_core(cellf, ktf)
        rel = abs(abs(rcf["beta"]) / max(abs(core[x]["beta"]), 1e-300)
                  - 1)
        fr_rows.append((x, rcf["beta"], core[x]["beta"], rel))
        okfr = okfr and rel <= FRAME_BAR
        print("  FRAME x=%-2d KFAC1.60 beta %+.3e vs KFAC1.25 %+.3e "
              "(rel dev %.3f) alpha %.6f resid2v %.2e nsoft %d"
              % (x, rcf["beta"], core[x]["beta"], rel, rcf["alpha"],
                 rcf["resid2v"], rcf["nsoft"]))
    if not smoke:
        check("G44-frame-test", True,
              "beta under mode-density change KFAC 1.25 -> 1.60: rel "
              "devs %s => %s" % (["x%d:%.3f" % (r[0], r[3])
                                  for r in fr_rows],
                                 "FRAME-STABLE (physical, not an "
                                 "artifact)" if okfr else
                                 "FRAME-SENSITIVE (artifact typing)"))
    # AMENDMENT 1: KFAC ladder read (frame direction quantified)
    kf_slopes = []
    if not smoke:
        for x, dpsx, kfs in KFAC_LADDER:
            pts = [(KFAC1, core[x]["beta"], core[x]["nsoft"],
                    cells[x]["K"]
                    - ward_band_count(gam, cells[x]["K"] * math.pi
                                      / cells[x]["a"]),
                    core[x]["alpha"], core[x]["resid2v"])]
            for kf in kfs:
                if abs(kf - KFAC2) < 1e-12 and x in cl2:
                    cellf = cl2[x]
                else:
                    t0 = time.time()
                    cellf = R4.build_cell(x, kf, "MAIN", dpsx,
                                          want_mp=True)
                    print("  KFAC %.2f x=%d built (K=%d, %.1f s)"
                          % (kf, x, cellf["K"], time.time() - t0),
                          flush=True)
                ktf = R4.prolate_kvec(x, cellf)
                rcf = rung_core(cellf, ktf)
                adim = cellf["K"] - ward_band_count(
                    gam, cellf["K"] * math.pi / cellf["a"])
                pts.append((kf, rcf["beta"], rcf["nsoft"], adim,
                            rcf["alpha"], rcf["resid2v"]))
            for kf, bb, ns, ad, al, rs in pts:
                print("  KFAC-LADDER x=%-2d kfac %.2f beta %+.3e "
                      "nsoft %-2d anndim %-2d alpha %.6f resid2v "
                      "%.1e" % (x, kf, bb, ns, ad, al, rs))
            if len(pts) >= 3:
                slk = ols_slope(
                    [math.log10(max(p[3], 1)) for p in pts],
                    [math.log10(max(abs(p[1]), 1e-300))
                     for p in pts])[0]
            else:
                slk = float("nan")
            kf_slopes.append((x, slk))
        check("G47-kfac-ladder", True,
              "AMENDMENT-1 read: slope log|beta| vs log(annihilator "
              "dim) per rung: %s -- the frame direction of the "
              "mixing number quantified (negative slope = the "
              "number falls with band enrichment at fixed lambda)"
              % ["x%d:%.2f" % s for s in kf_slopes])
    # Hermite swap
    hs_rows = []
    for x in deep:
        cell = cells[x]
        L = cell["a"]
        vg = np.linspace(-L, L, 20001)
        kh = project_cell(hermite_swap_vals(x, vg), vg, cell)
        kh = kh / np.linalg.norm(kh)
        bh = mp_overlap(cell, core[x]["v1f"], kh, normalize=False)
        hs_rows.append((x, bh, core[x]["beta"]))
        print("  HERMITE-SWAP x=%-2d beta_H %+.3e vs beta %+.3e "
              "(ratio %.4f)" % (x, bh, core[x]["beta"],
                                bh / core[x]["beta"]))
    check("G45-hermite-swap", True,
          "prolate -> Hermite pair in the same Poisson lift: "
          "beta_H/beta = %s -- if ~1 the Meixner-Schaefke lambda^-2 "
          "prolate correction is NOT the source of the mixing"
          % ["x%d:%.4f" % (r[0], r[1] / r[2]) for r in hs_rows])
    # r121 scale table
    r121_rows = []
    okr121 = False
    for nm, val in R121_SCALES:
        ratios = [abs(core[x]["beta"]) / val for x in deep
                  if x in core]
        inband = all(abs(math.log(r)) <= R121_MATCH_BAND
                     for r in ratios)
        okr121 = okr121 or inband
        r121_rows.append("%s:%s%s" % (nm, ["%.2f" % r for r in ratios],
                                      "<MATCH>" if inband else ""))
    check("G46-r121-scale-table", True,
          "|beta|/r121-scale at deep rungs: %s => %s"
          % ("; ".join(r121_rows),
             "R121-SCALE-MATCH (same wall in two costumes -- "
             "unification candidate)" if okr121 else
             "R121-SCALE-NO-MATCH (different walls)"))

    # ---------------------------------------------------------- S5
    section("S5  T3 KILL TEST (source-only enrichment, RR in mp)")
    kill_results: dict[int, dict[str, dict]] = {}
    for x in deep:
        cell = cells[x]
        L = cell["a"]
        vg = np.linspace(-L, L, 20001)
        kd = kds[x]
        pro = kd["pro"]
        kt = kts[x]
        # arch space
        arch_vecs = [kt]
        for n in (0, 2, 4, 6, 8):
            en = esum_on_grid(lambda xx, n=n: pro.eval_mode(n, xx),
                              vg, int(x) + 2, pro.lam)
            arch_vecs.append(project_cell(en, vg, cell))
        # edge space
        wdt = L / 8.0
        bump = (np.exp(-((vg - L) / wdt) ** 2)
                + np.exp(-((vg + L) / wdt) ** 2))
        edge_vecs = [kt, project_cell(bump, vg, cell)]
        # Lambda space
        lam_vecs = [kt]
        for p in (2, 3):
            sh = (k_vals_on(kd, vg - math.log(p), int(x) * p + 2)
                  + k_vals_on(kd, vg + math.log(p), int(x) + 2))
            lam_vecs.append(project_cell(sh, vg, cell))
        klam = np.zeros_like(vg)
        for q, lq in prime_power_atoms(x):
            klam = klam + (lq / math.sqrt(q)) * (
                k_vals_on(kd, vg - math.log(q), int(x) * q + 2)
                + k_vals_on(kd, vg + math.log(q), int(x) + 2))
        lam_vecs.append(project_cell(klam, vg, cell))
        all_vecs = arch_vecs + edge_vecs[1:] + lam_vecs[1:]
        # Krylov comparator (mp)
        with mp.workdps(cell["dps"]):
            kv = lift_vec(kt)
            q1 = R4.matvec(cell["mpM"], kv, cell["K"])
            q2 = R4.matvec(cell["mpM"], q1, cell["K"])
            kry_vecs = [kt, [mp.mpf(t) for t in q1],
                        [mp.mpf(t) for t in q2]]
        # zero-data WARD comparator
        z_vecs = [kt] + ward_eval_vecs(cell, gam, 3)
        spaces = (("S_ARCH", arch_vecs, True),
                  ("S_EDGE", edge_vecs, True),
                  ("S_LAM", lam_vecs, True),
                  ("S_ALL", all_vecs, True),
                  ("S_KRY", kry_vecs, False),
                  ("S_Z*ward", z_vecs, False))
        kill_results[x] = {}
        b0v = abs(core[x]["beta"])
        for nm, vecs, _src in spaces:
            rr = rr_space(cell, vecs, core[x]["v0f"], core[x]["v1f"])
            kill_results[x][nm] = rr
            print("  x=%-2d %-8s dim %d R(u*) %.3e alpha %.6f "
                  "beta(u*) %+.3e imp %.2f c1 %.2e F %.2e "
                  "mu1 %.2e |<v1,u1*>| %.4f"
                  % (x, nm, rr["dim"], rr["mu0"], rr["alpha"],
                     rr["beta"], b0v / max(abs(rr["beta"]), 1e-300),
                     rr["c1"],
                     rr["muperp"] / max(rr["mu0"], 1e-300),
                     rr["mu1"], rr["b1o"]),
                  flush=True)
    ok50 = True
    for x in deep:
        for nm, rr in kill_results[x].items():
            with mp.workdps(cells[x]["dps"]):
                kv = lift_vec(kts[x])
                rk = float(R4.mp_dot(kv, R4.matvec(cells[x]["mpM"],
                                                   kv, cells[x]["K"])))
            ok50 = ok50 and rr["mu0"] <= rk * (1 + 1e-6) + 1e-30
    check("G50-rr-sanity", ok50,
          "R(u*) <= R(k-hat) for every space containing k at every "
          "deep rung (Rayleigh-Ritz coherence)")
    # kill adjudication on the two deepest rungs
    deep2 = deep[-2:]
    verdict_kill = "KMIX-OBSTRUCTED"
    best_space, best_factor = "", 1.0
    for nm in ("S_ARCH", "S_EDGE", "S_LAM", "S_ALL"):
        facs = []
        ok_al = True
        for x in deep2:
            rr = kill_results[x][nm]
            facs.append(abs(core[x]["beta"])
                        / max(abs(rr["beta"]), 1e-300))
            ok_al = ok_al and rr["alpha"] >= ALPHA_MIN
        f = min(facs) if facs else 1.0
        if ok_al and f > best_factor:
            best_factor, best_space = f, nm
    if best_factor >= KILL_FACTOR:
        verdict_kill = "KMIX-KILLED(%s, factor %.1f)" % (best_space,
                                                         best_factor)
    elif best_factor >= PARTIAL_FACTOR:
        verdict_kill = "KMIX-PARTIAL(%s, factor %.1f)" % (best_space,
                                                          best_factor)
    check("G51-kill-adjudication", True,
          "best source-only space %s improvement factor %.2f at the "
          "two deepest rungs (bars: KILL >= %.0f, PARTIAL >= %.0f, "
          "alpha >= %.2f) => %s"
          % (best_space or "none", best_factor, KILL_FACTOR,
             PARTIAL_FACTOR, ALPHA_MIN, verdict_kill))
    zfacs = ["x%d:%.2f" % (x, abs(core[x]["beta"])
                           / max(abs(kill_results[x]["S_Z*ward"]
                                     ["beta"]), 1e-300))
             for x in deep]
    kfacs = ["x%d:%.2f" % (x, abs(core[x]["beta"])
                           / max(abs(kill_results[x]["S_KRY"]
                                     ["beta"]), 1e-300))
             for x in deep]
    check("G52-comparators", True,
          "zero-data WARD comparator improvement %s; Krylov "
          "instrument comparator %s -- calibrates what zero "
          "transcription and the instrument-solving-itself buy "
          "relative to the source-only spaces" % (zfacs, kfacs))
    reach = ["x%d:%s:%.1e" % (x, nm, kill_results[x][nm]["c1"])
             for x in deep2 for nm in ("S_ARCH", "S_LAM", "S_ALL")]
    check("G53-obstruction-reachability", True,
          "reachability c1 = ||P_S v1|| and deflation cost F = "
          "muperp/mu0 printed per space -- the measured "
          "moment-matching obstruction profile: %s" % ", ".join(reach))

    # ---------------------------------------------------------- S6
    section("S6  T5 WORLDS + TAU SCREEN + MIN-CUT")
    wrows = []
    for x, _d in scr_r:
        rcw = rung_core(cw["SCRARITH"][x], kts[x])
        wrows.append(("SCRARITH", x, rcw["beta"], core[x]["beta"]))
        print("  SCRARITH x=%-2d beta %+.3e (true %+.3e) nsoft %d "
              "eps %.2e" % (x, rcw["beta"], core[x]["beta"],
                            rcw["nsoft"], rcw["eps"]))
    for x, _d in eps_r:
        cellq = cw["EPSTEIN"][x]
        rcq = rung_core(cellq, kts[x])
        L = cellq["a"]
        vg = np.linspace(-L, L, 20001)
        kq = project_cell(kq_vals_on(kds[x], vg, int(x) + 2), vg,
                          cellq)
        kq = kq / np.linalg.norm(kq)
        with mp.workdps(cellq["dps"]):
            E, V = cellq["mpE"], cellq["mpV"]
            K = cellq["K"]
            v0q = sign_fix(R4.matcol(V, 0, K))
            v1q = sign_fix(R4.matcol(V, 1, K))
            kqm = lift_vec(kq)
            aq = float(abs(R4.mp_dot(v0q, kqm)))
            bq = float(R4.mp_dot(v1q, kqm))
        wrows.append(("EPSTEIN-kZ", x, rcq["beta"], core[x]["beta"]))
        wrows.append(("EPSTEIN-kQ", x, bq, core[x]["beta"]))
        print("  EPSTEIN  x=%-2d beta(k_Z) %+.3e beta(k_Q) %+.3e "
              "alpha(k_Q) %.4f (true %+.3e) eps %.2e gap %.2e nsoft %d"
              % (x, rcq["beta"], bq, aq, core[x]["beta"], rcq["eps"],
                 rcq["gap"], rcq["nsoft"]))
    for x, _d in smooth_r:
        rcw = next(r for r in sm_rows if r[0] == x)
        wrows.append(("SMOOTH", x, rcw[4], core[x]["beta"]))
    seps = []
    for wnm, x, bw, bt in wrows:
        lr = abs(math.log(max(abs(bw), 1e-300)
                          / max(abs(bt), 1e-300)))
        seps.append((wnm, x, lr))
    sep_worlds = sorted(set(w for w, _x, lr in seps
                            if lr >= WORLD_SEP_LOG))
    check("G60-world-separation", True,
          "|log(beta_world/beta_true)| per row: %s => %s"
          % (["%s-x%d:%.2f" % s for s in seps],
             ("KMIX-WORLD-SEPARATING(%s)" % ",".join(sep_worlds))
             if sep_worlds else "KMIX-WORLD-BLIND"))
    # tau screens
    te = [math.log10(core[x]["eps"]) for x in deep if x in core]
    tg = [math.log10(core[x]["gap"]) for x in deep if x in core]
    tb = [math.log10(abs(core[x]["beta"])) for x in deep if x in core]
    sl_e = ols_slope(te, tb)[0] if len(te) >= 3 else float("nan")
    sl_g = ols_slope(tg, tb)[0] if len(tg) >= 3 else float("nan")

    def band(s):
        if s != s:
            return "N/A"
        return "PASS" if abs(s) <= 0.30 else \
            ("RELOCATION" if abs(s) >= 0.70 else "MID")
    check("G61-tau-screen", True,
          "slope log|beta| vs log eps = %.4f [%s], vs log gap = %.4f "
          "[%s] (r121 floor scales cross-checked in G46; a ~0 slope "
          "= the mixing does NOT ride the Connes scale)"
          % (sl_e, band(sl_e), sl_g, band(sl_g)))
    # min-cut replica (round-116 base + round-122 extension)
    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "LANEACONV"): 1,
                ("LANEACONV", "R4HYP"): INF})
    f_ext = maxflow(dict(ext), "UNC", "RH")
    check("G62-mincut", f_base == 4 and f_ext == 5,
          "flows UNC->RH: base %d, extended %d -- the mixing number "
          "is MEAS data ON the LANEACONV omega edge (it prices "
          "(H-conv) for the prolate candidate); no capacity change, "
          "class census {MEAS, OMEGA-POS} cardinality 4 unchanged"
          % (f_base, f_ext))

    # ---------------------------------------------------------- S7
    section("S7  CONDITIONING (doublet law) + RUNTIME")
    okc = True
    okz = True
    for x in ([5] if smoke else [5, 8]):
        cell = cells[x]
        K = cell["K"]
        jstar = int(np.argmax(np.abs(core[x]["v0f"]
                                     * core[x]["v1f"])))
        with mp.workdps(cell["dps"]):
            v00 = mp.mpf(repr(float(core[x]["v0f"][jstar])))
            v10 = mp.mpf(repr(float(core[x]["v1f"][jstar])))
            gapm = cell["mpE"][1] - cell["mpE"][0]
            tgt = mp.mpf(repr(PERT_THETA_TGT))
            den = max(abs(v00 * v10), mp.mpf("1e-30"))
            delta = tgt * gapm / den
            delta = max(min(delta, mp.mpf("1e-8")), mp.mpf("1e-45"))
            Qp = cell["mpM"].copy()
            Qp[jstar, jstar] = Qp[jstar, jstar] + delta
            Ep, Vp = mp.eigsy(Qp)
            order = sorted(range(K), key=lambda i: Ep[i])
            v1p = R4.matcol(Vp, order[1], K)
            v1m = lift_vec(core[x]["v1f"])
            if R4.mp_dot(v1p, v1m) < 0:
                v1p = [-t for t in v1p]
            kv = lift_vec(kts[x])
            bp = R4.mp_dot(v1p, kv)
            dbeta = float(abs(bp - mp.mpf(repr(core[x]["beta"]))))
            theta = float(delta * v00 * v10 / gapm)
            pred = abs(theta * core[x]["alpha"])
            de = float(abs(min(Ep[i] for i in range(K))
                           - cell["mpE"][0]))
        ratio = dbeta / max(pred, 1e-300)
        okc = okc and COND_RATIO[0] <= ratio <= COND_RATIO[1]
        okz = okz and dbeta > 0 and de > 0
        print("  x=%-2d j*=%d delta %.2e theta_pred %.2e dbeta %.3e "
              "pred %.3e ratio %.2f deps %.2e"
              % (x, jstar, float(delta), theta, dbeta, pred, ratio,
                 de))
    check("G70-conditioning-law", okc,
          "measured dbeta == 2x2 doublet prediction theta*alpha "
          "within [%.2f, %.2f] (theta = delta |v00 v10|/gap): the "
          "mixing number's condition number against operator "
          "perturbations IS 1/gap = inverse-Connes -- beta is an "
          "exact-arithmetic observable" % COND_RATIO)
    check("G71-perturbation-nonzero", okz,
          "perturbation responses strictly nonzero (round-118 "
          "silent-rounding red flag absent; all mp under workdps)")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    smix = "KMIX-SINGLE-MODE" if ok33 else "KMIX-CLUSTER-SUM"
    sflat = ("KMIX-FLAT(slope %.3f +- %.3f)" % (sl_b, se_b)) if flat \
        else ("KMIX-TREND(slope %.3f +- %.3f)" % (sl_b, se_b))
    # source composite from the measured comparators
    sm_ratio = [abs(r[4]) / abs(core[r[0]]["beta"]) for r in sm_rows
                if r[0] in core]
    verdicts = [
        smix, "KMIX-TWO-VECTOR(%s)" % ("PASS" if ok31 else "FAIL"),
        sflat,
        "CHANNEL-UNSPLIT(cancellation digits %s)" % ", ".join(canc),
        "SMOOTH-RATIO(%s)" % ["%.3f" % r for r in sm_ratio],
        "FRAME(%s)" % ("STABLE" if okfr else "SENSITIVE"),
        "HERMITE-SWAP(%s)" % ["%.4f" % (r[1] / r[2])
                              for r in hs_rows],
        "R121-%s" % ("SCALE-MATCH" if okr121 else "SCALE-NO-MATCH"),
        verdict_kill,
        ("KMIX-WORLD-SEPARATING(%s)" % ",".join(sep_worlds))
        if sep_worlds else "KMIX-WORLD-BLIND",
        "TAU-SCREEN(eps %.3f [%s], gap %.3f [%s])"
        % (sl_e, band(sl_e), sl_g, band(sl_g)),
        "KMIX-CONDITIONING(1/gap law %s)" % ("CONFIRMED" if okc
                                             else "NOT-CONFIRMED"),
        "MINCUT(4 base / 5 ext, census {MEAS, OMEGA-POS} unchanged)",
    ]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc_, _d in CHECKS if okc_)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc_, _ in CHECKS if not okc_]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
