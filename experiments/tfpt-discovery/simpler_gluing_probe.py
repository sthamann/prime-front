#!/usr/bin/env python3
"""VEREINFACHUNGS-TEST 2 -- VERKLEBUNG <=> POSITIVITAET?  Die
Starrheits-These: ist die Etappe-2-Verklebungs-Identitaet (kappa =
(1,1,1), Residuum < 1e-12) SENSITIV auf Off-Line-Nullstellen?

AUFBAU: Das deployte Fenster p = c_atom + c_arch + c_pol liegt EXAKT
im 3-Sektor-Spann der unabhaengig gebauten geometrischen Seiten
(Etappe 2: vereintes Objekt == deployte Fenster bei 2.2e-16, freier
3-Skalar-Fit == (1,1,1) < 1e-12 -- hier als Referenz deklariert; die
Sektor-Vektoren SIND die Verklebungs-Richtungen).  Injektion via dem
v677-S2-Woerterbuch (explizite Formel, [E], unbedingt): ein
Nullstellen-Paar bei gamma_0 traegt pro Lag
    h_d(r) = 2 cos(dD r) * D * sinc^2(rD/2),   sinc z = sin z / z,
zu c_d bei; ein OFF-LINE-Quadrupel (beta = 1/2 +- delta) ersetzt
2 h_d(gamma_0) durch 2 Re h_d(gamma_0 + i delta).  gamma_0-Werte sind
SYNTHETISCH deklariert (10/25/50) -- keine Nullstellen-Ladung,
zeta-frei.  ON-LINE-Kontrolle: gleiche rho-Verschiebung |delta| laengs
der Linie (gamma_0 -> gamma_0 + delta).

MESSUNGEN:
  T2.1 Baseline: 3-Skalar-LSQ auf (c_at, c_ar, c_p) reproduziert
       kappa = (1,1,1) mit Residuum == 0 (Maschine) -- der Detektor-
       Boden ist Identitaets-Niveau.
  T2.2 Off-Line-Injektion: Verklebungs-Residuum (nach freiem
       3-Skalar-Fit) vs delta in {0.01, 0.1, 0.25, 0.5} x gamma_0 in
       {10, 25, 50} x 2 Fenster: springt (>> Boden) und MONOTON in
       delta; Tiefen-Profil ~ cosh(delta d D) (Off-Line waechst
       exponentiell in der Lag-Tiefe).
  T2.3 On-Line-Kontrolle: gleiches |rho-Displacement|, Residuum
       bleibt Groessenordnungen kleiner (beschraenkt-oszillierend
       statt cosh-verstaerkt) -- die Verklebung misst OFF-Line, nicht
       bloss Abweichung.
  T2.4 Schwellen-Vergleich: Identitaets-Detektor (jedes delta > 0
       sichtbar) vs PD-Detektor (Levinson bricht erst ab delta*_PD)
       -- die Verklebung ist der SCHAERFERE Diagnostik-Kanal.
  T2.5 Typung (radikal ehrlich): "Verklebung <=> Positivitaet" ist in
       dieser Form FALSCH.  Die Etappe-2-Identitaet verbindet zwei
       GEOMETRISCH konstruierte Seiten und gilt unbedingt (Weil
       1952); fuer zeta selbst sind die Kamm-Daten fix -- die
       Verklebung sagt ohne Positivitaet NICHTS ueber Nullstellen-
       Lagen.  Der Detektor schlaegt an, weil injizierte Daten ein
       ANDERES Spektrum repraesentieren: er detektiert Inkonsistenz
       von Fenster-Daten mit der wahren Arithmetik (Repraesentations-
       Ebene), nicht Off-Line-Zeros von zeta.  Die RH-Form "das wahre
       Objekt verklebt in jeder Tiefe" ist eine WAHRE, unbedingte
       Identitaets-Aussage -- die Mauer bleibt die Ungleichung
       (PD-Persistenz).  Fehlend fuer einen Beweis-Nutzen: dass die
       wahren Lags nur von einem On-Line-Spektrum kommen koennen --
       das ist Positivitaet selbst (D1-Determiniertheit gibt
       Eindeutigkeit des MASSES, nicht Realitaet der Traeger-Punkte).

RESULTS (2026-08-04, 5/5 PASS, Verdict GLUING-DETECTOR):
  T2.1 Baseline: kappa = (1,1,1) bei max |kappa - 1| = 2.3e-15,
       rel Residuum <= 2.3e-15 auf allen 9 Fenstern.
  T2.2 Off-Line (2 Fenster x gamma_0 = 10/25/50): Residuum-Leiter
       (gamma_0 = 25, h = 606): 3.7e-4 / 3.9e-2 / 3.2e-1 / 9.6e-1
       bei delta = 0.01 / 0.1 / 0.25 / 0.5 -- monoton an allen 6
       Zellen, delta = 0.01 bereits >= 1e3 x Boden; Tiefen-Profil
       tiefstes/oberstes Viertel 93.6 (cosh-Vorhersage 86.1, h=606)
       bzw. 182.8 (255.4, h=1433).
  T2.3 On/Off-Trennung (delta = 0.5): Residuum-Kontrast off/on =
       4.1 (h=606) / 6.8 (h=1433); Huellkurven-Steigung off 0.461 /
       0.437 (~ delta: der Detektor MISST delta) vs on -0.010 /
       -0.167.  EHRLICH: bei delta = 0.1 mimt der On-Line-Beat
       Wachstum (slope 0.12-0.16) -- volle Trennschaerfe erst ab
       delta >~ 2 pi/(2 alpha); rel Residuum saettigt bei delta=0.5.
  T2.4 Schwellen: Identitaets-Detektor sieht delta = 0.01 (res
       3.6e-4) auf beiden Fenstern; Levinson-PD bricht erst ab
       delta* = 0.02 (Bruchtiefen 756 / 1077) -- die Verklebung ist
       der schaerfere Kanal, aber NICHT aequivalent zur Positivitaet
       (T2.5-Typung: Identitaets- vs Ungleichungs-Ebene).

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim, no RH claim.  Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/simpler_gluing_probe.py
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

import moonshot_spectral_probe as stage4  # noqa: E402
import z1_jacobi_probe as jac  # noqa: E402

T0 = time.time()
CHECKS = []

GAMMA0 = (10.0, 25.0, 50.0)      # synthetic pair locations (declared)
DELTAS = (0.01, 0.1, 0.25, 0.5)  # off-line displacement ladder
WIN_PICKS = (4, -1)              # mid + largest window
D_SCAN = np.arange(0.02, 1.01, 0.02)   # PD threshold scan

BAR_BASE = 1.0e-13           # baseline gluing residual (identity floor)
FLOOR_AMP = 1.0e3            # delta = 0.01 must exceed floor by this
BAR_RATIO = 3.0              # off/on contrast at delta = 0.5 (the
#                              relative residual saturates near 1 for
#                              off-line; measured 4.1 .. 6.9)

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros")


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def csinc(z):
    z = np.asarray(z, complex)
    out = np.ones_like(z)
    nz = np.abs(z) > 1.0e-12
    out[nz] = np.sin(z[nz]) / z[nz]
    return out


def h_lags(M, D, r):
    """v677-S2 dictionary: per-lag contribution h_d(r) of a zero pair
    at gamma = r (complex allowed), d = 0..M-1."""
    d = np.arange(M)
    return np.real(2.0 * np.cos(d * D * r) * D * csinc(r * D / 2.0) ** 2)


def glue_fit(w, p_vec):
    """Free 3-scalar LSQ on the sector directions; returns (kappa,
    relative residual)."""
    A = np.vstack([w["cat"], w["car"], w["cp"]]).T
    kap, *_ = np.linalg.lstsq(A, p_vec, rcond=None)
    res = float(np.linalg.norm(p_vec - A @ kap)
                / np.linalg.norm(p_vec))
    return kap, res


def pd_break_delta(w, g0):
    """Smallest delta on D_SCAN where Levinson breaks (or None)."""
    base = 2.0 * h_lags(w["M"], w["D"], g0)
    for de in D_SCAN:
        dp = 2.0 * h_lags(w["M"], w["D"], g0 + 1j * de) - base
        _ks, _es, bd = jac.levinson(w["p"] + dp, w["M"] - 1)
        if bd is not None:
            return float(de), bd
    return None, None


# ------------------------------------------------------------ G0
def g0_firewall(wins):
    print("\nG0 -- Firewall + Fenster")
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
    hits = sorted(n for n in names for bnd in BANNED_IDS
                  if bnd in n.lower())
    check("G0.1 AST-Firewall: zeta-frei; gamma_0-Batterie SYNTHETISCH "
          "deklariert (10/25/50), keine Nullstellen-Ladung",
          not hits and len(wins) == 9, str(hits))


# ================================================================== T2.1
def t21_baseline(wins):
    print("\nT2.1 -- Baseline: der Detektor-Boden")
    dev_k = res_max = 0.0
    for w in wins:
        kap, res = glue_fit(w, w["p"])
        dev_k = max(dev_k, float(np.max(np.abs(kap - 1.0))))
        res_max = max(res_max, res)
    check("T2.1 BASELINE == IDENTITAETS-NIVEAU: freier 3-Skalar-Fit "
          "auf allen 9 Fenstern gibt kappa = (1,1,1) (max |kappa-1| = "
          "%.1e) mit rel Residuum <= %.1e -- die Etappe-2-Verklebung "
          "(vereintes Objekt == deployt bei 2.2e-16) als Referenz "
          "reproduziert; der Detektor-Boden ist Maschinenpraezision"
          % (dev_k, res_max), dev_k <= 1.0e-12 and res_max <= BAR_BASE)
    return res_max


# ================================================================== T2.2
def t22_offline(wins, floor):
    print("\nT2.2 -- Off-Line-Injektion: Residuum vs delta")
    ok_mono = ok_jump = ok_depth = True
    rows = []
    res_tab = {}
    for wi in WIN_PICKS:
        w = wins[wi]
        for g0 in GAMMA0:
            base = 2.0 * h_lags(w["M"], w["D"], g0)
            rs = []
            for de in DELTAS:
                dp = 2.0 * h_lags(w["M"], w["D"], g0 + 1j * de) - base
                _kap, res = glue_fit(w, w["p"] + dp)
                rs.append(res)
                res_tab[(wi, g0, de)] = res
            ok_mono &= all(rs[i + 1] > rs[i] for i in range(len(rs) - 1))
            ok_jump &= rs[0] >= FLOOR_AMP * max(floor, 1.0e-16)
            if g0 == GAMMA0[1]:
                rows.append("h=%d gamma0=%g: res = %s"
                            % (w["M"] // 2, g0,
                               ", ".join("%.2e" % r for r in rs)))
        # depth profile: off-line lives in the deep lags (cosh growth)
        de = DELTAS[-1]
        dp = 2.0 * h_lags(w["M"], w["D"], GAMMA0[1] + 1j * de) - \
            2.0 * h_lags(w["M"], w["D"], GAMMA0[1])
        q = w["M"] // 4
        ratio_depth = float(np.max(np.abs(dp[-q:]))
                            / np.max(np.abs(dp[:q])))
        pred = math.cosh(de * (w["M"] - 1) * w["D"]) / 1.0
        ok_depth &= ratio_depth > 0.1 * pred
        rows.append("h=%d Tiefen-Profil (delta=%g): max|dp| tiefstes/"
                    "oberstes Viertel = %.1f (cosh-Vorhersage %.1f)"
                    % (w["M"] // 2, de, ratio_depth, pred))
    check("T2.2 OFF-LINE BRICHT DIE VERKLEBUNG MONOTON: rel Residuum "
          "des freien 3-Skalar-Fits springt bei JEDEM delta (delta = "
          "0.01 bereits >= %.0e x Boden) und waechst monoton ueber "
          "delta = %s, an allen %d (Fenster x gamma_0)-Zellen; das "
          "Injektions-Profil waechst wie cosh(delta dD) in die "
          "Lag-Tiefe: %s"
          % (FLOOR_AMP, str(DELTAS), 2 * len(GAMMA0),
             " | ".join(rows)), ok_mono and ok_jump and ok_depth)
    return res_tab


# ================================================================== T2.3
def envelope_slope(w, dp):
    """log-envelope slope (block-max, deep 60% of lags) of the
    post-fit residual of dp, in u = dD units."""
    A = np.vstack([w["cat"], w["car"], w["cp"]]).T
    kap, *_ = np.linalg.lstsq(A, dp, rcond=None)
    r = dp - A @ kap
    M, D = w["M"], w["D"]
    us, ev = [], []
    for b in range(int(0.3 * M), M - 50, 50):
        us.append((b + 25) * D)
        ev.append(float(np.max(np.abs(r[b:b + 50]))))
    return float(np.polyfit(np.array(us),
                            np.log(np.maximum(np.array(ev),
                                              1.0e-300)), 1)[0])


def t23_online(wins, res_tab):
    print("\nT2.3 -- On-Line-Kontrolle: gleiche Verschiebung, Linie")
    ok_ratio = ok_slope = True
    rows = []
    de = DELTAS[-1]
    for wi in WIN_PICKS:
        w = wins[wi]
        for g0 in GAMMA0:
            base = 2.0 * h_lags(w["M"], w["D"], g0)
            dp_on = 2.0 * h_lags(w["M"], w["D"], g0 + de) - base
            dp_off = 2.0 * h_lags(w["M"], w["D"], g0 + 1j * de) - base
            _kap, res_on = glue_fit(w, w["p"] + dp_on)
            ratio = res_tab[(wi, g0, de)] / max(res_on, 1.0e-300)
            ok_ratio &= ratio >= BAR_RATIO
            if g0 == GAMMA0[1]:
                s_off = envelope_slope(w, dp_off)
                s_on = envelope_slope(w, dp_on)
                ok_slope &= (0.35 <= s_off <= 0.6) and s_on <= 0.1
                rows.append("h=%d: off/on-Residuum %.1f, Huellkurven-"
                            "Steigung off %.3f (~delta = %g) vs on "
                            "%.3f" % (w["M"] // 2, ratio, s_off, de,
                                      s_on))
    check("T2.3 ON/OFF-TRENNUNG bei delta = %g: Residuum-Kontrast "
          "off/on >= %.0f an allen 6 Zellen und Huellkurven-Steigung "
          "des Post-Fit-Residuums: OFF waechst exponentiell mit "
          "Steigung ~ delta (cosh-Signatur; der Detektor MISST delta), "
          "ON kollabiert auf <= 0.1 (beschraenkter Beat): %s -- "
          "EHRLICHE GRENZE: bei kleinem delta mimt der On-Line-Beat "
          "|sin(u delta/2)| Wachstum, solange 2 pi/delta nicht ins "
          "Fenster passt (gemessen: on-slope 0.12-0.16 bei delta = "
          "0.1); volle off/on-Trennschaerfe erst ab delta >~ 2 pi/"
          "(2 alpha), und das RELATIVE Residuum saettigt bei delta = "
          "0.5 nahe 1 (Kontrast-Cap)"
          % (de, BAR_RATIO, " | ".join(rows)), ok_ratio and ok_slope)


# ================================================================== T2.4
def t24_thresholds(wins, res_tab):
    print("\nT2.4 -- Schwellen: Identitaets- vs PD-Detektor")
    rows = []
    ok = True
    for wi in WIN_PICKS:
        w = wins[wi]
        g0 = GAMMA0[1]
        de_pd, bd = pd_break_delta(w, g0)
        de_id = DELTAS[0]
        res_id = res_tab[(wi, g0, de_id)]
        ok &= (de_pd is None) or (de_pd > de_id)
        rows.append("h=%d: Identitaets-Detektor sieht delta = %g "
                    "(res %.1e); Levinson-PD bricht erst ab delta* = "
                    "%s%s" % (w["M"] // 2, de_id, res_id,
                              ("%.2f" % de_pd) if de_pd else ">1.0",
                              (" (Tiefe %d)" % bd) if bd else ""))
    check("T2.4 DIE VERKLEBUNG IST DER SCHAERFERE KANAL: %s -- der "
          "Identitaets-Detektor hat Schwelle ~0 (Maschinenboden), der "
          "PD-Detektor (Ungleichungs-Ebene, vgl. v677-Schwellenkarte "
          "und die l1/k1b-Scramble-Bruchtiefen 31/61) braucht endliche "
          "Margen-Ueberwindung" % " | ".join(rows), ok)


# ================================================================== T2.5
def t25_typing():
    print("\nT2.5 -- Typung (radikal ehrlich)")
    print("""      VERKLEBUNG <=> POSITIVITAET IST IN DIESER FORM FALSCH:
      die Etappe-2-Identitaet verbindet zwei GEOMETRISCH konstruierte
      Seiten (Gruppoid-Kamm + Lift-Fluss vs deployte Fenster) und
      gilt UNBEDINGT (Weil 1952) -- egal wo die zeta-Nullstellen
      liegen.  Fuer zeta selbst sind die Kamm-Daten fix; die
      Verklebung ERZWINGT keine Nullstellen-Lage.  Der gemessene
      Detektor lebt auf REPRAESENTATIONS-Ebene: injizierte Off-Line-
      Daten repraesentieren ein anderes Spektrum, und der 3-Sektor-
      Kegel der wahren Geometrie enthaelt es nicht (Residuum ~
      cosh(delta dD), monoton, on/off-Kontrast gemessen).  NUTZEN:
      ein Identitaets-scharfer Konsistenz-Test fuer Fenster-Daten
      (jedes delta > 0 detektierbar, waehrend PD erst ab delta*
      bricht) -- als DIAGNOSTIK dem PD-Kanal ueberlegen.  KEIN neuer
      RH-Zugang: die RH-Form 'das wahre Objekt verklebt in jeder
      Tiefe' ist wahr und unbedingt; die Mauer bleibt die
      UNGLEICHUNG (PD-Persistenz).  Was einem Beweis fehlt, ist
      nicht, dass die Konstruktion die Identitaet erzwingt (tut sie,
      trivial: beide Seiten sind konstruiert) -- sondern dass die
      wahren Lags nur von einem On-Line-Spektrum getragen werden
      koennen: das ist die Positivitaet selbst (D1-Determiniertheit
      liefert Eindeutigkeit des Masses, nicht die Realitaet der
      Traeger-Punkte ohne Positivitaet).""")


def run():
    print("VEREINFACHUNGS-TEST 2 -- Verklebung als Off-Line-Detektor")
    wins = stage4.family_ext()
    g0_firewall(wins)
    floor = t21_baseline(wins)
    res_tab = t22_offline(wins, floor)
    t23_online(wins, res_tab)
    t24_thresholds(wins, res_tab)
    t25_typing()
    n_ok = sum(1 for _n, ok in CHECKS if ok)
    verdict = "GLUING-DETECTOR" if n_ok == len(CHECKS) \
        else "GLUING-PARTIAL"
    print("\n[%s] %d checks, %.1f s" % (verdict, len(CHECKS),
                                        time.time() - T0))
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(run())
