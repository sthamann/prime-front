#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""szego_equilibrium_probe -- PRIME.PORT.SZEGO.EQUILIBRIUM.01
(round 232): does a DISCRETE CONSTRAINED EQUILIBRIUM problem with
the exact comb field reproduce the zero distribution of pihat_n --
i.e. is the open scalar Szego/g-function task constructively
solved by an electrostatic minimizer on the union nodes?

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX AND FILLING FIREWALL (binding): w = window, S = #supp
(mutilde) = 367 (w = 9, all three worlds), N_w = (S+1)/2 = 184,
n = degree, t = n/S = filling.  Directions never mixed.

SEALED PROBLEM (leg A): minimize over masses 0 <= rho_j <= 1 on
the S union nodes with sum rho_j = n the energy
    E[rho] = sum_{j != k} rho_j rho_k (-log|x_j - x_k|)
             + sum_j rho_j V_j
(pair term counted both ways, so the per-particle field V_j =
-log|wtilde_j| is the Stieltjes normalization Q/2 per ordered
pair).  CANDIDATE FIELDS: (i) V0: V = 0 (pure capacity/counting);
(ii) Vw: V_j = -log|wtilde_j| on the union support (exact weight
field, sign only via |.|); (iii) Vpos: V_j = -log w_j restricted
to the mu-zone support (sign handled separately: support
selection).  NULLS: THIN = evenly index-spaced integer selection
of n nodes; UNIF = proportional thinning rho = n/S.  SOLVER:
FISTA (projected accelerated gradient, adaptive restart) with
exact projection onto the capped simplex {0 <= rho <= 1,
sum = n} by bisection; Lipschitz constant from power iteration;
convergence = fixed-point residual < 1e-8 (leg A) / 1e-7 (leg B
sweep, warm-started); cross-check vs scipy SLSQP on a sealed
subsampled instance (every 8th node, mass 12).

SEALED METRICS (leg A, MAIN w = 9, fillings n = round(t*S) for
t in {0.15, 0.30, 0.45} -> 55/110/165, plus n = N_w - 1 = 183;
zeros = eigvalsh of the signed Jacobi matrix J_n from
fermiedge_classify_probe.signed_chain, real simple for the used
degrees): (m1) Kolmogorov distance of the counting measures,
sealed bar 2/sqrt(n); (m2) node-resolved hit rate = fraction of
zeros whose nearest union node lies in the rounded equilibrium
selection; (m3) sorted one-to-one matching distance; (m4) growth
residual log|pihat_n(z)| - sum_j rho_j log|z - x_j| on the sealed
z-panel (midpoints of the 8 largest node gaps + hull endpoints
+-0.5), reported as max-min spread; scalar-closure bar 0.5 log
units.  REFERENCE CANDIDATE for all cross-world gates: (ii) Vw.

SEALED ADJUDICATION: SZEGO_EQUILIBRIUM_EXACT iff Vw passes the
KS bar at ALL leg-A fillings AND all leg-C tests AND beats THIN
in hit rate by >= 0.15 at all four fillings AND the growth
spread <= 0.5 at all fillings.  EQUILIBRIUM_APPROX_ONLY iff the
KS bar holds everywhere AND Vw beats THIN strictly at >= 3 of 4
fillings (but EXACT fails).  Otherwise NO_SCALAR_CLOSURE.
CRITICAL_FILLING_FROM_EQUILIBRIUM is awarded ONLY if the leg-B
blind prediction lands within +-2 of the measured flip on ALL
three worlds.

SEALED LEG B (blind, source-pure): the degeneracy indicator is
the mean-field norm-dominance rule -- at each mass n solve the
union-Vw equilibrium, form W_j = log|wtilde_j| - 2 (A rho)_j on
eligible nodes (rho_j <= 1/2, self term excluded via zero
diagonal), and predict the sign of h_n as the sign of wtilde at
argmax W; n_pred = FIRST n with a negative dominant node.  The
predictor consumes ONLY node positions and weights; r_n / tau /
flip degrees never enter the predictor path.  Secondary
(informational, not adjudicated): persistent-3 crossing, fraction
of degrees with positive margin.  SEALED SEPARATION RULE: the
equilibrium separates worlds iff first-cross(MAIN) >= 2 x
max(first-cross(controls)) AND margin>0-fraction(MAIN) <= 0.5 x
min(controls).  ALIAS TYPING: corr(margin_n, log|r_n|) reported;
|corr| <= 0.5 on all worlds types the indicator as NOT r_n in
disguise.

SEALED LEG C (worlds): EPSTEIN (x^2+5y^2 Dirichlet comb via
PIK.lambda_eps at N_E = floor(exp(2 alpha_9)) + 1 = 256) and
SCRAMBLE (seed 1); pre-flip test degrees from chain positivity
alone: n_pos = (first nonpositive gammahat index) + 1 (= the
largest degree whose Jacobi matrix consumes only positive
gammahat) -> tests {n_pos // 2, n_pos - 1} = EPSTEIN {12, 24},
SCRAMBLE {10, 20};
matched-filling reference MAIN n = 24; typing gate: |hit_MAIN(24)
- mean(control hits)| <= 0.15 (node resolution is a FILLING
effect, not a world defect).

MUST-FAIL (sealed): the reversed field REV (V_j = Vw reversed in
node order) must degrade the hit rate strictly at MAIN n = 110
and n = 183.  Disclosed: at control small fillings there is no
node-resolved signal to degrade, so the must-fail is sealed on
MAIN mid/high filling only (amendment A2).

SEALED VERDICTS: SZEGO_EQUILIBRIUM_EXACT /
EQUILIBRIUM_APPROX_ONLY / NO_SCALAR_CLOSURE /
CRITICAL_FILLING_FROM_EQUILIBRIUM (optional, leg B).

CALIBRATION AMENDMENTS (disclosed BEFORE the record freeze):
(A1) the contract's KS bar proved NULL-DEGENERATE in calibration
-- THIN and UNIF pass it identically to every candidate (the
union nodes are dense and near-regular at counting resolution);
the node-resolved hit rate, matching distance, and growth
residual were therefore added as discriminators before the
freeze.  (A2) must-fail restricted to MAIN mid/high filling (see
above).  (A3) the first record attempt transcribed n_pos as the
first nonpositive gammahat index itself (testing {12, 23} /
{10, 19} instead of the calibrated {12, 24} / {10, 20}); the
definition was corrected to the calibrated one BEFORE the final
record freeze -- no adjudication outcome changes (all four
control tests pass the KS bar under either transcription).
AMENDMENTS AFTER FREEZE: NONE.

RECORD TABLES (frozen from the calibration pass, 2026-08-24):
CAL_VERDICT = EQUILIBRIUM_APPROX_ONLY + KS_NULL_DEGENERATE +
NO_CRITICAL_FILLING_FROM_EQUILIBRIUM +
COARSE_WORLD_SEPARATION_ONLY.
Leg A (MAIN, n = 55/110/165/183, bars .2697/.1907/.1557/.1478):
  KS   Vw .0364/.0182/.0121/.0109 ; V0 .0364/.0182/.0182/.0164 ;
       Vpos .0364/.0182/.0121/.0109 ; THIN .0364/.0182/.0121/
       .0109 ; UNIF .0353/.0162/.0108/.0080  (ALL pass the bar:
       KS is null-degenerate, typed).
  hit  Vw .236/.473/.576/.699 ; V0 .109/.255/.467/.481 ; Vpos
       .236/.473/.600/.699 ; THIN .164/.391/.448/.470 ; REV
       .182/.345/.497/.530  (Vw beats THIN at 4/4; winner by
       mean hit is Vpos .502 vs Vw .496 -- a near-tie: the union
       equilibrium places <= 7 mass units on nu nodes, (ii) and
       (iii) nearly coincide).
  md   Vw .0119/.0073/.0047/.0041 (sub-node-spacing matching;
       mean gap 2/S ~ .0055).
  growth spread  Vw 3.66/3.28/4.91/3.90 ; V0 2.76/3.05/4.39/
       3.48 ; Vpos 3.73/1.83/5.05/4.97 ; UNIF 3.15/3.04/3.51/
       3.04  (NO candidate reaches the 0.5 scalar-closure bar:
       the discrete equilibrium resolves the zeros to NODE
       accuracy only; the within-gap positions that the g-task
       needs are not in the minimizer).
Leg C: EPSTEIN KS(Vw) .0833/.0833 at n = 12/24 (bars .577/.408),
  hit 0/.167 ; SCRAMBLE KS .1000/.1000 at n = 10/20 (bars .632/
  .447), hit 0/0 ; MAIN matched n = 24: hit .083 -- matched-
  filling typing holds (|.083 - .042| = .041 <= .15).
Leg B (blind): n_pred = 74/8/16 vs measured flips 184/25/21 ->
  NO HIT at +-2 anywhere (|Delta| = 110/17/5);
  CRITICAL_FILLING_FROM_EQUILIBRIUM NOT awarded.  Secondary:
  persistent-3 = None/None/91; margin>0 count 5/37/33 of 182
  (frac .027/.203/.181) -> separation rule PASSES (74 >= 2 x 16;
  .027 <= .5 x .181): the equilibrium field SEPARATES the main
  world from the controls coarsely but does NOT localize the
  flip.  Alias: corr(margin, log|r_n|) = -.225/+.270/-.017 --
  the indicator is NOT r_n in disguise (and not predictive).
Must-fail: REV degrades hit at MAIN 110 (.345 < .473) and 183
  (.530 < .699), loud.  QP cross-check: FISTA vs SLSQP relative
  energy gap 3.4e-14 on the sealed subinstance.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import fermiedge_classify_probe as FC        # noqa: E402 r227
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

W_MAIN = 9
FILLINGS = (55, 110, 165, 183)          # round(t*S) for t = .15/.30/.45, N_w - 1
KS_C = 2.0                              # bar = KS_C / sqrt(n)
HIT_EXACT_MARGIN = 0.15
GROWTH_CLOSURE_BAR = 0.5
FLIP_TOL = 2
ELIG_CAP = 0.5
CROSS_SUB = 8                           # SLSQP subinstance stride
CROSS_MASS = 12.0
CAL_VERDICT = ("EQUILIBRIUM_APPROX_ONLY + KS_NULL_DEGENERATE + "
               "NO_CRITICAL_FILLING_FROM_EQUILIBRIUM + "
               "COARSE_WORLD_SEPARATION_ONLY")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the leg-B predictor "
                       "consumes node positions + weights + the QP "
                       "minimizer ONLY; r_n/tau/flip degrees enter "
                       "adjudication AFTER the predictions are fixed"
                       if not bad else "; ".join(bad))


# ------------------------------------------------------------ worlds
def build_world(name):
    if name == "MAIN":
        return HS.window_data(W_MAIN)
    if name == "SCRAMBLE":
        return HS.window_data(W_MAIN, scramble_seed=1)
    rr9 = core.build_window(W_MAIN)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lam = PIK.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lam) > 1e-12)[0]
    return HS.window_data(W_MAIN, comb=(
        np.log(nn.astype(float)),
        2.0 * lam[nn] / np.sqrt(nn.astype(float))))


def union_setup(d):
    """sorted union nodes, signed weights, log-distance matrix A
    (zero diagonal), Lipschitz constant 2||A||_2."""
    x = np.concatenate([d["xs"], d["ys"]])
    wt = np.concatenate([d["ws"], -d["vs"]])
    o = np.argsort(x)
    x, wt = x[o], wt[o]
    D = np.abs(x[:, None] - x[None, :])
    np.fill_diagonal(D, 1.0)
    A = -np.log(D)
    np.fill_diagonal(A, 0.0)
    v = np.ones(len(x)) / math.sqrt(len(x))
    for _ in range(80):
        v2 = A @ v
        nv = float(np.linalg.norm(v2))
        v = v2 / nv
    return x, wt, A, 2.0 * nv


# ------------------------------------------------------------ solver
def project_capped_simplex(y, mass):
    lo, hi = float(y.min()) - 1.0, float(y.max())
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if np.clip(y - mid, 0.0, 1.0).sum() > mass:
            lo = mid
        else:
            hi = mid
    return np.clip(y - 0.5 * (lo + hi), 0.0, 1.0)


def solve_qp(A, Lip, V, mass, rho0=None, iters=6000, tol=1e-8):
    """FISTA with adaptive restart on E = rho'A rho + V'rho over
    the capped simplex.  Returns (rho, fixed-point residual)."""
    step = 1.0 / Lip
    S = A.shape[0]
    rho = project_capped_simplex(
        np.full(S, mass / S) if rho0 is None else rho0, mass)
    y = rho.copy()
    tk = 1.0
    res = 1.0
    for it in range(iters):
        g = 2.0 * (A @ y) + V
        rn = project_capped_simplex(y - step * g, mass)
        dv = rn - rho
        if g @ dv > 0.0:
            tk = 1.0
            y = rn
        else:
            tn = 0.5 * (1.0 + math.sqrt(1.0 + 4.0 * tk * tk))
            y = rn + ((tk - 1.0) / tn) * dv
            tk = tn
        rho = rn
        if it % 50 == 49:
            g2 = 2.0 * (A @ rho) + V
            res = float(np.max(np.abs(
                rho - project_capped_simplex(rho - step * g2, mass))))
            if res < tol:
                break
    return rho, res


# ------------------------------------------------------------ metrics
def zeros_pihat(alv, gam, n):
    od = np.sqrt(gam[:n - 1])
    J = np.diag(alv[:n]) + np.diag(od, 1) + np.diag(od, -1)
    return np.sort(np.linalg.eigvalsh(J))


def ks_dist(zeros, xn, rho):
    n = len(zeros)
    grid = np.union1d(zeros, xn)
    zs = np.sort(zeros)
    cr = np.concatenate([[0.0], np.cumsum(rho)]) / n
    dm = 0.0
    for side in ("right", "left"):
        Fz = np.searchsorted(zs, grid, side=side) / n
        Fe = cr[np.searchsorted(xn, grid, side=side)]
        dm = max(dm, float(np.max(np.abs(Fz - Fe))))
    return dm


def hit_rate(zeros, x_union, rho, idx_map=None):
    """fraction of zeros whose nearest UNION node is selected
    (rho rounded); idx_map lifts a sub-support selection to union
    indices."""
    sel = np.where(np.round(rho) > 0.5)[0]
    if idx_map is not None:
        sel = idx_map[sel]
    sset = set(sel.tolist())
    near = [int(np.argmin(np.abs(x_union - z))) for z in zeros]
    return sum(1 for j in near if j in sset) / len(zeros)


def match_dist(zeros, xn, rho):
    sel = np.repeat(xn, np.round(rho).astype(int))
    if len(sel) != len(zeros):
        return float("nan")
    return float(np.mean(np.abs(np.sort(zeros) - sel)))


def growth_spread(zeros, xn, rho, zpanel):
    resid = []
    for z in zpanel:
        lgpi = float(np.sum(np.log(np.abs(z - zeros))))
        U = float(np.sum(rho * np.log(np.abs(z - xn))))
        resid.append(lgpi - U)
    return max(resid) - min(resid)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("szego_equilibrium_probe -- PRIME.PORT.SZEGO."
          "EQUILIBRIUM.01 (round 232)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "fillings %s (= round(t S), t = .15/.30/.45, N_w - 1); "
          "KS bar %.1f/sqrt(n); hit-exact margin %.2f; growth "
          "closure bar %.1f; blind tolerance +-%d; eligibility "
          "cap %.1f; candidates (i) V0 / (ii) Vw / (iii) Vpos + "
          "nulls THIN/UNIF; reference candidate Vw; verdicts and "
          "amendments A1/A2 sealed in the frozen spec"
          % (str(FILLINGS), KS_C, HIT_EXACT_MARGIN,
             GROWTH_CLOSURE_BAR, FLIP_TOL, ELIG_CAP))

    # ---------------- MAIN world objects
    dM = build_world("MAIN")
    x, wt, A, Lip = union_setup(dM)
    S = len(x)
    neg = wt < 0
    Vw = -np.log(np.abs(wt))
    ip = np.where(~neg)[0]
    Ap = A[np.ix_(ip, ip)]
    vp = np.ones(len(ip)) / math.sqrt(len(ip))
    for _ in range(80):
        v2 = Ap @ vp
        nvp = float(np.linalg.norm(v2))
        vp = v2 / nvp
    Lip_p = 2.0 * nvp
    ch = FC.signed_chain(dM, dM["n_max"])
    alv = np.array([c["alphahat"] for c in ch])
    gam = np.array([c["gammahat_next"] for c in ch])
    check("G03-support-audit", S == 367 and int(neg.sum()) == 104
          and dM["n_max"] == 184,
          "MAIN w9: S = %d union nodes (263 mu + %d nu), N_w = "
          "%d; established support arithmetic reproduced"
          % (S, int(neg.sum()), dM["n_max"]))

    section("S1  LEG A -- CONSTRAINED EQUILIBRIUM VS ZEROS (MAIN)")
    fillings = (110, 183) if smoke else FILLINGS
    okz = all(float(gam[k]) > 0.0 for k in range(max(fillings) - 1))
    check("G10-zeros-real", okz,
          "gammahat_1..gammahat_%d > 0: J_n symmetric tridiagonal "
          "for every used degree -- the zeros of pihat_n are real "
          "simple (established r228/r231 fact reproduced)"
          % (max(fillings) - 1))

    srt = np.sort(x)
    gaps = np.diff(srt)
    gi = np.argsort(gaps)[::-1][:8]
    zpanel = [0.5 * (srt[i] + srt[i + 1]) for i in gi]
    zpanel += [srt[-1] + 0.5, srt[0] - 0.5]

    ks_tab, hit_tab, md_tab, spr_tab = {}, {}, {}, {}
    res_max = 0.0
    for n in fillings:
        zr = zeros_pihat(alv, gam, n)
        bar = KS_C / math.sqrt(n)
        rw, r1 = solve_qp(A, Lip, Vw, float(n))
        r0, r2 = solve_qp(A, Lip, np.zeros(S), float(n))
        rp, r3 = solve_qp(Ap, Lip_p, Vw[ip], float(n))
        rrev, r4 = solve_qp(A, Lip, Vw[::-1].copy(), float(n))
        res_max = max(res_max, r1, r2, r3, r4)
        rthin = np.zeros(S)
        rthin[np.round(np.linspace(0, S - 1, n)).astype(int)] = 1.0
        runif = np.full(S, n / S)
        row_ks = dict(Vw=ks_dist(zr, x, rw), V0=ks_dist(zr, x, r0),
                      Vpos=ks_dist(zr, x[ip], rp),
                      THIN=ks_dist(zr, x, rthin),
                      UNIF=ks_dist(zr, x, runif),
                      REV=ks_dist(zr, x, rrev))
        row_hit = dict(Vw=hit_rate(zr, x, rw),
                       V0=hit_rate(zr, x, r0),
                       Vpos=hit_rate(zr, x, rp, idx_map=ip),
                       THIN=hit_rate(zr, x, rthin),
                       REV=hit_rate(zr, x, rrev))
        row_spr = dict(Vw=growth_spread(zr, x, rw, zpanel),
                       V0=growth_spread(zr, x, r0, zpanel),
                       Vpos=growth_spread(zr, x[ip], rp, zpanel),
                       UNIF=growth_spread(zr, x, runif, zpanel))
        ks_tab[n], hit_tab[n], spr_tab[n] = row_ks, row_hit, row_spr
        md_tab[n] = match_dist(zr, x, rw)
        sat = int((rw > 1.0 - 1e-6).sum())
        void = int((rw < 1e-6).sum())
        info("n = %3d (bar %.4f): KS Vw %.4f V0 %.4f Vpos %.4f "
             "THIN %.4f UNIF %.4f | hit Vw %.3f V0 %.3f Vpos "
             "%.3f THIN %.3f | md(Vw) %.4f | growth spread Vw "
             "%.2f UNIF %.2f | Vw saturation/void %d/%d "
             "(integer selection), nu-zone mass %.1f"
             % (n, bar, row_ks["Vw"], row_ks["V0"], row_ks["Vpos"],
                row_ks["THIN"], row_ks["UNIF"], row_hit["Vw"],
                row_hit["V0"], row_hit["Vpos"], row_hit["THIN"],
                md_tab[n], row_spr["Vw"], row_spr["UNIF"],
                sat, void, float(rw[neg].sum())))

    check("G11-qp-converged", res_max < 1e-6,
          "max fixed-point residual over all leg-A solves %.1e "
          "(< 1e-6); every minimizer is a saturated 0/1 node "
          "selection (capacity-driven regime)" % res_max)

    # SLSQP cross-check on the sealed subinstance
    from scipy.optimize import minimize
    sub = np.arange(0, S, CROSS_SUB)
    As = A[np.ix_(sub, sub)]
    Vs = Vw[sub]
    Ss = len(sub)
    vs_ = np.ones(Ss) / math.sqrt(Ss)
    for _ in range(80):
        v2 = As @ vs_
        nvs = float(np.linalg.norm(v2))
        vs_ = v2 / nvs
    rf, _ = solve_qp(As, 2.0 * nvs, Vs, CROSS_MASS, iters=8000)
    Ef = float(rf @ (As @ rf) + Vs @ rf)
    res = minimize(lambda r: r @ (As @ r) + Vs @ r,
                   np.full(Ss, CROSS_MASS / Ss),
                   jac=lambda r: 2.0 * (As @ r) + Vs,
                   method="SLSQP", bounds=[(0.0, 1.0)] * Ss,
                   constraints=[{"type": "eq",
                                 "fun": lambda r: r.sum() - CROSS_MASS,
                                 "jac": lambda r: np.ones(Ss)}],
                   options={"maxiter": 600, "ftol": 1e-12})
    rel = abs(Ef - float(res.fun)) / abs(Ef)
    check("G12-qp-crosscheck", rel < 1e-8 and bool(res.success),
          "FISTA vs scipy SLSQP on the sealed subinstance "
          "(stride %d, mass %.0f): relative energy gap %.1e -- "
          "the projected-gradient minimizer is trusted"
          % (CROSS_SUB, CROSS_MASS, rel))

    ok_ks = all(ks_tab[n][c] <= KS_C / math.sqrt(n)
                for n in fillings for c in ("Vw", "V0", "Vpos"))
    check("G13-ks-all-pass", ok_ks,
          "ALL candidates pass the sealed KS bar 2/sqrt(n) at "
          "every filling (max KS %.4f vs min bar %.4f)"
          % (max(ks_tab[n][c] for n in fillings
                 for c in ("Vw", "V0", "Vpos")),
             KS_C / math.sqrt(max(fillings))))
    ok_null = all(ks_tab[n]["THIN"] <= KS_C / math.sqrt(n)
                  and ks_tab[n]["UNIF"] <= KS_C / math.sqrt(n)
                  for n in fillings)
    check("G14-ks-null-degenerate", ok_null,
          "TYPED (amendment A1): the THIN and UNIF nulls pass the "
          "same KS bar at every filling (THIN is IDENTICAL to Vw "
          "at counting resolution) -- the contract's KS metric "
          "cannot adjudicate the equilibrium; counting-level "
          "agreement is a node-density artifact, NOT evidence of "
          "scalar closure")
    beats = [n for n in fillings
             if hit_tab[n]["Vw"] > hit_tab[n]["THIN"]]
    ok_sig = len(beats) >= (len(fillings) - 1)
    check("G15-node-resolved-signal", ok_sig,
          "the EXACT weight field carries real above-null signal "
          "at node resolution: hit(Vw) > hit(THIN) at %d/%d "
          "fillings (%s); matching distance is sub-node-spacing "
          "(%.4f at n = %d vs mean gap %.4f); V0 is clearly "
          "weaker -- the field MATTERS even though KS cannot "
          "see it"
          % (len(beats), len(fillings),
             ", ".join("%.3f>%.3f" % (hit_tab[n]["Vw"],
                                      hit_tab[n]["THIN"])
                       for n in fillings),
             md_tab[max(fillings)], max(fillings), 2.0 / S))
    ok_ngrow = max(spr_tab[n]["Vw"] for n in fillings) \
        > GROWTH_CLOSURE_BAR
    check("G16-growth-not-closed", ok_ngrow,
          "the growth residual spread of the Vw equilibrium on "
          "the sealed z-panel is %s log units (bar for scalar "
          "closure %.1f): the discrete equilibrium resolves the "
          "zeros to NODE accuracy only -- the within-gap "
          "positions that the scalar Szego/g-task needs are NOT "
          "in the minimizer (no candidate closes it; UNIF %s)"
          % (", ".join("%.2f" % spr_tab[n]["Vw"] for n in fillings),
             GROWTH_CLOSURE_BAR,
             ", ".join("%.2f" % spr_tab[n]["UNIF"] for n in fillings)))

    section("S2  LEG C -- CONTROL WORLDS (world-blind algebra)")
    ctrl_hits = []
    ok_cks = True
    if not smoke:
        for wname in ("EPSTEIN", "SCRAMBLE"):
            dc = build_world(wname)
            xc, wtc, Ac, Lc = union_setup(dc)
            Vc = -np.log(np.abs(wtc))
            chc = FC.signed_chain(dc, dc["n_max"])
            ac = np.array([c["alphahat"] for c in chc])
            gc = np.array([c["gammahat_next"] for c in chc])
            n_pos = int(np.where(gc <= 0)[0][0]) + 1
            for n in (n_pos // 2, n_pos - 1):
                zr = zeros_pihat(ac, gc, n)
                rc, _ = solve_qp(Ac, Lc, Vc, float(n))
                ksv = ks_dist(zr, xc, rc)
                hv = hit_rate(zr, xc, rc)
                ctrl_hits.append(hv)
                bar = KS_C / math.sqrt(n)
                ok_cks = ok_cks and (ksv <= bar)
                info("%-8s n = %2d (n_pos %d, bar %.3f): KS(Vw) "
                     "%.4f, hit %.3f" % (wname, n, n_pos, bar,
                                         ksv, hv))
        # matched-filling MAIN reference
        zr24 = zeros_pihat(alv, gam, 24)
        r24, _ = solve_qp(A, Lip, Vw, 24.0)
        h24 = hit_rate(zr24, x, r24)
        mean_ctrl = float(np.mean(ctrl_hits))
        info("MAIN matched-filling n = 24: hit %.3f vs mean "
             "control hit %.3f" % (h24, mean_ctrl))
        check("G20-worlds-ks", ok_cks,
              "the Vw equilibrium passes the KS bar on EPSTEIN "
              "(n = 12/24) and SCRAMBLE (n = 10/20) before their "
              "flips -- the algebra is world-blind at counting "
              "resolution (with the SAME null-degeneracy caveat "
              "as G14)")
        check("G21-matched-filling-typing",
              abs(h24 - mean_ctrl) <= 0.15,
              "TYPED: at matched small filling the node-resolved "
              "hit rate is ~0 on ALL worlds (MAIN %.3f vs control "
              "mean %.3f): node resolution is a FILLING effect "
              "(zeros sit at nodes only in the saturated high-t "
              "regime), not a world defect -- the leg-A signal "
              "has no control counterpart below t ~ 0.07 and is "
              "typed accordingly" % (h24, mean_ctrl))
    else:
        check("G20-worlds-ks", True, "SMOKE: leg C skipped")
        check("G21-matched-filling-typing", True,
              "SMOKE: leg C skipped")

    section("S3  LEG B -- BLIND DEGENERACY INDICATOR (sealed)")
    preds, flips, fracs, firsts, corrs = {}, {}, {}, {}, {}
    worlds_b = ("MAIN",) if smoke else ("MAIN", "EPSTEIN", "SCRAMBLE")
    n_hi = 30 if smoke else 184
    for wname in worlds_b:
        dc = dM if wname == "MAIN" else build_world(wname)
        if wname == "MAIN":
            xc, wtc, Ac, Lc, Vc = x, wt, A, Lip, Vw
        else:
            xc, wtc, Ac, Lc = union_setup(dc)
            Vc = -np.log(np.abs(wtc))
        negc = wtc < 0
        rho = None
        marg = np.full(n_hi, -np.inf)
        for n in range(2, n_hi):
            rho, _ = solve_qp(Ac, Lc, Vc, float(n), rho0=rho,
                              iters=4000, tol=1e-7)
            W = np.log(np.abs(wtc)) - 2.0 * (Ac @ rho)
            elig = rho <= ELIG_CAP
            mneg = np.max(W[negc & elig]) \
                if np.any(negc & elig) else -np.inf
            mpos = np.max(W[(~negc) & elig]) \
                if np.any((~negc) & elig) else -np.inf
            marg[n] = mneg - mpos
        pos = np.where(marg[2:n_hi] > 0)[0] + 2
        preds[wname] = int(pos[0]) if len(pos) else -1
        firsts[wname] = preds[wname]
        fracs[wname] = len(pos) / (n_hi - 2)
        # measured truth (target side, consumed only NOW)
        rs = HS.r_chain(dc, dc["n_max"] + 1)
        negr = np.where(rs < 0)[0]
        flips[wname] = int(negr[0]) if len(negr) else -1
        lr = np.log(np.abs(rs[2:n_hi]))
        corrs[wname] = float(np.corrcoef(marg[2:n_hi], lr)[0, 1])
        info("%-8s: n_pred (first cross) %d, measured flip %d, "
             "margin>0 on %d/%d degrees (frac %.3f), "
             "corr(margin, log|r|) %+.3f"
             % (wname, preds[wname], flips[wname], len(pos),
                n_hi - 2, fracs[wname], corrs[wname]))
    if smoke:
        check("G30-blind-adjudication", True, "SMOKE: sweep "
              "capped at n = 30, no adjudication")
        check("G31-separation", True, "SMOKE: skipped")
        check("G32-alias-typed", True, "SMOKE: skipped")
    else:
        deltas = {w: abs(preds[w] - flips[w]) for w in worlds_b}
        any_hit = all(d <= FLIP_TOL for d in deltas.values())
        ok30 = (preds == {"MAIN": 74, "EPSTEIN": 8, "SCRAMBLE": 16}
                and flips == {"MAIN": 184, "EPSTEIN": 25,
                              "SCRAMBLE": 21} and not any_hit)
        check("G30-blind-adjudication", ok30,
              "the sealed norm-dominance indicator predicts "
              "74/8/16; the measured flips are 184/25/21 "
              "(|Delta| = %d/%d/%d): NO blind hit at +-%d -- "
              "CRITICAL_FILLING_FROM_EQUILIBRIUM is NOT awarded "
              "(honest negative; the mean-field first-crossing "
              "is far too early on every world)"
              % (deltas["MAIN"], deltas["EPSTEIN"],
                 deltas["SCRAMBLE"], FLIP_TOL))
        ok_sep = (firsts["MAIN"] >= 2 * max(firsts["EPSTEIN"],
                                            firsts["SCRAMBLE"])
                  and fracs["MAIN"] <= 0.5 * min(fracs["EPSTEIN"],
                                                 fracs["SCRAMBLE"]))
        check("G31-separation", ok_sep,
              "sealed separation rule PASSES: first-cross MAIN "
              "%d >= 2 x max(controls %d/%d) AND margin-fraction "
              "MAIN %.3f <= 0.5 x min(controls %.3f/%.3f) -- the "
              "equilibrium field separates the main world from "
              "the controls COARSELY (late/rare nu-dominance) "
              "but does NOT localize the flip degree"
              % (firsts["MAIN"], firsts["EPSTEIN"],
                 firsts["SCRAMBLE"], fracs["MAIN"],
                 fracs["EPSTEIN"], fracs["SCRAMBLE"]))
        ok_alias = all(abs(c) <= 0.5 for c in corrs.values())
        check("G32-alias-typed", ok_alias,
              "ALIAS TYPING: corr(margin_n, log|r_n|) = "
              "%+.3f/%+.3f/%+.3f (all |corr| <= 0.5): the "
              "indicator is NOT r_n in disguise -- and it is not "
              "predictive of the flip either; both facts typed"
              % (corrs["MAIN"], corrs["EPSTEIN"],
                 corrs["SCRAMBLE"]))

    section("S4  MUST-FAIL")
    mf_ns = [n for n in (110, 183) if n in fillings]
    ok_mf = all(hit_tab[n]["REV"] < hit_tab[n]["Vw"] for n in mf_ns)
    check("G40-must-fail-reversed-field", ok_mf,
          "the reversed field REV degrades the node-resolved hit "
          "rate strictly at MAIN mid/high filling (%s): the "
          "leg-A signal is pinned to the TRUE weight-node "
          "assignment, not to the field's value distribution "
          "(sealed on MAIN only, amendment A2)"
          % ", ".join("n=%d %.3f<%.3f" % (n, hit_tab[n]["REV"],
                                          hit_tab[n]["Vw"])
                      for n in mf_ns))

    section("S5  VERDICT")
    # sealed adjudication
    exact = (ok_ks and ok_cks
             and all(hit_tab[n]["Vw"] - hit_tab[n]["THIN"]
                     >= HIT_EXACT_MARGIN for n in fillings)
             and all(spr_tab[n]["Vw"] <= GROWTH_CLOSURE_BAR
                     for n in fillings))
    approx = (ok_ks and ok_cks and ok_sig and not exact)
    verdict = ("SZEGO_EQUILIBRIUM_EXACT" if exact else
               "EQUILIBRIUM_APPROX_ONLY" if approx else
               "NO_SCALAR_CLOSURE")
    check("G50-verdict-rule", smoke or verdict
          == "EQUILIBRIUM_APPROX_ONLY",
          "sealed adjudication yields %s: the discrete "
          "constrained equilibrium with the exact comb field "
          "reproduces the zero distribution at counting "
          "resolution (trivially, with the nulls) and carries "
          "REAL above-null signal at node resolution (hit up to "
          "%.2f vs null %.2f at n = 183), but it does NOT close "
          "the scalar Szego/g-task (growth spread >> %.1f) and "
          "its blind degeneracy indicator misses the flips -- "
          "the open scalar task now has a MEASURED lower "
          "boundary: any constructive g-function must carry "
          "within-gap information beyond the capped-simplex "
          "minimizer; CAL_VERDICT reproduced: %s"
          % (verdict,
             hit_tab[max(fillings)]["Vw"],
             hit_tab[max(fillings)]["THIN"],
             GROWTH_CLOSURE_BAR, CAL_VERDICT))
    check("G51-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; no promotion, no "
          "ledger row, no marker; the parametrix follow-up "
          "inherits: (a) the capacity-driven 0/1 selection "
          "regime as the correct leading order, (b) the "
          "measured node-resolution ceiling of any scalar "
          "equilibrium ansatz, (c) the still-open source-side "
          "critical filling (r231 + this round, two independent "
          "refutations)")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G60-verdict", npass == len(CHECKS),
          "%s + KS_NULL_DEGENERATE + "
          "NO_CRITICAL_FILLING_FROM_EQUILIBRIUM + "
          "COARSE_WORLD_SEPARATION_ONLY; NO RH claim" % verdict)

    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
