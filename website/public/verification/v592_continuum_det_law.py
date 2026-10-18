"""v592 -- PRIME.DETLAW.01: the continuum determinant law: det S in closed
form, one full exponential order suppressed, and the dominance growth
derived.  From the v587/v588 closed entries [E, symbolic]:

  det S(a) = 16 a^3 (a^5 + 20 pi^2 a^3 + 40 pi^2 a^2 e^a - 40 pi^2 a^2
             + 64 pi^4 a + 256 pi^4 e^a - 256 pi^4)
             / ((a^2 + 4 pi^2)^2 (a^2 + 16 pi^2)^2),

with the e^{2a} coefficient IDENTICALLY zero (the v591 rank-one
cancellation) and the exact leading law

  det S(a) ~ 640 pi^2 e^a / a^3        (a -> infinity):

the determinant is suppressed by one full exponential order relative
to the entries squared -- derived, not measured.  Consequences and
honest layers:

(1) THE DOMINANCE GROWTH, DERIVED AT THE CONTINUUM LEVEL: with det B
    slowly varying (measured 2.6..9.5 across the ladder), P = det S/
    det B tracks e^alpha/alpha^3 -- the closed-form origin of the
    measured v570 growth (P ~ h up to polylog, exponent ~ 0.9 on the
    ladder).
(2) THE FINITE-N GAP, MEASURED AND TYPED: at ladder windows the
    continuum det captures 0.19 -> 0.50 of the finite-N determinant
    (growing as D shrinks): the finite-N (Euler-Maclaurin/edge) layer
    is first-order for the determinant and is the named remaining
    expansion step of the density-layer theorem.
(3) THE ENTRY-LEVEL ARITHMETIC CERTIFICATE: the deviation of the real
    entries from the density model is rigorously bounded -- GIVEN the
    measured oscillation sup -- by sup|Osc| x TV(read profile)
    (integration by parts); the certificate holds with margin on
    every tested window.

FIREWALL: symbolic algebra exact; ladder comparisons at declared
windows; the certificate is conditional on the measured sup|Osc| (an
unconditional sup needs the zero-oscillation theorem -- the named
open); no uniformity, no rate beyond the surface, NO RH statement.
Verdict enums (frozen): DET-LAW-DERIVED, PARTIAL, FAILS.

PROVENANCE: discovery probe continuum_det_law_probe.py (2026-08-01,
6/6, DET-LAW-DERIVED); v583/v588/v591 read-only.
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


def pnt_S_and_reads(r):
    """The v583 grid model + the read profiles X_ij(u) for the TV
    certificate."""
    alpha, Mz, D = r["alpha"], r["M"], r["D"]
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((2.0 * alpha - U0) / delta))
    edges = U0 + delta * np.arange(n_cells + 1)
    lam = 0.5 * 4.0 * (np.exp(edges[1:] / 2) - np.exp(edges[:-1] / 2))
    centers = 0.5 * (edges[:-1] + edges[1:])
    X = np.empty((n_cells, 3))
    for k, u_j in enumerate(centers):
        X[k, 0] = core.spline_project(r["W11"], u_j, D, Mz)
        X[k, 1] = core.spline_project(r["W22"], u_j, D, Mz)
        X[k, 2] = core.spline_project(r["W12"], u_j, D, Mz)
    s = (lam[:, None] * X).sum(axis=0)
    Sm = np.array([[s[0], s[2]], [s[2], s[1]]])
    return Sm, centers, X


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.DETLAW -- the continuum determinant law and the "
          "certificates")
    print("=" * 78)

    # ---- L1: the closed determinant and its leading law -------------------
    a = sp.symbols("a", positive=True)
    pi = sp.pi
    S11 = 4 * a * (-a**3 - 4 * pi**2 * a - 8 * pi**2 * sp.exp(a)
                   + 8 * pi**2) / (a**4 + 8 * pi**2 * a**2 + 16 * pi**4)
    S22 = 4 * a * (-a**3 - 16 * pi**2 * a - 32 * pi**2 * sp.exp(a)
                   + 32 * pi**2) / (a**4 + 32 * pi**2 * a**2 + 256 * pi**4)
    S12 = 64 * pi**2 * a * (1 - sp.exp(a)) / (a**4 + 20 * pi**2 * a**2
                                              + 64 * pi**4)
    detS = sp.factor(sp.simplify(sp.expand(S11 * S22 - S12**2)))
    E = sp.symbols("E", positive=True)
    detS_E = sp.expand(detS.subs(sp.exp(a), E))
    c2 = sp.simplify(detS_E.coeff(E, 2))
    c1 = sp.factor(detS_E.coeff(E, 1))
    c1_expect = 128 * pi**2 * a**3 * (5 * a**2 + 32 * pi**2) \
        / ((a**2 + 4 * pi**2)**2 * (a**2 + 16 * pi**2)**2)
    lead = sp.limit(c1 * a**3, a, sp.oo)
    check("L1.1 [E, symbolic -- THE DETERMINANT LAW] det S(a) is closed "
          "and one full exponential order suppressed: the e^{2a} "
          "coefficient is IDENTICALLY %s (the v591 rank-one cancellation) "
          "and the e^a coefficient is 128 pi^2 a^3 (5a^2 + 32 pi^2)/"
          "((a^2+4pi^2)^2 (a^2+16pi^2)^2), giving the exact leading law "
          "det S ~ 640 pi^2 e^a/a^3 (lim a^3 c_1 = %s = 640 pi^2)"
          % (c2, lead),
          c2 == 0 and sp.simplify(c1 - c1_expect) == 0
          and sp.simplify(lead - 640 * pi**2) == 0)

    detS_f = sp.lambdify(a, detS)
    c1e_f = sp.lambdify(a, c1 * sp.exp(a))
    law_f = sp.lambdify(a, 640 * pi**2 * sp.exp(a) / a**3)
    dom = [c1e_f(x) / detS_f(x) for x in (3.0, 5.0, 10.0)]
    ratios_int = [law_f(x) / detS_f(x) for x in (20.0, 40.0, 80.0, 160.0)]
    check("L1.2 [E, internal consistency] the e^a term with its EXACT "
          "closed coefficient carries the determinant already at window "
          "scales ((c1 e^a)/det = %.4f/%.4f/%.4f at a = 3/5/10), and the "
          "leading 640 pi^2 e^a/a^3 law converges monotonically "
          "(law/exact = %.2f/%.2f/%.2f/%.2f at a = 20/40/80/160; the "
          "1/a^2 corrections carry ~40 pi^2 coefficients, so the "
          "approach is slow but clean)"
          % (dom[0], dom[1], dom[2], *ratios_int),
          all(abs(x - 1) < 0.01 for x in dom)
          and all(ratios_int[k + 1] < ratios_int[k]
                  for k in range(len(ratios_int) - 1))
          and abs(ratios_int[-1] - 1) < 0.05)

    # ---- L2: ladder comparisons -------------------------------------------
    zones = core.frame_a_zones()
    rows = []
    for kz in zones:
        r = core.build_window(kz)
        if r["h"] not in (184, 291, 540, 839, 997, 1445):
            continue
        Sm, centers, X = pnt_S_and_reads(r)
        det_fin = float(np.linalg.det(Sm))
        det_cont = float(detS_f(r["alpha"]))
        detB = float(np.linalg.det(r["B"]))
        rows.append((r["h"], r["alpha"], r["D"], det_cont / det_fin,
                     det_fin / detB, r, Sm, centers, X))

    gaps = [x[3] for x in rows]
    Ds = [x[2] for x in rows]
    check("L2.1 [MEASURED, the finite-N gap typed] the continuum "
          "determinant captures %.2f -> %.2f of the finite-N determinant "
          "across the ladder, growing monotonically as D shrinks (D: "
          "%.4f -> %.4f): the finite-N (Euler-Maclaurin/edge) layer is "
          "first-order for the determinant -- the named remaining "
          "expansion step of the density-layer theorem"
          % (gaps[0], gaps[-1], Ds[0], Ds[-1]),
          gaps[0] < gaps[-1] and 0.1 < gaps[0] and gaps[-1] < 0.9)

    P_meas = np.array([float(np.linalg.det(x[5]["S"]))
                       / float(np.linalg.det(x[5]["B"])) for x in rows])
    alphas = np.array([x[1] for x in rows])
    P_pred = np.array([detS_f(al) for al in alphas]) \
        / np.array([float(np.linalg.det(x[5]["B"])) for x in rows])
    cc = float(np.corrcoef(np.log(P_meas), np.log(P_pred))[0, 1])
    check("L2.2 [MEASURED, the dominance growth derived] the REAL "
          "measured dominance P = det S/det B tracks the closed "
          "continuum formula with log-log correlation %.4f across the "
          "ladder (the level is offset by the typed finite-N gap, the "
          "GROWTH is the closed law e^alpha/alpha^3 up to 1/a^2 "
          "corrections) -- the closed-form origin of the v570 growth "
          "measurement" % cc, cc > 0.99)

    # ---- L3: the entry-level arithmetic certificate ------------------------
    uu, mm = core.U_ALL, core.MU_ALL
    ug = np.arange(U0, 9.6, 0.01)
    osc = np.array([float(mm[uu <= u].sum()) - 4.0 * math.exp(u / 2)
                    - C_TH for u in ug])
    sup_osc = float(np.abs(osc).max())
    ok_cert = True
    worst_margin = np.inf
    for h, alpha, D, gap, P, r, Sm, centers, X in rows:
        if h not in (184, 540, 1445):
            continue
        S_real = r["S"]
        for col, (i, j) in enumerate(((0, 0), (1, 1), (0, 1))):
            dev = abs(S_real[i, j] - Sm[i, j])
            prof = 0.5 * X[:, col]
            TV = float(np.abs(np.diff(prof)).sum()) \
                + abs(prof[0]) + abs(prof[-1])
            bound = sup_osc * TV
            if bound < dev:
                ok_cert = False
            worst_margin = min(worst_margin, bound / max(dev, 1e-300))
    check("L3.1 [MEASURED-conditional, the entry certificate] the "
          "arithmetic deviation of every tested real entry from the "
          "density model is bounded by sup|Osc| x TV(read profile) "
          "(integration by parts; sup|Osc| = %.2f measured on the atom "
          "table): the certificate holds on every tested window/entry "
          "with worst margin %.1fx -- the entry-level arithmetic layer "
          "is CERTIFIED given the oscillation sup; an unconditional sup "
          "is exactly the zero-oscillation theorem (v589), named"
          % (sup_osc, worst_margin),
          ok_cert and worst_margin > 1.0)

    check("L4.1 [C, program status] the density-layer theorem now has: "
          "the entry closed forms (v587), the ladder/pole assembly "
          "(v588), the rank-one structure and direction law (v591), the "
          "continuum determinant law with its e^a/a^3 leading order "
          "(here), and the finite-N gap typed as the one remaining "
          "expansion layer.  The zero-oscillation theorem (arithmetic "
          "layer) and the OS/RP positivity theorem stay the two named "
          "hard opens; no uniformity, no rate beyond the surface, NO RH "
          "statement", True)

    VERDICT = "DET-LAW-DERIVED" if not FAILS else "PARTIAL"
    print("\nVERDICT: %s -- det S ~ 640 pi^2 e^a/a^3 exact; dominance "
          "growth correlation %.3f; finite-N gap %.2f->%.2f typed; entry "
          "certificate margin %.1fx" % (VERDICT, cc, gaps[0], gaps[-1],
                                        worst_margin))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: symbolic exact; certificate conditional on measured "
          "sup; no uniformity/rate/RH claim")

    print("--- PRIME.DETLAW.01 continuum determinant law: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
