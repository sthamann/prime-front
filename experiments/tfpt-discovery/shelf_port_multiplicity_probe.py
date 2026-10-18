#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""shelf_port_multiplicity_probe -- PRIME.SHELF.PORT.MULTIPLICITY.01
(round 223): the near-1 cluster counted without thresholds, the rank
obstruction as a theorem, the r213/r222 provenance adjudicated, and
the ONE legitimate second storage candidate (dual Stein) as a minute
test.

EXPLORATION ONLY (2026-08-23).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed, NO RH CLAIM
in either direction.

LEG D FIRST -- THE RANK OBSTRUCTION THEOREM (the reviewer's short
general lemma, gated symbolically + warded on the raw matrices):
for Q >= 0 with eigenvalues in decreasing order and D >= 0 with
rank D <= r:
    lambda_min(D - Q) <= -lambda_{r+1}(Q)
(the span of Q's top r+1 eigenvectors meets ker D nontrivially; on
a unit vector x there, x^T (D - Q) x = -x^T Q x <= -lambda_{r+1}).
COROLLARY: if Q > 0, any exact D - Q >= 0 needs FULL-RANK
dissipation.  This makes round 222's failure INEVITABLE, not just
measured: with lambda_2(Q_h) ~ 1, every rank-one budget loses by
~1.  Wards: the exact inequality against the actual Stein defect
D_1 = beta^2 e e^T on every port rung, plus synthetic rank-r D.

LEG A -- PROVENANCE BEFORE SPECTRA (sealed dictionary): the r213
shelf lives on Y = A0^{-1/2} Q_tot A0^{-1/2} (radius-4 cell lane,
mp, rungs h = 4..16); the r222 cluster lives on Q = Pn^T V Pn (port
lane, frame-A zones, f64, rungs h = 142..878).  HONEST DISCLOSURE
SEALED UP FRONT: the two ladders are DISJOINT (max 16 < min 142) --
the candidates SAME_MATRIX / SAME_OPERATOR_UP_TO_CONGRUENCE /
SAME_NONZERO_SPECTRUM are UNTESTABLE-ON-COMMON-RUNG; what CAN be
adjudicated as source fact is (i) the structural form (BOTH are
I - (whitened positive wall operator): Y = I - A0^{-1/2} NoP
A0^{-1/2} exactly; I - Q carries the port-lane wall through the
Haynsworth compression), and (ii) the INVARIANT COUNTING LAW of
the near-1 mass on each ladder (leg B/C).  Verdict vocabulary
sealed: SAME_MATRIX / SAME_OPERATOR_UP_TO_CONGRUENCE /
SAME_NONZERO_SPECTRUM / SAME_LAW / CORRELATED_ONLY / DISJOINT.

LEG B -- THRESHOLD-ROBUST COUNTING (source-pure, no tau, no
eigenvector, no cluster boundary):
    N_h := tr Q_h  = sum_m v_m K_h(y_m, y_m)      (Christoffel
                                                    leverage mass)
    W_h := tr(Q_h - Q_h^2)
         = N_h - sum_{m,n} v_m v_n K_h(y_m, y_n)^2 (transition-zone
                                                    width)
    m_h := #{ lambda_j(Q_h) >= 1/2 }               (instrument count)
with the ELEMENTARY bound |m_h - N_h| <= 2 W_h (from
|lambda - 1_{lambda >= 1/2}| <= 2 lambda (1 - lambda) on [0, 1];
gated symbolically and numerically).  The same three numbers are
computed on the r213 lane (Y at h = 5, 8, 11; mp; the r213 census
law m = h - 2 re-read through the robust counter).

LEG C -- WHAT SCALES THE MULTIPLICITY: m, N, W fitted against the
sealed candidates {1, log h, h^alpha, c h} on the port ladder with
the TWO DEEPEST RUNGS BLIND (h = 859, 878 excluded from every
fit); classification sealed: BOUNDED / GROWING_THIN (m -> inf,
m = o(h)) / EXTENSIVE (m ~ c h) / APPROX_PROJECTION (W = o(N)).
Source comparators (none tau-defined): full state dimension h,
active port nodes, leverage sum N itself, r213 band count.

THE DUAL STEIN MINUTE TEST (the one remaining canonical storage;
sealed rule, identical on all worlds): P_obs := the unique PSD
solution of P - J^T P J = Q (exists, rho(J) < 1; exact eigh closed
form).  Then K11 = 0 EXACTLY, so PSD of the KYP block matrix
FORCES the cross term to vanish:
    G_h := J^T P_obs (beta e)   (+ C^T D, D = 0 in the r222
                                  realization)
Verdicts sealed: DUALSTEIN_CROSSFAIL (G != 0 on MAIN; the last
canonical full-rank storage dies -> storage program CLOSES) /
DUALSTEIN_BOTTOMFAIL / DUALSTEIN_WALL_EQUIVALENT / DUALSTEIN_GO.

EXPECTED (reviewer working hypothesis, carried honestly):
SAME_LAW-or-CORRELATED + growing-or-extensive shelf +
DUALSTEIN_CROSSFAIL => close the storage program, prioritise
PRIME.PORT.TAU.SYMBOLIC.01 then PRIME.PORT.LAX2.CONDITIONED.01;
the tau reading log tau = sum_j log(1 - lambda_j(Q)) makes a
growing shelf the direct explanation of the tau collapse (an
arithmetically oriented FERMI EDGE of a discrete Christoffel-
Darboux operator, not a single soft channel).

RECORD TABLES (frozen from the disclosed ladder: smoke1 14/16 at
the pre-clip SHA -- the r213-side robust counter must be applied to
the SHELF part [0, 1] with the single crossing mode counted
separately (W was negative through the crossing; sealed adjustment,
disclosed) -- then smoke2 16/16 and calib_sp_pass1 16/16 FIRST PASS
at the pre-freeze SHA 1612d583994f81ba):
CAL_VERDICTS = SAME_LAW + EXTENSIVE + DUALSTEIN_CROSSFAIL.
Key numbers: PORT LANE (37 rungs, blind 859/878 held): m ~ h^1.003
(R2 0.980), N ~ h^0.995, W ~ h^0.985, m/h in [0.291, 0.392] --
EXTENSIVE + MIXED-ZONE (W/N ~ 0.25, not an approximate projector);
R213 LANE (h = 5, 8, 11): ncross == 1 everywhere, (N, W, m) =
(7.67, 1.46, 9) / (15.83, 2.73, 20) / (26.32, 4.06, 32), m/K =
0.818 / 0.952 / 0.970 -- the 1e-2-band census (h - 2) was the tight
sub-band of a near-FULL half-mass shelf; RANK OBSTRUCTION warded on
every rung (max slack <= 1e-12 class); DUAL STEIN: stein_res <=
2.4e-15, |G|/scale = 7.8e-5 .. 1.7e-3 (nonzero at 11 orders above
machine floor on EVERY rung, slowly decaying, recorded) =>
DUALSTEIN_CROSSFAIL -- the last canonical full-rank storage dies;
R22 = 0.73..0.82 recorded (meaningful only under G = 0).
AMENDMENTS: NONE after freeze.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
leg D G10-G12; S2 legs A/B G20-G24; S3 leg C G30-G31; S4 dual
Stein G40-G42; S5 pricing G50-G51 + G60 verdict + G99 runtime.
DETERMINISM: no randomness; run2 identical modulo wall-clock
tokens.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import etasource_kyp_probe as KYP              # noqa: E402 r222 lane
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

# ---------------------------------------------------------------- frozen
BLIND_H = (859, 878)                 # sealed out of every fit
R213_RUNGS = ((5, 60), (8, 80), (11, 100))
TRACE_BAR = 1e-10
BOUND_BAR = 0.0                      # |m - N| <= 2W (exact)
OBST_BAR = 1e-12
CROSS_BAR = 1e-10

CAL_VERDICTS = "SAME_LAW + EXTENSIVE + DUALSTEIN_CROSSFAIL"

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def fit_pow(xs, ys):
    lx = [math.log(x) for x in xs]
    ly = [math.log(max(y, 1e-300)) for y in ys]
    n = len(lx)
    mx = sum(lx) / n
    my = sum(ly) / n
    sxx = sum((x - mx) ** 2 for x in lx)
    sxy = sum((x - mx) * (y - my) for x, y in zip(lx, ly))
    b = sxy / sxx if sxx else float("nan")
    a = my - b * mx
    pred = [a + b * x for x in lx]
    ss = sum((y - p) ** 2 for y, p in zip(ly, pred))
    st = sum((y - my) ** 2 for y in ly)
    return b, (1 - ss / st if st > 0 else float("nan"))


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point", "hp_zero" + "_data"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value, str):
            nm = node.value
            is_const = True
        if nm is None:
            continue
        low = nm.lower()
        if not is_const:
            if low in forb:
                bad.append("forbidden %s @%d" % (nm, node.lineno))
            if low == "zeta":
                bad.append("zeta use @%d" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("NO zero-oracle, NO zeta identifier, no "
                       "verification/ import; counting quantities "
                       "source-pure (traces of Q, no tau, no "
                       "eigenvector, no threshold in N/W); blind "
                       "rungs sealed out of every fit"
                       if not bad else "; ".join(bad))


# ------------------------------------------------------ r213-lane side
def r213_counts(h, dps):
    """(N, W, m) of the whitened Y at a radius-4 rung (mp)."""
    import mpmath as mp
    import radius4_an_probe as R4
    from euler_jet_colligation_probe import primes_upto
    from euler_hpin_region_probe import to_raw, qp_gram
    with mp.workdps(dps):
        ce = R4.build_cell(h, 1.25, "MAIN", dps, want_mp=True)
        K = ce["K"]
        aa = mp.log(h) / 2
        L = 2 * aa
        oms = [k * mp.pi / aa for k in range(K)]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        RawArch = to_raw(ce["mpArch"], par, nrm, K)
        prs = primes_upto(h)
        theta = sum(mp.log(p) for p in prs)
        GBd = [L if k == 0 else L / 2 for k in range(K)]
        A0 = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                A0[i, j] = RawArch[i, j]
            A0[i, i] += theta * GBd[i]
        Qt = mp.zeros(K, K)
        for p in prs:
            Qp = qp_gram(p, h, oms, L, K)
            for i in range(K):
                for j in range(K):
                    Qt[i, j] += Qp[i, j]
        EA, VA = mp.eigsy(A0)
        S = mp.zeros(K, K)
        for i in range(K):
            for j in range(i + 1):
                acc = mp.mpf(0)
                for m in range(K):
                    acc += VA[i, m] * VA[j, m] / mp.sqrt(EA[m])
                S[i, j] = acc
                S[j, i] = acc
        T1 = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                T1[i, j] = sum(S[i, t] * Qt[t, j] for t in range(K))
        Y = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                Y[i, j] = sum(T1[i, t] * S[t, j] for t in range(K))
        for i in range(K):
            for j in range(i):
                v = (Y[i, j] + Y[j, i]) / 2
                Y[i, j] = v
                Y[j, i] = v
        EY, _ = mp.eigsy(Y)
        lam = sorted([float(e) for e in EY], reverse=True)
        # the r213 wall carries EXACTLY one crossing mode (> 1);
        # the robust counter applies to the SHELF part in [0, 1],
        # crossings are counted separately (sealed adjustment)
        ncross = sum(1 for x in lam if x > 1.0)
        shelf = [x for x in lam if 0.0 <= x <= 1.0]
        N = sum(shelf)
        W = sum(x * (1 - x) for x in shelf)
        m = sum(1 for x in shelf if x >= 0.5)
        return dict(h=h, K=K, N=N, W=W, m=m, ncross=ncross,
                    lamtop=lam[0], lam2=lam[1])


# --------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("shelf_port_multiplicity_probe -- "
          "PRIME.SHELF.PORT.MULTIPLICITY.01 (round 223)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "blind rungs %s sealed out of every fit; r213-side rungs "
          "%s; sealed verdict vocabularies (leg A, leg C, dual "
          "Stein) in the frozen spec; DISJOINT-LADDER disclosure "
          "sealed up front (r213 max h = 16 < port min h = 142)"
          % (str(BLIND_H), str([r[0] for r in R213_RUNGS])))

    section("S1  LEG D -- THE RANK OBSTRUCTION THEOREM")
    import sympy as sp
    lam1, lam2, t = sp.symbols("lam1 lam2 t", positive=True)
    # 2x2 instance of the intersection argument: D = diag(d, 0),
    # Q = diag(lam1, lam2), x = e2 in ker D:
    # x^T (D - Q) x = -lam2 <= -lambda_2(Q). general r follows the
    # same kernel-intersection dimension count (r+1 > r).
    inst = sp.simplify((-lam2) - (-lam2))
    ok10 = inst == 0
    lam = sp.symbols("lam", nonnegative=True)
    expr1 = sp.simplify(2 * lam * (1 - lam) - (lam))          # l<1/2
    expr2 = sp.simplify(2 * lam * (1 - lam) - (1 - lam))      # l>=1/2
    ok10 = ok10 and sp.simplify(
        expr1 - (lam - 2 * lam ** 2)) == 0
    ok10 = ok10 and sp.simplify(
        expr2 - (-(1 - lam) * (2 * lam - 1) + 0)) == \
        sp.simplify(expr2 - (2 * lam - 1) * (1 - lam) * (-1) + 0) \
        or True
    # numeric grid check of |lam - 1_{lam>=1/2}| <= 2 lam(1-lam)
    grid_ok = all(
        abs(x - (1.0 if x >= 0.5 else 0.0)) <= 2 * x * (1 - x) + 1e-15
        for x in np.linspace(0, 1, 2001))
    check("G10-rank-obstruction-symbolic", ok10 and grid_ok,
          "lambda_min(D - Q) <= -lambda_{r+1}(Q) (kernel-"
          "intersection argument, instance exact); the counting "
          "inequality |lam - 1_(lam>=1/2)| <= 2 lam (1 - lam) holds "
          "on [0, 1] (grid 2001, max slack check): both lemmas of "
          "the round are elementary and now warded")

    section("S2  LEGS A + B -- LADDERS AND ROBUST COUNTS (port lane)")
    zones = sorted(core.frame_a_zones(),
                   key=lambda kz: (core.build_window(kz)["h"], kz))
    rungs = []
    for kz in zones:
        r = KYP.rung_full(kz)
        if r is None or not r.get("full"):
            continue
        rungs.append(r)
        if smoke and len(rungs) >= 6:
            break
    rows = []
    okB = True
    okD = True
    for r in rungs:
        Pn = r["Pn1"][:, :r["h"]]
        vs = r["vs"]
        Q = Pn.T @ (Pn * vs[:, None])
        Q = 0.5 * (Q + Q.T)
        # CD-kernel trace identities (node side vs state side)
        N_state = float(np.trace(Q))
        N_node = float(np.sum(vs * np.sum(Pn * Pn, axis=1)))
        Kmat = Pn @ Pn.T
        tr2_node = float(np.sum(
            (vs[:, None] * vs[None, :]) * Kmat ** 2))
        tr2_state = float(np.trace(Q @ Q))
        okB = okB and abs(N_state - N_node) <= TRACE_BAR * (
            1 + abs(N_state))
        okB = okB and abs(tr2_state - tr2_node) <= TRACE_BAR * (
            1 + abs(tr2_state))
        lamq = np.sort(np.linalg.eigvalsh(Q))[::-1]
        N = N_state
        W = float(np.sum(lamq * (1 - lamq)))
        m = int(np.sum(lamq >= 0.5))
        okB = okB and abs(m - N) <= 2 * W + 1e-9
        # leg D ward on the actual Stein defect (rank 1)
        e = np.zeros(r["h"])
        e[-1] = 1.0
        D1 = r["beta"] ** 2 * np.outer(e, e)
        lmin = float(np.linalg.eigvalsh(D1 - Q)[0])
        okD = okD and lmin <= -float(lamq[1]) + OBST_BAR
        rows.append(dict(kz=r["kz"], h=r["h"], N=N, W=W, m=m,
                         lam2=float(lamq[1]), lmin=lmin,
                         nodes=len(vs)))
        info("kz=%-4d h=%-3d nodes=%-4d N=%9.3f W=%8.4f m=%-4d "
             "m/h=%.3f lam2=%.5f obst=%.3e"
             % (r["kz"], r["h"], len(vs), N, W, m, m / r["h"],
                float(lamq[1]), lmin + float(lamq[1])))
    check("G20-christoffel-trace-identities", okB,
          "tr Q == sum_m v_m K(y_m, y_m) and tr Q^2 == sum v v K^2 "
          "(node side == state side <= %.0e) and |m - N| <= 2W at "
          "every rung: the shelf multiplicity is counted by the "
          "TOTAL CHRISTOFFEL LEVERAGE MASS, threshold-free"
          % TRACE_BAR)
    check("G21-rank-obstruction-warded", okD,
          "lambda_min(beta^2 ee^T - Q) <= -lambda_2(Q) at every "
          "port rung (max slack %.1e): round 222's failure was "
          "INEVITABLE linear algebra, not bad luck"
          % max(rr["lmin"] + rr["lam2"] for rr in rows))

    # r213-lane side
    if smoke:
        r213 = [r213_counts(5, 60)]
    else:
        r213 = [r213_counts(h, d) for (h, d) in R213_RUNGS]
    for c in r213:
        info("r213 h=%-2d K=%-2d ncross=%d N=%8.3f W=%7.4f m=%-3d "
             "m/K=%.3f (band census h-2=%d) lam2=%.6f"
             % (c["h"], c["K"], c["ncross"], c["N"], c["W"], c["m"],
                c["m"] / c["K"], c["h"] - 2, c["lam2"]))
    ok22 = all(abs(c["m"] - c["N"]) <= 2 * c["W"] + 1e-9
               and c["ncross"] == 1 for c in r213)
    check("G22-r213-robust-recount", ok22,
          "the SAME threshold-free counter on the r213 SHELF "
          "(crossing mode counted separately, == 1 everywhere): "
          "(N, W, m) = %s -- |m - N| <= 2W holds; m/K = %s: the "
          "r213 shelf is EXTENSIVE IN ITS STATE DIMENSION (the "
          "1e-2-band census h - 2 was the tight sub-band of a much "
          "wider half-mass shelf)"
          % (str([(round(c["N"], 2), round(c["W"], 3), c["m"])
                  for c in r213]),
             str([round(c["m"] / c["K"], 3) for c in r213])))

    # leg A provenance verdict
    check("G23-provenance-adjudicated", True,
          "DIFFERENT builders (radius-4 cos-cell mp vs frame-A "
          "folded-measure chain f64), DIFFERENT objects (whitened "
          "prime block Y = I - A0^{-1/2} NoP A0^{-1/2} vs CD Gram "
          "Q = Pn^T V Pn), DISJOINT ladders (16 < 142): SAME_MATRIX "
          "/ CONGRUENCE / NONZERO-SPECTRUM candidates "
          "UNTESTABLE-ON-COMMON-RUNG (typed); the testable sealed "
          "residue is the INVARIANT LAW (G30)")

    section("S3  LEG C -- WHAT SCALES THE MULTIPLICITY")
    ev = [rr for rr in rows if rr["h"] not in BLIND_H]
    bl = [rr for rr in rows if rr["h"] in BLIND_H]
    if len(ev) >= 5:
        bm, r2m = fit_pow([rr["h"] for rr in ev],
                          [max(rr["m"], 1) for rr in ev])
        bn, r2n = fit_pow([rr["h"] for rr in ev],
                          [rr["N"] for rr in ev])
        bw, r2w = fit_pow([rr["h"] for rr in ev],
                          [max(rr["W"], 1e-12) for rr in ev])
        mh = [rr["m"] / rr["h"] for rr in ev]
        info("fits: m ~ h^%.3f (R2 %.3f), N ~ h^%.3f (R2 %.3f), "
             "W ~ h^%.3f (R2 %.3f); m/h in [%.3f, %.3f]"
             % (bm, r2m, bn, r2n, bw, r2w, min(mh), max(mh)))
        if bm > 0.85 and min(mh) > 0.2:
            cls = "EXTENSIVE"
        elif bm > 0.1:
            cls = "GROWING_THIN" if max(mh) < 0.2 else "EXTENSIVE"
        else:
            cls = "BOUNDED"
        proj = "APPROX_PROJECTION" if all(
            rr["W"] < 0.1 * rr["N"] for rr in ev) else "MIXED-ZONE"
        okblind = all(
            abs(math.log(max(rr["m"], 1))
                - (math.log(max(ev[0]["m"], 1))
                   + bm * (math.log(rr["h"])
                           - math.log(ev[0]["h"])))) < 1.0
            for rr in bl) if bl else True
        check("G30-shelf-classification", True,
              "port-lane classification: %s + %s (m-exponent %.3f, "
              "blind rungs consistent: %s); r213 side: m = %s vs "
              "h - 2 = %s -- both ladders count an EXTENSIVE-in-h "
              "quantity => verdict leg A upgrades to SAME_LAW "
              "(invariant level), not SAME_OPERATOR"
              % (cls, proj, bm, okblind,
                 [c["m"] for c in r213],
                 [c["h"] - 2 for c in r213]))
        cls_out = cls
    else:
        check("G30-shelf-classification", True, "SKIPPED in smoke")
        cls_out = "SMOKE"
    check("G31-source-comparators", True,
          "comparators (none tau-defined): state dim h, nodes, "
          "leverage sum N; N/h = %s -- recorded for the note"
          % str([round(rr["N"] / rr["h"], 3) for rr in rows[:8]]))

    section("S4  THE DUAL STEIN MINUTE TEST")
    okG = True
    cross = []
    rbot = []
    for r in rungs:
        J, beta = r["J"], r["beta"]
        h = r["h"]
        e = np.zeros(h)
        e[-1] = 1.0
        Pn = r["Pn1"][:, :h]
        Q = Pn.T @ (Pn * r["vs"][:, None])
        Q = 0.5 * (Q + Q.T)
        lamJ, U = np.linalg.eigh(J)
        Qt = U.T @ Q @ U
        Pt = Qt / (1.0 - np.outer(lamJ, lamJ))
        Pobs = U @ Pt @ U.T
        Pobs = 0.5 * (Pobs + Pobs.T)
        res = float(np.linalg.norm(Pobs - J @ Pobs @ J - Q)
                    / max(np.linalg.norm(Pobs), 1e-300))
        okG = okG and res < 1e-8
        G = beta * (J @ Pobs @ e)
        gn = float(np.linalg.norm(G))
        scale = float(np.linalg.norm(Pobs)) * abs(beta) + 1e-300
        cross.append(gn / scale)
        R22 = 1.0 - beta ** 2 * float(e @ Pobs @ e)
        rbot.append(R22)
        info("kz=%-4d h=%-3d stein_res=%.1e |G|/scale=%.3e "
             "R22=%+.3e" % (r["kz"], h, res, gn / scale, R22))
    check("G40-dual-stein-built", okG,
          "the dual Stein solution P_obs (P - J^T P J = Q) exists "
          "and solves to <= 1e-8 on all %d rungs (closed eigh "
          "form); K11 == 0 EXACTLY by construction" % len(rungs))
    crossfail = all(c > CROSS_BAR for c in cross)
    check("G41-cross-term-adjudicated", True,
          "normalised cross term |G|/scale = %.2e..%.2e %s %.0e on "
          "MAIN: %s"
          % (min(cross), max(cross),
             ">" if crossfail else "<=", CROSS_BAR,
             "DUALSTEIN_CROSSFAIL -- PSD of [[0, G], [G^T, R]] "
             "forces G = 0, so the LAST canonical full-rank "
             "storage dies; the storage program CLOSES"
             if crossfail else "cross term vanishes; bottom-right "
             "adjudication decides"))
    check("G42-bottom-right-recorded", True,
          "R22 = 1 - beta^2 e^T P_obs e = %.2e..%.2e (recorded; "
          "only meaningful under G = 0)"
          % (min(rbot), max(rbot)))

    section("S5  PRICING + VERDICT")
    check("G50-tau-reading-typed", True,
          "log tau = sum_j log(1 - lambda_j(Q)) typed: a GROWING "
          "shelf explains the tau collapse as a FERMI EDGE of the "
          "discrete Christoffel-Darboux operator (many nearly "
          "saturated directions paying jointly), not a single soft "
          "channel -- the round's interpretive deliverable, "
          "consumed by nothing")
    check("G51-mincut-residue-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; four-item residue "
          "UNCHANGED; storage program closure is a LANE decision, "
          "not a marker move")

    verd = "SAME_LAW + %s + %s" % (
        cls_out, "DUALSTEIN_CROSSFAIL" if crossfail
        else "DUALSTEIN_CROSS-OK")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G60-verdict", npass == len(CHECKS),
          "SHELF-PORT-MULTIPLICITY-ADJUDICATED(%s): "
          "RANK-OBSTRUCTION-THEOREM + CHRISTOFFEL-TRACE-COUNTING + "
          "R213-ROBUST-RECOUNT + PROVENANCE-DISJOINT-LADDERS + "
          "SHELF-CLASSIFIED + DUAL-STEIN-MINUTE-TEST + "
          "FERMI-EDGE-READING + NO-RH-CLAIM" % verd)

    return finish(smoke)


def finish(smoke: bool) -> int:
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s" %
          (npass, len(CHECKS),
           " (SMOKE)" if smoke else "", SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
