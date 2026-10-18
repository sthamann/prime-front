#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zloc_head_probe -- PRIME.TERMINAL.ZLOC_HEAD_BOUND.01
(round 429): |Z_loc(W_k)| <= 1/2 on the selected
sequence as a source-pure finite head bound.

THE OBJECT.  R428 ranked |Z_loc| the most
provable remaining coordinate.  The lemma
asks for a quellreine Kopfabschatzung that
would, with COMPOSE- (r378 SATZ) and the
measured R, L1 envelopes, give q_N<1 on
selected cofinally.

CALIBRATION DISCLOSURE.  Exact split
Z = t_loc + chain + t_bulk, edge-mask
formula, unsigned triangle, left-right
pairing, Abel partial sums, Chebyshev-style
majorant, scramble / dead chi / kz=16 /
EDGE_F-mutant first measured in /tmp
(r429_cal.py) on the r378/r383/r428
constructors, 2026-08-29.  Frozen floors
below are that measurement, sealed as
gates.  Pins disclosed.  No k=8 rebuild
(r421 pin, N=5690).

FROZEN FROM /tmp (live re-gated):
  * FORMULA SATZ: Z_loc = t_loc + chain
    with t_loc = sum_{x in E} w x v^(2)(x) fac
    on the F=1/5 hull-edge of the smooth
    border, hull [-1,1].  Split
    Z = Z_loc + t_bulk to 1e-14 (Lean
    canonical_split).  Pins k=3/4/5:
    0.486846 / 0.157211 / 0.227187.
  * NOT a finite von-Mangoldt head of
    small n: n_edge = 85,217,113,429,989,
    1691 on selected; support is a
    positive-fraction geometric tail.
  * UNSIGNED TRIANGLE REFUTED on selected:
    tri in [2.240, 19.245] ALL >> 1/2;
    log-log slope vs N = +0.534 (grows;
    r386 old-ladder slope was +0.25).
    k=9 tri=19.24.  Selected is NOT
    nicer for the unsigned bound.
  * Mild sign (left-right / Abel) REFUTED
    as SATZ: pair_c = 1 on k=5,7,9
    (same-sign edges); |A|_max / ||w||_1
    = 1 on k=3,4,6 (no weight cancel);
    var(phi) is 10^3..10^6.
  * |Z_loc| <= 1/2 is a FINITE CENSUS
    on k=3,4,5,6,7,9 (max 0.48685 at
    k=3, air 0.013).  No k0 from
    triangle / Chebyshev / Abel.
  * COMPOSE envelopes on selected:
    R <= 1.396 < 3/2 (census);
    L1 <= 0.628 -- the hoped 3/5 FAILS
    at k=9 (0.628 > 0.600); 2/3 works.
  * KILLS: scramble kz9 |Z_loc|=0.5236
    > 1/2; CHI3-15 1.021 > M; CHI4-20
    0.892 > M; kz16 0.756 (formula
    reproduces the 42er razor; the
    bound is selected-only).  False
    EDGE_F=2/5 at w9 gives 0.354
    (not 0.157).  Drop-chain is 0.037
    (not 0.157).  2*tri always worse.

AUSGANG FORMULA_SATZ / TRIANGLE_REFUTED /
BOUND_CENSUS / NO_K0.
SATZ: the identity Z_loc = t_loc + chain
and Lean canonical_split; COMPOSE-
imported.  REFUTED: unsigned triangle,
finite-head Chebyshev, left-right Abel
as a SATZ route to 1/2, even on selected.
REDUZIERT: |Z_loc|<=1/2 remains a sealed
finite census (k=3 tight, scramble-
unstable); no explicit k0.  Does not
move the mincut.  No RH claim.

MACHINERY: r378 row_of / r383 split,
r386 gram triangle, r428 selected map.

NO RH CLAIM.  Finite identities, a named
refutation of the unsigned-head route, a
named selected census.  Research
documentation, not a theorem of RH.
No L* claim.  No R-dagger claim.
Sealed gates: 18/18 smoke / 24/24 full
(G00--G02, G10--G12, G20--G25, G30--G34,
G40--G45, G50).
Companion verifier 6/6 ZLOC HEAD VERIFIED.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import compose_premises_probe as C  # noqa: E402
import compose_premises2_probe as C2  # noqa: E402
import bordered_hankel_probe as BH  # noqa: E402
import qn_reopened_probe as Q  # noqa: E402

C_SHA_PREFIX = "146b0b45"
C2_SHA_PREFIX = "82d07e56"
Q_SHA_PREFIX = "fc2c617a"
BH_SHA_PREFIX = "c21e15b5"

M_W = C.M_W
Z0 = Fr(1, 2)
EDGE_F = C.PBB.EDGE_F
SEL_LIVE = ((3, 5), (4, 9), (5, 17), (6, 26), (7, 43), (9, 116))

K3_ZLOC, K4_ZLOC, K5_ZLOC = 0.486846, 0.157211, 0.227187
K3_TRI, K4_TRI, K9_TRI = 2.2403, 2.8744, 19.2445
K3_NEDGE, K4_NEDGE, K9_NEDGE = 85, 217, 1691
K4_TLOC, K4_CHAIN = -0.03720, -0.12001
SCR_ZLOC, KZ16_ZLOC = 0.5236, 0.75567
DEAD15_ZLOC, DEAD20_ZLOC = 1.0213, 0.8920
FALSE_F40 = 0.3541
R_MAX, L1_K9, L1_23 = 1.3961, 0.628, Fr(2, 3)
TRI_SLOPE_LO = 0.30
REL = 5.0e-3

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
    return (not bad), ("NO zero/prime oracles; selected "
                       "head identity / triangle only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


def dict_Q():
    Z = Fr(1, 2)
    q = Fr(7, 5) * Z * Z
    return dict(Z=Z, q=q, z0=Z, z0_lt_M=(Z * Z < Fr(5, 7)))


def split_Q():
    """Z = Zloc + t_bulk over Q (Lean canonical_split)."""
    t_loc, chain, t_bulk = Fr(-2, 5), Fr(-1, 5), Fr(1, 10)
    Zloc = t_loc + chain
    Z = Zloc + t_bulk
    tri = abs(t_loc) + abs(chain)
    return dict(Z=Z, Zloc=Zloc, t_bulk=t_bulk,
                split=Z - Zloc - t_bulk == 0,
                tri=tri, tri_gt_half=tri > Fr(1, 2))


def dissect(p):
    N = p["N"]
    rows = p["rows"]
    r, t, ap, bp = C.TX.drive_arrays(rows, N)
    chain = float(ap[N - 2] * r[N - 2] + bp[N - 2] * r[N - 3])
    Z = float(t[N - 2] + chain)
    xu, wu = C.CT.union_arrays(p["d"])
    bx, bw = C.CT.union_arrays(p["dsm"])
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    v2 = C.BR.eval_scaled(rows, bx, N - 2)
    fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
        / math.sqrt(abs(rows[N - 1]["eta"]))
    ct = bw * bx * v2 * fac
    o = np.argsort(bx, kind="stable")
    bxs, cts = bx[o], ct[o]
    ed = C.PBB.mask_edge(bxs, lo, hi, EDGE_F)
    t_loc = float(np.sum(cts[ed])) if np.any(ed) else 0.0
    tri = float(np.sum(np.abs(cts[ed]))) if np.any(ed) else 0.0
    Zloc = t_loc + chain
    cb = cts[~ed]
    t_bulk = float(np.sum(cb)) if cb.size else 0.0
    mid = 0.5 * (lo + hi)
    tL = float(np.sum(cts[ed & (bxs <= mid)]))
    tR = float(np.sum(cts[ed & (bxs > mid)]))
    pair = abs(tL) + abs(tR)
    return dict(
        N=N, Z=Z, Zloc=Zloc, absZloc=abs(Zloc),
        t_loc=t_loc, chain=chain, t_bulk=t_bulk, tri=tri,
        n_edge=int(np.sum(ed)), n_atom=int(len(cts)),
        lo=lo, hi=hi, tL=tL, tR=tR,
        pair_c=abs(tL + tR) / max(pair, 1e-300),
        split=abs(Z - Zloc - t_bulk),
        cancel=abs(t_loc) / max(tri, 1e-300),
    )


def pack(kz, **kw):
    return BH.wpack(kz, kw) if kw else BH.wpack(kz)


def false_edge(kz, frac):
    p = pack(kz)
    N = p["N"]
    rows = p["rows"]
    r, t, ap, bp = C.TX.drive_arrays(rows, N)
    chain = float(ap[N - 2] * r[N - 2] + bp[N - 2] * r[N - 3])
    xu, _wu = C.CT.union_arrays(p["d"])
    bx, bw = C.CT.union_arrays(p["dsm"])
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    v2 = C.BR.eval_scaled(rows, bx, N - 2)
    fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
        / math.sqrt(abs(rows[N - 1]["eta"]))
    ct = bw * bx * v2 * fac
    o = np.argsort(bx, kind="stable")
    bxs, cts = bx[o], ct[o]
    ed = C.PBB.mask_edge(bxs, lo, hi, frac)
    return abs(float(np.sum(cts[ed])) + chain)


def part_satz():
    section("S1  SATZ / Q")
    t = dict_Q()
    check("G10-dictionary-Q",
          t["q"] == Fr(7, 20) and t["z0_lt_M"],
          "q_N=7/20 at Z=1/2; 1/2 < M")
    s = split_Q()
    check("G11-split-Q",
          s["split"] and s["Zloc"] == Fr(-3, 5)
          and s["tri_gt_half"] and s["Z"] == Fr(-1, 2),
          "Z=Zloc+t_bulk; triangle 2/5+1/5 > 1/2")
    check("G12-half-lt-M-Q",
          Fr(1, 4) < Fr(5, 7) and L1_23 > Fr(3, 5),
          "Z0=1/2 works in COMPOSE; 2/3 > 3/5")


def part_pins():
    section("S2  FORMULA PINS (k=3,4,5)")
    d3 = dissect(pack(5))
    d4 = dissect(pack(9))
    d5 = dissect(pack(17))
    check("G20-k3-formula",
          abs(d3["absZloc"] - K3_ZLOC) <= 2e-6
          and d3["split"] <= 1e-12
          and abs(d3["lo"] + 1) <= 1e-9
          and d3["hi"] > 0.99
          and d3["n_edge"] == K3_NEDGE,
          "|Zloc|=%.6f t_loc+chain split=%.1e n_edge=%d hull[-1,1]"
          % (d3["absZloc"], d3["split"], d3["n_edge"]))
    check("G21-k4-formula",
          abs(d4["absZloc"] - K4_ZLOC) <= 2e-6
          and abs(d4["t_loc"] - K4_TLOC) <= 2e-5
          and abs(d4["chain"] - K4_CHAIN) <= 2e-5
          and d4["n_edge"] == K4_NEDGE,
          "w9 |Zloc|=%.6f = t_loc %.5f + chain %.5f; n_edge=%d"
          % (d4["absZloc"], d4["t_loc"], d4["chain"], d4["n_edge"]))
    check("G22-k5-formula",
          abs(d5["absZloc"] - K5_ZLOC) <= 2e-5
          and d5["split"] <= 1e-12,
          "k=5 |Zloc|=%.6f (pin %.6f)"
          % (d5["absZloc"], K5_ZLOC))
    check("G23-triangle-gt-half",
          d3["tri"] > 0.5 and d4["tri"] > 0.5
          and abs(d3["tri"] - K3_TRI) <= 0.01
          and abs(d4["tri"] - K4_TRI) <= 0.01,
          "tri k3/k4 = %.3f / %.3f >> 1/2"
          % (d3["tri"], d4["tri"]))
    check("G24-not-finite-head",
          d3["n_edge"] >= 80 and d4["n_edge"] > d3["n_edge"]
          and abs(d3["lo"] + 1) <= 1e-9,
          "n_edge grows 85->217 on hull[-1,1]; "
          "geometric F=1/5, not small-n")
    check("G25-k5-same-sign-edges",
          d5["pair_c"] >= 0.99,
          "k=5 pair_c=%.3f (left-right Abel does not fire)"
          % d5["pair_c"])
    return d3, d4, d5


def part_kills():
    section("S3  KILLS")
    s = dissect(pack(9, scramble_seed=1))
    check("G30-scramble-breaks-half",
          s["absZloc"] > 0.5
          and abs(s["absZloc"] - SCR_ZLOC) <= 0.02,
          "SCR |Zloc|=%.4f > 1/2 (named kill off MAIN)"
          % s["absZloc"])
    d15 = dissect(C2.chi_pack("CHI3", 15))
    check("G31-dead15-gt-M",
          d15["absZloc"] > M_W
          and abs(d15["absZloc"] - DEAD15_ZLOC) <= 0.02,
          "CHI3-15 |Zloc|=%.4f > M (formula shows death)"
          % d15["absZloc"])
    a16 = dissect(pack(16))
    check("G32-kz16-razor",
          abs(a16["absZloc"] - KZ16_ZLOC) <= 0.002
          and a16["absZloc"] > 0.5,
          "kz16 |Zloc|=%.4f (42er razor; bound is selected-only)"
          % a16["absZloc"])
    f40 = false_edge(9, 2 * EDGE_F)
    check("G33-false-head-zone",
          abs(f40 - FALSE_F40) <= 0.01
          and abs(f40 - K4_ZLOC) >= 0.1,
          "EDGE_F=2/5 |Zloc|=%.4f != 0.157" % f40)
    d4 = dissect(pack(9))
    check("G34-drop-chain-and-psi2",
          abs(abs(d4["t_loc"]) - abs(K4_TLOC)) <= 2e-4
          and abs(d4["t_loc"]) < 0.5 * K4_ZLOC
          and 2 * d4["tri"] > 5,
          "drop-chain |t_loc|=%.4f; 2*tri=%.2f"
          % (abs(d4["t_loc"]), 2 * d4["tri"]))


def part_census(smoke):
    section("S4  SELECTED CENSUS" + (" (smoke skip)" if smoke else ""))
    if smoke:
        return []
    rows = []
    for k, kz in SEL_LIVE:
        d = dissect(pack(kz))
        r0 = C2.row2(pack(kz))
        d["k"], d["kz"] = k, kz
        d["R"], d["L1"], d["qN"] = r0["R"], r0["L1"], r0["qN"]
        rows.append(d)
        print("    k=%d kz=%d N=%d |Zloc|=%.5f tri=%.3f "
              "n_edge=%d R=%.3f L1=%.3f pair_c=%.3f"
              % (k, kz, d["N"], d["absZloc"], d["tri"],
                 d["n_edge"], d["R"], d["L1"], d["pair_c"]))
    zls = [r["absZloc"] for r in rows]
    tris = [r["tri"] for r in rows]
    # two-point log-log slope (k=3 vs k=9); no fit primitive
    sl = (math.log(rows[-1]["tri"]) - math.log(rows[0]["tri"])) / (
        math.log(rows[-1]["N"]) - math.log(rows[0]["N"]))
    check("G40-selected-half",
          all(z < 0.5 for z in zls) and max(zls) < 0.487
          and abs(max(zls) - K3_ZLOC) <= 2e-5,
          "6/6 |Zloc|<=1/2; max=%.5f at k=3" % max(zls))
    check("G41-tri-grows",
          max(tris) > 15 and abs(max(tris) - K9_TRI) <= 0.05
          and rows[-1]["n_edge"] == K9_NEDGE,
          "k=9 tri=%.3f n_edge=%d (unsigned grows)"
          % (max(tris), rows[-1]["n_edge"]))
    check("G42-slope-positive",
          sl > TRI_SLOPE_LO,
          "log-log tri vs N slope=%.3f > 0.30 (no k0)"
          % sl)
    check("G43-L1-35-fails",
          rows[-1]["L1"] > float(Fr(3, 5))
          and abs(rows[-1]["L1"] - L1_K9) <= 0.01
          and rows[-1]["L1"] < float(L1_23),
          "k=9 L1=%.3f > 3/5, < 2/3 (hoped 3/5 FAILS)"
          % rows[-1]["L1"])
    check("G44-compose-census",
          max(r["R"] for r in rows) < 1.5
          and abs(max(r["R"] for r in rows) - R_MAX) <= 0.01
          and all(r["L1"] < float(L1_23) for r in rows)
          and all(r["qN"] < 1 for r in rows),
          "R<=%.3f < 3/2; L1<=2/3; qN<1 (all CENSUS)"
          % max(r["R"] for r in rows))
    d20 = dissect(C2.chi_pack("CHI4", 20))
    check("G45-dead20-gt-M",
          d20["absZloc"] > M_W
          and abs(d20["absZloc"] - DEAD20_ZLOC) <= 0.02,
          "CHI4-20 |Zloc|=%.4f > M" % d20["absZloc"])
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("zloc_head_probe -- "
          "PRIME.TERMINAL.ZLOC_HEAD_BOUND.01 (round 429)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (selected k=3..7,9; k=8 not rebuilt)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (C.SPEC_SHA.startswith(C_SHA_PREFIX)
              and C2.SPEC_SHA.startswith(C2_SHA_PREFIX)
              and Q.SPEC_SHA.startswith(Q_SHA_PREFIX)
              and BH.SPEC_SHA.startswith(BH_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "C %s C2 %s Q %s BH %s"
          % (C.SPEC_SHA[:8], C2.SPEC_SHA[:8],
             Q.SPEC_SHA[:8], BH.SPEC_SHA[:8]))
    ag = antigate_fragment_audit()
    check("G00c-no-fit", not ag,
          "no fit primitives" if not ag else "; ".join(ag))

    part_satz()
    part_pins()
    part_kills()
    part_census(smoke)

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "FORMULA_SATZ / TRIANGLE_REFUTED / "
          "BOUND_CENSUS / NO_K0.  no RH / L* / R-dagger")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = ("FORMULA_SATZ / TRIANGLE_REFUTED / "
            "BOUND_CENSUS / NO_K0")
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("ZLOC HEAD %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("ZLOC HEAD FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
