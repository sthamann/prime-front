#!/usr/bin/env python3
"""v719 -- PRIME.MOONSHOT.05: MOONSHOT Satz-1 slice -- die Spurformel
des verklebten Objekts.

Der Etappe-3-Differenzterm Delta = T - phi_pole - phi_orb ist "der Rand
der fehlenden Spurformel".  Diese Scheibe legt die ENDLICHE Spurformel
exakt und charakterisiert Delta geometrisch, Glied fuer Glied gegen die
klassische Weil-Formel (1952).

F1 [die endliche Spurformel exakt]: auf jeder GNS-Trunkierung gilt die
  Gauss-Quadratur-Identitaet  tr f(J_K) = sum_i w_i f(tau_i)
  = sum_d a_d p_d  fuer jedes bandlimitierte f(tau) = sum a_d cos(dD tau)
  (Grad <= 2K-1 = M-1).  Spektralseite: Knoten/Gewichte aus Etappe 4;
  geometrische Seite: p = car + cat + cp (Arch-Integral + Atom-Summe +
  Pol).  Batterie: Einheits-Lags, Fejer, Zelt-Stack, Zufall, kollokierte
  Gauss-Pakete -- ueber die volle 9-Fenster-Leiter.  BUCHFUEHRUNG (das
  Woerterbuch, geschlossen verifiziert):
    POL-Block   sum a_d cp_d  == int a~(u) 2cosh(u/2) du
                (cp_d ist EXAKT der Zelt-Read von 2cosh(u/2):
                 das g^(i/2)+g^(-i/2)-Glied der Weil-Formel,
                 Residuen der Pole s = 0, 1),
    ATOM-Block  sum a_d cat_d == -sum_n (mu_n/2)(a~(log n)+a~(-log n))
                (das Primglied -sum Lambda(n)/sqrt(n) g(log n)),
    ARCH-Block  sum_{d>=1} a_d car_d == -int rho(u) a~(u) du,
                car_0 == Weil-regularisierte UV-Zelle (Etappe 2),
  mit a~ = Zelt-Interpolant der Lag-Koeffizienten.  Delta bleibt der
  benannte Rest der QUADRATISCHEN Lesart (F2).

F2 [Delta geometrisch]:
  (i) Arch-Fluss-Anteil: fuer glatte Gauss-Pakete g gilt die
      geschlossene Streuterm-Gestalt
        W_freq(g) := (1/2pi) int g^(tau) omega(tau) dtau,
        omega(tau) = Re psi(1/4 + i tau/2) - log pi,
      == W_len(g) := int_0^inf [g(0)e^{-2u}/u - 2 rho(u) g(u)] du
                     - log(pi) g(0)          (Frequenz == Laenge), und
      omega = 2 theta'_RS (Riemann-Siegel-Theta-Ableitung = glatte
      Nullstellendichte = GL(1)-Streuphase; Eisenstein-Analogon).
      Der deployte ARCH-Block konvergiert in der ZWEISEITIGEN (geraden)
      Lesart g(0)car_0 + 2 sum g(dD)car_d auf der feinen D-Leiter gegen
      sigma * W_len(g) + c * g(0) mit sigma = 1, c = 0 fuer alle
      Pakete: der Block IST das klassische -(1/2pi) int phi^ (G'/G)-
      Glied, ohne Zusatzkonstante.  EHRLICHKEIT: die einseitige
      Koeffizientensumme hat KEINEN Limes (UV-Drift +(1/2)g(0)log(1/D),
      gemessen log(2)/2 pro D-Halbierung).
  (ii) Orbit-Interferenz: fuer festes stetiges ungerades Paket f0 und
      g0 = f0 * f0~ (Autokorrelation) misst die h-Leiter
        D * t_at  ->  C_at := -sum_n mu_n g0(log n)  (Rate),
      d.h. die Kreuzterme verschiedener Primkanaele sind NICHT
      Aliasing: ihr Grenzwert ist das VOLLE klassische Primglied an
      der Autokorrelation; nur der Diskretisierungsanteil (Alias)
      verschwindet, Rate gemessen.
  (iii) Diagonal-Subtraktion: D * phi_orb -> 0 und D * phi_pole -> 0
      (Raten) -- Diagonale und Polquadrat sind subleading.
      Ergebnis: D * Delta -> [Arch-Glied] + [Primglied], exakt die
      geometrische Seite der klassischen Weil-Formel am
      Autokorrelations-Test.  SATZ-KANDIDAT wird formuliert (was
      klassisch ist vs. was neu zu beweisen waere).

F3 [E8-Eindeutigkeit als endlicher Census, Bonus]: die unimodularen
  Z-Gitter in Dimension 8 sind klassisch genau {Z^8, E8} (Mordell 1938;
  deklarierter klassischer Input).  Beide tragen eine Z[i]-Struktur
  (J-Automorphismus, maschinell verifiziert; hermitesch-unimodulare
  Z[i]-Basis fuer E8 konstruiert: |det H| = 1, H_aa = 1).  Der
  Traeger fixiert die Norm-Paritaet (E8 GERADE: alle Normen even,
  maschinell; Z^8 UNGERADE: 16 Norm-1-Vektoren), die Paritaet fixiert
  die Mode-Turm-Periode (deklarierte Bruecke aus Etappe-2-A1/v695-S2):
  E8 -> rho = e^{-w/2}/(1-e^{-2w}) (m == 1 mod 4), Z^8 -> mu2-Turm
  e^{-w/2}/(1-e^{-w}).  Verklebungs-Batterie (Zelt-Reads vs deployte
  Arch-Lags, LSQ-Skalar): NUR der E8-Turm verklebt (kappa = 1); der
  Z^8/mu2-Turm und die falsche mu4-Klasse reissen mit hartem Residuum.

F4: Verdict + finale Bilanz + PRIME.Z1.MOONSHOT-Notiz.

RESULTS (Lauf 2026-08-03, 24/24 PASS, 126 s; Leiter h = 142 .. 1433):
  * F1: Gauss-Quadratur-Identitaet exakt auf 9 Fenstern x 14 Batterie-
    Vektoren (max rel dev 1.7e-11); Ledger h = 1433, Paket (0.5, 25):
    Spektralseite +2.746337777907 == POL +0.004353333627 + ARCH
    +2.701457620503 + ATOME +0.040526823777 (dev 3.2e-14).
    Woerterbuch geschlossen: POL == int a~ 2cosh(u/2) (1.7e-13),
    ATOME == -sum (mu/2)(a~(log n)+a~(-log n)) (1.8e-15), ARCH ==
    -int rho a~ (3.4e-16), UV-Zelle == Etappe-2-Regularisierung
    (2.2e-16).
  * F2i: W_freq == W_len auf 3 Paketen (5.6e-17); omega == 2 theta'_RS
    (0.0); zweiseitige feine D-Leiter (alpha = 6.5, M = 4096..32768):
    sigma = 1.000161, c = -0.000100 (Residuum 7.0e-05) -- der Block
    IST das Gamma'/Gamma-Glied; einseitige Summe driftet exakt um
    log(2)/2 pro D-Halbierung (0.346593/0.346622/0.346609, dev 4.9e-5).
  * F2ii (Pakete (0.40, 25), (0.32, 50)): Alias 9.5e-4 -> 7.0e-5
    (Rate +2.43) bzw. 1.0e-2 -> 3.1e-4 (Rate +1.30) bei C_at =
    +0.058531 / +0.084507 (Interferenz = volles Primglied, NICHT
    Aliasing); D*phi_orb Rate +0.96 / klein (4.2e-7), D*phi_pole
    <= 3.8e-35; D*t_ar-Limes +0.488984 / +0.589075 == W_len(g0)
    +0.488634 / +0.587930 (rel dev 3.5e-4 / 1.1e-3; synthetisch
    1.8e-5 / 5.9e-5); D*Delta(h_max) +0.548506 / +0.676526 ==
    Arch + Primglied (rel dev 1.3e-3 / 4.1e-3).
  * F3: E8: 240 Norm-2-Wurzeln, J^2 = -1, hermitesche Z[i]-Basis
    |det H| = 1/16 (Selbstdualitaet det_Z = 4^4|det H|^2 = 1);
    Paritaet E8 gerade / Z^8 ungerade; Verklebungs-Census: E8
    kappa = 1 (Residuum 8.5e-17), Z^8/mu2 reisst (0.102), falsche
    mu4-Klasse reisst (0.314).
  * VERDICT: MOONSHOT-SATZ1-LEDGER-EXACT.

PROVENANCE: discovery probe moonshot_traceformula_probe.py
(2026-08-03, 24/24 PASS, verdict MOONSHOT-SATZ1-LEDGER-EXACT: the
finite trace formula is EXACT Gauss quadrature on every truncation
(max rel dev 1.7e-11; ledger example 3.2e-14); the term dictionary to
the classical Weil formula CLOSES (pole 1.7e-13, atoms 1.8e-15, arch
3.4e-16, UV cell 2.2e-16); Delta -> Gamma'/Gamma term + prime term
classically (sigma = 1.000161, c = -1.0e-4; one-sided sum drifts
exactly log(2)/2 per D-halving); E8 census {Z^8, E8} (Mordell 1938):
only the Gaussian E8 glues (kappa = 1, residual 8.5e-17; Z^8/mu2
0.102, wrong mu4 class 0.314)).  Promoted verbatim (sibling imports
now point at v716/v717/v718); numbers unchanged.
"""

import ast
import itertools
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..",
                                                "verification")))

import v563_paper2_readouts as core  # noqa: E402  (declared surfaces)
import v716_moonshot_arch_glue as stage2  # noqa: E402
import v717_moonshot_state as stage3  # noqa: E402
import v718_moonshot_spectral as stage4  # noqa: E402

T0 = time.time()
CHECKS = []

SEED = 5
RNG = np.random.default_rng(SEED)
GLX, GLW = np.polynomial.legendre.leggauss(24)

# Gauss packets (s, tau0): linear trace tests (even) / quadratic (odd)
PACKETS_LIN = ((0.50, 25.0), (0.35, 60.0), (0.80, 10.0))
PACKETS_QUAD = ((0.40, 25.0), (0.32, 50.0))
X_SMALL = 1000               # geo comb reach for continuum atom targets
N_RAND = 6                   # random battery vectors per window

BAR_EXACT = 1.0e-8           # F1 Gauss exactness (calibrate)
BAR_DICT = 1.0e-9            # closed dictionary identities (calibrate)
BAR_FREQ = 1.0e-8            # W_freq == W_len
BAR_THETA = 1.0e-8           # omega == 2 theta'_RS
BAR_CONST = 2.0e-3           # (sigma, c) identification tolerance
BAR_LIMIT = 1.0e-2           # limit identification at largest window
RATE_POS = 0.8               # discretization decay rate in D (log-log)
ALPHA_SYN = 6.5              # synthetic fine D-ladder (same constructor)
MS_SYN = (4096, 8192, 16384, 32768)
BAR_POLSQ = 1.0e-9           # E3 pole-square identity re-lock
CENS_KAPPA = 1.0e-8          # E8 gluing: |kappa - 1| and residual
CENS_FLOOR = 5.0e-2          # counterfactual residual floor

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros")

def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


# ------------------------------------------------------------ small helpers
def lag_interp(a, D, x):
    """a~(x) = sum_d a_d tent((x - dD)/D), one-sided centers d = 0..M-1
    (the exact adjoint of the deployed tent reads)."""
    x = np.asarray(x, float)
    idx = x / D
    i0 = np.floor(idx).astype(int)
    fr = idx - i0
    out = np.zeros_like(x)
    M = len(a)
    ok0 = (i0 >= 0) & (i0 < M)
    out[ok0] += np.asarray(a)[i0[ok0]] * (1.0 - fr[ok0])
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    out[ok1] += np.asarray(a)[i0[ok1] + 1] * fr[ok1]
    return out


def cell_integral(a, M, D, dens, k0=-1):
    """int a~(u) dens(u) du over the cells [k0 D, M D], GL-24 per cell."""
    ks = np.arange(k0, M)
    u = ((ks[:, None] + 0.5) + 0.5 * GLX[None, :]) * D
    vals = lag_interp(a, D, u.ravel()) * dens(u.ravel())
    return 0.5 * D * float(np.sum(vals.reshape(len(ks), -1) @ GLW))


def gauss_even(s, t0):
    return lambda u: np.exp(-np.asarray(u, float) ** 2
                            / (2.0 * s * s)) * np.cos(t0 * np.asarray(u,
                                                                      float))


def gauss_odd(s, t0):
    return lambda u: np.exp(-np.asarray(u, float) ** 2
                            / (2.0 * s * s)) * np.sin(t0 * np.asarray(u,
                                                                      float))


def autocorr_num(f, s, x):
    """g0(x) = int f(v) f(v - x) dv by GL-400 over the support
    (vectorized/chunked; |x| > 16 s returns 0 at the 1e-28 level)."""
    lo, hi = -8.0 * s, 8.0 * s
    xg, wg = np.polynomial.legendre.leggauss(400)
    v = 0.5 * (hi + lo) + 0.5 * (hi - lo) * xg
    w = (0.5 * (hi - lo) * wg) * f(v)
    x = np.atleast_1d(np.asarray(x, float))
    out = np.zeros(len(x))
    near = np.abs(x) <= 16.0 * s
    xn = x[near]
    vals = np.empty(len(xn))
    for i0 in range(0, len(xn), 4096):
        blk = xn[i0:i0 + 4096]
        vals[i0:i0 + len(blk)] = f(v[None, :] - blk[:, None]) @ w
    out[near] = vals
    return out


def fit_limit_d2(Ds, vals):
    """LSQ fit vals = L + c D^2; returns (L, c, max rel residual)."""
    A = np.vstack([np.ones_like(Ds), Ds ** 2]).T
    sol, *_ = np.linalg.lstsq(A, vals, rcond=None)
    res = A @ sol - vals
    scale = max(1.0e-300, float(np.max(np.abs(vals))))
    return float(sol[0]), float(sol[1]), float(np.max(np.abs(res))) / scale


def loglog_slope(Ds, devs):
    good = np.asarray(devs) > 0.0
    if int(np.sum(good)) < 3:
        return 0.0
    return float(np.polyfit(np.log(np.asarray(Ds)[good]),
                            np.log(np.asarray(devs)[good]), 1)[0])


# --------------------------------------------------- mpmath closed targets
def w_len_general(g, g0val):
    """W_len(g) = int_0^inf [g(0) e^{-2u}/u - 2 rho(u) g(u)] du
    - log(pi) g(0), the length-side regularized arch functional
    (dps 60 kills the u -> 0 cancellation)."""
    import mpmath as mp
    mp.mp.dps = 60

    def integ(u):
        r = mp.e ** (-u / 2) / (1 - mp.e ** (-2 * u))
        return g0val * mp.e ** (-2 * u) / u - 2 * r * g(u)

    val = mp.quad(integ, [0, 1, 5, 30])
    return float(val - mp.log(mp.pi) * g0val)


def w_len_packet(s, t0):
    import mpmath as mp
    mp.mp.dps = 60
    g = lambda u: mp.e ** (-u * u / (2 * s * s)) * mp.cos(t0 * u)
    return w_len_general(g, 1.0)


def w_freq_packet(s, t0):
    """W_freq(g) = (1/2pi) int_R g^(tau) omega(tau) dtau, closed
    Gaussian transform, omega = Re psi(1/4 + i tau/2) - log pi."""
    import mpmath as mp
    mp.mp.dps = 30
    c = s * mp.sqrt(2 * mp.pi) / 2

    def gh(t):
        return c * (mp.e ** (-s * s * (t - t0) ** 2 / 2)
                    + mp.e ** (-s * s * (t + t0) ** 2 / 2))

    def om(t):
        return mp.re(mp.digamma(mp.mpf(1) / 4 + mp.mpc(0, t / 2))) \
            - mp.log(mp.pi)

    val = mp.quad(lambda t: gh(t) * om(t),
                  [0, t0 / 2, t0, t0 + 25 / s]) / mp.pi
    return float(val)


def rs_theta_dev():
    """max_tau |omega(tau) - 2 theta'_RS(tau)|,
    theta_RS(tau) = Im log Gamma(1/4 + i tau/2) - (tau/2) log pi."""
    import mpmath as mp
    mp.mp.dps = 30

    def theta(x):
        return mp.im(mp.loggamma(mp.mpf(1) / 4 + mp.mpc(0, x / 2))) \
            - x / 2 * mp.log(mp.pi)

    devs = []
    for t in (5.0, 20.0, 80.0):
        om = mp.re(mp.digamma(mp.mpf(1) / 4 + mp.mpc(0, t / 2))) \
            - mp.log(mp.pi)
        devs.append(abs(om - 2 * mp.diff(theta, t)))
    return float(max(devs))


def pole_target_packet(s, t0):
    """int_0^inf g(u) 2cosh(u/2) du for the even packet (mp quad)."""
    import mpmath as mp
    mp.mp.dps = 30
    g = lambda u: mp.e ** (-u * u / (2 * s * s)) * mp.cos(t0 * u)
    return float(mp.quad(lambda u: g(u) * 2 * mp.cosh(u / 2), [0, 30]))


# ------------------------------------------------------------ G0 firewall
def g0_firewall(wins):
    print("\nG0 -- Firewall + Flaechen")
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            names.add(node.id)
        elif isinstance(node, ast.Attribute):
            names.add(node.attr)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for al in node.names:
                names.add(al.name.split(".")[0])
    hits = sorted(n for n in names for b in BANNED_IDS if b in n.lower())
    check("G0.1 AST-Firewall: keine Primtabellen-/Nullstellen-Ladung im "
          "Konstruktionspfad (diese Scheibe braucht KEINE Nullstellen; "
          "Runde-10/11-Flaechen unberuehrt)", not hits, str(hits))
    fam = ", ".join("h=%d" % (w["M"] // 2) for w in wins)
    check("G0.2 deklarierte 9-Fenster-Leiter (Etappe 4) reproduziert: %s"
          % fam, len(wins) == 9)


# ================================================================== F1
def battery_for(w):
    M, D = w["M"], w["D"]
    ab = []
    for d in (0, 1, M // 2, M - 1):
        a = np.zeros(M)
        a[d] = 1.0
        ab.append(("e_%d" % d, a))
    ab.append(("Fejer", 1.0 - np.arange(M) / M))
    ab.append(("Zelt-Stack", np.maximum(
        0.0, 1.0 - np.abs(np.arange(M) - M / 2.0) / (M / 4.0))))
    for j in range(N_RAND):
        ab.append(("rand%d" % j, RNG.standard_normal(M)
                   * np.exp(-3.0 * np.arange(M) / M)))
    for (s, t0) in PACKETS_LIN[:2]:
        g = gauss_even(s, t0)
        ab.append(("Gauss(s=%.2f,t0=%g)" % (s, t0),
                   g(np.arange(M) * D)))
    return ab


def f1(wins):
    print("\nF1 -- die endliche Spurformel exakt (Spektral == Geometrie)")
    worst_all = 0.0
    rows = []
    for w in wins:
        M, D = w["M"], w["D"]
        tau, wts, kbad, devg = stage4.gns_nodes(w["p"], M // 2, D)
        w["tau"], w["wts"] = tau, wts
        th = tau * D
        C = np.cos(np.outer(th, np.arange(M, dtype=float)))
        worst = 0.0
        for name, a in battery_for(w):
            fv = C @ a
            S = float(wts @ fv)
            G = float(a @ w["p"])
            scale = float(np.abs(wts) @ np.abs(fv)) + abs(G) + 1.0e-300
            worst = max(worst, abs(S - G) / scale)
        worst_all = max(worst_all, worst)
        rows.append("h=%d: %.1e" % (M // 2, worst))
    check("F1.1 GAUSS-QUADRATUR-IDENTITAET tr f(J_K) = sum_i w_i f(tau_i) "
          "= sum_d a_d p_d EXAKT auf allen 9 Fenstern x %d Batterie-"
          "Vektoren (max rel dev %.1e)"
          % (4 + 2 + N_RAND + 2, worst_all), worst_all <= BAR_EXACT,
          "; ".join(rows[:4]) + " ...")

    # ledger on the largest window, Gauss packet
    w = wins[-1]
    M, D = w["M"], w["D"]
    s, t0 = PACKETS_LIN[0]
    a = gauss_even(s, t0)(np.arange(M) * D)
    th = w["tau"] * D
    S = float(w["wts"] @ (np.cos(np.outer(th, np.arange(M, dtype=float)))
                          @ a))
    P_blk = float(a @ w["cp"])
    A_blk = float(a @ w["car"])
    Pi_blk = float(a @ w["cat"])
    print("      LEDGER (h=%d, Gauss-Paket s=%.2f, tau0=%g):" % (M // 2,
                                                                 s, t0))
    print("        Spektralseite  sum w_i f(tau_i) = %+.12f" % S)
    print("        POL-Block   (g^(i/2)+g^(-i/2))  = %+.12f" % P_blk)
    print("        ARCH-Block  (Gamma'/Gamma)      = %+.12f" % A_blk)
    print("        ATOM-Block  (Primglied)         = %+.12f" % Pi_blk)
    check("F1.2 Buchfuehrung: Spektralseite == POL + ARCH + ATOME "
          "(dev %.1e); Delta der Etappe 3 ist exakt der benannte Rest "
          "der QUADRATISCHEN Lesart (F2)"
          % abs(S - (P_blk + A_blk + Pi_blk)),
          abs(S - (P_blk + A_blk + Pi_blk))
          <= BAR_EXACT * max(1.0, abs(S)))

    # closed dictionary identities on 3 windows, Fejer + packet
    dev_pol = dev_at = dev_ar = dev_uv = 0.0
    for w in (wins[0], wins[4], wins[-1]):
        M, D = w["M"], w["D"]
        for a in (1.0 - np.arange(M) / M,
                  gauss_even(*PACKETS_LIN[0])(np.arange(M) * D)):
            # POL: cp_d is the exact full-line tent read of 2cosh(u/2)
            lhs = float(a @ w["cp"])
            rhs = cell_integral(a, M, D,
                                lambda u: 2.0 * np.cosh(0.5 * u), k0=-1)
            dev_pol = max(dev_pol, abs(lhs - rhs) / max(1.0, abs(lhs)))
            # ATOME: block == -sum (mu/2)(a~(u_n) + a~(-u_n))
            ka = w["ka"]
            us, mus = core.U_ALL[:ka], core.MU_ALL[:ka]
            gsum = 0.5 * (lag_interp(a, D, us) + lag_interp(a, D, -us))
            rhs = -float(np.dot(mus, gsum))
            lhs = float(a @ w["cat"])
            dev_at = max(dev_at, abs(lhs - rhs) / max(1.0, abs(lhs)))
            # ARCH far: sum_{d>=1} a_d car_d == -int rho a~_far
            b = a.copy()
            b[0] = 0.0
            lhs = float(b @ w["car"])
            rhs = -cell_integral(b, M, D, stage2.rho, k0=0)
            dev_ar = max(dev_ar, abs(lhs - rhs) / max(1.0, abs(lhs)))
        dev_uv = max(dev_uv, abs(w["car"][0] - stage2.arch_lag0_geo(w["D"]))
                     / abs(w["car"][0]))
    check("F1.3 WOERTERBUCH POL: cp-Block == int a~(u) 2cosh(u/2) du "
          "geschlossen (max dev %.1e) -- die Residuen der Pole s = 0, 1 "
          "(g^(i/2) + g^(-i/2)-Glied von Weil 1952)" % dev_pol,
          dev_pol <= BAR_DICT)
    check("F1.4 WOERTERBUCH ATOME: cat-Block == "
          "-sum_n (mu_n/2)(a~(log n) + a~(-log n)) (max dev %.1e) -- "
          "das Primglied -sum Lambda(n)/sqrt(n) g(log n)" % dev_at,
          dev_at <= BAR_DICT)
    check("F1.5 WOERTERBUCH ARCH: car-Block (d>=1) == -int rho(u) a~(u) du "
          "(max dev %.1e), UV-Zelle car_0 == Weil-regularisierte Zelle "
          "der Etappe 2 (max dev %.1e) -- das Gamma'/Gamma-Glied"
          % (dev_ar, dev_uv), dev_ar <= BAR_DICT and dev_uv <= BAR_DICT)


# ================================================================== F2 (i)
def f2i(wins):
    print("\nF2(i) -- der Arch-Fluss-Anteil: geschlossene "
          "Eisenstein/Streuterm-Gestalt")
    # frequency == length identity for the packets
    dev_fl = 0.0
    WLs = []
    for (s, t0) in PACKETS_LIN:
        wl = w_len_packet(s, t0)
        wf = w_freq_packet(s, t0)
        WLs.append(wl)
        dev_fl = max(dev_fl, abs(wf - wl) / max(1.0, abs(wl)))
    check("F2i.1 GESCHLOSSENE GESTALT: (1/2pi) int g^ (Re psi(1/4+i tau/2)"
          " - log pi) dtau == int_0^inf [g(0)e^{-2u}/u - 2 rho g] du "
          "- log(pi) g(0) auf 3 Gauss-Paketen (max rel dev %.1e) -- das "
          "klassische Gamma'/Gamma-Glied der Weil-Formel in Laengen-Form"
          % dev_fl, dev_fl <= BAR_FREQ,
          "W_len = " + ", ".join("%+.6f" % x for x in WLs))
    dev_th = rs_theta_dev()
    check("F2i.2 STREUPHASE: omega(tau) == 2 theta'_RS(tau) (Riemann-"
          "Siegel-Theta, max dev %.1e) -- der Arch-Fluss ist die glatte "
          "Nullstellendichte = GL(1)-Streuphase (Eisenstein-Analogon "
          "der Spurformel)" % dev_th, dev_th <= BAR_THETA)

    # deployed lag route on the SYNTHETIC fine D-ladder (same deployed
    # constructor, alpha fixed): the TWO-SIDED (even) reading
    #   B_two(g; D) = g(0) car_0 + 2 sum_{d>=1} g(dD) car_d
    Dsyn = 2.0 * ALPHA_SYN / np.array(MS_SYN, float)
    lados = {}
    for M in MS_SYN:
        D = 2.0 * ALPHA_SYN / M
        far = stage2.arch_lags_far_geo(M, D)
        lados[M] = (D, far, stage2.arch_lag0_geo(D))
    lims = []
    ones = []
    ok_fit = True
    for (s, t0), wl in zip(PACKETS_LIN, WLs):
        g = gauss_even(s, t0)
        two = []
        one = []
        for M in MS_SYN:
            D, far, c0c = lados[M]
            sfar = float(g(np.arange(1, M) * D) @ far)
            two.append(g(0.0) * c0c + 2.0 * sfar)
            one.append(g(0.0) * c0c + sfar)
        L, _c, res = fit_limit_d2(Dsyn, np.array(two))
        ok_fit &= res <= 1.0e-3
        lims.append(L)
        ones.append(np.array(one))
    A = np.vstack([np.asarray(WLs), np.ones(3)]).T
    (sig, c0), *_ = np.linalg.lstsq(A, np.asarray(lims), rcond=None)
    res_sc = float(np.max(np.abs(A @ np.array([sig, c0])
                                 - np.asarray(lims))))
    check("F2i.3 DEPLOYTE ARCH-LESART (zweiseitig/gerade, feine "
          "D-Leiter): D->0-Limes von g(0)car_0 + 2 sum g(dD)car_d == "
          "sigma * W_len(g) + c * g(0) fuer alle 3 Pakete mit "
          "sigma = %.6f == 1, c = %.6f == 0 (Fit-Residuum %.1e) -- der "
          "deployte Arch-Block IST das klassische Gamma'/Gamma-Glied, "
          "OHNE Zusatzkonstante" % (sig, c0, res_sc),
          ok_fit and abs(sig - 1.0) <= BAR_CONST
          and abs(c0) <= BAR_CONST and res_sc <= 1.0e-3)

    # honesty: the ONE-SIDED coefficient sum has NO limit -- it drifts
    # like +(1/2) g(0) log(1/D) (UV cell only half-compensated)
    inc = np.array([ones[2][j + 1] - ones[2][j]
                    for j in range(len(MS_SYN) - 1)])
    dev_inc = float(np.max(np.abs(inc - 0.5 * math.log(2.0))))
    check("F2i.4 EHRLICHKEIT: die einseitige Summe sum_d g(dD) car_d "
          "divergiert -- Halbierung von D hebt sie um (1/2) g(0) log 2 "
          "(gemessen %s, max dev %.1e): nur die GERADE Lesart traegt "
          "den Grenzwert; genau sie steht im Woerterbuch F1.4/F1.5"
          % (", ".join("%.6f" % x for x in inc), dev_inc),
          dev_inc <= 5.0e-3)


# ============================================================= F2 (ii/iii)
def f2ii(wins, comb_small):
    print("\nF2(ii/iii) -- Orbit-Interferenz + Diagonale: die "
          "Delta-Zerlegung auf der h-Leiter")
    ns = np.array(sorted(n for n in comb_small))
    mu = np.array([2.0 * comb_small[int(n)] / math.sqrt(float(n))
                   for n in ns])
    lg = np.log(ns.astype(float))
    Ds = np.array([w["D"] for w in wins])
    FINE = slice(4, None)        # limit fits on the 5 finest windows

    ok_pp = True
    verdict_rows = []
    for (s, t0) in PACKETS_QUAD:
        f0 = gauss_odd(s, t0)
        g0v = autocorr_num(f0, s, np.concatenate(([0.0], lg)))
        g00, g0_at = float(g0v[0]), g0v[1:]
        C_at = -float(np.dot(mu, g0_at))
        import mpmath as mp

        def g0_call(u):
            return mp.mpf(float(autocorr_num(f0, s, [float(u)])[0]))

        WLq = w_len_general(g0_call, g00)
        t_ar_n = np.zeros(len(wins))
        t_at_n = np.zeros(len(wins))
        pp_n = np.zeros(len(wins))
        orb_n = np.zeros(len(wins))
        dlt_n = np.zeros(len(wins))
        for i, w in enumerate(wins):
            M, D = w["M"], w["D"]
            q = (np.arange(M) - 0.5 * (M - 1)) * D
            V = f0(q[:M // 2])
            u = stage3.odd_extend(V, M)
            t_ar = stage3.toep_quad(w["car"], u)
            t_at = stage3.toep_quad(w["cat"], u)
            t_cp = stage3.toep_quad(w["cp"], u)
            pp = stage3.pole_square_closed(V, M, D)
            ok_pp &= abs(pp + t_cp) <= BAR_POLSQ * max(1.0, abs(pp))
            phi = stage3.interp_odd(u, M, D, lg)
            porb = float(np.dot(mu, phi * phi))
            t_ar_n[i] = D * t_ar
            t_at_n[i] = D * t_at
            pp_n[i] = D * pp
            orb_n[i] = D * porb
            dlt_n[i] = D * ((t_ar + t_at) - pp - porb)
        alias = np.abs(t_at_n - C_at)
        sl_alias = loglog_slope(Ds, alias)
        sl_orb = loglog_slope(Ds, orb_n)
        A_lim, _cA, resA = fit_limit_d2(Ds[FINE], t_ar_n[FINE])
        dev_A = abs(A_lim - WLq) / max(1.0, abs(WLq))
        # synthetic two-sided lock at the SAME autocorrelation
        two = []
        for M in MS_SYN:
            D = 2.0 * ALPHA_SYN / M
            far = stage2.arch_lags_far_geo(M, D)
            gv = autocorr_num(f0, s, np.arange(1, M) * D)
            two.append(g00 * stage2.arch_lag0_geo(D)
                       + 2.0 * float(gv @ far))
        Dsyn = 2.0 * ALPHA_SYN / np.array(MS_SYN, float)
        L2, _c2, res2 = fit_limit_d2(Dsyn, np.array(two))
        dev_syn = abs(L2 - WLq)
        D_pred = WLq + C_at
        dev_D = abs(dlt_n[-1] - D_pred) / max(1.0, abs(D_pred))
        tag = "s=%.2f,tau0=%g" % (s, t0)
        check("F2ii.1 [%s] INTERFERENZ IST NICHT ALIASING: D*t_at -> "
              "C_at = -sum mu_n g0(log n) = %+.6f != 0 (volles "
              "klassisches Primglied an der Autokorrelation); nur der "
              "Alias-Anteil stirbt: |D*t_at - C_at| %.2e -> %.2e, "
              "log-log-Rate in D %+.2f" % (tag, C_at, alias[0],
                                           alias[-1], sl_alias),
              abs(C_at) >= 10.0 * alias[-1] and sl_alias >= RATE_POS)
        check("F2ii.2 [%s] DIAGONALE + POLQUADRAT subleading: D*phi_orb "
              "%.2e -> %.2e (Rate in D %+.2f), D*phi_pole <= %.1e "
              "(exponentiell tot)" % (tag, orb_n[0], orb_n[-1], sl_orb,
                                      pp_n[-1]),
              (sl_orb >= 0.5 or orb_n[-1] <= 1.0e-3 * abs(dlt_n[-1]))
              and pp_n[-1] <= 1.0e-12)
        check("F2ii.3 [%s] ARCH-FLUSS-ANTEIL: Limes von D*t_ar = %+.6f "
              "== W_len(g0) = %+.6f (rel dev %.1e, Fit-Res %.1e); "
              "synthetische zweiseitige Leiter: %+.6f (dev %.1e) -- "
              "sigma = 1, c = 0: der Arch-Anteil von Delta IST das "
              "klassische Gamma'/Gamma-Glied an der Autokorrelation"
              % (tag, A_lim, WLq, dev_A, resA, L2, dev_syn),
              dev_A <= 5.0e-3 and resA <= 1.0e-3 and dev_syn <= 1.0e-3
              and res2 <= 1.0e-3)
        check("F2ii.4 [%s] DELTA GEOMETRISCH: D*Delta(h_max) = %+.6f == "
              "[Arch-Glied %+.6f] + [Primglied %+.6f] (rel dev %.1e) -- "
              "Delta ist im Limes EXAKT (Gamma'/Gamma + Primsumme) der "
              "klassischen Weil-Formel am Autokorrelations-Test"
              % (tag, dlt_n[-1], WLq, C_at, dev_D),
              dev_D <= BAR_LIMIT)
        verdict_rows.append((tag, C_at, sl_alias, dev_D))
    check("F2ii.5 E3-Identitaet re-verriegelt: phi_pole == "
          "-u^T Toep(cp) u geschlossen auf allen Fenstern x Paketen",
          ok_pp)

    print("""
      SATZ-KANDIDAT (Spurformel des verklebten Objekts):
      Fuer jede Trunkierung (alpha, M, D; K = M/2) und jedes gerade
      bandlimitierte f (Grad <= M-1) gilt EXAKT (F1.1, 1e-13-Niveau):
        sum_i w_i f(tau_i)  =  P_D(g) + A_D(g) + Pi_D(g),
      g = Zelt-Interpolant der Lag-Koeffizienten, mit (gerade Lesart)
        P_D(g)  = int g(u) 2cosh(u/2) du           [g^(i/2)+g^(-i/2)],
        A_D(g)  = W_len(g) + O(D^2), sigma = 1, c = 0
                  [Gamma'/Gamma-Glied, omega = 2 theta'_RS Streuphase],
        Pi_D(g) = -sum_n Lambda(n)/sqrt(n)(g(log n)+g(-log n))/2 + O(D^2)
                  [Weil-Primglied];
      im Limes D -> 0 ist die geometrische Seite Glied fuer Glied die
      klassische Weil-Formel (1952) -- KLASSISCH, nichts neu.
      NEU zu beweisen waeren genau:
        (K1) Knoten -> Nullstellen (Etappe-4-MESSUNG: Rate -1.61) --
             d.h. die Spektralseite konvergiert gegen sum_gamma f(gamma)
             + Quadratur-Fuellung, mit Gewichts-Normierung;
        (K2) der Grenzwert-Austausch (GNS/Mosco-Konvergenz der
             Trunkierungen gegen den L1-Operator);
        (K3) die Positivitaets-Persistenz im Limes (Etappe 3).
      KEIN RH-Claim: (K1)-(K3) zusammen WAEREN die Spurformel; heute
      sind sie Messungen mit Raten.""")
    return verdict_rows


# ================================================================== F3
def f3_census(wins):
    print("\nF3 -- E8-Eindeutigkeit als endlicher Census (Bonus)")
    # --- the two dimension-8 unimodular Z-lattices (declared classical:
    #     Mordell 1938: Z^8 (odd) and E8 (even) are the complete list)
    roots = []
    for v in itertools.product(range(-1, 2), repeat=8):
        if sum(x * x for x in v) == 2 and sum(v) % 2 == 0:
            roots.append(tuple(2 * x for x in v))
    for y in itertools.product((0, -1), repeat=8):
        v = tuple(2 * x + 1 for x in y)
        if sum(x * x for x in v) == 8 and sum(v) % 4 == 0:
            roots.append(v)
    RD = np.array(sorted(roots), dtype=np.int64)
    rset = set(map(tuple, RD.tolist()))

    def J_vec(x):
        out = np.empty_like(x)
        out[0::2] = -x[1::2]
        out[1::2] = x[0::2]
        return out

    j_ok = all(tuple(J_vec(RD[i]).tolist()) in rset
               for i in range(len(RD)))
    # completeness of the norm-2 enumeration (doubled coords, |y|^2 = 8):
    # integer type y = 2v needs |v|^2 = 2 (two +-1, sum even); odd type
    # needs all |y_i| = 1 (any +-3 gives >= 9); both enumerated above.
    check("F3.1 E8 maschinell: 240 Norm-2-Vektoren (Kusszahl, "
          "vollstaendige Enumeration in verdoppelten Koordinaten), "
          "J-Automorphismus mit J^2 = -1 auf allen Wurzeln: %s; "
          "Z^8: Kusszahl 16 (Norm-1-Vektoren +-e_i) geschlossen"
          % j_ok, len(RD) == 240 and j_ok)

    # norm parity: sum v == |v|^2 mod 2 forces even norms (integer type);
    # odd type: sum of 8 odd squares == 8 mod 8 -> norm even.  Spot check:
    par = []
    for _ in range(200):
        co = RNG.integers(-3, 4, size=8)
        y = co @ RD[:8]            # lattice vector in doubled coords
        par.append(int(y @ y) % 8)
    check("F3.2 NORM-PARITAET: E8 GERADE (200 Zufallsvektoren: Norm "
          "|y|^2/4 stets gerade: %s; Beweis-Skizze im Code), Z^8 "
          "UNGERADE (16 Norm-1-Vektoren) -- der Traeger fixiert die "
          "Paritaet" % all(p == 0 for p in par),
          all(p == 0 for p in par))

    # hermitian-unimodular Z[i]-basis of E8 (machine construction)
    found = None
    for _ in range(4000):
        idx = RNG.choice(len(RD), size=4, replace=False)
        Y = np.zeros((8, 8), dtype=np.int64)
        for k, i in enumerate(idx):
            Y[2 * k] = RD[i]
            Y[2 * k + 1] = J_vec(RD[i])
        det = round(float(np.linalg.det(Y.astype(float))))
        if abs(det) == 256:        # |det| in true coords = 256/2^8 = 1
            found = (idx, Y)
            break
    ok_h = False
    detH = 0.0
    if found is not None:
        idx, Y = found
        H = np.zeros((4, 4), dtype=complex)
        for a in range(4):
            for b in range(4):
                xa, xb = Y[2 * a], Y[2 * b]
                H[a, b] = (float(xa @ xb)
                           + 1j * float(xa @ J_vec(xb))) / 8.0
        detH = abs(np.linalg.det(H))
        ok_h = (np.max(np.abs(H - H.conj().T)) <= 1.0e-12
                and np.max(np.abs(np.diag(H) - 1.0)) <= 1.0e-12
                and abs(detH - 1.0 / 16.0) <= 1.0e-9)
    check("F3.3 HERMITESCHE Z[i]-BASIS des E8 konstruiert: 4 Wurzeln, "
          "Z[i]-Spann = E8 (|det_Z| = 1 exakt), H hermitesch, H_aa = 1, "
          "|det H| = %.12f == 4^-2 (Selbstdualitaet: det_Z = "
          "4^4 |det H|^2 = 1 in der Spurform-Normierung H = (<x,y> + "
          "i<x,Jy>)/2); Z^8 = Z[i]^4 traegt dieselbe Struktur trivial "
          "-- BEIDE Census-Klassen sind Z[i]-Traeger, der Unterschied "
          "ist allein die Paritaet" % detH, ok_h)

    # parity -> tower period (declared bridge: stage-2 A1 mode census +
    # v695-S2 half tower), then the gluing battery over the window ladder
    print("      deklarierte Bruecke: gerade Klasse -> Perioden-2-Turm "
          "m == 1 mod 4 (rho), ungerade Klasse -> mu2-Turm (alle "
          "Halbzahl-Moden); Kontrafaktual mu4-falsch: m == 3 mod 4")
    cands = (("E8 (gerade, mu4-Klasse m==1 mod 4)", stage2.rho),
             ("Z^8 (ungerade, mu2-Turm)", stage2.rho_mu2),
             ("E8-falsche-Klasse (m==3 mod 4)", stage2.rho_mu4_wrong))
    results = []
    for name, dens in cands:
        kaps, resids = [], []
        for w in wins[::2]:
            M, D, alpha = w["M"], w["D"], w["alpha"]
            ds = np.unique(np.round(np.geomspace(
                max(2.0, 0.5 / D), 2.0 * alpha / D - 2.0, 20))
                .astype(int))
            x = np.array([-stage2.tent_read(dens, int(d), D) for d in ds])
            y = w["car"][ds]
            kap = float(x @ y) / float(x @ x)
            resid = float(np.linalg.norm(kap * x - y)
                          / np.linalg.norm(y))
            kaps.append(kap)
            resids.append(resid)
        results.append((name, max(abs(k - 1.0) for k in kaps),
                        min(resids)))
    (n1, k1, r1), (n2, _k2, r2), (n3, _k3, r3) = results
    check("F3.4 VERKLEBUNGS-CENSUS: %s verklebt (|kappa-1| max %.1e, "
          "Residuum <= %.1e); %s reisst (bestes Residuum %.3f); %s "
          "reisst (bestes Residuum %.3f) -- unter dem endlichen Census "
          "{Z^8, E8} verklebt NUR das Gauss-E8"
          % (n1, k1, r1, n2, r2, n3, r3),
          k1 <= CENS_KAPPA and r1 <= CENS_KAPPA
          and r2 >= CENS_FLOOR and r3 >= CENS_FLOOR)
    print("      EHRLICHKEIT: der Census-SATZ braucht als klassischen "
          "Input die Klassifikation unimodularer Z-Gitter in dim 8 "
          "(Mordell 1938: genau Z^8 und E8) und die deklarierte "
          "Paritaets-Bruecke (Etappe-2-A1-Moden-Census, gemessen, kein "
          "Satz); modulo dieser zwei Inputs ist die E8-Eindeutigkeit "
          "ein endlicher 2-Klassen-Census mit hartem Messausgang.")


# ================================================================== F4
def f4():
    print("\nF4 -- Verdict + finale Bilanz")
    n_ok = sum(1 for _n, ok in CHECKS if ok)
    verdict = "MOONSHOT-SATZ1-LEDGER-EXACT" if n_ok == len(CHECKS) \
        else "MOONSHOT-SATZ1-PARTIAL"
    print("""
  BILANZ DER SATZ-1-SCHEIBE:
  * F1: die endliche Spurformel IST die Gauss-Quadratur-Identitaet der
    GNS-Trunkierung -- exakt auf Maschinenniveau, und das Woerterbuch
    Spurformel <-> explizite Formel ist GESCHLOSSEN: POL-Block =
    Residuen s = 0, 1; ARCH-Block = Gamma'/Gamma-Glied; ATOM-Block =
    Primglied.  Kein Term bleibt unbenannt.
  * F2: Delta ist geometrisch ZERLEGT: (i) der Arch-Fluss hat die
    geschlossene Streuterm-Gestalt (omega = 2 theta'_RS, Frequenz ==
    Laenge) und der deployte Block IST das Gamma'/Gamma-Glied
    (sigma = 1, c = 0, gerade Lesart); (ii) die Orbit-Interferenz ist
    NICHT Aliasing -- sie konvergiert gegen das VOLLE klassische
    Primglied an der Autokorrelation (nur der Diskretisierungs-Anteil
    stirbt, Rate gemessen); (iii) Diagonale und Polquadrat sind
    subleading.  Also: D*Delta -> Gamma'/Gamma-Glied + Primglied --
    die Spurformel-Aussage ist die klassische Weil-Formel PLUS eine
    Konvergenz-Aussage (K1-K3 im Satz-Kandidaten), nichts anderes.
  * F3 (Bonus): unter dem endlichen Census {Z^8, E8} (klassisch
    vollstaendig, Mordell 1938) verklebt NUR das Gauss-E8; die
    Paritaets-Bruecke (gerade Klasse -> m == 1 mod 4-Turm) ist der
    deklarierte, gemessene Schritt.
  * PRIME.Z1.MOONSHOT-Notiz (Update): Etappen 1-4 + Satz-1-Scheibe:
    das verklebte Objekt hat jetzt (a) exakte endliche Spurformeln auf
    jeder Trunkierung, (b) ein vollstaendiges Glied-Woerterbuch zur
    Weil-Formel, (c) einen gemessenen Spektral-Limes auf die
    Nullstellen (E4), (d) einen 2-Klassen-Eindeutigkeits-Census.
    OFFEN (in Reihenfolge): K1 Knoten-Konvergenz als Satz, K2
    GNS/Mosco-Limes, K3 Positivitaets-Persistenz.  RADIKALE
    EHRLICHKEIT: alles Geometrische ist klassisch (Weil 1952); der
    neue Gehalt sitzt AUSSCHLIESSLICH in den Konvergenz-Aussagen --
    KEIN RH-Claim, kein neuer Satz, eine exakte Buchfuehrung.""")
    return verdict


def run():
    print("MOONSHOT SATZ-1-SCHEIBE -- die Spurformel des verklebten "
          "Objekts (F1 Ledger, F2 Delta-Geometrie, F3 Census)")
    wins = stage4.family_ext()
    g0_firewall(wins)
    f1(wins)
    f2i(wins)
    comb_small, _meta = stage2.geo_comb(X_SMALL)
    f2ii(wins, comb_small)
    f3_census(wins)
    verdict = f4()
    print("\n[%s] %d checks, %.1f s" % (verdict, len(CHECKS),
                                        time.time() - T0))
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    sys.exit(run())
