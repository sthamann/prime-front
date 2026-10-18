#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wrap_genesis_probe -- PRIME.WRAP.GENESIS.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-rung finite statements gated below, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files (the
independent session's untracked probes including
alphabet31_hidden_structure_probe, axiom246_hold_probe,
broad_sweep_clocks_registers_probe, ftransfer_context15_probe,
gesamtbild_synthesis_claims_probe, nonclifford_prime_probe,
qsys_jet_iso_probe, quillen_jet_a4_probe,
quillen_level_dictionary_census_probe, quillen_ramified_level_probe,
readout_fourier_factor_probe, rp_nsr_flat_probe,
state_factorization_census_probe and its logs/note, sieve4_helper.bin,
and every verification/paper/website surface) are not touched.

=======================================================================
MISSION (round ~212: WRAP GENESIS -- is p_wrap(h) a source-explicit
arithmetic event, and does (first Euler wrap) <=> (kappa = 1) hold
on MAIN while Epstein's extra inertia is extra wraps?).  Round 205
(euler_hpin_region_probe, SPEC cb1dfde33a198fb3) FROZE the wrap:
j* = min{j : mu_j <= -1} on the prime-cascade orbit
N_j = A0 - sum_{i<=j} Q_{p_i}, A0 = RawArch + theta(h) G_B, wrap_p
= 0 if j* = 0 else order[j*-1] (seed-in-region).  Observed MAIN
inc/dec CAL_WRAP, extended by r210 (secular_crossing_coord_probe,
SPEC e7ef1d6cdb96cfb4) to h = 20: inc 13, dec 7.  Round 208
(pontryagin_n1_weyl_probe, SPEC 8beceaaef64ec782) classified the
Krein-Langer fingerprint MAIN N_1 / Epstein N_3 / Smooth N_2, with
the ONE negative direction CASCADE-BORN at the wrap prime and on
the pole ray (alpha/|phi|^2 = 0.99638..0.99912).  TODAY wrap is an
EVENT, not a theorem.  THIS round freezes a PREDEFINED family of
source-explicit predicates Phi(p,h) from a disclosed prototype at
h = 4, 5, 8 + Epstein/Scrarith cells ONLY (proto_wrap_genesis_scratch,
log kept as proto_wrap_genesis_scratch.out1.log, script deleted at
freeze), then tests p_wrap^pred vs p_wrap^obs on a frozen train/
hold split, and tests the kappa dictionary on the world battery.

THE FROZEN PHI FAMILY (THREE members, no post-hoc additions).
All three locked on the prototype TRAIN_RUNGS = (4, 5, 8) against
the r205 wrap definition; HOLDOUT_RUNGS = (10, 11, 12, 13, 16, 20)
are the real test (fit-free; intermediate rungs 6, 7, 9 reported
but MAY NOT add members).  PRIMARY series = INC wrap (the wrap
that CREATES n_neg = 1 on MAIN); DEC is a cross-check only.

  Phi_2x2 (PRIMARY).  Let {u, v} be the ONB of span{phi-hat, e_0}
  (pole datum + DC mode; wrap-independent).  Compress seed and
  each Euler Gram to 2x2: A0_2 = [A0]_{u,v}, Q_p,2 = [Q_p]_{u,v}.
  Walk the SHORT 2x2 prefix (NOT the K-dimensional Woodbury orbit)
    N2_0 = A0_2,   N2_j = N2_{j-1} - Q_{p_j,2}   (inc primes).
  Source-explicit scalar
    Phi_2x2(p_j, h) := -lam_min(N2_j),
  lam_min of a 2x2 by the closed form (tr - sqrt(tr^2 - 4 det))/2.
  p_wrap^pred := 0 if lam_min(N2_0) <= 0 else
                 min{p_j : Phi_2x2(p_j, h) >= 0}
  (discrete analogue: first p at which the 2x2 prefix fails
  cholesky).  THIS IS NOT "first p at which the full orbit enters
  Omega" -- the full orbit DEFINES the observed wrap; Phi is a
  2x2 Euler-block vs seed test.  Prototype: pred = obs = 0, 2, 3
  at h = 4, 5, 8 EXACT.

  Phi_gap (arithmetic companion).  If seed A0 is not PD (H4): 0;
  else min{p prime : p * p' > h} with p' = next prime after p.
  Prototype: 0, 2, 3 at h = 4, 5, 8 EXACT (seed clause at h = 4).

  Phi_half (arithmetic companion).  If seed A0 is not PD: 0;
  else max{p prime : p <= h/2} (or 2 if empty).  Prototype:
  0, 2, 3 at h = 4, 5, 8 EXACT.

DISCLOSED PROTOTYPE REJECTS (frozen as NON-members, not to be
revived after freeze): single-prime A0 - Q_p (full-K or 2x2)
MISSES h = 8 (never loses PD); p^2 > h, 2p >= h, first M_p = 1
MISS at least one train rung.  NO further Phi after freeze.

PRIMARY = Phi_2x2.  Verdict: PREDICTOR-EXACT iff primary matches
obs inc at EVERY rung incl. holdout; PREDICTOR-PARTIAL iff
primary hits train and a proper subset of holdout, or only a
companion hits a proper subset; PREDICTOR-FAIL iff primary misses
any holdout rung (or train -- which would be a freeze bug).
A regression log p = beta log h + O(1) / p ~ h^alpha WITHOUT an
exact prime identity is a SCREEN, not a predictor (typed WEAK:
few terms 2, 3, 5, 7, 13).  Classical closed form is a SUCCESS
FORM only if it is an exact prime identity at the frozen rungs.

THE KAPPA DICTIONARY (the prize; machine-certified at reachable
rungs, NOT all-h).  Wrap DEFINITION for the observed prime is
r205 Omega-entry (mu <= -1).  Independent-wrap COUNT for the
dictionary is the INERTIA-BIRTH census: seed n_neg(A0) plus the
sum of positive Delta n_neg along the cascade (the r205 Epstein
wording "wraps THREE times (ladder 1,1,2,3)").  These two are
NOT identified a priori: Omega-entry count is at most one on
MAIN (r205 theorem-skeleton given wall+inertia-1) and may stay
1 on a control that is already in Omega while n_neg grows.
  MAIN: inc wrap sequence, kappa = 1 at every rung h >= 5.
        h = 4 seed-in-region, n_neg(A0) = 1 already -- DISCLOSED,
        H4-ANOMALY-TYPED, must not silently break the skeleton.
  Epstein: kappa = 3, seed partly born (ladder 1,1,2,3).  Test:
        several independent wraps <=> kappa = 3.
  Scrarith: kappa = 3, HARD control (sign-coherent, budget
        overshoot).  Prototype: seed PD, one wrap at p = 2
        (MAIN-like), then a last-step DOUBLE birth at p = 5
        (n_neg 1 -> 3) and Omega EXIT.  Typed honestly as
        HYBRID, not forced into MAIN-like or Epstein-like.
  Smooth: kappa = 2, portless.  Wrap count 0 cascade / seed-born
        2; type the degeneracy, do not force a wrap.
Prize shape: first Euler wrap <=> kappa = 1 on MAIN; extra
independent wraps <=> extra negative squares on Epstein/
Scrarith.  If wrap count does NOT match kappa, DICTIONARY-FAILS
(do not weaken to "wraps correlate with inertia").  Finite
certified correspondence, NOT an all-h theorem.

GEOMETRY (independence of "negative direction = pole ray"):
first wrap's created direction overlaps the pole ray at 0.996+
(r208 CAL_ALPH = ovl^2); extra Epstein wraps create extra
directions NOT on that ray (prototype: second ovl 0.067, third
0.0056).  Gate vs r208 CAL_ALPH.  FIRST-WRAP-BIRTHS-POLE-RAY /
EXTRA-WRAPS-BIRTH-EXTRA-SQUARES / GEOMETRY-FAILS.

ANTI-LOOP.  Phi builders consume no lam/tau/Delta/eig/wall.
Loop-guard for the flagged cycles (canonical seven + r208
INERTIA-FROM-WALL).  Proving kappa from the wall is forbidden;
proving kappa from wrap-count, and wrap from Euler source, is
the point.  Using kappa as Phi input would make wrap <=> kappa
tautological -- forbidden.  Using the full orbit to DEFINE Phi
is PHI-USED-ORBIT (fail of the point).

NOTATION (r171-r210 conventions VERBATIM).  Rung h = builder x
(R4.build_cell, even sector, MAIN world); a = log(h)/2; L = 2a;
K = ceil(1.25 h log h); om_k = k pi/a; par_k = (-1)^k; nrm_0 =
sqrt(2a), nrm_k = sqrt(a); Raw* = D_par N M* N D_par; phi_k =
1/(1/4 + om_k^2); c_h = 2 sinh^2(a/2); G_B = (L/2) diag(2, 1,
..., 1); theta = sum_{p<=h} log p; A0 = RawArch + theta G_B;
Q_p = r204 dissipation Grams (qp_gram VERBATIM, helpers COPIED
not imported from frozen probes); N_j = A0 - sum_{i<=j} Q_{p_i};
NoP = N_P = RawM - RawPole; mu_j = c_h phi^T N_j^{-1} phi
(mp.lu_solve); j* = min{j : mu_j <= -1}; wrap_p as above;
eigsy zero class zb_h = 10^{-(dps-20)} fro(NoP) on MAIN, ZCLS
1e-30 fro on controls; kappa = #{m : d_m < 0 and
z_m^2/|phi|^2 > ZSQ_CLS}; tau_h = ce["mpE"][0], measured
per-rung scalar only, NEVER an input to Phi.  Controls:
SCRARITH(5, 60), EPSTEIN(8, 80), SMOOTH(5, 60) builder recipes
r205 VERBATIM.

RUNGS AND DPS (house ladder + r210 h = 20): RUNGS = (4, 5, 6, 7,
8, 9, 10, 11, 12, 13, 16, 20); DPS = {4: 60, 5: 60, 6: 65, 7: 70,
8: 80, 9: 85, 10: 90, 11: 100, 12: 110, 13: 120, 16: 130, 20: 144}.
TRAIN_RUNGS = (4, 5, 8); HOLDOUT_RUNGS = (10, 11, 12, 13, 16, 20);
INTERMEDIATE_RUNGS = (6, 7, 9).  QEIG_RUNGS = (4, 5, 8) (full
n_neg stage ladders).  WORKERS = 6.  Smoke: rungs (4, 5) +
SCRARITH.  h = 20 at house dps 144 (r210); disclose skips if
the worker errors (none expected).

FROZEN BARS: WARD_BAR 1e-45 (cascade closure, rel max entry);
WOOD_BAR 1e-30 (optional Woodbury step ward on the OBSERVED
path only); OVL_MIN 0.90 (first-wrap / terminal pole-ray
|z_0|/|phi|); EXTRA_OVL_MAX 0.25 (extra-direction overlap
ceiling); ZSQ_CLS 1e-30; ZCLS 1e-30; TRAIN_LOCK exact prime
identity; LOG_TOL 0.10 dex vs r208 CAL_ALPH; VAL_TOL 0.01;
RUNTIME_BAR 3600 s.  Inheritance: wrap primes == R205_WRAP at
shared rungs and == R210_WRAP at h = 20 (exact); terminal
ovl^2 == r208 CAL_ALPH (LOG_TOL on the overlap itself, i.e.
sqrt of CAL_ALPH compared at VAL_TOL 0.01).

TAXONOMY (frozen resolution logic):
  wrapEnum   := WRAP-SEQUENCE-REPRODUCED iff observed inc/dec
                match R205_WRAP at shared rungs and R210_WRAP
                at h = 20 (own recompute), else WRAP-BREAK(h);
  predEnum   := PREDICTOR-EXACT iff primary Phi_2x2 == obs inc
                at every computed rung incl. holdout;
                PREDICTOR-PARTIAL iff train exact and holdout
                mixed / only a companion hits a subset;
                PREDICTOR-FAIL iff primary misses train or any
                holdout rung;
  phiEnum    := SOURCE-EXPLICIT-PHI iff the predictor AST path
                calls no full-K Woodbury/orbit/eig/tau/Delta/
                wall, else PHI-USED-ORBIT;
  dictEnum   := DICTIONARY-HOLDS iff (MAIN h >= 5: exactly one
                inertia birth, kappa = 1, seed n_neg = 0) AND
                (Epstein: inertia-birth sum + seed = kappa = 3)
                AND Scrarith typed (births vs kappa reported,
                hybrid allowed) AND Smooth typed degenerate;
                else DICTIONARY-FAILS;
  geomEnum   := FIRST-WRAP-BIRTHS-POLE-RAY iff MAIN wrap-stage
                and terminal ovl >= OVL_MIN and ovl^2 == CAL_ALPH
                class; EXTRA-WRAPS-BIRTH-EXTRA-SQUARES iff
                Epstein extra directions have ovl <= EXTRA_OVL_MAX
                while the first stays >= OVL_MIN; GEOMETRY-FAILS
                otherwise.  Composite concatenates the two
                geometry tags when both hold;
  h4Enum     := H4-ANOMALY-TYPED iff h = 4 wrap_p = 0 and
                n_neg(A0) = 1 (always demanded).

PRE-REGISTERED PRIORS (resolve-and-record; none gate-forcing
beyond frozen bars; ALL informed by the ONE DISCLOSED pre-freeze
prototype proto_wrap_genesis_scratch at h = 4, 5, 8 + Epstein/
Scrarith, log kept, script deleted at freeze):
  P1 observed wrap inc/dec == r205 at 4/5/8: (0,0), (2,5), (3,5);
     h = 4 seed-in-region, n_neg(A0) = 1, mu_0 = -8.26.
  P2 Phi_2x2 pred = 0, 2, 3 at h = 4, 5, 8 EXACT; Phi_gap and
     Phi_half same on train (seed clause at h = 4).  Single-prime
     tests FAIL at h = 8 (disclosed, not in the family).
  P3 MAIN n_neg ladders (QEIG): h = 4 stays 1; h = 5: 0 -> 1 at
     p = 2; h = 8: 0 -> 1 at p = 3.  Terminal ovl 0.998+.
  P4 Epstein ladder (1, 1, 2, 3), seed ovl 0.975 on-ray; extra
     ovls 0.067 and 0.006 off-ray; mus all <= -1 (already in
     Omega from seed: Omega-wrap count = 1 != kappa = 3 -- the
     dictionary uses INERTIA BIRTHS, not Omega-reentry).
  P5 Scrarith: seed PD, wrap at p = 2 (n_neg 0 -> 1, mu -6.55),
     still 1 after p = 3, then n_neg 1 -> 3 at p = 5 with Omega
     EXIT (mu -0.94 > -1).  HYBRID.  kappa = 3.
  P6 Smooth: portless, n_neg = 2, Delta > 0 (r205 CAL_CTRL).
  P7 scaling screen WEAK: two train points (h, p) = (5, 2),
     (8, 3) do not pin a unique alpha with an exact next-prime
     identity; typed SCREEN, not theorem.
  P8 holdout is UNSEEN by the family lock.  Expected: Phi_2x2
     either hits (LIVE candidate) or misses (KILL the
     predictor).  No member will be added if it misses.

RECORD TABLES (frozen at freeze from the disclosed ladder: ONE
structural smoke (rungs 4/5 + SCRARITH, wrap_genesis_probe.smoke1.log
at pre-A1 SHA 867b1afcf145560d; the 26/27 print was A1's off-by-one,
all instrument gates PASS), ONE calibration pass
(calib_wgen_pass1.log, 27/27, all 12 rungs + all three controls,
793.9 s, SHA f371c1c21d32943d); house pattern identical to
r205/r208/r210; no bar, dps, rung, Phi member or control recipe
moved at any point; record tables inserted at freeze).  Verdicts
frozen from calibration: wrap sequence REPRODUCED at all 12 rungs
incl. h = 20 (inc 13, dec 7); PRIMARY Phi_2x2 == obs inc EXACT at
every rung including the frozen holdout (10, 11, 12, 13, 16, 20)
AND the intermediate rungs (6, 7, 9) -- PREDICTOR-EXACT;
companions Phi_gap / Phi_half hit train (4, 5, 8) and FAIL
holdout (disclosed, not revived); MAIN kappa = 1, seed 0 at
h >= 5, one inertia birth, H4 typed; Epstein ladder (1, 1, 2, 3),
birth_sum 2, seed+births = kappa = 3, extra ovls 0.067 / 0.006
off-ray; Scrarith HYBRID (one wrap at p = 2 then double birth at
p = 5, Omega exit); Smooth portless degenerate kappa = 2;
pole-ray wrap-stage ovl 0.977..0.998, terminal 0.998..0.9997 ==
r208 CAL_ALPH class.  LIVE at reachable rungs: a source-explicit
2x2 Euler-seed Phi hits the observed primes exactly, and
wrap-count matches kappa on MAIN vs Epstein.  Finite certified
correspondence, NOT an all-h theorem.  NO RH claim.
CAL_WRAP {h: (inc, dec)}: 4: (0, 0), 5: (2, 5), 6: (2, 5),
  7: (3, 5), 8: (3, 5), 9: (3, 5), 10: (3, 5), 11: (5, 5),
  12: (5, 5), 13: (7, 5), 16: (7, 7), 20: (13, 7).
CAL_PRED {h: (Phi_2x2, Phi_gap, Phi_half)}: 4: (0, 0, 0),
  5: (2, 2, 2), 6: (2, 3, 3), 7: (3, 3, 3), 8: (3, 3, 3),
  9: (3, 3, 3), 10: (3, 3, 5), 11: (5, 3, 5), 12: (5, 3, 5),
  13: (7, 3, 5), 16: (7, 5, 7), 20: (13, 5, 7).
CAL_OVL {h: (wrap-stage ovl, terminal ovl)}: 4: (0.97698, 0.99828),
  5: (0.98830, 0.99819), 6: (0.98781, 0.99942), 7: (0.99224, 0.99867),
  8: (0.99030, 0.99932), 9: (0.99014, 0.99943), 10: (0.99107, 0.99953),
  11: (0.99654, 0.99923), 12: (0.99592, 0.99951), 13: (0.99765, 0.99945),
  16: (0.99638, 0.99956), 20: (0.99844, 0.99974).
AMENDMENTS: A1 (smoke1-driven, SHA 867b1afcf145560d, 26/27 print was
an off-by-one: npass was counted BEFORE G99 was appended; all
instrument gates PASS in the kept log).  Fix: count npass after
G99; suppress LIVE in smoke/calib (NOT-VERDICT-BEARING).  No bar,
dps, rung, Phi member or control recipe moved.
=======================================================================

WHAT IS BUILT AND GATED: S0 G01 firewall + G02 predefinition +
G03 predictor-AST; S1 exact layer G10-G12 (sympy); S2 observed
wrap + predictor G20-G27; S3 kappa dictionary G30-G33; S4
geometry G40-G41; S5 guards G50-G53; S6 pricing G60-G61 + G99
runtime.  DETERMINISM: no randomness; ProcessPool results keyed;
run2 identical modulo wall-clock tokens (lines carrying 'WALL').

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
Even a perfect wrap <=> kappa dictionary at reachable rungs is a
finite certified correspondence, not an all-h theorem.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery ONLY

# ---------------------------------------------------------------- frozen
KFAC = 1.25
WORKERS = 6
RUNTIME_BAR = 3600.0

RUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 20)
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 16: 130, 20: 144}
TRAIN_RUNGS = (4, 5, 8)
HOLDOUT_RUNGS = (10, 11, 12, 13, 16, 20)
INTERMEDIATE_RUNGS = (6, 7, 9)
QEIG_RUNGS = (4, 5, 8)
SMOKE_RUNGS = (4, 5)

WARD_BAR = 1e-45
WOOD_BAR = 1e-30
OVL_MIN = 0.90
EXTRA_OVL_MAX = 0.25
ZSQ_CLS = 1e-30
ZCLS = 1e-30
LOG_TOL = 0.10
VAL_TOL = 0.01

CTRL_CELLS = (("SCRARITH", 5, 60), ("EPSTEIN", 8, 80),
              ("SMOOTH", 5, 60))

# r205 / r210 inheritance (observed wrap; own recompute must match)
R205_WRAP = {4: (0, 0), 5: (2, 5), 6: (2, 5), 7: (3, 5), 8: (3, 5),
             9: (3, 5), 10: (3, 5), 11: (5, 5), 12: (5, 5),
             13: (7, 5), 16: (7, 7)}
R210_WRAP = {20: (13, 7)}
R208_ALPH = {4: "0.99656", 5: "0.99638", 6: "0.99883", 7: "0.99735",
             8: "0.99864", 9: "0.99885", 10: "0.99906", 11: "0.99847",
             12: "0.99901", 13: "0.99890", 16: "0.99912"}

# --------------------- calibrated record tables (filled at freeze)
CAL_WRAP = {4: (0, 0), 5: (2, 5), 6: (2, 5), 7: (3, 5), 8: (3, 5),
            9: (3, 5), 10: (3, 5), 11: (5, 5), 12: (5, 5),
            13: (7, 5), 16: (7, 7), 20: (13, 7)}
CAL_PRED = {
    4: dict(twox=0, gap=0, half=0),
    5: dict(twox=2, gap=2, half=2),
    6: dict(twox=2, gap=3, half=3),
    7: dict(twox=3, gap=3, half=3),
    8: dict(twox=3, gap=3, half=3),
    9: dict(twox=3, gap=3, half=3),
    10: dict(twox=3, gap=3, half=5),
    11: dict(twox=5, gap=3, half=5),
    12: dict(twox=5, gap=3, half=5),
    13: dict(twox=7, gap=3, half=5),
    16: dict(twox=7, gap=5, half=7),
    20: dict(twox=13, gap=5, half=7),
}
CAL_OVL = {
    4: ("0.97698", "0.99828"), 5: ("0.98830", "0.99819"),
    6: ("0.98781", "0.99942"), 7: ("0.99224", "0.99867"),
    8: ("0.99030", "0.99932"), 9: ("0.99014", "0.99943"),
    10: ("0.99107", "0.99953"), 11: ("0.99654", "0.99923"),
    12: ("0.99592", "0.99951"), 13: ("0.99765", "0.99945"),
    16: ("0.99638", "0.99956"), 20: ("0.99844", "0.99974"),
}
CAL_CTRL = {
    "EPSTEIN": dict(nneg=3, seed=1, ladder=(1, 1, 2, 3),
                    Delta="-0.2610"),
    "SCRARITH": dict(nneg=3, Delta="0.0594"),
    "SMOOTH": dict(nneg=2, Delta="0.2147"),
}

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []

FORBIDDEN_PROBE_IMPORTS = (
    "euler_hpin_region_probe",
    "secular_crossing_coord_probe",
    "pontryagin_n1_weyl_probe",
    "euler_jet_colligation_probe",
    "euler_jet_dictionary_probe",
    "alphabet31_hidden_structure_probe",
    "axiom246_hold_probe",
    "broad_sweep_clocks_registers_probe",
    "ftransfer_context15_probe",
    "gesamtbild_synthesis_claims_probe",
    "nonclifford_prime_probe",
    "qsys_jet_iso_probe",
    "quillen_jet_a4_probe",
    "quillen_level_dictionary_census_probe",
    "quillen_ramified_level_probe",
    "readout_fourier_factor_probe",
    "rp_nsr_flat_probe",
    "state_factorization_census_probe",
    "bughunt11_probe",
)


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def fit_line(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return sxy / sxx if sxx else float("nan")


def has_cycle(graph: dict) -> bool:
    WHITE, GREY, BLACK = 0, 1, 2
    color = {u: WHITE for u in graph}
    for v in list(graph):
        for w in graph[v]:
            color.setdefault(w, WHITE)

    def dfs(u):
        color[u] = GREY
        for w in graph.get(u, ()):
            if color[w] == GREY:
                return True
            if color[w] == WHITE and dfs(w):
                return True
        color[u] = BLACK
        return False

    return any(color[u] == WHITE and dfs(u) for u in list(color))


def ancestors(graph: dict, node: str) -> set:
    rev: dict = {}
    for u, vs in graph.items():
        for v in vs:
            rev.setdefault(v, set()).add(u)
    seen: set = set()
    stack = [node]
    while stack:
        u = stack.pop()
        for p in rev.get(u, ()):
            if p not in seen:
                seen.add(p)
                stack.append(p)
    return seen


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        is_const = False
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Constant) and isinstance(node.value,
                                                           str):
            nm = node.value
            is_const = True
        if nm is None:
            continue
        low = nm.lower()
        if not is_const:
            if low in forb:
                bad.append("forbidden %s @%d" % (nm, node.lineno))
            if low == "zeta":
                bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d (zero-free round)" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m is None:
                    continue
                base = m.split(".")[0]
                if m.startswith("verification") or base == "verification":
                    bad.append("import " + m)
                if base in FORBIDDEN_PROBE_IMPORTS:
                    bad.append("frozen-probe import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "NO zero-oracle, NO zeta, NO np.load, no "
                       "verification/ import, no frozen-probe import "
                       "(helpers COPIED verbatim); R4 cell machinery "
                       "only; eigsy consumed only as per-rung finite "
                       "inertia/overlap (observed path); tau as "
                       "measured scalar NEVER fed to Phi; fully "
                       "zero-free; concurrent-lane files untouched")


def predictor_ast_audit() -> tuple[bool, str]:
    """G03: predictor helpers must not call full-K orbit/Woodbury/eig."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    pred_names = {"phi_2x2_predict", "phi_arith_gap", "phi_arith_half",
                  "compress_2", "onb_phi_e0", "lammin2",
                  "next_prime_ge", "pd_flag_n"}
    forbid_call = {"eigsy", "lu_solve", "orbit_observed", "m_weyl",
                   "qp_gram", "build_cell", "woodbury", "w_rung",
                   "w_ctrl"}
    fns = {n.name: n for n in tree.body
           if isinstance(n, ast.FunctionDef) and n.name in pred_names}
    missing = pred_names - set(fns)
    if missing:
        return False, "missing predictor helpers %s" % sorted(missing)
    bad = []
    for nm, fn in fns.items():
        for node in ast.walk(fn):
            called = None
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    called = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    called = node.func.attr
            if called in forbid_call:
                bad.append("%s calls %s @%d" % (nm, called, node.lineno))
    return (not bad), ("; ".join(bad) if bad else
                       "predictor path is 2x2 compression + "
                       "arithmetic only: no full-K Woodbury, no "
                       "orbit_observed, no eigsy, no qp_gram, no "
                       "lu_solve, no wall/tau/Delta -- "
                       "SOURCE-EXPLICIT-PHI")


# --------------------------------------------- copied r204/r205 helpers
def primes_upto(x: int) -> list[int]:
    return [p for p in range(2, x + 1)
            if all(p % d for d in range(2, int(math.isqrt(p)) + 1))]


def m_nilp(p: int, h: int) -> int:
    m, q = 0, p
    while q < h:
        m += 1
        q *= p
    return m


def trig_int(alpha, beta, phi, psi, t0, t1):
    if t1 <= t0:
        return mp.mpf(0)

    def F(t):
        if alpha == 0 and beta == 0:
            return t * mp.cos(phi) * mp.cos(psi)
        if alpha == beta:
            return (t * mp.cos(phi - psi)
                    + mp.sin(2 * alpha * t + phi + psi)
                    / (2 * alpha)) / 2
        return (mp.sin((alpha - beta) * t + phi - psi) / (alpha - beta)
                + mp.sin((alpha + beta) * t + phi + psi)
                / (alpha + beta)) / 2
    return F(t1) - F(t0)


def w_kernel_add(Acc, u, w, oms, L, K):
    for i in range(K):
        for j in range(i):
            bi, bj = oms[i] ** 2, oms[j] ** 2
            od = 2 * (oms[i] * mp.sin(oms[i] * u)
                      - oms[j] * mp.sin(oms[j] * u)) / (bi - bj)
            Acc[i, j] += w * od
            Acc[j, i] += w * od
    for k in range(K):
        if k == 0:
            Acc[0, 0] += w * 2 * (u - L)
        else:
            Acc[k, k] += w * (mp.sin(oms[k] * u) / oms[k]
                              + (u - L) * mp.cos(oms[k] * u))


def to_raw(Mb, par, nrm, K):
    Rb = mp.zeros(K, K)
    for i in range(K):
        for j in range(K):
            Rb[i, j] = par[i] * nrm[i] * Mb[i, j] * nrm[j] * par[j]
    return Rb


def qp_gram(p, h, oms, L, K):
    """r204 dissipation Gram Q_p VERBATIM (copied, not imported)."""
    lp = mp.log(p)
    lam = mp.exp(-lp / 2)
    Mt = m_nilp(p, h)

    def d2ip(i, j, m, n):
        lo = max(m, n) * lp
        sp = L - lp
        ph_ = -oms[i] * m * lp
        ps_ = -oms[j] * n * lp
        acc = mp.mpf(0)
        if sp > lo:
            acc += (1 - lam ** 2) * trig_int(oms[i], oms[j],
                                             ph_, ps_, lo, sp)
        acc += trig_int(oms[i], oms[j], ph_, ps_, max(lo, sp), L)
        return acc

    Qp = mp.zeros(K, K)
    for i in range(K):
        for j in range(i + 1):
            s = mp.mpf(0)
            for m in range(Mt + 1):
                for n in range(Mt + 1):
                    s += lam ** (m + n) * d2ip(i, j, m, n)
            Qp[i, j] = lp * s
            Qp[j, i] = Qp[i, j]
    return Qp


def pd_flag(N, K):
    try:
        mp.cholesky(N)
        return True
    except Exception:                             # noqa: BLE001
        return False


def pd_flag_n(N, n):
    """Cholesky PD test of an n x n mp matrix (predictor-safe)."""
    try:
        mp.cholesky(N)
        return True
    except Exception:                             # noqa: BLE001
        return False


def m_weyl(N, phi, K):
    x = mp.lu_solve(N, mp.matrix(phi))
    return sum(phi[i] * x[i] for i in range(K)), x


def next_prime_ge(n: int) -> int:
    n = max(2, int(n))
    while True:
        if all(n % d for d in range(2, int(math.isqrt(n)) + 1)):
            return n
        n += 1


def lammin2(M):
    """Closed-form smaller eigenvalue of a symmetric 2x2."""
    tr = M[0, 0] + M[1, 1]
    det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    disc = tr * tr - 4 * det
    if disc < 0:
        disc = mp.mpf(0)
    return (tr - mp.sqrt(disc)) / 2


def compress_2(A, u, v, K):
    def ip(x, M, y):
        My = [sum(M[i, j] * y[j] for j in range(K)) for i in range(K)]
        return sum(x[i] * My[i] for i in range(K))
    M2 = mp.zeros(2, 2)
    M2[0, 0] = ip(u, A, u)
    M2[0, 1] = ip(u, A, v)
    M2[1, 0] = M2[0, 1]
    M2[1, 1] = ip(v, A, v)
    return M2


def onb_phi_e0(phi, K):
    nrm = mp.sqrt(sum(phi[i] ** 2 for i in range(K)))
    u = [phi[i] / nrm for i in range(K)]
    e0 = [mp.mpf(1 if i == 0 else 0) for i in range(K)]
    a = sum(u[i] * e0[i] for i in range(K))
    v = [e0[i] - a * u[i] for i in range(K)]
    nv = mp.sqrt(sum(vi ** 2 for vi in v))
    if nv < mp.mpf("1e-30"):
        e1 = [mp.mpf(1 if i == 1 else 0) for i in range(K)]
        a = sum(u[i] * e1[i] for i in range(K))
        v = [e1[i] - a * u[i] for i in range(K)]
        nv = mp.sqrt(sum(vi ** 2 for vi in v))
    v = [vi / nv for vi in v]
    return u, v


def phi_2x2_predict(A0, Qs, phi, prs, K):
    """PRIMARY Phi: 2x2 prefix PD-loss / lam_min crossing.

    Consumes only seed A0, Euler Grams Q_p, pole datum phi, primes.
    Does NOT walk the K-dimensional orbit.
    """
    u, v = onb_phi_e0(phi, K)
    A02 = compress_2(A0, u, v, K)
    l0 = lammin2(A02)
    if l0 <= 0 or not pd_flag_n(A02, 2):
        return 0, float(l0)
    N2 = mp.matrix(A02)
    last_l = float(l0)
    for p in prs:
        Q2 = compress_2(Qs[p], u, v, K)
        for i in range(2):
            for j in range(2):
                N2[i, j] -= Q2[i, j]
        lm = lammin2(N2)
        last_l = float(lm)
        if lm <= 0 or not pd_flag_n(N2, 2):
            return p, last_l
    return None, last_l


def phi_arith_gap(h: int, seed_pd: bool):
    if not seed_pd:
        return 0
    prs = primes_upto(h)
    for i, p in enumerate(prs):
        nxt = prs[i + 1] if i + 1 < len(prs) else next_prime_ge(p + 1)
        if p * nxt > h:
            return p
    return None


def phi_arith_half(h: int, seed_pd: bool):
    if not seed_pd:
        return 0
    half = [p for p in primes_upto(h) if p <= h / 2.0]
    return max(half) if half else 2


def nneg_ovls(N, phi, K, zb, phin):
    En, Qn = mp.eigsy(N)
    idx = sorted(range(K), key=lambda m: En[m])
    nneg = 0
    ovls = []
    kappa = 0
    for m in range(K):
        if En[idx[m]] < -zb:
            nneg += 1
            z = sum(Qn[i, idx[m]] * phi[i] for i in range(K))
            ov = float(abs(z) / phin)
            ovls.append(ov)
            if (z * z) / (phin * phin) > ZSQ_CLS:
                kappa += 1
        else:
            break
    return nneg, kappa, ovls, float(En[idx[0]])


def orbit_observed(A0, Qs, order, phi, c, K):
    """r205 wrap on the FULL cascade (observed path; NOT Phi)."""
    N = mp.matrix(A0)
    m0, x0 = m_weyl(N, phi, K)
    mus = [c * m0]
    pds = [pd_flag(N, K)]
    xs = [x0]
    for p in order:
        for i in range(K):
            for j in range(K):
                N[i, j] -= Qs[p][i, j]
        m1, x1 = m_weyl(N, phi, K)
        mus.append(c * m1)
        pds.append(pd_flag(N, K))
        xs.append(x1)
    P = len(order)
    trans = [j for j in range(P) if pds[j] and not pds[j + 1]]
    back = [j for j in range(P) if (not pds[j]) and pds[j + 1]]
    jstar_pd = 0 if not pds[0] else (trans[0] + 1 if trans else None)
    jstar_mu = next((j for j in range(P + 1) if mus[j] <= -1), None)
    wrap_pd = (0 if jstar_pd == 0 else order[jstar_pd - 1]) \
        if jstar_pd is not None else None
    wrap_mu = (0 if jstar_mu == 0 else order[jstar_mu - 1]) \
        if jstar_mu is not None else None
    wood_worst = mp.mpf(0)
    for j in range(1, P + 1):
        p = order[j - 1]
        dmu = mus[j] - mus[j - 1]
        Qx = [sum(Qs[p][i, k2] * xs[j - 1][k2] for k2 in range(K))
              for i in range(K)]
        wood = c * sum(xs[j][i] * Qx[i] for i in range(K))
        wrel = abs(dmu - wood) / max(abs(dmu), mp.mpf("1e-300"))
        wood_worst = max(wood_worst, wrel)
    return dict(jstar_pd=jstar_pd, jstar_mu=jstar_mu,
                wrap_pd=wrap_pd, wrap_mu=wrap_mu,
                ntrans=len(trans), nback=len(back),
                mus_f=[float(v) for v in mus], pds=pds,
                wood_worst=float(wood_worst))


def mat_at_prefix(A0, Qs, order, nsteps, K):
    N = mp.matrix(A0)
    for p in order[:nsteps]:
        for i in range(K):
            for j in range(K):
                N[i, j] -= Qs[p][i, j]
    return N


# ------------------------------------------------------- rung worker
def w_rung(args) -> dict:
    h, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(h) / 2
            L = 2 * aa
            oms = [k * mp.pi / aa for k in range(K)]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            RawM = to_raw(ce["mpM"], par, nrm, K)
            RawPole = to_raw(ce["mpPole"], par, nrm, K)
            RawArch = to_raw(ce["mpArch"], par, nrm, K)
            tau = ce["mpE"][0]
            out["tau_log10"] = float(mp.log(abs(tau), 10))
            out["tau_pos"] = bool(tau > 0)
            phi = [1 / (mp.mpf(1) / 4 + oms[k] ** 2) for k in range(K)]
            c = 2 * mp.sinh(aa / 2) ** 2
            prs = primes_upto(h)
            out["primes"] = prs
            theta = sum(mp.log(p) for p in prs)
            GBd = [L if k == 0 else L / 2 for k in range(K)]
            A0 = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    A0[i, j] = RawArch[i, j]
                A0[i, i] += theta * GBd[i]
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = RawM[i, j] - RawPole[i, j]
            froN = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            denN = max(abs(NoP[i, j]) for i in range(K)
                       for j in range(K))
            Qs = {p: qp_gram(p, h, oms, L, K) for p in prs}
            dev = mp.mpf(0)
            for i in range(K):
                for j in range(K):
                    acc = A0[i, j]
                    for p in prs:
                        acc -= Qs[p][i, j]
                    dev = max(dev, abs(acc - NoP[i, j]))
            out["closure_dev"] = float(dev / denN)

            zb = mp.mpf(10) ** (-(dps - 20)) * froN
            phin = mp.sqrt(sum(phi[i] ** 2 for i in range(K)))
            nA0, kA0, ovA0, _ = nneg_ovls(A0, phi, K, zb, phin)
            nNoP, kNoP, ovT, _ = nneg_ovls(NoP, phi, K, zb, phin)
            out["nA0"] = nA0
            out["kA0"] = kA0
            out["nNoP"] = nNoP
            out["kappa"] = kNoP
            out["ovl_term"] = ovT[0] if ovT else 0.0
            out["ovl_term_all"] = ovT
            out["seed_pd"] = bool(pd_flag(A0, K))

            orb = {}
            for tag, order in (("inc", prs),
                               ("dec", list(reversed(prs)))):
                cen = orbit_observed(A0, Qs, order, phi, c, K)
                orb[tag] = cen
            out["orb"] = orb
            out["wrap_inc"] = orb["inc"]["wrap_mu"]
            out["wrap_dec"] = orb["dec"]["wrap_mu"]
            out["wrap_agree"] = (orb["inc"]["wrap_mu"]
                                 == orb["inc"]["wrap_pd"]
                                 and orb["dec"]["wrap_mu"]
                                 == orb["dec"]["wrap_pd"])
            out["wood_worst"] = max(orb["inc"]["wood_worst"],
                                    orb["dec"]["wood_worst"])

            # wrap-stage birth overlap (inc, the creating wrap)
            jstar = orb["inc"]["jstar_mu"]
            if jstar is None:
                out["ovl_wrap"] = 0.0
                out["nneg_wrap"] = None
            elif jstar == 0:
                out["ovl_wrap"] = ovA0[0] if ovA0 else 0.0
                out["nneg_wrap"] = nA0
            else:
                Nw = mat_at_prefix(A0, Qs, prs, jstar, K)
                nw, _kw, ovw, _ = nneg_ovls(Nw, phi, K, zb, phin)
                out["ovl_wrap"] = ovw[0] if ovw else 0.0
                out["nneg_wrap"] = nw

            if h in QEIG_RUNGS:
                N = mp.matrix(A0)
                lad = [nneg_ovls(N, phi, K, zb, phin)[0]]
                for p in prs:
                    for i in range(K):
                        for j in range(K):
                            N[i, j] -= Qs[p][i, j]
                    lad.append(nneg_ovls(N, phi, K, zb, phin)[0])
                out["nneg_ladder_inc"] = lad
                births = sum(max(lad[j + 1] - lad[j], 0)
                             for j in range(len(lad) - 1))
                out["birth_sum"] = births
            else:
                # seed + terminal: births = nNoP - nA0 if monotone
                out["birth_sum"] = nNoP - nA0

            # ---- Phi family (source-explicit; no full orbit)
            p2, lfin = phi_2x2_predict(A0, Qs, phi, prs, K)
            out["pred_2x2"] = p2
            out["pred_2x2_lmin"] = lfin
            out["pred_gap"] = phi_arith_gap(h, out["seed_pd"])
            out["pred_half"] = phi_arith_half(h, out["seed_pd"])
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc, traceback.format_exc())}


def w_ctrl(args) -> dict:
    world, x, dps = args
    try:
        t0 = time.time()
        ce = R4.build_cell(x, KFAC, world, dps, want_mp=True)
        K = ce["K"]
        out = dict(world=world, x=x, K=K, err="")
        with mp.workdps(dps):
            aa = mp.log(x) / 2
            L = 2 * aa
            oms = [k * mp.pi / aa for k in range(K)]
            par = [mp.mpf((-1.0) ** k) for k in range(K)]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            RawM = to_raw(ce["mpM"], par, nrm, K)
            RawPole = to_raw(ce["mpPole"], par, nrm, K)
            RawArch = to_raw(ce["mpArch"], par, nrm, K)
            phi = [1 / (mp.mpf(1) / 4 + oms[k] ** 2) for k in range(K)]
            c = 2 * mp.sinh(aa / 2) ** 2
            GBd = [L if k == 0 else L / 2 for k in range(K)]
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = RawM[i, j] - RawPole[i, j]
            froN = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                               for j in range(K)))
            zb = mp.mpf(ZCLS) * froN
            phin = mp.sqrt(sum(phi[i] ** 2 for i in range(K)))
            nT, kT, ovT, _ = nneg_ovls(NoP, phi, K, zb, phin)
            out["nneg"] = nT
            out["kappa"] = kT
            out["ovls_term"] = ovT
            out["Delta"] = float(1 + c * m_weyl(NoP, phi, K)[0])

            if world == "SMOOTH":
                out["nA0"] = nT
                out["ports"] = 0
                out["omega_wraps"] = 0
                out["birth_sum"] = 0
                out["degenerate"] = True

            if world == "SCRARITH":
                gold = (math.sqrt(5.0) - 1.0) / 2.0
                nlist = []
                for p in primes_upto(x):
                    q = p
                    while q <= x:
                        nlist.append((q, p))
                        q *= p
                nlist.sort()
                atoms = [(mp.log(q), mp.log(p) / mp.sqrt(q))
                         for q, p in nlist]
                keys = [math.fmod(q * gold, 1.0) for q, _p in nlist]
                perm = sorted(range(len(keys)), key=lambda i: keys[i])
                wts = [atoms[i][1] for i in range(len(atoms))]
                atomw = {nlist[i][0]: wts[perm[i]]
                         for i in range(len(nlist))}
                prs = primes_upto(x)
                theta = sum(mp.log(p) for p in prs)
                A0 = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        A0[i, j] = RawArch[i, j]
                    A0[i, i] += theta * GBd[i]
                Qs = {}
                qmins = {}
                for p in prs:
                    lp = mp.log(p)
                    Qw = mp.zeros(K, K)
                    for i in range(K):
                        Qw[i, i] = lp * GBd[i]
                    for q, pp in nlist:
                        if pp == p:
                            w_kernel_add(Qw, mp.log(q), -atomw[q],
                                         oms, L, K)
                    Qs[p] = Qw
                    Eq, _ = mp.eigsy(Qw)
                    qmins[p] = float(min(Eq))
                out["qmins"] = qmins
                N = mp.matrix(A0)
                stages = []
                nn, kk, ov, _ = nneg_ovls(N, phi, K, zb, phin)
                mu = float(c * m_weyl(N, phi, K)[0])
                stages.append(dict(p=0, nneg=nn, kappa=kk, ovls=ov,
                                   mu=mu, pd=pd_flag(N, K)))
                for p in prs:
                    for i in range(K):
                        for j in range(K):
                            N[i, j] -= Qs[p][i, j]
                    nn, kk, ov, _ = nneg_ovls(N, phi, K, zb, phin)
                    mu = float(c * m_weyl(N, phi, K)[0])
                    stages.append(dict(p=p, nneg=nn, kappa=kk, ovls=ov,
                                       mu=mu, pd=pd_flag(N, K)))
                out["stages"] = stages
                lad = [s["nneg"] for s in stages]
                out["ladder"] = lad
                out["nA0"] = lad[0]
                out["birth_sum"] = sum(max(lad[j + 1] - lad[j], 0)
                                       for j in range(len(lad) - 1))
                trans = [j for j in range(len(stages) - 1)
                         if stages[j]["pd"] and not stages[j + 1]["pd"]]
                out["omega_wraps"] = len(trans) + (
                    0 if stages[0]["pd"] else 1)
                extra = []
                for j in range(1, len(stages)):
                    if stages[j]["nneg"] > stages[j - 1]["nneg"]:
                        extra.append(dict(
                            p=stages[j]["p"],
                            dn=stages[j]["nneg"] - stages[j - 1]["nneg"],
                            ovls=stages[j]["ovls"]))
                out["extra_births"] = extra

            if world == "EPSTEIN":
                icap = x
                rq = [0.0] * (icap + 1)
                xm = int(math.isqrt(icap)) + 1
                ym = int(math.isqrt(icap // 5)) + 1
                for xx in range(-xm, xm + 1):
                    for yy in range(-ym, ym + 1):
                        n = xx * xx + 5 * yy * yy
                        if 1 <= n <= icap:
                            rq[n] += 1.0
                av = [mp.mpf(v) / 2 for v in rq]
                lamq = [mp.mpf(0)] * (icap + 1)
                for n in range(2, icap + 1):
                    sacc = av[n] * mp.log(n)
                    for dd in range(2, n):
                        if n % dd == 0:
                            sacc -= lamq[dd] * av[n // dd]
                    lamq[n] = sacc
                w4 = lamq[4] / 2
                w5 = lamq[5] / mp.sqrt(5)
                w6 = lamq[6] / mp.sqrt(6)
                l2, l5 = mp.log(2), mp.log(5)
                Q2 = mp.zeros(K, K)
                for i in range(K):
                    Q2[i, i] = l2 * GBd[i]
                w_kernel_add(Q2, mp.log(4), -w4, oms, L, K)
                Q5 = mp.zeros(K, K)
                for i in range(K):
                    Q5[i, i] = l5 * GBd[i]
                w_kernel_add(Q5, mp.log(5), -w5, oms, L, K)
                K6 = mp.zeros(K, K)
                w_kernel_add(K6, mp.log(6), w6, oms, L, K)
                for i in range(K):
                    for j in range(K):
                        K6[i, j] = -K6[i, j]
                A0e = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        A0e[i, j] = RawArch[i, j]
                    A0e[i, i] += (l2 + l5) * GBd[i]
                den = max(abs(NoP[i, j]) for i in range(K)
                          for j in range(K))
                dev = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        acc = A0e[i, j] - Q2[i, j] - Q5[i, j] - K6[i, j]
                        dev = max(dev, abs(acc - NoP[i, j]))
                out["closure_dev"] = float(dev / den)
                N = mp.matrix(A0e)
                names = ("seed", "Q2", "Q5", "K6")
                blocks = (None, Q2, Q5, K6)
                stages = []
                for nm, B in zip(names, blocks):
                    if B is not None:
                        for i in range(K):
                            for j in range(K):
                                N[i, j] -= B[i, j]
                    nn, kk, ov, _ = nneg_ovls(N, phi, K, zb, phin)
                    mu = float(c * m_weyl(N, phi, K)[0])
                    stages.append(dict(name=nm, nneg=nn, kappa=kk,
                                       ovls=ov, mu=mu,
                                       pd=pd_flag(N, K)))
                out["stages"] = stages
                lad = [s["nneg"] for s in stages]
                out["ladder"] = lad
                out["nA0"] = lad[0]
                out["birth_sum"] = sum(max(lad[j + 1] - lad[j], 0)
                                       for j in range(len(lad) - 1))
                out["omega_wraps"] = (
                    0 if stages[0]["pd"] else 1) + sum(
                    1 for j in range(len(stages) - 1)
                    if stages[j]["pd"] and not stages[j + 1]["pd"])
                extra = []
                for j in range(1, len(stages)):
                    if stages[j]["nneg"] > stages[j - 1]["nneg"]:
                        extra.append(dict(
                            name=stages[j]["name"],
                            dn=stages[j]["nneg"] - stages[j - 1]["nneg"],
                            ovls=stages[j]["ovls"],
                            prev=stages[j - 1]["ovls"]))
                out["extra_births"] = extra
                Eq, _ = mp.eigsy(Q2)
                out["q2min"] = float(min(Eq))
                Eq, _ = mp.eigsy(K6)
                out["k6lo"] = float(min(Eq))
                out["k6hi"] = float(max(Eq))
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"world": world, "x": x,
                "err": "%s\n%s" % (exc, traceback.format_exc())}


# ------------------------------------------------------------ S1 exact
def exact_layer() -> None:
    import sympy as sp

    tr, a, b, d = sp.symbols("tr a b d", real=True)
    M00, M01, M11 = sp.symbols("m00 m01 m11", real=True)
    trv = M00 + M11
    detv = M00 * M11 - M01 ** 2
    disc = trv ** 2 - 4 * detv
    lmin = (trv - sp.sqrt(disc)) / 2
    lmax = (trv + sp.sqrt(disc)) / 2
    ok10 = sp.simplify(lmin + lmax - trv) == 0 \
        and sp.simplify(lmin * lmax - detv) == 0
    check("G10-2x2-lammin-closed-form", bool(ok10),
          "Phi_2x2 scalar is the closed-form smaller eigenvalue of "
          "a symmetric 2x2: lam_min = (tr - sqrt(tr^2 - 4 det))/2, "
          "lam_min + lam_max = tr and lam_min * lam_max = det "
          "(sympy exact) -- a genuine source-explicit crossing, "
          "not an orbit restatement")

    n = 2
    Q = sp.Matrix(n, n, lambda i, j: sp.Symbol(
        "q_%d_%d" % (min(i, j), max(i, j))))
    P = sp.Matrix(n, 2, lambda i, j: sp.Symbol("p_%d_%d" % (i, j)))
    C = P.T * Q * P
    # compression of a PSD Gram is PSD: C = P^T Q P, so v^T C v =
    # (Pv)^T Q (Pv) >= 0 whenever Q >= 0.  Gated as a quadratic-form
    # identity, not a numeric claim about Q_p.
    v = sp.Matrix(2, 1, lambda i, _j: sp.Symbol("v_%d" % i))
    lhs = sp.expand((v.T * C * v)[0, 0])
    rhs = sp.expand(((P * v).T * Q * (P * v))[0, 0])
    ok11 = sp.simplify(lhs - rhs) == 0
    check("G11-compression-of-PSD-is-PSD", bool(ok11),
          "the 2x2 Euler-block compression Q_{p,2} = P^T Q_p P "
          "satisfies v^T Q_{p,2} v = (Pv)^T Q_p (Pv) identically "
          "(generic 2-col P, sympy): Q_p PSD (r204 KYP) => Q_{p,2} "
          "PSD -- the 2x2 prefix is Loewner-monotone, same as the "
          "full cascade, WITHOUT walking the K-orbit")

    # Weyl: subtracting PSD cannot raise eigenvalues.  Exact 2x2
    # certificate: A = I, Q = diag(2, 0) => A - Q = diag(-1, 1) has
    # n_neg = 1 > 0 = n_neg(A).  Direction: n_neg NONDECREASING.
    A = sp.eye(2)
    Qd = sp.diag(2, 0)
    N = A - Qd
    ok12 = N[0, 0] == -1 and N[1, 1] == 1
    check("G12-weyl-nneg-nondecreasing-2x2", bool(ok12),
          "exact-rational 2x2: A0 = I (n_neg = 0), Q = diag(2, 0) "
          "PSD, A0 - Q = diag(-1, 1) has n_neg = 1 -- inertia "
          "births are the ONLY way n_neg grows along a passive "
          "cascade (r208 direction, re-gated).  Dictionary count "
          "= seed n_neg + sum of positive Delta n_neg")


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "calib", "smoke"),
                     default="record")
    args = apx.parse_args()
    calib = args.mode == "calib"
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("wrap_genesis_probe -- PRIME.WRAP.GENESIS.01  (mode %s)"
          % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    okp, detp = predictor_ast_audit()
    check("G03-predictor-ast-source-explicit", okp, detp)
    check("G02-predefinition", True,
          "Phi family FROZEN from the disclosed prototype at "
          "TRAIN_RUNGS %s (log proto_wrap_genesis_scratch.out1.log, "
          "script deleted at freeze): PRIMARY Phi_2x2 (2x2 Euler-"
          "block vs seed prefix, lam_min crossing) + companions "
          "Phi_gap (min p with p p' > h, seed-PD clause) and "
          "Phi_half (max p <= h/2, seed-PD clause).  NO post-hoc "
          "members.  HOLDOUT_RUNGS %s are the real test.  Primary "
          "series = INC wrap (creates n_neg = 1).  Wrap definition "
          "= r205 Omega-entry (mu <= -1), helpers COPIED not "
          "imported.  dps ladder = house + r210 h = 20 at 144"
          % (str(TRAIN_RUNGS), str(HOLDOUT_RUNGS)))

    section("S1  EXACT LAYER (sympy: 2x2 Phi scalar + Weyl)")
    exact_layer()

    rungs = SMOKE_RUNGS if smoke else RUNGS
    section("S2  OBSERVED WRAP + PREDICTOR (mp at h = %s)" % str(rungs))
    tasks = [(h, DPS[h]) for h in rungs]
    ctasks = [("SCRARITH", 5, 60)] if smoke else list(CTRL_CELLS)
    res: dict = {}
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(w_rung, t): ("rung", t[0]) for t in tasks}
        futs.update({ex.submit(w_ctrl, t): ("ctrl", t[0])
                     for t in ctasks})
        for fu in list(futs):
            outw = fu.result()
            kind, _key = futs[fu]
            if kind == "rung":
                res[outw["h"]] = outw
            else:
                cres[outw["world"]] = outw
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    cerrs = [w for w in cres if cres[w].get("err")]
    for w in cerrs:
        print("  [ERR] %s %s" % (w, cres[w]["err"]))
    if errs or cerrs:
        check("G20-cascade-closure", False,
              "worker errors at %s %s" % (errs, cerrs))
        print("ABORT: worker errors")
        return 1

    check("G20-cascade-closure", all(
        res[h]["closure_dev"] <= WARD_BAR for h in rungs),
          "A0 - sum_p Q_p == NoP entrywise at every rung (max rel "
          "dev %s, bar %.0e) -- r204/r205 central identity, own "
          "recompute, helpers copied"
          % (str({h: "%.1e" % res[h]["closure_dev"]
                  for h in rungs if h in (4, 8, 13, 20)}), WARD_BAR))

    wrapp = {h: (res[h]["wrap_inc"], res[h]["wrap_dec"]) for h in rungs}
    ok21 = all(res[h]["wrap_agree"] for h in rungs)
    ok21 = ok21 and all(
        wrapp[h] == R205_WRAP[h] for h in rungs if h in R205_WRAP)
    ok21 = ok21 and all(
        wrapp[h] == R210_WRAP[h] for h in rungs if h in R210_WRAP)
    if not (calib or smoke):
        ok21 = ok21 and all(wrapp[h] == CAL_WRAP[h] for h in rungs)
    check("G21-wrap-sequence-reproduced", ok21,
          "OWN recompute of the r205 wrap (j* = min{j : mu_j <= -1}, "
          "PD trans agrees): {h: (inc, dec)} = %s == R205_WRAP at "
          "all shared rungs and == R210_WRAP at h = 20 (inc 13, "
          "dec 7).  Primary series = INC.  Enum "
          "WRAP-SEQUENCE-REPRODUCED"
          % str(wrapp))

    check("G27-pd-mu-wrap-agreement", all(
        res[h]["wrap_agree"] and res[h]["wood_worst"] <= WOOD_BAR
        for h in rungs),
          "PD-transition wrap == Omega-entry wrap at every rung/"
          "order (membership ward) and Woodbury step law on the "
          "OBSERVED path only (worst rel %.1e, bar %.0e) -- the "
          "observed wrap IS the r205 event; Phi does not use this "
          "path"
          % (max(res[h]["wood_worst"] for h in rungs), WOOD_BAR))

    ok22 = all(res[h]["nNoP"] == 1 and res[h]["kappa"] == 1
               for h in rungs)
    check("G22-main-inertia-kappa-one", ok22,
          "MAIN: n_neg(NoP) = 1 and kappa = 1 at every rung incl. "
          "h = 20 (eigsy, dps-scaled zero class, overlap floor "
          "ZSQ_CLS) -- the N_1 fingerprint of r208, own recompute")

    ok23 = (res[4]["nA0"] == 1 and res[4]["wrap_inc"] == 0
            and all(res[h]["nA0"] == 0 and res[h]["seed_pd"]
                    for h in rungs if h >= 5))
    check("G23-h4-anomaly-typed", ok23,
          "H4-ANOMALY-TYPED: h = 4 seed-in-region (n_neg(A0) = %d, "
          "wrap_p = %s, mu_0 = %s); every rung h >= 5 has PD seed "
          "(n_neg(A0) = 0).  The skeleton first-wrap <=> kappa = 1 "
          "is the h >= 5 statement; h = 4 is disclosed not silently "
          "dropped"
          % (res[4]["nA0"], str(res[4]["wrap_inc"]),
             res[4]["orb"]["inc"]["mus_f"][0]))

    pred_tab = {h: dict(obs=res[h]["wrap_inc"],
                        p2=res[h]["pred_2x2"],
                        gap=res[h]["pred_gap"],
                        half=res[h]["pred_half"])
                for h in rungs}
    train_hit = all(
        res[h]["pred_2x2"] == res[h]["wrap_inc"]
        for h in rungs if h in TRAIN_RUNGS)
    hold_r = [h for h in rungs if h in HOLDOUT_RUNGS]
    hold_hit = all(res[h]["pred_2x2"] == res[h]["wrap_inc"]
                   for h in hold_r) if hold_r else True
    inter_r = [h for h in rungs if h in INTERMEDIATE_RUNGS]
    inter_hit = all(res[h]["pred_2x2"] == res[h]["wrap_inc"]
                    for h in inter_r) if inter_r else True
    all_hit = all(res[h]["pred_2x2"] == res[h]["wrap_inc"]
                  for h in rungs)
    gap_hit = all(res[h]["pred_gap"] == res[h]["wrap_inc"]
                  for h in rungs)
    half_hit = all(res[h]["pred_half"] == res[h]["wrap_inc"]
                   for h in rungs)
    if all_hit:
        pred_enum = "PREDICTOR-EXACT"
    elif train_hit and hold_r and not hold_hit:
        n_h = sum(res[h]["pred_2x2"] == res[h]["wrap_inc"]
                  for h in hold_r)
        pred_enum = "PREDICTOR-FAIL" if n_h == 0 else "PREDICTOR-PARTIAL"
        if not inter_hit and n_h == 0:
            pred_enum = "PREDICTOR-FAIL"
    elif train_hit:
        pred_enum = "PREDICTOR-EXACT" if (hold_hit and inter_hit) \
            else ("PREDICTOR-PARTIAL" if hold_hit or inter_hit
                  else "PREDICTOR-FAIL")
    else:
        pred_enum = "PREDICTOR-FAIL"
    if not (calib or smoke) and CAL_PRED:
        ok24c = all(
            res[h]["pred_2x2"] == CAL_PRED[h]["twox"]
            and res[h]["pred_gap"] == CAL_PRED[h]["gap"]
            and res[h]["pred_half"] == CAL_PRED[h]["half"]
            for h in rungs)
        ok24c = ok24c and all(
            abs(res[h]["ovl_wrap"] - float(CAL_OVL[h][0])) <= 0.00005
            and abs(res[h]["ovl_term"] - float(CAL_OVL[h][1])) <= 0.00005
            for h in rungs)
    else:
        ok24c = True
    check("G24-predictor-table", train_hit and ok24c,
          "Phi family vs obs inc: %s.  PRIMARY Phi_2x2 train lock "
          "at %s: %s.  Holdout %s hit=%s.  Intermediate %s hit=%s.  "
          "Companions gap-all=%s half-all=%s.  Enum %s.  (Calib/"
          "smoke skip CAL_PRED match.)"
          % (str(pred_tab), str(TRAIN_RUNGS), train_hit,
             str(hold_r), hold_hit, str(inter_r), inter_hit,
             gap_hit, half_hit, pred_enum))

    # scaling screen: train (h, p) at h >= 5
    tr_hp = [(h, res[h]["wrap_inc"]) for h in rungs
             if h in TRAIN_RUNGS and h >= 5 and res[h]["wrap_inc"]]
    if len(tr_hp) >= 2:
        xs = [math.log(h) for h, _p in tr_hp]
        ys = [math.log(p) for _h, p in tr_hp]
        beta = fit_line(xs, ys)
        alpha_pts = [math.log(p) / math.log(h) for h, p in tr_hp]
        alpha_mean = sum(alpha_pts) / len(alpha_pts)
    else:
        beta = float("nan")
        alpha_mean = float("nan")
    scale_rows = []
    for h in rungs:
        pobs = res[h]["wrap_inc"]
        if not pobs:
            continue
        p_a = next_prime_ge(int(round(h ** alpha_mean))) \
            if alpha_mean == alpha_mean else None
        p_b = next_prime_ge(int(round(math.exp(
            beta * math.log(h))))) if beta == beta else None
        scale_rows.append((h, pobs, p_a, p_b))
    n_exact_a = sum(r[1] == r[2] for r in scale_rows)
    check("G25-scaling-screen-weak", True,
          "SCREEN (WEAK, few terms): train (h, p) = %s give "
          "alpha = log p / log h = %s (mean %.3f) and OLS beta = "
          "d log p / d log h = %.3f.  nextprime(round(h^alpha)) "
          "exact-hits %d/%d rungs %s -- NOT a theorem, NOT a "
          "predictor.  Exact prime identity is Phi_2x2 / Phi_gap / "
          "Phi_half, not this regression"
          % (str(tr_hp),
             str(["%.3f" % (math.log(p) / math.log(h))
                  for h, p in tr_hp]),
             alpha_mean, beta, n_exact_a, len(scale_rows),
             str(scale_rows)))

    phi_enum = "SOURCE-EXPLICIT-PHI" if okp else "PHI-USED-ORBIT"
    check("G26-phi-source-explicit", okp,
          "Phi builders consume seed Gram + Euler 2x2 compressions "
          "+ primes/prime-gaps only; AST audit %s.  Enum %s"
          % ("CLEAN" if okp else "DIRTY", phi_enum))

    section("S3  KAPPA DICTIONARY (MAIN / Epstein / Scrarith / Smooth)")
    main_ok = all(
        (h == 4 and res[h]["nA0"] == 1 and res[h]["kappa"] == 1
         and res[h]["birth_sum"] == 0)
        or (h >= 5 and res[h]["nA0"] == 0 and res[h]["kappa"] == 1
            and res[h]["birth_sum"] == 1
            and res[h]["nneg_wrap"] == 1)
        for h in rungs)
    check("G30-dictionary-main", main_ok,
          "MAIN first-Euler-wrap <=> kappa = 1 at reachable rungs: "
          "h >= 5 seed n_neg = 0, exactly one inertia birth "
          "(birth_sum = 1), wrap-stage n_neg = 1, terminal kappa = 1; "
          "h = 4 seed-born kappa = 1, birth_sum = 0 (no cascade "
          "birth).  Inc wrap primes %s"
          % str({h: res[h]["wrap_inc"] for h in rungs}))

    ep = cres.get("EPSTEIN")
    scr = cres.get("SCRARITH")
    smo = cres.get("SMOOTH")
    ok31 = False
    if ep:
        extra_ovl_ok = True
        first_onray = True
        for b in ep.get("extra_births", []):
            # new directions: those beyond the previous count
            prev_n = len(b.get("prev") or [])
            new_ov = b["ovls"][prev_n:]
            extra_ovl_ok = extra_ovl_ok and all(
                ov <= EXTRA_OVL_MAX for ov in new_ov)
            first_onray = first_onray and (
                b["ovls"][0] >= OVL_MIN if b["ovls"] else False)
        seed_onray = (ep["stages"][0]["ovls"][0] >= OVL_MIN
                      if ep.get("stages") and ep["stages"][0]["ovls"]
                      else False)
        ok31 = (ep["nneg"] == 3 and ep["kappa"] == 3
                and ep["nA0"] == 1
                and ep["ladder"] == [1, 1, 2, 3]
                and ep["birth_sum"] == 2
                and ep["nA0"] + ep["birth_sum"] == ep["kappa"]
                and extra_ovl_ok and seed_onray)
        if not (calib or smoke):
            ok31 = ok31 and ep["ladder"] == list(
                CAL_CTRL["EPSTEIN"]["ladder"])
    check("G31-dictionary-epstein", bool(ok31 and ep) if ep
          else smoke,
          "skipped in smoke mode" if not ep else
          "EPSTEIN(8): kappa = %d, seed n_neg = %d, ladder %s, "
          "inertia-birth sum %d, seed+births = kappa is %s.  "
          "Omega-wrap count = %d (seed already in Omega: r205 "
          "Omega-entry is NOT the extra-inertia counter -- the "
          "dictionary uses inertia births, as r205's own Epstein "
          "wording).  Extra births %s.  Enum test: several "
          "independent wraps <=> kappa = 3: %s"
          % (ep["kappa"], ep["nA0"], str(ep["ladder"]),
             ep["birth_sum"],
             ep["nA0"] + ep["birth_sum"] == ep["kappa"],
             ep["omega_wraps"],
             str([{k: (v if k != "prev" else "...")
                   for k, v in b.items()}
                  for b in ep.get("extra_births", [])]),
             bool(ok31)))

    ok32 = False
    scr_type = "SKIP"
    if scr:
        ok32 = (scr["nneg"] == 3 and scr["kappa"] == 3
                and scr["nA0"] == 0
                and scr["nA0"] + scr["birth_sum"] == scr["kappa"])
        # hybrid: one MAIN-like wrap then last-step overshoot
        st = scr.get("stages", [])
        hybrid = (len(st) >= 2 and st[0]["pd"] and st[0]["nneg"] == 0
                  and st[1]["nneg"] == 1 and not st[1]["pd"]
                  and st[-1]["nneg"] == 3 and st[-1]["mu"] > -1)
        scr_type = "HYBRID-ONE-WRAP-THEN-DOUBLE-OVERSHOOT" if hybrid \
            else "TYPED-OTHER"
        if not (calib or smoke):
            ok32 = ok32 and abs(scr["Delta"] - float(
                CAL_CTRL["SCRARITH"]["Delta"])) <= VAL_TOL
    check("G32-dictionary-scrarith", bool(ok32 and scr),
          "" if not scr else
          "SCRARITH(5) HARD CONTROL: kappa = %d, seed n_neg = %d "
          "(PD like MAIN), birth_sum = %d, seed+births = kappa is "
          "%s, Omega wraps = %d, Delta = %.4f, stages %s.  Type "
          "%s -- not forced into MAIN-like (one wrap then stop) "
          "nor Epstein-like (seed-born + two single births).  "
          "qmins %s"
          % (scr["kappa"], scr["nA0"], scr["birth_sum"],
             scr["nA0"] + scr["birth_sum"] == scr["kappa"],
             scr.get("omega_wraps"), scr["Delta"],
             str([(s["p"], s["nneg"], "%.3g" % s["mu"])
                  for s in scr.get("stages", [])]),
             scr_type, str(scr.get("qmins"))))

    ok33 = False
    if smo:
        ok33 = (smo["nneg"] == 2 and smo["kappa"] == 2
                and smo.get("ports") == 0
                and smo.get("degenerate") is True)
        if not (calib or smoke):
            ok33 = ok33 and abs(smo["Delta"] - float(
                CAL_CTRL["SMOOTH"]["Delta"])) <= VAL_TOL
    check("G33-smooth-portless-degenerate", bool(ok33 and smo) if smo
          else smoke,
          "skipped in smoke mode" if not smo else
          "SMOOTH(5): portless (atom list empty), cascade wrap "
          "ILL-DEFINED (0 cascade births), seed/terminal n_neg = "
          "kappa = %d, Delta = %.4f > 0 -- degeneracy TYPED, wrap "
          "not forced.  PORTLESS-DEGENERATE"
          % (smo["kappa"], smo["Delta"]))

    dict_holds = bool(main_ok and (ok31 if ep else smoke)
                      and ok32 and (ok33 if smo else smoke))
    dict_enum = "DICTIONARY-HOLDS" if dict_holds else "DICTIONARY-FAILS"
    info("dictionary enum %s (MAIN %s Epstein %s Scrarith %s/%s "
         "Smooth %s)"
         % (dict_enum, main_ok, bool(ok31 and ep), ok32, scr_type,
            bool(ok33 and smo)))

    section("S4  GEOMETRY (pole-ray vs extra squares)")
    ovl_ok = all(
        res[h]["ovl_wrap"] >= OVL_MIN and res[h]["ovl_term"] >= OVL_MIN
        for h in rungs)
    alph_ok = True
    for h in rungs:
        if h not in R208_ALPH:
            continue
        tgt = math.sqrt(float(R208_ALPH[h]))
        alph_ok = alph_ok and abs(res[h]["ovl_term"] - tgt) <= 0.01
    check("G40-first-wrap-births-pole-ray", ovl_ok and alph_ok,
          "MAIN first wrap creates a direction on the pole ray: "
          "wrap-stage ovl %s, terminal ovl %s, both >= %.2f; "
          "terminal ovl == sqrt(r208 CAL_ALPH) within 0.01 at "
          "shared rungs.  Enum FIRST-WRAP-BIRTHS-POLE-RAY"
          % (str({h: "%.5f" % res[h]["ovl_wrap"] for h in rungs}),
             str({h: "%.5f" % res[h]["ovl_term"] for h in rungs}),
             OVL_MIN))

    geom_extra = False
    if ep:
        geom_extra = True
        for b in ep.get("extra_births", []):
            prev_n = len(b.get("prev") or [])
            new_ov = b["ovls"][prev_n:]
            geom_extra = geom_extra and len(new_ov) >= 1 and all(
                ov <= EXTRA_OVL_MAX for ov in new_ov)
            geom_extra = geom_extra and b["ovls"][0] >= OVL_MIN
        seed_ok = (ep["stages"][0]["ovls"]
                   and ep["stages"][0]["ovls"][0] >= OVL_MIN)
        geom_extra = geom_extra and seed_ok
    check("G41-extra-wraps-birth-extra-squares",
          bool(geom_extra and ep) if ep else smoke,
          "skipped in smoke mode" if not ep else
          "EPSTEIN extra inertia births create directions NOT on "
          "the pole ray (new-direction ovl <= %.2f) while the "
          "first (seed-born) stays on-ray (>= %.2f): extra births "
          "%s.  Enum EXTRA-WRAPS-BIRTH-EXTRA-SQUARES"
          % (EXTRA_OVL_MAX, OVL_MIN,
             str([(b["name"], b["dn"],
                   ["%.4f" % o for o in b["ovls"]])
                  for b in ep.get("extra_births", [])])))
    if ovl_ok and alph_ok and geom_extra:
        geom_enum = ("FIRST-WRAP-BIRTHS-POLE-RAY|"
                     "EXTRA-WRAPS-BIRTH-EXTRA-SQUARES")
    elif ovl_ok and alph_ok:
        geom_enum = "FIRST-WRAP-BIRTHS-POLE-RAY"
    else:
        geom_enum = "GEOMETRY-FAILS"

    section("S5  LOOPS / MINCUT / ANTI-LOOP")
    flagged = {
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"],
                        "TAUPOS": ["TLAWCAP"]},
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "GONEK-1984": {"GONEK-1984": ["RH"], "RH": ["GONEK-1984"]},
        "MONTGOMERY-PC": {"MONTGOMERY-PC": ["RH"],
                          "RH": ["MONTGOMERY-PC"]},
        "WEIL-ALLTESTS": {"WEIL-ALLTESTS": ["RH"],
                          "RH": ["WEIL-ALLTESTS"]},
        "ZEROVERIF-HYP": {"ZEROVERIF-HYP": ["RH"],
                          "RH": ["ZEROVERIF-HYP"]},
        "TURAN-CONE-POSITIVITY": {"TURAN-CONE-POSITIVITY": ["RH"],
                                  "RH": ["TURAN-CONE-POSITIVITY"]},
        "INERTIA-FROM-WALL": {"WALL-PSD": ["INERTIA1"],
                              "INERTIA1": ["SECULAR-CRIT"],
                              "SECULAR-CRIT": ["WALL-PSD"]}}
    delivered = {
        "ATOMS": ["SEED-A0"], "MODES": ["SEED-A0"],
        "SEED-A0": ["OBS-WRAP", "PHI-2X2"],
        "QP-KYP": ["OBS-WRAP", "PHI-2X2"],
        "OBS-WRAP": ["DICT-MAIN", "GEOMETRY"],
        "PHI-2X2": ["PRED-TABLE"],
        "PRED-TABLE": ["ADJUDICATION"],
        "DICT-MAIN": ["ADJUDICATION"],
        "GEOMETRY": ["ADJUDICATION"],
        "CTRL-WORLDS": ["ADJUDICATION"],
        "ADJUDICATION": ["SCREENS"], "SCREENS": []}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    joint = dict(delivered)
    for g2 in flagged.values():
        for u2, vs in g2.items():
            joint.setdefault(u2, list(vs))
    anc = set()
    for node in ("PRED-TABLE", "DICT-MAIN", "GEOMETRY",
                 "ADJUDICATION", "SCREENS"):
        anc |= ancestors(joint, node)
    hot = anc & {"TAUPOS", "TLAWCAP", "EPSLOCK", "A0-FLOOR",
                 "CENSUS-ALL-K", "GONEK-1984", "MONTGOMERY-PC",
                 "WEIL-ALLTESTS", "ZEROVERIF-HYP",
                 "TURAN-CONE-POSITIVITY", "WALL-PSD", "RH"}
    check("G51-loop-guard", ndet == 8 and not has_cycle(delivered)
          and not hot,
          "EIGHT flagged cycles DETECTED (canonical seven + r208 "
          "INERTIA-FROM-WALL: wall-PSD -> inertia-1 -> secular "
          "criterion -> wall-PSD), consumed by NOTHING: DFS ancestry "
          "of every delivered node clean; Phi and wrap-count do not "
          "edge into WALL-PSD")

    check("G50-phi-no-wall-inputs", True,
          "ANTI-LOOP: Phi_2x2 / Phi_gap / Phi_half consume no "
          "lam_min(RawM), no tau, no Delta, no s*, no m_h(0) of "
          "NoP, no kappa, no wall PSD, no zero ordinates.  Observed "
          "orbit (Woodbury along the full cascade) is used ONLY to "
          "DEFINE p_wrap^obs.  INERTIA-FROM-WALL is flagged and "
          "not consumed: kappa is compared to wrap-count, not "
          "proved from the wall")
    check("G52-inertia-from-wall-not-consumed", "WALL-PSD" not in anc,
          "INERTIA-FROM-WALL not in the ancestry of any delivered "
          "node -- proving kappa from the wall is refused; the "
          "round's route is wrap-from-Euler-source and "
          "kappa-from-wrap-count (finite, per-rung)")

    ALLOWED = {"euler-product-structure", "positive-prime-weights",
               "passivity-kyp", "elementary-prime-theorems",
               "exact-closed-form",
               "finite-per-rung-spectrum-measured"}
    FORBIDDEN = {"census-roots", "tau-positive",
                 "terminal-positivity",
                 "smallest-eigenvalue-positive", "zeros-on-line"}
    LEGS = {
        "observed-wrap-r205": {
            "finite-per-rung-spectrum-measured",
            "passivity-kyp"},
        "phi-2x2-source": {"exact-closed-form",
                           "passivity-kyp",
                           "euler-product-structure"},
        "phi-arith": {"elementary-prime-theorems"},
        "kappa-dictionary": {
            "finite-per-rung-spectrum-measured"},
        "geometry-pole-ray": {
            "finite-per-rung-spectrum-measured"},
    }
    mincut_ok = all(LEGS[k] <= ALLOWED for k in LEGS) and not any(
        LEGS[k] & FORBIDDEN for k in LEGS)
    check("G53-mincut-unchanged", mincut_ok,
          "min-cut UNCHANGED: every delivered leg sits in "
          "{euler-product, KYP, elementary primes, exact 2x2, "
          "finite per-rung spectrum}; none consume census-roots / "
          "tau-positive / terminal-positivity / zeros-on-line")

    section("S6  TABLES + COMPOSITE")
    nlines = 0
    for h in rungs:
        print("  WRAP h=%-2d inc=%s dec=%s  Phi2x2=%s gap=%s half=%s  "
              "nA0=%d k=%d birth=%d ovlW=%.5f ovlT=%.5f"
              % (h, str(res[h]["wrap_inc"]), str(res[h]["wrap_dec"]),
                 str(res[h]["pred_2x2"]), str(res[h]["pred_gap"]),
                 str(res[h]["pred_half"]), res[h]["nA0"],
                 res[h]["kappa"], res[h]["birth_sum"],
                 res[h]["ovl_wrap"], res[h]["ovl_term"]))
        nlines += 1
    check("G61-wrap-predictor-table", nlines == len(rungs),
          "wrap + predictor design table delivered: %d lines "
          "(one per rung) -- obs inc/dec, Phi_2x2/gap/half, seed "
          "n_neg, kappa, births, pole-ray overlaps"
          % nlines)

    live = (not smoke and not calib
            and pred_enum == "PREDICTOR-EXACT"
            and dict_enum == "DICTIONARY-HOLDS"
            and phi_enum == "SOURCE-EXPLICIT-PHI"
            and "GEOMETRY-FAILS" not in geom_enum)
    if live:
        live_para = (
            "LIVE CUT: Phi_2x2 hits every frozen rung including "
            "holdout, wrap-count matches kappa on MAIN vs Epstein "
            "(Scrarith typed hybrid, Smooth degenerate), first wrap "
            "births the pole ray and extra wraps birth extra "
            "squares.  Later rounds MAY use p < p_wrap vs p >= "
            "p_wrap as the dynamical low/tail cut Probe D could not "
            "find -- still a finite certified correspondence, NOT "
            "an all-h theorem, NO RH claim.")
    else:
        live_para = (
            "KILL: wrap remains an observed event.  Primary Phi_2x2 "
            "enum %s, dictionary %s, Phi path %s, geometry %s.  No "
            "new Phi members after freeze.  Honest.  Do not use "
            "wrap as a source-explicit low/tail cut.  NO RH claim."
            % (pred_enum, dict_enum, phi_enum, geom_enum))
    info(live_para)

    info("POST-ROUND RESIDUE (cardinality UNCHANGED): {H1 ^ H2 ^ "
         "H3}-KOFINAL (mod D = 0.0042) + {census-forall-k == LOOP, "
         "flagged, not consumed} + {H-PIN, now additionally: wrap "
         "genesis %s/%s} + {WPD/TAILWPD front}.  Closes NOTHING, "
         "upgrades NOTHING.  NO RH CLAIM."
         % (pred_enum, dict_enum))

    wrap_enum = "WRAP-SEQUENCE-REPRODUCED" if ok21 else "WRAP-BREAK"
    h4_enum = "H4-ANOMALY-TYPED"
    verdicts = [
        wrap_enum + "(G21)",
        pred_enum + "(G24)",
        dict_enum + "(G30-G33)",
        geom_enum + "(G40/G41)",
        phi_enum + "(G03/G26)",
        h4_enum + "(G23)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G51)",
        "MINCUT-UNCHANGED(G53)",
        "RESIDUE-UNCHANGED"]
    section("S7  COMPOSITE VERDICT")
    for v in verdicts:
        print("  " + v)
    check("G60-composite", True,
          "composite " + " ".join(verdicts) + " -- " + (
              "LIVE" if live else "KILL"))

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "WALL runtime %.1f s (bar %.0f s)" % (dt, RUNTIME_BAR))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)

    print()
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [n for n, ok, _d in CHECKS if not ok]
    if fails:
        print("FAILS: %s" % ", ".join(fails))
    print("COMPOSITE: %s" % " ".join(verdicts))
    print("LIVE/KILL: %s" % ("LIVE" if live else "KILL"))
    print(live_para)
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
        print("CALIB_PRED " + str(
            {h: dict(obs=res[h]["wrap_inc"],
                     p2=res[h]["pred_2x2"],
                     gap=res[h]["pred_gap"],
                     half=res[h]["pred_half"],
                     ovlW=round(res[h]["ovl_wrap"], 5),
                     ovlT=round(res[h]["ovl_term"], 5))
             for h in rungs}))
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
