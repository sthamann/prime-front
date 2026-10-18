#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wall_head_tail_bound_probe -- PRIME.PORT.HEADTAIL.BOUND.01
(EXPLORATION ONLY, experiments/; round 59, theorem-engineering on the
RH-side wall; probe 5, gated by wall_matched_asymptotics_probe =
H2D2-POSITIVE-STABLE(c0 = 4.954): split the arithmetic hub at n <=
NCUT into a FINITE EXPLICIT prime(-power) head and a tail, and
measure the tail-bound accuracy required to keep the wall margin
positive.  2026-08-10.)

THE SPLIT (frozen, exact).  On the lift-race surface (probe 4
verbatim: m_h = lam_min(K) = lift_h - demand_h exactly), the hub is
the explicit weighted sum lift = sum_n mu_n q_v(u_n) - smooth
integral (race S1.b identity, warded).  Cut at u_cut = log NCUT:
    head_err = sum_{n <= NCUT} mu_n q_v(u_n) - int_{u <= u_cut},
    tail_err = sum_{n >  NCUT} mu_n q_v(u_n) - int_{u >  u_cut},
    head_err + tail_err = lift          [SPLIT-EXACT, warded]
    m_h = G_head + tail_err,  G_head := head_err - demand_h.
G_head is the EXPLICITLY COMPUTABLE part (a finite sum over
prime powers n <= NCUT plus source integrals -- no unproved input);
tail_err is the deep error-term leg.  POSITIVITY BOOKKEEPING
(exact): m_h > 0 iff tail_err > -G_head.

WHAT IS MEASURED (frozen; typed, never kills):
 (a) HEAD COVERAGE: the sign ladder of G_head at NCUT = 100.
     HEAD-COVERS(n) iff G_head > 0 on n = ALL rungs (then a
     ONE-SIDED tail bound |tail_err| < G_head would close the wall
     at that rung from the explicit head alone); else
     HEAD-UNDERWATER(count G_head <= 0) (on those rungs positivity
     NEEDS a POSITIVE tail lower bound -- a much harder object).
 (b) NULL-TAIL TEST: does the trivial tail estimate (tail = 0, the
     PNT-null guess) suffice, i.e. |tail_err| < G_head?  Typed
     NULL-TAIL-SUFFICES(n/N) / NULL-TAIL-INSUFFICIENT(n/N).
 (c) REQUIRED ACCURACY: any tail estimate keeping the sign must be
     accurate to the margin itself: eps_abs = m_h; the ladder of
     the RELATIVE requirement rho_h = m_h / |tail_err| (how well
     the tail must be known relative to its own size), with the
     depth law: slope of log rho vs log h with jackknife 2SE.
     Typed TAILREQ(med-rho, slope +- 2SE).
 (d) CUT SENSITIVITY: the same at NCUT = 50 and 200 (printed
     ladder summary; head mass fraction per cut).

FROZEN PROTOCOL:

 W   THE LADDER + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): faithful ladder verbatim from probe 4 (kz 2..
     KZMAX, H_MIN <= h <= HCAP, X <= ATOM_MAX); W1 >= MIN_RUNGS =
     40; W2 WARD m_h > 0 everywhere; W3 WARD exact bookkeeping
     |(lift - demand) - m_h| <= ID_WARD; W4 WARD the race atom
     identity per rung: |sum_n mu_n q_v(u_n) - E_at(v)| relative <=
     ID_WARD and the PNT-grid version for E_at_smooth; W5 WARD
     SPLIT-EXACT |head_err + tail_err - lift| <= ID_WARD x scale
     for every cut.

 H   THE HEAD/TAIL LEDGER: full per-rung table at NCUT = 100
     (G_head, tail_err, m, rho); typed answers (a), (b), (c) as
     frozen above; cut-sensitivity summary (d).

 C   CONTROLS (kill -> WARD-BROKEN if silent): scramble (seed 1)
     at kz 9 on this surface: lam_min < 0 fires; Epstein x^2+5y^2
     comb at kz 9: lam_min < 0 fires.

KILLS: K1 ladder (W1) -> PIPELINE-BROKEN; K2 wards (W2-W5, C) ->
WARD-BROKEN.  All H-typed outcomes are measurements, never kills.

VERDICT (frozen enum): HEADTAIL-MEASURED with typed sublabels
SPLIT-EXACT(dev), HEAD-COVERS(n)/HEAD-UNDERWATER(n),
NULL-TAIL-SUFFICES(n/N)/NULL-TAIL-INSUFFICIENT(n/N),
TAILREQ(med-rho, slope +- 2SE); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; NCUT = 100 (primary);
CUTS = (50, 100, 200); ID_WARD = 1e-10; NG_SMOOTH = 6000; CTRL_KZ =
9; scramble seed 1; jackknife = full leave-one-out, CI = +- 2SE.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run of
this script (11/11 with the identical bars; NO bar, band, count,
rule or enum was moved after it) measured, recorded as the honest
context the frozen run must confirm: 67 rungs (h 142..1433); split
exact to 3.9e-13 (all three cuts), atom identity 1.9e-13,
bookkeeping 4.6e-15; at NCUT = 100 the head is UNDERWATER on 41 of
67 rungs (G_head <= 0: on those rungs the explicit n <= 100 part
does NOT cover the demand and positivity needs a POSITIVE lower
bound on the deep error-term tail -- the hard direction); the
null-tail estimate suffices on exactly the 26 covering rungs
(|tail_err| < G_head there -- those rungs close from the explicit
head alone; the other 41 do not); the required relative accuracy is
BRUTAL and TIGHTENS with depth: rho = m/|tail_err| med 2.5e-04,
range [9.7e-06, 1.2e-02], slope log rho vs log h = -2.316 +- 2SE
0.332 (R^2 0.786) -- the tail must be known to ~h^-2.3 relative
accuracy because |tail_err| stays O(1)-ish (med 0.178) while m med
2.9e-05; tail sign 41+/26-; cut sensitivity: G_head > 0 on 52/67
(NCUT 50), 26/67 (NCUT 100), 25/67 (NCUT 200) with head/lift med
1.128 / 0.949 / 0.938 -- the SMALLER n <= 50 head covers MORE rungs
because the head OVERSHOOTS the full lift on median at that cut
(the deeper atoms are a net-negative correction there).
Fail-first preserved: nothing was weakened; all typed outcomes are
measurements over exact-warded decompositions.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
machinery verbatim from wall_matched_asymptotics_probe (q_read,
smooth_comb, jackknife, OLS); (ii) the cut acts on u: atoms u_n <=
log NCUT, smooth grid ug <= log NCUT (same functional, same cut);
(iii) rho ladder uses |tail_err| with sign counts printed.

NO-GO COMPLIANCE (frozen): no certified-bound retry, no rank-1
approximation, no Herglotz; no fit where an identity is claimed
(the split and bookkeeping are exact wards; the depth law is a
typed trend with jackknife error bars).

NO RH claim: the head/tail ledger quantifies what a tail theorem
would need to deliver on this deployed family; it does not provide
such a theorem, and G_head > 0 on a subset proves nothing beyond
those rungs.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids zetazero
/ nzeros / primerange / isprime / primepi / nextprime / prevprime;
the n <= NCUT head reads the DEPLOYED window atoms, not a prime
oracle); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; lift-race machinery
verbatim from arithmetic_lift_race_probe.py via
wall_matched_asymptotics_probe.py; probe-4 gate
H2D2-POSITIVE-STABLE (declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wall_head_tail_bound_probe.py
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

KZMAX = 150
MIN_RUNGS = 40
NCUT = 100
CUTS = (50, 100, 200)
ID_WARD = 1e-10
NG_SMOOTH = 6000
CTRL_KZ = 9
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


def ols_line(x, y):
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


def jack_slope(x, y):
    """Leave-one-out jackknife SE of the OLS slope."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        bb.append(ols_line(x[m], y[m])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                              ** 2)))
    return b, se, r2


def q_read(W, u, D, M):
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


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


def main():
    section("PRIME.PORT.HEADTAIL.BOUND.01 -- the explicit n <= %d "
            "head vs the tail-bound requirement (EXPLORATION ONLY)"
            % NCUT)
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    GATE (declared): probe 4 = H2D2-POSITIVE-STABLE.")
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder (race surface) + wards")
    rungs = []
    dev_at = 0.0
    dev_sp = 0.0
    for kz in range(2, KZMAX + 1):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
        uu = np.asarray(rr["uu"], float)
        mu = 2.0 * np.asarray(rr["lam"], float)
        c_at = core.atom_lags_at(alpha, M, uu, mu)[0]
        c_ar = np.asarray(core.arch_lags(M, D), float)
        w, V = np.linalg.eigh(core.odd_toeplitz(c_ar + c_at, M))
        v = V[:, 0]
        ug, mg = smooth_comb(alpha)
        c_sm = core.atom_lags_at(alpha, M, ug, mg)[0]
        Wv = core.lag_weights_from_v(v, h)
        e_ar = float(np.asarray(c_ar) @ Wv)
        e_t = float(np.asarray(c_at) @ Wv)
        e_s = float(np.asarray(c_sm) @ Wv)
        qa = mu * q_read(Wv, uu, D, M)
        qg = mg * q_read(Wv, ug, D, M)
        dev_at = max(dev_at,
                     abs(float(qa.sum()) - e_t)
                     / max(abs(e_t), 1e-30),
                     abs(float(qg.sum()) - e_s)
                     / max(abs(e_s), 1e-30))
        lift = e_t - e_s
        demand = -(e_ar + e_s)
        row = dict(kz=kz, alpha=float(alpha), h=h, m=float(w[0]),
                   lift=lift, demand=demand, split={})
        for nc in CUTS:
            ucut = math.log(nc)
            he = (float(qa[uu <= ucut].sum())
                  - float(qg[ug <= ucut].sum()))
            te = (float(qa[uu > ucut].sum())
                  - float(qg[ug > ucut].sum()))
            dev_sp = max(dev_sp, abs((he + te) - lift)
                         / max(abs(lift), 1e-30))
            row["split"][nc] = (he, te)
        rungs.append(row)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    check("W2 WARD truth margin m_h > 0 on every rung (min %.3e)"
          % min(r["m"] for r in rungs),
          all(r["m"] > 0 for r in rungs), kill="K2")
    dev_bk = max(abs((r["lift"] - r["demand"]) - r["m"])
                 / max(1.0, abs(r["m"])) for r in rungs)
    check("W3 WARD exact bookkeeping lift - demand = m_h: max dev "
          "%.2e <= %.0e" % (dev_bk, ID_WARD), dev_bk <= ID_WARD,
          kill="K2")
    check("W4 WARD race atom identity (sum mu q = E_at; PNT grid = "
          "E_smooth): max rel dev %.2e <= %.0e" % (dev_at, ID_WARD),
          dev_at <= ID_WARD, kill="K2")
    check("W5 WARD SPLIT-EXACT head_err + tail_err = lift on all "
          "rungs x %d cuts: max rel dev %.2e <= %.0e"
          % (len(CUTS), dev_sp, ID_WARD), dev_sp <= ID_WARD,
          kill="K2")

    # ------------------------------------------------------------ H
    section("H -- the head/tail ledger at NCUT = %d" % NCUT)
    print("    kz   h    alpha   m_h        G_head     tail_err   "
          "|tail|/m    rho=m/|tail|")
    Gh, Te, Ms, Hs = [], [], [], []
    for r in rungs:
        he, te = r["split"][NCUT]
        g = he - r["demand"]
        Gh.append(g)
        Te.append(te)
        Ms.append(r["m"])
        Hs.append(float(r["h"]))
        print("    %-4d %-4d %6.3f  %.3e  %+.3e %+.3e  %.3e  "
              "%.3e"
              % (r["kz"], r["h"], r["alpha"], r["m"], g, te,
                 abs(te) / r["m"], r["m"] / max(abs(te), 1e-300)),
              flush=True)
    Gh = np.array(Gh)
    Te = np.array(Te)
    Ms = np.array(Ms)
    Hs = np.array(Hs)
    n_under = int(np.sum(Gh <= 0.0))
    if n_under == 0:
        ha = "HEAD-COVERS(%d/%d)" % (len(Gh), len(Gh))
    else:
        ha = "HEAD-UNDERWATER(%d/%d)" % (n_under, len(Gh))
    check("H1 typed (a): %s (G_head = explicit n <= %d head - "
          "demand; underwater rungs need a POSITIVE tail lower "
          "bound)" % (ha, NCUT), True)
    n_null = int(np.sum(np.abs(Te) < Gh))
    hb = ("NULL-TAIL-SUFFICES(%d/%d)" % (n_null, len(Gh))
          if n_null == len(Gh)
          else "NULL-TAIL-INSUFFICIENT(%d/%d)" % (n_null, len(Gh)))
    check("H2 typed (b): %s (|tail_err| < G_head would close the "
          "rung from the explicit head + a null tail estimate)"
          % hb, True)
    rho = Ms / np.maximum(np.abs(Te), 1e-300)
    sl_r, se_r, r2_r = jack_slope(np.log(Hs), np.log(rho))
    print("\n    required relative tail accuracy rho = m/|tail|: "
          "med %.2e, range [%.2e, %.2e]; depth law slope log rho "
          "vs log h = %+.3f +- 2SE %.3f (R^2 %.3f); |tail| med "
          "%.3f vs m med %.2e; tail sign %d+/%d-"
          % (float(np.median(rho)), float(np.min(rho)),
             float(np.max(rho)), sl_r, 2 * se_r, r2_r,
             float(np.median(np.abs(Te))), float(np.median(Ms)),
             int(np.sum(Te > 0)), int(np.sum(Te < 0))))
    hc = "TAILREQ(med-rho=%.1e, slope=%+.2f+-%.2f)" % (
        float(np.median(rho)), sl_r, 2 * se_r)
    check("H3 typed (c): %s (eps_abs = m_h itself; rho is the "
          "relative version)" % hc, True)
    print("\n    cut sensitivity:")
    for nc in CUTS:
        g_nc = np.array([r["split"][nc][0] - r["demand"]
                         for r in rungs])
        frac = np.array([r["split"][nc][0]
                         / r["lift"] if r["lift"] != 0 else
                         float("nan") for r in rungs])
        print("      NCUT %-4d: G_head > 0 on %d/%d; head/lift "
              "med %.3f (range [%.2f, %.2f])"
              % (nc, int(np.sum(g_nc > 0)), len(g_nc),
                 float(np.nanmedian(frac)),
                 float(np.nanmin(frac)), float(np.nanmax(frac))))
    check("H4 typed (d): cut-sensitivity ledger printed (no "
          "typing; NCUT = %d is the frozen primary)" % NCUT, True)

    # ------------------------------------------------------------ C
    section("C -- controls on this surface at kz %d" % CTRL_KZ)
    rr = core.build_window(CTRL_KZ)
    alpha, M = rr["alpha"], rr["M"]
    c_ar9 = np.asarray(core.arch_lags(M, rr["D"]), float)
    N_E = int(math.floor(math.exp(2.0 * alpha))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    c_E = core.atom_lags_at(alpha, M, np.log(nn.astype(float)),
                            2.0 * lamE_[nn]
                            / np.sqrt(nn.astype(float)))[0]
    lamE = float(np.linalg.eigvalsh(
        core.odd_toeplitz(c_ar9 + np.asarray(c_E, float), M))[0])
    rr_s = core.build_window(CTRL_KZ, scramble_seed=1)
    c_s = core.atom_lags_at(
        rr_s["alpha"], rr_s["M"],
        np.asarray(rr_s["uu"], float),
        2.0 * np.asarray(rr_s["lam"], float))[0]
    lamS = float(np.linalg.eigvalsh(core.odd_toeplitz(
        np.asarray(core.arch_lags(rr_s["M"], rr_s["D"]), float)
        + np.asarray(c_s, float), rr_s["M"]))[0])
    print("    Epstein  : lam_min %+.3e -> %s"
          % (lamE, "FIRES" if lamE < 0 else "SILENT"))
    print("    scramble : lam_min %+.3e -> %s"
          % (lamS, "FIRES" if lamS < 0 else "SILENT"))
    check("C1 WARD both controls fire (lam_min < 0)",
          lamE < 0 and lamS < 0, kill="K2")

    return finish(dict(dev=dev_sp, ha=ha, hb=hb, hc=hc))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("HEADTAIL-MEASURED / SPLIT-EXACT(%(dev).1e) / "
                   "%(ha)s / %(hb)s / %(hc)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the ledger quantifies what a tail
  theorem would need to deliver on this deployed family -- it does
  not deliver one.  A HEAD-UNDERWATER rung needs a positive lower
  bound on an error-term tail (the hard direction); a NULL-TAIL-
  INSUFFICIENT ledger means the explicit head alone cannot close
  any rung without a tail estimate accurate to the margin itself.
  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
