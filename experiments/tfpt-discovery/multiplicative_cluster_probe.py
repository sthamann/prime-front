#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""multiplicative_cluster_probe -- PRIME.CLUSTER.MULT.01
(EXPLORATION ONLY, experiments/; F5 of the 2026-08-07 evening plan:
the ALL-ORDERS route -- connected multiplicative clusters instead of
pair statistics).

THE PREMISE (frozen, read-only): the GUE strand's typed limit says
pair statistics saturate at second moments -- the true comb's
information beyond GUE is exactly what fakes lack.  The margin-law
census showed the excess is a growing cancellation (CI 5.7 -> 29.5,
diffuse at cell grade).  F5 asks whether the DIVISIBILITY GRAPH on
the window's events (nodes = prime powers; edges = shared prime
support / d | n) organizes a CLUSTER EXPANSION of the log-pivot --
the all-orders object pair correlation cannot see.

THE OBJECT: per rung the deployed corner block is A = B + sum_j
lam_j E_j (B = the arch-only structural 2x2, E_j = the per-event
read block, E_j = -Xn_j shipped; ward lambda_min(A) == tau_X ==
lambda_min(Ah)).  The log-pivot family: for a PD shift sigma,
    g_sigma(S) = log det(B + sigma I + sum_{j in S} lam_j E_j),
a set function on the event lattice.  The CLUSTER WEIGHTS are the
subset cumulants (Moebius inversion on the Boolean lattice):
    w(C) = sum_{S subset C} (-1)^{|C|-|S|} g_sigma(S),
the standard cluster/cumulant logic: (i) EXACT RESUMMATION
sum_{C} w(C) = g_sigma(full) (telescoping identity); (ii) w(C) = 0
whenever the events of C split into two non-interacting groups --
only CONNECTED correlation terms survive (the mixed-trace expansion
log det(B + sum lam_j E_j) = log det B + sum_k (-1)^{k+1}/k
tr((B^{-1} sum lam_j E_j)^k), each w(C) collecting exactly the
traces that touch EVERY member of C).  Both sympy-checked exactly,
then numeric.

THE PD FLOOR (typed before the run): the arch-only base B is
INDEFINITE at deployed scale (lambda_min(B) ~ -2.3 < 0 < tau_X),
so the expansion around the comb-blind base exists only above a
shift floor sigma_c; the sigma-ladder measures the floor and the
census runs at the smallest valid sigma* (all evaluated subsets PD).
The margin itself sits BELOW the floor -- if the census is
favorable, crossing that floor IS the control problem; typed.

THE CENSUS (kz 9 primary, orders <= 3 exhaustive; 16-event
sub-window lattice EXACT to order 16): order histogram (W1, W2,
W3, remainder R = Delta - W1 - W2 - W3 with Delta = g(full) -
g(empty)); the CONNECTIVITY split -- pair (i, j) multiplicatively
connected iff gcd(m_i, m_j) > 1 (for the prime-power comb: same
base prime; the divisibility relation coincides), 3-clusters
connected iff their gcd-graph is connected (>= 2 edges), exactly
one edge = MIXED (counted in the disconnected sector); per-sector
enrichment E2 = mean |w2| over connected pairs / mean |w2| over
disconnected pairs, sector cancellation indices CI_conn / CI_disc
(orders 2+3); per-prime connected aggregates (small primes exact);
dyadic band table (band(C) = floor(max_j u_j / ln 2) from the MASS
labels), signed band sums vs absolute mass -- band-wise coherence.

THE DISCRIMINATOR (the F5 point; anchors kz = 9, 12, 13, common
sigma* per anchor): TRUE comb (shipped reads) vs the mass-fixed
SCRAMBLE (seed 1, same mass labels, reads at scrambled positions --
the cluster structure must die if it is arithmetic) vs the h = 2
EPSTEIN comb x^2 + 5y^2 (first-ka support at own log positions,
deployed weights, unrouted -- its divisibility graph differs at the
class-group obstruction sites: composites represented while their
factors are not).  Measured per comb: E2, connected share of the
order-2 absolute mass, CI_conn / CI_disc, edge density of the
gcd-graph.

CONTROLS: the resummation ward (16-event lattice, machine
precision); the disconnected-cancellation ward (sympy exact +
float synthetic); the connected-correlation identity (sympy: the
mixed second derivative of w({i,j}) equals
-tr(B^{-1} E_i B^{-1} E_j)); tau_X / EXC regressions on the
anchors; the margin identity det A = tau_X lambda_max(A) at
sigma = 0; the read-convention ward (spline reads vs shipped Xn).

VERDICT (frozen): CLUSTERS-CARRY (connected concentration + band
summability + scramble collapse + Epstein fingerprint -- the
all-orders route has structure; the control gap typed) /
CLUSTERS-DIFFUSE (no connected concentration, E2 < 1.5 -- the
route closes; typed) / CLUSTERS-PARTIAL (bars split; typed which).
HONESTY: NO RH claim; nothing outside experiments/; no file
written; deployed-scale measurement in a 2-dim corner compression
-- a negative census closes THIS pivot's cluster route, not the
all-orders idea per se; typed in the verdict.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/multiplicative_cluster_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from itertools import combinations
from math import gcd

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.CLUSTER.MULT.01 spec v1 (2026-08-07, frozen before the run).
Object: per rung A(S) = B + sigma I + sum_{j in S} lam_j E_j with
E_j = -Xn_j (shipped) for the TRUE comb and E = -conv * spline
reads for SCR/EPS (conv from the read-convention ward, bar 1e-6
rel); g_sigma(S) = log det A(S); cluster weights w(C) =
sum_{S subset C} (-1)^{|C|-|S|} g(S).  PD shift ladder: sigma_0 =
1 + max(0, -lmin(B)) + max_comb sum_j lam_j ||E_j||_2; halving
until a census subset (orders <= 3 + full, all three combs) loses
PD (det <= 0 or tr <= 0); then 8 bisection steps; sigma* = last
valid.  Census: orders <= 3 exhaustive (triples capped 600000 --
skip typed if over); Delta = g(full) - g(empty); R = Delta - W1 -
W2 - W3.  Sub-window lattice: kz 9, first 16 events by mass, all
2^16 subsets, subset-Moebius transform; resummation ward rel 1e-8;
order histogram 1..16; geometric ratio rho_ord = median
|W_{k+1}/W_k| over k = 1..6.  Connectivity: conn2(i,j) iff
gcd(m_i, m_j) > 1 (mass labels); conn3 iff >= 2 gcd-edges; exactly
1 edge = MIXED (disconnected sector).  E2 = mean|w2|_conn /
mean|w2|_disc; CI_sector = sum|w| / |sum w| over orders 2+3 per
sector.  Bands: band(C) = floor(max_j log(m_j)/ln 2); T = W1 + W2
+ W3; band bar sum_b |S_b| <= 3 |T|.  Sympy wards (exact): 3-event
telescoping == 0; block-disconnected pair w == 0 while its
1-cluster product is nonzero; connected pair nonzero at numeric
substitution; mixed derivative d2 w/dl1 dl2 |_0 ==
-tr(B^{-1} E1 B^{-1} E2).  Float synthetic disconnected pair: |w|
<= 1e-12.  Controls: tau refs kz 9/12/13 = 5.984165e-4 /
4.351189e-4 / 5.637632e-4 rel 1e-4; EXC refs 2.28526 / 2.48552 /
2.52887 rel 1e-3; margin identity |det A - tau lmax| <= 1e-10
scale at sigma = 0; lambda_min(B + sum lam E) == lambda_min(Ah)
1e-9 scale.  Discriminator (anchors, common sigma*): SCR collapse
iff E2_scr <= E2_true / 3 on all anchors; EPS fingerprint iff
|log2(E2_eps / E2_true)| >= 1 OR conn-share ratio outside
[0.5, 2] on all anchors.  VERDICT: CLUSTERS-CARRY iff order bar
(|R| <= 0.05 |Delta| OR rho_ord <= 0.6) AND E2_true(kz9, sigma*)
>= 3 AND CI_conn <= CI_disc / 3 AND band bar AND SCR collapse AND
EPS fingerprint; CLUSTERS-DIFFUSE iff E2_true(kz9, sigma*) < 1.5;
else CLUSTERS-PARTIAL.  Scramble seed 1.  NO RH claim; writes
nothing.
"""

ANCHORS = (9, 12, 13)
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
EXC_REFS = {9: 2.28526, 12: 2.48552, 13: 2.52887}
SCR_SEED = 1
N_LATTICE = 16
N3_MAX = 600000
N_BISECT = 8
BAR_RESUM = 1.0e-8
BAR_CONV = 1.0e-6
BAR_TAU = 1.0e-4
BAR_EXC = 1.0e-3
BAR_ORDER = 0.05
BAR_RHO = 0.6
BAR_E2 = 3.0
BAR_E2_LOW = 1.5
BAR_CI_RATIO = 3.0
BAR_BAND = 3.0
X_EPS = 4096
LN2 = math.log(2.0)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


# ------------------------------------------------------------ helpers
def reads_at(rr, uus):
    Mz, D = rr["M"], rr["D"]
    out = np.empty((len(uus), 3))
    for j, u in enumerate(uus):
        out[j, 0] = core.spline_project(rr["W11"], float(u), D, Mz)
        out[j, 1] = core.spline_project(rr["W22"], float(u), D, Mz)
        out[j, 2] = core.spline_project(rr["W12"], float(u), D, Mz)
    return out


def specnorm2(a, c, b):
    m = 0.5 * (a + c)
    r = np.hypot(0.5 * (a - c), b)
    return np.maximum(np.abs(m + r), np.abs(m - r))


def sum2sq_free_support(count, cap):
    rep = np.zeros(cap + 1, dtype=np.int64)
    s = int(math.isqrt(cap)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= cap:
                rep[v] += 1
    return [n for n in range(2, cap + 1) if rep[n] > 0][:count]


_TRIPLE_CACHE = {}


def triple_idx(ka):
    if ka not in _TRIPLE_CACHE:
        _TRIPLE_CACHE[ka] = np.array(
            list(combinations(range(ka), 3)), dtype=np.int32)
    return _TRIPLE_CACHE[ka]


def cluster_census(B2, F, masses, sigma, do_triples=True):
    """Subset-cumulant census of g(S) = log det(B + sigma I +
    sum_S F_j) at orders <= 3.  F = (ka, 3) array of lam_j E_j in
    (a, c, b) layout.  Returns None if any evaluated subset loses
    positive-definiteness."""
    ka = F.shape[0]
    Ba = B2[0, 0] + sigma
    Bc = B2[1, 1] + sigma
    Bb = B2[0, 1]
    FA, FC, FB = F[:, 0], F[:, 1], F[:, 2]

    def dets(sa, sc, sb):
        det = (Ba + sa) * (Bc + sc) - (Bb + sb) ** 2
        tr = (Ba + sa) + (Bc + sc)
        return det, tr

    d0, t0 = dets(0.0, 0.0, 0.0)
    d1, t1 = dets(FA, FC, FB)
    dF, tF = dets(FA.sum(), FC.sum(), FB.sum())
    iu, ju = np.triu_indices(ka, k=1)
    d2, t2 = dets(FA[iu] + FA[ju], FC[iu] + FC[ju], FB[iu] + FB[ju])
    ok = (d0 > 0 and t0 > 0 and np.all(d1 > 0) and np.all(t1 > 0)
          and np.all(d2 > 0) and np.all(t2 > 0) and dF > 0 and tF > 0)
    d3 = t3 = tri = None
    if do_triples:
        tri = triple_idx(ka)
        i3, j3, k3 = tri[:, 0], tri[:, 1], tri[:, 2]
        d3, t3 = dets(FA[i3] + FA[j3] + FA[k3],
                      FC[i3] + FC[j3] + FC[k3],
                      FB[i3] + FB[j3] + FB[k3])
        ok = ok and np.all(d3 > 0) and np.all(t3 > 0)
    if not ok:
        return None
    g0 = math.log(d0)
    g1 = np.log(d1)
    g2 = np.log(d2)
    gF = math.log(dF)
    w1 = g1 - g0
    w2 = g2 - g1[iu] - g1[ju] + g0
    out = dict(g0=g0, gF=gF, delta=gF - g0, w1=w1, iu=iu, ju=ju,
               w2=w2, W1=float(np.sum(w1)), W2=float(np.sum(w2)))
    mm = np.asarray(masses, dtype=np.int64)
    conn2 = np.array([gcd(int(mm[a]), int(mm[b])) > 1
                      for a, b in zip(iu, ju)])
    out["conn2"] = conn2
    if do_triples:
        G2 = np.zeros((ka, ka))
        G2[iu, ju] = g2
        G2[ju, iu] = g2
        i3, j3, k3 = tri[:, 0], tri[:, 1], tri[:, 2]
        g3 = np.log(d3)
        w3 = (g3 - G2[i3, j3] - G2[i3, k3] - G2[j3, k3]
              + g1[i3] + g1[j3] + g1[k3] - g0)
        E2m = np.zeros((ka, ka), dtype=bool)
        E2m[iu, ju] = conn2
        E2m[ju, iu] = conn2
        ne3 = (E2m[i3, j3].astype(np.int8) + E2m[i3, k3]
               + E2m[j3, k3])
        out.update(w3=w3, tri=tri, ne3=ne3, W3=float(np.sum(w3)))
    return out


def census_stats(cs, masses):
    """Sector sums, enrichment, CIs, band table from a census."""
    mm = np.asarray(masses, dtype=np.int64)
    u = np.log(mm.astype(float))
    band1 = np.floor(u / LN2).astype(int)
    w1, w2, conn2 = cs["w1"], cs["w2"], cs["conn2"]
    iu, ju = cs["iu"], cs["ju"]
    W2c = float(np.sum(w2[conn2]))
    W2d = float(np.sum(w2[~conn2]))
    n_c, n_d = int(np.sum(conn2)), int(np.sum(~conn2))
    e2 = ((np.mean(np.abs(w2[conn2])) if n_c else 0.0)
          / max(np.mean(np.abs(w2[~conn2])), 1e-300))
    band2 = np.maximum(band1[iu], band1[ju])
    res = dict(W1=cs["W1"], W2=cs["W2"], W2c=W2c, W2d=W2d,
               n_c=n_c, n_d=n_d, e2=float(e2), delta=cs["delta"])
    sec_c = list(w2[conn2])
    sec_d = list(w2[~conn2])
    bands = {}
    for b, w in zip(band1, w1):
        bands.setdefault(int(b), []).append(float(w))
    for b, w in zip(band2, w2):
        bands.setdefault(int(b), []).append(float(w))
    if "w3" in cs:
        w3, tri, ne3 = cs["w3"], cs["tri"], cs["ne3"]
        conn3 = ne3 >= 2
        mix3 = ne3 == 1
        res.update(W3=cs["W3"], W3c=float(np.sum(w3[conn3])),
                   W3m=float(np.sum(w3[mix3])),
                   W3d=float(np.sum(w3[ne3 == 0])),
                   n3c=int(np.sum(conn3)))
        sec_c += list(w3[conn3])
        sec_d += list(w3[~conn3])
        band3 = np.max(band1[tri], axis=1)
        for b, w in zip(band3, w3):
            bands.setdefault(int(b), []).append(float(w))
    else:
        res.update(W3=0.0, W3c=0.0, W3m=0.0, W3d=0.0, n3c=0)
    sec_c = np.asarray(sec_c)
    sec_d = np.asarray(sec_d)
    res["CIc"] = float(np.sum(np.abs(sec_c))
                       / max(abs(np.sum(sec_c)), 1e-300))
    res["CId"] = float(np.sum(np.abs(sec_d))
                       / max(abs(np.sum(sec_d)), 1e-300))
    res["R"] = cs["delta"] - res["W1"] - res["W2"] - res["W3"]
    res["T"] = res["W1"] + res["W2"] + res["W3"]
    res["conn_share"] = (float(np.sum(np.abs(cs["w2"][conn2])))
                         / max(float(np.sum(np.abs(cs["w2"]))),
                               1e-300))
    res["bands"] = {b: (len(v), float(np.sum(v)),
                        float(np.sum(np.abs(v))))
                    for b, v in sorted(bands.items())}
    return res


# ================================================================= main
def main():
    section("PRIME.CLUSTER.MULT.01 -- connected multiplicative "
            "clusters of the log-pivot (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim; the census lives in the 2-dim corner "
          "compression above the PD floor; typed before the run: "
          "the arch-only base is indefinite, so the margin itself "
          "sits below the expansion floor.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol "
          "(gcd / divisor arithmetic is the admissible Euler-"
          "product datum)", not bad,
          "found %s" % bad if bad else "clean")

    # ----------------------------------------------------- S1 frame
    section("S1 -- frame, anchors, read convention, margin identity")
    A = {}
    ok_tau = ok_exc = ok_mid = True
    conv = None
    conv_dev = None
    for kz in ANCHORS:
        rr = core.build_window(kz)
        B2 = np.asarray(rr["B"], float)
        Xn = np.asarray(rr["Xn"], float)
        lam = np.asarray(rr["lam"], float)
        uu = np.asarray(rr["uu"], float)
        nv = np.rint(np.exp(uu)).astype(np.int64)
        Amat = np.array([[B2[0, 0], B2[0, 1]], [B2[0, 1], B2[1, 1]]])
        Ee = -Xn  # E_j in (a, c, b) layout so A = B + sum lam E
        S = (lam[:, None] * Ee).sum(axis=0)
        Afull = Amat + np.array([[S[0], S[2]], [S[2], S[1]]])
        ev = np.linalg.eigvalsh(Afull)
        tau = float(ev[0])
        lmax = float(ev[1])
        tau_ah = float(np.linalg.eigvalsh(rr["Ah"])[0])
        lmB = float(np.linalg.eigvalsh(Amat)[0])
        ok_tau &= (abs(tau - TAU_REFS[kz]) / TAU_REFS[kz] <= BAR_TAU
                   and abs(tau - tau_ah) <= 1e-9
                   * max(1.0, abs(tau_ah)))
        ok_exc &= (abs((tau - lmB) - EXC_REFS[kz]) / EXC_REFS[kz]
                   <= BAR_EXC)
        detA = float(np.linalg.det(Afull))
        ok_mid &= abs(detA - tau * lmax) <= 1e-10 * max(1.0,
                                                        abs(detA))
        if conv is None:
            Xr = reads_at(rr, uu)
            sc = max(1.0, float(np.max(np.abs(Xn))))
            dp = float(np.max(np.abs(Xr - Xn))) / sc
            dn = float(np.max(np.abs(Xr + Xn))) / sc
            conv = 1.0 if dp <= dn else -1.0
            conv_dev = min(dp, dn)
        A[kz] = dict(rr=rr, B2=B2, lam=lam, uu=uu, nv=nv, Ee=Ee,
                     tau=tau, lmB=lmB, lmax=lmax)
    check("S1.1 [CONTROL] tau_X refs (rel 1e-4) AND lambda_min(B + "
          "sum lam E) == lambda_min(Ah) (1e-9) on anchors %s"
          % (ANCHORS,), ok_tau)
    check("S1.2 [CONTROL] EXC refs (tau - lambda_min(B), rel 1e-3) "
          "on all anchors -- the certified-ladder excess reproduced "
          "in the cluster frame", ok_exc)
    check("S1.3 [WARD] the margin identity at sigma = 0: det A == "
          "tau_X * lambda_max(A) (rel 1e-10) -- the margin IS the "
          "bottom factor of the pivot determinant", ok_mid)
    check("S1.4 [WARD] read convention: spline reads at the true "
          "positions match shipped Xn with sign %+d (dev %.1e <= "
          "%.0e) -- SCR/EPS reads enter in the same convention"
          % (int(conv), conv_dev, BAR_CONV), conv_dev <= BAR_CONV)
    print("    PD floor typed: lambda_min(B) = %.4f / %.4f / %.4f "
          "< 0 on kz = 9/12/13 -- the sigma = 0 subset lattice is "
          "NOT log-expandable around the arch base; the ladder "
          "below measures the floor."
          % (A[9]["lmB"], A[12]["lmB"], A[13]["lmB"]))

    # -------------------------------------- S2 construction wards
    section("S2 -- THE EXPANSION CONSTRUCTION: exact wards "
            "(sympy + lattice)")
    import sympy as sp
    l1, l2, l3 = sp.symbols("l1 l2 l3")
    Bs = sp.Matrix([[7, 1], [1, 5]])
    E1 = sp.Matrix([[2, 1], [1, 0]])
    E2s = sp.Matrix([[0, 1], [1, 3]])
    E3 = sp.Matrix([[1, -1], [-1, 2]])
    lams = (l1, l2, l3)
    Es = (E1, E2s, E3)

    def g_sym(S):
        M = Bs + sum((lams[j] * Es[j] for j in S), sp.zeros(2, 2))
        return sp.log(M.det())

    gtab = {frozenset(S): g_sym(S)
            for r in range(4) for S in combinations(range(3), r)}
    total = sp.S.Zero
    for r in range(4):
        for C in combinations(range(3), r):
            Cf = frozenset(C)
            for r2 in range(len(C) + 1):
                for S in combinations(C, r2):
                    total += (-1) ** (len(C) - len(S)) \
                        * gtab[frozenset(S)]
    resid = sp.simplify(total - gtab[frozenset((0, 1, 2))])
    check("S2.1 [SYMPY EXACT] the resummation identity on 3 "
          "symbolic events: sum over ALL clusters C of w(C) == "
          "g(full) (telescoping on the Boolean lattice) -- residual "
          "simplifies to %s" % resid, resid == 0)
    b1, b2, e1, e2 = sp.symbols("b1 b2 e1 e2", positive=True)
    w_disc = (sp.log((b1 + l1 * e1) * (b2 + l2 * e2))
              - sp.log((b1 + l1 * e1) * b2)
              - sp.log(b1 * (b2 + l2 * e2)) + sp.log(b1 * b2))
    w_disc_s = sp.simplify(sp.logcombine(w_disc, force=True))
    Mc = Bs + l1 * E1 + l2 * E2s
    w_conn = (sp.log(Mc.det()) - sp.log((Bs + l1 * E1).det())
              - sp.log((Bs + l2 * E2s).det()) + sp.log(Bs.det()))
    w_conn_val = float(w_conn.subs({l1: sp.Rational(1, 3),
                                    l2: sp.Rational(1, 5)}))
    check("S2.2 [SYMPY EXACT -- THE MOEBIUS ELIMINATION] the "
          "block-DISCONNECTED 2-cluster weight is IDENTICALLY zero "
          "(w = %s: the pair term cancels exactly against the "
          "product of 1-clusters) while a CONNECTED pair carries "
          "weight (%.6f != 0 at l = 1/3, 1/5) -- only connected "
          "clusters survive, the genuine cumulant structure"
          % (w_disc_s, w_conn_val),
          w_disc_s == 0 and abs(w_conn_val) > 1e-6)
    d2w = sp.diff(w_conn, l1, l2).subs({l1: 0, l2: 0})
    tr_ref = -(Bs.inv() * E1 * Bs.inv() * E2s).trace()
    check("S2.3 [SYMPY EXACT -- THE CONNECTED CORRELATION TERM] "
          "d^2 w({i,j}) / dl_i dl_j |_0 == -tr(B^{-1} E_i B^{-1} "
          "E_j) (residual %s) -- the cluster weights ARE the "
          "connected correlation terms of the events against the "
          "base" % sp.simplify(d2w - tr_ref),
          sp.simplify(d2w - tr_ref) == 0)
    Bn = np.array([[3.7, 0.0], [0.0, 2.1]])
    f1 = np.array([0.9, 0.0, 0.0])
    f2 = np.array([0.0, 1.3, 0.0])

    def gnum(fs):
        s = sum(fs, np.zeros(3))
        return math.log((Bn[0, 0] + s[0]) * (Bn[1, 1] + s[1])
                        - (Bn[0, 1] + s[2]) ** 2)

    w_syn = gnum([f1, f2]) - gnum([f1]) - gnum([f2]) + gnum([])
    check("S2.4 [FLOAT] synthetic disconnected pair cancels to "
          "machine precision (|w| = %.1e <= 1e-12) while its total "
          "increment %.4f is fully carried by the 1-clusters"
          % (abs(w_syn), gnum([f1, f2]) - gnum([])),
          abs(w_syn) <= 1e-12)

    # 16-event lattice at kz 9
    a9 = A[9]
    lam9, Ee9, nv9 = a9["lam"], a9["Ee"], a9["nv"]
    B29 = a9["B2"]
    F9 = lam9[:, None] * Ee9
    nrm_true = float(np.sum(lam9 * specnorm2(Ee9[:, 0], Ee9[:, 1],
                                             Ee9[:, 2])))
    sig0_9 = 1.0 + max(0.0, -a9["lmB"]) + nrm_true  # provisional
    idxL = np.arange(1 << N_LATTICE)
    bitsm = ((idxL[:, None] >> np.arange(N_LATTICE)) & 1)
    pop = bitsm.sum(axis=1)

    def lattice_orders(sigma):
        FL = F9[:N_LATTICE]
        SA = bitsm @ FL[:, 0]
        SC = bitsm @ FL[:, 1]
        SB = bitsm @ FL[:, 2]
        det = ((B29[0, 0] + sigma + SA) * (B29[1, 1] + sigma + SC)
               - (B29[0, 1] + SB) ** 2)
        tr = (B29[0, 0] + sigma + SA) + (B29[1, 1] + sigma + SC)
        if not (np.all(det > 0) and np.all(tr > 0)):
            return None
        g = np.log(det)
        w = g.copy()
        for i in range(N_LATTICE):
            bit = 1 << i
            has = (idxL & bit) != 0
            w[has] -= w[idxL[has] ^ bit]
        resum = abs(float(np.sum(w)) - float(g[-1]))
        Wk = np.array([float(np.sum(w[pop == k]))
                       for k in range(N_LATTICE + 1)])
        return resum, Wk, float(g[-1] - g[0])

    lat0 = lattice_orders(sig0_9)
    resum0, Wk0, dl0 = lat0
    check("S2.5 [THE RESUMMATION WARD, NUMERIC] kz 9 sub-window "
          "(first %d events, masses %d..%d, ALL 2^%d subsets): "
          "|sum_C w(C) - g(full)| = %.2e <= %.0e * scale -- the "
          "full expansion resums to the log-pivot exactly"
          % (N_LATTICE, int(nv9[0]), int(nv9[N_LATTICE - 1]),
             N_LATTICE, resum0, BAR_RESUM),
          resum0 <= BAR_RESUM * max(1.0, abs(dl0)))
    nz = [k for k in range(1, 8) if abs(Wk0[k]) > 0]
    ratios0 = [abs(Wk0[k + 1] / Wk0[k]) for k in nz
               if abs(Wk0[k]) > 1e-300 and k + 1 <= N_LATTICE]
    rho_ord0 = float(np.median(ratios0)) if ratios0 else 0.0
    print("    lattice order histogram at sigma_0 = %.3f "
          "(sub-window Delta = %+.5f):" % (sig0_9, dl0))
    for k in range(1, 9):
        print("      order %2d: W_k = %+12.3e   share %8.2e"
              % (k, Wk0[k], Wk0[k] / dl0 if dl0 else float("nan")))
    print("      orders 9..16 total: %+.3e; geometric ratio "
          "rho_ord (median |W_{k+1}/W_k|, k = 1..6) = %.4f"
          % (float(np.sum(Wk0[9:])), rho_ord0))

    # ------------------------------------- S3 sigma ladder + census
    section("S3 -- THE CENSUS: sigma ladder to the PD floor, "
            "orders <= 3, connectivity, bands (kz 9)")
    # build the three combs per anchor
    combs = {}
    for kz in ANCHORS:
        a = A[kz]
        rr = a["rr"]
        ka = len(a["lam"])
        uu_s = np.asarray(core.build_window(kz,
                                            scramble_seed=SCR_SEED)
                          ["uu"], float)
        E_scr = -conv * reads_at(rr, uu_s)
        me = sum2sq_free_support(ka, X_EPS)
        E_eps = -conv * reads_at(rr, np.log(np.array(me, float)))
        combs[kz] = {
            "TRUE": (a["lam"][:, None] * a["Ee"], a["nv"]),
            "SCR": (a["lam"][:, None] * E_scr, a["nv"]),
            "EPS": (a["lam"][:, None] * E_eps,
                    np.array(me, dtype=np.int64)),
        }
    sig_star = {}
    census_at_star = {}
    evo9 = []
    for kz in ANCHORS:
        a = A[kz]
        ka = len(a["lam"])
        do3 = math.comb(ka, 3) <= N3_MAX
        nrm_max = max(
            float(np.sum(specnorm2(F[:, 0], F[:, 1], F[:, 2])))
            for F, _m in combs[kz].values())
        sig0 = 1.0 + max(0.0, -a["lmB"]) + nrm_max

        def all_census(sigma):
            out = {}
            for name, (F, mm) in combs[kz].items():
                cs = cluster_census(a["B2"], F, mm, sigma,
                                    do_triples=do3)
                if cs is None:
                    return None
                out[name] = cs
            return out

        sig = sig0
        res = all_census(sig)
        assert res is not None, "sigma_0 not PD -- bound violated"
        lo_bad = None
        while True:
            nxt = sig / 2.0
            r2 = all_census(nxt)
            if r2 is None:
                lo_bad = nxt
                break
            sig, res = nxt, r2
            if kz == 9:
                evo9.append((sig, census_stats(res["TRUE"],
                                               combs[9]["TRUE"][1])))
            if sig < 1e-6 * sig0:
                break
        if lo_bad is not None:
            for _ in range(N_BISECT):
                mid = 0.5 * (sig + lo_bad)
                r2 = all_census(mid)
                if r2 is None:
                    lo_bad = mid
                else:
                    sig, res = mid, r2
        sig_star[kz] = (sig0, sig)
        census_at_star[kz] = res
        if not do3:
            print("    kz=%d: C(ka,3) = %d > cap %d -- order-3 "
                  "census SKIPPED (typed)"
                  % (kz, math.comb(ka, 3), N3_MAX))

    sig0_9r, sigs9 = sig_star[9]
    st9 = census_stats(census_at_star[9]["TRUE"],
                       combs[9]["TRUE"][1])
    print("    kz 9: sigma_0 = %.4f -> sigma* = %.6f (PD floor; "
          "|lambda_min(B)| = %.4f; base bottom eig at sigma*: "
          "%+.4e); the margin tau_X = %.4e sits BELOW the floor "
          "by construction" % (sig0_9r, sigs9, -a9["lmB"],
                               sigs9 + a9["lmB"], a9["tau"]))
    print("\n    TRUE-comb census evolution along the sigma "
          "ladder (kz 9, orders <= 3):")
    print("    %-10s %-11s %-11s %-11s %-11s %-8s %-6s %-8s %-8s"
          % ("sigma", "Delta", "W1", "W2", "W3", "|R|/|D|", "E2",
             "CI_conn", "CI_disc"))
    for sg, st in evo9 + [(sigs9, st9)]:
        print("    %-10.4f %+-11.4e %+-11.4e %+-11.4e %+-11.4e "
              "%-8.1e %-6.2f %-8.2f %-8.2f"
              % (sg, st["delta"], st["W1"], st["W2"], st["W3"],
                 abs(st["R"]) / max(abs(st["delta"]), 1e-300),
                 st["e2"], st["CIc"], st["CId"]))
    order_share = abs(st9["R"]) / max(abs(st9["delta"]), 1e-300)
    lat_s = lattice_orders(sigs9)
    if lat_s is not None:
        _rs, WkS, dlS = lat_s
        ratiosS = [abs(WkS[k + 1] / WkS[k]) for k in range(1, 7)
                   if abs(WkS[k]) > 1e-300]
        rho_ordS = float(np.median(ratiosS)) if ratiosS else 0.0
        print("    lattice at sigma*: orders 1..6 = %s; rho_ord = "
              "%.4f" % (["%+.2e" % WkS[k] for k in range(1, 7)],
                        rho_ordS))
    else:
        rho_ordS = rho_ord0
        print("    lattice at sigma*: NOT PD (sub-window loses "
              "positivity before the census set does) -- rho_ord "
              "taken from sigma_0 (typed)")
    order_ok = order_share <= BAR_ORDER or rho_ordS <= BAR_RHO
    check("S3.1 [ORDER HISTOGRAM] at sigma* the remainder beyond "
          "order 3 is |R|/|Delta| = %.3e (bar %.2f) and the exact "
          "sub-window ratio rho_ord = %.3f (bar %.2f): %s"
          % (order_share, BAR_ORDER, rho_ordS, BAR_RHO,
             "effectively finite-order / geometrically decaying -- "
             "the control problem is finite-dimensional per band"
             if order_ok else
             "the series is NOT effectively finite-order at the "
             "floor -- typed"), order_ok)
    conn_ok = (st9["e2"] >= BAR_E2
               and st9["CIc"] <= st9["CId"] / BAR_CI_RATIO)
    check("S3.2 [THE FROZEN QUESTION -- CONNECTIVITY] order-2 "
          "enrichment E2 = %.3f (connected pairs %d / %d, bar "
          ">= %.1f) and sector cancellation CI_conn = %.2f vs "
          "CI_disc = %.2f (bar: conn <= disc/%.0f): the margin %s"
          % (st9["e2"], st9["n_c"], st9["n_c"] + st9["n_d"],
             BAR_E2, st9["CIc"], st9["CId"], BAR_CI_RATIO,
             "LIVES in the connected sector" if conn_ok else
             "does NOT concentrate on the connected sector -- the "
             "cluster weights are position-geometric at this "
             "grade"), conn_ok)
    print("    sector sums at sigma*: W2_conn = %+.4e  W2_disc = "
          "%+.4e  W3_conn = %+.4e  W3_mixed = %+.4e  W3_disc = "
          "%+.4e  (tau_X = %.3e)"
          % (st9["W2c"], st9["W2d"], st9["W3c"], st9["W3m"],
             st9["W3d"], a9["tau"]))
    # per-prime connected aggregates (small primes exact)
    cs9 = census_at_star[9]["TRUE"]
    mm9 = combs[9]["TRUE"][1]
    spf9 = {}
    for m in mm9:
        m0 = int(m)
        p = 2
        while p * p <= m0 and m0 % p:
            p += 1
        spf9[m0] = p if m0 % p == 0 else m0
    prime_agg = {}
    for w, i, j, c in zip(cs9["w2"], cs9["iu"], cs9["ju"],
                          cs9["conn2"]):
        if c:
            p = spf9[int(mm9[i])]
            s, sa, n = prime_agg.get(p, (0.0, 0.0, 0))
            prime_agg[p] = (s + float(w), sa + abs(float(w)), n + 1)
    print("    per-prime connected 2-cluster aggregates (small "
          "primes exact):")
    for p in sorted(prime_agg):
        s, sa, n = prime_agg[p]
        print("      p = %-3d  n_pairs = %-3d  sum w2 = %+11.4e  "
              "sum |w2| = %10.4e" % (p, n, s, sa))
    topi = np.argsort(-np.abs(cs9["w2"]))[:6]
    print("    heaviest 2-clusters: %s"
          % ["(%d,%d)%s %+0.2e"
             % (mm9[cs9["iu"][t]], mm9[cs9["ju"][t]],
                "*" if cs9["conn2"][t] else " ",
                cs9["w2"][t]) for t in topi])
    bl = st9["bands"]
    sum_abs_bands = sum(abs(s) for _n, s, _sa in bl.values())
    band_ok = sum_abs_bands <= BAR_BAND * max(abs(st9["T"]), 1e-300)
    print("    dyadic band table (band = floor(max u / ln 2), "
          "orders 1..3, kz 9, sigma*):")
    print("      %-5s %-7s %-13s %-13s %-9s"
          % ("band", "n_C", "sum w", "sum |w|", "coherence"))
    for b, (n, s, sa) in bl.items():
        print("      %-5d %-7d %+-13.4e %-13.4e %-9.3f"
              % (b, n, s, sa, abs(s) / max(sa, 1e-300)))
    check("S3.3 [BAND SUMMABILITY] sum_b |S_b| = %.4e vs %.0f x "
          "|T| = %.4e: %s"
          % (sum_abs_bands, BAR_BAND,
             BAR_BAND * abs(st9["T"]),
             "the cluster series is band-wise summable (coherent "
             "within dyadic bands)" if band_ok else
             "band sums carry heavy cancellation ACROSS bands -- "
             "the typed absolute-divergence limit"), band_ok)

    # ------------------------------------------ S4 discriminator
    section("S4 -- THE THREE-COMB DISCRIMINATOR (anchors, common "
            "sigma*)")
    scr_ok = eps_ok = True
    e2_tab = {}
    for kz in ANCHORS:
        rowstats = {}
        for name in ("TRUE", "SCR", "EPS"):
            cs = census_at_star[kz][name]
            mm = combs[kz][name][1]
            rowstats[name] = census_stats(cs, mm)
        e2_tab[kz] = rowstats
        et, es, ee = (rowstats[n]["e2"] for n in ("TRUE", "SCR",
                                                  "EPS"))
        cst, css, cse = (rowstats[n]["conn_share"]
                         for n in ("TRUE", "SCR", "EPS"))
        dens = {n: rowstats[n]["n_c"]
                / max(rowstats[n]["n_c"] + rowstats[n]["n_d"], 1)
                for n in ("TRUE", "SCR", "EPS")}
        print("    kz=%d (sigma* = %.4f):" % (kz, sig_star[kz][1]))
        print("      %-5s %-7s %-11s %-11s %-9s %-9s %-9s"
              % ("comb", "E2", "connshare", "edgedens", "CI_c",
                 "CI_d", "Delta"))
        for n in ("TRUE", "SCR", "EPS"):
            r = rowstats[n]
            print("      %-5s %-7.3f %-11.4f %-11.4f %-9.2f %-9.2f "
                  "%+9.3e"
                  % (n, r["e2"], r["conn_share"], dens[n],
                     r["CIc"], r["CId"], r["delta"]))
        scr_ok &= es <= et / 3.0
        share_ratio = cse / max(cst, 1e-300)
        eps_ok &= (abs(math.log2(max(ee, 1e-300)
                                 / max(et, 1e-300))) >= 1.0
                   or share_ratio >= 2.0 or share_ratio <= 0.5)
    check("S4.1 [SCRAMBLE] the connected enrichment collapses "
          "under the mass-fixed scramble on all anchors (E2_scr <= "
          "E2_true / 3): %s -- %s"
          % (scr_ok,
             "the cluster structure is carried by the positions-"
             "with-arithmetic, not by the mass labels alone"
             if scr_ok else
             "the scramble does NOT collapse the enrichment: the "
             "connected weights were never arithmetic to begin "
             "with (position-geometry only)"), scr_ok)
    check("S4.2 [EPSTEIN h=2] the connected-cluster fingerprint "
          "differs from the true comb on all anchors (E2 factor 2 "
          "or conn-share factor 2): %s -- its divisibility graph "
          "carries the class-group obstruction (composites without "
          "their factors)" % eps_ok, eps_ok)

    # --------------------------------------------------- S5 verdict
    section("V -- FROZEN VERDICT + the control-problem shape / "
            "closure + honest consequence")
    controls_ok = not FAILS or all(
        f.startswith(("S3.", "S4.")) for f in FAILS)
    if (order_ok and conn_ok and band_ok and scr_ok and eps_ok):
        verdict = "CLUSTERS-CARRY"
    elif st9["e2"] < BAR_E2_LOW:
        verdict = "CLUSTERS-DIFFUSE"
    else:
        verdict = "CLUSTERS-PARTIAL"
    print("\n  VERDICT: %s   [order: %s | connectivity: %s | "
          "bands: %s | scramble: %s | epstein: %s | controls: %s]"
          % (verdict, "OK" if order_ok else "FAIL",
             "OK" if conn_ok else "FAIL",
             "OK" if band_ok else "FAIL",
             "OK" if scr_ok else "FAIL",
             "OK" if eps_ok else "FAIL",
             "OK" if controls_ok else "FAIL"))
    if verdict == "CLUSTERS-CARRY":
        print("""
  THE FINDING (report prominently): THE CONNECTED SECTOR CARRIES.
  The log-pivot's cluster expansion (exact cumulant lattice, wards
  S2) concentrates on the multiplicatively connected clusters, the
  concentration dies under the mass-fixed scramble, and the h = 2
  Epstein comb shows a distinct connected fingerprint -- the first
  quantitative object in the program that sees the ALL-ORDERS
  arithmetic beyond pair statistics.  THE CONTROL-PROBLEM SHAPE
  (typed, not claimed): a cofinal theorem needs per-band bounds on
  the connected cluster sums; the order-1 band sums are
  Lambda-weighted event masses per dyadic band (Chebyshev /
  Mertens-type sums: sum_{p <= x} log p / p^s-grade, classical and
  unconditional); the connected order-2 sums are same-prime
  geometric ladders (per-prime tails summable exactly, Mertens
  controls the sum over p); the DISCONNECTED sector needs a
  quadratic-form bound of large-sieve / Selberg-weight type per
  band pair.  THE HONEST GAP: (i) all bounds must be uniform in
  the band index along the ladder; (ii) the expansion lives above
  the PD floor sigma_c ~ |lambda_min(B)| while the margin sits at
  sigma = 0 -- crossing the floor (analytic continuation of the
  resummed series, or a floor-free pivot) IS the remaining control
  problem, not covered by the census.""")
    elif verdict == "CLUSTERS-DIFFUSE":
        print("""
  THE FINDING (the honest closure): NO CONNECTED CONCENTRATION.
  The cluster expansion exists and resums exactly (wards S2 all
  pass -- the construction is sound), but the weights ignore the
  divisibility graph: the enrichment of multiplicatively connected
  pairs is statistically absent, i.e. the 2-cluster weights are
  POSITION-GEOMETRIC (they measure spline-read overlap in the
  2-dim corner, which knows |u_i - u_j|, not p_i = p_j).  TYPED
  CLOSURE: the all-orders route THROUGH THIS PIVOT closes -- the
  corner compression to 2x2 destroys the cluster-arithmetic
  before the expansion can see it; any surviving all-orders route
  must expand an object that is not a 2-dim compression (the full
  Toeplitz determinant, or the per-prime block structure) -- a
  different construction, not a parameter change on this one.
  The GUE-strand statement sharpens: not only do pair statistics
  saturate; the pairwise CLUSTER data of the deployed corner is
  equally blind to multiplicativity.""")
    else:
        print("""
  THE FINDING: PARTIAL -- the bars split (see the flag list in the
  verdict line).  The failing bars localize exactly what the
  all-orders route lacks at this grade; the passing bars stand as
  measured structure.  Typed per bar above; no promotion.""")
    print("""
  HONEST FRAME: the census lives above the PD floor of the
  arch-indefinite base and inside a 2-dim corner compression; a
  favorable census is NOT a positivity statement along the ladder,
  and an unfavorable one closes only this pivot's cluster route.
  Nothing here is an RH-relevant bound.  NO RH claim.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
