#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""euler_rouche_probe -- PRIME.PORT.EULER.ROUCHE.01
(EXPLORATION ONLY, experiments/; round 51, reviewer priority 3:
the matrix-Rouche form of corridor inheritance -- can ONE norm
bound on a contour force the Euler extension step h -> h+1 to
preserve the determinant-zero count inside the corridor?
2026-08-09.)

THE QUESTION (frozen).  port_sflow_toda_probe measured: the
truth corridor is pole-free on s in [0, 1] -- for A_h(s) =
I - s C_h on the fixed 12-window the first determinant zero
sits at s*_h = 1/lam_max(C_h) > 1 on every full-window rung,
while the smooth-mass world violates its wall (s* <= 1).
factor_avoidance_euler_probe measured the one-step increments
Delta C = C_{h+1} - C_h.  THE ROUCHE FORM asked here: on a
closed contour Gamma enclosing the physical corridor [0, 1],
does
    M_h := sup_{s in Gamma} ||A_h(s)^{-1} Delta_h(s)||_2 < 1,
    Delta_h(s) := A_{h+1}(s) - A_h(s) = -s (C_{h+1} - C_h)
hold on truth?  THE ROUCHE STATEMENT (exact, elementary): if
A_h(s) is invertible for every s on Gamma and M_h < 1, then
det A_{h+1} = det A_h * det(I + A_h^{-1} Delta_h) and the
homotopy A^(t) := A_h + t Delta_h (t in [0, 1]) satisfies
||A_h^{-1} t Delta_h|| <= t M_h < 1 on Gamma, so det A^(t)(s)
!= 0 for every s on Gamma and every t; the argument-principle
count of determinant zeros of A^(t) inside Gamma is a
continuous integer in t, hence CONSTANT: A_h and A_{h+1} have
the SAME zero count inside Gamma.  On truth that count is 0 --
NO Euler extension step can pull a pole into the corridor
while the sup bound holds.  Delta is s-PROPORTIONAL in this
affine family: the |s| factor is carried exactly.  The mirror
question: does the SAME mechanism FAIL (M >= 1 / contour
undrawable) on the smooth world exactly where its corridor
actually contains zeros?

CONTOUR-CHOICE HONESTY (stated up front, frozen): Gamma is the
rectangle Re s in [-delta_0, 1 + delta_1], Im s in [-b, +b],
delta_0 = 0.1, b = 0.3.  Variant A (TARGET-INFORMED): per pair
delta_1 = min over the two rungs of (s*_h - 1)/2.  This uses
the TARGET rung's pole location -- fine for the MEASUREMENT
(we ask whether the mechanism exists), but a self-contained
theorem must choose the contour from the source side.  Variant
B (FIXED): one contour for the whole ladder with delta_1^fix =
tau-law/2 -- the h-trend law log(s*_h - 1) = c0 + c1 log h
(the PRIME.PORT.SFLOW.01 S4 pole-distance law) evaluated at
the deepest ladder depth h_max, halved:
    delta_1^fix = exp(c0) * h_max^c1 / 2.
HONEST LIMIT of variant B: the law's coefficients are fitted
across the whole truth ladder, so it is source-legitimate in
FORM only (a single fixed contour, no per-target pole is
consulted); a self-contained theorem needs the margin law
itself derived from the source side (open).  Both variants are
frozen and both are reported.

THE LADDER (frozen, factor_avoidance verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive FULL-WINDOW pairs (both rungs carry all 12 indices
of J = {2, 4, ..., 24}); truth + smooth-mass world (B1
LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n, midpoint cells,
lattice_parametrix verbatim); Epstein/scramble frame status
reported (C1).

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 G1  THE CONTOUR: per truth full-window rung the exact pole
     s*_h = 1/lam_max(C_h) (symmetric eig; sflow identity
     (iii)); LS fit of log(s*_h - 1) vs log h over the truth
     full-window rungs -> delta_1^fix as above; per pair the
     variant-A delta_1.  Discretization (frozen, 80 points,
     denser near s = 1 + delta_1): right edge 32 points at
     Im = b*v|v|, v uniform in [-1, 1] (quadratic clustering
     toward the real axis); top and bottom edges 20 points
     each at Re = (1+delta_1) - (1+delta_1+delta_0)(1-t)^2,
     t uniform in [0, 1] (clustering toward the right corner);
     left edge 8 points uniform.

 G2  THE SUP LEDGER: per full-window step and per contour
     variant M_h = max over the 80 frozen points of
     |s| * ||(I - s C_h)^{-1} (C_{h+1} - C_h)||_2 (exact
     complex solve + spectral norm; the -s factor of Delta
     carried via |s|), plus min_Gamma sigma_min(A_h) (the
     invertibility margin of the Rouche premise).  CENSUS:
     truth M_h < 1 on all steps?  Print the full M ladder,
     its max, and WHERE the sup is attained (region tag:
     RIGHT-CAP = Re s >= 1, the honest bottleneck near the
     nearly singular cap).  If M >= 1 only with the sup at
     the RIGHT-CAP, the contour choice is the issue:
     CONTOUR-LIMITED (typed per variant).  On the smooth
     world, variant A is UNDRAWABLE on a pair whose corridor
     is already broken (min s* <= 1 gives delta_1 <= 0: no
     rectangle of this family encloses [0, 1] without
     swallowing the real pole) -- typed POLE-IN-CORRIDOR,
     itself a detection.

 G3  THE ZERO-COUNT VERIFICATION (5 frozen steps = the middle
     five of the truth step list sorted by h, the
     factor_avoidance MEDIUM_N rule; both variants): count
     determinant zeros of A_h and A_{h+1} inside Gamma by the
     argument principle, N = (1/2 pi i) closed-int of
     d/ds log det A = -tr[A(s)^{-1} C] (the sflow variational
     identity continued to complex s; trace route), integrated
     by composite 16-point Gauss-Legendre with geometric panel
     grading toward the pole-nearest contour point.  WARDS
     (kill KW): (i) trace vs spectral integrand agreement at
     3 frozen contour nodes, rel <= 1e-9; (ii) |N - nearest
     integer| <= 1e-6; (iii) the integer equals the EXACT
     eigenvalue census #{i: 1/lam_i(C) inside Gamma}; (iv)
     the pair counts are EQUAL whenever M_h < 1 (the Rouche
     conclusion).  A pole within 1e-9 of the contour edge is
     typed BOUNDARY-POLE and exempted from (ii)-(iv) (honesty
     guard; census printed).  REPORT-ONLY extra: the same
     integral on the smooth world's first corridor-broken
     step (variant B) -- the count must show the zeros.

 G4  THE SMOOTH WORLD: same G2 ledgers per variant, plus per
     rung the exact zero census inside Gamma_B and the
     corridor-broken flag (min(s*_a, s*_b) <= 1).  CENSUSES:
     (i) where is M >= 1; (ii) where does the corridor
     actually contain zeros; (iii) the 2x2 of zero-count
     CHANGE across the step (census_a != census_b) vs M >= 1
     -- count change with M < 1 would CONTRADICT the theorem
     (ward-grade, printed; the contrapositive direction).
     DETECTION (frozen): a corridor-broken smooth step is
     DETECTED under variant A iff POLE-IN-CORRIDOR or M >= 1;
     under variant B iff M >= 1 or a nonzero census inside
     Gamma_B on either rung.  ROUCHE-DISCRIMINATES iff truth
     all-passes under at least one variant AND under that same
     variant every corridor-broken smooth step is detected AND
     every zero-count-change step has M >= 1.

 G5  TYPED (frozen): per variant ROUCHE-HOLDS(variant) iff
     truth M < 1 on ALL steps; CONTOUR-LIMITED(variant) iff
     violations exist but EVERY violating step attains its sup
     at the RIGHT-CAP (Re s >= 1); ROUCHE-FAILS(variant)
     otherwise.  Plus ROUCHE-DISCRIMINATES /
     ROUCHE-NONDISCRIMINATING per G4, and the honest analysis
     of which contour variant is source-legitimate (variant A
     is not; variant B in form only, see above).

 C   CONTROLS: the SMOOTH-MASS world is the PRIMARY embedded
     control -- it must have at least one corridor-broken step
     (kill KC -> CONTROL-DEAD); Epstein/scramble (kz 9) frame
     status REPORTED (frame death / exterior supercritical /
     window supercritical; report-only per this contract).

 W   PIPELINE + REPRODUCTION WARDS: W1 truth full-window rung
     census == 37 (sflow P0.1; kill KP -> PIPELINE-BROKEN);
     W2 truth consecutive full-window pairs == 31 and W3
     smooth pairs == 28 (factor_avoidance printed ledger; kill
     KW); W4 truth s*_h > 1 on every full-window rung (sflow
     S3/S4 CORRIDOR-CLEAR + pole table; kill KW).

KILLS: KP pipeline -> PIPELINE-BROKEN; KW wards (reproduction /
integrand / integer / census / pair-equality) -> WARD-BROKEN;
KC smooth control silent -> CONTROL-DEAD.

VERDICT (frozen enum): ROUCHE-MEASURED (+ typed sublabels per
variant ROUCHE-HOLDS(variant) / CONTOUR-LIMITED /
ROUCHE-FAILS, plus ROUCHE-DISCRIMINATES /
ROUCHE-NONDISCRIMINATING) / PIPELINE-BROKEN / WARD-BROKEN /
CONTROL-DEAD.

HONEST FRAME: M < 1 on a finite ladder is a MEASUREMENT of the
mechanism's existence, not a theorem -- the bound must be
DERIVED (and the variant-B margin law derived from the source
side) before anything is claimed; the zero-count identity and
the pole census are exact algebra whose wards protect the
bookkeeping only.  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- the
frozen 80-point grid, all bars, and every run-1 number stand
unchanged; v2 only ADDS reports and STRENGTHENS one typing
condition, it rescues nothing):

 (i)   GRID HONESTY AT THE CAP: the frozen right edge samples
       Im = b*v|v| with 32 EVEN-count points, so no grid point
       lies exactly on the real axis (nearest |Im s| = b/31^2
       ~ 3.1e-4).  With truth margins s* - 1 ~ 1e-7..1e-4 the
       printed M is therefore a LOWER bound of the continuum
       sup (run 1: min_Gamma sigma_min(A) ~ 3.1e-4 was set by
       the grid, not by the pole).  v2 adds the EXACT cap-point
       report M_cap = |s| ||A^{-1} Delta(s)|| at s = 1 +
       delta_1 + 0i (the sup lower bound at the nearest
       contour point to the pole) per step and variant.

 (ii)  CONTOUR-LIMITED STRENGTHENED: run 1 typed
       CONTOUR-LIMITED from the sup LOCATION only.  v2
       additionally requires the OFF-CAP sup (the max of the
       same ledger restricted to the frozen grid points with
       Re s < 1) to be < 1 on EVERY truth step of that
       variant; otherwise ROUCHE-FAILS.  This is a stricter
       bar, applied to the same run-1 grid values.

 (iii) OFF-CAP DIAGNOSTIC CENSUS (report-only, both worlds):
       M_off per step and variant.  HONEST LIMIT stated: an
       off-cap bound gives NO Rouche conclusion (the premise
       needs the whole contour); this census only locates
       where the mechanism is starved.

 (iv)  GAMMA_B CORRIDOR CENSUS ON ALL TRUTH RUNGS (exact
       algebra, report + ward-grade print): d1_fix = 8.07e-8
       sits BELOW the smallest measured truth margin (1.42e-7)
       by a factor of only ~1.8 -- v2 prints the exact zero
       census inside Gamma_B for every truth full-window rung
       (must be 0 throughout for the variant-B corridor to be
       meaningful) and the margin/d1_fix ratio.

Sources (read-only): v563_paper2_readouts (build_window /
atom_lags_at / arch_lags / frame_a_zones, verbatim);
factor_avoidance_euler_probe.py (ladder + 12-window pipeline +
smooth-mass world, VERBATIM; pair censuses = reproduction
anchor); port_sflow_toda_probe.py (pole identity s* =
1/lam_max, variational identity d/ds log det = -tr[A^{-1}C],
S4 h-trend law = the variant-B seed).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/euler_rouche_probe.py
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

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
NW = 12
MIN_COMMON_J = 8

# contour (frozen)
D0 = 0.1                    # delta_0, left margin
B_IM = 0.3                  # +/- imaginary half-height
N_RIGHT, N_TOP, N_BOT, N_LEFT = 32, 20, 20, 8   # 80 points
RIGHT_CAP_RE = 1.0          # sup-location region tag bar

# argument principle (frozen)
GL_N = 16                   # Gauss-Legendre nodes per panel
K_MAX = 45                  # geometric grading depth cap
G3_N = 5                    # medium-5 rule (factor_avoidance)
INT_WARD = 1e-6             # integer ward
SPEC_WARD = 1e-9            # trace-vs-spectral integrand ward
EDGE_GUARD = 1e-9           # BOUNDARY-POLE exemption distance

# reproduction anchors (predecessor printed ledgers)
REF_N_FULLWIN = 37          # sflow P0.1
REF_N_TRUTH_PAIRS = 31      # factor_avoidance A0.2
REF_N_SMOOTH_PAIRS = 28     # factor_avoidance A0.3

CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
AMENDMENTS = []
T0 = time.time()

GLX, GLW = np.polynomial.legendre.leggauss(GL_N)


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


# --------- pipeline, VERBATIM from factor_avoidance_euler_probe
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def build_rung(kz, scramble_seed=None, comb=None, rr_cache=None):
    rr = (rr_cache if rr_cache is not None
          else core.build_window(kz, scramble_seed=scramble_seed))
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h)


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


def rung_win(kz, scramble_seed=None, comb=None, rr_cache=None):
    """One rung -> 12x12 window compression (factor_avoidance
    rung_win VERBATIM)."""
    b = build_rung(kz, scramble_seed=scramble_seed, comb=comb,
                   rr_cache=rr_cache)
    h, L = b["h"], b["L"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, alpha=b["alpha"],
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["CJ"] = CJ
        out["jav"] = jav
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    return out


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    """B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n (verbatim)."""
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


# ------------------------------------- contour + Rouche machinery
def s_star_of(C):
    """Exact first positive determinant zero of I - sC (sflow
    identity (iii)): s* = 1/lam_max, inf if lam_max <= 0."""
    lam_mx = float(np.max(np.linalg.eigvalsh(C)))
    return ((1.0 / lam_mx) if lam_mx > 0.0 else float("inf")),\
        lam_mx


def gamma_points(d1):
    """Frozen 80-point discretization of the rectangle boundary,
    denser near s = 1 + d1 (G1)."""
    x_r = 1.0 + d1
    pts = []
    v = np.linspace(-1.0, 1.0, N_RIGHT)
    pts += [complex(x_r, B_IM * vv * abs(vv)) for vv in v]
    t = np.linspace(0.0, 1.0, N_TOP)
    xs = x_r - (x_r + D0) * (1.0 - t) ** 2
    pts += [complex(x, B_IM) for x in xs]
    pts += [complex(x, -B_IM) for x in xs]
    for yy in np.linspace(-B_IM, B_IM, N_LEFT):
        pts.append(complex(-D0, yy))
    return np.asarray(pts, complex)


def region_tag(s):
    if s.real >= RIGHT_CAP_RE:
        return "RIGHT-CAP"
    if abs(s.real + D0) <= 1e-12:
        return "LEFT-EDGE"
    return "TOP/BOT"


def sup_ledger(Ca, Dmat, pts):
    """M = sup_Gamma ||A^{-1} Delta(s)||_2 with Delta(s) = -s D;
    plus the invertibility margin min_Gamma sigma_min(A) and the
    OFF-CAP sup restricted to Re s < 1 (SPEC v2 (ii)/(iii))."""
    Iw = np.eye(NW)
    M, s_at = -1.0, None
    Moff, s_off = -1.0, None
    smin, s_sm = float("inf"), None
    for s in pts:
        A = Iw - s * Ca
        sv = np.linalg.svd(A, compute_uv=False)
        if sv[-1] < smin:
            smin, s_sm = float(sv[-1]), s
        m = abs(s) * float(np.linalg.norm(
            np.linalg.solve(A, Dmat), 2))
        if m > M:
            M, s_at = m, s
        if s.real < RIGHT_CAP_RE and m > Moff:
            Moff, s_off = m, s
    return M, s_at, smin, s_sm, Moff, s_off


def cap_point(Ca, Dmat, d1):
    """EXACT cap-point value at s = 1 + d1 + 0i (SPEC v2 (i)):
    the nearest contour point to the real pole; a lower bound
    of the continuum sup."""
    s = 1.0 + d1
    A = np.eye(NW) - s * Ca
    sv = np.linalg.svd(A, compute_uv=False)
    return (s * float(np.linalg.norm(np.linalg.solve(A, Dmat),
                                     2)), float(sv[-1]))


def real_poles(C):
    ev = np.linalg.eigvalsh(C)
    return [1.0 / float(v) for v in ev if abs(v) > 1e-14]


def census_inside(C, d1):
    """EXACT zero census of det(I - sC) inside Gamma(d1) plus the
    minimal pole distance to the vertical edges."""
    x_r = 1.0 + d1
    n = 0
    dmin = float("inf")
    for p in real_poles(C):
        dmin = min(dmin, abs(p - x_r), abs(p + D0))
        if -D0 < p < x_r:
            n += 1
    return n, dmin


def _ell_trace(zs, C):
    """d/ds log det(I - sC) = -tr[(I - sC)^{-1} C] (sflow
    variational identity, complex s; trace route)."""
    Iw = np.eye(NW)
    out = np.empty(len(zs), complex)
    for i, z in enumerate(zs):
        out[i] = -np.trace(np.linalg.solve(Iw - z * C, C))
    return out


def _ell_spectral(zs, C):
    ev = np.linalg.eigvalsh(C)[:, None]
    return np.sum(-ev / (1.0 - zs[None, :] * ev), axis=0)


def _seg_dist(p, z0, z1):
    dz = z1 - z0
    t = ((p - z0) * dz.conjugate()).real / abs(dz) ** 2
    t = min(1.0, max(0.0, t))
    return abs(p - (z0 + t * dz))


def _graded_panels(z0, z1, poles, toward):
    """Geometric panel grading toward the pole-nearest end of the
    segment ('end'/'start'); uniform 4 panels if toward is None."""
    L = abs(z1 - z0)
    if toward is None:
        us = np.linspace(0.0, 1.0, 5)
    else:
        d = max(min((_seg_dist(p, z0, z1) for p in poles),
                    default=L), 1e-9)
        K = int(min(K_MAX, max(4, math.ceil(
            math.log2(max(L / d, 2.0))))))
        us = np.concatenate(
            ([0.0], 1.0 - 2.0 ** -np.arange(1, K + 1), [1.0]))
        if toward == "start":
            us = 1.0 - us[::-1]
    return [(z0 + (z1 - z0) * a, z0 + (z1 - z0) * b)
            for a, b in zip(us[:-1], us[1:])]


def count_zeros_numeric(C, d1):
    """Argument-principle zero count of det(I - sC) inside
    Gamma(d1): composite Gauss-Legendre on the graded rectangle
    boundary, counterclockwise."""
    x_r = 1.0 + d1
    poles = real_poles(C)
    bl = complex(-D0, -B_IM)
    br = complex(x_r, -B_IM)
    tr = complex(x_r, B_IM)
    tl = complex(-D0, B_IM)
    rc = complex(x_r, 0.0)
    sides = ((bl, br, "end"),      # bottom, pole-nearest right
             (br, rc, "end"),      # right lower half -> center
             (rc, tr, "start"),    # right upper half <- center
             (tr, tl, "start"),    # top, pole-nearest right
             (tl, bl, None))       # left, far from all poles
    tot = 0.0 + 0.0j
    for z0, z1, toward in sides:
        for a, b in _graded_panels(z0, z1, poles, toward):
            mid = 0.5 * (a + b)
            half = 0.5 * (b - a)
            tot += half * np.sum(GLW * _ell_trace(
                mid + half * GLX, C))
    return tot / (2.0j * math.pi)


def fmt_s(s):
    return "%.4f%+.4fi" % (s.real, s.imag)


def main():
    section("PRIME.PORT.EULER.ROUCHE.01 -- matrix-Rouche corridor "
            "inheritance: sup_Gamma ||A_h^{-1} Delta_h|| < 1 "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ P0
    section("P0 -- build the truth + smooth-mass ladders (all "
            "frame-A zones, h <= %d; pipeline VERBATIM)"
            % H_DEEP_MAX)
    rungs, srungs = [], []
    n_smooth_dead = 0
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        r = rung_win(kz, rr_cache=rr)
        if not isinstance(r, dict):
            continue
        rungs.append(r)
        uu = np.asarray(rr["uu"], float)
        rs = rung_win(kz, comb=(uu, smooth_masses(uu)),
                      rr_cache=rr)
        if isinstance(rs, dict):
            srungs.append(rs)
        else:
            n_smooth_dead += 1
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    srungs.sort(key=lambda r: (r["h"], r["kz"]))
    full_t = [r for r in rungs if r.get("full")]
    print("    truth: %d rungs (%d full-window), h %d .. %d | "
          "smooth: %d rungs, %d chain/window deaths"
          % (len(rungs), len(full_t), rungs[0]["h"],
             rungs[-1]["h"], len(srungs), n_smooth_dead))
    check("W1 truth full-window rung census %d == %d (sflow "
          "P0.1 anchor)" % (len(full_t), REF_N_FULLWIN),
          len(full_t) == REF_N_FULLWIN, kill="KP")

    def make_pairs(rr_list):
        rows = []
        for ra, rb in zip(rr_list[:-1], rr_list[1:]):
            if not (ra.get("full") and rb.get("full")):
                continue
            Ca, Cb = ra["CJ"], rb["CJ"]
            ssa, _ = s_star_of(Ca)
            ssb, _ = s_star_of(Cb)
            rows.append(dict(ha=ra["h"], hb=rb["h"],
                             kza=ra["kz"], kzb=rb["kz"],
                             Ca=Ca, Cb=Cb, D=Cb - Ca,
                             ssa=ssa, ssb=ssb))
        return rows

    tpairs = make_pairs(rungs)
    spairs = make_pairs(srungs)
    check("W2 truth consecutive full-window pairs %d == %d "
          "(factor_avoidance anchor)"
          % (len(tpairs), REF_N_TRUTH_PAIRS),
          len(tpairs) == REF_N_TRUTH_PAIRS, kill="KW")
    check("W3 smooth pairs %d == %d (factor_avoidance anchor)"
          % (len(spairs), REF_N_SMOOTH_PAIRS),
          len(spairs) == REF_N_SMOOTH_PAIRS, kill="KW")
    if KILLS:
        return finish("n/a")

    # ------------------------------------------------------------ G1
    section("G1 -- THE CONTOUR: rectangle Re s in [-%.1f, 1 + "
            "delta_1], Im s in [-%.1f, +%.1f]; variant A "
            "(target-informed) vs variant B (fixed, tau-law/2)"
            % (D0, B_IM, B_IM))
    hs, margins = [], []
    n_out = 0
    for r in full_t:
        ss, _ = s_star_of(r["CJ"])
        if ss > 1.0:
            n_out += 1
            if math.isfinite(ss):
                hs.append(float(r["h"]))
                margins.append(ss - 1.0)
    check("W4 truth pole outside the corridor (s* > 1) on "
          "%d/%d full-window rungs (sflow S3/S4 anchor)"
          % (n_out, len(full_t)), n_out == len(full_t),
          kill="KW")
    if KILLS:
        return finish("n/a")
    c1, c0 = np.polyfit(np.log(hs), np.log(margins), 1)
    h_max = max(hs)
    d1_fix = 0.5 * math.exp(c0) * h_max ** c1
    mq = np.percentile(margins, [0, 25, 50, 75, 100])
    print("    truth margins s* - 1: min %.4e  q25 %.4e  med "
          "%.4e  q75 %.4e  max %.4e" % tuple(mq))
    print("    h-trend law (sflow S4 seed): log(s* - 1) = "
          "%+.4f %+.4f log h  -> predicted margin at h_max = "
          "%d: %.4e" % (c0, c1, int(h_max),
                        math.exp(c0) * h_max ** c1))
    print("    variant B FIXED delta_1^fix = tau-law/2 = %.6e "
          "(one contour for the whole ladder)" % d1_fix)
    print("    variant A per pair: delta_1 = min(s*_h, "
          "s*_{h+1} - 1)/2 -- TARGET-INFORMED (honest note: "
          "fine for the")
    print("    measurement, NOT source-legitimate for a "
          "theorem; variant B is source-legitimate in FORM "
          "only, its law is")
    print("    fitted across the ladder -- the margin law "
          "itself must be derived for a self-contained "
          "statement).")
    gammaB = gamma_points(d1_fix)
    # SPEC v2 (iv): Gamma_B corridor census on ALL truth rungs
    nz_B = 0
    for r in full_t:
        nz_B += census_inside(r["CJ"], d1_fix)[0]
    ratio = min(margins) / d1_fix
    print("    v2 (iv) Gamma_B truth census: %d determinant "
          "zeros inside Gamma_B over all %d truth rungs "
          "(min margin / delta_1^fix = %.2f)"
          % (nz_B, len(full_t), ratio))
    check("G1.v2 Gamma_B encloses a zero-free truth corridor "
          "(0 zeros on all %d rungs)" % len(full_t), nz_B == 0)
    AMENDMENTS.append("v2(i) exact cap-point report added "
                      "(even-count right edge has no real-axis "
                      "sample; grid M is a lower bound)")
    AMENDMENTS.append("v2(ii) CONTOUR-LIMITED strengthened: "
                      "off-cap sup < 1 required on all steps")
    AMENDMENTS.append("v2(iii) off-cap diagnostic census, both "
                      "worlds (report-only, no Rouche "
                      "conclusion)")
    AMENDMENTS.append("v2(iv) Gamma_B truth corridor census on "
                      "all rungs")

    # ------------------------------------------------------------ G2
    section("G2 -- THE SUP LEDGER, truth (%d steps): M = "
            "sup_Gamma |s| ||(I - s C_h)^{-1} (C_{h+1} - "
            "C_h)||_2, both variants" % len(tpairs))

    TAG_SHORT = {"RIGHT-CAP": "RC", "TOP/BOT": "TB",
                 "LEFT-EDGE": "LE"}

    def measure(row):
        d1A = 0.5 * (min(row["ssa"], row["ssb"]) - 1.0)
        if d1A > 0.0 and math.isfinite(d1A):
            MA, sA, smA, _, MoA, _ = sup_ledger(
                row["Ca"], row["D"], gamma_points(d1A))
            McA, _ = cap_point(row["Ca"], row["D"], d1A)
        else:
            MA, sA, smA, MoA, McA = (None,) * 5  # POLE-IN-CORRIDOR
        MB, sB, smB, _, MoB, _ = sup_ledger(row["Ca"], row["D"],
                                            gammaB)
        McB, _ = cap_point(row["Ca"], row["D"], d1_fix)
        row.update(d1A=d1A, MA=MA, sA=sA, smA=smA, MoA=MoA,
                   McA=McA, MB=MB, sB=sB, smB=smB, MoB=MoB,
                   McB=McB)

    print("    (M = grid sup, LOWER bound of the continuum sup; "
          "Moff = sup over Re s < 1; Mcap = exact value at s = "
          "1 + delta_1, v2)")
    print("    step        delta1(A)  M_A       Moff_A   "
          "Mcap_A     M_B       Moff_B   Mcap_B     sup A/B")
    for row in tpairs:
        measure(row)
        print("    h %3d->%3d  %.4e %9.4f  %7.4f  %.3e  "
              "%9.4f  %7.4f  %.3e  %s/%s"
              % (row["ha"], row["hb"], row["d1A"], row["MA"],
                 row["MoA"], row["McA"], row["MB"], row["MoB"],
                 row["McB"], TAG_SHORT[region_tag(row["sA"])],
                 TAG_SHORT[region_tag(row["sB"])]))
    violA = [r for r in tpairs if r["MA"] >= 1.0]
    violB = [r for r in tpairs if r["MB"] >= 1.0]
    MAmax = max(r["MA"] for r in tpairs)
    MBmax = max(r["MB"] for r in tpairs)
    MoAmax = max(r["MoA"] for r in tpairs)
    MoBmax = max(r["MoB"] for r in tpairs)
    smin_grid = min(r["smA"] for r in tpairs)
    print("\n    TRUTH CENSUS: variant A M < 1 on %d/%d (max M "
          "%.4f) | variant B M < 1 on %d/%d (max M %.4f)"
          % (len(tpairs) - len(violA), len(tpairs), MAmax,
             len(tpairs) - len(violB), len(tpairs), MBmax))
    print("    OFF-CAP (v2): max Moff_A = %.4f, max Moff_B = "
          "%.4f over all truth steps (< 1 on %d/%d and %d/%d)"
          % (MoAmax, MoBmax,
             sum(1 for r in tpairs if r["MoA"] < 1.0),
             len(tpairs),
             sum(1 for r in tpairs if r["MoB"] < 1.0),
             len(tpairs)))
    print("    CAP HONESTY (v2): grid min sigma_min(A) = %.2e "
          "is set by the nearest-to-axis grid point (|Im s| = "
          "b/31^2 = %.1e)," % (smin_grid, B_IM / 31.0 ** 2))
    print("    not by the pole; the exact cap values Mcap "
          "(range %.2e .. %.2e for A) show the continuum sup "
          "-- the M ledger is a lower bound."
          % (min(r["McA"] for r in tpairs),
             max(r["McA"] for r in tpairs)))
    for nm, viol in (("A", violA), ("B", violB)):
        if viol:
            tags = [region_tag(r["sA" if nm == "A" else "sB"])
                    for r in viol]
            print("    variant %s violations (%d): first/worst "
                  "%s; sup regions %s"
                  % (nm, len(viol),
                     ["h%d->%d M=%.3f" % (r["ha"], r["hb"],
                      r["MA" if nm == "A" else "MB"])
                      for r in (viol[0], max(
                          viol, key=lambda r:
                          r["MA" if nm == "A" else "MB"]))],
                     sorted(set(tags))))

    def variant_type(viol, skey, mkey):
        """SPEC v2 (ii): CONTOUR-LIMITED needs sup location at
        the RIGHT-CAP on every violation AND off-cap sup < 1
        on EVERY step."""
        if not viol:
            return "ROUCHE-HOLDS"
        if (all(region_tag(r[skey]) == "RIGHT-CAP"
                for r in viol)
                and all(r[mkey] < 1.0 for r in tpairs)):
            return "CONTOUR-LIMITED"
        return "ROUCHE-FAILS"

    typA = variant_type(violA, "sA", "MoA")
    typB = variant_type(violB, "sB", "MoB")
    check("G2.s truth typed (v2 bars): variant A %s, variant "
          "B %s" % (typA, typB), True)

    # ------------------------------------------------------------ G3
    section("G3 -- ZERO-COUNT VERIFICATION (argument principle, "
            "%d frozen medium steps, both variants): N = "
            "(1/2pi i) closed-int -tr[A^{-1}C] ds" % G3_N)
    i0 = (len(tpairs) - G3_N) // 2
    g3 = tpairs[i0:i0 + G3_N]
    print("    frozen steps (medium-5 rule): %s"
          % ["h%d->%d" % (r["ha"], r["hb"]) for r in g3])
    w_spec = 0.0
    w_int = 0.0
    ok_census = True
    ok_equal = True
    n_bpole = 0
    print("\n    step        var  rung  N_num (re, |im|)      "
          "int-err   N_exact  pair-equal (M<1)")
    for row in g3:
        for vn, d1, M in (("A", row["d1A"], row["MA"]),
                          ("B", d1_fix, row["MB"])):
            nints = []
            for side_nm, C in (("h  ", row["Ca"]),
                               ("h+1", row["Cb"])):
                Nnum = count_zeros_numeric(C, d1)
                nint = int(round(Nnum.real))
                err = abs(Nnum - nint)
                nex, dmin = census_inside(C, d1)
                if dmin < EDGE_GUARD:
                    n_bpole += 1
                    print("    h %3d->%3d  %s   %s   "
                          "BOUNDARY-POLE (pole within %.0e of "
                          "the edge; census %d) -- ward exempt"
                          % (row["ha"], row["hb"], vn, side_nm,
                             EDGE_GUARD, nex))
                    continue
                w_int = max(w_int, err)
                ok_census &= (nint == nex)
                nints.append(nint)
                print("    h %3d->%3d  %s   %s   %+9.6f  %.1e   "
                      "%.1e   %d        %s"
                      % (row["ha"], row["hb"], vn, side_nm,
                         Nnum.real, abs(Nnum.imag), err, nex,
                         "-"))
            if len(nints) == 2 and M < 1.0:
                eq = (nints[0] == nints[1])
                ok_equal &= eq
                print("      -> pair counts %d == %d under M = "
                      "%.4f < 1: %s" % (nints[0], nints[1], M,
                                        eq))
            # integrand ward at 3 frozen nodes (rung h)
            zs = gamma_points(d1)[[0, 40, 79]]
            lt = _ell_trace(zs, row["Ca"])
            lsp = _ell_spectral(zs, row["Ca"])
            w_spec = max(w_spec, float(np.max(
                np.abs(lt - lsp)
                / np.maximum(np.abs(lt), 1e-30))))
    check("G3.W1 integrand trace vs spectral, worst rel %.1e "
          "<= %.0e" % (w_spec, SPEC_WARD), w_spec <= SPEC_WARD,
          kill="KW")
    check("G3.W2 argument-principle count integer at %.0e "
          "(worst dev %.1e; %d BOUNDARY-POLE exemptions)"
          % (INT_WARD, w_int, n_bpole), w_int <= INT_WARD,
          kill="KW")
    check("G3.W3 numeric count == exact eigenvalue census on "
          "every warded rung/variant", ok_census, kill="KW")
    check("G3.W4 Rouche conclusion verified: pair counts EQUAL "
          "whenever M < 1", ok_equal, kill="KW")

    # ------------------------------------------------------------ G4
    section("G4 -- THE SMOOTH WORLD (%d steps): same ledgers; "
            "corridor-broken census; does the mechanism DETECT "
            "the failures?" % len(spairs))
    print("    step        s*_a     s*_b     broken  variant A"
          "            M_B       sup at (B)            zeros "
          "in Gamma_B (a,b)")
    n_broken = 0
    n_MB_ge1 = 0
    det_A_all = True
    det_B_all = True
    n_change = 0
    n_change_Mlt1 = 0
    first_broken = None
    for row in spairs:
        measure(row)
        za, _ = census_inside(row["Ca"], d1_fix)
        zb, _ = census_inside(row["Cb"], d1_fix)
        row.update(za=za, zb=zb)
        broken = min(row["ssa"], row["ssb"]) <= 1.0
        row["broken"] = broken
        if broken:
            n_broken += 1
            if first_broken is None:
                first_broken = row
        if row["MB"] >= 1.0:
            n_MB_ge1 += 1
        if za != zb:
            n_change += 1
            if row["MB"] < 1.0:
                n_change_Mlt1 += 1
        pic = row["MA"] is None
        a_str = ("POLE-IN-CORRIDOR    " if pic
                 else "M_A %8.4f %-7s"
                 % (row["MA"], region_tag(row["sA"])))
        if broken:
            det_A = pic or (row["MA"] is not None
                            and row["MA"] >= 1.0)
            det_B = (row["MB"] >= 1.0) or (za + zb > 0)
            det_A_all &= det_A
            det_B_all &= det_B
        print("    h %3d->%3d  %7.4f  %7.4f  %-5s   %s %9.4f  "
              "%s %-9s %d,%d"
              % (row["ha"], row["hb"],
                 min(row["ssa"], 99.0), min(row["ssb"], 99.0),
                 str(broken), a_str, row["MB"],
                 fmt_s(row["sB"]), region_tag(row["sB"]),
                 za, zb))
    n_picA = sum(1 for r in spairs if r["MA"] is None)
    print("\n    SMOOTH CENSUS: corridor-broken on %d/%d steps; "
          "variant A undrawable (POLE-IN-CORRIDOR) on %d; "
          "M_B >= 1 on %d" % (n_broken, len(spairs), n_picA,
                              n_MB_ge1))
    n_off_s = sum(1 for r in spairs if r["MoB"] >= 1.0)
    print("    OFF-CAP DIAGNOSTIC (v2, report-only -- no "
          "Rouche conclusion off a full contour): smooth "
          "Moff_B >= 1 on %d/%d steps (max %.3f); truth had "
          "max Moff = %.4f/%.4f (A/B)"
          % (n_off_s, len(spairs),
             max(r["MoB"] for r in spairs), MoAmax, MoBmax))
    print("    zero-count CHANGE across the step on %d steps; "
          "change with M_B < 1 (would contradict the theorem): "
          "%d" % (n_change, n_change_Mlt1))
    check("G4.W theorem contrapositive on smooth: every "
          "zero-count change has M_B >= 1 (%d/%d)"
          % (n_change - n_change_Mlt1, n_change),
          n_change_Mlt1 == 0, kill="KW")
    if first_broken is not None:
        row = first_broken
        print("\n    REPORT-ONLY: argument-principle integral "
              "on the smooth FIRST broken step h %d->%d "
              "(variant B):" % (row["ha"], row["hb"]))
        for side_nm, C, zx in (("h  ", row["Ca"], row["za"]),
                               ("h+1", row["Cb"], row["zb"])):
            Nn = count_zeros_numeric(C, d1_fix)
            print("      rung %s: N_num = %+9.6f%+9.2ei "
                  "(exact census %d)"
                  % (side_nm, Nn.real, Nn.imag, zx))
    truth_pass = {"A": not violA, "B": not violB}
    disc = None
    for vn in ("A", "B"):
        if not truth_pass[vn]:
            continue
        if vn == "A" and det_A_all and n_broken > 0:
            disc = "A"
            break
        if vn == "B" and det_B_all and n_broken > 0 \
                and n_change_Mlt1 == 0:
            disc = "B"
            break
    sub_disc = ("ROUCHE-DISCRIMINATES(variant %s)" % disc
                if disc else "ROUCHE-NONDISCRIMINATING")
    check("G4.s discrimination typed: %s (truth all-pass A=%s "
          "B=%s; smooth broken steps detected A=%s B=%s)"
          % (sub_disc, truth_pass["A"], truth_pass["B"],
             det_A_all, det_B_all), True)

    # ------------------------------------------------------------ G5
    section("G5 -- TYPED OUTCOME + the contour-legitimacy "
            "analysis")
    print("    variant A (target-informed): %s | variant B "
          "(fixed, tau-law/2): %s | %s"
          % (typA, typB, sub_disc))
    print("""
    HONEST ANALYSIS (frozen frame): variant A consults the
    TARGET rung's pole to place the right edge -- it can only
    ever certify what the target already reveals; it measures
    whether the Rouche MECHANISM exists, nothing more.
    Variant B is a single fixed contour (no per-target pole is
    consulted), so the Rouche step is source-legitimate GIVEN
    the contour -- but its delta_1^fix is calibrated by the
    ladder-wide h-trend law, which itself is fitted on target
    data.  A self-contained inheritance theorem therefore
    needs (i) the margin law derived (not fitted), and (ii)
    the sup bound M < 1 derived from the increment structure.
    Both remain open; this probe only measures whether the
    bound is TRUE on the deployed ladder.""")

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C2 -- smooth-mass world (PRIMARY): corridor-broken "
          "on %d/%d steps." % (n_broken, len(spairs)))
    check("C2 smooth control fires (>= 1 corridor-broken step)",
          n_broken > 0, kill="KC")
    print("  C1 -- Epstein/scramble frame status (kz %d, "
          "report-only per contract):" % CTRL_KZ)
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = rung_win(CTRL_KZ, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
        elif "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES"
                  % nmc)
        else:
            ssc, lamc = s_star_of(rc["CJ"])
            print("    %-8s: lam(out) %.3e | lam(C_J) %.3e | "
                  "pole s* = %.4f -> %s"
                  % (nmc, rc["lamO"], rc["lamC"], ssc,
                     "EXTERIOR supercritical"
                     if rc["lamO"] > 1.0 else
                     "WINDOW supercritical / pole inside"
                     if rc["lamC"] > 1.0 or ssc <= 1.0
                     else "silent (reported)"))

    typed = ("A: %s, B: %s, %s" % (typA, typB, sub_disc))
    return finish(typed)


def finish(typed):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN", "KW": "WARD-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = "ROUCHE-MEASURED"
        print("\n  VERDICT: %s (%s)" % (VERDICT, typed))
    print("\n  SPEC v2 amendments (fail-first preserved): %s"
          % ("; ".join(AMENDMENTS) if AMENDMENTS else "none"))
    print("""
  HONEST FRAME (as frozen): the Rouche step, the zero-count
  identity and the pole census are exact algebra -- the wards
  protect the bookkeeping.  The measured content is (a)
  whether ONE contour sup bound M < 1 holds on every truth
  step (then no Euler extension step can pull a pole into the
  corridor, per step, on this finite ladder), (b) whether the
  same mechanism fails on the smooth world exactly where its
  corridor breaks, and (c) the honest fact that neither
  contour variant is yet source-derived.  NO RH claim.  No
  marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
