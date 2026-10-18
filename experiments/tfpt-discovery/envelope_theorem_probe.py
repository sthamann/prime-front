"""SECTOR.ENVELOPETHEOREM.01 -- (A) the h^{-3/2} envelope of rho =
tau/tau_pnt attacked as a derivation from certified objects, and
(B) the angle-native capture sandwich (EXPLORATION ONLY).

PARENTS (2026-08-06): sector_floor_attack_probe (FLOOR-MECHANISM-
PARTIAL: onem = F(r) eps exact; capture tau/lambda_min(A_h) median
1.53) and floor_ingredients_probe (CAPTURE-BOUNDED / INGREDIENT-II-
THEOREM-SHAPE / AMPLIFIER-MECHANISM: envelope L1 rho h^{3/2} in
[4.85, 24.2] slope +0.14; the amplifier accumulates at the LOW-u end,
u_half/2a falling 0.12 -> 0.05; the I1 test-vector bound loose
through E).  NO RH claim -- the deliverable is the derivation
skeleton or the exact breaking factor.

PART A -- THE ENVELOPE (frozen candidate chain):
 A1 SCALE ACCOUNTING: tau_pnt (the density model, atom-free) is
    evaluated on the REAL ladder and on a SYNTHETIC extension ladder
    (frames from the fitted h(alpha) relation, SYN_ALPHAS = 7.0,
    7.5, 8.0, 8.5, 9.0 -- the density block needs no atoms); fits
    tau_pnt ~ C h^-a (gate R^2 >= FIT_R2 = 0.90).  SYMBOLIC STATUS
    typed honestly: the deployed arch integrals + spline weights
    have no closed form in the house convention -- the asymptotic
    leg is NUMERIC; the symbolic derivation is typed OPEN with that
    exact obstruction named.
 A2 THE CANDIDATE SCALE CARRIERS (frozen):
    (i) THE LOW-u ATOM MASS x PROJECTION GEOMETRY (the dissection
        winner): m_low = sum_{u_n <= u*} Lambda(n)/sqrt(n) with the
        FROZEN convention u* = U_FRAC 2 alpha, U_FRAC = 0.15 (the
        per-window u_half from the fluctuation path is REPORTED as
        the secondary convention; U_FRAC_WRONG = 0.50 is the
        wrong-convention control).  CHEBYSHEV LEG (unconditional):
        m_low >= psi(x*)/sqrt(x*) >= c_psi sqrt(x*) for x* = e^{u*}
        >= T0 with frozen (c_psi, T0) = (0.7, 8), psi(t) >= 0.7 t
        verified DIRECTLY on the atom table over the full reachable
        range (classical Chebyshev cited beyond); below T0 the
        explicit finite sum.  THE COMPOSITE (the mechanism test):
            tau_k = c_k * q_low_k,   q_low = sum_{u<=u*} m_n phi_n,
        phi_n = u2^T Xhat_n u2 (the projection geometry; u2 = the
        bottom eigenvector of the density block) -- i.e. tau =
        (explicit mass) x (measured angle/read factor phi_bar =
        q_low/m_low) x c.  STABILITY GATE: q_low > 0 on every rung,
        max/min c_k <= C_STAB_RATIO = 10, |log-log slope of c_k vs
        h| <= C_STAB_SLOPE = 0.30.
    (ii) THE PACKET FLOOR (v791, CITED -- not rebuilt): min sector
        weight +2.0e-7 (X=4) -> +8.3e-9 (X=10), cited log-slope
        -0.53/alpha-unit; tracking iff |slope(log tau vs alpha) -
        (-0.53)| <= TRACK_TOL = 0.15.
    (iii) THE RAM-ODD CHANNEL MASS: q_odd = sum_{n odd} m_n phi_n
        (deployed-frame version); tracking iff |slope log(tau/q_odd)
        vs log h| <= 0.30.
 A3 EXPONENT BOOKKEEPING + PER-FACTOR TYPING: each factor typed
    (unconditional / measured-structural / open); if the composite
    fails, the exact breaking factor named.

PART B -- THE CAPTURE TIGHTENING (frozen construction): work in the
 parity plane V (QR-orthonormalized) with the TWO bottom modes u1,
 u2 of the full window form (lambda_1 <= lambda_2):
   *  LOWER: tau >= lambda_1 (Cauchy interlacing, exact).
   *  UPPER, angle-native: the certificate vector v* = V c*, c* =
      top eigenvector of O O^T with O = V^T [u1 u2] (the 2x2 overlap
      matrix) -- v* is built PURELY from the angle data; the bound
      tau <= v*^T A v* is exact; its decomposition v*^T A v* =
      lambda_1 a^2 + lambda_2 b^2 + J* names the residual coupling
      J* (no global E).  SANDWICH GATE: max (v*^T A v*)/lambda_1 <=
      CUP_BAR = 10 and max J*/lambda_1 <= JSTAR_BAR = 10 -->
      CAPTURE-SANDWICHED; else CAPTURE-STILL-LOOSE (census printed:
      cos overlaps of u1 AND u2, the junk weight delta_min = 1 -
      lambda_max(O O^T), lambda_2/lambda_1).

CONTROLS (frozen): C1 scramble breaks the atom-mass composite (the
 low-u mass/geometry is comb content): the scrambled c-census
 violates the stability gate; C2 Epstein: the Chebyshev factor must
 differ measurably (median |m_low_E/m_low - 1| >= EPS_MASS_DIFF =
 0.20, mass-matched totals); C3 the wrong u* convention (0.50)
 must break the composite stability (typed as it falls).

VERDICT (frozen): ENVELOPE-THREE-FACTOR (A1 fit + Chebyshev leg +
 composite stable + C1, C2 fire; the open factor stated exactly) /
 ENVELOPE-PARTIAL / ENVELOPE-OPEN; plus CAPTURE-SANDWICHED /
 CAPTURE-STILL-LOOSE.  Updated reduced floor statement printed
 (report only).

FIREWALL: v563 READ-ONLY; mpmath zeta VALUES only (the v583
constant); no zeta zero read (AST-checked); RNG only in v563's
declared scramble; nothing outside experiments/ touched.  NO RH
claim.

DECLARED IMPLEMENTATION CORRECTIONS (run 1 -> run 2, 2026-08-06; no
numeric bar or candidate changed):
  (1) stab_of spec fix: run 1 typed the SCRAMBLED composite census
      'stable' with c in [-0.993, -0.696] -- a NEGATIVE constant,
      i.e. scrambled tau < 0.  A positive-lower-bound skeleton with
      c <= 0 is a break BY DEFINITION (the frozen text says 'tau >=
      mass x angle x explicit constant'); the stability reading now
      additionally requires min c > 0.  This is a spec-encoding fix,
      not a bar change; with it C1 fires exactly as the frozen
      control demanded.
  (2) report-only additions: the synthetic-only tau_pnt fit (the
      controlled single-family experiment vs the zone-scattered real
      ladder) and the TRUE-minimizer residual J_min/lambda_1 census
      in Part B (names exactly what any angle-native upper bound
      must reproduce).
  Run-1 numbers carried: composite c drifts h^-2.27 ratio 962 (the
  breaking factor = the constant: q_low is a tau_pnt-scale object,
  ~1e3 above tau -- no additive low-u sub-mass carries the tau
  scale); B upper leg explodes to 1.4e6 lambda_1 through cos_u2 ~
  0.5; A2.ii/iii non-tracking; C2 fires 0.52; C3 breaks via q_low
  sign flip.
"""
import ast
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
from mpmath import mp, zeta, diff as mpdiff  # noqa: E402 (VALUES only)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
FIT_R2 = 0.90
U_FRAC = 0.15
U_FRAC_WRONG = 0.50
C_PSI, T0_CHEB = 0.7, 8.0
C_STAB_RATIO = 10.0
C_STAB_SLOPE = 0.30
TRACK_TOL = 0.15
PACKET_SLOPE_CITED = -0.53    # v791 min sector weight, per alpha-unit
CUP_BAR = 10.0
JSTAR_BAR = 10.0
EPS_MASS_DIFF = 0.20
FLAT_TOL = 0.30
STRIDE = 5
SCR_SEED = 1
GRID_PER_D = 4.0
ANOMALOUS_H = 1292
SYN_ALPHAS = [7.0, 7.5, 8.0, 8.5, 9.0]

mp.dps = 30
C_TH = float(-2 * mpdiff(lambda s: zeta(s), 0.5) / zeta(0.5))
U0 = 2.0 * math.log(-C_TH / 4.0)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in ("zetazero", "nzeros", "find_zeros"):
                return False
    return True


def ols_loglog(x, y):
    lx, ly = np.log(np.asarray(x, float)), np.log(np.abs(np.asarray(y)))
    b, q = np.polyfit(lx, ly, 1)
    pred = b * lx + q
    r2 = 1.0 - float(((ly - pred) ** 2).sum()) \
        / max(float(((ly - ly.mean()) ** 2).sum()), 1e-300)
    return float(b), float(math.exp(q)), r2


def eig2(M):
    a, b, c = M[0, 0], M[0, 1], M[1, 1]
    if max(abs(a), abs(b), abs(c)) == 0.0:
        return 0.0, 0.0, np.array([1.0, 0.0]), np.array([0.0, 1.0])
    mid, R = 0.5 * (a + c), math.hypot(0.5 * (a - c), b)
    l1, l2 = mid + R, mid - R
    if abs(b) < 1e-300 * max(abs(a), abs(c), 1e-300):
        v1 = np.array([1.0, 0.0]) if a >= c else np.array([0.0, 1.0])
    else:
        v1 = np.array([b, l1 - a])
        v1 /= np.linalg.norm(v1)
    if v1[0] < 0:
        v1 = -v1
    return l1, l2, v1, np.array([-v1[1], v1[0]])


def xmat(row3):
    return np.array([[row3[0], row3[2]], [row3[2], row3[1]]])


def pnt_cells_frame(alpha, Mz, D, W11, W22, W12, umax):
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((umax - U0) / delta))
    edges = U0 + delta * np.arange(n_cells + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    reads = np.empty((n_cells, 3))
    for j, u_j in enumerate(centers):
        reads[j, 0] = core.spline_project(W11, u_j, D, Mz)
        reads[j, 1] = core.spline_project(W22, u_j, D, Mz)
        reads[j, 2] = core.spline_project(W12, u_j, D, Mz)
    return edges, reads


def pnt_S_of(edges, reads, ulim):
    hi = np.minimum(edges[1:], ulim)
    lo = np.minimum(edges[:-1], ulim)
    m = 2.0 * (np.exp(hi / 2.0) - np.exp(lo / 2.0))
    s = m @ reads
    return np.array([[s[0], s[2]], [s[2], s[1]]])


def density_lock(alpha, Mz):
    """The atom-free density lock block on an arbitrary frame."""
    D = 2.0 * alpha / Mz
    hz = Mz // 2
    c_ar = np.asarray(core.arch_lags(Mz, D), float)
    Tb = core.parity_basis(hz, 2)
    t1, t2 = Tb[0].copy(), Tb[1].copy()
    W11 = core.lag_weights_from_v(t1, hz)
    W22 = core.lag_weights_from_v(t2, hz)
    Wpp = core.lag_weights_from_v(t1 + t2, hz)
    W12 = 0.5 * (Wpp - W11 - W22)
    B = np.array([[float(c_ar @ W11), float(c_ar @ W12)],
                  [float(c_ar @ W12), float(c_ar @ W22)]])
    edges, reads = pnt_cells_frame(alpha, Mz, D, W11, W22, W12,
                                   2.0 * alpha + 1e-9)
    Sp = pnt_S_of(edges, reads, 2.0 * alpha)
    return B - Sp


def full_A(rr, uu=None, mm=None):
    uu = rr["uu"] if uu is None else uu
    mm = 2.0 * rr["lam"] if mm is None else mm
    c_at, _ = core.atom_lags_at(rr["alpha"], rr["M"], uu, mm)
    c_ar = np.asarray(core.arch_lags(rr["M"], rr["D"]), float)
    return core.odd_toeplitz(c_ar + c_at, rr["M"])


def epstein_atoms(alpha):
    Nmax = int(math.floor(math.exp(2.0 * alpha)))
    cnt = np.zeros(Nmax + 1)
    for x in range(0, int(math.isqrt(Nmax)) + 1):
        rem = Nmax - x * x
        if rem < 0:
            break
        y = np.arange(0, int(math.isqrt(rem // 5)) + 1)
        n = x * x + 5 * y * y
        mult = (2.0 if x > 0 else 1.0) * np.where(y > 0, 2.0, 1.0)
        np.add.at(cnt, n, mult)
    nn = np.nonzero(cnt[2:])[0] + 2
    return np.log(nn.astype(float)), cnt[nn] / np.sqrt(nn.astype(float))


def composite_census(win_list, u_frac, scrambled=False):
    """The frozen composite: per window (q_low, m_low, c = tau/q_low)
    with u* = u_frac * 2 alpha; scrambled=True re-reads positions."""
    out = []
    for w in win_list:
        rr = w["rr"]
        if scrambled:
            rr_s = core.build_window(w["kz"], scramble_seed=SCR_SEED)
            uu, lamv, Xn = rr_s["uu"], rr_s["lam"], rr_s["Xn"]
            l1s, tau_s, _, _ = eig2(rr_s["Ah"])
            tau_w = tau_s
        else:
            uu, lamv, Xn = rr["uu"], rr["lam"], rr["Xn"]
            tau_w = w["tau"]
        u2 = w["u2"]
        ustar = u_frac * 2.0 * w["alpha"]
        msk = uu <= ustar
        phi = np.array([float(u2 @ (xmat(x) @ u2)) for x in Xn[msk]])
        m_low = float(np.sum(2.0 * lamv[msk]))
        q_low = float(np.sum(lamv[msk] * phi))
        out.append(dict(h=w["h"], alpha=w["alpha"], m_low=m_low,
                        q_low=q_low, tau=tau_w,
                        c=(tau_w / q_low) if q_low != 0 else float("nan")))
    return out


def stab_of(cens):
    """The frozen stability reading of a composite census."""
    qs = [c["q_low"] for c in cens]
    if min(qs) <= 0:
        return False, "q_low <= 0 on %d rungs (sign breaks)" % sum(
            1 for q in qs if q <= 0), None, None
    cc = [c["c"] for c in cens]
    if min(cc) <= 0:
        return False, ("c <= 0 on %d rungs (a positive lower-bound "
                       "skeleton is broken by definition; declared "
                       "correction (1))"
                       % sum(1 for c in cc if c <= 0)), None, None
    ratio = max(cc) / min(cc)
    sl, _, r2 = ols_loglog([c["h"] for c in cens], cc)
    ok = ratio <= C_STAB_RATIO and abs(sl) <= C_STAB_SLOPE
    return ok, ("c in [%.3g, %.3g] ratio %.2f, trend h^%.2f (R^2 %.2f)"
                % (min(cc), max(cc), ratio, sl, r2)), ratio, sl


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("SECTOR.ENVELOPETHEOREM.01 -- envelope derivation + capture "
          "sandwich (envelope_theorem_probe)")
    print("=" * 78)

    print("\nS0 -- firewall + ladder")
    check("S0.AST no zeta-zero loader; mpmath = the v583 constant "
          "-2 zeta'/zeta(1/2) = %.4f only" % C_TH,
          ast_zero_firewall(__file__))

    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        l1v, l2v, v1, v2 = eig2(rr["Ah"])
        rows.append(dict(rr=rr, kz=kz, h=rr["h"], alpha=rr["alpha"],
                         lam=l1v, tau=l2v))
    rows.sort(key=lambda w: w["alpha"])
    aas = [w["alpha"] for w in rows]
    hs = [w["h"] for w in rows]
    check("S0.SET %d regular complete windows, alpha %.3f..%.3f, h "
          "%d..%d" % (len(rows), aas[0], aas[-1], min(hs), max(hs)),
          len(rows) >= 30)

    # ============================================================== A1
    print("\nA1 -- the tau_pnt scale accounting")
    for w in rows:
        rr = w["rr"]
        edges, reads = pnt_cells_frame(
            rr["alpha"], rr["M"], rr["D"], rr["W11"], rr["W22"],
            rr["W12"], 2.0 * rr["alpha"] + 1e-9)
        Sp = pnt_S_of(edges, reads, 2.0 * rr["alpha"])
        Mp = rr["B"] - Sp
        l1p, tau_p, v1p, u2 = eig2(Mp)
        w.update(tau_pnt=tau_p, u2=u2, S_pnt=Sp)
    a_fit, C_fit, r2_fit = ols_loglog(hs, [w["tau_pnt"] for w in rows])
    bh, ch = np.polyfit(aas, np.log(hs), 1)
    syn = []
    for a_s in SYN_ALPHAS:
        h_s = int(round(math.exp(bh * a_s + ch)))
        Mz = 2 * h_s
        Mng = density_lock(a_s, Mz)
        _, tau_s, _, _ = eig2(Mng)
        syn.append((a_s, h_s, tau_s))
        print("    synthetic frame alpha = %.1f, h = %5d: tau_pnt = "
              "%.4e" % (a_s, h_s, tau_s))
    all_h = hs + [s[1] for s in syn]
    all_t = [w["tau_pnt"] for w in rows] + [s[2] for s in syn]
    a_ext, C_ext, r2_ext = ols_loglog(all_h, all_t)
    a_syn, C_syn, r2_syn = ols_loglog([s[1] for s in syn],
                                      [s[2] for s in syn])
    print("    synthetic-only fit (controlled single-family "
          "experiment): tau_pnt ~ %.3g h^-%.3f (R^2 %.4f) -- the "
          "zone scatter of the real ladder is what breaks the "
          "global fit" % (C_syn, -a_syn, r2_syn))
    check("A1.1 tau_pnt ~ C h^-a on the real ladder: a = %.3f, C = "
          "%.3g (R^2 %.3f >= %.2f); WITH the synthetic extension to "
          "h = %d: a = %.3f, C = %.3g (R^2 %.3f) -- the density-"
          "model transversal has a stable numeric asymptotic"
          % (-a_fit, C_fit, r2_fit, FIT_R2, max(all_h), -a_ext, C_ext,
             r2_ext),
          r2_fit >= FIT_R2 and r2_ext >= FIT_R2)
    print("    SYMBOLIC STATUS (typed): OPEN -- the deployed arch "
          "integrals (arch_A near/far branches) and the T163/T170 "
          "spline lag weights have no closed form in the house "
          "convention; the asymptotic leg is NUMERIC.  Envelope "
          "target restated: rho >= c h^-3/2 <=> tau >= c C h^-(a + "
          "3/2) = c %.3g h^-%.2f (measured tau ~ h^%.2f)"
          % (C_ext, -a_ext + 1.5, ols_loglog(hs, [w["tau"] for w in
                                                  rows])[0]))

    # ============================================================== A2
    print("\nA2 -- the candidate scale carriers")
    # Chebyshev leg on the table
    NN = np.arange(2, core.ATOM_MAX + 1)
    psi_tab = np.cumsum(core.LAM_TAB[NN])
    tt = NN.astype(float)
    m_cheb = psi_tab >= C_PSI * tt
    lo_i = int(np.searchsorted(NN, int(T0_CHEB)))
    cheb_ok = bool(m_cheb[lo_i:].all())
    check("A2.CHEB [unconditional leg] psi(t) >= %.1f t verified "
          "DIRECTLY on the atom table for all t in [%d, %d] "
          "(classical Chebyshev cited beyond); worst ratio %.4f"
          % (C_PSI, int(T0_CHEB), core.ATOM_MAX,
             float((psi_tab[lo_i:] / tt[lo_i:]).min())), cheb_ok)

    cens = composite_census(rows, U_FRAC)
    for c, w in zip(cens, rows):
        x_star = math.exp(U_FRAC * 2.0 * w["alpha"])
        if x_star >= T0_CHEB:
            c["m_bound"] = C_PSI * math.sqrt(x_star)
        elif x_star >= 2.0:
            c["m_bound"] = math.log(2.0) / math.sqrt(2.0)
        else:
            c["m_bound"] = 0.0
    mb_ok = all(c["m_low"] >= c["m_bound"] - 1e-12 for c in cens
                if c["m_bound"] > 0)
    n_act = sum(1 for c in cens if c["m_bound"] > 0)
    check("A2.i-MASS the explicit lower bound m_low >= psi(x*)/"
          "sqrt(x*) >= %.1f sqrt(x*) holds on all %d active rungs "
          "(u* = %.2f x 2 alpha; m_low = %.3f..%.3f, bound "
          "tightness median %.2f)"
          % (C_PSI, n_act, U_FRAC, min(c["m_low"] for c in cens),
             max(c["m_low"] for c in cens),
             float(np.median([c["m_low"] / c["m_bound"] for c in cens
                              if c["m_bound"] > 0]))), mb_ok)

    ok_c, txt_c, ratio_c, sl_c = stab_of(cens)
    print("    composite table (every %dth rung): tau = c x m_low x "
          "phi_bar (phi_bar = q_low/m_low)" % STRIDE)
    print("    %5s %7s | %7s %10s %10s | %10s"
          % ("h", "alpha", "m_low", "phi_bar", "q_low", "c"))
    for c in cens[::STRIDE]:
        print("    %5d %7.3f | %7.3f %10.3e %10.3e | %10.3g"
              % (c["h"], c["alpha"], c["m_low"],
                 c["q_low"] / c["m_low"], c["q_low"], c["c"]))
    check("A2.i-COMPOSITE the frozen composite tau = c q_low with "
          "u* = %.2f x 2 alpha: %s (gates: q_low > 0 all rungs, "
          "ratio <= %.0f, |slope| <= %.2f)"
          % (U_FRAC, txt_c, C_STAB_RATIO, C_STAB_SLOPE), ok_c)
    uhalfs = []
    for w in rows:
        rr = w["rr"]
        u2 = w["u2"]
        edges, reads = pnt_cells_frame(
            rr["alpha"], rr["M"], rr["D"], rr["W11"], rr["W22"],
            rr["W12"], 2.0 * rr["alpha"] + 1e-9)
        centers = 0.5 * (edges[:-1] + edges[1:])
        phi_c = np.array([float(u2 @ (xmat(x) @ u2)) for x in reads])
        m_c = 2.0 * (np.exp(edges[1:] / 2.0) - np.exp(edges[:-1] / 2.0))
        contrib = rr["lam"] * np.array(
            [float(u2 @ (xmat(x) @ u2)) for x in rr["Xn"]])
        atom_cum = np.zeros(len(centers))
        idx = np.searchsorted(centers, rr["uu"])
        np.add.at(atom_cum, np.minimum(idx, len(centers) - 1), contrib)
        path = np.cumsum(atom_cum - m_c * phi_c)
        tgt = path[-1]
        uhalfs.append(float(
            centers[int(np.argmax(np.abs(path) >= 0.5 * abs(tgt)))]
            / (2.0 * rr["alpha"])))
    print("    secondary convention reported: per-window u_half/2a = "
          "%.3f..%.3f (median %.3f) vs the frozen fixed fraction "
          "%.2f" % (min(uhalfs), max(uhalfs),
                    float(np.median(uhalfs)), U_FRAC))

    s_tau_a = np.polyfit(aas, np.log([w["tau"] for w in rows]), 1)[0]
    pack_ok = abs(s_tau_a - PACKET_SLOPE_CITED) <= TRACK_TOL
    check("A2.ii the packet floor (v791 CITED, not rebuilt): tau "
          "slope %.3f/alpha-unit vs cited min-sector slope %.2f -- "
          "%s (bar |diff| <= %.2f)"
          % (s_tau_a, PACKET_SLOPE_CITED,
             "tracks" if pack_ok else "does NOT track: the packet "
             "dilution is slower than the lock margin", TRACK_TOL),
          pack_ok)

    q_odds = []
    for w in rows:
        rr = w["rr"]
        u2 = w["u2"]
        nn = np.rint(np.exp(rr["uu"])).astype(np.int64)
        phi = np.array([float(u2 @ (xmat(x) @ u2)) for x in rr["Xn"]])
        odd = (nn % 2) == 1
        q_odds.append(float(np.sum(rr["lam"][odd] * phi[odd])))
    sl_odd, _, r2_odd = ols_loglog(hs, [w["tau"] / q
                                        for w, q in zip(rows, q_odds)])
    odd_ok = abs(sl_odd) <= FLAT_TOL
    check("A2.iii the ram-odd channel mass: tau/q_odd trend h^%.2f "
          "(R^2 %.2f, bar |slope| <= %.2f) -- %s"
          % (sl_odd, r2_odd, FLAT_TOL,
             "tracks" if odd_ok else "does NOT track: the odd-"
             "channel quadratic mass is a tau_pnt-scale object, not "
             "a tau-scale object"), odd_ok)

    # ============================================================== A3
    print("\nA3 -- exponent bookkeeping + per-factor typing")
    sl_m, _, _ = ols_loglog(hs, [c["m_low"] for c in cens])
    sl_phi, _, _ = ols_loglog(hs, [c["q_low"] / c["m_low"]
                                   for c in cens])
    sl_tau, _, _ = ols_loglog(hs, [w["tau"] for w in rows])
    print("""    tau ~ h^%.2f  =  m_low (h^%+.2f, UNCONDITIONAL via Chebyshev)
                x  phi_bar (h^%+.2f, measured-structural: the low-u
                   projection geometry of the parity frame)
                x  c (h^%+.2f, %s)
    envelope bookkeeping: rho = tau/tau_pnt ~ h^%.2f vs the h^-3/2
    envelope -- the three-factor skeleton carries a = %.2f of the
    density scale plus the composite factors."""
          % (sl_tau, sl_m, sl_phi, sl_c if sl_c is not None else
             float("nan"),
             "the OPEN factor: stable = derivation skeleton complete"
             if ok_c else "UNSTABLE -- the breaking factor",
             ols_loglog(hs, [w["tau"] / w["tau_pnt"]
                             for w in rows])[0], -a_ext))

    # ============================================================== B
    print("\nB -- the angle-native capture sandwich")
    for w in rows:
        A = full_A(w["rr"])
        wA, VA = np.linalg.eigh(A)
        l1, l2 = float(wA[0]), float(wA[1])
        u1v, u2v = VA[:, 0], VA[:, 1]
        Vq, _ = np.linalg.qr(np.stack([w["rr"]["t1"], w["rr"]["t2"]],
                                      axis=1))
        M2 = Vq.T @ (A @ Vq)
        tau_q = float(np.linalg.eigvalsh(M2)[0])
        O = Vq.T @ np.stack([u1v, u2v], axis=1)
        gram = O @ O.T
        gw, gV = np.linalg.eigh(gram)
        cstar = gV[:, 1]
        vstar = Vq @ cstar
        bnd = float(vstar @ (A @ vstar))
        a2 = float(vstar @ u1v) ** 2
        b2 = float(vstar @ u2v) ** 2
        wM, VM = np.linalg.eigh(M2)
        vmin = Vq @ VM[:, 0]
        jmin = (float(wM[0]) - l1 * float(vmin @ u1v) ** 2
                - l2 * float(vmin @ u2v) ** 2)
        w.update(l1_full=l1, l2_full=l2, tau_q=tau_q, bnd=bnd,
                 dmin=1.0 - float(gw[1]), a2=a2, b2=b2,
                 jstar=bnd - l1 * a2 - l2 * b2, jmin=jmin,
                 cos1=float(np.linalg.norm(O[:, 0])),
                 cos2=float(np.linalg.norm(O[:, 1])))
        del A, VA
    print("    sandwich table (every %dth rung): lambda_1 <= tau <= "
          "v*^T A v* (v* angle-built from the top-2 co-capture)"
          % STRIDE)
    print("    %5s %7s | %6s %6s %6s | %7s %8s %8s %7s"
          % ("h", "alpha", "cos_u1", "cos_u2", "dmin", "tau/l1",
             "bnd/l1", "J*/l1", "l2/l1"))
    for w in rows[::STRIDE]:
        print("    %5d %7.3f | %6.3f %6.3f %6.4f | %7.3f %8.3f "
              "%8.3f %7.2f"
              % (w["h"], w["alpha"], w["cos1"], w["cos2"], w["dmin"],
                 w["tau_q"] / w["l1_full"], w["bnd"] / w["l1_full"],
                 w["jstar"] / w["l1_full"],
                 w["l2_full"] / w["l1_full"]))
    jm = [w["jmin"] / w["l1_full"] for w in rows]
    print("    report: the TRUE minimizer's residual J_min/lambda_1 "
          "= %.3f..%.3f (median %.3f) -- what any angle-native upper "
          "bound must reproduce; the top-2 co-capture misses it "
          "because cos_u2 stays ~0.5" %
          (min(jm), max(jm), float(np.median(jm))))
    sand_lo = all(w["tau_q"] >= w["l1_full"] * (1 - 1e-8) for w in rows)
    bnd_r = [w["bnd"] / w["l1_full"] for w in rows]
    js_r = [w["jstar"] / w["l1_full"] for w in rows]
    sand_up = max(bnd_r) <= CUP_BAR and max(js_r) <= JSTAR_BAR
    verdict_b = ("CAPTURE-SANDWICHED" if (sand_lo and sand_up)
                 else "CAPTURE-STILL-LOOSE")
    check("B.1 the sandwich: lower tau >= lambda_1 exact on all "
          "rungs (%s); upper bnd/lambda_1 in [%.2f, %.2f] (bar <= "
          "%.0f), residual J*/lambda_1 in [%.2f, %.2f] (bar <= %.0f) "
          "--> %s"
          % ("holds" if sand_lo else "VIOLATED", min(bnd_r),
             max(bnd_r), CUP_BAR, min(js_r), max(js_r), JSTAR_BAR,
             verdict_b), sand_lo and sand_up)

    # ============================================================== C
    print("\nC -- controls")
    sub5 = rows[::STRIDE]
    cens_scr = composite_census(sub5, U_FRAC, scrambled=True)
    ok_scr, txt_scr, _, _ = stab_of(cens_scr)
    check("C1 [must-fire] the scramble breaks the composite: "
          "scrambled census %s -- %s"
          % (txt_scr, "still stable (control fails)" if ok_scr else
             "UNSTABLE as demanded (the low-u mass/geometry is comb "
             "content)"), not ok_scr)

    ratios = []
    for w in sub5:
        uuE, mE_raw = epstein_atoms(w["alpha"])
        kap = 2.0 * float(np.sum(w["rr"]["lam"])) / float(np.sum(mE_raw))
        ustar = U_FRAC * 2.0 * w["alpha"]
        m_low_E = float(np.sum(kap * mE_raw[uuE <= ustar]))
        m_low_R = float(np.sum(
            2.0 * w["rr"]["lam"][w["rr"]["uu"] <= ustar]))
        ratios.append(m_low_E / m_low_R)
    med_dev = float(np.median([abs(r - 1.0) for r in ratios]))
    check("C2 [must-fire] the Epstein comb has a measurably "
          "different Chebyshev factor: m_low_E/m_low = %.2f..%.2f, "
          "median |ratio - 1| = %.2f (bar >= %.2f) -- the low-u "
          "mass is arithmetic-specific"
          % (min(ratios), max(ratios), med_dev, EPS_MASS_DIFF),
          med_dev >= EPS_MASS_DIFF)

    cens_w = composite_census(rows, U_FRAC_WRONG)
    ok_w, txt_w, _, _ = stab_of(cens_w)
    check("C3 the wrong u* convention (%.2f x 2 alpha): census %s "
          "-- %s (typed as it falls)"
          % (U_FRAC_WRONG, txt_w,
             "breaks as demanded" if not ok_w else "does NOT break: "
             "the composite is convention-robust up to u* = alpha "
             "(the amplifier saturates early -- consistent with the "
             "low-u accumulation)"), not ok_w)

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- verdicts + the updated reduced floor statement "
          "(report only)")
    print("=" * 78)
    env_ok = (r2_fit >= FIT_R2 and r2_ext >= FIT_R2 and cheb_ok
              and mb_ok and ok_c and (not ok_scr)
              and med_dev >= EPS_MASS_DIFF)
    if env_ok:
        verdict_a = "ENVELOPE-THREE-FACTOR"
    elif ok_c or (cheb_ok and mb_ok):
        verdict_a = "ENVELOPE-PARTIAL"
    else:
        verdict_a = "ENVELOPE-OPEN"
    print("""
  PART A: %s
      tau_pnt ~ %.3g h^-%.2f (numeric, R^2 %.2f; symbolic OPEN --
      house arch/spline conventions).  The composite tau = c x
      m_low x phi_bar: %s.
      FACTOR TYPING: m_low UNCONDITIONAL (Chebyshev, verified on
      the table); phi_bar MEASURED-STRUCTURAL (h^%+.2f, the low-u
      parity read geometry); c %s (h^%+.2f).
      Candidates (ii) packet floor: %s; (iii) ram-odd mass: %s.
  PART B: %s
      lambda_1 <= tau <= v*^T A v* with v* angle-built; bnd/lambda_1
      max %.2f, J*/lambda_1 max %.2f -- %s.

  UPDATED REDUCED FLOOR STATEMENT (report only):
  'inf_X lambda_min(T_GL1,X) >= 0 reduces to tau(X) > 0 of the
  2-mode lock compression [angle-sandwiched: lambda_1 <= tau <= v*
  Rayleigh, v* from the top-2 co-capture%s].  tau = tau_pnt x rho
  with tau_pnt ~ %.3g h^-%.2f numeric-explicit and the h^-3/2
  envelope of rho carrying the three-factor skeleton (Chebyshev
  mass x parity read geometry x constant%s).  The named open
  factors: the symbolic tau_pnt asymptotic, and %s.'
""" % (verdict_a, C_ext, -a_ext, r2_ext, txt_c,
       sl_phi, "STABLE -- the skeleton closes at finite level"
       if ok_c else "UNSTABLE -- the open factor",
       sl_c if sl_c is not None else float("nan"),
       "tracks" if pack_ok else "non-tracking (typed)",
       "tracks" if odd_ok else "non-tracking (typed)",
       verdict_b, max(bnd_r), max(js_r),
       "the sandwich is O(1)-tight with NO global-E factor"
       if (sand_lo and sand_up) else "the upper leg stays loose",
       "" if (sand_lo and sand_up) else " -- upper leg loose",
       C_ext, -a_ext,
       "" if ok_c else " -- composite unstable",
       "the composite constant c" if ok_c else
       "the composite stability itself"))

    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
