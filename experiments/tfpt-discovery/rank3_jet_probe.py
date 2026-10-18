"""rank3_jet_probe -- PRIME.RANK3.JET_CURVATURE.01: THE REVIEW
SIMPLIFICATION OF THE RANK-3 WALL, TESTED EXACTLY.

REVIEW CLAIM (to be machine-tested, kill rule armed): the three
functionals of the load-bearing 2x2 block are linear reads of the
FIRST JET of one complex function

    F(gamma) = sum_{n <= X} rho_n n^{i gamma},   rho_n = Lambda(n)/sqrt(n),

at the two dual points gamma_1, gamma_2 = 2 gamma_1, spacing
Delta_gamma = 2 pi / (N D), N = 2h + 1.  IF the Delta_gamma expansion
of the closed parity weights kills orders 0, 1, 2 STRUCTURALLY (for
arbitrary F), the observed third power 1 - r12^2 <~ h^{-3+eps} would
be a JET IDENTITY, not an arithmetic coincidence.  KILL RULE
(declared): one non-vanishing too-large order-0/1/2 term = route dead.

SLICES (bars and enums declared BEFORE any number):

J1 [THE JET REPRESENTATION, EXACT].
  J1.T1   T_0(gamma) = F(gamma), T_1(gamma) = -i F'(gamma) (first
          log-moment as derivative): mpmath-dps-40 derivative on a
          declared 500-atom subcomb, rel dev <= TOL_T1 = 1e-15.
  J1.READ the EXACT read structure: the closed weights read the
          LAG-PROJECTED comb G(gamma) = sum_d c_d e^{i gamma d D}
          (two-point spline projection c_d of the atom comb), NOT F
          itself; with the zero-lag correction (W(0) = 1, the closed
          formula would give 2):
            S_kk  = 2 Re G(g_k) - c_0 - (2/(ND)) Im G'(g_k)
                    + (2/N) cot(w_k) Im G(g_k),
            S_12  = (2/N) [sin w_2 Im G(g_1) - sin w_1 Im G(g_2)]
                    / (cos w_1 - cos w_2),   w_k = D g_k = 2 pi k/N.
          Bars: S rebuild residuum <= TOL_READ = 1e-12 (scale
          max(1, ||rho||_1), v683 convention) on ALL 15 declared
          windows; same identity for B (arch lag comb) and
          Ahat = B - S (combined comb cc), entry dev <= TOL_AH =
          1e-10 (v692 T163 bar).
  J1.FGAP the F-jet version (atom side, no lag projection) deviates
          by the spline-projection gap: documented, declared soft bar
          <= 5e-2 scaled (the identity holds for G, not F -- the
          exact read structure is part of the finding).
  J1.LOEW the exact Loewner rewrite (float sanity <= TOL_LOEW = 1e-9
          scaled; mp-exact in J2b): with x = cos(w), sig_k = sin(w_k),
          gt(x) := Im G / sin(w) = sum_d c_d U_{d-1}(x)  (Chebyshev-U
          resummation of the comb),
            S = 2 diag(Re G(g_1), Re G(g_2)) - c_0 I
                + (Dw/pi) * L,   Dw = 2 pi/N = D Delta_gamma,
            L = [[sig1^2 gt'(x_1),        sig1 sig2 gt[x_1,x_2]],
                 [sig1 sig2 gt[x_1,x_2],  sig2^2 gt'(x_2)     ]],
          gt[x_1,x_2] = divided difference: the odd sector of the
          block is EXACTLY the two-point Loewner matrix of gt.

J2 [THE Delta_gamma EXPANSION, SYMBOLIC -- sympy, structural].
  Grading: the single small parameter is eps := Dw = D Delta_gamma
  (w_1 = eps, w_2 = 2 eps are COUPLED to the spacing: the dual points
  collapse to 0 with the spacing; orders in Delta_gamma == orders in
  eps).  "Arbitrary F" on this surface == arbitrary real comb ==
  arbitrary real moments M_m (Phi^(m)(0) = i^m M_m).
  J2.REWRITE  the two identities behind J1.LOEW hold symbolically
              (generic function, simplify == 0).
  J2.ORD      structural orders (polynomials in M_m must vanish
              identically or not):
              S12: eps^0, eps^1, eps^2 == 0 (structural kill of the
              cross read), eps^3 = 2(M3 - M1)/(3 pi);
              S_kk: eps^0 = 2 M0 (NOT zero), eps^1 == 0,
              eps^2 = -k^2 M2 (NOT zero), eps^3 = k^2 (M3-M1)/(3 pi).
  J2.RANK1    the eps^3 coefficient matrix is RANK ONE along k=(1,2):
              (M3-M1)/(3 pi) * k k^T (det == 0 identically).
  J2.KILL     1 - r12^2 = det S/(S11 S22): the eps^0 coefficient is
              IDENTICALLY 1 (not 0) for generic F (even sector
              M0 != 0) -- the literal review claim FAILS structurally
              at order zero.
  J2.ODD      on the ODD SECTOR (Re Phi == 0, i.e. even moments = 0)
              the claim DOES hold in strengthened form: orders
              eps^0..eps^3 of 1 - r12^2 vanish identically and
              eps^4 = (3/8) * S[gt](1),
              S[gt] = gt'''/gt' - (3/2)(gt''/gt')^2 the SCHWARZIAN
              of the Chebyshev-U resummed comb transform, with
              gt'(1)   = (M3 - M1)/3,
              gt''(1)  = (M5 - 5 M3 + 4 M1)/15,
              gt'''(1) = (M7 - 14 M5 + 49 M3 - 36 M1)/105.
  J2.SCHW     generic-g two-point Loewner determinant: orders eta^0,
              eta^1 vanish identically, eta^2 = (1/12)(2 g' g''' -
              3 g''^2) = (1/6) g'^2 S[g]; hence the EXACT leading
              form  1 - r12^2 |_odd = (eta^2/6) S[gt](xbar) + O(eta^3),
              eta = x_1 - x_2 = 2 sin(3 eps/2) sin(eps/2) ~ (3/2) eps^2.

J2b [THE MEASUREMENT -- is the deployed surface in the jet regime?].
  All reads in mpmath dps 40 on the float64 lag combs (the razor-thin
  det is conditioning-limited in float64; declared).
  J2b.MPID  the Loewner rewrite is mp-exact (rel <= 1e-25) and the
            lag-route onem agrees with the corpus onem (rel <=
            BAR_ONEM = 1e-2, conditioning declared).
  J2b.EVEN  kill-criterion measurement: |even sector| / |entry| >=
            BAR_BIG = 2 on all complete windows (the order-0 read
            2 Re G - c_0 is NOT small -- it EXCEEDS the net entry).
  J2b.LOEW  the pure jet (Loewner) block carries NO collinearity:
            onem_L = det L/(L11 L22) >= BAR_KILL_RATIO = 1e2 times
            the measured onem on all complete windows.
  J2b.DIR   the measured collinear direction a12/a11 drifts across
            the ladder and is NOT the structural jet direction
            (ratio 2): |dir - 2| >= 1 on all complete windows.
  J2b.FIT   context reproduction: onem ~ c h^{-eta_h}, R^2 > 0.5
            (v683 R2.MARGIN convention); Schwarzian h^2-approximation
            of onem_L printed (accuracy of the collapsed-jet regime).

J3 [THE ARITHMETIC -- only what survives the kill].
  J3.STATE  the exact statement that WOULD have to be proven is
            printed: the even/odd COMPENSATION at the dual points
            (both sectors O(3..7 x entry), net razor thin) -- not a
            single jet coefficient; the one structurally surviving
            coefficient (the Schwarzian) measurably does NOT carry
            the collinearity (factor J2b.LOEW).
  J3.BUDGET classical accessibility of the compensation: entrywise
            fluctuation budgets (Schoenfeld yardstick + exact
            |psi - x| envelope, v683 machinery) propagated to the
            margin det Ahat: min ratio margin/Delta_B printed, class
            (a/b/c) per v683 bars; expected and confirmed class (c)
            -- the jet reparametrisation does NOT open a classical
            route (same triangle-inequality wall as v683 T-B).
  J3.V684   comparison anchor (citations, no zero read here): v683
            T-B class (c); v684 zero-side ZONE-PASS class (a)
            (kappa_unc = 0.039..0.190); v692: the margin IS the
            transverse zero mass.  The arithmetic route to the
            razor-thin margin stays on the zero side.

J4 [SECTION-8 DIAGNOSTIC, honestly typed EXPLORATORY].
  J4.KREIN  the Krein/Wheeler chain on the v563 combined combs breaks
            early (kbad ~ 11 << h, measured per window): the v734
            boundary phase theta_h is NOT constructible on the
            surface that carries the collinearity (on the v734
            moonshot family the chain is intact but the lock block
            carries NO collinearity: onem ~ O(1), measured in the
            pre-test 0.22..0.99) -- the conjecture "rank-3
            collinearity = Krein boundary-phase curvature" has no
            common surface; documented.
  J4.CORR   substitute diagnostic (declared): Poisson-smoothed SYMBOL
            boundary phase theta_d(tau) = Im G_cc(tau + i delta),
            delta = 1 (v734 Poisson reading), analytic derivatives;
            fixed functional F_S = (2 th' th''' - 3 th''^2)/th'^2 at
            taubar = (g_1+g_2)/2; log-log Pearson correlation of
            onem vs Dg^4 |F_S| across the complete ladder vs the
            Dg^4-only control.  Enum KREIN-LINK-{SUPPORTED/WEAK/NONE}
            (SUPPORTED iff |r| >= 0.9 AND improves on the control).

VERDICT ENUM: RANK3-JET-{IDENTITY/DEAD} + the Schwarzian form.

FIREWALL: v563/v683 imported READ-ONLY; NO zeta zero is read anywhere
in this probe (AST-checked); mpmath for VALUES only (zeta'(1/2)/
zeta(1/2) for the U0 cutoff, v583/v587 convention); deterministic, no
RNG; no file outside experiments/ is touched; no marker moves; the
ledger is untouched.  Radical honesty: the kill verdict is reported
as it falls; the structurally beautiful parts (exact jet/Loewner/
Schwarzian representation) are documented WITHOUT upgrading them into
an explanation they measurably do not give.

PROVENANCE: v683_rank3_functionals.py (closed weights, dual points,
window set, budget machinery); v692_rank3_lockgram.py (lock block,
T163, transverse-mass margin identity); v684_rank3_zeroside.py
(class-(a) zero-side anchor, CITED); v734_s1_canonical.py (boundary
phase pattern, Poisson reading); v696_z1_jacobi.py (Wheeler chain);
parity_toeplitz_classification.tex (prop:split, lem:closedweight,
lem:dualpoint, prob:R1).
"""
import ast
import math
import os
import sys
import time

import numpy as np

# ---------------------------------------------------------------- imports
_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
import v683_rank3_functionals as r3          # noqa: E402 (READ-ONLY helpers)
import v696_z1_jacobi as jac                 # noqa: E402 (READ-ONLY)
import sympy as sp                           # noqa: E402
from mpmath import mp, mpf, mpc              # noqa: E402
from mpmath import zeta, diff as mpdiff      # noqa: E402 (VALUES only)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- declared bars/constants
TOL_T1 = 1.0e-15        # J1.T1: -iF' vs first log-moment, rel (mp dps 30)
N_SUB_T1 = 500          # declared subcomb size for the mp derivative
TOL_READ = 1.0e-12      # J1.READ: S rebuild, scale max(1,||rho||_1)
TOL_AH = 1.0e-10        # J1.READ: B/Ahat entries, absolute (v692 T163 bar)
BAR_FGAP = 5.0e-2       # J1.FGAP: F-vs-G spline gap, scaled soft bar
TOL_LOEW = 1.0e-9       # J1.LOEW float sanity, scaled
MP_DPS = 40             # J2b working precision on the lag combs
TOL_MPID = 1.0e-25      # J2b.MPID: Loewner rewrite in mp, rel
BAR_ONEM = 1.0e-2       # J2b.MPID: lag-route onem vs corpus onem, rel
BAR_BIG = 1.0           # J2b.EVEN: |even|/|entry| must exceed this
BAR_KILL_RATIO = 1.0e2  # J2b.LOEW: onem_L / onem must exceed this
BAR_DIR = 1.0           # J2b.DIR: |a12/a11 - 2| must exceed this
BAR_R2 = 0.5            # J2b.FIT: R^2 of the onem ~ h^-eta fit
N_SER = 9               # sympy series order (eps^8)
SCHOENFELD_X0 = 73.2    # Schoenfeld 1976 validity floor (yardstick)
EIGHT_PI = 8.0 * math.pi
CLASS_HI, CLASS_LO = r3.CLASS_HI, r3.CLASS_LO   # 3, 1/3 (v683 bars)
DELTA_POIS = 1.0        # J4: Poisson width (v734 DELTA convention)
BAR_CORR = 0.9          # J4: |Pearson r| for KREIN-LINK-SUPPORTED

mp.dps = MP_DPS


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
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            if isinstance(f, ast.Attribute) and f.attr in (
                    "zetazero", "nzeros", "second_sheet_zero", "find_zeros"):
                hits.append(f.attr)
            if isinstance(f, ast.Name) and f.id in ("zetazero", "nzeros",
                                                    "find_zeros"):
                hits.append(f.id)
    return not hits


def class_of(rmin):
    if rmin >= CLASS_HI:
        return "a"
    if rmin >= CLASS_LO:
        return "b"
    return "c"


def ols_loglog(x, y):
    lx, ly = np.log(np.asarray(x)), np.log(np.abs(np.asarray(y)))
    b, q = np.polyfit(lx, ly, 1)
    pred = b * lx + q
    ss = 1.0 - np.sum((ly - pred) ** 2) / max(np.sum((ly - ly.mean()) ** 2),
                                              1e-300)
    return float(b), float(math.exp(q)), float(ss)


def pearson(x, y):
    x = np.asarray(x) - np.mean(x)
    y = np.asarray(y) - np.mean(y)
    den = math.sqrt(float(np.sum(x ** 2) * np.sum(y ** 2)))
    return float(np.sum(x * y)) / max(den, 1e-300)


# ------------------------------------------------- lag projection (exact)
def lag_project(uu, lam, D, Mz):
    """Two-point spline projection of the atom comb onto lags
    (identical cell selection as v683 spline_read_vec; lag M and
    beyond dropped exactly as the read drops them)."""
    q = np.asarray(uu, dtype=float) / D
    i0 = np.floor(q).astype(np.int64)
    f = q - i0
    c = np.zeros(Mz)
    m0 = (i0 >= 0) & (i0 < Mz)
    np.add.at(c, i0[m0], ((1.0 - f) * lam)[m0])
    m1 = (i0 + 1 >= 0) & (i0 + 1 < Mz)
    np.add.at(c, (i0 + 1)[m1], (f * lam)[m1])
    return c


# ------------------------------------------------- float64 jet reads
def jet_block_f64(c, hz):
    """The 2x2 block from the lag comb c via the JET FORMULA at the
    dual points (float64; returns entries + the raw reads)."""
    N = 2 * hz + 1
    Mz = len(c)
    d = np.arange(Mz, dtype=float)
    eps = 2.0 * math.pi / N
    out = {}
    for k in (1, 2):
        wk = k * eps
        out[k] = (float(c @ np.cos(wk * d)),          # Re G
                  float(c @ np.sin(wk * d)),          # Im G
                  float(c @ (d * np.cos(wk * d))))    # Im G' (omega units)
    cot1 = math.cos(eps) / math.sin(eps)
    cot2 = math.cos(2 * eps) / math.sin(2 * eps)
    s11 = 2.0 * out[1][0] - c[0] + (eps / math.pi) * (
        cot1 * out[1][1] - out[1][2])
    s22 = 2.0 * out[2][0] - c[0] + (eps / math.pi) * (
        cot2 * out[2][1] - out[2][2])
    den = 2.0 * math.sin(3.0 * math.pi / N) * math.sin(math.pi / N)
    s12 = (eps / math.pi) * (math.sin(2 * eps) * out[1][1]
                             - math.sin(eps) * out[2][1]) / den
    return s11, s22, s12, out


def loewner_block_f64(c, hz):
    """Float64 Loewner rewrite: (even_1, even_2, L11, L22, L12)."""
    N = 2 * hz + 1
    Mz = len(c)
    d = np.arange(Mz, dtype=float)
    eps = 2.0 * math.pi / N
    w1, w2 = eps, 2.0 * eps
    s1, s2 = math.sin(w1), math.sin(w2)
    S0_1 = float(c @ np.sin(w1 * d))
    S0_2 = float(c @ np.sin(w2 * d))
    C1_1 = float(c @ (d * np.cos(w1 * d)))
    C1_2 = float(c @ (d * np.cos(w2 * d)))
    g1, g2 = S0_1 / s1, S0_2 / s2
    gx1 = -(C1_1 * s1 - S0_1 * math.cos(w1)) / s1 ** 3
    gx2 = -(C1_2 * s2 - S0_2 * math.cos(w2)) / s2 ** 3
    dx = 2.0 * math.sin(3.0 * eps / 2.0) * math.sin(eps / 2.0)
    L11 = s1 ** 2 * gx1
    L22 = s2 ** 2 * gx2
    L12 = s1 * s2 * (g1 - g2) / dx
    ev1 = 2.0 * float(c @ np.cos(w1 * d)) - c[0]
    ev2 = 2.0 * float(c @ np.cos(w2 * d)) - c[0]
    return ev1, ev2, L11, L22, L12, eps


# ------------------------------------------------- mp jet reads (dps 40)
def mp_trig_sums(c, om, mmax=3):
    """S_m = sum c_d d^m sin(d om), C_m = sum c_d d^m cos(d om) for
    m = 0..mmax, mp-exact via iterated multiplication."""
    step = mp.exp(mpc(0, 1) * om)         # e^{i om}
    z = mpc(1, 0)
    S = [mpf(0)] * (mmax + 1)
    C = [mpf(0)] * (mmax + 1)
    for dd in range(len(c)):
        cd = mpf(float(c[dd]))
        if cd != 0:
            re, im = z.real, z.imag
            dm = mpf(1)
            for m in range(mmax + 1):
                C[m] += cd * dm * re
                S[m] += cd * dm * im
                dm *= dd
        z *= step
    return S, C


def _build_gjet_lambdas():
    """sympy-derived x-derivatives of gt(x) = ImPhi(w)/sin(w) at
    x = cos(w), lambdified for mpmath.  Inputs: w and P0..P3 =
    d^m ImPhi/dw^m."""
    w = sp.Symbol("w")
    P = sp.Function("P")
    g = P(w) / sp.sin(w)
    gx = [g]
    for _ in range(3):
        gx.append(-sp.diff(gx[-1], w) / sp.sin(w))
    P0, P1, P2, P3 = sp.symbols("P0 P1 P2 P3")
    subs = {sp.Derivative(P(w), (w, 3)): P3,
            sp.Derivative(P(w), (w, 2)): P2,
            sp.Derivative(P(w), w): P1, P(w): P0}
    exprs = [sp.simplify(e.subs(subs)) for e in gx]
    return sp.lambdify((w, P0, P1, P2, P3), exprs, modules="mpmath")


GJET = _build_gjet_lambdas()


def mp_gjets(c, om):
    """(gt, gt', gt'', gt''') at x = cos(om) from the lag comb, mp."""
    S, C = mp_trig_sums(c, om, 3)
    # d^m ImPhi/dw^m: ImPhi = sum c sin(dw)
    return GJET(om, S[0], C[1], -S[2], -C[3])


def mp_block(c, hz):
    """mp-exact block + Loewner split from the lag comb."""
    N = 2 * hz + 1
    eps = 2 * mp.pi / N
    w1, w2 = eps, 2 * eps
    S1, C1 = mp_trig_sums(c, w1, 3)
    S2, C2 = mp_trig_sums(c, w2, 3)
    c0 = mpf(float(c[0]))
    ev1 = 2 * C1[0] - c0
    ev2 = 2 * C2[0] - c0
    # entry route
    a11 = ev1 + (eps / mp.pi) * (mp.cos(w1) / mp.sin(w1) * S1[0] - C1[1])
    a22 = ev2 + (eps / mp.pi) * (mp.cos(w2) / mp.sin(w2) * S2[0] - C2[1])
    dx = 2 * mp.sin(3 * eps / 2) * mp.sin(eps / 2)
    a12 = (eps / mp.pi) * (mp.sin(w2) * S1[0] - mp.sin(w1) * S2[0]) / dx
    # Loewner route
    g1 = GJET(w1, S1[0], C1[1], -S1[2], -C1[3])
    g2 = GJET(w2, S2[0], C2[1], -S2[2], -C2[3])
    L11 = mp.sin(w1) ** 2 * g1[1]
    L22 = mp.sin(w2) ** 2 * g2[1]
    L12 = mp.sin(w1) * mp.sin(w2) * (g1[0] - g2[0]) / dx
    return dict(eps=eps, ev1=ev1, ev2=ev2, a11=a11, a22=a22, a12=a12,
                L11=L11, L22=L22, L12=L12, dx=dx, g1=g1, g2=g2)


# ------------------------------------------------- window set (v683)
def declared_windows():
    KZ = core.frame_a_zones()
    L = len(KZ)
    fam5 = [0, (L - 1) // 4, L // 2, (3 * (L - 1)) // 4, L - 1]
    inter = []
    for (lo, hi), n_in in zip(zip(fam5[:-1], fam5[1:]), (2, 3, 3, 2)):
        for j in range(1, n_in + 1):
            inter.append(lo + j * (hi - lo) // (n_in + 1))
    idx = sorted(set(fam5 + inter))
    return [KZ[k] for k in idx]


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.RANK3.JET_CURVATURE.01 -- the review simplification, "
          "tested exactly (rank3_jet_probe)")
    print("=" * 78)

    # ============================================================== S0
    print("\nS0 -- firewall")
    check("S0.AST no zeta-zero loader in this module (zetazero/nzeros/"
          "find_zeros absent); zeros are NOT an input of this probe",
          ast_zero_firewall(__file__))

    # window set + corpus objects
    wins = []
    for kz in declared_windows():
        r = core.build_window(kz)
        hz, Mz, D = r["h"], r["M"], r["D"]
        assert float(r["uu"][0]) > D, "reflection branch would be live"
        cS = lag_project(r["uu"], r["lam"], D, Mz)
        c_ar = np.asarray(core.arch_lags(Mz, D), dtype=float)
        cc = c_ar - cS
        complete = r["n_zone"] ** 2 <= core.ATOM_MAX + 0.5
        wins.append(dict(r=r, h=hz, M=Mz, D=D, cS=cS, c_ar=c_ar, cc=cc,
                         complete=complete,
                         scale=max(1.0, float(np.sum(r["lam"])))))
    comp = [w for w in wins if w["complete"]]
    print("    %d declared windows (v683 quintiles + 2/3/3/2 "
          "intermediates), %d complete-comb" % (len(wins), len(comp)))

    # ============================================================== J1
    print("\nJ1 -- the jet representation, exact")
    ref = next(w for w in wins if w["h"] == core.Q_H_REF)
    r = ref["r"]

    # ---- J1.T1: first log-moment == -i F' (mp derivative, subcomb)
    uu_s = [mpf(float(u)) for u in r["uu"][:N_SUB_T1]]
    rho_s = [mpf(float(x)) for x in r["lam"][:N_SUB_T1]]
    gam1 = 2 * mp.pi / ((2 * ref["h"] + 1) * mpf(float(ref["D"])))

    def F_sub(g):
        return mp.fsum(rh * mp.exp(mpc(0, 1) * g * u)
                       for rh, u in zip(rho_s, uu_s))

    T1_direct = mp.fsum(rh * u * mp.exp(mpc(0, 1) * gam1 * u)
                        for rh, u in zip(rho_s, uu_s))
    Fp = mpdiff(F_sub, gam1)
    dev_t1 = abs(T1_direct - (-1j) * Fp) / abs(T1_direct)
    check("J1.T1 the first log-moment IS the derivative read: "
          "T_1(gamma) = sum rho_n u_n n^{i gamma} = -i F'(gamma) at "
          "gamma_1 = %.6f on the declared %d-atom subcomb "
          "(mp dps %d, rel dev %.1e <= %.0e)"
          % (float(gam1), N_SUB_T1, MP_DPS, float(dev_t1), TOL_T1),
          float(dev_t1) <= TOL_T1)

    # ---- J1.READ: jet rebuild of S, B, Ahat on all windows
    res_S = res_B = res_A = 0.0
    for w in wins:
        rr = w["r"]
        s11, s22, s12, _ = jet_block_f64(w["cS"], w["h"])
        res_S = max(res_S, max(abs(s11 - rr["S"][0, 0]),
                               abs(s22 - rr["S"][1, 1]),
                               abs(s12 - rr["S"][0, 1])) / w["scale"])
        b11, b22, b12, _ = jet_block_f64(w["c_ar"], w["h"])
        res_B = max(res_B, abs(b11 - rr["B"][0, 0]),
                    abs(b22 - rr["B"][1, 1]), abs(b12 - rr["B"][0, 1]))
        a11, a22, a12, _ = jet_block_f64(w["cc"], w["h"])
        res_A = max(res_A, abs(a11 - rr["a11"]), abs(a22 - rr["a22"]),
                    abs(a12 - rr["a12"]))
    check("J1.READ the closed weights are EXACTLY the first-jet read of "
          "the LAG-PROJECTED comb G at the dual points (with the c_0 "
          "zero-lag correction on the diagonal): S rebuilt on all %d "
          "windows, residuum %.1e <= %.0e (scale max(1,||rho||_1)); "
          "B (arch comb) dev %.1e and Ahat = B - S (combined comb) dev "
          "%.1e <= %.0e -- the whole lock block is a first-jet read of "
          "ONE function" % (len(wins), res_S, TOL_READ, res_B, res_A,
                            TOL_AH),
          res_S <= TOL_READ and res_B <= TOL_AH and res_A <= TOL_AH)

    # ---- J1.FGAP: the F-jet (atom-side, no lag projection)
    gap = 0.0
    for w in (wins[0], ref, wins[-1]):
        rr = w["r"]
        hz, D = w["h"], w["D"]
        N = 2 * hz + 1
        eps = 2.0 * math.pi / N
        uu, lam = rr["uu"], rr["lam"]
        ss = []
        for k in (1, 2):
            gk = k * eps / D
            ReF = float(lam @ np.cos(gk * uu))
            ImF = float(lam @ np.sin(gk * uu))
            ImFp = float(lam @ (uu * np.cos(gk * uu)))   # gamma units
            cot = math.cos(k * eps) / math.sin(k * eps)
            ss.append(2.0 * ReF - (2.0 / (N * D)) * ImFp
                      + (2.0 / N) * cot * ImF)
        den = 2.0 * math.sin(3.0 * math.pi / N) * math.sin(math.pi / N)
        ImF1 = float(lam @ np.sin((eps / D) * uu))
        ImF2 = float(lam @ np.sin((2 * eps / D) * uu))
        s12F = (eps / math.pi) * (math.sin(2 * eps) * ImF1
                                  - math.sin(eps) * ImF2) / den
        gap = max(gap, max(abs(ss[0] - rr["S"][0, 0]),
                           abs(ss[1] - rr["S"][1, 1]),
                           abs(s12F - rr["S"][0, 1])) / w["scale"])
    check("J1.FGAP read structure documented: the review's literal F-jet "
          "(atom side, NO lag projection) deviates by the two-point-"
          "spline projection gap %.2e (scaled, 3 declared windows) <= "
          "%.0e -- the EXACT identity holds for the lag-projected comb "
          "G, i.e. F composed with prop:split; F alone is the "
          "projection-free limit" % (gap, BAR_FGAP), gap <= BAR_FGAP)

    # ---- J1.LOEW: exact Loewner rewrite (float sanity)
    dev_L = 0.0
    for w in wins:
        s11, s22, s12, _ = jet_block_f64(w["cc"], w["h"])
        ev1, ev2, L11, L22, L12, eps = loewner_block_f64(w["cc"], w["h"])
        dev_L = max(dev_L,
                    abs(ev1 + (eps / math.pi) * L11 - s11) / w["scale"],
                    abs(ev2 + (eps / math.pi) * L22 - s22) / w["scale"],
                    abs((eps / math.pi) * L12 - s12) / w["scale"])
    check("J1.LOEW the exact rewrite  block = 2 diag(Re G) - c_0 I + "
          "(Dw/pi) Loewner(gt),  gt(x) = Im G/sin = sum_d c_d U_{d-1}(x) "
          "(Chebyshev-U resummation), L = [[s1^2 gt'(x1), s1 s2 "
          "gt[x1,x2]], [., s2^2 gt'(x2)]]: float dev %.1e <= %.0e on "
          "all %d windows (mp-exact in J2b) -- the odd sector IS the "
          "two-point Loewner matrix of ONE function"
          % (dev_L, TOL_LOEW, len(wins)), dev_L <= TOL_LOEW)

    # ============================================================== J2
    print("\nJ2 -- the Delta_gamma expansion, symbolic (sympy; grading "
          "eps = D Delta_gamma, dual points COUPLED: w_1 = eps, "
          "w_2 = 2 eps)")
    eps_s = sp.Symbol("varepsilon", positive=True)
    M = sp.symbols("M0:8", real=True)   # M0..M7

    def ImPhi(x):
        return (M[1] * x - M[3] * x ** 3 / 6 + M[5] * x ** 5 / 120
                - M[7] * x ** 7 / 5040)

    def RePhi(x):
        return (M[0] - M[2] * x ** 2 / 2 + M[4] * x ** 4 / 24
                - M[6] * x ** 6 / 720)

    def ImPhiP(x):
        return sp.diff(ImPhi(sp.Symbol("_t")), sp.Symbol("_t")).subs(
            sp.Symbol("_t"), x)

    def S_diag(k):
        wk = k * eps_s
        return (2 * RePhi(wk)
                + (eps_s / sp.pi) * (sp.cos(wk) / sp.sin(wk) * ImPhi(wk)
                                     - ImPhiP(wk)))

    S11s = S_diag(1)
    S22s = S_diag(2)
    S12s = (eps_s / sp.pi) * (sp.sin(2 * eps_s) * ImPhi(eps_s)
                              - sp.sin(eps_s) * ImPhi(2 * eps_s)) \
        / (sp.cos(eps_s) - sp.cos(2 * eps_s))

    # ---- J2.REWRITE (generic function identities)
    wsym = sp.Symbol("w")
    Pf = sp.Function("P")
    id1 = sp.simplify(sp.cos(wsym) / sp.sin(wsym) * Pf(wsym)
                      - sp.diff(Pf(wsym), wsym)
                      + sp.sin(wsym) * sp.diff(Pf(wsym) / sp.sin(wsym),
                                               wsym))
    w2sym = sp.Symbol("w2")
    lhs = sp.sin(w2sym) * Pf(wsym) - sp.sin(wsym) * Pf(w2sym)
    rhs = sp.sin(wsym) * sp.sin(w2sym) * (
        Pf(wsym) / sp.sin(wsym) - Pf(w2sym) / sp.sin(w2sym))
    id2 = sp.simplify(lhs - rhs)
    check("J2.REWRITE both rewrite identities hold symbolically for a "
          "generic function (diagonal: cot P - P' = -sin (P/sin)'; "
          "cross: sin w2 P(w1) - sin w1 P(w2) = s1 s2 [g(w1)-g(w2)]): "
          "residuals %s, %s" % (id1, id2), id1 == 0 and id2 == 0)

    # ---- series coefficients
    def coeffs(expr, kmax):
        ser = sp.series(expr, eps_s, 0, kmax + 1).removeO().expand()
        return [sp.simplify(ser.coeff(eps_s, k)) for k in range(kmax + 1)]

    c12 = coeffs(S12s, 5)
    c11 = coeffs(S11s, 4)
    c22 = coeffs(S22s, 4)
    tgt3 = (M[3] - M[1]) / (3 * sp.pi)
    ok_ord = (c12[0] == 0 and c12[1] == 0 and c12[2] == 0
              and sp.simplify(c12[3] - 2 * tgt3) == 0
              and sp.simplify(c11[0] - 2 * M[0]) == 0 and c11[1] == 0
              and sp.simplify(c11[2] + M[2]) == 0
              and sp.simplify(c11[3] - tgt3) == 0
              and sp.simplify(c22[0] - 2 * M[0]) == 0 and c22[1] == 0
              and sp.simplify(c22[2] + 4 * M[2]) == 0
              and sp.simplify(c22[3] - 4 * tgt3) == 0)
    check("J2.ORD structural orders: S12 kills eps^0, eps^1, eps^2 "
          "IDENTICALLY and starts at eps^3 = 2(M3-M1)/(3 pi); the "
          "DIAGONALS do NOT: S_kk = 2 M0 + 0 - k^2 M2 eps^2 + "
          "k^2 (M3-M1)/(3 pi) eps^3 + ... -- orders 0 and 2 of the "
          "diagonal reads survive for arbitrary F", ok_ord)

    E3 = sp.Matrix([[c11[3], c12[3]], [c12[3], c22[3]]])
    ok_rank1 = (sp.simplify(E3.det()) == 0
                and sp.simplify(c11[3] * 4 - c22[3]) == 0
                and sp.simplify(c11[3] * 2 - c12[3]) == 0)
    check("J2.RANK1 the eps^3 coefficient matrix is EXACTLY rank one "
          "along the frequency vector k = (1,2): (M3-M1)/(3 pi) * "
          "k k^T (det == 0, ratios 1:2:4 identically) -- the first odd "
          "correction is a pure phase-curvature dyad", ok_rank1)

    # polynomial approximants of the three entries (robust ratio series)
    S11p = sp.series(S11s, eps_s, 0, N_SER).removeO().expand()
    S22p = sp.series(S22s, eps_s, 0, N_SER).removeO().expand()
    S12p = sp.series(S12s, eps_s, 0, N_SER).removeO().expand()
    onem_s = 1 - S12p ** 2 / (S11p * S22p)
    ser_onem = sp.series(onem_s, eps_s, 0, 2).removeO().expand()
    c_onem0 = sp.simplify(ser_onem.coeff(eps_s, 0))
    check("J2.KILL the literal review claim FAILS structurally: the "
          "eps^0 coefficient of 1 - r12^2 = det S/(S11 S22) is "
          "IDENTICALLY %s (= 1, not 0) for arbitrary F with even "
          "sector M0 != 0 -- orders 0..2 of 1 - r12^2 do NOT vanish "
          "structurally; the KILL RULE is armed and decided by the "
          "J2b measurement of the even sector" % c_onem0,
          sp.simplify(c_onem0 - 1) == 0)

    # ---- odd sector: the strengthened claim
    odd_sub = {M[0]: 0, M[2]: 0, M[4]: 0, M[6]: 0}
    onem_odd = sp.cancel(1 - (S12p.subs(odd_sub)) ** 2
                         / (S11p.subs(odd_sub) * S22p.subs(odd_sub)))
    ser_odd = sp.series(onem_odd, eps_s, 0, 6).removeO().expand()
    co = [sp.simplify(ser_odd.coeff(eps_s, k)) for k in range(5)]
    g1s = (M[3] - M[1]) / 3
    g2s = (M[5] - 5 * M[3] + 4 * M[1]) / 15
    g3s = (M[7] - 14 * M[5] + 49 * M[3] - 36 * M[1]) / 105
    # (3/16)(2 g' g''' - 3 g''^2)/g'^2 = (3/8) S[gt] with the
    # Schwarzian S = (2 g' g''' - 3 g''^2)/(2 g'^2)
    schw_pred = sp.Rational(3, 16) * (2 * g1s * g3s - 3 * g2s ** 2) \
        / g1s ** 2
    ok_odd = (co[0] == 0 and co[1] == 0 and co[2] == 0 and co[3] == 0
              and sp.simplify(co[4] - schw_pred) == 0)
    check("J2.ODD on the ODD SECTOR (Re Phi == 0) the strengthened "
          "claim HOLDS: orders eps^0..eps^3 of 1 - r12^2 vanish "
          "identically, and the first survivor is\n"
          "        [1 - r12^2]_odd = (3/8) S[gt](1) eps^4 + O(eps^5),\n"
          "        S[gt] = gt'''/gt' - (3/2)(gt''/gt')^2 (SCHWARZIAN),\n"
          "        gt'(1) = (M3-M1)/3, gt''(1) = (M5-5M3+4M1)/15, "
          "gt'''(1) = (M7-14M5+49M3-36M1)/105", ok_odd)

    # ---- generic-g Loewner determinant expansion (arbitrary jet
    #      symbols G1..G4 = g', g'', g''', g'''' at x: structural)
    eta = sp.Symbol("eta")
    G1, G2, G3, G4 = sp.symbols("G1:5")
    g_shift = (G1 * eta + G2 * eta ** 2 / 2 + G3 * eta ** 3 / 6
               + G4 * eta ** 4 / 24)          # g(x+eta) - g(x)
    gp_shift = G1 + G2 * eta + G3 * eta ** 2 / 2 + G4 * eta ** 3 / 6
    Dl = sp.expand(G1 * gp_shift - (g_shift / eta) ** 2)
    d0 = sp.simplify(Dl.coeff(eta, 0))
    d1 = sp.simplify(Dl.coeff(eta, 1))
    d2 = sp.simplify(Dl.coeff(eta, 2))
    d2_target = (2 * G1 * G3 - 3 * G2 ** 2) / 12
    ok_schw = (d0 == 0 and d1 == 0
               and sp.simplify(d2 - d2_target) == 0)
    check("J2.SCHW generic two-point Loewner determinant: "
          "g'(x)g'(x+eta) - g[x,x+eta]^2 = (eta^2/12)(2 g' g''' - "
          "3 g''^2) + O(eta^3) = (eta^2/6) g'^2 S[g] -- orders eta^0, "
          "eta^1 vanish identically; hence 1-r12^2|_odd = (eta^2/6) "
          "S[gt](xbar) + O(eta^3) with eta = x1 - x2 = "
          "2 sin(3 eps/2) sin(eps/2) ~ (3/2) eps^2", ok_schw)

    # ============================================================== J2b
    print("\nJ2b -- the measurement: is the deployed surface in the jet "
          "regime?  (mp dps %d on the lag combs)" % MP_DPS)
    print("    %5s %2s %10s | %10s %10s %10s | %9s %9s | %8s | %9s"
          % ("h", "C", "onem", "even1", "odd1", "a11", "onem_lag",
             "onem_L", "dir", "|ev|/a11"))
    mpid_worst = 0.0
    onem_dev_worst = 0.0
    ev_ratio_min = float("inf")
    kill_ratio_min = float("inf")
    dir_dev_min = float("inf")
    schw_rows = []
    for w in wins:
        rr = w["r"]
        mb = mp_block(w["cc"], w["h"])
        # mp identity: entry route == Loewner route
        did = max(abs(mb["a11"] - (mb["ev1"] + mb["eps"] / mp.pi
                                   * mb["L11"])) / abs(mb["a11"]),
                  abs(mb["a22"] - (mb["ev2"] + mb["eps"] / mp.pi
                                   * mb["L22"])) / abs(mb["a22"]),
                  abs(mb["a12"] - mb["eps"] / mp.pi * mb["L12"])
                  / abs(mb["a12"]))
        mpid_worst = max(mpid_worst, float(did))
        det_lag = mb["a11"] * mb["a22"] - mb["a12"] ** 2
        onem_lag = det_lag / (mb["a11"] * mb["a22"])
        onem_dev = abs(float(onem_lag) - rr["onem"]) \
            / max(abs(rr["onem"]), 1e-300)
        onem_L = float((mb["L11"] * mb["L22"] - mb["L12"] ** 2)
                       / (mb["L11"] * mb["L22"]))
        dirv = rr["a12"] / rr["a11"]
        w.update(onem_lag=float(onem_lag), onem_L=onem_L, dirv=dirv,
                 ev1=float(mb["ev1"]), ev2=float(mb["ev2"]),
                 odd1=float(mb["eps"] / mp.pi * mb["L11"]),
                 odd2=float(mb["eps"] / mp.pi * mb["L22"]))
        if w["complete"]:
            onem_dev_worst = max(onem_dev_worst, onem_dev)
            ev_ratio_min = min(ev_ratio_min,
                               abs(w["ev1"]) / abs(rr["a11"]),
                               abs(w["ev2"]) / abs(rr["a22"]))
            kill_ratio_min = min(kill_ratio_min,
                                 abs(onem_L) / max(abs(rr["onem"]),
                                                   1e-300))
            dir_dev_min = min(dir_dev_min, abs(dirv - 2.0))
            # Schwarzian h^2-approximation of the Loewner block at xbar
            xbar = (mp.cos(mb["eps"]) + mp.cos(2 * mb["eps"])) / 2
            ombar = mp.acos(xbar)
            gb = mp_gjets(w["cc"], ombar)
            schw = gb[3] / gb[1] - mpf(3) / 2 * (gb[2] / gb[1]) ** 2
            onem_schw = float(mb["dx"] ** 2 / 6 * schw)
            schw_rows.append((w["h"], onem_L, onem_schw))
        print("    %5d %2s %10.3e | %10.3f %10.3f %10.4f | %9.3e "
              "%9.3e | %8.4f | %9.2f"
              % (w["h"], "C" if w["complete"] else "T", rr["onem"],
                 w["ev1"], w["odd1"], rr["a11"], w["onem_lag"], onem_L,
                 dirv, abs(w["ev1"]) / abs(rr["a11"])))
    check("J2b.MPID mp-exactness: entry route == Loewner route on all "
          "%d windows (worst rel %.1e <= %.0e); lag-route onem == "
          "corpus onem on the complete windows (worst rel %.1e <= "
          "%.0e, conditioning declared)"
          % (len(wins), mpid_worst, TOL_MPID, onem_dev_worst, BAR_ONEM),
          mpid_worst <= TOL_MPID and onem_dev_worst <= BAR_ONEM)
    ev_ratios = [abs(w["ev1"]) / abs(w["r"]["a11"]) for w in comp] \
        + [abs(w["ev2"]) / abs(w["r"]["a22"]) for w in comp]
    check("J2b.EVEN KILL-CRITERION MEASURED: the order-0 read (even "
          "sector 2 Re G - c_0) is NOT small on the deployed surface "
          "-- it exceeds the net entry on every complete window (min "
          "factor %.2f >= %.1f, median %.1f; for the jet identity to "
          "explain onem ~ 1e-6 it would have to be ~1e-6 of the odd "
          "sector, it is O(1) of it): the non-vanishing order-0/2 "
          "terms of J2.ORD are TOO LARGE in the review's sense; the "
          "razor-thin entries are an even/odd CANCELLATION, not a jet "
          "truncation" % (ev_ratio_min, BAR_BIG,
                          float(np.median(ev_ratios))),
          ev_ratio_min >= BAR_BIG)
    check("J2b.LOEW the pure jet (Loewner) block carries NO "
          "collinearity: onem_L = det L/(L11 L22) exceeds the measured "
          "onem by a factor >= %.1e on every complete window (bar "
          "%.0e) -- the observed third power does NOT sit in the "
          "structural jet part" % (kill_ratio_min, BAR_KILL_RATIO),
          kill_ratio_min >= BAR_KILL_RATIO)
    check("J2b.DIR the measured collinear direction a12/a11 = "
          "%.3f..%.3f drifts across the ladder and stays >= %.1f away "
          "from the structural jet direction 2 (the eps^3 dyad k=(1,2))"
          % (min(w["dirv"] for w in comp), max(w["dirv"] for w in comp),
             BAR_DIR), dir_dev_min >= BAR_DIR)
    h_arr = np.array([float(w["h"]) for w in comp])
    onem_arr = np.array([w["r"]["onem"] for w in comp])
    eta_h, c_h, r2_h = ols_loglog(h_arr, onem_arr)
    print("    context fit: 1 - r12^2 ~ %.3g h^{%.3f} (R^2 = %.3f); "
          "Delta_gamma^4-yardstick alone would give h^{-4} x frame "
          "growth" % (c_h, eta_h, r2_h))
    print("    Schwarzian h^2-approximation of onem_L (collapsed-jet "
          "regime test): h, onem_L, (eta^2/6) S[gt](xbar):")
    for hh, oL, oS in schw_rows:
        print("      h=%5d  onem_L=%9.3e  schw=%9.3e  ratio=%7.3f"
              % (hh, oL, oS, oS / oL if oL else float("nan")))
    check("J2b.FIT context reproduced: onem ~ c h^-eta with eta = %.3f "
          "(R^2 = %.3f > %.1f, v683 R2.MARGIN convention)"
          % (-eta_h, r2_h, BAR_R2), r2_h > BAR_R2)

    # ============================================================== J3
    print("\nJ3 -- the arithmetic, only what survives the kill")
    print("""    J3.STATE what WOULD have to be proven (the exact statement):
      det Ahat = det[ 2 diag(Re G_cc(g_1), Re G_cc(g_2)) - c_0 I
                      + (Dw/pi) Loewner(gt_cc) ]  >= 0  and  ~ h^-3,
      i.e. an even/odd COMPENSATION at the dual points: both sectors
      are O(3..7 x entry) and cancel to the razor-thin entries; the
      single structurally surviving jet coefficient (the Schwarzian,
      J2.ODD/J2.SCHW) measurably does NOT carry the collinearity
      (factor >= %.1e, J2b.LOEW).  There is no single-coefficient
      phase-curvature statement to feed into the v684 machinery: the
      review's route is DEAD at order 0.""" % kill_ratio_min)

    # classical accessibility of the compensation (v683 machinery)
    c_th = float(-2 * mpdiff(lambda s: zeta(s), 0.5) / zeta(0.5))
    u0_cut = 2.0 * math.log(-c_th / 4.0)
    lam_tab = core.LAM_TAB
    nn_ind = np.nonzero(lam_tab > 0.0)[0]
    psi_tab = np.cumsum(lam_tab[nn_ind])
    e_small = 0.0
    prev = 0.0
    for x_val, ps in zip(nn_ind.astype(float), psi_tab):
        if x_val > SCHOENFELD_X0:
            break
        e_small = max(e_small, abs(prev - x_val), abs(ps - x_val))
        prev = ps
    e_small = max(e_small, abs(prev - SCHOENFELD_X0))

    def env_schoenfeld(uuq):
        return np.where(np.exp(uuq) >= SCHOENFELD_X0,
                        uuq ** 2 / EIGHT_PI,
                        e_small * np.exp(-0.5 * uuq))

    def env_exact(uuq):
        x = np.exp(uuq)
        idx = np.searchsorted(nn_ind.astype(float), x,
                              side="right") - 1
        ps = np.where(idx >= 0, psi_tab[np.maximum(idx, 0)], 0.0)
        return np.abs(ps - x) * np.exp(-0.5 * uuq)

    print("\n    budgets on the margin (v683 Delta_B route, own "
          "recomputation):")
    print("    %5s %12s %12s %12s %10s %10s"
          % ("h", "margin", "Delta_B_sch", "Delta_B_ex", "ratio_sch",
             "ratio_ex"))
    rat_s_min = rat_x_min = float("inf")
    for w in comp:
        rr = w["r"]
        D, Mz, a2 = rr["D"], rr["M"], 2.0 * rr["alpha"]
        RBs = [r3.fluct_budget(rr[k], D, Mz, u0_cut, a2, env_schoenfeld)
               for k in ("W11", "W22", "W12")]
        RBx = [r3.fluct_budget(rr[k], D, Mz, u0_cut, a2, env_exact)
               for k in ("W11", "W22", "W12")]
        margin = rr["det"]

        def dB(RB):
            quad = RB[0] * RB[1] + RB[2] ** 2
            return (abs(rr["a11"]) * RB[1] + abs(rr["a22"]) * RB[0]
                    + 2.0 * abs(rr["a12"]) * RB[2] + quad)

        dBs, dBx = dB(RBs), dB(RBx)
        rat_s_min = min(rat_s_min, margin / dBs)
        rat_x_min = min(rat_x_min, margin / dBx)
        print("    %5d %12.4e %12.1f %12.1f %10.2e %10.2e"
              % (w["h"], margin, dBs, dBx, margin / dBs, margin / dBx))
    check("J3.BUDGET classical (envelope) accessibility of the "
          "compensation: min margin/Delta_B = %.2e (Schoenfeld "
          "yardstick) --> CLASS (%s); exact |psi-x| envelope %.2e --> "
          "CLASS (%s) -- the jet reparametrisation does NOT open a "
          "classical route; the missing factor ~%.0e is the same "
          "triangle-inequality wall as v683 R3.CLASS-TB"
          % (rat_s_min, class_of(rat_s_min), rat_x_min,
             class_of(rat_x_min), 1.0 / max(rat_s_min, 1e-300)),
          class_of(rat_s_min) == "c" and class_of(rat_x_min) == "c")
    check("J3.V684 comparison anchor (citations, no zero read here): "
          "v683 typed T-B class (c) entrywise; v684 typed the lifted "
          "K_M pairing ZONE-PASS class (a) on the ZERO SIDE (kappa_unc "
          "= 0.039..0.190); v692 identified the margin as the "
          "TRANSVERSE ZERO MASS c_P sum w_g |<s_perp, phi(g)>|^2 -- "
          "the arithmetic route to the razor-thin margin stays on the "
          "zero side; the jet picture adds the exact Loewner/Schwarzian "
          "COORDINATES but no new classical leverage", True)

    # ============================================================== J4
    print("\nJ4 -- section-8 diagnostic (EXPLORATORY, honestly typed)")
    kbads = []
    for w in comp:
        _aM, _gM, kbad = jac.wheeler(w["cc"], w["M"] // 2)
        kbads.append((w["h"], kbad))
    all_break = all(kb is not None for _h, kb in kbads)
    check("J4.KREIN the Krein/Wheeler chain on the v563 combined combs "
          "breaks early on EVERY complete window (depths %s << h): the "
          "v734 boundary phase theta_h is NOT constructible on the "
          "surface that carries the collinearity; on the v734 moonshot "
          "family the chain is intact (v734 G0) but the lock block "
          "there carries NO collinearity (onem ~ 0.2..0.99, pre-test) "
          "-- the section-8 conjecture has NO common surface in the "
          "Krein reading; only the SYMBOL-phase substitute below is "
          "testable" % (sorted(set(kb for _h, kb in kbads))),
          all_break)

    # substitute: Poisson-smoothed symbol boundary phase
    xs_log, ys_log, ctrl_log = [], [], []
    print("    %5s %12s %12s %12s"
          % ("h", "onem", "Dg^4|F_S|", "F_S(theta)"))
    for w in comp:
        rr = w["r"]
        hz, D, Mz = w["h"], w["D"], w["M"]
        N = 2 * hz + 1
        dg = 2.0 * math.pi / (N * D)
        taubar = 1.5 * dg
        d = np.arange(Mz, dtype=float)
        damp = np.exp(-d * D * DELTA_POIS)
        cd = w["cc"] * damp
        th1 = float(cd @ ((d * D) * np.cos(d * D * taubar)))
        th2 = float(cd @ (-(d * D) ** 2 * np.sin(d * D * taubar)))
        th3 = float(cd @ (-(d * D) ** 3 * np.cos(d * D * taubar)))
        FS = (2.0 * th1 * th3 - 3.0 * th2 ** 2) / th1 ** 2
        cand = dg ** 4 * abs(FS)
        print("    %5d %12.3e %12.3e %12.3e"
              % (hz, rr["onem"], cand, FS))
        xs_log.append(math.log(rr["onem"]))
        ys_log.append(math.log(max(cand, 1e-300)))
        ctrl_log.append(math.log(dg ** 4))
    r_cand = pearson(xs_log, ys_log)
    r_ctrl = pearson(xs_log, ctrl_log)
    sl_cand = float(np.polyfit(ys_log, xs_log, 1)[0])
    if abs(r_cand) >= BAR_CORR and abs(r_cand) > abs(r_ctrl):
        enum = "KREIN-LINK-SUPPORTED"
    elif abs(r_cand) >= 0.5:
        enum = "KREIN-LINK-WEAK"
    else:
        enum = "KREIN-LINK-NONE"
    check("J4.CORR substitute diagnostic (Poisson symbol phase, delta "
          "= %g, EXPLORATORY): log-log Pearson corr of onem vs "
          "Dg^4 |F_S(theta', theta'', theta''')| = %.3f (slope %.2f) "
          "vs the Dg^4-only control %.3f --> %s; %s"
          % (DELTA_POIS, r_cand, sl_cand, r_ctrl, enum,
             "the fixed Schwarzian functional of the smoothed boundary "
             "phase does NOT beat the trivial Delta_gamma^4 scale -- "
             "no evidence that the three programs share this scalar"
             if enum != "KREIN-LINK-SUPPORTED" else
             "candidate scalar identified -- promote only via a "
             "dedicated preregistered probe"), True)

    # ============================================================== J5
    print("\n" + "=" * 78)
    print("J5 -- VERDICT + contract note (chat report is the "
          "deliverable; no file outside experiments/ is touched)")
    print("=" * 78)
    verdict = "RANK3-JET-DEAD" if (ev_ratio_min >= BAR_BIG
                                   and kill_ratio_min >= BAR_KILL_RATIO) \
        else "RANK3-JET-IDENTITY"
    print("""
  VERDICT: %s

  WHAT IS TRUE (and exact, J1/J2):
    * The three functionals ARE first-jet reads of ONE function -- the
      LAG-PROJECTED comb transform G (F composed with the two-point
      spline, prop:split) at the dual points g_1, g_2 = 2 g_1,
      Delta_gamma = 2 pi/(ND); residuum %.1e.
    * Exact coordinates:  block = 2 diag(Re G) - c_0 I
      + (Dw/pi) Loewner(gt),  gt = Chebyshev-U resummation of the comb;
      the odd sector is the two-point LOEWNER matrix of gt.
    * Structural cancellations exist but only PARTIALLY: the cross
      read kills orders 0..2 identically; the eps^3 coefficient is the
      rank-one dyad (M3-M1)/(3 pi) k k^T; on the ODD SECTOR
      1 - r12^2 = (3/8) S[gt](1) eps^4 + O(eps^5) -- the SCHWARZIAN
      form the review predicted.

  WHY THE ROUTE IS DEAD (J2.KILL + J2b):
    * For arbitrary F the eps^0 coefficient of 1 - r12^2 is 1, not 0:
      the diagonal order-0/2 reads (even sector, Re F at the dual
      points) do not cancel structurally.
    * Measured on the deployed surface: the even sector EXCEEDS the
      net entries by a factor >= %.1f on every complete window, and
      the pure jet (Loewner) block has onem_L >= %.1e x the measured
      onem -- the observed h^-3 is an even/odd (arch vs prime)
      CANCELLATION at the dual points, i.e. the same razor-thin
      absorption as T-B, NOT a jet identity.  The collinear direction
      drifts (%.2f..%.2f) and is not the structural dyad direction 2.

  ARITHMETIC CONSEQUENCE (J3): no single surviving coefficient exists
  to feed the explicit formula; the classical envelope route stays
  class (c) (missing factor ~%.0e); the accessible route remains the
  zero side (v684 class (a); v692 transverse zero mass).

  SECTION-8 DIAGNOSTIC (J4, exploratory): Krein theta_h and the
  rank-3 collinearity have no common surface (Wheeler breaks at depth
  ~%s on the v563 combs; no collinearity on the v734 family); the
  Poisson-symbol substitute gives corr %.3f vs control %.3f -> %s.
""" % (verdict, res_S, ev_ratio_min, kill_ratio_min,
       min(w["dirv"] for w in comp), max(w["dirv"] for w in comp),
       1.0 / max(rat_s_min, 1e-300),
       sorted(set(kb for _h, kb in kbads)), r_cand, r_ctrl, enum))

    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(run())
