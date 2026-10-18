#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bughunt_r79_r85_probe -- ADVERSARIAL INSTRUMENT AUDIT, rounds 79-85

FROZEN SPEC v1 (2026-08-14).  EXPLORATION ONLY.  AUDIT ROLE.  This probe
writes no files, changes no verification module, paper, ledger, website,
manifest or status marker.  It makes NO RH claim in ANY direction.

MANDATE.  Hunt for bugs in the discovery rounds 79-85 corpus
(kill_atlas_dag_probe, sat_projection_alignment_probe,
untested_sign_sources_probe, birdseye_shape_freedom_probe,
semilocal_realroot_limit_probe, stc_sol/stc_opus_convergence_probe,
realroot_arbiter_probe, tp_sol/tp_da_probe; notes CCCLXXVI-CCCLXXXIV;
commit messages 0542ca72..8e0c2998; the round-79-82 surface sync).
Every finding is carried as DATA in FINDINGS below and pinned by an
executable gate that (a) greps the wrong text where it lives, and/or
(b) recomputes the quantity at honest precision and gates the repaired
value.  THE PROBE'S PASS MEANS THE AUDIT IS CONSISTENT, NOT "NO BUGS".

AUDIT ROLE DISCLOSURE: as an auditor this probe deliberately reads
target data (the verified-zero cache, git history, other probes'
sources) everywhere; it is not a source-only construction and feeds no
gate of any other probe.

=======================================================================
THE FINDINGS LEDGER (established by the pre-freeze audit; every row is
re-asserted executably below; severities: FATAL = flips a recorded
round verdict; MAJOR = a published number is wrong; MINOR =
cosmetic / disclosed / quantifier imprecision)
=======================================================================
F1 MAJOR  Commit 23ea7f9a (round 83) fuses two different quantities:
   "zeros track ordinates to 7.1e-15 (0.16 percent of mean spacing)".
   Measured here: -7.11e-15 is the FIRST-zero-only readout of lane 1's
   float64-refined instrument at x = 13, while 0.16 percent of mean
   spacing is the MEAN displacement over the 15 matched zeros
   (5.744e-3 ABSOLUTE) -- eleven orders apart.  Worse, BOTH numbers
   are instrument artifacts of the same float64 refinement (see F6):
   the exact-mp census reads first-zero dev -8.4e-16 (= the cache's
   own float64 quantization of gamma_1, measured +1.21e-15 against
   the 30-digit literature value) at BOTH x = 8 and x = 13, and mean
   displacement 0.0 at float64 resolution (all 15 matched zeros land
   bit-identically on the cache ordinates).  The honest statement:
   the minimizer zeros sit on the ordinates BELOW the comparator
   floor; every printed sub-1e-13 deviation digit is noise.  No
   verdict flips (the tracking claim gets STRONGER).
F2 MAJOR  "36 nodes vs 3 zeros in (0,30) at x = 55" (commit 23ea7f9a;
   note CCCLXXXIII; realroot_arbiter_probe.py adjudication print)
   pairs a TWO-SIDED node count (|tau| < 30 -> 36) with a ONE-SIDED
   zero census ((0,30) -> 3).  Measured here with lane 3's own
   builder: one-sided (0,30) = 18 nodes, two-sided = 36.  Honest
   pairings: 18-vs-3 or 36-vs-6.  Off by a factor 2 on one side; the
   conclusion (mesh family over-dense) is unchanged, no verdict flip.
F3 MINOR  Commit 806197a5 (round 84): the mesh-CF (0,30) count
   "tracking the uniform Nyquist prediction within 10 percent" is
   wrong at three rungs: measured deviations reach 10.2 / 10.6 /
   10.9 percent at x = 13 / 21 / 34.  The owning probe's frozen
   tolerance is 30 percent (honest and passed); the commit's "10"
   rounds 10.9 down.  Direction and conclusion unchanged.
F4 MINOR  Commit 23ea7f9a: "the WEIGHTED trace converges on all four
   (to 2.3e-06)" -- 2.3e-06 is the BEST of the four final values;
   the four finals are 9.3e-04 / 3.3e-06 / 2.3e-06 / 6.2e-04.
F5 MINOR  NINE gates in the corpus are hardcoded check(..., True, ...)
   and can never fail while being counted in the N/N PASS tallies:
   semilocal T1d-1 ("R4 catches lam^-2 mass escape" -- an analytic
   claim asserted, not tested), arbiter Q2e + Q3a and sat X2 + X5 and
   untested C2.4 (verdict/census-RECORDING gates whose substance is
   gated elsewhere -- disclosed style for the arbiter pair, silent
   for sat/untested), and the G0.2 "spec SHA frozen" self-attestations
   of sat / untested / birdseye.  Notably sat X5 is the line that
   records the round-80 headline "candidate #19 gate FAIL" (the
   substance sits in the gated X1/X3/X4).  Vacuous-by-construction.
F6 MAJOR  The round-83 float64 refinement bug (lane 1 hp_zero_data
   refines exact mp polynomial roots by bisection on the FLOAT64 trig
   profile; the docstring premise "zeros are O(1e-16)-stable under
   coefficient rounding" is false at depth).  Effect on PUBLISHED
   numbers, recomputed here at honest precision (pure mp roots, no
   refinement): at x = 13 the corruption reaches BELOW 0.75 om_max
   (max low-band |dz| ~ 5.9e-2, where tp_da's W4 bar is 1e-6 --
   tp_da warded only x = 5/8, the deepest rung was never
   cross-checked); the published eps finals move by up to ~117%
   (B=2.0 m=4: 2.071e-08 -> 9.550e-09; B=2.8 m=4: 3.708e-09 ->
   6.290e-09, both below the probe's own declared NF = 1e-8
   envelope); the decay exponents move (worst -4.47 -> -4.96); the
   displacement diagnostics are artifacts (F1).  WHAT DOES NOT MOVE:
   all six rows still type CONVERGES, the tau-screen live rows stay
   PASS (|s| <= 0.30), world separation and census are untouched --
   REALROOT-ARCHITECTURE-OPEN stands.  No verdict flips.
F7 MINOR  The arbiter's mp-scan ward (Q2c) checks (0,30)/(0,60) at
   x = 8/13 but the x = 21 deliverable includes a (0,100) census;
   the (60,100) scan band was warded NOWHERE although the exact
   census at x = 13 (om_max ~ 98) could have warded it.  Repaired
   here: scan(0,100) at x = 13 == exact census in (0,100).  The
   x = 21 row's methodology survives; the A-2 census-discontinuity
   (cache-precision plants) does not touch the source-built x = 21
   cell.
F8 MINOR  "tau-screen slopes 0.019-0.043 ALL PASS" (commit 23ea7f9a,
   note CCCLXXXII): only 4 of 6 battery rows are LIVE; two rows
   (B=2.0/2.8, m=4) are NOT-APPLICABLE because their eps values sit
   below the probe's own 10 NF floor filter.  "ALL" = "all live
   rows", undisclosed in commit and note.
F9 MINOR  Dead code: semilocal hp_zero_data builds b from float64
   om**2 and immediately overwrites it with the mp formula; tp_sol
   computes em = profile(...) and never uses it; stc_sol defines
   EULER_FLOAT and never uses it.  Cosmetic, no numeric effect.
AUDIT-CLEAN items (checked, no finding): the f4 np.interp truncation
   discontinuity is ABSENT from the rounds-79-85 corpus (the only
   np.interp, birdseye W2, evaluates strictly inside its grid;
   untested/birdseye consume the padded repair where it matters);
   all tau-screens use the frozen bands |s| <= 0.30 / >= 0.70;
   round-79-82 headline numbers (-3.379, -0.46..-1.09, Schur
   3.97e-07 -> 4.19e-12, MIN-U2 0.3635/0.2088/0.3533 vs
   0.4475/0.4443/0.4487, T_req h^4.77, 1.95e-05 vs Rosser 1.2e-02,
   107.1/4.36/0.21, 24/0/19 tally, stable rank 109.6 -> 1595.2)
   all reproduce bit-similar on fresh re-runs; lane-2 separations
   3.1e5/4.1e5 and lane-1 medians 1.26e6/1.40e6 reproduce; tp_sol
   7/7 numbers (delta* 1.19e-06, -9.1e-17 flip, prime/gap 91.7 /
   3.4e10 / 5.4e23) reproduce; the lane-2 quotient and the mesh
   ladder reproduce; no other hardcoded-True gate, no catch-all
   swallowing a gate failure, no float ==, no sieve boundary bug
   found (p^k <= x inclusive everywhere).

=======================================================================
FROZEN BARS
=======================================================================
 X_RE = (3, 5, 8, 13), DPS = lane 1's frozen HP ladder (45/60/80/120).
 CACHE_Q_BAR = 5e-15 (cache gamma_1 quantization vs 30-digit
 literature).  EXACT_DZ1_BAR = 2e-15 (honest first-zero dev at
 x = 8/13 must sit at the comparator floor).  NOISE_FACTOR = 5
 (published refined reads exceed the honest read by at least this).
 MEAN_DISP_REF_MIN = 1e-3, MEAN_DISP_EXACT_MAX = 1e-12 (x = 13).
 LOWBAND_REF_MIN = 1e-2 at x = 13, LOWBAND_MAX8 = 1e-6 at x = 8
 (0.75 om_max cut, tp_da's W4 bar).  EPS_MOVE_MIN = 0.30 (largest
 relative eps move at x = 13 between instruments).  MESH55 = (18, 36).
 NYQ_DEV_BAND = (0.10, 0.13), NYQ_OVER10 = 3.  WT_FINal: all four
 lane-3 weighted rows converge (< 0.2 first) but max final > 2.6e-4.
 TAU bands 0.30/0.70 (atlas).  RUNTIME_BAR = 900 s.
 --smoke: X_RE = (3, 5), skips F6/F7 deep gates; NOT verdict-bearing.

COMPOSITE VERDICT (frozen): BUGHUNT-CLEAN iff FINDINGS is empty;
 else BUGHUNT-FINDINGS(n, max severity).  This run records n = 9,
 max = MAJOR, 0 FATAL, no round verdict flipped.

NO RH CLAIM.  NO POSITIVITY CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import subprocess
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import realroot_arbiter_probe as arb            # noqa: E402
import semilocal_realroot_limit_probe as lane1  # noqa: E402
import stc_opus_convergence_probe as lane3      # noqa: E402

# ---------------------------------------------------------------- bars
X_RE = (3, 5, 8, 13)
DPS = {3: 45, 5: 60, 8: 80, 13: 120}
CACHE_Q_BAR = 5e-15
EXACT_DZ1_BAR = 2e-15
NOISE_FACTOR = 5.0
MEAN_DISP_REF_MIN = 1e-3
MEAN_DISP_EXACT_MAX = 1e-12
LOWBAND_REF_MIN = 1e-2
LOWBAND_MAX8 = 1e-6
EPS_MOVE_MIN = 0.30
MESH55_ONE, MESH55_TWO = 18, 36
NYQ_DEV_LO, NYQ_DEV_HI = 0.10, 0.13
NYQ_OVER10 = 3
WT_MAX_FINAL_MIN = 2.6e-4
RUNTIME_BAR = 900.0
GAMMA1_30 = "14.134725141734693790457251983562"   # literature, 30 digits
PUB_DZ1 = {8: -1.07e-14, 13: -7.11e-15}           # note CCCLXXXII
PUB_EPS13 = {(1.2, 2): 6.327e-05, (1.2, 4): 1.637e-07,
             (2.0, 2): 1.752e-05, (2.0, 4): 2.071e-08,
             (2.8, 2): 1.288e-05, (2.8, 4): 3.708e-09}
ARB_PUB = {"tent(1.5)[l3-B1]": (1.72e-2, 4.5e-3),
           "bump(1.5,3)[l3-B3]": (5.2e-5, 6.8e-7),
           "bessel(1.0,4)[l2]": (6.0e-6, 4.1e-7)}   # note CCCLXXXIII Q3
EXPECT_TRUE_GATES = {
    "semilocal_realroot_limit_probe.py": 1,
    "realroot_arbiter_probe.py": 2,
    "birdseye_shape_freedom_probe.py": 1,
    "untested_sign_sources_probe.py": 2,
    "sat_projection_alignment_probe.py": 3,
    "kill_atlas_dag_probe.py": 0,
    "stc_sol_convergence_probe.py": 0,
    "stc_opus_convergence_probe.py": 0,
    "tp_sol_probe.py": 0,
    "tp_da_probe.py": 0,
}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []

SEV = {"F1": "MAJOR", "F2": "MAJOR", "F3": "MINOR", "F4": "MINOR",
       "F5": "MINOR", "F6": "MAJOR", "F7": "MINOR", "F8": "MINOR",
       "F9": "MINOR"}
FINDINGS = [
    ("F1", "commit 23ea7f9a + note CCCLXXXII + tp_da docstring",
     "'7.1e-15 (0.16 percent of mean spacing)' fuses first-zero noise"
     " read with mean displacement; both are float64-refinement"
     " artifacts", "-7.11e-15 / 0.0016*spacing",
     "-8.4e-16 (= cache quantization) / 0.0 at float64", False),
    ("F2", "commit 23ea7f9a + note CCCLXXXIII + arbiter adjudication"
     " print", "'36 nodes vs 3 zeros in (0,30) at x=55' pairs"
     " two-sided nodes with one-sided zeros", "36 vs 3 in (0,30)",
     "18 vs 3 one-sided, or 36 vs 6 two-sided", False),
    ("F3", "commit 806197a5", "'within 10 percent' Nyquist tracking",
     "<= 10%", "max 10.9% (3 rungs over 10%); probe gate is 30%",
     False),
    ("F4", "commit 23ea7f9a", "'converges on all four (to 2.3e-06)'",
     "2.3e-06 for all four", "9.3e-04/3.3e-06/2.3e-06/6.2e-04", False),
    ("F5", "five probes", "hardcoded check(..., True) gates in PASS"
     " tallies (incl. sat X5, the candidate-#19 gate-verdict line)",
     "counted as tested gates", "vacuous by construction: 9 total"
     " (semilocal 1, arbiter 2, sat 3, untested 2, birdseye 1)",
     False),
    ("F6", "semilocal round 83 published eps/exponents/displacements",
     "float64 refinement corrupts zeros below 0.75 om_max at x=13;"
     " 'zeros are O(1e-16)-stable' premise false at depth",
     "eps13(2.0,4) 2.071e-08; exponents to -4.47; disp 0.0016",
     "9.550e-09 (+117%); to -4.96; 0.0 -- typings/verdict UNCHANGED",
     False),
    ("F7", "realroot_arbiter_probe Q2c", "(60,100) scan band never"
     " warded though x=13 census reaches ~98", "unwarded",
     "warded here: scan(0,100) == exact census at x=13", False),
    ("F8", "commit 23ea7f9a + note CCCLXXXII", "'tau-screen ... ALL"
     " PASS' hides 2/6 NOT-APPLICABLE rows", "6/6 implied",
     "4 live PASS + 2 N/A (below 10 NF)", False),
    ("F9", "lane1 hp_zero_data / tp_sol / stc_sol", "dead code",
     "n/a", "n/a", False),
]


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-56s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def git_body(sha: str) -> str:
    try:
        out = subprocess.run(
            ["git", "show", "-s", "--format=%B", sha], cwd=REPO,
            capture_output=True, text=True, timeout=30)
        return out.stdout if out.returncode == 0 else ""
    except Exception:
        return ""


def read_src(fname: str) -> str:
    with open(os.path.join(HERE, fname), "r", encoding="utf-8") as fh:
        return fh.read()


def exact_mp_roots(cell: dict) -> tuple[np.ndarray, int, int, mp.mpf]:
    """Honest census: pure mp polynomial roots of lane 1's numerator
    polynomial, NO float64 refinement.  Returns (real zeros, n_imag,
    n_cplx, first-zero-minus-cache-gamma1 as mpf)."""
    K = cell["K"]
    with mp.workdps(cell["dps"]):
        aa_mp = mp.log(cell["x"]) / 2
        b = [(k * mp.pi / aa_mp) ** 2 for k in range(1, K)]
        s_mp = b[-1] + 1
        b = [v / s_mp for v in b]
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]

        def pmul(p, q):
            out = [mp.mpf(0)] * (len(p) + len(q) - 1)
            for i, pv in enumerate(p):
                for j, qv in enumerate(q):
                    out[i + j] += pv * qv
            return out

        def padd(p, q):
            if len(p) < len(q):
                p, q = q, p
            out = list(p)
            off = len(p) - len(q)
            for j, qv in enumerate(q):
                out[off + j] += qv
            return out

        def deflate(p, root):
            out = [p[0]]
            for c in p[1:-1]:
                out.append(c + out[-1] * root)
            return out

        prod_all = [mp.mpf(1)]
        for bj in b:
            prod_all = pmul(prod_all, [mp.mpf(1), -bj])
        poly = [2 * cs[0] * c for c in prod_all]
        for i, k in enumerate(range(1, K)):
            q = deflate(prod_all, b[i])
            term = [2 * cs[k] * ((-1) ** k) * c for c in q] + [mp.mpf(0)]
            poly = padd(poly, term)
        rts = mp.polyroots(poly, maxsteps=600, extraprec=2 * cell["dps"])
        im_tol = mp.mpf(10) ** (-(cell["dps"] // 4))
        reals_mp = []
        n_imag = n_cplx = 0
        for r in rts:
            y = r * s_mp
            if abs(mp.im(y)) <= im_tol * s_mp:
                if mp.re(y) > 0:
                    reals_mp.append(mp.sqrt(mp.re(y)))
                else:
                    n_imag += 1
            else:
                n_cplx += 1
        reals_mp.sort()
        gam1 = np.load(CACHE_N7000)[0]
        dz1 = (reals_mp[0] - mp.mpf(float(gam1))
               if reals_mp else mp.mpf("nan"))
        return (np.array([float(v) for v in reals_mp]), n_imag, n_cplx,
                dz1)


def disp_stats(zeros: np.ndarray, x: int, gammas: np.ndarray):
    """Lane 1's target_displacements logic, reproduced."""
    band = min(0.8 * 2.0 * math.pi * x, 400.0)
    zc = zeros[zeros <= band]
    gg = gammas[gammas <= band]
    k = min(len(zc), len(gg))
    if k < 3:
        return None
    d = zc[:k] - gg[:k]
    spac = np.diff(gg[: k + 1]) if len(gg) > k else np.diff(gg[:k])
    ms = float(np.mean(spac))
    return (k, float(np.mean(np.abs(d))),
            float(np.mean(np.abs(d)) / ms))


def type_row(es: list[float]) -> str:
    nf = lane1.NF_EPS
    steps_ok = 0
    for i in range(len(es) - 1):
        if es[i] <= 10 * nf and es[i + 1] <= 10 * nf:
            steps_ok += 1
        elif es[i + 1] <= lane1.WOBBLE * es[i]:
            steps_ok += 1
    if es[-1] <= es[0] / lane1.DROP_BAR_HP and steps_ok >= len(es) - 2:
        return "CONVERGES"
    if es[-1] > 2.0 * es[0] and es[-1] > 10 * nf:
        return "DIVERGES"
    return "PLATEAU"


def main() -> int:
    global X_RE
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = bool(args.smoke)
    if smoke:
        X_RE = (3, 5)

    print("=" * 78)
    print("bughunt_r79_r85_probe  ADVERSARIAL INSTRUMENT AUDIT r79-r85")
    print("FROZEN SPEC_SHA %s%s" % (SPEC_SHA[:16],
          "   *** SMOKE -- NOT VERDICT-BEARING ***" if smoke else ""))
    print("=" * 78)

    # ================================================= I. comparator
    section("I. COMPARATOR FLOOR (the cache's own quantization)")
    gammas = np.asarray(np.load(CACHE_N7000), float)
    with mp.workdps(40):
        # mp.mpf(float) converts the BINARY double exactly (repr would
        # re-parse the shortest decimal and overstate by ~4e-16)
        cache_q = float(mp.mpf(float(gammas[0])) - mp.mpf(GAMMA1_30))
    check("I1 cache health + gamma_1 quantization vs 30-digit"
          " literature value",
          len(gammas) >= 5000 and bool(np.all(np.diff(gammas) > 0))
          and abs(cache_q) < CACHE_Q_BAR,
          "n=%d  cache gamma_1 - literature = %+.3e (bar %.0e):"
          " every sub-1e-14 'tracking' digit is below this floor"
          % (len(gammas), cache_q, CACHE_Q_BAR))

    # ============================================== II. text pins (B1)
    section("II. TEXT PINS -- the wrong strings, where they live")
    b83 = git_body("23ea7f9a")
    b84 = git_body("806197a5")
    git_ok = bool(b83) and bool(b84)
    if not git_ok:
        check("II0 git history reachable", True,
              "git unavailable -- commit-text findings carried as"
              " DATA only")
    check("G-F1a commit 23ea7f9a carries the fused pair '7.1e-15"
          " (0.16 percent of mean spacing)'",
          (not git_ok) or ("zeros track ordinates to 7.1e-15 (0.16"
                           " percent of mean spacing)" in b83),
          "pinned in immutable history (standing correction = this"
          " audit)")
    tpda_doc = read_src("tp_da_probe.py")
    check("G-F1b tp_da docstring repeats the blanket 'zeros tracking"
          " ordinates to 7e-15'",
          "zeros tracking ordinates to 7e-15" in tpda_doc,
          "first-zero-only readout quoted as a blanket claim")
    arb_src = read_src("realroot_arbiter_probe.py")
    nxt = open(os.path.join(REPO, "experiments", "next.txt"),
               encoding="utf-8").read()
    check("G-F2a the '36-vs-3 in (0,30)' pairing lives in the arbiter"
          " print, note CCCLXXXIII and commit 23ea7f9a",
          ("36-vs-3 in (0,30)" in arb_src)
          and ("36-vs-3 in (0,30)" in nxt)
          and ((not git_ok)
               or "36 nodes vs 3 zeros in (0,30) at x = 55" in b83),
          "two-sided nodes paired with one-sided zeros")
    check("G-F3a commit 806197a5 carries 'within 10 percent'",
          (not git_ok) or ("within 10 percent" in b84), "")
    check("G-F4a commit 23ea7f9a carries 'converges on all four (to"
          " 2.3e-06)'",
          (not git_ok) or ("converges on all four (to 2.3e-06)" in b83),
          "")
    check("G-F8a commit 23ea7f9a carries 'tau-screen slopes"
          " 0.019-0.043 ALL PASS'",
          (not git_ok) or ("tau-screen slopes 0.019-0.043 ALL PASS"
                           in b83), "")

    # ====================================== III. gate-vacuity census
    section("III. F5 -- HARDCODED-TRUE GATE CENSUS (AST)")
    found = {}
    for fname in EXPECT_TRUE_GATES:
        tree = ast.parse(read_src(fname))
        n_true = 0
        for node in ast.walk(tree):
            if (isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Name)
                    and node.func.id == "check"
                    and len(node.args) >= 2
                    and isinstance(node.args[1], ast.Constant)
                    and node.args[1].value is True):
                n_true += 1
        found[fname] = n_true
    check("G-F5 the vacuous-gate census matches the frozen expectation"
          " (semilocal 1, arbiter 2, sat 3, untested 2, birdseye 1,"
          " all others 0 -- 9 total)", found == EXPECT_TRUE_GATES,
          "%s" % {k.split("_")[0]: v for k, v in found.items()
                  if v})

    # ============================================ IV. band constants
    section("IV. TAU-SCREEN BANDS + F9 DEAD-CODE PINS")
    l1s = read_src("semilocal_realroot_limit_probe.py")
    tps = read_src("tp_sol_probe.py")
    sol2 = read_src("stc_sol_convergence_probe.py")
    unt = read_src("untested_sign_sources_probe.py")
    check("G-B2 every tau-screen in the corpus uses the frozen atlas"
          " bands 0.30 / 0.70",
          ("TAU_PASS = 0.30" in l1s and "TAU_RELOC = 0.70" in l1s
           and "TAU_PASS = 0.30" in tpda_doc
           and "TAU_RELOC = 0.70" in tpda_doc
           and "SLOPE_PASS = 0.30" in unt
           and "SLOPE_RELOC = 0.70" in unt), "no band drift")
    check("G-F9 dead code pinned: lane1 duplicate b-build; tp_sol"
          " unused em; stc_sol unused EULER_FLOAT",
          ("b = [mp.mpf(float(om[i] ** 2)) for i in range(1, K)]"
           in l1s)
          and ("em = profile(cell, base_vector," in tps
               and tps.count(" em ") <= 1)
          and sol2.count("EULER_FLOAT") == 1,
          "cosmetic only")

    # ================================================ V. mesh (F2-F4)
    section("V. LANE-3 RECOMPUTES (F2 pairing, F3 Nyquist, F4 finals)")
    r55 = lane3.run_rung(55)
    tp55 = r55["tau"][r55["tau"] > 0]
    one55 = int((tp55 < 30.0).sum())
    two55 = int((np.abs(r55["tau"]) < 30.0).sum())
    check("R-F2b lane 3's own builder at x = 55: one-sided (0,30)"
          " = %d, two-sided |tau|<30 = %d" % (one55, two55),
          one55 == MESH55_ONE and two55 == MESH55_TWO,
          "honest pairing 18-vs-3 (one-sided) or 36-vs-6 (two-sided);"
          " the published 36-vs-3 mixes them")
    mesh_x = (5, 8, 13, 21, 34, 55, 89, 144)
    devs = []
    r_by_x = {55: r55}
    for x in mesh_x:
        r = r_by_x.get(x) or lane3.run_rung(x)
        r_by_x[x] = r
        tp = r["tau"][r["tau"] > 0]
        c30 = int((tp < 30.0).sum())
        upred = 30.0 * r["ell"] / (2.0 * math.pi)
        devs.append(abs(c30 / upred - 1.0))
    n_over = sum(1 for d in devs if d > NYQ_DEV_LO)
    check("R-F3b Nyquist tracking deviations: max %.4f, %d rungs over"
          " 10%% (x = 13/21/34)" % (max(devs), n_over),
          NYQ_DEV_LO < max(devs) < NYQ_DEV_HI and n_over == NYQ_OVER10,
          "devs: %s" % " ".join("%.3f" % d for d in devs))
    bat3 = lane3.make_battery(lane3.B_FIX)
    r5 = r_by_x[5]
    r144 = r_by_x[144]
    wt_firsts, wt_finals = [], []
    for (nm3, kf, k0, kp0, brk, hf3) in bat3:
        tgt = lane3.weil_of_kernel(kf, k0, kp0, lane3.B_FIX, brk,
                                   r144["au"], r144["am"])[0]
        wt_firsts.append(abs(float(np.dot(r5["w"], hf3(r5["tau"])))
                             - tgt))
        wt_finals.append(abs(float(np.dot(r144["w"],
                                          hf3(r144["tau"]))) - tgt))
    check("R-F4b lane-3 weighted finals: %s -- all four converge, but"
          " only ONE reaches 2.3e-06"
          % " ".join("%.1e" % v for v in wt_finals),
          all(f < 0.2 * i for f, i in zip(wt_finals, wt_firsts))
          and max(wt_finals) > WT_MAX_FINAL_MIN,
          "the commit's '(to 2.3e-06)' is the best row, not all four")

    # ======================================= VI. lane-1 honest census
    section("VI. F1/F6/F7 -- LANE-1 RECOMPUTE AT HONEST PRECISION"
            " (pure mp roots vs the float64-refined instrument)")
    src_tab = {bm: lane1.src_of_battery(*bm) for bm in lane1.BATTERY}
    eps_ref = {bm: [] for bm in lane1.BATTERY}
    eps_hon = {bm: [] for bm in lane1.BATTERY}
    tau_logs = []
    cells = {}
    ok_census = True
    dz1_ref = {}
    dz1_hon = {}
    lowband = {}
    for x in X_RE:
        t0 = time.time()
        cell = lane1.build_trig_cell_hp(x, lane1.KFAC, "MAIN", DPS[x])
        lane1.hp_zero_data(cell)              # lane 1's instrument
        z_ref = cell["zeros"]
        z_ex, n_im, n_cx, dz1 = exact_mp_roots(cell)
        cells[x] = (cell, z_ex)
        tau_logs.append(cell["tau_log10"])
        ok_census &= (len(z_ref) == len(z_ex) == cell["K"] - 1
                      and n_im == 0 and n_cx == 0)
        cut = 0.75 * float(cell["om"][-1])
        dev = (np.abs(z_ref - z_ex) if len(z_ref) == len(z_ex)
               else np.array([np.inf]))
        lo_mask = z_ex < cut if len(z_ref) == len(z_ex) else None
        lowband[x] = (float(np.max(dev[lo_mask]))
                      if lo_mask is not None and lo_mask.any() else 0.0)
        dz1_ref[x] = float(z_ref[0]) - float(gammas[0])
        dz1_hon[x] = float(dz1)
        print("    x=%2d  census %d/%d both instruments  low-band"
              " max|z_ref-z_exact| %.2e  dz1 ref %+.3e exact %+.3e"
              "  %.0fs"
              % (x, len(z_ref), cell["K"] - 1, lowband[x], dz1_ref[x],
                 dz1_hon[x], time.time() - t0))
        for bm in lane1.BATTERY:
            eps_ref[bm].append(lane1.trig_eps(cell, *bm, src_tab[bm]))
            cell_sw = dict(cell)
            cell_sw["zeros"] = z_ex
            eps_hon[bm].append(lane1.trig_eps(cell_sw, *bm,
                                              src_tab[bm]))
    check("R-C1 census counts identical on both instruments (0 imag,"
          " 0 complex, K-1 real everywhere)", ok_census,
          "the bug moves POSITIONS, not counts")
    if not smoke:
        check("R-F1c the honest first-zero read sits AT the comparator"
              " floor at x = 8 AND x = 13 (|dz1_exact| < %.0e); the"
              " published reads are refinement noise (>= %gx larger)"
              % (EXACT_DZ1_BAR, NOISE_FACTOR),
              all(abs(dz1_hon[x]) < EXACT_DZ1_BAR for x in (8, 13))
              and all(abs(PUB_DZ1[x]) > NOISE_FACTOR * abs(dz1_hon[x])
                      for x in (8, 13))
              and all(abs(dz1_ref[x] - PUB_DZ1[x])
                      < 0.15 * abs(PUB_DZ1[x]) for x in (8, 13)),
              "exact %+.2e / %+.2e vs published %+.2e / %+.2e"
              % (dz1_hon[8], dz1_hon[13], PUB_DZ1[8], PUB_DZ1[13]))
        d_ref = disp_stats(cells[13][0]["zeros"], 13, gammas)
        d_hon = disp_stats(cells[13][1], 13, gammas)
        check("R-F1d the published mean-displacement 0.0016*spacing at"
              " x = 13 is 100%% refinement artifact: honest mean = %.1e"
              % d_hon[1],
              d_ref is not None and d_hon is not None
              and d_ref[1] > MEAN_DISP_REF_MIN
              and d_hon[1] < MEAN_DISP_EXACT_MAX
              and abs(d_ref[2] - 0.0016) < 5e-4,
              "refined mean %.3e (rel %.4f) vs exact mean %.3e over"
              " k=%d matched zeros" % (d_ref[1], d_ref[2], d_hon[1],
                                       d_hon[0]))
        check("R-F6a the corruption reaches BELOW 0.75 om_max at"
              " x = 13 (max %.2e > %.0e) while x = 8 holds tp_da's"
              " W4 bar (%.2e < %.0e): tp_da's cross-ward subsample"
              " (x = 5/8) did not support the deepest rung"
              % (lowband[13], LOWBAND_REF_MIN, lowband[8],
                 LOWBAND_MAX8),
              lowband[13] > LOWBAND_REF_MIN
              and lowband[8] < LOWBAND_MAX8, "")
    moves = []
    flips = 0
    live_rows = 0
    for bm in lane1.BATTERY:
        er, eh = eps_ref[bm], eps_hon[bm]
        move = max(abs(a - b) / max(b, 1e-300) for a, b in zip(er, eh))
        moves.append(move)
        t_r, t_h = type_row(er), type_row(eh)
        if t_r != t_h:
            flips += 1
        live = sum(1 for tl, e in zip(tau_logs, er)
                   if e > 10 * lane1.NF_EPS and tl > -290)
        if live >= 3:
            live_rows += 1
        print("    B=%.1f m=%d  ref %s / honest %s  max rel eps move"
              " %.2f  finals %.3e -> %.3e"
              % (bm[0], bm[1], t_r, t_h, move, er[-1], eh[-1]))
    if not smoke:
        check("R-F6b published eps values move by up to %.0f%% under"
              " the honest census, yet NO row typing flips (6/6 stay"
              " CONVERGES) -- REALROOT-ARCHITECTURE-OPEN stands"
              % (100.0 * max(moves)),
              max(moves) > EPS_MOVE_MIN and flips == 0
              and all(type_row(eps_hon[bm]) == "CONVERGES"
                      for bm in lane1.BATTERY),
              "the published digit strings are instrument-specific;"
              " the typings are not")
        rep_ok = all(abs(eps_ref[bm][-1] - PUB_EPS13[bm])
                     < 0.02 * PUB_EPS13[bm] for bm in lane1.BATTERY)
        check("R-F6c the refined instrument reproduces the published"
              " x = 13 finals bit-similar (rel < 0.02) -- the drift is"
              " the bug, not this rerun", rep_ok,
              "published finals re-derived from lane 1's own path")
        check("R-F8b tau-screen row applicability: exactly %d of 6"
              " rows are live (>= 3 points above 10 NF); the other 2"
              " are NOT-APPLICABLE -- 'ALL PASS' covers 4 rows"
              % live_rows, live_rows == 4, "")
        # arbiter Q3 extremal rows, both instruments
        ok_arb = True
        for (nm, hf, ff, f0, Bb) in arb.unified_battery():
            src = lane1.src_value(
                lambda v: np.asarray(ff(np.abs(v)), float), f0, Bb)
            ef_r, ef_h = [], []
            for x in (5, 8, 13):
                cell, z_ex = cells[x]
                ef_r.append(arb.ext_eps(cell, hf, src, True))
                cell_sw = dict(cell)
                cell_sw["zeros"] = z_ex
                ef_h.append(arb.ext_eps(cell_sw, hf, src, True))
            if nm in ARB_PUB:
                pf, pl = ARB_PUB[nm]
                ok_arb &= (abs(ef_r[0] - pf) < 0.05 * pf
                           and abs(ef_r[-1] - pl) < 0.05 * pl)
            ok_arb &= (arb.row_type(ef_h[0], ef_h[-1]) == "CONVERGES")
            print("    arb %-20s ref %s | honest %s"
                  % (nm, " ".join("%.2e" % v for v in ef_r),
                     " ".join("%.2e" % v for v in ef_h)))
        check("R-F6d the arbiter's published Q3 extremal rows"
              " reproduce (rel < 0.05) AND still type CONVERGES on"
              " the honest census -- REALROOT-DEPTH-UNDECIDED stands",
              ok_arb, "")
        t0 = time.time()
        zs100 = arb.mp_profile_scan(cells[13][0], 100.0)
        z_ex13 = cells[13][1]
        n_scan = len(zs100)
        n_exact = int((z_ex13 < 100.0).sum())
        check("R-F7b the previously unwarded (60,100) scan band is"
              " warded NOW: mp-scan (0,100) at x = 13 finds %d =="
              " exact census %d (%.0fs) -- the x = 21 (0,100) = 29"
              " methodology survives" % (n_scan, n_exact,
                                         time.time() - t0),
              n_scan == n_exact, "")

    # ================================================== VII. verdict
    section("VII. FINDINGS LEDGER + COMPOSITE VERDICT")
    for (fid, loc, what, before, after, flip) in FINDINGS:
        print("  %s [%s]%s %s" % (fid, SEV[fid],
                                  " FLIPS-VERDICT" if flip else "",
                                  loc))
        print("      wrong : %s" % what)
        print("      before: %s" % before)
        print("      after : %s" % after)
    n_flip = sum(1 for f in FINDINGS if f[5])
    check("V1 no recorded round verdict flips (0 FATAL findings)",
          n_flip == 0, "%d findings, max severity MAJOR" % len(FINDINGS))
    wall = time.time() - T0_WALL
    check("V2 runtime", wall <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (wall, RUNTIME_BAR))

    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    max_sev = ("FATAL" if n_flip else
               "MAJOR" if any(SEV[f[0]] == "MAJOR" for f in FINDINGS)
               else "MINOR") if FINDINGS else "NONE"
    verdict = ("BUGHUNT-CLEAN" if not FINDINGS else
               "BUGHUNT-FINDINGS(%d, max %s)" % (len(FINDINGS),
                                                 max_sev))
    print("\n" + "=" * 78)
    print("CHECKS %d/%d PASS   runtime %.1f s   SPEC_SHA %s"
          % (n_pass, len(CHECKS), wall, SPEC_SHA[:16]))
    print("VERDICT: %s" % verdict)
    print("(the probe's PASS = the audit is consistent, NOT 'no"
          " bugs'; the bugs are the FINDINGS above)")
    if smoke:
        print("*** SMOKE RUN -- NOT VERDICT-BEARING ***")
    print("NO RH CLAIM. NO POSITIVITY CLAIM. EXPLORATION ONLY.")
    print("=" * 78)
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
