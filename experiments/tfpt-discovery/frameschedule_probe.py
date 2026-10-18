#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""frameschedule_probe -- PRIME.CCM.FRAMESCHEDULE.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION
=======================================================================
Round 126 (selection_probe, verdict SELECTION-SECTOR-ONLY) left two
open levers on the CCM selection omega:
 (L1) THE FRAME SCHEDULE: the S_K selector floor is EXACTLY the
      round-122 mixing number beta = <v_1, k_lambda>; on the KFAC
      ladder beta falls and FLIPS SIGN (round 124: x=5
      +1.85e-3 -> -8.9e-4, x=8 +3.57e-3 -> -2.45e-4, x=13 +2.52e-3 ->
      -5.86e-5), and the matched enriched frame (KFAC 2.0) floor obeys
      |beta| ~ x^(-2.8).  At the sign flip the selector is (nearly)
      EXACT.  Is the flip STABLE, PREDICTABLE FROM SOURCE at
      polynomial cost, and what does the certified approximant at the
      flip frame buy?
 (L2) THE COMMUTATOR HUNT: the exact trade-off identity
      (E0-E1) s01 = <v0, [Q, S] v1> makes sub-beta selection a search
      for a source operator S whose commutator doublet element is
      Connes-small while its split is not.  For ANY linear family
      {S(theta) = sum_i theta_i B_i} the kernel {s01(theta) = 0} has
      codim <= 1 (exactly 1 iff c != 0, c_i = s01(B_i)); the content
      is whether the kernel DIRECTION is source-predictable (frozen
      from shallow rungs, transferred out-of-sample to deep rungs) or
      whether its localization is itself the Connes-priced doublet
      datum (the round-126 block-pencil finding, now over a 12-member
      source-operator basis).

STRUCTURAL FACTS DRIVING THE DESIGN (new in this spec, gated):
 (i)  THE FRAME DIAL IS INTEGER.  R4.build_cell uses kfac only via
      K = ceil(kfac * x * log x); the cell depends on (x, world, dps,
      K) alone.  The "crossing KFAC_c" is therefore a SIGN FLIP
      between adjacent integers K, the schedule is a ladder in K, and
      the best achievable crossing floor is set by the per-step
      increment Delta-beta, NOT zero.  Gated exactly (G13: two kfacs
      with the same ceil produce bit-identical f64 matrices).
 (ii) SIGN-CHAIN COHERENCE.  beta's sign convention (v1 largest-
      |entry| positive, per round 122/124) is per-cell; at adjacent-K
      granularity a convention jump could fake or hide a flip.  The
      cos basis at K is a PREFIX of the basis at K+1 (a = log(x)/2 is
      K-independent), so v1 vectors chain exactly by zero-padded
      overlaps.  The probe reports beta in BOTH conventions and
      adjudicates the flip on the CHAIN-COHERENT sign; chain overlap
      |<v1(K), v1(K')>| >= 0.90 required at the gate rungs (hard),
      reported at depth.  This also adjudicates whether the round-124
      sign flip is real or a convention artifact.
 (iii) CROSSING-PROXIMITY DECOMPOSITION.  With the integer crossing
      K*(x) and the step size measured, the matched-frame floor
      decomposes as |beta(K_2.0)| ~= slope * |K_2.0 - K*|; the probe
      measures whether the x^(-2.8) law is a genuine depth law or a
      crossing-proximity artifact.

=======================================================================
LADDERS AND FROZEN NUMERICS
=======================================================================
MAIN even cells (round-122 builder R4.build_cell verbatim, want_mp).
K-grids (kfac = (K - 0.5)/(x log x), so ceil == K exactly):
  x=5  (dps 60):  K = 11, 12, 13, 17, 20, 23
  x=8  (dps 80):  K = 21, 27, 30, 34, 40, 47
  x=13 (dps 120): K = 42, 54, 61, 67, 81
  x=18 (dps 160 at the pin K=66; dps 120 at enriched K = 105, 125 and
        bisection cells -- gap(18) = 1.7e-71 leaves >= 49 digits of
        headroom at dps 120; the crossing cell K_lo is REBUILT at dps
        160 and |beta| compared, bar 1e-9 abs = the dps-downshift ward)
  x=24 (dps 150): K = 153 (matched KFAC 2.0) + K_pred(24) (predictor
        single-shot).  gap(24) extrapolates to ~1e-99 (log10 gap ~=
        -4.649 x + 12.9 from the round-124 pins), headroom ~50 digits;
        eigen-residual gate binds honestly if the extrapolation fails.
INTEGER BISECTION of the sign flip (chain-coherent sign), budgets of
extra builds: x=5: 6, x=8: 6, x=13: 6, x=18: 5, x=24: 0.  At x = 13
and 18 the FIRST bisection probe is the predictor value K_pred(x)
(clamped into the open bracket) -- predictor-guided search; the
recorded prediction precedes its build (out-of-sample discipline).
Saturation pairs (|beta| change across the two deepest grid points):
x=5: (20,23), x=8: (40,47), x=13: (67,81), x=18: (105,125); x=24
saturation UNMEASURED (budget decision, disclosed).  x=32 DECLINED:
measured cost law (below) prices one K(2.0)=222 build at dps>=280
beyond 4 h; stated, not attempted.
Worlds (enriched frame, want_mp): SMOOTH / SCRARITH / EPSTEIN x=8
K=34 dps 80; EPSTEIN x=13 K=67 dps 120.
Candidate k_lambda via R4.prolate_kvec (NGRID 20001) bit-for-bit;
rung anatomy via CM.rung_core (round-124 machinery verbatim).
SOFT_BAR = 1e-2.  All mp under explicit mp.workdps at the cell dps
(round-118/120 unary-negation lesson); templates are frozen f64 unit
vectors.  Deterministic: no RNG anywhere.  Sign conventions: v0 by
<v0,k> > 0 (alpha > 0); v1 raw = largest-|entry| positive (round-124
regression currency), v1 chain-coherent = zero-pad-overlap chained
from the smallest built K per rung (crossing currency).

ROUND-124 REGRESSION PINS (run2 log = run of record; RAW convention):
  1.25 cells (K = 11/21/42/66): eps, gap, beta, nsoft as in round-126
  spec (SP.R124_* reused; bar 2e-2 rel on beta, 1e-4 on gap, exact
  nsoft).  KFAC-ladder rows: beta(5,K13) = -2.316e-4, beta(5,K17) =
  -8.456e-4, beta(5,K20) = -8.905e-4, beta(8,K27) = +5.218e-4,
  beta(8,K34) = -2.177e-4, beta(8,K40) = -2.451e-4, beta(13,K67) =
  -5.864e-5 (bar 2e-2 rel); anndim rows (ward count) exact:
  (5,K11)=4, (5,K13)=3, (5,K17)=2, (5,K20)=0, (8,K21)=7, (8,K27)=6,
  (8,K34)=4, (8,K40)=2, (13,K42)=12, (13,K67)=7.

PRE-FREEZE TIMING SMOKE (disclosed): builds x=8 K=34 at dps
80/160/220 = 38.5/163.0/510.0 s and x=13 K=42 at dps 220 = 773.5 s
=> cost law t ~= C * K^2.0 * dps^2.55 (dps exponent 2.1-2.6 across
the pairs); this smoke fixed the dps-downshift decisions and the
x=24/x=32 budget above.  No beta/verdict data was read in the smoke.

=======================================================================
T1  THE COUPLED SCHEDULE (per x: grid + bisection + reads)
=======================================================================
Per cell: beta (raw + chain-coherent), alpha, nsoft, anndim (ward
count AND the source-side Riemann-von-Mangoldt main term N_rvm(T) =
T/(2pi) log(T/(2pi e)) + 7/8 -- NO zero data), gap, eps,
eigen-residual (bar 10^-(dps/2)), two-vector residual, build time.
Crossing record per x: bracket (K_lo, K_lo+1), interpolated K*, the
crossing floor betac* = min(|beta(K_lo)|, |beta(K_lo+1)|), step
Delta = |beta(K_lo+1) - beta(K_lo)|.  Laws: (a) matched-2.0 floor
|beta(K_2.0(x))| vs x (OLS slope; CONTINUES iff slope in -2.8 +- 0.7
over x = 5..24); (b) crossing-floor betac* law; (c) step law
Delta(x); (d) proximity decomposition |beta(K_2.0)| vs
Delta * |K_2.0 - K*|; (e) cost law (fit exponents, measured).

PREDICTORS (frozen rules; source-only inputs: measured shallow
crossings + RvM/arch arithmetic; NO deep doublet data enters a
prediction before its out-of-sample build):
  P-FIT: gamma(x) = K*(x)/(x log x); log gamma linear in log x.
    Stage 1 fit on x = (5, 8) -> K_pred(13); stage 2 on (5, 8, 13) ->
    K_pred(18); stage 3 on (5, 8, 13, 18) -> K_pred(24).
  P-RVM: A(x, K) = K - N_rvm(K pi / a); a* = mean of A(x, K*(x)) over
    the fitted rungs (same stages); K_pred = integer K minimizing
    |A(x, K) - a*|.  Adjudication (typed): distance |K_pred -
    round(K*)| at x = 13, 18 for both; headline predictor = P-FIT.
  PREDICTABLE bar: |beta(K_pred(x))| <= |beta(K_2.0(x))| at x = 13
  AND x = 18 (the predicted frame beats the matched enriched floor)
  => CROSSING-SOURCE-PREDICTABLE, else CROSSING-CONNES-PINNED.
  x=24 single-shot: build K_pred(24) only; typed SINGLE-SHOT (no flip
  verification affordable).

T1c APPROXIMANT: at the best crossing cell (13, 18): xi-hat = f64
pipeline S_K selection (f64 eigh cluster basis, rank-1 compression =
normalized cluster projection of k-hat, frozen MAX branch); reads:
ov(xi-hat, v0_mp) (bar >= 1 - 1e-4, round-126 F64_SK_BAR), error
angle vs the 1.25-frame beta and the matched floor, mp Rayleigh
R(xi-hat) vs eps (upper bound ONLY -- the RH datum is the SIGN of
eps_lambda, which no vector approximant certifies; typed
OMEGA-ABSORBED unless a sign-certifying read exists, which none
does), Z1/disguise screens at the crossing frame (in-band doublet
evaluations, above-band canonical-Gram traceless correlation,
flag 0.95).

=======================================================================
T2  THE COMMUTATOR KERNEL (12-member source basis)
=======================================================================
Basis (frozen f64 objects per rung, Frobenius-normalized; source-only:
Lambda(n)/Gamma/pi/prolate/Legendre/frame data, no zero ordinate):
  rank-1: S_K (k-hat), S_E4, S_E8 (prolate-mode Poisson lifts n=4,8),
          S_GAUSS (positive cone template), S_KLAM (Lambda-shift
          template);
  matrix: S_POS2 (v^2 multiplication, closed form), S_FREQ
          (dilation-generator-squared diag), S_ABSD (|D| diag),
          S_PRIME (arithmetic block, f64-frozen), S_TOEP / S_HANK
          (Toeplitz / Hankel diagonal-averaged compressions of the
          prime block), S_LPROF (multiplication by the Lambda-weighted
          profile g(v) = sum_q Lambda(q)/sqrt(q) cos(log q * v),
          exact closed form, warded vs 40001-grid quadrature at x=5,
          bar 1e-6 rel).
  (S_DC/S_BEV/S_EU excluded: round-126 typed UNSTABLE / edge-disguise.)
Rungs: the 1.25 cells x = 5, 8, 13, 18 (K = 11/21/42/66).  Per rung:
mp cluster compressions Sc_i (round-126 machinery verbatim), doublet
triples (s00, s01, s11)_i, kernel vector c_i = s01_i, split vector
d_i = s00_i - s11_i, Gram G_ij = <Sc_i, Sc_j>_F.
KERNEL: dim = 11 iff c != 0 (G61); in-sample max split theta* =
argmax (theta.d)^2 / theta.G.theta s.t. theta.c = 0 (closed form
theta* = B (B^T G B)^+ B^T d, B an ONB of c-perp; exact-instance
sympy gate G11); reads: max split value, split_rel and error angle of
S(theta*) on the cluster, effective rank of the compressed family
(SVD), G spectrum (conditioning).
TWO FROZEN TRANSFER CANDIDATES (both by the same freeze protocol:
mean of sign-aligned gate-rung directions iff |cos| >= 0.90, else the
x=8 direction as disclosed fallback; orientation frozen at the gate
rungs, round-126 protocol):
  (i)  theta* = the in-kernel MAX-SPLIT direction;
  (ii) theta_g = the kernel-PROJECTED S_K (e_SK minus its c-component
       = the minimal source correction to the standing selector that
       zeroes the commutator element -- the sharpest form of "can
       source operators absorb beta").
TRANSFER (out-of-sample, x = 13, 18): phi_ach, achieved cluster
overlap and split_rel with the frozen branch, for BOTH candidates.
BEATS-BETA iff phi_ach <= |beta(x)|/2 AND split_rel >= 0.05 AND
aligned (<= 0.30 rad) at BOTH deep rungs (round-126 bars; either
candidate suffices) => KERNEL-TRANSFERS (then screens: Z1, above-band
disguise corr, conditioning, worlds); else KERNEL-REVERTS with the
measured reversion law (phi_ach vs beta, drift angles of c-hat(x),
and the rank-1 ratio table r_i = s01_i/s00_i -- the annihilator-
scalar pattern test: do all v0-family templates see the doublet
through one common mixing ratio?).  The smoke exposed (disclosed):
at shallow rungs the 12-op family spans ALL of sym(cluster), so the
in-sample kernel-opt is trivially perfect (split sqrt(2) at unit
cluster-Frobenius norm) -- the deep rungs, where sym(cluster) is
66/136-dimensional and the family has 12 members, and the transfer
are the only content-bearing measurements.

=======================================================================
T4  CONTROLS / SCREENS (every internal round)
=======================================================================
Worlds: nsoft == 0 expected at SMOOTH/SCRARITH/EPSTEIN enriched cells
(no cluster => no crossing, no kernel target: the schedule is
world-typed; hard gate).  Conditioning at the x=5 crossing cell:
Connes-scale perturbation delta targeting theta ~ 1e-6, measured
dbeta vs the 2x2 law within [1/3, 3], strictly nonzero (round-118 red
flag); flip budget read delta_flip ~= |beta_c| gap / (alpha |v00
v10|) = the perturbation that moves the crossing by one step.  Tau
screens: OLS slopes of log10 (matched floor, crossing floor, phi_pred,
phi_ach(theta_f)) vs log10 gap over the shared rungs; bands |s| <=
0.30 PASS / >= 0.70 RELOCATION.  Grid certification |beta_40001 -
beta_20001| <= 5e-6 at the x=24 cells and the deep crossing cells.
Min-cut: round-116 replica + round-122 extension (flows 4/5, census
{MEAS, OMEGA-POS} cardinality 4 expected unchanged; all outcomes here
are MEAS data on the LANEACONV omega edge).

VERDICT ENUMS (frozen): FLIP-{REAL-SIGNED, CONVENTION-ARTIFACT,
NOFLIP}(per x); FLOOR-LAW-{CONTINUES, BREAKS}(slope); PROXIMITY-
{ARTIFACT, GENUINE}(decomposition ratios); CROSSING-{SOURCE-
PREDICTABLE, CONNES-PINNED}(distances, phi_pred ratios);
APPROXIMANT(err; OMEGA-ABSORBED); KERNEL-{TRANSFERS, REVERTS}(law);
composite FRAMESCHEDULE-{UPGRADE(lever), COMPOSITE-NOGO, MIXED}.

BARS (frozen; calibrated only on round-124/126 records + the
disclosed pre-freeze smokes): REG 2e-2 rel beta / 1e-4 gap / exact
nsoft+anndim; CHAIN_OV 0.90 (hard at x = 5, 8); EIGRES 10^-(dps/2);
DPS_WARD 1e-9; GRID_CERT 5e-6; F64 approximant 1 - 1e-4; COND [1/3,3];
BEATS beta/2 + split_rel 0.05 + align 0.30; DISGUISE 0.95; PREDICTABLE
phi_pred <= |beta_2.0|; FLOOR band -2.8 +- 0.7; TAU 0.30/0.70; LPROF
ward 1e-6; runtime 28800 s.

SMOKE (--smoke): x = 3 (K = 5..8) and x = 5 (K = 11, 12, 13, 17),
no deep rungs, no worlds, loosened data gates (instrument gates
hard).  NOT-VERDICT-BEARING.  Amendments after the frozen run, if
any, are appended as numbered AMENDMENT blocks.

AST FIREWALL: no zetazero/siegelz/siegeltheta/nzeros/grampoint
anywhere; no zeta anywhere in this probe; np.load absent from this
file (cache access via CM ward functions, READ-ONLY, X5); no import
of verification/.  NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4          # round-122 pipeline (verbatim)
import blockreal_lemma_probe as BR     # round-114 machinery  # noqa: F401
import cluster_mixing_probe as CM      # round-124 machinery (verbatim)
import selection_probe as SP           # round-126 machinery (verbatim)

# ---------------------------------------------------------------- frozen
GRID_K = {5: (11, 12, 13, 17, 20, 23),
          8: (21, 27, 30, 34, 40, 47),
          13: (42, 54, 61, 67, 81),
          18: (66, 105, 125),
          24: (153,)}
DPS_PIN = {3: 45, 5: 60, 8: 80, 13: 120, 18: 160, 24: 150}
DPS_ENR = {3: 45, 5: 60, 8: 80, 13: 120, 18: 120, 24: 150}
PIN_K = {5: 11, 8: 21, 13: 42, 18: 66}
MATCH20_K = {5: 17, 8: 34, 13: 67, 18: 105, 24: 153}
SAT_PAIR = {5: (20, 23), 8: (40, 47), 13: (67, 81), 18: (105, 125)}
BISECT_BUDGET = {3: 3, 5: 6, 8: 6, 13: 6, 18: 6, 24: 0}
XS_MAIN = (5, 8, 13, 18, 24)   # predictor chain order
GATE_X = (5, 8)
DEEP_X = (13, 18)
KER_X = (5, 8, 13, 18)

R124_LADDER_RAW = {(5, 13): -2.316e-4, (5, 17): -8.456e-4,
                   (5, 20): -8.905e-4, (8, 27): +5.218e-4,
                   (8, 34): -2.177e-4, (8, 40): -2.451e-4,
                   (13, 67): -5.864e-5}
R124_ANNDIM = {(5, 11): 4, (5, 13): 3, (5, 17): 2, (5, 20): 0,
               (8, 21): 7, (8, 27): 6, (8, 34): 4, (8, 40): 2,
               (13, 42): 12, (13, 67): 7}
KLADDER_BAR = 2e-2
REG_BAR = 2e-2
CHAIN_OV_BAR = 0.90
DPS_WARD_BAR = 1e-9
GRID_CERT_BAR = 5e-6
F64_BAR = 1e-4
COND_RATIO = (1.0 / 3.0, 3.0)
PERT_THETA_TGT = 1e-6
BEATS_BETA_FAC = 0.5
SPLIT_BAR = 0.05
ALIGN_BAR = 0.30
DISGUISE_CORR = 0.95
FLOOR_SLOPE, FLOOR_BAND = -2.8, 0.7
THETA_FREEZE_COS = 0.90
LPROF_WARD_BAR = 1e-6
PINV_RCOND = 1e-10
TAU_PASS, TAU_RELOC = 0.30, 0.70
ZAB_N = 40
SOFT_BAR = 1e-2
RUNTIME_BAR = 28800.0
GAMMA1_LIT = 14.134725141734693790   # ward only

KER_BASIS = ("S_K", "S_E4", "S_E8", "S_GAUSS", "S_KLAM", "S_POS2",
             "S_FREQ", "S_ABSD", "S_PRIME", "S_TOEP", "S_HANK",
             "S_LPROF")
RANK1_SET = ("S_K", "S_E4", "S_E8", "S_GAUSS", "S_KLAM")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-38s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point", "zeta"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        if nm.lower() in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load in probe @%d" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle, no zeta, no load in this file; "
                       "cache via CM ward_ only")


# --------------------------------------------------- schedule machinery
def kfac_for(x: int, K: int) -> float:
    return (K - 0.5) / (x * math.log(x))


def nrvm(T: float) -> float:
    """Riemann-von-Mangoldt main term (source-side, no zero data)."""
    if T <= 2 * math.pi * math.e:
        return 7.0 / 8.0
    return T / (2 * math.pi) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


def pad_to(v: np.ndarray, K: int) -> np.ndarray:
    out = np.zeros(K)
    out[:len(v)] = v
    return out


class Rung:
    """All built cells + chain-coherent beta bookkeeping for one x."""

    def __init__(self, x: int, gam: np.ndarray):
        self.x = x
        self.gam = gam
        self.rec: dict[int, dict] = {}

    def build(self, K: int, dps: int, keep_mp: bool = True) -> dict:
        if K in self.rec:
            return self.rec[K]
        x = self.x
        t0 = time.time()
        cell = R4.build_cell(x, kfac_for(x, K), "MAIN", dps,
                             want_mp=True)
        assert cell["K"] == K, "K mismatch %d != %d" % (cell["K"], K)
        kt = R4.prolate_kvec(x, cell)
        rc = CM.rung_core(cell, kt)
        edge = K * math.pi / cell["a"]
        nb = CM.ward_band_count(self.gam, edge)
        r = {"K": K, "dps": dps, "cell": cell, "kt": kt,
             "beta_raw": rc["beta"], "alpha": rc["alpha"],
             "nsoft": rc["nsoft"], "anndim": K - nb,
             "anndim_rvm": K - int(round(nrvm(edge))),
             "gap": rc["gap"], "eps": rc["eps"],
             "eps_str": rc["eps_str"], "gap_str": rc["gap_str"],
             "eigres": rc["eigres"], "resid2v": rc["resid2v"],
             "v0f": rc["v0f"], "v1f": rc["v1f"],
             "build_s": time.time() - t0, "core": rc}
        # chain coherence vs the nearest already-built K
        if not self.rec:
            r["flip"] = 1.0
            r["chain_ov"] = 1.0
        else:
            Kn = min(self.rec, key=lambda q: abs(q - K))
            ref = self.rec[Kn]
            n = max(K, Kn)
            ov = float(np.dot(pad_to(ref["v1c"], n), pad_to(r["v1f"], n)))
            r["flip"] = -1.0 if ov < 0 else 1.0
            r["chain_ov"] = abs(ov)
        r["v1c"] = r["flip"] * r["v1f"]
        r["beta"] = r["flip"] * r["beta_raw"]
        if not keep_mp:
            for kk in ("mpM", "mpV", "mpE", "mpPole", "mpArch",
                       "mpPrime"):
                cell.pop(kk, None)
        self.rec[K] = r
        print("  SCHED x=%-2d K=%-3d kfac %.3f dps %d | beta_raw "
              "%+.6e beta_coh %+.6e ov %.4f | nsoft %-2d anndim %d/%d "
              "| gap %s eigres %.1e | %.1f s (cum %.0f s)"
              % (self.x, K, kfac_for(self.x, K), dps, r["beta_raw"],
                 r["beta"], r["chain_ov"], r["nsoft"], r["anndim"],
                 r["anndim_rvm"], r["gap_str"], r["eigres"],
                 r["build_s"], time.time() - T0_WALL), flush=True)
        return r

    def bracket(self) -> tuple | None:
        ks = sorted(self.rec)
        for a, b in zip(ks, ks[1:]):
            ba, bb = self.rec[a]["beta"], self.rec[b]["beta"]
            if ba == 0.0 or bb == 0.0:
                continue
            if math.copysign(1, ba) != math.copysign(1, bb):
                return (a, b)
        return None

    def bisect(self, dps: int, budget: int,
               guided: int | None = None) -> dict | None:
        used = 0
        first = True
        while used < budget:
            br = self.bracket()
            if br is None or br[1] - br[0] <= 1:
                break
            a, b = br
            if first and guided is not None and a < guided < b:
                Km = guided
            else:
                Km = (a + b) // 2
            first = False
            self.build(Km, dps)
            used += 1
        br = self.bracket()
        if br is None:
            return None
        a, b = br
        ra, rb = self.rec[a], self.rec[b]
        Kstar = a + (b - a) * ra["beta"] / (ra["beta"] - rb["beta"])
        out = {"K_lo": a, "K_hi": b, "beta_lo": ra["beta"],
               "beta_hi": rb["beta"], "Kstar": Kstar,
               "tight": (b - a == 1),
               "betac": min(abs(ra["beta"]), abs(rb["beta"])),
               "step": (abs(rb["beta"] - ra["beta"]) / (b - a)),
               "K_best": a if abs(ra["beta"]) <= abs(rb["beta"]) else b}
        return out


# ---------------------------------------------------- T2 kernel basis
def toeplitz_avg(M: np.ndarray) -> np.ndarray:
    K = M.shape[0]
    out = np.zeros_like(M)
    for o in range(K):
        d = np.mean(np.diagonal(M, offset=o))
        for i in range(K - o):
            out[i, i + o] = d
            out[i + o, i] = d
    return out


def hankel_avg(M: np.ndarray) -> np.ndarray:
    K = M.shape[0]
    out = np.zeros_like(M)
    Mf = np.fliplr(M)
    for o in range(-(K - 1), K):
        d = np.mean(np.diagonal(Mf, offset=o))
        for i in range(K):
            j = K - 1 - (i - o)
            if 0 <= j < K:
                out[i, j] = d
    return out


def _cosint(w: float, a: float) -> float:
    if abs(w) < 1e-14:
        return 2.0 * a
    return 2.0 * math.sin(w * a) / w


def lprof_matrix(cell: dict, x: int) -> np.ndarray:
    """Multiplication by g(v) = sum_q Lambda(q)/sqrt(q) cos(log q * v)
    in the normalized cos basis on [-a, a] (exact closed form, f64)."""
    a = cell["a"]
    K = cell["K"]
    om = cell["om"]
    nrm = np.full(K, math.sqrt(a))
    nrm[0] = math.sqrt(2 * a)
    atoms = CM.prime_power_atoms(x)
    M = np.zeros((K, K))
    for q, lq in atoms:
        w = lq / math.sqrt(q)
        mu = math.log(q)
        for i in range(K):
            for j in range(i, K):
                s = (_cosint(om[i] - om[j] - mu, a)
                     + _cosint(om[i] - om[j] + mu, a)
                     + _cosint(om[i] + om[j] - mu, a)
                     + _cosint(om[i] + om[j] + mu, a))
                M[i, j] += w * 0.25 * s / (nrm[i] * nrm[j])
    for i in range(K):
        for j in range(i + 1, K):
            M[j, i] = M[i, j]
    return M


def kernel_basis(cell: dict, x: int, kt: np.ndarray,
                 tp: dict) -> dict:
    K = cell["K"]
    om = cell["om"]
    out = {}
    out["S_K"] = ("terms", [(1.0, kt)])
    out["S_E4"] = ("terms", [(1.0, tp["ehat"][4])])
    out["S_E8"] = ("terms", [(1.0, tp["ehat"][8])])
    out["S_GAUSS"] = ("terms", [(1.0, tp["t_gauss"])])
    out["S_KLAM"] = ("terms", [(1.0, tp["t_klam"])])
    for nm, M in (("S_POS2", SP.v2_matrix(cell)),
                  ("S_FREQ", np.diag((om / om[K - 1]) ** 2)),
                  ("S_ABSD", np.diag(om / om[K - 1])),
                  ("S_PRIME", cell["blk_prime"].copy()),
                  ("S_TOEP", toeplitz_avg(cell["blk_prime"])),
                  ("S_HANK", hankel_avg(cell["blk_prime"])),
                  ("S_LPROF", lprof_matrix(cell, x))):
        f = float(np.linalg.norm(M))
        out[nm] = ("mat64", M / f)
    return out


def kernel_opt(c: np.ndarray, d: np.ndarray,
               G: np.ndarray) -> tuple[np.ndarray, float]:
    """argmax (theta.d)^2 / theta.G.theta  s.t. theta.c = 0."""
    _u, _s, vh = np.linalg.svd(c[None, :])
    B = vh[1:].T
    Gb = B.T @ G @ B
    rhs = B.T @ d
    u = np.linalg.pinv(Gb, rcond=PINV_RCOND) @ rhs
    th = B @ u
    nq = math.sqrt(max(float(th @ G @ th), 1e-300))
    th = th / nq
    return th, abs(float(th @ d))


def phi_of(s00: float, s01: float, s11: float) -> float:
    dd = s00 - s11
    if dd == 0.0:
        return math.pi / 4 if s01 != 0.0 else 0.0
    return 0.5 * math.atan(2.0 * s01 / dd)


def theta_reads(th: np.ndarray, trip: dict, Scf: dict) -> dict:
    """Doublet + cluster reads of S(theta) from the per-op mp exports."""
    s00 = float(sum(th[i] * trip[nm][0]
                    for i, nm in enumerate(KER_BASIS)))
    s01 = float(sum(th[i] * trip[nm][1]
                    for i, nm in enumerate(KER_BASIS)))
    s11 = float(sum(th[i] * trip[nm][2]
                    for i, nm in enumerate(KER_BASIS)))
    C = sum(th[i] * Scf[nm] for i, nm in enumerate(KER_BASIS))
    w, U = np.linalg.eigh(C)
    order = np.argsort(w)
    ovs = np.abs(U[0, :])
    istar = int(np.argmax(ovs))
    rank = int(np.where(order == istar)[0][0])
    d = len(w)
    evs = w[order]
    spread = float(evs[-1] - evs[0])
    iso = min([abs(evs[rank] - evs[r]) for r in range(d) if r != rank],
              default=0.0)
    pos = "BOT" if rank == 0 else ("TOP" if rank == d - 1
                                   else "MID%d" % rank)
    return {"s00": s00, "s01": s01, "s11": s11,
            "phi": phi_of(s00, s01, s11),
            "split": math.hypot(s00 - s11, 2 * s01),
            "branch": "MAX" if s00 > s11 else "MIN",
            "pos": pos, "ov0": float(ovs[istar]),
            "split_rel": iso / max(spread, 1e-300), "evs": evs}


def theta_reads_at(th: np.ndarray, trip: dict, Scf: dict,
                   branch: str, pos: str) -> dict:
    """Achieved reads with the FROZEN branch/pos applied."""
    r = theta_reads(th, trip, Scf)
    phi = r["phi"]
    match = (r["branch"] == branch)
    ovd = math.cos(phi) if match else abs(math.sin(phi))
    C = sum(th[i] * Scf[nm] for i, nm in enumerate(KER_BASIS))
    w, U = np.linalg.eigh(C)
    order = np.argsort(w)
    d = len(w)
    rank = 0 if pos == "BOT" else (d - 1 if pos == "TOP"
                                   else int(pos[3:]))
    rank = min(max(rank, 0), d - 1)
    iv = order[rank]
    evs = w[order]
    spread = float(evs[-1] - evs[0])
    iso = min([abs(evs[rank] - evs[r]) for r in range(d) if r != rank],
              default=0.0)
    return {"ov_dblt": ovd, "phi_ach": math.acos(min(ovd, 1.0)),
            "ov_clu": float(abs(U[0, iv])),
            "split_rel": iso / max(spread, 1e-300),
            "s01": r["s01"], "split": r["split"]}


# --------------------------------------------------------- symbolic S1
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as spy
    out = []
    # shared rational orthogonal spectral example
    S3 = spy.Matrix([[0, spy.Rational(1, 2), spy.Rational(-1, 3)],
                     [spy.Rational(-1, 2), 0, spy.Rational(1, 5)],
                     [spy.Rational(1, 3), spy.Rational(-1, 5), 0]])
    I3 = spy.eye(3)
    R = (I3 - S3).inv() * (I3 + S3)
    lam = spy.diag(spy.Rational(1, 7), spy.Rational(3, 5),
                   spy.Integer(2))
    Q3 = R * lam * R.T
    v0 = R.col(0)
    v1 = R.col(1)
    # G10: the commutator functional on sym(3) has rank exactly 1 and
    # kernel {s01 = 0} (codim 1): image == (E0-E1) * s01 per basis elt
    basis = []
    for i in range(3):
        for j in range(i, 3):
            E = spy.zeros(3, 3)
            E[i, j] = 1
            E[j, i] = 1
            basis.append(E)
    ok10 = True
    nonzero = 0
    for E in basis:
        comm = (v0.T * (Q3 * E - E * Q3) * v1)[0, 0]
        s01 = (v0.T * E * v1)[0, 0]
        ok10 = ok10 and spy.simplify(
            comm - (lam[0, 0] - lam[1, 1]) * s01) == 0
        if spy.simplify(s01) != 0:
            nonzero += 1
    ok10 = ok10 and nonzero >= 1
    out.append(("G10-kernel-codim1-exact", ok10,
                "S -> <v0,[Q,S]v1> == (E0-E1)<v0,S v1> on all 6 sym "
                "basis elements (rational orthogonal example): the "
                "commutator kernel of ANY operator family is exactly "
                "{s01 = 0}, codim <= 1 -- the hunt is a linear "
                "problem in S"))
    # G11: constrained maximizer closed form on an exact instance
    G = spy.Matrix([[2, spy.Rational(1, 3), 0],
                    [spy.Rational(1, 3), 1, spy.Rational(1, 5)],
                    [0, spy.Rational(1, 5), 3]])
    cv = spy.Matrix([1, 1, 1])
    dv = spy.Matrix([1, 0, -2])
    B = spy.Matrix([[1, 0], [-1, 1], [0, -1]])   # basis of c-perp
    Gb = B.T * G * B
    th = B * Gb.inv() * B.T * dv
    val = (dv.T * B * Gb.inv() * B.T * dv)[0, 0]
    q = (th.T * G * th)[0, 0]
    r0 = (th.T * dv)[0, 0]
    ok11 = (spy.simplify((cv.T * th)[0, 0]) == 0
            and spy.simplify(r0 ** 2 / q - val) == 0)
    t = spy.symbols("t")
    for wcol in range(2):
        wv = B.col(wcol)
        F = ((th + t * wv).T * dv)[0, 0] ** 2 \
            / ((th + t * wv).T * G * (th + t * wv))[0, 0]
        ok11 = ok11 and spy.simplify(spy.diff(F, t).subs(t, 0)) == 0
    out.append(("G11-constrained-max-exact", ok11,
                "theta* = B (B^T G B)^-1 B^T d satisfies c.theta = 0, "
                "attains (theta.d)^2/theta.G.theta = d^T B(B^T G B)^-1 "
                "B^T d, and is stationary in every kernel direction "
                "(exact rational instance): the in-kernel max-split "
                "problem has this closed form"))
    # G12: 2x2 rotation / trade-off (round-126 G10 re-gated)
    s00, s01, s11 = spy.symbols("s00 s01 s11", real=True)
    dd = s00 - s11
    t2 = 2 * s01 / dd
    c2 = 1 / spy.sqrt(1 + t2 ** 2)
    s2 = t2 * c2
    off = s01 * c2 - dd / 2 * s2
    ok12 = spy.simplify(off) == 0
    out.append(("G12-rotation-tradeoff-exact", ok12,
                "tan(2 phi) = 2 s01/(s00-s11) kills the 2x2 "
                "off-diagonal exactly: phi ~= |s01|/split is the "
                "selector error angle; with G10 this is the exact "
                "accuracy-split trade-off"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("frameschedule_probe -- PRIME.CCM.FRAMESCHEDULE.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    if smoke:
        grid = {3: (5, 6, 7, 8), 5: (11, 12, 13, 17)}
        xs_main = (3, 5)
        gate_x = (3, 5)
        deep_x = (5,)
        ker_x = (3, 5)
        worlds_on = False
    else:
        grid = dict(GRID_K)
        xs_main = XS_MAIN
        gate_x = GATE_X
        deep_x = DEEP_X
        ker_x = KER_X
        worlds_on = True

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det)
    gam = CM.ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)))

    # ---------------------------------------------------------- S1
    section("S1  EXACT GATES (sympy + integer dial)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg)
    xl3 = 3 * math.log(3)
    ca = R4.build_cell(3, 4.5 / xl3, "MAIN", 45)
    cb = R4.build_cell(3, 4.9 / xl3, "MAIN", 45)
    same = bool(np.array_equal(ca["m_tilde"], cb["m_tilde"])) \
        and ca["K"] == cb["K"] == 5
    check("G13-integer-dial-exact", same,
          "kfac 1.365 and 1.487 both give K = 5 at x = 3 and "
          "BIT-IDENTICAL f64 matrices: the cell depends on kfac only "
          "via K = ceil(kfac x log x) -- the frame dial is the "
          "INTEGER K, the crossing is a sign flip between adjacent K, "
          "and the crossing floor is set by the step size, not zero")

    # ---------------------------------------------------------- S2
    section("S2  THE COUPLED (x, K) SCHEDULE (grids + bisection)")
    rungs: dict[int, Rung] = {}
    cross: dict[int, dict | None] = {}
    pred_log: list[str] = []

    def gamma_of(x: int, Kst: float) -> float:
        return Kst / (x * math.log(x))

    def pfit_predict(xs_fit: list[int], Kst: dict, x_new: int) -> int:
        lx = [math.log(x) for x in xs_fit]
        ly = [math.log(gamma_of(x, Kst[x])) for x in xs_fit]
        if len(xs_fit) == 2:
            p = (ly[1] - ly[0]) / (lx[1] - lx[0])
            A = ly[0] - p * lx[0]
        else:
            p, A = np.polyfit(lx, ly, 1)
        g = math.exp(A + p * math.log(x_new))
        return int(round(g * x_new * math.log(x_new)))

    def prvm_predict(xs_fit: list[int], Kst: dict, x_new: int) -> int:
        astar = float(np.mean(
            [Kst[x] - nrvm(Kst[x] * math.pi / (math.log(x) / 2))
             for x in xs_fit]))
        a_new = math.log(x_new) / 2
        lo = int(math.ceil(1.0 * x_new * math.log(x_new)))
        hi = int(math.ceil(3.0 * x_new * math.log(x_new)))
        best, bK = None, lo
        for K in range(lo, hi + 1):
            v = abs((K - nrvm(K * math.pi / a_new)) - astar)
            if best is None or v < best:
                best, bK = v, K
        return bK

    Kst: dict[int, float] = {}
    guided_used: dict[int, int | None] = {}
    for x in xs_main:
        if x not in grid:
            continue
        rg = Rung(x, gam)
        rungs[x] = rg
        for K in grid[x]:
            dps = DPS_PIN[x] if K == grid[x][0] else DPS_ENR[x]
            if x in PIN_K and K == PIN_K[x]:
                dps = DPS_PIN[x]
            rg.build(K, dps)
        guided = None
        if not smoke and x == 13 and all(q in Kst for q in (5, 8)):
            guided = pfit_predict([5, 8], Kst, 13)
            pred_log.append("P-FIT stage1 (5,8) -> K_pred(13) = %d"
                            % guided)
            prv = prvm_predict([5, 8], Kst, 13)
            pred_log.append("P-RVM stage1 (5,8) -> K_pred(13) = %d"
                            % prv)
        if not smoke and x == 18 and all(q in Kst for q in (5, 8, 13)):
            guided = pfit_predict([5, 8, 13], Kst, 18)
            pred_log.append("P-FIT stage2 (5,8,13) -> K_pred(18) = %d"
                            % guided)
            prv = prvm_predict([5, 8, 13], Kst, 18)
            pred_log.append("P-RVM stage2 (5,8,13) -> K_pred(18) = %d"
                            % prv)
        guided_used[x] = guided
        cr = rg.bisect(DPS_ENR[x], BISECT_BUDGET.get(x, 0),
                       guided=guided)
        cross[x] = cr
        if cr is not None:
            Kst[x] = cr["Kstar"]
            print("  CROSSING x=%-2d bracket (%d, %d) beta (%+.3e, "
                  "%+.3e) K* %.3f tight %s | betac* %.3e step %.3e"
                  % (x, cr["K_lo"], cr["K_hi"], cr["beta_lo"],
                     cr["beta_hi"], cr["Kstar"], cr["tight"],
                     cr["betac"], cr["step"]), flush=True)
        else:
            print("  CROSSING x=%-2d NO SIGN FLIP in scanned range %s"
                  % (x, sorted(rungs[x].rec)), flush=True)
    # x=24 predictor single-shot (after 18)
    if not smoke and 24 in rungs and all(q in Kst for q in (5, 8, 13, 18)):
        kp24 = pfit_predict([5, 8, 13, 18], Kst, 24)
        pred_log.append("P-FIT stage3 (5,8,13,18) -> K_pred(24) = %d"
                        % kp24)
        prv24 = prvm_predict([5, 8, 13, 18], Kst, 24)
        pred_log.append("P-RVM stage3 (5,8,13,18) -> K_pred(24) = %d"
                        % prv24)
        rungs[24].build(kp24, DPS_ENR[24])
        guided_used[24] = kp24
        cross[24] = rungs[24].bisect(DPS_ENR[24], 0)  # loose record
    for s in pred_log:
        info(s)

    # per-cell hard gates
    okeig = True
    okchain = True
    for x, rg in rungs.items():
        for K, r in rg.rec.items():
            okeig = okeig and r["eigres"] <= 10.0 ** (-(r["dps"] // 2))
            if x in gate_x and K != sorted(rg.rec)[0]:
                okchain = okchain and r["chain_ov"] >= CHAIN_OV_BAR
    check("G23-eigen-residuals", okeig,
          "||Q v_i - lam_i v_i|| <= 10^-(dps/2) at every built cell "
          "(worst %.1e)" % max(r["eigres"] for rg in rungs.values()
                               for r in rg.rec.values()))
    deep_ovs = ["x%d:%.4f" % (x, min(r["chain_ov"]
                                     for K, r in rungs[x].rec.items()
                                     if K != sorted(rungs[x].rec)[0]))
                for x in rungs if len(rungs[x].rec) > 1]
    check("G30-chain-coherence", okchain,
          "v1 sign chain (zero-padded prefix overlaps) >= %.2f at the "
          "gate rungs (hard); min |ov| per rung: %s -- the flip "
          "adjudication runs on the chain-coherent sign"
          % (CHAIN_OV_BAR, ", ".join(deep_ovs)))
    # regression pins (RAW convention)
    okreg = True
    regd = []
    for x, Kp in PIN_K.items():
        if x not in rungs or Kp not in rungs[x].rec:
            continue
        r = rungs[x].rec[Kp]
        rel = abs(abs(r["beta_raw"]) / SP.R124_BETA[x] - 1)
        gr = abs(r["gap"] / SP.R124_GAP[x] - 1)
        okreg = okreg and rel <= REG_BAR and gr <= 1e-4 \
            and r["nsoft"] == SP.R124_NSOFT[x]
        regd.append("x%d:b%.1e,g%.1e" % (x, rel, gr))
    check("G21-r124-regression", okreg or smoke,
          "1.25-cell beta/gap/nsoft vs round-124 pins: %s"
          % ", ".join(regd))
    okl = True
    lad = []
    for (x, K), bpin in R124_LADDER_RAW.items():
        if x not in rungs or K not in rungs[x].rec:
            continue
        r = rungs[x].rec[K]
        rel = abs(r["beta_raw"] / bpin - 1)
        okl = okl and rel <= KLADDER_BAR
        lad.append("x%dK%d:%.1e" % (x, K, rel))
    okad = True
    for (x, K), apin in R124_ANNDIM.items():
        if x not in rungs or K not in rungs[x].rec:
            continue
        okad = okad and rungs[x].rec[K]["anndim"] == apin
    check("G22-r124-kfac-ladder-pins", (okl and okad) or smoke,
          "enriched-frame beta_raw vs the round-124 amendment-1 rows "
          "(bar %.0e rel): %s; anndim rows exact: %s"
          % (KLADDER_BAR, ", ".join(lad), "OK" if okad else "DEV"))
    # anndim ward vs RvM
    okrv = True
    worst_rv = 0
    for x, rg in rungs.items():
        for K, r in rg.rec.items():
            dev = abs(r["anndim"] - r["anndim_rvm"])
            worst_rv = max(worst_rv, dev)
            okrv = okrv and dev <= 2
    check("G24-anndim-rvm-ward", okrv,
          "annihilator dim (ward zero count) == K - round(N_rvm(edge)) "
          "+- 2 at every cell (worst dev %d): the frame-schedule "
          "coordinate anndim is SOURCE-computable via the RvM main "
          "term" % worst_rv)
    # dps-downshift ward at x=18 crossing cell
    if not smoke and 18 in cross and cross[18] is not None:
        Klo = cross[18]["K_lo"]
        r120 = rungs[18].rec[Klo]
        t0 = time.time()
        cell160 = R4.build_cell(18, kfac_for(18, Klo), "MAIN", 160,
                                want_mp=True)
        kt160 = R4.prolate_kvec(18, cell160)
        rc160 = CM.rung_core(cell160, kt160)
        dev = abs(abs(rc160["beta"]) - abs(r120["beta_raw"]))
        check("G26-dps-ward-x18", dev <= DPS_WARD_BAR,
              "x=18 K=%d rebuilt at dps 160: | |beta_160| - "
              "|beta_120| | = %.1e (bar %.0e, %.0f s): the enriched-"
              "cell dps downshift is certified" % (Klo, dev,
                                                   DPS_WARD_BAR,
                                                   time.time() - t0))
        del cell160
    # grid certification at x=24 cells + deep crossing cells
    if not smoke:
        okgc = True
        gcd = []
        gc_list = [(24, K) for K in (rungs[24].rec if 24 in rungs
                                     else ())]
        for x in deep_x:
            if cross.get(x) is not None:
                gc_list.append((x, cross[x]["K_best"]))
        for x, K in gc_list:
            r = rungs[x].rec[K]
            cell = r["cell"]
            L = cell["a"]
            kd = CM.kfun_data(x)
            vg = np.linspace(-L, L, 40001)
            kv = CM.k_vals_on(kd, vg, int(x) + 2)
            pr = CM.project_cell(kv, vg, cell)
            pr = pr / np.linalg.norm(pr)
            b40 = CM.mp_overlap(cell, r["v1f"], pr, normalize=False)
            dev = abs(b40 - r["beta_raw"])
            okgc = okgc and dev <= GRID_CERT_BAR
            gcd.append("x%dK%d:%.1e" % (x, K, dev))
        check("G27-grid-certification", okgc,
              "|beta_40001 - beta_20001| <= %.0e at the x=24 cells "
              "and the deep crossing cells: %s"
              % (GRID_CERT_BAR, ", ".join(gcd)))

    # ---------------------------------------------------------- S3
    section("S3  SCHEDULE LAWS (flip, floors, steps, cost)")
    flip_rows = []
    for x in sorted(rungs):
        cr = cross.get(x)
        if cr is None:
            flip_rows.append("x%d:NOFLIP" % x)
        else:
            raw_a = rungs[x].rec[cr["K_lo"]]["beta_raw"]
            raw_b = rungs[x].rec[cr["K_hi"]]["beta_raw"]
            conv = (math.copysign(1, raw_a) != math.copysign(1, raw_b))
            flip_rows.append("x%d:COH-FLIP%s@(%d,%d)"
                             % (x, "+RAW" if conv else "(RAW-blind)",
                                cr["K_lo"], cr["K_hi"]))
    hard_flip = all(cross.get(x) is not None
                    for x in (5, 8, 13) if x in rungs) or smoke
    check("G31-flip-existence", hard_flip,
          "sign flip in the CHAIN-COHERENT convention: %s (hard at "
          "x = 5, 8, 13 where round 124 measured the raw flip; x = 18 "
          "typed) -- adjudicates FLIP-REAL-SIGNED vs "
          "CONVENTION-ARTIFACT" % "; ".join(flip_rows))
    crd = []
    for x in sorted(rungs):
        cr = cross.get(x)
        if cr is not None:
            crd.append("x%d: K* %.2f (gamma_c %.3f) betac* %.2e "
                       "step %.2e %s"
                       % (x, cr["Kstar"], gamma_of(x, cr["Kstar"]),
                          cr["betac"], cr["step"],
                          "TIGHT" if cr["tight"] else "LOOSE"))
    check("G32-crossing-pins", True,
          "crossing records: " + ("; ".join(crd) if crd else "none"))
    satd = []
    for x, (Ka, Kb) in SAT_PAIR.items():
        if x in rungs and Ka in rungs[x].rec and Kb in rungs[x].rec:
            ba = rungs[x].rec[Ka]["beta"]
            bb = rungs[x].rec[Kb]["beta"]
            rel = abs(bb - ba) / max(abs(bb), 1e-300)
            satd.append("x%d:(K%d->K%d) %.3f" % (x, Ka, Kb, rel))
    check("G33-saturation-reads", True,
          "|beta| change across the two deepest grid frames "
          "(saturation currency): %s; x=24 saturation UNMEASURED "
          "(budget decision, disclosed)" % ", ".join(satd))
    # matched-2.0 floor law
    fl_x, fl_b = [], []
    for x, K in MATCH20_K.items():
        if x in rungs and K in rungs[x].rec:
            fl_x.append(x)
            fl_b.append(abs(rungs[x].rec[K]["beta"]))
    slope20 = float("nan")
    if len(fl_x) >= 3:
        slope20 = CM.ols_slope([math.log10(t) for t in fl_x],
                               [math.log10(max(t, 1e-300))
                                for t in fl_b])[0]
    cont = (abs(slope20 - FLOOR_SLOPE) <= FLOOR_BAND
            if slope20 == slope20 else False)
    check("G34-matched-floor-law", True,
          "matched KFAC-2.0 floor |beta| = %s at x = %s: OLS slope "
          "log|beta| vs log x = %.3f => FLOOR-LAW-%s (band %.1f +- "
          "%.1f)" % (["%.2e" % t for t in fl_b], fl_x, slope20,
                     "CONTINUES" if cont else "BREAKS",
                     FLOOR_SLOPE, FLOOR_BAND))
    # crossing-floor + step laws + proximity decomposition
    cf_x = [x for x in sorted(rungs) if cross.get(x) is not None
            and cross[x]["tight"]]
    sl_cf = sl_st = float("nan")
    if len(cf_x) >= 3:
        sl_cf = CM.ols_slope([math.log10(x) for x in cf_x],
                             [math.log10(max(cross[x]["betac"], 1e-300))
                              for x in cf_x])[0]
        sl_st = CM.ols_slope([math.log10(x) for x in cf_x],
                             [math.log10(max(cross[x]["step"], 1e-300))
                              for x in cf_x])[0]
    check("G35-crossing-floor-law", True,
          "integer-crossing floor betac* %s and step Delta %s over "
          "x = %s: slopes %.3f / %.3f -- the best achievable frame-"
          "dial selection floor and its quantum"
          % (["%.2e" % cross[x]["betac"] for x in cf_x],
             ["%.2e" % cross[x]["step"] for x in cf_x], cf_x,
             sl_cf, sl_st))
    proxd = []
    for x in sorted(rungs):
        cr = cross.get(x)
        if cr is None or x not in MATCH20_K:
            continue
        K20 = MATCH20_K[x]
        if K20 not in rungs[x].rec:
            continue
        b20 = abs(rungs[x].rec[K20]["beta"])
        pred = cr["step"] * abs(K20 - cr["Kstar"])
        proxd.append("x%d: |beta20| %.2e vs step*dist %.2e (ratio "
                     "%.2f, dist %.1f)" % (x, b20, pred,
                                           b20 / max(pred, 1e-300),
                                           abs(K20 - cr["Kstar"])))
    check("G36-proximity-decomposition", True,
          "matched-floor vs crossing-proximity model |beta(K20)| ~= "
          "step * |K20 - K*|: %s -- ratios ~1 with shrinking dist "
          "type the x^-2.8 law PROXIMITY-ARTIFACT, ratios/dist "
          "stable type it GENUINE" % "; ".join(proxd))
    # cost law
    cx, cy = [], []
    for x, rg in rungs.items():
        for K, r in rg.rec.items():
            cx.append((K, r["dps"], r["build_s"]))
    try:
        A = np.array([[math.log(k), math.log(d), 1.0]
                      for k, d, _s in cx])
        y = np.array([math.log(max(s, 1e-3)) for _k, _d, s in cx])
        coef = np.linalg.lstsq(A, y, rcond=None)[0]
        pk, pd = float(coef[0]), float(coef[1])
        t222 = math.exp(float(coef[2])) * 222 ** pk * 280 ** pd
    except Exception:
        pk = pd = t222 = float("nan")
    check("G37-cost-law", True,
          "build cost fit t ~ K^%.2f dps^%.2f over %d builds; "
          "extrapolated x=32 matched cell (K=222, dps>=280): %.0f s "
          "PER BUILD -- x=32 DECLINED (stated, not attempted)"
          % (pk, pd, len(cx), t222))

    # ---------------------------------------------------------- S4
    section("S4  PREDICTOR ADJUDICATION (out-of-sample)")
    pred_ok = None
    if not smoke:
        rows = []
        phi_pred: dict[int, float] = {}
        for x in deep_x:
            kp = guided_used.get(x)
            cr = cross.get(x)
            if kp is None or cr is None:
                rows.append("x%d: n/a" % x)
                continue
            dist = abs(kp - cr["Kstar"])
            bpred = (abs(rungs[x].rec[kp]["beta"])
                     if kp in rungs[x].rec else float("nan"))
            phi_pred[x] = bpred
            K20 = MATCH20_K[x]
            b20 = abs(rungs[x].rec[K20]["beta"])
            rows.append("x%d: K_pred %d vs K* %.2f (dist %.2f) "
                        "phi_pred %.2e vs matched floor %.2e (%s)"
                        % (x, kp, cr["Kstar"], dist, bpred, b20,
                           "BEATS" if bpred <= b20 else "MISSES"))
        check("G41-oos-deep", True, "; ".join(rows))
        pred_ok = all(
            x in phi_pred and cross.get(x) is not None
            and phi_pred[x] <= abs(rungs[x].rec[MATCH20_K[x]]["beta"])
            for x in deep_x)
        r24 = ""
        if 24 in rungs and guided_used.get(24) in rungs[24].rec:
            kp24 = guided_used[24]
            b24p = rungs[24].rec[kp24]["beta"]
            b2420 = rungs[24].rec[MATCH20_K[24]]["beta"]
            r24 = ("x24 SINGLE-SHOT: beta(K_pred=%d) = %+.3e vs "
                   "beta(K_2.0=153) = %+.3e (|ratio| %.3f)"
                   % (kp24, b24p, b2420,
                      abs(b24p) / max(abs(b2420), 1e-300)))
        check("G43-x24-single-shot", True, r24 or "n/a")
        check("G44-predictor-adjudication", True,
              "CROSSING-%s (bar: phi_pred <= matched-2.0 floor at "
              "x = 13 AND 18)" % ("SOURCE-PREDICTABLE" if pred_ok
                                  else "CONNES-PINNED"))

    # ---------------------------------------------------------- S5
    section("S5  THE CERTIFIED APPROXIMANT AT THE CROSSING FRAME")
    apx_rows = []
    okf64 = True
    if not smoke:
        for x in deep_x:
            cr = cross.get(x)
            if cr is None:
                continue
            r = rungs[x].rec[cr["K_best"]]
            cell = r["cell"]
            if "mpV" not in cell:
                continue
            kt = r["kt"]
            ncl = r["nsoft"] + 1
            w, U = np.linalg.eigh(cell["m_tilde"])
            B = U[:, :ncl]
            xi = B @ (B.T @ kt)
            xi = xi / np.linalg.norm(xi)
            with mp.workdps(cell["dps"]):
                K = cell["K"]
                v0 = R4.matcol(cell["mpV"], 0, K)
                kv = CM.lift_vec(kt)
                if R4.mp_dot(v0, kv) < 0:
                    v0 = [-t for t in v0]
                xm = CM.lift_vec(xi)
                ov = float(abs(R4.mp_dot(v0, xm)))
                qx = R4.matvec(cell["mpM"], xm, K)
                ray = float(R4.mp_dot(xm, qx))
                eps = float(cell["mpE"][0])
            err = math.sqrt(max(2.0 - 2.0 * ov, 0.0))
            okf64 = okf64 and ov >= 1.0 - F64_BAR
            b125 = abs(rungs[x].rec[PIN_K[x]]["beta"])
            b20 = abs(rungs[x].rec[MATCH20_K[x]]["beta"])
            apx_rows.append(
                "x%d K%d: ov %.10f err %.2e (1.25-frame beta %.2e, "
                "matched %.2e, crossing floor %.2e) R(xi^)-eps %+.2e "
                "eps %+.2e" % (x, cr["K_best"], ov, err, b125, b20,
                               cr["betac"], ray - eps, eps))
        check("G50-f64-approximant", okf64 or not apx_rows,
              "xi-hat = f64-pipeline S_K selection at the crossing "
              "frame vs mp truth: %s (bar ov >= 1 - %.0e): the "
              "certified approximant exists at f64 spectral cost"
              % ("; ".join(apx_rows), F64_BAR))
        check("G52-omega-absorption", True,
              "R(xi-hat) >= eps ALWAYS (Rayleigh from above): the "
              "approximant upper-bounds eps_lambda and cannot certify "
              "its SIGN; the RH datum is sign(eps_lambda) >= 0 for "
              "all lambda, which no vector approximant touches "
              "-- OMEGA-ABSORBED (the min-cut LANEACONV/R4HYP edges "
              "are determinant/positivity data, not vector data)")
        # crossing-frame screens (Z1 in-band + above-band disguise)
        scr_rows = []
        for x in deep_x:
            cr = cross.get(x)
            if cr is None:
                continue
            r = rungs[x].rec[cr["K_best"]]
            cell = r["cell"]
            if "mpV" not in cell:
                continue
            edge = r["K"] * math.pi / cell["a"]
            inb = gam[gam <= edge][:5]
            abv = gam[gam > edge][:ZAB_N]
            kt = r["kt"]
            cb = SP.cluster_basis_mp(cell, kt)
            d = len(cb["soft"])
            mx_in = 0.0
            for g in inb:
                ev = SP.ward_evec_gamma(cell, float(g))
                ev = ev / np.linalg.norm(ev)
                with mp.workdps(cell["dps"]):
                    o0 = abs(float(R4.mp_dot(cb["vecs"][0],
                                             CM.lift_vec(ev))))
                    o1 = abs(float(R4.mp_dot(cb["vecs"][1],
                                             CM.lift_vec(ev))))
                mx_in = max(mx_in, o0, o1)
            G = np.zeros((d, d))
            for g in abv:
                ev = SP.ward_evec_gamma(cell, float(g))
                ev = ev / np.linalg.norm(ev)
                with mp.workdps(cell["dps"]):
                    cc = np.array([float(R4.mp_dot(cb["vecs"][i],
                                                   CM.lift_vec(ev)))
                                   for i in range(d)])
                G += np.outer(cc, cc)
            ScK = SP.compress_selector(cell, cb, "terms", [(1.0, kt)])
            Sf = np.array([[float(ScK[i, j]) for j in range(d)]
                           for i in range(d)])
            G0 = G - np.trace(G) / d * np.eye(d)
            S0 = Sf - np.trace(Sf) / d * np.eye(d)
            den = np.linalg.norm(G0) * np.linalg.norm(S0)
            corr = abs(float(np.sum(S0 * G0)) / den) if den > 0 else 0.0
            scr_rows.append("x%d: in-band doublet max %.1e, "
                            "above-band corr %.2f" % (x, mx_in, corr))
        check("G53-crossing-screens", True,
              "crossing-frame S_K screens: %s (disguise flag %.2f; "
              "in-band = annihilator law)"
              % ("; ".join(scr_rows), DISGUISE_CORR))

    # ---------------------------------------------------------- S6
    section("S6  THE COMMUTATOR KERNEL (12-op source basis)")
    # instrument ward: LPROF closed form vs grid quadrature + oracle
    xw = ker_x[0]
    if xw in rungs:
        rw = rungs[xw].rec[PIN_K.get(xw, sorted(rungs[xw].rec)[0])]
        cellw = rw["cell"]
        Lw = cellw["a"]
        Kw = cellw["K"]
        omw = cellw["om"]
        Mlp = lprof_matrix(cellw, xw)
        vgw = np.linspace(-Lw, Lw, 40001)
        gv = np.zeros_like(vgw)
        for q, lq in CM.prime_power_atoms(xw):
            gv = gv + (lq / math.sqrt(q)) * np.cos(math.log(q) * vgw)
        worst = 0.0
        for (i, j) in ((0, 0), (0, min(3, Kw - 1)),
                       (min(2, Kw - 1), min(4, Kw - 1)), (1, 1)):
            bi = (np.full_like(vgw, 1.0 / math.sqrt(2 * Lw)) if i == 0
                  else np.cos(omw[i] * vgw) / math.sqrt(Lw))
            bj = (np.full_like(vgw, 1.0 / math.sqrt(2 * Lw)) if j == 0
                  else np.cos(omw[j] * vgw) / math.sqrt(Lw))
            qv = float(np.trapezoid(gv * bi * bj, vgw))
            worst = max(worst, abs(qv - Mlp[i, j])
                        / max(abs(Mlp[i, j]), 1e-12))
        cbw = SP.cluster_basis_mp(cellw, rw["kt"])
        ScO = SP.compress_selector(cellw, cbw, "terms",
                                   [(1.0, cbw["vecs_f64"][0])])
        dO = SP.dblt_read(cellw, ScO)
        okO = abs(dO["phi"]) <= 1e-10 and abs(dO["s01"]) <= 1e-10
        check("G60-basis-wards", worst <= LPROF_WARD_BAR and okO,
              "S_LPROF closed form vs 40001-grid quadrature worst rel "
              "%.1e (bar %.0e); kernel-pipeline oracle v0 v0^T: phi "
              "%.1e s01 %.1e (exact)" % (worst, LPROF_WARD_BAR,
                                         dO["phi"], dO["s01"]))
    ker: dict[int, dict] = {}
    for x in ker_x:
        if x not in rungs:
            continue
        Kp = PIN_K.get(x, sorted(rungs[x].rec)[0])
        r = rungs[x].rec[Kp]
        cell = r["cell"]
        if "mpV" not in cell:
            continue
        kt = r["kt"]
        tp = SP.build_templates(cell, x)
        basis = kernel_basis(cell, x, kt, tp)
        cb = SP.cluster_basis_mp(cell, kt)
        d = len(cb["soft"])
        trip = {}
        Scf = {}
        for nm in KER_BASIS:
            kind, payload = basis[nm]
            Sc = SP.compress_selector(cell, cb, kind, payload)
            db = SP.dblt_read(cell, Sc)
            trip[nm] = (db["s00"], db["s01"], db["s11"])
            Scf[nm] = np.array([[float(Sc[i, j]) for j in range(d)]
                                for i in range(d)])
        c = np.array([trip[nm][1] for nm in KER_BASIS])
        dd = np.array([trip[nm][0] - trip[nm][2] for nm in KER_BASIS])
        G = np.array([[float(np.sum(Scf[a] * Scf[b]))
                       for b in KER_BASIS] for a in KER_BASIS])
        th, val = kernel_opt(c, dd, G)
        rd = theta_reads(th, trip, Scf)
        # kernel-projected S_K: the minimal source correction to the
        # standing selector that zeroes the commutator element
        eK = np.zeros(len(KER_BASIS))
        eK[0] = 1.0
        thg = eK - (c[0] / max(float(c @ c), 1e-300)) * c
        ng = math.sqrt(max(float(thg @ G @ thg), 1e-300))
        thg = thg / ng
        V = np.array([Scf[nm].ravel() for nm in KER_BASIS])
        sv = np.linalg.svd(V, compute_uv=False)
        gev = np.linalg.eigvalsh(G)
        ker[x] = {"c": c, "d": dd, "G": G, "trip": trip, "Scf": Scf,
                  "theta": th, "val": val, "read": rd, "dim": d,
                  "sv": sv, "gev": gev, "thg": thg}
        print("  x=%-2d |c| %.3e rank(c) %d | in-sample kernel-opt: "
              "s01 %.1e split %.3e split_rel %.3f pos %s ov0 %.4f "
              "phi %.1e" % (x, float(np.linalg.norm(c)),
                            1 if np.linalg.norm(c) > 0 else 0,
                            rd["s01"], rd["split"], rd["split_rel"],
                            rd["pos"], rd["ov0"], rd["phi"]),
              flush=True)
        print("       c = %s" % ["%+.2e" % t for t in c])
        print("       d = %s" % ["%+.2e" % t for t in dd])
        print("       theta* = %s" % ["%+.3f" % t for t in th])
        print("       family sv (eff. rank): %s"
              % ["%.1e" % t for t in sv])
        print("       G spectrum: [%.1e .. %.1e]"
              % (float(gev[0]), float(gev[-1])))
        # rank-1 ratio table (annihilator-scalar pattern)
        rats = []
        for nm in RANK1_SET:
            s00, s01, _s11 = trip[nm]
            rats.append("%s:%+.3e" % (nm, s01 / max(s00, 1e-300)))
        print("       rank-1 ratios s01/s00 (v1/v0 coupling): %s"
              % ", ".join(rats))
    okc = all(float(np.linalg.norm(ker[x]["c"])) > 0 for x in ker)
    check("G61-kernel-dim", okc,
          "c != 0 at every rung => the commutator kernel has codim "
          "EXACTLY 1 (dim 11) in the 12-op family; |c| = %s"
          % ["x%d:%.1e" % (x, float(np.linalg.norm(ker[x]["c"])))
             for x in sorted(ker)])
    ok62 = all(abs(ker[x]["read"]["s01"])
               <= 1e-8 * max(float(np.linalg.norm(ker[x]["theta"]))
                             * float(np.linalg.norm(ker[x]["c"])),
                             1e-300)
               for x in ker)
    check("G62-kernel-maxsplit-insample", ok62,
          "in-sample kernel-opt selector: s01(theta*) == 0 to f64 "
          "(rel <= 1e-8) and max split %s with split_rel %s -- the "
          "kernel contains cluster-splitting selectors at EVERY rung "
          "(in-sample = Connes-informed, typed)"
          % (["x%d:%.2e" % (x, ker[x]["val"]) for x in sorted(ker)],
             ["x%d:%.3f" % (x, ker[x]["read"]["split_rel"])
              for x in sorted(ker)]))
    # freeze at the gate rungs
    trans_rows = []
    beats = None
    if all(x in ker for x in gate_x):
        t5 = ker[gate_x[0]]["theta"]
        t8 = ker[gate_x[1]]["theta"]
        sgn = 1.0 if float(np.dot(t5, t8)) >= 0 else -1.0
        cosg = abs(float(np.dot(t5, t8))
                   / (np.linalg.norm(t5) * np.linalg.norm(t8)))
        th_f = t5 / np.linalg.norm(t5) + sgn * t8 / np.linalg.norm(t8)
        th_f = th_f / np.linalg.norm(th_f)
        frozen = cosg >= THETA_FREEZE_COS
        if not frozen:
            th_f = t8 / np.linalg.norm(t8)
        # orientation at the gate rungs
        ors = [(theta_reads(th_f, ker[x]["trip"], ker[x]["Scf"])
                ["branch"],
                theta_reads(th_f, ker[x]["trip"], ker[x]["Scf"])
                ["pos"]) for x in gate_x]
        or_ok = ors[0] == ors[1]
        check("G63-theta-freeze", True,
              "gate-rung kernel directions cos = %.4f (freeze bar "
              "%.2f) => %s; orientation %s/%s %s"
              % (cosg, THETA_FREEZE_COS,
                 "FROZEN(mean)" if frozen else
                 "UNSTABLE-AT-GATE (theta*(8) tested as disclosed "
                 "secondary)", ors[0][0], ors[0][1],
                 "stable" if or_ok else "UNSTABLE"))
        br_f, pos_f = ors[1]
        # secondary frozen candidate: kernel-projected S_K
        g5 = ker[gate_x[0]]["thg"]
        g8 = ker[gate_x[1]]["thg"]
        sgg = 1.0 if float(np.dot(g5, g8)) >= 0 else -1.0
        cosgg = abs(float(np.dot(g5, g8))
                    / (np.linalg.norm(g5) * np.linalg.norm(g8)))
        th_g = g5 / np.linalg.norm(g5) + sgg * g8 / np.linalg.norm(g8)
        th_g = th_g / np.linalg.norm(th_g)
        if cosgg < THETA_FREEZE_COS:
            th_g = g8 / np.linalg.norm(g8)
        org = theta_reads(th_g, ker[gate_x[1]]["trip"],
                          ker[gate_x[1]]["Scf"])
        brg, posg = org["branch"], org["pos"]
        info("kernel-projected S_K: gate cos %.4f (%s); orientation "
             "%s/%s" % (cosgg, "FROZEN(mean)" if cosgg
                        >= THETA_FREEZE_COS else "gate-8 only",
                        brg, posg))
        deep_ok = []
        for x in deep_x:
            if x not in ker:
                continue
            a = theta_reads_at(th_f, ker[x]["trip"], ker[x]["Scf"],
                               br_f, pos_f)
            ag = theta_reads_at(th_g, ker[x]["trip"], ker[x]["Scf"],
                                brg, posg)
            bx = abs(SP.R124_BETA.get(x, 1e-3))
            okb = (a["phi_ach"] <= BEATS_BETA_FAC * bx
                   and a["split_rel"] >= SPLIT_BAR
                   and a["ov_dblt"] >= math.cos(ALIGN_BAR))
            okg2 = (ag["phi_ach"] <= BEATS_BETA_FAC * bx
                    and ag["split_rel"] >= SPLIT_BAR
                    and ag["ov_dblt"] >= math.cos(ALIGN_BAR))
            deep_ok.append(okb or okg2)
            trans_rows.append(
                "x%d MAXSPLIT: phi_ach %.3e (beta %.3e, bar %.1e) "
                "s01 %+.2e split %.2e split_rel %.3f ov_clu %.4f => "
                "%s | PROJ-SK: phi_ach %.3e s01 %+.2e split %.2e "
                "split_rel %.3f => %s"
                % (x, a["phi_ach"], bx, BEATS_BETA_FAC * bx,
                   a["s01"], a["split"], a["split_rel"], a["ov_clu"],
                   "BEATS" if okb else "REVERTS",
                   ag["phi_ach"], ag["s01"], ag["split"],
                   ag["split_rel"], "BEATS" if okg2 else "REVERTS"))
        beats = bool(deep_ok) and all(deep_ok)
        check("G64-kernel-transfer", True,
              "OUT-OF-SAMPLE frozen-kernel transfer (max-split theta* "
              "AND kernel-projected S_K): %s => KERNEL-%s"
              % ("; ".join(trans_rows),
                 "TRANSFERS" if beats else "REVERTS"))
        # drift + collapse law
        xs_k = sorted(ker)
        drift = []
        for a, b in zip(xs_k, xs_k[1:]):
            ca = ker[a]["c"] / np.linalg.norm(ker[a]["c"])
            cbv = ker[b]["c"] / np.linalg.norm(ker[b]["c"])
            drift.append("(%d->%d):%.4f"
                         % (a, b, abs(float(np.dot(ca, cbv)))))
        phis = []
        for x in xs_k:
            a = theta_reads_at(th_f, ker[x]["trip"], ker[x]["Scf"],
                               br_f, pos_f)
            phis.append((x, a["phi_ach"]))
        sl_ph = float("nan")
        if len(phis) >= 3:
            sl_ph = CM.ols_slope(
                [math.log10(x) for x, _p in phis],
                [math.log10(max(p, 1e-300)) for _x, p in phis])[0]
        check("G65-kernel-drift", True,
              "kernel-normal coherence |<c-hat, c-hat'>|: %s; "
              "phi_ach(theta_f) ladder %s slope %.2f vs beta "
              "(flat/frame-set): the reversion/transfer law"
              % (", ".join(drift),
                 ["x%d:%.1e" % t for t in phis], sl_ph))
        if beats:
            # screens for the winner (above-band corr at deep rungs)
            wrows = []
            for x in deep_x:
                if x not in ker:
                    continue
                r = rungs[x].rec[PIN_K[x]]
                cell = r["cell"]
                d = ker[x]["dim"]
                edge = r["K"] * math.pi / cell["a"]
                abv = gam[gam > edge][:ZAB_N]
                cbv = SP.cluster_basis_mp(cell, r["kt"])
                G = np.zeros((d, d))
                for g in abv:
                    ev = SP.ward_evec_gamma(cell, float(g))
                    ev = ev / np.linalg.norm(ev)
                    with mp.workdps(cell["dps"]):
                        cc = np.array([float(R4.mp_dot(
                            cbv["vecs"][i], CM.lift_vec(ev)))
                            for i in range(d)])
                    G += np.outer(cc, cc)
                C = sum(th_f[i] * ker[x]["Scf"][nm]
                        for i, nm in enumerate(KER_BASIS))
                G0 = G - np.trace(G) / d * np.eye(d)
                C0 = C - np.trace(C) / d * np.eye(d)
                den = np.linalg.norm(G0) * np.linalg.norm(C0)
                corr = (abs(float(np.sum(C0 * G0))) / den
                        if den > 0 else 0.0)
                wrows.append("x%d:corr %.2f" % (x, corr))
            check("G66-winner-screens", True,
                  "kernel-winner disguise screen (above-band "
                  "canonical Gram, flag %.2f): %s"
                  % (DISGUISE_CORR, ", ".join(wrows)))
        else:
            check("G66-collapse-law", True,
                  "KERNEL-REVERTS: the frozen kernel direction's "
                  "out-of-sample s01 reverts to the beta scale -- "
                  "the kernel hyperplane is doublet data (its "
                  "localization drifts with the frame/rung exactly "
                  "like beta); with the round-126 block-pencil this "
                  "closes the linear-family loophole OPERATIONALLY: "
                  "any FROZEN source-basis combination fails at "
                  "depth, and re-localizing the kernel per rung "
                  "requires the doublet = Connes-resolution "
                  "(trade-off identity, G10)")
    # trade-off audit on measured data
    devs = []
    for x in ker:
        for nm in ("S_K", "S_E4", "S_POS2"):
            s00, s01, s11 = ker[x]["trip"][nm]
            ph = phi_of(s00, s01, s11)
            if abs(ph) < 0.1 and s01 != 0.0:
                devs.append(abs(math.tan(2 * ph) * (s00 - s11)
                                / (2 * s01) - 1.0))
    check("G67-tradeoff-audit", all(t <= 1e-6 for t in devs),
          "tan(2 phi)(s00 - s11) == 2 s01 on the measured doublets "
          "(max dev %.1e)" % (max(devs) if devs else 0.0))

    # ---------------------------------------------------------- S7
    section("S7  WORLDS + CONDITIONING + TAU")
    if worlds_on:
        okw = True
        wr = []
        for wnm, x, K, dps in (("SMOOTH", 8, 34, 80),
                               ("SCRARITH", 8, 34, 80),
                               ("EPSTEIN", 8, 34, 80),
                               ("EPSTEIN", 13, 67, 120)):
            t0 = time.time()
            cw = R4.build_cell(x, kfac_for(x, K), wnm, dps,
                               want_mp=True)
            with mp.workdps(dps):
                E = cw["mpE"]
                ns = len([i for i in range(1, K)
                          if E[i] - E[0] <= mp.mpf(repr(SOFT_BAR))])
                eps = float(E[0])
            okw = okw and ns == 0
            wr.append("%s-x%d-K%d: eps %+.2e nsoft %d (%.0f s)"
                      % (wnm, x, K, eps, ns, time.time() - t0))
            del cw
        check("G70-worlds", okw,
              "ENRICHED-frame controls: %s -- nsoft == 0 in every "
              "control world: enrichment does NOT create a fake "
              "cluster; no cluster => no crossing and no kernel "
              "target: the frame schedule is world-typed (the "
              "arithmetic supplies the selection problem)"
              % "; ".join(wr))
    # conditioning at the x=5 crossing cell
    okc7 = okz7 = True
    if cross.get(5) is not None:
        cr5 = cross[5]
        r5 = rungs[5].rec[cr5["K_best"]]
        cell = r5["cell"]
        if "mpM" in cell:
            K = cell["K"]
            jstar = int(np.argmax(np.abs(r5["v0f"] * r5["v1f"])))
            with mp.workdps(cell["dps"]):
                v00 = mp.mpf(repr(float(r5["v0f"][jstar])))
                v10 = mp.mpf(repr(float(r5["v1f"][jstar])))
                gapm = cell["mpE"][1] - cell["mpE"][0]
                tgt = mp.mpf(repr(PERT_THETA_TGT))
                den = max(abs(v00 * v10), mp.mpf("1e-30"))
                delta = max(min(tgt * gapm / den, mp.mpf("1e-8")),
                            mp.mpf("1e-45"))
                Qp = cell["mpM"].copy()
                Qp[jstar, jstar] = Qp[jstar, jstar] + delta
                Ep, Vp = mp.eigsy(Qp)
                order = sorted(range(K), key=lambda i: Ep[i])
                v1p = R4.matcol(Vp, order[1], K)
                v1m = CM.lift_vec(r5["v1f"])
                if R4.mp_dot(v1p, v1m) < 0:
                    v1p = [-t for t in v1p]
                kv = CM.lift_vec(r5["kt"])
                bp = R4.mp_dot(v1p, kv)
                dbeta = float(abs(bp - mp.mpf(repr(r5["beta_raw"]))))
                theta = float(delta * v00 * v10 / gapm)
                pred = abs(theta * r5["alpha"])
            ratio = dbeta / max(pred, 1e-300)
            okc7 = COND_RATIO[0] <= ratio <= COND_RATIO[1]
            okz7 = dbeta > 0
            dflip = abs(cr5["betac"]) * r5["gap"] \
                / max(abs(float(v00 * v10)) * r5["alpha"], 1e-300)
            check("G71-conditioning-at-crossing", okc7 and okz7,
                  "x=5 crossing cell K=%d: delta %.2e -> dbeta %.3e "
                  "vs 2x2 law %.3e (ratio %.2f, strictly nonzero): "
                  "beta at the crossing keeps the inverse-Connes "
                  "condition number" % (cr5["K_best"], float(delta),
                                        dbeta, pred, ratio))
            check("G72-flip-budget", True,
                  "delta_flip ~= |betac*| gap / (alpha |v00 v10|) = "
                  "%.2e at x=5: an operator perturbation of this "
                  "size moves the crossing by one step -- the "
                  "crossing LOCATION is exact-arithmetic data with "
                  "inverse-Connes conditioning (source data is "
                  "exact, so predictability is not excluded; "
                  "certification at depth still costs the gap "
                  "digits)" % dflip)
    # tau screens
    if not smoke:
        tsx = [x for x in (5, 8, 13, 18) if x in rungs
               and cross.get(x) is not None]
        lg = [math.log10(rungs[x].rec[PIN_K[x]]["gap"]) for x in tsx]
        rows = []
        for nm, vals in (
                ("matched-floor",
                 [abs(rungs[x].rec[MATCH20_K[x]]["beta"])
                  for x in tsx]),
                ("crossing-floor", [cross[x]["betac"] for x in tsx]),
                ("step", [cross[x]["step"] for x in tsx])):
            sl = CM.ols_slope(lg, [math.log10(max(v, 1e-300))
                                   for v in vals])[0] \
                if len(tsx) >= 3 else float("nan")
            bandv = ("PASS" if abs(sl) <= TAU_PASS else
                     ("RELOCATION" if abs(sl) >= TAU_RELOC else "MID"))
            rows.append("%s: %.4f [%s]" % (nm, sl, bandv))
        check("G73-tau-screens", True,
              "slopes log10(quantity) vs log10(gap): %s -- ~0 means "
              "the schedule floors do NOT ride the Connes scale "
              "(they are frame data); >= %.2f would relocate the "
              "problem into the frame dial" % ("; ".join(rows),
                                               TAU_RELOC))

    # ---------------------------------------------------------- S8
    section("S8  MIN-CUT")
    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = CM.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "LANEACONV"): 1,
                ("LANEACONV", "R4HYP"): INF})
    f_ext = CM.maxflow(dict(ext), "UNC", "RH")
    check("G80-mincut", f_base == 4 and f_ext == 5,
          "flows UNC->RH: base %d, extended %d -- the schedule and "
          "kernel outcomes are MEAS data ON the LANEACONV omega edge; "
          "no capacity change, census {MEAS, OMEGA-POS} cardinality 4 "
          "unchanged" % (f_base, f_ext))

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = []
    if not smoke:
        verdicts.append("FLIP(%s)" % "; ".join(flip_rows))
        verdicts.append("FLOOR-LAW-%s(slope %.3f)"
                        % ("CONTINUES" if cont else "BREAKS", slope20))
        verdicts.append("CROSSING-FLOOR(betac* slope %.3f, step slope "
                        "%.3f)" % (sl_cf, sl_st))
        if pred_ok is not None:
            verdicts.append("CROSSING-%s"
                            % ("SOURCE-PREDICTABLE" if pred_ok
                               else "CONNES-PINNED"))
        verdicts.append("APPROXIMANT(%s; OMEGA-ABSORBED)"
                        % ("; ".join(apx_rows) if apx_rows else "n/a"))
        if beats is not None:
            verdicts.append("KERNEL-%s(%s)"
                            % ("TRANSFERS" if beats else "REVERTS",
                               "; ".join(trans_rows)))
        up1 = bool(pred_ok)
        up2 = bool(beats)
        if up1 or up2:
            verdicts.append("FRAMESCHEDULE-UPGRADE(%s%s%s)"
                            % ("L1-crossing" if up1 else "",
                               "+" if up1 and up2 else "",
                               "L2-kernel" if up2 else ""))
        else:
            verdicts.append("FRAMESCHEDULE-COMPOSITE-NOGO(both "
                            "levers Connes-pinned)")
        verdicts.append("MINCUT(4 base / 5 ext, census {MEAS, "
                        "OMEGA-POS} unchanged)")
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc_, _d in CHECKS if okc_)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc_, _ in CHECKS if not okc_]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
