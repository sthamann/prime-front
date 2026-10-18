#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""normalized_core_update_probe -- PRIME.PORT.NORMALIZED.CORE.01
(EXPLORATION ONLY, experiments/; round 55, reviewer priority 2:
extract the EXACT normalized 8x8 update -- the object of the
invariant-region theorem.  2026-08-09.)

THE QUESTION (frozen): deepcore_schur_reduction_probe (round 51,
PRIME.PORT.DEEPCORE.SCHUR.01) reduced the whole wall to the fixed
8x8 Schur family S_h at the core aliases CORE_J = {2,...,16},
with lambda_min(S_h) * w_core / tau_h = 1 to high precision and
core inheritance eta_core >= 0.0315.  The reviewer's frame: the
NORMALIZED core X_h := S_h / tau_h is O(1) (lambda_min(X_h) ~
1/w_core ~ 1), and the sought object is the exact dynamics
    X_{h+1} = Phi(X_h, u_h),
with u_h the finitely many NORMALIZED arithmetic observables the
8 core positions actually see per step.  A compact invariant set
K in Herm_8^+ with Phi(K) inside K and inf_K lambda_min(I + H(X))
> 0 would close the ladder tail.  This probe extracts Phi exactly
on the deployed ladder, measures the boundedness of {X_h}, counts
the effective dimension of u_h, and runs a first corner-sweep
probe of the invariant region.  READ-ONLY v563.

THE PIPELINE (frozen, deepcore_schur_reduction verbatim): full
wall operator A_h = I - E_h on ALL folded neg nodes; block split
along the fixed core CORE_J; S_h = B_h - X_h R_h^{-1} X_h^T; the
42-rung ladder core.frame_a_zones() restricted to h <= 900 via
the closed M_k formula, sorted by (h, kz).

THE EXACT UPDATE (stated up front; elementary): write per rung
Y_h := Xc_h Z_h with Xc_h the 8 x (n-8) coupling block and
Z_h := R_h^{-1} Xc_h^T the exterior resolvent response, so
S_h = B_h - Y_h EXACTLY.  Then
    S_{h+1} - S_h = DB - DY,      DB := B_{h+1} - B_h,
and, splitting the exterior folded-index sets into the common
part C, the dropped part O (rung h only) and the new part N
(rung h+1 only), the SECOND-ORDER-FREE TELESCOPING holds exactly:
    DY = (Xc'_C - Xc_C) Z_C           [coupling increment]
       + Xc'_C (Z'_C - Z_C)           [exterior resolvent update]
       + Xc'_N Z'_N                   [new exterior nodes]
       - Xc_O Z_O                     [dropped exterior nodes].
With U_h := (S_{h+1} - S_h)/tau_h and c_h := tau_h/tau_{h+1} the
normalized update is EXACT:
    X_{h+1} = c_h (X_h + U_h)  =  Phi(X_h, u_h),
so u_h = (c_h, U_h): ONE scalar plus one symmetric 8x8 = at most
1 + 36 numbers per step; the DECISIVE COUNT is the effective rank
of {vec36(U_h)} across the ladder at 95 percent energy (k95), the
reported u-dimension being 1 + k95.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before the first
run; all bars frozen before the run):

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 exactly 42
     reachable rungs, every chain completes, all tau finite;
     W2 >= 30 full-core rungs (CORE-INCOMPLETE skips printed);
     W3 truth all-PSD (A, R, S) on every full-core rung and
     >= MIN_STEPS = 20 consecutive full-core steps.
     REPRODUCTION WARDS (kill -> WARD-BROKEN): W4 the deepcore
     product law max |lambda_min(S) * w_core / tau - 1| <=
     REPRO_PROD_BAR = 1e-6 over the full-core ladder; W5 the
     deepcore inheritance floor min eta_core = 0.0315 at print
     precision (tol 5.001e-5).

 N1  THE NORMALIZED LADDER: X_h = S_h / tau_h per full-core
     rung; the full table printed (lambda_min(X) = lamS/tau,
     its product with w_core, lambda_max(X), ||X||_F); the
     Frobenius DIAMETER of the family {X_h} (max pairwise
     distance), and the consecutive step sizes
     ||X_{h+1} - X_h||_F.  TYPED: FAMILY-BOUNDED(diam) iff the
     log-log slope of lambda_max(X_h) vs h satisfies |slope| <=
     SLOPE_BND = 0.15 (no systematic growth/decay of the top of
     the family); else FAMILY-UNBOUNDED(slope).

 N2  THE EXACT UPDATE DECOMPOSITION (per consecutive full-core
     step): DS := S_{h+1} - S_h; WARDS (kill -> WARD-BROKEN):
       N2.a DS-IDENTITY: ||DS - (DB - DY)||_F / ||DS||_F <=
            DS_WARD = 1e-12 (exact by construction);
       N2.b TELESCOPING: the four-term exterior split above
            reconstructs DY to TELE_WARD = 1e-9 relative;
       N2.c NORMALIZED UPDATE: ||X_{h+1} - c_h (X_h + U_h)||_F
            / ||X_{h+1}||_F <= XUPD_WARD = 1e-10 on every step.
     THE INPUT ANATOMY: per step print c_h and the normalized
     sizes ||DB||/tau, and of the four DY terms /tau, plus
     ||DS||/tau -- WHICH increment functionals enter.  THE
     DECISIVE COUNT: stack {vec36(U_h)} (Frobenius-isometric
     upper-triangle coordinates), SVD (uncentered), k95 =
     smallest k with cumulative energy >= U_ENERGY = 0.95;
     u-dimension = 1 + k95.  TYPED: UPDATE-EXACT(udim = 1+k95).

 N3  THE EMPIRICAL INVARIANT SET (first probe, corner sweep --
     NOT a proof): frozen coordinates = vec36 (the 36-dim real
     parametrization of symmetric 8x8, Frobenius-isometric);
     PCA of the centered family {vec36(X_h)}; top K_PCA = 6
     coordinates; per-coordinate bounding box inflated by
     INFLATE = 1.5 about its center (residual coordinates held
     at the family mean).  (a) LEAVE-ONE-OUT CONTAINMENT: every
     family member inside the inflated box of the others (global
     frozen basis + mean, per-coordinate LOO ranges, residual
     norm <= INFLATE x max residual of the others); census
     printed.  (b) THE MARGIN FUNCTIONAL at the measured points:
     matched-step margins c_h (1 + lambda_min(X_h^{-1/2} U_h
     X_h^{-1/2})) (= (tau/tau') eta_core > 0, known positive)
     AND the cross-min over the full measured u-range, printed.
     (c) THE CORNER SWEEP: at each of the 2^6 = 64 inflated-box
     corners X_c, require X_c PD and evaluate the margin
     m(X_c) = min over the measured u-range of
     c_h (1 + lambda_min(X_c^{-1/2} U_h X_c^{-1/2})); the WORST
     corner margin printed.  TYPED: REGION-CANDIDATE(margin)
     iff every corner is PD AND the worst corner margin > 0 AND
     the LOO containment census has zero failures; else
     REGION-OPEN(reason).  (Honest: a corner sweep on the top-6
     PCA box is a first probe of invariant-set existence, not a
     proof; the residual 30 dimensions are held at the mean.)

 N4  THE ASYMPTOTIC COORDINATE (report): t_h = 1/(2 alpha_h) =
     1/log(atom cutoff X) per rung; component-wise OLS of the
     36 coordinates of X_h vs t; extrapolated X_0 at t = 0
     (intercepts); print median R^2 across components,
     lambda_min(X_0), and ||X_deepest - X_0||_F (the distance
     of the deepest rung to the extrapolant).  Cocycle
     convergence slope -2.80 cited as CONTEXT ONLY (earlier
     round).  TYPED (report): T0-EXTRAP(dist).

 C   CONTROLS/WARDS: (C1, primary, kill -> WARD-BROKEN) the
     SMOOTH-MASS world (masses 2 e^{u/2} du, lattice_parametrix
     B1 verbatim) must violate at rung level (some neg(A) > 0);
     ITS X-FAMILY: rungs with tau <= 0 cannot even be normalized
     (NORM-DEAD); rungs with tau > 0 and full core are checked
     against the frozen truth box (inside/outside) and PD --
     the smooth family must exit (NORM-DEAD or outside or not
     PD somewhere), else the region test is blind ->
     WARD-BROKEN.  (C2, must fire, kill -> WARD-BROKEN) Epstein
     x^2+5y^2 comb and scramble (seed 1) at kz 9: neg(A) > 0 on
     both; either silent -> WARD-BROKEN.  (C0, truth anchor)
     the truth wall holds on every rung (neg(A) = 0).

KILLS: K1 a W1-W3 pipeline ward breaks -> PIPELINE-BROKEN; K2 a
reproduction/exactness/control ward (W4, W5, N2.a-c, C0-C2)
breaks -> WARD-BROKEN.

VERDICT (frozen enum): NORMCORE-MEASURED with typed sublabels
FAMILY-BOUNDED(diam) / FAMILY-UNBOUNDED(slope) (N1),
UPDATE-EXACT(udim) (N2), REGION-CANDIDATE(margin) /
REGION-OPEN(reason) (N3), T0-EXTRAP(dist) (N4); else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,4,6,8,10,12,14,16); H_LADDER_MAX = 900;
N_RUNGS_EXP = 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20;
REPRO_PROD_BAR = 1e-6; REPRO_ETA_MIN = 0.0315; ROUND_TOL =
5.001e-5; SLOPE_BND = 0.15; DS_WARD = 1e-12; TELE_WARD = 1e-9;
XUPD_WARD = 1e-10; U_ENERGY = 0.95; K_PCA = 6; INFLATE = 1.5;
COCYCLE_SLOPE_REF = -2.80 (context only); CTRL_KZ = 9; scramble
seed 1.

SPEC AMENDMENTS (documented; fail-first preserved):
  v1 (2026-08-09, frozen pre-run): everything above.  Mechanical
     concretizations frozen with v1: (i) core.build_window
     results are MEMOIZED per (kz, seed) (deepcore verbatim;
     pure memoization, bit-identical physics); (ii) the LOO
     containment uses the GLOBAL frozen PCA basis and mean with
     per-coordinate leave-one-out ranges (the cheap honest
     version; a per-point basis refit is a different, costlier
     protocol); (iii) degenerate LOO coordinate ranges (zero
     width) require agreement to 1e-12; (iv) vec36 uses
     upper-triangle coordinates with off-diagonals scaled by
     sqrt(2) (Frobenius-isometric), so all box geometry is in
     the Frobenius metric; (v) the deepest rung = max (h, kz) in
     the ladder order; (vi) transparency prints frozen with v1:
     the N2 SVD ladder prints raw sigma_k next to the cumulative
     energy shares, and the N3 corner-sweep summary prints the
     sign pattern of the worst corner.

NO RH claim: the normalized family {X_h}, the exact update
decomposition, and a 64-corner sweep of a 6-dim PCA box are
numerical measurements on the deployed v563 window ladder; the
invariant-region theorem (compact K, Phi(K) inside K, uniform
margin) remains an open theorem, and no marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; full wall operator +
fixed-core split + Schur core verbatim from
deepcore_schur_reduction_probe.py (PRIME.PORT.DEEPCORE.SCHUR.01,
round 51); congruence/inheritance frame from
relative_congruence_probe.py (PRIME.PORT.RELCONG.01, round 51);
smooth-mass world from lattice_parametrix_probe.py (B1); Epstein
control comb verbatim from port_schur_reduction_probe.py.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/normalized_core_update_probe.py
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
REPRO_PROD_BAR = 1e-6          # W4 deepcore product law
REPRO_ETA_MIN = 0.0315         # W5 deepcore eta_core floor
ROUND_TOL = 5.001e-5
SLOPE_BND = 0.15               # N1 lam_max(X) slope band
DS_WARD = 1e-12                # N2.a
TELE_WARD = 1e-9               # N2.b
XUPD_WARD = 1e-10              # N2.c
U_ENERGY = 0.95                # N2 k95 energy
K_PCA = 6                      # N3 top PCA coordinates
INFLATE = 1.5                  # N3 box inflation
DEGEN_TOL = 1e-12              # N3 zero-width LOO coordinate
COCYCLE_SLOPE_REF = -2.80      # context only (earlier round)
CTRL_KZ = 9
R_SING_TOL_REL = 1e-10         # Haynsworth-style relative guard
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


# --------------- pipeline, verbatim (deepcore_schur_reduction)
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


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


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


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None,
                 want_vec=False):
    """Full wall operator A = I - E on the folded neg grid + the
    fixed-core block split (deepcore verbatim), EXTENDED with the
    exact update inventory: B, coupling Xc, exterior response
    Z = R^{-1} Xc^T, Y = Xc Z, and the exterior folded-index
    labels (for the N2 common/old/new telescoping)."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    if comb is not None:
        uu, mm = comb
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
    out["Rsing"] = bool(float(np.min(np.abs(evR)))
                        < R_SING_TOL_REL
                        * float(np.max(np.abs(evR))))
    Z = np.linalg.solve(R, Xc.T)          # exterior response
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y                             # EXACT: S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["B"] = B
    out["Y"] = Y
    out["S"] = S
    out["Xcpl"] = Xc
    out["Z"] = Z
    out["ext_uf"] = uf_n[ib].astype(np.int64)
    out["lamS"] = float(evS[0])
    out["lamSmax"] = float(evS[-1])
    out["negS"] = int(np.sum(evS < 0.0))
    if want_vec:
        v = VA[:, 0]                    # soft mode of the wall
        out["wcore"] = float(np.sum(v[ic] ** 2))
    return out


# ------------------------------------------- vec36 / PCA helpers
_NCORE = len(CORE_J)
_TRIU = [(i, j) for i in range(_NCORE) for j in range(i, _NCORE)]
_SQ2 = math.sqrt(2.0)


def vec36(M):
    """Frobenius-isometric upper-triangle coordinates (SPEC iv)."""
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


def margin_over_u(Xbase, u_list):
    """m(X) = min over measured u of c (1 + lam_min(X^{-1/2} U
    X^{-1/2})); requires X PD (returns None otherwise)."""
    w = np.linalg.eigvalsh(Xbase)
    if float(w[0]) <= 0.0:
        return None
    Wi = inv_sqrt(Xbase)
    vals = []
    for (c, U) in u_list:
        lam = float(np.linalg.eigvalsh(Wi @ U @ Wi)[0])
        vals.append(c * (1.0 + lam))
    return float(np.min(vals))


def ols_line(x, y):
    """OLS y = a + b x; returns (a, b, R^2)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def main():
    section("PRIME.PORT.NORMALIZED.CORE.01 -- the exact "
            "normalized 8x8 update X' = Phi(X, u) "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; corner sweep = first probe of the "
          "invariant region, NOT a proof.")
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

    # reproduction wards (deepcore printed ledger)
    prods = np.array([r["lamS"] * r["wcore"] / r["tau"]
                      for r in full])
    prod_dev = float(np.max(np.abs(prods - 1.0)))
    check("W4 REPRODUCTION deepcore product law: max "
          "|lamS*wcore/tau - 1| = %.3e <= %.0e"
          % (prod_dev, REPRO_PROD_BAR), prod_dev <= REPRO_PROD_BAR,
          kill="K2")
    # consecutive full-core steps (adjacent in the sorted ladder)
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
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ N1
    section("N1 -- THE NORMALIZED LADDER  X_h = S_h / tau_h "
            "(%d full-core rungs)" % len(full))
    for r in full:
        r["X"] = r["S"] / r["tau"]
    print("    kz   h     tau        lamin(X)  lamin*wcore "
          "lamax(X)   ||X||_F    wcore")
    for r in full:
        lmn = r["lamS"] / r["tau"]
        lmx = r["lamSmax"] / r["tau"]
        print("    %-4d %-4d %.3e %9.4f  %9.6f  %9.3f  %9.3f  "
              "%.4f"
              % (r["kz"], r["h"], r["tau"], lmn,
                 lmn * r["wcore"], lmx,
                 float(np.linalg.norm(r["X"])), r["wcore"]),
              flush=True)
    vecs = np.array([vec36(r["X"]) for r in full])
    nfam = len(full)
    diam = 0.0
    for i in range(nfam):
        for j in range(i + 1, nfam):
            diam = max(diam, float(np.linalg.norm(
                vecs[i] - vecs[j])))
    stepd = [float(np.linalg.norm(vec36(r2["X"] - r1["X"])))
             for r1, r2 in steps]
    print("\n    consecutive steps ||X_{h+1} - X_h||_F:")
    for (r1, r2), d in zip(steps, stepd):
        print("      h %3d->%3d  %.4f" % (r1["h"], r2["h"], d))
    hh = np.array([r["h"] for r in full], float)
    lmx_arr = np.array([r["lamSmax"] / r["tau"] for r in full])
    _, slope_mx, _ = ols_line(np.log(hh), np.log(lmx_arr))
    print("\n    family diameter (Frobenius) = %.4f; median "
          "||X||_F = %.3f; step sizes: min %.4f med %.4f max "
          "%.4f" % (diam,
                    float(np.median([np.linalg.norm(v)
                                     for v in vecs])),
                    float(np.min(stepd)),
                    float(np.median(stepd)),
                    float(np.max(stepd))))
    print("    lam_max(X) range [%.3f, %.3f]; log-log slope vs "
          "h %+0.4f (band +-%.2f)"
          % (float(np.min(lmx_arr)), float(np.max(lmx_arr)),
             slope_mx, SLOPE_BND))
    n1 = ("FAMILY-BOUNDED(diam=%.3f)" % diam
          if abs(slope_mx) <= SLOPE_BND
          else "FAMILY-UNBOUNDED(slope=%+.3f)" % slope_mx)
    check("N1.1 typed: %s" % n1, True)

    # ------------------------------------------------------------ N2
    section("N2 -- THE EXACT UPDATE  X' = c (X + U): "
            "decomposition + wards + the u-dimension")
    print("    DS = DB - DY; DY = [dXc]Z + Xc'[dZ] + new - old "
          "(exact telescoping on the exterior split)")
    print("    step        c=tau/tau'  |DB|/tau  |dXcZ|/tau  "
          "|Xc dZ|/tau  |new|/tau  |old|/tau  |DS|/tau   "
          "tele-err   Xrec-err")
    ds_dev = 0.0
    tele_dev = 0.0
    xrec_dev = 0.0
    u_list = []
    for r1, r2 in steps:
        tau1, tau2 = r1["tau"], r2["tau"]
        c = tau1 / tau2
        DS = r2["S"] - r1["S"]
        DB = r2["B"] - r1["B"]
        DY = r2["Y"] - r1["Y"]
        # N2.a exact DS identity
        dsr = (float(np.linalg.norm(DS - (DB - DY)))
               / max(float(np.linalg.norm(DS)), 1e-300))
        ds_dev = max(ds_dev, dsr)
        # exterior split: common / old-only / new-only
        uf1, uf2 = r1["ext_uf"], r2["ext_uf"]
        com, i1, i2 = np.intersect1d(uf1, uf2,
                                     return_indices=True)
        o1 = np.setdiff1d(np.arange(len(uf1)), i1)
        n2i = np.setdiff1d(np.arange(len(uf2)), i2)
        t_dx = (r2["Xcpl"][:, i2] - r1["Xcpl"][:, i1]) \
            @ r1["Z"][i1, :]
        t_dz = r2["Xcpl"][:, i2] @ (r2["Z"][i2, :]
                                    - r1["Z"][i1, :])
        t_new = r2["Xcpl"][:, n2i] @ r2["Z"][n2i, :]
        t_old = r1["Xcpl"][:, o1] @ r1["Z"][o1, :]
        recon = t_dx + t_dz + t_new - t_old
        tr = (float(np.linalg.norm(recon - DY))
              / max(float(np.linalg.norm(DY)), 1e-300))
        tele_dev = max(tele_dev, tr)
        # N2.c normalized update
        U = DS / tau1
        Xn = c * (r1["X"] + U)
        xr = (float(np.linalg.norm(Xn - r2["X"]))
              / max(float(np.linalg.norm(r2["X"])), 1e-300))
        xrec_dev = max(xrec_dev, xr)
        u_list.append((c, U))
        print("    h %3d->%3d  %9.5f  %9.4f  %9.4f   %9.4f   "
              "%9.4f  %9.4f  %9.4f  %.2e  %.2e"
              % (r1["h"], r2["h"], c,
                 float(np.linalg.norm(DB)) / tau1,
                 float(np.linalg.norm(t_dx)) / tau1,
                 float(np.linalg.norm(t_dz)) / tau1,
                 float(np.linalg.norm(t_new)) / tau1,
                 float(np.linalg.norm(t_old)) / tau1,
                 float(np.linalg.norm(DS)) / tau1, tr, xr),
              flush=True)
    check("N2.a DS-IDENTITY WARD: max rel ||DS - (DB - DY)|| "
          "%.2e <= %.0e" % (ds_dev, DS_WARD), ds_dev <= DS_WARD,
          kill="K2")
    check("N2.b TELESCOPING WARD: max rel four-term "
          "reconstruction of DY %.2e <= %.0e"
          % (tele_dev, TELE_WARD), tele_dev <= TELE_WARD,
          kill="K2")
    check("N2.c NORMALIZED-UPDATE WARD: max rel ||X' - "
          "c(X + U)|| %.2e <= %.0e" % (xrec_dev, XUPD_WARD),
          xrec_dev <= XUPD_WARD, kill="K2")
    # the decisive count: effective rank of {vec36(U_h)} at 95%
    Umat = np.array([vec36(U) for (_c, U) in u_list])
    sv = np.linalg.svd(Umat, compute_uv=False)
    en = sv ** 2
    cum = np.cumsum(en) / float(np.sum(en))
    k95 = int(np.argmax(cum >= U_ENERGY)) + 1
    print("\n    u-INPUT SVD (uncentered, %d steps x 36 coords); "
          "energy ladder (with raw sigma, SPEC vi):" % len(u_list))
    for k in range(min(len(sv), 12)):
        print("      k=%2d  sigma %.4e  cumulative energy %.6f%s"
              % (k + 1, float(sv[k]), float(cum[k]),
                 "   <-- k95" if k + 1 == k95 else ""))
        if cum[k] >= 0.999 and k + 1 >= k95:
            break
    cs = np.array([c for (c, _U) in u_list])
    print("    scalar input c = tau/tau': range [%.5f, %.5f], "
          "med %.5f" % (float(np.min(cs)), float(np.max(cs)),
                        float(np.median(cs))))
    udim = 1 + k95
    print("    THE DECISIVE COUNT: k95 = %d matrix modes at "
          "%.0f%% energy  ->  u-dimension = 1 + %d = %d"
          % (k95, 100 * U_ENERGY, k95, udim))
    n2 = "UPDATE-EXACT(udim=%d)" % udim
    check("N2.1 typed: %s" % n2, True)

    # ------------------------------------------------------------ N3
    section("N3 -- THE EMPIRICAL INVARIANT SET: top-%d PCA box "
            "x %.1f + %d-corner sweep (first probe)"
            % (K_PCA, INFLATE, 2 ** K_PCA))
    mean = np.mean(vecs, axis=0)
    Cmat = vecs - mean[None, :]
    _uu, ss_, vt = np.linalg.svd(Cmat, full_matrices=False)
    basis = vt[:K_PCA]                       # frozen global basis
    coords = Cmat @ basis.T                  # (nfam, K_PCA)
    resid = np.linalg.norm(Cmat - coords @ basis, axis=1)
    print("    PCA energy of top-%d coords: %.4f of the family "
          "variance; residual norms: med %.4f max %.4f"
          % (K_PCA,
             float(np.sum(ss_[:K_PCA] ** 2)
                   / max(np.sum(ss_ ** 2), 1e-300)),
             float(np.median(resid)), float(np.max(resid))))
    # (a) leave-one-out containment (SPEC ii: global basis/mean,
    #     per-coordinate LOO ranges)
    n_out = 0
    for i in range(nfam):
        oth = np.delete(np.arange(nfam), i)
        ok_i = True
        for k in range(K_PCA):
            lo = float(np.min(coords[oth, k]))
            hi = float(np.max(coords[oth, k]))
            ctr, w = 0.5 * (lo + hi), 0.5 * (hi - lo)
            if w <= DEGEN_TOL:
                ok_i &= abs(coords[i, k] - ctr) <= DEGEN_TOL
            else:
                ok_i &= abs(coords[i, k] - ctr) <= INFLATE * w
        ok_i &= resid[i] <= INFLATE * float(np.max(resid[oth]))
        if not ok_i:
            n_out += 1
            print("    LOO OUT: kz %d h %d" % (full[i]["kz"],
                                               full[i]["h"]))
    print("    (a) LOO containment: %d/%d family members inside "
          "the inflated box of the others (%d failures)"
          % (nfam - n_out, nfam, n_out))
    # (b) margin functional at the measured points
    matched = [c * (1.0 + float(np.linalg.eigvalsh(
        inv_sqrt(r1["X"]) @ U @ inv_sqrt(r1["X"]))[0]))
        for (c, U), (r1, _r2) in zip(u_list, steps)]
    cross = [margin_over_u(r["X"], u_list) for r in full]
    print("    (b) matched-step margins c(1+lam_min): min %.4f "
          "med %.4f (all > 0: %s; = (tau/tau') eta_core)"
          % (float(np.min(matched)), float(np.median(matched)),
             all(m > 0 for m in matched)))
    print("        cross-min over the full measured u-range at "
          "the measured points: min %.4f med %.4f"
          % (float(np.min(cross)), float(np.median(cross))))
    # (c) the corner sweep
    box = []
    for k in range(K_PCA):
        lo = float(np.min(coords[:, k]))
        hi = float(np.max(coords[:, k]))
        box.append((0.5 * (lo + hi), 0.5 * (hi - lo)))
    worst = None
    worst_sgn = None
    n_notpd = 0
    for sgn in itertools.product((-1.0, 1.0), repeat=K_PCA):
        cc = np.array([ctr + s * INFLATE * w
                       for s, (ctr, w) in zip(sgn, box)])
        Xc = unvec36(mean + cc @ basis)
        Xc = 0.5 * (Xc + Xc.T)
        m = margin_over_u(Xc, u_list)
        if m is None:
            n_notpd += 1
            m = float(np.linalg.eigvalsh(Xc)[0])  # info only
        if worst is None or m < worst:
            worst, worst_sgn = m, sgn
    print("    (c) corner sweep: %d corners, %d not PD; worst "
          "corner margin = %.4f at sign pattern %s (SPEC vi)"
          % (2 ** K_PCA, n_notpd, worst,
             "".join("+" if s > 0 else "-" for s in worst_sgn)))
    if n_notpd > 0:
        reason = "corner-not-PD(%d)" % n_notpd
    elif worst <= 0.0:
        reason = "corner-margin<=0"
    elif n_out > 0:
        reason = "LOO-out(%d)" % n_out
    else:
        reason = ""
    n3 = ("REGION-CANDIDATE(margin=%.4f)" % worst
          if not reason else "REGION-OPEN(%s)" % reason)
    print("    honesty: 6-dim corner sweep with residual "
          "coordinates at the mean -- a first probe of the "
          "invariant set, NOT a proof.")
    check("N3.1 typed: %s" % n3, True)

    # ------------------------------------------------------------ N4
    section("N4 -- THE ASYMPTOTIC COORDINATE  t = 1/(2 alpha) = "
            "1/log X (report)")
    tt = np.array([1.0 / (2.0 * r["alpha"]) for r in full])
    order = np.argsort(-tt)     # shallow (large t) -> deep
    x0 = np.zeros(36)
    r2s = []
    for k in range(36):
        a, b, r2 = ols_line(tt, vecs[:, k])
        x0[k] = a
        if np.isfinite(r2):
            r2s.append(r2)
    X0 = unvec36(x0)
    X0 = 0.5 * (X0 + X0.T)
    deep = full[-1]             # SPEC (v): max (h, kz)
    dist = float(np.linalg.norm(vec36(deep["X"]) - x0))
    print("    t range: %.5f (shallow) .. %.5f (deep); %d rungs"
          % (float(np.max(tt)), float(np.min(tt)), nfam))
    print("    component-wise OLS X(t) = X_0 + b t: median R^2 "
          "= %.4f (q25 %.4f, q75 %.4f) over %d coords"
          % (float(np.median(r2s)),
             float(np.percentile(r2s, 25)),
             float(np.percentile(r2s, 75)), len(r2s)))
    print("    extrapolated X_0 (t = 0): lam_min = %.4f, "
          "lam_max = %.4f, ||X_0||_F = %.4f"
          % (float(np.linalg.eigvalsh(X0)[0]),
             float(np.linalg.eigvalsh(X0)[-1]),
             float(np.linalg.norm(X0))))
    print("    distance of the DEEPEST rung (kz %d, h %d, t "
          "%.5f) to X_0: ||X_deep - X_0||_F = %.4f (family "
          "diameter %.4f)"
          % (deep["kz"], deep["h"],
             1.0 / (2.0 * deep["alpha"]), dist, diam))
    print("    trend of the distance to X_0 along the ladder "
          "(first/mid/last of the t-order): %.4f / %.4f / %.4f"
          % (float(np.linalg.norm(vecs[order[0]] - x0)),
             float(np.linalg.norm(
                 vecs[order[len(order) // 2]] - x0)),
             float(np.linalg.norm(vecs[order[-1]] - x0))))
    print("    context only: earlier cocycle convergence slope "
          "%.2f (cited, not re-derived)." % COCYCLE_SLOPE_REF)
    n4 = "T0-EXTRAP(dist=%.3f)" % dist
    check("N4.1 typed (report): %s" % n4, True)

    # ------------------------------------------------------------ C
    section("C -- controls: smooth world + Epstein/scramble")
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
        inside = rs <= INFLATE * float(np.max(resid))
        for k in range(K_PCA):
            ctr, w = box[k]
            inside &= abs(cc[k] - ctr) <= INFLATE * max(w,
                                                        DEGEN_TOL)
        if inside:
            n_in_s += 1
        else:
            n_out_s += 1
    print("    %d rungs built; neg(A) > 0 on %d (rung-level "
          "violation); X-family: %d NORM-DEAD (tau <= 0), %d "
          "S not PD, %d outside the truth box, %d inside"
          % (len(sm), n_viol, n_dead, n_npd, n_out_s, n_in_s))
    smooth_exits = (n_dead + n_npd + n_out_s) > 0
    check("C1.1 WARD smooth violates at rung level (neg(A) > 0 "
          "somewhere)", n_viol > 0, kill="K2")
    check("C1.2 WARD smooth X-family exits (NORM-DEAD / not PD "
          "/ outside)", smooth_exits, kill="K2")
    check("C0.1 WARD truth wall holds on every rung "
          "(neg(A) = 0)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    print("  C2 -- Epstein + scramble at kz %d:" % CTRL_KZ)
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {"Epstein": gram_anatomy(
               CTRL_KZ, comb=(np.log(nn.astype(float)),
                              2.0 * lamE_[nn]
                              / np.sqrt(nn.astype(float)))),
           "scramble": gram_anatomy(CTRL_KZ, scramble_seed=1)}
    fired_all = True
    for name, r in ctl.items():
        if r is None:
            print("    %-9s: chain dies -> fires (frame death)"
                  % name)
            continue
        f = r["negA"] > 0
        fired_all &= f
        print("    %-9s: tau %+.3e  neg(A) %d -> %s"
              % (name, r["tau"], r["negA"],
                 "FIRES" if f else "SILENT"), flush=True)
    check("C2.1 WARD both controls fire (neg(A) > 0)", fired_all,
          kill="K2")

    return finish(dict(n1=n1, n2=n2, n3=n3, n4=n4))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("NORMCORE-MEASURED / %(n1)s / %(n2)s / "
                   "%(n3)s / %(n4)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
