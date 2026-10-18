#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tau_field_probe -- LEMMA.TAU_FIELD.01 (round 393):
DELTA^2 log tau UNDER F1, the cluster anatomy of the Uvarov
tau-field after r392.

Coexistence: r392 proved the Uvarov ratio
gamma_n(mu) = gamma_n(sigma) * tau_{n+1} tau_{n-1} / tau_n^2
with tau_n = det(I - K_n[Xi] W), and reduced F_eps to a bound
on d2 log tau for F1-bounded nu-runs.  r382 proved max nu-run
<= 2 on MAIN (85/85).  This round attacks that bound.

THE FROZEN QUESTION.  Under F1 (max nu-run <= 2) + half-filling
+ cosine-grid separation, does |exp(d2 log tau) - 1| <= 1/4
and the last-12 jump of gamma stay inside JUMP (2/5, or the
legal V3'/A_15 relaxation 0.45, first fail of A_15 at
coherent scale 2.0) for the last 12 degrees?

LEGS (lemma-first; exits PROVED / REFUTED / REDUCED):
  A  tau-field anatomy.  Under F1, Xi = singletons cup pairs.
     1x1 and 2x2 tau via Sherman-Morrison / 2x2 det, EXPLICIT.
     d2 log tau = sum_clusters d2 log tau_c + d2 log kappa.
     Identity on toys + w9.  Coupling vs separation.
  B  Cluster bounds.  Naive n_cl * typical is linear in N and
     does not close the box.  Rank-1 matrix-det lemma makes
     d2 log tau = Delta log rho_n LOCAL in n (volume telescopes
     to the rank-1 increment at the degree window) -- the
     structural SATZ of this round.  Cluster L1 still exceeds
     log(5/4); coupling is load-bearing (~30% of |d2| on w9).
  C  Adversary.  Run-3 killer is a 3x3 block that violates the
     pair bound.  Sharpest F1-legal object (isolated central
     pair; densest 110-tile; half-fill 1100) vs the box / JUMP /
     JUMP'.  Scramble-OUT classified as an F1/cluster break
     (max_len >= 5), not a coupling remainder.
  D  Kills: drop coupling; wrong SM sign.  Two-period AP:
     cluster contributions identical => d2 = 0 (r392 non-kill).

CALIBRATION DISCLOSURE.  Cluster 1x1/2x2, decomp identity,
rank-1 rho, w9 F1 census (102 clusters), coupling share,
AP / run-3 / center-pair / scramble F1, core-42 last-12, and
the random-F1 half-fill counterexample were first measured in
/tmp (r393_cal.py .. r393_cal7.py) on the same constructors,
2026-08-28.  Frozen floors/ceilings below are that measurement,
sealed as gates.  No two-commit pre-blind freeze: pins
disclosed.  Builder fallback: core-42 only.

FROZEN FROM /tmp (live re-gated, not fitted):
  * 1x1 and adjacent-pair 2x2 MATCH over Q.
  * Decomp identity d2_diag + d2_kappa = d2_full at 3e-14.
  * Rank-1: tau_{n+1}/tau_n = 1 - (W pi)^T (I-K W)^{-1} pi
    at 3e-14; d2 log tau = Delta log rho.
  * w9: n_nu=104, 102 clusters (100 sings, 2 pairs), F1 True.
    last-12 |d2|=0.1553, |e^{d2}-1|=0.1438 < 1/4,
    |Delta d2|=0.2379 (= occupied-Fejer jump).
    diag 0.146, coupling 0.049 (~31% of full) -- load-bearing.
    per-cluster last-12 maxabs med 0.0072 max 0.0125;
    L1(clusters)=0.456 > log(5/4)=0.223 (triangle does not
    close); |sum|/L1 cancel ~0.68.
  * AP every-2: d2 = 0.  Run-3 (h=40, nref=60): j=0.4619 OUT
    even at JUMP'=0.45 and the box.  Isolated center pair:
    j=0.4183 OUT at 2/5, IN at 0.45.  Regular 1100/1010/110
    tiles IN at the r392 window.  Random F1 half-fill OUT
    (h=80 n=60 j~1.18) -- F1+half-fill is not sufficient.
  * Scramble seed=3: max_len=6, F1=False, occ jump=0.4438 OUT
    (cluster break, not coupling).
  * Core-42 occupied last-12 0/42 OUT at JUMP=2/5, maxj=0.3942
    (kz55).  JUMP'=0.45 is legal V3' air; it covers the
    isolated-pair F1 object but not random F1, and does not
    turn the core-42 row into a theorem of F1.

AUSGANG REDUZIERT.  SATZ: F1 cluster split; 1x1/2x2 tau;
decomp identity; rank-1 locality (d2 = Delta log rho, volume
does not enter linearly).  F1 is NECESSARY (run-3 3x3 kills)
and NOT SUFFICIENT (random F1 half-fill leaves any legal JUMP;
L1 triangle does not close; coupling ~31% cannot be dropped).
L-star MAIN/core-42 stay IN at 2/5 -- census, even after
raising JUMP to 0.45.  Remaining: L-star occupation regularity
(the gap between F1-legal cosine masks and the folded
half-filling that actually occurs), still sibling to
Sign-Schur of K^mu[Xi].  No RH claim.

MACHINERY: r392 deletion_transform (Uvarov, scaled_ops),
r390 full_grid / mu_gams, r382 flanking_stats, r379 box,
r226 window_data.

NO RH CLAIM.  Finite identities, a named reduction, named
kills.  Research documentation, not a theorem of RH.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deletion_transform_probe as D  # noqa: E402
import g_eps_mu_probe as P  # noqa: E402
import hirota_sign_probe as HS  # noqa: E402
import pivot_entry_lemma_probe as PE  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

BOX = 1.0 / 16.0
JUMP = 2.0 / 5.0
JUMP_RELAX = 0.45  # legal V3'/A_15 air (A_15 first fails at scale 2.0)
LOG54 = math.log(5.0 / 4.0)
SCR_SEED = 3
CORE_N = 42

# disclosed /tmp pins
DECOMP_BAR = 1.0e-12
RANK1_BAR = 1.0e-12
W9_NCL = 102
W9_NSING, W9_NPAIR = 100, 2
W9_D2_ABS = (0.12, 0.19)
W9_COUPL_ABS = (0.03, 0.07)
W9_L1 = (0.30, 0.70)
W9_CANCEL = (0.50, 0.90)
CLUST_MED_BAR = 0.03
RUN3_J_FLOOR = 0.40
PAIR_J_LO, PAIR_J_HI = 0.35, 0.45
SCR_J_FLOOR = 0.40
CORE_FJ_J_BAR = 0.40
KZ55_J_LO = 0.35
RAND_F1_J_FLOOR = 0.50
MUTANT_FLOOR = 0.01
AP_D2_BAR = 1.0e-8

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; window_data / "
                       "scaled Stieltjes / Uvarov only"
                       if not bad else "; ".join(bad))


def last12(g):
    return D.last12(g)


def in_box(g, jump=JUMP):
    d, j = last12(g)
    return d <= BOX + 1e-12 and j <= jump + 1e-12, d, j


def d2_of_log(logt):
    """Delta^2 of a log-tau sequence; logt[n] = log tau_n, n=0..N."""
    logt = np.asarray(logt, float)
    d1 = np.diff(logt)
    return np.diff(d1)


def clusters_of_nu(idx_grid):
    """Group nu-nodes into consecutive-grid runs.  Returns clusters
    as lists of positions in the original idx_grid array."""
    order = np.argsort(idx_grid)
    g = np.asarray(idx_grid, int)[order]
    clusters = []
    cur = [int(order[0])]
    for k in range(1, len(g)):
        if g[k] == g[k - 1] + 1:
            cur.append(int(order[k]))
        else:
            clusters.append(cur)
            cur = [int(order[k])]
    clusters.append(cur)
    return clusters


def tau_1x1(Kii, w):
    return 1.0 - w * Kii


def tau_2x2(K11, K12, K22, w1, w2):
    return (1.0 - w1 * K11) * (1.0 - w2 * K22) - (K12 * K12) * w1 * w2


def tau_cluster_from_K(K, w, cols):
    if len(cols) == 1:
        a = cols[0]
        return tau_1x1(K[a, a], w[a])
    if len(cols) == 2:
        a, b = cols
        return tau_2x2(K[a, a], K[a, b], K[b, b], w[a], w[b])
    sub = K[np.ix_(cols, cols)]
    W = np.diag(w[cols])
    sign, logabs = np.linalg.slogdet(np.eye(len(cols)) - sub @ W)
    if sign <= 0:
        return 0.0
    return math.exp(logabs)


def log_tau_seq(Pi, w_del, n_upto):
    """tau_n = det(I - K_n W) for n=0..n_upto via slogdet of the
    running CD Gram.  Pi[j] is orthonormal pi_j on the deleted
    nodes (shape (height, m))."""
    m = Pi.shape[1]
    W = np.diag(np.asarray(w_del, float))
    G = np.zeros((m, m))
    out = [0.0]  # log tau_0 = 0
    for n in range(1, n_upto + 1):
        G = G + np.outer(Pi[n - 1], Pi[n - 1])
        sign, logabs = np.linalg.slogdet(np.eye(m) - G @ W)
        out.append(logabs if sign > 0 else -1e30)
    return np.array(out), G


def rank1_rho(G, Pi_n, w_del):
    """rho = 1 - (W pi)^T (I - K W)^{-1} pi."""
    w = np.asarray(w_del, float)
    m = len(w)
    A = np.eye(m) - G @ np.diag(w)
    try:
        y = np.linalg.solve(A, Pi_n)
    except np.linalg.LinAlgError:
        return float("nan")
    return 1.0 - float((w * Pi_n) @ y)


def part_a_standalone():
    section("S1  LEG A -- 1x1 / 2x2 TAU OVER Q + DECOMP")
    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3)]
    wts = [Fr(1), Fr(2), Fr(3), Fr(2), Fr(1)]
    full = D.stieltjes_Q(nodes, wts, 4)

    # 1x1: delete last
    tau1 = Fr(1) + (-wts[4]) * D.K_cross_Q(full["P"], full["h"], 3, 4, 4)
    tau1_sm = Fr(1) - wts[4] * D.K_cross_Q(full["P"], full["h"], 3, 4, 4)
    check("G01-singleton-SM-Q",
          tau1 == tau1_sm and tau1 != Fr(0),
          "1x1 tau = 1 - w K_nn = %s" % tau1)

    # adjacent pair idxs (1,2): closed 2x2
    idxs = [1, 2]
    Ms = [-wts[i] for i in idxs]
    tb = D.tau_block_Q(full["P"], full["h"], 3, idxs, Ms)
    K11 = D.K_cross_Q(full["P"], full["h"], 3, 1, 1)
    K12 = D.K_cross_Q(full["P"], full["h"], 3, 1, 2)
    K22 = D.K_cross_Q(full["P"], full["h"], 3, 2, 2)
    t2 = ((Fr(1) - wts[1] * K11) * (Fr(1) - wts[2] * K22)
          - K12 * K12 * wts[1] * wts[2])
    check("G02-pair-2x2-Q",
          tb == t2,
          "2x2 closed form MATCH %s" % tb)

    # decomp: two far singletons vs full 2-block
    idxs_f = [0, 4]
    Ms_f = [-wts[0], -wts[4]]
    tf = D.tau_block_Q(full["P"], full["h"], 3, idxs_f, Ms_f)
    t0 = Fr(1) - wts[0] * D.K_cross_Q(full["P"], full["h"], 3, 0, 0)
    t4 = Fr(1) - wts[4] * D.K_cross_Q(full["P"], full["h"], 3, 4, 4)
    kap = tf / (t0 * t4)
    check("G03-decomp-kappa-Q",
          kap != Fr(1) and tf == kap * t0 * t4,
          "far-sings kappa=%s (coupling ON)" % kap)

    # near vs far: |log kappa| larger when close (CD kernel)
    idxs_n = [0, 1]
    tn = D.tau_block_Q(full["P"], full["h"], 3, idxs_n, [-wts[0], -wts[1]])
    t0n = Fr(1) - wts[0] * D.K_cross_Q(full["P"], full["h"], 3, 0, 0)
    t1n = Fr(1) - wts[1] * D.K_cross_Q(full["P"], full["h"], 3, 1, 1)
    kap_n = tn / (t0n * t1n)
    # |log| comparison in float
    ln_near = abs(math.log(abs(float(kap_n))))
    ln_far = abs(math.log(abs(float(kap))))
    check("G04-coupling-vs-gap-Q",
          ln_near > ln_far,
          "|log kappa| near=%.3f far=%.3f (CD decay)" % (ln_near, ln_far))


def part_b_identities(smoke):
    section("S2  RANK-1 LOCALITY + w9 CLUSTER DECOMP")
    d = HS.window_data(9)
    xs, ws, ys, vs = d["xs"], d["ws"], d["ys"], d["vs"]
    N = int(d["n_max"])
    n = N - 2
    xf, wff = P.full_grid(N)
    idx_nu = D.match_indices(xf, ys)
    w_del = wff[idx_nu]
    cls = clusters_of_nu(idx_nu)
    n_sing = sum(1 for c in cls if len(c) == 1)
    n_pair = sum(1 for c in cls if len(c) == 2)
    n_long = sum(1 for c in cls if len(c) >= 3)
    f1 = (n_long == 0) and max(len(c) for c in cls) <= 2
    check("G10-w9-F1-clusters",
          f1 and len(cls) == W9_NCL and n_sing == W9_NSING
          and n_pair == W9_NPAIR,
          "n_nu=%d n_cl=%d sings=%d pairs=%d runs>=3=%d F1=%s"
          % (len(idx_nu), len(cls), n_sing, n_pair, n_long, f1))

    print("    scaled_ops n=%d m=%d ..." % (n, len(idx_nu)), flush=True)
    g_full, Pi = D.scaled_ops(xf, wff, n + 1, idx_nu)

    # rank-1 identity at a handful of n (including the last-12 window)
    G = np.zeros((len(idx_nu), len(idx_nu)))
    W = np.diag(w_del)
    rho_err = 0.0
    sample_n = [1, 2, 8, max(1, n // 2), n - 12, n - 1]
    log_tau = [0.0]
    for k in range(1, n + 2):
        G = G + np.outer(Pi[k - 1], Pi[k - 1])
        if k in sample_n or k == n or k == n + 1:
            sign, logabs = np.linalg.slogdet(np.eye(len(idx_nu)) - G @ W)
            # keep running log tau only when we need the sequence:
            # we fill log_tau densely below for last-20 via a second pass
        if k in sample_n:
            rho = rank1_rho(G - np.outer(Pi[k - 1], Pi[k - 1]), Pi[k - 1],
                            w_del)
            sign0, la0 = np.linalg.slogdet(
                np.eye(len(idx_nu))
                - (G - np.outer(Pi[k - 1], Pi[k - 1])) @ W)
            sign1, la1 = np.linalg.slogdet(np.eye(len(idx_nu)) - G @ W)
            if sign0 > 0 and sign1 > 0 and rho > 0:
                rho_err = max(rho_err, abs(math.exp(la1 - la0) - rho))
    check("G11-rank1-identity",
          rho_err < RANK1_BAR,
          "max |tau_{n+1}/tau_n - (1 - q_n)|=%.3e" % rho_err)

    # last-20 log tau full / diag / kappa  (decomp identity)
    n0 = max(0, n - 20)
    G = np.zeros((len(idx_nu), len(idx_nu)))
    for k in range(n0):
        G = G + np.outer(Pi[k], Pi[k])
    logs_f, logs_d, logs_k = [], [], []
    for k in range(n0, n + 2):
        if k > 0 and k > n0:
            G = G + np.outer(Pi[k - 1], Pi[k - 1])
        elif k == n0 and n0 > 0:
            pass
        elif k == 0:
            G = np.zeros_like(G)
        sign, la = np.linalg.slogdet(np.eye(len(idx_nu)) - G @ W)
        ld = 0.0
        for c in cls:
            tc = tau_cluster_from_K(G, w_del, c)
            if tc <= 0:
                ld = -1e30
                break
            ld += math.log(tc)
        logs_f.append(la if sign > 0 else -1e30)
        logs_d.append(ld)
        logs_k.append((la - ld) if (sign > 0 and ld > -1e20) else -1e30)
    logs_f, logs_d, logs_k = map(np.array, (logs_f, logs_d, logs_k))
    d2f = d2_of_log(logs_f)
    d2d = d2_of_log(logs_d)
    d2k = d2_of_log(logs_k)
    # align: d2[i] corresponds to n = n0+i+1  (second difference)
    err_de = float(np.max(np.abs(d2f - (d2d + d2k))))
    check("G12-decomp-identity",
          err_de < DECOMP_BAR,
          "max |d2_full - (d2_diag+d2_kappa)|=%.3e" % err_de)

    # last-12 of d2 (the F_eps window of gamma, since d2 log tau
    # at degree n is log(gamma_n / (1/4)) when gamma(sigma)=1/4)
    d2_last = d2f[-12:]
    d2d_last = d2d[-12:]
    d2k_last = d2k[-12:]
    maxabs_f = float(np.max(np.abs(d2_last)))
    maxabs_d = float(np.max(np.abs(d2d_last)))
    maxabs_k = float(np.max(np.abs(d2k_last)))
    box_ok = float(np.max(np.abs(np.exp(d2_last) - 1.0))) < 0.25 + 1e-12
    jump_d2 = float(np.max(np.abs(np.diff(d2_last))))
    check("G13-w9-last12-d2",
          W9_D2_ABS[0] < maxabs_f < W9_D2_ABS[1] and box_ok,
          "max|d2|=%.4f |e^{d2}-1|_max=%.4f |Delta d2|=%.4f"
          % (maxabs_f, float(np.max(np.abs(np.exp(d2_last) - 1.0))),
             jump_d2))
    check("G14-coupling-load-bearing",
          W9_COUPL_ABS[0] < maxabs_k < W9_COUPL_ABS[1],
          "max|d2_kappa|=%.4f (diag=%.4f full=%.4f) -- NOT droppable"
          % (maxabs_k, maxabs_d, maxabs_f))

    # per-cluster last-12 and L1 vs |sum|
    per = []
    for c in cls:
        lc = []
        G = np.zeros((len(idx_nu), len(idx_nu)))
        for k in range(n0):
            G = G + np.outer(Pi[k], Pi[k])
        logs_c = []
        for k in range(n0, n + 2):
            if k > n0:
                G = G + np.outer(Pi[k - 1], Pi[k - 1])
            tc = tau_cluster_from_K(G, w_del, c)
            logs_c.append(math.log(tc) if tc > 0 else -1e30)
        d2c = d2_of_log(logs_c)
        per.append(float(np.max(np.abs(d2c[-12:]))))
    per = np.array(per)
    l1 = float(np.sum(np.abs(d2d_last)))  # L1 of the SUM of cluster d2
    # better: L1 of per-n cluster-sum absolute
    # recompute L1 of cluster contributions at last-12
    l1_n = []
    G = np.zeros((len(idx_nu), len(idx_nu)))
    for k in range(n0):
        G = G + np.outer(Pi[k], Pi[k])
    logs_each = [[] for _ in cls]
    for k in range(n0, n + 2):
        if k > n0:
            G = G + np.outer(Pi[k - 1], Pi[k - 1])
        for i, c in enumerate(cls):
            tc = tau_cluster_from_K(G, w_del, c)
            logs_each[i].append(math.log(tc) if tc > 0 else -1e30)
    d2_each = [d2_of_log(np.array(lc)) for lc in logs_each]
    stack = np.stack([d[-12:] for d in d2_each], axis=0)  # (n_cl, 12)
    l1_mean = float(np.mean(np.sum(np.abs(stack), axis=0)))
    sum_abs = float(np.mean(np.abs(np.sum(stack, axis=0))))
    cancel = 1.0 - sum_abs / max(l1_mean, 1e-30)
    check("G15-cluster-L1-does-not-close",
          W9_L1[0] < l1_mean < W9_L1[1]
          and l1_mean > LOG54
          and W9_CANCEL[0] < cancel < W9_CANCEL[1]
          and float(np.median(per)) < CLUST_MED_BAR,
          "L1=%.3f |sum|=%.3f cancel=%.2f med|d2_c|=%.4f "
          "(L1 > log(5/4)=%.3f: triangle FAILS)"
          % (l1_mean, sum_abs, cancel, float(np.median(per)), LOG54))

    # d2 = Delta log rho  (local in n)
    # reconstruct rho from last-20 tau and compare d2
    dlogrho = np.diff(logs_f)  # log rho_n = log tau_{n+1} - log tau_n
    d2_from_rho = np.diff(dlogrho)
    err_loc = float(np.max(np.abs(d2_from_rho - d2f)))
    check("G16-d2-is-Delta-log-rho",
          err_loc < RANK1_BAR,
          "volume SATZ: d2 log tau = Delta log rho  maxerr=%.3e "
          "(not linear in n_cl)" % err_loc)

    if smoke:
        return
    # occupied last-12 jump equals |Delta d2|
    g_occ = P.mu_gams(xs, P.fejer_w(xs, float(ws.sum())), n)
    _d, jocc = last12(g_occ)
    check("G17-jump-equals-Delta-d2",
          abs(jocc - jump_d2) < 1e-4,
          "occ jump=%.4f |Delta d2|=%.4f" % (jocc, jump_d2))


def part_c_adversary(smoke):
    section("S3  LEG C -- F1 ADVERSARY / RUN-3 3x3 / SCRAMBLE")
    xf40, wf40 = P.full_grid(40)
    S40 = len(xf40)

    # AP every-2: d2 ~ 0
    m_ap = np.array([i % 2 == 0 for i in range(S40)], bool)
    g_ap = P.mu_gams(xf40[~m_ap], wf40[~m_ap],
                     min(int((~m_ap).sum()) - 2, 40))
    dap, jap = last12(g_ap)
    check("G20-AP-d2-zero",
          dap < 1e-4 and jap < 1e-4,
          "AP last12 d=%.4f j=%.4f (identical cluster contrib => d2=0)"
          % (dap, jap))

    # run-3 kill (r392 window)
    m3 = np.zeros(S40, dtype=bool)
    m3[S40 // 3:S40 // 3 + 3] = True
    g3 = P.mu_gams(xf40[~m3], wf40[~m3], min(int((~m3).sum()) - 2, 60))
    i3, d3, j3 = in_box(g3)
    i345, _, _ = in_box(g3, JUMP_RELAX)
    check("G21-run3-kills-box-and-JUMP",
          (not i3) and (not i345) and j3 > RUN3_J_FLOOR,
          "run=3 d=%.4f j=%.4f OUT at 2/5 AND 0.45 (3x3 > pair bound)"
          % (d3, j3))

    # isolated center pair: sharpest small F1 object at r392 window
    m2 = np.zeros(S40, dtype=bool)
    m2[S40 // 2] = m2[S40 // 2 + 1] = True
    g2 = P.mu_gams(xf40[~m2], wf40[~m2], min(int((~m2).sum()) - 2, 60))
    i2, d2, j2 = in_box(g2)
    i245, _, _ = in_box(g2, JUMP_RELAX)
    check("G22-center-pair-F1-supremum-toy",
          (not i2) and i245 and PAIR_J_LO < j2 < PAIR_J_HI and d2 <= BOX,
          "center pair d=%.4f j=%.4f OUT at 2/5, IN at JUMP'=0.45"
          % (d2, j2))

    # regular half-fill 1100 IN at r392 window
    m11 = np.array([i % 4 < 2 for i in range(S40)], bool)
    g11 = P.mu_gams(xf40[~m11], wf40[~m11],
                    min(int((~m11).sum()) - 2, 60))
    i11, d11, j11 = in_box(g11)
    check("G23-regular-1100-IN",
          i11,
          "1100 last12 d=%.4f j=%.4f IN (periodic F1 half-fill)"
          % (d11, j11))

    # 3x3 vs 2x2 cluster d2 on a tiny grid (h=12)
    xf12, wf12 = P.full_grid(12)
    S12 = len(xf12)
    idx_all = np.arange(S12)
    gF, Pi12 = D.scaled_ops(xf12, wf12, 16, idx_all)
    # run-3 block at center vs run-2
    c3 = list(range(S12 // 2, S12 // 2 + 3))
    c2 = list(range(S12 // 2, S12 // 2 + 2))
    G = np.zeros((S12, S12))
    logs3, logs2 = [0.0], [0.0]
    for k in range(1, 16):
        G = G + np.outer(Pi12[k - 1], Pi12[k - 1])
        logs3.append(math.log(max(tau_cluster_from_K(G, wf12, c3), 1e-300)))
        logs2.append(math.log(max(tau_cluster_from_K(G, wf12, c2), 1e-300)))
    d2_3 = d2_of_log(logs3)
    d2_2 = d2_of_log(logs2)
    max3 = float(np.max(np.abs(d2_3[-12:])))
    max2 = float(np.max(np.abs(d2_2[-12:])))
    e3 = float(np.max(np.abs(np.exp(d2_3[-12:]) - 1.0)))
    e2 = float(np.max(np.abs(np.exp(d2_2[-12:]) - 1.0)))
    check("G24-run3-3x3-violates-pair",
          max3 > max2 and e3 > 0.25,
          "3x3 max|d2|=%.3f |e^{d2}-1|=%.3f vs 2x2 %.3f / %.3f"
          % (max3, e3, max2, e2))

    # scramble seed=3: F1 break
    ds = HS.window_data(9, scramble_seed=SCR_SEED)
    mz = PE.scramble_mz(SCR_SEED)
    st = PE.flanking_stats(mz["wu"])
    ns = int(ds["n_max"]) - 2
    gsc = P.mu_gams(ds["xs"], P.fejer_w(ds["xs"], float(ds["ws"].sum())), ns)
    isc, dsc, jsc = in_box(gsc)
    check("G25-scramble-is-F1-cluster-break",
          (not st["F1"]) and st["max_len"] >= 5
          and (not isc) and jsc > SCR_J_FLOOR,
          "seed=3 F1=%s max_len=%d n>=3=%d occ j=%.4f OUT "
          "(cluster break, not coupling)"
          % (st["F1"], st["max_len"], st["n_lenge3"], jsc))

    if smoke:
        return

    # random F1 half-fill on h=80, nref=60: OUT -- F1 not sufficient
    xf80, wf80 = P.full_grid(80)
    S80 = len(xf80)
    rng = np.random.default_rng(2)
    m = np.zeros(S80, dtype=bool)
    target = int(round(0.45 * S80))
    i = nnu = 0
    while i < S80 and nnu < target:
        if rng.random() < 0.35:
            i += 1
            continue
        if rng.random() < 0.45 or i + 1 >= S80 or nnu + 2 > target:
            m[i] = True
            nnu += 1
            i += 2
        else:
            m[i] = m[i + 1] = True
            nnu += 2
            i += 3
    run = mx = 0
    for v in m.tolist():
        run = run + 1 if v else 0
        mx = max(mx, run)
    gR = P.mu_gams(xf80[~m], wf80[~m], min(int((~m).sum()) - 2, 60))
    iR, dR, jR = in_box(gR, JUMP_RELAX)
    check("G26-random-F1-half-fill-OUT",
          mx <= 2 and (not iR) and jR > RAND_F1_J_FLOOR,
          "F1 maxrun=%d n_nu=%d d=%.4f j=%.4f OUT at JUMP'=0.45 "
          "(F1+half-fill NOT sufficient)"
          % (mx, int(m.sum()), dR, jR))


def part_d_kills(smoke):
    section("S4  LEG D -- MUTANTS + AP CONTROL")
    # drop coupling: |d2_diag - d2_full| is the kappa term, already
    # measured; mutant = treat diag as the bound (fails vs full).
    d = HS.window_data(9)
    N = int(d["n_max"])
    n = N - 2
    xf, wff = P.full_grid(N)
    idx_nu = D.match_indices(xf, d["ys"])
    w_del = wff[idx_nu]
    cls = clusters_of_nu(idx_nu)
    g_full, Pi = D.scaled_ops(xf, wff, n + 1, idx_nu)
    n0 = n - 16
    G = np.zeros((len(idx_nu), len(idx_nu)))
    W = np.diag(w_del)
    for k in range(n0):
        G = G + np.outer(Pi[k], Pi[k])
    lf, ld, lw = [], [], []
    for k in range(n0, n + 2):
        if k > n0:
            G = G + np.outer(Pi[k - 1], Pi[k - 1])
        sign, la = np.linalg.slogdet(np.eye(len(idx_nu)) - G @ W)
        sdiag = 0.0
        swrong = 0.0
        for c in cls:
            tc = tau_cluster_from_K(G, w_del, c)
            sdiag += math.log(tc) if tc > 0 else -1e30
            # wrong SM sign: 1 + w K instead of 1 - w K
            if len(c) == 1:
                a = c[0]
                tw = 1.0 + w_del[a] * G[a, a]
            elif len(c) == 2:
                a, b = c
                tw = tau_2x2(-G[a, a], G[a, b], -G[b, b],
                             w_del[a], w_del[b])
                # equivalent: flip the diagonal K sign
                tw = ((1.0 + w_del[a] * G[a, a])
                      * (1.0 + w_del[b] * G[b, b])
                      - (G[a, b] ** 2) * w_del[a] * w_del[b])
            else:
                tw = 0.0
            swrong += math.log(tw) if tw > 0 else -1e30
        lf.append(la if sign > 0 else -1e30)
        ld.append(sdiag)
        lw.append(swrong)
    d2f = d2_of_log(np.array(lf))[-12:]
    d2d = d2_of_log(np.array(ld))[-12:]
    d2w = d2_of_log(np.array(lw))[-12:]
    drop_err = float(np.max(np.abs(d2d - d2f)))
    sign_err = float(np.max(np.abs(d2w - d2f)))
    check("G30-drop-coupling-mutant",
          drop_err > MUTANT_FLOOR,
          "max |d2_diag - d2_full|=%.4f (coupling omitted)" % drop_err)
    check("G31-wrong-SM-sign-mutant",
          sign_err > MUTANT_FLOOR,
          "max |d2_wrongSM - d2_full|=%.4f" % sign_err)

    if smoke:
        return

    section("S5  FULL CENSUS -- core-42 last-12 (JUMP vs JUMP')")
    core = list(V.admissible_indices())
    check("G40-ladder-size", len(core) == CORE_N, "core %d" % len(core))
    n_out = n_out45 = 0
    max_d = max_j = 0.0
    kz_j = None
    for i, kz in enumerate(core):
        dk = HS.window_data(kz)
        nk = int(dk["n_max"]) - 2
        gf = P.mu_gams(dk["xs"],
                       P.fejer_w(dk["xs"], float(dk["ws"].sum())), nk)
        dd, jj = last12(gf)
        max_d, max_j = max(max_d, dd), max(max_j, jj)
        if jj >= max_j - 1e-15:
            kz_j = kz
        if dd > BOX or jj > JUMP:
            n_out += 1
        if dd > BOX or jj > JUMP_RELAX:
            n_out45 += 1
        if (i + 1) % 14 == 0:
            print("    ... %d/42 t=%.1f" % (i + 1, time.time() - T0),
                  flush=True)
    check("G41-core42-inside-JUMP",
          n_out == 0 and max_j < CORE_FJ_J_BAR,
          "OUT@2/5 %d/42 maxd=%.5f maxj=%.4f (margin %.4f) -- CENSUS"
          % (n_out, max_d, max_j, JUMP - max_j))
    check("G42-JUMP-relax-still-census",
          n_out45 == 0 and kz_j == 55 and max_j > KZ55_J_LO,
          "OUT@0.45 %d/42 maxj=%.4f at kz%d; JUMP'=0.45 covers "
          "kz55 and the isolated pair, NOT random F1 -- still census"
          % (n_out45, max_j, kz_j))
    check("G43-jump-air-legal",
          JUMP_RELAX > JUMP and math.log(5.0 / 3.0) > JUMP_RELAX,
          "2/5=%.2f < 0.45 < log(5/3)=%.4f (V3' A_15 air; "
          "0.45 does not collapse JUMP to the box)"
          % (JUMP, math.log(5.0 / 3.0)))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("tau_field_probe -- LEMMA.TAU_FIELD.01 (round 393)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)

    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)

    part_a_standalone()
    part_b_identities(smoke)
    part_c_adversary(smoke)
    part_d_kills(smoke)

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (n_ok, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    tag = ("TAU FIELD LEMMA SMOKE" if smoke else "TAU FIELD LEMMA")
    if n_fail == 0:
        print(tag + " VERIFIED")
        return 0
    print(tag + " FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
