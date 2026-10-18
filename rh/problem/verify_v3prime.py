#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_v3prime.py -- machine check of every numbered lemma
in rh/problem/v3prime_proof.tex (round 379, V3' reduced to G_eps).

PART A (STANDALONE):
  G1  L = 4h-2 from M=2h, L=2M-2 (integer identity)
  G2  Jacobi-(0,1) |g-1/4| = 1/(4(2n+1)^2) over Q
  G3  Chebyshev monic: g1=1/2, gk=1/4 (k>=2)
  G4  WKB band at x=3/5, eps=1/16 sits in (1.2, 2.1)
  G5  two-period about pi/2, a<=0.85: 0 A15-violators
  G6  constant pi/2: 0 violators (r374 regression)
  G7  contrast: (0.4^21, 2.8^3) violates; (1.0^21, 2.0^3) not
  G8  interleaved two-period a=0.70 in A15; blocked rearrangement
      of the same two values leaves A15

PART B (CONSTRUCTION PINS):
  G10 mask Delta-theta ratio == 1 (fold-gap constant)
  G11 G_eps on pins: last12 |g-1/4|<=1/16, jump<=2/5
  G12 Path A: last-14 steps in A15 (0 eta-violators)
  G13 +x mask x>0 on last 9 bulk nodes
  G14 equal-weight occupied cosine grid: Chebyshev gamma
  G15 coherent last-12 scale: 1.5 in A15, 2.0 leaves, 8 v2-viol
  G16 kz46 step-ratio >5, still in A15
  G17 chi3 kz16 eta-111s all V2-regular

PART C (--full):
  G20 181-window census: G_eps + Delta-theta ratio 1 + A15

Exit: per-gate PASS/FAIL and the final line
"V3PRIME LEMMA VERIFIED" iff every (selected) gate passed.

NO RH CLAIM.  Finite identities and a named reduction.
"""
from __future__ import annotations

import argparse
import math
import os
import sys
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
VERIFY = os.path.join(REPO, "verification")
for p in (DISC, VERIFY):
    if p not in sys.path:
        sys.path.insert(0, p)

CHECKS = []
EPS0 = Fr(1, 16)
JUMP0 = Fr(2, 5)
EPS0_F = float(EPS0)
JUMP0_F = float(JUMP0)


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


def runs_of_sign(sig):
    sg = np.sign(np.asarray(sig, float))
    out, start, cur = [], 0, 0.0
    n = len(sg)
    for i in range(n):
        s = float(sg[i])
        if s == 0.0:
            continue
        if cur == 0.0:
            cur, start = s, i
        elif s != cur:
            out.append(i - start)
            start, cur = i, s
    if n:
        out.append(n - start)
    return out


def runs_of_levels(lev):
    lev = [int(v) for v in lev]
    if not lev:
        return []
    out, start, cur = [], 0, lev[0]
    for i in range(1, len(lev)):
        if lev[i] != cur:
            out.append(i - start)
            start, cur = i, lev[i]
    out.append(len(lev) - start)
    return out


def v2_holds(R):
    R = [int(v) for v in R]
    if len(R) < 7:
        return True, "short"
    if tuple(R[-3:]) != (1, 1, 1):
        return True, "no-triple-tail"
    prev4 = list(R[-7:-3])
    n_le2 = sum(1 for r in prev4 if r <= 2)
    if n_le2 >= 2:
        return True, "triple-regular prev4=%s" % (prev4,)
    return False, "VIOLATOR prev4=%s" % (prev4,)


def occupancy(dth, eta):
    th = float(eta)
    levs = [int(math.floor(th / math.pi))]
    for d in dth:
        th += float(d)
        levs.append(int(math.floor(th / math.pi)))
    return runs_of_levels(levs)


def scan_eta(dth, n_eta=1001):
    n111 = nviol = nreg = 0
    prevs = set()
    for eta in np.linspace(0.0, math.pi, n_eta, endpoint=False):
        R = occupancy(dth, eta)
        ok, _why = v2_holds(R)
        if len(R) >= 3 and tuple(R[-3:]) == (1, 1, 1):
            n111 += 1
            if not ok:
                nviol += 1
            else:
                nreg += 1
                if len(R) >= 7:
                    prevs.add(tuple(R[-7:-3]))
        elif not ok:
            nviol += 1
    return n111, nviol, nreg, prevs


def wkb_ratio(x, gam):
    a = math.sqrt(max(1.0 - x * x, 1e-30))
    b = math.sqrt(max(4.0 * gam - x * x, 1e-30))
    return a / b


def chain_pair(rows, pts, deg):
    import source_prufer_one_defect_probe as SP
    pts = np.asarray(pts, float)
    v = np.ones_like(pts)
    vm = np.zeros_like(pts)
    theta = np.full_like(pts, 0.5 * math.pi)
    phi_prev = theta.copy()
    for k in range(int(deg)):
        alh = rows[k]["alh"]
        if k == 0:
            px = (pts - alh) * v
        else:
            gam = rows[k - 1]["gam_next"]
            fc = math.exp(rows[k - 1]["Ls"] - rows[k]["Ls"])
            px = (pts - alh) * v - gam * fc * vm
        vm = v
        v = px * math.exp(rows[k]["Ls"] - rows[k + 1]["Ls"])
        phi = np.arctan2(v, vm)
        delta = phi - phi_prev
        delta = (delta + math.pi) % (2.0 * math.pi) - math.pi
        theta = theta + delta
        phi_prev = phi
    th = SP.unwrap_x(theta)
    dth = np.diff(th)
    dth = (dth + math.pi) % (2.0 * math.pi) - math.pi
    if float(np.sum(dth)) < 0:
        dth = -dth
    return v, vm, th, dth


def bulk_of(rc):
    import phase_bulk_bound_probe as PBB
    import dirichlet_secondworld_probe as DSW
    o = rc["o"]
    bxs = rc["bx"][o]
    cts = rc["ct"][o]
    ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], DSW.EDGE_F)
    return (rc["N"], bxs[~ed], cts[~ed], rc["p"]["rows"], rc["kz"],
            rc["lo"], rc["hi"])


def gamma_scale_rows(rows, scale, n_last, n):
    out = [dict(r) for r in rows]
    for k in range(max(0, n - n_last), n):
        if out[k].get("gam_next") is not None:
            out[k]["gam_next"] = float(out[k]["gam_next"]) * scale
    return out


def gams_of(rows, n):
    g, a = [], []
    for k in range(n):
        if rows[k].get("gam_next") is not None:
            g.append(float(rows[k]["gam_next"]))
        if rows[k].get("alh") is not None:
            a.append(float(rows[k]["alh"]))
    return np.array(g, float), np.array(a, float)


def analyze_rc(lab, rc, n_eta=1001):
    N, xb, cb, rows, kz, lo, hi = bulk_of(rc)
    n = N - 2
    v, vm, th, dth = chain_pair(rows, xb, n)
    g, a = gams_of(rows, n)
    Lwin = 15
    d_tail = dth[-(Lwin - 1):] if len(dth) >= Lwin - 1 else dth
    xb_tail = xb[-Lwin:] if len(xb) >= Lwin else xb
    thx = np.arccos(np.clip(xb_tail, -1.0, 1.0))
    dthx = np.abs(np.diff(thx))
    dthx_ratio = (float(np.max(dthx) / np.min(dthx))
                  if len(dthx) and np.min(dthx) > 0 else float("nan"))
    last12 = g[-12:] if len(g) >= 12 else g
    last3 = g[-3:] if len(g) >= 3 else g
    dcheb12 = float(np.max(np.abs(last12 - 0.25))) if len(last12) else 0.0
    dcheb3 = float(np.max(np.abs(last3 - 0.25))) if len(last3) else 0.0
    if len(last12) >= 2 and np.all(last12 > 0):
        gjump = float(np.max(np.abs(np.log(last12[1:] / last12[:-1]))))
    else:
        gjump = float("nan")
    n111, nviol, nreg, prevs = scan_eta(d_tail, n_eta=n_eta)
    Rv = runs_of_sign(np.sign(v))
    return dict(
        lab=lab, kz=kz, N=N, n=n, xb=xb, rows=rows, g=g, a=a,
        d_tail=d_tail, dthx_ratio=dthx_ratio, dcheb12=dcheb12,
        dcheb3=dcheb3, gjump=gjump, n111=n111, nviol=nviol,
        nreg=nreg, prevs=prevs, v=v, okv=v2_holds(Rv), Rv=Rv,
        x_last9=xb[-9:] if len(xb) >= 9 else xb,
        lo=lo, hi=hi,
    )


def equal_weight_gamma(xs, n_upto=40):
    pts = np.sort(np.asarray(xs, float))
    w = np.ones_like(pts)
    q = np.ones_like(pts)
    qm = np.zeros_like(pts)
    h = float(np.sum(w * q * q))
    g_eq, a_eq = [], []
    n_upto = min(n_upto, len(pts) - 2)
    for k in range(n_upto):
        alh = float(np.sum(w * pts * q * q)) / h
        a_eq.append(alh)
        if k == 0:
            px = (pts - alh) * q
        else:
            px = (pts - alh) * q - (h / h_m) * qm
        qm = q
        q = px
        h_m = h
        h = float(np.sum(w * q * q))
        g_eq.append(h / h_m)
    return np.array(g_eq), np.array(a_eq)


def part_a():
    section("PART A  MESH IDENTITY, FEJER, A15 NEIGHBOURHOOD")

    n_bad = 0
    n_chk = 0
    for h in (92, 142, 184, 203, 210, 285, 344, 371, 434, 606,
              1721, 2684, 3027, 3181):
        M = 2 * h
        L = 2 * M - 2
        n_chk += 1
        if L != 4 * h - 2 or M != 2 * h:
            n_bad += 1
    check("G1-L-equals-4h-minus-2",
          n_bad == 0 and n_chk >= 10,
          "%d integer triples M=2h, L=2M-2=4h-2, misses %d"
          % (n_chk, n_bad))

    n_bad = 0
    for n in range(1, 80):
        num = Fr(n) * Fr(n + 1)
        den = Fr(2 * n + 1) ** 2
        g = num / den
        err = abs(g - Fr(1, 4))
        pred = Fr(1, 4) / (Fr(2 * n + 1) ** 2)
        if err != pred:
            n_bad += 1
    check("G2-jacobi-0-1-fejer-Q",
          n_bad == 0,
          "n=1..79 exact |g-1/4|=1/(4(2n+1)^2), misses %d" % n_bad)

    # monic Chebyshev on [-1,1]: T0=1, T1=x, T2=x^2-1/2, T3=x^3-(3/4)x
    # so gamma_1 = 1/2, gamma_k = 1/4 for k>=2.
    x = Fr(2, 5)
    T0, T1 = Fr(1), x
    T2 = x * T1 - Fr(1, 2) * T0
    T3 = x * T2 - Fr(1, 4) * T1
    T4 = x * T3 - Fr(1, 4) * T2
    # T2 == x^2 - 1/2; T3 == x^3 - 3x/4
    ok_cheb = (T2 == x * x - Fr(1, 2)
               and T3 == x ** 3 - Fr(3, 4) * x
               and T4 == x * T3 - Fr(1, 4) * T2)
    check("G3-chebyshev-monic-quarters",
          ok_cheb,
          "T2=x^2-1/2, T3=x^3-3x/4 at x=2/5; gamma_1=1/2, gamma_k=1/4")

    x = 0.6
    eps = EPS0_F
    r_lo = wkb_ratio(x, 0.25 - eps)
    r_hi = wkb_ratio(x, 0.25 + eps)
    s0 = 0.5 * math.pi
    lo_s = s0 * min(r_lo, r_hi)
    hi_s = s0 * max(r_lo, r_hi)
    check("G4-wkb-band-inside-safe",
          1.2 < lo_s < hi_s < 2.1,
          "eps=1/16 at x=3/5 WKB-steps [%.3f, %.3f]" % (lo_s, hi_s))

    DELTA = 0.5 * math.pi
    n_bad_a = 0
    details = []
    for a in (0.0, 0.30, 0.50, 0.70, 0.85):
        dth = DELTA * np.array([1.0 + a * ((-1) ** i) for i in range(14)])
        if np.any(dth <= 0.0) or np.any(dth >= math.pi):
            n_bad_a += 1
            continue
        _n111, nviol, _nreg, _p = scan_eta(dth, n_eta=1001)
        details.append("a=%.2f viol=%d" % (a, nviol))
        if nviol:
            n_bad_a += 1
    check("G5-two-period-A15",
          n_bad_a == 0,
          "; ".join(details))

    d_c = np.full(24, 0.5 * math.pi)
    _a, v_c, _c, _p = scan_eta(d_c, n_eta=1001)
    check("G6-constant-pi2-no-violator",
          v_c == 0,
          "viol=%d/1001" % v_c)

    d_slow = np.array([0.4] * 21 + [2.8, 2.8, 2.8], dtype=float)
    d_edge = np.array([1.0] * 21 + [2.0, 2.0, 2.0], dtype=float)
    _a, v_slow, _c, _p = scan_eta(d_slow, n_eta=1001)
    _a, v_edge, _c, _p = scan_eta(d_edge, n_eta=1001)
    check("G7-contrast-block-regression",
          v_slow > 0 and v_edge == 0,
          "slow-block viol=%d; 1.0/2.0 viol=%d" % (v_slow, v_edge))

    a = 0.70
    d_alt = DELTA * np.array([1.0 + a * ((-1) ** i) for i in range(24)])
    slo, fhi = float(np.min(d_alt[:14])), float(np.max(d_alt[:14]))
    d_blk = np.array([slo] * 21 + [fhi, fhi, fhi], dtype=float)
    _a, v_alt, _c, _p = scan_eta(d_alt, n_eta=1001)
    _a, v_blk, _c, _p = scan_eta(d_blk, n_eta=1001)
    check("G8-interleave-vs-block",
          v_alt == 0 and v_blk > 0,
          "two-period a=0.70 viol=%d; blocked (%.3f^21, %.3f^3) viol=%d"
          % (v_alt, slo, fhi, v_blk))


def part_b():
    section("PART B  CONSTRUCTION PINS AND THE RAY")
    import bordered_hankel_probe as BH
    import dirichlet_matched_frame_probe as DMF
    import dirichlet_secondworld_probe as DSW
    import mean_sieve_floor_probe as MSF
    import port_integrable_kernel_probe as PIK
    import second_family_erosion_probe as SFE

    # G1 live: build_rung L=4h-2
    n_bad_L = 0
    for kz in (9, 15, 18, 21, 33, 46, 53):
        rr = PIK.build_rung(kz)
        h, L = int(rr["h"]), int(rr["L"])
        M = (L + 2) // 2
        if not (M == 2 * h and L == 4 * h - 2):
            n_bad_L += 1
    check("G1b-build-rung-L-identity",
          n_bad_L == 0,
          "7 rungs M=2h and L=4h-2")

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
    worlds.append(("FRAME_A_kz46", DSW.rung_rec(BH.wpack(46))))
    worlds.append(("FRAME_A_kz19", DSW.rung_rec(BH.wpack(19))))

    stats = []
    for lab, rc in worlds:
        stats.append(analyze_rc(lab, rc, n_eta=1001))

    ratio_ok = all(abs(s["dthx_ratio"] - 1.0) < 1e-10 for s in stats)
    check("G10-mask-dtheta-ratio-one",
          ratio_ok,
          "; ".join("%s r=%.3e" % (s["lab"], s["dthx_ratio"] - 1.0)
                    for s in stats))

    box_ok = all(s["dcheb12"] <= EPS0_F + 1e-12
                 and s["dcheb3"] <= EPS0_F + 1e-12
                 and (not math.isfinite(s["gjump"]) or s["gjump"] <= JUMP0_F)
                 for s in stats)
    check("G11-Geps-on-pins",
          box_ok,
          "; ".join("%s |g-1/4|_12=%.4f _3=%.4f jump=%.3f" % (
              s["lab"], s["dcheb12"], s["dcheb3"], s["gjump"])
              for s in stats))

    path_a = all(s["nviol"] == 0 for s in stats)
    check("G12-path-A-A15-pins",
          path_a,
          "; ".join("%s viol=%d/1001 111=%d" % (
              s["lab"], s["nviol"], s["n111"]) for s in stats))

    xconst = all(float(np.min(s["x_last9"])) > 0.0 for s in stats)
    check("G13-plus-x-mask-x-positive",
          xconst,
          "; ".join("%s min_x=%.4f" % (
              s["lab"], float(np.min(s["x_last9"]))) for s in stats))

    s9 = next(s for s in stats if s["lab"] == "FRAME_A_w9")
    p9 = worlds[0][1]["p"]
    xs = np.concatenate([p9["d"]["xs"], p9["d"]["ys"]])
    g_eq, a_eq = equal_weight_gamma(xs, n_upto=40)
    eq_ok = (len(g_eq) >= 20
             and abs(g_eq[0] - 0.5) < 1e-4
             and float(np.max(np.abs(g_eq[1:] - 0.25))) < 1e-5)
    check("G14-equal-weight-chebyshev",
          eq_ok,
          "n_nodes=%d g1=%.6f max|g-1/4|_{k>=2}=%.3e |a|_max=%.3e"
          % (len(xs), float(g_eq[0]),
             float(np.max(np.abs(g_eq[1:] - 0.25))),
             float(np.max(np.abs(a_eq)))))

    s_chi = next(s for s in stats if s["lab"] == "CHI3_w9")
    xb, n, rows = s_chi["xb"], s_chi["n"], s_chi["rows"]
    ray = {}
    for sc, n_eta in ((1.5, 401), (2.0, 401)):
        rr = gamma_scale_rows(rows, sc, 12, n)
        v, _vm, _th, dth = chain_pair(rr, xb, n)
        d_tail = dth[-14:] if len(dth) >= 14 else dth
        _n111, nviol, _nreg, _p = scan_eta(d_tail, n_eta=n_eta)
        R = runs_of_sign(np.sign(v))
        ok, why = v2_holds(R)
        ray[sc] = dict(nviol=nviol, ok=ok, why=why, R=R)
    rr8 = gamma_scale_rows(rows, 8.0, 12, n)
    v8, _vm, _th, _dth = chain_pair(rr8, xb, n)
    R8 = runs_of_sign(np.sign(v8))
    ok8, why8 = v2_holds(R8)
    check("G15-coherent-ray-1.5-in-2.0-out-8-viol",
          ray[1.5]["nviol"] == 0 and ray[2.0]["nviol"] > 0 and (not ok8),
          "s=1.5 A15_viol=%d; s=2.0 A15_viol=%d; s=8 v2 %s last7=%s"
          % (ray[1.5]["nviol"], ray[2.0]["nviol"], why8, R8[-7:]))

    s46 = next(s for s in stats if s["lab"] == "FRAME_A_kz46")
    pos = s46["d_tail"]
    ratio46 = (float(np.max(pos) / np.min(pos))
               if np.min(pos) > 0 else float("nan"))
    check("G16-kz46-high-ratio-in-A15",
          s46["nviol"] == 0 and ratio46 > 5.0 and np.min(pos) > 0,
          "ratio=%.3f steps[%.3f,%.3f] viol=%d/1001"
          % (ratio46, float(np.min(pos)), float(np.max(pos)), s46["nviol"]))

    s16 = next(s for s in stats if s["lab"] == "CHI3_kz16")
    actual_ok = (s16["okv"][0]
                 and tuple(s16["Rv"][-3:]) == (1, 1, 1)
                 and s16["nviol"] == 0
                 and s16["n111"] > 0)
    all_reg = all(sum(1 for r in p if r <= 2) >= 2
                  for p in s16["prevs"]) if s16["prevs"] else False
    check("G17-kz16-eta-111-regular",
          actual_ok and all_reg,
          "actual %s; eta-111=%d all-regular=%s n_prev=%d"
          % (s16["okv"][1], s16["n111"], all_reg, len(s16["prevs"])))
    return stats


def part_c_full():
    section("PART C  181-WINDOW CENSUS (--full)")
    import dirichlet_secondworld_probe as DSW
    import source_prufer_one_defect_probe as SP

    packs_a, packs_b, packs_c3, packs_c4, _l, _e, _e2 = SP.packs_full()
    fams = (("FRAME_A", packs_a), ("FRAME_B", packs_b),
            ("CHI3", packs_c3), ("CHI4", packs_c4))
    census = []
    n_skip = 0
    for fam, ps in fams:
        for p in ps:
            if p.get("nf") is not None or not p.get("complete", True):
                n_skip += 1
                continue
            if not p.get("rows"):
                n_skip += 1
                continue
            rc = DSW.rung_rec(p)
            lab = "%s_kz%d" % (fam, p["kz"])
            s = analyze_rc(lab, rc, n_eta=401)
            s["fam"] = fam
            census.append(s)
    n_live = len(census)
    n_viol = sum(1 for s in census if s["nviol"])
    max3 = max(s["dcheb3"] for s in census) if census else 1.0
    max12 = max(s["dcheb12"] for s in census) if census else 1.0
    maxj = max(s["gjump"] for s in census
               if math.isfinite(s["gjump"])) if census else 1.0
    ratio_ok = all(abs(s["dthx_ratio"] - 1.0) < 1e-9 for s in census)
    box_ok = max3 <= EPS0_F + 1e-12 and max12 <= EPS0_F + 1e-12 \
        and maxj <= JUMP0_F
    check("G20-census-181-Geps-mesh-A15",
          n_live == 181 and n_skip == 0 and n_viol == 0
          and ratio_ok and box_ok,
          "live=%d skip=%d A15_viol=%d max|g-1/4|_3=%.4f _12=%.4f "
          "jump=%.3f dthx_ratio_all_1=%s"
          % (n_live, n_skip, n_viol, max3, max12, maxj, ratio_ok))
    for fam in ("FRAME_A", "FRAME_B", "CHI3", "CHI4"):
        sub = [s for s in census if s["fam"] == fam]
        print("    %s n=%d max3=%.4f max12=%.4f jump=%.3f viol=%d"
              % (fam, len(sub),
                 max(s["dcheb3"] for s in sub),
                 max(s["dcheb12"] for s in sub),
                 max(s["gjump"] for s in sub if math.isfinite(s["gjump"])),
                 sum(s["nviol"] for s in sub)),
              flush=True)
    return census


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--full", action="store_true",
                     help="run the 181-window census (slow)")
    args = par.parse_args()

    part_a()
    part_b()
    if args.full:
        part_c_full()
    else:
        print("\n  (skip G20 181-census; pass --full to run it)",
              flush=True)

    section("SUMMARY")
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("V3PRIME LEMMA VERIFIED")
        return 0
    print("V3PRIME LEMMA FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
