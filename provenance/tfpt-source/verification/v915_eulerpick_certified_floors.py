#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v915 -- PRIME.EULERPICK.CERTIFIED.FLOORS.01: THE CERTIFIED
EULER--PICK FLOORS N = 1..4 -- outward-rounded interval positivity
certificates for the first four rungs of the Euler--Pick falsification
ladder, promoted as certified-finite results with a disclosed
recomputed/pinned split.

THE OBJECT (V0c, audited in round 92 and not re-litigated here):
P(sigma) = xi'/xi(1/2 + sigma), sigma_j = 1 + 1/j,
Pick_N[j,k] = (P(sigma_j) + P(sigma_k))/(sigma_j + sigma_k).
RH iff Pick_N >= 0 for every N; the FORWARD direction (RH => all
Pick_N PSD) is exact (two rank-one Grams per zero ordinate).  Hence a
certified positive floor lambda_min(Pick_N) > 0 is an unconditional
finite consequence check of RH from prime data alone (source-only: no
zero computations anywhere), and a certified NEGATIVE rung would be an
RH-disproof candidate via the forward direction alone.

THE CERTIFIED RESULTS.
  Recomputed in-run (this module, round-95 architecture verbatim,
  crude far tail, own sieve, outward-rounded mpmath.iv end to end):
    cap 4e6:    N = 1, 2 certified positive (lo2 = 9.0287394e-6),
    cap 1.6e7:  N = 1, 2, 3 certified positive
                (lo3 = 2.3643695e-10 > 1e-10).
  Pinned from run-of-record (round 100, sieve4_eulerpick_n4_probe.py
  + compiled helper, 22/22 gates, 2681.8 s, cap X = 10^13, NOT
  re-runnable at verification time -- the 45-minute compiled sieve
  wall; run-of-record sieve4_run1.log):
    N = 1: [4.5917135e-2,  4.5917136e-2 ]
    N = 2: [9.0288887e-6,  9.0288888e-6 ]
    N = 3: [6.9310239e-10, 6.9310252e-10]
    N = 4: [8.278338e-15,  1.3840906e-14]   (margin lo/lambda = 0.749)
  with the hard external ward pi(10^13) = 346,065,536,839 reproduced
  EXACTLY by the run-of-record hybrid sieve.

CITED INPUTS, all published and pinned:
  [B18]  J. Buethe, Math. Comp. 87 (2018) 1991-2009:
         |psi(x) - x| < 0.94 sqrt(x) for 11 < x <= 10^19 (backed by
         verified zeros; the v594 pin), warded against own sieve data.
  [RS62] Rosser--Schoenfeld, Illinois J. Math. 6 (1962), Theorem 12:
         psi(x) < 1.03883 x for all x > 0 (the v563 pin), warded.
  [N82]  M. Nair, Amer. Math. Monthly 89 (1982) 126-129:
         psi(x) >= (x - 2) log 2 for x >= 7 (via lcm(1..n) >= 2^{n-1});
         warded against own sieve data.  The round-100 far-tail floor:
         beyond 10^19, E(x) in [-(1 - log 2) x - 2 log 2, 0.03883 x];
         WITHOUT Nair the crude floor (psi >= 0) BLOCKS N = 4 at ANY
         sieve cap (recomputed, check C4).
  [Ru10] S. M. Rump, Acta Numerica 19 (2010), Sec. 10: verified
         interval Cholesky (the lambda_min certificate method).
  Pins: pi(1e6) = 78498, pi(4e6) = 283146, pi(1.6e7) = 1031130,
  pi(1e13) = 346065536839, psi(4e6) = 3999490.856797.

PINNING DISCLOSURE (the recomputed/pinned split, exact):
  RECOMPUTED IN-RUN: the certificate machinery self-tests (planted
  PSD / singular-refuse / planted negative); the certified digamma
  enclosure; the own sieve to 1.6e7 with all three cited psi-bounds
  warded against own data at both caps; the FULL certified floors at
  caps 4e6 and 1.6e7 for N <= 3 (matching the round-95 record); the
  EM float references and corpus-floor parity; the summation-error
  model of the round-100 compiled run, re-derived rigorously from the
  pinned pi(10^13) and an RS-Abel upper bound on the helper sums (no
  sieve needed); the far-tail-floor necessity and the corrected
  budget X_req(4) = 10^11.52; the N = 5 knowledge wall; a subset of
  the round-95 planted-off-line detection table (the reach cap).
  PINNED FROM RUN-OF-RECORD (not recomputed): the four certified
  intervals at cap 10^13 with their rho_up values and the exact
  pi(10^13) reproduction, plus the run's window/pointwise wards --
  carried by sieve4_eulerpick_n4_probe.py + sieve4_run1.log (22/22).
  Consistency of the pinned record with everything recomputed here is
  gated (C1, C2).

HONEST TYPING -- THE FALSIFICATION CHANNEL IS REACH-CAPPED (round-108
audit, carried verbatim; NO overselling).  The channel is
DISPROOF-SOUND: a certified negative rung would falsify RH using only
the proven forward direction.  But it is REACH-CAPPED: the certified
N <= 4 slice detects a planted off-line zero pair only at gamma ~ 5-8
(delta <= 0.4; recomputed here, check D1), FAR below the
Platt--Trudgian verification height 3.0e12 -- so the channel has ZERO
live falsification power in the classically certified range; "open
and empty" is a THEOREM GIVEN THE CITED INPUTS, not an observation.
Extension walls are knowledge walls, not compute walls: N = 5 needs
the sqrt(x) psi-bound out to ~10^28 (verified zeros far beyond the
current height); no sieve helps (check C5).  These floors are NOT
evidence for or against the Riemann Hypothesis and close no gate.
NO RH CLAIM in either direction.

PROVENANCE: discovery probes eulerpick_ladder_probe.py (round 95,
note CCCXCVI, 31/31, SPEC bef49fd06f5ef609, re-run green at promotion
102.8 s, verdict EULERPICK-CERTIFIED(N<=3) + EULERPICK-GENERIC-DECAY
+ EULERPICK-DETECTION-LAW) and sieve4_eulerpick_n4_probe.py
(round 100, note CDI, 22/22, SPEC 4e87d18c8667b4c7, 2681.8 s
run-of-record, verdict EULERPICK-N4-CERTIFIED(lo=8.278338e-15,
margin=0.749)); criterion audit vbk_invariant_probe.py (round 92);
reach-cap typing bigpicture_logic_probe.py (round 108).  Python-only
per GATE.WOLFRAM.02 (interval arithmetic, eigensolver, sieve).
"""
from __future__ import annotations

import math
import time
from fractions import Fraction

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
CAP_CORPUS = 4_000_000
CAP_BEST = 16_000_000
Y_SPLIT = 10 ** 6
N_CERT = 3
IV_DPS_SUM = 22
IV_DPS_CERT = 60
C_BUETHE = "0.94"
B_PSI = "1.03883"
T_BUETHE = 10 ** 19
X_BUETHE_MIN = 11
DG_SHIFT = 32
DG_TERMS = 32
EM_CUT = 400
EM_TERMS = 60
EM_CUT_HI = 700
EM_TERMS_HI = 80
DPS_DETECT = 340
N_DETECT = 12
NEG_BAR = "1e-250"
TAU_FACTORS = ("0.99999999", "0.9999", "0.99", "0.9", "0.5", "0.25")

PI_PINS = {10 ** 6: 78_498, 4 * 10 ** 6: 283_146,
           16 * 10 ** 6: 1_031_130, 10 ** 13: 346_065_536_839}
CORPUS_PSI_4E6 = "3999490.856797"
CORPUS_FLOORS = ("4.59171357e-2", "9.0288888e-6",
                 "6.93102462e-10", "1.10594158e-14")
CORPUS_LAM5 = "7.91863638e-20"

# round-95 record (recomputed and matched in-run)
R95_LO2_4E6 = "9.0287394e-6"
R95_LO3 = "2.3643695e-10"
R95_HI3 = "1.1497752e-9"

# round-100 run-of-record at cap 10^13 (PINNED, not recomputed)
RECORD_1E13 = (
    ("4.5917135e-2", "4.5917136e-2"),
    ("9.0288887e-6", "9.0288888e-6"),
    ("6.9310239e-10", "6.9310252e-10"),
    ("8.278338e-15", "1.3840906e-14"),
)
RECORD_MARGIN = "0.7485"
RECORD_ERR_S = ("2.4e-24", "3.6e-21", "4.3e-20", "1.5e-19")
RECORD_ERR_TH = "4.44e-3"
RECORD_XREQ4 = 11.52
# frozen per-term/accumulation error-model constants of the round-100
# compiled helper (units of u = 2^-53), re-priced here from citations
K_TERM_U = 32
E_LOG_U = 4
DD_ACC_U2 = 4

# round-95 planted-off-line detection table subset (the reach cap)
DETECT_EXPECT = ((("5", "0.1"), 3), (("8", "0.1"), 4), (("8", "0.4"), 3))

N_CHECKS = 15
EXPECTED = "EULERPICK-FLOORS-CERTIFIED(N<=3 recomputed @ 1.6e7; " \
    "N<=4 pinned @ 1e13; reach-capped gamma~5-8)"

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
    import numpy as np
    from mpmath import iv, mp

    def iv_lo(x):
        return mp.make_mpf(x._mpi_[0])

    def iv_hi(x):
        return mp.make_mpf(x._mpi_[1])

    def fmt(x, d=8):
        return mp.nstr(x, d, min_fixed=0, max_fixed=0)

    # ---------------------------------------------------- machinery
    def bernoulli_fracs(m_max):
        B = [Fraction(1)]
        for m in range(1, m_max + 1):
            acc = Fraction(0)
            for k in range(m):
                acc += math.comb(m + 1, k) * B[k]
            B.append(-acc / (m + 1))
        return B

    BFR = bernoulli_fracs(2 * DG_TERMS + 2)

    def iv_frac(fr):
        return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)

    def iv_digamma(x):
        acc = iv.mpf(0)
        for k in range(DG_SHIFT):
            acc += 1 / (x + k)
        y = x + DG_SHIFT
        res = iv.log(y) - 1 / (2 * y) - acc
        y2 = 1 / (y * y)
        yp = y2
        for k in range(1, DG_TERMS + 1):
            res -= iv_frac(BFR[2 * k] / (2 * k)) * yp
            yp = yp * y2
        rem = iv_frac(abs(BFR[2 * DG_TERMS + 2])
                      / (2 * DG_TERMS + 2)) * yp
        return res + iv.mpf([-1, 1]) * rem

    def tail_iv(s, X, EX):
        """Round-95 certified tail: Buethe on [X, 1e19], crude
        psi >= 0 / RS band beyond (reproduces the round-95 record)."""
        half = iv.mpf(1) / 2
        lX = iv.log(iv.mpf(X))
        main = iv.exp((1 - s) * lX) / (s - 1) - EX * iv.exp(-s * lX)
        r_bu = iv.mpf(C_BUETHE) * iv.exp((half - s) * lX) / (s - half)
        lT = iv.log(iv.mpf(T_BUETHE))
        T1ms = iv.exp((1 - s) * lT)
        r_lo = T1ms / (s - 1)
        r_hi = (iv.mpf(B_PSI) - 1) * T1ms / (s - 1)
        lo = iv_hi(s * (r_bu + r_lo))
        hi = iv_hi(s * (r_bu + r_hi))
        return main + iv.mpf([-lo, hi])

    def em_P(sigma, cutoff, terms):
        s = mp.mpf("0.5") + sigma
        tot = mp.mpf(0)
        der = mp.mpf(0)
        for n in range(2, cutoff):
            u = mp.power(n, -s)
            tot += u
            der -= mp.log(n) * u
        tot += 1
        M = mp.mpf(cutoff)
        lM = mp.log(M)
        lead = M ** (1 - s) / (s - 1)
        tot += lead
        der += lead * (-lM - 1 / (s - 1))
        half = mp.mpf("0.5") * M ** (-s)
        tot += half
        der -= lM * half
        for k in range(1, terms + 1):
            order = 2 * k - 1
            corr = (mp.bernpoly(2 * k, 0) / mp.factorial(2 * k)
                    * mp.rf(s, order) * M ** (-s - order))
            harm = mp.fsum(1 / (s + i) for i in range(order))
            tot += corr
            der += corr * (harm - lM)
        return (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
                + mp.digamma(s / 2) / 2 + der / tot)

    def certified_lambda(mid, rad, N):
        rho = mp.mpf(0)
        for j in range(N):
            acc = iv.mpf(0)
            for k in range(N):
                acc += iv.mpf(rad[j][k])
            rho = max(rho, iv_hi(acc))
        Mmid = mp.matrix(N, N)
        for j in range(N):
            for k in range(N):
                Mmid[j, k] = mid[j][k]
        Ev, Q = mp.eigsy(Mmid)
        lam_t = min(Ev)
        idx = list(Ev).index(lam_t)
        v = [Q[r, idx] for r in range(N)]

        def chol_ok(tau):
            A = [[iv.mpf(mid[j][k]) - (iv.mpf(tau) if j == k else 0)
                  for k in range(N)] for j in range(N)]
            L = [[iv.mpf(0)] * N for _ in range(N)]
            for j in range(N):
                d = A[j][j]
                for t in range(j):
                    d -= L[j][t] * L[j][t]
                if not iv_lo(d) > 0:
                    return False
                L[j][j] = iv.sqrt(d)
                for k in range(j + 1, N):
                    x = A[k][j]
                    for t in range(j):
                        x -= L[k][t] * L[j][t]
                    L[k][j] = x / L[j][j]
            return True

        tau_ok = None
        if lam_t > 0:
            for f in TAU_FACTORS:
                tau = lam_t * mp.mpf(f)
                if chol_ok(tau):
                    tau_ok = tau
                    break
        num = iv.mpf(0)
        den = iv.mpf(0)
        for j in range(N):
            den += iv.mpf(v[j]) ** 2
            for k in range(N):
                num += iv.mpf(v[j]) * iv.mpf(v[k]) * iv.mpf(mid[j][k])
        ray_up = iv_hi(num / den)
        lo = (iv_lo(iv.mpf(tau_ok) - iv.mpf(rho))
              if tau_ok is not None else None)
        hi = iv_hi(iv.mpf(ray_up) + iv.mpf(rho))
        return lo, hi, rho, lam_t

    def entry_mid_rad(P_enc, N):
        sig_fr = [Fraction(j + 1, j) for j in range(1, N + 1)]
        mid = [[None] * N for _ in range(N)]
        rad = [[None] * N for _ in range(N)]
        for j in range(N):
            for k in range(N):
                E = (P_enc[j] + P_enc[k]) / iv_frac(sig_fr[j]
                                                    + sig_fr[k])
                a, b = iv_lo(E), iv_hi(E)
                m = a + (b - a) / 2
                r = max(iv_hi(iv.mpf(m) - iv.mpf(a)),
                        iv_hi(iv.mpf(b) - iv.mpf(m)))
                mid[j][k] = m
                rad[j][k] = r
        return mid, rad

    # ================================================== A: self-tests
    section("A. CERTIFICATE MACHINERY SELF-TESTS")
    iv.dps = IV_DPS_CERT
    mp.dps = IV_DPS_CERT
    mid2 = [[mp.mpf(2), mp.mpf(0)], [mp.mpf(0), mp.mpf(2)]]
    rad2 = [[mp.mpf("0.1")] * 2 for _ in range(2)]
    lo_p, hi_p, _, _ = certified_lambda(mid2, rad2, 2)
    ones = [[mp.mpf(1), mp.mpf(1)], [mp.mpf(1), mp.mpf(1)]]
    zr = [[mp.mpf(0)] * 2 for _ in range(2)]
    lo_s, _, _, _ = certified_lambda(ones, zr, 2)
    negm = [[mp.mpf(1), mp.mpf(0)], [mp.mpf(0), mp.mpf(-1)]]
    _, hi_n, _, _ = certified_lambda(negm, zr, 2)
    check("A1 certificate self-tests (PSD/singular/negative)",
          lo_p is not None and lo_p > mp.mpf("1.79") and hi_p >= 2
          and lo_s is None and hi_n < 0,
          "PSD lo=%s; singular refused=%s; planted hi=%s < 0"
          % (fmt(lo_p, 6), lo_s is None, fmt(hi_n, 4)))

    mp.dps = 120
    worst_w = mp.mpf(0)
    contain = True
    for nu, de in ((3, 4), (5, 4), (11, 12), (7, 8), (5, 6), (1, 1)):
        x_iv = iv.mpf(nu) / iv.mpf(de)
        ref = mp.digamma(mp.mpf(nu) / de)
        enc = iv_digamma(x_iv)
        contain = contain and (iv_lo(enc) <= ref <= iv_hi(enc))
        worst_w = max(worst_w, iv_hi(enc) - iv_lo(enc))
    check("A2 certified digamma: containment + width",
          contain and worst_w < mp.mpf("1e-50"),
          "contains mp.digamma on 6 nodes, max width=%s"
          % fmt(worst_w, 3))

    # ================================================== B: recompute
    section("B. RECOMPUTED CERTIFIED FLOORS (caps 4e6 and 1.6e7, "
            "N <= 3)")
    t_s = time.time()
    limit = CAP_BEST
    bits = bytearray(b"\x01") * (limit + 1)
    bits[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if bits[p]:
            bits[p * p:limit + 1:p] = b"\x00" * ((limit - p * p) // p
                                                 + 1)
    primes = np.flatnonzero(
        np.frombuffer(bytes(bits), dtype=np.uint8)).astype(np.int64)
    pi_1e6 = int(np.searchsorted(primes, Y_SPLIT, "right"))
    pi_4e6 = int(np.searchsorted(primes, CAP_CORPUS, "right"))
    check("B1 sieve anchors: pi(1e6), pi(4e6), pi(1.6e7)",
          pi_1e6 == PI_PINS[10 ** 6] and pi_4e6 == PI_PINS[CAP_CORPUS]
          and len(primes) == PI_PINS[CAP_BEST],
          "pi=%d/%d/%d (pinned %d/%d/%d), sieve %.1f s"
          % (pi_1e6, pi_4e6, len(primes), PI_PINS[10 ** 6],
             PI_PINS[CAP_CORPUS], PI_PINS[CAP_BEST],
             time.time() - t_s))

    iv.dps = IV_DPS_SUM
    S_IV = [iv.mpf(3 * j + 2) / iv.mpf(2 * j)
            for j in range(1, N_CERT + 1)]
    t_pass = time.time()
    sums = [iv.mpf(0) for _ in range(N_CERT)]
    theta = iv.mpf(0)
    snap = {}
    for p in primes:
        p = int(p)
        if p > CAP_CORPUS and CAP_CORPUS not in snap:
            snap[CAP_CORPUS] = (theta, list(sums))
        L = iv.log(iv.mpf(p))
        theta += L
        for i in range(N_CERT):
            sums[i] += L * iv.exp(-S_IV[i] * L)
    snap[CAP_BEST] = (theta, list(sums))
    t_pass = time.time() - t_pass
    print("  interval prime pass (iv.dps=%d, %d nodes): %.1f s"
          % (IV_DPS_SUM, N_CERT, t_pass))

    iv.dps = IV_DPS_CERT
    mp.dps = 120

    def powers(cap):
        th = iv.mpf(0)
        ss = [iv.mpf(0) for _ in range(N_CERT)]
        for p in primes:
            p = int(p)
            if p * p > cap:
                break
            L = iv.log(iv.mpf(p))
            q = p * p
            while q <= cap:
                th += L
                Lq = iv.log(iv.mpf(q))
                for i in range(N_CERT):
                    ss[i] += L * iv.exp(-S_IV[i] * Lq)
                q *= p
        return th, ss

    ln2 = math.log(2.0)
    psi_iv = {}
    finite = {}
    ward_ok = True
    ward_lines = []
    for cap in (CAP_CORPUS, CAP_BEST):
        th, ss = snap[cap]
        thp, ssp = powers(cap)
        psi = th + thp
        psi_iv[cap] = psi
        finite[cap] = [ss[i] + ssp[i] for i in range(N_CERT)]
        E_abs = max(abs(iv_lo(psi) - cap), abs(iv_hi(psi) - cap))
        this = (X_BUETHE_MIN < cap <= T_BUETHE
                and E_abs <= mp.mpf(C_BUETHE) * mp.sqrt(cap)
                and iv_hi(psi) < mp.mpf(B_PSI) * cap
                and iv_lo(psi) > (cap - 2) * ln2)
        ward_ok = ward_ok and this
        ward_lines.append("X=%.0e |E|=%.4g" % (cap, float(E_abs)))
    psi4 = psi_iv[CAP_CORPUS]
    mid4 = iv_lo(psi4) + (iv_hi(psi4) - iv_lo(psi4)) / 2
    check("B2 psi anchors + Buethe/RS/Nair wards vs own sieve",
          ward_ok and abs(mid4 - mp.mpf(CORPUS_PSI_4E6))
          < mp.mpf("1e-5"),
          "psi(4e6)=%s (corpus %s); |E|<=0.94sqrtX, psi<1.03883X, "
          "psi>(X-2)ln2 at %s" % (fmt(mid4, 13), CORPUS_PSI_4E6,
                                  "; ".join(ward_lines)))

    LOG_PI = iv.log(iv.pi)
    P_ENC = {}
    for cap in (CAP_CORPUS, CAP_BEST):
        EX = psi_iv[cap] - cap
        for j in range(1, N_CERT + 1):
            s = iv.mpf(3 * j + 2) / iv.mpf(2 * j)
            elem = (1 / s + 1 / (s - 1) - LOG_PI / 2
                    + iv_digamma(s / 2) / 2)
            P_ENC[(cap, j)] = (elem - finite[cap][j - 1]
                               - tail_iv(s, cap, EX))

    sig120 = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, 5)]
    P_ref = [em_P(s, EM_CUT, EM_TERMS) for s in sig120]
    contain = all(iv_lo(P_ENC[(cap, j)]) <= P_ref[j - 1]
                  <= iv_hi(P_ENC[(cap, j)])
                  for cap in (CAP_CORPUS, CAP_BEST)
                  for j in range(1, N_CERT + 1))
    check("B3 EM float reference inside every certified enclosure",
          contain, "6 enclosures (3 nodes x 2 caps), dps 120")

    mp.dps = IV_DPS_CERT
    floors = {}
    for cap in (CAP_CORPUS, CAP_BEST):
        print("  certified lambda_min intervals, cap=%d:" % cap)
        for N in range(1, N_CERT + 1):
            mid, rad = entry_mid_rad([P_ENC[(cap, j)]
                                      for j in range(1, N + 1)], N)
            lo, hi, rho, lam_t = certified_lambda(mid, rad, N)
            floors[(cap, N)] = (lo, hi, rho, lam_t)
            print("    N=%d  lo=%-14s hi=%-13s rho_up=%-10s  %s"
                  % (N, fmt(lo, 8) if lo is not None else "none",
                     fmt(hi, 8), fmt(rho, 4),
                     "CERTIFIED POSITIVE"
                     if (lo is not None and lo > 0)
                     else "UNDECIDED AT THIS CAP"))
    lo2_4 = floors[(CAP_CORPUS, 2)][0]
    check("B4 cap 4e6 certifies N<=2 (round-95 record matched)",
          all(floors[(CAP_CORPUS, N)][0] is not None
              and floors[(CAP_CORPUS, N)][0] > 0 for N in (1, 2))
          and abs(lo2_4 / mp.mpf(R95_LO2_4E6) - 1) < mp.mpf("1e-5"),
          "lo2=%s (record %s)" % (fmt(lo2_4, 8), R95_LO2_4E6))
    lo3 = floors[(CAP_BEST, 3)][0]
    hi3 = floors[(CAP_BEST, 3)][1]
    check("B5 cap 1.6e7 certifies N<=3, lo3 > 1e-10 (record matched)",
          all(floors[(CAP_BEST, N)][0] is not None
              and floors[(CAP_BEST, N)][0] > 0 for N in (1, 2, 3))
          and lo3 > mp.mpf("1e-10")
          and abs(lo3 / mp.mpf(R95_LO3) - 1) < mp.mpf("1e-5")
          and abs(hi3 / mp.mpf(R95_HI3) - 1) < mp.mpf("1e-5"),
          "lo3=%s hi3=%s (record %s / %s)"
          % (fmt(lo3, 8), fmt(hi3, 8), R95_LO3, R95_HI3))

    mp.dps = 120
    lam_ref = []
    for N in range(1, 5):
        M = mp.matrix(N, N)
        for j in range(N):
            for k in range(N):
                M[j, k] = (P_ref[j] + P_ref[k]) / (sig120[j]
                                                   + sig120[k])
        lam_ref.append(mp.eigsy(M, eigvals_only=True)[0])
    in_int = all(
        (floors[(cap, N)][0] is None
         or floors[(cap, N)][0] <= lam_ref[N - 1])
        and lam_ref[N - 1] <= floors[(cap, N)][1]
        for cap in (CAP_CORPUS, CAP_BEST) for N in range(1, N_CERT + 1))
    neg_hit = [(cap, N) for cap in (CAP_CORPUS, CAP_BEST)
               for N in range(1, N_CERT + 1)
               if floors[(cap, N)][1] < 0]
    check("B6 float floors inside intervals; channel open and EMPTY",
          in_int and not neg_hit,
          "certified hi<0 rungs: %s (a hit would be an RH-disproof "
          "candidate)" % (neg_hit or "none"))

    # ================================================== C: the record
    section("C. THE PINNED 10^13 RUN-OF-RECORD + RECOMPUTED MODELS")
    rec = [(mp.mpf(lo), mp.mpf(hi)) for lo, hi in RECORD_1E13]
    tol = mp.mpf("1e-6")
    consistent = all(0 < lo < hi for lo, hi in rec)
    for N in range(1, N_CERT + 1):
        r_lo, r_hi = rec[N - 1]
        c_lo, c_hi = floors[(CAP_BEST, N)][0], floors[(CAP_BEST, N)][1]
        # both enclose the true lambda_min; the 1e13 run tightens
        consistent = consistent and (r_lo <= c_hi * (1 + tol)
                                     and c_lo <= r_hi * (1 + tol))
    check("C1 pinned record consistent with the recomputed floors",
          consistent,
          "N=1..3: pinned 1e13 intervals intersect the recomputed "
          "1.6e7 intervals; N=3 tightened %s -> %s"
          % (fmt(hi3 - lo3, 3), fmt(rec[2][1] - rec[2][0], 3)))

    parity = max(abs(lam_ref[i] / mp.mpf(CORPUS_FLOORS[i]) - 1)
                 for i in range(4))
    in_rec = all(rec[i][0] * (1 - tol) <= lam_ref[i]
                 <= rec[i][1] * (1 + tol) for i in range(4))
    margin = rec[3][0] / lam_ref[3]
    check("C2 corpus-floor parity + record margin",
          parity < mp.mpf("1e-7") and in_rec
          and abs(margin / mp.mpf(RECORD_MARGIN) - 1) < mp.mpf("5e-3"),
          "max floor rel dev=%s; lam_ref inside all four pinned "
          "intervals; N=4 margin lo/lambda=%s (record %s)"
          % (fmt(parity, 3), fmt(margin, 4), RECORD_MARGIN))

    u53 = mp.mpf(2) ** -53
    n_c = mp.mpf(PI_PINS[10 ** 13] - PI_PINS[10 ** 6])
    err_ok = True
    err_lines = []
    for j in range(1, 5):
        s = mp.mpf(3 * j + 2) / (2 * j)
        s_up = (mp.mpf(B_PSI) * s / (s - 1)
                * mp.power(Y_SPLIT, 1 - s))     # RS-Abel upper bound
        err_bound = (K_TERM_U * u53 + DD_ACC_U2 * n_c * u53 ** 2) * s_up
        err_ok = (err_ok and err_bound <= mp.mpf("1e-18")
                  and mp.mpf(RECORD_ERR_S[j - 1]) <= err_bound)
        err_lines.append("j=%d %.1e" % (j, float(err_bound)))
    th_up = mp.mpf(B_PSI) * mp.mpf(10) ** 13
    err_th = (E_LOG_U * u53 + DD_ACC_U2 * n_c * u53 ** 2) * th_up
    check("C3 summation-error model re-derived (no sieve needed)",
          err_ok and err_th <= mp.mpf("1e-2")
          and mp.mpf(RECORD_ERR_TH) <= err_th,
          "ERR_S bounds %s (all <= 1e-18, record values below them); "
          "ERR_TH<=%.2e (record %s)"
          % ("; ".join(err_lines), float(err_th), RECORD_ERR_TH))

    # far-tail floor + corrected budget (round-100 float model)
    SIG_F = [1.0 + 1.0 / j for j in range(1, 6)]
    S_F = [1.5 + 1.0 / j for j in range(1, 6)]

    def far_band(j, nair):
        s = S_F[j - 1]
        t1ms = math.exp((1 - s) * math.log(T_BUETHE))
        lo = s * ((1 - ln2) if nair else 1.0) * t1ms / (s - 1)
        hi = s * 0.03883 * t1ms / (s - 1)
        return lo, hi

    def model_matrices(logX, nair, n=4):
        r = []
        d = []
        for j in range(1, n + 1):
            s = S_F[j - 1]
            bu = s * 0.94 * math.exp((0.5 - s) * logX) / (s - 0.5)
            flo, fhi = far_band(j, nair)
            r.append(bu + (flo + fhi) / 2)
            d.append(abs(fhi - flo) / 2)
        fr = fs = 0.0
        for j in range(n):
            for k in range(n):
                den = SIG_F[j] + SIG_F[k]
                fr += ((r[j] + r[k]) / den) ** 2
                fs += ((d[j] + d[k]) / den) ** 2
        return math.sqrt(fr), math.sqrt(fs)

    def x_req(lam, nair):
        lo_l, hi_l = 9.0 * math.log(10), 16.0 * math.log(10)
        rho_inf, shift_inf = model_matrices(hi_l, nair)
        if rho_inf + shift_inf >= lam:
            return None
        mid_l = None
        for _ in range(200):
            mid_l = (lo_l + hi_l) / 2
            rho, shift = model_matrices(mid_l, nair)
            if rho + shift > lam:
                lo_l = mid_l
            else:
                hi_l = mid_l
        return mid_l / math.log(10)

    lam4 = float(mp.mpf(CORPUS_FLOORS[3]))
    rho_c, shift_c = model_matrices(50.0, nair=False)
    xr_crude = x_req(lam4, nair=False)
    xr_nair = x_req(lam4, nair=True)
    check("C4 Nair floor necessity + corrected budget X_req(4)",
          xr_crude is None and rho_c + shift_c > lam4
          and xr_nair is not None and 11.2 < xr_nair < 12.2
          and abs(xr_nair - RECORD_XREQ4) < 0.05,
          "crude (psi>=0) floor blocks N=4 at ANY cap "
          "(rho+shift=%.2e > lambda_4=%.2e); Nair unblocks: "
          "X_req(4)=10^%.2f (record 10^%.2f)"
          % (rho_c + shift_c, lam4, xr_nair or -1, RECORD_XREQ4))

    lam5 = float(mp.mpf(CORPUS_LAM5))
    flo5, _ = far_band(5, nair=True)
    s5 = S_F[4]
    t_pp = 1 - ln2
    T_need = (lam5 / 4 / (s5 * t_pp / (s5 - 1))) ** (1.0 / (1 - s5))
    lo_l, hi_l = 12.0 * math.log(10), 22.0 * math.log(10)
    for _ in range(200):
        mid_l = (lo_l + hi_l) / 2
        bu5 = s5 * 0.94 * math.exp((0.5 - s5) * mid_l) / (s5 - 0.5)
        if bu5 * 2.0 > lam5:
            lo_l = mid_l
        else:
            hi_l = mid_l
    xr5_bu = mid_l / math.log(10)
    check("C5 N=5 is a KNOWLEDGE wall, not a compute wall",
          flo5 > 100 * lam5 and T_need > 1e25
          and 15.5 < xr5_bu < 17.5,
          "far floor/lambda_5=%.1e at ANY cap; needs the sqrt-x "
          "psi-bound to T~%.1e (verified zeros ~3e12); "
          "X_req5(Buethe-only)=10^%.2f" % (flo5 / lam5, T_need,
                                           xr5_bu))

    # ================================================== D: reach cap
    section("D. THE REACH CAP (recomputed detection subset, "
            "round-108 typing)")
    mp.dps = DPS_DETECT
    sigD = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, N_DETECT + 1)]
    PE = [em_P(s, EM_CUT_HI, EM_TERMS_HI) for s in sigD]
    neg_bar = -mp.mpf(NEG_BAR)

    def Qpair(s, d, g):
        return (2 * (s - d) / ((s - d) ** 2 + g ** 2)
                + 2 * (s + d) / ((s + d) ** 2 + g ** 2))

    def detect(dm, gm, nmax):
        Pd = [PE[j] + Qpair(sigD[j], dm, gm) - Qpair(sigD[j], 0, gm)
              for j in range(nmax)]
        for n in range(1, nmax + 1):
            M = mp.matrix(n, n)
            for j in range(n):
                for k in range(n):
                    M[j, k] = (Pd[j] + Pd[k]) / (sigD[j] + sigD[k])
            if mp.eigsy(M, eigvals_only=True)[0] < neg_bar:
                return n
        return None

    det_ok = True
    det_lines = []
    for (gs, ds), expect in DETECT_EXPECT:
        nstar = detect(mp.mpf(ds), mp.mpf(gs), N_DETECT)
        det_ok = det_ok and nstar == expect
        det_lines.append("gamma=%s delta=%s N*=%s (expect %d)"
                         % (gs, ds, nstar, expect))
    check("D1 planted-off-line detection subset (round-95 table)",
          det_ok, "; ".join(det_lines))

    gamma_reach = 8
    t_pt = 3_000_175_332_800
    check("D2 reach cap vs the verification height (disproof-sound, "
          "reach-capped)",
          det_ok and t_pt / gamma_reach > 3.75e11
          and not neg_hit and consistent,
          "certified N<=4 slice sees off-line pairs only at "
          "gamma~5-8 << PT height 3.0e12 (factor %.2e): ZERO live "
          "falsification power in the certified range; channel open "
          "and EMPTY" % (t_pt / gamma_reach))
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v915 -- PRIME.EULERPICK.CERTIFIED.FLOORS.01 (certified "
          "Euler--Pick floors")
    print("N=1..4: N<=3 recomputed at cap 1.6e7, N=4 pinned from the "
          "10^13 run-of-")
    print("record; cited Buethe 2018 + RS 1962 + Nair 1982; "
          "falsification channel")
    print("disproof-sound but reach-capped gamma~5-8; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v915: %d/%d checks passed | runtime %.1f s"
          % (n_run - len(fails), n_run, time.time() - T_ALL))
    print("verdict %s" % verdict)
    print("PINNING: N<=3 floors + all wards + models RECOMPUTED; the "
          "cap-10^13 N=4")
    print("intervals + pi(10^13) ward PINNED from sieve4_run1.log "
          "(22/22, 2681.8 s).")
    print("Reach-capped falsification channel; NOT RH evidence; NO RH "
          "claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails "
          "(got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, n_run,
             fails or "none"))
    print("--- PRIME.EULERPICK.CERTIFIED.FLOORS.01 certified floors: "
          "%d passed, %d failed ---" % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
