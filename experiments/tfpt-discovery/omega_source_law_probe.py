#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""omega_source_law_probe -- PRIME.OMEGA.SOURCELAW.01
(EXPLORATION ONLY, experiments/; round 38 follow-up (b) of the
LXXXIV entry: the h-law of the scalar wall carrier, 2026-08-09).

CONTEXT: cd_pick_scalarization_probe (round 38, PICK-SCALARIZED)
compressed the Krein wall into ONE scalar statement -- the Cauchy-
Christoffel embedding E = b_h^2 C^T Phi^2 C <= I of the positive
source measure omega = nu~-weighted p_h^2 against the Christoffel
weights phi_i^2, with lam_max(E) = 1 - tau EXACTLY.  The round-37
named open object (a) (source-law persistence for h -> infinity) is
therefore now concentrated in ONE measure.  This probe MEASURES the
h-law of that carrier along the full reachable ladder.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run):
ladder = all frame_a_zones rungs with h <= 900 (the 42-rung v866
convention; the ATOM_MAX truncation wall of v877 makes deeper rungs
unreliable -- excluded by design).  Per rung, from the scalarization
pipeline (chain of mu~+, ends b_h; omega on the nu~- support; Gauss
nodes x_i; phi_i = last eigenvector components):

 S1  LADDER CENSUS: every rung builds, chain completes h+1 steps
     with be > 0 (frozen bar: ZERO skipped rungs), and the embedding
     transfer lam_max(E) == 1 - tau holds at rel <= 1e-6 per rung.

 S2  b_h UNIFORMITY (frozen bars, v879 convention): max/min <= 2.0
     AND |log-log slope of b_h vs h| <= 0.15.  An honest FAIL types
     BH-DRIFT and is kept (the finding either way).

 S3  MASS + PROFILE LAW (measurement, report-typed): Sigma omega
     range and log-log slope vs h; the tau-decile profile of omega
     (v866 weight-band convention, tau_m = theta_m L /(2 pi D)/...
     = (2 pi uf/L)/D) with the PORT SHARE = omega-mass fraction in
     the lowest tau decile; slopes reported fit-free.

 S4  THE LAW HUNT (predeclared candidates, frozen success rule):
     Pearson correlation of log tau against each of
       {alpha, log Sigma_omega, log b_h, log maxdiag(E),
        log mingap, port_share}
     over all truth rungs; the known defect law is log tau vs alpha
     (v866: slope -2.40, Pearson -0.935); SUCCESS TYPE
     OMEGA-CARRIES-LAW iff some NON-alpha candidate reaches
     |Pearson| >= 0.90 (else typed ALPHA-ONLY; both honest).

 S5  DIAGONAL SHARE (the certificate-shape question, typed
     dichotomy): r_diag = max_m E_mm / lam_max(E) per rung (E is
     PSD, so r_diag <= 1 automatically).  If the wall norm is
     asymptotically DIAGONAL in these coordinates (median r_diag >=
     0.5 and non-decreasing trend), a per-node Markov-quotient bound
     would asymptotically suffice -- typed DIAG-DOMINANT; else typed
     OFF-DIAGONAL-CARRIED (the cancellation lives between nodes).

 S6  CONTROLS (kz 9, MUST FIRE): Epstein x^2+5y^2 and scramble seed
     1: lam_max(E) > 1 on both; TYPED READOUT (either way a
     finding): does the control break already on the DIAGONAL
     (max_m E_mm > 1 -- a localized break) or only coherently?

KILLS: K1 census/transfer breaks -> PIPELINE-BROKEN; K2 a control
does not fire on the value -> CONTROL-DEAD.  S2 may FAIL honestly
(BH-DRIFT typed, exit 1, kept).

VERDICT (frozen enum): OMEGA-LAW-MEASURED (+ typed sublabels
OMEGA-CARRIES-LAW/ALPHA-ONLY, DIAG-DOMINANT/OFF-DIAGONAL-CARRIED,
BH-UNIFORM/BH-DRIFT) / PIPELINE-BROKEN / CONTROL-DEAD.

FIREWALL: no zeros, no prime-table oracles (AST scan); v563
READ-ONLY; RNG only inside the declared scramble control; writes
nothing but stdout.  NO RH claim; no marker moves.

Sources (read-only): v563_paper2_readouts (comb + windows), v866
(42-rung ladder + defect law), v879 (uniformity-bar convention),
cd_pick_scalarization_probe (the scalarization pipeline, round 38).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/omega_source_law_probe.py
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
    K = core.odd_toeplitz(c, M)
    d = grid_density(c)
    L = 2 * M - 2
    c_abs = np.real(np.fft.ifft(np.abs(d)))[:M]
    Tabs = core.odd_toeplitz(c_abs, M)
    return dict(d=d, K=K, Tabs=Tabs, L=L, D=D, alpha=alpha, h=h)


def tau_frame(b):
    Gp = 0.5 * (b["Tabs"] + b["K"])
    Gm = 0.5 * (b["Tabs"] - b["K"])
    ev, V = np.linalg.eigh(Gp)
    R = V @ np.diag(ev ** -0.5) @ V.T
    A = R @ Gm @ R
    lam = np.linalg.eigvalsh(0.5 * (A + A.T))
    return 1.0 - float(lam[-1])


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


def rung_scalars(kz, **kw):
    """The omega carrier scalars of one rung (or None if short)."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return "TOO-DEEP"
    tau = tau_frame(b)
    xs, ws, _uf = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    J = np.diag(al[:h]) + np.diag(be[:h - 1], 1) \
        + np.diag(be[:h - 1], -1)
    bh = float(be[h - 1])
    Pn = eval_chain(al, be, m0, ys, h + 1)
    om = vs * Pn[:, h] ** 2
    xg, Q = np.linalg.eigh(J)
    phi = Q[h - 1, :]
    Cmat = np.sqrt(om)[None, :] / (ys[None, :] - xg[:, None])
    E = (bh ** 2) * (Cmat.T @ ((phi ** 2)[:, None] * Cmat))
    E = 0.5 * (E + E.T)
    lam_emb = float(np.linalg.eigvalsh(E)[-1])
    maxdiag = float(np.max(np.diag(E)))
    # tau-coordinate deciles of omega (v866 band convention)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    edges = np.linspace(0.0, float(np.max(tau_m)), 11)
    prof = np.array([float(np.sum(om[(tau_m >= edges[i])
                                     & (tau_m <= edges[i + 1])]))
                     for i in range(10)])
    port = float(prof[0] / np.sum(om))
    # interlacing gap (relative to mean node spacing)
    gap = float(np.min(np.abs(ys[None, :] - xg[:, None])))
    mean_dx = float((xg[-1] - xg[0]) / max(h - 1, 1))
    return dict(kz=kz, h=h, alpha=b["alpha"], tau=tau, bh=bh,
                mass=float(np.sum(om)), lam_emb=lam_emb,
                maxdiag=maxdiag, port=port,
                gap_rel=gap / mean_dx,
                rel_emb=abs(lam_emb - (1.0 - tau))
                / max(abs(1.0 - tau), 1e-30),
                prof=prof / np.sum(om))


def slope(xv, yv):
    return float(np.polyfit(xv, yv, 1)[0])


def pearson(xv, yv):
    return float(np.corrcoef(xv, yv)[0, 1])


def main():
    section("PRIME.OMEGA.SOURCELAW.01 -- the h-law of the scalar "
            "wall carrier (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("S1 -- ladder census (all frame_a_zones, h <= 900)")
    rows = []
    n_short = 0
    for kz in core.frame_a_zones():
        r = rung_scalars(kz)
        if r == "TOO-DEEP":
            continue
        if r is None:
            n_short += 1
            print("    kz %-4d CHAIN SHORT (typed)" % kz)
            continue
        rows.append(r)
        print("    kz %-4d h %4d  tau %+.3e  b_h %.4f  |omega| "
              "%.3e  maxdiag %.4f  r_diag %.3f  port %.3f  "
              "gap_rel %.2e"
              % (r["kz"], r["h"], r["tau"], r["bh"], r["mass"],
                 r["maxdiag"], r["maxdiag"] / r["lam_emb"],
                 r["port"], r["gap_rel"]), flush=True)
    check("S1.1 census: %d rungs kept, %d chain-short (bar 0); "
          "embedding transfer lam_max(E) == 1 - tau on all rungs "
          "(max rel %.1e <= 1e-6)"
          % (len(rows), n_short,
             max(r["rel_emb"] for r in rows) if rows else 1.0),
          rows and n_short == 0
          and max(r["rel_emb"] for r in rows) <= 1e-6, kill="K1")

    hh = np.array([r["h"] for r in rows], float)
    bhv = np.array([r["bh"] for r in rows])
    section("S2 -- b_h uniformity (frozen bars)")
    ratio = float(np.max(bhv) / np.min(bhv))
    sl_bh = slope(np.log(hh), np.log(bhv))
    bh_uniform = ratio <= 2.0 and abs(sl_bh) <= 0.15
    check("S2.1 b_h in [%.4f, %.4f]: max/min %.3f <= 2.0 and "
          "|log-log slope| %.3f <= 0.15"
          % (float(np.min(bhv)), float(np.max(bhv)), ratio,
             abs(sl_bh)), bh_uniform)

    section("S3 -- mass + profile law (measurement)")
    mass = np.array([r["mass"] for r in rows])
    ports = np.array([r["port"] for r in rows])
    print("    Sigma omega in [%.3e, %.3e], log-log slope vs h "
          "%+.3f; port share in [%.3f, %.3f], slope vs log h %+.3f"
          % (float(np.min(mass)), float(np.max(mass)),
             slope(np.log(hh), np.log(mass)),
             float(np.min(ports)), float(np.max(ports)),
             slope(np.log(hh), ports)))
    prof_med = np.median(np.vstack([r["prof"] for r in rows]),
                         axis=0)
    print("    median tau-decile profile of omega: %s"
          % "/".join("%.3f" % p for p in prof_med))
    check("S3.1 profile measured (report; positivity of omega "
          "already warded in round 38)", True)

    section("S4 -- the law hunt (predeclared candidates)")
    lt = np.log(np.array([r["tau"] for r in rows]))
    cands = {
        "alpha": np.array([r["alpha"] for r in rows]),
        "log Sigma_omega": np.log(mass),
        "log b_h": np.log(bhv),
        "log maxdiag": np.log(np.array([r["maxdiag"]
                                        for r in rows])),
        "log mingap": np.log(np.array([r["gap_rel"]
                                       for r in rows])),
        "port_share": ports,
    }
    best_non_alpha = 0.0
    for nm, xv in cands.items():
        pr = pearson(xv, lt)
        print("    log tau vs %-16s: Pearson %+.3f  slope %+.3f"
              % (nm, pr, slope(xv, lt)))
        if nm != "alpha":
            best_non_alpha = max(best_non_alpha, abs(pr))
    law_type = ("OMEGA-CARRIES-LAW" if best_non_alpha >= 0.90
                else "ALPHA-ONLY")
    check("S4.1 typed: best non-alpha |Pearson| = %.3f -> %s "
          "(success rule >= 0.90; both outcomes honest)"
          % (best_non_alpha, law_type), True)

    section("S5 -- diagonal share (certificate-shape dichotomy)")
    rdiag = np.array([r["maxdiag"] / r["lam_emb"] for r in rows])
    med_rd = float(np.median(rdiag))
    sl_rd = slope(np.log(hh), rdiag)
    diag_type = ("DIAG-DOMINANT" if med_rd >= 0.5 and sl_rd >= -0.02
                 else "OFF-DIAGONAL-CARRIED")
    check("S5.1 typed: r_diag median %.3f (range [%.3f, %.3f]), "
          "trend slope %+.3f -> %s"
          % (med_rd, float(np.min(rdiag)), float(np.max(rdiag)),
             sl_rd, diag_type), True)

    section("S6 -- controls (kz 9; the value must fire)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctl = {}
    ctl["Epstein"] = rung_scalars(
        9, comb=(np.log(nn.astype(float)),
                 2.0 * lamE[nn] / np.sqrt(nn.astype(float))))
    ctl["scramble"] = rung_scalars(9, scramble_seed=1)
    ok_fire = all(c is not None and not isinstance(c, str)
                  and c["lam_emb"] > 1.0 for c in ctl.values())
    for nm, c in ctl.items():
        print("    %-8s: lam_emb %.4e  maxdiag %.4e  -> break is %s"
              % (nm, c["lam_emb"], c["maxdiag"],
                 "DIAGONAL (localized)" if c["maxdiag"] > 1.0
                 else "COHERENT (off-diagonal)"))
    check("S6.1 CONTROLS FIRE: lam_max(E) > 1 on Epstein and "
          "scramble", ok_fire, kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "OMEGA-LAW-MEASURED"
    sub = "%s + %s + %s" % (law_type, diag_type,
                            "BH-UNIFORM" if bh_uniform
                            else "BH-DRIFT")
    print("\n  VERDICT: %s (%s)" % (VERDICT, sub))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
