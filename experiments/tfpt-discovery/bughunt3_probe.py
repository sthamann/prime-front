#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bughunt3_probe -- PRIME.BUGHUNT3.01

FROZEN SPEC (2026-08-16).  EXPLORATION ONLY.  Adversarial audit of the
discovery rounds 110-129 corpus (probes resolvent_closure /
surface syncs / blockreal / stage1_construction / idgraph /
radius4_reduction / kr4_depth / coupling_ansatz / kr4_defectjet /
irwall / radius4_an / epstein_collapse / cluster_mixing / driver_cert
/ selection / lean4 radius4 modules / doublelimit_proof /
selfdual_construction; notes CDX-CDXXXI; promoted modules v916/v917).
This probe writes NOTHING but stdout, reads the frozen corpus
READ-ONLY (sources + run*.log evidence files), imports NO frozen
probe (every recompute below is an independent implementation), and
makes NO RH CLAIM in either direction.  Every confirmed finding
carries at least one falsifiable gate.

METHOD (bughunt I/II standard): (B1) the load-bearing theorems of
rounds 128/129 re-derived and attacked on exact adversarial
instances (Theorem R with C >> 1, signed defects, complex finite
pairs, r -> 4 boundary, edge-supported equality; the interior no-go
floor + moment monotonicity; the C0k <-> jet dictionary against the
round-102/106 Pascal machinery on exact rationals); (B2) the
promoted pair v916/v917 recomputed INDEPENDENTLY from raw lattice
counts (own r_Q, own Lambda_Q recursion, own g_Q, own row, own
Szego, own eigenvector certificate; own Euler-region bound with a
4-decade convergence ladder; own xi_Q evaluator repolishing the
driver passport); (B3) the localization exclusion argument of v917
stress-tested on its census-blind strip; (B4) cross-round number and
attribution consistency (t_death round labels, 4w(gamma_1) wards,
driver passport, min-cut replicas, note numerals); (B5) claim-drift
on the notes (Markov class label, "pre-declared" wording, Pascal
cell naming).

=======================================================================
FINDINGS LEDGER (the deliverable; severity frozen; gates named)
=======================================================================
BH3-F1 [MINOR][round-misattribution]  Round 129 attributes the
  Szego collapse scale t_death = 2.988 to "round-124" -- twice in
  selfdual_construction_probe.py (docstring "the round-124 in-window
  collapse scale" + gate G34 text "round-124 t_death = 2.988") and
  twice in note CDXXXI ("r124-t_death").  The collapse is ROUND 123
  (epstein_collapse_probe, note CDXXIV): driver_cert_probe (round
  125) says "round 123" / "t = 2.988 (round 123)" throughout, the
  promotion note CDXXVIII and v916 assign rounds 123/125, and round
  124 is the cluster-mixing round (note CDXXV; selection_probe cites
  "round 124" for cluster_mixing).  The NUMBER 2.988 is right
  everywhere (and independently reproduced here, G10); only the
  round label in round 129 is wrong.  GATE: G04 (grep conjunction on
  both sides).
BH3-F2 [MINOR][promoted-number-label]  The "Euler-region bound
  B(1.6)" carries three different values across promoted surfaces
  for the same named constant, and v916 mislabels its value: v916
  pins PIN_EULER_BOUND = 0.664 commented "sum_{n>=4} r_Q(n) n^-1.6 /
  r_Q(1)" and its D1 gate calls it the "pinned full-table value";
  v917 carries 0.650 ("Euler bound 0.650 < 1").  RECOMPUTED here
  from an own lattice sieve on a 4-decade ladder (N = 4e3..4e6, all
  totals agree to 6 digits): the true full sum is 0.645728.  Both
  corpus values are TRUNCATION reads plus the crude declared Abel
  tail 6 s/(s-1) N^{1-s}: 0.664 = N=20000 read (epstein_collapse
  G21), 0.650 = N=200000 read (driver_cert G26) -- valid UPPER
  BOUNDS, so every "< 1" conclusion stands; but 0.664 is NOT the
  full-table value of the sum, and the same named constant differs
  across the two promoted modules without a truncation label.
  GATE: G11 (own 4-decade recompute + exact reproduction of both
  corpus reads from one lattice).
BH3-F3 [MINOR][promoted-argument-gap]  v917's FIRE-LOCALIZED
  exclusion premise "every off-line zero below 45 is located, so
  unknown off-line zeros have gamma > 45 and delta <= 1.1" is
  STRONGER than what the census instruments certify: the off-line
  winding boxes have Re >= 0.51 (delta >= 0.01) and Im >= 0.1, and
  the line-straddling box [0.35, 0.65] runs only over the band
  (7.90, 31.40) -- the strips delta in (0, 0.01) with gamma in
  (0.1, 7.9) u (31.4, 45), and gamma < 0.1 at any delta, are
  census-blind.  A worst-case hidden zero there contributes up to
  ~1.3e-3 in MAGNITUDE to the depth difference at m = 15 -- 21x
  ABOVE B_out(15) = 6.0e-5 -- so B_out as stated does not bound the
  blind strip.  THE VERDICT SURVIVES on a repair argument gated
  here: (i) every blind-strip zero has |v(a0)| < 1 (max 0.6539
  measured on the region boundary; any zero with |v(a0)| > 1 needs
  a0 inside its violation window, whose half-width <= ~2 delta gamma
  <= 0.9 forces gamma ~ sqrt(a0) = 15.67 INSIDE the band, where the
  straddling winding box IS complete), and (ii) the blind-strip
  contribution to the diff d'_m - d'_{m-1} is STRICTLY NEGATIVE for
  every certified m <= 32 wherever |v| >= 0.1 (phase within
  pi +- 0.55 there), and where |v| < 0.1 any positive contribution
  is < 1e-40 -- 35 orders below the certified margins: hidden zeros
  can only MASK the fire, never fake it.
  Recommended correction to the v917 text: state the census premise
  as delta >= 0.01 + band-straddle completeness + the window-width
  argument, not "every off-line zero below 45".  GATE: G12 (blind-
  region scan: |v| < 1, phase/sign, magnitude vs pinned B_out(15)).
BH3-F4 [MINOR][note-class-overstatement]  Note CDXXVII (round 126)
  types the poly-filter no-go as "(a) POLYFILTER/ENERGIE {p(Q),
  deg <= d}: split <= 2d^2 gap/(M-m) BEWIESEN ... das r124-Krylov/
  Rayleigh-Scheitern in Satzform" -- dropping the load-bearing
  hypothesis (|p| <= 1 on the spectral hull INTERVAL) that the
  probe itself states.  Without it the class is NOT closed: a
  degree-(K-1) Lagrange interpolant with |p(E_i)| <= 1 at every
  eigenvalue (operator norm ||p(Q)|| = 1) splits any doublet
  COMPLETELY at polynomial-in-K degree (counterexample gated:
  gap 1e-12, split 2.0, K = 12); adaptive (Krylov-type) filters
  escape the DEGREE bound and pay in PRECISION instead -- which the
  probe prices separately (its own f64-pipeline gate measures
  sector selection f64-cheap).  The probe's hypothesis-carrying
  statement and its Markov citation are correct; only the note's
  class label overstates.  GATE: G13 (explicit counterexample +
  Markov bound verified under the hull hypothesis on the same
  instance + grep pin).
BH3-F5 [NOTE][naming-collision]  doublelimit_proof_probe L0(iii)
  defines C_{0,k} := sum_pairs w^k and calls these "the round-106
  Pascal-diagonal cells in closed jet form".  In the corpus's own
  Pascal-field convention (round 102/117: cells C_{n,k} = sum
  y^{n+1} (1-y)^k from b_n = sum y^{n+1}; DIAGONAL d_m = C_{m,m} =
  sum y w^m, radius4_reduction_probe line ~24) the object
  sum w^k = sum y^k (1-y)^k is the SUB-diagonal cell C_{k-1,k};
  the names coincide only at k = 1 (C_{0,1} = sum w both ways,
  which is how the collision crept in).  The probe's own dictionary
  (its G14) is correct for ITS defined object; the label is wrong
  for k >= 2.  GATE: G14 (exact-rational: sum w^k == cell(k-1,k),
  != cell(0,k), != cell(k,k) for k = 2,3, on the same instance that
  verifies the full C0k <-> jet dictionary).
BH3-F6 [NOTE][mincut-replica-label]  Round 129's S6 min-cut calls
  its base graph "the frozen round-116 replica (4 parallel
  capacity-1 omega edges)" -- but its base {PICKFLOORS, HANKEL,
  LANEACONV, OMEGA4} contains the LANEACONV edge, which rounds
  122/124/126/128 book as the FIFTH omega on top of the round-116
  four (their flows 4 -> 5; the canonical round-116 graph
  idgraph_search_probe.EDGES has HAUS-CELLS/PICK-FLOORS/
  DIAG-BOUNDS/WEYL-PINS and NO LANEACONV).  Rounds 123/125 use the
  canonical IG graph and correctly read 4/4.  Per-graph flows are
  all right (gated here on own Edmonds-Karp replicas: 4 / 5 / 4);
  only round 129's "round-116 replica" label and the cross-round
  comparability of its "extended flow 4" vs rounds 122/128's
  "extended flow 5" are off.  No verdict rides on it.  GATE: G15
  (three replica flows + edge-census greps).
BH3-F7 [NOTE][pre-declaration-wording]  Note CDXXVIII and v916 call
  G18/G19/G21 of the collapse probe "the three PRE-DECLARED
  falsified" gates ("exakt die drei VORDEKLARIERT falsifizierten
  Gates G18/G19/G21"; v916: "the pre-declared failure pattern of
  G18/G19/G21").  The falsifications of G18 and G21 were literally
  declared in advance (collapse AMENDMENT 1, blocks (f)/(g):
  "EXPECTED TO READ FALSIFIED"); G19's failure (law miss 0.505 >
  0.5) was NOT pre-declared anywhere -- P5 was a pre-registered
  prediction whose failure emerged only in the full run (the smoke
  read 2.988 vs the r120-law 2.81 was INSIDE the 0.5 bar; the refit
  prediction 2.483 that broke it came from the full plant ladder).
  Wording precision only; the failing gates were carried, never
  smoothed.  GATE: G16 (grep conjunction: AMENDMENT 1 pre-declares
  exactly G18/G21; v916 wording covers G19).

CHECKED CLEAN (adversarially, no finding): THEOREM R re-derived
end-to-end and attacked -- the k = 1 term of the domination needs
d_1 >= 0, which WPD itself forces (a negative d_1 makes WPD
unsatisfiable; logic gated), the true-side log-series convergence
under WPD holds because a finite exceptional multiset with |w| > 1/4
would make limsup |C0k|^{1/k} = max|w| > 1/4 (nonvanishing power
sums; Vandermonde) contradicting |C0k| <= 4^{1-k}(TrB + C d1); the
sandwich bound verified on an exact adversarial instance with
C_meas = 40.7 >> 1 (complex finite pair, signed defects) on a t-grid
through 3.999, and the Lemma-S equality case (edge-supported defect
at w = 1/4 exactly: d_k 4^{k-1} = d_1 for ALL k) is sharp as
claimed; Lemma X's counterexample and Lemma N's Vitali/Cauchy chain
re-derived; the C0k <-> jet dictionary verified END-TO-END on exact
rationals (sympy: 3-pair world, exact log-Phi derivatives ->
S_m = (-1)^{m-1} m c_m -> binomial dictionary == direct sum w^k,
k <= 5) and against the Pascal machinery (G14); the round-129
interior no-go is watertight in its stated (bounded-Theta) scope --
Theta + Theta* = I forces W = 1/4 + S*S >= 1/4 (re-gated exactly),
spec(4W) in [1, inf) makes 4^m phi(W^m) non-decreasing for EVERY
positive functional (operator monotonicity gated on instances), and
the no-go needs only the m = 0, 1 moments against the certified
margins 1.8347/2.7482/4.5028 (grep-pinned from the run of record):
no quantifier slip -- any state reproducing just d'_0 and d'_1
(even to within margin/2) is excluded; the note honestly scopes to
"beschraenkte" families (the algebra in fact extends to closed
unbounded Theta, so the restriction is conservative, not load-
bearing); the matched-pin inversion algebra re-derived in sympy
matches the round-127 Lean lemma set (matched_y / weight sum 1 /
matched_v = 1 + eps real / partner rigidity / on-line w <= 1/4);
the v916 collapse headline reproduced INDEPENDENTLY from raw
lattice counts to 9 significant digits (own t_death = 2.988 at
k = 996; own lambda_min(T_996) > 0 > lambda_min(T_998); own
V(1038) = -1.9697494679e-2 vs pin -1.9697494668e-2) with an own
error-budget check; the Lambda_Q recursion re-derived (Dirichlet
algebra) and Euler-warded on ideal counts with an own
implementation; the band-peel completeness logic is sound as a
FALSIFIABLE design (a hidden band pair breaks the 15==15 / 2==2
equalities rather than faking them; the straddling box [0.35,0.65]
closes the near-line strip INSIDE the band); m_2 = ln2 gamma^2/
delta^2 = 907.7 in [900, 916] rechecked; the driver passport
0.9329696975 + 15.6682495313i repolished from a coarse seed with an
OWN incomplete-gamma xi_Q evaluator (dev < 1e-8) and consistent
across rounds 123/125/128-note/129; the round-117 window formula
re-derived: the driver window contains both a* and 256, the witness
window (1308.9, 1337.5) reproduced; the ward values 4w(gamma_next)
= 0.973665070 / 0.984791384 / 0.994603870 at a = 144/256/512
recomputed from the literal cache ordinates (gamma_next = the
ordinate nearest sqrt(a): gamma_1, gamma_1, gamma_2) and
grep-matched across rounds 118/120/129; the irwall
coupled-schedule bookkeeping (Omega_r = 25
T_r/T_0, ell_r = 0.8 log(T_0/2pi)/log(T_r/2pi), dtau_r = 0.01875
ell_r) recomputed against the run-of-record rung table; the
round-124 KFAC ladder comparison is apples-to-apples (unit-
normalized beta per frame with per-frame alpha/two-vector residual
printed; the x^-2.8 matched-enriched-frame law recomputed from the
logged ladder: slopes 2.89/2.70); the round-126 block-collapse
identity s01(Mprime) == s01(Mpole+March) is a disclosed one-line
consequence of doublet orthogonality (the probe derives it as such;
"zero extra selection information on the doublet" is the fair
reading; the 1e-161 residual is arithmetic confirmation of algebra,
correctly typed exact, no retyping needed); the round-122 Z1
verdict (TRANSCRIBING-IN-BAND, median ratios ~0) is carried
honestly and re-typed by round 128 (G38) with the source-side proof
marked open -- not upgraded anywhere; note numerals CDVII..CDXXXI
are gap-free and strictly consecutive (parsed + gated), and the
promotion notes CDXXI/CDXXVIII correctly interleave without
disturbing the round <-> numeral offset.

NO ROUND VERDICT FLIPS.  No number in v916/v917 is wrong; the four
MINOR findings are label/attribution/argument-scope repairs on
promoted or note surfaces.  COMPOSITE: BUGHUNT3-FINDINGS(7) =
0 MAJOR / 4 MINOR / 3 NOTE.  NO RH CLAIM.
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
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
START = time.time()

CHECKS: list[tuple[str, bool, str]] = []
FINDINGS = [
    ("BH3-F1", "MINOR", "r129 says 'round-124 t_death'; collapse is r123"),
    ("BH3-F2", "MINOR", "B(1.6): v916 0.664 'full-table' vs v917 0.650 vs "
                        "true 0.6457 (all upper bounds; label wrong)"),
    ("BH3-F3", "MINOR", "v917 census premise overreach (blind strip "
                        "delta<0.01); verdict survives via window-width + "
                        "sign argument"),
    ("BH3-F4", "MINOR", "CDXXVII poly-filter class label omits hull "
                        "normalization; Lagrange escapes at degree K-1"),
    ("BH3-F5", "NOTE", "doublelimit calls sum w^k 'Pascal-diagonal cells' "
                       "(it is the C_{k-1,k} sub-diagonal)"),
    ("BH3-F6", "NOTE", "r129 min-cut base mislabeled 'round-116 replica' "
                       "(contains the r122 LANEACONV fifth edge)"),
    ("BH3-F7", "NOTE", "'pre-declared falsified' wording covers G19 whose "
                       "failure was not pre-declared (only G18/G21 were)"),
]


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 78 + "\n" + title + "\n" + "=" * 78, flush=True)


def blob(name: str) -> str:
    with open(os.path.join(HERE, name), encoding="utf-8",
              errors="replace") as fh:
        return fh.read()


REPO = os.path.abspath(os.path.join(HERE, "..", ".."))


def blob_repo(rel: str) -> str:
    with open(os.path.join(REPO, rel), encoding="utf-8",
              errors="replace") as fh:
        return fh.read()


# ===================================================================== G01
def g01_firewall() -> None:
    section("G01  SELF-FIREWALL (stdout only; no frozen-probe import)")
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    writers = []
    imports = []
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


# ===================================================================== G02/03
ROM = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def rom2int(s: str) -> int:
    t = 0
    for i, ch in enumerate(s):
        v = ROM[ch]
        t += -v if i + 1 < len(s) and ROM[s[i + 1]] > v else v
    return t


def g02_numerals() -> str:
    section("G02  NOTE-NUMERAL INTEGRITY (head of next.txt)")
    lines = blob_repo("experiments/next.txt").splitlines()
    seq = []
    for ln in lines[:80]:
        m = re.match(r"# 2026-\d\d-\d\d \(([IVXLCDM]+)\)", ln)
        if m:
            seq.append((m.group(1), rom2int(m.group(1)), ln))
    nums = [n for _r, n, _l in seq]
    lo = nums.index(407) if 407 in nums else len(nums)
    chain = all(nums[i] - 1 == nums[i + 1] for i in range(min(lo + 1,
                                                              len(nums) - 1)))
    check("G02-numeral-chain", len(nums) >= 20 and chain
          and 431 in nums and 417 in nums,
          "head numerals %s..%s strictly consecutive through CDVII "
          "(%d headers parsed): CDXVII..CDXXXI gap-free"
          % (seq[0][0], seq[min(lo, len(seq) - 1)][0], len(nums)))
    for r, n, ln in seq:
        if n == 431:
            return ln
    return ""


def g03_g04_round_attribution(cdxxxi_line: str) -> None:
    section("G03/G04  BH3-F1: t_death ROUND ATTRIBUTION")
    sd = blob("selfdual_construction_probe.py")
    dc = blob("driver_cert_probe.py")
    cm = blob("cluster_mixing_probe.py")
    v916 = blob_repo("verification/v916_epstein_weil_violation.py")
    sel = blob("selection_probe.py")
    check("G03-corpus-assigns-r123",
          "round-123 named lever" in dc
          and "t = 2.988 (round 123)" in dc
          and "round 123,\nnote CDXXIV" in v916.replace("\r", "")
          or ("round 123" in v916 and "CDXXIV" in v916
              and "round-123" in dc),
          "driver_cert (r125) + v916 provenance both assign the collapse "
          "to round 123 / note CDXXIV; cluster_mixing is round 124 "
          "(selection_probe cites 'round 124' %d times)"
          % sel.count("round 124"))
    mis = (sd.count("round-124 t_death") + sd.count(
        "round-124\n  in-window collapse scale"))
    mis_note = cdxxxi_line.count("r124-t_death")
    check("G04-F1-misattribution-pinned",
          "round-124 t_death" in sd and "round-124" in sd
          and mis_note == 2 and "PRIME.CCM.CLUSTER.MIXING" in cm,
          "selfdual probe carries 'round-124 t_death' (%d hits incl. "
          "G34 text) and note CDXXXI carries 'r124-t_death' twice -- "
          "both should read round 123" % max(mis, 1))


# ===================================================================== G05-07
def g05_theorem_r() -> None:
    section("G05  THEOREM R: ADVERSARIAL EXACT INSTANCE (C >> 1)")
    # true world: real w <= 1/4; finite world: shares two atoms, has a
    # COMPLEX conjugate pair (off-line-style, |4w| = 0.96 < 1) => signed
    # defects d_k, small d_1 > 0, WPD constant C_meas >> 1.
    with mp.workdps(60):
        w_true = [mp.mpf("0.2")] * 3 + [mp.mpf("0.05")]
        wc = mp.mpf("0.24") * mp.exp(1j * mp.pi / 3)
        w_fin_r = [mp.mpf("0.2")] * 2
        d = {}
        for k in range(1, 201):
            tr = sum(w ** k for w in w_true)
            fin = sum(w ** k for w in w_fin_r) + 2 * mp.re(wc ** k)
            d[k] = tr - fin
        d1 = d[1]
        cmeas = max(abs(d[k]) * mp.mpf(4) ** (k - 1) / d1
                    for k in range(2, 201))
        # geometric tail bound for k > 200:
        # |d_k| 4^{k-1} <= [4*(0.8)^k *? ] -- dominated by the 0.96 pair:
        tail = 2 * mp.mpf("0.96") ** 200 / 4 / d1 + \
            4 * mp.mpf("0.8") ** 200 / 4 / d1
        ok = d1 > 0 and cmeas > 10 and tail < cmeas
        worst = mp.mpf(0)
        for t in [mp.mpf(x) / 1000 for x in (500, 1500, 2500, 3500, 3900,
                                             3990, 3999)]:
            lt = sum(mp.log(1 - t * w) for w in w_true)
            lf = (sum(mp.log(1 - t * w) for w in w_fin_r)
                  + mp.log(abs(1 - t * wc) ** 2))
            lhs = abs(lf - lt)
            rhs = max(mp.mpf(1), cmeas) * (-4 * mp.log(1 - t / 4)) * d1
            worst = max(worst, lhs / rhs)
            ok = ok and lhs <= rhs
        check("G05-thmR-sandwich-adversarial", bool(ok),
              "d1 = %s, C_meas = %s >> 1 (k <= 200; k > 200 tail %s), "
              "|log(R_fin/R_true)| <= max(1,C)(-4log(1-t/4))d1 on the "
              "grid through t = 3.999 (worst lhs/rhs = %s)"
              % (mp.nstr(d1, 6), mp.nstr(cmeas, 6), mp.nstr(tail, 3),
                 mp.nstr(worst, 4)))

    # k=1 subtlety: WPD with d_1 < 0 is unsatisfiable (|d_k| >= 0 > C
    # 4^{1-k} d_1), so the domination |d_1| <= max(1,C) d_1 is implied.
    d1n = Fraction(-1, 100)
    unsat = all(Fraction(1, 10 ** 9) > Fraction(1) * 4 ** (1 - k) * d1n
                for k in range(2, 12))
    check("G06-thmR-k1-subtlety", unsat,
          "WPD RHS C 4^{1-k} d1 < 0 <= |d_k| whenever d1 < 0: the "
          "hypothesis itself forces d1 >= 0, closing the k = 1 term of "
          "the series domination (no hidden gap)")

    # Lemma S equality case: edge-supported defect at w = 1/4 exactly.
    wq = Fraction(1, 4)
    dks = [wq ** k for k in range(1, 13)]
    sharp = all(dks[k - 1] * Fraction(4) ** (k - 1) == dks[0]
                for k in range(1, 13))
    # Lemma X replication:
    a13 = [Fraction(1, 8)] * 2
    b13 = [Fraction(1, 16), Fraction(3, 16)]
    lemx = (sum(a13) == sum(b13)
            and sum(w ** 2 for w in a13) - sum(w ** 2 for w in b13)
            == Fraction(-1, 128))
    check("G07-lemmaS-sharp+lemmaX", sharp and lemx,
          "edge-supported defect (true {1/4 x5} vs fin {1/4 x4}): "
          "d_k 4^{k-1} == d_1 for all k <= 12 (Lemma S is SHARP at the "
          "edge); Lemma X counterexample exact ({1/8,1/8} vs "
          "{1/16,3/16}: d1 = 0, d2 = -1/128)")


def g08_jet_dictionary() -> None:
    section("G08/G14  C0k <-> JET DICTIONARY vs PASCAL MACHINERY (exact)")
    import sympy as sp
    a0 = sp.Integer(2)
    G2 = [sp.Integer(4), sp.Integer(9), sp.Integer(25)]   # g^2 rational
    z = sp.symbols("z")
    logphi = sum(sp.log(z + g2) for g2 in G2)
    ws = [a0 * (g2 + a0 - a0) / (g2 + a0) ** 2 for g2 in G2]
    ys = [a0 / (g2 + a0) for g2 in G2]
    ok_dict = True
    for k in range(1, 6):
        S = {}
        for m in range(1, 2 * k + 1):
            cm = sp.diff(logphi, z, m).subs(z, a0) / sp.factorial(m)
            S[m] = (-1) ** (m - 1) * m * cm
        c0k = a0 ** k * sum(sp.binomial(k, j) * (-a0) ** (k - j)
                            * S[2 * k - j] for j in range(k + 1))
        direct = sum(w ** k for w in ws)
        ok_dict = ok_dict and sp.simplify(c0k - direct) == 0
    check("G08-jet-dictionary-exact", ok_dict,
          "3-pair rational world (g^2 = 4, 9, 25; a = 2): C0k from exact "
          "log-Phi derivatives via S_m = (-1)^{m-1} m c_m + binomial "
          "dictionary == direct sum w^k, k = 1..5 (round-106 cross-check "
          "on exact rationals, as contracted)")

    def cell(n: int, k: int):
        return sum(y ** (n + 1) * (1 - y) ** k for y in ys)

    ok_f5 = True
    for k in (1, 2, 3):
        sw = sum(w ** k for w in ws)
        ok_f5 = ok_f5 and sp.simplify(sw - cell(k - 1, k)) == 0
        if k >= 2:
            ok_f5 = ok_f5 and sp.simplify(sw - cell(0, k)) != 0 \
                and sp.simplify(sw - cell(k, k)) != 0
    dl = blob("doublelimit_proof_probe.py")
    r4r = blob("radius4_reduction_probe.py")
    check("G14-F5-pascal-naming", ok_f5
          and "round-106 Pascal-diagonal cells" in dl
          and "C_{m,m}(a) = sum_rho y_rho w_a(z_rho)^m" in r4r,
          "sum w^k == Pascal cell C_{k-1,k} exactly; != C_{0,k} and "
          "!= diagonal C_{k,k} for k >= 2 (corpus convention b_n = sum "
          "y^{n+1}, diagonal = sum y w^m per radius4_reduction) -- the "
          "doublelimit label 'Pascal-diagonal cells' for sum w^k is a "
          "naming collision (its own math is self-consistent)")


def g09_matched_pin_and_nogo() -> None:
    section("G09  MATCHED-PIN ALGEBRA (r127 Lean set) + INTERIOR NO-GO")
    import sympy as sp
    de, ga, aa = sp.symbols("delta gamma a", positive=True)
    mu = de + sp.I * ga
    a0 = de ** 2 + ga ** 2
    y = sp.simplify(sp.expand_complex(a0 / (a0 - mu ** 2)))
    ok = sp.simplify(y - (ga + sp.I * de) / (2 * ga)) == 0
    ok = ok and sp.simplify(sp.expand_complex(y + sp.conjugate(y)) - 1) == 0
    v = sp.simplify(sp.expand_complex(4 * y * (1 - y)))
    ok = ok and sp.simplify(v - (1 + de ** 2 / ga ** 2)) == 0
    # partner rigidity + on-line bound (Lean wOnLine/partner set)
    zz = sp.symbols("z")
    wfun = -aa * zz / (aa - zz) ** 2
    ok = ok and sp.simplify(sp.together(
        wfun.subs(zz, aa ** 2 / zz) - wfun)) == 0
    gam = sp.symbols("g", positive=True)
    w_on = aa * gam ** 2 / (aa + gam ** 2) ** 2
    ok = ok and sp.simplify(sp.Rational(1, 4) - w_on
                            - (aa - gam ** 2) ** 2
                            / (4 * (aa + gam ** 2) ** 2)) == 0
    check("G09a-matched-pin-vs-lean", ok,
          "y* = (gamma + i delta)/(2 gamma); y* + conj = 1; v* = 1 + "
          "delta^2/gamma^2 exactly real; w(a^2/z) = w(z); 1/4 - w_on = "
          "(a-g^2)^2/(4(a+g^2)^2) >= 0 -- the round-127 Lean lemma set "
          "(matched_y/matched_weight_sum/matched_v/partner_w/"
          "wOnLine_le_quarter) re-derived independently")

    # interior no-go: W = 1/4 + S*S on an exact instance + monotonicity
    A3 = sp.Matrix(3, 3, lambda i, j: sp.Rational(i - j, 2 + i + j))
    S3 = A3 + sp.I * sp.Matrix(3, 3, lambda i, j: sp.Rational(1, 1 + i + j))
    S3 = (S3 - S3.conjugate().T) / 2     # exactly skew-adjoint
    Th = sp.eye(3) / 2 + S3
    W = sp.expand(Th * (sp.eye(3) - Th))
    okw = sp.simplify(W - (sp.eye(3) / 4
                           + S3.conjugate().T * S3)) == sp.zeros(3)
    # moment monotonicity for spec(4W) in [1, inf): any positive weights
    xs = [Fraction(1), Fraction(13, 10), Fraction(27, 10)]
    ph = [Fraction(1, 2), Fraction(3, 10), Fraction(1, 5)]
    mono = all(sum(p * x ** (m + 1) for p, x in zip(ph, xs))
               >= sum(p * x ** m for p, x in zip(ph, xs))
               for m in range(0, 25))
    log3 = blob("selfdual_construction_probe.run3.log")
    pins = all(t in log3 for t in
               ("d'_0 = 2.818185", "d'_1 = 0.983505",
                "d'_0 = 4.615536", "d'_1 = 1.867386",
                "d'_0 = 8.124053", "d'_1 = 3.621232"))
    marg = (2.818185 - 0.983505, 4.615536 - 1.867386, 8.124053 - 3.621232)
    okm = (abs(marg[0] - 1.8347) < 1e-3 and abs(marg[1] - 2.7482) < 1e-3
           and abs(marg[2] - 4.5028) < 1e-3)
    check("G09b-nogo-quantifier", bool(okw and mono and pins and okm),
          "Theta+Theta*=I => W = 1/4 + S*S (exact 3x3 skew instance); "
          "spec(4W) in [1,inf) => 4^m phi(W^m) NON-DECREASING for every "
          "positive functional (m <= 24 gated); the no-go needs ONLY "
          "m = 0,1 against the certified drops d'_0 -> d'_1 (run-of-"
          "record margins %.4f/%.4f/%.4f == note values): no quantifier "
          "slip, robust to margin/2 approximate reproduction" % marg)


# ===================================================================== G10-11
def own_collapse() -> dict:
    """Fully independent v916 recompute: own lattice, own Lambda_Q,
    own g_Q, own row, own Szego, own certificate."""
    NCUT, NROW = 40, 1100
    r = [0] * (NCUT + 1)
    b = 0
    while 5 * b * b <= NCUT:
        a = 0
        while a * a + 5 * b * b <= NCUT:
            q = a * a + 5 * b * b
            if q >= 1:
                r[q] += (2 if a else 1) * (2 if b else 1)
            a += 1
        b += 1
    with mp.workdps(40):
        lam = [mp.mpf(0)] * (NCUT + 1)
        for n in range(2, NCUT + 1):
            s = mp.mpf(0)
            for e in range(2, n):
                if n % e == 0:
                    s += lam[e] * r[n // e]
            lam[n] = (r[n] * mp.log(n) - s) / r[1]
        cQ = mp.euler + 2 * mp.log(2) - mp.log(mp.sqrt(20) / (2 * mp.pi))
        SQ0 = mp.pi ** 2 / 2

        def s_arch(t):
            if t == 0:
                return SQ0
            tot, k, zp = mp.mpf(0), 0, mp.exp(-t / 2)
            zf = mp.exp(-t)
            while True:
                term = zp / (k + mp.mpf(1) / 2) ** 2
                tot += term
                if term < mp.mpf("1e-35") * (1 + tot):
                    break
                zp *= zf
                k += 1
            return tot

        dl = mp.mpf("0.003")
        gv = []
        for j in range(NROW + 2):
            t = j * dl
            acc = -8 * (mp.cosh(t / 2) - 1) + cQ * t + s_arch(t) - SQ0
            for n in range(2, NCUT + 1):
                ln = mp.log(n)
                if ln < t and abs(lam[n]) > mp.mpf("1e-30"):
                    acc += lam[n] / mp.sqrt(n) * (t - ln)
            gv.append(acc)
        row = [float(-2 * gv[1] / dl)]
        for d in range(1, NROW + 1):
            row.append(float(-(gv[d - 1] - 2 * gv[d] + gv[d + 1]) / dl))
    row = np.array(row)
    rr = row / row[0]
    Phi = np.array([1.0])
    Phis = np.array([1.0])
    fail_k = -1
    for k in range(len(rr) - 1):
        num = float(np.dot(Phi, rr[1:k + 2]))
        den = float(np.dot(Phis, rr[0:k + 1]))
        if den <= 0 or abs(num / den) >= 1:
            fail_k = k
            break
        al = num / den
        zP = np.concatenate(([0.0], Phi))
        Ps = np.concatenate((Phis, [0.0]))
        Phi, Phis = zP - al * Ps, Ps - al * zP

    def lam_min(k: int) -> float:
        T = row[np.abs(np.subtract.outer(np.arange(k), np.arange(k)))]
        return float(np.linalg.eigvalsh(T)[0])

    kdag = -1
    for k in range(990, 1010):
        if lam_min(k) < 0:
            kdag = k
            break
    kc = 1038
    T = row[np.abs(np.subtract.outer(np.arange(kc), np.arange(kc)))]
    _w, V = np.linalg.eigh(T)
    x = V[:, 0]
    return {"r": r, "lam": lam, "fail_k": fail_k, "kdag": kdag,
            "V": float(x @ T @ x), "l996": lam_min(996),
            "l998": lam_min(998)}


def g10_collapse_recompute() -> None:
    section("G10  v916 HEADLINE: FULLY INDEPENDENT RECOMPUTE")
    t0 = time.time()
    oc = own_collapse()
    # own Euler ward: recursion on ideal counts == von Mangoldt (n<=60)
    CHI20 = {1: 1, 3: 1, 7: 1, 9: 1, 11: -1, 13: -1, 17: -1, 19: -1}
    N = 60
    tt = [0] * (N + 1)
    for dv in range(1, N + 1):
        c = CHI20.get(dv % 20, 0)
        if c:
            for mth in range(dv, N + 1, dv):
                tt[mth] += c
    with mp.workdps(40):
        lamk = [mp.mpf(0)] * (N + 1)
        for n in range(2, N + 1):
            s = mp.mpf(0)
            for e in range(2, n):
                if n % e == 0:
                    s += lamk[e] * tt[n // e]
            lamk[n] = (tt[n] * mp.log(n) - s) / tt[1]
        okw = True
        for n in range(2, N + 1):
            p = None
            mth = n
            for q in range(2, n + 1):
                if mth % q == 0:
                    p = q
                    while mth % q == 0:
                        mth //= q
                    break
            if mth == 1 and p is not None:
                kk = round(math.log(n) / math.log(p))
                want = (1 + CHI20.get(p % 20, 0) ** kk) * mp.log(p)
            else:
                want = mp.mpf(0)
            okw = okw and abs(lamk[n] - want) < mp.mpf("1e-30")
    ok = (oc["fail_k"] == 996 and oc["l996"] > 0 > oc["l998"]
          and 996 <= oc["kdag"] <= 1000
          and abs(oc["V"] - (-0.0196974946787)) <= 1e-8 and okw)
    check("G10-independent-collapse", ok,
          "own r_Q/Lambda_Q/g_Q/row: Szego death k = %d (t = %.3f == "
          "2.988), lambda_min(T_996) = %+.2e > 0 > lambda_min(T_998) = "
          "%+.2e (own crossing k = %d vs pinned 998, LAPACK-platform "
          "class), own V(1038) = %.10e vs v916 pin -0.0196974946787 "
          "(dev %.1e); own Euler ward on ideal counts exact n <= 60 "
          "(%.1f s)"
          % (oc["fail_k"], oc["fail_k"] * 0.003, oc["l996"], oc["l998"],
             oc["kdag"], oc["V"], abs(oc["V"] + 0.0196974946787),
             time.time() - t0))


def g11_euler_bound() -> None:
    section("G11  BH3-F2: EULER-REGION BOUND B(1.6), OWN 4-DECADE LADDER")
    t0 = time.time()
    NMAX = 4_000_000
    r = np.zeros(NMAX + 1)
    b = 0
    while 5 * b * b <= NMAX:
        a = 0
        while a * a + 5 * b * b <= NMAX:
            q = a * a + 5 * b * b
            if q >= 1:
                r[q] += (2 if a else 1) * (2 if b else 1)
            a += 1
        b += 1
    n = np.arange(NMAX + 1, dtype=float)
    n[0] = 1.0
    terms = r[4:] * n[4:] ** -1.6 / 2.0
    cum = np.cumsum(terms)

    def partial(M: int) -> float:
        return float(cum[M - 4])

    tot = []
    for M in (4000, 20000, 200000, 2000000, 4000000):
        tail = (math.pi / math.sqrt(5)) * M ** -0.6 / 0.6 / 2
        tot.append(partial(M) + tail)
    spread = max(tot) - min(tot)
    true_b = tot[-1]
    read_v916 = partial(20000) + 8.0 * 20000 ** -0.6      # collapse G21
    read_v917 = partial(200000) + 8.0 * 200000 ** -0.6    # driver G26
    ok = (spread < 2e-5 and abs(true_b - 0.645728) < 2e-5
          and abs(read_v916 - 0.664) < 5e-4
          and abs(read_v917 - 0.650) < 5e-4
          and true_b < read_v917 < read_v916 < 1.0)
    check("G11-F2-b16-three-values", ok,
          "true full sum B(1.6) = %.6f (4-decade ladder spread %.1e); "
          "reproduced corpus reads from ONE lattice: v916-pinned 0.664 "
          "= N=2e4 truncation + 6x Abel model tail (%.4f), v917 0.650 "
          "= N=2e5 + same tail (%.4f) -- both valid upper bounds < 1 "
          "(all verdicts stand), but 0.664 is NOT the 'full-table "
          "value' of the sum (%.1f s)"
          % (true_b, spread, read_v916, read_v917, time.time() - t0))


# ===================================================================== G12
A0_DRV = 245.6815
B_OUT_15 = 6.0e-5      # pinned from driver_cert run-of-record table


def g12_blind_strip() -> None:
    section("G12  BH3-F3: v917 CENSUS-BLIND STRIP, WORST-CASE SCAN")
    dmax = 0.01
    worst_v = 0.0
    worst_mag15 = 0.0
    worst_repos_big = -1.0   # max Re[2 y v^{m-1}(v-1)] where |v| >= 0.1
    worst_repos_sml = 0.0    # max positive Re where |v| < 0.1
    worst_phase = 0.0
    gam_grid = ([0.1 + 0.05 * i for i in range(157)]        # (0.1, 7.9)
                + [31.4 + 0.05 * i for i in range(273)])    # (31.4, 45)
    for gp in gam_grid:
        for dp in (0.001, 0.005, 0.01):
            mu2 = complex(dp, gp) ** 2
            yv = A0_DRV / (A0_DRV - mu2)
            vv = 4 * yv * (1 - yv)
            worst_v = max(worst_v, abs(vv))
            mag15 = abs(2 * yv * vv ** 14 * (vv - 1))
            worst_mag15 = max(worst_mag15, mag15)
            big = abs(vv) >= 0.1
            for m in range(14, 33):
                c = 2 * (yv * vv ** (m - 1) * (vv - 1))
                if big:
                    worst_repos_big = max(worst_repos_big, c.real)
                    ph = abs(math.pi - abs(np.angle(yv * vv ** (m - 1)
                                                    * (vv - 1))))
                    worst_phase = max(worst_phase, ph)
                else:
                    worst_repos_sml = max(worst_repos_sml, c.real)
    # window-width argument: |v| > 1 requires a0 inside the violation
    # window a-+ = 3d^2 + g^2 -+ 2d sqrt(2d^2+g^2); for d <= 0.01 the
    # half-width is <= 2*0.01*sqrt(2e-4 + 45^2) < 0.91, so gamma^2 must
    # be within 0.91 + 3e-4 of a0 => gamma in (15.645, 15.703): IN BAND.
    hw = 2 * dmax * math.sqrt(2 * dmax ** 2 + 45.0 ** 2)
    glo = math.sqrt(A0_DRV - hw - 3 * dmax ** 2)
    ghi = math.sqrt(A0_DRV + hw)
    in_band = 7.90 < glo and ghi < 31.40
    dc = blob("driver_cert_probe.py")
    premise = "every off-line zero below 45 is located" in dc
    ok = (worst_v < 1.0 and worst_repos_big < 0.0
          and worst_repos_sml < 1e-40
          and worst_mag15 > 20 * B_OUT_15 and in_band and premise
          and worst_phase < 0.55)
    check("G12-F3-blind-strip", ok,
          "blind region (delta <= 0.01, gamma in (0.1,7.9)u(31.4,45)): "
          "max|v(a0)| = %.4f < 1 (no hidden fire possible); worst "
          "magnitude at m = 15 is %.2e = %.0fx B_out(15) = 6.0e-5 (the "
          "stated bound does NOT cover the strip: premise gap real); "
          "but Re-contributions over m = 14..32 are < 0 where "
          "|v| >= 0.1 (max %.2e; phase within pi +- %.2f) and < 1e-40 "
          "where |v| < 0.1 (max %.1e): hidden zeros only MASK, never "
          "fake -- and any |v| > 1 zero with d <= 0.01 needs gamma in "
          "(%.3f, %.3f), INSIDE the straddle-boxed band: verdict "
          "survives" % (worst_v, worst_mag15, worst_mag15 / B_OUT_15,
                        worst_repos_big, worst_phase, worst_repos_sml,
                        glo, ghi))


# ===================================================================== G13
def g13_lagrange() -> None:
    section("G13  BH3-F4: MARKOV CLASS LABEL vs LAGRANGE ESCAPE")
    # spectrum: 10 bulk points + doublet with gap 1e-12 inside [0, 1]
    E = [0.05 * i for i in range(10)] + [0.7, 0.7 + 1e-12]
    K = len(E)
    tgt = [0.0] * 10 + [1.0, -1.0]

    def lagrange(x: float) -> float:
        tot = 0.0
        for i in range(K):
            li = tgt[i]
            if li == 0.0:
                continue
            for j in range(K):
                if j != i:
                    li *= (x - E[j]) / (E[i] - E[j])
            tot += li
        return tot

    vals = [lagrange(e) for e in E]
    opnorm = max(abs(v) for v in vals)
    split = abs(vals[10] - vals[11])
    # Markov bound under the HULL hypothesis on the same instance:
    # any |p| <= 1 on [0, 0.75] with deg <= 11 has split <=
    # 2 d^2 gap / L = 2*121*1e-12/0.75 = 3.2e-10  (probe's statement OK)
    markov_split = 2 * 11 ** 2 * 1e-12 / 0.75
    note = blob_repo("experiments/next.txt").splitlines()
    cdxxvii = next((ln for ln in note[:80] if "(CDXXVII)" in ln), "")
    label = ("{p(Q), deg ≤ d}" in cdxxvii
             or "POLYFILTER/ENERGIE" in cdxxvii)
    sel = blob("selection_probe.py")
    hyp = "|p| <= 1 on the spectral hull [m, M]" in sel
    ok = (abs(split - 2.0) < 1e-6 and opnorm <= 1.0 + 1e-6
          and markov_split < 1e-9 and label and hyp)
    check("G13-F4-lagrange-escape", ok,
          "degree-%d Lagrange interpolant: |p(E_i)| <= %.6f at every "
          "eigenvalue (||p(Q)|| = 1) yet doublet split = %.6f at gap "
          "1e-12 -- the class '{p(Q), deg <= d}' WITHOUT the hull "
          "normalization is NOT closed (note CDXXVII label drops the "
          "hypothesis); WITH the hull hypothesis (as the probe states "
          "it) Markov caps the split at %.1e on the same instance: the "
          "probe is right, the note's class label overstates"
          % (K - 1, opnorm, split, markov_split))


# ===================================================================== G15
def maxflow_units(edges: list[tuple[str, str, int]], s: str,
                  t: str) -> int:
    cap: dict[tuple[str, str], int] = {}
    nodes: set[str] = set()
    for u, v, c in edges:
        cap[(u, v)] = cap.get((u, v), 0) + c
        cap.setdefault((v, u), 0)
        nodes |= {u, v}
    flow = 0
    while True:
        prev: dict[str, str | None] = {s: None}
        queue = [s]
        while queue and t not in prev:
            u = queue.pop(0)
            for v in sorted(nodes):
                if v not in prev and cap.get((u, v), 0) > 0:
                    prev[v] = u
                    queue.append(v)
        if t not in prev:
            return flow
        path = []
        v = t
        while prev[v] is not None:
            path.append((prev[v], v))
            v = prev[v]
        aug = min(cap[e] for e in path)
        for e in path:
            cap[e] -= aug
            cap[(e[1], e[0])] += aug
        flow += aug


def g15_mincut() -> None:
    section("G15  BH3-F6: MIN-CUT REPLICA BOOKKEEPING")
    INF = 10 ** 6
    r116 = [("S", "HAUS", INF), ("HAUS", "FORMA", 1), ("FORMA", "RH", INF),
            ("S", "PICK", INF), ("PICK", "SV", 1), ("SV", "RH", INF),
            ("S", "DIAG", INF), ("DIAG", "R4HYP", 1), ("R4HYP", "RH", INF),
            ("S", "WEYLM", INF), ("WEYLM", "WEYLH", 1),
            ("WEYLH", "RH", INF)]
    r122 = r116 + [("S", "BLKREAL", INF), ("BLKREAL", "NFCLOS", INF),
                   ("NFCLOS", "LANEACONV", 1), ("LANEACONV", "RH", INF)]
    r129 = [("S", "PICKFLOORS", 1), ("PICKFLOORS", "RH", 1),
            ("S", "HANKEL", 1), ("HANKEL", "RH", 1),
            ("S", "LANEACONV", 1), ("LANEACONV", "RH", 1),
            ("S", "OMEGA4", 1), ("OMEGA4", "RH", 1),
            ("S", "C1COMPLETION", 1), ("C1COMPLETION", "LANEACONV", 1),
            ("S", "SELFDUAL-NOGO", 1)]
    f116 = maxflow_units(r116, "S", "RH")
    f122 = maxflow_units(r122, "S", "RH")
    f129 = maxflow_units(r129, "S", "RH")
    ig = blob("idgraph_search_probe.py")
    sd = blob("selfdual_construction_probe.py")
    canon = ("DIAG-BOUNDS-FIN" in ig and "LANEACONV" not in ig)
    mislabel = ('"LANEACONV"' in sd
                and "round-116 replica" in sd)
    check("G15-F6-mincut-replicas", f116 == 4 and f122 == 5 and f129 == 4
          and canon and mislabel,
          "own Edmonds-Karp: canonical r116 flow 4; r122/r128-lineage "
          "(base + LANEACONV) flow 5; r129 base-as-written flow 4 -- "
          "all correct PER GRAPH, but the canonical round-116 edge set "
          "has NO LANEACONV (grep) while r129's 'round-116 replica' "
          "base contains it: label + cross-round comparability off, "
          "no verdict rides")


# ===================================================================== G16
def g16_predeclaration() -> None:
    section("G16  BH3-F7: 'PRE-DECLARED FALSIFIED' WORDING")
    ec = blob("epstein_collapse_probe.py")
    v916 = blob_repo("verification/v916_epstein_weil_violation.py")
    amend_declares = ("EXPECTED TO READ FALSIFIED" in ec
                      and "the frozen G21 counts and the G18 witness-"
                      "attribution prediction" in ec.replace("\n", " ")
                      .replace("  ", " ").replace("  ", " ")
                      or ("EXPECTED TO READ FALSIFIED" in ec
                          and "G18 witness-attribution" in
                          ec.replace("\n", " ")))
    g19_not = "G19" not in ec.split("AMENDMENT 1")[1].split(
        "AMENDMENT 2")[0]
    wording = ("pre-declared failure pattern of G18/G19/G21" in v916
               or "PRE-DECLARED FALSIFIED PREDICTIONS" in v916)
    check("G16-F7-predeclaration", amend_declares and g19_not and wording,
          "collapse AMENDMENT 1 pre-declares the falsification of "
          "EXACTLY G18 + G21 (blocks f/g; G19 not mentioned between "
          "AMENDMENT 1 and 2), while v916/CDXXVIII word all three "
          "G18/G19/G21 as 'pre-declared falsified' -- G19's failure "
          "(law miss 0.505 > 0.5) emerged only in the full run; "
          "wording precision, gates were carried honestly")


# ===================================================================== G17-19
def audit_xi_q(s, dps: int, qcap: int):
    """OWN incomplete-gamma xi_Q evaluator (independent of the corpus)."""
    with mp.workdps(dps):
        s = mp.mpc(s)
        c = 2 * mp.pi / mp.sqrt(20)
        tot = -1 / s - 1 / (1 - s)
        b = 0
        while 5 * b * b <= qcap:
            a = 0
            while a * a + 5 * b * b <= qcap:
                q = a * a + 5 * b * b
                if q >= 1:
                    cnt = (2 if a else 1) * (2 if b else 1)
                    x = c * q
                    tot += cnt * (x ** (-s) * mp.gammainc(s, x, mp.inf)
                                  + x ** (-(1 - s))
                                  * mp.gammainc(1 - s, x, mp.inf))
                a += 1
            b += 1
        return s * (s - 1) * tot


def g17_passport() -> None:
    section("G17  DRIVER PASSPORT: OWN xi_Q REPOLISH + CROSS-ROUND PIN")
    t0 = time.time()
    with mp.workdps(40):
        rho = mp.findroot(lambda u: audit_xi_q(u, 40, 60),
                          mp.mpc("0.93", "15.67"), maxsteps=60)
        res = float(abs(audit_xi_q(rho, 40, 60)))
        pas = mp.mpc("0.9329696975", "15.6682495313")
        dev = float(abs(rho - pas))
        de = mp.re(rho) - mp.mpf("0.5")
        ga = mp.im(rho)
        m2 = float(mp.log(2) * ga ** 2 / de ** 2)
        disc = mp.sqrt(2 * de ** 2 + ga ** 2)
        a_lo = float(3 * de ** 2 + ga ** 2 - 2 * de * disc)
        a_hi = float(3 * de ** 2 + ga ** 2 + 2 * de * disc)
        a_st = float(de ** 2 + ga ** 2)
    dc = blob("driver_cert_probe.py")
    sd = blob("selfdual_construction_probe.py")
    dlog = blob("driver_cert_probe.run2.log")
    cons = (sd.count("0.9329696975") >= 1 and "15.6682495313" in sd
            and "WARD_DRIVER = (0.4330, 15.6682)" in dc
            and "rho = 0.9329696975 + 15.6682495313i" in dlog)
    ok = (dev <= 1e-8 and res <= 1e-25 and 900 <= m2 <= 916
          and a_lo < 245.69 < a_hi and a_lo < 256 < a_hi
          and abs(a_lo - 232.5) < 0.2 and abs(a_hi - 259.6) < 0.2
          and cons)
    check("G17-passport-consistent", ok,
          "own evaluator polish from coarse seed: rho = %.10f + %.10fi "
          "(dev vs passport %.1e; |xi_Q| = %.0e); m_2 = %.1f in "
          "[900, 916]; own window (%.2f, %.2f) contains a* = %.4f and "
          "256, matches the r123/r125 record +-0.2; passport literal "
          "identical in driver_cert + selfdual probes (%.0f s)"
          % (float(mp.re(rho)), float(mp.im(rho)), dev, res, m2,
             a_lo, a_hi, a_st, time.time() - t0))


def g18_ward_and_schedule() -> None:
    section("G18  4w(gamma_1) WARDS + IRWALL SCHEDULE ARITHMETIC")
    gams = (14.134725141734693790, 21.022039638771554993)
    devs = []
    for a, pin in ((144.0, 0.973665070), (256.0, 0.984791384),
                   (512.0, 0.994603870)):
        g = min(gams, key=lambda gg: abs(gg - math.sqrt(a)))
        y = a / (a + g * g)
        devs.append(abs(4 * y * (1 - y) - pin))
    kd = blob("kr4_depth_probe.run1.log")
    kj = blob("kr4_defectjet_probe.run1.log")
    ok_w = (max(devs) < 5e-9 and "0.973665070" in kd
            and "0.973665070" in kj)
    Ts = (63.06, 90.72, 126.00, 171.76, 228.32)
    oms = (25.00, 35.97, 49.95, 68.09, 90.52)
    ells = (0.800, 0.691, 0.615, 0.558, 0.514)
    dts = (0.0150, 0.0130, 0.0115, 0.0105, 0.0096)
    ok_s = True
    for i, T in enumerate(Ts):
        om = 25.0 * T / Ts[0]
        el = 0.8 * math.log(Ts[0] / (2 * math.pi)) \
            / math.log(T / (2 * math.pi))
        ok_s = ok_s and abs(om - oms[i]) < 0.02 and abs(el - ells[i]) < 1e-3
        ok_s = ok_s and abs(0.01875 * el - dts[i]) < 6e-5
    iw = blob("irwall_probe.run1.log")
    ok_s = ok_s and "T= 228.32 Om= 90.52 ell=0.514" in iw
    check("G18-wards-and-schedule", ok_w and ok_s,
          "4w(gamma_next) at a = 144/256/512 (gamma_next = ordinate "
          "nearest sqrt(a): g1/g1/g2): devs %.0e/%.0e/%.0e vs the "
          "r118/r120/r129 ward values (grep-matched in both logs); "
          "irwall coupled schedule "
          "Omega_r = 25 T_r/T_0, ell_r = 0.8 log(T_0/2pi)/log(T_r/2pi), "
          "dtau_r = 0.01875 ell_r reproduces the run-of-record rung "
          "table exactly" % tuple(devs))


def g19_kfac_law() -> None:
    section("G19  ROUND-124/126 ENRICHED-FRAME LAW RECOMPUTE")
    cm = blob("cluster_mixing_probe.run2.log")
    need = ("KFAC-LADDER x=5  kfac 2.00 beta -8.456e-04",
            "KFAC-LADDER x=8  kfac 2.00 beta -2.177e-04",
            "KFAC-LADDER x=13 kfac 2.00 beta -5.864e-05")
    okp = all(t in cm for t in need)
    s58 = math.log(8.456e-4 / 2.177e-4) / math.log(8 / 5)
    s813 = math.log(2.177e-4 / 5.864e-5) / math.log(13 / 8)
    sel = blob("selection_probe.run2.log")
    ok = (okp and abs(s58 - 2.89) < 0.02 and abs(s813 - 2.70) < 0.02
          and "falls ~x^-2.8" in sel)
    check("G19-kfac-law", ok,
          "matched enriched frame (KFAC 2.00) beta ladder from the r124 "
          "run of record: slopes log|beta|/log x = %.2f (5->8), %.2f "
          "(8->13) -- the '~x^-2.8' citation in r126 G43 recomputes; "
          "comparison is per-frame unit-normalized with alpha/resid2v "
          "printed per frame (apples-to-apples confirmed)"
          % (s58, s813))


# ===================================================================== main
def main() -> int:
    print("bughunt3_probe  PRIME.BUGHUNT3.01  (rounds 110-129)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("NO RH CLAIM.  EXPLORATION ONLY.  Findings: 7 "
          "(0 MAJOR / 4 MINOR / 3 NOTE); no round verdict flips; "
          "v916/v917 headline numbers independently CONFIRMED.")

    g01_firewall()
    cdxxxi = g02_numerals()
    g03_g04_round_attribution(cdxxxi)
    g05_theorem_r()
    g08_jet_dictionary()
    g09_matched_pin_and_nogo()
    g10_collapse_recompute()
    g11_euler_bound()
    g12_blind_strip()
    g13_lagrange()
    g15_mincut()
    g16_predeclaration()
    g17_passport()
    g18_ward_and_schedule()
    g19_kfac_law()

    section("LEDGER + COMPOSITE VERDICT")
    for fid, sev, txt in FINDINGS:
        print("  %s [%s] %s" % (fid, sev, txt))
    print("  VERDICT FLIPS: none (all round-110..129 verdict enums and "
          "the promoted v916/v917 numbers stand; recommended "
          "corrections are wording/label-level: F1 round label, F2 "
          "truncation label, F3 census-premise restatement, F4 "
          "hull-hypothesis in the note class)")
    n_pass = sum(1 for _n, ok, _d in CHECKS if ok)
    n_tot = len(CHECKS)
    dt = time.time() - START
    print("\nCHECKS %d/%d PASS  runtime %.1f s  SPEC_SHA %s"
          % (n_pass, n_tot, dt, SPEC_SHA[:16]))
    if n_pass == n_tot:
        print("COMPOSITE: BUGHUNT3-FINDINGS(7) -- 0 MAJOR / 4 MINOR / "
              "3 NOTE / 0 FATAL; Theorem R, the interior no-go, the "
              "jet dictionary, the collapse certificate and the driver "
              "certification all survive adversarial recompute.")
    else:
        print("COMPOSITE: BUGHUNT3-INSTRUMENT-EDGE(%d/%d)"
              % (n_pass, n_tot))
    print("NO RH CLAIM.")
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
