#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""verify_postcap_steps.py -- machine check of every numbered lemma
in rh/problem/postcap_pivots.tex (round 377, LEMMA.POSTCAP_PIVOTS.01).

PART A (STANDALONE): Fractions five-atom toy + trig identities.
  G1  det K2 = H_N(w) H_{N-3}(a) / (H_{N+2}(w) H_{N-1}(a))
      = 1/(h_N h_{N+1} h_{N-3}(a) h_{N-2}(a))  = -196/35719
  G2  signed Borodin complement H_r(sigma a) = H_{S-r}(w)/C, all r
  G3  inertia complement In H_k(w)+In H_{S-k}(sa)=In diag(w)
  G4  adversary: det K2 = 1/2 with M still indefinite
  G5  signed Stieltjes pivots match Hankel signs and |h| (rel < 1e-10)
  G6  P_X(x)=2^{1-S}(x+1)U_{S-1}(x) vanishes on cosine nodes S=5,7,9
  G7  Chebyshev aliasing T_{S+k}(x_j)=(-1)^j T_k(x_j) on S=5
  G8  power-moment recurrence of P_X on cosine S=5 (rel < 1e-10)
  G9  low-mode positive f on S=5: all h_j>0 (mesh alone does not
      force a post-cap defect)

PART B (CONSTRUCTION PINS, repo builders):
  G10 w9 PINNED_N: first_neg=N, nneg_pref=1, h_N h_{N+1}<0, detK<0
  G11 kz12 LATE counterexample: first_neg=N+2, product>0, nnegA=0,
      detK>0, Mpd (universal P2-POSTCAP is false)
  G12 kz15 PINNED_Np1: first_neg=N+1, product<0, nnegA=1
  G13 chi3-w9 vacuous: nneg_pref=0, first=N+2, detK>0
  G14 scramble EARLY: first_neg=21, nneg_pref=37 (named P1 break)
  G15 dictionary (detK<0)==(sN*sNp1<0) on {9,12,15}
  G16 dead chi3-15 still nneg_pref<=1 (terminal death is not a
      prefix-pivot failure)

Exit: per-gate PASS/FAIL and the final line
"POSTCAP STEPS VERIFIED" iff every gate passed.

NO RH CLAIM.  Finite identities, a named counterexample, and
construction pins only.
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
PROB = os.path.dirname(os.path.abspath(__file__))
for p in (DISC, VERIFY, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

CHECKS = []
MAIN_KZ = 9
SCR_SEED = 1
ID_BAR = 1.0e-8


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


def det(A):
    A = [r[:] for r in A]
    n = len(A)
    d = Fr(1)
    for j in range(n):
        p = next((i for i in range(j, n) if A[i][j]), None)
        if p is None:
            return Fr(0)
        if p != j:
            A[j], A[p] = A[p], A[j]
            d = -d
        q = A[j][j]
        d *= q
        for i in range(j + 1, n):
            c = A[i][j] / q
            for k in range(j + 1, n):
                A[i][k] -= c * A[j][k]
    return d


def Hdet(xs, ws, n):
    if n == 0:
        return Fr(1)
    mu = [sum(w * x ** k for x, w in zip(xs, ws)) for k in range(2 * n - 1)]
    return det([[mu[i + j] for j in range(n)] for i in range(n)])


def hrat(xs, ws, j):
    return Hdet(xs, ws, j + 1) / Hdet(xs, ws, j)


def Hmat(xs, ws, n):
    if n == 0:
        return []
    mu = [sum(ww * xx ** k for xx, ww in zip(xs, ws))
          for k in range(2 * n - 1)]
    return [[mu[i + j] for j in range(n)] for i in range(n)]


def chebU(n):
    if n == 0:
        return [1]
    if n == 1:
        return [2, 0]
    um2, um1 = [1], [2, 0]
    for _ in range(2, n + 1):
        a = [2 * c for c in um1] + [0]
        b = [0] * (len(a) - len(um2)) + um2
        nxt = [a[i] - b[i] for i in range(len(a))]
        um2, um1 = um1, nxt
    return um1


def chebT(n):
    if n == 0:
        return [1]
    if n == 1:
        return [1, 0]
    tm2, tm1 = [1], [1, 0]
    for _ in range(2, n + 1):
        a = [2 * c for c in tm1] + [0]
        b = [0] * (len(a) - len(tm2)) + tm2
        nxt = [a[i] - b[i] for i in range(len(a))]
        tm2, tm1 = tm1, nxt
    return tm1


def poly_mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def poly_eval(p, x):
    v = 0.0
    for c in p:
        v = v * x + float(c)
    return v


def pivot_signs(x, w, nmax):
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    q = np.ones_like(x)
    qm = np.zeros_like(x)
    eta = float(np.dot(w, q * q))
    signs = [int(np.sign(eta)) if eta != 0 else 0]
    logh = [math.log(abs(eta)) if eta != 0 else float("-inf")]
    log_s = 0.0
    log_sm = 0.0
    etam = 1.0
    for n in range(nmax):
        if abs(eta) < 1e-300:
            signs.append(0)
            logh.append(float("-inf"))
            break
        al = float(np.dot(w, x * q * q)) / eta
        if n == 0:
            rvec = (x - al) * q
        else:
            coef = math.exp(log_s - log_sm) * (eta / etam)
            rvec = (x - al) * q - coef * qm
        sc = float(np.max(np.abs(rvec)))
        if sc == 0.0:
            signs.append(0)
            logh.append(float("-inf"))
            break
        qm = q
        q = rvec / sc
        log_sm = log_s
        log_s = log_s + math.log(sc)
        etam, eta = eta, float(np.dot(w, q * q))
        signs.append(int(np.sign(eta)) if eta != 0 else 0)
        logh.append(2.0 * log_s + math.log(abs(eta)) if eta != 0
                    else float("-inf"))
    return signs, logh


def classify(sg, N):
    first = next((j for j, s in enumerate(sg) if s < 0), None)
    nneg = sum(1 for s in sg[:N + 2] if s < 0)
    sN = sg[N] if len(sg) > N else 0
    sNp1 = sg[N + 1] if len(sg) > N + 1 else 0
    free = all(s > 0 for s in sg[:N])
    if first is None:
        cls = "NONE"
    elif not free:
        cls = "EARLY"
    elif nneg > 1:
        cls = "MULTI"
    elif sN < 0 and sNp1 > 0:
        cls = "PINNED_N"
    elif sN > 0 and sNp1 < 0:
        cls = "PINNED_Np1"
    elif sN < 0 and sNp1 < 0:
        cls = "DOUBLE"
    elif first > N + 1:
        cls = "LATE"
    else:
        cls = "OTHER"
    return dict(cls=cls, first_neg=first, nneg_pref=nneg,
                sN=int(sN), sNp1=int(sNp1), free=bool(free),
                offset=(None if first is None else first - N))


def main():
    section("A  STANDALONE FRACTIONS + TRIG")

    xs = list(map(Fr, [-2, -1, 0, 2, 3]))
    w = list(map(Fr, [2, -3, 5, -7, 11]))
    S, N, r = 5, 3, 0
    pd = [math.prod(xs[i] - xs[j] for j in range(S) if j != i)
          for i in range(S)]
    a = [Fr(1, 1) / (abs(w[i]) * pd[i] ** 2) for i in range(S)]
    sa = [(Fr(1) if w[i] > 0 else Fr(-1)) * a[i] for i in range(S)]
    detK = (hrat(xs, sa, r) * hrat(xs, sa, r + 1)) / (
        hrat(xs, a, r) * hrat(xs, a, r + 1))
    post = Fr(1) / (hrat(xs, w, N) * hrat(xs, w, N + 1)
                    * hrat(xs, a, r) * hrat(xs, a, r + 1))
    # det K2 = H_N(w) H_{N-3}(a) / (H_{N+2}(w) H_{N-1}(a))
    hankel = (Hdet(xs, w, N) * Hdet(xs, a, N - 3)) / (
        Hdet(xs, w, N + 2) * Hdet(xs, a, N - 1))
    prod_h = hrat(xs, w, N) * hrat(xs, w, N + 1)
    check("G1-detK-dictionary",
          detK == post == hankel == Fr(-196, 35719)
          and prod_h == Fr(-85536000, 7),
          "detK=post=hankel=%s; hN hN+1=%s" % (detK, prod_h))

    Delta2 = math.prod((xs[j] - xs[i]) ** 2
                       for i in range(S) for j in range(i + 1, S))
    C = Delta2 * math.prod(w)
    comp_ok = all(Hdet(xs, sa, rr) == Hdet(xs, w, S - rr) / C
                  for rr in range(S + 1))
    check("G2-borodin-complement", comp_ok,
          "H_r(sa)=H_{S-r}(w)/C on r=0..%d" % S)

    import final_two_rank_inertia_probe as FTI  # noqa: E402
    wv = [Fr(1, 1) / (w[i] * pd[i] ** 2) for i in range(S)]
    full = (sum(x > 0 for x in w), sum(x < 0 for x in w), 0)
    iner_ok = True
    bits = []
    for k in range(1, S):
        i1 = FTI.fr_inertia(Hmat(xs, w, k))
        i2 = FTI.fr_inertia(Hmat(xs, wv, S - k))
        sm = tuple(i1[j] + i2[j] for j in range(3))
        bits.append("k=%d %s+%s=%s" % (k, i1, i2, sm))
        iner_ok = iner_ok and (sm == full)
    check("G3-inertia-complement", iner_ok,
          "; ".join(bits))

    A = [[Fr(-2), Fr(0)], [Fr(0), Fr(1)]]
    K = [[Fr(1, 2), Fr(0)], [Fr(0), Fr(1)]]
    M = [[Fr(-1), Fr(0)], [Fr(0), Fr(1)]]
    check("G4-adversary",
          det(K) == Fr(1, 2) and det(M) == Fr(-1)
          and M[0][0] < 0 and M[1][1] > 0,
          "detK=1/2, M=diag(-1,1) indefinite; A=diag(-2,1)")

    xsf = [float(v) for v in xs]
    wf = [float(v) for v in w]
    sg, lh = pivot_signs(xsf, wf, 6)
    true_h = [hrat(xs, w, j) for j in range(5)]
    sign_ok = all(sg[j] == int(np.sign(float(true_h[j])))
                  for j in range(5))
    rels = [abs(math.exp(lh[j]) / abs(float(true_h[j])) - 1)
            for j in range(5)]
    check("G5-stieltjes-hankel",
          sign_ok and max(rels) < 1e-10,
          "signs %s; max |h| reldev %.3e" % (sg[:5], max(rels)))

    px_ok = True
    px_bits = []
    for Sv in (5, 7, 9):
        Un = chebU(Sv - 1)
        Px_int = poly_mul([1, 1], Un)
        px_ok = px_ok and (Px_int[0] == 2 ** (Sv - 1))
        thetas = [math.pi * j / Sv for j in range(1, Sv + 1)]
        xs_c = [math.cos(th) for th in thetas]
        vals = [2.0 ** (1 - Sv) * poly_eval(Px_int, x) for x in xs_c]
        mx = max(abs(v) for v in vals)
        px_ok = px_ok and mx < 1e-10 and abs(xs_c[-1] + 1.0) < 1e-14
        px_bits.append("S=%d max|P_X|=%.2e" % (Sv, mx))
    check("G6-node-polynomial", px_ok, "; ".join(px_bits))

    S5 = 5
    th = [math.pi * j / S5 for j in range(1, S5 + 1)]
    xc = np.array([math.cos(t) for t in th])
    alias_ok = True
    for k in range(0, 6):
        Tk = chebT(k)
        Tsk = chebT(S5 + k)
        for j, x in enumerate(xc, start=1):
            lhs = poly_eval(Tsk, x)
            rhs = ((-1) ** j) * poly_eval(Tk, x)
            alias_ok = alias_ok and abs(lhs - rhs) < 1e-10
    check("G7-chebyshev-alias", alias_ok,
          "T_{S+k}(x_j)=(-1)^j T_k(x_j) on S=5, k=0..5")

    P5 = [Fr(1), Fr(1), Fr(-3, 4), Fr(-3, 4), Fr(1, 16), Fr(1, 16)]
    f = 1.0 + 0.3 * np.cos(th) + 0.1 * np.cos(2.0 * np.array(th))
    wj = (1.0 - xc) * f
    moms = [float(np.sum(wj * xc ** k)) for k in range(12)]
    a5 = [float(c) for c in P5[1:]]
    mom_ok = True
    mom_bits = []
    for k in range(4):
        pred = -sum(a5[i] * moms[4 - i + k] for i in range(5))
        rel = (abs(pred / moms[5 + k] - 1) if moms[5 + k]
               else abs(pred))
        mom_ok = mom_ok and rel < 1e-10
        mom_bits.append("m_%d rel=%.2e" % (5 + k, rel))
    check("G8-moment-alias", mom_ok, "; ".join(mom_bits))

    sgc, _ = pivot_signs(xc, wj, 6)
    check("G9-lowmode-no-defect",
          all(s > 0 for s in sgc[:6]) and len(sgc) >= 6,
          "cosine S=5 low-mode f: signs %s (all +)" % sgc[:6])

    section("B  CONSTRUCTION PINS")
    import dirichlet_matched_frame_probe as DMF  # noqa: E402
    import pair_extremal_probe as PX  # noqa: E402
    import verify_lstar_instance as V  # noqa: E402
    import hirota_sign_probe as HS  # noqa: E402

    def row_at(kz, mz=None):
        if mz is None:
            mz = V.build_measures(kz)
        Nloc = int(mz["Nw"])
        sg_loc, _ = pivot_signs(mz["xu"], mz["wu"], Nloc + 3)
        c = classify(sg_loc, Nloc)
        j1, j2 = PX.pair_select(mz["yn"])
        o = FTI.cut_rung(mz["xu"], mz["wu"], mz["yn"], mz["vn"],
                         mz["Nw"], mz["S"], mz["L"], j1, j2)
        c.update(kz=kz, N=Nloc, detK=float(o["detK"]),
                 nnegA=int(o["nneg"]), Mpd=bool(o["Mpd"]),
                 P1=bool(o["P1"]), P2=bool(o["P2"]))
        return c

    s9 = row_at(MAIN_KZ)
    check("G10-w9-PINNED_N",
          s9["cls"] == "PINNED_N"
          and s9["first_neg"] == s9["N"]
          and s9["nneg_pref"] == 1
          and s9["sN"] * s9["sNp1"] < 0
          and s9["detK"] < 0
          and s9["nnegA"] == 1
          and abs(s9["detK"] / -5.0389 - 1.0) <= 2e-3,
          "w9 N=%d first=%s nneg=%d sN sN+1=%+d%+d detK=%+.4f nnegA=%d"
          % (s9["N"], s9["first_neg"], s9["nneg_pref"],
             s9["sN"], s9["sNp1"], s9["detK"], s9["nnegA"]))

    s12 = row_at(12)
    check("G11-kz12-LATE-counterexample",
          s12["cls"] == "LATE"
          and s12["first_neg"] == s12["N"] + 2
          and s12["sN"] * s12["sNp1"] > 0
          and s12["nneg_pref"] == 0
          and s12["nnegA"] == 0
          and s12["detK"] > 0
          and s12["Mpd"]
          and abs(s12["detK"] / 12.4632 - 1.0) <= 2e-2,
          "kz12 N=%d first=%s nneg=%d product>0 detK=%+.4f nnegA=%d Mpd=%s"
          % (s12["N"], s12["first_neg"], s12["nneg_pref"],
             s12["detK"], s12["nnegA"], s12["Mpd"]))

    s15 = row_at(15)
    check("G12-kz15-PINNED_Np1",
          s15["cls"] == "PINNED_Np1"
          and s15["first_neg"] == s15["N"] + 1
          and s15["sN"] * s15["sNp1"] < 0
          and s15["nnegA"] == 1
          and s15["detK"] < 0,
          "kz15 N=%d first=%s nneg=%d sN sN+1=%+d%+d detK=%+.4f"
          % (s15["N"], s15["first_neg"], s15["nneg_pref"],
             s15["sN"], s15["sNp1"], s15["detK"]))

    uu, ww, _nn, _ch = DMF.chi_window_comb(MAIN_KZ, DMF.Q_CHI3)
    mzc = DMF.chi_build_measures(MAIN_KZ, uu, ww, 1.0, DMF.LPQ3)
    c3 = row_at(MAIN_KZ, mzc)
    check("G13-chi3-w9-vacuous",
          c3["nneg_pref"] == 0
          and c3["first_neg"] == c3["N"] + 2
          and c3["nnegA"] == 0
          and c3["detK"] > 0
          and abs(c3["detK"] / 4.0186 - 1.0) <= 2e-2,
          "chi3-w9 N=%d first=%s nneg=%d detK=%+.4f nnegA=%d"
          % (c3["N"], c3["first_neg"], c3["nneg_pref"],
             c3["detK"], c3["nnegA"]))

    d = HS.window_data(9, scramble_seed=SCR_SEED)
    xu = np.concatenate([d["xs"], d["ys"]])
    wu = np.concatenate([d["ws"], -d["vs"]])
    o = np.argsort(xu)
    mz_s = dict(xu=xu[o], wu=wu[o], Nw=d["n_max"], S=len(xu),
                yn=d["ys"], vn=d["vs"], L=2 * len(xu))
    # L is unused by classify; cut_rung needs L == 2S
    Nscr = int(mz_s["Nw"])
    sg_s, _ = pivot_signs(mz_s["xu"], mz_s["wu"], Nscr + 3)
    cs = classify(sg_s, Nscr)
    check("G14-scramble-EARLY",
          cs["cls"] == "EARLY"
          and cs["first_neg"] == 21
          and cs["nneg_pref"] == 37
          and (not cs["free"]),
          "scramble first=%s nneg=%d free=%s cls=%s"
          % (cs["first_neg"], cs["nneg_pref"], cs["free"], cs["cls"]))

    dict_ok = True
    dict_bits = []
    for s in (s9, s12, s15):
        lhs = s["detK"] < 0
        rhs = s["sN"] * s["sNp1"] < 0
        dict_ok = dict_ok and (lhs == rhs)
        dict_bits.append("kz%d detK%+.3f product_sign=%d"
                         % (s["kz"], s["detK"],
                            int(np.sign(s["sN"] * s["sNp1"]))))
    check("G15-dictionary-live", dict_ok, "; ".join(dict_bits))

    uu15, ww15, _n15, _c15 = DMF.chi_window_comb(15, DMF.Q_CHI3)
    mz15 = DMF.chi_build_measures(15, uu15, ww15, 1.0, DMF.LPQ3)
    d15 = row_at(15, mz15)
    check("G16-dead-chi3-15-still-P1",
          d15["nneg_pref"] <= 1 and d15["free"],
          "dead chi3-15 cls=%s nneg=%d first=%s free=%s"
          % (d15["cls"], d15["nneg_pref"], d15["first_neg"], d15["free"]))

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    print("\n" + ("POSTCAP STEPS VERIFIED" if n_fail == 0
                  else "POSTCAP STEPS FAILED %d" % n_fail))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
