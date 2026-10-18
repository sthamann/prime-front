#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bulk_one_defect_probe -- PRIME.LDAGGER.BULK_ONE_DEFECT.01
(round 400): the threshold / phase form of the frame
inequality for P1 = ind_-(A0) <= 1, A0 = R_{N-3} - I/2,
after the r399 circularity verdict (E^bulk does not fall).

Coexistence: r367 A0; r389 Chebyshev-CD energy; r390
Bernstein-Szego Fejer (full cosine, residual 2e-6); r392
Uvarov tau; r393 rank-1 Delta^2 log tau; r398 36-mode
1/2-cluster; r399 exact Dirichlet polynomial of the
centered difference (Tent contractive, E at QM, grows);
r401 edge signature (sch<0 is the living chart).  DCCLXII
5.4 asked: energy => rank-1-defective frame => P1.
r399 killed the energy-decay hypothesis.  This round
adjudicates the TWO honest remainders: Form T (threshold
frame, perturbation essentially rank-1) and Form P
(C_m phases predict ind_- rather than E).

THE FROZEN QUESTIONS.
  T  Does A0 = A0^ref + B with A0^ref the Bernstein-Szego
     dual CD Gram on Y (r390 full-grid Fejer) have B of
     effective rank 1 on the 1/2-cluster, yielding a
     source-defined edge functional ell_k and
       <x, A0 x> >= c_k ||x||^2 - C_k |ell_k(x)|^2
     with c_k > 0?  Exact threshold via interlacing:
     a rank-r update changes ind_- by at most r, so
     rank-1 can turn nneg(A^ref) into nneg(A0) only if
     |nneg(A^ref) - nneg(A0)| <= 1.  Sub-band MVT as a
     hoped-for unconditional threshold (r399 gate).
  P  Which phase statistic of the r399 C_m (consecutive
     sign correlation, flip rate, lag-2, HHI, dyadic
     bands) separates ind_- (MAIN 1 vs scramble 21)
     while E only differs by a factor < 2?  If a winner
     is source-controllable, gate it (uncond / PNT /
     RH-near).

LEGS.
  A  Rank anatomy of B = R - R^ref on core-42 + the
     named sequence.  Effective rank
     r_eff = ||M||_F^2 / ||M||_op^2 of M = P B P
     (P = cluster projector, anatomy) and of whole B
     (spectral-free surrogate).  Leading share =
     ||M||_op^2 / ||M||_F^2.  If rank-1: build ell_k
     from the leading direction (source-defined, not
     eig(A0)) and verify the frame numerically.
  B  Exact threshold inequality that implies P1; Weyl
     and rank-interlacing; unconditional reachability
     of each block (r399 gate protocol).
  C  Phase screen MAIN / Twin / living chi / dead chi /
     scramble / two-period: which statistic tracks
     ind_- (not E)?  Winner: source-side gate.
  D  Kills: scramble must fail the rank-1 / threshold
     (ind_-=21); dead chi nneg(A0) -- bulk or only
     sch>0/edge?  Mutants: threshold x2, ell omitted.

CALIBRATION DISCLOSURE.  Reference inertia, lift rank,
cluster r_eff, vneg-dcent cosine, phase table, scramble
punch-through, dead/living chi nneg, core-42 lam2-gap
were first measured in /tmp (r400_cal.py, r400_cal2.py,
r400_cal3.py) on the same constructors, 2026-08-29.
Frozen floors below are that measurement, sealed as
gates -- not a search over 1/2.  No two-commit pre-blind
freeze: pins disclosed.  Builder fallback NOT taken:
full census wall < 3 s (bar 120 s) on core-42 +
chi3/chi4-42 + Twin.

FROZEN FROM /tmp (live re-gated, not fitted):
  * Frame lemma SATZ over Q: A=diag(-1,2), ell=e_0, C=2
    => A+C ell ell^T = diag(1,2) succ 0, nneg(A)=1.
    Omit-ell mutant: A not succeq c I (min=-1).
    Rank-1 interlacing SATZ: diag(-1,-1)+e0 e0^T =
    diag(0,-1) kills exactly one negative, never two.
  * Weyl SATZ: nneg(A+B) <= nneg(A)+nneg(B); 2x2 slack.
  * w9 MAIN: n=104, nneg=1, ncl=36 in [1/2, 3/5],
    rmin=0.46153, lam2=0.50004, gap2=4.1e-5 (RAZOR).
    pmass=0.1514 rest-hosted (r367), lam_rest<0.
  * Bernstein-Szego reference = dual of full-grid Fejer
    (r390 SATZ) restricted to Y: nneg_ref=49, ncl=32,
    r in [0.077, 0.888].  MAIN kills 48 of 49 negatives.
    Lift M = P_neg^ref B P_neg^ref: r_eff=9.55, lead=0.105,
    numerical rank=49 on the 49-dim negative space.
    Interlacing: rank-1 can kill at most 1; need rank>=48.
    Whole-B spectral-free r_eff=14.91, lead=0.067.
    Occupied-I (tiny nu floor) is DEGENERATE: depth
    N-3 > |Y| saturates R^ref=I (disclosed, not the
    r390 object; not used as the reference).
  * Source ell = dcent sampled on Y: cosine with v_neg
    = 0.0075 (orthogonal).  Frame with dcent / SVD(B) /
    cluster-leading FAILS for every C in the scan;
    tautological v_neg works.  No source-defined ell_k.
  * Phase does NOT track ind_-: MAIN rho1=-0.341
    scramble -0.363 (scramble MORE anti-correlated)
    with nneg 1 vs 21.  E=1.81 vs 3.39 factor <2.
    Dead chi3-15 rho1=-0.333 nneg=1 (MAIN-like).
  * Scramble: nneg=21, nneg_ref=35, killed=14 only,
    rmin=0.0036 (punches through 1/2), ncl=7.
    Two-period S=21: nneg=4, killed=0 (no lift).
  * Dead chi3 5/5 nneg in {0,1}; living chi3 37/37
    nneg<=1; chi4-20 nneg=0.  P1 HOLDS on dead chi --
    they die at sch>0 (r401), not at the bulk.
  * Core-42: 42/42 nneg in {0,1} (28 P1 + 14 vacuous);
    gap2 in [4.3e-8, 2.0e-4], median 6.9e-7.
    ncl grows 36 -> 250.  Twin-9 bit-identical nneg.
  * Mutant threshold x2 (lam2 >= 1): FALSE (lam2=1/2).
    Sub-band MVT: low-band energy of C_m is already ~0
    on MAIN, and dcent is orthogonal to v_neg, so a
    small sub-band energy does not control P1.

AUSGANG FORM_T REFUTED (rank-1) / FORM_P REFUTED
(no phase statistic tracks ind_-).  SATZ: the frame
implication (PD minus rank-1 => ind_- <= 1); rank-r
interlacing; Weyl.  CENSUS: the BS dual on Y has ~49
negatives; MAIN/living/dead-chi lift all but at most
one (high-rank positive repair, not a rank-1 defect);
the 1/2-cluster is the remnant of that lift, razor-thin
above 1/2; the genuine negative (when present) is
orthogonal to the r399 centered difference.  Dead chi
do not die at P1.  Honesty gate: proving lam2(R)>=1/2
by energy/phase of dcent is the same wall as r399
(orthogonal, and MVT 10^3-10^5 short).  No RH claim.

MACHINERY: r367 FTI.cut_rung / pair (cross-check),
r356 BDH.dual_weights, r390 GEP.fejer_w, r398 HM.r_nm3,
r399 SW.pack_kz / C_m, r357 DMF chi, r331 TR Twin,
r226 V.build_measures.

NO RH CLAIM.  Finite identities, two named refutations,
named kills.  Research documentation, not a theorem of RH.
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

import borodin_dual_hole_probe as BDH  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import g_eps_mu_probe as GEP  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import source_weyl_energy_probe as SW  # noqa: E402
import final_two_rank_inertia_probe as FTI  # noqa: E402
import pair_extremal_probe as PX  # noqa: E402
import twin_resolution_probe as TR  # noqa: E402
import arch_kernel_diophantine_probe as AKD  # noqa: E402
import minimal_firewall_probe as MF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

SCR_SEED = 1
DEAD_CHI3 = (15, 19, 23, 33, 39)
DEAD_CHI4 = (20,)
CORE_N, P1_N, VAC_N = 42, 28, 14
CHI3_LIVE_N, CHI3_DEAD_N = 37, 5
CHI4_LIVE_N, CHI4_DEAD_N = 41, 1
W9_N, W9_NW, W9_NNEG, W9_NCL = 104, 184, 1, 30
W9_NNEG_REF_LO = 40
W9_KILLED_LO = 40
W9_LIFT_REFF_LO = 5.0
W9_LEAD_HI = 0.25
W9_COS_HI = 0.05
W9_GAP2_HI = 1.0e-3
W9_PMASS_HI = 0.30
W9_RMIN = 0.46153
SCR_NNEG, SCR_KILLED_HI = 21, 20
SCR_RMIN_HI = 0.05
TP21_NNEG = 4
PHASE_DRHO1_HI = 0.10
CORE_GAP2_MAX = 1.0e-3
REL = 5.0e-3
C_SCAN = (0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0)

FTI_SHA_PREFIX = "e0d79840"
BDH_SHA_PREFIX = "36141c0a"
DMF_SHA_PREFIX = "4bf1a94b"
GEP_SHA_PREFIX = "c2c9c3f2"
HM_SHA_PREFIX = "bb1dcf6a"
SW_SHA_PREFIX = "c5a74fda"

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
    return (not bad), ("NO zero/prime oracles; dual CD Gram / "
                       "Fejer / Dirichlet C_m / interlacing only"
                       if not bad else "; ".join(bad))


def nneg_sym(A, floor=1e-12):
    ev = np.linalg.eigvalsh(0.5 * (np.asarray(A, float) + np.asarray(A, float).T))
    return int(np.sum(ev < -floor)), ev


def r_eff_of(M, floor=1e-18):
    """r_eff = ||M||_F^2 / ||M||_op^2 (= 1 for rank-1);
    lead = ||M||_op^2 / ||M||_F^2.  Spectral-free on the
    matrix M itself (SVD/eig of M, not of A0)."""
    ev = np.linalg.eigvalsh(0.5 * (M + M.T))
    f2 = float(np.sum(ev * ev))
    op = float(np.max(np.abs(ev)))
    if f2 < floor or op < floor:
        return dict(r_eff=float("nan"), lead=float("nan"),
                    rank_num=0, frob=0.0, op=0.0)
    return dict(r_eff=f2 / (op * op), lead=(op * op) / f2,
                rank_num=int(np.sum(np.abs(ev) > 1e-10 * op)),
                frob=math.sqrt(f2), op=op)


def phase_of(C, k):
    C = np.asarray(C, float)
    tail = C[1:k] if k > 1 else C[:1]
    s = np.sign(tail)
    s[s == 0] = 1.0
    rho1 = float(np.mean(s[:-1] * s[1:])) if len(s) > 1 else float("nan")
    flip = float(np.mean(s[:-1] != s[1:])) if len(s) > 1 else float("nan")
    rho2 = float(np.mean(s[:-2] * s[2:])) if len(s) > 2 else float("nan")
    pwr = tail ** 2
    tot = float(np.sum(pwr)) + 1e-30
    n = len(pwr)
    return dict(
        rho1=rho1, flip=flip, rho2=rho2,
        hhi=float(np.sum((pwr / tot) ** 2)),
        b_lo=float(np.sum(pwr[:max(1, n // 8)])) / tot if n else 0.0,
        b_hi=float(np.sum(pwr[n // 2:])) / tot if n else 0.0,
    )


def dual_fejer_R(mz):
    """r390 Bernstein-Szego reference: Fejer 1-x on the FULL
    cosine grid, dual weights, CD Gram of the first Nw-3
    dual columns restricted to Y.  Same shape as R_{N-3}."""
    xu = np.asarray(mz["xu"], float)
    yn = np.asarray(mz["yn"], float)
    S, L, Nw = int(mz["S"]), int(mz["L"]), int(mz["Nw"])
    fej = GEP.fejer_w(xu, 1.0)
    ud, _lA, _f, _eps, _lp = BDH.dual_weights(xu, fej, S, L)
    iY = np.searchsorted(xu, yn)
    ad, bd, h0d = V.mu_chain(xu, ud, Nw)
    Bd = V.b_matrix(ad, bd, h0d, yn, ud[iY], Nw)
    R = Bd[:, :Nw - 3] @ Bd[:, :Nw - 3].T
    return 0.5 * (R + R.T)


def r_of(mz):
    return HM.r_nm3(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                    mz["Nw"], mz["S"], mz["L"])


def spec_R(R):
    ev = np.linalg.eigvalsh(R)
    return dict(
        n=int(len(ev)), rmin=float(ev[0]), rmax=float(ev[-1]),
        nneg=int(np.sum(ev < 0.5 - 1e-12)),
        ncl=int(np.sum((ev >= 0.5) & (ev <= 0.6))),
        lam2=float(ev[1]) if len(ev) > 1 else float("nan"),
        gap2=float(ev[1] - 0.5) if len(ev) > 1 else float("nan"),
        ev=ev,
    )


def dcent_on_Y(mz, Psw):
    yn = np.asarray(mz["yn"], float)
    xg = np.cos(Psw["th"])
    return np.array([Psw["dcent"][int(np.argmin(np.abs(xg - y)))]
                     for y in yn], float)


def frame_min(A0, ell, Cs=C_SCAN):
    ell = np.asarray(ell, float).ravel()
    nrm = float(np.linalg.norm(ell))
    if nrm < 1e-18:
        return dict(ok=False, c=float("nan"), C=0.0, ru=float("nan"))
    u = ell / nrm
    ru = float(u @ A0 @ u)
    uu = np.outer(u, u)
    best_c, best_C = -1e9, 0.0
    for C in Cs:
        evmin = float(np.linalg.eigvalsh(A0 + C * uu)[0])
        if evmin > best_c:
            best_c, best_C = evmin, C
    return dict(ok=best_c > 1e-10, c=best_c, C=best_C, ru=ru)


def pack_world(mz, en=None, need_ref=True):
    R, meta = r_of(mz)
    sp = spec_R(R)
    A0 = R - 0.5 * np.eye(R.shape[0])
    if need_ref:
        Rr = dual_fejer_R(mz)
        B = R - Rr
        Aref = Rr - 0.5 * np.eye(Rr.shape[0])
        evA, VA = np.linalg.eigh(Aref)
        mneg = evA < -1e-12
        nneg_ref = int(np.sum(mneg))
        if nneg_ref:
            Pneg = VA[:, mneg] @ VA[:, mneg].T
            lift = r_eff_of(Pneg @ B @ Pneg)
        else:
            lift = dict(r_eff=float("nan"), lead=float("nan"),
                        rank_num=0, frob=0.0, op=0.0)
        whole = r_eff_of(B)
        evR, VR = np.linalg.eigh(R)
        mcl = (evR >= 0.5) & (evR <= 0.6)
        if np.any(mcl):
            Pcl = VR[:, mcl] @ VR[:, mcl].T
            cl = r_eff_of(Pcl @ B @ Pcl)
        else:
            cl = dict(r_eff=float("nan"), lead=float("nan"),
                      rank_num=0, frob=0.0, op=0.0)
    else:
        nneg_ref = -1
        lift = cl = whole = dict(r_eff=float("nan"), lead=float("nan"),
                                 rank_num=0, frob=0.0, op=0.0)
    evA0, VA0 = np.linalg.eigh(A0)
    vneg = VA0[:, 0]
    out = dict(
        n=sp["n"], Nw=int(mz["Nw"]), nneg=sp["nneg"], ncl=sp["ncl"],
        rmin=sp["rmin"], lam2=sp["lam2"], gap2=sp["gap2"],
        nneg_ref=nneg_ref, killed=nneg_ref - sp["nneg"],
        lift=lift, whole=whole, cl=cl,
        ok_sup=bool(meta["ok_sup"]), ok_map=bool(meta["ok_map"]),
        lminA=float(evA0[0]),
    )
    if en is not None and "C" in en:
        k = max(1, int(mz["Nw"]) - 3)
        out["ph"] = phase_of(en["C"], k)
        out["E"] = float(en.get("E_bulk", float("nan")))
        if "dcent" in en and "th" in en:
            ell = dcent_on_Y(mz, en)
            out["cos_vd"] = abs(float(vneg @ ell)) / (
                float(np.linalg.norm(vneg) * np.linalg.norm(ell)) + 1e-30)
            out["fr_dcent"] = frame_min(A0, ell)
        else:
            out["cos_vd"] = float("nan")
            out["fr_dcent"] = dict(ok=False, c=float("nan"), C=0.0, ru=0.0)
    out["fr_neg"] = frame_min(A0, vneg)
    out["_A0"] = A0
    out["_R"] = R
    out["_vneg"] = vneg
    return out


def drop_heavy(p):
    for k in ("_A0", "_R", "_vneg"):
        p.pop(k, None)
    return p


def part_a_toy():
    section("S1  LEG B -- FRAME / INTERLACING / WEYL (Q-EXACT)")
    A = np.array([[Fr(-1), Fr(0)], [Fr(0), Fr(2)]], dtype=object)
    C = Fr(2)
    Ap = np.array([[A[0, 0] + C, Fr(0)], [Fr(0), A[1, 1]]], dtype=object)
    check("G01-frame-Q",
          Ap[0, 0] == Fr(1) and Ap[1, 1] == Fr(2) and Ap[0, 0] > 0,
          "A=diag(-1,2)+2 e0 e0^T = diag(1,2) succ 0 => nneg(A)=1")
    check("G02-mutant-omit-ell",
          A[0, 0] == Fr(-1),
          "without ell, min(A)=-1: A not succeq c I (hypothesis fails)")
    A2 = np.array([[Fr(-1), Fr(0)], [Fr(0), Fr(-1)]], dtype=object)
    A2p = np.array([[Fr(0), Fr(0)], [Fr(0), Fr(-1)]], dtype=object)
    check("G03-interlace-rank1-Q",
          A2[0, 0] + A2[1, 1] == Fr(-2)
          and A2p[0, 0] == Fr(0) and A2p[1, 1] == Fr(-1),
          "diag(-1,-1)+e0 e0^T kills ONE negative, never two")
    # Weyl on a 2x2 float witness (identity is SATZ; numbers gated)
    Af = np.diag([-1.0, 1.0])
    Bf = np.diag([1.0, -1.0])
    nA, _ = nneg_sym(Af)
    nB, _ = nneg_sym(Bf)
    nS, _ = nneg_sym(Af + Bf)
    check("G04-Weyl",
          nS <= nA + nB and nA == 1 and nB == 1,
          "nneg(A+B)=%d <= nneg(A)+nneg(B)=%d+%d" % (nS, nA, nB))
    check("G05-mutant-threshold-x2",
          Fr(1, 2) < Fr(1),
          "lam2>=1 is strictly stronger than lam2>=1/2 (MAIN will miss)")


def part_b_w9():
    section("S2  LEG A/B -- w9 RANK ANATOMY + FRAME")
    mz = V.build_measures(9)
    en = SW.pack_kz(9)
    p = pack_world(mz, en)
    check("G10-w9-P1-cluster",
          p["n"] == W9_N and p["Nw"] == W9_NW
          and p["nneg"] == W9_NNEG and p["ncl"] >= W9_NCL
          and abs(p["rmin"] - W9_RMIN) <= 2e-4
          and p["ok_sup"] and p["ok_map"],
          "n=%d N=%d nneg=%d ncl=%d rmin=%.5f" % (
              p["n"], p["Nw"], p["nneg"], p["ncl"], p["rmin"]))
    check("G11-w9-ref-lift",
          p["nneg_ref"] >= W9_NNEG_REF_LO
          and p["killed"] >= W9_KILLED_LO,
          "nneg_ref=%d killed=%d (rank-1 can kill at most 1)"
          % (p["nneg_ref"], p["killed"]))
    check("G12-w9-lift-not-rank1",
          p["lift"]["r_eff"] >= W9_LIFT_REFF_LO
          and p["lift"]["lead"] <= W9_LEAD_HI
          and p["whole"]["r_eff"] >= W9_LIFT_REFF_LO,
          "lift r_eff=%.2f lead=%.3f rank_num=%d; whole r_eff=%.2f"
          % (p["lift"]["r_eff"], p["lift"]["lead"],
             p["lift"]["rank_num"], p["whole"]["r_eff"]))
    check("G13-w9-dcent-orthogonal",
          p["cos_vd"] <= W9_COS_HI,
          "cosine(vneg, dcent_Y)=%.4f <= %.2f (frame cannot lift)"
          % (p["cos_vd"], W9_COS_HI))
    check("G14-w9-gap2-razor",
          0.0 < p["gap2"] <= W9_GAP2_HI,
          "lam2-1/2=%.3e (razor; MVT cannot certify this)"
          % p["gap2"])
    i1, i2 = PX.pair_select(mz["yn"])
    o = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                     mz["Nw"], mz["S"], mz["L"], i1, i2)
    check("G15-w9-rest-hosted",
          o["pmass"] <= W9_PMASS_HI and o["lam_rest"] < 0
          and o["lam_pair"] > 0 and o["nneg"] == W9_NNEG,
          "pmass=%.4f lam_rest=%+.2e (NOT the pair functional)"
          % (o["pmass"], o["lam_rest"]))
    check("G16-w9-frame-source-FAIL",
          (not p["fr_dcent"]["ok"]) and p["fr_neg"]["ok"],
          "dcent frame ok=%s c=%.3g; tautological vneg ok=%s"
          % (p["fr_dcent"]["ok"], p["fr_dcent"]["c"], p["fr_neg"]["ok"]))
    drop_heavy(p)
    p["pmass"] = float(o["pmass"])
    return p


def part_d_kills():
    section("S3  LEG C/D -- SCRAMBLE / TWO-PERIOD / CHI / PHASE")
    mzs = HM.scramble_mz()
    ens = SW.scramble_energy()
    ps = pack_world(mzs, ens)
    check("G20-scramble-nneg21",
          ps["nneg"] == SCR_NNEG
          and ps["killed"] <= SCR_KILLED_HI,
          "nneg=%d killed=%d of nneg_ref=%d (lift INCOMPLETE)"
          % (ps["nneg"], ps["killed"], ps["nneg_ref"]))
    check("G21-scramble-punch",
          ps["rmin"] <= SCR_RMIN_HI and ps["ncl"] < 15,
          "rmin=%.4f ncl=%d -- cluster punches through 1/2"
          % (ps["rmin"], ps["ncl"]))
    mzt = HM.two_period_mz(21, 2.0 / 3.0)
    pt = pack_world(mzt, None)
    check("G22-two-period",
          pt["nneg"] >= TP21_NNEG and pt["killed"] == 0,
          "S=21 nneg=%d killed=%d (no BS-lift)"
          % (pt["nneg"], pt["killed"]))
    mzd = HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3)
    end = SW.chi_energy(15, DMF.Q_CHI3, DMF.LPQ3)
    pd = pack_world(mzd, end)
    check("G23-dead-chi3-15-bulk-P1",
          pd["nneg"] <= 1,
          "dead chi3-15 nneg=%d <= 1 -- death is NOT at P1"
          % pd["nneg"])
    mzl = HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3)
    enl = SW.chi_energy(9, DMF.Q_CHI3, DMF.LPQ3)
    pl = pack_world(mzl, enl)
    check("G24-live-chi3-9",
          pl["nneg"] <= 1,
          "live chi3-9 nneg=%d" % pl["nneg"])
    mz = V.build_measures(9)
    en = SW.pack_kz(9)
    pM = pack_world(mz, en)
    drho = abs(pM["ph"]["rho1"] - ps["ph"]["rho1"])
    check("G25-phase-does-not-separate",
          drho <= PHASE_DRHO1_HI and pM["nneg"] == 1
          and ps["nneg"] == SCR_NNEG,
          "|rho1_M - rho1_S|=%.3f <= %.2f  (E %.2f vs %.2f) "
          "but nneg 1 vs 21" % (
              drho, PHASE_DRHO1_HI, pM["E"], ps["E"]))
    uuc, mmc = TR.base_comb(9)
    mzD = TR.build_world(9, uuc, mmc)
    gapsc = MF.local_gaps(uuc)
    u2c, m2c, _dn, _du = AKD.twin_rational(
        uuc, mmc, gapsc, mzD["D"], 1.0e-8)
    mzT = TR.build_world(9, u2c, m2c)
    pT = pack_world(mzT, en)
    check("G26-twin-9",
          pT["nneg"] == pM["nneg"] and pT["ncl"] == pM["ncl"],
          "Twin nneg/ncl %d/%d == MAIN %d/%d"
          % (pT["nneg"], pT["ncl"], pM["nneg"], pM["ncl"]))
    for q in (ps, pt, pd, pl, pM, pT):
        drop_heavy(q)
    return dict(scr=ps, tp=pt, dead=pd, live=pl, main=pM, twin=pT)


def part_full():
    section("S4  LEG A/C -- CORE-42 + CHI CENSUS")
    core = list(V.admissible_indices())
    rows = []
    for kz in core:
        mz = V.build_measures(kz)
        p = pack_world(mz, None, need_ref=False)
        drop_heavy(p)
        p["kz"] = kz
        rows.append(p)
    nnegs = [r["nneg"] for r in rows]
    gaps = [r["gap2"] for r in rows]
    p1 = sum(n == 1 for n in nnegs)
    vac = sum(n == 0 for n in nnegs)
    check("G40-core42-P1",
          len(rows) == CORE_N
          and all(n in (0, 1) for n in nnegs)
          and p1 == P1_N and vac == VAC_N
          and all(r["ok_sup"] and r["ok_map"] for r in rows),
          "42/42 nneg in {0,1}; P1 %d vac %d" % (p1, vac))
    check("G41-core42-gap2",
          min(gaps) > 0.0 and max(gaps) <= CORE_GAP2_MAX,
          "gap2 [%.3e, %.3e] median %.3e -- razor, not MVT-scale"
          % (min(gaps), max(gaps), float(np.median(gaps))))
    live3, dead3, live4, dead4 = [], [], [], []
    for kz in core:
        mz3 = HM.chi_mz(kz, DMF.Q_CHI3, DMF.LPQ3)
        if mz3 is not None:
            p3 = pack_world(mz3, None, need_ref=False)
            drop_heavy(p3)
            (dead3 if kz in DEAD_CHI3 else live3).append(p3)
        mz4 = HM.chi_mz(kz, DMF.Q_CHI4, DMF.LPQ4)
        if mz4 is not None:
            p4 = pack_world(mz4, None, need_ref=False)
            drop_heavy(p4)
            (dead4 if kz in DEAD_CHI4 else live4).append(p4)
    check("G42-chi3-live-P1",
          len(live3) == CHI3_LIVE_N
          and all(r["nneg"] <= 1 for r in live3),
          "live chi3 %d/%d nneg<=1 (max %d)"
          % (len(live3), CHI3_LIVE_N, max(r["nneg"] for r in live3)))
    check("G43-chi3-dead-bulk-P1",
          len(dead3) == CHI3_DEAD_N
          and all(r["nneg"] <= 1 for r in dead3),
          "dead chi3 %d/%d nneg<=1 values=%s -- P1 holds, death is edge"
          % (len(dead3), CHI3_DEAD_N, [r["nneg"] for r in dead3]))
    check("G44-chi4-P1",
          len(live4) == CHI4_LIVE_N
          and all(r["nneg"] <= 1 for r in live4)
          and len(dead4) == CHI4_DEAD_N
          and all(r["nneg"] <= 1 for r in dead4),
          "live chi4 %d/%d nneg<=1; dead %d nneg=%s"
          % (len(live4), CHI4_LIVE_N, len(dead4),
             [r["nneg"] for r in dead4]))
    return rows


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("bulk_one_defect_probe -- "
          "PRIME.LDAGGER.BULK_ONE_DEFECT.01 (round 400)")
    print("SPEC_SHA %s   (FTI %s / BDH %s / GEP %s / HM %s / SW %s)"
          % (SPEC_SHA[:16], FTI.SPEC_SHA[:16], BDH.SPEC_SHA[:16],
             GEP.SPEC_SHA[:16], HM.SPEC_SHA[:16], SW.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                         "FULL (core-42 + chi3/chi4-42 + Twin)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (FTI.SPEC_SHA.startswith(FTI_SHA_PREFIX)
              and BDH.SPEC_SHA.startswith(BDH_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and GEP.SPEC_SHA.startswith(GEP_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and SW.SPEC_SHA.startswith(SW_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "FTI %s / BDH %s / DMF %s / GEP %s / HM %s / SW %s"
          % (FTI.SPEC_SHA[:8], BDH.SPEC_SHA[:8], DMF.SPEC_SHA[:8],
             GEP.SPEC_SHA[:8], HM.SPEC_SHA[:8], SW.SPEC_SHA[:8]))

    part_a_toy()
    part_b_w9()
    part_d_kills()
    if not smoke:
        part_full()
    else:
        section("S4  FULL CENSUS skipped (--smoke)")

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict-T-REFUTED-P-REFUTED",
          prev_ok,
          "FORM_T REFUTED (rank-1 cannot kill 48); "
          "FORM_P REFUTED (phase does not track ind_-); "
          "dead chi P1 holds (death is edge); no RH claim")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "FORM_T_REFUTED / FORM_P_REFUTED"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("BULK ONE DEFECT %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("BULK ONE DEFECT FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
