#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""evolutionary_certificate_probe --
PRIME.SEARCH.EVOLUTIONARY_CERTIFICATE.01 (round 438):
grammar GP / SOS-LP / adversarial GA over the r407 C,
r375 K2 and r433 q^dagger objects.  Search may be
heuristic; NOTHING counts without (a) a machine-precision
gate on every training window, (b) HOLDOUT worlds never
seen in any fitness loop, (c) Q-exact toys, (d) kill
tests.  The r395 truncation-overfit lesson is why (b)
is a hard split, sealed below.

TRAIN / HOLDOUT SPLIT (r395).  Fitness loops of ALL
three tracks see ONLY MAIN windows from TRAIN_KZ and
legal MAIN depth shifts of those windows.  NEVER in
any fitness loop:
  * chi_3 / chi_4 (any kz, matched frame a=1)
  * EXT (r286 extension anchors, here kz=35)
  * Selected k >= 7 (kz=43 = selected k=7)
Those worlds are evaluated AFTER search as holdout /
falsifier confirmation.  Fractional arch-parity a not
in {0,1} is ILLEGAL (Gamma-factor destroyed; r357);
it is a control, not a candidate.

SEALED BUDGET (deterministic seeds, generation counts
frozen before the live run; smoke < 60 s, full <= 30 min):
  Track A  SEED_A=43801  pop_smoke=8 gen_smoke=2
           pop_full=24   gen_full=10  depth=4
  Track B  SEED_B=43802  lp_smoke=40  lp_full=250
           b2_grid sealed (theta0, theta1) 6x6
  Track C  SEED_C=43803  legal MAIN grid
           CORE_KZ x DEPTH_DN  (enumerated, not stochastic)
           plus a 12-individual / 6-gen tiny weight-scale GA
           on TRAIN_KZ only

GRAMMAR (Track A, hole samples of psi_- of C):
  terminals Y, U=u^vee, PY=P_Y', INVPY, SQRTU, ONES, NYQ,
  TH, SGNPY, GAP, DX (nearest X).  ops + - * / neg inv
  abs sqrt sq.  Fitness = min_train |cos(v, psi_-)|.
  Target > 0.999 uniform.  Four canonical candidates
  on w9 sit in 0.007-0.71 and FAIL the uniform bar
  (INVPY is the best seed, min-cos 0.101 on {9,18,20}).

TRACK B: (1) NNLS of source-pure scalars onto -det K2
on the n_-=1 train branch, exact-checked on the r375
Q toy; (2) A0 = P - v v^T + Rest with P = theta0 I +
theta1 diag(u^vee), v = v_top (source), Rest PSD gate.

TRACK C: fitness -lam_2(C) on the legal MAIN grid.
The TWO-CASE object is the canonical cut n = N_w-3
(A0 = R_{N-3}-I/2).  nC >= 2 at that cut is the
falsifier.  Depth shifts are a DIAGNOSTIC (r395):
truncation n = N_w-5 can inflate nC to 2; deepening
goes vacuous.  Truncation nC=2 is NOT a falsifier of
the canonical two-case statement.

CALIBRATION DISCLOSURE.  Canonical cosines, train
C-spectra, chi/EXT/selected holdout nC, permute/scramble
nC, r375 det K2, illegal a=0 hybrid nC, B2 remainder
and a 12x8 GP first measured in /tmp (r438_cal.py,
r438_cal2.py, r438_cal3.py) on the r407/r431/r433
builders, 2026-08-30.  Frozen floors below are that
measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: pack wall << 120 s.

FROZEN FROM /tmp (live re-gated, not fitted):
  * w9: nC=1 Cmin=0.857119 C2=1.00017632 |Y|=104
    cos ones=0.0072 cent=0.0010 nyq=0.3859 vtop=0.6766
  * w18: nC=1 Cmin=0.640344 C2=1.00003201
    vtop cos=0.0584  (uniform bar already dead)
  * w20: nC=1 Cmin=0.975760 C2=1.00003567 vtop cos=0.7102
  * best seed uniform: INVPY min-cos=0.1010
  * CHI3-9 nC=0; CHI3-15 nC=1; CHI4-9 nC=1
  * selected k=7 kz=43 nC=0 Cmin=1.000000 C2=1.00000148
  * EXT kz=35 nC=1 C2=1.00000033
  * PERM nC=21; SCR nC=21
  * w9 q^dagger=0.933044234  det K2=-5.038869
  * illegal CHI3 a=0 nC=3 (control, not a falsifier)
  * truncation diagnostic (full grid): nC=2 at dn=-2
    on kz=5,18,22,38; canonical dn=0 is nC<=1 on all
    CORE_KZ.  r395 class, not a two-case falsifier.
  * Q: 1-Y recovers e_0 on the 2-node toy residual 0
  * Q: r375 det K2=-7, gamma=9/2, lam=1 EXACT
  * Q: A0=diag(-1,1,2,3) = P - 2 e0 e0^T, P=diag(1,1,2,3)

AUSGANG A:NOT_FOUND / B:NOT_FOUND / C:NOT_FOUND.
SATZ (machinery only): Q toys residual 0; r375
factorization live on w9; illegal a=0 hybrid nC=3
as a geometry-kill.  REFUTED as exact source
formulas: four canonical psi candidates (w9
0.007-0.71; uniform min 0.058 vtop / 0.101 INVPY)
and GP best INVPY (10 gen, min-cos 0.1010 << 0.999);
source NNLS for lam2-1, q^dagger and -det K2 all
relres >> 1; B2 family remainder lmin=-0.261 not
PSD.  Canonical two-case: nC<=1 on 11/11 CORE at
dn=0 and on 7/7 holdout; closest C2-1 = 2.245e-7
at kz=52.  Truncation dn=-2 inflates nC=2 on
{5,18,22,38,52} -- r395 class, not a falsifier.
No RH claim.  No L* claim.  No R-dagger claim.
Research documentation.

MACHINERY: r407 DI.pack_C / chain_C, r413 HTM.v_top,
r433 ER.row_of, r367 FTI.cut_rung / haynsworth_toy,
r375 verify_p2 six_scalar_fractions, r398 HM.scramble
/ chi_mz, r403 P1.reweight, r226 V.build_measures,
r357 DMF chi, r342 PX.build_rung.

NO RH CLAIM.  Finite identities, a named search with
a hard train/holdout split, named kill table.
Research documentation, not a theorem of RH.
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

import dual_intertwiner_probe as DI  # noqa: E402
import hole_top_mode_probe as HTM  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import edge_redheffer_probe as ER  # noqa: E402
import verify_p2_steps as P2  # noqa: E402

DI_SHA_PREFIX = "2ee74c59"
HTM_SHA_PREFIX = "9b0e69fe"
ER_SHA_PREFIX = "8371b954"
FTI_SHA_PREFIX = "e0d79840"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"

# ---- sealed split / budget ----
TRAIN_KZ = (9, 18, 20)
CORE_KZ = (5, 9, 12, 16, 18, 20, 22, 36, 38, 39, 52)
DEPTH_DN = (-2, -1, 0, 1, 2)
HOLDOUT_CHI = (
    (9, DMF.Q_CHI3, DMF.LPQ3, "CHI3-9"),
    (15, DMF.Q_CHI3, DMF.LPQ3, "CHI3-15"),
    (19, DMF.Q_CHI3, DMF.LPQ3, "CHI3-19"),
    (9, DMF.Q_CHI4, DMF.LPQ4, "CHI4-9"),
    (20, DMF.Q_CHI4, DMF.LPQ4, "CHI4-20"),
)
HOLDOUT_SEL_KZ = 43
HOLDOUT_EXT_KZ = 35
SEED_A, SEED_B, SEED_C = 43801, 43802, 43803
POP_A_SMOKE, GEN_A_SMOKE = 8, 2
POP_A_FULL, GEN_A_FULL = 24, 10
DEPTH_A = 4
LP_SMOKE, LP_FULL = 40, 250
GA_POP, GA_GEN = 12, 6

COS_EXACT = 0.999
FLOOR = 1.0e-8
W9_CMIN, W9_C2 = 0.857119, 1.00017632
W9_ONES, W9_NYQ, W9_VTOP = 0.0072, 0.3859, 0.6766
INVPY_MIN = 0.1010
PERM_NC_LO, SCR_NC = 15, 21
W9_QDAG = 0.933044234
W9_DETK = -5.038869
CHI3_A0_NC = 3
KZ52_C2 = 1.0000002245

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()
CONSTRUCTORS = ("feat_pack", "eval_tree", "nnls_source",
                "b2_family", "legal_grid")


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72, flush=True)


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
    return (not bad), ("NO zero/prime oracles; GP on Y/u^vee/P'"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = node.func
            nm = fn.attr if isinstance(fn, ast.Attribute) else (
                fn.id if isinstance(fn, ast.Name) else None)
            if nm in ("curve_fit", "least_squares"):
                hits.append(nm)
    return hits


def cosabs(a, b):
    a = np.asarray(a, float)
    b = np.asarray(b, float)
    na, nb = float(np.linalg.norm(a)), float(np.linalg.norm(b))
    if na < 1e-30 or nb < 1e-30 or not np.all(np.isfinite(a)):
        return 0.0
    return abs(float(np.vdot(a, b))) / (na * nb + 1e-30)


# ---- window pack (source features + targets) ----
FEAT_NAMES = ("Y", "U", "PY", "INVPY", "SQRTU", "ONES", "NYQ",
              "TH", "SGNPY", "GAP", "DX")


def feat_pack(mz, n=None):
    """Hole-sampled features of C plus psi_- = bottom evec.
    C is already on Y (r407).  n=None uses working depth Nw-3."""
    if n is None:
        pk = DI.pack_C(mz)
        C, meta = pk["C"], pk["meta"]
        nneg = int(pk["nneg"])
    else:
        C, meta = DI.chain_C(mz, n=int(n))
        nneg = None
        pk = None
    ev, W = np.linalg.eigh(C)
    nC = int(np.sum(ev < 1.0 - 1e-12))
    if nneg is None:
        nneg = nC
    psi = W[:, 0].copy()
    yn = np.asarray(meta["yn"], float)
    wY = np.maximum(np.asarray(meta["ud"][meta["iY"]], float), 1e-300)
    xp = np.asarray(meta["xp"], float)
    nY = len(yn)
    D = yn[:, None] - yn[None, :]
    np.fill_diagonal(D, 1.0)
    logabs = np.sum(np.log(np.maximum(np.abs(D), 1e-300)), axis=1)
    logabs -= float(np.max(logabs))
    PYp = np.prod(np.sign(D), axis=1) * np.exp(logabs)
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    o = np.argsort(th)
    nyq = np.zeros(nY)
    nyq[o] = np.cos(math.pi * np.arange(nY))
    ys = np.sort(yn)
    if nY > 1:
        dlt = np.diff(ys)
        gap_sorted = np.minimum(np.r_[dlt[0], dlt],
                                np.r_[dlt, dlt[-1]])
    else:
        gap_sorted = np.ones(1)
    gap = np.empty(nY)
    gap[np.argsort(yn)] = np.maximum(gap_sorted, 1e-300)
    dx = np.min(np.abs(yn[:, None] - xp[None, :]), axis=1)
    dx = np.maximum(dx, 1e-300)
    F = np.column_stack([
        yn, wY, PYp, 1.0 / (PYp + 1e-300 * np.sign(PYp + 1e-30)),
        np.sqrt(wY), np.ones(nY), nyq, th, np.sign(PYp), gap, dx,
    ])
    vtop = HTM.v_top_from_Y(yn, wY)
    ones = np.ones(nY)
    cent = yn - float(np.mean(yn))
    return dict(
        C=C, meta=meta, ev=ev, psi=psi, F=F, vtop=vtop,
        ones=ones, cent=cent, nyq=nyq, yn=yn, wY=wY, nY=nY,
        nC=nC, nneg=nneg, Cmin=float(ev[0]),
        C2=float(ev[1]) if len(ev) > 1 else float("nan"),
        mz=mz, n=int(C.shape[0]), pk=pk,
    )


def pack_main(kz, n=None):
    mz = V.build_measures(kz)
    d = feat_pack(mz, n=n)
    d["tag"] = "MAIN-%d" % kz
    d["kz"] = kz
    d["legal"] = True
    return d


def pack_chi(kz, q, lpq, tag):
    mz = HM.chi_mz(kz, q, lpq)
    if mz is None:
        return None
    d = feat_pack(mz)
    d["tag"] = tag
    d["kz"] = kz
    d["legal"] = True
    d["holdout"] = True
    return d


# ---- Track A: grammar GP ----
def rand_tree(rng, depth):
    if depth <= 0 or rng.random() < 0.45:
        return ("t", int(rng.integers(0, len(FEAT_NAMES))))
    if rng.random() < 0.35:
        op = rng.choice(["neg", "inv", "abs", "sqrt", "sq"])
        return ("u", str(op), rand_tree(rng, depth - 1))
    op = rng.choice(["add", "sub", "mul", "div"])
    return ("b", str(op), rand_tree(rng, depth - 1),
            rand_tree(rng, depth - 1))


def eval_tree(tr, F):
    k = tr[0]
    if k == "t":
        return F[:, int(tr[1])]
    if k == "u":
        x = eval_tree(tr[2], F)
        op = tr[1]
        if op == "neg":
            return -x
        if op == "inv":
            return 1.0 / (x + 1e-12 * np.sign(x + 1e-30))
        if op == "abs":
            return np.abs(x)
        if op == "sqrt":
            return np.sqrt(np.abs(x))
        return x * x
    x = eval_tree(tr[2], F)
    y = eval_tree(tr[3], F)
    op = tr[1]
    if op == "add":
        return x + y
    if op == "sub":
        return x - y
    if op == "mul":
        return x * y
    return x / (y + 1e-12 * np.sign(y + 1e-30))


def fmt_tree(tr):
    if tr[0] == "t":
        return FEAT_NAMES[int(tr[1])]
    if tr[0] == "u":
        return "%s(%s)" % (tr[1], fmt_tree(tr[2]))
    return "(%s %s %s)" % (fmt_tree(tr[2]), tr[1], fmt_tree(tr[3]))


def tree_cos(tr, wins):
    cs = []
    for w in wins:
        v = eval_tree(tr, w["F"])
        cs.append(cosabs(v, w["psi"]))
    return float(min(cs)), cs


def mut_tree(rng, tr, depth):
    if rng.random() < 0.25:
        return rand_tree(rng, depth)
    if tr[0] == "t":
        return ("t", int(rng.integers(0, len(FEAT_NAMES))))
    if tr[0] == "u":
        return ("u", tr[1], mut_tree(rng, tr[2], depth - 1))
    if rng.random() < 0.5:
        return ("b", tr[1], mut_tree(rng, tr[2], depth - 1), tr[3])
    return ("b", tr[1], tr[2], mut_tree(rng, tr[3], depth - 1))


def xover_tree(rng, a, b):
    if a[0] == "t" or b[0] == "t" or rng.random() < 0.4:
        return b if rng.random() < 0.5 else a
    if a[0] == "u" and b[0] == "u":
        return ("u", a[1], xover_tree(rng, a[2], b[2]))
    if a[0] == "b" and b[0] == "b":
        if rng.random() < 0.5:
            return ("b", a[1], xover_tree(rng, a[2], b[2]), a[3])
        return ("b", a[1], a[2], xover_tree(rng, a[3], b[3]))
    return a


def seeded_trees():
    """Canonical + best seed INVPY.  Indices match FEAT_NAMES."""
    iY, iU, iPY, iINV, iSQ, i1, iN = 0, 1, 2, 3, 4, 5, 6
    return [
        ("t", i1),                                      # ones
        ("b", "sub", ("t", iY), ("t", i1)),             # Y-1 ~ centered
        ("t", iN),                                      # nyquist
        ("b", "div", ("t", i1),                         # v_top ~ 1/(sqrt(U) PY)
         ("b", "mul", ("t", iSQ), ("t", iPY))),
        ("t", iINV),                                    # 1/P_Y'
        ("t", 8),                                       # sign P_Y'
        ("b", "mul", ("t", iN), ("t", iSQ)),
        ("b", "mul", ("t", iINV), ("t", 10)),           # INVPY * DX
    ]


def run_gp(wins, seed, pop_n, ngen, depth):
    rng = np.random.default_rng(int(seed))
    pop = list(seeded_trees())
    while len(pop) < pop_n:
        pop.append(rand_tree(rng, depth))
    hist = []
    best_f, best_tr, best_cs = -1.0, pop[0], []
    for g in range(int(ngen)):
        scored = []
        for tr in pop:
            f, cs = tree_cos(tr, wins)
            scored.append((f, tr, cs))
        scored.sort(key=lambda z: -z[0])
        hist.append(float(scored[0][0]))
        if scored[0][0] > best_f:
            best_f, best_tr, best_cs = scored[0]
        keep = [s[1] for s in scored[: max(3, pop_n // 4)]]
        new = keep[:]
        while len(new) < pop_n:
            i = int(rng.integers(0, min(6, len(scored))))
            j = int(rng.integers(0, min(6, len(scored))))
            child = xover_tree(rng, scored[i][1], scored[j][1])
            if rng.random() < 0.45:
                child = mut_tree(rng, child, depth)
            new.append(child)
        pop = new
    return dict(best=best_f, tree=best_tr, expr=fmt_tree(best_tr),
                cs=best_cs, hist=hist)


def scalar_features(d):
    F = d["F"]
    wY = d["wY"]
    invpy = F[:, 3]
    gap = F[:, 9]
    return np.array([
        float(np.sum(wY)),
        float(np.sum(wY * wY)),
        float(np.sum(invpy)),
        float(np.mean(gap)),
        float(np.min(gap)),
        float(d["nY"]),
        float(np.sum(np.abs(F[:, 6]))),
        1.0,
    ], float)


def nnls_fit(X, y, niter, seed):
    """Projected gradient on c >= 0.  Deterministic."""
    rng = np.random.default_rng(int(seed))
    c = np.abs(rng.normal(0.0, 0.1, size=X.shape[1]))
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    XtX = X.T @ X
    Xty = X.T @ y
    eta = 1.0 / (float(np.linalg.norm(XtX)) + 1e-12)
    for _ in range(int(niter)):
        g = XtX @ c - Xty
        c = np.maximum(c - eta * g, 0.0)
    pred = X @ c
    res = float(np.linalg.norm(pred - y) / (np.linalg.norm(y) + 1e-30))
    return c, pred, res


# ---- Q toys ----
def toy_A_psi():
    """2-node: psi = e_0 = 1 - Y on Y={0,1}. Residual 0."""
    Y = np.array([0.0, 1.0])
    F = np.column_stack([
        Y, np.array([1.0, 4.0]), np.array([-1.0, 1.0]),
        np.array([-1.0, 1.0]), np.array([1.0, 2.0]),
        np.ones(2), np.array([1.0, -1.0]), np.array([0.5, 0.0]),
        np.array([-1.0, 1.0]), np.array([1.0, 1.0]),
        np.array([0.5, 0.5]),
    ])
    psi = np.array([1.0, 0.0])
    tr = ("b", "sub", ("t", 5), ("t", 0))  # ONES - Y
    v = eval_tree(tr, F)
    return dict(cos=cosabs(v, psi), exact=bool(v[0] == 1 and v[1] == 0),
                expr="ONES-Y")


def toy_B_lp():
    """r375 Q: det K2 = -7, identity residual 0 with c=1."""
    T = P2.haynsworth_blocks()
    S = P2.six_scalar_fractions(T)
    return dict(detK=T["detK"], gamma=S["gamma"], lam=S["lam"],
                fact=S["detK_fact"],
                ok=T["detK"] == Fr(-7) and S["gamma"] == Fr(9, 2)
                and S["lam"] == Fr(1) and S["detK_fact"] == T["detK"])


def toy_B2():
    """A0 = P - 2 e0 e0^T, Rest = 0, nneg=1."""
    P = np.diag([1.0, 1.0, 2.0, 3.0])
    v = np.array([math.sqrt(2.0), 0.0, 0.0, 0.0])
    A0 = np.diag([-1.0, 1.0, 2.0, 3.0])
    Rest = A0 - P + np.outer(v, v)
    evR = np.linalg.eigvalsh(0.5 * (Rest + Rest.T))
    evA = np.linalg.eigvalsh(A0)
    nneg = int(np.sum(evA < -1e-12))
    return dict(res=float(np.max(np.abs(Rest))), nneg=nneg,
                lminR=float(evR[0]),
                ok=float(np.max(np.abs(Rest))) < 1e-15 and nneg == 1)


def toy_C_detector():
    """nneg=2 toy is flagged.  Legal MAIN must NOT look like this."""
    A = np.diag([-1.0, -0.5, 2.0, 3.0])
    nneg = int(np.sum(np.linalg.eigvalsh(A) < -1e-12))
    return nneg >= 2, nneg


# ---- Track B2 family ----
def b2_scan(d, seed):
    """P = t0 I + t1 diag(u), v = v_top.  Max lmin(Rest)."""
    rng = np.random.default_rng(int(seed))
    evC, W = np.linalg.eigh(d["C"])
    lamR = evC / (1.0 + evC)
    A0 = (W * (lamR - 0.5)) @ W.T
    A0 = 0.5 * (A0 + A0.T)
    v = d["vtop"]
    I = np.eye(d["nY"])
    Dw = np.diag(d["wY"])
    best = (-1e300, 0.0, 0.0, 0)
    grid = np.array([0.25, 0.5, 1.0, 2.0, 4.0, 8.0])
    for t0 in grid:
        for t1 in np.r_[0.0, grid]:
            P = t0 * I + t1 * Dw
            Rest = A0 - P + np.outer(v, v)
            evR = np.linalg.eigvalsh(0.5 * (Rest + Rest.T))
            nnegR = int(np.sum(evR < -1e-10))
            if evR[0] > best[0]:
                best = (float(evR[0]), float(t0), float(t1), nnegR)
    # tiny random extra, still deterministic
    for _ in range(8):
        t0, t1 = float(rng.uniform(0.1, 10)), float(rng.uniform(0.0, 10))
        P = t0 * I + t1 * Dw
        Rest = A0 - P + np.outer(v, v)
        evR = np.linalg.eigvalsh(0.5 * (Rest + Rest.T))
        nnegR = int(np.sum(evR < -1e-10))
        if evR[0] > best[0]:
            best = (float(evR[0]), t0, t1, nnegR)
    return dict(lminR=best[0], t0=best[1], t1=best[2], nnegR=best[3],
                psd=best[0] >= -1e-10)


# ---- Track C legal grid ----
def legal_point(kz, dn):
    mz = V.build_measures(kz)
    n0 = int(mz["Nw"]) - 3
    n = n0 + int(dn)
    if n < 4:
        return None
    d = feat_pack(mz, n=n)
    d["tag"] = "MAIN-%d:n%+d" % (kz, dn)
    d["kz"] = kz
    d["dn"] = dn
    d["legal"] = True
    return d


def weight_scale(mz, eps):
    wp = np.asarray(mz["wp"], float) * (1.0 + float(eps))
    vn = np.asarray(mz["vn"], float) * (1.0 + float(eps))
    if np.any(wp <= 0) or np.any(vn <= 0):
        return None
    return P1.rebuild(mz, wp, vn)


# ---- parts ----
def part_satz():
    section("S1  Q TOYS (exact machinery)")
    A = toy_A_psi()
    check("G1-Q-psi-ONES-minus-Y",
          A["exact"] and A["cos"] >= 1.0 - 1e-15,
          "cos=%.3e expr=%s" % (A["cos"], A["expr"]))
    B = toy_B_lp()
    check("G2-Q-r375-factorization",
          B["ok"],
          "detK=%s gamma=%s lam=%s fact=%s"
          % (B["detK"], B["gamma"], B["lam"], B["fact"]))
    B2 = toy_B2()
    check("G3-Q-B2-rank1-split",
          B2["ok"],
          "Rest max=%.1e nneg(A0)=%d" % (B2["res"], B2["nneg"]))
    okC, n2 = toy_C_detector()
    check("G4-Q-nneg2-detector",
          okC,
          "diag(-1,-1/2,2,3) nneg=%d flagged" % n2)
    return A, B, B2


def part_split_and_train(smoke):
    section("S2  TRAIN PACK + CANONICAL COSINES + SPLIT WARD")
    train = []
    for kz in TRAIN_KZ:
        d = pack_main(kz)
        train.append(d)
        print("    %s nY=%d nC=%d Cmin=%.6f C2=%.10f"
              % (d["tag"], d["nY"], d["nC"], d["Cmin"], d["C2"]),
              flush=True)
    w9 = train[0]
    c_ones = cosabs(w9["ones"], w9["psi"])
    c_cent = cosabs(w9["cent"], w9["psi"])
    c_nyq = cosabs(w9["nyq"], w9["psi"])
    c_vtop = cosabs(w9["vtop"], w9["psi"])
    check("G10-w9-C-spectrum",
          w9["nC"] == 1
          and abs(w9["Cmin"] - W9_CMIN) < 5e-6
          and abs(w9["C2"] - W9_C2) < 5e-8,
          "Cmin=%.6f C2=%.10f" % (w9["Cmin"], w9["C2"]))
    check("G11-canonical-cosines-w9",
          abs(c_ones - W9_ONES) < 5e-4
          and abs(c_nyq - W9_NYQ) < 5e-4
          and abs(c_vtop - W9_VTOP) < 5e-4,
          "ones=%.4f cent=%.4f nyq=%.4f vtop=%.4f"
          % (c_ones, c_cent, c_nyq, c_vtop))
    inv = ("t", 3)
    f_inv, cs_inv = tree_cos(inv, train)
    check("G12-INVPY-uniform-bar",
          abs(f_inv - INVPY_MIN) < 5e-3 and f_inv < 0.2,
          "min-cos INVPY=%.4f on train %s (canonical uniform FAIL)"
          % (f_inv, " ".join("%.4f" % c for c in cs_inv)))
    tags = {d["tag"] for d in train}
    check("G13-train-is-MAIN-only",
          tags == {"MAIN-9", "MAIN-18", "MAIN-20"}
          and all(d["nC"] == 1 for d in train),
          "fitness universe = %s" % sorted(tags))
    return train, dict(ones=c_ones, nyq=c_nyq, vtop=c_vtop,
                       invpy=f_inv)


def part_track_a(train, smoke):
    section("S3  TRACK A  GP on psi_- / lam2-1 / q^dagger")
    pop = POP_A_SMOKE if smoke else POP_A_FULL
    ngen = GEN_A_SMOKE if smoke else GEN_A_FULL
    gp = run_gp(train, SEED_A, pop, ngen, DEPTH_A)
    print("    GP hist %s" % ", ".join("%.4f" % h for h in gp["hist"]),
          flush=True)
    print("    best expr %s" % gp["expr"], flush=True)
    check("G20-gp-ran-sealed",
          len(gp["hist"]) == ngen and gp["best"] >= 0.05,
          "pop=%d gen=%d best_min_cos=%.4f seed=%d"
          % (pop, ngen, gp["best"], SEED_A))
    # scalar targets
    y_lam = np.array([d["C2"] - 1.0 for d in train], float)
    X = np.vstack([scalar_features(d) for d in train])
    c, pred, res = nnls_fit(X, y_lam, LP_SMOKE if smoke else LP_FULL,
                            SEED_A + 1)
    check("G21-lam2-source-nnls",
          np.all(c >= -1e-15),
          "relres=%.3f pred=%s truth=%s"
          % (res, np.array2string(pred, precision=2),
             np.array2string(y_lam, precision=2)))
    qd = []
    for d in train:
        r = ER.row_of(d["kz"])
        qd.append(float(r["qdag"]))
        d["qdag"] = float(r["qdag"])
    yq = np.array(qd, float)
    cq, predq, resq = nnls_fit(X, yq, LP_SMOKE if smoke else LP_FULL,
                               SEED_A + 2)
    check("G22-qdag-source-nnls",
          abs(train[0]["qdag"] - W9_QDAG) < 1e-8,
          "w9 q^d=%.9f relres=%.3f pred=%s"
          % (train[0]["qdag"], resq,
             np.array2string(predq, precision=3)))
    exact = gp["best"] >= COS_EXACT
    cand = (not exact) and gp["best"] >= 0.9
    verd_a = ("FOUND_EXACT" if exact else
              "FOUND_CANDIDATE" if cand else "NOT_FOUND")
    return gp, dict(lam_res=res, q_res=resq, qdag=qd,
                    verd=verd_a, X=X, y_lam=y_lam, c_lam=c,
                    c_q=cq)


def part_track_b(train, smoke):
    section("S4  TRACK B  SOS/LP certificates")
    R = PX.build_rung(9)
    mz = R["mz"]
    cut = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       R["Nw"], R["S"], mz["L"], R["i1"], R["i2"],
                       keep=True)
    check("G30-w9-K2",
          cut["nneg"] == 1 and cut["P2"]
          and abs(cut["detK"] - W9_DETK) < 5e-4,
          "nneg=%d detK=%.6f P2=%s" % (cut["nneg"], cut["detK"],
                                       cut["P2"]))
    y = []
    Xs = []
    for d in train:
        Rd = PX.build_rung(d["kz"])
        m = Rd["mz"]
        ct = FTI.cut_rung(m["xu"], m["wu"], m["yn"], m["vn"],
                          Rd["Nw"], Rd["S"], m["L"],
                          Rd["i1"], Rd["i2"])
        y.append(float(-ct["detK"]))
        Xs.append(scalar_features(d))
        d["ndet"] = float(-ct["detK"])
        d["nnegA0"] = int(ct["nneg"])
    X = np.vstack(Xs)
    y = np.array(y, float)
    c, pred, res = nnls_fit(X, y, LP_SMOKE if smoke else LP_FULL, SEED_B)
    check("G31-LP-source-onto-ndet",
          res >= 0.0 and np.all(c >= -1e-15),
          "relres=%.3f c=%s (source-only; r375 identity uses psi_-)"
          % (res, np.array2string(c, precision=3)))
    b2 = b2_scan(train[0], SEED_B)
    check("G32-B2-family-not-PSD",
          not b2["psd"] and b2["lminR"] < -0.1,
          "best lmin(Rest)=%.4f at t0=%.2f t1=%.2f nnegR=%d "
          "(v=v_top source; remainder not PSD)"
          % (b2["lminR"], b2["t0"], b2["t1"], b2["nnegR"]))
    # r375 identity is EXACT but NOT source-pure (uses psi_-)
    s6 = P2.six_from_AU(cut["A0"], cut["U"])
    check("G33-r375-live-w9",
          abs(s6["detK_fact"] - cut["detK"]) < 1e-6
          and s6["gamma"] > s6["lam"],
          "fact=%.6f detK=%.6f gamma/lam=%.3f"
          % (s6["detK_fact"], cut["detK"], s6["gamma"] / s6["lam"]))
    exact = res < 1e-12 and b2["psd"]
    cand = (not exact) and res < 0.05
    verd_b = ("FOUND_EXACT" if exact else
              "FOUND_CANDIDATE" if cand else "NOT_FOUND")
    return dict(lp_res=res, c=c, pred=pred, y=y, b2=b2,
                verd=verd_b, s6=s6, cut=cut)


def part_track_c(smoke):
    section("S5  TRACK C  adversarial legal grid")
    kzs = TRAIN_KZ if smoke else CORE_KZ
    dns = (0,) if smoke else DEPTH_DN
    rows = []
    best_can = None
    fals_can = []
    trunc = []
    for kz in kzs:
        for dn in dns:
            d = legal_point(kz, dn)
            if d is None:
                continue
            rec = dict(kz=kz, dn=dn, nC=d["nC"], Cmin=d["Cmin"],
                       C2=d["C2"], tag=d["tag"])
            rows.append(rec)
            if dn == 0:
                if best_can is None or d["C2"] < best_can["C2"]:
                    best_can = rec
                if d["nC"] >= 2:
                    fals_can.append(rec)
            if dn < 0 and d["nC"] >= 2:
                trunc.append(rec)
            print("    %s nC=%d Cmin=%.8f C2=%.12f"
                  % (d["tag"], d["nC"], d["Cmin"], d["C2"]),
                  flush=True)
    check("G40-canonical-cut-no-nC2",
          len(fals_can) == 0 and best_can is not None,
          "canonical dn=0 points=%d best C2=%.12f at %s (C2-1=%.3e)"
          % (sum(1 for r in rows if r["dn"] == 0),
             best_can["C2"], best_can["tag"], best_can["C2"] - 1.0))
    if smoke:
        check("G40b-truncation-diagnostic-smoke",
              True,
              "smoke skips dn!=0 (r395 truncation table is full-only)")
    else:
        t2 = [r for r in trunc if r["dn"] == -2]
        check("G40b-truncation-is-r395-not-falsifier",
              len(t2) >= 4
              and {5, 18, 22, 38}.issubset({r["kz"] for r in t2}),
              "dn=-2 inflates nC=2 on %s (object is not A0; "
              "r395 truncation class); any dn<0 nC>=2: %s"
              % (sorted({r["kz"] for r in t2}),
                 sorted(set((r["kz"], r["dn"]) for r in trunc))))
    # tiny weight-scale GA on TRAIN only (geometry-preserving)
    rng = np.random.default_rng(SEED_C)
    mz9 = V.build_measures(9)
    ga_best = 1e9
    ga_nc = 0
    n_ga = 4 if smoke else GA_POP * GA_GEN
    for i in range(n_ga):
        eps = float(rng.uniform(-2e-4, 2e-4))
        mz = weight_scale(mz9, eps)
        if mz is None:
            continue
        d = feat_pack(mz)
        ga_best = min(ga_best, d["C2"])
        ga_nc = max(ga_nc, d["nC"])
    check("G41-weight-scale-GA",
          ga_nc <= 1,
          "n=%d best C2=%.10f max nC=%d (eps~1e-4, MAIN-9)"
          % (n_ga, ga_best, ga_nc))
    verd_c = "FALSIFIER_FOUND" if fals_can else "NOT_FOUND"
    return dict(rows=rows, best=best_can, fals=fals_can,
                trunc=trunc, verd=verd_c,
                ga_best=ga_best, ga_nc=ga_nc)


def part_holdout(train, gp, smoke):
    section("S6  HOLDOUT (never in fitness) + KILLS")
    holds = []
    chi_list = HOLDOUT_CHI[:2] if smoke else HOLDOUT_CHI
    for kz, q, lpq, tag in chi_list:
        d = pack_chi(kz, q, lpq, tag)
        if d is None:
            continue
        holds.append(d)
        print("    %s nC=%d Cmin=%.6f C2=%.10f"
              % (tag, d["nC"], d["Cmin"], d["C2"]), flush=True)
    if not smoke:
        dsel = pack_main(HOLDOUT_SEL_KZ)
        dsel["tag"] = "SEL-k7-%d" % HOLDOUT_SEL_KZ
        holds.append(dsel)
        print("    %s nC=%d Cmin=%.8f C2=%.10f"
              % (dsel["tag"], dsel["nC"], dsel["Cmin"], dsel["C2"]),
              flush=True)
        dext = pack_main(HOLDOUT_EXT_KZ)
        dext["tag"] = "EXT-%d" % HOLDOUT_EXT_KZ
        holds.append(dext)
        print("    %s nC=%d Cmin=%.8f C2=%.10f"
              % (dext["tag"], dext["nC"], dext["Cmin"], dext["C2"]),
              flush=True)
    nC2 = [h for h in holds if h["nC"] >= 2]
    check("G50-holdout-no-nC2",
          len(nC2) == 0,
          "holdout %d worlds, nC>=2 is %d (falsifier would fire)"
          % (len(holds), len(nC2)))
    # GP holdout cosine on nC=1 worlds
    h1 = [h for h in holds if h["nC"] == 1]
    if h1:
        f_h, cs_h = tree_cos(gp["tree"], h1)
    else:
        f_h, cs_h = float("nan"), []
    check("G51-gp-holdout-cosine",
          True,
          "best-train-expr holdout min-cos=%.4f on nC=1 %s"
          % (f_h, " ".join("%.4f" % c for c in cs_h)))
    mz9 = train[0]["mz"]
    mzP = P1.reweight(mz9, "permute", 43810)
    dP = feat_pack(mzP)
    mzS = HM.scramble_mz()
    dS = feat_pack(mzS)
    check("G52-permute-kills-P1",
          dP["nC"] >= PERM_NC_LO,
          "PERM nC=%d C2=%.4f (train formula must not survive)"
          % (dP["nC"], dP["C2"]))
    check("G53-scramble-kills-P1",
          dS["nC"] == SCR_NC,
          "SCR nC=%d C2=%.4f" % (dS["nC"], dS["C2"]))
    fP = cosabs(eval_tree(gp["tree"], dP["F"]), dP["psi"])
    fS = cosabs(eval_tree(gp["tree"], dS["F"]), dS["psi"])
    check("G54-kills-break-or-are-nC-inflated",
          dP["nC"] >= 15 and dS["nC"] >= 15,
          "expr cos PERM=%.3f SCR=%.3f (nC already 21; "
          "defect direction is no longer unique)"
          % (fP, fS))
    # illegal arch-parity control (NOT a falsifier)
    uu, ww, _, _ = DMF.chi_window_comb(9, DMF.Q_CHI3)
    mz_bad = DMF.chi_build_measures(9, uu, ww, 0.0, DMF.LPQ3)
    d_bad = feat_pack(mz_bad)
    check("G55-illegal-a0-control",
          d_bad["nC"] == CHI3_A0_NC,
          "CHI3 a=0 (wrong Gamma parity) nC=%d -- geometry "
          "destroyed, typed CONTROL not falsifier"
          % d_bad["nC"])
    return dict(holds=holds, f_h=f_h, dP=dP, dS=dS,
                nC2=nC2, d_bad=d_bad)


def verdict_of(va, vb, vc, gp, hold):
    if vc == "FALSIFIER_FOUND" or hold["nC2"]:
        return "FALSIFIER_FOUND"
    return "A:%s B:%s C:%s" % (va, vb, vc)


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("evolutionary_certificate_probe -- "
          "PRIME.SEARCH.EVOLUTIONARY_CERTIFICATE.01 (round 438)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (train {9,18,20}; holdout chi/EXT/sel k>=7)"))
    print("split: TRAIN=%s  HOLDOUT=chi3/chi4+EXT-%d+SEL-%d"
          % (list(TRAIN_KZ), HOLDOUT_EXT_KZ, HOLDOUT_SEL_KZ))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA + BUDGET")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HTM.SPEC_SHA.startswith(HTM_SHA_PREFIX)
              and ER.SPEC_SHA.startswith(ER_SHA_PREFIX)
              and FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "DI %s HTM %s ER %s FTI %s HM %s P1 %s"
          % (DI.SPEC_SHA[:8], HTM.SPEC_SHA[:8], ER.SPEC_SHA[:8],
             FTI.SPEC_SHA[:8], HM.SPEC_SHA[:8], P1.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no curve_fit" if not ag else "; ".join(ag))
    check("G00d-sealed-budget",
          POP_A_FULL == 24 and GEN_A_FULL == 10 and SEED_A == 43801
          and SEED_B == 43802 and SEED_C == 43803
          and HOLDOUT_SEL_KZ == 43,
          "A pop/gen %d/%d  B lp %d  C grid %dx%d"
          % (POP_A_FULL, GEN_A_FULL, LP_FULL,
             len(CORE_KZ), len(DEPTH_DN)))

    part_satz()
    train, can = part_split_and_train(smoke)
    gp, ta = part_track_a(train, smoke)
    tb = part_track_b(train, smoke)
    tc = part_track_c(smoke)
    hold = part_holdout(train, gp, smoke)

    section("S7  VERDICT")
    va, vb, vc = ta["verd"], tb["verd"], tc["verd"]
    if hold["nC2"]:
        vc = "FALSIFIER_FOUND"
    summary = verdict_of(va, vb, vc, gp, hold)
    prev = all(ok for _n, ok in CHECKS)
    check("G60-verdict",
          prev,
          "%s  A best_min_cos=%.4f expr=%s  B lp_res=%.3f "
          "B2 lminR=%.3f  C best C2-1=%.3e"
          % (summary, gp["best"], gp["expr"], tb["lp_res"],
             tb["b2"]["lminR"],
             (tc["best"]["C2"] - 1.0) if tc["best"] else float("nan")))
    n_ok = sum(1 for _n, ok in CHECKS if ok)
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, summary))
    print("NO RH CLAIM.  NO L* CLAIM.  NO R-dagger CLAIM.")
    if n_ok != len(CHECKS):
        sys.exit(1)


if __name__ == "__main__":
    main()
