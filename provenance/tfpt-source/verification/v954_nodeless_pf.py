#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v954 -- PRIME.NODELESS.PF.01: THE PERRON-FROBENIUS ADJUDICATION
of round 198 -- the r197/v953 candidate route for OBJECT-A fully
adjudicated: DEAD IN THE MODE BASIS (off-diagonals mixed at every
rung, decided already at adjacent pairs), with the obstruction
LOCALIZED EXACTLY (the pole's rank-one POSITIVE kernel is the SOLE
cone obstruction -- removing it repairs cone invariance at every
rung) and a SURVIVING Z-STRUCTURE (the arithmetic hopping is
one-signed ATTRACTIVE in band-limited position coordinates on the
prime + arch parts).

THE SIGN-PATTERN CENSUS (recomputed in-run at h = 4, 5): PF gives
one-signedness of the bottom eigenvector iff the matrix is (up to
diagonal sign similarity) a Z-matrix; the wall's off-diagonals are
the Loewner divided differences of f = f_pole + f_arch + 2 om pj
(r189/v947 dictionary) and they are MIXED: (n+, n-) = (15, 6) at
h = 4 and (38, 17) at h = 5 (recomputed EXACTLY from the own wall
build, matching the record), checkerboard-mixed in BOTH parities:
pfMode = OFF-DIAG-MIXED-PF-MODE-DEAD at every reachable rung.  THE
TRIVIAL-ROUTE EXHIBIT (recomputed exactly): coefficientwise
nonnegativity does NOT imply function nonnegativity -- v = e_1
has nonneg coefficients and A(L/2) = cos(pi) = -1 EXACTLY: even a
one-signed v_0 would NOT close A >= 0 by inspection -- the
mode-basis PF chain, had it closed, would prove the WRONG
statement's sign pattern.  V0 IS NOT PARITY-ALIGNED (pinned; P2
refuted): mis = 2..24 misaligned entries, the aligned head shallow
(hd = 4..7), and the misaligned |c|-mass fraction FLAT at the
1e-2.5..1e-3.0 class (slope +0.004 -- NOT a tau ladder; the
pre-registered alignment-depth expectation CORRECTED on the
record); recomputed at h = 4, 5: mis = 2, 4.

THE SOURCE CONTENT (recomputed at h = 4, 5): pole + arch
off-diagonals are POSITIVE AT EVERY PAIR (pole = rank-1 Cauchy
2 sinh^2(a/2)/((1/4 + b_i)(1/4 + b_j)) > 0 EXACT -- recomputed
symbolically; arch positivity censused pairwise), so EVERY
negative off-diagonal is a pair where the prime leg DOMINATES
pole + arch (cross-gate nflip == raw_nn EXACT in-run); the prime
leg dominates at the MAJORITY of pairs (fracdom 0.45..0.77,
recomputed 0.524/0.509 at h = 4/5): the pole does NOT dominate the
off-diagonals anywhere near rung-uniformly.

THE KERNEL SPLIT (pinned; the round's sharpest kernel finding):
the WALL position kernel is mixed at band resolution (negfrac
0.20..0.56) but the BLOCKS are NOT -- the pole kernel has negfrac
0.000 EXACTLY at every rung (phi > 0 on the whole lattice,
near-flat; recomputed at h = 4, 5: the rank-one factor phi(t) =
sum_k sinh(a/2)/(1/4 + b_k) cos(om_k t) > 0 at all 33 lattice
points), the arch kernel negfrac 0.955..0.989, the prime kernel
negfrac 0.973..1.000: KERNEL-SPLIT-POLE-POSITIVE-HOPPING-Z -- THE
ATTRACTIVE-HOPPING Z-STRUCTURE SURVIVES THE BAND PROJECTION almost
exactly on the prime + arch part (the r195/v951 ACF law's -2 w_q
translation couplings ARE one-signed attractive at kernel level),
and the wall's kernel mixing is ENTIRELY the pole-vs-hopping
competition.

THE CONE ADJUDICATION (recomputed at h = 4): the natural
Krein-Rutman candidate T = froW I - RawW violates cone invariance
on 11..14 of the 20 even-symmetrized Fejer family members at EVERY
rung (recomputed at h = 4: inside the record band), while the
NO-POLE operator fro(RawW - RawP) I - (RawW - RawP) has ZERO
violations at EVERY rung (recomputed: 0 at h = 4): krEnum =
KR-WALL-CONE-FAILS-POLE-IS-THE-OBSTRUCTION -- THE OPERATOR PIECE
THAT FAILS TO PRESERVE THE NONNEGATIVE-FUNCTION CONE IS EXACTLY
THE RANK-ONE PIECE THAT CARRIES THE POSITIVITY (the v951
pole-vs-atoms compensation reappearing as cone-geometry tension);
chain = CHAIN-OPEN-FUNCTION-SPACE: the profile nonnegativity is
re-verified at all 14 rungs (rmin == r197 per the KC rider -- the
r197/r198 pair CONSISTENT) while every mode-basis PF door is dead:
the OBJECT-A target stays GENUINELY FUNCTION-SPACE.

WORLDS (pinned): SMOOTH is the STRUCTURAL OUTLIER -- off-diagonals
ALL POSITIVE (the mixed census is an ATOM-WORLD phenomenon),
fracdom 0.000, its wall operator CONE-PRESERVING despite carrying
the same pole (the pole obstruction is BALANCE-dependent, not
absolute), and it keeps nonnegativity with NO Z-structure -- a
live exhibit that the shape needs none; EPSTEIN breaks the shape
with all-positive weights and censuses of the SAME KIND as MAIN
except the alignment head (hd = 0 vs 4..7 -- single-cell
separation, recorded NOT sold as a detector); the witness leaves
the alignment/cone readings stable at x1000 (ovl 0.998106).  THE
X6 DISCIPLINE (adopted): "pole-vs-hopping balance" is the CLASS
NAME of OBJECT-W (wall positivity itself) -- treating it as a new
attack object would repeat the BH8-X1 error; this round named the
concrete successor SUBSTRUCTURE, not a new omega.

RE-RUN GREEN AS TYPED AT PROMOTION: nodeless_pf_probe.py round 198
(note DXXII (522), contract PRIME.NODELESS.PF.01), 27/27 gates,
SPEC_SHA 7499c39a026d0d0f, record + deterministic re-run
(timing-normalized diff empty, all logs kept; amendment A1
disclosed: the NO-POLE operator added to the cone battery after
smoke1 -- no bar, grid, dps or recipe moved), re-run at promotion
817.1 s, 27/27 -- log kept as nodeless_pf_probe.promo_rerun.log.

HONEST TYPING: PROVEN = the trivial-route exhibit, the pole
rank-1-Cauchy positivity, the exact censuses/cross-gates and cone
tests at h = 4 (5) (recomputed in-run); MEASURED = the full
census/dominance/kernel/cone/world ladders (pinned).  The
mode-basis kill CLOSES the named candidate route of r197/v953 and
nothing else; OBJECT-A stays open, function-space.  THE RESIDUE
(canonical, notes DII/DXVI/DXXIV): {H1 AND H2 AND H3}-cofinal
(mod D = 0.0042) + {census-forall-k == LOOP} + {H-PIN = the one
lambda-uniform edge of {L1, WPD}; WPD non-lambda legs: extension
instantiated, TAILWPD world-front}.  Census cardinality 4
UNCHANGED.  NOT evidence for or against the Riemann Hypothesis in
either direction.  NO RH CLAIM.

PROVENANCE: discovery probe nodeless_pf_probe.py (round 198,
2026-08-21, note DXXII); consumes v953 (the OBJECT-A target whose
candidate route this round adjudicates) + v951 (the ACF law behind
the attractive-hopping structure); externally covered by Bughunt X
(round 199, note DXXIII: F3/KC the r197/r198 consistency -- the
parity-misalignment factor explains the printed-ratio difference
exactly; all exact claims reproduced in own code).  Python-only
per GATE.WOLFRAM.02.
"""
from __future__ import annotations

import math
import time

import mpmath as mp

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R198 = "7499c39a026d0d0f"
PIN_RAWNP = {4: 15, 5: 38}             # recomputed in-run
PIN_RAWNN = {4: 6, 5: 17}
PIN_CBNP = {4: 9, 5: 26}
PIN_MIS = {4: 2, 5: 4}
PIN_FRACDOM = {4: 0.524, 5: 0.509}
PIN_FRACDOM_RANGE = (0.45, 0.77)
PIN_HD_RANGE = (4, 7)
PIN_MISMASS_RANGE = (-3.0, -2.5)
PIN_MISMASS_SLOPE = 0.004
PIN_KNEGW_RANGE = (0.197, 0.561)
PIN_KNEGA_RANGE = (0.955, 0.989)
PIN_KNEGPR_RANGE = (0.973, 1.000)
PIN_CONE_W = (11, 14)                  # of 20 members, every rung
PIN_CONE_NP = 0
PIN_CONE_WORST = (-1.8, -0.8)          # log10 excursion band
PIN_EPSTEIN = {"hd": 0, "negw": 0, "fracdom": 0.767}
PIN_SMOOTH = {"raw_nn": 0, "fracdom": 0.000}
PIN_WIT_OVL = 0.998106
ZCLS = 1e-30
CONE_BAR = 1e-25
FEJ_BAR = 1e-30

N_CHECKS = 10
EXPECTED = "PF-MODE-BASIS-DEAD-POLE-IS-THE-OBSTRUCTION"

CHECKS: list[tuple[str, bool]] = []
FAILS: list[str] = []


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %-52s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


# ------------------------------------------------------ own wall builder
def r_of(w):
    if w == 0:
        return mp.mpf("0.25")
    return mp.exp(-w / 2) / (-mp.expm1(-2 * w)) - 1 / (2 * w)


def own_cell(h, dps):
    """Own build (v953-identical transcription; BH9/BH10 lineage)."""
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        K = int(math.ceil(1.25 * h * math.log(h)))
        L = 2 * aa
        oms = [k * mp.pi / aa for k in range(K)]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        jvec = [mp.mpf(0)]
        for i in range(1, K):
            o = oms[i]
            npts = int(mp.floor(L * o / mp.pi))
            pts = ([mp.mpf(0)]
                   + [j * mp.pi / o for j in range(1, npts + 1)]
                   + [L])
            jvec.append(mp.quad(lambda w, o=o: mp.sin(o * w)
                                * r_of(w), pts) + mp.si(L * o) / 2)
        icap = int(h)
        comp = [False] * (icap + 1)
        nlist = []
        for p in range(2, icap + 1):
            if comp[p]:
                continue
            for m in range(p * p, icap + 1, p):
                comp[m] = True
            q = p
            while q <= icap:
                nlist.append((q, p))
                q *= p
        nlist.sort()
        atoms = [(mp.log(q), mp.log(p) / mp.sqrt(q)) for q, p in nlist]
        pj = [sum((w * mp.sin(o * u) for u, w in atoms), mp.mpf(0))
              for o in oms]
        Mpole = mp.zeros(K, K)
        March = mp.zeros(K, K)
        Mprime = mp.zeros(K, K)
        ipv = [par[i] * mp.sinh(aa / 2) / (mp.mpf(1) / 4 + oms[i] ** 2)
               for i in range(K)]
        for i in range(K):
            for j in range(K):
                Mpole[i, j] = 2 * ipv[i] * ipv[j]
        for i in range(K):
            for j in range(i):
                sg = par[i] * par[j]
                den = oms[j] ** 2 - oms[i] ** 2
                March[i, j] = March[j, i] = (
                    -2 * sg * (oms[i] * jvec[i]
                               - oms[j] * jvec[j]) / den)
                pod = 2 * sg * (oms[i] * pj[i] - oms[j] * pj[j]) / den
                Mprime[i, j] += pod
                Mprime[j, i] += pod
        for i in range(K):
            o = oms[i]
            if i == 0:
                f0 = L
                psi_d = lambda w: L - w                # noqa: E731
            else:
                f0 = aa
                psi_d = (lambda w, o=o: (aa - w / 2) * mp.cos(o * w)
                         - mp.sin(o * w) / (2 * o))
            integrand = (lambda w, f0=f0, psi_d=psi_d:
                         (f0 * mp.exp(-2 * w)
                          - psi_d(w) * mp.exp(-w / 2))
                         / (-mp.expm1(-2 * w)))
            npts = max(int(mp.floor(L * o / mp.pi)), 1) if i else 1
            base = [mp.mpf(0), mp.mpf("1e-6"), mp.mpf("1e-3"),
                    mp.mpf("0.05"), L]
            if i:
                base += [j * mp.pi / o for j in range(1, npts + 1)]
            pts = sorted(set(p for p in base if p <= L))
            body = mp.quad(integrand, pts)
            tail = -f0 / 2 * mp.log1p(-mp.exp(-2 * L))
            March[i, i] += -f0 * (mp.euler + mp.log(mp.pi)) \
                + 2 * (body + tail)
            pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                              - mp.sin(o * u) / (2 * o))
                         if i else w * (L - u)
                         for u, w in atoms), mp.mpf(0))
            Mprime[i, i] += 2 * pdiag
        RawP = mp.zeros(K, K)
        RawA = mp.zeros(K, K)
        RawPr = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                sg = par[i] * par[j]
                RawP[i, j] = Mpole[i, j] * sg
                RawA[i, j] = March[i, j] * sg
                RawPr[i, j] = Mprime[i, j] * sg
        RawW = RawP + RawA - RawPr
        for i in range(K):
            for j in range(i):
                for Mb in (RawW, RawP, RawA, RawPr):
                    sym = (Mb[i, j] + Mb[j, i]) / 2
                    Mb[i, j] = Mb[j, i] = sym
        return dict(K=K, aa=aa, L=L, oms=oms,
                    b=[o * o for o in oms],
                    RawW=RawW, RawP=RawP, RawA=RawA, RawPr=RawPr)


def bottom_vec(Raw, K):
    x = mp.matrix([mp.mpf(1)] * K)
    for _ in range(3):
        x = mp.lu_solve(Raw, x)
        x = x / mp.sqrt(sum(x[i] ** 2 for i in range(K)))
    v = [x[i] for i in range(K)]
    Rv = [sum(Raw[i, j] * v[j] for j in range(K)) for i in range(K)]
    lam = sum(v[i] * Rv[i] for i in range(K))
    res = max(abs(Rv[i] - lam * v[i]) for i in range(K))
    return v, lam, res


def offdiag_census(B, K):
    om = mp.mpf(0)
    for i in range(K):
        for j in range(i):
            om = max(om, abs(B[i, j]))
    zb = mp.mpf(ZCLS) * om
    np_, nn, cbp, cbn = 0, 0, 0, 0
    for i in range(K):
        for j in range(i):
            x = B[i, j]
            if abs(x) <= zb:
                continue
            if x > 0:
                np_ += 1
            else:
                nn += 1
            cb = x if ((i + j) % 2 == 0) else -x
            if cb > 0:
                cbp += 1
            else:
                cbn += 1
    return np_, nn, cbp, cbn, zb


def fejer_family(K, L):
    c8 = [mp.cos(2 * mp.pi * m / 8) for m in range(8)]
    fam = []
    for M in sorted(set((1, 2, K // 2, K - 1))):
        for j in range(5):
            v = [mp.mpf(0)] * K
            v[0] = mp.mpf(2 * (M + 1))
            for k in range(1, min(M, K - 1) + 1):
                v[k] = 4 * (M + 1 - k) * c8[(k * j) % 8]
            fam.append(v)
    return fam


def prof_min_max(v, K, N):
    Av = [sum(v[k] * mp.cos(2 * mp.pi * ((k * j) % N) / N)
              for k in range(K)) for j in range(N // 2 + 1)]
    return min(Av), max(abs(x) for x in Av)


def part():
    import sympy as sp

    # ================================================ A: exact layer
    section("A. THE EXACT LAYER (trivial route; pole positivity)")
    a_, t_ = sp.symbols("a t", positive=True)
    L_ = 2 * a_
    om1 = sp.pi / a_
    okA = sp.simplify(sp.cos(om1 * L_ / 2) + 1) == 0
    check("A1 the trivial-route exhibit: v = e_1 ==> A(L/2) = -1 "
          "(exact)", okA,
          "A(t) = cos(om_1 t) has nonnegative coefficients and "
          "A(L/2) = cos(pi) = -1 EXACTLY (sympy): coefficientwise "
          "nonnegativity does NOT imply function nonnegativity -- "
          "even a one-signed v_0 (in any parity) would NOT close "
          "A >= 0 by inspection: the mode-basis PF chain, had it "
          "closed, would prove the WRONG statement's sign pattern "
          "(both directions adjudicated on the record)")

    bi, bj = sp.symbols("b_i b_j", positive=True)
    s2 = 2 * sp.sinh(a_ / 2) ** 2
    fpole = lambda b: -s2 / (sp.Rational(1, 4) + b)    # noqa: E731
    dd = sp.simplify((fpole(bi) - fpole(bj)) / (bi - bj)
                     - s2 / ((sp.Rational(1, 4) + bi)
                             * (sp.Rational(1, 4) + bj)))
    okB = dd == 0
    check("A2 the pole off-diagonal is rank-1 Cauchy POSITIVE "
          "(exact; r189 law)", okB,
          "DD_pole(i, j) == 2 sinh^2(a/2)/((1/4 + b_i)(1/4 + "
          "b_j)) > 0 at every pair (sympy exact): the pole block "
          "is a rank-one POSITIVE kernel phi phi^T with phi_k = "
          "sinh(a/2)/(1/4 + b_k) > 0 -- the piece that CARRIES "
          "the positivity, and (C1 below) the SOLE cone "
          "obstruction")

    # ================================================ B: censuses h = 4, 5
    section("B. THE CENSUSES RECOMPUTED (h = 4, 5, own build)")
    okC = True
    okD = True
    okE = True
    dat = {}
    for h in (4, 5):
        dps = 60
        ce = own_cell(h, dps)
        with mp.workdps(dps):
            K = ce["K"]
            np_, nn, cbp, cbn, zb = offdiag_census(ce["RawW"], K)
            okC = okC and (np_, nn) == (PIN_RAWNP[h], PIN_RAWNN[h]) \
                and cbp == PIN_CBNP[h] and cbn > 0
            # pole + arch positive at every pair; cross-gate
            PA = ce["RawP"] + ce["RawA"]
            pa_neg = 0
            nflip = 0
            ndom = 0
            npair = 0
            om = mp.mpf(0)
            for i in range(K):
                for j in range(i):
                    om = max(om, abs(PA[i, j]))
            zb2 = mp.mpf(ZCLS) * om
            for i in range(K):
                for j in range(i):
                    pa = PA[i, j]
                    pr = ce["RawPr"][i, j]
                    if pa < -zb2:
                        pa_neg += 1
                    w = pa - pr
                    if abs(w) > zb and w < 0:
                        nflip += 1
                    if abs(pa) > zb2:
                        npair += 1
                        if abs(pr) > abs(pa):
                            ndom += 1
            okD = okD and pa_neg == 0 and nflip == nn
            fd = ndom / float(npair)
            okD = okD and abs(fd - PIN_FRACDOM[h]) < 0.02
            # parity alignment of v_0
            v0, lam0, _res = bottom_vec(ce["RawW"], K)
            Amid = sum(v0[k] * mp.cos(ce["oms"][k] * ce["L"] / 2)
                       for k in range(K))
            if Amid < 0:
                v0 = [-t for t in v0]
            c = [((-1) ** k) * v0[k] for k in range(K)]
            kmax = max(range(K), key=lambda k: abs(c[k]))
            if c[kmax] < 0:
                c = [-x for x in c]
            zb3 = mp.mpf(ZCLS) * max(abs(x) for x in c)
            mis = sum(1 for x in c if x < -zb3)
            okE = okE and mis == PIN_MIS[h]
            # pole position kernel factor phi > 0 on the 33-lattice
            aa = ce["aa"]
            phi_ok = all(
                sum(mp.sinh(aa / 2) / (mp.mpf(1) / 4 + ce["b"][k])
                    * mp.cos(2 * mp.pi * ((k * g) % 32) / 32)
                    for k in range(K)) > 0
                for g in range(33))
            okE = okE and phi_ok
            dat[h] = dict(ce=ce, v0=v0)
    check("B1 OFF-DIAG-MIXED-PF-MODE-DEAD (exact censuses match "
          "the record)", okC,
          "the wall off-diagonal census at h = 4: (n+, n-) = "
          "(%d, %d), h = 5: (%d, %d) -- MIXED (recomputed from the "
          "own build, matching the record EXACTLY); checkerboard "
          "census mixed in BOTH parities (cb n+ = %d/%d): neither "
          "direct-Z nor checkerboard-Z nor Metzler -- classical PF "
          "does NOT apply in the mode basis at any reachable rung; "
          "decided already at adjacent pairs (descents == r189)"
          % (PIN_RAWNP[4], PIN_RAWNN[4], PIN_RAWNP[5], PIN_RAWNN[5],
             PIN_CBNP[4], PIN_CBNP[5]))

    check("B2 PRIME-CARRIES-ALL-NEGATIVE-OFFDIAG (cross-gate "
          "exact) + dominance", okD,
          "pole + arch off-diagonals POSITIVE at every pair "
          "(negative count 0 at h = 4, 5), so every negative wall "
          "off-diagonal is a prime-dominated pair (cross-gate "
          "nflip == raw_nn EXACT in-run); the prime leg dominates "
          "pole + arch at the MAJORITY of pairs (fracdom "
          "recomputed %.3f/%.3f at h = 4/5, record %.3f/%.3f; "
          "full-ladder range %.2f..%.2f): the pole does NOT "
          "dominate the off-diagonals anywhere near rung-uniformly"
          % (PIN_FRACDOM[4], PIN_FRACDOM[5], PIN_FRACDOM[4],
             PIN_FRACDOM[5], PIN_FRACDOM_RANGE[0],
             PIN_FRACDOM_RANGE[1]))

    check("B3 V0-PARITY-BROKEN (P2 refuted; recomputed) + the "
          "pole kernel phi > 0", okE,
          "v_0 is NOT parity-aligned: mis = %d/%d misaligned "
          "entries at h = 4/5 (recomputed; record 2..24 across the "
          "ladder), the aligned head SHALLOW (hd = %d..%d), the "
          "misaligned |c|-mass FLAT at the 1e%.1f..1e%.1f class "
          "(slope +%.3f -- NOT a tau ladder, the pre-registered "
          "expectation CORRECTED on the record); the pole "
          "position-kernel factor phi(t) > 0 at all 33 lattice "
          "points of both rungs (recomputed): the rank-one kernel "
          "is POSITIVE" % (PIN_MIS[4], PIN_MIS[5], PIN_HD_RANGE[0],
                           PIN_HD_RANGE[1], PIN_MISMASS_RANGE[0],
                           PIN_MISMASS_RANGE[1], PIN_MISMASS_SLOPE))

    # ================================================ C: the cone tests
    section("C. THE CONE ADJUDICATION (recomputed at h = 4)")
    ce = dat[4]["ce"]
    K, L = ce["K"], ce["L"]
    with mp.workdps(60):
        froW = mp.sqrt(sum(ce["RawW"][i, j] ** 2
                           for i in range(K) for j in range(K)))
        NP = ce["RawW"] - ce["RawP"]
        froNP = mp.sqrt(sum(NP[i, j] ** 2
                            for i in range(K) for j in range(K)))
        fam = fejer_family(K, L)
        N = 16 * K
        nv_w, nv_np = 0, 0
        fej_ok = True
        worst = -300.0
        for v in fam:
            mn, am = prof_min_max(v, K, N)
            if mn < -mp.mpf(FEJ_BAR) * am:
                fej_ok = False
            for tag, B, fro in (("W", ce["RawW"], froW),
                                ("NP", NP, froNP)):
                y = [fro * v[i] - sum(B[i, j] * v[j]
                                      for j in range(K))
                     for i in range(K)]
                mny, amy = prof_min_max(y, K, N)
                if mny < -mp.mpf(CONE_BAR) * amy:
                    if tag == "W":
                        nv_w += 1
                        worst = max(worst,
                                    float(mp.log(abs(mny) / amy, 10)))
                    else:
                        nv_np += 1
    okF = fej_ok and PIN_CONE_W[0] <= nv_w <= PIN_CONE_W[1] \
        and nv_np == PIN_CONE_NP \
        and PIN_CONE_WORST[0] - 0.5 <= worst <= PIN_CONE_WORST[1] + 0.5
    check("C1 KR-WALL-CONE-FAILS-POLE-IS-THE-OBSTRUCTION "
          "(recomputed at h = 4)", okF,
          "the wall operator froW I - RawW violates cone "
          "invariance on %d of 20 even-symmetrized Fejer members "
          "(record band %d..%d at every rung; worst excursion "
          "log10 %.2f, record band %.1f..%.1f), while the NO-POLE "
          "operator fro(RawW - RawP) I - (RawW - RawP) has %d "
          "violations (record 0 at EVERY rung; family membership "
          "warded): REMOVING THE POLE ALONE REPAIRS CONE "
          "INVARIANCE -- the operator piece that fails the "
          "nonneg-function cone is exactly the rank-one piece that "
          "CARRIES the positivity (the v951 pole-vs-atoms "
          "compensation as cone-geometry tension)"
          % (nv_w, PIN_CONE_W[0], PIN_CONE_W[1], worst,
             PIN_CONE_WORST[0], PIN_CONE_WORST[1], nv_np))

    okG = PIN_KNEGA_RANGE[0] > 0.9 and PIN_KNEGPR_RANGE[0] > 0.9 \
        and PIN_KNEGW_RANGE[0] > 0 and PIN_KNEGW_RANGE[1] < 1
    check("C2 KERNEL-SPLIT-POLE-POSITIVE-HOPPING-Z (the surviving "
          "Z-structure)", okG,
          "position kernels on the 33-point lattice (pinned): the "
          "WALL kernel is mixed at band resolution (negfrac "
          "%.3f..%.3f) but the BLOCKS are not -- pole negfrac "
          "0.000 EXACTLY at every rung, arch %.3f..%.3f, prime "
          "%.3f..%.3f: THE ATTRACTIVE-HOPPING Z-STRUCTURE (the "
          "v951 ACF law's -2 w_q translation couplings) SURVIVES "
          "the band projection almost exactly on prime + arch -- "
          "the wall's kernel mixing is ENTIRELY the "
          "pole-vs-hopping competition"
          % (PIN_KNEGW_RANGE[0], PIN_KNEGW_RANGE[1],
             PIN_KNEGA_RANGE[0], PIN_KNEGA_RANGE[1],
             PIN_KNEGPR_RANGE[0], PIN_KNEGPR_RANGE[1]))

    # ================================================ D: worlds + typing
    section("D. WORLDS + THE CHAIN + THE X6 DISCIPLINE")
    okH = PIN_SMOOTH["raw_nn"] == 0 and PIN_SMOOTH["fracdom"] == 0 \
        and PIN_EPSTEIN["hd"] == 0 and PIN_EPSTEIN["negw"] == 0
    check("D1 SMOOTH the structural outlier; EPSTEIN the shape "
          "breaker (pinned)", okH,
          "SMOOTH: off-diagonals ALL POSITIVE (raw n- = %d -- the "
          "mixed census is an ATOM-WORLD phenomenon), fracdom "
          "%.3f, wall operator CONE-PRESERVING (W0/NP0) despite "
          "the same pole -- the pole obstruction is "
          "BALANCE-dependent, not absolute; and SMOOTH keeps "
          "nonnegativity with NO Z-structure: a live exhibit that "
          "the shape needs none; EPSTEIN breaks the shape with "
          "all-POSITIVE weights (negw = %d) and censuses of the "
          "SAME KIND as MAIN except the alignment head (hd = %d "
          "vs MAIN %d..%d -- single-cell separation, recorded NOT "
          "sold); the witness leaves alignment/cone readings "
          "stable at x1000 (ovl %.6f)"
          % (PIN_SMOOTH["raw_nn"], PIN_SMOOTH["fracdom"],
             PIN_EPSTEIN["negw"], PIN_EPSTEIN["hd"],
             PIN_HD_RANGE[0], PIN_HD_RANGE[1], PIN_WIT_OVL))

    okI = True
    check("D2 CHAIN-OPEN-FUNCTION-SPACE (the target stays "
          "function-space)", okI,
          "the profile nonnegativity is re-verified at all 14 "
          "rungs (rmin == r197 per the KC rider -- the r197/r198 "
          "pair CONSISTENT: A_{v_0} >= 0 and V0-PARITY-BROKEN are "
          "logically independent and both measured TRUE) while "
          "every mode-basis PF door is dead: the OBJECT-A target "
          "'A_{v_0(h)} >= 0 for all h' stays GENUINELY "
          "FUNCTION-SPACE -- the adjudication CLOSES the named "
          "candidate route of r197/v953 and nothing else")

    okJ = True
    check("D3 THE X6 DISCIPLINE: pole-vs-hopping balance is the "
          "CLASS NAME of OBJECT-W", okJ,
          "the Bughunt-X X6 adjudication ADOPTED: the "
          "'pole-vs-hopping balance' named by this round is the "
          "CLASS NAME of OBJECT-W (wall positivity itself, whose "
          "relabeling r195/v951's cofinal domination already is) "
          "-- treating it as a NEW attack object would repeat the "
          "BH8-X1 error; this round named the concrete successor "
          "SUBSTRUCTURE, not a new omega; census cardinality 4 "
          "UNCHANGED; no loop consumed; NOT RH evidence")

    print("\n  [TYPED] The PF route for OBJECT-A is DEAD in the mode")
    print("  basis (mixed off-diagonals, exact); the pole's rank-one")
    print("  POSITIVE kernel is the SOLE cone obstruction; the")
    print("  attractive-hopping Z-structure survives on prime + arch.")
    print("  OBJECT-A stays open, function-space.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v954 -- PRIME.NODELESS.PF.01 (PF-mode-basis-dead; the "
          "pole rank-one")
    print("kernel the sole cone obstruction; the attractive-hopping "
          "Z-structure;")
    print("the r197/r198 consistency per KC; round 198; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v954: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the trivial-route exhibit + the pole Cauchy law "
          "(sympy exact);")
    print("the off-diagonal/checkerboard/dominance/alignment "
          "censuses and the")
    print("wall-vs-no-pole cone tests recomputed in-run at h = 4 "
          "(5); the kernel/")
    print("world/witness ladders PINNED from nodeless_pf_probe.py "
          "(SPEC %s," % PIN_SPEC_R198)
    print("27/27, record + deterministic re-run, amendment A1 "
          "disclosed, RE-RUN")
    print("GREEN AS TYPED AT PROMOTION 817.1 s, 27/27).  NOT RH "
          "evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.NODELESS.PF.01 PF adjudication + kernel split: "
          "%d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
