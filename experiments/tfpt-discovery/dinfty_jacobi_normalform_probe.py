#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dinfty_jacobi_normalform_probe -- PRIME.DINFTY.JACOBI.01
(EXPLORATION ONLY, experiments/; round 38, executing the LXXXIX
named object (a) = the survey's Rank-1 suggestion: is the port
limit operator a CRITICAL Jacobi matrix in the Janas-Naboko /
Yafaev sense (transfer matrix at the spectral edge lambda = 1
approaching a JORDAN BLOCK)?, 2026-08-09).

CONTEXT: the dressed port family D_P(h) converges entrywise
(LXXXVII, ENTRY-CONVERGENT) with lam_max(D_P) = 1 - tau -> 1 from
below -- the limit operator D_infty is norm-critical.  The
classical trichotomy for Jacobi-type operators at a spectral edge
(Janas-Naboko double-root case; Yafaev |gamma| = 1): with local
transfer matrix at lambda = 1,
    T_k = [[(1 - a_k)/b_k, -b_{k-1}/b_k], [1, 0]],
the discriminant  Delta_k = ((1 - a_k)/b_k)^2 - 4 b_{k-1}/b_k
decides:  Delta -> 0 (double root, JORDAN BLOCK) = CRITICAL;
Delta -> positive constant = SUBCRITICAL (gap, edge not attained);
Delta -> negative = SUPERCRITICAL (lambda = 1 inside the band).
FALSIFIER: if the truth chain is NOT in the Jordan class, the
criticality reading of D_infty is mistyped and the round-38
reduction must be re-read.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; full ladder h <= 900 for convergence, heavy rungs
kz {9, 12, 13, 26, 40} for profiles; controls kz 9):

 J1  NORMAL FORM: Lanczos-tridiagonalize D_P(h) with start
     vector e_1 (the first port node, the pole-port seat; full
     reorthogonalization).  Wards: reconstruction
     ||Q^T D_P Q - tri||_F / ||D_P||_F <= 1e-10 and all b_k > 0
     (chain complete) on every heavy rung.

 J2  COEFFICIENT CONVERGENCE (the Jacobi normal form of
     D_infty): a_k(h), b_k(h) at fixed k in {0..5} vs the deepest
     rung across the full ladder: sup-difference trend log-log
     slope <= -0.15 (typed JACOBI-CONVERGENT / DRIFTING); the
     limit coefficients (first 8) printed -- the first Jacobi
     normal form of the port limit operator.

 J3  THE TRICHOTOMY (the headline): the discriminant profile
     Delta_k on the chain interior (k in [m/4, 3m/4]) at every
     heavy rung; typed from the deepest rung's interior median
     med(Delta):
       CRITICAL-JORDAN     iff |med| <= 0.1,
       SUBCRITICAL-GAP     iff med > +0.1,
       SUPERCRITICAL-BAND  iff med < -0.1;
     plus the h-trend of |med| (report).  The edge-criticality
     profile c_k = 1 - a_k - 2 b_k is printed alongside (the
     free-edge reading; b_k -> 1/2 would echo the Szego law).

 J4  EIGENVECTOR SHAPE (report): the top eigenvector psi of the
     tridiagonal form: decay type via log|psi_k| regression --
     critical chains carry polynomially-decaying (non-Weyl) edge
     vectors, subcritical ones exponential.

 C   CONTROLS (kz 9, must fire): Epstein and scramble through
     the SAME machinery (their I - R may be indefinite; the
     dressing solve is still defined): their typing must NOT be
     CRITICAL-JORDAN (lambda = 1 lies inside their spectrum:
     expected SUPERCRITICAL-BAND) -- the Jordan class is not an
     artifact of the pipeline.

KILLS: K1 pipeline/tridiagonalization breaks -> PIPELINE-BROKEN;
K2 truth typing = SUBCRITICAL-GAP (the falsifier: criticality
mistyped) -> CRITICALITY-MISTYPED; K3 a control lands in
CRITICAL-JORDAN -> CONTROL-DEAD.

VERDICT (frozen enum): JORDAN-CLASS-CONFIRMED (truth
CRITICAL-JORDAN + controls fire) / CRITICALITY-MISTYPED /
SUPERCRITICAL-SURPRISE (truth band-interior; typed, honest) /
PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: no zeros, no prime-table oracles (AST
scan); v563 READ-ONLY; RNG only inside the declared scramble
control; writes nothing but stdout.  No marker moves.

Sources (read-only): v563_paper2_readouts; round-38 chain
(port_schur_reduction / port_limit_operator probes, declared
inputs); survey LXXXIX (Janas-Naboko / Yafaev trichotomy).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/dinfty_jacobi_normalform_probe.py
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
    return dict(DP=DP, h=h, alpha=b["alpha"], m=DP.shape[0],
                lamE=float(np.linalg.eigvalsh(G)[-1]))


def tridiagonalize(A):
    """Lanczos from e_1 with full reorth; returns (a, b, Q)."""
    m = A.shape[0]
    Q = np.zeros((m, m))
    Q[0, 0] = 1.0
    a = np.zeros(m)
    b = np.zeros(m - 1)
    steps = m
    for k in range(m):
        z = A @ Q[:, k]
        a[k] = float(Q[:, k] @ z)
        z = z - a[k] * Q[:, k]
        if k > 0:
            z = z - b[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == m - 1:
            break
        nb = float(np.linalg.norm(z))
        if nb <= 1e-13:
            steps = k + 1
            break
        b[k] = nb
        Q[:, k + 1] = z / nb
    return a[:steps], b[:max(steps - 1, 0)], Q[:, :steps], steps


def profile_of(DP):
    a, b, Q, steps = tridiagonalize(DP)
    m = len(a)
    tri = np.diag(a)
    if m > 1:
        tri += np.diag(b, 1) + np.diag(b, -1)
    rec = float(np.linalg.norm(Q.T @ DP @ Q - tri)
                / np.linalg.norm(DP))
    # trichotomy discriminant on the interior
    disc = []
    cker = []
    for k in range(1, m - 1):
        if b[k] <= 0:
            continue
        disc.append(((1.0 - a[k]) / b[k]) ** 2
                    - 4.0 * b[k - 1] / b[k])
        cker.append(1.0 - a[k] - 2.0 * b[k])
    disc = np.array(disc)
    cker = np.array(cker)
    lo, hi = max(1, m // 4), max(2, (3 * m) // 4)
    med = float(np.median(disc[lo - 1:hi - 1])) if len(disc) else 0.0
    # top eigenvector decay in chain coordinates
    ev, V = np.linalg.eigh(tri)
    psi = np.abs(V[:, -1]) + 1e-300
    kk = np.arange(m)
    sl_exp = float(np.polyfit(kk, np.log(psi), 1)[0])
    sl_pol = float(np.polyfit(np.log(kk + 1.0), np.log(psi), 1)[0])
    return dict(a=a, b=b, m=m, rec=rec, steps=steps, disc=disc,
                cker=cker, med=med, sl_exp=sl_exp, sl_pol=sl_pol,
                lam_tri=float(ev[-1]))


def typing_of(med):
    if abs(med) <= 0.1:
        return "CRITICAL-JORDAN"
    return "SUBCRITICAL-GAP" if med > 0.1 else "SUPERCRITICAL-BAND"


def main():
    section("PRIME.DINFTY.JACOBI.01 -- the Jordan-block test of "
            "the port limit operator (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("J1/J3/J4 -- normal form + trichotomy (heavy rungs)")
    profs = {}
    for kz in HEAVY:
        r = dressed_port(kz)
        p = profile_of(r["DP"])
        profs[kz] = (r, p)
        inner = slice(max(1, p["m"] // 4), max(2, 3 * p["m"] // 4))
        print("    kz %-3d h %4d m %3d: rec %.1e | med(Delta) "
              "interior %+.4f | c_k interior [%.3f, %.3f] | "
              "b_k interior [%.3f, %.3f] | psi decay exp %+.3f "
              "poly %+.2f"
              % (kz, r["h"], p["m"], p["rec"], p["med"],
                 float(np.min(p["cker"][inner])),
                 float(np.max(p["cker"][inner])),
                 float(np.min(p["b"][inner])),
                 float(np.max(p["b"][inner])),
                 p["sl_exp"], p["sl_pol"]))
    ok_rec = all(p["rec"] <= 1e-10 and p["steps"] == p["m"]
                 for _r, p in profs.values())
    check("J1.1 NORMAL FORM: tridiagonalization exact (max rec "
          "%.1e <= 1e-10) with complete chains on all heavy rungs"
          % max(p["rec"] for _r, p in profs.values()),
          ok_rec, kill="K1")

    deep_kz = max(HEAVY, key=lambda kz: profs[kz][0]["h"])
    med_deep = profs[deep_kz][1]["med"]
    truth_type = typing_of(med_deep)
    meds = {kz: profs[kz][1]["med"] for kz in HEAVY}
    print("    med(Delta) along rungs: %s"
          % ", ".join("kz%d %+0.4f" % (kz, meds[kz])
                      for kz in HEAVY))
    print("    Jacobi normal form of D_P (deepest rung kz %d), "
          "first 8:" % deep_kz)
    ad, bd = profs[deep_kz][1]["a"], profs[deep_kz][1]["b"]
    print("      a_k: %s" % " ".join("%+.5f" % v for v in ad[:8]))
    print("      b_k: %s" % " ".join("%+.5f" % v for v in bd[:8]))
    check("J3.1 TRICHOTOMY typed from the deepest rung: "
          "med(Delta) = %+.4f -> %s (falsifier bar: SUBCRITICAL "
          "would mistype the round-38 criticality)"
          % (med_deep, truth_type),
          truth_type != "SUBCRITICAL-GAP", kill="K2")

    section("J2 -- coefficient convergence (full ladder)")
    rows = []
    for kz in core.frame_a_zones():
        r = dressed_port(kz)
        if r in (None, "TOO-DEEP"):
            continue
        p = profile_of(r["DP"])
        rows.append((r["h"], p))
    rows.sort(key=lambda t: t[0])
    h_deep, p_deep = rows[-1]
    difs = []
    for hh, p in rows[:-1]:
        k6 = min(6, len(p["a"]), len(p_deep["a"]))
        da = float(np.max(np.abs(p["a"][:k6] - p_deep["a"][:k6])))
        db = float(np.max(np.abs(p["b"][:k6 - 1]
                                 - p_deep["b"][:k6 - 1])))
        difs.append((hh, max(da, db)))
    hh_v = np.array([x[0] for x in difs], float)
    dd_v = np.array([x[1] for x in difs])
    mask = hh_v <= h_deep / 2.0
    sl = float(np.polyfit(np.log(hh_v[mask]),
                          np.log(dd_v[mask]), 1)[0])
    conv_type = ("JACOBI-CONVERGENT" if sl <= -0.15
                 else "JACOBI-DRIFTING")
    check("J2.1 typed: %s (sup-diff of (a_k, b_k), k <= 5, vs "
          "deepest: %.4f -> %.4f, log-log slope %+.3f, bar <= "
          "-0.15) -- the Jacobi normal form of D_infty converges"
          % (conv_type, dd_v[0], dd_v[-1], sl), sl <= -0.15)

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
        r = dressed_port(9, **kw)
        p = profile_of(r["DP"])
        t = typing_of(p["med"])
        ok_ctl &= (t != "CRITICAL-JORDAN")
        print("    %-8s: lam(E) %.3e | med(Delta) %+.3f -> %s"
              % (nmc, r["lamE"], p["med"], t))
    check("C1 CONTROLS FIRE: neither control lands in "
          "CRITICAL-JORDAN (lambda = 1 is not their critical "
          "edge)", ok_ctl, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "CRITICALITY-MISTYPED",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    elif truth_type == "CRITICAL-JORDAN":
        VERDICT = "JORDAN-CLASS-CONFIRMED"
    else:
        VERDICT = "SUPERCRITICAL-SURPRISE"
    print("\n  VERDICT: %s (%s + %s)"
          % (VERDICT, truth_type, conv_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
