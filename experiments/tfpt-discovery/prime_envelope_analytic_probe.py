#!/usr/bin/env python3
"""prime_envelope_analytic_probe -- from measured to proven: can the
analytic h- and X-asymptotic of the certified FAMILY SUM be derived
from the closed forms, yielding an analytic lower bound of envelope
type rho(X) >= c h^{-3/2}?

EXPLORATION ONLY (experiments/): no verification claim, no ledger row,
no paper edit.  NO RH claim anywhere -- the mandatory logical-status
typing is in S4.  Frozen before running.

CONTEXT.  The certified pole x alias family carries the floor
(per-rung 0.977..0.981 at depth, citation-grade >= 0.868 to
alpha = 12.75); the fixed pair has the fully analytic limit
X_inf(alpha, gamma) = 16 alpha pi^2 sin(alpha gamma) sinh(alpha/2)
[bracket] (Piece 2, UNIFORM-VERIFIED); the measured envelope
rho >= c h^{-3/2}, c ~ 4.85, is kill-tested to X = 25.5 but PROVEN
nowhere.  KEY INSTRUMENT FACT: the family sum is a pure ZERO-SIDE
object (frames + zero list) -- no sieve is needed for items 1-3; the
73-point envelope ward uses the freshly rebuilt 67-rung v818 ladder
plus the six deep rungs' frozen cited values.

THE FAMILY CLOSED FORM (item 1, exact at every finite h):
    X(gamma) = 2 sqrt(w) [S_1(gamma) p_2 - S_2(gamma) p_1],
    w = D csinc^2(gamma D / 2),
    S_k  = Dirichlet closed form (ft.S_closed; exact == direct sum),
    p_k  = cp sum_j t_k[j] sinh((h-j-1/2) D/2),
           cp = 2 sqrt(D) sinh(D/4)/(D/4),
    F(h, D) = sum_zeros X(gamma)^2   (the certified family sum).
THE ALIAS LAW (item 1, k-dependence; gamma = (2 pi m + delta)/D):
    w = D sin^2(delta/2)/(pi m + delta/2)^2   [exact, m integer],
    |S_k| <= (2/sqrt(N)) / |sin((om +- delta)/2)|  (Dirichlet peak),
    so the sin(delta/2) CANCELS in the mean square:
    E[X^2 | cell m] ~ (2D/(pi^2 m^2 N)) (p_1^2 + p_2^2)  -- every
    zero of alias cell m contributes at the same order, 1/m^2 law,
    N_m ~ log(m/D)/D zeros per cell.  Summing cells and dividing by
    lambda ~ p_1^2 + p_2^2 (the pole carries the top eigenvector):
    TAU LAW (derived, leading order, random-phase constants):
      tau ~ kappa * shape(h, D),
      shape = (2/(pi^2 (2h+1))) sum_m log(m/D)/m^2   [~ 1/h].
THE ENVELOPE DECOMPOSITION (item 2):
      rho = tau / tau_pnt ~ kappa shape(h, D) / tau_pnt(h),
    so the -3/2 splits as: -1 (derived, the alias/weight/
    normalization conspiracy above) + log-drift (derived shape)
    - slope(tau_pnt) (MEASURED, instrument side); the envelope
    rho >= c h^{-3/2} holds iff tau_pnt grows slower than h^{1/2}.

MACHINE-CHECKED DERIVATION STEPS (S2; sympy where algebraic, high-h
convergence wards where analytic limits):
  A1 sympy: 8 alpha [G1 Gp2 - G2 Gp1] == 16 alpha pi^2 sin(u)
     sinh(alpha/2) [bracket]  (the Piece-2 identity, exact algebra).
  A2 sympy: u^2 [bracket] -> 3 pi^2/((pi^2+a^2/4)(4pi^2+a^2/4)) as
     u -> inf  (the large-u simplification).
  A3 sympy: X_inf alpha^5 gamma^2/(sinh(alpha/2) sin(alpha gamma))
     -> 192 pi^4 (4 gamma^2 + 1)/gamma^2 as alpha -> inf (exact;
     -> 768 pi^4 for gamma >> 1)  (the deep-alpha law).
  A4 sympy: sin^2(pi m + d/2) == sin^2(d/2), m integer  (alias
     weight).
  A5 numeric: pole legs p_k/(2 sqrt(2 alpha)) -> Gp_k(alpha) =
     pi k sinh(alpha/2)/(pi^2 k^2 + alpha^2/4), rel <= 5e-3 at
     h = 2^15, k-consistency <= 1e-3.
  A6 numeric: the composite pair X^2 -> X_inf^2 with 1/h rate
     (dev <= 0.1 at h = 2^15 AND h-doubling halves it, ratio in
     [1.5, 2.5]).
  A7 numeric (alias census at the deepest frame): fit of
     log(cell-mean X^2 * m^2) vs log m has |slope| <= 0.4; cell
     counts match log(m/D)/D within 20% (median).
  A8 numeric (h-law at fixed alpha): F(h, alpha) -> F_inf(alpha)
     with |fit exponent| <= 0.1 over h = 2^9..2^14; the subleading
     |F - F_inf| ~ h^-q, q in [0.5, 1.5] (typed).
  A9 numeric (tower law): tau_zero = det(M2)/lambda(M2) on the
     D = 1/64 tower h = 588..816: fit slope in [-1.35, -0.65]
     (the derived -1).
  A10 numeric (73-point shape fit): kappa_r = tau_r/shape_r on the
     deployed battery; on the alpha >= 4.5 subset (predeclared: the
     alias regime; the low-alpha mixed regime typed separately)
     |slope of log kappa vs log h| <= 0.25 and R^2(log tau vs
     log shape) >= 0.85.
THE LOWER-BOUND ATTEMPT (item 3): the explicit candidate
      rho(X) >= rho_certfam(X) >= c_cert h^{-3/2}
  with c_cert = min over the 73 points of rho_certfam h^{3/2}
  (explicit number; certified-family route, citation-grade error
  terms frozen in the parent probes), PASS iff additionally the
  certified envelope e1_cert = rho_certfam h^{3/2} is non-decaying
  (fit slope >= -0.02) and the phase floor survives (below).
PHASE-CONSPIRACY SCAN (item 3 kill): the detrended family sum
  G(alpha) = F(alpha; h = 512)/sinh^2(alpha/2), residuals of the
  log-log fit over alpha in [2, 12.75] (1076 points): KILL iff
  exp(min residual - median residual) < 0.03 (a conspiracy dip) --
  plus the deployed-battery minimum of the certified share (typed).
VERDICT (frozen): ENVELOPE-OSCILLATION-KILLED iff the phase ward
  fails; else ENVELOPE-THEOREM-CANDIDATE iff W1 (closed form,
  1e-5 vs components; <= 5%% task bar vs cited), A1-A7, A9, A10,
  W3 (73-point envelope + non-decay) all pass (A8 subleading soft,
  typed); else ENVELOPE-ASYMPTOTIC-PARTIAL typed by piece.

CONTROLS: W1 analytic-vs-numeric (all 73 frames); the phase scan;
scramble has NO analytic form -- the family structure is
comb-specific; measured evidence restated from the parent probes
(lambda_min(A2_scr - M2) = -3.794e+03, det -> -2.1e+02 at M = 1176,
seed 7): the closed forms above are theorems about the Dirichlet
kernels of THIS comb, and the scrambled comb refuses the psd chain.

FIREWALL: v563 / v692 / parent probes READ-ONLY; zero values used
openly (on-line by computation <= 2e4 via the parent's RS scan); NO
RNG anywhere in this probe.  Report only, nothing written.
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
import prime_lagrange_pair_probe as pp       # noqa: E402 (READ-ONLY)
import prime_floor_theorem_probe as ft       # noqa: E402 (READ-ONLY)
import prime_tail_envelope_probe as tp       # noqa: E402 (READ-ONLY)
import floor_envelope_depth_probe as fdp     # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
DGRID = fdp.DGRID
DEEP_MS = (1176, 1326, 1414, 1504, 1588, 1632)
K_FAM = ft.K_FAM
CF_BAR = 1.0e-5             # closed form vs components (all 73)
CITED_BAR = 2.0e-2          # vs the 3-4 sig cited deep values
PAIR_CITED_BAR = 5.0e-2     # pair vs cited (3 cited values combined)
TASK_BAR = 5.0e-2           # the item-1 5% bar (analytic vs certified)
LIM_H = 1 << 15             # A5/A6 convergence rung
LIM_ALPHA = 4.489           # A5/A6/A8 anchor alpha (deployed value)
A5_REL = 5.0e-3
A5_KCONS = 1.0e-3
A6_DEV = 0.10
A6_RATIO = (1.5, 2.5)
A7_SLOPE = 0.40
A7_COUNT = 0.20
A7_M_RANGE = (2, 45)
A7_MIN_CELL = 8
A8_HS = (512, 1024, 2048, 4096, 8192, 16384)
A8_EXP = 0.10
A8_Q = (0.5, 1.5)           # soft, typed
A9_SLOPE = (-1.35, -0.65)
A10_ALPHA_MIN = 4.5         # predeclared alias-regime subset
A10_KSLOPE = 0.25
A10_R2 = 0.85
ENV_SLOPE_MIN = -0.02
PHASE_H = 512
PHASE_N = 1076
PHASE_RANGE = (2.0, 12.75)
PHASE_FLOOR = 0.03
C_CONTRACT = 4.85           # the deployed contract constant (context)
# frozen cited deep values (prime_family_depth_probe, 2026-08-06):
CITED = {
    1176: dict(rho=1.959e-3, cert=1.52e-1, rho_cf=1.915e-3,
               rho_cp=4.876e-5),
    1326: dict(rho=1.773e-3, cert=2.98e-1, rho_cf=1.733e-3,
               rho_cp=3.243e-5),
    1414: dict(rho=1.684e-3, cert=4.49e-1, rho_cf=1.645e-3,
               rho_cp=1.765e-5),
    1504: dict(rho=1.683e-3, cert=7.27e-1, rho_cf=1.646e-3,
               rho_cp=2.502e-6),
    1588: dict(rho=1.770e-3, cert=1.21e0, rho_cf=1.735e-3,
               rho_cp=4.378e-6),
    1632: dict(rho=1.855e-3, cert=1.62e0, rho_cf=1.820e-3,
               rho_cp=1.830e-5),
}
EPSM = float(np.finfo(float).eps)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def s_vec(k, h, phi):
    """Vectorized Dirichlet closed form S_k at real phi (with the
    degenerate-denominator fallback to ft.S_closed)."""
    out = tp.S_closed_c(k, h, np.asarray(phi, dtype=complex))
    outr = np.real(out)
    bad = ~np.isfinite(outr)
    if bad.any():
        D_eff = 1.0
        for i in np.nonzero(bad)[0]:
            outr[i] = ft.S_closed(k, h, D_eff, float(phi[i]))
    return outr


def fam_closed(h, D, gam):
    """The exact closed-form family: per-zero X(gamma), the legs."""
    phi = D * gam
    wg = D * np.real(fdp.csinc(np.asarray(phi, complex) / 2.0) ** 2)
    S1 = s_vec(1, h, phi)
    S2 = s_vec(2, h, phi)
    rt = 2.0 * np.sqrt(np.maximum(wg, 0.0))
    av, bv = rt * S1, rt * S2
    jj = np.arange(h)
    ee = np.sinh((h - jj - 0.5) * D / 2.0)
    sp1 = float(ft.parity_t(1, h) @ ee)
    sp2 = float(ft.parity_t(2, h) @ ee)
    cp = 2.0 * math.sqrt(D) * (math.sinh(D / 4.0) / (D / 4.0))
    p1, p2 = cp * sp1, cp * sp2
    Xv = av * p2 - bv * p1
    return Xv, av, bv, p1, p2


def m2_closed(h, D, gam):
    """Zero-side 2x2 gram (zeros + pole) from the closed forms."""
    Xv, av, bv, p1, p2 = fam_closed(h, D, gam)
    M2 = np.array([[float(av @ av) + p1 * p1,
                    float(av @ bv) + p1 * p2],
                   [float(av @ bv) + p1 * p2,
                    float(bv @ bv) + p2 * p2]])
    lam, tau, _, _ = fdp.eig2(M2)
    return Xv, M2, lam, tau


def shape_of(h, D):
    """The derived tau law shape (2/(pi^2 N)) sum_m log(m/D)/m^2."""
    m_max = int(math.floor(2.0e4 * D / (2.0 * math.pi)))
    if m_max < 1:
        return float("nan")
    mm = np.arange(1, m_max + 1, dtype=float)
    return (2.0 / (math.pi ** 2 * (2 * h + 1))) \
        * float(np.sum(np.log(mm / D) / mm ** 2))


def gp_k(k, al):
    return math.pi * k * math.sinh(al / 2.0) \
        / (math.pi ** 2 * k * k + al * al / 4.0)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE ANALYTIC ENVELOPE ATTEMPT -- family closed form -> "
          "asymptotic -> lower bound")
    print("(prime_envelope_analytic_probe, exploration only, "
          "no RH claim)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- sympy machine checks of the algebraic steps")
    import sympy as sp
    u, al, g, d = sp.symbols("u alpha gamma delta", positive=True)
    m_i = sp.Symbol("m", integer=True, positive=True)
    G1 = sp.pi * sp.sin(u) / (sp.pi ** 2 - u ** 2)
    G2 = 2 * sp.pi * sp.sin(u) / (4 * sp.pi ** 2 - u ** 2)
    Gp1 = sp.pi * sp.sinh(al / 2) / (sp.pi ** 2 + al ** 2 / 4)
    Gp2 = 2 * sp.pi * sp.sinh(al / 2) / (4 * sp.pi ** 2 + al ** 2 / 4)
    br = (1 / ((sp.pi ** 2 - u ** 2) * (4 * sp.pi ** 2 + al ** 2 / 4))
          - 1 / ((4 * sp.pi ** 2 - u ** 2)
                 * (sp.pi ** 2 + al ** 2 / 4)))
    a1 = sp.simplify(8 * al * (G1 * Gp2 - G2 * Gp1)
                     - 16 * al * sp.pi ** 2 * sp.sin(u)
                     * sp.sinh(al / 2) * br)
    check("A1.SYM the Piece-2 identity 8a[G1 Gp2 - G2 Gp1] == "
          "16 a pi^2 sin(u) sinh(a/2)[bracket] (exact algebra)",
          a1 == 0)
    a2 = sp.limit(br * u ** 2, u, sp.oo)
    a2_ref = 3 * sp.pi ** 2 / ((sp.pi ** 2 + al ** 2 / 4)
                               * (4 * sp.pi ** 2 + al ** 2 / 4))
    check("A2.SYM u^2 [bracket] -> 3 pi^2/((pi^2+a^2/4)(4pi^2+a^2/4)) "
          "(large-u law)", sp.simplify(a2 - a2_ref) == 0)
    a3 = sp.limit(16 * al ** 6 * sp.pi ** 2 * g ** 2
                  * br.subs(u, al * g), al, sp.oo)
    a3_ref = 192 * sp.pi ** 4 * (4 * g ** 2 + 1) / g ** 2
    check("A3.SYM the deep-alpha law: X_inf alpha^5 gamma^2 / "
          "(sinh(a/2) sin(a g)) -> 192 pi^4 (4 g^2 + 1)/g^2 "
          "(-> 768 pi^4 for g >> 1; exact iterated limit)",
          sp.simplify(a3 - a3_ref) == 0)
    a4 = sp.simplify(sp.expand_trig(sp.sin(sp.pi * m_i + d / 2) ** 2)
                     - sp.sin(d / 2) ** 2)
    check("A4.SYM the alias weight sin^2(pi m + d/2) == sin^2(d/2), "
          "m integer (the csinc-null cancellation)", a4 == 0)

    # ============================================================== S1
    print("\nS1 -- the family closed form on the deployed battery "
          "(zero-side; no sieve needed)")
    gam, n_rvm = pp.zero_list()
    check("S1.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    g1 = float(gam[0])
    # the 67-rung v818 ladder (frames + rho, v818 part-2 recipe)
    t0 = time.time()
    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == fdp.ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        lam, tau, _, _ = fdp.eig2(rr["Ah"])
        edges, reads = fdp.pnt_cells(rr["W11"], rr["W22"], rr["W12"],
                                     rr["D"], rr["M"],
                                     2.0 * rr["alpha"] + 1e-9)
        Sp = fdp.pnt_S_of(edges, reads, 2.0 * rr["alpha"])
        _, tau_p, _, _ = fdp.eig2(rr["B"] - Sp)
        rows.append(dict(h=rr["h"], M=rr["M"], D=rr["D"],
                         alpha=rr["alpha"], t1=rr["t1"], t2=rr["t2"],
                         lam=lam, tau=tau, tau_pnt=tau_p,
                         rho=tau / tau_p, deep=False))
    rows.sort(key=lambda w: w["alpha"])
    check("S1.SET the deployed 67-rung ladder rebuilt (%d windows, "
          "%.0f s); e1 range [%.2f, %.1f] vs promoted [4.85, 24.2]"
          % (len(rows), time.time() - t0,
             min(w["rho"] * w["h"] ** 1.5 for w in rows),
             max(w["rho"] * w["h"] ** 1.5 for w in rows)),
          len(rows) == 67
          and abs(min(w["rho"] * w["h"] ** 1.5 for w in rows)
                  - 4.85) <= 0.02
          and abs(max(w["rho"] * w["h"] ** 1.5 for w in rows)
                  - 24.2) <= 0.1)
    # the six deep tower frames (cited normalizations)
    for M in DEEP_MS:
        h = M // 2
        Tb = core.parity_basis(h, 2)
        ct = CITED[M]
        lam_tp = ct["cert"] / ct["rho_cf"]      # lambda tau_pnt
        rows.append(dict(h=h, M=M, D=DGRID, alpha=h * DGRID,
                         t1=Tb[0].copy(), t2=Tb[1].copy(),
                         lam=float("nan"), tau=float("nan"),
                         tau_pnt=float("nan"), rho=ct["rho"],
                         lam_taupnt=lam_tp, deep=True))
    print("    73-point battery: 67 v818 rungs (alpha %.2f..%.2f) + "
          "6 tower rungs (alpha %.2f..%.2f, cited normalizations)"
          % (rows[0]["alpha"], rows[66]["alpha"],
             rows[67]["alpha"], rows[-1]["alpha"]))

    # closed form vs components on all 73 (the item-1 ward)
    print("    closed-form vs component family sums (all 73 frames):")
    worst_cf, worst_c100 = 0.0, 0.0
    t0 = time.time()
    for w in rows:
        h, D, M = w["h"], w["D"], w["M"]
        Xv, M2, lamz, tauz = m2_closed(h, D, gam)
        x2 = Xv ** 2
        order = np.argsort(x2)[::-1]
        w.update(fam_cf=float(np.sum(x2)),
                 cert_cf=float(np.sum(x2[order[:K_FAM]])),
                 x2_g1=float(x2[0]), lam_z=lamz, tau_z=tauz,
                 det_z=lamz * tauz, Xv=Xv)
        wd = dict(f1=fdp.odd_ext(w["t1"], M),
                  f2=fdp.odd_ext(w["t2"], M), D=D, M=M)
        a, b, _ = pp.components_of(wd, gam)
        x_num = (a[:-1] * b[-1] - b[:-1] * a[-1]) ** 2
        fam_num = float(np.sum(x_num))
        c100_num = float(np.sum(np.sort(x_num)[::-1][:K_FAM]))
        worst_cf = max(worst_cf,
                       abs(w["fam_cf"] - fam_num) / fam_num)
        worst_c100 = max(worst_c100,
                         abs(w["cert_cf"] - c100_num) / c100_num)
    print("    done in %.0f s: worst rel dev fam %.1e, cert100 %.1e"
          % (time.time() - t0, worst_cf, worst_c100))
    check("W1.CF the analytic (Dirichlet closed-form) family "
          "reproduces the component-based certified sums on ALL 73 "
          "frames: worst rel %.1e <= %.0e (task bar 5%%: passed at "
          "machine grade)" % (max(worst_cf, worst_c100), CF_BAR),
          max(worst_cf, worst_c100) <= CF_BAR
          and max(worst_cf, worst_c100) <= TASK_BAR)
    cited_dev, pair_dev = 0.0, 0.0
    for w in rows[67:]:
        ct = CITED[w["M"]]
        cited_dev = max(cited_dev,
                        abs(w["cert_cf"] - ct["cert"]) / ct["cert"])
        x2g1_cited = ct["rho_cp"] * ct["cert"] / ct["rho_cf"]
        pair_dev = max(pair_dev,
                       abs(w["x2_g1"] - x2g1_cited) / x2g1_cited)
    check("W1.CITED the deep cert100 reproduce the frozen cited "
          "values (rel %.1e <= %.0e) and the closed-form fixed pair "
          "matches the cited pair chain (rel %.1e <= %.0e)"
          % (cited_dev, CITED_BAR, pair_dev, PAIR_CITED_BAR),
          cited_dev <= CITED_BAR and pair_dev <= PAIR_CITED_BAR)

    # ============================================================== S2
    print("\nS2 -- the asymptotic derivation (numeric limit wards)")
    # A5: pole-leg limit
    hL = LIM_H
    aL = LIM_ALPHA
    DL = aL / hL
    jj = np.arange(hL)
    ee = np.sinh((hL - jj - 0.5) * DL / 2.0)
    cp = 2.0 * math.sqrt(DL) * (math.sinh(DL / 4.0) / (DL / 4.0))
    r_k = []
    for k in (1, 2):
        p_k = cp * float(ft.parity_t(k, hL) @ ee)
        r_k.append(p_k / gp_k(k, aL))
    norm = 2.0 * math.sqrt(2.0 * aL)
    a5_rel = max(abs(r / norm - 1.0) for r in r_k)
    a5_kc = abs(r_k[0] - r_k[1]) / abs(r_k[0])
    check("A5.POLE p_k / (2 sqrt(2 alpha)) -> Gp_k(alpha) at h = %d: "
          "rel %.1e <= %.0e, k-consistency %.1e <= %.0e"
          % (hL, a5_rel, A5_REL, a5_kc, A5_KCONS),
          a5_rel <= A5_REL and a5_kc <= A5_KCONS)
    # A6: composite pair convergence with 1/h rate
    x2_h, _ = ft.pair_x2_closed(aL, hL, g1)
    x2_h2, _ = ft.pair_x2_closed(aL, 2 * hL, g1)
    xi2 = ft.x_inf(aL, g1) ** 2
    dev1 = abs(x2_h / xi2 - 1.0)
    dev2 = abs(x2_h2 / xi2 - 1.0)
    rat = dev1 / max(dev2, 1e-300)
    check("A6.PAIR X^2 -> X_inf^2 at alpha = %.3f: dev %.1e <= %.1f "
          "at h = %d and h-doubling ratio %.2f in [%.1f, %.1f] "
          "(the 1/h law)" % (aL, dev1, A6_DEV, hL, rat, *A6_RATIO),
          dev1 <= A6_DEV and A6_RATIO[0] <= rat <= A6_RATIO[1])
    # A7: the alias census at the deepest frame
    wD = rows[-1]
    x2D = wD["Xv"] ** 2
    m_idx = np.round(gam * DGRID / (2.0 * math.pi)).astype(int)
    ms, mean_m, cnt_m, cnt_pred = [], [], [], []
    for m in range(A7_M_RANGE[0], A7_M_RANGE[1] + 1):
        sel = m_idx == m
        n_m = int(sel.sum())
        if n_m < A7_MIN_CELL:
            continue
        ms.append(m)
        mean_m.append(float(np.mean(x2D[sel])))
        cnt_m.append(n_m)
        cnt_pred.append(math.log(m / DGRID) / DGRID)
    ms = np.array(ms, float)
    sl_m, _, r2_m = fdp.ols_loglog(ms, np.array(mean_m) * ms ** 2)
    cnt_dev = float(np.median(np.abs(np.array(cnt_m, float)
                                     / np.array(cnt_pred) - 1.0)))
    check("A7.ALIAS at M = %d: cell-mean X^2 follows the derived "
          "1/m^2 law (fit slope of mean*m^2 = %+.2f, |.| <= %.1f, "
          "%d cells, R^2 %.2f) and cell counts match log(m/D)/D "
          "(median dev %.2f <= %.1f)"
          % (wD["M"], sl_m, A7_SLOPE, len(ms), r2_m, cnt_dev,
             A7_COUNT),
          abs(sl_m) <= A7_SLOPE and cnt_dev <= A7_COUNT)
    # A8: the h-law at fixed alpha
    f_hs = []
    for h_s in A8_HS:
        Xs, _, _, _, _ = fam_closed(h_s, aL / h_s, gam)
        f_hs.append(float(np.sum(Xs ** 2)))
    xiv = np.array([ft.x_inf(aL, float(gg)) for gg in gam])
    f_inf = float(np.sum(xiv ** 2))
    sl_f, _, _ = fdp.ols_loglog(A8_HS, f_hs)
    sub = np.abs(np.array(f_hs) - f_inf)
    sl_q, _, r2_q = fdp.ols_loglog(A8_HS, sub)
    q_ok = A8_Q[0] <= -sl_q <= A8_Q[1]
    check("A8.HLAW F(h, alpha = %.3f) is h-free (fit exponent %+.3f, "
          "|.| <= %.1f; F_inf = %.3e) with subleading |F - F_inf| ~ "
          "h^%+.2f (q in [%.1f, %.1f]: %s -- soft, typed)"
          % (aL, sl_f, A8_EXP, f_inf, sl_q, *A8_Q,
             "ok" if q_ok else "OUTSIDE"), abs(sl_f) <= A8_EXP)
    # A9: the tower law tau_zero ~ 1/h at fixed D
    t0 = time.time()
    hs_t = list(range(588, 817, 4))
    tau_t = []
    for h_t in hs_t:
        _, _, lam_t, ta_t = m2_closed(h_t, DGRID, gam)
        tau_t.append(ta_t)
    sl_t, _, r2_t = fdp.ols_loglog(hs_t, tau_t)
    check("A9.TOWER tau_zero = det(M2)/lambda(M2) on the D = 1/64 "
          "tower (h = 588..816, %d frames, %.0f s): fit slope %+.3f "
          "in [%.2f, %.2f] (the DERIVED -1; R^2 %.2f)"
          % (len(hs_t), time.time() - t0, sl_t, *A9_SLOPE, r2_t),
          A9_SLOPE[0] <= sl_t <= A9_SLOPE[1])
    # A10: the 73-point shape fit of the derived tau law
    for w in rows:
        w["shape"] = shape_of(w["h"], w["D"])
        w["tau_eff"] = (w["tau"] if not w["deep"] else w["tau_z"])
    sub73 = [w for w in rows if w["alpha"] >= A10_ALPHA_MIN]
    kap = [w["tau_eff"] / w["shape"] for w in sub73]
    sl_k, _, _ = fdp.ols_loglog([w["h"] for w in sub73], kap)
    lt = np.log([w["tau_eff"] for w in sub73])
    lp = np.log([np.median(kap) * w["shape"] for w in sub73])
    r2_s = 1.0 - float(np.sum((lt - lp) ** 2)) \
        / float(np.sum((lt - lt.mean()) ** 2))
    kap_lo = [w["tau_eff"] / w["shape"] for w in rows
              if w["alpha"] < A10_ALPHA_MIN]
    check("A10.SHAPE the derived tau law tau = kappa shape(h, D) on "
          "the alpha >= %.1f battery subset (%d/%d rungs): kappa "
          "drift slope %+.3f (|.| <= %.2f), R^2(log tau vs log "
          "shape) = %.3f >= %.2f; kappa = %.3f..%.3f (median %.3f); "
          "low-alpha mixed regime kappa %.3f..%.3f (typed, excluded "
          "by predeclaration)"
          % (A10_ALPHA_MIN, len(sub73), len(rows), sl_k, A10_KSLOPE,
             r2_s, A10_R2, min(kap), max(kap),
             float(np.median(kap)),
             min(kap_lo) if kap_lo else float("nan"),
             max(kap_lo) if kap_lo else float("nan")),
          abs(sl_k) <= A10_KSLOPE and r2_s >= A10_R2)
    # the exponent decomposition + constant (item 2, assembled)
    tp_pts = [w for w in rows if not w["deep"]]
    sl_tp, _, _ = fdp.ols_loglog([w["h"] for w in tp_pts],
                                 [w["tau_pnt"] for w in tp_pts])
    sl_rho_meas, _, _ = fdp.ols_loglog([w["h"] for w in tp_pts],
                                       [w["rho"] for w in tp_pts])
    sl_shape, _, _ = fdp.ols_loglog([w["h"] for w in tp_pts],
                                    [w["shape"] for w in tp_pts])
    kap_med = float(np.median(kap))
    w0 = rows[0]
    c_pred = kap_med * w0["shape"] * w0["h"] ** 1.5 / w0["tau_pnt"]
    print("\n    THE EXPONENT DECOMPOSITION (old ladder, h-fit):")
    print("      shape (derived)   : h^%+.3f   (the -1 + log drift)"
          % sl_shape)
    print("      tau_pnt (measured): h^%+.3f   (instrument side)"
          % sl_tp)
    print("      rho predicted     : h^%+.3f = shape - tau_pnt"
          % (sl_shape - sl_tp))
    print("      rho measured      : h^%+.3f   (v818: -1.36)"
          % sl_rho_meas)
    print("      envelope condition: rho >= c h^-1.5 iff tau_pnt "
          "grows slower than h^{+0.5 %+.3f} -- margin %.3f"
          % (sl_shape + 1.0, 1.5 + (sl_shape - sl_tp)))
    print("    THE CONSTANT (do not force): kappa_med = %.3f; "
          "random-phase prediction kappa_RP = 1 gives the order; "
          "c_pred = kappa shape h0^1.5 / tau_pnt(h0) = %.2f vs the "
          "contract c = %.2f (ratio %.2f)"
          % (kap_med, c_pred, C_CONTRACT, c_pred / C_CONTRACT))
    exp_dev = abs((sl_shape - sl_tp) - sl_rho_meas)
    check("S2.EXP the derived-plus-measured decomposition reproduces "
          "the measured rho law: predicted h^%+.2f vs measured "
          "h^%+.2f (|dev| = %.2f <= 0.15)"
          % (sl_shape - sl_tp, sl_rho_meas, exp_dev), exp_dev <= 0.15)

    # ============================================================== S3
    print("\nS3 -- the lower-bound attempt (73-point ward) + phase "
          "scan")
    for w in rows:
        if w["deep"]:
            w["rho_cert"] = CITED[w["M"]]["rho_cf"]
        else:
            bud = 100.0 * EPSM * (w["lam"] ** 2 + w["lam_z"] ** 2)
            w["rho_cert"] = (w["cert_cf"] - bud) \
                / (w["lam"] * w["tau_pnt"])
        w["e1_cert"] = w["rho_cert"] * w["h"] ** 1.5
        w["e1"] = w["rho"] * w["h"] ** 1.5
    below = all(w["rho_cert"] <= w["rho"] * (1 + 1e-9) for w in rows)
    c_cert = min(w["e1_cert"] for w in rows)
    w_min = min(rows, key=lambda w: w["e1_cert"])
    sl_e1c, _, _ = fdp.ols_loglog([w["h"] for w in rows],
                                  [w["e1_cert"] for w in rows])
    print("    e1_cert = rho_certfam h^1.5 over the 73 points: min "
          "%.3f (at h = %d), max %.1f, cross-frame slope %+.3f"
          % (c_cert, w_min["h"], max(w["e1_cert"] for w in rows),
             sl_e1c))
    check("W3.ENV the explicit candidate rho >= rho_certfam >= "
          "c_cert h^{-3/2} with c_cert = %.3f holds on 73/73 points "
          "(rho_cert <= rho everywhere: %s) and the certified "
          "envelope is non-decaying (slope %+.3f >= %.2f)"
          % (c_cert, "yes" if below else "NO", sl_e1c,
             ENV_SLOPE_MIN),
          below and c_cert > 0.0 and sl_e1c >= ENV_SLOPE_MIN)
    # the phase-conspiracy scan
    t0 = time.time()
    aa = np.linspace(PHASE_RANGE[0], PHASE_RANGE[1], PHASE_N)
    Fv = np.empty(PHASE_N)
    for i, a_s in enumerate(aa):
        Xs, _, _, _, _ = fam_closed(PHASE_H, a_s / PHASE_H, gam)
        Fv[i] = float(np.sum(Xs ** 2))
    y = np.log(Fv / np.sinh(aa / 2.0) ** 2)
    cf = np.polyfit(np.log(aa), y, 1)
    resid = y - np.polyval(cf, np.log(aa))
    floor_ratio = math.exp(float(np.min(resid))
                           - float(np.median(resid)))
    i_min = int(np.argmin(resid))
    print("    phase scan (h = %d, %d alphas in [%.1f, %.2f], %.0f "
          "s): detrended F ~ alpha^%+.2f sinh^2; dip floor "
          "min/med = %.3f at alpha = %.3f"
          % (PHASE_H, PHASE_N, *PHASE_RANGE, time.time() - t0,
             cf[0], floor_ratio, aa[i_min]))
    share_min = min(w["rho_cert"] / w["rho"] for w in rows)
    check("W4.PHASE no oscillation conspiracy: the family-sum dip "
          "floor %.3f >= %.2f over the admissible alpha range (the "
          "SOS over 22491 zeros never conspires to near-zero); "
          "deployed-battery min certified share %.3f"
          % (floor_ratio, PHASE_FLOOR, share_min),
          floor_ratio >= PHASE_FLOOR)

    # ============================================================== S4
    print("\nS4 -- THE LOGICAL STATUS (mandatory typing)")
    print("""
    What a proven envelope WOULD give: battery-relative floor
    positivity -- lambda tau > 0 with the explicit margin
    c_cert h^{-3/2} -- for every accessible X on the DEPLOYED frame
    battery (the 67 v818 windows + the D = 1/64 tower), at
    citation grade (inputs: [A1] strip, verified zeros to 3e12,
    RvM constants, the linear float budget).
    What it would NOT give: Weil positivity for ALL admissible test
    functions (only the deployed parity frames); zero-location
    information beyond the [A1] strip; ANY statement about RH --
    the floor is necessary-side structure, and only the
    detector-inversion direction converts floor bounds into
    zero-exclusion.
    THE SEPARATION (one sentence): what still separates this from
    the full sector floor contract is the instrument-side growth
    law tau_pnt <= c2 h^{1/2} -- measured (h^%+.2f) but not derived
    -- and the frame-battery restriction (deployed windows, not all
    admissible test functions).""" % sl_tp)

    # ============================================================== C
    print("\nC -- controls")
    check("C1 the analytic-vs-numeric ward passed on all 73 frames "
          "(W1.CF above, machine grade %.1e)"
          % max(worst_cf, worst_c100),
          max(worst_cf, worst_c100) <= CF_BAR)
    check("C2 the phase-conspiracy scan passed (W4 above, floor "
          "%.3f)" % floor_ratio, floor_ratio >= PHASE_FLOOR)
    print("    C3 scramble (restated, measured in the parent "
          "probes): the closed forms are Dirichlet-kernel theorems "
          "about THIS comb; the scrambled comb has no analytic "
          "form and the psd chain refuses it "
          "(lambda_min(A2_scr - M2) = -3.794e+03, det -> -2.1e+02 "
          "at M = 1176, seed 7).")

    # ============================================================== V
    print("\n" + "=" * 78)
    key_ok = not any(f in FAILS for f in
                     ("A1.SYM", "A2.SYM", "A3.SYM", "A4.SYM",
                      "A5.POLE", "A6.PAIR", "A7.ALIAS", "A9.TOWER",
                      "A10.SHAPE", "W1.CF", "W1.CITED", "W3.ENV",
                      "S2.EXP"))
    phase_ok = "W4.PHASE" not in FAILS
    if not phase_ok:
        verdict = "ENVELOPE-OSCILLATION-KILLED"
    elif key_ok:
        verdict = "ENVELOPE-THEOREM-CANDIDATE"
    else:
        verdict = "ENVELOPE-ASYMPTOTIC-PARTIAL"
    print("V -- VERDICT: %s" % verdict)
    print("=" * 78)
    if verdict == "ENVELOPE-THEOREM-CANDIDATE":
        print("""
  THE ENVELOPE THEOREM CANDIDATE (explicit, verbatim):
    'On the deployed battery (67 v818 frames + the D = 1/64 tower
     to X = 25.5), rho(X) >= rho_certfam(X) >= %.3f h^{-3/2}, where
     rho_certfam is the citation-grade certified family floor.  The
     h-law is DERIVED: the certified family sum obeys the alias law
     E[X^2 | cell m] ~ (2D/(pi^2 m^2 N))(p1^2 + p2^2) (every alias
     cell contributes at the same order after the csinc-null
     cancellation), giving tau = kappa (2/(pi^2 N)) sum_m
     log(m/D)/m^2 with kappa = %.2f measured stable; the envelope
     exponent decomposes as -1 (derived) %+.2f (derived shape
     drift) %+.2f (measured tau_pnt) = %+.2f vs -3/2 with margin
     +%.2f; phases cannot conspire (SOS dip floor %.2f).'
  STATUS: promotion-grade CANDIDATE -- the strongest possible floor
  statement short of deriving the instrument-side tau_pnt law."""
              % (c_cert, kap_med, sl_shape + 1.0, -sl_tp,
                 sl_shape - sl_tp, 1.5 + sl_shape - sl_tp,
                 floor_ratio))
    elif verdict == "ENVELOPE-ASYMPTOTIC-PARTIAL":
        print("""
  Exponent/constant derived but uniformity blocked -- failed
  pieces: %s (typed above).""" % ", ".join(sorted(set(FAILS))))
    else:
        print("""
  Phase conspiracy real at alpha = %.3f (dip floor %.3f) -- the
  analytic route dies there; typed above.""" % (aa[i_min],
                                                floor_ratio))
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
