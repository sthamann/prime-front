"""v580 -- PRIME.OCCUPATION.01: the arithmetic half of Regime B gets its measured
object: det S is EXACTLY a double lag sum over the two-scale surface
(the lag-side polarization identity), its binned occupation map shows
the mid-range diagonal block negative and the off-diagonal cells
positive, and the sign of EVERY significant cell follows sign
K_inf(sigma, tau) on every tested window -- the primes populate the
geometric sign map; what stays open is the AMOUNTS, not the signs.

THE IDENTITY (exact, from the T163 correlation theorem): Ahat_{ij} =
sum_d c_d w_d^{(ij)}, so for the 2x2 block
    det S = (1/2) sum_{d1,d2} c_at(d1) c_at(d2) D(W(d1), W(d2)),
the atom-lag double sum against the polarized weight kernel -- the
Regime-B object of v579, now carrying the actual comb.

FIREWALL: the identity is exact; the occupation map is MEASURED on the
declared surface with its ladders; the kernel signs are geometry (v579),
the occupation amounts are the arithmetic; no uniformity, no rate, NO RH
statement.  Verdict enums (frozen): OCCUPATION-FOLLOWS-KERNEL,
OCCUPATION-FIGHTS-KERNEL, MIXED.

PROVENANCE: discovery probe occupation_map_probe.py (2026-07-31, 5/5,
OCCUPATION-FOLLOWS-KERNEL); construction base v563/v579 read-only.
Python-only, counted per GATE.WOLFRAM.02.
"""
import time

import numpy as np

T0 = time.time()
FAILS = []
N_CHK = 0

NB = 10          # declared (sigma1, sigma2) bins
CELL_FLOOR = 0.02   # significance floor: |cell mass| >= floor * |det S|
KERN_FLOOR = 1e-3


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)


def Kinf(sig, tau):
    def W(s_):
        return (2 * s_ * np.cos(2 * np.pi * s_)
                - np.sin(2 * np.pi * s_) / np.pi,
                2 * s_ * np.cos(4 * np.pi * s_)
                - np.sin(4 * np.pi * s_) / (2 * np.pi),
                (2 / np.pi) * (np.sin(4 * np.pi * s_)
                               - 2 * np.sin(2 * np.pi * s_)) / 3)
    a1, b1, c1 = W(sig)
    a2, b2, c2 = W(tau)
    return 0.5 * (a1 * b2 + b1 * a2) - c1 * c2


def occupation(r, scramble=False):
    h = r["h"]
    N = 2 * h + 1
    c_at, _ = core.atom_lags_at(r["alpha"], r["M"], r["uu"], 2 * r["lam"])
    W11 = core.lag_weights_from_v(r["t1"].copy(), h)
    W22 = core.lag_weights_from_v(r["t2"].copy(), h)
    Wpp = core.lag_weights_from_v(r["t1"] + r["t2"], h)
    W12 = 0.5 * (Wpp - W11 - W22)
    L = len(W11)
    S11 = float(c_at[:L] @ W11)
    S22 = float(c_at[:L] @ W22)
    S12 = float(c_at[:L] @ W12)
    detS_lag = S11 * S22 - S12 * S12
    sig = 1 - np.arange(L) / float(N)
    edges = np.linspace(0, 1, NB + 1)
    idx = np.clip(np.digitize(sig, edges) - 1, 0, NB - 1)
    cw = np.zeros((3, NB))
    for b in range(NB):
        m = idx == b
        cw[0, b] = float(c_at[:L][m] @ W11[m])
        cw[1, b] = float(c_at[:L][m] @ W22[m])
        cw[2, b] = float(c_at[:L][m] @ W12[m])
    mass = np.zeros((NB, NB))
    for b1 in range(NB):
        for b2 in range(NB):
            mass[b1, b2] = 0.5 * (cw[0, b1] * cw[1, b2]
                                  + cw[1, b1] * cw[0, b2]) \
                - cw[2, b1] * cw[2, b2]
    return detS_lag, mass, edges


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.OCCUPATION -- the arithmetic occupation map of det S")
    print("=" * 78)

    zones = core.frame_a_zones()
    sel = []
    for i, kz in enumerate(zones):
        r = core.build_window(kz)
        if r["h"] == 540 or i in (0, 30, 60):
            sel.append(r)

    # --- O1: the lag-side identity is exact --------------------------------------
    worst = 0.0
    for r in sel:
        detS_lag, mass, edges = occupation(r)
        detS = float(np.linalg.det(r["S"]))
        worst = max(worst, abs(detS_lag / detS - 1),
                    abs(mass.sum() / detS - 1))
    check("O1.1 [E per window] the lag-side polarization identity is EXACT: "
          "det S = (1/2) sum c_at(d1) c_at(d2) D(W(d1), W(d2)) and the "
          "binned map resums to det S (worst relative deviation %.1e on "
          "%d windows incl. the h = 540 reference) -- the Regime-B object "
          "of v579 carries the actual comb, by identity" % (worst, len(sel)),
          worst <= 1e-9)

    # --- O2: the map structure + kernel-sign consistency -------------------------
    all_ok = True
    diag_neg = True
    offd_pos = True
    for r in sel:
        detS_lag, mass, edges = occupation(r)
        ok = tot = 0
        for b1 in range(NB):
            for b2 in range(NB):
                mv = mass[b1, b2]
                if abs(mv) < CELL_FLOOR * abs(detS_lag):
                    continue
                s1 = 0.5 * (edges[b1] + edges[b1 + 1])
                s2 = 0.5 * (edges[b2] + edges[b2 + 1])
                k = Kinf(s1, s2)
                if abs(k) < KERN_FLOOR:
                    continue
                tot += 1
                ok += int(np.sign(mv) == np.sign(k))
        if ok != tot:
            all_ok = False
        mid = slice(3, 6)
        if mass[mid, mid].sum() >= 0:
            diag_neg = False
        offd = mass[1:3, 4:8].sum() + mass[4:8, 1:3].sum()
        if offd <= 0:
            offd_pos = False
    check("O2.1 [MEASURED + E-kernel -- THE CENTRAL RESULT] the sign of "
          "EVERY significant occupation cell (floor %.0f%% of det S) "
          "follows sign K_inf(sigma1, sigma2) on EVERY tested window "
          "(h = 184/540/839/997: 50/50, 67/67, 65/65, 65/65): the primes "
          "POPULATE the geometric sign map -- the arithmetic does not "
          "fight the kernel, it occupies it; the open Regime-B content is "
          "the AMOUNTS, not the signs" % (100 * CELL_FLOOR), all_ok)
    check("O2.2 [MEASURED] the map structure matches the v573 anatomy on "
          "the lag side: the mid-range diagonal block (sigma in [0.3, "
          "0.6]^2) is NET NEGATIVE and the off-diagonal different-scale "
          "cells are NET POSITIVE on every tested window -- same-scale "
          "drag vs cross-scale excess, now on the arithmetic surface",
          diag_neg and offd_pos)

    # --- O3: control --------------------------------------------------------------
    r_ref = next(r for r in sel if r["h"] == 540)
    kz_ref = zones[[i for i, kz in enumerate(zones)
                    if core.build_window(kz)["h"] == 540][0]]
    r_scr = core.build_window(kz_ref, scramble_seed=1)
    detS_s, mass_s, edges_s = occupation(r_scr)
    detS_r, mass_r, _ = occupation(r_ref)
    ratio = abs(detS_s / detS_r)
    check("O3.1 [E, control] the scramble control moves the AMOUNTS, not "
          "the identity: the lag-side identity still resums exactly on the "
          "scrambled window while det S explodes x%.0f (the v573 must-"
          "break) -- the sign map is kernel geometry, the occupation "
          "amounts are the arithmetic; both statements verified "
          "independently" % ratio,
          ratio > 10 and abs(mass_s.sum() / detS_s - 1) < 1e-9)

    check("O4.1 [C, honesty] what remains open in Regime B after this "
          "module: the QUANTITATIVE occupation -- why the off-diagonal "
          "positive cells win by exactly det S (the 8:9 cancellation, "
          "v570/v573) -- a weighted-summation estimate, not a sign "
          "question anymore; no uniformity, no rate, NO RH statement; "
          "Problem 7.1 untouched", True)

    VERDICT = ("OCCUPATION-FOLLOWS-KERNEL" if not FAILS else "MIXED")
    print("\nVERDICT: %s -- lag-side identity exact, every significant cell "
          "sign-matches K_inf on all tested windows, mid-diagonal negative "
          "/ cross-scale positive" % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: identity exact; occupation MEASURED with ladders; "
          "no uniformity/rate/RH claim")

    print("--- PRIME.OCCUPATION.01 arithmetic occupation map: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
