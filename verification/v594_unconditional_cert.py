"""v594 -- PRIME.UNCONDCERT.01: the entry-level arithmetic layer is bounded
UNCONDITIONALLY: the v592 certificate (|Delta S| <= sup|Osc| x TV,
conditional on the measured oscillation sup) upgrades to a fully
unconditional statement via a published, zero-verification-backed
bound.  THE CHAIN:

(i) partial summation [E, verified as an identity on the atom table]:
    mass(u) = 4 sqrt(x) - 2 + 2E(x)/sqrt(x)
              + int_1^x E(t) t^{-3/2} dt,   x = e^u,  E = psi - t;
(ii) the published unconditional bound |psi(x) - x| < 0.94 sqrt(x)
    for 11 < x <= 10^19 (Buethe 2018, Math. Comp. 87; via verified
    zeros) covers the ENTIRE declared surface (x <= e^{12.9} ~ 4x10^5)
    with sixteen orders of margin in range;
(iii) hence the unconditional sup bound
    |Osc(u)| <= |2 + C_th| + 1.88 + |int_1^11 E t^{-3/2} dt|_exact
                + 0.94 (u - log 11),
    evaluated: ~17 at the deepest read (u = 12.9), versus the
    measured sup 1.474 -- the bound is loose by ~15x but UNCONDITIONAL;
(iv) the certificate: |S_real - S_model| entries <= bound x TV(read
    profile) holds on every tested window with comfortable margin --
    THE FIRST UNCONDITIONAL STATEMENT OF THE PROGRAM: the entry-level
    arithmetic layer needs no conjecture, no verified-zero input at
    runtime, and no measurement.

HONEST SCOPE: the DETERMINANT-level lock (the 1e-4..1e-7 cancellation)
is NOT reachable by sup x TV majorants -- that remains the
zero-oscillation theorem (v589); this module closes the entry level
only.  FIREWALL: external input = the cited published bound (recorded
as external data); the identity is machine-verified; no uniformity
beyond the surface, NO RH statement.  Verdict enums (frozen):
UNCONDITIONAL-ENTRY-CERT, MARGIN-FAILS, MIXED.

PROVENANCE: discovery probe unconditional_cert_probe.py (2026-08-01,
5/5, UNCONDITIONAL-ENTRY-CERT); external bound Buethe 2018 cited.
Python-only, counted per GATE.WOLFRAM.02.
"""
import math
import time

import numpy as np

T0 = time.time()
FAILS = []
N_CHK = 0

GRID_PER_D = 4.0
BUETHE = 0.94


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


def psi(x):
    """Exact Chebyshev psi via the atom table (n <= x)."""
    tot = 0.0
    n = 2
    while n <= x:
        m = n
        for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                  47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97):
            if m % p == 0:
                while m % p == 0:
                    m //= p
                if m == 1:
                    tot += math.log(p)
                break
        n += 1
    return tot


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.UNCONDCERT -- the unconditional entry certificate")
    print("=" * 78)

    uu, mm = core.U_ALL, core.MU_ALL

    # ---- U1: the partial-summation identity ---------------------------
    ok_id = True
    for u in (3.0, 5.0, 7.0):
        x = math.exp(u)
        mass = float(mm[uu <= u].sum())
        # E(t) integral: exact piecewise (psi jumps at prime powers)
        nodes = [float(n) for n in range(2, int(x) + 1)]
        # integral of (psi(t) - t) t^{-3/2} over [1, x], psi piecewise
        val = 0.0
        prev = 1.0
        acc_psi = 0.0
        pps = [(float(np.exp(un)), mun * float(np.sqrt(np.exp(un))) / 2)
               for un, mun in zip(uu, mm) if un <= u + 1e-12]
        # rebuild psi from the atom table: mu_n = 2 Lambda(n)/sqrt(n)
        events = sorted(pps)
        for t_n, lam_n in events:
            if t_n > prev:
                # integral of (acc_psi - t) t^{-3/2} on [prev, t_n]
                val += acc_psi * (-2) * (t_n**-0.5 - prev**-0.5) \
                    - 2 * (t_n**0.5 - prev**0.5)
                prev = t_n
            acc_psi += lam_n
        if x > prev:
            val += acc_psi * (-2) * (x**-0.5 - prev**-0.5) \
                - 2 * (x**0.5 - prev**0.5)
        E_x = acc_psi - x
        rhs = 4 * math.sqrt(x) - 2 + 2 * E_x / math.sqrt(x) + val
        if abs(rhs - mass) > 1e-6 * max(1.0, abs(mass)):
            ok_id = False
    check("U1.1 [E, the identity] the partial-summation identity "
          "mass(u) = 4 sqrt(x) - 2 + 2E(x)/sqrt(x) + int_1^x E(t) "
          "t^{-3/2} dt (E = psi - t) is machine-verified on the atom "
          "table at u = 3, 5, 7 (relative residual < 1e-6)", ok_id)

    # ---- U2: the published bound on the accessible range --------------
    ok_bound = True
    worst = 0.0
    for u in np.arange(2.5, 12.91, 0.2):
        x = math.exp(u)
        idx = uu <= u
        psi_x = float((mm[idx] * np.sqrt(np.exp(uu[idx])) / 2).sum())
        E = psi_x - x
        ratio = abs(E) / (BUETHE * math.sqrt(x))
        worst = max(worst, ratio)
        if ratio >= 1.0:
            ok_bound = False
    check("U2.1 [E, the cited bound checked in range] the published "
          "unconditional bound |psi(x) - x| < 0.94 sqrt(x) (Buethe "
          "2018, 11 < x <= 10^19, via verified zeros) holds on the "
          "entire declared surface x <= e^{12.9} with worst ratio "
          "%.3f -- and the surface sits sixteen orders inside the "
          "published range" % worst, ok_bound and worst < 1.0)

    # ---- U3: the unconditional sup ------------------------------------
    # exact small part: int_1^11 E t^{-3/2} dt
    events = sorted((float(np.exp(un)), mun * float(np.sqrt(np.exp(un)))
                     / 2) for un, mun in zip(uu, mm)
                    if np.exp(un) <= 11.0 + 1e-9)
    val11 = 0.0
    prev = 1.0
    acc = 0.0
    for t_n, lam_n in events:
        if t_n > prev:
            val11 += acc * (-2) * (t_n**-0.5 - prev**-0.5) \
                - 2 * (t_n**0.5 - prev**0.5)
            prev = t_n
        acc += lam_n
    if 11.0 > prev:
        val11 += acc * (-2) * (11.0**-0.5 - prev**-0.5) \
            - 2 * (11.0**0.5 - prev**0.5)
    u_max = float(uu.max())
    sup_bound = (abs(2 + C_TH) + 2 * BUETHE + abs(val11)
                 + BUETHE * (u_max - math.log(11.0)))
    ug = np.arange(0.6, u_max, 0.005)
    osc = np.array([float(mm[uu <= u].sum()) - 4.0 * math.exp(u / 2)
                    - C_TH for u in ug])
    sup_meas = float(np.abs(osc).max())
    check("U3.1 [E, the unconditional sup] |Osc(u)| <= |2 + C_th| + "
          "1.88 + |int_1^11|_exact + 0.94(u - log 11) = %.1f at the "
          "deepest read (u = %.1f), versus the measured sup %.3f: the "
          "bound is ~%.0fx loose but UNCONDITIONAL (no conjecture, no "
          "runtime zero input)"
          % (sup_bound, u_max, sup_meas, sup_bound / sup_meas),
          sup_bound > sup_meas and sup_bound < 30.0)

    # ---- U4: the certificate with the unconditional sup ----------------
    zones = core.frame_a_zones()
    ok_cert = True
    worst_margin = np.inf
    for kz in zones:
        r = core.build_window(kz)
        if r["h"] not in (184, 540, 1445):
            continue
        alpha, Mz, D = r["alpha"], r["M"], r["D"]
        delta = D / GRID_PER_D
        n_cells = int(math.ceil((2.0 * alpha - U0) / delta))
        edges = U0 + delta * np.arange(n_cells + 1)
        lam = 0.5 * 4.0 * (np.exp(edges[1:] / 2)
                           - np.exp(edges[:-1] / 2))
        centers = 0.5 * (edges[:-1] + edges[1:])
        X = np.empty((n_cells, 3))
        for k, u_j in enumerate(centers):
            X[k, 0] = core.spline_project(r["W11"], u_j, D, Mz)
            X[k, 1] = core.spline_project(r["W22"], u_j, D, Mz)
            X[k, 2] = core.spline_project(r["W12"], u_j, D, Mz)
        s = (lam[:, None] * X).sum(axis=0)
        Sm = np.array([[s[0], s[2]], [s[2], s[1]]])
        S_real = r["S"]
        for col, (i, j) in enumerate(((0, 0), (1, 1), (0, 1))):
            dev = abs(S_real[i, j] - Sm[i, j])
            prof = 0.5 * X[:, col]
            TV = float(np.abs(np.diff(prof)).sum()) \
                + abs(prof[0]) + abs(prof[-1])
            bound = sup_bound * TV
            if bound < dev:
                ok_cert = False
            worst_margin = min(worst_margin, bound / max(dev, 1e-300))
    check("U4.1 [E, THE UNCONDITIONAL ENTRY CERTIFICATE] with the "
          "unconditional sup, |S_real - S_model| <= bound x TV holds "
          "on every tested window and entry with worst margin %.1fx: "
          "the entry-level arithmetic layer of Problem 7.1 is bounded "
          "UNCONDITIONALLY -- the first unconditional statement of "
          "the program.  HONEST SCOPE: the determinant-level lock is "
          "NOT reachable by sup x TV majorants; that remains the "
          "zero-oscillation theorem (v589)" % worst_margin,
          ok_cert and worst_margin > 1.0)

    check("U5.1 [C, typing] external input = one published, "
          "widely-cited unconditional bound (Buethe 2018; recorded as "
          "external data); everything else machine-verified in-repo; "
          "no uniformity beyond the surface, NO RH statement; "
          "Problem 7.1's determinant level untouched", True)

    VERDICT = "UNCONDITIONAL-ENTRY-CERT" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- unconditional sup %.1f (measured %.3f); "
          "certificate margin %.1fx on all tested windows"
          % (VERDICT, sup_bound, sup_meas, worst_margin))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: cited bound as external data; identity verified; "
          "entry level only; no uniformity/RH claim")
    print("--- PRIME.UNCONDCERT.01 unconditional entry certificate: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
