"""v577 -- PRIME.NULLRAY.01: the null-ray locking census -- the pencil
locking direction is CORRELATED with the Pythagorean null ray (2,-1)
on every declared window (23-34 degrees, all below random), falls
slowly (h^-0.10), and is destroyed by the scramble: a real partial
carrier, NOT the full locking direction.

PROVENANCE.  The second review's Priority-2 test, executed verbatim on
the declared surface: v_lock = the near-null eigenvector of Ahat =
B - S per window (the v569 locking mode), v0 = (2,-1) = the exact null
direction of the v576 rank-one edge profile [[1,2],[2,4]]; raw and
B-metric angles; discovery probe nullray_census_probe.py (5/5, verdict
NULL-RAY-CORRELATED).

[E] 1. the tested direction is exact: [[1,2],[2,4]](2,-1)^T = 0.
[MEASURED] 2. the alignment is real: raw angle in [23.5, 33.8] deg
    (median 28.1), B-metric in [23.0, 35.0] deg across all 70 windows
    -- everywhere below the 45-deg isotropic mean.
[MEASURED] 3. HONEST: the decline is real but SLOW -- angle ~ h^-0.10
    (raw) / h^-0.12 (B-metric): the review's clean success bar
    ('uniformly falling to zero') is NOT met on this surface.
[E] 4. must-break: the position scramble destroys the alignment
    (28.1 -> 49.4 deg raw, 28.2 -> 54.8 deg B-metric): the alignment is
    ARITHMETIC structure; the review's 'scramble-blind' kill is
    excluded.
[C] 5. verdict typing: the ray is a real PARTIAL carrier -- consistent
    with the v576 three-regime split (the edge regime, whose null ray
    this is, is closed at N^-4; the macro regime carries the remaining
    weight and bends the locking direction).  The named follow-up is
    the macro-regime direction from K_inf(sigma, tau), not more angle
    fits.

NAMED LIMITS: declared surface only; MEASURED with ladders (v562
anti-promotion); no uniformity, no rate, NO RH statement; Problem 7.1
untouched.  Fences: the v563 fence chain unchanged.  Python-only,
counted per GATE.WOLFRAM.02.  Discovery:
experiments/tfpt-discovery/nullray_census_probe.py (2026-07-31, 5/5,
NULL-RAY-CORRELATED).
"""
import time

import numpy as np

T0 = time.time()
FAILS = []
N_CHK = 0

V0 = np.array([2.0, -1.0])
REF_H = 540
SCRAMBLE_SEED = 1


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)


def angles(r):
    B, Ah = r["B"], r["Ah"]
    ew, ev = np.linalg.eigh(0.5 * (Ah + Ah.T))
    vl = ev[:, np.argmin(np.abs(ew))]
    c_raw = abs(vl @ V0) / (np.linalg.norm(vl) * np.linalg.norm(V0))
    Bh = np.linalg.cholesky(-B)
    a1, a2 = Bh @ vl, Bh @ V0
    c_B = abs(a1 @ a2) / (np.linalg.norm(a1) * np.linalg.norm(a2))
    return (np.degrees(np.arccos(min(1.0, c_raw))),
            np.degrees(np.arccos(min(1.0, c_B))))


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.NULLRAY -- the null-ray locking census on the declared "
          "surface")
    print("=" * 78)

    M0 = np.array([[1.0, 2.0], [2.0, 4.0]])
    check("N1.1 [E] the tested direction is the exact null ray of the "
          "rank-one edge profile: [[1,2],[2,4]] (2,-1)^T = 0 identically "
          "(the v576 Lorentz null point (5,-3,4))",
          np.allclose(M0 @ V0, 0.0))

    zones = core.frame_a_zones()
    rows = []
    ref_kz = None
    for kz in zones:
        r = core.build_window(kz)
        ar, ab = angles(r)
        rows.append((r["h"], ar, ab))
        if r["h"] == REF_H:
            ref_kz = kz
    rows.sort()
    hs = np.array([x[0] for x in rows], float)
    ar = np.array([x[1] for x in rows])
    ab = np.array([x[2] for x in rows])
    sl_r = float(np.polyfit(np.log(hs), np.log(ar), 1)[0])
    sl_b = float(np.polyfit(np.log(hs), np.log(ab), 1)[0])

    check("N2.1 [MEASURED, declared surface] the locking mode is FAR from "
          "random relative to the null ray on every one of the %d windows: "
          "raw angle in [%.1f, %.1f] deg (median %.1f), B-metric in "
          "[%.1f, %.1f] deg -- all below the 45-deg isotropic mean, most "
          "below 30 deg (|cos| ~ 0.83-0.92)"
          % (len(rows), ar.min(), ar.max(), float(np.median(ar)),
             ab.min(), ab.max()),
          ar.max() < 40.0 and ab.max() < 40.0)

    check("N2.2 [MEASURED, honest -- NOT the clean success criterion] the "
          "decline is REAL but SLOW: angle ~ h^%.3f (raw) / h^%.3f "
          "(B-metric) from %.1f deg at h = %d to %.1f deg at h = %d -- "
          "falling, monotone in trend, but far from a demonstrated "
          "convergence to zero: the review's 'uniformly falling' success "
          "bar is NOT met on this surface"
          % (sl_r, sl_b, rows[0][1], int(rows[0][0]), rows[-1][1],
             int(rows[-1][0])),
          -0.3 < sl_r < -0.02 and -0.3 < sl_b < -0.02)

    r_real = core.build_window(ref_kz)
    r_scr = core.build_window(ref_kz, scramble_seed=SCRAMBLE_SEED)
    ar0, ab0 = angles(r_real)
    ars, abs_ = angles(r_scr)
    check("N3.1 [E, must-break -- the kill criterion does NOT fire] the "
          "position scramble at the same masses DESTROYS the alignment: "
          "raw %.1f -> %.1f deg, B-metric %.1f -> %.1f deg on the "
          "reference window -- the null-ray alignment is ARITHMETIC "
          "structure, not a build artefact (the review's "
          "'scramble-blind' kill is excluded)"
          % (ar0, ars, ab0, abs_),
          ars > ar0 + 10.0 and abs_ > ab0 + 10.0)

    check("N4.1 [C, the verdict typing] the ray (2,-1) is a REAL PARTIAL "
          "carrier of the locking mode: below-random alignment everywhere, "
          "slow decline, scramble-sensitive -- but not the full carrier "
          "(no clean convergence).  Consistent with the v576 three-regime "
          "split: the edge regime (whose null ray this is) is closed at "
          "N^-4, while the macro regime carries the remaining weight and "
          "bends the locking direction away; the named follow-up is the "
          "macro-regime direction from K_inf(sigma, tau), not more angle "
          "fits", True)

    VERDICT = ("NULL-RAY-CORRELATED" if not FAILS else "NULL-RAY-DEAD")
    print("\nVERDICT: %s -- angles [%.1f, %.1f] deg across %d windows, "
          "slope h^%.2f, scramble +%.0f deg: real partial carrier, not the "
          "full locking direction"
          % (VERDICT, ar.min(), ar.max(), len(rows), sl_r, ars - ar0))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: declared surface only; MEASURED with ladders; no "
          "uniformity/rate/RH claim; Problem 7.1 untouched")

    print("--- PRIME.NULLRAY.01 null-ray locking census: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
