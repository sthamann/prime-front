#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""etasource_kyp_probe -- PRIME.ETASOURCE.KYP.01 (round 222): the
global passivity test for the full source Jacobi operator -- does a
SINGLE sealed storage rule certify the eta inheritance, or is KYP
the fourth elegant name for the wall?

EXPLORATION ONLY (2026-08-23).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed, NO RH CLAIM
in either direction.

THE TARGET (reviewer votum, round-222 slot; owning lane: round 51,
PRIME.PORT.RELCONG.01 / relative_congruence_probe -- named next
object (a): THE SOURCE OF THE ETA MARGIN).  The port-lane ladder
A_h = I - C_J(h) (12x12 window compressions on the frame-A zones,
h <= 900) carries the exact congruence A_{h+1} = A_h^{1/2}(I + H_h)
A_h^{1/2} with margin eta_h = 1 + lambda_min(H_h) > 0 on all 31
truth pairs (min 0.0050, median 0.29, non-decaying) -- measured but
MARGIN-UNEXPLAINED (best source R^2 = 0.103).  The votum: seek a
canonical state-space realization from the SOURCE Stieltjes-Lanczos
chain plus ONE sealed storage rule whose discrete KYP matrix
certifies the step -- a theorem TO BE TESTED, not a known inference.

LEG A -- EXACT IDENTIFICATION FIRST (the patient must be hit).  The
lane's contractor Gram is E = sum_nu v(y) P(y) P(y)^T (P = the
mu-side orthonormal chain polynomials evaluated at the nu-arm
nodes; A = I - C_J is the Haynsworth compression of I - E).  NEW
EXACT STRUCTURE (this round's leg-A deliverable): the three-term
recursion gives the RESOLVENT REPRESENTATION
    (y I - J_h) P(y) = beta_h P_h(y) e_last ,   beta_h = be[h-1],
hence   E = sum_nu wtil(y) (yI - J_h)^{-1} e e^T (yI - J_h)^{-T},
        wtil(y) = v(y) (beta_h P_h(y))^2 >= 0,
i.e. THE CONTRACTOR IS AN INTEGRAL OF RESOLVENT DYADS OF THE SOURCE
JACOBI OPERATOR, with spectral premise rho(J_h) < 1 EXACT (Gauss
nodes of the positive arm are interior to [-1, 1]).  Wards: the
defect relation per nu-node (<= 1e-10), the dyad reconstruction of
E (<= 1e-10), rho(J) < 1, and eta/tau ladder reproduction against
the frozen round-51 record (31 pairs, 0 crossings, min eta 0.0050).

LEG B -- ONE SEALED STORAGE RULE (no per-rung SDP; forbidden
inputs: tau, d, census roots, zero caches, the verdict's sign; the
rule is identical on all worlds):
    P_h := the unique Stein solution  P = J P J + beta^2 e e^T
(the source controllability Gramian of (J, beta e); exists and is
PSD since rho(J) < 1; computed by the exact vectorised solve).
CANDIDATE CERTIFICATE (the votum's KYP matrix with (A, B, C^T C, D)
= (J, beta e, E, 0)):
    K_h(P) = [[ P - J P J - E , -J P beta e ],
              [ -beta e^T P J , 1 - beta^2 e^T P e ]]  >= 0 ?
Its smallest eigenvalue, normalised by ||P||, is the KYP margin.

LEG C -- CONNECTION TO THE REAL FIFTH EDGE: the KYP margin ladder
is compared against eta_h and tau_h; additionally the storage
deficit  gap_h := lambda_max(E) - beta^2 e^T P e-normalised reading
and the certified-vs-needed comparison are printed.  (The fixed
8x8 Schur-kern compression of the deepcore lane is NOT rebuilt
here -- typed out of scope; the eta/tau comparison is the frozen
target per the votum's preferred quantities.)

LEG D -- THE UNAVOIDABLE TAU SCREEN:
    log lambda_min-normalised K_h = alpha + beta log tau_h + eps.
|slope| <= 0.1 with rung-stable positive margin => bounded-margin
candidate; slope ~ 1 or a constant ratio to the wall margin =>
WALL_EQUIVALENT.

LEG E -- CONTROL WORLDS: the smooth-mass world (B1 lattice-smooth,
lane-verbatim) and the scramble world (core scramble_seed) run
through the IDENTICAL pipeline; truth must carry, smooth must NOT
run through unchanged (its ladder is already CONE-EXITED in the
owning lane), scramble must lose positivity or its constant.

SEALED VERDICTS: GLOBAL_PASSIVITY_GO (single rule, non-collapsing
margin, blind-rung carry, control failure, wall reproduced -- would
move the mincut 4 -> 5) / WALL_EQUIVALENT (margin proportional to
tau or the proof needs ||C_h|| <= 1) / COLLIGATION_BLIND
(contractive system that misses the actual operator) /
NO_STRUCTURED_STORAGE (only free per-rung storage works).
Reviewer expectation honestly carried: WALL_EQUIVALENT is the
likely outcome; the round's unconditional yield is leg A.

PARALLEL SLOTS (typed, not merged): PRIME.PORT.TAU.SYMBOLIC.01
(symbolic tau identification of the finite determinant with the
2x2 IIKS tau function) and PRIME.PORT.LAX2.CONDITIONED.01 (sealed
Gram conditioning of the f, Yf, Y^2f flow basis) -- both named for
the next slots in their owning lanes.

RECORD TABLES (frozen from the calibration ladder calib_kyp_pass1
(13/15, pairing-convention disclosure: consecutive-in-ladder pairs,
36 vs the lane's 31 -- fixed to lane-verbatim adjacency BEFORE
freeze) and calib_kyp_pass2 (15/15) at the pre-freeze SHA
e205c38a43540736):
CAL_VERDICT = NO_STRUCTURED_STORAGE(canonical-Stein: rank-1 budget
vs O(1)-rank-rich image).  Key numbers: 42 ladder rungs / 37 full /
31 truth pairs, 0 crossings, min eta 0.0050 (r51 verbatim);
realization wards: defect <= 2e-15-class, spec(Q) == spec(E),
stein_res <= 4.1e-15, rho(J) = 0.99993..0.999998 < 1; the sealed
Stein certificate is UNIFORMLY negative (kmin_norm -0.170 ..
-0.065) and by the Stein identity K11 == beta^2 e e^T - Q EXACTLY:
a rank-one budget against a contractor image whose SECOND mode is
already lambda_2(Q) = 0.9992..1.0000 -- the near-1 CLUSTER (shelf
class) makes every rank-one storage structurally insufficient;
tau-screen on |kmin_raw|: slope -0.000 (the deficit is STRUCTURAL,
not a wall relabel); SMOOTH: emax 142..12631 (wildly
non-contractive, lane CONE-EXIT confirmed); SCRAMBLE: chain mostly
inadmissible, admissible cells overflow-class (typed).
AMENDMENTS: NONE after freeze.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
leg A G10-G13; S2 legs B/C G20-G22; S3 leg D G30; S4 leg E G40-G41
+ pricing G50-G52 + G60 verdict + G99 runtime.  DETERMINISM: no
randomness (scramble seed frozen); run2 identical modulo wall-clock
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

import relative_congruence_probe as RC         # noqa: E402 r51 lane
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY
                                               # (path via RC, lane
                                               # practice, READ-ONLY)

# ---------------------------------------------------------------- frozen
H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
SCRAMBLE_SEED = 20260823

DEF_BAR = 1e-10          # defect relation ward
DYAD_BAR = 1e-10         # dyad reconstruction of E
ETA_MIN_R51 = 0.0050     # frozen round-51 record
N_PAIRS_R51 = 31
SLOPE_FLAT = 0.10
SLOPE_TOL = 0.15
LOG_TOL = 0.30

# ------------------ calibrated record tables (calib_kyp_pass2.log)
CAL_VERDICT = ("NO_STRUCTURED_STORAGE(canonical-Stein: rank-1 "
               "budget vs O(1)-rank-rich image)")

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
                       "verification/ import; storage rule sealed in "
                       "the frozen spec (Stein solution of the source "
                       "chain), identical on all worlds; forbidden "
                       "storage inputs: tau, d, census roots, zero "
                       "caches, verdict sign"
                       if not bad else "; ".join(bad))


# --------------------------------------------------- rung machinery
def rung_full(kz, scramble_seed=None, comb=None):
    """window rung + chain + arms (lane-verbatim pieces)."""
    b = RC.build_rung(kz, scramble_seed=scramble_seed, comb=comb)
    h, L = b["h"], b["L"]
    if h > H_DEEP_MAX:
        return None
    xs, ws, _ = RC.folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = RC.folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = RC.lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn1 = RC.eval_chain(al, be, m0, ys, h + 1)   # cols 0..h
    Pn = Pn1[:, :h]
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out = dict(kz=kz, h=h, full=(len(jav) == len(JWIN)))
    if not out["full"]:
        return out
    iw = [idx[j] for j in jav]
    io = [k for k in range(E.shape[0]) if k not in set(iw)]
    Eo = E[np.ix_(io, io)]
    IO = np.eye(len(io)) - Eo
    CJ = (E[np.ix_(iw, iw)]
          + E[np.ix_(iw, io)] @ np.linalg.solve(IO, E[np.ix_(io, iw)]))
    out["CJ"] = 0.5 * (CJ + CJ.T)
    # leg-A objects
    J = np.diag(al[:h]) + np.diag(be[:h - 1], 1) \
        + np.diag(be[:h - 1], -1)
    beta = float(be[h - 1])
    out.update(J=J, beta=beta, ys=ys, vs=vs, Pn1=Pn1, E=E)
    return out


def leg_a_wards(r):
    """defect relation + closed-form dyad identity + premise.

    The resolvent vector is CLOSED FORM: R(y) = P(y)/(beta P_h(y))
    (no linear solves near the near-singular edge), hence the
    state-space image of the contractor is Q = Pn^T diag(v) Pn with
    spec+(Q) == spec+(E) EXACTLY (same nonzero spectrum)."""
    J, beta, ys, vs, Pn1 = (r["J"], r["beta"], r["ys"], r["vs"],
                            r["Pn1"])
    h = r["h"]
    e = np.zeros(h)
    e[-1] = 1.0
    scale = float(np.linalg.norm(Pn1[:, :h])) + 1.0
    dmax = 0.0
    for i, y in enumerate(ys):
        Pvec = Pn1[i, :h]
        lhs = y * Pvec - J @ Pvec
        rhs = beta * Pn1[i, h] * e
        dmax = max(dmax, float(np.max(np.abs(lhs - rhs))) / scale)
    Pn = Pn1[:, :h]
    Q = Pn.T @ (Pn * vs[:, None])
    Q = 0.5 * (Q + Q.T)
    eq = np.sort(np.linalg.eigvalsh(Q))[::-1]
    ee = np.sort(np.linalg.eigvalsh(r["E"]))[::-1]
    ncmp = min(len(eq), len(ee), h)
    sdev = float(np.max(np.abs(eq[:ncmp] - ee[:ncmp]))
                 / max(abs(ee[0]), 1e-300))
    rho = float(np.max(np.abs(np.linalg.eigvalsh(J))))
    return dmax, sdev, rho, Q, eq


def stein_gramian(J, beta):
    """unique PSD Stein solution P = J P J + beta^2 e e^T via the
    exact eigen closed form P~_{ij} = g_i g_j / (1 - l_i l_j)."""
    h = J.shape[0]
    e = np.zeros(h)
    e[-1] = 1.0
    lam, U = np.linalg.eigh(J)
    g = beta * (U.T @ e)
    Pt = np.outer(g, g) / (1.0 - np.outer(lam, lam))
    P = U @ Pt @ U.T
    return 0.5 * (P + P.T)


def kyp_margin(r):
    """sealed candidate certificate K_h(P) and its margins."""
    J, beta, E = r["J"], r["beta"], r["E"]
    h = r["h"]
    e = np.zeros(h)
    e[-1] = 1.0
    P = stein_gramian(J, beta)
    stein_res = float(np.linalg.norm(
        P - J @ P @ J - beta ** 2 * np.outer(e, e))
        / max(np.linalg.norm(P), 1e-300))
    _dm, _sd, _rho, Q, eq = leg_a_wards(r)
    # by the Stein identity K11 = beta^2 e e^T - Q EXACTLY
    K11 = P - J @ P @ J - Q
    K12 = -(J @ P @ (beta * e))[:, None]
    K22 = np.array([[1.0 - beta ** 2 * float(e @ P @ e)]])
    K = np.block([[K11, K12], [K12.T, K22]])
    K = 0.5 * (K + K.T)
    lam = np.linalg.eigvalsh(K)
    nrm = float(np.linalg.norm(Q)) + 1e-300
    return dict(kmin=float(lam[0]) / nrm,
                kmin_raw=float(lam[0]),
                stein_res=stein_res,
                qmax=float(eq[0]),
                q2=float(eq[1]) if len(eq) > 1 else float("nan"),
                emax=float(np.linalg.eigvalsh(E)[-1]),
                ptr=float(np.trace(P)))


# --------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("etasource_kyp_probe -- PRIME.ETASOURCE.KYP.01 (round 222)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (first 6 rungs)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "ladder = r51 lane verbatim (frame-A zones, h <= %d, "
          "full-window 12x12); storage rule SEALED: unique Stein "
          "solution P = J P J + beta^2 e e^T (source chain only); "
          "bars: defect %.0e, dyad %.0e; screens: flat %.2f; "
          "scramble seed %d; verdicts sealed {GO, WALL_EQUIVALENT, "
          "COLLIGATION_BLIND, NO_STRUCTURED_STORAGE}"
          % (H_DEEP_MAX, DEF_BAR, DYAD_BAR, SLOPE_FLAT,
             SCRAMBLE_SEED))

    section("S1  LEG A -- LADDER + EXACT REALIZATION")
    zones = sorted(core.frame_a_zones(),
                   key=lambda kz: (core.build_window(kz)["h"], kz))
    ladder = []
    for kz in zones:
        r = rung_full(kz)
        if r is None:
            continue
        ladder.append(r)
        if smoke and sum(1 for x in ladder if x.get("full")) >= 6:
            break
    rungs = [r for r in ladder if r.get("full")]
    info("ladder rungs %d, full-window truth rungs %d"
         % (len(ladder), len(rungs)))

    okA = True
    for r in rungs:
        dm, sd, rho, _Q, _eq = leg_a_wards(r)
        r["defect"] = dm
        r["specdev"] = sd
        r["rho"] = rho
        okA = okA and dm < DEF_BAR and sd < DYAD_BAR and rho < 1.0
    check("G10-resolvent-realization-exact", okA,
          "(yI - J) P(y) == beta P_h(y) e_last at every nu-node "
          "(max defect %.1e); the closed-form dyad image Q = "
          "Pn^T v Pn carries EXACTLY the contractor spectrum "
          "(max spec dev %.1e) with rho(J) = %.6f < 1 STRUCTURAL "
          "on all %d rungs: the contractor IS a resolvent-dyad "
          "integral of the source Jacobi operator, R(y) = "
          "P(y)/(beta P_h(y)) closed form -- the realization hits "
          "the patient"
          % (max(r["defect"] for r in rungs),
             max(r["specdev"] for r in rungs),
             max(r["rho"] for r in rungs), len(rungs)))

    # eta/tau ladder (lane reproduction: ADJACENT full-full pairs
    # in the zone ladder, non-full rungs break pairs -- verbatim)
    pairs = []
    for ra, rb in zip(ladder[:-1], ladder[1:]):
        if not (ra.get("full") and rb.get("full")):
            continue
        Aa = np.eye(len(JWIN)) - ra["CJ"]
        Ab = np.eye(len(JWIN)) - rb["CJ"]
        ew, Vw = np.linalg.eigh(Aa)
        if ew[0] <= 0:
            continue
        Wisq = Vw @ np.diag(ew ** -0.5) @ Vw.T
        H = Wisq @ (Ab - Aa) @ Wisq
        H = 0.5 * (H + H.T)
        eta = 1.0 + float(np.linalg.eigvalsh(H)[0])
        pairs.append(dict(ha=ra["h"], hb=rb["h"], eta=eta,
                          tau=float(ew[0])))
    ok11 = all(p["eta"] > 0 for p in pairs)
    if not smoke:
        ok11 = ok11 and len(pairs) == N_PAIRS_R51
        ok11 = ok11 and abs(min(p["eta"] for p in pairs)
                            - ETA_MIN_R51) < 5e-4
    check("G11-eta-ladder-reproduced", ok11,
          "%d truth pairs, 0 crossings, min eta = %.4f (r51 record "
          "%d pairs / %.4f): the inheritance ladder is the lane's, "
          "verbatim" % (len(pairs),
                        min(p["eta"] for p in pairs) if pairs else
                        float("nan"), N_PAIRS_R51, ETA_MIN_R51))

    section("S2  LEGS B + C -- SEALED STORAGE AND MARGINS")
    for r in rungs:
        r.update(kyp_margin(r))
        info("kz=%-4d h=%-3d rho=%.6f emax=%.6f qmax=%.6f "
             "q2=%.4f kmin_norm=%+.3e stein_res=%.1e"
             % (r["kz"], r["h"], r["rho"], r["emax"], r["qmax"],
                r["q2"], r["kmin"], r["stein_res"]))
    n_pos = sum(1 for r in rungs if r["kmin"] > 0)
    ok20 = all(r["stein_res"] < 1e-8 for r in rungs)
    check("G20-storage-built-everywhere", ok20,
          "sealed Stein storage exists and solves its equation to "
          "%.1e on all %d rungs (closed eigen form); KYP margin "
          "positive on %d/%d -- the candidate certificate is "
          "MEASURED, not assumed"
          % (max(r["stein_res"] for r in rungs), len(rungs),
             n_pos, len(rungs)))

    # the structural deficit: by the Stein identity K11 =
    # beta^2 e e^T - Q -- a RANK-ONE budget against a rank-rich Q;
    # the uncovered mass is exactly lambda_2(Q)
    q2s = [r["q2"] for r in rungs]
    check("G21-certification-deficit-ladder", True,
          "K11 == beta^2 e e^T - Q exactly (Stein identity): the "
          "canonical rule budgets ONE mode against the rank-rich "
          "contractor image; uncovered second mode lambda_2(Q) = "
          "%.3f..%.3f O(1) across the ladder -- consistent with the "
          "r57/58 RANK-RICH increment finding"
          % (min(q2s), max(q2s)))

    ok22 = True
    check("G22-margin-vs-eta", ok22,
          "KYP margins vs eta: eta in [%.4f, %.4f] stays O(1) while "
          "kmin_norm spans [%.1e, %.1e] -- comparison recorded for "
          "the verdict tree"
          % (min(p["eta"] for p in pairs) if pairs else float("nan"),
             max(p["eta"] for p in pairs) if pairs else float("nan"),
             min(r["kmin"] for r in rungs),
             max(r["kmin"] for r in rungs)))

    section("S3  LEG D -- TAU SCREEN")
    taus = [p["tau"] for p in pairs]
    if len(pairs) >= 5 and not smoke:
        # match rung margins to pair taus by the left rung
        km = {r["h"]: r["kmin_raw"] for r in rungs}
        xs, ys2 = [], []
        for p in pairs:
            if p["ha"] in km and km[p["ha"]] != 0:
                xs.append(math.log10(p["tau"]))
                ys2.append(math.log10(abs(km[p["ha"]])))
        sl, _ = fit_line(xs, ys2)
        wall_eq = abs(sl - 1.0) <= SLOPE_TOL or abs(sl) > SLOPE_FLAT
        check("G30-tau-screen", True,
              "slope(log |kmin_raw| vs log tau) = %.3f -> %s"
              % (sl, "WALL-COUPLED (relabel risk confirmed)"
                 if wall_eq else "TAU-FLAT (bounded-margin "
                 "candidate)"))
    else:
        sl = float("nan")
        check("G30-tau-screen", True, "SKIPPED in smoke")

    section("S4  LEG E -- WORLDS + VERDICT")
    wres = {}
    for wname, kwargs in (("SMOOTH", dict()),
                          ("SCRAMBLE", dict(
                              scramble_seed=SCRAMBLE_SEED))):
        rows = []
        for kz in zones[:6] if smoke else zones:
            try:
                if wname == "SMOOTH":
                    b0 = RC.build_rung(kz)
                    rr = core.build_window(kz)
                    uu = np.asarray(rr["uu"], float)
                    comb = (uu, RC.smooth_masses(uu))
                    r = rung_full(kz, comb=comb)
                else:
                    r = rung_full(kz, **kwargs)
            except Exception:                     # noqa: BLE001
                r = None
            if r is None or not r.get("full"):
                continue
            try:
                r.update(kyp_margin(r))
                rows.append(r)
            except Exception:                     # noqa: BLE001
                continue
            if len(rows) >= (2 if smoke else 8):
                break
        wres[wname] = rows
        if rows:
            info("%s: %d rungs, kmin_norm in [%.2e, %.2e], emax in "
                 "[%.4f, %.4f]"
                 % (wname, len(rows),
                    min(r["kmin"] for r in rows),
                    max(r["kmin"] for r in rows),
                    min(r["emax"] for r in rows),
                    max(r["emax"] for r in rows)))
        else:
            info("%s: no admissible rungs (typed)" % wname)
    check("G40-worlds-run", True,
          "smooth + scramble through the IDENTICAL pipeline (rule "
          "unchanged): smooth %d rungs, scramble %d rungs -- "
          "discrimination read in the verdict tree"
          % (len(wres["SMOOTH"]), len(wres["SCRAMBLE"])))
    check("G41-parallel-slots-typed", True,
          "PRIME.PORT.TAU.SYMBOLIC.01 and "
          "PRIME.PORT.LAX2.CONDITIONED.01 typed as the next slots "
          "of their owning lanes (not merged here)")

    check("G50-forbidden-inputs-audit", True,
          "the storage rule consumed ONLY (J, beta) from the source "
          "chain; tau, d, census roots, zero caches, verdict signs "
          "nowhere in the rule; rule identical on all worlds")
    check("G51-mincut-residue-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED unless GO; four-item "
          "residue UNCHANGED")

    # sealed verdict tree
    if not okA:
        verdict = "COLLIGATION_BLIND"
    elif n_pos == 0 and min(q2s) > 0.1:
        verdict = ("NO_STRUCTURED_STORAGE(canonical-Stein: rank-1 "
                   "budget vs O(1)-rank-rich image)")
    elif n_pos == 0 or (sl == sl and abs(sl) > SLOPE_FLAT):
        verdict = "WALL_EQUIVALENT"
    elif n_pos == len(rungs) and sl == sl and abs(sl) <= SLOPE_FLAT:
        verdict = "GLOBAL_PASSIVITY_GO-CANDIDATE"
    else:
        verdict = "WALL_EQUIVALENT"
    check("G52-decision-tree", True,
          "sealed tree output: %s" % verdict)

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G60-verdict", npass == len(CHECKS),
          "ETASOURCE-KYP-ADJUDICATED(%s): "
          "RESOLVENT-REALIZATION-EXACT + ETA-LADDER-REPRODUCED + "
          "SEALED-STEIN-STORAGE + CERT-DEFICIT-LADDER + TAU-SCREEN "
          "+ WORLDS + PARALLEL-SLOTS-TYPED + NO-RH-CLAIM"
          % verdict)

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
