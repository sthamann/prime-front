#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mobius_crossratio_firewall_probe -- PRIME.PORT.MOEBIUS.
CRFIREWALL.01 (EXPLORATION ONLY, experiments/; round 48, reviewer
probes 1 + 6: is the Moebius structure of the port carrier ladder
REAL -- cross-ratio invariance, three-anchor holdout
determination, cocycle composition -- or a least-squares
artifact?, 2026-08-09).

THE QUESTION (frozen): port_schur_cocycle_probe fitted one
Moebius map per rung to the PSL(2,R)-NORMALIZED carrier (median
residual 0.0015); moebius_source_step_probe then typed the
normalized carrier CARRIER-INVARIANT.  The reviewer's worry: the
per-rung three-point normalization pins 3 of ~11 nodes and can
MANUFACTURE identity; the TLS fit can absorb noise.  This probe
uses NO per-rung normalization anywhere.  THE PRINCIPLE:
cross-ratios are Moebius-invariant, so if the step is truly
Moebius NO gauge is needed at all -- cr equality across rungs,
exact three-anchor determination with holdout prediction, and
cocycle composition are all decidable FIT-FREE in the raw
carrier coordinate.

THE RAW COORDINATE (honesty note, frozen): the carrier pairs
(g_j, f_j) carry ONLY the frozen SPEC v2 extraction gauge (the
SO(2) rotation pinning the deepest port node, lax2 verbatim --
machinery, not a per-step fit; the SVD basis of the degenerate
singular pair is otherwise arbitrary, so the gauge is what makes
the frame deterministic).  The gauge acts as a chordal ISOMETRY
of RP^1 and a Moebius map, hence F1 (cross-ratios), F2 (holdout
errors) and F3 (projective distances) are EXACTLY gauge-free;
only the F4 raw-identity readout is stated 'in the frozen
extraction gauge' and is flagged as such.

THE LADDER (frozen, port_schur_cocycle verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
rung pairs at ladder separation k with >= 8 common port alias
indices (typed skips counted); k in {1, 2, 4, 5, 8} (k = 1 is
the truth battery; k = 5 is the reviewer's mismatched-pair null;
the k-law distinguishes 'one global function' (flat in k) from
'smooth flow' (growing in k) fit-free).

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; all bars frozen before the run):

 F1  CROSS-RATIO INVARIANCE: per rung pair, the frozen battery
     of well-conditioned quadruples of common nodes: if the pair
     carries more than 16 common nodes, subsample 16 node
     indices evenly across the sorted common list
     (round(linspace), deterministic -- full-range coverage, no
     depth bias); enumerate ALL quadruples of the selected
     nodes; CONDITIONING (frozen, applied on BOTH rungs): reject
     if the min pairwise chordal separation within the quadruple
     < 1e-3 x the within-quadruple chordal spread, or if |cr|
     lies outside [1e-3, 1e3] on either rung; keep the 200
     BEST-CONDITIONED survivors (ranked by min pairwise chordal
     separation, min over both rungs; deterministic tie-break by
     lexicographic index order).  cr is the homogeneous
     cross-ratio cr(p_i, p_j; p_k, p_l) = (d_ik d_jl)/(d_il
     d_jk) with signed 2x2 determinants d_ab = det[p_a p_b].
     Invariance defect per quadruple: Dcr = |cr_{h'} - cr_h| /
     (1 + |cr_h|).  Report per-step (median, q90, max) and the
     POOLED ladder distribution at k = 1.  TYPED: CR-INVARIANT
     iff pooled median <= 1e-3 AND pooled q90 <= 1e-2
     (certificate level); CR-APPROX iff pooled median <= 0.02;
     CR-DEAD otherwise.  DEEP-CORE SUB-BATTERY (report-only,
     never typed): the same battery restricted to the 8 DEEPEST
     common nodes (smallest alias indices) -- prints WHERE any
     cr-coherence lives if the full-coverage battery dies.  THE k-LAW (reviewer null (b),
     concretized fit-free): the same battery at k = 2, 4, 5, 8;
     pooled median per k; printed ratio med(k=8)/med(k=1) with
     the frozen reading: <= 2 -> ladder-global (one function);
     > 2 -> grows with separation (smooth flow); k = 5 is the
     mismatch null quoted against k = 1.

 F2  THREE-ANCHOR HOLDOUT: per k = 1 step, anchor triples =
     combinations of common nodes, conditioned like F1 (min
     pairwise chordal >= 1e-3 x within-triple spread on both
     rungs, non-degenerate three-point normalizers); the PRIMARY
     triple is the one maximizing the min pairwise chordal
     separation (min over both rungs; deterministic tie-break by
     lexicographic index order).  The step map is determined
     EXACTLY (closed form, no fit): M = N_b^{-1} N_a where N_a,
     N_b send the anchor values to (0, 1, inf).  Holdout error =
     chordal(M p_a, p_b) on all NON-anchor common nodes; per-step
     median, ladder median over steps.  ANCHOR STABILITY: over
     the top-60 conditioned triples (by score, deterministic),
     the pairwise projective distance of the exact maps d_P(A, B)
     = min_lambda ||A - lambda B||_F / ||A||_F = |sin angle(A,
     B)|; per-step median, ladder median.  TYPED: ANCHOR-STABLE
     iff ladder median holdout <= 3e-3 AND ladder median d_P <=
     1e-2; ANCHOR-FRAGILE otherwise (the reviewer kill: the map
     depends on the anchor choice).

 F3  COCYCLE COMPOSITION (reviewer probe 6): the exact primary
     three-anchor maps must compose in the raw coordinate:
     d_P(M_{h->h+2}, M_{h+1->h+2} M_{h->h+1}) on all consecutive
     triples, and the k-step transfers d_P(M_{h->h+4}, product
     of the four unit steps); all direct maps use the SAME
     frozen primary-anchor rule on their own pair.  TYPED:
     COCYCLE-EXACT iff the pooled median d_P (k = 2 and k = 4
     comparisons together) <= 1e-2; COCYCLE-BROKEN otherwise
     (41 independent local fits, not a cocycle).

 F4  SIGNIFICANCE ANATOMY (reviewer section 4; report, no
     score): per k = 1 step print the chordal spread of the
     common-node carrier values (region size), the median
     pairwise chordal (are the points on a tiny arc?), the
     numerical precision floor of the carrier (the SVD rank-2
     defect s3/s1 of the commutator extraction, worse rung of
     the pair), the RAW identity residual median
     chordal(p_h, p_{h'}) (frozen extraction gauge, NO
     normalization), and the TLS fitted-map residual (fit on all
     common nodes, residual median over all -- reference only).
     THE SETTLING LINE (frozen reading, three-way): RAW-
     INVARIANT iff the ladder median raw identity <= 3 x the
     ladder median fit residual AND <= 0.02 absolute -- then the
     un-normalized carrier is ALREADY rung-invariant, stronger
     and gauge-free, settling the tautology worry in the
     POSITIVE direction; RAW-NEITHER iff raw identity <= 3 x fit
     residual but BOTH are poor (> 0.02 absolute) -- then in the
     raw coordinate neither identity nor any single Moebius map
     captures the step, and the predecessor's tiny normalized
     residual was manufactured by the three-point pinning (the
     reviewer's worry CONFIRMED); RAW-MOVES otherwise (the
     fitted step carries real content beyond identity).

 C   CONTROLS: (C1, kz 9, must fire) Epstein (lambda_eps
     recursion comb) + scramble (seed 1): frame death (window
     unavailable or I - E_out indefinite or lam(C_J) > 1),
     channel reported; silent -> CONTROL-DEAD.  (C2, the frame-
     SURVIVING control, decisive): the SMOOTH-MASS world --
     masses 2 e^{u/2} du on the TRUE prime-power lattice
     (lattice_parametrix B1 verbatim; the frame is geometry-
     driven, so its window/port machinery is expected to exist:
     VERIFIED and reported per rung).  Build the full smooth
     ladder, run F1 (k = 1 battery) and F2 (primary holdout) on
     it.  TYPED REPORT: SMOOTH-FRAME-DEAD (< 10 measured smooth
     steps -- no answer); SMOOTH-CARRIES-CR iff the smooth
     pooled k = 1 cr-defect median <= 0.02 (then the cr-
     invariance is GEOMETRIC -- the lattice + smooth masses
     already carry it); SMOOTH-CR-DEAD otherwise (then it is
     ARITHMETIC -- the actual Lambda masses are load-bearing).
     If the TRUTH full-coverage battery is itself CR-DEAD, the
     geometric-vs-arithmetic question devolves to the DEEP CORE:
     the truth vs smooth deep-core medians are printed side by
     side with the same 0.02 reading (report-only).  The smooth
     world is a physics answer, not a kill channel.

 W   PIPELINE WARDS: W1 >= 30 rungs built; W2 [Y, D_P] rank 2 on
     every truth rung (s3/s1 <= 1e-10); W3 >= 30 k = 1 steps
     with a non-empty quadruple battery.

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; K3 the C1
controls are silent -> CONTROL-DEAD.

VERDICT (frozen enum): CRFIREWALL-MEASURED with typed sublabels
CR-INVARIANT / CR-APPROX / CR-DEAD (F1), ANCHOR-STABLE /
ANCHOR-FRAGILE (F2), COCYCLE-EXACT / COCYCLE-BROKEN (F3), and
the C2 report label SMOOTH-CARRIES-CR / SMOOTH-CR-DEAD /
SMOOTH-FRAME-DEAD; else PIPELINE-BROKEN / CONTROL-DEAD.

SPEC v2 AMENDMENTS (documented before the run; fail-first
preserved): (i) the conditioning rule is concretized in the
CHORDAL metric (min pairwise chordal < 1e-3 x within-tuple
spread rejected, applied on both rungs) -- the affine
|r_a - r_b| rule is chart-dependent and breaks at f ~ 0 nodes,
which are regular points of RP^1; (ii) the battery is frozen
deterministically: even-coverage node subsample (16 of n if
n > 16), full quadruple enumeration on the subsample, top 200
survivors by conditioning score -- REPLACES the first-draft
lexicographic accept order, which on deep rungs (up to 53
common nodes) tested almost only the deepest nodes and
FLATTERED the invariance; the coverage rule makes F1 strictly
harder (fail-first preserved); anchor triples capped at the top
60 by conditioning score; (iii) the reviewer's affine-only null
(b) is realized as the frozen k-separation law (the prompt's
own simplification), with k = 5 as the explicit mismatched-pair
null; (iv) the raw coordinate carries the frozen one-point
SO(2) extraction gauge (machinery verbatim, a chordal isometry
-- F1/F2/F3 are exactly gauge-free, F4's raw identity is
flagged); (v) the smooth-mass control reuses build_rung with
the B1 masses via a bookkeeping flag (physics verbatim from
lattice_parametrix_probe); (vi) the F4 positive settlement
carries an ABSOLUTE smallness bar (0.02) on top of the factor-3
comparison -- the first draft's relative-only rule would have
typed 'raw-invariant' when identity and fit are equally POOR,
which is the opposite of a positive settlement (bar added
before scoring; strictly harder, fail-first preserved); (vii)
the DEEP-CORE sub-battery (8 deepest common nodes) is printed
REPORT-ONLY on truth and smooth ladders -- it is exactly the
sub-region the first-draft bias accidentally tested, kept as
anatomy so the probe itself localizes any surviving coherence;
typing stays on the full-coverage battery.

NO RH claim -- cross-ratio invariance of a compressed-truncation
carrier is a numerical measurement, not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; carrier extraction
verbatim from port_schur_cocycle_probe.py (PRIME.PORT.
SCHURSTEP.01, itself SPEC v2 of port_riemann_hilbert_setup);
normalization warning from moebius_source_step_probe.py
(PRIME.PORT.MOEBIUS.SOURCE.01); smooth-mass B1 world from
lattice_parametrix_probe.py (PRIME.PORT.LATTICE.PARAMETRIX.01).
IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mobius_crossratio_firewall_probe.py
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
MIN_RUNGS = 30
MIN_STEPS = 30
MIN_COMMON_J = 8
RANK_BAR = 1e-10
CTRL_KZ = 9

K_SEPS = (1, 2, 4, 5, 8)          # k=1 truth; k=5 mismatch null
COND_SEP_FRAC = 1e-3              # within-tuple conditioning
CR_ABS_LO, CR_ABS_HI = 1e-3, 1e3  # |cr| window (both rungs)
QUAD_NODE_CAP = 16                # even-coverage node subsample
QUAD_ACCEPT_CAP = 200             # best-conditioned survivors
DEEP_CORE_N = 8                   # deep-core sub-battery (report)
MAX_TRIPLES = 60
CR_INV_MED = 1e-3
CR_INV_Q90 = 1e-2
CR_APPROX_MED = 0.02
K_FLAT_FACTOR = 2.0               # k-law reading (report-only)
HOLDOUT_BAR = 3e-3
DP_STAB_BAR = 1e-2
COCYCLE_BAR = 1e-2
RAWID_FACTOR = 3.0                # F4 settling line (report-only)
RAWID_ABS = 0.02                  # F4 absolute smallness bar
SMOOTH_MIN_STEPS = 10
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


def cell_widths(uu):
    """Midpoint cells (lattice_parametrix verbatim; smooth world)."""
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def build_rung(kz, scramble_seed=None, comb=None, smooth=False):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if smooth:
        # B1 world: smooth masses 2 e^{u/2} du on the TRUE lattice
        mm = 2.0 * np.exp(uu / 2.0) * cell_widths(uu)
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
    """FROZEN EXTRACTION GAUGE (lax2 verbatim): the SO(2) rotation
    pinning the deepest port node.  A chordal isometry and a
    Moebius map -- F1/F2/F3 are exactly gauge-free (see docstring
    honesty note)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, **kw):
    """One heavy build per rung (port_schur_cocycle verbatim): the
    negative-arm Gram E feeds the 12-index window compression (the
    controls' frame channel) and the dressed-port IIKS generators."""
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
    out = dict(kz=kz, h=h, alpha=b["alpha"],
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    # ---- window compression (frame channel, verbatim)
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
        out["jp"], out["yp"] = uf_n[ip], ys[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    """Raw carrier pairs p_j = (g_j, f_j), unit length; NO
    normalization anywhere in this probe."""
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    """Chordal distance on RP^1 between unit pair rows."""
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def chord_mat(P):
    """Full pairwise chordal matrix (battery conditioning)."""
    return np.abs(P[:, None, 0] * P[None, :, 1]
                  - P[:, None, 1] * P[None, :, 0])


def norm_map(p0, p1, p2):
    """The unique PSL(2, R) map sending p0 -> 0, p1 -> 1,
    p2 -> infinity (verbatim).  Used ONLY inside the exact
    three-anchor step map M = N_b^{-1} N_a -- never to normalize
    the carrier."""
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
    """TLS Moebius fit (verbatim) -- F4 REFERENCE ONLY, never used
    to type F1/F2/F3."""
    rows = np.stack([P[:, 0] * Q[:, 1], P[:, 1] * Q[:, 1],
                     -P[:, 0] * Q[:, 0], -P[:, 1] * Q[:, 0]],
                    axis=1)
    _u, _s, Vh = np.linalg.svd(rows)
    a, b, c, d = Vh[-1]
    T = np.array([[a, b], [c, d]])
    return T, chordal(apply_hom(T, P), Q)


def sdet(p, q):
    """Signed 2x2 determinant det[p q] on homogeneous pairs."""
    return float(p[0] * q[1] - p[1] * q[0])


def cross_ratio(P, i, j, k, l):
    """Homogeneous cross-ratio cr(p_i, p_j; p_k, p_l)."""
    den = sdet(P[i], P[l]) * sdet(P[j], P[k])
    if abs(den) < 1e-300:
        return None
    return (sdet(P[i], P[k]) * sdet(P[j], P[l])) / den


def d_proj(A, B):
    """Projective distance d_P(A, B) = min_lambda ||A - lambda B||_F
    / ||A||_F = |sin angle(A, B)| (symmetric, scale-free)."""
    na = float(np.linalg.norm(A))
    nb = float(np.linalg.norm(B))
    if na < 1e-300 or nb < 1e-300:
        return 1.0
    c = float(np.sum(A * B)) / (na * nb)
    return math.sqrt(max(0.0, 1.0 - c * c))


def pair_pairs(ra, rb):
    """Raw unit pairs on the sorted common port alias indices of a
    rung pair; None if < MIN_COMMON_J common nodes."""
    com, ia, ib = np.intersect1d(ra.get("jp", []),
                                 rb.get("jp", []),
                                 return_indices=True)
    if len(com) < MIN_COMMON_J:
        return None
    Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
    Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
    return Pa, Pb, com


def quad_battery(Pa, Pb, deep_core=False):
    """F1 frozen battery: even-coverage node subsample (no depth
    bias), full quadruple enumeration on the subsample, top
    QUAD_ACCEPT_CAP survivors by conditioning score (min pairwise
    chordal, min over both rungs); returns the defect list and the
    reject count.  deep_core=True restricts to the DEEP_CORE_N
    deepest common nodes (report-only sub-battery)."""
    n = len(Pa)
    if deep_core:
        nodes = np.arange(min(DEEP_CORE_N, n))
    elif n > QUAD_NODE_CAP:
        nodes = np.unique(np.round(
            np.linspace(0, n - 1, QUAD_NODE_CAP)).astype(int))
    else:
        nodes = np.arange(n)
    Da, Db = chord_mat(Pa), chord_mat(Pb)
    cands, n_rej = [], 0
    for q in combinations(nodes.tolist(), 4):
        qi = list(q)
        score = 1.0
        ok = True
        for Dm in (Da, Db):
            sub = Dm[np.ix_(qi, qi)]
            vals = sub[np.triu_indices(4, 1)]
            spread = float(np.max(vals))
            if spread < 1e-300 or float(np.min(vals)) \
                    < COND_SEP_FRAC * spread:
                ok = False
                break
            score = min(score, float(np.min(vals)))
        if not ok:
            n_rej += 1
            continue
        cra = cross_ratio(Pa, *q)
        crb = cross_ratio(Pb, *q)
        if (cra is None or crb is None
                or not (CR_ABS_LO <= abs(cra) <= CR_ABS_HI)
                or not (CR_ABS_LO <= abs(crb) <= CR_ABS_HI)):
            n_rej += 1
            continue
        cands.append((score, q,
                      abs(crb - cra) / (1.0 + abs(cra))))
    cands.sort(key=lambda sqd: (-sqd[0], sqd[1]))
    return [d for _s, _q, d in cands[:QUAD_ACCEPT_CAP]], n_rej


def cond_triples(Pa, Pb):
    """F2 conditioned anchor triples, sorted by descending score =
    min pairwise chordal separation (min over both rungs);
    deterministic tie-break by lexicographic index order."""
    n = len(Pa)
    Da, Db = chord_mat(Pa), chord_mat(Pb)
    out = []
    for t in combinations(range(n), 3):
        ti = list(t)
        score = 1.0
        ok = True
        for Dm in (Da, Db):
            sub = Dm[np.ix_(ti, ti)]
            vals = sub[np.triu_indices(3, 1)]
            spread = float(np.max(vals))
            if spread < 1e-300 or float(np.min(vals)) \
                    < COND_SEP_FRAC * spread:
                ok = False
                break
            score = min(score, float(np.min(vals)))
        if ok:
            out.append((score, t))
    out.sort(key=lambda st: (-st[0], st[1]))
    return out


def anchor_map(Pa, Pb, t):
    """The EXACT (closed-form, fit-free) Moebius map determined by
    the three anchors t: M = N_b^{-1} N_a."""
    Na = norm_map(Pa[t[0]], Pa[t[1]], Pa[t[2]])
    Nb = norm_map(Pb[t[0]], Pb[t[1]], Pb[t[2]])
    if Na is None or Nb is None:
        return None
    M = np.linalg.solve(Nb, Na)
    return M / np.linalg.norm(M)


def primary_step(Pa, Pb):
    """The frozen primary three-anchor map of a pair; returns
    (M, triple, holdout_median, triples_list) or None."""
    tri = cond_triples(Pa, Pb)
    for score, t in tri:
        M = anchor_map(Pa, Pb, t)
        if M is None:
            continue
        keep = np.ones(len(Pa), dtype=bool)
        keep[list(t)] = False
        err = chordal(apply_hom(M, Pa), Pb)
        return M, t, float(np.median(err[keep])), tri
    return None


def q_stats(v):
    a = np.asarray(v, float)
    return (float(np.median(a)), float(np.percentile(a, 90)),
            float(np.max(a)))


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.2e  med %.2e  q75 %.2e" % tuple(q)


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


def build_ladder(smooth=False):
    rungs = []
    rk_max = 0.0
    for kz in core.frame_a_zones():
        r = rung_all(kz, smooth=smooth)
        if not isinstance(r, dict) or "f" not in r:
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    return rungs, rk_max


def k_battery(rungs, k, deep_core=False):
    """Pooled cr-defects for rung pairs at ladder separation k."""
    pooled, per_step, n_skip = [], [], 0
    for i in range(len(rungs) - k):
        pp = pair_pairs(rungs[i], rungs[i + k])
        if pp is None:
            n_skip += 1
            continue
        Pa, Pb, _com = pp
        dfs, _rej = quad_battery(Pa, Pb, deep_core=deep_core)
        if not dfs:
            n_skip += 1
            continue
        pooled.extend(dfs)
        per_step.append((rungs[i]["h"], rungs[i + k]["h"], dfs))
    return pooled, per_step, n_skip


def main():
    section("PRIME.PORT.MOEBIUS.CRFIREWALL.01 -- fit-free Moebius "
            "firewall on the raw port carrier (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; NO per-rung normalization anywhere; "
          "no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth ladder (all frame-A zones, "
            "h <= %d; machinery verbatim)" % H_DEEP_MAX)
    rungs, rk_max = build_ladder(smooth=False)
    print("    %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 %.1e"
          % (len(rungs), rungs[0]["h"] if rungs else -1,
             rungs[-1]["h"] if rungs else -1, rk_max))
    check("W1 >= %d rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= %.0e)"
          % (rk_max, RANK_BAR), rk_max <= RANK_BAR, kill="K1")

    # ------------------------------------------------------------ F1
    section("F1 -- cross-ratio invariance, raw coordinate, frozen "
            "quadruple battery")
    print("    conditioning: min pairwise chordal >= %.0e x "
          "within-quadruple spread (both rungs);" % COND_SEP_FRAC)
    print("    |cr| in [%.0e, %.0e] on both rungs; accept cap %d "
          "per pair.  Dcr = |cr' - cr|/(1 + |cr|)."
          % (CR_ABS_LO, CR_ABS_HI, QUAD_ACCEPT_CAP))
    k_pooled = {}
    for k in K_SEPS:
        pooled, per_step, n_skip = k_battery(rungs, k)
        k_pooled[k] = pooled
        if k == 1:
            print("\n    per-step battery (k = 1; %d typed skips):"
                  % n_skip)
            for ha, hb, dfs in per_step:
                m, q90, mx = q_stats(dfs)
                print("    h %3d->%3d  n_quad %3d  med %.2e  "
                      "q90 %.2e  max %.2e"
                      % (ha, hb, len(dfs), m, q90, mx))
            n_steps_k1 = len(per_step)
    check("W3 >= %d k=1 steps with non-empty battery" % MIN_STEPS,
          n_steps_k1 >= MIN_STEPS, "%d steps" % n_steps_k1,
          kill="K1")
    m1, q901, mx1 = (q_stats(k_pooled[1]) if k_pooled[1]
                     else (1.0, 1.0, 1.0))
    print("\n    POOLED ladder distribution (k = 1, %d quadruples):"
          " med %.2e  q90 %.2e  max %.2e"
          % (len(k_pooled[1]), m1, q901, mx1))
    f1_type = ("CR-INVARIANT" if (m1 <= CR_INV_MED
                                  and q901 <= CR_INV_Q90) else
               "CR-APPROX" if m1 <= CR_APPROX_MED else "CR-DEAD")
    print("    TYPED: med %.2e vs %.0e (and q90 %.2e vs %.0e) / "
          "approx bar %.2f -> %s"
          % (m1, CR_INV_MED, q901, CR_INV_Q90, CR_APPROX_MED,
             f1_type))
    dc_pooled, _dc_steps, _dc_skip = k_battery(rungs, 1,
                                               deep_core=True)
    if dc_pooled:
        dc_med, dc_q90, dc_max = q_stats(dc_pooled)
        print("    DEEP-CORE sub-battery (%d deepest common "
              "nodes, %d quadruples, REPORT-ONLY): med %.2e  "
              "q90 %.2e  max %.2e"
              % (DEEP_CORE_N, len(dc_pooled), dc_med, dc_q90,
                 dc_max))
    else:
        dc_med = float("inf")
        print("    DEEP-CORE sub-battery: no measurable "
              "quadruples")
    check("F1.1 typed: %s (fit-free, gauge-free)" % f1_type, True)
    print("\n    THE k-LAW (reviewer null: neighbor property vs "
          "one global function):")
    meds_k = {}
    for k in K_SEPS:
        if k_pooled[k]:
            mk, qk, xk = q_stats(k_pooled[k])
            meds_k[k] = mk
            print("      k = %d : %5d quadruples  med %.2e  "
                  "q90 %.2e  max %.2e%s"
                  % (k, len(k_pooled[k]), mk, qk, xk,
                     "   <- mismatch null (h vs h+5)"
                     if k == 5 else ""))
        else:
            print("      k = %d : no measurable pairs" % k)
    if 1 in meds_k and 8 in meds_k and meds_k[1] > 0:
        ratio = meds_k[8] / meds_k[1]
        print("      med(k=8)/med(k=1) = %.2f -> %s (frozen "
              "reading, factor %.0f)"
              % (ratio, "LADDER-GLOBAL (one function)"
                 if ratio <= K_FLAT_FACTOR else
                 "GROWS WITH SEPARATION (smooth flow)",
                 K_FLAT_FACTOR))
    if 1 in meds_k and 5 in meds_k:
        print("      mismatch check: med(k=5) %.2e vs med(k=1) "
              "%.2e" % (meds_k[5], meds_k[1]))

    # ------------------------------------------------------------ F2
    section("F2 -- three-anchor holdout (exact maps, no fit) + "
            "anchor stability")
    print("    primary triple: max-min chordal separation (both "
          "rungs); stability over top-%d" % MAX_TRIPLES)
    print("    conditioned triples, pairwise d_P(A, B) = "
          "|sin angle|.")
    steps = []          # (i, Pa, Pb, com, M, t, holdout)
    hold_meds, dp_meds = [], []
    n_skip = 0
    for i in range(len(rungs) - 1):
        pp = pair_pairs(rungs[i], rungs[i + 1])
        if pp is None:
            n_skip += 1
            continue
        Pa, Pb, com = pp
        ps = primary_step(Pa, Pb)
        if ps is None:
            n_skip += 1
            continue
        M, t, hold, tri = ps
        maps = []
        for _sc, tt in tri[:MAX_TRIPLES]:
            Mt = anchor_map(Pa, Pb, tt)
            if Mt is not None:
                maps.append(Mt)
        dps = [d_proj(maps[a], maps[b])
               for a in range(len(maps))
               for b in range(a + 1, len(maps))]
        dpm = float(np.median(dps)) if dps else float("inf")
        hold_meds.append(hold)
        dp_meds.append(dpm)
        steps.append(dict(i=i, Pa=Pa, Pb=Pb, com=com, M=M, t=t,
                          hold=hold))
        print("    h %3d->%3d  n %2d  anchors %-12s  holdout med "
              "%.2e  n_tri %3d  d_P med %.2e"
              % (rungs[i]["h"], rungs[i + 1]["h"], len(com),
                 str(list(t)), hold, len(maps), dpm))
    med_hold = float(np.median(hold_meds)) if hold_meds else 1.0
    med_dp = float(np.median(dp_meds)) if dp_meds else 1.0
    print("    holdout ladder: %s" % quart(hold_meds))
    print("    d_P     ladder: %s" % quart(dp_meds))
    f2_type = ("ANCHOR-STABLE" if (med_hold <= HOLDOUT_BAR
                                   and med_dp <= DP_STAB_BAR)
               else "ANCHOR-FRAGILE")
    print("    TYPED: med holdout %.2e vs %.0e AND med d_P %.2e "
          "vs %.0e -> %s"
          % (med_hold, HOLDOUT_BAR, med_dp, DP_STAB_BAR, f2_type))
    check("F2.1 typed: %s (%d steps, %d typed skips)"
          % (f2_type, len(steps), n_skip), True)

    # ------------------------------------------------------------ F3
    section("F3 -- cocycle composition of the exact three-anchor "
            "maps (raw coordinate)")
    map_cache = {}
    for s in steps:
        map_cache[(s["i"], 1)] = s["M"]
    for k in (2, 4):
        for i in range(len(rungs) - k):
            pp = pair_pairs(rungs[i], rungs[i + k])
            if pp is None:
                continue
            ps = primary_step(pp[0], pp[1])
            if ps is None:
                continue
            map_cache[(i, k)] = ps[0]
    dp_coc = []
    for k in (2, 4):
        n_cmp = 0
        vals = []
        for i in range(len(rungs) - k):
            if (i, k) not in map_cache:
                continue
            prod = np.eye(2)
            ok = True
            for j in range(k):
                if (i + j, 1) not in map_cache:
                    ok = False
                    break
                prod = map_cache[(i + j, 1)] @ prod
            if not ok:
                continue
            d = d_proj(map_cache[(i, k)], prod)
            vals.append(d)
            n_cmp += 1
            print("    h %3d ->(+%d) %3d : d_P(direct, product) "
                  "%.2e"
                  % (rungs[i]["h"], k, rungs[i + k]["h"], d))
        if vals:
            print("    k = %d summary: %d comparisons, %s"
                  % (k, n_cmp, quart(vals)))
        dp_coc.extend(vals)
    med_coc = float(np.median(dp_coc)) if dp_coc else 1.0
    f3_type = ("COCYCLE-EXACT" if med_coc <= COCYCLE_BAR
               else "COCYCLE-BROKEN")
    print("    TYPED: pooled median d_P %.2e vs %.0e -> %s "
          "(%d comparisons)"
          % (med_coc, COCYCLE_BAR, f3_type, len(dp_coc)))
    check("F3.1 typed: %s" % f3_type, True)

    # ------------------------------------------------------------ F4
    section("F4 -- significance anatomy (report; raw = frozen "
            "extraction gauge, NO normalization)")
    print("    step        spread   med-arc  prec-floor  raw-id "
          "med  fit res med")
    raw_ids, fit_res = [], []
    for s in steps:
        i = s["i"]
        Pa, Pb = s["Pa"], s["Pb"]
        Da = chord_mat(Pa)
        vals = Da[np.triu_indices(len(Pa), 1)]
        spread = float(np.max(vals))
        arc = float(np.median(vals))
        floor = max(rungs[i].get("rk", 0.0),
                    rungs[i + 1].get("rk", 0.0))
        rid = float(np.median(chordal(Pa, Pb)))
        _T, res = moebius_fit(Pa, Pb)
        fr = float(np.median(res))
        raw_ids.append(rid)
        fit_res.append(fr)
        print("    h %3d->%3d  %.3f    %.3f    %.1e     %.2e"
              "     %.2e"
              % (rungs[i]["h"], rungs[i + 1]["h"], spread, arc,
                 floor, rid, fr))
    med_rid = float(np.median(raw_ids)) if raw_ids else 1.0
    med_fit = float(np.median(fit_res)) if fit_res else 1.0
    print("    ladder: raw-id med %.2e | fit res med %.2e "
          "(settling factor %.0f, abs bar %.2f)"
          % (med_rid, med_fit, RAWID_FACTOR, RAWID_ABS))
    if med_rid <= RAWID_FACTOR * med_fit and med_rid <= RAWID_ABS:
        f4_line = ("RAW-INVARIANT: the un-normalized carrier is "
                   "already rung-invariant -- stronger and "
                   "gauge-free; the tautology worry is settled "
                   "in the POSITIVE direction (no normalization "
                   "was applied anywhere in this probe).")
    elif med_rid <= RAWID_FACTOR * med_fit:
        f4_line = ("RAW-NEITHER: raw identity is as good as the "
                   "fit but BOTH are poor -- in the raw "
                   "coordinate neither identity nor any single "
                   "Moebius map captures the step; the "
                   "predecessor's tiny normalized residual was "
                   "manufactured by the three-point pinning "
                   "(reviewer's worry CONFIRMED).")
    else:
        f4_line = ("RAW-MOVES: the raw carrier moves between "
                   "rungs; the Moebius step carries real content "
                   "beyond identity (fit beats raw identity by "
                   "more than the settling factor).")
    print("    " + f4_line)
    check("F4.1 anatomy reported (raw-id med %.2e, fit med %.2e)"
          % (med_rid, med_fit), True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C1 frame-die controls (kz %d, must fire):" % CTRL_KZ)
    ok = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        rc = rung_all(CTRL_KZ, **kw)
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
            continue
        if "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES"
                  % nmc)
            continue
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        ok &= fired
        print("    %-8s: lam(out) %.3e | lam(C_J) %.3e | lam(E) "
              "%.3e -> fires via %s"
              % (nmc, rc["lamO"], rc["lamC"], rc["lamE"],
                 "EXTERIOR" if rc["lamO"] > 1.0 else
                 "WINDOW" if rc["lamC"] > 1.0 else "NOTHING"))
    check("C1 CONTROLS FIRE (frame death on both)", ok, kill="K3")

    print("\n  C2 SMOOTH-MASS world (masses 2 e^{u/2} du on the "
          "true lattice, lattice_parametrix B1;")
    print("     frame-SURVIVING control -- geometric vs "
          "arithmetic; report-only):")
    sm_rungs, sm_rk = build_ladder(smooth=True)
    n_frame = sum(1 for r in sm_rungs if "lamC" in r)
    n_sub = sum(1 for r in sm_rungs
                if "lamC" in r and r["lamC"] <= 1.0
                and r.get("lamO", 2.0) <= 1.0)
    print("    smooth ladder: %d rungs with carrier (%d with "
          "window; %d subcritical); worst s3/s1 %.1e"
          % (len(sm_rungs), n_frame, n_sub, sm_rk))
    sm_pooled, sm_steps, sm_skip = k_battery(sm_rungs, 1)
    sm_holds = []
    for i in range(len(sm_rungs) - 1):
        pp = pair_pairs(sm_rungs[i], sm_rungs[i + 1])
        if pp is None:
            continue
        ps = primary_step(pp[0], pp[1])
        if ps is not None:
            sm_holds.append(ps[2])
    if len(sm_steps) < SMOOTH_MIN_STEPS:
        c2_label = "SMOOTH-FRAME-DEAD"
        print("    only %d measurable smooth steps (< %d) -> %s "
              "(no answer from this control)"
              % (len(sm_steps), SMOOTH_MIN_STEPS, c2_label))
    else:
        sm_med, sm_q90, sm_max = q_stats(sm_pooled)
        sm_hold_med = (float(np.median(sm_holds)) if sm_holds
                       else float("inf"))
        print("    smooth k=1 battery: %d steps, %d quadruples "
              "(%d typed skips): med %.2e  q90 %.2e  max %.2e"
              % (len(sm_steps), len(sm_pooled), sm_skip,
                 sm_med, sm_q90, sm_max))
        print("    smooth primary holdout median: %s"
              % (("%.2e" % sm_hold_med)
                 if sm_hold_med < float("inf") else "n/a"))
        c2_label = ("SMOOTH-CARRIES-CR"
                    if sm_med <= CR_APPROX_MED
                    else "SMOOTH-CR-DEAD")
        print("    TYPED REPORT: smooth cr med %.2e vs %.2f -> %s"
              % (sm_med, CR_APPROX_MED, c2_label))
        print("    reading: %s"
              % ("the cr-structure is GEOMETRIC -- the lattice "
                 "with smooth masses already carries it"
                 if c2_label == "SMOOTH-CARRIES-CR" else
                 "the cr-structure is ARITHMETIC -- the actual "
                 "Lambda masses are load-bearing"))
        if f1_type == "CR-DEAD":
            sm_dc, _s, _k = k_battery(sm_rungs, 1,
                                      deep_core=True)
            sm_dc_med = (q_stats(sm_dc)[0] if sm_dc
                         else float("inf"))
            print("    DEEP-CORE comparison (truth full battery "
                  "is CR-DEAD; report-only): truth %.2e vs "
                  "smooth %s (reading bar %.2f):"
                  % (dc_med, ("%.2e" % sm_dc_med)
                     if sm_dc_med < float("inf") else "n/a",
                     CR_APPROX_MED))
            print("      %s"
                  % ("BOTH deep cores coherent -> the surviving "
                     "deep-core cr-coherence is GEOMETRIC"
                     if (dc_med <= CR_APPROX_MED
                         and sm_dc_med <= CR_APPROX_MED) else
                     "truth deep core coherent, smooth one dead "
                     "-> the surviving deep-core cr-coherence "
                     "is ARITHMETIC"
                     if dc_med <= CR_APPROX_MED else
                     "no deep-core coherence on truth either -> "
                     "nothing survives to localize"))
    check("C2 smooth-mass control reported: %s" % c2_label, True)

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("CRFIREWALL-MEASURED / %s / %s / %s / %s"
                   % (f1_type, f2_type, f3_type, c2_label))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (F1 pooled med %.2e q90 %.2e; F2 holdout med "
              "%.2e d_P med %.2e; F3 med %.2e;"
              % (m1, q901, med_hold, med_dp, med_coc))
        print("   F4 raw-id med %.2e vs fit med %.2e)"
              % (med_rid, med_fit))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
