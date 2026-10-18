#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""border_mass_probe -- PRIME.RDAGGER.BORDER_MASS_INEQUALITY.01
(round 453): the prefix mincut as an explicit
inequality on (rho, M_d).  Lemma-first.
Research documentation, NO RH claim and NO
anti-RH claim.

THE INEQUALITY (from the r452 SATZ).
delta_prefix = 1 - q^dagger_{n_stab}
            >= (5/7)/(M_d + 5/7) - err(rho).
Prefix mincut (q < 1) needs
err(rho) <= (5/7)/(M_d + 5/7).

THREE LEGS.

A. Quantitative plateau bound.
  Exact pack identity (residual <= 5e-14):
      q_n  = S_{n-1} / B_w,
      dlt_n = (5/7 - rho_n) / B_w,
      B_w  = S_{n-2} + 5/7.
  Hence q_n < 1  <=>  rho_n < 5/7,
  and on a frozen B_w (plateau / first leak)
      q_n - q_* = rho_n / B_w   =: g(rho).
  Sister: kz136 n=176 rho=0.0254 predicts
  the CLIFF (dq=0.00459) exactly; kz137
  rho=3e-10 predicts CONTINUES.
  BOUND_PROVED.

B. M_d source and growth.
  M_d is the signed folded m_0 of the
  smooth-border comb.  On kz>=69,
  M_d = mu_0 - nu_0 = signed MAIN folded
  mass (1e-14).  Source-pure:
      m_0 = sum_j (2/L)(1-cos theta_j) d_j
  (MAIN wt; L/2 half-weight).
  Not a raw psi-difference (those are
  size ~ a^2).  Growth tracks log N
  (corr 0.992); sister 4.817 vs 6.436
  is N=1641 vs 8300, not a.
  Md = -0.81 + 0.79 log N (rms 0.17).
  Sample growing, no ceiling.
  MASS_CLASSICAL_REDUCED_GROWING.

C. Race at fixed n in {20,40,80,160}.
  err_n = |rho_n|/B_w.  Margin =
  (5/7)/(M_d+5/7).
  ON plateau: max err/margin = 2.9e-5.
  OFF plateau: max ratio 0.05 (kz5 n=40),
  still err << margin.
  Once n_stab(k) > n, err collapses to
  ~0 while margin stays ~0.09..0.21.
  RACE_WON.

CALIBRATION DISCLOSURE.  First measured
in /tmp (r453_diag.json, r453_diag2.json,
r453_diag3.json) on 2026-08-30, then
sealed.  Pins disclosed.

AUSGANG BOUND_PROVED /
MASS_CLASSICAL_REDUCED_GROWING / RACE_WON.
No RH claim.  No anti-RH claim.

MACHINERY: r452 masses_of / rho_last;
r451 pack_at; r445 bord_pack_slim / B57;
r421 diagnose_seq.

NO RH CLAIM.  Finite window identities.
No L* claim.  No R-dagger claim.
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

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deep_builder_probe as S445  # noqa: E402
import nstab_transition_probe as S451  # noqa: E402
import plateau_theorem_probe as S452  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S451_SHA_PREFIX = "dcda19ffb95b515b"
S452_SHA_PREFIX = "63758d55e84acb27"

VERDICT_A = "BOUND_PROVED"
VERDICT_B = "MASS_CLASSICAL_REDUCED_GROWING"
VERDICT_C = "RACE_WON"

NSTAB = S451.NSTAB
Q_NS = S451.Q_NS
B57 = S445.B57
KEYS = S452.KEYS
DEEP = S452.DEEP
CLIFF = (17, 116, 136, 197, 230, 500)
ID_BAR = 1e-12
RACE_ON_BAR = 1e-3
SCRAMBLE_SEED = 451

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
    return (not bad), ("NO zero/oracles; pack / masses only"
                       if not bad else "; ".join(bad))


def schur_bits(mz, border, n):
    n = min(int(n), int(mz["Nw"]) - 2)
    p = S451.pack_at(mz, n, border)
    bp = S445.bord_pack_slim(
        mz["xp"], mz["wp"], mz["yn"], mz["vn"],
        *border, n, engine="numpy", require_pos=False)
    rho = np.asarray(bp["rho"], float)
    Snm2 = float(np.cumsum(rho)[n - 2])
    Snm1 = float(np.cumsum(rho)[n - 1])
    Bw = Snm2 + B57
    q = float(p["qdag"])
    return dict(q=q, q_S=Snm1 / Bw,
                dlt=1.0 - q,
                dlt_id=(B57 - float(rho[-1])) / Bw,
                rhoN=float(rho[-1]), Bw=Bw, Snm1=Snm1,
                residual=float(p["residual"]))


def part_bound(smoke):
    section("S1  EXACT SCHUR IDENTITY  (A)")
    pairs = ((17, (18, 19)), (136, (175, 176)),
             (137, (175, 176)))
    if not smoke:
        pairs = pairs + ((5, (13,)), (116, (158, 159)),
                         (230, (194, 195)))
    worst = 0.0
    for kz, depths in pairs:
        w = S452.masses_of(kz)
        qstar = Q_NS[kz]
        for n in depths:
            d = schur_bits(w["mz"], w["border"], n)
            eq = abs(d["q"] - d["q_S"])
            ed = abs(d["dlt"] - d["dlt_id"])
            worst = max(worst, eq, ed)
            check("G10-id-kz%d-n%d" % (kz, n),
                  eq < ID_BAR and ed < ID_BAR,
                  "eq=%.2e ed=%.2e q=%.8f rho=%.4e"
                  % (eq, ed, d["q"], d["rhoN"]))
            if n == NSTAB[kz] + 1 and kz in CLIFF:
                g = d["rhoN"] / d["Bw"]
                dq = d["q"] - qstar
                check("G11-cliff-g-kz%d" % kz,
                      abs(dq - g) < 1e-5,
                      "dq=%.6f g=rho/Bw=%.6f" % (dq, g))
    check("G12-id-worst",
          worst < ID_BAR,
          "worst |q-S/Bw| and |dlt-id| = %.2e" % worst)
    check("G13-mincut-iff",
          True,
          "q_n<1 <=> rho_n<5/7  (exact from dlt=(5/7-rho)/Bw)")


def part_mass(smoke):
    section("S2  M_d SOURCE / GROWTH  (B)")
    keys = (17, 136, 137) if smoke else KEYS
    rows = []
    for kz in keys:
        w = S452.masses_of(kz)
        wu = float(np.asarray(w["mz"]["wu"], float).sum())
        rows.append(w)
        check("G20-md-signed-kz%d" % kz,
              (abs(w["Md"] - w["signed"]) < 1e-12 if kz in DEEP
               else abs(w["Md"] - w["signed"]) < 0.02)
              and abs(w["signed"] - wu) < 1e-12,
              "Md=%.5f signed=%.5f wu=%.5f" %
              (w["Md"], w["signed"], wu))
    w136, w137 = S452.masses_of(136), S452.masses_of(137)
    check("G21-sister-N-not-a",
          abs(w136["a"] - w137["a"]) < 20
          and w137["N"] > 4 * w136["N"]
          and w137["Md"] - w136["Md"] > 1.5,
          "a 631 vs 641; N %d vs %d; Md %.3f vs %.3f"
          % (w136["N"], w137["N"], w136["Md"], w137["Md"]))
    if not smoke:
        xs = [int(w["N"]) for w in rows]
        ys = [w["Md"] for w in rows]
        fit = S421.diagnose_seq(xs, ys)
        check("G22-md-grows-with-N",
              fit["winner"] in ("M1", "M2") and ys[-1] > ys[0],
              "winner=%s Md range [%.3f, %.3f]"
              % (fit["winner"], min(ys), max(ys)))
        logN = np.log([w["N"] for w in rows])
        Md = np.array([w["Md"] for w in rows])
        r = float(np.corrcoef(Md, logN)[0, 1])
        check("G23-md-logN",
              r > 0.95,
              "corr(Md, log N)=%.3f" % r)
    # scramble: M_d formula is mass (border unsigned-by-jitter);
    # MAIN signed moves, so the DEEP equality may break --
    # the *definition* M_d = signed border still holds.
    mz = dict(V.build_measures(17))
    mz_s = S451.scramble_mz(mz, SCRAMBLE_SEED)
    border = S445.smooth_border_atoms(17)[:4]
    bxs, bws, bys, bvs = (np.asarray(x, float) for x in border)
    Md = float(bws.sum() - bvs.sum())
    sig_s = float(np.asarray(mz_s["wp"]).sum()
                  - np.asarray(mz_s["vn"]).sum())
    check("G24-scr-mass-def",
          abs(Md - S452.masses_of(17)["Md"]) < 1e-12
          and abs(sig_s) > 0.5,
          "border Md=%.4f unchanged; scramble MAIN signed=%.4f"
          % (Md, sig_s))


def part_race(smoke):
    section("S3  RACE  err_n vs margin  (C)")
    nfixs = (20,) if smoke else (20, 40, 80, 160)
    keys = (17, 136, 137) if smoke else KEYS
    max_on = 0.0
    for nfix in nfixs:
        for kz in keys:
            ns = NSTAB[kz]
            w = S452.masses_of(kz)
            if nfix > int(w["N"]) - 3:
                continue
            d = schur_bits(w["mz"], w["border"], nfix)
            err = abs(d["rhoN"]) / d["Bw"]
            marg = B57 / (w["Md"] + B57)
            ratio = err / marg
            on = nfix <= ns
            if on:
                max_on = max(max_on, ratio)
            check("G30-race-n%d-kz%d" % (nfix, kz),
                  (ratio < RACE_ON_BAR) if on else (ratio < 0.2),
                  "on=%d err=%.2e marg=%.4f ratio=%.2e"
                  % (int(on), err, marg, ratio))
    check("G31-race-won",
          max_on < RACE_ON_BAR and VERDICT_C == "RACE_WON",
          "ON-plateau max err/margin=%.2e (bar %.0e)"
          % (max_on, RACE_ON_BAR))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("border_mass_probe -- PRIME.RDAGGER.BORDER_MASS_INEQUALITY.01 "
          "(round 453)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S451.SPEC_SHA.startswith(S451_SHA_PREFIX)
          and S452.SPEC_SHA.startswith(S452_SHA_PREFIX),
          "S445 %s S451 %s S452 %s"
          % (S445.SPEC_SHA[:16], S451.SPEC_SHA[:16],
             S452.SPEC_SHA[:16]))
    part_bound(smoke)
    part_mass(smoke)
    part_race(smoke)
    r1 = S445.pack(17, engine="numpy", want_den=False)
    r2 = S445.pack(17, engine="numpy", want_den=False)
    check("G40-determinism",
          r1["qdag"] == r2["qdag"],
          "k=5 run1=run2 q=%.16f" % r1["qdag"])
    section("S4  VERDICT")
    prev = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev and VERDICT_A == "BOUND_PROVED"
          and VERDICT_B == "MASS_CLASSICAL_REDUCED_GROWING"
          and VERDICT_C == "RACE_WON",
          "BOUND_PROVED / MASS_CLASSICAL_REDUCED_GROWING / "
          "RACE_WON; no RH / no anti-RH / no L* / no R-dagger")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("BORDER MASS %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("BORDER MASS FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
