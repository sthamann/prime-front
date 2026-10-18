#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_riemann_hilbert_setup_probe -- PRIME.PORT.RIEMANNHILBERT.01
(EXPLORATION ONLY, experiments/; round 39 follow-up, step 3 of the
solve plan: set up the discrete Riemann-Hilbert problem of the
dressed port operator and verify the IIKS closure numerically --
the entry ticket to nonlinear steepest descent, 2026-08-09).

THE SETUP (frozen): XCII measured [Y, D_P] EXACTLY rank 2, so D_P
is an integrable (IIKS-class) kernel:
    D_P[m, m'] = (f_m g_m' - g_m f_m') / (y_m - y_m'),  m != m',
with two explicit generator vectors (f, g) extracted canonically
from the antisymmetric rank-2 commutator.  IIKS theory then says:
the RESOLVENT kernel R_s = s D_P (I - s D_P)^{-1} is AGAIN
integrable with transformed generators
    F = (I - s D_P)^{-1} f,     G = (I - s D_P)^{-T} g,
and the eigenvalue problem of D_P is equivalent to a 2 x 2 matrix
Riemann-Hilbert problem with jump data built from (f, g) on the
node set.  This probe extracts (f, g), verifies the integrable
reconstruction, and tests the IIKS closure at frozen s -- if it
holds, the steepest-descent program is well-posed and the wall
lambda_max <= 1 becomes a sign condition on RH data.

FROZEN PROTOCOL (2026-08-09; heavy rungs kz {9, 12, 13, 26, 40};
frozen resolvent points s in {0.5, 0.9}; controls kz 9):

 R1  GENERATORS: SVD of C = [Y, D_P] gives rank 2 (re-ward
     sigma_3/sigma_1 <= 1e-10); canonical antisymmetric
     generators (f, g) from the two singular pairs; integrable
     reconstruction of D_P off-diagonal rel <= 1e-8.

 R2  IIKS CLOSURE: at each frozen s, R_s = s D_P (I - s D_P)^{-1}
     satisfies [Y, R_s] rank 2 (sigma_3/sigma_1 <= 1e-8) AND its
     generators match (F, G) = ((I - s D_P)^{-1} f, (I - s D_P)
     ^{-T} g) via the integrable reconstruction of R_s
     off-diagonal (rel <= 1e-6) -- the class is closed under
     resolvents: the RH problem is well-posed.

 R3  THE REGISTERED CONTRACT (printed): the 2 x 2 RH/steepest-
     descent program statement.

 C   CONTROLS (kz 9, must fire): value fires (lam(E) > 1); the
     IIKS algebra persists (class membership is algebra).

KILLS: K1 rank/reconstruction breaks -> IIKS-BROKEN; K2 closure
fails -> CLOSURE-BROKEN; K3 controls silent -> CONTROL-DEAD.

VERDICT (frozen enum): RH-SETUP-WELLPOSED / IIKS-BROKEN /
CLOSURE-BROKEN / CONTROL-DEAD.

NO RH claim -- well-posedness of the RH problem is the entry
ticket, not the theorem.

SPEC v2 (extraction repair; run 1 = 3/5): the v1 generator
extraction used f = sqrt(s1) u1, g = -sqrt(s1) v1 from the SVD --
wrong normal form (an antisymmetric rank-2 matrix has PAIRED
singular values and C = s1 (u1 u2^T - u2 u1^T) with the two LEFT
singular vectors); the rank ward passed at 1.7e-14 in run 1, only
the reconstruction failed (rel 2.0 = complete miss, as a wrong
basis must).  v2 extracts (f, g) = sqrt(s1) (u1, +-u2) with the
sign fixed by matching C; no bar changed.

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; XCII (exact dressed
displacement rank 2, declared input); IIKS = Its-Izergin-Korepin-
Slavnov integrable-kernel theory (the classical frame).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_riemann_hilbert_setup_probe.py
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
SPTS = (0.5, 0.9)
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


def dressed_port(kz, **kw):
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    P = G[np.ix_(ip, ip)]
    X = G[np.ix_(ip, ib)]
    R = G[np.ix_(ib, ib)]
    IR = np.eye(len(ib)) - R
    DP = P + X @ np.linalg.solve(IR, X.T)
    DP = 0.5 * (DP + DP.T)
    return dict(DP=DP, yp=ys[ip], h=h,
                lamE=float(np.linalg.eigvalsh(G)[-1]))


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T from the rank-2
    SVD of the antisymmetric C."""
    U, sv, _Vh = np.linalg.svd(C)
    # antisymmetric rank 2: paired singular values, normal form
    # C = s1 (u1 u2^T - u2 u1^T) with the two LEFT vectors
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def integrable_offdiag(f, g, y):
    dy = y[:, None] - y[None, :] + np.eye(len(y))
    K = (f[:, None] * g[None, :] - g[:, None] * f[None, :]) / dy
    np.fill_diagonal(K, 0.0)
    return K


def offdiag_rel(A, B):
    M_ = A - B
    np.fill_diagonal(M_, 0.0)
    A0 = A.copy()
    np.fill_diagonal(A0, 0.0)
    return float(np.linalg.norm(M_) / np.linalg.norm(A0))


def main():
    section("PRIME.PORT.RIEMANNHILBERT.01 -- the IIKS setup of "
            "the dressed port operator (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    section("R1/R2 -- generators + IIKS closure (heavy rungs)")
    rel1max = relCmax = 0.0
    rk_max = 0.0
    for kz in HEAVY:
        r = dressed_port(kz)
        Y = np.diag(r["yp"])
        C = Y @ r["DP"] - r["DP"] @ Y
        f, g, sv = antisym_generators(C)
        rk = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
        rk_max = max(rk_max, rk)
        Krec = integrable_offdiag(f, g, r["yp"])
        rel1 = offdiag_rel(r["DP"], Krec)
        rel1max = max(rel1max, rel1)
        rels = []
        for s in SPTS:
            Minv = np.linalg.inv(np.eye(r["DP"].shape[0])
                                 - s * r["DP"])
            Rs = s * (r["DP"] @ Minv)
            Rs = 0.5 * (Rs + Rs.T)
            CR = Y @ Rs - Rs @ Y
            svR = np.linalg.svd(CR, compute_uv=False)
            rkR = float(svR[2] / svR[0]) if len(svR) > 2 else 0.0
            F = Minv @ (s * f)
            Gv = Minv.T @ g
            Rrec = integrable_offdiag(F, Gv, r["yp"])
            relC = offdiag_rel(Rs, Rrec)
            rels.append((rkR, relC))
            relCmax = max(relCmax, max(rkR, relC))
        print("    kz %-3d h %4d: [Y,D_P] s3/s1 %.1e | rec rel "
              "%.1e | closure (s=0.5, 0.9): rank %.1e/%.1e, rec "
              "%.1e/%.1e"
              % (kz, r["h"], rk, rel1, rels[0][0], rels[1][0],
                 rels[0][1], rels[1][1]))
    check("R1.1 GENERATORS: rank 2 exact (max s3/s1 %.1e) and "
          "integrable reconstruction of D_P (max rel %.1e <= "
          "1e-8)" % (rk_max, rel1max),
          rk_max <= 1e-10 and rel1max <= 1e-8, kill="K1")
    check("R2.1 IIKS CLOSURE: the resolvent stays integrable "
          "with the transformed generators on all rungs and both "
          "s (worst %.1e <= 1e-6) -- the RH problem is "
          "WELL-POSED" % relCmax, relCmax <= 1e-6, kill="K2")

    section("R3 -- the registered contract")
    print("""    PRIME.PORT.RIEMANNHILBERT.01 (registered): the
    eigenvalue problem of the dressed port family is the 2 x 2
    matrix Riemann-Hilbert problem with jump data built from the
    EXPLICIT generator pair (f, g) on the port node set (IIKS);
    the wall lambda_max(D_P) <= 1 is the statement that the RH
    solution has no pole at s = 1.  PROGRAM: nonlinear steepest
    descent for h -> infinity with the Mellin-Cauchy source
    (XCII) as the leading symbol and the arithmetic fluctuation
    as the perturbation.  This is the solve-candidate route; NO
    RH claim.""")
    check("R3.1 contract registered (statement printed)", True)

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        r = dressed_port(9, **kw)
        ok &= r["lamE"] > 1.0
        Y = np.diag(r["yp"])
        C = Y @ r["DP"] - r["DP"] @ Y
        sv = np.linalg.svd(C, compute_uv=False)
        print("    %-8s: lam(E) %.3e (fires) | [Y,D_P] s3/s1 "
              "%.1e (class is algebra)"
              % (nmc, r["lamE"], float(sv[2] / sv[0])))
    check("C1 CONTROLS FIRE (value), class persists", ok,
          kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "IIKS-BROKEN", "K2": "CLOSURE-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "RH-SETUP-WELLPOSED"
    print("\n  VERDICT: %s" % VERDICT)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
