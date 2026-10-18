#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v916 -- PRIME.KR4.EPSTEIN.COLLAPSE.01: THE CERTIFIED EPSTEIN
WEIL-POSITIVITY VIOLATION -- an explicit sha-pinned unit test vector
whose Weil pairing with the source data of Q = x^2 + 5y^2 is certified
negative, built purely from r_Q(n) lattice counts, promoted as a
certified-finite falsifier instrument with a disclosed recomputed/
pinned split.

THE STATEMENT (certified-numeric, recomputed at every suite run):
there is an explicit unit float64 vector x (len 1038, sha-256 prefix
b01436d53d2cbbee) such that the tent-autocorrelation test function
psi_x = h_x * h~_x >= 0 pairs NEGATIVELY with the Epstein source data
-g_Q'' of Q(x,y) = x^2 + 5y^2 (discriminant -20, class number 2):
  V = x^T T x = -1.9697e-2,  error budget <= 4.3e-68,
  two-precision (dps 80/110) relative agreement 9.8e-79,
i.e. windowed Weil positivity for xi_Q FAILS at window t <= 3.114 --
a mesh-free statement (the mesh only selects test functions; the
finite t is an UPPER bound on the true violation window).  The row
T_k[i,j] = row[|i-j|] is built from the Lambda_Q sieve ALONE:
r_Q(n) by exact lattice count, Lambda_Q by the log-derivative
recursion r(1) Lam(n) = r(n) log n - sum_{e|n,1<e<n} Lam(e) r(n/e)
(NO Euler product exists; Lambda_Q lives on all n and can be
negative), screw function
  g_Q(t) = -8(cosh(t/2) - 1) + sum_{log n < t} (Lambda_Q(n)/sqrt n)
           (t - log n) + a_Q t - S_Q(0) + S_Q(t),
  S_Q(t) = e^{-t/2} Phi(e^{-t}, 2, 1/2),  S_Q(0) = pi^2/2,
  a_Q = -psi(1/2) - c20,  c20 = log(sqrt(20)/(2 pi)),
lag row by exact second differences.  Zero cache unused; witness
constants firewalled out of every builder (probe gate G01); the
detection consumes NO zero data.

THE CONTROLS (the fires-iff-fires content): TRUE zeta AND the
conductor-matched null zeta_K = zeta L_{-20} (same pole layer, same
arch layer, same conductor constant, Euler atoms, GRH-expected)
both complete Weil positivity through L = 8.0 -- conductor alone
does not collapse; the round-120 background caveat is RESOLVED.
The Q world DIES at t_death = 2.988 (Szego pivot k = 996 at dps 80;
eigenvalue crossing k_dagger = 998, |diff| = 2 bins; mesh mate
delta = 0.006 dies at 3.006; dps 60/80 identical).  Recomputed
HERE: the Q death, the mesh mate, the ZK null positive through the
recomputed prefix L = 4.0 > t_death + 1.0, the Q-scramble control
death at 2.727, and the certificate vector's positivity on the ZK
null row (the same x reads POSITIVE on the matched null).

INTERPRETATION TYPING (carried verbatim from the frozen probe): the
certified value V < 0 is an unconditional-numeric SOURCE-side
statement (typed CERT-NUM: two-precision-warded, budgeted evaluation
of an exact finite rational-in-logs expression).  The step
"V < 0 => xi_Q has an off-line zero" rides the classical
Weil/Guinand explicit formula for xi_Q (Hecke theta; typed
COND-CLASSICAL, cited not re-proven).  The classical fact that such
Epstein zeta functions have off-line zeros is 90 years old
(Potter--Titchmarsh 1935 computed the first ones;
Davenport--Heilbronn 1936): the promoted claim is the certified
explicit finite certificate FROM SOURCE DATA, not the existence.
KNOWN-FALSEHOOD, NEW-INSTRUMENT.

PRE-DECLARED FALSIFIED PREDICTIONS, carried (the probe's three
failing gates G18/G19/G21 are the RECORD, not smoothed away):
  G18 attribution -- the single-witness model is FALSIFIED:
      Q-minus-witness dies at 2.970 (witness removal moves the death
      by only 0.018), typed COLLECTIVE; Q minus ALL FOUR located
      off-line pairs survives to 4.428 (LOCATED-SPECTRUM-CARRIES).
  G19 death law -- the measured law 1.875 + 0.374 ln(1/delta)
      predicts 2.483 at the witness excess vs measured 2.988: the
      0.505 miss exceeds the frozen 0.5 bar by 0.005.
  G21 census -- the frozen counts (0 off-line below 30, 1 below 45)
      are FALSIFIED: FOUR off-line pairs live below 45 (0.9330 +
      15.6682i the DRIVER with 26x the witness excess, 0.9377 +
      29.9834i, the round-117 witness 0.6969 + 36.3741i, 0.8232 +
      44.0001i); the witness was never gamma-minimal.
This module gates that the recomputed/pinned numbers reproduce
EXACTLY this failure pattern (check D3) -- no bar is retro-moved.

PINNING DISCLOSURE (the recomputed/pinned split, exact):
  RECOMPUTED IN-RUN: the exact r_Q lattice sieve with the exact ward
  r_Q = 1*chi_-20 + chi_-4*chi_5 (all n <= 4000) and
  r_Q' = t - u >= 0; the Euler ward (the same recursion on the ideal
  counts reproduces Lambda_K exactly); the exact-rational symbolic
  ward (n <= 48); the Dirichlet three-route ward at s = 6.5/16.5;
  the arch gauge identity with exact psi-form tail + a_Q + psi(1/2)
  + S_Q(0) exact + the S_Q'' density ward; the world atom censuses
  (Q 435, ZK 676 at log n < 8); the Q death (eigenvalue crossing
  k_dagger = 998), the mesh mate, the ZK prefix positivity to
  L = 4.0, the Q-scramble death; the FULL certificate (pad rule,
  k_cert = 1038, the eigenvector, its sha, V at dps 80 AND 110 with
  the printed error budget), the frequency-attribution peak
  lambda* = 3.40, the certificate's positivity on the ZK null, the
  conditioning response, the Euler-region bound B(1.6) < 1, the
  round-117 window formula at the pinned witness and driver, and
  the pre-declared failure pattern of G18/G19/G21.
  PINNED FROM RUN-OF-RECORD (epstein_collapse_probe.py, frozen SPEC
  SHA bb51d1a3299f4f62, 27/30 with exactly G18/G19/G21 failing,
  968.8 s, re-run reproduced identically; run-of-record
  epstein_collapse_probe.run3.log): the TRUE and ZK completions
  through L = 8.0 (the ~1000 s Szego ladder at dps 80 on n = 2667
  rows, not re-runnable in-suite at minutes scale; the ZK
  lambda_min(T_997) = 4.785e-3 anchor IS recomputed and gated
  here), the Szego death index fail_k = 996, the located off-line
  census and witness refinement (audit-side incomplete-gamma
  machinery), the plant-ladder law fit (1.875, 0.374), the
  attribution-control deaths (2.970 / 4.428 / 5.457), the
  SMOOTH/SCRARITH round-90 control radii (0.267/0.741), and the
  min-cut record (flows 4/4, classes {MEAS, OMEGA-POS}, no path
  from the falsifier into RH).

NOT RH EVIDENCE -- in either direction.  This module says NOTHING
about the Riemann Hypothesis for zeta: the min-cut is unchanged
(flows 4/4, the falsifier node has no path into RH or R4-HYP); a
detector is a falsifier, not a prover; for zeta the same instrument
at any finite window proves nothing (the all-m/dense-a/all-L omega
absorbs every finite certificate).  What it supplies is a validated
falsification instrument: any world whose sieve data collapse is
CERTIFIED non-RH-like, with measured cost t_death ~ 1.87 +
0.37 ln(1/delta) and source price e^t sieve atoms.  NO RH CLAIM.

PROVENANCE: discovery probe epstein_collapse_probe.py (round 123,
note CDXXIV, contract PRIME.KR4.EPSTEIN.COLLAPSE.01, SPEC_SHA
bb51d1a3299f4f62, 27/30 with the three pre-declared fails, 968.8 s,
verdict EPQC-FIRES-UNATTRIBUTED + LAW-MEASURED + RATE-SILENT +
MINCUT-UNCHANGED + CONTROLS + Z1-CLEAN; re-run green-as-typed at
promotion with identical SPEC_SHA and identical failing set);
instrument lineage rounds 90/117/118/120.  Python-only per
GATE.WOLFRAM.02 (mpmath rows, LAPACK eigenvectors, sieve).
"""
from __future__ import annotations

import hashlib
import math
import time
from fractions import Fraction

import mpmath as mp
import numpy as np

T_ALL = time.time()

# ------------------------------------------------------------ frozen pins
SPEC_SHA_PROBE = "bb51d1a3299f4f62"     # frozen probe spec (run-of-record)
DPS_ROW = 90
DPS_LAM = 120
D3, D6 = "0.003", "0.006"
L_BUILD = 3.6                  # recomputed prefix window (covers k_cert)
L_ZK = 4.0                     # recomputed null prefix (> t_death + 1.0)
L_MAX_RECORD = 8.0             # run-of-record window (completions pinned)
NCUT_ATOMS = 2980              # e^{8.0} = 2980.96: full atom table
NCUT_WARD = 4000
NCUT_EULER = 1200
SYMB_N = 48
PAD_SET = (40, 80, 160, 320)
ERR_G_ABS = 1e-76
BAR_CERT_VAL = -1e-6
BAR_CERT_BUDGET_FAC = 1e6
BAR_CERT_2DPS = 1e-40
BAR_SZEGO_EIG = 12
BAR_DEATH_MESH = 0.15
BAR_EULER = 1e-90
BAR_SYMB = 1e-40
BAR_ARCH_EXACT = 1e-30
BAR_LAM_DIR = 1e-12
BAR_LAM_DEEP = 1e-25
BAR_COND_HI = 1e-8

# run-of-record pins (epstein_collapse_probe.run3.log, 27/30)
PIN_T_DEATH = 2.988            # Szego death, fail_k = 996 at dps 80
PIN_FAIL_K = 996
PIN_K_DAGGER = 998             # eigenvalue crossing (t = 2.994)
PIN_K_DAGGER6 = 503            # mesh-mate eigenvalue crossing (0.006)
PIN_SZ_K6 = 501                # mesh-mate Szego death (t = 3.006)
PIN_T_PRED_R120 = 2.81         # round-120 log-law point prediction
PIN_K_CERT = 1038
PIN_LAM_CERT = -1.969749e-2
PIN_V = "-0.0196974946787"     # dps-80 record value
PIN_V_BUDGET_MAX = 5e-68       # record budget 4.3e-68
PIN_X_SHA = "b01436d53d2cbbee"
PIN_LAM_PEAK = 3.40            # certificate frequency peak (collective)
PIN_ATOMS_Q = 435
PIN_ATOMS_ZK = 676
PIN_ZK_LMIN_997 = 4.785e-3     # ZK float64 lambda_min(T_997) anchor
PIN_QSCR_DEATH = 2.727
PIN_LAW = (1.875, 0.374)       # measured t_death = A + B ln(1/delta)
PIN_LAW_BAR = 0.5              # frozen G19 bar (missed by 0.005)
PIN_QMW_DEATH = 2.970          # Q-minus-witness (G18 FAIL: COLLECTIVE)
PIN_QMALL_DEATH = 4.428        # Q minus all located pairs (survives)
PIN_ZKPLANT_DEATH = 5.457
# witness (round 117) and the located off-line census (round 123)
PIN_WITNESS = ("0.1969270453", "36.3740636864")     # (delta, gamma)
PIN_WIT_WINDOW = (1308.9, 1337.5)
PIN_DRIVER = ("0.4330", "15.6682")
PIN_DRV_WINDOW = (232.6, 259.7)
PIN_OFFLINE = ((0.9330, 15.6682), (0.9377, 29.9834),
               (0.6969, 36.3741), (0.8232, 44.0001))
# Euler-region bound pin: the N = 20000 truncation of
# sum_{n>=4} r_Q(n) n^-1.6 / r_Q(1) PLUS the declared Abel-model
# tail 6 s/(s-1) N^{1-s} (epstein_collapse G21 read) -- NOT the
# full-table value of the sum: the true full sum is 0.645728
# (bughunt III, round 130, note CDXXXII: own 4-decade ladder
# N = 4e3..4e6, spread 8e-7); v917's 0.650 is the same
# construction at N = 2e5.  Both reads are valid UPPER bounds < 1,
# so the D1 gate logic stands unchanged.
PIN_EULER_BOUND = 0.664
# min-cut record (extension nodes + the four cut edges; no RH path)
MINCUT_EDGES = (("UNCOND", "EPQ-SIEVE-MEAS"),
                ("EPQ-SIEVE-MEAS", "EPQ-COLLAPSE-CERT"),
                ("EPQ-COLLAPSE-CERT", "KR4-FALSIFIER-VALIDATED"),
                ("UNCOND", "WEYL-PINS-MEAS"),
                ("HAUS-CELLS-FIN", "FORMA-HYP"),
                ("PICK-FLOORS-FIN", "SV-HYP"),
                ("DIAG-BOUNDS-FIN", "R4-HYP"))

N_CHECKS = 20
EXPECTED = "EPSTEIN-WEIL-VIOLATION-CERTIFIED(V = -1.9697e-2 @ " \
    "t <= 3.114 from r_Q counts alone; controls complete; " \
    "COND-CLASSICAL step cited; NOT RH evidence)"

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


# ------------------------------------------------------------ the sieve
CHI20 = {1: 1, 3: 1, 7: 1, 9: 1, 11: -1, 13: -1, 17: -1, 19: -1}
CHI4 = {1: 1, 3: -1}
CHI5 = {1: 1, 2: -1, 3: -1, 4: 1}


def sieve_rq(ncut):
    """r_Q(n) = #{(x,y): x^2 + 5y^2 = n}, exact lattice count."""
    r = [0] * (ncut + 1)
    b = 0
    while 5 * b * b <= ncut:
        a = 0
        while a * a + 5 * b * b <= ncut:
            q = a * a + 5 * b * b
            if q >= 1:
                r[q] += (2 if a else 1) * (2 if b else 1)
            a += 1
        b += 1
    return r


def sieve_rqp(ncut):
    """r_{Q'}(n) for Q' = 2x^2 + 2xy + 3y^2 (both signs, all pairs)."""
    r = [0] * (ncut + 1)
    ymax = int(math.isqrt(2 * ncut // 5) + 2)
    for y in range(-ymax, ymax + 1):
        xmax = int(math.isqrt(ncut) + abs(y) + 2)
        for x in range(-xmax, xmax + 1):
            q = 2 * x * x + 2 * x * y + 3 * y * y
            if 1 <= q <= ncut:
                r[q] += 1
    return r


def sieve_tu(ncut):
    """t = 1 * chi_{-20} (ideal counts), u = chi_{-4} * chi_5 (genus)."""
    t = [0] * (ncut + 1)
    u = [0] * (ncut + 1)
    for d in range(1, ncut + 1):
        c20v = CHI20.get(d % 20, 0)
        c4 = CHI4.get(d % 4, 0)
        for m in range(d, ncut + 1, d):
            if c20v:
                t[m] += c20v
            if c4:
                u[m] += c4 * CHI5.get((m // d) % 5, 0)
    return t, u


def lam_from_coeffs(r, ncut, dps):
    """r(1) Lam(n) = r(n) log n - sum_{e|n,1<e<n} Lam(e) r(n/e)."""
    with mp.workdps(dps):
        lam = [mp.mpf(0)] * (ncut + 1)
        pre = [mp.mpf(0)] * (ncut + 1)
        r1 = mp.mpf(r[1])
        logs = {}
        for n in range(2, ncut + 1):
            if n not in logs:
                logs[n] = mp.log(n)
            lam[n] = (r[n] * logs[n] - pre[n]) / r1
            if lam[n] != 0:
                ln = lam[n]
                for m in range(2 * n, ncut + 1, n):
                    if r[m // n]:
                        pre[m] += ln * r[m // n]
    return lam


def lam_euler_k(ncut, dps):
    """Lambda of zeta_K = zeta L_{-20}: (1 + chi(p)^k) log p on p^k."""
    with mp.workdps(dps):
        lam = [mp.mpf(0)] * (ncut + 1)
        comp = np.zeros(ncut + 1, dtype=bool)
        for p in range(2, ncut + 1):
            if comp[p]:
                continue
            comp[p * p:: p] = True
            chi = CHI20.get(p % 20, 0)
            lp = mp.log(p)
            q, k = p, 1
            while q <= ncut:
                lam[q] = (1 + chi ** k) * lp
                q *= p
                k += 1
    return lam


# ------------------------------------------------------------ arch layer
MPQ: dict = {}
SQ_CACHE: dict = {}


def sq_setup():
    with mp.workdps(DPS_ROW + 20):
        MPQ["C20"] = mp.log(mp.sqrt(20) / (2 * mp.pi))
        MPQ["AQ"] = -mp.digamma(mp.mpf(1) / 2) - MPQ["C20"]
        MPQ["SQ0"] = mp.pi ** 2 / 2


def sq_arch_mp(m_idx):
    """S_Q(t) = e^{-t/2} Phi(e^{-t}, 2, 1/2) at t = m_idx * 0.003."""
    if m_idx in SQ_CACHE:
        return SQ_CACHE[m_idx]
    with mp.workdps(DPS_ROW + 10):
        t = mp.mpf(m_idx) * mp.mpf("0.003")
        if m_idx == 0:
            v = MPQ["SQ0"]
        elif t >= mp.mpf("0.3"):
            z = mp.exp(-t)
            tot = mp.mpf(0)
            zp = mp.exp(-t / 2)
            k = 0
            floor = mp.mpf(10) ** (-(DPS_ROW + 8))
            while zp / (k + mp.mpf(1) / 2) ** 2 > floor * (1 + tot):
                tot += zp / (k + mp.mpf(1) / 2) ** 2
                k += 1
                zp *= z
            v = tot
        else:
            v = mp.exp(-t / 2) * mp.lerchphi(mp.exp(-t), 2,
                                             mp.mpf(1) / 2)
    SQ_CACHE[m_idx] = v
    return v


def build_lags_c20(L, delta_name, atoms):
    """Lag row of a conductor-20 world: pole layer + atoms (u_float,
    w_mp) + the Gamma(s) arch layer; exact second differences."""
    with mp.workdps(DPS_ROW + 10):
        dl = mp.mpf(delta_name)
        step = int(round(float(delta_name) / 0.003))
        n = int(round(L / float(delta_name)))
        aq, sq0 = MPQ["AQ"], MPQ["SQ0"]
        gvals = []
        ai = 0
        wsum = mp.mpf(0)
        uwsum = mp.mpf(0)
        for j in range(n + 1):
            t = mp.mpf(j) * dl
            while ai < len(atoms) and atoms[ai][0] < t:
                u, w = atoms[ai]
                wsum += w
                uwsum += w * mp.mpf(u)
                ai += 1
            v = -8 * (mp.cosh(t / 2) - 1) + (t * wsum - uwsum) \
                + aq * t - sq0 + sq_arch_mp(j * step)
            gvals.append(v)
        row = [(-2 * gvals[1] / dl)]
        for d in range(1, n):
            row.append(-(gvals[d - 1] - 2 * gvals[d] + gvals[d + 1]) / dl)
    return row


def first_negative_k(row_f, kmax):
    """Smallest k with lambda_min(T_k) < 0 (coarse scan + bisection)."""
    ks = []
    k = 64
    while k < kmax:
        ks.append(k)
        k = int(k * 1.4) + 8
    ks.append(kmax)
    lo, hi = 8, -1
    for k in ks:
        T = row_f[np.abs(np.subtract.outer(np.arange(k), np.arange(k)))]
        if np.linalg.eigvalsh(T)[0] < 0:
            hi = k
            break
        lo = k
    if hi < 0:
        return -1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        T = row_f[np.abs(np.subtract.outer(np.arange(mid),
                                           np.arange(mid)))]
        if np.linalg.eigvalsh(T)[0] < 0:
            hi = mid
        else:
            lo = mid
    return hi


def quadform_mp(row, x, dps):
    """x^T T x on the EXACT mp row (autocorrelation of the 53-bit x
    is exact at dps >= ~45); returns (value, sum|w_d| weight)."""
    k = len(x)
    with mp.workdps(dps):
        xs = [mp.mpf(float(v)) for v in x]
        val = mp.mpf(0)
        wsum = mp.mpf(0)
        for d in range(k):
            wd = mp.fsum(xs[i] * xs[i + d] for i in range(k - d))
            fac = 1 if d == 0 else 2
            val += fac * wd * row[d]
            wsum += fac * abs(wd)
        return val, wsum


def window_formula(delta_s, gamma_s, dps=60):
    """Round-117 exact violation window a+- = 3d^2 + g^2 +-
    2d sqrt(2d^2 + g^2)."""
    with mp.workdps(dps):
        d = mp.mpf(delta_s)
        g = mp.mpf(gamma_s)
        disc = mp.sqrt(2 * d * d + g * g)
        return (float(3 * d * d + g * g - 2 * d * disc),
                float(3 * d * d + g * g + 2 * d * disc))


def part():
    # ================================================ A: sieve + wards
    section("A. THE LAMBDA_Q SIEVE + EXACT WARDS (all recomputed)")
    t0 = time.time()
    rq = sieve_rq(NCUT_WARD)
    rqp = sieve_rqp(NCUT_WARD)
    tt, uu = sieve_tu(NCUT_WARD)
    dec_ok = all(rq[n] == tt[n] + uu[n] for n in range(1, NCUT_WARD + 1))
    genus_ok = all(rqp[n] == tt[n] - uu[n] and rqp[n] >= 0
                   for n in range(1, NCUT_WARD + 1))
    check("A1 r_Q = t + u and r_Q' = t - u >= 0 exact",
          dec_ok and genus_ok and rq[1] == 2 and rq[5] == 2
          and rq[21] == 8,
          "all n <= %d exact integers; r_Q(1)=2, r_Q(5)=2, r_Q(21)=8 "
          "(%.1f s)" % (NCUT_WARD, time.time() - t0))

    lam_k_euler = lam_euler_k(NCUT_EULER, DPS_LAM)
    lam_k_rec = lam_from_coeffs(tt[:NCUT_EULER + 1], NCUT_EULER, DPS_LAM)
    with mp.workdps(DPS_LAM):
        worst_e = max(float(abs(lam_k_rec[n] - lam_k_euler[n]))
                      for n in range(2, NCUT_EULER + 1))
    check("A2 Euler ward: recursion on ideal counts == Lambda_K",
          worst_e <= BAR_EULER,
          "n <= %d, worst dev %.1e (bar %.0e): the recursion is the "
          "classical von Mangoldt on the Euler-product world"
          % (NCUT_EULER, worst_e, BAR_EULER))

    lam_q = lam_from_coeffs(rq[:NCUT_ATOMS + 1], NCUT_ATOMS, DPS_LAM)
    primes48 = [p for p in range(2, SYMB_N + 1)
                if all(p % d for d in range(2, p))]

    def logvec(n):
        out = {}
        m = n
        for p in primes48:
            while m % p == 0:
                out[p] = out.get(p, Fraction(0)) + 1
                m //= p
        return out

    lam_sym = {}
    for n in range(2, SYMB_N + 1):
        acc = {p: Fraction(rq[n]) * v for p, v in logvec(n).items()}
        for e in range(2, n):
            if n % e == 0 and e in lam_sym and rq[n // e]:
                for p, v in lam_sym[e].items():
                    acc[p] = acc.get(p, Fraction(0)) - v * rq[n // e]
        lam_sym[n] = {p: v / rq[1] for p, v in acc.items()}
    worst_s = 0.0
    with mp.workdps(DPS_LAM):
        lp = {p: mp.log(p) for p in primes48}
        for n in range(2, SYMB_N + 1):
            val = mp.fsum(mp.mpf(v.numerator) / v.denominator * lp[p]
                          for p, v in lam_sym[n].items()) \
                if lam_sym[n] else mp.mpf(0)
            sc = max(1.0, abs(float(val)))
            worst_s = max(worst_s, float(abs(val - lam_q[n])) / sc)
    check("A3 symbolic ward: exact-rational log-basis recursion",
          worst_s <= BAR_SYMB,
          "n <= %d in Fractions vs mp table: worst rel %.1e (bar %.0e)"
          % (SYMB_N, worst_s, BAR_SYMB))

    sq_setup()
    with mp.workdps(DPS_LAM):
        psi_half = mp.digamma(mp.mpf(1) / 2)
        exact_ok = float(abs(psi_half + mp.euler + 2 * mp.log(2)))
        sq0_ok = float(abs(MPQ["SQ0"] - mp.pi ** 2 / 2))
        # gauge identity sigma^2 LS_Q(sigma) - sigma S_Q(0)
        #   = -(psi(sigma + 1/2) - psi(1/2)) at sigma = 6
        # LS_Q(s) = int_0^inf S_Q(t) e^{-s t} dt
        #         = sum_k 1/((k + 1/2)^2 (s + k + 1/2)); exact psi tail
        s6 = mp.mpf(6)
        acc = mp.mpf(0)
        for k in range(200):
            kh = k + mp.mpf(1) / 2
            acc += 1 / (kh * kh * (s6 + kh))
        # tail: 1/((k+1/2)^2 (s+k+1/2)) = [1/(k+1/2)^2 - closed psi form]
        # exact closed tail via partial fractions:
        #   1/(x^2 (s + x)) = 1/(s x^2) - 1/(s^2 x) + 1/(s^2 (s + x))
        k0 = mp.mpf(200) + mp.mpf(1) / 2
        tail = (mp.zeta(2, k0) / s6
                + (mp.digamma(k0) - mp.digamma(s6 + k0)) / (s6 * s6))
        ls = acc + tail
        lhs = s6 * s6 * ls - s6 * MPQ["SQ0"]
        rhs = -(mp.digamma(s6 + mp.mpf(1) / 2) - psi_half)
        gauge_dev = float(abs(lhs - rhs))
    check("A4 arch layer exact: psi(1/2), S_Q(0), gauge identity",
          exact_ok <= 1e-110 and sq0_ok <= 1e-100
          and gauge_dev <= BAR_ARCH_EXACT,
          "psi(1/2) = -gamma - 2 log 2 dev %.0e; S_Q(0) = pi^2/2 dev "
          "%.0e; gauge identity at sigma = 6 dev %.1e (bar %.0e, "
          "exact psi-form tail)" % (exact_ok, sq0_ok, gauge_dev,
                                    BAR_ARCH_EXACT))

    with mp.workdps(130):
        dens_dev = 0.0
        h = mp.mpf("1e-25")
        for ts in ("0.5", "1.5", "3.0"):
            t = mp.mpf(ts)

            def sq_at(tv):
                z = mp.exp(-tv)
                tot = mp.mpf(0)
                zp = mp.exp(-tv / 2)
                k = 0
                while zp / (k + mp.mpf(1) / 2) ** 2 \
                        > mp.mpf(10) ** -128 * (1 + tot):
                    tot += zp / (k + mp.mpf(1) / 2) ** 2
                    k += 1
                    zp *= z
                return tot

            fd = (sq_at(t - h) - 2 * sq_at(t) + sq_at(t + h)) / (h * h)
            rho = mp.exp(-t / 2) / (1 - mp.exp(-t))
            dens_dev = max(dens_dev, float(abs(fd - rho)))
    check("A5 S_Q'' density ward: S_Q'' = e^{-t/2}/(1 - e^{-t})",
          dens_dev <= 1e-40,
          "FD second difference vs closed density at t = 0.5/1.5/3.0: "
          "worst dev %.1e" % dens_dev)

    with mp.workdps(DPS_LAM):
        dir_dev = deep_dev = 0.0
        for s_str, bar, lab in (("6.5", BAR_LAM_DIR, "s=6.5"),
                                ("16.5", BAR_LAM_DEEP, "s=16.5")):
            s = mp.mpf(s_str)
            zdir = mp.fsum(-rq[n] * mp.log(n) * mp.power(n, -s)
                           for n in range(2, NCUT_WARD + 1))
            zden = mp.fsum(rq[n] * mp.power(n, -s)
                           for n in range(1, NCUT_WARD + 1))
            route_dir = zdir / zden
            route_lam = -mp.fsum(lam_q[n] * mp.power(n, -s)
                                 for n in range(2, NCUT_ATOMS + 1))
            # shared truncation tail (measured, added to the bar)
            tail = float(abs(rq[NCUT_WARD] * mp.log(NCUT_WARD)
                             * mp.power(NCUT_WARD, -s))) * NCUT_WARD
            dev = float(abs(route_dir - route_lam))
            if s_str == "6.5":
                dir_dev, dir_bar = dev, bar + 3 * tail
            else:
                deep_dev, deep_bar = dev, bar + 3 * tail
    check("A6 Dirichlet two-route ward: Z_Q'/Z_Q from r vs Lambda",
          dir_dev <= dir_bar and deep_dev <= deep_bar,
          "s=6.5 dev %.1e (bar %.1e); s=16.5 dev %.1e (bar %.1e)"
          % (dir_dev, dir_bar, deep_dev, deep_bar))

    # ================================================ B: the collapse
    section("B. THE COLLAPSE (Q dies, the matched null completes)")
    # ZK atoms exactly as the probe: the RECURSION table on the ideal
    # counts (its sub-1e-119 composite residuals are numerically inert
    # but count as table atoms -- probe convention, reproduced)
    lam_k_rec = lam_from_coeffs(tt[:NCUT_ATOMS + 1], NCUT_ATOMS,
                                DPS_LAM)
    with mp.workdps(DPS_ROW + 10):
        atoms_q = []
        atoms_k = []
        for n in range(2, NCUT_ATOMS + 1):
            u = float(mp.log(n))
            if u >= L_MAX_RECORD:
                break
            if lam_q[n] != 0:
                atoms_q.append((u, lam_q[n] / mp.sqrt(n)))
        for n in range(2, NCUT_ATOMS + 1):
            u = float(mp.log(n))
            if u >= L_MAX_RECORD:
                break
            if lam_k_rec[n] != 0:
                atoms_k.append((u, lam_k_rec[n] / mp.sqrt(n)))
    check("B1 world atom censuses (log n < 8.0)",
          len(atoms_q) == PIN_ATOMS_Q and len(atoms_k) == PIN_ATOMS_ZK,
          "Q %d (all n, no Euler product; pinned %d), ZK %d (prime-"
          "power table atoms, probe convention; pinned %d)"
          % (len(atoms_q), PIN_ATOMS_Q, len(atoms_k), PIN_ATOMS_ZK))

    t0 = time.time()
    row_q = build_lags_c20(L_BUILD, D3, atoms_q)
    row_f = np.array([float(v) for v in row_q])
    k_dag = first_negative_k(row_f, len(row_f))
    check("B2 Q dies: eigenvalue crossing k_dagger recomputed",
          k_dag == PIN_K_DAGGER
          and abs(k_dag - PIN_FAIL_K) <= BAR_SZEGO_EIG,
          "k_dagger = %d (t = %.3f; pinned %d), |k_dagger - szego "
          "fail_k %d| = %d <= %d; pinned Szego t_death = %.3f "
          "(round-120 log-law prediction %.2f) (%.1f s)"
          % (k_dag, k_dag * 0.003, PIN_K_DAGGER, PIN_FAIL_K,
             abs(k_dag - PIN_FAIL_K), BAR_SZEGO_EIG, PIN_T_DEATH,
             PIN_T_PRED_R120, time.time() - t0))

    row_q6 = build_lags_c20(L_BUILD, D6, atoms_q)
    row_f6 = np.array([float(v) for v in row_q6])
    k_dag6 = first_negative_k(row_f6, len(row_f6))
    check("B3 mesh mate delta = 0.006: death stable",
          k_dag6 == PIN_K_DAGGER6
          and abs(k_dag6 - PIN_SZ_K6) <= BAR_SZEGO_EIG
          and abs(k_dag6 * 0.006 - PIN_T_DEATH) <= BAR_DEATH_MESH,
          "eigenvalue crossing k = %d (t = %.3f; pinned %d; Szego "
          "record %d -> 3.006 within the %d-bin bar); |t6 - t_death| "
          "= %.3f <= %.2f" % (k_dag6, k_dag6 * 0.006, PIN_K_DAGGER6,
                              PIN_SZ_K6, BAR_SZEGO_EIG,
                              abs(k_dag6 * 0.006 - PIN_T_DEATH),
                              BAR_DEATH_MESH))

    t0 = time.time()
    row_zk = build_lags_c20(L_ZK, D3, atoms_k)
    row_zf = np.array([float(v) for v in row_zk])
    kz = len(row_zf)
    Tz = row_zf[np.abs(np.subtract.outer(np.arange(kz), np.arange(kz)))]
    lam_zk_full = float(np.linalg.eigvalsh(Tz)[0])
    T997 = row_zf[np.abs(np.subtract.outer(np.arange(997),
                                           np.arange(997)))]
    lam_zk_997 = float(np.linalg.eigvalsh(T997)[0])
    check("B4 ZK matched null POSITIVE through L = 4.0 (recomputed); "
          "L = 8.0 pinned",
          lam_zk_full > 0
          and abs(lam_zk_997 / PIN_ZK_LMIN_997 - 1) <= 1e-3,
          "lambda_min(T_%d) = %.3e > 0 (t = %.1f > t_death + 1.0); "
          "anchor lambda_min(T_997) = %.4e (pinned %.4e); TRUE and ZK "
          "complete through 8.0 in the run-of-record (%.1f s)"
          % (kz, lam_zk_full, L_ZK, lam_zk_997, PIN_ZK_LMIN_997,
             time.time() - t0))

    with mp.workdps(DPS_ROW + 10):
        atoms_scr = [(u, w) for (u, _), w in
                     zip(atoms_q, [w for _u, w in atoms_q][::-1])]
    row_scr = build_lags_c20(L_BUILD, D3, atoms_scr)
    row_sf = np.array([float(v) for v in row_scr])
    k_scr = first_negative_k(row_sf, len(row_sf))
    check("B5 Q-scramble control dies (weights reversed)",
          k_scr > 0 and abs(k_scr * 0.003 - PIN_QSCR_DEATH) <= 0.01,
          "t = %.3f (pinned %.3f): the death needs the exact "
          "weight-position pairing, not the weight multiset"
          % (k_scr * 0.003, PIN_QSCR_DEATH))

    # ================================================ C: the certificate
    section("C. THE CERTIFIED QUADRATIC FORM (the promoted object)")
    k_cert = -1
    lam_c = 0.0
    x = None
    for pad in PAD_SET:
        k_cert = min(k_dag + pad, len(row_f))
        T = row_f[np.abs(np.subtract.outer(np.arange(k_cert),
                                           np.arange(k_cert)))]
        evals, evecs = np.linalg.eigh(T)
        lam_c = float(evals[0])
        if lam_c <= -1e-5:
            x = np.ascontiguousarray(evecs[:, 0])
            break
    xsha = hashlib.sha256(x.tobytes()).hexdigest()[:16]
    unit = abs(float(np.linalg.norm(x)) - 1.0)
    check("C1 certificate vector: pad rule, unit norm, sha pinned",
          k_cert == PIN_K_CERT and unit <= 1e-12
          and abs(lam_c / PIN_LAM_CERT - 1) <= 1e-5
          and xsha == PIN_X_SHA,
          "k_cert = %d (pinned %d), |x| - 1 = %.1e, float lambda_min "
          "= %.6e (pinned %.6e), sha %s (pinned %s)"
          % (k_cert, PIN_K_CERT, unit, lam_c, PIN_LAM_CERT, xsha,
             PIN_X_SHA))

    t0 = time.time()
    val, wsum = quadform_mp(row_q, x, 80)
    val2, _w2 = quadform_mp(row_q, x, 110)
    with mp.workdps(80):
        gmax = max(500.0, 8 * math.cosh(L_MAX_RECORD / 2))
        budget = float(wsum) * 4 * ERR_G_ABS * gmax / 0.003
        rel2 = float(abs(val - val2) / max(abs(val), mp.mpf("1e-300")))
        vdev = float(abs(val / mp.mpf(PIN_V) - 1))
    check("C2 V = x^T T x CERTIFIED NEGATIVE (dps 80/110 + budget)",
          float(val) <= BAR_CERT_VAL
          and abs(float(val)) >= BAR_CERT_BUDGET_FAC * budget
          and budget <= PIN_V_BUDGET_MAX and rel2 <= BAR_CERT_2DPS
          and vdev <= 1e-9,
          "V = %.10e (record %s, rel dev %.1e); budget %.1e <= %.0e; "
          "two-dps rel %.1e <= %.0e: windowed Weil positivity for "
          "xi_Q FAILS at t <= %.3f (%.1f s)"
          % (float(val), PIN_V, vdev, budget, PIN_V_BUDGET_MAX, rel2,
             BAR_CERT_2DPS, k_cert * 0.003, time.time() - t0))

    lam_grid = np.arange(0.0, 80.0, 0.05)
    ph = np.exp(1j * np.outer(lam_grid, 0.003 * np.arange(k_cert)))
    spec = np.abs(ph @ x) ** 2
    lam_peak = float(lam_grid[int(np.argmax(spec))])
    check("C3 frequency attribution: peak far from the witness",
          abs(lam_peak - PIN_LAM_PEAK) <= 0.1
          and abs(lam_peak - float(PIN_WITNESS[1])) > 1.5,
          "lambda* = %.2f (pinned %.2f) vs witness gamma = %s: the "
          "violating test function targets a DIFFERENT spectral "
          "region -- collective/other zeros (the G18 finding)"
          % (lam_peak, PIN_LAM_PEAK, PIN_WITNESS[1]))

    with mp.workdps(80):
        pert = mp.mpf(1) + mp.mpf("1e-25")
        row_p = [v * pert for v in row_q]
    val_p, _wp = quadform_mp(row_p, x, 80)
    with mp.workdps(80):
        shift = float(abs(val_p - val))
    check("C4 conditioning: nonzero bounded response",
          0.0 < shift <= BAR_COND_HI,
          "1e-25 row perturbation shifts V by %.2e in (0, %.0e]: the "
          "round-120 exactly-zero red flag gated from both sides"
          % (shift, BAR_COND_HI))

    tv_zk, _wz = quadform_mp(row_zk, x, 80)
    check("C5 the same vector reads POSITIVE on the matched null",
          float(tv_zk) > 0,
          "x^T T_ZK x = %.6e > 0 (ZK row, same test function): the "
          "certificate fires on Q and not on the conductor-matched "
          "GRH-expected null" % float(tv_zk))

    # ================================================ D: context + typing
    section("D. CENSUS CONTEXT, PRE-DECLARED FAILURES, NOT-RH TYPING")
    with mp.workdps(60):
        s = mp.mpf("1.6")
        bsum = mp.fsum(rq[n] * mp.power(n, -s)
                       for n in range(4, NCUT_WARD + 1)) / rq[1]
        # Abel tail with the rigorous lattice-count envelope
        # R(x) = sum_{n <= x} r_Q(n) <= (2 sqrt x + 1)(2 sqrt(x/5) + 1)
        #      <= (4/sqrt 5) x + 5 sqrt x  (x >= 1), so
        # sum_{n > N} r n^{-s} <= s int_N^inf R(x) x^{-s-1} dx
        N = mp.mpf(NCUT_WARD)
        c_lin = 4 / mp.sqrt(5)
        tailb = s * (c_lin * mp.power(N, 1 - s) / (s - 1)
                     + 5 * mp.power(N, mp.mpf("0.5") - s)
                     / (s - mp.mpf("0.5")))
        b_tot = float(bsum + tailb / rq[1])
    check("D1 Euler-region bound B(1.6) < 1 (no zeros Re s >= 1.6)",
          0.55 <= float(bsum) <= PIN_EULER_BOUND + 0.01 and b_tot < 1,
          "sum_{4<=n<=%d} r_Q n^-1.6 / r_Q(1) = %.3f (pin %.3f = "
          "N=2e4 truncation + declared Abel-model tail, NOT the full-"
          "table value -- true full sum 0.645728, bughunt CDXXXII; "
          "v917's 0.650 = same construction at N=2e5) + rigorous "
          "Abel tail %.3f: total %.3f < 1 "
          "at ALL heights" % (NCUT_WARD, float(bsum), PIN_EULER_BOUND,
                              float(tailb / rq[1]), b_tot))

    w_lo, w_hi = window_formula(PIN_WITNESS[0], PIN_WITNESS[1])
    d_lo, d_hi = window_formula(PIN_DRIVER[0], PIN_DRIVER[1])
    with mp.workdps(60):
        exc_w = float(mp.mpf(PIN_WITNESS[0]) ** 2
                      / mp.mpf(PIN_WITNESS[1]) ** 2)
        exc_d = float(mp.mpf(PIN_DRIVER[0]) ** 2
                      / mp.mpf(PIN_DRIVER[1]) ** 2)
    check("D2 round-117 window formula at the pinned census",
          abs(w_lo - PIN_WIT_WINDOW[0]) <= 0.1
          and abs(w_hi - PIN_WIT_WINDOW[1]) <= 0.1
          and abs(d_lo - PIN_DRV_WINDOW[0]) <= 0.2
          and abs(d_hi - PIN_DRV_WINDOW[1]) <= 0.2
          and d_lo < 245.7 < d_hi and d_lo < 256 < d_hi
          and 25 < exc_d / exc_w < 27,
          "witness window (%.1f, %.1f) [pinned (%.1f, %.1f)]; DRIVER "
          "window (%.1f, %.1f) contains a = 256 and a*; driver excess "
          "%.3e = %.1fx witness %.3e"
          % (w_lo, w_hi, PIN_WIT_WINDOW[0], PIN_WIT_WINDOW[1], d_lo,
             d_hi, exc_d, exc_d / exc_w, exc_w))

    law_pred = PIN_LAW[0] + PIN_LAW[1] * math.log(
        1 / float(PIN_WITNESS[0]))
    law_miss = abs(law_pred - PIN_T_DEATH)
    g18_delta = abs(PIN_QMW_DEATH - PIN_T_DEATH)
    check("D3 the three pre-declared FALSIFIED predictions carried",
          law_miss > PIN_LAW_BAR and law_miss - PIN_LAW_BAR < 0.02
          and g18_delta < 0.05 and PIN_QMALL_DEATH > PIN_T_DEATH + 0.5
          and len(PIN_OFFLINE) == 4,
          "G19: law %.3f + %.3f ln(1/delta) predicts %.3f vs %.3f "
          "(miss %.3f > bar %.1f by %.3f); G18: witness removal moves "
          "the death by only %.3f -> COLLECTIVE (all-located removal "
          "survives to %.3f: LOCATED-SPECTRUM-CARRIES); G21: census "
          "counts falsified -- FOUR off-line pairs below 45, witness "
          "not gamma-minimal" % (PIN_LAW[0], PIN_LAW[1], law_pred,
                                 PIN_T_DEATH, law_miss, PIN_LAW_BAR,
                                 law_miss - PIN_LAW_BAR, g18_delta,
                                 PIN_QMALL_DEATH))

    adj = {}
    for a, b in MINCUT_EDGES:
        adj.setdefault(a, []).append(b)
    seen = {"EPQ-COLLAPSE-CERT"}
    stack = ["EPQ-COLLAPSE-CERT"]
    while stack:
        u = stack.pop()
        for v in adj.get(u, []):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    omega_edges = [e for e in MINCUT_EDGES if e[1].endswith("-HYP")]
    check("D4 min-cut unchanged: the falsifier has NO path into RH",
          "RH" not in seen and "FORMA-HYP" not in seen
          and "R4-HYP" not in seen and "SV-HYP" not in seen
          and len(omega_edges) == 3,
          "BFS from EPQ-COLLAPSE-CERT reaches %d node(s) %s; the "
          "omega cut edges are untouched (record flows 4/4, classes "
          "{MEAS, OMEGA-POS}): a detector is a falsifier, not a "
          "prover -- NOT RH evidence in either direction"
          % (len(seen) - 1, sorted(seen - {"EPQ-COLLAPSE-CERT"})))
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    SQ_CACHE.clear()
    print("=" * 74)
    print("v916 -- PRIME.KR4.EPSTEIN.COLLAPSE.01 (the certified Epstein")
    print("Weil-positivity violation: V = -1.9697e-2 +- 4.3e-68 from "
          "r_Q(n) lattice")
    print("counts alone; sha-pinned test vector, len 1038; TRUE and "
          "zeta_K controls")
    print("complete; Potter--Titchmarsh 1935 zeros -- KNOWN falsehood, "
          "NEW instrument;")
    print("explicit-formula step COND-CLASSICAL; NO RH claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v916: %d/%d checks passed | runtime %.1f s"
          % (n_run - len(fails), n_run, time.time() - T_ALL))
    print("verdict %s" % verdict)
    print("PINNING: sieve + wards + deaths + ZK prefix + FULL "
          "certificate RECOMPUTED;")
    print("the L = 8.0 completions, Szego index, census, law and "
          "attribution PINNED")
    print("from epstein_collapse_probe.run3.log (SPEC %s, 27/30, "
          "G18/G19/G21" % SPEC_SHA_PROBE)
    print("pre-declared fails carried verbatim).  NOT RH evidence; "
          "NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails "
          "(got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, n_run,
             fails or "none"))
    print("--- PRIME.KR4.EPSTEIN.COLLAPSE.01 certified violation: "
          "%d passed, %d failed ---" % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
