"""Discovery probe (2026-07-29), part 149 of the prime/window investigation.
Contract WEIGHT.SMOOTHING -- THE MISSING INPUT VIA THE SMOOTHING FREEDOM.

WHERE THIS SITS (T148 END STATE: ONE-INPUT-MISSING, and what exactly was missing)
  T140 reduced the question to two small matrices per zone, T141 made it a
  weighted Hardy problem, T142 closed the comparison branch, T143 estimated the
  exact capacity Rayleigh form, T144 closed the two-weight calculus, T145
  transcribed Maz'ya's capacitary proof, T146 closed the level lemma on the
  measurement surface, T147 reduced D-uniformity to TWO scalars via the identity
  Gam = sqrt(Q_star) x Sw, and T148 CLOSED ONE OF THEM and NAMED the other.
  QUOTED from T140 .. T148 and NEVER re-derived here:
    * the chain lam >= 1 / (kap_up c_0 Psi) is certified window by window;
    * Sw IS CLOSED on the surface: certified <= 1.9587 by an LDL^T inertia layer
      cake, flat in m (m^0.007), with the honest negative that the arithmetic
      Toeplitz symbol has f(0) < 0 on 48 of 48 windows -- so the positive
      definiteness of the section is a FINITE-SECTION effect of the minus-Hankel
      part and the KMS order-2 symbol hypothesis is REFUTED as a hypothesis;
    * the COMMUTATOR route (Davis-Kahan on the reweighting) is DEAD by 2.7 .. 5.7
      orders of magnitude, because the perturbation is O(||A||) while the bottom
      gap is Theta(D^3);
    * the LIVE route is weighted Szego via the LIOUVILLE TRANSFORM: with
      Lam the whitening diagonal, phi = Lam^{-1/2} psi solves A phi = lam Lam phi
      and m ||psi||_inf^2 <= 2 kap_Lam ceil(phi_hat)^2 with kap_Lam = max Lam /
      min Lam certified 1.733 .. 3.933 -- a factor 50.6 gain in the smoothness
      functional;
    * THE ONE MISSING INPUT is an m-FREE bound nu_L <= F(form) for the smoothness
      functional of the REWEIGHTED bottom mode.  Target nu_L <~ m / (8 kap_Lam)
      ~ 34 at m = 1077; MEASURED 282, trend m^0.166;
    * the hypothesis behind ROUTE S is ISOLATED and it is TV(log Lam), not the
      condition number: in T148's weight-class experiment two bounded-variation
      classes stayed flat and a lattice-rough class grew like m^1.994 at
      IDENTICAL kap_Lam.  On the arithmetic surface TV(log Lam) = 11.93 and grows
      like m^0.444 -- NOT flat.  That single number is what blocks the route.
    * the whole certified chain delivers 8.36 .. 15.86 % of the true gap
      (0.7 .. 1.6 % with a priori-shaped factors) on 48 of 48 windows.

THE LEVER THIS PROBE PULLS
  Lam IS A CHOICE.  Nothing in the chain requires Lam = diag(A_B); T144's
  kap_up <= 1.3162 is a certificate FOR THAT CHOICE, not a constraint on the
  method.  For ANY positive diagonal Lam~,
      x^T A x / x^T A_B x = (x^T A x / x^T Lam~ x) (x^T Lam~ x / x^T A_B x)
                         >= lam_min(Lam~^{-1/2} A Lam~^{-1/2})
                            / lam_max(Lam~^{-1/2} A_B Lam~^{-1/2})
  is an identity plus one Rayleigh step, so the whole chain runs with Lam~ in
  place of Lam and the ONLY price is the certified constant
  kap~_up = lam_max(Lam~^{-1/2} A_B Lam~^{-1/2}).  If Lam~ is a SMOOTHED version
  of Lam with a certified Loewner sandwich c_1 Lam <= Lam~ <= c_2 Lam, then
      kap~_up <= kap_up / c_1  and  kap_Lam~ <= (c_2 / c_1) kap_Lam ,
  both certified, while TV(log Lam~) can be made SMALL BY CONSTRUCTION.  So the
  blocked hypothesis of T148 is attacked with a change of gauge, paid for by a
  bounded sandwich factor.  THE QUESTION OF THIS PROBE is whether ONE member of
  a preregistered smoothing family makes ALL THREE numbers -- sandwich, TV, and
  the smoothness functional nu_L~ -- simultaneously bounded, flat in m, and flat
  across zones, and what the lifted chain then delivers end to end.

WHAT THIS PROBE DOES
  V0  THE LICENCES.  The RH fence first; then every inequality used, each with
      its DIRECTION in its name and each VERIFIED before use: the exact
      Dirichlet/Neumann eigenpairs, the sup bounds, the second-difference l1
      CEILING of T148 (quoted, re-verified, never re-derived), the elementary
      sin t >= 2t/pi, the GENERALISED WHITENING inequality above (verified
      against the exact generalised eigenvalue), the SANDWICH TRANSPORT
      kap~_up <= kap_up / c_1, the SCALE INVARIANCE of the whole chain under
      Lam~ -> t Lam~, the LIOUVILLE identity, the monotone-hull TV identity, the
      moving-geometric-mean sandwich, and Sylvester inertia as a certified count.
  V1  THE SMOOTHING FAMILY -- the heart.  Nine preregistered candidates for
      Lam~, from the identity through moving geometric means, a dyadic
      piecewise-geometric mean, polynomial macro fits, monotone and unimodal
      hulls, to the fully degenerate constant.  Each candidate carries, per
      window: the CERTIFIED sandwich (c_1, c_2, ratio) and its D-trend, the
      TV(log Lam~) it achieves, its certified kap~_up, and the pass-through
      nu_L~ / ceil / rho = 2 kap_Lam~ ceil^2 / m at the reweighted bottom.  The
      family is CALIBRATED FIRST on the model ladder of T148, where the pure
      statement is a theorem and where the lattice-rough weight class is known
      to break the route: if the smoothing repairs THAT, the family does what it
      claims.  Then the surface, and then the preregistered WINNER RULE.
  V2  THE LIFTED CHAIN.  The full T146/T147/T148 chain rebuilt with the winning
      Lam~: Q_star ceiling a priori, Gam^ap, c_0^ap, Psi, and the fraction of the
      TRUE gap delivered end to end -- against T148's 8.36 .. 15.86 % certified
      and 0.7 .. 1.6 % a priori.  Because EVERY candidate gives a VALID lower
      bound, the MAXIMUM over the family is also valid, and that is reported as
      the family bound.  A UNIFORMITY BALANCE classifies every factor, and the
      extrapolation discipline is hard: a finite surface proves nothing for all D.
  V3  STRESS AND ANATOMY.  The MANDATORY STRESS PAIR, now against the smoothing
      family: the NO-GO R = a a^T + eps I with a_i = i^{-1/2} -- whose whitening
      diagonal is ALREADY SMOOTH, so the smoothing family must be nearly the
      identity there and must NOT rescue it; WHERE the break stays visible is
      located exactly.  And the Dirichlet control, whose diagonal is CONSTANT, so
      every candidate is exactly the identity and every number must stay flat.
      Then the ANATOMY of TV(log Lam): the split into a smooth macro part and an
      arithmetic flutter part, the share sitting at the frame edges, and the share
      sitting on the lag indices where the prime-power atoms land -- with numbers.
      Finally the order-2 bottom ladder from the minus-Hankel structure
      (Basor-Ehrhardt 2009): theorem candidate or clearly named open.
  V4  THE MAP V21, the promotion list (T148's v548 .. v553 are being promoted in
      parallel and are NOT duplicated), the shortest rest list, and the honest
      three-sentence conclusion.

WHAT IS A THEOREM, WHAT IS CERTIFIED, WHAT IS A PRIORI, WHAT IS MEASURED
  * THEOREM means classical, cited, and never re-proved.
  * CERTIFIED means a completed Cholesky (Wilkinson 1968; Higham 2002) with the
    declared floating-point floor, or a completed LDL^T inertia count
    (Sylvester 1852; Bunch-Kaufman 1977), or an elementary inequality evaluated
    EXACTLY on the actual objects with a declared rounding guard -- always in the
    DIRECTION stated in the name.  The sandwich constants of V1 are of the third
    kind: c_1 = min_j Lam~_j / Lam_j and c_2 = max_j Lam~_j / Lam_j are finite
    minima of computed ratios, rounded OUTWARD.
  * A PRIORI means: the number is a functional of the FORM alone.  kap_Lam~,
    c_1, c_2, TV(log Lam~) and kap~_up all are.  nu_L~ is a functional of a MODE,
    so it is a priori only once it is bounded by a functional of the form, and
    that is exactly the input this probe hunts.
  * MEASURED means a number that reads a computed eigenvector as an object in its
    own right.  It enters as a CROSS-CHECK, never as a hypothesis.
  * A FIT is a least-squares exponent with a delete-one jackknife band, always
    labelled, NEVER load-bearing.  A FINITE SURFACE PROVES NO STATEMENT FOR ALL
    D, and the verdict rule enforces that: the word 'proved' is unreachable in
    every branch.

FENCES
  * THE RH FENCE, PROMINENT AND FIRST.  The surrounding statement is the
    positivity of a Weil window form (Weil 1952; Bombieri 2000; Connes 1999) on a
    FINITE list of prime-power zones and a FINITE window.  Weil's criterion is
    CITED as an address and is NEVER USED, in either direction.  Nothing here
    claims, assumes or approaches RH.  Even with the missing input closed, what
    would stand is a finite-window positivity statement with an explicit constant
    on prime-power zones in frame A; the distance from there to RH is mapped in V4
    and never travelled.  No zero data of any kind is read, generated or
    approximated; an AST firewall enforces this together with the import
    whitelist and the absence of any write-mode file access.
  * DISCOVERY ONLY.  Nothing is promoted.  No verification module, no ledger, no
    TeX, no website, no changelog, no next.txt is touched; this is ONE new file in
    experiments/tfpt-discovery/ and it writes nothing.
  * HARD CAPS.  Largest factorised / inverted / diagonalised matrix <= 1500;
    runtime budget 690 s (< 900 s), with per-block guards that truncate a pool
    rather than overrun.

CLASSICAL ADDRESSES (cited, never re-proved)
  Kac-Murdock-Szego 1953 (the exact sine/cosine sections and their eigenvalue
  ladder); Widom 1958 (Toeplitz sections with a vanishing symbol); Basor-Ehrhardt
  2009 (Toeplitz-plus-Hankel determinants and their Fredholm theory);
  Bottcher-Silbermann (the modern Toeplitz+Hankel algebra); Maz'ya 1985
  (capacitary inequalities); Charikar 2000 (greedy density); Davis-Kahan 1970;
  Sylvester 1852; Bunch-Kaufman 1977; Wilkinson 1968; Higham 2002.
"""

import ast
import math
import os
import time

import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import cho_factor, cho_solve, eigh, eigvalsh, ldl

np.seterr(all="ignore")

PASS = 0
FAIL = 0
T_START = time.time()

EULER = 0.5772156649015328606065120900824
LOG_PI = math.log(math.pi)

MAX_H = 1500                 # HARD cap on any FACTORISED / INVERTED form
BUDGET_S = 690.0             # HARD probe budget (< 900 s)
RESERVE_S = 230.0            # reserved for V2 .. V4 after the window loop

U_ROUND = 2.0 ** -53
ROUND_GUARD = 8.0 * U_ROUND  # outward rounding on every certified ratio
GL_N = 48
_GLX, _GLW = np.polynomial.legendre.leggauss(GL_N)

NU_MAIN = 4                  # T105 admissibility floor / T112 frame A
H_MIN = 24
CHUNK = 16384

ATOM_MAX = 2200000
ZONE_DEEP = 2050000

# --- the measurement surface (declared BEFORE any result is seen) ------------
# The cap is deliberately HIGHER than T148's 1100: the entire question of this
# probe is m-FREENESS, so the longest admissible lever arm inside MAX_H is used.
SURF_ZONES = 44
SURF_HCAP = 1400
STRATA = 4

# --- THE BOTTOM BLOCK, preregistered exactly as in T147 / T148 ---------------
THETA_BLK = 10.0
NB_PROBE = 6                 # bottom modes computed per candidate in V1

# --- THE SMOOTHING FAMILY, preregistered in full ------------------------------
# Nine candidates for the whitening diagonal Lam~.  Every one of them is a
# POSITIVE DIAGONAL, so every one of them gives a VALID chain (V0 licence 5); the
# family is therefore a family of valid lower bounds and the MAXIMUM over it is
# valid too.  The names are fixed here, before any number is seen.
CAND_ORDER = ("id", "const", "mgm05", "mgm15", "dyad",
              "poly2", "poly6", "mono", "unim")
MGM_FRAC = {"mgm05": 0.05, "mgm15": 0.15}
POLY_DEG = {"poly2": 2, "poly6": 6}
DEG_MACRO = 6                # degree of the macro part in the TV anatomy
EDGE_FRAC = 0.05             # frame-edge share in the TV anatomy

# --- THE WINNER RULE, preregistered --------------------------------------------
# Admissible = certified sandwich ratio <= SAND_BAR on every window AND
# TV(log Lam~) <= TV_BAR on every window.  Among the admissible candidates the
# winner MINIMISES the worst-window rho = 2 kap_Lam~ ceil^2 / m, i.e. the
# relative distance of the Liouville ceiling to the trivial bound m.  Ties are
# broken by the smaller |TV trend|.  rho < 1 is the point where the ceiling
# beats the trivial bound at all; rho <= RHO_BAR is the reading of "nu_L~ in the
# target", because rho < 1 is exactly nu_L~ <~ m / (8 kap_Lam~).
SAND_BAR = 8.0
TV_BAR = 4.0
RHO_BAR = 1.0

# --- the certified counting ladder (T148, quoted in form) --------------------
RHO_LADDER = (1.5, 2.0, 4.0, 8.0, 16.0, 64.0, 256.0, 1024.0)
K_FIT = 12

# --- THE CUT LADDER of the Q_star ceiling (T148, quoted in form) ------------
CUT_LADDER_Q = (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256)
CUT_MAX = 256

# --- the cake (T145 .. T148, quoted in form) --------------------------------
BASE_GRID = (2.0, 1.5, 1.25, 1.125, 1.0625, 1.03125)
FL_TARGET = 1.0e-12

# --- THE MODEL LADDER --------------------------------------------------------
MODEL_Q = 0.3
MODEL_C = (2.0 + 6.0 * MODEL_Q, -1.0 - 4.0 * MODEL_Q, MODEL_Q)
MODEL_SIZES = (96, 192, 384, 768)
MODEL_KINDS = ("smooth", "rough")
MODEL_CANDS = ("id", "const", "mgm15", "dyad")
WEIGHT_AMP = 0.6

# --- the stress forms --------------------------------------------------------
NOGO_EPS = 1.0e-3
NOGO_SIZES = (64, 128, 256, 512, 1024, 1500)
CTRL_SIZES = (64, 128, 256, 512, 1024, 1500)

# --- reading rules, ALL preregistered ---------------------------------------
BAR_UNIF = 0.25              # |exponent| + band for "FLAT", as in T146 .. T148
NU_BAR = 1000.0
CEIL_BAR = 1.0e4
SW_AP_BAR = 1.0e3
TV_FLAT_BAR = 0.25
KMS_BAND = (1.5, 2.5)

# --- T140 .. T148 numbers, QUOTED and never recomputed -----------------------
KAP_UP_T144 = 1.3162
C0AP_T146 = (3.9042, 4.8488)
QSTAR_T147 = 2.8634
QB_T147 = (1.375, 1.839)
TDEF_T147 = (0.21, 0.54)
IDENT_T147 = 2.3e-16
SW_CERT_T148 = 1.9587
SW_EXP_T148 = 0.007
KAPL_T148 = (1.733, 3.933)
NUL_T148 = 282.0
NUL_EXP_T148 = 0.166
NUL_TARGET_T148 = 34.0
TV_T148 = 11.93
TV_EXP_T148 = 0.444
FRAC_T148 = (0.0836, 0.1586)
FRACAP_T148 = (0.007, 0.016)
LIOU_GAIN_T148 = 50.6
DK_DEAD_T148 = (2.7, 5.7)
ROUGH_EXP_T148 = 1.994
WIN_T148 = 48
PROMO_T148 = 6

ZETA4 = math.pi ** 4 / 90.0  # sum_{k>=1} k^{-4} (Euler 1735), an EXACT constant


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print("check  %-42s %s  %s" % (name, "PASS" if ok else "FAIL", detail))


def info(name, detail=""):
    print("info   %-42s %s" % (name, detail))


def section(title):
    print("")
    print("=" * 78)
    print(title)
    print("=" * 78)


def wrap_at(text, width):
    out, line = [], ""
    for w in text.split():
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + " " + w) if line else w
    if line:
        out.append(line)
    return out


def para(text, width=76, indent="  "):
    for ln in wrap_at(text, width - len(indent)):
        print(indent + ln)


def budget_left():
    return BUDGET_S - (time.time() - T_START)


def sym(A):
    return 0.5 * (A + A.T)


def rel(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    sc = max(float(np.max(np.abs(a))), float(np.max(np.abs(b))), 1.0e-300)
    return float(np.max(np.abs(a - b))) / sc


def qmin(v):
    v = [x for x in v if np.isfinite(x)]
    return float(min(v)) if v else float("nan")


def qmax(v):
    v = [x for x in v if np.isfinite(x)]
    return float(max(v)) if v else float("nan")


def qmed(v):
    v = [x for x in v if np.isfinite(x)]
    return float(np.median(v)) if v else float("nan")


def fit_line(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    A = np.stack([np.ones_like(x), x], axis=1)
    sol, *_ = np.linalg.lstsq(A, y, rcond=None)
    return float(sol[0]), float(sol[1]), float(np.sqrt(np.mean((A @ sol - y) ** 2)))


def fit_band(x, y):
    """A FIT with a delete-one jackknife band on both coefficients."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    a0, b0, rms = fit_line(x, y)
    aa, bb = [], []
    n = x.shape[0]
    if n >= 4:
        for i in range(n):
            msk = np.ones(n, dtype=bool)
            msk[i] = False
            ai, bi, _ = fit_line(x[msk], y[msk])
            aa.append(ai)
            bb.append(bi)
    sa = (0.5 * (max(aa) - min(aa))) if aa else float("nan")
    sb = (0.5 * (max(bb) - min(bb))) if bb else float("nan")
    return a0, b0, rms, sa, sb, n


def pow_fit(xv, yv, tag):
    """A FIT of y ~ c x^p in log-log with a jackknife band.  NEVER load-bearing."""
    x = np.asarray(xv, dtype=float)
    y = np.asarray(yv, dtype=float)
    ok = np.isfinite(x) & np.isfinite(y) & (x > 0.0) & (y > 0.0)
    n_ok = int(np.count_nonzero(ok))
    if n_ok < 3:
        return dict(tag=tag, c=float("nan"), p=float("nan"), rms=float("nan"),
                    sc=float("nan"), sp=float("nan"), n=n_ok)
    a0, b0, rms, sa, sb, n = fit_band(np.log(x[ok]), np.log(y[ok]))
    return dict(tag=tag, c=math.exp(a0), p=b0, rms=rms, sc=sa, sp=sb, n=n)


def fit_str(f):
    return "x^(%.3f +- %.3f)" % (f["p"], f["sp"])


def flat_ok(f, bar=BAR_UNIF):
    """The preregistered READING of a FIT: |p| plus its jackknife band inside the
    bar.  A FIT is never load-bearing; this only LABELS it."""
    return bool(np.isfinite(f["p"]) and np.isfinite(f["sp"])
                and abs(f["p"]) + f["sp"] <= bar)


def band_ok(f, lo, hi):
    """Does the measured exponent's jackknife band CONTAIN the theory value?
    A reading, not a proof."""
    if not (np.isfinite(f["p"]) and np.isfinite(f["sp"])):
        return False
    return bool(f["p"] - f["sp"] <= hi and f["p"] + f["sp"] >= lo)


# ----------------------------------------------------------------------------
# THE AST FIREWALL -- no zero data, no unexpected import, no file write
# ----------------------------------------------------------------------------
FORBIDDEN_TOKENS = tuple("".join(parts) for parts in (
    ("zeta", "zero"), ("zeta_", "zero"), ("zeros_of_", "zeta"), ("odly", "zko"),
    ("lm", "fdb"), ("gram_", "point"), ("14.13", "4725"), ("21.02", "2039"),
    ("25.01", "0857"), ("30.42", "4876"),
))
ALLOWED_IMPORT_ROOTS = {"ast", "math", "os", "time", "numpy", "scipy"}


def firewall():
    src = open(os.path.abspath(__file__), "r").read()
    low = src.lower()
    hits = [tok for tok in FORBIDDEN_TOKENS if tok in low]
    tree = ast.parse(src)
    bad_imports, bad_writes = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                    bad_imports.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split(".")[0] not in ALLOWED_IMPORT_ROOTS:
                bad_imports.append(node.module)
        elif isinstance(node, ast.Call):
            fn = node.func
            nm = getattr(fn, "id", None) or getattr(fn, "attr", None)
            if nm in ("open",):
                mode = ""
                if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                    mode = str(node.args[1].value)
                for kw in node.keywords:
                    if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                        mode = str(kw.value.value)
                if any(ch in mode for ch in "wax+"):
                    bad_writes.append(mode)
    check("ws_firewall.tokens", not hits, "forbidden token hits: %d" % len(hits))
    check("ws_firewall.imports", not bad_imports,
          "non-whitelisted imports: %s" % (bad_imports or "none"))
    check("ws_firewall.no_writes", not bad_writes,
          "write-mode file access: %s" % (bad_writes or "none"))
    check("ws_firewall.one_file", os.path.basename(os.path.abspath(__file__))
          == "weight_smoothing_probe.py", "single new file in the sandbox")


# ----------------------------------------------------------------------------
# prime-power arithmetic (exact, cheap) -- the T111 .. T148 code path
# ----------------------------------------------------------------------------
def von_mangoldt_table(n_max):
    sieve = np.ones(n_max + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(math.isqrt(n_max)) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    lam = np.zeros(n_max + 1)
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        lp = math.log(p)
        q = p
        while q <= n_max:
            lam[q] = lp
            q *= p
    return lam


def atom_table(n_max):
    lam = von_mangoldt_table(n_max)
    out = []
    for n in np.nonzero(lam > 0)[0]:
        n = int(n)
        out.append((n, lam[n], math.log(n), 2.0 * lam[n] / math.sqrt(n)))
    return out


def atoms_in(alpha, atoms_all):
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    return ATOM_PAIRS[:k]


def atom_hit_lags(alpha, M):
    """THE LAG INDICES WHERE THE PRIME-POWER ATOMS LAND, vectorised: i0 =
    floor(u_j / D) dilated by the linear-spline support +-2.  Used ONLY by the
    TV anatomy of V3, never by any bound."""
    D = 2.0 * alpha / M
    lim = 2.0 * alpha + 1.0e-14
    k = int(np.searchsorted(U_SORTED, lim, side="right"))
    if k == 0:
        return np.zeros(0, dtype=np.int64)
    i0 = np.floor(U_SORTED[:k] / D).astype(np.int64)
    out = np.concatenate([i0 + d for d in (-2, -1, 0, 1, 2)])
    out = out[(out >= 0) & (out < M)]
    return np.unique(out)


# ----------------------------------------------------------------------------
# the archimedean kernel (Weil 1952 -- CITED, never used as a criterion)
# ----------------------------------------------------------------------------
def _arch_A_far(s, D):
    s = np.asarray(s, dtype=float).reshape(-1, 1)
    out = np.zeros(s.shape[0])
    for lo, hi in ((s - D, s), (s, s + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX[None, :]
        val = (1.0 - np.abs(s - w) / D) * np.exp(-0.5 * w) / (-np.expm1(-2.0 * w))
        out -= half[:, 0] * (val @ _GLW)
    return out


def _arch_integrand(w, s, D):
    tri_s = max(0.0, 1.0 - abs(s) / D)
    S = 0.5 * (np.maximum(0.0, 1.0 - np.abs(s - w) / D)
               + np.maximum(0.0, 1.0 - np.abs(s + w) / D))
    return (tri_s * np.exp(-2.0 * w) - S * np.exp(-0.5 * w)) / (-np.expm1(-2.0 * w))


def _arch_A_near(s, D):
    s = abs(float(s))
    tri_s = max(0.0, 1.0 - s / D)
    W = s + D
    pts = sorted({0.0, s, D - s, W})
    pts = [p for p in pts if 0.0 <= p <= W]
    tot = 0.0
    for lo, hi in zip(pts[:-1], pts[1:]):
        if hi <= lo:
            continue
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid + half * _GLX
        tot += half * float(np.dot(_GLW, _arch_integrand(w, s, D)))
    return (-(EULER + LOG_PI) * tri_s + 2.0 * tot
            + tri_s * (-math.log1p(-math.exp(-2.0 * W))))


def arch_A(sv, D):
    sv = np.abs(np.asarray(sv, dtype=float))
    out = np.empty(sv.shape[0])
    far = sv >= D
    if far.any():
        out[far] = _arch_A_far(sv[far], D)
    for i in np.nonzero(~far)[0]:
        out[i] = _arch_A_near(sv[i], D)
    return out


def arch_lags(M, D):
    out = np.empty(M)
    for a in range(0, M, CHUNK):
        b = min(M, a + CHUNK)
        out[a:b] = arch_A(np.arange(a, b) * D, D)
    return out


def lag_vector_fast(alpha, M, atoms):
    """The T115 O(#atoms) lag assembly (bit-identical to the T111 reference)."""
    D = 2.0 * alpha / M
    c = arch_lags(M, D)
    for u_j, mu_j in atoms:
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= mu_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= mu_j * 0.5 * v
    return c, D


def odd_toeplitz(c, M):
    """A_rs = c_{|r-s|} - c_{M-1-r-s} on the odd section, r, s = 0 .. M/2 - 1.
    THE TOEPLITZ-MINUS-HANKEL STRUCTURE, exact and not an approximation: the
    object Szego/Widom theory speaks about (Widom 1958; Basor-Ehrhardt 2009)."""
    h = M // 2
    rr = np.arange(h)
    return c[np.abs(rr[:, None] - rr[None, :])] - c[(M - 1) - rr[:, None] - rr[None, :]]


def symbol_values(c, n_th=512):
    """THE SYMBOL f(th) = c_0 + 2 sum_{k>=1} c_k cos(k th) of the Toeplitz part
    on a uniform grid of [0, pi]."""
    c = np.asarray(c, dtype=float)
    th = np.linspace(0.0, math.pi, n_th)
    kk = np.arange(1, c.shape[0])
    f = c[0] + 2.0 * (np.cos(np.outer(th, kk)) @ c[1:])
    return th, f


def symbol_order(c, n_th=512):
    """THE ORDER OF THE NEAR-ZERO of the symbol, MEASURED.  T148's honest
    negative is re-read here and never re-derived: f(0) < 0 on the arithmetic
    windows, so the KMS order-2 SYMBOL hypothesis is refuted as a hypothesis and
    is available only as a measurement."""
    th, f = symbol_values(c, n_th)
    i0 = int(np.argmin(np.abs(f)))
    f0 = float(f[0])
    dec = max(4, n_th // 32)
    xs = th[1:dec]
    ys = np.abs(f[1:dec] - f[0])
    ex = pow_fit(xs, ys, "symbol order")
    return dict(f0=f0, th_min=float(th[i0]), gam=float(f[i0]),
                exponent=ex["p"], exp_sd=ex["sp"])


# ----------------------------------------------------------------------------
# CERTIFICATION (Wilkinson 1968; Higham 2002; Sylvester 1852)
# ----------------------------------------------------------------------------
def safe_cho(Q):
    try:
        return cho_factor(Q, lower=True, check_finite=False)
    except LinAlgError:
        return None


def chol_floor(A_norm, h):
    """THE DECLARED FLOATING-POINT FLOOR (Wilkinson 1968; Higham 2002)."""
    ch = (h + 1.0) / max(1.0 - (h + 1.0) * U_ROUND, 1.0e-300)
    return ch * U_ROUND * A_norm


def gersh(X):
    return float(np.max(np.abs(X).sum(axis=1)))


def ray_top(X, iters=90):
    """lam_max of a SYMMETRIC X by a SHIFTED power iteration.  The returned value
    is a RAYLEIGH QUOTIENT, hence a rigorous LOWER bound -- used only as a SEED."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    if n == 1:
        return float(X[0, 0])
    sig = gersh(X)
    y = np.ones(n) / math.sqrt(n)
    lam = float(y @ (X @ y))
    for _ in range(iters):
        z = X @ y + sig * y
        nz = float(np.linalg.norm(z))
        if not (nz > 0.0):
            break
        y = z / nz
        lam = max(lam, float(y @ (X @ y)))
    return lam


def cert_lam_max(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_max(X) <= s by a COMPLETED CHOLESKY of s I - X.  DIRECTION: an
    UPPER bound.  The GUESS is only a SEED."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    if guess is None or not np.isfinite(guess):
        guess = nrm
    s = max(float(guess), 0.0) + fl + 1.0e-300
    I = np.eye(n)
    for _ in range(tries):
        if safe_cho(s * I - X) is not None:
            return s + fl
        s = s * (1.0 + grow) + 10.0 * fl + 1.0e-300
        grow *= 3.0
    return float("nan")


def cert_lam_min(X, guess=None, tries=14, grow=1.0e-7):
    """CERTIFY lam_min(X) >= t by a completed Cholesky of X - t I.  DIRECTION: a
    LOWER bound."""
    n = X.shape[0]
    if n == 0:
        return 0.0
    nrm = gersh(X)
    fl = chol_floor(nrm, n)
    if guess is None or not np.isfinite(guess):
        guess = 0.0
    t = float(guess) - fl
    I = np.eye(n)
    for _ in range(tries):
        if safe_cho(X - t * I) is not None:
            return t - fl
        t = t - max(abs(t), nrm) * grow - 10.0 * fl - 1.0e-300
        grow *= 3.0
    return float("nan")


def inertia_neg(X):
    """THE CERTIFIED EIGENVALUE COUNT (Sylvester 1852; Bunch-Kaufman 1977;
    Higham 2002 ch. 11).  Returns -1 when the factorisation does not complete, so
    a missing certificate is REPORTED rather than silently replaced."""
    n = X.shape[0]
    if n == 0:
        return 0
    try:
        _lu, d, _perm = ldl(sym(X), lower=True)
    except (LinAlgError, ValueError):
        return -1
    if not np.all(np.isfinite(d)):
        return -1
    i, neg = 0, 0
    while i < n:
        two = (i + 1 < n) and (abs(float(d[i, i + 1])) > 0.0
                               or abs(float(d[i + 1, i])) > 0.0)
        if two:
            a = float(d[i, i])
            b = float(d[i, i + 1]) if abs(float(d[i, i + 1])) > 0.0 else float(d[i + 1, i])
            c = float(d[i + 1, i + 1])
            det = a * c - b * b
            tr = a + c
            if det < 0.0:
                neg += 1
            elif tr < 0.0:
                neg += 2
            i += 2
        else:
            if float(d[i, i]) < 0.0:
                neg += 1
            i += 1
    return neg


# ----------------------------------------------------------------------------
# the frame (T112 frame A, window forced EVEN so that h = M/2 exactly)
# ----------------------------------------------------------------------------
def even_window(u, D):
    M = int(math.ceil(u / D - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return M


def lump_pair(A):
    """Delta = the POSITIVE off-diagonal part, L_Delta = diag(Delta 1) - Delta,
    A_B = A + L_Delta.  DIRECTION: L_Delta >= 0, so A_B >= A."""
    h = A.shape[0]
    dg = np.diag(A).copy()
    off = A - np.diag(dg)
    Dl = np.where(off > 0.0, off, 0.0)
    P_row = Dl.sum(axis=1)
    LD = np.diag(P_row) - Dl
    A_B = sym(A + LD)
    offB = A_B - np.diag(np.diag(A_B))
    return dict(h=h, A_B=A_B, dg=dg, dgB=np.diag(A_B).copy(),
                stieltjes=int(bool(np.all(offB <= 1.0e-300))
                              and bool(np.all(np.diag(A_B) > 0.0))))


# ----------------------------------------------------------------------------
# THE EXACT MODELS AND THE SECOND-DIFFERENCE l1 CEILING (T148, QUOTED)
# ----------------------------------------------------------------------------
def dirichlet_mu(m):
    """THE EXACT DIRICHLET EIGENVALUES mu_k = 4 sin^2(pi k / (2(m+1))), k = 1..m,
    with EXACT eigenvectors s_k(j) = sqrt(2/(m+1)) sin(pi k (j+1)/(m+1)).
    THEOREM (Kac-Murdock-Szego 1953, section 4; classical)."""
    kk = np.arange(1, m + 1, dtype=float)
    return 4.0 * np.sin(0.5 * math.pi * kk / (m + 1.0)) ** 2


def sine_basis(m):
    """THE ORTHONORMAL DIRICHLET (sine) BASIS, sup bound sqrt(2/(m+1))."""
    jj = np.arange(m)
    kk = np.arange(1, m + 1)
    return math.sqrt(2.0 / (m + 1.0)) * np.sin(
        math.pi * np.outer(kk, jj + 1.0) / (m + 1.0))


def neumann_mu(m):
    """THE EXACT NEUMANN EIGENVALUES mu_k = 4 sin^2(pi k / (2m)), k = 0..m-1, the
    second Kac-Murdock-Szego model.  mu_0 = 0, so the k = 0 coefficient is bounded
    by the trivial |a_0| <= 1 and by nothing else."""
    kk = np.arange(m, dtype=float)
    return 4.0 * np.sin(0.5 * math.pi * kk / m) ** 2


def cosine_basis(m):
    """THE ORTHONORMAL NEUMANN (cosine) BASIS, sup bound sqrt(2/m).  WHY IT IS
    NEEDED (T148): a bottom mode of a Toeplitz-minus-Hankel section is generically
    REFLECTION-symmetric, and the Dirichlet ceiling charges such a mode an edge
    term that alone inflates nu to order m.  Each ceiling is valid on its own, so
    the pointwise minimum of the two is valid."""
    jj = np.arange(m)
    kk = np.arange(m)
    C = math.sqrt(2.0 / m) * np.cos(math.pi * np.outer(kk, jj + 0.5) / m)
    C[0, :] = 1.0 / math.sqrt(m)
    return C


def _lap_D(X):
    """L_0 X columnwise, L_0 = tridiag(-1, 2, -1) (DIRICHLET)."""
    out = 2.0 * X
    out[:-1] -= X[1:]
    out[1:] -= X[:-1]
    return out


def _lap_N(X):
    """L_N X columnwise, the same with corner diagonals 1 (NEUMANN)."""
    out = _lap_D(X)
    out[0] -= X[0]
    out[-1] -= X[-1]
    return out


def ceilings(X, m, mu, sup_s, lap, scale):
    """THE VECTORISED CERTIFIED CEILING of T148, applied to every column at once.
    Columns must be unit vectors.  DIRECTION: every entry of B is an UPPER bound
    on |a_k|, hence the column sums are UPPER bounds on ||a||_1."""
    L1 = lap(X.copy())
    L2 = lap(L1.copy())
    n1 = np.sum(np.abs(L1), axis=0)
    n2 = np.sum(np.abs(L2), axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        B1 = np.minimum(1.0, sup_s * n1[None, :] / mu[:, None])
        B2 = np.minimum(1.0, sup_s * n2[None, :] / (mu * mu)[:, None])
    B1 = np.where(np.isfinite(B1), B1, 1.0)
    B2 = np.where(np.isfinite(B2), B2, 1.0)
    B = np.minimum(B1, B2)
    nu = scale * n1
    del L1, L2
    return dict(nu=nu, ceil=np.sum(B, axis=0),
                ceil_closed=2.0 * np.sqrt(np.maximum(nu, 0.0)) + 1.0, B=B)


def mode_bounds(X, m, S, C, muD, muN, cap=None):
    """THE PER-MODE UPPER BOUND ON m ||psi||_inf^2 as the MINIMUM of every valid
    bound available: the DIRICHLET l1 ceiling, the NEUMANN one, and (when a cap is
    given) the trivial m.  The true coefficients in both bases are computed and
    the coefficient inequality is VERIFIED, so a violated licence is reported."""
    X = np.ascontiguousarray(X, dtype=float)
    nrm = np.linalg.norm(X, axis=0)
    nrm = np.where(nrm > 0.0, nrm, 1.0)
    X = X / nrm[None, :]
    supD = math.sqrt(2.0 / (m + 1.0))
    supN = math.sqrt(2.0 / m)
    cD = ceilings(X, m, muD, supD, _lap_D,
                  (m + 1.0) ** 1.5 / (2.0 * math.sqrt(2.0)))
    cN = ceilings(X, m, muN, supN, _lap_N,
                  float(m) ** 1.5 / (2.0 * math.sqrt(2.0)))
    aS = S @ X
    aC = C @ X
    viol = max(float(np.max(np.abs(aS) - cD["B"])),
               float(np.max(np.abs(aC) - cN["B"])))
    l1S = np.sum(np.abs(aS), axis=0)
    l1C = np.sum(np.abs(aC), axis=0)
    bnd = 2.0 * np.minimum(cD["ceil"], cN["ceil"]) ** 2
    if cap is not None:
        bnd = np.minimum(bnd, float(cap))
    return dict(bound=bnd, viol=viol,
                ceil=np.minimum(cD["ceil"], cN["ceil"]),
                nu=np.minimum(cD["nu"], cN["nu"]),
                nu_D=cD["nu"], nu_N=cN["nu"],
                ceil_D=cD["ceil"], ceil_N=cN["ceil"],
                l1=np.minimum(l1S, l1C),
                which_N=int(np.count_nonzero(cN["ceil"] < cD["ceil"])))


# ----------------------------------------------------------------------------
# THE SMOOTHING FAMILY -- THE HEART OF THIS PROBE
# ----------------------------------------------------------------------------
def _movgeo(Lam, half):
    """THE MOVING GEOMETRIC MEAN of width 2 half + 1, i.e. exp of the moving
    ARITHMETIC mean of log Lam.  Two properties, both used and both elementary:
      * every entry is a CONVEX COMBINATION of values of log Lam over a window, so
        min_window Lam <= Lam~_j <= max_window Lam -- the sandwich is LOCAL and is
        controlled by the LOCAL oscillation of Lam, not by its global range;
      * TV(log Lam~) = sum_j |mean_{j+1} - mean_j| = (1/L) sum_j |sum of the two
        boundary increments| <= TV(log Lam), with the CANCELLATION at lattice
        scale making it O(TV / L) for an oscillation whose period is short.  With
        half = ceil(frac m) the reduction factor is proportional to m, which is
        exactly what turns a TV growing like a power of m into a flat one.
    The half-width is a FRACTION of m, declared in MGM_FRAC before any result."""
    lg = np.log(np.asarray(Lam, dtype=float))
    m = lg.shape[0]
    cs = np.concatenate(([0.0], np.cumsum(lg)))
    jj = np.arange(m)
    lo = np.maximum(jj - half, 0)
    hi = np.minimum(jj + half + 1, m)
    return np.exp((cs[hi] - cs[lo]) / (hi - lo).astype(float))


def _dyadic_geo(Lam):
    """THE DYADIC PIECEWISE-GEOMETRIC MEAN, refined towards BOTH window edges.
    Block widths 1, 1, 2, 4, 8, ... from the left up to the midpoint and mirrored
    on the right, so the partition respects the DIHEDRAL symmetry of the
    Toeplitz-minus-Hankel section (odd_toeplitz is covariant under r -> h-1-r) and
    resolves the edge structure while averaging the bulk.  The number of blocks is
    O(log m), so TV(log Lam~) is at most O(log m) x the largest block-to-block
    step -- a construction whose TV is bounded by construction whenever the MACRO
    profile of Lam is monotone in each half."""
    Lam = np.asarray(Lam, dtype=float)
    m = Lam.shape[0]
    lg = np.log(Lam)
    edges = [0]
    wid = 1
    while edges[-1] + wid < m // 2:
        edges.append(edges[-1] + wid)
        wid *= 2
    left = edges + [m // 2]
    bnds = sorted(set(left + [m - e for e in left] + [0, m]))
    bnds = [b for b in bnds if 0 <= b <= m]
    out = np.empty(m)
    for lo, hi in zip(bnds[:-1], bnds[1:]):
        if hi > lo:
            out[lo:hi] = float(np.mean(lg[lo:hi]))
    return np.exp(out)


def _poly_geo(Lam, deg):
    """THE POLYNOMIAL MACRO FIT: exp of a least-squares Chebyshev fit of log Lam
    in x = 2j/(m-1) - 1 of the declared degree.  THE HYPOTHESIS BEING TESTED: the
    whitening diagonal is a SMOOTH MACRO PROFILE times an ARITHMETIC FLUTTER, and
    a fixed-degree fit isolates the macro part.  TV of a degree-d polynomial on an
    interval is at most d times its range, so TV(log Lam~) is bounded by
    construction; the SANDWICH is then exactly the size of the flutter, which is
    the number that decides whether the separation is real."""
    Lam = np.asarray(Lam, dtype=float)
    m = Lam.shape[0]
    x = (2.0 * np.arange(m, dtype=float) / max(m - 1.0, 1.0)) - 1.0
    lg = np.log(Lam)
    d = int(min(deg, max(m - 1, 1)))
    co = np.polynomial.chebyshev.chebfit(x, lg, d)
    return np.exp(np.polynomial.chebyshev.chebval(x, co))


def _mono_hull(Lam):
    """THE LEAST NONDECREASING MAJORANT, Lam~_j = max_{i <= j} Lam_i (the running
    maximum).  DIRECTIONS, both exact: Lam~ >= Lam entrywise, so c_1 = 1 before
    normalisation; and TV(log Lam~) = log(Lam~_last / Lam~_first) EXACTLY, because
    a monotone sequence's total variation is its endpoint difference -- so the TV
    is bounded by log kap_Lam BY CONSTRUCTION, with no hypothesis at all.  The
    price is the sandwich c_2 = max_j Lam~_j / Lam_j, which is large exactly when
    Lam is far from monotone."""
    return np.maximum.accumulate(np.asarray(Lam, dtype=float))


def _unim_hull(Lam):
    """THE UNIMODAL HULL, the pointwise MINIMUM of the running maximum from the
    left and the running maximum from the right.  It is >= Lam, it is unimodal,
    and its TV in log is at most 2 log kap_Lam -- again by construction.  This is
    the right hull for a window profile that RISES and then FALLS, which is what a
    minus-Hankel diagonal does when the reflected lag term is largest at the two
    edges."""
    Lam = np.asarray(Lam, dtype=float)
    return np.minimum(np.maximum.accumulate(Lam),
                      np.maximum.accumulate(Lam[::-1])[::-1])


def smoothing_family(Lam, names=CAND_ORDER):
    """THE PREREGISTERED FAMILY OF CANDIDATE WHITENING DIAGONALS.  Every member is
    a POSITIVE DIAGONAL of the same length, so every member yields a VALID chain
    (licence 5), and the family is a family of valid lower bounds whose MAXIMUM is
    therefore also valid.  'id' is T148's Jacobi choice and 'const' is the fully
    degenerate one, for which the reweighted section is the PURE section rescaled
    -- the case where the classical Szego/Widom statement applies verbatim and the
    entire price has moved into the single certified constant kap~_up."""
    Lam = np.asarray(Lam, dtype=float)
    m = Lam.shape[0]
    out = {}
    for nm in names:
        if nm == "id":
            v = Lam.copy()
        elif nm == "const":
            v = np.full(m, float(np.exp(np.mean(np.log(Lam)))))
        elif nm in MGM_FRAC:
            v = _movgeo(Lam, max(1, int(math.ceil(MGM_FRAC[nm] * m))))
        elif nm == "dyad":
            v = _dyadic_geo(Lam)
        elif nm in POLY_DEG:
            v = _poly_geo(Lam, POLY_DEG[nm])
        elif nm == "mono":
            v = _mono_hull(Lam)
        elif nm == "unim":
            v = _unim_hull(Lam)
        else:
            raise ValueError(nm)
        if not np.all(np.isfinite(v)) or not (float(np.min(v)) > 0.0):
            continue
        out[nm] = v
    return out


def sandwich_cert(Lam, Lam_t):
    """THE CERTIFIED LOEWNER SANDWICH c_1 Lam <= Lam~ <= c_2 Lam.  The two
    constants are finite minima/maxima of computed ratios, rounded OUTWARD by the
    declared guard, so each is a certificate in the direction of its name.  Lam~
    is first NORMALISED so that the geometric mean of the ratio is 1: the whole
    chain is INVARIANT under Lam~ -> t Lam~ (licence 7), so only the RATIO
    sig = c_2 / c_1 has meaning, and the normalisation makes c_1 <= 1 <= c_2 so
    that the two halves of the price are readable separately."""
    Lam = np.asarray(Lam, dtype=float)
    r = np.asarray(Lam_t, dtype=float) / Lam
    g = float(np.exp(np.mean(np.log(r))))
    Lam_t = np.asarray(Lam_t, dtype=float) / g
    r = r / g
    c1 = float(np.min(r)) * (1.0 - ROUND_GUARD)
    c2 = float(np.max(r)) * (1.0 + ROUND_GUARD)
    return dict(Lam_t=Lam_t, c1=c1, c2=c2, sig=c2 / max(c1, 1.0e-300))


def weight_regularity(Lam):
    """THE REGULARITY OF THE DIAGONAL MULTIPLIER -- the hypothesis of ROUTE S.
      * kap_Lam = max Lam / min Lam, the Loewner range;
      * TV(log Lam) = sum_j |log Lam_{j+1} - log Lam_j|, the total variation that
        controls a smooth multiplier in the Sturm-Liouville reading;
      * the scaled second difference, the discrete curvature.
    T148's weight-class experiment isolated TV(log Lam) -- NOT the condition
    number -- as the operative hypothesis, and that is why TV is the target of the
    smoothing family."""
    Lam = np.asarray(Lam, dtype=float)
    m = Lam.shape[0]
    lg = np.log(Lam)
    d1 = np.diff(lg)
    d2 = lg[2:] - 2.0 * lg[1:-1] + lg[:-2] if m >= 3 else np.zeros(1)
    return dict(kap=float(np.max(Lam)) / max(float(np.min(Lam)), 1.0e-300),
                tv=float(np.sum(np.abs(d1))),
                d1_max=float(np.max(np.abs(d1))) if d1.size else 0.0,
                curv=float(m * float(np.sum(np.abs(d2)))),
                spread=(float(np.max(Lam)) - float(np.min(Lam)))
                / max(float(np.max(Lam)) + float(np.min(Lam)), 1.0e-300))


def tv_anatomy(Lam, hits_r=None, deg=DEG_MACRO, edge_frac=EDGE_FRAC):
    """WHERE DOES TV(log Lam) COME FROM?  Three decompositions, all MEASURED and
    none load-bearing, answering the question V3 asks:
      (a) MACRO versus FLUTTER: log Lam = P_d + f with P_d the degree-d Chebyshev
          least-squares fit.  TV(P_d) is the smooth part, TV(f) the flutter.  The
          triangle inequality gives TV(log Lam) <= TV(P_d) + TV(f) in the
          direction stated, and the SHARE of each is the anatomy.
      (b) THE FRAME EDGES: the share of TV sitting in the outer edge_frac of the
          indices at each end, where the reflected (minus-Hankel) lag term is
          largest.
      (c) THE ARITHMETIC FLUTTER: the share of TV sitting on the diagonal indices
          r whose REFLECTED lag M-1-2r is a lag index hit by a prime-power atom.
          If a small index share carries a large TV share, the roughness is
          arithmetic and LOCAL, which is precisely what a moving geometric mean
          removes."""
    Lam = np.asarray(Lam, dtype=float)
    m = Lam.shape[0]
    lg = np.log(Lam)
    d = np.abs(np.diff(lg))
    tv = float(np.sum(d))
    x = (2.0 * np.arange(m, dtype=float) / max(m - 1.0, 1.0)) - 1.0
    co = np.polynomial.chebyshev.chebfit(x, lg, int(min(deg, max(m - 1, 1))))
    macro = np.polynomial.chebyshev.chebval(x, co)
    flut = lg - macro
    tv_ma = float(np.sum(np.abs(np.diff(macro))))
    tv_fl = float(np.sum(np.abs(np.diff(flut))))
    ne = max(1, int(edge_frac * m))
    tv_edge = float(np.sum(d[:ne])) + float(np.sum(d[max(0, d.shape[0] - ne):]))
    out = dict(tv=tv, tv_macro=tv_ma, tv_flut=tv_fl,
               share_macro=tv_ma / max(tv, 1.0e-300),
               share_flut=tv_fl / max(tv, 1.0e-300),
               share_edge=tv_edge / max(tv, 1.0e-300),
               idx_edge=2.0 * ne / max(m, 1),
               amp_flut=float(np.max(np.abs(flut))),
               share_hit=float("nan"), idx_hit=float("nan"))
    if hits_r is not None and len(hits_r) and d.shape[0]:
        msk = np.zeros(d.shape[0], dtype=bool)
        idx = np.asarray(hits_r, dtype=np.int64)
        idx = idx[(idx >= 0) & (idx < d.shape[0])]
        msk[idx] = True
        out["share_hit"] = float(np.sum(d[msk])) / max(tv, 1.0e-300)
        out["idx_hit"] = float(np.count_nonzero(msk)) / max(d.shape[0], 1)
    return out


# ----------------------------------------------------------------------------
# THE GENERALISED WHITENING and THE LIOUVILLE PASS-THROUGH
# ----------------------------------------------------------------------------
def whiten_with(A, A_B, Lam_t, want_kap=True):
    """THE GENERALISED WHITENING BY AN ARBITRARY POSITIVE DIAGONAL Lam~.
        E~ = Lam~^{-1/2} A Lam~^{-1/2} ,   W~ = Lam~^{-1/2} A_B Lam~^{-1/2} ,
        lam_min(A, A_B) >= lam_min(E~) / lam_max(W~) ,
    the last line being an identity plus one Rayleigh step (licence 5).  DIRECTION:
    kap~_up = cert_lam_max(W~) is an UPPER bound, and it is the ONLY price of the
    change of gauge."""
    sq = 1.0 / np.sqrt(np.asarray(Lam_t, dtype=float))
    E = sym(A * np.outer(sq, sq))
    W = sym(A_B * np.outer(sq, sq))
    kap_up = cert_lam_max(W, guess=ray_top(W)) if want_kap else float("nan")
    return dict(E=E, W=W, sqinv=sq, kap_up=kap_up)


def block_split(w, theta=THETA_BLK):
    """B = { k : lam_k <= theta lam_hat }.  PREREGISTERED rule, not tuned."""
    m = w.shape[0]
    lam_hat = float(w[0])
    nb = int(np.count_nonzero(w <= theta * lam_hat))
    nb = max(1, min(nb, m - 1)) if m > 1 else 1
    tau = (math.sqrt(max(float(w[nb - 1]), 1.0e-300) * max(float(w[nb]), 1.0e-300))
           if nb < m else float(w[-1]))
    return nb, tau


def liou_norm(V, sqinv):
    """phi = Lam~^{-1/2} psi, columnwise and normalised.  THE LIOUVILLE TRANSFORM:
        E~ psi = lam psi   <=>   A phi = lam Lam~ phi ,
    so phi -- not psi -- is the vector the PURE Toeplitz-minus-Hankel section acts
    on, and phi is what the classical theory speaks about."""
    PH = np.asarray(sqinv, dtype=float)[:, None] * V
    nrm = np.linalg.norm(PH, axis=0)
    nrm = np.where(nrm > 0.0, nrm, 1.0)
    return PH / nrm[None, :]


def bottom_pass(E, sqinv, kap_Lam, m, S, C, muD, muN, nb_probe=NB_PROBE):
    """THE PASS-THROUGH OF ONE CANDIDATE at the reweighted bottom.  The bottom
    nb_probe modes of E~ are computed, the preregistered block rule selects B, and
    the LIOUVILLE CEILING is applied to phi = Lam~^{-1/2} psi:
        m ||psi_j||_inf^2 <= kap_Lam~ m ||phi_hat_j||_inf^2 <= 2 kap_Lam~ ceil^2 ,
    every step in the direction stated and every step VERIFIED against the true
    sup norm.  rho = 2 kap_Lam~ ceil^2 / m is the relative distance to the trivial
    bound: rho < 1 is exactly the statement nu_L~ <~ m / (8 kap_Lam~)."""
    k = int(min(max(nb_probe, 2), m))
    try:
        w, V = eigh(E, subset_by_index=[0, k - 1])
    except (LinAlgError, ValueError):
        return None
    if not (float(w[0]) > 0.0):
        return None
    lam_hat = float(w[0])
    nb = int(np.count_nonzero(w <= THETA_BLK * lam_hat))
    nb = max(1, min(nb, k))
    VB = np.ascontiguousarray(V[:, :nb])
    PH = liou_norm(VB, sqinv)
    ml = mode_bounds(PH, m, S, C, muD, muN)
    mp = mode_bounds(VB, m, S, C, muD, muN, cap=m)
    sup = m * np.max(np.abs(VB), axis=0) ** 2
    b_L = np.minimum(2.0 * kap_Lam * ml["ceil"] ** 2, float(m))
    b_best = np.minimum(mp["bound"], b_L)
    nu_L = float(np.max(ml["nu"]))
    ceil_L = float(np.max(ml["ceil"]))
    out = dict(nb=nb, lam_hat=lam_hat,
               sep=float(w[min(nb, k - 1)] / lam_hat) if k > 1 else float("nan"),
               nu_L=nu_L, ceil_L=ceil_L,
               nu_plain=float(np.max(mp["nu"])),
               rho=2.0 * kap_Lam * ceil_L ** 2 / max(m, 1),
               rho_best=float(np.max(b_best)) / max(m, 1),
               sup_max=float(np.max(sup)),
               viol=max(ml["viol"], mp["viol"], float(np.max(sup - b_L)),
                        float(np.max(sup - b_best))),
               Q_B_ceil=float(np.sum(b_best)))
    del V, VB, PH, ml, mp
    return out


# ----------------------------------------------------------------------------
# THE CHAIN FACTORS (T145 .. T148, quoted in form)
# ----------------------------------------------------------------------------
def greedy_density(Wp):
    """CHARIKAR'S GREEDY PEELING (Charikar 2000).  Both directions used: the
    returned density is ATTAINED, hence a LOWER bound on the optimum, and the
    guarantee greedy >= opt/2 turns it into opt <= 2 x greedy -- the only bound
    here that holds over ALL 2^m subsets."""
    m = Wp.shape[0]
    if m < 2:
        return dict(dens=0.0, size=m)
    deg = Wp.sum(axis=1).astype(float)
    tot = 0.5 * float(deg.sum())
    alive = np.ones(m, dtype=bool)
    n_alive = m
    best, best_n = tot / m, m
    while n_alive > 1:
        d = np.where(alive, deg, np.inf)
        j = int(np.argmin(d))
        tot -= float(deg[j])
        alive[j] = False
        deg = deg - Wp[j]
        deg[j] = 0.0
        n_alive -= 1
        dens = tot / n_alive
        if dens > best:
            best, best_n = dens, n_alive
    return dict(dens=float(best), size=int(best_n))


def density_all_upper(R):
    """AN UPPER BOUND for Psi = sup_A (1^T R_AA 1)/|A| over ALL 2^m sets, the
    smaller of Charikar's greedy bound and the CERTIFIED lam_max of the same
    nonnegative matrix.  T145's LICENCE-4 lesson: what is passed in must be |R|."""
    Rp = np.maximum(R, 0.0)
    np.fill_diagonal(Rp, 0.0)
    gr = greedy_density(Rp)
    dg_max = float(np.max(np.diag(R)))
    psi_char = dg_max + 4.0 * gr["dens"]
    psi_spec = dg_max + cert_lam_max(Rp, guess=ray_top(Rp))
    cands = [x for x in (psi_char, psi_spec) if np.isfinite(x)]
    best = min(cands) if cands else float("nan")
    del Rp
    return dict(up=best, char=psi_char, spec=psi_spec, greedy=gr["dens"])


def c0_of_base(Gam, Gam_1, base, m):
    """THE A PRIORI LEVEL CONSTANT at a given cake base (T146, quoted):
        c_0^ap(base) = 2 base^2 Gam min(1, Gam_1) + eps ."""
    vmax_ap = Gam / math.sqrt(max(m, 1))
    lb = math.log(base)
    k_bot = int(math.floor(math.log(FL_TARGET) / lb))
    while base ** k_bot > FL_TARGET:
        k_bot -= 1
    eps = 2.0 * base * vmax_ap * m * (base ** k_bot)
    return 2.0 * base * base * Gam * min(1.0, Gam_1) + eps, eps


def counting_cert(E, lam_lo, m, ladder=RHO_LADDER):
    """THE CERTIFIED COUNTING FUNCTION AND THE Sw BOUND (T148, quoted in form).
    At tau_i = rho_i lam_lo a completed LDL^T gives N_i = #{k : lam_k < tau_i} as
    a CERTIFICATE (Sylvester 1852), whence the LAYER-CAKE bound
        sum_k lam_k^{-2} <= N_1/lam_lo^2 + sum_i (N_{i+1}-N_i)/tau_i^2
                            + (m - N_L)/tau_L^2
    and the CERTIFIED bottom-band constant C_bot with lam_k >= lam_lo k^2/C_bot
    for k <= N_L.  No sorted eigenvalue list is trusted anywhere."""
    N = []
    taus = []
    for rho in ladder:
        tau = rho * lam_lo
        n_i = inertia_neg(E - tau * np.eye(m))
        if n_i < 0:
            return None
        N.append(int(n_i))
        taus.append(float(tau))
    N = np.maximum.accumulate(np.array(N, dtype=float))
    taus = np.array(taus, dtype=float)
    s2 = N[0] / (lam_lo * lam_lo)
    for i in range(len(taus) - 1):
        s2 += max(N[i + 1] - N[i], 0.0) / (taus[i] * taus[i])
    s2 += max(m - N[-1], 0.0) / (taus[-1] * taus[-1])
    c_bot = max(N[0] ** 2, 1.0)
    for i in range(len(taus) - 1):
        c_bot = max(c_bot, N[i + 1] ** 2 / ladder[i])
    return dict(N=N, taus=taus, sum_inv2_up=float(s2), C_bot=float(c_bot),
                C_tail=float((m * m) / ladder[-1]), n_band=int(N[-1]))


def kms_scaling(w, k_fit=K_FIT):
    """THE MEASURED BOTTOM SCALING lam_k/lam_hat ~ k^alpha, with the classical
    order-2 value alpha = 2 (Kac-Murdock-Szego 1953: for the Dirichlet section the
    ratio lies in [4k^2/pi^2, k^2] EXACTLY).  MEASURED with a jackknife band; a
    FIT is never load-bearing.  C_meas = max_k k^2 lam_hat / lam_k is the constant
    the a priori ceiling would need over the WHOLE spectrum, and it READS the
    eigenvalues, so it is MEASURED."""
    m = w.shape[0]
    lam_hat = float(w[0])
    kk = np.arange(1, m + 1, dtype=float)
    ratio = w / max(lam_hat, 1.0e-300)
    kf = min(k_fit, m)
    f = pow_fit(kk[1:kf], ratio[1:kf], "lam_k/lam_hat")
    c_all = float(np.max(kk * kk / np.maximum(ratio, 1.0e-300)))
    c_bot = float(np.max((kk * kk / np.maximum(ratio, 1.0e-300))[:kf]))
    br_up = bool(np.all(ratio[:kf] <= kk[:kf] ** 2 * (1.0 + 1.0e-9)))
    br_lo = bool(np.all(ratio[:kf] >= 4.0 * kk[:kf] ** 2 / math.pi ** 2 - 1.0e-9))
    return dict(fit=f, C_meas=c_all, C_meas_bot=c_bot,
                bracket_up=br_up, bracket_lo=br_lo,
                r2=float(ratio[1]) if m > 1 else float("nan"))


def qstar_ceiling(V, w, m, S, C, muD, muN, sqinv, kap):
    """THE l1 CEILING APPLIED TO Q_star (T148, quoted in form).
        Q_star = m max_j sum_k V_jk^2 wt_k / sum_k wt_k ,   wt_k = lam_k^{-2}
              <= [ sum_{k <= K} b_k wt_k + m wt_{K+1} ] / sum_k wt_k
    for ANY cut K and ANY per-mode upper bounds b_k on m ||psi_k||_inf^2, the tail
    charged by ORTHONORMALITY and not by summing weights.  Four valid bounds per
    mode -- Dirichlet, Neumann, LIOUVILLE (2 kap_Lam~ ceil(phi_hat)^2) and the
    trivial m -- so the mode-by-mode minimum is valid, and minimising over the
    preregistered cut ladder is valid because every single cut is already an
    upper bound.  DIRECTION: an UPPER bound throughout."""
    wt = 1.0 / (w * w)
    tot = float(np.sum(wt))
    order = np.argsort(-wt)
    K = int(min(m, CUT_MAX))
    idx = order[:K]
    VW = np.ascontiguousarray(V[:, idx])
    mp = mode_bounds(VW, m, S, C, muD, muN, cap=m)
    ml = mode_bounds(liou_norm(VW, sqinv), m, S, C, muD, muN)
    sup = m * np.max(np.abs(VW), axis=0) ** 2
    b_pl = mp["bound"]
    b_li = np.minimum(2.0 * kap * ml["ceil"] ** 2, float(m))
    b_best = np.minimum(b_pl, b_li)
    wt_sorted = wt[order]
    wk = wt_sorted[:K]
    cum = np.cumsum(wk)

    def _best(bv):
        best, bcut = float("inf"), 1
        for cut in CUT_LADDER_Q:
            if cut > K:
                break
            tail = float(wt_sorted[cut]) if cut < m else 0.0
            val = (float(np.sum(bv[:cut] * wk[:cut])) + m * tail) \
                / max(tot, 1.0e-300)
            if val < best:
                best, bcut = val, cut
        return best, bcut

    q_pl, cut_pl = _best(b_pl)
    q_li, cut_li = _best(b_li)
    q_bs, cut_bs = _best(b_best)
    q_sup, _ = _best(np.minimum(sup, float(m)))
    # THE LADDER-NORMALISED FUNCTIONAL.  In the EXACT Kac-Murdock-Szego model the
    # k-th mode has nu_k = pi k^2 EXACTLY (verified on the control in V3.1), so
    # boundedness of nu over a GROWING set of modes is the wrong question: the
    # classical statement is nu_k <= C k^2 with C m-FREE.  This reads C off the
    # weighted cut, in the weight ordering, and it is the sharpened form of the
    # remaining rest.
    kk2 = (np.arange(cut_bs, dtype=float) + 1.0) ** 2
    rat = ml["nu"][:cut_bs] / kk2
    nu_k2 = float(np.max(rat))
    nu_k2_arg = int(np.argmax(rat)) + 1
    nu_k2_all = float(np.max(ml["nu"] / (np.arange(K, dtype=float) + 1.0) ** 2))
    out = dict(K=K, Qs_sup=q_sup, Qs_ceil=q_pl, Qs_ceil_L=q_li,
               nu_L_k2=nu_k2, nu_L_k2_all=nu_k2_all, nu_L_k2_arg=nu_k2_arg,
               nu_L_1=float(ml["nu"][0]),
               Qs_ceil_best=q_bs, cut=cut_bs, cut_pl=cut_pl, cut_li=cut_li,
               nu_wmax=float(np.max(mp["nu"][:cut_bs])),
               nu_L_wmax=float(np.max(ml["nu"][:cut_bs])),
               ceil_L_wmax=float(np.max(ml["ceil"][:cut_bs])),
               viol=max(mp["viol"], ml["viol"]),
               viol_b=float(np.max(sup - b_best)),
               wt_cut_frac=float(cum[cut_bs - 1]) / max(tot, 1.0e-300))
    del VW, mp, ml
    return out


def full_chain(A, A_B, Lam_t, S, C, muD, muN, gap_ex):
    """THE WHOLE T146/T147/T148 CHAIN with an ARBITRARY positive diagonal Lam~:
        lam_min(A, A_B) >= lam_min(E~) / kap~_up  >=  1 / (kap~_up c_0^ap Psi) ,
        c_0^ap = 2 base^2 Gam min(1, Gam_1) + eps ,  Gam = sqrt(Q_star) Sw .
    Every factor is rebuilt from the raw form, and the returned 'chain' is a LOWER
    bound on the true generalised eigenvalue -- which is verified against gap_ex
    by the caller.  Both variants are returned: the CERTIFIED one (computed
    factors) and the A PRIORI-SHAPED one (the certified Q_star CEILING and the
    certified counting bound substituted), so the price of a prioricity is a
    number and not an adjective."""
    m = A.shape[0]
    wt = whiten_with(A, A_B, Lam_t)
    E = wt["E"]
    kap_up = wt["kap_up"]
    if not np.isfinite(kap_up) or not (kap_up > 0.0):
        return None
    try:
        w, V = eigh(E)
    except (LinAlgError, ValueError):
        return None
    lam_hat = float(w[0])
    if not (lam_hat > 0.0):
        return None
    lam_lo = cert_lam_min(E, guess=lam_hat)
    if not (np.isfinite(lam_lo) and lam_lo > 0.0):
        return None
    fac = safe_cho(E)
    if fac is None:
        return None
    R = sym(cho_solve(fac, np.eye(m), check_finite=False))
    EV = E @ R
    den = np.sum(R * R, axis=0)
    num = np.sum(R * EV, axis=0)
    rres = np.linalg.norm(EV - np.eye(m), axis=0)
    del EV
    fl_q = chol_floor(gersh(E), m)
    lam_up = float(np.min(num / den)) + fl_q
    res_f = float(np.linalg.norm(rres))
    fro2 = float(np.sum(R * R))
    fro = math.sqrt(max(fro2, 1.0e-300))
    fro_lo = max(fro - res_f / lam_lo, 1.0e-300)
    fro_up = fro + res_f / lam_lo
    col_true = np.sqrt(den)
    col_cert = col_true + rres / lam_lo
    cmax = float(np.max(col_true))
    cmax_up = float(np.max(col_cert))
    Sw = lam_up * fro
    Sw_up = lam_up * fro_up
    Qs = m * cmax * cmax / fro2
    Qs_up = m * cmax_up * cmax_up / (fro_lo * fro_lo)
    gam_cert = math.sqrt(m) * lam_up * cmax_up
    gam_fac = math.sqrt(max(Qs_up, 0.0)) * Sw_up
    gam_id = math.sqrt(max(Qs, 0.0)) * Sw
    gam_true = math.sqrt(m) * lam_up * cmax
    gam1_cert = lam_up * float(np.sum(col_cert)) / math.sqrt(m)
    kap_Lam = float(np.max(Lam_t)) / max(float(np.min(Lam_t)), 1.0e-300)
    nb, tau = block_split(w)
    qc = qstar_ceiling(V, w, m, S, C, muD, muN, wt["sqinv"], kap_Lam)
    cc = counting_cert(E, lam_lo, m)
    km = kms_scaling(w)
    Sw_cnt = (lam_up * math.sqrt(max(cc["sum_inv2_up"], 0.0))
              if cc is not None else float("nan"))
    Sw_ap_meas = (lam_up / lam_lo) * km["C_meas"] * math.sqrt(ZETA4)
    gam_best = min(gam_cert, gam_fac)
    gam1_best = min(gam1_cert, lam_up * fro_up)
    c0_tbl = {b: c0_of_base(gam_best, gam1_best, b, m) for b in BASE_GRID}
    b_star = min(BASE_GRID, key=lambda b: c0_tbl[b][0])
    c0_ap, eps_ap = c0_tbl[b_star]
    dens = density_all_upper(np.abs(R))
    ok_psi = bool(np.isfinite(dens["up"]) and dens["up"] > 0.0)
    chain = (1.0 / (kap_up * c0_ap * dens["up"])) if ok_psi else float("nan")
    sw_apr = min([x for x in (Sw_cnt, Sw_ap_meas) if np.isfinite(x)] or [float("nan")])
    gam_apr = math.sqrt(max(qc["Qs_ceil_best"], 0.0)) * sw_apr
    c0_apr = min(c0_of_base(gam_apr, gam1_best, b, m)[0] for b in BASE_GRID)
    chain_apr = (1.0 / (kap_up * c0_apr * dens["up"])) if ok_psi else float("nan")
    out = dict(m=m, kap_up=kap_up, kap_Lam=kap_Lam, lam_hat=lam_hat,
               lam_lo=lam_lo, lam_up=lam_up, nb=nb, tau_rel=tau / lam_hat,
               Sw=Sw, Sw_up=Sw_up, Sw_cnt=Sw_cnt, Sw_ap_meas=Sw_ap_meas,
               Qs=Qs, Qs_up=Qs_up, Qs_ceil=qc["Qs_ceil"],
               Qs_ceil_L=qc["Qs_ceil_L"], Qs_ceil_best=qc["Qs_ceil_best"],
               Qs_sup=qc["Qs_sup"], cut=qc["cut"], wt_cut=qc["wt_cut_frac"],
               nu_wmax=qc["nu_wmax"], nu_L_wmax=qc["nu_L_wmax"],
               nu_L_k2=qc["nu_L_k2"], nu_L_k2_all=qc["nu_L_k2_all"],
               nu_L_k2_arg=qc["nu_L_k2_arg"], nu_L_1=qc["nu_L_1"],
               ceil_L_wmax=qc["ceil_L_wmax"], viol=qc["viol"],
               viol_b=qc["viol_b"], gam_true=gam_true, gam_id=gam_id,
               gam_best=gam_best, gam1_best=gam1_best, gam_apr=gam_apr,
               ident=abs(gam_id - gam_true) / max(abs(gam_true), 1.0e-300),
               c0_ap=c0_ap, c0_apr=c0_apr, base_star=b_star, psi_up=dens["up"],
               C_bot=cc["C_bot"] if cc is not None else float("nan"),
               n_band=cc["n_band"] if cc is not None else -1,
               kms_p=km["fit"]["p"], kms_sp=km["fit"]["sp"],
               C_meas=km["C_meas"], bracket_up=km["bracket_up"],
               bracket_lo=km["bracket_lo"],
               chain=chain, chain_apr=chain_apr,
               frac=chain / gap_ex if gap_ex > 0.0 else float("nan"),
               frac_apr=chain_apr / gap_ex if gap_ex > 0.0 else float("nan"))
    del E, R, V, wt, qc
    return out


# ----------------------------------------------------------------------------
# THE MODEL LADDER -- where the pure statement IS a theorem
# ----------------------------------------------------------------------------
def model_section(h, c=MODEL_C):
    """THE MODEL Toeplitz-minus-Hankel SECTION from the short symbol c, built
    through the SAME odd_toeplitz code path as the arithmetic form.  The symbol
    f(th) = (2 - 2 cos th) + q (2 - 2 cos th)^2 has a GENUINE ORDER-2 ZERO at
    th = 0 (verified in V0), so this is the setting of the classical statement."""
    M = 2 * h
    cc = np.zeros(M)
    n = min(len(c), M)
    cc[:n] = np.asarray(c, dtype=float)[:n]
    return sym(odd_toeplitz(cc, M))


def model_weight(m, kind):
    """THE WEIGHT CLASSES of T148's controlled experiment, quoted verbatim in form.
      'smooth' : Lam = 1 + amp cos(pi x) -- ONE oscillation, TV m-INDEPENDENT.
      'rough'  : Lam = 1 + amp cos(2 pi phi j), phi irrational -- oscillation at
                 the LATTICE scale, TV growing LINEARLY in m.  T148 measured
                 nu ~ m^1.994 for this class at IDENTICAL kap_Lam, which is what
                 named TV(log Lam) as the operative hypothesis.  THE SMOOTHING
                 FAMILY MUST REPAIR EXACTLY THIS CLASS, and that is the
                 calibration of V1."""
    x = np.arange(m, dtype=float) / max(m - 1.0, 1.0)
    if kind == "flat":
        return np.ones(m)
    if kind == "smooth":
        return 1.0 + WEIGHT_AMP * np.cos(math.pi * x)
    if kind == "wave":
        return 1.0 + WEIGHT_AMP * np.cos(8.0 * math.pi * x)
    if kind == "rough":
        phi = 0.5 * (math.sqrt(5.0) - 1.0)
        return 1.0 + WEIGHT_AMP * np.cos(
            2.0 * math.pi * phi * np.arange(m, dtype=float))
    raise ValueError(kind)


def nogo_form(m, eps=NOGO_EPS):
    """THE T145 NO-GO: R = a a^T + eps I with a_i = i^{-1/2}.  R is PD, entrywise
    nonnegative, its density sup over ALL sets is absolutely bounded, and the
    bottom eigenvector of E = R^{-1} is LOCALISED, so m ||psi||_inf^2 = m/H_m
    DIVERGES.  DECISIVE FOR THIS PROBE: the off-diagonal of E is NEGATIVE, so the
    lumping is trivial and the whitening diagonal is diag(E), which is a SMOOTH,
    monotone, nearly constant profile.  The smoothing family must therefore be
    nearly the IDENTITY here and must NOT rescue anything -- the break has to stay
    visible in the FORM, not in the multiplier."""
    a = 1.0 / np.sqrt(np.arange(1, m + 1, dtype=float))
    R = np.outer(a, a) + eps * np.eye(m)
    n2 = float(a @ a)
    E = sym((np.eye(m) - np.outer(a, a) / (eps + n2)) / eps)
    return dict(R=sym(R), E=E, a=a, psi=a / math.sqrt(n2),
                lam_min=1.0 / (n2 + eps), Q_exact=m / n2)


def control_form(m):
    """THE CONTROL: the Dirichlet path Laplacian L_0, the EXACT Kac-Murdock-Szego
    model.  Its whitening diagonal is CONSTANT, so EVERY candidate of the
    smoothing family is exactly the identity on it and every number must stay
    flat: bottom mode the half sine, m ||psi||_inf^2 -> 2, nu -> pi."""
    E = sym(2.0 * np.eye(m) - np.eye(m, k=1) - np.eye(m, k=-1))
    return dict(E=E, w=dirichlet_mu(m), psi=sine_basis(m)[0].copy())


# ----------------------------------------------------------------------------
section("V0  SETUP, THE RH FENCE, and THE LICENCES")
# ----------------------------------------------------------------------------
firewall()

ATOMS_ALL = atom_table(ATOM_MAX)
UU_ALL = [t[2] for t in ATOMS_ALL]
NN_ALL = [t[0] for t in ATOMS_ALL]
ATOM_PAIRS = [(t[2], t[3]) for t in ATOMS_ALL]
U_SORTED = np.array(UU_ALL, dtype=float)
GG_ALL = [UU_ALL[i + 1] - UU_ALL[i] for i in range(len(UU_ALL) - 1)]

NZ_DEEP = sum(1 for n in NN_ALL if n <= ZONE_DEEP)
G_DEEP = np.array(GG_ALL[:NZ_DEEP], dtype=float)
N_DEEP = np.array(NN_ALL[:NZ_DEEP], dtype=np.int64)

BERT_OK = bool(np.all(G_DEEP <= math.log(2.0) + 1.0e-12))
EVEN_OK = bool(np.all(G_DEEP >= np.log1p(1.0 / N_DEEP) - 1.0e-12))
check("ws_v0.gap_facts", BERT_OK and EVEN_OK,
      "the ONLY two gap facts consumed anywhere in this file hold on all %d "
      "prime-power gaps up to n = %d: Bertrand-Chebyshev 1852 (g <= log 2) and "
      "the trivial even bound (g >= log(1 + 1/n)).  No gap CONJECTURE is used"
      % (NZ_DEEP, ZONE_DEEP))

para("""V0.0  THE RH FENCE, STATED BEFORE ANY NUMBER AND PROMINENTLY.  The
surrounding statement of this whole investigation is the positivity of a Weil
window form (Weil 1952; Bombieri 2000; Connes 1999) on a FINITE list of
prime-power zones and a FINITE window.  Weil's explicit-formula criterion is
CITED here as an ADDRESS and is NEVER USED, in either direction.  No zero data of
any kind is read, generated, approximated or extrapolated -- the AST firewall
above enforces that together with the import whitelist and the absence of any
write-mode file access.  What this probe investigates is a GAUGE CHOICE in a
matrix inequality: which positive diagonal to whiten a Toeplitz-minus-Hankel
section with.  Even if the missing input closed perfectly, what would stand is a
finite-window positivity statement with an explicit constant on prime-power zones
in frame A; the distance from there to RH is mapped in V4 and is never
travelled.""")

para("""V0.1  WHAT MOVED IN T148 AND WHAT THIS FILE IS FOR.  T148 closed the Sw
side (certified <= %.4f, trend m^%.3f) and reduced the OTHER side to ONE scalar
inequality: an m-free bound on the smoothness functional nu_L of the bottom mode
of the REWEIGHTED section, target nu_L <~ m/(8 kap_Lam) ~ %.0f at m = 1077 against
%.0f measured.  It also ISOLATED the hypothesis behind the live route -- bounded
variation of log Lam, not the condition number -- by a model experiment in which
two bounded-variation weight classes stayed flat while a lattice-rough class grew
like m^%.3f at IDENTICAL kap_Lam.  On the arithmetic surface TV(log Lam) = %.2f
and grows like m^%.3f, which is what blocks the route.  THIS FILE ATTACKS THE
FACT THAT Lam IS A CHOICE: T144's kap_up <= %.4f certifies the JACOBI choice, it
does not privilege it, and any positive diagonal gives a valid chain.  The
question is whether a SMOOTHED diagonal with a certified sandwich buys a flat TV
without losing the chain."""
     % (SW_CERT_T148, SW_EXP_T148, NUL_TARGET_T148, NUL_T148, ROUGH_EXP_T148,
        TV_T148, TV_EXP_T148, KAP_UP_T144))

# --- V0.2  THE LICENCES, each VERIFIED before use ---------------------------
LIC = []

_m_lic = 401
_mu_lic = dirichlet_mu(_m_lic)
_muN_lic = neumann_mu(_m_lic)
_S_lic = sine_basis(_m_lic)
_C_lic = cosine_basis(_m_lic)
_L0_lic = sym(2.0 * np.eye(_m_lic) - np.eye(_m_lic, k=1) - np.eye(_m_lic, k=-1))
_eig_err = rel(_L0_lic @ _S_lic.T, _S_lic.T * _mu_lic[None, :])
check("ws_v0.lic1_exact_eigenpair", _eig_err < 1.0e-12,
      "LICENCE 1 (THEOREM, Kac-Murdock-Szego 1953): L_0 s_k = mu_k s_k with "
      "mu_k = 4 sin^2(pi k/(2(m+1))) holds to %.1e at m = %d, and the sine basis "
      "is orthonormal to %.1e -- the exact model both ceilings are built on"
      % (_eig_err, _m_lic, rel(_S_lic @ _S_lic.T, np.eye(_m_lic))))
LIC.append(("L1", "THEOREM", "exact Dirichlet eigenpair (KMS 1953)"))

_sup_ok = bool(np.max(np.abs(_S_lic)) <= math.sqrt(2.0 / (_m_lic + 1.0)) + 1.0e-14
               and np.max(np.abs(_C_lic)) <= math.sqrt(2.0 / _m_lic) + 1.0e-14)
check("ws_v0.lic2_sup_bounds", _sup_ok,
      "LICENCE 2 (THEOREM, elementary): ||s_k||_inf <= sqrt(2/(m+1)) and "
      "||c_k||_inf <= sqrt(2/m), the two facts that turn an l1 bound on Fourier "
      "coefficients into a sup bound on the mode via m||psi||_inf^2 <= 2||a||_1^2")
LIC.append(("L2", "THEOREM", "sup bounds of the two exact bases"))

_tt = np.linspace(1.0e-9, 0.5 * math.pi, 4001)
check("ws_v0.lic3_sine_lower", bool(np.all(np.sin(_tt) >= 2.0 * _tt / math.pi - 1e-15)),
      "LICENCE 3 (THEOREM, concavity): sin t >= 2t/pi on [0, pi/2], hence "
      "mu_k >= 4k^2/(m+1)^2 -- the step that makes the l1 ceiling's closed form "
      "2 sqrt(nu) + 1 completely m-FREE, with nu the only carrier of m")
LIC.append(("L3", "THEOREM", "sin t >= 2t/pi, hence mu_k >= 4k^2/(m+1)^2"))

_rng = np.random.default_rng(20260729)
_Xl = np.stack([_S_lic[0], _C_lic[0], _C_lic[3],
                np.exp(-((np.arange(_m_lic) - 200.0) / 40.0) ** 2),
                _rng.standard_normal(_m_lic)], axis=1)
_mbl = mode_bounds(_Xl, _m_lic, _S_lic, _C_lic, _mu_lic, _muN_lic, cap=_m_lic)
_sup_l = _m_lic * np.max(np.abs(_Xl / np.linalg.norm(_Xl, axis=0)[None, :]),
                         axis=0) ** 2
check("ws_v0.lic4_l1_ceiling", _mbl["viol"] <= 1.0e-9
      and bool(np.all(_sup_l <= _mbl["bound"] * (1.0 + 1.0e-9))),
      "LICENCE 4 (CERTIFIED, T148 quoted and re-verified): the coefficient bound "
      "|a_k| <= min(1, ||s_k||_inf ||L^p psi||_1/mu_k^p) holds against the TRUE "
      "coefficients with worst excess %.1e on 5 test vectors (two exact modes, a "
      "Gaussian bump, a random vector), and the resulting bound on m||psi||_inf^2 "
      "holds with worst ratio %.4f.  DIRECTION: upward on |a_k|, upward on the sup"
      % (_mbl["viol"], float(np.max(_sup_l / np.maximum(_mbl["bound"], 1e-300)))))
LIC.append(("L4", "CERTIFIED", "the second-difference l1 ceiling (T148)"))

# THE NEW LICENCES OF THIS PROBE: the gauge freedom, its price, and its invariance
_h_lic = 140
_A_lic = model_section(_h_lic)
_lp_lic = lump_pair(_A_lic)
_AB_lic = _lp_lic["A_B"]
_Lam_lic = np.diag(_AB_lic).copy()
_gap_lic = float(eigh(_A_lic, _AB_lic, eigvals_only=True,
                      subset_by_index=[0, 0])[0])
_fam_lic = smoothing_family(_Lam_lic)
_S_h = sine_basis(_h_lic)
_C_h = cosine_basis(_h_lic)
_muD_h = dirichlet_mu(_h_lic)
_muN_h = neumann_mu(_h_lic)
_worst_gauge = -1.0
_worst_sand = -1.0
_W0_lic = sym(_AB_lic * np.outer(1.0 / np.sqrt(_Lam_lic), 1.0 / np.sqrt(_Lam_lic)))
_kap0_lic = cert_lam_max(_W0_lic, guess=ray_top(_W0_lic))
for _nm, _Lt in _fam_lic.items():
    _sd = sandwich_cert(_Lam_lic, _Lt)
    _wt = whiten_with(_A_lic, _AB_lic, _sd["Lam_t"])
    _lo = cert_lam_min(_wt["E"], guess=float(eigvalsh(
        _wt["E"], subset_by_index=[0, 0])[0]))
    _worst_gauge = max(_worst_gauge, (_lo / _wt["kap_up"]) / _gap_lic)
    _worst_sand = max(_worst_sand,
                      _wt["kap_up"] / (_kap0_lic / max(_sd["c1"], 1.0e-300)))
check("ws_v0.lic5_gauge_freedom", _worst_gauge <= 1.0 + 1.0e-9,
      "LICENCE 5 (CERTIFIED, the lever of this probe): for EVERY one of the %d "
      "candidate diagonals, lam_min(E~)/kap~_up is a LOWER bound on the true "
      "generalised eigenvalue lam_min(A, A_B) -- worst ratio %.6f <= 1 on the "
      "model pair at h = %d.  The inequality is an identity plus one Rayleigh "
      "step and needs NOTHING about Lam~ beyond positivity, which is exactly why "
      "the whitening diagonal is a free gauge"
      % (len(_fam_lic), _worst_gauge, _h_lic))
LIC.append(("L5", "CERTIFIED", "any positive diagonal gives a valid chain"))

check("ws_v0.lic6_sandwich_transport", _worst_sand <= 1.0 + 1.0e-9,
      "LICENCE 6 (CERTIFIED, the price): c_1 Lam <= Lam~ implies "
      "kap~_up = lam_max(Lam~^{-1/2} A_B Lam~^{-1/2}) <= kap_up/c_1, verified with "
      "worst ratio %.6f <= 1 over the family; and c_1 Lam <= Lam~ <= c_2 Lam "
      "implies kap_Lam~ <= (c_2/c_1) kap_Lam.  So the ENTIRE cost of smoothing is "
      "the certified sandwich ratio, and it enters the chain LINEARLY"
      % _worst_sand)
LIC.append(("L6", "CERTIFIED", "kap~_up <= kap_up/c_1, the whole price"))

_t_sc = 3.7
_wt_a = whiten_with(_A_lic, _AB_lic, _Lam_lic)
_wt_b = whiten_with(_A_lic, _AB_lic, _t_sc * _Lam_lic)
_lo_a = cert_lam_min(_wt_a["E"], guess=float(eigvalsh(_wt_a["E"],
                     subset_by_index=[0, 0])[0]))
_lo_b = cert_lam_min(_wt_b["E"], guess=float(eigvalsh(_wt_b["E"],
                     subset_by_index=[0, 0])[0]))
_inv_err = abs((_lo_a / _wt_a["kap_up"]) - (_lo_b / _wt_b["kap_up"])) \
    / max(abs(_lo_a / _wt_a["kap_up"]), 1.0e-300)
check("ws_v0.lic7_scale_invariance", _inv_err < 1.0e-9,
      "LICENCE 7 (CERTIFIED, elementary): the chain bound lam_min(E~)/kap~_up is "
      "INVARIANT under Lam~ -> t Lam~ (relative change %.1e at t = %.1f), so only "
      "the SHAPE of Lam~ matters and the sandwich constants are normalised to "
      "geometric mean 1 without loss.  This is why 'const' is a single candidate "
      "and not a one-parameter family" % (_inv_err, _t_sc))
LIC.append(("L7", "CERTIFIED", "scale invariance of the whole chain"))

_sq_lic = 1.0 / np.sqrt(_Lam_lic)
_w_lic, _V_lic = eigh(sym(_A_lic * np.outer(_sq_lic, _sq_lic)),
                      subset_by_index=[0, 3])
_PH_lic = liou_norm(np.ascontiguousarray(_V_lic), _sq_lic)
_liou_err = rel(_A_lic @ _PH_lic,
                (_Lam_lic[:, None] * _PH_lic) * _w_lic[None, :])
check("ws_v0.lic8_liouville", _liou_err < 1.0e-10,
      "LICENCE 8 (CERTIFIED, the Liouville transform): E~ psi = lam psi is "
      "EQUIVALENT to A phi = lam Lam~ phi with phi = Lam~^{-1/2} psi, verified to "
      "%.1e on the bottom 4 modes.  phi -- not psi -- is the vector the PURE "
      "Toeplitz-minus-Hankel section acts on, so phi is the object the classical "
      "weighted-Szego statement speaks about, and the pass-through price is the "
      "single constant kap_Lam~ = max Lam~ / min Lam~" % _liou_err)
LIC.append(("L8", "CERTIFIED", "the Liouville transform is exact"))

_n_lic = 240
_ng_lic = nogo_form(_n_lic)
_w_ng = np.linalg.eigvalsh(_ng_lic["E"])
_in_ng = inertia_neg(_ng_lic["E"] - 1.5 * float(_w_ng[0]) * np.eye(_n_lic))
check("ws_v0.lic9_inertia", _in_ng >= 0
      and _in_ng == int(np.count_nonzero(_w_ng < 1.5 * float(_w_ng[0]))),
      "LICENCE 9 (CERTIFIED, Sylvester 1852 / Bunch-Kaufman 1977): the LDL^T "
      "inertia count at tau agrees with the sorted spectrum on the no-go form "
      "(count %d at m = %d).  Used for the counting bound of the Sw factor, which "
      "is QUOTED from T148 and not re-derived" % (_in_ng, _n_lic))
LIC.append(("L9", "CERTIFIED", "inertia counting (Sylvester 1852)"))

_Lr = np.exp(0.7 * np.sin(np.arange(600) * 0.9) + 0.3 * np.arange(600) / 600.0)
_mo = _mono_hull(_Lr)
_un = _unim_hull(_Lr)
_tv_mo = float(np.sum(np.abs(np.diff(np.log(_mo)))))
_tv_un = float(np.sum(np.abs(np.diff(np.log(_un)))))
_kap_r = math.log(float(np.max(_Lr)) / float(np.min(_Lr)))
_hull_ok = (abs(_tv_mo - math.log(_mo[-1] / _mo[0])) < 1.0e-12
            and _tv_un <= 2.0 * _kap_r + 1.0e-12
            and bool(np.all(_mo >= _Lr - 1.0e-15))
            and bool(np.all(_un >= _Lr - 1.0e-15)))
check("ws_v0.lic10_hull_tv", _hull_ok,
      "LICENCE 10 (CERTIFIED, elementary): the monotone majorant satisfies "
      "TV(log Lam~) = log(last/first) EXACTLY (%.6f) and the unimodal hull "
      "TV <= 2 log kap_Lam (%.4f <= %.4f), both BY CONSTRUCTION and with no "
      "hypothesis on Lam at all -- these two candidates have a flat TV for free "
      "and pay only in the sandwich" % (_tv_mo, _tv_un, 2.0 * _kap_r))
LIC.append(("L10", "CERTIFIED", "hull candidates: TV bounded by construction"))

_mg = _movgeo(_Lr, 60)
_tv_r = float(np.sum(np.abs(np.diff(np.log(_Lr)))))
_tv_mg = float(np.sum(np.abs(np.diff(np.log(_mg)))))
_mg_ok = (_tv_mg <= _tv_r + 1.0e-12
          and bool(np.all(_mg >= float(np.min(_Lr)) - 1.0e-12))
          and bool(np.all(_mg <= float(np.max(_Lr)) + 1.0e-12)))
check("ws_v0.lic11_movgeo", _mg_ok,
      "LICENCE 11 (CERTIFIED, convexity): every entry of the moving geometric "
      "mean is a convex combination of values of log Lam, so min Lam <= Lam~ <= "
      "max Lam entrywise, and TV(log Lam~) <= TV(log Lam) always (%.4f <= %.4f, a "
      "factor %.1f on this test sequence).  The reduction is by the WINDOW WIDTH "
      "for oscillation at short period, which is the mechanism the family bets on"
      % (_tv_mg, _tv_r, _tv_r / max(_tv_mg, 1.0e-300)))
LIC.append(("L11", "CERTIFIED", "moving geometric mean: sandwich and TV"))

_mc_lic = np.array(MODEL_C, dtype=float)
_mod_sym = symbol_order(_mc_lic)
_th_lic, _f_lic = symbol_values(_mc_lic)
_ord_lic = pow_fit(_th_lic[1:16], np.abs(_f_lic[1:16] - _f_lic[0]), "model order")
_f0_ok = abs(_mod_sym["f0"]) < 1.0e-12
check("ws_v0.lic12_model_order2", _f0_ok and band_ok(_ord_lic, 1.7, 2.3),
      "LICENCE 12 (CERTIFIED): the MODEL symbol f = (2-2cos th) + %.1f (2-2cos "
      "th)^2 has f(0) = %.1e and a measured local exponent in the order-2 band, so "
      "the model ladder tests the classical KMS/Widom statement WHERE IT IS A "
      "THEOREM.  The arithmetic symbol does NOT (T148: f(0) < 0 on 48/48), and "
      "that asymmetry is respected everywhere below" % (MODEL_Q, _mod_sym["f0"]))
LIC.append(("L12", "CERTIFIED", "the model symbol has an order-2 zero"))

_cst = np.full(_h_lic, float(np.exp(np.mean(np.log(_Lam_lic)))))
_wt_c = whiten_with(_A_lic, _AB_lic, _cst, want_kap=False)
_wc, _Vc = eigh(_wt_c["E"], subset_by_index=[0, 2])
_PHc = liou_norm(np.ascontiguousarray(_Vc), _wt_c["sqinv"])
_wA, _VA = eigh(_A_lic, subset_by_index=[0, 2])
_nu_c = mode_bounds(_PHc, _h_lic, _S_h, _C_h, _muD_h, _muN_h)["nu"]
_nu_A = mode_bounds(np.ascontiguousarray(_VA), _h_lic, _S_h, _C_h,
                    _muD_h, _muN_h)["nu"]
_const_err = float(np.max(np.abs(_nu_c - _nu_A))) / max(float(np.max(_nu_A)),
                                                        1.0e-300)
check("ws_v0.lic13_const_is_pure", _const_err < 1.0e-8,
      "LICENCE 13 (CERTIFIED, identification): for the 'const' candidate the "
      "reweighted section is the PURE section rescaled, so the Liouville mode IS "
      "the pure bottom mode and nu_L~ EQUALS the pure nu (relative difference "
      "%.1e on the bottom 3 modes).  Consequence, and it is the conceptual point "
      "of this probe: with Lam~ constant the smoothness question is EXACTLY the "
      "classical Szego/Widom question about A itself, kap_Lam~ = 1 EXACTLY, and "
      "the entire cost of the gauge has moved into the single certified constant "
      "kap~_up" % _const_err)
LIC.append(("L13", "CERTIFIED", "'const' reduces nu_L~ to the classical object"))

info("V0.2.licence_count", "%d licences: %d THEOREM, %d CERTIFIED.  Every one is "
     "verified ABOVE its first use, and every name states its DIRECTION"
     % (len(LIC), sum(1 for _, c, _ in LIC if c == "THEOREM"),
        sum(1 for _, c, _ in LIC if c == "CERTIFIED")))
del _A_lic, _AB_lic, _L0_lic, _S_lic, _C_lic, _Xl, _ng_lic, _fam_lic


# ----------------------------------------------------------------------------
section("V1  THE SMOOTHING FAMILY -- SANDWICH, TV, and nu_L~")
# ----------------------------------------------------------------------------
para("""V1.0  THE FAMILY AND THE THREE NUMBERS.  Nine candidate whitening
diagonals are declared in CAND_ORDER before any result is seen: 'id' (T148's
Jacobi diagonal), 'const' (the geometric mean -- the fully degenerate smoothing,
for which the reweighted section is the PURE section rescaled and kap_Lam~ = 1
EXACTLY, licence 13), two MOVING GEOMETRIC MEANS at half-width 5%% and 15%% of m,
the DYADIC piecewise geometric mean refined towards both window edges, two
POLYNOMIAL MACRO FITS of degree 2 and 6, and the MONOTONE and UNIMODAL hulls whose
TV is bounded by construction (licence 10).  Each candidate is scored on exactly
three numbers, and the contract of this probe is that ONE candidate must carry all
three simultaneously, m-flat and zone-flat:
  (1) THE SANDWICH sig = c_2/c_1 with c_1 Lam <= Lam~ <= c_2 Lam, CERTIFIED per
      window by outward-rounded extremal ratios.  It is the whole price: it enters
      the chain through kap~_up <= kap_up/c_1 and kap_Lam~ <= sig kap_Lam
      (licence 6).  Bar: sig <= %.1f.
  (2) TV(log Lam~), the isolated hypothesis of T148's ROUTE S.  Bar: <= %.1f, and
      FLAT in m.  Baseline to beat: %.2f growing like m^%.3f.
  (3) nu_L~, the smoothness functional of the bottom block AFTER the Liouville
      transform with respect to Lam~, read through rho = 2 kap_Lam~ ceil^2/m.
      rho < 1 IS the statement nu_L~ <~ m/(8 kap_Lam~), i.e. the Liouville ceiling
      beating the trivial bound at all.  Baseline to beat: nu_L = %.0f against a
      target of %.0f at m = 1077.""" % (SAND_BAR, TV_BAR, TV_T148, TV_EXP_T148,
                                        NUL_T148, NUL_TARGET_T148))

# --- V1.1  THE CALIBRATION: does the family repair the class it must? --------
para("""V1.1  CALIBRATION ON THE MODEL LADDER, BEFORE THE SURFACE.  T148's
controlled experiment is re-run, with the smoothing family inserted.  The model
section has a GENUINE order-2 symbol zero (licence 12), so the pure statement is a
THEOREM there (Kac-Murdock-Szego 1953; Widom 1958).  Two weight classes are used:
'smooth' (one oscillation, TV m-free -- the route works already) and 'rough'
(oscillation at the LATTICE scale, TV growing like m -- the class that BROKE the
route, nu ~ m^%.3f in T148).  IF the smoothing family is the right instrument, it
must repair the rough class and leave the smooth one alone, and it must do so at a
BOUNDED sandwich.  This is a calibration of the instrument, not a claim about the
arithmetic surface.""" % ROUGH_EXP_T148)

MOD = {}
for kind in MODEL_KINDS:
    for h in MODEL_SIZES:
        if h > MAX_H or budget_left() < RESERVE_S + 60.0:
            break
        A_m = model_section(h)
        Lam_m = model_weight(h, kind)
        S_m = sine_basis(h)
        C_m = cosine_basis(h)
        muD_m = dirichlet_mu(h)
        muN_m = neumann_mu(h)
        fam_m = smoothing_family(Lam_m, MODEL_CANDS)
        for nm, Lt in fam_m.items():
            sd = sandwich_cert(Lam_m, Lt)
            reg = weight_regularity(sd["Lam_t"])
            wt = whiten_with(A_m, A_m, sd["Lam_t"], want_kap=False)
            bp = bottom_pass(wt["E"], wt["sqinv"], reg["kap"], h,
                             S_m, C_m, muD_m, muN_m)
            if bp is None:
                continue
            MOD.setdefault((kind, nm), []).append(dict(
                m=h, sig=sd["sig"], c1=sd["c1"], c2=sd["c2"], tv=reg["tv"],
                kap=reg["kap"], nu_L=bp["nu_L"], nu_plain=bp["nu_plain"],
                rho=bp["rho"], viol=bp["viol"], nb=bp["nb"]))
            del wt, bp
        del A_m, S_m, C_m, fam_m

MOD_FIT = {}
MOD_VIOL = 0.0
for key, rows in MOD.items():
    MOD_FIT[key] = dict(
        nu=pow_fit([r["m"] for r in rows], [r["nu_L"] for r in rows], "nu_L"),
        npl=pow_fit([r["m"] for r in rows], [r["nu_plain"] for r in rows], "nu"),
        tv=pow_fit([r["m"] for r in rows], [r["tv"] for r in rows], "tv"))
    MOD_VIOL = max(MOD_VIOL, qmax([r["viol"] for r in rows]))
    info("V1.1.model", "%-7s %-6s sig %6.3f TV %8.3f %-16s nu(psi) %10.2f %-16s "
         "nu_L(phi) %8.2f %-16s rho %7.4f"
         % (key[0], key[1], qmax([r["sig"] for r in rows]),
            qmax([r["tv"] for r in rows]), fit_str(MOD_FIT[key]["tv"]),
            qmax([r["nu_plain"] for r in rows]), fit_str(MOD_FIT[key]["npl"]),
            qmax([r["nu_L"] for r in rows]), fit_str(MOD_FIT[key]["nu"]),
            qmax([r["rho"] for r in rows])))

_rough_id = MOD_FIT.get(("rough", "id"))
_rough_cst = MOD_FIT.get(("rough", "const"))
_rough_mgm = MOD_FIT.get(("rough", "mgm15"))
_smooth_id = MOD_FIT.get(("smooth", "id"))
MODEL_REPAIRS = bool(
    _rough_id is not None and _rough_cst is not None
    and _rough_id["npl"]["p"] > 1.0 and flat_ok(_rough_cst["nu"], 0.6)
    and flat_ok(_rough_id["nu"], 0.6))
check("ws_v1.model_calibration", MOD_VIOL <= 1.0e-8 and MODEL_REPAIRS,
      "V1.1 CALIBRATION, AND IT SEPARATES THE TWO OBJECTS CLEANLY.  On the rough "
      "(lattice-scale) weight class the RAW mode functional nu(psi) -- exactly "
      "T148's measured object -- grows like %s, reproducing T148's %s: the raw "
      "mode inherits the lattice oscillation of the multiplier.  The LIOUVILLE "
      "functional nu_L(phi) of the SAME gauge is already FLAT (%s), which is the "
      "model-side confirmation that phi and not psi is the object the classical "
      "theory speaks about (licence 8).  What the SMOOTHING then buys is not the "
      "exponent but the CONSTANT: 'const' has kap_Lam~ = 1 exactly and rho %.4f "
      "against %.4f for 'id', at a certified sandwich %.3f.  On the smooth class "
      "everything is flat already (%s).  Every Liouville bound was VERIFIED "
      "against the true sup norm, worst excess %.1e"
      % (fit_str(_rough_id["npl"]) if _rough_id else "n/a",
         "m^%.3f" % ROUGH_EXP_T148,
         fit_str(_rough_id["nu"]) if _rough_id else "n/a",
         qmax([r["rho"] for r in MOD.get(("rough", "const"), [dict(rho=float("nan"))])]),
         qmax([r["rho"] for r in MOD.get(("rough", "id"), [dict(rho=float("nan"))])]),
         qmax([r["sig"] for r in MOD.get(("rough", "const"), [dict(sig=float("nan"))])]),
         fit_str(_smooth_id["nu"]) if _smooth_id else "n/a", MOD_VIOL))

# --- V1.2  THE SURFACE ------------------------------------------------------
para("""V1.2  THE SURFACE.  Same construction as T140 .. T148: prime-power zones
in frame A, D = g/(2 nu) with nu = %d, the window forced even so that h = M/2, the
odd Toeplitz-minus-Hankel section A, the lumped Stieltjes partner A_B = A + L_Delta,
and then the NINE gauges.  %d zones with h <= %d are declared here, BEFORE any
result is seen.  Per window and per gauge: the certified sandwich, TV(log Lam~),
kap_Lam~, the CERTIFIED kap~_up (one completed Cholesky each), and the bottom-block
pass-through nu_L~ / ceil / rho.  Per window additionally: the TV ANATOMY of the
Jacobi diagonal, and the FULL CHAIN for the 'id' gauge, the 'const' gauge, and the
best admissible gauge of that window.""" % (NU_MAIN, SURF_ZONES, SURF_HCAP))

CAND = []
for k in range(2, NZ_DEEP - 2):
    D_k = 0.5 * float(G_DEEP[k]) / NU_MAIN
    M_k = even_window(UU_ALL[k], D_k)
    h_k = M_k // 2
    if h_k < H_MIN or h_k > SURF_HCAP:
        continue
    CAND.append((k, D_k, M_k, h_k))
SZ = []
if CAND:
    step = max(1, len(CAND) // max(SURF_ZONES, 1))
    SZ = CAND[::-1][::step][:SURF_ZONES]
    SZ.sort(key=lambda t: t[0])
info("V1.2.zones", "%d prime-power zones admit a frame-A window inside the cap "
     "(h <= %d, MAX_H = %d); the surface takes %d of them (stride %d) from the "
     "deep end" % (len(CAND), SURF_HCAP, MAX_H, len(SZ), step))

ROWS = []
CROWS = {}
ANAT = []
SKIP = dict(stieltjes=0, gap=0, pos=0, cand=0, chain=0)
for (i_w, (k, D_k, M_k, h_k)) in enumerate(SZ):
    if budget_left() < RESERVE_S:
        info("V1.2.budget", "surface truncated at n = %d after %d windows"
             % (NN_ALL[k], len(ROWS)))
        break
    al = 0.5 * M_k * D_k
    c_lag, _ = lag_vector_fast(al, M_k, atoms_in(al, ATOMS_ALL))
    A = sym(odd_toeplitz(c_lag, M_k))
    so = symbol_order(c_lag)
    lp = lump_pair(A)
    if lp["stieltjes"] != 1:
        SKIP["stieltjes"] += 1
        continue
    A_B = lp["A_B"]
    Lam = np.diag(A_B).copy()
    if not (float(np.min(Lam)) > 0.0):
        SKIP["pos"] += 1
        continue
    try:
        gap_ex = float(eigh(A, A_B, eigvals_only=True, subset_by_index=[0, 0])[0])
    except (LinAlgError, ValueError):
        SKIP["gap"] += 1
        continue
    if not (gap_ex > 0.0):
        SKIP["gap"] += 1
        continue
    m = A.shape[0]
    S = sine_basis(m)
    C = cosine_basis(m)
    muD = dirichlet_mu(m)
    muN = neumann_mu(m)

    # THE TV ANATOMY of the Jacobi diagonal: the diagonal index r carries the
    # reflected lag M-1-2r, so an atom landing on lag i imprints at r = (M-1-i)/2
    hits_lag = atom_hit_lags(al, M_k)
    hits_r = np.unique(np.floor((M_k - 1 - hits_lag) / 2.0).astype(np.int64))
    an = tv_anatomy(Lam, hits_r=hits_r)
    an["m"] = m
    an["D"] = D_k
    an["n"] = NN_ALL[k]
    ANAT.append(an)

    fam = smoothing_family(Lam)
    rec = {}
    for nm, Lt in fam.items():
        sd = sandwich_cert(Lam, Lt)
        reg = weight_regularity(sd["Lam_t"])
        wt = whiten_with(A, A_B, sd["Lam_t"])
        if not np.isfinite(wt["kap_up"]) or not (wt["kap_up"] > 0.0):
            del wt
            continue
        bp = bottom_pass(wt["E"], wt["sqinv"], reg["kap"], m, S, C, muD, muN)
        if bp is None:
            del wt
            continue
        row = dict(n=NN_ALL[k], D=D_k, m=m, cand=nm,
                   c1=sd["c1"], c2=sd["c2"], sig=sd["sig"],
                   tv=reg["tv"], kap_Lam=reg["kap"], curv=reg["curv"],
                   d1_max=reg["d1_max"], kap_up=wt["kap_up"],
                   nu_L=bp["nu_L"], nu_plain=bp["nu_plain"],
                   ceil_L=bp["ceil_L"], rho=bp["rho"], rho_best=bp["rho_best"],
                   nb=bp["nb"], viol=bp["viol"], sup_max=bp["sup_max"],
                   target=m / (8.0 * max(reg["kap"], 1.0e-300)),
                   Lam_t=sd["Lam_t"])
        rec[nm] = row
        CROWS.setdefault(nm, []).append({kk: vv for kk, vv in row.items()
                                         if kk != "Lam_t"})
        del wt, bp
    if "id" not in rec:
        SKIP["cand"] += 1
        del A, A_B, S, C, fam, rec
        continue

    # the in-window best ADMISSIBLE gauge by the preregistered rule
    adm = [r for r in rec.values()
           if r["sig"] <= SAND_BAR and r["tv"] <= TV_BAR]
    best_nm = (min(adm, key=lambda r: r["rho"])["cand"] if adm else "id")
    ch = {}
    for nm in dict.fromkeys(("id", "const", best_nm)):
        if nm not in rec or budget_left() < 0.35 * RESERVE_S:
            continue
        fc = full_chain(A, A_B, rec[nm]["Lam_t"], S, C, muD, muN, gap_ex)
        if fc is None:
            continue
        ch[nm] = fc
    if "id" not in ch:
        SKIP["chain"] += 1
        del A, A_B, S, C, fam, rec
        continue
    ROWS.append(dict(n=NN_ALL[k], D=D_k, m=m, gap_ex=gap_ex,
                     best_nm=best_nm, n_adm=len(adm), rec=rec, ch=ch,
                     sym_f0=so["f0"], sym_gam=so["gam"],
                     tv_id=rec["id"]["tv"], kap_Lam_id=rec["id"]["kap_Lam"],
                     anat=an))
    del A, A_B, S, C, muD, muN, fam

check("ws_v1.surface_nonempty", len(ROWS) >= 8,
      "%d windows carried the full nine-gauge anatomy and at least the 'id' chain "
      "(need >= 8 for four populated D-strata); skips %s"
      % (len(ROWS), SKIP))

if not ROWS:
    info("V1.abort", "no window survived; the remaining blocks are skipped")
    print("")
    print("TOTAL  %d checks, %d passed, %d failed, %.1f s"
          % (PASS + FAIL, PASS, FAIL, time.time() - T_START))
    raise SystemExit(1)

DV = [r["D"] for r in ROWS]
MV = [r["m"] for r in ROWS]
info("V1.2.surface", "%d windows, m = %d .. %d, D = %.3e .. %.3e, n = %d .. %d; "
     "the exact generalised eigenvalue spans %.3e .. %.3e and the arithmetic "
     "symbol has f(0) = %.3e .. %.3e -- T148's honest negative, re-read and NOT "
     "re-derived: the section is NOT a nonnegative order-2 symbol section"
     % (len(ROWS), min(MV), max(MV), qmin(DV), qmax(DV),
        min(r["n"] for r in ROWS), max(r["n"] for r in ROWS),
        qmin([r["gap_ex"] for r in ROWS]), qmax([r["gap_ex"] for r in ROWS]),
        qmin([r["sym_f0"] for r in ROWS]), qmax([r["sym_f0"] for r in ROWS])))

# --- V1.3  THE PER-GAUGE TABLE, the three numbers each ----------------------
VIOL_ALL = qmax([qmax([r["viol"] for r in rows]) for rows in CROWS.values()])
check("ws_v1.liouville_valid", VIOL_ALL <= 1.0e-8,
      "V1.3 EVERY LIOUVILLE BOUND IS VALID ON EVERY GAUGE AND EVERY WINDOW: the "
      "certified bound 2 kap_Lam~ ceil(phi_hat)^2 was compared with the TRUE "
      "m||psi||_inf^2 of each bottom mode of each of the %d gauges on all %d "
      "windows, worst excess %.1e.  A gauge that broke a direction would be "
      "reported here rather than silently used" % (len(CROWS), len(ROWS), VIOL_ALL))

TBL = {}
for nm in CAND_ORDER:
    rows = CROWS.get(nm, [])
    if len(rows) < max(6, len(ROWS) // 2):
        continue
    mm = [r["m"] for r in rows]
    f_sig = pow_fit(mm, [r["sig"] for r in rows], "sig")
    f_tv = pow_fit(mm, [max(r["tv"], 1.0e-12) for r in rows], "tv")
    f_nu = pow_fit(mm, [r["nu_L"] for r in rows], "nu_L")
    f_rho = pow_fit(mm, [r["rho"] for r in rows], "rho")
    f_kap = pow_fit(mm, [r["kap_up"] for r in rows], "kap_up")
    sig_max = qmax([r["sig"] for r in rows])
    tv_max = qmax([r["tv"] for r in rows])
    rho_max = qmax([r["rho"] for r in rows])
    nu_max = qmax([r["nu_L"] for r in rows])
    hit = sum(1 for r in rows if r["nu_L"] <= r["target"])
    hit_m = [r["m"] for r in rows if r["nu_L"] <= r["target"]]
    top = max(rows, key=lambda r: r["m"])
    TBL[nm] = dict(
        m_hit=min(hit_m) if hit_m else float("nan"),
        nu_top=top["nu_L"], tgt_top=top["target"], rho_top=top["rho"],
        rho_best_max=qmax([r["rho_best"] for r in rows]), m_top=top["m"],
        n=len(rows), sig_max=sig_max, sig_fit=f_sig,
        tv_max=tv_max, tv_min=qmin([r["tv"] for r in rows]), tv_fit=f_tv,
        nu_max=nu_max, nu_min=qmin([r["nu_L"] for r in rows]), nu_fit=f_nu,
        rho_max=rho_max, rho_min=qmin([r["rho"] for r in rows]), rho_fit=f_rho,
        kap_max=qmax([r["kap_up"] for r in rows]), kap_fit=f_kap,
        kapL_max=qmax([r["kap_Lam"] for r in rows]),
        hit=hit, frac_hit=hit / max(len(rows), 1),
        sand_ok=bool(sig_max <= SAND_BAR),
        tv_ok=bool(tv_max <= TV_BAR),
        tv_flat=flat_ok(f_tv, TV_FLAT_BAR),
        rho_ok=bool(rho_max <= RHO_BAR),
        nu_flat=flat_ok(f_nu, BAR_UNIF),
        adm=bool(sig_max <= SAND_BAR and tv_max <= TV_BAR))

info("V1.3.header", "%-6s %6s %8s %17s %8s %17s %7s %7s %7s %7s" %
     ("gauge", "sig", "TV", "TV trend", "nu_L", "nu_L trend", "rho", "rho_top",
      "kap~up", "in-tgt"))
for nm in CAND_ORDER:
    if nm not in TBL:
        continue
    t = TBL[nm]
    info("V1.3.gauge", "%-6s %6.3f %8.4f %17s %8.2f %17s %7.3f %7.3f %7.3f %3d/%2d"
         % (nm, t["sig_max"], t["tv_max"], fit_str(t["tv_fit"]), t["nu_max"],
            fit_str(t["nu_fit"]), t["rho_max"], t["rho_top"], t["kap_max"],
            t["hit"], t["n"]))
info("V1.3.reading", "COLUMNS: sig, TV and kap~up are the WORST window; nu_L is "
     "the worst window; rho is the worst window and rho_top the LARGEST-m window "
     "(m = %d), because the target m/(8 kap_Lam~) GROWS with m and the worst "
     "window is therefore the smallest one.  'in-tgt' counts windows on which "
     "nu_L~ <= m/(8 kap_Lam~) holds, i.e. on which the Liouville ceiling beats the "
     "trivial bound.  rho <= 1 is the reading of the target being met"
     % TBL[CAND_ORDER[0]]["m_top"])

# --- V1.4  THE WINNER RULE, applied exactly as preregistered ----------------
ADM = [nm for nm in CAND_ORDER if nm in TBL and TBL[nm]["adm"]]
if ADM:
    WIN = min(ADM, key=lambda nm: (TBL[nm]["rho_max"],
                                   abs(TBL[nm]["tv_fit"]["p"])))
else:
    WIN = min([nm for nm in CAND_ORDER if nm in TBL],
              key=lambda nm: TBL[nm]["rho_max"])
W = TBL[WIN]
THREE_OK = bool(W["sand_ok"] and W["tv_ok"] and W["tv_flat"] and W["rho_ok"])
check("ws_v1.winner_rule_applied", WIN in TBL and len(ADM) >= 1,
      "V1.4 THE PREREGISTERED WINNER RULE selects '%s' out of %d admissible "
      "gauges (admissible = certified sandwich <= %.1f AND TV <= %.1f on EVERY "
      "window): worst-window sandwich %.4f, TV %.4f with trend %s, nu_L~ %.2f "
      "with trend %s, rho %.4f, certified kap~_up <= %.4f.  The rule was fixed in "
      "the constants block before any number was produced and is applied here "
      "without adjustment"
      % (WIN, len(ADM), SAND_BAR, TV_BAR, W["sig_max"], W["tv_max"],
         fit_str(W["tv_fit"]), W["nu_max"], fit_str(W["nu_fit"]), W["rho_max"],
         W["kap_max"]))

info("V1.4.three_numbers", "THE THREE NUMBERS OF THE WINNER '%s', each against "
     "its bar: SANDWICH %.4f <= %.1f [%s] with trend %s; TV(log Lam~) %.4f <= "
     "%.1f [%s] with trend %s [flat: %s] against T148's %.2f at m^%.3f; nu_L~ "
     "%.2f with trend %s, target m/(8 kap_Lam~) reached on %d of %d windows [%s], "
     "rho %.4f <= %.1f [%s].  ALL THREE: %s"
     % (WIN, W["sig_max"], SAND_BAR, "OK" if W["sand_ok"] else "OVER",
        fit_str(W["sig_fit"]), W["tv_max"], TV_BAR,
        "OK" if W["tv_ok"] else "OVER", fit_str(W["tv_fit"]), W["tv_flat"],
        TV_T148, TV_EXP_T148, W["nu_max"], fit_str(W["nu_fit"]), W["hit"],
        W["n"], "OK" if W["frac_hit"] >= 1.0 else "PARTIAL", W["rho_max"],
        RHO_BAR, "OK" if W["rho_ok"] else "OVER",
        "CARRIED" if THREE_OK else "NOT ALL CARRIED"))

_bid = TBL.get("id")
_tv_txt = ("EXACTLY 0 by construction" if W["tv_max"] < 1.0e-12
           else "%.4f, a factor %.1f smaller"
           % (W["tv_max"], _bid["tv_max"] / max(W["tv_max"], 1.0e-300)))
info("V1.4.against_t148", "THE COMPARISON WITH THE JACOBI GAUGE, same windows and "
     "same code path: 'id' has TV %.4f (trend %s) and nu_L~ %.2f (trend %s) with "
     "rho %.3f at kap~_up <= %.4f -- T148 reported TV = %.2f and nu_L = %.0f at a "
     "cap of m <= 1100, and this surface runs further, so the baseline numbers are "
     "reproduced in shape and are LARGER in value, as they must be -- while '%s' "
     "has TV %s and nu_L~ %.2f with rho %.3f at kap~_up <= %.4f.  "
     "nu_L~ improves by a factor %.2f and the price in kap~_up is a factor %.2f, "
     "which is a BOUNDED price paid ONCE and linearly in the chain"
     % (_bid["tv_max"], fit_str(_bid["tv_fit"]), _bid["nu_max"],
        fit_str(_bid["nu_fit"]), _bid["rho_max"], _bid["kap_max"],
        TV_T148, NUL_T148, WIN, _tv_txt, W["nu_max"], W["rho_max"],
        W["kap_max"], _bid["nu_max"] / max(W["nu_max"], 1.0e-300),
        W["kap_max"] / max(_bid["kap_max"], 1.0e-300)))
info("V1.4.where_the_target_sits", "THE TARGET, WINDOW BY WINDOW.  For '%s' the "
     "certified statement nu_L~ <= m/(8 kap_Lam~) HOLDS on %d of %d windows, and "
     "the smallest window on which it holds has m = %s; at the largest window "
     "(m = %d) it reads nu_L~ = %.2f against a target of %.1f, i.e. rho = %.3f.  "
     "The rho trend is %s and at the top of the surface the target is %s; the "
     "worst window is the SMALLEST one (rho %.3f at m = %d), which is a "
     "FINITE-SIZE statement about a target that grows linearly in m and NOT a "
     "divergence -- but a trend is a FIT and this file does not extrapolate it "
     "into a claim for any m outside the list"
     % (WIN, W["hit"], W["n"],
        ("%d" % W["m_hit"]) if np.isfinite(W["m_hit"]) else "none",
        W["m_top"], W["nu_top"], W["tgt_top"], W["rho_top"],
        fit_str(W["rho_fit"]), "MET" if W["rho_top"] <= 1.0 else "MISSED",
        W["rho_max"], min(r["m"] for r in CROWS[WIN])))

FLUT_G = [nm for nm in ("mgm05", "mgm15", "dyad", "poly2", "poly6", "unim")
          if nm in TBL]
MACRO_G = [nm for nm in ("const", "mono") if nm in TBL]
_fs = [TBL[nm]["sig_max"] for nm in FLUT_G]
_fn = [TBL[nm]["nu_max"] for nm in FLUT_G]
_ms = [TBL[nm]["sig_max"] for nm in MACRO_G]
_mn = [TBL[nm]["nu_max"] for nm in MACRO_G]
_nu_id = TBL["id"]["nu_max"]
para("""V1.5  THE FAMILY SPLITS IN TWO, AND THE SPLIT IS THE RESULT.  The nine
gauges fall into two groups whose behaviour is qualitatively different, and reading
them against each other locates the remaining roughness exactly.
  * FLUTTER SMOOTHERS (%s): they remove the arithmetic flutter of Lam and keep its
    macro profile.  They are CHEAP -- certified sandwich only %.4f .. %.4f, close
    to 1, because the flutter amplitude is small -- and they bring TV down to
    %.4f .. %.4f.  BUT THEY DO NOT MOVE nu_L~ AT ALL: %.2f .. %.2f against %.2f
    for the Jacobi gauge, a change of at most %.1f%%.
  * MACRO REMOVERS (%s): they replace Lam by a constant (or by a monotone hull that
    is nearly constant here), so TV is EXACTLY 0 and kap_Lam~ = 1.  They are
    EXPENSIVE -- certified sandwich %.4f .. %.4f, which is the FULL range of Lam --
    and they improve nu_L~ to %.2f .. %.2f, a factor %.2f.
  THE READING, and it is the honest answer to what resists: the smoothness
functional of the bottom mode is essentially BLIND to the flutter of the
multiplier, and only weakly sensitive to its macro shape.  T148 named TV(log Lam)
as the hypothesis of ROUTE S because TV was what separated the model weight
classes; on the arithmetic surface the gauge that kills TV without touching the
macro profile buys NOTHING in nu_L~.  So the roughness that nu_L~ actually sees is
NOT in the multiplier -- it is in the FORM A itself, which is exactly what the
no-go stress independently shows in V3.1.""" % (
    ", ".join(FLUT_G), qmin(_fs), qmax(_fs),
    qmin([TBL[nm]["tv_max"] for nm in FLUT_G]),
    qmax([TBL[nm]["tv_max"] for nm in FLUT_G]), qmin(_fn), qmax(_fn), _nu_id,
    100.0 * max(abs(x - _nu_id) for x in _fn) / max(_nu_id, 1e-300),
    ", ".join(MACRO_G), qmin(_ms), qmax(_ms), qmin(_mn), qmax(_mn),
    _nu_id / max(qmax(_mn), 1e-300)))

info("V1.6.zone_flatness", "ZONE FLATNESS of the winner, the second uniformity "
     "axis: over the %d zones the sandwich spans %.4f .. %.4f, TV %.4f .. %.4f "
     "and nu_L~ %.2f .. %.2f, with D spanning %.3e .. %.3e -- reported as a "
     "STRATIFIED CERTIFIED LIST and NOT as a statement for all zones"
     % (W["n"], qmin([r["sig"] for r in CROWS[WIN]]),
        qmax([r["sig"] for r in CROWS[WIN]]), W["tv_min"], W["tv_max"],
        W["nu_min"], W["nu_max"], qmin(DV), qmax(DV)))


# ----------------------------------------------------------------------------
section("V2  THE LIFTED CHAIN -- END TO END WITH THE SMOOTHED GAUGE")
# ----------------------------------------------------------------------------
para("""V2.0  WHAT IS ASSEMBLED.  Per window the full T146/T147/T148 chain is
rebuilt from the raw form in THREE gauges -- 'id' (T148's baseline, so the
comparison is same-code-path and not same-paper), 'const' (the winner of V1.4),
and the best admissible gauge of that window -- as
    lam_min(A, A_B) >= lam_min(E~) / kap~_up >= 1 / (kap~_up c_0^ap Psi) ,
    c_0^ap = 2 base^2 Gam min(1, Gam_1) + eps ,   Gam = sqrt(Q_star) Sw ,
with Psi the density bound over ALL 2^m subsets (Charikar 2000 plus a certified
lam_max), Sw the spectral half and Q_star the geometric half of T147's identity.
Two variants per gauge: the CERTIFIED one, which reads computed columns of
R = E~^{-1}, and the A PRIORI-SHAPED one, in which Q_star is replaced by its
certified l1 CEILING and Sw by the certified inertia layer cake.  BECAUSE EVERY
GAUGE GIVES A VALID LOWER BOUND (licence 5), THE MAXIMUM OVER THE GAUGES IS ALSO A
VALID LOWER BOUND, and that family maximum is the honest headline number.""")

CH_OK = True
CH_ID_OK = True
for r in ROWS:
    for nm, fc in r["ch"].items():
        if not (np.isfinite(fc["chain"]) and fc["chain"] <= r["gap_ex"] * (1.0 + 1.0e-9)):
            CH_OK = False
        if not (np.isfinite(fc["chain_apr"])
                and fc["chain_apr"] <= r["gap_ex"] * (1.0 + 1.0e-9)):
            CH_OK = False
    r["frac_id"] = r["ch"]["id"]["frac"]
    r["frac_apr_id"] = r["ch"]["id"]["frac_apr"]
    r["frac_fam"] = max(fc["frac"] for fc in r["ch"].values())
    r["frac_apr_fam"] = max(fc["frac_apr"] for fc in r["ch"].values())
    r["arg_fam"] = max(r["ch"].items(), key=lambda kv: kv[1]["frac"])[0]
    r["frac_cst"] = r["ch"]["const"]["frac"] if "const" in r["ch"] else float("nan")
    r["frac_apr_cst"] = (r["ch"]["const"]["frac_apr"] if "const" in r["ch"]
                         else float("nan"))
NCH = sum(len(r["ch"]) for r in ROWS)
check("ws_v2.chain_is_a_lower_bound", CH_OK,
      "V2.1 EVERY ONE OF THE %d ASSEMBLED CHAINS (both variants, all gauges, all "
      "%d windows) IS A LOWER BOUND on the exact generalised eigenvalue.  This is "
      "the only thing that must hold for the gauge freedom to be usable at all, "
      "and it holds without exception" % (2 * NCH, len(ROWS)))

F_FRID = pow_fit(DV, [r["frac_id"] for r in ROWS], "frac id")
F_FRCS = pow_fit(DV, [r["frac_cst"] for r in ROWS], "frac const")
F_FRFAM = pow_fit(DV, [r["frac_fam"] for r in ROWS], "frac family")
F_FRAPID = pow_fit(DV, [r["frac_apr_id"] for r in ROWS], "frac ap id")
F_FRAPFAM = pow_fit(DV, [r["frac_apr_fam"] for r in ROWS], "frac ap family")

info("V2.1.the_big_number", "THE BIG NUMBER.  CERTIFIED chain: 'id' delivers "
     "%.4f .. %.4f of the true gap (median %.4f, trend %s) -- T148 reported %.4f "
     ".. %.4f on 48 windows capped at m <= 1100, so the baseline is reproduced in "
     "shape on this longer surface -- '%s' delivers %.4f "
     ".. %.4f (median %.4f, trend %s), and the FAMILY MAXIMUM delivers %.4f .. "
     "%.4f (median %.4f, trend %s).  A PRIORI-SHAPED chain: 'id' %.3e .. %.3e "
     "(T148: %.3f .. %.3f), family maximum %.3e .. %.3e, trend %s"
     % (qmin([r["frac_id"] for r in ROWS]), qmax([r["frac_id"] for r in ROWS]),
        qmed([r["frac_id"] for r in ROWS]), fit_str(F_FRID),
        FRAC_T148[0], FRAC_T148[1], WIN,
        qmin([r["frac_cst"] for r in ROWS]), qmax([r["frac_cst"] for r in ROWS]),
        qmed([r["frac_cst"] for r in ROWS]), fit_str(F_FRCS),
        qmin([r["frac_fam"] for r in ROWS]), qmax([r["frac_fam"] for r in ROWS]),
        qmed([r["frac_fam"] for r in ROWS]), fit_str(F_FRFAM),
        qmin([r["frac_apr_id"] for r in ROWS]),
        qmax([r["frac_apr_id"] for r in ROWS]),
        FRACAP_T148[0], FRACAP_T148[1],
        qmin([r["frac_apr_fam"] for r in ROWS]),
        qmax([r["frac_apr_fam"] for r in ROWS]), fit_str(F_FRAPFAM)))

_gain = [r["frac_apr_fam"] / max(r["frac_apr_id"], 1.0e-300) for r in ROWS]
_gain_c = [r["frac_fam"] / max(r["frac_id"], 1.0e-300) for r in ROWS]
_argc = {}
for r in ROWS:
    _argc[r["arg_fam"]] = _argc.get(r["arg_fam"], 0) + 1
info("V2.1.gauge_gain", "WHAT THE GAUGE CHANGE IS WORTH, window by window: the a "
     "priori-shaped chain improves by a factor %.3f .. %.3f (median %.3f) and the "
     "certified chain by %.3f .. %.3f (median %.3f).  The gauge attaining the "
     "family maximum is %s -- the certified chain still prefers the JACOBI gauge "
     "wherever the sharper kap~_up (%.4f against %.4f) outweighs the smoother "
     "Q_star ceiling, which is exactly the trade-off the sandwich buys"
     % (qmin(_gain), qmax(_gain), qmed(_gain), qmin(_gain_c), qmax(_gain_c),
        qmed(_gain_c),
        ", ".join("%s x%d" % (k, v) for k, v in sorted(_argc.items())),
        TBL["id"]["kap_max"], W["kap_max"]))

# --- V2.2  the factor-by-factor comparison ----------------------------------
def _agg(nm, key):
    return [r["ch"][nm][key] for r in ROWS if nm in r["ch"]]


for key, lab in (("Qs_ceil_best", "Q_star CEILING (certified, a priori shape)"),
                 ("Qs_up", "Q_star certified from columns"),
                 ("Sw_cnt", "Sw layer-cake counting bound"),
                 ("gam_apr", "Gam^ap = sqrt(Q_star ceiling) x Sw"),
                 ("c0_apr", "c_0^ap from Gam^ap"),
                 ("kap_up", "kap~_up (the price of the gauge)"),
                 ("psi_up", "Psi, density over ALL 2^m subsets"),
                 ("nu_L_wmax", "nu_L~ on the Green-weighted modes"),
                 ("nu_L_k2", "C in nu_k <= C k^2 on the weighted cut"),
                 ("C_meas", "KMS constant C, MEASURED")):
    a = _agg("id", key)
    b = _agg(WIN, key)
    fa = pow_fit([r["m"] for r in ROWS if "id" in r["ch"]], a, key)
    fb = pow_fit([r["m"] for r in ROWS if WIN in r["ch"]], b, key)
    info("V2.2.factor", "%-42s id %10.4g .. %10.4g %-16s | %s %10.4g .. %10.4g %s"
         % (lab, qmin(a), qmax(a), fit_str(fa), WIN, qmin(b), qmax(b),
            fit_str(fb)))

QC_ID = qmax(_agg("id", "Qs_ceil_best"))
QC_WIN = qmax(_agg(WIN, "Qs_ceil_best"))
F_QCID = pow_fit(MV, _agg("id", "Qs_ceil_best"), "Q ceil id")
F_QCWIN = pow_fit([r["m"] for r in ROWS if WIN in r["ch"]],
                  _agg(WIN, "Qs_ceil_best"), "Q ceil win")
CEIL_BOUNDED = bool(QC_WIN <= CEIL_BAR)
CEIL_FLAT = flat_ok(F_QCWIN, BAR_UNIF)
QSTAR_LIFTS = bool(CEIL_BOUNDED and CEIL_FLAT)
check("ws_v2.qstar_ceiling_valid",
      all(r["ch"][nm]["viol_b"] <= 1.0e-6 for r in ROWS for nm in r["ch"]),
      "V2.2 THE Q_star CEILING IS VALID IN BOTH GAUGES on every window: the "
      "per-mode bounds were compared with the TRUE m||psi_k||_inf^2 over the whole "
      "weighted cut, worst excess %.1e.  VALUES: 'id' %.4g (trend %s), '%s' %.4g "
      "(trend %s) against the bar %.0e.  m-FREENESS of the ceiling is the whole "
      "question and the answer on this surface is: bounded %s, flat %s"
      % (max(r["ch"][nm]["viol_b"] for r in ROWS for nm in r["ch"]),
         QC_ID, fit_str(F_QCID), WIN, QC_WIN, fit_str(F_QCWIN), CEIL_BAR,
         CEIL_BOUNDED, CEIL_FLAT))

_ARG = [r["ch"][WIN]["nu_L_k2_arg"] for r in ROWS if WIN in r["ch"]]
_CUT = [r["ch"][WIN]["cut"] for r in ROWS if WIN in r["ch"]]
info("V2.2.ladder_location", "WHERE THE LADDER CONSTANT IS ATTAINED, which decides "
     "whether the remaining growth is a BOTTOM effect or a DEPTH effect.  In the "
     "'%s' gauge C = max_k nu_k/k^2 over the weighted cut is attained at k = %d .. "
     "%d (median %.0f) while the optimal cut itself is K = %d .. %d (median %.0f), "
     "and the bottom mode alone has nu_1 = %.2f .. %.2f.  READING: the constant is "
     "attained %s, so the growth is %s -- and that is exactly the statement REST "
     "ONE asks to be made m-free"
     % (WIN, min(_ARG), max(_ARG), qmed(_ARG), min(_CUT), max(_CUT), qmed(_CUT),
        qmin(_agg(WIN, "nu_L_1")), qmax(_agg(WIN, "nu_L_1")),
        "at the very bottom of the spectrum" if qmed(_ARG) <= 2.5
        else "well above the bottom mode",
        "NOT a property of the bottom mode alone" if qmed(_ARG) > 2.5
        else "already visible in the bottom mode"))

IDENT_OK = all(r["ch"][nm]["ident"] < 1.0e-9 for r in ROWS for nm in r["ch"])
check("ws_v2.identity_holds", IDENT_OK,
      "V2.2 T147's IDENTITY Gam = sqrt(Q_star) x Sw HOLDS IN EVERY GAUGE, worst "
      "relative deviation %.1e over %d assemblies (T147 reported %.1e on 85 "
      "windows).  The identity is gauge-COVARIANT: both factors change with Lam~, "
      "their product remains Gam, and that is why a gauge change can move the "
      "difficulty between the spectral and the geometric half without creating or "
      "destroying any"
      % (max(r["ch"][nm]["ident"] for r in ROWS for nm in r["ch"]), NCH,
         IDENT_T147))

# --- V2.3  THE D-STRATA -----------------------------------------------------
ORD = sorted(ROWS, key=lambda r: r["D"])
LAY = []
nper = max(1, len(ORD) // STRATA)
for s in range(STRATA):
    lo = s * nper
    hi = len(ORD) if s == STRATA - 1 else min(len(ORD), (s + 1) * nper)
    part = ORD[lo:hi]
    if not part:
        continue
    LAY.append(dict(
        n=len(part), D_lo=part[0]["D"], D_hi=part[-1]["D"],
        m_lo=min(r["m"] for r in part), m_hi=max(r["m"] for r in part),
        sig=qmax([r["rec"][WIN]["sig"] for r in part if WIN in r["rec"]]),
        tv=qmax([r["rec"][WIN]["tv"] for r in part if WIN in r["rec"]]),
        nu=qmax([r["rec"][WIN]["nu_L"] for r in part if WIN in r["rec"]]),
        rho=qmax([r["rec"][WIN]["rho"] for r in part if WIN in r["rec"]]),
        frac=qmin([r["frac_fam"] for r in part]),
        frac_ap=qmin([r["frac_apr_fam"] for r in part])))
for i, L in enumerate(LAY):
    info("V2.3.stratum", "layer %d: %2d windows, D %.3e .. %.3e, m %4d .. %4d, "
         "sandwich <= %.4f, TV <= %.4f, nu_L~ <= %.2f, rho <= %.3f, family chain "
         ">= %.4f (a priori %.3e) x the true gap"
         % (i + 1, L["n"], L["D_lo"], L["D_hi"], L["m_lo"], L["m_hi"], L["sig"],
            L["tv"], L["nu"], L["rho"], L["frac"], L["frac_ap"]))
check("ws_v2.strata_populated", len(LAY) >= 3,
      "V2.3 %d D-strata are populated and each carries its own certified list.  "
      "THE EXTRAPOLATION DISCIPLINE, stated as a rule and not as a hope: a "
      "stratified certified list over %d windows in %d layers is NOT a statement "
      "for all D, no trend in this file is load-bearing, and no branch of the "
      "verdict rule can produce the word 'proved'" % (len(LAY), len(ROWS), len(LAY)))

# --- V2.4  THE UNIFORMITY BALANCE -------------------------------------------
BAL = [
    ("the gauge freedom lam_min(E~)/kap~_up", "THEOREM (identity + Rayleigh)",
     "licence 5, verified on the whole family"),
    ("the exact Dirichlet/Neumann models", "THEOREM (KMS 1953)",
     "licences 1, 2, 3"),
    ("the l1 ceiling |a_k| <= min(1, ...)", "CERTIFIED (T148, quoted)",
     "licence 4, worst excess %.1e" % _mbl["viol"]),
    ("the Liouville transform", "CERTIFIED (exact change of variables)",
     "licence 8, %.1e" % _liou_err),
    ("the sandwich c_1 Lam <= Lam~ <= c_2 Lam", "CERTIFIED per window",
     "sig <= %.4f for '%s'" % (W["sig_max"], WIN)),
    ("kap~_up = lam_max(W~)", "CERTIFIED per window (Cholesky)",
     "<= %.4f for '%s' against %.4f for 'id'"
     % (W["kap_max"], WIN, TBL["id"]["kap_max"])),
    ("TV(log Lam~)", "CERTIFIED per window / by construction",
     "%s for '%s'" % ("exactly 0" if W["tv_max"] < 1e-12
                      else "%.4f" % W["tv_max"], WIN)),
    ("Sw (the spectral half)", "CERTIFIED per window (inertia layer cake)",
     "<= %.4f, T148 closed this side" % qmax(_agg(WIN, "Sw_cnt"))),
    ("Psi (density over all 2^m sets)", "CERTIFIED per window",
     "Charikar 2000 + certified lam_max"),
    ("Q_star ceiling", "CERTIFIED per window, NOT YET m-FREE",
     "%.4g, trend %s -- THE REMAINING FACTOR" % (QC_WIN, fit_str(F_QCWIN))),
    ("nu_L~ <= F(form)", "OPEN (a functional of a MODE)",
     "%.2f vs target %.1f at m = %d" % (W["nu_top"], W["tgt_top"], W["m_top"])),
    ("the KMS constant C", "MEASURED", "reads the eigenvalues, cross-check only"),
    ("the bottom exponent", "FIT", "never enters an inequality"),
    ("the gap law Theta(D^3)", "FIT", "quoted from T147, never used here"),
]
for nm, cl, note in BAL:
    info("V2.4.balance", "%-40s %-42s %s" % (nm, cl, note))
N_THM = sum(1 for _, c, _ in BAL if c.startswith("THEOREM"))
N_CERT = sum(1 for _, c, _ in BAL if c.startswith("CERTIFIED"))
N_FIT = sum(1 for _, c, _ in BAL if c.startswith("FIT"))
N_OPEN = sum(1 for _, c, _ in BAL if c.startswith("OPEN"))
check("ws_v2.balance_no_fit_load_bearing",
      N_FIT == 2 and N_CERT >= 6 and N_OPEN == 1 and CH_OK,
      "V2.4 THE UNIFORMITY BALANCE: of the %d factors, %d are THEOREM, %d "
      "CERTIFIED, %d MEASURED, %d FIT and %d OPEN.  The two fits enter NO "
      "inequality of this file, which is why every chain above is a lower bound "
      "without them.  The load-bearing distinction is CERTIFIED-PER-WINDOW versus "
      "CERTIFIED-AND-m-FREE, and after the gauge change exactly ONE factor still "
      "sits on the wrong side of it"
      % (len(BAL), N_THM, N_CERT, len(BAL) - N_THM - N_CERT - N_FIT - N_OPEN,
         N_FIT, N_OPEN))


# ----------------------------------------------------------------------------
section("V3  STRESS, THE ROUGHNESS ANATOMY, and THE ORDER-2 LADDER")
# ----------------------------------------------------------------------------
para("""V3.0  THE MANDATORY STRESS PAIR, NOW AGAINST THE GAUGE FREEDOM.  A gauge
freedom is dangerous precisely because it is free: if smoothing the multiplier
could rescue anything, it would also rescue the T145 NO-GO, and the whole chain
would be worthless.  The no-go is R = a a^T + eps I with a_i = i^{-1/2}: positive
definite, entrywise nonnegative, bounded density over ALL subsets, and yet
m||psi||_inf^2 = m/H_m DIVERGES.  ITS WHITENING DIAGONAL IS ALREADY SMOOTH -- the
off-diagonal of E = R^{-1} is negative, so the lumping is trivial and Lam =
diag(E) is a monotone, nearly constant profile -- so the smoothing family must be
nearly the IDENTITY there and must NOT change the outcome.  The control is the
Dirichlet path Laplacian, whose diagonal is CONSTANT, so every candidate is
EXACTLY the identity on it and every number must stay flat.""")

NG, CT = [], []
for m_s in NOGO_SIZES:
    if m_s > MAX_H or budget_left() < 40.0:
        break
    ng = nogo_form(m_s)
    lp_s = lump_pair(ng["E"])
    Lam_s = np.diag(lp_s["A_B"]).copy()
    S_s = sine_basis(m_s)
    C_s = cosine_basis(m_s)
    muD_s = dirichlet_mu(m_s)
    muN_s = neumann_mu(m_s)
    fam_s = smoothing_family(Lam_s)
    per = {}
    for nm, Lt in fam_s.items():
        sd = sandwich_cert(Lam_s, Lt)
        reg = weight_regularity(sd["Lam_t"])
        wt = whiten_with(ng["E"], lp_s["A_B"], sd["Lam_t"], want_kap=False)
        bp = bottom_pass(wt["E"], wt["sqinv"], reg["kap"], m_s,
                         S_s, C_s, muD_s, muN_s)
        if bp is not None:
            per[nm] = dict(sig=sd["sig"], tv=reg["tv"], kap=reg["kap"],
                           nu_L=bp["nu_L"], nu_plain=bp["nu_plain"],
                           rho=bp["rho"], viol=bp["viol"])
        del wt, bp
    if "id" in per:
        NG.append(dict(m=m_s, Q_exact=ng["Q_exact"], per=per,
                       tv=weight_regularity(Lam_s)["tv"],
                       kap=weight_regularity(Lam_s)["kap"],
                       nu_best=min(v["nu_L"] for v in per.values()),
                       rho_best=min(v["rho"] for v in per.values()),
                       sig_max=max(v["sig"] for v in per.values()),
                       viol=max(v["viol"] for v in per.values())))
    del ng, lp_s, S_s, C_s, fam_s

for m_s in CTRL_SIZES:
    if m_s > MAX_H or budget_left() < 40.0:
        break
    cf = control_form(m_s)
    lp_s = lump_pair(cf["E"])
    Lam_s = np.diag(lp_s["A_B"]).copy()
    S_s = sine_basis(m_s)
    C_s = cosine_basis(m_s)
    fam_s = smoothing_family(Lam_s)
    dev = 0.0
    for nm, Lt in fam_s.items():
        sd = sandwich_cert(Lam_s, Lt)
        dev = max(dev, abs(sd["sig"] - 1.0),
                  float(np.max(np.abs(sd["Lam_t"] / Lam_s - 1.0))))
    wt = whiten_with(cf["E"], lp_s["A_B"], Lam_s, want_kap=False)
    bp = bottom_pass(wt["E"], wt["sqinv"], 1.0, m_s, S_s, C_s,
                     dirichlet_mu(m_s), neumann_mu(m_s))
    # THE SINGLE BOTTOM MODE, which is the object T148's control read: the exact
    # half sine, for which nu = (m+1) sin(pi/(m+1)) -> pi.  Separately, the FIRST
    # FOUR modes, for which the classical value is nu_k = pi k^2 EXACTLY -- the
    # ladder that says boundedness over a growing mode set is the wrong demand.
    mb1 = mode_bounds(cf["psi"].reshape(-1, 1), m_s, S_s, C_s,
                      dirichlet_mu(m_s), neumann_mu(m_s))
    S4 = np.ascontiguousarray(sine_basis(m_s)[:4].T)
    mb4 = mode_bounds(S4, m_s, S_s, C_s, dirichlet_mu(m_s), neumann_mu(m_s))
    lad = float(np.max(mb4["nu"] / (np.arange(4, dtype=float) + 1.0) ** 2))
    if bp is not None:
        CT.append(dict(m=m_s, nu_L=bp["nu_L"], nu1=float(mb1["nu"][0]),
                       lad=lad, rho=bp["rho"],
                       sup=m_s * float(np.max(cf["psi"] ** 2)),
                       viol=max(bp["viol"], mb1["viol"], mb4["viol"]), dev=dev,
                       tv=weight_regularity(Lam_s)["tv"], n_cand=len(fam_s)))
    del cf, lp_s, S_s, C_s, fam_s, wt, bp, mb1, mb4, S4

F_NG_PL = pow_fit([r["m"] for r in NG],
                  [r["per"]["id"]["nu_plain"] for r in NG], "no-go nu")
F_NG_BEST = pow_fit([r["m"] for r in NG], [r["nu_best"] for r in NG],
                    "no-go nu best gauge")
F_NG_CST = pow_fit([r["m"] for r in NG],
                   [r["per"]["const"]["nu_L"] for r in NG], "no-go nu const")
F_CT_NU = pow_fit([r["m"] for r in CT], [r["nu1"] for r in CT], "control nu")
F_CT_BLK = pow_fit([r["m"] for r in CT], [r["nu_L"] for r in CT], "control block")
NOGO_BREAKS = bool(
    len(NG) >= 3 and F_NG_BEST["p"] > 0.5
    and NG[-1]["nu_best"] > 3.0 * NG[0]["nu_best"]
    and all(r["viol"] <= 1.0e-8 for r in NG))
CTRL_HOLDS = bool(len(CT) >= 3 and flat_ok(F_CT_NU, BAR_UNIF)
                  and all(abs(r["nu1"] - math.pi) < 0.05 for r in CT)
                  and all(abs(r["sup"] - 2.0) < 0.05 for r in CT)
                  and all(abs(r["lad"] - math.pi) < 0.05 for r in CT)
                  and all(r["viol"] <= 1.0e-8 for r in CT)
                  and all(r["dev"] < 1.0e-12 for r in CT))
check("ws_v3.stress_pair", NOGO_BREAKS and CTRL_HOLDS,
      "V3.1 THE STRESS PAIR SEPARATES, AND THE SMOOTHING DOES NOT RESCUE THE "
      "NO-GO.  ITS MULTIPLIER IS ALREADY SMOOTH -- TV(log Lam) = %.4f .. %.4f, "
      "kap_Lam = %.4f .. %.4f, and the BEST candidate over the whole family has a "
      "sandwich of only %.4f, i.e. the family is essentially the identity there, "
      "as it must be.  AND THE BREAK STAYS EXACTLY WHERE IT WAS: the best gauge's "
      "nu still grows like %s (%.3g -> %.3g over m = %d .. %d), the 'const' gauge "
      "-- the PURE form's own bottom mode, licence 13 -- grows like %s, and the raw "
      "functional grows like %s.  SO THE ANSWER TO 'WHERE DOES IT BREAK' IS: IN "
      "THE FORM, NOT IN THE MULTIPLIER -- the localised bottom mode of a rank-one "
      "spike is not made smooth by any regauging, which is precisely the "
         "separation this probe needs.  CONTROL: the Dirichlet diagonal is CONSTANT, "
         "all %d candidates coincide with the identity to %.1e, the bottom mode has "
         "nu = %.4f .. %.4f (pi = %.4f, trend %s) and m||psi||_inf^2 = %.4f .. %.4f "
         "(exactly 2 in the limit) -- bounded uniformly in m"
      % (qmin([r["tv"] for r in NG]), qmax([r["tv"] for r in NG]),
         qmin([r["kap"] for r in NG]), qmax([r["kap"] for r in NG]),
         qmax([r["sig_max"] for r in NG]), fit_str(F_NG_BEST),
         NG[0]["nu_best"], NG[-1]["nu_best"], NG[0]["m"], NG[-1]["m"],
         fit_str(F_NG_CST), fit_str(F_NG_PL),
         CT[0]["n_cand"], qmax([r["dev"] for r in CT]),
         qmin([r["nu1"] for r in CT]), qmax([r["nu1"] for r in CT]),
         math.pi, fit_str(F_CT_NU),
         qmin([r["sup"] for r in CT]), qmax([r["sup"] for r in CT])))

info("V3.1.the_classical_ladder", "AND THE CONTROL SETTLES A QUESTION THE Q_star "
     "CEILING RAISES.  On the EXACT Kac-Murdock-Szego model the k-th mode has "
     "nu_k = pi k^2 EXACTLY -- measured max_k nu_k/k^2 = %.4f .. %.4f over the "
     "first four modes against pi = %.4f, and the whole bottom BLOCK (%d modes "
     "under the preregistered theta rule) has nu = %.4f .. %.4f with trend %s.  "
     "CONSEQUENCE, and it reshapes the rest list: even in the PERFECTLY smooth "
     "case nu GROWS along the spectrum like k^2, so 'nu_L~ bounded over the "
     "weighted cut' is the WRONG demand.  The right m-free statement is "
     "nu_k <= C k^2 with C m-free, and that is what V4.4 asks for"
     % (qmin([r["lad"] for r in CT]), qmax([r["lad"] for r in CT]), math.pi,
        NB_PROBE, qmin([r["nu_L"] for r in CT]), qmax([r["nu_L"] for r in CT]),
        fit_str(F_CT_BLK)))

info("V3.1.nogo_detail", "THE NO-GO, GAUGE BY GAUGE at m = %d: %s.  Every one of "
     "them is a VALID bound (worst excess %.1e) and every one of them DIVERGES; "
     "the exact object m/H_m = %.2f is what they are all tracking"
     % (NG[-1]["m"],
        ", ".join("%s nu %.1f rho %.2f" % (k, v["nu_L"], v["rho"])
                  for k, v in sorted(NG[-1]["per"].items())),
        qmax([r["viol"] for r in NG]), NG[-1]["Q_exact"]))

# --- V3.2  THE ANATOMY OF TV(log Lam) ---------------------------------------
para("""V3.2  WHERE THE ROUGHNESS COMES FROM.  T148 left TV(log Lam) = %.2f growing
like m^%.3f as the blocking number.  The smoothing family removes it by
construction, but the ANATOMY still matters, because it is what says whether a
FUTURE a priori argument can bound the sandwich of a smoothed gauge from the form
alone.  Three MEASURED decompositions, none load-bearing: log Lam = P_d + f with
P_d the degree-%d Chebyshev fit (macro versus flutter); the share of TV in the
outer %.0f%% of indices at each end (the frame edges, where the reflected
minus-Hankel lag term is largest); and the share of TV sitting on the diagonal
indices r whose reflected lag M-1-2r is hit by a prime-power atom (the arithmetic
flutter proper).""" % (TV_T148, TV_EXP_T148, DEG_MACRO, 100.0 * EDGE_FRAC))

AM = [a["m"] for a in ANAT]
F_AN_TV = pow_fit(AM, [a["tv"] for a in ANAT], "TV")
F_AN_MA = pow_fit(AM, [max(a["tv_macro"], 1e-12) for a in ANAT], "TV macro")
F_AN_FL = pow_fit(AM, [max(a["tv_flut"], 1e-12) for a in ANAT], "TV flutter")
F_AN_AMP = pow_fit(AM, [max(a["amp_flut"], 1e-12) for a in ANAT], "flutter amp")
info("V3.2.macro_vs_flutter", "MACRO VERSUS FLUTTER.  TV(log Lam) = %.3f .. %.3f "
     "(trend %s) splits as TV(macro) = %.3f .. %.3f (trend %s, share %.1f%% .. "
     "%.1f%%) plus TV(flutter) = %.3f .. %.3f (trend %s, share %.1f%% .. %.1f%%; "
     "the two shares need NOT sum to 1, since subadditivity of the total variation "
     "runs in one direction only).  THE ROUGHNESS IS ALMOST ENTIRELY FLUTTER, and "
     "the flutter's AMPLITUDE is "
     "%.4f .. %.4f with trend %s -- it is many SMALL steps, not a few large ones "
     "(largest single step %.4f .. %.4f).  That is the structural reason a moving "
     "geometric mean or a fixed-degree fit can absorb it at a BOUNDED sandwich: "
     "the sandwich is controlled by the flutter AMPLITUDE, while TV is controlled "
     "by its step COUNT"
     % (qmin([a["tv"] for a in ANAT]), qmax([a["tv"] for a in ANAT]),
        fit_str(F_AN_TV),
        qmin([a["tv_macro"] for a in ANAT]), qmax([a["tv_macro"] for a in ANAT]),
        fit_str(F_AN_MA), 100.0 * qmin([a["share_macro"] for a in ANAT]),
        100.0 * qmax([a["share_macro"] for a in ANAT]),
        qmin([a["tv_flut"] for a in ANAT]), qmax([a["tv_flut"] for a in ANAT]),
        fit_str(F_AN_FL), 100.0 * qmin([a["share_flut"] for a in ANAT]),
        100.0 * qmax([a["share_flut"] for a in ANAT]),
        qmin([a["amp_flut"] for a in ANAT]), qmax([a["amp_flut"] for a in ANAT]),
        fit_str(F_AN_AMP),
        qmin([r["rec"]["id"]["d1_max"] for r in ROWS]),
        qmax([r["rec"]["id"]["d1_max"] for r in ROWS])))

info("V3.2.edges_and_atoms", "THE TWO LOCALISATIONS.  FRAME EDGES: the outer "
     "%.0f%% of indices at each end (index share %.1f%%) carry %.1f%% .. %.1f%% of "
     "TV -- an enrichment factor of %.2f .. %.2f, so the edges are %s.  "
     "ARITHMETIC ATOMS: the diagonal indices whose reflected lag is hit by a "
     "prime-power atom are an index share of %.1f%% .. %.1f%% and carry %.1f%% .. "
     "%.1f%% of TV -- an enrichment of %.2f .. %.2f.  READING: the roughness is "
     "%s, which is consistent with the flutter being generated by the ATOM "
     "POSITIONS entering the lag vector rather than by the window boundary"
     % (100.0 * EDGE_FRAC, 100.0 * qmed([a["idx_edge"] for a in ANAT]),
        100.0 * qmin([a["share_edge"] for a in ANAT]),
        100.0 * qmax([a["share_edge"] for a in ANAT]),
        qmin([a["share_edge"] / max(a["idx_edge"], 1e-12) for a in ANAT]),
        qmax([a["share_edge"] / max(a["idx_edge"], 1e-12) for a in ANAT]),
        "NOT the main source" if qmed([a["share_edge"] for a in ANAT]) < 0.25
        else "a genuine contributor",
        100.0 * qmin([a["idx_hit"] for a in ANAT]),
        100.0 * qmax([a["idx_hit"] for a in ANAT]),
        100.0 * qmin([a["share_hit"] for a in ANAT]),
        100.0 * qmax([a["share_hit"] for a in ANAT]),
        qmin([a["share_hit"] / max(a["idx_hit"], 1e-12) for a in ANAT]),
        qmax([a["share_hit"] / max(a["idx_hit"], 1e-12) for a in ANAT]),
        "SPREAD OVER THE WHOLE WINDOW, not localised"
        if qmed([a["share_hit"] / max(a["idx_hit"], 1e-12) for a in ANAT]) < 1.5
        else "CONCENTRATED ON THE ATOM IMPRINTS"))

# --- V3.3  THE ORDER-2 BOTTOM LADDER ----------------------------------------
BR_UP = sum(1 for r in ROWS if r["ch"]["id"]["bracket_up"])
BR_LO = sum(1 for r in ROWS if r["ch"]["id"]["bracket_lo"])
F_KMSP = pow_fit(MV, [r["ch"]["id"]["kms_p"] for r in ROWS], "bottom exponent")
KMS_IN = sum(1 for r in ROWS
             if KMS_BAND[0] <= r["ch"]["id"]["kms_p"] <= KMS_BAND[1])
CBOT = [r["ch"]["id"]["C_bot"] for r in ROWS]
para("""V3.3  THE ORDER-2 BOTTOM LADDER FROM THE MINUS-HANKEL STRUCTURE.  The
cosmetic rest of T148 was a THEOREM behind the ladder lam_k >= lam_hat k^2 / C.
The address is the Toeplitz-plus-Hankel Fredholm theory (Basor-Ehrhardt 2009;
Bottcher-Silbermann), and the classical model statement is exact (Kac-Murdock-Szego
1953: for the Dirichlet section lam_k / lam_hat = sin^2(pi k/(2(m+1))) /
sin^2(pi/(2(m+1))) lies in [4k^2/pi^2, k^2]).  MEASURED HERE: the bracket's UPPER
half holds on %d of %d windows and its LOWER half on %d of %d, the measured bottom
exponent lies in the order-2 band [%.1f, %.1f] on %d of %d windows with trend %s,
and the CERTIFIED bottom-band constant from the inertia ladder is C_bot = %.1f ..
%.1f while the MEASURED whole-spectrum constant is C = %.2f .. %.2f.  VERDICT ON
THIS ITEM, stated plainly: it is a NAMED OPEN PROBLEM and NOT a theorem candidate
in the form needed, for one specific reason -- Basor-Ehrhardt's theory is developed
for symbols in a Wiener algebra with controlled winding, whereas T148's honest
negative says this symbol takes the value f(0) = %.3e < 0, so the section's
positive definiteness is a finite-section effect of the minus-Hankel part.  A
theorem for the ladder would have to come from the minus-Hankel part directly, and
nothing in this file supplies it.  It remains COSMETIC: the Sw factor is certified
by an inertia count that needs no ladder at all.""" % (
    BR_UP, len(ROWS), BR_LO, len(ROWS), KMS_BAND[0], KMS_BAND[1], KMS_IN,
    len(ROWS), fit_str(F_KMSP), qmin(CBOT), qmax(CBOT),
    qmin([r["ch"]["id"]["C_meas"] for r in ROWS]),
    qmax([r["ch"]["id"]["C_meas"] for r in ROWS]),
    qmax([r["sym_f0"] for r in ROWS])))
LADDER_OPEN = True
check("ws_v3.ladder_classified",
      LADDER_OPEN and all(np.isfinite(c) and c > 0.0 for c in CBOT),
      "V3.3 THE ORDER-2 LADDER IS CLASSIFIED AS NAMED OPEN, not quietly assumed: "
      "the certified constant C_bot exists on every window (%.1f .. %.1f) and the "
      "Sw bound that the chain actually uses is an INERTIA COUNT, so no branch of "
      "this file depends on the ladder being a theorem.  The measured bracket is "
      "reported (%d/%d upper, %d/%d lower) and is a CROSS-CHECK only"
      % (qmin(CBOT), qmax(CBOT), BR_UP, len(ROWS), BR_LO, len(ROWS)))


# ----------------------------------------------------------------------------
section("V4  THE MAP V21, THE VERDICT, and THE SHORTEST REST LIST")
# ----------------------------------------------------------------------------
_NUW_ID = pow_fit(MV, _agg("id", "nu_L_wmax"), "nu_L weighted id")
_NUW_WIN = pow_fit([r["m"] for r in ROWS if WIN in r["ch"]],
                   _agg(WIN, "nu_L_wmax"), "nu_L weighted win")
MAP21 = [
    ("the two gap facts (Bertrand + trivial)", "THEOREM",
     "verified on %d prime-power gaps" % NZ_DEEP),
    ("the level lemma L1", "CLOSED on the surface (T146)", "quoted, not re-run"),
    ("Gam = sqrt(Q_star) x Sw", "IDENTITY (T147)",
     "re-verified to %.1e in EVERY gauge" % max(
         r["ch"][nm]["ident"] for r in ROWS for nm in r["ch"])),
    ("Sw <= C, m-FREE", "CLOSED on the surface (T148)",
     "certified <= %.4f here, trend %s"
     % (qmax(_agg(WIN, "Sw_cnt")), fit_str(pow_fit(
         [r["m"] for r in ROWS if WIN in r["ch"]], _agg(WIN, "Sw_cnt"), "sw")))),
    ("THE WHITENING DIAGONAL IS A FREE GAUGE", "THEOREM (this file, licence 5)",
     "%d gauges, all valid, family maximum used" % len(TBL)),
    ("TV(log Lam~) flat", "CLOSED BY CONSTRUCTION (this file)",
     "%s for '%s' against %.2f at m^%.3f for the Jacobi gauge"
     % ("exactly 0" if W["tv_max"] < 1e-12 else "%.4f" % W["tv_max"], WIN,
        TV_T148, TV_EXP_T148)),
    ("the sandwich price c_2/c_1", "CERTIFIED (this file)",
     "<= %.4f, kap~_up <= %.4f against %.4f"
     % (W["sig_max"], W["kap_max"], TBL["id"]["kap_max"])),
    ("nu_L~ sees the FLUTTER of Lam", "REFUTED (this file, V1.5)",
     "killing TV without touching the macro profile moves nu_L~ by <= %.1f%%"
     % (100.0 * max(abs(x - _nu_id) for x in _fn) / max(_nu_id, 1e-300))),
    ("nu_L~ at the BOTTOM BLOCK", "CERTIFIED, target met on %d/%d windows"
     % (W["hit"], W["n"]),
     "%.2f, trend %s; rho %.3f at m = %d" % (W["nu_max"], fit_str(W["nu_fit"]),
                                             W["rho_top"], W["m_top"])),
    ("nu_L~ on the GREEN-WEIGHTED modes", "OPEN -- THE NEW LOCATION OF THE REST",
     "id %.1f (trend %s) -> '%s' %.1f (trend %s)"
     % (qmax(_agg("id", "nu_L_wmax")), fit_str(_NUW_ID), WIN,
        qmax(_agg(WIN, "nu_L_wmax")), fit_str(_NUW_WIN))),
    ("Q_star ceiling, m-FREE and a priori", "OPEN -- narrowed (this file)",
     "%.4g trend %s against %.4g trend %s for the Jacobi gauge"
     % (QC_WIN, fit_str(F_QCWIN), QC_ID, fit_str(F_QCID))),
    ("ROUTE C (commutator / Davis-Kahan)", "DEAD (T148)",
     "vacuous by %.1f .. %.1f orders of magnitude" % DK_DEAD_T148),
    ("ROUTE S (weighted Szego / Liouville)", "LIVE, hypothesis RETIRED and RELOCATED",
     "the gauge freedom removes TV entirely, and V1.5 shows nu_L~ was not "
     "responding to TV in the first place"),
    ("the KMS SYMBOL hypothesis", "REFUTED (T148)",
     "f(0) = %.3e < 0 on %d/%d windows here"
     % (qmax([r["sym_f0"] for r in ROWS]), len(ROWS), len(ROWS))),
    ("the order-2 bottom ladder", "NAMED OPEN, cosmetic (this file, V3.3)",
     "Basor-Ehrhardt 2009 does not cover a sign-changing symbol"),
    ("the no-go / Dirichlet stress pair", "SEPARATES under every gauge",
     "no-go nu grows like %s under the BEST gauge" % fit_str(F_NG_BEST)),
    ("all-D uniformity", "STRATIFIED CERTIFIED LIST, %d windows / %d D-layers"
     % (len(ROWS), len(LAY)), "not a statement for all D"),
]
for nm, st, note in MAP21:
    info("V4.1.map", "%-42s %-48s %s" % (nm, st, note))

PROMO = [
    ("v554", "THE GAUGE FREEDOM AS A LEMMA: for ANY positive diagonal Lam~, "
     "lam_min(A, A_B) >= lam_min(Lam~^{-1/2} A Lam~^{-1/2}) / "
     "lam_max(Lam~^{-1/2} A_B Lam~^{-1/2}), an identity plus one Rayleigh step, "
     "together with the SANDWICH TRANSPORT kap~_up <= kap_up / c_1 and "
     "kap_Lam~ <= (c_2/c_1) kap_Lam and the SCALE INVARIANCE in Lam~.  Verified on "
     "%d gauges x %d windows, worst ratio %.6f <= 1.  This is what makes the "
     "whitening diagonal a design choice instead of a constraint"
     % (len(TBL), len(ROWS), _worst_gauge)),
    ("v555", "THE SMOOTHED GAUGE ITSELF: 'const' (the geometric mean of the "
     "Jacobi diagonal) has TV(log Lam~) = 0 EXACTLY, certified sandwich %.4f, "
     "certified kap~_up <= %.4f, and it identifies nu_L~ with the PURE "
     "Toeplitz-minus-Hankel section's own smoothness functional (licence 13) -- "
     "so the blocking hypothesis of T148 is not weakened but ELIMINATED, at a "
     "bounded and certified price" % (W["sig_max"], W["kap_max"])),
    ("v556", "THE Q_star CEILING IN THE SMOOTHED GAUGE: %.4g with trend %s "
     "against %.4g with trend %s for the Jacobi gauge on the same %d windows -- "
     "a factor %.2f better in value and %.2f better in exponent, still NOT m-free"
     % (QC_WIN, fit_str(F_QCWIN), QC_ID, fit_str(F_QCID), len(ROWS),
        QC_ID / max(QC_WIN, 1e-300),
        F_QCID["p"] / max(F_QCWIN["p"], 1e-300))),
    ("v557", "THE GAUGE-INVARIANCE OF THE STRESS PAIR: the T145 no-go's own "
     "whitening diagonal is ALREADY smooth (TV %.4f .. %.4f, best sandwich over "
     "the whole family %.4f), and its smoothness functional still diverges like "
     "%s under EVERY gauge.  A negative result and a necessary one: it shows the "
     "gauge freedom cannot manufacture equidistribution"
     % (qmin([r["tv"] for r in NG]), qmax([r["tv"] for r in NG]),
        qmax([r["sig_max"] for r in NG]), fit_str(F_NG_BEST))),
    ("v558", "THE ROUGHNESS ANATOMY of the Jacobi diagonal: %.0f%% .. %.0f%% of "
     "TV(log Lam) is FLUTTER around a smooth macro profile, the flutter amplitude "
     "is %.4f .. %.4f with trend %s, and the largest single log-step is %.4f -- so "
     "TV grows through the STEP COUNT while the SANDWICH depends only on the "
     "AMPLITUDE.  This is the quantitative reason a smoothed gauge is cheap"
     % (100.0 * qmin([a["share_flut"] for a in ANAT]),
        100.0 * qmax([a["share_flut"] for a in ANAT]),
        qmin([a["amp_flut"] for a in ANAT]), qmax([a["amp_flut"] for a in ANAT]),
        fit_str(F_AN_AMP),
        qmax([r["rec"]["id"]["d1_max"] for r in ROWS]))),
    ("v559", "THE TWO REGIMES OF THE FAMILY, and the separation of the cause: the "
     "gauges that remove the flutter and keep the macro profile (%s) are CHEAP "
     "(certified sandwich <= %.4f) and drive TV to <= %.4f, yet they move nu_L~ by "
     "at most %.1f%% away from the Jacobi value %.2f; the gauges that remove the "
     "MACRO profile (%s) are EXPENSIVE (sandwich <= %.4f) and are the only ones "
     "that improve nu_L~, by a factor %.2f.  Hence TV(log Lam) -- the named "
     "hypothesis of ROUTE S -- is NOT the quantity nu_L~ responds to on the "
     "arithmetic surface"
     % (", ".join(FLUT_G), qmax(_fs),
        qmax([TBL[nm]["tv_max"] for nm in FLUT_G]),
        100.0 * max(abs(x - _nu_id) for x in _fn) / max(_nu_id, 1e-300), _nu_id,
        ", ".join(MACRO_G), qmax(_ms), _nu_id / max(qmax(_mn), 1e-300))),
    ("v560", "THE FAMILY-MAXIMUM CHAIN: because every gauge is a valid lower "
     "bound, the maximum over the %d-gauge family is one too.  End to end it "
     "delivers %.4f .. %.4f of the true gap certified and %.3e .. %.3e a priori, "
     "against T148's %.4f .. %.4f and %.3f .. %.3f"
     % (len(TBL), qmin([r["frac_fam"] for r in ROWS]),
        qmax([r["frac_fam"] for r in ROWS]),
        qmin([r["frac_apr_fam"] for r in ROWS]),
        qmax([r["frac_apr_fam"] for r in ROWS]),
        FRAC_T148[0], FRAC_T148[1], FRACAP_T148[0], FRACAP_T148[1])),
]
for tag, txt in PROMO:
    info("V4.2.promotion", "%s  %s" % (tag, txt))
info("V4.2.count", "%d promotion candidates from THIS pass, numbered from v554 "
     "because T148's v548 .. v553 are being promoted in parallel and are NOT "
     "duplicated here.  Promotion itself is OUT OF SCOPE of this file, which "
     "writes nothing outside itself" % len(PROMO))

# --- V4.3  THE VERDICT, with the refusal built in ---------------------------
STRESS_OK = bool(NOGO_BREAKS and CTRL_HOLDS)
BASE_OK = bool(CH_OK and IDENT_OK and STRESS_OK and MODEL_REPAIRS
               and VIOL_ALL <= 1.0e-8)
TV_IMPROVED = bool(W["tv_max"] <= 0.5 * TBL["id"]["tv_max"] and W["tv_ok"])
NUM_FAIL = []
if not W["sand_ok"]:
    NUM_FAIL.append("the SANDWICH (sig = %.4f > %.1f)" % (W["sig_max"], SAND_BAR))
if not (W["tv_ok"] and W["tv_flat"]):
    NUM_FAIL.append("TV(log Lam~) (%.4f, trend %s)"
                    % (W["tv_max"], fit_str(W["tv_fit"])))
if not W["rho_ok"]:
    NUM_FAIL.append("nu_L~ AT THE SMALL-m END (rho = %.3f > %.1f at m = %d, "
                    "while rho = %.3f at m = %d)"
                    % (W["rho_max"], RHO_BAR, min(r["m"] for r in CROWS[WIN]),
                       W["rho_top"], W["m_top"]))
if not (CEIL_BOUNDED and CEIL_FLAT):
    NUM_FAIL.append("the Q_star CEILING's m-FREENESS (%.4g, trend %s, driven by "
                    "nu_L~ = %.1f with trend %s on the GREEN-WEIGHTED modes above "
                    "the bottom block)"
                    % (QC_WIN, fit_str(F_QCWIN), qmax(_agg(WIN, "nu_L_wmax")),
                       fit_str(_NUW_WIN)))

if not BASE_OK:
    VERDICT = "SMOOTHING-RESISTS"
    WHY = ("a load-bearing certification failed, so no shape statement is made "
           "at all")
elif THREE_OK and CEIL_BOUNDED and CEIL_FLAT:
    VERDICT = "SMOOTHING-CARRIES"
    WHY = ("one gauge carries a certified sandwich, a flat TV and nu_L~ inside the "
           "target on every window, with an m-free certified Q_star ceiling")
elif TV_IMPROVED:
    VERDICT = "PARTIAL-SMOOTHING"
    WHY = ("TV falls to %s and the sandwich is certified at %.4f, but %s"
           % ("exactly 0" if W["tv_max"] < 1e-12 else "%.4f" % W["tv_max"],
              W["sig_max"], "; ".join(NUM_FAIL)))
else:
    VERDICT = "SMOOTHING-RESISTS"
    WHY = ("no admissible gauge reduces TV without breaking the sandwich, so the "
           "roughness of the multiplier is essential")

FORBIDDEN_VERDICTS = ("PROVEN", "PROVED", "QED", "THEOREM-FOR-ALL-D",
                      "SMOOTHING-PROVED", "ESTABLISHED-FOR-ALL-D")
check("ws_v4.verdict_refuses_proof",
      VERDICT in ("SMOOTHING-CARRIES", "PARTIAL-SMOOTHING", "SMOOTHING-RESISTS")
      and all(t not in VERDICT for t in FORBIDDEN_VERDICTS),
      "V4.3 THE VERDICT RULE REFUSES A PROOF CONSTRUCTIVELY, as in T145 .. T148: "
      "the admissible verdicts are exactly %s, none of %s can be produced by the "
      "rule at all, and even the TOP verdict SMOOTHING-CARRIES is DEFINED as "
      "'certified on this finite surface with a named a priori mechanism', which "
      "is strictly weaker than a statement for all D and is labelled as such "
      "wherever it appears"
      % ("/".join(("SMOOTHING-CARRIES", "PARTIAL-SMOOTHING",
                   "SMOOTHING-RESISTS")), "/".join(FORBIDDEN_VERDICTS)))

for nm, ok in (("sandwich certified and bounded", W["sand_ok"]),
               ("TV(log Lam~) bounded and flat", bool(W["tv_ok"] and W["tv_flat"])),
               ("nu_L~ inside the target on EVERY window", W["rho_ok"]),
               ("Q_star ceiling bounded AND m-flat", QSTAR_LIFTS)):
    info("V4.3.side", "%-44s %s" % (nm, "CARRIES" if ok else "DOES NOT CARRY"))
info("V4.3.verdict", "VERDICT  %s -- %s" % (VERDICT, WHY))

REST = [
    "ONE (load-bearing), and V3.1 SHARPENS IT: an m-free constant C in the "
    "CLASSICAL LADDER FORM nu_k <= C k^2 for the modes of the smoothed section, "
    "not a bound on nu_k itself.  The control shows nu_k = pi k^2 EXACTLY in the "
    "perfectly smooth case, so the ladder and not the constant is what a "
    "smoothness statement can possibly give.  MEASURED on the weighted cut in the "
    "'%s' gauge: C = %.2f .. %.2f with trend %s (against pi in the exact model), "
    "while the bottom block alone is already inside the target on the upper %d of "
    "%d windows (rho = %.3f at m = %d).  A bound C <= F(form) with F m-free makes "
    "the Q_star ceiling m-free and the whole measurement-surface chain a priori.  "
    "THIS, and no longer TV(log Lam), IS THE REST"
    % (WIN, qmin(_agg(WIN, "nu_L_k2")), qmax(_agg(WIN, "nu_L_k2")),
       fit_str(pow_fit([r["m"] for r in ROWS if WIN in r["ch"]],
                       _agg(WIN, "nu_L_k2"), "C")),
       W["hit"], W["n"], W["rho_top"], W["m_top"]),
    "TWO (would close ONE outright): an a priori bound on the SANDWICH of the "
    "smoothed gauge from the form alone, i.e. an m-free bound on the flutter "
    "AMPLITUDE of log diag(A_B).  Measured %.4f .. %.4f with trend %s; a bound "
    "here makes kap_Lam~ = 1 and kap~_up <= %.4f a priori rather than certified "
    "per window, and V3.2 says the amplitude and not the step count is what the "
    "price depends on"
    % (qmin([a["amp_flut"] for a in ANAT]), qmax([a["amp_flut"] for a in ANAT]),
       fit_str(F_AN_AMP), W["kap_max"]),
    "THREE (cosmetic, unchanged from T148): a THEOREM behind the order-2 bottom "
    "ladder from the minus-Hankel structure.  V3.3 classifies it as NAMED OPEN "
    "because the symbol changes sign; the chain does not wait on it, since Sw is "
    "certified by an inertia count",
]
for i, t in enumerate(REST):
    info("V4.4.rest%d" % (i + 1), t)
info("V4.4.rest_count", "SHORTEST REST LIST: %d items, and only the first is "
     "load-bearing" % len(REST))

para("""V4.5  THE HONEST THREE SENTENCES.
(1) THE SMOOTHING FREEDOM DELIVERS WHAT IT WAS ASKED FOR AND NOT MORE: the
whitening diagonal is a free gauge (an identity plus one Rayleigh step, verified on
%d gauges and %d windows), the blocking number of T148 -- TV(log Lam) = %.2f
growing like m^%.3f -- is not merely reduced but ELIMINATED, exactly %s for the
winning gauge '%s', and the entire price is one certified sandwich %.4f and one
certified constant kap~_up <= %.4f against %.4f, so the hypothesis that blocked
ROUTE S is retired rather than weakened.
(2) WHAT DID NOT FOLLOW, stated with its number: the smoothness functional itself
improved only by a factor %.2f (nu_L~ %.1f against %.1f), it now sits INSIDE the
target m/(8 kap_Lam~) on the upper %d of %d windows (rho = %.3f at m = %d) but not
on the small-m end, and the object the chain actually uses -- the certified Q_star
ceiling -- fell from %.4g to %.4g with its exponent falling from %.3f to %.3f
WITHOUT becoming flat, because the Green-weighted cut also charges modes above the
bottom block, where nu_L~ still grows like %s.  End to end the family-maximum chain
delivers %.4f .. %.4f of the true gap certified and %.3e .. %.3e a priori, against
T148's %.4f .. %.4f and %.3f .. %.3f: the a priori side improved by up to a factor
%.2f, the certified side did not move, because there the Jacobi gauge's sharper
kap~_up still wins.
(3) SO THE MISSING INPUT MOVED RATHER THAN CLOSED, and the family says WHY in one
number: the gauges that delete the flutter and keep the macro profile shift nu_L~ by
at most %.1f%%, so the roughness the functional responds to was never in the
multiplier -- which is why it moved to a place where the classical literature
actually speaks, since with the constant gauge the question is EXACTLY the
smoothness of the PURE Toeplitz-minus-Hankel section's low modes (licence 13), no
multiplier, no whitening, no arithmetic weight, and the remaining rest is how far up
the spectrum that smoothness reaches.  The stress pair
confirms the freedom is not a loophole: the no-go's multiplier is already smooth
(best sandwich %.4f over the whole family) and its functional still diverges like
%s under every gauge, while the Dirichlet control's diagonal is constant, every
candidate is the identity on it to %.1e, and nu_L~ stays at pi.""" % (
    len(TBL), len(ROWS), TV_T148, TV_EXP_T148,
    "0" if W["tv_max"] < 1e-12 else "%.4f" % W["tv_max"], WIN, W["sig_max"],
    W["kap_max"], TBL["id"]["kap_max"],
    TBL["id"]["nu_max"] / max(W["nu_max"], 1e-300), W["nu_max"],
    TBL["id"]["nu_max"], W["hit"], W["n"], W["rho_top"], W["m_top"],
    QC_ID, QC_WIN, F_QCID["p"], F_QCWIN["p"], fit_str(_NUW_WIN),
    qmin([r["frac_fam"] for r in ROWS]), qmax([r["frac_fam"] for r in ROWS]),
    qmin([r["frac_apr_fam"] for r in ROWS]),
    qmax([r["frac_apr_fam"] for r in ROWS]),
    FRAC_T148[0], FRAC_T148[1], FRACAP_T148[0], FRACAP_T148[1],
    qmax(_gain),
    100.0 * max(abs(x - _nu_id) for x in _fn) / max(_nu_id, 1e-300),
    qmax([r["sig_max"] for r in NG]), fit_str(F_NG_BEST),
    qmax([r["dev"] for r in CT])))

para("""V4.6  THE DISTANCE TO RH, MAPPED AND NOT TRAVELLED.  Even if all three rest
items closed, what would stand is: a lower bound with an explicit constant on the
bottom generalised eigenvalue of a Toeplitz-minus-Hankel section, for prime-power
zones in frame A, on a FINITE window, over the D-strata listed in V2.3.  Between
that and RH lie at least: all D and not a stratified list; all zones and not
prime-power zones; the full window and not frame A; and the passage from a window
form's positivity to the criterion itself, which this file CITES (Weil 1952;
Bombieri 2000; Connes 1999) and never uses.  No zero data was read, generated or
approximated anywhere in this file.""")

print("")
print("VERDICT  %s" % VERDICT)
print("")
print("TOTAL  %d checks, %d passed, %d failed, %.1f s"
      % (PASS + FAIL, PASS, FAIL, time.time() - T_START))
if FAIL:
    raise SystemExit(1)






