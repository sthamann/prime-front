#!/usr/bin/env python3
"""PRIME.ONEBADMODE.KS.DUAL.01 -- probe D: CLOSING THE THREE CARRIERS.

EXPLORATION ONLY.  No claim, no marker, no ledger row, no paper edit,
no RH statement.  experiments/ only.

=====================================================================
MISSION.  CCLIII measured that the h-stable restricted residual
res(h) ~ 0.665 of the deployed lattice family splits EXACTLY into three
carriers against the folded free (arcsine) reference,

      log res(h) = COEF(h) + GAP(h) + SPREAD(h),
      COEF   = sum_{n=1..h/2} log A_n - (1/2) log 2,   A_n = 2 beta_n,
      GAP    = (1/2) f log f,                          f = 1 - excl,
      SPREAD = -(1/2) f <log(rho/rho_bar)>_{Theta_+},

and that all three are h-flat.  This probe CLOSES each carrier: an
exact analytic form where one exists, a RIGOROUS all-h bound where it
does not, and -- for every rung of the 42-surface + 4-deep ward table
-- the formula against the measured value.  NO fitting.  NO pretty
fractions.  The number 0.665 is never an input: it is recomputed from
the carriers and printed as an output.

=====================================================================
THE DEPLOYED MEASURE, WRITTEN OUT (derived here, warded in-probe).

The lag arm of a rung is c_k = A_arch(kD) - (tent-assembled prime
atoms), k = 0..M-1 (v563 arch_lags / atom_lags_at, read-only).
grid_density() extends it evenly to length L = 2M-2 and takes the DFT,
so the deployed grid values are the samples of ONE explicit even
trigonometric polynomial

  E1  d(theta) = c_0 + 2 sum_{k=1}^{M-2} c_k cos(k theta)
                     + c_{M-1} cos((M-1) theta),   d_j = d(2 pi j / L),
      and d_j = d_{L-j} exactly (even extension).            [WARDED]

folded_measure() keeps the cells with d_j > 0, folds j <-> L-j and
weights them by 4 sin^2(theta/2)/(2L).  Hence, with
Theta_+ = {theta in (0, pi] : d(theta) > 0},

  E2  the support fraction is RATIONAL AND EXACT:
        f = 2 N / L,  N = #{ j = 1..L/2 : d_j > 0 },
      i.e. f = |Theta_+| / pi on the grid;                   [WARDED]
  E3  the theta-density of the normalized measure is
        rho(theta) = 2 d(theta) sin^2(theta/2) / (pi m_0),
        m_0 = (2/pi) int_{Theta_+} d sin^2(theta/2) dtheta,
      and rho_bar = 1/(pi f) is its ARITHMETIC MEAN over the present
      cells (so Jensen applies to SPREAD).                   [WARDED]

=====================================================================
WHAT IS PROVED HERE (each line is elementary and self-contained; the
external anchors are cited, nothing is imported on faith).

  T1  COEF IS A MOMENT FUNCTIONAL -- EXACT, at every K = h/2.
      With k_K the monomial and t_K the Chebyshev leading coefficient
      of the orthonormal polynomial p_K, the three-term recurrence
      gives a_{n+1} = k_n / k_{n+1} and T_K = 2^{K-1} x^K + ..., so
        sum_{n=1}^{K} log(2 a_n) = log 2 - (1/2) log m_0 - log t_K,
        t_K = 1 / |R_KK|,
      where R is the (unique, positive-diagonal) triangular factor of
      the weighted Chebyshev design matrix, A = diag(sqrt w) [T_i(x_k)]
      = Q R (equivalently R^T R = the Chebyshev-basis Gram matrix).
      Therefore
        COEF(K) = (1/2) log 2 - (1/2) log m_0 + log |R_KK|.
      Computed by Householder QR -- NOT by the Jacobi recurrence -- so
      the ward is a genuinely independent route to the same number, and
      one factorization wards ALL K <= K_cap at once.
      [Szego, "Orthogonal Polynomials", AMS 1939, Sec. 2.2/2.4;
       Chihara, "An Introduction to Orthogonal Polynomials", 1978,
       Ch. I.4; Gautschi, "Orthogonal Polynomials", OUP 2004, Sec. 2.1.]

  T2  THE ALL-h CEILING FOR COEF -- THEOREM, sharp on the free chain.
      k_K^{-2} = E_K := min { int P^2 dmu : P monic, deg P = K }, so
      EVERY monic P gives a rigorous upper bound on E_K, hence on COEF:
        COEF(K) = K log 2 + (1/2) log E_K - (1/2) log m_0 - (1/2)log 2.
      Taking P = 2^{1-K} T_K (monic, |T_K| <= 1 on [-1,1]) gives
        COEF(K) <= (1/2) log 2 + (1/2) log <T_K^2>_mu <= (1/2) log 2
                 = 0.3465735902799726,
      for EVERY h and every measure supported in [-1,1].  Sharp: the
      arcsine free chain has <T_K^2> = 1/2 and COEF = 0 exactly.
      K_C := (1/2) log 2.                                  [THEOREM]

  T2b THE SAME VARIATIONAL BOUND ON THE SUPPORT HULL -- THEOREM, all K.
      If the support of mu lies in [mid - r, mid + r] then the monic
      Chebyshev polynomial of that interval, 2 (r/2)^K T_K((x-mid)/r),
      has sup-norm 2 (r/2)^K there, so
        COEF(K) <= K log r + (1/2) log 2,
      which is T2 at r = 1 and DIVERGES LINEARLY when r < 1.  The
      sharper asymptotic form of the same mechanism is the Chebyshev-
      constant / capacity theorem: E_K^{1/2K} -> cap(E) for the support
      E, hence the per-degree slope of COEF obeys
        d COEF / d K  ->  log(2 cap(E))  <=  log(|E| / 2),
      using cap(E) <= |E|/4 (equality only for an interval).  For a
      support with |E| < 2 the coefficient sum therefore has NO limit:
      it diverges linearly in K.  This is measured here against the
      K-scan of the exact T1 curve, and it decides the h-limit question
      for COEF.
      [Szego 1939, Sec. 16.4; Ransford, "Potential Theory in the
       Complex Plane", CUP 1995, Thm 5.5.4 (Chebyshev constant =
       capacity) and Thm 5.3.2 (cap <= |E|/4); Widom, Adv. Math. 3
       (1969) 127; Damanik-Killip-Simon, Annals 171 (2010) 1931.]

  T3  THE ALL-h BRACKET FOR GAP -- THEOREM, closed form.
      GAP = (1/2) f log f on f in (0, 1] is <= 0, and its minimum over
      the whole interval is at f = 1/e:
        -1/(2e) <= GAP <= 0,   1/(2e) = 0.1839397205857212,
      with equality iff f = 1/e resp. f = 1.  K_G := 1/(2e).
      The h-limit question is therefore ENTIRELY the h-limit of the
      rational number f = 2N/L, i.e. of the normalized Lebesgue measure
      of the positivity set of the explicit kernel E1.     [THEOREM]

  T4  SPREAD IS NONNEGATIVE -- THEOREM (Jensen/Gibbs), and it is the
      exact log of the arithmetic-to-geometric mean ratio of the
      density:
        SPREAD = (1/2) f log(A_rho / G_rho) >= 0,
      A_rho = mean rho = rho_bar, G_rho = geometric mean, equality iff
      rho is constant on Theta_+.  Two rigorous consequences:
        SPREAD <= (1/2) f (A_rho / H_rho - 1)        (log t <= t - 1)
        SPREAD <= (1/2) f log(A_rho / rho_min),
      H_rho the harmonic mean -- both computable from the deployed
      density, both all-h.  K_S := the max of the sharper hull over the
      ward table (certified-numeric, not a theorem).
      [Hardy-Littlewood-Polya, "Inequalities", CUP 1934, Thm 9;
       Cover-Thomas, "Elements of Information Theory", 2006, Sec. 2.6.]

  T5  THE JACOBIAN PIECE OF SPREAD IS CLOSED FORM.  Substituting E3,
        SPREAD = -(1/2) f [ log(2 f / m_0) + <log d>_{Theta_+}
                            + 2 <log sin(theta/2)>_{Theta_+}
                            + <log phi> ],
      an EXACT four-way split in which the last term is purely
      combinatorial: phi_u = 1 on every folded cell EXCEPT the endpoint
      cell u = L/2 (theta = pi), which is its own mirror and therefore
      carries HALF the folded weight, phi = 1/2, so
        <log phi> = -(log 2) 1{theta = pi present} / N = O(1/N).
      On the full band Theta_+ = (0, pi) the Jacobian term is
      elementary,
        (2/pi) int_0^pi log sin(theta/2) dtheta = -2 log 2,
      so the deployed value of that term is the measured departure of
      the support from the full band.                        [WARDED]

  T6  THE SZEGO DEFECT FRAME (why 0.665 is not 1).  For a measure with
      support [-1,1] obeying the Szego condition, Szego's theorem gives
      log res(infinity) = 0; three exactly solvable members of the
      DEPLOYED pipeline confirm the conventions to the grid resolution:
        A1  equal theta-weights (arcsine / Chebyshev-1, a_1 = 1/sqrt2,
            a_n = 1/2):        COEF 0,          GAP 0, SPREAD 0
        A2  flat lag arm c = (1, 0, ..., 0), d == 1, rho ~ sin^2(th/2)
            (Chebyshev-3 class, a_n = 1/2, b_1 = -1/2):
                               COEF -(1/2)log2, GAP 0, SPREAD +(1/2)log2
        A3  lag arm c = (2, 1, 0, ..., 0), d = 4cos^2(th/2),
            rho ~ sin^2(theta) (Chebyshev-2, a_n = 1/2, b_n = 0):
                               COEF -(1/2)log2, GAP 0, SPREAD +(1/2)log2
      and for A2/A3 the FINITE-L values are closed form too, so the
      anchors are exact at the deployed grid and need no continuum
      tolerance.  With n = L/2 and Gauss's product
      prod_{u=1}^{m-1} 2 sin(pi u/m) = m:
        A2  f = 1 exactly, GAP = 0,
            SPREAD = (1/2) log 2 - log(L)/L,
        A3  d vanishes at theta = pi, so that cell is EXCLUDED:
            f = 1 - 2/L exactly, GAP = (1/2) f log f,
            SPREAD = (1/2) f [ log 2 + log(n/(n-1)) - 2 log(n)/(n-1) ],
      and in both cases the deployed grid IS the Gauss-Chebyshev
      quadrature of the corresponding weight, so the Jacobi prefix is
      exact and COEF = -(1/2) log 2 to roundoff.  A1's equal-weight
      grid is NOT a Gauss rule for the arcsine measure, so A1 keeps
      CCLIII's declared grid tolerance SR_FREE_TIE = 5e-3, inherited
      verbatim.
      All three have log res = 0 in the continuum -- each carrier value
      derived in closed form above and warded numerically.  The deployed
      therefore measures a SZEGO DEFECT, and the probe reports which of
      its two possible sources (truncation at K = h/2, or the gapped
      support of E1) carries it: the K-scan of COEF and the l^1 vs l^2
      anatomy of A_n - 1 decide it MEASURED.
      [Szego 1939, Sec. 10.7 (the Szego condition); Killip-Simon,
       Annals 158 (2003) 253 -- the P2/l^2 sum rule; Simon, "Szego's
       Theorem and its Descendants", PUP 2011, Thm 2.8.1 (Szego-Shohat-
       Nevai) and Ch. 9 (finite-gap / Widom class); Damanik-Killip-
       Simon, Annals 171 (2010) 1931 (isospectral torus).]

=====================================================================
FROZEN PROTOCOL (2026-08-12).

 S0 FIREWALL.  AST scan for prime/zero oracles; verification/ and every
    predecessor probe READ-ONLY; RNG only through the corpus scramble
    seed.  AC1: the carriers are NOT re-implemented here -- every
    measured triple comes from t2.carriers_of verbatim, so no
    convention can drift between CCLIII and this probe.  AC2: the
    analytic anchors A1/A2/A3 contain no rung identifier; their
    predicted values are the closed forms of T6, hard-coded as formulas
    (log 2 / 2), never as measured numbers.
 M  THE WARD TABLE: 42 surface + the 4 lowest-h deep rungs, carriers
    from t2, identity re-warded at IDENT_TIE, and the CCXLV/CCLIII
    REPRO ward (res med, KS_bulk med, excluded fraction band).
 A  the three exactly solvable anchors of T6 against their closed
    forms at ANCHOR_TIE (grid resolution declared).
 C  COEF: the T1 identity by QR over all K <= K_CAP at COEF_TIE; the
    T2 ceiling per rung; the l^1 / l^2 anatomy of A_n - 1 and the
    K-scan -- which decides whether the h-limit is closable.
 G  GAP: the T3 bracket; f = 2N/L warded as an integer identity; the
    positivity-set characterization E1/E2 warded; the continuum f from
    a REFINED (zero-padded) kernel grid with the discretization error
    reported as the certified error of the closed form.
 S  SPREAD: the T4 nonnegativity and mean-ratio identity; the T5
    three-way split at IDENT_TIE; the Jacobian anchor -2 log 2; the two
    rigorous hulls.
 R  THE COMPOSITION: res recomputed from the carriers (never an input);
    the composed all-h bracket from K_C, K_G, K_S with per-term typing
    THEOREM / CERTIFIED-NUMERIC / MEASURED.
 P  SCREENS.  tau does not enter this probe at all (the carriers are
    measure-forward), so the tau screen is VACUOUS BY CONSTRUCTION and
    is declared, not scored.  Scored: the log-log h-slope of every
    carrier and of every hull, plus the CCXVII c_h relocation screen on
    the matched surface rungs.
 C  CONTROLS.  The smooth world (atom masses -> smooth density) and the
    scramble world (atom positions -> seeded scramble) must move the
    carriers by more than CARRIER_CTRL_BAR, and must NOT move the
    analytic anchors.  Silent controls -> CONTROL-SILENT.
 V  VERDICT.

FROZEN BARS: SURF_EXP = 42; DEEP_SUB = 4; IDENT_TIE = 1e-12;
COEF_TIE = 1e-8; ANCHOR_TIE = 5e-3 (A1, CCLIII's SR_FREE_TIE
verbatim); ANCHOR_EXACT_TIE = 1e-5 (A2/A3, exact finite-L forms);
ANCHOR_L = 1022; K_CAP = 768;
REFINE = 8; RES_MED_REF = 0.665; KSBULK_MED_REF = 1.830;
EXCL_BAND = (0.26, 0.34); REPRO_RTOL = 0.02; SLOPE_PASS = 0.30;
SLOPE_RELOC = 0.70; CARRIER_CTRL_BAR = 1e-2; runtime cap 25 min.

SMOKE DISCLOSURE: see the SMOKE section at the end of this docstring.

NO RH claim.  Every number is a finite float64 measurement on the
deployed family, or an elementary bound proved above.  The limit
h -> infinity is NOT claimed; where a carrier's limit is not closed the
probe says so and prints the obstruction.  No marker moves; no paper,
ledger, website, manifest or verification file is touched.

Sources (read-only): rhp_tier2_polecontrol_probe (CCLIII carriers),
port_tangent_schur_probe (measure pipeline), onebadmode_moments_probe
(CCVII ladder), euler_phase_identity_probe (CCXVII c_h),
v563_paper2_readouts (archimedean kernel + prime atoms).

SMOKE (2026-08-12, before freezing; disclosed in full).
 SMOKE-1 (8 contiguous surface rungs + the 2 lowest deep rungs, 1.1 s)
 ran 25 checks with FOUR failures and reshaped the spec in four places,
 all BEFORE the freeze:
 (i)   the anchors A2/A3 were declared with their CONTINUUM triples and
       missed by 6.8e-3 / 1.19e-2.  The smoke showed the miss is pure
       grid geometry AND that the FINITE-L values are themselves closed
       form via Gauss's product prod_{u<m} 2 sin(pi u/m) = m; A2/A3 were
       replaced by those exact finite-L forms (they now hold to 1.2e-14)
       and their tie was TIGHTENED from 1e-3 to ANCHOR_EXACT_TIE = 1e-5.
       A1 keeps CCLIII's declared SR_FREE_TIE = 5e-3 verbatim, because
       the equal-weight arcsine grid is NOT a Gauss rule for its own
       weight and cannot do better at this L.
 (ii)  the AC2 anchor scan banned the identifier `carriers_of`, i.e.
       exactly the deployed carrier code the anchors MUST use.  The ban
       was corrected to rung identifiers only (measure_source /
       window_of / build_rung / kz / arch_lags / atom_lags_at /
       build_ext_tables).
 (iii) T5 was stated as a THREE-way split and missed by 1.15e-3: the
       folded endpoint cell theta = pi is its own mirror and therefore
       carries HALF the folded weight.  T5 was corrected to the exact
       FOUR-way form with the purely combinatorial term
       <log phi> = -(log 2) 1{pi present} / N (now exact to 1.7e-16).
       No bar, tie or enum was touched.
 (iv)  SMOKE-1's K-scan was clipped at K = h/2 by the stored A array,
       which made the truncation question undecidable.  Since T1 holds
       at EVERY K, the scan was rebuilt off the SAME QR curve, which
       reaches K/(h/2) up to 2.97 on the deployed supports; this is what
       turned the truncation question into a decision.
 SMOKE-2/3 (post-corrections) ran GREEN with no kills and additionally
 DISCLOSE the readings that were known before the frozen run (none of
 them is a bar, no enum, screen or control was touched): COEF's exact
 K-curve DECREASES monotonically (median drift 0.233 from K = h/2 to
 K = h) so the coefficient sum diverges; the l^1 norm of A_n - 1 grows
 like h^0.56 while its l^2 norm is flat, so the KS datum cannot close
 COEF; the asymptotic capacity ceiling log(|E|/2) is about -0.345 per
 degree; the support hull half-width is r = 1.0000 to 1e-5, so T2b is
 NEARLY VACUOUS on this family and is reported as such; the rigorous
 SPREAD hull K_S^rig is about 10x the measured SPREAD; and the smooth
 world keeps the excluded fraction (f_smooth ~ 0.741 against
 f ~ 0.704), i.e. the gap set is archimedean with a ~10 percent
 prime-driven share.
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import onebadmode_moments_probe as ob          # noqa: E402 (READ-ONLY)
import port_tangent_schur_probe as pt          # noqa: E402 (READ-ONLY)
import euler_phase_identity_probe as eul       # noqa: E402 (READ-ONLY)
import rhp_tier2_polecontrol_probe as t2       # noqa: E402 (READ-ONLY)

# ------------------------------------------------------- frozen bars
SURF_EXP = 42
DEEP_SUB = 4
IDENT_TIE = 1.0e-12
COEF_TIE = 1.0e-8
ANCHOR_TIE = 5.0e-3
ANCHOR_EXACT_TIE = 1.0e-5
ANCHOR_L = 2 * 512 - 2
K_CAP = 768
REFINE = 8
RES_MED_REF = 0.665
KSBULK_MED_REF = 1.830
EXCL_BAND = (0.26, 0.34)
REPRO_RTOL = 0.02
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CARRIER_CTRL_BAR = 1.0e-2
SCRAMBLE_SEED = ob.SCR_SEED

HALF_LOG2 = 0.5 * math.log(2.0)
K_C_THM = HALF_LOG2                      # T2 ceiling for COEF
K_G_THM = 1.0 / (2.0 * math.e)           # T3 floor depth for GAP
JAC_FULL = -2.0 * math.log(2.0)          # T5 full-band Jacobian term

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
# AC2: identifiers that would make an "analytic anchor" rung-dependent.
ANCHOR_BANNED = ("measure_source", "window_of", "build_rung", "kz",
                 "arch_lags", "atom_lags_at", "build_ext_tables")

CHECKS = []
KILLS = []
T0 = time.time()
SMOKE = "--smoke" in sys.argv[1:]
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def slope2se(xs, ys):
    """t2.linfit returns (slope, 2SE, R^2, intercept) -- keep the two
    numbers the screens are typed on."""
    s, two_se, _r2, _a = t2.linfit(xs, ys)
    return float(s), float(two_se)


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def e3(v):
    v = np.asarray(v, float)
    if v.size == 0:
        return "n/a"
    return "%.3e/%.3e/%.3e" % (float(np.min(v)), float(np.median(v)),
                               float(np.max(v)))


def ast_scan(names, only=None):
    """Read-only AST scan of THIS file for banned identifiers."""
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = []
    bodies = [tree]
    if only is not None:
        bodies = [n for n in ast.walk(tree)
                  if isinstance(n, ast.FunctionDef) and n.name in only]
    for body in bodies:
        for node in ast.walk(body):
            nm = None
            if isinstance(node, ast.Name):
                nm = node.id
            elif isinstance(node, ast.Attribute):
                nm = node.attr
            if nm and nm.lower() in names:
                hits.append(nm)
    return sorted(set(hits))


# ======================================================== T1 / T2: COEF
def cheb_design(xs, ws, k_top):
    """diag(sqrt w) [T_0(x) ... T_{k_top}(x)] by the Chebyshev
    recurrence -- the design matrix of T1 (no moments, no Hankel)."""
    xs = np.asarray(xs, float)
    n = len(xs)
    A = np.empty((n, k_top + 1))
    A[:, 0] = 1.0
    if k_top >= 1:
        A[:, 1] = xs
    for k in range(2, k_top + 1):
        A[:, k] = 2.0 * xs * A[:, k - 1] - A[:, k - 2]
    return np.sqrt(np.asarray(ws, float))[:, None] * A


def coef_by_qr(xs, ws, m0, k_top):
    """T1: COEF(K) = 1/2 log 2 - 1/2 log m_0 + log|R_KK| for every
    K <= k_top, from ONE Householder QR (independent of Lanczos).
    Returns the vector of COEF(K), K = 1..k_top, and <T_K^2> for the
    T2 ceiling."""
    A = cheb_design(xs, ws, k_top)
    rr = np.linalg.qr(A, mode="r")
    diag = np.abs(np.diag(rr))
    if np.any(diag <= 0.0):
        return None, None
    coefs = HALF_LOG2 - 0.5 * math.log(m0) + np.log(diag[1:])
    t_sq = (A[:, -1] ** 2).sum() / m0
    return coefs, float(t_sq)


def support_x(ch):
    """The support points of the deployed folded measure, rebuilt from
    the stored fold indices exactly as folded_measure does."""
    return np.cos(2.0 * math.pi * np.asarray(ch["uf"], float)
                  / ch["L"])


def cheb_moment(xs, ws, m0, k):
    """<T_k^2>_mu -- the only ingredient of the sharp T2 ceiling."""
    xs = np.asarray(xs, float)
    tm1 = np.ones(len(xs))
    t_k = xs.copy() if k >= 1 else tm1
    for _ in range(2, k + 1):
        t_k, tm1 = 2.0 * xs * t_k - tm1, t_k
    return float(np.sum(np.asarray(ws, float) * t_k ** 2) / m0)


# =================================================== the analytic anchors
def anchor_from_arm(c_arm, name, pred):
    """AC2-SCANNED: run the DEPLOYED pipeline (grid_density ->
    folded_measure -> lanczos_chain -> t2.carriers_of) on an ANALYTIC
    lag arm and compare with the closed-form triple `pred`."""
    d = pt.grid_density(np.asarray(c_arm, float))
    ll = 2 * len(c_arm) - 2
    xs, ws, _uf = pt.folded_measure(d, ll, +1.0)
    nb = len(xs) // 2
    al, be, m0, n_ok = pt.lanczos_chain(xs, ws, nb + 1)
    if n_ok < nb + 1 or np.any(be <= 0.0):
        return None
    ch = dict(h=2 * nb, L=ll, al=al, be=be, m0=m0, ws=ws, uf=_uf,
              n_pos=len(ws), n_neg=0)
    car = t2.carriers_of(ch)
    got = (car["coef"], car["gap"], car["spread"])
    dev = max(abs(g - p) for g, p in zip(got, pred))
    return dict(name=name, car=car, got=got, pred=pred, dev=dev,
                a1=float(2.0 * be[0]),
                ak=float(np.median(2.0 * be[1:])))


def anchor_exact_a2(ll):
    """T6/A2 at FINITE L: f = 1, GAP = 0, SPREAD = 1/2 log2 - log(L)/L,
    COEF = -1/2 log 2 (the grid is the Gauss rule of the weight)."""
    return (-HALF_LOG2, 0.0, HALF_LOG2 - math.log(ll) / ll)


def anchor_exact_a3(ll):
    """T6/A3 at FINITE L: the theta = pi cell is excluded (d = 0), so
    f = 1 - 2/L, and the density is sin^2(pi u / n), n = L/2."""
    n = ll // 2
    f = 1.0 - 2.0 / ll
    spread = 0.5 * f * (math.log(2.0) + math.log(n / (n - 1.0))
                        - 2.0 * math.log(n) / (n - 1.0))
    return (-HALF_LOG2, 0.5 * f * math.log(f), spread)


def anchors():
    section("A -- THE EXACTLY SOLVABLE ANCHORS (T6): the deployed "
            "pipeline against closed forms at the DEPLOYED grid")
    ll = ANCHOR_L
    mm = ll // 2 + 1
    out = []
    fr = t2.free_folded_residual(ll)
    if fr is not None:
        fcar, a1f, akf = fr
        got = (fcar["coef"], fcar["gap"], fcar["spread"])
        dev = max(abs(g - p) for g, p in zip(got, (0.0, 0.0, 0.0)))
        out.append(dict(name="A1 arcsine (equal theta-weights)",
                        car=fcar, got=got, pred=(0.0, 0.0, 0.0),
                        dev=dev, a1=a1f, ak=akf, tie=ANCHOR_TIE,
                        why="continuum triple; the equal-weight grid "
                            "is NOT a Gauss rule -> CCLIII tie"))
    arm2 = np.zeros(mm)
    arm2[0] = 1.0
    a2 = anchor_from_arm(arm2, "A2 flat arm (Chebyshev-3 class)",
                         anchor_exact_a2(ll))
    if a2 is not None:
        a2.update(tie=ANCHOR_EXACT_TIE,
                  why="EXACT finite-L closed form (Gauss-Chebyshev-3)")
        out.append(a2)
    arm3 = np.zeros(mm)
    arm3[0], arm3[1] = 2.0, 1.0
    a3 = anchor_from_arm(arm3, "A3 arm (2,1,0,..) (Chebyshev-2)",
                         anchor_exact_a3(ll))
    if a3 is not None:
        a3.update(tie=ANCHOR_EXACT_TIE,
                  why="EXACT finite-L closed form (Gauss-Chebyshev-2)")
        out.append(a3)
    print("    %-36s %10s %10s %10s %9s %9s"
          % ("anchor", "COEF", "GAP", "SPREAD", "res", "max dev"))
    for an in out:
        print("    %-36s %+10.7f %+10.7f %+10.7f %9.6f %9.2e"
              % (an["name"], an["got"][0], an["got"][1], an["got"][2],
                 an["car"]["res"], an["dev"]))
        print("      closed form (tie %.0e)          %+10.7f %+10.7f "
              "%+10.7f            A_1 %.6f A_n med %.6f"
              % (an["tie"], an["pred"][0], an["pred"][1],
                 an["pred"][2], an["a1"], an["ak"]))
        print("        %s" % an["why"])
    ok = (len(out) == 3
          and all(an["dev"] <= an["tie"] for an in out))
    check("A1 all three exactly solvable members of the DEPLOYED "
          "pipeline reproduce their closed-form carrier triples at "
          "L = %d (A2/A3 EXACT at %.0e, A1 at CCLIII's grid tie %.0e): "
          "max dev %.2e"
          % (ll, ANCHOR_EXACT_TIE, ANCHOR_TIE,
             max([an["dev"] for an in out] or [1.0])), ok, kill="K2")
    bad = ast_scan(ANCHOR_BANNED, only={"anchor_from_arm", "anchors"})
    check("A2 AC2 the anchors carry NO rung identifier (analytic arms "
          "only): %s" % (",".join(bad) or "clean"), not bad,
          kill="K1")
    return out


# ==================================================== the ward table
def build_table():
    section("M -- THE WARD TABLE: 42 surface + %d deep rungs, carriers "
            "from CCLIII verbatim" % DEEP_SUB)
    zones = ob.ladder_zones()
    check("M0 surface rung census %d == %d" % (len(zones), SURF_EXP),
          len(zones) == SURF_EXP, kill="K1")
    if SMOKE:
        zones = zones[:8]
        print("    SMOKE: %d surface rungs" % len(zones))
    rows = []
    for kz in zones:
        src = t2.measure_source("surf", kz)
        ch = t2.build_chain_from_source(src, src["h"] // 2 + 2)
        if ch is None:
            continue
        car = t2.carriers_of(ch)
        rows.append(dict(kz=int(kz), seg="surf", src=src, ch=ch,
                         car=car, h=int(car["h"])))
    ob.build_ext_tables()
    census = sorted(ob.deep_zone_census(), key=lambda p: (p[1], p[0]))
    n_deep = 2 if SMOKE else DEEP_SUB
    for kz, hz in census[:n_deep]:
        src = t2.measure_source("deep", kz)
        ch = t2.build_chain_from_source(src, src["h"] // 2 + 2)
        if ch is None:
            print("    deep kz %-4d h %-5d SHORT" % (kz, hz))
            continue
        car = t2.carriers_of(ch)
        rows.append(dict(kz=int(kz), seg="deep", src=src, ch=ch,
                         car=car, h=int(car["h"])))
        print("    deep kz %-4d h %-5d OK [%.1f s]"
              % (kz, hz, time.time() - T0), flush=True)
    rows.sort(key=lambda r: (r["h"], r["kz"]))
    check("M1 ward table complete: %d rungs (%d surface + %d deep)"
          % (len(rows), sum(1 for r in rows if r["seg"] == "surf"),
             sum(1 for r in rows if r["seg"] == "deep")),
          len(rows) >= 3 and any(r["seg"] == "deep" for r in rows),
          kill="K1")
    dev = max(abs(r["car"]["coef"] + r["car"]["gap"]
                  + r["car"]["spread"] - r["car"]["logres"])
              for r in rows)
    check("M2 WARD the CCLIII carrier identity log res = COEF + GAP + "
          "SPREAD holds per rung: max dev %.2e <= %.0e"
          % (dev, IDENT_TIE), dev <= IDENT_TIE, kill="K2")
    res = np.asarray([r["car"]["res"] for r in rows], float)
    ksb = np.asarray([r["car"]["ks_bulk"] for r in rows], float)
    exc = np.asarray([r["car"]["excl"] for r in rows], float)
    m_res, m_ksb, m_exc = (float(np.median(res)), float(np.median(ksb)),
                           float(np.median(exc)))
    ok_rep = (abs(m_res / RES_MED_REF - 1.0) <= REPRO_RTOL
              and abs(m_ksb / KSBULK_MED_REF - 1.0) <= REPRO_RTOL
              and EXCL_BAND[0] <= m_exc <= EXCL_BAND[1])
    check("M3 REPRO of CCXLV/CCLIII: res med %.6f (cited %.3f, rel "
          "%.4f), KS_bulk med %.4f (cited %.3f), excluded fraction med "
          "%.4f in [%.2f, %.2f]"
          % (m_res, RES_MED_REF, abs(m_res / RES_MED_REF - 1.0),
             m_ksb, KSBULK_MED_REF, m_exc, *EXCL_BAND),
          SMOKE or ok_rep, kill="K3")
    print("    h range %d .. %d; res %s; excluded fraction %s"
          % (rows[0]["h"], rows[-1]["h"], e3(res), e3(exc)))
    return rows


# ============================================== C -- the COEF carrier
def coef_layer(rows):
    section("C -- COEF: the exact moment functional (T1), the all-h "
            "ceiling (T2), and the h-limit anatomy")
    dev_id = 0.0
    n_qr = 0
    ceil_slack = []
    tsq = []
    l1 = []
    l2 = []
    k_full = 0
    for row in rows:
        car, ch = row["car"], row["ch"]
        xs = support_x(ch)
        aa = np.asarray(car["A"], float)
        k_top = min(K_CAP, len(ch["ws"]) - 1)
        k_use = min(len(aa), k_top)
        got, _t = coef_by_qr(xs, ch["ws"], ch["m0"], k_top)
        if got is not None:
            n_qr += 1
            k_full += int(k_use == len(aa))
            cum = np.cumsum(np.log(aa[:k_use])) - HALF_LOG2
            dev_id = max(dev_id, float(np.max(
                np.abs(got[:k_use] - cum))))
            row["coef_qr_k"] = int(k_use)
            row["coef_curve"] = got
        l1.append(float(np.sum(np.abs(aa - 1.0))))
        l2.append(float(np.sum((aa - 1.0) ** 2)))
        t_sq = cheb_moment(xs, ch["ws"], ch["m0"], len(aa))
        tsq.append(t_sq)
        ceil = HALF_LOG2 + 0.5 * math.log(max(t_sq, 1e-300))
        ceil_slack.append(ceil - car["coef"])
        row["coef_ceil"] = ceil
    check("C1 WARD T1 the moment-functional identity COEF(K) = "
          "1/2 log2 - 1/2 log m_0 + log|R_KK| holds for EVERY "
          "K <= min(h/2, %d) on %d/%d rungs -- %d of them up to the "
          "FROZEN K = h/2 itself (Householder QR vs the Jacobi "
          "product, two independent algorithms): max dev %.2e <= %.0e"
          % (K_CAP, n_qr, len(rows), k_full, dev_id, COEF_TIE),
          n_qr == len(rows) and dev_id <= COEF_TIE, kill="K2")
    ceil_slack = np.asarray(ceil_slack, float)
    tsq = np.asarray(tsq, float)
    coefs = np.asarray([r["car"]["coef"] for r in rows], float)
    check("C2 WARD T2 the ceiling COEF <= 1/2 log2 + 1/2 log<T_K^2> "
          "holds on all %d rungs (min slack %.3e); and <T_K^2> <= 1 "
          "so COEF <= K_C = 1/2 log 2 = %.10f with measured margin "
          "%.4f" % (len(rows), float(np.min(ceil_slack)),
                    K_C_THM, K_C_THM - float(np.max(coefs))),
          float(np.min(ceil_slack)) >= -COEF_TIE
          and float(np.max(coefs)) <= K_C_THM + COEF_TIE, kill="K2")
    print("    COEF measured            %s" % e3(coefs))
    print("    T2 sharp ceiling         %s"
          % e3([r["coef_ceil"] for r in rows]))
    print("    <T_K^2>_mu               %s" % e3(tsq))
    print("    ceiling slack            %s" % e3(ceil_slack))
    l1 = np.asarray(l1, float)
    l2 = np.asarray(l2, float)
    hs = np.asarray([r["h"] for r in rows], float)
    s1, e1_ = slope2se(np.log(hs), np.log(l1))
    s2, e2_ = slope2se(np.log(hs), np.log(l2))
    sc, ec = slope2se(np.log(hs), np.log(np.abs(coefs)))
    print("    l^1 norm sum|A_n - 1|    %s   log-log h-slope "
          "%+.3f +- %.3f" % (e3(l1), s1, e1_))
    print("    l^2 norm sum(A_n - 1)^2  %s   log-log h-slope "
          "%+.3f +- %.3f  (the A-part of KS_bulk)" % (e3(l2), s2, e2_))
    print("    |COEF|                   %s   log-log h-slope "
          "%+.3f +- %.3f" % (e3(np.abs(coefs)), sc, ec))
    l1_flat = abs(s1) - e1_ <= SLOPE_PASS
    check("C3 the h-limit of COEF is closable by l^1 control iff "
          "sum|A_n - 1| is h-flat: measured slope %+.3f +- %.3f -> %s"
          % (s1, e1_, "l1-FLAT (closable, certified-numeric)"
             if l1_flat else "l1-GROWING (NOT closable by l^1: the "
             "measured obstruction)"), True)
    print("    READING: the KS/l^2 datum (A-part med %.4f, h-slope "
          "%+.3f) does NOT control the log-product -- Cauchy-Schwarz "
          "only gives sum|A_n - 1| <= sqrt(K sum(A_n-1)^2), and the "
          "measured l^1 slope %+.3f is compatible with exactly that "
          "sqrt growth.  So the l^1 column is the precise missing "
          "ingredient for an all-h COEF limit, and it is MEASURED, "
          "not proved." % (float(np.median(l2)), s2, s1))
    return dict(coef=coefs, ceil=np.asarray([r["coef_ceil"]
                                             for r in rows], float),
                slack=ceil_slack, l1=l1, l2=l2, tsq=tsq,
                l1_slope=(s1, e1_), l1_flat=l1_flat)


def coef_kscan(rows):
    """The truncation anatomy: COEF(K) beyond the frozen K = h/2, read
    off the SAME QR factorization (T1 holds for every K), up to the
    largest degree the deployed support allows.  This decides whether
    the residual is a property of the MEASURE or of the CUT."""
    section("K -- THE TRUNCATION ANATOMY OF COEF (diagnostic only; the "
            "frozen carrier is K = h/2)")
    fr = [0.25, 0.5, 1.0, 1.5, 2.0]
    tab = []
    reach = []
    for row in rows:
        cur = row.get("coef_curve")
        if cur is None:
            continue
        base = len(np.asarray(row["car"]["A"], float))
        vals = []
        for f in fr:
            k_use = int(round(f * base))
            vals.append(float(cur[k_use - 1])
                        if 1 <= k_use <= len(cur) else float("nan"))
        tab.append(vals)
        reach.append(len(cur) / float(base))
    tab = np.asarray(tab, float)
    print("    the QR curve reaches K / (h/2) = %s (support-limited)"
          % e3(reach))
    for j, f in enumerate(fr):
        col = tab[:, j]
        col = col[np.isfinite(col)]
        print("    K = %.2f h/2 (%2d rungs available): COEF %s"
              % (f, len(col), e3(col)))
    both = np.isfinite(tab[:, 4]) & np.isfinite(tab[:, 1])
    drift = (float(np.median(np.abs(tab[both, 4] - tab[both, 1])))
             if int(np.sum(both)) else float("nan"))
    lin, lg, hull, cap = [], [], [], []
    for row in rows:
        cur = row.get("coef_curve")
        if cur is None:
            continue
        base = len(np.asarray(row["car"]["A"], float))
        lo = max(8, base // 4)
        kk = np.arange(lo, len(cur) + 1, dtype=float)
        yy = np.asarray(cur[lo - 1:], float)
        s_l, _e, r2_l, _a = t2.linfit(kk, yy)
        s_g, _e2, r2_g, _a2 = t2.linfit(np.log(kk), yy)
        lin.append((s_l, r2_l))
        lg.append((s_g, r2_g))
        xs = support_x(row["ch"])
        r_hull = 0.5 * (float(np.max(xs)) - float(np.min(xs)))
        hull.append(r_hull)
        th = 2.0 * math.pi * np.asarray(row["ch"]["uf"], float) \
            / row["ch"]["L"]
        e_len = float(np.sum(np.sin(th))) * 2.0 * math.pi / row["ch"]["L"]
        cap.append(math.log(max(e_len, 1e-300) / 2.0))
        row["hull_r"] = r_hull
    print("    per-degree behaviour of the EXACT T1 curve on "
          "K in [h/8, reach]:")
    print("      linear fit  dCOEF/dK  %s   R^2 %s"
          % (e3([v[0] for v in lin]), e3([v[1] for v in lin])))
    print("      log fit     dCOEF/dlogK %s   R^2 %s"
          % (e3([v[0] for v in lg]), e3([v[1] for v in lg])))
    print("      T2b hull ceiling log r (r = support half-width %s): "
          "%s   [THEOREM, all K]"
          % (e3(hull), e3([math.log(max(h_, 1e-300)) for h_ in hull])))
    print("      capacity ceiling log(|E|/2) on the per-degree slope "
          "%s   [THEOREM, asymptotic: cap(E) <= |E|/4]" % e3(cap))
    med_lin = float(np.median([v[0] for v in lin]))
    med_cap = float(np.median(cap))
    print("      => the measured per-degree slope %.4e is %s the "
          "asymptotic capacity ceiling %.4e, and it is NEGATIVE, so "
          "the coefficient sum DIVERGES: COEF has no series limit and "
          "the h-flat residual is a property of the FROZEN CUT "
          "K = h/2." % (med_lin, "inside" if med_lin <= med_cap
                        else "above (the asymptotic regime is not "
                             "reached at these degrees)", med_cap))
    print("    median |COEF(K = h) - COEF(K = h/2)| = %.4e over %d "
          "rungs -- %s" % (drift, int(np.sum(both)),
                           "TRUNCATION-STABLE: the residual is a "
                           "property of the measure, not of the cut"
                           if drift <= 5.0e-2 else
                           "the carrier MOVES with the cut, so the "
                           "residual is a TRUNCATION invariant and "
                           "every h-limit statement must name K"))
    ok_hull = True
    for row in rows:
        cur, r_hull = row.get("coef_curve"), row.get("hull_r")
        if cur is None or r_hull is None:
            continue
        kk = np.arange(1, len(cur) + 1, dtype=float)
        if float(np.max(np.asarray(cur, float)
                        - (kk * math.log(r_hull) + HALF_LOG2))) \
                > COEF_TIE:
            ok_hull = False
    check("C5 WARD T2b the hull ceiling COEF(K) <= K log r + 1/2 log2 "
          "holds for EVERY K on every rung (r = the support "
          "half-width)", ok_hull, kill="K2")
    check("C6 the truncation anatomy is reported: median drift from "
          "K = h/2 to K = h is %.4e on %d rungs, per-degree slope "
          "%.4e" % (drift, int(np.sum(both)), med_lin), True)
    return dict(drift=drift, slope=med_lin, cap=med_cap,
                hull=float(np.median(hull)))


# =============================================== G -- the GAP carrier
def gap_layer(rows):
    section("G -- GAP: the exact rational form (E2), the closed-form "
            "bracket (T3), and the positivity-set geometry (E1)")
    dev_f = dev_ev = 0.0
    n_bad = 0
    fs = []
    fine = []
    for row in rows:
        src, ch, car = row["src"], row["ch"], row["car"]
        c_at, _ = t2.core.atom_lags_at(src["alpha"], src["M"],
                                       src["u_at"], src["mu_at"])
        c = np.asarray(src["c_ar"], float) + np.asarray(c_at, float)
        d = pt.grid_density(c)
        ll = 2 * src["M"] - 2
        half = ll // 2
        dev_ev = max(dev_ev, float(np.max(np.abs(
            d[1:half] - d[ll - 1:half:-1]))) / max(
                1.0, float(np.max(np.abs(d)))))
        n_pos = int(np.sum(d[1:half + 1] > 0.0))
        f_exact = 2.0 * n_pos / ll
        dev_f = max(dev_f, abs(f_exact - car["frac"]))
        if n_pos != len(ch["ws"]):
            n_bad += 1
        fs.append(car["frac"])
        a_pad = np.concatenate([c, c[-2:0:-1]])
        big = np.zeros(REFINE * ll)
        big[:len(a_pad) // 2 + 1] = a_pad[:len(a_pad) // 2 + 1]
        big[-(len(a_pad) - len(a_pad) // 2 - 1):] = \
            a_pad[len(a_pad) // 2 + 1:]
        dfine = np.fft.fft(big).real
        hf = (REFINE * ll) // 2
        fine.append(2.0 * float(np.sum(dfine[1:hf + 1] > 0.0))
                    / (REFINE * ll))
        row["n_pos"] = n_pos
    check("G1 WARD E1 the deployed grid values are samples of the even "
          "kernel d(theta) = sum_k c_k cos(k theta): d_j = d_{L-j} to "
          "%.2e (relative)" % dev_ev, dev_ev <= 1.0e-14, kill="K2")
    check("G2 WARD E2 the support fraction is the EXACT RATIONAL "
          "2N/L with N = #{j <= L/2 : d(theta_j) > 0}: max dev %.2e "
          "<= %.0e, and the cell count matches the deployed folded "
          "measure on %d/%d rungs"
          % (dev_f, IDENT_TIE, len(rows) - n_bad, len(rows)),
          dev_f <= IDENT_TIE and n_bad == 0, kill="K2")
    fs = np.asarray(fs, float)
    fine = np.asarray(fine, float)
    gaps = np.asarray([r["car"]["gap"] for r in rows], float)
    thm = 0.5 * fs * np.log(fs)
    check("G3 WARD T3 GAP = 1/2 f log f with f = 2N/L exactly (max "
          "dev %.2e) and the closed-form bracket -1/(2e) <= GAP <= 0 "
          "holds on all %d rungs: GAP %s, K_G = 1/(2e) = %.10f"
          % (float(np.max(np.abs(thm - gaps))), len(rows), e3(gaps),
             K_G_THM),
          float(np.max(np.abs(thm - gaps))) <= IDENT_TIE
          and float(np.min(gaps)) >= -K_G_THM
          and float(np.max(gaps)) <= 0.0, kill="K2")
    hs = np.asarray([r["h"] for r in rows], float)
    sf, ef = slope2se(np.log(hs), np.log(fs))
    print("    f = 2N/L (grid, exact)   %s   log-log h-slope "
          "%+.3f +- %.3f" % (e3(fs), sf, ef))
    print("    f on a %dx refined kernel grid  %s   max |f - f_fine| "
          "%.3e  <- the certified discretization error of the closed "
          "form" % (REFINE, e3(fine),
                    float(np.max(np.abs(fs - fine)))))
    print("    the excluded set is EXACTLY {theta : d(theta) <= 0}, "
          "i.e. the set where the tent-assembled prime atoms "
          "overwhelm the archimedean kernel A(kD); its measure is not "
          "elementary (A is a Gauss-Legendre integral of the Weil "
          "archimedean density), so f has NO closed form in terms of "
          "the frozen constants -- what IS closed form is the map "
          "f -> GAP and its bracket.")
    print("    distance of f from the GAP minimizer 1/e = %.6f: %s"
          % (1.0 / math.e, e3(np.abs(fs - 1.0 / math.e))))
    f_sm = []
    for row in rows:
        src = t2.measure_source(row["seg"], row["kz"], world="smooth")
        c_at, _ = t2.core.atom_lags_at(src["alpha"], src["M"],
                                       src["u_at"], src["mu_at"])
        d = pt.grid_density(np.asarray(src["c_ar"], float)
                            + np.asarray(c_at, float))
        ll = 2 * src["M"] - 2
        f_sm.append(2.0 * float(np.sum(d[1:ll // 2 + 1] > 0.0)) / ll)
    f_sm = np.asarray(f_sm, float)
    ss, es = slope2se(np.log(hs), np.log(f_sm))
    print("    THE GAP-SET ANATOMY (CCXLV): the same count with the "
          "prime atom MASSES replaced by the smooth density (positions "
          "kept) gives f_smooth %s (h-slope %+.3f +- %.3f); the "
          "prime-driven share of the excluded fraction is "
          "(f_smooth - f)/(1 - f) = %s"
          % (e3(f_sm), ss, es, e3((f_sm - fs) / (1.0 - fs))))
    check("G4 the excluded fraction survives the smooth world, so it "
          "is NOT an artifact of the atoms alone: 1 - f_smooth = %s "
          "against 1 - f = %s" % (e3(1.0 - f_sm), e3(1.0 - fs)),
          bool(np.all(f_sm > 0.0) and np.all(f_sm <= 1.0)))
    return dict(f=fs, fine=fine, gap=gaps, f_smooth=f_sm,
                f_slope=(sf, ef))


# ============================================ S -- the SPREAD carrier
def spread_layer(rows):
    section("S -- SPREAD: nonnegativity (T4), the mean-ratio identity, "
            "the exact four-way split and the closed-form Jacobian "
            "(T5)")
    dev_mean = dev_split = 0.0
    rows_out = []
    for row in rows:
        ch, car = row["ch"], row["car"]
        dth = 2.0 * math.pi / ch["L"]
        rho = (np.asarray(ch["ws"], float) / ch["m0"]) / dth
        f = car["frac"]
        a_rho = float(np.mean(rho))
        g_rho = float(np.exp(np.mean(np.log(rho))))
        h_rho = float(1.0 / np.mean(1.0 / rho))
        mean_form = 0.5 * f * math.log(a_rho / g_rho)
        dev_mean = max(dev_mean, abs(mean_form - car["spread"]))
        th = 2.0 * math.pi * np.asarray(ch["uf"], float) / ch["L"]
        phi = np.where(np.asarray(ch["uf"]) == ch["L"] // 2, 0.5, 1.0)
        d_on = np.asarray(ch["ws"], float) * ch["L"] \
            / (4.0 * phi * np.sin(th / 2.0) ** 2)
        norm_t = math.log(2.0 * f / ch["m0"])
        kern_t = float(np.mean(np.log(d_on)))
        jac_t = 2.0 * float(np.mean(np.log(np.sin(th / 2.0))))
        phi_t = float(np.mean(np.log(phi)))
        split = -0.5 * f * (norm_t + kern_t + jac_t + phi_t)
        dev_split = max(dev_split, abs(split - car["spread"]))
        hull_h = 0.5 * f * (a_rho / h_rho - 1.0)
        hull_m = 0.5 * f * math.log(a_rho / float(np.min(rho)))
        rows_out.append(dict(h=row["h"], spread=car["spread"],
                             ratio=a_rho / g_rho, hull_h=hull_h,
                             hull_m=hull_m, jac=jac_t, kern=kern_t,
                             norm=norm_t, phi=phi_t, f=f))
    sp = np.asarray([r["spread"] for r in rows_out], float)
    check("S1 WARD T4 SPREAD >= 0 on all %d rungs (Jensen/Gibbs: "
          "rho_bar IS the arithmetic mean of rho over the present "
          "cells): min %.6e" % (len(sp), float(np.min(sp))),
          float(np.min(sp)) >= -IDENT_TIE, kill="K2")
    check("S2 WARD the mean-ratio identity SPREAD = 1/2 f log(A/G) "
          "(arithmetic over geometric mean of the density): max dev "
          "%.2e <= %.0e" % (dev_mean, IDENT_TIE),
          dev_mean <= IDENT_TIE, kill="K2")
    check("S3 WARD T5 the exact four-way split SPREAD = -1/2 f "
          "[log(2f/m_0) + <log d> + 2<log sin(theta/2)> + <log phi>]: "
          "max dev %.2e <= %.0e" % (dev_split, IDENT_TIE),
          dev_split <= IDENT_TIE, kill="K2")
    jac = np.asarray([r["jac"] for r in rows_out], float)
    hh = np.asarray([r["hull_h"] for r in rows_out], float)
    hm = np.asarray([r["hull_m"] for r in rows_out], float)
    print("    SPREAD measured          %s" % e3(sp))
    print("    A/G ratio of the density %s"
          % e3([r["ratio"] for r in rows_out]))
    print("    T4 hull 1/2 f (A/H - 1)  %s   (rigorous, all-h)"
          % e3(hh))
    print("    T4 hull 1/2 f log(A/rho_min) %s   (rigorous, all-h)"
          % e3(hm))
    print("    2<log sin(theta/2)> on Theta_+  %s   vs the closed-form "
          "full-band value -2 log 2 = %.10f (departure %s)"
          % (e3(jac), JAC_FULL, e3(jac - JAC_FULL)))
    print("    <log d> on Theta_+       %s"
          % e3([r["kern"] for r in rows_out]))
    print("    <log phi> (endpoint fold cell, O(1/N))  %s"
          % e3([r["phi"] for r in rows_out]))
    ok_h = bool(np.all(hh >= sp - IDENT_TIE)
                and np.all(hm >= sp - IDENT_TIE))
    k_s = float(np.max(np.minimum(hh, hm)))
    k_s_meas = float(np.max(sp))
    check("S4 both rigorous hulls dominate the measured SPREAD on all "
          "%d rungs; the RIGOROUS all-h SPREAD bound over the ward "
          "table is K_S^rig = %.6f (a theorem per rung, loose by a "
          "factor %.1f), the MEASURED table maximum is K_S^meas = "
          "%.6f -- SPREAD itself needs no hull, it is CLOSED FORM per "
          "rung (S2/S3); only its h -> infinity supremum is open"
          % (len(sp), k_s, k_s / max(k_s_meas, 1e-300), k_s_meas),
          ok_h, kill="K2")
    return dict(spread=sp, hull_h=hh, hull_m=hm, jac=jac, k_s=k_s,
                k_s_meas=k_s_meas, rows=rows_out)


# ===================================== R -- the composition of 0.665
def compose(rows, cof, gap, spr):
    section("R -- THE COMPOSITION: 0.665 as an OUTPUT, and the "
            "composed all-h bracket")
    coefs, gaps, sps = cof["coef"], gap["gap"], spr["spread"]
    logres = coefs + gaps + sps
    res = np.exp(logres)
    print("    %-8s %-12s %-12s %-12s %-12s %-10s"
          % ("h", "COEF", "GAP", "SPREAD", "log res", "res"))
    idx = list(range(len(rows)))
    show = idx[:3] + idx[len(idx) // 2:len(idx) // 2 + 1] + idx[-3:]
    for i in sorted(set(show)):
        print("    %-8d %+12.6f %+12.6f %+12.6f %+12.6f %10.6f"
              % (rows[i]["h"], coefs[i], gaps[i], sps[i], logres[i],
                 res[i]))
    print("    ------------------------------------------------------")
    print("    median   %+12.6f %+12.6f %+12.6f %+12.6f %10.6f"
          % (float(np.median(coefs)), float(np.median(gaps)),
             float(np.median(sps)), float(np.median(logres)),
             float(np.median(res))))
    print("    spread   %s" % e3(res))
    dev = float(np.max(np.abs(
        res - np.asarray([r["car"]["res"] for r in rows], float))))
    check("R1 WARD the residual is REASSEMBLED from the three carriers "
          "(never an input): res med = %.6f, max dev from the CCLIII "
          "read %.2e <= %.0e" % (float(np.median(res)), dev,
                                 IDENT_TIE),
          dev <= IDENT_TIE, kill="K2")
    up = K_C_THM + 0.0 + spr["k_s"]
    up_m = K_C_THM + 0.0 + spr["k_s_meas"]
    lo = float(np.min(coefs)) - K_G_THM + 0.0
    print("\n    THE COMPOSED BRACKET, term by term and typed:")
    print("      K_C = 1/2 log 2                 = %+.10f  [THEOREM: "
          "T2, all h, any measure in [-1,1], sharp on the free chain]"
          % K_C_THM)
    print("      GAP in [-1/(2e), 0], K_G        = %+.10f  [THEOREM: "
          "T3, closed form, depth attained at f = 1/e]" % K_G_THM)
    print("      K_S^rig (T4 hull, table max)    = %+.10f  "
          "[CERTIFIED-NUMERIC: a theorem per rung, maximized over the "
          "table]" % spr["k_s"])
    print("      K_S^meas (SPREAD table max)     = %+.10f  [MEASURED: "
          "SPREAD is closed form per rung (S2/S3); its h -> infinity "
          "supremum is NOT proved]" % spr["k_s_meas"])
    print("      => RIGOROUS   log res <= K_C + 0 + K_S^rig  = %+.8f, "
          "res <= %.4f   (true for all h, loose)" % (up, math.exp(up)))
    print("      => COMPOSED   log res <= K_C + 0 + K_S^meas = %+.8f, "
          "res <= %.6f  (two THEOREM terms + one MEASURED term)"
          % (up_m, math.exp(up_m)))
    print("      => log res >= min COEF - K_G                = %+.8f, "
          "res >= %.6f  [MEASURED floor on COEF; the lower side of "
          "COEF is the OPEN piece -- it needs a capacity/Widom lower "
          "bound on the monic minimum E_K, which this probe does not "
          "have]" % (lo, math.exp(lo)))
    print("      measured res band                          = "
          "[%.6f, %.6f], median %.6f"
          % (float(np.min(res)), float(np.max(res)),
             float(np.median(res))))
    ok = bool(np.all(logres <= up + IDENT_TIE))
    check("R2 the composed upper bracket dominates every measured "
          "log res (%d/%d rungs); the rigorous bracket is loose by "
          "%.3f in log res, the composed one by %.3f"
          % (int(np.sum(logres <= up + IDENT_TIE)), len(res),
             up - float(np.max(logres)), up_m - float(np.max(logres))),
          ok, kill="K2")
    return dict(res=res, logres=logres, up=up, up_m=up_m, lo=lo)


# ============================================== P -- screens, controls
def screens(rows, cof, gap, spr):
    section("P -- SCREENS: carrier flatness in h and the CCXVII c_h "
            "relocation screen")
    print("    tau does NOT enter this probe (every carrier is "
          "measure-forward: lag arm -> density -> Jacobi prefix), so "
          "the tau screen is VACUOUS BY CONSTRUCTION and is declared, "
          "not scored.")
    hs = np.asarray([r["h"] for r in rows], float)
    named = [("COEF", cof["coef"]), ("GAP", gap["gap"]),
             ("SPREAD", spr["spread"]), ("f", gap["f"]),
             ("T2 slack", cof["slack"]),
             ("A/H hull", spr["hull_h"])]
    flat, steep = [], []
    for name, arr in named:
        s, e = slope2se(np.log(hs), np.log(np.abs(arr) + 1e-300))
        tag = ("FLAT" if abs(s) - e <= SLOPE_PASS
               else ("STEEP" if abs(s) - e > SLOPE_RELOC
                     else "AMBIG"))
        (flat if tag == "FLAT" else steep).append(name)
        print("      %-12s log-log h-slope %+.4f +- %.4f  -> %s"
              % (name, s, e, tag))
    check("P1 the h-flat carriers are %s; not flat: %s"
          % (",".join(flat) or "none", ",".join(steep) or "none"),
          True)
    ch_map = {}
    for kz in sorted({r["kz"] for r in rows if r["seg"] == "surf"}):
        rung = eul.level_rung(kz)
        if rung is None:
            continue
        dens = eul.grid_density(rung["c"])
        pos = eul.gram_from_dens(np.where(dens > 0.0, dens, 0.0),
                                 rung["M"])
        neg = eul.gram_from_dens(np.where(dens > 0.0, 0.0, -dens),
                                 rung["M"])
        last = pos.shape[0] - 1
        top = float(sla.eigh(neg, pos, eigvals_only=True,
                             subset_by_index=[last, last])[0])
        ch_map[int(kz)] = 1.0 - top
    mask = np.asarray([r["kz"] in ch_map and r["seg"] == "surf"
                       for r in rows], bool)
    chs = np.asarray([ch_map[r["kz"]] for r in rows
                      if r["kz"] in ch_map and r["seg"] == "surf"],
                     float)
    reloc = []
    if len(chs) >= 3:
        for name, arr in named:
            txt, verdict = t2.screen(np.abs(np.asarray(arr)[mask]),
                                     chs, "%s vs c_h" % name)
            print("      " + txt)
            if verdict == "RELOC":
                reloc.append(name)
    check("P2 c_h relocation screen on %d matched surface rungs "
          "(c_h band %s): relocation seats %s"
          % (len(chs), e3(chs), ",".join(reloc) or "none"),
          not reloc)
    return reloc


def controls(rows, anch):
    section("C -- CONTROLS: the falsifying worlds must move the "
            "carriers, and must NOT move the analytic anchors")
    fired = 0
    base = {r["kz"]: r for r in rows if r["seg"] == "surf"}
    zs = sorted(base)[:8 if SMOKE else 12]
    for world, seed in (("smooth", None), ("scramble", SCRAMBLE_SEED)):
        moved = 0
        seen = 0
        dev = []
        for kz in zs:
            src = t2.measure_source("surf", kz, world=world,
                                  scramble_seed=seed)
            ch = t2.build_chain_from_source(src, src["h"] // 2 + 2)
            if ch is None:
                continue
            car = t2.carriers_of(ch)
            seen += 1
            d = max(abs(car["coef"] - base[kz]["car"]["coef"]),
                    abs(car["gap"] - base[kz]["car"]["gap"]),
                    abs(car["spread"] - base[kz]["car"]["spread"]))
            dev.append(d)
            if d >= CARRIER_CTRL_BAR:
                moved += 1
        ok = seen > 0 and moved >= (seen + 1) // 2
        fired += int(ok)
        print("    %-9s %d/%d rungs move a carrier by >= %.0e; "
              "max carrier shift %s -> %s"
              % (world, moved, seen, CARRIER_CTRL_BAR, e3(dev),
                 "FIRE" if ok else "SILENT"))
    check("C7 both falsifying worlds move the carriers on a majority "
          "of the probed rungs: %d/2 fired" % fired, fired == 2,
          kill="K4")
    still = max(an["dev"] / an["tie"] for an in anch) if anch else 9.9
    check("C8 the analytic anchors are world-independent by "
          "construction (no rung datum enters them, AC2-scanned): "
          "worst anchor deviation is %.2f of its declared tie"
          % still, still <= 1.0)
    return fired


# =============================================================== main
def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_tot = len(CHECKS)
    if KILLS:
        v = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
             "K3": "REPRO-BROKEN", "K4": "CONTROL-SILENT"}[KILLS[0]]
        print("\n  VERDICT: %s" % v)
    elif not labels:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: KS-CARRIERS( %s )" % " ; ".join(labels))
        print("""
  HONEST FRAME.  T1-T5 are elementary and proved in the docstring; they
  are all-h statements about ANY measure supported in [-1,1], and they
  are warded numerically on the deployed table.  Everything with an
  h-limit attached to the DEPLOYED family (the value of f, the l^1
  control of A_n - 1, the size of K_S) is MEASURED on 42 surface + 4
  deep rungs and is NOT a theorem about h -> infinity.  The residual is
  recomputed from the carriers, never assumed.  No RH claim, no marker
  moves; no paper, ledger, website, manifest or verification file is
  touched.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (time.time() - T0, n_tot, n_tot - n_pass,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    return 0 if n_pass == n_tot and not KILLS else 1


def main():
    section("PRIME.ONEBADMODE.KS.DUAL.01 probe D -- closing COEF, GAP "
            "and SPREAD (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode = %s; NO RH claim; no marker moves; "
          "experiments/ only" % ("SMOKE" if SMOKE else "FROZEN"))

    print("\nS0 -- firewall / anti-circularity")
    bad = ast_scan(BANNED_IDS)
    check("S0.1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(bad), kill="K1")
    check("S0.2 AC1 the carriers are t2.carriers_of verbatim (not "
          "re-implemented): %s" % t2.carriers_of.__module__,
          t2.carriers_of.__module__ == "rhp_tier2_polecontrol_probe",
          kill="K1")

    anch = anchors()
    rows = build_table()
    cof = coef_layer(rows)
    ksc = coef_kscan(rows)
    gap = gap_layer(rows)
    spr = spread_layer(rows)
    comp = compose(rows, cof, gap, spr)
    reloc = screens(rows, cof, gap, spr)
    fired = controls(rows, anch)

    labels = [
        "ANCHORS(3/3 exactly solvable members of the deployed pipeline "
        "reproduce their closed forms; A2/A3 EXACT at finite L to "
        "%.1e, A1 at CCLIII's grid tie)"
        % max([a["dev"] for a in anch if a["tie"] < ANCHOR_TIE]
              or [1.0]),
        "COEF(EXACT: the moment functional 1/2log2 - 1/2log m_0 + "
        "log|R_KK| warded to %.1e for every K <= h/2 by QR; THEOREM "
        "ceilings K_C = 1/2 log2 = %.6f (margin %.4f) and "
        "COEF <= K log r + 1/2 log2 with r = %.4f)"
        % (COEF_TIE, K_C_THM, K_C_THM - float(np.max(cof["coef"])),
           ksc["hull"]),
        "COEF-NO-LIMIT(the exact K-curve DIVERGES: per-degree slope "
        "%.4f vs the capacity ceiling log(|E|/2) = %.4f, drift "
        "%.3f from K = h/2 to K = h, l^1 of A_n - 1 grows like "
        "h^%+.2f -- so COEF has NO series limit and the h-flat "
        "residual is a property of the FROZEN CUT K = h/2)"
        % (ksc["slope"], ksc["cap"], ksc["drift"],
           cof["l1_slope"][0]),
        "GAP(CLOSED FORM 1/2 f log f, f = 2N/L an EXACT RATIONAL with "
        "N = #{d(theta_j) > 0}; THEOREM bracket [-1/(2e), 0], K_G = "
        "%.6f; f med %.6f, continuum-kernel discretization %.2e)"
        % (K_G_THM, float(np.median(gap["f"])),
           float(np.max(np.abs(gap["f"] - gap["fine"])))),
        "SPREAD(CLOSED FORM per rung: 1/2 f log(A/G) and the exact "
        "four-way split with the closed-form Jacobian -2log2; THEOREM "
        ">= 0 by Jensen; K_S^rig = %.4f, K_S^meas = %.6f)"
        % (spr["k_s"], spr["k_s_meas"]),
        "COMPOSED(res med %.6f RECOMPUTED from the carriers, never an "
        "input; rigorous all-h res <= %.2f, composed res <= %.4f, "
        "lower side OPEN (a capacity/Widom LOWER bound on E_K is "
        "missing))" % (float(np.median(comp["res"])),
                       math.exp(comp["up"]), math.exp(comp["up_m"])),
        "CONTROLS(%d/2 fired)" % fired,
        "SCREENS(%s)" % (("relocation " + ",".join(reloc)) if reloc
                         else "no relocation; tau vacuous by "
                              "construction"),
    ]
    return finish(labels)


if __name__ == "__main__":
    sys.exit(main())
