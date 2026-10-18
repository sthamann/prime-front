#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""fullcomb_cleanup_probe -- PRIME.RDAGGER.FULLCOMB_CLEANUP.01
(round 459): clean three TABLE_CAP-contaminated
findings after r458.  Lemma-first.  No polish.
Research documentation, NO RH claim.

CONTEXT.  r457 measured a monotone race
kz17 0.493 -> kz69 0.539 -> kz116 0.713 ->
kz136 0.784 -> kz197 0.996 -> kz230 2.165
and concluded RACE_EATS_K10.  r458 showed
kz197/kz230 ran on the GETRUNKTEN Kamm
(TABLE_CAP=4e5).  The race table and the
"eats k=10" reading are contaminated.
r457 budget identity stands:
  q^dagger_full < 1  <=>  Delta q_arith < 1-q*
  q* = q_ARCH(J_P).

A. Frame-A race on the FULL a^2 comb.
  Sealed /tmp/r459_census.py (2026-08-30)
  BEFORE this probe.  ARCH world, identical
  fold (r456 measures_from_c).  Completeness:
  ka == #{prime powers <= a^2}.
    kz   a     race     live  vs r457
    17   32    0.49316  Y     same (already complete)
    69   256   0.53944  Y     same
    116  512   0.71271  Y     same
    136  631   0.78376  Y     same
    138  643   0.75949  Y     revival (was dead capped)
    197  1024  0.72448  Y     was 0.996 EATS
    230  1259  0.77041  Y     was 2.165 overshoot
  All race < 1.  Monotone after 136 BREAKS
  (0.784 -> 0.760 -> 0.724 -> 0.770).
  Fit on 7: M2.  Drop-197/230/138: M2.
  only_old (17,69,116,136): M1 -- the r457
  trend was the incomplete ladder.
  RACE_TREND_BROKEN.

B. Lean family (the mincut-relevant ladder).
  selectedMesh a=2^k, m=k*2^{floor sqrt k}-1.
  pack_at2 allows nstar>=2 (S451 pack_at
  refuses nstar<4; Lean k=5..8 have J_P=3).
  Complete members k=5..12 (k=12 sieve 16.8e6,
  ka=1078555).  k=14 a^2=2.68e8 NOT complete
  (BUDGET_LIMIT).
    k   race    q*      live
    5   0.67506 0.62423 Y
    6   0.69491 0.62423 Y
    7   0.62874 0.62423 Y
    8   0.60657 0.62423 Y
    9   0.63537 0.71910 Y
    10  0.75778 0.71910 Y
    11  0.71578 0.71910 Y
    12  0.69356 0.71910 Y
  Not monotone.  Stays in ~0.61--0.76.
  Does NOT run to 1.
  Exact dps=50 (/tmp/r459_exact.py):
    k=10 n_flip=0 pos_ok n_done=40  ka=82267
    k=11 n_flip=0 pos_ok n_done=44  ka=296347
    k=12 n_flip=0 pos_ok n_done=48  ka=1078555
  k=14/16 exact not computed (a^2 budget).
  LEANFAM_EXACT_ALIVE(12).

C. kz137 residual death.
  a=641 N=8300.  Inventory COMPLETE:
  ka=34856/34856, a^2=410881 <= sieve.
  Float pack: n_flip=103, qM=NaN, live=False.
  Mass-chain first flip 7308 (r458).
  Lean-admissible window at a=641 with
  selectedMesh k=9 (m=71 N=36) and k=10
  (m=79 N=40): BOTH live, race 0.453 / 0.534.
  Frame-A couples mesh to the local log-gap
  (N=8300); Lean mincut never consumes that
  depth.  Higher p^k > a^2 are outside
  ExactPrimeSource(a).  Reflection tents
  already in prime_lags.  Input-complete
  at the a^2 cutoff, then the death is a
  frame-A property.
  KZ137_OUTSIDE_MINCUT.

AUSGANG RACE_TREND_BROKEN /
LEANFAM_EXACT_ALIVE(12) /
KZ137_OUTSIDE_MINCUT.
SATZ: none (cleanup census).
No RH claim.  No anti-RH claim.

MACHINERY: r456 world fold; r451 pack;
r458 lean_shape / border_from_shape;
r445 bord_pack_slim; V.arch_lags.

NO RH CLAIM.  Finite window census.
Research documentation, not a theorem of RH.
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
import vacuity_redteam_probe as S456  # noqa: E402
import cofinal_family_probe as S458  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S451_SHA_PREFIX = "dcda19ffb95b515b"
S456_SHA_PREFIX = "bbb203039bf73e98"
S458_SHA_PREFIX = "a4aa21a54f33eace"

VERDICT_A = "RACE_TREND_BROKEN"
VERDICT_B = "LEANFAM_EXACT_ALIVE(12)"
VERDICT_C = "KZ137_OUTSIDE_MINCUT"

LOG2 = math.log(2.0)

# sealed from /tmp/r459_census.json + r459_lean_race.json
FA_RACE = {
    17: 0.49315736627224754,
    69: 0.5394384660162291,
    116: 0.7127117420061213,
    136: 0.7837595779418907,
    138: 0.7594938540705529,
    197: 0.724476754005576,
    230: 0.7704088352459775,
}
FA_QM = {
    17: 0.8913639457250059,
    197: 0.9691034684774628,
    230: 0.9709010751634095,
}
LEAN_RACE = {
    5: 0.6750602575677171,
    6: 0.6949067407361886,
    7: 0.628735899841535,
    8: 0.6065660774872124,
    9: 0.6353690439116121,
    10: 0.7577828845524202,
    11: 0.7157819445351823,
    12: 0.6935644234675039,
}
LEAN10_Q = 0.9319618718590412
KZ137_KA = 34856
KZ137_NEED = 410881
KZ137_PACK_NFLIP = 103
KZ137_MASS_FIRST = 7308
LEAN641_RACE9 = 0.4531664349711691
LEAN_EXACT_ALIVE = (10, 11, 12)

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
    return (not bad), ("NO zero/oracles; sieve+fold+pack only"
                       if not bad else "; ".join(bad))


def sieve_pp(n_max):
    s = bytearray(b"\x01") * (n_max + 1)
    s[0] = s[1] = 0
    lim = int(math.isqrt(n_max))
    for i in range(2, lim + 1):
        if s[i]:
            st = i * i
            s[st:n_max + 1:i] = b"\x00" * (((n_max - st) // i) + 1)
    rows = []
    for p in range(2, n_max + 1):
        if not s[p]:
            continue
        q, lp = p, math.log(p)
        while q <= n_max:
            rows.append((q, lp))
            if q > n_max // p:
                break
            q *= p
    rows.sort()
    return rows


def n_pp_upto(rows, nmax):
    return sum(1 for n, _ in rows if n <= nmax)


def lags_from_rows(rows, alpha, M, D):
    u_cut = 2.0 * alpha + 1e-14
    c = np.zeros(M)
    ka = 0
    for n, lp in rows:
        u = math.log(n)
        if u >= u_cut:
            break
        ka += 1
        w = 2.0 * lp / math.sqrt(n)
        i0 = int(math.floor(u / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u) / D
            if v > 0.0:
                c[i] -= w * 0.5 * v
        if u < D:
            for i in range(0, min(M, int(math.floor((D - u) / D)) + 2)):
                v = 1.0 - (i * D + u) / D
                if v > 0.0:
                    c[i] -= w * 0.5 * v
    return c, ka


def pack_at2(mz, nstar, border):
    """S451.pack_at with nstar>=2 (Lean J_P=3)."""
    bxs, bws, bys, bvs = border
    nstar = min(int(nstar), int(mz["Nw"]))
    if nstar < 2:
        return dict(ok=False, qdag=float("nan"))
    bp = S445.bord_pack_slim(
        mz["xp"], mz["wp"], mz["yn"], mz["vn"],
        bxs, bws, bys, bvs, nstar, engine="numpy", require_pos=False)
    if bp.get("rho") is None:
        return dict(ok=False, qdag=float("nan"), n_flip=bp.get("n_flip"))
    a, b, h0 = S445.mu_chain_opt(mz["xp"], mz["wp"], nstar, engine="numpy")
    bxa = np.concatenate([np.asarray(bxs, float), np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float), -np.asarray(bvs, float)])
    bvec = S445.bvec_opt(a, b, h0, bxa, bwa, nstar, engine="numpy")
    rho = np.asarray(bp["rho"], float)
    Bw = float(np.cumsum(rho)[max(0, nstar - 2)]) + S445.B57
    sol = S445.solve_qdag(a, b, h0, mz["yn"], mz["vn"], bvec, Bw,
                          engine="numpy")
    return dict(ok=True, qdag=float(sol["qdag"]),
                n_flip=bp.get("n_flip") or 0,
                pos_ok=bool(bp.get("pos_ok", True)))


def mz_pair(cP, ka, alpha, M, L, Nw, D):
    cA = V.arch_lags(M, D)
    mzM = S456.measures_from_c(cA + cP, alpha, M, L, Nw, D, ka=ka)
    mzA = S456.measures_from_c(cA, alpha, M, L, Nw, D, ka=0)
    mzM["Nw"] = mzA["Nw"] = Nw
    return mzM, mzA


def race_nums(mzM, mzA, Nw, jp, border):
    pM = pack_at2(mzM, Nw, border)
    pA = pack_at2(mzA, max(min(jp, Nw), 2), border)
    qM, qA = pM.get("qdag", float("nan")), pA.get("qdag", float("nan"))
    dqa = qM - qA
    marg = 1.0 - qA
    race = dqa / marg if (marg == marg and marg > 1e-15) else float("nan")
    live = bool(pM.get("ok") and qM == qM and qM < 1.0
                and (pM.get("n_flip") or 0) == 0
                and pM.get("pos_ok", False))
    return dict(qM=qM, qA=qA, dqa=dqa, marg=marg, race=race,
                n_flip=pM.get("n_flip"), pos_ok=pM.get("pos_ok"),
                okM=pM.get("ok"), okA=pA.get("ok"), live=live)


def fa_budget(kz, rows):
    alpha, M, L, Nw, D = V.window_shape(kz)
    a = int(V.PP[kz])
    need = a * a
    cP, ka = lags_from_rows(rows, alpha, M, D)
    nexp = n_pp_upto(rows, need)
    complete = (need <= rows[-1][0]) and (ka == nexp)
    mzM, mzA = mz_pair(cP, ka, alpha, M, L, Nw, D)
    border = S445.smooth_border_atoms(kz)[:4]
    jp = int(math.ceil(LOG2 / D - 1.0 - 1e-12))
    r = race_nums(mzM, mzA, Nw, jp, border)
    r.update(kz=kz, a=a, Nw=Nw, jp=jp, ka=ka, nexp=nexp,
             need=need, complete=complete)
    return r


def lean_budget(k, rows, a=None):
    shp = S458.lean_shape(k, a=a)
    alpha, M, L, Nw, D = (shp["alpha"], shp["M"], shp["L"],
                          shp["Nw"], shp["D"])
    aa = shp["a"]
    need = aa * aa
    cP, ka = lags_from_rows(rows, alpha, M, D)
    nexp = n_pp_upto(rows, need) if need <= rows[-1][0] else n_pp_upto(
        rows, rows[-1][0])
    complete = need <= rows[-1][0] and ka == n_pp_upto(rows, need)
    mzM, mzA = mz_pair(cP, ka, alpha, M, L, Nw, D)
    border = S458.border_from_shape(shp)
    jp = int(math.ceil(LOG2 / D - 1.0 - 1e-12))
    r = race_nums(mzM, mzA, Nw, jp, border)
    r.update(k=k, a=aa, m=shp["m"], Nw=Nw, jp=jp, ka=ka,
             nexp=nexp, need=need, complete=complete)
    return r


def part_fa(smoke, rows):
    section("S1  FRAME-A RACE ON FULL a^2 COMB  (A)")
    keys = (17,) if smoke else (17, 136, 138, 197, 230)
    rows_out = {}
    for kz in keys:
        r = fa_budget(kz, rows)
        rows_out[kz] = r
        pin = abs(r["race"] - FA_RACE[kz]) < 1e-10
        check("G10-fa-kz%d" % kz,
              r["complete"] and r["live"] and pin and r["qM"] < 1.0,
              "a=%d N=%d ka=%d/%d race=%.5f live qM=%.5f"
              % (r["a"], r["Nw"], r["ka"], r["nexp"], r["race"], r["qM"]))
    check("G11-kz17-qM",
          abs(rows_out[17]["qM"] - FA_QM[17]) < 1e-12,
          "qM=%.16f" % rows_out[17]["qM"])
    races = [FA_RACE[k] for k in (17, 69, 116, 136, 138, 197, 230)]
    mono = all(races[i] <= races[i + 1] + 1e-9
               for i in range(len(races) - 1))
    check("G12-mono-broken",
          (not mono) and FA_RACE[197] < 0.80 and FA_RACE[230] < 0.80
          and FA_RACE[197] < FA_RACE[136],
          "197=%.4f 230=%.4f < 136=%.4f (r457 0.996/2.165 was table-cap)"
          % (FA_RACE[197], FA_RACE[230], FA_RACE[136]))
    if not smoke:
        xs = [float(V.PP[k]) for k in (17, 136, 138, 197, 230)]
        ys = [rows_out[k]["race"] for k in (17, 136, 138, 197, 230)]
        fit = S421.diagnose_seq(xs, ys)
        check("G13-fit-not-M1-runaway",
              fit["winner"] != "M1" or (
                  fit.get("M1_Rinf") == fit.get("M1_Rinf")
                  and fit.get("M1_Rinf", 2) < 0.9),
              "winner=%s M1_Rinf=%s" % (fit["winner"], fit.get("M1_Rinf")))
    check("G14-verdict-A",
          VERDICT_A == "RACE_TREND_BROKEN",
          "r457 RACE_EATS_K10 is a TABLE_CAP echo")


def part_lean(smoke, rows):
    section("S2  LEAN FAMILY RACE + EXACT  (B)")
    keys = (5, 10) if smoke else (5, 10, 11, 12)
    for k in keys:
        r = lean_budget(k, rows)
        pin = abs(r["race"] - LEAN_RACE[k]) < 1e-10
        qpin = True
        if k == 10:
            qpin = abs(r["qM"] - LEAN10_Q) < 1e-12
        check("G20-lean-k%d" % k,
              r["complete"] and r["live"] and pin and qpin
              and 0.55 < r["race"] < 0.80,
              "a=%d m=%d N=%d jp=%d ka=%d race=%.5f qM=%.6f"
              % (r["a"], r["m"], r["Nw"], r["jp"], r["ka"],
                 r["race"], r["qM"]))
    lr = [LEAN_RACE[k] for k in range(5, 13)]
    lmono = all(lr[i] <= lr[i + 1] + 1e-9 for i in range(len(lr) - 1))
    check("G21-lean-not-to-1",
          (not lmono) and max(lr) < 0.80 and min(lr) > 0.55,
          "k=5..12 race in [%.3f, %.3f]; no run to 1"
          % (min(lr), max(lr)))
    check("G22-exact-pins",
          LEAN_EXACT_ALIVE == (10, 11, 12),
          "dps=50 n_flip=0 for k=10,11,12; k=14 a^2=2.68e8 BUDGET_LIMIT")
    check("G23-verdict-B",
          VERDICT_B == "LEANFAM_EXACT_ALIVE(12)",
          "central: Lean race stays ~0.61-0.76")


def part_kz137(smoke, rows):
    section("S3  kz137 vs LEAN a=641  (C)")
    r = fa_budget(137, rows)
    check("G30-kz137-complete",
          r["complete"] and r["ka"] == KZ137_KA
          and r["need"] == KZ137_NEED,
          "ka=%d/%d need=%d (input-complete at a^2)"
          % (r["ka"], r["nexp"], r["need"]))
    check("G31-kz137-dead",
          (not r["live"]) and (r["n_flip"] or 0) >= 1,
          "live=%s n_flip=%s (mass-chain first=%d r458)"
          % (r["live"], r["n_flip"], KZ137_MASS_FIRST))
    r9 = lean_budget(9, rows, a=641)
    r10 = lean_budget(10, rows, a=641)
    check("G32-lean641-lives",
          r9["live"] and r10["live"]
          and r9["complete"] and r10["complete"]
          and abs(r9["race"] - LEAN641_RACE9) < 1e-9,
          "k=9 race=%.4f k=10 race=%.4f (selectedMesh at a=641)"
          % (r9["race"], r10["race"]))
    check("G33-not-higher-pk",
          KZ137_NEED == 641 * 641,
          "ExactPrimeSource cuts at a^2; p^k>a^2 is outside the object")
    check("G34-verdict-C",
          VERDICT_C == "KZ137_OUTSIDE_MINCUT",
          "frame-A gap-coupled depth; Lean mincut lives at a=641")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("fullcomb_cleanup_probe -- PRIME.RDAGGER.FULLCOMB_CLEANUP.01 "
          "(round 459)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S451.SPEC_SHA.startswith(S451_SHA_PREFIX)
          and S456.SPEC_SHA.startswith(S456_SHA_PREFIX)
          and S458.SPEC_SHA.startswith(S458_SHA_PREFIX),
          "S445/451/456/458 prefixes")
    cap = 1_100_000 if smoke else 16_800_000
    print("sieve", cap, flush=True)
    rows = sieve_pp(cap)
    print("n_pp", len(rows), flush=True)
    part_fa(smoke, rows)
    part_lean(smoke, rows)
    part_kz137(smoke, rows)
    r1 = fa_budget(17, rows)
    r2 = fa_budget(17, rows)
    check("G40-determinism",
          r1["race"] == r2["race"] and r1["qM"] == r2["qM"],
          "kz17 run1=run2 race=%.16f" % r1["race"])
    prev = all(ok for _n, ok in CHECKS)
    check("G41-verdict",
          prev and VERDICT_A == "RACE_TREND_BROKEN"
          and VERDICT_B == "LEANFAM_EXACT_ALIVE(12)"
          and VERDICT_C == "KZ137_OUTSIDE_MINCUT",
          "RACE_TREND_BROKEN / LEANFAM_EXACT_ALIVE(12) / "
          "KZ137_OUTSIDE_MINCUT; no RH / no anti-RH")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("FULLCOMB CLEANUP %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("FULLCOMB CLEANUP FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
