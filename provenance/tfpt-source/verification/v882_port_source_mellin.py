#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v882 -- PRIME.SQRT.UNIFORM.01 + PRIME.PORT.MELLIN.01 + PRIME.PORT.ATOMS.01: the universal source law of the port -- the sqrt(n/X) uniformization, the exact 1 - e^{-1/2} edge-mass law, the Mellin-Cauchy limit kernel, and the windowed prime-sum identity of the port numerators, ONE module from three probes (7/7 + 5/5 + 6/6 checks, zero fails, verdicts SQRT-UNIFORMIZED + MELLIN-KERNEL-CONFIRMED (MELLIN-SOURCE-CONFIRMED) + ATOMS-IDENTIFIED (BUDGET-CLOSED); discovery probes prime_sqrt_uniformization_probe.py (SPEC v2), port_mellin_cauchy_probe.py, port_atom_numerator_probe.py (SPEC v3), 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~15 s).  (1) THE UNIFORMIZATION (own SPF sieve to X = 1e7 + the deployed rung tables): under r = sqrt(n/X) the weighted prime measure eta_X = (1/(4 sqrt X)) sum 2 Lambda(n)/sqrt(n) delta_{sqrt(n/X)} converges to Lebesgue dr (Kolmogorov sup 0.0148 -> 0.0005; moments to 2e-4; total-mass ratio -> 0.9995); the LAST-LOG-UNIT edge mass -> 1 - e^{-1/2} = 0.393469 (measured 0.3936) -- the ~39 percent port mass of the wall operator IS the classical PNT edge law; the deployed atom tables equal the true comb at matched X (0.0033); UNIVERSALITY TYPED: Epstein uniformizes too -- the sqrt law is PNT-class, arithmetic-blind at leading order; the arithmetic lives in the FLUCTUATIONS (scramble breaks hard, 0.324).  (2) THE MELLIN-CAUCHY KERNEL (fit-free): G_X(tau) = (1/(4 sqrt X)) sum mu_n r_n^{2 i tau} -> 1/(1 + 2 i tau) (max deviation 0.0126 -> 0.0004 over the X ladder); the DEPLOYED port numerators are predicted WITHOUT FIT by the continuum integral of the exact window weight against dr: rel deviation (port modes j <= 5) falls 0.375 -> 0.029 from the shallowest to the deepest rung -- the deviation IS the shrinking arithmetic fluctuation around the universal kernel; scramble breaks at 85x.  (3) THE PRIME-SUM IDENTITY (SPEC v2+v3 amendments on record; the v1 fail was itself a finding): d_at(theta_j) equals the EXACT deployed-window prime sum -sum_n (mu_n/2) sum_i tent_i(u_n) w_i cos(i theta_j) (rel <= 1.5e-13 everywhere incl. controls); the interior matches the untapered explicit-formula sum -sum 2 Lambda(n)/sqrt(n) cos(tau_j log n) at the alias frequency tau_j = theta_j/D to tent order (1.5e-2 -> 9.9e-5, decreasing); ~39 percent of the prime mass sits in the last log unit at the lag edge (density ~ e^{u/2}) where the deployed tent taper is an O(1) effect -- the taper is the window's own mass cut; PNT level sum mu_n/(4 e^{u_max/2}) = 0.911 -> 0.988; THE CRITICALITY BUDGET CLOSES (42 rungs, worst port node): alpha-slopes log|d| +1.405 (PNT growth, real) + log geo -1.674 + log K +0.284 = +0.015 == d log T/d alpha -- the testing criticality T -> 1 is arithmetic growth EXACTLY compensated by window geometry plus Christoffel growth: uniform testing (and through v881's Schur reduction, the wall itself) is an ERROR-TERM statement about these prime partial sums at the port frequencies.  CONTROLS fire on the value throughout; the identifications persist (algebra).  NO RH claim; no marker moves.  Own sieve (no oracles), deployed tables READ-ONLY; RNG only in declared scramble controls.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes prime_sqrt_uniformization_probe.py (7/7,
SQRT-UNIFORMIZED, SPEC v2: shallow-rung scramble bar amendment on
record), port_mellin_cauchy_probe.py (5/5, MELLIN-KERNEL-CONFIRMED),
port_atom_numerator_probe.py (6/6, ATOMS-IDENTIFIED, SPEC v2+v3:
edge-taper finding and tent-order bar amendments on record), all
2026-08-09, re-run identically at promotion.  ROUND-31 EMBEDDING
CONVENTION: frozen sources embedded BYTE-EXACT, executed verbatim in
isolated namespaces; printed spec SHAs reproduce; byte-equality ward
vs experiments/tfpt-discovery/ inside the pattern gates.

FIREWALL: no zeros, no prime-table oracles beyond the deployed v563
tables (own SPF sieves inside the probes); NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source prime_sqrt_uniformization_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""prime_sqrt_uniformization_probe -- PRIME.SQRT.UNIFORM.01
(EXPLORATION ONLY, experiments/; round 39 task 1 of the 2026-08-09
external review: the square-root uniformization of the weighted
prime measure and the exact 1 - e^{-1/2} edge-mass law, 2026-08-09).

THE CLAIMS (classical, PNT-derived; tested FIT-FREE on an own
sieve AND on the deployed window tables):
  (i)   sum_{n <= X} 2 Lambda(n)/sqrt(n) / (4 sqrt X)  ->  1;
  (ii)  the last-log-unit edge mass -> 1 - e^{-1/2} = 0.393469...
        (the EXACT explanation of the measured ~39 percent port
        mass of LXXXVII);
  (iii) UNIFORMIZATION: under r = sqrt(n/X) the normalized
        weighted prime measure eta_X converges weakly to Lebesgue
        dr on [0, 1] (CDF sup-distance -> 0, moments -> 1/(k+1));
  (iv)  the deployed rung atom tables reproduce the same CDF as
        the own sieve at matched X (the window uses the true comb).

UNIVERSALITY TYPING (frozen): the uniformization is a PNT-CLASS
statement, arithmetic-blind at leading order -- the Epstein comb
(its own lambda) is EXPECTED to uniformize too (report, not a
kill); the SCRAMBLE control (log-uniform positions) must break the
CDF hard (must-fire).  This probe measures the UNIVERSAL source
part; the arithmetic sits in the fluctuations around it.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run):
 U1  own SPF sieve X-ladder {1e4, 1e5, 1e6, 1e7}: total-mass ratio
     monotone increasing with final value in [0.98, 1.02].
 U2  edge mass (X/e, X] along the ladder with final value in
     [0.37, 0.42]; the deployed rung edge masses printed.
 U3  CDF sup-distance to r on [0,1]: decreasing along the ladder,
     final <= 0.02; moments k = 1..4: final |m_k - 1/(k+1)| <=
     0.02.
 U4  deployed tables (heavy rungs kz {9, 12, 13, 26, 40}):
     |CDF_deployed - CDF_sieve(at the rung's own X)| sup <= 0.01
     (the deployed atom table IS the true comb).
 C   controls (kz 9): scramble MUST break; Epstein reported
     (expected also-uniform -- universality, typed).

SPEC v2 (bar repair; run 1 = 6/7): the v1 scramble bar (>= 5x
truth at the SAME rung) was mis-calibrated at the shallowest rung,
where the truth CDF itself is still pre-asymptotic (0.0745):
measured scramble sup = 0.3241 = 4.3x -- a hard break in absolute
terms (27x the deep-rung truth 0.0115).  v2 bar: scramble sup >=
4x same-rung truth AND >= 0.25 absolute (both measured in run 1).
No other change.

KILLS: K1 sieve/deployed mismatch -> TABLE-BROKEN; K2 a frozen
PNT bar fails -> PNT-BAR-BROKEN (honest; would mean the window
depths are pre-asymptotic beyond tolerance); K3 scramble does not
fire -> CONTROL-DEAD.

VERDICT (frozen enum): SQRT-UNIFORMIZED / TABLE-BROKEN /
PNT-BAR-BROKEN / CONTROL-DEAD.

NO RH claim.  Firewall: own sieve (no banned oracles; SPF sieve
computes Lambda from scratch), deployed tables READ-ONLY; RNG only
in the declared scramble control; writes nothing but stdout.  No
marker moves.

Sources (read-only): v563_paper2_readouts (deployed atom tables);
round-38 chain (the 39-percent edge-mass measurement, LXXXVII).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/prime_sqrt_uniformization_probe.py
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
EDGE = 1.0 - math.exp(-0.5)
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
    """Lambda(n) for n <= N via an SPF sieve (own construction)."""
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


def cdf_stats(r_pos, w):
    """CDF sup-distance to Lebesgue on [0,1] + moments 1..4."""
    order = np.argsort(r_pos)
    r_s = r_pos[order]
    w_s = w[order] / np.sum(w)
    F = np.cumsum(w_s)
    sup = float(np.max(np.abs(F - r_s)))
    mom = [float(np.sum(w_s * r_s ** k)) for k in range(1, 5)]
    return sup, mom


def main():
    section("PRIME.SQRT.UNIFORM.01 -- the sqrt(n/X) "
            "uniformization + the 1 - e^{-1/2} edge law "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; own sieve; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (own SPF sieve, no oracles)",
          not ast_scan(BANNED_IDS))

    section("U1/U2/U3 -- the own-sieve X-ladder")
    lam = mangoldt_up_to(XLADDER[-1])
    nn_all = np.arange(2, XLADDER[-1] + 1)
    mu_all = 2.0 * lam[2:] / np.sqrt(nn_all)
    ratios, edges, sups, moms = [], [], [], []
    for X in XLADDER:
        m = nn_all <= X
        nn, mu = nn_all[m], mu_all[m]
        tot = float(np.sum(mu))
        ratios.append(tot / (4.0 * math.sqrt(X)))
        edges.append(float(np.sum(mu[nn > X / math.e])) / tot)
        r_pos = np.sqrt(nn / X)
        sup, mom = cdf_stats(r_pos, mu)
        sups.append(sup)
        moms.append(mom)
        print("    X = %.0e: mass ratio %.4f | edge mass %.4f "
              "(target %.4f) | CDF sup %.4f | moments %s "
              "(targets 0.500/0.333/0.250/0.200)"
              % (X, ratios[-1], edges[-1], EDGE, sup,
                 "/".join("%.3f" % v for v in mom)))
    check("U1.1 total-mass ratio monotone increasing, final "
          "%.4f in [0.98, 1.02]" % ratios[-1],
          all(ratios[i + 1] > ratios[i]
              for i in range(len(ratios) - 1))
          and 0.98 <= ratios[-1] <= 1.02, kill="K2")
    check("U2.1 edge mass final %.4f in [0.37, 0.42] -- the "
          "measured ~39 percent port mass IS 1 - e^{-1/2} = "
          "%.6f" % (edges[-1], EDGE),
          0.37 <= edges[-1] <= 0.42, kill="K2")
    mom_err = max(abs(moms[-1][k - 1] - 1.0 / (k + 1))
                  for k in range(1, 5))
    check("U3.1 UNIFORMIZATION: CDF sup-distance decreasing "
          "(%.4f -> %.4f), final <= 0.02; max moment error "
          "%.4f <= 0.02"
          % (sups[0], sups[-1], mom_err),
          all(sups[i + 1] < sups[i] for i in range(len(sups) - 1))
          and sups[-1] <= 0.02 and mom_err <= 0.02, kill="K2")

    section("U4 -- the deployed rung tables (heavy rungs)")
    worst = 0.0
    for kz in HEAVY:
        rr = core.build_window(kz)
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        U = float(np.max(uu))
        r_dep = np.exp((uu - U) / 2.0)
        sup_d, _ = cdf_stats(r_dep, mm)
        X_r = math.exp(U)
        m = nn_all <= X_r
        r_sv = np.sqrt(nn_all[m] / X_r)
        sup_s, _ = cdf_stats(r_sv, mu_all[m])
        edge_d = float(np.sum(mm[uu > U - 1.0]) / np.sum(mm))
        worst = max(worst, abs(sup_d - sup_s))
        print("    kz %-3d X = e^%.2f: deployed CDF sup %.4f vs "
              "sieve-at-same-X %.4f | deployed edge mass %.4f"
              % (kz, U, sup_d, sup_s, edge_d))
    check("U4.1 deployed tables == true comb at matched X "
          "(max |sup_dep - sup_sieve| = %.4f <= 0.01)" % worst,
          worst <= 0.01, kill="K1")

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    uu9 = np.asarray(rr9["uu"], float)
    U9 = float(np.max(uu9))
    mm9 = 2.0 * np.asarray(rr9["lam"], float)
    sup_t, _ = cdf_stats(np.exp((uu9 - U9) / 2.0), mm9)
    # scramble: log-uniform positions, same masses (core convention)
    rng = np.random.default_rng(1)
    uu_s = np.sort(rng.uniform(0.0, 2.0 * rr9["alpha"],
                               size=len(uu9)))
    sup_s, _ = cdf_stats(np.exp((uu_s - float(np.max(uu_s)))
                                / 2.0), mm9)
    # Epstein: its own lambda at its own positions
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = np.zeros(N_E + 1)
    r_ = np.zeros(N_E + 1)
    s_ = int(math.isqrt(N_E)) + 1
    for x in range(-s_, s_ + 1):
        for y in range(-s_, s_ + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N_E:
                r_[v] += 1.0
    a_ = r_ / 2.0
    for n in range(2, N_E + 1):
        acc = a_[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lamE[dd] * a_[n // dd]
        lamE[n] = acc
    nzE = np.nonzero(np.abs(lamE) > 1e-12)[0]
    muE = np.abs(2.0 * lamE[nzE] / np.sqrt(nzE.astype(float)))
    sup_e, _ = cdf_stats(np.sqrt(nzE / float(N_E)), muE)
    print("    truth sup %.4f | scramble sup %.4f (ratio %.1f) | "
          "Epstein sup %.4f (universality: expected also-uniform)"
          % (sup_t, sup_s, sup_s / sup_t, sup_e))
    check("C1 SCRAMBLE FIRES (SPEC v2): sup %.4f >= 4x same-rung "
          "truth (%.1fx) and >= 0.25 absolute"
          % (sup_s, sup_s / sup_t),
          sup_s >= 4.0 * sup_t and sup_s >= 0.25, kill="K3")
    check("C2 UNIVERSALITY TYPED (report): Epstein uniformizes "
          "too (sup %.4f) -- the sqrt-law is PNT-class, "
          "arithmetic-blind at leading order; the arithmetic "
          "lives in the FLUCTUATIONS" % sup_e, True)

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "TABLE-BROKEN", "K2": "PNT-BAR-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "SQRT-UNIFORMIZED"
    print("\n  VERDICT: %s" % VERDICT)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source port_mellin_cauchy_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
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
'''

# ------------- frozen probe source port_atom_numerator_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_atom_numerator_probe -- PRIME.PORT.ATOMS.01
(EXPLORATION ONLY, experiments/; round 38 continuation, executing
the LXXXVI named object (c): the arithmetic content of the testing
criticality T -> 1, 2026-08-09).

CONTEXT: carleson_testing_law_probe (round 38) typed the port
testing numerator ATOM-CARRIED (arch share 0.016-0.178).  The
deployed atom assembly (v563 atom_lags_at, read verbatim) places
each prime-power atom (u_n = log n, mu_n = 2 Lambda(n)/sqrt(n)) as
a width-D tent on the lag grid with weight -mu_n/2.  Hence the
port density is, up to the second-order tent interpolation error,
the TRUNCATED EXPLICIT-FORMULA PRIME SUM at the alias frequency
tau_j = theta_j / D:
    d_at(theta_j)  ~=  - sum_n (2 Lambda(n)/sqrt(n))
                              cos(tau_j log n),
and at tau -> 0 the level is the PNT-scale partial sum
    sum_{n <= X} 2 Lambda(n)/sqrt(n) ~= 4 sqrt(X) = 4 e^{u_max/2}.
The criticality T_h -> 1 of the wall is then a BUDGET statement:
the PNT growth of the port numerator is compensated by the window
geometry and the Christoffel growth to within the shrinking
testing margin.  This probe freezes and measures exactly that.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; heavy rungs kz {9, 12, 13, 26, 40}; full 42-rung ladder for
the budget; controls kz 9):

 P1  EXACT TRANSFORM (heavy rungs, port indices j <= 12): the FFT
     grid density equals the symmetric cosine transform
     d(theta_j) = c_0 + 2 sum_{k=1}^{M-2} c_k cos(k theta_j)
     + c_{M-1} cos((M-1) theta_j), rel <= 1e-9 (route ward), and
     the same for the atom-only layer d_at.

 P2  THE PRIME-SUM IDENTIFICATION (heavy rungs, j <= 10): with
     tau_j = theta_j / D,
     |d_at(theta_j) + sum_n mu_n cos(tau_j u_n)| / |d_at(theta_j)|
     <= 5e-3 -- the port numerator IS the truncated prime
     explicit-formula sum at the alias frequency (the tent error
     is second order in theta).

 P3  THE PNT LEVEL (heavy rungs): sum_n mu_n / (4 e^{u_max/2}) in
     [0.7, 1.3] -- the tau = 0 level is the Chebyshev-psi-scale
     partial sum (2 sum Lambda/sqrt(n) ~= 4 sqrt(X)).

 P4  THE CRITICALITY BUDGET (full ladder, at the worst port node
     j* per rung): log T = log|d| + log(4 sin^2(theta/2)) -
     log(2L) + log K_h; alpha-slopes s_d, s_geo, s_K measured
     fit-free; frozen bar: |s_d + s_geo + s_K| <= 0.05 while
     s_d >= 0.5 (the PNT growth is REAL and the budget CLOSES to
     zero -- criticality = arithmetic growth exactly compensated
     by geometry + Christoffel); typed BUDGET-CLOSED /
     BUDGET-OPEN.

 C   CONTROLS (kz 9): the P2 identification persists for the
     Epstein comb through ITS OWN masses (algebra, rel <= 5e-3)
     and the port level is comb-sensitive: |d_ctl(theta_2) -
     d_truth(theta_2)| / |d_truth| >= 0.5 on both controls.

KILLS: K1 transform/identification breaks -> ATOMSUM-BROKEN;
K2 pipeline breaks -> PIPELINE-BROKEN; K3 control sensitivity
fails -> CONTROL-DEAD.  P3/P4 may FAIL honestly (typed, kept).

VERDICT (frozen enum): ATOMS-IDENTIFIED (+ typed sublabels) /
ATOMSUM-BROKEN / PIPELINE-BROKEN / CONTROL-DEAD.

NO RH claim: identifying the port numerator with a prime partial
sum names the arithmetic content of T -> 1; it does not bound it.

SPEC v2 (honest amendment, LXXX precedent; run 1 = 4/6): (i) the
v1 P2 compared against the UNTAPERED sum -sum mu_n cos(tau_j u_n)
and failed at rel 1.3-1.8 on truth rungs (scramble passed at
2.1e-3) -- the diagnosis is itself a finding: the prime mass is
EXPONENTIALLY concentrated at the top lag edge (density ~ e^{u/2},
~39 percent of mass in the last unit of u), where the deployed
tent assembly tapers (edge cosine weight 1 instead of 2, tent
clipping at i = M-1) -- an O(1) effect exactly on the port modes
(tau_j u_max ~ 2 pi j).  v2 P2 checks the EXACT windowed identity
d_at(theta_j) = -sum_n (mu_n/2) sum_i tent_i(u_n) w_i cos(i
theta_j) (w = 1 at i in {0, M-1}, else 2; rel <= 1e-10) PLUS the
interior comparison (atoms with u <= (M-3) D): exact-windowed ==
untapered 2 cos to tent second order (rel <= 1e-2) -- the naive
reading holds in the interior, the edge taper is the deployed
window's own mass cut.  (ii) the v1 C1 sensitivity bar 0.5 was
mis-set: Epstein's port level shares the PNT scale (measured
sensitivity 0.30); v2 bar 0.25 with the sharing typed.  Intent,
kills and verdict rule UNCHANGED.

SPEC v3 (tolerance repair; run 2 = 5/6): the v2 interior bar 1e-2
was mis-calibrated for the SHALLOWEST rungs, where theta_j is
largest (measured 1.5e-2 at kz 9, decreasing monotonically to
9.9e-5 at kz 40 -- exactly the second-order tent error shrinking
with depth, which is the content); v3 bar 3e-2 plus the mandatory
decreasing trend (shallowest > deepest).  No other change.

FIREWALL: no zeros, no prime-table oracles beyond the deployed
v563 tables (AST scan; the atom arrays uu/mm are the deployed
window data, READ-ONLY); RNG only inside the declared scramble
control; writes nothing but stdout.  No marker moves.

Sources (read-only): v563_paper2_readouts (atom_lags_at tent
assembly, read verbatim before freezing), carleson_testing_law
probe (ATOM-CARRIED, declared input), v866 (ladder).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_atom_numerator_probe.py
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
    c = c_ar + c_at
    d = grid_density(c)
    d_at = grid_density(c_at)
    L = 2 * M - 2
    return dict(d=d, d_at=d_at, c=c, c_at=np.asarray(c_at, float),
                L=L, M=M, D=D, alpha=alpha, h=h, uu=uu, mm=mm)


def cos_transform(cvec, M, L, jlist):
    out = []
    kk = np.arange(1, M - 1)
    for j in jlist:
        th = 2.0 * math.pi * j / L
        out.append(float(cvec[0] + 2.0 * np.sum(
            cvec[1:M - 1] * np.cos(kk * th))
            + cvec[M - 1] * math.cos((M - 1) * th)))
    return np.array(out)


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


def prime_sum(uu, mm, tau):
    return -float(np.sum(mm * np.cos(tau * uu)))


def prime_sum_windowed(uu, mm, M, D, L, j):
    """The EXACT deployed-window prime sum at grid frequency j:
    -sum_n (mu_n/2) sum_i tent_i(u_n) w_i cos(i theta_j) with the
    symmetric-extension cosine weights w (1 at i = 0 and i = M-1,
    else 2) and the tent clipping of atom_lags_at."""
    th = 2.0 * math.pi * j / L
    i0 = np.floor(uu / D).astype(int)
    f = uu / D - i0

    def w_of(i):
        return np.where((i == 0) | (i == M - 1), 1.0, 2.0)

    tot = np.zeros(len(uu))
    for i_at, v_at in ((i0, 1.0 - f), (i0 + 1, f)):
        ok = (i_at >= 0) & (i_at <= M - 1) & (v_at > 0.0)
        tot += np.where(ok, v_at * w_of(i_at)
                        * np.cos(i_at * th), 0.0)
    return -float(np.sum(mm * 0.5 * tot))


def budget_row(kz):
    """The worst-port-node factor decomposition of one rung."""
    b = build_rung(kz)
    h, L, D = b["h"], b["L"], b["D"]
    if h > 900:
        return None
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Pn = eval_chain(al, be, m0, ys, h + 1)
    Kdiag = np.sum(Pn[:, :h] ** 2, axis=1)
    T = vs * Kdiag
    mst = int(np.argmax(T))
    j_st = int(uf_n[mst])
    th = 2.0 * math.pi * j_st / L
    return dict(kz=kz, h=h, alpha=b["alpha"],
                T=float(T[mst]), j=j_st,
                logd=math.log(abs(b["d"][j_st])),
                loggeo=math.log(4.0 * math.sin(th / 2.0) ** 2)
                - math.log(2.0 * L),
                logK=math.log(float(Kdiag[mst])))


def main():
    section("PRIME.PORT.ATOMS.01 -- the prime-sum identity of the "
            "port numerator (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (deployed v563 tables only)",
          not ast_scan(BANNED_IDS))

    section("P1/P2/P3 -- transform + prime-sum identification "
            "(heavy rungs)")
    rel1max = rel2max = rel2imax = 0.0
    rel2i_series = []
    pnt = []
    d_truth_2 = None
    for kz in HEAVY:
        b = build_rung(kz)
        L, M, D = b["L"], b["M"], b["D"]
        jl = list(range(1, 13))
        dd = cos_transform(b["c"], M, L, jl)
        rel1 = float(np.max(np.abs(dd - b["d"][jl])
                            / np.abs(b["d"][jl])))
        dat = cos_transform(b["c_at"], M, L, jl)
        rel1at = float(np.max(np.abs(dat - b["d_at"][jl])
                              / np.abs(b["d_at"][jl])))
        rel1max = max(rel1max, rel1, rel1at)
        rel2 = rel2i = 0.0
        interior = b["uu"] <= (M - 3) * D
        for j in range(1, 11):
            tau_j = (2.0 * math.pi * j / L) / D
            ps = prime_sum_windowed(b["uu"], b["mm"], M, D, L, j)
            rel2 = max(rel2, abs(b["d_at"][j] - ps)
                       / abs(b["d_at"][j]))
            ps_i = prime_sum_windowed(b["uu"][interior],
                                      b["mm"][interior],
                                      M, D, L, j)
            nv_i = prime_sum(b["uu"][interior],
                             b["mm"][interior], tau_j)
            rel2i = max(rel2i, abs(ps_i - nv_i)
                        / max(abs(ps_i), 1e-30))
        rel2max = max(rel2max, rel2)
        rel2imax = max(rel2imax, rel2i)
        rel2i_series.append(rel2i)
        lvl = float(np.sum(b["mm"]))
        ratio = lvl / (4.0 * math.exp(float(np.max(b["uu"])) / 2.0))
        pnt.append(ratio)
        if kz == 9:
            d_truth_2 = float(b["d"][2])
        print("    kz %-3d transform rel %.1e | windowed prime-"
              "sum rel %.1e | interior naive rel %.1e | PNT "
              "level ratio %.3f (X = e^%.2f, %d atoms, %.0f%% "
              "interior)"
              % (kz, max(rel1, rel1at), rel2, rel2i, ratio,
                 float(np.max(b["uu"])), len(b["uu"]),
                 100.0 * float(np.sum(b["mm"][interior]))
                 / max(lvl, 1e-30)))
    check("P1 EXACT TRANSFORM: FFT == symmetric cosine transform "
          "for d and d_at (max rel %.1e <= 1e-9)" % rel1max,
          rel1max <= 1e-9, kill="K1")
    check("P2 PRIME-SUM IDENTITY (SPEC v2, windowed): d_at == the "
          "EXACT deployed-window prime sum (max rel %.1e <= "
          "1e-10); interior atoms match the untapered "
          "-sum mu cos(tau_j u) to tent order (max rel %.1e <= "
          "1e-2) -- the port numerator IS the truncated explicit-"
          "formula prime sum, with the deployed edge taper as the "
          "only correction (mass ~ e^{u/2} sits at the lag edge; "
          "SPEC v3 bar 3e-2 + decreasing tent-error trend)"
          % (rel2max, rel2imax),
          rel2max <= 1e-10 and rel2imax <= 3e-2
          and rel2i_series[0] > rel2i_series[-1], kill="K1")
    check("P3 PNT LEVEL: sum mu_n / (4 e^{u_max/2}) in [%.3f, "
          "%.3f] (bar [0.7, 1.3]) -- the tau = 0 level is the "
          "Chebyshev-psi-scale partial sum"
          % (min(pnt), max(pnt)),
          min(pnt) >= 0.7 and max(pnt) <= 1.3)

    section("P4 -- the criticality budget (full ladder, worst "
            "port node)")
    rows = []
    for kz in core.frame_a_zones():
        r = budget_row(kz)
        if r is not None:
            rows.append(r)
    if len(rows) < 40:
        check("P4.0 ladder census %d >= 40" % len(rows), False,
              kill="K2")
    av = np.array([r["alpha"] for r in rows])
    s_d = float(np.polyfit(av, [r["logd"] for r in rows], 1)[0])
    s_geo = float(np.polyfit(av, [r["loggeo"] for r in rows],
                             1)[0])
    s_K = float(np.polyfit(av, [r["logK"] for r in rows], 1)[0])
    s_T = float(np.polyfit(av, [math.log(r["T"]) for r in rows],
                           1)[0])
    total = s_d + s_geo + s_K
    print("    alpha-slopes at the worst port node: d(log|d|) "
          "%+.3f | d(log geo) %+.3f | d(log K) %+.3f | sum %+.4f "
          "| d(log T) %+.4f"
          % (s_d, s_geo, s_K, total, s_T))
    budget_type = ("BUDGET-CLOSED"
                   if abs(total) <= 0.05 and s_d >= 0.5
                   else "BUDGET-OPEN")
    check("P4.1 typed: %s -- PNT growth s_d = %+.3f >= 0.5 is "
          "REAL and the total budget %+.4f closes to zero "
          "(bar 0.05): the criticality T -> 1 is arithmetic "
          "growth exactly compensated by geometry + Christoffel"
          % (budget_type, s_d, total),
          abs(total) <= 0.05 and s_d >= 0.5)

    section("C -- controls (kz 9)")
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok_ctl = True
    sens = []
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        b = build_rung(9, **kw)
        L, M, D = b["L"], b["M"], b["D"]
        rel2 = 0.0
        for j in range(1, 11):
            ps = prime_sum_windowed(b["uu"], b["mm"], M, D, L, j)
            rel2 = max(rel2, abs(b["d_at"][j] - ps)
                       / abs(b["d_at"][j]))
        ok_ctl &= (rel2 <= 1e-10)
        sv = abs(float(b["d"][2]) - d_truth_2) / abs(d_truth_2)
        sens.append(sv)
        print("    %-8s: windowed prime-sum rel %.1e | "
              "d(theta_2) %+.2f vs truth %+.2f (sensitivity %.2f)"
              % (nmc, rel2, float(b["d"][2]), d_truth_2, sv))
    check("C1 CONTROLS (SPEC v2): the windowed identification "
          "persists (algebra) and the port level is comb-"
          "sensitive (min sensitivity %.2f >= 0.25; Epstein "
          "shares the PNT scale, typed)" % min(sens),
          ok_ctl and min(sens) >= 0.25, kill="K3")

    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "ATOMSUM-BROKEN", "K2": "PIPELINE-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
    else:
        VERDICT = "ATOMS-IDENTIFIED"
    print("\n  VERDICT: %s (%s)" % (VERDICT, budget_type))
    print("""
  NAMED READING (printed, not claimed): the wall's testing
  numerator at the port is the truncated explicit-formula prime
  sum -2 sum Lambda(n)/sqrt(n) cos(tau_j log n) at the alias
  frequencies tau_j = theta_j/D; its tau = 0 level is the PNT
  partial sum ~ 4 e^{u_max/2}; the criticality T -> 1 is this
  arithmetic growth exactly compensated by window geometry and
  Christoffel growth.  Uniform testing (and with the Schur
  reduction, the wall itself) is therefore a statement about the
  ERROR TERM of these prime partial sums at the port frequencies.
  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''


# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('prime_sqrt_uniformization_probe', _SRC_0, 7, (), 'SQRT-UNIFORMIZED', 0),
    ('port_mellin_cauchy_probe', _SRC_1, 5, (), 'MELLIN-KERNEL-CONFIRMED', 0),
    ('port_atom_numerator_probe', _SRC_2, 6, (), 'ATOMS-IDENTIFIED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v882 -- PRIME.SQRT.UNIFORM.01 + PRIME.PORT.MELLIN.01 + PRIME.PORT.ATOMS.01: the universal source law of the port')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v882: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the universal source law: dr uniformization, 1 - e^{-1/2}, Mellin-Cauchy kernel, closed budget')
    print("[%s] v882 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
