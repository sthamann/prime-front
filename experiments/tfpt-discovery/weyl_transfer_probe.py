#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weyl_transfer_probe -- PRIME.PORT.WEYLTRANSFER.01
(EXPLORATION ONLY, experiments/; round 57: does the ladder step
act on a scalar Weyl-type parameter as a 2x2 transfer / Moebius
map whose half-plane (or interval) invariance IS the wall
positivity -- the reviewer's 'final proof mechanism, not just a
representation'.  2026-08-09.)

THE QUESTION (frozen).  Round 55 (christoffel_ratio_probe,
PRIME.PORT.CHRISTOFFEL.RATIO.01) made the soft flag EXACT:
1/d_12 = 1 + v_* K_sigma(y_*) (warded), c = d_12/tau with c'/c
SENS [0.223, 5.258], r_12 = (tau'/tau)(c'/c) exact at 2.1e-16.
Round ~45 (port_schur_cocycle_probe, PRIME.PORT.SCHURSTEP.01)
measured a single Moebius map per rung on the port carrier
FUNCTION m = g/f (MOEBIUS-STEP).  Round 44 (port_sflow_toda,
PRIME.PORT.SFLOW.01) put the wall margin at the pole distance of
a pole-free s-corridor.  The reviewer's synthesis: if ONE SCALAR
Weyl parameter is transported rung-to-rung by a 2x2 transfer
matrix T_h whose invariant half-plane / interval IS the positive
cone, then wall positivity becomes the invariance statement of a
transfer dynamics -- a proof MECHANISM, not a representation.

THE TWO CANDIDATES (W1; both frozen before the run):
 m_h   (PORT) := the port carrier scalar of the cocycle probe,
       evaluated at the frozen PORT SEAT alias j* = 24 (the
       window soft coordinate, = JWIN[-1], the SAME node that
       carries the christoffel mass): per rung the gauge-fixed
       IIKS generators (f, g) of the dressed port D_P
       (port_riemann_hilbert_setup SPEC v2 extraction, pipeline
       VERBATIM from port_schur_cocycle_probe / lax2_flow_probe;
       SO(2) gauge pinned at the deepest port node), and
       m_h := g(j*)/f(j*) as a homogeneous RP^1 pair
       (g, f).  Typed skips: seat absent from the port, seat ==
       the gauge node (value pinned 0), |f| <= POLE_GUARD x
       |(f, g)| (affine chart pole; the PAIR is still used where
       only projective data is needed).
 m^C_h (CHR)  := v_* K_sigma(y_*) = 1/d_12 - 1 >= 0 on the PD
       ladder (christoffel_ratio identification (iii) VERBATIM,
       warded per rung by the deflation chain W-D below).

FROZEN PROTOCOL (all consecutive full-window rungs of the truth
ladder, frame-A zones, h <= H_DEEP_MAX = 900; machinery verbatim
from christoffel_ratio_probe + port_schur_cocycle_probe):

 W1  THE FIT-FREE MOEBIUS TEST, per candidate.  The 2x2 transfer
     family is the Weyl/Jacobi coefficient-stripping normal form
         m' = 1/(A - B m)   <=>   T = [[0, 1], [-B, A]]
     (2 real dof; the classical m-function transfer of a Jacobi
     step -- 'a 2x2 transfer whose Herglotz sign is one sign').
     On every sliding QUADRUPLE of ADJACENT truth rungs (all
     four full-window, candidate values live): the two pairs
     (m_1 -> m_2), (m_2 -> m_3) SOLVE (A, B) exactly (2x2
     linear system; degenerate solves = typed skips), and the
     third pair m_3 -> m_4 is PREDICTED out of sample:
         err := chordal RP^1 distance between (1, A - B m_3)
                and the actual pair at rung 4
     (pole-safe, scale-free, in [0, 1]).  Print the full ladder
     of errors.  NULL (the decisive comparison): the same solve+
     predict on the candidate ladder PERMUTED by
     rng(NULL_SEED = 2) (mismatched rung triples) -- both error
     distributions printed.  TYPED per candidate:
       MOEBIUS-LAWFUL   iff med err < MOEB_LAWFUL_BAR = 1e-3
                        AND null med >= NULL_FAC = 10 x med
       MOEBIUS-DRIFTING iff med err <= DRIFT_FAC = 0.1 x null
                        med (trend printed: OLS slope of
                        log10 err vs log h_4)
       MOEBIUS-DEAD     otherwise; a LAWFUL/DRIFTING candidate
                        whose null does NOT separate (null med
                        < 10 x med) is downgraded to
                        MOEBIUS-DEAD(NULL-INDISTINCT) -- typed,
                        honest, no kill.
     SECONDARY (unscored, printed): the full 3-dof Moebius
     solved exactly from THREE pairs on sliding QUINTUPLES
     (nullspace of the 3x4 incidence rows), fourth pair
     predicted -- separates 'wrong 2-parameter family' from
     'no Moebius law at all'.

 W2  THE TRANSFER GEOMETRY, per quadruple of W1 (printed for
     both candidates, TYPED on the primary candidate = the
     lawful/lower-median one, default CHR): T_h = [[0, 1],
     [-B, A]] normalized by sqrt(|B|) to det = sign(B); print
     det sign, trace A/sqrt(|B|), the fixed points (roots of
     B m^2 - A m + 1; 'cplx' when A^2 < 4B), and the TWO
     invariance censuses:
       UHP  (Herglotz):  T maps the upper half-plane into
             itself iff det > 0 iff B > 0;
       INT  (Stieltjes): T maps [0, inf] into itself iff
             A > 0 and B <= 0 (then A - B m >= A > 0 on m >= 0
             and the image is (0, 1/A] u {0}).
     (The two are mutually exclusive for this family -- which
     sign structure the ladder chooses is the measurement.)
     TYPED on SENS quadruples (no rung == kz 21):
     HERGLOTZ-INVARIANT(UHP) iff all steps UHP;
     HERGLOTZ-INVARIANT(INT) iff all steps INT;
     HERGLOTZ-BROKEN(counts, first offender) otherwise.

 W3  THE MARGIN AS BOUNDARY DISTANCE + THE C-RATIO
     IDENTIFICATION (typed on the primary candidate, printed
     for both).  (a) boundary distance: dist_h := chordal RP^1
     distance of m_h to the NEAREST invariant-interval endpoint
     {0, inf} = min(|m|, 1)/sqrt(1 + m^2); print
     corr(log dist, log tau_12) (and corr vs log tau_full),
     and the ratio ladder dist/tau_12 with quartiles.  TYPED:
     MARGIN-IS-DISTANCE iff corr >= MARGIN_CORR_BAR = 0.9 on
     the SENS rungs, else MARGIN-DECOUPLED(corr).  (b) c-ratio:
     per quadruple the Moebius derivative
         dT/dm |_{m_3} = (ad - bc)/(c m_3 + d)^2
                       = B/(A - B m_3)^2
     against the MEASURED c'/c across the predicted step
     (c_4/c_3, c = d_12/tau_12); rel errors printed (signed
     comparison, no absolute-value rescue).  TYPED:
     CRATIO-IS-DERIVATIVE iff med rel < CRATIO_BAR = 1e-2 on
     SENS quadruples, else CRATIO-FREE(med).

 C   CONTROLS (kill -> WARD-BROKEN if silent):
     C-S  smooth world (B1 LATTICE-SMOOTH masses m_n =
          2 e^{u_n/2} du_n on the true lattice, verbatim): the
          PD premise must die -- REPRODUCTION: 28 smooth
          full-window pairs with base tau_12 <= 0 on 28/28 AND
          sigma indefinite (tau_full < 0) on >= 1 rung (m^C
          loses its Christoffel meaning; census + first h
          printed).
     C-E  scramble (seed 1) at kz 9: frame death OR neg(A) > 0
          OR tau_12 <= 0; channel printed.
     (The W1 shuffled-triple null is typed inside W1 -- its
     failure downgrades the candidate, it does not kill the
     probe; frozen above.)

 W   PIPELINE + REPRODUCTION WARDS:
     W0   (kill KP) truth ladder == 42 rungs; W0c full-window
          census == 37; W0p >= MIN_PORT_RUNGS = 30 rungs carry
          the port block; W0r [Y, D_P] rank-2 exact on every
          port rung (max s3/s1 <= RANK_BAR = 1e-10); W0q >=
          MIN_QUADS = 15 CHR quadruples and >= MIN_QUADS_PORT =
          10 PORT quadruples.
     W-D  (kill KW) deflation chain 1/d_12 == 1 + m^C per full
          rung, rel <= max(CHR_WARD_FLOOR = 1e-8,
          CHR_COND_FAC = 1e3 x eps/tau_full) (round-55 W-C1c
          verbatim); leading-minor signs +1; tau_12 > 0 and
          c >= 1 on every full rung.
     W-R  (kill KW) REPRODUCTION of the round-55 printed
          ledger: consecutive full-window pair census == 31,
          r_12 > 0 on all pairs, SENS pair census == 29, and
          c'/c SENS min/max == [0.223, 5.258] within rtol 2e-2.

KILLS: KP a W0 ward breaks -> PIPELINE-BROKEN; KW W-D/W-R
breaks OR a control stays silent -> WARD-BROKEN.  Typed labels
(W1/W2/W3) report, never kill.

VERDICT (frozen enum): WEYLTRANSFER-MEASURED with typed
sublabels W1 PORT: MOEBIUS-LAWFUL / MOEBIUS-DRIFTING /
MOEBIUS-DEAD and W1 CHR: (same enum), W2 HERGLOTZ-INVARIANT
(UHP|INT) / HERGLOTZ-BROKEN, W3 MARGIN-IS-DISTANCE /
MARGIN-DECOUPLED and CRATIO-IS-DERIVATIVE / CRATIO-FREE; else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2,4,...,24); NW = 12;
PORT_SEAT_J = 24; N_RUNGS_EXP = 42; N_FULLWIN_FROZEN = 37;
REF_N_TRUTH_PAIRS = 31; REF_N_SENS_PAIRS = 29;
REF_N_SMOOTH_PAIRS = 28; KZ_STAR = 21; REF_CRAT_MIN = 0.223;
REF_CRAT_MAX = 5.258; REF_CRAT_RTOL = 2e-2; CHR_WARD_FLOOR =
1e-8; CHR_COND_FAC = 1e3; CGE1_WARD = 1e-9; RANK_BAR = 1e-10;
MIN_PORT_RUNGS = 30; MIN_QUADS = 15; MIN_QUADS_PORT = 10;
SOLVE_DEGEN = 1e-12; POLE_GUARD = 1e-12; MOEB_LAWFUL_BAR =
1e-3; NULL_FAC = 10; DRIFT_FAC = 0.1; NULL_SEED = 2;
MARGIN_CORR_BAR = 0.9; CRATIO_BAR = 1e-2; CTRL_KZ = 9;
scramble seed 1; EPS = 2.220446049250313e-16.

SPEC v1 (2026-08-09, frozen + SHA-hashed before the first run):
everything above.  Mechanical concretizations frozen with v1:
(i) 'three consecutive rungs, solve from two pairs, predict the
third' is realized on sliding QUADRUPLES of adjacent truth
rungs: two pairs solve the 2-dof Weyl family exactly, the third
pair is the out-of-sample prediction (a general 3-dof Moebius
map is NOT solvable from two pairs; the general family is the
unscored quintuple diagnostic); (ii) all prediction errors are
chordal RP^1 distances (pole-safe; the LAWFUL bar 1e-3 applies
to the chordal median); (iii) SENS = quadruples/rungs not
touching kz 21 (round-53 COORDINATE-ARTIFACT rule; raw always
printed first); (iv) the primary candidate for the W2/W3 typed
labels is the W1-lawful one (lower median if both, CHR if
neither); (v) window/deflation machinery verbatim from
christoffel_ratio_probe (memoized build_window, ONE Gram E per
rung, big Schur solve, slogdet routes); port machinery verbatim
from port_schur_cocycle_probe (fused single heavy build);
smooth/control rungs run LIGHT (no port block); (vi) the W1
tables print the prediction error and the W2 transfer-geometry
columns fused (one table per candidate); the W3 margin
correlation prints raw and SENS side by side.

HONEST FRAME.  A LAWFUL Moebius step with an invariant interval
on 20+ finite rungs is a MEASUREMENT on compressed truncations
-- it does not prove transfer positivity for all h, and the
Weyl-family choice is a frozen concretization, not a derived
normal form.  MOEBIUS-DEAD on both candidates closes the
scalar-transfer route honestly (the cocycle probe's map then
lives only on the full carrier function, not on one scalar).
The census is FINITE.  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared null
permutation (seed 2) and the scramble control (seed 1); stdout
only.

Sources (read-only): v563_paper2_readouts (build_window,
atom_lags_at, arch_lags -- verbatim); window + deflation +
smooth-world machinery verbatim from christoffel_ratio_probe
(PRIME.PORT.CHRISTOFFEL.RATIO.01); IIKS port-carrier machinery
(antisym generators, SO(2) gauge, RP^1 chordal arithmetic)
verbatim from port_schur_cocycle_probe (PRIME.PORT.SCHURSTEP.01,
itself from port_riemann_hilbert_setup SPEC v2 /
lax2_flow_probe); pole-distance framing from port_sflow_toda
(PRIME.PORT.SFLOW.01).  IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/weyl_transfer_probe.py
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
PORT_SEAT_J = 24
N_RUNGS_EXP = 42
N_FULLWIN_FROZEN = 37
REF_N_TRUTH_PAIRS = 31
REF_N_SENS_PAIRS = 29
REF_N_SMOOTH_PAIRS = 28
KZ_STAR = 21
REF_CRAT_MIN = 0.223
REF_CRAT_MAX = 5.258
REF_CRAT_RTOL = 2e-2
CHR_WARD_FLOOR = 1e-8
CHR_COND_FAC = 1e3
CGE1_WARD = 1e-9
RANK_BAR = 1e-10
MIN_PORT_RUNGS = 30
MIN_QUADS = 15
MIN_QUADS_PORT = 10
SOLVE_DEGEN = 1e-12
POLE_GUARD = 1e-12
MOEB_LAWFUL_BAR = 1e-3
NULL_FAC = 10.0
DRIFT_FAC = 0.1
NULL_SEED = 2
MARGIN_CORR_BAR = 0.9
CRATIO_BAR = 1e-2
CTRL_KZ = 9
EPS = 2.220446049250313e-16
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


# --------- pipeline, verbatim (christoffel_ratio / cocycle chain)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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
    cocycle verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN SO(2) GAUGE pinned at the deepest port node
    (cocycle/lax2 verbatim)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    """SPEC v1 (v): pure memoization of core.build_window."""
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def ols_ab(x, y):
    """OLS y = a + b x -> (a, b)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    xm, ym = float(np.mean(x)), float(np.mean(y))
    b = float(np.sum((x - xm) * (y - ym))
              / np.sum((x - xm) ** 2))
    return ym - b * xm, b


def corr(x, y):
    return float(np.corrcoef(np.asarray(x, float),
                             np.asarray(y, float))[0, 1])


def quart_row(v):
    v = np.asarray(v, float)
    q = np.percentile(v, [25, 50, 75])
    return (float(np.min(v)), float(q[0]), float(q[1]),
            float(q[2]), float(np.max(v)))


def anatomy(kz, scramble_seed=None, comb=None, mode="truth"):
    """One rung -> ONE Gram E -> (a) the 12-window compression
    C_J + the deflated-Christoffel mass m^C at the soft seat
    (christoffel_ratio verbatim), and (b) mode 'truth' only: the
    dressed-port IIKS generators and the port carrier scalar at
    the frozen seat alias j* = 24 (cocycle verbatim, fused --
    both read the same negative-arm Gram)."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    B = np.sqrt(vs)[:, None] * Pn
    E = B @ B.T
    E = 0.5 * (E + E.T)
    n = E.shape[0]
    out = dict(kz=kz, h=h, n=n)
    G = B.T @ B
    G = 0.5 * (G + G.T)
    egG = np.linalg.eigvalsh(G)
    out["tau_full"] = float(1.0 - egG[-1])
    out["negA"] = int(np.sum(egG > 1.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    # 12-window compression (verbatim big Schur solve)
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if out["full"]:
        iw = [idx[j] for j in jav]
        io = [k for k in range(n) if k not in set(iw)]
        IO = np.eye(len(io)) - E[np.ix_(io, io)]
        try:
            CJ = (E[np.ix_(iw, iw)]
                  + E[np.ix_(iw, io)] @ np.linalg.solve(
                      IO, E[np.ix_(io, iw)]))
            out["CJ"] = 0.5 * (CJ + CJ.T)
        except np.linalg.LinAlgError:
            out["full"] = False
    if out["full"]:
        jstar = idx[JWIN[-1]]
        p = Pn[jstar]
        out["m_chr"] = float(vs[jstar]
                             * (p @ np.linalg.solve(
                                 np.eye(h) - G, p)))
    if mode != "truth":
        return out
    # dressed port + IIKS generators + seat scalar (cocycle
    # verbatim, fused)
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
        jp = uf_n[ip]
        f, g = gauge_fix(f, g, jp)
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
        kk = np.where(jp == PORT_SEAT_J)[0]
        if len(kk) == 1 and int(np.argmin(jp)) != int(kk[0]):
            k = int(kk[0])
            out["port_pair"] = (float(g[k]), float(f[k]))
            nrm = math.hypot(f[k], g[k])
            if abs(f[k]) > POLE_GUARD * nrm:
                out["m_port"] = float(g[k] / f[k])
            else:
                out["port_skip"] = "affine-pole"
        else:
            out["port_skip"] = ("seat-missing" if len(kk) != 1
                                else "seat-is-gauge-node")
    else:
        out["port_skip"] = "port-block-unavailable"
    return out


def win_attrs(r):
    """Per full rung: slogdet routes, d_12, tau_12, c, and the
    deflation-chain ward deviation (christoffel verbatim)."""
    A = np.eye(NW) - r["CJ"]
    sg12, ld12 = np.linalg.slogdet(A)
    sg11, ld11 = np.linalg.slogdet(A[:11, :11])
    r["sg_ok"] = (sg12 == 1.0 and sg11 == 1.0)
    r["d12"] = math.exp(ld12 - ld11) * sg12 * sg11
    r["tau12"] = float(np.linalg.eigvalsh(A)[0])
    r["c"] = r["d12"] / r["tau12"] if r["tau12"] != 0.0 \
        else float("inf")
    r["dev_chr"] = (abs(1.0 / r["d12"] - (1.0 + r["m_chr"]))
                    / max(abs(1.0 / r["d12"]), 1e-300))
    return r


# ---------------------------------------- Weyl-transfer machinery
def chord(u1, w1, u2, w2):
    """Chordal RP^1 distance between projective pairs."""
    n1 = math.hypot(u1, w1)
    n2 = math.hypot(u2, w2)
    if n1 <= 1e-300 or n2 <= 1e-300:
        return float("nan")
    return abs(u1 * w2 - w1 * u2) / (n1 * n2)


def solve_weyl(m1, m2, m3):
    """Exact (A, B) of m' = 1/(A - B m) from the two pairs
    (m1 -> m2), (m2 -> m3); None if degenerate."""
    Mx = np.array([[m2, -m1 * m2], [m3, -m2 * m3]])
    sc = float(np.max(np.abs(Mx)))
    det = float(np.linalg.det(Mx))
    if abs(det) <= SOLVE_DEGEN * max(sc, 1.0) ** 2:
        return None
    A, Bc = np.linalg.solve(Mx, np.array([1.0, 1.0]))
    return float(A), float(Bc)


def quad_rows(entries):
    """Sliding quadruples of ADJACENT ladder entries: solve the
    Weyl transfer from pairs 1, 2, predict pair 3 chordally.
    entry: dict(h, kz, m (affine or None), pair (u, w) or None,
    c, tau)."""
    rows, n_skip = [], 0
    for i in range(len(entries) - 3):
        e = entries[i:i + 4]
        if any(x is None for x in e):
            continue
        if any(x["m"] is None for x in e[:3]) \
                or e[3]["pair"] is None:
            n_skip += 1
            continue
        sol = solve_weyl(e[0]["m"], e[1]["m"], e[2]["m"])
        if sol is None:
            n_skip += 1
            continue
        A, Bc = sol
        den = A - Bc * e[2]["m"]
        u4, w4 = e[3]["pair"]
        err = chord(1.0, den, u4, w4)
        if err != err:
            n_skip += 1
            continue
        row = dict(hs=[x["h"] for x in e],
                   kzs=[x["kz"] for x in e],
                   A=A, B=Bc, m3=e[2]["m"], err=err,
                   sens=all(x["kz"] != KZ_STAR for x in e))
        if e[2]["c"] is not None and e[3]["c"] is not None:
            row["cr"] = e[3]["c"] / e[2]["c"]
            row["deriv"] = (Bc / den ** 2 if den != 0.0
                            else float("inf"))
        rows.append(row)
    return rows, n_skip


def quint_rows(entries):
    """Unscored diagnostic: full 3-dof Moebius solved exactly
    from three pairs (quintuples), fourth pair predicted."""
    errs = []
    for i in range(len(entries) - 4):
        e = entries[i:i + 5]
        if any(x is None for x in e):
            continue
        if any(x["m"] is None for x in e[:4]) \
                or e[4]["pair"] is None:
            continue
        rws = np.array([[e[k]["m"], 1.0,
                         -e[k]["m"] * e[k + 1]["m"],
                         -e[k + 1]["m"]] for k in range(3)])
        _u, s, Vh = np.linalg.svd(rws)
        if s[2] <= 1e-12 * max(s[0], 1e-300):
            continue
        a, b, c, dd = Vh[-1]
        u4, w4 = e[4]["pair"]
        err = chord(a * e[3]["m"] + b, c * e[3]["m"] + dd,
                    u4, w4)
        if err == err:
            errs.append(err)
    return errs


def null_errs(entries, seed):
    """Shuffled-triple null: the same solve+predict on the
    rng-permuted candidate ladder (mismatched rung triples)."""
    live = [x for x in entries
            if x is not None and x["m"] is not None
            and x["pair"] is not None]
    rng = np.random.default_rng(seed)
    perm = [live[i] for i in rng.permutation(len(live))]
    rows, _ = quad_rows(perm)
    return [row["err"] for row in rows]


def typed_w1(name, med, null_med, slope):
    if med < MOEB_LAWFUL_BAR and null_med >= NULL_FAC * med:
        return "MOEBIUS-LAWFUL"
    if med <= DRIFT_FAC * null_med:
        if med < MOEB_LAWFUL_BAR:
            return "MOEBIUS-DEAD(NULL-INDISTINCT)"
        return "MOEBIUS-DRIFTING(med=%.1e, slope=%+.2f)" % (med,
                                                            slope)
    if med < MOEB_LAWFUL_BAR:
        return "MOEBIUS-DEAD(NULL-INDISTINCT)"
    return "MOEBIUS-DEAD"


def main():
    section("PRIME.PORT.WEYLTRANSFER.01 -- the ladder step as a "
            "2x2 Weyl transfer / Moebius map (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth + smooth ladders (frame-A "
            "zones, h <= %d; ONE Gram per rung, fused port "
            "block)" % H_DEEP_MAX)
    truth, smooth = [], []
    n_toodeep, n_dead_t, n_dead_s = 0, 0, 0
    for kz in core.frame_a_zones():
        r = anatomy(kz, mode="truth")
        if r == "TOO-DEEP":
            n_toodeep += 1
            continue
        if r is None:
            n_dead_t += 1
            continue
        truth.append(r)
        uu = window_of(kz)["uu"]
        rs = anatomy(kz, comb=(uu, smooth_masses(uu)),
                     mode="smooth")
        if isinstance(rs, dict):
            smooth.append(rs)
        else:
            n_dead_s += 1
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    smooth.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs (h %d..%d; %d TOO-DEEP zones, %d "
          "chain deaths) | smooth: %d rungs (%d deaths)  [%.1f s]"
          % (len(truth), truth[0]["h"], truth[-1]["h"],
             n_toodeep, n_dead_t, len(smooth), n_dead_s,
             time.time() - T0))
    check("W0 truth ladder == %d rungs (deepcore census)"
          % N_RUNGS_EXP, len(truth) == N_RUNGS_EXP,
          "%d" % len(truth), kill="KP")
    fullw = [r for r in truth if r.get("full") and "CJ" in r]
    check("W0c truth full-window census %d == %d (hirota frozen)"
          % (len(fullw), N_FULLWIN_FROZEN),
          len(fullw) == N_FULLWIN_FROZEN, kill="KP")
    portr = [r for r in truth if "rk" in r]
    check("W0p >= %d rungs carry the port block" % MIN_PORT_RUNGS,
          len(portr) >= MIN_PORT_RUNGS, "%d" % len(portr),
          kill="KP")
    rk_max = max((r["rk"] for r in portr), default=1.0)
    check("W0r [Y, D_P] rank-2 exact on every port rung (max "
          "s3/s1 %.1e <= %.0e)" % (rk_max, RANK_BAR),
          rk_max <= RANK_BAR, kill="KP")
    skips = {}
    for r in truth:
        if "port_skip" in r:
            skips[r["port_skip"]] = skips.get(r["port_skip"],
                                              0) + 1
    print("    port seat (j* = %d) typed skips: %s"
          % (PORT_SEAT_J, skips if skips else "none"))
    if KILLS:
        return finish({})

    # ---------------------------------------------------- W-D, W-R
    section("W-D / W-R -- deflation-chain + round-55 "
            "reproduction wards")
    for r in fullw:
        win_attrs(r)
    sg_all = all(r["sg_ok"] for r in fullw)
    chr_worst = max(r["dev_chr"]
                    / max(CHR_WARD_FLOOR,
                          CHR_COND_FAC * EPS / r["tau_full"])
                    for r in fullw)
    dev_chr = max(r["dev_chr"] for r in fullw)
    check("W-D deflation chain 1/d_12 == 1 + m^C per full rung: "
          "max rel %.1e, worst dev/bar %.3f <= 1; minor signs "
          "+1: %s" % (dev_chr, chr_worst, sg_all),
          chr_worst <= 1.0 and sg_all, kill="KW")
    c_min = min(r["c"] for r in fullw)
    tau_min = min(r["tau12"] for r in fullw)
    check("W-D2 c >= 1 (min %.3f) and tau_12 > 0 (min %.3e) on "
          "every full rung" % (c_min, tau_min),
          c_min >= 1.0 - CGE1_WARD and tau_min > 0.0, kill="KW")
    pairs = []
    for ra, rb in zip(truth[:-1], truth[1:]):
        if ra.get("full") and rb.get("full") \
                and "c" in ra and "c" in rb:
            pairs.append((ra, rb))
    n_pos = sum(1 for ra, rb in pairs
                if rb["d12"] / ra["d12"] > 0.0)
    pairs_s = [(ra, rb) for ra, rb in pairs
               if KZ_STAR not in (ra["kz"], rb["kz"])]
    crat_s = np.array([rb["c"] / ra["c"] for ra, rb in pairs_s])
    m_s, M_s = float(np.min(crat_s)), float(np.max(crat_s))
    check("W-R pair census %d == %d, r_12 > 0 on %d/%d, SENS "
          "census %d == %d, c'/c SENS [%.3f, %.3f] == [%.3f, "
          "%.3f] (rtol %.0e)"
          % (len(pairs), REF_N_TRUTH_PAIRS, n_pos, len(pairs),
             len(pairs_s), REF_N_SENS_PAIRS, m_s, M_s,
             REF_CRAT_MIN, REF_CRAT_MAX, REF_CRAT_RTOL),
          len(pairs) == REF_N_TRUTH_PAIRS
          and n_pos == len(pairs)
          and len(pairs_s) == REF_N_SENS_PAIRS
          and abs(m_s / REF_CRAT_MIN - 1.0) <= REF_CRAT_RTOL
          and abs(M_s / REF_CRAT_MAX - 1.0) <= REF_CRAT_RTOL,
          kill="KW")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ W1
    section("W1 -- THE FIT-FREE MOEBIUS TEST (Weyl family "
            "m' = 1/(A - B m); quadruples: 2 pairs solve, 3rd "
            "pair predicted)")
    cand = {}
    for name in ("PORT", "CHR"):
        entries = []
        for r in truth:
            if not (r.get("full") and "c" in r):
                entries.append(None)
                continue
            if name == "PORT":
                m = r.get("m_port")
                pair = r.get("port_pair")
            else:
                m = r.get("m_chr")
                pair = (m, 1.0) if m is not None else None
            entries.append(dict(h=r["h"], kz=r["kz"], m=m,
                                pair=pair, c=r["c"],
                                tau=r["tau12"]))
        rows, n_skip = quad_rows(entries)
        nerrs = null_errs(entries, NULL_SEED)
        cand[name] = dict(entries=entries, rows=rows,
                          n_skip=n_skip, nerrs=nerrs)
        print("\n  %s candidate (%d quadruples, %d typed skips):"
              % (name, len(rows), n_skip))
        print("    %-22s %-11s %-11s %-9s %-6s %-7s %-13s %s"
              % ("step (h1..h4)", "A", "B", "err", "sgn",
                 "trace", "fixed pts", ""))
        for row in rows:
            s = math.sqrt(abs(row["B"])) if row["B"] != 0.0 \
                else float("nan")
            tr = row["A"] / s if s == s and s > 0.0 \
                else float("nan")
            disc = row["A"] ** 2 - 4.0 * row["B"]
            if disc >= 0.0 and row["B"] != 0.0:
                rt = math.sqrt(disc)
                fp = "%+.2e/%+.2e" % (
                    (row["A"] - rt) / (2.0 * row["B"]),
                    (row["A"] + rt) / (2.0 * row["B"]))
            else:
                fp = "cplx"
            row["uhp"] = row["B"] > 0.0
            row["intv"] = (row["A"] > 0.0 and row["B"] <= 0.0)
            print("    %3d>%3d>%3d>%3d      %-+11.3e %-+11.3e "
                  "%-9.1e %-6s %-+7.2f %-13s%s"
                  % (row["hs"][0], row["hs"][1], row["hs"][2],
                     row["hs"][3], row["A"], row["B"],
                     row["err"], "+" if row["uhp"] else "-",
                     tr, fp,
                     "" if row["sens"] else "  <-- kz-21"))
        errs = np.array([row["err"] for row in rows])
        med = float(np.median(errs)) if len(errs) else 1.0
        nmed = (float(np.median(cand[name]["nerrs"]))
                if cand[name]["nerrs"] else float("nan"))
        h4 = np.log([row["hs"][3] for row in rows])
        le = np.log10(np.maximum(errs, 1e-300))
        _a, slope = ols_ab(h4, le) if len(rows) >= 3 \
            else (0.0, float("nan"))
        cand[name]["med"] = med
        cand[name]["slope"] = slope
        mn, q1, q2, q3, mx = quart_row(errs) if len(errs) \
            else (1,) * 5
        print("    truth errs: min %.1e q25 %.1e med %.1e q75 "
              "%.1e max %.1e | trend slope(log10 err vs log h) "
              "%+.2f" % (mn, q1, q2, q3, mx, slope))
        if cand[name]["nerrs"]:
            nn = quart_row(cand[name]["nerrs"])
            print("    NULL errs (%d shuffled quadruples, seed "
                  "%d): min %.1e q25 %.1e med %.1e q75 %.1e max "
                  "%.1e" % ((len(cand[name]["nerrs"]),
                             NULL_SEED) + nn))
        print("    DECISIVE: truth med %.2e vs null med %.2e "
              "(ratio %.1f; LAWFUL needs < %.0e and >= %.0fx)"
              % (med, nmed, nmed / med if med > 0 else
                 float("inf"), MOEB_LAWFUL_BAR, NULL_FAC))
        cand[name]["type"] = typed_w1(name, med, nmed, slope)
        qerrs = quint_rows(entries)
        print("    secondary (unscored) full-Moebius quintuple "
              "diagnostic: %d quints, med err %s"
              % (len(qerrs),
                 "%.2e" % float(np.median(qerrs)) if qerrs
                 else "n/a"))
    check("W1.1 quadruple censuses: CHR %d >= %d, PORT %d >= %d"
          % (len(cand["CHR"]["rows"]), MIN_QUADS,
             len(cand["PORT"]["rows"]), MIN_QUADS_PORT),
          len(cand["CHR"]["rows"]) >= MIN_QUADS
          and len(cand["PORT"]["rows"]) >= MIN_QUADS_PORT,
          kill="KP")
    check("W1.2 typed: PORT %s | CHR %s (honest either way)"
          % (cand["PORT"]["type"], cand["CHR"]["type"]), True)
    if KILLS:
        return finish({})

    lawful = [n for n in ("PORT", "CHR")
              if cand[n]["type"].startswith("MOEBIUS-LAWFUL")
              or cand[n]["type"].startswith("MOEBIUS-DRIFTING")]
    if len(lawful) == 2:
        primary = min(lawful, key=lambda n: cand[n]["med"])
    elif len(lawful) == 1:
        primary = lawful[0]
    else:
        primary = "CHR"
    print("\n    PRIMARY candidate for W2/W3 typed labels: %s "
          "(frozen rule iv)" % primary)

    # ------------------------------------------------------------ W2
    section("W2 -- TRANSFER GEOMETRY / INVARIANCE CENSUS "
            "(typed on %s, SENS quadruples)" % primary)
    w2lab = {}
    for name in ("PORT", "CHR"):
        rows = cand[name]["rows"]
        rs = [row for row in rows if row["sens"]]
        n_uhp = sum(1 for row in rs if row["uhp"])
        n_int = sum(1 for row in rs if row["intv"])
        bad_u = [row["hs"][2] for row in rs if not row["uhp"]]
        bad_i = [row["hs"][2] for row in rs if not row["intv"]]
        if rs and n_uhp == len(rs):
            lab = "HERGLOTZ-INVARIANT(UHP)"
        elif rs and n_int == len(rs):
            lab = "HERGLOTZ-INVARIANT(INT)"
        else:
            lab = ("HERGLOTZ-BROKEN(UHP %d/%d, INT %d/%d; "
                   "first UHP-viol h=%s, first INT-viol h=%s)"
                   % (n_uhp, len(rs), n_int, len(rs),
                      bad_u[0] if bad_u else "-",
                      bad_i[0] if bad_i else "-"))
        w2lab[name] = lab
        n_uhp_r = sum(1 for row in rows if row["uhp"])
        n_int_r = sum(1 for row in rows if row["intv"])
        print("  %s: sign census RAW %d quads: UHP(B>0) %d, "
              "INT(A>0,B<=0) %d | SENS %d quads: UHP %d, INT %d"
              % (name, len(rows), n_uhp_r, n_int_r, len(rs),
                 n_uhp, n_int))
        print("        -> %s" % lab)
    print("    (UHP and INT are mutually exclusive for this "
          "family: which sign structure the ladder chooses is "
          "the measurement.)")
    check("W2.1 typed: %s (on %s)" % (w2lab[primary], primary),
          True)

    # ------------------------------------------------------------ W3
    section("W3 -- MARGIN AS BOUNDARY DISTANCE + C-RATIO "
            "IDENTIFICATION (typed on %s)" % primary)
    w3m, w3c = {}, {}
    for name in ("PORT", "CHR"):
        ent = [x for x in cand[name]["entries"]
               if x is not None and x["m"] is not None
               and x["m"] != 0.0]
        dist = np.array([min(abs(x["m"]), 1.0)
                         / math.sqrt(1.0 + x["m"] ** 2)
                         for x in ent])
        tau = np.array([x["tau"] for x in ent])
        kzs = np.array([x["kz"] for x in ent])
        sel = kzs != KZ_STAR
        cr_raw = corr(np.log(dist), np.log(tau))
        cr_sens = corr(np.log(dist[sel]), np.log(tau[sel]))
        # align tau_full by kz for the secondary corr
        tf_map = {r["kz"]: r["tau_full"] for r in fullw}
        tf = np.array([tf_map[x["kz"]] for x in ent])
        cr_tf = corr(np.log(dist[sel]), np.log(tf[sel]))
        rat = dist[sel] / tau[sel]
        mn, q1, q2, q3, mx = quart_row(rat)
        print("  %s (%d rungs): corr(log dist, log tau_12) "
              "%+.4f raw / %+.4f SENS | corr vs log tau_full "
              "%+.4f SENS" % (name, len(ent), cr_raw, cr_sens,
                              cr_tf))
        print("        ratio dist/tau_12 (SENS): min %.3g q25 "
              "%.3g med %.3g q75 %.3g max %.3g"
              % (mn, q1, q2, q3, mx))
        w3m[name] = ("MARGIN-IS-DISTANCE(corr=%.3f)" % cr_sens
                     if cr_sens >= MARGIN_CORR_BAR else
                     "MARGIN-DECOUPLED(corr=%.3f)" % cr_sens)
        # c-ratio identification on the quadruples
        rows = [row for row in cand[name]["rows"]
                if "cr" in row and row["sens"]]
        rels = np.array([abs(row["deriv"] - row["cr"])
                         / max(abs(row["cr"]), 1e-300)
                         for row in rows])
        med_rel = float(np.median(rels)) if len(rels) \
            else float("inf")
        w3c[name] = ("CRATIO-IS-DERIVATIVE(med=%.1e)" % med_rel
                     if med_rel < CRATIO_BAR else
                     "CRATIO-FREE(med=%.1e)" % med_rel)
        if len(rels):
            mn, q1, q2, q3, mx = quart_row(rels)
            print("        c-ratio: deriv B/(A - B m_3)^2 vs "
                  "measured c'/c on %d SENS quads: rel min %.2g "
                  "q25 %.2g med %.2g q75 %.2g max %.2g"
                  % (len(rels), mn, q1, q2, q3, mx))
        print("        -> %s | %s" % (w3m[name], w3c[name]))
    check("W3.1 typed: %s (on %s; bar %.2f)"
          % (w3m[primary], primary, MARGIN_CORR_BAR), True)
    check("W3.2 typed: %s (on %s; bar %.0e, signed comparison)"
          % (w3c[primary], primary, CRATIO_BAR), True)

    # ------------------------------------------------------------ C
    section("C -- controls: the machinery must BREAK off the "
            "truth comb")
    sfull = [r for r in smooth if r.get("full") and "CJ" in r]
    for r in sfull:
        A = np.eye(NW) - r["CJ"]
        r["tau12"] = float(np.linalg.eigvalsh(A)[0])
    spairs = []
    for ra, rb in zip(smooth[:-1], smooth[1:]):
        if ra.get("full") and rb.get("full") \
                and "tau12" in ra and "tau12" in rb:
            spairs.append((ra, rb))
    n_cone = sum(1 for ra, _rb in spairs if ra["tau12"] <= 0.0)
    sneg = [r for r in smooth if r["tau_full"] < 0.0]
    print("  C-S  smooth 12-window: %d pairs, base tau_12 <= 0 "
          "on %d/%d; sigma indefinite (tau_full < 0) on %d/%d "
          "rungs, first at h = %s"
          % (len(spairs), n_cone, len(spairs), len(sneg),
             len(smooth), sneg[0]["h"] if sneg else "n/a"))
    print("       (the PD premise of BOTH candidates dies: m^C "
          "is no Christoffel mass of a PD functional, and the "
          "interval [0, inf) is no cone)")
    check("C-S smooth world: %d pairs == %d with cone-exit "
          "%d/%d AND sigma indefinite on >= 1 rung (%d)"
          % (len(spairs), REF_N_SMOOTH_PAIRS, n_cone,
             len(spairs), len(sneg)),
          len(spairs) == REF_N_SMOOTH_PAIRS
          and n_cone == len(spairs) and len(sneg) >= 1,
          kill="KW")
    try:
        rc = anatomy(CTRL_KZ, scramble_seed=1, mode="ctrl")
    except (np.linalg.LinAlgError, AssertionError):
        rc = None
    if not isinstance(rc, dict):
        print("  C-E  scramble: chain dies (%r) -> FIRES "
              "(frame death)" % (rc,))
        fired = True
    else:
        tau12c = None
        if rc.get("full") and "CJ" in rc:
            tau12c = float(np.linalg.eigvalsh(
                np.eye(NW) - rc["CJ"])[0])
        fired = (rc["negA"] > 0
                 or (tau12c is not None and tau12c <= 0.0)
                 or tau12c is None)
        print("  C-E  scramble at kz %d: neg(A) %d | tau_12 %s "
              "-> %s via %s"
              % (CTRL_KZ, rc["negA"],
                 ("%+.3e" % tau12c) if tau12c is not None
                 else "n/a (window not full)",
                 "FIRES" if fired else "SILENT",
                 "NEG-COUNT" if rc["negA"] > 0 else
                 "WINDOW" if tau12c is not None else
                 "FRAME-DEATH"))
    check("C-E scramble control fires", fired, kill="KW")

    return finish(dict(port=cand["PORT"]["type"],
                       chr=cand["CHR"]["type"],
                       primary=primary,
                       w2=w2lab[primary],
                       w3m=w3m[primary], w3c=w3c[primary],
                       med_p=cand["PORT"]["med"],
                       med_c=cand["CHR"]["med"]))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("WEYLTRANSFER-MEASURED / PORT: %(port)s / "
                   "CHR: %(chr)s / %(w2)s / %(w3m)s / %(w3c)s"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
        print("  (primary %(primary)s; med errs PORT %(med_p).2e"
              " / CHR %(med_c).2e)" % labels)
    print("""
  HONEST FRAME (as frozen): a lawful Moebius step with an
  invariant interval on finitely many rungs is a MEASUREMENT on
  compressed truncations -- it does not prove transfer
  positivity for all h, and the Weyl family m' = 1/(A - B m) is
  a frozen concretization, not a derived normal form.
  MOEBIUS-DEAD on both candidates closes the scalar-transfer
  route honestly (the cocycle probe's Moebius map then lives
  only on the full carrier function).  The census is FINITE.
  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
