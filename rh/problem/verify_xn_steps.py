#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_xn_steps.py -- machine check of every numbered lemma
in rh/problem/xn_invariant.tex.

PART A (STANDALONE): pairing combinatorics and interval geometry.
  G1  n=1 occurs only as an odd tail of a length-1 run
  G2  prefixes (2,1) and (1,1) are impossible
  G3  the unique possible sep=3/2 locus is the theta-edge (1,2)
  G4  C2 n=(1,2,8^10) still violates (ratio 16/3) -- pairing does
      not forbid C2 by itself
  G5  short C2 (1,2,6,6,6,6) violates (third=6)
  G6  saturating (1,2,6,5,4,4) and single-spike (1,2,7,4,4,4)
      hold with third=4, ratio 8/3
  G7  random paired run sequences still produce MED-CAP violators
  G8  a Chebyshev (uniform-in-theta) colouring after an x-mask
      produces no C2 and no (1,2)

PART B (CONSTRUCTION CROSS-CHECK, repo builders):
  G9  sign(ct) = sign(bw)*sign(x)*sign(v2) on four w9 + chi4 kz53
  G10 n_i equals the smooth-border grid occupation (window atoms
      add 0 cells) and equals paired sign-run grid lengths
  G11 n=1 lives only at theta-index 0; four w9 worlds have no
      (1,2) prefix (hence no sep=3/2)
  G12 chi4 kz53 realises the unique (1,2) of the deep pin, prefix
      (1,2,6,5,4,4,4,8), third-smallest=4, nearest n>=7 at index 7

Exit: per-gate PASS/FAIL and the final line
"XN STEPS VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named remainder only.
"""
from __future__ import annotations

import math
import os
import random
import sys
from collections import Counter
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
RNG = random.Random(364)


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 72)
    print(t)
    print("=" * 72, flush=True)


def pack_from_n(ns):
    m = len(ns)
    sb = [Fr(ns[i] + ns[i + 1], 2) for i in range(m - 1)]
    d = list(sb)
    gaps = [d[0]] + [min(d[i - 1], d[i])
                     for i in range(1, m - 1)] + [d[-1]]
    seps = [sb[0]] + [min(sb[i - 1], sb[i])
                      for i in range(1, m - 1)] + [sb[-1]]
    med = []
    for i in range(m):
        lo, hi = max(0, i - W), min(m, i + W + 1)
        nb = sorted(gaps[j] for j in range(lo, hi) if j != i)
        k = len(nb)
        med.append(nb[k // 2] if k % 2
                   else (nb[k // 2 - 1] + nb[k // 2]) / 2)
    viol = [i for i in range(m) if med[i] > CAP * seps[i]]
    return dict(gaps=gaps, seps=seps, med=med, viol=viol,
                worst=max((med[i] / seps[i] for i in range(m)),
                          default=Fr(0)))


def pair_runs(run_lens):
    """Pair consecutive run lengths from the start of the list
    (x-min); odd tail its own block.  Theta order reverses, so
    the odd tail (x-max) becomes index 0."""
    nr = len(run_lens)
    ns_x = []
    i = 0
    while i < nr:
        if i + 1 < nr:
            ns_x.append(run_lens[i] + run_lens[i + 1])
            i += 2
        else:
            ns_x.append(run_lens[i])
            i += 1
    return ns_x, list(reversed(ns_x)), (nr % 2 == 1)


def small_sep_indices(ns):
    m = len(ns)
    if m < 2:
        return []
    sb = [(ns[i] + ns[i + 1]) / 2.0 for i in range(m - 1)]
    seps = [sb[0]] + [min(sb[i - 1], sb[i])
                      for i in range(1, m - 1)] + [sb[-1]]
    return [i for i, s in enumerate(seps) if s <= 1.5]


def chebyshev_runs_xmask(T, mdeg, mask_frac=0.20):
    """sign(sin(mdeg * theta)) on a uniform theta-grid of T cells,
    drop an x-mask of fraction mask_frac of the hull [-1,1] (so
    keep x in [-1+2f, 1-2f]).  Return run lengths in t-order."""
    lo_x = -1.0 + 2.0 * mask_frac
    hi_x = 1.0 - 2.0 * mask_frac
    sig = []
    for t in range(T):
        th = math.pi * (t + 0.5) / T
        x = math.cos(th)
        if x < lo_x or x > hi_x:
            continue
        s = math.sin(mdeg * th)
        sig.append(1 if s >= 0 else -1)
    if not sig:
        return []
    runs = []
    start = 0
    cur = sig[0]
    for i in range(1, len(sig)):
        if sig[i] != cur:
            runs.append(i - start)
            start = i
            cur = sig[i]
    runs.append(len(sig) - start)
    return runs


def main():
    section("PART A  PAIRING COMBINATORICS")

    # G1-G3 random positive run sequences
    n_p12 = n_21 = n_11 = 0
    n_n1_off = 0
    n_small_not12 = 0
    n_checked = 0
    for _ in range(4000):
        nr = RNG.randint(3, 36)
        runs = [RNG.randint(1, 7) for _ in range(nr)]
        _nsx, ns, odd = pair_runs(runs)
        n_checked += 1
        n1 = [i for i, n in enumerate(ns) if n == 1]
        if any(i != 0 for i in n1):
            n_n1_off += 1
        if 0 in n1 and not (odd and runs[-1] == 1):
            n_n1_off += 1
        if len(ns) >= 2:
            if ns[0] == 1 and ns[1] == 2:
                n_p12 += 1
            if ns[0] == 2 and ns[1] == 1:
                n_21 += 1
            if ns[0] == 1 and ns[1] == 1:
                n_11 += 1
        for i in small_sep_indices(ns):
            if not (len(ns) >= 2 and ns[0] == 1 and ns[1] == 2
                    and i in (0, 1)):
                n_small_not12 += 1
    check("G1-n1-only-odd-tail",
          n_n1_off == 0,
          "%d sequences, n=1 off-tail = %d" % (n_checked, n_n1_off))
    check("G2-no-21-no-11",
          n_21 == 0 and n_11 == 0,
          "(1,2) %d, (2,1) %d, (1,1) %d" % (n_p12, n_21, n_11))
    check("G3-small-sep-only-edge-12",
          n_small_not12 == 0,
          "non-(1,2) small-sep loci %d" % n_small_not12)

    rC2 = pack_from_n([1, 2] + [8] * 10)
    check("G4-C2-still-violates",
          rC2["viol"][:2] == [0, 1] and rC2["worst"] == Fr(16, 3),
          "viol=%s worst=%s" % (rC2["viol"][:4], rC2["worst"]))

    rS = pack_from_n([1, 2, 6, 6, 6, 6])
    third_s = sorted(rS["gaps"][1:6])[2]
    check("G5-short-C2-third-6",
          0 in rS["viol"] and third_s == Fr(6)
          and rS["med"][0] / rS["seps"][0] == Fr(4),
          "third=%s ratio=%s" % (third_s, rS["med"][0] / rS["seps"][0]))

    rE = pack_from_n([1, 2, 6, 5, 4, 4])
    r7 = pack_from_n([1, 2, 7, 4, 4, 4])
    tE = sorted(rE["gaps"][1:6])[2]
    t7 = sorted(r7["gaps"][1:6])[2]
    check("G6-saturating-and-single-spike",
          rE["viol"] == [] and tE == Fr(4)
          and rE["med"][0] / rE["seps"][0] == CAP
          and r7["viol"] == [] and t7 == Fr(4)
          and r7["med"][0] / r7["seps"][0] == CAP,
          "eq third=%s spike third=%s (a single n=7 with return "
          "to 4 saturates, it does not violate)" % (tE, t7))

    nv = 0
    npr = 0
    for _ in range(1500):
        runs = [RNG.randint(1, 8) for _ in range(RNG.randint(8, 24))]
        _nsx, ns, _odd = pair_runs(runs)
        if len(ns) < 6:
            continue
        npr += 1
        if pack_from_n(ns)["viol"]:
            nv += 1
    check("G7-random-paired-still-violate",
          nv > 0,
          "%d/%d paired random run sequences violate MED-CAP"
          % (nv, npr))

    n_ch = n_ch_v = n_ch_12 = 0
    for T in range(50, 361, 10):
        for mdeg in (max(2, T // 3), T // 2 - 1, T // 2, T // 2 + 1):
            runs_t = chebyshev_runs_xmask(T, mdeg, 0.20)
            if len(runs_t) < 6:
                continue
            # x-order is reversed t-order (x = cos theta)
            _nsx, ns, _odd = pair_runs(list(reversed(runs_t)))
            if len(ns) < 6:
                continue
            n_ch += 1
            if pack_from_n(ns)["viol"]:
                n_ch_v += 1
            if ns[0] == 1 and ns[1] == 2:
                n_ch_12 += 1
    check("G8-chebyshev-no-C2",
          n_ch > 50 and n_ch_v == 0,
          "%d x-masked Chebyshev windows, (1,2) %d, viol %d"
          % (n_ch, n_ch_12, n_ch_v))

    section("PART B  CONSTRUCTION CROSS-CHECK")
    import numpy as np  # noqa: E402
    import mean_sieve_floor_probe as MSF  # noqa: E402
    import local_gap_carleson_probe as LGC  # noqa: E402
    import dirichlet_matched_frame_probe as DMF  # noqa: E402
    import dirichlet_secondworld_probe as DSW  # noqa: E402
    import bordered_hankel_probe as BH  # noqa: E402
    import second_family_erosion_probe as SFE  # noqa: E402
    import phase_bulk_bound_probe as PBB  # noqa: E402
    import window_border_transfer_probe as WBT  # noqa: E402
    import border_resolvent_identity_probe as BR  # noqa: E402

    def anatomy(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        bws = rc["bw"][o]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], DSW.EDGE_F)
        cb = cts[~ed]
        xb = bxs[~ed]
        wb = bws[~ed]
        runs = PBB.runs_split(cb)
        brk, m, jb = WBT.block_breaks(xb, runs)
        N = rc["N"]
        v2 = BR.eval_scaled(rc["p"]["rows"], rc["bx"], N - 2)[o][~ed]
        fac = math.exp(rc["p"]["rows"][N - 2]["Ls"]
                       - rc["p"]["rows"][N - 1]["Ls"]) \
            / math.sqrt(abs(rc["p"]["rows"][N - 1]["eta"]))
        prod = np.sign(wb) * np.sign(xb) * np.sign(v2) \
            * math.copysign(1.0, fac)
        n_dis = int(np.sum(prod != np.sign(cb)))
        edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], DSW.EDGE_F)
        xw = rc["xu"][~edw]
        jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
        pos_all = np.concatenate([xb, xw])
        blk_all = np.concatenate([jb, jw]).astype(int)
        fl = MSF.frac_center_ledger(pos_all, blk_all, m, N)
        ns = list(fl["ndist"])
        # smooth-only occupation in theta order
        fls = MSF.frac_center_ledger(xb, jb, m, N)
        ns_sm = list(fls["ndist"])
        # paired grid runs in x-order, reversed to theta
        ti = np.round(LGC.theta_col(xb, N)).astype(np.int64)
        rg = []
        for a, b, _s in runs:
            rg.append(len(set(int(t) for t in ti[a:b].tolist())))
        _nsx, ns_pr, odd = pair_runs(rg)
        n1 = [i for i, n in enumerate(ns) if n == 1]
        r = pack_from_n(ns)
        ge7 = [i for i, n in enumerate(ns) if n >= 7]
        third = sorted(r["gaps"][1:6])[2] if m >= 6 else None
        return dict(ns=ns, ns_sm=ns_sm, ns_pr=ns_pr, odd=odd,
                    n_dis=n_dis, n_bulk=len(cb), n1=n1, m=m, nr=len(runs),
                    r=r, ge7=ge7, third=third, pref=ns[:8])

    worlds = []
    worlds.append(("FRAME_A_w9", DSW.rung_rec(BH.wpack(9))))
    worlds.append(("FRAME_B_w9",
                   DSW.rung_rec(SFE.wpack_b(9, MSF.NU_B))))
    for lab, q, lpq in (("CHI3_w9", MSF.Q_CHI3, MSF.LPQ3),
                        ("CHI4_w9", MSF.Q_CHI4, MSF.LPQ4)):
        u, wc, _nn, _ch = DMF.chi_window_comb(9, q)
        worlds.append((lab, DSW.rung_rec(
            DMF.chi_wpack(9, 1.0, lpq, (u, wc)))))
    u4, w4c, _nn, _ch = DMF.chi_window_comb(53, MSF.Q_CHI4)
    worlds.append(("CHI4_kz53", DSW.rung_rec(
        DMF.chi_wpack(53, 1.0, MSF.LPQ4, (u4, w4c)))))

    an = [(lab, anatomy(rc)) for lab, rc in worlds]

    ok_sign = all(st["n_dis"] == 0 for _l, st in an)
    check("G9-sign-ct-equals-bw-x-v2",
          ok_sign,
          "; ".join("%s dis=%d/%d" % (lab, st["n_dis"], st["n_bulk"])
                    for lab, st in an))

    ok_occ = all(st["ns"] == st["ns_sm"] == st["ns_pr"] for _l, st in an)
    check("G10-n-equals-paired-smooth-grid",
          ok_occ,
          "; ".join("%s m=%d n[:4]=%s" % (lab, st["m"], st["ns"][:4])
                    for lab, st in an))

    n1_off = [(lab, st["n1"]) for lab, st in an
              if any(i != 0 for i in st["n1"])]
    w9 = [(lab, st) for lab, st in an if lab != "CHI4_kz53"]
    p12_w9 = [lab for lab, st in w9
              if len(st["ns"]) >= 2 and st["ns"][0] == 1
              and st["ns"][1] == 2]
    small_w9 = sum(len(small_sep_indices(st["ns"])) for _l, st in w9)
    check("G11-n1-at-0-and-w9-no-12",
          n1_off == [] and p12_w9 == [] and small_w9 == 0,
          "n1-off=%s w9-(1,2)=%s w9-small-sep=%d; w9 prefixes %s"
          % (n1_off, p12_w9, small_w9,
             {lab: st["pref"] for lab, st in w9}))

    st53 = dict(an)["CHI4_kz53"]
    r53 = st53["r"]
    ge7 = st53["ge7"]
    d0 = min(abs(0 - j) for j in ge7) if ge7 else None
    check("G12-kz53-unique-12-saturates",
          st53["pref"][:6] == [1, 2, 6, 5, 4, 4]
          and st53["ns"][0] == 1 and st53["ns"][1] == 2
          and st53["third"] == Fr(4)
          and r53["viol"] == []
          and r53["med"][0] / r53["seps"][0] == CAP
          and ge7 and min(ge7) == 7 and d0 == 7,
          "pref=%s third=%s ratio=%s ge7[0]=%s dist0=%s"
          % (st53["pref"], st53["third"],
             r53["med"][0] / r53["seps"][0],
             min(ge7) if ge7 else None, d0))

    section("SUMMARY")
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("XN STEPS VERIFIED")
        return 0
    print("XN STEPS FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
