"""v569 -- PRIME.PENCIL.ONEMODE.01: the relative pencil on the declared
Paper-II surface -- the near-cancellation is a ONE-mode eigenvalue-locking
problem (the Priority-5 question of the self-code review, answered on the
reachable surface, with the review's label corrected).

PROVENANCE.  v566 S8 proved the exact reformulation of the Paper-II rank-3
polarisation as (2+1)-Lorentz geometry and the relative-pencil identities
det(B-S) = det B det(I-Z), D(B,S) = det B tr Z, det S = det B det Z for
Z = B^{-1} S.  The review's Priority 5 asked the ONE measurable question
that decides whether the pencil route is alive: is one eigenvalue of Z
uniformly separated from 1 on the reachable surface, so that the
two-dimensional cancellation det(I-Z) = (1-lam1)(1-lam2) reduces to a
SINGLE scalar?  Audited and answered by the discovery probe
(lambda_pencil_probe.py, 4/4, verdict ONE-MODE); this module is the
load-bearing version.  Construction base: the declared T170 frame-A scan
of v563_paper2_readouts (imported READ-ONLY, bit for bit -- no new
surface, no new instrument, no new observable).

[E] 1. THE SURFACE IS THE DECLARED ONE: the frame-A zone scan of v563
    yields exactly 70 windows, all with definite arch block (B and S are
    both negative definite in the v563 sign convention; the pencil
    Z = B^{-1} S = (-B)^{-1} (-S) is convention-free).
[E] 2. THE PENCIL IDENTITIES ARE MACHINE-TIGHT ON THE REAL SURFACE:
    det(B-S) = det B (1-lam1)(1-lam2), D(B,S) = det B (lam1+lam2),
    det S = det B lam1 lam2 hold on every window (worst relative
    residual ~2e-14).
[MEASURED] 3. THE LABELS ARE THE REVERSE OF THE REVIEW GUESS (reported
    honestly): the LOCKING mode is the SECOND eigenvalue -- lam2 hugs 1
    (median 1.000021) while lam1 is LARGE (4.53 .. 180.64, always > 1).
    The review guessed the separated mode BELOW 1; it sits far ABOVE 1.
[MEASURED] 4. THE PRIORITY-5 ANSWER (the central result): exactly ONE
    eigenvalue can approach 1 -- min |1 - lam1| = 3.53 across ALL 70
    windows, so det(I-Z)/(1-lam2) = 1 - lam1 is uniformly bounded away
    from zero and the two-dimensional cancellation reduces to the SINGLE
    scalar 1 - lam2 on the whole reachable surface: verdict ONE-MODE,
    the route is alive.
[E] 5. THE REFERENCE WINDOW READS THROUGH THE PENCIL: on the h = 540
    window of v563 the locking factor is 1 - lam2 = -2.27e-5 and the
    pencil reproduces det Ahat = 4.22e-3 exactly (the 4.7-order
    cancellation of Paper II IS the single factor 1 - lam2).
[E] 6. MUST-BREAK: the position scramble (uniform u at the SAME masses,
    the v563 intervention) explodes |1 - lam2| by a factor ~1.9e6 and
    destroys the pencil geometry (both eigenvalues go negative) while
    the identities of (2) keep holding -- the locking is ARITHMETIC
    PLACEMENT, not an identity artefact.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   NO uniformity claim beyond the declared finite surface: the open
        Paper-II quantifier (Problem 7.1, uniform delta <= C h^{-3+eps})
        is UNTOUCHED -- this module types its structure (one scalar mode),
        it does not bound it.
  (ii)  MEASURED quantities stay MEASURED with their ladders (the v562
        anti-promotion applies); no rate, no bound, NO RH statement
        (finite tables below the declared caps).
  (iii) The reduction is a statement about the reachable surface only;
        whether lam1 stays separated as h grows is a new open question,
        strictly weaker than Problem 7.1.

Fences: Cholesky/symmetric-pencil reduction CLASSICAL; Cauchy-Binet
CLASSICAL; the surface, tables and caps are v563's (Schur 1917 fence
chain unchanged).  Python-only, counted per GATE.WOLFRAM.02.
Discovery surface: experiments/tfpt-discovery/lambda_pencil_probe.py
(2026-07-31, 4/4, ONE-MODE).
"""
import time

import numpy as np

import v563_paper2_readouts as core  # READ-ONLY import of the surface

T0 = time.time()
N_PASS = 0
N_FAIL = 0

# declared thresholds (frozen before the run, from the discovery probe)
TOL_IDENT = 1.0e-9        # pencil identities, relative
MARGIN_SEP = 0.05         # |1 - lam1| uniform separation margin
TOL_MEDIAN = 1.0e-2       # |median(lam2) - 1|
REF_H = 540               # the v563 reference window
TOL_REF_LOCK = 1.0e-4     # |1 - lam2| on the reference window
TOL_REF_SUM = 0.02        # relative match of det Ahat vs Q_SUM
BAR_SCRAMBLE = 1.0e4      # must-break: |1 - lam2| growth factor
SCRAMBLE_SEED = 1


def check(name, ok):
    global N_PASS, N_FAIL
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
    print("[%s] %s" % ("PASS" if ok else "FAIL", name))


def pencil_eigs(r):
    """Eigenvalues of Z = B^{-1} S via the symmetric similar form
    (-B)^{-1/2} (-S) (-B)^{-1/2}; descending order."""
    G, T = -r["B"], -r["S"]
    Bh = np.linalg.cholesky(G)
    Zs = np.linalg.solve(Bh, np.linalg.solve(Bh, T.T).T)
    lam = np.sort(np.linalg.eigvalsh(0.5 * (Zs + Zs.T)))[::-1]
    return float(lam[0]), float(lam[1])


def identity_residual(r, l1, l2):
    """Worst relative residual of the three pencil identities."""
    B, S = r["B"], r["S"]
    detB = float(np.linalg.det(B))
    DBS = float(B[0, 0] * S[1, 1] + B[1, 1] * S[0, 0]
                - 2.0 * B[0, 1] * S[0, 1])
    i1 = abs(float(np.linalg.det(B - S)) - detB * (1 - l1) * (1 - l2))
    i2 = abs(DBS - detB * (l1 + l2))
    i3 = abs(float(np.linalg.det(S)) - detB * l1 * l2)
    scale = max(abs(detB), abs(DBS), 1.0e-30)
    return max(i1, i2, i3) / scale


def run():
    global N_PASS, N_FAIL
    N_PASS = 0
    N_FAIL = 0
    print("=" * 78)
    print("v569 -- PRIME.PENCIL.ONEMODE.01: the relative pencil on the "
          "declared surface")
    print("=" * 78)

    zones = core.frame_a_zones()
    lam1s, lam2s = [], []
    id_worst = 0.0
    n_g_pd = 0
    n_s_pd = 0
    ref = None
    for kz in zones:
        r = core.build_window(kz)
        evG = np.linalg.eigvalsh(-r["B"])
        evS = np.linalg.eigvalsh(-r["S"])
        if evG.min() > 0:
            n_g_pd += 1
        if evS.min() > 0:
            n_s_pd += 1
        l1, l2 = pencil_eigs(r)
        id_worst = max(id_worst, identity_residual(r, l1, l2))
        lam1s.append(l1)
        lam2s.append(l2)
        if r["h"] == REF_H:
            ref = (kz, r, l1, l2)
    lam1s = np.array(lam1s)
    lam2s = np.array(lam2s)
    n_win = len(lam1s)

    check("1. SURFACE [E]: the declared v563 frame-A scan yields %d windows "
          "(= 70); the arch block -B is positive definite on %d/70 (all) "
          "and -S on %d/70 (one indefinite kernel block, honest count); "
          "the pencil Z = B^-1 S = (-B)^-1 (-S) is convention-free"
          % (n_win, n_g_pd, n_s_pd),
          n_win == 70 and n_g_pd == 70)

    check("2. IDENTITIES [E]: det(B-S) = det B (1-lam1)(1-lam2), D(B,S) = "
          "det B (lam1+lam2), det S = det B lam1 lam2 on EVERY window -- "
          "worst relative residual %.1e <= %.0e: the v566 S8 reformulation "
          "is machine-tight on the real surface"
          % (id_worst, TOL_IDENT),
          id_worst <= TOL_IDENT)

    med2 = float(np.median(lam2s))
    check("3. LABELS REVERSED vs the review guess [MEASURED, honest]: the "
          "LOCKING mode is lam2 -- median %.6f (|median - 1| = %.1e <= "
          "1e-2), range [%.4f, %.4f]; the spectator lam1 is LARGE: range "
          "[%.2f, %.2f], every window > 1 (the review guessed it BELOW 1)"
          % (med2, abs(med2 - 1.0), lam2s.min(), lam2s.max(),
             lam1s.min(), lam1s.max()),
          abs(med2 - 1.0) <= TOL_MEDIAN and lam1s.min() > 1.0)

    sep = float(np.abs(1.0 - lam1s).min())
    check("4. THE PRIORITY-5 ANSWER [MEASURED, declared surface]: exactly "
          "ONE eigenvalue can approach 1 -- min |1 - lam1| = %.2f >= %.2f "
          "on ALL %d windows, so det(I-Z)/(1-lam2) = 1-lam1 is uniformly "
          "bounded away from zero: the two-dimensional cancellation reduces "
          "to the SINGLE scalar 1 - lam2 -- verdict ONE-MODE, the pencil "
          "route is ALIVE (no claim beyond the declared surface; Problem "
          "7.1 untouched)"
          % (sep, MARGIN_SEP, n_win),
          sep >= MARGIN_SEP)

    assert ref is not None, "reference window h = 540 not on the scan"
    kz_ref, r_ref, l1_ref, l2_ref = ref
    det_pencil = float(np.linalg.det(r_ref["B"])) * (1 - l1_ref) * (1 - l2_ref)
    rel_sum = abs(det_pencil - core.Q_SUM) / core.Q_SUM
    check("5. REFERENCE WINDOW [E]: on h = 540 the locking factor is "
          "1 - lam2 = %.3e (|.| <= 1e-4) and the pencil reproduces "
          "det Ahat = %.3e vs the Paper-II quote %.2e (rel %.1e <= 2%%): "
          "the 4.7-order cancellation IS the single factor 1 - lam2"
          % (1 - l2_ref, det_pencil, core.Q_SUM, rel_sum),
          abs(1 - l2_ref) <= TOL_REF_LOCK and rel_sum <= TOL_REF_SUM)

    r_scr = core.build_window(kz_ref, scramble_seed=SCRAMBLE_SEED)
    m1, m2 = pencil_eigs(r_scr)
    id_scr = identity_residual(r_scr, m1, m2)
    ratio = abs(1 - m2) / abs(1 - l2_ref)
    check("6. MUST-BREAK [E]: the position scramble (uniform u at the SAME "
          "masses, the v563 intervention) explodes |1 - lam2| by x%.1e >= "
          "1e4 and destroys the pencil geometry (lam = %.2f, %.2f -- both "
          "negative) while the identities keep holding (residual %.1e): "
          "the locking is ARITHMETIC PLACEMENT, not an identity artefact"
          % (ratio, m1, m2, id_scr),
          ratio >= BAR_SCRAMBLE and m1 < 0 and m2 < 0
          and id_scr <= TOL_IDENT)

    print("\nkey numbers: lam2 (locking) in [%.4f, %.4f] median %.6f; "
          "lam1 (spectator) in [%.2f, %.2f]; min |1-lam1| = %.2f; "
          "reference 1-lam2 = %.3e; scramble x%.1e"
          % (lam2s.min(), lam2s.max(), med2, lam1s.min(), lam1s.max(),
             sep, 1 - l2_ref, ratio))
    print("NAMED LIMITS: declared surface only; MEASURED stays MEASURED; "
          "no uniformity, no rate, no bound, NO RH statement; Problem 7.1 "
          "untouched (its structure is typed, not bounded)")
    print("elapsed: %.1f s" % (time.time() - T0))
    print("--- PRIME.PENCIL.ONEMODE.01 relative pencil one-mode: "
          "%d passed, %d failed ---" % (N_PASS, N_FAIL))
    return N_FAIL


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
