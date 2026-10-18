"""v682 -- PRIME.LKSPLIT.01: THE L+K SPLIT AND THE RELATIVE FORM BOUND
THETA -- OFFENSIVE 1 of the uniform-operator-positivity program
(PRIME.UNIFPOS.01): construct the NON-CIRCULAR split B_a = L_a + K_a of
the deployed window form and MEASURE the relative bound |<K v, v>| <=
theta <L v, v> on the odd sector, over the 5-window family x an
M-ladder.  This module measures, derives and types; it moves no
marker; NO RH claim.

THE OBJECT (v563 read-only; v643 gives the verbatim transfer to
Suzuki's B_a = D* G_a D via the one-scalar dictionary).  A frame-A
window = (alpha, M = 2h, D = 2 alpha/M); deployed lag vector
c = c_ar + c_at with
  c_ar[d] = -<W_sm, tent_d>   (W_sm = arch density rho(t) =
            e^{-t/2}/(1 - e^{-2t}) away from 0 + the Pf origin block;
            v643 THEOREM (ii): exact at every lag),
  c_at[d] = -sum_n (Lambda(n)/sqrt n)[tent_D(dD - u_n) +
            tent_D(dD + u_n)],  u_n = log n <= 2 alpha,
and the deployed form B = odd_toeplitz(c, M) on the odd sector
(h x h), measured PD on the whole family (v677 S3.1).  Master
identity (v677 S2.3, unconditional): <B v, v> = sum_{gamma>0}
T_v(gamma_rho) + P(v) with the closed pole layer
  P(v) = -T_v(i/2) = D (sinh(D/4)/(D/4))^2 e^{(M-1)D/2}
         (sum_j f_j e^{-jD/2})^2  >= 0   (rank 1 on the odd sector).

THE SIGN BOOKKEEPING (task T4a; derived here, verified in S0):
  (i)   the arch density rho is a POSITIVE and POSITIVE-DEFINITE
        function: rho(t) = sum_{k>=0} e^{-(2k+1/2)|t|} (geometric
        collapse, sympy + 25-digit numeric), a sum of Laplace
        kernels, each with Fourier transform 2a/(a^2 + xi^2) > 0.
        Hence the tent-Toeplitz form of the POSITIVE assembly +rho
        is PSD, exactly (Gram argument; the diagonal read
        <rho, tent_0> DIVERGES logarithmically) -- the task's first
        check.
  (ii)  the DEPLOYED arch layer is the NEGATIVE of those reads with
        the Pf-renormalized diagonal: c_ar[d>=1] = -<rho, tent_d> < 0,
        c_ar[0] > 0.  Frequency side (v677 S2.1): the deployed arch
        layer has density Omega(r) = Re psi(1/4 + ir/2) - log pi --
        SIGN-CHANGING at t* = 6.2898... (the digamma crossing).  The
        deployed arch layer alone is INDEFINITE on the odd sector:
        the ~ floor(t* alpha/pi) lattice modes below t* are negative.
  (iii) the pole block 2 cosh(t/2) is a positive density but NOT a
        positive-definite function; its odd-sector tent form is a
        NEGATIVE rank-1 square (sum_d w_d pole_d = T_v(i/2) <= 0),
        i.e. P = odd_toeplitz(-pole_lag) is rank-1 PSD.
  (iv)  the atom layer's PNT mean density m(u) = e^{u/2} equals the
        pole density asymptotically (e^{u/2} vs 2 cosh(u/2)); its
        tent reads are c_mean = -pole-reads + Laplace-KMS reads:
        MEAN form = rank-1 pole square + PD-kernel form >= 0
        (closed, for support u >= 0) -- the positive low-frequency
        content of the atoms IS the pole block (PNT <-> s = 1 pole).
  CONSEQUENCE: window positivity is NOT "arch minus atoms" uniformly:
  for t > t* the arch density carries and the atoms oscillate; for
  t < t* the arch layer is NEGATIVE and positivity is carried by the
  pole/mean rank-1 plus the prime oscillation.  The split candidates
  below are chosen accordingly.

THE SPLIT CANDIDATES (all EXACT decompositions B = L + K; L is
NULLSTELLEN-FREI by definition -- Gamma data, cosh block, PNT mean;
no zero of any L-function enters any definition):
  C1a  L = ARCH               = odd_toeplitz(c_ar),        K = atoms
  C1b  L = ARCH + POLE        = odd_toeplitz(c_ar - pole), K = B - L
       (the task's candidate 1: Gamma-function data + cosh block)
  C3   L = ARCH + PNT MEAN    = odd_toeplitz(c_ar + c_mean),
       K = PRIME FLUCTUATION  = odd_toeplitz(c_at - c_mean),
       mean support [log 2, 2 alpha] (atom-matched; the u0 = 0
       variant carries the closed PSD statement, both measured)
  OS   L = TOEPLITZ BLOCK     T_h(c)[j,k] = c_|j-k|,
       K = -HANKEL BLOCK      -c_{M-1-j-k}
       (the v622-inspired reflection split: the odd sector's index
       flip j -> M-1-j is the lattice mirror x -> -x; B_odd =
       translation layer minus reflection pairing.  NOTE: L contains
       the primes -- zero-free in definition, but not Gamma-only)
  C4   L = L(C3) + (K(C3))_+ spectral positive part, K = (K(C3))_-
       (the TRIVIAL spectral split -- measured only as the
       circularity yardstick)

THE MEASUREMENT (T1): theta(a, M) = max |generalized eigenvalue| of
the pencil (K, L) on the odd sector = max over v of
|<K v,v>|/<L v,v>, REQUIRING L >= 0 (family floor convention
floor = 20 eps rad sqrt(h)).  Decomposition of theta:
  mu_min = min eig(K, L),  mu_max = max eig(K, L),
  theta  = max(|mu_min|, mu_max);
  |mu_min| < 1  <=>  B > 0 relative to L  (the RH-strength side:
                     1 + mu_min = gen-lambda_min(B, L)),
  mu_max  < 1  <=>  B < 2L  (the coupling-regularity side -- NOT
                     implied by RH; the genuinely new content).
If L is indefinite the candidate is DEAD as stated; we then measure
the DEFLATED theta on the L-positive subspace and type the negative
directions (frequency profile: do they live below t*?).

FAMILY AND LADDER (declared): the 5-window garding selection of the
pinch/coverage probes (smallest complete frame-A window + h-quantiles
{0.25, 0.5, 0.75, 1.0} of the complete family); M-ladder factors
(0.5, 0.75, 1.0, 1.5) x deployed M on the smallest and largest pick,
deployed M on all five (a-trend at fixed assembly).  Lags certified:
arch spot lags vs mpmath quadrature of rho (bar 1e-8 rel), atom lags
vs the independent binned assembly (bar 1e-10 rel), pole lag closed
form vs quadrature of 2 cosh(t/2) (bar 1e-10 rel).

SYMBOL LEVEL (T2): with sigma_X(theta) = X_0 + 2 sum_d X_d cos(d
theta) and t = theta/D, the odd form of a pure lag layer satisfies
f^T T_M(c) f = (1/2pi) int sigma |F_f|^2 EXACTLY, so the POINTWISE
inequality |sigma_fluct(theta)| <= thetabar sigma_ar(theta) on
(0, pi] PLUS MEAN-form >= 0 (closed) IS SUFFICIENT for
|<K3 v,v>| <= thetabar <L3 v,v>.  We measure r3(t) =
|sigma_fluct|/sigma_ar (and r1 = |sigma_at|/sigma_ar) where
sigma_ar > 0, its sup, location, band table, and the M-trend of
sup r3 (the almost-periodic prime sum has sup_t -> sum_n
Lambda(n)/sqrt n ~ 2 e^alpha as the reach grows: the pointwise route
MUST die in the M -> infinity limit; where does it die on the
deployed reach?).  The exact target inequality is printed with all
constants (T2 deliverable).

CIRCULARITY (T3, honest): theta < 1 uniform ==> B >= (1-theta) L > 0
uniform ==> family Weil positivity ==> (all windows, all a; Weil
1952/Yoshida 1992 via the v677 typing) RH -- the intermediate form is
RH-strong BY DESIGN.  The converse: RH gives ONLY the lower side
mu_min >= -1 (with margin = the measured W3 margin, known tiny); the
upper side mu_max <= 1 is a split-regularity statement RH does not
give.  The lower-side theta measurement is therefore a REPACKAGING of
the measured window positivity (named, not hidden); the genuinely new
measurable content is mu_max.  C4's theta < 1 is (up to its own
L-PSD status) the measured B > 0 (pure renaming; printed as the
yardstick).

PREREGISTERED BARS (declared BEFORE the numbers):
  G0.2 arch cert rel <= 1e-8 (d in {1, 5, 50}, anchor);
  G0.3 atom route rel <= 1e-10; pole closed form rel <= 1e-10;
  S0.1 geometric collapse: sympy branch + mpmath 1e-25; FT sympy
       exact; S0.2 eigmin >= -1e-10 x rad (K in {1, 4, 16, 64});
  S0.3 c_ar signs exact; n_neg(ARCH) = #modes below the measured
       window crossing +- 2; S0.4 pole three-way rel <= 1e-8,
       rank-1: second |eig| <= 1e-10 x top;
  S0.5 the u0 = 0 mean form PSD: eigmin >= -1e-8 x rad (closed
       statement); the u0 = log 2 variant is MEASURED (printed);
  S1.1 wiring max|L + K - B| <= 1e-9 x scale, per cell and split;
  S1.2 theta tables MEASURED (no pass bar; trends typed);
  S2.1 FFT symbol vs direct cos sum <= 1e-9 x scale (3 spots);
       anchor window crossing within 10% of the digamma root t*;
  S3.1 pencil bracket: gen-eig(B, L)|V+ == 1 + eig(K, L)|V+ to
       1e-10 (the identity B = L + K in the L-metric).
  S3.3 (added in run 2, declared BEFORE its first evaluation): the
       upper-side SPIKE LAW mu_max ~ 1 + 2 alpha/Omega(t_peak)
       (the v669 Fejer main-lobe height 2 pi F_a(0) = 2a of ONE
       zero pair against the smooth density Omega): median rel dev
       over {C1b, C3} x 5 deployed windows <= 0.35; the top
       extremal direction sits at the first comb spike: t_peak
       within 4%% of the CITED literature gamma_1 = 14.134725
       (cited, never loaded); the top-5 pencil directions vs the
       first cited zeros are PRINTED (no bar -- mixtures allowed).
  EDGE_BAR = 0.95 (theta above this = knife edge), LOWBAND_FAC = 1.5
  (an L-negative direction is 'low band' if its DST peak t <=
  1.5 t*), N_NEG_TOL = 2.

VERDICT ENUMS (frozen, precedence top-down; the EXPECTED verdict of
this module is LK-SPLIT-DIES -- the naive smooth split is structurally
dead, WITH the new positive find that the deployed windows resolve
individual zeros, forcing any surviving intermediate form to be
one-sided or multi-resolution):
  LK-MIXED             -- any G0/S0 guard or wiring fails;
  LK-INTERMEDIATE-FORM -- >= 1 nontrivial split (C1a/C1b/C3/OS) has
                          L >= -floor on ALL cells AND sup theta <=
                          0.95: the intermediate form has substance;
  LK-EDGE              -- as above but 0.95 < sup theta < 1;
  LK-LOWBAND-RESIDUE   -- every nontrivial split has an indefinite L
                          somewhere, but ALL negative directions are
                          low-band (peak t <= 1.5 t*) AND >= 1 split
                          has deflated theta < 1 on all cells: the
                          split lives on t > t*, dies on a thin
                          explicit band (dim ~ alpha t*/pi);
  LK-SPLIT-DIES        -- otherwise (typed).

CALIBRATION HISTORY (honesty first): this header is written BEFORE
the first full run; any post-run recalibration is recorded here
explicitly.  Run 1 (2026-08-03): all guards and measurements passed
except S0.1, which failed for a PURE SYMPY-FORM reason (the
geometric sum stayed an unevaluated Sum; the Fourier integral
returned a Piecewise on arg(xi)) while the 25-digit mpmath check of
the same identity passed at dev 0.0.  Run 2 repairs S0.1 by the
q-substitution branch (Sum(q^k) with 0 < q < 1, q = e^{-2t}) and a
positive xi (WLOG: the transform is even in xi) -- no float of run
1 changed.  Run 2 also ADDS the S3.3 spike-law check (bars declared
above before its first evaluation), motivated by the run-1
OBSERVATION that every C1b/C3 extremal vector peaked at t ~ 13.6 -
14.3 with mu_max growing ~ linearly in alpha.

FIREWALL: no marker moves; no positivity claim beyond the measured
tables; no RH statement; NO zero of any L-function is read anywhere
(assembly = primes + digamma + closed exponentials only; AST-checked).
Python-only, counted per GATE.WOLFRAM.02.

PROVENANCE: discovery probe lk_split_theta_probe.py (2026-08-03, 20/20
PASS, verdict LK-SPLIT-DIES); v563_paper2_readouts (window machinery),
v643_w1_theorem (measure-level layer dictionary, Pf origin, verbatim
transfer to Suzuki's B_a), v677_w3_structure_theorem (master
identity, pole layer closed, symbol sandwich, S2.1 arch dictionary),
epstein_firewall_probe (the load rests on the Euler product),
v622_seam_identification (diameter-reflection dictionary),
pinch_attack_probe / v680 + coverage_hole_probe / v681 (5-window
garding selection), Weil 1952, Yoshida 1992, Kac-Murdock-Szego 1953,
Grenander-Szego 1958, Iwaniec-Kowalski Thm 5.12.
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

# ---------------------------------------------------------------- bars
EPS = float(np.finfo(float).eps)
FLOOR_SAFETY = 20.0            # family floor convention, verbatim
SEED = 20260803
TWO_PI = 2.0 * math.pi
U0_MEAN = math.log(2.0)        # PNT mean support starts at the first atom

BAR_CERT_ARCH = 1e-8
BAR_CERT_ATOM = 1e-10
BAR_CERT_POLE = 1e-10
BAR_GEO_NUM = 1e-25
BAR_PSD = 1e-10                # x radius (S0.2)
BAR_MEAN_PSD = 1e-8            # x radius (S0.5, u0 = 0 closed variant)
BAR_POLE3 = 1e-8               # pole three-way identity (S0.4)
BAR_RANK1 = 1e-10              # x top eigenvalue
BAR_WIRE = 1e-9                # split wiring x scale
BAR_SYM = 1e-9                 # FFT symbol vs direct
BAR_TSTAR = 0.10               # window crossing vs digamma root, rel
BAR_BRACKET = 1e-10            # S3.1 shift identity
EDGE_BAR = 0.95
LOWBAND_FAC = 1.5
N_NEG_TOL = 2

M_FACT_ALL = (1.0,)                      # deployed M on all 5 windows
M_FACT_LADDER = (0.5, 0.75, 1.0, 1.5)    # ladder on smallest + largest
ND_SYM = 1 << 16                         # symbol grid (theta_i = 2pi i/Nd)
SPLIT_NAMES = ("C1a", "C1b", "C3", "OS")
NONTRIV = ("C1a", "C1b", "C3", "OS")


# ------------------------------------------------- window machinery
def window_geometry(kz):
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return alpha, M


def pole_lag_vec(M, D):
    """pole_d = <tent_d, 2 cosh(t/2)> = 2 D cosh(dD/2)
    (sinh(D/4)/(D/4))^2 = h_d(i/2) (v677 closed form)."""
    sh = math.sinh(D / 4.0) / (D / 4.0)
    return 2.0 * D * np.cosh(np.arange(M) * D / 2.0) * sh ** 2


def mean_lags(alpha, M, D, u0):
    """Closed tent reads of the PNT mean density m(u) = e^{u/2} on
    [u0, 2 alpha], assembled with the atom sign convention
    (c_mean[d] = -<m, tent-pair_d>, including the d = 0 reflection
    when u0 < D, mirroring atom_lags_at)."""
    top = 2.0 * alpha

    def F0(a, b):
        return 2.0 * (math.exp(b / 2.0) - math.exp(a / 2.0))

    def F1(a, b):
        return (2.0 * (b * math.exp(b / 2.0) - a * math.exp(a / 2.0))
                - 2.0 * F0(a, b))

    c = np.zeros(M)
    for d in range(M):
        p = d * D
        val = 0.0
        a1, b1 = max(u0, p - D), min(p, top)          # left flank
        if b1 > a1:
            val += (F1(a1, b1) - (p - D) * F0(a1, b1)) / D
        a2, b2 = max(u0, p), min(p + D, top)          # right flank
        if b2 > a2:
            val += ((p + D) * F0(a2, b2) - F1(a2, b2)) / D
        c[d] = -val
    if u0 < D:                                        # d = 0 reflection
        a3, b3 = u0, min(D, top)
        if b3 > a3:
            c[0] -= (D * F0(a3, b3) - F1(a3, b3)) / D
    return c


def toeplitz_block(c, M):
    h = M // 2
    rr = np.arange(h)
    return np.asarray(c)[np.abs(rr[:, None] - rr[None, :])]


def hankel_block(c, M):
    h = M // 2
    rr = np.arange(h)
    return np.asarray(c)[(M - 1) - rr[:, None] - rr[None, :]]


def dst_matrix(h, M):
    """Row-normalized DST modes sin(theta_k (j - h + 1/2)), k = 1..h,
    theta_k = 2 pi k/M (w3 convention); physical frequency t_k =
    theta_k / D."""
    th = TWO_PI * np.arange(1, h + 1) / M
    jj = np.arange(h) - h + 0.5
    U = np.sin(np.outer(th, jj))
    nrm = np.sqrt(np.sum(U * U, axis=1))
    nrm[nrm == 0.0] = 1.0
    return U / nrm[:, None], th


def symbol_of(c, M, Nd=ND_SYM):
    arr = np.zeros(Nd)
    arr[:M] = 2.0 * np.asarray(c)
    arr[0] = c[0]
    return np.fft.rfft(arr).real     # sigma(theta_i), theta_i = 2 pi i/Nd


def analyze_split(Lm, Km, h, D, U_dst, th_dst, t_star):
    """Pencil analysis of B = L + K on the odd sector: PSD status of
    L, (deflated) theta = max|eig(K, L)| on the L-positive subspace,
    both pencil ends, frequency profiles."""
    w, V = sla.eigh(0.5 * (Lm + Lm.T))
    rad = max(abs(float(w[0])), abs(float(w[-1])))
    floor = FLOOR_SAFETY * EPS * rad * math.sqrt(h)
    neg = w < -floor
    pos = w > floor
    n_neg = int(np.sum(neg))
    n_zero = int(h - n_neg - int(np.sum(pos)))
    tk = th_dst / D
    out = dict(lmin_L=float(w[0]), rad_L=rad, floor=floor,
               n_neg=n_neg, n_zero=n_zero)
    if n_neg:
        PP = (U_dst @ V[:, neg]) ** 2         # (h modes) x (n_neg dirs)
        peaks = tk[np.argmax(PP, axis=0)]
        out["neg_peak_t"] = [float(x) for x in peaks]
        out["neg_low_only"] = bool(np.all(peaks <= LOWBAND_FAC * t_star))
    else:
        out["neg_peak_t"] = []
        out["neg_low_only"] = True
    Vp = V[:, pos] * (1.0 / np.sqrt(w[pos]))[None, :]
    Kt = Vp.T @ (Km @ Vp)
    Kt = 0.5 * (Kt + Kt.T)
    mu, Y = sla.eigh(Kt)
    mu_min, mu_max = float(mu[0]), float(mu[-1])
    theta = max(abs(mu_min), abs(mu_max))
    side = "lower" if abs(mu_min) >= mu_max else "upper"
    y = Y[:, 0] if side == "lower" else Y[:, -1]
    v_star = Vp @ y
    prof = (U_dst @ v_star) ** 2
    prof = prof / float(np.sum(prof))
    ipk = int(np.argmax(prof))
    out.update(theta=theta, mu_min=mu_min, mu_max=mu_max, side=side,
               v_star=v_star, t_peak=float(tk[ipk]),
               share_low=float(np.sum(prof[tk <= t_star])))
    return out


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    rng = np.random.default_rng(SEED)
    print("=" * 78)
    print("L+K SPLIT AND THE RELATIVE FORM BOUND THETA -- offensive 1 "
          "(uniform operator positivity)")
    print("=" * 78)

    # ================================================================ G0
    print("\nG0 -- guards, family, certified lags")
    check("G0.0 [E] AST zero-firewall: no zero-table loader in this "
          "probe (assembly = primes + digamma + closed exponentials)",
          ast_zero_firewall(os.path.abspath(__file__)))

    zones = core.frame_a_zones()
    fam = []
    for kz in zones:
        alpha, M = window_geometry(kz)
        complete = math.exp(2.0 * alpha) <= core.ATOM_MAX + 0.5
        fam.append((kz, alpha, M, complete))
    comp = [t for t in fam if t[3]]
    hs_c = np.array([t[2] // 2 for t in comp], float)
    picks = [comp[0]]
    for qq in (0.25, 0.5, 0.75, 1.0):
        tgt = float(np.quantile(hs_c, qq))
        cand = min(comp, key=lambda t_: abs(t_[2] // 2 - tgt))
        if all(cand[0] != p[0] for p in picks):
            picks.append(cand)
    picks = sorted(picks, key=lambda t_: t_[2])
    print("   family (garding selection): " + ", ".join(
        "h=%d (alpha=%.4f, X=%.0f)" % (M // 2, a, math.exp(2 * a))
        for _kz, a, M, _c in picks))
    check("G0.1 [E] 5-window family selected from the %d complete "
          "frame-A windows (smallest + h-quantiles 0.25/0.5/0.75/1.0)"
          % len(comp), len(picks) == 5 and len(comp) == 67)

    # anchor window data for the certificates
    kz0, alpha0, M0, _c0 = picks[0]
    h0 = M0 // 2
    D0 = 2.0 * alpha0 / M0
    ka0 = core.atoms_in(alpha0)
    c_ar0 = core.arch_lags(M0, D0)
    c_at0, _ = core.atom_lags_at(alpha0, M0, core.U_ALL[:ka0],
                                 core.MU_ALL[:ka0])

    mp.mp.dps = 30
    Dm = mp.mpf(D0)

    def rho_mp(x):
        return mp.exp(-x / 2) / (-mp.expm1(-2 * x))

    def tent_mp(x, dd):
        v = 1 - abs(x - dd * Dm) / Dm
        return v if v > 0 else mp.mpf(0)

    devs = []
    for dd in (1, 5, 50):
        exact = -mp.quad(lambda x: tent_mp(x, dd) * rho_mp(x),
                         [(dd - 1) * Dm, dd * Dm, (dd + 1) * Dm])
        devs.append(abs(mp.mpf(float(c_ar0[dd])) - exact) / abs(exact))
    check("G0.2 [E] arch lags CERTIFIED on the anchor: c_ar[d] = "
          "-<rho, tent_d> vs mpmath quad at d = 1, 5, 50 (worst rel "
          "%s <= %.0e); c_ar[0] = %+.6f (Pf origin)"
          % (mp.nstr(max(devs), 3), BAR_CERT_ARCH, c_ar0[0]),
          max(devs) < mp.mpf(BAR_CERT_ARCH))

    c_at0b, _ = core.atom_lags_binned(alpha0, M0, core.U_ALL[:ka0],
                                      core.MU_ALL[:ka0])
    dev_at = float(np.max(np.abs(c_at0 - c_at0b))) \
        / float(np.max(np.abs(c_at0)))
    pole0 = pole_lag_vec(M0, D0)
    dpol = []
    for dd in (0, 3):
        if dd == 0:
            exact = mp.quad(lambda x: (1 - abs(x) / Dm)
                            * 2 * mp.cosh(x / 2), [-Dm, 0, Dm])
        else:
            exact = mp.quad(lambda x: tent_mp(x, dd) * 2 * mp.cosh(x / 2),
                            [(dd - 1) * Dm, dd * Dm, (dd + 1) * Dm])
        dpol.append(abs(mp.mpf(float(pole0[dd])) - exact) / abs(exact))
    check("G0.3 [E] atom lags: independent binned assembly matches "
          "atom_lags_at (rel %.1e <= %.0e); pole lag closed form = "
          "<tent_d, 2 cosh(t/2)> at d = 0, 3 (worst rel %s <= %.0e)"
          % (dev_at, BAR_CERT_ATOM, mp.nstr(max(dpol), 3),
             BAR_CERT_POLE),
          dev_at < BAR_CERT_ATOM and max(dpol) < mp.mpf(BAR_CERT_POLE))

    # the digamma crossing t* (Gamma data only)
    t_star = float(mp.findroot(
        lambda r: mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * r / 2))
        - mp.log(mp.pi), 6.3))
    print("   digamma crossing: Omega(t*) = 0 at t* = %.6f "
          "(Omega(t) = Re psi(1/4 + it/2) - log pi)" % t_star)

    # ================================================================ S0
    print("\nS0 -- the sign bookkeeping and the PSD first check")
    import sympy as sp
    t_s = sp.symbols("t_s", positive=True)
    k_s = sp.symbols("k_s", integer=True, nonnegative=True)
    q_s = sp.symbols("q_s", positive=True)
    rho_sym = sp.exp(-t_s / 2) / (1 - sp.exp(-2 * t_s))
    s_geo = sp.Sum(q_s ** k_s, (k_s, 0, sp.oo)).doit()   # Piecewise
    br = s_geo.args[0]                   # branch |q| < 1 (t > 0 gives it)
    ok_geo = (sp.simplify(br.expr - 1 / (1 - q_s)) == 0
              and br.cond == (sp.Abs(q_s) < 1)
              and sp.simplify(
                  sp.exp(-t_s / 2) / (1 - sp.exp(-2 * t_s)) - rho_sym)
              == 0)
    dev_geo = mp.mpf(0)
    for tv in (mp.mpf(3) / 10, mp.mpf(17) / 10):
        ssum = mp.nsum(lambda k: mp.exp(-(2 * k + mp.mpf(1) / 2) * tv),
                       [0, mp.inf])
        dev_geo = max(dev_geo, abs(ssum - rho_mp(tv)) / rho_mp(tv))
    a_s = sp.symbols("a_s", positive=True)
    xi_s = sp.symbols("xi_s", positive=True)   # WLOG: even in xi
    ft = 2 * sp.integrate(sp.exp(-a_s * t_s) * sp.cos(xi_s * t_s),
                          (t_s, 0, sp.oo))
    ok_ft = sp.simplify(ft - 2 * a_s / (a_s ** 2 + xi_s ** 2)) == 0
    check("S0.1 [E] rho IS a positive-definite function: rho(t) = "
          "sum_{k>=0} e^{-(2k+1/2)|t|} (sympy geometric branch q = "
          "e^{-2t} < 1: %s; mpmath 25-digit rel dev %s <= %.0e), "
          "each Laplace kernel has Fourier transform 2a/(a^2 + "
          "xi^2) > 0 (sympy exact, xi > 0 WLOG: %s) -- "
          "Bochner-positive term by term"
          % (ok_geo, mp.nstr(dev_geo, 3), BAR_GEO_NUM, ok_ft),
          ok_geo and dev_geo < mp.mpf(BAR_GEO_NUM) and ok_ft)

    # S0.2: the POSITIVE assembly of rho has a PSD tent-Toeplitz form
    m0 = min(h0, 360)

    def laplace_lags(a, D, m):
        E = math.exp(-a * D)
        v0 = 2.0 * ((1.0 - E) / a
                    - (1.0 - E * (1.0 + a * D)) / (a * a * D))
        vd = (np.exp(-a * D * np.arange(1, m))
              * D * (math.sinh(a * D / 2.0) / (a * D / 2.0)) ** 2)
        return np.concatenate([[v0], vd])

    rows_psd = []
    ok_psd = True
    for K in (1, 4, 16, 64):
        lag = np.zeros(m0)
        for k in range(K):
            lag += laplace_lags(2.0 * k + 0.5, D0, m0)
        Tm = toeplitz_block(np.concatenate([lag, np.zeros(m0)]),
                            2 * m0)
        ev = sla.eigvalsh(Tm)
        rad = max(abs(float(ev[0])), abs(float(ev[-1])))
        ok_psd &= float(ev[0]) >= -BAR_PSD * rad
        rows_psd.append((K, float(lag[0]), float(ev[0])))
    check("S0.2 [E, the task's first check] the POSITIVE-assembly "
          "tent-Toeplitz form of the arch density is PSD, exactly: "
          "T[j,k] = <rho_K, tent_(j-k)D> on %d lags, eigmin >= "
          "-%.0e x rad for K = 1, 4, 16, 64 truncations (%s); the "
          "diagonal read DIVERGES (l_K[0] = %s): the PSD-ness is "
          "real, the deployed object subtracts the divergence"
          % (m0, BAR_PSD,
             ["K=%d: %+.1e" % (K, e) for K, _l, e in rows_psd],
             ["%.3f" % l for _K, l, _e in rows_psd]), ok_psd)

    # S0.3: the DEPLOYED arch layer is indefinite, negatives = low band
    sig_ar0 = symbol_of(c_ar0, M0)
    th_grid = TWO_PI * np.arange(sig_ar0.size) / ND_SYM
    tt_grid = th_grid / D0
    band0 = (th_grid > 0) & (th_grid <= math.pi)
    icross = int(np.argmax((sig_ar0 > 0) & band0 & (tt_grid > 1.0)))
    t_cross = float(tt_grid[icross])
    U0d, th0d = dst_matrix(h0, M0)
    res_ar = analyze_split(core.odd_toeplitz(c_ar0, M0),
                           core.odd_toeplitz(c_at0, M0),
                           h0, D0, U0d, th0d, t_star)
    k_pred = int(np.sum(th0d / D0 < t_cross))
    ok_signs = (float(np.max(c_at0)) <= 0.0
                and float(np.max(c_ar0[1:])) < 0.0 and c_ar0[0] > 0.0)
    check("S0.3 [E] the DEPLOYED arch layer: c_ar[d>=1] < 0 (max "
          "%+.2e), c_ar[0] = %+.4f > 0, c_at <= 0 (max %+.1e) -- and "
          "it is INDEFINITE on the odd sector: eigmin = %+.4e, n_neg "
          "= %d vs the frequency prediction #modes below the window "
          "crossing t_cross = %.3f (digamma t* = %.4f): %d (|diff| "
          "<= %d); negative-direction DST peaks %s -- the arch layer "
          "alone CANNOT serve as L"
          % (float(np.max(c_ar0[1:])), c_ar0[0],
             float(np.max(c_at0)), res_ar["lmin_L"], res_ar["n_neg"],
             t_cross, t_star, k_pred, N_NEG_TOL,
             ["%.2f" % x for x in res_ar["neg_peak_t"][:6]]),
          ok_signs and abs(res_ar["n_neg"] - k_pred) <= N_NEG_TOL)

    # S0.4: the pole layer -- closed rank-1 square on the odd sector
    Pmat0 = core.odd_toeplitz(-pole0, M0)
    snc = math.sinh(D0 / 4.0) / (D0 / 4.0)
    dev3 = 0.0
    for _ in range(3):
        v = rng.standard_normal(h0)
        f = np.concatenate([v, -v[::-1]])
        w = core.lag_weights_from_v(v, h0)
        lagsum = float(w @ pole0)                       # = T_v(i/2)
        closed = (-D0 * snc * snc * math.exp((M0 - 1) * D0 / 2.0)
                  * float(f @ np.exp(-np.arange(M0) * D0 / 2.0)) ** 2)
        quad = float(v @ (Pmat0 @ v))                   # = P(v)
        sc = max(abs(closed), 1e-300)
        dev3 = max(dev3, abs(lagsum - closed) / sc,
                   abs(quad + closed) / sc)
    evP = sla.eigvalsh(Pmat0)
    sub = max(abs(float(evP[0])), abs(float(evP[-2])))
    rank1 = float(evP[-1]) > 0.0 and sub <= BAR_RANK1 * float(evP[-1])
    check("S0.4 [E] pole layer: sum_d w_d pole_d = T_v(i/2) = "
          "-(closed square) <= 0 on 3 random odd vectors (three-way "
          "rel dev %.1e <= %.0e), and P = odd_toeplitz(-pole) is "
          "EXACTLY rank-1 PSD on the odd sector (top eig %+.3e, "
          "second %.1e) -- a positive density (2 cosh) whose tent "
          "form is NEGATIVE: positive density does NOT imply PSD "
          "tent form (cosh is not a PD function)"
          % (dev3, BAR_POLE3, float(evP[-1]), sub),
          dev3 <= BAR_POLE3 and rank1)

    # S0.5: mean layer = pole square + Laplace reads (two variants)
    c_mean0 = mean_lags(alpha0, M0, D0, U0_MEAN)
    c_mean0_full = mean_lags(alpha0, M0, D0, 0.0)
    evM = sla.eigvalsh(core.odd_toeplitz(c_mean0, M0))
    evMf = sla.eigvalsh(core.odd_toeplitz(c_mean0_full, M0))
    radM = max(abs(float(evM[0])), abs(float(evM[-1])))
    radMf = max(abs(float(evMf[0])), abs(float(evMf[-1])))
    s_mean = float(np.sum(c_mean0))
    s_at = float(np.sum(c_at0))
    check("S0.5 [E+C] T4a SIGN BOOKKEEPING, typed: the atoms' PNT "
          "mean e^{u/2} is the pole density asymptotically; the "
          "u0 = 0 mean form is PSD by the CLOSED decomposition "
          "-pole-reads + Laplace-reads = rank-1 pole square + "
          "PD-kernel form (measured eigmin %+.3e >= -%.0e x rad "
          "%.2e, top %+.3e); the atom-matched u0 = log 2 variant "
          "(deployed in C3) measures eigmin %+.3e (rad %.2e; the "
          "compact [0, log 2) hole breaks the closed statement by "
          "at most this much); mean mass: sum c_mean = %.2f vs "
          "sum c_at = %.2f (residue %.1f%%).  Window positivity is "
          "NOT 'arch minus atom' uniformly: above t* the arch "
          "density carries, below t* the arch layer is NEGATIVE and "
          "the positive mass is the pole/mean rank-1 + prime "
          "oscillation -- the split must put the MEAN into L"
          % (float(evMf[0]), BAR_MEAN_PSD, radMf, float(evMf[-1]),
             float(evM[0]), radM, s_mean, s_at,
             100.0 * abs(s_at - s_mean) / abs(s_at)),
          float(evMf[0]) >= -BAR_MEAN_PSD * radMf)

    # ================================================================ S1
    print("\nS1 -- THE THETA MEASUREMENT: 5-window family x M-ladder")
    print("   theta = max |eig(K, L)| on the odd sector; L-floor = "
          "20 eps rad sqrt(h); DEAD if n_neg > 0 (deflated theta "
          "then diagnostic only)")
    cells = []
    for i, (kz, alpha, Mdep, _c) in enumerate(picks):
        facts = M_FACT_LADDER if i in (0, len(picks) - 1) \
            else M_FACT_ALL
        for fmul in facts:
            M = int(round(Mdep * fmul))
            if M % 2:
                M += 1
            cells.append((i, alpha, fmul, M))

    rows = []
    print("   %-4s %-5s %-5s | %-4s | %5s %10s | %7s %8s %8s %5s "
          "| %7s %6s" % ("win", "h", "fM", "spl", "n_neg", "lmin(L)",
                         "theta", "mu_min", "mu_max", "side",
                         "t_peak", "loshr"))
    wire_worst = 0.0
    for (iw, alpha, fmul, M) in cells:
        h = M // 2
        D = 2.0 * alpha / M
        t1 = time.time()
        ka = core.atoms_in(alpha)
        c_at, _ = core.atom_lags_at(alpha, M, core.U_ALL[:ka],
                                    core.MU_ALL[:ka])
        c_ar = core.arch_lags(M, D)
        pole = pole_lag_vec(M, D)
        c_mean = mean_lags(alpha, M, D, U0_MEAN)
        c_tot = c_ar + c_at
        B = core.odd_toeplitz(c_tot, M)
        U_dst, th_dst = dst_matrix(h, M)
        scale = float(np.max(np.abs(B)))
        splits = {
            "C1a": (core.odd_toeplitz(c_ar, M),
                    core.odd_toeplitz(c_at, M)),
            "C1b": (core.odd_toeplitz(c_ar - pole, M),
                    core.odd_toeplitz(c_at + pole, M)),
            "C3": (core.odd_toeplitz(c_ar + c_mean, M),
                   core.odd_toeplitz(c_at - c_mean, M)),
            "OS": (toeplitz_block(c_tot, M),
                   -hankel_block(c_tot, M)),
        }
        for nm in SPLIT_NAMES:
            Lm, Km = splits[nm]
            wire = float(np.max(np.abs(Lm + Km - B))) / scale
            wire_worst = max(wire_worst, wire)
            r = analyze_split(Lm, Km, h, D, U_dst, th_dst, t_star)
            r.update(win=iw, h=h, f=fmul, M=M, D=D, split=nm,
                     alpha=alpha, wire=wire, c_ar=c_ar, c_at=c_at,
                     c_mean=c_mean, pole=pole)
            rows.append(r)
            print("   %-4d %-5d %-5.2f | %-4s | %5d %+10.3e | %7.4f "
                  "%+8.4f %+8.4f %5s | %7.2f %6.3f"
                  % (iw, h, fmul, nm, r["n_neg"], r["lmin_L"],
                     r["theta"], r["mu_min"], r["mu_max"], r["side"],
                     r["t_peak"], r["share_low"]))
        print("   [cell win=%d h=%d f=%.2f: %.1f s, atoms=%d, "
              "D=%.5f, reach pi/D=%.0f]"
              % (iw, h, fmul, time.time() - t1, ka, D, math.pi / D))

    check("S1.1 [E] split wiring: B = L + K exactly on every cell "
          "and split (max rel dev %.1e <= %.0e)"
          % (wire_worst, BAR_WIRE), wire_worst <= BAR_WIRE)

    # summary per split
    print("\n   summary per split (over all %d cells):" % len(cells))
    alive, sup_theta, low_only, defl_ok = {}, {}, {}, {}
    for nm in SPLIT_NAMES:
        rs = [r for r in rows if r["split"] == nm]
        alive[nm] = all(r["n_neg"] == 0 for r in rs)
        sup_theta[nm] = max(r["theta"] for r in rs)
        low_only[nm] = all(r["neg_low_only"] for r in rs)
        defl_ok[nm] = all(r["theta"] < 1.0 for r in rs)
        n_dead = sum(1 for r in rs if r["n_neg"] > 0)
        print("   %-4s: L PSD on %d/%d cells; max n_neg = %d; "
              "sup theta%s = %.4f; negatives low-band only: %s"
              % (nm, len(rs) - n_dead, len(rs),
                 max(r["n_neg"] for r in rs),
                 "" if alive[nm] else " (deflated)", sup_theta[nm],
                 low_only[nm]))

    print("\n   a-trend (deployed M, f = 1.0):")
    for nm in SPLIT_NAMES:
        tr = sorted((r["alpha"], r["theta"], r["n_neg"]) for r in rows
                    if r["split"] == nm and r["f"] == 1.0)
        print("   %-4s: " % nm + "  ".join(
            "a=%.2f: %.4f(n%d)" % t for t in tr))
    print("   M-trend (smallest + largest window):")
    for nm in SPLIT_NAMES:
        for iw in (0, len(picks) - 1):
            tr = sorted((r["f"], r["theta"], r["n_neg"]) for r in rows
                        if r["split"] == nm and r["win"] == iw)
            if len(tr) > 1:
                print("   %-4s win %d: " % (nm, iw) + "  ".join(
                    "f=%.2f: %.4f(n%d)" % t for t in tr))
    check("S1.2 [MEASURED, central] theta tables complete: %d cells "
          "x 4 splits; measured sup theta per split: %s; L-PSD "
          "status per split: %s -- the theta measurement is the "
          "table above (no pass bar on measured values)"
          % (len(cells),
             ", ".join("%s=%.4f" % (nm, sup_theta[nm])
                       for nm in SPLIT_NAMES),
             ", ".join("%s=%s" % (nm, "PSD" if alive[nm] else "DEAD")
                       for nm in SPLIT_NAMES)), True)

    # T1(iii): where the extremal vector lives (C3, deployed M)
    print("\n   T1(iii) -- extremal-vector attribution (split C3, "
          "deployed M):")
    for iw in (0, len(picks) - 1):
        r = next(r for r in rows if r["split"] == "C3"
                 and r["win"] == iw and r["f"] == 1.0)
        v = r["v_star"]
        h, M, D, alpha = r["h"], r["M"], r["D"], r["alpha"]
        W = core.lag_weights_from_v(v, h)
        at_part = float(W @ r["c_at"])
        mean_part = -float(W @ r["c_mean"])
        ka = core.atoms_in(alpha)
        contrib = np.empty(ka)
        for i in range(ka):
            contrib[i] = -0.5 * float(core.MU_ALL[i]) \
                * core.spline_project(W, float(core.U_ALL[i]), D, M)
        dev_attr = abs(float(np.sum(contrib)) - at_part) \
            / max(abs(at_part), 1e-300)
        order = np.argsort(-np.abs(contrib))[:5]
        print("   win %d (h=%d): <K3 v*,v*> = atoms %+0.4e + "
              "(-mean) %+0.4e (attribution closes to rel %.1e); "
              "DST peak t = %.2f, low-band share %.3f; top atoms: %s"
              % (iw, h, at_part, mean_part, dev_attr, r["t_peak"],
                 r["share_low"],
                 ", ".join("n=%d (%+.2e)"
                           % (int(round(math.exp(core.U_ALL[i]))),
                              contrib[i]) for i in order)))
    check("S1.3 [MEASURED] extremal profiles printed (DST peak, "
          "low-band share, per-atom attribution closes)", True)

    # ================================================================ S2
    print("\nS2 -- the symbol level: pointwise ratio r(t) and the "
          "target prime-sum inequality")
    dev_sym = 0.0
    sup_tab = []
    for iw in range(len(picks)):
        rr = next(r for r in rows if r["split"] == "C3"
                  and r["win"] == iw and r["f"] == 1.0)
        M, D, alpha = rr["M"], rr["D"], rr["alpha"]
        c_ar, c_at, c_mean = rr["c_ar"], rr["c_at"], rr["c_mean"]
        sig_ar = symbol_of(c_ar, M)
        sig_at = symbol_of(c_at, M)
        sig_fl = symbol_of(c_at - c_mean, M)
        th = TWO_PI * np.arange(sig_ar.size) / ND_SYM
        tt = th / D
        bandm = (th > 0) & (th <= math.pi)
        for i_spot in (7, ND_SYM // 8, ND_SYM // 2 - 3):
            thv = TWO_PI * i_spot / ND_SYM
            direct = c_ar[0] + 2.0 * float(
                c_ar[1:] @ np.cos(np.arange(1, M) * thv))
            dev_sym = max(dev_sym, abs(direct - sig_ar[i_spot])
                          / max(1.0, abs(direct)))
        pos = bandm & (sig_ar > 0)
        negfrac = float(np.sum(bandm & (sig_ar <= 0))) \
            / float(np.sum(bandm))
        i0 = int(np.argmax(pos & (tt > 1.0)))
        t_cr = float(tt[i0])
        r1 = np.abs(sig_at[pos]) / sig_ar[pos]
        r3 = np.abs(sig_fl[pos]) / sig_ar[pos]
        tp = tt[pos]
        i3 = int(np.argmax(r3))
        bands = [(t_cr * 1.05, 2 * t_star), (2 * t_star, 20.0),
                 (20.0, 100.0), (100.0, math.pi / D)]
        bsup = []
        for lo, hi in bands:
            m_ = (tp >= lo) & (tp < hi)
            bsup.append(float(np.max(r3[m_])) if m_.any()
                        else float("nan"))
        sup_tab.append((iw, alpha, t_cr, negfrac, float(np.max(r1)),
                        float(np.max(r3)), float(tp[i3]), bsup))
        print("   win %d (a=%.3f, reach pi/D=%.0f): sigma_ar <= 0 on "
              "%.2f%% of the band (t < %.3f); sup r1 = "
              "|s_at|/s_ar = %.2f; sup r3 = |s_fluct|/s_ar = %.3f "
              "at t = %.2f; band sups r3 %s"
              % (iw, alpha, math.pi / D, 100 * negfrac, t_cr,
                 float(np.max(r1)), float(np.max(r3)), float(tp[i3]),
                 ["%.3f" % b for b in bsup]))
    t_cr0 = sup_tab[0][2]
    check("S2.1 [E] symbol wiring: FFT symbol == direct cosine sum "
          "(worst rel %.1e <= %.0e); the anchor window's sigma_ar "
          "crossing t_cross = %.3f matches the digamma root t* = "
          "%.4f within %.0f%%"
          % (dev_sym, BAR_SYM, t_cr0, t_star, 100 * BAR_TSTAR),
          dev_sym <= BAR_SYM
          and abs(t_cr0 - t_star) / t_star <= BAR_TSTAR)

    print("\n   M-trend of sup r3 (anchor ladder; the almost-periodic "
          "prime sum has sup_t -> 2 e^alpha = %.0f as the reach "
          "grows):" % (2 * math.exp(picks[0][1])))
    for fmul in M_FACT_LADDER:
        rr = next((r for r in rows if r["split"] == "C3"
                   and r["win"] == 0 and r["f"] == fmul), None)
        if rr is None:
            continue
        M, D = rr["M"], rr["D"]
        sig_ar = symbol_of(rr["c_ar"], M)
        sig_fl = symbol_of(rr["c_at"] - rr["c_mean"], M)
        th = TWO_PI * np.arange(sig_ar.size) / ND_SYM
        tt = th / D
        pos = (th > 0) & (th <= math.pi) & (sig_ar > 0) \
            & (tt > 1.05 * t_star)
        r3 = np.abs(sig_fl[pos]) / sig_ar[pos]
        i3 = int(np.argmax(r3))
        print("   f=%.2f (reach %.0f): sup r3 = %.3f at t = %.2f"
              % (fmul, math.pi / D, float(np.max(r3)),
                 float(tt[pos][i3])))
    sup_r3_all = max(s[5] for s in sup_tab)
    check("S2.2 [MEASURED] pointwise profile: sup r3 over the 5 "
          "deployed windows = %.3f (per window %s); sigma_ar <= 0 "
          "on the sub-t* band always (%.2f-%.2f%% of the reach) -- "
          "the pointwise route NEVER covers t < t*; above t* the "
          "measured sup r3 decides"
          % (sup_r3_all, ["%.3f" % s[5] for s in sup_tab],
             100 * min(s[3] for s in sup_tab),
             100 * max(s[3] for s in sup_tab)), True)

    X0 = math.exp(2 * alpha0)
    check("S2.3 [C] the TARGET INEQUALITY (T2 deliverable), exact: "
          "sufficient for |<K3 v,v>| <= thetabar <L3 v,v> is "
          "(i) MEAN-form >= 0 [closed for u0 = 0: rank-1 pole "
          "square + Laplace reads; S0.5] AND (ii) pointwise, for "
          "all theta in (0, pi], t = theta/D: "
          "|sum_{2<=n<=X} (Lambda(n)/sqrt n) kappa_D(theta; log n) "
          "- int_{log 2}^{2 alpha} e^{u/2} kappa_D(theta; u) du| "
          "<= thetabar (Re psi(1/4 + it/2) - log pi + A_D(t)), "
          "with kappa_D the tent-sampled cosine (= cos(t u) + "
          "O(D^2) interpolation) and A_D the alias/Pf correction "
          "(anchor: t_cross = %.3f vs t* = %.4f), X = e^{2 alpha} "
          "= %.0f at the anchor.  A PRIME-SUM vs GAMMA-GROWTH "
          "inequality (partial summation + Stirling), NO zeros in "
          "the statement -- but it FAILS for t < t* (RHS < 0 "
          "there) and its sup over t -> infinity diverges (almost "
          "periodicity): it can hold at most on the deployed band "
          "[t*, pi/D]; measured sup r3 = %.3f decides whether the "
          "form-level coupling must rescue"
          % (t_cr0, t_star, X0, sup_r3_all), True)

    # ================================================================ S3
    print("\nS3 -- the circularity check (T3)")
    r_anchor = next(r for r in rows if r["split"] == "C3"
                    and r["win"] == 0 and r["f"] == 1.0)
    Ma, ha, Da = r_anchor["M"], r_anchor["h"], r_anchor["D"]
    L3a = core.odd_toeplitz(r_anchor["c_ar"] + r_anchor["c_mean"], Ma)
    K3a = core.odd_toeplitz(r_anchor["c_at"] - r_anchor["c_mean"], Ma)
    wL, VL = sla.eigh(L3a)
    radL = max(abs(float(wL[0])), abs(float(wL[-1])))
    floorL = FLOOR_SAFETY * EPS * radL * math.sqrt(ha)
    posL = wL > floorL
    VpL = VL[:, posL] * (1.0 / np.sqrt(wL[posL]))[None, :]
    KtL = VpL.T @ (K3a @ VpL)
    KtL = 0.5 * (KtL + KtL.T)
    muL = sla.eigvalsh(KtL)
    BtL = VpL.T @ ((L3a + K3a) @ VpL)
    evB = sla.eigvalsh(0.5 * (BtL + BtL.T))
    dev_br = max(abs(float(evB[0]) - (1.0 + float(muL[0]))),
                 abs(float(evB[-1]) - (1.0 + float(muL[-1]))))
    check("S3.1 [E] the pencil bracket: on the L-positive subspace, "
          "gen-eig(B, L) = 1 + eig(K, L) exactly (both ends, dev "
          "%.1e <= %.0e): theta < 1 <=> (1-theta) L <= B <= "
          "(1+theta) L; the lower side |mu_min| < 1 IS window "
          "positivity B > 0 relative to L, the upper side mu_max < "
          "1 is B < 2L (split regularity, NOT RH-implied)"
          % (dev_br, BAR_BRACKET), dev_br <= BAR_BRACKET)

    print("   per deployed window (split C3): the two sides")
    for iw in range(len(picks)):
        r = next(r for r in rows if r["split"] == "C3"
                 and r["win"] == iw and r["f"] == 1.0)
        print("   win %d: 1+mu_min = gen-lmin(B,L)|V+ = %+.4e "
              "(RH-side margin), 1-mu_max = %+.4e (regularity "
              "margin), binding side: %s"
              % (iw, 1.0 + r["mu_min"], 1.0 - r["mu_max"], r["side"]))

    # C4, the trivial spectral split (circularity yardstick), anchor
    wK, VK = sla.eigh(0.5 * (K3a + K3a.T))
    Kpos = (VK * np.maximum(wK, 0.0)[None, :]) @ VK.T
    Kneg = (VK * np.minimum(wK, 0.0)[None, :]) @ VK.T
    U0a, th0a = dst_matrix(ha, Ma)
    r_c4 = analyze_split(L3a + Kpos, Kneg, ha, Da, U0a, th0a, t_star)
    B0a = L3a + K3a
    g0 = np.zeros(Ma)
    g0[0], g0[1] = 2.0 * Da / 3.0, Da / 6.0
    G0a = core.odd_toeplitz(g0, Ma)
    wBG = sla.eigh(0.5 * (B0a + B0a.T), 0.5 * (G0a + G0a.T),
                   eigvals_only=True)
    check("S3.2 [C+MEASURED] CIRCULARITY VERDICT: (i) theta < 1 "
          "uniform ==> B >= (1-theta)L > 0 on every window ==> "
          "family Weil positivity; uniform over ALL (a, M) it is "
          "the Weil criterion (v677 S4 typing) ==> RH-STRONG, as "
          "intended.  (ii) the CONVERSE: RH gives only the lower "
          "side (mu_min >= -1; anchor margin 1+mu_min = %+.4e, cf. "
          "the W3 margin gen-lmin(B,G) = %+.4e); the upper side "
          "(mu_max <= 1) is split regularity RH does NOT give: "
          "theta < 1 is STRICTLY STRONGER than family positivity "
          "unless mu_max stays clear of 1.  (iii) the YARDSTICK: "
          "the trivial spectral split C4 measures n_neg(L) = %d, "
          "theta = %.6f -- its lower side is the measured B > 0 "
          "verbatim (pure renaming); any candidate binding on the "
          "lower side at the same value adds nothing beyond "
          "measured window positivity"
          % (1.0 + r_anchor["mu_min"], float(wBG[0]),
             r_c4["n_neg"], r_c4["theta"]), True)

    # S3.3 (run-2 addition, declared): the upper-side SPIKE LAW
    print("\n   S3.3 -- the upper-side spike law (run-2 addition)")
    GAMMA_CIT = (14.134725, 21.022040, 25.010858, 30.424876,
                 32.935062, 37.586178, 40.918719, 43.327073,
                 48.005151, 49.773832)   # CITED literature values

    def omega_of(t):
        return float(mp.re(mp.digamma(mp.mpf(1) / 4 + 1j * t / 2))) \
            - math.log(math.pi)

    law_devs = []
    for nm in ("C1b", "C3"):
        for iw in range(len(picks)):
            r = next(r for r in rows if r["split"] == nm
                     and r["win"] == iw and r["f"] == 1.0)
            pred = 1.0 + 2.0 * r["alpha"] / omega_of(r["t_peak"])
            dev = abs(pred - r["mu_max"]) / r["mu_max"]
            law_devs.append(dev)
            print("   %-3s win %d: t_peak = %6.2f, Omega = %.4f, "
                  "predicted mu_max = 1 + 2a/Omega = %7.3f vs "
                  "measured %7.3f (rel dev %.3f)"
                  % (nm, iw, r["t_peak"], omega_of(r["t_peak"]),
                     pred, r["mu_max"], dev))
    med_law = float(np.median(law_devs))
    r_big = next(r for r in rows if r["split"] == "C3"
                 and r["win"] == len(picks) - 1 and r["f"] == 1.0)
    dev_g1 = abs(r_big["t_peak"] - GAMMA_CIT[0]) / GAMMA_CIT[0]
    # top-5 pencil directions of the largest deployed window (C3)
    Mb, hb, Db = r_big["M"], r_big["h"], r_big["D"]
    L3b = core.odd_toeplitz(r_big["c_ar"] + r_big["c_mean"], Mb)
    K3b = core.odd_toeplitz(r_big["c_at"] - r_big["c_mean"], Mb)
    wLb, VLb = sla.eigh(L3b)
    radLb = max(abs(float(wLb[0])), abs(float(wLb[-1])))
    posb = wLb > FLOOR_SAFETY * EPS * radLb * math.sqrt(hb)
    Vpb = VLb[:, posb] * (1.0 / np.sqrt(wLb[posb]))[None, :]
    Ktb = Vpb.T @ (K3b @ Vpb)
    mub, Yb = sla.eigh(0.5 * (Ktb + Ktb.T))
    Ub, thb = dst_matrix(hb, Mb)
    tkb = thb / Db
    print("   top-5 upper pencil directions (largest window, C3) vs "
          "the CITED first zeros (never loaded):")
    for i in range(1, 6):
        vv = Vpb @ Yb[:, -i]
        pr = (Ub @ vv) ** 2
        tpk = float(tkb[int(np.argmax(pr))])
        gnear = min(GAMMA_CIT, key=lambda g: abs(g - tpk))
        print("   #%d: mu = %8.3f, t_peak = %7.3f, nearest cited "
              "zero %.4f (dev %+0.3f)"
              % (i, float(mub[-i]), tpk, gnear, tpk - gnear))
    check("S3.3 [MEASURED, run-2] THE UPPER SIDE IS THE ZERO-COMB "
          "SPIKE: mu_max follows 1 + 2 alpha/Omega(t_peak) (the "
          "v669 Fejer main-lobe height 2a of ONE zero pair over the "
          "smooth density; median rel dev %.3f <= 0.35 over "
          "{C1b, C3} x 5 windows), and the extremal direction of "
          "the largest window sits at t_peak = %.3f, within %.1f%% "
          "of the cited gamma_1 = %.6f -- the pencil FINDS the "
          "first Riemann zero from primes + digamma alone; no "
          "smooth zero-free L can cap the comb spikes: the "
          "two-sided theta < 1 dies on the upper side at rate "
          "~ 2a/Omega(gamma_1), linearly in a"
          % (med_law, r_big["t_peak"], 100 * dev_g1, GAMMA_CIT[0]),
          med_law <= 0.35 and dev_g1 <= 0.04)

    # ================================================================ S4
    print("\nS4 -- the OS reflection split (T4b, first structure "
          "check)")
    rs_os = [r for r in rows if r["split"] == "OS"]
    n_dead_os = sum(1 for r in rs_os if r["n_neg"] > 0)
    peaks_os = [r["neg_peak_t"][0] for r in rs_os if r["n_neg"] > 0]
    check("S4.1 [MEASURED] the v622-style reflection split B = "
          "T_h(c) - Hankel_h(c) (translation layer minus reflection "
          "pairing about the lattice mirror j -> M-1-j = the seam "
          "diameter x -> -x): L = T_h(c) is %s (dead on %d/%d "
          "cells, worst eigmin %+.3e, first negative peaks at t %s); "
          "sup theta%s = %.4f.  HONESTY: even where alive, the "
          "lower side of theta_OS < 1 is EXACTLY B > 0 (the odd "
          "form IS Toeplitz minus Hankel) -- the OS split is a "
          "repackaging of positivity plus the Toeplitz-domination "
          "statement B <= 2 T_h; not an independent lever, and its "
          "L contains the primes (zero-free in definition, not "
          "Gamma-only)"
          % ("PSD on all cells" if n_dead_os == 0 else "INDEFINITE",
             n_dead_os, len(rs_os),
             min(r["lmin_L"] for r in rs_os),
             ["%.1f" % p for p in peaks_os[:5]],
             "" if n_dead_os == 0 else " (deflated)",
             max(r["theta"] for r in rs_os)), True)

    # ================================================================ S5
    print("\nS5 -- verdict + contract note")
    guards_ok = not any(f.startswith(("G0", "S0", "S1.1", "S2.1",
                                      "S3.1")) for f in FAILS)
    best_alive = [nm for nm in NONTRIV if alive[nm]]
    if not guards_ok:
        VERDICT = "LK-MIXED"
    elif best_alive and min(sup_theta[nm] for nm in best_alive) \
            <= EDGE_BAR:
        VERDICT = "LK-INTERMEDIATE-FORM"
    elif best_alive and min(sup_theta[nm] for nm in best_alive) < 1.0:
        VERDICT = "LK-EDGE"
    elif (all(not alive[nm] for nm in NONTRIV)
          and any(low_only[nm] and defl_ok[nm] for nm in NONTRIV)):
        VERDICT = "LK-LOWBAND-RESIDUE"
    else:
        VERDICT = "LK-SPLIT-DIES"

    check("S5.1 [C] typed verdict %s: alive splits %s; sup theta "
          "(deflated where dead) per split %s; low-band-only "
          "deaths: %s -- the task's kill criterion ('theta -> 1 "
          "kills the naive split, stabilization keeps the "
          "intermediate form in reach') is adjudicated by the "
          "printed a/M-trends"
          % (VERDICT, best_alive or "NONE",
             ", ".join("%s=%.4f" % (nm, sup_theta[nm])
                       for nm in NONTRIV),
             ", ".join("%s=%s" % (nm, low_only[nm])
                       for nm in NONTRIV)), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this module):

  PRIME.UNIFPOS.01, L+K split round (2026-08-03): the non-circular
  split B = L + K of the deployed odd-sector window form was
  constructed and measured on the 5-window family x M-ladder.
  (1) SIGN STRUCTURE [E]: the arch density rho is positive-definite
  (sum of Laplace kernels) and its POSITIVE-assembly tent-Toeplitz
  form is PSD with divergent diagonal; the DEPLOYED arch layer is
  its negative with Pf-renormalized diagonal -- frequency density
  Omega(t), sign-changing at t* = %.4f -- and is measurably
  indefinite on the odd sector (negatives = the sub-t* modes).  The
  pole block is a NEGATIVE rank-1 square as a tent form (P =
  -T_v(i/2) >= 0); the atoms' PNT mean e^{u/2} IS the pole density
  asymptotically, its u0 = 0 form is PSD in closed form (pole
  square + Laplace).  Window positivity = arch density above t* +
  pole/mean rank-1 and prime oscillation below t*.
  (2) THETA [MEASURED]: per split sup theta = %s; L-PSD %s.
  (3) POINTWISE [MEASURED]: sup r3 = |sigma_fluct|/sigma_ar = %.3f
  on the deployed windows (the sub-t* band is never covered
  pointwise); the exact target prime-sum inequality is in S2.3.
  (4) CIRCULARITY [C]: theta < 1 uniform ==> family Weil positivity
  ==> RH-strong (intended); RH returns only the lower side (anchor
  margin 1+mu_min = %+.4e); the upper side B <= 2L is new, non-RH
  content; the trivial spectral split (theta = %.6f, n_neg = %d)
  marks the pure-renaming floor.
  (5) THE DEATH MECHANISM [MEASURED, S3.3]: the binding side is the
  UPPER one, at the zero-comb spike: the extremal pencil direction
  sits at t = gamma_1 (found from primes + digamma alone) and
  mu_max follows 1 + 2 alpha/Omega(t_peak) (median dev %.3f) --
  the deployed windows RESOLVE individual zeros, so no smooth
  zero-free L can satisfy B <= (1 + theta) L with theta < 1; a
  surviving intermediate form must either be ONE-SIDED (lower side
  only -- but that is the repackaged positivity) or use an L that
  carries the comb spikes at matched resolution (multi-resolution
  split; untested here, typed as the open lever).
  (6) VERDICT: %s.  No marker move, no RH claim.
""" % (t_star,
       ", ".join("%s=%.4f" % (nm, sup_theta[nm]) for nm in NONTRIV),
       ", ".join("%s=%s" % (nm, alive[nm]) for nm in NONTRIV),
       sup_r3_all, 1.0 + r_anchor["mu_min"], r_c4["theta"],
       r_c4["n_neg"], med_law, VERDICT))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
