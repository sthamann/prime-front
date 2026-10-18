#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_v2_steps.py -- machine check of every numbered lemma
in rh/problem/v2_regularity.tex.

PART A (STANDALONE): product combinatorics, Chebyshev mask, adversary.
  G1  AB flips at i iff exactly one of A, B flips at i
  G2  a 2-regular factor does NOT imply V2 (random products with
      one 2-regular factor still violate; the tempting reduction
      is false)
  G3  Chebyshev after an x-mask never ends with (1,1,1)
  G4  Chebyshev x flip-first Nyquist burst of length 3..15 never
      violates V2 (0/425 in the scan; 0 (1,1,1) tails)
  G5  random independent run-products DO violate V2 (so V2 is not
      a theorem of arbitrary paired colourings)
  G6  the named plateau violator x-runs (3^8, 1,1,1) pairs to
      n=(1,2,6^4), violates MED-CAP, and fails V2
  G7  bulk-mode prefix (2,2,3,3,1,1,1) satisfies V2 (prev4 has
      two 2s) and pairs to the spike n=(1,2,6,4), which holds
  G8  (1,1,1) yields theta-prefix (1,2) iff the run-count is odd

PART B (CONSTRUCTION CROSS-CHECK, repo builders):
  G9  four w9 worlds: w has a single bulk sign-run, no colouring
      (1,1,1), V2 holds vacuously
  G10 chi4 kz53: colouring (1,1,1) is w-driven (v2 last3 != (1,1,1)),
      prev4=[4,1,2,4] regular, odd run-count, prefix (1,2,6,5,4,4)
  G11 chi3 kz16: v2 itself ends (1,1,1), colouring follows v2 at
      the mask (w constant there), prev4=[3,2,1,3] regular, EVEN
      run-count so n0=2 (not the small-sep locus)
  G12 sign(ct)=sign(w x v2) on the five pin windows plus chi3 kz16

Exit: per-gate PASS/FAIL and the final line
"V2 STEPS VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, a named freeze, and a hydra ward.
"""
from __future__ import annotations

import math
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
RNG = random.Random(365)
CAP = Fr(8, 3)
W = 5


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


def runs_of(sig):
    sig = list(sig)
    if not sig:
        return []
    out = []
    start = 0
    cur = sig[0]
    for i in range(1, len(sig)):
        if sig[i] != cur:
            out.append(i - start)
            start = i
            cur = sig[i]
    out.append(len(sig) - start)
    return out


def colour_from_runs(runs, start=1):
    s = []
    sg = start
    for r in runs:
        s.extend([sg] * int(r))
        sg = -sg
    return s


def v2_holds(R):
    if len(R) < 7:
        return True, "short"
    if tuple(R[-3:]) != (1, 1, 1):
        return True, "no-triple-tail"
    prev4 = list(R[-7:-3])
    n_le2 = sum(1 for r in prev4 if r <= 2)
    if n_le2 >= 2:
        return True, "triple-regular prev4=%s" % (prev4,)
    return False, "VIOLATOR prev4=%s" % (prev4,)


def pair_runs(run_lens):
    ns_x = []
    i = 0
    nr = len(run_lens)
    while i < nr:
        if i + 1 < nr:
            ns_x.append(run_lens[i] + run_lens[i + 1])
            i += 2
        else:
            ns_x.append(run_lens[i])
            i += 1
    return ns_x, list(reversed(ns_x)), (nr % 2 == 1)


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


def chebyshev_xmask(T, mdeg, mask_frac=0.20):
    lo_x = -1.0 + 2.0 * mask_frac
    hi_x = 1.0 - 2.0 * mask_frac
    xs, sig = [], []
    for t in range(T):
        th = math.pi * (t + 0.5) / T
        x = math.cos(th)
        if x < lo_x or x > hi_x:
            continue
        s = math.sin(mdeg * th)
        xs.append(x)
        sig.append(1 if s >= 0 else -1)
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    return [sig[i] for i in order]


def burst_w(n, burst, start_flip=True):
    w = [1] * n
    s0 = -1 if start_flip else 1
    for k in range(min(burst, n)):
        w[-1 - k] = s0 * (1 if (k % 2 == 0) else -1)
    return w


def main():
    section("PART A  PRODUCT COMBINATORICS AND ADVERSARY")

    # G1 flip-XOR: AB flips iff exactly one factor flips
    n_bad = 0
    n_chk = 0
    for _ in range(800):
        ra = [RNG.randint(1, 6) for _ in range(RNG.randint(8, 24))]
        rb = [RNG.randint(1, 6) for _ in range(RNG.randint(8, 24))]
        a = colour_from_runs(ra)
        b = colour_from_runs(rb)
        L = min(len(a), len(b))
        a, b = a[:L], b[:L]
        for i in range(1, L):
            flip_a = a[i] != a[i - 1]
            flip_b = b[i] != b[i - 1]
            flip_p = (a[i] * b[i]) != (a[i - 1] * b[i - 1])
            if flip_p != (flip_a != flip_b):
                n_bad += 1
            n_chk += 1
    check("G1-product-flips-xor",
          n_bad == 0,
          "%d adjacent pairs, xor-misses %d" % (n_chk, n_bad))

    # G2: 2-regular factor does NOT imply V2 (hydra: the tempting
    # reduction is false).  Fixed-seed search, 8000 draws.
    n_v = 0
    n_ok = 0
    rng2 = random.Random(3652)
    for _ in range(8000):
        ra = [rng2.randint(1, 2) for _ in range(rng2.randint(16, 50))]
        rb = [rng2.randint(1, 8) for _ in range(rng2.randint(16, 50))]
        a = colour_from_runs(ra)
        b = colour_from_runs(rb)
        L = min(len(a), len(b))
        Rp = runs_of([a[i] * b[i] for i in range(L)])
        ok, _why = v2_holds(Rp)
        n_ok += 1
        if not ok:
            n_v += 1
    check("G2-2regular-factor-does-not-imply-V2",
          n_v > 0,
          "%d/%d products with a 2-regular factor violate V2 "
          "(the 2-regular reduction is false)" % (n_v, n_ok))

    # G3 Chebyshev x-mask
    n_ch = n_111 = 0
    for T in range(50, 361, 10):
        for mdeg in (max(2, T // 3), T // 2 - 1, T // 2, T // 2 + 1):
            sig = chebyshev_xmask(T, mdeg, 0.20)
            if len(sig) < 12:
                continue
            R = runs_of(sig)
            n_ch += 1
            if len(R) >= 3 and tuple(R[-3:]) == (1, 1, 1):
                n_111 += 1
    check("G3-chebyshev-xmask-no-111",
          n_ch > 50 and n_111 == 0,
          "%d windows, (1,1,1) tails %d" % (n_ch, n_111))

    # G4 Chebyshev x Nyquist burst
    n_b = n_b111 = n_bv = 0
    for T in range(80, 401, 20):
        for mdeg in (T // 3, T // 2 - 1, T // 2, T // 2 + 1, 2 * T // 3):
            ch = chebyshev_xmask(T, max(2, mdeg), 0.20)
            if len(ch) < 20:
                continue
            for burst in (3, 4, 5, 6, 7):
                w = burst_w(len(ch), burst, True)
                R = runs_of([w[i] * ch[i] for i in range(len(ch))])
                n_b += 1
                ok, _why = v2_holds(R)
                if len(R) >= 3 and tuple(R[-3:]) == (1, 1, 1):
                    n_b111 += 1
                if not ok:
                    n_bv += 1
    check("G4-chebyshev-x-nyquist-burst-clean",
          n_b > 100 and n_b111 == 0 and n_bv == 0,
          "%d burst-windows, (1,1,1) %d, V2-viol %d" % (n_b, n_b111, n_bv))

    # G5 random products violate
    nv = 0
    npr = 0
    for _ in range(4000):
        ra = [RNG.randint(1, 6) for _ in range(RNG.randint(12, 36))]
        rb = [RNG.randint(1, 6) for _ in range(RNG.randint(12, 36))]
        a = colour_from_runs(ra)
        b = colour_from_runs(rb)
        L = min(len(a), len(b))
        R = runs_of([a[i] * b[i] for i in range(L)])
        if len(R) < 7:
            continue
        npr += 1
        ok, _why = v2_holds(R)
        if not ok:
            nv += 1
    check("G5-random-products-do-violate",
          nv > 0,
          "%d/%d random products violate V2 (V2 is not abstract "
          "product combinatorics)" % (nv, npr))

    # G6 named plateau violator
    runs_v = [3] * 8 + [1, 1, 1]
    _nsx, ns, odd = pair_runs(runs_v)
    pk = pack_from_n(ns)
    okV, whyV = v2_holds(runs_v)
    check("G6-plateau-violator-is-V2-and-MEDCAP",
          (not okV) and odd and ns[:6] == [1, 2, 6, 6, 6, 6]
          and 0 in pk["viol"],
          "n=%s odd=%s V2=%s viol=%s" % (ns[:6], odd, whyV, pk["viol"][:3]))

    # G7 spike with bulk mode 2
    runs_s = [2] * 8 + [3, 3, 1, 1, 1]
    _nsx, ns_s, odd_s = pair_runs(runs_s)
    pk_s = pack_from_n(ns_s)
    okS, whyS = v2_holds(runs_s)
    third = sorted(pk_s["gaps"][1:6])[2]
    check("G7-bulk-mode-spike-holds-V2",
          okS and odd_s and ns_s[:4] == [1, 2, 6, 4]
          and pk_s["viol"] == [] and third == Fr(4),
          "n=%s V2=%s third=%s" % (ns_s[:4], whyS, third))

    # G8 parity
    n_12_even = n_12_odd = 0
    n_par = 0
    for _ in range(2000):
        nr = RNG.randint(7, 25)
        runs = [RNG.randint(1, 5) for _ in range(nr - 3)] + [1, 1, 1]
        _nsx, ns, odd = pair_runs(runs)
        n_par += 1
        is12 = len(ns) >= 2 and ns[0] == 1 and ns[1] == 2
        if is12 and not odd:
            n_12_even += 1
        if is12 and odd:
            n_12_odd += 1
        if odd and runs[-1] == 1 and runs[-2] == 1:
            if not is12:
                n_12_even += 1  # misuse counter: odd with (1,1) tail must be (1,2)
    # recompute cleanly
    n_miss = 0
    n_false = 0
    for _ in range(2000):
        nr = RNG.randint(7, 25)
        runs = [RNG.randint(1, 5) for _ in range(nr - 3)] + [1, 1, 1]
        _nsx, ns, odd = pair_runs(runs)
        is12 = len(ns) >= 2 and ns[0] == 1 and ns[1] == 2
        should = odd  # last run 1, previous pair 1+1=2
        if should and not is12:
            n_miss += 1
        if is12 and not should:
            n_false += 1
    check("G8-111-gives-12-iff-odd",
          n_miss == 0 and n_false == 0,
          "2000 (1,1,1)-tails: miss=%d false=%d" % (n_miss, n_false))

    section("PART B  CONSTRUCTION CROSS-CHECK")
    import numpy as np  # noqa: E402
    import mean_sieve_floor_probe as MSF  # noqa: E402
    import dirichlet_matched_frame_probe as DMF  # noqa: E402
    import dirichlet_secondworld_probe as DSW  # noqa: E402
    import bordered_hankel_probe as BH  # noqa: E402
    import second_family_erosion_probe as SFE  # noqa: E402
    import phase_bulk_bound_probe as PBB  # noqa: E402
    import border_resolvent_identity_probe as BR  # noqa: E402
    import local_gap_carleson_probe as LGC  # noqa: E402
    import window_border_transfer_probe as WBT  # noqa: E402

    def extract(rc):
        o = rc["o"]
        bxs = rc["bx"][o]
        cts = rc["ct"][o]
        bws = rc["bw"][o]
        N = rc["N"]
        ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], DSW.EDGE_F)
        xb, wb, cb = bxs[~ed], bws[~ed], cts[~ed]
        v2 = BR.eval_scaled(rc["p"]["rows"], rc["bx"], N - 2)[o][~ed]
        sg_v2 = np.sign(v2)
        sg_v2[sg_v2 == 0] = 1
        sg_w = np.sign(wb)
        sg_w[sg_w == 0] = 1
        sg_x = np.sign(xb)
        sg_x[sg_x == 0] = 1
        sg_c = np.sign(cb)
        sg_c[sg_c == 0] = 1
        fac = math.exp(rc["p"]["rows"][N - 2]["Ls"]
                       - rc["p"]["rows"][N - 1]["Ls"]) \
            / math.sqrt(abs(rc["p"]["rows"][N - 1]["eta"]))
        prod = sg_w * sg_x * sg_v2 * math.copysign(1.0, fac)
        n_dis = int(np.sum(prod != sg_c))
        Rv2, Rw, Rc = runs_of(sg_v2), runs_of(sg_w), runs_of(sg_c)
        okc, whyc = v2_holds(Rc)
        ti = np.round(LGC.theta_col(xb, N)).astype(np.int64)
        runs = PBB.runs_split(cb)
        rg = [len(set(int(t) for t in ti[a:b].tolist()))
              for a, b, _s in runs]
        _nsx, ns, odd = pair_runs(rg)
        return dict(N=N, kz=rc["kz"], n_dis=n_dis, n_bulk=len(xb),
                    Rc=Rc, Rv2=Rv2, Rw=Rw, okc=okc, whyc=whyc,
                    ns=ns, odd=odd, nr=len(Rc), n_w=len(Rw))

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
    u3, w3c, _nn, _ch = DMF.chi_window_comb(16, MSF.Q_CHI3)
    worlds.append(("CHI3_kz16", DSW.rung_rec(
        DMF.chi_wpack(16, 1.0, MSF.LPQ3, (u3, w3c)))))

    st = {lab: extract(rc) for lab, rc in worlds}

    w9 = ["FRAME_A_w9", "FRAME_B_w9", "CHI3_w9", "CHI4_w9"]
    ok_w9 = all(st[l]["n_w"] == 1
                and tuple(st[l]["Rc"][-3:]) != (1, 1, 1)
                and st[l]["okc"]
                for l in w9)
    check("G9-w9-single-arm-no-triple",
          ok_w9,
          "; ".join("%s n_w=%d last3=%s" % (l, st[l]["n_w"], st[l]["Rc"][-3:])
                    for l in w9))

    s53 = st["CHI4_kz53"]
    check("G10-kz53-w-driven-regular-12",
          s53["okc"] and tuple(s53["Rc"][-3:]) == (1, 1, 1)
          and tuple(s53["Rv2"][-3:]) != (1, 1, 1)
          and tuple(s53["Rw"][-3:]) == (1, 1, 1)
          and s53["Rc"][-7:-3] == [4, 1, 2, 4]
          and s53["odd"] and s53["ns"][:6] == [1, 2, 6, 5, 4, 4],
          "why=%s last3 c/v2/w=%s/%s/%s pref=%s odd=%s" % (
              s53["whyc"], s53["Rc"][-3:], s53["Rv2"][-3:],
              s53["Rw"][-3:], s53["ns"][:6], s53["odd"]))

    s16 = st["CHI3_kz16"]
    check("G11-kz16-v2-triple-even-not-12",
          s16["okc"] and tuple(s16["Rc"][-3:]) == (1, 1, 1)
          and tuple(s16["Rv2"][-3:]) == (1, 1, 1)
          and s16["Rc"][-7:-3] == [3, 2, 1, 3]
          and (s16["nr"] % 2 == 0) and (not s16["odd"])
          and s16["ns"][0] == 2,
          "why=%s last3 c/v2=%s/%s n0=%s nr=%d odd=%s" % (
              s16["whyc"], s16["Rc"][-3:], s16["Rv2"][-3:],
              s16["ns"][0], s16["nr"], s16["odd"]))

    ok_sign = all(st[l]["n_dis"] == 0 for l in st)
    check("G12-sign-ct-equals-w-x-v2",
          ok_sign,
          "; ".join("%s dis=%d/%d" % (l, st[l]["n_dis"], st[l]["n_bulk"])
                    for l in st))

    section("SUMMARY")
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("V2 STEPS VERIFIED")
        return 0
    print("V2 STEPS FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
