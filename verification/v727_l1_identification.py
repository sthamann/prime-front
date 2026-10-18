#!/usr/bin/env python3
"""v727 -- PRIME.L1IDENT.01: L1-SCHEIBE -- Identifikation des
Limes ueber Momentenproblem-
Determiniertheit, und die maximale Praezisierung der Mauer.

K2K3 hat gemessen: der vage Limes existiert (Tightness, Kompakta
Cauchy).  Diese Scheibe legt die IDENTIFIKATIONS-Kette und typt, wo
exakt die RH-Substanz sitzt.

D1 [Carleman]: Auf welchem Raum lebt das Momentenproblem?
  D1.1 Pro Trunkierung: kompaktes Band [0, pi/D] -> HAUSDORFF-
       determiniert.  TRIVIAL, ehrlich als solches verbucht.
  D1.2 SCHAERFUNG DER NORMIERUNG (Mess-Befund dieser Scheibe): das
       ROHE tau-Mass der Fenster traegt den Limes nicht -- seine
       lokale Dichte ist ~ D omega/pi (Masse auf Kompakta schrumpft
       wie D, konsistent mit K3.1b), naive Momente wachsen wie
       tau_max^k log (gemessene Steigungen 2.254 / 4.245 fuer
       k = 2 / 4, eine Potenz UNTER dem Dichte-Gesetz).  Das
       Weil-Objekt ist die pro-Bandbreite normierte LAG-Lesart
       (exakt die L1-Montage-Normierung "Fenster-Symbol pro
       Bandbreite"); dort lebt der Hamburger-Rahmen.
  D1.3 Der RICHTIGE Rahmen: Gauss-gedaempftes Momentenproblem auf
       der Weil-Achse (SIG = 5, fester positiv-analytischer Daempfer
       -> mu_w bestimmt nu).  Gemessen: Lag-Lesart-Momente Cauchy
       ueber die Leiter + Extrapolation; Identifikation gegen die
       geschlossene geometrische Seite
         m_2k = (1/pi) int_0^inf tau^{2k} e^{-tau^2/2SIG^2} omega dtau
                + 2 (-1)^k 4^{-k} e^{1/(8 SIG^2)}   [Pol bei +-i/2]
                - sum_n mu_n g_k(log n)              [Atom-Kamm]
       mit max rel dev 1.4e-3 ueber m_0..m_16 (z.B. m_16: extrap
       6.998089e17 == Modell 6.995306e17, dev 4.0e-4).  Wachstums-
       Typ Gauss/Freud: m_2k^{1/2k}/(SIG sqrt(2k/e)) in [0.638,
       1.117] => Carleman-Glieder >= 1/(1.12 SIG sqrt(2k/e)), Summe
       >= c sqrt(K) -> unendlich: DETERMINIERT (klassisch; roher
       Inkrement-Exponent -0.710, praeasymptotisch vs. -1/2).
       Nichts hiervon ist RH-haltig -- (b) ist Standard.

D2 [Die Identifikations-Kette und das Loch]:
  (a) vager Limes existiert            [K2K3: gemessen straff]
  (b) Momentenproblem determiniert     [D1.3: klassisch + gemessen]
  (c) Limes-Momente == geometrische Seite [F1-Ledger; hier: Knoten-
      Lesart == Lag-Lesart maschinenexakt pro Fenster, D2.1; plus
      Kontinuums-Raten K3.1d/K2.1d]
  (d) geometrische Seite == Nullstellen-Seite [explizite Formel,
      Weil 1952 -- KLASSISCH, UNBEDINGT, egal wo die Nullstellen
      liegen; Woerterbuch-Stuetze: omega == 2 theta'_RS re-verifiziert]
  DAS SCHEIN-PARADOX: T_h(g*g~) >= 0 (Zustaende) und T_h -> W
  (klassisch) wuerde naiv W(g*g~) >= 0 fuer alle g liefern = Weil-
  Kriterium = RH.  DIE AUFLOESUNG: "T_h ist PD" ist pro h eine
  MESSUNG, kein Satz -- die Fenster-Lags sind nicht die Momente eines
  a priori positiven Objekts (das rohe Symbol dippt negativ, E3.2a-2;
  Scramble zerstoert PD, D2.3).  DIE MAUER, maximal praezise:
     PD-PERSISTENZ: unendlich viele Fenster der Leiter sind PD.
  Das ist HINREICHEND fuer RH (PD auf einer Teilfolge + (c)-Raten +
  (d) => W(g*g~) >= 0 fuer alle kompakt getragenen g => Weil).
  Pro Fenster ist PD eine ENDLICHE Rechnung (Levinson); gemessen
  9/9.  Umkehrung (RH => jedes endliche Fenster PD) ist NICHT
  gezeigt -- ehrliche Asymmetrie.  Aequivalente Lesart der Substanz
  (Riesz-Haviland + D1-Determiniertheit): "die geometrische Seite
  definiert ein positives Mass auf R" -- exakt der Verdacht der
  Aufgabenstellung, hier an die messbare PD-Leiter gebunden.

D3 [Zusammenschluss]: die eine verbleibende Aussage in drei
  aequivalenten Sprachen (Momente / Zustand / Symbol), auf dem
  groessten Fenster alle drei gemessen (Hankel-PSD, Levinson-
  Headroom, Fejer-Symbol >= 0) und am Scramble kontrastiert;
  finales Programm-Diagramm + PRIME.Z1.MOONSHOT-Notiz.  K1b
  (Super-Aufloesung, parallele Sonde) stand bei Abschluss dieser
  Scheibe noch aus -- konditional eingebunden.

RESULTS (11/11 PASS, L1-DETERMINED-WALL-TYPED):
  D1: Hausdorff pro Trunkierung trivial; rohes tau-Mass vage -> 0
    (Steigungen 2.254/4.245 == k+log); gedaempfte Weil-Momente
    identifiziert (max 1.4e-3 ueber m_0..m_16); Carleman-Schranke
    aus gemessenem Gauss/Freud-Band [0.638, 1.117]: determiniert.
  D2: (c) Spektral == Lag maschinenexakt (4.7e-14, Gauss-Exaktheit);
    (d) omega == 2 theta'_RS auf 0.0e0 (Weil 1952 klassisch);
    g*g~-Batterie: T_h >= 0 auf 9 x 3 (0 negative), Limes ==
    geschlossener Weil-Wert (devs 5.6e-7 / 1.3e-4 / 1.9e-3);
    Scramble h = 606: Levinson-Breakdown Tiefe 61, Fejer-Minimum
    -2.953e2 -- PD ist arithmetische Substanz.  DIE MAUER:
    PD-PERSISTENZ (unendlich viele PD-Fenster) => Weil-Kriterium
    => RH; pro Fenster endlich entscheidbar, gemessen 9/9
    (min Headroom 0.718); Umkehrung nicht gezeigt.
  D3: drei Sprachen auf h = 1433: Hankel min EW 1.373e-11 >= 0,
    Levinson-Headroom 0.830, Fejer-Minimum 6.475e-3 -- ein Fakt,
    drei Lesarten; K1b stand bei Abschluss noch aus (betrifft die
    Rate der Spektral-Identifikation, nicht die Positivitaet).

PROVENANCE: discovery probe l1_identification_probe.py (2026-08-03,
11/11 PASS, verdict L1-DETERMINED-WALL-TYPED: determinacy is classical
-- damped Weil moments identified against the closed geometric side to
max 1.4e-3 over m_0..m_16, Carleman bound from the measured Gauss/Freud
band [0.638, 1.117]; the identification chain (a)-(d) contains RH
nowhere; THE WALL, maximally precise: PD persistence of the window
ladder -- per window a FINITE Levinson computation, measured 9/9;
equivalent reading via Riesz-Haviland: 'the geometric side defines a
positive measure on R').  Promoted verbatim (sibling imports now point
at the promoted v696/v716-v719 modules); numbers unchanged.
"""

import ast
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..",
                                                "verification")))

import v563_paper2_readouts as core  # noqa: E402
import v716_moonshot_arch_glue as stage2  # noqa: E402
import v717_moonshot_state as stage3  # noqa: E402
import v718_moonshot_spectral as stage4  # noqa: E402
import v719_moonshot_traceformula as stage5  # noqa: E402
import v696_z1_jacobi as jac  # noqa: E402

T0 = time.time()
CHECKS = []

SIG = 5.0                    # Gaussian damping scale on the tau axis
KMAX = 8                     # even moments m_0 .. m_16
SEED = 4                     # scramble control (the E4 recipe)
GL_N, GL_CAP = 400, 60.0     # omega-weighted integrals on [0, cap]
S_GG = 0.5                   # packet width for the g*g~ battery
T0_GG = (0.0, 18.0, 40.0)

BAR_GAUGE = 1.0e-10          # node reading == lag reading
BAR_NAIVE = 0.35             # |slope - (k+1)| of naive moment blowup
BAR_MOM = 5.0e-3             # damped moment identification
BAR_GG = 5.0e-3              # g*g~ limit identification

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros")


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


# ------------------------------------------------------------ helpers
def two_sided(w, gv):
    return float(gv[0] * w["p"][0] + 2.0 * (gv[1:] @ w["p"][1:]))


def omega_grid():
    """GL nodes/weights on [0, GL_CAP] + omega values (mp digamma)."""
    import mpmath as mp
    mp.mp.dps = 20
    xg, wg = np.polynomial.legendre.leggauss(GL_N)
    tq = 0.5 * GL_CAP * (xg + 1.0)
    wq = 0.5 * GL_CAP * wg
    om = np.array([float(mp.re(mp.digamma(mp.mpf(1) / 4
                                          + mp.mpc(0, tt / 2))))
                   - math.log(math.pi) for tt in tq])
    return tq, wq, om


def damped_model(tq, wq, om, k2, atom_j):
    """Closed geometric side of the damped even moment m_{2k}:
    arch omega-integral + pole at +-i/2 + atom comb (all zeta-free)."""
    arch = float(wq @ (tq ** k2 * np.exp(-tq * tq / (2 * SIG * SIG))
                       * om)) / math.pi
    pole = 2.0 * (-1.0) ** (k2 // 2) * 4.0 ** (-(k2 // 2)) \
        * math.exp(1.0 / (8.0 * SIG * SIG))
    return arch + pole - atom_j


def fj_damped(tq, j):
    return tq ** j * np.exp(-tq * tq / (2 * SIG * SIG))


def g_len_of_fj(tq, wq, j, cosC):
    """Length-side transform g_f(u) = (1/pi) int_0^inf f_j cos(tau u)
    dtau, using the precomputed cosine matrix cosC = cos(outer(u, tq))."""
    return (cosC @ (wq * fj_damped(tq, j))) / math.pi


# ------------------------------------------------------------ G0
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
    check("G0.1 AST-Firewall: keine Primtabellen-/Nullstellen-Ladung "
          "(diese Scheibe ist komplett zeta-frei)", not hits, str(hits))
    dev = 0.0
    for w in wins:
        tau, wts, kbad, _d = stage4.gns_nodes(w["p"], w["M"] // 2,
                                              w["D"])
        w["tau"], w["wts"] = tau, wts
        dev = max(dev, abs(float(np.sum(wts)) - float(w["p"][0])))
    check("G0.2 9-Fenster-Leiter + E4-Quadratur reproduziert (Gauge "
          "sum w == p_0, max dev %.1e)" % dev,
          len(wins) == 9 and dev <= 1.0e-10)


# ================================================================== D1
def d1_carleman(wins, tq, wq, om):
    print("\nD1 -- Carleman: auf welchem Raum lebt das Momentenproblem?")
    # D1.1 per truncation: compact -> Hausdorff (trivial, bookkeeping)
    inband = all(float(np.max(w["tau"])) <= math.pi / w["D"] + 1.0e-12
                 for w in wins)
    check("D1.1 PRO TRUNKIERUNG TRIVIAL: Traeger in [0, pi/D] "
          "(kompakt) -> Hausdorff-determiniert; KEINE Substanz hier, "
          "ehrlich verbucht", inband)

    # D1.2 the RAW tau-measure: local density ~ D * omega/pi (mass on
    # compacts shrinks like D, K3.1b); its naive moments grow like
    # tau_max^k * log (NOT k+1: the D-shrinkage eats one power)
    tmax = np.array([math.pi / w["D"] for w in wins])
    rows = []
    ok_naive = True
    for k in (2, 4):
        mk = np.array([float(w["wts"] @ w["tau"] ** k) for w in wins])
        sl = float(np.polyfit(np.log(tmax), np.log(mk), 1)[0])
        ok_naive &= abs(sl - k) <= BAR_NAIVE
        rows.append("k=%d: m_k %.3e -> %.3e, Steigung %.3f (Soll ~%d"
                    "+log-Korrektur)" % (k, mk[0], mk[-1], sl, k))
    check("D1.2 DAS ROHE tau-MASS TRAEGT DEN LIMES NICHT: lokale "
          "Dichte ~ D omega/pi (vage -> 0), naive Momente wachsen wie "
          "tau_max^k log (gemessen; eine Potenz unter dem Dichte-"
          "Gesetz, weil die Masse D-schrumpft): %s.  Das WEIL-Objekt "
          "ist die pro-Bandbreite normierte LAG-Lesart (die L1-"
          "Montage-Normierung) -- alle folgenden Momente werden dort "
          "gelesen; der Hamburger-Rahmen lebt auf der GEDAEMPFTEN "
          "Weil-Achse" % "; ".join(rows), ok_naive)

    # D1.3 damped moments in the LAG (Weil-normalized) reading:
    # Cauchy + extrapolation + closed identification
    comb, _meta = stage2.geo_comb(stage5.X_SMALL)
    us = np.array(sorted(comb))
    mu = np.array([2.0 * comb[int(n)] / math.sqrt(float(n))
                   for n in us])
    lgu = np.log(us.astype(float))
    cosA = np.cos(np.outer(lgu, tq))
    Ds = np.array([w["D"] for w in wins])
    for w in wins:
        w["cosC"] = np.cos(np.outer(np.arange(w["M"]) * w["D"], tq))
    m_ex = {}
    rows = []
    ok_id = True
    dev_max = 0.0
    for k2 in range(0, 2 * KMAX + 1, 2):
        m_h = np.array([two_sided(w, g_len_of_fj(tq, wq, k2,
                                                 w["cosC"]))
                        for w in wins])
        L, _c, _res = stage5.fit_limit_d2(Ds[5:], m_h[5:])
        m_ex[k2] = L
        atom_j = float(mu @ ((cosA @ (wq * fj_damped(tq, k2)))
                             / math.pi))
        model = damped_model(tq, wq, om, k2, atom_j)
        dev = abs(L / model - 1.0)
        dev_max = max(dev_max, dev)
        ok_id &= dev <= BAR_MOM
        if k2 in (0, 4, 10, 16):
            rows.append("m_%d: extrap %.6e == Modell %.6e (dev %.1e)"
                        % (k2, L, model, dev))
    check("D1.3a GEDAEMPFTE WEIL-MOMENTE (SIG = %g) SIND "
          "IDENTIFIZIERT: Lag-Lesart, Leiter-Extrapolation == "
          "geschlossene geometrische Seite (Arch-omega-Integral + Pol "
          "2(-1)^k 4^-k e^{1/8SIG^2} + Atom-Kamm), max rel dev %.1e "
          "ueber m_0..m_16: %s"
          % (SIG, dev_max, "; ".join(rows)), ok_id)

    # growth type + Carleman divergence as a measured BOUND (cleaner
    # than an asymptote fit at small k: the raw increment exponent is
    # pre-asymptotic, reported for honesty)
    ks = np.arange(1, KMAX + 1)
    dS = np.array([m_ex[2 * k] ** (-1.0 / (2 * k)) for k in ks])
    sl = float(np.polyfit(np.log(ks), np.log(dS), 1)[0])
    S_K = np.cumsum(dS)
    gr = np.array([m_ex[2 * k] ** (1.0 / (2 * k))
                   / (SIG * math.sqrt(2 * k / math.e)) for k in ks])
    g_lo, g_hi = float(np.min(gr)), float(np.max(gr))
    check("D1.3b WACHSTUMS-TYP GAUSS/FREUD: m_2k^{1/2k} / "
          "(SIG sqrt(2k/e)) = %.3f .. %.3f (O(1)-Band, kein ueber-"
          "Gauss-Wachstum) => Carleman-Glieder m_2k^{-1/(2k)} >= "
          "1/(%.2f SIG sqrt(2k/e)): Summe >= c sqrt(K) -> unendlich, "
          "DETERMINIERT (Partialsummen S_K = %s; roher Exponent "
          "%+.3f, praeasymptotisch vs. -1/2) -- (b) ist Standard-"
          "Analysis, nichts RH-haltiges"
          % (g_lo, g_hi, g_hi, ", ".join("%.4f" % x for x in S_K[::2]),
             sl), 0.3 <= g_lo and g_hi <= 1.5)
    return m_ex


# ================================================================== D2
def d2_chain(wins, tq, wq, om):
    print("\nD2 -- die Identifikations-Kette und das Loch")
    # D2.1 (c)-link gauge: spectral reading == lag reading (Gauss
    # exactness sum_i w_i cos(dD tau_i) = p_d for all d <= M-1)
    dev = 0.0
    for w in (wins[0], wins[4], wins[-1]):
        D, M = w["D"], w["M"]
        for j in (0, 8):
            a = g_len_of_fj(tq, wq, j, w["cosC"])
            lag = float(a[0] * w["p"][0] + 2.0 * (a[1:] @ w["p"][1:]))
            f2 = (np.cos(np.outer(w["tau"], np.arange(M) * D))
                  @ (np.concatenate(([1.0], 2.0 * np.ones(M - 1)))
                     * a))
            node = float(w["wts"] @ f2)
            dev = max(dev, abs(node - lag) / max(1.0, abs(lag)))
    check("D2.1 (c)-GLIED AUF TRUNKIERUNGEN MASCHINENEXAKT: Spektral-"
          "Lesart sum_i w_i f2(tau_i) == Lag-Lesart sum_d a_d p_d "
          "(Gauss-Exaktheit aller M Lags) fuer j = 0, 8 auf 3 Fenstern "
          "(max rel dev %.1e) -- die endliche Spurformel in Momenten-"
          "Sprache (F1-Ledger)" % dev, dev <= BAR_GAUGE)

    # (d)-link dictionary support (zeta-free): omega == 2 theta'_RS
    dev_th = stage5.rs_theta_dev()
    check("D2.2 (d)-GLIED-STUETZE (zeta-frei): omega(tau) == "
          "2 theta'_RS(tau) (max dev %.1e) -- der Arch-Fluss ist die "
          "glatte Nullstellendichte; die explizite Formel selbst ist "
          "Weil 1952: KLASSISCH und UNBEDINGT (gilt egal wo die "
          "Nullstellen liegen)" % dev_th, dev_th <= 1.0e-8)

    # D2.3 the g*g~ battery: positivity given PD + limit identification
    import mpmath as mp
    Ds = np.array([w["D"] for w in wins])
    rows = []
    ok_pos = ok_id = True
    n_neg = 0
    for t0 in T0_GG:
        A = math.sqrt(math.pi) * S_GG / 2.0
        sp = math.sqrt(2.0) * S_GG
        cross = math.exp(-S_GG * S_GG * t0 * t0)

        def f_len(u):
            u = np.asarray(u, float)
            return A * np.exp(-u * u / (4 * S_GG * S_GG)) \
                * (np.cos(t0 * u) + cross)

        vals = np.array([two_sided(w, f_len(np.arange(w["M"]) * w["D"]))
                         for w in wins])
        n_neg += int(np.sum(vals < 0.0))
        ok_pos &= bool(np.all(vals >= 0.0))
        # closed limit: pole + arch per packet component + atoms
        mp.mp.dps = 30
        lim = 0.0
        for (tt, amp) in ((t0, A), (0.0, A * cross)):
            if amp < 1.0e-30:
                continue
            pol = sum(float(mp.re(mp.sqrt(2 * mp.pi) * sp
                                  * mp.e ** (sp * sp
                                             * mp.mpc(a_, tt) ** 2 / 2)))
                      for a_ in (0.5, -0.5))
            lim += amp * (pol + stage5.w_freq_packet(sp, tt))
        comb, _meta = stage2.geo_comb(stage5.X_SMALL)
        us = np.array(sorted(comb))
        mu = np.array([2.0 * comb[int(n)] / math.sqrt(float(n))
                       for n in us])
        lim += -float(mu @ f_len(np.log(us.astype(float))))
        L, _c, _res = stage5.fit_limit_d2(Ds[5:], vals[5:])
        dev = abs(L - lim) / max(1.0, abs(lim))
        ok_id &= dev <= BAR_GG
        rows.append("t0=%g: T_h %.5f -> %.5f, Limes-Fit %.5f == "
                    "geschlossen %.5f (dev %.1e)"
                    % (t0, vals[0], vals[-1], L, lim, dev))
    check("D2.3 g*g~-BATTERIE: T_h(g*g~) >= 0 auf ALLEN 9 Fenstern x 3 "
          "Paketen (%d negative) -- folgt aus PD [Levinson, gemessen] "
          "+ f^ = |g^|^2 >= 0; und T_h -> geschlossener Weil-Wert mit "
          "D^2-Raten: %s" % (n_neg, " | ".join(rows)),
          ok_pos and ok_id)

    # D2.4 scramble: PD is data-sensitive, not formal
    w2 = wins[len(wins) // 2]
    M, D, alpha, ka = w2["M"], w2["D"], w2["alpha"], w2["ka"]
    rng = np.random.default_rng(SEED)
    pos_scr = np.sort(rng.uniform(0.5, 2.0 * alpha, ka))
    cat_scr = stage2.atom_tent_geo(alpha, M, pos_scr,
                                   np.asarray(core.MU_ALL[:ka], float))
    p_scr = w2["car"] + cat_scr + w2["cp"]
    _ks, _es, bd = jac.levinson(p_scr, M - 1)
    mn_f, _th = stage3.symbol_scan(p_scr, fejer=True)
    check("D2.4 SCRAMBLE-KONTROLLE (h = %d, Positionen verwuerfelt, "
          "Massen erhalten): Levinson-BREAKDOWN bei Tiefe %s, Fejer-"
          "Symbol-Minimum %.3e -- PD ist ARITHMETISCHE SUBSTANZ der "
          "wahren Atomdaten, kein formales Truncation-Artefakt: genau "
          "deshalb ist PD-Persistenz die Mauer und kein Freebie"
          % (M // 2, str(bd), mn_f), bd is not None)

    print("""      DIE KETTE UND DAS LOCH (maximal praezise):
      (a) vager Limes existiert          [K2K3: gemessen, straff]
      (b) Momentenproblem determiniert   [D1.3: klassisch, gemessen]
      (c) Limes == geometrische Seite    [D2.1 exakt + K2/K3-Raten]
      (d) geometrisch == Nullstellen     [Weil 1952, unbedingt]
      In (a)-(d) versteckt sich KEIN RH -- der Verdacht der Aufgabe
      bestaetigt sich.  Das Schein-Paradox 'T_h >= 0 und T_h -> W,
      also W >= 0, also RH' bricht an EINEM Glied: 'T_h ist PD' ist
      pro h eine MESSUNG (Levinson), kein Satz [D2.4: Scramble
      zerstoert PD; E3.2a-2: rohes Symbol dippt negativ].  DIE MAUER:
         PD-PERSISTENZ -- unendlich viele Fenster der Leiter sind PD.
      HINREICHEND fuer RH: PD auf einer Teilfolge + (c) + (d)
      => W(g*g~) >= 0 fuer alle kompakt getragenen g => Weil-
      Kriterium.  Pro Fenster ENDLICH entscheidbar (gemessen 9/9,
      min Headroom 0.718).  Umkehrung (RH => endliche Fenster PD)
      NICHT gezeigt -- ehrliche Asymmetrie.  Aequivalent (Riesz-
      Haviland + (b)): 'die geometrische Seite definiert ein
      positives Mass auf R' -- die sauberste uns bekannte Form.""")


# ================================================================== D3
def d3_final(wins):
    print("\nD3 -- Zusammenschluss: drei Sprachen, ein Diagramm")
    w = wins[-1]
    # (i) moments: Stieltjes-Hankel of damped moments, largest window
    mj = np.array([float(w["wts"] @ (w["tau"] ** j
                                     * np.exp(-w["tau"] ** 2
                                              / (2 * SIG * SIG))))
                   for j in range(2 * KMAX + 1)])
    H = np.array([[mj[i + j] for j in range(KMAX + 1)]
                  for i in range(KMAX + 1)])
    dg = 1.0 / np.sqrt(np.diag(H))
    ev_H = float(np.min(np.linalg.eigvalsh(H * np.outer(dg, dg))))
    # (ii) state: Levinson headroom; (iii) symbol: Fejer minimum
    ks, ok_pd, _dep = stage3.levinson(w["p"])
    head = float(1.0 - np.max(np.abs(ks)))
    mn_f, _th = stage3.symbol_scan(w["p"], fejer=True)
    check("D3.1 DREI SPRACHEN, EIN FAKT (groesstes Fenster h = %d): "
          "(Momente) Hankel der gedaempften m_j PSD, min EW %.3e >= 0; "
          "(Zustand) Levinson-PD, Headroom %.3e; (Symbol) Fejer-"
          "Minimum %.3e >= 0 -- dieselbe Positivitaet in Hamburger-, "
          "GNS- und Toeplitz-Lesart (auf Trunkierungen automatisch "
          "aequivalent; die Substanz ist der h-Allquantor)"
          % (w["M"] // 2, ev_H, head, mn_f),
          ev_H >= -1.0e-10 and ok_pd and mn_f >= 0.0)

    print("""      DAS FINALE DIAGRAMM DES PROGRAMMS:
      [E]/exakt:    Keystone-Zerlegung B = odd(p) + Pol (v701);
                    endliche Spurformel tr f(J_K) == int f dmu_K (F1);
                    Woerterbuch Arch == Gamma'/Gamma, omega == 2
                    theta'_RS; Atom-Schicht aus dem Z[i]-Gruppoid
                    (Etappe 1, Abweichung 0); Verklebung EINE
                    Normierung (Etappe 2, kappa = 1).
      GEMESSEN:     Tightness + vager Limes (K2K3); Cauchy-Raten
                    D^2 / X^{1/2-s} mit unbedingter Majorante (K2);
                    gedaempfte Momente identifiziert, Carleman-
                    Determiniertheit (D1); Spektrum trifft
                    Nullstellen mit Rate -1.61 (E4); PD 9/9 Fenster.
      DIE EINE VERBLEIBENDE AUSSAGE (drei aequivalente Sprachen):
        (Momente)  Die geometrische Momentenfolge (Arch + Pol +
                   Atome, gedaempft) ist positiv definit fuer JEDES
                   Fenster der Leiter -- Hamburger-Positivitaet der
                   Weil-Daten.
        (Zustand)  Die GNS-Familie T_h ist ein Zustand fuer alle h
                   (PD-Persistenz); dann ist der vage Limes ein
                   positives Mass == Nullstellen-Mass, alle
                   Nullstellen reell.
        (Symbol)   Das Fenster-Symbol omega + Kamm + Pol bleibt
                   (Fejer-gelesen) >= 0 auf der ganzen Leiter.
      Jede Form ist pro h ENDLICH entscheidbar; der Allquantor ueber
      h ist RH-aequivalent in Richtung '=>' (hinreichend); alles
      andere im Diagramm ist klassisch oder gemessen-mit-Raten.
      K1b (Super-Aufloesungs-Typung) lief parallel und stand bei
      Abschluss dieser Scheibe noch aus; ihr Ausgang aendert die
      Mauer-Typung nicht (sie betrifft die RATE der Spektral-
      Identifikation, nicht die Positivitaet).
      PRIME.Z1.MOONSHOT (final): Hilbert-Polya-Kandidat strukturell
      komplett auf Messniveau; Satz-Bedarf kollabiert auf (L1) =
      PD-Persistenz der Fenster-Leiter (diese Scheibe: die sauberste
      Form der Mauer) und (L2) = K1-Spektralsatz.  KEIN RH-Claim:
      9/9 PD ist eine Messung, kein Allquantor.""")


def run():
    print("L1-SCHEIBE -- Identifikation ueber Determiniertheit, "
          "Mauer-Typung")
    wins = stage4.family_ext()
    g0_firewall(wins)
    tq, wq, om = omega_grid()
    d1_carleman(wins, tq, wq, om)
    d2_chain(wins, tq, wq, om)
    d3_final(wins)
    n_ok = sum(1 for _n, ok in CHECKS if ok)
    verdict = "L1-DETERMINED-WALL-TYPED" if n_ok == len(CHECKS) \
        else "L1-IDENTIFICATION-PARTIAL"
    print("\n[%s] %d checks, %.1f s" % (verdict, len(CHECKS),
                                        time.time() - T0))
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(run())
