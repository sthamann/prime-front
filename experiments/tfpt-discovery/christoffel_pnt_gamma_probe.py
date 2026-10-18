#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""christoffel_pnt_gamma_probe -- PRIME.CASE.PNTGAMMA.01
(EXPLORATION ONLY, experiments/; round 43: THE DECIDER for the
repaired sum-rule theorem -- is the one-sided Christoffel correction
gamma PNT-LEVEL (H5 closes on classical zero-free-region strength,
strictly weaker than RH) or not?  2026-08-09.)

CONTEXT (machinery verbatim from christoffel_hypotheses_probe /
freetail_case_bridge_probe): the deployed window kz carries atoms at
u_n = log n (prime powers, deployed von Mangoldt table), masses
mu_n = 2 Lambda(n)/sqrt(n), entering through tent-tapered window lags
(T115 assembly) -> grid density -> folded pos/neg measures -> Lanczos
chain -> CD kernel K_h; lambda_h(y) = 1/K_h(y, y); the neg atoms are
the tilde-masses nu~_m.  H7 (round 42) measured gamma_{h,m} =
(lambda_h - nu~_m)/Lambda^ref > 0 on all port aliases but shrinking
(min 5.9e-2 -> 1.07e-2 at kz 40).  THIS probe decides where that
correction lives: in the smooth PNT world, in the prime-power MASK
(support pattern), in the arithmetic MASS fluctuation (Lambda - 1),
or in their interaction.

FROZEN PROTOCOL (2026-08-09; constants frozen before the first
measurement run):

 THE FOUR MATCHED WORLDS (identical pipeline through lags ->
 measures -> CD kernel -> Christoffel; only the atom lag block c_at
 changes; the archimedean lags, the grid (M, D, L), the fold and the
 chain length h+1 are identical per rung):
   W1 TRUTH   : atoms (u_n, mu_n) via the deployed tent assembly.
   W2 PNT-SMOOTH (the full reference rho^0): the continuum PNT
      density 2 e^{u/2} du on u in [0, 2 alpha] (the smooth image of
      sum 2 Lambda(n) n^{-1/2} f(log n) under psi(x) ~ x, x in
      [1, X = e^{2 alpha}]) deposited on the SAME tent-tapered lag
      grid by the CLOSED-FORM integrals c^0[i] =
      -(1/2) Int tent_i(u) 2 e^{u/2} du, tent_i(u) =
      max(0, 1 - |iD - u|/D), plus the i = 0 reflection (the u < D
      mirror term of the deployed assembly, integrated exactly);
      primitive Int (A + B u) 2 e^{u/2} du = 4 e^{u/2} (A + B(u-2)).
   CELLS: b_0 = 0, b_j = (u_j + u_{j+1})/2 (j = 1..ka-1), b_ka =
      2 alpha; smooth cell mass m0_j = 4 (e^{b_j/2} - e^{b_{j-1}/2})
      (the exact rho^0 mass of atom j's Voronoi cell).
   W3 MASK ACTUAL, MASS SMOOTH: atoms at the ACTUAL positions u_n
      carrying the SMOOTH cell masses m0_n (tent assembly verbatim).
   W4 MASS ACTUAL, MASK SMOOTH: the piecewise density
      (mu_j / m0_j) 2 e^{u/2} du on cell j (actual cell masses,
      smooth profile; closed form per cell x tent piece).  With
      mu_j = m0_j for all j, W4 == W2 EXACTLY (partition identity,
      self-tested to 1e-12) and W3 == W1 by construction.

 RUNGS: heavy kz {9, 12, 13, 26, 40} + the deepest 3 REACHABLE =
   the frame-A zones with COMPLETE deployed atom table on the window
   (X = e^{2 alpha} <= ATOM_MAX = 4e5; the zones kz 142/177/243
   violate this -- their truth world is table-truncated and the
   comparison would be contaminated), sorted by (h desc, kz asc),
   top 3 not already heavy: kz 116 (h 1433), kz 90 (h 1430), kz 88
   (h 1393; tied with kz 121 at h 1393, tie broken by smaller kz).
   Pre-sizing (zone table + one chain timing) disclosed below.

 G1 PER WORLD r AND PORT ALIAS m <= h^{3/4}/pi (N_al =
   floor(h^{3/4}/pi); aliases = that world's N_al neg nodes closest
   to x = +1, RANK-PAIRED across worlds by closeness order; alias
   positions printed so misalignment is visible): the exact discrete
   Christoffel lambda^{(r)}_m = 1/K_h^{(r)}(y_m, y_m), the target
   mass nu^{(r)}_m (that world's neg atom), and gamma^{(r)}_{h,m} =
   (lambda^{(r)}_m - nu^{(r)}_m) / Lambda^0_m with Lambda^0_m =
   lambda^{(2)}_m (the W2 Christoffel at ITS m-th alias -- the
   common reference; so gamma^{(2)}_m = 1 - T^{(2)}_m exactly).
   Print the four gamma profiles per rung (first 8 aliases + min +
   median over all N_al).

 G2 THE DECOMPOSITION: gamma^{(1)} - gamma^{(2)} = (MASK:
   gamma^{(3)} - gamma^{(2)}) + (MASS: gamma^{(4)} - gamma^{(2)})
   + (INTERACTION: remainder), evaluated per rung at m* =
   argmin_m gamma^{(1)}_m and as medians over aliases.  Dominant
   piece = largest |.| at m*; the cross-rung answer = the majority
   dominant over the deep half (the 4 largest-h rungs) + its sign.

 G3 THE ENVELOPE FIT (typed): y(h) = min_m gamma^{(2)} against the
   candidates c / c/log X / c/(log X)^2 / c h^{-p} (log X = 2 alpha
   per rung), least squares in log space; TRAIN on the 5 smallest-h
   rungs, PREDICT the 3 largest (leave-last-third-out); winner =
   min test RMSE; DISCRIMINATION honest: RESOLVED only if the
   runner-up test RMSE >= 1.25x the winner's, else UNRESOLVED
   (eight points); any y <= 0 -> UNRESOLVED (reason printed).

 G4 THE VK PROPAGATION (the rigorous half, measured): per W2 port
   alias the Christoffel MINIMIZER p*_m(x) = K^{(2)}(x, y_m) /
   K^{(2)}(y_m, y_m) (coefficients P^{(2)}_k(y_m)/K^{(2)}(y_m,y_m)
   in the W2 orthonormal chain); eps_m = |Int p*^2 d(mu^{(1)} -
   rho^0)| / Int p*^2 d rho^0 with Int p*^2 d rho^0 = lambda^{(2)}_m
   EXACTLY (orthonormality; recomputed numerically as a pipeline
   check <= 1e-8) and Int p*^2 d mu^{(1)} = the W1 pos-measure
   quadratic form; eps_A^exact(h) = max_m eps_m.  TYPED against
   min gamma^{(2)} on the deep half (4 largest-h rungs), ratio_r =
   eps_A(r) / min gamma^{(2)}(r):
     PNT-CLOSES       iff every deep ratio <= 0.5 AND the deep
                      ratio trend does not cross (last <= first);
     PNT-INSUFFICIENT iff any deep ratio >= 1.0 OR any deep
                      min gamma^{(2)} <= 0;
     UNRESOLVED       otherwise.
   HONEST FENCE: this replaces the analytic Vinogradov-Korobov
   bound by the MEASURED arithmetic deviation on the deployed
   window; the analytic closure additionally needs the VK-to-eps_A
   lemma (an unconditional |psi(x) - x| bound propagated through
   the same finite Gram comparison) -- NOT proved here, and the
   textbook explicit bounds do not apply at our tiny X.

 C  CONTROLS (kz 9, scramble seed 1, mirroring the deployed
   scramble: positions uniform on (0, 2 alpha), SAME masses):
   (value control) the scrambled-truth gamma at the port must flip
   sign (min_m gamma^{scr} <= 0 against the real W2 reference);
   (persistence) the four-world pipeline + the scramble chain all
   complete with finite outputs.  Value control silent ->
   CONTROL-DEAD.

 SELF-TESTS (S0, kill PIPELINE on failure): (i) closed-form W2
   lags vs 64-pt Gauss-Legendre quadrature per tent piece on kz 9
   (rel sup <= 1e-10); (ii) W4 with unit scales == W2 (partition
   identity, rel sup <= 1e-12); (iii) AST firewall clean.

KILLS: chain short / non-finite Christoffels / self-test failure /
alias sets empty -> PIPELINE-BROKEN; value control silent ->
CONTROL-DEAD.  G1..G4 outcomes are MEASUREMENTS, never kills.

VERDICT (frozen enum): PNTGAMMA-MEASURED (+ typed decision
PNT-CLOSES / PNT-INSUFFICIENT / UNRESOLVED) / PIPELINE-BROKEN /
CONTROL-DEAD.

SPEC AMENDMENTS (fail-first preserved):
  v1 (2026-08-09): initial freeze.  Pre-sizing (before the first
  measurement run) fixed the deep-rung eligibility rule (complete
  atom table X <= 4e5) and the deepest-3 selection kz 116/90/88;
  chain timing 0.6 s at h = 1433 -- the full battery fits the
  budget with slack.
  v2 (2026-08-09, after the first full run; fail-first -- every
  typed outcome of the first run is UNCHANGED by this amendment):
  (a) the smooth worlds carry far FEWER neg nodes than the truth
  (their density has few sign changes), so the frozen cap N_al ->
  min neg-node count binds on EVERY rung (disclosed per rung); the
  rank-paired alias POSITIONS nevertheless coincide across worlds
  bit for bit (printed).  (b) the PNT reference gap min gamma^{(2)}
  measured NEGATIVE on every rung, so the G4 ratio display divided
  by the 1e-300 guard and printed garbage -- the DISPLAY now says
  n/a when the reference gap is <= 0; the frozen decision branch
  (nonpositive deep reference gap -> PNT-INSUFFICIENT) is what
  decides and was hit already in the first run.  (c) G3 stays typed
  UNRESOLVED per freeze on a nonpositive gap; a clearly-labelled
  DESCRIPTIVE addendum fit of the magnitude |min gamma^{(2)}| and a
  descriptive eps_A-vs-TRUTH-gap ratio line were added (reported,
  never typed).  No bar, no world construction, no rung changed.

NO RH claim: gamma > 0 at PNT strength would close H5 of the
repaired sum-rule theorem on classical zero-free-region estimates
(strictly weaker than RH); this probe MEASURES the four-world
anatomy on the deployed finite family -- it proves no bound, no
rate, no uniformity in h.  No marker moves.

FIREWALL: no zeros, no prime oracles beyond the deployed table
(AST scan: zetazero/nzeros/primerange/isprime/primepi/nextprime/
prevprime banned); v563 READ-ONLY; RNG only in the scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts (window geometry, tent
assembly, arch lags, deployed atom table); christoffel_hypotheses_
probe / freetail_case_bridge_probe (fold + chain + CD machinery,
verbatim), declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/christoffel_pnt_gamma_probe.py
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
DEEP3 = (88, 90, 116)          # frozen pre-sizing (see docstring)
RUNGS = tuple(sorted(set(HEAVY) | set(DEEP3)))
N_GL_SELF = 64                 # self-test quadrature order
TOL_SELF_GL = 1.0e-10          # closed form vs quadrature, rel sup
TOL_SELF_PART = 1.0e-12        # W4(unit) == W2 partition identity
TOL_QF = 1.0e-8                # numeric qf_PNT vs lambda^{(2)}
FIT_TRAIN = 5                  # G3: train on 5 smallest-h rungs
FIT_TEST = 3                   # G3: predict the 3 largest
FIT_DISCRIM = 1.25             # runner-up RMSE >= this x winner
DEEP_HALF = 4                  # G4: the 4 largest-h rungs
BAR_CLOSE = 0.5                # eps_A <= this x min gamma^(2)
BAR_INSUF = 1.0                # eps_A >= this x min gamma^(2)
SCRAMBLE_SEED = 1
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
WNAME = {1: "W1 truth", 2: "W2 pnt  ", 3: "W3 mask ", 4: "W4 mass "}

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
# (grid density, folded measures, Lanczos chain, CD kernel: verbatim from
#  christoffel_hypotheses_probe / freetail_case_bridge_probe)

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


# ------------------------------------------------- the four world lag blocks
def _prim(u, A, B):
    """Primitive of (A + B u) 2 e^{u/2}: 4 e^{u/2} (A + B (u - 2))."""
    return 4.0 * np.exp(0.5 * u) * (A + B * (u - 2.0))


def cont_lags(alpha, M, seg_lo, seg_hi, seg_sc):
    """Tent lags of the density sc_j 2 e^{u/2} du on [lo_j, hi_j]:
    c[i] = -(1/2) sum_j sc_j Int_{seg_j} tent_i(u) 2 e^{u/2} du,
    plus the exact i = 0 reflection (u < D mirror of the deployed
    tent assembly).  Closed form per (segment x tent piece)."""
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


def world_lags(alpha, M, uu, mm, m0c, bb, world,
               scramble_seed=None):
    """The atom lag block c_at of one world (see FROZEN PROTOCOL)."""
    if scramble_seed is not None:
        rng = np.random.default_rng(scramble_seed)
        us = np.sort(rng.uniform(0.0, 2.0 * alpha, size=len(uu)))
        return np.asarray(
            core.atom_lags_at(alpha, M, us, mm)[0], float)
    if world == 1:
        return np.asarray(
            core.atom_lags_at(alpha, M, uu, mm)[0], float)
    if world == 2:
        return cont_lags(alpha, M, [0.0], [2.0 * alpha], [1.0])
    if world == 3:
        return np.asarray(
            core.atom_lags_at(alpha, M, uu, m0c)[0], float)
    return cont_lags(alpha, M, bb[:-1], bb[1:], mm / m0c)   # W4


def build_world(geom, world, scramble_seed=None):
    """One world's measures + chain + port-alias Christoffel data."""
    alpha, M, h = geom["alpha"], geom["M"], geom["h"]
    c_at = world_lags(alpha, M, geom["uu"], geom["mm"],
                      geom["m0c"], geom["bb"], world,
                      scramble_seed=scramble_seed)
    d = grid_density(geom["c_ar"] + c_at)
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, _ = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1:
        return None
    o = np.argsort(-ys)[:geom["n_al"]]              # rank pairing
    Pn = eval_chain(al, be, m0, ys[o], h)
    Kd = np.sum(Pn ** 2, axis=1)
    return dict(xs=xs, ws=ws, y_al=ys[o], nu_al=vs[o],
                lam_al=1.0 / Kd, n_neg=len(ys),
                al=al, be=be, m0=m0)


def cells_of(uu, alpha):
    """FROZEN Voronoi cells on [0, 2 alpha] + exact rho^0 masses."""
    bb = np.concatenate([[0.0], 0.5 * (uu[1:] + uu[:-1]),
                         [2.0 * alpha]])
    m0c = 4.0 * (np.exp(0.5 * bb[1:]) - np.exp(0.5 * bb[:-1]))
    return bb, m0c


def build_geometry(kz):
    rr = core.build_window(kz)
    alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    bb, m0c = cells_of(uu, alpha)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    n_al = int(h ** 0.75 / math.pi)
    return dict(kz=kz, alpha=alpha, M=M, h=h, D=D, uu=uu, mm=mm,
                bb=bb, m0c=m0c, c_ar=c_ar, n_al=n_al,
                X=math.exp(2.0 * alpha))


def gamma_profiles(worlds, n_al):
    """gamma^{(r)}_m = (lambda^{(r)}_m - nu^{(r)}_m)/Lambda^0_m."""
    lam0 = worlds[2]["lam_al"][:n_al]
    gam = {}
    for r in (1, 2, 3, 4):
        w = worlds[r]
        gam[r] = ((w["lam_al"][:n_al] - w["nu_al"][:n_al]) / lam0)
    return gam, lam0


def prof_line(tag, g):
    head = " ".join("%+.2e" % v for v in g[:8])
    return ("    %s: %s | min %+.3e med %+.3e"
            % (tag, head, float(np.min(g)), float(np.median(g))))


def fit_models(hs, lx, ys):
    """G3 candidate fits in log space; returns per-model
    (name, predict(h, lx), train_resid, params)."""
    ly = np.log(ys)
    out = []

    def lstsq(Amat, rhs):
        sol, *_ = np.linalg.lstsq(Amat, rhs, rcond=None)
        return sol

    lh = np.log(hs)
    llx = np.log(lx)
    # c
    c0 = float(np.mean(ly))
    out.append(("c            ", lambda h_, x_: np.full(len(h_), c0),
                "c=%.3e" % math.exp(c0)))
    # c / log X
    c1 = float(np.mean(ly + llx))
    out.append(("c/logX       ",
                lambda h_, x_: c1 - np.log(x_),
                "c=%.3e" % math.exp(c1)))
    # c / (log X)^2
    c2 = float(np.mean(ly + 2.0 * llx))
    out.append(("c/(logX)^2   ",
                lambda h_, x_: c2 - 2.0 * np.log(x_),
                "c=%.3e" % math.exp(c2)))
    # c h^-p
    A = np.vstack([np.ones_like(lh), -lh]).T
    sol = lstsq(A, ly)
    c3, p3 = float(sol[0]), float(sol[1])
    out.append(("c h^-p       ",
                lambda h_, x_: c3 - p3 * np.log(h_),
                "c=%.3e p=%.3f" % (math.exp(c3), p3)))
    return out


def main():
    section("PRIME.CASE.PNTGAMMA.01 -- four-world PNT anatomy of the "
            "port Christoffel correction (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")

    print("\nS0 -- firewall + self-tests")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS),
          kill="PIPELINE")

    g9 = build_geometry(9)
    # (i) closed form vs Gauss-Legendre per tent piece (kz 9, W2)
    gx, gw = np.polynomial.legendre.leggauss(N_GL_SELF)
    alpha, M, D = g9["alpha"], g9["M"], g9["D"]
    c_ref = np.zeros(M)
    for i in range(M):
        tot = 0.0
        for a, b in (((i - 1) * D, i * D), (i * D, (i + 1) * D)):
            a = max(a, 0.0)
            b = min(b, 2.0 * alpha)
            if b <= a:
                continue
            uq = 0.5 * (b - a) * gx + 0.5 * (a + b)
            tent = 1.0 - np.abs(i * D - uq) / D
            tot += 0.5 * (b - a) * float(
                np.sum(gw * tent * 2.0 * np.exp(0.5 * uq)))
        if i == 0:
            b0 = min(D, 2.0 * alpha)
            uq = 0.5 * b0 * gx + 0.5 * b0
            tot += 0.5 * b0 * float(np.sum(
                gw * (1.0 - uq / D) * 2.0 * np.exp(0.5 * uq)))
        c_ref[i] = -0.5 * tot
    c_w2 = cont_lags(alpha, M, [0.0], [2.0 * alpha], [1.0])
    dev = float(np.max(np.abs(c_w2 - c_ref))
                / np.max(np.abs(c_ref)))
    check("S0.2 W2 closed-form lags == %d-pt GL quadrature (kz 9)"
          % N_GL_SELF, dev <= TOL_SELF_GL, "rel sup dev %.2e" % dev,
          kill="PIPELINE")
    # (ii) partition identity: W4 at unit scales == W2
    c_w4u = cont_lags(alpha, M, g9["bb"][:-1], g9["bb"][1:],
                      np.ones(len(g9["m0c"])))
    devp = float(np.max(np.abs(c_w4u - c_w2))
                 / np.max(np.abs(c_w2)))
    check("S0.3 partition identity W4(unit scales) == W2",
          devp <= TOL_SELF_PART, "rel sup dev %.2e" % devp,
          kill="PIPELINE")

    section("B0 -- rungs (geometry + smooth-mass sanity)")
    G = {}
    for kz in RUNGS:
        g = build_geometry(kz) if kz != 9 else g9
        G[kz] = g
        rat = g["mm"] / g["m0c"]
        print("    kz %-3d h %4d M %4d: atoms %5d, X %.3e, N_al %2d"
              " | mass/smooth-cell-mass: med %.3f  [%.2e, %.2e],"
              " total %.4f"
              % (kz, g["h"], g["M"], len(g["uu"]), g["X"],
                 g["n_al"], float(np.median(rat)),
                 float(np.min(rat)), float(np.max(rat)),
                 float(np.sum(g["mm"]) / np.sum(g["m0c"]))))
    order = sorted(RUNGS, key=lambda kz: G[kz]["h"])

    section("G1 -- the four gamma profiles per rung "
            "(rank-paired port aliases, Lambda^0 = W2 Christoffel)")
    RES = {}
    ok_g1 = True
    for kz in order:
        g = G[kz]
        worlds = {}
        for r in (1, 2, 3, 4):
            w = build_world(g, r)
            if w is None:
                ok_g1 = False
                print("    kz %-3d world %d: CHAIN SHORT" % (kz, r))
                break
            worlds[r] = w
        if len(worlds) < 4:
            break
        n_al = min(g["n_al"],
                   min(len(w["y_al"]) for w in worlds.values()))
        if n_al < g["n_al"]:
            print("    kz %-3d: N_al capped %d -> %d (neg-node "
                  "count)" % (kz, g["n_al"], n_al))
        if n_al == 0:
            ok_g1 = False
            break
        gam, lam0 = gamma_profiles(worlds, n_al)
        ok_g1 &= all(bool(np.all(np.isfinite(gam[r])))
                     for r in gam)
        h = g["h"]
        a1 = 2.0 * h * h * (1.0 - worlds[1]["y_al"][:8])
        a2 = 2.0 * h * h * (1.0 - worlds[2]["y_al"][:8])
        print("  kz %-3d h %4d (N_al %d):  alias a_m truth: %s"
              % (kz, h, n_al,
                 " ".join("%8.2f" % v for v in a1)))
        print("                          alias a_m W2   : %s"
              % " ".join("%8.2f" % v for v in a2))
        for r in (1, 2, 3, 4):
            print(prof_line(WNAME[r], gam[r]))
        RES[kz] = dict(gam=gam, lam0=lam0, n_al=n_al,
                       worlds=worlds)
    check("G1.0 four-world chains complete, gammas finite", ok_g1,
          kill="PIPELINE")
    if not ok_g1:
        return finish(None, None, None, None)

    section("G2 -- decomposition gamma_truth - gamma_PNT = MASK + "
            "MASS + INTERACTION (at m* = argmin gamma^(1); medians)")
    dom_seq = []
    for kz in order:
        gam = RES[kz]["gam"]
        ms = int(np.argmin(gam[1]))
        d_mask = gam[3] - gam[2]
        d_mass = gam[4] - gam[2]
        d_int = (gam[1] - gam[2]) - d_mask - d_mass
        pieces = dict(MASK=float(d_mask[ms]),
                      MASS=float(d_mass[ms]),
                      INT=float(d_int[ms]))
        dom = max(pieces, key=lambda k: abs(pieces[k]))
        dom_seq.append((kz, dom, pieces[dom]))
        print("    kz %-3d h %4d m*=%2d: g1 %+.3e g2 %+.3e | "
              "MASK %+.3e MASS %+.3e INT %+.3e -> %s"
              % (kz, G[kz]["h"], ms + 1, float(gam[1][ms]),
                 float(gam[2][ms]), pieces["MASK"], pieces["MASS"],
                 pieces["INT"], dom))
        print("           medians over m: MASK %+.3e MASS %+.3e "
              "INT %+.3e  (g1-g2 %+.3e)"
              % (float(np.median(d_mask)), float(np.median(d_mass)),
                 float(np.median(d_int)),
                 float(np.median(gam[1] - gam[2]))))
    deep_doms = [d for (kz, d, v) in dom_seq
                 if kz in [k for k in order[-DEEP_HALF:]]]
    dom_answer = max(set(deep_doms), key=deep_doms.count)
    dom_vals = [v for (kz, d, v) in dom_seq
                if kz in [k for k in order[-DEEP_HALF:]]
                and d == dom_answer]
    dom_sign = "+" if float(np.median(dom_vals)) > 0 else "-"
    print("    deep-half dominant piece: %s (sign %s; %d/%d deep "
          "rungs)" % (dom_answer, dom_sign,
                      deep_doms.count(dom_answer), len(deep_doms)))
    check("G2.1 decomposition exact (identity by construction)",
          True)

    section("G3 -- envelope fit of min gamma^(2) (train %d shallow, "
            "predict %d deep)" % (FIT_TRAIN, FIT_TEST))
    hs = np.array([G[kz]["h"] for kz in order], float)
    lx = np.array([2.0 * G[kz]["alpha"] for kz in order])
    yg2 = np.array([float(np.min(RES[kz]["gam"][2]))
                    for kz in order])
    for kz, y in zip(order, yg2):
        print("    kz %-3d h %4d logX %6.2f: min gamma^(2) %+.4e"
              % (kz, G[kz]["h"], 2.0 * G[kz]["alpha"], y))
    if np.any(yg2 <= 0.0):
        g3_type = "UNRESOLVED"
        g3_win = "n/a (non-positive reference gap)"
        print("    non-positive min gamma^(2) -> envelope fit "
              "UNRESOLVED (typed per freeze)")
        # DESCRIPTIVE ADDENDUM (v2; reported, never typed): the
        # magnitude |min gamma^(2)| against the same candidates.
        ya = np.abs(yg2)
        tr = slice(0, FIT_TRAIN)
        te = slice(FIT_TRAIN, FIT_TRAIN + FIT_TEST)
        models = fit_models(hs[tr], lx[tr], ya[tr])
        rms = []
        for name, pred, par in models:
            e_te = float(np.sqrt(np.mean(
                (pred(hs[te], lx[te]) - np.log(ya[te])) ** 2)))
            rms.append((e_te, name, par))
            print("    [addendum |.|] %s TEST-RMSE %.3f  (%s)"
                  % (name, e_te, par))
        rms.sort()
        print("    [addendum |.|] best descriptor: %s (runner-up/"
              "winner %.2f)" % (rms[0][1].strip(),
                                rms[1][0] / max(rms[0][0], 1e-300)))
    else:
        tr = slice(0, FIT_TRAIN)
        te = slice(FIT_TRAIN, FIT_TRAIN + FIT_TEST)
        models = fit_models(hs[tr], lx[tr], yg2[tr])
        rms = []
        for name, pred, par in models:
            e_tr = float(np.sqrt(np.mean(
                (pred(hs[tr], lx[tr]) - np.log(yg2[tr])) ** 2)))
            e_te = float(np.sqrt(np.mean(
                (pred(hs[te], lx[te]) - np.log(yg2[te])) ** 2)))
            rms.append((e_te, name, par, e_tr))
            print("    %s train-RMSE %.3f  TEST-RMSE %.3f  (%s)"
                  % (name, e_tr, e_te, par))
        rms.sort()
        g3_win = rms[0][1].strip()
        ratio = rms[1][0] / max(rms[0][0], 1e-300)
        resolved = ratio >= FIT_DISCRIM
        g3_type = ("WINNER %s" % g3_win) if resolved else "UNRESOLVED"
        print("    winner %s; runner-up/winner test-RMSE ratio "
              "%.2f (bar %.2f) -> %s"
              % (g3_win, ratio, FIT_DISCRIM,
                 "RESOLVED" if resolved else
                 "UNRESOLVED (honest: %d points)" % len(order)))
    check("G3.1 typed: %s (envelope of the PNT reference gap)"
          % g3_type, True)

    section("G4 -- measured VK propagation: eps_A^exact vs "
            "min gamma^(2) (bars %.2f / %.2f on the deep half)"
            % (BAR_CLOSE, BAR_INSUF))
    ok_g4 = True
    eps_seq = {}
    for kz in order:
        g = G[kz]
        w1, w2 = RES[kz]["worlds"][1], RES[kz]["worlds"][2]
        n_al = RES[kz]["n_al"]
        h = g["h"]
        P2a = eval_chain(w2["al"], w2["be"], w2["m0"],
                         w2["y_al"][:n_al], h)
        K2 = np.sum(P2a ** 2, axis=1)
        coef = P2a / K2[:, None]                    # p*_m coefficients
        E1 = eval_chain(w2["al"], w2["be"], w2["m0"], w1["xs"], h)
        vals1 = E1 @ coef.T                         # p*_m at W1 atoms
        qf1 = w1["ws"] @ (vals1 ** 2)
        E2 = eval_chain(w2["al"], w2["be"], w2["m0"], w2["xs"], h)
        qf2n = w2["ws"] @ ((E2 @ coef.T) ** 2)
        lam2 = 1.0 / K2
        qdev = float(np.max(np.abs(qf2n / lam2 - 1.0)))
        ok_g4 &= (qdev <= TOL_QF and bool(np.all(np.isfinite(qf1))))
        eps_m = np.abs(qf1 - lam2) / lam2
        eps_seq[kz] = float(np.max(eps_m))
        mg2 = float(np.min(RES[kz]["gam"][2]))
        mg1 = float(np.min(RES[kz]["gam"][1]))
        rat_s = ("%.3f" % (eps_seq[kz] / mg2) if mg2 > 0.0
                 else "n/a (ref gap <= 0)")
        print("    kz %-3d h %4d: eps_A^exact %.4e  min gamma^(2) "
              "%+.4e  ratio %s  (med eps %.2e; qf self-test %.1e; "
              "descriptive eps/min gamma^(1) %.0f)"
              % (kz, h, eps_seq[kz], mg2, rat_s,
                 float(np.median(eps_m)), qdev,
                 eps_seq[kz] / max(mg1, 1e-300)))
    check("G4.0 quadratic-form pipeline sane (qf == lambda^(2) to "
          "%.0e; finite)" % TOL_QF, ok_g4, kill="PIPELINE")
    deep = order[-DEEP_HALF:]
    mg2d = {kz: float(np.min(RES[kz]["gam"][2])) for kz in deep}
    nonpos = any(mg2d[kz] <= 0.0 for kz in deep)
    ratios = [(eps_seq[kz] / mg2d[kz] if mg2d[kz] > 0.0
               else float("inf")) for kz in deep]
    if nonpos or max(ratios) >= BAR_INSUF:
        decision = "PNT-INSUFFICIENT"
    elif max(ratios) <= BAR_CLOSE and ratios[-1] <= ratios[0]:
        decision = "PNT-CLOSES"
    else:
        decision = "UNRESOLVED"
    print("    deep-half ratios (h asc): %s%s"
          % (" ".join(("%.3f" % r if math.isfinite(r) else "inf")
                      for r in ratios),
             "; NONPOS ref gap" if nonpos else ""))
    print("    -> typed decision: %s  (CLOSES: all <= %.2f and "
          "non-crossing; INSUFFICIENT: any >= %.2f)"
          % (decision, BAR_CLOSE, BAR_INSUF))
    print("    honest fence: analytic closure still needs the "
          "VK-to-eps_A lemma on top of this measured deviation.")
    check("G4.1 typed: %s (measured eps_A vs the PNT reference "
          "gap)" % decision, True)

    section("C -- controls (kz 9, scramble seed %d)"
            % SCRAMBLE_SEED)
    ws = build_world(G[9], 1, scramble_seed=SCRAMBLE_SEED)
    if ws is None:
        check("C0 scramble chain completes", False, kill="PIPELINE")
        return finish(None, None, None, None)
    n_al9 = min(RES[9]["n_al"], len(ws["y_al"]))
    lam0 = RES[9]["lam0"][:n_al9]
    gam_s = (ws["lam_al"][:n_al9] - ws["nu_al"][:n_al9]) / lam0
    fin = bool(np.all(np.isfinite(gam_s)))
    fires = bool(np.min(gam_s) <= 0.0)
    print("    scramble gamma at the port: %s"
          % " ".join("%+.2e" % v for v in gam_s[:8]))
    print("    min %+.3e (real W1 min %+.3e) -> %s; flipped %d/%d"
          % (float(np.min(gam_s)),
             float(np.min(RES[9]["gam"][1])),
             "FIRES" if fires else "SILENT",
             int(np.sum(gam_s <= 0.0)), n_al9))
    check("C1 value control fires (scramble flips gamma sign at "
          "the port)", fires and fin, kill="CONTROL")
    check("C2 four-world pipeline persists (all chains + scramble "
          "finite)", fin)

    return finish(decision, g3_type, (dom_answer, dom_sign),
                  dict(order=order, eps=eps_seq,
                       mg2={kz: float(np.min(RES[kz]["gam"][2]))
                            for kz in order}))


def finish(decision, g3_type, dom, extra):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if "PIPELINE" in KILLS:
        VERDICT = "PIPELINE-BROKEN"
    elif "CONTROL" in KILLS:
        VERDICT = "CONTROL-DEAD"
    else:
        VERDICT = "PNTGAMMA-MEASURED"
    sub = []
    if decision:
        sub.append("DECISION=%s" % decision)
    if g3_type:
        sub.append("ENVELOPE=%s" % g3_type)
    if dom:
        sub.append("DOMINANT=%s(%s)" % dom)
    print("\n  VERDICT: %s%s"
          % (VERDICT, (" (%s)" % "; ".join(sub)) if sub else ""))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
