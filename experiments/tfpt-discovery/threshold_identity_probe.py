#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""threshold_identity_probe --
PRIME.LDAGGER.THRESHOLD_IDENTITY.01 (round 411):
is ||T0||=1 on PD windows an exact identity, and is
||T0||<=1 exactly the dual energy split on the quotient?

THE LEMMA.  T0 is the min-norm interpolant Y->X in P_<d0
(r409).  T0*T0 = C^{-1} (r407/r409 dictionary), so
    ||T0|| = 1/sqrt(lam_min(C)).
On the quotient P_<d0>/K0 (min-norm interpolants;
K0 = P_Y * P_<d0-|Y|>, Y-energy 0) the Rayleigh of C^{-1}
IS the energy ratio ||q||_X^2 / ||q||_Y^2.  Hence
    ||T0|| <= 1  <=>  C succeq I  <=>  every q in K0^perp
    carries at least half its dual-weighted energy on Y.
Kernel vectors are excluded: their Y-energy vanishes.

WHAT IS NOT THE LEMMA.  R409 printed ||T0||=1.00000 on
kz42/kz130.  That is 1/sqrt(Cmin) with Cmin = 1+eps
(kz42 eps=4.57e-8, kz130 eps=4.90e-9, core-42 PD
[1.33e-7, 7.54e-5]).  Not exact 0.  No saturating
combinatorial polynomial (node poly / single T_k /
alias T_S) achieves EX=EY on the quotient.  The
Fourier hole-Nyquist face is NOT the excess direction
(||T v_F||=0.656 < ||T||=1.080 on w9; R410).  The
true excess IS C's lowest evec = T0's top SV (SATZ).
k=37 is lam_min(C) crossing 1 in a theta-prefix, not
a single-hole Christoffel collapse (Klast=6.94; several
leave-one-outs restore nC=0).

CALIBRATION DISCLOSURE.  Dictionary residuals, Cmin-1
table, Fourier-vs-SV, Q projection identity, sequential
Cmin, leave-one-out, permute/1010 first measured in
/tmp (r411_cal.py, r411_cal2.py, r411_cal3.py) on the
same constructors, 2026-08-29.  Frozen floors below
are that measurement, sealed as gates.  Pins disclosed.
Builder fallback NOT taken: full wall < 30 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ over Q: ||TT-Cinv||=4.6e-17; proj-id 1.4e-15;
    P_Y is kernel (EY=0); u^vee=1/u breaks ||T||
    0.670 -> 2.221.
  * w9: ||T||=1.080138437324 = 1/sqrt(Cmin) to 1e-14;
    ||TT-Cinv||=6.6e-14; Four-corr=0.386;
    ||T v_F||=0.656538 (R410 pin).
  * PD: kz42 Cmin-1=+4.565e-8 ||T||-1=-2.28e-8;
    kz130 Cmin-1=+4.90e-9; core-42 PD 14/14 Cmin>1.
  * P1 excess = C-ev0 = top SV; B^T v peaks deep
    (w9 j=165/181), not a low-degree T_k.
  * SEQ: k=36 Cmin-1=+6.82e-5 nC=0; k=37 -9.23e-5 nC=1.
    Permute flips by k=10; Kmin=0.148 only at full Y.
  * KILLS: SCR nC=21 Cmin=0.0036 ||T||=16.66;
    1010-20 ||T||=165; chi9 ||T||<1; chi15 ||T||>1.

AUSGANG ENERGY_SPLIT_EXACT / SATURATION_REFUTED.
SATZ: dictionary ||T0||=1/sqrt(lam_min(C)) and the
energy split on K0^perp.  REFUTED: exact ||T0||=1 on
PD; combinatorial saturator; k=37 as a named
Christoffel-weight hole.  P1 is one excess direction
on the quotient (already r407 nC<=1, now in energy
language).  Does not move the mincut.  No RH claim.
No L* claim (the split is a finite dual-coordinate
dictionary, not the L* subordination).

MACHINERY: r409 B.pack_graph / source_T0_cls / toy;
r407 DI.pack_C / C_plus_Q; r408 CT.rebuild_holes /
two_period; r410 Fourier face as a named miss;
r356 BDH dual weights; r403 P1.reweight; r226 V.

NO RH CLAIM.  Finite identities, one named refutation.
Research documentation, not a theorem of RH.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import borodin_birkhoff_intertwiner_probe as B  # noqa: E402
import dual_intertwiner_probe as DI  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import verify_lstar_instance as V  # noqa: E402
import c_threshold_probe as CT  # noqa: E402

B_SHA_PREFIX = "baee9fc5"
DI_SHA_PREFIX = "2ee74c59"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"
CT_SHA_PREFIX = "cb03729f"

FORMULA_HI = 1.0e-10
W9_OP = 1.080138437
W9_CMIN = 0.857119
W9_TF_LO, W9_TF_HI = 0.64, 0.68
FOUR_CORR_HI = 0.50
KZ42_GAP_LO, KZ42_GAP_HI = 1.0e-8, 1.0e-6
KZ130_GAP_LO, KZ130_GAP_HI = 1.0e-9, 1.0e-7
PD_GAP_LO = 1.0e-9
PREFIX36_GAP_LO = 1.0e-5
PERM_KMIN_HI = 0.20
SCR_NC = 21
PERM_NC_LO = 15
CORE_N = 42
SAMPLE_EXT = HM.SAMPLE_EXT

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
    return (not bad), ("NO zero/prime oracles; CLS / dual C / "
                       "energy split on the quotient"
                       if not bad else "; ".join(bad))


def fourier_face(yn, v):
    th = np.arccos(np.clip(np.asarray(yn, float), -1.0, 1.0))
    o = np.argsort(th)
    vs = np.asarray(v, float)[o]
    n = len(vs)
    k = n // 2
    t = np.arange(n)
    vF = np.cos(2.0 * math.pi * k * t / float(n))
    vF /= np.linalg.norm(vF) + 1e-30
    out = np.zeros(n)
    out[o] = vF
    F = np.fft.rfft(vs - vs.mean())
    return out, int(np.argmax(np.abs(F)))


def top_right(T):
    _U, s, Vt = np.linalg.svd(T, full_matrices=False)
    return float(s[0]), Vt[0]


def dict_pack(mz):
    g = B.pack_graph(mz)
    pk = DI.pack_C(mz)
    inv = 1.0 / math.sqrt(max(pk["Cmin"], 1e-300))
    rest = B.relres(g["TT"], np.linalg.inv(pk["C"]))
    return dict(g=g, pk=pk, inv=inv, rest=rest,
                gap=pk["Cmin"] - 1.0,
                dT=abs(g["opnorm"] - inv))


def theta_prefix(mz, k):
    yn = np.asarray(mz["yn"], float)
    vn = np.asarray(mz["vn"], float)
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    o = np.argsort(th)
    return CT.rebuild_holes(mz, yn[o][:k], vn[o][:k])


def part_satz():
    section("S1  LEG A -- DICTIONARY / QUOTIENT / KERNEL OVER Q")
    xs, u, ud, iX, iY, d0 = B.toy_dual()
    xs_f = np.array([float(x) for x in xs])
    ud_f = np.array([float(w) for w in ud])
    xp, yn = xs_f[iX], xs_f[iY]
    wX, wY = ud_f[iX], ud_f[iY]
    T = B.source_T0_cls(xp, wX, yn, wY, d0)
    TT = T.T @ T
    Cq = B.C_plus_Q(xs, ud, iX, iY, d0)
    Cf = np.array([[float(Cq[i][j]) for j in range(len(Cq))]
                   for i in range(len(Cq))])
    Cinv = np.linalg.inv(Cf)
    cmin = float(np.linalg.eigvalsh(Cf)[0])
    check("G01-toy-TT-equals-Cinv",
          B.relres(TT, Cinv) <= 1e-12
          and abs(np.linalg.norm(T, 2) - 1.0 / math.sqrt(cmin)) <= 1e-12,
          "||TT-Cinv||=%.3e ||T||=%.8f=1/sqrt(Cmin)"
          % (B.relres(TT, Cinv), float(np.linalg.norm(T, 2))))
    kX = xp * (xp - 0.5)
    eyK = float(wY @ ((yn * (yn - 0.5)) ** 2))
    check("G02-toy-PY-is-kernel",
          eyK <= 1e-18,
          "P_Y energy on Y = %.3e (split does not apply)" % eyK)
    PX, PY = B.chebV(xp, d0), B.chebV(yn, d0)
    Gk = float(wX @ (kX * kX))
    rng = np.random.default_rng(411)
    rests = []
    for _ in range(8):
        c = rng.normal(size=d0)
        qX, qY = PX @ c, PY @ c
        qXm = qX - (float(wX @ (qX * kX)) / Gk) * kX
        got = T @ (np.sqrt(wY) * qY)
        want = np.sqrt(wX) * qXm
        rests.append(B.relres(got, want))
    check("G03-toy-proj-identity",
          max(rests) <= 1e-12,
          "T(sY q_Y)=sX q_min on K0^perp maxrel=%.3e" % max(rests))
    ud_bad = np.array([1.0 / float(u[j]) for j in range(5)])
    Tb = B.source_T0_cls(xp, ud_bad[iX], yn, ud_bad[iY], d0)
    check("G04-mustfail-uvee-without-Pprime2",
          abs(np.linalg.norm(Tb, 2) - np.linalg.norm(T, 2)) >= 0.5,
          "u^vee=1/u ||T||=%.4f vs %.4f" % (
              float(np.linalg.norm(Tb, 2)), float(np.linalg.norm(T, 2))))
    Tm = B.source_T0_cls(xp, wX, yn, wY, d0 - 1)
    check("G05-mustfail-d0-shift",
          B.relres(Tm.T @ Tm, Cinv) >= 1e-3,
          "d0-1 breaks TT=Cinv (wrong kernel quotient)")


def part_w9():
    section("S2  LEG B -- ENERGY SPLIT = ||T||<=1 (w9)")
    mz = V.build_measures(9)
    d = dict_pack(mz)
    g, pk = d["g"], d["pk"]
    check("G10-w9-dictionary",
          d["rest"] <= FORMULA_HI and d["dT"] <= FORMULA_HI
          and abs(g["opnorm"] - W9_OP) <= 1e-8
          and abs(pk["Cmin"] - W9_CMIN) <= 5e-6,
          "||TT-Cinv||=%.3e ||T||=%.12f=1/sqrt(Cmin) Cmin=%.6f"
          % (d["rest"], g["opnorm"], pk["Cmin"]))
    _s, v = top_right(g["T0"])
    vF, kpk = fourier_face(g["yn"], v)
    nTF = float(np.linalg.norm(g["T0"] @ vF))
    corr = abs(float(np.vdot(v, vF))) / (
        np.linalg.norm(v) * np.linalg.norm(vF) + 1e-30)
    ev, vec = np.linalg.eigh(pk["C"])
    corrC = abs(float(np.vdot(v, vec[:, 0]))) / (
        np.linalg.norm(v) * np.linalg.norm(vec[:, 0]) + 1e-30)
    check("G11-w9-excess-is-C-ev0-not-Fourier",
          corrC >= 0.999 and corr <= FOUR_CORR_HI
          and W9_TF_LO <= nTF <= W9_TF_HI
          and kpk == len(g["yn"]) // 2,
          "corr(v,C-ev0)=%.4f corr(v,vF)=%.4f ||T vF||=%.6f "
          "(R410 Fourier face is not the excess)"
          % (corrC, corr, nTF))
    # raw T_1 energy ratio is NOT the quotient Rayleigh
    qX = B.chebV(g["xp"], 2)[:, 1]
    qY = B.chebV(g["yn"], 2)[:, 1]
    raw = float(g["wX"] @ (qX * qX)) / float(g["wY"] @ (qY * qY))
    check("G12-mustfail-raw-Tk-not-quotient",
          raw >= 1.5,
          "raw T_1 EX/EY=%.3f > ||T||^2=%.3f (kernel not projected)"
          % (raw, g["opnorm"] ** 2))
    return dict(mz=mz, d=d, v=v)


def part_pd_seq(w9, smoke):
    section("S3  LEG A/C -- PD GAP / SEQ k=37 / SATURATION")
    d42 = dict_pack(V.build_measures(42))
    check("G20-kz42-not-exact-one",
          KZ42_GAP_LO <= d42["gap"] <= KZ42_GAP_HI
          and d42["g"]["opnorm"] < 1.0
          and d42["pk"]["nC"] == 0
          and d42["dT"] <= 1e-9,
          "kz42 Cmin-1=%.3e ||T||-1=%.3e (SATURATION REFUTED)"
          % (d42["gap"], d42["g"]["opnorm"] - 1.0))
    mz = w9["mz"]
    p36 = DI.pack_C(theta_prefix(mz, 36))
    p37 = DI.pack_C(theta_prefix(mz, 37))
    g37 = B.pack_graph(theta_prefix(mz, 37))
    C37, m37 = DI.chain_C(theta_prefix(mz, 37))
    udY = m37["ud"][m37["iY"]]
    Kdiag = np.diag(C37) / np.maximum(udY, 1e-300)
    yn = np.asarray(mz["yn"], float)
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    last = yn[np.argsort(th)][36]
    i_last = int(np.argmin(np.abs(m37["yn"] - last)))
    check("G21-k37-is-eigenvalue-cross-not-K-collapse",
          p36["nC"] == 0 and p36["Cmin"] - 1.0 >= PREFIX36_GAP_LO
          and p37["nC"] == 1 and p37["Cmin"] < 1.0
          and float(Kdiag[i_last]) >= 2.0
          and g37["opnorm"] > 1.0,
          "k36 Cmin-1=%.3e nC=0; k37 Cmin-1=%.3e nC=1 "
          "Klast=%.2f ||T||=%.6f (not a Christoffel hole)"
          % (p36["Cmin"] - 1.0, p37["Cmin"] - 1.0,
             float(Kdiag[i_last]), g37["opnorm"]))
    if smoke:
        section("S3b  kz130 / core-42 / EXT skipped (--smoke)")
        return
    d130 = dict_pack(V.build_measures(130))
    check("G22-kz130-not-exact-one",
          KZ130_GAP_LO <= d130["gap"] <= KZ130_GAP_HI
          and d130["g"]["opnorm"] < 1.0 and d130["pk"]["nC"] == 0,
          "kz130 Cmin-1=%.3e ||T||-1=%.3e" % (
              d130["gap"], d130["g"]["opnorm"] - 1.0))
    n_ok = n_pd = n_p1 = 0
    gaps_pd = []
    for kz in V.admissible_indices():
        dd = dict_pack(V.build_measures(kz))
        if dd["pk"]["nC"] == 0:
            n_pd += 1
            gaps_pd.append(dd["gap"])
            n_ok += int(dd["gap"] >= PD_GAP_LO and dd["g"]["opnorm"] < 1.0
                        and dd["dT"] <= 1e-8)
        else:
            n_p1 += 1
            n_ok += int(dd["g"]["opnorm"] > 1.0 and dd["gap"] < 0.0
                        and dd["dT"] <= 1e-8)
    check("G23-core42-dictionary-and-gap",
          n_pd + n_p1 == CORE_N and n_ok == CORE_N
          and n_pd == 14 and min(gaps_pd) >= PD_GAP_LO,
          "core-%d dict 42/42; PD %d Cmin-1 in [%.3e, %.3e] "
          "(none exact 0)" % (CORE_N, n_pd, min(gaps_pd), max(gaps_pd)))
    ext_ok = True
    for kz in SAMPLE_EXT:
        dd = dict_pack(V.build_measures(kz))
        ext_ok = ext_ok and dd["dT"] <= 1e-8
        ext_ok = ext_ok and ((dd["pk"]["nC"] == 0 and dd["gap"] > 0)
                             or (dd["pk"]["nC"] == 1 and dd["gap"] < 0))
    check("G24-main-sample", ext_ok, "EXT %s dictionary+sign(Cmin-1)"
          % (SAMPLE_EXT,))


def part_kills(w9):
    section("S4  LEG D -- KILLS")
    mz = w9["mz"]
    mzP = P1.reweight(mz, "permute", 1000)
    dP = dict_pack(mzP)
    C, meta = DI.chain_C(mzP)
    K = np.diag(C) / np.maximum(meta["ud"][meta["iY"]], 1e-300)
    check("G30-permute-breaks-split-by-K-collapse",
          dP["pk"]["nC"] >= PERM_NC_LO and dP["g"]["opnorm"] > 2.0
          and float(K.min()) <= PERM_KMIN_HI
          and dP["dT"] <= 1e-8,
          "PERM nC=%d ||T||=%.3f Kmin=%.4f (same Y; split dies "
          "because the mu-chain collapses)" % (
              dP["pk"]["nC"], dP["g"]["opnorm"], float(K.min())))
    dS = dict_pack(HM.scramble_mz())
    check("G31-scramble-overload",
          dS["pk"]["nC"] == SCR_NC and dS["g"]["opnorm"] > 10.0
          and dS["dT"] <= FORMULA_HI,
          "SCR nC=%d ||T||=%.2f Cmin=%.5f" % (
              dS["pk"]["nC"], dS["g"]["opnorm"], dS["pk"]["Cmin"]))
    d20 = dict_pack(CT.with_xp(HM.two_period_mz(20, 1.0)))
    check("G32-1010-kernel",
          d20["g"]["opnorm"] > 10.0 and d20["pk"]["nC"] >= 3,
          "1010-20 ||T||=%.1f nC=%d (periodic kill)"
          % (d20["g"]["opnorm"], d20["pk"]["nC"]))
    dL = dict_pack(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    dD = dict_pack(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G33-chi-split-consistent-death-is-edge",
          dL["g"]["opnorm"] < 1.0 and dL["pk"]["nC"] == 0
          and dD["g"]["opnorm"] > 1.0 and dD["pk"]["nC"] == 1
          and dL["dT"] <= FORMULA_HI and dD["dT"] <= FORMULA_HI,
          "chi9 ||T||=%.6f nC=0; dead-15 ||T||=%.6f nC=1 "
          "(split holds; death is edge)"
          % (dL["g"]["opnorm"], dD["g"]["opnorm"]))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("threshold_identity_probe -- "
          "PRIME.LDAGGER.THRESHOLD_IDENTITY.01 (round 411)")
    print("SPEC_SHA %s   (B %s / DI %s / CT %s)"
          % (SPEC_SHA[:16], B.SPEC_SHA[:16], DI.SPEC_SHA[:16],
             CT.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else
                        "FULL (core-42 + kz130 + EXT)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT SHA")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (B.SPEC_SHA.startswith(B_SHA_PREFIX)
              and DI.SPEC_SHA.startswith(DI_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX)
              and CT.SPEC_SHA.startswith(CT_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "B %s / DI %s / CT %s" % (B.SPEC_SHA[:8], DI.SPEC_SHA[:8],
                                    CT.SPEC_SHA[:8]))

    part_satz()
    w9 = part_w9()
    part_pd_seq(w9, smoke)
    part_kills(w9)

    section("S5  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G50-verdict",
          prev_ok,
          "ENERGY_SPLIT_EXACT / SATURATION_REFUTED: "
          "||T||=1/sqrt(Cmin) SATZ; exact ||T||=1 on PD "
          "REFUTED; no RH / L* / R-dagger claim")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    verd = "ENERGY_SPLIT_EXACT / SATURATION_REFUTED"
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("THRESHOLD IDENTITY %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("THRESHOLD IDENTITY FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
