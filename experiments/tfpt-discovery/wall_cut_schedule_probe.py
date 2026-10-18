#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wall_cut_schedule_probe -- PRIME.PORT.CUT.SCHEDULE.01
(EXPLORATION ONLY, experiments/; round 60, theorem-engineering on
the RH-side wall; successor of wall_head_tail_bound_probe (round
59): no SINGLE head cut covers all rungs (n <= 50: 52/67, n <= 100:
26/67, n <= 200: 25/67 -- different subsets, overshoot mechanism).
THE QUESTION: does a PER-RUNG cut schedule c(h) exist such that
explicit-head + certified null-tail covers EVERY rung, is it
structured, and which atoms carry the overshoot?  2026-08-10.)

THE SPLIT (round-59 verbatim, exact).  On the lift-race surface
(m_h = lam_min(K) = lift_h - demand_h exactly), cut at u_c:
    head_err(c) = sum_{u_n <= u_c} mu_n q_v(u_n) - int_{u <= u_c},
    tail_err(c) = lift - head_err(c)                [SPLIT-EXACT]
    G(c) := head_err(c) - demand,   m = G(c) + tail_err(c).
COVERAGE (frozen, two senses): COVER-G(c) iff G(c) > 0 (a
one-sided tail bound |tail| < G would close the rung); COVER-CERT
(c) iff G(c) - |tail_err(c)| > 0 (the null-tail estimate closes
the rung from the explicit head alone).  EXACT ALGEBRA (warded):
cert(c) = m - tail - |tail|, so cert = m iff tail(c) <= 0 and
cert = m - 2 tail iff tail(c) > 0; cert(c) <= m ALWAYS -- a
covering cut can never beat the margin itself, and NO cut covers
when m <= 0 (which is what the controls must show).  SAID PLAINLY
(frozen): the cut set is the deployed ATOM POSITIONS (each cut =
"include the explicit window atoms n' <= n"); a covering cut is a
MEASURED SURFACE STATEMENT -- the tail beyond any cut still needs
its (here: null) bound proved; nothing here is a tail theorem.

WHAT IS MEASURED (frozen; typed, never kills):
 (a) THE COVERAGE MATRIX: per rung, coverage over ALL atom cuts
     (counts, first covering cut n_min, best cut n_best, best
     margin); the union answer FULL-COVERAGE(n/N) iff every rung
     has >= 1 CERT-covering cut, with the schedule depth ladder
     n_min(h); cap table: rungs coverable with some cut <= NCAP
     for NCAP in CAPS.
 (b) STRUCTURE of the minimal schedule: OLS + jackknife of
     log n_min vs log h and vs alpha; monotonicity (concordant
     pair fraction); the node tie corr(u_min, u*(alpha)) with the
     prime-free drift law u* = (NODE_C + NODE_S alpha) alpha
     (declared input).  TYPED: SCHEDULE-STRUCTURED(R2) iff the
     best of the two fits has R^2 >= STRUCT_R2, else
     SCHEDULE-UNSTRUCTURED(R2).  Plus the GREEDY MINIMAL GLOBAL
     SCHEDULE (set cover over shared cut values; greedy is an
     upper bound, said plainly): size + the chosen cuts.
 (c) THE OVERSHOOT MECHANISM: per-atom net increments inc_n =
     mu_n q_v(u_n) - (smooth slice between consecutive atoms), so
     G(c_i) = sum_{k <= i} inc_k - demand exactly (warded); the
     50 -> 100 window: Delta G = G(100) - G(50) ladder (med, sign
     counts -- WHY less head helps); the atom ledger: med_h
     inc_n for every atom value n <= N_ANAT, top NEG / top POS
     atoms printed with their prime-power structure (integer-root
     factorization of the deployed atom values; no primality
     oracle -- the table is the deployed comb).
 (d) TAU-SCREEN (mandatory; on this surface the wall margin IS
     m_h): slope of log(best cert margin) vs log m_h -- by the
     exact algebra above the unrestricted best margin can only be
     <= m, so a slope ~ +1 is STRUCTURAL, not a finding (said in
     the type); the informative screen is the RESTRICTED one at
     cuts n <= NCAP_SCREEN on the rungs it covers.  Bands PASS
     |s| <= 0.30 / RELOC s >= 0.70 / else AMBIG.

FROZEN PROTOCOL (machinery verbatim from
wall_head_tail_bound_probe = probe-4/5 chain):

 W   LADDER + WARDS (kill -> PIPELINE-BROKEN / WARD-BROKEN): W1
     faithful ladder >= MIN_RUNGS = 40 (kz 2..KZMAX, H_MIN <= h <=
     HCAP, X <= ATOM_MAX); W2 WARD m_h > 0 everywhere; W3 WARD
     exact bookkeeping |(lift - demand) - m_h| <= ID_WARD; W4 WARD
     race atom identity (atoms + PNT grid) rel <= ID_WARD; W5 WARD
     SPLIT-EXACT at the three frozen reference cuts (50, 100,
     200); W6 WARD scan-vs-split consistency: the cumsum scan
     reproduces the reference-cut split at the largest atom <=
     NCUT (rel <= SCAN_WARD) AND the increment identity G(c_i) =
     cumsum(inc) - demand (rel <= SCAN_WARD); W7 REPRODUCTION of
     the round-59 fixed-cut census: G > 0 counts at (50, 100, 200)
     == (52, 26, 25).

 H   THE SCHEDULE (typed as frozen above): (a) coverage ledger +
     FULL-COVERAGE / PARTIAL-COVERAGE; (b) structure + greedy
     schedule; (c) overshoot anatomy; (d) screens.

 C   CONTROLS (kill -> WARD-BROKEN if silent): scramble (seed 1)
     and Epstein x^2+5y^2 comb at kz 9 on this surface: m < 0 AND
     cert coverage count == 0 at EVERY cut (the schedule cannot
     manufacture coverage without the wall); smooth comb (lattice
     masses 2 e^{u/2} du): m < 0, coverage 0, and the DIFFERENT
     failure recorded (lift collapses: |lift| ~ discretization,
     printed vs the truth O(1) lift).

KILLS: K1 ladder (W1) -> PIPELINE-BROKEN; K2 wards (W2-W7, C) ->
WARD-BROKEN.  All H-typed outcomes are measurements, never kills.

VERDICT (frozen enum): CUTSCHED-MEASURED with typed sublabels
FULL-COVERAGE(n/N, max n_min)/PARTIAL-COVERAGE(n/N),
SCHEDULE-STRUCTURED(R2)/SCHEDULE-UNSTRUCTURED(R2),
SCHED-GREEDY(k), OVERSHOOT-NEG(med)/OVERSHOOT-MIXED,
SCREEN-.../RESTRICTED-...; else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: KZMAX = 150; MIN_RUNGS = 40; REF_CUTS = (50, 100,
200); REF_COUNTS = (52, 26, 25); ID_WARD = 1e-10; SCAN_WARD =
1e-9; NG_SMOOTH = 6000; CAPS = (50, 100, 200, 1000, 10000);
NCAP_SCREEN = 200; N_ANAT = 200; N_TOP = 8; STRUCT_R2 = 0.60;
SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; NODE_C = 0.3727, NODE_S =
-0.0116 (declared input); CTRL_KZ = 9; scramble seed 1; jackknife
= full leave-one-out, CI = +- 2SE.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): TWO smoke
runs.  Smoke 1 (13 pass / 1 fail) exposed a SPEC DEFECT in W6,
not a pipeline fact: the scan cuts sit at ATOM positions (there
is no atom at n = 50), so comparing the atom-position scan
against the u = log 50 reference split mixes two smooth-slice
conventions (measured mismatch 4.1e-01 = the (log 49, log 50]
smooth slice, not an error).  AMENDMENT 1 (disclosed): W6 was
re-specified as the honest two-route check -- cumsum scan vs
direct masked sum AT THE SAME atom cut -- plus the increment
identity; no bar, band, count, enum or typed rule was moved.
AMENDMENT 2 (disclosed): the cert_best == m equality DIAGNOSTIC
(print only) got a cancellation-scaled tolerance (cert = m -
tail - |tail| loses ~|tail|/m digits when |tail| >> m).
Fail-first preserved.  Smoke 2 (14/14, 14.5 s) MEASURED, recorded
as the honest context the frozen run must confirm: (a) FULL
COVERAGE EXISTS AND IS SHALLOW: 67/67 rungs have CERT-covering
atom cuts (median count 1381 per rung), and the minimal covering
cut is TINY -- n_min ladder 3..9 (med 5): the explicit head n <=
9 (atoms 2, 3, 4, 5, 7, 8, 9) plus the null-tail estimate covers
EVERY rung, because at these small cuts the head OVERSHOOTS the
full lift (tail <= 0 at the first covering cut on 67/67, so cert
= m exactly there); round 59 saw no covering single cut because
it only probed n = 50/100/200 -- INSIDE the mid-band where the
deeper atoms are net-negative; (b) STRUCTURED: log n_min vs alpha
slope +0.335 +- 2SE 0.036 (R^2 0.849; vs log h R^2 0.611),
concordant pair fraction 0.851, and the node tie is the sharpest
structure: corr(u_min, u*(alpha)) = +0.918 -- the minimal
covering cut tracks the prime-free classical-node drift law;
GREEDY GLOBAL SCHEDULE: ONE shared cut n = 9 covers 67/67
(greedy upper bound, said plainly); (c) THE OVERSHOOT MECHANISM:
Delta G(50 -> 100) med -2.30e-01, negative on 42/67; the atom
ledger localizes the net-negative q_v-read carriers as 16 = 2^4
(med -0.68), 37 (-0.30), 23 (-0.27), 27 = 3^3 (-0.22), 59
(-0.20), 64 = 2^6 (-0.18) vs positive carriers 2 (+0.77), 17
(+0.52), 29 (+0.29), 31 (+0.27), 19 (+0.24): an interference
geometry of the deployed window read, not an arithmetic accident
(the scramble kills all coverage); (d) SCREENS: unrestricted best
margin slope +1.000 (R^2 1.000) -- STRUCTURAL (cert <= m exact);
restricted n <= 200 screen covers 67/67 with slope +1.000 =
RESTRICTED-RELOC: the covered margin IS the wall margin, never a
new floor; (e) controls all fire with DIFFERENT anatomies:
Epstein m = -10.1 (lift -11.1), scramble m = -7.86 (lift -8.89),
smooth m = -1.64 (lift -3.47), coverage 0 at every cut on all
three; truth |lift| med 1.21.  Fail-first preserved: nothing was
weakened; all typed outcomes are measurements over exact-warded
decompositions.

SPEC v2 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v2: (i)
machinery verbatim from wall_head_tail_bound_probe (q_read,
smooth_comb, jackknife, OLS); (ii) cuts INCLUSIVE at atom
positions (atoms u_n <= u_c, smooth grid ug <= u_c -- same
functional, same convention as round 59); (iii) coverage at a
shared cut value n reads the rung's largest atom position <=
log n; (iv) the smooth slice allocation assigns (u_{i-1}, u_i] to
atom i (the increment identity is warded); (v) prime-power labels
by integer-root factorization of the deployed atom values only.

NO-GO COMPLIANCE (frozen): no certified-bound retry, no rank-1
approximation, no Herglotz; no fit where an identity is claimed
(split/bookkeeping/increment identities are exact wards; the
schedule laws are typed trends with jackknife error bars).

NO RH claim: a covering cut schedule is a finite measured surface
-- for every deployed rung there exists an explicit head whose
null-tail residual keeps the margin positive; turning that into a
certificate family requires a PROVED tail bound at every cut,
which this probe does not provide and does not claim.  No marker
moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime; the heads read the DEPLOYED window atoms); v563
READ-ONLY; RNG only inside the declared scramble control; stdout
only.

Sources (read-only): v563_paper2_readouts; lift-race machinery
verbatim from wall_head_tail_bound_probe.py (round 59) via
wall_matched_asymptotics_probe.py; round-59 head/tail census
(declared reproduction targets); node drift law from
node_origin_arch_probe.py (declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wall_cut_schedule_probe.py
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

KZMAX = 150
MIN_RUNGS = 40
REF_CUTS = (50, 100, 200)
REF_COUNTS = (52, 26, 25)
ID_WARD = 1e-10
SCAN_WARD = 1e-9
NG_SMOOTH = 6000
CAPS = (50, 100, 200, 1000, 10000)
NCAP_SCREEN = 200
N_ANAT = 200
N_TOP = 8
STRUCT_R2 = 0.60
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
NODE_C = 0.3727
NODE_S = -0.0116
CTRL_KZ = 9
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


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        bb.append(ols_line(x[m], y[m])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                              ** 2)))
    return b, se, r2


def corr(x, y):
    return float(np.corrcoef(np.asarray(x, float),
                             np.asarray(y, float))[0, 1])


def q_read(W, u, D, M):
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
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


def pp_label(n):
    """Prime-power structure of a deployed atom value by integer
    roots (no primality oracle; the table IS the comb)."""
    for k in range(int(math.log2(max(n, 2))), 1, -1):
        b = int(round(n ** (1.0 / k)))
        for bb in (b - 1, b, b + 1):
            if bb >= 2 and bb ** k == n:
                return "%d^%d" % (bb, k)
    return "%d" % n


def race_rung(kz, comb=None, scramble_seed=None, smooth_world=False):
    """One rung of the lift-race surface (head_tail verbatim) with
    the full atom-cut scan."""
    try:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
    except Exception:
        return None
    if not (core.H_MIN <= rr["h"] <= core.HCAP):
        return None
    if rr["X"] > core.ATOM_MAX:
        return None
    alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
    uu = np.asarray(rr["uu"], float)
    mu = 2.0 * np.asarray(rr["lam"], float)
    if smooth_world:
        du = np.zeros(len(uu))
        du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
        du[0] = uu[1] - uu[0]
        du[-1] = uu[-1] - uu[-2]
        mu = 2.0 * np.exp(uu / 2.0) * du
    if comb is not None:
        uu, mu = comb
    c_at = core.atom_lags_at(alpha, M, uu, mu)[0]
    c_ar = np.asarray(core.arch_lags(M, D), float)
    w, V = np.linalg.eigh(core.odd_toeplitz(c_ar + c_at, M))
    v = V[:, 0]
    ug, mg = smooth_comb(alpha)
    c_sm = core.atom_lags_at(alpha, M, ug, mg)[0]
    Wv = core.lag_weights_from_v(v, h)
    e_ar = float(np.asarray(c_ar) @ Wv)
    e_t = float(np.asarray(c_at) @ Wv)
    e_s = float(np.asarray(c_sm) @ Wv)
    qa = mu * q_read(Wv, uu, D, M)
    qg = mg * q_read(Wv, ug, D, M)
    dev_at = max(abs(float(qa.sum()) - e_t) / max(abs(e_t), 1e-30),
                 abs(float(qg.sum()) - e_s) / max(abs(e_s), 1e-30))
    lift = e_t - e_s
    demand = -(e_ar + e_s)
    row = dict(kz=kz, alpha=float(alpha), h=h, m=float(w[0]),
               lift=lift, demand=demand, dev_at=dev_at, uu=uu,
               split={})
    row["he_dir"] = {}
    for nc in REF_CUTS:
        ucut = math.log(nc)
        he = (float(qa[uu <= ucut].sum())
              - float(qg[ug <= ucut].sum()))
        te = (float(qa[uu > ucut].sum())
              - float(qg[ug > ucut].sum()))
        row["split"][nc] = (he, te)
        i = int(np.searchsorted(uu, ucut, side="right")) - 1
        if i >= 0:
            ua = float(uu[i])
            row["he_dir"][nc] = (float(qa[uu <= ua].sum())
                                 - float(qg[ug <= ua].sum()))
    # ---- the atom-cut scan (cumsum route)
    cq = np.cumsum(qa)
    idxg = np.searchsorted(ug, uu, side="right")
    cg_all = np.concatenate([[0.0], np.cumsum(qg)])
    head = cq - cg_all[idxg]
    G = head - demand
    tail = lift - head
    cert = G - np.abs(tail)
    # increment identity: smooth slice (u_{i-1}, u_i] -> atom i
    inc = qa.copy()
    inc[0] -= cg_all[idxg[0]]
    inc[1:] -= (cg_all[idxg[1:]] - cg_all[idxg[:-1]])
    dev_inc = float(np.max(np.abs((np.cumsum(inc) - demand) - G))
                    ) / max(float(np.max(np.abs(G))), 1e-30)
    row.update(G=G, tail=tail, cert=cert, inc=inc,
               dev_inc=dev_inc)
    return row


def main():
    section("PRIME.PORT.CUT.SCHEDULE.01 -- the per-rung cut "
            "schedule of the explicit head (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder + wards")
    rungs = []
    for kz in range(2, KZMAX + 1):
        row = race_rung(kz)
        if row is not None:
            rungs.append(row)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    N = len(rungs)
    check("W2 WARD truth margin m_h > 0 on every rung (min %.3e)"
          % min(r["m"] for r in rungs),
          all(r["m"] > 0 for r in rungs), kill="K2")
    dev_bk = max(abs((r["lift"] - r["demand"]) - r["m"])
                 / max(1.0, abs(r["m"])) for r in rungs)
    check("W3 WARD exact bookkeeping lift - demand = m_h: max dev "
          "%.2e <= %.0e" % (dev_bk, ID_WARD), dev_bk <= ID_WARD,
          kill="K2")
    dev_at = max(r["dev_at"] for r in rungs)
    check("W4 WARD race atom identity: max rel dev %.2e <= %.0e"
          % (dev_at, ID_WARD), dev_at <= ID_WARD, kill="K2")
    dev_sp = max(abs((he + te) - r["lift"])
                 / max(abs(r["lift"]), 1e-30)
                 for r in rungs for he, te in r["split"].values())
    check("W5 WARD SPLIT-EXACT at reference cuts %s: max rel dev "
          "%.2e <= %.0e" % (REF_CUTS, dev_sp, ID_WARD),
          dev_sp <= ID_WARD, kill="K2")
    dev_scan = max(r["dev_inc"] for r in rungs)
    for r in rungs:
        for nc in REF_CUTS:
            i = int(np.searchsorted(r["uu"], math.log(nc),
                                    side="right")) - 1
            if i < 0:
                continue
            heS = r["G"][i] + r["demand"]
            he_dir = r["he_dir"][nc]
            dev_scan = max(dev_scan, abs(heS - he_dir)
                           / max(abs(he_dir), 1e-30))
    check("W6 WARD scan two-route (cumsum vs direct masked sum "
          "at the same atom cut) + increment identity: max rel "
          "dev %.2e <= %.0e" % (dev_scan, SCAN_WARD),
          dev_scan <= SCAN_WARD, kill="K2")
    cnts = tuple(int(np.sum(np.array(
        [r["split"][nc][0] - r["demand"] for r in rungs]) > 0))
        for nc in REF_CUTS)
    check("W7 REPRODUCTION round-59 fixed-cut census: G > 0 "
          "counts at %s = %s == %s"
          % (REF_CUTS, cnts, REF_COUNTS), cnts == REF_COUNTS,
          kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ Ha
    section("Ha -- THE COVERAGE MATRIX (all atom cuts, both "
            "senses)")
    print("    kz   h    m_h        #G>0  #cert  n_minG  n_min   "
          "n_best   cert_best   tail@n_min")
    n_min_all, u_min_all, ok_cov = [], [], []
    for r in rungs:
        nn = np.round(np.exp(r["uu"])).astype(int)
        covG = r["G"] > 0.0
        covC = r["cert"] > 0.0
        ok = bool(np.any(covC))
        ok_cov.append(ok)
        ib = int(np.argmax(r["cert"]))
        if ok:
            i0 = int(np.argmax(covC))
            n_min_all.append(int(nn[i0]))
            u_min_all.append(float(r["uu"][i0]))
            print("    %-4d %-4d %.3e  %-5d %-6d %-7s %-7d %-8d "
                  "%.3e  %+.3e"
                  % (r["kz"], r["h"], r["m"], int(np.sum(covG)),
                     int(np.sum(covC)),
                     str(nn[int(np.argmax(covG))])
                     if np.any(covG) else "-", nn[i0], nn[ib],
                     r["cert"][ib], r["tail"][i0]), flush=True)
        else:
            n_min_all.append(-1)
            u_min_all.append(float("nan"))
            print("    %-4d %-4d %.3e  %-5d NO COVERING CUT "
                  "(best cert %+.3e at n = %d)"
                  % (r["kz"], r["h"], r["m"], int(np.sum(covG)),
                     r["cert"][ib], nn[ib]), flush=True)
    n_cov = int(np.sum(ok_cov))
    if n_cov == N:
        ha = ("FULL-COVERAGE(%d/%d, med n_min=%d, max n_min=%d)"
              % (n_cov, N, int(np.median(n_min_all)),
                 int(np.max(n_min_all))))
    else:
        ha = "PARTIAL-COVERAGE(%d/%d)" % (n_cov, N)
    med_cnt = float(np.median([int(np.sum(r["cert"] > 0))
                               for r in rungs]))
    print("\n    covering-cut count med %.0f; cap table (rungs "
          "with some covering cut <= NCAP):" % med_cnt)
    for cap in CAPS:
        nc_ = sum(1 for r, nm in zip(rungs, n_min_all)
                  if nm > 0 and nm <= cap)
        print("      NCAP %-6d: %d/%d" % (cap, nc_, N))
    check("Ha.1 typed (a): %s (a covering cut is a measured "
          "surface statement -- the null tail beyond it is NOT a "
          "theorem)" % ha, True)

    # ------------------------------------------------------------ Hb
    section("Hb -- STRUCTURE of the minimal schedule n_min(h)")
    hh = np.array([float(r["h"]) for r in rungs])
    aa = np.array([r["alpha"] for r in rungs])
    nm = np.array(n_min_all, float)
    msk = nm > 0
    sl_h, se_h, r2_h = jack_slope(np.log(hh[msk]),
                                  np.log(nm[msk]))
    sl_a, se_a, r2_a = jack_slope(aa[msk], np.log(nm[msk]))
    x = np.log(hh[msk])
    y = np.log(nm[msk])
    conc, tot = 0, 0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            tot += 1
            if (x[i] - x[j]) * (y[i] - y[j]) > 0:
                conc += 1
    ustar = (NODE_C + NODE_S * aa[msk]) * aa[msk]
    co_node = corr(np.array(u_min_all)[msk], ustar)
    print("    log n_min vs log h: slope %+.3f +- 2SE %.3f (R^2 "
          "%.3f); vs alpha: %+.3f +- %.3f (R^2 %.3f); concordant "
          "pair fraction %.3f; node tie corr(u_min, u*) = %+.3f"
          % (sl_h, 2 * se_h, r2_h, sl_a, 2 * se_a, r2_a,
             conc / max(tot, 1), co_node))
    best_r2 = max(r2_h, r2_a)
    if best_r2 >= STRUCT_R2:
        hb = "SCHEDULE-STRUCTURED(R2=%.2f)" % best_r2
    else:
        hb = "SCHEDULE-UNSTRUCTURED(R2=%.2f)" % best_r2
    check("Hb.1 typed (b): %s (bar %.2f)" % (hb, STRUCT_R2), True)
    # greedy global set cover over shared cut values
    grid_n = np.unique(np.concatenate(
        [np.round(np.exp(r["uu"])).astype(int) for r in rungs]))
    covmat = np.zeros((N, len(grid_n)), bool)
    for i, r in enumerate(rungs):
        pos = np.searchsorted(r["uu"],
                              np.log(grid_n.astype(float))
                              + 1e-12, side="right") - 1
        val = np.zeros(len(grid_n), bool)
        okp = pos >= 0
        val[okp] = r["cert"][pos[okp]] > 0.0
        covmat[i] = val
    unc = np.ones(N, bool)
    sched = []
    while np.any(unc) and len(sched) < 20:
        gains = covmat[unc].sum(axis=0)
        jbest = int(np.argmax(gains))
        if gains[jbest] == 0:
            break
        sched.append((int(grid_n[jbest]), int(gains[jbest])))
        unc &= ~covmat[:, jbest]
    print("    greedy global schedule (upper bound): %d cuts -> %s"
          "; uncovered left %d"
          % (len(sched), ", ".join("n=%d (+%d)" % s
                                   for s in sched),
             int(np.sum(unc))))
    check("Hb.2 typed: SCHED-GREEDY(%d)" % len(sched), True)

    # ------------------------------------------------------------ Hc
    section("Hc -- THE OVERSHOOT MECHANISM (per-atom increments)")
    dg = np.array([r["split"][100][0] - r["split"][50][0]
                   for r in rungs])
    n_neg = int(np.sum(dg < 0))
    print("    Delta G(50 -> 100) = G(100) - G(50): med %+.3e, "
          "negative on %d/%d rungs"
          % (float(np.median(dg)), n_neg, N))
    # atom ledger: med increment per atom value n <= N_ANAT
    led = {}
    for r in rungs:
        nn = np.round(np.exp(r["uu"])).astype(int)
        for i in np.nonzero(nn <= N_ANAT)[0]:
            led.setdefault(int(nn[i]), []).append(
                float(r["inc"][i]))
    med_led = sorted(((float(np.median(v)), n)
                      for n, v in led.items()))
    print("    top %d NEGATIVE median increments:" % N_TOP)
    for v, n in med_led[:N_TOP]:
        print("      n = %-6d (%s%-6s): inc med %+.3e"
              % (n, "", pp_label(n), v))
    print("    top %d POSITIVE median increments:" % N_TOP)
    for v, n in med_led[-N_TOP:][::-1]:
        print("      n = %-6d (%s%-6s): inc med %+.3e"
              % (n, "", pp_label(n), v))
    hc = ("OVERSHOOT-NEG(medDG=%.1e, %d/%d)" % (
        float(np.median(dg)), n_neg, N)
        if float(np.median(dg)) < 0 else
        "OVERSHOOT-MIXED(medDG=%+.1e, %d/%d)" % (
            float(np.median(dg)), n_neg, N))
    n_tneg = sum(1 for r, nm_ in zip(rungs, n_min_all) if nm_ > 0
                 and r["tail"][int(np.argmax(r["cert"] > 0))]
                 <= 0.0)
    print("    tail sign at the first covering cut: tail <= 0 on "
          "%d/%d covered rungs (there cert = m exactly)"
          % (n_tneg, n_cov))
    check("Hc.1 typed (c): %s (why LESS head helps: the (50,100] "
          "atoms are a net-negative q_v-read correction)" % hc,
          True)

    # ------------------------------------------------------------ Hd
    section("Hd -- TAU-SCREENS (margin vs m_h; the wall margin IS "
            "m on this surface)")
    mm_ = np.array([r["m"] for r in rungs])
    cb = np.array([float(np.max(r["cert"])) for r in rungs])
    _a, sl_u, r2_u = ols_line(np.log(mm_), np.log(np.maximum(
        cb, 1e-300)))
    lif = np.array([abs(r["lift"]) for r in rungs])
    n_eq = int(np.sum(np.abs(cb - mm_) <= 1e-12 * (1.0 + lif)))
    scr = np.full(N, np.nan)
    for i, r in enumerate(rungs):
        nn = np.round(np.exp(r["uu"])).astype(int)
        sel = nn <= NCAP_SCREEN
        if np.any(sel) and float(np.max(r["cert"][sel])) > 0:
            scr[i] = float(np.max(r["cert"][sel]))
    oks = np.isfinite(scr)
    _a, sl_r, r2_r = ols_line(np.log(mm_[oks]), np.log(scr[oks]))
    print("    unrestricted best margin: slope %+.3f (R^2 %.3f); "
          "cert_best == m (cancellation-scaled tol) on %d/%d "
          "(STRUCTURAL: cert <= m by the exact algebra)"
          % (sl_u, r2_u, n_eq, N))
    print("    restricted (n <= %d) best margin: covers %d/%d; "
          "slope %+.3f (R^2 %.3f)"
          % (NCAP_SCREEN, int(np.sum(oks)), N, sl_r, r2_r))
    if abs(sl_r) <= SLOPE_PASS:
        hd = "RESTRICTED-PASS(slope=%+.3f)" % sl_r
    elif sl_r >= SLOPE_RELOC:
        hd = "RESTRICTED-RELOC(slope=%+.3f)" % sl_r
    else:
        hd = "RESTRICTED-AMBIG(slope=%+.3f)" % sl_r
    check("Hd.1 typed (d): SCREEN-STRUCTURAL(+%.2f) / %s (bands "
          "PASS |s| <= %.2f, RELOC s >= %.2f)"
          % (sl_u, hd, SLOPE_PASS, SLOPE_RELOC), True)

    # ------------------------------------------------------------ C
    section("C -- controls on this surface at kz %d" % CTRL_KZ)
    rr9 = core.build_window(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nnE = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {}
    ctl["Epstein"] = race_rung(CTRL_KZ, comb=(
        np.log(nnE.astype(float)),
        2.0 * lamE_[nnE] / np.sqrt(nnE.astype(float))))
    ctl["scramble"] = race_rung(CTRL_KZ, scramble_seed=1)
    ctl["smooth"] = race_rung(CTRL_KZ, smooth_world=True)
    fired = True
    for name, r in ctl.items():
        if r is None:
            print("    %-9s: rung dies -> fires" % name)
            continue
        ncov = int(np.sum(r["cert"] > 0))
        f = (r["m"] < 0) and ncov == 0
        fired &= f
        print("    %-9s: m %+.3e  lift %+.3e  covering cuts %d "
              "-> %s" % (name, r["m"], r["lift"], ncov,
                         "FIRES" if f else "SILENT"), flush=True)
    print("    truth |lift| med %.3f (the smooth comb has no race "
          "to win; the scramble loses it at scale)"
          % float(np.median([abs(r["lift"]) for r in rungs])))
    check("C1 WARD all three controls fire (m < 0 and coverage "
          "0)", fired, kill="K2")

    return finish(dict(ha=ha, hb=hb, k=len(sched), hc=hc, hd=hd,
                       sl_u=sl_u))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("CUTSCHED-MEASURED / %(ha)s / %(hb)s / "
                   "SCHED-GREEDY(%(k)d) / %(hc)s / "
                   "SCREEN-STRUCTURAL(%(sl_u)+.2f) / %(hd)s"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): a covering cut schedule is a finite
  MEASURED SURFACE -- for every deployed rung there exists an
  explicit atom head whose null-tail residual keeps the margin
  positive.  It is NOT a certificate family: the tail beyond every
  cut still needs its bound, and cert(c) <= m_h always (the
  schedule cannot beat the wall margin, only reach it).  A RELOC
  restricted screen means the covered margin is the wall margin
  relocated, not a new floor.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
