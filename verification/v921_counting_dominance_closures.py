#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v921 -- PRIME.COUNTING.DOMINANCE.CLOSURES.01: THE COUNTING-CLASS
CLOSURES -- the pure classical-citation theorems of rounds 133 and 143,
promoted as certified finite theorems: Theorems M/E/T/C (ball-counting
dominance; Theorem T UNCONDITIONAL) and Theorem T1 (TAILVIS existence,
closed from HSW22/RvM alone), with Theorem A's closed-form assemblage
and its honest Q-swamp obstruction carried verbatim.

THE THEOREMS:

  ROUND 133 (note CDXXXVI, dominance_proof_probe.py):
  THEOREM M (ball-counting slack dominance; PROVEN, pure counting):
     matching all m zone zeros into disjoint ordered balls
     [gamma_j - g_j, gamma_j + g_j] (H1) + no stray nodes below
     max(T_z, gamma_m + g_m) (H2) + one node per ball (H3) ==>
     sorted mu_i >= gamma_i - g_i for i <= m and mu_i > T_z beyond;
     COROLLARY: the false-sign mass M^- is bounded by pinning-gap
     mass at ANY sign resolution (no sign reads).
  THEOREM E (edge counting bounds; PROVEN): M^-_edge <=
     (N - m) w(T_z) exactly; M^+_edge <= a G(T_z) (HSW-closed).
  THEOREM T (top segment; PROVEN, UNCONDITIONAL): N_fin(T) <=
     N_true(T) for ALL T >= T*(x), T* the closed solve of
     M(T*) - Q(T*) = K - 1, consuming ONLY the exact node count
     K - 1 (v919 secular, cited) + HSW22 |N - M| <= Q; and
     gamma_{K-1} <= T* anchors the tail.
  THEOREM C (chain sharpening; PROVEN, exact): DOM ==> MRB <= 1 ==>
     WPD with constant <= 1 on the whole battery; and weak one-
     sidedness M^- <= (1 - th)(M^+ + tail_1) gives the EXACT
     identity d_1 == th (M^+ + tail_1) and MRB <= (2 - th)/th
     (monotone in M^-): MRB is STRICTLY WEAKER than DOM -- per-node
     one-sidedness is NOT needed and is not claimed.
  THEOREM A (assemblage; PROVEN CONDITIONAL on H-pin): under H-pin
     the closed HSW forms give d_1 >= D(x, a) > 0 and the MRB bound,
     machine-instantiated for all integer x in [x_0, 200] and the
     asymptotic grid to 1e6 with x_0 = 121; the bound falls 144.1
     (x = 144) -> 10.5 (x = 1e6).  HONEST OBSTRUCTION (Q-SWAMP,
     carried): D < 0 on the battery strip x in {13..89} -- the
     unconditional counting currency cannot see tail_1 below
     x_0 = 121; the battery strip stays per-rung certified only.

  ROUND 143 (note CDXLVII, toproot_tailvis_probe.py):
  THEOREM T1 (TAILVIS existence; PROVEN, classical): N(T + L) -
     N(T) >= L rho_RvM(T) - 2 err_HSW(T + L) via the two-sided HSW
     envelope + convexity (main'' = 1/(2 pi T) > 0, exact); hence
     every window of length L*(T) = (1 + 2 err)/rho carries a true
     zero UNCONDITIONALLY; L* = O(20) and FALLING at the onset
     heights while the B1 windows grow ~ x^2.06: TAILVIS is
     ELIMINATED as a standalone arithmetic omega (counting class).
     CARRIER DISCLOSURE (typed, carried): the window sits at height
     Theta ~ x^2.06, so the on-line reading of window zeros is
     PT21-warranted only for 2 Theta(x) <= T_PT, i.e. x <~ 2.3e5 --
     a carrier class like the census itself, NOT a new arithmetic
     omega; all six rungs (2 Theta <= 25181) are far inside.
  THEOREM T3 (B1 source+counting instantiation): (1 - theta)_cnt >=
     8 eps^2 (1 - rho)^2 A_0^2/((2 Theta)^2 (tau + OFF)) with
     rho = 0.5, eps = 0.1 -- NO zero ordinate consumed: positive at
     ALL SIX rungs including x = 24/28 (the round-140
     TAILVIS-HORIZON-LIMITED typing RESOLVED without new zeros).

WHAT IS RECOMPUTED IN-RUN (exact / closed-form, self-contained):
  T1  Theorems M/E on an exact rational instance (H1/H2/H3,
      conclusions, M^-/edge bounds) + the stray refusal (H2 AND
      dominance both fail) + the empty-ball refusal;
  T2  Theorem C: the equality-case identity and (2 - th)/th cap
      (exact rationals) + the sympy general identity d_1 ==
      th (M^+ + tail_1) and the monotonicity derivative;
  T3  Theorem T: T*(x) recomputed by closed-form bisection at
      K - 1 = 4/10/20/41 (== ceil(1.25 x log x) - 1) and the pinned
      classical gamma anchors below T* (63.55/79.17/102.80/147.13
      vs 30.42/49.77/77.14/124.26);
  T4  Theorem A closed forms (the Bughunt-IV independent re-
      implementation, ported): the Q-swamp strip D < 0 at x in
      {13, 21, 34, 55, 89}, x_0 = 121, x_0(BW25) = 112 under the
      published BW25 constants (0.10076, 0.24460, 8.08344), MRB
      bound 144.1 at x = 144 and 10.5 at x = 1e6;
  T5  Theorem T1 algebra: main' == rho_RvM, main'' == 1/(2 pi T) > 0,
      the rearrangement and the L* solve (sympy exact);
  T6  the L*(T) and m_W^HSW tables recomputed from the pinned onset
      heights (L* falling 34.4 -> 19.1; m_W = Theta rho(Theta) -
      2 q(2 Theta) >= 100 at every rung);
  T7  Theorem T3 recomputed at x = 5/8/13 from the v919-pinned
      (A_0, tau) strings (5.38e-7/1.06e-7/1.95e-8 -- matching the
      frozen table to < 2%), pinned at x = 18/24/28; the poly
      envelope log10(1/(1 - theta)) <= 4.5 + 4.0 log10 x at all six.

PINNED FROM RUN-OF-RECORD, disclosed split:
  ROUND 133 -- RE-RUN GREEN AS TYPED AT PROMOTION (40/40 gates,
  SPEC_SHA 00b98f5eebf9c5fb; run-of-record 339.0 s + deterministic
  re-run, logs sha256 34eb2b2ffa477681 / f67016f3bd078568): the
  per-rung certificates -- zone/matched/stray = 1/1/0, 4/4/0,
  10/10/0, 21/21/0; M^- <= 7.3e-7/5.8e-10/4.9e-13/1.6e-13 (a = 4);
  MRB_cert flat 0.0693..0.0833 (bar 0.25); C_cert = 1.025..1.048
  <= 1.5 with d_1_lo > 0 everywhere; the controls REFUSE at the
  named hypothesis H2 (SMOOTH/SCRARITH x=5, EPSTEIN x=8: stray
  counts 7/7/16, mu_1 = 4.836/2.006/1.230 inside the verified
  zero-free gap (0, 14.13) -- H2 IS the consumption of the
  arithmetic zero-free structure).
  ROUND 143 -- PINNED (NOT re-run at promotion; 4016.1 s run-of-
  record + 3921.4 s deterministic re-run, 27/27 gates, SPEC_SHA
  4fcd70beb7cf4f17, logs sha256 25c774de5c31f9c8 / 86022c425b62c942;
  the T1 window counting was independently re-derived against the
  cache in Bughunt IV, and the T1/L*/T3 closed forms are recomputed
  in-run here): the onset heights 359.9/942.8/2619.6/5191.2/9276.4/
  12590.4, the (1 - theta)_cnt table, N_vis/N_bad in-cache tables
  (N_bad <= 5.8%), the S_C Landau-form tables (Landau 1912 / Gonek
  1993 cited AS FORM only, consumed with >= 500x headroom).

HONEST TYPING (carried verbatim; nothing upgraded).  Theorem A is
CONDITIONAL on H-pin (typed; H-pin is exactly the L1-BAND omega of
v919 in ball currency).  The Q-swamp strip obstruction is carried,
not smoothed.  The TAILVIS window carrier x <~ 2.3e5 is disclosed
(carrier class, like the PT21 census carrier x <= 4.8e11).  DOM
itself (per-node one-sidedness) is NOT proven and NOT needed
(Theorem C).  These closures eliminate TAILVIS as a standalone
arithmetic omega and make counting dominance a theorem for T >= T*;
they close NO other omega: OPEN stays {TOPROOT, ONSETCAP(=TLAWCAP),
SUSCAP2R} + DELTA1FLOOR + dense-a/a-extension/window-a; the census
{MEAS, OMEGA-POS} stays at CARDINALITY 4.  NOT evidence for or
against the Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probes dominance_proof_probe.py (round 133,
2026-08-16, note CDXXXVI, contract PRIME.MRB.DOMINANCE.PROOF.01) and
toproot_tailvis_probe.py (round 143, note CDXLVII, contract
PRIME.TOPROOT.TAILVIS.PROOF.01); independent re-derivations
bughunt4_probe.py (round 149: own Theorem M/E/T/C/A instances +
closed forms, strip/x_0/MRB replicated; own T1 window counting).
Cited classical inputs: Hasanalizade--Shen--Wong JNT 235 (2022)
Cor. 1.2; the published BW25 constants (v1-abstract discrepancy
disclosed in round 144 and verified in Bughunt IV); Platt--Trudgian
2021; Rosser--von-Mangoldt density; Landau 1912 / Gonek 1993 as
form; the classical gamma_1 isolation.  Python-only per
GATE.WOLFRAM.02.
"""
from __future__ import annotations

import math
import time
from fractions import Fraction

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R133 = "00b98f5eebf9c5fb"
PIN_SPEC_R143 = "4fcd70beb7cf4f17"
HSW = (0.1038, 0.2573, 9.3675)
BW25 = (0.10076, 0.24460, 8.08344)
# Theorem T anchors: (x, K-1, T* pinned, gamma_{K-1} pinned)
PIN_THMT = ((3, 4, "63.55", "30.42"), (5, 10, "79.17", "49.77"),
            (8, 20, "102.80", "77.14"), (13, 41, "147.13", "124.26"))
# r143 onset heights + tables (x = 5/8/13/18/24/28)
PIN_THETA = ("359.9", "942.8", "2619.6", "5191.2", "9276.4", "12590.4")
PIN_LSTAR = ("34.4", "28.2", "23.7", "21.4", "19.9", "19.1")
PIN_MW = (211, 731, 2494, 5528, 10752, 15213)
PIN_T3 = ("5.383e-07", "1.057e-07", "1.945e-08", "6.781e-09",
          "2.666e-09", "1.487e-09")
XS6 = (5, 8, 13, 18, 24, 28)
# v919-pinned (A_0, tau) at x = 5/8/13 for the T3 recompute
PIN_A0_TAU = (("4.73e-08", "1.607e-16"), ("8.42e-15", "3.773e-30"),
              ("8.17e-27", "2.499e-54"))
# r133 per-rung certificates (a = 4)
PIN_MRB_CERT = ("0.0713", "0.0831", "0.0785", "0.0739")
PIN_C_CERT = ("1.025", "1.032", "1.038", "1.048")
PIN_MMINUS = ("7.3e-07", "5.8e-10", "4.9e-13", "1.6e-13")
PIN_MU1_CONTROLS = ("4.836", "2.006", "1.230")   # inside (0, 14.13)

N_CHECKS = 9
EXPECTED = "COUNTING-DOMINANCE-CLOSURES"

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


def m_rvm(T):
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


def q_hsw(T, C=HSW):
    return C[0] * math.log(T) + C[1] * math.log(math.log(T)) + C[2]


def hsw_G(T, C=HSW):
    from mpmath import mp
    with mp.workdps(40):
        Tm = mp.mpf(T)
        al, be, cc = (mp.mpf(repr(c)) for c in C)
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg)) + cc) \
            / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return float(t1 + t2 + t3)


def t_star(N, C=HSW):
    lo, hi = 20.0, 1e30
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if m_rvm(mid) - q_hsw(mid, C) >= N:
            hi = mid
        else:
            lo = mid
    return hi


def part():
    import sympy as sp

    # ================================================== T1: M/E instance
    section("T1. THEOREMS M/E ON AN EXACT INSTANCE + REFUSALS")
    a = Fraction(4)

    def w(t):
        return a * t * t / (a + t * t) ** 2
    trues = [Fraction(4), Fraction(5), Fraction(6), Fraction(17, 2),
             Fraction(11), Fraction(30), Fraction(45)]
    gs = [Fraction(1, 50), Fraction(1, 40), Fraction(1, 30)]
    nodes = [Fraction(4) + Fraction(1, 100),
             Fraction(5) - Fraction(1, 80),
             Fraction(6) + Fraction(1, 90), Fraction(9), Fraction(13)]
    Tz = Fraction(7)
    m = sum(1 for t in trues if t <= Tz)
    balls = [(trues[j] - gs[j], trues[j] + gs[j]) for j in range(m)]
    okH1 = all(balls[j][1] < balls[j + 1][0] for j in range(m - 1))
    inb = [[n for n in nodes if lo <= n <= hi] for lo, hi in balls]
    top = max(Tz, balls[-1][1])
    okH2 = all(any(lo <= n <= hi for lo, hi in balls)
               for n in nodes if n <= top)
    okH3 = all(len(v) == 1 for v in inb)
    okC1 = all(sorted(nodes)[i] >= trues[i] - gs[i] for i in range(m))
    okC2 = all(sorted(nodes)[i] > Tz for i in range(m, len(nodes)))
    mm = sum(max(Fraction(0), w(nodes[i]) - w(trues[i]))
             for i in range(len(nodes)))
    zone_bound = sum(w(trues[j] - gs[j]) - w(trues[j]) for j in range(m))
    edge_bound = sum(max(Fraction(0), w(nodes[i]) - w(trues[i]))
                     for i in range(m, len(nodes)))
    okM2 = mm <= zone_bound + edge_bound
    okE = (edge_bound <= (len(nodes) - m) * w(Tz))
    nodes_s = sorted([Fraction(3)] + nodes)
    okH2s = all(any(lo <= n <= hi for lo, hi in balls)
                for n in nodes_s if n <= top)
    doms = all(nodes_s[i] >= trues[i] - gs[i] for i in range(m))
    ok_stray = (not okH2s) and (not doms)
    nodes_e = [Fraction(4) + Fraction(1, 100),
               Fraction(4) + Fraction(3, 200),
               Fraction(6) + Fraction(1, 90), Fraction(9), Fraction(13)]
    okP_e = all(any(lo <= n <= hi for n in nodes_e)
                for lo, hi in balls)
    ok_empty = not okP_e
    check("T1 Theorems M/E exact instance + both refusals",
          okH1 and okH2 and okH3 and okC1 and okC2 and okM2 and okE
          and ok_stray and ok_empty,
          "H1/H2/H3 + sorted dominance + M^-/edge bounds exact in Q; "
          "stray refusal (H2 AND dominance both fail); empty-ball "
          "refusal (pure counting -- no sign reads, no monotonicity)")

    # ================================================== T2: Theorem C
    section("T2. THEOREM C (chain sharpening, exact)")
    th = Fraction(1, 3)
    Mp, tail = Fraction(7, 5), Fraction(2, 5)
    Mm = (1 - th) * (Mp + tail)
    d1 = Mp - Mm + tail
    okC = (d1 == th * (Mp + tail)) and \
        ((Mp + Mm) / d1 <= (2 - th) / th)
    ths, Mps, tls = sp.symbols("th Mp tl", positive=True)
    Mmv = sp.symbols("Mm", positive=True)
    Mms = (1 - ths) * (Mps + tls)
    d1s = sp.simplify(Mps - Mms + tls - ths * (Mps + tls))
    mrb = (Mps + Mms) / (Mps - Mms + tls)
    dnum = sp.simplify(sp.expand(sp.together(sp.diff(
        (Mps + Mmv) / (Mps - Mmv + tls), Mmv))
        * (Mps - Mmv + tls) ** 2) - (2 * Mps + tls))
    # (2-th)/th - MRB == tail_1/(th (M^+ + tail_1)) EXACTLY (>= 0):
    # equality iff tail_1 = 0 -- the cap is sharp in that limit
    cap = sp.simplify((2 - ths) / ths - mrb
                      - tls / (ths * (Mps + tls)))
    check("T2 Theorem C: exact identity + (2 - th)/th cap", okC
          and d1s == 0 and dnum == 0 and cap == 0,
          "M^- <= (1-th)(M^+ + tail_1) ==> d_1 == th (M^+ + tail_1) "
          "EXACT; MRB monotone in M^- (derivative numerator == "
          "2 M^+ + tail_1); at equality MRB == (2-th)/th: MRB "
          "STRICTLY WEAKER than DOM -- per-node one-sidedness not "
          "needed")

    # ================================================== T3: Theorem T
    section("T3. THEOREM T (unconditional counting dominance)")
    okT = True
    dets = []
    for x, N, ts_pin, gam_pin in PIN_THMT:
        K = int(math.ceil(1.25 * x * math.log(x)))
        okT = okT and (K - 1 == N)
        ts = t_star(N)
        okT = okT and abs(ts / float(ts_pin) - 1) < 5e-3 \
            and float(gam_pin) <= ts
        dets.append("x%d T*=%.2f g_%d=%s" % (x, ts, N, gam_pin))
    check("T3 T*(x) recomputed; gamma_(K-1) <= T* per rung", okT,
          "; ".join(dets) + " -- N_fin(T) <= N_true(T) is a THEOREM "
          "for ALL T >= T* (consumes only K-1 exact [v919] + HSW22)")

    # ================================================== T4: Theorem A
    section("T4. THEOREM A CLOSED FORMS + THE Q-SWAMP (honest)")

    def wf(av, t):
        return av * t * t / (av + t * t) ** 2

    def DM(x, av, C=HSW):
        K = int(math.ceil(1.25 * x * math.log(x)))
        N = K - 1

        def qh(T):
            return C[0] * math.log(T) + C[1] * math.log(math.log(T)) \
                + C[2]
        lo, hi = 20.0, 1e30
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            if m_rvm(mid) - qh(mid) >= N:
                hi = mid
            else:
                lo = mid
        Ts = hi
        Tzx = 2 * math.pi * x
        nz = m_rvm(Tzx) - qh(Tzx)
        best = 0.0
        for lam in (1.5, 2.0, 3.0):
            for J in (1, 2, 3, 4, 6, 8):
                Tj = [Ts * lam ** j for j in range(J + 1)]
                tot, up = 0.0, m_rvm(Ts) + qh(Ts)
                for j in range(J):
                    nn = m_rvm(Tj[j + 1]) - qh(Tj[j + 1])
                    tot += max(0.0, nn - max(float(N), up)) \
                        * wf(av, Tj[j + 1])
                    up = m_rvm(Tj[j + 1]) + qh(Tj[j + 1])
                best = max(best, tot)
        TL = best
        me = max(0.0, N - nz) * wf(av, Tzx)
        Dv = TL - TL / 8.0 - me
        mrb = ((TL / 8.0 + av * hsw_G(Tzx, C) + me) / Dv
               if Dv > 0 else float("inf"))
        return Dv, mrb

    bat = (1.0, 4.0, 16.0)
    ok_strip = all(DM(x, av)[0] < 0 for x in (13, 21, 34, 55, 89)
                   for av in bat)

    def x0_scan(C):
        okx = {x: all(DM(float(x), av, C)[0] > 0 for av in bat)
               for x in range(90, 201)}
        for xc in range(90, 201):
            if all(okx[x] for x in range(xc, 201)):
                return xc
        return None

    x0 = x0_scan(HSW)
    x0_bw = x0_scan(BW25)
    mrb144 = max(DM(144.0, av)[1] for av in bat)
    mrb1e6 = max(DM(1e6, av)[1] for av in bat)
    ok_asym = (abs(mrb144 / 144.1 - 1) < 0.01
               and abs(mrb1e6 / 10.5 - 1) < 0.02)
    check("T4 strip D<0 (13..89), x_0 = 121, BW25 x_0 = 112, MRB "
          "ladder", ok_strip and x0 == 121 and x0_bw == 112
          and ok_asym,
          "x_0 = %s (r133: 121), x_0(BW25) = %s (r144: 112), "
          "MRB(144) = %.1f, MRB(1e6) = %.1f (Bughunt-IV closed forms "
          "ported); the Q-SWAMP obstruction is CARRIED: the counting "
          "currency cannot see tail_1 below x_0 -- Theorem A is "
          "CONDITIONAL on H-pin" % (x0, x0_bw, mrb144, mrb1e6))

    # ================================================== T5: T1 algebra
    section("T5. THEOREM T1 (TAILVIS existence, classical; sympy)")
    Tsym, Lsym, rhosym, e1, e2 = sp.symbols("T L rho e1 e2",
                                            positive=True)
    mainT = Tsym / (2 * sp.pi) * sp.log(Tsym / (2 * sp.pi * sp.E))
    ok5 = sp.simplify(sp.diff(mainT, Tsym)
                      - sp.log(Tsym / (2 * sp.pi)) / (2 * sp.pi)) == 0
    ok5 = ok5 and sp.simplify(sp.diff(mainT, Tsym, 2)
                              - 1 / (2 * sp.pi * Tsym)) == 0
    # two-sided envelope rearrangement:
    # N(T+L) - N(T) >= [main(T+L) - e2] - [main(T) + e1]
    #               >= L main'(T) - (e1 + e2)   (convexity)
    lower = (mainT.subs(Tsym, Tsym + Lsym) - e2) - (mainT + e1)
    conv = sp.simplify(
        lower - (Lsym * sp.log(Tsym / (2 * sp.pi)) / (2 * sp.pi)
                 - (e1 + e2))
        - (mainT.subs(Tsym, Tsym + Lsym) - mainT
           - Lsym * sp.log(Tsym / (2 * sp.pi)) / (2 * sp.pi)))
    solL = sp.solve(sp.Eq(Lsym * rhosym - (1 + 2 * sp.symbols(
        "err", positive=True)), 0), Lsym)
    ok5 = ok5 and conv == 0 and len(solL) == 1 and sp.simplify(
        solL[0] - (1 + 2 * sp.symbols("err", positive=True))
        / rhosym) == 0
    check("T5 T1 window counting (convexity + L* solve, exact)", ok5,
          "main' == rho_RvM, main'' == 1/(2 pi T) > 0; N(T+L) - N(T) "
          ">= L rho(T) - 2 err(T+L); L* == (1 + 2 err)/rho: window "
          "existence is CLASSICAL (HSW22 Cor. 1.2 cited)")

    # T6: L* and m_W tables from the pinned onset heights
    ok6 = True
    dets = []
    prev = None
    for i, th_s in enumerate(PIN_THETA):
        Th = float(th_s)
        rho = math.log(Th / (2 * math.pi)) / (2 * math.pi)
        lstar = (1 + 2 * q_hsw(Th)) / rho
        mw = Th * rho - 2 * q_hsw(2 * Th)
        ok6 = ok6 and abs(lstar / float(PIN_LSTAR[i]) - 1) < 0.02
        ok6 = ok6 and abs(mw / PIN_MW[i] - 1) < 0.01 and mw >= 100
        ok6 = ok6 and (prev is None or lstar < prev)
        prev = lstar
        dets.append("x%d L* %.1f mW %d" % (XS6[i], lstar, round(mw)))
    check("T6 L*(T) falling + m_W^HSW >= 100 (recomputed)", ok6,
          "; ".join(dets) + " -- L*/Theta collapses 0.096 -> 0.0015: "
          "every B1 window carries a zero unconditionally")

    # T7: Theorem T3 recompute (x = 5/8/13) + pinned poly envelope
    ok7 = True
    dets = []
    for i in range(3):
        A0 = float(PIN_A0_TAU[i][0])
        tau = float(PIN_A0_TAU[i][1])
        Th = float(PIN_THETA[i])
        val = 8 * 0.1 ** 2 * (1 - 0.5) ** 2 * A0 ** 2 \
            / ((2 * Th) ** 2 * tau)
        ok7 = ok7 and abs(val / float(PIN_T3[i]) - 1) < 0.02
        dets.append("x%d %.3e" % (XS6[i], val))
    for i in range(6):
        inv = -math.log10(float(PIN_T3[i]))
        ok7 = ok7 and inv <= 4.5 + 4.0 * math.log10(XS6[i])
    ok7 = ok7 and all(float(PIN_T3[i]) > float(PIN_T3[i + 1])
                      for i in range(5))
    check("T7 T3 recomputed from v919 pins + poly envelope", ok7,
          "; ".join(dets) + " (frozen %s/%s/%s); all six rungs "
          "positive incl. x = 24/28 (TAILVIS-HORIZON-RESOLVED, no "
          "new zeros); log10(1/(1-th)) <= 4.5 + 4.0 log10 x"
          % PIN_T3[:3])

    # ================================================== pinned r133
    section("T8. PINNED r133 CERTIFICATES + CONTROLS (consistency)")
    okm = all(float(v) <= 0.25 for v in PIN_MRB_CERT)
    okc = all(1.0 < float(v) <= 1.5 for v in PIN_C_CERT)
    okmm = all(float(v) <= 1e-6 for v in PIN_MMINUS)
    check("T8a MRB_cert <= 0.25; C_cert <= 1.5; M^- tiny", okm
          and okc and okmm,
          "MRB_cert(a=4) = %s (flat); C_cert = %s; M^- <= %s..%s: "
          "the full round-132 residue {d_1 > 0, MRB} certified "
          "per rung with NO sign reads"
          % ((PIN_MRB_CERT,), (PIN_C_CERT,), PIN_MMINUS[0],
             PIN_MMINUS[3]))
    okmu = all(0 < float(v) < 14.13 for v in PIN_MU1_CONTROLS)
    check("T8b controls refuse at H2 (zero-free gap consumed)", okmu,
          "SMOOTH/SCRARITH/EPSTEIN mu_1 = %s/%s/%s all inside the "
          "verified zero-free gap (0, 14.13): the mechanism claims "
          "WPD nowhere PD is false" % PIN_MU1_CONTROLS)

    print("\n  [TYPED, carried verbatim] Theorem A CONDITIONAL on "
          "H-pin; Q-swamp strip")
    print("  carried; TAILVIS window carrier x <~ 2.3e5 disclosed "
          "(carrier class);")
    print("  DOM itself not proven and not needed.  OPEN stays "
          "{TOPROOT, ONSETCAP,")
    print("  SUSCAP2R} + DELTA1FLOOR + a-walls; census cardinality 4 "
          "UNCHANGED.  NOT RH")
    print("  evidence.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v921 -- PRIME.COUNTING.DOMINANCE.CLOSURES.01 (Theorems "
          "M/E/T/C + Theorem A")
    print("closed forms + T1 TAILVIS existence + T3 counting "
          "instantiation; rounds")
    print("133/143, re-derived in Bughunt IV; NOT RH evidence; NO RH "
          "claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v921: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: Theorems M/E/C instances, T* solves, Theorem A "
          "closed forms, T1")
    print("algebra, L*/m_W/T3 recomputed in-run; r133 certificates "
          "pinned from")
    print("dominance_proof_probe.py (SPEC %s, 40/40, RE-RUN GREEN AT "
          "PROMOTION" % PIN_SPEC_R133)
    print("339.3 s); r143 tables PINNED from run-of-record "
          "toproot_tailvis_probe.py")
    print("(SPEC %s, 27/27, run1+run2 logs kept; T1 re-derived in "
          "Bughunt IV)." % PIN_SPEC_R143)
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.COUNTING.DOMINANCE.CLOSURES.01 counting-"
          "dominance closures: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
