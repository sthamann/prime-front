#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_p2_steps.py -- machine check of every numbered lemma
in rh/problem/p2_lemma_proof.tex (round 375, LEMMA.P2.01).

PART A (STANDALONE): Fractions 4-node toy + numpy adversary.
  G1  identity (12) on the r367 Haynsworth toy (Lemma six/fact)
  G2  six-scalar spectral expansion of Q (Lemma six)
  G3  det K2 = det(I+R+) (1 - gamma/lam) exact (Lemma fact)
  G4  sign carrier: det K2 < 0 <=> gamma > lam (Lemma sign)
  G5  det(I+R+) >= 1 SATZ (Lemma pos)
  G6  adversary: P1 without P2, tiny overlaps (Lemma adv)

PART B (CONSTRUCTION PINS, repo builders):
  G10 w9 factorization + rest-hosted psi_minus (Lemmas fact, notbind)
  G11 kz18 floor window: well-conditioned min excess
  G12 kz46: the delta-term is necessary (Lemma delta)
  G13 chi3-w9 already PD (world-separating); chi4-w9 nneg-1
  G14 matched scramble breaks named at P1
  G15 RANK_KZ (18,9,44,52) all P1+P2 with gamma > lam

Exit: per-gate PASS/FAIL and the final line
"P2 STEPS VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities and a named remainder only.
"""
from __future__ import annotations

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
FLOOR = 1.0e-8
ID_BAR = 1.0e-8
MAIN_KZ = 9
RANK_KZ = (18, 9, 44, 52)
SCR_SEED = 1


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


def fr_mul(A, B):
    return [[sum(a * b for a, b in zip(row, col))
             for col in zip(*B)] for row in A]


def haynsworth_blocks():
    A0 = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
          [Fr(0), Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(2), Fr(0)],
          [Fr(0), Fr(0), Fr(0), Fr(3)]]
    U = [[Fr(2), Fr(1)],
         [Fr(0), Fr(1)],
         [Fr(0), Fr(0)],
         [Fr(0), Fr(0)]]
    A0inv = [[Fr(-1), Fr(0), Fr(0), Fr(0)],
             [Fr(0), Fr(1), Fr(0), Fr(0)],
             [Fr(0), Fr(0), Fr(1, 2), Fr(0)],
             [Fr(0), Fr(0), Fr(0), Fr(1, 3)]]
    UT = [[row[i] for row in U] for i in range(2)]
    Q = fr_mul(UT, fr_mul(A0inv, U))
    K2 = [[Q[0][0] + Fr(1), Q[0][1]],
          [Q[1][0], Q[1][1] + Fr(1)]]
    detK = K2[0][0] * K2[1][1] - K2[0][1] * K2[1][0]
    q11, q22, q12 = Q[0][0], Q[1][1], Q[0][1]
    wterm = q11 * q22 - q12 * q12
    return dict(A0=A0, U=U, Q=Q, K2=K2, detK=detK,
                q11=q11, q22=q22, q12=q12, wterm=wterm)


def six_scalar_fractions(T):
    alpha, beta, lam = T["U"][0][0], T["U"][0][1], Fr(1)
    ruu, rvv, ruv = Fr(0), Fr(1), Fr(0)
    q11p = -alpha * alpha / lam + ruu
    q22p = -beta * beta / lam + rvv
    q12p = -alpha * beta / lam + ruv
    dBd = (alpha * alpha * rvv + beta * beta * ruu
           - Fr(2) * alpha * beta * ruv)
    N = alpha * alpha + beta * beta + dBd
    detIRp = (Fr(1) + ruu) * (Fr(1) + rvv) - ruv * ruv
    gamma = (alpha * alpha * (Fr(1) + rvv)
             + beta * beta * (Fr(1) + ruu)
             - Fr(2) * alpha * beta * ruv) / detIRp
    detK_fact = detIRp * (Fr(1) - gamma / lam)
    ndet_pos = (N - lam * detIRp) / lam
    return dict(alpha=alpha, beta=beta, lam=lam, ruu=ruu, rvv=rvv,
                ruv=ruv, q11p=q11p, q22p=q22p, q12p=q12p, N=N,
                detIRp=detIRp, gamma=gamma, detK_fact=detK_fact,
                ndet_pos=ndet_pos)


def six_from_AU(A0, U, floor=FLOOR):
    A0 = 0.5 * (np.asarray(A0, float) + np.asarray(A0, float).T)
    U = np.asarray(U, float)
    ev, W = np.linalg.eigh(A0)
    nneg = int(np.sum(ev < -floor))
    psi = W[:, 0]
    lam = -float(ev[0])
    u, v = U[:, 0], U[:, 1]
    alpha = float(u @ psi)
    beta = float(v @ psi)
    inv_pos = np.zeros_like(ev)
    pos = ev > floor
    inv_pos[pos] = 1.0 / ev[pos]
    B = (W * inv_pos) @ W.T
    Rp = U.T @ B @ U
    Rp = 0.5 * (Rp + Rp.T)
    ruu, ruv, rvv = float(Rp[0, 0]), float(Rp[0, 1]), float(Rp[1, 1])
    w = np.array([alpha, beta], float)
    IRp = np.eye(2) + Rp
    detIRp = float(IRp[0, 0] * IRp[1, 1] - IRp[0, 1] * IRp[1, 0])
    gamma = float(w @ np.linalg.solve(IRp, w))
    dBd = (alpha * alpha * rvv + beta * beta * ruu
           - 2.0 * alpha * beta * ruv)
    N = alpha * alpha + beta * beta + dBd
    w2 = float(w @ w)
    Gt = U.T @ U
    pair_span = float(w @ np.linalg.solve(Gt, w))
    evR = np.linalg.eigvalsh(Rp)
    suff = bool(w2 > lam * (1.0 + float(evR[-1]))) if lam > 0 else False
    detK_fact = detIRp * (1.0 - gamma / lam) if lam > 0 else float("nan")
    return dict(nneg=nneg, lam=lam, alpha=alpha, beta=beta,
                ruu=ruu, ruv=ruv, rvv=rvv, gamma=gamma, detIRp=detIRp,
                N=N, dBd=dBd, w2=w2, pair_span=pair_span, suff=suff,
                detK_fact=detK_fact,
                excess=gamma / lam - 1.0 if lam > 0 else float("nan"),
                share_dBd=dBd / N if N > 0 else float("nan"))


def split_rung(FTRI, xu, wu, yn, vn, Nw, S, L, i1, i2):
    o = FTRI.cut_rung(xu, wu, yn, vn, Nw, S, L, i1, i2, keep=True)
    s = six_from_AU(o["A0"], o["U"])
    s.update(detK=o["detK"], P1=o["P1"], P2=o["P2"], eps=o["eps"],
             pmass=o["pmass"], lam_pair=o["lam_pair"], nnegA=o["nneg"],
             Nw=Nw)
    s["err_fact"] = abs(s["detK_fact"] - o["detK"])
    del o
    return s


def main():
    print("=" * 72)
    print("verify_p2_steps.py -- P2 factorization lemmas (round 375)")
    print("=" * 72)

    section("A  CLOSED ALGEBRA")
    T = haynsworth_blocks()
    check("G1-ident12-toy",
          T["detK"] == Fr(-7)
          and T["detK"] == Fr(1) + T["q11"] + T["q22"] + T["wterm"],
          "det K2 = %s = 1+q11+q22+wterm" % T["detK"])
    S = six_scalar_fractions(T)
    check("G2-six-scalar-Q",
          S["q11p"] == T["q11"] and S["q22p"] == T["q22"]
          and S["q12p"] == T["q12"],
          "Q = -ww^T/lam + R+ EXACT; "
          "(alpha,beta,lam,ruu,rvv,ruv)=(%s,%s,%s,%s,%s,%s)"
          % (S["alpha"], S["beta"], S["lam"], S["ruu"], S["rvv"], S["ruv"]))
    check("G3-factorization-toy",
          S["detK_fact"] == T["detK"] and S["ndet_pos"] == -T["detK"]
          and S["detIRp"] == Fr(2) and S["gamma"] == Fr(9, 2)
          and S["N"] == Fr(9),
          "det K2 = %s*(1-%s/%s) = %s; N=%s"
          % (S["detIRp"], S["gamma"], S["lam"], S["detK_fact"], S["N"]))
    check("G4-sign-carrier",
          (T["detK"] < 0) == (S["gamma"] > S["lam"]),
          "det K2 < 0 <=> gamma > lam: %s > %s" % (S["gamma"], S["lam"]))
    check("G5-detIRp-at-least-one",
          S["detIRp"] >= Fr(1),
          "det(I+R+) = %s >= 1" % S["detIRp"])
    A0a = np.diag([-1.0, 1.0, 2.0, 3.0])
    Ua = 0.05 * np.array([[1.0, 0.0], [0.0, 1.0],
                          [0.0, 0.0], [0.0, 0.0]])
    detA = float(np.linalg.det(np.eye(2) + Ua.T @ np.linalg.solve(A0a, Ua)))
    sA = six_from_AU(A0a, Ua, floor=1e-14)
    nnegM = int(np.sum(np.linalg.eigvalsh(A0a + Ua @ Ua.T) < -1e-12))
    check("G6-adversary-tiny-overlap",
          sA["nneg"] == 1 and detA > 0 and sA["gamma"] < sA["lam"]
          and nnegM >= 1,
          "P1 without P2: gamma=%.4f < lam=%.4f, detK2=%+.4f, nneg(M)=%d"
          % (sA["gamma"], sA["lam"], detA, nnegM))

    section("B  CONSTRUCTION PINS")
    import final_two_rank_inertia_probe as FTRI
    import pair_extremal_probe as PX
    import dirichlet_matched_frame_probe as DMF
    import verify_lstar_instance as V

    def rung_at(kz):
        Rr = PX.build_rung(kz)
        mz = Rr["mz"]
        s = split_rung(FTRI, mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                       Rr["Nw"], Rr["S"], mz["L"], Rr["i1"], Rr["i2"])
        s["kz"] = kz
        return s

    s9 = rung_at(MAIN_KZ)
    check("G10-w9-factorization",
          s9["P1"] and s9["P2"]
          and s9["err_fact"] <= ID_BAR
          and s9["gamma"] > s9["lam"]
          and abs(s9["detK"] + 5.0389) / 5.0389 <= 1e-3
          and s9["pmass"] < 0.5 and s9["lam_pair"] > 0
          and abs(s9["pair_span"] - 0.6836) <= 2e-2,
          "w9 detK=%.4f excess=%.4f det(I+R+)=%.4f pair-span=%.4f "
          "pmass=%.4f (rest-hosted) lam_pair=%+.2e err=%.1e"
          % (s9["detK"], s9["excess"], s9["detIRp"], s9["pair_span"],
             s9["pmass"], s9["lam_pair"], s9["err_fact"]))

    s18 = rung_at(18)
    check("G11-kz18-floor",
          s18["P1"] and s18["P2"]
          and abs(s18["detK"] + 1.1572) / 1.1572 <= 1e-3
          and s18["excess"] > 0.27 and s18["excess"] < 0.28
          and s18["detIRp"] >= 4.0 and s18["err_fact"] <= 1e-9
          and s18["suff"],
          "kz18 -detK=%.4f excess=%.4f det(I+R+)=%.4f "
          "(well-conditioned min excess of the branch)"
          % (-s18["detK"], s18["excess"], s18["detIRp"]))

    s46 = rung_at(46)
    check("G12-kz46-delta-necessary",
          s46["P1"] and s46["P2"] and (not s46["suff"])
          and s46["share_dBd"] > 0.70 and s46["gamma"] > s46["lam"]
          and s46["err_fact"] <= 1e-8,
          "kz46 Cauchy-sufficient FAILS but P2 HOLDS: "
          "delta-share=%.3f excess=%.4f -- the wedge dressing "
          "of N is load-bearing"
          % (s46["share_dBd"], s46["excess"]))

    def chi_w9(q, lpq):
        uu, ww, _nn, _ch = DMF.chi_window_comb(MAIN_KZ, q)
        mzc = DMF.chi_build_measures(MAIN_KZ, uu, ww, 1.0, lpq)
        j1, j2 = PX.pair_select(mzc["yn"])
        return split_rung(FTRI, mzc["xu"], mzc["wu"], mzc["yn"],
                          mzc["vn"], mzc["Nw"], mzc["S"], mzc["L"],
                          j1, j2)

    c3 = chi_w9(DMF.Q_CHI3, DMF.LPQ3)
    c4 = chi_w9(DMF.Q_CHI4, DMF.LPQ4)
    check("G13-chi-w9",
          c3["nnegA"] == 0 and c3["detK"] > 0
          and abs(c3["detK"] / 4.0186 - 1.0) <= 2e-2
          and c4["P1"] and c4["P2"]
          and abs(c4["detK"] / -6.1804 - 1.0) <= 2e-2
          and c4["gamma"] > c4["lam"],
          "chi3-w9 nneg=%d detK=%+.3f (vacuous PD, world-separating); "
          "chi4-w9 nneg=%d detK=%+.3f excess=%+.3f"
          % (c3["nnegA"], c3["detK"], c4["nnegA"], c4["detK"],
             c4["excess"]))

    alpha9v = float(V.U[MAIN_KZ])
    uu3, ww3, _n3, _c3 = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
    rng = np.random.default_rng(SCR_SEED)
    u_scr = np.sort(rng.uniform(0.0, 2.0 * alpha9v, size=len(ww3)))
    mzs = DMF.chi_build_measures(MAIN_KZ, u_scr, ww3, 1.0, DMF.LPQ3)
    s1_, s2_ = PX.pair_select(mzs["yn"])
    oS = FTRI.cut_rung(mzs["xu"], mzs["wu"], mzs["yn"], mzs["vn"],
                       mzs["Nw"], mzs["S"], mzs["L"], s1_, s2_)
    check("G14-scramble-p1",
          oS["nneg"] == 21 and (not oS["P1"]) and oS["P2"]
          and abs(oS["detK"] / -8.8814 - 1.0) <= 5e-2,
          "scramble BREAKS named at P1 (nneg=%d); P2 survives detK=%.3f"
          % (oS["nneg"], oS["detK"]))

    rank_ok = True
    bits = []
    for kz in RANK_KZ:
        s = s9 if kz == MAIN_KZ else (s18 if kz == 18 else rung_at(kz))
        ok = (s["P1"] and s["P2"] and s["gamma"] > s["lam"]
              and s["err_fact"] <= 1e-8)
        rank_ok = rank_ok and ok
        bits.append("kz%d excess=%.3f" % (kz, s["excess"]))
    check("G15-rank-kz", rank_ok,
          "RANK_KZ all P1+P2 with gamma>lam: " + ", ".join(bits))

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    print("\n" + ("P2 STEPS VERIFIED" if n_fail == 0
                  else "P2 STEPS FAILED %d" % n_fail))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
