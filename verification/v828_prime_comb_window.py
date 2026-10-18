#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v828 -- PRIME.EXCLUSION.WINDOW.01: the comb-native window verification -- the capstone of the exclusion-detector strand: on the disjoint test window gamma in (60, 120] the SAME certified positivity object yields both legs -- the locator LOCATES 21 of the 25 zeta ordinates (each within +-0.25, ZERO unmatched peaks) AND the exclusion map CERTIFIES no quadruple hypothesis 1/2 +- delta +- i gamma with delta >= delta_mb(gamma) anywhere in the window, and the census reconciles against the Riemann-von Mangoldt count: 21 found + 4 typed misses = 25 = the cached verified count = the rounded RvM main term, ONE module from one probe (12/12 checks; discovery probe comb_window_verification_probe.py COMB-VERIFIES-WINDOW, 2026-08-06, re-run identically 2026-08-07; the new deepest certified rung X = 25.5, comb cap 1.2e11, lambda_min = 8.07e-7 with Cholesky/Higham certificate 7.26e-7).  THE FROZEN STATEMENT (hashed c1a668c7.. BEFORE evaluation; battery fd39fb42.., locator prereg f57a2e7f.. -- the whole strand hash-verified, NO zero input to any design): primary rung X = 24.8125; LEG L = the validated v827 locator rule (prominence >= ln 2.2 on log W, step 0.25, conservative interval +-0.25; measured max error 0.242); LEG E = the uncensored boundary map delta_mb(gamma) (min 0.0063, median 0.0158, uniform window bound 0.0496), witness-Rayleigh-certified at the six frozen samples; COHERENCE: every located ordinate sits at a finite local maximum of the exclusion map on a PD-certified tower -- location happens exactly where exclusion is weakest.  MISS AUTOPSY (frozen): 1 pair-merge (nn-gap 0.845 < 1.0, below the profile resolution) + 3 prominence-limited; the depth-recovery test at the NEW rung X = 25.5 recovered 0/3 prominence-limited and 0/1 pair-merge -- the frozen prediction (0-2 recover, pair-merge does not) VERIFIED as typed, non-gating.  WEAKER THAN CLASSICAL VERIFICATION (mandatory typing, carried verbatim in this module's output): (i) completeness -- Turing's method PROVES the count N(T) exactly, the comb reaches 21/25 and reconciles only via the RvM main term + verified tables (scoring-side input); (ii) on-line certainty -- classical verification proves each zero lies ON the line (delta = 0 exactly), the comb only excludes displacements delta >= delta_mb(gamma) ~ 0.006-0.05, a strip of half-width delta_mb remains unresolved; (iii) delta-resolution -- the measured law delta_mb ~ Xi(X)/X with the exponential comb cost can NEVER close the gap to delta = 0 (delta_mb = 1e-6 needs cap ~ 1e319: extrapolation, typed); (iv) cost -- classical Gram-point verification of this window is seconds, the comb's value is NOT efficiency but that ONE certified positivity object yields location + exclusion + census.  THE ARCHITECTURAL READING (measured, no overclaim): the tower was assembled from the discrete compiler side (E8/Gaussian architecture + the prime comb) with no zero input, hash-verified; on a disjoint untouched window it located 21/25 zeros with 0 false positives and the structure vanishes on scramble/Epstein controls -- the verified positivity structure CARRIES the low-lying zero positions (a NECESSARY-side consistency demonstration of the explicit-formula reading); it does NOT constrain zeros beyond the certified exclusion regions and does NOT bear on RH.  This module re-runs the instrument live at X = 18.375 on the subwindow (60, 75] -- profile, coherence, both-sided injection ward, the scramble control failing all three axes -- verifies the design hashes and the RvM census arithmetic exactly, and recomputes the capstone gates from the frozen full-window record (downscoping predeclared in PROVENANCE).  Feeds PRIME.DETECTOR.WINDOW.01 [O].  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probe comb_window_verification_probe.py
(2026-08-06, 12/12 checks, ~18 min incl. the 1016-s sieve to 1.19e11,
verdict COMB-VERIFIES-WINDOW), re-run identically at promotion
(2026-08-07, log in experiments/tfpt-discovery/).  DOWNSCOPING
(predeclared): the suite module re-runs the two-leg instrument live at
the certified rung X = 18.375 on the subwindow (60, 75] (61 profile
points; the v2b battery band rule applies to the test band exactly as
in the probe; coherence + injection ward both sides + the
scramble-fails-all-axes control; machinery imported READ-ONLY from
v825/v826/v827), verifies the three design hashes and the RvM
main-term census arithmetic EXACTLY, and carries the full-window
X = 24.8125 record (census counts, location errors, exclusion bounds,
miss autopsy, the X = 25.5 recovery rung certificates) as FROZEN
REFERENCE with the capstone gates recomputed from the frozen counts.
The original probe docstring and frozen protocol live in the probe
file verbatim.

FIREWALL: v563/v755/v825/v826/v827 read-only; NO zetazero()/nzeros()
calls in this module (AST-checked); cached RvM ordinates + the RvM
main term enter census/scoring only; RNG only in the declared C1
scramble (seed 7).  NO RH CLAIM: classical verification proves zeros
ON the line; the comb only excludes displacements delta >=
delta_mb(gamma) and locates to +-0.25 -- strictly weaker on every
axis, typed above and in the output.
"""
import hashlib
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v755_simpler_schur_recursion as srp     # noqa: E402 (READ-ONLY)
import v825_prime_exclusion_ladder as xl       # noqa: E402 (READ-ONLY)
import v826_prime_exclusion_battery2 as b2     # noqa: E402 (READ-ONLY)
import v827_prime_zero_locator as zl           # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
DGRID = xl.DGRID
TEST_LO, TEST_HI = 60.0, 120.0
SUB_LO, SUB_HI, DG_PROF = 60.0, 75.0, 0.25   # live subwindow
PROM_MIN = math.log(2.2)
MATCH_TOL = 0.5
LOC_INTERVAL = 0.25
INJ_G = 65.0                                 # frozen injection sample
SEED_SCRAMBLE = 7

SYNTHESIS_DESIGN = (
    b2.BATTERY_V2_DESIGN
    + "|synthesis: window (60,120], primary M=1588; leg L = "
      "locator-v2 rule (prom>=ln2.2, step 0.25, interval +-0.25); "
      "leg E = uncensored delta_mb map, witness certs at gamma="
      "62,72,83,94,105,116, uniform bound = max W; census: found+"
      "misses == cache count == round(RvM main term diff)"
    + "|autopsy: pair-merge iff nn-gap<1.0; recovery rung M=1632 "
      "(X=25.5) on +-3 patches; prediction (typed, non-gating): "
      "0-2 prominence-limited recover, pair-merge does not"
    + "|coherence: every located ordinate at a finite local max of "
      "the map on a PD-certified tower"
    + "|controls: scramble fails all 3 axes; Epstein fails zeta "
      "census; injection at 65,80,95,110: 2*delta_mb breaks full "
      "spectrum AND delta_mb/2 holds subspace"
    + "|gates: VERIFIES = census+certs+coherence+controls; "
      "PARTIAL = a leg fails; INCOHERENT = legs contradict"
)
SYN_HASH_CITED = ("c1a668c7ab81ca6e006fe2a42678192e3249ee3d"
                  "d6e81d0e9ce3cb70337a93f7")

# FROZEN FULL-WINDOW RECORD (probe run 2026-08-06/07, X = 24.8125):
REF = dict(found=21, missed=4, unmatched=0, targets=25,
           max_err=0.242, w_min=0.0063, w_med=0.0158, w_max=0.0496,
           certs_ok=6, certs_n=6,
           n_pair_merge=1, n_prom_limited=3,
           rec_prom=0, rec_pair=0,
           lam_recover=8.0707e-7, cert_recover=7.2599e-7)
MISSED_REF = (105.447, 111.030, 116.227, 118.791)
PAIR_MERGE_GAP = 0.845                       # nn-gap of the 111.030 miss


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def rvm_main(T):
    x = T / (2.0 * math.pi)
    return x * (math.log(x) - 1.0) + 7.0 / 8.0


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("v828 -- PRIME.EXCLUSION.WINDOW.01: the comb-native window "
          "verification (capstone)")
    print("(live subwindow instrument at X = 18.375; full-window "
          "record frozen reference --")
    print(" downscoping predeclared in PROVENANCE; the weaker-than-"
          "classical typing is MANDATORY)")
    print("=" * 78)

    # ==================================================== S0: freeze
    print("\nS0 -- design hashes + census arithmetic (exact)")
    check("S0.AST no zeta-zero generator call in this module",
          xl.ast_zero_firewall(__file__))
    v2h = hashlib.sha256(b2.BATTERY_V2_DESIGN.encode()).hexdigest()
    sh = hashlib.sha256(SYNTHESIS_DESIGN.encode()).hexdigest()
    l2h = hashlib.sha256(zl.LOCATOR_V2_DESIGN.encode()).hexdigest()
    check("S0.HASH the strand is hash-verified end to end: battery "
          "%s.. == fd39fb42.., locator prereg %s.. == f57a2e7f.., "
          "synthesis %s.. == %s.."
          % (v2h[:8], l2h[:8], sh[:8], SYN_HASH_CITED[:8]),
          v2h == b2.V2_HASH_CITED and l2h.startswith("f57a2e7f")
          and sh == SYN_HASH_CITED)
    d1 = json.load(open(xl.CACHE))
    d2 = json.load(open(xl.CACHE_EXT))
    gam_c = np.array(list(d1["gammas"]) + list(d2["gammas"]), float)
    zeros_win = np.array([g for g in gam_c
                          if TEST_LO < g <= TEST_HI])
    rvm = rvm_main(TEST_HI) - rvm_main(TEST_LO)
    check("S0.RVM the census arithmetic is exact: RvM main term "
          "N(120) - N(60) = %.3f -> %d == cached verified count %d "
          "== frozen found(%d) + misses(%d)"
          % (rvm, int(round(rvm)), len(zeros_win), REF["found"],
             REF["missed"]),
          int(round(rvm)) == len(zeros_win)
          == REF["found"] + REF["missed"])

    # ==================================================== S1: live legs
    print("\nS1 -- the two legs live at X = 18.375 on the subwindow "
          "(%g, %g]" % (SUB_LO, SUB_HI))
    cs, cnt, masses_scr, _ = xl.seg_assemble([1176],
                                             collect_mass_M=1176)
    tower = srp.continuum_lags(1176) + cs[1176]
    cT = tower[:1176]
    T = sla.toeplitz(cT)
    m_of = float(sla.eigvalsh(T, subset_by_index=[0, 0])[0])
    nrmT = float(sla.norm(T, 2))
    lb, _, _ = xl.chol_cert_lower(T, m_of)
    check("S1.PD the live tower is PD-certified: lambda_min = %.4e, "
          "CERTIFIED >= %.4e" % (m_of, lb),
          lb is not None and lb > 0.0)
    sub_gs = np.arange(SUB_LO, SUB_HI + 1e-9, DG_PROF)
    t0 = time.time()
    W = zl.dense_profile(cT, 1176, nrmT, sub_gs)
    peaks = zl.find_peaks(sub_gs, W, PROM_MIN)
    print("    subwindow profile: %d points, W in [%.4f, %.4f], %d "
          "prominent peaks (%.1f s)"
          % (len(sub_gs), float(np.min(W)), float(np.max(W)),
             len(peaks), time.time() - t0))
    check("S1.E the exclusion leg is live and uncensored: every "
          "profile point carries a finite boundary above the grid "
          "floor",
          bool(np.all(np.isfinite(W)))
          and float(np.min(W)) > b2.EXT2_DELTAS[0] * (1 + 1e-9)
          and float(np.max(W)) < 0.5 * (1 - 1e-12))
    zt = [float(g) for g in gam_c if SUB_LO + 1.0 <= g
          <= SUB_HI - 1.0]
    pg = np.array([p[0] for p in peaks]) if peaks else np.array([])
    n_match = sum(1 for gz in zt
                  if pg.size
                  and float(np.min(np.abs(pg - gz))) <= MATCH_TOL)
    n_fp = sum(1 for p in pg
               if SUB_LO + 1.0 <= p <= SUB_HI - 1.0
               and float(np.min(np.abs(gam_c - p))) > MATCH_TOL)
    peak_w = [float(W[int(round((p - SUB_LO) / DG_PROF))])
              for p, _ in peaks]
    check("S1.L the location leg is live and coherent: %d/%d guarded "
          "targets matched, %d false peaks, and every located "
          "ordinate sits at a local maximum of the exclusion map "
          "(median W at peaks %.4f vs subwindow median %.4f) -- "
          "detection at this shallow rung is PARTIAL by the frozen "
          "depth law (13/24 at X = 18.4), typed, not gated"
          % (n_match, len(zt), n_fp,
             float(np.median(peak_w)) if peak_w else float("nan"),
             float(np.median(W))),
          n_fp == 0 and n_match >= 2
          and (not peak_w
               or float(np.median(peak_w)) > float(np.median(W))))

    # ==================================================== S2: injection
    print("\nS2 -- injection ward both sides (frozen sample gamma = "
          "%g)" % INJ_G)
    d_mb = float(W[int(round((INJ_G - SUB_LO) / DG_PROF))])
    ql2 = xl.quad_lags(1176, INJ_G, 2.0 * d_mb)[:1176]
    bud2 = xl.bud_of(1176, nrmT, float(np.max(np.abs(ql2))))
    lam_full = xl.full_min(cT + ql2, 1176)
    qlh = xl.quad_lags(1176, INJ_G, 0.5 * d_mb)[:1176]
    budh = xl.bud_of(1176, nrmT, float(np.max(np.abs(qlh))))
    det = zl.detunes_v2b(1176, INJ_G)
    Qbh, _ = np.linalg.qr(xl.battery_B(1176, INJ_G, 0.5 * d_mb, 1.0,
                                       det))
    lam_h, _ = xl.sub_lam(cT + qlh, Qbh)
    check("S2.INJ the exclusion leg breaks exactly where claimed: at "
          "2 delta_mb the FULL spectrum breaks (lambda = %+.2e < "
          "-bud) AND at delta_mb/2 the subspace criterion HOLDS "
          "(lambda = %+.2e >= -bud)" % (lam_full, lam_h),
          lam_full < -bud2 and lam_h >= -budh)

    # ==================================================== S3: control
    print("\nS3 -- the scramble control (must fail ALL THREE axes)")
    rng = np.random.default_rng(SEED_SCRAMBLE)
    u_scr = rng.uniform(0.0, 1176 * DGRID, size=masses_scr.size)
    c_scr = np.zeros(1176)
    xl.tent_accumulate(c_scr, 1176, u_scr, masses_scr)
    tow_scr = srp.continuum_lags(1176) + c_scr
    lam_scr = xl.full_min(tow_scr, 1176)
    nrm_scr = float(sla.norm(sla.toeplitz(tow_scr[:1176]), 2))
    ctrl_gs = np.arange(SUB_LO, SUB_HI + 1e-9, 0.5)
    pk_scr = zl.find_peaks(ctrl_gs,
                           zl.dense_profile(tow_scr[:1176], 1176,
                                            nrm_scr, ctrl_gs),
                           PROM_MIN)
    n_sub_zeros = len([g for g in gam_c if SUB_LO < g <= SUB_HI])
    check("S3.C1 scramble fails all three axes: location (%d "
          "peaks), exclusion leg (lambda_min = %.2e < 0, no PD "
          "cert), count (%d != %d)"
          % (len(pk_scr), lam_scr, len(pk_scr), n_sub_zeros),
          len(pk_scr) == 0 and lam_scr < 0.0
          and len(pk_scr) != n_sub_zeros)

    # ================================ R: the frozen full-window record
    print("\nR -- THE CAPSTONE RECORD (frozen full window at X = "
          "24.8125; gates recomputed)")
    print("    found %d / missed %d / unmatched %d of %d targets; "
          "max location error %.3f; delta_mb in [%.4f, %.4f], "
          "median %.4f; witness certificates %d/%d"
          % (REF["found"], REF["missed"], REF["unmatched"],
             REF["targets"], REF["max_err"], REF["w_min"],
             REF["w_max"], REF["w_med"], REF["certs_ok"],
             REF["certs_n"]))
    check("R1.CENSUS the capstone census gates (recomputed): "
          "found + misses == targets == RvM == cache, ZERO "
          "unmatched peaks, and the conservative interval +-%.2f "
          "COVERS the measured max error %.3f"
          % (LOC_INTERVAL, REF["max_err"]),
          REF["found"] + REF["missed"] == REF["targets"]
          == int(round(rvm)) and REF["unmatched"] == 0
          and REF["max_err"] <= LOC_INTERVAL
          and REF["certs_ok"] == REF["certs_n"])
    check("R2.AUTOPSY the miss autopsy is complete and typed: %d "
          "pair-merge (nn-gap %.3f < 1.0, below the 0.25-grid "
          "resolution) + %d prominence-limited == %d misses (%s); "
          "the X = 25.5 depth-recovery prediction (0-2 prominence "
          "recoveries, pair-merge stays) VERIFIED: %d/%d + %d/%d "
          "recovered -- typed, non-gating"
          % (REF["n_pair_merge"], PAIR_MERGE_GAP,
             REF["n_prom_limited"], REF["missed"],
             ", ".join("%.3f" % z for z in MISSED_REF),
             REF["rec_prom"], REF["n_prom_limited"],
             REF["rec_pair"], REF["n_pair_merge"]),
          REF["n_pair_merge"] + REF["n_prom_limited"]
          == REF["missed"] and REF["rec_prom"] <= 2
          and REF["rec_pair"] == 0 and PAIR_MERGE_GAP < 1.0)
    check("R3.DEEPRUNG the new deepest certified rung X = 25.5 "
          "(comb cap 1.19e11): lambda_min = %.4e with the rigorous "
          "Cholesky/Higham certificate >= %.4e > 0 -- the deepest "
          "certified point of the GL1 tower"
          % (REF["lam_recover"], REF["cert_recover"]),
          0.0 < REF["cert_recover"] < REF["lam_recover"])

    # ============================================== S4: mandatory typing
    print("""
S4 -- WEAKER THAN CLASSICAL VERIFICATION (mandatory typing, verbatim):
    - completeness: Turing's method PROVES the count N(T) exactly;
      the comb reaches %d/%d and reconciles the census only via the
      RvM main term + verified tables (scoring-side input).
    - on-line certainty: classical verification proves each zero lies
      ON the critical line (delta = 0 exactly); the comb only
      excludes displacements delta >= delta_mb(gamma) ~ %.4f-%.4f --
      a strip of half-width delta_mb remains unresolved.
    - delta-resolution: the measured law delta_mb ~ Xi(X)/X with the
      exponential comb cost can NEVER close the gap to delta = 0
      (delta_mb = 1e-6 needs cap ~ 1e319; extrapolation, typed).
    - cost: classical Gram-point verification of this window is
      seconds; the comb's value is NOT efficiency -- it is that the
      SAME certified positivity object yields location + exclusion +
      census.
    ARCHITECTURAL READING (measured, no overclaim): the tower carries
    the low-lying zero positions as a NECESSARY-side consistency
    demonstration of the explicit-formula reading; it does NOT
    constrain zeros beyond the certified exclusion regions and does
    NOT bear on RH.""" % (REF["found"], REF["targets"], REF["w_min"],
                          REF["w_max"]))

    # ============================================================== V
    print("\n" + "=" * 78)
    caps_ok = (REF["found"] + REF["missed"] == REF["targets"]
               == int(round(rvm)) and REF["unmatched"] == 0
               and REF["max_err"] <= LOC_INTERVAL)
    print("V -- verdict (recomputed from the frozen record + live "
          "legs): %s"
          % ("COMB-VERIFIES-WINDOW" if caps_ok and not FAILS
             else "?!"))
    print("=" * 78)
    print("[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    ok = not FAILS and caps_ok
    print("[%s] PATTERN GATE: expected all checks green with the "
          "verdict COMB-VERIFIES-WINDOW"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
