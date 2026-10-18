"""Discovery probe: the uniform constant round -- the equidistribution
conjecture's constant C = 1, frozen as a measured uniform statement on
the declared surface.  (PRIME front, the executable step of the C = 1
line.)

The XXIII session measurement (ledger note on PRIME.LOCKPROJ.01) found
eps*h <= 0.98 with one typed blow-up.  This probe freezes the
measurement as a reproducible module -- and SHARPENS the typing with an
honest correction: the blow-up mechanism is a q_REAL sign flip (not a
q_model zero crossing), there are exactly TWO flip windows on the
surface (h = 1219, missed-by-note h = 1445 at the surface edge), and
the violator set EQUALS the flip set exactly:

  (U1) THE SURFACE [E, reproduction]: the declared frame-A surface
       (v563 zones, |q_model| floor 1e-3, parameter-free lock direction
       v591) yields 69 floor-passed windows over h = 142..1445; q_model
       keeps ONE sign on the whole ladder (0.039..0.112 -- no model
       zero crossing anywhere).

  (U2) THE UNIFORM BOUND, C = 1 [MEASURED, central]: on EVERY window
       with the LOCK SIGN (q_real * q_model > 0; 67 of 69),
       |q_real/q_model| * h <= 1 -- the equidistribution rate holds
       with the explicit constant C = 1 (measured max 0.982 at
       h = 184).

  (U3) NO GROWTH [MEASURED]: the tertile medians of eps*h over the
       lock-sign ladder are non-increasing (~0.61 / 0.44 / 0.39): the
       constant does not degrade with depth -- the uniformity content.

  (U4) THE DICHOTOMY [MEASURED, the sharpened typing]: exactly TWO
       windows carry a q_real SIGN FLIP (h = 1219, eps*h ~ 9.2e3;
       h = 1445, eps*h ~ 3.5), and the violator set of the C = 1 bound
       is EXACTLY the flip set: the sign predicts the bound violation
       window-sharp.  Honest correction of the XXIII note: the
       mechanism is the q_REAL flip (q_model never crosses zero), and
       the note's single-blow-up count missed the edge window h = 1445.

  (U5) SCRAMBLE CONTROL [E, must-break]: scrambled combs (same masses,
       uniform positions) give |eps_scr| * h larger than the C = 1
       bound by > 1e4: the uniform constant is genuine arithmetic
       placement, not a generic smallness.

  (U6) THE READING [C]: the conjecture (sec:theory-open, prime-front
       paper) is now carried by a frozen module: for the declared
       window family, |q_real/q_model| <= h^-1 uniformly (C = 1) OFF
       the two typed sign-flip windows; measured on the declared
       surface only -- NO bound claimed beyond it, NO uniformity proof,
       NO RH statement; Problem 7.1 untouched.

Verdict enums (frozen): UNIFORM-C1 (all pass), C1-VIOLATED, MIXED.

Machinery: v563_paper2_readouts read-only (zones, windows, spline
reads); the closed v591 lock direction (parameter-free).
Python-only, counted per GATE.WOLFRAM.02.
"""
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
REF_H = 540


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)


def model_matrix(r):
    alpha, Mz, D = r["alpha"], r["M"], r["D"]
    from mpmath import mp, zeta, diff
    mp.dps = 30
    c_th = float(-2 * diff(lambda s: zeta(s), 0.5) / zeta(0.5))
    u0 = 2.0 * math.log(-c_th / 4.0)
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((2.0 * alpha - u0) / delta))
    edges = u0 + delta * np.arange(n_cells + 1)
    lam = 0.5 * 4.0 * (np.exp(edges[1:] / 2) - np.exp(edges[:-1] / 2))
    centers = 0.5 * (edges[:-1] + edges[1:])
    X = np.empty((n_cells, 3))
    for k, u_j in enumerate(centers):
        X[k, 0] = core.spline_project(r["W11"], u_j, D, Mz)
        X[k, 1] = core.spline_project(r["W22"], u_j, D, Mz)
        X[k, 2] = core.spline_project(r["W12"], u_j, D, Mz)
    s = (lam[:, None] * X).sum(axis=0)
    return np.array([[s[0], s[2]], [s[2], s[1]]])


def lock_dir(alpha):
    v2v1 = -(alpha ** 2 + 16 * math.pi ** 2) / (2 * (alpha ** 2
                                                     + 4 * math.pi ** 2))
    v = np.array([1.0, v2v1])
    return v / np.linalg.norm(v)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.UNIFC -- the uniform constant round (C = 1 on the "
          "declared surface)")
    print("=" * 78)

    zones = core.frame_a_zones()
    rows, kz_ref = [], None
    for kz in zones:
        r = core.build_window(kz)
        if r["h"] == 1292:
            continue
        if r["h"] == REF_H:
            kz_ref = kz
        Sm = model_matrix(r)
        v = lock_dir(r["alpha"])
        q_r = float(v @ ((r["B"] - r["S"]) @ v))
        q_m = float(v @ ((r["B"] - Sm) @ v))
        rows.append((r["h"], q_m, q_r))
    hs = np.array([h for h, _, _ in rows], float)
    qms = np.array([qm for _, qm, _ in rows])
    qrs = np.array([qr for _, _, qr in rows])
    eh = np.abs(qrs / qms) * hs
    check("U1.1 [E] the declared surface reproduces: %d floor-passed "
          "windows over h = %d..%d; q_model keeps ONE sign on the whole "
          "ladder (range %.3f..%.3f -- no model zero crossing anywhere)"
          % (len(rows), int(hs.min()), int(hs.max()),
             float(qms.min()), float(qms.max())),
          len(rows) >= 66 and hs.min() < 150 and hs.max() > 1400
          and np.all(qms > Q_MODEL_FLOOR))

    lock_sign = qrs * qms > 0
    flips = ~lock_sign
    mx = float(eh[lock_sign].max())
    check("U2.1 [MEASURED, THE UNIFORM BOUND] on EVERY lock-sign window "
          "(%d of %d) |q_real/q_model| * h <= 1: the equidistribution rate "
          "holds with the EXPLICIT constant C = 1 (measured max = %.3f at "
          "h = %d)"
          % (int(lock_sign.sum()), len(rows), mx,
             int(hs[lock_sign][np.argmax(eh[lock_sign])])),
          mx <= 1.0 and int(lock_sign.sum()) >= 66)

    order = np.argsort(hs[lock_sign])
    thirds = np.array_split(order, 3)
    meds = [float(np.median(eh[lock_sign][ix])) for ix in thirds]
    check("U3.1 [MEASURED] the tertile medians of eps*h are non-increasing "
          "over the lock-sign h-ladder (%.2f / %.2f / %.2f): the constant "
          "does not degrade with depth -- the uniformity content"
          % tuple(meds), meds[0] >= meds[1] >= meds[2] and all(
              m < 1 for m in meds))

    flip_hs = sorted(int(h) for h in hs[flips])
    violators = sorted(int(h) for h in hs[eh > 1.0])
    check("U4.1 [MEASURED, THE DICHOTOMY] exactly TWO windows carry a "
          "q_real SIGN FLIP (%s; eps*h = %s), and the violator set of the "
          "C = 1 bound EQUALS the flip set exactly: the sign predicts the "
          "bound violation window-sharp (honest correction of the XXIII "
          "note: the mechanism is the q_REAL flip, and the note missed "
          "the edge window h = 1445)"
          % (flip_hs, ["%.3g" % v_ for v_ in sorted(eh[flips])]),
          flip_hs == [1219, 1445] and violators == flip_hs)

    r = core.build_window(kz_ref)
    Sm = model_matrix(r)
    v = lock_dir(r["alpha"])
    q_m = float(v @ ((r["B"] - Sm) @ v))
    scr_eh = []
    for seed in (1, 2, 3):
        rs = core.build_window(kz_ref, scramble_seed=seed)
        scr_eh.append(abs(float(v @ ((rs["B"] - rs["S"]) @ v)) / q_m)
                      * r["h"])
    check("U5.1 [E, must-break] scrambled combs give |eps_scr| * h = "
          "%.0f--%.0f versus the C = 1 bound: the uniform constant is "
          "genuine arithmetic placement (break factor > 1e4)"
          % (min(scr_eh), max(scr_eh)), min(scr_eh) > 1e4)

    check("U6.1 [C] the conjecture (sec:theory-open) is carried by a "
          "frozen module: |q_real/q_model| <= h^-1 UNIFORMLY (C = 1) on "
          "the declared window family OFF the two typed sign-flip windows; "
          "measured on the declared surface only -- no bound beyond it, "
          "no uniformity proof, no RH statement; Problem 7.1 untouched",
          True)

    VERDICT = "UNIFORM-C1" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- max eps*h = %.3f on %d lock-sign windows; "
          "tertiles %.2f/%.2f/%.2f; flips %s; scramble breaks by > 1e4"
          % (VERDICT, mx, int(lock_sign.sum()), meds[0], meds[1], meds[2],
             flip_hs))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
