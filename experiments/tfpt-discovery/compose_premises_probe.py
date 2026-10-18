#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""compose_premises_probe -- LEMMA.COMPOSE.PREMISES.01 (round 383):
THE THREE COMPOSE INPUTS (R), (L), (Z).

Coexistence: r378 reduced COMPOSE to the pointwise implication
  M3 <= phi(m)  and  (R) S_F <= R0 D  and  (L) L1 <= Lambda
  (or L1 = O(m^gamma), gamma < 1/4)  and  (Z) |Z_loc| <= Z0 < M
  ==> |Z| < M  (and q_N < 1 given the r263 dictionary).
This round attacks the three named remainders, sharing the
canonical-window Fejer / vdC machinery.  T1-combo
(M3 = ((log m)^2/m^2) T2 E_pi(F^2)) is tested as a joint
route for (L) and T1.

LEGS (lemma-first; each exit PROVED / REFUTED / REDUCED):
  R  S_F <= R0 D with an absolute R0 (trivial envelope H is
     too coarse; fold-parity of B(omega,omega) as a pairing
     SATZ is tested, not assumed).
  L  L1 <= Lambda, or L1 = O(m^gamma) with proved gamma < 1/4
     from von Mangoldt / FAB / K2, or the T1-floor identity
     plus a proved T2 E_pi(F^2) bound.
  Z  |Z_loc| <= Z0 < M = sqrt(5/7), PNT-free Chebyshev/Rosser
     on a finite head, or a conditional m2 + finite census.
  K  scramble must break (R) or (L); mutants R0/2 and gamma=1/4
     must fail; chi as second world on the 181-census.

CALIBRATION DISCLOSURE.  Numbers below were first measured in
/tmp/tfpt_r383_cal.py (WALL 622.3 s, 181 live rows) on the same
constructors, 2026-08-28.  Frozen constants are that measurement,
sealed as gates -- not a search over R0/Lambda/Z0.  No two-commit
pre-blind freeze: pins disclosed.

FROZEN FROM /tmp (live re-gated, not fitted):
  * sup S_F/D on 181 = 2.91678766 at FRAME-A kz37 (H=15).
    R0 = 4 (<= 2 x measured sup 5.8336; integer).  R0/2 = 2
    fails on 17/181.  Trivial envelope H_max=29.  n_R_gt_H=0.
  * MAIN/S_F med 0.00860 (empty for composition); max 0.157 at
    CHI3 kz29.  pair_w med 0.512 -- NOT exact fold pairing.
    rho1_w med -0.459 (window block field is anti-correlated).
  * L1_max = 2.12619 at FRAME-B kz124.  Lambda = 3.  Log-log
    slope(L1) = +0.202 on the 42 / +0.223 on FRAME-A 89 /
    +0.243 on 181.  Triangle TV slope +0.307 on A (>= 1/4).
  * T2 E_pi identity rel <= 1.5e-15 on 181 (SATZ).  E_pi max
    52.276 (A kz111) / 75.691 (B kz117): T1-combo REFUTED as
    a family-uniform E_pi bound (r368 SPIKES_DOMINATE_PI).
    T2_max = 1.329 < (8/3)^2 = 7.111 (floor would cap T2).
  * |Z_loc| max FRAME-A = 0.755675 at kz16 < M=0.845154.
    Z0 = 4/5 = 0.8.  89/89 A and 8/8 B and 42/42 ladder
    satisfy |Z_loc| < Z0.  Chi REFUTES |Z_loc| < M on six
    windows: CHI3 {15,19,23,33,39}, CHI4 {20}.  175/181
    have |Z_loc| < M.  n_edge 167..4689 (NOT a finite head).
  * SCRAMBLE seed=1 w9: R=0.598 does NOT break (R); L1=0.492
    does NOT break Lambda=3.  Named (L) break is the T1/M3
    polylog: M3 exceeds r306 C=1.069 (log m)^2/m^2 (MAIN w9
    holds).  E_pi 2.44 vs MAIN 0.47.
  * gamma=1/4 mutant: T1 M3 ~ (log m)^2/m^2 vs phi ~ m^{-2}
    requires (log m)^2 bounded, which fails.

MACHINERY IMPORTED VERBATIM (SPEC_SHA prefix gated): r298
WBT, r287 L2D, r269 PBB, r358 LGC (identity pins only),
r357 DMF, r353 SFE, r361 MSF, r244 BH, r257 CT, r263 CA,
r260 TX, r266 BR, r368 WL2 identity helpers used as a
formula not a census freeze.

NO RH CLAIM.  Finite identities, named reductions, a named
scramble break.  Research documentation, not a theorem of RH.
Sealed gates: 12/12 smoke / 20/20 full (G1--G7 toys, G10--G14
pins, G20--G27 census).  Companion verifier adds G8/G9/G9b/G9c.
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
VERIFY = os.path.join(REPO, "verification")
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, VERIFY, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import bordered_hankel_probe as BH  # noqa: E402
import coupledtau_probe as CT  # noqa: E402
import cancellation_adjudication_probe as CA  # noqa: E402
import terminal_crossratio_probe as TX  # noqa: E402
import border_resolvent_identity_probe as BR  # noqa: E402
import phase_bulk_bound_probe as PBB  # noqa: E402
import window_border_transfer_probe as WBT  # noqa: E402
import l2_deterministic_cancellation_probe as L2D  # noqa: E402
import dirichlet_secondworld_probe as DSW  # noqa: E402
import second_family_erosion_probe as SFE  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import mean_sieve_floor_probe as MSF  # noqa: E402
import local_gap_carleson_probe as LGC  # noqa: E402
import v563_paper2_readouts as core  # noqa: E402
import port_integrable_kernel_probe as PIK  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

# disclosed /tmp pins
M_W = math.sqrt(5.0 / 7.0)
R0 = 4.0
R0_HALF = 2.0
R_STAR = 2.9167876597574613
R_STAR_KZ = 37
LAMBDA = 3.0
L1_STAR = 2.1261947535704877
Z0 = 0.8
Z_STAR_A = 0.7556749150210934
Z_STAR_KZ = 16
R306_C = 1.069
ID_BAR = 1e-12
DEC_BAR = 1e-9
N_181 = 181
N_A, N_B, N_C3, N_C4 = 89, 8, 42, 42
N_R_GT_2 = 17
N_ZLOC_LT_M = 175
CHI_Z_VIOL = {
    ("CHI3", 15), ("CHI3", 19), ("CHI3", 23),
    ("CHI3", 33), ("CHI3", 39), ("CHI4", 20),
}
SCR_SEED = 1
CAP = Fr(8, 3)

WBT_SHA_PREFIX = "05e831be"
L2D_SHA_PREFIX = "761d88fa"
LGC_SHA_PREFIX = "fb2d499f"
DMF_SHA_PREFIX = "4bf1a94b"
SFE_SHA_PREFIX = "bd89e331"
MSF_SHA_PREFIX = "1bec7175"

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
    return (not bad), ("NO zero/prime oracles; constructors consume "
                       "measure arrays / positions only"
                       if not bad else "; ".join(bad))


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def lambda_n(n):
    """von Mangoldt Lambda via trial division (PNT-free)."""
    if n < 2:
        return 0.0
    k, m = 0, n
    while m % 2 == 0:
        k += 1
        m //= 2
    if k:
        return math.log(2.0) if m == 1 else 0.0
    d = 3
    while d * d <= n:
        k = 0
        while m % d == 0:
            k += 1
            m //= d
        if k:
            return math.log(d) if m == 1 else 0.0
        d += 2
    return math.log(n) if m == n else 0.0


def pair_cancel_ratio(P):
    P = np.asarray(P, float)
    n = (len(P) // 2) * 2
    if n < 2:
        return 1.0
    a, b = P[:n:2], P[1:n:2]
    num = float(np.sum(np.abs(a + b)))
    den = float(np.sum(np.abs(a) + np.abs(b)))
    return num / max(den, 1e-300)


def m3_r306_bound(m):
    lg = math.log(float(m))
    return R306_C * (lg * lg) / (float(m) * float(m))


def phi_of(m, R0_=R0, Lam=LAMBDA, z0=Z0):
    """compose M3-cap of r378, with pref <= sqrt(m)+1."""
    pref = math.sqrt(float(m)) + 1.0
    gap = M_W - float(z0)
    return (gap ** 4) / (pref * pref * float(R0_) * float(R0_)
                         * float(Lam) ** 4)


def t1_m3(ck, m):
    lg = math.log(float(m))
    return float(CAP) ** 2 * float(ck) * float(ck) * (lg * lg) / (
        float(m) * float(m))


def row_of(p, with_t1=False):
    """compose + r298 split on one window pack.  Source-pure:
    positions, weights, chain values.  T1 columns optional."""
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
    bxs, cts = bx[o], ct[o]
    ed = PBB.mask_edge(bxs, lo, hi, PBB.EDGE_F)
    t_loc = float(np.sum(cts[ed]))
    Zloc = t_loc + float(chain)
    cb, xb = cts[~ed], bxs[~ed]
    t_bulk = float(np.sum(cb)) if cb.size else 0.0
    # Lean canonical_split: Z = t_loc + chain + t_bulk = Zloc + t_bulk.
    # NOT |sum Pd|: Pd is the F2 block difference, a different object.
    split_dev = abs(Z - Zloc - t_bulk)
    split_ok = split_dev <= 1e-8 * max(1.0, abs(Z), abs(Zloc), abs(t_bulk))
    runs = PBB.runs_split(cb)
    brk, mblk, jb = WBT.block_breaks(xb, runs)
    Pb = np.bincount(jb, weights=cb, minlength=mblk) if mblk \
        else np.zeros(0)
    Pw = WBT.aggregate_blocks(xu, cw, lo, hi, brk, mblk)
    Pd = Pb - Pw
    H = max(2, int(math.ceil(math.sqrt(max(mblk, 1)))))
    Sf = WBT.fejer_bil(Pb, Pb, H) if mblk else 0.0
    MAIN = WBT.fejer_bil(Pw, Pw, H) if mblk else 0.0
    Tdel = WBT.fejer_bil(Pd, Pb + Pw, H) if mblk else 0.0
    L1 = float(np.sum(np.abs(Pd))) if Pd.size else 0.0
    D = float(np.dot(Pd, Pd)) if Pd.size else 0.0
    qabs = (np.abs(Pd) / max(L1, 1e-300)) if L1 > 0 else Pd
    M3 = float(np.sum(qabs ** 3)) if L1 > 0 else 0.0
    R = (Sf / D) if D > 0 else 0.0
    out = dict(
        kz=p.get("kz"), N=N, m=int(mblk), H=H, g=float(g),
        Z=Z, Zloc=Zloc, absZ=abs(Z), absZloc=abs(Zloc),
        t_bulk=t_bulk, split_dev=split_dev,
        Sf=Sf, MAIN=MAIN, Tdel=Tdel, L1=L1, D=D, M3=M3, R=R,
        n_edge=int(np.sum(ed)), n_atom=int(len(cts)),
        main_over_Sf=MAIN / max(abs(Sf), 1e-300),
        pair_w=pair_cancel_ratio(Pw),
        split_ok=split_ok,
        dec_dev=abs(Sf - MAIN - Tdel) / max(abs(Sf), abs(MAIN),
                                            abs(Tdel), 1e-300),
        r306=m3_r306_bound(max(mblk, 2)),
        t2=None, epi=None, id_dev=None,
    )
    if with_t1:
        rc = DSW.rung_rec(p)
        ev = LGC.eval_gap(rc)
        if not ev.get("degenerate"):
            col = LGC.gap_columns(ev)
            t2 = col["t2v"]
            q, gg = col["q"], col["g"]
            lg = math.log(max(mblk, 2))
            F = (float(mblk) * q / lg) * gg
            wpi = q / (gg * gg)
            pi = wpi / max(float(np.sum(wpi)), 1e-300)
            epi = float(np.dot(pi, F * F))
            rhs = (lg * lg) / (float(mblk) * float(mblk)) * t2 * epi
            out["t2"] = t2
            out["epi"] = epi
            out["id_dev"] = abs(M3 - rhs) / max(abs(M3), 1e-300)
            out["ming"] = col["ming"]
    return out


def load_surface():
    kzs_l, ekz, ekz2 = [], [], []
    for kz in core.frame_a_zones():
        h = PIK.build_rung(kz)["h"]
        if h <= LGC.H_CAP:
            kzs_l.append(kz)
        elif h <= LGC.EXT_H_MAX:
            ekz.append(kz)
        elif h <= LGC.EXT2_H_MAX:
            ekz2.append((h, kz))
    ladder = [BH.wpack(kz) for kz in kzs_l]
    ladder.sort(key=lambda p: (p["N"], p["kz"]))
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
    packs_c3, packs_c4 = [], []
    for kz in V.admissible_indices():
        u3, w3c, _n, _c = DMF.chi_window_comb(kz, MSF.Q_CHI3)
        if len(u3) >= V.N_ATOM_MIN:
            packs_c3.append(DMF.chi_wpack(kz, 1.0, MSF.LPQ3,
                                          (u3, w3c)))
        u4, w4c, _n, _c = DMF.chi_window_comb(kz, MSF.Q_CHI4)
        if len(u4) >= V.N_ATOM_MIN:
            packs_c4.append(DMF.chi_wpack(kz, 1.0, MSF.LPQ4,
                                          (u4, w4c)))
    return dict(A=packs_a, B=packs_b, CHI3=packs_c3, CHI4=packs_c4,
                ladder=ladder)


def part_toys():
    section("TOYS / SATZ (no window builders)")
    P = np.array([1.0, -1.0] * 8)
    H = 4
    Sf = WBT.fejer_bil(P, P, H)
    D = float(np.dot(P, P))
    check("G1-period2-even-H",
          abs(Sf - 1.0) < 1e-12 and abs(D - 16.0) < 1e-12
          and abs(Sf / D - 1.0 / 16.0) < 1e-12,
          "S_F=%.6f D=%.6f R=%.6f (exact 1/16, not 0: edge windows)"
          % (Sf, D, Sf / D))
    Q = np.ones(16)
    Sdc = WBT.fejer_bil(Q, Q, 4)
    Ddc = float(np.dot(Q, Q))
    Rdc = Sdc / Ddc
    check("G2-DC-envelope-and-R0half",
          Rdc <= 4.0 + 1e-12 and Rdc > R0_HALF
          and Rdc <= 4.0 + 1e-9,
          "DC R=%.4f <= H=4 and <= R0=4; mutant R0/2=2 FAILS"
          % Rdc)
    u = np.array([1.0, 0.0, -1.0, 2.0])
    v = np.array([0.5, -0.5, 1.0, 0.0])
    Buv = WBT.fejer_bil(u, v, 2)
    Buu = WBT.fejer_bil(u, u, 2)
    Bvv = WBT.fejer_bil(v, v, 2)
    check("G3-fejer-CS",
          Buv * Buv <= Buu * Bvv + 1e-12,
          "B(u,v)^2=%.6f <= B(u,u)B(v,v)=%.6f" % (Buv * Buv, Buu * Bvv))
    q = np.array([0.5, 0.3, 0.2])
    gg = np.array([0.5, 0.4, 0.6])
    m = 10.0
    lg = math.log(m)
    F = (m * q / lg) * gg
    t2 = float(np.sum(q / gg ** 2))
    pi = (q / gg ** 2) / t2
    epi = float(np.dot(pi, F * F))
    m3 = float(np.sum(q ** 3))
    rhs = (lg * lg) / (m * m) * t2 * epi
    check("G4-M3-L2-identity",
          abs(m3 - rhs) / m3 < 1e-12,
          "M3=%.12f rhs=%.12f rel=%.3e" % (m3, rhs, abs(m3 - rhs) / m3))
    # gamma=1/4: T1 vs phi with L1 = m^{1/4}, R0=4, Z0=4/5, C_K=1
    m_big = 1.0e6
    t1 = t1_m3(1.0, m_big)
    lam = m_big ** 0.25
    ph = phi_of(m_big, R0, lam, Z0)
    check("G5-gamma-quarter-mutant",
          t1 > ph,
          "T1 M3=%.3e > phi=%.3e at m=1e6, L1=m^{1/4} "
          "(logs unbounded at equality gamma=1/4)"
          % (t1, ph))
    ok_l = True
    for n in range(2, 121):
        ok_l &= (lambda_n(n) <= math.log(n) + 1e-12)
        if n >= 2 and is_prime(n):
            ok_l &= abs(lambda_n(n) - math.log(n)) < 1e-12
    check("G6-Lambda-le-log",
          ok_l,
          "Lambda(n)<=log n on n=2..120 (trial division, PNT-free)")
    fw_ok, fw_d = firewall_audit()
    sha_ok = (WBT.SPEC_SHA.startswith(WBT_SHA_PREFIX)
              and L2D.SPEC_SHA.startswith(L2D_SHA_PREFIX)
              and LGC.SPEC_SHA.startswith(LGC_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and SFE.SPEC_SHA.startswith(SFE_SHA_PREFIX)
              and MSF.SPEC_SHA.startswith(MSF_SHA_PREFIX))
    check("G7-firewall-and-sha",
          fw_ok and sha_ok,
          "%s; WBT/L2D/LGC/DMF/SFE/MSF prefixes"
          % fw_d)


def part_pins():
    section("CONSTRUCTION PINS (w9 + scramble + R-star + Z-star)")
    pA = BH.wpack(9)
    a = row_of(pA, with_t1=True)
    check("G10-w9-R-L-Z",
          a["R"] <= R0 and a["L1"] <= LAMBDA and a["absZloc"] < Z0
          and a["dec_dev"] < DEC_BAR and a["split_ok"]
          and a["id_dev"] is not None and a["id_dev"] < ID_BAR
          and a["M3"] <= a["r306"] + 1e-12,
          "R=%.4f<=4 L1=%.4f<=3 |Zloc|=%.4f<0.8 MAIN/Sf=%.3e "
          "dec=%.1e id=%.1e M3<=r306 pair_w=%.3f n_edge=%d"
          % (a["R"], a["L1"], a["absZloc"], a["main_over_Sf"],
             a["dec_dev"], a["id_dev"] or -1, a["pair_w"], a["n_edge"]))
    pS = BH.wpack(9, dict(scramble_seed=SCR_SEED))
    s = row_of(pS, with_t1=True)
    brk_R = s["R"] > R0
    brk_L_abs = s["L1"] > LAMBDA
    brk_L_m3 = s["M3"] > s["r306"]
    check("G11-scramble-breaks-L-via-M3",
          (not brk_R) and (not brk_L_abs) and brk_L_m3
          and a["M3"] <= a["r306"] + 1e-12,
          "SCR R=%.4f (does NOT break R0=4) L1=%.4f (not Lambda) "
          "M3=%.4e > r306=%.4e (BREAKS (L) on T1/M3 polylog); "
          "MAIN w9 M3=%.4e <= %.4e; E_pi scr=%.3f vs MAIN %.3f"
          % (s["R"], s["L1"], s["M3"], s["r306"], a["M3"], a["r306"],
             s["epi"] or -1, a["epi"] or -1))
    p37 = BH.wpack(R_STAR_KZ)
    a37 = row_of(p37)
    check("G12-R-star-kz37",
          a37["kz"] == R_STAR_KZ
          and abs(a37["R"] - R_STAR) < 1e-4
          and a37["R"] <= R0
          and a37["R"] > R0_HALF,
          "kz37 R=%.6f (pin %.6f) <=4; mutant R0/2=2 FAILS"
          % (a37["R"], R_STAR))
    p16 = BH.wpack(Z_STAR_KZ)
    a16 = row_of(p16)
    check("G13-Z-star-A-kz16",
          a16["kz"] == Z_STAR_KZ
          and abs(a16["absZloc"] - Z_STAR_A) < 1e-4
          and a16["absZloc"] < Z0 < M_W,
          "|Zloc|=%.6f (pin %.6f) < Z0=0.8 < M=%.6f"
          % (a16["absZloc"], Z_STAR_A, M_W))
    p111 = BH.wpack(111)
    a111 = row_of(p111, with_t1=True)
    check("G14-T1-combo-Epi-spike-A-kz111",
          a111["epi"] is not None and a111["epi"] > 40.0
          and a111["id_dev"] is not None and a111["id_dev"] < ID_BAR
          and a111["t2"] is not None and a111["t2"] < float(CAP) ** 2,
          "kz111 E_pi=%.3f >40 (small family-uniform C_K REFUTED); "
          "id_dev=%.1e T2=%.3f < (8/3)^2; identity SATZ, T1-combo "
          "does not close as a theorem"
          % (a111["epi"], a111["id_dev"], a111["t2"]))
    return dict(w9=a, scr=s, kz37=a37, kz16=a16, kz111=a111)


def part_full():
    section("181-WINDOW CENSUS (89 A + 8 B + 42 chi3 + 42 chi4)")
    print("  loading packs...", flush=True)
    fams = load_surface()
    recs = {}
    all_rows = []
    viol = []
    n_R2 = 0
    n_zM = 0
    for lab in ("A", "B", "CHI3", "CHI4"):
        rows = []
        for p in fams[lab]:
            if p.get("nf") is not None:
                continue
            r = row_of(p)
            r["fam"] = lab
            rows.append(r)
            all_rows.append(r)
            if r["R"] > R0_HALF + 1e-12:
                n_R2 += 1
            if r["absZloc"] < M_W:
                n_zM += 1
            if (lab, r["kz"]) in CHI_Z_VIOL:
                viol.append((lab, r["kz"], r["absZloc"]))
        recs[lab] = rows
        print("    %s n=%d R_max=%.4f L1_max=%.4f Zloc_max=%.4f"
              % (lab, len(rows),
                 max(x["R"] for x in rows),
                 max(x["L1"] for x in rows),
                 max(x["absZloc"] for x in rows)),
              flush=True)
    nA, nB, n3, n4 = (len(recs["A"]), len(recs["B"]),
                      len(recs["CHI3"]), len(recs["CHI4"]))
    check("G20-181-counts",
          nA == N_A and nB == N_B and n3 == N_C3 and n4 == N_C4
          and nA + nB + n3 + n4 == N_181,
          "families %d+%d+%d+%d = %d" % (nA, nB, n3, n4,
                                         nA + nB + n3 + n4))
    okR = all(r["R"] <= R0 + 1e-12 for r in all_rows)
    rmax = max(r["R"] for r in all_rows)
    rmax_row = max(all_rows, key=lambda r: r["R"])
    check("G21-R-census-R0-eq-4",
          okR and abs(rmax - R_STAR) < 1e-4
          and rmax_row["kz"] == R_STAR_KZ and rmax_row["fam"] == "A"
          and n_R2 == N_R_GT_2,
          "R<=4 on %d/%d; max=%.6f at %s kz%s; n_R>2 = %d (pin %d)"
          % (N_181, N_181, rmax, rmax_row["fam"],
             rmax_row["kz"], n_R2, N_R_GT_2))
    okL = all(r["L1"] <= LAMBDA + 1e-12 for r in all_rows)
    lmax = max(r["L1"] for r in all_rows)
    check("G22-L-census-Lambda-eq-3",
          okL and abs(lmax - L1_STAR) < 1e-4,
          "L1<=3 on %d/%d; max=%.6f (pin %.6f)"
          % (N_181, N_181, lmax, L1_STAR))
    okZA = all(r["absZloc"] < Z0 for r in recs["A"])
    okZB = all(r["absZloc"] < Z0 for r in recs["B"])
    zA = max(r["absZloc"] for r in recs["A"])
    check("G23-Z-FRAME-A-and-B",
          okZA and okZB and abs(zA - Z_STAR_A) < 1e-4
          and zA < Z0 < M_W,
          "A 89/89 and B 8/8 |Zloc|<0.8; A max=%.6f (pin %.6f)"
          % (zA, Z_STAR_A))
    chi_over = [(r["fam"], r["kz"]) for r in recs["CHI3"] + recs["CHI4"]
                if r["absZloc"] >= M_W - 1e-12]
    check("G24-Z-chi-refutes-family-uniform",
          set(chi_over) == CHI_Z_VIOL and n_zM == N_ZLOC_LT_M,
          "chi |Zloc|>=M on %s (pin 6); 175/181 |Zloc|<M"
          % (sorted(chi_over),))
    n_edge_min = min(r["n_edge"] for r in all_rows)
    n_edge_max = max(r["n_edge"] for r in all_rows)
    check("G25-edge-not-finite-head",
          n_edge_min >= 100 and n_edge_max >= 1000,
          "n_edge min=%d max=%d (geometric F=0.20 is not a "
          "finite von-Mangoldt head)"
          % (n_edge_min, n_edge_max))
    pair_med = float(np.median([r["pair_w"] for r in all_rows]))
    main_med = float(np.median([r["main_over_Sf"] for r in all_rows]))
    check("G26-fold-pairing-refuted-MAIN-empty-census",
          0.45 <= pair_med <= 0.60 and main_med < 0.03,
          "pair_w med=%.3f (not ~0: fold pairing REFUTED); "
          "MAIN/Sf med=%.4f (empty as CENSUS, not a pairing SATZ)"
          % (pair_med, main_med))
    n_dec = sum(1 for r in all_rows if r["dec_dev"] < DEC_BAR)
    n_split = sum(1 for r in all_rows if r["split_ok"])
    check("G27-r298-and-split-181",
          n_dec == N_181 and n_split == N_181,
          "r298 identity %d/%d; Z=Zloc+t_bulk %d/%d "
          "(Lean canonical_split; NOT |sum Pd|)"
          % (n_dec, N_181, n_split, N_181))
    return recs


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    print("=" * 78)
    print("compose_premises_probe -- LEMMA.COMPOSE.PREMISES.01 "
          "(round 383)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM.", flush=True)
    part_toys()
    pins = part_pins()
    if not args.smoke:
        part_full()
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    print("\nRESULT: %d/%d gates PASS%s   SPEC_SHA %s   (%.1fs)"
          % (len(CHECKS) - n_fail, len(CHECKS),
             "" if n_fail == 0 else "  ** FAIL **",
             SPEC_SHA[:16], time.time() - T0))
    print("COMPOSE PREMISES "
          + ("VERIFIED" if n_fail == 0 else "FAILED %d" % n_fail))
    letters = ("(R) REDUCED (R0=4 census 181; fold pairing "
               "REFUTED; MAIN empty CENSUS)  "
               "(L) REDUCED (Lambda=3 census; triangle gamma "
               "REFUTED; T1-combo E_pi REFUTED; measured "
               "gamma~0.20<1/4 not SATZ)  "
               "(Z) REDUCED on FRAME-A (Z0=4/5); REFUTED "
               "family-uniform on chi (6 windows); finite "
               "Chebyshev head REFUTED")
    print("LETTERS: %s" % letters)
    print("T1-COMBO: does NOT carry (E_pi spikes; identity SATZ).")
    print("KILL: scramble breaks (L) on the T1/M3 polylog; "
          "R0/2=2 fails (DC toy + 17/181); gamma=1/4 fails "
          "T1-vs-phi algebra.")
    _ = pins
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
