#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_medcap_steps.py -- machine check of every numbered lemma
in rh/problem/medcap_lemma.tex.

PART A (STANDALONE): exact Fractions arithmetic on abstract packings.
  G1  window convention (W=5, odd third / even midpoint)
  G2  SEP-SATZ identity d = e + (n+n')/2
  G3  tiling => gap = sep
  G4  C2 counterexample n=(1,2,8^10), ratio 16/3
  G5  short C2 n=(1,2,6,6,6,6), third-smallest 6, ratio 4
  G6  saturating prefix (1,2,6,5,4,4), med=4, sep=3/2, ratio 8/3
  G7  random tiled compositions still violate (n-variation, not empties)
  G8  ledger toy {0}/{2,3}/{6} holds SEP and MED-CAP

PART B (CONSTRUCTION CROSS-CHECK, repo builders):
  G9  chi4 kz53 realises the saturating prefix, two atoms g=3/8
  G10 four w9 worlds are tiled (empty==0, hull-solid) and MED-CAP clean

Exit: per-gate PASS/FAIL and the final line
"MEDCAP STEPS VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named remainder only.
"""
from __future__ import annotations

import os
import random
import sys
from fractions import Fraction as Fr

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
VERIFY = os.path.join(REPO, "verification")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, VERIFY, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

CHECKS = []
W = 5
CAP = Fr(8, 3)
RNG = random.Random(361)


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72, flush=True)


def sides(ns, empties):
    return [Fr(empties[i]) + Fr(ns[i] + ns[i + 1], 2)
            for i in range(len(ns) - 1)]


def gaps_of(d):
    m = len(d) + 1
    return [d[0]] + [min(d[i - 1], d[i]) for i in range(1, m - 1)] + [d[-1]]


def seps_of(ns):
    sb = [Fr(ns[i] + ns[i + 1], 2) for i in range(len(ns) - 1)]
    m = len(ns)
    out = []
    for i in range(m):
        if i == 0:
            out.append(sb[0])
        elif i == m - 1:
            out.append(sb[-1])
        else:
            out.append(min(sb[i - 1], sb[i]))
    return out, sb


def medians(gaps, w=W):
    m = len(gaps)
    out = []
    for i in range(m):
        lo, hi = max(0, i - w), min(m, i + w + 1)
        nb = sorted(gaps[j] for j in range(lo, hi) if j != i)
        k = len(nb)
        if k % 2:
            med = nb[k // 2]
        else:
            med = (nb[k // 2 - 1] + nb[k // 2]) / 2
        out.append(med)
    return out


def pack(ns, empties):
    d = sides(ns, empties)
    g = gaps_of(d)
    seps, sb = seps_of(ns)
    med = medians(g)
    viol = [i for i in range(len(ns)) if med[i] > CAP * seps[i]]
    ratios = [med[i] / seps[i] for i in range(len(ns))]
    return dict(d=d, gaps=g, seps=seps, sb=sb, med=med,
                viol=viol, worst=max(ratios))


# ------------------------------------------------------------------ PART A
section("PART A  STANDALONE FRACTIONS GEOMETRY")

# G1 window convention
gtoy = [Fr(2), Fr(1), Fr(1), Fr(3), Fr(3)]
m5 = medians(gtoy, 5)
# m=5, i=2: 4 neighbours, even, midpoint of 2nd and 3rd of [1,2,3,3] = 2.5
check("G1-window-W5-even-midpoint",
      m5[2] == Fr(5, 2),
      "center med=%s (4 neighbours, midpoint)" % m5[2])
# edge i=0 of a 6-block column: 5 neighbours, third-smallest
g6 = [Fr(3, 2), Fr(3, 2), Fr(4), Fr(9, 2), Fr(4), Fr(4)]
m6 = medians(g6, 5)
nb0 = sorted(g6[1:])
check("G1-edge-third-of-five",
      m6[0] == nb0[2] == Fr(4),
      "med_0=%s third of %s" % (m6[0], nb0))

# G2 SEP identity
ns = [1, 2, 6, 5]
emp = [0, 1, 3]
d = sides(ns, emp)
sb = [Fr(ns[i] + ns[i + 1], 2) for i in range(3)]
check("G2-SEP-identity",
      d == [emp[i] + sb[i] for i in range(3)] and all(x >= y for x, y in zip(d, sb)),
      "d=%s sb=%s" % (d, sb))

# G3 tiling => gap=sep
r = pack([3, 4, 5, 4, 3], [0, 0, 0, 0])
check("G3-tiling-gap-eq-sep",
      r["gaps"] == r["seps"] and r["d"] == r["sb"],
      "gaps=%s seps=%s" % (r["gaps"], r["seps"]))

# G4 C2
rC2 = pack([1, 2] + [8] * 10, [0] * 11)
check("G4-C2-ratio-16/3",
      rC2["viol"][:2] == [0, 1] and rC2["med"][0] == Fr(8)
      and rC2["seps"][0] == Fr(3, 2)
      and rC2["worst"] == Fr(16, 3),
      "viol=%s med0=%s sep0=%s worst=%s" %
      (rC2["viol"][:4], rC2["med"][0], rC2["seps"][0], rC2["worst"]))

# G5 short C2
rS = pack([1, 2, 6, 6, 6, 6], [0] * 5)
check("G5-short-C2-third-is-6",
      0 in rS["viol"] and rS["med"][0] == Fr(6)
      and rS["med"][0] / rS["seps"][0] == Fr(4),
      "med0=%s ratio=%s" % (rS["med"][0], rS["med"][0] / rS["seps"][0]))

# G6 saturating prefix
rE = pack([1, 2, 6, 5, 4, 4], [0] * 5)
check("G6-equality-prefix-8/3",
      rE["viol"] == [] and rE["med"][0] == Fr(4)
      and rE["seps"][0] == Fr(3, 2)
      and rE["med"][0] / rE["seps"][0] == CAP
      and rE["med"][1] / rE["seps"][1] == CAP,
      "med0=%s med1=%s sep=%s ratio=%s" %
      (rE["med"][0], rE["med"][1], rE["seps"][0],
       rE["med"][0] / rE["seps"][0]))

# G7 random tiled still violate
nv = 0
for _ in range(200):
    m = RNG.randint(8, 16)
    ns = [RNG.randint(1, 9) for _ in range(m)]
    rr = pack(ns, [0] * (m - 1))
    if rr["viol"]:
        nv += 1
check("G7-random-tiled-still-violate",
      nv > 0,
      "%d/200 tiled random compositions violate MED-CAP" % nv)

# G8 ledger toy
# supports {0}, {2,3}, {6}: n=(1,2,1), empty=(1,2)
rT = pack([1, 2, 1], [1, 2])
check("G8-ledger-toy-holds",
      rT["viol"] == [] and rT["d"][0] == Fr(5, 2) and rT["seps"][0] == Fr(3, 2),
      "sides=%s seps=%s worst=%s" % (rT["d"], rT["seps"], rT["worst"]))


# ------------------------------------------------------------------ PART B
section("PART B  CONSTRUCTION CROSS-CHECK (r361 Fractions ledger)")

import numpy as np  # noqa: E402
import mean_sieve_floor_probe as MSF  # noqa: E402
import local_gap_carleson_probe as LGC  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import dirichlet_secondworld_probe as DSW  # noqa: E402
import bordered_hankel_probe as BH  # noqa: E402
import second_family_erosion_probe as SFE  # noqa: E402
import verify_lstar_instance as V  # noqa: E402


def hull_holes(rc, m, fl):
    pos, blk, _m = MSF.row_positions(rc)
    o = np.lexsort((pos, blk))
    pb, pp = np.asarray(blk, int)[o], np.asarray(pos, float)[o]
    new = np.concatenate([[True], (pb[1:] != pb[:-1]) | (pp[1:] != pp[:-1])])
    ti = np.round(LGC.theta_col(pp[new], rc["N"])).astype(np.int64)
    seen = [set() for _ in range(m)]
    for b, t in zip(pb[new].tolist(), ti.tolist()):
        seen[b].add(int(t))
    h = 0
    for s in seen:
        if s:
            h += (max(s) - min(s) + 1) - len(s)
    return h


def row_empty_and_cap(rc):
    ev = LGC.eval_gap(rc)
    if ev["degenerate"] or ev.get("mx_mult", 0) > MSF.MULT_CAP:
        return None
    fr = MSF.frac_row(rc, ev)
    fl = fr["fl"]
    ns = list(fl["ndist"])
    m = len(ns)
    empties = [fl["sides"][i] - Fr(ns[i] + ns[i + 1], 2)
               for i in range(m - 1)]
    return dict(fr=fr, fl=fl, ns=ns, empties=empties, m=m,
                holes=hull_holes(rc, m, fl),
                n_emp=sum(1 for e in empties if e != 0),
                n_viol=len(fr["cap_viol"]))


# G9 chi4 kz53
u4, w4c, _nn, _ch = DMF.chi_window_comb(53, MSF.Q_CHI4)
pk = DMF.chi_wpack(53, 1.0, MSF.LPQ4, (u4, w4c))
rc53 = DSW.rung_rec(pk)
st53 = row_empty_and_cap(rc53)
floor_i = [i for i, g in enumerate(st53["fr"]["gfr"]) if g == Fr(3, 8)]
pref = st53["ns"][:6]
check("G9-kz53-saturating-prefix",
      st53 is not None and st53["n_emp"] == 0 and st53["holes"] == 0
      and st53["n_viol"] == 0
      and floor_i == [0, 1]
      and pref == [1, 2, 6, 5, 4, 4]
      and st53["fr"]["med"][0] == Fr(4)
      and st53["fr"]["sep_min"][0] == Fr(3, 2)
      and st53["fr"]["gfr"][0] == Fr(3, 8),
      "m=%d empty_nz=%d holes=%d floor_i=%s n[:6]=%s med0=%s g0=%s"
      % (st53["m"], st53["n_emp"], st53["holes"], floor_i, pref,
         st53["fr"]["med"][0], st53["fr"]["gfr"][0]))

# G10 four w9 worlds tiled
w9 = []
# FRAME A
w9.append(("FRAME_A", DSW.rung_rec(BH.wpack(9))))
# FRAME B
w9.append(("FRAME_B", DSW.rung_rec(SFE.wpack_b(9, MSF.NU_B))))
# CHI3 / CHI4
for lab, q, lpq in (("CHI3", MSF.Q_CHI3, MSF.LPQ3),
                    ("CHI4", MSF.Q_CHI4, MSF.LPQ4)):
    u, wc, _nn, _ch = DMF.chi_window_comb(9, q)
    w9.append((lab, DSW.rung_rec(DMF.chi_wpack(9, 1.0, lpq, (u, wc)))))

det = []
ok10 = True
for lab, rc in w9:
    st = row_empty_and_cap(rc)
    if st is None:
        ok10 = False
        det.append("%s degenerate" % lab)
        continue
    bit = (st["n_emp"] == 0 and st["holes"] == 0 and st["n_viol"] == 0)
    ok10 = ok10 and bit
    det.append("%s m=%d empty_nz=%d holes=%d viol=%d" %
               (lab, st["m"], st["n_emp"], st["holes"], st["n_viol"]))
check("G10-w9-four-worlds-tiled", ok10, "; ".join(det))

section("SUMMARY")
n_ok = sum(1 for _n, o in CHECKS if o)
n_all = len(CHECKS)
print("  %d/%d gates" % (n_ok, n_all))
if n_ok == n_all:
    print("MEDCAP STEPS VERIFIED")
    sys.exit(0)
print("MEDCAP STEPS FAILED")
sys.exit(1)
