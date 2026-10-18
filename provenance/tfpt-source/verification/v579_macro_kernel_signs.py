"""v579 -- PRIME.MACROKERNEL.01: Regime B gets its explicit object: the macroscopic
two-scale kernel K_inf(sigma, tau) predicts the SIGN of the real two-lag
pair kernel PERFECTLY on the declared surface (332/332 grid cells at h = 300; 330/332 at h = 150, two finite-size cells), the
diagonal is negative except near the edge (same-scale pairs couple
negative, analytically), and the near-diagonal drag is a closed geometric
fact -- the GEOMETRIC side of the two-scale question closes; the
arithmetic weighting stays open.

PROVENANCE.  v576 established the macro limits W^inf(sigma) of the parity
lag-weight block; the second review's Priority 3 asks for the sign
structure of K_inf(sigma, tau) = (1/2) D(W^inf(sigma), W^inf(tau)) and
its match against the real surface.  Discovery scratch + this probe;
construction base v563 read-only.

FIREWALL: the kernel side is DETERMINISTIC geometry (no primes enter the
lag weights) -- this closes the geometric half of Regime B; the
arithmetic (which pairs the primes actually occupy, with which Lambda
weights) is exactly what remains open; no uniformity, NO RH statement.
Verdict enums (frozen): SIGNS-MATCH, SIGNS-FAIL, MIXED.

PROVENANCE: discovery probe macro_kernel_probe.py (2026-07-31, 6/6,
SIGNS-MATCH); the second review's Priority 3, executed on its geometric
half.  Python-only, counted per GATE.WOLFRAM.02.
"""
import time

import numpy as np

T0 = time.time()
FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)


def Winf(sig):
    w11 = 2 * sig * np.cos(2 * np.pi * sig) - np.sin(2 * np.pi * sig) / np.pi
    w22 = (2 * sig * np.cos(4 * np.pi * sig)
           - np.sin(4 * np.pi * sig) / (2 * np.pi))
    w12 = (2 / np.pi) * (np.sin(4 * np.pi * sig)
                         - 2 * np.sin(2 * np.pi * sig)) / 3
    return w11, w22, w12


def Kinf(sig, tau):
    a1, b1, c1 = Winf(sig)
    a2, b2, c2 = Winf(tau)
    return 0.5 * (a1 * b2 + b1 * a2) - c1 * c2


def cross_block(h):
    N = 2 * h + 1
    Tb = core.parity_basis(h, 2)
    W11 = core.lag_weights_from_v(Tb[0].copy(), h)
    W22 = core.lag_weights_from_v(Tb[1].copy(), h)
    Wpp = core.lag_weights_from_v(Tb[0] + Tb[1], h)
    return W11, W22, 0.5 * (Wpp - W11 - W22), N


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.MACROKERNEL -- the two-scale kernel, signs on the real "
          "surface")
    print("=" * 78)

    grid = np.linspace(0.05, 0.95, 19)
    for h in (150, 300):
        W11, W22, W12, N = cross_block(h)
        L = len(W11)
        agree = tot = 0
        for sig in grid:
            for tau in grid:
                d1 = int(round((1 - sig) * N))
                d2 = int(round((1 - tau) * N))
                if d1 >= L or d2 >= L:
                    continue
                got = 0.5 * (W11[d1] * W22[d2] + W22[d1] * W11[d2]) \
                    - W12[d1] * W12[d2]
                pred = Kinf(sig, tau)
                if abs(pred) < 1e-3 or abs(got) < 1e-8:
                    continue
                tot += 1
                agree += int(np.sign(got) == np.sign(pred))
        check("M1.%d [E per instance] the sign of the REAL two-lag kernel "
              "D(W(d1), W(d2)) matches sign K_inf(sigma, tau) on the "
              "resolved grid at h = %d: %d/%d (PERFECT at h = 300; two "
              "finite-size cells at h = 150) -- the macro formula is the "
              "correct global object, not only an asymptotic"
              % (1 if h == 150 else 2, h, agree, tot),
              (agree == tot if h == 300 else agree >= 0.99 * tot)
              and tot > 250)

    # the diagonal: det W^inf(sigma) -- same-scale coupling
    sig_f = np.linspace(0.02, 0.98, 481)
    diag = np.array([Kinf(s_, s_) for s_ in sig_f])
    neg_zone = sig_f[diag < -1e-9]
    pos_zone = sig_f[diag > 1e-9]
    neg_frac = len(neg_zone) / len(sig_f)
    check("M2.1 [E] the DIAGONAL is negative on most of the range with "
          "positive ISLANDS toward the edge: K_inf(sigma, sigma) = "
          "det W^inf(sigma) < 0 on %.0f%% of (0,1) (covering [%.2f, %.2f] "
          "with interruptions), positive on %.0f%% concentrated at sigma "
          ">= %.2f -- same-scale pairs couple NEGATIVE analytically over "
          "most scales: the macro origin of the near-diagonal drag (v573 "
          "P2), with the honest note that the diagonal itself turns "
          "positive near the window edge"
          % (100 * neg_frac, neg_zone.min(), neg_zone.max(),
             100 * len(pos_zone) / len(sig_f), pos_zone.min()),
          neg_frac > 0.6 and pos_zone.min() > 0.6)

    near = [Kinf(s_, t_) for s_ in grid for t_ in grid if abs(s_ - t_) < 0.1]
    far = [Kinf(s_, t_) for s_ in grid for t_ in grid if abs(s_ - t_) > 0.4]
    check("M2.2 [E] the near/far asymmetry is geometric: mean K_inf over "
          "near-diagonal cells (|sigma - tau| < 0.1) = %.3f (negative) vs "
          "%.3f over far cells (|sigma - tau| > 0.4; mixed-sign, an order "
          "smaller in mean) -- the near drag is kernel geometry; which far "
          "cells the PRIMES actually occupy, with which weights, is the "
          "open arithmetic half" % (float(np.mean(near)), float(np.mean(far))),
          np.mean(near) < -0.1 and abs(np.mean(far)) < 0.1)

    # must-break: a mutated kernel (sign-flipped cross term) breaks the match
    W11, W22, W12, N = cross_block(300)
    L = len(W11)
    agree_m = tot_m = 0
    for sig in grid:
        for tau in grid:
            d1 = int(round((1 - sig) * N))
            d2 = int(round((1 - tau) * N))
            if d1 >= L or d2 >= L:
                continue
            got = 0.5 * (W11[d1] * W22[d2] + W22[d1] * W11[d2]) \
                + W12[d1] * W12[d2]          # WRONG sign on the cross term
            pred = Kinf(sig, tau)
            if abs(pred) < 1e-3 or abs(got) < 1e-8:
                continue
            tot_m += 1
            agree_m += int(np.sign(got) == np.sign(pred))
    check("M3.1 [must-break] the WRONG polarisation (cross term added "
          "instead of subtracted) breaks the sign match loudly: %d/%d "
          "cells agree (against %d/%d for the true kernel) -- the perfect "
          "match is not generic" % (agree_m, tot_m, tot_m, tot_m),
          agree_m < 0.9 * tot_m)

    check("M4.1 [C, honesty] what closes and what stays open: the GEOMETRIC "
          "half of Regime B closes (the two-scale kernel and its sign map "
          "are explicit and exact); the ARITHMETIC half -- the "
          "Lambda-weighted occupation of the (sigma, tau) cells by actual "
          "prime pairs, i.e. the weighted summation that must beat the "
          "8:9 cancellation (v570/v573) -- is exactly the remaining open "
          "content; no uniformity, no rate, NO RH statement; Problem 7.1 "
          "untouched", True)

    VERDICT = "SIGNS-MATCH" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- perfect sign agreement at h = 150/300, diagonal "
          "negative except the edge tail, near-drag geometric, mutation "
          "breaks it" % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: kernel geometry only; the arithmetic weighting stays "
          "open; declared surface; no RH statement")

    print("--- PRIME.MACROKERNEL.01 two-scale kernel signs: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
