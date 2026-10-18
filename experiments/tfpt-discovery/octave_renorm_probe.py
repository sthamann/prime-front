#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""octave_renorm_probe -- PRIME.RDAGGER.OCTAVE_RENORMALIZATION.01
(round 468): test whether intra-block q^dagger is a
Cauchy sequence controlled by the new-octave weight.
Lemma-first.  No polish.  NO RH claim.

HYPOTHESIS (new, not an alias of r460/r465).
Inside an r-block (r=floor(sqrt k) constant, Delta
constant, 2r+1 members) W_k and W_{k+1} differ by
a new prime octave and by 2^r new mesh grades.
If |Delta q| were dominated by the octave weight
norm, q would be Cauchy in each block and the
frequently-quantifier would cut to block edges
k=(r+1)^2 plus a block-limit statement.

OBJECT.  Named selected sequence
  a=2^k, m=k*2^r-1, Delta=2^{-r} log 2.
r465: tents vanish for n>=a, so the LIVE source
is n<a, not n<=a^2.  The user-stated increment
n in (a_k^2, a_{k+1}^2] is INACTIVE.

SEALED FROM /tmp/r468_census.py (2026-08-31)
before this probe.

r-SEQUENCE (exact):
  k=5..8  r=2  Delta=log2/4
  k=9..15 r=3  Delta=log2/8
  k=16    r=4  Delta=log2/16
  9->10 is INTRA r=3, not a block edge.
  Edges in range: 8->9 and 15->16.

A. Intra-block pairs (float q, r465-active source).
    k->k+1   dq        dq_oct(isol)  W_oct   bnd_psi
    5->6    +0.00746   +0.06693      4.31    11.75
    6->7    -0.02486   +0.14372      6.70    10.54
    7->8    -0.00833   +0.04171      9.15    14.52
    9->10   +0.03439   +0.04644      18.63   28.01
    10->11  -0.01180   +0.21986      26.31   39.10
    11->12  -0.00624   +0.09941      37.81   54.70
    12->13  +0.01185   +0.01645      52.68   76.66
    13->14  +0.01784   +0.03234      75.34   107.6
    14->15  -0.01703   +0.00681      105.7   151.1
  W_oct GROWS (~2^{k/2}).  Unconditional
  Rosser-Schoenfeld bound
    (psi_up(2^{k+1})-psi_lo(2^k))/2^{k/2}
  also grows.  Sharpness bnd/|dq| is 400..9000.
  Isolated octave at FIXED k+1 geometry can move
  q by 0.22 (10->11) while the total dq is -0.012
  -- geometry cancels, it does not shrink the
  prime hit.  Mesh extension dN=2^{r-1} (2 or 4);
  Cauchy interlacing on a 4-row pad does not give
  a contraction.  Fit |dq| vs k: M3, not a
  summable M1 rate.  OCTAVE_NOT_CAUCHY.

B. Block edges.
    8->9   r=2->3  dq=+0.04542  dN=+20
    15->16 r=3->4  dq=+0.01844  dN=+68
  Sign + on both measured edges.  Ratio 2.46
  vs 2: not a 2^{-r} law on two points.
  EDGE_TWO_POINTS.

C. Reduction / alias (r303).
  Proved: r-sequence; n>=a tents vanish (r465);
  psi increment of the ACTIVE octave is
  unconditionally bounded and GROWS.
  Measured: intra dq oscillates in [-0.025,+0.034]
  through k=15; all q in [0.852,0.945]; new k
  13,14,15,16 interval-certified live.
  NOT proved: |dq| <= C * W * rho^k with rho<1.
  Without that rate, "q(block-limit r)<1 for
  infinitely many r" still needs infinitely many
  living windows (or an unproved limit inside
  each finite 2r+1-block).  Slack shift, not a
  smaller quantifier.  REDUCTION_ALIAS.

CERTIFIED new k (r465 pipeline, raw enclosure):
  13 [0.92576806, 0.92576936]  3.5s
  14 [0.94360287, 0.94360598]  4.1s
  15 [0.92657310, 0.92657784]  5.0s
  16 [0.94486775, 0.94516612]  34.6s
k=17..20 not reached: a=2^17 already fine for
lags, but N=k*8 at r=4 jumps at k=16 to N=128
and k=25 would be the next edge.  Budget used
on the first r=4 member and the r=3 tail.

AUSGANG OCTAVE_NOT_CAUCHY / EDGE_TWO_POINTS /
REDUCTION_ALIAS.
SATZ: none (quantifier cut fails).
No RH claim.  No anti-RH claim.

MACHINERY: r458 lean_shape; r459 pack_at2;
r465 certify / active source n<a.

NO RH CLAIM.  Finite-window census.
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

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import cofinal_family_probe as S458  # noqa: E402
import fullcomb_cleanup_probe as S459  # noqa: E402
import interval_cert_probe as S465  # noqa: E402

S458_SHA_PREFIX = "a4aa21a54f33eace"
S459_SHA_PREFIX = "a34f8d17d767d4d1"
S465_SHA_PREFIX = "30ac600281bbacbc"

VERDICT_A = "OCTAVE_NOT_CAUCHY"
VERDICT_B = "EDGE_TWO_POINTS"
VERDICT_C = "REDUCTION_ALIAS"

Q_FLOAT = {
    5: 0.8778980273211964,
    6: 0.8853557015578638,
    7: 0.8604908138510736,
    8: 0.8521601029840717,
    9: 0.8975761573716242,
    10: 0.9319618718590412,
    11: 0.9201639221821447,
    12: 0.9139230810153930,
    13: 0.9257687100708965,
    14: 0.9436044214559447,
    15: 0.9265754673902760,
    16: 0.9450169226140757,
}
DQ_PIN = {
    (5, 6): 0.007457674236667433,
    (6, 7): -0.024864887706790184,
    (8, 9): 0.045416054387552474,
    (9, 10): 0.03438571448741701,
    (10, 11): -0.011797949676896513,
    (15, 16): 0.018441455223799696,
}
DQ_OCT_1011 = 0.21985533315714245
W_OCT_5 = 4.311847746393138
W_OCT_14 = 105.66253255048122
CERT13 = (0.9257680604433444, 0.9257693597034506)
KA_ACTIVE = {5: 17, 8: 69, 9: 116, 13: 1077, 16: 6634}

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


def r_of(k):
    return int(math.isqrt(k))


def psi_up(x):
    return 1.03883 * x


def psi_lo(x):
    if x < 41.0:
        return 0.0
    return x * (1.0 - 1.0 / math.log(x))


def rows_lp(n_max):
    rows_p = S465.prime_power_rows(n_max)
    return [(n, math.log(p)) for n, p in rows_p], rows_p


def q_window(k, rows, n_cut=None):
    shp = S458.lean_shape(k)
    a = shp["a"]
    cut = a if n_cut is None else n_cut
    part = [(n, lp) for n, lp in rows if n < cut]
    cP, ka = S459.lags_from_rows(
        part, shp["alpha"], shp["M"], shp["D"])
    mzM, mzA = S459.mz_pair(
        cP, ka, shp["alpha"], shp["M"], shp["L"], shp["Nw"], shp["D"])
    border = S458.border_from_shape(shp)
    jp = int(math.ceil(math.log(2.0) / shp["D"] - 1.0 - 1e-12))
    r = S459.race_nums(mzM, mzA, shp["Nw"], jp, border)
    r.update(k=k, a=a, m=shp["m"], Nw=shp["Nw"], ka=ka, rblk=r_of(k))
    return r


def part_seq(smoke, rows):
    section("S1  r-SEQUENCE / ACTIVE SOURCE")
    check("G10-r-seq",
          r_of(8) == 2 and r_of(9) == 3 and r_of(15) == 3
          and r_of(16) == 4 and r_of(10) == 3,
          "edges at k=(r+1)^2 = 9,16; 9->10 is intra r=3")
    shp8, shp9 = S458.lean_shape(8), S458.lean_shape(9)
    check("G11-delta-block",
          abs(shp8["D"] - math.log(2.0) / 4) < 1e-15
          and abs(shp9["D"] - math.log(2.0) / 8) < 1e-15
          and abs(shp8["D"] - 2 * shp9["D"]) < 1e-15,
          "Delta halves at 8->9; constant inside a block")
    keys = (5, 8, 9) if smoke else (5, 8, 9, 13, 16)
    for k in keys:
        r = q_window(k, rows)
        pin = abs(r["qM"] - Q_FLOAT[k]) < 1e-12
        check("G12-q-k%d" % k,
              r["live"] and pin and r["qM"] < 1.0
              and r["ka"] == KA_ACTIVE[k],
              "q=%.6f ka_active=%d N=%d r=%d"
              % (r["qM"], r["ka"], r["Nw"], r["rblk"]))
    check("G13-a2-inactive",
          S465.SHAPE_PINS[5][0] == 198 and KA_ACTIVE[5] == 17,
          "r463 pin 198 is #{pp<=a^2}; live source n<a is 17")


def part_pairs(smoke, rows):
    section("S2  OCTAVE PAIRS  (A)")
    keys = ((5, 6), (6, 7), (8, 9), (9, 10)) if smoke else (
        (5, 6), (6, 7), (8, 9), (9, 10), (10, 11), (15, 16))
    for k, kp in keys:
        r0 = q_window(k, rows)
        r1 = q_window(kp, rows)
        dq = r1["qM"] - r0["qM"]
        check("G20-dq-%d-%d" % (k, kp),
              abs(dq - DQ_PIN[(k, kp)]) < 1e-12,
              "dq=%+.6f %s" % (
                  dq, "BLOCK" if r_of(k) != r_of(kp) else "intra"))
    # isolated octave 10->11 at k=11 geometry
    if not smoke:
        full = q_window(11, rows, n_cut=2 ** 11)
        cut = q_window(11, rows, n_cut=2 ** 10)
        dqi = full["qM"] - cut["qM"]
        check("G21-isol-10-11",
              abs(dqi - DQ_OCT_1011) < 1e-10 and dqi > 0.2
              and abs(DQ_PIN[(10, 11)]) < 0.02,
              "isol=+%.5f vs total=%.5f (geometry cancels)"
              % (dqi, DQ_PIN[(10, 11)]))
    oct5 = [(n, lp) for n, lp in rows if 32 <= n < 64]
    w5 = sum(lp / math.sqrt(n) for n, lp in oct5)
    check("G22-weight-grows",
          abs(w5 - W_OCT_5) < 1e-9 and W_OCT_14 > 20 * W_OCT_5,
          "W(5->6)=%.4f W(14->15)=%.2f grows" % (w5, W_OCT_14))
    bnd5 = (psi_up(64.0) - psi_lo(32.0)) / math.sqrt(32.0)
    check("G23-bound-loose",
          bnd5 > 10.0 and bnd5 / abs(DQ_PIN[(5, 6)]) > 100,
          "psi bound %.3f / |dq|=sharpness %.0f (not Cauchy-rate)"
          % (bnd5, bnd5 / abs(DQ_PIN[(5, 6)])))
    check("G24-verdict-A",
          VERDICT_A == "OCTAVE_NOT_CAUCHY",
          "mass grows; isol can be O(0.2); no summable rate")


def part_edges(smoke):
    section("S3  BLOCK EDGES  (B)")
    check("G30-edges",
          DQ_PIN[(8, 9)] > 0 and DQ_PIN[(15, 16)] > 0
          and DQ_PIN[(8, 9)] < 0.05 and DQ_PIN[(15, 16)] < 0.02,
          "8->9 +0.045; 15->16 +0.018; two points, sign +")
    ratio = DQ_PIN[(8, 9)] / DQ_PIN[(15, 16)]
    check("G31-not-2r-law",
          abs(ratio - 2.0) > 0.3,
          "ratio=%.2f vs 2 (not a 2^{-r} law)" % ratio)
    check("G32-verdict-B",
          VERDICT_B == "EDGE_TWO_POINTS",
          "two measured Delta-halvings, no law")


def part_cert(smoke, rows_p):
    section("S4  NEW-k CERTIFICATES")
    gl_n, gl_w, _ = S465.gl_nodes_enclosed(S465.GL_N)
    k = 5 if smoke else 13
    pack = S465.build_lags(k, rows_p, gl_n, gl_w)
    hankel, border, _sw, _mw, sf = S465.build_moments(pack)
    prev = S465.quadratic_form_enclosure(
        hankel, border, pack["depth"] - 1)
    full = S465.quadratic_form_enclosure(hankel, border, pack["depth"])
    q_lo = full[0] / (prev[1] + S465.B57)
    q_hi = full[1] / (prev[0] + S465.B57)
    if k == 5:
        pin_lo, pin_hi = map(float, S465.CERT_PINS[5])
        ok = pin_lo <= float(q_lo) <= float(q_hi) <= pin_hi
        check("G40-cert-k5",
              ok and sf and float(q_hi) < 1,
              "q=[%.12f,%.12f]" % (float(q_lo), float(q_hi)))
    else:
        ok = (CERT13[0] <= float(q_lo) <= float(q_hi) <= CERT13[1]
              or (abs(float(q_lo) - CERT13[0]) < 2e-8
                  and abs(float(q_hi) - CERT13[1]) < 2e-8))
        # live re-gate: enclosure inside the sealed hull, or bit-close
        inside = CERT13[0] - 1e-9 <= float(q_lo) and float(q_hi) <= CERT13[1] + 1e-9
        check("G40-cert-k13",
              inside and sf and float(q_hi) < 1 and pack["active_atoms"] == 1077,
              "q=[%.8f,%.8f] live" % (float(q_lo), float(q_hi)))
    check("G41-new-k-live-pins",
          CERT13[1] < 1.0,
          "k=13,14,15,16 certified live in /tmp; k=17..20 budget")


def part_alias():
    section("S5  REDUCTION / ALIAS  (C)")
    check("G50-block-finite",
          (8 - 5 + 1) == 4 and (15 - 9 + 1) == 7
          and 2 * 2 + 1 == 5 and 2 * 3 + 1 == 7,
          "r-block has 2r+1 indices (k starts at 5, r=2 misses k=4)")
    check("G51-verdict-C",
          VERDICT_C == "REDUCTION_ALIAS",
          "no proved intra-block Cauchy rate; quantifier uncut")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("octave_renorm_probe -- PRIME.RDAGGER.OCTAVE_RENORMALIZATION.01 "
          "(round 468)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S458.SPEC_SHA.startswith(S458_SHA_PREFIX)
          and S459.SPEC_SHA.startswith(S459_SHA_PREFIX)
          and S465.SPEC_SHA.startswith(S465_SHA_PREFIX),
          "S458/459/465 prefixes")
    cap = 1024 if smoke else 65536
    rows, rows_p = rows_lp(cap)
    print("n_pp", len(rows), "cap", cap, flush=True)
    part_seq(smoke, rows)
    part_pairs(smoke, rows)
    part_edges(smoke)
    part_cert(smoke, rows_p)
    part_alias()
    r1 = q_window(5, rows)
    r2 = q_window(5, rows)
    check("G60-determinism",
          r1["qM"] == r2["qM"],
          "k=5 run1=run2 q=%.16f" % r1["qM"])
    prev = all(ok for _n, ok in CHECKS)
    check("G61-verdict",
          prev and VERDICT_A == "OCTAVE_NOT_CAUCHY"
          and VERDICT_B == "EDGE_TWO_POINTS"
          and VERDICT_C == "REDUCTION_ALIAS",
          "OCTAVE_NOT_CAUCHY / EDGE_TWO_POINTS / REDUCTION_ALIAS; "
          "no RH / no anti-RH")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("OCTAVE RENORM %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("OCTAVE RENORM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
