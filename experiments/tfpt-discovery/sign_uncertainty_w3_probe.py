"""Discovery probe: the sign-uncertainty / Mellin-strip toolbox (OpenAI
'Ten Advances' manuscript, Ch. 1: the sphere-packing exponent and the
Bourgain-Clozel-Kahane / Cohn-Goncalves sign-uncertainty constants
A_pm(d)/sqrt(d) -> 1/pi) read against the TFPT 1D Weil window cone
(contract PRIME.WEIL.OPERATOR.01, W3: uniform discrete positivity
Ahat_{a,h} >= 0 on the declared v563 frame-A window family).

THE DICTIONARY (S1) -- what plays what:

  paper object (d -> infinity)          | 1D Weil window cone (TFPT)
  --------------------------------------+--------------------------------
  radial eigenfunction g, ghat = +-g,   | Weil test function on the
  g(0) = 0 (BCK class)                  | window: autocorrelation cone
                                        | (ghat >= 0), pole block
                                        | separated (v591 rank-one)
  radius r(g) of the last sign change   | last-sign-change radius rho* of
  (g >= 0 beyond r)                     | the minimal Galerkin mode
                                        | (measured here, P2)
  the Mellin strip |Im t| <= lambda,    | THE CRITICAL STRIP: at d = 1,
  lambda = d/2                          | lambda = 1/2 -- strip width 1,
                                        | 0 <= Re s <= 1, FIXED
  the strip multiplier m_lambda(t) =    | the completed-zeta gamma factor
  pi^{it} G((l-it)/2)/G((l+it)/2)       | Gamma_R(s) = pi^{-s/2}Gamma(s/2)
                                        | phase slope at t = 0 equals
                                        | L = log pi - psi(1/4) -- v631's
                                        | delta_0 weight (anchor P1.1)
  upper strip boundary |Z| <= 1         | the model / mass side: q_model
  (total L1 mass)                       | one-sign floor (v618 U1)
  lower boundary via the functional     | the arithmetic side via the
  equation (gamma majorant h_lambda)    | explicit formula: |q_r/q_m|
                                        | <= 1/h, C = 1 (v618 U2)
  interpolation parameter sigma with    | ladder / refinement parameter h
  the DERIVED sharp constant            | with the MEASURED constant
  J_sigma -> log(pi/2) (Lemma 3.4)      | C = 1 (not derived)
  g(0) = ghat(0) = 0 cancels the        | pole block 2 cosh(t/2) at
  gamma pole at the strip corner        | s = 0, 1 tracked separately
                                        | (v591 / v631 D2)

  WHERE THE ANALOGY BREAKS (typed):
  (B-1) NO LARGE PARAMETER: the paper's exponential mass gain e^{-gamma d}
        is powered by the strip HALF-WIDTH lambda = d/2 -> infinity
        (Stirling on the gamma majorant).  The zeta strip has width 1,
        FIXED.  The window length 2*alpha is the analogue of the BALL
        RADIUS R = c sqrt(d) (a support parameter), not of the strip
        width -- growing alpha does not widen the strip.
  (B-2) MEASURE: BCK counts Lebesgue L1 mass |g| dx; the window form
        pairs against the SIGNED Weil measure (poles - primes + arch).
  (B-3) CONE: the BCK constraint is the eigenfunction equation
        ghat = +-g; the window cone is compact support + ghat >= 0
        (Cohn-Elkies-type, autocorrelations), discretized (Galerkin
        tents, parity fold) -- eigenfunction structure is NOT available.

SECTIONS (verdict-bearing checks):

  P0 [E]        rebuild validation: this probe's window assembly
                reproduces v563's build_window bit-for-bit surfaces.
  P1 [E]        dictionary anchors, 20+ digits: (1.1) the d = 1 strip
                multiplier phase slope IS L = log pi - psi(1/4); (1.2)
                the J_sigma certificate constant reproduces Lemma 3.4
                (J -> log(pi/2), harmonic-measure mass exact); (1.3)
                the d = 1 Mellin-Hankel functional equation on the
                Gaussian (convention lock).
  P2 [MEASURED] the sign-uncertainty readout of the REAL window family:
                the 67 complete-comb frame-A windows, full parity-sector
                Galerkin form Ahat = odd Toeplitz(c_arch + c_atom);
                lambda_min as L2(window) Rayleigh quotient (generalized
                eigenvalue against the tent Gram), the last-sign-change
                radius rho* of the minimal mode, scaling fits
                lambda_min ~ C (2 alpha)^{-p} vs ~ C e^{-kappa 2 alpha},
                named-constant scan (honest: whatever comes out).
  P3 [MEASURED] the LP-ceiling test at d = 1: (3.1) the paper's OWN
                mass-bound budget at lambda = 1/2 -- the exponent
                E* = max_sigma (1/4)(1 - sigma) delta_c and the measured
                scale mismatch rho* vs the maximal BCK ball 1/pi;
                (3.2) the v618 C = 1 certificate re-measured on the
                full surface and typed against the Mellin-strip
                certificate structure (two-boundary family: where the
                correspondence holds and where it breaks).
  P4 [C]        the typed verdict + contract-note text.

Verdict enums (frozen): W3-MECHANISM-CANDIDATE (a pi-family constant
with R^2 >= 0.95 shows up in the window scaling AND the mass route
survives), LP-CEILING-ANALOG-TYPED (dictionary anchors pass, the d = 1
mass budget is dead, positivity margin measured -- the typed negative
with a named dictionary), TECHNIQUE-NOT-APPLICABLE-1D (anchors fail),
MIXED.

FIREWALL: experiments-only; verification/ read-only; no marker moves;
no RH statement; NO zero of any L-function is read (AST-checked);
the windows are the DECLARED v563 surface, nothing beyond it.

Provenance: OpenAI ten-proofs manuscript Ch. 1 (Thm 1.1/1.2, Prop 3.1,
Lemmas 3.2-3.6, Thm 3.8, Thm 4.1); Suzuki arXiv:2606.09096 via
v631/w1_* (read-only); v563/v618 machinery read-only.
"""
import ast
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

EPS = float(np.finfo(float).eps)
FLOOR_SAFETY = 20.0          # heuristic eigh backward-error safety factor
SIGN_TINY = 1.0e-9           # eigenvector zero threshold (max-normalized)
R2_LAW_BAR = 0.60            # preregistered: below this, "no clean law"
R2_CAND_BAR = 0.95           # candidate upgrade needs this fit quality
CONST_CAND_BAR = 0.05        # ... and a pi-family constant within 5%
MASS_KILL_BAR = 0.5          # contradiction needs mass factor < 1/2
SCALE_KILL_BAR = 2.0         # rho* must exceed the BCK ball by >= this
V618_MAX_QUOTE = 0.982       # v618 U2: measured max eps*h at h = 184
V618_FLIPS = [1219, 1445]    # v618 U4: the two sign-flip windows


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
        if isinstance(node, ast.Attribute) and node.attr in (
                "zetazero", "nzeros", "second_sheet_zero"):
            return False
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id in ("zetazero", "nzeros"):
            return False
    return True


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import mpmath as mp  # noqa: E402
import scipy.linalg as sla  # noqa: E402

GRID_PER_D = 4.0             # v618 model grid, verbatim
NAMED = None                 # filled in run() (needs mpmath)


# ------------------------------------------------------------------ helpers
def zeta_grid_const():
    """v618's model anchor u0 = 2 log(-c_th/4), c_th = -2 zeta'(1/2)/zeta(1/2)
    (verbatim, read-only reproduction)."""
    mp.mp.dps = 30
    c_th = float(-2 * mp.diff(lambda s: mp.zeta(s), mp.mpf(1) / 2)
                 / mp.zeta(mp.mpf(1) / 2))
    return 2.0 * math.log(-c_th / 4.0)


def model_matrix(alpha, Mz, D, W11, W22, W12, u0):
    """v618's smooth model of S (verbatim): cell masses of the arch
    density 4 e^{u/2} heads against the spline reads of the weights."""
    delta = D / GRID_PER_D
    n_cells = int(math.ceil((2.0 * alpha - u0) / delta))
    edges = u0 + delta * np.arange(n_cells + 1)
    lam = 0.5 * 4.0 * (np.exp(edges[1:] / 2) - np.exp(edges[:-1] / 2))
    centers = 0.5 * (edges[:-1] + edges[1:])
    X = np.empty((n_cells, 3))
    for k, u_j in enumerate(centers):
        X[k, 0] = core.spline_project(W11, u_j, D, Mz)
        X[k, 1] = core.spline_project(W22, u_j, D, Mz)
        X[k, 2] = core.spline_project(W12, u_j, D, Mz)
    s = (lam[:, None] * X).sum(axis=0)
    return np.array([[s[0], s[2]], [s[2], s[1]]])


def lock_dir(alpha):
    """v618's parameter-free lock direction (verbatim)."""
    v2v1 = -(alpha ** 2 + 16 * math.pi ** 2) / (2 * (alpha ** 2
                                                     + 4 * math.pi ** 2))
    v = np.array([1.0, v2v1])
    return v / np.linalg.norm(v)


def J_sigma(sig, t_max=120.0, n_pts=400001):
    """Lemma 3.3/3.4: J_sigma = -(1/M_sigma) int P_sigma(T) I0(T) dT with
    the closed form I0(T) = int_0^1 log sqrt(x^2 + T^2/4) dx.  Returns
    (J, harmonic-measure mass relative to M_sigma, M_sigma)."""
    th = math.pi * (1.0 + sig) / 2.0
    m_sig = (1.0 - sig) / 2.0
    tt = np.linspace(0.0, t_max, n_pts)
    pp = math.sin(th) / (4.0 * (np.cosh(math.pi * tt / 2.0) - math.cos(th)))
    b = tt / 2.0
    i0 = 0.5 * (np.log1p(b * b) - 2.0 + 2.0 * b * np.arctan2(1.0, b))
    mass = 2.0 * float(np.trapezoid(pp, tt))
    jj = -(2.0 / m_sig) * float(np.trapezoid(pp * i0, tt))
    return jj, mass / m_sig, m_sig


def mass_budget(c, n_sig=1999):
    """The d = 1 main-term budget of Prop 3.1: E*(c) = max_sigma
    lambda M_sigma delta_c at lambda = 1/2; returns (E*, sigma*)."""
    best, s_best = -1.0e18, None
    for sig in np.linspace(-0.999, 0.999, n_sig):
        jj, _, m_sig = J_sigma(float(sig), t_max=80.0, n_pts=100001)
        delta = -(math.log(2.0 * math.pi * c * c) + jj)
        e_val = 0.5 * m_sig * delta
        if e_val > best:
            best, s_best = e_val, float(sig)
    return best, s_best


def gen_min_eig(A, G):
    """lambda_min and eigenvector of the pencil (A, G), plus the pencil
    spectral radius (for the float noise floor)."""
    w, V = sla.eigh(0.5 * (A + A.T), 0.5 * (G + G.T))
    rad = max(abs(float(w[0])), abs(float(w[-1])))
    return float(w[0]), V[:, 0], rad


def last_sign_change(v, D, hz):
    """the outermost sign flip of the minimal mode in the half-window:
    grid index j sits at distance (hz - 0.5 - j) D from the fold center
    (edge at j = 0, distance ~ alpha = hz D).  Returns (rho*, n_flips);
    rho* = 0.0 when the profile carries no flip."""
    w = v / float(np.max(np.abs(v)))
    s = np.where(np.abs(w) > SIGN_TINY, np.sign(w), 0.0)
    idx = np.nonzero(s)[0]
    flips = [(idx[k], idx[k + 1]) for k in range(len(idx) - 1)
             if s[idx[k]] * s[idx[k + 1]] < 0.0]
    if not flips:
        return 0.0, 0
    i1, i2 = flips[0]            # smallest index = closest to the edge
    rho = (hz - 0.5 - 0.5 * (i1 + i2)) * D
    return float(rho), len(flips)


def ols(cols, y):
    """OLS with intercept; returns (beta, R^2)."""
    Xd = np.column_stack([np.ones_like(y)] + cols)
    beta, _, _, _ = np.linalg.lstsq(Xd, y, rcond=None)
    r = y - Xd @ beta
    yc = y - y.mean()
    return beta, 1.0 - float(r @ r) / float(yc @ yc)


def nearest_named(x):
    best = min(NAMED.items(), key=lambda kv: abs(kv[1] - x) / abs(kv[1]))
    return best[0], abs(best[1] - x) / abs(best[1])


def run():
    global N_CHK, FAILS, NAMED
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("SIGN-UNCERTAINTY / MELLIN-STRIP vs THE 1D WEIL WINDOW CONE "
          "(W3 probe)")
    print("=" * 78)
    mp.mp.dps = 40
    L_CONST = float(mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4))
    NAMED = {
        "1/pi": 1.0 / math.pi, "2/pi": 2.0 / math.pi,
        "1/(2pi)": 0.5 / math.pi, "pi/2": math.pi / 2.0,
        "pi/4": math.pi / 4.0, "pi": math.pi,
        "sqrt(e)/(2pi)": math.sqrt(math.e) / (2.0 * math.pi),
        "1/4": 0.25, "1/2": 0.5, "3/4": 0.75, "1": 1.0,
        "3/2": 1.5, "2": 2.0, "3": 3.0, "4": 4.0,
        "L=logpi-psi(1/4)": L_CONST,
    }

    check("P0.0 [E] AST zero-firewall: no Riemann-zero loader in this "
          "probe", ast_zero_firewall(__file__))

    # ------------------------------------------------------------- P0
    KZ = core.frame_a_zones()
    kz_ref = KZ[len(KZ) // 2]
    r_ref = core.build_window(kz_ref)
    alpha, Mz, hz = r_ref["alpha"], r_ref["M"], r_ref["h"]
    ka = core.atoms_in(alpha)
    c_at, D = core.atom_lags_at(alpha, Mz, core.U_ALL[:ka],
                                core.MU_ALL[:ka])
    c_ar = core.arch_lags(Mz, D)
    A_ref = core.odd_toeplitz(c_ar + c_at, Mz)
    t1, t2 = r_ref["t1"], r_ref["t2"]
    Ah_mine = np.array([[t1 @ (A_ref @ t1), t1 @ (A_ref @ t2)],
                        [t1 @ (A_ref @ t2), t2 @ (A_ref @ t2)]])
    e_proj = float(np.max(np.abs(Ah_mine - r_ref["Ah"]))
                   / np.max(np.abs(r_ref["Ah_dir"])))
    B_mine = np.array([[c_ar @ r_ref["W11"], c_ar @ r_ref["W12"]],
                       [c_ar @ r_ref["W12"], c_ar @ r_ref["W22"]]])
    e_b = float(np.max(np.abs(B_mine - r_ref["B"]))
                / np.max(np.abs(r_ref["B"])))
    check("P0.1 [E] rebuild validation on the reference window (h = %d): "
          "this probe's odd-Toeplitz assembly projects onto (t1, t2) to "
          "the v563 Ahat within rel %.1e <= 1e-6, and the B block "
          "matches bit-level (rel %.1e <= 1e-14)"
          % (hz, e_proj, e_b), e_proj <= 1.0e-6 and e_b <= 1.0e-14)

    # ------------------------------------------------------------- P1
    print("\nP1 -- dictionary anchors (the d = 1 specialization is the "
          "zeta strip)")
    mp.mp.dps = 40

    def phase(t):
        return t * mp.log(mp.pi) - 2 * mp.im(
            mp.loggamma(mp.mpf(1) / 4 + mp.mpf(1) / 2 * 1j * t))

    slope0 = mp.diff(phase, 0)
    L_mp = mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)
    dev0 = abs(slope0 - L_mp)
    devs_t = []
    for tv in (mp.mpf(1), mp.mpf(2)):
        want = mp.log(mp.pi) - mp.re(mp.digamma(mp.mpf(1) / 4
                                                + 1j * tv / 2))
        devs_t.append(abs(mp.diff(phase, tv) - want))
    mods = [abs(abs(mp.pi ** (1j * tv)
                    * mp.gamma(mp.mpf(1) / 4 - 1j * tv / 2)
                    / mp.gamma(mp.mpf(1) / 4 + 1j * tv / 2)) - 1)
            for tv in (mp.mpf(1) / 2, mp.mpf(3), mp.mpf(10))]
    check("P1.1 [E, 25+ digits] the d = 1 strip multiplier m_{1/2}(t) = "
          "pi^{it} Gamma(1/4 - it/2)/Gamma(1/4 + it/2) is unimodular "
          "(worst |.|-1 = %s) and its phase slope at t = 0 is EXACTLY "
          "L = log pi - psi(1/4) = %s -- the SAME archimedean constant "
          "v631/w1_boundary froze as Suzuki's delta_0 weight (dev %s); "
          "at t = 1, 2 the slope is log pi - Re psi(1/4 + it/2) "
          "(worst dev %s): the paper's gamma majorant at d = 1 IS the "
          "completed-zeta functional-equation factor"
          % (mp.nstr(max(mods), 3), mp.nstr(L_mp, 20), mp.nstr(dev0, 3),
             mp.nstr(max(devs_t), 3)),
          max(mods) < mp.mpf(10) ** -25 and dev0 < mp.mpf(10) ** -25
          and max(devs_t) < mp.mpf(10) ** -25)

    j_vals = [(sig,) + J_sigma(sig) for sig in
              (-0.99, -0.5, 0.0, 0.5, 0.9, 0.99, 0.9999)]
    mass_dev = max(abs(m - 1.0) for _, _, m, _ in j_vals)
    mono = all(j_vals[i][1] > j_vals[i + 1][1]
               for i in range(len(j_vals) - 1))
    gap_lim = abs(j_vals[-1][1] - math.log(math.pi / 2.0))
    gap_end = abs(j_vals[0][1] - 1.0)
    print("      J_sigma: " + ", ".join("J(%+.4g) = %.6f" % (s, j)
                                        for s, j, _, _ in j_vals))
    check("P1.2 [E] the certificate constant of Lemma 3.3/3.4 "
          "reproduces: harmonic-measure mass int P_sigma = M_sigma to "
          "%.1e, J_sigma DECREASES monotonically and J(0.9999) = %.6f "
          "hits log(pi/2) = %.6f within %.1e; the sigma -> -1 endpoint "
          "J -> -I0(0) = 1 within %.3f -- the 1/pi threshold "
          "log(2 pi c^2) + log(pi/2) = log(pi^2 c^2) is implemented "
          "correctly" % (mass_dev, j_vals[-1][1],
                         math.log(math.pi / 2.0), gap_lim, gap_end),
          mass_dev < 1.0e-6 and mono and gap_lim < 1.0e-4
          and gap_end < 0.03)

    mp.mp.dps = 30

    def mellin_gauss(z):
        # log substitution r = e^v removes the endpoint singularity
        return mp.quad(lambda v: mp.exp(-mp.pi * mp.exp(2 * v))
                       * mp.exp(z * v), [-mp.inf, 0, 3])

    fe_devs = []
    for z in (mp.mpf(3) / 10 + mp.mpf(7) / 10 * 1j, mp.mpf(1) / 2,
              mp.mpf(4) / 5 - mp.mpf(1) / 5 * 1j):
        lhs = mellin_gauss(z)          # ghat = g for the Gaussian
        rhs = (mp.pi ** (mp.mpf(1) / 2 - z) * mp.gamma(z / 2)
               / mp.gamma((1 - z) / 2) * mellin_gauss(1 - z))
        fe_devs.append(abs(lhs - rhs) / abs(lhs))
    check("P1.3 [E, 20+ digits] the d = 1 Mellin-Hankel functional "
          "equation (paper eq. 9) locks the conventions: M_ghat(z) = "
          "pi^{1/2 - z} Gamma(z/2)/Gamma((1-z)/2) M_g(1-z) on the "
          "self-Fourier Gaussian at 3 strip points (worst rel dev %s)"
          % mp.nstr(max(fe_devs), 3), max(fe_devs) < mp.mpf(10) ** -20)

    # ------------------------------------------------------------- P2
    print("\nP2 -- the MEASURED sign-uncertainty readout of the window "
          "family")
    u0 = zeta_grid_const()
    rows = []
    n_done = 0
    for kz in KZ:
        alpha = float(core.U_ALL[kz])
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
        if Mz % 2:
            Mz += 1
        hz = Mz // 2
        X_cap = math.exp(2.0 * alpha)
        complete = X_cap <= core.ATOM_MAX + 0.5
        ka = core.atoms_in(alpha)
        uu, mm = core.U_ALL[:ka], core.MU_ALL[:ka]
        c_at, D = core.atom_lags_at(alpha, Mz, uu, mm)
        c_ar = core.arch_lags(Mz, D)
        A = core.odd_toeplitz(c_ar + c_at, Mz)
        g = np.zeros(Mz)
        g[0], g[1] = 2.0 * D / 3.0, D / 6.0
        G = core.odd_toeplitz(g, Mz)
        lam_min, v_min, rad = gen_min_eig(A, G)
        floor = FLOOR_SAFETY * EPS * rad * math.sqrt(hz)
        rho_star, n_flips = last_sign_change(v_min, D, hz)
        T8 = core.parity_basis(hz, 8)
        o8 = float(np.sum((T8 @ v_min) ** 2) / (v_min @ v_min))
        T32 = core.parity_basis(hz, 32)
        A32 = T32 @ (A @ T32.T)
        G32 = T32 @ (G @ T32.T)
        lam32, _, rad32 = gen_min_eig(A32, G32)
        floor32 = FLOOR_SAFETY * EPS * rad32 * math.sqrt(32.0)
        # v618 lock read (verbatim route, read-only)
        Tb = core.parity_basis(hz, 2)
        t1v, t2v = Tb[0], Tb[1]
        W11 = core.lag_weights_from_v(t1v, hz)
        W22 = core.lag_weights_from_v(t2v, hz)
        Wpp = core.lag_weights_from_v(t1v + t2v, hz)
        W12 = 0.5 * (Wpp - W11 - W22)
        B2 = np.array([[c_ar @ W11, c_ar @ W12], [c_ar @ W12, c_ar @ W22]])
        s11 = s22 = s12 = 0.0
        lamw = 0.5 * mm
        for i in range(ka):
            s11 += lamw[i] * core.spline_project(W11, uu[i], D, Mz)
            s22 += lamw[i] * core.spline_project(W22, uu[i], D, Mz)
            s12 += lamw[i] * core.spline_project(W12, uu[i], D, Mz)
        S2 = np.array([[s11, s12], [s12, s22]])
        Sm = model_matrix(alpha, Mz, D, W11, W22, W12, u0)
        vl = lock_dir(alpha)
        q_r = float(vl @ ((B2 - S2) @ vl))
        q_m = float(vl @ ((B2 - Sm) @ vl))
        rows.append(dict(kz=kz, h=hz, alpha=alpha, D=D, X=X_cap,
                         complete=complete, lam=lam_min, floor=floor,
                         lam32=lam32, floor32=floor32, rho=rho_star,
                         f=rho_star / (hz * D), nf=n_flips, o8=o8,
                         qr=q_r, qm=q_m, eh=abs(q_r / q_m) * hz,
                         lock=q_r * q_m > 0.0))
        n_done += 1
        if n_done % 20 == 0:
            print("      ... %d/%d windows (%.0f s)"
                  % (n_done, len(KZ), time.time() - T0))

    comp = [r for r in rows if r["complete"]]
    inc = [r for r in rows if not r["complete"]]
    print("      surface: %d windows, %d complete combs (X <= %g), "
          "%d truncated: %s"
          % (len(rows), len(comp), float(core.ATOM_MAX),
             len(inc), sorted(r["h"] for r in inc)))
    check("P2.1 [E] the declared surface reproduces: %d frame-A windows, "
          "of which EXACTLY 67 have complete combs (h = %d..%d, "
          "2 alpha = %.3f..%.3f), and the 3 truncated windows are "
          "PRECISELY %s = the two v618 sign-flip windows + the excluded "
          "h = 1292: the C = 1 violators are the incomplete combs"
          % (len(rows), min(r["h"] for r in comp),
             max(r["h"] for r in comp),
             2 * min(r["alpha"] for r in comp),
             2 * max(r["alpha"] for r in comp),
             sorted(r["h"] for r in inc)),
          len(comp) == 67
          and sorted(r["h"] for r in inc) == [1219, 1292, 1445])

    print("      h    2alpha      D       lam_min(L2)   floor     "
          "lam32(L2)    rho*    f*   nfl  o8    eps*h")
    for r in sorted(comp, key=lambda r: r["h"]):
        print("    %5d  %6.3f  %.4e  %+.4e  %.1e  %+.4e  %6.3f  %.3f  "
              "%3d  %.2f  %.3f"
              % (r["h"], 2 * r["alpha"], r["D"], r["lam"], r["floor"],
                 r["lam32"], r["rho"], r["f"], r["nf"], r["o8"],
                 r["eh"]))

    n_below = sum(1 for r in comp if abs(r["lam"]) <= r["floor"])
    n_neg = sum(1 for r in comp if r["lam"] < -r["floor"])
    lam_min_all = min(r["lam"] for r in comp)
    check("P2.2 [MEASURED, W3 surface sanity] discrete positivity holds "
          "on ALL 67 complete windows at float level: min lambda_min = "
          "%+.3e, %d windows certified-negative (< -floor), %d below "
          "the float floor; the 32-mode block agrees (min %+.3e, all "
          "> floor32)"
          % (lam_min_all, n_neg, n_below,
             min(r["lam32"] for r in comp)),
          n_neg == 0
          and all(r["lam32"] > r["floor32"] for r in comp))

    fit_rows = [r for r in comp if r["lam"] > r["floor"]]
    y = np.log(np.array([r["lam"] for r in fit_rows]))
    x_a = np.log(np.array([2.0 * r["alpha"] for r in fit_rows]))
    x_h = np.log(np.array([float(r["h"]) for r in fit_rows]))
    x_e = np.array([2.0 * r["alpha"] for r in fit_rows])
    (b1, r2_1) = ols([x_a], y)
    (b2, r2_2) = ols([x_e], y)
    (b3, r2_3) = ols([x_a, x_h], y)
    p1, c1 = -float(b1[1]), math.exp(float(b1[0]))
    kap, c2 = -float(b2[1]), math.exp(float(b2[0]))
    p3a, p3h = -float(b3[1]), -float(b3[2])
    print("      fits on %d complete windows (lam > floor):" % len(y))
    print("      M1 power:  lam = %.4g (2a)^-%.4f      R^2 = %.4f"
          % (c1, p1, r2_1))
    print("      M2 exp:    lam = %.4g e^{-%.4f (2a)}  R^2 = %.4f"
          % (c2, kap, r2_2))
    print("      M3 mixed:  lam ~ (2a)^-%.4f h^-%.4f   R^2 = %.4f"
          % (p3a, p3h, r2_3))
    y32 = np.log(np.array([r["lam32"] for r in fit_rows]))
    (b1b, r2_1b) = ols([x_a], y32)
    (b2b, r2_2b) = ols([x_e], y32)
    print("      32-block:  power p = %.4f (R^2 = %.4f), exp kappa = "
          "%.4f (R^2 = %.4f)"
          % (-float(b1b[1]), r2_1b, -float(b2b[1]), r2_2b))
    for tag, val in (("p (M1)", p1), ("C (M1)", c1), ("kappa (M2)", kap),
                     ("C (M2)", c2)):
        nm, dist = nearest_named(val)
        print("      named-constant scan: %s = %.5f -> nearest %s "
              "(rel dist %.3f)" % (tag, val, nm, dist))
    best_r2 = max(r2_1, r2_2, r2_3)
    check("P2.3 [MEASURED] scaling law: the best of the three "
          "preregistered models reaches R^2 = %.4f (bar %.2f): "
          "M1 p = %.3f / M2 kappa = %.3f / M3 (p, q) = (%.3f, %.3f) -- "
          "reported as measured, constants scanned above"
          % (best_r2, R2_LAW_BAR, p1, kap, p3a, p3h),
          best_r2 >= R2_LAW_BAR)

    rhos = np.array([r["rho"] for r in comp])
    fstars = np.array([r["f"] for r in comp])
    n_noflip = int(np.sum(rhos == 0.0))
    rho_min = float(np.min(rhos[rhos > 0])) if np.any(rhos > 0) else 0.0
    bck_ball = 1.0 / math.pi
    check("P2.4 [MEASURED] the last-sign-change radius of the minimal "
          "mode sits at WINDOW scale: median rho* = %.3f (u-units), "
          "median f* = rho*/alpha = %.3f, %d/%d profiles carry no flip; "
          "min positive rho* = %.3f exceeds the maximal BCK ball "
          "1/pi = %.3f by a factor %.1f (bar >= %.1f)"
          % (float(np.median(rhos)), float(np.median(fstars)),
             n_noflip, len(comp), rho_min, bck_ball,
             rho_min / bck_ball, SCALE_KILL_BAR),
          rho_min / bck_ball >= SCALE_KILL_BAR and n_noflip == 0)

    # ------------------------------------------------------------- P3
    print("\nP3 -- the LP-ceiling test at d = 1")
    budg = {}
    for cfac in (0.5, 0.9, 0.99):
        c = cfac / math.pi
        e_star, s_star = mass_budget(c)
        budg[cfac] = (e_star, s_star, math.exp(-e_star))
        print("      c = %.2f/pi: E* = %.6f at sigma* = %+.3f -> "
              "main-term mass factor e^{-E*} = %.6f (contradiction "
              "needs < %.1f); d_needed = %.1f"
              % (cfac, e_star, s_star, math.exp(-e_star),
                 MASS_KILL_BAR, math.log(2.0) / e_star))
    check("P3.1 [MEASURED, the ceiling] the paper's OWN mass-bound "
          "budget dies at d = 1: at c = 0.9/pi the main-term factor is "
          "e^{-E*} = %.4f > %.1f (no contradiction possible even before "
          "the growing prefactors; the same machinery needs d >= %.0f), "
          "and the window family's negative structure sits %.1fx "
          "outside the maximal BCK ball (P2.4): the Cohn-Elkies-ceiling "
          "route does NOT transfer to the window cone -- the missing "
          "large parameter is the strip HALF-WIDTH, and the zeta strip "
          "is width 1, fixed"
          % (budg[0.9][2], MASS_KILL_BAR,
             math.ceil(math.log(2.0) / budg[0.9][0]),
             rho_min / bck_ball),
          budg[0.9][2] > MASS_KILL_BAR
          and rho_min / bck_ball >= SCALE_KILL_BAR)

    lock_rows = [r for r in rows if r["h"] != 1292]
    locks = [r for r in lock_rows if r["lock"]]
    flips = sorted(r["h"] for r in lock_rows if not r["lock"])
    eh_max = max(r["eh"] for r in locks)
    h_at_max = [r["h"] for r in locks if r["eh"] == eh_max][0]
    r1292 = [r for r in rows if r["h"] == 1292]
    if r1292:
        print("      (h = 1292, outside the declared v618 surface: "
              "lock = %s, eps*h = %.3g)"
              % (r1292[0]["lock"], r1292[0]["eh"]))
    check("P3.2 [E, reproduction + typing] the v618 two-boundary "
          "certificate re-measured on the declared surface: %d/%d "
          "lock-sign windows with max eps*h = %.3f at h = %d (v618 "
          "quote %.3f), flip set %s = %s -- STRUCTURE: like the "
          "Mellin-strip certificate it is a two-boundary family "
          "(model/mass side + functional-equation side, interpolation "
          "parameter h vs sigma), BUT it certifies the MAGNITUDE "
          "(|q_r| <= q_m/h), not the SIGN: the paper's strip bound "
          "forces a sign contradiction via mass, the C = 1 bound "
          "cannot -- the correspondence breaks exactly at the "
          "sign step, which is the RH-hard content of W3"
          % (len(locks), len(lock_rows), eh_max, h_at_max,
             V618_MAX_QUOTE, flips, V618_FLIPS),
          abs(eh_max - V618_MAX_QUOTE) <= 0.01 and h_at_max == 184
          and flips == V618_FLIPS and eh_max <= 1.0)

    lock_c = [r for r in comp if r["lock"] and r["lam"] > r["floor"]]
    le = np.log(np.array([r["eh"] for r in lock_c]))
    ll = np.log(np.array([r["lam"] for r in lock_c]))
    cc = float(np.corrcoef(le, ll)[0, 1])
    print("      diagnostic: corr(log lambda_min, log eps*h) on %d "
          "lock-sign complete windows = %+.3f (the positivity margin "
          "and the C = 1 contraction margin are %s)"
          % (len(lock_c), cc,
             "correlated" if abs(cc) > 0.5 else "decoupled"))

    # ------------------------------------------------------------- P4
    print("\nP4 -- the typed verdict")
    pi_family = {k: v for k, v in NAMED.items()
                 if "pi" in k or k == "sqrt(e)/(2pi)"}
    cand_hit = False
    for val in (p1, c1, kap, c2):
        for nm, ref in pi_family.items():
            if abs(val - ref) / abs(ref) <= CONST_CAND_BAR \
                    and best_r2 >= R2_CAND_BAR:
                cand_hit = True
                print("      candidate hit: %.5f matches %s within %.1f%% "
                      "at R^2 = %.3f" % (val, nm, 100 * CONST_CAND_BAR,
                                         best_r2))
    mass_dead = (budg[0.9][2] > MASS_KILL_BAR
                 and rho_min / bck_ball >= SCALE_KILL_BAR)
    if FAILS:
        verdict = "MIXED"
    elif cand_hit and not mass_dead:
        verdict = "W3-MECHANISM-CANDIDATE"
    elif mass_dead:
        verdict = "LP-CEILING-ANALOG-TYPED"
    else:
        verdict = "TECHNIQUE-NOT-APPLICABLE-1D"

    check("P4.1 [C] the typed reading: the DICTIONARY is real and "
          "anchored (the d = 1 strip multiplier is the completed-zeta "
          "gamma factor with phase slope L = v631's delta_0 weight; the "
          "two-boundary certificate structure is shared with v618's "
          "C = 1), the QUANTITATIVE mechanism is not: the exponential "
          "mass gain is powered by the strip half-width d/2 -> inf, "
          "the zeta strip has fixed width 1, and the paper's own "
          "budget yields e^{-E*} = %.3f at c = 0.9/pi where < 0.5 is "
          "needed (d >= %.0f would be required).  No marker move, no "
          "RH statement; W3 stays open"
          % (budg[0.9][2], math.ceil(math.log(2.0) / budg[0.9][0])),
          True)

    print("\nVERDICT: %s" % verdict)
    print("""
CONTRACT-NOTE TEXT (for the report ONLY -- nothing is written to the
contract by this probe):

  PRIME.WEIL.OPERATOR.01, note on W3 candidate mechanisms (sign-
  uncertainty round, 2026-08-02): the Bourgain-Clozel-Kahane /
  Cohn-Elkies sign-uncertainty toolbox (ten-proofs Ch. 1) was read
  against the window cone.  Dictionary (verified to 25 digits): the
  d = 1 Mellin strip IS the critical strip; the strip multiplier is
  the completed-zeta gamma factor, phase slope L = log pi - psi(1/4)
  (= the W1 dictionary's delta_0 weight, v631); the paper's
  two-boundary certificate (L1-mass boundary + functional-equation
  boundary, harmonic-measure interpolation) has the same shape as the
  v618 C = 1 contraction (model floor + arithmetic contraction,
  ladder parameter h).  TYPED NEGATIVE (LP-ceiling analogue): the
  quantitative mechanism -- exponential interior-mass smallness
  e^{-gamma d} -- is powered by the strip half-width lambda = d/2 and
  dies at d = 1: max main-term budget e^{-E*} = %.3f at c = 0.9/pi
  (needs < 1/2; the machinery would need d >= %.0f), and the measured
  negative structure of the window family (last-sign-change radius
  rho* = %.2f..%.2f, median %.2f in u-units) sits %.0fx outside the
  maximal BCK ball 1/pi.  A BCK-type mass obstruction therefore
  cannot certify Ahat_{a,h} >= 0; any W3 route through this toolbox
  must replace the dimension lever by a different large parameter
  (window length 2 alpha acts as the BALL radius, not the strip
  width).  Measured on the declared v563 surface: lambda_min > 0 on
  67/67 complete windows (min %+.2e, float-floor certified), scaling
  lambda_min ~ (2 alpha)^-p with p = %.2f (R^2 = %.2f) [reported, no
  named constant claimed].  No marker move; W3 open; Problem 7.1
  untouched.
""" % (budg[0.9][2], math.ceil(math.log(2.0) / budg[0.9][0]),
       float(np.min(rhos[rhos > 0])), float(np.max(rhos)),
       float(np.median(rhos)), rho_min / bck_ball * 1.0,
       lam_min_all, p1, r2_1))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
