"""Discovery probe: the W2 START -- form density of the nested window
(hat) spaces in the odd form sector of Suzuki's localized Weil operator
A_a (arXiv:2606.09096), in honest feasible slices.

The W2 contract step behind PRIME.WEIL.OPERATOR.01: after W1 (the TFPT
window form IS a Galerkin discretization of B_a = D* G_a D at the
declared windows, w1_theorem_probe), the next rung is that the NESTED
window spaces are form-dense in the (odd sector of the) form domain of
A_a, so that the window spectra converge to the operator spectrum.
This probe does NOT claim W2; it verifies the classical slice, measures
the two spectral slices, and types what remains.

Slices and their honest types:

  (i)  [CLASSICAL, verified] FEM density.  The hat spaces V_M on the
       uniform lattice are H^1_0(-a,a)-dense with the classical rate:
       for f in H^2 cap H^1_0 the H^1_0-seminorm projection onto V_M
       IS nodal interpolation (1-D exact fact: (f - I_M f)' integrates
       to zero against piecewise constants), and the error obeys
       ||(f - I_M f)'|| ~ D^1, ||f - I_M f|| ~ D^2.  Verified here on
       3 smooth odd test functions over 4 dyadic refinements
       (M = 92/184/368/736).  Together with the classical facts that
       Q_W is bounded in the H^1 norm (Suzuki Sec. 8.4; Bombieri's
       Problem B setting) and that H^1_0 contains a form core of A_a
       (Suzuki Thm 1.1: the form-norm closure of C_c^infty(-a,a)
       carries the form; C_c^infty subset H^1_0), this yields
       form-norm density of union_M V_M in D(Q_W^a) -- the chain is
       CLASSICAL and cited, not re-proved here; the numeric content is
       the measured rate.  The parity split is compatible (Suzuki
       Sec. 4.5: A_a commutes with J, lambda_a = min(lambda_a^+,
       lambda_a^-)), so the same holds sector-wise.

  (ii) [MEASURED, central] Galerkin eigenvalue convergence at FIXED
       a = alpha(h = 184) = log 16 = 2.7726: the lowest 3 eigenvalues
       of the generalized problem G x = lambda M x (G = hat-Galerkin
       matrix of D* G_a D; M = hat mass matrix) over the NESTED dyadic
       refinements M = 92/184/368/736.  Rayleigh-Ritz gives
       monotone-from-above convergence (min-max on nested spaces);
       measured: monotone decrease + Cauchy gaps + empirical rates,
       full space and odd sector, plus the parity identity
       lambda_full = min(lambda_even, lambda_odd) per refinement.
       LAG ROUTE (essential): the eigenvalue scale turns out to be
       |lambda| ~ 1e-4, BELOW the ~2e-5-per-lag error of the plain
       16-pt Gauss route at in-cell atom kinks (that route breaks the
       exact Rayleigh-Ritz monotonicity -- observed, documented).  The
       lags are therefore assembled LAYERWISE in the route certified
       by w1_theorem_probe P2.3: smooth screw layer by Gauss on the
       analytic integrand (1-D correlation form; d <= 2 by exact
       mpmath), atom layer by the CLOSED B-spline form (exact), pole
       layer closed -- machine-precision lags, no kink systematic.

 (iii) [MEASURED] lambda_a in a: the lowest Galerkin eigenvalue at
       fixed M = 368 across 5 frame-A window sizes a = alpha(h), with
       a per-a discretization-gap estimate gap(a) := lambda^{(184)}(a)
       - lambda^{(368)}(a) >= 0.  WHAT THE PAPER CLAIMS (read from
       the local full text): Suzuki Thm 1.3 claims ONLY that lambda_a
       is CONTINUOUS in a -- no monotonicity statement anywhere;
       Thm 1.4 gives the small-a asymptote lambda_a = log(1/a) + mu_1
       - log(2 pi) + psi(2) - 1 + O(a) (decreasing like log(1/a) as
       a -> 0+, EVEN ground state for small a).  Monotone non-increase
       of the TRUE lambda_a is nevertheless PREDICTED by the classical
       zero-extension nesting H^1_0(-a,a) subset H^1_0(-a',a'); the
       fixed-M Galerkin values are upper bounds whose defect grows
       with a, so the measured bar is nesting-consistency WITHIN the
       measured gaps: lambda(a') - lambda(a) <= 2 gap(a') for a' > a.
       Reported: the profile, local slopes, gaps, ground-state parity
       (an observation -- Thm 1.4 only covers small a).

  (iv) [C, typed] WHAT IS STILL MISSING for the full W2 statement:
       (a) Mosco/Gamma convergence of the discretized forms to Q_W^a
           (recovery sequences follow from slice (i) + H^1-boundedness;
           the liminf inequality needs the closedness of Q_W^a along
           L^2-convergent sequences UNIFORMLY over the discretization,
           i.e. the compact embedding H_log -> L^2 (Suzuki Prop. 4.1)
           transferred to the lattice family -- not yet written);
       (b) norm-resolvent convergence of the Galerkin operators to A_a
           (would upgrade slice (ii) from measured monotone bounds to
           eigenvalue convergence WITH rates; requires (a) + a
           discrete compactness argument);
       (c) interval-arithmetic certification of the layerwise lag
           route (the kink systematic of the plain Gauss route is
           REMOVED here by the closed atom layer; the remaining series
           truncation ~ e^{-2 D N_LERCH} and float roundoff are typed
           but not certified as rigorous enclosures);
       (d) the a -> infinity limit (Suzuki Sec. 7, strong-resolvent
           D_{a,theta} -> D) is W3/W4 territory: OUT OF SCOPE here.
       No positivity claim, no RH statement; lambda values are
       REPORTED, not interpreted.

CONVENTION NOTE: the screw function used here is Suzuki's TRUE g with
the Lerch block carrying the coefficient +1/4 (the (1/4)(F(0) - F(t))
bracket of eq. (1.3)), as locked by w1_theorem_probe C0 against the
paper's own Sec. 2.2 data (A = 0.707546..., g(0) = 0, r_1'' = rho -
1/(2|t|)).  With the earlier w1-chain kernel gtil (Lerch coefficient
-1) the quadratic form acquires a -4 rho smooth layer, is unbounded
below on refining lattices (eigenvalues diverge ~ -log(1/D)), and the
lambda_a measurement is meaningless -- that misreading was found and
corrected in this work cycle.

Verdict enums (frozen): W2-SLICES-PASS (i-iii all pass), MIXED,
W2-SLICES-FAIL (>= 2 slices fail).

FIREWALL: experiments-only; v563 read-only; no marker moves.
Python-only, counted per GATE.WOLFRAM.02.
"""
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

T0 = time.time()
FAILS = []
N_CHK = 0


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import mpmath as mp  # noqa: E402

MS = (92, 184, 368, 736)        # the dyadic refinement ladder (nested)
M_FIX = 368                     # fixed resolution for the a-scan
H_TARGETS = (184, 286, 540, 750, 1000)   # 5 window sizes for the a-scan
N_LERCH = 20000
_NN_L = np.arange(N_LERCH, dtype=float)
_WTS = 1.0 / (_NN_L + 0.25) ** 2

mp.mp.dps = 30
PSI14_F = float(mp.digamma(mp.mpf(1) / 4))
LOGPI_F = math.log(math.pi)
PHI1_F = float(mp.lerchphi(1, 2, mp.mpf(1) / 4))
UU = np.array([float(u) for u in core.U_ALL])
MU = np.array([float(m) for m in core.MU_ALL])
CW = np.cumsum(MU / 2.0)
CS = np.cumsum(MU / 2.0 * UU)

from numpy.polynomial.legendre import leggauss  # noqa: E402
GX16, GW16 = leggauss(16)
GX8, GW8 = leggauss(8)


def g_smooth_vec(ts):
    """the SMOOTH layer of the TRUE screw function (Lerch coefficient
    +1/4 per the (1/4)(F(0) - F(t)) bracket of eq. (1.3), locked in
    w1_theorem_probe C0), vectorized series route; analytic away from
    t = 0 -- no in-cell kinks."""
    xf = np.abs(np.asarray(ts, dtype=float))
    out = xf / 2.0 * (LOGPI_F - PSI14_F) - 0.25 * PHI1_F
    lb = np.empty_like(xf)
    for a in range(0, xf.size, 400):
        b = min(xf.size, a + 400)
        E = np.exp(-np.outer(2.0 * xf[a:b], _NN_L) - 0.5 * xf[a:b, None])
        lb[a:b] = E @ _WTS
    return out + 0.25 * lb


def g_sm_mp(tv):
    """smooth TRUE screw layer, mpmath."""
    tv = abs(mp.mpf(tv))
    PHI1m = mp.lerchphi(1, 2, mp.mpf(1) / 4)
    LLm = mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)
    if tv == 0:
        return mp.mpf(0)
    return (LLm * tv / 2 - PHI1m / 4 + mp.exp(-tv / 2)
            * mp.lerchphi(mp.exp(-2 * tv), 2, mp.mpf(1) / 4) / 4)


def galerkin_lags(a, M):
    """cgal(d), d = 0..M-2: the hat-Galerkin Toeplitz lags of
    D* G_a D at window a with M cells (D = 2a/M), assembled LAYERWISE
    in the route certified by w1_theorem_probe P2.3: smooth layer by
    16-pt Gauss on the 1-D correlation form (analytic integrand;
    d <= 2 by exact mpmath -- the |t| log|t| head), atom layer by the
    closed B-spline read (exact), pole layer closed."""
    D = 2.0 * a / M
    # smooth layer, 1-D correlation form int g_sm(kD+s)(D-|s|) ds
    ss = np.concatenate([0.5 * D * (GX16 + 1) - D, 0.5 * D * (GX16 + 1)])
    ww = np.tile(0.5 * D * GW16, 2) * (D - np.abs(ss))
    ks = np.arange(M)
    vals = g_smooth_vec((ks[:, None] * D + ss[None, :]).ravel())
    II = vals.reshape(M, ss.size) @ ww
    c = np.empty(M - 1)
    for d in range(M - 1):
        c[d] = (2.0 * II[d] - II[abs(d - 1)] - II[d + 1]) / (D * D)
    Dm = mp.mpf(D)
    II_b = {k: mp.quad(lambda s: g_sm_mp(k * Dm + s) * (Dm - abs(s)),
                       [-Dm, 0, Dm]) for k in range(4)}
    for d in range(3):
        c[d] = float((2 * II_b[d] - II_b[abs(d - 1)] - II_b[d + 1])
                     / Dm ** 2)
    # atom layer: closed B-spline reads of the prime measure (exact)
    dd_grid = np.arange(M - 1) * D

    def K_f(x):
        u = np.abs(x) / D
        return np.where(u <= 1.0, D * (2.0 / 3.0 - u ** 2 + u ** 3 / 2.0),
                        np.where(u < 2.0, D * (2.0 - u) ** 3 / 6.0, 0.0))

    ka = core.atoms_in(a)
    for u_j, m_j in zip(UU[:ka], MU[:ka]):
        c -= 0.5 * m_j * (K_f(u_j - dd_grid) + K_f(u_j + dd_grid))
    # pole layer, closed
    Xp = math.exp(D / 2) + math.exp(-D / 2) - 2.0
    c += 2.0 * np.cosh(dd_grid / 2.0) * 16.0 * Xp ** 2 / (D * D)
    return c, D


def eig_low(a, M, n_low=3):
    """lowest generalized eigenvalues of G x = lambda Mass x on the
    interior hats (full space, even sector, odd sector)."""
    c, D = galerkin_lags(a, M)
    n = M - 1                              # interior nodes 1..M-1
    idx = np.abs(np.arange(n)[:, None] - np.arange(n)[None, :])
    G = c[idx]
    Mass = np.zeros((n, n))
    np.fill_diagonal(Mass, 2.0 * D / 3.0)
    rng_ = np.arange(n - 1)
    Mass[rng_, rng_ + 1] = D / 6.0
    Mass[rng_ + 1, rng_] = D / 6.0

    def low(A_, B_):
        Lc = np.linalg.cholesky(B_)
        Y = np.linalg.solve(Lc, A_)
        S = np.linalg.solve(Lc, Y.T).T
        return np.linalg.eigvalsh(0.5 * (S + S.T))[:n_low]

    ev_full = low(G, Mass)
    # parity split: reflection i -> M-i on interior node labels 1..M-1
    hh = M // 2
    P_odd = np.zeros((hh - 1, n))
    for i in range(1, hh):
        P_odd[i - 1, i - 1] = 1.0 / math.sqrt(2.0)
        P_odd[i - 1, M - i - 1] = -1.0 / math.sqrt(2.0)
    P_ev = np.zeros((hh, n))
    for i in range(1, hh):
        P_ev[i - 1, i - 1] = 1.0 / math.sqrt(2.0)
        P_ev[i - 1, M - i - 1] = 1.0 / math.sqrt(2.0)
    P_ev[hh - 1, hh - 1] = 1.0
    ev_odd = low(P_odd @ G @ P_odd.T, P_odd @ Mass @ P_odd.T)
    ev_ev = low(P_ev @ G @ P_ev.T, P_ev @ Mass @ P_ev.T)
    return ev_full, ev_ev, ev_odd, D


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("W2 START -- form density of the nested window spaces, in slices")
    print("=" * 78)

    kz = core.frame_a_zones()[0]
    r = core.build_window(kz)
    a0 = r["alpha"]                       # = log 16 = 2.7726 (h = 184)
    print("fixed window: a = alpha(h=184) = %.12f (= log %d)"
          % (a0, r["n_zone"]))

    # ================================================== slice (i): FEM
    print("\n(i) FEM density, classical slice")
    fs = (lambda x: np.sin(math.pi * x / a0),
          lambda x: (x / a0) * (1.0 - (x / a0) ** 2),
          lambda x: np.sin(2.0 * math.pi * x / a0)
          + 0.3 * np.sin(3.0 * math.pi * x / a0))
    dfs = (lambda x: (math.pi / a0) * np.cos(math.pi * x / a0),
           lambda x: (1.0 - 3.0 * (x / a0) ** 2) / a0,
           lambda x: (2.0 * math.pi / a0) * np.cos(2.0 * math.pi * x / a0)
           + (0.9 * math.pi / a0) * np.cos(3.0 * math.pi * x / a0))

    def interp_err(f, df, M):
        D = 2.0 * a0 / M
        nodes = -a0 + D * np.arange(M + 1)
        fv = f(nodes)
        fv[0] = fv[-1] = 0.0              # Dirichlet ends (exact for fs)
        slopes = np.diff(fv) / D
        mid = 0.5 * (nodes[:-1] + nodes[1:])
        xg = mid[:, None] + 0.5 * D * GX8[None, :]
        wg = 0.5 * D * GW8[None, :]
        e_h1 = float(np.sqrt(np.sum(wg * (df(xg) - slopes[:, None]) ** 2)))
        lin = fv[:-1, None] + slopes[:, None] * (xg - nodes[:-1, None])
        e_l2 = float(np.sqrt(np.sum(wg * (f(xg) - lin) ** 2)))
        # orthogonality: (f - I f)' integrates to 0 per cell
        ortho = float(np.max(np.abs(np.sum(wg * (df(xg) - slopes[:, None]),
                                           axis=1))))
        return e_h1, e_l2, ortho

    rates_h1, rates_l2, orthos = [], [], []
    for fi, (f, df) in enumerate(zip(fs, dfs)):
        errs = [interp_err(f, df, M) for M in MS]
        rh = [math.log2(errs[i][0] / errs[i + 1][0]) for i in range(3)]
        rl = [math.log2(errs[i][1] / errs[i + 1][1]) for i in range(3)]
        rates_h1.append(rh[-1])
        rates_l2.append(rl[-1])
        orthos.append(max(e[2] for e in errs))
        print("   f%d: H1 err %s rates %s | L2 err %s rates %s"
              % (fi + 1, ["%.2e" % e[0] for e in errs],
                 ["%.3f" % z for z in rh],
                 ["%.2e" % e[1] for e in errs],
                 ["%.3f" % z for z in rl]))
    check("W2.1 [E] the 1-D projection fact: (f - I_M f)' is orthogonal "
          "to piecewise constants (per-cell integrals vanish, worst "
          "%.1e < 1e-12 x scale): the H^1_0-seminorm projection onto "
          "the hat space IS nodal interpolation" % max(orthos),
          max(orthos) < 1e-10)
    check("W2.2 [E-float, classical slice] FEM density with the "
          "classical rate on 3 smooth odd test functions: H^1 rates "
          "%s (bar |rate - 1| <= 0.05), L^2 rates %s (bar |rate - 2| "
          "<= 0.1) over M = 92/184/368/736 -- with Q_W H^1-bounded "
          "(Suzuki Sec. 8.4) and H^1_0 a form core (Thm 1.1) this is "
          "the CLASSICAL density chain, typed [C], cited not re-proved"
          % (["%.3f" % z for z in rates_h1], ["%.3f" % z for z in rates_l2]),
          max(abs(z - 1.0) for z in rates_h1) <= 0.05
          and max(abs(z - 2.0) for z in rates_l2) <= 0.10)

    # ====================================== slice (ii): refinement at a0
    print("\n(ii) Galerkin eigenvalue convergence at fixed a = %.4f" % a0)
    tabs = {}
    for M in MS:
        t1 = time.time()
        tabs[M] = eig_low(a0, M)
        print("   M = %3d (D = %.6f): full %s | even %s | odd %s"
              " [%.1f s]"
              % (M, tabs[M][3],
                 ["%+.6f" % z for z in tabs[M][0]],
                 ["%+.6f" % z for z in tabs[M][1]],
                 ["%+.6f" % z for z in tabs[M][2]],
                 time.time() - t1))
    ok_mono, ok_cauchy, rates = True, True, []
    for which, lab in ((0, "full"), (2, "odd")):
        for k in range(3):
            seq = [float(tabs[M][which][k]) for M in MS]
            gaps = [seq[i] - seq[i + 1] for i in range(3)]
            if any(gp < -1e-10 for gp in gaps):
                ok_mono = False
            if not (gaps[2] < gaps[1] < gaps[0] + 1e-15):
                ok_cauchy = False
            rt = [math.log2(gaps[i] / gaps[i + 1]) if gaps[i + 1] > 0
                  else float("nan") for i in range(2)]
            rates.append((lab, k + 1, gaps, rt))
    print("   Cauchy gaps and empirical rates (log2 of gap ratios):")
    for lab, k, gaps, rt in rates:
        print("     %-4s lambda_%d: gaps %s rates %s"
              % (lab, k, ["%.3e" % gp for gp in gaps],
                 ["%.2f" % z for z in rt]))
    par_dev = max(abs(min(float(tabs[M][1][0]), float(tabs[M][2][0]))
                      - float(tabs[M][0][0])) for M in MS)
    check("W2.3 [E-float, central] Rayleigh-Ritz on NESTED window "
          "spaces: the lowest 3 eigenvalues decrease monotonically "
          "from above under dyadic refinement (full + odd sector, all "
          "6 sequences), the Cauchy gaps shrink at every step, and the "
          "parity identity lambda_full = min(lambda_even, lambda_odd) "
          "holds per refinement (worst |diff| %.1e < 1e-10) -- the "
          "min-max structure of the form-density contract, MEASURED"
          % par_dev, ok_mono and ok_cauchy and par_dev < 1e-10)
    r_odd1 = [z for lab, k, _, z in rates if lab == "odd" and k == 1][0]
    check("W2.4 [E-float] the ground-sector convergence is Cauchy with "
          "a stable empirical rate: odd lambda_1 gap rates %s (last "
          ">= 0.8, i.e. gap factor >= 1.74 per refinement; extrapolated"
          " limit lambda_1^odd ~ %.6f), full lambda_1 rates %s -- "
          "rates are MEASURED, not claimed (norm-resolvent statement "
          "is the open (iv)(b))"
          % (["%.2f" % z for z in r_odd1],
             float(tabs[736][2][0])
             - (float(tabs[368][2][0]) - float(tabs[736][2][0])),
             ["%.2f" % z for z in
              [z for lab, k, _, z in rates if lab == "full" and k == 1][0]]),
          r_odd1[-1] >= 0.8)

    # ====================================== slice (iii): the a-scan
    print("\n(iii) lambda_a across 5 window sizes at fixed M = %d" % M_FIX)
    zs = core.frame_a_zones()
    cand = []
    for kz_ in zs:
        D_k = 0.5 * float(core.G_ALL[kz_]) / float(core.NU_MAIN)
        M_k = int(math.ceil(core.U_ALL[kz_] / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if 2.0 * float(core.U_ALL[kz_]) <= 12.7:   # atom table complete
            cand.append((M_k // 2, kz_))
    picks = []
    for tgt in H_TARGETS:
        pool = [(hh, kz_) for hh, kz_ in cand if (hh, kz_) not in picks]
        picks.append(min(pool, key=lambda p: abs(p[0] - tgt)))
    picks.sort(key=lambda p: float(core.U_ALL[p[1]]))
    rows_a = []
    for hh, kz_ in picks:
        av = float(core.U_ALL[kz_])
        t1 = time.time()
        ev_f, ev_e, ev_o, Dw = eig_low(av, M_FIX, n_low=1)
        ev_f2, _, _, _ = eig_low(av, M_FIX // 2, n_low=1)
        gap = float(ev_f2[0]) - float(ev_f[0])
        par = "even" if ev_e[0] < ev_o[0] else "odd"
        par_dev_a = abs(min(float(ev_e[0]), float(ev_o[0]))
                        - float(ev_f[0]))
        rows_a.append((hh, av, float(ev_f[0]), gap, par, par_dev_a))
        print("   h = %4d: a = %.6f, lambda_a = %+.8f (gap(184->368) "
              "= %+.2e, even %+.8f, odd %+.8f, ground state %s) "
              "[%.1f s]"
              % (hh, av, ev_f[0], gap, ev_e[0], ev_o[0], par,
                 time.time() - t1))
    lam_seq = [z for _, _, z, _, _, _ in rows_a]
    a_seq = [av for _, av, _, _, _, _ in rows_a]
    gaps_a = [gp for _, _, _, gp, _, _ in rows_a]
    slopes = [(lam_seq[i + 1] - lam_seq[i]) / (a_seq[i + 1] - a_seq[i])
              for i in range(len(lam_seq) - 1)]
    mono_dir = all(lam_seq[i + 1] <= lam_seq[i] + 1e-9
                   for i in range(len(lam_seq) - 1))
    consistent = all(lam_seq[i + 1] - lam_seq[i]
                     <= 2.0 * abs(gaps_a[i + 1]) + 1e-9
                     for i in range(len(lam_seq) - 1))
    check("W2.5 [E-float] the lambda_a profile: %s over a = %s "
          "(local slopes %s; per-a discretization gaps %s) -- the "
          "PAPER claims only CONTINUITY (Thm 1.3; no monotonicity "
          "statement in the text); the TRUE lambda_a is non-"
          "increasing by zero-extension nesting; the fixed-M Galerkin "
          "values are upper bounds with a-dependent defect, so the "
          "declared bar is nesting-CONSISTENCY within twice the "
          "measured gap: %s (raw monotone: %s)"
          % (["%+.2e" % z for z in lam_seq],
             ["%.3f" % av for av in a_seq],
             ["%+.4f" % s for s in slopes],
             ["%.1e" % gp for gp in gaps_a],
             "PASS" if consistent else "VIOLATED",
             mono_dir), consistent)
    pars = [p for *_, p, _ in rows_a]
    par_dev_scan = max(z for *_, z in rows_a)
    check("W2.6 [E-float] the parity identity lambda_a = min(lambda_"
          "even, lambda_odd) holds at every a (worst |diff| %.1e < "
          "1e-10; Suzuki Sec. 4.5); ground-state parity across the "
          "scan: %s (REPORTED -- Thm 1.4 proves 'even' only for "
          "sufficiently small a, no claim at these a)"
          % (par_dev_scan, pars), par_dev_scan < 1e-10)

    # ====================================== slice (iv): the typed gap
    check("W2.7 [C] typed remainder for full W2 (no claim made here): "
          "(a) Mosco/Gamma convergence of the lattice forms to Q_W^a "
          "(recovery from slice (i) + H^1-boundedness; liminf needs "
          "the compact embedding H_log -> L^2, Suzuki Prop. 4.1, "
          "transferred uniformly to the lattice family); (b) "
          "norm-resolvent convergence of the Galerkin operators to "
          "A_a (upgrades slice (ii) to convergence with rates); (c) "
          "rigorous enclosures for the layerwise lag route (the atom-"
          "kink systematic of the plain Gauss route is REMOVED by the "
          "closed atom layer; remaining: series truncation ~ "
          "e^{-2 D N} and float roundoff -- note the lambda ~ 1e-10 "
          "values sit at the dense-eigensolver resolution ~5e-11, so "
          "the honest reading is lambda_a = 0+ within ~1e-9, not a "
          "sign statement); (d) the a -> infinity strong-resolvent "
          "limit is W3/W4, out of scope.  No positivity claim, no RH "
          "statement", True)

    n_slice_fails = len(set(f.split(".")[0] for f in FAILS))
    if not FAILS:
        VERDICT = "W2-SLICES-PASS"
    elif n_slice_fails >= 2:
        VERDICT = "W2-SLICES-FAIL"
    else:
        VERDICT = "MIXED"
    print("\nVERDICT: %s -- FEM density classical-verified, eigenvalue "
          "convergence and lambda_a profile measured, W2 remainder "
          "typed" % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
