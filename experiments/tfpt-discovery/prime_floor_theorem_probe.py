#!/usr/bin/env python3
"""prime_floor_theorem_probe -- the floor-theorem assembly attempt.

EXPLORATION ONLY (experiments/): no verification claim, no ledger row,
no paper edit.  NO RH claim anywhere.  Maximal honesty about which
pieces reach theorem grade vs verified-per-rung grade.

CONTEXT (prime_lagrange_pair_probe -> prime_lagrange_budget_probe,
PAIR-CERTIFIED): lambda tau = det Ahat2 >= det(G_Z+P) >= X^2(pole,g1)
per rung via the psd-remainder chain.  Three named gaps attacked here.

PIECE 1 -- PSD REMAINDER AS THEOREM.  Replace the per-rung eigencheck
  lambda_min(R) > 0 by the citation-grade decomposition
    R = R_band(2e4 < gamma <= 3e12; psd BY CITATION, zeros on-line
        by verified computation [Platt-Trudgian 2021])
      + R_deep(gamma > 3e12; UNKNOWN location inside the strip
        0 < Re s < 1 = [A1], worst-case displacement |delta| <= 1/2),
  with the EXPLICIT elementary envelope (per rung, all sums finite):
    E_i = 2 sum_j |t_ij| e^{(h-j-1/2) D/2}   (worst off-line leg),
    |layer entry| <= 4 cosh^2(D/4) E_i E_j / (D gamma^2),
    sum_{gamma > T} gamma^-2 <= (log T + 1)/(pi T)   (Abel with
      N(t) <= t log t / 2pi),
    eps_deep = 4 cosh^2(D/4) max(E_i E_j)/D x (log T_RH + 1)/(pi T_RH)
  plus the master-identity defect budget: eps_arch = the measured
  GL-48 -> GL-96 shift of the arch lags (x ARCH_SLACK) and float.
  Chain: det Ahat2 >= det(G_Z+P) - pert(eps_deep + eps_arch + eps_f),
  pert(e) = e (|a11|+|a22|+2|a12|) + 2 e^2.  PASS per rung iff
  pert < X^2.  KILL/type: where the envelope's h-growth beats X^2,
  the required citation horizon T_need(h) is printed -- the precise
  RH-content re-entry point (zero location beyond the strip is never
  used; only DEPTH of the verified on-line band).

PIECE 2 -- UNIFORM h-ASYMPTOTIC OF THE FIXED PAIR.  The exact closed
  form (Dirichlet kernels; hD = alpha exactly in the deployed frame):
    S_k(phi) = (1/sqrt N)[T1 - T2],  T_m = cos(c_m + s_m (h-1)/2)
               sin(h s_m / 2)/sin(s_m / 2),
    s_1 = om + phi, c_1 = om - (h-1/2) phi;  s_2 = om - phi,
    c_2 = om + (h-1/2) phi;  om = 2 pi k / N, N = 2h+1,
  and the ANALYTIC h -> infinity limit (derived, then verified):
    G_k(u)  = pi k sin(u) / (pi^2 k^2 - u^2),        u = alpha gamma_1,
    Gp_k    = pi k sinh(alpha/2) / (pi^2 k^2 + alpha^2/4),
    X_inf(alpha) = 8 alpha [G_1(u) Gp_2 - G_2(u) Gp_1]
      = 16 alpha pi^2 sin(u) sinh(alpha/2)
        [ ((pi^2-u^2)(4pi^2+alpha^2/4))^-1
        - ((4pi^2-u^2)(pi^2+alpha^2/4))^-1 ].
  Deliverable: L(h) = X_inf^2(alpha)(1 - C(alpha)/h) with C(alpha)
  measured on a synthetic h-ladder AT EACH DEPLOYED alpha (x2
  slack; C blows up near the sin-nodes), valid on the explicit
  domain h > h0(alpha) = C(alpha); wards: closed form == direct sum
  (machine), the limit matches all rungs within C(alpha)/h,
  L(h) <= measured X^2 in-domain.  KILL test: sign flips of X
  in h at fixed alpha (expected NONE); the sin(alpha gamma_1) factor
  gives alpha-NODES (spacing pi/gamma_1 ~ 0.2223) -- typed: the fixed
  pair is h-uniform per rung but canNOT be ladder-uniform in alpha;
  at nodes the family (piece 3) takes over.

PIECE 3 -- FAMILY EXTENSION (pole x zeros, the alias carriers).
  Per rung: the family total sum_k X_k^2 vs the pair total
  det(G_Z+P) (Lagrange split: det(G_Z+P) = det(G_Z) + pole-family
  total EXACTLY); the certified family fraction of the floor
  (top-K = 100, same chain, all carriers <= 2e4 on-line by
  computation); the residue 1 - det(G_Z+P)/det(Ahat2) (= the >2e4
  remainder's det contribution) share + trend -- exhaustion iff the
  residue is small with non-growing trend (it is truncation depth,
  not a structural carrier); the family limit F_inf(alpha) =
  sum_zeros X_inf^2(gamma_k; alpha) on a dense alpha grid: its
  minimum must stay positive across the fixed-pair nodes (the
  family never dies simultaneously).

CONTROLS: CT1 synthetic OFF-LINE zero pairs (frozen grid; a single
  off-line pair layer has det < 0 STRUCTURALLY -- Re of a complex
  rank-one -- though the negative eigenvalue can be subleading when
  the two parity legs share the dominant phase) -- the chain must
  break exactly at the off-line locus AND every layer must respect
  the piece-1 envelope   family/identity structure (lambda_min(R_scr) < 0, from the
  declared scramble); CT3 the L(h) ward (piece 2).

SYNTHESIS: per-piece status PROVEN / UNIFORM-VERIFIED /
  PER-RUNG-ONLY / DEAD (frozen rules in code), the strongest
  supported floor assertion verbatim, and the single separating
  object from tau > 0 for all h -- with the honesty note: floor
  positivity on the deployed battery is NECESSARY-side evidence,
  NOT RH; the detector-inversion direction is where floor bounds
  convert to zero-exclusion.

VERDICT (frozen): FLOOR-SKELETON-COMPLETE (all three pieces at least
  UNIFORM-VERIFIED) / FLOOR-PARTIAL (typed per piece) /
  FLOOR-BLOCKED (a piece DEAD, blocker named).

FIREWALL: v563 / v684 / v692 / parent probes READ-ONLY; zero values
used openly (on-line by computation <= 2e4, citation <= 3e12); RNG
only in v563's declared scramble.  Report only, nothing written.
"""

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
sys.path.insert(0, _here)

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
import v684_rank3_zeroside as zp             # noqa: E402 (READ-ONLY)
import v692_rank3_lockgram as lg             # noqa: E402 (READ-ONLY)
import prime_lagrange_pair_probe as pp       # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
T_RH = 3.0e12           # Platt-Trudgian 2021 (cited on-line horizon)
DELTA_OFF = 0.5         # worst-case off-line displacement ([A1] strip)
GL_FINE = 96            # refined arch quadrature (vs deployed 48)
ARCH_SLACK = 10.0       # slack on the measured GL shift as eps_arch
CHAIN_FAC = 100.0       # float chain budget factor
WARD_CF = 1.0e-9        # closed form vs direct sum, relative
SYN_HS = (128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536)
C_SLACK = 2.0           # slack on the measured 1/h-correction constant
K_FAM = 100             # certified family size
FAM_PAIR_TOT = 0.999    # pole family share of the pair total
RES_MAX = 0.06          # residue share bar (exhaustion)
RES_SLOPE_MAX = 0.05    # residue trend bar (vs log h)
FAM_CERT_MED = 0.90     # median certified family fraction of floor
N_GRID = 2001           # alpha grid for the node / family-limit scan
ALPHA_LO, ALPHA_HI = 2.0, 12.0
N_ZLIM = 2000           # zeros in the family-limit sum
# CT1 off-line control grid (calibrated once, then frozen): a single
# off-line pair layer is asymptotically degenerate-indefinite (det < 0
# structurally but the negative eigenvalue can be subleading), so the
# control uses a small grid and fires on the worst configuration
CT1_GRID = ((20.0, 0.3), (20.0, 0.45), (80.0, 0.3), (80.0, 0.45))
CT1_NEG = -1.0e-3       # worst min-eig/scale must be below this
SCRAMBLE_SEED = 20260806
EPSM = float(np.finfo(float).eps)
EPS_JS = 1.0e-300
G1REF = 14.134725141734695   # gamma_1 (cache-verified vs zetazero(1))


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def eig2_min(M):
    tr = M[0, 0] + M[1, 1]
    dif = M[0, 0] - M[1, 1]
    rad = math.sqrt(0.25 * dif * dif + M[0, 1] * M[0, 1])
    return 0.5 * tr - rad


# ---------------------------------------------------------- closed forms
def parity_t(k, h):
    N = 2 * h + 1
    jj = np.arange(h)
    return (2.0 / math.sqrt(N)) * np.sin(
        2.0 * math.pi * k * (jj + 1.0) / N)


def S_direct(k, h, D, g):
    jj = np.arange(h)
    return float(parity_t(k, h) @ np.sin((h - jj - 0.5) * D * g))


def S_closed(k, h, D, g):
    """Exact Dirichlet-kernel closed form of S_k (piece 2)."""
    N = 2 * h + 1
    om = 2.0 * math.pi * k / N
    phi = D * g
    out = 0.0
    for sgn in (1.0, -1.0):
        s = om + sgn * phi
        c = om - sgn * (h - 0.5) * phi
        if abs(math.sin(0.5 * s)) < 1e-14:
            term = h * math.cos(c)          # degenerate Dirichlet
        else:
            term = (math.cos(c + 0.5 * s * (h - 1.0))
                    * math.sin(0.5 * h * s) / math.sin(0.5 * s))
        out += sgn * term
    return out / math.sqrt(N)


def pair_x2_closed(alpha, h, g1):
    """X^2(pole, gamma_1) from the exact closed forms (any alpha, h)."""
    D = alpha / h
    phi = D * g1
    wg = D * (math.sin(0.5 * phi) / (0.5 * phi)) ** 2
    a1 = 2.0 * math.sqrt(wg) * S_closed(1, h, D, g1)
    b1 = 2.0 * math.sqrt(wg) * S_closed(2, h, D, g1)
    jj = np.arange(h)
    e = np.sinh((h - jj - 0.5) * D / 2.0)
    sp1 = float(parity_t(1, h) @ e)
    sp2 = float(parity_t(2, h) @ e)
    cp = 2.0 * math.sqrt(D) * (math.sinh(D / 4.0) / (D / 4.0))
    p1, p2 = cp * sp1, cp * sp2
    x = a1 * p2 - p1 * b1
    return x * x, x


def x_inf(alpha, g):
    """The ANALYTIC h -> infinity limit of X(pole, gamma) (piece 2)."""
    u = alpha * g
    pi2 = math.pi ** 2
    a24 = 0.25 * alpha * alpha
    br = (1.0 / ((pi2 - u * u) * (4.0 * pi2 + a24))
          - 1.0 / ((4.0 * pi2 - u * u) * (pi2 + a24)))
    return (16.0 * alpha * pi2 * math.sin(u)
            * math.sinh(0.5 * alpha) * br)


# ------------------------------------------------- refined arch (piece 1)
_GX96, _GW96 = np.polynomial.legendre.leggauss(GL_FINE)


def arch_A_fine(sv, D):
    """core.arch_A re-evaluated with GL-96 nodes (identical integrand)."""
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        s = sv[far].reshape(-1, 1)
        acc = np.zeros(s.shape[0])
        for lo, hi in ((s - D, s), (s, s + D)):
            mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
            w = mid + half * _GX96[None, :]
            val = ((1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w)
                   / (-np.expm1(-2.0 * w)))
            acc -= half[:, 0] * (val @ _GW96)
        out[far] = acc
    for i in np.nonzero(~far)[0]:
        s = float(sv[i])
        tri_s = max(0.0, 1.0 - s / D)
        W = s + D
        pts = sorted({0.0, s, D - s, W})
        pts = [p for p in pts if 0.0 <= p <= W]
        tot = 0.0
        for lo, hi in zip(pts[:-1], pts[1:]):
            if hi <= lo:
                continue
            mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
            w = mid + half * _GX96
            tri = np.maximum(0.0, 1.0 - np.abs(s - w) / D)
            trr = np.maximum(0.0, 1.0 - np.abs(s + w) / D)
            val = ((tri_s * np.exp(-2.0 * w)
                    - 0.5 * (tri + trr) * np.exp(-0.5 * w))
                   / (-np.expm1(-2.0 * w)))
            tot += half * float(np.dot(_GW96, val))
        out[i] = (-(core.EULER + core.LOG_PI) * tri_s + 2.0 * tot
                  + tri_s * (-math.log1p(-math.exp(-2.0 * W))))
    return out


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE FLOOR-THEOREM ASSEMBLY -- three pieces, honest grades")
    print("(prime_floor_theorem_probe, exploration only, no RH claim)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- rebuild (parent machinery)")
    gam, n_rvm = pp.zero_list()
    check("S0.Z zero list: %d zeros to T = %.0f (RvM dev %.2f <= 3)"
          % (len(gam), zp.T_SCAN, abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    KZ = core.frame_a_zones()
    L15 = len(KZ)
    fam5 = [0, (L15 - 1) // 4, L15 // 2, (3 * (L15 - 1)) // 4, L15 - 1]
    inter = []
    for (lo_i, hi_i), n_in in zip(zip(fam5[:-1], fam5[1:]), (2, 3, 3, 2)):
        for j in range(1, n_in + 1):
            inter.append(lo_i + j * (hi_i - lo_i) // (n_in + 1))
    idx15 = sorted(set(fam5 + inter))
    wins = [lg.lock_block(KZ[i]) for i in idx15]
    wins = [w for w in wins if w["complete"]]
    wins.sort(key=lambda w: w["alpha"])
    g1 = float(gam[0])
    for w in wins:
        a, b, meta = pp.components_of(w, gam)
        M2 = np.array([[float(a @ a), float(a @ b)],
                       [float(a @ b), float(b @ b)]])
        x = a[0] * b[-1] - a[-1] * b[0]
        w.update(a=a, b=b, meta=meta, M2=M2,
                 det_m2=float(np.linalg.det(M2)),
                 det_a2=float(np.linalg.det(w["A2"])),
                 x2=float(x * x))
    print("    %d windows; gamma_1 = %.15f (cache; |cache - "
          "zetazero(1)| = 5.3e-15 measured in the parent probe)"
          % (len(wins), g1))

    # ========================================================== PIECE 1
    print("\nP1 -- PSD REMAINDER AS THEOREM (citation band + explicit "
          "deep envelope)")
    print("    %5s %6s | %9s %9s %9s | %9s %11s | %6s %9s"
          % ("h", "alpha", "eps_deep", "eps_arch", "eps_f", "pert",
             "X^2", "close?", "T_need"))
    n_close, close_flags = 0, []
    for w in wins:
        D, hz, Mz, al = w["D"], w["h"], w["M"], w["alpha"]
        jj = np.arange(hz)
        t1v = parity_t(1, hz)
        t2v = parity_t(2, hz)
        grow = np.exp((hz - jj - 0.5) * D * DELTA_OFF)
        E1 = 2.0 * float(np.abs(t1v) @ grow)
        E2 = 2.0 * float(np.abs(t2v) @ grow)
        ee = max(E1 * E1, E1 * E2, E2 * E2)
        ch2 = math.cosh(D / 4.0) ** 2
        eps_deep = 4.0 * ch2 * ee / D \
            * (math.log(T_RH) + 1.0) / (math.pi * T_RH)
        # master-identity defect: measured GL-48 -> GL-96 arch shift
        c48 = core.arch_lags(Mz, D)
        c96_idx = np.arange(Mz) * D
        c96 = arch_A_fine(c96_idx, D)
        dc = c96 - c48
        W11 = core.lag_weights_from_v(t1v, hz)
        W22 = core.lag_weights_from_v(t2v, hz)
        Wpp = core.lag_weights_from_v(t1v + t2v, hz)
        W12 = 0.5 * (Wpp - W11 - W22)
        dA2 = max(abs(float(dc @ W11)), abs(float(dc @ W22)),
                  abs(float(dc @ W12)))
        eps_arch = ARCH_SLACK * dA2
        eps_f = CHAIN_FAC * EPSM * float(np.linalg.norm(w["A2"])) ** 2
        eps = eps_deep + eps_arch + eps_f
        s1 = (abs(w["A2"][0, 0]) + abs(w["A2"][1, 1])
              + 2.0 * abs(w["A2"][0, 1]))
        pert = eps * s1 + 2.0 * eps * eps
        close = pert < w["x2"]
        close_flags.append(close)
        n_close += int(close)
        t_need = float("nan")
        if not close:
            # smallest citation horizon that would close this rung
            tt = T_RH
            for _ in range(400):
                tt *= 1.25
                e_d = 4.0 * ch2 * ee / D \
                    * (math.log(tt) + 1.0) / (math.pi * tt)
                e_t = e_d + eps_arch + eps_f
                if e_t * s1 + 2.0 * e_t * e_t < w["x2"]:
                    t_need = tt
                    break
        w.update(pert=pert, eps_deep=eps_deep, eps_arch=eps_arch,
                 p1_close=close, t_need=t_need)
        print("    %5d %6.3f | %9.2e %9.2e %9.2e | %9.2e %11.4e | "
              "%6s %9s"
              % (hz, al, eps_deep, eps_arch, eps_f, pert, w["x2"],
                 "yes" if close else "NO",
                 ("-" if close else "%.1e" % t_need)))
    p1_uniform = n_close == len(wins)
    if p1_uniform:
        p1_grade = "UNIFORM-VERIFIED"
    elif n_close > 0:
        p1_grade = "PER-RUNG-ONLY (beyond h of rung %d)" \
            % ([w["h"] for w, c in zip(wins, close_flags) if c][-1])
    else:
        p1_grade = "PER-RUNG-ONLY (envelope never closes)"
    check("P1.CLOSE the citation-grade chain pert < X^2 closes on "
          "%d/%d rungs -- %s; the deep envelope uses ONLY the [A1] "
          "strip + the cited on-line depth (no zero-location input); "
          "where it fails, the printed T_need is the exact "
          "citation-depth re-entry point"
          % (n_close, len(wins), p1_grade), n_close > 0)

    # ========================================================== PIECE 2
    print("\nP2 -- UNIFORM h-ASYMPTOTIC of the fixed pair")
    # ward 1: closed form == direct sum on all rungs
    cf_dev = 0.0
    for w in wins:
        for k in (1, 2):
            sc = S_closed(k, w["h"], w["D"], g1)
            sd = S_direct(k, w["h"], w["D"], g1)
            cf_dev = max(cf_dev, abs(sc - sd) / max(abs(sd), 1e-12))
    check("P2.CF the Dirichlet closed form of S_k equals the direct "
          "sum on all rungs (max rel dev %.1e <= %.0e)"
          % (cf_dev, WARD_CF), cf_dev <= WARD_CF)
    # ward 2: the closed-form pipeline reproduces the measured X^2
    pipe_dev = max(abs(pair_x2_closed(w["alpha"], w["h"], g1)[0]
                       - w["x2"]) / w["x2"] for w in wins)
    check("P2.PIPE the closed-form pair pipeline reproduces the "
          "deployed X^2 on all rungs (max rel dev %.1e <= 1e-6)"
          % pipe_dev, pipe_dev <= 1e-6)
    # synthetic h-ladder study AT EACH DEPLOYED alpha: the 1/h
    # correction constant C(alpha) (it blows up near the sin-nodes),
    # sign stability in h, and the per-alpha uniform bound
    print("    synthetic h-ladders at the deployed alphas "
          "(h in %d..%d):" % (SYN_HS[0], SYN_HS[-1]))
    print("    %5s %6s | %8s %8s | %10s %10s | %6s %6s"
          % ("h", "alpha", "C(alpha)", "h0", "L(h)", "X^2",
             "in-dom", "L<=X2"))
    flips, lim_ok, lh_ok, n_dom = 0, True, True, 0
    for w in wins:
        al = w["alpha"]
        xi = x_inf(al, g1)
        c_al, signs = 0.0, []
        for h_s in SYN_HS:
            x2s, xs = pair_x2_closed(al, h_s, g1)
            c_al = max(c_al, h_s * abs(x2s / xi ** 2 - 1.0))
            signs.append(math.copysign(1.0, xs))
        flips += sum(1 for s0, s1_ in zip(signs[:-1], signs[1:])
                     if s0 != s1_)
        c_al *= C_SLACK
        h0_al = c_al
        dev_h = abs(w["x2"] / xi ** 2 - 1.0) * w["h"]
        lim_ok = lim_ok and dev_h <= c_al
        lh = xi ** 2 * (1.0 - c_al / w["h"])
        in_dom = w["h"] > h0_al
        if in_dom:
            n_dom += 1
            lh_ok = lh_ok and (lh <= w["x2"]) and lh > 0.0
        w.update(lh=lh, c_al=c_al, h0_al=h0_al, in_dom=in_dom)
        print("    %5d %6.3f | %8.1f %8.0f | %10.3e %10.4e | "
              "%6s %6s"
              % (w["h"], al, c_al, h0_al, lh, w["x2"],
                 "yes" if in_dom else "no",
                 "ok" if (not in_dom or lh <= w["x2"]) else "NO"))
    check("P2.SIGN no sign flips of X in h at fixed alpha on the "
          "synthetic ladders (%d flips over 14 alphas x %d h) -- "
          "the KILL branch does NOT fire in h"
          % (flips, len(SYN_HS)), flips == 0)
    check("P2.LIM the ANALYTIC limit X_inf^2(alpha) matches the "
          "deployed X^2 within the per-alpha measured 1/h "
          "correction (x%.0f slack) on all rungs" % C_SLACK, lim_ok)
    small = [w["h"] for w in wins if not w["in_dom"]]
    c_l = max(w["c_al"] for w in wins)
    h0 = max(w["h0_al"] for w in wins)
    check("P2.L(h) the per-alpha uniform bound L(h) = "
          "X_inf^2(alpha)(1 - C(alpha)/h) is positive and below "
          "the measured X^2 on every rung in its explicit domain "
          "h > h0(alpha) (%d/%d rungs in-domain; excluded small "
          "rungs %s stand on the per-rung certificate) (CT3 ward)"
          % (n_dom, len(wins), small), lh_ok and n_dom >= 10)
    # the alpha-node structure (typed, the honest limitation)
    aa = np.linspace(ALPHA_LO, ALPHA_HI, N_GRID)
    xg = np.array([x_inf(al, g1) ** 2 for al in aa])
    thr = 1e-3 * float(np.median(xg))
    nodes = int(np.sum((xg[1:-1] < xg[:-2]) & (xg[1:-1] < xg[2:])
                       & (xg[1:-1] < thr)))
    min_sin = min(abs(math.sin(w["alpha"] * g1)) for w in wins)
    print("    ALPHA-NODES (typed): X_inf^2 has %d near-zeros on "
          "alpha in [%.0f, %.0f] (sin(alpha gamma_1) nodes, spacing "
          "pi/gamma_1 = %.4f); deployed rungs keep |sin| >= %.3f -- "
          "the fixed pair is h-UNIFORM per rung but NOT "
          "ladder-uniform in alpha; at nodes the family takes over"
          % (nodes, ALPHA_LO, ALPHA_HI, math.pi / g1, min_sin))
    p2_grade = ("UNIFORM-VERIFIED (per-alpha, h > h0(alpha) <= %.0f)"
                % h0
                if (cf_dev <= WARD_CF and pipe_dev <= 1e-6
                    and lim_ok and flips == 0
                    and lh_ok and n_dom >= 10) else "PER-RUNG-ONLY")

    # ========================================================== PIECE 3
    print("\nP3 -- FAMILY EXTENSION (pole x zeros)")
    print("    %5s %6s | %8s %8s %8s | %8s %8s | %8s"
          % ("h", "alpha", "fam/pt", "cert100", "cert/fl", "zz/pt",
             "residue", "med_alias"))
    fam_ok, res_list, cert_fracs, lam_r_min = True, [], [], np.inf
    for w in wins:
        a, b = w["a"], w["b"]
        x_pz = a[:-1] * b[-1] - b[:-1] * a[-1]
        fam_tot = float(np.sum(x_pz ** 2))
        fam_share_pt = fam_tot / w["det_m2"]
        zz_share = 1.0 - fam_share_pt
        top = np.sort(x_pz ** 2)[::-1]
        cert100 = float(np.sum(top[:K_FAM]))
        # per-rung chain (the PAIR-CERTIFIED grade): psd remainder
        # verified per rung + the float budget -- NOT piece 1's
        # citation-grade pert (that distinction is piece 1's grade)
        lam_r = eig2_min(w["A2"] - w["M2"])
        lam_r_min = min(lam_r_min, lam_r)
        bud_pr = CHAIN_FAC * EPSM * (
            float(np.linalg.norm(w["A2"])) ** 2
            + float(np.linalg.norm(w["M2"])) ** 2)
        cert_frac = (cert100 - bud_pr) / w["det_a2"]
        residue = 1.0 - w["det_m2"] / w["det_a2"]
        res_list.append(residue)
        cert_fracs.append(cert_frac)
        fam_ok = fam_ok and fam_share_pt >= FAM_PAIR_TOT
        # alias identity of the top-10 family carriers
        idx10 = np.argsort(x_pz ** 2)[::-1][:10]
        r = gam[idx10] * w["D"] / (2.0 * math.pi)
        med_alias = float(np.median(np.abs(r - np.round(r))))
        print("    %5d %6.3f | %8.5f %8.5f %8.4f | %8.1e %8.4f | "
              "%8.4f"
              % (w["h"], w["alpha"], fam_share_pt,
                 cert100 / w["det_m2"], cert_frac, zz_share,
                 residue, med_alias))
    sl_res = float(np.polyfit(np.log([w["h"] for w in wins]),
                              res_list, 1)[0])
    exhaust = (max(res_list) <= RES_MAX
               and sl_res <= RES_SLOPE_MAX and fam_ok)
    check("P3.EXH the pole family carries >= %.3f of the pair total "
          "on every rung; the residue (the >2e4 remainder's det "
          "share) is %.4f..%.4f with trend slope %+.3f vs log h "
          "(bars %.2f / %.2f) -- %s"
          % (FAM_PAIR_TOT, min(res_list), max(res_list), sl_res,
             RES_MAX, RES_SLOPE_MAX,
             "EXHAUSTION: the floor reduces to pieces 1+2 plus the "
             "family sum" if exhaust else
             "persistent residue (typed)"), exhaust)
    check("P3.CERT the certified top-%d family bound (per-rung "
          "chain: lambda_min(R) = %.1e >= 0 on all rungs, float "
          "budget only) carries a median %.3f of the floor (bar >= "
          "%.2f; min %.3f), all carriers on-line by computation"
          % (K_FAM, lam_r_min, float(np.median(cert_fracs)),
             FAM_CERT_MED, min(cert_fracs)),
          float(np.median(cert_fracs)) >= FAM_CERT_MED
          and lam_r_min >= 0.0)
    # the family limit across the fixed-pair nodes
    gz_lim = np.asarray(gam[:N_ZLIM], dtype=float)
    f_min, f_min_al = float("inf"), float("nan")
    for al in aa[::4]:
        u = al * gz_lim
        pi2 = math.pi ** 2
        a24 = 0.25 * al * al
        br = (1.0 / ((pi2 - u * u) * (4.0 * pi2 + a24))
              - 1.0 / ((4.0 * pi2 - u * u) * (pi2 + a24)))
        xv = (16.0 * al * pi2 * np.sin(u)
              * math.sinh(0.5 * al) * br)
        fv = float(np.sum(xv * xv))
        if fv < f_min:
            f_min, f_min_al = fv, float(al)
    check("P3.FAM-LIM the ANALYTIC family limit F_inf(alpha) = "
          "sum_k X_inf^2(gamma_k) stays positive across the "
          "fixed-pair nodes (min %.3e at alpha = %.2f > 0): the "
          "family never dies simultaneously" % (f_min, f_min_al),
          f_min > 0.0)
    p3_grade = ("UNIFORM-VERIFIED" if (exhaust and f_min > 0.0
                and float(np.median(cert_fracs)) >= FAM_CERT_MED)
                else "PER-RUNG-ONLY")

    # ========================================================== CONTROLS
    print("\nCT -- controls")
    w_mid = wins[len(wins) // 2]
    D, hz = w_mid["D"], w_mid["h"]
    jj = np.arange(hz)
    worst_rel, n_detneg, env_ok = 0.0, 0, True
    for gs, de in CT1_GRID:
        zc = complex(gs, de)
        L_off = np.empty((2, 2))
        pairs = {(0, 0): (w_mid["f1"], w_mid["f1"]),
                 (1, 1): (w_mid["f2"], w_mid["f2"]),
                 (0, 1): (w_mid["f1"], w_mid["f2"])}
        for (i, j), (fa, fb) in pairs.items():
            tp = lg.T_pair(fa, fb, D, np.array([zc, np.conj(zc)]))
            L_off[i, j] = L_off[j, i] = float(np.real(np.sum(tp)))
        sc = float(np.max(np.abs(L_off)))
        worst_rel = min(worst_rel, eig2_min(L_off) / sc)
        n_detneg += int(float(np.linalg.det(L_off)) < 0.0)
        grow_s = np.exp((hz - jj - 0.5) * D * de)
        E1s = 2.0 * float(np.abs(parity_t(1, hz)) @ grow_s)
        E2s = 2.0 * float(np.abs(parity_t(2, hz)) @ grow_s)
        env = 8.0 * math.cosh(D / 4.0) ** 2 \
            * max(E1s * E1s, E1s * E2s, E2s * E2s) / (D * gs * gs)
        env_ok = env_ok and sc <= env
    check("CT1 [must-fire] synthetic OFF-line pairs (grid %s) break "
          "the psd chain exactly at the off-line locus: det < 0 on "
          "%d/%d configurations (the structural signature) and the "
          "worst min-eig/scale = %.2f <= %.0e; all layers respect "
          "the piece-1 envelope: %s"
          % (str(CT1_GRID), n_detneg, len(CT1_GRID), worst_rel,
             CT1_NEG, "ok" if env_ok else "VIOLATED"),
          n_detneg == len(CT1_GRID) and worst_rel <= CT1_NEG
          and env_ok)
    lam_scr = []
    for si in (0, len(wins) // 2, len(wins) - 1):
        w = wins[si]
        rr_s = core.build_window(w["kz"], scramble_seed=SCRAMBLE_SEED)
        lam_scr.append(eig2_min(rr_s["Ah_dir"] - w["M2"]))
    check("CT2 [must-fire] scramble kills the family/identity "
          "structure: lambda_min(R_scr) = %.1f..%.1f < 0 (the psd "
          "chain refuses the scrambled comb)"
          % (min(lam_scr), max(lam_scr)), max(lam_scr) < 0.0)

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- synthesis: the theorem-status table + verdict")
    print("=" * 78)
    grades = {"P1 psd remainder": p1_grade,
              "P2 uniform h-asymptotic": p2_grade,
              "P3 family extension": p3_grade}
    all_uniform = all(g.startswith("UNIFORM") for g in grades.values())
    any_dead = any(g == "DEAD" for g in grades.values())
    if all_uniform:
        verdict = "FLOOR-SKELETON-COMPLETE"
    elif any_dead:
        verdict = "FLOOR-BLOCKED"
    else:
        verdict = "FLOOR-PARTIAL"
    print("\n  THEOREM-STATUS TABLE:")
    for k_, v_ in grades.items():
        print("    %-28s %s" % (k_, v_))
    hs_close = [w["h"] for w, c in zip(wins, close_flags) if c]
    print("""
  VERDICT: %s

  STRONGEST SUPPORTED FLOOR ASSERTION (verbatim):
    'On every rung of the deployed ladder, lambda tau = det Ahat2
     >= sum over the top-%d (pole x zero) pairs of X_k^2 minus the
     explicit budget pert(h): a certified %.2f..%.2f of the floor,
     all carriers on-line by verified computation (<= 2e4).  The
     fixed pair (pole, gamma_1) satisfies X^2(alpha, h) >=
     X_inf^2(alpha)(1 - C(alpha)/h) for h > h0(alpha) = C(alpha)
     (measured C(alpha) <= %.1f, worst h0 = %.0f), X_inf ANALYTIC
     (= 16 alpha pi^2 sin(alpha gamma_1) sinh(alpha/2) [bracket]);
     h-uniform at every deployed alpha in-domain.  The chain
     upgrades from per-rung eigencheck to
     citation-grade (strip + on-line depth only) on rungs with h <=
     %s, where the deep-tail envelope closes: pert < X^2.'

  THE SINGLE SEPARATING OBJECT from tau > 0 for all h:
    the deep-tail envelope grows ~ h e^alpha against the FIXED
    citation horizon T_RH = 3e12 -- beyond the printed T_need the
    psd of the remainder needs verified on-line DEPTH (never
    location outside the strip); plus the alpha-nodes of the fixed
    pair, where the certified brick must hand over to the family
    (P3: the analytic family limit stays positive, min %.1e).
    HONESTY: floor positivity on the deployed battery is
    NECESSARY-side evidence, NOT RH; the detector-inversion
    direction is where floor bounds convert to zero-exclusion.
""" % (verdict, K_FAM, min(cert_fracs), max(cert_fracs), c_l, h0,
       (str(max(hs_close)) if hs_close else "NONE"), f_min))

    dt = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim; exploration only; nothing outside "
          "experiments/ touched.")


if __name__ == "__main__":
    run()
