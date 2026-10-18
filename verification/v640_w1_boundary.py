"""v640 -- PRIME.WEIL.BOUNDARY.01: the W1 boundary closure -- the typed
remainder of v631
(D6: the d <= 2 boundary cells and the second-order discretization term)
is CLOSED SYMBOLICALLY, and the closure is certified at 20+ digits.

CONVENTION ERRATUM (2026-08-02, corrected the same day; machine
evidence: v643_w1_theorem.py C0.1):
  The w1 chain read Suzuki's eq. (1.3) with Lerch coefficient -1;
  Suzuki's own Sec. 2.2 data (A = (1/2)(log 2 pi - psi(2)), g(0) = 0,
  r_1'' = rho - 1/(2|t|)) LOCK it to +1/4.  The g_sm below is the
  smooth layer of the chain kernel gtil := g - (5/4) Lerch, and every
  identity below is a CORRECT, certified identity of gtil -- via the
  exact transfer cgal_sm(gtil) = -4 cgal_sm(g) all numbers transfer
  verbatim, so NO check changes.  Only the labels do: on Suzuki's TRUE
  g the boundary equation is simply A_arch = -g''_smooth EXACTLY at
  every lag, with NO constant and NO scalar -- the candidate origin
  constant vanishes, kappa = 0 exactly (v643 P2.2), and the
  "-(5/4)(log pi - psi(1/4)) delta_0" term below is the artifact of
  the -1 misreading (it is the delta_0 weight OF THE MISREAD KERNEL,
  not of Suzuki's g): the v563 near-cell scheme IS Suzuki's origin
  bookkeeping.  The boundary constants B(0..2) remain exact
  gtil-normalization data; their true-g counterparts Btil(0..2) are
  computed in v643 P2.3.  Where the text below writes "Suzuki
  delta_0 weight" or "g''_smooth", read the gtil-normalization used
  by this chain; see the erratum and v643.

The chain (Suzuki arXiv:2606.09096, eq. 1.3; v563/v630/v631 read-only;
gtil-normalization per the erratum above):

  (B1) [E, sympy] the duplication identity psi(1/4) = -gamma - 3 log 2
       - pi/2 (the "one Gauss/duplication identity" typed in v631 D6).

  (B2) [E, sympy] the scheme conversion: v563's _arch_A_near pairs the
       arch density rho(w) = e^{-w/2}/(1-e^{-2w}) with the e^{-3w/2}
       regularizer and delta weight -(gamma + log pi).  The conversion
       to the PLAIN subtraction scheme (phi(w)+phi(-w)-2 phi(0)) costs
       exactly 2k with k = int_0^inf rho (1 - e^{-3w/2}) dw
       = (1/2)(psi(1) - psi(1/4)) = (3 log 2 + pi/2)/2, term-wise
       geometric.  Hence the TFPT delta_0 weight in the plain scheme is
       -(gamma + log pi) - 2k = psi(1/4) - log pi = -L,
       L := log pi - psi(1/4): EXACTLY the (negated) coefficient of
       Suzuki's linear |t| term.  The two delta_0 conventions
       (gamma + log pi vs psi(1/4) - log pi) are ONE object in ONE
       scheme -- the D6 remainder item closes.

  (B3) [E] the origin kinks of the screw function, typed exactly:
       pole block -4(e^{t/2}+e^{-t/2}-2): kink 0 at 0 (sympy limit),
       second derivative -2 cosh(t/2) is a plain density (NO delta_0);
       Lerch block f(t) = e^{-t/2} Phi(e^{-2t},2,1/4): term-wise
       f'(t) = -2 e^{-t/2} Phi(e^{-2t},1,1/4)
             = -2 [log((1+y)/(1-y)) + 2 arctan y],  y = e^{-t/2}
       (closed form, certified 30 digits), so
       f'(t) = 2 log t - (4 log 2 + pi) + o(1):
       the kink is LOG-DIVERGENT with exact finite part -(4 log 2 + pi)
       -- it carries NO discrete delta_0 in the plain scheme; the
       divergence is the non-integrable 2/|t| head of the density 4 rho
       and lives in the PV pairing.  The |t| term alone carries the
       delta_0 weight +L.

  (B4-B6) [E, 20+ digits] THE EXACT BOUNDARY EQUATION.  As distributions
       (paired with the v563 tents, d = 0, 1, 2):

         A_arch = (1/4) g''_smooth - (5/4) L delta_0,

       g''_smooth := g'' + 2 cosh(t/2) - prime atoms (= L delta_0 +
       PV[-4 rho]).  Equivalently: TFPT delta_0 weight = (1/4) x Suzuki
       delta_0 weight + pole share (= 0, B3) - (5/4)(log pi - psi(1/4)).
       Verified: v563's verbatim near/far assembly (mpmath) against the
       POINT ROUTE (1/D)[G((d-1)D) - 2 G(dD) + G((d+1)D)] of the smooth
       screw-function layer -- both sides independent, residuals < 1e-25
       relative.

  (B7-B8) [E, 20+ digits] the heavy Galerkin route closes cell by cell:
       the v631 double integrals (reduced exactly to 1-D correlation
       form) satisfy cgal(d) = poleK(d) - <g''_sm, K_d> with the CLOSED
       pole formula poleK(d) = 2 cosh(dD/2) 16 (e^{D/2}+e^{-D/2}-2)^2
       / D^2, and the full boundary dictionary

         c_ar[d] = -(1/(4D)) (cgal(d) - poleK(d)) + B(d),

       with B(d) = (1/4) <g''_sm, tent_d - K_d / D> - (5/4) L delta_{d0}
       explicit (printed to 25 digits): the d <= 2 cells are no longer a
       remainder -- they are three computable constants.

  (B9) [E, sympy] the second-order term, exact: tent read (TFPT lags)
       = D [f + D^2/12 f'' + D^4/360 f'''' + D^6/20160 f^(6)];
       hat-autocorrelation read (Galerkin lags, cubic B-spline knots
       (1,4,1)/6) = D^2 [f + D^2/6 f'' + D^4/80 f'''' + 17 D^6/30240
       f^(6)] -- c_2 = 1/6 vs 1/12, so the -4D dictionary carries the
       exact leading correction ratio 1 + (D^2/12)(rho''/rho)(dD)
       -> 1 + 1/(6 d^2) (window-independent!).

  (B10) [E-float + E-quad] the measured v631 D4 profile 1.0212 /
       1.0068 / 1.0033 / 1.0020 / 1.0011 / 1.0006 (d = 3,5,7,9,12,16)
       is REPRODUCED and PREDICTED by B9's closed correction factor --
       the 1/d^2 profile is the derived discretization law, not a fit.

Verdict enums (frozen): W1-BOUNDARY-CLOSED (all pass), BOUNDARY-OPEN,
MIXED.

FIREWALL: v563/v630/v631 read-only; no marker moves; no positivity
claim, no RH statement; the L^2_0 projection was the named last
theorem-level W1 remainder at promotion time (since closed by the
v643 projection lemma; see the erratum block above).

PROVENANCE: discovery probe w1_boundary_closure_probe.py (2026-08-02,
11/11, verdict W1-BOUNDARY-CLOSED; Suzuki arXiv:2606.09096 eq. 1.3).

Python-only (sympy exact + mpmath 20-50 digit certificates), counted
per GATE.WOLFRAM.02.
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

# v631 float machinery (verbatim), for the B10 reproduction
N_LERCH = 20000
_NN_L = np.arange(N_LERCH, dtype=float)
_WTS = 1.0 / (_NN_L + 0.25) ** 2

QUOTED_D4 = {3: 1.0212, 5: 1.0068, 7: 1.0033, 9: 1.0020,
             12: 1.0011, 16: 1.0006}   # v631 D4, printed %.4f


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("W1 BOUNDARY CLOSURE -- the typed d <= 2 / second-order remainder")
    print("=" * 78)

    # ------------------------------------------------------------------ B1
    gam, lp = sp.EulerGamma, sp.log(sp.pi)
    psi14 = sp.digamma(sp.Rational(1, 4))
    dup = sp.simplify(psi14 - (-gam - 3 * sp.log(2) - sp.pi / 2))
    check("B1.1 [E] the duplication identity psi(1/4) = -gamma - 3 log 2 "
          "- pi/2 (sympy exact) -- the 'one Gauss/duplication identity' "
          "of the v631 D6 remainder", dup == 0)

    # ------------------------------------------------------------------ B2
    n = sp.symbols("n", integer=True, nonnegative=True)
    w = sp.symbols("w", positive=True)
    # (i) rho is the geometric series sum_n e^{-(2n+1/2) w}
    xg = sp.symbols("xg")
    geo = sp.Sum(xg ** n, (n, 0, sp.oo)).doit()
    geo_val = geo.args[0][0] if isinstance(geo, sp.Piecewise) else geo
    ok_geo = sp.simplify(
        sp.exp(-w / 2) * geo_val.subs(xg, sp.exp(-2 * w))
        - sp.exp(-w / 2) / (1 - sp.exp(-2 * w))) == 0
    # (ii) per-mode integral (positive decay symbol) + partial fractions
    a = sp.symbols("a", positive=True)
    term = sp.integrate(sp.exp(-a * w) * (1 - sp.exp(-3 * w / 2)),
                        (w, 0, sp.oo))
    ok_term = sp.simplify(term - (1 / a - 1 / (a + sp.Rational(3, 2)))) == 0
    ok_pf = sp.simplify(
        (1 / (2 * n + sp.Rational(1, 2)) - 1 / (2 * n + 2))
        - sp.Rational(1, 2) * (1 / (n + sp.Rational(1, 4))
                               - 1 / (n + 1))) == 0
    # (iii) k exactly, via u = e^{-w/2} (the integral becomes rational)
    uu_ = sp.symbols("uu_", positive=True)
    integrand_w = (sp.exp(-w / 2) - sp.exp(-2 * w)) / (1 - sp.exp(-2 * w))
    ok_sub = sp.simplify(
        integrand_w.subs(w, -2 * sp.log(uu_)) * (2 / uu_)
        - 2 * (1 - uu_ ** 3) / (1 - uu_ ** 4)) == 0
    k_val = sp.integrate(2 * (1 - uu_ ** 3) / (1 - uu_ ** 4), (uu_, 0, 1))
    k_closed = (3 * sp.log(2) + sp.pi / 2) / 2
    ok_k = sp.simplify(k_val - k_closed) == 0
    # k = (1/2)(psi(1) - psi(1/4)) via B1
    ok_kpsi = sp.simplify(
        (sp.digamma(1) - psi14) / 2 - k_closed) == 0
    # 30-digit quad certificate
    mp.mp.dps = 35
    kq = mp.quad(lambda x: (mp.exp(-x / 2) - mp.exp(-2 * x))
                 / (-mp.expm1(-2 * x)), [0, 1, 5, mp.inf])
    ok_kq = abs(kq - (3 * mp.log(2) + mp.pi / 2) / 2) < mp.mpf(10) ** -28
    # (iv) the scheme move: -(gamma+log pi) - 2k = psi(1/4) - log pi
    ok_scheme = sp.simplify((-gam - lp - 2 * k_closed)
                            - (psi14 - lp)) == 0
    check("B2.1 [E] scheme conversion k = int rho (1 - e^{-3w/2}) dw = "
          "pi/4 + (3/2) log 2 = (1/2)(psi(1)-psi(1/4)) (sympy exact: "
          "geometric rho, per-mode integral, u = e^{-w/2} rational "
          "route; 30-digit quad certificate), hence the TFPT delta_0 "
          "weight in the plain scheme is -(gamma+log pi) - 2k = "
          "psi(1/4) - log pi: EXACTLY Suzuki's linear coefficient -- "
          "one delta_0 convention, one scheme",
          ok_geo and ok_term and ok_pf and ok_sub and ok_k and ok_kpsi
          and ok_kq and ok_scheme)

    # ------------------------------------------------------------------ B3
    t = sp.symbols("t", positive=True)
    pole_kink = sp.limit(sp.diff(-4 * (sp.exp(t / 2) + sp.exp(-t / 2) - 2),
                                 t), t, 0, "+")
    # Lerch derivative closed form: f'(t) = -2[log((1+y)/(1-y)) + 2 atan y]
    mp.mp.dps = 35
    ok_closed = True
    for tv in (mp.mpf(3) / 10, mp.mpf(1), mp.mpf(2)):
        lhs = mp.diff(lambda s: mp.exp(-s / 2)
                      * mp.lerchphi(mp.exp(-2 * s), 2, mp.mpf(1) / 4), tv)
        y = mp.exp(-tv / 2)
        rhs = -2 * (mp.log((1 + y) / (1 - y)) + 2 * mp.atan(y))
        if abs(lhs - rhs) / abs(rhs) > mp.mpf(10) ** -28:
            ok_closed = False
    # exact finite part of the kink via sympy limit of the closed form
    y_of_t = sp.exp(-t / 2)
    fprime = -2 * (sp.log((1 + y_of_t) / (1 - y_of_t))
                   + 2 * sp.atan(y_of_t))
    fin_part = sp.limit(fprime - 2 * sp.log(t), t, 0, "+")
    ok_fin = sp.simplify(fin_part - (-(4 * sp.log(2) + sp.pi))) == 0
    check("B3.1 [E] origin kinks typed: pole kink at 0+ is 0 (sympy limit"
          " = %s; -2 cosh(t/2) is a plain density, NO delta_0); Lerch "
          "kink f'(t) = -2[log((1+y)/(1-y)) + 2 atan y], y = e^{-t/2} "
          "(30-digit certificates at t = 0.3, 1, 2) = 2 log t - "
          "(4 log 2 + pi) + o(1): log-divergent, exact finite part "
          "-(4 log 2 + pi), NO discrete delta_0 -- it is the PV head "
          "2/|t| of 4 rho" % pole_kink,
          pole_kink == 0 and ok_closed and ok_fin)

    # ------------------------------------------- the window (h = 184)
    kz = core.frame_a_zones()[0]
    r = core.build_window(kz)
    alpha, Mz = r["alpha"], r["M"]
    c_ar_f = core.arch_lags(Mz, r["D"])

    mp.mp.dps = 55
    D = mp.mpf(r["D"])          # the exact binary64 lattice constant
    EULER_MP = mp.euler
    LOGPI_MP = mp.log(mp.pi)
    PSI14_MP = mp.digamma(mp.mpf(1) / 4)
    LL = LOGPI_MP - PSI14_MP    # L = log pi - psi(1/4) > 0
    PHI1 = mp.lerchphi(1, 2, mp.mpf(1) / 4)

    def rho_mp(x):
        return mp.exp(-x / 2) / (-mp.expm1(-2 * x))

    def tent_mp(x, dd):
        v = 1 - abs(x - dd * D) / D
        return v if v > 0 else mp.mpf(0)

    def K_mp(x):
        u = abs(x) / D
        if u >= 2:
            return mp.mpf(0)
        if u <= 1:
            return D * (mp.mpf(2) / 3 - u ** 2 + u ** 3 / 2)
        return D * (2 - u) ** 3 / 6

    def g_sm(tv):
        """smooth screw layer: linear + const + Lerch (t >= 0)."""
        tv = mp.mpf(tv)
        if tv == 0:
            return -PHI1 / 4 - PHI1
        return (LL * tv / 2 - PHI1 / 4 - mp.exp(-tv / 2)
                * mp.lerchphi(mp.exp(-2 * tv), 2, mp.mpf(1) / 4))

    def g_pole(tv):
        return -4 * (mp.exp(tv / 2) + mp.exp(-tv / 2) - 2)

    def g_full(tv):
        tv = abs(mp.mpf(tv))
        assert tv < mp.log(2)   # boundary cells only: below the 1st atom
        return g_pole(tv) + g_sm(tv)

    # v563 near/far assembly, verbatim, in mpmath
    def c_ar_verbatim(dd):
        if dd >= 1:             # _arch_A_far
            return -mp.quad(lambda x: tent_mp(x, dd) * rho_mp(x),
                            [(dd - 1) * D, dd * D, (dd + 1) * D])
        W = D                   # _arch_A_near at s = 0
        def integ(x):
            S = (tent_mp(x, 0) + tent_mp(-x, 0)) / 2
            return (mp.exp(-2 * x) - S * mp.exp(-x / 2)) / (-mp.expm1(-2 * x))
        return (-(EULER_MP + LOGPI_MP) + 2 * mp.quad(integ, [0, W])
                - mp.log(-mp.expm1(-2 * W)))

    # <g''_sm, tent_d>: POINT route (exact integration by parts: the tent's
    # second derivative is (delta_{(d-1)D} - 2 delta_{dD} + delta_{(d+1)D})/D)
    def gsm_tent_point(dd):
        return (g_sm(abs(dd - 1) * D) - 2 * g_sm(dd * D)
                + g_sm((dd + 1) * D)) / D

    # <g''_sm, tent_d>: DISTRIBUTIONAL route (L delta_0 + PV[-4 rho])
    def gsm_tent_dist(dd):
        if dd == 0:
            pv = (mp.quad(lambda x: rho_mp(x) * (-2 * x / D), [0, D])
                  + mp.quad(lambda x: -2 * rho_mp(x), [D, 1, 5, mp.inf]))
            return LL - 4 * pv
        pv = mp.quad(lambda x: rho_mp(x) * tent_mp(x, dd),
                     [max(0, (dd - 1)) * D, dd * D, (dd + 1) * D])
        return -4 * pv

    # <g''_sm, K_d> distributional (K = hat autocorrelation, mass D^2)
    def gsm_K_dist(dd):
        K0 = K_mp(dd * D)
        def comb(x):
            return K_mp(x - dd * D) + K_mp(x + dd * D) - 2 * K0
        pts = sorted({max(0, (dd + j)) * D for j in (-2, -1, 0, 1, 2)})
        pv = mp.quad(lambda x: rho_mp(x) * comb(x), pts)
        if K0 > 0:
            pv += mp.quad(lambda x: rho_mp(x) * (-2 * K0),
                          [pts[-1], 1, 5, mp.inf])
        return LL * K0 - 4 * pv

    def poleK_closed(dd):
        X = mp.exp(D / 2) + mp.exp(-D / 2) - 2
        return 2 * mp.cosh(dd * D / 2) * 16 * X ** 2 / D ** 2

    def poleK_quad(dd):
        return mp.quad(lambda x: 2 * mp.cosh(x / 2) * K_mp(x - dd * D),
                       [(dd + j) * D for j in (-2, -1, 0, 1, 2)])

    def II_heavy(kk):
        """II(k) = int int_{[0,D]^2} g(kD + x - y) dx dy, reduced exactly
        to the 1-D correlation form int g(kD+s)(D-|s|) ds."""
        kk = abs(kk)
        return mp.quad(lambda s: g_full(kk * D + s) * (D - abs(s)),
                       [-D, 0, D])

    II_cache = {kk: II_heavy(kk) for kk in range(4)}

    def cgal_heavy(dd):
        return (2 * II_cache[dd] - II_cache[abs(dd - 1)]
                - II_cache[dd + 1]) / D ** 2

    # ------------------------------------------------------------------ B4
    devs4 = [abs(c_ar_verbatim(dd) - mp.mpf(float(c_ar_f[dd])))
             for dd in range(3)]
    check("B4.1 [E-float] the mpmath verbatim near/far assembly matches "
          "v563's float lags c_ar[0..2] (max |diff| %.1e < 5e-13): same "
          "object, higher precision" % float(max(devs4)),
          float(max(devs4)) < 5e-13,
          "c_ar[0..2] = %s" % [mp.nstr(c_ar_verbatim(dd), 20)
                               for dd in range(3)])

    # ------------------------------------------------------------------ B5
    res5 = []
    for dd in range(3):
        a, b = gsm_tent_point(dd), gsm_tent_dist(dd)
        res5.append(abs(a - b) / abs(a))
    check("B5.1 [E, 20+ digits] the distributional bookkeeping of the "
          "smooth layer is EXACT: point route (1/D)[G((d-1)D) - 2G(dD) + "
          "G((d+1)D)] = L delta_0 + PV[-4 rho] paired with the tent, "
          "d = 0,1,2 (worst relative residual %s < 1e-25) -- the "
          "|t|-kink carries + L delta_0, the Lerch block is pure PV"
          % mp.nstr(max(res5), 3), max(res5) < mp.mpf(10) ** -25)

    # ------------------------------------------------------------------ B6
    res6 = []
    vals6 = []
    for dd in range(3):
        lhs = c_ar_verbatim(dd)
        rhs = gsm_tent_point(dd) / 4 - (mp.mpf(5) / 4) * LL * (dd == 0)
        res6.append(abs(lhs - rhs) / abs(lhs))
        vals6.append((lhs, rhs))
    check("B6.1 [E, 20+ digits] THE EXACT BOUNDARY EQUATION (gtil-"
          "normalization, see erratum) A_arch = (1/4) gtil''_smooth "
          "- (5/4)(log pi - psi(1/4)) delta_0: TFPT delta_0 weight = "
          "(1/4) gtil delta_0 weight + pole share (= 0) - (5/4) L, "
          "verified against the tents d = 0,1,2 (worst relative "
          "residual %s < 1e-22); L = %s, (5/4)L = %s.  On Suzuki's "
          "TRUE g the same tents read A_arch = -g''_smooth with NO "
          "constant: kappa = 0 exactly (v643 P2.2)"
          % (mp.nstr(max(res6), 3), mp.nstr(LL, 25),
             mp.nstr(mp.mpf(5) / 4 * LL, 25)),
          max(res6) < mp.mpf(10) ** -22)
    for dd in range(3):
        print("      d=%d: c_ar = %s" % (dd, mp.nstr(vals6[dd][0], 25)))
        print("           rhs  = %s" % mp.nstr(vals6[dd][1], 25))

    # ------------------------------------------------------------------ B7
    ok_pole = max(abs(poleK_closed(dd) - poleK_quad(dd))
                  / poleK_closed(dd) for dd in range(3)) < mp.mpf(10) ** -25
    res7 = []
    for dd in range(3):
        heavy = cgal_heavy(dd)
        dist = poleK_closed(dd) - gsm_K_dist(dd)
        res7.append(abs(heavy - dist) / abs(heavy))
    check("B7.1 [E, 20+ digits] the heavy Galerkin route closes: "
          "cgal(d) [v631 double integrals, exact 1-D correlation form] = "
          "poleK(d) - <g''_sm, K_d> for d = 0,1,2 (worst relative "
          "residual %s < 1e-20), with the CLOSED pole-block formula "
          "poleK(d) = 2 cosh(dD/2) 16 (e^{D/2}+e^{-D/2}-2)^2/D^2 "
          "(quad check < 1e-25)" % mp.nstr(max(res7), 3),
          ok_pole and max(res7) < mp.mpf(10) ** -20)

    # ------------------------------------------------------------------ B8
    res8 = []
    Bvals = []
    for dd in range(3):
        Bd = (gsm_tent_point(dd) - gsm_K_dist(dd) / D) / 4 \
            - (mp.mpf(5) / 4) * LL * (dd == 0)
        Bvals.append(Bd)
        lhs = c_ar_verbatim(dd)
        rhs = -(cgal_heavy(dd) - poleK_closed(dd)) / (4 * D) + Bd
        res8.append(abs(lhs - rhs) / abs(lhs))
    check("B8.1 [E, 20+ digits] the full boundary dictionary "
          "c_ar[d] = -(1/(4D))(cgal(d) - poleK(d)) + B(d) with "
          "B(d) = (1/4)<g''_sm, tent_d - K_d/D> - (5/4) L delta_{d0} "
          "EXPLICIT, d = 0,1,2 (worst relative residual %s < 1e-20): "
          "the boundary cells are three computable constants, not a "
          "remainder" % mp.nstr(max(res8), 3),
          max(res8) < mp.mpf(10) ** -20)
    for dd in range(3):
        print("      B(%d) = %s" % (dd, mp.nstr(Bvals[dd], 25)))

    # ------------------------------------------------------------------ B9
    x, Dp = sp.symbols("x", nonnegative=True), sp.symbols("Dp", positive=True)
    mphi = {2 * kk: 2 * sp.integrate((1 - x / Dp) * x ** (2 * kk),
                                     (x, 0, Dp)) for kk in range(4)}
    ok_phi = (sp.simplify(mphi[0] - Dp) == 0
              and sp.simplify(mphi[2] - Dp ** 3 / 6) == 0
              and sp.simplify(mphi[4] - Dp ** 5 / 15) == 0
              and sp.simplify(mphi[6] - Dp ** 7 / 28) == 0)
    mK = {}
    for nn in (0, 2, 4, 6):
        mK[nn] = sum(sp.binomial(nn, j) * mphi[j] * mphi[nn - j]
                     for j in (0, 2, 4, 6) if j <= nn)
    ok_K = (sp.simplify(mK[0] - Dp ** 2) == 0
            and sp.simplify(mK[2] - Dp ** 4 / 3) == 0
            and sp.simplify(mK[4] - 3 * Dp ** 6 / 10) == 0
            and sp.simplify(mK[6] - 17 * Dp ** 8 / 42) == 0)
    f0, f2, f4, f6 = sp.symbols("f0 f2 f4 f6")
    Tread = sum(mphi[2 * kk] / sp.factorial(2 * kk) * ff
                for kk, ff in enumerate((f0, f2, f4, f6)))
    Kread = sum(mK[2 * kk] / sp.factorial(2 * kk) * ff
                for kk, ff in enumerate((f0, f2, f4, f6)))
    ratio_ser = sp.series(Kread / (Dp * Tread), Dp, 0, 4).removeO()
    c2_coeff = sp.simplify(ratio_ser.coeff(Dp, 2) - f2 / (12 * f0)) == 0
    # leading law with f = rho at t = d D
    ws, ds = sp.symbols("ws", positive=True), sp.symbols("ds", positive=True)
    rho_s = sp.exp(-ws / 2) / (1 - sp.exp(-2 * ws))
    r2_s = sp.diff(rho_s, ws, 2) / rho_s
    lead = sp.limit((Dp ** 2 / 12 * r2_s).subs(ws, ds * Dp), Dp, 0, "+")
    ok_lead = sp.simplify(lead - 1 / (6 * ds ** 2)) == 0
    check("B9.1 [E] the second-order term, exact (sympy): tent read = "
          "D[f + D^2/12 f'' + D^4/360 f'''' + D^6/20160 f6], B-spline "
          "read = D^2[f + D^2/6 f'' + D^4/80 f'''' + 17 D^6/30240 f6] "
          "(moments D^3/6, D^5/15, D^7/28 vs D^4/3, 3D^6/10, 17D^8/42); "
          "ratio = 1 + (D^2/12)(f''/f) + O(D^4), and with f = rho at "
          "t = dD the leading correction is 1/(6 d^2) EXACTLY, "
          "window-independent", ok_phi and ok_K and c2_coeff and ok_lead)

    # ----------------------------------------------------------------- B10
    # (a) float reproduction of the v631 D4 profile, verbatim machinery
    UU = np.array([float(u) for u in core.U_ALL])
    MU = np.array([float(m) for m in core.MU_ALL])
    CW = np.cumsum(MU / 2.0)
    CS = np.cumsum(MU / 2.0 * UU)
    PSI14_F = float(PSI14_MP)
    LOGPI_F = math.log(math.pi)
    PHI1_F = float(PHI1)
    Df = float(r["D"])

    def g_vec(ts, pole=True):
        xf = np.abs(np.asarray(ts, dtype=float))
        kk = np.searchsorted(UU, xf, side="right")
        cw = np.where(kk > 0, CW[np.maximum(kk - 1, 0)], 0.0)
        cs = np.where(kk > 0, CS[np.maximum(kk - 1, 0)], 0.0)
        out = xf * cw - cs - xf / 2.0 * (PSI14_F - LOGPI_F) - 0.25 * PHI1_F
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
    XS = 0.5 * Df * (GX + 1)
    WS = 0.5 * Df * GW
    DIFF = (XS[:, None] - XS[None, :]).ravel()
    W2 = np.outer(WS, WS).ravel()

    def II_f(kk, **kw):
        return float(np.dot(W2, g_vec(kk * Df + DIFF, **kw)))

    def cgal_f(dd, **kw):
        return (2.0 * II_f(dd, **kw) - II_f(dd - 1, **kw)
                - II_f(dd + 1, **kw)) / (Df * Df)

    lags = (3, 5, 7, 9, 12, 16)
    vals_meas = {dd: cgal_f(dd, pole=False) / (-4.0 * Df * float(c_ar_f[dd]))
                 for dd in lags}
    ok_quote = max(abs(vals_meas[dd] - QUOTED_D4[dd]) for dd in lags) < 6e-5
    check("B10.1 [E-float] the v631 D4 profile REPRODUCED bit-for-bit at "
          "print precision: ratio(d)/(-4D) = %s vs quoted %s (max |diff| "
          "< 6e-5)" % (["%.4f" % vals_meas[dd] for dd in lags],
                       [QUOTED_D4[dd] for dd in lags]), ok_quote)

    # (b) exact-route ratios and the B9 prediction
    mp.mp.dps = 30
    rho_l = sp.lambdify(ws, rho_s, "mpmath")
    r2_l = sp.lambdify(ws, sp.diff(rho_s, ws, 2), "mpmath")
    r4_l = sp.lambdify(ws, sp.diff(rho_s, ws, 4), "mpmath")
    r6_l = sp.lambdify(ws, sp.diff(rho_s, ws, 6), "mpmath")

    def ratio_exact(dd):
        Krd = mp.quad(lambda xx: rho_mp(xx) * K_mp(xx - dd * D),
                      [(dd + j) * D for j in (-2, -1, 0, 1, 2)])
        Trd = mp.quad(lambda xx: rho_mp(xx) * tent_mp(xx, dd),
                      [(dd - 1) * D, dd * D, (dd + 1) * D])
        return Krd / (D * Trd)

    def ratio_pred(dd):
        tv = dd * D
        f, g2, g4, g6 = rho_l(tv), r2_l(tv), r4_l(tv), r6_l(tv)
        num = f + D ** 2 / 6 * g2 + D ** 4 / 80 * g4 \
            + 17 * D ** 6 / 30240 * g6
        den = f + D ** 2 / 12 * g2 + D ** 4 / 360 * g4 \
            + D ** 6 / 20160 * g6
        return num / den

    rows = []
    for dd in lags:
        re_, rp_ = float(ratio_exact(dd)), float(ratio_pred(dd))
        rows.append((dd, vals_meas[dd], re_, rp_, 1.0 + 1.0 / (6.0 * dd * dd)))
    print("      d | measured(v631) | exact-quad | predicted(B9) | 1+1/(6d^2)")
    for dd, vm, re_, rp_, rn in rows:
        print("     %2d | %.6f | %.6f | %.6f | %.6f" % (dd, vm, re_, rp_, rn))
    dev_pred = max(abs(re_ - rp_) / (re_ - 1.0) for _, _, re_, rp_, _ in rows)
    dev_route = max(abs(vm - re_) for _, vm, re_, _, _ in rows)
    ok_closure = dev_pred < 0.02 and dev_route < 3e-4
    check("B10.2 [E-quad] the 1/d^2 profile IS the derived law: the exact"
          "-quadrature ratio matches the B9 moment prediction to %s of "
          "the excess (ratio-1) at every lag (< 2%%), and the float "
          "route sits within %.1e (< 3e-4) of the exact quadrature: the "
          "second-order term of the -4D dictionary is CLOSED, "
          "quantitatively" % (mp.nstr(mp.mpf(dev_pred), 3), dev_route),
          ok_closure)

    VERDICT = "W1-BOUNDARY-CLOSED" if not FAILS else (
        "MIXED" if len(FAILS) < 4 else "BOUNDARY-OPEN")
    print("\nVERDICT: %s -- the v631 D6 remainder (boundary cells + "
          "second-order term) is symbolically closed and certified"
          % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
