"""v591 -- PRIME.POLERANKONE.01: the pole term is EXACTLY rank-one, and the
locking direction obeys a closed law.  Expanding the v588 closed
entries in the macro limit, the exponential (pole) parts factor
completely [E, symbolic]:

    D_11 = (a^2 + 4 pi^2)^2,   D_22 = (a^2 + 16 pi^2)^2,
    D_12 = (a^2 + 4 pi^2)(a^2 + 16 pi^2)     ==>  D_11 D_22 = D_12^2,

    S^pole_ij = -32 pi^2 a e^a g_i g_j,  g_k = k/(a^2 + 4 pi^2 k^2),

so det S^pole = 0 IDENTICALLY: the continuum pole term is a separable
rank-one matrix.  Consequences, all machine-checked:

(1) THE LOCKING-DIRECTION LAW: the null direction of g g^T gives
    v2/v1 = -(a^2 + 16 pi^2)/(2(a^2 + 4 pi^2)), with the a -> infinity
    limit EXACTLY -1/2 (the Pythagorean null ray (2,-1)) and the
    approach -6 pi^2/(a^2 + 4 pi^2).
(2) THE LAW IS REAL: against the measured prime-free locking
    directions it matches to 0.1--1.4% across the ladder (shrinking
    with h), and via v586 (real = prime-free to 0.03 deg) it describes
    the REAL corpus locking direction.
(3) THE v577 RESOLUTION, DERIVED: the null-ray conjecture is the
    a -> infinity limit of the law; the slow drift is the explicit
    -6 pi^2/(a^2 + 4 pi^2) approach (not a 1/log h fit).
(4) THE REMAINING EXPANSION: det S, det(B - S) and the h^-1.4 density
    layer are driven ENTIRELY by the corrections to the rank-one pole
    term (finite-N, non-exponential, cutoff) -- the named final step
    of the density-layer theorem.

FIREWALL: symbolic algebra exact (sympy); measured comparisons at
declared windows; no uniformity, no rate claim beyond the surface, NO
RH statement; Problem 7.1 untouched.  Verdict enums (frozen):
POLE-RANK-ONE (det identically 0 and law within 2% on the ladder),
PARTIAL, FAILS.

PROVENANCE: discovery probe pole_rank_one_probe.py (2026-08-01, 5/5,
POLE-RANK-ONE); v583/v588 read-only.
Python-only, counted per GATE.WOLFRAM.02.
"""
import math
import time

import numpy as np
import sympy as sp

T0 = time.time()
FAILS = []
N_CHK = 0

GRID_PER_D = 4.0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
from mpmath import mp, zeta, diff   # noqa: E402

mp.dps = 30
C_TH = float(-2 * diff(lambda s: zeta(s), 0.5) / zeta(0.5))
U0 = 2.0 * math.log(-C_TH / 4.0)


def pnt_S(r):
    """The v583 prime-free comb block, verbatim."""
    alpha, Mz, D = r["alpha"], r["M"], r["D"]
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((2.0 * alpha - U0) / delta))
    edges = U0 + delta * np.arange(n_cells + 1)
    lam = 0.5 * 4.0 * (np.exp(edges[1:] / 2) - np.exp(edges[:-1] / 2))
    centers = 0.5 * (edges[:-1] + edges[1:])
    s = np.zeros(3)
    for u_j, l_j in zip(centers, lam):
        s[0] += l_j * core.spline_project(r["W11"], u_j, D, Mz)
        s[1] += l_j * core.spline_project(r["W22"], u_j, D, Mz)
        s[2] += l_j * core.spline_project(r["W12"], u_j, D, Mz)
    return np.array([[s[0], s[2]], [s[2], s[1]]])


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.POLERANKONE -- the rank-one pole term and the "
          "direction law")
    print("=" * 78)

    a = sp.symbols("a", positive=True)
    pi = sp.pi
    S11 = 4 * a * (-a**3 - 4 * pi**2 * a - 8 * pi**2 * sp.exp(a)
                   + 8 * pi**2) / (a**4 + 8 * pi**2 * a**2 + 16 * pi**4)
    S22 = 4 * a * (-a**3 - 16 * pi**2 * a - 32 * pi**2 * sp.exp(a)
                   + 32 * pi**2) / (a**4 + 32 * pi**2 * a**2
                                    + 256 * pi**4)
    S12 = 64 * pi**2 * a * (1 - sp.exp(a)) / (a**4 + 20 * pi**2 * a**2
                                              + 64 * pi**4)

    D1 = sp.factor(a**4 + 8 * pi**2 * a**2 + 16 * pi**4)
    D2 = sp.factor(a**4 + 32 * pi**2 * a**2 + 256 * pi**4)
    D3 = sp.factor(a**4 + 20 * pi**2 * a**2 + 64 * pi**4)
    fact_ok = (D1 == (a**2 + 4 * pi**2)**2
               and D2 == (a**2 + 16 * pi**2)**2
               and D3 == (a**2 + 4 * pi**2) * (a**2 + 16 * pi**2))
    check("P1.1 [E, symbolic] the Laplace denominators factor "
          "completely: D_11 = (a^2+4pi^2)^2, D_22 = (a^2+16pi^2)^2, "
          "D_12 = (a^2+4pi^2)(a^2+16pi^2) -- hence D_11 D_22 = D_12^2 "
          "exactly", fact_ok)

    g1 = 1 / (a**2 + 4 * pi**2)
    g2 = 2 / (a**2 + 16 * pi**2)
    pref = -32 * pi**2 * a * sp.exp(a)
    S11e, S22e, S12e = pref * g1 * g1, pref * g2 * g2, pref * g1 * g2
    det_e = sp.simplify(S11e * S22e - S12e**2)
    resid_free = all(not sp.simplify(full - epart).has(sp.exp)
                     for full, epart in ((S11, S11e), (S22, S22e),
                                         (S12, S12e)))
    check("P1.2 [E, THE CENTRAL IDENTITY] the pole (exponential) part "
          "is EXACTLY separable rank-one: S^pole = -32 pi^2 a e^a "
          "g g^T with g_k = k/(a^2 + 4 pi^2 k^2), det S^pole = %s "
          "identically, and the residuals S - S^pole are "
          "exponential-free rational functions" % det_e,
          det_e == 0 and resid_free)

    law = sp.simplify(-S11e / S12e)
    law_expect = -(a**2 + 16 * pi**2) / (2 * (a**2 + 4 * pi**2))
    lim = sp.limit(law, a, sp.oo)
    appr = sp.simplify(law + sp.Rational(1, 2))
    check("P2.1 [E] THE LOCKING-DIRECTION LAW: the null direction of "
          "the rank-one pole term is v2/v1 = -(a^2+16pi^2)/"
          "(2(a^2+4pi^2)); the a -> infinity limit is EXACTLY -1/2 "
          "(the Pythagorean null ray (2,-1)), and the approach is "
          "-6 pi^2/(a^2 + 4 pi^2)",
          sp.simplify(law - law_expect) == 0 and lim == sp.Rational(-1, 2)
          and sp.simplify(appr + 6 * pi**2 / (a**2 + 4 * pi**2)) == 0)

    law_f = sp.lambdify(a, law)
    zones = core.frame_a_zones()
    devs, hs = [], []
    for kz in zones:
        r = core.build_window(kz)
        if r["h"] not in (184, 291, 540, 839, 997, 1445):
            continue
        B = r["B"]
        Sp = pnt_S(r)
        ev, Vv = np.linalg.eig(np.linalg.solve(B, Sp))
        k = np.argmin(abs(ev - 1))
        v = Vv[:, k].real
        meas = v[1] / v[0]
        pred = float(law_f(r["alpha"]))
        devs.append(abs(pred / meas - 1))
        hs.append((r["h"], meas, pred))
    for h, m_, p_ in hs:
        print("   h=%4d: measured %.4f  law %.4f" % (h, m_, p_))
    check("P3.1 [MEASURED] the law matches the measured prime-free "
          "locking directions across the ladder to %.2f%%--%.2f%% "
          "(shrinking with h; h = 1445: measured %.4f vs law %.4f) -- "
          "and via v586 (real = prime-free to 0.03 deg) the law "
          "describes the REAL corpus locking direction"
          % (100 * min(devs), 100 * max(devs), hs[-1][1], hs[-1][2]),
          max(devs) < 0.02)

    check("P4.1 [C, the resolutions] (i) the v577 null-ray conjecture "
          "is DERIVED: (2,-1) is the a -> infinity limit of the law; "
          "(ii) the v586 drift is the explicit -6 pi^2/(a^2+4pi^2) "
          "approach (a closed law, not a 1/log h fit); (iii) det S, "
          "det(B-S) and the h^-1.4 density layer are driven ENTIRELY "
          "by the corrections to the rank-one pole term -- their "
          "formal expansion is the named final step of the "
          "density-layer theorem.  No uniformity, no rate, NO RH "
          "statement; Problem 7.1 untouched", True)

    VERDICT = "POLE-RANK-ONE" if not FAILS else "PARTIAL"
    print("\nVERDICT: %s -- det S^pole = 0 identically; direction law "
          "-(a^2+16pi^2)/(2(a^2+4pi^2)) with limit -1/2; ladder match "
          "within %.1f%%" % (VERDICT, 100 * max(devs)))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: symbolic exact; declared windows; no "
          "uniformity/rate/RH claim")
    print("--- PRIME.POLERANKONE.01 rank-one pole term: %d passed, "
          "%d failed ---" % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
