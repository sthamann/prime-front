"""Discovery probe: the W1 frozen-dictionary transport -- the KILL test.

The v631 dictionary was DERIVED on the single declared window h = 184:
  (i)   smooth layer: A_arch = -(1/(4D)) x (Galerkin minus pole block),
        with the closed pole-block formula
        poleK(d) = 2 cosh(dD/2) 16 (e^{D/2}+e^{-D/2}-2)^2 / D^2
        and the DERIVED discretization law (w1_boundary_closure_probe
        B9/B10: moment brackets, leading correction 1 + 1/(6 d^2));
  (ii)  atom layer: per-atom Galerkin mass / TFPT tent mass = D^2;
  (iii) the closed per-lag ratio law c_gal/c_arch =
        -D [4 + (e^t + 1)(1 - e^{-2t})] (v631 D3).

Here the dictionary is FROZEN (all formulas closed in D, no knob) and
executed UNCHANGED on three fresh frame-A windows with distinctly
different h (285, 540, 997 -- the derivation window h = 184 excluded).
Only D = 2 alpha / M changes per window, as the dictionary itself
declares.

KILL criterion (preregistered): if any window needs a conversion beyond
the explicit D dependence -- pole-subtracted ratio not converging to 1
on the same lag numbers, atom constant not D^2(window), or the
discretization excess not following the derived 1/(6 d^2)-type law --
then W1 dies as an operator identification.  PASS: the same closed
formulas in D work everywhere.

Frozen bars (v631 D3/D4/D5 + boundary-closure B10, declared before the
fresh windows are touched): last pole-free ratio |r(16) - 1| < 3e-3
with monotone |r - 1| decrease on d = 3,5,7,9,12,16; moment prediction
explains the excess to < 2% at every lag (exact-quad route), float
route within 3e-4 of exact quad; atom constant within 1e-3 of D^2 and
atom-to-atom spread < 1e-3 (log 2 vs log 3); D3 law worst deviation
< 1.2e-2 on d = 4..9, monotonically shrinking.

Verdict enums (frozen): W1-DICTIONARY-PORTABLE (all pass on all three
windows), W1-KILLED (systematic failure on any fresh window), MIXED.

FIREWALL: experiments-only; v563/v630/v631 read-only; no marker moves;
no positivity claim, no RH statement.
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


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

# ------------------------- frozen bars (declared before any fresh data)
H_TARGETS = (286, 540, 1000)     # fresh windows near these h; h=184 excluded
LAGS_D4 = (3, 5, 7, 9, 12, 16)
TOL_D4_LAST = 3.0e-3             # v631 D4, frozen
TOL_PRED_EXCESS = 0.02           # boundary-closure B10.2, frozen
TOL_ROUTE = 3.0e-4               # float route vs exact quad, frozen
TOL_ATOM = 1.0e-3                # v631 D5, frozen
TOL_D3 = 1.2e-2                  # v631 D3, frozen

N_LERCH = 20000
_NN_L = np.arange(N_LERCH, dtype=float)
_WTS = 1.0 / (_NN_L + 0.25) ** 2


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("W1 FROZEN DICTIONARY -- the kill test on three fresh windows")
    print("=" * 78)

    mp.mp.dps = 30
    PSI14_F = float(mp.digamma(mp.mpf(1) / 4))
    LOGPI_F = math.log(math.pi)
    PHI1_F = float(mp.lerchphi(1, 2, mp.mpf(1) / 4))
    UU = np.array([float(u) for u in core.U_ALL])
    MU = np.array([float(m) for m in core.MU_ALL])
    CW = np.cumsum(MU / 2.0)
    CS = np.cumsum(MU / 2.0 * UU)

    ws = sp.symbols("ws", positive=True)
    rho_s = sp.exp(-ws / 2) / (1 - sp.exp(-2 * ws))
    rho_l = sp.lambdify(ws, rho_s, "mpmath")
    r2_l = sp.lambdify(ws, sp.diff(rho_s, ws, 2), "mpmath")
    r4_l = sp.lambdify(ws, sp.diff(rho_s, ws, 4), "mpmath")
    r6_l = sp.lambdify(ws, sp.diff(rho_s, ws, 6), "mpmath")

    def g_vec(ts, Dw, pole=True, prime_only=False):
        """v631's vectorized screw function, verbatim."""
        xf = np.abs(np.asarray(ts, dtype=float))
        kk = np.searchsorted(UU, xf, side="right")
        cw = np.where(kk > 0, CW[np.maximum(kk - 1, 0)], 0.0)
        cs = np.where(kk > 0, CS[np.maximum(kk - 1, 0)], 0.0)
        prime = xf * cw - cs
        if prime_only:
            return prime
        out = prime - xf / 2.0 * (PSI14_F - LOGPI_F) - 0.25 * PHI1_F
        if pole:
            out += -4.0 * (np.exp(xf / 2) + np.exp(-xf / 2) - 2.0)
        lb = np.empty_like(xf)
        for a in range(0, xf.size, 400):
            b = min(xf.size, a + 400)
            E = np.exp(-np.outer(2.0 * xf[a:b], _NN_L) - 0.5 * xf[a:b, None])
            lb[a:b] = E @ _WTS
        return out - lb

    from numpy.polynomial.legendre import leggauss
    GX, GW = leggauss(16)

    # ------------------------------------------ pick the three windows
    zs = core.frame_a_zones()
    cand = []
    for kz in zs:
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(core.U_ALL[kz] / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        cand.append((M_k // 2, kz))
    kz_deriv = zs[0]
    picks = []
    for tgt in H_TARGETS:
        pool = [(hh, kz) for hh, kz in cand
                if kz != kz_deriv and (hh, kz) not in picks]
        picks.append(min(pool, key=lambda p: abs(p[0] - tgt)))
    hs = [p[0] for p in picks]
    ok_pick = (len(set(hs)) == 3 and kz_deriv not in [p[1] for p in picks]
               and max(hs) - min(hs) > 300)
    check("W0.1 [E] three FRESH frame-A windows selected (derivation "
          "window h = 184 excluded), distinctly different sizes: "
          "h = %s (kz = %s)" % (hs, [p[1] for p in picks]), ok_pick)

    # ---------------------------------------------------- per window
    for wi, (hz, kz) in enumerate(picks):
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        Dw = 2.0 * alpha / Mz
        n_zone = int(core._NN[kz])
        print("\n-- window %d: h = %d, M = %d, alpha = %.6f, D = %.8f, "
              "n_zone = %d --" % (wi + 1, hz, Mz, alpha, Dw, n_zone))

        XS = 0.5 * Dw * (GX + 1)
        WS = 0.5 * Dw * GW
        DIFF = (XS[:, None] - XS[None, :]).ravel()
        W2 = np.outer(WS, WS).ravel()
        II_cache = {}

        def II_f(kk, **kw):
            key = (kk, tuple(sorted(kw.items())))
            if key not in II_cache:
                II_cache[key] = float(np.dot(
                    W2, g_vec(kk * Dw + DIFF, Dw, **kw)))
            return II_cache[key]

        def cgal_f(dd, **kw):
            return (2.0 * II_f(dd, **kw) - II_f(abs(dd - 1), **kw)
                    - II_f(dd + 1, **kw)) / (Dw * Dw)

        nlag = max(LAGS_D4) + 2
        c_ar = core.arch_A(np.arange(nlag) * Dw, Dw)

        # mpmath window kernels for the exact-quad route
        Dm = mp.mpf(Dw)

        def rho_mp(x):
            return mp.exp(-x / 2) / (-mp.expm1(-2 * x))

        def tent_mp(x, dd):
            v = 1 - abs(x - dd * Dm) / Dm
            return v if v > 0 else mp.mpf(0)

        def K_mp(x):
            u = abs(x) / Dm
            if u >= 2:
                return mp.mpf(0)
            if u <= 1:
                return Dm * (mp.mpf(2) / 3 - u ** 2 + u ** 3 / 2)
            return Dm * (2 - u) ** 3 / 6

        def ratio_exact(dd):
            Krd = mp.quad(lambda xx: rho_mp(xx) * K_mp(xx - dd * Dm),
                          [(dd + j) * Dm for j in (-2, -1, 0, 1, 2)])
            Trd = mp.quad(lambda xx: rho_mp(xx) * tent_mp(xx, dd),
                          [(dd - 1) * Dm, dd * Dm, (dd + 1) * Dm])
            return float(Krd / (Dm * Trd))

        def ratio_pred(dd):
            tv = dd * Dm
            f, g2, g4, g6 = rho_l(tv), r2_l(tv), r4_l(tv), r6_l(tv)
            num = f + Dm ** 2 / 6 * g2 + Dm ** 4 / 80 * g4 \
                + 17 * Dm ** 6 / 30240 * g6
            den = f + Dm ** 2 / 12 * g2 + Dm ** 4 / 360 * g4 \
                + Dm ** 6 / 20160 * g6
            return float(num / den)

        # (i) the pole-subtracted scalar -4D + derived discretization law
        assert (max(LAGS_D4) + 2) * Dw < math.log(2.0)
        meas, exact_q, pred = [], [], []
        for dd in LAGS_D4:
            meas.append(cgal_f(dd, pole=False) / (-4.0 * Dw * float(c_ar[dd])))
            exact_q.append(ratio_exact(dd))
            pred.append(ratio_pred(dd))
        diffs1 = [abs(v - 1.0) for v in meas]
        mono = all(diffs1[i + 1] < diffs1[i] for i in range(len(diffs1) - 1))
        dev_pred = max(abs(e - p) / (e - 1.0) for e, p in zip(exact_q, pred))
        dev_route = max(abs(m - e) for m, e in zip(meas, exact_q))
        print("   d      | " + " | ".join("%6d" % dd for dd in LAGS_D4))
        print("   meas   | " + " | ".join("%.4f" % v for v in meas))
        print("   pred   | " + " | ".join("%.4f" % v for v in pred))
        ok1 = (mono and diffs1[-1] < TOL_D4_LAST
               and dev_pred < TOL_PRED_EXCESS and dev_route < TOL_ROUTE)
        check("W%d.1 [E-float] h=%d: pole-subtracted conversion is the "
              "SCALAR -4D(window) with the DERIVED discretization law: "
              "ratio -> 1 monotonically (last %.4f, |r-1| = %.2e < 3e-3), "
              "moment prediction explains the excess to %.3f (< 0.02), "
              "route dev %.1e (< 3e-4) -- same closed formulas, only D "
              "changed" % (wi + 1, hz, meas[-1], diffs1[-1], dev_pred,
                           dev_route), ok1)

        # (ii) the atom constant D^2(window), atoms log 2 and log 3
        rs = []
        for j in (0, 1):
            u_j = float(core.U_ALL[j])
            d0 = int(round(u_j / Dw))
            m_gal = sum(cgal_f(dd, prime_only=True)
                        for dd in range(d0 - 3, d0 + 4)) * Dw
            c1, _ = core.atom_lags_at(alpha, Mz, core.U_ALL[j:j + 1],
                                      core.MU_ALL[j:j + 1])
            rs.append(m_gal / float(np.sum(c1)))
        same = abs(rs[0] - rs[1]) / abs(rs[0])
        dev_at = max(abs(rr / (Dw * Dw) - 1.0) for rr in rs)
        ok2 = same < TOL_ATOM and dev_at < TOL_ATOM
        check("W%d.2 [E-float] h=%d: the atom constant IS D^2(window): "
              "gal/tfpt mass = %.6e = %.6f x D^2 (log 2), %.6f x D^2 "
              "(log 3), spread %.1e < 1e-3 -- the frozen atomic "
              "dictionary transports with the explicit D only"
              % (wi + 1, hz, rs[0], rs[0] / (Dw * Dw), rs[1] / (Dw * Dw),
                 same), ok2)

        # (iii) the closed per-lag ratio law (v631 D3), frozen bars
        devs3 = []
        for dd in range(4, 10):
            tv = dd * Dw
            cg = cgal_f(dd)
            pr = -Dw * (4.0 + (math.exp(tv) + 1.0)
                        * (1.0 - math.exp(-2.0 * tv)))
            devs3.append(abs(cg / float(c_ar[dd]) - pr) / abs(pr))
        mono3 = all(devs3[i + 1] < devs3[i] for i in range(len(devs3) - 1))
        ok3 = max(devs3) < TOL_D3 and mono3
        check("W%d.3 [E-float] h=%d: the closed per-lag law c_gal/c_arch "
              "= -D[4 + (e^t+1)(1-e^{-2t})] holds with the frozen bars "
              "(d = 4..9, worst %.2e < 1.2e-2, monotonically shrinking)"
              % (wi + 1, hz, max(devs3)), ok3)

    n_window_fails = len([f for f in FAILS if not f.startswith("W0")])
    if not FAILS:
        VERDICT = "W1-DICTIONARY-PORTABLE"
    elif n_window_fails >= 3:
        VERDICT = "W1-KILLED"
    else:
        VERDICT = "MIXED"
    print("\nVERDICT: %s -- the frozen dictionary (closed formulas in D "
          "only) on three fresh windows" % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
