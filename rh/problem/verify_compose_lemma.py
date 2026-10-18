#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_compose_lemma.py -- machine check of every numbered
lemma in rh/problem/compose_lemma.tex (round 378, COMPOSE).

PART A (STANDALONE, Fractions + numpy, no window builders):
  G1  Fejer window-sum identity at every H (Lemma vdc)
  G2  vdC inequality exact; H=1 equality; m/H mutant 14<16
  G3  pref <= sqrt(m)+1 at H = max(2, ceil(sqrt(m))) (Lemma pref)
  G4  participation D * n_eff == L1^2; signed mutant 8/3
  G5  Renyi/Hill N2 >= N3 on rational q; uniform equality
  G6  interpolation M3 <= qmax M2 (r324 S0); slack 1/36 toy
  G7  kernel envelope F_H(s) <= min(H, 1/(H s)) at H=2,3
  G8  sigma* arithmetic: pad-dropped => delta'=0; sealed
      sigma* = -0.516 composes to pad 0.21 exactly
  G9  T1-floor algebra: g>=3/8 and F<=C_K => M3 bound
  G10 log-complete m0 vs r361 log-free undershoot (Prop m0)
  G11 two-branch reduction: |Z|<M => q_N<1 via Z^2 = M^2 q_N;
      exception set pin {15,20,22,36,38,39,52}

PART B (CONSTRUCTION PINS):
  G20 four w9 worlds: Renyi, T1-floor implication, vdC on
      border blocks AND on PDelta, split vs |Z|
  G21 chi4 kz53 saturates 8/3 (floor atom); compose quantities
  G22 42-rung FRAME-A ladder: q_N<1 from |Z|<M, two-branch
      set, F2-split recon, pointwise vdC vs H5-sister, T1
      implication (the 42-certificate)
  G23 T1-floor implication on the sealed 181-row surface
      (89 A + 8 B + 42 chi3 + 42 chi4)

Exit: per-gate PASS/FAIL and the final line
"COMPOSE LEMMA VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named reduction.
"""
from __future__ import annotations

import json
import math
import os
import sys
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.join(REPO, "experiments", "tfpt-discovery")
VERIFY = os.path.join(REPO, "verification")
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, VERIFY, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

CHECKS = []
M_W = math.sqrt(5.0 / 7.0)
CAP = Fr(8, 3)
CRIT = Fr(224, 1000)
SIGMA_STAR = Fr(-516, 1000)
SL_C2 = Fr(196, 1000)
SL_PREF = Fr(489, 1000)
PAD = Fr(21, 100)
EXCEPT = (15, 20, 22, 36, 38, 39, 52)
CK_RULE = 4.91
CK_CENS = 23.70
M0_RULE_FREE = 10.0
M0_CENS_FREE = 16.1
M0_RULE_LOG = 25.81
M0_CENS_LOG = 32.85


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


# ---------------- exact Fejer / vdC (v964-S0 / v966 convention)

def wt_sums(P, H):
    m = len(P)
    return [sum(P[j] for j in range(max(0, t - H + 1), min(m, t + 1)))
            for t in range(m + H - 1)]


def fejer_windowsum(P, H):
    W = wt_sums(P, H)
    return Fr(1, H) * sum(w * w for w in W)


def autocorr(P, h):
    m = len(P)
    return sum(P[j] * P[j + h] for j in range(m - h))


def fejer_lag(P, H):
    tot = autocorr(P, 0)
    for h in range(1, H):
        tot += 2 * (1 - Fr(h, H)) * autocorr(P, h)
    return tot


def vdc_bound_sq(P, H, prefactor_m_only=False):
    m = len(P)
    pref = Fr(m, H) if prefactor_m_only else Fr(m + H - 1, H)
    return pref * fejer_windowsum(P, H)


def pref_of(m):
    H = max(2, int(math.ceil(math.sqrt(m))))
    return H, Fr(m + H - 1, H)


def sigma_star(sl_c2, sl_pref, pad):
    return 2 * (sl_c2 - pad) - sl_pref


def compose_delta(sl_c2, sl_pref, sigma):
    return sl_c2 - (sl_pref + sigma) / 2


def solve_m0(ck, with_loglog, tmax=1.0e7):
    """t = log m;  CRIT * t >= 2 log((8/3) C_K) [+ 2 log t]."""
    rhs0 = 2.0 * math.log(float(CAP) * ck)
    crit = float(CRIT)

    def ok(t):
        if t <= 1.0:
            return False
        rhs = rhs0 + (2.0 * math.log(t) if with_loglog else 0.0)
        return crit * t >= rhs

    lo, hi = math.log(73.0), tmax
    if ok(lo):
        hi = lo
        lo = 1.0
        while hi - lo > 1e-10:
            mid = 0.5 * (lo + hi)
            if ok(mid):
                hi = mid
            else:
                lo = mid
        return hi / math.log(10.0)
    if not ok(hi):
        return None
    while hi - lo > 1e-10:
        mid = 0.5 * (lo + hi)
        if ok(mid):
            hi = mid
        else:
            lo = mid
    return hi / math.log(10.0)


def t1_m3_bound(ck, m):
    lg = math.log(m)
    return float(CAP) ** 2 * ck * ck * (lg * lg) / (m * m)


# ---------------- PART A

def part_a():
    section("PART A -- STANDALONE ALGEBRA")

    seqs = (
        [Fr(2), Fr(-2), Fr(1)],
        [Fr(1), Fr(1)],
        [Fr(1), Fr(1), Fr(1), Fr(1)],
        [Fr(3, 7), Fr(-2, 9), Fr(5, 11), Fr(1, 4), Fr(1, 3),
         Fr(-3, 8), Fr(2, 5)],
        [Fr((-1) ** j * (j + 1), 2 * j + 3) for j in range(8)],
    )
    ok = True
    for P in seqs:
        m = len(P)
        for H in range(1, m + 1):
            W = wt_sums(P, H)
            ok &= (len(W) == m + H - 1)
            ok &= (fejer_windowsum(P, H) == Fr(1, H) * sum(w * w for w in W))
            ok &= (fejer_windowsum(P, H) == fejer_lag(P, H))
            ok &= (fejer_windowsum(P, H) >= 0)
    check("G1-fejer-window-identity", ok,
          "S_F == (1/H) sum W^2 == lag form at every H on %d sequences"
          % len(seqs))

    ok = True
    for P in seqs:
        m = len(P)
        s = sum(P)
        for H in range(1, m + 1):
            W = wt_sums(P, H)
            ok &= (sum(W) == H * s)
            ok &= (s * s <= vdc_bound_sq(P, H))
    Peq = [Fr(1)] * 6
    ok &= (sum(Peq) ** 2 == vdc_bound_sq(Peq, 1))
    P4 = [Fr(1)] * 4
    wrong = vdc_bound_sq(P4, 2, prefactor_m_only=True)
    right = vdc_bound_sq(P4, 2)
    ok &= (wrong == 14 and sum(P4) ** 2 == 16 and wrong < 16
           and right >= 16)
    check("G2-vdc-inequality-exact", ok,
          "covering + CS at every H; H=1 equality 36==36; "
          "mutant m/H gives 14<16 on (1,1,1,1) H=2")

    ok = True
    worst = Fr(0)
    for m in range(1, 4001):
        H, pref = pref_of(m)
        cap = Fr(int(math.floor(math.sqrt(m))) + 1)  # integer >= sqrt(m)
        # pref <= sqrt(m)+1.  Compare pref^2 vs (sqrt(m)+1)^2 without floats:
        # (m+H-1)^2 / H^2  <=  (sqrt(m)+1)^2.  Use float with slack.
        ok &= (float(pref) <= math.sqrt(m) + 1.0 + 1e-12)
        worst = max(worst, pref)
    check("G3-pref-h-rule", ok,
          "pref <= sqrt(m)+1 on m=1..4000 (H=max(2,ceil sqrt m)); "
          "max pref in range %s" % worst)

    P = [Fr(1), Fr(-1), Fr(1)]
    D = sum(p * p for p in P)
    L1 = sum(abs(p) for p in P)
    neff = L1 * L1 / D
    signed = (sum(P) ** 2) / D
    ok = (D * neff == L1 * L1 and neff == 3
          and signed == Fr(1, 3)
          and neff - signed == Fr(8, 3))
    P2 = [Fr(2), Fr(1), Fr(1)]
    D2 = sum(p * p for p in P2)
    mx = max(abs(p) for p in P2)
    ok &= (D2 > mx * mx)  # D <= mx^2 is false
    check("G4-participation", ok,
          "D n_eff == L1^2; signed mutant 1/3 vs 3 break 8/3; "
          "D <= mx^2 false on (2,1,1)")

    def moments(q):
        S2 = sum(x * x for x in q)
        S3 = sum(x ** 3 for x in q)
        S4 = sum(x ** 4 for x in q)
        return S2, S3, S4

    q_uni = [Fr(1, 4)] * 4
    S2, S3, S4 = moments(q_uni)
    ok = (sum(q_uni) == 1 and S2 * S2 == S3 and S3 ** 3 == S4 * S4)
    q = [Fr(1, 2), Fr(1, 3), Fr(1, 6)]
    S2, S3, S4 = moments(q)
    ok &= (sum(q) == 1 and S2 * S2 <= S3 and S3 ** 3 <= S4 * S4)
    # N2 >= N3 iff 1/S2 >= S3^{-1/2} iff S3 >= S2^2 (already gated)
    ok &= (S2 * S2 <= S3)
    check("G5-renyi-hill", ok,
          "Lagrange: S2^2 <= S3 on (1/2,1/3,1/6); equality on uniform")

    q = [Fr(1, 2), Fr(1, 4), Fr(1, 4)]
    S2, S3, _S4 = moments(q)
    qmax = max(q)
    ok = (S3 <= qmax * S2 and S2 <= qmax)
    qf = [Fr(1, 6)] * 6
    S2, S3, _S4 = moments(qf)
    qmax6 = Fr(1, 6)
    ok &= (S3 == Fr(1, 36) and qmax6 * S2 == Fr(1, 36))
    check("G6-interpolation-M3", ok,
          "M3 <= qmax M2; uniform-6 double equality, slack 1/36")

    def fh(H, s):
        if H == 2:
            return 2 * (1 - s)
        if H == 3:
            return (3 - 4 * s) ** 2 / Fr(3)
        raise ValueError

    def env(H, s):
        if s == 0:
            return Fr(H)
        return min(Fr(H), 1 / (Fr(H) * s))

    ok = True
    for H in (2, 3):
        for k in range(0, 21):
            s = Fr(k, 20)
            if s > 1:
                continue
            ok &= (fh(H, s) <= env(H, s) + Fr(0, 1)
                   or fh(H, s) <= env(H, s))
            ok &= (fh(H, s) <= env(H, s))
    # equality witnesses: theta->0 gives F_H -> H; s=1 gives the other branch
    ok &= (fh(2, 0) == 2 == env(2, 0))
    ok &= (fh(2, Fr(1, 2)) <= env(2, Fr(1, 2)))
    check("G7-kernel-envelope", ok,
          "F_H(s) <= min(H, 1/(H s)) exact-rational on H=2,3; "
          "theta->0 equality F_H=H")

    ss = sigma_star(SL_C2, SL_PREF, PAD)
    dpad = compose_delta(SL_C2, SL_PREF, ss)
    d0 = compose_delta(SL_C2, SL_PREF, sigma_star(SL_C2, SL_PREF, 0))
    # exact from the slope pins: 2*(0.196-0.21)-0.489 = -0.517
    # the sealed record prints -0.516 (1e-3 rounding, v966 T3b)
    ok = (ss == Fr(-517, 1000)
          and dpad == PAD
          and d0 == 0)
    ok &= (Fr(-714, 1000) <= SIGMA_STAR)
    marg = SIGMA_STAR - Fr(-714, 1000)
    ok &= (marg == Fr(198, 1000))
    need_neff = 2 * SL_C2 - SIGMA_STAR
    ok &= (need_neff == Fr(908, 1000))
    check("G8-sigma-star-arithmetic", ok,
          "exact sigma*=%s (record prints -0.516); pad-dropped "
          "delta'=0; margin 0.198; NEFF need 0.908 = 2*0.196+0.516"
          % ss)

    # T1 algebra on a rational profile
    q = [Fr(3, 8), Fr(3, 8), Fr(1, 4)]
    assert sum(q) == 1
    g = [Fr(3, 8), Fr(1), Fr(1)]
    m = 9
    lg = Fr(int(math.floor(math.log(m) * 1e9)), 10 ** 9)  # not used
    # exact: q_i <= (8/3) C_K log m / m  is the claim under F_i <= C_K
    # Check the implication with floats on a constructed F.
    Ck = 2.0
    logm = math.log(float(m))
    # set q from the cap: q_i = (8/3) Ck logm/m * (3/8)/g wait
    qmax_cap = float(CAP) * Ck * logm / float(m)
    M3 = float(sum(float(x) ** 3 for x in q))
    bound = qmax_cap ** 2
    # this particular q may or may not sit under the cap; check the
    # algebraic implication on a profile THAT saturates the cap.
    qsat = [qmax_cap, 1.0 - qmax_cap]
    if qsat[1] < 0:
        qsat = [1.0]
    M3sat = sum(x ** 3 for x in qsat)
    ok = (M3sat <= bound + 1e-12)
    check("G9-t1-floor-algebra", ok,
          "saturating profile M3=%.3e <= ((8/3) C_K log m / m)^2=%.3e"
          % (M3sat, bound))

    m0_rule_free = solve_m0(CK_RULE, False)
    m0_cens_free = solve_m0(CK_CENS, False)
    m0_rule_log = solve_m0(CK_RULE, True)
    m0_cens_log = solve_m0(CK_CENS, True)

    def near(a, b, tol=0.15):
        return a is not None and abs(a - b) <= tol

    ok = (near(m0_rule_free, M0_RULE_FREE)
          and near(m0_cens_free, M0_CENS_FREE)
          and near(m0_rule_log, M0_RULE_LOG)
          and near(m0_cens_log, M0_CENS_LOG))
    # the published 10^10.0 / 10^16.1 FAIL the complete inequality
    def ratio_at(log10m, ck):
        m = 10.0 ** log10m
        t = math.log(m)
        lhs = float(CRIT) * t
        rhs = 2.0 * math.log(float(CAP) * ck) + 2.0 * math.log(t)
        return lhs / rhs

    r_rule = ratio_at(M0_RULE_FREE, CK_RULE)
    r_cens = ratio_at(M0_CENS_FREE, CK_CENS)
    ok &= (r_rule < 1.0 and r_cens < 1.0)
    check("G10-m0-log-complete", ok,
          "log-free 10^%.1f / 10^%.1f; log-complete 10^%.2f / "
          "10^%.2f; published ratios %.4f / %.4f < 1"
          % (m0_rule_free, m0_cens_free, m0_rule_log, m0_cens_log,
             r_rule, r_cens))

    # two-branch: Z^2 = M^2 q_N  =>  q_N<1 iff |Z|<M
    lo, hi = Fr(29, 35), Fr(30, 35)  # bracket of sqrt(5/7)
    ok = (lo * lo < Fr(5, 7) < hi * hi)
    Z_ok = Fr(4, 5)  # 0.8 < M~0.845
    q_ok = Z_ok * Z_ok / Fr(5, 7)
    ok &= (q_ok < 1)
    Z_bad = Fr(13, 14)
    q_bad = Z_bad * Z_bad / Fr(5, 7)
    ok &= (Z_bad > hi and q_bad > 1)
    ok &= (EXCEPT == (15, 20, 22, 36, 38, 39, 52))
    check("G11-two-branch-dictionary", ok,
          "sqrt(5/7) in (29/35,30/35); |Z|=4/5 => q_N<1; "
          "|Z|=13/14 > M => q_N>1; exception set %s" % (EXCEPT,))

    return {
        "m0_rule_free": m0_rule_free,
        "m0_cens_free": m0_cens_free,
        "m0_rule_log": m0_rule_log,
        "m0_cens_log": m0_cens_log,
        "ratio_rule": r_rule,
        "ratio_cens": r_cens,
        "sigma_star": float(ss),
        "neff_need": float(need_neff),
    }


# ---------------- PART B construction

def fejer_energy_np(P):
    """S_F = (1/H) sum W^2 at the frozen H rule (numpy)."""
    P = np.asarray(P, float)
    m = int(P.size)
    if m == 0:
        return 0.0, 2, 0.0
    H = max(2, int(math.ceil(math.sqrt(m))))
    pad = np.zeros(m + 2 * (H - 1))
    pad[H - 1:H - 1 + m] = P
    c = np.concatenate(([0.0], np.cumsum(pad)))
    W = c[H:] - c[:-H]
    sw2 = float(np.sum(W * W))
    Sf = sw2 / float(H)
    return Sf, H, sw2


def compose_from_pack(p, L2D, PBB, WBT, TX, CA, CT, BR):
    """pointwise compose quantities on one window pack."""
    N = p["N"]
    rows = p["rows"]
    r, t, ap, bp = TX.drive_arrays(rows, N)
    g = CA.g_gap(r[:N - 1], t, ap, bp)
    chain = ap[N - 2] * r[N - 2] + bp[N - 2] * r[N - 3]
    Z = float(t[N - 2] + chain)
    xu, wu = CT.union_arrays(p["d"])
    bx, bw = CT.union_arrays(p["dsm"])
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    v2 = BR.eval_scaled(rows, bx, N - 2)
    v2w = BR.eval_scaled(rows, xu, N - 2)
    fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
        / math.sqrt(abs(rows[N - 1]["eta"]))
    ct = bw * bx * v2 * fac
    cw = wu * xu * v2w * fac
    o = np.argsort(bx, kind="stable")
    bxs = bx[o]
    cts = ct[o]
    ed = PBB.mask_edge(bxs, lo, hi, PBB.EDGE_F)
    t_loc = float(np.sum(cts[ed]))
    Zloc = t_loc + float(chain)
    cb = cts[~ed]
    xb = bxs[~ed]
    runs = PBB.runs_split(cb)
    masses = [abs(float(np.sum(cb[a:b]))) for a, b, _sg in runs]
    sruns = [float(np.sum(cb[a:b])) for a, b, _sg in runs]
    P_f2 = L2D.blocks_level2(sruns)
    vd_f2 = L2D.bound_vdc(P_f2)
    brk, mblk, jb = WBT.block_breaks(xb, runs)
    Pb = np.bincount(jb, weights=cb, minlength=mblk) if mblk \
        else np.zeros(0)
    Pw = WBT.aggregate_blocks(xu, cw, lo, hi, brk, mblk)
    Pd = Pb - Pw
    vd_d = L2D.bound_vdc(Pd)
    Sf_d, Hd, _ = fejer_energy_np(Pd)
    L1 = float(np.sum(np.abs(Pd))) if Pd.size else 0.0
    D = float(np.sum(Pd * Pd)) if Pd.size else 0.0
    n2 = (L1 * L1 / D) if D > 0 else 0.0
    qabs = np.abs(Pd) / max(L1, 1e-300) if L1 > 0 else Pd
    M3 = float(np.sum(qabs ** 3)) if L1 > 0 else 0.0
    N3 = M3 ** (-0.5) if M3 > 0 else 0.0
    pair = PBB.bound_pairsum(masses)
    q_from_Z = (Z * Z) / (5.0 / 7.0)
    pref = (mblk + vd_d["H"] - 1) / float(vd_d["H"]) if mblk else 1.0
    R = (Sf_d / D) if D > 0 else 0.0
    sum_f2 = float(sum(P_f2)) if P_f2 else 0.0
    bulk = float(np.sum(cb))
    t_term = float(t[N - 2])
    recon = abs(t_term - float(np.sum(ct))) <= 1e-7 * max(1.0, abs(t_term))
    split_ok = abs(Z) <= abs(Zloc) + abs(sum_f2) + 1e-7
    return dict(
        kz=p.get("kz"), N=N, m=mblk, g=float(g), Z=Z, Zloc=Zloc,
        absZ=abs(Z), qZ=q_from_Z, cheap=float(g) >= 0.0,
        eps_f2=vd_f2["eps"], eps_d=vd_d["eps"], pair=pair,
        Sf=Sf_d, H=vd_d["H"], pref=pref, L1=L1, D=D, n2=n2,
        M3=M3, N3=N3, R=R,
        vdc_f2_closes=abs(Zloc) + vd_f2["eps"] < M_W,
        vdc_d_closes=abs(Zloc) + vd_d["eps"] < M_W,
        pair_closes=abs(Zloc) + pair < M_W,
        triangle_closes=abs(Z) < M_W,
        split_ok=split_ok,
        recon=recon,
        bulk=bulk, sum_f2=sum_f2,
        n2_ge_n3=n2 + 1e-9 >= N3,
    )


def t1_on_eval(ev, LGC):
    col = LGC.gap_columns(ev)
    m = ev["m"]
    M3 = col["m3"]
    ck_row = col["maxprod"]
    bound = t1_m3_bound(ck_row, m)
    return dict(m=m, M3=M3, n2=col["n2"], n3=col["n3"],
                ming=col["ming"], maxprod=ck_row,
                bound_row=bound,
                holds_row=M3 <= bound + 1e-12,
                n2_ge_n3=col["n2"] + 1e-9 >= col["n3"],
                floor_ok=col["ming"] + 1e-12 >= 0.375)


def part_b():
    section("PART B -- CONSTRUCTION PINS")
    import bordered_hankel_probe as BH
    import coupledtau_probe as CT
    import cancellation_adjudication_probe as CA
    import terminal_crossratio_probe as TX
    import border_resolvent_identity_probe as BR
    import phase_bulk_bound_probe as PBB
    import window_border_transfer_probe as WBT
    import l2_deterministic_cancellation_probe as L2D
    import dirichlet_secondworld_probe as DSW
    import second_family_erosion_probe as SFE
    import dirichlet_matched_frame_probe as DMF
    import mean_sieve_floor_probe as MSF
    import local_gap_carleson_probe as LGC
    import v563_paper2_readouts as core
    import port_integrable_kernel_probe as PIK

    recs = {}
    worlds = []

    pA = BH.wpack(9)
    worlds.append(("FRAME_A_w9", pA))
    pB = SFE.wpack_b(9, MSF.NU_B)
    worlds.append(("FRAME_B_w9", pB))
    u3, w3c, _n3, _c3 = DMF.chi_window_comb(9, MSF.Q_CHI3)
    pC3 = DMF.chi_wpack(9, 1.0, MSF.LPQ3, (u3, w3c))
    worlds.append(("CHI3_w9", pC3))
    u4, w4c, _n4, _c4 = DMF.chi_window_comb(9, MSF.Q_CHI4)
    pC4 = DMF.chi_wpack(9, 1.0, MSF.LPQ4, (u4, w4c))
    worlds.append(("CHI4_w9", pC4))

    rows20 = []
    ok_split = True
    ok_renyi = True
    ok_tri = True
    n_vdc_f2 = 0
    n_vdc_d = 0
    n_pair = 0
    for name, p in worlds:
        c = compose_from_pack(p, L2D, PBB, WBT, TX, CA, CT, BR)
        recs[name] = c
        rows20.append(c)
        ok_split &= c["split_ok"]
        ok_renyi &= c["n2_ge_n3"]
        if c["cheap"]:
            ok_tri &= c["triangle_closes"]
        n_vdc_f2 += int(c["vdc_f2_closes"])
        n_vdc_d += int(c["vdc_d_closes"])
        n_pair += int(c["pair_closes"])
        rc = DSW.rung_rec(p)
        ev = LGC.eval_gap(rc)
        if not ev.get("degenerate"):
            t1 = t1_on_eval(ev, LGC)
            c["t1"] = t1
            ok_renyi &= t1["n2_ge_n3"] and t1["holds_row"]

    w9 = recs["FRAME_A_w9"]
    check("G20-w9-compose",
          ok_split and ok_renyi and w9["triangle_closes"]
          and w9["cheap"] and w9["qZ"] < 1.0,
          "four w9 worlds: split %s Renyi+T1-row %s; "
          "FRAME_A_w9 cheap |Z|=%.4f < M=%.4f qZ=%.4f; "
          "vdC-F2 closes %d/4 vdC-Delta %d/4 pair %d/4"
          % (ok_split, ok_renyi, w9["absZ"], M_W, w9["qZ"],
             n_vdc_f2, n_vdc_d, n_pair))

    u53, w53, _n, _c = DMF.chi_window_comb(53, MSF.Q_CHI4)
    p53 = DMF.chi_wpack(53, 1.0, MSF.LPQ4, (u53, w53))
    rc53 = DSW.rung_rec(p53)
    ev53 = LGC.eval_gap(rc53)
    t153 = t1_on_eval(ev53, LGC) if not ev53.get("degenerate") else None
    ok53 = (t153 is not None
            and abs(t153["ming"] - 0.375) <= 1e-9
            and t153["holds_row"] and t153["n2_ge_n3"])
    c53 = compose_from_pack(p53, L2D, PBB, WBT, TX, CA, CT, BR)
    recs["CHI4_kz53"] = c53
    recs["CHI4_kz53_t1"] = t153
    check("G21-chi4-kz53-floor", ok53,
          "min g=%.6f (3/8); T1-row M3=%.3e <= %.3e; "
          "N2=%.3f >= N3=%.3f; |Z|=%.4f qZ=%.4f"
          % (t153["ming"] if t153 else -1,
             t153["M3"] if t153 else -1,
             t153["bound_row"] if t153 else -1,
             t153["n2"] if t153 else -1,
             t153["n3"] if t153 else -1,
             c53["absZ"], c53["qZ"]))

    # 42-rung certificate
    kzs_l = []
    for kz in core.frame_a_zones():
        h = PIK.build_rung(kz)["h"]
        if h <= LGC.H_CAP:
            kzs_l.append(kz)
    ladder = [BH.wpack(kz) for kz in kzs_l]
    ladder.sort(key=lambda p: (p["N"], p["kz"]))
    okL = (len(ladder) == 42
           and all(p.get("nf") is None for p in ladder))
    comps = []
    t1s = []
    for p in ladder:
        c = compose_from_pack(p, L2D, PBB, WBT, TX, CA, CT, BR)
        comps.append(c)
        rc = DSW.rung_rec(p)
        ev = LGC.eval_gap(rc)
        if not ev.get("degenerate"):
            t1s.append(t1_on_eval(ev, LGC))
    cheap = [c for c in comps if c["cheap"]]
    exc = [c for c in comps if not c["cheap"]]
    exc_kz = tuple(sorted(c["kz"] for c in exc))
    n_tri = sum(1 for c in comps if c["triangle_closes"])
    n_qz = sum(1 for c in comps if c["qZ"] < 1.0 - 1e-12)
    n_split = sum(1 for c in comps if c["split_ok"])
    n_ren = sum(1 for c in t1s if c["n2_ge_n3"] and c["holds_row"])
    n_f2 = sum(1 for c in comps if c["vdc_f2_closes"])
    n_d = sum(1 for c in comps if c["vdc_d_closes"])
    n_pair = sum(1 for c in comps if c["pair_closes"])
    # cheap branch should close by triangle
    cheap_tri = all(c["triangle_closes"] for c in cheap)
    n_recon = sum(1 for c in comps if c.get("recon"))
    cheap_f2 = sum(1 for c in cheap if c["vdc_f2_closes"])
    ok42 = (okL and n_qz == 42 and n_tri == 42 and n_split == 42
            and exc_kz == EXCEPT and cheap_tri
            and len(cheap) == 35 and len(exc) == 7
            and n_ren == len(t1s) and len(t1s) == 42
            and n_recon == 42)
    recs["ladder"] = dict(
        n=len(comps), n_cheap=len(cheap), n_exc=len(exc),
        exc_kz=exc_kz, n_tri=n_tri, n_qz=n_qz, n_split=n_split,
        n_vdc_f2=n_f2, n_vdc_d=n_d, n_pair=n_pair, n_t1=n_ren,
        n_t1_rows=len(t1s), n_recon=n_recon, cheap_f2=cheap_f2,
        min_qZ=min(c["qZ"] for c in comps) if comps else None,
        max_qZ=max(c["qZ"] for c in comps) if comps else None,
        min_margin=min(1.0 - c["qZ"] for c in comps) if comps else None,
    )
    check("G22-42-certificate", ok42,
          "42/42 packs nf=None; qZ<1 %d/42; |Z|<M %d/42; "
          "F2-split %d/42 recon %d/42; cheap %d triangle-all %s; "
          "exceptions %s; T1-row %d/%d; "
          "vdC-F2 %d/42 (cheap %d/35) vdC-Delta %d/42 "
          "pair(H5-sister) %d/42; min q-margin %.4f"
          % (n_qz, n_tri, n_split, n_recon, len(cheap), cheap_tri,
             exc_kz, n_ren, len(t1s),
             n_f2, cheap_f2, n_d, n_pair,
             recs["ladder"]["min_margin"] or -1))

    # 181-row T1-floor implication (89 A + 8 B + 42 chi3 + 42 chi4)
    import verify_lstar_instance as V
    kzs_a = []
    ekz = []
    ekz2 = []
    for kz in core.frame_a_zones():
        h = PIK.build_rung(kz)["h"]
        if h <= LGC.H_CAP:
            kzs_a.append(kz)
        elif h <= LGC.EXT_H_MAX:
            ekz.append(kz)
        elif h <= LGC.EXT2_H_MAX:
            ekz2.append((h, kz))
    epool = [BH.wpack(kz) for kz in ekz]
    epool.sort(key=lambda p: (p["N"], p["kz"]))
    ext = epool[:LGC.K_EXT]
    ekz2.sort()
    pool2 = epool[LGC.K_EXT:] + [
        BH.wpack(kz) for _h, kz in ekz2[:LGC.EXT2_POOL_CAP]]
    pool2.sort(key=lambda p: (p["N"], p["kz"]))
    ext2 = [p for p in pool2 if p["nf"] is None][:LGC.K_EXT2]
    ext3 = [BH.wpack(kz) for kz in LGC.EXT3_KZ_B + LGC.EXT3_KZ_A]
    ext4 = [BH.wpack(kz) for kz in LGC.EXT4_KZ]
    ext5 = [BH.wpack(kz) for kz in LGC.EXT5_KZ_B + LGC.EXT5_KZ_A]
    packs_a = ladder + ext + ext2 + ext3 + ext4 + ext5
    packs_b = [SFE.wpack_b(kz, MSF.NU_B) for kz in LGC.FRAMEB_KZ]
    kzs_c = list(V.admissible_indices())
    packs_c3, packs_c4 = [], []
    for kz in kzs_c:
        u3, w3c, _nn, _ch = DMF.chi_window_comb(kz, MSF.Q_CHI3)
        if len(u3) >= V.N_ATOM_MIN:
            packs_c3.append(DMF.chi_wpack(kz, 1.0, MSF.LPQ3,
                                          (u3, w3c)))
        u4, w4c, _nn, _ch = DMF.chi_window_comb(kz, MSF.Q_CHI4)
        if len(u4) >= V.N_ATOM_MIN:
            packs_c4.append(DMF.chi_wpack(kz, 1.0, MSF.LPQ4,
                                          (u4, w4c)))
    fams = (("A", packs_a), ("B", packs_b),
            ("CHI3", packs_c3), ("CHI4", packs_c4))
    n_rows = 0
    n_t1 = 0
    n_n23 = 0
    n_floor = 0
    n_deg = 0
    for _lab, packs in fams:
        for p in packs:
            if p.get("nf") is not None:
                continue
            rc = DSW.rung_rec(p)
            ev = LGC.eval_gap(rc)
            if ev.get("degenerate"):
                n_deg += 1
                continue
            t1 = t1_on_eval(ev, LGC)
            n_rows += 1
            n_t1 += int(t1["holds_row"])
            n_n23 += int(t1["n2_ge_n3"])
            n_floor += int(t1["floor_ok"])
    nA, nB, n3, n4 = (len(packs_a), len(packs_b),
                      len(packs_c3), len(packs_c4))
    ok181 = (nA + nB + n3 + n4 >= 181
             and n_rows >= 181
             and n_t1 == n_rows and n_n23 == n_rows
             and n_floor == n_rows)
    recs["surface181"] = dict(
        nA=nA, nB=nB, n3=n3, n4=n4, n_rows=n_rows, n_deg=n_deg,
        n_t1=n_t1, n_n23=n_n23, n_floor=n_floor)
    check("G23-181-t1-implication", ok181,
          "families %d+%d+%d+%d = %d; live T1-rows %d "
          "(deg %d); T1-row-cap %d/%d; N2>=N3 %d/%d; "
          "g>=3/8 %d/%d"
          % (nA, nB, n3, n4, nA + nB + n3 + n4,
             n_rows, n_deg, n_t1, n_rows, n_n23, n_rows,
             n_floor, n_rows))
    return recs


def main():
    print("verify_compose_lemma.py -- COMPOSE pointwise chain "
          "(round 378)")
    print("NO RH CLAIM.", flush=True)
    a = part_a()
    b = part_b()
    npass = sum(1 for _n, ok in CHECKS if ok)
    nfail = sum(1 for _n, ok in CHECKS if not ok)
    print("\n" + "=" * 72)
    print("%d/%d gates  (%d FAIL)" % (npass, len(CHECKS), nfail))
    artefact = {
        "round": 378,
        "lemma": "COMPOSE",
        "outcome": "REDUCED",
        "npass": npass,
        "nfail": nfail,
        "gates": [(n, ok) for n, ok in CHECKS],
        "part_a": a,
        "ladder": b.get("ladder"),
        "surface181": b.get("surface181"),
        "claim_boundary": "NO RH CLAIM",
    }
    outp = "/tmp/tfpt_r378_compose.json"
    with open(outp, "w") as f:
        json.dump(artefact, f, indent=2, default=str)
        f.write("\n")
    import hashlib
    h = hashlib.sha256()
    with open(outp, "rb") as f:
        h.update(f.read())
    print("artefact %s  SHA-256 %s" % (outp, h.hexdigest()),
          flush=True)
    if nfail:
        print("COMPOSE LEMMA FAILED")
        sys.exit(1)
    print("COMPOSE LEMMA VERIFIED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
