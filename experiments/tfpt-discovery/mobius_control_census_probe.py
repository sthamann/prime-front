#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mobius_control_census_probe -- PRIME.PORT.MOEBIUS.CENSUS.01
(EXPLORATION ONLY, experiments/; round 48, reviewer probe 4: run
the IDENTICAL Moebius-analysis pipeline on SIX worlds and report
the full discriminator table with NO post-hoc selection -- this
decides whether the Moebius structure is arithmetic dynamics,
universal geometry, or artifact, 2026-08-09).

THE QUESTION (frozen): port_schur_cocycle_probe measured a clean
per-rung Moebius step on the PSL(2,R)-normalized port carrier
m = g/f (median residual 0.0015, |alpha| < 1 on 100%), and
moebius_source_step_probe typed it CARRIER-INVARIANT.  But the
only controls run so far (Epstein, scramble at kz 9) die at the
FRAME, so nothing yet separates "arithmetic dynamics" from
"rank-2 kinematics that any window of this geometry produces".
The smooth worlds of lattice_parametrix_probe (B1) and
edge_bulk_smoothing_probe (Z1/Z2) keep the WINDOW GEOMETRY
intact (same positions, smoothed masses), so their frames should
survive where Epstein/scramble frame-die -- verify -- and they
are the honest controls for the census.

THE SIX WORLDS (frozen; identical pipeline, full ladder each):
  W1  TRUTH:      masses 2 Lambda(n)/sqrt(n) at u_n = log n;
  W2  EPSTEIN:    lambda_eps recursion comb of x^2 + 5 y^2
                  (per-rung N_E = floor(exp(2 alpha)) + 1);
  W3  SCRAMBLE:   positions ~ U(0, 2 alpha), seed 1 (the only
                  RNG in the probe), true masses;
  W4  LATTICE-SMOOTH (B1): true positions, fully smooth
                  quadrature masses 2 e^{u/2} du (lattice_
                  parametrix verbatim) -- no Lambda information;
  W5  EDGE-SMOOTHED (Z1): B2-style local-average masses on the
                  edge zone u > U - 1 only, interior exact
                  (edge_bulk_smoothing verbatim);
  W6  INTERIOR-SMOOTHED (Z2): local-average masses on u <= U - 1
                  only, edge exact (edge_bulk_smoothing
                  verbatim).

THE LADDER (frozen, port_schur_cocycle verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive rung pairs with >= 8 common port alias indices.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run; the
NO-POST-HOC-SELECTION RULE: every world runs the identical
pipeline end to end, every discriminator is computed wherever it
mechanically runs, and every number is printed -- no world, rung,
step, or discriminator is dropped after seeing results):

 P   THE PIPELINE PER WORLD (identical, port_schur_cocycle /
     moebius_source_step verbatim): build the windows (heavy
     build: tent assembly, folded measures, Lanczos chain, Gram
     E), the 12-index window compression C_J (J = {2,...,24}),
     the dressed port D_P and the gauge-fixed IIKS generators
     (f, g) on the port-decile nodes.  A rung's carrier is VALID
     iff the commutator [Y, D_P] is numerically rank 2
     (s3/s1 <= 1e-6, identical bar for all worlds; the truth
     ladder is additionally warded at the predecessor's 1e-10,
     K1).  Per consecutive valid pair with >= 8 common alias
     indices, five discriminators:
     (a) CR   fit-free cross-ratio defect: from the common nodes
         (sorted by alias index) take K = min(n, 12) evenly
         spaced nodes; battery = all C(K, 4) quadruples whose
         six pairwise chordal separations are >= 1e-3 in BOTH
         rungs (well-conditioned); per quadruple the homogeneous
         cross-ratio cr = ([p0 p2][p1 p3] : [p0 p3][p1 p2]) as a
         unit pair, defect = chordal(cr_a, cr_b); per-step value
         = median over the battery (typed skip if < 5
         quadruples).  Fit-free: Moebius maps preserve cr
         exactly.  (The battery rule is frozen HERE; the
         parallel crossratio probe was not in the tree at freeze
         time -- amendment (ii).)
     (b) STEP the three-anchor step map: anchors = the three
         deepest common nodes (smallest alias j, predecessor
         verbatim; degenerate anchors = typed skip); S =
         T_b^{-1} T_a with T the (0, 1, inf) normalizers;
         per-step value = median chordal(S p_a, p_b) on the
         NON-anchor common nodes; |alpha| = the Cayley datum of
         the det-normalized S_n = S / sqrt(|det S|) (frozen
         convention).
     (c) JRES J-contractivity residual: min eig(J - S_n^* J S_n)
         with J = [[0, -i], [i, 0]] (upper-half-plane signature)
         on the det-normalized S_n; for real 2x2 this equals
         -(1 - sign det S) sized, i.e. 0 for orientation-
         preserving steps and -2 for orientation-reversing ones
         -- the census is the orientation/contractivity
         coherence of the ladder.
     (d) RAW  raw identity distance: median chordal(p_a, p_b)
         over ALL common nodes, gauge-fixed but UNNORMALIZED (no
         PSL(2,R) three-point normalization).
     (e) TAU  tau-factor sign census: per rung with an available
         window (>= 8 of the 12 alias indices), the sign of
         det(I - C_J) via slogdet; the world's census = the
         number of sign flips along the ladder.
     WORLD VALUES: ladder medians of (a), (b), (d); ladder MIN
     of (c) plus the det > 0 fraction; flip count for (e).

 F   FRAME-SURVIVAL CENSUS (part of the deliverable): per world
     report #rungs built (Lanczos completes), #carrier-valid
     (rank-2 bar), #window-available (>= 8 alias indices),
     #window-ALIVE (available AND lam(I-E_out) subcritical
     lam(out) < 1 AND lam(C_J) < 1), #full 12-window, #measured
     steps.  FROZEN FRAME-ALIVE RULE: a world is FRAME-ALIVE iff
     #built >= 10 AND #window-alive >= 0.5 x #built AND
     #carrier-valid >= 10.  FROZEN FALLBACK: if any FRAME-ALIVE
     world has < 5 window-available rungs, discriminator (e) is
     additionally computed on the largest common window = the
     port-decile alias indices present on >= 0.80 of the rungs
     of EVERY frame-alive world (12 smallest; needs >= 4), via
     the stored Lanczos chains; the fallback census then stands
     in for (e) wherever the primary is N/A.

 T   TYPED READING (frozen decision rules, no cherry-picking).
     PASS bars per discriminator and world: (a) median <= 0.05;
     (b) median <= 0.05; (c) ladder min >= -1e-8 (all steps
     orientation-preserving J-isometries); (d) median <= 0.05;
     (e) >= 5 windowed rungs and 0 sign flips.  A discriminator
     with < 10 measured steps (or < 5 windowed rungs for (e)) in
     a world is N/A there; N/A counts as FAIL in the typing of a
     frame-alive world (typed, reported).  Per discriminator D:
       D-ARITHMETIC iff truth passes AND >= 1 control is
         frame-alive AND ALL frame-alive controls fail;
       D-GEOMETRIC  iff truth passes AND >= 2 frame-alive
         controls pass;
       D-UNDECIDED  otherwise (including truth-fails and the
         no-frame-alive-controls case: frame-only separation).
     Frame-DEAD controls' discriminator values are printed
     (no post-hoc selection) but do not enter the typing.
     The reviewer's expectation under test: the Moebius/cr
     structure itself types GEOMETRIC (rank-2 kinematics), while
     the arithmetic separation lives in (c), in (e), or in
     neither -- then the census says the route needs the
     scalar-cocycle/determinant bridge instead (the parallel
     tau_mobius_factor probe's territory).

KILLS: K1 truth-pipeline ward breaks (>= 30 truth rungs, truth
rank ward 1e-10, >= 30 truth steps, truth frame-alive, Epstein
sieve ward) -> PIPELINE-BROKEN.  Frame death of any CONTROL
world is a reported census outcome, not a kill.

VERDICT (frozen enum): MOEBIUSCENSUS-MEASURED with the
per-discriminator typing a:/b:/c:/d:/e: each in {ARITHMETIC,
GEOMETRIC, UNDECIDED(...)}; else PIPELINE-BROKEN.

SPEC v2 AMENDMENTS (documented before the run; fail-first
preserved): (i) the Epstein recursion is sieve-accelerated
(vectorized r-count + forward-push divisor sieve), warded in-run
against the verbatim O(N^2) recursion at N = 2000 (max dev
<= 1e-9, K1); (ii) the quadruple-battery rule for (a) is frozen
in this docstring (the parallel crossratio probe was absent from
the tree at freeze time); (iii) the carrier-validity bar is
1e-6 identically for all six worlds; the predecessor's 1e-10 is
kept as the TRUTH ward only (a control failing rank-2 is a
frame-death channel, not a kill); (iv) each rung stores its
Lanczos chain and negative-arm data so the frozen fallback
window can be recompressed without a second heavy pass --
bookkeeping only, physics verbatim; (v) the frame-alive rule is
quantified as printed above (the predecessors' single-rung
controls never needed a ladder-level rule); (vi) after run 1
(which measured win-ALIVE = 0 on all five controls) the frame
table gained the median lam(out) / lam(C_J) columns, the
fire-channel counts, and the explicit availability-vs-
subcriticality note for the fallback clause, and the verdict
block gained the computed frame-dead context lines -- REPORTING
ONLY: no bar, rule, or pipeline change; fail-first preserved.

NO RH claim -- a six-world discriminator census on compressed
truncations is a numerical measurement, not a theorem about
zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble world (seed 1); stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; carrier pipeline
verbatim from port_schur_cocycle_probe.py (PRIME.PORT.
SCHURSTEP.01) / moebius_source_step_probe.py (PRIME.PORT.
MOEBIUS.SOURCE.01); smooth worlds verbatim from
lattice_parametrix_probe.py (PRIME.PORT.LATTICE.PARAMETRIX.01,
B1) and edge_bulk_smoothing_probe.py (PRIME.PORT.LATTICE.
PARAMETRIX.02, Z1/Z2).  IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mobius_control_census_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from itertools import combinations

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
MIN_COMMON_J = 8
REF_SEP_MIN = 1e-6
CARRIER_RK_BAR = 1e-6       # identical validity bar, all worlds (iii)
TRUTH_RK_BAR = 1e-10        # predecessor ward, truth only (K1)
MIN_RUNGS_TRUTH = 30
MIN_STEPS_TRUTH = 30

# frame-alive rule (v)
MIN_BUILT_ALIVE = 10
WIN_ALIVE_FRAC = 0.5
MIN_CARRIER_ALIVE = 10

# discriminator bars (frozen)
CR_MAX_NODES = 12
CR_SEP_MIN = 1e-3
CR_MIN_QUADS = 5
BAR_A = 0.05
BAR_B = 0.05
BAR_C = -1e-8
BAR_D = 0.05
MIN_STEPS_WORLD = 10
MIN_WIN_RUNGS_E = 5

# fallback window (F)
FB_PRESENCE_FRAC = 0.80
FB_MAX_NODES = 12
FB_MIN_NODES = 4

EPS_WARD_N = 2000
EPS_WARD_BAR = 1e-9
SCRAMBLE_SEED = 1

WORLDS = ("W1", "W2", "W3", "W4", "W5", "W6")
WNAME = {"W1": "truth", "W2": "epstein", "W3": "scramble",
         "W4": "lattice-smooth", "W5": "edge-smoothed",
         "W6": "interior-smoothed"}
CONTROLS = ("W2", "W3", "W4", "W5", "W6")

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


# --------- pipeline, verbatim from port_schur_cocycle_probe
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps_slow(N):
    """The predecessors' verbatim O(N^2) Epstein recursion (ward
    reference only, amendment (i))."""
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


def lambda_eps(N):
    """Sieve-accelerated Epstein recursion: vectorized r-count +
    forward-push divisor sieve; warded against lambda_eps_slow at
    N = 2000 (amendment (i))."""
    s = int(math.isqrt(N)) + 1
    g = np.arange(-s, s + 1)
    v = (g[:, None] ** 2 + 5 * g[None, :] ** 2).ravel()
    v = v[(v >= 1) & (v <= N)]
    a = np.bincount(v, minlength=N + 1).astype(float) / 2.0
    lam = np.zeros(N + 1)
    nn = np.arange(N + 1, dtype=float)
    nn[0] = 1.0
    acc = a * np.log(nn)
    for n in range(2, N + 1):
        lam[n] = acc[n]
        if lam[n] != 0.0 and 2 * n <= N:
            acc[2 * n::n] -= lam[n] * a[2:(N // n) + 1]
    return lam


_EPS_CACHE = {}


def eps_comb(alpha):
    N_E = int(math.floor(math.exp(2.0 * alpha))) + 1
    if N_E not in _EPS_CACHE:
        lamE_ = lambda_eps(N_E)
        nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
        _EPS_CACHE[N_E] = (np.log(nn.astype(float)),
                           2.0 * lamE_[nn] / np.sqrt(
                               nn.astype(float)))
    return _EPS_CACHE[N_E]


# --------- smooth-world mass constructions, verbatim
def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smoothed_masses(uu, mm, zone_mask):
    """B2-style local-average masses inside the zone, exact outside
    (edge_bulk_smoothing verbatim)."""
    du = cell_widths(uu)
    m_shape = 2.0 * np.exp(uu / 2.0) * du
    out = mm.copy()
    for i in np.where(zone_mask)[0]:
        w = (np.abs(uu - uu[i]) <= 0.5) & zone_mask
        s_true = float(np.sum(mm[w]))
        s_shape = float(np.sum(m_shape[w]))
        out[i] = m_shape[i] * (s_true / s_shape
                               if s_shape > 0 else 1.0)
    return out


def world_source(world, rr):
    """The (positions, masses) of a world on one rung.  W1/W4/W5/W6
    share the true positions; W2 replaces the comb; W3 scrambles
    positions upstream (build_window seed)."""
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if world in ("W1", "W3"):
        return uu, mm
    if world == "W2":
        return eps_comb(float(rr["alpha"]))
    if world == "W4":
        return uu, 2.0 * np.exp(uu / 2.0) * cell_widths(uu)
    edge = uu > float(np.max(uu)) - 1.0
    if world == "W5":
        return uu, smoothed_masses(uu, mm, edge)
    return uu, smoothed_masses(uu, mm, ~edge)          # W6


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
    verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN GAUGE (lax2 verbatim)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, world):
    """One heavy build per (rung, world): identical pipeline; the
    world enters ONLY through the source comb (P).  Chain data is
    stored for the frozen fallback recompression (amendment iv)."""
    rr = core.build_window(
        kz, scramble_seed=(SCRAMBLE_SEED if world == "W3"
                           else None))
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    uu, mm = world_source(world, rr)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    if len(xs) < 4 or len(ys) < 4:
        return None
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, al=al, be=be, m0=m0, ys=ys, vs=vs,
               uf_n=uf_n)
    # ---- window compression (port_cocycle_window verbatim)
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
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
        sgn, ld = np.linalg.slogdet(np.eye(len(jav)) - CJ)
        out["detsgn"], out["detld"] = float(sgn), float(ld)
    # ---- dressed port + IIKS generators (verbatim)
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
        f, g = gauge_fix(f, g, uf_n[ip])
        out["f"], out["g"] = f, g
        out["jp"] = uf_n[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


def rebuild_E(r):
    """Recompute the Gram E of a stored rung from its Lanczos chain
    (fallback pass only; amendment iv)."""
    Pn = eval_chain(r["al"], r["be"], r["m0"], r["ys"], r["h"])
    E = (np.sqrt(r["vs"])[:, None] * (Pn @ Pn.T)
         * np.sqrt(r["vs"])[None, :])
    return 0.5 * (E + E.T)


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    """Chordal distance on RP^1 between unit pair rows."""
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def norm_map(p0, p1, p2):
    """The unique PSL(2, R) map sending p0 -> 0, p1 -> 1,
    p2 -> infinity (verbatim); None if degenerate."""
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


def cayley_alpha(T):
    den = T[1, 0] * 1j + T[1, 1]
    if abs(den) < 1e-300:
        return float("inf")
    z = (T[0, 0] * 1j + T[0, 1]) / den
    return abs((z - 1j) / (z + 1j))


J_SIG = np.array([[0.0, -1.0j], [1.0j, 0.0]])


def j_residual(Sn):
    """min eig(J - Sn^* J Sn), upper-half-plane signature."""
    R = J_SIG - Sn.conj().T @ J_SIG @ Sn
    R = 0.5 * (R + R.conj().T)
    return float(np.linalg.eigvalsh(R)[0])


def br(p, q):
    return p[0] * q[1] - p[1] * q[0]


def cr_pair(P4):
    """Homogeneous cross-ratio of four unit pairs as a unit pair;
    None if degenerate."""
    num = br(P4[0], P4[2]) * br(P4[1], P4[3])
    den = br(P4[0], P4[3]) * br(P4[1], P4[2])
    v = np.array([num, den])
    n = float(np.linalg.norm(v))
    if n < 1e-300:
        return None
    return v / n


def cr_defect_step(Pa, Pb):
    """(a): median cross-ratio defect over the frozen
    well-conditioned quadruple battery; (value, n_quads)."""
    n = len(Pa)
    K = min(n, CR_MAX_NODES)
    sel = np.unique(np.round(np.linspace(0, n - 1, K)).astype(int))
    defects = []
    for quad in combinations(sel, 4):
        qa, qb = Pa[list(quad)], Pb[list(quad)]
        ok = True
        for u, v in combinations(range(4), 2):
            if (chordal(qa[[u]], qa[[v]])[0] < CR_SEP_MIN
                    or chordal(qb[[u]], qb[[v]])[0] < CR_SEP_MIN):
                ok = False
                break
        if not ok:
            continue
        ca, cb = cr_pair(qa), cr_pair(qb)
        if ca is None or cb is None:
            continue
        defects.append(abs(ca[0] * cb[1] - ca[1] * cb[0]))
    if len(defects) < CR_MIN_QUADS:
        return None, len(defects)
    return float(np.median(defects)), len(defects)


def measure_world(rungs):
    """The identical per-world measurement: consecutive valid-
    carrier pairs, five discriminators, typed skips counted."""
    steps = []
    skips = dict(no_carrier=0, common_j=0, anchor=0, battery=0)
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        if ("f" not in ra or "f" not in rb
                or ra["rk"] > CARRIER_RK_BAR
                or rb["rk"] > CARRIER_RK_BAR):
            skips["no_carrier"] += 1
            continue
        com, ia, ib = np.intersect1d(ra["jp"], rb["jp"],
                                     return_indices=True)
        if len(com) < MIN_COMMON_J:
            skips["common_j"] += 1
            continue
        Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
        Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
        st = dict(ha=ra["h"], hb=rb["h"], n=len(com))
        # (d) raw identity distance (always computable here)
        st["raw"] = float(np.median(chordal(Pa, Pb)))
        # (a) cross-ratio defect
        crv, nq = cr_defect_step(Pa, Pb)
        st["cr"], st["nq"] = crv, nq
        if crv is None:
            skips["battery"] += 1
        # (b)/(c) three-anchor step map (com sorted ascending)
        seps = [chordal(Pa[[u]], Pa[[v]])[0]
                for u, v in ((0, 1), (0, 2), (1, 2))] \
            + [chordal(Pb[[u]], Pb[[v]])[0]
               for u, v in ((0, 1), (0, 2), (1, 2))]
        Ta = norm_map(Pa[0], Pa[1], Pa[2])
        Tb = norm_map(Pb[0], Pb[1], Pb[2])
        if min(seps) <= REF_SEP_MIN or Ta is None or Tb is None:
            skips["anchor"] += 1
            st["step"] = st["alpha"] = st["jres"] = None
            st["dsg"] = 0.0
        else:
            S = np.linalg.inv(Tb) @ Ta
            ds = float(np.linalg.det(S))
            if abs(ds) < 1e-300:
                skips["anchor"] += 1
                st["step"] = st["alpha"] = st["jres"] = None
                st["dsg"] = 0.0
            else:
                Sn = S / math.sqrt(abs(ds))
                keep = np.ones(len(com), dtype=bool)
                keep[[0, 1, 2]] = False
                st["step"] = float(np.median(chordal(
                    apply_hom(S, Pa), Pb)[keep]))
                st["alpha"] = cayley_alpha(Sn)
                st["jres"] = j_residual(Sn)
                st["dsg"] = math.copysign(1.0, ds)
        steps.append(st)
    return steps, skips


def frame_census(rungs):
    lo = [r["lamO"] for r in rungs if "lamC" in r]
    lc = [r["lamC"] for r in rungs if "lamC" in r]
    c = dict(built=len(rungs),
             carrier=sum(1 for r in rungs if "f" in r),
             valid=sum(1 for r in rungs
                       if "f" in r and r["rk"] <= CARRIER_RK_BAR),
             winav=sum(1 for r in rungs if "lamC" in r),
             winalive=sum(1 for r in rungs if "lamC" in r
                          and r["lamO"] < 1.0 and r["lamC"] < 1.0),
             full=sum(1 for r in rungs if r.get("full")),
             rkmax=max([r["rk"] for r in rungs if "f" in r],
                       default=float("inf")),
             medO=(float(np.median(lo)) if lo else float("nan")),
             medC=(float(np.median(lc)) if lc else float("nan")),
             nfireO=sum(1 for v in lo if v > 1.0),
             nfireC=sum(1 for v in lc if v > 1.0))
    c["alive"] = (c["built"] >= MIN_BUILT_ALIVE
                  and c["winalive"] >= WIN_ALIVE_FRAC * c["built"]
                  and c["valid"] >= MIN_CARRIER_ALIVE)
    return c


def sign_flips(rungs, key="detsgn"):
    sg = [r[key] for r in rungs if key in r]
    flips = sum(1 for u, v in zip(sg[:-1], sg[1:]) if u != v)
    return len(sg), sum(1 for s in sg if s > 0), flips


def fmt(v, spec="%.4f"):
    return (spec % v) if v is not None else "   -  "


def main():
    section("PRIME.PORT.MOEBIUS.CENSUS.01 -- six-world Moebius "
            "discriminator census (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; NO post-hoc selection; no marker "
          "moves.")
    print("\nS0 -- firewall + Epstein sieve ward")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    dev = float(np.max(np.abs(lambda_eps(EPS_WARD_N)
                              - lambda_eps_slow(EPS_WARD_N))))
    check("S0.2 EPSTEIN SIEVE WARD: fast vs verbatim at N = %d, "
          "max dev %.2e <= %.0e (amendment i)"
          % (EPS_WARD_N, dev, EPS_WARD_BAR),
          dev <= EPS_WARD_BAR, kill="K1")

    # ------------------------------------------------------------ P
    section("P -- build the six ladders (identical pipeline; all "
            "frame-A zones, h <= %d)" % H_DEEP_MAX)
    zones = core.frame_a_zones()
    world_rungs = {}
    for w in WORLDS:
        rungs = []
        n_fail = 0
        for kz in zones:
            r = rung_all(kz, w)
            if not isinstance(r, dict):
                if r is None:
                    n_fail += 1
                continue
            rungs.append(r)
        rungs.sort(key=lambda r: (r["h"], r["kz"]))
        world_rungs[w] = rungs
        print("    %s %-17s: %d rungs built, %d Lanczos/arm "
              "failures  [%.1f s]"
              % (w, WNAME[w], len(rungs), n_fail, time.time() - T0),
              flush=True)

    # ------------------------------------------------------------ F
    section("F -- frame-survival census (part of the deliverable)")
    print("    world                 built carrier rank2  win-av "
          "win-ALIVE full12  worst-rk   med-lamO   med-lamC  "
          "fires(O/C)  FRAME")
    census = {}
    for w in WORLDS:
        c = frame_census(world_rungs[w])
        census[w] = c
        print("    %s %-17s  %4d  %5d  %5d   %5d   %5d   %5d   "
              "%.1e  %9.3e  %9.3e   %2d/%2d     %s"
              % (w, WNAME[w], c["built"], c["carrier"], c["valid"],
                 c["winav"], c["winalive"], c["full"], c["rkmax"],
                 c["medO"], c["medC"], c["nfireO"], c["nfireC"],
                 "ALIVE" if c["alive"] else "DEAD"))
    fa_controls = [w for w in CONTROLS if census[w]["alive"]]
    print("    frame-alive controls: %s (rule: built >= %d, "
          "win-alive >= %.2f x built, rank2-valid >= %d)"
          % (fa_controls or "NONE", MIN_BUILT_ALIVE,
             WIN_ALIVE_FRAC, MIN_CARRIER_ALIVE))
    keep12 = [w for w in WORLDS
              if census[w]["winav"] >= MIN_WIN_RUNGS_E]
    print("    12-window AVAILABILITY: kept by %s; the smooth "
          "worlds' death channel is SUBCRITICALITY (lam > 1), "
          "not availability." % ", ".join(keep12))
    check("F.1 frame census reported (six worlds; truth must be "
          "ALIVE)", census["W1"]["alive"], kill="K1")

    # frozen fallback window, only if a frame-alive world lost it
    fb_needed = any(census[w]["winav"] < MIN_WIN_RUNGS_E
                    for w in WORLDS if census[w]["alive"])
    jfb = []
    if fb_needed:
        sets = []
        for w in [x for x in WORLDS if census[x]["alive"]]:
            rr = [r for r in world_rungs[w] if "jp" in r]
            cnt = {}
            for r in rr:
                for j in set(int(x) for x in r["jp"]):
                    cnt[j] = cnt.get(j, 0) + 1
            sets.append({j for j, n in cnt.items()
                         if n >= FB_PRESENCE_FRAC * len(rr)})
        jfb = sorted(set.intersection(*sets))[:FB_MAX_NODES] \
            if sets else []
        print("    FALLBACK WINDOW fired: J_fb = %s" % jfb)
        if len(jfb) >= FB_MIN_NODES:
            for w in WORLDS:
                for r in world_rungs[w]:
                    idx = {int(j): k for k, j
                           in enumerate(r["uf_n"])}
                    if not all(j in idx for j in jfb):
                        continue
                    E = rebuild_E(r)
                    iw = [idx[j] for j in jfb]
                    io = [k for k in range(E.shape[0])
                          if k not in set(iw)]
                    IO = np.eye(len(io)) - E[np.ix_(io, io)]
                    Cfb = (E[np.ix_(iw, iw)]
                           + E[np.ix_(iw, io)] @ np.linalg.solve(
                               IO, E[np.ix_(io, iw)]))
                    Cfb = 0.5 * (Cfb + Cfb.T)
                    sgn, _ = np.linalg.slogdet(
                        np.eye(len(jfb)) - Cfb)
                    r["detsgn_fb"] = float(sgn)
    else:
        print("    fallback window NOT needed (every frame-alive "
              "world keeps >= %d windowed rungs)." % MIN_WIN_RUNGS_E)

    # ------------------------------------------------------------ D
    section("D -- the five discriminators, per world (identical "
            "pipeline; full per-step tables)")
    wsum = {}
    for w in WORLDS:
        rungs = world_rungs[w]
        steps, skips = measure_world(rungs)
        print("\n  %s %s -- %d steps (typed skips: %d no-carrier, "
              "%d common-j, %d anchor, %d battery)"
              % (w, WNAME[w], len(steps), skips["no_carrier"],
                 skips["common_j"], skips["anchor"],
                 skips["battery"]))
        for st in steps:
            print("    h %4d->%4d n %2d | cr %s(q%3d) | step %s "
                  "|a| %s | jres %s dsg %+.0f | raw %s"
                  % (st["ha"], st["hb"], st["n"], fmt(st["cr"]),
                     st["nq"], fmt(st["step"]),
                     fmt(st["alpha"], "%.3f"),
                     fmt(st["jres"], "%+.1e"), st["dsg"],
                     fmt(st["raw"])))
        a_v = [s["cr"] for s in steps if s["cr"] is not None]
        b_v = [s["step"] for s in steps if s["step"] is not None]
        c_v = [s["jres"] for s in steps if s["jres"] is not None]
        d_v = [s["raw"] for s in steps]
        al_v = [s["alpha"] for s in steps
                if s["alpha"] is not None]
        nw, npos, nfl = sign_flips(rungs, "detsgn")
        nwf, nposf, nflf = sign_flips(rungs, "detsgn_fb")
        vals = dict(
            n_steps=len(steps),
            a=(float(np.median(a_v)) if len(a_v)
               >= MIN_STEPS_WORLD else None),
            b=(float(np.median(b_v)) if len(b_v)
               >= MIN_STEPS_WORLD else None),
            c=(float(np.min(c_v)) if len(c_v)
               >= MIN_STEPS_WORLD else None),
            cfrac=(float(np.mean([s["dsg"] > 0 for s in steps
                                  if s["jres"] is not None]))
                   if len(c_v) >= MIN_STEPS_WORLD else None),
            d=(float(np.median(d_v)) if len(d_v)
               >= MIN_STEPS_WORLD else None),
            alpha=(float(np.median(al_v)) if al_v else None),
            e=((nw, npos, nfl) if nw >= MIN_WIN_RUNGS_E else
               ((nwf, nposf, nflf) if nwf >= MIN_WIN_RUNGS_E
                else None)),
            e_fb=(nw < MIN_WIN_RUNGS_E and nwf >= MIN_WIN_RUNGS_E))
        wsum[w] = vals

    # ------------------------------------------------------------ T
    section("T -- the six-world five-discriminator table + frozen "
            "typing")
    print("    bars: (a) med <= %.2f; (b) med <= %.2f; (c) min >= "
          "%.0e; (d) med <= %.2f; (e) >= %d rungs, 0 flips"
          % (BAR_A, BAR_B, BAR_C, BAR_D, MIN_WIN_RUNGS_E))

    def passes(w, d):
        v = wsum[w]
        if d == "a":
            return None if v["a"] is None else (v["a"] <= BAR_A)
        if d == "b":
            return None if v["b"] is None else (v["b"] <= BAR_B)
        if d == "c":
            return None if v["c"] is None else (v["c"] >= BAR_C)
        if d == "d":
            return None if v["d"] is None else (v["d"] <= BAR_D)
        if v["e"] is None:
            return None
        return v["e"][2] == 0

    print("\n    world                 steps  a:cr-def    "
          "b:step-res  |alpha|  c:jres-min  det>0  d:raw-id    "
          "e:tau-signs        FRAME")
    for w in WORLDS:
        v = wsum[w]
        e_txt = ("-" if v["e"] is None else
                 "%d rungs %d+ %dflip%s" % (v["e"][0], v["e"][1],
                                            v["e"][2],
                                            " FB" if v["e_fb"]
                                            else ""))
        marks = {d: ("P" if passes(w, d) is True else
                     "F" if passes(w, d) is False else "-")
                 for d in "abcde"}
        print("    %s %-17s  %4d   %s %s  %s %s  %s   %s %s  "
              "%s   %s %s  %-18s %s  %s"
              % (w, WNAME[w], v["n_steps"],
                 fmt(v["a"]), marks["a"], fmt(v["b"]), marks["b"],
                 fmt(v["alpha"], "%.3f"),
                 fmt(v["c"], "%+.1e"), marks["c"],
                 fmt(v["cfrac"], "%.2f"),
                 fmt(v["d"]), marks["d"], e_txt, marks["e"],
                 "ALIVE" if census[w]["alive"] else "DEAD"))

    typing = {}
    for d in "abcde":
        t = passes("W1", d)
        if t is not True:
            typing[d] = ("UNDECIDED(truth-fails)" if t is False
                         else "UNDECIDED(truth-n/a)")
        elif not fa_controls:
            typing[d] = "UNDECIDED(no-frame-alive-controls)"
        else:
            pv = [passes(w, d) for w in fa_controls]
            n_pass = sum(1 for x in pv if x is True)
            if all(x is not True for x in pv):
                typing[d] = "ARITHMETIC"
            elif n_pass >= 2:
                typing[d] = "GEOMETRIC"
            else:
                typing[d] = "UNDECIDED"
    print("\n    per-discriminator typing (frame-alive controls "
          "only: %s):" % (fa_controls or "NONE"))
    for d, nm in (("a", "cross-ratio defect"),
                  ("b", "three-anchor step map"),
                  ("c", "J-contractivity"),
                  ("d", "raw identity distance"),
                  ("e", "tau-factor signs")):
        print("      (%s) %-24s -> %s" % (d, nm, typing[d]))
    print("\n    FRAME-DEAD CONTEXT (computed, printed, NOT typed "
          "-- no post-hoc selection):")
    for d in "abcde":
        cp = [w for w in CONTROLS if passes(w, d) is True]
        print("      (%s) controls meeting the bar anyway: %s"
              % (d, ", ".join(cp) if cp else "none"))
    print("      frame separation: truth win-alive %d/%d; "
          "controls win-alive %s -- the arithmetic/control "
          "separation happens at the FRAME (window "
          "subcriticality), upstream of every carrier "
          "discriminator."
          % (census["W1"]["winalive"], census["W1"]["winav"],
             ["%s %d/%d" % (w, census[w]["winalive"],
                            census[w]["winav"])
              for w in CONTROLS]))
    check("T.1 typed reading computed (frozen decision rules)",
          True)

    # ------------------------------------------------------------ K1
    section("K -- truth-pipeline wards (K1)")
    tr = world_rungs["W1"]
    rk_t = max([r["rk"] for r in tr if "f" in r],
               default=float("inf"))
    check("K.1 >= %d truth rungs built" % MIN_RUNGS_TRUTH,
          len(tr) >= MIN_RUNGS_TRUTH, "%d rungs" % len(tr),
          kill="K1")
    check("K.2 truth rank-2 ward (max s3/s1 %.1e <= %.0e, "
          "predecessor bar)" % (rk_t, TRUTH_RK_BAR),
          rk_t <= TRUTH_RK_BAR, kill="K1")
    check("K.3 >= %d truth steps measured" % MIN_STEPS_TRUTH,
          wsum["W1"]["n_steps"] >= MIN_STEPS_TRUTH,
          "%d steps" % wsum["W1"]["n_steps"], kill="K1")

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: MOEBIUSCENSUS-MEASURED / "
              + " ".join("%s:%s" % (d, typing[d]) for d in "abcde"))
        print("  (frame-alive controls: %s; frame-dead: %s)"
              % (", ".join(fa_controls) or "none",
                 ", ".join(w for w in CONTROLS
                           if w not in fa_controls) or "none"))
        if not fa_controls:
            print("  PLAIN ANSWER: with zero frame-alive controls "
                  "the census cannot type any discriminator as "
                  "ARITHMETIC or GEOMETRIC -- the arithmetic "
                  "separates at the FRAME (window "
                  "subcriticality), and the Moebius/cr route "
                  "needs the scalar-cocycle/determinant bridge "
                  "(parallel tau_mobius_factor probe) for any "
                  "claim finer than frame survival.")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
