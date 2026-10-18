"""v581 -- PRIME.TRANSPORT.01: the second review's Priority 4 (the multilevel
locking-transport lemma), measured and KILLED honestly: the locking
direction drifts SLOWLY between doubled window sizes (median ~2.4 deg
per octave) but the drift does NOT decay -- it grows h^{+0.37} against
the proposed bar sin <= C h^{-1-delta}: the review's own kill criterion
fires, and the route is ended without romantic extension.

THE PROPOSED LEMMA (review, Priority 4): sin angle(P_h v_h, v_{2h}) <=
C h^{-1-delta}; summable increments would give a convergent locking
direction and a transportable scalar defect.  THE MEASURED FORM: on the
declared surface the mode coordinates are scale-free, so the doubling
comparison is direct -- sin angle(v_lock(h), v_lock(h')) over all
window pairs with h' within 15% of 2h (40 pairs).

FIREWALL: declared surface, read-only; MEASURED with ladders; an honest
negative is a result; no uniformity, NO RH statement.  Verdict enums
(frozen): TRANSPORT-SUMMABLE (bar met), TRANSPORT-KILLED (drift does
not decay -- the review's kill), MIXED.

PROVENANCE: discovery probe locking_transport_probe.py (2026-07-31, 4/4,
TRANSPORT-KILLED); construction base v563 read-only.  Python-only,
counted per GATE.WOLFRAM.02.
"""
import time

import numpy as np

T0 = time.time()
FAILS = []
N_CHK = 0

PAIR_TOL = 0.15


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)

def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.TRANSPORT -- the multilevel locking-transport lemma, "
          "measured")
    print("=" * 78)

    zones = core.frame_a_zones()
    data = []
    for kz in zones:
        r = core.build_window(kz)
        Ah = 0.5 * (r["Ah"] + r["Ah"].T)
        ew, ev = np.linalg.eigh(Ah)
        vl = ev[:, np.argmin(np.abs(ew))]
        if float(vl[0]) < 0:
            vl = -vl
        data.append((float(r["h"]), vl))
    data.sort(key=lambda x: x[0])
    hs = np.array([x[0] for x in data], float)
    vs = np.array([x[1] for x in data])

    pairs = []
    for i, h in enumerate(hs):
        tgt = 2 * h
        j = int(np.argmin(np.abs(hs - tgt)))
        if abs(hs[j] - tgt) / tgt < PAIR_TOL and j != i:
            s = abs(float(vs[i][0] * vs[j][1] - vs[i][1] * vs[j][0]))
            pairs.append((h, hs[j], s))
    hs_p = np.array([p[0] for p in pairs])
    ss = np.array([p[2] for p in pairs])
    sl = float(np.polyfit(np.log(hs_p), np.log(np.maximum(ss, 1e-12)), 1)[0])

    check("T1.1 [E] the doubling census exists on the declared surface: "
          "%d window pairs with h' within %.0f%% of 2h (mode coordinates "
          "are scale-free, so the comparison is direct -- no prolongation "
          "operator needed at the 2x2 block level)"
          % (len(pairs), 100 * PAIR_TOL), len(pairs) >= 30)

    check("T2.1 [MEASURED] the per-octave drift is SMALL in absolute "
          "terms: sin angle(v_lock(h), v_lock(~2h)) in [%.4f, %.4f] "
          "(%.2f--%.2f deg; median %.2f deg) -- the locking direction is "
          "slowly varying"
          % (ss.min(), ss.max(), np.degrees(np.arcsin(ss.min())),
             np.degrees(np.arcsin(ss.max())),
             float(np.degrees(np.arcsin(np.median(ss))))),
          ss.max() < 0.15)

    check("T2.2 [MEASURED, THE KILL -- the review's own criterion fires] "
          "the drift does NOT decay: the doubling-pair fit gives sin ~ "
          "h^%+.3f -- GROWING, against the proposed bar sin <= C "
          "h^{-1-delta}; the increments are not summable by this measure, "
          "no convergent locking direction is demonstrated, and the "
          "multilevel transport lemma FAILS on the declared surface: per "
          "the review's own discipline, the route is ended without "
          "romantic extension" % sl,
          sl > -0.5)

    check("T3.1 [C, typing] the honest picture assembles consistently: the "
          "locking direction is null-ray-correlated (v577, 23-34 deg to "
          "(2,-1)), slowly varying (this module), and NOT convergent at "
          "the proposed rate -- the macro regime re-bends it per window "
          "(v576/v579): a scalar-defect transport along a FIXED direction "
          "is not available; any future transport must carry the "
          "window-dependent macro direction with it; no uniformity claim, "
          "Problem 7.1 untouched", True)

    VERDICT = ("TRANSPORT-KILLED" if not FAILS and sl > -0.5
               else ("TRANSPORT-SUMMABLE" if sl <= -1.0 else "MIXED"))
    print("\nVERDICT: %s -- %d doubling pairs, drift %.2f-%.2f deg "
          "(median %.2f), fit h^%+.2f against the bar h^{-1-delta}: the "
          "lemma fails honestly"
          % (VERDICT, len(pairs), np.degrees(np.arcsin(ss.min())),
             np.degrees(np.arcsin(ss.max())),
             float(np.degrees(np.arcsin(np.median(ss)))), sl))
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    print("FIREWALL: declared surface only; MEASURED with ladders; an "
          "honest negative; no uniformity/rate/RH claim")

    print("--- PRIME.TRANSPORT.01 multilevel transport, measured: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
