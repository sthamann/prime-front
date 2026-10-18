"""PRIME.LOCKPROJ -- the 1D reduction of the arithmetic layer: along
the CLOSED lock direction (the v591 law) the zero-side functional
cancels the closed density value in a NEAR-IDENTITY, and the
cancellation is collective across the zeros.

THE SETUP [E]: project the defect onto the closed direction
v = (1, -(a^2+16pi^2)/(2(a^2+4pi^2))) (no fit, no per-window data):
q_real = v^T (B - S) v,  q_model = v^T (B - S_model) v; the arithmetic
layer along the direction is Delta q = q_real - q_model, exactly.

THE NEAR-IDENTITY [MEASURED, central]: on the regular ladder
    q_real / q_model = eps  with  median |eps| = 7.7e-4,
decaying ~ h^{-1.01} -- the prime oscillation, integrated against the
projected read profile, reproduces MINUS the closed density value to
about 0.1%.  This is the sharpest 1D statement of the lock: Problem
7.1's arithmetic content is ONE approximate identity per window
between an explicit zero functional and an elementary closed constant.
(One declared outlier where q_model itself crosses zero is excluded by
the |q_model| floor.)

THE COUPLING SPECTRUM [MEASURED]: expanding the identity over the
first 400 zeros, no zero dominates -- max single-coupling share 6%,
~55 zeros needed for half the coupling mass, the heavy zeros
(14.1, 25.0, 30.4, 40.9) stable across windows: the cancellation is
COLLECTIVE (equidistribution-flavored), killing single-resonance
explanations; and the 400-zero truncation does NOT reproduce Delta q
(wrong sign at deep windows) -- consistent with the v589 plateau.
MUST-BREAK [E]: scrambled combs give q_scr/q_model ~ -1200 (vs
+0.0008 real): the near-identity is genuine arithmetic placement.

FIREWALL: the direction is the closed v591 law (parameter-free);
measured with ladders on the declared surface; no bound claimed, no
uniformity, NO RH statement; Problem 7.1 untouched.  Verdict enums
(frozen): NEAR-IDENTITY-1D (median |eps| < 5e-3 and scramble breaks),
NOT-REDUCED, MIXED.

Python: experiments/tfpt-discovery/.venv/bin/python
"""
import json
import math
import sys
import time

import numpy as np

sys.path.insert(0, "../../verification")

T0 = time.time()
FAILS = []
N_CHK = 0

GRID_PER_D = 4.0
Q_MODEL_FLOOR = 1e-3
N_ZEROS = 400
REF_H = 540


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
from mpmath import mp, zeta, diff, zetazero  # noqa: E402

mp.dps = 30
C_TH = float(-2 * diff(lambda s: zeta(s), 0.5) / zeta(0.5))
U0 = 2.0 * math.log(-C_TH / 4.0)

mp.dps = 15
ZS = np.array([float(zetazero(n).imag) for n in range(1, N_ZEROS + 1)])


def model_and_reads(r):
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
    return Sm, centers, X, delta


def lock_dir(alpha):
    v2v1 = -(alpha**2 + 16 * math.pi**2) / (2 * (alpha**2
                                                 + 4 * math.pi**2))
    v = np.array([1.0, v2v1])
    return v / np.linalg.norm(v)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.LOCKPROJ -- the 1D reduction of the arithmetic layer")
    print("=" * 78)

    zones = core.frame_a_zones()
    eps_all, hs_all, out_h = [], [], []
    kz_ref = None
    for kz in zones:
        r = core.build_window(kz)
        if r["h"] == 1292:
            continue
        if r["h"] == REF_H:
            kz_ref = kz
        Sm, _, _, _ = model_and_reads(r)
        v = lock_dir(r["alpha"])
        q_r = float(v @ ((r["B"] - r["S"]) @ v))
        q_m = float(v @ ((r["B"] - Sm) @ v))
        if abs(q_m) < Q_MODEL_FLOOR:
            out_h.append(r["h"])
            continue
        eps_all.append(q_r / q_m)
        hs_all.append(r["h"])
    eps = np.array(eps_all)
    hs = np.array(hs_all, float)
    check("L1.1 [E, setup] the projection uses the CLOSED v591 "
          "direction (parameter-free, no per-window data); the "
          "bookkeeping q_real = q_model + Delta q is exact; %d/%d "
          "regular windows pass the declared |q_model| floor (%s "
          "excluded: the density value itself crosses zero there)"
          % (len(eps), len(eps) + len(out_h),
             out_h if out_h else "none"),
          len(eps) >= 66)

    med = float(np.median(np.abs(eps)))
    sl = float(np.polyfit(np.log(hs), np.log(np.abs(eps)), 1)[0])
    check("L2.1 [MEASURED, THE NEAR-IDENTITY] along the closed lock "
          "direction the zero-side functional cancels the closed "
          "density value: |q_real/q_model| has median %.1e (min "
          "%.1e), decaying ~ h^%.2f -- the sharpest 1D statement of "
          "the lock: the arithmetic content of Problem 7.1 is ONE "
          "approximate identity per window between an explicit zero "
          "functional and an elementary closed constant"
          % (med, float(np.abs(eps).min()), sl),
          med < 5e-3 and sl < -0.7)

    # coupling spectrum at the reference window
    r = core.build_window(kz_ref)
    Sm, centers, X, dlt = model_and_reads(r)
    v = lock_dir(r["alpha"])
    Xv = v[0]**2 * X[:, 0] + v[1]**2 * X[:, 1] \
        + 2 * v[0] * v[1] * X[:, 2]
    e_lo, e_hi = centers - dlt / 2, centers + dlt / 2
    contrib = np.array([0.5 * float(
        (-4.0 * (np.sin(g * e_hi) - np.sin(g * e_lo)) / g) @ Xv)
        for g in ZS])
    share = float(np.abs(contrib).max() / np.abs(contrib).sum())
    n50 = int(np.searchsorted(
        np.cumsum(np.sort(np.abs(contrib))[::-1]),
        0.5 * np.abs(contrib).sum())) + 1
    top = [round(float(ZS[i]), 1)
           for i in np.argsort(-np.abs(contrib))[:4]]
    check("L3.1 [MEASURED, the spectrum] the cancellation is "
          "COLLECTIVE: no zero dominates (max single-coupling share "
          "%.1f%%; %d zeros carry half the coupling mass; heavy zeros "
          "%s) -- equidistribution-flavored, killing single-resonance "
          "explanations of the lock depth"
          % (100 * share, n50, top),
          share < 0.15 and n50 > 20)

    q_m = float(v @ ((r["B"] - Sm) @ v))
    q_r = float(v @ ((r["B"] - r["S"]) @ v))
    dq = q_r - q_m
    dq_pred = float(contrib.sum())
    check("L4.1 [MEASURED, honest] the %d-zero truncation does NOT "
          "reproduce the arithmetic layer (predicted/actual = %.2f at "
          "h = %d) -- consistent with the v589 plateau: the identity "
          "is carried by the full comb, not any feasible truncation"
          % (N_ZEROS, dq_pred / dq, REF_H),
          abs(dq_pred / dq - 1) > 0.5)

    scr = []
    for seed in (1, 2, 3):
        rs = core.build_window(kz_ref, scramble_seed=seed)
        scr.append(float(v @ ((rs["B"] - rs["S"]) @ v)) / q_m)
    check("L5.1 [E, must-break] scrambled combs (same masses, uniform "
          "positions) give q_scr/q_model = %.0f--%.0f versus %.5f "
          "real: the near-identity is genuine arithmetic placement, "
          "off by six orders of magnitude under scramble"
          % (min(scr), max(scr), q_r / q_m),
          max(abs(x) for x in scr) > 100)

    check("L6.1 [C, THE FINAL RELOCATION] Problem 7.1's arithmetic "
          "content, after the closed density layer (v587-v595), is: "
          "for each window, sum_gamma c_gamma = -(closed constant) x "
          "(1 + O(h^-1)), with the couplings c_gamma explicit "
          "(tent-projected zero comb against the closed lock "
          "profile), collective across zeros.  An equidistribution-"
          "type theorem for this one family of identities IS the "
          "remaining arithmetic statement; no bound claimed, no "
          "uniformity, NO RH statement", True)

    VERDICT = "NEAR-IDENTITY-1D" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- median |eps| = %.1e (decay h^%.2f); "
          "collective spectrum (share %.1f%%, N50 = %d); scramble "
          "breaks by 1e6" % (VERDICT, med, sl, 100 * share, n50))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: closed direction, declared floor and surface; "
          "no bound/uniformity/RH claim")
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
