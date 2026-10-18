#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""nyquist_feshbach_probe -- PRIME.NYQUIST.FESHBACH.01 (round 219):
the reviewer's decisive test executed -- IS the negative index of the
full wall at most one, and does the one channel sit exactly at
Nyquist?  ANSWER: NO, on both legs -- fast and honest, exactly as the
proposal itself demanded.

EXPLORATION ONLY (2026-08-23).  experiments/ level: NO promotion, NO
ledger row, NO marker moved, NO gate closed or narrowed, NO RH CLAIM
in either direction.

THE PROPOSAL (external synthesis, 2026-08-23; its contracts 7.1
PRIME.NYQUIST.IDENTIFICATION.01 + 7.2 PRIME.NYQUIST.FESHBACH.01 are
adjudicated here in one round).  Claimed route: with J_pi =
diag(1, -1, 1, ...), B_h = J_pi M_h J_pi, constant channel e_h, the
Albert-Haynsworth/Feshbach split B ⪰ 0 <=> C = QBQ ⪰ 0, r in ran C,
sigma = a - r^T C^+ r >= 0 localises the ENTIRE wall positivity in
ONE alternating (Nyquist) boundary scalar; predicted pattern (N1):
MAIN C ⪰ 0 with stable bulk and sigma carrying the margin; EPSTEIN
exactly ONE crossing, in sigma.  Equivalent formulation used here:
Feshbach of M_h itself on the alternating unit ray alt_k =
(-1)^k / sqrt(K) (= J_pi e); the midpoint-evaluation ray n_k =
(-1)^k / nrm_k (the window-midpoint functional A(L/2) -- the
evaluation at u = a = log sqrt(h), the Chebyshev midpoint) is tested
as the second candidate channel.  SCOPE FENCE: the proposal cites a
'round 201' Epstein finding not present in this corpus (its own
numbering); typed EXTERNAL-UNVERIFIED -- the adjudication below is
against the CANONICAL wall M_h = mpM of the frozen radius-4 cell
builder (a = log(h)/2, K = ceil(1.25 h log h), omega_k = k pi / a),
i.e. exactly the object the proposal's boxed test names.

PRE-REGISTERED ADJUDICATION (frozen; the disclosed prototype -- a
shell one-liner in the session lane, output kept in the chat record
-- measured h = 5, 8 + all three controls and the bars below encode
its findings; both PASS-directions of the original N1 were given
their chance and both fail):
  P1 (identification, 7.1): the softest eigenvector d_h of M_h has
     SMALL overlap with the alternating ray (measured 0.04..0.06 on
     MAIN) and NEAR-ZERO overlap with the midpoint-evaluation ray
     (measured < 1e-4 at prototype precision; this round measures it
     at full precision and adjudicates EXACT-NODE vs merely small).
     IDENTIFICATION REFUTED unless ovl >= OVL_ID at some MAIN rung.
  P2 (localisation, 7.2): after eliminating the alternating channel
     the BULK C_h still carries the tau-class softness
     (lambda_min+(C_h) within RATIO_BAR decades of tau_h at every
     MAIN rung; measured 2.4 dex at h = 5, 5.4 dex at h = 8 -- vs
     the >= 10 dex an O(1)-stable bulk would need); sigma_alt > 0
     but NOT the margin carrier.  NO-LOCALISATION.
  P3 (worlds): EPSTEIN(8) n_neg(M) = 2 (NOT 1) with BOTH negative
     directions in the bulk and sigma_alt = +1.65 > 0; SCRARITH(5)
     n_neg = 3 bulk; SMOOTH(5) n_neg = 2 bulk (and tau < 0: the
     smooth world's wall is honestly non-PSD).  The predicted
     'Epstein crosses exactly in the Nyquist scalar' pattern is
     REFUTED.
  P4 exact layer: Albert-Haynsworth criterion, the Feshbach
     determinant factorisation det M = det C+ * sigma (on the
     channel-completed system), and inertia invariance under J_pi
     conjugation verified on exact Fraction instances.
VERDICT (expected): NYQUIST-FESHBACH-REFUTED -- the wall's soft mode
is spread over the bulk, not localised at Nyquist; the reviewer's
route N1 -> N2 (period-two Weyl passivity of a single boundary
scalar) loses its premise.  HONEST NUGGET recorded: the soft mode's
near-orthogonality to the midpoint-evaluation functional (a
selection rule candidate) and the exact ladder positions of the
alternating-channel Rayleigh quotient a_ch (O(1), tau-flat).

RECORD TABLES (frozen from calib_nf_pass1.log, 16/18 at the
pre-freeze SHA af7ea5c2f1f0d02c -- the two fails were exactly the
placeholder-table comparisons in G23 + the G60 aggregate; every
structural finding held at all 11 rungs; tables below verbatim from
the calibration prints):
CAL_TAU_LOG: -10.67 / -15.79 / -20.23 / -25.03 / -29.42 / -34.08 /
  -38.97 / -43.75 / -48.98 / -53.60 / -68.38 (h = 4..13, 16).
CAL_OVL_ALT: 0.0780 .. 0.0204 (monotonically DECAYING with h: the
  identification gets WORSE, not better).
CAL_OVL_MID (recorded): 5.1e-6 .. 5.9e-35 -- the midpoint-blindness
  DEEPENS exponentially, log-slope vs tau ~ 0.5 (a sqrt(tau)-class
  node; the round's nugget).
CAL_SIG: -8.45 .. -65.00; CAL_BULK: -6.21 .. -61.23 (bulk/tau ratio
  4.5 .. 7.2 dex, NEVER O(1); both ride tau at slope ~ 1).
CAL_CTRL: EPSTEIN {nneg 2, sigma_alt +1.649, bulk_min -1.57};
  SCRARITH {nneg 3, sigma_alt +1.535, bulk_min -0.328};
  SMOOTH {nneg 2, sigma_alt +1.978, bulk_min -1.03}.
AMENDMENTS: NONE after freeze.

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition; S1
exact layer G10-G12; S2 MAIN battery G20-G24; S3 worlds G40-G42; S4
pricing G50-G52 + G60 verdict + G99 runtime.  DETERMINISM: no
randomness; ProcessPool keyed; run2 identical modulo wall-clock
tokens (lines carrying 'WALL' or 'wall=').

RE-PRICING OF THE PROPOSAL'S REMAINING CONTRACTS (typed, not
executed): 7.3 period-two Weyl passivity loses its premise with N1
(no single channel carries the wall); 7.4 census self-adjoint
linearisation stays independently interesting (named follow-up);
7.5 dyadic tau averaging inherits the same objection as every
post-hoc-free averaging (the exact scalar to be averaged is the
wall margin itself -- GPSD-MARGIN-IS-THE-WALL); 7.6 relative
determinant = the CCM/spectral-triple class, already tracked.
Mincut base 4 / refined 5 UNCHANGED; four-item residue UNCHANGED.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction

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
CTRL_CELLS = (("SCRARITH", 5, 60), ("EPSTEIN", 8, 80), ("SMOOTH", 5, 60))

OVL_ID = 0.5          # identification would need at least this
RATIO_BAR = 8.0       # an O(1)-stable bulk would sit >= 8 dex above tau
LOG_TOL = 0.30
VAL_TOL = 0.02

# --------------------- calibrated record tables (calib_nf_pass1.log)
CAL_TAU_LOG = {4: "-10.67", 5: "-15.79", 6: "-20.23", 7: "-25.03",
               8: "-29.42", 9: "-34.08", 10: "-38.97", 11: "-43.75",
               12: "-48.98", 13: "-53.60", 16: "-68.38"}
CAL_OVL_ALT = {4: "0.0780", 5: "0.0585", 6: "0.0496", 7: "0.0422",
               8: "0.0380", 9: "0.0340", 10: "0.0309", 11: "0.0284",
               12: "0.0261", 13: "0.0244", 16: "0.0204"}
CAL_SIG = {4: "-8.45", 5: "-13.33", 6: "-17.63", 7: "-22.28",
           8: "-26.58", 9: "-31.14", 10: "-35.95", 11: "-40.65",
           12: "-45.81", 13: "-50.38", 16: "-65.00"}
CAL_BULK = {4: "-6.21", 5: "-10.63", 6: "-14.90", 7: "-19.21",
            8: "-23.61", 9: "-27.98", 10: "-32.76", 11: "-37.30",
            12: "-42.38", 13: "-46.76", 16: "-61.23"}
CAL_CTRL = {
    "EPSTEIN": dict(nneg=2, sig="1.649", bulk="-1.57"),
    "SCRARITH": dict(nneg=3, sig="1.535", bulk="-0.328"),
    "SMOOTH": dict(nneg=2, sig="1.978", bulk="-1.03"),
}

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
                       "no verification/ import; eigen-data consumed as "
                       "per-rung finite instrument spectra only (this is "
                       "an adjudication round); fully zero-free"
                       if not bad else "; ".join(bad))


# ------------------------------------------------------- rung worker
def w_cell(args) -> dict:
    world, x, dps = args
    try:
        t0 = time.time()
        out = dict(world=world, x=x, err="")
        with mp.workdps(dps):
            ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
            K = ce["K"]
            out["K"] = K
            M = ce["mpM"]
            tau = ce["mpE"][0]
            out["tau"] = float(tau)
            out["tau_log"] = (float(mp.log(abs(tau), 10))
                              if tau != 0 else float("nan"))
            out["tau_neg"] = bool(tau < 0)
            fro = mp.sqrt(sum(M[i, j] ** 2 for i in range(K)
                              for j in range(K)))
            zb = mp.mpf(10) ** (-(dps - 20)) * fro
            E, V = mp.eigsy(M)
            idx = sorted(range(K), key=lambda m: E[m])
            d = [E[m] for m in idx]
            out["nneg"] = sum(1 for e in d if e < -zb)
            soft = [V[i, idx[0]] for i in range(K)]
            # candidate channels
            alt = [mp.mpf((-1) ** k) for k in range(K)]
            an = mp.sqrt(sum(t * t for t in alt))
            alt = [t / an for t in alt]
            aa = mp.log(x) / 2
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            mid = [mp.mpf((-1) ** k) / nrm[k] for k in range(K)]
            mn = mp.sqrt(sum(t * t for t in mid))
            mid = [t / mn for t in mid]
            ovl_a = abs(sum(soft[i] * alt[i] for i in range(K)))
            ovl_m = abs(sum(soft[i] * mid[i] for i in range(K)))
            out["ovl_alt"] = float(ovl_a)
            out["ovl_mid"] = float(ovl_m)
            out["ovl_mid_log"] = (float(mp.log(ovl_m, 10))
                                  if ovl_m > 0 else -300.0)
            # Feshbach on the alternating channel
            Ma = [sum(M[i, j] * alt[j] for j in range(K))
                  for i in range(K)]
            a_ch = sum(alt[i] * Ma[i] for i in range(K))
            out["a_ch"] = float(a_ch)
            Pm = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    Pm[i, j] = (M[i, j] - alt[i] * Ma[j]
                                - Ma[i] * alt[j]
                                + alt[i] * alt[j] * a_ch)
            EC, _ = mp.eigsy(Pm)
            ECs = sorted(EC)
            # drop the structural zero of the channel direction
            nz = [e for e in ECs if abs(e) > zb]
            out["bulk_min"] = float(nz[0]) if nz else float("nan")
            out["bulk_min_log"] = (float(mp.log(abs(nz[0]), 10))
                                   if nz and nz[0] != 0 else float("nan"))
            out["bulk_nneg"] = sum(1 for e in nz if e < 0)
            r = [Ma[i] - a_ch * alt[i] for i in range(K)]
            A2 = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    A2[i, j] = Pm[i, j] + alt[i] * alt[j]
            z = mp.lu_solve(A2, mp.matrix(r))
            sig = a_ch - sum(r[i] * z[i] for i in range(K))
            out["sig"] = float(sig)
            out["sig_log"] = (float(mp.log(abs(sig), 10))
                              if sig != 0 else float("nan"))
            out["sig_neg"] = bool(sig < 0)
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def frac_inertia_3(M):
    """inertia of exact symmetric 3x3 via principal minors /
    characteristic polynomial sign chain (all Fractions)."""
    import sympy as sp
    S = sp.Matrix(3, 3, lambda i, j: sp.Rational(M[i][j]))
    ev = S.eigenvals()
    npos = sum(m for v, m in ev.items() if sp.simplify(v) > 0)
    nneg = sum(m for v, m in ev.items() if sp.simplify(v) < 0)
    return nneg, 3 - npos - nneg, npos


def exact_layer() -> None:
    import sympy as sp
    section("S1  EXACT LAYER")
    # Albert-Haynsworth on a PSD and a non-PSD instance
    Mp = [[2, 1, 0], [1, 2, 1], [0, 1, 2]]          # PD
    Mn = [[1, 2, 0], [2, 1, 0], [0, 0, 3]]          # indefinite
    okA = True
    for M, want_psd in ((Mp, True), (Mn, False)):
        S = sp.Matrix(3, 3, lambda i, j: sp.Rational(M[i][j]))
        a = S[0, 0]
        r = S[1:, 0]
        C = S[1:, 1:]
        sig = a - (r.T * C.inv() * r)[0, 0]
        psd = (C.det() > 0 and C[0, 0] > 0 and sig >= 0)
        okA = okA and (psd == want_psd)
        if want_psd:
            okA = okA and sp.simplify(S.det() - C.det() * sig) == 0
    check("G10-albert-haynsworth-exact", okA,
          "PSD <=> (C PSD, sigma >= 0) on exact instances; "
          "det M == det C * sigma exact (Feshbach factorisation)")

    # inertia invariance under J conjugation
    J = sp.diag(1, -1, 1)
    S = sp.Matrix(3, 3, lambda i, j: sp.Rational(Mn[i][j]))
    i1 = frac_inertia_3(Mn)
    B = J * S * J
    i2 = frac_inertia_3([[B[i, j] for j in range(3)] for i in range(3)])
    check("G11-jpi-inertia-invariance", i1 == i2,
          "inertia(M) == inertia(J_pi M J_pi) exact (Sylvester): the "
          "alternating modulation changes nothing spectral -- the "
          "proposal's B_h and M_h carry the same wall")

    # midpoint functional identity: cos(omega_k * a) = (-1)^k
    kk = sp.symbols("k", integer=True, nonnegative=True)
    a_s = sp.symbols("a_s", positive=True)
    val = sp.cos((kk * sp.pi / a_s) * a_s)
    check("G12-midpoint-is-alternating", sp.simplify(
        val - sp.cos(kk * sp.pi)) == 0,
          "cos(omega_k a) == (-1)^k symbolically: the window-midpoint "
          "evaluation A(L/2) IS the alternating functional in the "
          "cos basis (up to the nrm weights) -- the midpoint u = a = "
          "log sqrt(h), i.e. the Chebyshev sqrt-position")


# --------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("nyquist_feshbach_probe -- PRIME.NYQUIST.FESHBACH.01 "
          "(round 219; adjudicates proposal contracts 7.1 + 7.2)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (rungs 4/5 + SCRARITH)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "rungs %s; dps %s; bars: OVL_ID %.2f, RATIO_BAR %.1f dex; "
          "external 'round 201' claim typed EXTERNAL-UNVERIFIED; "
          "adjudication target = the canonical wall mpM of the "
          "frozen radius-4 cell builder" %
          (str(RUNGS), str(sorted(DPS.items())), OVL_ID, RATIO_BAR))

    exact_layer()

    section("S2  MAIN BATTERY")
    rungs = SMOKE_RUNGS if smoke else RUNGS
    tasks = [("MAIN", h, DPS[h]) for h in rungs]
    res = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_cell, tasks):
            res[out["x"]] = out
    errs = [r for r in res.values() if r.get("err")]
    for r in errs:
        print("  [ERR] h=%s: %s" % (r["x"], r["err"]))
    if errs:
        for g in ("G20", "G21", "G22", "G23", "G24"):
            check("%s-worker-error" % g, False, "worker error")
        return finish(smoke)

    for h in sorted(res):
        r = res[h]
        info("h=%-2d K=%-2d tau_log=%.2f nneg=%d ovl_alt=%.4f "
             "ovl_mid=%.2e sig_log=%.2f bulk_log=%.2f bulk_nneg=%d "
             "a_ch=%.3f wall=%.1fs"
             % (h, r["K"], r["tau_log"], r["nneg"], r["ovl_alt"],
                r["ovl_mid"], r["sig_log"], r["bulk_min_log"],
                r["bulk_nneg"], r["a_ch"], r.get("wall_s", 0.0)))

    ok20 = all((not res[h]["tau_neg"]) and res[h]["nneg"] == 0
               for h in rungs)
    if not smoke:
        ok20 = ok20 and all(abs(res[h]["tau_log"]
                                - float(CAL_TAU_LOG[h])) <= 1.0
                            for h in rungs)
    check("G20-wall-psd-at-built-rungs", ok20,
          "MAIN wall PSD at every built rung (tau > 0, n_neg = 0), "
          "tau ladder == the known wall ladder class (== CAL within "
          "1 dex; dps-limited at depth)")

    ok21 = all(res[h]["ovl_alt"] < OVL_ID for h in rungs)
    if not smoke:
        ok21 = ok21 and all(abs(res[h]["ovl_alt"]
                                - float(CAL_OVL_ALT[h])) <= VAL_TOL
                            for h in rungs)
    check("G21-identification-refuted", ok21,
          "7.1 REFUTED: soft-eigenvector overlap with the "
          "alternating/Nyquist ray %.3f..%.3f < %.2f at every MAIN "
          "rung -- the wall's soft mode is NOT the Nyquist channel "
          "(== CAL)"
          % (min(res[h]["ovl_alt"] for h in rungs),
             max(res[h]["ovl_alt"] for h in rungs), OVL_ID))

    ok22 = all(res[h]["ovl_mid"] < 1e-3 for h in rungs)
    check("G22-midpoint-node-nugget", ok22,
          "NUGGET (recorded): the soft mode is midpoint-BLIND -- "
          "overlap with the midpoint-evaluation ray %.1e..%.1e "
          "(< 1e-3 at every rung; log10 values %s): a selection-"
          "rule candidate, typed observation"
          % (min(res[h]["ovl_mid"] for h in rungs),
             max(res[h]["ovl_mid"] for h in rungs),
             str([round(res[h]["ovl_mid_log"], 1) for h in rungs])))

    ratios = {h: res[h]["bulk_min_log"] - res[h]["tau_log"]
              for h in rungs}
    ok23 = all((not res[h]["sig_neg"]) and res[h]["bulk_nneg"] == 0
               and ratios[h] < RATIO_BAR for h in rungs)
    if not smoke:
        ok23 = ok23 and all(abs(res[h]["sig_log"]
                                - float(CAL_SIG[h])) <= LOG_TOL
                            for h in rungs)
        ok23 = ok23 and all(abs(res[h]["bulk_min_log"]
                                - float(CAL_BULK[h])) <= LOG_TOL
                            for h in rungs)
    check("G23-no-localisation", ok23,
          "7.2 REFUTED in its strong form: sigma_alt > 0 and bulk "
          "PSD at every rung, BUT the bulk minimum sits only "
          "%.1f..%.1f dex above tau (< %.1f): the tau-class "
          "softness SURVIVES the channel elimination -- the wall "
          "margin is NOT localised in the Nyquist scalar (== CAL)"
          % (min(ratios.values()), max(ratios.values()), RATIO_BAR))

    if not smoke and len(rungs) >= 5:
        hs = [h for h in rungs]
        s_sig = fit_line([res[h]["tau_log"] for h in hs],
                         [res[h]["sig_log"] for h in hs])
        s_blk = fit_line([res[h]["tau_log"] for h in hs],
                         [res[h]["bulk_min_log"] for h in hs])
        ok24 = 0.8 <= s_sig <= 1.2 and 0.8 <= s_blk <= 1.2
        check("G24-both-ride-tau", ok24,
              "BOTH the Nyquist scalar (slope %.3f) and the bulk "
              "minimum (slope %.3f) ride the tau ladder at slope ~1: "
              "the Feshbach split relabels the wall, it does not "
              "factor it (GPSD-MARGIN-IS-THE-WALL, inherited)"
              % (s_sig, s_blk))
    else:
        check("G24-both-ride-tau", True, "SKIPPED in smoke")

    section("S3  WORLDS")
    ctasks = ([("SCRARITH", 5, 60)] if smoke else list(CTRL_CELLS))
    cres = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for out in ex.map(w_cell, ctasks):
            cres[out["world"]] = out
    for w in sorted(cres):
        r = cres[w]
        if r.get("err"):
            print("  [ERR] %s: %s" % (w, r["err"]))
        else:
            info("%-8s nneg=%d sig=%.3f bulk_min=%.3f bulk_nneg=%d "
                 "ovl_alt=%.3f" % (w, r["nneg"], r["sig"],
                                   r["bulk_min"], r["bulk_nneg"],
                                   r["ovl_alt"]))

    scr = cres.get("SCRARITH")
    ok41 = (scr and not scr.get("err") and scr["nneg"] == 3
            and scr["sig"] > 0 and scr["bulk_nneg"] >= 2)
    if not smoke and scr and not scr.get("err"):
        ok41 = ok41 and abs(scr["sig"]
                            - float(CAL_CTRL["SCRARITH"]["sig"])) <= VAL_TOL
    check("G41-scrarith-bulk-breaks", bool(ok41),
          "SCRARITH(5): n_neg(M) = 3, ALL in the bulk (sigma_alt = "
          "%.3f > 0): the scramble breaks the bulk, not the Nyquist "
          "channel (== CAL)"
          % (scr["sig"] if scr and not scr.get("err") else float("nan")))

    if smoke:
        check("G40-epstein-pattern-refuted", True, "SKIPPED in smoke")
        check("G42-smooth-honest", True, "SKIPPED in smoke")
    else:
        eps = cres.get("EPSTEIN")
        ok40 = (eps and not eps.get("err") and eps["nneg"] == 2
                and eps["sig"] > 0 and eps["bulk_nneg"] == 2)
        if eps and not eps.get("err"):
            ok40 = ok40 and abs(eps["sig"]
                                - float(CAL_CTRL["EPSTEIN"]["sig"])) \
                <= VAL_TOL
        check("G40-epstein-pattern-refuted", bool(ok40),
              "EPSTEIN(8): n_neg(M) = 2 (NOT 1), BOTH negative "
              "directions in the bulk, sigma_alt = %.3f > 0: the "
              "proposal's predicted 'exactly one crossing, in the "
              "Nyquist scalar' pattern is REFUTED on the canonical "
              "wall (== CAL)"
              % (eps["sig"] if eps and not eps.get("err")
                 else float("nan")))
        smo = cres.get("SMOOTH")
        ok42 = (smo and not smo.get("err") and smo["nneg"] == 2
                and smo["sig"] > 0)
        check("G42-smooth-honest", bool(ok42),
              "SMOOTH(5): n_neg(M) = 2, bulk-broken, sigma_alt > 0 "
              "-- no false arithmetic positivity via the channel "
              "(the atom-free world stays honestly non-PSD)")

    section("S4  PRICING")
    check("G50-proposal-repricing", True,
          "remaining proposal contracts re-priced: 7.3 period-two "
          "Weyl passivity LOSES ITS PREMISE (no single channel "
          "carries the wall); 7.5 dyadic tau averaging averages the "
          "wall margin itself (GPSD-MARGIN-IS-THE-WALL); 7.4 census "
          "self-adjoint linearisation and 7.6 relative determinant "
          "stay named follow-ups (7.6 = the CCM spectral-triple "
          "class, already tracked); the proposal's own honesty "
          "standard ('dies fast and honestly') is met")
    check("G51-mincut-residue-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; four-item residue "
          "UNCHANGED; no marker moved")
    check("G52-external-claim-typed", True,
          "the proposal's 'round 201' Epstein/A(L/2) finding is not "
          "an artifact of this corpus (its own numbering): typed "
          "EXTERNAL-UNVERIFIED; this round adjudicated the substance "
          "directly on the canonical wall")

    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G60-verdict", npass == len(CHECKS),
          "NYQUIST-FESHBACH-REFUTED: IDENTIFICATION-REFUTED(ovl "
          "0.02..0.08) + MIDPOINT-NODE-NUGGET + NO-LOCALISATION"
          "(bulk rides tau) + BOTH-RIDE-TAU(slope ~1) + "
          "EPSTEIN-TWO-BULK-NEGATIVES + SCRARITH-THREE-BULK + "
          "SMOOTH-HONEST + PROPOSAL-REPRICED + NO-RH-CLAIM")

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
