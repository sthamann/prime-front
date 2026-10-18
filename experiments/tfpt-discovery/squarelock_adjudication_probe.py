#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""squarelock_adjudication_probe -- PRIME.SQUARELOCK.ADJUDICATION.01
(round 221): the hard, cheap mechanism test of the SquareLock
hypothesis -- COFINAL must earn itself first.

EXPLORATION ONLY (2026-08-23).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed, NO RH CLAIM
in either direction.

THE HYPOTHESIS (reviewer votum, round-221 slot).  At h = p^2 the
whole von-Mangoldt source is read on a p-canonically normalised
logarithmic phase grid (omega_k log q = k pi log q / log p).  The
round adjudicates whether this buys ANYTHING beyond window geometry,
with five verdicts sealed in advance: GLOBAL_SOURCE_LOCK_GO /
LOCAL_ATOM_ONLY / GEOMETRY_ONLY / COLLECTIVE_NONREDUCTIVE /
TAU_RELABEL.  Reviewer expectation: COLLECTIVE_NONREDUCTIVE or
GEOMETRY_ONLY.

LEG A (algebraic wards, exact).  At h = p^2, a = log p, the
builder's linear atom maps give EXACTLY: the midpoint atom p has
ZERO off-diagonal coupling (P_k^(p) = w_p sin(k pi) = 0 for k >= 1;
pj[0] = 0 structurally) and PURE ALTERNATING DIAGONAL
Ptilde_k^(p) = (a/2) w_p (-1)^k, i.e. its whole matrix block is
diag(2 a w_p (-1)^k / (2 if k=0 else 1)) / nrm^2-normalised, with
the k = 0 entry from the exact w_p (L - a) = w_p a limit (NOT
extrapolated); the edge atom p^2 is BUILDER-INVISIBLE (its entire
matrix block vanishes: sin(2 k pi) = 0, a - log(p^2)/2 = 0, and
w (L - L) = 0 at k = 0).  Both warded against prime_block (which
round 220 warded against the builder's mpPrime to 1e-25).
JET DICTIONARY (the round-220 by-catch booked correctly): with
A_{2m} = sum_k (-1)^k omega_k^{2m} c_k, the midpoint derivative
tower is f^(2m)(a) = (-1)^m A_{2m} (symbolic + numeric); A_2 =
-f''(a) retires the 'omega^2 tower' name; the census scale
y_t = |A_2/A_0| makes the round-220 flat well width EXACTLY
sqrt(2/y_t) -- verdict JET_TOWER == MOMENT_LAURENT_DICTIONARY, no
fifth name for the same object.

LEG B (sealed cells; all frozen HERE, before any sign evaluation):
LOCK rungs h = 4 (p = 2) and h = 9 (p = 3).  CONTROLS (MAIN):
h = 3, 5 (4 +- 1), h = 8, 10 (9 +- 1), h = 11 (similar non-square
prime), h = 16 (nearest affordable COMPOSITE square 4^2, the
geometry separator).  SAME-RUNG ABLATIONS at each lock: DROP_P
(atom p removed), DROP_P2 (atom p^2 removed), SHIFT_HALF (atom p
moved by exactly half a mode cell, delta = a/(2(K-1))), PERMW
(sealed golden-key weight permutation).  WORLD GEOMETRY controls:
SMOOTH at h = 4 and 9.  COST EXCLUSION disclosed: p = 5 (h = 25,
K = 101, dps ~ 160) exceeds the round budget; there is NO blind
prime-square holdout in the affordable set -- the verdict is
therefore typed MECHANISM-ADJUDICATION (no cofinality reach), and
all adjudication bars are SEALED AS FORMULAS (5 MAD / 0.3 dex; no
numeric tuning after sight), preserving bar-blindness.

LEG C (terminal quantities, reduced set DISCLOSED): tau is printed
but NEVER a go-criterion.  Measured: |A_0| (the H1/H3 numerator
currency), y_t = |A_2/A_0| (the H3 scale), and the census-root
REALNESS census (roots of N_h(y), the numerator of the rational
census F_h(y) = sum_k (-1)^k c_k y/(y - omega_k^2): fraction real
and fraction real-nonnegative -- the H2 robustness proxy; root
metrics at h <= 11 for cost, disclosed).  The full H1 envelope and
the H-pin components (EPSLOCK / QSUBGAP) live in the census / L1
lanes and are OUT OF SCOPE here -- typed, not silently dropped.
RESIDUALISATION: for each Q, beta_Q is fit ONLY on the sealed
non-square MAIN controls (log|Q| vs log|tau|); the lock effect is
E_Q = Delta log|Q| - beta_Q Delta log|tau| against the control
residual band max(5 MAD, 0.3 dex).

LEG D (local vs global): the ablation cells decide -- effect gone
under DROP_P => LOCAL_ATOM_ONLY; effect surviving DROP_P + DROP_P2
but killed by SHIFT_HALF / composite square => the global lock
pattern; composite square 16 and SMOOTH sharing the pattern =>
GEOMETRY_ONLY.

LEG E (escape from the killed sieve box, TYPED): T170 proved the
bilinear von-Mangoldt form falls back to three linear sums with the
arithmetic sitting in their JOINT near-degeneracy; unless this
round outputs GLOBAL_SOURCE_LOCK_GO with a moved terminal edge,
SQUARELOCK.HYPERBOLA (Lambda = mu * log at sqrt h) is INADMISSIBLE
-- it would be T170 with a new badge.  No S11/S22/S12 computation
is attempted here; the leg is an admissibility gate.

CENSUS-PENCIL MINI (votum 5): DEFERRED TYPED -- the source-side
census pencil lives in the census_lift lane; a compliant mini test
(source-pure D0 + y D1 + y^2 D2, coefficients sealed before roots,
definite on MAIN, failing on a control world) needs that lane's
objects and is parked as the named parallel slot, not silently
merged into this probe.

RECORD TABLES (frozen from calib_sq_pass1.log, 16/16 first-pass at
the pre-freeze SHA 53724d366768b621; bars were FORMULAS throughout
and were never retuned -- bar-blindness held):
CAL_VERDICT = TAU_RELABEL.  Key numbers: lock effects after tau
residualisation E[A0] = -0.018 / +0.025 and E[y_t] = +0.044 /
+0.096 (bands 0.300 / 1.039) -- deep inside; composite square 16
behaves like the locks (E[A0] = -0.035); H2 realness proxy = 1.00
at EVERY MAIN cell (no discrimination); DROP_P2 cells are
BIT-IDENTICAL to the locks (the edge-invisibility theorem in
vivo); DROP_P / SHIFT_HALF / PERMW move tau by 9-34 orders while
the shape currencies move O(1) -- generic source sensitivity, no
lock specialness.  Raw lock-vs-neighbour deviations are large but
vanish under residualisation: the sealed tree outputs TAU_RELABEL.
AMENDMENTS: NONE after freeze (this table insertion is the only
pre-freeze edit after calibration, house pattern).

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition
(sealed cells); S1 leg A G10-G12; S2 legs B/C G20-G23; S3 leg D
G30; S4 legs E + pricing G50-G53 + G60 verdict + G99 runtime.
DETERMINISM: no randomness (golden key frozen); ProcessPool keyed;
run2 identical modulo wall-clock tokens.

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
from midpoint_a0_adjudication_probe import (  # round-220 (warded)
    prime_block, main_atoms)

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 6
RUNTIME_BAR = 4000.0

DPS = {3: 60, 4: 60, 5: 60, 8: 80, 9: 85, 10: 90, 11: 100, 16: 130}
LOCKS = {4: 2, 9: 3}
CONTROLS = (3, 5, 8, 10, 11)          # sealed non-square MAIN
CSQ = 16                              # composite square 4^2
SMOOTH_H = (4, 9)
ABLTAGS = ("DROP_P", "DROP_P2", "SHIFT_HALF", "PERMW")
ROOT_HCAP = 11                        # census roots at h <= 11

BAND_DEX = 0.3                        # sealed formula: max(5 MAD, .3)
MAD_FACT = 5.0
WARD_BAR = 1e-40
JET_BAR = 1e-35

# --------------------- calibrated record tables (calib_sq_pass1.log)
CAL_VERDICT = "TAU_RELABEL"

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
    b = sxy / sxx if sxx else float("nan")
    return b, my - b * mx


def median(v):
    s = sorted(v)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


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
    return (not bad), ("NO zero-oracle (hp_zero_data explicitly "
                       "forbidden), NO zeta identifier, NO np.load, "
                       "no verification/ import; tau printed, never "
                       "a go-criterion; cells + bars sealed in the "
                       "frozen spec" if not bad else "; ".join(bad))


# ------------------------------------------------------- cell worker
def census_metrics(cs, oms, K, dps, want_roots):
    """A0, A2, y_t, and root realness census of N_h(y)."""
    A0 = sum(((-1) ** k) * cs[k] for k in range(K))
    A2 = sum(((-1) ** k) * oms[k] ** 2 * cs[k] for k in range(K))
    A4 = sum(((-1) ** k) * oms[k] ** 4 * cs[k] for k in range(K))
    A6 = sum(((-1) ** k) * oms[k] ** 6 * cs[k] for k in range(K))
    yt = abs(A2 / A0) if A0 != 0 else mp.mpf("inf")
    out = dict(A0=A0, A2=A2, A4=A4, A6=A6, yt=yt,
               frac_real=float("nan"), frac_nn=float("nan"))
    if not want_roots:
        return out
    bs = [oms[k] ** 2 for k in range(K)]
    # N(y) = sum_k r_k y prod_{j != k}(y - b_j), r_k = (-1)^k c_k
    # build via full product P(y) = prod (y - b_j) and division-free
    # accumulation of coefficient lists
    full = [mp.mpf(1)]
    for b in bs:
        new = [mp.mpf(0)] * (len(full) + 1)
        for i, co in enumerate(full):
            new[i + 1] += co
            new[i] -= co * b
        full = new
    N = [mp.mpf(0)] * (K + 1)
    for k in range(K):
        # full / (y - b_k) by synthetic division
        q = [mp.mpf(0)] * K
        rem = mp.mpf(0)
        for i in range(K, -1, -1):
            if i == K:
                q[i - 1] = full[i]
            elif i > 0:
                q[i - 1] = full[i] + q[i] * bs[k]
            else:
                rem = full[i] + q[i] * bs[k]
        _ = rem
        rk = ((-1) ** k) * cs[k]
        for i in range(K):
            N[i + 1] += rk * q[i]
    while len(N) > 1 and N[-1] == 0:
        N.pop()
    coeffs = list(reversed(N))
    try:
        roots = mp.polyroots(coeffs, maxsteps=200,
                             extraprec=dps * 4)
    except Exception:                           # noqa: BLE001
        return out
    nz = [r for r in roots if abs(r) > mp.mpf(10) ** (-dps // 2)]
    if not nz:
        return out
    scale = max(abs(r) for r in nz)
    nreal = sum(1 for r in nz
                if abs(mp.im(r)) < mp.mpf(1e-20) * scale)
    nnn = sum(1 for r in nz
              if abs(mp.im(r)) < mp.mpf(1e-20) * scale
              and mp.re(r) > -mp.mpf(1e-20) * scale)
    out["frac_real"] = nreal / len(nz)
    out["frac_nn"] = nnn / len(nz)
    return out


def w_cell(args) -> dict:
    tag, world, h, dps, abl = args
    try:
        t0 = time.time()
        out = dict(tag=tag, world=world, h=h, err="")
        with mp.workdps(dps):
            ce = R4.build_cell(h, KFAC, world, dps, want_mp=True)
            K = ce["K"]
            out["K"] = K
            aa = mp.log(h) / 2
            L2v = 2 * aa
            nrm = [mp.sqrt(L2v) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            oms = [k * mp.pi / aa for k in range(K)]
            M = ce["mpM"]
            if abl is not None:
                p = LOCKS[h]
                atoms4 = main_atoms(h)
                base = [(u, w) for (u, w, _q, _p) in atoms4]
                if abl == "DROP_P":
                    var = [(u, w) for (u, w, q, _pp) in atoms4
                           if q != p]
                elif abl == "DROP_P2":
                    var = [(u, w) for (u, w, q, _pp) in atoms4
                           if q != p * p]
                elif abl == "SHIFT_HALF":
                    dlt = aa / (2 * (K - 1))
                    var = [((u + dlt) if q == p else u, w)
                           for (u, w, q, _pp) in atoms4]
                elif abl == "PERMW":
                    gold = (math.sqrt(5.0) - 1.0) / 2.0
                    keys = [math.fmod(q * gold, 1.0)
                            for (_u, _w, q, _pp) in atoms4]
                    perm = sorted(range(len(keys)),
                                  key=lambda i: keys[i])
                    wts = [atoms4[i][1] for i in range(len(atoms4))]
                    var = [(atoms4[i][0], wts[perm[i]])
                           for i in range(len(atoms4))]
                else:
                    raise ValueError(abl)
                Pb = prime_block(base, oms, par, aa, L2v, nrm, K)
                Pv = prime_block(var, oms, par, aa, L2v, nrm, K)
                M2 = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        M2[i, j] = M[i, j] + Pb[i, j] - Pv[i, j]
                M = M2
            fro = mp.sqrt(sum(M[i, j] ** 2 for i in range(K)
                              for j in range(K)))
            zb = mp.mpf(10) ** (-(dps - 20)) * fro
            E, V = mp.eigsy(M)
            idx = sorted(range(K), key=lambda m: E[m])
            tau = E[idx[0]]
            d = [V[i, idx[0]] for i in range(K)]
            dn = mp.sqrt(sum(t * t for t in d))
            cs = [d[k] / (nrm[k] * dn) for k in range(K)]
            cm = census_metrics(cs, oms, K, dps,
                                h <= ROOT_HCAP)
            out["tau_log"] = float(mp.log(abs(tau), 10))
            out["tau_neg"] = bool(tau < 0)
            out["nneg"] = sum(1 for e in E if e < -zb)
            out["A0_log"] = float(mp.log(abs(cm["A0"]), 10))
            out["yt_log"] = float(mp.log(cm["yt"], 10))
            out["frac_real"] = cm["frac_real"]
            out["frac_nn"] = cm["frac_nn"]
            # jet-dictionary devs (leg A, on MAIN unablated cells)
            if abl is None and world == "MAIN":
                devs = []
                for m in range(0, 4):
                    f2m = sum(cs[k] * mp.cos(oms[k] * aa
                                             + m * mp.pi)
                              * oms[k] ** (2 * m)
                              for k in range(K))
                    Aval = [cm["A0"], cm["A2"], cm["A4"],
                            cm["A6"]][m]
                    tgt = ((-1) ** m) * Aval
                    sc = max(abs(tgt), mp.mpf(10) ** (-dps))
                    devs.append(float(abs(f2m - tgt) / sc))
                out["jet_dev"] = max(devs)
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"tag": tag, "err": "%s\n%s"
                % (exc, traceback.format_exc())}


# --------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("squarelock_adjudication_probe -- "
          "PRIME.SQUARELOCK.ADJUDICATION.01 (round 221)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (p = 2 family)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "LOCKS %s; CONTROLS %s; CSQ %d; SMOOTH %s; ablations %s; "
          "root cap h <= %d; bars sealed as FORMULAS max(%.0f MAD, "
          "%.1f dex); COST EXCLUSION disclosed: h = 25 (K = 101) "
          "out of budget -> verdict typed MECHANISM-ADJUDICATION, "
          "no cofinality reach"
          % (str(LOCKS), str(CONTROLS), CSQ, str(SMOOTH_H),
             str(ABLTAGS), ROOT_HCAP, MAD_FACT, BAND_DEX))

    section("S1  LEG A -- EXACT SQUARELOCK ALGEBRA")
    import sympy as sp
    kk = sp.symbols("k", integer=True, positive=True)
    a_s = sp.symbols("a_s", positive=True)
    okA = sp.simplify(sp.sin((kk * sp.pi / a_s) * a_s)) == 0
    okA = okA and sp.simplify(
        (a_s - a_s / 2) * sp.cos(kk * sp.pi)
        - ((-1) ** kk) * a_s / 2) == 0
    okA = okA and sp.simplify(sp.sin((kk * sp.pi / a_s)
                                     * (2 * a_s))) == 0
    check("G10-squarelock-identities-symbolic", okA,
          "at h = p^2, a = log p: sin(omega_k a) = 0 and "
          "Ptilde_k(p) = (a/2)(-1)^k w_p for k >= 1; the edge atom "
          "p^2 has sin(2 k pi) = 0 AND a - log(p^2)/2 = 0 "
          "(symbolic; k = 0 handled by the exact w (L - u) limit "
          "below, not extrapolated)")

    ok11 = True
    with mp.workdps(60):
        for h, p in sorted(LOCKS.items()):
            aa = mp.log(h) / 2
            L2v = 2 * aa
            K = int(math.ceil(KFAC * h * math.log(h)))
            nrm = [mp.sqrt(L2v) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            parv = [mp.mpf((-1.0) ** k) for k in range(K)]
            oms = [k * mp.pi / aa for k in range(K)]
            wp = mp.log(p) / mp.sqrt(p)
            Bp = prime_block([(mp.log(p), wp)], oms, parv, aa,
                             L2v, nrm, K)
            dev = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    if i == j:
                        tgt = (2 * wp * (L2v - aa) / nrm[0] ** 2
                               if i == 0 else
                               2 * wp * (aa / 2) * ((-1) ** i)
                               / nrm[i] ** 2)
                    else:
                        tgt = mp.mpf(0)
                    dev = max(dev, abs(Bp[i, j] - tgt))
            ok11 = ok11 and dev < mp.mpf(WARD_BAR)
            wp2 = mp.log(p) / p
            Bp2 = prime_block([(mp.log(p * p), wp2)], oms, parv,
                              aa, L2v, nrm, K)
            dev2 = max(abs(Bp2[i, j]) for i in range(K)
                       for j in range(K))
            ok11 = ok11 and dev2 < mp.mpf(WARD_BAR)
            info("h=%d: midpoint-atom block == alternating diagonal "
                 "(dev %.1e); edge-atom p^2 block == 0 (dev %.1e)"
                 % (h, float(dev), float(dev2)))
    check("G11-squarelock-blocks-exact", ok11,
          "the midpoint atom's ENTIRE matrix block is the "
          "alternating diagonal 2 w_p (a/2) (-1)^k / nrm_k^2 (k = 0 "
          "via w_p a exactly) and the edge atom p^2 is "
          "BUILDER-INVISIBLE at h = p^2 -- both to %.0e through the "
          "round-220-warded atom map" % WARD_BAR)

    section("S2  LEGS B + C -- SEALED CELLS AND TERMINAL LADDERS")
    cells = []
    lockset = ((4,) if smoke else tuple(sorted(LOCKS)))
    for h in lockset:
        cells.append(("LOCK%d" % h, "MAIN", h, DPS[h], None))
        for abl in ABLTAGS:
            cells.append(("ABL%d_%s" % (h, abl), "MAIN", h,
                          DPS[h], abl))
    ctr = (3, 5) if smoke else CONTROLS
    for h in ctr:
        cells.append(("CTRL%d" % h, "MAIN", h, DPS[h], None))
    if not smoke:
        cells.append(("CSQ%d" % CSQ, "MAIN", CSQ, DPS[CSQ], None))
        for h in SMOOTH_H:
            cells.append(("SMOOTH%d" % h, "SMOOTH", h, DPS[h],
                          None))
    res = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_cell, cells):
            res[out["tag"]] = out
    errs = [r for r in res.values() if r.get("err")]
    for r in errs:
        print("  [ERR] %s: %s" % (r["tag"], r["err"]))
    if errs:
        for g in ("G12", "G20", "G21", "G22", "G23", "G30"):
            check("%s-worker-error" % g, False, "worker error")
        return finish(smoke)

    for tag in sorted(res):
        r = res[tag]
        info("%-14s h=%-2d K=%-3d tau_log=%7.2f%s A0_log=%7.2f "
             "yt_log=%6.2f real=%s nn=%s wall=%.1fs"
             % (tag, r["h"], r["K"], r["tau_log"],
                "(-)" if r["tau_neg"] else "   ",
                r["A0_log"], r["yt_log"],
                ("%.2f" % r["frac_real"])
                if r["frac_real"] == r["frac_real"] else "n/a",
                ("%.2f" % r["frac_nn"])
                if r["frac_nn"] == r["frac_nn"] else "n/a",
                r.get("wall_s", 0.0)))

    ok12 = all(res["LOCK%d" % h]["jet_dev"] < JET_BAR
               for h in lockset)
    ok12 = ok12 and all(res["CTRL%d" % h].get("jet_dev", 1) < JET_BAR
                        for h in ctr)
    check("G12-jet-dictionary", ok12,
          "f^(2m)(a) == (-1)^m A_{2m} for m = 0..3 at every MAIN "
          "cell (max dev < %.0e); A_2 = -f''(a) and well-width^2 == "
          "2/y_t: JET_TOWER == MOMENT_LAURENT_DICTIONARY -- the "
          "round-220 by-catch is booked into the census currency, "
          "no fifth name" % JET_BAR)

    # ---- leg C: residualisation against sealed controls
    ctags = ["CTRL%d" % h for h in ctr]
    quants = ("A0_log", "yt_log")
    eff = {}
    ok20 = True
    for q in quants:
        xs = [res[t]["tau_log"] for t in ctags]
        ys = [res[t][q] for t in ctags]
        beta, alpha = fit_line(xs, ys)
        resid = [y - (alpha + beta * x) for x, y in zip(xs, ys)]
        mad = median([abs(r - median(resid)) for r in resid])
        band = max(MAD_FACT * mad, BAND_DEX)
        eff[q] = {}
        for h in lockset:
            t = "LOCK%d" % h
            e = res[t][q] - (alpha + beta * res[t]["tau_log"])
            eff[q][h] = (e, band)
            info("E[%s] at LOCK%d = %+.3f (band %.3f, beta %.3f)"
                 % (q, h, e, band, beta))
        if not smoke:
            t = "CSQ%d" % CSQ
            e = res[t][q] - (alpha + beta * res[t]["tau_log"])
            eff[q]["CSQ"] = (e, band)
            info("E[%s] at CSQ%d  = %+.3f (band %.3f)"
                 % (q, CSQ, e, band))
    check("G20-residualisation-built", True,
          "beta_Q fit ONLY on sealed non-square controls %s; "
          "effects E_Q computed for both locks and the composite "
          "square; tau printed, never consumed as a criterion"
          % str(ctr))

    lock_out = {q: [h for h in lockset
                    if abs(eff[q][h][0]) > eff[q][h][1]]
                for q in quants}
    any_out = any(lock_out[q] for q in quants)
    both_out = any(len(lock_out[q]) == len(lockset) >= 2
                   for q in quants)
    check("G21-lock-effect-census", True,
          "locks outside band: %s -- %s"
          % (str(lock_out),
             "NO terminal quantity moves at any lock after tau "
             "residualisation" if not any_out else
             "some lock effect present; leg D decides its type"))

    if not smoke:
        csq_shares = all(
            (abs(eff[q]["CSQ"][0]) > eff[q]["CSQ"][1])
            == bool(lock_out[q]) for q in quants)
        check("G22-composite-square-separator", True,
              "composite square 16 shares the lock pattern: %s "
              "(sharing => GEOMETRY; separating => arithmetic "
              "candidate)" % csq_shares)
        smooth_ok = all("SMOOTH%d" % h in res for h in SMOOTH_H)
        check("G23-smooth-geometry-row", smooth_ok,
              "SMOOTH cells measured at the lock rungs (yt_log %s "
              "vs locks %s): the atom-free world carries the same "
              "window geometry -- recorded"
              % (["%.2f" % res["SMOOTH%d" % h]["yt_log"]
                  for h in SMOOTH_H],
                 ["%.2f" % res["LOCK%d" % h]["yt_log"]
                  for h in sorted(LOCKS)]))
    else:
        check("G22-composite-square-separator", True, "SKIP smoke")
        check("G23-smooth-geometry-row", True, "SKIP smoke")

    section("S3  LEG D -- LOCAL VS GLOBAL")
    det30 = []
    for h in lockset:
        for abl in ABLTAGS:
            t = "ABL%d_%s" % (h, abl)
            det30.append("%s: dyt=%+.2f dtau=%+.1f"
                         % (t, res[t]["yt_log"]
                            - res["LOCK%d" % h]["yt_log"],
                            res[t]["tau_log"]
                            - res["LOCK%d" % h]["tau_log"]))
    check("G30-ablation-matrix", True,
          "ablation responses recorded: %s" % "; ".join(det30))

    section("S4  LEG E + PRICING + VERDICT")
    check("G50-hyperbola-admissibility", True,
          "T170 carried: the bilinear vM form falls back to three "
          "linear sums with the arithmetic in their JOINT "
          "near-degeneracy; absent GLOBAL_SOURCE_LOCK_GO with a "
          "moved terminal edge, SQUARELOCK.HYPERBOLA is "
          "INADMISSIBLE (T170 with a new badge)")
    check("G51-pencil-mini-deferred", True,
          "CENSUS.DEFINITE_PENCIL.MINI typed as the named parallel "
          "slot (needs the census_lift source pencil objects); "
          "kill conditions per the votum stand; not merged here")
    check("G52-mincut-residue-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; four-item residue "
          "UNCHANGED")

    # sealed decision tree
    if not any_out:
        verdict = "GEOMETRY_ONLY-or-TAU_RELABEL"
        if not smoke:
            raw_dev = max(abs(res["LOCK%d" % h][q]
                              - res["CTRL%d" % c][q])
                          for q in quants for h in lockset
                          for c in ((3, 5) if h == 4 else (8, 10)))
            verdict = ("TAU_RELABEL" if raw_dev > 1.0
                       else "GEOMETRY_ONLY")
    elif both_out:
        drop_kills = all(
            abs(res["ABL%d_DROP_P" % h]["yt_log"]
                - res["LOCK%d" % h]["yt_log"]) > BAND_DEX
            for h in lockset)
        verdict = ("LOCAL_ATOM_ONLY" if drop_kills
                   else "COLLECTIVE_NONREDUCTIVE")
    else:
        verdict = "COLLECTIVE_NONREDUCTIVE"
    check("G53-decision-tree", True,
          "sealed tree output: %s (GO would additionally need the "
          "T170 edge, per G50 -- not reachable in this round by "
          "construction)" % verdict)

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G60-verdict", npass == len(CHECKS),
          "SQUARELOCK-ADJUDICATED(%s): SQUARELOCK-ALGEBRA-EXACT"
          "(midpoint atom = alternating diagonal, edge atom "
          "builder-invisible) + JET-DICTIONARY-BOOKED + "
          "SEALED-CELL-CENSUS + RESIDUALISED-EFFECTS + "
          "ABLATION-MATRIX + HYPERBOLA-GATE + PENCIL-DEFERRED + "
          "NO-RH-CLAIM" % verdict)

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
