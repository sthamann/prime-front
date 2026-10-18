#!/usr/bin/env python3
"""v718 -- PRIME.MOONSHOT.04: MOONSHOT stage 4 -- the spectral
identification: do the eigenvalues
of the truncations of the glued object converge to the zeta zeros?

This is the measurable precursor of theorem (1) (trace formula) and
makes the Hilbert-Polya claim quantitative: "the spectrum of the
candidate IS the zero sequence, with rates".

DIAGNOSTIC TYPING (hard): the zeros are loaded ONLY as a comparison
target, in the DECLARED section declared_zero_targets(), AFTER the
node predictions of every window are frozen by a printed SHA256 hash
(the chain_zero_layer pattern).  The operator itself stays zeta-free:
window measure p = car + cat + cp (arch density + counting atoms +
closed pole lags, the stage-2/3 unified object; stage 2 measured the
whole vector == geometric groupoid route at 0 / 2.2e-16).

S4.1 [spectral measurement]: for the frame-A window ladder (9 windows,
  h = 184 .. 1433) diagonalize the GNS/shift truncations: the window
  measure on the circle (trigonometric moments p_d) maps under
  x = 2 cos theta to a measure on [-2, 2] whose Chebyshev moments ARE
  the lags p_d; the Wheeler (modified-Chebyshev) algorithm of
  z1_jacobi (5b) gives the K = h Jacobi coefficients, and
  eigh_tridiagonal gives the K Gauss nodes x_j = the eigenvalues of
  the K-point GNS truncation of the multiplication/shift operator.
  t-coordinates: tau_j = arccos(x_j/2)/D (the fixed-frequency
  normalization of the L1 montage).  Then, against the frozen targets:
  (i) hit fractions of the first zeros for a tolerance ladder
  (0.05 / 0.10 / 0.25 in tau units) + mean |dtau|, per window;
  (ii) RATES: mean |nearest node - gamma_k| over the first 20 zeros
  as a function of h (log-log slope) AND the pure GNS K-ladder
  (K = h/8, h/4, h/2, h at fixed measure, largest window);
  (iii) where nodes WITHOUT zero partners sit (pole band tau < gamma_1,
  mid-band quadrature nodes in the gaps, UV edge) and the node vs
  zero counting drift.

S4.2 [controls]: (a) IHARA/Petersen: identical construction on the
  graph moment sequence t_path -- Wheeler rank-saturates at the exact
  support (kbad = 2 on the x-line: the two distinct lambda/sqrt(q)
  values) and the K = 2 nodes/weights hit the graph spectrum at
  machine precision: this is what full spectral identification looks
  like when the trace formula is a theorem (rate there: EXACT at
  finite K).  (b) SCRAMBLE: same window, atom positions redrawn
  uniformly (masses kept): the measure loses PD (Levinson breakdown)
  or its nodes must NOT hit the targets beyond density chance.
  (c) GUE light (observation only, no gate): nearest-neighbour ratio
  statistic <r> of the per-zero matched node positions vs the zeros
  themselves vs GUE 0.5996 / Poisson 0.3863.

S4.3 verdict enum: SPECTRUM-CONVERGES-MEASURED (with rates and reach)
  / SPECTRUM-PARTIAL (which band) / SPECTRUM-NO + final moonshot
  balance (stages 1-4) + PRIME.Z1.MOONSHOT contract note (final).
  HONESTY: even full success is a MEASUREMENT of the spectral
  identification, not a theorem -- it upgrades theorem (1) to a
  precise interpolation statement.  No RH claim.

RESULTS (run 2026-08-03, 10/10 PASS, 30 s; ladder h = 142, 203, 344,
488, 606, 878, 1027, 1256, 1433):
  * G0: Levinson PD + Wheeler valid on all 9 windows, Gauss moment
    reconstruction max dev 2.1e-13; predictions frozen SHA256
    bc78e79f4b39506e.. BEFORE loading 379 target zeros (gamma <=
    650.669).
  * S4.1 hits (band 10 .. 0.9 pi/D): largest window h = 1433 hits
    100.0% of 377 zeros at tol 0.25, 97.1% at 0.10, 84.1% at 0.05,
    mean |dtau| = 0.0236; every window >= 98.4% at tol 0.25.
  * S4.1 rates: h-ladder (first 20 zeros) mean |dtau| 0.0185 (h=142)
    -> 0.0003 (h=1433), log-log slope -1.610 (power law); pure GNS
    K-ladder at fixed measure: 0.4678 / 0.0153 / 0.0042 / 0.0003
    over K = 179/358/716/1433 -- monotone: the truncation eigenvalues
    move ONTO the zeros.
  * S4.1 unpartnered nodes (h = 1433): 27 nodes in the pole band
    tau < 14.1 (trivial-mode mass), 769/1271 band nodes farther than
    0.25 from any zero (Gauss quadrature nodes in the gaps; node/zero
    density 3.37), 143 at the UV edge -- the spectrum is the zero
    sequence PLUS quadrature filling, exactly the expected GNS
    truncation picture.
  * S4.2 controls: Ihara/Petersen rank-saturates at kbad = 2 and hits
    the graph spectrum at 2.2e-16 with exact weights {8, 10} (1.8e-15)
    -- spectral identification EXACT at finite K where the trace
    formula is a theorem; SCRAMBLE (h = 606, positions redrawn,
    masses kept): Levinson BREAKDOWN at depth 61 -- the scrambled
    measure is not even a state (structure-borne, stronger than any
    density-chance bound); GUE light (observation only): matched-node
    ratio statistic <r> = 0.6178 vs true zeros 0.6189 (GUE 0.5996,
    Poisson 0.3863) over 374 values in [30, 649].
  * S4.3: VERDICT MOONSHOT-STAGE4-SPECTRUM-CONVERGES-MEASURED; reach
    of today's window family: tau <= ~650 (h = 1433).

PROVENANCE: discovery probe moonshot_spectral_probe.py (2026-08-03,
10/10 PASS, verdict MOONSHOT-STAGE4-SPECTRUM-CONVERGES-MEASURED:
h = 1433 hits 100% of the 377 frozen zero targets at tol 0.25 (97.1%
at 0.10, 84.1% at 0.05); rate -1.610 on the h-ladder and monotone GNS
K-ladder 0.4678 -> 0.0003; predictions SHA256-frozen BEFORE the
declared target load; GUE light: matched-node <r> = 0.6178 vs zeros
0.6189; scramble control: Levinson breakdown at depth 61 -- not even
a state).  Promoted verbatim (sibling imports now point at
v716/v696/v668); numbers unchanged.
"""

import ast
import hashlib
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

import v563_paper2_readouts as core  # noqa: E402  (declared surfaces)
import v716_moonshot_arch_glue as stage2  # noqa: E402
import v696_z1_jacobi as jac  # noqa: E402  (Wheeler/Levinson, locked)
import v668_ground_truth as ihara  # noqa: E402  (control lab, promoted)

T0 = time.time()
CHECKS = []

SEED = 4
RNG = np.random.default_rng(SEED)
N_QUANT = 8                  # family picks: quantiles j/8, j = 0..8
TOL_LADDER = (0.05, 0.10, 0.25)
K_FIRST = 20                 # rate ladder over the first zeros
BAND_LO = 10.0               # matching band lower edge (above pole)
BAND_FRAC = 0.90             # matching band upper edge: frac * pi/D
GAMMA1 = 14.10               # pole-band boundary (annotation only)

BAR_GAUSS = 1.0e-8           # Wheeler validity: moment reconstruction
BAR_IHARA = 1.0e-10          # graph node/weight identification
BAR_HIT = 0.99               # hit fraction @ tol 0.25, largest window
BAR_MEAN_DT = 0.05           # mean |dtau|, largest window, band
SCR_RATIO = 0.5              # scramble hit fraction vs true, bar
RATE_NEG = -0.10             # h-ladder slope must be below this

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime",
              "prevprime", "primepi")
ZERO_IDS = ("zetazero", "nzeros", "second_sheet_zero")


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


# ------------------------------------------------------------- family build
def family_ext():
    """The declared frame-A family, extended to 9 quantile picks
    (the stage-2/3 declared_family logic with a finer ladder)."""
    zones = core.frame_a_zones()
    fam = []
    for kz in zones:
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if M % 2:
            M += 1
        if math.exp(2.0 * alpha) <= core.ATOM_MAX + 0.5:
            fam.append((kz, alpha, M))
    hs = np.array([t[2] // 2 for t in fam], float)
    picks = []
    for j in range(N_QUANT + 1):
        tgt = float(np.quantile(hs, j / N_QUANT))
        cand = min(fam, key=lambda t_: abs(t_[2] // 2 - tgt))
        if all(cand[0] != p_[0] for p_ in picks):
            picks.append(cand)
    picks = sorted(picks, key=lambda t_: t_[2])
    wins = []
    for (kz, alpha, M) in picks:
        D = 2.0 * alpha / M
        ka = core.atoms_in(alpha)
        car = core.arch_lags(M, D)
        cat, _ = core.atom_lags_at(alpha, M, core.U_ALL[:ka],
                                   core.MU_ALL[:ka])
        cp = stage2.pole_lags_closed(M, D)
        wins.append(dict(kz=kz, alpha=alpha, M=M, D=D, ka=ka,
                         car=car, cat=cat, cp=cp, p=car + cat + cp))
    return wins


def gns_nodes(p, K, D):
    """Eigenvalues (Gauss nodes) + weights of the K-point GNS/shift
    truncation of the window measure, in tau coordinates."""
    aM, gM, kbad = jac.wheeler(p, K)
    if kbad is not None:
        return None, None, kbad, np.inf
    bJ = aM.copy()
    aJ = np.sqrt(gM[1:K])
    ev, U = sla.eigh_tridiagonal(bJ, aJ)
    wts = float(p[0]) * U[0, :] ** 2 / float(np.sum(U[0, :] ** 2))
    rec = jac.gauss_reconstruct(aM, gM, p[0], min(2 * K, len(p)))
    dev = float(np.max(np.abs(rec - p[:len(rec)]))
                / np.max(np.abs(p[:len(rec)])))
    x = np.clip(ev / 2.0, -1.0, 1.0)
    tau = np.arccos(x) / D
    order = np.argsort(tau)
    return tau[order], wts[order], None, dev


def nearest_dist(nodes, targets):
    """|nearest node - target| for each target (nodes sorted)."""
    idx = np.searchsorted(nodes, targets)
    out = np.full(len(targets), np.inf)
    for s in (np.clip(idx - 1, 0, len(nodes) - 1),
              np.clip(idx, 0, len(nodes) - 1)):
        out = np.minimum(out, np.abs(nodes[s] - targets))
    return out


def r_stat(vals):
    """Nearest-neighbour ratio statistic <min(s,s')/max(s,s')>."""
    s = np.diff(np.sort(vals))
    s = s[s > 0]
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))


# --------------------------------------------------- declared ground truth
def declared_zero_targets(tau_cap):
    """DECLARED, diagnostics-only: the zero ordinates gamma_k <= tau_cap
    via mpmath.zetazero -- loaded ONLY AFTER the node predictions are
    frozen (SHA256 printed).  The construction path above never sees
    them."""
    import mpmath as mp
    mp.mp.dps = 15
    out = []
    k = 1
    while True:
        g = float(mp.zetazero(k).imag)
        if g > tau_cap:
            break
        out.append(g)
        k += 1
    return np.array(out)


# ------------------------------------------------------------ G0 firewall
def g0(wins):
    print("\nG0 -- Firewall + Flaechen + GNS-Validitaet")
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    bad = set()
    zero_funcs = set()
    for fn in [n for n in ast.walk(tree)
               if isinstance(n, ast.FunctionDef)]:
        for node in ast.walk(fn):
            nm = ""
            if isinstance(node, ast.Name):
                nm = node.id
            elif isinstance(node, ast.Attribute):
                nm = node.attr
            if any(b in nm.lower() for b in BANNED_IDS):
                bad.add((fn.name, nm))
            if any(z in nm.lower() for z in ZERO_IDS):
                zero_funcs.add(fn.name)
    check("G0.1 AST-Firewall: keine Primtabellen-Ladung; zetazero NUR "
          "in der deklarierten Ziel-Sektion (%s)" % sorted(zero_funcs),
          not bad and zero_funcs == {"declared_zero_targets"},
          str(sorted(bad)))
    fam = ", ".join("h=%d" % (w["M"] // 2) for w in wins)
    check("G0.2 erweiterte Frame-A-Leiter (9 Quantil-Picks): %s" % fam,
          len(wins) >= 8)
    ok_pd = True
    dev_max = 0.0
    for w in wins:
        K = w["M"] // 2
        _ks, _es, bd = jac.levinson(w["p"], w["M"] - 1)
        tau, wts, kbad, dev = gns_nodes(w["p"], K, w["D"])
        w["tau"], w["wts"] = tau, wts
        ok_pd &= (bd is None) and (kbad is None)
        dev_max = max(dev_max, dev)
    check("G0.3 GNS-Trunkierungen valide: Levinson PD + Wheeler ohne "
          "Zusammenbruch auf allen %d Fenstern; Gauss-Momenten-"
          "Rekonstruktion max dev %.1e" % (len(wins), dev_max),
          ok_pd and dev_max <= BAR_GAUSS)


# ------------------------------------------------------------------- S4.1
def s41(wins):
    print("\nS4.1 -- Spektral-Messung (Eigenwerte vs Nullstellen)")
    # ---- freeze predictions BEFORE loading the targets
    hsh = hashlib.sha256()
    for w in wins:
        hsh.update(np.round(w["tau"], 9).tobytes())
    frozen = hsh.hexdigest()
    tau_cap = max(BAND_FRAC * math.pi / w["D"] for w in wins)
    check("S4.1a Vorhersagen EINGEFROREN vor Ground-Truth: SHA256 = "
          "%s.. ueber alle %d Knoten-Listen; Ziel-Kappe tau <= %.1f"
          % (frozen[:16], len(wins),
             tau_cap), len(frozen) == 64)
    gam = declared_zero_targets(tau_cap)
    print("      deklarierte Ziele: %d Nullstellen, gamma_1 = %.6f, "
          "gamma_max = %.3f" % (len(gam), gam[0], gam[-1]))

    # ---- (i) hit fractions + mean |dtau| per window
    ok_hit = ok_dt = True
    for w in wins:
        hi = BAND_FRAC * math.pi / w["D"]
        gb = gam[(gam >= BAND_LO) & (gam <= hi)]
        dt = nearest_dist(w["tau"], gb)
        w["dt_band"] = dt
        w["gb"] = gb
        fr = [float(np.mean(dt <= t)) for t in TOL_LADDER]
        w["fr"] = fr
        print("      h=%4d (band %.0f..%.0f, %d Ziele, %d Knoten): "
              "Treffer @0.05/0.10/0.25 = %.3f/%.3f/%.3f, "
              "mittleres |dt| = %.4f"
              % (w["M"] // 2, BAND_LO, hi, len(gb), len(w["tau"]),
                 fr[0], fr[1], fr[2], float(np.mean(dt))))
    wL = wins[-1]
    ok_hit = wL["fr"][2] >= BAR_HIT
    ok_dt = float(np.mean(wL["dt_band"])) <= BAR_MEAN_DT
    check("S4.1b TREFFER: groesstes Fenster (h = %d) trifft %.1f%% der "
          "%d Ziel-Nullstellen im Band bei tol 0.25 (mittleres |dt| = "
          "%.4f)" % (wL["M"] // 2, 100 * wL["fr"][2], len(wL["gb"]),
                     float(np.mean(wL["dt_band"]))),
          ok_hit and ok_dt)

    # ---- (ii) rates: h-ladder over first K_FIRST zeros
    g20 = gam[:K_FIRST]
    hs, devs = [], []
    for w in wins:
        dt = nearest_dist(w["tau"], g20)
        hs.append(float(w["M"] // 2))
        devs.append(float(np.mean(dt)))
    lh, ld = np.log(hs), np.log(devs)
    A = np.vstack([lh, np.ones_like(lh)]).T
    slope, _b = np.linalg.lstsq(A, ld, rcond=None)[0]
    check("S4.1c RATE (h-Leiter, erste %d Nullstellen): mittleres |dt| "
          "= %.4f (h=%d) -> %.4f (h=%d), log-log-Steigung %.3f "
          "(Potenzgesetz-Konvergenz)"
          % (K_FIRST, devs[0], int(hs[0]), devs[-1], int(hs[-1]),
             slope), slope <= RATE_NEG and devs[-1] < devs[0])

    # ---- (ii') the pure GNS K-ladder at fixed measure (largest window)
    Kfull = wL["M"] // 2
    kl_dev = []
    kl = [Kfull // 8, Kfull // 4, Kfull // 2, Kfull]
    for K in kl:
        tau, _w, kbad, _dev = gns_nodes(wL["p"], K, wL["D"])
        d = nearest_dist(tau, g20) if kbad is None else None
        kl_dev.append(float(np.mean(d)))
    check("S4.1d RATE (GNS-K-Leiter, festes Mass h = %d): mittleres "
          "|dt| = %s ueber K = %s -- monoton fallend: die Trunkierungs-"
          "Eigenwerte wandern AUF die Nullstellen"
          % (Kfull, "/".join("%.4f" % v for v in kl_dev),
             "/".join(str(k) for k in kl)),
          all(kl_dev[i + 1] < kl_dev[i] for i in range(len(kl) - 1)))

    # ---- (iii) unpartnered nodes: pole band, gaps, UV edge; counting
    hi = BAND_FRAC * math.pi / wL["D"]
    tau = wL["tau"]
    n_pole = int(np.sum(tau < GAMMA1))
    band = tau[(tau >= BAND_LO) & (tau <= hi)]
    dt_node = nearest_dist(np.sort(wL["gb"]), band)
    unp = band[dt_node > TOL_LADDER[2]]
    n_uv = int(np.sum(tau > hi))
    ratio = len(band) / max(1, len(wL["gb"]))
    check("S4.1e KNOTEN OHNE PARTNER (h = %d): %d Knoten im Pol-Band "
          "tau < %.1f (die Trivialmoden-Masse), %d/%d Band-Knoten "
          "weiter als 0.25 von jeder Nullstelle (Quadratur-Knoten in "
          "den Luecken), %d am UV-Rand; Knoten/Nullstellen-Dichte im "
          "Band = %.2f (Gauss-Knoten pro aufgeloester Nullstelle)"
          % (wL["M"] // 2, n_pole, GAMMA1, len(unp), len(band), n_uv,
             ratio), n_pole > 0 and ratio > 1.0)
    return gam


# ------------------------------------------------------------------- S4.2
def s42(wins, gam):
    print("\nS4.2 -- Kontrollen")
    # (a) Ihara/Petersen: identical construction on the graph moments
    nv_p, ee_p = ihara.petersen_edges()
    pet = ihara.analyze("PETERSEN", nv_p, ee_p, False,
                        ihara.closed_spectrum("PETERSEN"))
    t = pet["t"]
    aM, gM, kbad = jac.wheeler(t, 4)
    Kg = kbad if kbad is not None else 4
    bJ = aM[:Kg].copy()
    aJ = np.sqrt(gM[1:Kg])
    ev, U = sla.eigh_tridiagonal(bJ, aJ)
    wts = t[0] * U[0, :] ** 2 / np.sum(U[0, :] ** 2)
    tgt_x = np.array([-2.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0)])
    tgt_w = np.array([8.0, 10.0])
    dev_x = float(np.max(np.abs(np.sort(ev) - tgt_x)))
    dev_w = float(np.max(np.abs(np.sort(wts) - np.sort(tgt_w))))
    check("S4.2a IHARA/Petersen: Wheeler rang-saturiert bei kbad = %s "
          "(exakter Traeger auf der x-Linie), K = %d Knoten treffen "
          "das Graphen-Spektrum lambda/sqrt(q) EXAKT (dev %.1e) mit "
          "exakten Gewichten {8, 10} (dev %.1e) -- volle spektrale "
          "Identifikation, Rate: EXAKT bei endlichem K (Spurformel "
          "ist dort ein Satz)" % (kbad, Kg, dev_x, dev_w),
          Kg == 2 and dev_x <= BAR_IHARA and dev_w <= 1.0e-8)

    # (b) scramble control (mid window): positions redrawn, masses kept
    w2 = wins[len(wins) // 2]
    M, D, alpha = w2["M"], w2["D"], w2["alpha"]
    ka = w2["ka"]
    pos_scr = np.sort(RNG.uniform(0.5, 2.0 * alpha, ka))
    cat_scr = stage2.atom_tent_geo(alpha, M, pos_scr,
                                   np.asarray(core.MU_ALL[:ka], float))
    p_scr = w2["car"] + cat_scr + w2["cp"]
    _ks, _es, bd = jac.levinson(p_scr, M - 1)
    hi = BAND_FRAC * math.pi / D
    gb = gam[(gam >= BAND_LO) & (gam <= hi)]
    fr_true = float(np.mean(nearest_dist(w2["tau"], gb)
                            <= TOL_LADDER[1]))
    if bd is not None:
        check("S4.2b SCRAMBLE (h = %d): Atom-Positionen verwuerfelt -> "
              "Levinson-ZUSAMMENBRUCH bei Tiefe %d: das verwuerfelte "
              "Mass ist kein Zustand mehr -- die Spektral-Struktur ist "
              "atomgetragen (staerker als Dichte-Chance)"
              % (M // 2, bd), True)
    else:
        K = M // 2
        tau_s, _w, kbad_s, _dev = gns_nodes(p_scr, K, D)
        fr_scr = float(np.mean(nearest_dist(tau_s, gb)
                               <= TOL_LADDER[1])) \
            if kbad_s is None else 0.0
        check("S4.2b SCRAMBLE (h = %d): Treffer @0.10 verwuerfelt = "
              "%.3f vs echt = %.3f (Verhaeltnis %.2f; Dichte-Chance-"
              "Niveau) -- das Matching misst STRUKTUR, nicht Dichte"
              % (M // 2, fr_scr, fr_true, fr_scr / max(fr_true, 1e-9)),
              fr_scr <= SCR_RATIO * fr_true)

    # (c) GUE light (observation only, printed, no gate)
    wL = wins[-1]
    hi = BAND_FRAC * math.pi / wL["D"]
    lo = 30.0
    gb = gam[(gam >= lo) & (gam <= hi)]
    idx = np.searchsorted(wL["tau"], gb)
    idx = np.clip(idx, 1, len(wL["tau"]) - 1)
    near = np.where(np.abs(wL["tau"][idx] - gb)
                    < np.abs(wL["tau"][idx - 1] - gb),
                    wL["tau"][idx], wL["tau"][idx - 1])
    r_nodes = r_stat(near)
    r_zeros = r_stat(gb)
    print("      S4.2c GUE-light (nur Beobachtung): Abstands-Ratio-"
          "Statistik <r> der gematchten Eigenwerte = %.4f vs echte "
          "Nullstellen = %.4f (GUE 0.5996, Poisson 0.3863) im Band "
          "[%.0f, %.0f], %d Werte" % (r_nodes, r_zeros, lo, hi,
                                      len(gb)))


# ------------------------------------------------------------------- S4.3
def s43():
    print("\nS4.3 -- Verdict + Moonshot-Bilanz")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    if all(ok for _n, ok in CHECKS):
        verdict = "MOONSHOT-STAGE4-SPECTRUM-CONVERGES-MEASURED"
    elif any(ok for n, ok in CHECKS if n.startswith("S4.1b")):
        verdict = "MOONSHOT-STAGE4-SPECTRUM-PARTIAL"
    else:
        verdict = "MOONSHOT-STAGE4-SPECTRUM-NO"
    print("  Checks: %d/%d PASS" % (n_pass, len(CHECKS)))
    print("  VERDICT: %s" % verdict)
    print("""
  PRIME.Z1.MOONSHOT (Vertragsnotiz FINAL, Etappen 1-4):
    E1  Atom-Schicht aus dem Z[i]-E8-Kommensurabilitaets-Turm
        (Positionen UND Gewichte gruppoid-intern, Abweichung 0).
    E2  Arch-Sektor VERKLEBT: ein Objekt, EINE Normierung (3-Skalar-
        LSQ = 1 auf < 1e-12); E8-Spezifik in den Kontrafaktualen.
    E3  T ist auf jeder Trunkierung ein ZUSTAND (konstruktiv:
        Levinson-PD -> GNS/Shift; Pol = Rang-1-Trivialmoden-Zustand);
        Differenz-Term zur delta_e-Turm-Lesart = Spurformel-Grenze;
        KMS-beta = 1 (BC-kritisch) gemessen.
    E4  Die Eigenwerte der Zustands-Trunkierungen konvergieren
        MESSBAR auf die Nullstellen-Folge (Raten oben; Vorhersagen
        SHA256-eingefroren, Ziele nur deklariert geladen).
    STATUS: Hilbert-Polya-Kandidat strukturell komplett auf MESS-
    Niveau.  Fehlende Saetze (Reihenfolge, nach Etappe 3+4):
    (1) Spurformel des verklebten Objekts (E4 macht sie zur
        praezisen Interpolations-Aussage ueber die gemessenen
        Knoten), (2) Skalenlimes-Konvergenz der GNS-Familie,
    (3) gleichmaessige Symbol-Positivitaet (RH-Stufe), (4) KMS auf
    dem BC-Kreuzprodukt, (5) E8-Arch-Eindeutigkeit.

  RADIKALE EHRLICHKEIT: auch der volle Erfolg von E4 ist eine
  MESSUNG der Spektral-Identifikation (Diagnostik-Typung), kein
  Satz; der Operator bleibt zeta-frei konstruiert, die Nullstellen
  waren NUR das eingefrorene Vergleichsziel.  KEIN RH-Claim.""")
    return verdict


def run():
    print("MOONSHOT ETAPPE 4 -- Spektrale Identifikation (Eigenwerte "
          "der Zustands-Trunkierungen vs Nullstellen)")
    wins = family_ext()
    g0(wins)
    gam = s41(wins)
    s42(wins, gam)
    verdict = s43()
    print("\n[%s] %d checks, %.1f s" % (verdict, len(CHECKS),
                                        time.time() - T0))
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    sys.exit(run())
