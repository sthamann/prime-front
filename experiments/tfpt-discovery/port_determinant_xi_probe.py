#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_determinant_xi_probe -- PRIME.PORT.DETXI.01
(EXPLORATION ONLY, experiments/; round 38, executing the LXXXIX
named object (b) = the survey's Rank-3 suggestion: does the edge
spectrum of the dressed port family track zero-comb structure --
the determinant/CCM twin test, 2026-08-09).

THE QUESTION: the CCM zeta-spectral-triple program builds finite
prime-generated matrices whose regularized determinants converge
to Xi; the round-38 dressed port family D_P(h) is a structural
twin (prime-built, critical, margin-free limit).  First
measurement: (i) does the SCALED edge spectrum of D_P(h) --
u_i := (1 - lam_i)/(1 - lam_1), the gap ratios in units of tau --
stabilize along the ladder (a discrete scaled spectrum of the
limit operator)?  (ii) does it track the zero-ordinate ratios
(gamma_i/gamma_1)^p for a frozen power p (DIAGNOSTIC comparison;
zero data from the committed cache, used ONLY as a comparison
target, never in construction -- the exclusion-battery
precedent)?  (iii) do the normalized determinant sections
converge on the scaled window (the finite Fredholm approximant)?

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; heavy rungs kz {9, 12, 13, 26, 40}; controls kz 9):

 X1  SCALED EDGE SPECTRUM: u_1..u_10 per rung (u_1 = 1); typed
     LIMIT-SPECTRUM-STABLE iff the pairwise max relative
     deviation over the three DEEPEST rungs (kz 13, 26, 40) is
     <= 0.15 for i <= 5, else SPECTRUM-DRIFTING (both honest;
     shallow rungs printed for the trend).

 X2  GAMMA TRACKING (diagnostic-only zero cache, declared): with
     r_i = (gamma_i/gamma_1)^p, p in {1, 2} frozen: typed
     TRACKS-GAMMA(p) iff max_{i<=5} |u_i - r_i|/r_i <= 0.15 at
     the deepest rung for some p, else NO-TRACK (expected-honest:
     a raw two-parameter guess; NO-TRACK kills only the naive
     mapping, not the twin reading).

 X3  DETERMINANT SECTION: F_h(w) := log|det(zI - D_P)| -
     log|det(zI)| at z = 1 - w (1 - lam_1), w on the frozen grid
     {0.5, 1, 2, 4, 8, 12}; typed DET-SECTION-CONVERGENT iff the
     sup-difference of F_h between consecutive heavy rungs is
     monotonically decreasing, else DET-SECTION-DRIFTING.

 C   CONTROLS (kz 9, must fire): Epstein and scramble: lam_max >
     1 (edge crossed -- no scaled edge spectrum exists on the
     truth side of 1); their u-sequences printed (report).

KILLS: K1 pipeline breaks -> PIPELINE-BROKEN; K2 a control does
not fire -> CONTROL-DEAD.  X1/X2/X3 are typed dichotomies (all
outcomes honest).

VERDICT (frozen enum): DETXI-MEASURED (+ typed sublabels) /
PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim; no Hilbert-Polya claim -- a NO-TRACK on the naive
mapping is the expected honest baseline; the value of the probe
is the X1/X3 limit-structure measurement plus the recorded
baseline for any future CCM-normalization comparison.

SPEC v2 (design-slip repair; run 1 = 5/5 but X3 returned NaN):
the frozen w-grid contained w = 1.0, which evaluates the section
EXACTLY at the top eigenvalue z = lam_1 (log 0 by construction --
a structural collision, not numerics).  v2 grid {0.3, 0.7, 1.3,
3, 6, 10} avoids the built-in collision; no other change.

FIREWALL: construction uses NO zero data (AST scan for oracles;
the cache is read as a JSON file and enters ONLY the X2
comparison target, declared diagnostic per the exclusion-battery
precedent); v563 READ-ONLY; RNG only inside the declared
scramble control; writes nothing but stdout.  No marker moves.

Sources (read-only): v563_paper2_readouts; round-38 chain
(port_schur_reduction / port_limit_operator, declared inputs);
zero_comb_cache_n2000.json (diagnostic target only); survey
LXXXIX (CCM twin reading); v592 (continuum determinant law,
narrative sibling -- different object, no numeric reuse).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_determinant_xi_probe.py
"""

import ast
import hashlib
import json
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
DEEP3 = (13, 26, 40)
WGRID = (0.3, 0.7, 1.3, 3.0, 6.0, 10.0)
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
    ev = np.linalg.eigvalsh(DP)[::-1]
    return dict(ev=ev, h=h, m=DP.shape[0],
                lamE=float(np.linalg.eigvalsh(G)[-1]))


def main():
    section("PRIME.PORT.DETXI.01 -- scaled edge spectrum + "
            "determinant sections (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; zero cache DIAGNOSTIC-ONLY (X2).")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (construction zero-free)",
          not ast_scan(BANNED_IDS))

    section("X1 -- the scaled edge spectrum u_i (heavy rungs)")
    res = {}
    for kz in HEAVY:
        r = dressed_port(kz)
        g = 1.0 - r["ev"]
        g = g[g > 0]
        u = g / g[0]
        res[kz] = dict(u=u[:10], g1=float(g[0]), h=r["h"],
                       m=r["m"])
        print("    kz %-3d h %4d m %3d  tau %.2e  u_1..u_8: %s"
              % (kz, r["h"], r["m"], g[0],
                 " ".join("%.2f" % v for v in u[:8])))
    dev = 0.0
    for a_ in range(len(DEEP3)):
        for b_ in range(a_ + 1, len(DEEP3)):
            ua = res[DEEP3[a_]]["u"][:5]
            ub = res[DEEP3[b_]]["u"][:5]
            k5 = min(len(ua), len(ub))
            dev = max(dev, float(np.max(
                np.abs(ua[:k5] - ub[:k5])
                / np.maximum(ub[:k5], 1e-30))))
    x1_type = ("LIMIT-SPECTRUM-STABLE" if dev <= 0.15
               else "SPECTRUM-DRIFTING")
    check("X1.1 typed: %s (pairwise max rel dev over kz %s, "
          "i <= 5: %.3f, bar 0.15)" % (x1_type, DEEP3, dev), True)

    section("X2 -- gamma tracking (DIAGNOSTIC-ONLY cache)")
    cache = json.load(open(os.path.join(
        _HERE, "zero_comb_cache_n2000.json")))
    gam = np.array([float(x) for x in cache["gammas"][:10]])
    u_deep = res[40]["u"]
    best = ("NO-TRACK", float("inf"))
    for p in (1, 2):
        r_i = (gam / gam[0]) ** p
        k5 = min(5, len(u_deep))
        md = float(np.max(np.abs(u_deep[:k5] - r_i[:k5])
                          / r_i[:k5]))
        print("    p = %d: (gamma_i/gamma_1)^p = %s vs u_i = %s "
              "-> max rel dev %.2f"
              % (p, " ".join("%.2f" % v for v in r_i[:5]),
                 " ".join("%.2f" % v for v in u_deep[:5]), md))
        if md < best[1]:
            best = (("TRACKS-GAMMA(p=%d)" % p) if md <= 0.15
                    else "NO-TRACK", md)
    check("X2.1 typed: %s (best max rel dev %.2f, bar 0.15; "
          "NO-TRACK kills only the naive two-parameter mapping)"
          % best, True)

    section("X3 -- determinant sections on the scaled window")
    curves = {}
    for kz in HEAVY:
        r = dressed_port(kz)
        g1 = 1.0 - float(np.max(r["ev"]))
        F = []
        for w in WGRID:
            z = 1.0 - w * g1
            F.append(float(np.sum(np.log(np.abs(z - r["ev"]))))
                     - r["m"] * math.log(abs(z)))
        curves[kz] = np.array(F)
    sups = []
    for a_, b_ in zip(HEAVY[:-1], HEAVY[1:]):
        sups.append(float(np.max(np.abs(curves[a_]
                                        - curves[b_]))))
    x3_type = ("DET-SECTION-CONVERGENT"
               if all(sups[i + 1] <= sups[i]
                      for i in range(len(sups) - 1))
               else "DET-SECTION-DRIFTING")
    print("    consecutive sup-differences of F_h: %s"
          % " -> ".join("%.3f" % s for s in sups))
    check("X3.1 typed: %s" % x3_type, True)

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
        ok_ctl &= (r["lamE"] > 1.0)
        print("    %-8s: lam(E) %.3e (edge crossed -- no truth-"
              "side scaled spectrum)" % (nmc, r["lamE"]))
    check("C1 CONTROLS FIRE: lam(E) > 1 on both", ok_ctl,
          kill="K2")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "DETXI-MEASURED"
    print("\n  VERDICT: %s (%s + %s + %s)"
          % (VERDICT, x1_type, best[0], x3_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
