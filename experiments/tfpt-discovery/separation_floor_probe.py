"""SEPARATION.FLOOR -- the v569 open question, reduced and certified on the
surface: the spectator separation |1 - lam1| follows from two one-line
theorems plus the scalar dominance det S >> det B -- and the cheap witness
route is honestly killed.

THE QUESTION (named open by v569, strictly weaker than Paper-II Problem
7.1): does the spectator eigenvalue lam1 of the relative pencil
Z = B^{-1} S stay uniformly separated from 1?  v569 MEASURED the
separation (min |1 - lam1| = 3.53); this probe asks whether it can be
CERTIFIED from closed scalars, and what the h-uniform question reduces to.

THE REDUCTION (exact, one line each; eigenvalues are real because Z is
similar to a symmetric matrix):
  (i)  P := det Z = det S/det B > 0 and T := tr Z > 0
       ==> both eigenvalues positive ==> lam1 >= sqrt(P).
  (ii) P <= 0 ==> lam2 <= 0 <= lam1 ==> lam1 = T - lam2 >= T.
  So the closed per-window floor  F := sqrt(P) if P > 0 else T  certifies
  the separation whenever F >= 1 + margin -- the open question reduces to
  DETERMINANT/TRACE DOMINANCE of the comb block over the arch block.

FIREWALL (prime-front discipline, unchanged): a structural readout on the
already-declared T170 frame-A surface (the v563 scan, read-only, bit for
bit); finite matrices only; NO uniformity claim beyond the surface, no
rate, no bound, NO RH statement.  Verdict enums (frozen before the run):
FLOOR-CERTIFIED (the closed floor >= 1 + margin on ALL windows, margin
declared 0.05), FLOOR-FAILS (some window below), MIXED (identity failure).

Python: experiments/tfpt-discovery/.venv/bin/python
"""
import sys
import time

import numpy as np

sys.path.insert(0, "../../verification")

T0 = time.time()
FAILS = []
N_CHK = 0

MARGIN = 0.05          # declared separation margin (same as v569)
KERNEL_STRIDE = 6      # pair-kernel analysis on every 6th window + reference
REF_H = 540


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

print("=" * 78)
print("SEPARATION.FLOOR -- the v569 open question reduced to scalar "
      "dominance")
print("=" * 78)

# --- S1: the two one-line theorems, verified symbolically ----------------
import sympy as sp  # noqa: E402

l1, l2 = sp.symbols("lambda1 lambda2", real=True)
T_, P_ = l1 + l2, l1 * l2
# (i) P > 0, T > 0, l1 >= l2  ==>  l1 >= sqrt(P):
#     both roots positive, and l1**2 >= l1*l2 = P since l1 >= l2 > 0.
lhs_i = sp.simplify(l1**2 - P_)          # = l1*(l1 - l2) >= 0 when l1>=l2>0
ok_i = sp.simplify(lhs_i - l1 * (l1 - l2)) == 0
# (ii) P <= 0 ==> l2 <= 0 (product nonpositive, l1 the larger root)
#      ==> l1 = T - l2 >= T.
ok_ii = sp.simplify((T_ - l2) - l1) == 0
check("S1.1 [E, theorem] the two floor lemmas verified symbolically: "
      "lam1^2 - P = lam1 (lam1 - lam2) exactly (so P > 0, T > 0, "
      "lam1 >= lam2 give lam1 >= sqrt(P)), and lam1 = T - lam2 exactly "
      "(so P <= 0, T > 0 give lam1 >= T)", ok_i and ok_ii)

x = sp.symbols("x")
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
check("S1.2 [E, symbolic] the scalars are CLOSED objects: T = tr Z = "
      "D(B,S)/det B, P = det Z = det S/det B, and det(B-S)/det B = "
      "1 - T + P exactly -- so on deficit windows T - P = 1 + o(1): "
      "the trace dominance IS the determinant dominance plus one",
      ok_t and ok_p and ok_link)

# --- S2: the certified floor on the whole declared surface ---------------
zones = core.frame_a_zones()
data = []
for kz in zones:
    r = core.build_window(kz)
    B, S = r["B"], r["S"]
    detB = float(np.linalg.det(B))
    P = float(np.linalg.det(S)) / detB
    T = float(np.trace(np.linalg.solve(B, S)))
    G = -B
    Bh = np.linalg.cholesky(G)
    Zsym = np.linalg.solve(Bh, np.linalg.solve(Bh, (-S).T).T)
    lam = np.sort(np.linalg.eigvalsh(0.5 * (Zsym + Zsym.T)))[::-1]
    floor = np.sqrt(P) if P > 0 else T
    data.append(dict(kz=kz, h=r["h"], detB=detB, P=P, T=T,
                     l1=float(lam[0]), l2=float(lam[1]), floor=floor,
                     r=r))

n_win = len(data)
floors = np.array([d["floor"] for d in data])
l1s = np.array([d["l1"] for d in data])
Ps = np.array([d["P"] for d in data])
Ts = np.array([d["T"] for d in data])
n_pneg = int((Ps <= 0).sum())
sound = all(d["l1"] >= d["floor"] - 1e-9 for d in data)
info("surface", "%d declared windows; P <= 0 on %d; T > 0 on %d/%d"
     % (n_win, n_pneg, int((Ts > 0).sum()), n_win))
info("floor", "min %.3f  median %.3f (true min lam1 = %.3f)"
     % (floors.min(), float(np.median(floors)), l1s.min()))

check("S2.1 [E per window] the floor is SOUND: lam1 >= floor on every "
      "window (floor = sqrt(P) on %d windows, = T on %d)"
      % (n_win - n_pneg, n_pneg), sound)
check("S2.2 [E per window -- THE CERTIFICATION] the closed scalar floor "
      "certifies the v569 separation on the WHOLE declared surface: "
      "min floor = %.3f >= 1 + %.2f on ALL %d windows -- the separation "
      "is no longer only a measured eigenvalue fact, it follows from "
      "det S/det B and tr Z alone (conservative against the measured "
      "min lam1 = %.3f, as a floor should be)"
      % (floors.min(), MARGIN, n_win, l1s.min()),
      floors.min() >= 1 + MARGIN)

# --- S3: the dominance structure (measured, with its ladder) -------------
hs = np.array([d["h"] for d in data], float)
mask = Ps > 0
slope = float(np.polyfit(np.log(hs[mask]), np.log(Ps[mask]), 1)[0])
tp = np.array([d["T"] - d["P"] for d in data if d["P"] > 0])
info("dominance", "P = det S/det B in [%.1f, %.1f] median %.1f; "
     "log-log slope vs h: %.3f" % (Ps[mask].min(), Ps.max(),
                                   float(np.median(Ps[mask])), slope))
check("S3.1 [MEASURED, declared surface] the dominance GROWS with depth: "
      "P = det S/det B has log-log slope %.3f > 0 in h on the surface "
      "(median P = %.1f; every deep window far above the floor "
      "threshold) -- reported with the surface ladder, no rate claim "
      "beyond it" % (slope, float(np.median(Ps[mask]))),
      slope > 0.5)
def _link_dev(d):
    detAB = float(np.linalg.det(d["r"]["B"] - d["r"]["S"])) / d["detB"]
    return abs(1 - d["T"] + d["P"] - detAB) / max(1.0, abs(detAB))


worst_link = max(_link_dev(d) for d in data)
check("S3.2 [E per window] the exact link 1 - T + P = det(B-S)/det B "
      "holds numerically on every window (worst relative deviation "
      "%.1e), i.e. T - P = 1 - det(B-S)/det B: on deficit windows the "
      "trace exceeds the determinant ratio by exactly one -- dominance "
      "certified in EITHER scalar certifies the other" % worst_link,
      worst_link <= 1e-9)

# --- S4: the cheap witness route, honestly killed ------------------------
sel = [d for i, d in enumerate(data) if i % KERNEL_STRIDE == 0
       or d["h"] == REF_H]
worst_cb = 0.0
neg_fracs = []
best_pairs = []
for d in sel:
    r = d["r"]
    lamw, Xn = r["lam"], r["Xn"]
    a, b, c = Xn[:, 0], Xn[:, 1], Xn[:, 2]
    K = 0.5 * (np.outer(a, b) + np.outer(b, a)) - np.outer(c, c)
    detS_cb = float(lamw @ K @ lamw)
    worst_cb = max(worst_cb,
                   abs(detS_cb / (d["P"] * d["detB"]) - 1.0))
    W = np.outer(lamw, lamw) * 0.5 * (K + K.T)
    neg_fracs.append(float(-W[W < 0].sum() / abs(detS_cb)))
    iu = np.triu_indices(len(lamw), 1)
    best_pairs.append(float((2 * W[iu]).max()) / d["detB"])
neg_fracs = np.array(neg_fracs)
best_pairs = np.array(best_pairs)
check("S4.1 [E per window] the pair decomposition is EXACT (Cauchy-"
      "Binet): det S = lam^T K lam with K the polarisation kernel of "
      "the per-atom 2x2 reads, worst relative deviation %.1e on the "
      "%d-window kernel subset" % (worst_cb, len(sel)),
      worst_cb <= 1e-9)
check("S4.2 [E, HONEST NEGATIVE -- the cheap route is killed] det S is "
      "itself a pair-level CANCELLATION object: the negative pair mass "
      "reaches %.1f x det S (median %.1f x), and the best single-pair "
      "witness delivers only %.2f--%.2f x det B against the >= "
      "(1+margin)^2 = %.2f it would need -- NO two-atom witness "
      "certifies the dominance: the h-uniform question is typed as "
      "pair-level size-vs-cancellation (strictly weaker than Problem "
      "7.1 -- an 8:9 cancellation, not a 4.7-order one -- but not free)"
      % (neg_fracs.max(), float(np.median(neg_fracs)),
         best_pairs.min(), best_pairs.max(), (1 + MARGIN)**2),
      best_pairs.max() < (1 + MARGIN)**2 and neg_fracs.max() > 1.0)

# --- S5: must-break -------------------------------------------------------
d_ref = next(d for d in data if d["h"] == REF_H)
r_scr = core.build_window(d_ref["kz"], scramble_seed=1)
detB_s = float(np.linalg.det(r_scr["B"]))
P_s = float(np.linalg.det(r_scr["S"])) / detB_s
T_s = float(np.trace(np.linalg.solve(r_scr["B"], r_scr["S"])))
check("S5.1 [must-break] the position scramble (same masses, the v563 "
      "intervention) FLIPS the trace sign: T = %.2f < 0 on the "
      "scrambled reference window (real: T = %.2f > 0) -- the T > 0 "
      "gate of the floor detects the destroyed geometry loudly; the "
      "dominance is arithmetic placement, not a build artefact"
      % (T_s, d_ref["T"]),
      T_s < 0 and d_ref["T"] > 0)

VERDICT = ("FLOOR-CERTIFIED" if not FAILS and floors.min() >= 1 + MARGIN
           else ("FLOOR-FAILS" if floors.min() < 1 + MARGIN else "MIXED"))
print("\nVERDICT: %s -- closed floor min %.3f over %d windows (margin "
      "%.2f); dominance P in [%.1f, %.1f] growing h^%.2f; pair-witness "
      "route dead (neg mass up to %.1f x det S)"
      % (VERDICT, floors.min(), n_win, MARGIN, Ps[mask].min(), Ps.max(),
         slope, neg_fracs.max()))
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s" % (time.time() - T0))
print("FIREWALL: declared surface only, finite matrices, no uniformity/"
      "rate/RH claim; Problem 7.1 untouched")
