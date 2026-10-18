#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""screwind_meshdrift_check -- companion diagnostic to
screwind_induction_probe (PRIME.SCREW.INDUCTION.01).

EXPLORATION ONLY.  Writes nothing, no RH claim, no gate of the main
probe is moved.  QUESTION SETTLED HERE: the frozen run measured the
windowed E-rates kappa(u) FALLING (0.333/0.224/0.127/0.092 at delta =
0.006) -- is the drift intrinsic to the screw accelerant or a
mesh-resolution effect?  PREDICTION IF MESH-DRIVEN: the drop onsets at
the first multi-atom tent bin u_mix(delta) (5.549 at delta = 0.006,
6.735 at delta = 0.003), so at the finer mesh the rate must stay high
LONGER.  Two typed checks:
  C1 ORDERING: the last window before the measured rate falls below
     60 percent of the resolved-regime rate starts LATER (in u) at
     delta = 0.003 than at delta = 0.006.
  C2 RESOLVED-REGIME STABILITY: kappa fitted on [1.2, u_mix - 0.2]
     agrees across the two meshes within 0.06 absolute.
Also printed: the resolved-regime kappa vs the main probe's net-spike
slope s_kick + 1/2 (the kick-decay law re-read with the resolved
rate), and per-window tables for both meshes.
"""

from __future__ import annotations

import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import screwind_induction_probe as SI  # noqa: E402

T0 = time.time()
WINDOWS = ((1.2, 2.4), (2.4, 3.6), (3.6, 4.8), (4.8, 5.5), (5.5, 6.6),
           (6.6, 7.4), (7.4, 8.4), (8.4, 9.0))
U_MIX = {"0.006": 5.5491, "0.003": 6.7346}
DROP_FRAC = 0.60
C2_TOL = 0.06
S_KICK_MAIN = -0.1626


def windowed(dl: float, dens: np.ndarray) -> dict:
    n = len(dens)
    u = (np.arange(n) + 1) * dl
    ln_e = np.log(dens)
    out = {}
    for wl, wh in WINDOWS:
        i0, i1 = int(wl / dl), min(int(wh / dl), n)
        if i1 - i0 > 20:
            s, _ = SI.ols(u[i0:i1], ln_e[i0:i1])
            out[(wl, wh)] = -s
    return out


def main() -> int:
    print("=" * 78)
    print("screwind_meshdrift_check  (companion to PRIME.SCREW."
          "INDUCTION.01)")
    print("=" * 78)
    SI.setup_constants()
    atoms = SI.atom_table(9.0)
    results = {}
    for dtext, dl, n in (("0.006", 0.006, 1500), ("0.003", 0.003, 3000)):
        t0 = time.time()
        base = np.array([float(v) for v in SI.lag_row_from_g(
            SI.base_g_values(n, dtext), dtext)])
        row = SI.comb_row(base, [(a[2], a[3]) for a in atoms
                                 if a[2] < n * dl - 1e-12], n, dl)
        res = SI.levinson_rec(row)
        assert res["ok"], "stream must complete (matches frozen run)"
        dens = res["dens"]
        tab = windowed(dl, dens)
        umix = U_MIX[dtext]
        nres = int((umix - 0.2) / dl)
        i0 = int(1.2 / dl)
        uu = (np.arange(len(dens)) + 1) * dl
        s, _ = SI.ols(uu[i0:nres], np.log(dens[i0:nres]))
        results[dtext] = {"tab": tab, "k_res": -s}
        print("\n  delta=%s (n=%d, build+run %.1f s):  resolved-regime"
              " kappa on [1.2, %.2f) = %.4f"
              % (dtext, n, time.time() - t0, umix - 0.2, -s))
        for (wl, wh), kv in tab.items():
            marker = " <-- u_mix=%.3f in this window" % umix \
                if wl <= umix < wh else ""
            print("    [%4.1f,%4.1f)  kappa = %.4f%s" % (wl, wh, kv,
                                                         marker))

    def drop_onset(dtext: str) -> float:
        k_res = results[dtext]["k_res"]
        for (wl, wh), kv in results[dtext]["tab"].items():
            if kv < DROP_FRAC * k_res:
                return wl
        return 9.0

    on6, on3 = drop_onset("0.006"), drop_onset("0.003")
    c1 = on3 > on6
    print("\n  C1 drop onset (first window with kappa < %.2f *"
          " resolved): delta=0.006 at u=%.1f, delta=0.003 at u=%.1f"
          % (DROP_FRAC, on6, on3))
    print("  [%s] C1 ordering: finer mesh holds the rate longer =>"
          " drift is MESH-RESOLUTION-DRIVEN" % ("PASS" if c1 else
                                                "FAIL"))
    k6, k3 = results["0.006"]["k_res"], results["0.003"]["k_res"]
    c2 = abs(k6 - k3) <= C2_TOL
    print("  [%s] C2 resolved-regime kappa mesh-stable: %.4f vs %.4f"
          " (|diff| = %.4f, tol %.2f)"
          % ("PASS" if c2 else "FAIL", k6, k3, abs(k6 - k3), C2_TOL))
    print("  kick-decay law re-read: s_kick + 1/2 = %.4f vs resolved"
          " kappa %.4f (main-probe global kappa was 0.1776)"
          % (S_KICK_MAIN + 0.5, k6))
    print("\n  runtime %.1f s" % (time.time() - T0))
    print("EXPLORATION ONLY.  NO RH CLAIM.")
    print("=" * 78)
    return 0 if (c1 and c2) else 1


if __name__ == "__main__":
    raise SystemExit(main())
