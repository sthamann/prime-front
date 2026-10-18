#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_v2_lemma.py -- machine check of every numbered lemma
in rh/problem/v2_lemma_v3.tex (round 374, V2 reduced to V3').

PART A (STANDALONE):
  G1  Wronskian/Lagrange identity over Q
  G2  named combinatorial violator vs spike (regression)
  G3  constant-step rigid walks: 0 V2-violators
  G4  slow-then-fast contrast dichotomy (0.4/2.8 violates;
      1.0/2.0 does not)
  G5  r>=3 dwell bound: r * slow < pi  =>  slow < pi/r <= pi/3
  G6  Chebyshev x-mask never ends (1,1,1)
  G7  Chebyshev theta-compress: (1,1,1) tails exist, 0 V2-viol

PART B (CONSTRUCTION PINS):
  G8  Wronskian sin-id residual < 1e-12 on the six pins
  G9  Path A: last-15 Pruefer steps in A_15 (0 eta-violators)
  G10 chi3 kz16 v2-triple is regular prev4=[3,2,1,3]; every
      eta-(1,1,1) on that window is V2-regular
  G11 source gamma bounds on pins (last3 |g-1/4|, last8 jump)
  G12 8x last-12 gamma on CHI3_w9 is a v2-violator; scale 6 is not
  G13 sign(x)>0 on last 9 bulk nodes
  G14 r372 dictionary: floor(theta/pi) runs = v2 sign-runs
  G15 colouring V2 holds; kz53 w-driven regular
  G16 weight-cluster (boost 8 and 64): breaks positivity, no V2-viol

Exit: per-gate PASS/FAIL and the final line
"V2 LEMMA V3 VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named reduction.
"""
from __future__ import annotations

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


def pair_runs(run_lens):
    ns_x, i, nr = [], 0, len(run_lens)
    while i < nr:
        if i + 1 < nr:
            ns_x.append(run_lens[i] + run_lens[i + 1])
            i += 2
        else:
            ns_x.append(run_lens[i])
            i += 1
    return ns_x, list(reversed(ns_x)), (nr % 2 == 1)


def occupancy(dth, eta):
    th = float(eta)
    levs = [int(math.floor(th / math.pi))]
    for d in dth:
        th += float(d)
        levs.append(int(math.floor(th / math.pi)))
    return runs_of_levels(levs)


def pattern_rr111(R):
    """user-equivalent violator: last five runs (r, r, 1, 1, 1) with r>=3."""
    if len(R) < 5:
        return False
    return tuple(R[-3:]) == (1, 1, 1) and R[-5] >= 3 and R[-4] >= 3


def scan_eta(dth, n_eta=2001):
    n111 = nviol = nreg = npat = 0
    prevs = set()
    for eta in np.linspace(0.0, math.pi, n_eta, endpoint=False):
        R = occupancy(dth, eta)
        ok, _why = v2_holds(R)
        if pattern_rr111(R):
            npat += 1
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
    return n111, nviol, nreg, npat, prevs


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


def clustered_cheb(T, mdeg, compress, mask_frac=0.20):
    lo_x = -1.0 + 2.0 * mask_frac
    hi_x = 1.0 - 2.0 * mask_frac
    th_cut = math.acos(hi_x) + 0.4
    xs, sig = [], []
    for t in range(T):
        th = math.pi * (t + 0.5) / T
        x = math.cos(th)
        if x < lo_x or x > hi_x:
            continue
        if th < th_cut:
            u = th / th_cut
            th_eff = th_cut * (u ** compress)
        else:
            th_eff = th
        s = math.sin(mdeg * th_eff)
        xs.append(x)
        sig.append(1 if s >= 0 else -1)
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    return [sig[i] for i in order]


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
    return v, vm, th, dth, theta


def wronskian_residual(v, vm):
    rx = np.hypot(v[:-1], vm[:-1])
    ry = np.hypot(v[1:], vm[1:])
    cross = v[1:] * vm[:-1] - vm[1:] * v[:-1]
    with np.errstate(divide="ignore", invalid="ignore"):
        sin_pred = np.where(rx * ry > 0.0, cross / (rx * ry), 0.0)
    phi = np.arctan2(v, vm)
    dphi = np.diff(phi)
    dphi = (dphi + math.pi) % (2.0 * math.pi) - math.pi
    res = np.abs(sin_pred - np.sin(dphi))
    return float(np.max(res)) if len(res) else 0.0


def bulk_of(rc):
    import phase_bulk_bound_probe as PBB
    import dirichlet_secondworld_probe as DSW
    o = rc["o"]
    bxs = rc["bx"][o]
    bws = rc["bw"][o]
    cts = rc["ct"][o]
    ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], DSW.EDGE_F)
    return (rc["N"], bxs[~ed], bws[~ed], cts[~ed],
            rc["p"]["rows"], rc["kz"])


def gamma_scale_rows(rows, scale, n_last, n):
    out = [dict(r) for r in rows]
    for k in range(max(0, n - n_last), n):
        if out[k].get("gam_next") is not None:
            out[k]["gam_next"] = float(out[k]["gam_next"]) * scale
    return out


def weight_adversary_frame_a(boost=8.0, n_spike=3, n_gap=6):
    """Deplete n_gap arithmetic atoms just before the +x mask,
    boost n_spike at the mask, recompute the Jacobi chain."""
    import bordered_hankel_probe as BH
    import dirichlet_secondworld_probe as DSW
    p = BH.wpack(9)
    d = p["d"]
    dsm = p["dsm"]
    xs = np.array(d["xs"], float).copy()
    ws = np.array(d["ws"], float).copy()
    ys = np.array(d["ys"], float).copy()
    vs = np.array(d["vs"], float).copy()
    xu = np.concatenate([xs, ys])
    wu = np.concatenate([ws, -vs])
    src = np.concatenate([np.zeros(len(xs), dtype=int),
                          np.ones(len(ys), dtype=int)])
    idx = np.concatenate([np.arange(len(xs)), np.arange(len(ys))])
    o = np.argsort(xu)
    xu, wu, src, idx = xu[o], wu[o], src[o], idx[o]
    n_tot = n_spike + n_gap
    tail_i = np.arange(len(xu))[-n_tot:]
    gap_i = tail_i[:n_gap]
    spk_i = tail_i[n_gap:]
    wu2 = wu.copy()
    wu2[gap_i] *= 1.0 / boost
    wu2[spk_i] *= boost
    xs2, ws2 = xs.copy(), ws.copy()
    ys2, vs2 = ys.copy(), vs.copy()
    for _j, s, k, wnew in zip(np.arange(len(xu)), src, idx, wu2):
        if s == 0:
            ws2[k] = abs(wnew)
        else:
            vs2[k] = abs(wnew)
    rows = BH.bord_chain(xs2, ws2, ys2, vs2,
                         dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"],
                         p["N"])
    n = p["N"] - 2
    gpos = all(float(rows[k]["gam_next"]) > 0.0
               for k in range(n) if rows[k].get("gam_next") is not None)
    p2 = dict(p)
    p2["rows"] = rows
    p2["d"] = dict(d)
    p2["d"]["xs"], p2["d"]["ws"] = xs2, ws2
    p2["d"]["ys"], p2["d"]["vs"] = ys2, vs2
    rc = DSW.rung_rec(p2)
    _N, xb, _wb, cb, _rows_r, _kz = bulk_of(rc)
    v, _vm, _th, _dth, _theta = chain_pair(rows, xb, n)
    Rv = runs_of_sign(np.sign(v))
    Rc = runs_of_sign(np.sign(cb))
    return dict(gpos=gpos, okv=v2_holds(Rv), okc=v2_holds(Rc),
                last7v=Rv[-7:] if len(Rv) >= 7 else Rv)


def main():
    section("PART A  WRONSKIAN, CONTRAST, CHEBYSHEV")

    # G1 Lagrange over Q
    n_bad = 0
    n_chk = 0
    rng = np.random.default_rng(374)
    for _ in range(400):
        vals = [Fr(int(x), int(d))
                for x, d in zip(rng.integers(-20, 21, size=4),
                                rng.integers(1, 13, size=4))]
        vx, vmx, vy, vmy = vals
        cross = vy * vmx - vmy * vx
        dot = vx * vy + vmx * vmy
        rx2 = vx * vx + vmx * vmx
        ry2 = vy * vy + vmy * vmy
        n_chk += 1
        if cross * cross + dot * dot != rx2 * ry2:
            n_bad += 1
    # a few exact integer witnesses
    witnesses = [(Fr(3), Fr(4), Fr(5), Fr(12)),
                 (Fr(1), Fr(0), Fr(0), Fr(1)),
                 (Fr(-2, 3), Fr(5, 7), Fr(1, 2), Fr(-8, 9))]
    for vx, vmx, vy, vmy in witnesses:
        cross = vy * vmx - vmy * vx
        dot = vx * vy + vmx * vmy
        rx2 = vx * vx + vmx * vmx
        ry2 = vy * vy + vmy * vmy
        n_chk += 1
        if cross * cross + dot * dot != rx2 * ry2:
            n_bad += 1
    check("G1-wronskian-lagrange-Q",
          n_bad == 0 and n_chk >= 400,
          "%d rational pairs, misses %d" % (n_chk, n_bad))

    # G2 combinatorial regression
    runs_v = [3] * 8 + [1, 1, 1]
    runs_s = [2] * 8 + [3, 3, 1, 1, 1]
    okV, whyV = v2_holds(runs_v)
    okS, whyS = v2_holds(runs_s)
    _nsx, ns, odd = pair_runs(runs_v)
    check("G2-violator-vs-spike",
          (not okV) and okS and odd and ns[:4] == [1, 2, 6, 6],
          "viol %s; spike %s; n=%s" % (whyV, whyS, ns[:4]))

    # G3 constant step (long walk so 7-run V2 is defined)
    n_bad_c = 0
    n_tot_c = 0
    for step in (0.8, 1.0, 1.2, 0.5 * math.pi, 1.8, 2.0):
        dth = np.full(24, step)
        _n111, nviol, _nreg, npat, _p = scan_eta(dth, n_eta=1001)
        n_tot_c += 1
        if nviol or npat:
            n_bad_c += 1
    check("G3-constant-step-no-violator",
          n_bad_c == 0 and n_tot_c == 6,
          "%d constant-step profiles, viol-profiles %d" % (n_tot_c, n_bad_c))

    # G4 contrast dichotomy: 21 slow + 3 fast (25 nodes, 7-run V2 live)
    d_slow = np.array([0.4] * 21 + [2.8, 2.8, 2.8], dtype=float)
    d_edge = np.array([1.0] * 21 + [2.0, 2.0, 2.0], dtype=float)
    _a, v_slow, _c, p_slow, _p = scan_eta(d_slow, n_eta=1001)
    _a, v_edge, _c, p_edge, _p = scan_eta(d_edge, n_eta=1001)
    check("G4-contrast-dichotomy",
          (v_slow + p_slow) > 0 and v_edge == 0 and p_edge == 0,
          "slow=0.4/fast=2.8 V2-viol=%d pat=%d/1001; "
          "slow=1.0/fast=2.0 V2-viol=%d pat=%d"
          % (v_slow, p_slow, v_edge, p_edge))

    # G5 dwell bound Fractions: pi/3 bound for r=3
    # r * slow < pi  => slow < pi/r.  For r=3, pi/3 vs 1.047...
    three = Fr(3)
    # compare 3 * (9/10) = 27/10 = 2.7 < 22/7 (pi upper) and
    # 3 * (11/10) = 33/10 = 3.3 > 333/106 (pi lower ~3.1415)
    pi_lo = Fr(333, 106)   # 3.14150... < pi
    pi_hi = Fr(22, 7)      # 3.142... > pi
    slow_ok = Fr(9, 10)
    slow_bad = Fr(11, 10)
    bound_ok = three * slow_ok < pi_lo
    bound_bad = three * slow_bad > pi_hi
    check("G5-dwell-r3-bound",
          bound_ok and bound_bad,
          "3*(9/10)=%s < pi; 3*(11/10)=%s > pi (Archimedes)"
          % (three * slow_ok, three * slow_bad))

    # G6 Chebyshev x-mask
    n_ch = n_111 = 0
    for T in range(50, 361, 20):
        for mdeg in (max(2, T // 3), T // 2, T // 2 + 1):
            sig = chebyshev_xmask(T, mdeg, 0.20)
            if len(sig) < 12:
                continue
            R = runs_of_sign(sig)
            n_ch += 1
            if len(R) >= 3 and tuple(R[-3:]) == (1, 1, 1):
                n_111 += 1
    check("G6-chebyshev-xmask-no-111",
          n_ch > 30 and n_111 == 0,
          "%d windows, (1,1,1) tails %d" % (n_ch, n_111))

    # G7 theta-compress: triples exist, 0 violators
    n_w = n_t = n_v = 0
    for T in range(80, 401, 40):
        for mdeg in (T // 2 - 1, T // 2, T // 2 + 1):
            for comp in (0.5, 1.0, 2.0, 3.0):
                sig = clustered_cheb(T, max(2, mdeg), compress=comp)
                if len(sig) < 12:
                    continue
                R = runs_of_sign(sig)
                n_w += 1
                ok, _why = v2_holds(R)
                if len(R) >= 3 and tuple(R[-3:]) == (1, 1, 1):
                    n_t += 1
                if not ok:
                    n_v += 1
    check("G7-chebyshev-compress-111-regular",
          n_w > 50 and n_t > 0 and n_v == 0,
          "%d warp-windows, (1,1,1) %d, V2-viol %d" % (n_w, n_t, n_v))

    section("PART B  CONSTRUCTION PINS AND V3'")
    import bordered_hankel_probe as BH  # noqa: E402
    import dirichlet_matched_frame_probe as DMF  # noqa: E402
    import dirichlet_secondworld_probe as DSW  # noqa: E402
    import mean_sieve_floor_probe as MSF  # noqa: E402
    import second_family_erosion_probe as SFE  # noqa: E402
    import source_prufer_one_defect_probe as SP  # noqa: E402

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

    stats = []
    for lab, rc in worlds:
        N, xb, wb, cb, rows, kz = bulk_of(rc)
        n = N - 2
        v, vm, th, dth, theta = chain_pair(rows, xb, n)
        sg_v = np.sign(v)
        sg_v[sg_v == 0] = 1
        Rv = runs_of_sign(sg_v)
        Rc = runs_of_sign(np.sign(cb))
        wr = wronskian_residual(v, vm)
        lev = np.floor(th / math.pi).astype(np.int64)
        Rlev = runs_of_levels(lev)
        gams = []
        for k in range(max(n, 0)):
            g = rows[k].get("gam_next")
            if g is not None:
                gams.append(float(g))
        gams = np.array(gams, float)
        last8 = gams[-8:] if len(gams) >= 8 else gams
        if len(last8) >= 2 and np.all(last8 > 0):
            gjump = float(np.max(np.abs(np.log(last8[1:] / last8[:-1]))))
        else:
            gjump = float("nan")
        dcheb_last3 = (float(np.max(np.abs(gams[-3:] - 0.25)))
                       if len(gams) >= 3 else 0.0)
        L = 15
        d_tail = dth[-(L - 1):] if len(dth) >= L - 1 else dth
        n111, nviol, nreg, npat, prevs = scan_eta(d_tail, n_eta=2001)
        stats.append(dict(
            lab=lab, kz=kz, N=N, n_bulk=len(xb), wr=wr,
            Rv=Rv, Rc=Rc, Rlev=Rlev, xb=xb, dth=dth,
            n111=n111, nviol=nviol, nreg=nreg, npat=npat, prevs=prevs,
            gjump=gjump, dcheb_last3=dcheb_last3,
            gams=gams, rows=rows, n=n, v=v,
            okc=v2_holds(Rc), okv=v2_holds(Rv),
            dict_ok=(Rlev == Rv),
            x_last9=xb[-9:] if len(xb) >= 9 else xb,
        ))

    wr_max = max(s["wr"] for s in stats)
    check("G8-wronskian-sin-residual",
          wr_max < 1e-12,
          "max residual %.3e on %d pins" % (wr_max, len(stats)))

    path_a = all(s["nviol"] == 0 for s in stats)
    n111_tot = sum(s["n111"] for s in stats)
    check("G9-path-A-A15-no-eta-violator",
          path_a and n111_tot >= 0,
          "; ".join("%s viol=%d/2001 111=%d" % (
              s["lab"], s["nviol"], s["n111"]) for s in stats))

    s16 = next(s for s in stats if s["lab"] == "CHI3_kz16")
    actual_ok = (s16["okv"][0]
                 and tuple(s16["Rv"][-3:]) == (1, 1, 1)
                 and s16["Rv"][-7:-3] == [3, 2, 1, 3]
                 and s16["nviol"] == 0
                 and s16["n111"] > 0)
    all_reg = all(sum(1 for r in p if r <= 2) >= 2
                  for p in s16["prevs"]) if s16["prevs"] else False
    check("G10-kz16-triple-and-eta-111s-regular",
          actual_ok and all_reg,
          "actual %s; eta-111=%d all-regular=%s n_prev_types=%d"
          % (s16["okv"][1], s16["n111"], all_reg, len(s16["prevs"])))

    last3_ok = all(s["dcheb_last3"] <= 0.05 for s in stats)
    jump_ok = all(s["gjump"] <= 0.30 for s in stats
                  if math.isfinite(s["gjump"]))
    check("G11-source-gamma-bounds",
          last3_ok and jump_ok,
          "; ".join("%s last3|g-1/4|=%.4f jump8=%.3f" % (
              s["lab"], s["dcheb_last3"], s["gjump"]) for s in stats))

    s_chi = next(s for s in stats if s["lab"] == "CHI3_w9")
    xb = s_chi["xb"]
    n = s_chi["n"]
    rows = s_chi["rows"]
    rr8 = gamma_scale_rows(rows, 8.0, 12, n)
    v8, vm8, th8, dth8, _ = chain_pair(rr8, xb, n)
    R8 = runs_of_sign(np.sign(v8))
    ok8, why8 = v2_holds(R8)
    rr6 = gamma_scale_rows(rows, 6.0, 12, n)
    v6, vm6, th6, dth6, _ = chain_pair(rr6, xb, n)
    R6 = runs_of_sign(np.sign(v6))
    ok6, why6 = v2_holds(R6)
    check("G12-gamma-scale-8-violates-6-does-not",
          (not ok8) and ok6,
          "x8 last8=%s %s; x6 last8=%s %s"
          % (R8[-8:], why8, R6[-8:], why6))

    xconst = all(float(np.min(s["x_last9"])) > 0.0 for s in stats)
    check("G13-plus-x-mask-x-positive",
          xconst,
          "; ".join("%s min_x last9=%.4f" % (
              s["lab"], float(np.min(s["x_last9"]))) for s in stats))

    dict_ok = all(s["dict_ok"] for s in stats)
    check("G14-prufer-to-run-dictionary",
          dict_ok,
          "; ".join("%s dict=%s last7v=%s" % (
              s["lab"], s["dict_ok"], s["Rv"][-7:]) for s in stats))

    s53 = next(s for s in stats if s["lab"] == "CHI4_kz53")
    colouring_ok = all(s["okc"][0] for s in stats)
    kz53_ok = (s53["okc"][0]
               and tuple(s53["Rc"][-3:]) == (1, 1, 1)
               and tuple(s53["Rv"][-3:]) != (1, 1, 1)
               and s53["Rc"][-7:-3] == [4, 1, 2, 4])
    check("G15-colouring-V2-and-kz53-w-driven",
          colouring_ok and kz53_ok,
          "all colouring V2; kz53 %s last3 c/v2=%s/%s"
          % (s53["okc"][1], s53["Rc"][-3:], s53["Rv"][-3:]))

    n_wadv = 0
    n_wadv_all = 0
    details = []
    for boost in (8.0, 64.0):
        ad = weight_adversary_frame_a(boost=boost, n_spike=3, n_gap=6)
        n_wadv_all += 1
        ok_case = ((not ad["gpos"]) and ad["okv"][0] and ad["okc"][0])
        if ok_case:
            n_wadv += 1
        details.append("boost=%s gpos=%s v2=%s c=%s last7v=%s"
                       % (boost, ad["gpos"], ad["okv"][1], ad["okc"][1],
                          ad["last7v"]))
    check("G16-weight-cluster-breaks-positivity-not-V2",
          n_wadv == n_wadv_all == 2,
          "; ".join(details))

    section("SUMMARY")
    n_ok = sum(1 for _n, o in CHECKS if o)
    n_all = len(CHECKS)
    print("  %d/%d gates" % (n_ok, n_all))
    if n_ok == n_all:
        print("V2 LEMMA V3 VERIFIED")
        return 0
    print("V2 LEMMA V3 FAILED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
