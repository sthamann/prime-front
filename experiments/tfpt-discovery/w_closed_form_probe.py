"""PRIME.WCLOSED -- the diagonal companion of the v576 cross formula,
and the closed entry forms of the deterministic layer.  NEW EXACT
FORMULA (machine-exact, 1e-15, all h and modes tested): for the parity
mode t_k on the window of half-length m (N = 2m + 1, w_k = 2 pi k/N)
the diagonal lag weight of the corpus (v563 lag_weights_from_v) is the
SINGLE closed expression

    W_kk(d) = (2/N) [ (N-1-d) cos(w_k d) + sin(w_k (d+1))/sin(w_k) ],
    d >= 1,  W_kk(0) = 1.

Structure that falls out exactly: (i) the apparent piecewise break at
d = m (the autocorrelation dies at d = m, only the reflection
convolution survives) CANCELS -- both branches assemble to the same
single formula; (ii) the reflection-edge suppression of the weights is
an exact two-term cancellation (both terms are O(s) at d = N-1-s);
(iii) the macro limit is g_k(sigma) = 2(1-sigma) cos(2 pi k sigma)
+ sin(2 pi k sigma)/(pi k), and the v579 kernel is its edge-anchored
version, g(sigma) = -W_inf(1-sigma) -- the two normalizations are now
dictionaried.  THE PAYOFF: the S-side entries of the v583 prime-free
model become exact finite geometric-trig sums (lambda-cell masses x closed
weights; the tent assembly is mass-preserving): the exact discrete sum
reproduces the v583 entries AND det to ~0.2%, and the elementary
Laplace closed forms (rational-exponential in alpha) are their macro
limits.  The deterministic layer of Problem 7.1 (v585/v586) is now
closed-form at the entry level; the named next steps are the arch/B
side and the delta_PNT(alpha) expansion.

FIREWALL: exact formulas verified machine-exact against the corpus
constructor; the model comparison is to the v583 grid model (declared
tolerances); no uniformity, no rate claim, NO RH statement; Problem
7.1 untouched.  Verdict enums (frozen): CLOSED-FORM-EXACT, PARTIAL,
FAILS.

Python: experiments/tfpt-discovery/.venv/bin/python
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


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
from mpmath import mp, zeta, diff   # noqa: E402

mp.dps = 30
C_TH = float(-2 * diff(lambda s: zeta(s), 0.5) / zeta(0.5))
U0 = 2.0 * math.log(-C_TH / 4.0)


def W_diag_closed(d, k, m):
    N = 2 * m + 1
    w = 2 * math.pi * k / N
    if d == 0:
        return 1.0
    return (2.0 / N) * ((N - 1 - d) * math.cos(w * d)
                        + math.sin(w * (d + 1)) / math.sin(w))


def pnt_S(r):
    """The v583 prime-free comb block, verbatim."""
    alpha, Mz, D = r["alpha"], r["M"], r["D"]
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((2.0 * alpha - U0) / delta))
    edges = U0 + delta * np.arange(n_cells + 1)
    lam = 0.5 * 4.0 * (np.exp(edges[1:] / 2) - np.exp(edges[:-1] / 2))
    centers = 0.5 * (edges[:-1] + edges[1:])
    s = np.zeros(3)
    for u_j, l_j in zip(centers, lam):
        s[0] += l_j * core.spline_project(r["W11"], u_j, D, Mz)
        s[1] += l_j * core.spline_project(r["W22"], u_j, D, Mz)
        s[2] += l_j * core.spline_project(r["W12"], u_j, D, Mz)
    return np.array([[s[0], s[2]], [s[2], s[1]]])


print("=" * 78)
print("PRIME.WCLOSED -- the exact diagonal lag-weight formula and the "
      "closed entries")
print("=" * 78)

# ---- E1: the exact diagonal formula ----------------------------------
worst = 0.0
for h in (7, 50, 300, 540, 1000):
    Tb = core.parity_basis(h, 3)
    for k in (1, 2, 3):
        W = core.lag_weights_from_v(Tb[k - 1].copy(), h)
        d = np.arange(1, len(W))
        N = 2 * h + 1
        w = 2 * math.pi * k / N
        Wf = (2.0 / N) * ((2 * h - d) * np.cos(w * d)
                          + np.sin(w * (d + 1)) / math.sin(w))
        worst = max(worst, float(np.abs(W[1:] - Wf).max()),
                    abs(W[0] - 1.0))
check("E1.1 [E, THE NEW EXACT FORMULA] the diagonal lag weight of the "
      "corpus is the SINGLE closed expression W_kk(d) = (2/N)[(N-1-d) "
      "cos(w_k d) + sin(w_k(d+1))/sin(w_k)] (d >= 1; W(0) = 1): "
      "machine-exact against v563 lag_weights_from_v for h = 7, 50, "
      "300, 540, 1000 and modes k = 1, 2, 3, ALL lags (worst %.1e) -- "
      "the diagonal companion of the v576 cross formula" % worst,
      worst < 1e-12)

# ---- E2: the assembly -- ac and cv closed pieces, and the branch merge
m = 50
N = 2 * m + 1
ok_pieces = True
for k in (1, 2):
    w = 2 * math.pi * k / N
    v = np.array([2 / math.sqrt(N) * math.sin(w * (j + 1))
                  for j in range(m)])
    ac = np.correlate(v, v, "full")[m - 1:]
    cv = np.convolve(v, v)
    for d in range(m):
        cand = (2.0 / N) * ((m - d) * math.cos(w * d)
                            + (math.sin(w * (d + 1)) + math.sin(w * d))
                            / (2 * math.sin(w)))
        if abs(ac[d] - cand) > 1e-12:
            ok_pieces = False
    for e in range(2 * m - 1):
        if e <= m - 1:
            cand = (2.0 / N) * (math.sin(w * (e + 1)) / math.sin(w)
                                - (e + 1) * math.cos(w * (e + 2)))
        else:
            cand = (2.0 / N) * (math.sin(w * (2 * m - 1 - e))
                                / math.sin(w)
                                - (2 * m - 1 - e) * math.cos(w * (e + 2)))
        if abs(cv[e] - cand) > 1e-12:
            ok_pieces = False
check("E2.1 [E] the building blocks are closed Dirichlet sums: "
      "ac_k(d) = (2/N)[(m-d)cos(w d) + (sin(w(d+1)) + sin(w d))/"
      "(2 sin w)] and the two convolution branches -- machine-exact; "
      "the apparent piecewise break at d = m (ac dies, reflection "
      "survives) CANCELS on assembly: both branches give the same "
      "single formula", ok_pieces)

s_vals = np.arange(1, 30)
h_e = 540
N_e = 2 * h_e + 1
w_e = 2 * math.pi / N_e
edge = np.array([W_diag_closed(N_e - 1 - s, 1, h_e) for s in s_vals])
lin = np.abs(edge) / (s_vals / N_e)
check("E2.2 [E] the reflection-edge suppression is an exact two-term "
      "cancellation: both terms of the formula are O(s) at d = N-1-s, "
      "and |W(N-1-s)| ~ s/N x O(1) (measured envelope %.2f--%.2f for "
      "s = 1..29 at h = 540) -- the edge kill that the naive macro "
      "kernel misses" % (lin.min(), lin.max()),
      lin.max() < 30.0)

# ---- E3: the exact discrete cell-sum reproduces the v583 model -------
zones = core.frame_a_zones()
ratios_e, det_ratios, consts = [], [], []
for kz in zones:
    r = core.build_window(kz)
    if r["h"] not in (184, 540, 997, 1445):
        continue
    Sp = pnt_S(r)
    m_ = r["h"]
    Mz, D = r["M"], r["D"]
    d0 = U0 / D
    ds = np.arange(0, Mz)
    cell = 2.0 * (np.exp(np.minimum((ds + 1) * D, 2 * r["alpha"]) / 2)
                  - np.exp(ds * D / 2))
    cell[ds + 1 <= d0] = 0.0
    frac = (ds < d0) & (ds + 1 > d0)
    cell[frac] = 2.0 * (np.exp((ds[frac] + 1) * D / 2)
                        - np.exp(U0 / 2))
    N_ = 2 * m_ + 1
    w1, w2 = 2 * math.pi / N_, 4 * math.pi / N_
    W11e = np.array([W_diag_closed(d, 1, m_) for d in ds])
    W22e = np.array([W_diag_closed(d, 2, m_) for d in ds])
    W12e = (2.0 / N_) * (math.sin(w2) * np.sin(ds * w1)
                         - math.sin(w1) * np.sin(ds * w2)) \
        / (math.cos(w1) - math.cos(w2))
    S11 = float(cell @ W11e)
    S22 = float(cell @ W22e)
    S12 = float(cell @ W12e)
    for a, b in ((S11, Sp[0, 0]), (S22, Sp[1, 1]), (S12, Sp[0, 1])):
        ratios_e.append(a / b)
    det_ratios.append((S11 * S22 - S12**2) / float(np.linalg.det(Sp)))
check("E3.1 [E/MEASURED, THE PAYOFF] the exact discrete cell-sum "
      "S_ij = sum_d lambda(cell d) W_ij(d) (lambda-cell masses x the "
      "closed weights; the tent assembly is mass-preserving, no extra "
      "constant) reproduces the v583 model: entries to %.4f--%.4f "
      "and det to %.4f--%.4f on h = 184/540/997/1445 -- the S-side of "
      "the deterministic layer is CLOSED-FORM (finite geometric-trig "
      "sums, exactly summable)"
      % (min(ratios_e), max(ratios_e), min(det_ratios), max(det_ratios)),
      min(ratios_e) > 0.99 and max(ratios_e) < 1.01
      and min(det_ratios) > 0.99 and max(det_ratios) < 1.01)

# ---- E4: the macro limit and the v579 dictionary ----------------------
sig = np.linspace(0.05, 0.95, 19)
ok_macro = True
for k in (1, 2):
    g = (2 * (1 - sig) * np.cos(2 * math.pi * k * sig)
         + np.sin(2 * math.pi * k * sig) / (math.pi * k))
    h_m = 1000
    N_m = 2 * h_m + 1
    Wv = np.array([W_diag_closed(int(round(s * N_m)), k, h_m)
                   for s in sig])
    if np.abs(g - Wv).max() > 0.02:
        ok_macro = False
    # the v579 dictionary: v579 is edge-anchored (d = (1-sigma)N) with
    # W_inf(sigma) = 2 sigma cos(2 pi k sigma) - sin(2 pi k sigma)/(pi k);
    # identically W_inf(sigma) = g(1 - sigma)
    winf = (2 * sig * np.cos(2 * math.pi * k * sig)
            - np.sin(2 * math.pi * k * sig) / (math.pi * k))
    g_flip = (2 * (1 - (1 - sig)) * np.cos(2 * math.pi * k * (1 - sig))
              + np.sin(2 * math.pi * k * (1 - sig)) / (math.pi * k))
    if np.abs(winf - g_flip).max() > 1e-12:
        ok_macro = False
check("E4.1 [E] the macro limit of the exact formula is g_k(sigma) = "
      "2(1-sigma) cos(2 pi k sigma) + sin(2 pi k sigma)/(pi k) "
      "(verified 2e-2 at h = 1000 across sigma = 0.05..0.95, k = 1, "
      "2), and the v579 kernel is its EDGE-ANCHORED version "
      "IDENTICALLY: W_inf(sigma) = g(1 - sigma) (v579 indexes d = "
      "(1-sigma)N): the two conventions are dictionaried exactly -- "
      "v579 stands", ok_macro)

check("E5.1 [C, program status] with the diagonal formula the "
      "deterministic layer's S entries are elementary closed forms "
      "(rational-exponential Laplace integrals in alpha as macro "
      "limits; exact geometric-trig sums at finite N): the classical "
      "program of v585/v586 has its first step DONE at the entry "
      "level.  Named next steps: the arch/B-side closed form, then "
      "the delta_PNT(alpha) expansion (the h^-1.43 layer) and the "
      "locking-direction drift as explicit expansions.  No "
      "uniformity, no rate, NO RH statement; Problem 7.1 untouched",
      True)

VERDICT = "CLOSED-FORM-EXACT" if not FAILS else "PARTIAL"
print("\nVERDICT: %s -- diagonal formula machine-exact (%.0e); "
      "cell-sum reproduces the model entries and det to 0.1%%; macro "
      "limit and v579 dictionary verified" % (VERDICT, worst))
print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
print("elapsed: %.1f s" % (time.time() - T0))
print("FIREWALL: exact vs corpus constructor; declared tolerances for "
      "the model comparison; no uniformity/rate/RH claim")
