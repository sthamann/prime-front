#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""carrier_cauchy_identity_probe -- PRIME.PORT.CARRIER.CAUCHY.01
(EXPLORATION ONLY, experiments/; round 47, the direct sequel to the
round-46 CARRIER-INVARIANT finding: is the port carrier EXACTLY the
Cauchy transform of the window's negative-arm measure, PER RUNG, as
a static source-derived identity?  2026-08-09).

THE QUESTION (frozen): moebius_source_step_probe found that the
PSL(2,R)-normalized carrier m_h = g/f (IIKS generator ratio of
[Y, I - D_P] at the port nodes) is rung-INVARIANT (per-rung
deviation from the pointwise median m_* has ladder median 0.0001,
sharpening with depth), and that m_* matches the Cauchy transform
of the NEGATIVE-ARM measure at the deepest rung (chordal 0.0295,
self-atom excluded, Moebius-normalized comparison).  THE TARGET
IDENTITY: m_h(y_j) == C_nu(y_j) := sum_{k != j} nu~_k / (y_k - y_j)
(the discrete Cauchy/Hilbert transform of the negative-arm masses
at the nodes, self-atom excluded), PER RUNG, up to ONE global
Moebius gauge for the whole ladder (frozen by three reference
values, see G below).  The content: the IIKS generators of the
dressed port are then source-derived in closed form,
f_j g_k - g_j f_k = (y_j - y_k) x (a known source expression) --
a static identification that replaces dynamics.

THE LADDER (frozen, predecessor verbatim): all frame-A zones
(core.frame_a_zones()) with h <= 900, sorted by (h, kz) -- the 42
reachable rungs.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
all bars frozen before the run):

 W   PIPELINE WARDS (predecessor verbatim): W1 >= 30 rungs and
     exactly 42 (the predecessor's count); W2 [Y, D_P] rank 2 on
     every rung (s3/s1 <= 1e-10).

 S1  REPRODUCTION WARD (kill -> WARD-BROKEN): rebuild the
     predecessor's direct-invariance machinery verbatim (J* at
     presence >= 0.90 with the 0.90 -> 0.80 -> 0.70 availability
     rule, reference triple = three smallest J* indices, per-rung
     three-point normalization, pointwise chordal median m_*) and
     its candidate (C) at the reference rung.  The ladder median
     of the per-rung deviation from m_* must reproduce 0.0001 and
     the candidate-C value must reproduce 0.0295, both within the
     print-rounding radius 5.001e-5 (the predecessor persists its
     numbers only at print precision; the machinery is verbatim,
     so the reproduction is bit-level in fact and the ward bar is
     the rounding radius -- documented amendment, predecessor
     precedent).

 I1  PER-RUNG MATCH: per rung, extract the carrier at the port
     nodes (machinery verbatim) and compute C_nu(y_j) from the
     rung's OWN deployed negative-arm masses (the same folded
     negative-arm objects the wall uses; self-atom excluded at
     |y_k - y_j| <= 1e-12).  BOTH node-set variants are computed
     and printed on every run: (PORT) the sum runs over the port
     nodes only (masses vs restricted to the port block); (FULL)
     the sum runs over the full negative-arm window.  FROZEN
     DECISION RULE (stated in advance): the variant with the
     smaller deviation at the deepest scored rung is the frozen
     candidate for typing; the other is the report.  GAUGE (the
     strong form, ONE global gauge for the whole ladder): the
     carrier's antisymmetric-factorization gauge is intrinsically
     per-rung (GL(2) freedom of C = f g^T - g f^T), so the global
     gauge is realized as (a) the per-rung three-point
     normalization at the FROZEN J* reference triple -> (0,1,inf)
     on the carrier side (one ladder-wide convention, predecessor
     verbatim), plus (b) ONE fixed normalization map G on the
     C_nu side, frozen from the deepest scored rung's three C_nu
     reference values -- so the C_nu ladder is NOT re-fitted per
     rung; any rung-drift of C_nu at the reference nodes shows up
     as deviation.  Per-rung deviation = median chordal over the
     rung's non-reference port nodes; full table printed.
     TYPED (frozen bars): CAUCHY-IDENTIFIED iff the deep-half
     median (deepest half of scored rungs by h) <= 0.01 AND every
     per-rung deviation <= 0.05; CAUCHY-ASYMPTOTIC iff not
     IDENTIFIED but the four depth-quartile bin medians are
     nonincreasing (slack 5e-5) and the deepest bin median
     <= 0.01 (an h -> infinity identification -- still a theorem
     seed); CAUCHY-PARTIAL iff deep-half median <= 0.05; else
     CAUCHY-DEAD.

 I2  CLOSED-FORM GENERATOR TEST (the payoff; computed and printed
     on every run, SCORED only if I1 types IDENTIFIED or
     ASYMPTOTIC -- fail-first preserved): under the identity the
     dressed-port off-diagonal is D_P[j,k] = w_j w_k
     (C_nu(y_j) - C_nu(y_k)) / (y_j - y_k) with unknown gauge
     weights w.  HONEST VERSION: fit NO weights -- test the
     GAUGE-FREE consequence instead: the double ratios
     R_{jklm} = (M_jk M_lm) / (M_jl M_km) of the off-diagonal
     entries cancel ALL w's AND any Moebius gauge on the carrier
     (the per-node Moebius denominators (c m + d) enter M rank-one
     per node and cancel in R exactly like the w's).  Frozen
     census: per rung, the 8 smallest port alias indices, all
     C(8,4) = 70 canonical quadruples j<k<l<m; R measured from
     D_P's off-diagonal vs R predicted from
     s[j,k] = (C_nu(y_j) - C_nu(y_k)) / (y_j - y_k) (frozen I1
     candidate variant); degenerate quadruples (any needed entry
     < 1e-13 x the median absolute off-diagonal of its own
     matrix) are skipped and counted.  Per-quadruple deviation =
     chordal |R_m - R_p| / sqrt((1+R_m^2)(1+R_p^2)); per-rung
     census median; TYPED GENERATOR-CLOSED iff the median of the
     per-rung census medians on the deep half <= 1e-3; else
     GENERATOR-OPEN (reported).

 I3  HERGLOTZ / POSITIVITY READING (report, honest, NO bar):
     C_nu with POSITIVE masses nu~ is (minus) a Herglotz-type
     function off the nodes.  IF I1+I2 held exactly, the
     off-diagonal of the dressed port would be a Loewner-type
     matrix of a monotone source function -- sign-definite
     quadratic-form statements about the OFF-DIAGONAL would
     follow from source positivity alone.  What would still NOT
     follow: the wall is the full matrix INCLUDING the diagonal,
     and the diagonal law was the Loewner probe's break point.
     RECHECK here, reported WITHOUT a bar as the named open piece
     (DIAGONAL-OPEN): (I - D_P)_{jj} vs the derivative sum
     sum_{k != j} nu~_k / (y_k - y_j)^2 (frozen I1 candidate
     variant): per-rung Pearson correlation and median ratio,
     deepest-rung node table printed.

 I4  CONTROLS (kz 9, must fire): Epstein (lambda_eps recursion
     comb) + scramble (seed 1).  Fire channels vs the TRUTH
     ladder, reported per control: FRAME (window unavailable or
     I - E_out indefinite or lam(C_J) > 1, predecessor verbatim)
     or INVARIANCE-BREAK (frame survives but the control
     carrier's deviation from the truth m_* exceeds 10 x the
     truth ladder's median deviation).  Silent on both channels
     -> CONTROL-DEAD.  CRITICAL SECOND READOUT (mandated): the
     controls also have negative-arm masses and nodes -- test
     whether each LIVE control's carrier matches its OWN C_nu
     (self-contained per-rung Moebius comparison: its three
     smallest port alias indices as references, both sides
     normalized by their own values there, median chordal on the
     rest; frozen bar 0.05).  If a live control ALSO matches its
     own C_nu, the identification is STRUCTURAL (gauge-level) and
     the ARITHMETIC lives elsewhere -- in the masses/nodes
     themselves; this is still fine (the wall value comes from
     the masses) but must be SAID PLAINLY.  TYPED:
     IDENTITY-STRUCTURAL (some live control self-matches) /
     IDENTITY-ARITHMETIC (live controls fail their own C_nu) /
     IDENTITY-UNRESOLVED(FRAME-DEAD) (no control survives to be
     tested).

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW the S1
reproduction ward breaks -> WARD-BROKEN; K3 controls silent ->
CONTROL-DEAD.

VERDICT (frozen enum): CAUCHYID-MEASURED with typed sublabels
CAUCHY-IDENTIFIED / CAUCHY-ASYMPTOTIC / CAUCHY-PARTIAL /
CAUCHY-DEAD (I1, with the frozen variant named), GENERATOR-CLOSED
/ GENERATOR-OPEN (I2, scored only in the IDENTIFIED/ASYMPTOTIC
branch), IDENTITY-STRUCTURAL / IDENTITY-ARITHMETIC /
IDENTITY-UNRESOLVED (I4); else PIPELINE-BROKEN / WARD-BROKEN /
CONTROL-DEAD.

SPEC v2 AMENDMENTS (documented before the run; fail-first
preserved): (i) the reproduction ward anchors on the predecessor's
PRINTED numbers (0.0001 / 0.0295 / 42 rungs) at rounding radius
5.001e-5 -- full-precision values are not persisted (predecessor
precedent); (ii) rung_all is extended with bookkeeping fields vp
(port-block negative-arm masses) and DP (dressed-port matrix) --
bookkeeping only, physics verbatim; (iii) the prompt's "one global
Moebius gauge" is concretized as I1's (a)+(b) split because the
carrier side carries an intrinsic per-rung GL(2) ambiguity while
the C_nu side is gauge-rigid -- the single frozen map G lives on
the rigid side; (iv) both I1 node-set variants and the full I2
census print on every run and are scored only per the frozen
rules; (v) I3 is a bar-free report by mandate (named open piece);
(vi) POST-HOC RECONCILIATION REPORT (added after run 1, which
typed CAUCHY-DEAD on the frozen protocol -- typing, bars and the
frozen decision rule are UNCHANGED, fail-first preserved): the
round-46 candidate-(C) match (0.0295) was measured on the 8
non-reference J* alias nodes only, while I1 scores ALL port
nodes; to reconcile, the I1 table additionally prints the
J*-restricted per-rung deviation for both variants, and the
deepest rung prints its per-node deviation profile vs alias
index -- report only, showing WHERE the identity lives (the J*
alias core) and where it dies (the rest of the port).

NO RH claim -- a per-rung Cauchy identification of the normalized
carrier is a numerical measurement on compressed truncations, not
a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; carrier machinery
verbatim from moebius_source_step_probe.py
(PRIME.PORT.MOEBIUS.SOURCE.01) which carries it verbatim from
port_schur_cocycle_probe.py (PRIME.PORT.SCHURSTEP.01) and the
SPEC v2 IIKS extraction of port_riemann_hilbert_setup_probe.py;
port_loewner_identity_probe (the diagonal break point, context).
IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/carrier_cauchy_identity_probe.py
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
MIN_COMMON_J = 8
RANK_BAR = 1e-10
CTRL_KZ = 9
JSTAR_FRACS = (0.90, 0.80, 0.70)
MIN_JSTAR = 6
SELF_EPS = 1e-12

# S1 reproduction ward anchors (predecessor's printed numbers).
REF_N_RUNGS = 42
REF_MED_DEV = 0.0001
REF_CAND_C = 0.0295
ROUND_TOL = 5.001e-5

# I1 frozen bars.
I1_DEEP_BAR = 0.01
I1_ALL_BAR = 0.05
I1_PART_BAR = 0.05
N_BINS = 4
MONO_SLACK = 5e-5

# I2 frozen census.
NQ_NODES = 8
I2_BAR = 1e-3
GUARD_REL = 1e-13

# I4 frozen bars.
CTRL_SELF_BAR = 0.05
CTRL_INV_FACTOR = 10.0

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
    """FROZEN GAUGE (lax2 verbatim; the normalization quotients it
    out exactly)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, **kw):
    """One heavy build per rung (predecessor verbatim), plus
    bookkeeping fields vp and DP (amendment ii)."""
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
    out = dict(kz=kz, h=h, alpha=b["alpha"], M=b["M"], D=D,
               uu=b["uu"], mm=b["mm"], xs=xs, ws=ws, ys=ys, vs=vs,
               lamE=float(np.linalg.eigvalsh(E)[-1]))
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
        out["vp"] = vs[ip]
        out["DP"] = DP
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


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
    p2 -> infinity (homogeneous); None if degenerate (verbatim)."""
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


def chordal_median(pairs_list):
    """The chordal median on RP^1 of a list of unit pairs
    (verbatim)."""
    P = np.stack(pairs_list)
    D = np.abs(P[:, None, 0] * P[None, :, 1]
               - P[:, None, 1] * P[None, :, 0])
    return P[int(np.argmin(np.sum(D, axis=1)))]


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


# ------------------------------------------- Cauchy-transform sources
def cauchy_at(nodes, masses, y):
    """C_nu(y) = sum_k nu_k / (x_k - y), self-atom excluded at
    |x_k - y| <= SELF_EPS (predecessor's exclusion, verbatim)."""
    d = np.asarray(nodes, float) - float(y)
    m = np.abs(d) > SELF_EPS
    return float(np.sum(np.asarray(masses, float)[m] / d[m]))


def cauchy_vec(nodes, masses, yv):
    return np.array([cauchy_at(nodes, masses, y) for y in yv])


def dcauchy_vec(nodes, masses, yv):
    """The derivative sum sum_k nu_k / (x_k - y)^2, self-atom
    excluded (I3)."""
    out = []
    for y in yv:
        d = np.asarray(nodes, float) - float(y)
        m = np.abs(d) > SELF_EPS
        out.append(float(np.sum(
            np.asarray(masses, float)[m] / d[m] ** 2)))
    return np.array(out)


def cnu_variant(r, variant):
    """The two frozen node-set variants of C_nu at the port nodes."""
    if variant == "PORT":
        return cauchy_vec(r["yp"], r["vp"], r["yp"])
    return cauchy_vec(r["ys"], r["vs"], r["yp"])


# ------------------------------------------- I2 double-ratio census
def double_ratio_census(Moff, Spred, idx):
    """All canonical quadruples j<k<l<m of the node positions idx;
    R = (M_jk M_lm)/(M_jl M_km) measured vs predicted; chordal
    deviation per quadruple.  Returns (devs, n_skipped)."""
    def med_off(A):
        v = np.abs(A[np.ix_(idx, idx)])
        v = v[~np.eye(len(idx), dtype=bool)]
        return float(np.median(v))

    gm = GUARD_REL * med_off(Moff)
    gs = GUARD_REL * med_off(Spred)
    devs = []
    n_skip = 0
    for j, k, l, m in combinations(idx, 4):
        em = (Moff[j, k], Moff[l, m], Moff[j, l], Moff[k, m])
        es = (Spred[j, k], Spred[l, m], Spred[j, l], Spred[k, m])
        if (min(abs(x) for x in em) < gm
                or min(abs(x) for x in es) < gs):
            n_skip += 1
            continue
        rm = (em[0] * em[1]) / (em[2] * em[3])
        rp = (es[0] * es[1]) / (es[2] * es[3])
        devs.append(abs(rm - rp)
                    / math.sqrt((1.0 + rm * rm) * (1.0 + rp * rp)))
    return devs, n_skip


def deep_half(vals):
    """Median over the deepest half of an h-ordered value list."""
    n = len(vals)
    return float(np.median(np.asarray(vals[n // 2:], float)))


def main():
    section("PRIME.PORT.CARRIER.CAUCHY.01 -- is the carrier the "
            "Cauchy transform of the negative arm, per rung? "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; v563 READ-ONLY.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the ladder (all frame-A zones, h <= %d; "
            "machinery verbatim)" % H_DEEP_MAX)
    rungs = []
    rk_max = 0.0
    for kz in core.frame_a_zones():
        r = rung_all(kz)
        if not isinstance(r, dict):
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 %.1e"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"], rk_max))
    check("W1 rung count %d == %d (>= %d)"
          % (len(rungs), REF_N_RUNGS, MIN_RUNGS),
          len(rungs) == REF_N_RUNGS and len(rungs) >= MIN_RUNGS,
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= %.0e)"
          % (rk_max, RANK_BAR), rk_max <= RANK_BAR, kill="K1")

    # ------------------------------------------------------------ S1
    section("S1 -- reproduction ward (predecessor invariance "
            "machinery verbatim; radius %.1e)" % ROUND_TOL)
    all_jp = [set(int(j) for j in r.get("jp", [])) for r in rungs]
    jstar, used_frac = [], None
    for fr in JSTAR_FRACS:
        cand = sorted(j for j in set().union(*all_jp)
                      if sum(j in s for s in all_jp)
                      >= fr * len(rungs))
        if len(cand) >= MIN_JSTAR:
            jstar, used_frac = cand, fr
            break
    check("S1.0 ladder-wide node set J* built (|J*| %d >= %d at "
          "presence >= %.2f)" % (len(jstar), MIN_JSTAR,
                                 used_frac or 0.0),
          len(jstar) >= MIN_JSTAR, kill="K1")
    if len(jstar) < MIN_JSTAR:
        return finish(None)
    refs = jstar[:3]
    print("    J* = %s; reference triple %s -> (0, 1, inf)"
          % (jstar, refs))
    norm_carriers = {}
    n_skip_inv = 0
    for irx, r in enumerate(rungs):
        jp = list(r.get("jp", []))
        if not all(j in jp for j in refs):
            n_skip_inv += 1
            continue
        pos = {int(j): k for k, j in enumerate(jp)}
        P = unit_pairs(r["g"], r["f"])
        Tn = norm_map(P[pos[refs[0]]], P[pos[refs[1]]],
                      P[pos[refs[2]]])
        if Tn is None:
            n_skip_inv += 1
            continue
        norm_carriers[irx] = dict(
            N=apply_hom(Tn, P), pos=pos)
    mstar = {}
    for j in jstar:
        vals = [nc["N"][nc["pos"][j]]
                for nc in norm_carriers.values() if j in nc["pos"]]
        if len(vals) >= 3:
            mstar[j] = chordal_median(vals)
    devs_mstar = []
    for irx in sorted(norm_carriers):
        nc = norm_carriers[irx]
        dd = [float(chordal(nc["N"][[nc["pos"][j]]],
                            mstar[j][None, :])[0])
              for j in jstar[3:] if j in nc["pos"] and j in mstar]
        if dd:
            devs_mstar.append(float(np.median(dd)))
    med_dev = (float(np.median(devs_mstar)) if devs_mstar
               else float("inf"))
    print("    per-rung deviation from m_*: %s (%d rungs, %d "
          "typed skips)" % (quart(devs_mstar), len(devs_mstar),
                            n_skip_inv))
    # ---- candidate (C) at the reference rung (verbatim)
    ref_irx = max((irx for irx in norm_carriers),
                  key=lambda irx: rungs[irx]["h"], default=None)
    cand_c = float("inf")
    if ref_irx is not None:
        rr = rungs[ref_irx]
        pos = norm_carriers[ref_irx]["pos"]
        nodes = [j for j in jstar if j in pos and j in mstar]
        yv = np.array([rr["yp"][pos[j]] for j in nodes])
        deep = rungs[max(range(len(rungs)),
                         key=lambda i: rungs[i]["h"])]
        vC = cauchy_vec(deep["ys"], deep["vs"], yv)
        Pc = unit_pairs(vC, np.ones(len(vC)))
        i0, i1, i2 = (nodes.index(refs[0]), nodes.index(refs[1]),
                      nodes.index(refs[2]))
        Tn = norm_map(Pc[i0], Pc[i1], Pc[i2])
        if Tn is not None:
            Nc = apply_hom(Tn, Pc)
            dd = [float(chordal(Nc[[k]],
                                mstar[nodes[k]][None, :])[0])
                  for k in range(len(nodes))
                  if nodes[k] not in refs]
            cand_c = float(np.median(dd))
        print("    reference rung h %d kz %d; candidate (C) "
              "deepest-measure Cauchy vs m_* = %.4f"
              % (rr["h"], rr["kz"], cand_c))
    check("S1.1 REPRODUCTION WARD: |med dev - %.4f| = %.1e <= "
          "%.1e AND |cand C - %.4f| = %.1e <= %.1e"
          % (REF_MED_DEV, abs(med_dev - REF_MED_DEV), ROUND_TOL,
             REF_CAND_C, abs(cand_c - REF_CAND_C), ROUND_TOL),
          abs(med_dev - REF_MED_DEV) <= ROUND_TOL
          and abs(cand_c - REF_CAND_C) <= ROUND_TOL, kill="KW")

    # ------------------------------------------------------------ I1
    section("I1 -- PER-RUNG MATCH: m_h vs C_nu (both variants; one "
            "global gauge)")
    print("    gauge: carrier per-rung three-point normalized at "
          "refs %s (ladder-wide" % (refs,))
    print("    convention); C_nu side normalized by ONE fixed map "
          "G frozen from the deepest")
    print("    scored rung's three C_nu reference values (per "
          "variant).  self-atom excluded")
    print("    at |y_k - y_j| <= %.0e." % SELF_EPS)
    variants = ("PORT", "FULL")
    Gmap = {}
    rr = rungs[ref_irx]
    pos_ref = norm_carriers[ref_irx]["pos"]
    for v in variants:
        cv = cnu_variant(rr, v)
        Pc = unit_pairs(cv, np.ones(len(cv)))
        Gmap[v] = norm_map(Pc[pos_ref[refs[0]]],
                           Pc[pos_ref[refs[1]]],
                           Pc[pos_ref[refs[2]]])
    check("I1.0 global gauge maps G frozen at the deepest scored "
          "rung (h %d kz %d)" % (rr["h"], rr["kz"]),
          all(Gmap[v] is not None for v in variants), kill="K1")
    if not all(Gmap[v] is not None for v in variants):
        return finish(None)

    dev_tab = {v: [] for v in variants}   # h-ordered per-rung devs
    jdev_tab = {v: [] for v in variants}  # J*-restricted (report)
    scored = []                           # (irx, h)
    jset = set(jstar[3:])
    print("\n    h    kz   nodes   dev PORT   dev FULL   "
          "[J* only: PORT   FULL]")
    for irx in sorted(norm_carriers):
        r = rungs[irx]
        nc = norm_carriers[irx]
        test_j = [j for j in r["jp"] if int(j) not in refs]
        if len(test_j) < 1:
            continue
        row, jrow = {}, {}
        for v in variants:
            cv = cnu_variant(r, v)
            Nc = apply_hom(Gmap[v], unit_pairs(
                cv, np.ones(len(cv))))
            dd = {int(j): float(chordal(
                nc["N"][[nc["pos"][int(j)]]],
                Nc[[nc["pos"][int(j)]]])[0]) for j in test_j}
            row[v] = float(np.median(list(dd.values())))
            dev_tab[v].append(row[v])
            jd = [d for j, d in dd.items() if j in jset]
            jrow[v] = (float(np.median(jd)) if jd
                       else float("nan"))
            jdev_tab[v].append(jrow[v])
        scored.append((irx, r["h"]))
        print("    %4d %4d   %3d    %8.4f   %8.4f    %8.4f  "
              "%8.4f"
              % (r["h"], r["kz"], len(test_j),
                 row["PORT"], row["FULL"],
                 jrow["PORT"], jrow["FULL"]))
    for v in variants:
        print("    ladder %s: %s   deep-half med %.4f   max %.4f"
              % (v, quart(dev_tab[v]), deep_half(dev_tab[v]),
                 float(np.max(dev_tab[v]))))
    for v in variants:
        jv = [x for x in jdev_tab[v] if not math.isnan(x)]
        print("    J*-restricted %s (report only, round-46 "
              "reconciliation): %s   deep-half med %.4f"
              % (v, quart(jv), deep_half(jv)))
    # post-hoc report: per-node profile at the deepest scored rung
    r = rungs[ref_irx]
    nc = norm_carriers[ref_irx]
    print("\n    deepest-rung per-node deviation profile "
          "(h %d kz %d, report only):" % (r["h"], r["kz"]))
    prof = {}
    for v in variants:
        cv = cnu_variant(r, v)
        Nc = apply_hom(Gmap[v], unit_pairs(cv, np.ones(len(cv))))
        prof[v] = [float(chordal(nc["N"][[k]], Nc[[k]])[0])
                   for k in range(len(r["jp"]))]
    print("      j:      " + "".join("%7d" % int(j)
                                     for j in r["jp"][:16]))
    for v in variants:
        print("      %s:  " % ("%-5s" % v)
              + "".join("%7.3f" % d for d in prof[v][:16]))
    for v in variants:
        tail = prof[v][16:]
        if tail:
            print("      %s beyond j=%d: %s"
                  % (v, int(r["jp"][15]), quart(tail)))
    # frozen decision: better variant at the deepest scored rung
    frozen_v = min(variants, key=lambda v: dev_tab[v][-1])
    other_v = "FULL" if frozen_v == "PORT" else "PORT"
    print("    FROZEN DECISION (deepest rung dev %s %.4f vs %s "
          "%.4f): candidate = %s, report = %s"
          % (frozen_v, dev_tab[frozen_v][-1], other_v,
             dev_tab[other_v][-1], frozen_v, other_v))

    dv = dev_tab[frozen_v]
    dh = deep_half(dv)
    mx = float(np.max(dv))
    bins = np.array_split(np.asarray(dv, float), N_BINS)
    bmed = [float(np.median(b)) for b in bins]
    mono = all(bmed[i] >= bmed[i + 1] - MONO_SLACK
               for i in range(N_BINS - 1))
    print("    depth-quartile bin medians (%s): %s  "
          "(nonincreasing: %s)"
          % (frozen_v, "  ".join("%.4f" % b for b in bmed), mono))
    if dh <= I1_DEEP_BAR and mx <= I1_ALL_BAR:
        i1_label = "CAUCHY-IDENTIFIED(%s)" % frozen_v
    elif mono and bmed[-1] <= I1_DEEP_BAR:
        i1_label = "CAUCHY-ASYMPTOTIC(%s)" % frozen_v
    elif dh <= I1_PART_BAR:
        i1_label = "CAUCHY-PARTIAL(%s)" % frozen_v
    else:
        i1_label = "CAUCHY-DEAD(%s)" % frozen_v
    check("I1.1 typed: %s (deep-half med %.4f vs %.2f; max %.4f "
          "vs %.2f; deepest bin %.4f)"
          % (i1_label, dh, I1_DEEP_BAR, mx, I1_ALL_BAR, bmed[-1]),
          True)

    # ------------------------------------------------------------ I2
    section("I2 -- CLOSED-FORM GENERATOR TEST (gauge-free double "
            "ratios; frozen variant %s)" % frozen_v)
    print("    per rung: 8 smallest port alias indices, all "
          "C(8,4) = 70 quadruples;")
    print("    R = (M_jk M_lm)/(M_jl M_km) from D_P off-diagonal "
          "vs from s[j,k] =")
    print("    (C_nu(y_j) - C_nu(y_k))/(y_j - y_k); all w's and "
          "any carrier Moebius cancel.")
    cen_meds = []
    cen_all = []
    n_skip_tot = 0
    n_rung_skip = 0
    print("\n    h    kz   quads  skipped  census med")
    for irx, _h in scored:
        r = rungs[irx]
        n = len(r["jp"])
        if n < NQ_NODES:
            n_rung_skip += 1
            continue
        idx = list(range(NQ_NODES))       # jp ascending -> smallest
        cv = cnu_variant(r, frozen_v)
        yp = r["yp"]
        S = np.zeros((n, n))
        for a in range(n):
            d = yp - yp[a]
            d[a] = 1.0
            S[a, :] = (cv - cv[a]) / d
            S[a, a] = 0.0
        devs, nsk = double_ratio_census(r["DP"], S, idx)
        n_skip_tot += nsk
        if not devs:
            n_rung_skip += 1
            continue
        cen_meds.append(float(np.median(devs)))
        cen_all.extend(devs)
        print("    %4d %4d   %4d   %4d     %.2e"
              % (r["h"], r["kz"], len(devs), nsk, cen_meds[-1]))
    cen_dh = deep_half(cen_meds) if cen_meds else float("inf")
    print("    census: %d quadruples over %d rungs (%d skipped "
          "quads, %d skipped rungs)"
          % (len(cen_all), len(cen_meds), n_skip_tot, n_rung_skip))
    if cen_all:
        print("    full census: %s;  per-rung medians deep-half "
              "med %.2e" % (quart(cen_all), cen_dh))
    i2_scored = i1_label.startswith(("CAUCHY-IDENTIFIED",
                                     "CAUCHY-ASYMPTOTIC"))
    i2_label = ("GENERATOR-CLOSED" if cen_dh <= I2_BAR
                else "GENERATOR-OPEN")
    if not i2_scored:
        print("    (I1 typed %s -> I2 printed but NOT scored; "
              "fail-first preserved)" % i1_label)
    check("I2.1 %s: deep-half census med %.2e vs bar %.0e (%s)"
          % (i2_label, cen_dh, I2_BAR,
             "scored" if i2_scored else "report only"), True)

    # ------------------------------------------------------------ I3
    section("I3 -- HERGLOTZ / POSITIVITY READING (report, NO bar; "
            "named open piece)")
    print("    IF I1+I2 held exactly: C_nu with positive masses "
          "is (minus) a Herglotz-type")
    print("    function off the nodes, so the dressed-port "
          "OFF-DIAGONAL would be a")
    print("    Loewner-type matrix of a monotone source function "
          "-- off-diagonal sign/")
    print("    definiteness statements would follow from source "
          "positivity alone.")
    print("    What would NOT follow: the wall is the FULL matrix "
          "with the diagonal, and")
    print("    the diagonal law was the Loewner probe's break "
          "point.  Recheck (frozen")
    print("    variant %s): (I - D_P)_jj vs sum_{k != j} nu_k / "
          "(y_k - y_j)^2." % frozen_v)
    corrs, ratios = [], []
    for irx, _h in scored:
        r = rungs[irx]
        lhs = 1.0 - np.diag(r["DP"])
        if frozen_v == "PORT":
            rhs = dcauchy_vec(r["yp"], r["vp"], r["yp"])
        else:
            rhs = dcauchy_vec(r["ys"], r["vs"], r["yp"])
        if (len(lhs) >= 3 and float(np.std(lhs)) > 0.0
                and float(np.std(rhs)) > 0.0):
            corrs.append(float(np.corrcoef(lhs, rhs)[0, 1]))
        m = np.abs(lhs) > 1e-300
        if np.any(m):
            ratios.append(float(np.median(rhs[m] / lhs[m])))
    print("    per-rung Pearson corr((I-D_P)_jj, deriv-sum): %s"
          % quart(corrs))
    print("    per-rung median ratio deriv-sum / (I-D_P)_jj: %s"
          % quart(ratios))
    rd = rungs[ref_irx]
    lhs = 1.0 - np.diag(rd["DP"])
    rhs = (dcauchy_vec(rd["yp"], rd["vp"], rd["yp"])
           if frozen_v == "PORT"
           else dcauchy_vec(rd["ys"], rd["vs"], rd["yp"]))
    print("    deepest-rung node table (h %d kz %d, first 10 "
          "nodes):" % (rd["h"], rd["kz"]))
    print("      j     y_j       (I-D_P)_jj    deriv-sum     "
          "ratio")
    for k in range(min(10, len(lhs))):
        print("      %-4d %+.4f   %+.4e   %+.4e   %+.3e"
              % (int(rd["jp"][k]), rd["yp"][k], lhs[k], rhs[k],
                 rhs[k] / lhs[k] if abs(lhs[k]) > 1e-300
                 else float("nan")))
    check("I3.1 diagonal comparison reported WITHOUT a bar "
          "(DIAGONAL-OPEN, the named open piece)", True)

    # ------------------------------------------------------------ I4
    section("I4 -- controls (kz %d, must fire; plus the mandated "
            "structural-vs-arithmetic readout)" % CTRL_KZ)
    ok = True
    live_self = {}
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
        if "jp" not in rc:
            print("    %-8s: frame alive but carrier unavailable "
                  "-> fires via FRAME" % nmc)
            continue
        # ---- fire channel (a): invariance break vs truth m_*
        fired = False
        jp = list(rc["jp"])
        if all(j in jp for j in refs):
            pos = {int(j): k for k, j in enumerate(jp)}
            P = unit_pairs(rc["g"], rc["f"])
            Tn = norm_map(P[pos[refs[0]]], P[pos[refs[1]]],
                          P[pos[refs[2]]])
            if Tn is not None:
                N = apply_hom(Tn, P)
                dd = [float(chordal(N[[pos[j]]],
                                    mstar[j][None, :])[0])
                      for j in jstar[3:]
                      if j in pos and j in mstar]
                if dd:
                    dev_c = float(np.median(dd))
                    fired = dev_c > CTRL_INV_FACTOR * med_dev
                    print("    %-8s: frame ALIVE; carrier dev vs "
                          "truth m_* %.4f vs bar %.4f -> %s via "
                          "INVARIANCE-BREAK"
                          % (nmc, dev_c,
                             CTRL_INV_FACTOR * med_dev,
                             "fires" if fired else "SILENT"))
        if not fired and not all(j in jp for j in refs):
            print("    %-8s: frame alive but reference triple "
                  "absent -> fires via FRAME" % nmc)
            fired = True
        ok &= fired
        # ---- readout (b): self-match vs its OWN C_nu (mandated)
        if len(jp) >= 7:
            crefs = jp[:3]
            pos = {int(j): k for k, j in enumerate(jp)}
            P = unit_pairs(rc["g"], rc["f"])
            Ts = norm_map(P[0], P[1], P[2])
            cv = cnu_variant(rc, frozen_v)
            Pc = unit_pairs(cv, np.ones(len(cv)))
            Tc = norm_map(Pc[0], Pc[1], Pc[2])
            if Ts is not None and Tc is not None:
                Ns = apply_hom(Ts, P)
                Nc = apply_hom(Tc, Pc)
                dd = [float(chordal(Ns[[k]], Nc[[k]])[0])
                      for k in range(3, len(jp))]
                live_self[nmc] = float(np.median(dd))
                print("    %-8s: SELF-MATCH vs own C_nu(%s): dev "
                      "%.4f vs bar %.2f -> %s"
                      % (nmc, frozen_v, live_self[nmc],
                         CTRL_SELF_BAR,
                         "MATCHES (structural)"
                         if live_self[nmc] <= CTRL_SELF_BAR
                         else "fails (arithmetic)"))
            else:
                print("    %-8s: self-match degenerate reference "
                      "triple -> untested" % nmc)
        else:
            print("    %-8s: too few port nodes (%d) for "
                  "self-match -> untested" % (nmc, len(jp)))
    check("C1 CONTROLS FIRE (frame death or invariance break on "
          "both controls)", ok, kill="K3")
    if not live_self:
        i4_label = "IDENTITY-UNRESOLVED(FRAME-DEAD)"
        print("    STRUCTURAL-VS-ARITHMETIC: no control survives "
              "to self-match -> UNRESOLVED.")
    elif any(v <= CTRL_SELF_BAR for v in live_self.values()):
        who = ",".join(n for n, v in live_self.items()
                       if v <= CTRL_SELF_BAR)
        i4_label = "IDENTITY-STRUCTURAL(%s)" % who
        print("    STRUCTURAL-VS-ARITHMETIC: said plainly -- the "
              "control's carrier ALSO matches")
        print("    its OWN C_nu, so the Cauchy identification is "
              "STRUCTURAL (gauge-level, a")
        print("    property of the dressed-port construction); "
              "the ARITHMETIC lives in the")
        print("    masses/nodes nu~, y themselves.  The wall "
              "value still comes from the")
        print("    masses -- the identity remains useful as a "
              "closed form, not as an")
        print("    arithmetic discriminator.")
    else:
        i4_label = "IDENTITY-ARITHMETIC"
        print("    STRUCTURAL-VS-ARITHMETIC: live controls FAIL "
              "their own C_nu -- the")
        print("    identification does not transfer to foreign "
              "combs; it is specific to the")
        print("    arithmetic window (IDENTITY-ARITHMETIC).")
    check("I4.1 typed: %s (self-match devs: %s)"
          % (i4_label,
             ", ".join("%s %.4f" % (n, v)
                       for n, v in live_self.items()) or "none"),
          True)

    return finish(dict(i1=i1_label, i2=i2_label,
                       i2_scored=i2_scored, i4=i4_label,
                       dh=dh, mx=mx, cen_dh=cen_dh,
                       med_dev=med_dev))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("CAUCHYID-MEASURED / %s / %s%s / %s"
                   % (labels["i1"], labels["i2"],
                      "" if labels["i2_scored"]
                      else " (report only)", labels["i4"]))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (I1 deep-half med %.4f, max %.4f; I2 deep-half "
              "census med %.2e; truth m_* med dev %.4f; diagonal "
              "= DIAGONAL-OPEN, the named open piece)"
              % (labels["dh"], labels["mx"], labels["cen_dh"],
                 labels["med_dev"]))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
