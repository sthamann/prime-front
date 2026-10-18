#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v914 -- PRIME.PASCAL.REGION.THEOREM.01: THE PASCAL-REGION THEOREM --
the largest proven positivity region of the prime-front campaign,
promoted as a certified-finite result.

THE STATEMENT (proven from cited external inputs alone).  Put a = 256,
z_rho = (rho - 1/2)^2, y_rho = a/(a - z_rho) and

    C_{n,k}(256) = sum_{Im rho > 0} y_rho^(n+1) (1 - y_rho)^k

(absolutely convergent; rho runs over the nontrivial zeta zeros).  Then

    C_{n,k}(256) > 0   for every n >= 0 and every integer
                       0 <= k <= 7,444,682,106,464,286,365,865  (~7.44e21).

External inputs, all published and pinned (the v594 pinning style):

  [PT21]  Platt--Trudgian, Bull. LMS 53 (2021) 792-797, Theorem 1:
          every nontrivial zero with 0 < Im rho <= T = 3,000,175,332,800
          lies on Re rho = 1/2.
  [HSW22] Hasanalizade--Shen--Wong, J. Number Theory 235 (2022) 219-241,
          COROLLARY 1.2:  |N(t) - M(t)| <= 0.1038 log t
          + 0.2573 log log t + 9.3675 for t >= e, with
          M(t) = t/(2 pi) log(t/(2 pi e)).
  [R41]   Rosser, Amer. J. Math. 63 (1941), Theorem 19 (zero counting
          with explicit error), used by the k <= 10^19 base region.
  [G1]    the classical first-zero isolation 14.1347 < gamma_1 < 14.1348.

HSW ATTRIBUTION, RESOLVED (the round-110 flag).  The discovery probe
moonshot_o3_probe.py quotes the constants under "Corollary 1.2" but then
calls "Corollary 1.4" the corrected replacement.  Resolution from the
paper itself: COROLLARY 1.2 is the N(t) bound with exactly the constants
(0.1038, 0.2573, 9.3675) and main term M(t) -- the statement this
theorem consumes; COROLLARY 1.4 is the companion S(t) bound
|S(t)| <= min{0.1038 log t + 0.2573 log log t + 8.3675,
0.1095 log t + 0.2042 log log t + 3.0305} and is NOT used here.  The
older constants (0.110, 0.290, 2.290) are the earlier Platt--Trudgian
S(t) bound whose proof consumed an incorrect Cheng--Graham estimate
(recorded in [HSW22]); they bound S(t), not N(t), and are NOT used.

THE PROOF MECHANISM, two stages, both recomputed or pinned below.
Stage 1 (round 103, k <= 10^19, [PT21]+[R41]+[G1]; re-derived
independently in the round-109 Bughunt II, B1a): a four-region
partition -- (i) n = 0, k <= 24 by the first zero alone; (ii) n = 0,
25 <= k <= 10^19 by a Rosser-counted on-line Beta-kernel interval
against the unknown-zero tail bound B_0(T); (iii) n >= 1, theta =
k/(n+1) <= 40 by the first zero against B_n(T); (iv) n >= 1,
40 <= theta <= 10^19/(n+1) by the counted interval.  All four regions
are recomputed at verification time (checks B1-B9).  The same n = 0
mechanism exhausts at k* = 1.40544e19 -- a bound failure, not a
negative cell (printed).
Stage 2 (round 106, the 530x extension to k_max, [PT21]+[HSW22]):
retain the q^k factor in the arbitrary-zero envelope; below H = T - 1
bound the verified on-line zeros from below by 16384 RvM packets
(Corollary 1.2 at each packet endpoint); above T bound the unknown
tail by an alternating Gaussian-log series enclosure; cover all
integers k on a 33-cell adaptive endpoint partition (verified kernel
decreasing in k, unknown envelope increasing on each cell, so ONE
endpoint inequality proves the whole cell).  The n = 0 inequality
lifts to all n >= 0 because y(H) > p(T) (check C1).

THE LAW (round 106, proven for this packet/tail mechanism): the
frontier of the mechanism obeys

    k_front(T) = (lambda_inf + O(1/log T)) T^2/(a - 1/2),
    lambda_inf = 0.226987054723979955
    (unique root of erfc(r sqrt(l)) = r erf(sqrt(l)), r = sqrt(a/c)),

i.e. verification height qT buys q^2 columns; the geometric ceiling
k_geo = (T^2 + 1/4)/(a - 1/2) is intrinsically unreachable by this
route (stop at ~0.227 k_geo; today k_max/k_geo = 0.2113215513454976).
The constant is recomputed at verification time (check D1).

PINNING DISCLOSURE (what is recomputed vs pinned from run-of-record):
  RECOMPUTED IN-RUN: the complete Stage-1 four-region arithmetic
  (B1-B9, all inequalities strict, anchors matched to the frozen
  probe values); the HSW error value E_N(T); the uniform-n lift and
  the geometric ceiling; the STRUCTURE of the 33-cell partition
  (contiguity, bootstrap endpoint 10^19, frontier endpoint k_max); a
  FROZEN SUBSAMPLE of 6 of the 33 cells including the worst (last)
  cell, each re-proved by the full 16384-packet endpoint inequality
  L(k_hi) > B(k_lo); the tail-enclosure validity conditions; the
  frontier-exactness diagnostic (the next 2e-6 relative step FAILS);
  lambda_inf and the law coefficient.
  PINNED FROM RUN-OF-RECORD (not recomputed in-run): the remaining
  27 of the 33 cell endpoint inequalities, carried by the frozen
  probe moonshot_o3_probe.py, re-run green at promotion (16/16,
  100.8 s, frontier verbatim 7,444,682,106,464,286,365,865); the cell
  list below is that run's adaptive partition, byte-exact.

HONEST TYPING (round-108 big-picture audit, carried verbatim).  This
is a VERIFICATION-POWERED, FORM-LOCAL theorem: its zero-location
content sits below gamma_1 = 14.13, where [PT21] is infinitely
stronger; certified Pascal/Hausdorff cells say NOTHING about screw
sections or Weyl disks (form-locality -- the round-108 counterexample
world keeps every Hausdorff cell positive at n + k <= 50 while the
Euler--Pick section fires at N = 12); the k -> infinity quantifier is
touched nowhere.  It consumes NO wall positivity, NO zero table and
NO zeta evaluator at runtime.  It is NOT evidence for or against the
Riemann Hypothesis and must not be counted as RH progress.  NO RH
CLAIM in either direction.

PROVENANCE: discovery probes moonshot_sol_probe.py (round 103,
2026-08-15, 12/12, SPEC b29984ca9c1570f2, verdict
MOONSHOT-PARTIAL(Form A; k <= 10^19)) and moonshot_o3_probe.py
(round 106, 16/16, SPEC 88ea3c73 prefix per frozen file, verdict
MOONSHOT3-EXTENDED(frontier = 7444682106464286365865)); independent
re-derivation bughunt2_r86_r105_probe.py (round 109, B1a: B_0 exact,
four partition ratios to 1e-9, k* consistent); typing
bigpicture_logic_probe.py (round 108: form-locality, reach caps).
Python-only per GATE.WOLFRAM.02 (mpmath findroot/quadrature-free
enclosures; the exact identities live in the probes).
"""
from __future__ import annotations

import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
A_INT = 256
T_PT_INT = 3_000_175_332_800
K_BOOT = 10 ** 19
K_MAX = 7_444_682_106_464_286_365_865
PACKETS = 16384
U_CAP = 12

# HSW22 Cor. 1.2 constants (N(t) bound; Cor. 1.4 is the S(t) companion).
HSW_A = "0.1038"
HSW_B = "0.2573"
HSW_C = "9.3675"
# Rosser 1941 Thm 19 constants (Stage 1 only).
ROSSER = ("0.137", "0.443", "1.588")
GAMMA1 = ("14.1347", "14.1348")

# run-of-record anchors (frozen probe outputs, re-run at promotion)
PIN_B0 = "7.57565571105606088e-10"
PIN_E_N_T = "13.213637697887"
PIN_R_BRIDGE = "1.876981097339"
PIN_R_ROW0 = "1.176577026464"
PIN_R_LOW = "335.835448342609"
PIN_R_HIGH = "1416.754103822636"
PIN_KSTAR = "1.405443828790708e19"
PIN_H4E = ("1.931162851973", "2.662737548397")
PIN_WORST_RATIO = "1.000001535385559"
PIN_NEXT_DIAG = "0.999999870144434"
PIN_K_FRAC = "0.2113215513454976"
PIN_LAMBDA_INF = "0.226987054723979955"
PIN_COEFF = "0.000888403345299334461"

# the 33-cell adaptive endpoint partition of the run-of-record
# (moonshot_o3_probe.py, re-run at promotion; contiguous; the single
# endpoint test packet_lower(hi) > tail_upper(lo) proves each cell)
CELLS = (
    (10000000000000000000, 15000000000000000000),
    (15000000000000000000, 22500000000000000000),
    (22500000000000000000, 33750000000000000000),
    (33750000000000000000, 50625000000000000000),
    (50625000000000000000, 75937500000000000000),
    (75937500000000000000, 113906250000000000000),
    (113906250000000000000, 170859375000000000000),
    (170859375000000000000, 256289062500000000000),
    (256289062500000000000, 384433593750000000000),
    (384433593750000000000, 576650390625000000000),
    (576650390625000000000, 864975585937500000000),
    (864975585937500000000, 1297463378906250000000),
    (1297463378906250000000, 1946195068359375000000),
    (1946195068359375000000, 2919292602539062500000),
    (2919292602539062500000, 4378938903808593750000),
    (4378938903808593750000, 5726412449942440604409),
    (5726412449942440604409, 6534516936186455659187),
    (6534516936186455659187, 6976098923912000680076),
    (6976098923912000680076, 7206847844716148205226),
    (7206847844716148205226, 7324823859289099644149),
    (7324823859289099644149, 7384496100143501454093),
    (7384496100143501454093, 7414517323790223461590),
    (7414517323790223461590, 7429580846251991967426),
    (7429580846251991967426, 7437129097228619147550),
    (7437129097228619147550, 7440908968437922174357),
    (7440908968437922174357, 7442801151244209424617),
    (7442801151244209424617, 7443748209831520351994),
    (7443748209831520351994, 7444222183709115601666),
    (7444222183709115601666, 7444459383204218268056),
    (7444459383204218268056, 7444578086824601872932),
    (7444578086824601872932, 7444637489996340081148),
    (7444637489996340081148, 7444667217129852106161),
    (7444667217129852106161, 7444682106464286365865),
)
# frozen recompute subsample (indices into CELLS; 32 = the worst cell)
SUBSAMPLE = (0, 8, 16, 24, 30, 32)

N_CHECKS = 18
EXPECTED = "PASCAL-REGION-THEOREM(k_max=%d)" % K_MAX

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


def part():
    from mpmath import mp

    def match(value, pinned_str, digits):
        pin = mp.mpf(pinned_str)
        return abs(value / pin - 1) < mp.mpf(10) ** (-digits)

    # ================================================== A: inputs
    section("A. CITED INPUTS + THE HSW ATTRIBUTION (resolved)")
    mp.dps = 70
    a = mp.mpf(A_INT)
    A_sh = a - mp.mpf("0.25")
    c_sh = a - mp.mpf("0.5")
    T = mp.mpf(T_PT_INT)
    H = T - 1

    def rv_main(t):
        return t / (2 * mp.pi) * mp.log(t / (2 * mp.pi * mp.e))

    def rv_error(t):
        return (mp.mpf(HSW_A) * mp.log(t)
                + mp.mpf(HSW_B) * mp.log(mp.log(t)) + mp.mpf(HSW_C))

    e_n_t = rv_error(T)
    check("A1 HSW22 Cor. 1.2 applicability + E_N(T) anchor",
          T >= mp.e and H >= mp.e and match(e_n_t, PIN_E_N_T, 10),
          "t >= e at every endpoint; E_N(T)=%s (pinned %s)"
          % (mp.nstr(e_n_t, 14), PIN_E_N_T))
    print("  [RESOLVED] Cor. 1.2 = the N(t) bound used here "
          "(0.1038, 0.2573, 9.3675);")
    print("  Cor. 1.4 = the companion S(t) bound (NOT used); the old "
          "(0.110, 0.290,")
    print("  2.290) constants bound S(t) via an invalid Cheng--Graham "
          "input (per HSW22).")

    # ================================================== B: stage 1
    section("B. STAGE 1 RECOMPUTED: THE k <= 10^19 REGION "
            "([PT21]+[R41]+[G1])")
    mp.dps = 80
    a80 = mp.mpf(A_INT)
    A80 = a80 - mp.mpf("0.25")
    T80 = mp.mpf(T_PT_INT)
    r_iv = mp.mpf(3) / 2
    ros_a, ros_b, ros_c = (mp.mpf(x) for x in ROSSER)
    g1_lo, g1_hi = (mp.mpf(x) for x in GAMMA1)

    def rosser_error(t):
        return ros_a * mp.log(t) + ros_b * mp.log(mp.log(t)) + ros_c

    def count_half_lower(theta):
        g = mp.sqrt(a80 * theta)
        return (g * (r_iv - 1 / r_iv) / (2 * mp.pi)
                * mp.log(g / (2 * mp.pi * r_iv)) / 2)

    def tail_bound(n):
        ls = mp.log(T80 / (2 * mp.pi))
        if n == 0:
            return a80 / mp.pi * (ls + 1) / T80
        ratio = a80 / (T80 ** 2 + A80)
        return a80 * (n + 1) / (2 * mp.pi * n) * ls / T80 * ratio ** n

    gap = T80 / (2 * mp.pi) - mp.mpf(7) / 8 - rosser_error(T80)
    deriv = (1 / (2 * mp.pi) - ros_a / T80
             - ros_b / (T80 * mp.log(T80)))
    check("B1 COUNT from Rosser at T", gap > 0 and deriv > 0,
          "gap=%.6e deriv=%.6e" % (float(gap), float(deriv)))

    geo_ok = True
    for delta in ("-0.5", "-0.25", "0", "0.25", "0.5"):
        for gamma in (mp.mpf(14), mp.mpf(1000), T80, 10 * T80):
            z = (mp.mpf(delta) + 1j * gamma) ** 2
            y = a80 / (a80 - z)
            geo_ok &= abs(y) <= a80 / (A80 + gamma ** 2) \
                * (1 + mp.mpf("1e-60"))
            geo_ok &= abs(1 - y) <= 1
    check("B2 GEO arbitrary-zero envelope", geo_ok,
          "|y| <= a/(A+g^2), |1-y| <= 1 on the sample grid")

    b0 = tail_bound(0)
    b1 = tail_bound(1)
    check("B3 unknown-zero tail B_0(T) anchor", match(b0, PIN_B0, 15),
          "B_0=%s (pinned %s)" % (mp.nstr(b0, 19), PIN_B0))

    y_lo = a80 / (a80 + g1_hi ** 2)
    q_lo = g1_lo ** 2 / (a80 + g1_lo ** 2)
    bridge = y_lo * q_lo ** 24 / b0
    bridge25 = y_lo * q_lo ** 25 / b0
    check("B4 region (i): n=0, k<=24 first-zero bridge",
          bridge > 1 and match(bridge, PIN_R_BRIDGE, 10),
          "ratio(k=24)=%s > 1; same bound at k=25: %s"
          % (mp.nstr(bridge, 13), mp.nstr(bridge25, 6)))

    h4e_25 = (2 * count_half_lower(mp.mpf(25))
              / (4 * rosser_error(r_iv * mp.sqrt(a80 * 25))))
    h4e_40 = (2 * count_half_lower(mp.mpf(40))
              / (4 * rosser_error(r_iv * mp.sqrt(a80 * 40))))
    check("B5 Rosser interval-count starts",
          h4e_25 > 1 and h4e_40 > 1
          and match(h4e_25, PIN_H4E[0], 10)
          and match(h4e_40, PIN_H4E[1], 10),
          "H/(4E): theta=25 %s; theta=40 %s"
          % (mp.nstr(h4e_25, 13), mp.nstr(h4e_40, 13)))

    d_const = mp.mpf("0.5") * min(r_iv ** 2 * mp.exp(-r_iv ** 2),
                                  r_iv ** -2 * mp.exp(-r_iv ** -2))
    row0 = count_half_lower(mp.mpf(K_BOOT)) * d_const / K_BOOT / b0
    check("B6 region (ii): n=0 counted-Beta range to 10^19",
          row0 > 1 and match(row0, PIN_R_ROW0, 10),
          "ratio=%s (pinned %s)" % (mp.nstr(row0, 13), PIN_R_ROW0))

    kstar = mp.findroot(
        lambda k: count_half_lower(k) * d_const / k - b0,
        (mp.mpf("1e19"), mp.mpf("2e19")))
    check("B7 the n=0 mechanism root k* (bound failure, not a "
          "negative cell)",
          mp.mpf("1.40e19") < kstar < mp.mpf("1.41e19")
          and match(kstar, PIN_KSTAR, 10),
          "k*=%s (pinned %s)" % (mp.nstr(kstar, 16), PIN_KSTAR))

    low = y_lo ** 2 * q_lo ** 80 / b1
    check("B8 region (iii): n>=1, theta<=40 first-zero region",
          low > 335 and match(low, PIN_R_LOW, 10),
          "worst n=1,k=80 ratio=%s" % mp.nstr(low, 13))

    theta_max = mp.mpf(K_BOOT) / 2
    high = count_half_lower(theta_max) * (d_const / theta_max) ** 2 / b1
    top = r_iv * mp.sqrt(a80 * theta_max)
    check("B9 region (iv): n>=1, 40<=theta<=1e19/(n+1) counted region",
          high > 1416 and top < T80 and match(high, PIN_R_HIGH, 10),
          "worst n=1 theta=5e18 ratio=%s; interval top %s < T"
          % (mp.nstr(high, 13), mp.nstr(top, 6)))

    # ================================================== C: stage 2
    section("C. STAGE 2: THE 33-CELL FRONTIER TO k_max "
            "([PT21]+[HSW22 Cor. 1.2])")
    mp.dps = 70

    def online_kernel_0(t, k):
        y = a / (a + t * t)
        return y * mp.power(1 - y, k)

    def unknown_kernel_0(t, k):
        den = t * t + A_sh
        return a / den * mp.power((t * t + mp.mpf("0.25")) / den, k)

    def packet_lower(k):
        kmp = mp.mpf(k)
        g = mp.sqrt(a * kmp)
        u_floor = g / H
        du = (mp.mpf(U_CAP) - u_floor) / PACKETS
        total = mp.mpf(0)
        for i in range(PACKETS):
            u_l = u_floor + i * du
            u_r = u_l + du
            t_hi = g / u_l
            t_lo = g / u_r
            cnt = (rv_main(t_hi) - rv_main(t_lo)
                   - rv_error(t_hi) - rv_error(t_lo))
            if cnt <= 0:
                continue
            total += cnt * min(online_kernel_0(t_lo, k),
                               online_kernel_0(t_hi, k))
        return total

    def gaussian_log_integral_upper(v, log_scale, terms=20):
        total = mp.mpf(0)
        for j in range(terms + 1):
            deg = 2 * j + 1
            mag = (v ** deg / mp.factorial(j)
                   * ((log_scale - mp.log(v)) / deg
                      + mp.mpf(1) / deg ** 2))
            total += (-1) ** j * mag
        nj = terms + 1
        deg = 2 * nj + 1
        width = (v ** deg / mp.factorial(nj)
                 * ((log_scale - mp.log(v)) / deg
                    + mp.mpf(1) / deg ** 2))
        return total, width

    def tail_upper(k):
        kmp = mp.mpf(k)
        d_eff = c_sh / (1 + A_sh / T ** 2)
        v = mp.sqrt(d_eff * kmp) / T
        ls = mp.log(mp.sqrt(d_eff * kmp) / (2 * mp.pi))
        integral, series_width = gaussian_log_integral_upper(v, ls)
        main = a / (2 * mp.pi * mp.sqrt(d_eff * kmp)) * integral
        err = (2 * rv_error(T) * unknown_kernel_0(T, k)
               + (mp.mpf(HSW_A) + mp.mpf(HSW_B) / mp.log(T))
               * a / (2 * T ** 2))
        return main + err, v, series_width / integral

    y_h = a / (a + H ** 2)
    p_t = a / (T ** 2 + A_sh)
    check("C1 uniform-n lift: y(H) > p(T)", y_h > p_t,
          "y(H)/p(T)-1 = %.3e (V_n >= y(H)^n L_0 > p(T)^n B_0)"
          % float(y_h / p_t - 1))

    k_geo = (T ** 2 + mp.mpf("0.25")) / c_sh
    k_frac = mp.mpf(K_MAX) / k_geo
    check("C2 geometric ceiling + frontier fraction",
          mp.mpf(K_MAX) < k_geo and match(k_frac, PIN_K_FRAC, 12),
          "k_geo=%s; k_max/k_geo=%s (pinned %s)"
          % (mp.nstr(k_geo, 10), mp.nstr(k_frac, 16), PIN_K_FRAC))

    contiguous = (CELLS[0][0] == K_BOOT
                  and CELLS[-1][1] == K_MAX
                  and all(CELLS[i][1] == CELLS[i + 1][0]
                          for i in range(len(CELLS) - 1))
                  and all(lo < hi for lo, hi in CELLS))
    check("C3 pinned 33-cell partition structure",
          len(CELLS) == 33 and contiguous,
          "33 contiguous cells, 10^19 (Stage-1 bootstrap) -> k_max")

    worst_ratio = None
    sub_ok = True
    details = []
    for idx in SUBSAMPLE:
        lo, hi = CELLS[idx]
        lower = packet_lower(hi)
        upper, v_at, w_rel = tail_upper(lo)
        ratio = lower / upper
        sub_ok = sub_ok and ratio > 1 and v_at < mp.mpf("0.5") \
            and w_rel < mp.mpf("1e-30")
        details.append("cell%d %.9f" % (idx, float(ratio)))
        if idx == 32:
            worst_ratio = ratio
            worst_v, worst_w = v_at, w_rel
    check("C4 subsample cell recompute (6 of 33, full 16384 packets)",
          sub_ok and worst_ratio is not None
          and match(worst_ratio, PIN_WORST_RATIO, 10),
          "; ".join(details))
    check("C5 tail alternating enclosure valid at the worst cell",
          worst_v < mp.mpf("0.5") and worst_w < mp.mpf("1e-30"),
          "v=%.6f < 1/2; omitted-series/main <= %.2e"
          % (float(worst_v), float(worst_w)))

    next_k = K_MAX + int(K_MAX * 2e-6)
    diag = packet_lower(next_k) / tail_upper(K_MAX)[0]
    check("C6 frontier is mechanism-exact: next 2e-6 step FAILS",
          diag < 1 and match(diag, PIN_NEXT_DIAG, 8),
          "L(k_max+2e-6 rel)/B(k_max)=%s (pinned %s)"
          % (mp.nstr(diag, 15), PIN_NEXT_DIAG))

    # ================================================== D: the law
    section("D. THE QUADRATIC VERIFICATION-HEIGHT LAW")
    ratio_ac = mp.sqrt(a / c_sh)
    lam_inf = mp.findroot(
        lambda lam: mp.erfc(ratio_ac * mp.sqrt(lam))
        - ratio_ac * mp.erf(mp.sqrt(lam)),
        (mp.mpf("0.20"), mp.mpf("0.24")))
    residual = abs(mp.erfc(ratio_ac * mp.sqrt(lam_inf))
                   - ratio_ac * mp.erf(mp.sqrt(lam_inf)))
    check("D1 lambda_inf recomputed",
          residual < mp.mpf("1e-60") and match(lam_inf, PIN_LAMBDA_INF, 17),
          "lambda_inf=%s (pinned %s), residual %.1e"
          % (mp.nstr(lam_inf, 19), PIN_LAMBDA_INF, float(residual)))
    coeff = lam_inf / c_sh
    check("D2 law coefficient + headroom",
          match(coeff, PIN_COEFF, 15) and k_frac < lam_inf,
          "k_front(T)=(lambda_inf+O(1/log T)) T^2/(a-1/2); coeff=%s; "
          "headroom lambda_inf - k_frac = %s"
          % (mp.nstr(coeff, 18), mp.nstr(lam_inf - k_frac, 8)))

    print("\n  [FORM-LOCAL, round-108 typing] zero-location content "
          "below gamma_1 = 14.13,")
    print("  where [PT21] is stronger; certified Pascal cells say "
          "NOTHING about screw")
    print("  sections or Weyl disks; the k -> infinity quantifier is "
          "untouched; NOT RH")
    print("  evidence.  No wall positivity, no zero table, no zeta "
          "evaluator consumed.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v914 -- PRIME.PASCAL.REGION.THEOREM.01 (the Pascal-region "
          "theorem:")
    print("C_(n,k)(256) > 0 for all n >= 0, 0 <= k <= "
          "7,444,682,106,464,286,365,865;")
    print("cited inputs PT21 + HSW22 Cor. 1.2 + Rosser 1941; "
          "form-local; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v914: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: Stage 1 fully recomputed; Stage 2 = pinned 33-cell "
          "run-of-record")
    print("partition with a 6-cell full-packet recompute (incl. the "
          "worst cell) and")
    print("structure/exactness gates.  Form-local; NOT RH evidence; "
          "NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict %s "
          "(got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.PASCAL.REGION.THEOREM.01 pascal-region theorem: "
          "%d passed, %d failed ---" % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
