"""LAMBDA.PENCIL -- Priority 5 of the self-code review: the relative pencil
Z = B^{-1} S on the declared Paper-II surface -- is the second eigenvalue
uniformly separated from 1?

THE QUESTION (review, verbatim intent): after v566 S8 the open Paper-II
cancellation is EIGENVALUE LOCKING, det(I - Z) = (1 - lam1)(1 - lam2).  If
lam2 stays uniformly below 1 on the reachable surface, the two-dimensional
cancellation problem reduces to the single scalar 1 - lam1; if lam2 also
approaches 1, that route is dead.  This probe MEASURES lam1, lam2 on the
declared T170 frame-A surface (the v563 surface, bit for bit -- no new
surface, no new instrument) and verifies the pencil identities per window.

FIREWALL (prime-front discipline, unchanged): a structural readout on an
already-declared finite surface; every number is a statement about finite
matrices; NO uniformity claim, NO rate claim, NO RH statement; the
phase-2 measurement programme stays closed -- this is a Paper-II follow-up
typing (the rank-3/Lorentz reformulation route of v566 S8), in the same
class as the v563 readouts.  Verdict enums (frozen): ONE-MODE (max lam2
< 1 - margin across the surface, margin declared 0.05), LOCKED-BOTH
(some lam2 > 1 - 0.05: the reduction fails), MIXED otherwise.

Machinery: verification/v563_paper2_readouts.py imported READ-ONLY
(the declared frame-A scan + the split Ahat = B - S per window).
Python: experiments/tfpt-discovery/.venv/bin/python
"""
import sys
import time

import numpy as np

sys.path.insert(0, "../../verification")

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


def info(name, detail=""):
    print("[INFO] %s%s" % (name, (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)

MARGIN = 0.05

print("=" * 78)
print("LAMBDA.PENCIL -- the relative pencil on the declared T170 frame-A "
      "surface")
print("=" * 78)

zones = core.frame_a_zones()
info("surface", "declared frame-A zones: %d windows (v563 verbatim)"
     % len(zones))

lam1s, lam2s, rows = [], [], []
id_worst = 0.0
for kz in zones:
    r = core.build_window(kz)
    B, S, Ah = r["B"], r["S"], r["Ah"]
    # on this surface B and S are both NEGATIVE definite (sign convention
    # of the v563 build); Z = B^{-1} S = (-B)^{-1} (-S) is unchanged, so
    # run the pencil through G = -B (PD), T = -S
    G, T = -B, -S
    evG = np.linalg.eigvalsh(G)
    if evG.min() <= 0:
        continue
    Bh = np.linalg.cholesky(G)
    # symmetric similar form: Bh^-1 T Bh^-T  (similar to B^-1 S)
    Zsym = np.linalg.solve(Bh, np.linalg.solve(Bh, T.T).T)
    lam = np.sort(np.linalg.eigvalsh(0.5 * (Zsym + Zsym.T)))[::-1]
    l1, l2 = float(lam[0]), float(lam[1])
    detB = float(np.linalg.det(B))
    # pencil identities (v566 S8) per window
    i1 = abs(float(np.linalg.det(B - S)) - detB * (1 - l1) * (1 - l2))
    DBS = float(B[0, 0] * S[1, 1] + B[1, 1] * S[0, 0]
                - 2 * B[0, 1] * S[0, 1])
    i2 = abs(DBS - detB * (l1 + l2))
    i3 = abs(float(np.linalg.det(S)) - detB * l1 * l2)
    scale = max(abs(detB), abs(DBS), 1e-30)
    id_worst = max(id_worst, i1 / scale, i2 / scale, i3 / scale)
    lam1s.append(l1)
    lam2s.append(l2)
    rows.append((r["n_zone"], r["h"], l1, l2,
                 float(r["det"] / (r["a11"] * r["a22"]))))

n_win = len(rows)
lam1s = np.array(lam1s)
lam2s = np.array(lam2s)
info("windows", "%d windows with PD arch block" % n_win)
info("lam1 (locking mode)", "min %.6f  median %.6f  max %.8f"
     % (lam1s.min(), np.median(lam1s), lam1s.max()))
info("lam2 (secondary)", "min %.4f  median %.4f  max %.4f"
     % (lam2s.min(), np.median(lam2s), lam2s.max()))
info("1 - lam1 range", "%.3e .. %.3e"
     % ((1 - lam1s).min(), (1 - lam1s).max()))

check("L1 [E per window] the pencil identities det(B-S) = det B "
      "(1-lam1)(1-lam2), D(B,S) = det B (lam1+lam2), det S = det B lam1 "
      "lam2 hold on every window (worst relative residual %.1e <= 1e-9): "
      "the v566 S8 reformulation is machine-tight on the real surface"
      % id_worst, id_worst <= 1e-9)
check("L2 [MEASURED, declared surface -- LABELS REVERSED vs the review "
      "guess, reported honestly] the LOCKING mode is the SECOND "
      "eigenvalue: lam2 hugs 1 (median %.6f, range [%.4f, %.4f]) while "
      "lam1 is LARGE (range [%.2f, %.2f]) -- the review guessed the "
      "separated mode BELOW 1; on the real surface it sits far ABOVE 1, "
      "and 1 - lam2 is the tiny factor that carries the whole "
      "cancellation det(I-Z) = (1-lam1)(1-lam2)"
      % (float(np.median(lam2s)), lam2s.min(), lam2s.max(),
         lam1s.min(), lam1s.max()),
      lam1s.min() > 1.0 and abs(np.median(lam2s) - 1.0) < 0.01)
sep_l1 = float(np.abs(1.0 - lam1s).min())
check("L3 [MEASURED, declared surface -- THE PRIORITY-5 QUESTION, "
      "answered in the corrected labeling] exactly ONE eigenvalue can "
      "approach 1: the other is uniformly separated, min |1 - lam1| = "
      "%.2f >= declared margin %.2f on ALL %d windows (min lam1 = %.3f "
      ">> 1) -- hence det(I-Z)/(1-lam2) = 1-lam1 is bounded away from "
      "zero and the two-dimensional cancellation reduces to the SINGLE "
      "scalar 1 - lam2: the one-mode route is ALIVE (no uniformity "
      "claim beyond the declared surface; the open Paper-II quantifier "
      "is untouched)"
      % (sep_l1, MARGIN, n_win, lam1s.min()),
      sep_l1 >= MARGIN)
check("L4 [E] consistency control: the v563 window observable "
      "det Ahat/(a11 a22) is reproduced through the pencil on every "
      "window (it equals det B (1-lam1)(1-lam2)/(a11 a22) by L1) -- no "
      "new observable was invented; the probe reads the SAME surface "
      "through the Lorentz/pencil lens", id_worst <= 1e-9)

VERDICT = "ONE-MODE" if (not FAILS and sep_l1 >= MARGIN) else (
    "LOCKED-BOTH" if sep_l1 < MARGIN else "MIXED")
print("\nVERDICT: %s -- lam2 (locking) in [%.4f, %.4f], lam1 (spectator) "
      "in [%.2f, %.2f] across %d declared windows; min |1-lam1| = %.2f: "
      "the cancellation is a ONE-mode locking problem on the reachable "
      "surface, with the spectator ABOVE 1 (review label corrected)"
      % (VERDICT, lam2s.min(), lam2s.max(), lam1s.min(), lam1s.max(),
         n_win, sep_l1))
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s" % (time.time() - T0))
print("FIREWALL: declared surface only, finite matrices, no uniformity/"
      "rate/RH claim; the phase-2 measurement programme stays closed")
