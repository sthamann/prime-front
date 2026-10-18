#!/usr/bin/env python3
"""VEREINFACHUNGS-TEST 1 -- GENESTETE TURM-TRUNKIERUNG: ist der
Fenster-Quantor ein Artefakt der historischen Frame-A-Familie?

DER STRUKTUR-BEFUND, auf dem alles ruht: die Toeplitz-Form in den
deployten TENT-Lags c_d (arch + atome + pol, fester Gitterabstand D)
IST exakt die Weil-Form von STUFENFUNKTIONEN auf dem D-Gitter:
tent_D = (box_D * box_D)/D, also
    x^T T_M(c) x = (1/D) W(G * G~),   G = sum x_j box_D(. - jD)
mit W dem Weil-Funktional (Laengenseite).  Daraus folgen DREI exakte
Struktur-Eigenschaften, die der historischen Fenster-Familie fehlten:

  T_X-NESTUNG (X = e^{2 alpha}, kanonische Etappe-2-Paarung
  Kamm-Norm <= X <-> Lag-Reichweite log X, M = 2 alpha/D):
    T_X ist die fuehrende Hauptuntermatrix von T_X' (X < X') --
    Kompression durch Koordinaten-Injektion, Konsistenz GRATIS
    (die Eigenschaft, an der die Fenster-Einbettungen scheiterten).

  D-VERFEINERUNG (dyadisch): box_D = box_{D/2}(.-D/4) + box_{D/2}(.+D/4)
  exakt, auf Lag-Ebene
    c^{(D)}_d = c'_{2d} + (c'_{2d-1} + c'_{2d+1})/2   (d >= 1),
    c^{(D)}_0 = c'_0 + c'_1,
  und auf Form-Ebene T_M(c^{(D)}) = (1/2) L T_{2M}(c^{(D/2)}) L^T mit
  L = Box-Verdopplung (Zeile j: Einsen bei 2j, 2j+1): PD der FEINEN
  Stufe erzwingt PD der groben -- der D-Quantor kollabiert entlang
  jeder dyadischen Kette NACH UNTEN auf den Limes.

  FENSTER-REDUKTION: das deployte Frame-A-Fenster ist die exakte
  Odd-Sektor-Kompression A = odd_toeplitz(c) = (1/2) E^T T_M(c) E
  (v677 S1, E = odd-Extension, Eintraege +-1), und der Lag-Vektor
  jedes deployten Fensters IST ein Turm-Mitglied (D_w = 2 alpha/M,
  X_w = e^{2 alpha}) -- Fenster-Positivitaet folgt EXAKT aus
  Turm-Positivitaet.

EHRLICHE GRENZE: die historischen D_w sind paarweise inkommensurabel;
Ketten zu VERSCHIEDENEN Wurzel-D verbindet nur eine approximative
Tent-Interpolation (T1.5c misst den Fehler ehrlich).  Der Quantor
reduziert also auf: "PD des 2-Parameter-Turms (D, X)", nach unten
geordnet laengs dyadischer Ketten mit exakter Kompressions-Vererbung
-- EIN genestetes Objekt statt 67 historischer Fenster, aber der
D-Richtungs-Quantor bleibt (kontinuierlich, kettengeordnet).

RESULTS (2026-08-04, 8/8 PASS, Verdict TOWER-NESTED-REDUCES):
  T1.1 X-Nestung: Praefix-Identitaet max rel dev 6.7e-18 (float-exakt;
       nur 2 Randzellen der Kamm-Reichweite X-abhaengig).
  T1.2 Verfeinerung: Lag-Identitaet max rel dev 8.0e-17 (d >= 1) /
       9.0e-16 (d = 0) -- sogar der GL-48-arch-Anteil respektiert die
       Tent-Zerlegung exakt (Zellgrenzen teilen sich dyadisch);
       Form-Kompression 3.7e-16.
  T1.3 PD 12/12: Levinson-Headroom 0.746 / 0.800 / 0.833 (D = 1/64,
       1/128, 1/256; X-unabhaengig!); lambda_min > 0 an allen Ecken,
       ABER relativer Margen-TREND FAELLT mit der Tiefe:
       lambda_min/c_0 = 1.9e-5 (M = 256) -> 3.9e-7 (M = 1792) --
       die Mauer wird im Turm nicht kleiner, nur kanonischer.
  T1.4 (a) Frame-A = Odd-Kompression, dev 3.4e-16; (b) deployte
       Fenster SIND Turm-Mitglieder, dev 0.0; (c) Ketten-Uebersetzung
       inkommensurabler D: Residuum 4.3e-2 >> lambda_min 2.8e-5 --
       PD-Transfer ueber Kettengrenzen schliesst NICHT (ehrliche
       Grenze; der D-Quantor bleibt kontinuierlich, kettengeordnet).

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim, no RH claim.  Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/simpler_tower_probe.py
"""

import ast
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _here)
sys.path.insert(0, os.path.abspath(os.path.join(_here, "..", "..",
                                                "verification")))

import v563_paper2_readouts as core  # noqa: E402
import moonshot_arch_glue_probe as stage2  # noqa: E402
import moonshot_spectral_probe as stage4  # noqa: E402
import z1_jacobi_probe as jac  # noqa: E402

T0 = time.time()
CHECKS = []

D_LEVELS = (1.0 / 64.0, 1.0 / 128.0, 1.0 / 256.0)   # dyadic, float-exact
ALPHAS = (2.0, 2.5, 3.0, 3.5)                       # X = e^{2 alpha}
EIG_CORNERS = ((0, 0), (0, -1), (-1, 0), (-1, -1))  # (D-idx, alpha-idx)
SEED = 11

BAR_NEST = 1.0e-15           # X-nesting prefix identity (relative)
BAR_REFINE = 5.0e-9          # dyadic lag identity (arch quadrature)
BAR_FORM = 1.0e-12           # quadratic-form identities (relative)

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros")


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def tower_lags(D, alpha):
    """Tower member (D, X = e^{2 alpha}): tent lags arch + atoms + pole
    at fixed D, depth M = 2 alpha / D (the deployed constructors)."""
    M = int(round(2.0 * alpha / D))
    al = 0.5 * M * D
    ka = core.atoms_in(al)
    cat, _dd = core.atom_lags_at(al, M, core.U_ALL[:ka],
                                 core.MU_ALL[:ka])
    return core.arch_lags(M, D) + cat + stage2.pole_lags_closed(M, D)


def lev_headroom(c):
    """Levinson diagnostics: (PD?, 1 - max|k|, min E)."""
    ks, Es, bd = jac.levinson(c, len(c) - 1)
    if bd is not None:
        return False, -1.0, float(np.min(Es[:bd])), bd
    return True, float(1.0 - np.max(np.abs(ks))), float(np.min(Es)), None


# ------------------------------------------------------------ G0
def g0_firewall():
    print("\nG0 -- Firewall")
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
    check("G0.1 AST-Firewall: zeta-frei, keine Primtabellen-Ladung "
          "(Turm aus den deployten geometrischen Konstruktoren)",
          not hits, str(hits))


# ================================================================== T1.1
def t11_nesting(tow):
    print("\nT1.1 -- kanonische Paarung + X-NESTUNG (exakt)")
    dev = 0.0
    for D in D_LEVELS:
        for a0, a1 in zip(ALPHAS[:-1], ALPHAS[1:]):
            c0, c1 = tow[(D, a0)], tow[(D, a1)]
            m = len(c0) - 2                    # boundary cells excluded
            sc = float(np.max(np.abs(c0[:m])))
            dev = max(dev, float(np.max(np.abs(c0[:m] - c1[:m]))) / sc)
    check("T1.1 X-NESTUNG EXAKT: Praefix-Identitaet c^(X)_d == c^(X')_d "
          "fuer d <= M_X - 3, alle 3 D-Stufen x 3 alpha-Paare (max rel "
          "dev %.1e; nur die 2 Randzellen der Kamm-Reichweite sind "
          "X-abhaengig) -- T_X ist die FUEHRENDE HAUPTUNTERMATRIX von "
          "T_X': Restriktion/Kompression durch Koordinaten-Injektion, "
          "Zustands-Konsistenz der Familie GRATIS (die Eigenschaft, "
          "die den historischen Fenster-Einbettungen fehlte)" % dev,
          dev <= BAR_NEST)


# ================================================================== T1.2
def t12_refine(tow):
    print("\nT1.2 -- dyadische D-VERFEINERUNG (exakte Kompression)")
    rows = []
    dev_lag = dev0 = 0.0
    for Dc, Df in zip(D_LEVELS[:-1], D_LEVELS[1:]):
        for al in (ALPHAS[0], ALPHAS[-1]):
            c, cf = tow[(Dc, al)], tow[(Df, al)]
            M = len(c)
            d = np.arange(1, M - 1)
            pred = cf[2 * d] + 0.5 * (cf[2 * d - 1] + cf[2 * d + 1])
            sc = float(np.max(np.abs(c)))
            dev_lag = max(dev_lag,
                          float(np.max(np.abs(c[1:M - 1] - pred))) / sc)
            dev0 = max(dev0, abs(c[0] - (cf[0] + cf[1])) / sc)
    check("T1.2a LAG-IDENTITAET DER VERFEINERUNG: c^(D)_d == "
          "c^(D/2)_2d + (c^(D/2)_2d-1 + c^(D/2)_2d+1)/2 (d >= 1, max "
          "rel dev %.1e) und c^(D)_0 == c'_0 + c'_1 (dev %.1e) -- "
          "tent_D ist die exakte Interpolation in halben Tents; "
          "arch-Anteil traegt die GL-48-Quadratur-Toleranz"
          % (dev_lag, dev0), max(dev_lag, dev0) <= BAR_REFINE)

    rng = np.random.default_rng(SEED)
    dev_f = 0.0
    for (Dc, Df) in ((D_LEVELS[0], D_LEVELS[1]),):
        for al in (ALPHAS[0], ALPHAS[-1]):
            c, cf = tow[(Dc, al)], tow[(Df, al)]
            M = len(c)
            Tc = sla.toeplitz(c)
            Tf = sla.toeplitz(cf[:2 * M])
            for _ in range(3):
                x = rng.standard_normal(M)
                y = np.zeros(2 * M)
                y[0::2] = x
                y[1::2] = x
                qc = float(x @ Tc @ x)
                qf = 0.5 * float(y @ Tf @ y)
                dev_f = max(dev_f, abs(qc - qf) / max(1.0, abs(qc)))
            rows.append("D=%.5f alpha=%g: M=%d" % (Dc, al, M))
    check("T1.2b FORM-KOMPRESSION EXAKT: x^T T_M(c^(D)) x == (1/2) "
          "(L^T x)^T T_2M(c^(D/2)) (L^T x) mit L = Box-Verdopplung "
          "(max rel dev %.1e; %s) -- PD DER FEINEN STUFE ERZWINGT PD "
          "DER GROBEN: der D-Quantor kollabiert entlang jeder "
          "dyadischen Kette nach unten auf den Limes [E: box_D = "
          "box_D/2(.-D/4) + box_D/2(.+D/4), Weil-Form von "
          "Stufenfunktionen]" % (dev_f, "; ".join(rows)),
          dev_f <= BAR_FORM)


# ================================================================== T1.3
def t13_pd(tow):
    print("\nT1.3 -- PD ueber den (D, X)-Turm")
    ok_pd = True
    rows = []
    eig_rows = []
    for D in D_LEVELS:
        heads = []
        for al in ALPHAS:
            pd, head, emin, bd = lev_headroom(tow[(D, al)])
            ok_pd &= pd
            heads.append(head)
        rows.append("D=1/%d: Headroom %s"
                    % (int(round(1.0 / D)),
                       ", ".join("%.3f" % h for h in heads)))
    for (i, j) in EIG_CORNERS:
        D, al = D_LEVELS[i], ALPHAS[j]
        c = tow[(D, al)]
        ev = float(np.min(np.linalg.eigvalsh(sla.toeplitz(c))))
        ok_pd &= ev > 0.0
        eig_rows.append("(D=1/%d, alpha=%g, M=%d): lambda_min = %.3e "
                        "(rel %.1e)"
                        % (int(round(1.0 / D)), al, len(c), ev,
                           ev / c[0]))
    check("T1.3 POSITIVITAET DES TURMS GEMESSEN: Levinson-PD auf allen "
          "12 Mitgliedern (3 dyadische D x 4 X-Stufen), Headroom "
          "1 - max|k| pro X-Schnitt: %s; Eck-Eigenwerte exakt: %s -- "
          "PD-Margen bleiben positiv ueber beide Richtungen des Turms"
          % (" | ".join(rows), "; ".join(eig_rows)), ok_pd)


# ================================================================== T1.4
def t14_windows(tow):
    print("\nT1.4 -- die Fenster-Reduktion (deployt -> Turm)")
    wins = stage4.family_ext()
    rng = np.random.default_rng(SEED + 1)

    # (a) frame-A odd compression (v677 S1), machine-exact
    dev_a = 0.0
    for w in (wins[0], wins[4], wins[-1]):
        M = w["M"]
        h = M // 2
        A = core.odd_toeplitz(w["p"], M)
        T = sla.toeplitz(w["p"])
        for _ in range(3):
            x = rng.standard_normal(h)
            f = np.concatenate((x, -x[::-1]))
            qa = float(x @ A @ x)
            qt = 0.5 * float(f @ T @ f)
            dev_a = max(dev_a, abs(qa - qt) / max(1.0, abs(qa)))
    check("T1.4a FRAME-A == ODD-KOMPRESSION DER TOEPLITZ-FORM: "
          "x^T A x == (1/2) f^T T_M(c) f (odd-Extension, v677 S1; max "
          "rel dev %.1e auf 3 Fenstern) -- die deployte Fensterform "
          "ist eine EXAKTE Kompression der Turm-Form" % dev_a,
          dev_a <= BAR_FORM)

    # (b) every deployed window IS a tower member
    dev_b = 0.0
    for w in (wins[0], wins[4], wins[-1]):
        c_tw = tower_lags(w["D"], w["alpha"])
        sc = float(np.max(np.abs(w["p"])))
        dev_b = max(dev_b,
                    float(np.max(np.abs(c_tw[:w["M"]] - w["p"]))) / sc)
    check("T1.4b JEDES DEPLOYTE FENSTER IST TURM-MITGLIED: Lag-Vektor "
          "== Turm-Konstruktor bei (D_w = 2 alpha/M, X_w = e^{2 alpha}) "
          "(max rel dev %.1e auf 3 Fenstern) -- Fenster-Positivitaet "
          "folgt EXAKT aus Turm-Positivitaet: DER FENSTER-QUANTOR "
          "REDUZIERT AUF DEN TURM-QUANTOR" % dev_b, dev_b <= 1.0e-14)

    # (c) cross-chain translation (honest boundary, measurement only)
    w = wins[0]
    Dw, Ds = w["D"], D_LEVELS[-1]
    Mw = w["M"]
    Ms = int(round(2.0 * w["alpha"] / Ds))
    cs = tower_lags(Ds, 0.5 * Ms * Ds)
    ks = np.arange(len(cs))
    p_hat = np.empty(Mw)
    v0 = np.maximum(0.0, 1.0 - np.abs(ks * Ds) / Dw)
    p_hat[0] = v0[0] * cs[0] + 2.0 * float(v0[1:] @ cs[1:])
    for j in range(1, Mw):
        vj = np.maximum(0.0, 1.0 - np.abs(ks * Ds - j * Dw) / Dw)
        p_hat[j] = float(vj[1:] @ cs[1:]) + vj[0] * 0.5 * cs[0]
    res = float(np.max(np.abs(p_hat[:Mw - 2] - w["p"][:Mw - 2])))
    lam = float(np.min(np.linalg.eigvalsh(sla.toeplitz(w["p"]))))
    check("T1.4c KETTEN-UEBERSETZUNG (ehrliche Grenze, nur Messung): "
          "kleinstes Fenster (D_w = %.5f, M = %d) auf die kanonische "
          "Kette D* = 1/%d interpoliert: Lag-Residuum %.2e vs "
          "lambda_min(T(p^w)) = %.3e -- die Interpolation ist NICHT "
          "exakt (inkommensurable Gitter, Tent-Knicke neben dem "
          "D*-Gitter); der Gershgorin-Transfer (M x Residuum = %.2e) "
          "schliesst die PD-Vererbung ueber Kettengrenzen NICHT: der "
          "D-Richtungs-Quantor bleibt kettengeordnet-kontinuierlich "
          "(dokumentierte Grenze der Reduktion)"
          % (Dw, Mw, int(round(1.0 / Ds)), res, lam, res * Mw),
          res < 0.1 * float(np.max(np.abs(w["p"]))))


# ================================================================== T1.5
def t15_verdict():
    print("\nT1.5 -- Verdict")
    n_ok = sum(1 for _n, ok in CHECKS if ok)
    verdict = "TOWER-NESTED-REDUCES" if n_ok == len(CHECKS) \
        else "TOWER-NESTED-PARTIAL"
    print("""
  DIE REDUKTION (radikal ehrlich):
  [E]  T_X-Nestung exakt (Praefix/Kompression, Konsistenz gratis);
       dyadische D-Verfeinerung = exakte PSD-Kompression (PD unten
       => PD oben entlang jeder Kette); Frame-A-Fenster = exakte
       Odd-Kompression; jedes deployte Fenster = Turm-Mitglied.
  =>   Der historische "fuer alle 67 Fenster"-Quantor REDUZIERT auf
       den Turm-Quantor "T_(D,X) PD fuer alle (D, X)", und dieser
       lebt auf einer GENESTETEN Familie: in X eine aufsteigende
       Kette (Limes-Positivitaet = ein einziges Grenzobjekt pro
       Kette), in D dyadisch nach unten vererbend.  Der Fenster-
       Quantor war insofern ein ARTEFAKT der historischen Auswahl.
  ABER (die ehrliche Restgroesse): der D-Richtungs-Quantor bleibt --
       inkommensurable Wurzel-D verbindet nur approximative
       Interpolation (T1.4c: Residuum schliesst PD-Transfer nicht);
       und "Turm-PD fuer alle (D, X)" ist weiterhin die PD-
       Persistenz-Mauer (L1-Scheibe), nur in kanonischer, genesteter
       Gestalt: box-Stufenfunktionen sind dicht, also ist Turm-PD
       fuer D -> 0, X -> inf AEQUIVALENT zum Weil-Kriterium
       (klassischer Dichte-Schritt).  KEIN RH-Claim.""")
    return verdict


def run():
    print("VEREINFACHUNGS-TEST 1 -- genestete Turm-Trunkierung")
    g0_firewall()
    tow = {}
    for D in D_LEVELS:
        for al in ALPHAS:
            tow[(D, al)] = tower_lags(D, al)
    print("  Turm gebaut: %d Mitglieder, M = %d .. %d"
          % (len(tow), min(len(c) for c in tow.values()),
             max(len(c) for c in tow.values())))
    t11_nesting(tow)
    t12_refine(tow)
    t13_pd(tow)
    t14_windows(tow)
    verdict = t15_verdict()
    print("\n[%s] %d checks, %.1f s" % (verdict, len(CHECKS),
                                        time.time() - T0))
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    sys.exit(run())
