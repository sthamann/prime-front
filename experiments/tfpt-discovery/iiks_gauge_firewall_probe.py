#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""iiks_gauge_firewall_probe -- PRIME.PORT.MOEBIUS.GAUGEFW.01
(EXPLORATION ONLY, experiments/; round 48, reviewer probes 2+3 of
the round-47 review: prove the carrier invariance is NOT
manufactured by the per-rung normalization, 2026-08-09).

THE QUESTION (frozen): moebius_source_step_probe measured
CARRIER-INVARIANT -- but under a PER-RUNG three-point PSL(2,R)
normalization.  The reviewer's tautology warning: a per-rung gauge
choice G_h is a free function of h; choosing G_{h+1} = G_h M_h^{-1}
forces every step to the identity.  THE FIVE GAUGE-VALIDITY
CONDITIONS (reviewer, quoted verbatim): a valid gauge must be
"(1) frozen before comparison, (2) source-only, (3) identically
defined on all rungs, (4) unchanged on truth and controls,
(5) using NO neighbor-rung information."  This probe re-derives
everything in three SOURCE-FROZEN gauges satisfying (1)-(5), asks
where the discarded scalar lambda went (reviewer probe 2), and
tests whether the Moebius step is the projectivization of the
source Jacobi transfer (reviewer probe 3).

THE LADDER (frozen, predecessor verbatim): all frame-A zones
(core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive rung pairs with >= 8 common port alias indices.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
all bars frozen before the run):

 W   PIPELINE (predecessor verbatim): heavy build per rung, SPEC
     v2 IIKS extraction of the antisymmetric generators (f, g) of
     C = [Y, D_P] (NO gauge rotation applied at extraction; each
     gauge below fixes its own frame).  Wards: W1 >= 30 rungs;
     W2 [Y, D_P] rank 2 on every rung (s3/s1 <= 1e-10); W3 the
     frozen reference set exists.  FROZEN REFERENCES: J* = alias
     indices present on >= 0.90 of rungs (deterministic
     availability stepdown 0.90 -> 0.80 -> 0.70 if |J*| < 4,
     reported); reference PAIR = two smallest J* indices
     (jr1 < jr2); step ANCHORS = three smallest J* indices.  These
     are GRID indices, not rung-dependent choices -- conditions
     (1)-(5) hold: frozen rule, source-side index bookkeeping
     only, same rule on every rung and on the controls, no
     neighbor-rung data.

 G0  BASELINE (printed, not a claim): the predecessor's per-rung
     three-point normalization + TLS step fit, machinery verbatim
     -- reproduces the numbers the reviewer challenged (median fit
     residual, median identity-candidate residual).

 G1  SOURCE-FROZEN GAUGES (three candidates, all rung-local and
     source-only; each fully fixes the GL(2) frame of (f, g)):
     (i)  WRONSKIAN gauge "W": the unique generator basis with
          (f(jr1), f(jr2)) = (1, 0) and (g(jr1), g(jr2)) = (0, 1)
          -- then the antisymmetric pairing W(jr1, jr2) =
          f(jr1) g(jr2) - g(jr1) f(jr2) = 1 at the FIXED reference
          pair of grid indices, and g's component along the frozen
          reference direction e_{jr1} vanishes at the deepest
          reference node (g(jr1) = 0), as demanded.  PRECISE
          STATEMENT of the amendment: the prompt's two conditions
          (pairing = 1, g(jr1) = 0) leave a one-parameter shear
          f -> f + t g free (it preserves both); the interpolation
          frame above realizes both conditions AND kills the
          shear; it is the unique completion that stays rung-local
          and reference-pair-only.  Degenerate 2x2 node matrix
          (s2/s1 <= 1e-12) or missing reference index = typed
          rung skip.
     (ii) ASYMPTOTIC gauge "A": window-edge (y -> 1) frame.  Edge
          functionals from the rung's OWN two deepest port nodes
          (largest y): L1(v) = linear extrapolation of v to y = 1,
          L2(v) = (v(y_1) - v(y_0))/(y_0 - y_1) (the leading slope
          in 1 - y).  Frame: (L1, L2)(f) = (1, 0), (L1, L2)(g) =
          (0, 1) -- f carries the unit leading coefficient, g is
          purely subleading.  Source-computable from the
          extraction; same rule on every rung.
     (iii) DETERMINANT-PHASE gauge "D": det-normalize the
          extraction SVD convention itself: f = U[:, 0], g =
          U[:, 1] (unit vectors, det-scale s1 divided out), the
          orientation sign fixed by C = +s1 (f g^T - g f^T), the
          SO(2) rotation of the (degenerate) singular pair fixed
          by the frozen convention g = 0 with f > 0 at the rung's
          deepest port node (smallest alias index) -- a fixed
          sign/order convention, no per-rung choice.
     UNDER EACH GAUGE: the carrier r_h = g/f at the common nodes;
     the rung-to-rung RAW chordal deviation at matched nodes (NO
     further normalization of any kind); the step map M_h = the
     unique Moebius map through the carrier values at the three
     frozen anchors (exact three-point construction, no fitting).
     TYPED per gauge: RAW-INVARIANT iff median over steps of the
     per-step median raw chordal deviation <= 0.05, else
     RAW-MOVING.  CROSS-GAUGE: for each of the three gauge pairs,
     the single global conjugation S is solved from the FIRST
     common valid step (Sylvester nullspace; that anchor step is
     excluded from scoring) and the pairwise projective distance
     d_P(S M^a S^-1, M^b) is medianed over the remaining steps.
     TYPED: GAUGE-ROBUST iff all three pairwise medians <= 0.05
     AND the per-gauge RAW labels agree; GAUGE-MADE iff the
     baseline G0 invariance holds (median id-res <= 0.05) while NO
     frozen gauge is RAW-INVARIANT and the cross-gauge agreement
     fails at 0.20 (the reviewer kill -- reported plainly);
     GAUGE-PARTIAL otherwise.

 G2  THE SCALAR COCYCLE (reviewer probe 2, 'where did lambda
     go'): the quotient r = g/f is blind to (f, g) -> lambda_h
     (f, g).  In gauge (i) the frame is FULLY fixed, so the
     gauged generator values are data.  FROZEN: lambda_h =
     median_j |f_{h+1}(j)| / |f_h(j)| over the matched common
     nodes j (the two pinned reference nodes excluded -- f(jr1) =
     1 and f(jr2) = 0 identically by the gauge).  Printed: the
     lambda ladder, its cumulative log sum, and the tau ladder
     tau_h = 1 - lam_max(E_h) (the Krein wall margin).  SCORED:
     Pearson correlation and OLS slope of cumsum(log lambda)
     against log tau at the arriving rung, over steps with
     tau > 0.  TYPED: LAMBDA-IS-WALL iff |corr| >= 0.90 (the
     reviewer's boxed hypothesis: the projective carrier is
     universal, the arithmetic sits in the scalar cocycle);
     LAMBDA-PARTIAL iff |corr| >= 0.60; else LAMBDA-FLAT.
     (Unscored: the same correlation in gauges (ii) and (iii),
     printed.)

 G3  JACOBI TRANSFER IDENTIFICATION (reviewer probe 3): the
     SOURCE Jacobi one-step transfer of the tilde-measure chain
     (cd_pick_scalarization convention frozen: positive-arm
     folded tilde measure, Lanczos chain a_k = al[k], b_k =
     be[k]):
        T_k(z) = [[ (z - a_k)/b_k, -b_{k-1}/b_k ], [1, 0]]
     at the FROZEN spectral parameter z_ref = 1.0 (the window
     edge y -> 1 in the x = cos theta variable -- the port edge,
     rung-independent, source-only; matches the gauge (ii)
     anchor point).  CANDIDATE: the measured step M_h (gauge (i))
     ~ projectivization of the product of the Jacobi transfers
     entering between rung h and h+1: J_h = T_{h_b - 1} ... T_
     {h_a} from the DEEPER rung's chain (the chain that contains
     the entering levels); equal-h steps carry the empty product
     (identity).  COMPARISON: NO free parameters beyond the
     single global conjugation S solved from the first step with
     dh >= 5 (excluded from scoring); scored = median d_P(S J_h
     S^-1, M_h) over the remaining steps.  TYPED: JACOBI-DERIVED
     iff median <= 0.05 / JACOBI-PARTIAL iff <= 0.20 /
     JACOBI-DEAD.  Unscored diagnostic: corr(log lambda_h,
     accumulated log growth of the transfer product) -- the G2/G3
     bridge.  HONEST CAVEAT (frozen): the same identification is
     run on the SMOOTH-MASS world; if it holds there too, the
     Moebius motion is generic OPRL kinematics (universal
     geometry) and the arithmetic is confirmed to sit in G2's
     scalar / the measure itself -- reported as sublabel
     UNIVERSAL-KINEMATICS.

 SM  SMOOTH-MASS WORLD (the frame-surviving control throughout,
     christoffel_pnt_gamma W3 convention frozen: atoms at the
     ACTUAL positions u_n carrying the smooth PNT Voronoi cell
     masses m0_j = 4 (e^{b_j/2} - e^{b_{j-1}/2}), b_0 = 0, b_j =
     (u_j + u_{j+1})/2, b_ka = 2 alpha): the full ladder is
     rebuilt with the smooth comb and G1 raw deviations, the G2
     correlation and the G3 identification are re-measured with
     the SAME frozen gauges/references (condition (4)).  Frame
     survival census printed; if < 10 smooth steps are available
     the affected blocks are typed SMOOTH-UNAVAILABLE (reported,
     no kill -- the truth answer stands on its own).

 C   CONTROLS (kz 9, must fire): Epstein (lambda_eps recursion
     comb) + scramble (seed 1); frame death reported per control
     (window unavailable / lam(out) > 1 / lam(C_J) > 1 /
     extraction unavailable).  Silent on both -> CONTROL-DEAD.
     The smooth-mass world is the frame-SURVIVING control and is
     not required to fire.

KILLS: K1 pipeline ward breaks (rungs / rank-2 / references /
gauge-(i) step count / lambda ladder) -> PIPELINE-BROKEN; K3
Epstein+scramble silent -> CONTROL-DEAD.

VERDICT (frozen enum): GAUGEFW-MEASURED with typed sublabels
GAUGE-ROBUST / GAUGE-PARTIAL / GAUGE-MADE (G1, + per-gauge
RAW-INVARIANT / RAW-MOVING), LAMBDA-IS-WALL / LAMBDA-PARTIAL /
LAMBDA-FLAT (G2), JACOBI-DERIVED / JACOBI-PARTIAL / JACOBI-DEAD
(G3, + UNIVERSAL-KINEMATICS caveat where applicable); else
PIPELINE-BROKEN / CONTROL-DEAD.

SPEC v2 AMENDMENTS (documented before the first run; fail-first
preserved): (i) gauge (i) is concretized as the interpolation
frame at the frozen reference pair -- the prompt's two conditions
alone leave a one-parameter shear free (stated precisely in G1);
(ii) z_ref = 1.0 frozen (window edge; the only rung-independent
source-side spectral point); (iii) the lambda median excludes the
two gauge-pinned reference nodes (0/0 there by construction);
(iv) equal-h ladder steps carry the empty Jacobi product and the
entering levels are hosted by the deeper rung's chain; (v) the
global-conjugation anchor steps (first common step for G1 cross
pairs; first dh >= 5 step for G3) are excluded from the scored
medians; (vi) cumulative log lambda is accumulated over the
measured step sequence (typed skips break no bookkeeping).

SPEC v3 AMENDMENTS (documented after the first full run; every
first-run typed outcome is quoted so nothing is silently
upgraded): (vii) DEGENERACY GUARD: the first run printed gauge
(ii) raw deviation 0.0000 on every step -- invariance of a
COLLAPSED (near-constant) carrier is vacuous, so each gauge now
also reports the per-rung carrier SPREAD (median pairwise chordal
distance over the common nodes, the two gauge-pinned reference
nodes excluded) and types RAW-DEGENERATE iff the median spread
< 0.05; RAW-INVARIANT now additionally requires median spread >=
0.05.  (viii) ROBUST GLOBAL CONJUGATION: the first run solved S
from the single first common step; the Sylvester nullspace vector
came out singular on two of the three gauge pairs (cross d_P
printed as inf over 0 steps) because near-identity step families
make the one-step Sylvester problem ill-posed.  v3 scores the
better of TWO frozen global candidates: S = Id (the trivial
global conjugation) and S = the joint least-squares Sylvester
solve stacked over ALL common steps (still exactly ONE global
conjugation, 3 projective dof against ~40 steps); both medians
are printed.  The same robustification applies to G3 (first-run
G3 numbers under the one-step solve: truth med d_P 1.0000, smooth
med d_P 1.0000, kappa corr -0.14/-0.11).  (ix) SMOOTH-FRAME-DEAD:
the first run measured lam(E) >= 1 on ALL 42 smooth-mass rungs
(min tau -2.0e9) -- the smooth-mass world is NOT frame-surviving
under this probe's Gram frame; it is typed SMOOTH-FRAME-DEAD, its
measurements are still printed as the universality caveat (with
that caveat stated), and its G2 correlation uses log|tau| (tau <
0 throughout, disclosed).  (x) unscored diagnostic added: the
extraction scale ladder corr(log s1, log tau) over rungs (s1 =
the [Y, D_P] commutator scale) -- the scale channel the gauge-(i)
lambda (which pins f(jr1) = 1) cannot see.  (xi) G1.0 FRAME
SELF-TEST ward: every gauge frame is re-verified against its
defining linear conditions (gauge (i): interpolation values;
gauge (ii): edge functionals; gauge (iii): unit norms + rotation
zero + sign) at 1e-8 -- a broken frame is a pipeline kill (K1);
the per-gauge relative motion (median raw dev / median spread) is
printed alongside.  No frozen bar moved; first-run typed
outcomes: G1 GAUGE-PARTIAL (W:RAW-INVARIANT before the spread
guard, A:RAW-INVARIANT before the spread guard, D:RAW-MOVING;
cross d_P inf/inf/0.98 under the ill-posed one-step solve),
G2 LAMBDA-FLAT (corr 0.1292), G3 JACOBI-DEAD (med d_P 1.0000).

NO RH claim -- gauge-frozen invariance, a scalar cocycle tracking
a wall margin, or a Jacobi-transfer identification are numerical
measurements on compressed truncations, not theorems about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; extraction + ladder
machinery verbatim from moebius_source_step_probe.py /
port_schur_cocycle_probe.py (PRIME.PORT.MOEBIUS.SOURCE.01 /
PRIME.PORT.SCHURSTEP.01); Jacobi chain convention from
cd_pick_scalarization_probe.py (PRIME.CD.PICKDEFECT.01);
smooth-mass cells from christoffel_pnt_gamma_probe.py.  IIKS =
Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/iiks_gauge_firewall_probe.py
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
MIN_RUNGS = 30
MIN_PAIRS = 30
MIN_COMMON_J = 8
MIN_JSTAR = 4
JSTAR_FRACS = (0.90, 0.80, 0.70)
RANK_BAR = 1e-10
REF_SEP_MIN = 1e-6
FRAME_COND = 1e-12          # min s2/s1 of the 2x2 frame solve
CTRL_KZ = 9

RAW_INV_BAR = 0.05          # G1: RAW-INVARIANT bar (median chordal)
DP_ROBUST_BAR = 0.05        # G1: cross-gauge d_P robust bar
DP_PART_BAR = 0.20          # G1: cross-gauge d_P partial bar
LAM_WALL_CORR = 0.90        # G2: LAMBDA-IS-WALL bar
LAM_PART_CORR = 0.60        # G2: LAMBDA-PARTIAL bar
JAC_DER_BAR = 0.05          # G3: JACOBI-DERIVED bar
JAC_PART_BAR = 0.20         # G3: JACOBI-PARTIAL bar
Z_REF = 1.0                 # G3: frozen spectral parameter
ANCHOR_MIN_DH = 5           # G3: conjugation anchor needs dh >= 5
MIN_SMOOTH_STEPS = 10
GAUGES = ("W", "A", "D")
GAUGE_NAMES = {"W": "(i) WRONSKIAN", "A": "(ii) ASYMPTOTIC",
               "D": "(iii) DET-PHASE"}
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


# --------- pipeline, verbatim from moebius_source_step_probe
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


def build_rung(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h,
                uu=uu, mm=mm, M=M)


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


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (SPEC v2 extraction,
    verbatim; sign/order convention fixed, NO rotation applied)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def rung_all(kz, **kw):
    """One heavy build per rung (predecessor verbatim) + Jacobi
    chain storage; generators stored WITHOUT any gauge rotation."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
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
    lamE = float(np.linalg.eigvalsh(E)[-1])
    out = dict(kz=kz, h=h, alpha=b["alpha"], M=b["M"], D=D,
               lamE=lamE, tau=1.0 - lamE, al=al, be=be)
    # ---- window compression (controls' frame channel, verbatim)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    # ---- dressed port + IIKS generators (verbatim, no rotation)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) >= 4 and len(ib) >= 1:
        P = E[np.ix_(ip, ip)]
        X = E[np.ix_(ip, ib)]
        R = E[np.ix_(ib, ib)]
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        Y = np.diag(ys[ip])
        C = Y @ DP - DP @ Y
        f, g, sv = antisym_generators(C)
        out["fS"], out["gS"] = f, g
        out["s1"] = float(sv[0])
        out["jp"], out["yp"] = uf_n[ip], ys[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def norm_map(p0, p1, p2):
    M = np.stack([p2, p0], axis=1)
    if abs(float(np.linalg.det(M))) < 1e-12:
        return None
    T0 = np.linalg.inv(M)
    s, t = T0 @ p1
    if abs(s) < 1e-10 or abs(t) < 1e-10:
        return None
    return np.diag([1.0 / s, 1.0 / t]) @ T0


def apply_hom(T, P):
    Q = (T @ P.T).T
    n = np.linalg.norm(Q, axis=1)
    n[n < 1e-300] = 1.0
    return Q / n[:, None]


def moebius_fit(P, Q):
    rows = np.stack([P[:, 0] * Q[:, 1], P[:, 1] * Q[:, 1],
                     -P[:, 0] * Q[:, 0], -P[:, 1] * Q[:, 0]],
                    axis=1)
    _u, _s, Vh = np.linalg.svd(rows)
    a, b, c, d = Vh[-1]
    T = np.array([[a, b], [c, d]])
    return T, chordal(apply_hom(T, P), Q)


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


def cells_of(uu, alpha):
    """FROZEN Voronoi cells on [0, 2 alpha] + exact rho^0 masses
    (christoffel_pnt_gamma verbatim)."""
    bb = np.concatenate([[0.0], 0.5 * (uu[1:] + uu[:-1]),
                         [2.0 * alpha]])
    m0c = 4.0 * (np.exp(0.5 * bb[1:]) - np.exp(0.5 * bb[:-1]))
    return bb, m0c


# ------------------------------------------- gauge + projective tools
def solve_frame(B, F, G):
    """Unique basis (fN, gN) of span(F, G) with the two linear
    functionals (rows of B) taking values (1,0) / (0,1); None if
    the functional matrix is degenerate."""
    sv = np.linalg.svd(B, compute_uv=False)
    if sv[0] <= 0 or sv[1] / sv[0] <= FRAME_COND:
        return None
    cf = np.linalg.solve(B, np.array([1.0, 0.0]))
    cg = np.linalg.solve(B, np.array([0.0, 1.0]))
    return cf[0] * F + cf[1] * G, cg[0] * F + cg[1] * G


def edge_functionals(r):
    """The two window-edge functionals of gauge (ii): linear
    extrapolation to y = 1 and the leading slope in 1 - y, built
    from the rung's own two deepest port nodes."""
    yp = np.asarray(r["yp"], float)
    o = np.argsort(-yp)
    e0, e1 = int(o[0]), int(o[1])
    y0, y1 = float(yp[e0]), float(yp[e1])
    if abs(y0 - y1) <= 1e-15:
        return None

    def L1(v):
        return v[e0] + (v[e1] - v[e0]) * (1.0 - y0) / (y1 - y0)

    def L2(v):
        return (v[e1] - v[e0]) / (y0 - y1)
    return L1, L2


def gauge_frames(r, refs):
    """The three source-frozen gauges on one rung; each entry is
    (f, g) arrays over the port nodes, or None (typed skip)."""
    out = {"W": None, "A": None, "D": None}
    if "fS" not in r:
        return out
    F, G = r["fS"], r["gS"]
    jp = [int(j) for j in r["jp"]]
    # (i) WRONSKIAN: interpolation frame at the frozen grid pair
    if refs[0] in jp and refs[1] in jp:
        k1, k2 = jp.index(refs[0]), jp.index(refs[1])
        B = np.array([[F[k1], G[k1]], [F[k2], G[k2]]])
        out["W"] = solve_frame(B, F, G)
    # (ii) ASYMPTOTIC: window-edge value/slope frame (own edge)
    Ls = edge_functionals(r)
    if Ls is not None:
        L1, L2 = Ls
        B = np.array([[L1(F), L1(G)], [L2(F), L2(G)]])
        out["A"] = solve_frame(B, F, G)
    # (iii) DET-PHASE: unit SVD basis + frozen rotation/sign
    s1 = r["s1"]
    f3 = F / math.sqrt(s1)
    g3 = G / math.sqrt(s1)
    m0 = int(np.argmin(r["jp"]))
    rr = math.hypot(f3[m0], g3[m0])
    if rr > 1e-300:
        c, s = f3[m0] / rr, g3[m0] / rr
        out["D"] = (c * f3 + s * g3, -s * f3 + c * g3)
    return out


def frame_selftest(rungs, refs):
    """G1.0 (v3 xi): re-verify every gauge frame against its
    defining conditions; returns max deviation per gauge."""
    dev = {g: 0.0 for g in GAUGES}
    for r in rungs:
        fr = gauge_frames(r, refs)
        jp = [int(j) for j in r.get("jp", [])]
        if fr["W"] is not None:
            k1, k2 = jp.index(refs[0]), jp.index(refs[1])
            fN, gN = fr["W"]
            dev["W"] = max(dev["W"], abs(fN[k1] - 1.0),
                           abs(fN[k2]), abs(gN[k1]),
                           abs(gN[k2] - 1.0))
        if fr["A"] is not None:
            L1, L2 = edge_functionals(r)
            fN, gN = fr["A"]
            dev["A"] = max(dev["A"], abs(L1(fN) - 1.0),
                           abs(L2(fN)), abs(L1(gN)),
                           abs(L2(gN) - 1.0))
        if fr["D"] is not None:
            f3, g3 = fr["D"]
            m0 = int(np.argmin(r["jp"]))
            dev["D"] = max(dev["D"],
                           abs(float(np.linalg.norm(f3)) - 1.0),
                           abs(float(np.linalg.norm(g3)) - 1.0),
                           abs(g3[m0]), max(0.0, -f3[m0]))
    return dev


def proj_dist(A, B):
    """Projective (sine) distance between real 2x2 matrices mod
    scale and sign."""
    na = float(np.linalg.norm(A))
    nb = float(np.linalg.norm(B))
    if na < 1e-300 or nb < 1e-300:
        return 1.0
    ipd = float(np.sum(A * B)) / (na * nb)
    return math.sqrt(max(0.0, 1.0 - ipd * ipd))


def conj_joint(As, Bs):
    """ONE global S with B_i ~ S A_i S^{-1} for all i: joint
    least-squares Sylvester solve (stacked nullspace of
    B_i S - S A_i); returns (S, s_min/s_max of the stack)."""
    rows = []
    for A, B in zip(As, Bs):
        L = np.zeros((4, 4))
        for j in range(4):
            E = np.zeros((2, 2))
            E[j // 2, j % 2] = 1.0
            L[:, j] = (B @ E - E @ A).ravel()
        rows.append(L)
    L = np.concatenate(rows, axis=0)
    _u, sv, Vh = np.linalg.svd(L)
    S = Vh[-1].reshape(2, 2)
    return S, float(sv[-1] / max(sv[0], 1e-300))


def conj_apply(S, A):
    dS = float(np.linalg.det(S))
    if abs(dS) < 1e-12 * float(np.linalg.norm(S)) ** 2:
        return None
    return S @ A @ np.linalg.inv(S)


def kappa(M):
    d = float(np.linalg.det(M))
    if abs(d) < 1e-300:
        return float("inf")
    return float(np.trace(M)) ** 2 / d


def pearson(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if len(x) < 3 or float(np.std(x)) < 1e-15 \
            or float(np.std(y)) < 1e-15:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def jacobi_product(al, be, ka, kb, z):
    """prod_{k=ka}^{kb-1} T_k(z), Frobenius-renormalized per
    factor; returns (J, accumulated log norm)."""
    J = np.eye(2)
    lognorm = 0.0
    for k in range(ka, kb):
        Tk = np.array([[(z - al[k]) / be[k], -be[k - 1] / be[k]],
                       [1.0, 0.0]])
        J = Tk @ J
        n = float(np.linalg.norm(J))
        lognorm += math.log(n)
        J /= n
    return J, lognorm


# ------------------------------------------- ladder-level machinery
def build_ladder(comb_of=None, tag="truth"):
    """Build all frame-A rungs; comb_of(kz, uu, alpha) -> comb or
    None for the truth comb."""
    rungs = []
    rk_max = 0.0
    n_incomplete = 0
    for kz in core.frame_a_zones():
        kw = {}
        if comb_of is not None:
            rr0 = core.build_window(kz)
            uu = np.asarray(rr0["uu"], float)
            kw["comb"] = comb_of(uu, rr0["alpha"])
        r = rung_all(kz, **kw)
        if r == "TOO-DEEP":
            continue
        if not isinstance(r, dict):
            n_incomplete += 1
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    [%s] %d rungs (h %d .. %d), %d incomplete chains, "
          "worst rank s3/s1 %.1e   [t %.0f s]"
          % (tag, len(rungs), rungs[0]["h"] if rungs else -1,
             rungs[-1]["h"] if rungs else -1, n_incomplete,
             rk_max, time.time() - T0), flush=True)
    return rungs, rk_max


def ladder_pairs(rungs):
    pairs = []
    n_skip = 0
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        com, ia, ib = np.intersect1d(ra.get("jp", []),
                                     rb.get("jp", []),
                                     return_indices=True)
        if len(com) >= MIN_COMMON_J and "fS" in ra and "fS" in rb:
            pairs.append(dict(ra=ra, rb=rb, com=com, ia=ia, ib=ib))
        else:
            n_skip += 1
    return pairs, n_skip


def jstar_refs(rungs):
    all_jp = [set(int(j) for j in r.get("jp", [])) for r in rungs]
    for fr in JSTAR_FRACS:
        cand = sorted(j for j in set().union(*all_jp)
                      if sum(j in s for s in all_jp)
                      >= fr * len(rungs))
        if len(cand) >= MIN_JSTAR:
            return cand, fr
    return [], None


def pair_spread(P):
    """Median pairwise chordal distance among unit-pair rows (the
    carrier's own contrast on the rung)."""
    n = len(P)
    if n < 2:
        return 0.0
    D = np.abs(P[:, None, 0] * P[None, :, 1]
               - P[:, None, 1] * P[None, :, 0])
    iu = np.triu_indices(n, 1)
    return float(np.median(D[iu]))


def measure_gauges(rungs, pairs, refs):
    """Per gauge: raw deviations + carrier spread + anchor step
    maps per pair."""
    frames = [gauge_frames(r, refs) for r in rungs]
    idx_of = {id(r): i for i, r in enumerate(rungs)}
    out = {g: {} for g in GAUGES}
    anchors = refs[:3]
    for si, p in enumerate(pairs):
        ra, rb = p["ra"], p["rb"]
        fa_all = frames[idx_of[id(ra)]]
        fb_all = frames[idx_of[id(rb)]]
        jpa = [int(j) for j in ra["jp"]]
        jpb = [int(j) for j in rb["jp"]]
        nref = np.array([int(j) not in refs[:2] for j in p["com"]])
        for g in GAUGES:
            if fa_all[g] is None or fb_all[g] is None:
                continue
            fa, ga = fa_all[g]
            fb, gb = fb_all[g]
            Pa = unit_pairs(ga[p["ia"]], fa[p["ia"]])
            Pb = unit_pairs(gb[p["ib"]], fb[p["ib"]])
            raw = float(np.median(chordal(Pa, Pb)))
            spr = pair_spread(Pa[nref]) if int(np.sum(nref)) >= 2 \
                else 0.0
            rec = dict(raw=raw, spr=spr, M=None, kap=float("nan"),
                       fa=fa, fb=fb)
            if all(j in jpa and j in jpb for j in anchors):
                PA = unit_pairs(ga, fa)
                PB = unit_pairs(gb, fb)
                qa = [PA[jpa.index(j)] for j in anchors]
                qb = [PB[jpb.index(j)] for j in anchors]
                seps = [chordal(x[None, :], y[None, :])[0]
                        for xy in (qa, qb)
                        for x, y in ((xy[0], xy[1]),
                                     (xy[0], xy[2]),
                                     (xy[1], xy[2]))]
                Ta = norm_map(*qa)
                Tb = norm_map(*qb)
                if (min(seps) > REF_SEP_MIN and Ta is not None
                        and Tb is not None):
                    M = np.linalg.inv(Tb) @ Ta
                    rec["M"] = M / max(float(np.linalg.norm(M)),
                                       1e-300)
                    rec["kap"] = kappa(M)
            out[g][si] = rec
    return out


def family_dp(As, Bs, S):
    """Median d_P(S A S^-1, B) over the two matched families;
    inf if S is singular."""
    ds = []
    for A, B in zip(As, Bs):
        AC = conj_apply(S, A)
        if AC is None:
            return float("inf")
        ds.append(proj_dist(AC, B))
    return float(np.median(ds)) if ds else float("inf")


def robust_conj_score(As, Bs):
    """Score the agreement of two step families up to ONE global
    conjugation: the better of S = Id and the joint least-squares
    Sylvester solve (SPEC v3 amendment viii).  Returns (best med,
    med at Id, med at joint S, s_min/s_max, n)."""
    if len(As) < 2:
        return (float("inf"), float("inf"), float("inf"),
                float("nan"), len(As))
    d_id = family_dp(As, Bs, np.eye(2))
    S, smin = conj_joint(As, Bs)
    d_jt = family_dp(As, Bs, S)
    return min(d_id, d_jt), d_id, d_jt, smin, len(As)


def cross_gauge(meas, ga, gb):
    """Cross-gauge step-family comparison up to ONE global
    conjugation (robust, v3)."""
    common = sorted(si for si in meas[ga]
                    if si in meas[gb]
                    and meas[ga][si]["M"] is not None
                    and meas[gb][si]["M"] is not None)
    As = [meas[ga][si]["M"] for si in common]
    Bs = [meas[gb][si]["M"] for si in common]
    return robust_conj_score(As, Bs)


def lambda_ladder(meas_g, pairs, refs):
    """G2: gauge-(i) scalar cocycle over the measured steps."""
    rows = []
    for si, p in enumerate(pairs):
        if si not in meas_g:
            continue
        rec = meas_g[si]
        fa, fb = rec["fa"], rec["fb"]
        com = p["com"]
        keep = np.array([int(j) not in refs[:2] for j in com])
        va = np.abs(fa[p["ia"]][keep])
        vb = np.abs(fb[p["ib"]][keep])
        m = va > 1e-300
        if int(np.sum(m)) < 3:
            continue
        lam = float(np.median(vb[m] / va[m]))
        if lam <= 0:
            continue
        rows.append(dict(si=si, ha=p["ra"]["h"], hb=p["rb"]["h"],
                         lam=lam, tau_b=p["rb"]["tau"]))
    cum = 0.0
    for r in rows:
        cum += math.log(r["lam"])
        r["cum"] = cum
    return rows


def jacobi_family(pairs, z):
    """G3: entering-level transfer products from the deeper rung's
    chain; equal-h steps carry the empty product."""
    fam = {}
    for si, p in enumerate(pairs):
        ha, hb = p["ra"]["h"], p["rb"]["h"]
        if hb < ha:
            continue
        al, be = p["rb"]["al"], p["rb"]["be"]
        if hb > ha and (len(al) < hb or len(be) < hb or ha < 1):
            continue
        J, lognorm = jacobi_product(al, be, ha, hb, z) \
            if hb > ha else (np.eye(2), 0.0)
        fam[si] = dict(J=J / max(float(np.linalg.norm(J)), 1e-300),
                       lognorm=lognorm, dh=hb - ha)
    return fam


def jacobi_score(fam, meas_g, tag):
    """Global-conjugation scoring of the Jacobi candidate against
    the gauge-(i) measured steps (robust, v3)."""
    common = sorted(si for si in fam
                    if si in meas_g and meas_g[si]["M"] is not None)
    if len(common) < 2:
        print("    [%s] JACOBI: < 2 comparable steps -> "
              "UNAVAILABLE" % tag)
        return None
    As = [fam[si]["J"] for si in common]
    Bs = [meas_g[si]["M"] for si in common]
    med, d_id, d_jt, smin, n = robust_conj_score(As, Bs)
    kj = [kappa(fam[si]["J"]) for si in common]
    km = [meas_g[si]["kap"] for si in common]
    n_dh0 = sum(1 for si in common if fam[si]["dh"] == 0)
    print("    [%s] JACOBI: %d steps (%d with dh=0); global "
          "conjugation candidates: d_P med %.4f at S=Id, %.4f at "
          "joint-LSQ S (stack s_min/s_max %.1e)"
          % (tag, n, n_dh0, d_id, d_jt, smin))
    print("    [%s] SCORED median d_P = %.4f (better candidate); "
          "median d_P(J, Id) = %.4f; kappa corr(J, M) = %.3f"
          % (tag, med,
             family_dp(As, [np.eye(2)] * len(As), np.eye(2)),
             pearson(kj, km)))
    return dict(med=med, common=common)


# ------------------------------------------------------------------ main
def main():
    section("PRIME.PORT.MOEBIUS.GAUGEFW.01 -- source-frozen gauge "
            "firewall + scalar cocycle + Jacobi transfer "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth ladder (all frame-A zones, "
            "h <= %d; machinery verbatim)" % H_DEEP_MAX)
    rungs, rk_max = build_ladder(tag="truth")
    check("W1 >= %d rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= %.0e)"
          % (rk_max, RANK_BAR), rk_max <= RANK_BAR, kill="K1")
    jstar, used_frac = jstar_refs(rungs)
    check("W3 frozen reference set built (|J*| %d >= %d at "
          "presence >= %.2f)" % (len(jstar), MIN_JSTAR,
                                 used_frac or 0.0),
          len(jstar) >= MIN_JSTAR, kill="K1")
    if len(jstar) < MIN_JSTAR:
        return finish({})
    refs = jstar[:3]
    print("    J* = %s; reference pair (jr1, jr2) = (%d, %d); "
          "step anchors = %s" % (jstar, jstar[0], jstar[1], refs))
    pairs, n_skip_pairs = ladder_pairs(rungs)
    print("    %d consecutive pairs with >= %d common port nodes "
          "(%d typed skips)" % (len(pairs), MIN_COMMON_J,
                                n_skip_pairs))

    # ------------------------------------------------------------ G0
    section("G0 -- baseline: the per-rung-normalized machinery the "
            "reviewer challenged (verbatim; printed, not a claim)")
    fit_res, id_res = [], []
    for p in pairs:
        Pa = unit_pairs(p["ra"]["gS"][p["ia"]],
                        p["ra"]["fS"][p["ia"]])
        Pb = unit_pairs(p["rb"]["gS"][p["ib"]],
                        p["rb"]["fS"][p["ib"]])
        order = np.argsort(p["com"])
        i0, i1, i2 = order[0], order[1], order[2]
        seps = [chordal(Pa[[u]], Pa[[v]])[0]
                for u, v in ((i0, i1), (i0, i2), (i1, i2))] \
            + [chordal(Pb[[u]], Pb[[v]])[0]
               for u, v in ((i0, i1), (i0, i2), (i1, i2))]
        Ta = norm_map(Pa[i0], Pa[i1], Pa[i2])
        Tb = norm_map(Pb[i0], Pb[i1], Pb[i2])
        if min(seps) <= REF_SEP_MIN or Ta is None or Tb is None:
            continue
        Na, Nb = apply_hom(Ta, Pa), apply_hom(Tb, Pb)
        T, res = moebius_fit(Na, Nb)
        keep = np.ones(len(p["com"]), dtype=bool)
        keep[[i0, i1, i2]] = False
        fit_res.append(float(np.median(res[keep])))
        id_res.append(float(np.median(
            chordal(Na, Nb)[keep])))
    med_fit = float(np.median(fit_res)) if fit_res else float("inf")
    med_idn = float(np.median(id_res)) if id_res else float("inf")
    norm_invariant = med_idn <= RAW_INV_BAR
    print("    %d normalized steps; med fit res %.4f; med id-res "
          "(identity candidate) %.4f -> baseline %s"
          % (len(fit_res), med_fit, med_idn,
             "NORM-INVARIANT" if norm_invariant else "NORM-MOVING"))
    check("G0.1 baseline computed (%d steps)" % len(fit_res),
          len(fit_res) >= MIN_PAIRS, kill="K1")

    # ------------------------------------------------------------ G1
    section("G1 -- the three SOURCE-FROZEN gauges (raw chordal "
            "deviation, NO renormalization; anchor step maps)")
    st_dev = frame_selftest(rungs, refs)
    check("G1.0 FRAME SELF-TEST: all gauge frames satisfy their "
          "defining conditions (max dev W %.1e / A %.1e / D %.1e "
          "<= 1e-8)" % (st_dev["W"], st_dev["A"], st_dev["D"]),
          max(st_dev.values()) <= 1e-8, kill="K1")
    meas = measure_gauges(rungs, pairs, refs)
    print("    step          raw/spread (i)W    raw/spread (ii)A"
          "   raw/spread (iii)D    kap(W)     kap(A)     kap(D)")
    for si, p in enumerate(pairs):
        cols = []
        kaps = []
        for g in GAUGES:
            if si in meas[g]:
                cols.append("%.4f/%.4f" % (meas[g][si]["raw"],
                                           meas[g][si]["spr"]))
                kaps.append(("%+.3e" % meas[g][si]["kap"])
                            if meas[g][si]["M"] is not None
                            else "    -    ")
            else:
                cols.append("  -   /  -   ")
                kaps.append("    -    ")
        print("    h %3d->%3d   %s      %s      %s   %s %s %s"
              % (p["ra"]["h"], p["rb"]["h"], cols[0], cols[1],
                 cols[2], kaps[0], kaps[1], kaps[2]))
    raw_label = {}
    for g in GAUGES:
        rv = [meas[g][si]["raw"] for si in meas[g]]
        sv = [meas[g][si]["spr"] for si in meas[g]]
        med = float(np.median(rv)) if rv else float("inf")
        med_s = float(np.median(sv)) if sv else 0.0
        if med_s < RAW_INV_BAR:
            raw_label[g] = "RAW-DEGENERATE"
        elif med <= RAW_INV_BAR:
            raw_label[g] = "RAW-INVARIANT"
        else:
            raw_label[g] = "RAW-MOVING"
        nM = sum(1 for si in meas[g]
                 if meas[g][si]["M"] is not None)
        d_id = [proj_dist(meas[g][si]["M"], np.eye(2))
                for si in meas[g]
                if meas[g][si]["M"] is not None]
        print("    %-16s: %d steps (%d anchor maps), raw dev %s | "
              "med spread %.4f (rel motion %s) | med d_P(M, Id) "
              "%.4f -> %s"
              % (GAUGE_NAMES[g], len(rv), nM,
                 quart(rv) if rv else "none", med_s,
                 "%.2f" % (med / med_s) if med_s > 0 else "n/a",
                 float(np.median(d_id)) if d_id else float("nan"),
                 raw_label[g]))
    nW = sum(1 for si in meas["W"]
             if meas["W"][si]["M"] is not None)
    check("G1.1 >= %d gauge-(i) steps with anchor maps" % MIN_PAIRS,
          nW >= MIN_PAIRS, "%d steps" % nW, kill="K1")
    print("\n    CROSS-GAUGE (ONE global conjugation, robust v3: "
          "better of S=Id and joint-LSQ S):")
    cross = {}
    for ga, gb in (("W", "A"), ("W", "D"), ("A", "D")):
        med, d_id, d_jt, smin, n = cross_gauge(meas, ga, gb)
        cross[(ga, gb)] = med
        print("    %s vs %s : SCORED med d_P %.4f over %d steps "
              "(S=Id %.4f | joint-LSQ %.4f, stack s_min/s_max "
              "%.1e)" % (ga, gb, med, n, d_id, d_jt, smin))
    all_pairs_ok = all(v <= DP_ROBUST_BAR for v in cross.values())
    any_pair_part = all(v <= DP_PART_BAR for v in cross.values())
    nondeg = [g for g in GAUGES
              if raw_label[g] != "RAW-DEGENERATE"]
    labels_agree = len(set(raw_label[g] for g in nondeg)) <= 1
    if all_pairs_ok and labels_agree:
        g1_label = "GAUGE-ROBUST"
    elif (norm_invariant
          and not any(raw_label[g] == "RAW-INVARIANT"
                      for g in GAUGES)
          and not any_pair_part):
        g1_label = "GAUGE-MADE"
    else:
        g1_label = "GAUGE-PARTIAL"
    sub = ",".join("%s:%s" % (g, raw_label[g][4:]) for g in GAUGES)
    print("    TYPED: cross-gauge medians %s vs bars %.2f/%.2f; "
          "raw labels {%s}; baseline %s -> %s"
          % (["%.4f" % cross[k] for k in cross],
             DP_ROBUST_BAR, DP_PART_BAR, sub,
             "NORM-INVARIANT" if norm_invariant else "NORM-MOVING",
             g1_label))
    check("G1.2 typed: %s (%s)" % (g1_label, sub), True)

    # ------------------------------------------------------------ G2
    section("G2 -- the scalar cocycle lambda_h (gauge (i) frozen) "
            "vs the tau ladder")
    rows = lambda_ladder(meas["W"], pairs, refs)
    print("    step          lambda_h   cum log lambda   tau_b"
          "        log tau_b")
    for r in rows:
        lt = math.log(r["tau_b"]) if r["tau_b"] > 0 else float("nan")
        print("    h %3d->%3d   %9.4f   %+12.4f    %+.3e   %s"
              % (r["ha"], r["hb"], r["lam"], r["cum"], r["tau_b"],
                 "%+9.4f" % lt if lt == lt else "   n/a  "))
    ok_rows = [r for r in rows if r["tau_b"] > 0]
    cum_v = [r["cum"] for r in ok_rows]
    ltau_v = [math.log(r["tau_b"]) for r in ok_rows]
    corr = pearson(cum_v, ltau_v)
    slope = (float(np.polyfit(ltau_v, cum_v, 1)[0])
             if len(ok_rows) >= 3 else float("nan"))
    g2_label = ("LAMBDA-IS-WALL" if abs(corr) >= LAM_WALL_CORR
                else "LAMBDA-PARTIAL" if abs(corr) >= LAM_PART_CORR
                else "LAMBDA-FLAT") if corr == corr else \
        "LAMBDA-FLAT"
    check("G2.1 lambda ladder measured (%d steps, %d with tau > 0)"
          % (len(rows), len(ok_rows)), len(ok_rows) >= 3,
          kill="K1")
    print("    corr(cumsum log lambda, log tau) = %.4f; OLS slope "
          "d(cum log lambda)/d(log tau) = %.4f" % (corr, slope))
    print("    TYPED: |corr| %.4f vs bars %.2f / %.2f -> %s"
          % (abs(corr) if corr == corr else float("nan"),
             LAM_WALL_CORR, LAM_PART_CORR, g2_label))
    for g in ("A", "D"):
        rg = lambda_ladder(meas[g], pairs, refs)
        og = [r for r in rg if r["tau_b"] > 0]
        cg = pearson([r["cum"] for r in og],
                     [math.log(r["tau_b"]) for r in og])
        print("    (unscored) gauge %s: corr = %s over %d steps"
              % (g, "%.4f" % cg if cg == cg else "n/a", len(og)))
    s1r = [(math.log(r["s1"]), math.log(r["tau"]))
           for r in rungs if "s1" in r and r["tau"] > 0]
    print("    (unscored, v3 x) extraction-scale ladder: corr(log "
          "s1, log tau) = %s over %d rungs"
          % ("%.4f" % pearson([a for a, _ in s1r],
                              [b for _, b in s1r])
             if len(s1r) >= 3 else "n/a", len(s1r)))
    check("G2.2 typed: %s" % g2_label, True)

    # ------------------------------------------------------------ G3
    section("G3 -- Jacobi transfer identification at z_ref = %.1f "
            "(cd_pick chain convention frozen)" % Z_REF)
    fam = jacobi_family(pairs, Z_REF)
    print("    step          dh   log|prod|   kap(J)      "
          "kap(M gauge i)")
    for si in sorted(fam):
        if si not in meas["W"] or meas["W"][si]["M"] is None:
            continue
        print("    h %3d->%3d  %4d   %+8.3f   %+.3e   %+.3e"
              % (pairs[si]["ra"]["h"], pairs[si]["rb"]["h"],
                 fam[si]["dh"], fam[si]["lognorm"],
                 kappa(fam[si]["J"]), meas["W"][si]["kap"]))
    jsc = jacobi_score(fam, meas["W"], "truth")
    if jsc is None:
        g3_label = "JACOBI-UNAVAILABLE"
    else:
        g3_label = ("JACOBI-DERIVED" if jsc["med"] <= JAC_DER_BAR
                    else "JACOBI-PARTIAL"
                    if jsc["med"] <= JAC_PART_BAR
                    else "JACOBI-DEAD")
    # G2/G3 bridge: does the scalar cocycle track the transfer
    # growth? (unscored diagnostic)
    lam_of = {r["si"]: math.log(r["lam"]) for r in rows}
    xs_b, ys_b = [], []
    for si in fam:
        if fam[si]["dh"] > 0 and si in lam_of:
            xs_b.append(lam_of[si])
            ys_b.append(fam[si]["lognorm"])
    print("    (unscored bridge) corr(log lambda_h, log transfer "
          "growth) = %s over %d steps"
          % ("%.4f" % pearson(xs_b, ys_b)
             if len(xs_b) >= 3 else "n/a", len(xs_b)))
    print("    TYPED: %s (med d_P %s vs bars %.2f / %.2f)"
          % (g3_label,
             "%.4f" % jsc["med"] if jsc else "n/a",
             JAC_DER_BAR, JAC_PART_BAR))
    check("G3.1 typed: %s" % g3_label, True)

    # ------------------------------------------------------------ SM
    section("SM -- the SMOOTH-MASS world (mask actual, mass smooth;"
            " frame-surviving control, same frozen gauges)")
    sm_rungs, _sm_rk = build_ladder(
        comb_of=lambda uu, alpha: (uu, cells_of(uu, alpha)[1]),
        tag="smooth")
    sm_stats = dict(g1=None, g2=None, g3=None, alive=None)
    if sm_rungs:
        alive = [r for r in sm_rungs if r["lamE"] < 1.0]
        sm_stats["alive"] = (len(alive), len(sm_rungs))
        sm_frame_dead = len(alive) == 0
        print("    frame survival census: lam(E) < 1 on %d / %d "
              "smooth rungs (min tau %+.3e, max %+.3e)%s"
              % (len(alive), len(sm_rungs),
                 min(r["tau"] for r in sm_rungs),
                 max(r["tau"] for r in sm_rungs),
                 "  -> typed SMOOTH-FRAME-DEAD (v3 ix): the "
                 "smooth-mass world is NOT frame-surviving here; "
                 "its measurements below carry that caveat"
                 if sm_frame_dead else ""))
        sm_pairs, sm_skip = ladder_pairs(sm_rungs)
        print("    %d smooth pairs (%d typed skips)"
              % (len(sm_pairs), sm_skip))
        if len(sm_pairs) >= MIN_SMOOTH_STEPS:
            sm_meas = measure_gauges(sm_rungs, sm_pairs, refs)
            for g in GAUGES:
                rv = [sm_meas[g][si]["raw"] for si in sm_meas[g]]
                sv = [sm_meas[g][si]["spr"] for si in sm_meas[g]]
                print("    smooth %-16s: %d steps, raw dev %s | "
                      "med spread %.4f"
                      % (GAUGE_NAMES[g], len(rv),
                         quart(rv) if rv else "none",
                         float(np.median(sv)) if sv else 0.0))
            rvW = [sm_meas["W"][si]["raw"] for si in sm_meas["W"]]
            sm_stats["g1"] = (float(np.median(rvW))
                              if rvW else float("inf"))
            sm_rows = lambda_ladder(sm_meas["W"], sm_pairs, refs)
            sm_ok = [r for r in sm_rows if r["tau_b"] != 0]
            sm_corr = pearson([r["cum"] for r in sm_ok],
                              [math.log(abs(r["tau_b"]))
                               for r in sm_ok])
            sm_stats["g2"] = sm_corr
            print("    smooth G2: corr(cum log lambda, log|tau|) "
                  "= %s over %d steps (tau < 0 throughout when "
                  "frame dead, disclosed)"
                  % ("%.4f" % sm_corr if sm_corr == sm_corr
                     else "n/a", len(sm_ok)))
            sm_fam = jacobi_family(sm_pairs, Z_REF)
            sm_jsc = jacobi_score(sm_fam, sm_meas["W"], "smooth")
            if sm_jsc is not None:
                sm_stats["g3"] = sm_jsc["med"]
        else:
            print("    typed: SMOOTH-UNAVAILABLE (%d < %d steps)"
                  % (len(sm_pairs), MIN_SMOOTH_STEPS))
    else:
        print("    typed: SMOOTH-UNAVAILABLE (no rungs)")
    caveat = ""
    if g3_label == "JACOBI-DERIVED":
        if sm_stats["g3"] is not None \
                and sm_stats["g3"] <= JAC_DER_BAR:
            caveat = "+UNIVERSAL-KINEMATICS"
            print("    HONEST CAVEAT: the identification holds on "
                  "the SMOOTH-MASS world too -> generic OPRL "
                  "kinematics; the arithmetic sits in the scalar "
                  "cocycle / the measure itself.")
        elif sm_stats["g3"] is not None:
            print("    caveat test: smooth med d_P %.4f > %.2f -> "
                  "the identification is NOT generic OPRL "
                  "kinematics on this evidence."
                  % (sm_stats["g3"], JAC_DER_BAR))
        else:
            print("    caveat test: smooth world unavailable -- "
                  "generic-kinematics question left open (typed).")
    check("SM.1 smooth-mass control measured (alive %s, G1 med %s,"
          " G2 corr %s, G3 med %s)"
          % (sm_stats["alive"],
             "%.4f" % sm_stats["g1"]
             if sm_stats["g1"] is not None else "n/a",
             "%.4f" % sm_stats["g2"]
             if sm_stats["g2"] == sm_stats["g2"]
             and sm_stats["g2"] is not None else "n/a",
             "%.4f" % sm_stats["g3"]
             if sm_stats["g3"] is not None else "n/a"), True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz %d, must fire; frame channels "
            "reported)" % CTRL_KZ)
    ok = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        rc = rung_all(CTRL_KZ, **kw)
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> fires via "
                  "FRAME" % (nmc, rc))
            continue
        frame_dead = ("lamC" not in rc or rc["lamO"] > 1.0
                      or rc["lamC"] > 1.0)
        if frame_dead:
            why = ("window unavailable" if "lamC" not in rc else
                   "lam(out) %.3e" % rc["lamO"]
                   if rc["lamO"] > 1.0 else
                   "lam(C_J) %.3e" % rc["lamC"])
            print("    %-8s: fires via FRAME (%s)" % (nmc, why))
            continue
        if "fS" not in rc:
            print("    %-8s: frame alive but extraction "
                  "unavailable -> fires via FRAME" % nmc)
            continue
        print("    %-8s: frame ALIVE and extraction available -> "
              "SILENT" % nmc)
        ok = False
    check("C1 CONTROLS FIRE (frame death on both controls; the "
          "smooth-mass world is the frame-surviving control)",
          ok, kill="K3")

    return finish(dict(g1=g1_label, sub=sub, g2=g2_label,
                       corr=corr, slope=slope, g3=g3_label,
                       caveat=caveat, cross=cross,
                       med_fit=med_fit, med_idn=med_idn,
                       jmed=(jsc["med"] if jsc else float("inf")),
                       sm=sm_stats))


def finish(st):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("GAUGEFW-MEASURED / %s (%s) / %s / %s%s"
                   % (st["g1"], st["sub"], st["g2"], st["g3"],
                      st["caveat"]))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (baseline med id-res %.4f; cross-gauge d_P %s; "
              "lambda-tau corr %.4f slope %.4f; jacobi med d_P "
              "%s; smooth: %r)"
              % (st["med_idn"],
                 ["%.4f" % st["cross"][k] for k in st["cross"]],
                 st["corr"], st["slope"],
                 "%.4f" % st["jmed"]
                 if st["jmed"] < float("inf") else "n/a",
                 st["sm"]))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
