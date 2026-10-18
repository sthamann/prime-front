#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""core_graph_region_probe -- PRIME.PORT.GRAPH.REGION.01
(EXPLORATION ONLY, experiments/; round 56: fix the REGION-OPEN
failure of the normalized-core invariant set by measuring the
STATE DEPENDENCE of the input u_h and building the invariant
region as a GRAPH over the X-family, not a product box.
2026-08-09.)

THE QUESTION (frozen): normalized_core_update_probe (round 55,
PRIME.PORT.NORMALIZED.CORE.01) extracted the EXACT normalized
8x8 update X_{h+1} = c_h (X_h + U_h) (warded at the 1e-15 scale),
counted the input dimension u-dim = 2 (the scalar c = tau/tau' in
[0.051, 19.5] plus ONE matrix mode carrying ~97.5 percent of the
U-energy), and its naive PRODUCT invariant set (top-6 PCA box x
the full measured u-range) failed REGION-OPEN with 45/64 corners
not PD -- the probe's own diagnosis: u is strongly CORRELATED
with X, so the product of the X-box with the u-range contains
pairs (X, u) that the dynamics never visits.  This probe measures
the coupling law u_h ~ F(X_h) honestly (G1), replaces the product
set by the GRAPH TUBE {(X, F(X) + small residual ball)} and
re-runs the region test on the tube (G2), and projects the whole
dynamics to the 2 decisive coordinates (c, alpha) to look for the
reviewer's fixed-point cloud in 2D (G3).  READ-ONLY v563.

THE PIPELINE (frozen, normalized_core_update / deepcore verbatim):
full wall operator A_h = I - E_h on ALL folded neg nodes; block
split along the fixed core CORE_J = {2,...,16}; the exact Schur
core S_h = B_h - Y_h; the 42-rung ladder core.frame_a_zones()
restricted to h <= 900, sorted by (h, kz); X_h = S_h / tau_h,
U_h = (S_{h+1} - S_h)/tau_h, c_h = tau_h/tau_{h+1} on every
consecutive full-core step.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before the first
run; all bars frozen before the run):

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 exactly 42
     reachable rungs, every chain completes, all tau finite;
     W2 >= 30 full-core rungs (skips printed); W3 truth all-PSD
     (A, R, S) on every full-core rung, >= MIN_STEPS = 20
     consecutive full-core steps AND >= MIN_TRANS = 10 chained
     step-transitions (consecutive steps sharing the middle
     rung -- the G3 orbit).  REPRODUCTION WARDS (kill ->
     WARD-BROKEN): W4 deepcore product law max
     |lambda_min(S) w_core / tau - 1| <= 1e-6; W5 deepcore
     inheritance floor min eta_core = 0.0315 (tol 5.001e-5);
     W6 exactness of the update reproduced: DS-identity
     ||DS - (DB - DY)|| rel <= DS_WARD = 1e-12 and normalized
     update ||X' - c(X + U)|| rel <= XUPD_WARD = 1e-10 on every
     step (round-55 N2.a/N2.c; the four-term telescoping N2.b is
     cited as established there, not re-run); W7 the round-55
     input anatomy reproduced: k95 = 1 (ONE matrix mode at 95
     percent U-energy, so u-dim = 2) and top-1 U-mode energy
     share >= M1_SHARE_BAR = 0.90 (measured 0.975 in round 55).

 G1  THE COUPLING LAW u_h ~ F(X_h): frozen mode M1 = unvec36 of
     the TOP right-singular vector of the uncentered leave-none
     SVD of {vec36(U_h)} (sign fixed so mean <U_h, M1>_F >= 0);
     alpha_h = <U_h, M1>_F.  Frozen X-features per step (at the
     base rung): f1 = lam_max(X_h), f2 = tr(X_h), f3 = the
     squared overlap of the top eigenvector of X_h with the top
     |eigenvalue| eigenvector of M1 (the M1-range overlap made
     scalar), f4 = ||X_h||_F.  (a) alpha_h vs each feature: R^2
     per feature (OLS with intercept) and the best 2-feature
     linear law (max R^2 over the 6 pairs, deterministic order);
     (b) c_h vs the same 4 features + alpha_h as a 5th feature:
     R^2 per feature and the best 2-feature law over the 10
     pairs.  HONESTY: the same table DETRENDED in h (targets and
     features replaced by their OLS-in-h residuals) is printed
     too -- a common h-trend is not a coupling law.  TYPED per
     input (on the raw best-2 R^2; alpha: X-only pairs; c: pairs
     may include alpha): COUPLING-LAWFUL(R2 >= 0.90) /
     COUPLING-PARTIAL(0.50 <= R2 < 0.90) / COUPLING-FREE(R2 <
     0.50).  The C3 shuffle null below can DEMOTE a label to
     COUPLING-FREE(shuffle-null) -- frozen demotion rule there.

 G2  THE GRAPH SET (region test v2): the TUBE laws are the best
     X-ONLY 2-feature laws F_alpha(X), F_c(X) from G1 (the tube
     input must be a function of X alone; the alpha-augmented
     c-law is reported in G1 only).  Graph residuals r_h =
     (c_h - F_c(X_h), alpha_h - F_alpha(X_h)) in the 2D input
     space, WHITENED per component by the RMS of the measured
     residuals; the residual ball = the frozen 2-signs x
     top-1-residual-direction sweep: d = top right-singular
     vector of the whitened residual cloud (uncentered), radius
     rho = TUBE_INFLATE = 1.5 x the max whitened residual norm.
     THE SWEEP: X over the 2^6 = 64 corners of the round-55
     top-6 PCA box (global basis + mean, per-coordinate ranges
     inflated INFLATE = 1.5 -- 'as before'); at each corner
     u = (F_c(X), F_alpha(X)) + s rho d (s = +-1, mapped back to
     raw units), U = alpha M1 (rank-1 in the matrix direction,
     k95 = 1 warded; the off-mode ~2.5 percent U-energy is not
     swept -- honesty); evaluate the EXACT one-step margin
     m = c (1 + lam_min(X^{-1/2} U X^{-1/2})) (PD corners only;
     non-PD corners counted) and the PD of the image Phi =
     c (X + U) directly.  ONE-STEP CONTAINMENT: is vec36(Phi)
     back inside the inflated X-box (top-6 coords + residual
     norm <= INFLATE x max family residual)?  Census printed.
     REPORT-ONLY transparency: the same tube sweep on the TIGHT
     box (inflate 1.0) is printed; the typed label uses the
     frozen 1.5 box only.  TYPED: GRAPH-REGION-CANDIDATE(worst
     margin, containment) iff zero non-PD corners AND worst tube
     margin > 0 AND full containment census; else
     GRAPH-REGION-OPEN(worst, where) with 'where' the aggregated
     failure reasons (corner-not-PD(n) / margin<=0@pattern /
     image-not-PD(n) / containment(n_out)).

 G3  THE 2D SHADOW: since u-dim = 2, the orbit (c_i, alpha_i)
     over the chained transitions (consecutive steps sharing the
     middle rung) is printed; the affine return map (c', alpha')
     = A (c, alpha) + b fitted by OLS; per-component R^2, the
     residual RMS, the spectral radius rho(A) of the linear
     part, and the fixed point (I - A)^{-1} b (the reviewer's
     fixed-point coordinate made concrete) with the orbit cloud
     (mean +- std) for comparison.  TYPED:
     SHADOW-LAWLESS(meanR2) iff mean R^2 < SHAD_R2_BAR = 0.50
     (residuals dominate); else SHADOW-CONTRACTING(specrad) iff
     rho(A) < 1.0; else SHADOW-NEUTRAL(specrad).

 C   CONTROLS/WARDS: (C1, kill -> WARD-BROKEN) the SMOOTH-MASS
     world (masses 2 e^{u/2} du, lattice_parametrix B1 verbatim)
     must violate at rung level (some neg(A) > 0) AND its
     X-family must exit (NORM-DEAD tau <= 0 / S not PD / outside
     the frozen truth box) -- NORM-DEAD census reported as
     before.  (C2, must fire, kill -> WARD-BROKEN) the scramble
     frame (seed 1) at kz 9: neg(A) > 0.  (C0, truth anchor,
     kill -> WARD-BROKEN) the truth wall holds on every rung.
     (C3, shuffle null for G1) N_SHUF = 200 rung-shuffles (seed
     20260809) of the PAIRED input (c_h, alpha_h) as a unit
     against the X-features; per shuffle the best X-only
     2-feature R^2 for alpha and for c (same selection over 6
     pairs -- the null carries the same selection bias); report
     median and q95 of both nulls next to the measured X-only
     R^2.  FROZEN DEMOTION: if the measured X-only best-2 R^2 of
     an input is <= its null q95, that input's G1 label is
     demoted to COUPLING-FREE(shuffle-null) -- the 'law' would
     be a trivial scale artifact; both numbers printed.

KILLS: K1 a W1-W3 pipeline ward breaks -> PIPELINE-BROKEN; K2 a
reproduction/exactness/control ward (W4-W7, C0-C2) breaks ->
WARD-BROKEN.

VERDICT (frozen enum): GRAPHREGION-MEASURED with typed sublabels
COUPLING-LAWFUL / COUPLING-PARTIAL / COUPLING-FREE for each of
the two inputs (G1, C3-demotable), GRAPH-REGION-CANDIDATE(worst,
contain) / GRAPH-REGION-OPEN(worst, where) (G2),
SHADOW-CONTRACTING(specrad) / SHADOW-NEUTRAL(specrad) /
SHADOW-LAWLESS(meanR2) (G3); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,4,6,8,10,12,14,16); H_LADDER_MAX = 900;
N_RUNGS_EXP = 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MIN_TRANS
= 10; REPRO_PROD_BAR = 1e-6; REPRO_ETA_MIN = 0.0315; ROUND_TOL =
5.001e-5; DS_WARD = 1e-12; XUPD_WARD = 1e-10; U_ENERGY = 0.95;
K95_EXP = 1; M1_SHARE_BAR = 0.90; COUP_LAW = 0.90; COUP_PART =
0.50; K_PCA = 6; INFLATE = 1.5; TUBE_INFLATE = 1.5; DEGEN_TOL =
1e-12; SHAD_R2_BAR = 0.50; N_SHUF = 200; SHUF_SEED = 20260809;
CTRL_KZ = 9; scramble seed 1; R_SING_TOL_REL = 1e-10.

SPEC AMENDMENTS (documented; fail-first preserved):
  v1 (2026-08-09, frozen pre-run): everything above.  Mechanical
     concretizations frozen with v1: (i) core.build_window
     results are MEMOIZED per (kz, seed) (pure memoization,
     bit-identical physics); (ii) M1 sign fixed so mean
     <U_h, M1>_F >= 0; (iii) the 'M1-range overlap' feature is
     made scalar as the squared inner product of the top
     eigenvector of X with the top |eigenvalue| eigenvector of
     M1; (iv) the tube laws are X-only (see G2); (v) the 2D
     residual space is whitened per component before the
     top-direction SVD and the radius (c and alpha carry
     different units); (vi) the tube matrix part is rank-1
     U = alpha M1 (off-mode energy not swept, printed); (vii)
     the round-55 telescoping ward is cited, not re-run; (viii)
     the tight-box (inflate 1.0) tube sweep is REPORT-ONLY;
     (ix) vec36 = Frobenius-isometric upper-triangle coordinates
     (round-55 SPEC iv verbatim); box geometry in the Frobenius
     metric; (x) best-2-feature selection scans pairs in a fixed
     lexicographic order and keeps the first maximum
     (deterministic); (xi) transparency prints frozen with v1:
     the G2 tube-law restatement prints the R^2 of the deployed
     X-only laws next to the coefficients, and the C3 null
     summary prints the null MAX next to med/q95.
  v2 (2026-08-09, after run 1 -- which was already 23/23 green
     with the full typed verdict; run-1 and run-2 verdicts
     identical): ONE transparency-only diagnostic added, no bar,
     no object, no typed label moved: G2 additionally prints the
     eigenvalue range of M1 and the MATCHED-POINT rank-1 margins
     c_h (1 + lam_min(X_h^{-1/2} (alpha_h M1) X_h^{-1/2}))
     next to the true matched margins with the full U_h -- run 1
     showed image-not-PD on 128/128 tube points, and this print
     separates the two candidate causes (corner geometry vs the
     rank-1 truncation of U): if the rank-1 margin is already
     negative AT the measured family points, the tube fails
     because the decisive positivity lives in the off-mode
     ~2.5 percent of the U-energy, not because of the corners.

NO RH claim: a coupling-law regression, a 128-point tube sweep
of a 6-dim PCA box, and a fitted 2D return map are numerical
measurements on the deployed v563 window ladder; the
invariant-region theorem (compact K, Phi(K) inside K, uniform
margin) remains an open theorem, and no marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control and the declared C3 shuffle null; stdout only.  No marker
moves.

Sources (read-only): v563_paper2_readouts; full wall operator +
fixed-core split + exact normalized update verbatim from
normalized_core_update_probe.py (PRIME.PORT.NORMALIZED.CORE.01,
round 55); core extraction from deepcore_schur_reduction_probe.py
(PRIME.PORT.DEEPCORE.SCHUR.01, round 51); smooth-mass world from
lattice_parametrix_probe.py (B1).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/core_graph_region_probe.py
"""

import ast
import hashlib
import itertools
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_LADDER_MAX = 900
N_RUNGS_EXP = 42
MIN_CORE_RUNGS = 30
MIN_STEPS = 20
MIN_TRANS = 10
REPRO_PROD_BAR = 1e-6          # W4 deepcore product law
REPRO_ETA_MIN = 0.0315         # W5 deepcore eta_core floor
ROUND_TOL = 5.001e-5
DS_WARD = 1e-12                # W6 (round-55 N2.a)
XUPD_WARD = 1e-10              # W6 (round-55 N2.c)
U_ENERGY = 0.95                # W7 k95 energy
K95_EXP = 1                    # W7 round-55 anatomy: udim = 2
M1_SHARE_BAR = 0.90            # W7 top-mode share (measured .975)
COUP_LAW = 0.90                # G1 typed bars
COUP_PART = 0.50
K_PCA = 6                      # G2 box (round-55 verbatim)
INFLATE = 1.5
TUBE_INFLATE = 1.5             # G2 residual-ball inflation
DEGEN_TOL = 1e-12
SHAD_R2_BAR = 0.50             # G3 lawless bar
N_SHUF = 200                   # C3
SHUF_SEED = 20260809
CTRL_KZ = 9
R_SING_TOL_REL = 1e-10
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


# --------------- pipeline, verbatim (normalized_core_update)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    """SPEC concretization (i): pure memoization of the
    deterministic core.build_window (deepcore verbatim)."""
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def ladder_zones():
    """The 42 reachable rungs (christoffel_zone_envelope verbatim)."""
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


def smooth_masses(uu):
    """PNT-mean masses 2 e^{u/2} du (lattice_parametrix B1)."""
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


def gram_anatomy(kz, world_fn=None, scramble_seed=None,
                 want_vec=False):
    """Full wall operator A = I - E on the folded neg grid + the
    fixed-core block split + the exact Schur core S = B - Y
    (normalized_core_update verbatim, minus the telescoping
    inventory -- SPEC (vii))."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    A = np.eye(n) - G
    out = dict(kz=kz, h=h, n=n, alpha=float(alpha))
    if want_vec:
        evA, VA = np.linalg.eigh(A)
    else:
        evA = np.linalg.eigvalsh(A)
        VA = None
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["lamR"] = float(evR[0])
    out["negR"] = int(np.sum(evR < 0.0))
    Z = np.linalg.solve(R, Xc.T)          # exterior response
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y                             # EXACT: S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["B"] = B
    out["Y"] = Y
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["lamSmax"] = float(evS[-1])
    out["negS"] = int(np.sum(evS < 0.0))
    if want_vec:
        v = VA[:, 0]                    # soft mode of the wall
        out["wcore"] = float(np.sum(v[ic] ** 2))
    return out


# ------------------------------------------- vec36 / OLS helpers
_NCORE = len(CORE_J)
_TRIU = [(i, j) for i in range(_NCORE) for j in range(i, _NCORE)]
_SQ2 = math.sqrt(2.0)


def vec36(M):
    """Frobenius-isometric upper-triangle coordinates (SPEC ix)."""
    return np.array([M[i, j] * (1.0 if i == j else _SQ2)
                     for (i, j) in _TRIU])


def unvec36(v):
    M = np.zeros((_NCORE, _NCORE))
    for k, (i, j) in enumerate(_TRIU):
        if i == j:
            M[i, i] = v[k]
        else:
            M[i, j] = M[j, i] = v[k] / _SQ2
    return M


def inv_sqrt(M):
    w, V = np.linalg.eigh(M)
    return V @ np.diag(w ** -0.5) @ V.T


def ols_multi(cols, y):
    """OLS y ~ 1 + cols; returns (beta, R^2, residuals)."""
    y = np.asarray(y, float)
    A = np.column_stack([np.ones(len(y))] + [np.asarray(c, float)
                                             for c in cols])
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ beta
    st = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - float(np.sum(res ** 2)) / st if st > 0 \
        else float("nan")
    return beta, r2, res


def best2(feats, names, y):
    """Best 2-feature law over lexicographic pairs (SPEC x);
    returns (pair-indices, pair-names, beta, R^2)."""
    best = None
    for i, j in itertools.combinations(range(len(feats)), 2):
        beta, r2, _res = ols_multi([feats[i], feats[j]], y)
        if best is None or (np.isfinite(r2) and r2 > best[3]):
            best = ((i, j), "%s+%s" % (names[i], names[j]),
                    beta, r2)
    return best


def detrend_on(y, h):
    _b, _r, res = ols_multi([h], y)
    return res


def features_of(Xmat, m1_top_vec):
    """Frozen G1 features f1..f4 of a symmetric 8x8 X."""
    w, V = np.linalg.eigh(Xmat)
    vtop = V[:, -1]
    ovl = float(np.dot(vtop, m1_top_vec)) ** 2
    return np.array([float(w[-1]), float(np.trace(Xmat)), ovl,
                     float(np.linalg.norm(Xmat))])


FEAT_NAMES = ("lamax", "tr", "ovlM1", "fro")


def coup_label(tag, r2):
    if not np.isfinite(r2) or r2 < COUP_PART:
        return "COUPLING-FREE(%s,R2=%.3f)" % (tag, r2)
    if r2 < COUP_LAW:
        return "COUPLING-PARTIAL(%s,R2=%.3f)" % (tag, r2)
    return "COUPLING-LAWFUL(%s,R2=%.3f)" % (tag, r2)


def main():
    section("PRIME.PORT.GRAPH.REGION.01 -- the invariant region "
            "as a GRAPH over the X-family (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; graph-tube corner sweep = a probe of "
          "invariant-set existence, NOT a proof.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder (42 reachable rungs, h <= %d) "
            "+ reproduction wards" % H_LADDER_MAX)
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    for kz in zones:
        r = gram_anatomy(kz, want_vec=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
        truth.append(r)
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    fin = all(np.isfinite(r["tau"]) for r in truth)
    check("W1c all tau finite", fin, kill="K1")
    full = [r for r in truth if r["core_ok"]]
    n_inc = len(truth) - len(full)
    check("W2 >= %d full-core rungs (CORE-INCOMPLETE skips: %d)"
          % (MIN_CORE_RUNGS, n_inc), len(full) >= MIN_CORE_RUNGS,
          "%d full-core rungs" % len(full), kill="K1")
    ok_psd = all(r["negA"] == 0 and r["negR"] == 0
                 and r["negS"] == 0 for r in full)
    check("W3a WARD truth all-PSD (A, R, S) on every full-core "
          "rung", ok_psd, kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})

    prods = np.array([r["lamS"] * r["wcore"] / r["tau"]
                      for r in full])
    prod_dev = float(np.max(np.abs(prods - 1.0)))
    check("W4 REPRODUCTION deepcore product law: max "
          "|lamS*wcore/tau - 1| = %.3e <= %.0e"
          % (prod_dev, REPRO_PROD_BAR), prod_dev <= REPRO_PROD_BAR,
          kill="K2")
    steps = []
    for r1, r2 in zip(truth, truth[1:]):
        if (r1 is None or r2 is None or not r1.get("core_ok")
                or not r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
        steps.append((r1, r2))
    check("W3b >= %d consecutive full-core steps" % MIN_STEPS,
          len(steps) >= MIN_STEPS, "%d steps" % len(steps),
          kill="K1")
    etas_core = []
    for r1, r2 in steps:
        Wi = inv_sqrt(r1["S"])
        etas_core.append(float(np.linalg.eigvalsh(
            Wi @ r2["S"] @ Wi)[0]))
    eta_min = float(np.min(etas_core))
    check("W5 REPRODUCTION deepcore inheritance floor: min "
          "eta_core %.4f == %.4f (tol %.1e)"
          % (eta_min, REPRO_ETA_MIN, ROUND_TOL),
          abs(eta_min - REPRO_ETA_MIN) <= ROUND_TOL, kill="K2")

    # exact update + W6 exactness wards (round-55 N2.a / N2.c)
    for r in full:
        r["X"] = r["S"] / r["tau"]
    ds_dev, xrec_dev = 0.0, 0.0
    u_list = []
    for r1, r2 in steps:
        tau1, tau2 = r1["tau"], r2["tau"]
        c = tau1 / tau2
        DS = r2["S"] - r1["S"]
        DB = r2["B"] - r1["B"]
        DY = r2["Y"] - r1["Y"]
        dsr = (float(np.linalg.norm(DS - (DB - DY)))
               / max(float(np.linalg.norm(DS)), 1e-300))
        ds_dev = max(ds_dev, dsr)
        U = DS / tau1
        Xn = c * (r1["X"] + U)
        xr = (float(np.linalg.norm(Xn - r2["X"]))
              / max(float(np.linalg.norm(r2["X"])), 1e-300))
        xrec_dev = max(xrec_dev, xr)
        u_list.append((c, U))
    check("W6a WARD DS-identity reproduced: max rel "
          "||DS - (DB - DY)|| %.2e <= %.0e" % (ds_dev, DS_WARD),
          ds_dev <= DS_WARD, kill="K2")
    check("W6b WARD normalized update reproduced: max rel "
          "||X' - c(X + U)|| %.2e <= %.0e" % (xrec_dev, XUPD_WARD),
          xrec_dev <= XUPD_WARD, kill="K2")

    # W7: the round-55 input anatomy (k95 = 1, top-mode share)
    Umat = np.array([vec36(U) for (_c, U) in u_list])
    _uu, sv, vt = np.linalg.svd(Umat, full_matrices=False)
    en = sv ** 2
    cum = np.cumsum(en) / float(np.sum(en))
    k95 = int(np.argmax(cum >= U_ENERGY)) + 1
    share1 = float(en[0] / np.sum(en))
    print("    u-input SVD: top-1 share %.4f, k95 = %d "
          "(u-dim = %d); sigma_1 %.4e sigma_2 %.4e"
          % (share1, k95, 1 + k95, float(sv[0]), float(sv[1])))
    check("W7a WARD round-55 anatomy: k95 == %d" % K95_EXP,
          k95 == K95_EXP, "k95 = %d" % k95, kill="K2")
    check("W7b WARD top-1 U-mode share %.4f >= %.2f"
          % (share1, M1_SHARE_BAR), share1 >= M1_SHARE_BAR,
          kill="K2")
    if KILLS:
        return finish({})

    # frozen mode M1 (SPEC ii) + the 2D input coordinates
    m1v = vt[0].copy()
    M1 = unvec36(m1v)
    alphas = np.array([float(np.sum(vec36(U) * m1v))
                       for (_c, U) in u_list])
    if float(np.mean(alphas)) < 0.0:
        m1v = -m1v
        M1 = -M1
        alphas = -alphas
    cs = np.array([c for (c, _U) in u_list])
    wM1, VM1 = np.linalg.eigh(M1)
    m1_top_vec = VM1[:, int(np.argmax(np.abs(wM1)))]
    offmode = np.array(
        [float(np.linalg.norm(vec36(U) - a * m1v))
         for (_c, U), a in zip(u_list, alphas)])
    print("    M1 frozen: |eig| top %.4f; alpha range "
          "[%+.4f, %+.4f]; c range [%.5f, %.5f]"
          % (float(np.max(np.abs(wM1))), float(np.min(alphas)),
             float(np.max(alphas)), float(np.min(cs)),
             float(np.max(cs))))
    print("    off-mode remainder ||U - alpha M1||_F: med %.4f "
          "max %.4f (vs |alpha| med %.4f) -- not swept (SPEC vi)"
          % (float(np.median(offmode)), float(np.max(offmode)),
             float(np.median(np.abs(alphas)))))

    # ------------------------------------------------------------ G1
    section("G1 -- THE COUPLING LAW  u_h ~ F(X_h): state "
            "dependence of the input")
    hh = np.array([r1["h"] for r1, _r2 in steps], float)
    F = np.array([features_of(r1["X"], m1_top_vec)
                  for r1, _r2 in steps])   # (m, 4)
    feats = [F[:, k] for k in range(4)]
    print("    %d steps; features at the base rung: %s"
          % (len(steps), ", ".join(FEAT_NAMES)))

    def coupling_table(y, yname, with_alpha):
        cols = list(feats) + ([alphas] if with_alpha else [])
        names = list(FEAT_NAMES) + (["alpha"] if with_alpha
                                    else [])
        r2s = [ols_multi([c_], y)[1] for c_ in cols]
        bidx, bname, bbeta, br2 = best2(cols, names, y)
        yd = detrend_on(y, hh)
        colsd = [detrend_on(c_, hh) for c_ in cols]
        r2sd = [ols_multi([c_], yd)[1] for c_ in colsd]
        _bi_d, bname_d, _bb_d, br2_d = best2(colsd, names, yd)
        print("    %s ~ F(X): per-feature R^2 (raw | detrended "
              "in h):" % yname)
        for nm, ra, rd in zip(names, r2s, r2sd):
            print("      %-6s  R^2 %.4f | %.4f" % (nm, ra, rd))
        print("      best 2-feature law: %s  R^2 %.4f "
              "(detrended best: %s  R^2 %.4f)"
              % (bname, br2, bname_d, br2_d))
        return bidx, bname, bbeta, br2, br2_d

    a_idx, a_name, a_beta, a_r2, a_r2d = coupling_table(
        alphas, "alpha", with_alpha=False)
    c_idx, c_name, c_beta, c_r2, c_r2d = coupling_table(
        cs, "c", with_alpha=True)
    # X-only c-law (deployed in the G2 tube + the C3 null)
    cx_idx, cx_name, cx_beta, cx_r2 = best2(feats, FEAT_NAMES, cs)
    print("    c ~ F(X) X-ONLY (tube law, SPEC iv): %s  "
          "R^2 %.4f" % (cx_name, cx_r2))
    g1a = coup_label("alpha", a_r2)
    g1c = coup_label("c", c_r2)
    print("    honesty: detrended-in-h best R^2: alpha %.4f, "
          "c %.4f -- a common h-trend is not a coupling law."
          % (a_r2d, c_r2d))
    check("G1.1 typed: %s" % g1a, True)
    check("G1.2 typed: %s" % g1c, True)

    # ------------------------------------------------------------ G2
    section("G2 -- THE GRAPH SET: tube sweep of the top-%d PCA "
            "box x %.1f (region test v2)" % (K_PCA, INFLATE))
    vecs = np.array([vec36(r["X"]) for r in full])
    mean = np.mean(vecs, axis=0)
    Cmat = vecs - mean[None, :]
    _u2, ss_, vt2 = np.linalg.svd(Cmat, full_matrices=False)
    basis = vt2[:K_PCA]
    coords = Cmat @ basis.T
    resid = np.linalg.norm(Cmat - coords @ basis, axis=1)
    box = []
    for k in range(K_PCA):
        lo = float(np.min(coords[:, k]))
        hi = float(np.max(coords[:, k]))
        box.append((0.5 * (lo + hi), 0.5 * (hi - lo)))
    max_resid = float(np.max(resid))

    def f_alpha(fv):
        return float(a_beta[0] + a_beta[1] * fv[a_idx[0]]
                     + a_beta[2] * fv[a_idx[1]])

    def f_c(fv):
        return float(cx_beta[0] + cx_beta[1] * fv[cx_idx[0]]
                     + cx_beta[2] * fv[cx_idx[1]])

    # graph residuals in (c, alpha), whitened (SPEC v)
    res2 = np.stack([cs - np.array([f_c(fv) for fv in F]),
                     alphas - np.array([f_alpha(fv)
                                        for fv in F])], axis=1)
    rms = np.sqrt(np.mean(res2 ** 2, axis=0))
    rms = np.where(rms > 0, rms, 1.0)
    resw = res2 / rms[None, :]
    _u3, _s3, vt3 = np.linalg.svd(resw, full_matrices=False)
    d_w = vt3[0]
    rho = TUBE_INFLATE * float(np.max(
        np.linalg.norm(resw, axis=1)))
    print("    tube laws (X-only, SPEC iv; R^2 at the point of "
          "use, SPEC xi):")
    print("      alpha = %+.4f %+.4f*%s %+.4f*%s   (R^2 %.4f)"
          % (a_beta[0], a_beta[1], FEAT_NAMES[a_idx[0]],
             a_beta[2], FEAT_NAMES[a_idx[1]], a_r2))
    print("      c     = %+.4f %+.4f*%s %+.4f*%s   (R^2 %.4f)"
          % (cx_beta[0], cx_beta[1], FEAT_NAMES[cx_idx[0]],
             cx_beta[2], FEAT_NAMES[cx_idx[1]], cx_r2))
    print("    graph residuals: rms (c, alpha) = (%.4f, %.4f); "
          "max whitened norm %.4f -> tube radius rho = %.4f "
          "along d_w = (%+.3f, %+.3f)"
          % (float(rms[0]), float(rms[1]), rho / TUBE_INFLATE,
             rho, float(d_w[0]), float(d_w[1])))
    print("    PCA energy of top-%d coords: %.4f; max family "
          "residual %.4f"
          % (K_PCA,
             float(np.sum(ss_[:K_PCA] ** 2)
                   / max(np.sum(ss_ ** 2), 1e-300)), max_resid))

    def tube_sweep(inflate, tag):
        n_notpd = 0
        n_img_npd = 0
        n_contain = 0
        n_pts = 0
        worst = None
        worst_where = None
        for sgn in itertools.product((-1.0, 1.0), repeat=K_PCA):
            cc = np.array([ctr + s * inflate * w
                           for s, (ctr, w) in zip(sgn, box)])
            Xc = unvec36(mean + cc @ basis)
            Xc = 0.5 * (Xc + Xc.T)
            wX = np.linalg.eigvalsh(Xc)
            pd = float(wX[0]) > 0.0
            if not pd:
                n_notpd += 1
            fv = features_of(Xc, m1_top_vec)
            c0, a0 = f_c(fv), f_alpha(fv)
            Wi = inv_sqrt(Xc) if pd else None
            for s_ in (-1.0, 1.0):
                n_pts += 1
                du = s_ * rho * d_w * rms
                c_u = c0 + float(du[0])
                a_u = a0 + float(du[1])
                Phi = c_u * (Xc + a_u * M1)
                Phi = 0.5 * (Phi + Phi.T)
                if float(np.linalg.eigvalsh(Phi)[0]) <= 0.0:
                    n_img_npd += 1
                pv = vec36(Phi)
                pc = (pv - mean) @ basis.T
                inside = (float(np.linalg.norm(
                    pv - mean - pc @ basis))
                    <= INFLATE * max_resid)
                for k in range(K_PCA):
                    ctr, w = box[k]
                    inside &= abs(pc[k] - ctr) <= INFLATE * max(
                        w, DEGEN_TOL)
                if inside:
                    n_contain += 1
                if pd:
                    lam = float(np.linalg.eigvalsh(
                        Wi @ (a_u * M1) @ Wi)[0])
                    m = c_u * (1.0 + lam)
                    if worst is None or m < worst:
                        worst = m
                        worst_where = ("".join(
                            "+" if s > 0 else "-"
                            for s in sgn), "+" if s_ > 0 else "-")
        print("    [%s] %d corners x 2 residual signs = %d tube "
              "points:" % (tag, 2 ** K_PCA, n_pts))
        print("      corners not PD: %d/%d; image Phi not PD: "
              "%d/%d; containment: %d/%d inside the inflated "
              "X-box" % (n_notpd, 2 ** K_PCA, n_img_npd, n_pts,
                         n_contain, n_pts))
        if worst is not None:
            print("      worst tube-corner margin "
                  "c(1+lam_min(H)) = %+.4f at corner %s residual "
                  "sign %s" % (worst, worst_where[0],
                               worst_where[1]))
        else:
            print("      no PD corner -- margin not evaluable")
        return dict(n_notpd=n_notpd, n_img_npd=n_img_npd,
                    n_contain=n_contain, n_pts=n_pts, worst=worst)

    # v2 transparency: locate the failure -- rank-1 vs corners.
    # Matched-point margins with the TRUE U_h (known positive,
    # round 55) vs with the rank-1 tube surrogate alpha_h M1.
    m_true, m_rk1 = [], []
    for (c_, U_), a_, (r1, _r2) in zip(u_list, alphas, steps):
        Wi = inv_sqrt(r1["X"])
        m_true.append(c_ * (1.0 + float(np.linalg.eigvalsh(
            Wi @ U_ @ Wi)[0])))
        m_rk1.append(c_ * (1.0 + float(np.linalg.eigvalsh(
            Wi @ (a_ * M1) @ Wi)[0])))
    print("    v2 diagnostic: eig(M1) range [%+.4f, %+.4f] "
          "(indefinite mode)"
          % (float(np.min(wM1)), float(np.max(wM1))))
    print("    v2 diagnostic: matched-point margins  TRUE U: "
          "min %+.4f med %+.4f | rank-1 alpha*M1: min %+.4f "
          "med %+.4f (%d/%d negative)"
          % (float(np.min(m_true)), float(np.median(m_true)),
             float(np.min(m_rk1)), float(np.median(m_rk1)),
             int(np.sum(np.array(m_rk1) <= 0.0)), len(m_rk1)))
    prim = tube_sweep(INFLATE, "FROZEN inflate 1.5")
    tight = tube_sweep(1.0, "report-only TIGHT inflate 1.0")
    _ = tight
    reasons = []
    if prim["n_notpd"] > 0:
        reasons.append("corner-not-PD(%d)" % prim["n_notpd"])
    if prim["worst"] is not None and prim["worst"] <= 0.0:
        reasons.append("margin<=0")
    if prim["n_img_npd"] > 0:
        reasons.append("image-not-PD(%d)" % prim["n_img_npd"])
    if prim["n_contain"] < prim["n_pts"]:
        reasons.append("containment(%d out)"
                       % (prim["n_pts"] - prim["n_contain"]))
    if not reasons and prim["worst"] is not None:
        g2 = ("GRAPH-REGION-CANDIDATE(worst=%.4f, contain=%d/%d)"
              % (prim["worst"], prim["n_contain"], prim["n_pts"]))
    else:
        g2 = ("GRAPH-REGION-OPEN(worst=%s, where=%s)"
              % ("%.4f" % prim["worst"]
                 if prim["worst"] is not None else "n/a",
                 "+".join(reasons) if reasons else "unknown"))
    print("    honesty: rank-1 tube in the matrix direction "
          "(U = alpha M1); off-mode U-energy ~%.1f%% not swept; "
          "a 64-corner sweep is a probe, NOT a proof."
          % (100.0 * (1.0 - share1)))
    check("G2.1 typed: %s" % g2, True)

    # ------------------------------------------------------------ G3
    section("G3 -- THE 2D SHADOW: orbit + return map in "
            "(c, alpha)")
    trans = []
    for i in range(len(steps) - 1):
        if steps[i][1] is steps[i + 1][0]:
            trans.append((i, i + 1))
    check("W3c >= %d chained step-transitions" % MIN_TRANS,
          len(trans) >= MIN_TRANS, "%d transitions" % len(trans),
          kill="K1")
    if KILLS:
        return finish({})
    print("    orbit (chained transitions; base rung h):")
    print("      h1->h2      c_i      alpha_i   ->  c_i+1    "
          "alpha_i+1")
    for i, j in trans:
        print("      %3d->%3d  %8.4f  %+8.4f  -> %8.4f  %+8.4f"
              % (steps[i][0]["h"], steps[j][0]["h"], cs[i],
                 alphas[i], cs[j], alphas[j]))
    ci = np.array([cs[i] for i, _j in trans])
    ai = np.array([alphas[i] for i, _j in trans])
    cj = np.array([cs[j] for _i, j in trans])
    aj = np.array([alphas[j] for _i, j in trans])
    bc, r2c, resc = ols_multi([ci, ai], cj)
    ba, r2a, resa = ols_multi([ci, ai], aj)
    Amap = np.array([[bc[1], bc[2]], [ba[1], ba[2]]])
    bvec = np.array([bc[0], ba[0]])
    specrad = float(np.max(np.abs(np.linalg.eigvals(Amap))))
    mean_r2 = float(np.mean([r2c, r2a]))
    print("\n    fitted affine return map (c', alpha') = "
          "A (c, alpha) + b:")
    print("      A = [[%+.4f, %+.4f], [%+.4f, %+.4f]]   b = "
          "(%+.4f, %+.4f)"
          % (Amap[0, 0], Amap[0, 1], Amap[1, 0], Amap[1, 1],
             bvec[0], bvec[1]))
    print("      R^2: c' %.4f, alpha' %.4f (mean %.4f); "
          "residual RMS: c' %.4f, alpha' %.4f"
          % (r2c, r2a, mean_r2,
             float(np.sqrt(np.mean(resc ** 2))),
             float(np.sqrt(np.mean(resa ** 2)))))
    print("      spectral radius rho(A) = %.4f" % specrad)
    IA = np.eye(2) - Amap
    if abs(float(np.linalg.det(IA))) > 1e-12:
        fp = np.linalg.solve(IA, bvec)
        print("      fixed point (c*, alpha*) = (%.4f, %+.4f); "
              "orbit cloud c %.4f+-%.4f, alpha %+.4f+-%.4f"
              % (fp[0], fp[1], float(np.mean(cs)),
                 float(np.std(cs)), float(np.mean(alphas)),
                 float(np.std(alphas))))
    else:
        print("      fixed point: I - A singular (neutral)")
    if not np.isfinite(mean_r2) or mean_r2 < SHAD_R2_BAR:
        g3 = "SHADOW-LAWLESS(meanR2=%.3f)" % mean_r2
    elif specrad < 1.0:
        g3 = "SHADOW-CONTRACTING(specrad=%.3f)" % specrad
    else:
        g3 = "SHADOW-NEUTRAL(specrad=%.3f)" % specrad
    check("G3.1 typed: %s" % g3, True)

    # ------------------------------------------------------------ C
    section("C -- controls: smooth world + scramble + the "
            "shuffled-pairs null")
    print("  C1 -- the smooth-mass world (2 e^{u/2} du):")
    sm = []
    for kz in zones:
        r = gram_anatomy(kz, world_fn=world_smooth)
        if r is not None:
            sm.append(r)
    sm.sort(key=lambda r: (r["h"], r["kz"]))
    n_viol = sum(1 for r in sm if r["negA"] > 0)
    n_dead, n_out_s, n_in_s, n_npd = 0, 0, 0, 0
    for r in sm:
        if not r.get("core_ok"):
            continue
        if r["tau"] <= 0.0:
            n_dead += 1        # NORM-DEAD: cannot normalize
            continue
        if r["lamS"] <= 0.0:
            n_npd += 1
            continue
        xs_v = vec36(r["S"] / r["tau"])
        cc = (xs_v - mean) @ basis.T
        rs = float(np.linalg.norm(xs_v - mean - cc @ basis))
        inside = rs <= INFLATE * max_resid
        for k in range(K_PCA):
            ctr, w = box[k]
            inside &= abs(cc[k] - ctr) <= INFLATE * max(w,
                                                        DEGEN_TOL)
        if inside:
            n_in_s += 1
        else:
            n_out_s += 1
    print("    %d rungs built; neg(A) > 0 on %d; X-family: %d "
          "NORM-DEAD (tau <= 0), %d S not PD, %d outside the "
          "truth box, %d inside"
          % (len(sm), n_viol, n_dead, n_npd, n_out_s, n_in_s))
    check("C1.1 WARD smooth violates at rung level (neg(A) > 0 "
          "somewhere)", n_viol > 0, kill="K2")
    check("C1.2 WARD smooth X-family exits (NORM-DEAD / not PD "
          "/ outside)", (n_dead + n_npd + n_out_s) > 0,
          kill="K2")
    check("C0.1 WARD truth wall holds on every rung "
          "(neg(A) = 0)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    print("  C2 -- scramble frame (seed 1) at kz %d:" % CTRL_KZ)
    rsc = gram_anatomy(CTRL_KZ, scramble_seed=1)
    if rsc is None:
        print("    scramble: chain dies -> fires (frame death)")
        fired = True
    else:
        fired = rsc["negA"] > 0
        print("    scramble: tau %+.3e  neg(A) %d -> %s"
              % (rsc["tau"], rsc["negA"],
                 "FIRES" if fired else "SILENT"))
    check("C2.1 WARD scramble fires (neg(A) > 0)", fired,
          kill="K2")

    print("  C3 -- shuffled-pairs null for G1 (%d shuffles, "
          "seed %d; (c, alpha) shuffled as a unit vs the "
          "X-features):" % (N_SHUF, SHUF_SEED))
    rng = np.random.default_rng(SHUF_SEED)
    null_a, null_c = [], []
    for _ in range(N_SHUF):
        perm = rng.permutation(len(steps))
        null_a.append(best2(feats, FEAT_NAMES, alphas[perm])[3])
        null_c.append(best2(feats, FEAT_NAMES, cs[perm])[3])
    qa_med, qa_95 = (float(np.median(null_a)),
                     float(np.quantile(null_a, 0.95)))
    qc_med, qc_95 = (float(np.median(null_c)),
                     float(np.quantile(null_c, 0.95)))
    print("    alpha: measured X-only best-2 R^2 %.4f | null "
          "med %.4f q95 %.4f max %.4f"
          % (a_r2, qa_med, qa_95, float(np.max(null_a))))
    print("    c    : measured X-only best-2 R^2 %.4f | null "
          "med %.4f q95 %.4f max %.4f"
          % (cx_r2, qc_med, qc_95, float(np.max(null_c))))
    demoted = []
    if a_r2 <= qa_95:
        g1a = "COUPLING-FREE(alpha,shuffle-null,R2=%.3f)" % a_r2
        demoted.append("alpha")
    if cx_r2 <= qc_95:
        g1c = "COUPLING-FREE(c,shuffle-null,R2=%.3f)" % c_r2
        demoted.append("c")
    print("    frozen demotion applied to: %s"
          % (", ".join(demoted) if demoted else "none -- the "
             "null collapses, the law is not a scale artifact"))
    check("C3.1 null printed; separation alpha %s, c %s"
          % ("YES" if a_r2 > qa_95 else "NO",
             "YES" if cx_r2 > qc_95 else "NO"), True)

    return finish(dict(g1a=g1a, g1c=g1c, g2=g2, g3=g3))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("GRAPHREGION-MEASURED / %(g1a)s / %(g1c)s / "
                   "%(g2)s / %(g3)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
