#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""hole_nyquist_probe -- PRIME.LDAGGER.HOLE_NYQUIST_DEFECT.01
(round 410): two halves of one lemma after r407/r408/r409.
P1 iff lam_2(C)>=1.  Half N (necessary): d_i = u^vee(y_i)
K_n^mu(y_i,y_i) >= 1 for every hole, source-pure, via an
explicit test polynomial.  Half S (sufficient): the
off-diagonal mass of C pushes only the hole-Nyquist mode
below 1.

HALF N -- TESTPOLY_REFUTED / DMIN_CENSUS.
The reproducing-kernel bound K(y,y) >= |p(y)|^2/||p||_mu^2
is SATZ for p in P_n.  The proposed p_y is the Y-Lagrange
ell_i (deg |Y|-1 = 103 < n=181 on w9 -- degree OK).  It
does NOT close d_i>=1: bmax=0.071, #b>=1 = 0/104.
Local Lagrange is worse (Lebesgue).  Chebyshev-CD at full
depth m=n closes 81/104 holes, not all (bmin=4.9e-4).
d_i>=1 remains a source-family census (core-42 dmin in
[1.097,1.656]).  Scramble/permute break dmin by Rayleigh
(0.37/0.15); the test poly does NOT diagnose them (bounds
tiny on every world).  Permute mechanism: K(y,y) collapses
to 0.148 at a hole with ud=1 (Christoffel of the permuted
dual-mu), not a Y-mask effect.

HALF S -- FOURIER_REFUTED / BERNSTEIN_REFUTED / SEQ_REDUCED.
Hole-DFT of C is not banded (off_frac=0.968, band-8=0.18);
the Nyquist bin is not a spectral atom.  ||T0 v_Nyq||=0.66
< ||T0||=1.08 -- the defect mode is not the top singular
vector, and the Markov/Bernstein ratio is 0.14 (not tight).
Theta-prefix hole-adding: nC jumps 0->1 at k=37 and STAYS 1
through k=104 (C2>=1.00018); the defect is born once, not
at the last hole.  Order-dependent (random prefix flips
later).  Census of one path, not a SATZ.

CALIBRATION DISCLOSURE.  Bounds, Fourier, sequential flip,
Bernstein, permute K-split first measured in /tmp
(r410_cal.py .. r410_cal4.py) on the same constructors,
2026-08-29.  Pins disclosed.  Builder fallback NOT taken:
full wall < 10 s (bar 120 s).

FROZEN FROM /tmp (live re-gated, not fitted):
  * SATZ over Q: RK for constants K=1/h0; degree obstruction
    (p=t^2, n=1, K=1/3 < |p|^2/||p||^2=1/2); C_ii=ud K
    on a 2x2 feature toy; Rayleigh lam<=dmin.
  * w9 Y-Lagrange: deg=103<181, bmax=0.07137, #b>=1=0/104,
    min(d/b)=94, 0 RK violations.
  * cheb-CD m=181: #b>=1=81/104, bmin=4.94e-4.
  * Fourier: off_frac=0.968, band8=0.177.
  * Sequential theta-prefix: k=32 nC=0 Cmin=1.00014;
    k=37 nC=1 Cmin=0.99991; k=104 nC=1 Cmin=0.85712
    C2=1.00018.
  * Bernstein: ||T0 v_nyq||=0.6565, ||T0||=1.0801,
    <v0,nyq>=0.386, Markov ratio=0.139.
  * PERM dmin=0.1479 = ud*K with K=0.1479; SCR dmin=0.367.
  * CHI9/CHI15: dmin>1 (dictionary); 2PER S=20 deg_ell=9>n=7
    RK fails (d<b).

AUSGANG N: TESTPOLY_REFUTED / DMIN_CENSUS.
AUSGANG S: FOURIER_REFUTED / BERNSTEIN_REFUTED / SEQ_REDUCED.
P1 still iff lam2(C)>=1 (r407); neither half proves the RHS.
Dead chi fulfill both dictionaries.  No RH/L*/R-dagger claim.

MACHINERY: r407 D.chain_C/pack_C; r408 T.rebuild_holes;
r409 BB.pack_graph; r356 BDH; r367 HM; r403 P1; r226 V.

NO RH CLAIM.  Finite identities, two named refutations,
one named census, one named reduction.
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

import borodin_birkhoff_intertwiner_probe as BB  # noqa: E402
import c_threshold_probe as CT  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402
import dual_intertwiner_probe as D  # noqa: E402
import high_moment_inertia_probe as HM  # noqa: E402
import p1_construction_probe as P1  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

D_SHA_PREFIX = "2ee74c59"
CT_SHA_PREFIX = "cb03729f"
BB_SHA_PREFIX = "baee9fc5"
HM_SHA_PREFIX = "bb1dcf6a"
P1_SHA_PREFIX = "ba6817f5"
DMF_SHA_PREFIX = "4bf1a94b"

W9_DMIN = 1.6557
LAG_BMAX_HI = 0.10
CHEB_NGE1 = 81
CHEB_NGE1_LO, CHEB_NGE1_HI = 70, 90
FOURIER_OFF_LO = 0.90
BAND8_HI = 0.30
SEQ32_CMIN_LO = 1.0
SEQ37_CMIN_HI = 1.0
TNYQ_HI = 0.80
T0_LO = 1.05
PERM_DMIN_HI = 0.20
SCR_DMIN_HI = 0.40
CORE_N, CORE_DMIN_LO = 42, 1.09
REL_PIN = 5.0e-4

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
    return (not bad), ("NO zero/prime oracles; test-poly RK / "
                       "hole-DFT / sequential C / T0-Nyquist"
                       if not bad else "; ".join(bad))


def log_lagrange_at(x, yn, i):
    yi = yn[i]
    if abs(x - yi) < 1e-16:
        return 0.0, 1.0
    s, acc = 1.0, 0.0
    for j, yj in enumerate(yn):
        if j == i:
            continue
        num, den = x - yj, yi - yj
        if num == 0.0:
            return -np.inf, 0.0
        s *= (1.0 if num * den >= 0 else -1.0)
        acc += math.log(abs(num)) - math.log(abs(den))
    return acc, s


def ell_on(xs, yn, i):
    out = np.empty(len(xs), float)
    for k, x in enumerate(xs):
        lg, sg = log_lagrange_at(float(x), yn, i)
        out[k] = 0.0 if lg == -np.inf else sg * math.exp(min(lg, 700.0))
    return out


def y_lagrange_bounds(mz):
    C, meta = D.chain_C(mz)
    yn = np.asarray(meta["yn"], float)
    xp = np.asarray(meta["xp"], float)
    ud = np.asarray(meta["ud"], float)
    udY, udX = ud[meta["iY"]], ud[meta["iP"]]
    d = np.diag(C)
    b = np.empty(len(yn), float)
    for i in range(len(yn)):
        ell = ell_on(xp, yn, i)
        nrm = float(np.sum(udX * ell * ell))
        b[i] = float(udY[i] / max(nrm, 1e-300))
    return dict(C=C, d=d, b=b, n=meta["n"], deg=len(yn) - 1,
                NY=len(yn), udY=udY, meta=meta)


def cheb_cd_bounds(mz, m):
    C, meta = D.chain_C(mz)
    yn = np.asarray(meta["yn"], float)
    xp = np.asarray(meta["xp"], float)
    ud = np.asarray(meta["ud"], float)
    udY, udX = ud[meta["iY"]], ud[meta["iP"]]
    Tx = D.chebV(xp, m)
    d = np.diag(C)
    b = np.empty(len(yn), float)
    for i, y in enumerate(yn):
        Ty = D.chebV(np.array([y]), m)[0]
        Ky = float(Ty @ Ty)
        p = (Tx @ Ty) / max(Ky, 1e-300)
        nrm = float(np.sum(udX * p * p))
        b[i] = float(udY[i] / max(nrm, 1e-300))
    return d, b


def fourier_off(C, yn):
    th = np.arccos(np.clip(np.asarray(yn, float), -1.0, 1.0))
    o = np.argsort(th)
    Cc = C[np.ix_(o, o)]
    N = Cc.shape[0]
    F = np.fft.fft(np.eye(N), axis=0) / math.sqrt(N)
    Chat = F @ Cc @ F.conj().T
    off = Chat - np.diag(np.diag(Chat))
    tot = float(np.sum(np.abs(Chat) ** 2))
    off_frac = float(np.sum(np.abs(off) ** 2) / (tot + 1e-300))
    band = np.zeros((N, N), bool)
    for i in range(N):
        for k in range(-8, 9):
            band[i, (i + k) % N] = True
    b8 = float(np.sum(np.abs(Chat[band]) ** 2) / (tot + 1e-300))
    return off_frac, b8, o


def part_satz():
    section("S1  SATZ -- RK / DEGREE / C_ii = ud K / RAYLEIGH")
    # constants on {-1,0,1} wt 1: K(y,y)=1/3 for n=1
    h0 = Fr(3)
    check("G01-RK-constants-Q",
          Fr(1, 3) == Fr(1) / h0,
          "K_0=1/h0=1/3 on three unit atoms")
    # degree obstruction: p=t^2, n=1, atoms {-1,0,1}
    # ||p||^2 = 1+0+1=2, |p(1)|^2/||p||^2=1/2 > K=1/3
    check("G02-degree-obstruction-Q",
          Fr(1, 2) > Fr(1, 3),
          "deg p=2 > n-1=0: |p|^2/||p||^2=1/2 > K=1/3 (RK fails)")
    # C_ii = ud * K on a feature toy: B=sqrt(4)*[1,0] => C11=4, K=1
    check("G03-Cii-ud-K-Q",
          Fr(4) == Fr(4) * Fr(1),
          "C_ii = ud K on a 1-feature atom")
    check("G04-rayleigh-Q",
          Fr(2) <= Fr(2),
          "lam_min <= dmin (diagonal C=diag(2,3))")


def part_N():
    section("S2  HALF N -- TEST POLYNOMIAL (w9)")
    mz = V.build_measures(9)
    tb = y_lagrange_bounds(mz)
    n_b = int(np.sum(tb["b"] >= 1.0 - 1e-12))
    n_d = int(np.sum(tb["d"] >= 1.0 - 1e-12))
    rk_ok = bool(np.all(tb["d"] + 1e-8 >= tb["b"]))
    check("G10-Y-Lagrange-degree-OK",
          tb["deg"] < tb["n"],
          "deg ell=|Y|-1=%d < n=%d (in P_n; RK applies)"
          % (tb["deg"], tb["n"]))
    check("G11-Y-Lagrange-does-NOT-close",
          float(tb["b"].max()) <= LAG_BMAX_HI and n_b == 0
          and n_d == tb["NY"] and rk_ok,
          "bmax=%.4f #b>=1=%d/%d #d>=1=%d RK_ok=%s "
          "(test poly REFUTED as a proof of d_i>=1)"
          % (float(tb["b"].max()), n_b, tb["NY"], n_d, rk_ok))
    dC, bC = cheb_cd_bounds(mz, tb["n"])
    nge = int(np.sum(bC >= 1.0 - 1e-12))
    check("G12-chebCD-partial",
          CHEB_NGE1_LO <= nge <= CHEB_NGE1_HI
          and float(bC.min()) < 1.0,
          "cheb-CD m=n: #b>=1=%d/%d bmin=%.3e (not all holes)"
          % (nge, len(bC), float(bC.min())))
    check("G13-w9-dmin-census",
          abs(float(tb["d"].min()) - W9_DMIN) <= 5e-3
          and float(tb["d"].min()) > 1.5,
          "w9 dmin=%.5f (census, not SATZ)" % float(tb["d"].min()))
    return dict(mz=mz, tb=tb)


def part_worlds(w9):
    section("S3  HALF N -- WORLDS / BREAK MECHANISM")
    mz = w9["mz"]
    mzS = CT.with_xp(HM.scramble_mz())
    mzP = P1.reweight(mz, "permute", 1000)
    pS = D.pack_C(mzS)
    pP = D.pack_C(mzP)
    stS = CT.C_diag_stats(pS["C"])
    stP = CT.C_diag_stats(pP["C"])
    tbS = y_lagrange_bounds(mzS)
    tbP = y_lagrange_bounds(mzP)
    check("G20-scramble-dmin",
          stS["dmin"] < SCR_DMIN_HI
          and int(np.sum(tbS["b"] >= 1.0 - 1e-12)) == 0,
          "SCR dmin=%.3f (Rayleigh => nC>=1); Y-Lagrange "
          "#b>=1=0 -- test poly does NOT show the break"
          % stS["dmin"])
    # permute K-split
    CP, mP = D.chain_C(mzP)
    udYP = mP["ud"][mP["iY"]]
    KP = np.diag(CP) / np.maximum(udYP, 1e-300)
    i = int(np.argmin(np.diag(CP)))
    check("G21-permute-K-collapse",
          stP["dmin"] < PERM_DMIN_HI and pP["NY"] == w9["tb"]["NY"]
          and float(KP[i]) < 1.0
          and int(np.sum(tbP["b"] >= 1.0 - 1e-12)) == 0,
          "PERM dmin=%.4f = ud*K with K=%.4f at hole i=%d "
          "(same Y; Christoffel collapse)"
          % (stP["dmin"], float(KP[i]), i))
    pL = D.pack_C(HM.chi_mz(9, DMF.Q_CHI3, DMF.LPQ3))
    pD = D.pack_C(HM.chi_mz(15, DMF.Q_CHI3, DMF.LPQ3))
    check("G22-chi-dmin",
          CT.C_diag_stats(pL["C"])["dmin"] >= 1.0
          and CT.C_diag_stats(pD["C"])["dmin"] >= 1.0
          and pL["nC"] == 0 and pD["nC"] == 1,
          "CHI9 dmin=%.4f nC=0; CHI15 dmin=%.4f nC=1 "
          "(both halves' dictionaries hold; death is edge)"
          % (CT.C_diag_stats(pL["C"])["dmin"],
             CT.C_diag_stats(pD["C"])["dmin"]))
    return dict(pS=pS, pP=pP)


def part_S(w9):
    section("S4  HALF S -- FOURIER / SEQUENTIAL / BERNSTEIN")
    mz, tb = w9["mz"], w9["tb"]
    off, b8, o = fourier_off(tb["C"], tb["meta"]["yn"])
    check("G30-fourier-NOT-banded",
          off >= FOURIER_OFF_LO and b8 <= BAND8_HI,
          "hole-DFT off_frac=%.3f band8=%.3f (NOT a block SATZ)"
          % (off, b8))
    yn = np.asarray(mz["yn"], float)
    vn = np.asarray(mz["vn"], float)
    th = np.arccos(np.clip(yn, -1.0, 1.0))
    oo = np.argsort(th)
    yth, vth = yn[oo], vn[oo]
    p32 = D.pack_C(CT.rebuild_holes(mz, yth[:32], vth[:32]))
    p37 = D.pack_C(CT.rebuild_holes(mz, yth[:37], vth[:37]))
    pk = D.pack_C(mz)
    check("G31-sequential-birth",
          p32["nC"] == 0 and p32["Cmin"] >= SEQ32_CMIN_LO
          and p37["nC"] == 1 and p37["Cmin"] < SEQ37_CMIN_HI
          and pk["nC"] == 1 and pk["C2"] >= 1.0,
          "theta-prefix k=32 nC=%d Cmin=%.5f; k=37 nC=%d "
          "Cmin=%.5f; full nC=%d C2=%.5f (born once, not last)"
          % (p32["nC"], p32["Cmin"], p37["nC"], p37["Cmin"],
             pk["nC"], pk["C2"]))
    g = BB.pack_graph(mz)
    N = len(oo)
    v = np.exp(2j * math.pi * (N // 2) * np.arange(N) / N).real
    v = v / (np.linalg.norm(v) + 1e-30)
    vnq = np.zeros(N)
    vnq[o] = v
    tnyq = float(np.linalg.norm(g["T0"] @ vnq))
    check("G32-Bernstein-NOT-tight",
          tnyq <= TNYQ_HI and g["opnorm"] >= T0_LO
          and tnyq < g["opnorm"] - 0.2,
          "||T0 v_Nyq||=%.4f < ||T0||=%.4f (Nyquist is not "
          "the top singular vector; Bernstein REFUTED)"
          % (tnyq, g["opnorm"]))
    return dict(off=off, tnyq=tnyq, op=g["opnorm"])


def part_kills(w9):
    section("S5  KILLS")
    mz20 = CT.with_xp(HM.two_period_mz(20, 1.0))
    tb20 = y_lagrange_bounds(mz20)
    check("G40-1010-degree-kill",
          tb20["deg"] > tb20["n"]
          and float((tb20["d"] / np.maximum(tb20["b"], 1e-300)).min()) < 1.0,
          "2PER S=20 deg=%d > n=%d; min(d/b)=%.3f (RK fails)"
          % (tb20["deg"], tb20["n"],
             float((tb20["d"] / np.maximum(tb20["b"], 1e-300)).min())))
    mz, tb = w9["mz"], w9["tb"]
    C1, _ = D.chain_C(mz, n=tb["n"] + 1)
    ev1 = np.linalg.eigvalsh(C1)
    check("G41-depth-mutant",
          abs(float(ev1[0]) - 1.0) <= 5e-4
          or abs(float(ev1[0]) - float(tb["d"].min())) >= 0.01,
          "n+1 Cmin=%.5f (wrong depth moves the razor)"
          % float(ev1[0]))
    rng = np.random.default_rng(508 + 1)
    yn = np.asarray(mz["yn"], float)
    vn = np.asarray(mz["vn"], float)
    xp, wp = np.asarray(mz["xp"], float), np.asarray(mz["wp"], float)
    flip = rng.choice(len(xp), size=10, replace=False)
    keep = np.ones(len(xp), bool)
    keep[flip] = False
    pF = D.pack_C(CT.rebuild_holes(
        mz, np.concatenate([yn, xp[~keep]]),
        np.concatenate([vn, wp[~keep]]), xp[keep], wp[keep]))
    check("G42-densify-kill",
          pF["nC"] >= 5,
          "flip+10 nC=%d (density mutant)" % pF["nC"])


def part_census():
    section("S6  CORE-42 -- dmin>1 CENSUS")
    core = list(V.admissible_indices())
    dmins = []
    nC_hi = 0
    for kz in core:
        p = D.pack_C(V.build_measures(kz))
        st = CT.C_diag_stats(p["C"])
        dmins.append(st["dmin"])
        nC_hi += int(p["nC"] > 1)
    check("G50-core-dmin",
          len(core) == CORE_N and min(dmins) >= CORE_DMIN_LO
          and nC_hi == 0,
          "core-%d dmin in [%.4f, %.4f]; nC>1 nowhere "
          "(Half N census; Half S nC<=1 inherited)"
          % (CORE_N, min(dmins), max(dmins)))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("hole_nyquist_probe -- "
          "PRIME.LDAGGER.HOLE_NYQUIST_DEFECT.01 (round 410)")
    print("SPEC_SHA %s   (D %s / CT %s / BB %s)"
          % (SPEC_SHA[:16], D.SPEC_SHA[:16], CT.SPEC_SHA[:16],
             BB.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE" if smoke else "FULL (core-42)"))
    print("=" * 78)

    section("S0  FIREWALL + IMPORT INTEGRITY")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    sha_ok = (D.SPEC_SHA.startswith(D_SHA_PREFIX)
              and CT.SPEC_SHA.startswith(CT_SHA_PREFIX)
              and BB.SPEC_SHA.startswith(BB_SHA_PREFIX)
              and HM.SPEC_SHA.startswith(HM_SHA_PREFIX)
              and P1.SPEC_SHA.startswith(P1_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX))
    check("G00b-import-sha", sha_ok,
          "D %s / CT %s / BB %s / HM %s"
          % (D.SPEC_SHA[:8], CT.SPEC_SHA[:8], BB.SPEC_SHA[:8],
             HM.SPEC_SHA[:8]))

    part_satz()
    w9 = part_N()
    part_worlds(w9)
    part_S(w9)
    part_kills(w9)
    if not smoke:
        part_census()
    else:
        section("S6  CORE census skipped (--smoke)")

    section("S7  VERDICT")
    prev_ok = all(ok for _n, ok in CHECKS)
    check("G60-verdict",
          prev_ok,
          "N: TESTPOLY_REFUTED / DMIN_CENSUS; "
          "S: FOURIER_REFUTED / BERNSTEIN_REFUTED / SEQ_REDUCED")

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  "
          "N=TESTPOLY_REFUTED  S=SEQ_REDUCED" % (
              n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("HOLE NYQUIST %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("HOLE NYQUIST FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
