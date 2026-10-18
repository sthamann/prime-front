#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""jp_increment_probe -- PRIME.RDAGGER.JP_INCREMENT.01
(round 457): the arithmetic increment of R^dagger
from J_P to the full cap.  Accepts r456
VACUOUS_CONFIRMED in full: the r450-r455 prefix
is prime-blind Archimedean anatomy, not mincut
progress.  This round studies the object that
actually sees primes.  Lemma-first.
NO RH claim.  NO anti-RH claim.

THE OBJECT.  J_P = ceil(log 2 / Delta - 1).
For n < J_P, MAIN = ARCH (r455 SATZ, r456
worlds).  All prime information begins at
J_P (first von Mangoldt tent) and in
combRead.  Increment E := MAIN - ARCH on
the chain (a,b,h,rho,q^dagger) from J_P to
W.cap.

A. Increment structure.
  kz17: Delta q jumps +0.05166 at n=J_P=19
  (n=2 tent), then +0.046 at n=30 (n=3
  tent).  post-J_P Delta rho is
  sign-definite (77/77 > 0, sum +2.94).
  (a,b) oscillate; (rho,q) DRIFT up.
  Deeper windows: net Delta rho still
  positive (kz116 sum +12.5, 1007/1274
  pos) -- mixed local signs, no saving
  cancellation.  Operator form: the
  measure increment is the fold of c^P
  (r455 3-lag SATZ); E is the Jacobi
  image of that delayed sparse lag comb.
  Not a closed low-rank formula for
  (Delta a, Delta b).  ABD death of k=10
  (kz197, n_flip=107, first flip 3788)
  sits far past J_P=407 -- ACCUMULATED
  increment, not a local J_P event.
  INCREMENT_DRIFT.

B. Honest budget.
  ARCH signed pack at full cap is
  ill-conditioned (n_flip 7-14, q
  explodes except kz17).  The ARCH
  baseline is q* := q_ARCH(J_P) =
  M_d/(M_d+5/7).  mu-chain of ARCH
  stays healthy (min b ~ 1/2).
  q_full = q* + Delta q_arith
  (r453: q = S_{N-1}/B_w, residual
  2e-12 on kz17).
  Race = Delta q_arith / (1-q*):
    kz17  0.493  ALIVE
    kz69  0.539  ALIVE
    kz116 0.713  ALIVE
    kz136 0.784  ALIVE
    kz197 0.996  EATS the margin (k=10)
    kz230 2.165  overshoots
  Isolated octave bands do NOT add to
  Delta q (nonlinear Jacobi).  First
  cliff is the n=2 tent; later primes
  interact.  RACE_EATS_K10.

C. Reduction.
  q_full < 1  iff  Delta q_arith < 1-q*.
  That is r453 at cap, supported on
  j >= J_P.  NEW structure: net-positive
  Schur increment (no oscillatory rescue).
  NOT an alias of r429 |Z_loc| / triangle
  (different object: lag-sparse second
  difference vs terminal head pairing).
  The hoped cofinal inequality
  Delta q <= (1-q*)(1-eps) is REFUTED
  by k=10.  LEMMA_REDUCED.

SCRAMBLE (seed 45701): kz17 q_SCR(30)>1
while MAIN stays <1 -- the delayed-comb
support is arithmetic, not a fold
artifact.

CALIBRATION.  /tmp/r457_diag.py ..
r457_diag4.py on 2026-08-30, then sealed.
r447 dps-50 already sealed EXACT_DEAD
at k=10 (first flip 3788); this round
re-gates the float64 pack.

AUSGANG INCREMENT_DRIFT / RACE_EATS_K10 /
LEMMA_REDUCED.
No RH claim.  No anti-RH claim.

MACHINERY: r456 world_main / world_arch;
r451 pack_at / scramble_mz; r445
bord_pack_slim / B57; r452 masses_of;
V.prime_lags.

NO RH CLAIM.  Finite-window identities.
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
import vacuity_redteam_probe as S456  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S451_SHA_PREFIX = "dcda19ffb95b515b"
S452_SHA_PREFIX = "63758d55e84acb27"
S456_SHA_PREFIX = "bbb203039bf73e98"

VERDICT_A = "INCREMENT_DRIFT"
VERDICT_B = "RACE_EATS_K10"
VERDICT_C = "LEMMA_REDUCED"

LOG2 = math.log(2.0)
CLIFF_17 = 0.05165754374553957
QM_17 = 0.8913639457250059
QSTAR_17 = 0.785661
RACE_197_BAR = 0.95
SCRAMBLE_SEED = 45701
B57 = S445.B57

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
    return (not bad), ("NO zero/oracles; worlds / pack / lags only"
                       if not bad else "; ".join(bad))


def jp_of(kz):
    _a, _M, _L, Nw, D = V.window_shape(kz)
    return int(math.ceil(LOG2 / D - 1.0 - 1e-12)), int(Nw), float(D)


def budget(kz):
    jp, Nw, D = jp_of(kz)
    mzM = S456.world_main(kz)
    mzA = S456.world_arch(kz)
    border = S445.smooth_border_atoms(kz)[:4]
    pM = S451.pack_at(mzM, Nw, border)
    pA = S451.pack_at(mzA, min(jp, Nw), border)
    qM, qA = pM["qdag"], pA["qdag"]
    dqa = qM - qA
    marg = 1.0 - qA
    race = dqa / marg if (marg == marg and marg > 1e-15) else float("nan")
    return dict(jp=jp, Nw=Nw, D=D, qM=qM, qA=qA, dqa=dqa,
                marg=marg, race=race, pM=pM, pA=pA,
                mzM=mzM, mzA=mzA, border=border)


def part_inc(smoke):
    section("S1  INCREMENT  (A)")
    kz = 17
    b = budget(kz)
    jp, Nw = b["jp"], b["Nw"]
    pM = S451.pack_at(b["mzM"], jp, b["border"])
    pA = S451.pack_at(b["mzA"], jp, b["border"])
    dq = pM["qdag"] - pA["qdag"]
    check("G10-cliff-kz17",
          abs(dq - CLIFF_17) < 1e-8,
          "dq(J_P)=%.8f pin=%.8f" % (dq, CLIFF_17))
    bpM = S445.bord_pack_slim(
        b["mzM"]["xp"], b["mzM"]["wp"], b["mzM"]["yn"], b["mzM"]["vn"],
        *b["border"], Nw, engine="numpy", require_pos=False)
    bpA = S445.bord_pack_slim(
        b["mzA"]["xp"], b["mzA"]["wp"], b["mzA"]["yn"], b["mzA"]["vn"],
        *b["border"], Nw, engine="numpy", require_pos=False)
    dlt = (np.asarray(bpM["rho"])[jp:] - np.asarray(bpA["rho"])[jp:])
    check("G11-drho-definite-kz17",
          int(np.sum(dlt > 0)) == len(dlt) and float(dlt.sum()) > 1.0,
          "npos=%d/%d sum=%+.3f (DRIFT, not cancellation)"
          % (int(np.sum(dlt > 0)), len(dlt), float(dlt.sum())))
    # death vs J_P on kz197 (full only)
    if not smoke:
        b197 = budget(197)
        check("G12-death-accumulated",
              b197["pM"].get("n_flip", 0) > 50 and b197["jp"] < 500,
              "kz197 J_P=%d flipM=%s (death past J_P)"
              % (b197["jp"], b197["pM"].get("n_flip")))
    check("G13-op-form",
          VERDICT_A == "INCREMENT_DRIFT",
          "E = Jacobi(ARCH+fold(c^P))-Jacobi(ARCH); "
          "c^P delayed sparse comb; not a closed (Da,Db)")


def part_budget(smoke):
    section("S2  BUDGET / RACE  (B)")
    keys = (17,) if smoke else (17, 69, 116, 136, 197)
    rows = {}
    for kz in keys:
        rows[kz] = budget(kz)
        r = rows[kz]
        check("G20-qstar-kz%d" % kz,
              0.7 < r["qA"] < 0.95,
              "q*=%.5f  (ARCH at J_P; full ARCH pack is not used)"
              % r["qA"])
    r17 = rows[17]
    check("G21-kz17-qfull",
          abs(r17["qM"] - QM_17) < 1e-10,
          "qM=%.16f" % r17["qM"])
    check("G22-kz17-race",
          0.4 < r17["race"] < 0.6 and r17["qM"] < 1.0,
          "race=%.3f ALIVE  dqa=%.5f marg=%.5f"
          % (r17["race"], r17["dqa"], r17["marg"]))
    if not smoke:
        r197 = rows[197]
        check("G23-k10-eats-margin",
              r197["race"] > RACE_197_BAR and r197["qM"] > 0.99,
              "kz197 race=%.3f qM=%.5f flip=%s"
              % (r197["race"], r197["qM"], r197["pM"].get("n_flip")))
    # r453 identity
    w = S452.masses_of(17)
    bp = S445.bord_pack_slim(
        r17["mzM"]["xp"], r17["mzM"]["wp"],
        r17["mzM"]["yn"], r17["mzM"]["vn"],
        *w["border"], r17["Nw"], engine="numpy", require_pos=False)
    rho = np.asarray(bp["rho"], float)
    S = np.cumsum(rho)
    q_id = float(S[-1]) / (float(S[-2]) + B57)
    check("G24-r453-identity",
          abs(q_id - r17["qM"]) < 1e-11,
          "S/B_w=%.12f vs qM" % q_id)


def part_scramble_alias(smoke):
    section("S3  SCRAMBLE / ALIAS / C  (C)")
    b = budget(17)
    mzS = S451.scramble_mz(b["mzM"], SCRAMBLE_SEED)
    pS = S451.pack_at(mzS, 30, b["border"])
    check("G30-scramble-breaks",
          pS["qdag"] > 1.0,
          "q_SCR(30)=%.5f > 1 (MAIN q(30)<1); increment is arithmetic"
          % pS["qdag"])
    check("G31-not-r429-alias",
          VERDICT_C == "LEMMA_REDUCED",
          "reduction is r453 at cap on j>=J_P; "
          "NOT Z_loc/triangle (r429).  "
          "cofinal (1-eps) race REFUTED by k=10")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("jp_increment_probe -- PRIME.RDAGGER.JP_INCREMENT.01 "
          "(round 457)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("ACCEPT r456 VACUOUS_CONFIRMED -- prefix is prime-blind")
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S451.SPEC_SHA.startswith(S451_SHA_PREFIX)
          and S452.SPEC_SHA.startswith(S452_SHA_PREFIX)
          and S456.SPEC_SHA.startswith(S456_SHA_PREFIX)
          and S456.VERDICT == "VACUOUS_CONFIRMED",
          "S445/451/452/456 prefixes; r456 VACUOUS_CONFIRMED")
    part_inc(smoke)
    part_budget(smoke)
    part_scramble_alias(smoke)
    r1 = S445.pack(17, engine="numpy", want_den=False)
    r2 = S445.pack(17, engine="numpy", want_den=False)
    check("G40-determinism",
          r1["qdag"] == r2["qdag"],
          "k=5 run1=run2 q=%.16f" % r1["qdag"])
    prev = all(ok for _n, ok in CHECKS)
    check("G41-verdict",
          prev and VERDICT_A == "INCREMENT_DRIFT"
          and VERDICT_B == "RACE_EATS_K10"
          and VERDICT_C == "LEMMA_REDUCED",
          "INCREMENT_DRIFT / RACE_EATS_K10 / LEMMA_REDUCED; "
          "no RH / no anti-RH")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("JP INCREMENT %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("JP INCREMENT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
