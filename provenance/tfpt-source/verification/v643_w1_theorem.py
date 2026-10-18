"""v643 -- PRIME.WEIL.THEOREM.01: W1 AS A THEOREM at the measure level --
the precise statement on SUZUKI'S TRUE SCREW FUNCTION, the L^2_0
projection bookkeeping (the last open D6 item of the v631 chain), and
the full form equality on the common odd sector.  Contains the machine
evidence (C0.1) for the CONVENTION ERRATUM of the v631/v640-v642 chain
(Lerch coefficient +1/4, not -1) and the exact transfer identity that
keeps every measured number of that chain valid verbatim.

THE CONVENTION LOCK (C0; central honesty finding of this probe):
  Suzuki (arXiv:2606.09096) eq. (1.3) ends in the bracket
      - (1/4) ( Phi(1,2,1/4) - e^{-|t|/2} Phi(e^{-2|t|}, 2, 1/4) ),
  i.e. the Hurwitz-Lerch block carries the coefficient +1/4, NOT -1.
  This is locked by the paper's own data: (a) Sec. 2.2 writes
  g = ... - (1/4)(F(0) - F(t)) + primes with F(t) the expansion of
  e^{-|t|/2} Phi(e^{-2|t|},2,1/4), and the printed constant
  A = (1/2)(log 2 pi - psi(2)) = 0.707546... of the origin expansion
  g = (1/2)|t| log|t| + A|t| + primes + O(t^2) holds ONLY with +1/4;
  (b) Sec. 2.4 computes r_1''(t) = rho(t) - 1/(2|t|) from the (1/4)
  bracket, rho(t) = e^{-|t|/2}/(1 - e^{-2|t|}); (c) g(0) = 0 (the
  Krein-Langer screw normalization).  The earlier w1 probe chain
  (w1_dictionary/boundary/frozen/matrix) used the kernel
      gtil := g - (5/4) e^{-|t|/2} Phi(e^{-2|t|}, 2, 1/4)
  (Lerch coefficient -1: a bracket misreading of (1.3)).  All its
  INTERNAL identities are correct identities of gtil, and ALL ITS
  MEASURED NUMBERS TRANSFER VERBATIM, because
      cgal_sm(gtil) = -4 cgal_sm(g)   (exactly:
      gtil_sm'' = rho - 5 rho = -4 rho vs g_sm'' = +rho),
  so its ratio cgal(gtil)/(-4 D c_ar) == cgal(g)/(+D c_ar) number for
  number (verified below).  Only the LABELS change: 'Suzuki's smooth
  layer = -4 x arch density' becomes '= +1 x arch density', and the
  two-layer dictionary (-1/(4D) smooth, 1/D atomic) collapses to the
  ONE scalar +1/D on both layers -- sign-compatible with positivity
  (the TFPT window form and Suzuki's Q_W^a sit on the SAME side).

THE PROJECTION LEMMA (P1; proved, then verified by computation):
  Setting (Suzuki): L^2_0(-a,a) = {u in L^2(-a,a) : int u = 0}; P_a =
  orthogonal projection (eq. 2.1: subtract the mean); G_a = P_a G P_a;
  D = i d/dx with Dirichlet domain D(D) = H^1_0(-a,a) and RANGE
  R(D) = L^2_0(-a,a); B_a = D* G_a D on H^1_0(-a,a); A_a = Friedrichs
  extension of B_a (Thm 1.1); Q_W^a(v) = <B_a v, v> on H^1_0 (1.8).
  (a) THE MEAN-ZERO CONDITION LIVES ON THE u-SIDE AND IS AUTOMATIC:
      for every v in H^1_0(-a,a), int Dv = v(a) - v(-a) = 0, i.e.
      D : H^1_0 -> L^2_0 is a bijection (Suzuki Sec. 8.2).  Hence
      P_a(Dv) = Dv identically and <G_a Dv, Dw> = <G Dv, Dw> on all of
      H^1_0 x H^1_0: Suzuki's L^2_0 imposes NO linear condition on the
      coefficient vectors of any H^1_0-conforming Galerkin family, and
      the projection generates NO dictionary term.  Kernel form: the
      Krein correction g(x-y) -> g(x-y) - g(x) - g(-y) + g(0) pairs to
      -2 (int g u)(int u) + g(0)(int u)^2 on the derived objects and
      vanishes identically there.
  (b) THE v563 PARITY PROJECTION IS AN (EXTRA) v-SIDE CONDITION: the
      odd sector V_{M-1-j} = -V_j (odd_toeplitz), read as hat functions
      on the half-integer lattice p_j = (j - (M-1)/2) D, is EXACTLY the
      sector of odd piecewise-linear functions in H^1_0(-atil, atil),
      atil = alpha + D/2: Phi_V(-x) = -Phi_V(x), Phi_V(+-atil) = 0,
      int Phi_V = D sum V_j = 0.  Oddness is a mean-zero condition on
      the TEST FUNCTION itself -- extra, harmless, parity-compatible
      (Suzuki Sec. 4.5).  CONCLUSION: the odd TFPT window sector is a
      SUBSPACE of the Suzuki form domain and the L^2_0/H^1_0
      bookkeeping closes TRIVIALLY.

THE THEOREM (W1, measure level; window h = 184 declared; all constants
explicit; portability of the measured ratios per v641_w1_portability
via the verbatim-transfer identity of C0):
  Let g be the (true) screw function, rho as above, L := log pi -
  psi(1/4), A := (1/2)(log 2 pi - psi(2)), and define the WEIL MEASURE
    W := g'' + 2 cosh(t/2)   (as tempered distributions):
  explicitly, W has density rho(t) away from t = 0, atoms
  (Lambda(n)/sqrt n) delta_{+-log n}, and the origin Pf/delta_0 block
  of |t| log|t|-type with total delta_0 mass 2A + 1 in the Pf scheme.
  Then:
  (i)   g'' = -2 cosh(t/2) + W, and the separated pole block
        -2 cosh(t/2) = -(e^{t/2} + e^{-t/2}) (the zeta poles s = 0, 1)
        has rank <= 2 after parity projection;
  (ii)  TENT reads: A_arch = -g''_smooth EXACTLY -- the v563 arch lags
        are the point-route tent reads of -W_sm at EVERY d >= 0:
        c_ar[d] = -<W_sm, tent_d>, with NO constant and NO scalar; the
        candidate origin constant kappa := c_ar[0] + point-read(0)
        VANISHES identically (measured < 1e-53; equivalently the
        closed identity (2/D) int_0^D t rho dt + 2 int_D^inf rho dt
        + (f(D) - Phi(1,2,1/4))/(2D) = 0, f(t) := e^{-t/2}
        Phi(e^{-2t},2,1/4) -- the v563 near-cell scheme IS Suzuki's
        origin bookkeeping); the atom lags are the literal tent reads
        of -W_at;
  (iii) B-SPLINE reads: the hat-Galerkin lags of D* G_a D are
        cgal(d) = poleK(d) - <W, K_d> with the closed pole read
        poleK(d) = 32 cosh(dD/2)(e^{D/2}+e^{-D/2}-2)^2/D^2 and K = hat
        autocorrelation (cubic B-spline (1,4,1)/6, mass D^2): smooth
        density read -<rho, K_d> exact for d >= 3, atoms in closed
        B-spline form, boundary constants Btil(0..2) exact;
  (iv)  hence the ONE-SCALAR dictionary
        c_TFPT[d] = (1/D)(cgal(d) - poleK(d)) holds up to (a) the
        derived second-order law R(d) = 1 + (D^2/12)(rho''/rho)(dD)
        + O(D^4) -> 1 + 1/(6 d^2) (window-independent; the D^8 bracket
        coefficients D^9/45 and 31 D^10/45 are derived below and type
        the remainder), (b) the measure-level re-binnings (atoms: tent
        <-> B-spline reads of the SAME atom data; smooth near cells
        d <= 12: the exact read ratio <rho,K_d>/(D <rho,tent_d>) of the
        SAME density), (c) the exact origin constants kappa, Btil(0..2)
        -- verified on 10 odd 16-mode test vectors to the task bar
        |Q_T - Q_S|/|Q_T| < 1e-4 per vector, with the SIGN of the
        identification now positivity-compatible.

Route note (declared): Suzuki-side lags assembled LAYERWISE -- smooth
screw layer by 16-pt Gauss on the analytic integrand (d <= 2 by exact
mpmath integrals), atom layer by the CLOSED B-spline form (certified
against exact kink-split integrals, cf. v642_w1_matrix M1.1),
pole layer closed.  The smooth near-cell re-binning is NOT tautological:
cgal_sm enters from the independent double-integral route, so per-lag
agreement tests THEOREM (iii) at that lag.

Verdict enums (frozen): W1-THEOREM (all pass incl. the 1e-4 bar),
W1-THEOREM-GAP (a structural identity fails), MIXED (identities hold,
only the literal numeric bar fails).

FIREWALL: v563 read-only; no marker moves; no positivity claim, no RH
statement.  Python-only, counted per GATE.WOLFRAM.02.

PROVENANCE: discovery probe w1_theorem_probe.py (2026-08-02, 11/11,
verdict W1-THEOREM; Suzuki arXiv:2606.09096 eq. 1.3 / Sec. 2.2).
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
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402

SEED = 20260803                 # fresh seed (matrix probe used 20260802)
N_VEC = 10
N_MODES = 16
BAR_TASK = 1.0e-4               # the task bar, per vector, 16-mode block
N_LERCH = 20000
_NN_L = np.arange(N_LERCH, dtype=float)
_WTS = 1.0 / (_NN_L + 0.25) ** 2


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("W1 THEOREM -- measure-level statement on Suzuki's true g")
    print("=" * 78)

    # ------------------------------------------------ window and tables
    kz = core.frame_a_zones()[0]
    r = core.build_window(kz)
    alpha, Mz, hz, D = r["alpha"], r["M"], r["h"], r["D"]
    atil = alpha + D / 2.0
    ka = core.atoms_in(alpha)
    uu = np.array([float(u) for u in core.U_ALL[:ka]])
    mm = np.array([float(m) for m in core.MU_ALL[:ka]])
    c_at, _ = core.atom_lags_at(alpha, Mz, core.U_ALL[:ka].copy(),
                                core.MU_ALL[:ka].copy())
    c_ar = core.arch_lags(Mz, D)
    c_tfpt = c_ar + c_at
    print("window: h = %d, M = %d, alpha = %.12f, D = %.12f, atil = "
          "%.12f, atoms = %d" % (hz, Mz, alpha, D, atil, ka))

    mp.mp.dps = 30
    PSI14_F = float(mp.digamma(mp.mpf(1) / 4))
    LOGPI_F = math.log(math.pi)
    L_F = LOGPI_F - PSI14_F
    PHI1_F = float(mp.lerchphi(1, 2, mp.mpf(1) / 4))
    G0_F = 0.0                      # g(0) = 0 (true normalization)

    UU = np.array([float(u) for u in core.U_ALL])
    MU = np.array([float(m) for m in core.MU_ALL])
    CW = np.cumsum(MU / 2.0)
    CS = np.cumsum(MU / 2.0 * UU)

    def g_vec(ts, pole=True, prime=True, smooth=True, lerch_coeff=0.25):
        """Suzuki's true screw function (lerch_coeff = +1/4), layer-
        selectable; lerch_coeff = -1 reproduces the w1-chain's gtil."""
        xf = np.abs(np.asarray(ts, dtype=float))
        kk = np.searchsorted(UU, xf, side="right")
        cw = np.where(kk > 0, CW[np.maximum(kk - 1, 0)], 0.0)
        cs = np.where(kk > 0, CS[np.maximum(kk - 1, 0)], 0.0)
        out = np.zeros_like(xf)
        if prime:
            out += xf * cw - cs
        if pole:
            out += -4.0 * (np.exp(xf / 2) + np.exp(-xf / 2) - 2.0)
        if smooth:
            out += xf / 2.0 * L_F - 0.25 * PHI1_F
            lb = np.empty_like(xf)
            for a in range(0, xf.size, 400):
                b = min(xf.size, a + 400)
                E = np.exp(-np.outer(2.0 * xf[a:b], _NN_L)
                           - 0.5 * xf[a:b, None])
                lb[a:b] = E @ _WTS
            out += lerch_coeff * lb
        return out

    # ================================================================ C0
    print("\nC0 -- the convention lock")
    mp.mp.dps = 40

    def f_lerch(tv):
        return mp.exp(-tv / 2) * mp.lerchphi(mp.exp(-2 * tv), 2,
                                             mp.mpf(1) / 4)

    PHI1m = mp.lerchphi(1, 2, mp.mpf(1) / 4)
    LLm40 = mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)

    def g_sm_true(tv):
        tv = mp.mpf(tv)
        if tv == 0:
            return mp.mpf(0)
        return LLm40 * tv / 2 - PHI1m / 4 + f_lerch(tv) / 4

    def g_sm_til(tv):
        tv = mp.mpf(tv)
        if tv == 0:
            return -PHI1m / 4 - PHI1m
        return LLm40 * tv / 2 - PHI1m / 4 - f_lerch(tv)

    A_paper = (mp.log(2 * mp.pi) - mp.digamma(2)) / 2
    devs_A, off_til = [], []
    for tv in (mp.mpf(10) ** -6, mp.mpf(10) ** -8):
        devs_A.append(abs((g_sm_true(tv) - tv / 2 * mp.log(tv)) / tv
                          - A_paper))
        off_til.append(abs((g_sm_til(tv) - g_sm_til(0)
                            - tv / 2 * mp.log(tv)) / tv - A_paper))
    check("C0.1 [E] THE BRACKET IS (1/4)(F(0) - F(t)): with Lerch "
          "coefficient +1/4 the origin expansion reproduces the "
          "paper's printed A = (1/2)(log 2pi - psi(2)) = %s "
          "(deviation %s at t = 1e-6, 1e-8 -> 0 like t log t) and "
          "g(0) = 0 (screw normalization); with the w1-chain's "
          "coefficient -1 the same read is off by %s (log-divergent) "
          "and g(0) = %s != 0 -- eq. (1.3) is LOCKED to +1/4 by the "
          "paper's own Sec. 2.2 data"
          % (mp.nstr(A_paper, 8),
             ["%.1e" % float(z) for z in devs_A],
             ["%.1f" % float(z) for z in off_til],
             mp.nstr(g_sm_til(0), 6)),
          float(devs_A[1]) < 1e-6 and float(off_til[1]) > 5.0)

    # ================================================================ P1
    print("\nP1 -- the projection lemma")
    x_ = sp.symbols("x_", real=True)
    p_ = sp.symbols("p_", real=True)
    D_ = sp.symbols("D_", positive=True)
    hat = sp.Piecewise((0, sp.Abs(x_ - p_) >= D_),
                       (1 - sp.Abs(x_ - p_) / D_, True))
    dphi = sp.integrate(sp.diff(hat, x_), (x_, p_ - D_, p_ + D_))
    check("P1.1 [E] the u-side mean-zero is AUTOMATIC on H^1_0: "
          "int phi' = 0 per hat (sympy exact), so int (sum x_i phi_i)' "
          "= 0 for EVERY coefficient vector; with int v' = v(a) - "
          "v(-a) = 0 on all of H^1_0 (fundamental theorem + Dirichlet),"
          " u = Dv lies in L^2_0 identically and P_a(Dv) = Dv: "
          "Suzuki's L^2_0 imposes NO linear condition on Galerkin "
          "coefficients (D : H^1_0 -> L^2_0 is a bijection, Sec. 8.2)",
          sp.simplify(dphi) == 0)

    rng = np.random.default_rng(SEED)
    T16 = core.parity_basis(hz, N_MODES)
    vecs = []
    for _ in range(N_VEC):
        cf = rng.standard_normal(N_MODES) / np.arange(1, N_MODES + 1)
        vecs.append((cf, cf @ T16))
    pj = (np.arange(Mz) - (Mz - 1) / 2.0) * D      # half-integer lattice
    xg = np.linspace(0.0, atil, 4001)

    def phi_of(V, xs):
        out = np.zeros_like(xs)
        for j in range(Mz):
            out += V[j] * np.maximum(0.0, 1.0 - np.abs(xs - pj[j]) / D)
        return out

    worst = 0.0
    for cf, v in vecs:
        V = np.concatenate([v, -v[::-1]])
        sc = float(np.max(np.abs(V)))
        worst = max(worst,
                    float(np.max(np.abs(phi_of(V, xg)
                                        + phi_of(V, -xg)))) / sc,
                    abs(phi_of(V, np.array([atil]))[0]) / sc,
                    abs(phi_of(V, np.array([-atil]))[0]) / sc,
                    abs(D * float(np.sum(V))) / sc)
    check("P1.2 [E] the v563 parity sector IS the odd subspace of "
          "H^1_0(-atil, atil), atil = alpha + D/2: on all %d odd test "
          "vectors (V_{M-1-j} = -V_j as hats on the half-integer "
          "lattice) Phi(-x) + Phi(x) = 0, Phi(+-atil) = 0, and "
          "int Phi = D sum V = 0 (worst %.1e) -- oddness is an EXTRA "
          "v-side mean-zero, a SUBSPACE of the Suzuki form domain; "
          "bookkeeping closes trivially" % (N_VEC, worst),
          worst < 1e-12)

    from numpy.polynomial.legendre import leggauss
    GX, GW = leggauss(16)
    cells = np.concatenate([[-atil], pj, [atil]])
    mids = 0.5 * (cells[:-1] + cells[1:])
    halfs = 0.5 * (cells[1:] - cells[:-1])
    pts = (mids[:, None] + halfs[:, None] * GX[None, :]).ravel()
    wts = (halfs[:, None] * GW[None, :]).ravel()
    cell_int = (g_vec(pts) * wts).reshape(Mz + 1, 16).sum(axis=1)
    J_full = float(np.sum(cell_int))
    cf0, v0 = vecs[0]
    V0 = np.concatenate([v0, -v0[::-1]])
    slopes0 = np.diff(np.concatenate([[0.0], V0, [0.0]])) / D
    s1 = float(np.sum(slopes0 * cell_int))
    s0 = float(np.sum(slopes0)) * D
    corr = -2.0 * s1 * s0 + G0_F * s0 * s0
    corr_mut = -2.0 * (2.0 * atil) * J_full + G0_F * (2.0 * atil) ** 2
    check("P1.3 [E-float] the Krein-kernel correction g(x-y) - g(x) - "
          "g(-y) + g(0) is ANNIHILATED on the derived objects: paired "
          "with u = Phi' it equals -2 (int g u)(int u) + g(0)"
          "(int u)^2 with int u = %.1e, correction = %.1e (int g u = "
          "%.4f finite); must-break: on the NON-mean-zero u = 1 the "
          "two kernels differ by %.4f != 0 -- P_a has content exactly "
          "OFF the form domain, none on it"
          % (s0, abs(corr), s1, corr_mut),
          abs(corr) < 1e-12 and abs(corr_mut) > 1.0)

    # ================================================================ P2
    print("\nP2 -- the theorem components (i)-(iii), exact layers")

    # ---- P2.1 [E]: (i) g'' = -2 cosh(t/2) + W, smooth density = +rho
    t = sp.symbols("t", positive=True)
    n = sp.symbols("n", integer=True, nonnegative=True)
    ratio = (2 * n + sp.Rational(1, 2)) ** 2 / (n + sp.Rational(1, 4)) ** 2
    ok_term = sp.simplify(ratio - 4) == 0
    g_pole = -4 * (sp.exp(t / 2) + sp.exp(-t / 2) - 2)
    lerch_dd = 4 * sp.exp(-t / 2) / (1 - sp.exp(-2 * t))
    g_dd = sp.diff(g_pole, t, 2) + lerch_dd / 4
    target = -2 * sp.cosh(t / 2) + sp.exp(-t / 2) / (1 - sp.exp(-2 * t))
    ok_smooth = sp.simplify(g_dd - target) == 0

    def G_p(tv):
        tv = abs(float(tv))
        kk = int(np.searchsorted(UU, tv, side="right"))
        if kk == 0:
            return 0.0
        return tv * float(CW[kk - 1]) - float(CS[kk - 1])

    dd_grid = np.arange(Mz) * D
    pr_point = np.array([(G_p((dd - 1) * D) - 2.0 * G_p(dd * D)
                          + G_p((dd + 1) * D)) / D for dd in range(Mz)])
    dev_at = float(np.max(np.abs(pr_point - (-c_at))))
    check("P2.1 [E] THEOREM (i): g'' = -2 cosh(t/2) + W with SMOOTH "
          "DENSITY +rho -- Lerch collapse x(1/4) gives g''_smooth = "
          "-2 cosh(t/2) + rho(t) off the atoms (sympy: collapse %s, "
          "structure %s); atom layer: (1/D)-second-difference of the "
          "prime staircase = tent read of W_at on ALL %d lags (max "
          "|diff| %.1e < 1e-11)" % (ok_term, ok_smooth, Mz, dev_at),
          ok_term and ok_smooth and dev_at < 1e-11)

    # ---- P2.2 [E]: (ii) the TFPT tent reads, exact at every d >= 1
    mp.mp.dps = 55
    Dm = mp.mpf(D)
    LLm = mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)
    PHI1m55 = mp.lerchphi(1, 2, mp.mpf(1) / 4)
    EULER_MP = mp.euler
    LOGPI_MP = mp.log(mp.pi)

    def rho_mp(x):
        return mp.exp(-x / 2) / (-mp.expm1(-2 * x))

    def tent_mp(x, dd):
        v = 1 - abs(x - dd * Dm) / Dm
        return v if v > 0 else mp.mpf(0)

    def g_sm_mp(tv):
        tv = mp.mpf(tv)
        if tv == 0:
            return mp.mpf(0)
        return (LLm * tv / 2 - PHI1m55 / 4
                + mp.exp(-tv / 2)
                * mp.lerchphi(mp.exp(-2 * tv), 2, mp.mpf(1) / 4) / 4)

    def point_suz(dd):
        return (g_sm_mp(abs(dd - 1) * Dm) - 2 * g_sm_mp(dd * Dm)
                + g_sm_mp((dd + 1) * Dm)) / Dm

    def c_ar_verbatim(dd):
        if dd >= 1:
            return -mp.quad(lambda x: tent_mp(x, dd) * rho_mp(x),
                            [(dd - 1) * Dm, dd * Dm, (dd + 1) * Dm])
        W_ = Dm

        def integ(x):
            S = (tent_mp(x, 0) + tent_mp(-x, 0)) / 2
            return (mp.exp(-2 * x) - S * mp.exp(-x / 2)) / (-mp.expm1(-2 * x))
        return (-(EULER_MP + LOGPI_MP) + 2 * mp.quad(integ, [0, W_])
                - mp.log(-mp.expm1(-2 * W_)))

    res_ii = []
    for dd in (1, 2, 3, 10, 50):
        lhs = c_ar_verbatim(dd)
        res_ii.append(abs(lhs + point_suz(dd)) / abs(lhs))
    kappa = c_ar_verbatim(0) + point_suz(0)
    kappa_closed = (2 / Dm * mp.quad(lambda x: x * rho_mp(x), [0, Dm])
                    + 2 * mp.quad(rho_mp, [Dm, 1, 5, mp.inf])
                    + (f_lerch(Dm) - PHI1m55) / (2 * Dm))
    res_far = []
    for dd in (3, 10, 50):
        res_far.append(abs(c_ar_verbatim(dd) - mp.mpf(float(c_ar[dd])))
                       / abs(c_ar_verbatim(dd)))
    c_at_direct = np.zeros(Mz)
    for u_j, m_j in zip(uu, mm):
        c_at_direct -= (m_j / 2.0) * (
            np.maximum(0.0, 1.0 - np.abs(dd_grid - u_j) / D)
            + np.maximum(0.0, 1.0 - (dd_grid + u_j) / D))
    dev_atl = float(np.max(np.abs(c_at_direct - c_at)))
    check("P2.2 [E] THEOREM (ii): A_arch = -g''_smooth EXACTLY, at "
          "EVERY lag -- c_ar[d] = -<W_sm, tent_d> at d = 1, 2, 3, 10, "
          "50 (worst rel %s < 1e-25, NO constant, NO scalar), and the "
          "candidate origin constant kappa = c_ar[0] + point-read(0) "
          "= %s VANISHES (closed-identity residual %s): the v563 "
          "near-cell scheme IS Suzuki's origin bookkeeping; v563 "
          "float far lags match the exact assembly (worst %s); atom "
          "layer literal on all %d lags (max |diff| %.1e); L = %s"
          % (mp.nstr(max(res_ii), 3), mp.nstr(kappa, 6),
             mp.nstr(abs(kappa - kappa_closed), 3),
             mp.nstr(max(res_far), 3), Mz, dev_atl, mp.nstr(LLm, 25)),
          max(res_ii) < mp.mpf(10) ** -25
          and abs(kappa) < mp.mpf(10) ** -40
          and abs(kappa - kappa_closed) < mp.mpf(10) ** -40
          and max(res_far) < mp.mpf(10) ** -10 and dev_atl < 1e-14)

    # ---- the Suzuki-side lag assembly, layerwise (declared route)
    XS = 0.5 * D * (GX + 1)
    WS = 0.5 * D * GW
    DIFF = (XS[:, None] - XS[None, :]).ravel()
    W2 = np.outer(WS, WS).ravel()

    t_lag = time.time()
    II_s = np.empty(Mz + 2)
    for kk_ in range(Mz + 2):
        II_s[kk_] = float(np.dot(W2, g_vec(kk_ * D + DIFF, pole=False,
                                           prime=False)))
    cgal_sm = np.empty(Mz)
    for dd in range(Mz):
        cgal_sm[dd] = (2.0 * II_s[dd] - II_s[abs(dd - 1)]
                       - II_s[dd + 1]) / (D * D)
    mp.mp.dps = 30
    II_b = {kk_: mp.quad(lambda s: g_sm_mp(abs(kk_ * Dm + s))
                         * (Dm - abs(s)), [-Dm, 0, Dm])
            for kk_ in range(7)}

    def cgal_sm_exact(dd):
        return (2 * II_b[dd] - II_b[abs(dd - 1)] - II_b[dd + 1]) / Dm ** 2

    for dd in range(3):
        cgal_sm[dd] = float(cgal_sm_exact(dd))

    def K_f(x):
        u = np.abs(x) / D
        return np.where(u <= 1.0, D * (2.0 / 3.0 - u ** 2 + u ** 3 / 2.0),
                        np.where(u < 2.0, D * (2.0 - u) ** 3 / 6.0, 0.0))

    cgal_prime = np.zeros(Mz)
    for u_j, m_j in zip(uu, mm):
        cgal_prime -= 0.5 * m_j * (K_f(u_j - dd_grid) + K_f(u_j + dd_grid))
    Xp = math.exp(D / 2) + math.exp(-D / 2) - 2.0
    poleK = 2.0 * np.cosh(np.arange(Mz) * D / 2.0) * 16.0 * Xp ** 2 / (D * D)
    print("layerwise Suzuki lags: %d smooth Galerkin lags in %.1f s"
          % (Mz, time.time() - t_lag))

    # ---- P2.3 [E]: (iii) Galerkin = B-spline read of W + pole read
    def K_mp(x):
        u = abs(x) / Dm
        if u >= 2:
            return mp.mpf(0)
        if u <= 1:
            return Dm * (mp.mpf(2) / 3 - u ** 2 + u ** 3 / 2)
        return Dm * (2 - u) ** 3 / 6

    def g_full_mp(tv):
        tv = abs(mp.mpf(tv))
        assert tv < mp.log(2)
        return -4 * (mp.exp(tv / 2) + mp.exp(-tv / 2) - 2) + g_sm_mp(tv)

    def poleK_closed(dd):
        X_ = mp.exp(Dm / 2) + mp.exp(-Dm / 2) - 2
        return 2 * mp.cosh(dd * Dm / 2) * 16 * X_ ** 2 / Dm ** 2

    II_h = {kk_: mp.quad(lambda s: g_full_mp(kk_ * Dm + s) * (Dm - abs(s)),
                         [-Dm, 0, Dm]) for kk_ in range(7)}
    res_full, res_route = [], []
    for dd in (0, 1, 2, 5):
        heavy = (2 * II_h[dd] - II_h[abs(dd - 1)] - II_h[dd + 1]) / Dm ** 2
        assembled = poleK_closed(dd) + cgal_sm_exact(dd)
        res_full.append(abs(heavy - assembled) / abs(heavy))
        refined = cgal_sm[dd] + poleK[dd]
        res_route.append(abs(float(heavy) - refined) / abs(float(heavy)))
    dens5 = -mp.quad(lambda x: rho_mp(x) * K_mp(x - 5 * Dm),
                     [(5 + j) * Dm for j in (-2, -1, 0, 1, 2)])
    res_dens = abs(cgal_sm_exact(5) - dens5) / abs(dens5)
    # closed atomic K-read vs exact kink-split integrals (log 3 cells)
    def prime_mp(tv):
        tv = abs(tv)
        kk_ = int(np.searchsorted(UU, float(tv), side="right"))
        if kk_ == 0:
            return mp.mpf(0)
        return tv * mp.mpf(float(CW[kk_ - 1])) - mp.mpf(float(CS[kk_ - 1]))

    def II_prime_mp(kk_):
        pts_ = [-Dm, mp.mpf(0), Dm]
        for u_j in [mp.mpf(float(u)) for u in UU[:6]]:
            s_kink = u_j - kk_ * Dm
            if -Dm < s_kink < Dm:
                pts_.append(s_kink)
        return mp.quad(lambda s: prime_mp(kk_ * Dm + s) * (Dm - abs(s)),
                       sorted(pts_))

    devs_x = []
    for dd in (72, 73, 74):
        exact = float((2 * II_prime_mp(dd) - II_prime_mp(dd - 1)
                       - II_prime_mp(dd + 1)) / Dm ** 2)
        devs_x.append(abs(exact - cgal_prime[dd]))
    # boundary constants of the K-side dictionary
    Btil = [float(c_ar_verbatim(dd) - cgal_sm_exact(dd) / Dm)
            for dd in range(3)]
    check("P2.3 [E] THEOREM (iii): cgal(d) = poleK(d) - <W, K_d> -- "
          "heavy exact route = closed poleK + smooth read at d = 0, 1, "
          "2, 5 (worst rel %s < 1e-25); smooth DENSITY read exact: "
          "cgal_sm(5) = -<rho, K_5> (rel %s < 1e-25); layerwise float "
          "route vs exact heavy route (worst rel %.1e < 1e-9); closed "
          "B-spline atom read = exact kink-split integrals at the "
          "log 3 cells (max |diff| %.1e < 1e-14); boundary constants "
          "Btil(0) = %.12f, Btil(1) = %.12f, Btil(2) = %.12f"
          % (mp.nstr(max(res_full), 3), mp.nstr(res_dens, 3),
             max(res_route), max(devs_x), Btil[0], Btil[1], Btil[2]),
          max(res_full) < mp.mpf(10) ** -25
          and res_dens < mp.mpf(10) ** -25
          and max(res_route) < 1e-9 and max(devs_x) < 1e-14)

    # ---- P2.4 [E]: the verbatim-transfer identity (C0, quantitative)
    II_t = {}
    for kk_ in (4, 5, 6, 8, 9, 10):
        II_t[kk_] = float(np.dot(W2, g_vec(kk_ * D + DIFF, pole=False,
                                           prime=False, lerch_coeff=-1.0)))
    res_tr = []
    for dd in (5, 9):
        ctil = (2.0 * II_t[dd] - II_t[dd - 1] - II_t[dd + 1]) / (D * D)
        res_tr.append(abs(ctil + 4.0 * cgal_sm[dd]) / abs(ctil))
    check("P2.4 [E-float] THE TRANSFER IDENTITY: the w1-chain's kernel "
          "gtil = g - (5/4) Lerch satisfies cgal_sm(gtil) = "
          "-4 cgal_sm(g) (checked d = 5, 9: rel %s < 1e-10), so every "
          "measured ratio of the chain transfers verbatim: "
          "cgal(gtil)/(-4 D c_ar) == cgal(g)/(+D c_ar) -- the frozen-"
          "window portability table (h = 285/540/997) and the moment-"
          "law numbers hold for the TRUE dictionary number for number, "
          "only relabeled (-4D two-layer -> +D one-scalar)"
          % ("%.1e" % max(res_tr)), max(res_tr) < 1e-10)

    # ---- P2.5 [E-quad]: the derived second-order law + D^8 typing
    ws_ = sp.symbols("ws_", positive=True)
    rho_sym = sp.exp(-ws_ / 2) / (1 - sp.exp(-2 * ws_))
    jets = [sp.lambdify(ws_, sp.diff(rho_sym, ws_, 2 * j), "mpmath")
            for j in range(5)]

    def ratio_exact(dd):
        Krd = mp.quad(lambda xx: rho_mp(xx) * K_mp(xx - dd * Dm),
                      [(dd + j) * Dm for j in (-2, -1, 0, 1, 2)])
        Trd = mp.quad(lambda xx: rho_mp(xx) * tent_mp(xx, dd),
                      [(dd - 1) * Dm, dd * Dm, (dd + 1) * Dm])
        return Krd / (Dm * Trd)

    def ratio_pred(dd, order8=False):
        tv = dd * Dm
        f, g2, g4, g6, g8 = (jj(tv) for jj in jets)
        num = f + Dm ** 2 / 6 * g2 + Dm ** 4 / 80 * g4 \
            + 17 * Dm ** 6 / 30240 * g6
        den = f + Dm ** 2 / 12 * g2 + Dm ** 4 / 360 * g4 \
            + Dm ** 6 / 20160 * g6
        if order8:
            num += 31 * Dm ** 8 / 1814400 * g8
            den += Dm ** 8 / 1814400 * g8
        return num / den

    rows24 = []
    for dd in (5, 9, 16):
        re_, rp_ = float(ratio_exact(dd)), float(ratio_pred(dd))
        rows24.append((dd, re_, rp_, abs(re_ - rp_) / (re_ - 1.0)))
    x8, Dp = sp.symbols("x8", nonnegative=True), sp.symbols(
        "Dp", positive=True)
    mphi_all = {2 * kk: 2 * sp.integrate((1 - x8 / Dp) * x8 ** (2 * kk),
                                         (x8, 0, Dp)) for kk in range(5)}
    ok_m8 = sp.simplify(mphi_all[8] - Dp ** 9 / 45) == 0
    mK8 = sum(sp.binomial(8, j) * mphi_all[j] * mphi_all[8 - j]
              for j in (0, 2, 4, 6, 8))
    ok_K8 = sp.simplify(mK8 - 31 * Dp ** 10 / 45) == 0
    expl = []
    for dd in (3, 4, 5, 8, 12):
        re_ = ratio_exact(dd)
        r6 = abs(re_ - ratio_pred(dd))
        r8 = abs(re_ - ratio_pred(dd, order8=True))
        expl.append((dd, float(r6), float(r8), float(1 - r8 / r6)))
    check("P2.5 [E-quad] THEOREM (iv), the derived O(D^2) law: the "
          "exact tent/B-spline read ratio matches R(d) = 1 + (D^2/12)"
          "(rho''/rho)(dD) + ... (-> 1 + 1/(6 d^2)) to %s of the "
          "excess at d = 5, 9, 16 (ratios %s); the D^8 bracket order "
          "is DERIVED (sympy: m_8 = D^9/45 %s, B-spline 31 D^10/45 %s) "
          "and explains %s of the D^6-law residual at d = 3, 4, 5, 8, "
          "12 -- the remainder is bracket truncation, typed"
          % ("%.4f" % max(z for *_, z in rows24),
             ["%.6f" % b for _, b, _, _ in rows24], ok_m8, ok_K8,
             ["%.0f%%" % (100 * e) for *_, e in expl]),
          max(z for *_, z in rows24) < 0.02 and ok_m8 and ok_K8
          and min(e for *_, e in expl) >= 0.70)

    # ================================================================ P3
    print("\nP3 -- the form equality on the common odd sector (the bar)")
    R_pred = np.ones(Mz)
    tt = np.arange(3, Mz) * D
    jets_np = [sp.lambdify(ws_, sp.diff(rho_sym, ws_, 2 * j), "numpy")
               for j in range(4)]
    f0v, f2v, f4v, f6v = (jj(tt) for jj in jets_np)
    R_pred[3:] = ((f0v + D ** 2 / 6 * f2v + D ** 4 / 80 * f4v
                   + 17 * D ** 6 / 30240 * f6v)
                  / (f0v + D ** 2 / 12 * f2v + D ** 4 / 360 * f4v
                     + D ** 6 / 20160 * f6v))

    # the ONE-SCALAR dictionary stages (true convention)
    c_s1 = (cgal_sm + cgal_prime) / D
    c_s2 = c_s1.copy()
    for dd in range(3):
        c_s2[dd] = cgal_sm[dd] / D + cgal_prime[dd] / D + Btil[dd]
    c_s3 = c_s2.copy()
    c_s3[3:] = cgal_sm[3:] / (D * R_pred[3:]) + cgal_prime[3:] / D
    c_s4 = c_s3 - cgal_prime / D + c_at
    c_s5 = c_s4.copy()
    for dd in range(3, 13):
        c_s5[dd] = cgal_sm[dd] / (D * float(ratio_exact(dd))) + c_at[dd]

    A_T = core.odd_toeplitz(c_tfpt, Mz)
    stages = (("one-scalar 1/D", core.odd_toeplitz(c_s1, Mz)),
              ("+Btil(0..2)", core.odd_toeplitz(c_s2, Mz)),
              ("+moment law", core.odd_toeplitz(c_s3, Mz)),
              ("+measure atoms", core.odd_toeplitz(c_s4, Mz)),
              ("+measure smooth", core.odd_toeplitz(c_s5, Mz)))
    AT16 = T16 @ (A_T @ T16.T)
    nrm16 = float(np.linalg.norm(AT16, 2))
    print("   16-mode block operator norms ||T16 (A_T - A_S) T16'|| / "
          "||T16 A_T T16'|| (nrm16 = %.6f):" % nrm16)
    blk_r = {}
    for lab, A_ in stages:
        blk_r[lab] = float(np.linalg.norm(
            T16 @ ((A_T - A_) @ T16.T), 2)) / nrm16
        print("     %-16s %.3e" % (lab, blk_r[lab]))

    A_S4, A_S5 = stages[3][1], stages[4][1]
    rows = []
    for cf, v in vecs:
        qT = float(v @ (A_T @ v))
        qS4 = float(v @ (A_S4 @ v))
        qS5 = float(v @ (A_S5 @ v))
        rows.append((qT, abs(qT - qS4) / abs(qT),
                     abs(qT - qS5) / abs(qT),
                     abs(qT - qS5) / (nrm16 * float(cf @ cf))))
    print("   per-vector deviations:")
    print("     |Q_T|            : %s"
          % ["%.3e" % abs(q) for q, *_ in rows])
    print("     rel dev (stage 4): %s" % ["%.2e" % z for _, z, _, _ in rows])
    print("     rel dev (stage 5): %s" % ["%.2e" % z for _, _, z, _ in rows])
    print("     scale-fixed (s5) : %s" % ["%.2e" % z for *_, z in rows])
    max_rel4 = max(z for _, z, _, _ in rows)
    max_rel5 = max(z for _, _, z, _ in rows)
    max_sf = max(z for *_, z in rows)
    check("P3.1 [E-float, central] THE TASK BAR: full form equality on "
          "the common odd sector, 10 odd 16-mode vectors, one-scalar "
          "measure-level dictionary (both layers re-binned): per-"
          "vector |Q_T - Q_S|/|Q_T| max %.2e < 1e-4 (median %.2e); "
          "scale-fixed max %.2e; 16-mode block operator-norm ratio "
          "%.2e (one-scalar stage %.2e).  HONEST: with the derived "
          "moment law instead of the near-cell exact ratios (stage 4) "
          "the max is %.2e -- the difference is the typed D^8 bracket "
          "truncation of P2.5 at d = 3, 4 hitting near-cancellation "
          "denominators |Q_T| ~ %.2f << form scale %.1f"
          % (max_rel5, float(np.median([z for _, _, z, _ in rows])),
             max_sf, blk_r["+measure smooth"], blk_r["one-scalar 1/D"],
             max_rel4, min(abs(q) for q, *_ in rows), nrm16),
          max_rel5 < BAR_TASK)

    A_P = core.odd_toeplitz(poleK, Mz)
    evP = np.linalg.eigvalsh(A_P)
    rankP = int(np.sum(np.abs(evP) > 1e-10 * np.max(np.abs(evP))))
    check("P3.2 [E-float] the separated pole block is rank %d <= 2 "
          "after parity projection (the cosh(dD/2) Toeplitz is spanned "
          "by e^{+t/2}, e^{-t/2}): the pole block in THEOREM (i) is "
          "the declared finite-rank freedom, not a leak" % rankP,
          rankP <= 2)

    if not FAILS:
        VERDICT = "W1-THEOREM"
    elif any(f.startswith("P2") or f.startswith("P1")
             or f.startswith("C0") for f in FAILS):
        VERDICT = "W1-THEOREM-GAP"
    else:
        VERDICT = "MIXED"
    print("\nVERDICT: %s -- the measure-level W1 statement on Suzuki's "
          "TRUE screw function: one scalar 1/D, sign positivity-"
          "compatible, L^2_0 projection closed (odd hat sector = "
          "subspace of the Suzuki form domain; u-side mean-zero "
          "automatic); the earlier chain's numbers transfer verbatim "
          "via cgal(gtil) = -4 cgal(g)" % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
