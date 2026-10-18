#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_mellin_cauchy_probe -- PRIME.PORT.MELLIN.01
(EXPLORATION ONLY, experiments/; round 39 task 2 of the 2026-08-09
external review: the explicit Mellin-Cauchy limit kernel of the
port source, FIT-FREE, 2026-08-09).

THE FROZEN CANDIDATES (derived from the sqrt uniformization, no
free scale): with r = sqrt(n/X) and eta_X => dr,
  (i)  G_X(tau) := (1/(4 sqrt X)) sum_n mu_n r_n^{2 i tau}
       ->  1/(1 + 2 i tau)     (the pure Cauchy kernel);
  (ii) the DEPLOYED port numerator is predicted WITHOUT FIT by the
       continuum integral of the exact deployed window weight
       against dr:
         pred_j = -4 sqrt X * int_0^1 w_j(U + 2 log r) dr,
       w_j = the exact tent/cosine transform weight of LXXXVII
       (incl. the edge taper); the deviation of the measured
       d_at(theta_j) from pred_j is the ARITHMETIC FLUCTUATION
       share -- expected to shrink with depth;
  (iii) the taper decomposition (report): pred with full taper vs
       untapered pure-kernel prediction -- the review's conjecture
       is that the taper correction is the 1/(1+2iz)^2 derivative
       kernel (the Mellin shadow of the linear tent).

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run):

 M1  PURE KERNEL (own SPF sieve, X in {1e4, 1e5, 1e6, 1e7}, tau
     grid {0.25, 0.5, 1, 2, 4, 8}): max_tau |G_X - 1/(1+2i tau)|
     DECREASING along the X-ladder with final <= 0.02.

 M2  DEPLOYED PORT PREDICTION (heavy rungs kz {9, 12, 13, 26,
     40}, port modes j = 1..8): rel deviation |d_at(theta_j) -
     pred_j| / |pred_j|; typed MELLIN-SOURCE-CONFIRMED iff the
     j <= 5 max deviation at the DEEPEST rung is <= 0.10 AND the
     rung-max deviations decrease from the shallowest to the
     deepest rung, else MELLIN-SOURCE-PARTIAL (values printed --
     the deviation IS the arithmetic fluctuation, not noise).

 M3  TAPER DECOMPOSITION (report): per rung the split pred_full
     vs pred_untapered (pure kernel, no edge taper): the taper
     share printed; the review's derivative-kernel reading typed
     qualitatively (does the taper correction scale like the
     second Cauchy power at the port frequencies?).

 C   CONTROLS (kz 9, must fire): the SAME continuum prediction
     against the scramble comb must break (its measure is
     log-uniform, not dr): rel deviation >= 3x the truth value
     at the same rung.

KILLS: K1 sieve/pipeline breaks -> PIPELINE-BROKEN; K2 M1 fails
(the pure kernel is wrong) -> KERNEL-BROKEN; K3 control does not
fire -> CONTROL-DEAD.  M2/M3 typed.

VERDICT (frozen enum): MELLIN-KERNEL-CONFIRMED (+ typed M2
sublabel) / PIPELINE-BROKEN / KERNEL-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: own sieve, no banned oracles (AST scan);
v563 READ-ONLY; RNG only in the declared scramble control; writes
nothing but stdout.  No marker moves.

Sources (read-only): v563_paper2_readouts (atom tables, tent
assembly conventions read verbatim in LXXXVII);
prime_sqrt_uniformization_probe (round 39 task 1, declared
input); port_atom_numerator_probe (the exact windowed weight).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_mellin_cauchy_probe.py
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
XLADDER = (10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7)
TGRID = (0.25, 0.5, 1.0, 2.0, 4.0, 8.0)
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


def mangoldt_up_to(N):
    spf = np.zeros(N + 1, dtype=np.int64)
    for p in range(2, int(math.isqrt(N)) + 1):
        if spf[p] == 0:
            spf[p * p::p] = np.where(spf[p * p::p] == 0, p,
                                     spf[p * p::p])
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        p = spf[n] if spf[n] else n
        m = n
        while m % p == 0:
            m //= p
        lam[n] = math.log(p) if m == 1 else 0.0
    return lam


def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def build_rung(kz, scramble_seed=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d_at = grid_density(np.asarray(c_at, float))
    return dict(d_at=d_at, M=M, D=D, L=2 * M - 2, alpha=alpha,
                uu=uu, mm=mm)


def w_exact(u_arr, M, D, L, j):
    """The exact deployed transform weight per unit mass at
    positions u (LXXXVII convention): 0.5 * sum_i tent_i(u) w_i
    cos(i theta_j)."""
    th = 2.0 * math.pi * j / L
    i0 = np.floor(u_arr / D).astype(int)
    f = u_arr / D - i0

    def w_of(i):
        return np.where((i == 0) | (i == M - 1), 1.0, 2.0)

    tot = np.zeros(len(u_arr))
    for i_at, v_at in ((i0, 1.0 - f), (i0 + 1, f)):
        ok = (i_at >= 0) & (i_at <= M - 1) & (v_at > 0.0)
        tot += np.where(ok, v_at * w_of(i_at)
                        * np.cos(i_at * th), 0.0)
    return 0.5 * tot


def pred_port(b, j, taper=True):
    """Continuum prediction: -4 sqrt(X) int_0^1 w_j(u(r)) dr."""
    U = float(np.max(b["uu"]))
    rg = np.linspace(1e-6, 1.0, 20000)
    ug = U + 2.0 * np.log(rg)
    keep = ug >= 0.0
    if taper:
        w = w_exact(ug[keep], b["M"], b["D"], b["L"], j)
    else:
        tau_j = (2.0 * math.pi * j / b["L"]) / b["D"]
        w = np.cos(tau_j * ug[keep])
    return -4.0 * math.exp(U / 2.0) * float(
        np.trapezoid(w, rg[keep]))


def main():
    section("PRIME.PORT.MELLIN.01 -- the Mellin-Cauchy limit "
            "kernel of the port source (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; fit-free; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (own sieve, no oracles)",
          not ast_scan(BANNED_IDS))

    section("M1 -- the pure Cauchy kernel (own sieve)")
    lam = mangoldt_up_to(XLADDER[-1])
    nn_all = np.arange(2, XLADDER[-1] + 1)
    mu_all = 2.0 * lam[2:] / np.sqrt(nn_all)
    devs = []
    for X in XLADDER:
        m = nn_all <= X
        r = np.sqrt(nn_all[m] / X)
        mu = mu_all[m]
        dev = 0.0
        for t in TGRID:
            G = np.sum(mu * r ** (2j * t)) / (4.0 * math.sqrt(X))
            K = 1.0 / (1.0 + 2j * t)
            dev = max(dev, abs(G - K))
        devs.append(dev)
        print("    X = %.0e: max_tau |G_X - 1/(1+2i tau)| = %.4f"
              % (X, dev))
    check("M1.1 PURE KERNEL: deviations decreasing (%.4f -> "
          "%.4f), final <= 0.02 -- the port source Mellin limit "
          "IS the Cauchy kernel"
          % (devs[0], devs[-1]),
          all(devs[i + 1] < devs[i] for i in range(len(devs) - 1))
          and devs[-1] <= 0.02, kill="K2")

    section("M2/M3 -- the deployed port prediction (fit-free)")
    rung_devs = {}
    for kz in HEAVY:
        b = build_rung(kz)
        dv = []
        taper_share = []
        for j in range(1, 9):
            act = float(b["d_at"][j])
            pf = pred_port(b, j, taper=True)
            pu = pred_port(b, j, taper=False)
            dv.append(abs(act - pf) / max(abs(pf), 1e-30))
            taper_share.append(abs(pf - pu)
                               / max(abs(pu), 1e-30))
        rung_devs[kz] = dv
        print("    kz %-3d rel dev (j=1..8): %s | taper share: %s"
              % (kz, " ".join("%.3f" % v for v in dv),
                 " ".join("%.2f" % v for v in taper_share)))
    max5 = {kz: max(rung_devs[kz][:5]) for kz in HEAVY}
    m2_type = ("MELLIN-SOURCE-CONFIRMED"
               if max5[40] <= 0.10 and max5[9] > max5[40]
               else "MELLIN-SOURCE-PARTIAL")
    check("M2.1 typed: %s (j<=5 max dev: kz9 %.3f -> kz40 %.3f; "
          "bar 0.10 at the deepest) -- the deviation IS the "
          "arithmetic fluctuation around the universal kernel"
          % (m2_type, max5[9], max5[40]), True)
    check("M3.1 taper decomposition recorded (report; the "
          "derivative-kernel reading of the tent taper stays a "
          "named conjecture)", True)

    section("C -- controls (kz 9)")
    b_s = build_rung(9, scramble_seed=1)
    dv_s = []
    for j in range(1, 6):
        act = float(b_s["d_at"][j])
        pf = pred_port(b_s, j, taper=True)
        dv_s.append(abs(act - pf) / max(abs(pf), 1e-30))
    ratio = max(dv_s) / max(rung_devs[9][:5])
    check("C1 SCRAMBLE FIRES: continuum-dr prediction breaks on "
          "the log-uniform comb (max dev %.3f = %.1fx truth)"
          % (max(dv_s), ratio), ratio >= 3.0, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN", "K2": "KERNEL-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "MELLIN-KERNEL-CONFIRMED"
    print("\n  VERDICT: %s (%s)" % (VERDICT, m2_type))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
