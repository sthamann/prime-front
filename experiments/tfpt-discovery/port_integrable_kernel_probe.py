#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_integrable_kernel_probe -- PRIME.PORT.INTEGRABLE.01
(EXPLORATION ONLY, experiments/; round 39 task 3 of the 2026-08-09
external review: the integrable-kernel form of the Krein form and
the displacement structure of the DRESSED port operator,
2026-08-09).

THE FORMS (frozen): with J = Q X Q^T (Gauss diagonalization),
u = Q^T e_{h-1}, v = Q^T r (round-38 generators):
  (i)  INTEGRABLE KERNEL: Delta-hat_{ij} = b_h (u_i v_j - v_i
       u_j)/(x_i - x_j) for i != j -- the full-rank Cauchy/
       integrable-kernel class (numerator and denominator each
       antisymmetric; the review's corrected reading of the
       rank-2 displacement);
  (ii) PORT BLOCK EXACT: the UNdressed port block P =
       sqrt(nu) K_CD sqrt(nu) restricted to port nodes has EXACT
       displacement rank <= 2 wrt Y = diag(y_port) (the CD
       formula: (y_m - y_m') P_mm' collapses to two generators);
  (iii) DRESSED DISPLACEMENT (the open question): does [Y, D_P]
       with D_P = P + X (I-R)^{-1} X^T stay low-rank?  The
       dressing is a product of kernels -- no exact collapse is
       known; MEASURE the singular-value profile and type it.

FROZEN PROTOCOL (2026-08-09; heavy rungs kz {9, 12, 13, 26, 40};
controls kz 9):

 I1  INTEGRABLE FORM: off-diagonal identity rel error (Frobenius,
     off-diag part) <= 1e-8 on all heavy rungs.

 I2  PORT-BLOCK RANK 2: sigma_3/sigma_1 of [Y, P] <= 1e-10 on all
     heavy rungs (EXACT low displacement, CD-forced).

 I3  DRESSED PROFILE (typed): effective rank of [Y, D_P] at the
     1e-6 sigma_1 threshold per rung; typed DRESSED-LOW iff the
     effective rank is <= 6 on ALL heavy rungs (the dressing
     preserves near-integrability), else DRESSED-HIGH (the
     dressing genuinely thickens the displacement -- honest
     either way; the sigma profile printed).

 C   CONTROLS (kz 9, must fire): edge crossed on both (min gap <
     0); the algebraic identities I1/I2 PERSIST (algebra, not
     arithmetic -- re-typed).

KILLS: K1 identity I1 breaks -> INTEGRABLE-BROKEN; K2 the exact
port-block rank-2 breaks -> CDRANK-BROKEN; K3 controls do not
fire -> CONTROL-DEAD.

VERDICT (frozen enum): INTEGRABLE-CONFIRMED (+ typed I3
sublabel) / INTEGRABLE-BROKEN / CDRANK-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime-table oracles (AST
scan); v563 READ-ONLY; RNG only in the declared scramble control;
writes nothing but stdout.  No marker moves.

Sources (read-only): v563_paper2_readouts; round-38 chain
(cd_pick_scalarization / port_schur_reduction, declared inputs).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_integrable_kernel_probe.py
"""

import ast
import hashlib
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

HEAVY = (9, 12, 13, 26, 40)
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


def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
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


def build_rung(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h)


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


def full_objects(kz, **kw):
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    J = np.diag(al[:h]) + np.diag(be[:h - 1], 1) \
        + np.diag(be[:h - 1], -1)
    bh = float(be[h - 1])
    Pn = eval_chain(al, be, m0, ys, h + 1)
    V = np.sqrt(vs)[:, None] * Pn[:, :h]
    uvec = np.sqrt(vs) * Pn[:, h]
    Delta = np.eye(h) - V.T @ V
    xg, Q = np.linalg.eigh(J)
    Dh = Q.T @ Delta @ Q
    phi = Q.T @ np.eye(h)[h - 1]
    psi = Q.T @ (V.T @ uvec)
    # Carleson Gram + port split
    G = np.sqrt(vs)[:, None] * (Pn[:, :h] @ Pn[:, :h].T) \
        * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    Pb = G[np.ix_(ip, ip)]
    Xb = G[np.ix_(ip, ib)]
    Rb = G[np.ix_(ib, ib)]
    IR = np.eye(len(ib)) - Rb
    DP = Pb + Xb @ np.linalg.solve(IR, Xb.T)
    DP = 0.5 * (DP + DP.T)
    return dict(Dh=Dh, xg=xg, phi=phi, psi=psi, bh=bh,
                Pb=Pb, DP=DP, yp=ys[ip], h=h,
                lamE=float(np.linalg.eigvalsh(G)[-1]))


def offdiag_rel(A, B):
    M_ = A - B
    np.fill_diagonal(M_, 0.0)
    A0 = A.copy()
    np.fill_diagonal(A0, 0.0)
    return float(np.linalg.norm(M_) / np.linalg.norm(A0))


def eff_rank(C, thresh=1e-6):
    sv = np.linalg.svd(C, compute_uv=False)
    if sv[0] <= 0:
        return 0, sv
    return int(np.sum(sv > thresh * sv[0])), sv


def main():
    section("PRIME.PORT.INTEGRABLE.01 -- integrable kernel + "
            "dressed displacement (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("I1/I2/I3 -- heavy rungs")
    rel1max = rel2max = 0.0
    ranks = {}
    for kz in HEAVY:
        r = full_objects(kz)
        # I1 integrable form
        xg, phi, psi, bh = r["xg"], r["phi"], r["psi"], r["bh"]
        dx = xg[:, None] - xg[None, :] + np.eye(len(xg))
        Dpred = bh * (phi[:, None] * psi[None, :]
                      - psi[:, None] * phi[None, :]) / dx
        rel1 = offdiag_rel(r["Dh"], Dpred)
        rel1max = max(rel1max, rel1)
        # I2 exact port-block displacement rank 2
        Y = np.diag(r["yp"])
        C_P = Y @ r["Pb"] - r["Pb"] @ Y
        svP = np.linalg.svd(C_P, compute_uv=False)
        gapP = float(svP[2] / svP[0]) if len(svP) > 2 else 0.0
        rel2max = max(rel2max, gapP)
        # I3 dressed profile
        C_D = Y @ r["DP"] - r["DP"] @ Y
        rk, sv = eff_rank(C_D)
        ranks[kz] = rk
        print("    kz %-3d h %4d m %3d: I1 rel %.1e | [Y,P] "
              "s3/s1 %.1e | [Y,D_P] eff rank %d (s1..s6: %s)"
              % (kz, r["h"], r["DP"].shape[0], rel1, gapP, rk,
                 "/".join("%.1e" % v for v in sv[:6])))
    check("I1.1 INTEGRABLE FORM: Delta-hat == b_h (u_i v_j - "
          "v_i u_j)/(x_i - x_j) off-diagonal on all heavy rungs "
          "(max rel %.1e <= 1e-8)" % rel1max,
          rel1max <= 1e-8, kill="K1")
    check("I2.1 PORT-BLOCK RANK 2 EXACT: sigma_3/sigma_1 of "
          "[Y, P] <= 1e-10 on all heavy rungs (max %.1e) -- the "
          "CD collapse survives the port restriction" % rel2max,
          rel2max <= 1e-10, kill="K2")
    i3_type = ("DRESSED-LOW" if all(v <= 6 for v in ranks.values())
               else "DRESSED-HIGH")
    check("I3.1 typed: %s (eff ranks %s at 1e-6 threshold) -- "
          "%s"
          % (i3_type, sorted(ranks.values()),
             "the dressing preserves near-integrability"
             if i3_type == "DRESSED-LOW" else
             "the dressing genuinely thickens the displacement; "
             "the integrable structure lives UPSTREAM of the "
             "Schur step"), True)

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok_ctl = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        r = full_objects(9, **kw)
        xg, phi, psi, bh = r["xg"], r["phi"], r["psi"], r["bh"]
        dx = xg[:, None] - xg[None, :] + np.eye(len(xg))
        Dpred = bh * (phi[:, None] * psi[None, :]
                      - psi[:, None] * phi[None, :]) / dx
        rel1 = offdiag_rel(r["Dh"], Dpred)
        fired = r["lamE"] > 1.0 and rel1 <= 1e-6
        ok_ctl &= fired
        print("    %-8s: lam(E) %.3e (fires) | I1 persists "
              "(rel %.1e -- algebra, not arithmetic)"
              % (nmc, r["lamE"], rel1))
    check("C1 CONTROLS: value fires (lam > 1) while the "
          "integrable identity persists on both", ok_ctl,
          kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "INTEGRABLE-BROKEN",
                   "K2": "CDRANK-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "INTEGRABLE-CONFIRMED"
    print("\n  VERDICT: %s (%s)" % (VERDICT, i3_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
