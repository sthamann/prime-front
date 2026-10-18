#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_scaled_jost_reference_probe -- PRIME.PORT.JOSTREF.01
(EXPLORATION ONLY, experiments/; round 43: pin the correct solvable
REFERENCE KERNEL of the port -- pure negative-order Jacobi/Bessel
J_alpha vs Jost-modified J_{1/2} (Geronimo-Case class), 2026-08-09).

CONTEXT (machinery verbatim from freetail_case_bridge_probe /
christoffel_hypotheses_probe): the free-tail completion J_h^ft of
the deployed tilde-measure family has the Geronimo-Case density
form w_h(x) ~ sqrt(1-x^2)/|u_{0,h}(e^{i theta})|^2 (x = cos theta),
u_0 the Jost function of the free-tail Jacobi chain (the exact
identity Im m(E+i0) = sin(theta)/|u_0(e^{i theta})|^2 is WARDED
below).  Measured (round 42): |J_h(1)| = |u_{0,h}(2)| in
[2.2, 18.8], bounded away from 0 -> the TRUE fixed-h edge exponent
is +1/2; the fitted alpha ~ -0.364 is a MESOSCOPIC exponent over
h^-2 << 1-x << 1e-2 caused by the Jost modulation; some rungs carry
scaled near-edge bound states (kz 12/13: h^2 eps/2 = 21.0 / 110.6).
The alias positions a_m = 2 h^2 (1 - y_m) match pi^2 m^2 to
0.15-0.31 % (cosine-lattice kinematics) and are NEVER used to fit
alpha (kernel entries only).

FROZEN PROTOCOL (2026-08-09; all reachable rungs h <= 900 (42
expected), skipped honestly where the machinery does not permit;
heavy rungs kz {9, 12, 13, 26, 40} MANDATORY; controls kz 9):

 J1  SCALED JOST FUNCTION: u_{0,h}(z) of the free-tail chain in the
     TRUE Jost normalization (u_n = z^n for n > h; downward
     back-substitution with per-step renormalization; complex on
     the band, z = e^{i theta}, E = z + 1/z = 2 cos theta).
     U_h(k) = u_{0,h}(2 cos(k/h)) / u_{0,h}(2) on the frozen grid
     k in [0, h^{3/4}], 200 points.  |U_h| profiles printed for
     the heavy rungs.  WARDS: W1 U_h(0) = 1 (same-point ratio;
     |U - 1| <= 1e-15, the complex-division ulp -- v2; all rungs);
     W2 Geronimo-Case identity |f(E) pi |u_0|^2 / sin(theta) - 1|
     <= 1e-6 on 64 interior thetas in [0.2, pi - 0.2] (all rungs;
     f = |Im m|/pi by coefficient stripping -- an exact algebraic
     identity for finite-rank perturbations); W3 complex-path
     u_0(2) equals the real endpoint recursion (heavy rungs,
     rel <= 1e-9).

 J2  BOUND-STATE CENSUS: zeros of u_0 outside the band = point
     spectrum of J_h^ft (shooting + bisection, verbatim); for
     E_r > 2 report BOTH scaled conventions, kappa_r =
     h acosh(E_r/2) and A_r = h^2 (E_r - 2)/2; the CENSUS
     convention is FROZEN to A_r = h^2 eps/2 (the memo's).
     WARD W4: the NEAREST above-edge state reproduces the memo,
     kz 12 -> 21.0 and kz 13 -> 110.6, rel tol 10 %.

 J3  KERNEL SHOOTOUT (the deliverable): per rung the alias window
     m = 1..M, M = min(32, #neg nodes with sqrt(a_m) <= h^{3/4});
     rungs with M < 6 skipped (reported).  DATA: the exact CD
     kernel matrix K[m, m'] = sum_j p_j(y_m) p_j(y_m') (h terms,
     pos-measure chain), compared in SHAPE: the correlation-
     normalized C = K / sqrt(diag x diag) (cancels every scalar
     normalization incl. h^{2 alpha + 2}).       Three references, all
     evaluated at the MEASURED a_m through the same edge scaling
     x_m = 1 - a_m / (2 n_mod^2), n_mod = clip(ceil(6 sqrt(a_max)),
     64, 1200) (v2), n_mod polynomial terms:
      (a) pure Jacobi/Bessel: exact Jacobi(alpha, 1/2) chain
          (closed-form recurrence), ONE common alpha fitted over
          all rungs on the frozen grid alpha in [-0.90, 1.50] step
          0.02 (objective: mean over rungs of the per-rung
          residual; kernel entries only, never a_m);
      (b) J_{1/2} DRESSED by the measured Jost function: CD kernel
          of the model measure sin(theta)^2 dtheta / |U_h(k)|^2,
          k(x) = 2 n_mod sin(theta/2) = sqrt(2 n_mod^2 (1 - x)),
          |U_h| evaluated EXACTLY at the model k (capped at
          k_W = h^{3/4}, constant continuation beyond -- the
          measured window); discretized on N = max(6000,
          16 n_mod) midpoint thetas, chain by Lanczos;
      (c) finite-Darboux J_{1/2} from the measured bound states
          ONLY: minimal rational dressing |U_c(k)|^2 =
          prod_r (k^2 + kappa_r^2) / kappa_r^2 (zeros of u_0 at
          z_r = e^{-kappa_r/h} transplanted; E < -2 states ignored
          -- far edge), i.e. model weight sin^2 x
          prod_r kappa_r^2/(k^2 + kappa_r^2); same pipeline as (b).
     METRIC (frozen): operator-norm relative residual
     ||C_data - C_ref||_2 / ||C_data||_2 per rung.
     LEAVE-ONE-RUNG-OUT: (a) alpha refit on the remaining rungs
     (grid argmin), residual of the held-out rung at that alpha;
     (b)/(c) are PARAMETER-FREE per rung, so LORO = plain
     (documented, not hidden).  Per reference: median LORO
     residual + h-trend (participating rungs sorted by h; shallow
     = median of the lowest-h third, deep = median of the
     highest-h third).
     WARDS: W5 model-pipeline calibration -- with U == 1 the model
     kernel (n by the deployed rule, aliases pi^2 m^2, m = 1..24)
     reproduces the CLOSED-FORM Bessel-1/2 correlation kernel
     (J_{1/2}(x) = sqrt(2/(pi x)) sin x) to relres <= 0.05;
     W6 model discretization -- the Lanczos chain of the
     undressed semicircle matches the exact Chebyshev-U
     coefficients (al = 0, be = 1/2) to 1e-6.

 J4  TYPED DECISION (frozen bars, all honest):
     JOSTREF-J12-DRESSED iff min(med_b, med_c) <= 0.95 med_a AND
     the winning dressed reference's deep-third median <= its
     shallow-third median (residual decreases with h);
     JOSTREF-PURE-ALPHA iff med_a <= 0.95 min(med_b, med_c) AND
     the LORO alpha spread (max - min) <= 0.10 (stable alpha);
     JOSTREF-UNDECIDED otherwise.  Medians are LORO medians.
     MEMO CROSS-TEST: med res_a at the frozen mesoscopic alpha
     -0.364 and at the true edge +0.5 reported; "the density
     alpha FAILS on the kernel" stated iff med(res_a(-0.364)) >
     1.2 x med(res_a(alpha*)) -- a pure-alpha fit that succeeds
     on the density but fails on the KERNEL is rejected.

 C   CONTROLS (kz 9): ch1 SCRAMBLE (seed 1) -- the kernel match
     breaks on the values: min residual over the three references
     >= 1.5 x the real-rung minimum; ch2 ALIAS PERMUTATION
     (seed 1, on reference (b)): residual of the row/col-permuted
     reference >= 1.5 x the aligned residual.  FIRE = ch1 OR ch2
     (which fires is stated).  The Jost ALGEBRA (GC identity W2)
     PERSISTS for the scramble (measure-blind algebra -- stated,
     not a kill).

FROZEN CONCRETIZATIONS (pre-registered with the protocol, before
the first run):
  (i)   census convention: A_r = h^2 (E_r - 2)/2 (memo); kappa_r =
        h acosh(E_r/2) printed alongside (A_r ~ kappa_r^2/2 near
        the edge).
  (ii)  reference (a) uses the closed-form Jacobi(alpha, 1/2)
        chain (beta = +1/2 at the far edge, matching the model
        base weight); (b)/(c) use the discretized dressed
        semicircle -- W5/W6 bound the pipeline mismatch.
  (iii) the shape metric is correlation-normalized, so no scalar
        normalization (m0, c_h, h-powers) enters anywhere.
  (iv)  (b)/(c) carry NO fitted parameters (U_h and kappa_r are
        measured per rung); their LORO equals the plain residual.
  (v)   trend statistic: participating rungs sorted by h, thirds,
        shallow/deep medians; "decreases" = deep <= shallow.
  (vi)  aliases with a_m < 1e-6 dropped (edge-node degeneracy
        guard); heavy rungs must participate in J3 (M >= 6) or
        the probe is PIPELINE-BROKEN.

KILLS: pipeline breaks (chain short, model Lanczos short, fits
non-finite, heavy rung unreachable) -> PIPELINE-BROKEN; any ward
W1..W6 fails -> WARD-BROKEN; controls silent -> CONTROL-DEAD.
The J4 decision types are MEASUREMENTS, never kills.

VERDICT (frozen enum): JOSTREF-MEASURED (+ typed decision
JOSTREF-J12-DRESSED / JOSTREF-PURE-ALPHA / JOSTREF-UNDECIDED) /
PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  W4 checks the NEAREST
  above-edge state against the memo values (the round-42
  christoffel probe reported the nearest state found by the same
  shooting machinery); W2 at 1e-6 on every rung.
  v2 (2026-08-09, after the v1 run; no J3/J4 decision bar moved):
  (i) W5 FAILED honestly at relres 0.0759 (bar 0.05) with
  NMOD_FACTOR = 3: the model-to-Bessel convergence is measured
  O(n^-2) (n = 227/320/454 -> 0.0759/0.0372/0.0183; the
  hard-edge n-shift n+1 moves it by < 5 % relative -- not the
  cause), so the deployed rule is raised to n_mod =
  clip(ceil(6 sqrt(a_max)), 64, 1200), putting the pipeline
  systematic at ~2 % under the UNTOUCHED 0.05 bar.  (ii) W1
  "exactly" re-anchored to |U_h(0) - 1| <= 1e-15: four rungs
  (kz 15/27/30/33) returned 1 - 1.1e-16 -- the 1-ulp rounding of
  numpy's complex Smith division; the construction (same-point
  ratio) is unchanged.  v1 J3 numbers carried the 7.6 % pipeline
  systematic and are superseded by the v2 rerun.

NO RH claim: this pins the solvable reference model of the port
(comparison operator for a future Szego/Case argument); nothing
here proves or refutes a zero statement.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan); v563 READ-ONLY;
RNG only in the controls (scramble seed 1, permutation seed 1);
stdout only.

Sources (read-only): v563_paper2_readouts; freetail_case_bridge_
probe (chain, m-function, shooting -- verbatim);
christoffel_hypotheses_probe (Jacobi closed-form chain, endpoint
recursion -- verbatim); declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_scaled_jost_reference_probe.py
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
H_LADDER_MAX = 900             # reachable-rung cap
N_RUNGS_EXP = 42               # frozen expected rung count
K_EXP = 0.75                   # U-window k <= h^K_EXP
N_UGRID = 200                  # J1 frozen k-grid points
N_GC = 64                      # W2 interior thetas
GC_PAD = 0.2                   # W2 theta padding
TOL_GC = 1.0e-6                # W2 ward (all rungs, v1)
TOL_U0 = 1.0e-15               # W1: same-point ratio, 1 ulp (v2)
TOL_JOST = 1.0e-9              # W3 rel tol
MEMO_BS = {12: 21.0, 13: 110.6}
TOL_BS_REL = 0.10              # W4 rel tol
M_ALIAS_MAX = 32               # alias window cap
M_ALIAS_MIN = 6                # J3 participation floor
A_MIN = 1.0e-6                 # alias degeneracy guard
NMOD_FACTOR = 6.0              # n_mod = ceil(6 sqrt(a_max)) (v2)
NMOD_MIN = 64
NMOD_CAP = 1200
NGRID_FACTOR = 16              # model grid N = max(6000, 16 n_mod)
NGRID_MIN = 6000
CAL_M = 24                     # W5 calibration aliases
TOL_CAL = 0.05                 # W5 relres bar
TOL_COEF = 1.0e-6              # W6 coefficient bar
ALPHA_GRID = np.arange(-0.90, 1.50 + 1e-9, 0.02)
ALPHA_MESO = -0.364            # memo mesoscopic exponent (frozen)
ALPHA_EDGE = 0.5               # true edge exponent
REL_BEAT = 0.95                # J4 win margin
ALPHA_STAB = 0.10              # J4 LORO alpha spread bar
MESO_FAIL = 1.2                # memo cross-test bar
CTRL_FACTOR = 1.5              # control fire bars (ch1 and ch2)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


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
# (grid density, folded arm measures, Lanczos chain, CD kernel, m-function,
#  shooting, Jacobi closed-form chain: verbatim from freetail_case_bridge_
#  probe / christoffel_hypotheses_probe)

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


def build_rung(kz, scramble_seed=None):
    """Window -> pos/neg folded measures -> chain (pos) + neg nodes."""
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, _ = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    return dict(kz=kz, h=h, ys=ys, al=al, be=be, m0=m0,
                A2=2.0 * be[:h], B2=2.0 * al[:h])


def m_strip(A2, B2v, E):
    """Exact m-function of J_h^ft on the essential spectrum."""
    m = 0.5 * (-E + 1j * np.sqrt(4.0 - E * E))
    for k in range(len(A2) - 1, -1, -1):
        m = 1.0 / (B2v[k] - E - (A2[k] ** 2) * m)
    return m


def shoot_u0(A2, B2v, E):
    """Renormalized downward shooting: u_0(E) for real |E| > 2."""
    h = len(A2)
    beta = 0.5 * (E + np.sign(E) * np.sqrt(E * E - 4.0))
    up = np.ones_like(E)
    upp = 1.0 / beta
    for n in range(h + 1, 0, -1):
        Bn = B2v[n - 1] if n <= h else 0.0
        An = A2[n - 1] if n <= h else 1.0
        Anm1 = A2[n - 2] if n >= 2 else 1.0
        u = ((E - Bn) * up - An * upp) / Anm1
        upp, up = up, u
        sc = np.maximum(np.maximum(np.abs(up), np.abs(upp)), 1e-300)
        up = up / sc
        upp = upp / sc
    return up


def point_spectrum(A2, B2v):
    """Eigenvalues of J_h^ft outside [-2, 2] (shooting + bisection)."""
    h = len(A2)
    emax = 2.0
    for n in range(1, h + 2):
        b = B2v[n - 1] if n <= h else 0.0
        left = A2[n - 2] if 2 <= n <= h + 1 else (1.0 if n > h + 1
                                                  else 0.0)
        right = A2[n - 1] if n <= h else 1.0
        emax = max(emax, abs(b) + left + right)
    emax += 0.5
    tmax = 0.5 * (emax + math.sqrt(emax * emax - 4.0))
    ts = 1.0 + np.geomspace(1e-9, tmax - 1.0, 4000)
    eigs = []
    for sgn in (+1.0, -1.0):
        E = sgn * (ts + 1.0 / ts)
        v = shoot_u0(A2, B2v, E)
        idx = np.nonzero(v[:-1] * v[1:] < 0.0)[0]
        for i in idx:
            lo, hi = ts[i], ts[i + 1]
            flo = float(shoot_u0(A2, B2v,
                                 np.array([sgn * (lo + 1.0 / lo)]))[0])
            for _ in range(64):
                mid = 0.5 * (lo + hi)
                fm = float(shoot_u0(
                    A2, B2v, np.array([sgn * (mid + 1.0 / mid)]))[0])
                if flo * fm <= 0.0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            t = 0.5 * (lo + hi)
            eigs.append(sgn * (t + 1.0 / t))
    return eigs


def jost_endpoint(A2, B2v):
    """u_0(E = 2): real downward recursion, free-tail u = 1."""
    h = len(A2)
    up, upp = 1.0, 1.0
    for n in range(h + 1, 0, -1):
        Bn = B2v[n - 1] if n <= h else 0.0
        An = A2[n - 1] if n <= h else 1.0
        Anm1 = A2[n - 2] if n >= 2 else 1.0
        u = ((2.0 - Bn) * up - An * upp) / Anm1
        upp, up = up, u
    return float(up)


def jacobi_chain(a, b, n):
    """Closed-form orthonormal recurrence for the Jacobi weight
    (1-x)^a (1+x)^b on [-1, 1]."""
    al = np.empty(n)
    be = np.empty(n)
    al[0] = (b - a) / (a + b + 2.0)
    for k in range(1, n):
        d = 2.0 * k + a + b
        al[k] = (b * b - a * a) / (d * (d + 2.0))
    b1 = 4.0 * (a + 1.0) * (b + 1.0) / ((a + b + 2.0) ** 2
                                        * (a + b + 3.0))
    be[0] = math.sqrt(b1)
    for k in range(2, n + 1):
        d = 2.0 * k + a + b
        bk = (4.0 * k * (k + a) * (k + b) * (k + a + b)
              / (d * d * (d * d - 1.0)))
        be[k - 1] = math.sqrt(bk)
    mass = math.exp((a + b + 1.0) * math.log(2.0)
                    + math.lgamma(a + 1.0) + math.lgamma(b + 1.0)
                    - math.lgamma(a + b + 2.0))
    return al, be, mass


# --------------------------------------------------------- J1: Jost function
def u0_circle(A2, B2v, th):
    """Complex Jost function u_{0,h}(e^{i th}) on the band, TRUE
    normalization u_n = z^n for n > h; renormalized downward
    back-substitution (Geronimo-Case construction)."""
    th = np.asarray(th, float)
    z = np.exp(1j * th)
    E = 2.0 * np.cos(th)
    h = len(A2)
    up = np.ones(len(z), complex)      # u_{h+1} / z^{h+1}
    upp = z.copy()                     # u_{h+2} / z^{h+1}
    logs = np.zeros(len(z))
    for n in range(h + 1, 0, -1):
        Bn = B2v[n - 1] if n <= h else 0.0
        An = A2[n - 1] if n <= h else 1.0
        Anm1 = A2[n - 2] if n >= 2 else 1.0
        u = ((E - Bn) * up - An * upp) / Anm1
        upp, up = up, u
        sc = np.maximum(np.maximum(np.abs(up), np.abs(upp)), 1e-300)
        up = up / sc
        upp = upp / sc
        logs += np.log(sc)
    return up * np.exp(logs) * z ** (h + 1)


def gc_ratio(A2, B2v, th):
    """W2: f(E) pi |u_0(e^{i th})|^2 / sin(th); == 1 exactly for the
    free-tail chain (Wronskian identity)."""
    E = 2.0 * np.cos(th)
    f = np.abs(m_strip(A2, B2v, E).imag) / math.pi
    u0 = u0_circle(A2, B2v, th)
    return f * math.pi * np.abs(u0) ** 2 / np.sin(th)


# ---------------------------------------------------- J3: kernels + metric
def corrmat(K):
    d = np.sqrt(np.diag(K))
    return K / np.outer(d, d)


def relres(Cd, Cr):
    return float(np.linalg.norm(Cd - Cr, 2)
                 / np.linalg.norm(Cd, 2))


def bessel_half_corr(avec):
    """Closed-form Bessel-1/2 hard-edge kernel, correlation-
    normalized (J_{1/2}(x) = sqrt(2/(pi x)) sin x; common constants
    dropped -- they cancel in the correlation normalization)."""
    a = np.asarray(avec, float)
    k = np.sqrt(a)
    f = np.sin(k) / np.sqrt(k)
    g = np.sqrt(k) * np.cos(k) - np.sin(k) / (2.0 * np.sqrt(k))
    den = 2.0 * (a[:, None] - a[None, :]) + np.eye(len(a))
    K = (np.outer(f, g) - np.outer(g, f)) / den
    fp = np.cos(k) / np.sqrt(k) - np.sin(k) / (2.0 * k ** 1.5)
    gp = -np.sqrt(k) * np.sin(k) + np.sin(k) / (4.0 * k ** 1.5)
    K[np.diag_indices(len(a))] = (fp * g - f * gp) / (4.0 * k)
    return corrmat(K)


def bessel_half_entry(a, b):
    """Off-diagonal closed-form entry (self-test helper)."""
    ka, kb = math.sqrt(a), math.sqrt(b)
    f = lambda k: math.sin(k) / math.sqrt(k)          # noqa: E731
    g = lambda k: (math.sqrt(k) * math.cos(k)         # noqa: E731
                   - math.sin(k) / (2.0 * math.sqrt(k)))
    return (f(ka) * g(kb) - f(kb) * g(ka)) / (2.0 * (a - b))


def jacobi_cd(a_nodes, n_mod, alpha):
    """Reference (a): CD kernel of the exact Jacobi(alpha, 1/2)
    chain at x_m = 1 - a_m/(2 n_mod^2), n_mod terms."""
    al, be, mass = jacobi_chain(alpha, 0.5, n_mod)
    xm = 1.0 - np.asarray(a_nodes, float) / (2.0 * n_mod * n_mod)
    P = eval_chain(al, be, mass, xm, n_mod)
    return P @ P.T


def model_kernel(a_nodes, n_mod, dress_fn):
    """References (b)/(c): CD kernel of the dressed semicircle
    sin(th)^2 dth * dress(k), k = 2 n_mod sin(th/2); midpoint grid,
    Lanczos chain, n_mod terms.  Returns (K, al, be) or None."""
    N = int(max(NGRID_MIN, NGRID_FACTOR * n_mod))
    thg = (np.arange(N) + 0.5) * math.pi / N
    x = np.cos(thg)
    k = 2.0 * n_mod * np.sin(thg / 2.0)
    w = np.sin(thg) ** 2 * (math.pi / N) * dress_fn(k)
    al, be, m0, steps = lanczos_chain(x, w, n_mod + 1)
    if steps < n_mod + 1:
        return None
    xm = 1.0 - np.asarray(a_nodes, float) / (2.0 * n_mod * n_mod)
    P = eval_chain(al, be, m0, xm, n_mod)
    return P @ P.T, al, be


def alias_window(r):
    """FROZEN alias rule: neg nodes sorted by descending y; keep
    m while sqrt(a_m) <= h^K_EXP and m <= 32; drop a_m < A_MIN."""
    h = r["h"]
    o = np.argsort(-r["ys"])
    a = 2.0 * h * h * (1.0 - r["ys"][o])
    keep = (a >= A_MIN) & (np.sqrt(np.maximum(a, 0.0))
                           <= h ** K_EXP)
    idx = o[keep][:M_ALIAS_MAX]
    return idx, 2.0 * h * h * (1.0 - r["ys"][idx])


def data_kernel(r, idx):
    """The exact deployed CD kernel matrix at the alias nodes
    (h terms of the pos-measure chain)."""
    P = eval_chain(r["al"], r["be"], r["m0"], r["ys"][idx], r["h"])
    return P @ P.T


def dress_from_u(A2, B2v, h, kw):
    """(b): 1/|U_h(min(k, kw))|^2, U evaluated exactly."""
    def fn(k):
        kk = np.minimum(k, kw)
        u = u0_circle(A2, B2v, kk / h)
        return 1.0 / np.abs(u) ** 2
    return fn


def dress_from_kappa(kappas):
    """(c): prod_r kappa_r^2 / (k^2 + kappa_r^2)."""
    def fn(k):
        out = np.ones_like(k)
        for kap in kappas:
            out *= kap * kap / (k * k + kap * kap)
        return out
    return fn


def n_mod_of(a_max):
    return int(max(NMOD_MIN, min(NMOD_CAP, math.ceil(
        NMOD_FACTOR * math.sqrt(a_max)))))


def pair_thirds(vals):
    """Shallow/deep third medians (vals ordered by h)."""
    n3 = max(len(vals) // 3, 1)
    return (float(np.median(vals[:n3])),
            float(np.median(vals[-n3:])))


def shootout_rung(r, idx, a_m, kappas):
    """Residual curve over ALPHA_GRID for (a) + residuals (b)/(c)."""
    n_mod = n_mod_of(float(np.max(a_m)))
    Cd = corrmat(data_kernel(r, idx))
    curve = np.empty(len(ALPHA_GRID))
    for i, alp in enumerate(ALPHA_GRID):
        curve[i] = relres(Cd, corrmat(jacobi_cd(a_m, n_mod, alp)))
    kw = r["h"] ** K_EXP
    mb = model_kernel(a_m, n_mod, dress_from_u(r["A2"], r["B2"],
                                               r["h"], kw))
    mc = model_kernel(a_m, n_mod, dress_from_kappa(kappas))
    if mb is None or mc is None:
        return None
    res_b = relres(Cd, corrmat(mb[0]))
    res_c = relres(Cd, corrmat(mc[0]))
    return dict(n_mod=n_mod, Cd=Cd, curve=curve, res_b=res_b,
                res_c=res_c, Kb=mb[0])


def main():
    section("PRIME.PORT.JOSTREF.01 -- the scaled Jost reference "
            "kernel of the port, measured (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    alc, bec, msc = jacobi_chain(-0.5, -0.5, 6)
    cheb_ok = (max(abs(float(x)) for x in alc) <= 1e-14
               and abs(float(bec[0]) - math.sqrt(0.5)) <= 1e-14
               and max(abs(float(x) - 0.5) for x in bec[1:]) <= 1e-14
               and abs(msc - math.pi) <= 1e-12)
    check("S0.2 Jacobi recurrence self-test (Chebyshev)", cheb_ok,
          kill="PIPELINE")
    dg_ok = True
    for a0 in (7.3, 29.1, 88.4):
        num = bessel_half_entry(a0, a0 * (1.0 + 1e-6))
        Cf = bessel_half_corr(np.array([a0, 2.0 * a0]))
        del Cf                     # corr path exercised
        k0 = math.sqrt(a0)
        f0 = math.sin(k0) / math.sqrt(k0)
        g0 = (math.sqrt(k0) * math.cos(k0)
              - math.sin(k0) / (2.0 * math.sqrt(k0)))
        fp = (math.cos(k0) / math.sqrt(k0)
              - math.sin(k0) / (2.0 * k0 ** 1.5))
        gp = (-math.sqrt(k0) * math.sin(k0)
              + math.sin(k0) / (4.0 * k0 ** 1.5))
        ana = (fp * g0 - f0 * gp) / (4.0 * k0)
        dg_ok &= abs(num - ana) <= 1e-3 * max(abs(ana), 1e-6)
    check("S0.3 Bessel-1/2 diagonal: analytic limit == numeric "
          "near-diagonal (1e-3)", dg_ok, kill="PIPELINE")
    a_cal = (math.pi ** 2) * np.arange(1, CAL_M + 1, dtype=float) ** 2
    n_cal = n_mod_of(float(a_cal[-1]))
    mcal = model_kernel(a_cal, n_cal, lambda k: np.ones_like(k))
    ok_w6 = False
    ok_w5 = False
    if mcal is not None:
        Kc, alm, bem = mcal
        dev = max(float(np.max(np.abs(alm[:n_cal]))),
                  float(np.max(np.abs(bem[:n_cal - 1] - 0.5))))
        ok_w6 = dev <= TOL_COEF
        r_cal = relres(bessel_half_corr(a_cal), corrmat(Kc))
        ok_w5 = r_cal <= TOL_CAL
        print("    calibration: n_mod = %d, semicircle chain dev "
              "%.2e, model-vs-Bessel(1/2) relres %.4f"
              % (n_cal, dev, r_cal))
    check("W6 model discretization: undressed chain == Chebyshev-U "
          "(<= %.0e)" % TOL_COEF, ok_w6, kill="WARD")
    check("W5 model calibration: U==1 model kernel == closed-form "
          "Bessel-1/2 corr (relres <= %.2f)" % TOL_CAL, ok_w5,
          kill="WARD")

    section("J0 -- ladder build (all reachable rungs h <= %d)"
            % H_LADDER_MAX)
    lad = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] > H_LADDER_MAX:
            continue
        r = build_rung(kz)
        if r is None:
            print("    kz %-3d: CHAIN SHORT (skipped)" % kz)
            if kz in HEAVY:
                check("J0.h heavy rung kz %d reachable" % kz, False,
                      kill="PIPELINE")
            continue
        lad.append(r)
    lad.sort(key=lambda r: r["h"])
    check("J0.1 frozen rung count: %d reachable rungs" % N_RUNGS_EXP,
          len(lad) == N_RUNGS_EXP, "found %d" % len(lad))
    heavy_ok = all(any(r["kz"] == kz for r in lad) for kz in HEAVY)
    check("J0.2 all heavy rungs present", heavy_ok, kill="PIPELINE")
    if not heavy_ok:
        return finish(None, None, None)
    print("    h range: %d .. %d over %d rungs"
          % (lad[0]["h"], lad[-1]["h"], len(lad)))

    section("J1 -- SCALED JOST FUNCTION U_h(k) on k in [0, h^{3/4}] "
            "(%d points) + GC identity" % N_UGRID)
    ok_w1, ok_w2, ok_w3 = True, True, True
    jvals = []
    for r in lad:
        h = r["h"]
        kg = np.linspace(0.0, h ** K_EXP, N_UGRID)
        u0 = u0_circle(r["A2"], r["B2"], kg / h)
        U = u0 / u0[0]
        r["kgrid"], r["absU"] = kg, np.abs(U)
        r["jost1"] = abs(u0[0])
        jvals.append(r["jost1"])
        ok_w1 &= abs(U[0] - 1.0) <= TOL_U0
        thg = np.linspace(GC_PAD, math.pi - GC_PAD, N_GC)
        gc = gc_ratio(r["A2"], r["B2"], thg)
        gdev = float(np.max(np.abs(gc - 1.0)))
        r["gc_dev"] = gdev
        ok_w2 &= gdev <= TOL_GC
        if r["kz"] in HEAVY:
            je = jost_endpoint(r["A2"], r["B2"])
            ok_w3 &= (abs(abs(je) - r["jost1"])
                      <= TOL_JOST * max(abs(je), 1.0))
            prof = r["absU"][::N_UGRID // 10][:10]
            print("    kz %-3d h %4d: |J_h(1)| = %7.3f, GC dev "
                  "%.1e" % (r["kz"], h, r["jost1"], gdev))
            print("             |U_h| at k = 0..%.0f (10 samples): "
                  "%s" % (kg[-1], " ".join("%.3f" % v
                                           for v in prof)))
    check("W1 U_h(0) = 1 (same-point ratio, |U-1| <= %.0e, all %d "
          "rungs)" % (TOL_U0, len(lad)), ok_w1, kill="WARD")
    check("W2 Geronimo-Case identity f pi |u0|^2 = sin(theta) "
          "(<= %.0e, all rungs)" % TOL_GC, ok_w2, kill="WARD")
    check("W3 complex u_0(2) == real endpoint recursion (heavy, "
          "rel <= %.0e)" % TOL_JOST, ok_w3, kill="WARD")
    print("    |J_h(1)| ladder range: [%.2f, %.2f] (memo: "
          "[2.2, 18.8], bounded away from 0)"
          % (min(jvals), max(jvals)))

    section("J2 -- BOUND-STATE CENSUS (zeros of u_0 outside the "
            "band; frozen convention A_r = h^2 eps/2)")
    ok_w4 = True
    for r in lad:
        h = r["h"]
        eigs = point_spectrum(r["A2"], r["B2"])
        above = sorted(e for e in eigs if e > 2.0)
        below = [e for e in eigs if e < -2.0]
        A_r = [h * h * (e - 2.0) / 2.0 for e in above]
        kap = [h * math.acosh(e / 2.0) for e in above]
        r["kappas"] = kap
        r["A_r"] = A_r
        tag = ""
        if r["kz"] in MEMO_BS:
            memo = MEMO_BS[r["kz"]]
            hit = (len(A_r) > 0
                   and abs(A_r[0] - memo) <= TOL_BS_REL * memo)
            ok_w4 &= hit
            tag = "  [memo %.1f: %s]" % (memo,
                                         "HIT" if hit else "MISS")
        print("    kz %-3d h %4d: E>2 states %d (E<-2: %d) | "
              "A_r = h^2 eps/2: %s | kappa_r: %s%s"
              % (r["kz"], h, len(above), len(below),
                 " ".join("%.1f" % a for a in A_r[:4]) or "-",
                 " ".join("%.2f" % v for v in kap[:4]) or "-", tag))
    check("W4 memo bound states reproduced (kz 12 -> %.1f, kz 13 "
          "-> %.1f; nearest above-edge state, rel %.0f%%)"
          % (MEMO_BS[12], MEMO_BS[13], 100 * TOL_BS_REL), ok_w4,
          kill="WARD")

    section("J3 -- KERNEL SHOOTOUT on the alias window (correlation-"
            "normalized shape, operator-norm relres)")
    part = []
    for r in lad:
        idx, a_m = alias_window(r)
        if len(a_m) < M_ALIAS_MIN:
            print("    kz %-3d h %4d: M = %d < %d -- machinery does "
                  "not permit (skipped)"
                  % (r["kz"], r["h"], len(a_m), M_ALIAS_MIN))
            if r["kz"] in HEAVY:
                check("J3.h heavy rung kz %d participates"
                      % r["kz"], False, kill="PIPELINE")
            continue
        sr = shootout_rung(r, idx, a_m, r["kappas"])
        if sr is None:
            print("    kz %-3d: model Lanczos SHORT" % r["kz"])
            if r["kz"] in HEAVY:
                check("J3.h heavy rung kz %d model chain"
                      % r["kz"], False, kill="PIPELINE")
            continue
        r.update(sr, a_m=a_m, idx=idx, M=len(a_m))
        dev_pi = float(np.max(np.abs(
            a_m / (math.pi ** 2
                   * np.arange(1, len(a_m) + 1) ** 2) - 1.0)))
        print("    kz %-3d h %4d: M %2d, n_mod %3d, a_1 %.2f, "
              "max|a_m/(pi m)^2 - 1| %.4f (kinematics, NOT fitted)"
              % (r["kz"], r["h"], r["M"], r["n_mod"],
                 a_m[0], dev_pi), flush=True)
        part.append(r)
    if "PIPELINE" in KILLS:
        return finish(None, None, None)
    check("J3.0 participating rungs: %d of %d" % (len(part),
                                                  len(lad)),
          len(part) >= 10, kill="PIPELINE")

    # -------- common-alpha fit + LORO (reference a) ----------------
    curves = np.vstack([r["curve"] for r in part])
    mean_curve = curves.mean(axis=0)
    i_star = int(np.argmin(mean_curve))
    alpha_star = float(ALPHA_GRID[i_star])
    res_a = curves[:, i_star]
    tot = curves.sum(axis=0)
    loro_alpha = np.empty(len(part))
    loro_res_a = np.empty(len(part))
    for i in range(len(part)):
        j = int(np.argmin((tot - curves[i]) / (len(part) - 1)))
        loro_alpha[i] = ALPHA_GRID[j]
        loro_res_a[i] = curves[i, j]
    i_meso = int(np.argmin(np.abs(ALPHA_GRID - ALPHA_MESO)))
    i_edge = int(np.argmin(np.abs(ALPHA_GRID - ALPHA_EDGE)))
    res_b = np.array([r["res_b"] for r in part])
    res_c = np.array([r["res_c"] for r in part])

    print("\n    common alpha* = %+.2f (grid argmin of the mean "
          "residual; grid step 0.02)" % alpha_star)
    print("    LORO alpha: min %+.2f / max %+.2f (spread %.2f, "
          "stability bar %.2f)"
          % (float(np.min(loro_alpha)), float(np.max(loro_alpha)),
             float(np.max(loro_alpha) - np.min(loro_alpha)),
             ALPHA_STAB))
    print("\n    per-rung residual table (LORO for (a); (b)/(c) "
          "parameter-free):")
    print("      kz    h    M  | (a)J_alpha* LORO | (b)J12xU_h | "
          "(c)J12-Darboux | (a)@+0.50 | (a)@%.3f" % ALPHA_MESO)
    for i, r in enumerate(part):
        print("      %-3d %4d  %2d  |      %.4f      |   %.4f   |"
              "     %.4f     |   %.4f  |  %.4f"
              % (r["kz"], r["h"], r["M"], loro_res_a[i], res_b[i],
                 res_c[i], r["curve"][i_edge], r["curve"][i_meso]))
    med_a = float(np.median(loro_res_a))
    med_b = float(np.median(res_b))
    med_c = float(np.median(res_c))
    med_edge = float(np.median(curves[:, i_edge]))
    med_meso = float(np.median(curves[:, i_meso]))
    sh_a, dp_a = pair_thirds(loro_res_a)
    sh_b, dp_b = pair_thirds(res_b)
    sh_c, dp_c = pair_thirds(res_c)
    print("\n    medians + h-trend (shallow-third -> deep-third):")
    print("      (a) pure J_alpha (alpha* %+.2f): med %.4f | "
          "%.4f -> %.4f (%s)"
          % (alpha_star, med_a, sh_a, dp_a,
             "decreasing" if dp_a <= sh_a else "GROWING"))
    print("      (b) J_1/2 x measured U_h     : med %.4f | "
          "%.4f -> %.4f (%s)"
          % (med_b, sh_b, dp_b,
             "decreasing" if dp_b <= sh_b else "GROWING"))
    print("      (c) J_1/2 Darboux(kappa_r)   : med %.4f | "
          "%.4f -> %.4f (%s)"
          % (med_c, sh_c, dp_c,
             "decreasing" if dp_c <= sh_c else "GROWING"))
    print("      (a) at fixed alpha = +0.50   : med %.4f" % med_edge)
    print("      (a) at fixed alpha = %.3f  : med %.4f (memo "
          "mesoscopic)" % (ALPHA_MESO, med_meso))

    section("J4 -- TYPED DECISION (frozen bars)")
    best_dressed = min(med_b, med_c)
    win_dressed = "b" if med_b <= med_c else "c"
    win_trend = ((dp_b <= sh_b) if win_dressed == "b"
                 else (dp_c <= sh_c))
    alpha_stable = (float(np.max(loro_alpha) - np.min(loro_alpha))
                    <= ALPHA_STAB)
    if best_dressed <= REL_BEAT * med_a and win_trend:
        decision = "JOSTREF-J12-DRESSED"
    elif med_a <= REL_BEAT * best_dressed and alpha_stable:
        decision = "JOSTREF-PURE-ALPHA"
    else:
        decision = "JOSTREF-UNDECIDED"
    meso_fails = med_meso > MESO_FAIL * med_a
    print("    min(med_b, med_c) = %.4f (ref %s) vs %.2f x med_a "
          "= %.4f; winner trend %s; alpha stable %s"
          % (best_dressed, win_dressed, REL_BEAT,
             REL_BEAT * med_a, win_trend, alpha_stable))
    print("    MEMO CROSS-TEST: the density (mesoscopic) alpha "
          "%.3f on the KERNEL: med %.4f vs %.1f x med_a = %.4f "
          "-> %s"
          % (ALPHA_MESO, med_meso, MESO_FAIL, MESO_FAIL * med_a,
             "FAILS on the kernel (rejected as reference)"
             if meso_fails else "survives on the kernel"))
    check("J4.1 typed: %s" % decision, True)

    section("C -- controls (kz 9): scramble seed 1 + alias "
            "permutation seed 1")
    r9 = next(r for r in part if r["kz"] == 9)
    real_min = min(float(loro_res_a[part.index(r9)]), r9["res_b"],
                   r9["res_c"])
    rs = build_rung(9, scramble_seed=1)
    if rs is None:
        check("C0 scramble chain completes", False, kill="PIPELINE")
        return finish(decision, alpha_star, None)
    thg = np.linspace(GC_PAD, math.pi - GC_PAD, N_GC)
    gc_s = float(np.max(np.abs(gc_ratio(rs["A2"], rs["B2"], thg)
                               - 1.0)))
    print("    scramble GC identity dev %.1e (the Jost ALGEBRA "
          "persists -- measure-blind, stated not killed)" % gc_s)
    eig_s = point_spectrum(rs["A2"], rs["B2"])
    kap_s = [rs["h"] * math.acosh(e / 2.0) for e in eig_s
             if e > 2.0]
    idx_s, a_s = alias_window(rs)
    f1 = False
    if len(a_s) >= M_ALIAS_MIN:
        sr_s = shootout_rung(rs, idx_s, a_s, kap_s)
        if sr_s is not None:
            scr_a = float(sr_s["curve"][i_star])
            scr_min = min(scr_a, sr_s["res_b"], sr_s["res_c"])
            f1 = scr_min >= CTRL_FACTOR * real_min
            print("    ch1 scramble residuals: (a@alpha*) %.4f, "
                  "(b) %.4f, (c) %.4f -> min %.4f vs %.1f x real "
                  "min %.4f -> %s"
                  % (scr_a, sr_s["res_b"], sr_s["res_c"], scr_min,
                     CTRL_FACTOR, CTRL_FACTOR * real_min,
                     "FIRES" if f1 else "silent"))
        else:
            print("    ch1: scramble model chain short (silent)")
    else:
        print("    ch1: scramble alias window M = %d < %d "
              "(silent)" % (len(a_s), M_ALIAS_MIN))
    rng = np.random.default_rng(1)
    sig = rng.permutation(r9["M"])
    while np.all(sig == np.arange(r9["M"])):
        sig = rng.permutation(r9["M"])
    Cb9 = corrmat(r9["Kb"])
    res_perm = relres(r9["Cd"], Cb9[np.ix_(sig, sig)])
    f2 = res_perm >= CTRL_FACTOR * r9["res_b"]
    print("    ch2 alias permutation on (b): relres %.4f vs %.1f "
          "x aligned %.4f -> %s"
          % (res_perm, CTRL_FACTOR, r9["res_b"],
             "FIRES" if f2 else "silent"))
    ctrl = ("ch1+ch2" if (f1 and f2)
            else ("ch1" if f1 else ("ch2" if f2 else None)))
    check("C1 CONTROLS FIRE on the kernel-match values", f1 or f2,
          kill="CONTROL")
    return finish(decision, alpha_star, ctrl,
                  meds=(med_a, med_b, med_c))


def finish(decision, alpha_star, ctrl, meds=None):
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
        VERDICT = "JOSTREF-MEASURED"
    sub = []
    if decision:
        sub.append(decision)
    if alpha_star is not None:
        sub.append("ALPHA*=%+.2f" % alpha_star)
    if meds:
        sub.append("MED-RES(a/b/c)=%.3f/%.3f/%.3f" % meds)
    if ctrl:
        sub.append("CONTROL=%s" % ctrl)
    print("\n  VERDICT: %s (%s)" % (VERDICT, " + ".join(sub)))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
