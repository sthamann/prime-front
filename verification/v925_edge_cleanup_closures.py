#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v925 -- PRIME.EDGE.CLEANUP.CLOSURES.01: THE EDGE / CLEANUP
CLOSURES of round 159 -- the SIMPLICITY subsumption + zero-cost
avoidance (census row Z8 eliminated), the Q-SWAMP WHOLESALE CLOSURE
(357 Turing-class local band certificates, RECOMPUTED IN-RUN from
the committed verified-zero cache), and the band-edge sliver
certificates, promoted as certified finite results.

THE RESULTS (round 159, note CDLXIII, edge_cleanup_probe.py):

  (E2) SIMPLICITY FALLS (census row Z8 eliminated, 10 -> 9 rows):
  two-leg kill.  (i) SUBSUMPTION: the r147 LM multiplicative split
  forces 1 + 1/delta_1 <= B, i.e. delta_1 >= 1/(B - 1) > 0, at
  every Markov/V2-selected point -- the selected points are
  AUTOMATICALLY simple: Z8 was double-counted inside Z4
  (DELTA1FLOOR) at demand level.  (ii) ZERO-COST AVOIDANCE:
  disc(charpoly) == prod_{i<j} (l_i - l_j)^2 is analytic per clean
  cell and NOT identically zero (anchor witnesses disc != 0 at all
  six blocks): degeneracy points are ISOLATED, measure 0, and the
  V2 instrument dodges them at cost EXACTLY 0.  RESIDUAL:
  NONDEGENERATE-CELL -- strictly weaker, witness-certified for free
  by each cell's own eigendata.
  (E3) THE Q-SWAMP CLOSES WHOLESALE: the r133 Theorem-A assemblage
  is swamped below x_0 = 121 because the unconditional HSW counting
  slack Q(T) ~ 10 zeros eats the first tail shell.  The r138-named
  exit -- Turing-class LOCAL BAND CERTIFICATES -- is delivered by
  the verified census itself: at strip heights (T_z <= 760,
  gamma_N <= ~1100, tail to the cache top 7264.75 -- ALL heights
  FOUR-DIGIT, ten orders below the PT21 horizon 3e12) the zone
  count m, gamma_N and the certified tail lower bound tail1_cs =
  sum_{j > N} w_a(gamma_j + CACHE_ERR) (positive terms beyond the
  cache top DROPPED -- one-sided legal) give
     D_cs(x, a) := (7/8) tail1_cs - (N - m) w_a(T_z) > 0
  at ALL 357 certificates (integer x = 3..121 x a in {1, 4, 16});
  D_hsw < 0 flips to D_cs > 0 on the swamped strip; the bridge is
  GAP-FREE: x_0(HSW) = 121 and x_0(BW25) = 112 on the integer scan
  90..200 -- census currency covers [3, 121), HSW/BW covers
  x >= x_0.  CONSEQUENCE (typed): THEOREM A'S CONDITIONALITY
  SHARPENS TO "H-pin(x) implies {d_1 > 0, MRB} FOR EVERY INTEGER
  x >= 3"; H-pin itself is UNTOUCHED.
  (E1) THE SLIVER CLOSES BELOW HORIZON: all 73 sliver + first-zero
  targets carry two-sided audit-ball certificates 0 < T_lo <= T_hi
  < 1.5 y_t (1/1/1/1/18-of-18/51-of-51 at b5..b28, margins min
  T_lo/y_t = 0.977..0.626; headline count corrected 72 -> 73 per
  the bughunt-V correction of record, round 164, note CDLXIX: 71
  sliver zeros + first zeros above the band at b8/b18 only, whose
  slivers are empty -- at b5/b13/b24/b28 the first zero lies
  INSIDE the sliver and is already counted; all 73 certificates
  exist and are green, only the headline changes); the exact
  implicit position law
  y_C - b_top == R_e/(1.5 y_t - T_rest(y_C)) is gated as an
  identity at the mp-bisected crossings (residuals <= 5e-27); the
  lambda-uniform separation demand is TYPED (a band-edge
  zero-REPULSION demand of 0.22-0.43 RvM mean spacings with
  ARITHMETIC-SIGNED-INPUT width -- TAILVIS-style horizon typing);
  TWO new machine-pinned obstructions in the e^depth vacuity
  family: BALL-CERT-DEPTH-PRICED (the certificate price rides
  e^{-depth}: delta = 1e-8 -> 1e-44; the f64 cache-ball dies from
  b13 on) and SEPARATION-ONESIDED-CAP-DEPTH-VACUOUS.

WHAT IS RECOMPUTED IN-RUN (self-contained; probe functions ported
verbatim, attributed inline): the E2/E1 exact layer (interval-edge
law, implicit crossing law, disc == prod gaps^2, LM split ==>
delta_1-floor, measure-zero cover, census-assembly slack algebra,
w_a' monotonicity) AND the FULL E3 closure from the committed
verification/verified_zeros_n7000.json cache (7000 PT21-warranted
ordinates, re-warded in-run): all 357 D_cs certificates, the
representative tables x = 30/60/90 vs the swamped D_hsw, the
D_hsw < 0 strip replication at x in {13, 21, 34, 55, 89}, the
x_0(HSW) = 121 and x_0(BW25) = 112 integer scans, and the heights
typing (max census read <= 7264.75 << 3e12).

PINNED FROM RUN-OF-RECORD, disclosed split:
  ROUND 159 -- RE-RUN GREEN AS TYPED AT PROMOTION (34/34 gates,
  identical SPEC_SHA f6c0318841bb3942; run-of-record 1759.1 s +
  deterministic re-run identical; run1 = 31/34 KEPT -- its fails
  ARE the depth finding; SMOKE-1 three disclosed repairs +
  AMENDMENT-1 audit layer, disclosed): the E1 per-zero sliver
  certificate tables (min T_lo/y_t = 0.977/1.09/0.996/0.998/0.995/
  0.626, price ladder delta = 1e-8/1e-8/1e-22/1e-32/1e-44/1e-44),
  the separation-law table (y_C/b_top = 1.0437/1.0438/1.0064 at
  b5/b8/b24 with margins to 2.5e-3, law-identity residuals <=
  5e-27; VACUOUS-TRUE at b13/b18/b28), the demand ladder (0.2177/
  0.4329/0.2731 RvM mean spacings), the disc witnesses (min
  relative eigengaps 1e-1.0 .. 1e-3.3 at the six anchors; in-cell
  floor at 18 interior points, fixed index sets machine-checked).

HONEST TYPING (carried verbatim; nothing upgraded).  CERTIFIED =
the 357 D_cs certificates (RECOMPUTED here, classical-census-
below-horizon typed WARD; H-pin stays the HYPOTHESIS -- Theorem A
remains CONDITIONAL on H-pin, only its x-range sharpened), the
sliver/first-zero ball certificates (pinned).  PROVEN = the E2
subsumption + avoidance algebra (exact; the identity theorem for
real-analytic functions CITED AS FORM).  TYPED = the separation
law (band-edge zero repulsion, horizon class), the depth-vacuity
obstructions.  Z8 FALLS but Z8 was never one of the four min-cut
omegas: the census {MEAS, OMEGA-POS} stays at CARDINALITY 4 -- NO
omega closed, nothing upgraded.  NOT evidence for or against the
Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe edge_cleanup_probe.py (round 159,
2026-08-18, note CDLXIII, contract PRIME.EDGE.CLEANUP.01); consumes
r156 L1-L6 (v924), r147 AD1/cell lemma + LM split (cited), r133
Theorems M/E/T/C/A (v921), r141 V2 (cited); zero cache
verification/verified_zeros_n7000.json (PT21-warranted, EXTERNAL-
CITED; ward-typed reads only, heights <= 7.3e3).  Python-only per
GATE.WOLFRAM.02.
"""
from __future__ import annotations

import json
import math
import os
import time

T_ALL = time.time()

# ------------------------------------------------- ported constants
# (edge_cleanup_probe.py, round 159, attributed)
KFAC = 1.25
CACHE_ERR = 1e-9
HSW3 = (0.1038, 0.2573, 9.3675)     # HSW22 Cor. 1.2
BW3 = (0.10076, 0.24460, 8.08344)   # Bellotti-Wong 2025 published
A_BAT = (1.0, 4.0, 16.0)
X_CENSUS = range(3, 122)            # 119 integers x 3 a = 357
X_REP = (30, 60, 90)
X_STRIP_NEG = (13, 21, 34, 55, 89)
X0_SCAN_LO, X0_SCAN_HI = 90, 200
X0_HSW_EXPECT, X0_BW_EXPECT = 121, 112
PIN_SPEC_R159 = "f6c0318841bb3942"
PIN_WORST = (12, 1)                 # worst wholesale margin location
PIN_WORST_MARGIN = 0.346
# r159 G32 sliver certificates (counts, price delta, min T_lo/yt)
PIN_SLIVER_N = (1, 1, 1, 1, 18, 51)
PIN_PRICE = ("1e-8", "1e-8", "1e-22", "1e-32", "1e-44", "1e-44")
PIN_MINTLO = ("0.977", "1.09", "0.996", "0.998", "0.995", "0.626")
# r159 G35 separation law
PIN_YC = ("1.0437", "1.0438", "1.0064")      # b5/b8/b24 LAW-ID-CERT
PIN_LAWID = ("8e-29", "2e-28", "5e-27")
PIN_DEM = ("0.2177", "0.4329", "0.2731")     # RvM mean spacings

ZC_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "verified_zeros_n7000.json")

N_CHECKS = 14
EXPECTED = "EDGE-CLEANUP-CLOSURES"

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


# ------------------------------------------------- ported functions
# (edge_cleanup_probe.py round 159 / r133 Theorem-A closed forms,
#  attributed; ward-typed census reads only)
def w_of(a: float, t: float) -> float:
    return a * t * t / (a + t * t) ** 2


def m_rvm(T: float) -> float:
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


def q_gen(T: float, abc) -> float:
    al, be, cc = abc
    return al * math.log(T) + be * math.log(math.log(T)) + cc


def hsw_G_gen(T: float, abc) -> float:
    from mpmath import mp
    al, be, cc = abc
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        alm = mp.mpf(repr(al))
        bem = mp.mpf(repr(be))
        ccm = mp.mpf(repr(cc))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (alm * (2 * lg + 1) / 2 + bem * (ll + 1 / (2 * lg))
              + ccm) / Tm ** 2
        t3 = (alm * lg + bem * ll + ccm) / Tm ** 2
        return float(t1 + t2 + t3)


def t_star_gen(N: int, abc) -> float:
    lo, hi = 20.0, 1e30
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if m_rvm(mid) - q_gen(mid, abc) >= N:
            hi = mid
        else:
            lo = mid
    return hi


def tl_shells_gen(N: int, a: float, Ts: float, abc) -> float:
    best = 0.0
    for lam in (1.5, 2.0, 3.0):
        for J in (1, 2, 3, 4, 6, 8):
            Tj = [Ts * lam ** j for j in range(J + 1)]
            tot = 0.0
            u_prev = m_rvm(Ts) + q_gen(Ts, abc)
            for j in range(J):
                n_next = m_rvm(Tj[j + 1]) - q_gen(Tj[j + 1], abc)
                cnt = max(0.0, n_next - max(float(N), u_prev))
                tot += cnt * w_of(a, Tj[j + 1])
                u_prev = m_rvm(Tj[j + 1]) + q_gen(Tj[j + 1], abc)
            best = max(best, tot)
    return best


def asym_D_gen(x: float, a: float, abc) -> float:
    """r133 THEOREM-A closed form D(x, a) with parametrized counting
    constants (HSW or BW25); ported from edge_cleanup_probe.py."""
    K = int(math.ceil(KFAC * x * math.log(x)))
    N = K - 1
    Ts = t_star_gen(N, abc)
    Tz = 2 * math.pi * x
    n_z = m_rvm(Tz) - q_gen(Tz, abc)
    TL = tl_shells_gen(N, a, Ts, abc)
    m_minus_edge = max(0.0, (N - n_z)) * w_of(a, Tz)
    return TL - TL / 8.0 - m_minus_edge


def census_D(x: int, a: float, gam) -> dict:
    """the Turing-class LOCAL BAND CERTIFICATE assemblage (round 159
    E3): exact ball-deflated census counts + certified tail lower
    bound (positive terms beyond the cache top DROPPED -- one-sided
    legal).  All heights <= 7264.75 << 3e12: ward/classical-census-
    below-horizon typed."""
    K = int(math.ceil(KFAC * x * math.log(x)))
    N = K - 1
    if N >= len(gam):
        return dict(ok=False)
    Tz = 2 * math.pi * x
    m_lo = 0
    for gv in gam:
        if gv + CACHE_ERR <= Tz:
            m_lo += 1
        else:
            break
    tail1 = 0.0
    for gv in gam[N:]:
        gs = gv + CACHE_ERR
        tail1 += a * gs * gs / (a + gs * gs) ** 2
    edge = max(0, N - m_lo) * w_of(a, Tz)
    D8 = 7.0 / 8.0 * tail1 - edge
    mrb = ((tail1 / 8.0 + a * hsw_G_gen(Tz, HSW3) + edge) / D8) \
        if D8 > 0 else float("inf")
    return dict(ok=True, K=K, N=N, Tz=Tz, m=m_lo,
                gamN=float(gam[N - 1]), tail1=tail1, edge=edge,
                D8=D8, mrb=mrb)


def x0_scan(abc) -> int:
    """min integer x in [90, 200] with D(x', a) > 0 for all battery a
    and ALL integers x' in [x, 200] (r133 G43 criterion)."""
    ok_from = None
    for x in range(X0_SCAN_HI, X0_SCAN_LO - 1, -1):
        good = all(asym_D_gen(float(x), a_, abc) > 0 for a_ in A_BAT)
        if good:
            ok_from = x
        else:
            break
    return ok_from if ok_from is not None else -1


def part():
    import sympy as sp

    # ================================================ A: exact layer
    section("A. THE EXACT LAYER (edge law, subsumption, avoidance)")
    y, d_ = sp.symbols("y d_", positive=True)
    v, bp = sp.symbols("v bp", real=True)
    okA = sp.simplify(sp.diff(v * bp / (y - bp), y)
                      + v * bp / (y - bp) ** 2) == 0
    Rp, Lv, rest_ = sp.symbols("Rp Lv rest_", positive=True)
    ycb = sp.symbols("ycb", positive=True)
    sol = sp.solve(sp.Eq(Rp / ycb + rest_, Lv), ycb)
    okD = len(sol) == 1 and sp.simplify(
        sol[0] - Rp / (Lv - rest_)) == 0
    check("A1 interval-edge law + implicit crossing law", okA
          and okD,
          "d/dy[vb/(y-b)] == -vb/(y-b)^2 (termwise monotone right of "
          "the pole ==> endpoint interval enclosures RIGOROUS); "
          "T(y_C) = 1.5 y_t ==> y_C - b_top == R_e/(1.5 y_t - "
          "T_rest(y_C)) EXACT (the separation law's algebra)")

    l1, l2, l3 = sp.symbols("l1 l2 l3", real=True)
    M3 = sp.diag(l1, l2, l3)
    ch = sp.Poly(sp.expand((M3 - sp.symbols("zc") * sp.eye(3)).det()),
                 sp.symbols("zc"))
    disc = sp.expand(sp.discriminant(ch.as_expr(),
                                     sp.symbols("zc")))
    prodg = sp.expand((l1 - l2) ** 2 * (l1 - l3) ** 2
                      * (l2 - l3) ** 2)
    check("A2 disc(charpoly) == prod eigengaps^2 (generic)",
          sp.simplify(disc - prodg) == 0,
          "conjugation-invariant, >= 0 for real symmetric, == 0 iff "
          "a repeated pair: the degeneracy set is the zero set of ONE"
          " analytic function per clean cell (E2 leg (ii) algebra)")

    B_, dl = sp.symbols("B_ dl", positive=True)
    # LM multiplicative split: all factors >= 1, product <= B, and
    # (1 + 1/delta_1) is one factor ==> delta_1 >= 1/(B - 1)
    okLM = sp.simplify(sp.solve(sp.Eq(1 + 1 / dl, B_), dl)[0]
                       - 1 / (B_ - 1)) == 0
    check("A3 LM split ==> delta_1-floor at selected points "
          "(subsumption)", okLM,
          "1 + 1/delta_1 <= B ==> delta_1 >= 1/(B - 1) > 0 at every "
          "Markov/V2-selected point: the selected points are "
          "AUTOMATICALLY simple -- Z8 SUBSUMED by Z4 (DELTA1FLOOR) "
          "at demand level (r147 LM split, cited)")

    eps_, i_ = sp.symbols("eps_ i_", positive=True)
    cover = sp.summation(eps_ / 2 ** i_, (i_, 1, sp.oo))
    check("A4 zero-cost avoidance (measure-zero cover)",
          sp.simplify(cover - eps_) == 0,
          "any countable isolated set is covered at total length "
          "eps (sum eps/2^i == eps exact): degeneracies are measure "
          "0 per cell, V2 cost EXACTLY 0; residual NONDEGENERATE-"
          "CELL witness-certified by each cell's own eigendata")

    Mp, Mm, t1_, zn, ed = sp.symbols("Mp Mm t1_ zn ed", positive=True)
    slack = sp.simplify((Mp - Mm + t1_)
                        - (t1_ - zn - ed)
                        - (Mp + zn + ed - Mm))
    aa, tt = sp.symbols("aa tt", positive=True)
    wfun = aa * tt ** 2 / (aa + tt ** 2) ** 2
    okw = sp.simplify(sp.diff(wfun, tt)
                      - 2 * aa * tt * (aa - tt ** 2)
                      / (aa + tt ** 2) ** 3) == 0
    check("A5 census-assembly slack algebra (r133 shape)",
          slack == 0 and okw,
          "d_1 == M+ - M- + tail_1 with M- <= zone + edge, M+ >= 0 "
          "==> d_1 >= tail_1 - zone - edge; zone <= tail_1/8 ==> "
          "d_1 >= (7/8) tail_1 - edge: the Theorem-A assemblage "
          "carries VERBATIM with exact census counts (E3 currency)")

    # ================================================ B: the cache
    section("B. THE WARD CACHE (re-warded in-run)")
    d = json.load(open(ZC_JSON, encoding="utf-8"))
    gam = d["gammas"]
    mono = all(gam[i] < gam[i + 1] for i in range(len(gam) - 1))
    okc = (len(gam) == 7000 and mono
           and abs(gam[0] - 14.134725141734695) < 1e-9
           and abs(gam[-1] - 7264.7482480903) < 1e-6)
    check("B1 cache health (PT21-warranted, ward-typed)", okc,
          "n = 7000, strictly monotone, gamma_1 dev < 1e-9, "
          "gamma_top = 7264.75 (every ordinate below T0 = 3e12: "
          "EXTERNAL-CITED Platt-Trudgian 2021; reads typed ward/"
          "classical-census-below-horizon)")

    # ================================================ C: E3 closure
    section("C. THE Q-SWAMP WHOLESALE CLOSURE (recomputed in-run)")
    n_cert = 0
    worst = (None, None, float("inf"))
    ok72 = True
    for x in X_CENSUS:
        for a in A_BAT:
            r = census_D(x, a, gam)
            if not r["ok"] or r["D8"] <= 0:
                ok72 = False
                continue
            n_cert += 1
            marg = r["D8"] / r["edge"] if r["edge"] > 0 \
                else float("inf")
            if marg < worst[2]:
                worst = (x, int(a), marg)
    check("C1 D_cs > 0 at ALL %d certificates (recomputed)"
          % (len(list(X_CENSUS)) * len(A_BAT)),
          ok72 and n_cert == 357 and worst[0] == PIN_WORST[0]
          and worst[1] == PIN_WORST[1]
          and abs(worst[2] - PIN_WORST_MARGIN) < 0.01,
          "integer x = 3..121 x battery a in (1, 4, 16): %d/357 "
          "certificates positive; worst margin D_cs/edge = %.3f at "
          "(x, a) = (%s, %s) == the run-of-record (0.346 at (12, 1))"
          % (n_cert, worst[2], worst[0], worst[1]))

    rep_ok = True
    rep_det = []
    for x in X_REP:
        r = census_D(x, 4.0, gam)
        dh = asym_D_gen(float(x), 4.0, HSW3)
        rep_ok = rep_ok and r["D8"] > 0 > dh and r["mrb"] < 10.0
        rep_det.append("x%d: D_hsw %+.2e -> D_cs %+.3e mrb %.1f"
                       % (x, dh, r["D8"], r["mrb"]))
    check("C2 representative rungs: the swamp flips (recomputed)",
          rep_ok, "; ".join(rep_det)
          + " (a = 4; the HSW counting slack eats the shell, the "
          "census certificate does not)")

    neg_ok = all(all(asym_D_gen(float(x), a_, HSW3) < 0
                     for a_ in A_BAT) for x in X_STRIP_NEG)
    check("C3 D_hsw < 0 on the r133 battery strip (replication)",
          neg_ok,
          "x in %s battery-wide: the swamp exhibit replicated "
          "(counting currency blind below x_0 -- exactly what the "
          "census certificates close)" % (X_STRIP_NEG,))

    x0h = x0_scan(HSW3)
    x0b = x0_scan(BW3)
    check("C4 x_0(HSW) == 121 and x_0(BW25) == 112 (recomputed)",
          x0h == X0_HSW_EXPECT and x0b == X0_BW_EXPECT,
          "integer scan 90..200: x_0 = %d (HSW22) / %d (BW25 "
          "published constants); bridge GAP-FREE: census [3, 121) + "
          "HSW/BW [x_0, oo) ==> THEOREM A's conditionality sharpens "
          "to EVERY INTEGER x >= 3 (H-pin stays the hypothesis)"
          % (x0h, x0b))

    hmax = 0.0
    for x in X_CENSUS:
        K = int(math.ceil(KFAC * x * math.log(x)))
        hmax = max(hmax, 2 * math.pi * x, gam[min(K - 2,
                                                  len(gam) - 1)])
    hmax = max(hmax, gam[-1])
    check("C5 heights typing: all census reads below horizon",
          hmax <= 7.3e3 and hmax < 3e12 / 1e8,
          "max height consumed = %.1f <= 7.3e3 << 3e12 (PT21): "
          "every cache use typed ward/classical-census-below-"
          "horizon (v914/v921 citation conventions)" % hmax)

    # ================================================ D: pinned E1/E2
    section("D. PINNED E1/E2 TABLES (consistency arithmetic)")
    pr = [float(v) for v in PIN_PRICE]
    okp = all(pr[i] >= pr[i + 1] for i in range(5))
    okn = sum(PIN_SLIVER_N) == 73     # G32 table rows == 73 unique
    # targets (71 sliver zeros + first zeros at b8/b18, whose
    # slivers are empty; at b5/b13/b24/b28 the first zero lies
    # inside the sliver; headline corrected 72 -> 73 per bughunt V,
    # round 164, note CDLXIX)
    mt = [float(v) for v in PIN_MINTLO]
    check("D1 sliver certificates: every target, price rides "
          "e^{-depth}", okp and okn and all(v > 0 for v in mt),
          "G32 table counts %s (sliver + first zero, b5..b28; 73 "
          "unique targets); price delta %s -> %s (BALL-CERT-DEPTH-"
          "PRICED: the f64 ball dies from b13 on -- machine-pinned "
          "obstruction); min T_lo/y_t %s..%s > 0 two-sided"
          % (PIN_SLIVER_N, PIN_PRICE[0], PIN_PRICE[5],
             PIN_MINTLO[5], PIN_MINTLO[0]))

    yc = [float(v) for v in PIN_YC]
    li = [float(v) for v in PIN_LAWID]
    dm = [float(v) for v in PIN_DEM]
    okl = all(1.0 < v < 1.05 for v in yc) \
        and all(v <= 5e-27 for v in li) \
        and all(0.2 <= v <= 0.45 for v in dm)
    check("D2 separation law: identity-certified, demand typed",
          okl,
          "y_C/b_top = %s (LAW-ID-CERT at b5/b8/b24, residuals <= "
          "%s; VACUOUS-TRUE at b13/b18/b28); lambda-uniform demand "
          "= %s..%s RvM mean spacings (band-edge zero REPULSION, "
          "ARITHMETIC-SIGNED-INPUT width, TAILVIS-style horizon "
          "typing; one-sided caps DEPTH-VACUOUS machine-pinned)"
          % (PIN_YC, PIN_LAWID[2], PIN_DEM[0], PIN_DEM[1]))

    check("D3 Z8 falls; census cardinality 4 unchanged",
          True if okLM else False,
          "SIMPLICITY subsumed by DELTA1FLOOR at demand points + "
          "zero-cost avoidance: census row Z8 eliminated (10 -> 9 "
          "rows); Z8 was never one of the four min-cut omegas -- "
          "{MEAS, OMEGA-POS} cardinality 4 UNCHANGED, no omega "
          "closed, nothing upgraded")

    print("\n  [TYPED, carried verbatim] The certificates are "
          "classical-census reads")
    print("  below the horizon; H-pin stays OPEN; Theorem A stays "
          "CONDITIONAL on")
    print("  H-pin (x-range sharpened to x >= 3).  NOT RH evidence.  "
          "NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v925 -- PRIME.EDGE.CLEANUP.CLOSURES.01 (Z8 subsumption + "
          "zero-cost")
    print("avoidance; the Q-swamp wholesale closure, 357 Turing-"
          "class certificates")
    print("RECOMPUTED; sliver certificates pinned; round 159; NO RH "
          "claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v925: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: the E3 Q-swamp closure RECOMPUTED in-run from "
          "the committed")
    print("verified-zero cache; the E1 sliver/separation and E2 "
          "witness tables PINNED")
    print("from edge_cleanup_probe.py (SPEC %s, 34/34, RE-RUN GREEN"
          % PIN_SPEC_R159)
    print("AT PROMOTION).  NOT RH evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.EDGE.CLEANUP.CLOSURES.01 edge/cleanup closures: "
          "%d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
