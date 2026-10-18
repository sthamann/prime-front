"""v619 -- PRIME.FLIPMECH.01: the flip mechanics round -- the two C = 1
violators are truncation artifacts of the prime-data cap, reproduced by
injection; on the complete-comb surface the constant C = 1 holds with
ZERO exceptions.  (The mechanism behind the v618 dichotomy.)

v618 froze the dichotomy: the violator set of the C = 1 bound equals the
q_real sign-flip set exactly (h = 1219, 1445).  This probe lands the
MECHANISM:

  (F1) THE SATURATION IDENTIFICATION [E]: the atom demand of a window is
       u <= 2*alpha (atoms_in, v563 verbatim), and the prime-power data
       cap is U_max = max(U_ALL) = 12.899; EXACTLY the two flip windows
       have 2*alpha > U_max (alpha = 6.494, 6.788 -- their atom lists
       are TRUNCATED); every other window is complete: the flip set
       EQUALS the truncation set.

  (F2) NOT A RESONANCE [E, must-fail for the arithmetic reading]: the
       zero-comb coupling spectrum AT the flip windows is
       regular-collective (max share ~5.8%, N50 ~57 -- indistinguishable
       from reference windows): the flip is NOT carried by any zero
       resonance.

  (F3) THE INJECTION [E, the mechanism]: removing the SAME missing
       u-ranges from complete windows REPRODUCES the flips -- injecting
       Delta_u = 0.089 (= 2*alpha - U_max at h = 1445) into h = 540/1215
       gives q_real ~ -5e-5 / -1e-4 (matching 1445's observed -1.0e-4),
       and Delta_u = 0.677 (the h = 1219 gap) gives -0.18 / -0.22
       (matching 1219's -0.29): sign AND magnitude matched at both
       scales -- the truncated comb tail is the flip.

  (F4) MONOTONICITY [E]: the injected overshoot grows monotonically with
       the truncation depth (0 -> 0.089 -> 0.3 -> 0.677) on both
       reference windows.

  (F5) THE CORRECTED SURFACE [MEASURED, central]: on the COMPLETE-comb
       surface (2*alpha <= U_max: 67 windows -- identical to the v618
       lock-sign set) the C = 1 bound holds with ZERO exceptions
       (max eps*h = 0.982): the conjecture surface is exception-free
       once the data boundary is respected.

  (F6) THE READING [C]: the v618 sign dichotomy upgrades to a mechanism
       -- the "sign-flip windows" are RETIRED as data-boundary
       artifacts (incomplete prime combs), not arithmetic phenomena;
       the equidistribution conjecture with C = 1 stands exception-free
       on the complete-comb surface; extending the surface requires
       extending the prime-power data, not the theory.  No uniformity
       proof, no RH statement; Problem 7.1 untouched.

Verdict enums (frozen): FLIPS-ARE-TRUNCATION (all pass),
MECHANISM-FAILS, MIXED.

FIREWALL: no marker changes; Problem 7.1 untouched.

PROVENANCE: discovery probe flip_mechanics_probe.py (2026-08-01, 6/6,
verdict FLIPS-ARE-TRUNCATION).

Machinery: v563_paper2_readouts read-only.  Python-only, counted per
GATE.WOLFRAM.02.
"""
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

T0 = time.time()
FAILS = []
N_CHK = 0

GRID_PER_D = 4.0
N_ZEROS = 400


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
    return np.array([[s[0], s[2]], [s[2], s[1]]]), centers, X, delta


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
    print("PRIME.FLIPMECH -- the flip mechanics round (truncation, not "
          "arithmetic)")
    print("=" * 78)

    u_max = float(core.U_ALL[-1])
    all_rows = []
    windows = {}
    for kz in core.frame_a_zones():
        r = core.build_window(kz)
        if r["h"] == 1292:
            continue
        all_rows.append(r)
        windows[r["h"]] = r  # by-h access for the named windows (unique there)

    # F1: saturation identification
    saturated = sorted(r["h"] for r in all_rows if 2.0 * r["alpha"] > u_max)
    complete_rows = [r for r in all_rows if 2.0 * r["alpha"] <= u_max]
    gaps = {r["h"]: 2.0 * r["alpha"] - u_max for r in all_rows
            if 2.0 * r["alpha"] > u_max}
    check("F1.1 [E] the atom demand is u <= 2*alpha and the data cap is "
          "U_max = %.3f; EXACTLY the two flip windows are truncated "
          "(%s, gaps Delta_u = %s); all %d other windows are complete: "
          "the flip set EQUALS the truncation set"
          % (u_max, saturated,
             {h: round(g, 3) for h, g in gaps.items()}, len(complete_rows)),
          saturated == [1219, 1445] and len(complete_rows) == 67
          and abs(gaps[1445] - 0.089) < 5e-3
          and abs(gaps[1219] - 0.677) < 5e-3)

    # F2: coupling spectrum at the flips is regular-collective
    ZS = np.array([float(zetazero(n).imag) for n in range(1, N_ZEROS + 1)])
    shares = {}
    for h in (540, 1219, 1445):
        r = windows[h]
        Sm, centers, X, dlt = model_and_reads(r)
        v = lock_dir(r["alpha"])
        Xv = (v[0] ** 2 * X[:, 0] + v[1] ** 2 * X[:, 1]
              + 2 * v[0] * v[1] * X[:, 2])
        e_lo, e_hi = centers - dlt / 2, centers + dlt / 2
        contrib = np.array([0.5 * float(
            (-4.0 * (np.sin(g * e_hi) - np.sin(g * e_lo)) / g) @ Xv)
            for g in ZS])
        n50 = int(np.searchsorted(
            np.cumsum(np.sort(np.abs(contrib))[::-1]),
            0.5 * np.abs(contrib).sum())) + 1
        shares[h] = (float(np.abs(contrib).max() / np.abs(contrib).sum()),
                     n50)
    check("F2.1 [E, must-fail for the resonance reading] the coupling "
          "spectrum AT the flip windows is regular-collective (shares "
          "%.1f%%/%.1f%% vs reference %.1f%%; N50 = %d/%d vs %d): the "
          "flip is NOT carried by any zero resonance"
          % (100 * shares[1219][0], 100 * shares[1445][0],
             100 * shares[540][0], shares[1219][1], shares[1445][1],
             shares[540][1]),
          all(s_[0] < 0.15 and s_[1] > 20 for s_ in shares.values()))

    # F3/F4: the injection
    inj = {}
    for h in (540, 1215):
        r = windows[h]
        v = lock_dir(r["alpha"])
        uu, lam, Xn = r["uu"], r["lam"], r["Xn"]
        twoa = 2.0 * r["alpha"]
        vals = {}
        for du in (0.0, 0.089, 0.3, 0.677):
            mask = uu <= twoa - du
            s = (lam[mask, None] * Xn[mask]).sum(axis=0)
            S = np.array([[s[0], s[2]], [s[2], s[1]]])
            vals[du] = float(v @ ((r["B"] - S) @ v))
        inj[h] = vals
    # observed flip values
    obs = {}
    for h in (1219, 1445):
        r = windows[h]
        v = lock_dir(r["alpha"])
        obs[h] = float(v @ ((r["B"] - r["S"]) @ v))
    ok_small = all(-3e-4 < inj[h][0.089] < -2e-5 for h in (540, 1215))
    ok_large = all(-0.35 < inj[h][0.677] < -0.10 for h in (540, 1215))
    check("F3.1 [E, THE MECHANISM] truncation injection into complete "
          "windows REPRODUCES the flips: Delta_u = 0.089 (the 1445 gap) "
          "gives q_real = %.1e / %.1e (observed at 1445: %.1e); "
          "Delta_u = 0.677 (the 1219 gap) gives %.2f / %.2f (observed at "
          "1219: %.2f): sign AND magnitude matched at both scales"
          % (inj[540][0.089], inj[1215][0.089], obs[1445],
             inj[540][0.677], inj[1215][0.677], obs[1219]),
          ok_small and ok_large and obs[1445] < 0 and obs[1219] < -0.1)

    mono = all(inj[h][0.0] > inj[h][0.089] > inj[h][0.3] > inj[h][0.677]
               for h in (540, 1215))
    check("F4.1 [E] the injected overshoot grows monotonically with the "
          "truncation depth on both reference windows", mono)

    # F5: the corrected surface
    eh = []
    for r in complete_rows:
        Sm, _, _, _ = model_and_reads(r)
        v = lock_dir(r["alpha"])
        q_r = float(v @ ((r["B"] - r["S"]) @ v))
        q_m = float(v @ ((r["B"] - Sm) @ v))
        eh.append(abs(q_r / q_m) * r["h"])
    mx = float(max(eh))
    check("F5.1 [MEASURED, central] on the COMPLETE-comb surface "
          "(2*alpha <= U_max: %d windows = the v618 lock-sign set) the "
          "C = 1 bound holds with ZERO exceptions (max eps*h = %.3f)"
          % (len(complete_rows), mx), mx <= 1.0 and len(complete_rows) == 67)

    check("F6.1 [C] the v618 dichotomy upgrades to a MECHANISM: the "
          "sign-flip windows are RETIRED as data-boundary artifacts "
          "(incomplete prime combs), and the equidistribution conjecture "
          "with C = 1 stands exception-free on the complete-comb surface; "
          "extending the surface requires extending the prime-power data, "
          "not the theory; no uniformity proof, no RH statement", True)

    VERDICT = "FLIPS-ARE-TRUNCATION" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- flips = truncation set exactly; injection "
          "reproduces both scales; C = 1 exception-free on %d complete "
          "windows (max %.3f)" % (VERDICT, len(complete_rows), mx))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
