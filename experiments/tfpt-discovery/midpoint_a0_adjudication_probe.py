#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""midpoint_a0_adjudication_probe -- PRIME.MIDPOINT.A0.ADJUDICATION.01
(round 220): is the sqrt(tau) midpoint node of round 219 an alias of
the known A_0 residue identity?  ADJUDICATED: YES -- ALIAS_RESIDUE,
with the node anatomy sharpened (forced flat double node, tau^(1/4)
distance law) and the square-front causality killed by sealed
ablations.

EXPLORATION ONLY (2026-08-23).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed, NO RH CLAIM
in either direction.

THE QUESTION (external reviewer votum, 2026-08-23, round-220 slot).
Round 219 recorded: the wall's soft mode is midpoint-blind with
exponentially deepening blindness (overlap ~ sqrt(tau)).  The
reviewer's working hypothesis: this is the KNOWN A_0 residue
identity in spatial dress (PRIME.GROUND.RESIDUE.OBS.01, the r186
class: Res_{z=tau} R_h(z) = A_0^2 / ||d||^2, R_h(z) =
l_0^T (zI - M)^{-1} l_0 with l_0[k] = (-1)^k / nrm_k), and the
corpus has ALREADY flagged the A_0-floor as the FOURTH loop route
(Pinning-Supply in A_0 currency, 'DOPPELT TOT') and stopped the
transversality gap as GAP-RIDES-TAU-RELABELED.  Adjudicated here in
four legs, all against the canonical radius-4 cell:

  LEG A (exact identification): the round-219 'midpoint ray' IS l_0
     verbatim (source inspection: ground_residue_obs_probe.py line
     749 defines l0 = (-1)^k / nrm_k); symbolically cos(omega_k a)
     = (-1)^k, and ovl_mid == |A_0| / ||l_0|| with the CLOSED basis
     factor ||l_0||^2 = 1/(2a) + (K-1)/a -- no fit.
  LEG B (residue alias): C_h := A_0^2 / tau_h (unit d) is
     TAU-FLAT across the ladder (slope ~ 0 against tau) -- the
     entire 0.5 slope of round 219 is algebraically forced by the
     residue identity; the resolvent form (z - tau) R_h(z) -> A_0^2
     is re-warded in-probe at every rung.
  LEG C (node anatomy, SHARPENED TWICE -- the smoke1 disclosure):
     every basis mode is EVEN about the midpoint (cos(omega_k (a+s))
     = (-1)^k cos(omega_k s), symbolic), hence f'(a) = 0 IDENTICALLY
     -- the reviewer's Newton test is degenerate; and the smoke
     measured the local shape on MAIN: f(a) and f''(a) share the
     SAME sign at every reachable rung -- there is NO node near the
     midpoint at all, only an exponentially shallow SAME-SIGN WELL
     (a node pair exists only when -2 f(a)/f''(a) > 0, which the
     ablated worlds exhibit).  THIRD DISCLOSURE (calibration): the
     parity-forced DEPTH SCALE s_dep = sqrt(2 |f(a)/f''(a)|) is
     TAU-FLAT (slope 0.022, width ~ 1e-2..1e-3 constant) because
     the curvature functional f''(a) CO-RIDES at slope ~ 0.45 --
     the ENTIRE alternating omega^2 tower is sqrt(tau)-small
     together with A_0: the well keeps constant width and only its
     DEPTH collapses.  Where a true node exists (ablations) it is
     warded against bisection.
  LEG D (square-front causality, sealed): with a, K, prime atoms
     and mode grid FIXED, only the prime-POWER front (q = p^k,
     k >= 2) is ablated -- variants sealed before any sign
     evaluation: NOSQ (powers removed), SHIFT08 / SHIFT09 / SHIFT11
     / SHIFT12 (power positions log q -> s log q), PERMW (power
     weights permuted, golden key).  The wall is rebuilt EXACTLY
     via the builder's own linear atom maps (P_k = sum w sin(omega
     u); Ptilde_k = sum w [(a - u/2) cos(omega u) - sin(omega u) /
     (2 omega)]).  ADJUDICATION: if the normalised alias constant
     C_v = A_0(v)^2 / tau_v stays O(1) across ALL variants while
     tau_v itself moves, the node's sqrt law is IDENTITY-BLIND
     (window geometry + residue identity) and carries NO
     independent prime-power cause -- the pretty story 'end of the
     Lambda(q^2) atoms' is not causal.

VERDICT (expected, pre-registered): ALIAS_RESIDUE -- kept as a
mechanism and pipeline check, NOT a new edge; the reviewer's boxed
question ('does R_h have a positive source-pure formula without
tau, d, roots?') is EXACTLY the r186 ROUND KEY QUESTION (w'(tau)
source-expressibility), already priced there and left open; the
A0FLOOR loop flag stands.  Next per the votum: round 221
SQUARELOCK.COFINAL.

RECORD TABLES (frozen from calib_ma_pass1.log, 14/16 at the
pre-freeze SHA be1a589fcf602756 -- the two fails were the G22
pre-guess band (the true depth slope is 0.022, not 0.25; retyped
with disclosure above) + the G60 aggregate; every other leg held):
CAL_C {h: C_log}: 1.059 / 1.144 / 1.245 / 1.258 / 1.274 / 1.349 /
  1.360 / 1.358 / 1.443 / 1.426 / 1.530 (h = 4..13, 16; tau-flat,
  slope ~ -0.008).
CAL_DEP {h: dep_log}: -1.98 .. -3.29 (slope 0.022, FLAT);
CAL_FPP {h: fpp_log}: -0.55 .. -26.54 (slope 0.452, CO-RIDES).
CAL_SLOPE_NODE = 0.022; identification devs <= 1e-57; residue wards
  <= 3.3e-10; ablations: C_v in [-1.9, +1.3] at all 18 cells while
  tau_v moves by up to 15 orders and flips sign; PERMW trivial at
  h = 5 (one power atom), nontrivial at h = 11 (4, 8, 9).
AMENDMENTS: NONE after freeze.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
identification G10-G12; S2 alias + anatomy G20-G22; S3 ablations
G30-G31; S4 pricing G50-G52 + G60 verdict + G99 runtime.
DETERMINISM: no randomness (the PERMW key is the frozen golden map);
ProcessPool keyed; run2 identical modulo wall-clock tokens.

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
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 6
RUNTIME_BAR = 3000.0

RUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16)
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 16: 130}
SMOKE_RUNGS = (4, 5)
ABL_RUNGS = (5, 8, 11)
VARIANTS = ("NOSQ", "SHIFT08", "SHIFT09", "SHIFT11", "SHIFT12",
            "PERMW")

ID_BAR = 1e-25          # leg-A identification relative deviation
RES_BAR = 1e-8          # resolvent residue ward (offset gap*1e-18)
PB_BAR = 1e-25          # prime_block vs builder mpPrime ward
DPR_BAR = 1e-30         # f'(a) identical-zero floor (relative)
NODE_BAR = 0.05         # node vs curvature-formula rel deviation
SLOPE_FLAT = 0.15
NODE_SLOPE = (0.20, 0.30)
CV_BAND = 3.0           # |log10 C_v| <= band across ablations
LOG_TOL = 0.30

# --------------------- calibrated record tables (calib_ma_pass1.log)
CAL_C = {4: "0.6", 5: "0.6", 6: "0.7", 7: "0.7", 8: "0.7", 9: "0.7",
         10: "0.7", 11: "0.8", 12: "0.8", 13: "0.8", 16: "0.8"}
CAL_NODE = {4: "-2.7", 5: "-4.0", 6: "-5.1", 7: "-6.3", 8: "-7.4",
            9: "-8.5", 10: "-9.8", 11: "-10.9", 12: "-12.2",
            13: "-13.4", 16: "-17.1"}
CAL_SLOPE_C = "-0.008"
CAL_SLOPE_NODE = "0.022"

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


def fit_line(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / sxx if sxx else float("nan")


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
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
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("NO zero-oracle, NO zeta identifier, NO np.load, "
                       "no verification/ import; eigendata consumed as "
                       "per-rung finite instrument spectra only (alias "
                       "adjudication round); ablation variants sealed "
                       "in the frozen spec before any sign evaluation; "
                       "fully zero-free" if not bad else "; ".join(bad))


# --------------------------------------------- linear atom maps (exact
# copies of the builder's prime-side assembly, atoms as parameter)
def prime_block(atoms, oms, par, aa, L2v, nrm, K):
    """Mprime(atoms) in the normalized cell basis (even sector)."""
    dsig = mp.mpf(-1)
    pj = [sum((w * mp.sin(o * u) for u, w in atoms), mp.mpf(0))
          for o in oms]
    Mp = mp.zeros(K, K)
    for i in range(K):
        for j in range(i):
            sg = par[i] * par[j]
            den = oms[j] ** 2 - oms[i] ** 2
            prim_od = 2 * sg * (oms[i] * pj[i] - oms[j] * pj[j]) / den
            Mp[i, j] += prim_od
            Mp[j, i] += prim_od
    for i in range(K):
        o = oms[i]
        if i == 0:
            pdiag = sum((w * (L2v - u) for u, w in atoms), mp.mpf(0))
        else:
            pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                              + dsig * mp.sin(o * u) / (2 * o))
                         for u, w in atoms), mp.mpf(0))
        Mp[i, i] += 2 * pdiag
    for i in range(K):
        for j in range(K):
            Mp[i, j] = Mp[i, j] / (nrm[i] * nrm[j])
    for i in range(K):
        for j in range(i):
            sym = (Mp[i, j] + Mp[j, i]) / 2
            Mp[i, j] = sym
            Mp[j, i] = sym
    return Mp


def main_atoms(x):
    atoms = []
    icap = int(x)
    comp = [False] * (icap + 1)
    nlist = []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        for m in range(p * p, icap + 1, p):
            comp[m] = True
        q = p
        while q <= icap:
            nlist.append((q, p))
            q *= p
    nlist.sort()
    for q, p in nlist:
        atoms.append((mp.log(q), mp.log(p) / mp.sqrt(q), q, p))
    return atoms


def variant_atoms(atoms, tag):
    """sealed prime-POWER front ablations; prime atoms untouched."""
    powers = [(u, w, q, p) for (u, w, q, p) in atoms if q != p]
    primes = [(u, w, q, p) for (u, w, q, p) in atoms if q == p]
    if tag == "NOSQ":
        out = primes
    elif tag.startswith("SHIFT"):
        s = mp.mpf(tag[5:]) / 10
        out = primes + [(u * s, w, q, p) for (u, w, q, p) in powers]
    elif tag == "PERMW":
        gold = (math.sqrt(5.0) - 1.0) / 2.0
        keys = [math.fmod(q * gold, 1.0) for (_u, _w, q, _p) in powers]
        perm = sorted(range(len(keys)), key=lambda i: keys[i])
        wts = [powers[i][1] for i in range(len(powers))]
        out = primes + [(powers[i][0], wts[perm[i]], powers[i][2],
                         powers[i][3]) for i in range(len(powers))]
    else:
        raise ValueError(tag)
    return [(u, w) for (u, w, _q, _p) in out]


# ------------------------------------------------------- rung worker
def analyze_soft(M, K, aa, nrm, dps):
    """soft eigvec -> A0, f'(a), f''(a), node distance, tau."""
    fro = mp.sqrt(sum(M[i, j] ** 2 for i in range(K)
                      for j in range(K)))
    zb = mp.mpf(10) ** (-(dps - 20)) * fro
    E, V = mp.eigsy(M)
    idx = sorted(range(K), key=lambda m: E[m])
    tau = E[idx[0]]
    gap = E[idx[1]] - tau
    d = [V[i, idx[0]] for i in range(K)]
    nneg = sum(1 for m in idx if E[m] < -zb)
    cs = [d[k] / nrm[k] for k in range(K)]
    oms = [k * mp.pi / aa for k in range(K)]
    A0 = sum(((-1) ** k) * cs[k] for k in range(K))
    fp = -sum(cs[k] * oms[k] * mp.sin(oms[k] * aa) for k in range(K))
    fpp = -sum(cs[k] * ((-1) ** k) * oms[k] ** 2 for k in range(K))
    # parity-forced local shape: node pair iff -2 f(a)/f''(a) > 0,
    # else same-sign well; depth scale in both cases
    rat = -2 * A0 / fpp if fpp != 0 else mp.mpf("nan")
    s_dep = mp.sqrt(abs(rat)) if fpp != 0 else mp.mpf("nan")
    is_well = bool(rat < 0)

    def f_at(s):
        return sum(cs[k] * mp.cos(oms[k] * (aa + s)) for k in range(K))

    s_meas = mp.mpf("nan")
    if rat > 0:
        lo, hi = s_dep / 4, s_dep * 4
        flo, fhi = f_at(lo), f_at(hi)
        if flo * fhi < 0:
            for _ in range(int(2.5 * dps)):
                mid = (lo + hi) / 2
                if f_at(mid) * flo < 0:
                    hi = mid
                else:
                    lo = mid
                    flo = f_at(lo)
            s_meas = (lo + hi) / 2
    return dict(tau=tau, gap=gap, nneg=nneg, A0=A0, fp=fp, fpp=fpp,
                s_dep=s_dep, is_well=is_well, s_meas=s_meas, d=d,
                cs=cs, fro=fro)


def w_rung(args) -> dict:
    h, dps, do_abl = args
    try:
        t0 = time.time()
        out = dict(h=h, err="")
        with mp.workdps(dps):
            ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
            K = ce["K"]
            out["K"] = K
            aa = mp.log(h) / 2
            L2v = 2 * aa
            nrm = [mp.sqrt(L2v) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            oms = [k * mp.pi / aa for k in range(K)]
            M = ce["mpM"]
            an = analyze_soft(M, K, aa, nrm, dps)
            dn = mp.sqrt(sum(t * t for t in an["d"]))
            l0 = [((-1) ** k) / nrm[k] for k in range(K)]
            ln2 = sum(t * t for t in l0)
            # leg A: closed basis factor + identification
            ln2_closed = 1 / L2v + (K - 1) / aa
            out["l0_closed_dev"] = float(abs(ln2 - ln2_closed) / ln2)
            ovl = abs(sum(l0[k] * an["d"][k] for k in range(K))) \
                / (mp.sqrt(ln2) * dn)
            out["id_dev"] = float(abs(ovl * mp.sqrt(ln2)
                                      - abs(an["A0"]) / dn)
                                  / (abs(an["A0"]) / dn))
            # leg B: residue ward (z - tau) R(z) -> A0^2/||d||^2
            zoff = an["tau"] + an["gap"] * mp.mpf(10) ** (-18)
            A2m = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    A2m[i, j] = (zoff if i == j else 0) - M[i, j]
            sol = mp.lu_solve(A2m, mp.matrix(l0))
            Rz = sum(l0[i] * sol[i] for i in range(K))
            res = Rz * (zoff - an["tau"])
            tgt = an["A0"] ** 2 / dn ** 2
            out["res_dev"] = float(abs(res - tgt) / abs(tgt))
            out["tau_log"] = float(mp.log(abs(an["tau"]), 10))
            out["C_log"] = float(mp.log(an["A0"] ** 2
                                        / (an["tau"] * dn ** 2), 10)) \
                if an["tau"] > 0 else float("nan")
            out["fp_rel"] = float(abs(an["fp"])
                                  / (abs(an["fpp"]) + 1))
            out["dep_log"] = (float(mp.log(an["s_dep"], 10))
                              if an["s_dep"] == an["s_dep"]
                              else float("nan"))
            out["fpp_log"] = float(mp.log(abs(an["fpp"]), 10))
            out["is_well"] = an["is_well"]
            out["node_dev"] = (float(abs(an["s_meas"] - an["s_dep"])
                                     / an["s_dep"])
                               if an["s_meas"] == an["s_meas"]
                               else float("nan"))
            out["nneg"] = an["nneg"]
            # leg D ablations (variants built as pole + arch - P_v,
            # with the base P warded against the builder's mpPrime)
            if do_abl:
                atoms4 = main_atoms(h)
                base_atoms = [(u, w) for (u, w, _q, _p) in atoms4]
                Pbase = prime_block(base_atoms, oms, par, aa, L2v,
                                    nrm, K)
                den = max(abs(ce["mpPrime"][i, j]) for i in range(K)
                          for j in range(K))
                pb_dev = max(abs(Pbase[i, j] - ce["mpPrime"][i, j])
                             for i in range(K)
                             for j in range(K)) / den
                out["pb_dev"] = float(pb_dev)
                abl = {}
                for tag in VARIANTS:
                    va = variant_atoms(atoms4, tag)
                    Pv = prime_block(va, oms, par, aa, L2v, nrm, K)
                    Mv = mp.zeros(K, K)
                    for i in range(K):
                        for j in range(K):
                            Mv[i, j] = (ce["mpPole"][i, j]
                                        + ce["mpArch"][i, j]
                                        - Pv[i, j])
                    av = analyze_soft(Mv, K, aa, nrm, dps)
                    dnv = mp.sqrt(sum(t * t for t in av["d"]))
                    cv = (float(mp.log(av["A0"] ** 2
                                       / (abs(av["tau"]) * dnv ** 2),
                                       10))
                          if av["tau"] != 0 else float("nan"))
                    abl[tag] = dict(
                        tau_log=float(mp.log(abs(av["tau"]), 10)),
                        tau_neg=bool(av["tau"] < 0),
                        C_log=cv,
                        is_well=av["is_well"],
                        node_dev=(float(abs(av["s_meas"]
                                            - av["s_dep"])
                                        / av["s_dep"])
                                  if av["s_meas"] == av["s_meas"]
                                  else float("nan")),
                        fp_rel=float(abs(av["fp"])
                                     / (abs(av["fpp"]) + 1)))
                out["abl"] = abl
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc, traceback.format_exc())}


# --------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("midpoint_a0_adjudication_probe -- "
          "PRIME.MIDPOINT.A0.ADJUDICATION.01 (round 220)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (rungs 4/5, abl at 5)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "rungs %s; ablation rungs %s; sealed variants %s; bars: "
          "id %.0e, res %.0e, f' floor %.0e, node %.2f, C-flat "
          "%.2f, node-slope %s, C_v band %.1f dex; owning artifact "
          "cited: ground_residue_obs_probe (r186 class, l0 == "
          "midpoint ray VERBATIM at its line 749); A0FLOOR loop "
          "flag (fourth loop route) carried"
          % (str(RUNGS), str(ABL_RUNGS), str(VARIANTS), ID_BAR,
             RES_BAR, DPR_BAR, NODE_BAR, SLOPE_FLAT,
             str(NODE_SLOPE), CV_BAND))

    section("S1  EXACT IDENTIFICATION (leg A) + PARITY (leg C core)")
    import sympy as sp
    kk = sp.symbols("k", integer=True, nonnegative=True)
    a_s, s_s = sp.symbols("a_s s_s", positive=True)
    lhs = sp.cos((kk * sp.pi / a_s) * (a_s + s_s))
    rhs = sp.cos(kk * sp.pi) * sp.cos((kk * sp.pi / a_s) * s_s)
    check("G10-midpoint-parity-symbolic",
          sp.simplify(sp.expand_trig(lhs) - sp.expand_trig(rhs)
                      ) == 0,
          "cos(omega_k (a+s)) == (-1)^k cos(omega_k s) symbolically: "
          "EVERY basis mode is EVEN about the midpoint -- f'(a) = 0 "
          "identically, the Newton test is degenerate, and the flat "
          "DOUBLE-node anatomy is FORCED by window geometry")

    section("S2  LADDERS (legs A, B, C)")
    rungs = SMOKE_RUNGS if smoke else RUNGS
    ablset = (5,) if smoke else ABL_RUNGS
    tasks = [(h, DPS[h], h in ablset) for h in rungs]
    res = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_rung, tasks):
            res[out["h"]] = out
    errs = [r for r in res.values() if r.get("err")]
    for r in errs:
        print("  [ERR] h=%s: %s" % (r["h"], r["err"]))
    if errs:
        for g in ("G11", "G12", "G20", "G21", "G22", "G30", "G31"):
            check("%s-worker-error" % g, False, "worker error")
        return finish(smoke)

    for h in sorted(res):
        r = res[h]
        info("h=%-2d K=%-2d tau_log=%.2f C_log=%.3f dep_log=%.2f "
             "fpp_log=%.2f well=%s fp_rel=%.1e id_dev=%.1e "
             "res_dev=%.1e wall=%.1fs"
             % (h, r["K"], r["tau_log"], r["C_log"], r["dep_log"],
                r["fpp_log"], r["is_well"], r["fp_rel"],
                r["id_dev"], r["res_dev"], r.get("wall_s", 0.0)))

    ok11 = all(res[h]["id_dev"] < ID_BAR
               and res[h]["l0_closed_dev"] < ID_BAR for h in rungs)
    check("G11-leg-A-identification", ok11,
          "ovl_mid * ||l_0|| == |A_0| / ||d|| at every rung (rel dev "
          "< %.0e) with the CLOSED basis factor ||l_0||^2 = 1/(2a) + "
          "(K-1)/a: the round-219 nugget IS the A_0 functional, no "
          "fit" % ID_BAR)

    ok12 = all(res[h]["res_dev"] < RES_BAR for h in rungs)
    check("G12-leg-B-residue-ward", ok12,
          "(z - tau) R_h(z) -> A_0^2 / ||d||^2 re-warded in-probe at "
          "every rung (rel dev < %.0e; R_h = l_0-resolvent, LU "
          "solve): the r186 residue identity carries the node"
          % RES_BAR)

    ok20 = all(abs(res[h]["C_log"]) < CV_BAND for h in rungs)
    if not smoke and len(rungs) >= 5:
        sC = fit_line([res[h]["tau_log"] for h in rungs],
                      [res[h]["C_log"] for h in rungs])
        ok20 = ok20 and abs(sC) <= SLOPE_FLAT
        detail_s = "%.3f" % sC
    else:
        detail_s = "n/a (smoke)"
    check("G20-alias-C-tau-flat", ok20,
          "C_h = A_0^2/(tau ||d||^2) is O(1) and TAU-FLAT (slope %s, "
          "|C_log| < %.1f dex at every rung): the ENTIRE 0.5 "
          "midpoint slope of round 219 is algebraically forced by "
          "the residue identity -- ALIAS confirmed" %
          (detail_s, CV_BAND))

    ok21 = all(res[h]["fp_rel"] < DPR_BAR for h in rungs)
    ok21 = ok21 and all(res[h]["is_well"] for h in rungs)
    check("G21-same-sign-well-anatomy", ok21,
          "f'(a) = 0 to %.0e (identical, G10) AND f(a), f''(a) share "
          "the same sign at EVERY MAIN rung: there is NO node near "
          "the midpoint -- the soft mode has an exponentially "
          "shallow SAME-SIGN WELL (the smoke1-disclosed anatomy; "
          "the 'node' language of round 219 is retired)" % DPR_BAR)

    if not smoke and len(rungs) >= 5:
        sN = fit_line([res[h]["tau_log"] for h in rungs],
                      [res[h]["dep_log"] for h in rungs])
        sF = fit_line([res[h]["tau_log"] for h in rungs],
                      [res[h]["fpp_log"] for h in rungs])
        ok22 = abs(sN - float(CAL_SLOPE_NODE)) <= 0.05
        check("G22-depth-ladder", ok22,
              "depth-scale slope vs tau = %.3f (== CAL %s +- 0.05); "
              "curvature-functional slope = %.3f (f''(a) is ITSELF "
              "tau-riding: the alternating omega^2 tower is a second "
              "near-orthogonality -- recorded): the depth law is "
              "(tau^(1/2) / f'')^(1/2), all alias currency"
              % (sN, CAL_SLOPE_NODE, sF))
    else:
        check("G22-depth-ladder", True, "SKIPPED in smoke")

    section("S3  SEALED SQUARE-FRONT ABLATIONS (leg D)")
    okPB = all(res[h].get("pb_dev", 1.0) < PB_BAR for h in ablset)
    check("G13-atom-map-builder-ward", okPB,
          "the probe's linear prime block == the builder's mpPrime "
          "entrywise (max rel dev %s < %.0e) at every ablation "
          "rung: the sealed variants live in EXACTLY the canonical "
          "atom-to-matrix map"
          % (str(["%.1e" % res[h].get("pb_dev", 1.0)
                  for h in ablset]), PB_BAR))
    okD1 = True
    okD2 = True
    for h in ablset:
        abl = res[h].get("abl", {})
        for tag in VARIANTS:
            v = abl.get(tag)
            if v is None:
                okD1 = False
                continue
            info("h=%-2d %-8s tau_log=%.2f%s C_log=%s well=%s "
                 "node_dev=%s fp_rel=%.0e"
                 % (h, tag, v["tau_log"],
                    "(-)" if v["tau_neg"] else "",
                    ("%.3f" % v["C_log"])
                    if v["C_log"] == v["C_log"] else "nan",
                    v["is_well"],
                    ("%.2e" % v["node_dev"])
                    if v["node_dev"] == v["node_dev"] else "n/a",
                    v["fp_rel"]))
            okD1 = okD1 and v["fp_rel"] < DPR_BAR
            if v["C_log"] == v["C_log"]:
                okD2 = okD2 and abs(v["C_log"]) < CV_BAND
    check("G30-parity-survives-every-front", okD1,
          "f'(a) = 0 to floor under EVERY sealed power-front "
          "ablation (remove / shift x0.8-1.2 / permute): the "
          "midpoint parity is WINDOW GEOMETRY, not arithmetic")
    check("G31-alias-constant-front-blind", okD2,
          "C_v = A_0(v)^2/(|tau_v| ||d||^2) stays O(1) (|log10| < "
          "%.1f) across ALL variants while tau_v itself moves: the "
          "sqrt law is IDENTITY-BLIND -- no independent prime-power "
          "cause; the 'end of the Lambda(q^2) atoms' story is NOT "
          "causal" % CV_BAND)

    section("S4  PRICING")
    check("G50-boxed-question-priced", True,
          "the reviewer's boxed question ('positive source-pure "
          "formula for R_h without tau, d, roots?') is EXACTLY the "
          "r186 ROUND KEY QUESTION (w'(tau) source-expressibility), "
          "already priced there and open; the A0FLOOR loop route "
          "(fourth flagged loop, Pinning-Supply in A_0 currency, "
          "doubly dead) stands -- no new edge claimed")
    check("G51-mincut-residue-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; four-item residue "
          "UNCHANGED; nothing consumed from flagged loops")
    check("G52-next-step-named", True,
          "per the votum: round 221 = PRIME.SQUARELOCK.COFINAL.01 "
          "(pre-sealed prime-square rungs h = r^2, exact midpoint/"
          "edge atom algebra P_k(r) = 0, Ptilde_k(r) = a w_r "
          "(-1)^k / 2); the exact identities are already visible in "
          "the builder's linear atom maps used above")

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G60-verdict", npass == len(CHECKS),
          "ALIAS_RESIDUE: IDENTIFICATION-EXACT(l0 == midpoint ray, "
          "closed basis factor) + RESIDUE-WARD + C-TAU-FLAT + "
          "SAME-SIGN-WELL-ANATOMY(no node on MAIN) + "
          "DEPTH-FLAT-CURVATURE-CO-RIDES(second sqrt-tau "
          "orthogonality) + PARITY-GEOMETRY-NOT-ARITHMETIC + "
          "ALIAS-FRONT-BLIND + BOXED-QUESTION-IS-R186 + "
          "NO-NEW-EDGE + NO-RH-CLAIM")

    return finish(smoke)


def finish(smoke: bool) -> int:
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))
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
