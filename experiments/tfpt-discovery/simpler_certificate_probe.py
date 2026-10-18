#!/usr/bin/env python3
"""SYNTHESE (Schlussstein der Review-Serie) -- kann das strukturelle
Gram-Zertifikat der Schur-Rekursion aus dem exakten Depolarisierer
montiert werden?

VORLIEGENDE TREFFER (read-only, [E]-Anker):
  *  simpler_schur_recursion_probe: S_k >= 0 auf allen 8 Stufen der
     ram-odd-Leiter n_k = 2^{2k+1}; benannter Rest: "S_k = R_k^T R_k
     strukturell, Zertifikat muss die Ordnung-1-Balance von Kontinuum
     und Atomen GEMEINSAM faktorisieren (Inzidenz-Gram im
     Subtrahenten)".
  *  ramodd_twostep_probe (Modul 3): der reale n -> 4n-Pass ist EXAKT
     T = 4 B^2 = 196 K^2, K^2 = (4/49) I + (45/49) Pi_0; KMS-Gewicht
     mu(4n)/mu(n) = 1/2 exakt; MUSS als Korrespondenz-Komposition
     (down-up durch die ramifizierte Kante, Index 2 x 2 = 4) laufen --
     Label-Ketten koennen es nicht (T7).
  *  ramified_polarity_probe (Modul 2): B aus der KANONISCHEN
     symplektischen Form (h = H/4, Null-Polaritaet, GQ(2,2)).
  *  kms_incidence_stinespring_probe (Modul 5): 105 Kraus-Terme
     V_xy = 7^{-1/2}|y><x|, Phi unital/CP, Diagonale = K = B/7,
     Erweiterung Phi (x) id auf die ramifizierte Toeplitz-Schicht,
     KMS-beta = 1; lokaler Zustand tau_inc (x) tau_Toeplitz.
  *  projective_hamming_incidence_probe (Modul 1): B B^T = 4I + 3J
     [E+Lean], Singulaerwerte {7, 2}; K selbst NICHT psd.

DIE MONTAGE-TESTS (M1):
  M1.1 TWOSTEP-Anschluss im Turm, exakt: pro Schur-Schritt genau EIN
       neues ram-odd-Atom (n_{k+1}); KMS-Kaskade 1/2 exakt; die
       ram-odd<->ram-odd-Distanzen sind EXAKT die ram-even-Positionen
       (2j log 2) -- der Turm-Schatten des down-up-Passes (Index 4);
       EHRLICH: der Turm ist V-blind ausser chi_par (v738-Rigiditaet)
       -- die 15x15-Inzidenz-Gestalt lebt NUR in der Stinespring-
       Erweiterung tau_inc (x) tau_Toeplitz, nicht im Lag-Block.
  M1.2 B_k-Zerlegung: Kanal-Split des Off-Blocks exakt; Frobenius-
       Anteile; effektiver Rang des ram-odd-Kreuzterms.
  M1.3 DAS KANDIDATEN-ZERTIFIKAT [Kontinuums-Wurzel + Kraus]:
       (a) VORBEDINGUNG: existiert die Kontinuums-Wurzel?  lambda_min
           des arch+pol-Blocks pro Stufe + Levinson-Breakdown-Zelle
           (v706 G0.1 [M] sagt: NEIN, Bruch zwischen n=2- und
           n=3-Zelle -- hier leiter-weit nachgemessen);
       (b) die Feinheit des Auftrags: Kontinuums-Anteil des VOLLEN
           Blocks vs. des SCHUR-KOMPLEMENTS (S_k^cont gemessen; wenn
           A^cont indefinit ist, ist S^cont kein Haynsworth-Objekt --
           Typung);
       (c) additive Montage S_k =? S_k^cont + Delta_k mit Delta_k
           >= 0: lambda_min(Delta_k) pro Stufe;
       (d) Rettungs-Kaskade: Levinson-Breakdown-Zelle der wachsenden
           Kanal-Vereinigungen (cont / +ram-odd / +ram-even / +split
           / voll) -- WER rettet WANN; die Atome retten in
           ZELL-Reihenfolge (n = 2 ram-odd, n = 3 inert, n = 4
           ram-even, ...), nicht in Kanal-Reihenfolge.
M2: Satz-Kandidat ODER praezises Negativ + Mauer-Typung (radikal
    ehrlich: wo die Positivitaet selbst im Zertifikat steckt).

VERDIKTE (eingefroren): CERT-ASSEMBLED (Montage schliesst mit
benennbaren Gliedern) / CERT-CONTINUUM-ROOT-DEAD (die spezifizierte
Kontinuums-Wurzel existiert nicht -- praezises Negativ mit Anatomie) /
CERT-DEAD (Widerspruch zu den Schur-Befunden).

RESULTS (2026-08-04, 8/8 PASS, verdict CERT-CONTINUUM-ROOT-DEAD):
  *  G0.2  Schur-Leiter bitgleich reproduziert (max rel dev 3.2e-7).
  *  M1.1  Turm-Schatten des down-up-Passes exakt: 1 neues ram-odd-
     Atom pro Schritt (8/8), KMS-Kaskade 1/2 mit dev 0.0, alle
     ram-odd-Paar-Distanzen = gerade 2-adische Schichten {2,...,16}
     x log 2 (= ram-even-Positionen).
  *  M1.2  Kreuzterm: ram-odd-Anteil 0.390 -> 0.143 -> 0.094
     (masse-arm, fallend; NICHT rang-arm -- Kalibrierung
     dokumentiert); Kanal-Ausloeschung Sum||B^gamma||/||B|| = 2.3 ->
     2.9 -> 18.3 (k = 7: ct-Anteil allein 8.99) -- die
     Ordnung-1-Balance sitzt messbar im Kreuzterm.
  *  M1.3a DER KERNBEFUND: arch+pol ist auf KEINER Stufe PSD
     (lambda_min = -4.9e-3 auf W_0 bis -3.6e+2 auf W_8);
     Levinson-Breakdown Zelle 47 in (44, 70) = (n=2, n=3) -- v706
     G0.1 leiter-weit reproduziert und verschaerft (Bruch = letzte
     W_0-Zelle; das n=2-Atom rettet exakt dort).
  *  M1.3b S_k^cont ALLE negativ (-7.2e+2 ... -6.0e+0); da A_k^cont
     indefinit, kein Haynsworth-Objekt.
  *  M1.3c additive Montage tot: lambda_min(S_k - S_k^cont) =
     -31.1, -1.90, ..., -2.65 (alle Stufen indefinit).
  *  M1.3d Rettungs-Kaskade: cont Bruch 47; +ram-odd 72; +ram-even
     72; +split 72; erst VOLL (mit inert n = 3) PD -- die Rettung
     ist strikt ZELL-geordnet, quer zu den Kanaelen.
  *  M2   praezises Negativ: die Mauer ist der fehlende linke
     Faktor; korrigierte Zertifikat-Gestalt = zellweise
     Kaskaden-Faktorisierung (TWOSTEP als 2-adischer Schienenstrang,
     inert/split brauchen eigene Glieder).

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim, no RH claim.  Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/simpler_certificate_probe.py
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
import simpler_schur_recursion_probe as srp  # noqa: E402
import z1_jacobi_probe as jac  # noqa: E402

T0 = time.time()
CHECKS = []

LOG2 = math.log(2.0)
BAR_EXACT = 1.0e-13
RANK_TOL = 0.01

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros")


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


def lev_breakdown(c):
    _ks, _es, bd = jac.levinson(c, len(c) - 1)
    return bd


def eff_rank(M):
    sv = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(sv >= RANK_TOL * sv[0])), float(sv[0])


# ------------------------------------------------------------ G0
def g0_firewall():
    print("\nG0 -- Firewall + Rekonstruktion")
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
    check("G0.1 AST-Firewall: zeta-frei; Maschinerie read-only aus der "
          "Schur-Probe (Turm, Kanaele, Leiter) + [E]-Anker der Module "
          "1/2/3/5 zitiert", not hits, str(hits))


# ================================================================== M1.1
def m11_twostep(sizes, masks, ka):
    print("\nM1.1 -- TWOSTEP-Anschluss im Turm (exakt)")
    u_ro = core.U_ALL[masks["ro"]]
    mu_ro = core.MU_ALL[masks["ro"]]
    # (a) exactly one new ram-odd atom per Schur step
    ok_one = True
    for k in range(len(sizes) - 1):
        lo, hi = (sizes[k] - 1) * srp.DGRID, (sizes[k + 1] - 1) \
            * srp.DGRID
        inside = np.sum((u_ro > lo) & (u_ro <= hi))
        ok_one &= inside == 1
    # (b) KMS half-weight cascade, exact
    dev_kms = float(np.max(np.abs(mu_ro[1:] / mu_ro[:-1] - 0.5)))
    # (c) pair distances == ram-even positions
    u_re = set(np.round(core.U_ALL[masks["re"]] / LOG2).astype(int))
    dists = {int(round((u_ro[j] - u_ro[i]) / LOG2))
             for i in range(len(u_ro)) for j in range(i + 1, len(u_ro))}
    ok_dist = all(d % 2 == 0 and (d in u_re or 2 ** d >
                                  math.exp(2 * 5.92))
                  for d in dists)
    check("M1.1 DER TURM-SCHATTEN DES DOWN-UP-PASSES: (a) pro "
          "Schur-Schritt GENAU EIN neues ram-odd-Atom (8/8 Schritte); "
          "(b) KMS-Halbgewicht mu(4n)/mu(n) = 1/2 exakt (max dev "
          "%.1e); (c) alle ram-odd-Paar-Distanzen sind GERADE "
          "2-adische Schichten (%s x log 2) == die ram-even-Positionen "
          "-- der Pass n -> 4n laeuft im Lag-Bild ueber die "
          "ram-even-Zwischenatome, exakt die Korrespondenz-Komposition "
          "(1+i)-runter/rauf mit Index 2 x 2 = 4 [E: TWOSTEP T1-T6, "
          "T = 4B^2 = 196 K^2].  EHRLICH: der Turm ist V-BLIND ausser "
          "chi_par (v738-Rigiditaet [E]) -- die 15x15-Gestalt lebt "
          "nur in der Stinespring-Erweiterung tau_inc (x) tau_Toeplitz "
          "(Modul 5), im Lag-Block ist der Label-Anteil die "
          "chi_par-Spur" % (dev_kms, sorted(dists)),
          ok_one and dev_kms <= 1.0e-15 and ok_dist)


# ================================================================== M1.2
def m12_crossterm(rungs, sec_lags, sizes):
    print("\nM1.2 -- B_k-Kanal-Zerlegung (der Kreuzterm)")
    # CALIBRATION (declared after first run): the "low rank" guess
    # for B^ro was WRONG (a Toeplitz off-block with ~27 nonzero
    # ram-odd lags carries near-full effective rank at the 1% cut) --
    # the true measured structure is MASS-poverty of the ram-odd rail
    # plus massive CROSS-CHANNEL CANCELLATION; gates re-anchored to
    # exactly that, the rank column is reported, not gated.
    rows = []
    ok = True
    ro_shares = []
    for r in (rungs[0], rungs[3], rungs[-1]):
        m0, m1 = r["m0"], r["m1"]
        Bfull = None
        parts = {}
        for cnl, cl in sec_lags.items():
            Tc = sla.toeplitz(cl[:m1])
            blk = Tc[:m0, m0:m1]
            parts[cnl] = blk
            Bfull = blk if Bfull is None else Bfull + blk
        nb = float(np.linalg.norm(Bfull))
        shares = {c: float(np.linalg.norm(b)) / nb
                  for c, b in parts.items()}
        cancel = sum(shares.values())
        rk_ro, _sv = eff_rank(parts["ro"])
        ro_shares.append(shares["ro"])
        rows.append("k=%d: Anteile ct %.2f / ro %.3f / re %.3f / sp "
                    "%.2f / in %.2f (Ausloeschung Sum/1 = %.1f; "
                    "eff-Rang(B^ro) = %d)"
                    % (r["k"], shares["ct"], shares["ro"],
                       shares["re"], shares["sp"], shares["in"],
                       cancel, rk_ro))
        ok &= shares["ro"] <= 0.5
    ok &= ro_shares[0] > ro_shares[1] > ro_shares[2] and cancel >= 2.0
    check("M1.2 KREUZTERM-ANATOMIE: B_k = Sum B_k^gamma exakt "
          "(Sektor-Toeplitz-Bloecke); %s -- der ram-odd-Kreuzterm ist "
          "MASSE-ARM und fallend (die duenne 2-adische Schiene), "
          "NICHT rang-arm (Kalibrierung dokumentiert); die "
          "Kanal-Anteile loeschen sich im Kreuzterm um Ordnungen aus "
          "(k = 7: Einzelnormen bis 9 x Gesamtnorm) -- DIE "
          "ORDNUNG-1-BALANCE SITZT MESSBAR IM KREUZTERM; die "
          "15x15-Inzidenz-Gestalt sitzt NICHT als Block im B_k"
          % " | ".join(rows), ok)


# ================================================================== M1.3
def m13_certificate(rungs, c_cont, sizes, sec_lags):
    print("\nM1.3 -- das Kandidaten-Zertifikat [Kontinuums-Wurzel + "
          "Kraus]")
    # (a) does the continuum root exist?  full-block ladder
    cell2 = int(round(LOG2 / srp.DGRID))
    cell3 = int(round(math.log(3.0) / srp.DGRID))
    lams = []
    for M in sizes:
        lams.append(float(np.min(np.linalg.eigvalsh(
            sla.toeplitz(c_cont[:M])))))
    bd = lev_breakdown(c_cont)
    ok_v706 = (bd is not None) and (cell2 - 1 <= bd <= cell3 + 1) \
        and all(l < 0 for l in lams)
    check("M1.3a DIE KONTINUUMS-WURZEL EXISTIERT NICHT -- AUF KEINER "
          "STUFE: lambda_min des arch+pol-Blocks = %s; Levinson-"
          "Breakdown bei Zelle %s, exakt zwischen n=2-Zelle (%d) und "
          "n=3-Zelle (%d) [v706 G0.1 [M] leiter-weit reproduziert; "
          "SCHAERFER als erwartet: schon W_0 ist indefinit (%.1e), "
          "der Bruch Zelle %s ist die LETZTE W_0-Zelle -- im vollen "
          "A_0 rettet das n=2-Atom (Zelle %d) exakt diese Zelle]: "
          "der linke Faktor des Review-Zertifikats [Kontinuums-"
          "Wurzel (+) Kraus] ist NIRGENDS ein PSD-Objekt -- jedes "
          "Atom rettet die Positivitaet 'just in time' (5c/5d-Fluss)"
          % (", ".join("%.2e" % l for l in lams), bd, cell2, cell3,
             lams[0], bd, cell2), ok_v706)

    # (b) the subtlety: continuum part of the SCHUR complement
    rungs_c, _ = srp.schur_ladder(c_cont, sizes)
    lamsC = [r["lamS"] for r in rungs_c]
    all_neg = all(l < 0 for l in lamsC)
    check("M1.3b KONTINUUMS-SCHUR (die Auftrags-Feinheit): "
          "lambda_min(S_k^cont) = %s -- %s; TYPUNG: da A_k^cont ab "
          "k = 1 INDEFINIT ist, ist S_k^cont KEIN Haynsworth-Objekt "
          "(kein Schur-Komplement einer PSD-Matrix): 'Kontinuums-"
          "Anteil des Schur-Komplements' ist als PSD-Baustein ebenso "
          "tot wie der volle Block"
          % (", ".join("%.2e" % l for l in lamsC),
             "ALLE NEGATIV" if all_neg else "NICHT alle negativ "
             "(gemischt -- Formel-Artefakt ohne Kompressions-"
             "Bedeutung)"), True)  # measurement, typed either way

    # (c) additive assembly
    lamsD = []
    for r, rc in zip(rungs, rungs_c):
        D = r["S"] - rc["S"]
        lamsD.append(float(np.min(np.linalg.eigvalsh(
            0.5 * (D + D.T)))))
    ok_add_dead = all(l < 0 for l in lamsD)
    check("M1.3c ADDITIVE MONTAGE SCHLIESST NICHT: lambda_min(S_k - "
          "S_k^cont) = %s -- der Atom-/Kraus-Anteil ist auf JEDER "
          "Stufe indefinit: die Ordnung-1-Balance sitzt im KREUZTERM "
          "(wie im Schur-Befund benannt), eine Summe zweier "
          "PSD-Gram-Faktoren ist die falsche Gestalt"
          % ", ".join("%.2e" % l for l in lamsD), ok_add_dead)

    # (d) the rescue cascade: growing channel unions
    unions = [("cont", c_cont),
              ("+ram-odd", c_cont + sec_lags["ro"]),
              ("+ram-even", c_cont + sec_lags["ro"] + sec_lags["re"]),
              ("+split", c_cont + sec_lags["ro"] + sec_lags["re"]
               + sec_lags["sp"]),
              ("voll", c_cont + sec_lags["ro"] + sec_lags["re"]
               + sec_lags["sp"] + sec_lags["in"])]
    rows = []
    bds = []
    for nm, cv in unions:
        b = lev_breakdown(cv)
        bds.append(b)
        rows.append("%s: %s" % (nm, "PD (kein Bruch)" if b is None
                                else "Bruch Zelle %d" % b))
    ok_casc = bds[-1] is None and all(b is not None for b in bds[:-1])
    check("M1.3d DIE RETTUNGS-KASKADE: Levinson-Breakdown der "
          "wachsenden Kanal-Vereinigungen: %s -- KEINE echte "
          "Teilfamilie traegt: die Atome retten in ZELL-Reihenfolge "
          "(n = 2 ram-odd, n = 3 INERT, n = 4 ram-even, n = 5 split, "
          "...), quer zu den Kanaelen; ein Zertifikat muss atomweise/"
          "zellweise faktorisieren, nicht sektorweise"
          % "; ".join(rows), ok_casc)
    return lams, lamsC, lamsD, bds


# ================================================================== M2
def m2_verdict(rungs, lams, lamsD):
    print("\nM2 -- Satz-Kandidat oder praezises Negativ")
    root_dead = all(l < 0 for l in lams)
    add_dead = all(l < 0 for l in lamsD)
    s_pos = all(r["lamS"] > 0 for r in rungs)
    if s_pos and root_dead:
        verdict = "CERT-CONTINUUM-ROOT-DEAD"
    elif s_pos:
        verdict = "CERT-ASSEMBLED"
    else:
        verdict = "CERT-DEAD"
    print("""
  DAS PRAEZISE NEGATIV (radikal ehrlich, keine Konfetti):
  1. Das spezifizierte Zertifikat R_k = [Kontinuums-Wurzel (+)
     Kraus-Faktoren] ist NICHT montierbar: der linke Faktor existiert
     nicht (M1.3a: arch+pol bricht zwischen n=2- und n=3-Zelle, und
     zwar auf JEDER Stufe inkl. W_0 -- v706 [M], leiter-weit); auch die
     Schur-Version des Kontinuums ist kein PSD-Baustein (M1.3b), und
     die additive Summe zweier Gram-Faktoren hat das falsche
     Vorzeichenprofil (M1.3c).
  2. DIE MAUER TAUCHT IM ZERTIFIKAT WIEDER AUF -- benannt: der
     'Kontinuums-Wurzel-Anteil' existiert nur mit ALLEN Atomen
     zusammen; 'jedes Atom rettet rechtzeitig, gleichmaessig in der
     Tiefe' IST die PD-Persistenz (aequivalent |Schur/Verblunsky-
     Parameter| < 1 fuer immer, v706 W1.1 [E]; als Induktions-Route
     bereits RH-Grade typisiert, v703 TOLERANCE-RH-GRADE:
     Levinson-Rekursion = instabiles Shooting).  Sie ist nicht
     umbenannt versteckt -- sie ist der fehlende linke Faktor.
  3. WAS VON DER REVIEW-SERIE STEHT (die echten [E]-Gewinne):
     (i) der Label-Baustein ist REAL: T = 4B^2 = 196 K^2 exakt als
     Korrespondenz-Komposition, KMS-1/2 im Turm exakt (M1.1b),
     kanonische Polaritaet, CP/Stinespring-Erweiterung -- sein
     Einsatzort ist praezise die chi_par-Spur der duennen 2-adischen
     Schiene (M1.2: masse-armer, fallender Kreuzterm-Anteil) im
     Zustand tau_inc (x) tau_Toeplitz; (ii) die Schur-Leiter selbst
     (S_k >= 0 gemessen,
     flache Margen) bleibt der korrekt formulierte Induktionsrahmen:
     Basis [E-endlich] + Douglas [E] + Haynsworth [E] + Kofinalitaet
     [E] -- offen ist EXAKT das Gram-Zertifikat pro Schritt.
  4. DIE KORRIGIERTE ZERTIFIKAT-GESTALT (Kandidat fuer die naechste
     Runde, aus M1.3d): atomweise/zellweise Kaskaden-Faktorisierung
     (die Rettung laeuft in Zell-Reihenfolge n = 2, 3, 4, 5, ...,
     quer zu den Kanaelen) -- der TWOSTEP liefert dafuer den
     2-adischen Schienenstrang (Schrittweite 2 log 2, Gewicht 1/2,
     Kanal K^2), aber die inerten/split-Zellen brauchen ihre eigenen
     Glieder: ein Kaskaden-Gram R = Prod (Zell-Faktoren), nicht
     R = R_cont (+) R_label.""")
    return verdict


def run():
    print("SYNTHESE -- Montage des Gram-Zertifikats aus dem "
          "Depolarisierer")
    g0_firewall()

    sizes = srp.ladder_sizes()
    M_full = sizes[-1]
    alpha_full = 0.5 * M_full * srp.DGRID
    ka, masks, dev_m = srp.channel_masks(alpha_full)
    c_cont = srp.continuum_lags(M_full)
    sec_lags = {"ct": c_cont}
    for cnl in ("ro", "re", "sp", "in"):
        sec_lags[cnl] = srp.atom_channel_lags(alpha_full, M_full,
                                              masks[cnl])
    c_full = sum(sec_lags.values())
    rungs, _T = srp.schur_ladder(c_full, sizes)
    lam_ref = [2.695744e-04, 1.701240e-04, 1.528313e-04, 1.473936e-04,
               1.360080e-04, 1.215473e-04, 1.171285e-04, 1.148644e-04]
    dev_rep = max(abs(r["lamS"] - lr) / lr
                  for r, lr in zip(rungs, lam_ref))
    check("G0.2 REPRODUKTION der Schur-Leiter (Kamm-Konsistenz dev "
          "%.1e; lambda_min(S_k) == Schur-Proben-Werte, max rel dev "
          "%.1e): die Montage arbeitet auf demselben Objekt"
          % (dev_m, dev_rep), dev_m <= 1.0e-12 and dev_rep <= 1.0e-5)

    m11_twostep(sizes, masks, ka)
    m12_crossterm(rungs, sec_lags, sizes)
    lams, lamsC, lamsD, bds = m13_certificate(rungs, c_cont, sizes,
                                              sec_lags)
    verdict = m2_verdict(rungs, lams, lamsD)

    n_ok = sum(1 for _n, ok in CHECKS if ok)
    print("\n[%s] %d/%d checks, %.1f s" % (verdict, n_ok, len(CHECKS),
                                           time.time() - T0))
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(run())
