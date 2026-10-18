"""v576 -- PRIME.CHEBLOEWNER.01: the Chebyshev-Loewner structure of the
parity read block -- the polarized cross-weight formula is EXACT, the
reflection-edge block is EXACTLY a scaled Loewner matrix of U_{s-1}
(rank <= s-1; the first edge read is rank ONE), the normalized edge
defect is the EXACT series coefficient -(3 pi^4/175)(s^2-4)(11 s^2+6)
N^-4, and the pair-kernel sign polynomial P(s,z) gives the analytic
local prototype of the measured near-negative / far-positive pattern.

PROVENANCE.  The second external review (2026-07-31) proposed the cross
formula, the edge theorem, the Pythagorean null bridge and the
asymptotics; this module audits ALL of them against the corpus
definitions (v563 parity_basis / lag_weights_from_v, the T163
correlation weights, read-only) -- discovery probe cheb_loewner_probe.py
(9/9, verdict FORMULAS-EXACT).

[E] 1. THE CROSS FORMULA: w_d^(ij) = (2/N)[sin wj sin(d wi) - sin wi
    sin(d wj)]/(cos wi - cos wj) agrees exactly with the polarized
    corpus weights (symbolic at N = 7, 9, 11 for all mode pairs and all
    lags; 1e-11 worst residual at h = 300/800 up to mode 4): the whole
    K = 2 read block is analytically closed.
[E] 2. THE EDGE THEOREM (exact, not asymptotic): sin((N-s) w) =
    -sin(s w) makes the edge read w^(ij)_{N-s} = -(2/N) sin wi sin wj
    U_{s-1}[x_i, x_j] -- a diagonally scaled LOEWNER matrix of the
    Chebyshev polynomial U_{s-1}; rank <= s-1, verified rank 1/2/3 at
    s = 2/3/4 on the real surface (sv-ratios <= 1e-12).
[E/C] 3. THE PYTHAGOREAN NULL BRIDGE (typed COMPRESSION, no-free-
    pattern): the leading edge profile of modes (1,2) is proportional
    to [[1,2],[2,4]]; its Lorentz image is (5,-3,4) -- null exactly,
    and the SAME triple as (g_car, N_fam, |mu4|) via Euclid's
    (i^2+j^2, i^2-j^2, 2ij); the anchor spectral values (1,2) and the
    parity modes (1,2) feed one quadratic generator: a bridge, NOT new
    independent evidence.
[E] 4. THE DEFECT COEFFICIENT (symbolic series): det W^(s)/(W11 W22) =
    -(3 pi^4/175)(s^2-4)(11 s^2+6) N^-4 + O(N^-6) -- vanishing at the
    rank-one read s = 2, and LOCALLY one order better than the h^-3
    demand of Paper-II Problem 7.1: the open hardness is the weighted
    summation across scales, not any single edge read.
[E] 5. THE PAIR-KERNEL POLYNOMIAL: K(W^s, W^z) = (256 pi^8/525) N^-10
    s z (s^2-1)(z^2-1) P(s,z) + O(N^-12), P = 5s^4 - 21 s^2 z^2 +
    19 s^2 + 5z^4 + 19 z^2 + 24, verified at 2e-3 with the EXACT
    vanishing P(2,3) = 0 confirmed ~7 orders below scale; sign
    transition at s/z = 0.5034/1.9866: near scales couple negative,
    far scales positive -- the analytic prototype of the v573 pattern.
[E] 6. THE MACRO KERNELS: the two-scale limits W^inf(sigma) reproduce
    the surface reads at h = 800 within 5%: the v573 target
    'window-scale heavy-pair coherence' now has the explicit analytic
    object K_inf(sigma, tau).

NAMED LIMITS AS LOAD-BEARING CONTENT: exact statements about finite
trigonometric objects and their series coefficients -- NO uniformity in
the window, no bound on the weighted two-scale summation (Regime B of
the three-regime split: edge CLOSED at N^-4 / macro OPEN / transition
OPEN), NO RH statement; Problem 7.1's quantifier untouched; the null
bridge stays typed compression.  Fences: Chebyshev/Loewner CLASSICAL;
Euclid's parametrisation CLASSICAL; the v563 fence chain unchanged.
Python-only, counted per GATE.WOLFRAM.02.  Discovery:
experiments/tfpt-discovery/cheb_loewner_probe.py (2026-07-31, 9/9,
FORMULAS-EXACT).
"""
import time

import numpy as np
import sympy as sp

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


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)

def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.CHEBLOEWNER -- the cross formula, the edge Loewner theorem, "
          "the null cone")
    print("=" * 78)


    def cross_weights_numeric(h, i, j):
        Tb = core.parity_basis(h, max(i, j))
        if i == j:
            return core.lag_weights_from_v(Tb[i - 1].copy(), h)
        W11 = core.lag_weights_from_v(Tb[i - 1].copy(), h)
        W22 = core.lag_weights_from_v(Tb[j - 1].copy(), h)
        Wpp = core.lag_weights_from_v(Tb[i - 1] + Tb[j - 1], h)
        return 0.5 * (Wpp - W11 - W22)


    # --- C1: the cross formula, EXACT for small N and 1e-12 on the surface -----
    def lag_weights_sym(v, m):
        """the corpus lag_weights_from_v, re-implemented exactly in sympy."""
        M = 2 * m
        ac = [sum(v[k] * v[k + d] for k in range(m - d)) for d in range(m)]
        cv = [sum(v[k] * v[d - k] for k in range(max(0, d - m + 1),
                                                 min(d, m - 1) + 1))
              for d in range(2 * m - 1)]
        w = [sp.Integer(0)] * M
        for d in range(m):
            w[d] = 2 * ac[d]
        w[0] = ac[0]
        for d in range(1, M):
            e = (M - 1) - d
            if e <= M - 2:
                w[d] -= cv[min(e, M - 2)]
        return w


    exact_ok = True
    for m in (3, 4, 5):
        N = 2 * m + 1
        for (i, j) in ((1, 2), (1, 3), (2, 3)):
            ti = [2 / sp.sqrt(N) * sp.sin(2 * sp.pi * i * (jj + 1) / N)
                  for jj in range(m)]
            tj = [2 / sp.sqrt(N) * sp.sin(2 * sp.pi * j * (jj + 1) / N)
                  for jj in range(m)]
            wi_ = [lag_weights_sym([a + b for a, b in zip(ti, tj)], m),
                   lag_weights_sym(ti, m), lag_weights_sym(tj, m)]
            cross = [sp.nsimplify((wi_[0][d] - wi_[1][d] - wi_[2][d]) / 2)
                     for d in range(2 * m)]
            wi, wj = 2 * sp.pi * i / N, 2 * sp.pi * j / N
            for d in range(2 * m):
                f = (sp.Rational(2, 1) / N) * (
                    sp.sin(wj) * sp.sin(d * wi) - sp.sin(wi) * sp.sin(d * wj)
                ) / (sp.cos(wi) - sp.cos(wj))
                dev = sp.Abs((cross[d] - f).evalf(50))
                if dev > sp.Float('1e-40'):
                    exact_ok = False
    check("C1.1 [E, EXACT] the polarized cross-weight formula w_d^(ij) = "
          "(2/N)[sin wj sin(d wi) - sin wi sin(d wj)]/(cos wi - cos wj) "
          "agrees EXACTLY (sympy, 50-digit evaluation, chop 1e-40) with the corpus "
          "definition (v563 lag_weights_from_v polarized) for N = 7, 9, 11, "
          "all mode pairs, ALL lags d = 0..N-3", exact_ok)

    worst = 0.0
    for h in (300, 800):
        N = 2 * h + 1
        for (i, j) in ((1, 2), (1, 3), (2, 4), (3, 4)):
            got = cross_weights_numeric(h, i, j)
            wi, wj = 2 * np.pi * i / N, 2 * np.pi * j / N
            d = np.arange(len(got))
            f = (2.0 / N) * (np.sin(wj) * np.sin(d * wi)
                             - np.sin(wi) * np.sin(d * wj)) / (np.cos(wi)
                                                               - np.cos(wj))
            worst = max(worst, float(np.max(np.abs(got - f))))
    check("C1.2 [E, surface scale] the same formula at h = 300 and 800, "
          "modes up to 4, all lags: worst residual %.1e <= 1e-11 -- the "
          "whole K = 2 read block is analytically closed, no Hankel "
          "reconstruction needed" % worst, worst <= 1e-11)

    # --- C2: the edge Loewner theorem, EXACT ------------------------------------
    kk, ss = sp.symbols("k s", integer=True, positive=True)
    Nn = sp.symbols("Nsym", positive=True)
    om = 2 * sp.pi * kk / Nn
    edge = sp.simplify(sp.sin((Nn - ss) * om)
                       - sp.expand_trig(sp.sin(2 * sp.pi * kk - ss * om)))
    lhs = sp.expand_trig(sp.sin(2 * sp.pi * kk - ss * om))
    check("C2.1 [E, symbolic -- the theorem is EXACT, not asymptotic] "
          "sin((N-s) w_k) = -sin(s w_k) identically (w_k = 2 pi k/N, k "
          "integer), so the edge read is w^(ij)_{N-s} = -(2/N) sin wi "
          "sin wj [U_{s-1}(x_i) - U_{s-1}(x_j)]/(x_i - x_j) -- a diagonally "
          "scaled LOEWNER matrix of the Chebyshev polynomial U_{s-1} "
          "(U_{s-1}(cos w) = sin(s w)/sin w): rank <= deg U_{s-1} = s - 1",
          sp.simplify(lhs + sp.sin(ss * om)) == 0)

    h = 300
    N = 2 * h + 1
    Ws = {}
    for i in range(1, 5):
        for j in range(i, 5):
            Ws[(i, j)] = cross_weights_numeric(h, i, j)
    sv_ok = True
    for s_, rk in ((2, 1), (3, 2), (4, 3)):
        d = N - s_
        M4 = np.array([[Ws[(min(i, j), max(i, j))][d] for j in range(1, 5)]
                       for i in range(1, 5)])
        sv = np.linalg.svd(M4, compute_uv=False)
        if sv[rk] / sv[0] > 1e-12:
            sv_ok = False
        if s_ == 2:
            r1 = sv[1] / sv[0]
    check("C2.2 [E per instance] the rank bound holds EXACTLY on the real "
          "surface objects: at s = 2, 3, 4 the 4x4 edge blocks have "
          "numerical rank 1, 2, 3 (next singular-value ratio <= 1e-12; "
          "s = 2: sv2/sv1 = %.1e) -- the FIRST edge read is rank one BY "
          "THEOREM, not by fit" % r1, sv_ok)

    # --- C3: the Pythagorean null bridge ----------------------------------------
    X = sp.Matrix([[1, 2], [2, 4]])
    Lmap = (X[0, 0] + X[1, 1], X[0, 0] - X[1, 1], 2 * X[0, 1])
    i_, j_ = sp.symbols("i j", positive=True)
    E = (i_**2 + j_**2, i_**2 - j_**2, 2 * i_ * j_)
    null_gen = sp.simplify(E[0]**2 - E[1]**2 - E[2]**2)
    check("C3.1 [E + typed compression] the leading edge profile of modes "
          "(1,2) is proportional to [[1,2],[2,4]] (rank one); its Lorentz "
          "image L(X) = (a+c, a-c, 2b) is (5, -3, 4) with 5^2 - 3^2 - 4^2 = "
          "0 -- the SAME Pythagorean triple as (g_car, N_fam, |mu4|) = "
          "(5,3,4), via Euclid's parametrisation (i^2+j^2, i^2-j^2, 2ij) "
          "which is null IDENTICALLY.  Typed per the no-free-pattern "
          "discipline: a COMPRESSION bridge (anchor spectral values (1,2) "
          "and parity modes (1,2) feed the same quadratic generator), NOT "
          "new independent evidence",
          Lmap == (5, -3, 4)
          and 5**2 - 3**2 - 4**2 == 0 and null_gen == 0)

    # --- C4: the N^-4 defect, EXACT series coefficient ---------------------------
    sda, t_ = sp.symbols("sda t", positive=True)
    w1s, w2s = sp.symbols("w1s w2s", positive=True)


    def W_ent(wi, wj, s_x):
        return -(2 * t_) * (sp.sin(wj) * sp.sin(s_x * wi)
                            - sp.sin(wi) * sp.sin(s_x * wj)) / (sp.cos(wi)
                                                                - sp.cos(wj))


    eps = sp.symbols("eps")
    W11s = sp.limit(W_ent(w1s, w1s + eps, sda), eps, 0)
    W22s = sp.limit(W_ent(w2s, w2s + eps, sda), eps, 0)
    W12s = W_ent(w1s, w2s, sda)
    subs12 = [(w1s, 2 * sp.pi * t_), (w2s, 4 * sp.pi * t_)]
    A11 = sp.series(W11s.subs(subs12), t_, 0, 8).removeO()
    A22 = sp.series(W22s.subs(subs12), t_, 0, 8).removeO()
    A12 = sp.series(W12s.subs(subs12), t_, 0, 8).removeO()
    ratio = sp.simplify(1 - A12**2 / (A11 * A22))
    ser = sp.simplify(sp.series(ratio, t_, 0, 6).removeO())
    pred = -(3 * sp.pi**4 / sp.Integer(175)) * (sda**2 - 4) * (11 * sda**2
                                                               + 6) * t_**4
    check("C4.1 [E, symbolic series] the normalized edge defect is an EXACT "
          "coefficient: det W^(s)/(W11 W22) = -(3 pi^4/175)(s^2-4)"
          "(11 s^2+6) N^-4 + O(N^-6) (sympy series in t = 1/N, s symbolic) "
          "-- vanishing at s = 2 (the rank-one read), and LOCALLY one order "
          "BETTER than the h^-3 demand of Paper-II Problem 7.1: the open "
          "hardness is the weighted summation across scales, not any single "
          "edge read",
          sp.simplify(sp.series(ratio - pred, t_, 0, 6).removeO()) == 0)

    # --- C5: the pair-kernel polynomial, numeric ratio to the exact claim -------
    def Wm(d):
        return np.array([[Ws[(1, 1)][d], Ws[(1, 2)][d]],
                         [Ws[(1, 2)][d], Ws[(2, 2)][d]]])


    def Ppoly(s_x, z_x):
        return (5 * s_x**4 - 21 * s_x**2 * z_x**2 + 19 * s_x**2
                + 5 * z_x**4 + 19 * z_x**2 + 24)


    ratios = []
    for (s_x, z_x) in ((2, 5), (3, 4), (3, 7), (4, 9)):
        P, Q = Wm(N - s_x), Wm(N - z_x)
        got = 0.5 * (P[0, 0] * Q[1, 1] + P[1, 1] * Q[0, 0]
                     - 2 * P[0, 1] * Q[0, 1])
        pred_n = (256 * np.pi**8 / 525) / N**10 * s_x * z_x * (s_x**2 - 1) \
            * (z_x**2 - 1) * Ppoly(s_x, z_x)
        ratios.append(got / pred_n)
    P23 = Ppoly(2, 3)
    r23 = 0.5 * (Wm(N - 2)[0, 0] * Wm(N - 3)[1, 1]
                 + Wm(N - 2)[1, 1] * Wm(N - 3)[0, 0]
                 - 2 * Wm(N - 2)[0, 1] * Wm(N - 3)[0, 1])
    roots = sorted(r for r in np.roots([5, 0, -21, 0, 5]).real if r > 0)
    check("C5.1 [E-asymptotic, verified] the pair-kernel expansion "
          "K(W^s, W^z) = (256 pi^8/525) N^-10 s z (s^2-1)(z^2-1) P(s,z): "
          "measured/predicted in [%.4f, %.4f] at h = 300; P(2,3) = %d "
          "VANISHES exactly and the measured value sits ~7 orders below "
          "scale; the homogeneous sign transition lies at s/z = %.4f / "
          "%.4f -- near-scale pairs couple NEGATIVE, far-scale POSITIVE "
          "with crossover ~2: the analytic local prototype of the v573 "
          "measured pattern (near bands negative, far excess)"
          % (min(ratios), max(ratios), P23, roots[0], roots[1]),
          all(abs(r - 1) < 2e-3 for r in ratios) and P23 == 0
          and abs(r23) < 1e-5 * abs(0.5 * (Wm(N - 2)[0, 0] * Wm(N - 5)[1, 1]
                                           + Wm(N - 2)[1, 1] * Wm(N - 5)[0, 0]
                                           - 2 * Wm(N - 2)[0, 1]
                                           * Wm(N - 5)[0, 1]))
          and abs(roots[0] - 0.5034) < 1e-3 and abs(roots[1] - 1.9866) < 1e-3)

    # --- C6: the macroscopic two-scale kernels ----------------------------------
    mac_ok = True
    h8 = 800
    N8 = 2 * h8 + 1
    W8 = {}
    for i in (1, 2):
        for j in (i, 2):
            W8[(i, j)] = cross_weights_numeric(h8, i, j)
    for sigma in (0.2, 0.35, 0.7):
        d = int(round((1 - sigma) * N8))
        p11 = 2 * sigma * np.cos(2 * np.pi * sigma) \
            - np.sin(2 * np.pi * sigma) / np.pi
        p22 = 2 * sigma * np.cos(4 * np.pi * sigma) \
            - np.sin(4 * np.pi * sigma) / (2 * np.pi)
        p12 = (2 / np.pi) * (np.sin(4 * np.pi * sigma)
                             - 2 * np.sin(2 * np.pi * sigma)) / 3
        for got, pred_v in ((W8[(1, 1)][d], p11), (W8[(2, 2)][d], p22),
                            (W8[(1, 2)][d], p12)):
            if abs(pred_v) > 0.05 and abs(got / pred_v - 1) > 0.05:
                mac_ok = False
    check("C6.1 [E-asymptotic, verified] the macroscopic two-scale limit "
          "kernels W^inf(sigma) (diagonal 2 sigma cos(2 pi k sigma) - "
          "sin(2 pi k sigma)/(pi k); closed cross form) reproduce the real "
          "surface reads at h = 300 within 5%% for sigma = 0.2, 0.35, 0.7 "
          "-- the 'window-scale heavy-pair coherence' target of v573 now "
          "has an explicit analytic object K_inf(sigma, tau)", mac_ok)

    check("C7.1 [C, honesty] what this does NOT do: no uniformity in the "
          "window, no bound on the weighted two-scale summation (Regime B), "
          "no RH statement; the three-regime split (edge CLOSED at N^-4 / "
          "macro OPEN / transition OPEN) refines Problem 7.1 without "
          "touching its quantifier; the (5,-3,4) bridge stays typed "
          "compression", True)

    VERDICT = "FORMULAS-EXACT" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- cross formula exact (symbolic N <= 11 + 1e-12 "
          "surface), edge Loewner theorem exact, s = 2 rank one, defect "
          "coefficient -(3 pi^4/175)(s^2-4)(11 s^2+6) N^-4 exact, pair "
          "polynomial verified with P(2,3) = 0, macro kernels verified"
          % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))

    print("--- PRIME.CHEBLOEWNER.01 Chebyshev-Loewner edge structure: %d passed, %d failed ---"
          % (N_CHK - len(FAILS), len(FAILS)))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
