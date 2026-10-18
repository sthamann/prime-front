#!/usr/bin/env python3
"""MOONSHOT ETAPPE 3 -- the positivity STRUCTURE of the glued object:
is the Weil functional a STATE on the groupoid algebra?

Question (Hilbert-Polya form of theorem (5), the RH level): a trace
functional coming from a genuine unitary representation (vector/KMS
state) is automatically positive on f * f~.  This probe does NOT try
to prove positivity (that would be RH); it TYPES the structure on
truncations: which representation the state would come from, what is
measurable, and where exactly the gap sits.

Surfaces used (declared):
  * the 5-window family of L1/5b (v563 build == v643 W1 Weil-measure
    reference), the deployed odd window form B = odd_toeplitz(car+cat)
    with H^1_0 Galerkin metric Gm;
  * the v701 KEYSTONE decomposition B = odd_toeplitz(p) + P,
    p = c + pole_lags, P = -odd_toeplitz(pole_lags) rank-1 PSD;
  * the stage-1/2 groupoid comb (gaussian sieve + sigma-quotient +
    log generator; NO prime table in the construction path);
  * the v668 ground-truth labs verbatim: ihara_ground_truth_probe
    (Ramanujan graphs: T MUST be a state there) and
    epstein_firewall_probe (x^2+5y^2, h=2: T must NOT be a state).

E3.1 [convolution positivity, exactly posed]: on the test algebra
  (odd piecewise-linear window functions Phi_V on the half-integer
  lattice, v643 P1(b); f~ = conj(f(-.))), the Weil functional is
      T(f * f~) = int int f(v) f(w) K(v - w),
  K = the unified Weil kernel of stage 2 (2cosh pole - rho arch -
  atom comb; tent reads == deployed lags at 2.2e-16).  EXACT binding
  identity verified on a battery (window vectors + random f + the
  generalized minimizer):
      T(f*f~) = u^T Toeplitz(c) u = 2 V^T odd_toeplitz(c) V
  with u the odd extension of V -- the discrete convolution algebra
  evaluation EQUALS the deployed W1 window form (the keystone v701
  consistency, bound here at the quadratic-form level).  Plus the
  measured PD margins (the W3 numbers): lambda_min(B) plain and
  generalized (B, Gm) per window.

E3.2a [the natural representation]: (i) CONSTRUCTIVE STATE: Levinson
  on the unified moment vector p (all reflection coefficients |k| < 1
  == Toeplitz(p) PD) exhibits T as the vector state <e0, . e0> of the
  GNS/CMV shift representation of the truncated translation flow --
  the SAME flow whose scaling limit is the L1 continuum operator
  (rates measured in L1/M2).  Fejer symbol >= 0 (state side) vs RAW
  symbol sigma_p (may dip negative: the finite-truncation correction
  profile -- location + size reported).  (ii) THE TOWER delta_e
  COMPARISON: the naive regular-representation vector state of the
  finite tower + trivial mode,
      phi_reg(V) = phi_pole(V) + phi_orb(V),
      phi_pole = 2 K_D e^{-(M-1)D/2} (a_+ . u)^2   (closed rank-1
        pole square == the keystone P, the 'Trivialmoden' state),
      phi_orb  = sum_k mu_k Phi_V(log k)^2         (orbit-diagonal,
        beta = 1/2 GNS amplitudes, geo comb),
  does NOT equal T: the difference Delta = T - phi_pole - phi_orb =
  (arch flow term, NSD on the odd sector) + (atom orbit interference
  minus diagonal) is measured: sign profile, size relative to the
  W3 margin, structure (the trace-formula boundary = the RH
  substance).

E3.2b [KMS variant]: the degree grading as time evolution
  (Bost-Connes).  Measured Gibbs structure of the unified kernel:
  ONE global half-density e^{-u/2} across all three sectors --
      rho(u) e^{u/2} (1 - e^{-2u}) == 1        (flow partition),
      2cosh(u/2) e^{u/2} == e^u + 1            (boundary characters),
      mu_n sqrt(n) == 2 Lambda_geo(n)          (orbit counting),
  i.e. counting side M(u) = W(u) e^{u/2}; evenness of W (the
  functional equation) == detailed balance M(-u) = e^{-u} M(u):
  KMS-beta = 1, the BC critical temperature; the s = 1/2 axis is the
  symmetric GNS splitting.  Sharpness: the half-density exponent is
  MEASURED (-1/2 exact; -1/4 and -1 misfit reported).  The full KMS
  condition needs the noncommutative BC crossed product -- typed as a
  missing theorem, no claim.

E3.3 [controls]: IHARA lab (Petersen, Ramanujan): trace formula
  EXACT (integer path counts == spectral side), Toeplitz forms PSD at
  every depth, the representation EXISTS (finite unitary) -- this is
  what outcome (i) looks like when the trace formula is a theorem;
  Levinson rank-saturates at the support size F (states with margins
  -> 0, the v668 recalibration).  Violator prism C16 x K2 breaks at
  K* = 15.  EPSTEIN side (x^2+5y^2, disc -20, h = 2): genus identity
  exact, Lambda_E has negative sites (first n = 36: the orbit measure
  itself is NOT positive -- no Gibbs state candidate), and the
  identical window machinery gives lambda_min << -floor and Levinson
  BREAKDOWN: T is NOT a state there.  The construction measures
  something.

E3.4 verdict enum: STATE-ON-TRUNCATIONS / STATE-PLUS-CORRECTION /
  NOT-A-STATE, + PRIME.Z1.MOONSHOT.03 contract note + the final
  ordered list of missing theorems.  RADICAL HONESTY: no RH claim in
  any outcome; outcome (i) only moves the quantifier into the limit.

RESULTS (run 2026-08-03, 21/21 PASS; family h = 184, 344, 606, 1027,
1433 with X = 256 .. 262144):
  * E3.1: binding identity max rel dev 1.0e-12 over 80 battery
    vectors x 5 windows (two float summation orders); keystone
    B = odd(p) + P at 2.8e-16, P rank 1 PSD (lam2/lam1 2.9e-11),
    closed pole square == P-form at 1.5e-10; W3 margins
    lambda_min(B, Gm) = 2.679e-2 .. 1.516e-3 > 0 on all 5 windows
    (plain 4.04e-4 .. 6.60e-6), Levinson PD full depth (max |k| =
    0.2376, min headroom 1-|k| = 0.76).
  * E3.2a: Fejer symbol min +1.39e-2 .. >= 0 on all 5 windows (the
    state side); RAW sigma_p dips NEGATIVE on every window (mins
    -4.39 .. -11.57 at tau* = 48.8 .. 221.1, window-dependent,
    band-localized in the zero-ordinate band; PD holds anyway);
    tower delta_e comparison (windows h = 184/344/606, geo comb
    X = 29929): sector additivity exact (1.6e-11), phi_pole,
    phi_orb >= 0 on 48/48, arch origin cell car[0] = 2.7763 > 0
    carries the positive Pf/delta_0 mass; Delta has MIXED sign on
    the battery (negative on 3/48 = exactly the three generalized
    minimizers) and at the minimizer the conspiracy carries:
    T = 5.36e-2/1.31e-2/6.81e-3 vs Delta = -2.79/-4.58/-5.32,
    |Delta|/T = 52/350/781, |Delta|/margin = 104/699/1563 -- the
    delta_e-regular reading does NOT give T; the GNS/shift state
    gives T exactly.
  * E3.2b: Gibbs identities at 2.2e-16 / 5.7e-14 / 1.8e-15;
    half-density exponent -1/2 measured (residual 8.9e-16; -1/4
    misfit 2.577, -1 misfit 5.153); detailed balance M(-u) =
    e^{-u} M(u) at 1.1e-16 (KMS-beta = 1 = BC critical).
  * E3.3: Ihara/Petersen trace formula rel dev 2.7e-9 over m <= 39
    (integer counts to ~7e6), kstar = None, PSD all K = 2..40,
    support F = 4, Levinson rank-saturates at depth 4 (|k| -> 1:
    finite unitary rep); prism violator kstar = 15.  Epstein
    (N = 3721): genus identity exact, Lambda_E has 67 negative
    sites (first n = 36), window form lambda_min = -1.05e+3 /
    -4.08e+3 vs floor ~4e-12 (~14 orders), Levinson BREAKDOWN at
    depth 49/62 -- NOT a state.  Both controls calibrate.
  * E3.4: VERDICT MOONSHOT-STAGE3-STATE-ON-TRUNCATIONS.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper claim, no RH statement.  Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/moonshot_state_probe.py
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

import v563_paper2_readouts as core  # noqa: E402  (declared surfaces)
import moonshot_arch_glue_probe as stage2  # noqa: E402
import ihara_ground_truth_probe as ihara  # noqa: E402  (control lab)
import epstein_firewall_probe as eps  # noqa: E402  (control lab)

T0 = time.time()
CHECKS = []

EPS = float(np.finfo(float).eps)
FLOOR_SAFETY = 20.0
N_RAND = 12                 # random battery vectors per window
SEED = 3
N_THETA = 20000             # symbol grid on (0, pi)
E32A_WINS = 3               # tower comparison on the 3 smallest windows

BAR_BIND = 1.0e-10          # extension identity: two float summation
                            # orders at M = 2866  (calib 1.0e-12)
BAR_KEY = 1.0e-10           # keystone matrix identity    (calib 3.6e-14)
BAR_RANK1 = 1.0e-10         # P rank-1: lam2/lam1         (calib 2.7e-19)
BAR_POLSQ = 1.0e-9          # closed pole square vs P     (calib 2.7e-13)
BAR_FEJ = -1.0e-9           # Fejer symbol floor
BAR_GIBBS = 1.0e-12         # Gibbs sector identities     (calib 2.2e-16)
BAR_BETA = 1.0e-10          # half-density residual       (calib 8.9e-16)
BETA_MISFIT = 1.0           # wrong-exponent misfit floor
BAR_ATOMBIND = 1.0e-12      # deployed atoms vs counting side
BAR_EF = 1.0e-6             # Ihara explicit formula (integer)
LEV_HEADROOM = 1.0e-3       # zeta Levinson: min(1 - |k|) floor
EPSTEIN_FACTOR = 1.0e3      # |lambda_min| must exceed floor by this

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "zetas", "nzeros")

RNG = np.random.default_rng(SEED)


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""))
    return bool(ok)


# ------------------------------------------------------------ small helpers
def odd_extend(V, M):
    """Full odd lattice vector u (length M) from the free half V
    (length h = M/2): u_j = V_j (j < h), u_{M-1-j} = -V_j."""
    u = np.zeros(M)
    h = M // 2
    u[:h] = V
    u[h:] = -V[::-1]
    return u


def toep_quad(c, u):
    """u^T Toeplitz(c) u via the autocorrelation (discrete convolution
    algebra route): sum_m r_m c_{|m|}."""
    M = len(u)
    r = np.correlate(u, u, "full")          # lags -(M-1) .. (M-1)
    idx = np.abs(np.arange(-(M - 1), M))
    return float(np.dot(r, np.asarray(c)[idx]))


def levinson(p):
    """Levinson-Durbin on the moment vector p (p[0] > 0).  Returns
    (ks, ok_pd, depth): ok_pd iff all |k| < 1 with positive prediction
    error through full depth; depth = first failure index (or len)."""
    r = np.asarray(p, float) / float(p[0])
    M = len(r)
    a = np.zeros(M)
    a[0] = 1.0
    e = 1.0
    ks = []
    for m in range(1, M):
        acc = r[m] + float(np.dot(a[1:m], r[m - 1:0:-1]))
        k = -acc / e
        ks.append(k)
        if not (abs(k) < 1.0) or e <= 0.0:
            return np.array(ks), False, m
        a_new = a.copy()
        a_new[1:m + 1] += k * a[:m][::-1]
        a = a_new
        e *= (1.0 - k * k)
    return np.array(ks), True, M


def symbol_scan(p, fejer):
    """min over theta in (0, pi) of the (raw | Fejer) window symbol."""
    p = np.asarray(p, float)
    M = len(p)
    th = np.linspace(1.0e-4, math.pi - 1.0e-4, N_THETA)
    w = np.ones(M)
    if fejer:
        w = 1.0 - np.arange(M) / M
    vals = (p[0] * w[0]
            + 2.0 * np.cos(np.outer(th, np.arange(1, M))) @ (p[1:] * w[1:]))
    i = int(np.argmin(vals))
    return float(vals[i]), float(th[i])


def interp_odd(u, M, D, pts):
    """Phi_V(t) = sum_j u_j tent((t - q_j)/D), q_j = (j-(M-1)/2) D."""
    pts = np.asarray(pts, float)
    idx = pts / D + 0.5 * (M - 1)
    i0 = np.floor(idx).astype(int)
    fr = idx - i0
    out = np.zeros_like(pts)
    ok0 = (i0 >= 0) & (i0 <= M - 1)
    out[ok0] += u[i0[ok0]] * (1.0 - fr[ok0])
    ok1 = (i0 + 1 >= 0) & (i0 + 1 <= M - 1)
    out[ok1] += u[i0[ok1] + 1] * fr[ok1]
    return out


def pole_square_closed(V, M, D):
    """The closed rank-1 pole square on the odd sector:
    cp_d = K_D 2cosh(dD/2), K_D = (4/D)(2cosh(D/2) - 2), and with the
    odd extension u:  -u^T Toep(cp) u = 2 K_D e^{-(M-1)D/2} (a+ . u)^2."""
    u = odd_extend(V, M)
    K = (4.0 / D) * (2.0 * math.cosh(0.5 * D) - 2.0)
    ap = np.exp(0.5 * D * np.arange(M))
    A = float(ap @ u)
    return 2.0 * K * math.exp(-0.5 * (M - 1) * D) * A * A


# ------------------------------------------------------------- G0 firewall
def g0_firewall(wins):
    print("\nG0 -- Firewall + deklarierte Flaechen")
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
    check("G0.1 AST-Firewall: keine Primtabellen-/Zeta-Ladung im eigenen "
          "Konstruktionspfad (Kontroll-Labore ihara/epstein deklariert, "
          "Runde-10-Flaechen unberuehrt)", not hits, str(hits))

    fam = ", ".join("h=%d (X=%.0f)" % (w["M"] // 2,
                                       math.exp(2.0 * w["alpha"]))
                    for w in wins)
    check("G0.2 deklarierte 5-Fenster-Familie reproduziert: %s" % fam,
          len(wins) == 5 and all(w["M"] % 2 == 0 for w in wins))

    # stage-2 glue spot-check: own quadrature/closed lags vs deployed
    w0 = wins[0]
    dev_ar = max(abs(stage2.tent_read(stage2.rho, d, w0["D"])
                     + w0["car"][d]) / abs(w0["car"][d])
                 for d in (5, 50, w0["M"] // 2))
    cp0 = stage2.pole_lags_closed(w0["M"], w0["D"])
    K = (4.0 / w0["D"]) * (2.0 * math.cosh(0.5 * w0["D"]) - 2.0)
    dev_cp = float(np.max(np.abs(
        cp0 - K * 2.0 * np.cosh(0.5 * w0["D"] * np.arange(w0["M"])))
        / np.max(np.abs(cp0))))
    check("G0.3 Stage-2-Verklebung (Stichprobe): eigene rho-Quadratur == "
          "deployte Arch-Lags (%.1e), Pol-Lags == K_D 2cosh(dD/2) "
          "geschlossen (%.1e)" % (dev_ar, dev_cp),
          dev_ar <= 1.0e-10 and dev_cp <= 1.0e-9)


# ------------------------------------------------------------------- E3.1
def e31(wins):
    print("\nE3.1 -- Faltungs-Positivitaet, exakt gestellt "
          "(Bindung an die W1-Form)")
    dev_bind = 0.0
    n_batt = 0
    for w in wins:
        M, h = w["M"], w["M"] // 2
        c = w["car"] + w["cat"]
        B = core.odd_toeplitz(c, M)
        w["B"] = B
        g = np.zeros(M)
        g[0], g[1] = 2.0 * w["D"] / 3.0, w["D"] / 6.0
        w["Gm"] = core.odd_toeplitz(g, M)
        batt = [np.eye(h)[j] for j in (0, h // 2, h - 1)]
        batt += list(RNG.standard_normal((N_RAND, h)))
        lmg, vmin, _rad = eps.gen_min_eig2(B, w["Gm"])
        w["lmin_gen"], w["vmin"] = lmg, vmin
        batt.append(vmin)
        w["batt"] = batt
        for V in batt:
            u = odd_extend(V, M)
            t_conv = toep_quad(c, u)          # convolution-algebra route
            t_form = 2.0 * float(V @ (B @ V))  # deployed W1 window form
            dev_bind = max(dev_bind, abs(t_conv - t_form)
                           / max(1.0, abs(t_form)))
            n_batt += 1
    check("E3.1a KONSISTENZ-IDENTITAET: T(f*f~) via diskreter Faltungs-"
          "Algebra (Autokorrelation x unifizierte Lags) == deployte "
          "W1-Fensterform 2 V^T B V, %d Batterie-Vektoren x 5 Fenster"
          % n_batt, dev_bind <= BAR_BIND, "max rel dev %.1e" % dev_bind)

    # keystone v701: B = odd(p) + P, P rank-1 PSD; closed pole square
    dev_key = dev_r1 = dev_sq = 0.0
    lam_ratio = 0.0
    for w in wins:
        M = w["M"]
        p = w["car"] + w["cat"] + w["cp"]
        w["p"] = p
        P = -core.odd_toeplitz(w["cp"], M)
        rec = core.odd_toeplitz(p, M) + P
        dev_key = max(dev_key, float(np.max(np.abs(rec - w["B"]))
                                     / np.max(np.abs(w["B"]))))
        ev = np.linalg.eigvalsh(P)
        lam_ratio = max(lam_ratio, abs(ev[-2]) / ev[-1])
        dev_r1 = max(dev_r1, -min(0.0, ev[0]) / ev[-1])
        for V in w["batt"][:4]:
            q1 = 2.0 * float(V @ (P @ V))
            q2 = pole_square_closed(V, M, w["D"])
            dev_sq = max(dev_sq, abs(q1 - q2) / max(1.0, abs(q1)))
    check("E3.1b KEYSTONE (v701): B == odd_toeplitz(p) + P exakt (dev "
          "%.1e); P = -odd(pole) ist Rang-1 PSD (lam2/lam1 %.1e)"
          % (dev_key, lam_ratio),
          dev_key <= BAR_KEY and lam_ratio <= BAR_RANK1
          and dev_r1 <= BAR_RANK1)
    check("E3.1c Pol-Quadrat GESCHLOSSEN: P-Form == 2 K_D e^{-(M-1)D/2} "
          "(a+ . u)^2 -- der Trivialmoden-Sektor ist ein Rang-1-"
          "VEKTORZUSTAND in geschlossener Form", dev_sq <= BAR_POLSQ,
          "max rel dev %.1e" % dev_sq)

    # measured PD margins (the W3 numbers)
    ok_pd = True
    rows = []
    for w in wins:
        lp = float(np.linalg.eigvalsh(w["B"])[0])
        w["lmin_plain"] = lp
        floor = FLOOR_SAFETY * EPS * (w["M"] // 2) \
            * float(np.max(np.abs(w["car"] + w["cat"])))
        ok_pd &= (lp > floor) and (w["lmin_gen"] > 0.0)
        rows.append("h=%d: %.3e/%.3e" % (w["M"] // 2, lp, w["lmin_gen"]))
    check("E3.1d PD GEMESSEN (W3-Margen, plain/generalisiert): %s"
          % ", ".join(rows), ok_pd)

    # Levinson positive-feasibility on p (full depth)
    ok_lev = True
    head = 1.0
    kmax = 0.0
    for w in wins:
        ks, ok, depth = levinson(w["p"])
        ok_lev &= ok
        if len(ks):
            kmax = max(kmax, float(np.max(np.abs(ks))))
            head = min(head, float(np.min(1.0 - np.abs(ks))))
        w["lev_ok"] = ok
        w["lev_depth"] = depth
    check("E3.1e Levinson auf p in VOLLER Tiefe PD auf allen 5 Fenstern "
          "(max |k| = %.4f, min Headroom 1-|k| = %.1e)" % (kmax, head),
          ok_lev and head >= LEV_HEADROOM)
    return dev_bind


# ------------------------------------------------------------------ E3.2a
def e32a(wins, comb):
    print("\nE3.2a -- die natuerliche Darstellung (Kern)")
    # (i) constructive GNS/CMV state + symbol profile
    ok_fej = True
    rows = []
    for w in wins:
        mn_f, _th_f = symbol_scan(w["p"], fejer=True)
        mn_r, th_r = symbol_scan(w["p"], fejer=False)
        w["sym"] = (mn_f, mn_r, th_r)
        ok_fej &= mn_f >= BAR_FEJ
        rows.append("h=%d: Fejer %.3e, raw %.3e @ tau %.2f"
                    % (w["M"] // 2, mn_f, mn_r, th_r / w["D"]))
    check("E3.2a-1 KONSTRUKTIVER ZUSTAND: Levinson-PD (E3.1e) + Fejer-"
          "Symbol >= 0 auf allen Fenstern -- T ist Vektorzustand "
          "<e0,.e0> der GNS/Shift-Darstellung des trunkierten Flusses "
          "(Skalen-Limes = L1-Operator)", ok_fej,
          "; ".join(rows[:2]) + " ...")
    neg_raw = all(w["sym"][1] < 0.0 for w in wins)
    taus = [w["sym"][2] / w["D"] for w in wins]
    check("E3.2a-2 ROHES Symbol sigma_p dippt NEGATIV auf jedem Fenster "
          "(tau* = %.1f .. %.1f, fensterabhaengig im Nullstellen-"
          "Ordinaten-Band) -- die Trunkierungs-Korrektur ist BAND-"
          "LOKALISIERT, PD haelt trotzdem (Fejer >= 0): Struktur des "
          "Differenz-Terms, spektral gelesen"
          % (min(taus), max(taus)), neg_raw,
          "raw mins: " + ", ".join("%.2f" % w["sym"][1] for w in wins))

    # (ii) tower delta_e comparison on the smallest windows
    us = np.array(sorted(comb))
    mu = np.array([2.0 * comb[int(n)] / math.sqrt(float(n)) for n in us])
    lg = np.log(us.astype(float))
    stats = []
    n_neg = n_tot = 0
    ok_struct = True
    dev_split = 0.0
    far_lo, far_hi = 0.0, 0.0
    ok_min = True
    for w in wins[:E32A_WINS]:
        M, D = w["M"], w["D"]
        reach = math.exp(2.0 * w["alpha"])
        sel = us <= reach + 0.5
        half = 0.5 * (M - 1) * D + D
        seli = sel & (lg <= half)
        rows_w = []
        for V in w["batt"]:
            nrm = math.sqrt(float(V @ (w["Gm"] @ V)))
            Vn = V / nrm
            u = odd_extend(Vn, M)
            T = 2.0 * float(Vn @ (w["B"] @ Vn))
            ppole = pole_square_closed(Vn, M, D)
            phi = interp_odd(u, M, D, lg[seli])
            porb = float(np.dot(mu[seli], phi * phi))
            t_ar = toep_quad(w["car"], u)
            t_at = toep_quad(w["cat"], u)
            # exact split identities: geometric sectors + keystone
            dev_split = max(
                dev_split,
                abs(T - (t_ar + t_at)) / max(1.0, abs(T)),
                abs(T - (toep_quad(w["p"], u) + ppole))
                / max(1.0, abs(T)))
            # arch far part (origin Pf/delta_0 cell separated)
            far = t_ar - w["car"][0] * float(u @ u)
            far_lo, far_hi = min(far_lo, far), max(far_hi, far)
            delta = T - ppole - porb
            ok_struct &= (ppole >= -1.0e-15) and (porb >= -1.0e-15)
            n_tot += 1
            n_neg += int(delta < 0.0)
            rows_w.append((T, ppole, porb, delta, t_ar, t_at))
        w["cmp"] = rows_w
        Tm, pp, po, dl, ta, tt = rows_w[-1]     # generalized minimizer
        ok_min &= (dl < 0.0) and (abs(dl) / Tm >= 10.0)
        stats.append("h=%d @min: T=%.3e, phi_pole=%.3f, phi_orb=%.3f, "
                     "Delta=%.3f (|Delta|/T=%.0f, /Marge=%.0f)"
                     % (M // 2, Tm, pp, po, dl, abs(dl) / Tm,
                        abs(dl) / w["lmin_gen"]))
    check("E3.2a-3 STRUKTUR der delta_e-Zerlegung: exakte Sektor-"
          "Additivitaet T = T_ar + T_at = odd(p)-Form + phi_pole (max "
          "dev %.1e); phi_pole, phi_orb >= 0 auf allen %d Batterie-"
          "Vektoren; Arch-Ursprungszelle car[0] = %.4f > 0 traegt die "
          "positive Pf/delta_0-Masse (Ferm-Anteil in [%.2f, %.2f])"
          % (dev_split, n_tot, wins[0]["car"][0], far_lo, far_hi),
          dev_split <= BAR_BIND and ok_struct)
    check("E3.2a-4 DIFFERENZ-TERM (die RH-Substanz): der naive "
          "delta_e-Turm-Zustand liefert T NICHT -- Delta = T - "
          "phi_pole - phi_orb hat GEMISCHTES Vorzeichen auf der "
          "Batterie (Delta < 0 auf %d/%d) und am generalisierten "
          "Minimierer traegt die Konspiration: %s"
          % (n_neg, n_tot, " | ".join(stats)), ok_min)
    print("      Typ: Delta = (Arch-Fluss-Spur inkl. Pf/delta_0-"
          "Ursprungsblock) + (Orbit-INTERFERENZ - Diagonale) -- exakt "
          "der Rand der fehlenden Spurformel; der delta_e-Vektorzustand "
          "der Turm-Darstellung liefert T NICHT; der GNS/Shift-Zustand "
          "liefert T EXAKT (E3.2a-1).")


# ------------------------------------------------------------------ E3.2b
def e32b(wins, comb):
    print("\nE3.2b -- KMS-Variante (Bost-Connes-Graduierung)")
    tg = np.linspace(0.25, 6.0, 231)
    d1 = float(np.max(np.abs(stage2.rho(tg) * np.exp(0.5 * tg)
                             * (1.0 - np.exp(-2.0 * tg)) - 1.0)))
    d2 = float(np.max(np.abs(stage2.pole_density(tg) * np.exp(0.5 * tg)
                             - (np.exp(tg) + 1.0))))
    check("E3.2b-1 GIBBS-FAKTORISIERUNG, kontinuierliche Sektoren: "
          "rho(u) e^{u/2} (1-e^{-2u}) == 1 (dev %.1e) und "
          "2cosh(u/2) e^{u/2} == e^u + 1 (dev %.1e) -- EINE globale "
          "Halbdichte e^{-u/2}" % (d1, d2),
          d1 <= BAR_GIBBS and d2 <= BAR_GIBBS)

    reach2 = math.exp(2.0 * wins[E32A_WINS - 1]["alpha"])
    ka = core.atoms_in(wins[E32A_WINS - 1]["alpha"])
    nn = np.round(np.exp(np.asarray(core.U_ALL[:ka]))).astype(int)
    dev_at = max(abs(float(core.MU_ALL[k]) * math.sqrt(float(n)) / 2.0
                     - comb[int(n)]) for k, n in enumerate(nn))
    check("E3.2b-2 GIBBS-FAKTORISIERUNG, Atom-Sektor: mu_n sqrt(n)/2 == "
          "Lambda_geo(n) (Orbit-Zaehlseite, %d Atome bis X = %.0f)"
          % (ka, reach2), dev_at <= BAR_ATOMBIND, "max dev %.1e" % dev_at)

    lgn = np.log(nn.astype(float))
    y = np.log(np.asarray(core.MU_ALL[:ka], float) / 2.0) \
        - np.log(np.array([comb[int(n)] for n in nn]))
    mis = {}
    for s in (-0.5, -0.25, -1.0):
        mis[s] = float(np.max(np.abs(y - s * lgn)))
    check("E3.2b-3 SCHAERFE der inversen Temperatur: Halbdichte-Exponent "
          "GEMESSEN -1/2 (Residuum %.1e); Fehlanpassung bei -1/4: %.3f, "
          "bei -1: %.3f -- beta = 1/2 in Laengeneinheiten ist Messwert, "
          "nicht Setzung" % (mis[-0.5], mis[-0.25], mis[-1.0]),
          mis[-0.5] <= BAR_BETA and mis[-0.25] >= BETA_MISFIT
          and mis[-1.0] >= BETA_MISFIT)

    u0 = math.log(2.0)
    m_p = 2.0 * comb[2] / math.sqrt(2.0) * math.exp(0.5 * u0)
    m_m = 2.0 * comb[2] / math.sqrt(2.0) * math.exp(-0.5 * u0)
    db = abs(m_m - math.exp(-u0) * m_p)
    check("E3.2b-4 KMS-SPIEGELUNG: W gerade (Funktionalgleichung, "
          "deployte Spiegel-Konvention) == detaillierte Balance "
          "M(-u) = e^{-u} M(u) der Zaehlseite M = W e^{u/2}: "
          "KMS-beta = 1 (BC-kritisch), s = 1/2-Achse = symmetrische "
          "GNS-Aufspaltung (Instanz u = log 2, dev %.1e)" % db,
          db <= 1.0e-14)
    print("      Typ: volle KMS-Bedingung braucht das nichtkommutative "
          "BC-Kreuzprodukt (Zeitentwicklung sigma_t(u_n) = n^{it} u_n) "
          "-- fehlender Satz, hier nur die Gibbs-Struktur gemessen.")


# ------------------------------------------------------------------- E3.3
def e33(wins):
    print("\nE3.3 -- Kontrollen (Ihara MUSS Zustand sein, Epstein DARF "
          "keiner sein)")
    # ---- Ihara lab (v668 conventions, verbatim import)
    nv_p, ee_p = ihara.petersen_edges()
    pet = ihara.analyze("PETERSEN", nv_p, ee_p, False,
                        ihara.closed_spectrum("PETERSEN"))
    ok_psd = all(r["lmin"] >= -r["floor"] for r in pet["rows"])
    rel_ef = pet["dev_ef"] / float(np.max(pet["N_path"]))
    check("E3.3a IHARA/Petersen: Spurformel EXAKT (Pfad- == Spektral-"
          "Seite, rel dev %.1e ueber m <= 39, Zaehlungen bis %d), "
          "Toeplitz-Formen PSD fuer alle K = 2..40 (kstar = %s), "
          "Traeger F = %d"
          % (rel_ef, int(np.max(pet["N_path"])), pet["kstar"],
             pet["F"]),
          rel_ef <= BAR_EF and pet["kstar"] is None and ok_psd)
    ks, ok, depth = levinson(pet["t"])
    check("E3.3b IHARA/Petersen: Levinson RANG-SATURIERT bei Tiefe %d "
          "(F = %d, |k|->1, e->0): der Zustand kommt aus der ENDLICHEN "
          "unitaeren Darstellung des Graphen -- so sieht Ausgang (i) "
          "aus, wenn die Spurformel ein SATZ ist (Margen -> 0 ist das "
          "erwartete Profil echter Positivitaet, v668)"
          % (depth, pet["F"]),
          (not ok) and pet["F"] <= depth <= pet["F"] + 2)
    nv_r, ee_r = ihara.prism_edges(16)
    pri = ihara.analyze("PRISM16", nv_r, ee_r, True,
                        ihara.closed_spectrum("PRISM", 16))
    check("E3.3c IHARA/Violator (Prisma C16 x K2, nicht-Ramanujan): "
          "Fensterform bricht bei K* = %s -- das Labor detektiert "
          "'RH falsch'" % pri["kstar"], pri["kstar"] is not None)

    # ---- Epstein side (x^2 + 5y^2, disc -20, h = 2)
    picks = wins[:2]
    N_E = int(math.exp(2.0 * picks[-1]["alpha"]) + 0.5)
    chi4, chi5, chi20 = eps.chi_arrays(N_E)
    b = (eps.divisor_transform(chi20, N_E)
         + eps.convolution_45(chi4, chi5, N_E))
    r1 = eps.lattice_r1(N_E)
    # genus identity (v668 B-block): r_Q1(n) = sum_{d|n} chi_-20(d)
    #                                 + (chi_-4 * chi_5)(n), exact ints
    genus_ok = int(np.max(np.abs(r1[1:] - b[1:]))) == 0
    aE = np.zeros(N_E + 1)
    aE[1:] = r1[1:].astype(float) / float(r1[1])
    lam_E = eps.dirichlet_vonmangoldt(aE, N_E)
    neg = np.where(lam_E < -1.0e-9)[0]
    check("E3.3d EPSTEIN: Genus-Identitaet r_Q1 vs zeta L_-20 + L_-4 L_5 "
          "koeffizientenweise exakt bis %d; Lambda_E hat %d NEGATIVE "
          "Stellen (erste: n = %d) -- das Orbit-Mass selbst ist NICHT "
          "positiv: kein Gibbs-Zustands-Kandidat"
          % (N_E, len(neg), int(neg[0]) if len(neg) else -1),
          genus_ok and len(neg) > 0 and (len(neg) == 0 or neg[0] == 36))
    ok_break = True
    rows = []
    for w in picks:
        reach = math.exp(2.0 * w["alpha"])
        idx = np.where(np.abs(lam_E[:int(reach) + 1]) > 1.0e-9)[0]
        pos = np.log(idx.astype(float))
        ms = 2.0 * lam_E[idx] / np.sqrt(idx.astype(float))
        A_E, Gm_E, cat_E = eps.window_form(w["alpha"], w["M"], pos, ms,
                                           w["car"])
        lmE, _v, _rad = eps.gen_min_eig2(A_E, Gm_E)
        floor = FLOOR_SAFETY * EPS * (w["M"] // 2) \
            * float(np.max(np.abs(w["car"] + cat_E)))
        p_E = w["car"] + cat_E + w["cp"]
        _ks, okE, depthE = levinson(p_E)
        ok_break &= (lmE < -EPSTEIN_FACTOR * floor) and (not okE)
        rows.append("h=%d: lambda_min = %.3e (floor %.1e), Levinson-"
                    "BRUCH bei Tiefe %d" % (w["M"] // 2, lmE, floor,
                                            depthE))
        zrow = "h=%d zeta-Zwilling: lambda_min = %.3e > 0, Levinson " \
               "voll PD" % (w["M"] // 2, w["lmin_gen"])
        rows.append(zrow)
    check("E3.3e EPSTEIN: identische Fenster-Maschinerie -- KEIN Zustand "
          "auf denselben Trunkierungen (%s) -- die Konstruktion misst "
          "etwas" % " | ".join(rows), ok_break)


# ------------------------------------------------------------------- E3.4
def e34():
    print("\nE3.4 -- Verdict + Vertragsnotiz + fehlende Saetze")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if all(ok for _n, ok in CHECKS):
        verdict = "MOONSHOT-STAGE3-STATE-ON-TRUNCATIONS"
    elif any(ok for n, ok in CHECKS if n.startswith("E3.1d")):
        verdict = "MOONSHOT-STAGE3-STATE-PLUS-CORRECTION"
    else:
        verdict = "MOONSHOT-STAGE3-NOT-A-STATE"
    print("  Checks: %d/%d PASS" % (n_pass, n_tot))
    print("  VERDICT: %s" % verdict)
    print("""
  PRIME.Z1.MOONSHOT.03 (Vertragsnotiz-Update, Etappe 3):
    T ist auf JEDER Trunkierung des verklebten Objekts ein Zustand --
    konstruktiv (Levinson-PD auf p => GNS/Shift-Darstellung des
    trunkierten Flusses, Zyklenvektor e0; Pol = geschlossener Rang-1-
    Trivialmoden-Vektorzustand).  Positivitaet dort AUTOMATISCH; die
    RH-Frage ist damit die KONVERGENZ dieser Zustands-Familie im
    L1-Skalenlimes (Quantor im Limes -- KEIN RH-Claim).  Der naive
    delta_e-Vektorzustand der Turm-Darstellung liefert T NICHT: der
    Differenz-Term Delta (Arch-Fluss-Spur inkl. positiver Pf/delta_0-
    Ursprungsmasse + Orbit-Interferenz minus Diagonale) ist die
    exakte Spurformel-Grenze; am Minimierer |Delta|/T = 52..781,
    |Delta|/W3-Marge = 104..1563 -- die Konspiration ist die
    RH-Substanz.  KMS:
    beta = 1-detaillierte-Balance (BC-kritisch) gemessen, s = 1/2 =
    symmetrische GNS-Aufspaltung; volle KMS braucht das BC-
    Kreuzprodukt.  Kontrollen kalibrieren beide Ausgaenge.

  FEHLENDE SAETZE nach Etappe 3 (Reihenfolge):
    (1) SPURFORMEL fuer das verklebte Gruppoid-Objekt (geometrische
        == spektrale Seite; im Ihara-Labor exakt, hier offen) --
        verschiebt Delta auf die Spektralseite.
    (2) SKALENLIMES-KONVERGENZ der GNS-Zustandsfamilie (Mosco/Norm-
        Resolvente des CMV/Jacobi-Turms; L1-Raten N^-2 gemessen) --
        der Quantor von Ausgang (i).
    (3) GLEICHMAESSIGE Symbol-Positivitaet sigma_p >= 0 (v701-
        Kompression) == Grenzwert-Positivitaet == RH-Stufe; auf
        Trunkierungen nur Fejer >= 0 (gemessen), roh band-negativ.
    (4) KMS-CHARAKTERISIERUNG auf dem BC-Kreuzprodukt (beta = 1
        detaillierte Balance gemessen; modulare Theorie fehlt).
    (5) E8-ARCH-EINDEUTIGKEIT (welcher unimodulare Traeger verklebt;
        Stage-2-Kontrafaktuale gemessen, Eindeutigkeits-Satz fehlt).

  RADIKALE EHRLICHKEIT: kein RH-Claim in keinem Ausgang; auch
  STATE-ON-TRUNCATIONS verschiebt nur den Quantor in den Limes.""")
    return verdict


def run():
    print("MOONSHOT ETAPPE 3 -- Positivitaets-Struktur des verklebten "
          "Objekts (Zustands-Typung)")
    wins = stage2.declared_family()
    g0_firewall(wins)
    e31(wins)
    x_geo = int(math.exp(2.0 * wins[E32A_WINS - 1]["alpha"]) + 0.5)
    comb, _meta = stage2.geo_comb(x_geo)
    e32a(wins, comb)
    e32b(wins, comb)
    e33(wins)
    verdict = e34()
    print("\n[%s] %d checks, %.1f s" % (verdict, len(CHECKS),
                                        time.time() - T0))
    return 0 if all(ok for _n, ok in CHECKS) else 1


if __name__ == "__main__":
    sys.exit(run())
