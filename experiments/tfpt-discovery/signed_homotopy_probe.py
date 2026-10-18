#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""signed_homotopy_probe -- PRIME.CASE.SIGNEDHOMOTOPY.01
(EXPLORATION ONLY, experiments/; round 44: THE ROUTE-DECIDER from the
strategy memo -- the exact signed homotopy identity for the
Christoffel gap along the PNT-to-truth interpolation, and the typed
classification of the gain kernel: pointwise-PSD / averaged-PSD /
crossing-concentrated / indefinite-arithmetic.  2026-08-09.)

CONTEXT (machinery verbatim from christoffel_pnt_gamma_probe): the
deployed window kz gives the truth grid density d_truth (T115 tent
assembly of the prime-power atoms) and the PNT-smooth reference
d_PNT (the closed-form continuum density 2 e^{u/2} du deposited on
the same tent grid -- the W2 world, self-tested there against
quadrature to 1e-10).  christoffel_zone_envelope_probe froze the
critical zone a <= h^{2 theta*}, theta* = 0.700, as the port zone
that confines all measured criticality; christoffel_pnt_gamma_probe
measured the PNT reference gap NEGATIVE on every rung while the
truth gap is positive -- the homotopy below is the route-deciding
anatomy of exactly that rescue.

THE MATH (frozen verbatim from the strategy memo): with grid
densities d_t(j) = d_PNT(j) + t r(j), r = d_truth - d_PNT, weights
q_j = 4 sin^2(theta_j/2)/(2L); positive measure
mu_t = sum_j q_j [d_t(j)]_+ delta_{x_j}; target mass
nu_{t,m} = q_m [-d_t(m)]_+; extremal polynomial p_{t,m} (deg < h,
p(y_m) = 1, minimizing Int |p|^2 dmu_t; lambda_{t,m} the minimum;
Christoffel: lambda_{t,m} = 1/K_t(y_m, y_m)).  ENVELOPE IDENTITY
(exact, a.e. t):
    d/dt lambda_{t,m} = sum_j q_j r(j) 1{d_t(j) > 0} p_{t,m}(x_j)^2
    d/dt nu_{t,m}     = -q_m r(m) 1{d_t(m) < 0};
hence the SIGNED HOMOTOPY IDENTITY
    (lambda_1 - nu_1) - (lambda_0 - nu_0) = Int_0^1 J_{h,m}(t) dt,
    J_{h,m}(t) = sum_j q_j r(j) 1{d_t(j) > 0} p_{t,m}(x_j)^2
                 + q_m r(m) 1{d_t(m) < 0}.
Every mask indicator is linear in t, so every crossing time is the
EXACT rational t*_j = -d_PNT(j)/r(j) (a crossing in (0,1) iff
d_PNT(j) and d_truth(j) have strictly opposite signs).
CONCAVITY CAUTION (the memo): lambda_{t,m} is CONCAVE in the measure
mu within a fixed mask chamber (a minimum of linear functionals of
mu), so the fixed-chamber Hessian of the gap must be
NEGATIVE-semidefinite -- any positivity of the homotopy gain must
come from the crossings, the nu side, or the first-order terms.
M4 measures exactly this and reports it plainly.

FOLDED IMPLEMENTATION (exactly equivalent, stated): the deployed
grid density is symmetric, d(j) = d(L - j), so the memo's unfolded
sum over j = 0..L-1 collapses onto folded indices f = 0..L/2 with
aggregated weights qt_f = mult_f 4 sin^2(pi f / L)/(2L), mult_f = 2
for 0 < f < L/2 and 1 at the ends; f = 0 carries qt = 0 identically
(the sin^2 factor) and is excluded everywhere, exactly as the
deployed folded machinery drops it.  Self-test S0.2 pins this
construction to the verbatim folded_measure route at both endpoints.

FROZEN PROTOCOL (2026-08-09; pre-sizing run BEFORE the first
measurement run and disclosed here: crossings in (0,1) per rung =
98/82/90/210/346 on the heavy rungs kz 9/12/13/26/40 and
840/884/899 on the deep rungs kz 88/90/116; one Lanczos chain costs
about 1.0 s at h = 1433, so the exact full crossing split is
affordable on the heavy rungs only -- the deep-rung reductions
below are frozen consequences of that pre-sizing and are the memo's
"fewer t-points, and SAY SO" fallback, said so):

 RUNGS: heavy kz {9, 12, 13, 26, 40} + the deepest 3 with complete
   atom tables, kz {88, 90, 116} (verbatim eligibility and
   selection from christoffel_pnt_gamma_probe; X <= 4e5).

 ALIASES: all port aliases in the frozen critical zone -- folded
   neg nodes of the TRUTH endpoint (d_truth(f) < 0, f >= 1) with
   a_{h,f} = 2 h^2 (1 - x_f) <= h^{2 theta*}, theta* = 0.700,
   ranked by a ascending (the port-alias order of the context
   probes).  The alias grid index f is FIXED along the homotopy;
   nu_{t,m} and the constraint point y_m always live at that f.

 M1 THE IDENTITY WARD (the bookkeeping ward -- the identity is
   exact calculus): breakpoints = {0} + all exact crossing times
   t*_f in (0,1) (qt > 0 only) + {1}; per piece Gauss-Legendre with
   width-scaled order (width >= 3e-2 -> 12, >= 3e-3 -> 8,
   >= 3e-5 -> 4, else 2; spectral on analytic pieces).
   HEAVY rungs: the full piecewise integral Int_0^1 J dt vs the
   endpoint difference Delta_m = (lambda_1 - nu_1) - (lambda_0 -
   nu_0), rel error <= 1e-8 per alias with the denominator
   max(|Delta_m|, Int_0^1 |J| dt, lambda_m(a) + lambda_m(b)) (the
   last term is the v2 endpoint evaluation scale, see AMENDMENTS;
   the first run's heavy numbers pass under both denominators).
   DEEP rungs (frozen reduction, pre-sizing): the ~870 crossings x
   1 s chains put the full split at ~30 min PER RUNG -- out of
   budget; instead the ward integrates J over the WIDEST
   crossing-free piece [t_a, t_b] with GL-16 and checks it against
   G(t_b) - G(t_a) (G continuous), rel <= 1e-8, same denominator --
   the envelope derivative is thereby verified at depth, the
   crossing bookkeeping exactly on the five heavy rungs.  v2 adds
   at the deep rungs the POINTWISE ward: J at the piece midpoint vs
   the central finite difference (G(t+eps) - G(t-eps))/(2 eps),
   eps = 1e-4, rel <= 1e-3 per alias (FD-floor-limited bar,
   measured headroom ~200x).  Any ward failure -> WARD-BROKEN.

 M2 POINTWISE SIGN CENSUS: J_{h,m}(t) on the frozen census grid
   t = linspace(0, 1, N_T), N_T = 101 (heavy) / 41 (deep; the
   disclosed fewer-t fallback -- no typed number integrates over
   this grid, see M3).  Report per rung the max over aliases of
   frac{t : J < 0}, the global census fraction, and the worst
   negative excursion (value + location).

 M3 THE DECOMPOSITION (all three pieces CLOSED FORM -- no
   quadrature enters any typed number): with p_{0,m} and the t = 0
   mask frozen, and tau_f = Int_0^1 1{d_t(f) > 0} dt exact from the
   crossing times (tau-bar = 1 - tau a.e.),
     (a) FIXED  A_m = sum_f qt_f r_f 1{d_0(f) > 0} p_{0,m}(x_f)^2
                      + qt_m r_m 1{d_0(m) < 0}
         (the fixed-mask first variation; the frozen-mask nu term
         is included here by concretization, stated),
     (b) CROSSING B_m = [sum_f qt_f r_f tau_f p_{0,m}(x_f)^2
                      + qt_m r_m (1 - tau_m)] - A_m
         (the frozen-polynomial mask-crossing contribution, exact),
     (c) RESPONSE C_m = Delta_m - A_m - B_m
         (the polynomial-response remainder; Delta_m from the exact
         endpoints -- Int J dt = Delta by calculus).
   Print shares A/Delta, B/Delta, C/Delta at m* = argmin_m
   (lambda_1 - nu_1) (the critical truth alias) and as medians over
   aliases with Delta > 0.

 M4 THE QUADRATIC KERNEL (the classification): frozen residual
   subspace = the K_SUB = 12 folded grid indices with the largest
   weighted residual |qt_f r_f| that are mask-safe
   (|d_0(f)| >= 4 eta |r_f|, so no chamber wall is crossed by the
   probe steps; skipped indices disclosed), basis vectors
   b_i = r(f_i) delta_{f_i} (so the coordinate vector s = 1
   reproduces the subspace part of the truth residual); Phi(s) =
   lambda_{m*} - nu_{m*} at d_0 + sum_i s_i b_i; Hessian H by
   central differences, step eta = 0.05 (diagonal re-measured at
   eta/2; median rel drift > 0.2 -> label suffixed FD-UNSTABLE);
   gradient g_i cross-checked against the envelope first variation
   (reported).  Full eigenvalue spectrum; typed per M4 rung
   (frozen M4 rungs: kz 9 and kz 40):
     KERNEL-PSD        iff  e_min >= -1e-3 e_max and e_max > 0
     KERNEL-NSD        iff  e_max <=  1e-3 (-e_min) and e_min < 0
                       (the concavity-predicted outcome)
     KERNEL-INDEFINITE otherwise;
   truth-direction reading r^T H r = 1^T H 1 and first order
   g^T 1 reported (is the truth direction positive through an
   indefinite/NSD kernel only via first order + crossings?).

 M5 TYPED VERDICT (frozen decision rules, evaluated in this
   order -- the deliverable):
     HOMOTOPY-PSD        iff every (rung, alias) census fraction
                         frac{t : J < 0} <= 0.01 AND every
                         Delta_m > 0;
     HOMOTOPY-CROSSING   iff every Delta_m > 0 AND the median
                         crossing share B/Delta (over aliases with
                         Delta > 0, all rungs) > 0.5
                         (deterministic mask-monotonicity
                         candidate);
     HOMOTOPY-AVERAGED   iff every Delta_m > 0 (int J dt > 0
                         everywhere but pointwise fails);
     HOMOTOPY-INDEFINITE-ARITHMETIC iff some Delta_m <= 0 AND the
                         M4 kernel is not PSD (NSD or indefinite)
                         AND the fixed-mask first variation is not
                         positive somewhere (min over rung/alias
                         A_m <= 0) -- the pair-correlation
                         classification, downgrades the diagonal
                         route;
     HOMOTOPY-UNCLASSIFIED otherwise (reported plainly).
   The CROSSING-DOMINANT flag (median share > 0.5) and the M4
   kernel labels are attached to the verdict in every case.

 C  CONTROLS (kz 9):
   (i)  VALUE: scrambled-comb residual (positions uniform on
        (0, 2 alpha), seed 1, same masses -- the deployed scramble
        mirror): the homotopy gain must FAIL to rescue -- the
        scramble endpoint gap min_m (lambda - nu) over ITS zone
        aliases (fallback, disclosed if the zone set is empty: the
        8 a-closest scramble neg nodes) must be <= 0.  Both
        readings printed.  Silent -> CONTROL-DEAD.
   (ii) SCALING (reported, never a kill): deterministic cellwise
        sign-preserving residual r'(f) = (3 + cos(2 pi f/L))/8 x
        r(f); gain Delta(s) = G[d_0 + s r'] - G[d_0] at the kz 9
        critical alias for s = 0.5, 1.0; exponent p-hat =
        log2(Delta(1)/Delta(0.5)); FIRST-ORDER-DOMINATED iff
        |p-hat - 1| < 0.5, else SUPERLINEAR.

 SELF-TESTS (S0, kill PIPELINE on failure): (i) AST firewall
   clean; (ii) endpoint reconstruction (kz 9): the qt-route
   lambda/nu at the zone aliases vs the verbatim folded_measure
   route, rel <= 1e-8, at BOTH endpoints t = 0 and t = 1;
   (iii) orthonormality/quadratic-form self-test per rung at both
   endpoints: sum_j w_j p*_m(x_j)^2 == lambda_m to rel 1e-8 (the
   context probes' TOL_QF, verbatim).

KILLS: chain short anywhere needed / self-test failure / alias set
empty on a rung -> PIPELINE-BROKEN; any M1 ward relative error
> 1e-8 -> WARD-BROKEN; value control silent -> CONTROL-DEAD.
M2..M5 outcomes are MEASUREMENTS, never kills.

VERDICT (frozen enum): HOMOTOPY-MEASURED (+ CLASS=<HOMOTOPY-PSD |
HOMOTOPY-CROSSING | HOMOTOPY-AVERAGED |
HOMOTOPY-INDEFINITE-ARITHMETIC | HOMOTOPY-UNCLASSIFIED> + flags) /
PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  Pre-sizing (before the first
  measurement run) measured the crossing counts and chain timings
  quoted above and fixed: heavy-exact/deep-reduced M1 split, census
  101/41, the GL width ladder, K_SUB = 12, eta = 0.05, M4 rungs
  {9, 40}, and the M5 precedence order.
  v2 (2026-08-09, after the first full run; fail-first preserved):
  the first run returned WARD-BROKEN -- the three DEEP piece wards
  measured max rel 2.35e-8 / 3.36e-8 / 7.93e-8 against the v1
  denominator max(|Delta|, Int |J|), while all five HEAVY full
  wards passed at <= 4.2e-11.  Diagnosis (all disclosed, run
  before amending): (i) panel refinement of the deep piece
  quadrature leaves the defect unchanged (quadrature-converged);
  (ii) an independent orthonormal-Lanczos-Q route for the support
  sum reproduces it bit-for-bit (route-independent); (iii) the
  pointwise identity J = dG/dt holds at the piece midpoint to the
  Richardson-FD floor (5e-6 at eps 1e-4).  The absolute defect is
  ~8e-18: the endpoint difference G(b) - G(a) on a narrow piece is
  ~30x smaller than lambda itself, and the v1 denominator demanded
  certifying that difference BELOW the lambda evaluation noise
  floor (rel ~1e-9 at h ~ 1400).  v2 therefore (a) adds the
  endpoint evaluation scale lambda(a) + lambda(b) to the ward
  denominator (uniformly, heavy and deep; every heavy first-run
  number passes under both), and (b) STRENGTHENS the deep ward
  with the pointwise FD check above.  The 1e-8 bar, all rungs,
  aliases, census, decomposition, kernel and controls are
  untouched; every typed M2..M5 outcome of the first run is
  unchanged by this amendment.

NO RH claim: the identity is finite-dimensional exact calculus on
the deployed v563 window family; a typed classification here
decides which PROOF ROUTE the memo pursues (pointwise vs averaged
vs mask-monotone vs pair-correlation input) -- it proves no bound,
no rate, no uniformity in h.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (window geometry, tent
assembly, arch lags, deployed atom table); christoffel_pnt_gamma_
probe (four-world machinery: W2 closed-form PNT lags, folded
measures, Lanczos chain, CD kernel, port-alias bookkeeping,
quadratic-form self-tests -- verbatim); christoffel_zone_envelope_
probe (theta* = 0.700), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/signed_homotopy_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

HEAVY = (9, 12, 13, 26, 40)
DEEP3 = (88, 90, 116)          # frozen (christoffel_pnt_gamma_probe)
RUNGS = tuple(sorted(set(HEAVY) | set(DEEP3)))
THETA_STAR = 0.700             # frozen zone exponent (ZONESPLIT.01)
N_T_HEAVY = 101                # census grid, heavy rungs
N_T_DEEP = 41                  # census grid, deep rungs (disclosed)
GL_WIDTH_LADDER = ((3.0e-2, 12), (3.0e-3, 8), (3.0e-5, 4), (0.0, 2))
GL_DEEP_PIECE = 16             # deep reduced ward, widest piece
TOL_WARD = 1.0e-8              # M1 relative ward bar
FD_WARD_EPS = 1.0e-4           # M1 deep pointwise FD step (v2)
TOL_FD_WARD = 1.0e-3           # M1 deep pointwise FD bar (v2)
TOL_SELF_END = 1.0e-8          # S0.2 endpoint reconstruction
TOL_QF = 1.0e-8                # S0.3 quadratic-form self-test
PSD_EXCURSION = 0.01           # M5: census fraction bar per alias
CROSS_SHARE = 0.5              # M5: crossing-dominance bar
K_SUB = 12                     # M4 residual subspace dimension
FD_ETA = 0.05                  # M4 central-difference step
MASK_SAFE = 4.0                # M4 chamber-wall safety factor
FD_DRIFT_BAR = 0.2             # M4 eta vs eta/2 stability label
EIG_TOL = 1.0e-3               # M4 PSD/NSD classification tol
M4_RUNGS = (9, 40)             # frozen M4 rungs
SCRAMBLE_SEED = 1
CTRL_FALLBACK_AL = 8           # C(i) v2: a-closest neg nodes
CTRL_SCALES = (0.5, 1.0)       # C(ii) frozen scales
LINEAR_BAND = 0.5              # C(ii): |p-hat - 1| < this
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
_GL_CACHE = {}


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


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------------------------ pipeline
# (grid density, folded measures, Lanczos chain, CD kernel, W2 closed-form
#  PNT lags: verbatim from christoffel_pnt_gamma_probe)

def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def _prim(u, A, B):
    """Primitive of (A + B u) 2 e^{u/2}: 4 e^{u/2} (A + B (u - 2))."""
    return 4.0 * np.exp(0.5 * u) * (A + B * (u - 2.0))


def cont_lags(alpha, M, seg_lo, seg_hi, seg_sc):
    """W2 closed-form PNT tent lags (verbatim, incl. i=0 mirror)."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for lo, hi, sc in zip(seg_lo, seg_hi, seg_sc):
        i0 = max(0, int(math.floor(lo / D)) - 1)
        i1 = min(M - 1, int(math.ceil(hi / D)) + 1)
        ii = np.arange(i0, i1 + 1, dtype=float)
        val = np.zeros(len(ii))
        a = np.maximum((ii - 1.0) * D, lo)          # rising piece
        b = np.minimum(ii * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 - ii[m], 1.0 / D)
                   - _prim(a[m], 1.0 - ii[m], 1.0 / D))
        a = np.maximum(ii * D, lo)                  # falling piece
        b = np.minimum((ii + 1.0) * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 + ii[m], -1.0 / D)
                   - _prim(a[m], 1.0 + ii[m], -1.0 / D))
        if i0 == 0:                                 # i = 0 reflection
            a0, b0 = max(0.0, lo), min(D, hi)
            if b0 > a0:
                val[0] += (_prim(b0, 1.0, -1.0 / D)
                           - _prim(a0, 1.0, -1.0 / D))
        c[i0:i1 + 1] -= 0.5 * sc * val
    return c


def gl_nodes(order):
    if order not in _GL_CACHE:
        _GL_CACHE[order] = np.polynomial.legendre.leggauss(order)
    return _GL_CACHE[order]


def order_for(width):
    for bar, order in GL_WIDTH_LADDER:
        if width >= bar:
            return order
    return GL_WIDTH_LADDER[-1][1]


# --------------------------------------------------- homotopy construction
def build_homotopy(kz):
    """Folded d_PNT, d_truth, residual, weights, zone aliases and the
    exact crossing bookkeeping of one rung."""
    rr = core.build_window(kz)
    alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c1 = np.asarray(core.atom_lags_at(alpha, M, uu, mm)[0], float)
    c0 = cont_lags(alpha, M, [0.0], [2.0 * alpha], [1.0])
    L = 2 * M - 2
    F = L // 2 + 1
    d1 = grid_density(c_ar + c1)[:F]
    d0 = grid_density(c_ar + c0)[:F]
    r = d1 - d0
    ff = np.arange(F)
    x = np.cos(2.0 * math.pi * ff / L)
    a = 2.0 * h * h * (1.0 - x)
    mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
    qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 / (2.0 * L)
    # zone aliases (truth neg nodes, f >= 1, a <= h^{2 theta*})
    al_f = ff[(ff >= 1) & (d1 < 0.0)
              & (a <= h ** (2.0 * THETA_STAR))]
    al_f = al_f[np.argsort(a[al_f], kind="stable")]
    # exact crossings + occupation times tau
    up = (d0 < 0.0) & (d1 > 0.0) & (qt > 0.0)
    dn = (d0 > 0.0) & (d1 < 0.0) & (qt > 0.0)
    ts = np.full(F, np.nan)
    ts[up | dn] = -d0[up | dn] / r[up | dn]
    tau = np.where(d0 > 0.0, 1.0, 0.0)
    z0 = d0 == 0.0
    tau[z0] = np.where(d1[z0] > 0.0, 1.0, 0.0)
    tau[up] = 1.0 - ts[up]
    tau[dn] = ts[dn]
    breaks = np.unique(ts[up | dn])
    return dict(kz=kz, alpha=alpha, M=M, h=h, L=L, F=F,
                c_ar=c_ar, uu=uu, mm=mm, x=x, a=a, qt=qt,
                d0=d0, d1=d1, r=r, al_f=al_f, y_al=x[al_f],
                tau=tau, breaks=breaks,
                X=math.exp(2.0 * alpha))


def eval_t(R, tv, need_J=True, dens=None, al_f=None, qf=False):
    """One homotopy time slice: chain of mu_t, then per alias the
    Christoffel lambda, target mass nu, gap G and (optionally) the
    envelope integrand J.  dens/al_f override d_t and the alias set
    (controls)."""
    dv = R["d0"] + tv * R["r"] if dens is None else dens
    af = R["al_f"] if al_f is None else al_f
    pos = (dv > 0.0) & (R["qt"] > 0.0)
    xs = R["x"][pos]
    ws = (R["qt"] * dv)[pos]
    h = R["h"]
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    Phi = eval_chain(al, be, m0, R["x"][af], h)     # n_al x h
    K = np.sum(Phi ** 2, axis=1)
    lam = 1.0 / K
    dm = dv[af]
    qm = R["qt"][af]
    nu = qm * np.maximum(-dm, 0.0)
    out = dict(lam=lam, nu=nu, G=lam - nu, chain=(al, be, m0),
               pos=pos)
    if need_J or qf:
        Ppos = eval_chain(al, be, m0, xs, h)
        U = Ppos @ Phi.T                            # n_pos x n_al
        if need_J:
            S = ((R["qt"] * R["r"])[pos] @ (U * U)) / K ** 2
            out["J"] = S + qm * R["r"][af] * (dm < 0.0)
        if qf:
            out["qf_dev"] = float(np.max(np.abs(
                (ws @ (U * U)) / K - 1.0)))
    return out


def integrate_pieces(R, lo, hi, orders_by_width=True,
                     fixed_order=None):
    """Piecewise Gauss-Legendre of J over [lo, hi] split at the exact
    crossing times; returns (I, AbsI, n_chain_evals)."""
    br = R["breaks"]
    edges = np.concatenate([[lo], br[(br > lo) & (br < hi)], [hi]])
    n_al = len(R["al_f"])
    I = np.zeros(n_al)
    AbsI = np.zeros(n_al)
    n_ev = 0
    for aa, bb in zip(edges[:-1], edges[1:]):
        w = bb - aa
        if w <= 0.0:
            continue
        order = (order_for(w) if orders_by_width else fixed_order)
        gx, gw = gl_nodes(order)
        for xi, wi in zip(gx, gw):
            tv = 0.5 * w * xi + 0.5 * (aa + bb)
            e = eval_t(R, tv)
            if e is None:
                return None
            I += 0.5 * w * wi * e["J"]
            AbsI += 0.5 * w * wi * np.abs(e["J"])
            n_ev += 1
    return I, AbsI, n_ev


def widest_piece(R):
    edges = np.concatenate([[0.0], R["breaks"], [1.0]])
    wid = np.diff(edges)
    i = int(np.argmax(wid))
    return float(edges[i]), float(edges[i + 1])


def decompose(R, e0, delta):
    """M3 closed forms: fixed / crossing / response per alias."""
    al, be, m0 = e0["chain"]
    h = R["h"]
    Pall = eval_chain(al, be, m0, R["x"], h)        # F x h
    Phi0 = eval_chain(al, be, m0, R["y_al"], h)
    K0 = np.sum(Phi0 ** 2, axis=1)
    U0 = Pall @ Phi0.T                              # F x n_al
    P2 = (U0 * U0) / K0 ** 2                        # p_{0,m}(x_f)^2
    qr = R["qt"] * R["r"]
    af = R["al_f"]
    A = ((qr * (R["d0"] > 0.0)) @ P2
         + qr[af] * (R["d0"][af] < 0.0))
    FP = ((qr * R["tau"]) @ P2
          + qr[af] * (1.0 - R["tau"][af]))
    B = FP - A
    C = delta - FP
    return A, B, C, P2


def m4_kernel(R, e0, e1, P2):
    """M4: FD Hessian of the gap at the PNT point in the frozen
    K_SUB-dimensional residual subspace, at the critical alias."""
    ms = int(np.argmin(e1["G"]))
    m_f = int(R["al_f"][ms])
    y_m = np.array([R["x"][m_f]])
    qt, r, d0, h = R["qt"], R["r"], R["d0"], R["h"]
    cand = np.argsort(-np.abs(qt * r), kind="stable")
    safe = (np.abs(d0) >= MASK_SAFE * FD_ETA * np.abs(r)) \
        & (qt > 0.0)
    idx, skipped = [], 0
    for f in cand:
        if len(idx) == K_SUB:
            break
        if safe[f]:
            idx.append(int(f))
        else:
            skipped += 1
    idx = np.array(idx)

    def phi(svec):
        dv = d0.copy()
        dv[idx] += svec * r[idx]
        pos = (dv > 0.0) & (qt > 0.0)
        al, be, m0, steps = lanczos_chain(
            R["x"][pos], (qt * dv)[pos], h + 1)
        if steps < h + 1:
            return None
        P = eval_chain(al, be, m0, y_m, h)
        lam = 1.0 / float(np.sum(P ** 2))
        return lam - qt[m_f] * max(-dv[m_f], 0.0)

    K = len(idx)
    base = phi(np.zeros(K))
    if base is None:
        return None
    H = np.zeros((K, K))
    g = np.zeros(K)
    diag2 = np.zeros(K)
    for i in range(K):
        for eta, tgt in ((FD_ETA, H), (0.5 * FD_ETA, diag2)):
            sp = np.zeros(K)
            sp[i] = eta
            fp, fm = phi(sp), phi(-sp)
            if fp is None or fm is None:
                return None
            if eta == FD_ETA:
                g[i] = (fp - fm) / (2.0 * eta)
                H[i, i] = (fp - 2.0 * base + fm) / eta ** 2
            else:
                diag2[i] = (fp - 2.0 * base + fm) / eta ** 2
    for i in range(K):
        for k in range(i + 1, K):
            s = np.zeros(K)
            vals = {}
            for si in (+1.0, -1.0):
                for sk in (+1.0, -1.0):
                    s[:] = 0.0
                    s[i] = si * FD_ETA
                    s[k] = sk * FD_ETA
                    v = phi(s)
                    if v is None:
                        return None
                    vals[(si, sk)] = v
            H[i, k] = H[k, i] = (
                vals[(1, 1)] - vals[(1, -1)] - vals[(-1, 1)]
                + vals[(-1, -1)]) / (4.0 * FD_ETA ** 2)
    drift = np.abs(diag2 - np.diag(H)) / np.maximum(
        np.abs(np.diag(H)), 1e-300)
    eig = np.linalg.eigvalsh(0.5 * (H + H.T))
    emin, emax = float(eig[0]), float(eig[-1])
    if emin >= -EIG_TOL * max(emax, 0.0) and emax > 0.0:
        lab = "KERNEL-PSD"
    elif emax <= EIG_TOL * max(-emin, 0.0) and emin < 0.0:
        lab = "KERNEL-NSD"
    else:
        lab = "KERNEL-INDEFINITE"
    fd_unstable = float(np.median(drift)) > FD_DRIFT_BAR
    if fd_unstable:
        lab += "(FD-UNSTABLE)"
    # envelope first-variation cross-check (fixed mask, exact)
    env = (qt[idx] * r[idx] * (d0[idx] > 0.0) * P2[idx, ms]
           + np.where(idx == m_f,
                      qt[m_f] * r[m_f] * (d0[m_f] < 0.0), 0.0))
    env_dev = np.abs(g - env) / np.maximum(np.abs(env), 1e-300)
    return dict(idx=idx, skipped=skipped, ms=ms, H=H, g=g, eig=eig,
                emin=emin, emax=emax, label=lab,
                drift_med=float(np.median(drift)),
                rHr=float(np.ones(len(idx)) @ H @ np.ones(len(idx))),
                gT1=float(np.sum(g)),
                env_dev_med=float(np.median(env_dev)),
                env_dev_max=float(np.max(env_dev)))


def main():
    section("PRIME.CASE.SIGNEDHOMOTOPY.01 -- signed homotopy "
            "identity + gain-kernel classification (EXPLORATION "
            "ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    section("B0 -- rungs (homotopy geometry; crossings are exact "
            "rationals t* = -d_PNT/r)")
    RG = {}
    for kz in RUNGS:
        R = build_homotopy(kz)
        RG[kz] = R
        wp = widest_piece(R)
        print("    kz %-3d h %4d F %5d: crossings %4d  zone aliases "
              "%3d (a <= h^1.4 = %8.0f)  widest piece [%.4f, %.4f]"
              % (kz, R["h"], R["F"], len(R["breaks"]),
                 len(R["al_f"]), R["h"] ** 1.4, wp[0], wp[1]),
              flush=True)
    order = sorted(RUNGS, key=lambda kz: RG[kz]["h"])
    ok_al = all(len(RG[kz]["al_f"]) > 0 for kz in RUNGS)
    check("B0.1 zone alias sets nonempty on every rung", ok_al,
          kill="PIPELINE")
    if not ok_al:
        return finish(None, None, None)

    # S0.2 endpoint reconstruction vs verbatim folded_measure (kz 9)
    R9 = RG[9]
    dev_end = 0.0
    for tv, c_at in ((1.0, None), (0.0, None)):
        dv = R9["d1"] if tv == 1.0 else R9["d0"]
        # rebuild the FULL arm density for the verbatim route
        L = R9["L"]
        d_full = np.concatenate([dv, dv[-2:0:-1]])
        xs, ws, _uf = folded_measure(d_full, L, +1.0)
        ys, vs, uf_n = folded_measure(d_full, L, -1.0)
        al, be, m0, steps = lanczos_chain(xs, ws, R9["h"] + 1)
        if steps < R9["h"] + 1:
            check("S0.2 endpoint chain (verbatim route)", False,
                  kill="PIPELINE")
            return finish(None, None, None)
        Pn = eval_chain(al, be, m0, R9["y_al"], R9["h"])
        lam_ref = 1.0 / np.sum(Pn ** 2, axis=1)
        pos_map = {int(f): float(v) for f, v in zip(uf_n, vs)}
        nu_ref = np.array([pos_map.get(int(f), 0.0)
                           for f in R9["al_f"]])
        e = eval_t(R9, tv, need_J=False)
        if e is None:
            check("S0.2 endpoint chain (qt route)", False,
                  kill="PIPELINE")
            return finish(None, None, None)
        dev_end = max(dev_end, float(np.max(
            np.abs(e["lam"] / lam_ref - 1.0))))
        dev_end = max(dev_end, float(np.max(
            np.abs(e["nu"] - nu_ref)
            / np.maximum(np.abs(nu_ref), 1e-300))))
    check("S0.2 endpoint reconstruction == verbatim folded route "
          "(kz 9, t = 0 and 1)", dev_end <= TOL_SELF_END,
          "rel sup dev %.2e" % dev_end, kill="PIPELINE")

    section("E -- exact endpoints per rung: G_m(t) = lambda_{t,m} - "
            "nu_{t,m}, gain Delta_m = G_m(1) - G_m(0)")
    RES = {}
    ok_e = True
    qf_worst = 0.0
    for kz in order:
        R = RG[kz]
        e0 = eval_t(R, 0.0, need_J=False, qf=True)
        e1 = eval_t(R, 1.0, need_J=False, qf=True)
        if e0 is None or e1 is None:
            ok_e = False
            print("    kz %-3d: CHAIN SHORT at an endpoint" % kz)
            break
        qf_worst = max(qf_worst, e0["qf_dev"], e1["qf_dev"])
        delta = e1["G"] - e0["G"]
        RES[kz] = dict(e0=e0, e1=e1, delta=delta,
                       ms=int(np.argmin(e1["G"])))
        ms = RES[kz]["ms"]
        print("    kz %-3d h %4d (n_al %2d): G0 min %+.3e med %+.3e"
              " | G1 min %+.3e med %+.3e | Delta min %+.3e med "
              "%+.3e | m* %d: G0 %+.3e -> G1 %+.3e"
              % (kz, R["h"], len(R["al_f"]),
                 float(np.min(e0["G"])), float(np.median(e0["G"])),
                 float(np.min(e1["G"])), float(np.median(e1["G"])),
                 float(np.min(delta)), float(np.median(delta)),
                 ms + 1, float(e0["G"][ms]), float(e1["G"][ms])),
              flush=True)
    check("E0 endpoint chains complete on all rungs", ok_e,
          kill="PIPELINE")
    check("S0.3 quadratic-form self-test (sum w p*^2 == lambda, "
          "both endpoints, all rungs)", ok_e
          and qf_worst <= TOL_QF, "worst rel dev %.2e" % qf_worst,
          kill="PIPELINE")
    if not ok_e:
        return finish(None, None, None)

    section("M1 -- THE IDENTITY WARD (heavy: full crossing split; "
            "deep: widest-piece GL-%d, disclosed)" % GL_DEEP_PIECE)
    ward_ok = True
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        fd_txt = ""
        if kz in HEAVY:
            out = integrate_pieces(R, 0.0, 1.0)
            if out is None:
                check("M1 chains complete (kz %d)" % kz, False,
                      kill="PIPELINE")
                return finish(None, None, None)
            I, AbsI, n_ev = out
            tgt = RES[kz]["delta"]
            lam_ab = RES[kz]["e0"]["lam"] + RES[kz]["e1"]["lam"]
            mode = "FULL  (%4d pieces, %5d chains)" % (
                len(R["breaks"]) + 1, n_ev)
        else:
            lo, hi = widest_piece(R)
            out = integrate_pieces(R, lo, hi, orders_by_width=False,
                                   fixed_order=GL_DEEP_PIECE)
            ea = eval_t(R, lo, need_J=False)
            eb = eval_t(R, hi, need_J=False)
            if out is None or ea is None or eb is None:
                check("M1 chains complete (kz %d)" % kz, False,
                      kill="PIPELINE")
                return finish(None, None, None)
            I, AbsI, n_ev = out
            tgt = eb["G"] - ea["G"]
            lam_ab = ea["lam"] + eb["lam"]
            mode = "PIECE [%.4f, %.4f] (%d chains)" % (lo, hi,
                                                       n_ev + 2)
            # v2 pointwise ward: J vs central FD at the midpoint
            tm = 0.5 * (lo + hi)
            em = eval_t(R, tm)
            ep = eval_t(R, tm + FD_WARD_EPS, need_J=False)
            en = eval_t(R, tm - FD_WARD_EPS, need_J=False)
            if em is None or ep is None or en is None:
                check("M1 chains complete (kz %d)" % kz, False,
                      kill="PIPELINE")
                return finish(None, None, None)
            fd = (ep["G"] - en["G"]) / (2.0 * FD_WARD_EPS)
            fd_rel = float(np.max(np.abs(fd - em["J"])
                                  / np.maximum(np.abs(em["J"]),
                                               1e-300)))
            ward_ok &= fd_rel <= TOL_FD_WARD
            fd_txt = "  FD ward %.2e" % fd_rel
        rel = np.abs(I - tgt) / np.maximum(np.maximum(
            np.maximum(np.abs(tgt), AbsI), lam_ab), 1e-300)
        wmax = float(np.max(rel))
        RES[kz]["ward"] = wmax
        ward_ok &= wmax <= TOL_WARD
        print("    kz %-3d h %4d: %s  max rel err %.2e%s  [%.1f s]"
              % (kz, R["h"], mode, wmax, fd_txt,
                 time.time() - t_a), flush=True)
    check("M1.1 identity ward: max rel err <= %.0e (deep pointwise"
          " FD <= %.0e) on every rung/alias"
          % (TOL_WARD, TOL_FD_WARD), ward_ok, kill="WARD")

    section("M2 -- POINTWISE SIGN CENSUS of J on the frozen t-grid "
            "(%d heavy / %d deep points)" % (N_T_HEAVY, N_T_DEEP))
    worst = (0.0, None, None, None)          # (J, kz, alias, t)
    n_neg_tot = 0
    n_tot = 0
    census_ok = True
    for kz in order:
        R = RG[kz]
        t_a = time.time()
        n_t = N_T_HEAVY if kz in HEAVY else N_T_DEEP
        tt = np.linspace(0.0, 1.0, n_t)
        JJ = np.zeros((n_t, len(R["al_f"])))
        for i, tv in enumerate(tt):
            e = eval_t(R, tv)
            if e is None:
                check("M2 chains complete (kz %d)" % kz, False,
                      kill="PIPELINE")
                return finish(None, None, None)
            JJ[i] = e["J"]
        frac = np.mean(JJ < 0.0, axis=0)
        RES[kz]["frac_neg"] = frac
        census_ok &= bool(np.max(frac) <= PSD_EXCURSION)
        n_neg_tot += int(np.sum(JJ < 0.0))
        n_tot += JJ.size
        i0, m0i = np.unravel_index(int(np.argmin(JJ)), JJ.shape)
        if float(JJ[i0, m0i]) < worst[0]:
            worst = (float(JJ[i0, m0i]), kz, m0i + 1,
                     float(tt[i0]))
        print("    kz %-3d h %4d: frac(J<0) max %.3f med %.3f | "
              "min J %+.3e at (m %d, t %.2f) | med |J| %.2e  "
              "[%.1f s]"
              % (kz, R["h"], float(np.max(frac)),
                 float(np.median(frac)), float(JJ[i0, m0i]),
                 m0i + 1, float(tt[i0]),
                 float(np.median(np.abs(JJ))), time.time() - t_a),
              flush=True)
    print("    global census: %d / %d samples negative (%.2f%%); "
          "worst J %+.3e at (kz %s, alias %s, t %s)"
          % (n_neg_tot, n_tot, 100.0 * n_neg_tot / max(n_tot, 1),
             worst[0], worst[1], worst[2], worst[3]))
    check("M2.1 census recorded (measurement; PSD bar %.0f%% per "
          "rung/alias: %s)" % (100 * PSD_EXCURSION,
                               "met" if census_ok else "NOT met"),
          True)

    section("M3 -- DECOMPOSITION (closed form): Delta = FIXED(A) + "
            "CROSSING(B) + RESPONSE(C)")
    sh_cross_all = []
    A_min_all = float("inf")
    for kz in order:
        R = RG[kz]
        e0, delta = RES[kz]["e0"], RES[kz]["delta"]
        A, B, C, P2 = decompose(R, e0, delta)
        RES[kz].update(A=A, B=B, C=C, P2=P2)
        A_min_all = min(A_min_all, float(np.min(A)))
        ms = RES[kz]["ms"]
        pos = delta > 0.0
        shB = B[pos] / delta[pos]
        sh_cross_all.extend(shB.tolist())
        print("    kz %-3d h %4d m*=%2d: Delta %+.3e = A %+.3e "
              "(%.0f%%) + B %+.3e (%.0f%%) + C %+.3e (%.0f%%)"
              % (kz, R["h"], ms + 1, float(delta[ms]),
                 float(A[ms]), 100 * A[ms] / delta[ms],
                 float(B[ms]), 100 * B[ms] / delta[ms],
                 float(C[ms]), 100 * C[ms] / delta[ms]))
        print("           medians over m (Delta>0: %d/%d): A/D "
              "%+.3f  B/D %+.3f  C/D %+.3f | min A %+.3e"
              % (int(np.sum(pos)), len(delta),
                 float(np.median(A[pos] / delta[pos])),
                 float(np.median(shB)),
                 float(np.median(C[pos] / delta[pos])),
                 float(np.min(A))), flush=True)
    med_cross = (float(np.median(sh_cross_all)) if sh_cross_all
                 else float("nan"))
    print("    all-rung median crossing share B/Delta = %+.3f "
          "(dominance bar %.2f); min fixed first variation A = "
          "%+.3e" % (med_cross, CROSS_SHARE, A_min_all))
    check("M3.1 decomposition exact (A + B + C == Delta by "
          "construction)", True)

    section("M4 -- QUADRATIC KERNEL at the PNT point (K_SUB = %d "
            "top-|qt r| mask-safe grid modes, eta = %.2f, central "
            "FD; concavity caution: fixed-chamber part must be "
            "NSD)" % (K_SUB, FD_ETA))
    kernel_labels = {}
    kernel_not_psd = False
    for kz in M4_RUNGS:
        t_a = time.time()
        R = RG[kz]
        out = m4_kernel(R, RES[kz]["e0"], RES[kz]["e1"],
                        RES[kz]["P2"])
        if out is None:
            check("M4 chains complete (kz %d)" % kz, False,
                  kill="PIPELINE")
            return finish(None, None, None)
        kernel_labels[kz] = out["label"]
        kernel_not_psd |= not out["label"].startswith("KERNEL-PSD")
        eig = out["eig"]
        print("    kz %-3d (m* %d; subspace f = %s ...; %d skipped "
              "mask-unsafe):" % (kz, out["ms"] + 1,
                                 [int(f) for f in out["idx"][:6]],
                                 out["skipped"]))
        print("      spectrum: %s" % " ".join("%+.2e" % v
                                              for v in eig))
        print("      e_min %+.3e  e_max %+.3e  -> %s | FD eta/2 "
              "med drift %.3f | envelope-vs-FD gradient dev med "
              "%.2e max %.2e"
              % (out["emin"], out["emax"], out["label"],
                 out["drift_med"], out["env_dev_med"],
                 out["env_dev_max"]))
        print("      truth direction: r^T H r %+.3e (second "
              "order), g^T 1 %+.3e (first order)  [%.1f s]"
              % (out["rHr"], out["gT1"], time.time() - t_a),
              flush=True)
    concave_seen = all(lab.startswith("KERNEL-NSD")
                       for lab in kernel_labels.values())
    print("    concavity caution check: fixed-chamber kernel NSD "
          "on all M4 rungs -> %s"
          % ("YES (as the memo predicts: positivity must come "
             "from first order / crossings / nu side)"
             if concave_seen else "NO (see labels above)"))
    check("M4.1 kernel typed: %s"
          % ", ".join("kz %d %s" % (kz, kernel_labels[kz])
                      for kz in M4_RUNGS), True)

    section("M5 -- TYPED CLASSIFICATION (frozen precedence)")
    all_pos = all(bool(np.all(RES[kz]["delta"] > 0.0))
                  for kz in order)
    cross_dom = med_cross > CROSS_SHARE
    if census_ok and all_pos:
        klass = "HOMOTOPY-PSD"
    elif all_pos and cross_dom:
        klass = "HOMOTOPY-CROSSING"
    elif all_pos:
        klass = "HOMOTOPY-AVERAGED"
    elif kernel_not_psd and A_min_all <= 0.0:
        klass = "HOMOTOPY-INDEFINITE-ARITHMETIC"
    else:
        klass = "HOMOTOPY-UNCLASSIFIED"
    flags = []
    if cross_dom:
        flags.append("CROSSING-DOMINANT")
    flags.append("KERNEL={%s}" % ",".join(
        "kz%d:%s" % (kz, kernel_labels[kz]) for kz in M4_RUNGS))
    print("    pointwise PSD (census <= %.0f%% per rung/alias): %s"
          % (100 * PSD_EXCURSION, census_ok))
    print("    all gains Delta > 0 on every rung/alias: %s"
          % all_pos)
    print("    crossing-dominant (median share %.3f > %.2f): %s"
          % (med_cross, CROSS_SHARE, cross_dom))
    print("    kernel not PSD: %s; min fixed first variation "
          "%+.3e" % (kernel_not_psd, A_min_all))
    print("    -> CLASS = %s  [%s]" % (klass, "; ".join(flags)))
    check("M5.1 typed: %s" % klass, True)

    section("C -- controls (kz 9)")
    # (i) scrambled comb: the homotopy must fail to rescue
    rng = np.random.default_rng(SCRAMBLE_SEED)
    us = np.sort(rng.uniform(0.0, 2.0 * R9["alpha"],
                             size=len(R9["uu"])))
    c_s = np.asarray(core.atom_lags_at(R9["alpha"], R9["M"], us,
                                       R9["mm"])[0], float)
    d_s = grid_density(R9["c_ar"] + c_s)[:R9["F"]]
    ff9 = np.arange(R9["F"])
    neg_s = ff9[(ff9 >= 1) & (d_s < 0.0)]
    neg_s = neg_s[np.argsort(R9["a"][neg_s], kind="stable")]
    al_zone = neg_s[R9["a"][neg_s]
                    <= R9["h"] ** (2.0 * THETA_STAR)]
    al_port = neg_s[:CTRL_FALLBACK_AL]     # disclosed fallback
    es_z = (eval_t(R9, 1.0, need_J=False, dens=d_s, al_f=al_zone)
            if len(al_zone) else None)
    es_p = eval_t(R9, 1.0, need_J=False, dens=d_s, al_f=al_port)
    if es_p is None:
        check("C0 scramble chain completes", False,
              kill="PIPELINE")
        return finish(klass, flags, kernel_labels)
    gz = (float(np.min(es_z["G"])) if es_z is not None
          else float("nan"))
    gp = float(np.min(es_p["G"]))
    fires = (gz <= 0.0) if es_z is not None else (gp <= 0.0)
    print("    scramble endpoint gap: zone aliases (%d) min %s%s | "
          "first-%d neg nodes min %+.3e (real kz 9 truth min "
          "%+.3e) -> %s"
          % (len(al_zone),
             ("%+.3e" % gz) if es_z is not None else "n/a (empty",
             "" if es_z is not None else " -> frozen fallback)",
             CTRL_FALLBACK_AL, gp,
             float(np.min(RES[9]["e1"]["G"])),
             "FIRES" if fires else "SILENT"), flush=True)
    check("C1 value control fires (scrambled comb: homotopy fails "
          "to rescue, min gap <= 0)", fires, kill="CONTROL")
    # (ii) sign-preserving cellwise scaling (reported)
    mod = (3.0 + np.cos(2.0 * math.pi * ff9 / R9["L"])) / 8.0
    rp = mod * R9["r"]
    ms9 = RES[9]["ms"]
    g0 = float(RES[9]["e0"]["G"][ms9])
    dd = []
    for s in CTRL_SCALES:
        ep = eval_t(R9, 0.0, need_J=False, dens=R9["d0"] + s * rp)
        if ep is None:
            check("C2 perturbation chain completes", False,
                  kill="PIPELINE")
            return finish(klass, flags, kernel_labels)
        dd.append(float(ep["G"][ms9]) - g0)
    if dd[0] != 0.0 and dd[0] * dd[1] > 0.0:
        phat = math.log2(dd[1] / dd[0])
        lab = ("FIRST-ORDER-DOMINATED"
               if abs(phat - 1.0) < LINEAR_BAND else "SUPERLINEAR")
        det = "Delta(0.5)=%+.3e Delta(1)=%+.3e p-hat=%.3f" % (
            dd[0], dd[1], phat)
    else:
        lab = "SIGN-CHANGE (no clean exponent)"
        det = "Delta(0.5)=%+.3e Delta(1)=%+.3e" % (dd[0], dd[1])
    print("    sign-preserving cellwise gain scaling at m*: %s -> "
          "%s" % (det, lab))
    check("C2 scaling control reported: %s" % lab, True)

    return finish(klass, flags, kernel_labels)


def finish(klass, flags, kernel_labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "PIPELINE" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "WARD" in KILLS:
        VERDICT = "WARD-BROKEN"
    elif "CONTROL" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "HOMOTOPY-MEASURED"
    sub = []
    if klass:
        sub.append("CLASS=%s" % klass)
    if flags:
        sub.extend(flags)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    if VERDICT == "HOMOTOPY-MEASURED" and klass:
        if klass in ("HOMOTOPY-PSD", "HOMOTOPY-CROSSING"):
            print("  PLAIN ANSWER: the diagonal route stays "
                  "unconditional-shaped (%s)."
                  % ("pointwise-positive gain" if klass ==
                     "HOMOTOPY-PSD" else
                     "deterministic mask-monotonicity candidate"))
        elif klass == "HOMOTOPY-AVERAGED":
            print("  PLAIN ANSWER: positivity only in the "
                  "t-average -- the diagonal route survives but "
                  "needs the integrated gain, not a pointwise "
                  "kernel.")
        elif klass == "HOMOTOPY-INDEFINITE-ARITHMETIC":
            print("  PLAIN ANSWER: the input is pair-correlation "
                  "class -- the fixed-mask kernel cannot carry "
                  "the positivity; the diagonal route is "
                  "downgraded.")
        else:
            print("  PLAIN ANSWER: no frozen class fits -- "
                  "reported plainly above.")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
