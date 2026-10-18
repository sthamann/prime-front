#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_loewner_identity_probe -- PRIME.PORT.LOEWNER.01
(EXPLORATION ONLY, experiments/; round 45, probe 1 of the new
review's category shift -- THE HIGHEST-VALUE TEST: after a canonical
diagonal gauge, is M_h = I - D_P EXACTLY the weighted Loewner matrix
of the existing source-built Herglotz carrier?, 2026-08-09.)

THE CLAIM TO TEST (frozen): from [Y, M_h] = f g^T - g f^T
(antisymmetric rank 2, EXACT -- XCII / port_integrable /
port_riemann_hilbert measured it), the off-diagonal is FORCED:
(M_h)_{ij} = (f_i g_j - g_i f_j)/(y_i - y_j) for i != j.  The
review's hypothesis: there is a canonical diagonal gauge w_i and a
SOURCE-BUILT Herglotz function m such that
    (M_h)_{ij} = w_i w_j (m(y_i) - m(y_j))/(y_i - y_j)   (i != j)
    (M_h)_{ii} = w_i^2 m'(y_i),
i.e. M_h IS the weighted Loewner matrix of m; m Herglotz => the
Loewner kernel is a Cauchy-Gram against the positive measure mu of
m => M_h >= 0 manifestly.

PRE-RUN DERIVATIONS (frozen on paper before the first run):
 (D1) SIGN: with C := [Y, M_h] = f g^T - g f^T, algebra gives
      (M_h)_{ij} = (f_i g_j - g_i f_j)/(y_i - y_j) = w_i w_j
      (m_i - m_j)/(y_i - y_j) with w := f and m := -g/f -- the
      SAME minus sign as the documented L(-g) amendment of
      loewner_interlace_probe.  Frozen: m_i := -g_i/f_i.
 (D2) THE SOURCE CARRIER AT THE PORT NODES: the deployed carrier
      of cd_pick is v = b_h m_omega with m_omega(x) = sum_m
      omega_m/(y_m - x) -- its poles are the y-nodes, i.e. they sit
      ON the port node set, so it cannot interpolate a finite
      matrix there.  The unique source-built Herglotz partner that
      is finite at the port nodes is the DUAL carrier
          m_src(y) := sum_k phi_k^2/(x_k - y)  (= -g(y) of
      loewner_interlace T1, the Stieltjes transform of the
      Christoffel measure sum_k phi_k^2 delta_{x_k} -- built from
      the positive-arm source measure only; Herglotz BY
      CONSTRUCTION).  Frozen as THE candidate for L2(ii)/L3; the
      overall scale b_h^2 is a Moebius move and is absorbed by the
      L3 normalization.
 (D3) UNDRESSED BASELINE (known before running): for the FULL
      I - E the off-diagonal is the weighted Loewner of +g =
      -m_src (orientation-REVERSED) and the diagonal carries the
      identity's +1, so the naive diagonal law fails there.  The
      open content is whether the Schur DRESSING repairs (or
      preserves) the law on the port block.  Measured, not
      assumed.

THE CRITICAL HONESTY REQUIREMENT (frozen): a positive source
measure ALWAYS gives a Herglotz m; the Epstein control ALSO has a
positive source measure -- yet its wall is VIOLATED (lam(E) > 1).
So the naive chain (source positive => M_h PSD) MUST break
somewhere for Epstein, and this probe's job is to find WHERE.
Candidate break points, typed explicitly on BOTH controls AND on
truth:
  (a) GAUGE/ORIENTATION: w_i not real/consistent (f_i ~ 0, or the
      L3 Moebius normalization has det < 0 => the identified
      function is ANTI-Herglotz);
  (b) SOURCE-MISMATCH: the identified m is NOT the source carrier
      (a different, non-Herglotz function interpolates);
  (c) DIAGONAL-LAW: (M_h)_{ii} = w_i^2 m'(y_i) fails;
  (d) DOMAIN: the node set leaves the domain where m is
      Herglotz-representable (Christoffel poles x_k intrude into
      the port hull => divided differences of m_src change sign).

FROZEN PROTOCOL (2026-08-09; construction rungs kz {9, 12, 13},
BLIND HOLDOUTS kz {26, 40} as in cd_pick; controls kz 9 Epstein
x^2+5y^2 + scramble seed 1; all on M_h = I - D_P with the
port_schur split and the SPEC v2 generator extraction of
port_riemann_hilbert; port nodes sorted by y ascending):

 L1  GENERATOR-TO-CARRIER MATCH (parametrization ward -- this is
     an IDENTITY given rank 2; the CONTENT comes in L2-L4):
     extract (f, g) from C = [Y, M_h] (SVD left vectors, SPEC v2);
     rank ward sigma_3/sigma_1 <= 1e-10; conditioning gauge rule
     (frozen, value-blind): if min|g|/max|g| > min|f|/max|f|, swap
     (f, g) -> (g, -f) (same C, better-conditioned division);
     m_i := -g_i/f_i (D1), w_i^2 := f_i^2; ward: off-diagonal
     identity rel (Frobenius) <= 1e-8 on all rungs.

 L2  THE DIAGONAL LAW (first content test): (M_h)_{ii} ==
     w_i^2 m'(y_i) with m' computed INDEPENDENTLY:
     (i)  consistency route: 3-point Lagrange derivative of the
          interpolated m_i at the port nodes (discretization
          grade -- REPORT median/max rel, no machine bar);
     (ii) source route: m'(y_i) from the D2 carrier via the L3
          Moebius chain rule: m'(y_i) = m_src'(y_i)
          (c m_i + d)^2 / det(N), m_src'(y) = sum_k
          phi_k^2/(x_k - y)^2 (integral of dmu/(t-y)^2 against
          the source measure directly).
     Typed: DIAGONAL-LAW-EXACT iff route (ii) max rel <= 1e-6 on
     every port node on every truth rung; else
     DIAGONAL-LAW-CONSISTENT iff route (i) median rel <= 0.05 on
     every truth rung; else DIAGONAL-LAW-FAILS.

 L3  SOURCE IDENTIFICATION (the decisive test): is the
     interpolated m equal to m_src at the port nodes after ONE
     global Moebius normalization per rung?  FROZEN NORMALIZATION:
     the three reference nodes are the port nodes at sorted-y
     positions {0, floor(p/2), p-1} (geometry-determined, no fit
     search); N = the unique Moebius with N(m_ref) = m_src(y_ref)
     at the three references (cross-ratio construction);
     orientation sign(det N) printed (break point (a)).  Typed:
     SOURCE-IDENTIFIED iff rel <= 1e-6 on EVERY non-reference port
     node on EVERY rung including holdouts; SOURCE-MISMATCH
     otherwise -- with the honest reading: the Loewner
     parametrization exists (L1, algebra) but its function is NOT
     the source carrier; the review's 'only the gauge is missing'
     is then falsified and the function itself is the open object.

 L4  HERGLOTZ CENSUS: divided-difference census of the NORMALIZED
     m-hat = N(m) over all port-node pairs (fraction with
     (m_i - m_j)/(y_i - y_j) > 0); same census for m_src itself;
     count of Christoffel poles x_k inside the port hull (break
     point (d)).  Typed HERGLOTZ-CONSISTENT iff the m-hat census
     is 1.00 on all truth rungs.

 C   CONTROLS (kz 9, must fire on the VALUE: lam(E) > 1): the L1
     parametrization must PERSIST (algebra); then the break-point
     typing (a)-(d) IS the control -- print exactly which of
     L2/L3/L4 fail on Epstein and scramble vs truth.  This LOCATES
     the arithmetic content in the Pick language.

KILLS: K1 chain short / rank-2 / L1 ward breaks on a truth rung
-> PIPELINE-BROKEN; K2 a control does not fire on the value, or
the L1 algebra does not persist on a control -> CONTROL-DEAD.

VERDICT (frozen enum): LOEWNER-MEASURED (+ typed:
LOEWNER-IDENTIFIED = L2-exact AND source-identified AND
Herglotz-consistent / LOEWNER-PARTIAL(<passing pieces>) /
LOEWNER-DEAD = none of L2/L3/L4 hold on truth) / PIPELINE-BROKEN /
CONTROL-DEAD.

NO RH claim -- even LOEWNER-IDENTIFIED would relocate, not decide,
the wall; the controls' break point is the honest deliverable.

FIREWALL: no zeros, no prime-table oracles (AST scan; own sieves);
v563 READ-ONLY; RNG only inside the declared scramble control;
writes nothing but stdout.  No marker moves.

Sources (read-only): verification/v563_paper2_readouts.py;
cd_pick_scalarization_probe (T1-T4, deployed carrier),
loewner_interlace_probe (dual identity + sign amendment),
port_schur_reduction_probe (D_P = P + X(I-R)^{-1}X^T),
port_integrable_kernel_probe ([Y, D_P] rank 2 exact),
port_riemann_hilbert_setup_probe (SPEC v2 generator extraction).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_loewner_identity_probe.py
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

CONSTRUCTION = (9, 12, 13)
HOLDOUTS = (26, 40)
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


def rung_objects(kz, **kw):
    """Dressed port M_h = I - D_P + the J spectral source data."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    J = np.diag(al[:h]) + np.diag(be[:h - 1], 1) \
        + np.diag(be[:h - 1], -1)
    bh = float(be[h - 1])
    xg, Q = np.linalg.eigh(J)
    phi = Q[h - 1, :].copy()
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
    yp = ys[ip]
    o = np.argsort(yp)
    Mh = np.eye(len(ip)) - DP[np.ix_(o, o)]
    return dict(Mh=Mh, yp=yp[o], h=h, bh=bh, xg=xg, phi=phi,
                lamE=float(np.linalg.eigvalsh(G)[-1]))


def antisym_generators(C):
    """SPEC v2 (port_riemann_hilbert): C = f g^T - g f^T from the
    two LEFT singular vectors of the antisymmetric rank-2 C."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def offdiag_rel(A, B):
    M_ = A - B
    np.fill_diagonal(M_, 0.0)
    A0 = A.copy()
    np.fill_diagonal(A0, 0.0)
    return float(np.linalg.norm(M_) / np.linalg.norm(A0))


def moebius_matrix(z1, z2, z3):
    """2x2 matrix of the Moebius map sending z1, z2, z3 -> 0, 1,
    oo (cross-ratio normal form)."""
    return np.array([[z2 - z3, -z1 * (z2 - z3)],
                     [z2 - z1, -z3 * (z2 - z1)]])


def moebius_apply(A, z):
    return (A[0, 0] * z + A[0, 1]) / (A[1, 0] * z + A[1, 1])


def quad_deriv(y0, y1, y2, m0, m1, m2, t):
    """Derivative at t of the quadratic through three points."""
    return (m0 * (2.0 * t - y1 - y2) / ((y0 - y1) * (y0 - y2))
            + m1 * (2.0 * t - y0 - y2) / ((y1 - y0) * (y1 - y2))
            + m2 * (2.0 * t - y0 - y1) / ((y2 - y0) * (y2 - y1)))


def analyze(r, tag):
    """L1-L4 on one rung; returns the full metric dict."""
    Mh, yp = r["Mh"], r["yp"]
    xg, phi = r["xg"], r["phi"]
    p = len(yp)
    Y = np.diag(yp)
    C = Y @ Mh - Mh @ Y
    f, g, sv = antisym_generators(C)
    rk = float(sv[2] / sv[0]) if len(sv) > 2 and sv[0] > 0 else 0.0
    # frozen value-blind conditioning gauge: better-conditioned
    # division vector as denominator (same C under (f,g)->(g,-f))
    cond_f = float(np.min(np.abs(f)) / np.max(np.abs(f)))
    cond_g = float(np.min(np.abs(g)) / np.max(np.abs(g)))
    swapped = cond_g > cond_f
    if swapped:
        f, g = g, -f
    cond = max(cond_f, cond_g)
    w = f
    m = -g / f                                       # (D1)
    # L1 ward (identity given rank 2)
    dy = yp[:, None] - yp[None, :] + np.eye(p)
    Pred = (w[:, None] * w[None, :]) * (m[:, None] - m[None, :]) \
        / dy
    rel_L1 = offdiag_rel(Mh, Pred)
    # source carrier (D2) + derivative
    msrc = ((phi ** 2)[None, :]
            / (xg[None, :] - yp[:, None])) @ np.ones(len(xg))
    msrc_p = ((phi ** 2)[None, :]
              / (xg[None, :] - yp[:, None]) ** 2) @ np.ones(len(xg))
    # L3 frozen Moebius normalization (refs 0, p//2, p-1)
    refs = (0, p // 2, p - 1)
    Tz = moebius_matrix(m[refs[0]], m[refs[1]], m[refs[2]])
    Tw = moebius_matrix(msrc[refs[0]], msrc[refs[1]],
                        msrc[refs[2]])
    A = np.linalg.solve(Tw, Tz)
    A = A / np.max(np.abs(A))
    detN = float(np.linalg.det(A))
    mhat = moebius_apply(A, m)
    nonref = np.array([i for i in range(p) if i not in refs])
    rel3 = np.abs(mhat[nonref] - msrc[nonref]) \
        / np.maximum(np.abs(msrc[nonref]), 1e-30)
    rel3_max = float(np.max(rel3))
    rel3_med = float(np.median(rel3))
    # L2 (ii) source route via the Moebius chain rule
    denom = (A[1, 0] * m + A[1, 1])
    mp_src_route = msrc_p * denom ** 2 / detN
    pred_diag = w ** 2 * mp_src_route
    rel2 = np.abs(np.diag(Mh) - pred_diag) \
        / np.maximum(np.abs(np.diag(Mh)), 1e-30)
    rel2_max = float(np.max(rel2))
    rel2_med = float(np.median(rel2))
    # L2 (i) consistency route (3-point Lagrange on the m_i;
    # endpoints use the one-sided neighboring triple)
    mp_dd = np.empty(p)
    for i in range(p):
        j = min(max(i, 1), p - 2)
        mp_dd[i] = quad_deriv(yp[j - 1], yp[j], yp[j + 1],
                              m[j - 1], m[j], m[j + 1], yp[i])
    rel2i = np.abs(np.diag(Mh) - w ** 2 * mp_dd) \
        / np.maximum(np.abs(np.diag(Mh)), 1e-30)
    rel2i_med = float(np.median(rel2i))
    # L4 census (on the normalized m-hat, and on m_src itself)
    iu, ju = np.triu_indices(p, 1)
    dd_hat = (mhat[iu] - mhat[ju]) / (yp[iu] - yp[ju])
    frac_hat = float(np.mean(dd_hat > 0.0))
    dd_src = (msrc[iu] - msrc[ju]) / (yp[iu] - yp[ju])
    frac_src = float(np.mean(dd_src > 0.0))
    n_poles_in = int(np.sum((xg > yp[0]) & (xg < yp[-1])))
    tau = 1.0 - r["lamE"]
    # break-point typing (a)-(d), frozen rules
    breaks = []
    if cond < 1e-10 or detN <= 0.0:
        breaks.append("a:GAUGE/ORIENTATION(det %+.1e)" % detN)
    if rel3_max > 1e-6:
        breaks.append("b:SOURCE-MISMATCH")
    if rel2_max > 1e-6:
        breaks.append("c:DIAGONAL-LAW")
    if frac_hat < 1.0:
        breaks.append("d:HERGLOTZ-CENSUS(%d poles in hull)"
                      % n_poles_in)
    print("    %-20s h %4d  p %3d  tau %+.3e  lam(E) %.6f"
          % (tag, r["h"], p, tau, r["lamE"]))
    print("      L1: s3/s1 %.1e | off-diag ward rel %.1e | gauge "
          "min|f|/max|f| %.1e%s"
          % (rk, rel_L1, cond, " (swapped)" if swapped else ""))
    print("      L2: source-route rel max %.3e med %.3e | "
          "dd-route rel med %.3e"
          % (rel2_max, rel2_med, rel2i_med))
    print("      L3: m-hat vs m_src rel max %.3e med %.3e | "
          "det(N) %+.3e" % (rel3_max, rel3_med, detN))
    i_bad = nonref[int(np.argmax(rel3))]
    print("      L3 worst node: y %+.6f  m-hat %+.6e  m_src "
          "%+.6e" % (yp[i_bad], mhat[i_bad], msrc[i_bad]))
    print("      L4: census(m-hat) %.4f | census(m_src) %.4f | "
          "Christoffel poles in port hull %d/%d"
          % (frac_hat, frac_src, n_poles_in, len(xg)))
    print("      BREAK POINTS: %s"
          % (", ".join(breaks) if breaks else "none"))
    return dict(p=p, rk=rk, rel_L1=rel_L1, cond=cond,
                rel2_max=rel2_max, rel2_med=rel2_med,
                rel2i_med=rel2i_med, rel3_max=rel3_max,
                rel3_med=rel3_med, detN=detN, frac_hat=frac_hat,
                frac_src=frac_src, n_poles_in=n_poles_in,
                lamE=r["lamE"], tau=tau, breaks=breaks)


def main():
    section("PRIME.PORT.LOEWNER.01 -- is the port the weighted "
            "Loewner matrix of the source carrier? (EXPLORATION "
            "ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("L1-L4 -- construction rungs %s + blind holdouts %s"
            % (CONSTRUCTION, HOLDOUTS))
    res = {}
    for kz in CONSTRUCTION + HOLDOUTS:
        r = rung_objects(kz)
        res[kz] = None if r is None else analyze(
            r, "kz %d%s" % (kz, " (HOLDOUT)" if kz in HOLDOUTS
                            else ""))
    ok_all = all(r is not None for r in res.values())
    check("L0 all chains complete", ok_all, kill="K1")

    if ok_all:
        check("L1.1 PARAMETRIZATION (identity, validates the "
              "gauge): rank 2 exact (max s3/s1 %.1e <= 1e-10) and "
              "off-diagonal Loewner form with w = f, m = -g/f "
              "(max rel %.1e <= 1e-8) on all rungs -- ALGEBRA "
              "given rank 2; the content is L2-L4"
              % (max(r["rk"] for r in res.values()),
                 max(r["rel_L1"] for r in res.values())),
              max(r["rk"] for r in res.values()) <= 1e-10
              and max(r["rel_L1"] for r in res.values()) <= 1e-8,
              kill="K1")
        diag_exact = max(r["rel2_max"] for r in res.values()) \
            <= 1e-6
        diag_cons = max(r["rel2i_med"] for r in res.values()) \
            <= 0.05
        l2_type = ("DIAGONAL-LAW-EXACT" if diag_exact else
                   "DIAGONAL-LAW-CONSISTENT" if diag_cons else
                   "DIAGONAL-LAW-FAILS")
        check("L2.1 typed: %s (source-route max rel %s; dd-route "
              "med rel %s)"
              % (l2_type,
                 ["%.1e" % r["rel2_max"] for r in res.values()],
                 ["%.1e" % r["rel2i_med"] for r in res.values()]),
              True)
        src_id = max(r["rel3_max"] for r in res.values()) <= 1e-6
        l3_type = ("SOURCE-IDENTIFIED" if src_id
                   else "SOURCE-MISMATCH")
        check("L3.1 typed: %s (max rel per rung %s; det(N) signs "
              "%s)%s"
              % (l3_type,
                 ["%.1e" % r["rel3_max"] for r in res.values()],
                 ["%+d" % (1 if r["detN"] > 0 else -1)
                  for r in res.values()],
                 "" if src_id else " -- the Loewner structure "
                 "exists (L1) but its function is NOT the source "
                 "carrier; the function itself is the open "
                 "object"),
              True)
        herg = all(r["frac_hat"] >= 1.0 for r in res.values())
        l4_type = ("HERGLOTZ-CONSISTENT" if herg
                   else "HERGLOTZ-VIOLATED")
        check("L4.1 typed: %s (census(m-hat) %s; census(m_src) "
              "%s; poles in hull %s)"
              % (l4_type,
                 ["%.3f" % r["frac_hat"] for r in res.values()],
                 ["%.3f" % r["frac_src"] for r in res.values()],
                 [r["n_poles_in"] for r in res.values()]),
              True)
    else:
        l2_type = l3_type = l4_type = "N/A"
        diag_exact = src_id = herg = False

    section("C -- controls (kz 9; the value must fire; the L1 "
            "algebra must persist; the break point IS the "
            "control)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {}
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        r = rung_objects(9, **kw)
        ctl[nmc] = None if r is None else analyze(
            r, "%s (control)" % nmc)
    ctl_ok = all(c is not None for c in ctl.values())
    fired = ctl_ok and all(c["lamE"] > 1.0 for c in ctl.values())
    persists = ctl_ok and all(c["rk"] <= 1e-8
                              and c["rel_L1"] <= 1e-6
                              for c in ctl.values())
    check("C1 CONTROLS FIRE ON THE VALUE (lam(E) > 1: Epstein "
          "%s, scramble %s) and the L1 parametrization PERSISTS "
          "(algebra)"
          % tuple("%.3e" % c["lamE"] if c else "-"
                  for c in (ctl.get("Epstein"),
                            ctl.get("scramble"))),
          fired and persists, kill="K2")
    if ctl_ok and ok_all:
        check("C2 BREAK-POINT TYPING (the control): truth %s | "
              "Epstein %s | scramble %s"
              % (sorted(set(sum((r["breaks"]
                                 for r in res.values()), []))),
                 ctl["Epstein"]["breaks"],
                 ctl["scramble"]["breaks"]),
              True)

    section("V -- FROZEN VERDICT + honest synthesis")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if not (ctl_ok and fired and persists):
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = "PIPELINE-BROKEN" if KILLS[0] == "K1" \
            else "CONTROL-DEAD"
    else:
        pieces = [nm for nm, ok in
                  (("L2-diag", diag_exact), ("L3-source", src_id),
                   ("L4-herglotz", herg)) if ok]
        if len(pieces) == 3:
            sub = "LOEWNER-IDENTIFIED"
        elif pieces:
            sub = "LOEWNER-PARTIAL(%s)" % "+".join(pieces)
        else:
            sub = "LOEWNER-DEAD"
        VERDICT = "LOEWNER-MEASURED (%s)" % sub
    print("\n  VERDICT: %s" % VERDICT)
    if ok_all and ctl_ok:
        print("""
  HONEST SYNTHESIS: L1 is an identity (any rank-2-displacement
  matrix admits the ratio parametrization m = -g/f in the gauge
  w = f); it validates the coordinates, nothing more.  The
  CONTENT lives in L2 (diagonal law: %s), L3 (source
  identification: %s) and L4 (Herglotz census: %s).  The honesty
  requirement is discharged by the break-point typing above: the
  Epstein control also carries a positive source measure, so
  whichever of (a)-(d) fires on Epstein but not on truth is the
  exact seat of the arithmetic content in the Pick language --
  and whatever fires on BOTH is structural (not arithmetic) and
  the review's naive chain fails there for everyone.  NO RH
  claim.""" % (l2_type, l3_type, l4_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
