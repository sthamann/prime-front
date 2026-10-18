#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bughunt4_probe -- PRIME.BUGHUNT4.01

FROZEN SPEC (2026-08-17).  EXPLORATION ONLY.  Adversarial audit of the
discovery rounds 131-148 corpus (probes l1_weyllaw / wpd_proof /
dominance_proof / frameschedule / hpin_floor / spacing_remainder /
epslock / counteq_seedball / qsubgap / jetlock_bandmass /
pfloor_suscap2 / tlawcap_suscap2r / toproot_tailvis / suscap_master /
fullgap_onset (F-layer + ONSETCAP rescue addendum) / fullgap_spectrum
/ adjugate_logmaster; notes CDXXXIII-CDLII).  This probe writes
NOTHING but stdout, reads the frozen corpus READ-ONLY (sources +
run*.log evidence files + next.txt + the X5 zero cache in a ward_
function), imports NO frozen probe (every recompute below is an
independent implementation), and makes NO RH CLAIM in either
direction.  Every confirmed finding carries at least one falsifiable
gate.

METHOD (bughunt I/II/III standard): (B1) the load-bearing round-131
pair re-derived INDEPENDENTLY -- the secular identity det(Meta - z)
= -z C(z^2)/A_0 on an own exact-rational rank-one instance (K = 6,
dim 11, Fraction Gaussian elimination at 13 interpolation points, no
sympy), and the GW pinning tau = 2 sum |E_N(gamma)|^2 via an OWN
Weil-form build at x = 3 (pole/prime/archimedean kernels re-derived
from the classical Riemann-Weil explicit formula: the digamma
u-space kernel -(gamma_E + log pi) psi(0) + 2 int [psi(0) e^{-2w} -
psi(w) e^{-w/2}]/(1 - e^{-2w}) dw was re-derived here and CONFIRMS
the round-114 builder's kernel including the log1p tail; own
closed-form autocorrelations; own Lambda atoms; own eigensolve; own
zero-side sum over the full 7000-zero cache with declared slop and
own boundary-jet envelope tail); (B2) the AST-firewall claim
attacked by an own CALL-GRAPH REACHABILITY scan of the builder
(radius4_an_probe / semilocal_realroot_limit_probe): zeta owned only
by audit_*, np.load only by ward_*, and NOTHING zero-fed reachable
from build_cell / c01_target / hp_zero_data / trig_profile; (B3) the
certified tail machinery re-derived: the HSW G(T) closed form
verified against an independent mp.quad evaluation of the Stieltjes
IBP integral and against cache partial sums, and the HSW22 Cor. 1.2
/ BW25 published / PT21 citation pins verified against the published
sources (HSW 0.1038/0.2573/9.3675 Cor. 1.2 confirmed; BW25
0.10076/0.24460/8.08344 published + the v1-abstract 8.08292
discrepancy disclosed by r144 is real); (B4) the theorem layer of
rounds 132-148 re-proven by hand and re-gated on own exact
adversarial instances (Theorems M/E/T/C/A incl. stray/empty-ball
refusals and the Theorem-A closed forms x_0 = 121 / x_0(BW) = 112 /
MRB(144) / MRB(1e6) recomputed with own code; D1/D2/J3 sum rules
exact-rational sympy-free; W1 defect identity + pinch, W2 loop both
ways, X3 interlacing representation, Y4 chain identity, U1 two-sided
gap, W3/Y2 interlacing + tightness transfer, O1a cell budget with
exact integer recount, O2a Markov visibility, O3a/O3b assembly +
currency invariance, T1 window counting against the cache);
(B5) the Landau pins recomputed from the cache at x = 5/13/18;
(B6) the min-cut flow numbers re-verified with an OWN Dinic
implementation on re-encoded frozen graphs (r131 4/5/5, r141
4/5/5/6, r148 4/5/5/7); (B7) rescue provenance: SPEC_SHA of every
round probe recomputed and matched against its frozen logs
(including the disclosed 3eca7075 -> 82f845b8 addendum move),
run-of-record diffs re-computed (F-layer run1 vs run2 and rescue
run3 vs run4 timing-only; fullgap_spectrum run1 vs run2 raw diff ==
5 pairs, timing-only), and the wall-clock story (run2 restart at
15:00) checked against mtime - runtime; (B8) cross-round residue
bookkeeping CDXLIV -> CDLII, delta_1-lock quintuple consistency,
note-numeral integrity, tau/A_0/FULLGAP string continuity.

=======================================================================
FINDINGS LEDGER (the deliverable; severity frozen; gates named)
=======================================================================
BH4-F1 [MINOR][residue-implication-gap]  Round 141's assembled
  residue (probe info line + note CDXLV) states "QSUBGAP <==
  EPSLOCK-consumed + SUSCAP2R (PFLOOR REMOVED)" and freezes
  "RESIDUUM = {TOPROOT, TAILVIS, TLAWCAP, SUSCAP2R} + dense-a +
  a-extension + window-a" -- OMITTING the delta_1-floor that
  r141's OWN exact inequality gap >= 1/(s + 1/delta_1) (its G16,
  quoted verbatim in CDXLV) makes unavoidable: the secular root
  always satisfies g < delta_1, so s <= poly alone CANNOT give
  QSUBGAP.  Machine witness (exact rationals, G12 here): the
  2-level family rho2 = 1/(1+d1), et_1^2 = d1/(1+d1) has s == 1
  EXACTLY for every d1 while g = d1/(1+d1) -> 0: SUSCAP2R holds
  with constant 1 and QSUBGAP fails as d1 -> 0.  The corpus
  CAUGHT THIS ITSELF one round later -- r142 THEOREM W2 states
  "QSUBGAP-lambda-uniform <==> SUSCAP2R AND DELTA1FLOOR ... the
  r139-r141 chain has LOOPED on this leg", r144's A8 exposure
  repeats it against the owner's three-integrand M' ("the fourth
  summand 1/delta_1 is REQUIRED"), and every residue statement
  from CDXLVI on carries DELTA1FLOOR -- but CDXLV itself was never
  amended and its residue set is incomplete as frozen.  No r141
  theorem (V1/V2/V3) is touched; no verdict flips.  GATE: G12
  (exact witness + grep conjunction on r141/CDXLV/r142/r144).
BH4-F2 [MINOR][rescue-evidence-retention]  Note CDLI claims for
  round 147 "Record-Run 2053.2 s + deterministischer Re-Run
  identisch modulo Timing, Log ...adjugate_logmaster_probe.
  frozen.log" -- but the corpus keeps only ONE run:
  adjugate_logmaster_probe.frozen.log contains exactly one GATES
  line (30/30, 2053.2 s) and no second adjugate log exists, so
  the deterministic-re-run claim is UNVERIFIABLE from the frozen
  evidence.  Every other rescue lane kept both runs (CDXLIX/CDL/
  CDLII: run1+run2 and run3+run4, all re-diffed here and confirmed
  timing-only with exactly the claimed raw pair counts).  The
  record run itself is intact (SPEC_SHA matches the current file;
  mtime - runtime consistent).  Recommended correction: either
  retain the re-run log or restate CDLI as record-run-only.
  GATE: G13 (log census + one-GATES-line + claim grep + the other
  lanes' diffs verified).
BH4-F3 [NOTE][lock-label-drift]  Round 146's spec (L8) attributes
  "lock ratio FULLGAP/y_t = 3.64/2.39/3.31/2.58/2.84" to r143 --
  but r143 defined the SAME quintuple as delta_1/y_t (the
  ZONE-KILLED first excited eigenvalue), a different object a
  priori (delta_1 >= FULLGAP, r142 W3).  Harmless in substance:
  r146's own L4 measures q_1 == lambda_1 to rel 7.7e-6 (x=5)
  .. 3.9e-17 (x=13), the r143 delta_1 strings (2.2255e5/9.9512e5/
  1.0619e7) and the r146 FULLGAP strings (2.225493e5/9.951249e5/
  1.061906e7) agree to <= 4e-5 rel (gated), and CDL discloses the
  identification ("zwei unabhaengige Instrumente, ein Spektrum")
  with the exact reciprocal cross-replication against CDXLIX
  (1/3.6444 = 0.274 etc., gated here).  Label precision only.
  GATE: G14 (string parse + rel-dev + reciprocal identity).
BH4-F4 [NOTE][firewall-gate-scope]  Round 131's verdict
  "NOT-TRANSCRIPTION-BY-INPUT (builder consumes Lambda/arch/pole
  only, AST-gated)" cites its G01 -- but G01 scans ONLY
  l1_weyllaw_probe.py itself, not the imported builder modules
  where the construction actually lives (the same gate-scope
  pattern recurs in the whole r132-r148 family).  The CLAIM is
  TRUE: the builder files carry their own frozen firewalls, and
  the own call-graph reachability scan here confirms zeta is
  owned only by audit_* functions, np.load only by ward_*
  functions, and no zero-oracle name is reachable from
  build_cell / c01_target / hp_zero_data / trig_profile.  Gate-
  scope wording only; closed here at instrument level.  GATE:
  G15 (reachability scan).

CHECKED CLEAN (adversarially, no finding): the r131 SECULAR
IDENTITY re-derived on an own exact-rational rank-one instance
(K = 6, dim 11, sympy-free) and at working precision on the own
x = 3 cell; the GW PINNING reproduced INDEPENDENTLY at x = 3 --
own Weil form (own kernels, own quadrature, own atoms) hits the
frozen tau string 3.05582e-7 and the zero-side cache sum lands
inside the own envelope tail with the smallness law holding at
every cache zero (the arch kernel derivation here doubles as an
independent proof that the round-114 builder implements the
classical explicit-formula functional, including the boundary
atom log 3 == 2A contributing exactly zero at x = 3); the AST
firewall claim closed by reachability (BH4-F4); hsw_G re-derived
via independent numeric IBP (rel dev < 1e-8) + cache sanity with
margins; HSW22 Cor. 1.2 (0.1038, 0.2573, 9.3675), BW25 published
(0.10076, 0.24460, 8.08344; v1 abstract 8.08292 -- r144's
disclosure verified against both sources), PT21 = 3000175332800
citation pins verified; Theorems M/E/T/C/A re-proven with own
exact instances incl. stray + empty-ball refusals; the Theorem-A
closed forms recomputed with own code: D < 0 on the strip
(13..89), x_0 = 121 (own scan 90..200), x_0(BW25) = 112 (r144
G21 replicated), MRB(144) = 144.1, MRB(1e6) = 10.5; D1
(derivative identity, both closed forms), D2 (sum rules p = 0,1),
J3 (trace + spacing forms of A_2/A_0 -- mutually consistent with
D2), Y4 (s delta_1 share_1 rho2/et_1^2 == 1), W1 (defect identity
+ two-sided pinch), W2 (loop both directions), U1 (two-sided
susceptibility gap), X3 (interlacing pole/zero representation) --
all verified on own exact/mp instances; O1a's integer instance
recounted exactly (prime powers {7,8,9,11,13} in (5, 5e], Delta K
= 45 - 11 = 34, cells 40 <= budget 60.9); O3a/O3b assembly
algebra re-derived; the OFF identity 8 e^A ENV_3(T_PT)^2 G ==
8 sqrt(x) (1 + eta_PT)^2 A_0^2 G exact (e^A == sqrt(x)); the
LANDAU PINS recomputed from the cache: z(x=5) = +0.17, z(x=13) =
-0.10, z0(x=18) = +1.00 (r137 G37 strings reproduced to <= 0.05);
the min-cut flows re-verified with own Dinic: r131 4/5/5, r141
4/5/5/6, r148 4/5/5/7 (and the 4/5/5/7 quadruple checked by hand:
base 4 unit paths, serial chain +1, TOPROOT grant capped, 3
parallel counterfactual edges -> 7); SPEC_SHA integrity: the
recomputed docstring hash of EVERY round probe matches its frozen
logs (l1_weyllaw 7d8cc2e5, wpd 4ca02dba post-AMENDMENT-1,
dominance 00b98f5e, hpin 80366b4e, spacrem 861d9ff4, epslock
2ac675e2, counteq 1ec611ce, qsubgap 036c158e, jetlock 85e7ba69,
pfloor 0daf9dd0, tlawcap 85971e17, toproot 4fcd70be, suscap
ca9c7f92, fullgap_spectrum 87ab90ea, adjugate 0fb1fb1d,
fullgap_onset 82f845b8 current with run1/run2 at the disclosed
pre-addendum 3eca7075); rescue provenance: F-layer run1 vs run2
and rescue run3 vs run4 re-diffed -- non-timing diff EMPTY, raw
pair counts exactly as claimed (CDLII: 9; CDL: 5), run2's start
time from mtime - runtime = 15:00:34 matching CDLII's "15:00
restart", the refreeze (smoke2 -> smoke3, G74 circle-mean smoke
bar) sits between them exactly as disclosed; the r132 AMENDMENT 1
(f64-refine census corruption) and r147 float(pprime) underflow
abort are model disclosures, run/abort records kept; tau / A_0 /
FULLGAP / Theta_J string continuity across r131/135/137/140/143/
146/148 logs and specs; note numerals CDXXXII..CDLII gap-free and
strictly consecutive with CDXLIX correctly attached to the
F-layer fullgap_onset round; the round <-> numeral citation map
(r137=CDXLI, r139=CDXLIII, r140=CDXLIV, r141=CDXLV, r142=CDXLVI,
r142-144 = CDXLVI-CDXLVIII) grep-consistent; the honesty-crux
adjudication of r147 ("the OMEGA-a leg contracts {TOPROOT,
ONSETCAP} -> {EPSLOCK-AVG}") re-traced independently on the
dependency graph and CONFIRMED (TOPROOT/ONSETCAP/TAILVIS appear
only on the proof-route side of EPS-LOCK; LM consumes EPS-LOCK
directly; SUSCAP2R/DELTA1FLOOR legs unchanged; the r148 O3b
currency-invariance is consistent with it); the final residue
census {TOPROOT, ONSETCAP(=TLAWCAP), SUSCAP2R} + DELTA1FLOOR +
a-walls, cardinality 4, is consistent with every round's own
assembled-residue paragraph EXCEPT the CDXLV omission (BH4-F1);
the delta_1-lock quintuple is consistent at every quoted
precision across r143/r146/CDXLVII/CDL/CDXLIX (BH4-F3 label
nuance only); frameschedule (r134, CCM lane) verified frozen and
green at its own SPEC but not deep-audited (not on the prime
load-bearing chain; disclosed).

NO ROUND VERDICT FLIPS.  No frozen number in rounds 131-148 was
found wrong; the two MINOR findings are a residue-bookkeeping gap
at CDXLV (self-corrected in-corpus one round later, never
retro-amended) and a rescue-evidence retention gap at CDLI.
COMPOSITE: BUGHUNT4-FINDINGS(4) = 0 MAJOR / 2 MINOR / 2 NOTE.
NO RH CLAIM.
"""

from __future__ import annotations

import ast
import math
import os
import re
import sys
import time
import hashlib
from fractions import Fraction

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
START = time.time()

CHECKS: list[tuple[str, bool, str]] = []
FINDINGS = [
    ("BH4-F1", "MINOR", "r141/CDXLV residue omits DELTA1FLOOR that its "
                        "own G16 form gap >= 1/(s + 1/delta_1) requires; "
                        "corrected in-corpus by r142 W2 / r144 A8"),
    ("BH4-F2", "MINOR", "CDLI claims a deterministic re-run for r147 but "
                        "only one log (frozen.log) is kept: claim "
                        "unverifiable from frozen evidence"),
    ("BH4-F3", "NOTE", "r146 labels the r143 delta_1/y_t quintuple as "
                       "FULLGAP/y_t (same numbers; identification "
                       "measured in-corpus; label drift only)"),
    ("BH4-F4", "NOTE", "r131 G01 firewall scans only its own file while "
                       "the verdict speaks about the builder; claim true "
                       "(closed here by own reachability scan)"),
]


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def section(t: str) -> None:
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78, flush=True)


def blob(name: str) -> str:
    with open(os.path.join(HERE, name), encoding="utf-8",
              errors="replace") as fh:
        return fh.read()


def ward_cache() -> np.ndarray:
    return np.asarray(np.load(os.path.join(
        HERE, "verified_zeros_n7000.npy")), float)


# ===================================================================== G01
def g01_firewall() -> None:
    section("G01  SELF-FIREWALL (stdout only; no frozen-probe import)")
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    writers, imports = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            fn = node.func
            nm = (fn.attr if isinstance(fn, ast.Attribute)
                  else fn.id if isinstance(fn, ast.Name) else "")
            if nm == "open" and len(node.args) >= 2:
                m = node.args[1]
                if isinstance(m, ast.Constant) and "w" in str(m.value):
                    writers.append(node.lineno)
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([a.name for a in node.names]
                    if isinstance(node, ast.Import) else [node.module or ""])
            for m in mods:
                if m.endswith("_probe") or m.startswith("verification"):
                    imports.append(m)
    check("G01-firewall", not writers and not imports,
          "write-mode opens: %s; frozen-probe imports: %s"
          % (writers or "none", imports or "none"))


# ===================================================================== G02
ROM = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def rom2int(s: str) -> int:
    t = 0
    for i, ch in enumerate(s):
        v = ROM[ch]
        t += -v if i + 1 < len(s) and ROM[s[i + 1]] > v else v
    return t


NOTES: dict[int, str] = {}


def g02_numerals() -> None:
    section("G02  NOTE-NUMERAL INTEGRITY + ROUND MAP (head of next.txt)")
    lines = open(os.path.join(REPO, "experiments", "next.txt"),
                 encoding="utf-8").read().splitlines()
    seq = []
    for ln in lines[:40]:
        m = re.match(r"# 2026-\d\d-\d\d \(([IVXLCDM]+)\)", ln)
        if m:
            n = rom2int(m.group(1))
            seq.append(n)
            NOTES[n] = ln
    want = list(range(452, 431, -1))          # CDLII .. CDXXXII
    # anchor at CDLII (452): later notes may land above the audited head
    i0 = seq.index(452) if 452 in seq else -1
    chain = i0 >= 0 and seq[i0:i0 + 21] == want \
        and seq[:i0 + 1] == list(range(452 + i0, 451, -1))
    c449 = NOTES.get(449, "")
    ok_449 = ("fullgap_onset_probe.py" in c449
              and "3eca7075f38e2a2e" in c449 and "27/27" in c449
              and "1991.9" in c449)
    ok_452 = ("82f845b806f72fa7" in NOTES.get(452, "")
              and "fullgap_onset_probe.py" in NOTES.get(452, ""))
    ok_cite = ("CDXLI/CDXLIII/CDXLIV/CDXLV" in blob(
        "tlawcap_suscap2r_probe.py")
        and "CDXLVI/CDXLVII/CDXLVIII" in blob("fullgap_spectrum_probe.py"))
    check("G02-numeral-chain", chain and ok_449 and ok_452 and ok_cite,
          "CDLII..CDXXXII strictly consecutive (%d headers); CDXLIX = "
          "F-layer fullgap_onset (27/27, 3eca7075, 1991.9 s) verified; "
          "CDLII carries the addendum SHA; r137/139/140/141 <-> CDXLI/"
          "CDXLIII/CDXLIV/CDXLV and r142-144 <-> CDXLVI-CDXLVIII "
          "citation maps grep-consistent" % len(seq[:21]))


# ===================================================================== G03
LOG_PINS = {
    "l1_weyllaw_probe.py": (("l1_weyllaw_probe.run1.log",
                             "l1_weyllaw_probe.run2.log"), None),
    "wpd_proof_probe.py": (("wpd_proof_probe.run2.log",
                            "wpd_proof_probe.run3.log"), None),
    "dominance_proof_probe.py": (("dominance_proof_probe.run1.log",
                                  "dominance_proof_probe.run2.log"), None),
    "hpin_floor_probe.py": (("hpin_floor_probe.run2.log",
                             "hpin_floor_probe.run3.log"), None),
    "spacing_remainder_probe.py": (("spacing_remainder_probe.run1.log",
                                    "spacing_remainder_probe.run2.log"),
                                   None),
    "epslock_probe.py": (("epslock_probe.run1.log",
                          "epslock_probe.run2.log"), None),
    "counteq_seedball_probe.py": (("counteq_seedball_probe.run2.log",
                                   "counteq_seedball_probe.run3.log"),
                                  None),
    "qsubgap_probe.py": (("qsubgap_probe.run1.log",
                          "qsubgap_probe.run2.log"), None),
    "jetlock_bandmass_probe.py": (("jetlock_bandmass_probe.run1.log",
                                   "jetlock_bandmass_probe.run2.log"),
                                  None),
    "pfloor_suscap2_probe.py": (("pfloor_suscap2_probe.run4.log",
                                 "pfloor_suscap2_probe.run5.log"), None),
    "tlawcap_suscap2r_probe.py": (("tlawcap_suscap2r_probe.run1.log",
                                   "tlawcap_suscap2r_probe.run2.log"),
                                  None),
    "toproot_tailvis_probe.py": (("toproot_tailvis_probe.run1.log",
                                  "toproot_tailvis_probe.run2.log"), None),
    "suscap_master_probe.py": (("suscap_master_probe.run1.log",
                                "suscap_master_probe.run2.log"), None),
    "fullgap_spectrum_probe.py": (("fullgap_spectrum_probe.run1.log",
                                   "fullgap_spectrum_probe.run2.log"),
                                  None),
    "adjugate_logmaster_probe.py": (("adjugate_logmaster_probe.frozen.log",
                                     ), None),
    "fullgap_onset_probe.py": (("fullgap_onset_probe.run3.log",
                                "fullgap_onset_probe.run4.log"), None),
}


def doc_sha(fn: str) -> str:
    src = blob(fn)
    doc = ast.get_docstring(ast.parse(src), clean=False)
    return hashlib.sha256(doc.encode("utf-8")).hexdigest()[:16]


def log_sha(fn: str) -> str:
    m = re.search(r"SPEC_SHA ([0-9a-f]{16})", blob(fn))
    return m.group(1) if m else "?"


def g03_spec_sha() -> None:
    section("G03  SPEC_SHA INTEGRITY (17 round probes vs frozen logs)")
    bad = []
    for probe, (logs, _x) in LOG_PINS.items():
        d = doc_sha(probe)
        for lg in logs:
            ls = log_sha(lg)
            if ls != d:
                bad.append("%s: doc %s != log(%s) %s" % (probe, d, lg, ls))
    ok_pre = (log_sha("fullgap_onset_probe.run1.log")
              == log_sha("fullgap_onset_probe.run2.log")
              == "3eca7075f38e2a2e")
    # amendment chains: every pre-amendment run SHA is quoted verbatim
    # in the corresponding disclosed AMENDMENT block of the final spec
    chains = (
        ("wpd_proof_probe.py", "wpd_proof_probe.run1.log",
         "9d206e5f4bb9688d"),
        ("hpin_floor_probe.py", "hpin_floor_probe.run1.log",
         "c2c8f223f0d5748a"),
        ("counteq_seedball_probe.py", "counteq_seedball_probe.run1.log",
         "9047d9bfb1daa31e"),
        ("pfloor_suscap2_probe.py",
         "pfloor_suscap2_probe.run1.preamendment.log",
         "4d8c1c5cb6f76d92"),
        ("pfloor_suscap2_probe.py", "pfloor_suscap2_probe.run2.log",
         "7b2b60483662d9ce"),
        ("pfloor_suscap2_probe.py", "pfloor_suscap2_probe.run3.log",
         "c68e1eb7c658ed76"),
    )
    ok_chain = all(log_sha(lg) == sha and sha in blob(pf)
                   for pf, lg, sha in chains)
    check("G03-spec-sha", not bad and ok_pre and ok_chain
          and doc_sha("fullgap_onset_probe.py") == "82f845b806f72fa7",
          "all recomputed docstring hashes match their run-of-record "
          "logs; fullgap_onset run1/run2 carry the disclosed "
          "pre-addendum 3eca7075, current file == 82f845b8; every "
          "pre-amendment run SHA (wpd/hpin/counteq/pfloor x3) is "
          "quoted verbatim in its disclosed AMENDMENT block%s"
          % ("" if not bad else "; MISMATCH " + "; ".join(bad)))


# ===================================================================== G04
def norm_timing(fn: str) -> list[str]:
    out = []
    for ln in blob(fn).splitlines():
        ln = re.sub(r"\d+(\.\d+)? s\b", "TIME", ln)
        ln = re.sub(r"runtime \S+", "runtime TIME", ln)
        out.append(ln)
    return out


def raw_pairs(f1: str, f2: str) -> int:
    a = blob(f1).splitlines()
    b = blob(f2).splitlines()
    return sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))


def nontiming_pairs(f1: str, f2: str) -> int:
    a = norm_timing(f1)
    b = norm_timing(f2)
    return sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))


def g04_rescue_diffs() -> None:
    section("G04  RESCUE RUN-OF-RECORD DIFFS (claims re-computed)")
    n12 = nontiming_pairs("fullgap_onset_probe.run1.log",
                          "fullgap_onset_probe.run2.log")
    r34 = raw_pairs("fullgap_onset_probe.run3.log",
                    "fullgap_onset_probe.run4.log")
    n34 = nontiming_pairs("fullgap_onset_probe.run3.log",
                          "fullgap_onset_probe.run4.log")
    rsp = raw_pairs("fullgap_spectrum_probe.run1.log",
                    "fullgap_spectrum_probe.run2.log")
    nsp = nontiming_pairs("fullgap_spectrum_probe.run1.log",
                          "fullgap_spectrum_probe.run2.log")
    # wall-clock story: run2 start = mtime - runtime ~ 15:00 (CDLII)
    mt2 = os.path.getmtime(os.path.join(
        HERE, "fullgap_onset_probe.run2.log"))
    start2 = time.localtime(mt2 - 2022.5)
    ok_clock = (start2.tm_hour, abs(start2.tm_min)) <= (15, 5) and \
        start2.tm_hour == 15 and start2.tm_min <= 5
    check("G04-rescue-diffs", n12 == 0 and n34 == 0 and r34 == 9
          and nsp == 0 and rsp == 5,
          "F-layer run1 vs run2 non-timing diff %d (claim: identical); "
          "rescue run3 vs run4 raw %d (CDLII claim 9) non-timing %d; "
          "spectrum run1 vs run2 raw %d (CDL claim 5) non-timing %d; "
          "run2 start from mtime-runtime = %02d:%02d:%02d (CDLII: "
          "'15:00 restart'%s)"
          % (n12, r34, n34, rsp, nsp, start2.tm_hour, start2.tm_min,
             start2.tm_sec, ", consistent" if ok_clock else
             " -- INFO only, mtimes are copy-fragile"))


# ===================================================================== G05
def g05_hsw_citations() -> None:
    section("G05  CITATION PINS (HSW22 / BW25 / PT21) + corpus usage")
    # corpus pins (grep)
    l1 = blob("l1_weyllaw_probe.py")
    sm = blob("suscap_master_probe.py")
    ok = ("0.1038" in l1 and "0.2573" in l1 and "9.3675" in l1
          and "3000175332800" in l1
          and "0.10076" in sm and "0.24460" in sm and "8.08344" in sm
          and "8.08292" in sm)
    # published values verified externally 2026-08-17 (see spec):
    # HSW22 Cor. 1.2: 0.1038 log T + 0.2573 loglog T + 9.3675 (T >= e)
    # BW25 published (Math. Comp. / arXiv 2412.15470v2): 0.10076 /
    # 0.24460 / 8.08344 (T >= e); v1 abstract carried 8.08292.
    # PT21: RH verified to 3.0001753328e12 (Platt-Trudgian 2021).
    qb = lambda a, b, c, T: a * math.log(T) + b * math.log(math.log(T)) + c
    okq = all(qb(0.10076, 0.24460, 8.08344, T)
              < qb(0.1038, 0.2573, 9.3675, T)
              for T in (math.e, 50.0, 1e3, 1e6, 3e12))
    check("G05-citations", ok and okq,
          "HSW22 Cor. 1.2 / BW25 published (incl. the v1 8.08292 "
          "discrepancy r144 disclosed) / PT21 pins present and verified "
          "against the published statements; Q_BW(T) < Q_HSW(T) on the "
          "grid (all three coefficients smaller)")


# ================================================== independent tail form
def hsw_G(T: float, C=(0.1038, 0.2573, 9.3675)) -> float:
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        al, be, cc = (mp.mpf(repr(c)) for c in C)
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg)) + cc) \
            / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return float(t1 + t2 + t3)


def m_rvm(T: float) -> float:
    return (T / (2 * math.pi)) * math.log(T / (2 * math.pi * math.e)) \
        + 7.0 / 8.0


def q_hsw(T: float, C=(0.1038, 0.2573, 9.3675)) -> float:
    return C[0] * math.log(T) + C[1] * math.log(math.log(T)) + C[2]


def g06_hsw_independent() -> None:
    section("G06  hsw_G RE-DERIVED (independent numeric IBP + cache)")
    # G(T) <= 2 int_T^oo (M(t) + Q(t) - (M(T) - Q(T))) t^-3 dt; the
    # closed form is term1+term2+term3 with the loglog tangent bound.
    # Independent check WITHOUT the tangent bound (numeric loglog):
    # closed form must be >= the exact integral (tangent is an upper
    # bound), and within 1e-3 of it at moderate T.
    devs = []
    okmarg = True
    with mp.workdps(30):
        for T in (200.0, 2000.0):
            Tm = mp.mpf(T)

            def integ(t):
                Mt = (t / (2 * mp.pi)) * mp.log(t / (2 * mp.pi * mp.e)) \
                    + mp.mpf(7) / 8
                Qt = (mp.mpf("0.1038") * mp.log(t)
                      + mp.mpf("0.2573") * mp.log(mp.log(t))
                      + mp.mpf("9.3675"))
                MT = (Tm / (2 * mp.pi)) * mp.log(Tm / (2 * mp.pi * mp.e)) \
                    + mp.mpf(7) / 8
                QT = (mp.mpf("0.1038") * mp.log(Tm)
                      + mp.mpf("0.2573") * mp.log(mp.log(Tm))
                      + mp.mpf("9.3675"))
                return 2 * (Mt + Qt - (MT - QT)) / t ** 3
            exact = float(mp.quad(integ, [Tm, 10 * Tm, 1e3 * Tm,
                                          1e6 * Tm, mp.inf]))
            cf = hsw_G(T)
            devs.append((T, exact, cf, cf / exact - 1))
            okmarg = okmarg and 0 <= cf / exact - 1 < 1e-3
    gam = ward_cache()
    okc = all(float(np.sum(gam[gam > T] ** -2.0)) <= hsw_G(T)
              for T in (200.0, 2000.0, 5000.0))
    okm = hsw_G(200.0) > hsw_G(2000.0) > hsw_G(7264.0) > hsw_G(3e12)
    check("G06-hswG-independent", okmarg and okc and okm,
          "closed form vs own numeric IBP integral: " + "; ".join(
              "T=%g rel excess %.1e" % (T, d) for T, _e, _c, d in devs)
          + " (tangent bound the only slack); cache partials below G "
          "at T = 200/2000/5000; G monotone falling")


# ===================================================================== G07
def frac_det(Mrows: list[list[Fraction]]) -> Fraction:
    n = len(Mrows)
    A = [row[:] for row in Mrows]
    det = Fraction(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det *= A[c][c]
        inv = A[c][c]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] / inv
                for cc in range(c, n):
                    A[r][cc] -= f * A[c][cc]
    return det


def g07_secular() -> None:
    section("G07  r131 SECULAR IDENTITY (own exact instance, K = 6)")
    K = 6
    cs = [Fraction(3, 7), Fraction(-1, 3), Fraction(2, 5),
          Fraction(1, 11), Fraction(-2, 9), Fraction(5, 13)]
    A0 = sum((-1) ** k * cs[k] for k in range(K))
    dim = 2 * K - 1
    mid = K - 1
    dv = [Fraction(n - mid) for n in range(dim)]     # lattice units pi/A=1
    xi = [Fraction(0)] * dim
    xi[mid] = cs[0]
    for k in range(1, K):
        xi[mid + k] = cs[k] / 2
        xi[mid - k] = cs[k] / 2
    eta = [Fraction((-1) ** abs(n - mid)) for n in range(dim)]
    S = sum(eta[i] * xi[i] for i in range(dim))
    assert S == A0
    bs = [Fraction(k * k) for k in range(1, K)]      # b_k = om_k^2 = k^2

    def C_of(y: Fraction) -> Fraction:
        # C(y) = c0 prod(y-b) + sum_k (-1)^k c_k y prod_{j!=k}(y-b_j)
        prod_all = Fraction(1)
        for b in bs:
            prod_all *= (y - b)
        tot = cs[0] * prod_all
        for i, k in enumerate(range(1, K)):
            pr = Fraction(1)
            for j, b in enumerate(bs):
                if j != i:
                    pr *= (y - b)
            tot += (-1) ** k * cs[k] * y * pr
        return tot

    zs = [Fraction(p, q) for p, q in
          ((1, 2), (3, 4), (7, 5), (12, 7), (9, 4), (13, 5), (10, 3),
           (17, 4), (23, 5), (16, 3), (11, 2), (25, 4), (19, 3))]
    ok = True
    for z in zs:
        Mz = [[(dv[i] if i == j else Fraction(0))
               - dv[i] * xi[i] * eta[j] / S
               - (z if i == j else Fraction(0))
               for j in range(dim)] for i in range(dim)]
        lhs = frac_det(Mz)
        rhs = -z * C_of(z * z) / A0
        ok = ok and lhs == rhs
    check("G07-secular-own-instance", ok,
          "det(Meta - z) == -z C(z^2)/A_0 EXACT (Fractions, dim 11, "
          "13 interpolation points > deg 11: polynomial identity) -- "
          "node count == K-1 = %d census degree, own instance, "
          "sympy-free" % (K - 1))


# ===================================================================== G08
def g08_sumrules() -> None:
    section("G08  D1/D2/J3/Y4 SUM RULES (own exact-rational instance)")
    # F(y) = A0 prod(y - y_j)/prod(y - b_k), K-1 = 3
    A0 = Fraction(3, 7)
    bs = [Fraction(1), Fraction(4), Fraction(9)]
    ys = [Fraction(2), Fraction(11, 2), Fraction(7)]
    ws = []
    for i, b in enumerate(bs):
        num = Fraction(1)
        for y in ys:
            num *= (b - y)
        den = Fraction(1)
        for j, b2 in enumerate(bs):
            if j != i:
                den *= (b - b2)
        ws.append(A0 * num / den)

    def Fp_weight(y):
        return -sum(w / (y - b) ** 2 for w, b in zip(ws, bs))

    def Fp_spacing(yj, j):
        num = A0
        for i, y in enumerate(ys):
            if i != j:
                num *= (yj - y)
        den = Fraction(1)
        for b in bs:
            den *= (yj - b)
        return num / den

    ok1 = all(Fp_weight(ys[j]) == Fp_spacing(ys[j], j) for j in range(3))
    A2 = sum(ws)                       # m_0
    A4 = sum(w * b for w, b in zip(ws, bs))   # m_1
    s0 = sum(Fraction(1) / Fp_weight(y) for y in ys)
    s1 = sum(y / Fp_weight(y) for y in ys)
    ok2 = (s0 == (sum(ys) - sum(bs)) / A0 == -A2 / A0 ** 2)
    ok3 = (s1 == -A4 / A0 ** 2 + A2 ** 2 / A0 ** 3)
    tr = sum(bs) - sum(ys)             # J3 trace form
    sp = Fraction(0)
    for j, yj in enumerate(ys):
        num = Fraction(1)
        for b in bs:
            num *= (yj - b)
        den = Fraction(1)
        for i, y in enumerate(ys):
            if i != j:
                den *= (yj - y)
        sp += num / den
    ok4 = (A2 / A0 == tr) and (A2 / A0 == -sp)
    # Y4 identity on an exact 3-level instance (tau = 1 units)
    d1, d2 = Fraction(1, 2), Fraction(3)
    r2, e1, e2 = Fraction(1, 2), Fraction(3, 10), Fraction(1, 5)
    chi = e1 / d1 + e2 / d2
    s = chi / r2
    share1 = (e1 / d1) / chi
    ok5 = s * d1 * share1 * r2 / e1 == 1
    check("G08-sumrules-own-instance", ok1 and ok2 and ok3 and ok4 and ok5,
          "weight form == spacing form of F' at all census roots; "
          "sum 1/F' == (sum y - sum b)/A0 == -A2/A0^2; sum y/F' == "
          "-A4/A0^2 + A2^2/A0^3; J3 trace == A0-free spacing form "
          "(mutually consistent with D2); Y4 s d1 share1 r2/e1^2 == 1 "
          "-- ALL EXACT in Q, sympy-free")


# ===================================================================== G09
def g09_pinch_loop() -> None:
    section("G09  W1/W2/U1/X3 (pinch, loop, gap, interlacing; own inst)")
    with mp.workdps(60):
        d = [mp.mpf("0.5"), mp.mpf(2), mp.mpf(5)]           # delta_i
        e2 = [mp.mpf("0.5"), mp.mpf("0.25"), mp.mpf("0.125"),
              mp.mpf("0.125")]                              # rho2, et^2
        r2 = e2[0]

        def sec(g):
            return r2 / g - sum(e2[i + 1] / (d[i] - g) for i in range(3))
        lo, hi = mp.mpf("1e-30"), d[0] * (1 - mp.mpf("1e-25"))
        for _ in range(220):
            mid = (lo + hi) / 2
            if sec(mid) > 0:
                lo = mid
            else:
                hi = mid
        g = (lo + hi) / 2
        chi = sum(e2[i + 1] / d[i] for i in range(3))
        s = chi / r2
        defect = (g ** 2 / r2) * sum(e2[i + 1] / (d[i] * (d[i] - g))
                                     for i in range(3))
        ok_w1 = abs((1 - s * g) - defect) < mp.mpf("1e-45")
        ok_pinch = (1 - g / d[0]) - mp.mpf("1e-45") <= s * g \
            <= 1 + mp.mpf("1e-45")
        u1_lo = r2 / (chi + r2 / d[0])
        u1_hi = r2 / ((1 - r2) * chi)
        ok_u1 = u1_lo - mp.mpf("1e-45") <= g <= u1_hi + mp.mpf("1e-45")
        # W2 forward/backward on the instance
        ok_w2 = (s <= 1 / g + mp.mpf("1e-40")) and (d[0] > g) \
            and (g + mp.mpf("1e-40") >= 1 / (s + 1 / d[0]))
        # X3: Q(z) zeros interlace poles; s == sum brackets
        q = [mp.mpf(1), mp.mpf(1) + d[0], mp.mpf(1) + d[1],
             mp.mpf(1) + d[2]]

        # Q(z) = sum_i e2_i prod_{j != i} (z - q_j)  (degree 3)
        def expand(roots):
            c = [mp.mpf(1)]
            for r in roots:
                nc = [mp.mpf(0)] * (len(c) + 1)
                for k, v in enumerate(c):
                    nc[k] += v
                    nc[k + 1] -= v * r
                c = nc
            return c
        Qc = [mp.mpf(0)] * 4
        for i in range(4):
            pc = expand([q[j] for j in range(4) if j != i])
            for k in range(4):
                Qc[k] += e2[i] * pc[k]
        etas = sorted(mp.re(r) for r in mp.polyroots(Qc, maxsteps=200,
                                                     extraprec=60))
        inter = all(q[i] < etas[i] < q[i + 1] for i in range(3))
        s_x3 = sum(1 / (etas[i] - q[0]) - 1 / (q[i + 1] - q[0])
                   for i in range(3))
        ok_x3 = inter and abs(s_x3 - s) < mp.mpf("1e-40")
        # eta_0 == lam* cross-check
        ok_eta = abs((etas[0] - q[0]) - g) < mp.mpf("1e-40")
    check("G09-pinch-loop", bool(ok_w1 and ok_pinch and ok_u1 and ok_w2
                                 and ok_x3 and ok_eta),
          "W1 defect identity residual < 1e-45; pinch 1 - g/d1 <= sg <= "
          "1; U1 lower <= g <= upper; W2 forward+backward; X3 "
          "interlacing eta/pole ladder sums EXACTLY to s and eta_0 - "
          "q_0 == secular gap (dev < 1e-40)")


# ===================================================================== G10
def g10_theorems_meta() -> None:
    section("G10  THEOREMS M/E/T/C/A (own instances + closed forms)")
    a = Fraction(4)

    def w(t: Fraction) -> Fraction:
        return a * t * t / (a + t * t) ** 2
    trues = [Fraction(4), Fraction(5), Fraction(6), Fraction(17, 2),
             Fraction(11), Fraction(30), Fraction(45)]
    gs = [Fraction(1, 50), Fraction(1, 40), Fraction(1, 30)]
    nodes = [Fraction(4) + Fraction(1, 100), Fraction(5) - Fraction(1, 80),
             Fraction(6) + Fraction(1, 90), Fraction(9), Fraction(13)]
    Tz = Fraction(7)
    m = sum(1 for t in trues if t <= Tz)
    # H1 disjoint+ordered, H2 no strays, H3 one per ball
    balls = [(trues[j] - gs[j], trues[j] + gs[j]) for j in range(m)]
    okH1 = all(balls[j][1] < balls[j + 1][0] for j in range(m - 1))
    inb = [[n for n in nodes if lo <= n <= hi] for lo, hi in balls]
    top = max(Tz, balls[-1][1])
    okH2 = all(any(lo <= n <= hi for lo, hi in balls)
               for n in nodes if n <= top)
    okH3 = all(len(v) == 1 for v in inb)
    okC1 = all(sorted(nodes)[i] >= trues[i] - gs[i] for i in range(m))
    okC2 = all(sorted(nodes)[i] > Tz for i in range(m, len(nodes)))
    # M2 certified M- bound
    mm = sum(max(Fraction(0), w(nodes[i]) - w(trues[i]))
             for i in range(len(nodes)))
    zone_bound = sum(w(trues[j] - gs[j]) - w(trues[j]) for j in range(m))
    edge_bound = sum(max(Fraction(0), w(nodes[i]) - w(trues[i]))
                     for i in range(m, len(nodes)))
    okM2 = mm <= zone_bound + edge_bound
    # Theorem E on the instance
    okE = (edge_bound <= (len(nodes) - m) * w(Tz))
    # stray refusal: extra node 3 breaks H2 AND sorted dominance
    nodes_s = sorted([Fraction(3)] + nodes)
    okH2s = all(any(lo <= n <= hi for lo, hi in balls)
                for n in nodes_s if n <= top)
    doms = all(nodes_s[i] >= trues[i] - gs[i] for i in range(m))
    ok_stray = (not okH2s) and (not doms)
    # empty-ball refusal: two nodes in ball 1, ball 2 empty => P fails
    nodes_e = [Fraction(4) + Fraction(1, 100), Fraction(4)
               + Fraction(3, 200), Fraction(6) + Fraction(1, 90),
               Fraction(9), Fraction(13)]
    okP_e = all(any(lo <= n <= hi for n in nodes_e)
                for lo, hi in balls)
    ok_empty = not okP_e
    # Theorem C(ii) identity at equality th = 1/3
    th = Fraction(1, 3)
    Mp, tail = Fraction(7, 5), Fraction(2, 5)
    Mm = (1 - th) * (Mp + tail)
    d1 = Mp - Mm + tail
    okC = (d1 == th * (Mp + tail)) and \
        ((Mp + Mm) / d1 <= (2 - th) / th)
    # Theorem A closed forms, own code
    def t_star(N):
        lo, hi = 20.0, 1e30
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            if m_rvm(mid) - q_hsw(mid) >= N:
                hi = mid
            else:
                lo = mid
        return hi

    def wf(av, t):
        return av * t * t / (av + t * t) ** 2

    def tl_shell(N, av, Ts):
        best = 0.0
        for lam in (1.5, 2.0, 3.0):
            for J in (1, 2, 3, 4, 6, 8):
                Tj = [Ts * lam ** j for j in range(J + 1)]
                tot, up = 0.0, m_rvm(Ts) + q_hsw(Ts)
                for j in range(J):
                    nn = m_rvm(Tj[j + 1]) - q_hsw(Tj[j + 1])
                    tot += max(0.0, nn - max(float(N), up)) \
                        * wf(av, Tj[j + 1])
                    up = m_rvm(Tj[j + 1]) + q_hsw(Tj[j + 1])
                best = max(best, tot)
        return best

    def DM(x, av, C=(0.1038, 0.2573, 9.3675)):
        K = int(math.ceil(1.25 * x * math.log(x)))
        N = K - 1
        # t_star / q under the chosen constant set
        def qh(T):
            return C[0] * math.log(T) + C[1] * math.log(math.log(T)) \
                + C[2]
        lo, hi = 20.0, 1e30
        for _ in range(200):
            mid = math.sqrt(lo * hi)
            if m_rvm(mid) - qh(mid) >= N:
                hi = mid
            else:
                lo = mid
        Ts = hi
        Tzx = 2 * math.pi * x
        nz = m_rvm(Tzx) - qh(Tzx)
        best = 0.0
        for lam in (1.5, 2.0, 3.0):
            for J in (1, 2, 3, 4, 6, 8):
                Tj = [Ts * lam ** j for j in range(J + 1)]
                tot, up = 0.0, m_rvm(Ts) + qh(Ts)
                for j in range(J):
                    nn = m_rvm(Tj[j + 1]) - qh(Tj[j + 1])
                    tot += max(0.0, nn - max(float(N), up)) \
                        * wf(av, Tj[j + 1])
                    up = m_rvm(Tj[j + 1]) + qh(Tj[j + 1])
                best = max(best, tot)
        TL = best
        me = max(0.0, N - nz) * wf(av, Tzx)
        Dv = TL - TL / 8.0 - me
        mrb = ((TL / 8.0 + av * hsw_G(Tzx, C) + me) / Dv
               if Dv > 0 else float("inf"))
        return Dv, mrb
    bat = (1.0, 4.0, 16.0)
    ok_strip = all(DM(x, av)[0] < 0 for x in (13, 21, 34, 55, 89)
                   for av in bat)
    BW = (0.10076, 0.24460, 8.08344)

    def x0_scan(C):
        okx = {x: all(DM(float(x), av, C)[0] > 0 for av in bat)
               for x in range(90, 201)}
        for xc in range(90, 201):
            if all(okx[x] for x in range(xc, 201)):
                return xc
        return None
    x0 = x0_scan((0.1038, 0.2573, 9.3675))
    x0_bw = x0_scan(BW)
    mrb144 = max(DM(144.0, av)[1] for av in bat)
    mrb1e6 = max(DM(1e6, av)[1] for av in bat)
    ok_asym = (abs(mrb144 / 144.1 - 1) < 0.01
               and abs(mrb1e6 / 10.5 - 1) < 0.02)
    # Theorem T at x = 5: gamma_{K-1} <= T*
    gam = ward_cache()
    Ts5 = t_star(10)
    okT = float(gam[9]) <= Ts5 and 79.0 < Ts5 < 80.0
    check("G10-theorems-META", okH1 and okH2 and okH3 and okC1 and okC2
          and okM2 and okE and ok_stray and ok_empty and okC
          and ok_strip and x0 == 121 and x0_bw == 112 and ok_asym
          and okT,
          "Theorem M/E instance exact in Q (conclusions + M2/E bounds); "
          "stray refusal (H2 + dominance BOTH fail); empty-ball refusal "
          "(PINBALL fails); Theorem C equality + (2-th)/th; Theorem A "
          "own closed forms: strip D<0 (13..89), x_0 = %s (r133: 121), "
          "x_0(BW25) = %s (r144: 112), MRB(144) = %.1f (144.1), "
          "MRB(1e6) = %.1f (10.5); Theorem T: gamma_10 = %.2f <= "
          "T*(10) = %.1f" % (x0, x0_bw, mrb144, mrb1e6,
                             float(gam[9]), Ts5))


# ===================================================================== G11
def g11_gw_pinning() -> None:
    section("G11  r131 GW PINNING (OWN Weil form at x = 3, independent)")
    x = 3
    dps = 45
    with mp.workdps(dps):
        A = mp.log(x) / 2
        K = int(math.ceil(1.25 * x * math.log(x)))
        oms = [k * mp.pi / A for k in range(K)]
        nrm = [mp.sqrt(2 * A) if k == 0 else mp.sqrt(A)
               for k in range(K)]
        L = 2 * A

        def acorr(j, k, w):
            """psi_{jk}(w) = int_{-A+w}^{A} cos(om_j v) cos(om_k (v-w))
            dv, 0 <= w <= 2A, closed form."""
            if w >= L:
                return mp.mpf(0)
            lo, hi = -A + w, A
            wj, wk = oms[j], oms[k]

            def ianti(om, ph, v):
                # int cos(om v + ph) dv
                if om == 0:
                    return v * mp.cos(ph)
                return mp.sin(om * v + ph) / om
            # cos a cos b = [cos(a-b) + cos(a+b)]/2 ;
            # a = wj v, b = wk v - wk w
            t1 = (ianti(wj - wk, wk * w, hi)
                  - ianti(wj - wk, wk * w, lo)) / 2
            t2 = (ianti(wj + wk, -wk * w, hi)
                  - ianti(wj + wk, -wk * w, lo)) / 2
            return t1 + t2

        def psis(j, k, w):
            return (acorr(j, k, w) + acorr(k, j, w)) / 2

        # pole
        ip = [((-1) ** k) * mp.sinh(A / 2) / (mp.mpf(1) / 4 + oms[k] ** 2)
              for k in range(K)]
        # prime atoms q <= e^{2A} = 3
        atoms = [(mp.log(2), mp.log(2) / mp.sqrt(2)),
                 (mp.log(3), mp.log(3) / mp.sqrt(3))]
        Q = mp.zeros(K, K)
        splits = sorted(set(
            [mp.mpf(0), mp.mpf("1e-6"), mp.mpf("1e-3"), mp.mpf("0.05")]
            + [j * mp.pi / oms[K - 1] for j in range(1, int(
                mp.floor(L * oms[K - 1] / mp.pi)) + 1)] + [L]))
        tailc = -mp.log1p(-mp.exp(-2 * L))
        for j in range(K):
            for k in range(j, K):
                p0 = psis(j, k, mp.mpf(0))
                pole = 2 * ip[j] * ip[k]
                prime = sum(2 * wgt * psis(j, k, u) for u, wgt in atoms)

                def ig(w, j=j, k=k, p0=p0):
                    return (p0 * mp.exp(-2 * w)
                            - psis(j, k, w) * mp.exp(-w / 2)) \
                        / (-mp.expm1(-2 * w))
                body = mp.quad(ig, splits)
                arch = -(mp.euler + mp.log(mp.pi)) * p0 \
                    + 2 * body + p0 * tailc
                val = (pole + arch - prime) / (nrm[j] * nrm[k])
                Q[j, k] = val
                Q[k, j] = val
        E, V = mp.eigsy(Q)
        order = sorted(range(K), key=lambda i: E[i])
        tau = E[order[0]]
        cn = [V[i, order[0]] / nrm[i] for i in range(K)]
        if float(cn[int(np.argmax([abs(float(v)) for v in cn]))]) < 0:
            cn = [-v for v in cn]
        A0 = sum((-1) ** k * cn[k] for k in range(K))
        tauf = float(tau)
        dev_tau = abs(math.log10(tauf / 3.05582e-7))
        # zero side over the full cache
        gam = ward_cache()

        def en_pair(t):
            Rv = 2 * cn[0] / t
            Rp = -2 * cn[0] / t ** 2
            for k in range(1, K):
                den = t * t - oms[k] ** 2
                Rv += 2 * cn[k] * (-1) ** k * t / den
                Rp += 2 * cn[k] * (-1) ** k * (-(t * t + oms[k] ** 2)) \
                    / den ** 2
            sn, csn = mp.sin(A * t), mp.cos(A * t)
            return sn * Rv, A * csn * Rv + sn * Rp
        P = mp.mpf(0)
        slop = mp.mpf(0)
        worst_small = 0.0
        for gv in gam:
            t = mp.mpf(repr(float(gv)))
            f, fp = en_pair(t)
            P += 2 * f ** 2
            slop += 2 * (2 * abs(f) * abs(fp) * mp.mpf("1e-9")
                         + (abs(fp) * mp.mpf("1e-9")) ** 2)
            worst_small = max(worst_small, float(2 * f ** 2))
        # own envelope tail beyond gtop
        jets = []
        sabs = []
        for mdeg in range(0, 5):
            jets.append(sum((-1) ** k * cn[k] * oms[k] ** (2 * mdeg)
                            if (k or mdeg == 0) else mp.mpf(0)
                            for k in range(K)))
            sabs.append(sum(abs(cn[k]) * oms[k] ** (2 * mdeg)
                            if (k or mdeg == 0) else mp.mpf(0)
                            for k in range(K)))
        gtop = mp.mpf(repr(float(gam[-1])))

        def env(T):
            acc = mp.mpf(0)
            for i in range(4):
                acc += abs(jets[i]) / T ** (2 * i)
            acc += sabs[4] / (T ** 6 * (T ** 2 - oms[-1] ** 2))
            return acc
        tail = 8 * env(gtop) ** 2 * mp.mpf(repr(hsw_G(float(gam[-1]))))
        off = 8 * mp.exp(A) * env(mp.mpf(3000175332800)) ** 2 \
            * mp.mpf(repr(hsw_G(3000175332800.0)))
        gap = tau - P
        ok_id = (float(P) <= tauf * (1 + 1e-3) + float(off + slop)) and \
            (float(gap) <= float(tail + off + slop) + 1e-3 * tauf)
        ok_small = worst_small <= tauf + float(off) + 1e-3 * tauf
        # boundary-atom exactness: psi(log 3) == 0 (log 3 == 2A)
        okb = all(abs(float(psis(j, k, mp.log(3)))) < 1e-40
                  for j in range(K) for k in range(K))
        a0f = float(abs(A0))
    check("G11-gw-pinning-own-build", dev_tau < 1e-3 and ok_id
          and ok_small and okb and abs(a0f / 1.84e-3 - 1) < 0.01,
          "own Weil form (K=%d, dps %d): tau = %.5e vs frozen 3.05582e-7"
          " (|dlog10| %.1e); A0 = %.3e vs r131 1.84e-3; zero side P = "
          "%.4e, tau - P = %.1e <= own ENV tail + OFF + slop = %.1e; "
          "max 2|E(gamma)|^2 = %.1e <= tau + OFF (smallness law at all "
          "7000 cache zeros); boundary atom log3 == 2A contributes "
          "EXACTLY zero (independent consistency with the r114 "
          "builder)" % (K, dps, tauf, dev_tau, a0f, float(P),
                        float(gap), float(tail + off + slop),
                        worst_small))


# ===================================================================== G12
def g12_bh4f1() -> None:
    section("G12  BH4-F1: r141 residue omits DELTA1FLOOR (witness+greps)")
    ok_w = True
    for d1 in (Fraction(1, 100), Fraction(1, 10 ** 6),
               Fraction(1, 10 ** 12)):
        r2 = 1 / (1 + d1)
        e1 = d1 / (1 + d1)
        # secular: r2/g = e1/(d1 - g)  =>  g = r2 d1 / (r2 + e1)
        g = r2 * d1 / (r2 + e1)
        s = (e1 / d1) / r2
        ok_w = ok_w and s == 1 and g == d1 / (1 + d1) \
            and g < d1 and (1 - g / d1) == s * g
    p141 = blob("pfloor_suscap2_probe.py")
    p142 = blob("tlawcap_suscap2r_probe.py")
    p144 = blob("suscap_master_probe.py")
    n445 = NOTES.get(445, "")
    ok_g = ("EPSLOCK-consumed" in p141
            and "1/(s + 1/delta_1)" in p141
            and "DELTA1FLOOR" not in p141
            and "EPSLOCK-konsumiert + SUSCAP2R" in n445
            and "RESIDUUM = {TOPROOT, TAILVIS, TLAWCAP, SUSCAP2R}"
            in n445
            and "DELTA1FLOOR" not in n445
            and "DELTA1FLOOR" in p142 and "LOOPED" in p142
            and "the fourth summand 1/delta_1 is REQUIRED" in p144)
    later = all("DELTA1FLOOR" in NOTES.get(n, "")
                for n in (446, 447, 448, 450, 451, 452))
    check("G12-F1-delta1floor-gap", ok_w and ok_g and later,
          "exact witness: s == 1 while g = d1/(1+d1) -> 0 (SUSCAP2R "
          "alone cannot give QSUBGAP; pinch saturated); r141 spec + "
          "CDXLV carry the 1/(s + 1/delta_1) form yet omit DELTA1FLOOR "
          "from the residue; r142 W2 ('LOOPED') + r144 A8 correct it; "
          "every note CDXLVI..CDLII carries DELTA1FLOOR")


# ===================================================================== G13
def g13_bh4f2() -> None:
    section("G13  BH4-F2: r147 re-run evidence not kept")
    logs = sorted(f for f in os.listdir(HERE)
                  if f.startswith("adjugate_logmaster_probe")
                  and f.endswith(".log"))
    fr = blob("adjugate_logmaster_probe.frozen.log")
    n_gates = fr.count("GATES:")
    n451 = NOTES.get(451, "")
    claim = "deterministischer Re-Run identisch modulo Timing" in n451
    check("G13-F2-rerun-evidence", logs == [
        "adjugate_logmaster_probe.frozen.log"] and n_gates == 1
        and claim and "2053.2" in fr,
        "adjugate logs kept: %s (exactly one GATES line, 2053.2 s "
        "record); CDLI claims a deterministic re-run 'identisch modulo "
        "Timing' whose log is NOT in the corpus -- unverifiable; all "
        "other rescue lanes kept both runs (re-diffed in G04)" % logs)


# ===================================================================== G14
def g14_bh4f3_lock() -> None:
    section("G14  BH4-F3: delta_1-lock quintuple consistency + label")
    r143 = blob("toproot_tailvis_probe.py")
    r146 = blob("fullgap_spectrum_probe.py")
    ok_lab = "delta_1/y_t = 3.64" in r143.replace("\n", "")
    ok_146 = "lock ratio FULLGAP/y_t = 3.64/2.39/3.31/2.58/2.84" in r146
    # delta_1 (r143) vs FULLGAP (r146) strings
    d143 = [2.2255e5, 9.9512e5, 1.0619e7]
    f146 = [2.225493e5, 9.951249e5, 1.061906e7]
    ok_rel = all(abs(a / b - 1) < 4e-5 for a, b in zip(d143, f146)) \
        and "delta1 2.2255e5" in r143
    ratios = [3.6444, 2.3890, 3.3141, 2.5836, 2.8361]
    recip = [0.274, 0.419, 0.302, 0.387, 0.353]
    ok_rec = all(abs(1.0 / r - v) < 6e-4 for r, v in zip(ratios, recip))
    n450 = NOTES.get(450, "")
    n447 = NOTES.get(447, "")
    ok_notes = ("3.6444/2.3890/3.3141/2.5836/2.8361" in n450
                and "3.644/2.389/3.314/2.584/2.836" in n447
                and "zwei unabh" in n450)
    check("G14-F3-lock-consistency", ok_lab and ok_146 and ok_rel
          and ok_rec and ok_notes,
          "r143 defines delta_1/y_t, r146 quotes the SAME quintuple as "
          "FULLGAP/y_t 'r143' (label drift); numerically identified: "
          "delta_1 vs FULLGAP strings rel dev < 4e-5; reciprocals match"
          " the CDXLIX y_t/FG strings to < 6e-4; CDL discloses the "
          "two-instruments-one-spectrum identification")


# ===================================================================== G15
def g15_bh4f4_builder() -> None:
    section("G15  BH4-F4: builder firewall closed by own reachability")
    res = []
    okall = True
    for fn, roots in (("radius4_an_probe.py",
                       ("build_cell", "c01_target", "maxflow")),
                      ("semilocal_realroot_limit_probe.py",
                       ("hp_zero_data", "build_trig_cell_hp",
                        "trig_profile"))):
        src = blob(fn)
        tree = ast.parse(src)
        funcs = {}
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                funcs[node.name] = node

        def owner_of(lineno):
            best = None
            for name, node in funcs.items():
                lo = node.lineno
                hi = max(getattr(n, "lineno", lo) for n in ast.walk(node))
                if lo <= lineno <= hi and (
                        best is None or lo > funcs[best].lineno):
                    best = name
            return best or "<module>"
        owners = {}
        for node in ast.walk(tree):
            nm = None
            if isinstance(node, ast.Attribute):
                nm = node.attr
            elif isinstance(node, ast.Name):
                nm = node.id
            if nm and nm.lower() in ("zeta", "load", "zeta" + "zero",
                                     "siegel" + "z", "n" + "zeros",
                                     "gram" + "point"):
                owners.setdefault(nm.lower(), set()).add(
                    owner_of(node.lineno))
        bad_zeta = [o for o in owners.get("zeta", ())
                    if not o.startswith("audit_")]
        bad_load = [o for o in owners.get("load", ())
                    if not o.startswith("ward_")]
        bad_oracle = [k for k in owners
                      if k in ("zeta" + "zero", "siegel" + "z",
                               "n" + "zeros", "gram" + "point")]
        calls = {}
        for name, node in funcs.items():
            cs = set()
            for n in ast.walk(node):
                if isinstance(n, ast.Call):
                    f = n.func
                    if isinstance(f, ast.Name):
                        cs.add(f.id)
                    elif isinstance(f, ast.Attribute):
                        cs.add(f.attr)
            calls[name] = cs & set(funcs)
        reach_bad = []
        for root in roots:
            if root not in funcs:
                continue
            seen = {root}
            stack = [root]
            while stack:
                u = stack.pop()
                for v in calls.get(u, ()):
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
            for f in seen:
                if any(f in v for v in owners.values()):
                    reach_bad.append("%s<-%s" % (f, root))
        okall = okall and not bad_zeta and not bad_load \
            and not bad_oracle and not reach_bad
        res.append("%s: zeta %s load %s oracle %s reach %s"
                   % (fn.split("_probe")[0],
                      sorted(owners.get("zeta", ())) or "-",
                      sorted(owners.get("load", ())) or "-",
                      bad_oracle or "-", reach_bad or "-"))
    l1 = blob("l1_weyllaw_probe.py")
    scope_note = "firewall_audit" in l1 and "os.path.abspath(__file__)" \
        in l1
    check("G15-F4-builder-clean", okall and scope_note,
          "; ".join(res) + " -- builder consumes Lambda/arch/pole only "
          "(reachability, own scan); r131's G01 scans only its own file"
          " (the NOTE), claim itself TRUE")


# ===================================================================== G16
def g16_landau() -> None:
    section("G16  LANDAU PINS RECOMPUTED (cache; r137 G37 strings)")
    gam = ward_cache()
    gtop = float(gam[-1])
    res = []
    ok = True
    for x, zfro in ((5, 0.17), (13, -0.10), (18, 1.00)):
        A = math.log(x) / 2
        K = int(math.ceil(1.25 * x * math.log(x)))
        om = (K - 1) * math.pi / A
        sel = gam[(gam > om) & (gam <= gtop)]
        cm = math.fsum(math.cos(g * math.log(x)) / g ** 2 for g in sel)
        lam = 0.0
        pp = {5: math.log(5), 13: math.log(13)}
        lam = pp.get(x, 0.0)
        cp = -lam / (2 * math.pi * math.sqrt(x)) * (1 / om - 1 / gtop)
        sig = math.sqrt(math.fsum(g ** -4 for g in sel) / 2)
        z = (cm - cp) / sig
        res.append("x%d z %+0.2f (frozen %+0.2f)" % (x, z, zfro))
        ok = ok and abs(z - zfro) <= 0.05
    check("G16-landau-pins", ok, "; ".join(res)
          + " -- own cache sums, own C_pred = -Lambda(x)/(2 pi sqrt x)"
          "(1/om - 1/gtop), own sigma")


# ===================================================================== G17
def dinic(edges: dict, s: str, t: str) -> int:
    from collections import deque
    nodes = set()
    for (u, v) in edges:
        nodes.add(u)
        nodes.add(v)
    cap = {}
    adj = {n: set() for n in nodes}
    for (u, v), c in edges.items():
        cap[(u, v)] = cap.get((u, v), 0) + c
        cap.setdefault((v, u), 0)
        adj[u].add(v)
        adj[v].add(u)
    flow = 0
    while True:
        lvl = {s: 0}
        dq = deque([s])
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                if v not in lvl and cap[(u, v)] > 0:
                    lvl[v] = lvl[u] + 1
                    dq.append(v)
        if t not in lvl:
            return flow
        it = {n: iter(sorted(adj[n])) for n in nodes}

        def dfs(u, f):
            if u == t:
                return f
            for v in it[u]:
                if cap[(u, v)] > 0 and lvl.get(v, -1) == lvl[u] + 1:
                    d = dfs(v, min(f, cap[(u, v)]))
                    if d > 0:
                        cap[(u, v)] -= d
                        cap[(v, u)] += d
                        return d
            return 0
        while True:
            f = dfs(s, 10 ** 9)
            if f == 0:
                break
            flow += f


def g17_mincut() -> None:
    section("G17  MIN-CUT FLOWS (own Dinic on re-encoded frozen graphs)")
    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    fb = dinic(dict(base), "UNC", "RH")
    # r131 refined
    e131 = dict(base)
    e131.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                 ("NFCLOS", "L1TAILPROVEN"): INF,
                 ("L1TAILPROVEN", "L1BAND"): 1,
                 ("L1BAND", "WPDN"): 1, ("WPDN", "R4HYP"): INF})
    f131 = dinic(dict(e131), "UNC", "RH")
    c131 = dict(e131)
    c131[("L1TAILPROVEN", "L1BAND")] = INF
    f131g = dinic(dict(c131), "UNC", "RH")
    # r148 (verbatim re-encode of fullgap_onset S9)
    e148 = dict(base)
    e148.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                 ("NFCLOS", "L1TAILPROVEN"): INF,
                 ("L1TAILPROVEN", "TOPROOT"): 1,
                 ("TOPROOT", "TAILVISTHM"): INF,
                 ("TAILVISTHM", "TLAWCAP"): 1,
                 ("TLAWCAP", "ONSETCAPTHM"): INF,
                 ("ONSETCAPTHM", "CNTFLOORTHM"): INF,
                 ("CNTFLOORTHM", "BANDMASSTHM"): INF,
                 ("BANDMASSTHM", "SUSCAP2R"): 1,
                 ("SUSCAP2R", "DELTA1FLOOR"): 1,
                 ("DELTA1FLOOR", "FULLGAPTHM"): INF,
                 ("FULLGAPTHM", "QSUBGAPTHM"): INF,
                 ("QSUBGAPTHM", "PFLOORTHM"): INF,
                 ("PFLOORTHM", "COUNTEQTHM"): INF,
                 ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                 ("SEEDBALLTHM", "SPACREMTHM"): INF,
                 ("SPACREMTHM", "DOMASYM"): INF,
                 ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f148 = dinic(dict(e148), "UNC", "RH")
    o148 = dict(e148)
    o148[("TOPROOT", "TAILVISTHM")] = INF
    f148o = dinic(dict(o148), "UNC", "RH")
    cf148 = dict(base)
    cf148.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                  ("NFCLOS", "TOPROOT"): 1, ("TOPROOT", "R4HYP"): INF,
                  ("NFCLOS", "TLAWCAP"): 1, ("TLAWCAP", "R4HYP"): INF,
                  ("NFCLOS", "SUSCAP2R"): 1,
                  ("SUSCAP2R", "R4HYP"): INF})
    f148c = dinic(dict(cf148), "UNC", "RH")
    # r141 contracted chain (EPSLOCK -> SUSCAP2R)
    e141 = dict(base)
    e141.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                 ("NFCLOS", "L1TAILPROVEN"): INF,
                 ("L1TAILPROVEN", "EPSLOCK"): 1,
                 ("EPSLOCK", "SUSCAP2R"): 1,
                 ("SUSCAP2R", "QSUBGAPTHM"): INF,
                 ("QSUBGAPTHM", "SPACREMTHM"): INF,
                 ("SPACREMTHM", "DOMASYM"): INF,
                 ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f141 = dinic(dict(e141), "UNC", "RH")
    o141 = dict(e141)
    o141[("L1TAILPROVEN", "EPSLOCK")] = INF
    f141o = dinic(dict(o141), "UNC", "RH")
    cf141 = dict(base)
    cf141.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                  ("NFCLOS", "EPSLOCK"): 1, ("EPSLOCK", "R4HYP"): INF,
                  ("NFCLOS", "SUSCAP2R"): 1,
                  ("SUSCAP2R", "R4HYP"): INF})
    f141c = dinic(dict(cf141), "UNC", "RH")
    check("G17-mincut-own-dinic",
          fb == 4 and f131 == 5 and f131g == 5 and f148 == 5
          and f148o == 5 and f148c == 7 and f141 == 5 and f141o == 5
          and f141c == 6,
          "base 4; r131 refined 5 / grant 5; r141 refined 5 / grant 5 /"
          " parallel-counterfactual 6; r148 refined 5 / TOPROOT-grant 5"
          " / parallel-counterfactual 7 -- the 4/5/5/7 quadruple and "
          "its per-round variants all reproduce on an own Dinic")


# ===================================================================== G18
def g18_o1a_off() -> None:
    section("G18  O1a CELL BUDGET RECOUNT + OFF IDENTITY")
    x0, x1 = 5.0, 5.0 * math.e

    def is_pp(n: int) -> bool:
        for p in range(2, n + 1):
            if n % p == 0:
                while n % p == 0:
                    n //= p
                return n == 1
        return False
    pps = [n for n in range(6, int(x1) + 1) if is_pp(n)]
    dK = int(math.ceil(1.25 * x1 * math.log(x1))) \
        - int(math.ceil(1.25 * x0 * math.log(x0)))
    cells = 1 + len(pps) + dK
    budget = 2 + math.e * x0 + 1.25 * math.e * x0 * (math.log(x0) + 1) + 1
    ok1 = (pps == [7, 8, 9, 11, 13] and dK == 34 and cells == 40
           and 60.8 < budget < 61.0 and cells <= budget)
    # OFF identity: e^A == sqrt(x); 8 e^A ENV^2 G == 8 sqrt(x)
    # (1+eta)^2 A0^2 G with ENV = |A0|(1 + eta), eta = ENVres/|A0|
    with mp.workdps(30):
        okA = all(abs(mp.exp(mp.log(x) / 2) - mp.sqrt(x)) < mp.mpf("1e-25")
                  for x in (3, 5, 8, 13, 18, 24, 28))
        a0, envres = mp.mpf("4.733e-8"), mp.mpf("5.1e-14")
        env = a0 + envres
        eta = envres / a0
        ok_off = abs(8 * env ** 2 - 8 * (1 + eta) ** 2 * a0 ** 2) \
            < mp.mpf("1e-40")
    check("G18-o1a-off", ok1 and bool(okA and ok_off),
          "prime powers in (5, 5e] = %s (5), Delta K = %d (45 - 11), "
          "cells 1+5+34 = %d <= budget %.1f (CDLII: 40 <= 60.9); "
          "e^A == sqrt(x) exact on the ladder; OFF form r131 (8 e^A "
          "ENV^2 G) == r140 (8 sqrt x (1+eta)^2 A0^2 G) exact"
          % (pps, dK, cells, budget))


# ===================================================================== G19
def g19_string_continuity() -> None:
    section("G19  CROSS-ROUND STRING CONTINUITY (tau/A0/FULLGAP/QSUBGAP)")
    l1log = blob("l1_weyllaw_probe.run1.log")
    ep = re.sub(r"\s+", " ", blob("epslock_probe.py"))
    jl = blob("jetlock_bandmass_probe.py")
    fs_log = blob("fullgap_spectrum_probe.run1.log")
    fo_log = blob("fullgap_onset_probe.run3.log")
    ok_tau = ("tau 3.056e-07" in l1log and "3: 3.05582e-7" in ep
              and "5: 1.60658e-16" in ep and "5: 1.60658e-16" in jl
              and "28: 5.32373e-128" in jl
              and "tau=1.8456e-108" in fo_log)
    ok_a0 = ("A0 1.84e-03" in l1log and "A0 4.73e-08" in l1log
             and "5: 4.733e-8" in jl and "8: 8.419e-15" in jl
             and "13: 8.168e-27" in jl)
    ok_fg = ("FULLGAP 2.225493e+05" in fs_log
             and "FULLGAP=2.225493e+05" in fo_log
             and "FULLGAP=1.651310e+08" in fo_log)
    qs = blob("qsubgap_probe.py")
    ok_qs = "33.7/16.8/22.7/16.6/19.6" in qs
    check("G19-string-continuity", ok_tau and ok_a0 and ok_fg and ok_qs,
          "tau strings r131-log == r137/r140 dicts (incl. x28 "
          "5.32373e-128 == r148 log); A0 strings r131-log == r140 "
          "dict; FULLGAP strings r146-log == r148-log; QSUBGAP "
          "quintuple pinned in r139")


# ===================================================================== G20
def g20_newest_layer() -> None:
    section("G20  W3/Y2 INTERLACING + O2a/O3a/O3b + T1 (own instances)")
    # W3 (Cauchy interlacing) + Y2 (tightness transfer) on an instance
    with mp.workdps(40):
        lam = [mp.mpf(1), mp.mpf(2), mp.mpf(5), mp.mpf(7)]
        M = mp.diag(lam)
        # V = kernel of r = (0, 1, 1, 1) joined with ground e_1 in V
        # orthonormal basis of V: e_1, (0,1,-1,0)/sqrt2, (0,1,1,-2)/sqrt6
        b2 = [mp.mpf(0), 1 / mp.sqrt(2), -1 / mp.sqrt(2), mp.mpf(0)]
        b3 = [mp.mpf(0), 1 / mp.sqrt(6), 1 / mp.sqrt(6),
              -2 / mp.sqrt(6)]
        B = [[mp.mpf(1), mp.mpf(0), mp.mpf(0)],
             [mp.mpf(0), b2[1], b3[1]],
             [mp.mpf(0), b2[2], b3[2]],
             [mp.mpf(0), b2[3], b3[3]]]
        Wc = mp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                Wc[i, j] = sum(B[r][i] * lam[r] * B[r][j]
                               for r in range(4))
        qs, _ = mp.eigsy(Wc)
        qs = sorted(qs)
        ok_w3 = all(lam[i] - mp.mpf("1e-30") <= qs[i]
                    <= lam[i + 1] + mp.mpf("1e-30") for i in range(3))
        # Y2: psi_1 = e_2 (lam_1 = 2), eps^2 = |(I - P_V) e_2|^2
        pv = [sum(B[1][c] * B[r][c] for c in range(3)) for r in range(4)]
        eps2 = 1 - sum(v * v for v in pv)
        ok_y2 = qs[1] - lam[1] <= eps2 * (lam[3] - lam[1]) / (1 - eps2) \
            + mp.mpf("1e-30") and qs[1] >= lam[1] - mp.mpf("1e-30")
    # O2a Markov visibility (exact rationals; cos 2t = 1 - 2 sin^2 t)
    s2 = [Fraction(1, 100), Fraction(9, 10), Fraction(4, 10),
          Fraction(1, 200), Fraction(7, 10), Fraction(1, 2),
          Fraction(3, 5)]
    eps2f = Fraction(1, 50)
    m = len(s2)
    S_C = sum(1 - 2 * s for s in s2)
    nbad = sum(1 for s in s2 if s < eps2f)
    nvis = m - nbad
    ok_o2a = nvis >= (m * (1 - 2 * eps2f) - S_C) / (2 - 2 * eps2f)
    # O3a/O3b (exact rationals)
    Mb, Mo, V, A0s, G = (Fraction(1, 10), Fraction(2, 10),
                         Fraction(3, 100), Fraction(4), Fraction(5))
    Mbe = V * A0s
    tot = Mb + Mo + Mbe
    th = (Mb + Mo) / tot
    ok_o3a = 1 - th >= V * A0s / tot
    Pp = tot / (A0s * G)
    ok_o3b = 1 - th >= V / (Pp * G)
    # T1 window counting on the cache
    gam = ward_cache()
    ok_t1 = True
    for T in (500.0, 1000.0, 3000.0):
        rho = math.log(T / (2 * math.pi)) / (2 * math.pi)
        Ls = (1 + 2 * q_hsw(T + 40)) / rho
        cnt = int(np.sum((gam > T) & (gam <= T + Ls)))
        ok_t1 = ok_t1 and Ls < 40 and cnt >= 1 \
            and cnt >= Ls * rho - 2 * q_hsw(T + Ls)
    check("G20-newest-layer", bool(ok_w3 and ok_y2) and ok_o2a
          and ok_o3a and ok_o3b and ok_t1,
          "W3 Cauchy interlacing q_i in [lam_i, lam_i+1] on the "
          "codim-1 instance; Y2 tightness transfer bound holds; O2a "
          "Markov visibility exact in Q; O3a/O3b assembly + currency "
          "invariance exact in Q; T1: every L*(T) window at T = 500/"
          "1000/3000 holds >= 1 cache zero with the RvM-HSW floor "
          "(L* < 40)")


# ===================================================================== main
def main() -> int:
    print("bughunt4_probe -- PRIME.BUGHUNT4.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("adversarial audit of rounds 131-148; NO RH CLAIM.")
    g01_firewall()
    g02_numerals()
    g03_spec_sha()
    g04_rescue_diffs()
    g05_hsw_citations()
    g06_hsw_independent()
    g07_secular()
    g08_sumrules()
    g09_pinch_loop()
    g10_theorems_meta()
    g11_gw_pinning()
    g12_bh4f1()
    g13_bh4f2()
    g14_bh4f3_lock()
    g15_bh4f4_builder()
    g16_landau()
    g17_mincut()
    g18_o1a_off()
    g19_string_continuity()
    g20_newest_layer()

    section("FINDINGS + COMPOSITE")
    nmaj = sum(1 for _i, s, _d in FINDINGS if s == "MAJOR")
    nmin = sum(1 for _i, s, _d in FINDINGS if s == "MINOR")
    nnot = sum(1 for _i, s, _d in FINDINGS if s == "NOTE")
    for fid, sev, d in FINDINGS:
        print("  %s [%s] %s" % (fid, sev, d))
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    dt = time.time() - START
    print("\n" + "=" * 78)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: BUGHUNT4-FINDINGS(%d) = %d MAJOR / %d MINOR / "
          "%d NOTE" % (len(FINDINGS), nmaj, nmin, nnot))
    print("NO ROUND VERDICT FLIPS.  NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
