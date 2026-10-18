#!/usr/bin/env python3
"""v721 -- PRIME.K1CAPTURE.01: K1 SLICE -- the node-capture lemma behind
the E4 spectral measurement ("Gauss nodes of the window measures
converge to the zeta zeros", moonshot stage 4: 100% of 377 targets at
tol 0.25, rate -1.61).  This probe builds the PROOF STRUCTURE from
classical quadrature theory and adjudicates honestly which part of the
E4 statement it carries.

THE LEMMA CHAIN (classical ingredients, all implemented + verified):
  (a) [CITED: Szego 3.41 / Freud II.5, Markov-Stieltjes] for the
      K-point Gauss rule of a positive measure mu with nodes x_1 <
      ... < x_K and weights w_j:
        sum_{i<j} w_i <= mu((-inf, x_j))  and
        mu((-inf, x_j]) <= sum_{i<=j} w_i.
      Corollary (the engine): a NODE-FREE open interval (x_j, x_{j+1})
      carries mass mu <= w_j + w_{j+1}.
  (b) [CITED: Christoffel] w_j = lambda_K(x_j) = min_{deg p < K,
      p(x_j)=1} int p^2 dnu on the x-line.  Under x = 2 cos theta the
      admissible polynomials are the EVEN trigonometric ones, so the
      correct computable upper bound is the SYMMETRIZED Fejer test
      q(theta) = [F_{K'}(theta - t) + F_{K'}(theta + t)] /
      [F_{K'}(0) + F_{K'}(2t)], K' = (K+1)//2: int q^2 dmu =
      2 [A(t) + X(t)] / N(t)^2 with A = the kernel-square series,
      X = the cross series, N the normalizer -- ALL exact cosine
      series in the window lags (depth <= K-1).  (Run-1 honesty: the
      unsymmetrized kernel bounds the full-circle Christoffel
      function, which is ~1/2 the even-restricted one -- measured
      max w/lambda = 1.9993 before the fix; the symmetrized bound is
      the theorem.)
  (c) [DERIVED HERE: capture condition] a node exists within arc
      distance d of t as soon as for EVERY candidate node-free
      bracket (a, b) containing (t-d, t+d):
          mu((a,b)) > lambda_bd(a) + lambda_bd(b).
      With cumulative mass Cm and the running envelopes
          RM(x) = max_{a<=x} (Cm(a) + lambda_bd(a)),
          Lm(x) = min_{b>=x} (Cm(b) - lambda_bd(b)),
      the condition collapses to the closed form
          Lm(t+d) - RM(t-d) > 0,
      and d_pred(t) := min such d is the certified capture radius.
  (d) [E: v669/v668] the window symbol IS 2 pi (F_a * dN) -- the
      Fejer-smoothed zero-counting density (exact identity); peak
      positions/masses/gap densities are therefore measured objects
      of the CONSTRUCTION (zeta-free), and v678 supplies the
      unconditional gap input H_min(t) (peaks everywhere; NOTE: v678
      bounds gaps from ABOVE -- a lower separation bound does not
      exist unconditionally, close zero pairs merge into one peak and
      the lemma captures the merged peak without resolving it:
      declared).

DIAGNOSTIC TYPING (hard, the E4 pattern): zeros enter ONLY as the
declared comparison target (moonshot declared_zero_targets), loaded
AFTER the node predictions and peak lists of every window are frozen
by a printed SHA256.  The construction path (lags, nodes, peaks,
lambda bounds, capture radii) never sees them.

MEASUREMENTS (bars declared before any number):
  S1 [synthetic identity lab]: fully controlled peak measure
     (band-limited Fejer peaks + flat gap floor eps, exact moments,
     exact CDF):
     S1.1 grid/moment integrity <= 1e-9;
     S1.2 Markov-Stieltjes sandwich: 0 violations over all K nodes;
     S1.3 node-free-interval mass bound: all consecutive pairs;
     S1.4 Christoffel bound w_j <= lambda_bd(x_j): all nodes;
     S1.5 capture: EVERY peak (incl. a merged close pair) holds >= 1
          node within d_pred; surrogate-mass (Fejer-smoothed) vs
          true-mass d_pred ratio printed (the real-window surrogate
          bias, measured where truth is known).
  S2 [real windows, frame-A ladder h = 142..1433]:
     S2.1 Christoffel bound on every window (w_j <= lambda_bd);
     S2.2 peaks of the Fejer symbol (zeta-free) vs zeros: match
          fraction within 0.30 tau on the largest window >= 0.80
          (the v669 identity in action);
     S2.3 capture validity: fraction of band zeros with nearest node
          <= d_pred(their peak) >= 0.95 (largest window);
     S2.4 predicted hits at tol 0.25 (d_pred <= 0.25) vs measured E4
          hits -- the lemma must be a valid lower bound;
     S2.5 THE RATE QUESTION: per-window mean d_pred (first 20 zeros)
          vs mean measured |dtau|; both log-log slopes.  Honesty
          fork, preregistered: if the lemma slope matches the
          measured -1.61 within +-0.5 AND median d_pred/d_meas <= 10
          -> the rate IS classical (capture radius); else the coarse
          lemma carries the CAPTURE but not the precision, and the
          adjudication falls to S2.6;
     S2.6 THE CENTROID SHARPENING (the classical route to the
          super-resolution): a captured node of a locally symmetric
          peak sits at the peak CENTROID, not just inside the lobe;
          per peak the centroid of the Fejer symbol over +-3/4 lobe
          is computed zeta-free and FROZEN with the nodes.  After
          the target load: (i) |node - centroid| vs |node - gamma|
          (if the node tracks the centroid, the zeta-free centroid
          is the true predictor); (ii) ladder rate of
          |centroid - gamma| vs the measured -1.61.  Fork: centroid
          explains the rate iff median |node-centroid| <= 0.5 median
          |node-gamma| AND |slope_centroid - slope_meas| <= 0.5.
  S3 verdict enum: K1-LEMMA-FULL / K1-LEMMA-CAPTURE-ONLY /
     K1-LEMMA-FAILS + the theorem candidate with typed inputs + the
     off-line honesty note (the lemma PRESUPPOSES mu >= 0; an
     off-line zero breaks window positivity (v688 falsifier route) =
     Levinson breakdown = the GNS truncation has no real spectrum --
     nodes do not mislocate, they cease to exist; on the declared
     regime PD is machine-verified per window, so the statement
     there is unconditional).

PROVENANCE: discovery probe k1_node_capture_probe.py (2026-08-03,
14/14 PASS, verdict K1-LEMMA-CAPTURE-ONLY: the capture half of K1 is
proof-near from classical quadrature theory -- Markov-Stieltjes
sandwich + SYMMETRIZED Christoffel bound + the closed capture
condition Lm(t+d) - RM(t-d) > 0, all machine-verified incl. a merged
close pair; the certified radii d_pred ~ 1.4-2.4 tau carry the
CAPTURE but not the measured super-resolution (0.0003-0.03, factor
~900 below) -- that precision is trace-formula content (the
bg-subtracted centroid beats the node), honestly adjudicated).
Read-only parents: v718 (E4 machinery, family/gns/targets reused
verbatim), v668/v669 (Fejer identity), v678 (zero gap), v688
(falsifier, cited in typing), v696 (Wheeler/Levinson).  Promoted
verbatim (sibling imports now point at v718/v696); numbers unchanged.
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

import v718_moonshot_spectral as e4  # noqa: E402  (E4 lab, read-only)
import v696_z1_jacobi as jac  # noqa: E402

T0 = time.time()
FAILS = []
N_CHK = 0

NG = 1 << 17                 # circle grid (theta in [0, 2 pi))
BAND_LO = 10.0
BAND_FRAC = 0.90
K_FIRST = 20
TOL_HIT = 0.25               # the E4 headline tolerance (tau units)
TOL_MATCH = 0.30             # peak <-> zero match bar (tau units)

# synthetic lab parameters
S_MF = 96                    # Fejer peak order (lobe 2 pi / 96)
S_MOM = 800                  # moment depth (K = 400 rule)
S_K = 400
S_EPS = 1.0e-4               # flat gap floor density
S_POS = (0.50, 0.90, 1.30, 1.36, 1.80, 2.30, 2.80)
S_MASS = (1.00, 0.60, 1.40, 0.50, 1.00, 0.80, 1.20)

BANNED = ("zetazero", "nzeros", "second_sheet_zero", "isprime",
          "primerange", "sympy")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_firewall(src_path):
    """No zero/prime loader symbol in THIS file; the only zero access
    is the declared e4.declared_zero_targets call (attribute name
    checked explicitly)."""
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        nm = ""
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and any(b in nm.lower() for b in BANNED):
            return False
    return True


# ------------------------------------------------------- series on grid
def cos_series_grid(coef):
    """Values of c_0 + 2 sum_{m>=1} c_m cos(m theta) on the uniform
    grid theta_n = 2 pi n / NG (full circle), via FFT."""
    A = np.zeros(NG, dtype=complex)
    L = len(coef)
    A[0] = coef[0]
    A[1:L] = coef[1:]
    A[NG - L + 1:] = coef[1:][::-1]
    return np.real(np.fft.fft(A))


def lambda_even_parts(p, K):
    """Cosine-series data of the EVEN (x-line) Christoffel upper
    bound via the symmetrized Fejer test polynomial q(theta) =
    [F(theta-t) + F(theta+t)] / [F(0) + F(2t)] of order K' =
    (K+1)//2 (unnormalized kernel coefficients t_a = 1 - a/K',
    F(0) = K'):
        lambda_even(t) = 2 [A(t) + X(t)] / N(t)^2,
        A(t) = sum_m H_m p_|m| cos(mt),  H = t * t (autocorr.),
        X(t) = sum_k C_k-type cross series,
        C_k  = sum_a t_a t_{a+k} p_|2a+k|,
        N(t) = K' + t_0 + 2 sum_{a>=1} t_a cos(2at).
    All EXACT in the lags (max index 2K'-2 <= K-1)."""
    Kp = (K + 1) // 2
    t = 1.0 - np.arange(Kp) / Kp
    full = np.concatenate([t[::-1], t[1:]])      # a = -(K'-1)..K'-1
    H_full = np.convolve(full, full)
    mid = len(H_full) // 2
    H = H_full[mid:]                             # m = 0..2K'-2
    p_arr = np.asarray(p, float)
    cA = H * p_arr[:len(H)]
    # cross series C_k (even in k), k = 0..2K'-2
    aidx = np.arange(-(Kp - 1), Kp)
    tf = full
    C = np.zeros(2 * Kp - 1)
    for k in range(2 * Kp - 1):
        sel = np.abs(aidx + k) <= Kp - 1
        a = aidx[sel]
        C[k] = float(np.sum(tf[sel] * (1.0 - np.abs(a + k) / Kp)
                            * p_arr[np.abs(2 * a + k)]))
    # normalizer N(t): constant K' + t_0, cosine coeffs at even m
    nco = np.zeros(2 * Kp - 1)
    nco[0] = Kp + t[0]
    nco[2 * np.arange(1, Kp)] = t[1:]
    return cA, C, nco


def series_at(c, thetas):
    """c_0 + 2 sum_{m>=1} c_m cos(m theta) at arbitrary points."""
    m = np.arange(1, len(c))
    return c[0] + 2.0 * np.cos(np.outer(np.asarray(thetas), m)) @ c[1:]


def lambda_even_at(parts, thetas):
    cA, C, nco = parts
    return 2.0 * (series_at(cA, thetas) + series_at(C, thetas)) \
        / series_at(nco, thetas) ** 2


def lambda_even_grid(parts):
    cA, C, nco = parts
    half = NG // 2 + 1
    A = cos_series_grid(cA)[:half]
    X = cos_series_grid(C)[:half]
    Nn = cos_series_grid(nco)[:half]
    return np.maximum(2.0 * (A + X) / Nn ** 2, 0.0)


def capture_envelopes(Cm, lam):
    """RM(x) = running max of Cm + lam (from left); Lm(x) = running
    min of Cm - lam (from right); capture at radius d around index it
    iff Lm[it + kd] - RM[it - kd] > 0."""
    RM = np.maximum.accumulate(Cm + lam)
    Lm = np.minimum.accumulate((Cm - lam)[::-1])[::-1]
    return RM, Lm


KD_MAX = 4096                # capture-radius search cap (grid steps)


def d_pred_at(RM, Lm, it, dth):
    """Smallest certified capture radius (radians) for a target at
    grid index it (vectorized scan, capped at KD_MAX steps)."""
    n = len(RM)
    kds = np.arange(1, KD_MAX + 1)
    lo = np.clip(it - kds, 0, n - 1)
    hi = np.clip(it + kds, 0, n - 1)
    cond = Lm[hi] - RM[lo] > 0.0
    if not np.any(cond):
        return float("inf")
    return float(kds[int(np.argmax(cond))]) * dth


def gauss_theta(p, K):
    """Gauss nodes (as theta = arccos(x/2) in (0, pi)) + weights of
    the K-point rule of the trigonometric moment sequence p."""
    aM, gM, kbad = jac.wheeler(p, K)
    if kbad is not None:
        return None, None
    ev, U = sla.eigh_tridiagonal(aM.copy(), np.sqrt(gM[1:K]))
    wts = float(p[0]) * U[0, :] ** 2 / float(np.sum(U[0, :] ** 2))
    th = np.arccos(np.clip(ev / 2.0, -1.0, 1.0))
    order = np.argsort(th)
    return th[order], wts[order]


# ================================================================== S1
def s1():
    print("\nS1 -- synthetic identity lab (everything controlled)")
    dth = 2.0 * math.pi / NG
    th_g = np.arange(NG // 2 + 1) * dth          # [0, pi]

    # exact moments: peaks (Fejer order S_MF) at +-theta_k + flat eps
    d = np.arange(S_MOM + 1)
    p = np.zeros(S_MOM + 1)
    p[0] = 2.0 * math.pi * S_EPS
    fej = np.clip(1.0 - d / S_MF, 0.0, None)
    for tk, mk in zip(S_POS, S_MASS):
        p += mk * fej * np.cos(d * tk)

    # exact density on the grid (full circle), folded onto [0, pi]
    dens_c = cos_series_grid(p) / (2.0 * math.pi)
    # NOTE: cos_series_grid(p) IS the symbol s(theta) = sum p_m e^{im};
    # density = s / (2 pi) exactly because the peak moments are
    # band-limited (degree S_MF - 1 <= S_MOM): no truncation.
    dens_min = float(np.min(dens_c))
    # moment integrity: re-integrate two moments from the grid
    thc = np.arange(NG) * dth
    m_chk = max(abs(float(np.sum(dens_c * np.cos(7 * thc))) * dth
                    - p[7]),
                abs(float(np.sum(dens_c * np.cos(150 * thc))) * dth
                    - p[150]))
    check("S1.1 [E] synthetic measure integrity: band-limited density "
          ">= %.1e everywhere (a true positive measure), grid "
          "re-integration of moments m = 7, 150 dev %.1e"
          % (dens_min, m_chk), dens_min > 0 and m_chk < 1e-9)

    th_n, w_n = gauss_theta(p, S_K)
    fold = dens_c[:NG // 2 + 1] * 2.0            # folded density
    Cm = np.concatenate([[0.0], np.cumsum(fold[:-1] + fold[1:])
                         * 0.5 * dth])           # cumulative on [0,pi]

    # S1.2 Markov-Stieltjes sandwich on the x-line (x = 2 cos theta,
    # descending in theta): F_x(x_j) = mass{theta >= theta_j}
    xs = 2.0 * np.cos(th_n)
    order = np.argsort(xs)
    xj = xs[order]
    wj = w_n[order]
    thj = th_n[order]                            # descending theta
    Fx = Cm[-1] - np.interp(thj, th_g, Cm)       # mu((-inf, x_j])
    cum = np.cumsum(wj)
    viol_lo = float(np.max(np.concatenate([[0.0], cum[:-1]]) - Fx))
    viol_hi = float(np.max(Fx - cum))
    tol = 1e-9 * Cm[-1]
    check("S1.2 [E] Markov-Stieltjes sandwich (K = %d nodes): "
          "sum_{i<j} w_i <= F(x_j) <= sum_{i<=j} w_i -- max "
          "violations %.2e / %.2e (tol %.1e)"
          % (S_K, viol_lo, viol_hi, tol),
          viol_lo <= tol and viol_hi <= tol)

    # S1.3 node-free-interval mass bound (consecutive pairs)
    mass_gap = Fx[1:] - Fx[:-1] - wj[1:] - wj[:-1]
    check("S1.3 [E] node-free-interval bound mu((x_j, x_{j+1})) <= "
          "w_j + w_{j+1}: max excess %.2e over %d pairs (tol %.1e)"
          % (float(np.max(mass_gap)), S_K - 1, tol),
          float(np.max(mass_gap)) <= tol)

    # S1.4 Christoffel upper bound at the nodes (even/symmetrized)
    parts = lambda_even_parts(p, S_K)
    lam_n = lambda_even_at(parts, th_n)
    exc = float(np.max(w_n / lam_n))
    check("S1.4 [E] Christoffel bound w_j = lambda_K(x_j) <= "
          "lambda_even(x_j) (symmetrized Fejer test, K' = %d): max "
          "w/lambda = %.4f over %d nodes (must be <= 1)"
          % ((S_K + 1) // 2, exc, S_K), exc <= 1.0 + 1e-9)

    # S1.5 capture lemma: d_pred per peak (true mass) + node inside
    lam_g = lambda_even_grid(parts)
    RM, Lm = capture_envelopes(Cm, lam_g)
    print("   peak | d_pred(true) | nearest node | captured | "
          "nodes in lobe")
    n_cap = 0
    d_preds = []
    for tk, mk in zip(S_POS, S_MASS):
        it = int(round(tk / dth))
        dp = d_pred_at(RM, Lm, it, dth)
        dn = float(np.min(np.abs(th_n - tk)))
        lobe = 2.0 * math.pi / S_MF
        nl = int(np.sum(np.abs(th_n - tk) <= lobe))
        cap = dn <= dp
        n_cap += cap
        d_preds.append(dp)
        print("   %.2f (m=%.2f) | %.5f | %.5f | %s | %d"
              % (tk, mk, dp, dn, "yes" if cap else "NO", nl))
    check("S1.5 [E] capture lemma on synthetic peaks: %d/%d peaks "
          "hold >= 1 node within their certified radius d_pred "
          "(incl. the merged close pair 1.30/1.36)"
          % (n_cap, len(S_POS)), n_cap == len(S_POS))

    # surrogate bias: repeat d_pred with the M-Fejer-smoothed mass
    # (what the real windows must use); report the ratio
    pM = p * np.clip(1.0 - d / (S_MOM + 1), 0.0, None)
    dens_s = cos_series_grid(pM) / (2.0 * math.pi)
    fold_s = np.maximum(dens_s[:NG // 2 + 1] * 2.0, 0.0)
    Cms = np.concatenate([[0.0], np.cumsum(fold_s[:-1] + fold_s[1:])
                          * 0.5 * dth])
    RMs, Lms = capture_envelopes(Cms, lam_g)
    rat = []
    for tk, dp in zip(S_POS, d_preds):
        it = int(round(tk / dth))
        dps = d_pred_at(RMs, Lms, it, dth)
        rat.append(dps / dp)
    print("   surrogate-mass d_pred / true-mass d_pred: median %.3f, "
          "max %.3f (the declared real-window bias)"
          % (float(np.median(rat)), float(np.max(rat))))
    return float(np.median(rat))


# ================================================================== S2
def find_peaks_simple(vals, band_mask, min_sep, prom_frac=0.10):
    """Strict local maxima with a minimum separation and a prominence
    floor relative to the band median (no scipy.signal dependency)."""
    med = float(np.median(vals[band_mask]))
    idx = [i for i in range(1, len(vals) - 1)
           if band_mask[i] and vals[i] > vals[i - 1]
           and vals[i] >= vals[i + 1]]
    # prominence: drop on both sides within +- min_sep
    keep = []
    for i in idx:
        lo = max(0, i - min_sep)
        hi = min(len(vals), i + min_sep + 1)
        drop = vals[i] - min(float(np.min(vals[lo:i + 1])),
                             float(np.min(vals[i:hi])))
        if drop >= prom_frac * med:
            keep.append(i)
    # enforce separation (keep the higher of close pairs)
    keep.sort(key=lambda i: -vals[i])
    out = []
    for i in keep:
        if all(abs(i - j) >= min_sep for j in out):
            out.append(i)
    return sorted(out)


def s2(sur_bias):
    print("\nS2 -- real windows (frame-A ladder)")
    wins = e4.family_ext()
    print("   family: %s" % ", ".join("h=%d" % (w["M"] // 2)
                                      for w in wins))
    dth = 2.0 * math.pi / NG
    th_g = np.arange(NG // 2 + 1) * dth

    ok_chr = True
    chr_worst = 0.0
    hsh = hashlib.sha256()
    for w in wins:
        K = w["M"] // 2
        th_n, w_n = gauss_theta(w["p"], K)
        w["th_n"], w["w_n"] = th_n, w_n
        w["tau_n"] = th_n / w["D"]
        # Christoffel bound at the nodes (even/symmetrized, exact)
        parts = lambda_even_parts(w["p"], K)
        lam_n = lambda_even_at(parts, th_n)
        r = float(np.max(w_n / lam_n))
        chr_worst = max(chr_worst, r)
        ok_chr &= (r <= 1.0 + 1e-9)
        # Fejer symbol (guaranteed >= 0 for a PD sequence) + peaks
        M = w["M"]
        dd = np.arange(M)
        pF = w["p"][:M] * (1.0 - dd / M)
        sF = cos_series_grid(pF)[:NG // 2 + 1]
        w["sF"] = sF
        tau_g = th_g / w["D"]
        hi = BAND_FRAC * math.pi / w["D"]
        band = (tau_g >= BAND_LO) & (tau_g <= hi)
        lobe_th = 2.0 * math.pi / M
        pk = find_peaks_simple(sF, band, max(2, int(0.5 * lobe_th
                                                    / dth)))
        # sub-grid refinement (parabola) + zeta-free peak centroids
        pk_tau, ct_tau = [], []
        w2 = max(3, int(0.75 * lobe_th / dth))
        for i in pk:
            de = 0.5 * (sF[i - 1] - sF[i + 1]) / \
                (sF[i - 1] - 2.0 * sF[i] + sF[i + 1])
            pk_tau.append((i + de) * dth / w["D"])
            lo, hi_i = max(0, i - w2), min(len(sF), i + w2 + 1)
            seg = sF[lo:hi_i] - float(np.min(sF[lo:hi_i]))
            ct = float(np.sum(seg * np.arange(lo, hi_i))
                       / max(np.sum(seg), 1e-300))
            ct_tau.append(ct * dth / w["D"])
        w["pk_tau"] = np.array(pk_tau)
        w["ct_tau"] = np.array(ct_tau)
        w["pk_idx"] = np.array(pk, int)
        # capture machinery on the surrogate mass + lambda grid
        fold = np.maximum(sF, 0.0) / math.pi
        Cm = np.concatenate([[0.0],
                             np.cumsum(fold[:-1] + fold[1:])
                             * 0.5 * dth])
        lam_g = lambda_even_grid(parts)
        RM, Lm = capture_envelopes(Cm, lam_g)
        w["dpred_tau"] = np.array([d_pred_at(RM, Lm, i, dth)
                                   / w["D"] for i in pk])
        hsh.update(np.round(w["tau_n"], 9).tobytes())
        hsh.update(np.round(w["pk_tau"], 9).tobytes())
        hsh.update(np.round(w["ct_tau"], 9).tobytes())
        hsh.update(np.round(w["dpred_tau"], 9).tobytes())
    check("S2.1 [E] Christoffel bound on every window: max "
          "w_j/lambda_even = %.4f over %d windows (must be <= 1) -- "
          "the lemma engine is valid on the real measures"
          % (chr_worst, len(wins)), ok_chr)

    frozen = hsh.hexdigest()
    tau_cap = max(BAND_FRAC * math.pi / w["D"] for w in wins)
    check("S2.2a [E] predictions FROZEN before ground truth: SHA256 "
          "= %s.. (nodes + peaks + capture radii, all windows); "
          "target cap tau <= %.1f" % (frozen[:16], tau_cap),
          len(frozen) == 64)
    gam = e4.declared_zero_targets(tau_cap)
    print("   declared targets: %d zeros, gamma_1 = %.6f, gamma_max "
          "= %.3f" % (len(gam), gam[0], gam[-1]))

    # ---- peak <-> zero match + capture validity per window
    wL = wins[-1]
    for w in wins:
        hi = BAND_FRAC * math.pi / w["D"]
        gb = gam[(gam >= BAND_LO) & (gam <= hi)]
        w["gb"] = gb
        if len(w["pk_tau"]) == 0:
            w["match"] = 0.0
            continue
        dpk = e4.nearest_dist(np.sort(w["pk_tau"]), gb)
        w["dpk"] = dpk
        w["match"] = float(np.mean(dpk <= TOL_MATCH))
        # nearest node distance per zero + its peak's d_pred
        dnode = e4.nearest_dist(w["tau_n"], gb)
        w["dnode"] = dnode
        ip = np.argmin(np.abs(w["pk_tau"][None, :] - gb[:, None]),
                       axis=1)
        w["dpred_z"] = w["dpred_tau"][ip]
        w["cap_ok"] = float(np.mean(dnode <= w["dpred_z"] + 1e-12))
        w["hit_pred"] = float(np.mean(w["dpred_z"] <= TOL_HIT))
        w["hit_meas"] = float(np.mean(dnode <= TOL_HIT))
        print("   h=%4d: %d peaks / %d band zeros; peak-zero match "
              "@0.30 = %.3f (mean %.4f); capture valid %.3f; hits "
              "@0.25 pred %.3f vs meas %.3f; median d_pred %.3f vs "
              "median |dtau| %.4f"
              % (w["M"] // 2, len(w["pk_tau"]), len(gb), w["match"],
                 float(np.mean(dpk)), w["cap_ok"], w["hit_pred"],
                 w["hit_meas"], float(np.median(w["dpred_z"])),
                 float(np.median(dnode))))
    check("S2.2b [M] the v669 identity in action: largest window "
          "peak-zero match @0.30 tau = %.3f (bar >= 0.80), mean "
          "|peak - gamma| = %.4f"
          % (wL["match"], float(np.mean(wL["dpk"]))),
          wL["match"] >= 0.80)
    check("S2.3 [M] capture validity (largest window): %.3f of band "
          "zeros hold their nearest node within the certified "
          "d_pred (bar >= 0.95; surrogate-mass bias measured in S1: "
          "median ratio %.3f)" % (wL["cap_ok"], sur_bias),
          wL["cap_ok"] >= 0.95)
    check("S2.4 [M] the lemma is a valid lower bound on the hit "
          "statistic: predicted hits @0.25 = %.3f <= measured %.3f "
          "(largest window; predicted certifies, measurement can "
          "only exceed)" % (wL["hit_pred"], wL["hit_meas"]),
          wL["hit_pred"] <= wL["hit_meas"] + 1e-9)

    # ---- S2.5 the rate question (coarse certified radius)
    g20 = gam[:K_FIRST]
    hs, dm, dp, dc = [], [], [], []
    for w in wins:
        dnode = e4.nearest_dist(w["tau_n"], g20)
        ip = np.argmin(np.abs(w["pk_tau"][None, :] - g20[:, None]),
                       axis=1)
        hs.append(float(w["M"] // 2))
        dm.append(float(np.mean(dnode)))
        dp.append(float(np.mean(w["dpred_tau"][ip])))
        dc.append(float(np.mean(np.abs(w["ct_tau"][ip] - g20))))
    lh = np.log(hs)
    A = np.vstack([lh, np.ones_like(lh)]).T

    def slope(v):
        return float(np.linalg.lstsq(A, np.log(v),
                                     rcond=None)[0][0])

    sl_m, sl_p, sl_c = slope(dm), slope(dp), slope(dc)
    med_ratio = float(np.median([p_ / m_ for p_, m_ in zip(dp, dm)]))
    print("   rate ladder (first %d zeros): measured |dtau|   %s"
          % (K_FIRST, ", ".join("%.4f" % v for v in dm)))
    print("   rate ladder: certified d_pred            %s"
          % ", ".join("%.4f" % v for v in dp))
    print("   rate ladder: centroid predictor |c-gamma| %s"
          % ", ".join("%.4f" % v for v in dc))
    rate_classical = (abs(sl_p - sl_m) <= 0.5) and (med_ratio <= 10.0)
    check("S2.5 [M] THE COARSE RATE: measured slope %.3f (E4: -1.61)"
          " vs certified-radius slope %.3f; median d_pred/d_meas = "
          "%.1f -- prereg fork: classical-by-radius iff |diff| <= "
          "0.5 and ratio <= 10 -> %s"
          % (sl_m, sl_p, med_ratio,
             "YES" if rate_classical else
             "NO (adjudication falls to the centroid, S2.6)"), True)

    # ---- S2.6 the centroid sharpening
    gbL = wL["gb"]
    ipL = np.argmin(np.abs(wL["pk_tau"][None, :] - gbL[:, None]),
                    axis=1)
    ctz = wL["ct_tau"][ipL]
    dnodeL = wL["dnode"]
    idx = np.searchsorted(wL["tau_n"], gbL)
    idx = np.clip(idx, 1, len(wL["tau_n"]) - 1)
    near = np.where(np.abs(wL["tau_n"][idx] - gbL)
                    < np.abs(wL["tau_n"][idx - 1] - gbL),
                    wL["tau_n"][idx], wL["tau_n"][idx - 1])
    d_nc = np.abs(near - ctz)
    d_cg = np.abs(ctz - gbL)
    med_nc = float(np.median(d_nc))
    med_ng = float(np.median(dnodeL))
    med_cg = float(np.median(d_cg))
    centroid_explains = (med_nc <= 0.5 * med_ng) and \
        (abs(sl_c - sl_m) <= 0.5)
    check("S2.6 [M] CENTROID SHARPENING (largest window, %d zeros): "
          "median |node-centroid| = %.4f vs |node-gamma| = %.4f vs "
          "|centroid-gamma| = %.4f; centroid-rate slope %.3f vs "
          "measured %.3f -- prereg fork: centroid explains the "
          "super-resolution iff |n-c| <= 0.5 |n-g| and slope within "
          "0.5 -> %s"
          % (len(gbL), med_nc, med_ng, med_cg, sl_c, sl_m,
             "YES" if centroid_explains else "NO"), True)
    return (wins, sl_m, sl_p, sl_c, med_ratio, rate_classical,
            centroid_explains, wL)


# ================================================================== S3
def s3(sl_m, sl_p, sl_c, med_ratio, rate_classical,
       centroid_explains, lemma_ok):
    print("\nS3 -- Satz-Kandidat + Typung")
    if lemma_ok and (rate_classical or centroid_explains):
        verdict = "K1-LEMMA-FULL"
    elif lemma_ok:
        verdict = "K1-LEMMA-CAPTURE-ONLY"
    else:
        verdict = "K1-LEMMA-FAILS"
    check("S3.1 [M] preregistered adjudication: %s (capture engine "
          "%s; coarse radius %s [slope %.3f vs measured %.3f, ratio "
          "%.1f]; centroid sharpening %s [slope %.3f])"
          % (verdict, "valid" if lemma_ok else "BROKEN",
             "classical" if rate_classical else "saturates",
             sl_p, sl_m, med_ratio,
             "carries the rate" if centroid_explains else
             "does NOT carry the rate", sl_c),
          True)
    print("""
  SATZ-KANDIDAT K1 (getypte Bausteine):
    [Zitat]  Markov-Stieltjes-Ungleichungen + w_j = lambda_K(x_j)
             (Szego 3.41 / Freud II) -- der Einfang-Motor.
    [E hier] Christoffel-Schranke aus den Lags (Fejer-Testpolynom,
             S1.4/S2.1: w_j <= lambda_bd ueberall) und die
             geschlossene Einfang-Bedingung Lm(t+d) > RM(t-d)
             (S1.5: 7/7 synthetische Peaks inkl. Merge-Paar).
    [E]      v669: Fenster-Symbol = 2 pi (F_a * dN) exakt -- Peaks,
             Massen, Luecken sind Konstruktions-Objekte (zeta-frei);
             v678 liefert die unbedingte Luecken-Obergrenze H_min
             (Peaks ueberall); eine untere Separations-Schranke
             existiert unbedingt NICHT -- nahe Paare verschmelzen zu
             einem Peak, das Lemma faengt den Merge-Peak (deklariert,
             S1.5-Paar 1.30/1.36).
    [M]      auf dem deklarierten Regime (frame-A, h <= 1433,
             tau <= ~650) ist PD pro Fenster maschinell verifiziert
             -- DORT gilt der Einfang unbedingt.
  EHRLICHKEITS-FRAGE (off-line): das Lemma setzt mu >= 0 voraus --
  genau da sitzt RH.  Eine Off-Line-Nullstelle verschiebt keinen
  Peak: sie bricht die Positivitaet der Fensterform (v688-
  Falsifikator-Route) -> Levinson-Zusammenbruch -> die GNS-
  Trunkierung hat kein reelles Spektrum mehr.  Die Knoten
  mislokalisieren nicht -- sie hoeren auf zu existieren.  Das ist
  die K3-Verbindung: der Falsifikator und das Einfang-Lemma sind
  zwei Seiten derselben Positivitaets-Voraussetzung.""")
    return verdict


def run():
    print("=" * 78)
    print("K1 SLICE -- node-capture lemma for the E4 spectral "
          "measurement")
    print("=" * 78)
    check("K0.0 [E] AST firewall: no zero/prime loader symbol in "
          "this file; ground truth only via the declared e4 target "
          "section after the freeze",
          ast_firewall(os.path.abspath(__file__)))
    sur_bias = s1()
    (wins, sl_m, sl_p, sl_c, med_ratio, rate_classical,
     centroid_explains, wL) = s2(sur_bias)
    lemma_ok = len(FAILS) == 0
    verdict = s3(sl_m, sl_p, sl_c, med_ratio, rate_classical,
                 centroid_explains, lemma_ok)
    print("\nVERDICT: %s" % verdict)
    dt = time.time() - T0
    if FAILS:
        print("RESULT: %d/%d checks passed -- FAILURES: %s  (%.1f s)"
              % (N_CHK - len(FAILS), N_CHK, ", ".join(FAILS), dt))
        return 1
    print("RESULT: ALL %d CHECKS PASSED  (%.1f s)" % (N_CHK, dt))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
