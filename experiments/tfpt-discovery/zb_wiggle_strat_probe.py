#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zb_wiggle_strat_probe -- PRIME.ZB.WIGGLE.STRAT.01

FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  EXPLORATORY MECHANISM
FOLLOW-UP ROUND.  This probe writes no verification module, paper,
ledger, website, manifest, Lean file or status marker.  It makes NO
RH claim in any direction and NO numerology claim.  It closes no gate
and narrows no gate.  Small surgical round on the ONE blemish of
round 187.

=======================================================================
MISSION.  r187 (zero_causal_synth_probe, SPEC c20e87eec6d158b9,
31/33, note DVIII) established the ZB off-line dose response: DEV
(delta, f) = |C - C_Z0| monotone in delta at EVERY f, FIRST-RESPONSE
(0.1, 1e-2), but ONE f-cell violated the P1 monotonicity slack at
maximum dose: DEV(0.40, 1e-4) = 15.3 > DEV(0.40, 1e-3) = 14.2 (drop
1.14 vs slack 1.0; C 115.7 vs 116.8 vs C_Z0 131.04; moved sets = the
lowest floor(f*2e6) = 200 vs 2000 zeros, NESTED, deterministic
lowest-ordinate rule; ZB null-band keys 50/51).  Taxonomy stopped at
ZERO-CAUSALITY-PARTIAL(non-monotone).  THIS round stratifies the
wiggle and adjudicates among three frozen hypotheses: (a) SELECTION
NOISE of the low-f regime -- few moved zeros => high variance in
WHICH zeros carry the response; the surface is monotone in
expectation; (b) REAL INTERFERENCE -- specific ordinates reproducibly
invert the ordering (response is not a function of dose alone,
consistent with r187 EXACT-ORDINATES-REQUIRED); (c) INSTRUMENT
ARTIFACT -- the wiggle moves with the truncation depth of the
synthesis cache.  The verdict decides whether the r187 taxonomy
honestly upgrades BY REFERENCE (r187 record NOT edited, house style).
=======================================================================
ENGINE (REUSED FAITHFULLY, no new construction): this probe IMPORTS
zero_causal_synth_probe (the frozen r187 module; identity gated on
SPEC c20e87eec6d158b9) and uses ITS functions verbatim: ward_cache7/
ward_cache_big (the only np.load sites, inside the imported module's
ward_ functions -- delegated wards, disclosed), spike_positions,
osc_dens, weights_from_dens, triv_inc, synth_weights, landau_field,
coherence, d2_eval_syn.  Same depths (D2 synthesis N_D2 = 2e6, alt
checkpoint 1e6), same window (q-1/2, q+1/2], same chunk 20000, same
detector (n7000 Landau field, grid 4096, INTRAND band for W5/Z0,
family-33 keyed 20-scramble bands for the two record ZB cells).
Round is S2-ONLY (the wiggle lives in the S2 dose surface; the S1
lane was SYNTH-S1-DEAD-PREDICTED in r187) -- disclosed A0(i).

FROZEN CELLS.  delta* = 0.4 (beta* = 0.9) throughout.  CELL A =
(0.4, f=1e-4, m=200, key 50); CELL B = (0.4, f=1e-3, m=2000, key 51);
CELL C = (0.4, f=1e-2, m=20000, key 52) as ladder endpoint.  The
response currency is DEV = |C - C_Z0| with signed dC = C - C_Z0 also
reported (r187 cross-finding: the R-ratio is band-noisy near the
10-bar; C-based DEV is the load-bearing metric -- disclosed A0(ii):
stratification cells get NO own null bands, DEV needs none).

W1 REPLICATION (same seeds, same recipe, same arithmetic order
osc_base - inc(on) + inc(off)): W5-DIRECT anchor, Z0 synthesis and
cells A/B/C must reproduce the r187 record numbers.  The r187 logs
retain prints at 0.1/0.01 resolution, so the frozen replication bars
are the print-rounding bars: |C - C_rec| <= 0.05 for table prints
(115.7, 116.8, 105.2), <= 0.005 for 2-dec prints (C_W5 = C_Z0 =
131.04, band 12.60, R 10.40; R_A 7.65, R_B 8.12, R_C 8.77).
Bit-exactness proper is enforced by THIS round's own record run +
deterministic re-run with timing-normalized empty diff (disclosed
A0(iii)).  WIGGLE W_rec = DEV_A - DEV_B gated in [1.00, 1.30]
(record print 15.3 - 14.2, task-briefed full precision 1.14).

W2 STRATIFICATION (all selections predefined; indices ascending
before evaluation -- chunk-order determinism, A0(iv)):
  BANDS (deterministic ordinate windows, leverage profile):
    A-bands: 10 disjoint windows of 200 zeros [200j, 200(j+1)),
    j = 0..9, covering exactly CELL B's pool (band 0 == CELL A).
    B-bands: 10 disjoint windows of 2000 zeros [2000j, 2000(j+1)),
    j = 0..9, covering exactly CELL C's pool (band 0 == CELL B).
  RANDOM (the noise model; matched pools):
    R200-2K:  10 seeds, 200 zeros from the lowest 2000 without
              replacement, rng([2600, s]) -- CELL A's dose from
              CELL B's pool (the within-pair test).
    R200-20K: 10 seeds, 200 from the lowest 20000, rng([2650, s]).
    R2K-20K:  10 seeds, 2000 from the lowest 20000, rng([2700, s])
              -- matched-pool dose comparison at randomized
              selection (EXPECT-MONO below).
  PER-ZERO LEVERAGE LADDER: each of the lowest 10 zeros moved ALONE
  at delta* (m = 1); plus the 10-set moved together; nonadditivity
  = dC(set) - sum dC_i reported.
  M-LADDER (fine dose curve, lowest-m rule): m in (10, 50, 100,
  200, 500, 1000, 2000, 5000, 20000); the m = 200/2000/20000 cells
  double as the W1 replication cells.
FROZEN STATISTICS: SPREAD_X = max - min of DEV over the 10 seeds of
random family X; SPREAD = max(SPREAD_R200_2K, SPREAD_R200_20K,
SPREAD_R2K_20K).  EXPECT-MONO holds iff median DEV(R2K-20K) >=
median DEV(R200-20K) (dose-monotonicity in expectation at matched
pool, zero slack).  INV-FRAC = fraction of R200-2K seeds with DEV >
DEV_B (how generically a 200-sub-selection of B's pool inverts).

W3 DEPTH PARITY (predefined pair, no third depth): record depth 2e6
vs the r187 measured checkpoint depth 1e6.  The MOVED sets stay
FIXED (the lowest 200/2000 of the record depth) and only the
unmoved base synthesis is truncated (isolates the truncation tail;
recipe-rescaled m would conflate selection with depth -- disclosed
A0(v)).  W_alt = DEV_A - DEV_B at depth 1e6 with the depth-matched
C_Z0(1e6).  ARTIFACT RULE (frozen): sign(W_alt) != sign(W_rec) OR
|W_alt - W_rec| > 0.5 * |W_rec|.  Sanity: |C_Z0(1e6) - C_Z0(2e6)|
<= 0.01 (the r187 tail law measured |dC| = 0.0011).

W4 VERDICT (frozen precedence, evaluated in this order):
  1. ZB-DEPTH-ARTIFACT   iff the W3 artifact rule fires.
  2. ZB-WIGGLE-NOISE     iff W_rec <= SPREAD and EXPECT-MONO holds
                         (the wiggle sits inside the which-zeros
                         selection variability at matched dose and
                         the dose response is monotone in
                         expectation).
  3. ZB-INTERFERENCE-REAL otherwise (the specific lowest-ordinate
                         selection inverts the ordering beyond
                         selection noise, or expectation-
                         monotonicity itself fails -- then
                         additionally ZB-NONMONOTONE-IN-EXPECTATION
                         if median DEV(R2K-20K) < median
                         DEV(R200-20K)).
  Reported tokens either way: ZB-LEVERAGE-GRADIENT iff the A-band
  DEVs are strictly decreasing from band 0 to band 9 (the 1/gamma
  leverage shape); INV-FRAC; the per-zero ladder.
UPGRADE ADJUDICATION (frozen): verdict 1 or 2 => the r187 dose
surface is monotone modulo the quantified artifact/noise --
UPGRADE-BY-REFERENCE token ZERO-CAUSALITY-DEMONSTRATED-WITH-
STRATIFICATION (r187's own record stays PARTIAL, unedited; this
round's record supersedes by reference).  Verdict 3 => NO upgrade;
the interference is named as a new mechanistic fact (which zeros
move matters, not only how many -- EXACT-ORDINATES-REQUIRED
class).

FROZEN PREDICTIONS (before any evaluation; expectations only, the
rules above adjudicate): P-W1 exact replication (deterministic
engine).  P-W2 per-zero leverage falls ~1/gamma => A-bands
decreasing; selection spreads at m = 200 expected of order >= 1 (the
wiggle scale) => prior expectation NOISE; not enforced.  P-W3 the
r187 tail law (|dC| ~ 1e-3) predicts |W_alt - W_rec| << 0.5 W_rec =>
NOT artifact.  LOOP GUARD (machine-checked, r187 convention): the
verified cache as DATA for controlled selections is control-
construction (Epstein class); ZERO-VERIF-AS-HYP and RH-GRANT are
ancestors of NOTHING delivered.  AST firewall on THIS file: no
zero-oracle names, no zeta use, np.load nowhere (wards delegated to
the imported frozen engine), no verification/ import.

Bars: runtime <= 1800 s; gates numbered G01..G23; smoke mode
(--smoke) is structural only (reduced depth 2e5/1e5, nnull 5, 3
seeds per random family, 3 bands, ladder (10, 200, 2000), leverage
3 zeros; record-replication gates SMOKE-scoped to finiteness).
AMENDMENT BLOCK (disclosed at freeze): A0 (i) S2-only round; (ii)
DEV-only readout for stratification cells (no own null bands);
(iii) record bars = r187 print-rounding bars, bit-exactness via
this round's own re-run diff; (iv) selections sorted ascending;
(v) depth parity keeps moved sets fixed; (vi) the random-family
seed roots 2600/2650/2700 continue the r187 seed registry and are
exhaustive -- no reruns.  A1: none at freeze (no record run
existed; smoke1/smoke2 structural logs kept).
"""

# =====================================================================
# CORRECTION OF RECORD (Bughunt IX, note DXV, 2026-08-21)
# ---------------------------------------------------------------------
# Appended OUTSIDE the frozen spec text per the r131/r165
# corrections-of-record convention: the module docstring above is the
# historical record and is NOT edited; SPEC_SHA (= sha256 of the
# docstring) stays 8639b3a78503a0f9.  NO numeric change, NO verdict
# flip, NO RH CLAIM.
#
# BH9-F2 [MINOR, the "1.14" wiggle-figure provenance]: this spec's
#   label "task-briefed full precision 1.14" mislabels an UNSOURCED
#   brief figure -- 1.14 is derivable from NO record surface (the
#   r187 record log prints the two ZB cells at 1 decimal, 15.3/14.2,
#   difference 1.1, and its G24 FAIL line carries no numeric drop);
#   the correct full-precision value is W_rec = 15.300999 - 14.235535
#   = 1.065464 (reads 1.07; this round's own record, twice
#   replicated).  Note DXI's explanation of the 1.14 as "die
#   Differenz der 1-Dezimal-Prints" is arithmetically false (that
#   difference is 1.1).  The violation itself is REAL (1.0655 >
#   slack 1.0 -- by only 0.0655), the frozen window [1.00, 1.30]
#   holds for the true value, and r187's PARTIAL verdict stands: NO
#   verdict moves.
# =====================================================================

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import statistics
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import zero_causal_synth_probe as ZS          # the frozen r187 engine

# ---------------------------------------------------------------- frozen
R187_SPEC16 = "c20e87eec6d158b9"
DELTA_STAR = 0.4
BETA_STAR = 0.5 + DELTA_STAR
N_D2 = 2_000_000
N_ALT = 1_000_000
M_A, M_B, M_C = 200, 2000, 20000
KEY_A, KEY_B, KEY_C = 50, 51, 52
NNULL = 20
NBAND = 10
NRAND = 10
SEED_R200_2K = 2600
SEED_R200_20K = 2650
SEED_R2K_20K = 2700
LEV_N = 10
M_LADDER = (10, 50, 100, 200, 500, 1000, 2000, 5000, 20000)
REC = dict(C_W5=131.04, BAND_W5=12.60, R_W5=10.40,
           C_Z0=131.04, R_Z0=10.40,
           C_A=115.7, R_A=7.65,
           C_B=116.8, R_B=8.12,
           C_C=105.2, R_C=8.77)
TOL_2DEC = 0.005
TOL_1DEC = 0.05
WIG_LO, WIG_HI = 1.00, 1.30
DEPTH_FRAC = 0.5
Z0_DEPTH_TOL = 0.01
RUNTIME_BAR = 1800.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load in this file @%d (wards are "
                       "delegated to the imported engine)"
                       % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; NO zeta; np.load NOWHERE in "
                       "this file (wards delegated to the frozen "
                       "engine); no verification/ import")


# ------------------------------------------------------------- helpers
def cell_weights(gs_sel: np.ndarray, osc_base_: np.ndarray,
                 qs: np.ndarray, us_ep: np.ndarray,
                 na: int) -> np.ndarray:
    """the r187 ZB cell recipe VERBATIM: osc_base - inc(on-line)
    + inc(off-line at beta*), then synth_weights."""
    F_on = ZS.osc_dens(gs_sel, us_ep)
    F_off = ZS.osc_dens(gs_sel, us_ep, beta=BETA_STAR)
    osc = (osc_base_
           - ZS.weights_from_dens(qs, F_on[:na], F_on[na:])
           + ZS.weights_from_dens(qs, F_off[:na], F_off[na:],
                                  beta=BETA_STAR))
    return ZS.synth_weights(qs, osc)


# ============================================================== main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    args = ap.parse_args()
    smoke = args.smoke
    full = not smoke

    print("=" * 78)
    print("zb_wiggle_strat_probe -- PRIME.ZB.WIGGLE.STRAT.01  "
          "(EXPLORATORY MECHANISM follow-up)")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16], "  [SMOKE]" if smoke else ""))
    print("=" * 78)

    n_d2 = 200_000 if smoke else N_D2
    n_alt = 100_000 if smoke else N_ALT
    nnull = 5 if smoke else NNULL
    nband = 3 if smoke else NBAND
    nrand = 3 if smoke else NRAND
    lev_n = 3 if smoke else LEV_N
    m_ladder = (10, 200, 2000) if smoke else M_LADDER

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + ENGINE IDENTITY + WARDS")
    ok_fw, det = firewall_audit()
    check("G01-firewall-ast", ok_fw, det)
    check("G02-spec-seal", len(__doc__) > 4000,
          "SPEC_SHA %s (sha256 of __doc__)" % SPEC_SHA[:16])
    check("G03-engine-identity", ZS.SPEC_SHA[:16] == R187_SPEC16,
          "imported zero_causal_synth_probe SPEC %s == r187 record %s "
          "(engine reused verbatim, no reconstruction)"
          % (ZS.SPEC_SHA[:16], R187_SPEC16))
    gam7 = ZS.ward_cache7()
    gbig = ZS.ward_cache_big()
    mono7 = bool(np.all(np.diff(gam7) > 0))
    ovl = float(np.max(np.abs(gbig[:len(gam7)] - gam7)))
    okb = (len(gam7) == 7000 and len(gbig) == 20_000_000 and mono7
           and gam7[0] > 14.13 and ovl <= 1e-8)
    check("G04-ward-caches", okb,
          "n7000: %d (gamma_1 %.6f); big: %d (top %.4f); monotone %s; "
          "overlap %.2e <= 1e-8 (delegated wards, PT21 pedigree)"
          % (len(gam7), gam7[0], len(gbig), float(gbig[-1]), mono7,
             ovl))

    qs, us_atoms, w_true = ZS.spike_positions()
    us_ep = np.concatenate([np.log(qs - 0.5), np.log(qs + 0.5)])
    na = len(qs)
    ugrid = ZS.SPIKE_LO + (np.arange(1, ZS.SPIKE_GRID_N + 1)
                           * (ZS.SPIKE_HI - ZS.SPIKE_LO)
                           / (ZS.SPIKE_GRID_N + 1))
    zgrid = ZS.landau_field(gam7, ugrid)
    z_ms = float(np.mean(zgrid ** 2))
    info("spike support %d atoms; Landau grid rms %.2f"
         % (na, math.sqrt(z_ms)))

    # ------------------------------------------------------------ S1
    section("S1  W1 REPLICATION -- anchors + the two offending cells")
    w5 = ZS.d2_eval_syn(gam7, us_atoms, w_true, z_ms, nnull,
                        ZS.FAM_CODE["Z0"], 0, intrand=True)
    ok5 = (abs(w5["C"] - REC["C_W5"]) <= TOL_2DEC
           and abs(w5["nullmax"] - REC["BAND_W5"]) <= TOL_2DEC
           and abs(w5["R"] - REC["R_W5"]) <= TOL_2DEC) if full \
        else np.isfinite(w5["C"])
    check("G05-w5-direct-rep", ok5,
          "W5-DIRECT: C = %.6f (rec 131.04), band %.6f (rec 12.60), "
          "R = %.6f (rec 10.40)%s"
          % (w5["C"], w5["nullmax"], w5["R"],
             "" if full else " [SMOKE-scoped]"))

    t0 = time.time()
    gs_syn = gbig[:n_d2]
    F_base = ZS.osc_dens(gs_syn, us_ep)
    osc_base = ZS.weights_from_dens(qs, F_base[:na], F_base[na:])
    w_z0 = ZS.synth_weights(qs, osc_base)
    info("base pass (true ordinates, %d zeros x %d endpoints): %.0f s"
         % (n_d2, len(us_ep), time.time() - t0))
    z0 = ZS.d2_eval_syn(gam7, us_atoms, w_z0, z_ms, nnull,
                        ZS.FAM_CODE["Z0"], 0, intrand=True)
    C_Z0 = z0["C"]
    ok6 = (abs(C_Z0 - REC["C_Z0"]) <= TOL_2DEC
           and abs(z0["R"] - REC["R_Z0"]) <= TOL_2DEC) if full \
        else np.isfinite(C_Z0)
    check("G06-z0-s2-rep", ok6,
          "Z0-S2: C_Z0 = %.6f (rec 131.04), R = %.6f (rec 10.40)%s"
          % (C_Z0, z0["R"], "" if full else " [SMOKE-scoped]"))

    cells = {}
    for tag, m, key, cr, rr in (("A", M_A, KEY_A, REC["C_A"],
                                 REC["R_A"]),
                                ("B", M_B, KEY_B, REC["C_B"],
                                 REC["R_B"]),
                                ("C", M_C, KEY_C, REC["C_C"],
                                 REC["R_C"])):
        wv = cell_weights(gs_syn[:m], osc_base, qs, us_ep, na)
        r = ZS.d2_eval_syn(gam7, us_atoms, wv, z_ms, nnull,
                           ZS.FAM_CODE["ZB"], key)
        cells[tag] = r
        okc = (abs(r["C"] - cr) <= TOL_1DEC
               and abs(r["R"] - rr) <= TOL_2DEC) if full \
            else np.isfinite(r["C"])
        check("G%02d-cell-%s-rep" % (6 + "ABC".index(tag) + 1, tag),
              okc,
              "delta 0.40 f %.0e (m=%d, key %d): C = %.6f (rec %.1f), "
              "DEV = %.6f, R = %.6f (rec %.2f)%s"
              % ({"A": 1e-4, "B": 1e-3, "C": 1e-2}[tag], m, key,
                 r["C"], cr, abs(r["C"] - C_Z0), r["R"], rr,
                 "" if full else " [SMOKE-scoped]"))
    DEV_A = abs(cells["A"]["C"] - C_Z0)
    DEV_B = abs(cells["B"]["C"] - C_Z0)
    W_rec = DEV_A - DEV_B
    ok10 = (WIG_LO <= W_rec <= WIG_HI) if full else np.isfinite(W_rec)
    check("G10-wiggle-rep", ok10,
          "W_rec = DEV_A - DEV_B = %.6f - %.6f = %.6f (frozen window "
          "[%.2f, %.2f]; record print 15.3 - 14.2, briefed 1.14)%s"
          % (DEV_A, DEV_B, W_rec, WIG_LO, WIG_HI,
             "" if full else " [SMOKE-scoped]"))

    # ------------------------------------------------------------ S2
    section("S2  W2 STRATIFICATION -- bands, random families, "
            "per-zero leverage, m-ladder")

    def dev_of(gs_sel: np.ndarray) -> float:
        wv = cell_weights(gs_sel, osc_base, qs, us_ep, na)
        return float(ZS.coherence(gam7, us_atoms, wv, z_ms))

    # deterministic ordinate bands (leverage profile)
    band_rows = {"A": [], "B": []}
    for tag, m in (("A", M_A), ("B", M_B)):
        for j in range(nband):
            sel = gs_syn[j * m: (j + 1) * m]
            Cj = dev_of(sel)
            band_rows[tag].append((j, float(sel[0]), float(sel[-1]),
                                   Cj, Cj - C_Z0, abs(Cj - C_Z0)))
    print("\n  BANDS-A (m=200 windows of CELL B's pool; band 0 == "
          "CELL A)")
    print("  %-4s %-20s %10s %10s %8s" % ("j", "gamma range", "C",
                                          "dC", "DEV"))
    for j, g0, g1, Cj, dc, dv in band_rows["A"]:
        print("  %-4d [%8.2f, %8.2f] %10.4f %+10.4f %8.4f"
              % (j, g0, g1, Cj, dc, dv))
    devsA = [r[5] for r in band_rows["A"]]
    lev_grad = all(devsA[i + 1] < devsA[i]
                   for i in range(len(devsA) - 1))
    check("G11-bands-A", True,
          "DEFINITIONAL: %d disjoint 200-bands; DEV band0 %.4f -> "
          "band%d %.4f; strictly decreasing (ZB-LEVERAGE-GRADIENT): "
          "%s" % (nband, devsA[0], nband - 1, devsA[-1], lev_grad))
    print("\n  BANDS-B (m=2000 windows of CELL C's pool; band 0 == "
          "CELL B)")
    print("  %-4s %-20s %10s %10s %8s" % ("j", "gamma range", "C",
                                          "dC", "DEV"))
    for j, g0, g1, Cj, dc, dv in band_rows["B"]:
        print("  %-4d [%8.2f, %8.2f] %10.4f %+10.4f %8.4f"
              % (j, g0, g1, Cj, dc, dv))
    devsB = [r[5] for r in band_rows["B"]]
    check("G12-bands-B", True,
          "DEFINITIONAL: %d disjoint 2000-bands; DEV band0 %.4f -> "
          "band%d %.4f; strictly decreasing: %s"
          % (nband, devsB[0], nband - 1, devsB[-1],
             all(devsB[i + 1] < devsB[i]
                 for i in range(len(devsB) - 1))))

    # random families (the noise model)
    def rand_family(root: int, m: int, pool: int) -> list:
        out = []
        for s in range(nrand):
            rng = np.random.default_rng([root, s])
            idx = np.sort(rng.choice(pool, size=m, replace=False))
            Cs = dev_of(gs_syn[idx])
            out.append((s, Cs, abs(Cs - C_Z0)))
        return out

    fam = {}
    pool_b = min(M_B, n_d2)
    pool_c = min(M_C, n_d2)
    fam["R200-2K"] = rand_family(SEED_R200_2K, M_A, pool_b)
    fam["R200-20K"] = rand_family(SEED_R200_20K, M_A, pool_c)
    fam["R2K-20K"] = rand_family(SEED_R2K_20K, M_B, pool_c)
    print("")
    spreads = {}
    meds = {}
    for nm in ("R200-2K", "R200-20K", "R2K-20K"):
        dvs = [r[2] for r in fam[nm]]
        spreads[nm] = max(dvs) - min(dvs)
        meds[nm] = statistics.median(dvs)
        print("  %-9s DEV: %s | med %.4f spread %.4f"
              % (nm, " ".join("%.3f" % d for d in dvs), meds[nm],
                 spreads[nm]))
    SPREAD = max(spreads.values())
    check("G13-rand-spreads", True,
          "DEFINITIONAL: SPREAD = max(%.4f, %.4f, %.4f) = %.4f vs "
          "W_rec = %.4f -- wiggle %s the matched-dose selection "
          "spread"
          % (spreads["R200-2K"], spreads["R200-20K"],
             spreads["R2K-20K"], SPREAD, W_rec,
             "INSIDE" if W_rec <= SPREAD else "OUTSIDE"))
    expect_mono = meds["R2K-20K"] >= meds["R200-20K"]
    check("G14-expect-mono", True,
          "DEFINITIONAL: median DEV at randomized selection, matched "
          "pool (lowest %d): m=2000 %.4f vs m=200 %.4f -> dose "
          "monotone in expectation: %s"
          % (pool_c, meds["R2K-20K"], meds["R200-20K"], expect_mono))
    inv_frac = sum(1 for r in fam["R200-2K"] if r[2] > DEV_B) \
        / float(len(fam["R200-2K"]))
    check("G15-inversion-fraction", True,
          "DEFINITIONAL: INV-FRAC = %.2f (fraction of random "
          "200-subsets of CELL B's pool with DEV > DEV_B = %.4f; "
          "the r187 deterministic lowest-200 subset inverts with "
          "DEV_A = %.4f)" % (inv_frac, DEV_B, DEV_A))

    # per-zero leverage ladder
    print("\n  PER-ZERO LEVERAGE (each zero alone at delta 0.40)")
    print("  %-4s %10s %12s %12s" % ("i", "gamma", "C", "dC"))
    dcs = []
    for i in range(lev_n):
        Ci = dev_of(gs_syn[i: i + 1])
        dcs.append(Ci - C_Z0)
        print("  %-4d %10.4f %12.4f %+12.6f"
              % (i + 1, float(gs_syn[i]), Ci, Ci - C_Z0))
    C_set = dev_of(gs_syn[:lev_n])
    dc_set = C_set - C_Z0
    nonadd = dc_set - sum(dcs)
    check("G16-leverage-ladder", True,
          "DEFINITIONAL: lowest-%d single-zero dC in [%+.4f, %+.4f]; "
          "set-of-%d dC = %+.4f vs sum of singles %+.4f -> "
          "nonadditivity %+.4f"
          % (lev_n, min(dcs), max(dcs), lev_n, dc_set, sum(dcs),
             nonadd))

    # fine m-ladder (lowest-m rule)
    print("\n  M-LADDER (lowest-m moved at delta 0.40)")
    print("  %-8s %12s %12s %8s" % ("m", "C", "dC", "DEV"))
    lad = []
    for m in m_ladder:
        mm = min(m, n_d2)
        Cm = dev_of(gs_syn[:mm])
        lad.append((mm, Cm, abs(Cm - C_Z0)))
        print("  %-8d %12.4f %+12.4f %8.4f"
              % (mm, Cm, Cm - C_Z0, abs(Cm - C_Z0)))
    lad_mono_bad = [(lad[i][0], lad[i + 1][0])
                    for i in range(len(lad) - 1)
                    if lad[i + 1][2] < lad[i][2]]
    check("G17-m-ladder", True,
          "DEFINITIONAL: DEV(m) over %s; non-monotone steps: %s"
          % (str([r[0] for r in lad]),
             str(lad_mono_bad) if lad_mono_bad else "NONE"))

    # ------------------------------------------------------------ S3
    section("S3  W3 DEPTH PARITY (base truncation %d vs %d; moved "
            "sets FIXED)" % (n_d2, n_alt))
    t0 = time.time()
    F_sub = ZS.osc_dens(gbig[n_alt: n_d2], us_ep)
    F_alt = F_base - F_sub
    osc_alt = ZS.weights_from_dens(qs, F_alt[:na], F_alt[na:])
    w_z0_alt = ZS.synth_weights(qs, osc_alt)
    C_Z0_alt = float(ZS.coherence(gam7, us_atoms, w_z0_alt, z_ms))
    info("alt-depth pass: %.0f s" % (time.time() - t0))
    C_A_alt = float(ZS.coherence(
        gam7, us_atoms,
        cell_weights(gs_syn[:M_A], osc_alt, qs, us_ep, na), z_ms))
    C_B_alt = float(ZS.coherence(
        gam7, us_atoms,
        cell_weights(gs_syn[:M_B], osc_alt, qs, us_ep, na), z_ms))
    W_alt = abs(C_A_alt - C_Z0_alt) - abs(C_B_alt - C_Z0_alt)
    ok18 = abs(C_Z0_alt - C_Z0) <= Z0_DEPTH_TOL
    check("G18-depth-z0-sanity", ok18,
          "|C_Z0(depth %d) - C_Z0(depth %d)| = %.6f <= %.2f (r187 "
          "tail law measured 0.0011)"
          % (n_alt, n_d2, abs(C_Z0_alt - C_Z0), Z0_DEPTH_TOL))
    artifact = (np.sign(W_alt) != np.sign(W_rec)
                or abs(W_alt - W_rec) > DEPTH_FRAC * abs(W_rec))
    check("G19-depth-parity", True,
          "DEFINITIONAL: W(depth %d) = %.6f vs W_rec(depth %d) = "
          "%.6f; |dW| = %.6f vs %.2f*|W_rec| = %.6f; sign flip %s -> "
          "artifact rule %s"
          % (n_alt, W_alt, n_d2, W_rec, abs(W_alt - W_rec),
             DEPTH_FRAC, DEPTH_FRAC * abs(W_rec),
             np.sign(W_alt) != np.sign(W_rec),
             "FIRES" if artifact else "does NOT fire"))

    # ------------------------------------------------------------ S4
    section("S4  W4 LOOP GUARD + VERDICT + UPGRADE ADJUDICATION")
    dep = {"STRAT-VERDICT": ("R187-ENGINE", "CONTROLLED-SELECTIONS"),
           "R187-ENGINE": ("EXPLICIT-FORMULA-FORM", "CENSUS-AS-DATA",
                           "CACHE-WARD", "DETECTOR-PORTS"),
           "CONTROLLED-SELECTIONS": ("CENSUS-AS-DATA",),
           "EXPLICIT-FORMULA-FORM": (), "CENSUS-AS-DATA": (),
           "CACHE-WARD": (), "DETECTOR-PORTS": (),
           "ZERO-VERIF-AS-HYP": (), "RH-GRANT": (),
           "POSITIVITY-FROM-CENSUS": ("ZERO-VERIF-AS-HYP",
                                      "RH-GRANT")}

    def ancestors(node):
        seen = set()
        stack = [node]
        while stack:
            nn = stack.pop()
            for p in dep.get(nn, ()):
                if p not in seen:
                    seen.add(p)
                    stack.append(p)
        return seen

    banned = {"ZERO-VERIF-AS-HYP", "RH-GRANT"}
    ok20 = not (ancestors("STRAT-VERDICT") & banned)
    check("G20-loop-guard", ok20,
          "delivered ancestors clean: CENSUS-AS-DATA (control "
          "construction, Epstein class) is NOT ZERO-VERIF-AS-HYP; "
          "no positivity argument consumed anywhere")

    if artifact:
        verdict = "ZB-DEPTH-ARTIFACT"
    elif W_rec <= SPREAD and expect_mono:
        verdict = "ZB-WIGGLE-NOISE"
    else:
        verdict = "ZB-INTERFERENCE-REAL"
    extra = []
    if not expect_mono:
        extra.append("ZB-NONMONOTONE-IN-EXPECTATION")
    if lev_grad:
        extra.append("ZB-LEVERAGE-GRADIENT")
    check("G21-verdict", True,
          "DEFINITIONAL (frozen precedence artifact > noise > "
          "interference): %s (W_rec %.4f vs SPREAD %.4f; EXPECT-MONO "
          "%s; artifact %s)%s"
          % (verdict, W_rec, SPREAD, expect_mono, artifact,
             ("; extra: " + "+".join(extra)) if extra else ""))
    if verdict in ("ZB-WIGGLE-NOISE", "ZB-DEPTH-ARTIFACT"):
        upgrade = ("UPGRADE-BY-REFERENCE: ZERO-CAUSALITY-"
                   "DEMONSTRATED-WITH-STRATIFICATION (the r187 dose "
                   "surface is monotone modulo the quantified %s; "
                   "the r187 record itself stays PARTIAL, unedited)"
                   % ("selection noise" if verdict == "ZB-WIGGLE-NOISE"
                      else "depth artifact"))
    else:
        upgrade = ("NO UPGRADE: the inversion is ordinate-specific "
                   "beyond selection noise -- which zeros move "
                   "matters, not only how many (EXACT-ORDINATES-"
                   "REQUIRED class); r187 stays PARTIAL")
    check("G22-upgrade-adjudication", True,
          "DEFINITIONAL: " + upgrade)

    rt = time.time() - T0_WALL
    check("G23-runtime", rt <= RUNTIME_BAR,
          "runtime %.1f s <= %.0f s" % (rt, RUNTIME_BAR))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    ntot = len(CHECKS)
    tokens = [verdict] + extra
    tokens.append("INV-FRAC(%.2f)" % inv_frac)
    tokens.append("W-REC(%.4f)" % W_rec)
    tokens.append("SPREAD(%.4f)" % SPREAD)
    tokens += ["NO-RH-CLAIM", "NO-NUMEROLOGY-CLAIM"]
    print("\n" + "=" * 78)
    print("GATES: %d/%d PASS" % (npass, ntot))
    print("COMPOSITE VERDICT: " + " + ".join(tokens))
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("RUNTIME %.1f s" % rt)
    print("=" * 78)
    hard_fails = [nm for nm, ok, _d in CHECKS if not ok]
    return 0 if not hard_fails else 1


if __name__ == "__main__":
    sys.exit(main())
