#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_limit_operator_probe -- PRIME.PORT.LIMIT.01
(EXPLORATION ONLY, experiments/; round 38 continuation, executing
the LXXXVI named objects (a) + (b): construct the port limit
operator and secure the bulk-margin law, 2026-08-09).

CONTEXT (round 38, PORT-SCHUR-EXACT): the wall is exactly
  I - E >= 0  <=>  I - R >= 0 (bulk)  AND  lam_max(D_P) <= 1,
D_P = P + X (I-R)^{-1} X^T the dressed port block (nodes with
tau <= tau_max/10), and (1 - lam_max(D_P))/tau = 1.00 on every
tested rung -- PORT-IS-THE-WALL.  The top eigenvector of D_P is
stable at matched grid indices j (cos >= 0.985).  This probe asks:
do the ENTRIES of D_P converge in the j-coordinate (the limit
operator exists), is the limit CRITICAL (norm exactly 1), is the
bulk margin uniformly safe along the WHOLE ladder, and is the
reduction robust against the predeclared cut?

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run):

 E1  ENTRY CONVERGENCE (the limit operator): on every ladder rung
     (all 42, h <= 900) extract the 6 x 6 submatrix A_h of D_P at
     the matched port indices j in {2, 4, 6, 8, 10, 12} (always
     inside the port).  With A_deep = the deepest rung's matrix:
     delta(h) = ||A_h - A_deep||_F / ||A_deep||_F must TREND DOWN
     (log-log slope of delta vs h <= -0.2 over the rungs h <=
     h_deep/2, so the tail does not contaminate the fit); typed
     ENTRY-CONVERGENT / ENTRY-DRIFTING.  The deepest A_h is printed
     as the first numerical estimate of the PORT LIMIT OPERATOR.

 E2  THE CRITICAL-LIMIT TYPING: lam_max(D_P(h)) = 1 - tau(h) with
     tau -> 0 along the ladder (the v866 law); if E1 converges,
     continuity gives lam_max(D_infty) = 1 EXACTLY -- the limit
     operator is CRITICAL.  Typed statement printed (the named
     theorem target): RH-side positivity on the ladder ==
     "the finite sections of a critical operator approach norm 1
     FROM BELOW"; margin-based certificates cannot exist in the
     limit; the proof shape is exact criticality.  (Check: the
     measured lam_max(D_P) is < 1 on ALL rungs and increasing --
     approach from below.)

 E3  THE BULK-MARGIN LAW (object (b), full ladder): per rung
     1 - lam_max(R) and the safety ratio (1 - lam_max(R))/tau;
     frozen bars: I - R > 0 on ALL rungs AND min ratio >= 100
     (typed BULK-UNIFORMLY-SAFE / BULK-THIN); the log-log slope of
     the bulk margin vs h printed (the LXXXVI -1.485 readout was
     5 rungs; here 42).

 E4  CUT ROBUSTNESS (heavy rungs kz {9, 12, 13, 26, 40}): port
     cuts tau_max x {1/20, 1/10, 1/5}: (1 - lam_max(D_P))/tau in
     [0.99, 1.01] AND I - R > 0 for ALL three cuts on all heavy
     rungs -- the reduction does not depend on the decile choice;
     typed CUT-ROBUST / CUT-SENSITIVE.

 C   CONTROLS (kz 9, must fire): Epstein x^2+5y^2 + scramble seed
     1: lam_max(E) > 1 on both (through the same split machinery).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 I - R loses
positivity on a truth rung (the cut fails structurally) ->
BULK-BROKEN; K3 a control does not fire -> CONTROL-DEAD.
E1/E3/E4 typings may FAIL honestly (kept, exit 1).

VERDICT (frozen enum): PORT-LIMIT-MEASURED (+ typed sublabels) /
PIPELINE-BROKEN / BULK-BROKEN / CONTROL-DEAD.

NO RH claim: criticality of the limit is a TYPING of measured
trends; the limit inequality lam_max(D_infty) <= 1 remains the
open statement.

FIREWALL: no zeros, no prime-table oracles (AST scan); v563
READ-ONLY; RNG only inside the declared scramble control; writes
nothing but stdout.  No marker moves.

Sources (read-only): v563_paper2_readouts; the round-38 chain
(port_schur_reduction / carleson_testing_law probes, declared
inputs); v866 (ladder + defect law).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_limit_operator_probe.py
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
JLIST = (2, 4, 6, 8, 10, 12)
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
    c = c_ar + c_at
    d = grid_density(c)
    L = 2 * M - 2
    return dict(d=d, L=L, D=D, alpha=alpha, h=h)


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


def split_rung(kz, cut=0.10, **kw):
    """Carleson Gram + Schur split at the given tau cut."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h + 1)
    KCD = Pn[:, :h] @ Pn[:, :h].T
    G = np.sqrt(vs)[:, None] * KCD * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) * cut
    ip = np.where(port)[0]
    ib = np.where(~port)[0]
    P = G[np.ix_(ip, ip)]
    X = G[np.ix_(ip, ib)]
    R = G[np.ix_(ib, ib)]
    lamE = float(np.linalg.eigvalsh(G)[-1])
    lamR = float(np.linalg.eigvalsh(R)[-1])
    out = dict(kz=kz, h=h, alpha=b["alpha"], n=n, np_=len(ip),
               lamE=lamE, lamR=lamR, tau=1.0 - lamE,
               jj_port=uf_n[ip])
    if lamR < 1.0:
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        out["lamD"] = float(np.linalg.eigvalsh(DP)[-1])
        out["DP"] = DP
    return out


def submat(r, jlist):
    idx = {int(j): k for k, j in enumerate(r["jj_port"])}
    if any(j not in idx for j in jlist):
        return None
    kk = [idx[j] for j in jlist]
    return r["DP"][np.ix_(kk, kk)]


def main():
    section("PRIME.PORT.LIMIT.01 -- the port limit operator + the "
            "bulk-margin law (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("E1/E3 -- full ladder: entries at j = %s + bulk margins"
            % (JLIST,))
    rows = []
    for kz in core.frame_a_zones():
        r = split_rung(kz)
        if r in (None, "TOO-DEEP"):
            if r is None:
                check("E0 chain short at kz %d" % kz, False,
                      kill="K1")
            continue
        rows.append(r)
    rows.sort(key=lambda r: r["h"])
    ok_bulk_pos = all(r["lamR"] < 1.0 for r in rows)
    check("E3.0 I - R > 0 on ALL %d rungs (max lam(R) = %.6f)"
          % (len(rows), max(r["lamR"] for r in rows)),
          ok_bulk_pos, kill="K2")

    deep = rows[-1]
    A_deep = submat(deep, JLIST)
    deltas = []
    for r in rows[:-1]:
        A = submat(r, JLIST)
        if A is None:
            continue
        deltas.append((r["h"], float(
            np.linalg.norm(A - A_deep) / np.linalg.norm(A_deep))))
    hh_d = np.array([x[0] for x in deltas], float)
    dd = np.array([x[1] for x in deltas])
    fit_mask = hh_d <= deep["h"] / 2.0
    sl_conv = float(np.polyfit(np.log(hh_d[fit_mask]),
                               np.log(dd[fit_mask]), 1)[0])
    conv_type = ("ENTRY-CONVERGENT" if sl_conv <= -0.2
                 else "ENTRY-DRIFTING")
    print("    delta(h) = ||A_h - A_deep||/||A_deep|| over %d "
          "rungs: first %.3f -> last %.3f; log-log slope (h <= "
          "%d) %+.3f" % (len(deltas), dd[0], dd[-1],
                         int(deep["h"] / 2), sl_conv))
    print("    PORT LIMIT OPERATOR estimate (deepest rung h = %d, "
          "j = %s):" % (deep["h"], list(JLIST)))
    for row in A_deep:
        print("      [%s]" % "  ".join("%+.5f" % v for v in row))
    check("E1.1 typed: %s (slope %+.3f, bar <= -0.2)"
          % (conv_type, sl_conv), sl_conv <= -0.2)

    lam_series = np.array([r["lamD"] for r in rows])
    below = bool(np.all(lam_series < 1.0))
    increasing = bool(lam_series[-1] > lam_series[0])
    check("E2.1 CRITICAL-LIMIT TYPING: lam(D_P) < 1 on ALL rungs "
          "(%s), net increasing along the ladder (%.6f -> %.6f, "
          "%s): the finite sections approach norm 1 FROM BELOW; "
          "with E1 convergence, lam(D_infty) = 1 EXACTLY -- the "
          "limit operator is CRITICAL"
          % (below, float(lam_series[0]), float(lam_series[-1]),
             increasing), below and increasing)

    bulk = np.array([1.0 - r["lamR"] for r in rows])
    taus = np.array([r["tau"] for r in rows])
    hh = np.array([r["h"] for r in rows], float)
    ratio = bulk / taus
    sl_bulk = float(np.polyfit(np.log(hh), np.log(bulk), 1)[0])
    bulk_type = ("BULK-UNIFORMLY-SAFE" if float(np.min(ratio))
                 >= 100.0 else "BULK-THIN")
    check("E3.1 typed: bulk margin 1 - lam(R) in [%.3e, %.3e], "
          "log-log slope vs h %+.3f; safety ratio margin/tau in "
          "[%.1e, %.1e] -> %s (bar min >= 100)"
          % (float(np.min(bulk)), float(np.max(bulk)), sl_bulk,
             float(np.min(ratio)), float(np.max(ratio)),
             bulk_type), float(np.min(ratio)) >= 100.0)

    section("E4 -- cut robustness (heavy rungs, cuts 1/20, 1/10, "
            "1/5)")
    cut_ok = True
    for kz in HEAVY:
        vals = []
        for cut in (0.05, 0.10, 0.20):
            r = split_rung(kz, cut=cut)
            if r is None or "lamD" not in r:
                cut_ok = False
                vals.append("BROKEN")
                continue
            q = (1.0 - r["lamD"]) / r["tau"]
            vals.append("%.4f" % q)
            cut_ok &= (0.99 <= q <= 1.01)
        print("    kz %-3d (1-lamD)/tau at cuts 1/20|1/10|1/5: %s"
              % (kz, " | ".join(vals)))
    cut_type = "CUT-ROBUST" if cut_ok else "CUT-SENSITIVE"
    check("E4.1 typed: %s (all ratios in [0.99, 1.01] and I - R "
          "> 0 for all three cuts)" % cut_type, cut_ok)

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    cE = split_rung(9, comb=(np.log(nn.astype(float)),
                             2.0 * lamE_[nn]
                             / np.sqrt(nn.astype(float))))
    cS = split_rung(9, scramble_seed=1)
    fired = (cE is not None and cS is not None
             and cE["lamE"] > 1.0 and cS["lamE"] > 1.0)
    check("C1 CONTROLS FIRE: lam(E) > 1 on Epstein (%.3e) and "
          "scramble (%.3e)"
          % (cE["lamE"] if cE else 0, cS["lamE"] if cS else 0),
          fired, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if not fired:
        VERDICT = "CONTROL-DEAD"
    elif any(k == "K1" for k in KILLS):
        VERDICT = "PIPELINE-BROKEN"
    elif any(k == "K2" for k in KILLS):
        VERDICT = "BULK-BROKEN"
    else:
        VERDICT = "PORT-LIMIT-MEASURED"
    print("\n  VERDICT: %s (%s + %s + %s)"
          % (VERDICT, conv_type, bulk_type, cut_type))
    print("""
  NAMED THEOREM TARGET (printed, not claimed): the dressed port
  family D_P(h) converges entrywise in the j-coordinate to a limit
  operator D_infty of norm EXACTLY 1 (critical); the ladder wall
  ||C_h|| <= 1 is the statement that the finite sections approach
  criticality FROM BELOW.  Margin-based certificates cannot exist
  in the limit; the proof shape is exact criticality of D_infty
  plus one-sided approach.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
