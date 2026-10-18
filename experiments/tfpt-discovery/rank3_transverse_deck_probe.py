"""Discovery probe: P4 MAIN STRIKE -- TRANSVERSE SCALARIZATION x
DECK TRIPLICATION for the ten open T-B windows at citation height
3e12.

DIAGNOSIS (memo): the 2e route (v693) majorizes the THREE matrix
entries separately (entrywise absolute-value pairings in the original
basis) and only then applies the determinant structure via the
adjugate -- internal cancellation is sacrificed.  But the margin is
already understood as a transverse square sum (2d):
margin = c_P (s_perp^T G_Z s_perp).

T1 -- TRANSVERSE SCALARIZATION [E]:
  Work in the orthonormal pole frame (s, s_perp) from P = c_P s s^T.
  By bilinearity the frame components of every off-line bracket are
  SINGLE-PROFILE functionals:
     s_perp^T B_z s_perp  =  bracket of T[g] with g = s_perp . (f1,f2)
  (one scalar per hypothetical zero).  The chain
     det Ahat2 = det(A + B),  A = X + Q' psd  (X = G_Z^{<=2e4} + P,
     Q' = on-line >2e4 + off-line psd parts), B = sum_z B_z,
     det(A+B) = det A + tr(adj(A) B) + det B,   det A >= det X,
     |tr(adj(A)B)| <= (|Ahat2_ss|+E_ss) E_pp + (|Ahat2_pp|+E_pp) E_ss
                      + 2 (|Ahat2_sp|+E_sp) E_sp,
     |det B| <= E_ss E_pp + E_sp^2
  needs only envelopes E_cc of the frame-scalar brackets.  KEY: the
  dominant weight |Ahat2_ss| ~ c_P multiplies E_pp -- the TRANSVERSE
  envelope, where the internal cancellation lives.

  ENVELOPE (exact adversarial-phase sup, still zero-data-free):
   bracket_uu(gamma, delta) via FF_u(z) - FF_u(gamma)
     = sum_k c_k (e^{-k D delta} - 1) e^{i k D gamma},
   c_k = SIGNED correlation sum_m u[m] u[m-k]  (not |u| pairings!).
   Per zero:  sup_theta |F_delta(theta)|  -- a degree-(M-1) trig
   polynomial: FFT on N >= 64(M-1) points, elementary Bernstein
   rigor sup <= max_grid / (1 - pi (M-1)/N); delta-cell slack
   sum_k |c_k| |w_k(d_top) - w_k(d_bot)|.  The second bracket term
   uses sup_theta |F_u F_v|(theta) (grid max, Bernstein with degree
   2(M-1)) instead of ||u||_1 ||v||_1.  V(0) = 0, Abel in delta with
   running-max monotonization, W(u) tails and citations exactly as
   2e ([A1] Platt-Trudgian 3e12, [A2] Hasanalizade-Shen-Wong RvM,
   [A3] halving + on-line subtraction, [A4] explicit Ingham form
   arXiv:2507.15184 Cor. 1 Table 1).

T2 -- DECK TRIPLICATION [E-identity + honest test]:
  The arch tower rho(t) = e^{-t/2}/(1-e^{-2t}) splits EXACTLY into
  the three deck channels m mod 12 in {1,5,9} (chain_deck_sector D3)
  == digamma multiplication theorem psi(1/4 + it/2) = log 3 +
  (1/3) sum_j psi({1/12, 5/12, 3/4} + it/6) -- verified here to
  1e-20.  CIRCULARITY RULE: no measured phases above the citation
  height, no cancellation fitted from low zeros -- the only
  admissible use is algebraic.  HONEST STRUCTURAL FINDING (tested):
  the channel split of the scalar profile (lag classes mod 3, the
  zeta_12/deck mirror) gives sup_theta|F| <= sum_chi sup|F^chi| by
  triangle -- i.e. a PER-CHANNEL envelope can only be WEAKER than
  the direct T1 sup; the cross-channel cancellation the memo hopes
  for is exactly what the T1 sup already realizes (measured:
  ell^1 / sup ratio = the realized cancellation; channel-split
  ratio printed).  Deck triplication as an INDEPENDENT lever on top
  of T1 is therefore measured, and killed if < factor 2 (memo
  criterion).

T3 -- THE GATE: table over the ten open windows (h = 1359, 1868,
  2018, 2093, 2472, 2475, 1721, 2630, 2656, 5690) x {PEN_matrix
  (= 2e route), PEN_transverse, margin_cert, verdict}; full-70
  census with the best penalty; new exact T* for whatever stays
  open.

FIREWALL: new file only; parents (rank3_lockgram_probe = 2d,
rank3_density_close_probe = 2e) imported READ-ONLY.  Zeros <= 2e4
computed (RvM-checked) enter the MARGIN only; the penalty uses no
zero data (sup over all phases).  No RNG, no marker moves.
"""
import json
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
import rank3_zeroside_probe as zp            # noqa: E402 (parent, RO)
import rank3_lockgram_probe as lg            # noqa: E402 (parent, RO)
import rank3_density_close_probe as dc       # noqa: E402 (parent, RO)

T0 = time.time()
FAILS = []
N_CHK = 0

T_RH = 3.0e12
N_DELTA = 120
FFT_OVER = 64            # FFT grid >= FFT_OVER x degree (Bernstein)
SAFETY = 2.0

OPEN10 = {1359, 1868, 2018, 2093, 2472, 2475, 1721, 2630, 2656, 5690}


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def corr_signed(u, v):
    """c_k = sum_m u[m] v[m-k], k = -(M-1)..(M-1) (signed!)."""
    return np.convolve(u, v[::-1])


def sup_trig(coeffs, k_lo, deg_extra=0):
    """rigorous sup_theta |sum_k a_k e^{i k theta}| for the
    coefficient array coeffs (k starting at k_lo): FFT grid max
    x elementary Bernstein factor 1/(1 - pi deg / N)."""
    n = len(coeffs)
    deg = max(abs(k_lo), abs(k_lo + n - 1)) + deg_extra
    N = 1 << int(math.ceil(math.log2(max(FFT_OVER * deg, 4096))))
    buf = np.zeros(N, dtype=complex)
    idx = (np.arange(k_lo, k_lo + n)) % N
    buf[idx] = coeffs
    vals = np.abs(np.fft.fft(buf))
    bern = 1.0 / (1.0 - math.pi * deg / N)
    return float(vals.max()) * bern


def sup_product(u, v):
    """rigorous sup_theta |F_u(theta) F_v(theta)|, F_u of degree
    M-1: grid max of the product with degree-2(M-1) Bernstein."""
    m = len(u)
    deg = 2 * (m - 1)
    N = 1 << int(math.ceil(math.log2(max(FFT_OVER * deg, 4096))))
    fu = np.fft.fft(u, N)
    fv = np.fft.fft(v, N)
    bern = 1.0 / (1.0 - math.pi * deg / N)
    return float(np.max(np.abs(fu) * np.abs(fv))) * bern


def scalar_dv(u, v, D, dgrid, use_sup):
    """Abel increment vector dV for the frame-scalar envelope of the
    profile pair (u, v): E_uv(W) = dV . W[:-1] (linear in the count
    grid -- reused for every citation height).
    ENV1 per cell (delta_{m-1}, delta_m]:
      min( sup_theta|F_{delta_m}| + cell slack,  signed-ell1(delta_m) )
    where signed-ell1 is itself a valid whole-cell bound (increasing
    in delta) and the slack sum_k |c_k||w_k(d_m) - w_k(d_{m-1})|
    covers the non-monotonicity of the sup inside the cell."""
    Mz = len(u)
    cc = corr_signed(u, v)
    cs = 0.5 * (cc + cc[::-1])          # polarized, symmetric in k
    kk = np.arange(-(Mz - 1), Mz)
    corr_f = 1.0 + 2.0 / (T_RH * D)
    supp = sup_product(u, v)
    aw = np.abs(cs)
    env1 = np.zeros(len(dgrid))
    w_prev = np.zeros(len(kk))
    for m, d_ in enumerate(dgrid):
        if d_ == 0.0:
            continue
        w_k = np.exp(-kk * D * d_) - 1.0
        l1 = float(aw @ np.abs(w_k))
        if use_sup:
            slack = float(aw @ np.abs(w_k - w_prev))
            env1[m] = min(sup_trig(cs * w_k, -(Mz - 1)) + slack, l1)
        else:
            env1[m] = l1
        w_prev = w_k
    V = 8.0 * np.cosh(dgrid * D / 2.0) ** 2 \
        * (env1 / D + dgrid * corr_f * supp)
    V = np.maximum.accumulate(V)        # rigorous monotonization
    return V[1:] - V[:-1]


def frame_of(w):
    """orthonormal pole frame from P = c_P s s^T + exact Ahat2
    frame components."""
    P = np.empty((2, 2))
    for (i, j), (fa, fb) in {(0, 0): (w["f1"], w["f1"]),
                             (1, 1): (w["f2"], w["f2"]),
                             (0, 1): (w["f1"], w["f2"])}.items():
        tp = lg.T_pair(fa, fb, w["D"], np.array([0.5j, -0.5j]))
        P[i, j] = P[j, i] = -0.5 * float(np.real(np.sum(tp)))
    pw, pv = np.linalg.eigh(P)
    s = pv[:, 1]
    sp = np.array([-s[1], s[0]])
    A2 = w["A2"]
    return dict(s=s, sp=sp, c_p=float(pw[1]),
                rank1=abs(pw[0]) / abs(pw[1]),
                a_ss=float(s @ A2 @ s), a_pp=float(sp @ A2 @ sp),
                a_sp=float(s @ A2 @ sp))


def dvs_of(w, fr, dgrid, use_sup):
    """cached Abel increment vectors for the three frame pairs."""
    g_s = fr["s"][0] * w["f1"] + fr["s"][1] * w["f2"]
    g_p = fr["sp"][0] * w["f1"] + fr["sp"][1] * w["f2"]
    return (scalar_dv(g_s, g_s, w["D"], dgrid, False),
            scalar_dv(g_s, g_p, w["D"], dgrid, False),
            scalar_dv(g_p, g_p, w["D"], dgrid, use_sup))


def pen_transverse(fr, dvs, wgrid):
    """det-level transverse-scalarized penalty (linear in wgrid)."""
    E_ss = float(dvs[0] @ wgrid[:-1])
    E_sp = float(dvs[1] @ wgrid[:-1])
    E_pp = float(dvs[2] @ wgrid[:-1])
    pen = (abs(fr["a_ss"]) + E_ss) * E_pp \
        + (abs(fr["a_pp"]) + E_pp) * E_ss \
        + 2.0 * (abs(fr["a_sp"]) + E_sp) * E_sp \
        + E_ss * E_pp + E_sp ** 2
    return pen, E_ss, E_sp, E_pp


def t_star_trans(fr, dvs, m_cert, dgrid):
    def pen_at(tq):
        wg = np.array([dc.w_tail(u, tq) for u in dgrid])
        return pen_transverse(fr, dvs, wg)[0]
    lo, hi = math.log(T_RH), math.log(1e40)
    if pen_at(math.exp(lo)) < m_cert / SAFETY:
        return T_RH
    for _ in range(30):
        mid = 0.5 * (lo + hi)
        if pen_at(math.exp(mid)) < m_cert / SAFETY:
            hi = mid
        else:
            lo = mid
    return math.exp(hi)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("P4 MAIN STRIKE -- transverse scalarization x deck "
          "triplication (T-B remainder)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- zeros (margin only) + windows + circularity guard")
    with open(os.path.join(_here, "zero_comb_cache_n2000.json")) as fh:
        g_a = [float(s_) for s_ in json.load(fh)["gammas"]]
    with open(os.path.join(_here, "c1_zero_ext_n2500.json")) as fh:
        g_b = [float(s_) for s_ in json.load(fh)["gammas"]]
    g_prec = np.array(g_a + g_b)
    g_scan = zp.find_zeros(float(g_prec[-1]) + 0.4, zp.T_SCAN,
                           zp.SCAN_STEP)
    gam = np.sort(np.concatenate([g_prec, g_scan]))
    n_rvm = float(zp.theta_rs(np.array([zp.T_SCAN]))[0] / math.pi + 1.0)
    check("S0.Z zero list: %d zeros to 2e4 (RvM dev %.2f <= 3); "
          "CIRCULARITY GUARD: computed zeros enter the MARGIN only; "
          "the penalty envelopes take sup over ALL phases (no zero "
          "data, no fitted cancellation)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)

    dgrid = np.concatenate([[0.0], np.geomspace(2e-4, 0.5, N_DELTA - 1)])
    wgrid = np.array([dc.w_tail(u, T_RH) for u in dgrid])

    # ============================================================== T2a
    print("\nT2a -- triplication identity (exact, algebraic)")
    import mpmath as mp
    mp.mp.dps = 30
    dev = 0.0
    for t_ in (0.0, 0.7, 3.3, 14.1, 77.7):
        z = mp.mpf(1) / 12 + 1j * mp.mpf(t_) / 6
        lhs = mp.digamma(3 * z)
        rhs = mp.log(3) + (mp.digamma(z) + mp.digamma(z + mp.mpf(1) / 3)
                           + mp.digamma(z + mp.mpf(2) / 3)) / 3
        dev = max(dev, float(abs(lhs - rhs)))
    check("T2a.ID digamma multiplication theorem psi(1/4 + it/2) = "
          "log 3 + (1/3) sum psi({1/12, 5/12, 3/4} + it/6): max dev "
          "%.1e <= 1e-20 on the t-grid (the deck channel split of "
          "the arch tower is EXACT; chain_deck D3)" % dev,
          dev <= 1e-20)

    # ============================================================== T1
    print("\nT1/T3 -- transverse scalarization, all complete windows")
    print("    %5s %7s | %11s %11s %11s | %8s | %s"
          % ("h", "a", "margin_cert", "PEN_matrix", "PEN_transv",
             "T*_new", "verdict"))
    KZ = core.frame_a_zones()
    rows = []
    for kz in range(len(KZ)):
        w = lg.lock_block(kz)
        if not w["complete"]:
            continue
        m_cert = dc.margin_cert_of(w, gam)
        fr = frame_of(w)
        R = dc.pen_matrix(w, T_RH, dgrid, wgrid)
        pen_m = dc.det_penalty(w["A2"], R)
        # stage 1: signed-ell1 scalarization; stage 2: exact sup
        dvs = dvs_of(w, fr, dgrid, False)
        pen_t, E_ss, E_sp, E_pp = pen_transverse(fr, dvs, wgrid)
        used_sup = False
        if pen_t >= m_cert:
            dvs = dvs_of(w, fr, dgrid, True)
            pen_t, E_ss, E_sp, E_pp = pen_transverse(fr, dvs, wgrid)
            used_sup = True
        closes = m_cert > pen_t
        t_st = T_RH if closes else t_star_trans(fr, dvs, m_cert,
                                                dgrid)
        rows.append(dict(kz=kz, h=w["h"], a=w["alpha"], m=m_cert,
                         pm=pen_m, pt=pen_t, closes=closes, ts=t_st,
                         fr=fr, E=(E_ss, E_sp, E_pp), sup=used_sup))
        mark = "O" if w["h"] in OPEN10 else " "
        print("   %s%5d %7.3f | %11.4e %11.4e %11.4e | %8s | %s%s"
              % (mark, w["h"], w["alpha"], m_cert, pen_m, pen_t,
                 ("--" if closes else "%.1e" % t_st),
                 "CLOSES" if closes else "factor %.1f"
                 % (pen_t / m_cert),
                 " [sup]" if used_sup else ""))
    n_all = len(rows)
    n_close = sum(r["closes"] for r in rows)
    open_rows = [r for r in rows if not r["closes"]]
    imp = [r["pm"] / r["pt"] for r in rows]
    o10 = [r for r in rows if r["h"] in OPEN10]
    o10_closed = [r for r in o10 if r["closes"]]
    check("T1.SCAL scalarization consistent: rank-1 pole frame "
          "(max dev %.1e), improvement factor PEN_matrix/PEN_transv "
          "in [%.2f, %.2f] (median %.2f) over %d windows"
          % (max(r["fr"]["rank1"] for r in rows), min(imp), max(imp),
             float(np.median(imp)), n_all),
          max(r["fr"]["rank1"] for r in rows) < 1e-10)

    # ============================================================== T2b
    print("\nT2b -- deck channels as an independent lever (honest)")
    r_big = max(o10, key=lambda r: r["h"])
    w = lg.lock_block(r_big["kz"])
    fr = r_big["fr"]
    g_p = fr["sp"][0] * w["f1"] + fr["sp"][1] * w["f2"]
    Mz, D = len(g_p), w["D"]
    cc = corr_signed(g_p, g_p)
    cs = 0.5 * (cc + cc[::-1])
    kk = np.arange(-(Mz - 1), Mz)
    d_t = 0.24                       # dominant Abel cell (crossover)
    w_k = np.exp(-kk * D * d_t) - 1.0
    s_full = sup_trig(cs * w_k, -(Mz - 1))
    s_chan = 0.0
    for r_ in range(3):
        mask = ((kk % 3) == r_).astype(float)
        s_chan += sup_trig(cs * w_k * mask, -(Mz - 1))
    l1 = float(np.abs(cs * w_k).sum())
    check("T2b.DECK channel test at the dominant cell (h=%d, "
          "delta=%.2f): direct sup %.3e vs sum of 3 channel sups "
          "%.3e (ratio %.2f >= 1: triangle -- a per-channel envelope "
          "is never sharper) vs ell1 %.3e; the cancellation factor "
          "ell1/sup = %.1f IS the realized internal cancellation and "
          "is already captured by the T1 sup; deck triplication as "
          "an independent PEN lever: %s (memo kill criterion: "
          "factor < 2)"
          % (r_big["h"], d_t, s_full, s_chan, s_chan / s_full, l1,
             l1 / s_full,
             "DEAD" if s_chan / s_full >= 0.5 else "alive"),
          s_chan >= 0.999 * s_full)

    # ============================================================== T3
    print("\nT3 -- the gate")
    print("    open-10 status: %d/10 close at 3e12 with the "
          "transverse route" % len(o10_closed))
    for r in o10:
        print("      h=%5d: margin %.4e  PEN_matrix %.4e  "
              "PEN_transv %.4e  E=(ss %.2e, sp %.2e, pp %.2e)  "
              "frame |A2|=(ss %.2f, pp %.2e, sp %.2e)  -> %s"
              % (r["h"], r["m"], r["pm"], r["pt"], *r["E"],
                 r["fr"]["a_ss"], r["fr"]["a_pp"], r["fr"]["a_sp"],
                 "CLOSES" if r["closes"] else
                 "OPEN, T* = %.1e" % r["ts"]))
    med_imp_o10 = float(np.median([r["pm"] / r["pt"] for r in o10]))
    gate_alive = med_imp_o10 >= 2.0
    check("T3.GATE census %d/%d windows close at 3e12 "
          "(open-10: %d/10 closed); median improvement on the "
          "open-10: x%.2f -> route %s per memo criterion"
          % (n_close, n_all, len(o10_closed), med_imp_o10,
             "ALIVE" if gate_alive else "documented-DEAD (< x2)"),
          n_close >= 60)

    # ============================================================== T4
    print("\nT4 -- consolidation")
    if n_close == n_all:
        verdict = ("FULL T-B SURFACE THEOREM: det Ahat2 > 0 on ALL "
                   "%d complete windows, unconditional modulo "
                   "[A1]-[A4]" % n_all)
    else:
        verdict = ("PARTIAL: %d/%d; open remainder %s"
                   % (n_close, n_all,
                      [(r["h"], "%.1e" % r["ts"]) for r in open_rows]))
    print("""
  THEOREM CANDIDATE (T-B block, transverse route, typed inputs):
    det Ahat2 >= det(G_Z^{<=2e4} + P) - PEN_transverse > 0, with
      [E]  v677 master identity + psd superadditivity (2d),
      [E]  pole frame (s, s_perp), exact frame scalarization
           (bilinearity), det perturbation identity,
      [E]  adversarial-phase sup envelopes (FFT + Bernstein grid
           factor, delta-cell slack, running-max Abel),
      [E]  triplication identity of the arch tower (exact digamma
           multiplication theorem; structural explanation of the
           realized cancellation),
      [A1] RH to 3e12 (Platt-Trudgian 2021),
      [A2] explicit RvM count (Hasanalizade-Shen-Wong 2022),
      [A3] functional-equation halving + on-line subtraction,
      [A4] explicit Ingham-form zero density (arXiv:2507.15184).
  %s
  STILL MISSING FOR FULL RANK-3 POSITIVITY: the W3 orthogonal-mode
  remainder (all h modes beyond the lock plane) -- unchanged from 2e.
""" % verdict)
    print("=" * 78)
    print("CONTRACT NOTE UPDATE (prob:R1)")
    print("=" * 78)
    print("""
  P4 (transverse x deck): scalarization onto s_perp puts the whole
  off-line question on ONE profile g_perp; the exact adversarial-
  phase sup (zero-data-free) replaces entrywise ell1 majorization.
  Improvement on the open-10: median x%.2f.  Census: %d/%d complete
  windows close at 3e12%s.  Deck triplication verified EXACT on the
  arch side; as an independent PEN lever beyond the T1 sup it is
  %s.
""" % (med_imp_o10, n_close, n_all,
       "" if n_close == n_all else
       "; open: " + ", ".join("h=%d (T* %.1e)" % (r["h"], r["ts"])
                              for r in open_rows),
       "dead (triangle: channel sups can only lose)"))

    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
