#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bughunt2_r86_r105_probe -- PRIME.BUGHUNT2.R86.R105.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  Adversarial audit of the
discovery rounds 86-105 corpus (commits bf9e4779..f121cd65; probes
simple_principle / signpos / stieltjes_vitali_pin / krein_screw /
vbk_invariant / collective_rescue / cohomspec / eulerpick_ladder /
rigidity_inverse / sp_expsum_pricing / ccm_pn_adjudication / the four
round-99 Lean modules / sieve4_eulerpick_n4 + sieve4_helper.c /
screwind_induction / hausdorff_safepoint / moonshot_sol /
levinson_class / roadmap; notes CCCLXXXV-CDVI; synced surfaces paper
S8.12-8.14, prime-front 12.44-12.46, changelog XCIX-CI).  This probe
writes NOTHING but stdout, reads the frozen corpus READ-ONLY, imports
one frozen probe (collective_rescue_probe) as an engine for one
recompute-gate, and makes NO RH CLAIM in either direction.  Every
confirmed finding below carries exactly one falsifiable gate.

METHOD (the round-87 bughunt standard, applied to the never-audited
86-105 corpus): (B1) the load-bearing new theorems re-derived with an
OWN implementation (the round-103 partial theorem's four-partition
bounds; the round-100 N=4 error model and Nair floor; the round-102
Hausdorff continuation identities; the round-92 Euler-Pick backward
typing); (B2) cross-probe number consistency; (B3) AST-level gate
vacuity census; (B4) Lean statement review (executed out-of-band via
scripts/audit.sh, PASS; grep-pinned here); (B5) prose-vs-artifact
claim drift on the synced surfaces; (B6) fresh eyes.

=======================================================================
FINDINGS LEDGER (the deliverable; one gate each; severity frozen)
=======================================================================
BH2-F1 [MINOR][gate-vacuity]  levinson_class_probe.py G0.2 ("spec SHA
  frozen before the run of record") is check(..., True, ...) --
  hardcoded True, counted in the 23/23 run-of-record tally.  This is
  verbatim the round-87 F5 class (which convicted three G0.2
  self-attestations), reproduced in a round-104 probe written AFTER
  that warning.  No mathematical content rides on it; no verdict
  flips.  GATE: AST (G19).
BH2-F2 [MINOR][gate-vacuity]  vbk_invariant_probe.py carries two
  tautological gate conjuncts standing in for "the pin sequence
  accumulates at the interior point 1": V0a line ~661
  abs((1 + 1/10**9) - 1) < 2e-9 and V0c line ~762
  abs((mp.mpf(1) + 1/mp.mpf(10)**20) - 1) < 2e-20.  Both are
  arithmetic tautologies (1e-9 < 2e-9; 1e-20 < 2e-20) that can never
  fail under any computation; the surrounding gates remain live on
  their other conjuncts, and the Montel/normal-families step itself
  is HONESTLY citation-typed (Nicolau 2015/Pick 1916) -- the B1d
  question "gated or asserted" answers: asserted-with-citation,
  disclosed; only the accumulation conjunct is decorative.  GATE:
  AST-extract + evaluate (G20).
BH2-F3 [MINOR][cross-probe number]  screwind_induction_probe.py
  misattributes the mesh triple: its docstring says "0.207/0.184/0.156
  at delta 0.012/0.006/0.003" and its C-section print labels the same
  triple "(round 90: ...)".  RECOMPUTED through the frozen round-93
  engine on the common window [0, 4.8): sup|alpha| at delta = 0.008 is
  0.2065 (the actual source of "0.207": collective_rescue_probe's
  0.008-world, round 93), while the true delta = 0.012 value is 0.2219
  (screwind's own C-section measurement, quoted correctly as
  0.222/0.184/0.156 in the round-101 commit).  Round 90 published only
  0.156 at delta = 0.003.  The MESH-DAMPED verdict stands (0.2219 >
  0.2065 > 0.1839 > 0.156); only the docstring's mesh label and round
  attribution are wrong.  GATE: recompute + grep (G21).
BH2-F4 [MAJOR][claim-drift]  "THREE EQUIVALENT LEMMA FORMS" (paper
  S8.13 title + close, S8.14, prime-front 12.45/12.46, changelog C/CI,
  roadmap S0.3, commits r102/r104/r105) asserts a mathematical
  equivalence that the machine record does not establish per
  direction.  The honest per-form status (each direction cited where
  it lives):
    Form A (Hausdorff cell positivity, all C_{n,k}(256) >= 0):
      RH => A: elementary/proven (y in (0,1); hausdorff probe H1 +
        Pascal identity gates); A => RH: AUDITED-SOUND (H1c chain:
        Hausdorff 1921/Widder III.4a cited, no-atom + moment-Taylor
        gated, continuation step re-derived independently in THIS
        audit with no gap found) + literature (Zhang arXiv:2303.09396
        Thm 2, central point).  A is genuinely RH-equivalent.
    Form B (uniform Weyl-disk contraction of the Krein realization):
      B => RH: skeleton-sound gate-by-gate (svpin r89 17/17; vbk r92
        V0a; SVSkeleton.lean kernel-checks ONLY the composition, all
        three analytic steps named hypotheses/citations).
      RH/Weil => B: OPEN -- this direction IS the round-90 missing
        lemma itself ("let -g'' have positive sections ... then the
        Weyl disks contract": krein r90, stated as the open lemma,
        measured 16/16 truth-tight, never proven).  Calling B an
        "equivalent form" upgrades OPEN to EQUIVALENT.
    Form C (ground-eigenvector sign positions / TPL(i)):
      C <=> ladder positivity: r85 T4 secular reduction, kernel-checked
        in ParityLemma.lean UNDER the named simplicity hypothesis,
        verified on 3 finite rungs; ladder => RH: v848 chain modulo
        hypothesis (H); RH => ladder: Gram/Z1-transfer identity (r84,
        analytic modulo the explicit-formula step, measured 6.3e-5).
      C is RH-equivalent only modulo (H) + simplicity + the finite-rung
        scope.
  Honest phrasing (the corrected sentence): "three lemma forms of the
  one open input, each RH-sufficient with audited skeletons; Form A
  RH-equivalent (audited + cited); Forms B and C RH-equivalent only
  modulo open/measured/hypothesis-conditional converse directions" --
  i.e. pairwise equivalence holds THROUGH RH with individual
  equivalences of varying proof status, not as a machine-established
  pairwise fact.  No number is wrong and no verdict enum flips
  (SUZKREIN-CARRIER-OPEN / HAUSDORFF-EQUIVALENCE-SOUND / the E4
  OPEN marker all stand); the drift is prose-level but headline-level.
  GATE: grep-conjunction pinning the phrase AND the open-direction
  markers in the owning artifacts (G22).
BH2-F5 [MINOR][claim-drift]  The form-B name "UNIFORM Weyl-disk
  contraction" on every synced surface carries the pre-correction
  adjective: round 92 V0a established (and the same surfaces report)
  that POINTWISE contraction at the pins suffices and no sigma-down-
  to-1/2 uniformity is load-bearing.  The stale "uniform" survives
  from the frozen round-90 enum.  GATE: grep both (G23).
BH2-F6 [MINOR][stale acceptance value]  roadmap_probe.py M1b freezes
  the round-95 N=3 interval [2.3643695e-10, 1.1497752e-9] as an
  acceptance value although round 100 (cited in the same probe for
  N=4) tightened lo3 to 6.9310239e-10 with width 1.3e-16 -- the
  acceptance gate is ~3x weaker than the corpus's own certified
  state.  Not an error (both intervals are valid enclosures; owning
  artifacts disclosed); an inconsistent tightness.  GATE: grep +
  numeric compare (G24).
BH2-F7 [MINOR][doc-level error-model slips]  sieve4_helper.c header:
  (a) the accumulation remark "N <= 4e10 => 4Nu^2 < 2e-21" does not
  hold for the run's TOTAL count N_C ~ 3.46e11 (it holds per chunk;
  the probe's enacted Python-side model uses the true N_C, so the
  certificate is unaffected -- recomputed here: 4*N_C*u^2 ~ 1.7e-20,
  still 4 orders below the 32u*S term); (b) two per-step slips:
  cbrt(q) true input-propagation is u/3 (header says 0.5u/3) and f3
  accordingly 4u + A_CBRT + u/3 (header says u/6).  The corrected
  worst-case per-term bound is <= 13.34u under Assumption A -- still
  below the header's own 13.5u claim and far below the frozen
  K_TERM = 32u, so the certificate stands.  GATE: recompute (G18b).

CHECKED CLEAN (adversarially, no finding): the round-103 partial
theorem re-derived with an own implementation (GEO-1/2, the Stieltjes
tail bounds B_0/B_n including the two inner integral inequalities,
the Beta endpoint floor with unimodality, the Rosser packet count
F-diff >= H, all four partition ratios, the k* root); the round-100
tail assembly (Abel identity, Buethe split, Nair band -- Nair's
lcm(1..n) >= 2^{n-1} verified exact for n <= 60 and psi(x) >= (x-2)ln2
against an own sieve), the far-floor necessity numbers, the dd
accumulation bound (simulated against exact rationals), the
certified-lambda logic (Weyl + interval Cholesky + rowsum/Frobenius
norm bound -- both valid upper bounds for ||R||_2 on entrywise-bounded
symmetric perturbations); the Hausdorff H1c continuation step
re-derived (off-axis poles = zeros of the entire order-1/2 Phi, hence
closed + discrete with no finite accumulation point -- accumulation
toward the slit is impossible, toward infinity irrelevant in C;
slit-plane minus a closed countable set stays open + connected;
moment-Taylor identity re-derived by an independent geometric-series
route; genus-0/order bookkeeping consistent); the Euler-Pick backward
direction honestly citation-typed everywhere it appears; the 16-sigma
pin grid literally identical across svpin/krein/hausdorff; the
r = 0.264/0.744 death depths, kappa* ledger, certified floors,
depth-86/gamma*-563 and the k ~ 1.405e19 frontier all cross-probe
consistent; the four Lean modules say exactly what round 99 claims
(pickMatrix_posSemidef quantifies over arbitrary finite real ordinate
families and positive node families -- generic, no zeta content,
disclosed; the ParityLemma simplicity hypothesis is an explicit named
parameter, load-bearing; skeleton_not_unconditional is a genuine
existential witness with RH = False) and scripts/audit.sh returns
AUDIT: PASS with axioms exactly [propext, Classical.choice,
Quot.sound]; all 16 in-scope Python probes re-run green out-of-band
during this audit with verdict enums and headline numbers
bit-similar; the synced-surface numbers grep-match their artifacts.

NO ROUND VERDICT FLIPS.  COMPOSITE: BUGHUNT2-FINDINGS(7, MAJOR).
NO RH CLAIM.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import random
import sys
import time
from fractions import Fraction

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
START = time.time()
U = 2.0 ** -53

CHECKS: list[tuple[str, bool, str]] = []
FINDINGS = [
    ("BH2-F1", "MINOR", "levinson G0.2 hardcoded-True in 23/23 tally"),
    ("BH2-F2", "MINOR", "vbk V0a/V0c tautological accumulation conjuncts"),
    ("BH2-F3", "MINOR", "screwind mesh triple mislabeled 0.012 / round 90"),
    ("BH2-F4", "MAJOR", "'three equivalent lemma forms' status upgrade"),
    ("BH2-F5", "MINOR", "stale 'uniform' in form-B name post-V0a"),
    ("BH2-F6", "MINOR", "roadmap M1b stale r95 N=3 acceptance interval"),
    ("BH2-F7", "MINOR", "sieve4_helper.c header error-model slips"),
]


def check(name: str, ok: bool, detail: str) -> bool:
    result = bool(ok)
    CHECKS.append((name, result, detail))
    print("  [%s] %-46s %s" % ("PASS" if result else "FAIL", name, detail))
    return result


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def blob(name: str) -> str:
    with open(os.path.join(HERE, name), encoding="utf-8",
              errors="replace") as fh:
        return fh.read()


def blob_abs(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


REPO = os.path.abspath(os.path.join(HERE, "..", ".."))


# ===================================================================== B1a
# Independent re-derivation of the round-103 partial theorem.  Own
# implementation: different structure from moonshot_sol/roadmap (log-space
# kernel, quad-validated tail inequalities, sampled monotonicity).
mp.mp.dps = 60
A = mp.mpf(256)
ASH = A - mp.mpf("0.25")
T_PT = mp.mpf("3000175332800")
G1LO, G1HI = mp.mpf("14.1347"), mp.mpf("14.1348")
R = mp.mpf(3) / 2
K19 = mp.mpf(10) ** 19


def rosser_E(t):
    return (mp.mpf("0.137") * mp.log(t)
            + mp.mpf("0.443") * mp.log(mp.log(t)) + mp.mpf("1.588"))


def my_B0():
    return A / mp.pi * (mp.log(T_PT / (2 * mp.pi)) + 1) / T_PT


def my_Bn(n: int):
    return (A * (n + 1) / (2 * mp.pi * n) * mp.log(T_PT / (2 * mp.pi))
            / T_PT * (A / (T_PT ** 2 + ASH)) ** n)


def my_D():
    return min(R ** 2 * mp.exp(-R ** 2), R ** -2 * mp.exp(-R ** -2)) / 2


def log_kernel(n: int, k, gamma):
    """log K_{n,k}(gamma) for an on-line zero."""
    g2 = gamma ** 2
    return ((n + 1) * mp.log(A / (A + g2)) + k * mp.log(g2 / (A + g2)))


def my_H(theta):
    g = mp.sqrt(A * theta)
    return g * (R - 1 / R) / (2 * mp.pi) * mp.log(g / (2 * mp.pi * R))


def b1a_gates() -> None:
    section("B1a  ROUND-103 PARTIAL THEOREM, INDEPENDENT RE-DERIVATION")
    # tail inequality validation at a small scaled T (quad feasible):
    # sum_{gamma>T} f_n <= int_T^inf (t/2pi)log(t/2pi) (-f_n') dt <= B_n(T)
    t_small = mp.mpf(5000)

    def bound_integral(n: int):
        def integ(t):
            fnp = 2 * t * (n + 1) * A ** (n + 1) / (ASH + t ** 2) ** (n + 2)
            return t / (2 * mp.pi) * mp.log(t / (2 * mp.pi)) * fnp
        return mp.quad(integ, [t_small, 10 * t_small, 1000 * t_small,
                               mp.inf])

    def closed_form(n: int):
        if n == 0:
            return A / mp.pi * (mp.log(t_small / (2 * mp.pi)) + 1) / t_small
        return (A * (n + 1) / (2 * mp.pi * n)
                * mp.log(t_small / (2 * mp.pi)) / t_small
                * (A / (t_small ** 2 + ASH)) ** n)

    ok_tail = True
    msgs = []
    for n in (0, 1, 2):
        num = bound_integral(n)
        cf = closed_form(n)
        ok_tail &= num <= cf * (1 + mp.mpf("1e-30"))
        msgs.append("n=%d ratio=%.4f" % (n, float(num / cf)))
    check("G02 tail closed forms dominate the Stieltjes integral",
          ok_tail, "; ".join(msgs) + " (validated at scaled T=5000)")

    b0, b1 = my_B0(), my_Bn(1)
    check("G03 B_0, B_1 match the round-103 record",
          abs(b0 / mp.mpf("7.575655711056e-10") - 1) < mp.mpf("1e-9")
          and b1 < mp.mpf("2.1e-32"),
          "B_0=%s B_1=%s" % (mp.nstr(b0, 10), mp.nstr(b1, 6)))

    # kernel unimodality + endpoint floor on a dense interval sample
    d_const = my_D()
    ok_ker = True
    worst = mp.mpf("inf")
    for n, k in ((0, 25), (0, 10 ** 12), (1, 80), (1, 10 ** 10), (3, 200)):
        theta = mp.mpf(k) / (n + 1)
        if theta < 25:
            continue
        g = mp.sqrt(A * theta)
        floor_log = (n + 1) * mp.log(d_const / theta)
        for j in range(21):
            gamma = g / R + (R * g - g / R) * mp.mpf(j) / 20
            margin = log_kernel(n, mp.mpf(k), gamma) - floor_log
            worst = min(worst, margin)
            ok_ker &= margin >= 0
    check("G04 Beta endpoint floor K >= (D/theta)^(n+1) on I samples",
          ok_ker, "min log-margin over 5 cells x 21 pts = %s"
          % mp.nstr(worst, 4))

    # Rosser packet count: F(rg)-F(g/r) >= H(theta) reduces exactly to
    # (r-1/r)(log r - 1) + (r+1/r) log r > 0; then #I >= H/2 when H>=4E.
    slack = ((R - 1 / R) * (mp.log(R) - 1) + (R + 1 / R) * mp.log(R))
    ok_cnt = slack > 0
    worst_he = mp.mpf("inf")
    for lg in range(0, 20):
        theta = mp.mpf(25) * mp.mpf(10) ** lg
        if theta > K19:
            break
        he = my_H(theta) / (4 * rosser_E(R * mp.sqrt(A * theta)))
        worst_he = min(worst_he, he)
        ok_cnt &= he > 1
    check("G05 count floor: F-diff >= H exactly; H/(4E) > 1 on ladder",
          ok_cnt, "slack=%s; min H/(4E)=%s over theta=25..1e19"
          % (mp.nstr(slack, 4), mp.nstr(worst_he, 5)))

    # the four partition ratios, own numbers vs the round-103/105 record
    y_lo = A / (A + G1HI ** 2)
    q_lo = G1LO ** 2 / (A + G1LO ** 2)
    bridge = y_lo * q_lo ** 24 / b0
    row0 = (my_H(K19) / 2) * d_const / K19 / b0
    low = y_lo ** 2 * q_lo ** 80 / b1
    th_max = K19 / 2
    high = (my_H(th_max) / 2) * (d_const / th_max) ** 2 / b1
    refs = (("bridge", bridge, "1.876981097339"),
            ("row0", row0, "1.176577026464"),
            ("low", low, "335.835448342609"),
            ("high", high, "1416.754103822636"))
    ok_r = all(v > 1 for _n, v, _r in refs)
    ok_m = all(abs(v / mp.mpf(r) - 1) < mp.mpf("1e-9") for _n, v, r in refs)
    check("G06 four partition ratios re-derived, all > 1, record-match",
          ok_r and ok_m,
          " ".join("%s=%s" % (n_, mp.nstr(v, 10)) for n_, v, _ in refs))

    root = mp.findroot(lambda k: (my_H(k) / 2) * d_const / k - b0,
                       (mp.mpf("1.2e19"), mp.mpf("1.9e19")),
                       solver="bisect")
    check("G07 n=0 mechanism wall at k* ~ 1.4054e19 in (1.40e19,1.41e19)",
          mp.mpf("1.40e19") < root < mp.mpf("1.41e19")
          and abs(root / mp.mpf("1.405443828790708e19") - 1)
          < mp.mpf("1e-9"),
          "k* = %s" % mp.nstr(root, 12))

    # monotonicity samples for the region arguments
    ok_mono = True
    prev = None
    for lg in range(2, 20):
        k = mp.mpf(10) ** lg
        val = (my_H(k) / 2) * d_const / k
        if prev is not None:
            ok_mono &= val < prev
        prev = val
    ratio_prev = None
    for n in range(1, 8):
        rr = (y_lo * q_lo ** 40) ** (n + 1) / my_Bn(n)
        if ratio_prev is not None:
            ok_mono &= rr > ratio_prev
        ratio_prev = rr
    check("G08 monotonicity claims sampled (row0 decreasing; iii "
          "increasing in n)", ok_mono, "18 k-decades + n=1..7")


# ===================================================================== B1b
def b1b_gates() -> None:
    section("B1b  ROUND-100 N=4 CERTIFICATION AUDIT")
    # Nair, exact integer route
    ok_nair = True
    lcm = 1
    for n in range(1, 61):
        lcm = lcm * n // math.gcd(lcm, n)
        ok_nair &= lcm >= 2 ** (n - 1)
    # own sieve psi(x) >= (x-2) ln 2 spot checks
    limit = 10 ** 5
    bits = bytearray([1]) * 0 or bytearray(limit + 1)
    for i in range(len(bits)):
        bits[i] = 1
    bits[0] = bits[1] = 0
    for p in range(2, int(limit ** 0.5) + 1):
        if bits[p]:
            bits[p * p::p] = bytearray(len(bits[p * p::p]))
    psi_at = {}
    acc = 0.0
    targets = {10 ** 3, 10 ** 4, 10 ** 5}
    for n in range(2, limit + 1):
        if bits[n]:
            acc += math.log(n)
        else:
            m = n
            for p in range(2, int(n ** 0.5) + 1):
                if bits[p] and m % p == 0:
                    while m % p == 0:
                        m //= p
                    if m == 1:
                        acc += math.log(p)
                    break
        if n in targets:
            psi_at[n] = acc
    ok_psi = all(psi_at[x] >= (x - 2) * math.log(2) for x in targets)
    check("G09 Nair floor: lcm(1..n) >= 2^(n-1) exact n<=60; "
          "psi(x) >= (x-2)ln2 own-sieve", ok_nair and ok_psi,
          "psi/floor at 1e3/1e4/1e5 = %s"
          % ["%.4f" % (psi_at[x] / ((x - 2) * math.log(2)))
             for x in sorted(psi_at)])

    # far-floor necessity, own implementation of the radius model
    sig = [1.0 + 1.0 / j for j in range(1, 5)]
    s_ = [1.5 + 1.0 / j for j in range(1, 5)]
    ln2 = math.log(2.0)
    t19 = 1e19

    def far(j, nair):
        s = s_[j]
        t1ms = math.exp((1 - s) * math.log(t19))
        return (s * ((1 - ln2) if nair else 1.0) * t1ms / (s - 1),
                s * 0.03883 * t1ms / (s - 1))

    def rho_shift(logx, nair):
        r_, d_ = [], []
        for j in range(4):
            s = s_[j]
            bu = s * 0.94 * math.exp((0.5 - s) * logx) / (s - 0.5)
            lo, hi = far(j, nair)
            r_.append(bu + (lo + hi) / 2)
            d_.append(abs(hi - lo) / 2)
        fr = sum(((r_[j] + r_[k]) / (sig[j] + sig[k])) ** 2
                 for j in range(4) for k in range(4))
        fs = sum(((d_[j] + d_[k]) / (sig[j] + sig[k])) ** 2
                 for j in range(4) for k in range(4))
        return math.sqrt(fr) + math.sqrt(fs)

    lam4 = 1.10594158e-14
    crude_inf = rho_shift(60 * math.log(10), nair=False)
    nair_inf = rho_shift(60 * math.log(10), nair=True)
    lo_l, hi_l = 9 * math.log(10), 16 * math.log(10)
    for _ in range(120):
        mid = (lo_l + hi_l) / 2
        if rho_shift(mid, nair=True) > lam4:
            lo_l = mid
        else:
            hi_l = mid
    xreq = mid / math.log(10)
    lam5 = 7.91863638e-20
    s5 = 1.5 + 1.0 / 5
    floor5 = s5 * (1 - ln2) * math.exp((1 - s5) * math.log(t19)) / (s5 - 1)
    check("G10 far floors: crude blocks N=4 at any cap, Nair unblocks; "
          "X_req(4) ~ 1e11.5; floor5/lam5 ~ 4.7e5",
          crude_inf > lam4 > nair_inf and 11.2 < xreq < 12.2
          and 3e5 < floor5 / lam5 < 7e5,
          "crude=%.3e nair=%.3e lam4=%.3e X_req=10^%.2f floor5/lam5=%.1e"
          % (crude_inf, nair_inf, lam4, xreq, floor5 / lam5))

    # per-term error model, own re-derivation (Assumption A: 4u each)
    a_log = a_cbrt = 4.0
    e_r = 1.0            # 1/p
    e_p2 = 2 * e_r + 1.0  # r*r
    e_q = 1.0            # sqrt(pd)
    e_q4 = e_q / 2 + 1.0
    e_c6 = e_q / 3 + a_cbrt
    e_f1 = e_p2 + (e_r / 2 + 1.0) + 1.0
    e_f3 = e_p2 + e_c6 + 1.0
    e_f4 = e_p2 + e_q4 + 1.0
    worst_term = max(a_log + e + 1.0 for e in (e_f1, e_p2, e_f3, e_f4))
    check("G11 K_TERM re-derivation: worst per-term <= 13.34u <= "
          "13.5u (header) << 32u (frozen)",
          worst_term <= 13.34 + 1e-9 and worst_term <= 13.5
          and worst_term <= 32,
          "worst=%0.4fu (f3 path; header per-step slips u/6 vs u/3 "
          "immaterial = finding BH2-F7)" % worst_term)

    # F7 recompute: the header's own claimed c6 step (0.5u/3) understates
    header_c6 = a_cbrt + 0.5 / 3
    true_c6 = a_cbrt + 1.0 / 3
    n_total = 346_065_536_839 - 78_498
    acc_term = 4 * n_total * U * U
    check("G12 [BH2-F7] header slips pinned: true c6 bound u/3 > "
          "claimed u/6; 4*N_total*u^2 = 1.7e-20 > header's 2e-21 "
          "(certificate unaffected: enacted model uses true N)",
          true_c6 > header_c6 and 1.5e-20 < acc_term < 2e-20
          and acc_term < 32 * U,
          "4Nu^2=%.2e vs 32u=%.2e" % (acc_term, 32 * U))

    # dd accumulation bound, simulated vs exact rationals
    rng = random.Random(20260815)
    hi_acc = 0.0
    lo_acc = 0.0
    exact = Fraction(0)
    n_sim = 20000
    for _ in range(n_sim):
        x = rng.uniform(1e-9, 1.0)
        exact += Fraction(x)
        s = hi_acc + x
        b = s - hi_acc
        e = (hi_acc - (s - b)) + (x - b)
        e += lo_acc
        h = s + e
        lo_acc = e - (h - s)
        hi_acc = h
    dd_val = Fraction(hi_acc) + Fraction(lo_acc)
    err = abs(dd_val - exact)
    bound = Fraction(4 * n_sim) * Fraction(U) * Fraction(U) * exact
    check("G13 dd accumulation error <= 4*N*u^2*S (simulated, exact "
          "rationals)", err <= bound,
          "err=%.3e bound=%.3e (N=%d)" % (float(err), float(bound), n_sim))


# ===================================================================== B1c/d
def b1cd_gates() -> None:
    section("B1c/B1d  HAUSDORFF CONTINUATION + EULER-PICK BACKWARD TYPING")
    import sympy as sp
    z, av, w = sp.symbols("z a w", positive=True)
    # independent route: geometric series of 1/(a + y(z-a)) in (z-a)
    ys = sp.symbols("y1 y2 y3 y4", positive=True)
    ws = sp.symbols("w1 w2 w3 w4", positive=True)
    h = sp.symbols("h")
    ok_mt = True
    Gh = sum(wt / (av + yv * h) for yv, wt in zip(ys, ws))
    ser = sp.series(Gh, h, 0, 7).removeO()
    for n in range(7):
        coeff = ser.coeff(h, n)
        ok_mt &= sp.simplify(coeff - (-1) ** n / av ** (n + 1)
                             * sum(wt * yv ** n
                                   for yv, wt in zip(ys, ws))) == 0
    check("G14 moment-Taylor identity, independent geometric route "
          "(4 atoms, n<=6)", ok_mt,
          "G^(n)(a) Taylor coeff == (-1)^n b_n / a^(n+1) exactly")

    # F-side: b_n definition == sum y^(n+1) for the genus-0 pole sum
    ok_f = True
    for n in range(6):
        lhs = (av ** (n + 1) * (-1) ** n / sp.factorial(n)
               * sp.diff(1 / (z - w), z, n).subs(z, av))
        rhs = (av / (av - w)) ** (n + 1)
        ok_f &= sp.simplify(lhs - rhs) == 0
    check("G15 b_n per-pole identity a^{n+1}(-1)^n F^{(n)}(a)/n! == "
          "y^{n+1}", ok_f, "n<=5, symbolic")

    hs = blob("hausdorff_safepoint_probe.py")
    check("G16 continuation ingredients present + citation-typed in the "
          "owning probe",
          all(t in hs for t in
              ("Hausdorff 1921", "Widder", "identity theorem",
               "removable", "open and connected", "H1c-moment-taylor")),
          "adjudication: independently re-derived, NO GAP (off-axis "
          "poles = zeros of entire order-1/2 Phi: closed+discrete, no "
          "finite accumulation; countable closed set keeps slit-plane "
          "connectivity)")

    vbk = blob("vbk_invariant_probe.py")
    sv_lean = blob_abs(os.path.join(
        REPO, "experiments", "lean4-carrier-rigidity", "TfptCarrier",
        "SVSkeleton.lean"))
    check("G17 B1d: Montel/normal-families step citation-typed, never "
          "sold as proven",
          "normal families reduce it to" in vbk
          and "All hypotheses are named" in vbk
          and "cited, NOT proven" in sv_lean
          and "vitali_pick_interpolation : SectionsPSD" in sv_lean,
          "vbk V0c + SVSkeleton.lean named-hypothesis fields")


# ===================================================================== B2
def b2_gates() -> None:
    section("B2  CROSS-PROBE NUMBER CONSISTENCY")
    names = ("stieltjes_vitali_pin_probe.py",
             "krein_screw_realization_probe.py",
             "hausdorff_safepoint_probe.py")
    grids = []
    for nm in names:
        tree = ast.parse(blob(nm))
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign) \
                    and any(isinstance(t, ast.Name) and t.id == "SIGMAS"
                            for t in node.targets):
                grids.append(ast.dump(node.value))
                break
    check("G18 16-sigma pin grid literally identical (svpin/krein/"
          "hausdorff)", len(grids) == 3 and len(set(grids)) == 1,
          "AST literal compare")

    lev_log = blob("levinson_class_probe.run.log")
    road = blob("roadmap_probe.py")
    check("G19a kappa* ledger verbatim (levinson log == roadmap ward "
          "== note CDV)",
          "kappa*_ledger = ['0.995169', '0.998287', '0.998816']" in lev_log
          and "'0.995169', '0.998287', '0.998816'" in road,
          "0.995169/0.998287/0.998816")

    ep_log = blob("eulerpick_ladder_frozen.log")
    s4_log = blob("sieve4_run1.log")
    ok_fl = all(t in ep_log for t in
                ("N=1  lo=4.5917135e-2", "N=2  lo=9.0288701e-6",
                 "N=3  lo=2.3643695e-10"))
    ok_fl &= all(t in s4_log for t in
                 ("N=4  lo=8.278338e-15", "hi=1.3840906e-14",
                  "346065536839 (published 346065536839)",
                  "6.9310239e-10"))
    # r92 float ladder consistency with certified intervals
    ok_fl &= 4.5917135e-2 <= 4.59171357e-2 <= 4.5917136e-2
    ok_fl &= 8.278338e-15 <= 1.10594158e-14 <= 1.3840906e-14
    check("G19b certified floors consistent r92/r95/r100/roadmap",
          ok_fl, "intervals contain the float-ladder values")

    hs_log = blob("hausdorff_safepoint_probe.frozen.log")
    check("G19c depth-86 / gamma* 189.3/563.4 / 5290 cells verbatim",
          all(t in hs_log for t in
              ("d_max = 86", "5290 cells",
               "gamma* reach (main, a=256) = 189.3",
               "gamma* reach (arm, a=1024) = 563.4")),
          "hausdorff frozen log")

    moon = blob("moonshot_sol_probe.py")
    check("G19d k-frontier consistent: moonshot 1.40544e19 in roadmap "
          "bracket (1.40e19, 1.41e19)",
          "1.40544e19" in moon and "1.40e19 and" in road
          and 1.40e19 < 1.40544e19 < 1.41e19, "consistent relocation")


# ===================================================================== F3
def f3_gate() -> None:
    section("BH2-F3  MESH-TRIPLE RECOMPUTE (frozen round-93 engine)")
    import collective_rescue_probe as cr
    cr.setup_constants()
    t0 = time.time()
    sups = {}
    for delta_text, n in (("0.012", 400), ("0.008", 600)):
        atoms = cr.prime_atoms(4.8)
        base = cr.base_g_values(n, delta_text)
        packs = cr.packet_rows(atoms, n, delta_text)
        row = cr.lag_row_from_g(base, delta_text)
        for p in sorted(packs):
            row = cr.add_rows(row, packs[p])
        res = cr.szego(row, 60)
        sups[delta_text] = (cr.max_abs(res["alphas"])
                            if res["ok"] else float("nan"))
    scr = blob("screwind_induction_probe.py")
    mislabel = ("0.207/0.184/0.156 at delta 0.012/0.006/0.003" in scr
                and "round 90: 0.207/0.184/0.156" in scr)
    ok = (abs(sups["0.008"] - 0.2065) < 2e-3      # "0.207" is the 0.008 value
          and abs(sups["0.012"] - 0.2219) < 2e-3  # true 0.012 value
          and abs(sups["0.012"] - 0.207) > 1e-2   # mislabel is real
          and mislabel)
    check("G20 [BH2-F3] 0.207 belongs to delta=0.008 (round 93), not "
          "0.012/round 90; measured 0.012 sup = 0.222",
          ok, "sup[0,4.8): d=0.012 %.4f, d=0.008 %.4f (%.1f s); "
          "MESH-DAMPED verdict unaffected"
          % (sups["0.012"], sups["0.008"], time.time() - t0))


# ===================================================================== B3
GATE_FUNCS = {"check", "check_ward", "gate_law"}
PROBES_B3 = [
    "simple_principle_probe.py", "signpos_probe.py",
    "stieltjes_vitali_pin_probe.py", "krein_screw_realization_probe.py",
    "vbk_invariant_probe.py", "collective_rescue_probe.py",
    "cohomspec_probe.py", "eulerpick_ladder_probe.py",
    "rigidity_inverse_probe.py", "sp_expsum_pricing_probe.py",
    "ccm_pn_adjudication_probe.py", "sieve4_eulerpick_n4_probe.py",
    "screwind_induction_probe.py", "hausdorff_safepoint_probe.py",
    "moonshot_sol_probe.py", "levinson_class_probe.py",
    "roadmap_probe.py",
]


def b3_gates() -> None:
    section("B3  AST GATE-VACUITY CENSUS (17 probes)")
    hard_true = {}
    for nm in PROBES_B3:
        src = blob(nm)
        tree = ast.parse(src)
        lines = src.splitlines()
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) \
                    and isinstance(node.func, ast.Name) \
                    and node.func.id in GATE_FUNCS \
                    and len(node.args) >= 2 \
                    and isinstance(node.args[1], ast.Constant) \
                    and node.args[1].value is True:
                ctx = "\n".join(lines[max(0, node.lineno - 25):node.lineno])
                smoke_guard = ("if smoke" in ctx or "if args.smoke" in ctx)
                hard_true.setdefault(nm, []).append(
                    (node.lineno, smoke_guard))
    live = {(nm, ln) for nm, hits in hard_true.items()
            for ln, guarded in hits if not guarded}
    smoke_only = {(nm, ln) for nm, hits in hard_true.items()
                  for ln, guarded in hits if guarded}
    check("G21 [BH2-F1] exactly ONE run-of-record hardcoded-True gate: "
          "levinson G0.2",
          live == {("levinson_class_probe.py", 442)}
          and all(nm in ("krein_screw_realization_probe.py",
                         "rigidity_inverse_probe.py")
                  for nm, _ln in smoke_only),
          "live=%s smoke-guarded=%s" % (sorted(live), sorted(smoke_only)))

    vbk = blob("vbk_invariant_probe.py")
    t1 = abs((1 + 1 / 10 ** 9) - 1) < 2e-9
    t2 = abs((mp.mpf(1) + 1 / mp.mpf(10) ** 20) - 1) < mp.mpf("2e-20")
    check("G22 [BH2-F2] vbk tautological conjuncts pinned (never-fail "
          "arithmetic in V0a/V0c gates)",
          t1 and t2
          and "abs((1 + 1 / 10 ** 9) - 1) < 2e-9" in vbk
          and "abs((mp.mpf(1) + 1 / mp.mpf(10) ** 20) - 1)" in vbk,
          "both evaluate True unconditionally; Montel step itself "
          "citation-typed (honest)")


# ===================================================================== B4
def b4_gates() -> None:
    section("B4  LEAN STATEMENT REVIEW (out-of-band audit: PASS)")
    lean = os.path.join(REPO, "experiments", "lean4-carrier-rigidity",
                        "TfptCarrier")
    ax = blob_abs(os.path.join(lean, "AxiomCheck.lean"))
    n_pa = sum(1 for line in ax.splitlines()
               if line.startswith("#print axioms TfptCarrier.")
               and any(m in line for m in ("EulerPick.", "DeltaOneNoGo.",
                                           "ParityLemma.", "SVSkeleton.")))
    ep = blob_abs(os.path.join(lean, "EulerPick.lean"))
    pl = blob_abs(os.path.join(lean, "ParityLemma.lean"))
    sv = blob_abs(os.path.join(lean, "SVSkeleton.lean"))
    ok = (n_pa == 27
          and "theorem pickMatrix_posSemidef (γ : ι → ℝ) (σ : n → ℝ)" in ep
          and "(hσ : ∀ j, 0 < σ j) : (pickMatrix γ σ).PosSemidef" in ep
          and pl.count("simplicity : ∀ i, i < m →") == 3
          and "∃ S : SVtoRHSkeleton, ¬ S.RH ∧ ¬ S.SV" in sv
          and "sorry" not in ep.replace("no `sorry`", "")
          )
    check("G23 27 print-axioms lines; posSemidef quantifies over "
          "arbitrary finite real ordinates + positive nodes; simplicity "
          "an explicit hypothesis (x3); honesty lock a genuine "
          "existential with RH = False", ok,
          "print-axioms=%d; scripts/audit.sh AUDIT: PASS (7/7, axioms "
          "exactly propext/Classical.choice/Quot.sound; run out-of-band "
          "in this audit)" % n_pa)


# ===================================================================== B5
def b5_gates() -> None:
    section("B5  SYNCED-SURFACE CLAIM DRIFT")
    paper = blob_abs(os.path.join(
        REPO, "articles", "2026-08-11",
        "paper_endform_and_inertia_bridge_en.md"))
    pf = blob_abs(os.path.join(REPO, "tfpt_prime_front.tex"))
    cl = blob_abs(os.path.join(REPO, "changelog.tex"))
    nums = ("8.278338", "1.3840906", "0.749", "1.176577", "335.8",
            "1416.8", "0.9952/0.9983/0.9988", "5290", "189/563")
    ok_nums = all(n in paper or n in pf or n in cl for n in nums)
    ok_all3 = all(("8.278338" in t and "1.176577" in t)
                  for t in (paper, pf, cl))
    check("G24 load-bearing numbers grep-match on all three surfaces",
          ok_nums and ok_all3, "paper S8.13/14 + prime-front 12.45/46 "
          "+ changelog C/CI")

    krein = blob("krein_screw_realization_probe.py")
    vbk = blob("vbk_invariant_probe.py")
    phrase = "equivalent lemma forms"
    drift = (phrase in paper.lower() and phrase in pf.lower()
             and phrase in cl.lower())
    openb = ("SUZKREIN-CARRIER-OPEN" in krein
             and "positivity hypothesis remains Weil positivity" in krein)
    check("G25 [BH2-F4] drift pinned: 'equivalent lemma forms' on every "
          "surface WHILE the form-B converse is the round-90 OPEN lemma",
          drift and openb,
          "honest form: each RH-sufficient; A RH-equivalent (audited + "
          "Zhang); B/C converse directions open/measured/conditional")

    stale_uniform = ("uniform Weyl-disk contraction" in paper
                     and "uniform Weyl-disk" in pf)
    v0a_correct = ("uniformity as sigma decreases to 1/2 is used" in vbk
                   and "pointwise contraction" in vbk.lower())
    check("G26 [BH2-F5] stale 'uniform' in the form-B name vs the V0a "
          "pointwise correction (both live on the same surfaces)",
          stale_uniform and v0a_correct, "r90 enum adjective carried "
          "past the r92 correction")

    road = blob("roadmap_probe.py")
    s4_log = blob("sieve4_run1.log")
    check("G27 [BH2-F6] roadmap M1b acceptance uses stale r95 N=3 lo "
          "(2.3643695e-10) though r100 tightened to 6.9310239e-10",
          "2.3643695e-10" in road and "6.9310239e-10" in s4_log
          and "6.9310239e-10" not in road
          and 6.9310239e-10 > 2.3643695e-10,
          "acceptance ~2.9x weaker than the corpus's certified state")


# ===================================================================== main
def main() -> int:
    print("bughunt2_r86_r105_probe  PRIME.BUGHUNT2.R86.R105.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM.  EXPLORATION ONLY.  Findings ledger: 7 "
          "(1 MAJOR / 6 MINOR / 0 FATAL); no round verdict flips.")

    section("G01  SELF-FIREWALL")
    src = blob_abs(os.path.abspath(__file__))
    tree = ast.parse(src)
    writers = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = node.func
            name = (fn.attr if isinstance(fn, ast.Attribute)
                    else fn.id if isinstance(fn, ast.Name) else "")
            if name == "open" and len(node.args) >= 2:
                mode = node.args[1]
                if isinstance(mode, ast.Constant) and "w" in str(mode.value):
                    writers.append(node.lineno)
    check("G01 probe writes nothing (no open(...,'w'), stdout only)",
          not writers, "write-mode opens: %s" % (writers or "none"))

    b1a_gates()
    b1b_gates()
    b1cd_gates()
    b2_gates()
    f3_gate()
    b3_gates()
    b4_gates()
    b5_gates()

    section("LEDGER + COMPOSITE VERDICT")
    for fid, sev, txt in FINDINGS:
        print("  %s [%s] %s" % (fid, sev, txt))
    print("  VERDICT FLIPS: none (all round-86..105 verdict enums stand)")
    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    n_tot = len(CHECKS)
    elapsed = time.time() - START
    print("\nCHECKS %d/%d PASS  runtime %.1f s  SPEC_SHA %s"
          % (n_pass, n_tot, elapsed, SPEC_SHA[:16]))
    if n_pass == n_tot:
        print("COMPOSITE: BUGHUNT2-FINDINGS(7, MAJOR) -- 1 MAJOR "
              "(claim-drift, prose-level) / 6 MINOR / 0 FATAL; "
              "B1 re-derivations all CLEAN; no verdict flips.")
    else:
        print("COMPOSITE: BUGHUNT2-INSTRUMENT-EDGE(%d/%d)"
              % (n_pass, n_tot))
    print("NO RH CLAIM.")
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
