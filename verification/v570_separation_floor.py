"""v570 -- PRIME.PENCIL.SEPFLOOR.01: the v569 open question, reduced and
certified on the declared surface -- the spectator separation follows from
two one-line theorems plus the scalar dominance det S >> det B, and the
cheap witness route is honestly killed.

PROVENANCE.  v569 answered the Priority-5 question of the self-code review
on the reachable surface (verdict ONE-MODE) and left ONE new named open
question, strictly weaker than Paper-II Problem 7.1: does the spectator
eigenvalue lam1 of the relative pencil Z = B^{-1} S stay uniformly
separated from 1?  There the separation was MEASURED (min |1 - lam1| =
3.53).  This module CERTIFIES it from closed scalars and types what the
h-uniform question reduces to.  Audited by the discovery probe
(separation_floor_probe.py, 9/9, verdict FLOOR-CERTIFIED).  Construction
base: the declared T170 frame-A scan of v563_paper2_readouts (imported
READ-ONLY, bit for bit -- no new surface, no new instrument).

THE REDUCTION (exact; eigenvalues real because Z is similar symmetric):
  (i)  P := det Z = det S/det B > 0 and T := tr Z > 0 give both
       eigenvalues positive, hence lam1 >= sqrt(P)
       (lam1^2 - P = lam1 (lam1 - lam2) >= 0).
  (ii) P <= 0 gives lam2 <= 0 <= lam1, hence lam1 = T - lam2 >= T.
  The closed per-window floor F := sqrt(P) if P > 0 else T certifies the
  separation whenever F >= 1 + margin: the open question reduces to
  DETERMINANT/TRACE DOMINANCE of the comb block over the arch block.

[E] 1. The two floor lemmas verified symbolically; T, P and the link
    1 - T + P = det(B-S)/det B are closed objects of (B, S).
[E] 2. THE CERTIFICATION (the central result): on ALL 70 declared
    windows the closed floor is sound (lam1 >= F) and clears the margin,
    min F = 2.130 >= 1.05 -- the v569 separation is no longer only a
    measured eigenvalue fact, it follows from det S/det B and tr Z alone.
[MEASURED] 3. The dominance GROWS with depth: P = det S/det B in
    [4.5, 120.6], median 30.1, log-log slope +0.900 in h on the surface
    (reported with its ladder; no rate claim beyond the surface).
[E] 4. The pair decomposition is exact (Cauchy-Binet) -- and the cheap
    witness route is DEAD, reported honestly: det S is itself a
    pair-level cancellation object (negative pair mass up to 13.7 x
    det S, median 8.0 x; the best single-pair witness delivers only
    0.13--0.34 x det B against the >= 1.10 it would need).  The
    h-uniform question is typed as pair-level size-vs-cancellation --
    an 8:9 cancellation, not a 4.7-order one, but not free.
[E] 5. MUST-BREAK: the position scramble (same masses, the v563
    intervention) FLIPS the trace sign (T = -78.28 vs +32.15 real): the
    T > 0 gate detects the destroyed geometry loudly -- the dominance is
    arithmetic placement, not a build artefact.

NAMED LIMITS AS LOAD-BEARING CONTENT (the claim INCLUDES them):
  (i)   Declared finite surface only: the certification is per window on
        the reachable surface; whether the dominance persists as h grows
        is the SAME named open question as v569's, now in the sharper
        closed-scalar form det S >= (1 + c)^2 det B (or tr Z >= 1 + c).
  (ii)  Paper-II Problem 7.1 (the uniform deficit quantifier) is
        UNTOUCHED; MEASURED quantities keep their ladders (the v562
        anti-promotion applies); no rate, no bound, NO RH statement.

Fences: elementary 2x2 spectral theory CLASSICAL; Cauchy-Binet CLASSICAL;
the v563 fence chain (Schur 1917 etc.) unchanged.  Python-only, counted
per GATE.WOLFRAM.02.  Discovery surface:
experiments/tfpt-discovery/separation_floor_probe.py
(2026-07-31, 9/9, FLOOR-CERTIFIED).
"""
import time

import numpy as np
import sympy as sp

import v563_paper2_readouts as core  # READ-ONLY import of the surface

N_PASS = 0
N_FAIL = 0

# declared thresholds (frozen before the run, from the discovery probe)
MARGIN = 0.05            # separation margin (same as v569)
TOL_SOUND = 1.0e-9       # floor soundness slack
TOL_LINK = 1.0e-9        # link identity, relative
TOL_CB = 1.0e-9          # Cauchy-Binet, relative
BAR_SLOPE = 0.5          # dominance growth slope floor
BAR_NEGMASS = 1.0        # witness-kill: negative pair mass / det S
KERNEL_STRIDE = 6        # pair-kernel subset (every 6th window + reference)
REF_H = 540
SCRAMBLE_SEED = 1
PAIR_KERNEL_BLOCK = 1024  # rows of the n x n pair kernel held at once (see below)


def check(name, ok):
    global N_PASS, N_FAIL
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
    print("[%s] %s" % ("PASS" if ok else "FAIL", name))


def pair_kernel_stats(lamw, a, b, c, block=PAIR_KERNEL_BLOCK):
    """The three pair-level readouts of section 4 for the polarisation kernel
    K = (a b^T + b a^T)/2 - c c^T and its mass-weighted form W = (lam lam^T) o K:
    the Cauchy-Binet quadratic form lam^T K lam, the negative pair mass
    -sum(W[W < 0]) and the best single pair max_{i<j} W_ij.

    Evaluated in row blocks: K and W are never materialised as n x n arrays.
    The kernel subset reaches n = 26091 atoms, where one dense n x n double
    array is 5.4 GB and the original outer-product formulation peaked above
    30 GB -- more than the 16 GB CI runner holds (OOM, exit 143).  Entrywise
    the blocks are the same double-precision numbers as the dense arrays (K
    is exactly symmetric, so (K + K^T)/2 == K bitwise); only the summation
    order of the two accumulated sums differs, at the 1e-16 level.
    """
    n = len(lamw)
    quad = 0.0
    neg_mass = 0.0
    best_pair = -np.inf
    cols = np.arange(n)[None, :]
    for i0 in range(0, n, block):
        i1 = min(n, i0 + block)
        K_blk = (0.5 * (np.outer(a[i0:i1], b) + np.outer(b[i0:i1], a))
                 - np.outer(c[i0:i1], c))
        quad += float(lamw[i0:i1] @ (K_blk @ lamw))
        W_blk = np.outer(lamw[i0:i1], lamw) * K_blk
        neg_mass += float(-W_blk[W_blk < 0].sum())
        upper = W_blk[cols > np.arange(i0, i1)[:, None]]
        if upper.size:
            best_pair = max(best_pair, float(upper.max()))
    return quad, neg_mass, best_pair


def run():
    global N_PASS, N_FAIL
    N_PASS = 0
    N_FAIL = 0
    t0 = time.time()
    print("=" * 78)
    print("v570 -- PRIME.PENCIL.SEPFLOOR.01: the separation floor, "
          "certified on the declared surface")
    print("=" * 78)

    # --- 1. the reduction, symbolic ---------------------------------------
    l1, l2 = sp.symbols("lambda1 lambda2", real=True)
    ok_i = sp.simplify((l1**2 - l1 * l2) - l1 * (l1 - l2)) == 0
    ok_ii = sp.simplify(((l1 + l2) - l2) - l1) == 0
    b11, b12, b22, s11, s12, s22 = sp.symbols("b11 b12 b22 s11 s12 s22")
    Bs = sp.Matrix([[b11, b12], [b12, b22]])
    Ss = sp.Matrix([[s11, s12], [s12, s22]])
    Zs = Bs.inv() * Ss
    ok_t = sp.simplify(sp.trace(Zs)
                       - (b11 * s22 + b22 * s11 - 2 * b12 * s12)
                       / Bs.det()) == 0
    ok_p = sp.simplify(Zs.det() - Ss.det() / Bs.det()) == 0
    ok_link = sp.simplify((Bs - Ss).det() / Bs.det()
                          - (1 - sp.trace(Zs) + Zs.det())) == 0
    check("1. REDUCTION [E, symbolic]: lam1^2 - P = lam1 (lam1 - lam2) "
          "and lam1 = T - lam2 exactly (the two floor lemmas: P > 0, "
          "T > 0 give lam1 >= sqrt(P); P <= 0, T > 0 give lam1 >= T), "
          "and T = D(B,S)/det B, P = det S/det B, 1 - T + P = "
          "det(B-S)/det B are closed objects of (B, S)",
          ok_i and ok_ii and ok_t and ok_p and ok_link)

    # --- 2. the certified floor on the whole surface ----------------------
    zones = core.frame_a_zones()
    data = []
    for kz in zones:
        r = core.build_window(kz)
        B, S = r["B"], r["S"]
        detB = float(np.linalg.det(B))
        P = float(np.linalg.det(S)) / detB
        T = float(np.trace(np.linalg.solve(B, S)))
        Bh = np.linalg.cholesky(-B)
        Zsym = np.linalg.solve(Bh, np.linalg.solve(Bh, (-S).T).T)
        lam = np.sort(np.linalg.eigvalsh(0.5 * (Zsym + Zsym.T)))[::-1]
        floor = np.sqrt(P) if P > 0 else T
        data.append(dict(kz=kz, h=r["h"], detB=detB, P=P, T=T,
                         l1=float(lam[0]), floor=floor, r=r))
    n_win = len(data)
    floors = np.array([d["floor"] for d in data])
    l1s = np.array([d["l1"] for d in data])
    Ps = np.array([d["P"] for d in data])
    Ts = np.array([d["T"] for d in data])
    n_pneg = int((Ps <= 0).sum())
    sound = all(d["l1"] >= d["floor"] - TOL_SOUND for d in data)
    check("2a. SOUNDNESS [E per window]: lam1 >= floor on every one of "
          "the %d declared windows (floor = sqrt(P) on %d, = T on %d; "
          "T > 0 on %d/%d)"
          % (n_win, n_win - n_pneg, n_pneg, int((Ts > 0).sum()), n_win),
          sound and n_win == 70)
    check("2b. THE CERTIFICATION [E per window, the central result]: the "
          "closed scalar floor clears the margin on the WHOLE surface -- "
          "min floor = %.3f >= 1 + %.2f on ALL %d windows: the v569 "
          "separation follows from det S/det B and tr Z alone "
          "(conservative against the measured min lam1 = %.3f, as a "
          "floor should be)"
          % (floors.min(), MARGIN, n_win, l1s.min()),
          floors.min() >= 1 + MARGIN)

    # --- 3. the dominance structure ---------------------------------------
    hs = np.array([d["h"] for d in data], float)
    mask = Ps > 0
    slope = float(np.polyfit(np.log(hs[mask]), np.log(Ps[mask]), 1)[0])
    check("3a. DOMINANCE GROWS [MEASURED, declared surface]: P = "
          "det S/det B in [%.1f, %.1f], median %.1f, log-log slope "
          "%.3f > %.1f in h -- reported with the surface ladder, no "
          "rate claim beyond it"
          % (Ps[mask].min(), Ps.max(), float(np.median(Ps[mask])),
             slope, BAR_SLOPE),
          slope > BAR_SLOPE)

    def link_dev(d):
        detAB = (float(np.linalg.det(d["r"]["B"] - d["r"]["S"]))
                 / d["detB"])
        return abs(1 - d["T"] + d["P"] - detAB) / max(1.0, abs(detAB))

    worst_link = max(link_dev(d) for d in data)
    check("3b. THE LINK [E per window]: 1 - T + P = det(B-S)/det B on "
          "every window (worst relative deviation %.1e) -- on deficit "
          "windows T - P = 1 + o(1): dominance certified in EITHER "
          "scalar certifies the other" % worst_link,
          worst_link <= TOL_LINK)

    # --- 4. the witness route, honestly killed ----------------------------
    sel = [d for i, d in enumerate(data) if i % KERNEL_STRIDE == 0
           or d["h"] == REF_H]
    worst_cb = 0.0
    neg_fracs = []
    best_pairs = []
    for d in sel:
        r = d["r"]
        lamw, Xn = r["lam"], r["Xn"]
        a, b, c = Xn[:, 0], Xn[:, 1], Xn[:, 2]
        detS_cb, neg_mass, best_pair = pair_kernel_stats(lamw, a, b, c)
        worst_cb = max(worst_cb,
                       abs(detS_cb / (d["P"] * d["detB"]) - 1.0))
        neg_fracs.append(neg_mass / abs(detS_cb))
        best_pairs.append(2 * best_pair / d["detB"])
    neg_fracs = np.array(neg_fracs)
    best_pairs = np.array(best_pairs)
    check("4a. CAUCHY-BINET [E per window]: det S = lam^T K lam with K "
          "the polarisation kernel of the per-atom 2x2 reads -- worst "
          "relative deviation %.1e on the %d-window kernel subset"
          % (worst_cb, len(sel)), worst_cb <= TOL_CB)
    check("4b. THE CHEAP ROUTE IS DEAD [E, honest negative]: det S is "
          "itself a pair-level CANCELLATION object -- negative pair "
          "mass up to %.1f x det S (median %.1f x), best single-pair "
          "witness only %.2f--%.2f x det B against the >= %.2f needed: "
          "NO two-atom witness certifies the dominance; the h-uniform "
          "question is typed as pair-level size-vs-cancellation "
          "(an 8:9 cancellation, not a 4.7-order one -- but not free)"
          % (neg_fracs.max(), float(np.median(neg_fracs)),
             best_pairs.min(), best_pairs.max(), (1 + MARGIN)**2),
          best_pairs.max() < (1 + MARGIN)**2
          and neg_fracs.max() > BAR_NEGMASS)

    # --- 5. must-break -----------------------------------------------------
    d_ref = next(d for d in data if d["h"] == REF_H)
    r_scr = core.build_window(d_ref["kz"], scramble_seed=SCRAMBLE_SEED)
    T_s = float(np.trace(np.linalg.solve(r_scr["B"], r_scr["S"])))
    check("5. MUST-BREAK [E]: the position scramble (same masses, the "
          "v563 intervention) FLIPS the trace sign on the reference "
          "window -- T = %.2f < 0 against the real +%.2f: the T > 0 "
          "gate detects the destroyed geometry loudly; the dominance "
          "is ARITHMETIC PLACEMENT, not a build artefact"
          % (T_s, d_ref["T"]),
          T_s < 0 and d_ref["T"] > 0)

    print("\nkey numbers: floor min %.3f (margin %.2f) on %d windows; "
          "P in [%.1f, %.1f] median %.1f, slope h^%.2f; neg pair mass "
          "max %.1f x; scramble T = %.1f"
          % (floors.min(), MARGIN, n_win, Ps[mask].min(), Ps.max(),
             float(np.median(Ps[mask])), slope, neg_fracs.max(), T_s))
    print("NAMED LIMITS: declared surface only; the h-uniform dominance "
          "det S >= (1+c)^2 det B is the SAME open question as v569's, "
          "in sharper closed-scalar form; Problem 7.1 untouched; "
          "MEASURED stays MEASURED; no rate, no bound, NO RH statement")
    print("elapsed: %.1f s" % (time.time() - t0))
    print("--- PRIME.PENCIL.SEPFLOOR.01 separation floor certified: "
          "%d passed, %d failed ---" % (N_PASS, N_FAIL))
    return N_FAIL


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
