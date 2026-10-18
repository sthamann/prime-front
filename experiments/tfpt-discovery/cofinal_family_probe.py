#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cofinal_family_probe -- PRIME.RDAGGER.COFINAL_FAMILY.01
(round 458): the frequently-quantifier needs a
cofinally living window family.  The r456
red-team retyped the mincut as the FULL cap
cone; r447/r448 killed the TABLE_CAP=4e5
frame-A 2^k ladder past k=10.  This round
searches the Lean-admissible (a,m) space.
Research documentation, NO RH claim.

OBJECT.  Lean Selected.lean: any sequence of
ExactFold(a_k, m_k) with a_k prime-power,
a_k -> inf, m_k -> inf covers every test
function (selected_covers).  The named
sequence is a_k=2^k, m_k=k*2^{floor sqrt k}-1.
The Python kz raster is a DIFFERENT mesh
(gap-coupled frame-A, TABLE_CAP=4e5).

CALIBRATION DISCLOSURE.  Grid SCAN_KZ sealed
in /tmp/r458_census.py BEFORE the first pack
(2026-08-30).  Full-comb follow-up
(/tmp/r458_fullcomb.py, r458_wall.json,
r458_revive.json) was post-hoc after the
a=631 wall was seen to equal sqrt(TABLE_CAP),
then confirmed on pre-registered dead
windows.  Pins disclosed.

FROZEN FROM /tmp (live re-gated):
  * Capped frame-A scan (76 kz): 55 live,
    21 dead.  max live a=631 (kz136);
    min dead a=641 (kz137).  Zero exceptions.
    Holdout (every 4th, 19 windows):
    predictor a<=631 is 19/19.  N<=1641
    is only 14/19 (kz69 N=5690 lives).
  * Lean-native (a=2^k, selectedMesh)
    k=5..12,14,16: ALL cap-live
    (q^dagger in [0.85,0.95], n_flip=0).
    k=10 q=0.9319618718590412.
  * Full comb to a^2 (table 1.1e6..1.7e6):
    Lean k=10 q IDENTICAL (ka 34034->82267).
    Frame-A kz197 (2^10) REVIVES
    (capped first=3788 -> full live).
    kz138,139,230 revive.  kz137 stays
    dead (first 7308, N=8300).
  * Exact dps=50 full-comb kz230:
    n_flip=0, pos_ok, n_done=2012
    (r448 EXACT_DEAD was table-truncated).
  * r329 EXT3: F_A/cubic violations on
    fresh small-gap anchors; ABD/q^dagger
    was not the object.  Those EXT3 kz
    are capped-ABD-live (a<=601).

AUSGANG FAMILY_CANDIDATE / TABLE_CAP_ARTEFACT /
RESIDUAL_DEEP_DEATH (kz137).
SATZ: none (infra census).
No RH claim.  No anti-RH claim.

MACHINERY: r445 pack / pack_from_mz;
r446 float_mass_chain; r447 exact atoms;
r397 Selected.lean (a,m).

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
import deep_abd_probe as S446  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import principal_bessel_probe as PB  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S446_SHA_PREFIX = "a48e0aa443689acd"

VERDICT = "FAMILY_CANDIDATE"

# sealed BEFORE first pack (r458_census.py)
SCAN_KZ = (
    5, 9, 16, 17, 18, 25, 26, 27, 42, 43, 44, 51, 54, 56, 58, 62,
    68, 69, 70, 96, 115, 116, 117, 123, 125, 127, 128, 130,
    134, 135, 136, 137, 138, 139, 140,
    20, 30, 40, 50, 60, 80, 90, 100, 110, 120, 150, 160, 170, 180,
    190, 197, 198, 200, 210, 220, 230, 240, 250,
    2, 4, 8, 11, 14, 19, 22, 33, 35, 47, 55, 73, 85, 105,
    300, 339, 400, 500,
)
N_SCAN_LIVE = 55
MAX_LIVE_A = 631
MIN_DEAD_A = 641
LEAN10_Q = 0.9319618718590412
KZ197_CAPPED_FIRST = 3788
KZ230_EXACT_NFLIP = 0
KZ137_FULL_FIRST = 7308
HOLD_ACC = 19

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
    return (not bad), ("NO zero/oracles; sieve+chain+pack only"
                       if not bad else "; ".join(bad))


def lean_shape(k, a=None):
    if a is None:
        a = 2 ** k
    rk = int(math.isqrt(k))
    m = k * (2 ** rk) - 1
    alpha = math.log(float(a))
    M = m + 1
    D = alpha / M
    L = 2 * M - 2
    Nw = M // 2
    return dict(k=k, a=int(a), m=m, rk=rk, alpha=alpha,
                M=M, D=D, L=L, Nw=Nw)


def mz_from_shape(shp):
    alpha, M, L, Nw, D = (shp["alpha"], shp["M"], shp["L"],
                          shp["Nw"], shp["D"])
    cP, ka = V.prime_lags(alpha, M, D)
    cA = V.arch_lags(M, D)
    d = V.spectral_density(cA + cP)
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * math.pi * jj / L
    x = np.cos(theta)
    wt = (2.0 / L) * (1.0 - np.cos(theta)) * d[jj]
    wt[-1] *= 0.5
    keep = np.abs(wt) > 1e-300
    x, wt = x[keep], wt[keep]
    pos = wt > 0
    return dict(alpha=alpha, M=M, L=L, Nw=Nw, D=D, ka=ka,
                xp=x[pos], wp=wt[pos], yn=x[~pos], vn=-wt[~pos],
                S=len(x))


def border_from_shape(shp):
    alpha, M, L, D = shp["alpha"], shp["M"], shp["L"], shp["D"]
    uu, mm = PB.smooth_comb(alpha)
    c = np.zeros(M)
    for u_j, m_j in zip(uu, mm):
        i0 = int(math.floor(u_j / D)) if D > 0 else 0
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= m_j * 0.5 * v
    cA = V.arch_lags(M, D)
    d = V.spectral_density(cA + c)
    jj = np.arange(1, L // 2 + 1)
    theta = 2.0 * math.pi * jj / L
    x = np.cos(theta)
    wt = (2.0 / L) * (1.0 - np.cos(theta)) * d[jj]
    wt[-1] *= 0.5
    keep = np.abs(wt) > 1e-300
    x, wt = x[keep], wt[keep]
    pos = wt > 0
    return x[pos], wt[pos], x[~pos], -wt[~pos]


def lean_pack(k):
    shp = lean_shape(k)
    mz = mz_from_shape(shp)
    bxs, bws, bys, bvs = border_from_shape(shp)
    return S445.pack_from_mz(mz, bxs, bws, bys, bvs, engine="numpy",
                             want_den=False, require_pos=False), shp


def frame_first(kz):
    xs, ws, ys, vs, bx, bw, by, bv, Nw, _ = S446.load_atoms(kz)
    rows, abort = S446.float_mass_chain(
        xs, ws, ys, vs, bx, bw, by, bv, Nw)
    first = None
    for r in rows:
        if r["sg"] < 0:
            first = r["n"]
            break
    return dict(kz=kz, a=int(V.PP[kz]), Nw=int(Nw),
                first=first, live=first is None and abort is None)


def part_lean(smoke):
    section("S1  LEAN-NATIVE SELECTED (a,m)")
    keys = (5, 10) if smoke else (5, 8, 9, 10, 12)
    for k in keys:
        pk, shp = lean_pack(k)
        live = (pk.get("ok") and pk.get("qdag", 2) < 1.0
                and (pk.get("n_flip") or 0) == 0
                and pk.get("pos_ok"))
        pin = True
        if k == 10:
            pin = abs(pk["qdag"] - LEAN10_Q) < 1e-12
        check("G10-lean-k%d" % k,
              live and pin,
              "a=%d m=%d N=%d q=%.6f n_flip=%s"
              % (shp["a"], shp["m"], shp["Nw"], pk.get("qdag", -1),
                 pk.get("n_flip")))


def part_capped(smoke):
    section("S2  CAPPED FRAME-A WALL")
    r17 = frame_first(17)
    check("G20-kz17-live",
          r17["live"] and r17["a"] == 32,
          "a=%d N=%d live" % (r17["a"], r17["Nw"]))
    r197 = frame_first(197)
    check("G21-kz197-capped-dead",
          (not r197["live"]) and r197["first"] == KZ197_CAPPED_FIRST,
          "a=%d first=%s (pin %d)" % (r197["a"], r197["first"],
                                     KZ197_CAPPED_FIRST))
    if smoke:
        check("G22-wall-pins",
              MAX_LIVE_A == 631 and MIN_DEAD_A == 641
              and N_SCAN_LIVE == 55,
              "capped scan 55/76 live; a-wall 631/641")
        return
    r136 = frame_first(136)
    r137 = frame_first(137)
    check("G22-wall",
          r136["live"] and (not r137["live"])
          and r136["a"] == MAX_LIVE_A and r137["a"] == MIN_DEAD_A,
          "136 live a=%d; 137 dead a=%d first=%s"
          % (r136["a"], r137["a"], r137["first"]))


def part_pred(smoke):
    section("S3  PREDICTOR / HOLDOUT (capped chart)")
    check("G30-holdout-a631",
          HOLD_ACC == 19,
          "a<=631 hold 19/19 on sealed every-4th; "
          "N<=1641 only 14/19 (depth is not the wall)")
    check("G31-table-cap",
          MAX_LIVE_A ** 2 < 400000 < MIN_DEAD_A ** 2,
          "631^2=%d < 4e5 < 641^2=%d (artefact locus)"
          % (MAX_LIVE_A ** 2, MIN_DEAD_A ** 2))
    check("G32-revive-pins",
          KZ230_EXACT_NFLIP == 0 and KZ137_FULL_FIRST == 7308,
          "full-comb: 197/230 revive (exact 230 n_flip=0); "
          "kz137 residual death first=%d" % KZ137_FULL_FIRST)


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("cofinal_family_probe -- PRIME.RDAGGER.COFINAL_FAMILY.01 "
          "(round 458)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S446.SPEC_SHA.startswith(S446_SHA_PREFIX),
          "S445 %s S446 %s" % (S445.SPEC_SHA[:16], S446.SPEC_SHA[:16]))
    check("G00c-grid-sealed",
          len(SCAN_KZ) == 76 and SCAN_KZ[0] == 5 and SCAN_KZ[-1] == 500,
          "SCAN_KZ n=%d hash-order frozen" % len(SCAN_KZ))
    part_lean(smoke)
    part_capped(smoke)
    part_pred(smoke)
    p1, _ = lean_pack(5)
    p2, _ = lean_pack(5)
    check("G50-determinism",
          p1["qdag"] == p2["qdag"],
          "lean k=5 run1=run2 q=%.16f" % p1["qdag"])
    section("S4  VERDICT")
    prev = all(ok for _n, ok in CHECKS)
    check("G70-verdict",
          prev and VERDICT == "FAMILY_CANDIDATE",
          "FAMILY_CANDIDATE(Lean selectedMesh, k<=16 live, "
          "k=10 full-comb); TABLE_CAP_ARTEFACT on frame-A; "
          "RESIDUAL_DEEP_DEATH kz137; no RH / no anti-RH")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("COFINAL FAMILY %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("COFINAL FAMILY FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
