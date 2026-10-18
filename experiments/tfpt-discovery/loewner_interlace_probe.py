#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""loewner_interlace_probe -- PRIME.LOEWNER.INTERLACE.01
(EXPLORATION ONLY, experiments/; round 38 follow-up (c) of the
LXXXIV entry, designed AFTER the omega_source_law run and using its
finding (DIAG-DOMINANT, controls break on the diagonal) as declared
input, 2026-08-09).

THE QUESTION (the honest successor of review proposal 11.2): the
wall is now the embedding E = b_h^2 C^T Phi^2 C <= I with E a
weighted Loewner object whose nodes interlace its poles.  Herglotz
positivity alone does not decide it.  WHICH structure does?  This
probe (i) proves the DUAL Loewner identity numerically, (ii) makes
the interlacing census, (iii) dissects the worst-node anatomy that
the omega run localized, and (iv) measures whether a LOCAL
(single-node Gershgorin) certificate can exist.

THE DUAL IDENTITY, DERIVED BEFORE RUNNING: with
    g(y) := e_{h-1}^T (yI - J)^{-1} e_{h-1} = sum_i phi_i^2/(y-x_i)
(the LAST-entry resolvent = the monic ratio pi_{h-1}(y)/pi_h(y) by
Cramer, pi_{h-1} = charpoly of the leading (h-1)-block), partial
fractions give EXACTLY
    E_mm' = b_h^2 sqrt(om_m om_m') (g(y_m) - g(y_m'))/(y_m' - y_m),
    E_mm  = b_h^2 om_m (-g'(y_m)),
i.e. E = b_h^2 sqrt(om) L(-g) sqrt(om) -- a weighted LOEWNER matrix
of the rational Herglotz function -g (Stieltjes transform of the
Christoffel measure sum phi_i^2 delta_{x_i}) sampled at the omega
support.  Together with the round-38 x-side reading (Delta-hat =
I - b_h^2 Phi L(m_omega) Phi) the wall is a MUTUAL LOEWNER PAIRING
of two positive measures, each sampled on the other's support.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run):
rungs kz in {9, 12, 13} + holdouts {26, 40}; controls kz 9
(Epstein x^2+5y^2, scramble seed 1).  Per rung:

 T1  DUAL IDENTITY: ||E - b_h^2 sqrt(om) L(-g) sqrt(om)||_F /
     ||E||_F <= 1e-6 (the difference-quotient route vs the Gram
     route -- structurally different float paths); and g == monic
     ratio pi_{h-1}/pi_h at the 5 largest-omega nodes (log-sum
     evaluation, rel <= 1e-6).

 T2  MUTUAL PAIRING: the nonzero spectra of the x-side form
     b_h^2 Phi (C C^T) Phi and the y-side E match (top-10 eigen-
     values rel <= 1e-8) -- one wall, two Loewner readings.

 T3  INTERLACING CENSUS (report-typed): fraction of x-gaps
     (x_i, x_{i+1}) containing 0 / 1 / >= 2 omega nodes; the
     mass-weighted version; the port region vs bulk.

 T4  WORST-NODE ANATOMY (the DIAG-DOMINANT follow-up): locate
     m* = argmax_m E_mm; report its tau position (decile), omega
     share om_{m*}/Sigma om, distance to the nearest x_i in units
     of the local gap, and the diagonal profile E_mm across tau
     deciles; typed PORT-SEATED iff m* lies in the lowest tau
     decile, else BULK-SEATED.

 T5  SOFT-MODE SEAT: the top eigenvector of E: tau-decile mass
     profile, overlap^2 with the m* coordinate axis; typed
     ALIGNED iff the top eigenvector puts >= 25 percent of its
     mass in the m* decile.

 T6  LOCAL-CERTIFICATE TEST (frozen rule): at m*, Gershgorin row
     test maxdiag + sum_{m' != m*} |E_{m* m'}| <= 1?  (Perron says
     absolute tests fail for the FULL matrix; this measures whether
     they fail already at the single dominant node.)  Typed
     LOCAL-CERT-EXISTS / LOCAL-CERT-FAILS per rung; report the
     absolute row excess.

 C   CONTROLS (must fire): maxdiag(E) > 1 on Epstein AND scramble
     (the diagonal break of the omega run reproduced within this
     probe); report WHERE the diagonal breaks (tau decile of the
     worst node) -- the localization of the arithmetic failure.

KILLS: K1 dual identity / monic ratio breaks -> DUAL-BROKEN;
K2 spectra mismatch -> PAIRING-BROKEN; K3 a control does not break
on the diagonal -> CONTROL-DEAD.

VERDICT (frozen enum): LOEWNER-DUAL-EXACT (+ typed sublabels
PORT-SEATED/BULK-SEATED, ALIGNED/UNALIGNED, LOCAL-CERT-EXISTS/
LOCAL-CERT-FAILS) / DUAL-BROKEN / PAIRING-BROKEN / CONTROL-DEAD.

FIREWALL: no zeros, no prime-table oracles (AST scan); v563
READ-ONLY; RNG only inside the declared scramble control; writes
nothing but stdout.  NO RH claim; no marker moves.

Sources (read-only): v563_paper2_readouts, cd_pick_scalarization_
probe + omega_source_law_probe (round 38, declared inputs), v866
(heavy set), v879 (tilde convention).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/loewner_interlace_probe.py
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

RUNGS = (9, 12, 13, 26, 40)
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


def log_poly(y, roots):
    """log |prod (y - r)| and its sign, stable for large h."""
    dif = y - roots
    return float(np.sum(np.log(np.abs(dif)))), \
        int(np.prod(np.sign(dif)))


def anatomy(kz, tag, **kw):
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
    Pn = eval_chain(al, be, m0, ys, h + 1)
    om = vs * Pn[:, h] ** 2
    xg, Q = np.linalg.eigh(J)
    phi = Q[h - 1, :]
    Cmat = np.sqrt(om)[None, :] / (ys[None, :] - xg[:, None])
    E = (bh ** 2) * (Cmat.T @ ((phi ** 2)[:, None] * Cmat))
    E = 0.5 * (E + E.T)
    evE, VE = np.linalg.eigh(E)
    lam = float(evE[-1])
    # T1 dual identity: difference-quotient route
    gy = ((phi ** 2)[None, :] / (ys[:, None] - xg[None, :])) \
        @ np.ones(h)
    gprime = ((phi ** 2)[None, :]
              / (ys[:, None] - xg[None, :]) ** 2) @ np.ones(h)
    dq = (gy[:, None] - gy[None, :]) / (
        ys[None, :] - ys[:, None]
        + np.eye(len(ys)))                    # diag placeholder
    np.fill_diagonal(dq, gprime)
    # dq_mm' = (g(y_m)-g(y_m'))/(y_m'-y_m) = L(-g); diag = -g' >= 0
    Edual = (bh ** 2) * (np.sqrt(om)[:, None] * dq
                         * np.sqrt(om)[None, :])
    rel_dual = float(np.linalg.norm(E - Edual)
                     / np.linalg.norm(E))
    # monic ratio at the 5 largest-omega nodes
    x_sub = np.linalg.eigvalsh(J[:h - 1, :h - 1])
    idx5 = np.argsort(om)[-5:]
    rel_ratio = 0.0
    for m in idx5:
        y0 = ys[m]
        ln1, s1 = log_poly(y0, x_sub)
        ln2, s2 = log_poly(y0, xg)
        ratio = s1 * s2 * math.exp(ln1 - ln2)
        rel_ratio = max(rel_ratio,
                        abs(gy[m] - ratio) / max(abs(gy[m]),
                                                 1e-30))
    # T2 mutual pairing: x-side form
    Fx = (bh ** 2) * (phi[:, None] * (Cmat @ Cmat.T)
                      * phi[None, :])
    evX = np.sort(np.linalg.eigvalsh(0.5 * (Fx + Fx.T)))[::-1]
    evY = np.sort(evE)[::-1]
    k10 = min(10, h, len(ys))
    rel_pair = float(np.max(np.abs(evX[:k10] - evY[:k10])
                            / np.maximum(np.abs(evY[:k10]),
                                         1e-30)))
    # T3 interlacing census
    gaps = np.searchsorted(xg, ys)            # which gap each y is in
    inner = (gaps > 0) & (gaps < h)
    cnt = np.bincount(gaps[inner], minlength=h + 1)[1:h]
    n_gaps = h - 1
    f0 = float(np.sum(cnt == 0)) / n_gaps
    f1 = float(np.sum(cnt == 1)) / n_gaps
    f2 = float(np.sum(cnt >= 2)) / n_gaps
    # T4 worst node
    diag = np.diag(E)
    mstar = int(np.argmax(diag))
    tau_m = (2.0 * math.pi * uf_n / L) / D
    tmax = float(np.max(tau_m))
    dec_star = min(int(10 * tau_m[mstar] / tmax), 9)
    om_share = float(om[mstar] / np.sum(om))
    d_near = float(np.min(np.abs(ys[mstar] - xg)))
    gi = np.searchsorted(xg, ys[mstar])
    loc_gap = float(xg[min(gi, h - 1)] - xg[max(gi - 1, 0)])
    dec_prof = np.zeros(10)
    for m in range(len(ys)):
        dec_prof[min(int(10 * tau_m[m] / tmax), 9)] = max(
            dec_prof[min(int(10 * tau_m[m] / tmax), 9)],
            diag[m])
    # T5 soft mode seat
    top = VE[:, -1] ** 2
    dec_top = np.zeros(10)
    for m in range(len(ys)):
        dec_top[min(int(10 * tau_m[m] / tmax), 9)] += top[m]
    aligned = float(dec_top[dec_star])
    # T6 local certificate at m*
    row_off = float(np.sum(np.abs(E[mstar])) - abs(E[mstar,
                                                     mstar]))
    gersh = float(diag[mstar]) + row_off
    print("    %-20s h %4d  lam %.6f  maxdiag %.6f (decile %d, "
          "omega-share %.3f, d/gap %.2f)"
          % (tag, h, lam, float(diag[mstar]), dec_star, om_share,
             d_near / max(loc_gap, 1e-30)))
    print("      T1 dual rel %.1e | ratio rel %.1e | T2 pairing "
          "rel %.1e | gaps 0/1/2+: %.2f/%.2f/%.2f | soft-mass in "
          "m*-decile %.2f | Gershgorin(m*) %.3f (off %.3f)"
          % (rel_dual, rel_ratio, rel_pair, f0, f1, f2, aligned,
             gersh, row_off))
    print("      diag profile (max per tau decile): %s"
          % "/".join("%.3f" % v for v in dec_prof))
    print("      soft-mode tau-decile mass: %s"
          % "/".join("%.2f" % v for v in dec_top))
    return dict(h=h, lam=lam, maxdiag=float(diag[mstar]),
                rel_dual=rel_dual, rel_ratio=rel_ratio,
                rel_pair=rel_pair, f0=f0, f1=f1, f2=f2,
                dec_star=dec_star, om_share=om_share,
                aligned=aligned, gersh=gersh, row_off=row_off)


def main():
    section("PRIME.LOEWNER.INTERLACE.01 -- the mutual Loewner "
            "pairing + worst-node anatomy (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    section("T1-T6 -- rungs %s (26/40 = holdouts)" % (RUNGS,))
    res = {}
    for kz in RUNGS:
        res[kz] = anatomy(kz, "kz %d%s"
                          % (kz, " (HOLDOUT)" if kz in (26, 40)
                             else ""))
    ok_all = all(r is not None for r in res.values())
    check("T0 all chains complete", ok_all, kill="K1")
    if ok_all:
        check("T1 DUAL IDENTITY: E == b_h^2 sqrt(om) L(-g) sqrt(om) "
              "on all rungs (max rel %.1e <= 1e-6) and g == monic "
              "pi_{h-1}/pi_h at the 5 heaviest nodes (max rel %.1e "
              "<= 1e-6) -- the wall is a weighted LOEWNER matrix of "
              "the Christoffel resolvent"
              % (max(r["rel_dual"] for r in res.values()),
                 max(r["rel_ratio"] for r in res.values())),
              max(r["rel_dual"] for r in res.values()) <= 1e-6
              and max(r["rel_ratio"] for r in res.values()) <= 1e-6,
              kill="K1")
        check("T2 MUTUAL PAIRING: x-side and y-side Loewner "
              "readings share the top-10 spectrum on all rungs "
              "(max rel %.1e <= 1e-8) -- one wall, two positive "
              "measures, each sampled on the other's support"
              % max(r["rel_pair"] for r in res.values()),
              max(r["rel_pair"] for r in res.values()) <= 1e-8,
              kill="K2")
        seat = ("PORT-SEATED"
                if all(r["dec_star"] == 0 for r in res.values())
                else "BULK-SEATED")
        align = ("ALIGNED"
                 if all(r["aligned"] >= 0.25 for r in res.values())
                 else "UNALIGNED")
        cert = ("LOCAL-CERT-EXISTS"
                if all(r["gersh"] <= 1.0 for r in res.values())
                else "LOCAL-CERT-FAILS")
        check("T4/T5/T6 typed: worst-node deciles %s -> %s; "
              "soft-mass at m* decile %s -> %s; Gershgorin(m*) %s "
              "-> %s"
              % (sorted(r["dec_star"] for r in res.values()), seat,
                 ["%.2f" % r["aligned"] for r in res.values()],
                 align,
                 ["%.3f" % r["gersh"] for r in res.values()], cert),
              True)
    else:
        seat = align = cert = "N/A"

    section("C -- controls (kz 9; diagonal break must reproduce)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctl = {}
    ctl["Epstein"] = anatomy(9, "Epstein (control)",
                             comb=(np.log(nn.astype(float)),
                                   2.0 * lamE[nn]
                                   / np.sqrt(nn.astype(float))))
    ctl["scramble"] = anatomy(9, "scramble (control)",
                              scramble_seed=1)
    ctl_ok = all(c is not None for c in ctl.values())
    fired = ctl_ok and all(c["maxdiag"] > 1.0 for c in ctl.values())
    check("C1 CONTROLS BREAK ON THE DIAGONAL: maxdiag > 1 on both "
          "(Epstein %.3e at decile %s, scramble %.3e at decile %s) "
          "-- the arithmetic failure is LOCALIZED"
          % (ctl["Epstein"]["maxdiag"] if ctl_ok else 0,
             ctl["Epstein"]["dec_star"] if ctl_ok else "-",
             ctl["scramble"]["maxdiag"] if ctl_ok else 0,
             ctl["scramble"]["dec_star"] if ctl_ok else "-"),
          fired, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if not fired:
        VERDICT = "CONTROL-DEAD"
    elif KILLS:
        VERDICT = {"K1": "DUAL-BROKEN",
                   "K2": "PAIRING-BROKEN"}.get(KILLS[0],
                                               "CONTROL-DEAD")
    else:
        VERDICT = "LOEWNER-DUAL-EXACT"
    print("\n  VERDICT: %s (%s + %s + %s)"
          % (VERDICT, seat, align, cert))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
