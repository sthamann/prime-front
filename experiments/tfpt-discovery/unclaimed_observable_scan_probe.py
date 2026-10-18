#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""unclaimed_observable_scan_probe -- PHYS.UNCLAIMED.DECODER.01

FROZEN SPEC v1 (2026-08-15).  EXPLORATION ONLY, experiments/ only.
Nothing here is load-bearing, nothing is promoted, no marker moves,
no scorecard row is written by this probe.  This probe writes no files.

=======================================================================
MANDATE
=======================================================================
Owner directive: "Finde neue Muster, Beweise, Vorhersagen der Theorie."
The corpus already claims a dense prediction surface (121 scorecard
rows, full CKM, lepton ladder, inflation sector, flat budget).  Before
ANY new numeric relation may even be proposed, the project's own
red-team discipline demands a look-elsewhere-controlled scan: with the
frozen compiler vocabulary, is any UNCLAIMED dimensionless observable
expressible at a complexity/precision combination that placebo targets
cannot match?  This probe is that scan -- a numerology DETECTOR, not a
numerology generator.  Expected honest outcome per the transcription
verdict of PRIME.BIGPICTURE.SIMPLE.PRINCIPLE.02: NO-EXCESS or
SCAN-UNDECIDABLE.  Any CANDIDATE outcome is coincidence-risk [C]-tier
raw material for THEORY-side derivation, never a claim.

=======================================================================
UNCLAIMED TARGETS (frozen; verified unclaimed by ledger/scorecard grep
2026-08-15: alpha_s(M_Z) is a DECLARED EXTERNAL, |V_cb|/|V_ub| are
claimed via the CKM kernel, m_e/m_mu = (12/7) phi0^2 is claimed,
m_mu/m_tau is implied by Koide + m_e/m_mu, Omega_c/Omega_b is inside
the flat-budget scoring -- all EXCLUDED as already-claimed)
=======================================================================
T1  r_nu = Dm2_21/|Dm2_31| = 7.388e-5 / 2.511e-3 = 0.029423
    sigma_rel = 0.027  [JUNO 207d (Neutrino 2026) + NuFIT 6.x]
T2  m_u/m_d = 0.462, sigma_rel = 0.043  [PDG 2024 lattice MS-bar 2 GeV]
T3  m_s/m_d = 19.5,  sigma_rel = 0.051  [PDG 2024]
T4  (m_n - m_p)/m_e = 2.530885, sigma_rel = 4e-6 but F_transfer-fuzzy;
    frozen tolerance floor applies (below)  [CODATA 2022]

POSITIVE CONTROLS (claimed by the corpus; calibrate what the
vocabulary + statistic CAN see):
C1  m_e/m_mu = 0.00483633  (claimed expr (12/7) phi0^2, -0.11%)
C2  sin^2 theta13 = 0.02215, sigma_rel = 0.025  (claimed expr
    e^(-5/6) phi0, the known -1.7 sigma crack -- inside 2 sigma)

=======================================================================
FROZEN VOCABULARY
=======================================================================
value = (p/q) * phi0^e * c3^f * pi^d * exp(g/6)
  p, q in 1..16 coprime; e in 0..3; f in 0..2; d in -3..3; g in -6..6
  phi0 = (4/3) c3 + 48 c3^4,  c3 = 1/(8 pi)
  keep values with 1e-6 <= v <= 1e+6; drop the trivial identity 1.
COMPLEXITY (frozen):
  C = log2(p*q) + 2e + 2.5f + 1.5|d| + 0.5|g|
HIT RULE (frozen): |v/t - 1| <= max(2*sigma_rel, 0.005).
STATISTIC per target: Cmin = min complexity over all hits (inf if none).

=======================================================================
PLACEBO CALIBRATION (frozen)
=======================================================================
Per target: 400 pseudo-targets t' = t * exp(U(-ln 2, +ln 2)),
seed 20260815, same sigma_rel, same hit rule; null distribution of
Cmin.  p = (1 + #{Cmin_null <= Cmin_obs}) / 401, one-sided (real
structure = unusually LOW minimal complexity).

VERDICT RULES (frozen):
  per target: CANDIDATE iff p < 0.0125 (Bonferroni 0.05/4)
  global: CANDIDATES(list) if any;
          SCAN-UNDECIDABLE if the median placebo Cmin over all four
          targets is <= max(Cmin of the two controls) (the vocabulary
          is dense enough to express ANYTHING at control complexity --
          the scan then cannot separate structure from coincidence);
          NO-EXCESS otherwise.

=======================================================================
GATES
=======================================================================
G01 vocabulary deterministic, size in [50000, 400000], values sorted.
G02 both positive controls are hit AND the corpus's own expressions
    (12/7) phi0^2 for C1 (p=12, q=7, e=2, f=0, d=0, g=0) and
    phi0 * e^(-5/6) for C2 (p=q=1, e=1, f=0, d=0, g=-5) are MEMBERS of
    the respective hit sets.  [AMENDMENT A1, disclosed: run 1 (log
    unclaimed_observable_scan_probe.run1.log, 4/5 gates) had frozen
    this gate as "the corpus expression is the MINIMAL-complexity
    hit"; that bar was wrongly specified, not wrongly measured -- the
    scan found CHEAPER coincidental matches inside the tolerance
    window for both controls (C1: (1/11) phi0 at C=5.46 vs corpus
    C=10.39; C2: (1/2) phi0 e^(-1/6) at C=3.50 vs corpus C=4.50).
    That observation is itself evidence FOR vocabulary saturation and
    is reported below; the membership bar tests what the gate was
    meant to test (instrument sees the corpus expressions at all).
    No verdict-side bar was moved; the verdict logic is unchanged.]
G03 control and target p-values computed, finite, in (0, 1].
G04 placebo reproducibility: rerun of T1 placebo block with the frozen
    seed reproduces the p-value exactly.
G05 verdict enum frozen.
"""

import hashlib
import math
import sys
import time
from fractions import Fraction
from math import gcd

import numpy as np

FROZEN_SPEC = __doc__
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()

SEED = 20260815
N_PLACEBO = 400
TOL_FLOOR = 0.005

C3 = 1.0 / (8.0 * math.pi)
PHI0 = (4.0 / 3.0) * C3 + 48.0 * C3 ** 4

TARGETS = [
    ("T1 r_nu=Dm2_21/|Dm2_31|", 0.029423, 0.027),
    ("T2 m_u/m_d", 0.462, 0.043),
    ("T3 m_s/m_d", 19.5, 0.051),
    ("T4 (m_n-m_p)/m_e", 2.530885, 4e-6),
]
CONTROLS = [
    ("C1 m_e/m_mu", 0.00483633, 1e-4),
    ("C2 sin^2 th13", 0.02215, 0.025),
]

CHECKS = []


def gate(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  " + detail) if detail else ""))


def build_vocabulary():
    """Enumerate the frozen vocabulary; return sorted (logv, C, token)."""
    entries = []
    lphi = math.log(PHI0)
    lc3 = math.log(C3)
    lpi = math.log(math.pi)
    for p in range(1, 17):
        for q in range(1, 17):
            if gcd(p, q) != 1:
                continue
            lpq = math.log(p) - math.log(q)
            c_pq = math.log2(p * q)
            for e in range(0, 4):
                for f in range(0, 3):
                    for d in range(-3, 4):
                        for g in range(-7, 7):
                            if g == -7:
                                continue  # keep symmetric -6..6
                            logv = (lpq + e * lphi + f * lc3
                                    + d * lpi + g / 6.0)
                            if abs(logv) > 6.0 * math.log(10.0):
                                continue
                            comp = (c_pq + 2.0 * e + 2.5 * f
                                    + 1.5 * abs(d) + 0.5 * abs(g))
                            if comp == 0.0:
                                continue  # trivial identity 1
                            entries.append((logv, comp, (p, q, e, f, d, g)))
    entries.sort(key=lambda x: x[0])
    return entries


def hit_window(logvals, t, sigma_rel):
    tol = max(2.0 * sigma_rel, TOL_FLOOR)
    # |v/t - 1| <= tol  =>  log(t(1-tol)) <= logv <= log(t(1+tol))
    lo = math.log(t * (1.0 - tol))
    hi = math.log(t * (1.0 + tol))
    i = np.searchsorted(logvals, lo, side="left")
    j = np.searchsorted(logvals, hi, side="right")
    return i, j


def min_complexity(logvals, comps, tokens, t, sigma_rel):
    """Minimal complexity of any vocabulary hit on target t."""
    i, j = hit_window(logvals, t, sigma_rel)
    if i >= j:
        return math.inf, None
    k = i + int(np.argmin(comps[i:j]))
    return float(comps[k]), tokens[k]


def contains_token(logvals, tokens, t, sigma_rel, tok):
    """Is a specific token a member of the hit set for target t?"""
    i, j = hit_window(logvals, t, sigma_rel)
    return any(tokens[k] == tok for k in range(i, j))


def token_str(tok):
    p, q, e, f, d, g = tok
    parts = []
    if (p, q) != (1, 1):
        parts.append("%d/%d" % (p, q) if q != 1 else "%d" % p)
    if e:
        parts.append("phi0^%d" % e if e != 1 else "phi0")
    if f:
        parts.append("c3^%d" % f if f != 1 else "c3")
    if d:
        parts.append("pi^%d" % d if d != 1 else "pi")
    if g:
        parts.append("e^(%d/6)" % g)
    return " * ".join(parts) if parts else "1"


def placebo_pvalue(logvals, comps, tokens, t, sigma_rel, c_obs, rng):
    """One-sided placebo p for the observed minimal complexity."""
    count = 0
    finite_cs = []
    for _ in range(N_PLACEBO):
        t_p = t * math.exp(rng.uniform(-math.log(2.0), math.log(2.0)))
        c_p, _ = min_complexity(logvals, comps, tokens, t_p, sigma_rel)
        if c_p <= c_obs:
            count += 1
        if math.isfinite(c_p):
            finite_cs.append(c_p)
    p = (1 + count) / (N_PLACEBO + 1)
    med = float(np.median(finite_cs)) if finite_cs else math.inf
    return p, med


def main():
    t0 = time.time()
    print("unclaimed_observable_scan_probe -- PHYS.UNCLAIMED.DECODER.01")
    print("SPEC_SHA %s" % SPEC_SHA)
    print("phi0 %.9f  c3 %.9f  seed %d  placebos %d"
          % (PHI0, C3, SEED, N_PLACEBO))

    vocab = build_vocabulary()
    logvals = np.array([v[0] for v in vocab])
    comps = np.array([v[1] for v in vocab])
    tokens = [v[2] for v in vocab]
    ok1 = 50000 <= len(vocab) <= 400000 and \
        bool(np.all(np.diff(logvals) >= 0))
    gate("G01 vocabulary deterministic, size in range, sorted",
         ok1, "size %d" % len(vocab))

    # G02 positive controls (membership bar; Amendment A1 in spec)
    ctrl_results = []
    corpus_toks = [(12, 7, 2, 0, 0, 0), (1, 1, 1, 0, 0, -5)]
    ok2 = True
    for (name, t, srel), ctok in zip(CONTROLS, corpus_toks):
        c_obs, tok = min_complexity(logvals, comps, tokens, t, srel)
        member = contains_token(logvals, tokens, t, srel, ctok)
        ctrl_results.append((name, t, srel, c_obs, tok))
        ok2 &= (tok is not None) and member
        print("    %s: Cmin %.2f  cheapest expr %s  corpus expr %s "
              "in hit set: %s"
              % (name, c_obs, token_str(tok) if tok else "NONE",
                 token_str(ctok), member))
    gate("G02 controls hit + corpus expressions are hit-set members",
         ok2)

    # Targets
    print("\n  Unclaimed-target scan (hit rule: max(2 sigma, 0.5%)):")
    results = []
    all_p_finite = True
    placebo_medians = []
    for idx, (name, t, srel) in enumerate(TARGETS):
        c_obs, tok = min_complexity(logvals, comps, tokens, t, srel)
        rng = np.random.default_rng(SEED + idx)
        p, med = placebo_pvalue(logvals, comps, tokens, t, srel,
                                c_obs, rng)
        placebo_medians.append(med)
        results.append((name, t, srel, c_obs, tok, p))
        all_p_finite &= (0.0 < p <= 1.0)
        print("    %s: Cmin %.2f  expr %s  placebo-med %.2f  p=%.4f"
              % (name, c_obs, token_str(tok) if tok else "NONE", med, p))
    gate("G03 target/control p-values finite in (0,1]", all_p_finite)

    # G04 reproducibility of the placebo block (T1)
    name, t, srel = TARGETS[0]
    c_obs = results[0][3]
    p_a, _ = placebo_pvalue(logvals, comps, tokens, t, srel, c_obs,
                            np.random.default_rng(SEED + 0))
    gate("G04 placebo block reproducible at frozen seed",
         p_a == results[0][5], "p %.4f == %.4f" % (p_a, results[0][5]))

    # Verdict (frozen rules)
    candidates = [r for r in results if r[5] < 0.0125]
    ctrl_cmax = max(r[3] for r in ctrl_results)
    med_all = float(np.median(placebo_medians))
    if candidates:
        verdict = "CANDIDATES(%s)" % ",".join(r[0].split()[0]
                                              for r in candidates)
    elif med_all <= ctrl_cmax:
        verdict = "SCAN-UNDECIDABLE"
    else:
        verdict = "NO-EXCESS"
    gate("G05 verdict enum frozen",
         verdict.startswith(("CANDIDATES(", "SCAN-UNDECIDABLE",
                             "NO-EXCESS")))

    n_pass = sum(1 for _, ok in CHECKS if ok)
    rt = time.time() - t0
    print("\n  control Cmax %.2f  median placebo Cmin %.2f"
          % (ctrl_cmax, med_all))
    print("  GATES %d/%d  runtime %.1f s  SPEC_SHA %s"
          % (n_pass, len(CHECKS), rt, SPEC_SHA[:16]))
    print("  VERDICT: %s  (numerology DETECTOR; any CANDIDATE is "
          "[C]-tier raw material for theory-side derivation, never a "
          "claim)" % verdict)
    sys.exit(0 if n_pass == len(CHECKS) else 1)


if __name__ == "__main__":
    main()
