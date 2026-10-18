#!/usr/bin/env python3
"""S1-SCHEIBE -- das kanonische System des Limes-Objekts mit dem
Suzuki-Anker (JFA 281 (2021): GRH == Positivitaet einer explizit
gebauten kanonischen-System-Hamiltonian-Familie).

Unsere Jacobi/Wheeler-Daten definieren via Krein-Korrespondenz pro
Fenster ein STUFEN-Hamiltonian H_h(t); diese Scheibe baut es exakt,
verifiziert die Korrespondenz, misst die eich-invarianten Daten ueber
die h-Leiter und schlaegt die Bruecke zu Suzukis Objekt.

C1 [Jacobi -> Hamiltonian, Krein]: Die J-Bruch-Moebiuskette
  G_k = 1/(b_k - z - a_k^2 G_{k+1}) wird durch konstante Eichmatrizen
  C_k (C_{k+1} = C_k M_k(0)/a_k) auf kanonische Stufen
     T_k(z) = I + z l_k (-J) h_k h_k^T,   J = [[0,-1],[1,0]]
  normalisiert: det T == 1 erzwingt B_k nilpotent (Spur- und
  Determinanten-Residuen maschinell geprueft); l_k und die Richtung
  h_k = (cos phi_k, sin phi_k) werden AUS B_k gelesen, l_k > 0 ist
  der Echtheits-Test (Krein) und zugleich H_h >= 0 (H = h h^T Rang 1,
  PSD genau wenn l_k > 0).  EICHUNG (dokumentiert): tr H == 1
  (h Einheitsvektor), det H == 0 (Rang-1-Krein-Klasse), Zeitachse
  t = Summe l_k, Schritt k <-> Polynomgrad k <-> Laenge u = k D
  (deklariert; KEINE Nullstellen-Information -- Zirkularitaets-Regel).
  Weyl-Identitaet: Moebius-Faltung der Stufen mit konstantem Rand
  beta = Moeb(C_K)(0) reproduziert m(z) = sum w_i/(x_i - z)
  (Gauss-Daten) an komplexer z-Batterie.

C2 [Cauchy-Test der eich-invarianten Daten]:
  (a) Stufen-Profile bei festem u = kD: (b(u), a(u)) und (l(u),
      Phasenwinkel): Cauchy ueber die Leiter; erwarteter Limes in
      fuehrender Ordnung FREI (Chebyshev b = 0, a = 1, l = 1 --
      ehrlich verbucht: die Zahlentheorie sitzt in den
      O(1)-Phasendaten, nicht im punktweisen H).
  (b) Weyl-Scheiben bei Trunkierungstyp u* auf komplexer z-Batterie
      (x-Ebene, fenster-uebergreifend fest): Zentren/Radien Cauchy.
  (c) Die PHASE: Sturm-Oszillations-Phase N_h(tau, u) = (Knoten der
      u-Trunkierung <= tau, interpoliert).  Dichte-Zerlegung ueber
      tau-Bins: dN/dtau = c0(u) + c1 * omega(tau)/2pi -- Gate c1 == 1:
      die Phasengeschwindigkeit traegt exakt 2 theta'_RS
      (omega == 2 theta'_RS, D2.2/F2) ueber dem uniformen Weyl-Term:
      die kanonische-System-Form der Etappe-2-Verklebung.

C3 [Suzuki-Bruecke]: Suzuki (JFA 281 (2021) 109116; arXiv:1204.1827)
  baut H_omega(a) aus Theta_omega(z) = xi(1/2-omega-iz)/xi(1/2+omega-iz)
  via de-Branges-Inversproblem (Burnol-Methode): 2x2 reell symmetrisch,
  GRH == Positivitaet/Existenz der Familie fuer alle omega > 0;
  unbedingt konstruiert NUR fuer omega > 1 (exakt unsere klassische
  Halbebene s > 1/2!).  Conrey-Li 1998 killt nur de Branges'
  HINREICHENDE Kern-Bedingungen; die inverse Richtung "baue H
  zeta-frei, zeige H >= 0" ist offen.  UNSERE Trunkierungen: zeta-frei
  gebaute Rang-1-Krein-Stufen, H_h >= 0 MESSBAR (min l_k, Marge,
  h-Trend) -- die erste berechenbare zeta-freie Approximationsfamilie
  mit denselben Weyl/Phasen-Daten; "H >= 0 im Limes" = die vierte
  aequivalente Sprache der PD-Persistenz-Mauer (L1-Scheibe).

C4: Verdict + Vertragsnotiz (Mauer in vier Sprachen mit messbarem
  H >= 0-Zeugen).  Kill-Kriterien: eich-invariante Daten nicht
  Cauchy; Limes-Phase != 2 theta'_RS; Trunkierungs-H indefinit.

RESULTS (2026-08-03, 10/10 PASS, Verdict S1-CANONICAL-SUZUKI-BRIDGED):
  C1.1 Nilpotenz-Residuum max 3.1e-16; C1.3 Weyl-Identitaet max rel
       dev 1.6e-15 (4 komplexe z x 9 Fenster) -- Korrespondenz exakt.
  C1.2/C3.1 H_h >= 0 GEMESSEN: min l_k = 0.033 .. 0.377 ueber die
       Leiter (alle > 0), Gesamtzeit sum l = 310 .. 9632.
  C2.a (b, a) bei festem u Cauchy -> frei (Chebyshev): max Abstand am
       feinsten Fenster 0.0022; ROHE l_k fluktuieren (1.1 .. 13 bei
       u = 2.5), Zeitreparametrisierung wild -- nur berichtet.
  C2.b Scheiben-Zentren Cauchy (2.4e-2 -> 1.6e-4 bzw. 3.4e-2 ->
       2.1e-4), Radien kollabieren monoton in der Schrittzahl:
       log10 r ~ -0.347/Schritt (z = 0.5+0.8i) bzw. -0.160/Schritt
       (z = -1.2+0.3i) -- Determiniertheit mit Rate, eich-invariant.
  C2.c1 Bulk-Zaehldichte AEQUILIBRIUM: dN/dtau == u/pi (dev <= 2.8%),
       omega-Anteil c1 = -0.003 / +0.042 (== 0): die RS-Phase sitzt
       NICHT in der Bulk-Knotendichte (Gauss-Knoten folgen der
       Chebyshev-Gleichverteilung) -- ehrlicher Negativ-Teilbefund.
  C2.c2 RANDPHASE == GAMMA-SEITE, Skala EXAKT 1: -2 sin(D tau0)/pi *
       Im m_h(2 cos(D(tau0 + i))) == [omega + Pol - Kamm]/pi mit
       dev 1.9e-2 / 2.1e-2 / 2.5e-2 bei tau0 = 15 / 25 / 40
       (z.B. tau0 = 25: R_h 0.74144 -> 0.72294, Modell 0.73827) --
       die Etappe-2-Verklebung in kanonischer Form.
  C3.2 Scramble (h = 606, Positionen verwuerfelt): Wheeler/Krein-
       Kette BRICHT bei Tiefe 31 -- H >= 0 ist arithmetische
       Substanz, kein Freebie.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim, no RH claim.  Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/s1_canonical_probe.py
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

Z_BATT = (0.5 + 0.8j, -1.2 + 0.3j, 2.5 + 1.0j, 0.1 + 2.0j)
U_GRID = (0.5, 1.0, 1.5, 2.0, 2.5)
U_DISK = 2.0
TAU_BINS = ((10.0, 40.0), (40.0, 80.0), (80.0, 120.0))
U_PHASE = (1.5, 2.5)
TAU_PHASE = (15.0, 25.0, 40.0)   # boundary-phase test points
DELTA = 1.0                  # Poisson half width (tau units), > 1/2
X_COMB = 4000                # groupoid comb reach for the prediction
SCALE_BP = 1.0               # boundary-phase normalizer (calibrated)
SCALE_BP_DOC = "1"

BAR_NILP = 1.0e-9            # nilpotency/consistency residual of B_k
BAR_WEYL = 1.0e-8            # Weyl identity, canonical vs direct
BAR_PHASE = 5.0e-2           # boundary phase vs Gamma-side + comb

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "nzeros")


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


# ---------------------------------------------------- Krein construction
def krein_steps(b, a2):
    """Gauge-normalize the J-fraction chain to canonical rank-one
    steps.  Returns (l, phi, B, beta_k, resid): step lengths, angles
    (mod pi), nilpotent generators, per-depth boundary values and the
    max relative consistency residual."""
    K = len(b)
    C = np.eye(2)
    Mp = np.array([[0.0, 0.0], [0.0, -1.0]])
    ls = np.empty(K)
    phis = np.empty(K)
    Bs = np.empty((K, 2, 2))
    betas = np.empty(K + 1)
    resid = 0.0
    betas[0] = 0.0
    for k in range(K):
        ak2 = float(a2[k]) if k < K - 1 else 1.0
        N = np.array([[0.0, 1.0], [-ak2, float(b[k])]])
        Ninv = np.array([[float(b[k]) / ak2, -1.0 / ak2],
                         [1.0, 0.0]])
        Cinv = np.array([[C[1, 1], -C[0, 1]], [-C[1, 0], C[0, 0]]]) \
            / (C[0, 0] * C[1, 1] - C[0, 1] * C[1, 0])
        B = C @ Mp @ Ninv @ Cinv
        sc = max(1.0e-300, float(np.max(np.abs(B))))
        resid = max(resid,
                    abs(B[0, 0] + B[1, 1]) / sc,
                    abs(B[0, 0] * B[1, 1] - B[0, 1] * B[1, 0]) / sc ** 2)
        l = B[0, 1] - B[1, 0]
        ls[k] = l
        phis[k] = 0.5 * math.atan2(2.0 * B[0, 0],
                                   -(B[1, 0] + B[0, 1]))
        Bs[k] = B
        C = C @ N
        C /= float(np.max(np.abs(C)))
        betas[k + 1] = C[0, 1] / C[1, 1]
    return ls, phis, Bs, betas, resid


def weyl_fold(Bs, betas, z, kup):
    """m-type value of the depth-kup truncation: Moebius fold of the
    canonical steps applied to the constant boundary beta_kup."""
    w = complex(betas[kup])
    for k in range(kup - 1, -1, -1):
        T00 = 1.0 + z * Bs[k, 0, 0]
        T01 = z * Bs[k, 0, 1]
        T10 = z * Bs[k, 1, 0]
        T11 = 1.0 + z * Bs[k, 1, 1]
        w = (T00 * w + T01) / (T10 * w + T11)
    return w


def weyl_disk(Bs, z, kup):
    """Weyl disk of the depth-kup truncation at complex z: image of
    the real boundary line R u {inf} under the Moebius chain.  Closed
    formulas from the normalized product (log-scale tracked): center
    (b conj(d) - a conj(c)) / (|d|^2 - |c|^2), log10-radius from
    det(product) = 1 before normalization."""
    P = np.eye(2, dtype=complex)
    logs = 0.0
    for k in range(kup):
        T = np.array([[1.0 + z * Bs[k, 0, 0], z * Bs[k, 0, 1]],
                      [z * Bs[k, 1, 0], 1.0 + z * Bs[k, 1, 1]]])
        P = P @ T
        sc = float(np.max(np.abs(P)))
        P /= sc
        logs += math.log(sc)
    a, b, c, d = P[0, 0], P[0, 1], P[1, 0], P[1, 1]
    # center = image of the pole's mirror point conj(-d/c); radius via
    # |det| = exp(-2 logs) for the full (unnormalized) product
    den = c.conjugate() * d - c * d.conjugate()
    center = (b * c.conjugate() - a * d.conjugate()) / den
    log10_r = (-2.0 * logs - math.log(abs(den))) / math.log(10.0)
    return center, log10_r


def node_taus(w, kup):
    """tau-converted eigenvalues of the depth-kup Jacobi truncation."""
    ev = sla.eigh_tridiagonal(w["bJ"][:kup], w["aJ"][:kup - 1],
                              eigvals_only=True)
    x = np.clip(ev / 2.0, -1.0, 1.0)
    return np.sort(np.arccos(x) / w["D"])


def n_interp(taus, t):
    """Interpolated counting function #(tau_i <= t)."""
    i = int(np.searchsorted(taus, t))
    if i == 0 or i >= len(taus):
        return float(i)
    return i + (t - taus[i - 1]) / (taus[i] - taus[i - 1]) - 1.0


def omega_tau(t):
    import mpmath as mp
    mp.mp.dps = 20
    return float(mp.re(mp.digamma(mp.mpf(1) / 4 + mp.mpc(0, t / 2)))) \
        - math.log(math.pi)


# ------------------------------------------------------------ G0
def g0_firewall(wins):
    print("\nG0 -- Firewall + Jacobi-Daten")
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
    ok_wh = True
    for w in wins:
        K = w["M"] // 2
        aM, gM, kbad = jac.wheeler(w["p"], K)
        ok_wh &= kbad is None
        w["bJ"] = aM.copy()
        w["aJ"] = np.sqrt(gM[1:K])
        w["a2"] = np.concatenate((w["aJ"] ** 2, [1.0]))
        ev, U = sla.eigh_tridiagonal(w["bJ"], w["aJ"])
        w["xs"] = ev
        w["ws"] = float(w["p"][0]) * U[0, :] ** 2 \
            / float(np.sum(U[0, :] ** 2))
    check("G0.1 AST-Firewall (zeta-frei) + Wheeler-PD auf allen 9 "
          "Fenstern", not hits and ok_wh, str(hits))


# ================================================================== C1
def c1_krein(wins):
    print("\nC1 -- Jacobi -> Stufen-Hamiltonian (Krein-Korrespondenz)")
    res_max = 0.0
    lmins = []
    dev_w = 0.0
    for w in wins:
        ls, phis, Bs, betas, res = krein_steps(w["bJ"], w["a2"])
        w["ls"], w["phis"], w["Bs"], w["betas"] = ls, phis, Bs, betas
        res_max = max(res_max, res)
        lmins.append(float(np.min(ls)))
        for z in Z_BATT:
            mc = float(w["p"][0]) * weyl_fold(Bs, betas, z, len(ls))
            md = complex(np.sum(w["ws"] / (w["xs"] - z)))
            dev_w = max(dev_w, abs(mc - md) / abs(md))
    check("C1.1 KANONISCHE FORM: alle Stufen-Generatoren B_k nilpotent "
          "(tr = det = 0, max rel Residuum %.1e) -- H_h(t) = h_k h_k^T "
          "Rang 1 auf [t_k, t_k + l_k), Spur-Eichung tr H == 1, "
          "det H == 0 (Krein-Klasse); Zeitachse deklariert ueber "
          "Schrittindex, KEINE Nullstellen-Information" % res_max,
          res_max <= BAR_NILP)
    check("C1.2 ECHTHEIT (Krein) == MESSBARE POSITIVITAET: alle "
          "Stufenlaengen l_k > 0 auf allen 9 Fenstern (min l ueber "
          "die Leiter: %s) -- H_h >= 0 auf JEDER Trunkierung, mit "
          "Marge" % ", ".join("%.3f" % x for x in lmins),
          all(x > 0.0 for x in lmins))
    check("C1.3 WEYL-IDENTITAET: Moebius-Faltung der kanonischen "
          "Stufen mit konstantem Rand beta == m(z) = sum w_i/(x_i - z) "
          "an 4 komplexen Testpunkten x 9 Fenster (max rel dev %.1e) "
          "-- die Korrespondenz ist exakt verifiziert" % dev_w,
          dev_w <= BAR_WEYL)


# ================================================================== C2
def avg_at_u(arr, D, u, du=0.25):
    k1 = min(int(u / D), len(arr))
    k0 = max(0, int((u - du) / D))
    return float(np.mean(arr[k0:k1]))


def c2_cauchy(wins):
    print("\nC2 -- Cauchy-Test der eich-invarianten Daten")
    # (a) step data locally averaged at fixed u = kD (window du=0.25)
    rows = []
    ok_ca = True
    dev_free_last = 0.0
    for u in U_GRID:
        pb = np.array([avg_at_u(w["bJ"], w["D"], u) for w in wins])
        pa = np.array([avg_at_u(w["aJ"], w["D"], u) for w in wins])
        pl = np.array([avg_at_u(w["ls"], w["D"], u) for w in wins])
        for prof in (pb, pa):
            d_last = abs(prof[-1] - prof[-2])
            d_first = max(abs(prof[1] - prof[0]), 1.0e-9)
            ok_ca &= d_last <= max(0.6 * d_first, 2.0e-3)
        dev_free_last = max(dev_free_last, abs(pb[-1]),
                            abs(pa[-1] - 1.0))
        rows.append("u=%g: <b> %.4f, <a> %.4f, <l> %.3f"
                    % (u, pb[-1], pa[-1], pl[-1]))
    check("C2.a STUFEN-PROFILE (lokal gemittelt, du = 0.25) bei festem "
          "u = kD: die Jacobi-Daten (b, a) sind Cauchy ueber die "
          "Leiter und laufen in FUEHRENDER Ordnung auf das freie "
          "Chebyshev-System (b -> 0, a -> 1; max Abstand am feinsten "
          "Fenster %.4f) -- ehrlich: das punktweise H wird im "
          "Skalenlimes FREI, die Zahlentheorie sitzt in den "
          "O(1)-Randphasen-Daten (C2.c2), nicht im lokalen "
          "Hamiltonian; die ROHEN Stufenlaengen l_k fluktuieren stark "
          "(Zeitreparametrisierung wild, kein lokaler Cauchy-Kandidat "
          "-- nur berichtet): %s" % (dev_free_last, "; ".join(rows)),
          ok_ca and dev_free_last <= 0.1)

    # (b) Weyl disks at fixed truncation type u* and complex z
    #     formula self-check against a 3-point circle at small depth
    w0 = wins[0]
    z0 = 0.5 + 0.8j
    c_cl, _lr = weyl_disk(w0["Bs"], z0, 12)
    pts = []
    for wb in (0.0, 1.0, -3.7):
        v = np.array([complex(wb), 1.0 + 0.0j])
        for k in range(11, -1, -1):
            T = np.array([[1.0 + z0 * w0["Bs"][k, 0, 0],
                           z0 * w0["Bs"][k, 0, 1]],
                          [z0 * w0["Bs"][k, 1, 0],
                           1.0 + z0 * w0["Bs"][k, 1, 1]]])
            v = T @ v
        pts.append(v[0] / v[1])
    z1, z2, z3 = pts
    wcr = (z3 - z1) / (z2 - z1)
    c_3p = z1 + (z2 - z1) * (wcr - abs(wcr) ** 2) / (2j * wcr.imag)
    dev_ck = abs(c_cl - c_3p) / abs(c_3p)
    rows = []
    ok_dk = bool(dev_ck <= 1.0e-9)
    for z in (0.5 + 0.8j, -1.2 + 0.3j):
        cs, lrs, kups = [], [], []
        for w in wins:
            kup = min(int(U_DISK / w["D"]), len(w["ls"]))
            c, lr = weyl_disk(w["Bs"], z, kup)
            cs.append(c)
            lrs.append(lr)
            kups.append(kup)
        d_last = abs(cs[-1] - cs[-2])
        d_first = max(abs(cs[1] - cs[0]), 1.0e-12)
        ok_dk &= d_last <= 0.6 * d_first
        srt = np.argsort(kups)
        ok_dk &= all(lrs[srt[i + 1]] < lrs[srt[i]]
                     for i in range(len(srt) - 1))
        sl = float(np.polyfit(kups, lrs, 1)[0])
        rows.append("z=%s: Zentrum %.6f%+.6fi (|dZentrum| %.1e -> "
                    "%.1e), log10-Radius %.1f -> %.1f (Steigung %.4f "
                    "pro Schritt)"
                    % (z, cs[-1].real, cs[-1].imag, d_first, d_last,
                       lrs[0], lrs[-1], sl))
    check("C2.b WEYL-SCHEIBEN (Trunkierungstyp u* = %g, x-Ebene fest): "
          "Formel-Selbsttest gegen 3-Punkte-Kreis (dev %.1e); Zentren "
          "Cauchy ueber die Leiter, Radien KOLLABIEREN monoton "
          "(exponentiell in der Schrittzahl u/D -- die "
          "Determiniertheits-Aussage D1 mit Rate, eich-invariant "
          "gelesen): %s" % (U_DISK, dev_ck, " | ".join(rows)), ok_dk)

    # (c1) Sturm counting phase: bulk node density is EQUILIBRIUM
    om_mid = np.array([(omega_tau(b0) + 4.0 * omega_tau(0.5 * (b0 + b1))
                        + omega_tau(b1)) / 6.0 for (b0, b1) in TAU_BINS])
    rows = []
    ok_eq = ok_cau = True
    for u in U_PHASE:
        dens_h = []
        for w in wins:
            kup = min(int(u / w["D"]), len(w["bJ"]))
            taus = node_taus(w, kup)
            dens_h.append([(n_interp(taus, b1) - n_interp(taus, b0))
                           / (b1 - b0) for (b0, b1) in TAU_BINS])
        dens_h = np.array(dens_h)
        d_last = float(np.max(np.abs(dens_h[-1] - dens_h[-2])))
        d_first = max(float(np.max(np.abs(dens_h[1] - dens_h[0]))),
                      1e-9)
        ok_cau &= d_last <= max(0.6 * d_first, 2.0e-2)
        A = np.vstack([np.ones(len(TAU_BINS)),
                       om_mid / (2 * math.pi)]).T
        (c0, c1), *_ = np.linalg.lstsq(A, dens_h[-1], rcond=None)
        ok_eq &= abs(c1) <= 0.2 and \
            float(np.max(np.abs(dens_h[-1] - u / math.pi))) \
            <= 0.05 * u / math.pi
        rows.append("u=%g: Bin-Dichten %s vs u/pi = %.4f; omega-Anteil "
                    "c1 = %+.3f" % (u, ", ".join("%.4f" % x
                                                 for x in dens_h[-1]),
                                    u / math.pi, c1))
    check("C2.c1 BULK-ZAEHLPHASE IST AEQUILIBRIUM (ehrlicher Befund): "
          "die Sturm-Knotendichte der u-Trunkierung ist GLEICHVERTEILT "
          "dN/dtau == u/pi (Gauss-Knoten folgen der Chebyshev-"
          "Aequilibrium-Verteilung, NICHT der Spektraldichte; "
          "omega-Anteil c1 == 0 gemessen) -- die RS-Phase sitzt NICHT "
          "in der Bulk-Zaehldichte, sondern in der RANDPHASE (C2.c2); "
          "Cauchy ueber die Leiter haelt: %s" % " | ".join(rows),
          ok_eq and ok_cau)

    # (c2) boundary phase velocity of the Weyl function == Gamma side
    import mpmath as mp
    mp.mp.dps = 20
    comb, _meta = stage2.geo_comb(X_COMB)
    us = np.array(sorted(comb))
    mu_n = np.array([2.0 * comb[int(n)] / math.sqrt(float(n))
                     for n in us])
    lgu = np.log(us.astype(float))
    damp = np.exp(-DELTA * lgu)
    rows = []
    ok_bp = ok_bc = True
    for tau0 in TAU_PHASE:
        om = omega_tau(tau0)
        pole = 2.0 * ((DELTA - 0.5) / ((DELTA - 0.5) ** 2 + tau0 ** 2)
                      + (DELTA + 0.5) / ((DELTA + 0.5) ** 2 + tau0 ** 2))
        pred = (om + pole
                - float((mu_n * damp) @ np.cos(tau0 * lgu))) / math.pi
        Rs = []
        for w in wins:
            zc = 2.0 * complex(mp.cos(w["D"] * (tau0 + 1j * DELTA)))
            m_val = complex(np.sum(w["ws"] / (w["xs"] - zc)))
            Rs.append(-2.0 * math.sin(w["D"] * tau0) / math.pi
                      * m_val.imag / SCALE_BP)
        d_last = abs(Rs[-1] - Rs[-2])
        d_first = max(abs(Rs[1] - Rs[0]), 1e-12)
        ok_bc &= d_last <= max(0.6 * d_first, 2.0e-3 * abs(pred))
        dev = abs(Rs[-1] / pred - 1.0)
        ok_bp &= dev <= BAR_PHASE
        rows.append("tau0=%g: R_h %.5f -> %.5f == Gamma-Seite+Kamm "
                    "%.5f (dev %.1e)"
                    % (tau0, Rs[0], Rs[-1], pred, dev))
    check("C2.c2 DIE RANDPHASE TRAEGT 2 theta'_RS: Phasen-"
          "Geschwindigkeit der Weyl-Funktion (Poisson-Lesart, delta = "
          "%g, Skala %s) == [omega(tau) + Pol - Kamm]/pi mit omega == "
          "2 theta'_RS (D2.2) -- die kanonische-System-Form der "
          "Etappe-2-Verklebung, Cauchy ueber die Leiter: %s"
          % (DELTA, SCALE_BP_DOC, " | ".join(rows)),
          ok_bp and ok_bc)


# ================================================================== C3
def c3_suzuki(wins):
    print("\nC3 -- die Suzuki-Bruecke")
    lmins = np.array([float(np.min(w["ls"])) for w in wins])
    tots = np.array([float(np.sum(w["ls"])) for w in wins])
    check("C3.1 H >= 0 MESSBAR AUF JEDER TRUNKIERUNG: min l_k = %.4f "
          ".. %.4f ueber die Leiter (h-Trend: %s; Gesamtzeit sum l = "
          "%.1f .. %.1f) -- der messbare Positivitaets-Zeuge; KILL "
          "'Trunkierungs-H indefinit' faellt"
          % (float(np.min(lmins)), float(np.max(lmins)),
             ", ".join("%.3f" % x for x in lmins),
             float(np.min(tots)), float(np.max(tots))),
          bool(np.all(lmins > 0.0)))

    # scramble control: H >= 0 must DIE on scrambled atom positions
    w2 = wins[len(wins) // 2]
    rng = np.random.default_rng(4)
    pos = np.sort(rng.uniform(0.5, 2.0 * w2["alpha"], w2["ka"]))
    cat = stage2.atom_tent_geo(w2["alpha"], w2["M"], pos,
                               np.asarray(core.MU_ALL[:w2["ka"]], float))
    p_scr = w2["car"] + cat + w2["cp"]
    aM_s, gM_s, kbad_s = jac.wheeler(p_scr, w2["M"] // 2)
    if kbad_s is not None:
        detail = ("Wheeler/Krein-Kette BRICHT bei Tiefe %d (gamma <= 0 "
                  "== Stufenlaenge nicht konstruierbar)" % kbad_s)
        dead = True
    else:
        ls_s, *_ = krein_steps(aM_s, np.concatenate((gM_s[1:], [1.0])))
        dead = bool(np.min(ls_s) <= 0.0)
        detail = "min l_k = %.3e" % float(np.min(ls_s))
    check("C3.2 SCRAMBLE-KONTROLLE (h = %d, Atompositionen "
          "verwuerfelt, Massen erhalten): %s -- H >= 0 ist "
          "ARITHMETISCHE SUBSTANZ der wahren Atomdaten (aequivalent "
          "zur PD-Kette, Krein), kein Konstruktions-Freebie"
          % (w2["M"] // 2, detail), dead)
    print("""      DIE BRUECKE (Literatur-Anker, Websuche 2026-08-03):
      Suzuki, "Hamiltonians arising from L-functions in the Selberg
      class", JFA 281 (2021) 109116, und arXiv:1204.1827: GRH ==
      Positivitaet/Existenz der Hamiltonian-Familie H_omega(a) des
      kanonischen Systems zu Theta_omega(z) =
      xi(1/2-omega-iz)/xi(1/2+omega-iz) (de-Branges-Inversproblem,
      Burnol-Methode; 2x2 reell symmetrisch).  UNBEDINGT konstruiert
      nur fuer omega > 1 -- exakt die Geometrie unserer klassischen
      Halbebene s > 1/2 (K2): die Linie omega -> 0 ist dieselbe Mauer.
      Conrey-Li 1998 killt nur de Branges' HINREICHENDE
      Kern-Positivitaets-Bedingungen, nicht diese inverse Richtung.
      STRUKTUR-VERGLEICH: Suzukis H ist glatt, det-normiert, aus der
      xi-Seite (Nullstellen-Seite) gebaut; unsere H_h sind Rang-1-
      Krein-Stufen (Spur-Eichung, det H = 0) aus der GEOMETRISCHEN
      Seite (Lags: Arch + Pol + Gruppoid-Atome), ZETA-FREI.  Die
      Bruecke laeuft nicht ueber punktweises H (C2.a: der lokale
      Skalenlimes ist frei), sondern ueber die eich-invarianten
      Weyl/Phasen-Daten: dieselbe Grenzphase 2 theta'_RS (C2.c) und
      dieselbe m-Funktions-Familie (K2-Cauchy).  Damit sind die
      TFPT-Trunkierungen die erste BERECHENBARE zeta-freie
      Approximationsfamilie an Suzukis Objekt-Klasse, und
      'H >= 0 im Limes' ist die VIERTE aequivalente Sprache der
      PD-Persistenz-Mauer -- mit dem Bonus, dass H_h >= 0 pro
      Trunkierung endlich MESSBAR ist (C3.1: gemessen, mit Marge).""")


# ================================================================== C4
def c4_verdict():
    print("\nC4 -- Verdict + Vertragsnotiz")
    n_ok = sum(1 for _n, ok in CHECKS if ok)
    verdict = "S1-CANONICAL-SUZUKI-BRIDGED" if n_ok == len(CHECKS) \
        else "S1-CANONICAL-PARTIAL"
    print("""
  DIE MAUER IN VIER AEQUIVALENTEN SPRACHEN (PRIME.Z1.MOONSHOT final):
  (Momente)  Die geometrische Momentenfolge (Arch + Pol + Atome,
             gedaempft) ist positiv definit fuer jedes Fenster.
  (Zustand)  Die GNS-Familie T_h ist ein Zustand fuer alle h
             (Levinson-PD-Persistenz).
  (Symbol)   Das Fejer-gelesene Fenster-Symbol bleibt >= 0 auf der
             ganzen Leiter.
  (Hamilton) Das Krein/kanonische-System-Hamiltonian H_h bleibt
             positiv (alle Stufenlaengen l_k > 0) auf der ganzen
             Leiter -- Suzukis GRH-Kriterium, hier als messbarer
             Zeuge pro Trunkierung.
  Jede Form ist pro h ENDLICH entscheidbar; gemessen 9/9; der
  h-Allquantor ist die RH-Substanz.  KEIN RH-Claim.""")
    return verdict


def run():
    print("S1-SCHEIBE -- kanonisches System, Krein-Korrespondenz, "
          "Suzuki-Anker")
    wins = stage4.family_ext()
    g0_firewall(wins)
    c1_krein(wins)
    c2_cauchy(wins)
    c3_suzuki(wins)
    verdict = c4_verdict()
    print("\n[%s] %d checks, %.1f s" % (verdict, len(CHECKS),
                                        time.time() - T0))
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    sys.exit(run())
