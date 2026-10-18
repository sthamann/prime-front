#!/usr/bin/env python3
"""SHARPENED-Z1 kickoff -- the first Z1 gate: does the N2
Hilbert-Polya truncation family (the deployed zeta-free GNS/Jacobi
family of the glued object, v714/v716-v721/v727-v734) exhibit the
SAME moving-edge / near-kernel signature that the closed diagonal-
Gram route measured on its window operator?
z1_edge_signature_probe.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, no spectral-reality claim beyond measurement, and this probe
writes no files.  It never reads a zero ordinate; the construction
path is AST-firewalled against prime/zero identifiers exactly as in
the parent probes.

STRUCTURAL IDENTIFICATION (stated first, it frames the whole gate):
the closed Gram route's source window operator is
T = Toeplitz(continuum + atoms) on the dyadic grid D = 1/64, and
srp.continuum_lags(M) == core.arch_lags + stage2.pole_lags_closed:
the source tower IS the Toeplitz Gram matrix of the N2 unified Weil
measure p = car + cat + cp.  The N2 truncation family (v718
machinery: Wheeler modified-Chebyshev -> monic (aM, gM) -> orthonormal
Jacobi J_K, eigenvalues = Gauss nodes) is the GNS representation of
the multiplication/shift operator of the SAME measure.  This probe
therefore does NOT ask "same object?" (that is exact and guarded);
it asks whether the MEASURED handover constraints of the Gram route
survive the passage into the candidate's self-adjoint operator frame
J_K -- the frame in which any Z1 boundary-triple / Weyl-M-function
module would have to work.  A match = the candidate family carries
the threshold structure natively; a failure = the structure is
Gram-frame-specific and the constraint list rules the family out
as-is.

INPUT STATE (frozen findings, none re-adjudicated here):
  *  qf_edge_separation_probe (EDGE-KEEPS-MOVING, 1e9 comb): source
     near-kernel (thr 1e-4) mode entries at M = 888 / 992 / 1108 /
     1276 (X = 13.875 / 15.5 / 17.3125 / 19.9375), inter-entry gaps
     DX = 1.625 / 1.8125 / 2.625 -- WIDENING cadence (ratios
     1.11538, 1.44828), rel spread 0.381; avoided 7/8 crossing with
     min rel gap 0.0039 at M = 1240; separated dimension oscillates
     (6 separated under a 7/8/9 cluster at the top).
  *  qf_drainage_probe (QF-SETTLES-POSITIVE 14/14, 1e8 comb):
     settled per-function band weights (R2 family 0.225..0.358, R1
     family 0.008..0.079); entry anchors 888:6 / 992:7 / count 8
     from ~1108; 6/7 gap bottoms 0.1008 (~1100), recovers 0.1397 at
     1176; lambda_min(1176) = 3.882e-6.
  *  qf_representation_census_probe (QF-REPRESENTATION-OPEN):
     exactly ONE near-null direction is rung-stably (cos =
     0.992..0.999, typ. 0.997) the ram-odd most-negative wavepacket
     direction; the E_7 (+) E_{-2} identification failed the census.
  *  note_hilbert_polya_truncations / v718: the N2 family's GNS
     nodes converge onto the frozen targets (100% of 377 at tol
     0.25, ladder rate -1.61); pole band tau < GAMMA1 = 14.10 is
     the trivial-mode/threshold band of the family (27 nodes at
     h = 1433); Wheeler validity + Levinson PD measured on all
     windows.

CANDIDATE FAMILY (frozen; deployed construction reused read-only,
zeta-free by design, verified by the AST guard):  at dyadic rung M
(X = M*D), the candidate operator is the K-point GNS truncation
J_K of the unified window measure with K = M/2: Chebyshev moments
p[:M] -> jac.wheeler(p[:M], K) -> orthonormal Jacobi (bJ = aM,
aJ = sqrt(gM[1:K])) -- v718 gns_nodes machinery verbatim.  DECLARED
frame choice: the per-window D(h) of the deployed frame-A ladder is
replaced by the source's dyadic D = 1/64 so that the candidate's
ladder lives on the SAME X axis as the measured source cadence; the
K-ladder at fixed measure is exactly v718's "pure GNS ladder".
Deep comb cap ATOM_MAX_DEEP = 1e8 (drainage cap, frozen), M_TOP =
1176, ladder LAD = 648..1176 step 4 (133 rungs, K = 324..588),
census pre-rung M_PRE = 644.

THE GNS FRAME MAP (frozen; needed to transplant contact + drainage):
the ON polynomial basis of J_K is the Cholesky-ON basis of the
cos-basis Gram G_c[j,k] = (p_|j-k| + p_{j+k})/2 (the even folding of
the Toeplitz Gram under x = 2 cos theta); for a coefficient vector f
the GNS coordinates are c = L^T f (G_c = L L^T) and ||f||_mu =
||L^T f||.  Frame Ward G1.7: at M_WARD = 648 the tridiagonalization
L^{-1} A_x L^{-T} of the multiplication matrix A_x[j,k] =
<cos j, x cos k> must reproduce the Wheeler (aM, sqrt gM) tridiagonal
(max abs dev <= 1e-3, consistency Ward -- catches a wrong frame, not
a precision claim; the norm-chain L[k,k] = ||pi_k||/2 is REPORTED).

CANDIDATE EDGE BAND (frozen): the threshold/boundary band of the
family is the pole band of the N2 note: nodes with tau =
arccos(x/2)/D < TAU_EDGE = 14.10 (the deployed v718 GAMMA1
pole-band boundary, DECLARED; classical annotation: this equals the
smooth-density edge -- it enters ONLY as a fixed census line applied
identically to candidate and every control, and the cadence gate
compares RATIOS, insensitive to the line's placement).  Census count
n_edge(M) = #{tau_j < TAU_EDGE}; entry rung of level n = first LAD
rung with count >= n (baseline = count at M_PRE).

SIGNATURE GATES (all frozen BEFORE the first run; the comparison
object is the SOURCE cadence ratio sequence, never absolute
positions):
  Z1-A  MOVING-EDGE CADENCE: >= 4 entries (>= 3 gaps) on LAD; the
      LAST three inter-entry gaps g1, g2, g3 must WIDEN
      (g1 < g2 < g3, g1 > 0) AND their ratios r1 = g2/g1,
      r2 = g3/g2 must match the source ratios (1.11538, 1.44828)
      within RATIO_BAR = 0.25 relative each
      (|r_i / r_i^src - 1| <= 0.25).
  Z1-B  AVOIDED CROSSING AT THE BAND EDGE: boundary-pair gap
      profile g(M) = (tau_{ne+1} - tau_{ne}) / tau_{ne+1} (last
      node inside / first outside); PASS iff some rung within
      |X - X_entry| <= 1.0 of a measured entry has
      g <= DIP_BAR = 0.25 x median(g over LAD)  (source analog:
      7/8 dip 0.0039 vs O(0.05) typical, ratio ~0.08).
  Z1-C  RAM-ODD CONTACT DIRECTION: candidate avatar of the ram-odd
      negative wavepacket frame = the 5 MOST NEGATIVE eigenvectors
      of Toeplitz(c_ro)[:K,:K] (the census C1 E_{-2} avatar
      dimension; c_ro = hand-built ramified-odd comb: atoms
      u = (2k+1) log 2, masses 2 log2 * 2^{-(2k+1)/2} -- the srp ro
      channel, Ward-checked against srp masks at parent reach);
      contact = largest principal cosine between orth(L^T W_ro)
      and the edge-band eigenspace of J_K; PASS iff cos >=
      CONTACT_BAR = 0.95 on >= 4 of the LAST5 rungs (source: 0.997
      rung-stable).
      [CONSTRUCTION CORRECTION, documented: the first run
      (2026-08-05a) used a single-vector avatar (lowest ro
      eigenvector only) and its G1.10b anchor fired at 0.9534 --
      the census contact 0.992..0.999 is measured against the
      5-dim ro-negative FRAME, not one vector; the avatar was
      corrected once to the census frame object, all bars
      unchanged, and the rerun is the adjudicating run.  The
      invalid first run made no signature statement; under the
      wrong single-vector avatar its C gate read cos 0.22..0.37
      on LAST5 (fail), so the correction changes the measured
      object, not the bar.]
  Z1-D  SETTLED COUPLING LEVELS (drainage transplanted): q_f(M) =
      ||U_edge^T L^T f||^2 / ||L^T f||^2 for the 14 frozen battery
      functions (hbp.battery verbatim, NPAD = 128), mu-normalized
      (DECLARED: GNS-native normalization -- level IDENTITY with
      the source's settled levels is NOT gated, only the
      settles-positive property); drainage P bars verbatim on
      PARENT5/MID5/TOP5/HALF2: |b| <= 0.05 per X unit, level >=
      1e-3, TOP5 rel spread <= 0.15; PASS iff 14/14 type P.
GUARDS (must pass or the run is invalid):
  G0.1 AST firewall (banned: zetazero/nzeros/isprime/primerange/
       nextprime/prevprime/primepi/sympy); G0.2 SHA-256 freeze of
       battery bytes + ladders + bars + anchors BEFORE any comb
       data is built here; G0.3 reach census + runtime cap 1200 s;
  G1.1 deep-table overlap == deployed core table EXACTLY; G1.2
       Chebyshev envelope kappa <= KAPPA_REF + 1e-6 on [100, 1e8];
  G1.3 parent tower comb consistency (<= 1e-12); G1.4 prefix Ward
       deep tower leading 824-block == parent tower (<= 1e-12);
  G1.5 source anchor reproduction (Gram side, same object): (a)
       near-null counts 884:5, 888:6, 988:6, 992:7, 1104:7,
       1108:8; (b) 7/8 gap(1176) = 0.0613 +- 2e-4, lambda_min(1176)
       = 3.882e-6 +- 2e-8; (c) drainage settled levels med5(TOP5)
       reproduce the nine frozen values +- 2e-3;
  G1.6 Wheeler validity: kbad None on EVERY LAD rung AND Gauss
       moment reconstruction rel dev <= 1e-8 at M = 648/888/1176;
  G1.7 GNS frame Ward (above, <= 1e-3); G1.8 Cholesky PD of G_c on
       every LAD rung; G1.9 boundedness: every q_f in [-1e-12,
       1 + 1e-9], every contact cos <= 1 + 1e-12;
  G1.10 ro-comb Ward: hand ro lags == srp ro channel lags at parent
       reach (<= 1e-12) AND source-side contact anchor at M = 972:
       max principal cosine near-kernel(6) vs the 5-dim ram-odd
       negative frame >= 0.97 (census frozen band 0.992..0.999).
CONTROLS (mandatory, must fire):
  CG  STRUCTURAL (the discriminating control): a generic random
      self-adjoint family of the SAME dimensions -- 3 GOE principal
      -truncation families H_K = (A + A^T)[:K,:K] / sqrt(2K)
      (seeds 11/12/13) PLUS the free Chebyshev Jacobi (bJ = 0,
      aJ = 1, nodes 2cos(j pi/(K+1))) -- each run through the
      IDENTICAL edge census on the identical ladder; FIRE iff 0/4
      instances pass the Z1-A cadence bars (a cadence any operator
      family shows is worthless; the free family is the
      constant-density null anchor, ratios == 1).
  CS  position scramble (uniform (0.5, 2 alpha), masses kept, seed
      7, deep comb) on rungs 888..1176 step 32: FIRE iff the
      candidate construction breaks (Wheeler kbad) on some rung OR
      the census completes without passing the Z1-A bars.
  CE  Epstein x^2 + 5y^2 (epstein_firewall_probe read-only, cap
      M = 640) on rungs 400..640 step 8: same fire rule.
      A control that survives AND passes Z1-A has spuriously
      converged: the run is INVALID.
VERDICT ENUM (frozen; decision order as listed):
  0. any guard fails or a control spuriously matches -> printed as
     Z1-GATE-INVALID, exit 1, no signature statement follows.
  1. Z1-SIGNATURE-MATCH   = A and B and C and D all pass: the
     candidate family carries the measured threshold structure;
     the next Z1 module is named: the Weyl-M-function /
     boundary-triple construction on the candidate's edge band.
  2. Z1-SIGNATURE-PARTIAL = at least one of A/B/C/D passes (named
     exactly); the passing signatures define the surviving
     interface, the failing ones the missing structure.
  3. Z1-SIGNATURE-ABSENT  = none of A/B/C/D passes: the candidate
     family lacks the measured threshold structure as-is; what any
     future Z1 candidate must add is stated from the failure
     anatomy.
STOP-LIST (binding, inherited): no zeros / prime tables anywhere in
the construction path; no bare A^{-1}; no PD-margin or 1/eps in any
gate; no fits inside gates beyond the declared bounded-statistic
slope (drainage P clause verbatim); the cadence gate is fit-free;
NO RH claim.  This probe writes no files.  Runtime cap 1200 s.

RESULTS (2026-08-05, adjudicating preregistered run, 24.1 s; GATES
A/B/C/D = FAIL/PASS/PASS/PASS -> 3/4; GUARDS+CONTROLS 20/20;
verdict Z1-SIGNATURE-PARTIAL, the failing signature is exactly the
widening cadence):
  *  Z1-A FAILS -- THE CANDIDATE EDGE IS QUADRATURE FILLING, NOT A
     WIDENING CADENCE.  The edge census rises 22 -> 40 over
     K = 324..588 with 18 entries at an almost perfectly REGULAR
     spacing DX = 0.4375/0.5000 (mean 0.4485; grid note: gaps are
     quantized by the step-4 rung grid, resolution 0.0625).  The
     last-3 gaps 0.4375/0.5000/0.4375 give ratios 1.143/0.875 vs
     source 1.115/1.448: the FIRST ratio matches (dev 0.025) but
     the widening clause fails and dev2 = 0.396 > 0.25.  Scale
     observation (reported): candidate mean DX = 0.4485 is ~3.6x
     denser than the source's first gap 1.625 -- consistent with
     v718's node/zero density 3.37: the candidate edge fills at
     the Gauss-quadrature density, and that filling is REGULAR --
     exactly what the free-Jacobi null anchor shows (its ratios
     are 1.000/1.000).  The widening moving-edge cadence of the
     Gram near-kernel has no analog among the Gauss nodes.
  *  Z1-B PASSES -- WITH ITS CO-LOCATION CLAUSE VACUOUS, TYPED
     HONESTLY: at the candidate's entry density (0.44 X between
     entries < 2 x the +-1.0 X window) every rung is entry-
     adjacent, so the gate reduces to its dip-depth clause.  That
     clause is genuinely carried: the boundary-pair gap profile
     (ladder median 0.0353) collapses to 0.0032 at M = 896
     (0.090 x median) and 0.0043 around M = 1096 (0.123 x median)
     -- edge-node collisions of the SAME depth as the source's 7/8
     crossing minimum 0.0039.  Observation (reported, no gate,
     post-hoc): the two deepest dips sit at M = 896 and ~1096,
     within one or two rung-steps of the SOURCE's Gram landmarks
     (6th-mode entry 888; 6/7-gap bottom 1096..1100, 8th entry
     1108) -- the candidate's edge collisions echo the source's
     mode-entry depths even though its own census is regular.
  *  Z1-C PASSES 5/5 -- THE RAM-ODD CONTACT SURVIVES THE PASSAGE
     INTO THE OPERATOR FRAME: largest principal cosine between
     orth(L^T W_ro) (the mu-normalized 5-dim ram-odd negative
     frame) and the edge-band eigenspace of J_K = 0.9890 / 0.9860
     / 0.9775 / 0.9662 / 0.9667 on LAST5 (ladder median 0.9456,
     max 0.9971; chance floor ~ 0.26; source Gram-frame contact
     0.997, anchor reproduced here at 0.9931).  The one-
     dimensional qf/deck-odd contact that the census found in the
     Gram near-kernel is PRESENT in the candidate's threshold
     band -- the first genuinely positive structural transfer of
     the handover list onto the N2 family.
  *  Z1-D PASSES 14/14 -- SETTLED POSITIVE COUPLINGS IN THE
     CANDIDATE FRAME: all functions type P (rates |b| <= 0.017/X,
     TOP5 spreads <= 0.014, levels 0.0047..0.6450).  Honest
     anatomy: the mu-normalized hierarchy INVERTS the Gram wall's
     -- hats dominate (R2:hat(R/2,R/2) 0.6450 vs source 0.3127;
     R1:hat(R/4,R/4) 0.0222 vs 0.0082) while boxes collapse
     (R2:box[0,R] 0.0098 vs 0.3583): the edge band couples
     strongly to smooth localized packets and weakly to sharp
     boxes once the GNS metric reweights.
  *  CONTROLS ALL FIRE: CG 0/4 -- the three GOE truncation
     families produce 0..1 usable entry gaps (erratic edge, no
     cadence statement possible), the free Chebyshev Jacobi gives
     perfectly regular ratios 1.000/1.000 and fails the widening
     clause exactly as the candidate does; CS scramble: Wheeler
     breakdown kbad = 16 on all 10 control rungs (the scrambled
     measure is not a state -- v718's Levinson breakdown in the
     Wheeler chain); CE Epstein: Wheeler breakdown kbad = 27 on
     all 31 control rungs.  GUARDS 20/20: deep table exact, kappa
     0.038821, prefix Ward 2.0e-14, source anchors ALL reproduced
     (counts 884:5/888:6/988:6/992:7/1104:7/1108:8, 7/8 gap(1176)
     0.0613, lambda_min 3.8825e-6, drainage levels worst dev
     4.9e-5, contact anchor 0.9931), Wheeler valid on all 134
     rungs (recon dev <= 1.6e-13), frame Ward 5.2e-13, ro Ward
     0.0, Cholesky PD 134/134, boundedness clean.
  *  CONSEQUENCE FOR THE Z1 PROGRAMME (stated plainly): the N2
     truncation family carries three of the four measured
     handover signatures natively in its self-adjoint frame --
     edge collisions at the right depth (B), the ram-odd contact
     direction in its threshold band (C, cos 0.977..0.989), and
     settled positive battery couplings (D) -- but NOT the
     widening moving-edge cadence (A): the candidate's edge
     census is regular quadrature filling, indistinguishable in
     cadence TYPE from the free Chebyshev Jacobi (equilibrium
     filling), and the widening 1.625/1.8125/2.625 lives only in
     the Gram near-kernel entries.  For the boundary-triple /
     Weyl-M-function module this splits the work precisely: the
     candidate edge band is a legitimate carrier of the contact
     and coupling structure (C, D) and exhibits collision events
     (B), but the CELL STRUCTURE of the Z1 contract -- the entry
     rungs 888/992/1108/1276 with their widening cadence -- must
     be imported as boundary data from the Gram near-kernel (the
     cell-cocycle surface), not read off J_K's spectrum.  A Z1
     candidate built as "J_K + boundary triple over the Gram
     near-kernel band" is consistent with everything measured
     here; a Z1 candidate that expects the bulk spectrum alone to
     produce the cadence is ruled out at the frozen bars.  NOT
     claimed: any statement beyond X = 18.375, eps-uniformity,
     spectral reality, RH.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/z1_edge_signature_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402
import v696_z1_jacobi as jac  # noqa: E402  (Wheeler, locked)
import simpler_schur_recursion_probe as srp  # noqa: E402
import handoff_bulk_probe as hbp  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID                        # 1/64, dyadic float-exact
ATOM_MAX_DEEP = 100000000            # deep comb cap (drainage cap)
M_CAP_DEEP = int(math.floor(math.log(ATOM_MAX_DEEP) / D))   # 1178
M_TOP = 1176                         # deepest rung (X = 18.375)
M_PAR = 824                          # parent cap (prefix Ward)
M_PRE = 644                          # census baseline rung

LAD = list(range(648, 1177, 4))      # 133 rungs, K = 324..588
LAST5 = list(range(1160, 1177, 4))
PARENT5 = list(range(956, 973, 4))   # drainage blocks verbatim
MID5 = list(range(1056, 1073, 4))
TOP5 = list(range(1160, 1177, 4))
HALF2 = list(range(1072, 1177, 4))
M_WARD = 648                         # GNS frame Ward rung

TAU_EDGE = 14.10                     # v718 GAMMA1 pole-band bound
X_EDGE = 2.0 * math.cos(TAU_EDGE * D)

SRC_ENTRY_M = (888, 992, 1108, 1276)          # frozen source record
SRC_DX = (1.625, 1.8125, 2.625)
SRC_R1 = SRC_DX[1] / SRC_DX[0]                # 1.11538
SRC_R2 = SRC_DX[2] / SRC_DX[1]                # 1.44828
RATIO_BAR = 0.25                     # Z1-A cadence ratio bar
DIP_BAR = 0.25                       # Z1-B dip vs ladder median
W_ENTRY_X = 1.0                      # Z1-B entry co-location window
CONTACT_BAR = 0.95                   # Z1-C principal cosine bar
CONTACT_RUNGS = 4                    # of the LAST5
SRC_CONTACT = 0.997                  # source contact (report)
SRC_G78MIN = 0.0039                  # source crossing min (report)

P_SLOPE = 0.05                       # Z1-D drainage P bars verbatim
P_FLOOR = 1.0e-3
P_SPREAD = 0.15
N_MED = 5
NPAD = 128
R_BAT = (1.0, 2.0)
QF_FLOOR = 1.0e-12

THR_NULL = 1.0e-4                    # source near-null threshold
BAR_GAUSS = 1.0e-8                   # G1.6 moment reconstruction
WARD_FRAME = 1.0e-3                  # G1.7 frame consistency Ward
WARD_RO = 1.0e-12                    # G1.10 ro-comb Ward
ANCH_CONTACT = 0.97                  # G1.10 source contact anchor
COMB_DEV_BAR = 1.0e-12               # G1.3
PREFIX_WARD = 1.0e-12                # G1.4
REPRO_COUNTS = {884: 5, 888: 6, 988: 6, 992: 7, 1104: 7, 1108: 8}
REPRO_G78_1176 = 0.0613
REPRO_TOLG = 2.0e-4
REPRO_LMIN1176 = 3.882e-6
REPRO_LTOL = 2.0e-8
DRAIN_LEVELS = {                     # source settled levels (frozen)
    "R2:box[0,R]": 0.3583, "R2:box[R/2,R]": 0.3370,
    "R2:hat(R/2,R/2)": 0.3127, "R2:hat(3R/4,R/4)": 0.2590,
    "R2:box[R/4,3R/4]": 0.2249, "R1:box[R/2,R]": 0.0793,
    "R1:box[0,R]": 0.0741, "R2:box[0,R/2]": 0.0741,
    "R1:hat(R/4,R/4)": 0.0082}
REPRO_QTOL = 2.0e-3
BOUND_TOL = 1.0e-9
RUNTIME_CAP = 1200.0

CG_SEEDS = (11, 12, 13)              # GOE structural control seeds
SEED_CS = 7                          # scramble seed (verbatim)
CTRL_LAD_CS = list(range(888, 1177, 32))      # 10 rungs
EP_NCAP = 34000
EP_MMAX = 640
CTRL_LAD_CE = list(range(400, 641, 8))        # 31 rungs

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []       # guards + controls: all must pass, else invalid run
GATES = []        # signature gates: feed the verdict only


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def gate(name, ok, detail=""):
    GATES.append((name, bool(ok)))
    print("[GATE %s] %s%s" % ("PASS" if ok else "FAIL", name,
                              (": " + detail) if detail else ""))
    return bool(ok)


def ast_firewall():
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = set()
    for node in ast.walk(tree):
        name = ""
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                token = alias.name.split(".")[0]
                if any(b in token.lower() for b in BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in BANNED):
            hits.add(name)
    return sorted(hits)


def freeze_spec():
    """Battery bytes + ladders + bars + anchors, SHA-256 frozen
    BEFORE any comb data is built in this probe."""
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("z1-edge-signature spec: candidate = v718 gns_nodes "
                "machinery at dyadic D=%.10f, K=M/2, deep comb cap "
                "%d, M_TOP=%d, LAD=%s, M_PRE=%d; frame map = "
                "cholesky of cos-Gram (p_|j-k|+p_{j+k})/2, coords "
                "L^T f; edge band tau < %g (v718 GAMMA1, declared); "
                "Z1-A: last-3 gaps widening AND ratios vs (%f, %f) "
                "within %g; Z1-B: boundary-pair gap dip <= %g x "
                "ladder median within |X-Xentry| <= %g; Z1-C: 5-dim "
                "ro-negative frame (hand comb u=(2k+1)ln2, mu=2ln2 "
                "2^{-(2k+1)/2}) contact >= %g on >= %d of LAST5=%s; "
                "Z1-D: drainage P bars |b|<=%g floor %g spread %g "
                "on PARENT5=%s MID5=%s TOP5=%s HALF2=%s, 14/14; "
                "guards: gauss recon <= %g at 648/888/1176, frame "
                "ward <= %g at %d, ro ward <= %g, contact anchor >= "
                "%g at 972, counts %s, g78(1176)=%g+-%g, lmin=%g+-"
                "%g, drain levels %s +- %g, comb<=%g prefix<=%g "
                "runtime<=%g; controls: CG = 3 GOE truncation "
                "families (A+A^T)[:K,:K]/sqrt(2K) seeds %s + free "
                "Chebyshev Jacobi, fire iff 0/4 pass Z1-A; CS "
                "scramble seed %d rungs %s, CE Epstein cap %d M %d "
                "rungs %s, fire = wheeler breakdown OR no Z1-A "
                "match; verdict order: invalid -> MATCH(ABCD) -> "
                "PARTIAL(any) -> ABSENT"
                % (D, ATOM_MAX_DEEP, M_TOP, LAD, M_PRE, TAU_EDGE,
                   SRC_R1, SRC_R2, RATIO_BAR, DIP_BAR, W_ENTRY_X,
                   CONTACT_BAR, CONTACT_RUNGS, LAST5, P_SLOPE,
                   P_FLOOR, P_SPREAD, PARENT5, MID5, TOP5, HALF2,
                   BAR_GAUSS, WARD_FRAME, M_WARD, WARD_RO,
                   ANCH_CONTACT, sorted(REPRO_COUNTS.items()),
                   REPRO_G78_1176, REPRO_TOLG, REPRO_LMIN1176,
                   REPRO_LTOL, sorted(DRAIN_LEVELS.items()),
                   REPRO_QTOL, COMB_DEV_BAR, PREFIX_WARD,
                   RUNTIME_CAP, CG_SEEDS, SEED_CS, CTRL_LAD_CS,
                   EP_NCAP, EP_MMAX, CTRL_LAD_CE)).encode())
    for R in R_BAT:
        bats[R] = hbp.battery(R)
        for nm, v in bats[R]:
            hsh.update(nm.encode())
            hsh.update(v.tobytes())
    return bats, hsh.hexdigest()


def battery_matrix(bats):
    cols, names = [], []
    for R in R_BAT:
        nR = int(round(R / D))
        for nm, v in bats[R]:
            f = np.zeros(NPAD)
            f[:nR] = v
            cols.append(f)
            names.append("R%g:%s" % (R, nm))
    return np.stack(cols, axis=1), names


# ------------------------------------------------ towers (verbatim)
def build_parent_tower():
    alpha = 0.5 * M_PAR * D
    ka, masks, dev_m = srp.channel_masks(alpha)
    check("G1.3 parent tower comb consistency (zeta-free Gauss "
          "double sieve == deployed masses, rel dev <= %.0e)"
          % COMB_DEV_BAR, dev_m <= COMB_DEV_BAR,
          "rel dev %.1e, ka=%d atoms to e^%.4f"
          % (dev_m, ka, 2.0 * alpha))
    c = srp.continuum_lags(M_PAR)
    for cnl in ("ro", "re", "sp", "in"):
        c = c + srp.atom_channel_lags(alpha, M_PAR, masks[cnl])
    return sla.toeplitz(c[:M_PAR]), masks, alpha


def build_deep_comb():
    lam_deep = core.von_mangoldt_table(ATOM_MAX_DEEP)
    dev = float(np.max(np.abs(lam_deep[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("G1.1 deep-table overlap: deep von Mangoldt table == "
          "deployed core table on [0, %d] EXACTLY"
          % core.ATOM_MAX, dev == 0.0, "max abs dev %.1e" % dev)
    nn = np.nonzero(lam_deep > 0.0)[0]
    u_deep = np.log(nn.astype(float))
    mu_deep = 2.0 * lam_deep[nn] / np.sqrt(nn.astype(float))
    psi = np.cumsum(lam_deep[nn])
    keep = nn.astype(float) >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                         / nn[keep].astype(float)))
    check("G1.2 deep-range Chebyshev envelope: kappa = %.6f over "
          "[%.0f, %d] <= KAPPA_REF + %.0e = %.6f"
          % (kappa, core.KAPPA_X0, ATOM_MAX_DEEP, core.TOL_KAPPA,
             core.KAPPA_REF + core.TOL_KAPPA),
          kappa <= core.KAPPA_REF + core.TOL_KAPPA)
    return u_deep, mu_deep


def build_deep_tower(u_deep, mu_deep, T_par):
    alpha = 0.5 * M_TOP * D
    ka = int(np.searchsorted(u_deep, 2.0 * alpha + 1.0e-14,
                             side="right"))
    c_cont = srp.continuum_lags(M_TOP)
    c_at, _dd = core.atom_lags_at(alpha, M_TOP, u_deep[:ka],
                                  mu_deep[:ka])
    p = c_cont + c_at
    T = sla.toeplitz(p[:M_TOP])
    dev = float(np.max(np.abs(T[:M_PAR, :M_PAR] - T_par)))
    check("G1.4 prefix Ward: deep tower leading %d x %d block == "
          "parent tower, max abs dev %.1e <= %.0e"
          % (M_PAR, M_PAR, dev, PREFIX_WARD), dev <= PREFIX_WARD)
    print("  deep census: ka = %d atoms to e^%.4f" % (ka,
                                                      2.0 * alpha))
    return p, T, c_cont, alpha, ka


def build_ro_comb(alpha_top, masks, alpha_par):
    """Hand-built ramified-odd comb (powers 2^{2k+1}), zeta-free;
    Ward against the srp ro channel at parent reach."""
    ns, k = [], 0
    while (2 * k + 1) * math.log(2.0) <= 2.0 * alpha_top + 1e-14:
        ns.append(2 ** (2 * k + 1))
        k += 1
    ns = np.array(ns, float)
    u_ro = np.log(ns)
    mu_ro = 2.0 * math.log(2.0) / np.sqrt(ns)
    c_ro, _dd = core.atom_lags_at(alpha_top, M_TOP, u_ro, mu_ro)

    keep = u_ro <= 2.0 * alpha_par + 1e-14
    c_hand, _dd = core.atom_lags_at(alpha_par, M_PAR, u_ro[keep],
                                    mu_ro[keep])
    c_srp = srp.atom_channel_lags(alpha_par, M_PAR, masks["ro"])
    dev = float(np.max(np.abs(c_hand - c_srp)))
    check("G1.10a ro-comb Ward: hand ramified-odd lags == srp ro "
          "channel lags at parent reach (%d atoms), max abs dev "
          "%.1e <= %.0e" % (int(np.sum(keep)), dev, WARD_RO),
          dev <= WARD_RO)
    return c_ro


# ------------------------------------------------ source-side anchors
def source_anchors(T, c_ro, F, names):
    anchor_rungs = sorted(set(list(REPRO_COUNTS) + [972, 1176]
                              + TOP5))
    spec = {}
    for M in anchor_rungs:
        lam, V = np.linalg.eigh(T[:M, :M])
        spec[M] = (lam, V)

    ok_cnt = True
    det = []
    for M, want in sorted(REPRO_COUNTS.items()):
        got = int(np.sum(spec[M][0] <= THR_NULL))
        det.append("%d:%d" % (M, got))
        ok_cnt = ok_cnt and (got == want)
    check("G1.5a source entry anchors: near-null counts (thr %g) "
          "%s == frozen %s" % (THR_NULL, "/".join(det),
                               sorted(REPRO_COUNTS.items())),
          ok_cnt)

    lam76 = spec[1176][0]
    g78 = float((lam76[7] - lam76[6]) / lam76[7])
    check("G1.5b source gap/PD anchors: 7/8 gap(1176) = %.4f vs "
          "frozen %.4f (tol %.0e); lambda_min(1176) = %.4e vs "
          "frozen %.4e (tol %.0e)"
          % (g78, REPRO_G78_1176, REPRO_TOLG, lam76[0],
             REPRO_LMIN1176, REPRO_LTOL),
          abs(g78 - REPRO_G78_1176) <= REPRO_TOLG
          and abs(lam76[0] - REPRO_LMIN1176) <= REPRO_LTOL)

    qs = []
    for M in TOP5:
        V6 = spec[M][1][:, :6]
        qs.append(np.sum((V6[:NPAD, :].T @ F) ** 2, axis=0))
    med = np.median(np.stack(qs), axis=0)
    dev_worst = max(abs(float(med[j]) - DRAIN_LEVELS[nm])
                    for j, nm in enumerate(names)
                    if nm in DRAIN_LEVELS)
    check("G1.5c source drainage-level anchors: med%d(TOP5) "
          "reproduces the nine frozen levels, worst dev %.1e <= "
          "%.0e" % (N_MED, dev_worst, REPRO_QTOL),
          dev_worst <= REPRO_QTOL)

    lam72, V72 = spec[972]
    n72 = int(np.sum(lam72 <= THR_NULL))
    lam_ro, v_ro = np.linalg.eigh(sla.toeplitz(c_ro[:972]))
    sv = np.linalg.svd(V72[:, :n72].T @ v_ro[:, :5],
                       compute_uv=False)
    cosc = float(sv[0])
    check("G1.10b source contact anchor at M = 972: near-null "
          "count %d (== 6), max principal cosine near-kernel vs "
          "5-dim ram-odd negative frame = %.4f >= %g (census band "
          "0.992..0.999)" % (n72, cosc, ANCH_CONTACT),
          n72 == 6 and cosc >= ANCH_CONTACT)
    return {M: spec[M][0] for M in anchor_rungs}


# ------------------------------------------------ candidate machinery
def cheb_gram(p, K):
    """Cos-basis Gram G[j,k] = (p_|j-k| + p_{j+k})/2 (even folding
    of the Toeplitz Gram under x = 2 cos theta)."""
    idx = np.arange(K)
    return 0.5 * (p[np.abs(idx[:, None] - idx[None, :])]
                  + p[idx[:, None] + idx[None, :]])


def cand_rung(p, M, Fp, c_ro, want_recon=False):
    """One candidate rung: J_{K=M/2} of the unified measure; edge
    census, boundary gap, contact cosine, battery couplings."""
    K = M // 2
    aM, gM, kbad = jac.wheeler(p[:M], K)
    if kbad is not None:
        return dict(M=M, K=K, kbad=int(kbad))
    bJ = aM.copy()
    aJ = np.sqrt(gM[1:K])
    ev = sla.eigh_tridiagonal(bJ, aJ, eigvals_only=True)
    tau = np.sort(np.arccos(np.clip(ev / 2.0, -1.0, 1.0)) / D)
    n_edge = int(np.sum(ev > X_EDGE))
    g_bd = np.nan
    if 1 <= n_edge < K:
        g_bd = float((tau[n_edge] - tau[n_edge - 1]) / tau[n_edge])
    _evE, UE = sla.eigh_tridiagonal(bJ, aJ, select="v",
                                    select_range=(X_EDGE, 4.0))

    G = cheb_gram(p, K)
    try:
        L = sla.cholesky(G, lower=True, check_finite=False)
    except np.linalg.LinAlgError:
        return dict(M=M, K=K, kbad=None, chol=False)

    Fk = np.zeros((K, Fp.shape[1]))
    Fk[:NPAD, :] = Fp
    C = L.T @ Fk
    q = (np.sum((UE.T @ C) ** 2, axis=0)
         / np.maximum(np.sum(C ** 2, axis=0), QF_FLOOR))

    lam_ro, v_ro = sla.eigh(sla.toeplitz(c_ro[:K]),
                            subset_by_index=[0, 4])
    Qu, _r = np.linalg.qr(L.T @ v_ro)
    sv = np.linalg.svd(UE.T @ Qu, compute_uv=False)
    cosc = float(sv[0]) if sv.size else 0.0

    recon = None
    if want_recon:
        rec = jac.gauss_reconstruct(aM, gM, p[0], min(2 * K, M))
        recon = float(np.max(np.abs(rec - p[:len(rec)]))
                      / np.max(np.abs(p[:len(rec)])))
    return dict(M=M, K=K, kbad=None, chol=True, n_edge=n_edge,
                g_bd=g_bd, q=q, cos=cosc, recon=recon,
                lam_ro=float(lam_ro[0]), L=L if M == M_WARD else None,
                aM=aM if M == M_WARD else None,
                gM=gM if M == M_WARD else None)


def frame_ward(p, blk):
    """G1.7: L^{-1} A_x L^{-T} == Wheeler tridiagonal at M_WARD."""
    K = blk["K"]
    L, aM, gM = blk["L"], blk["aM"], blk["gM"]
    Gx = cheb_gram(p, K + 1)
    A = np.zeros((K, K))
    A[:, 0] = 2.0 * Gx[:K, 1]
    for k in range(1, K):
        A[:, k] = Gx[:K, k + 1] + Gx[:K, k - 1]
    A = 0.5 * (A + A.T)
    Y = sla.solve_triangular(L, A, lower=True, check_finite=False)
    J = sla.solve_triangular(L, Y.T, lower=True,
                             check_finite=False).T
    J = 0.5 * (J + J.T)
    Jw = np.diag(aM) + np.diag(np.sqrt(gM[1:K]), 1) \
        + np.diag(np.sqrt(gM[1:K]), -1)
    dev = float(np.max(np.abs(J - Jw)))
    check("G1.7 GNS frame Ward at M = %d (K = %d): max |L^-1 A_x "
          "L^-T - J_wheeler| = %.1e <= %.0e (frame consistency)"
          % (M_WARD, K, dev, WARD_FRAME), dev <= WARD_FRAME)
    lg = math.log(float(p[0])) + float(np.sum(np.log(gM[1:K])))
    lc = 2.0 * math.log(2.0 * float(L[K - 1, K - 1]))
    print("  norm-chain report (never gated): log ||pi_%d||^2 "
          "wheeler %.6f vs cholesky %.6f (dev %.1e)"
          % (K - 1, lg, lc, abs(lg - lc)))


# ------------------------------------------------ census + cadence
def entry_census(xs, counts, n_base):
    """Entry level n -> first x with count >= n (n > baseline)."""
    entries = []
    cmax = max(counts)
    for n in range(n_base + 1, cmax + 1):
        for x, c in zip(xs, counts):
            if c >= n:
                entries.append((n, x))
                break
    return entries


def cadence_match(entries, label):
    """Frozen Z1-A statistic: last-3 gaps widening AND ratios match
    the source ratios within RATIO_BAR (fit-free)."""
    xs = [x for (_n, x) in entries]
    gaps = [b - a for a, b in zip(xs, xs[1:])]
    if len(gaps) < 3:
        return False, ("%s: insufficient entries (%d gaps < 3)"
                       % (label, len(gaps))), gaps
    g1, g2, g3 = gaps[-3:]
    widening = (g1 > 0.0) and (g1 < g2 < g3)
    r1 = g2 / g1 if g1 > 0 else float("inf")
    r2 = g3 / g2 if g2 > 0 else float("inf")
    d1 = abs(r1 / SRC_R1 - 1.0)
    d2 = abs(r2 / SRC_R2 - 1.0)
    ok = widening and d1 <= RATIO_BAR and d2 <= RATIO_BAR
    det = ("%s: last-3 gaps %.4f/%.4f/%.4f, ratios %.3f/%.3f vs "
           "source %.3f/%.3f (devs %.3f/%.3f, bar %g), widening=%s"
           % (label, g1, g2, g3, r1, r2, SRC_R1, SRC_R2, d1, d2,
              RATIO_BAR, widening))
    return ok, det, gaps


# ------------------------------------------------ controls
def control_cg():
    print("\n-- CG structural control (3 GOE truncation families + "
          "free Chebyshev Jacobi, identical census)")
    K_top = M_TOP // 2
    n_match = 0
    for seed in CG_SEEDS:
        rng = np.random.default_rng(seed)
        A = rng.standard_normal((K_top, K_top))
        H = A + A.T
        counts = []
        for M in LAD:
            K = M // 2
            evs = np.linalg.eigvalsh(H[:K, :K] / math.sqrt(2.0 * K))
            counts.append(int(np.sum(evs > X_EDGE)))
        entries = entry_census([M * D for M in LAD], counts,
                               counts[0])
        ok, det, _g = cadence_match(entries, "GOE seed %d" % seed)
        print("  " + det)
        n_match += int(ok)
    counts = []
    for M in LAD:
        K = M // 2
        j = np.arange(1, K + 1)
        x = 2.0 * np.cos(j * math.pi / (K + 1))
        counts.append(int(np.sum(x > X_EDGE)))
    entries = entry_census([M * D for M in LAD], counts, counts[0])
    okf, detf, _g = cadence_match(entries, "free Jacobi")
    print("  " + detf)
    n_match += int(okf)
    return check("CG structural control fires: 0/4 generic "
                 "families pass the Z1-A cadence bars (%d matched)"
                 % n_match, n_match == 0)


def control_measure(pc, lad, label):
    """CS/CE fire rule: wheeler breakdown OR census completes
    without passing Z1-A."""
    kbads, counts, xs = [], [], []
    for M in lad:
        K = M // 2
        aM, gM, kbad = jac.wheeler(pc[:M], K)
        if kbad is not None:
            kbads.append((M, int(kbad)))
            continue
        ev = sla.eigh_tridiagonal(aM, np.sqrt(gM[1:K]),
                                  eigvals_only=True)
        counts.append(int(np.sum(ev > X_EDGE)))
        xs.append(M * D)
    if kbads:
        return check("%s control fires: candidate construction "
                     "breaks (Wheeler breakdown on %d/%d rungs, "
                     "first kbad = %d at M = %d)"
                     % (label, len(kbads), len(lad), kbads[0][1],
                        kbads[0][0]), True)
    entries = entry_census(xs, counts, counts[0])
    ok, det, _g = cadence_match(entries, label)
    print("  " + det)
    return check("%s control fires: construction survives and the "
                 "census does NOT pass the Z1-A bars" % label,
                 not ok)


# ------------------------------------------------ run
def run():
    print("=" * 78)
    print("SHARPENED-Z1 kickoff -- edge-signature gate: the N2 "
          "GNS/Jacobi family vs the source moving-edge record "
          "(X <= %.4f)" % (M_TOP * D))
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall (construction path zeta-free; edge "
          "census line is a declared constant)", not hits,
          str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 battery + ladders + bars + anchors SHA-256-frozen "
          "BEFORE any comb data is built here", True,
          "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP = %d <= floor(64 ln %d) = %d; "
          "sieve cover exp(X_top) + 2 = %d <= %d; runtime cap "
          "%.0f s predeclared"
          % (M_TOP, ATOM_MAX_DEEP, M_CAP_DEEP,
             int(math.exp(M_TOP * D)) + 2, ATOM_MAX_DEEP,
             RUNTIME_CAP),
          M_TOP <= M_CAP_DEEP
          and int(math.exp(M_TOP * D)) + 2 <= ATOM_MAX_DEEP)

    # ---- combs + towers strictly after the freeze
    u_deep, mu_deep = build_deep_comb()
    T_par, masks, alpha_par = build_parent_tower()
    p, T, c_cont, alpha_top, ka = build_deep_tower(u_deep, mu_deep,
                                                   T_par)
    c_ro = build_ro_comb(alpha_top, masks, alpha_par)
    F, names = battery_matrix(bats)

    # ---- source-side anchors (same glued object, Gram frame)
    print("\n-- source anchors (Gram frame; guards, not gates)")
    source_anchors(T, c_ro, F, names)

    # ---- candidate ladder
    print("\n-- candidate ladder: J_{K=M/2} on LAD = %d..%d step 4 "
          "(%d rungs), edge line tau < %.2f (x > %.6f)"
          % (LAD[0], LAD[-1], len(LAD), TAU_EDGE, X_EDGE))
    blks = {}
    recs = {}
    for M in [M_PRE] + LAD:
        blk = cand_rung(p, M, F, c_ro,
                        want_recon=(M in (648, 888, 1176)))
        blks[M] = blk
        if blk.get("recon") is not None:
            recs[M] = blk["recon"]
    bad = [(M, b["kbad"]) for M, b in blks.items()
           if b.get("kbad") is not None]
    check("G1.6 Wheeler validity: kbad None on every rung (%d "
          "rungs) AND Gauss moment reconstruction rel dev %s <= "
          "%.0e" % (len(LAD) + 1,
                    "/".join("%.1e" % recs[M] for M in sorted(recs)),
                    BAR_GAUSS),
          not bad and all(v <= BAR_GAUSS for v in recs.values()),
          str(bad[:3]) if bad else "")
    if bad:
        print("\nVERDICT: Z1-GATE-INVALID (candidate construction "
              "broke)")
        return 1
    nochol = [M for M, b in blks.items() if not b.get("chol", False)]
    check("G1.8 Cholesky PD of the cos-Gram on every rung",
          not nochol, str(nochol[:3]))
    if nochol:
        print("\nVERDICT: Z1-GATE-INVALID (Gram not PD)")
        return 1
    frame_ward(p, blks[M_WARD])

    # ---- Z1-A cadence
    print("\n-- Z1-A: edge census + entry cadence (source record: "
          "entries M = %s, DX = %s)"
          % (list(SRC_ENTRY_M), list(SRC_DX)))
    counts = [blks[M]["n_edge"] for M in LAD]
    print("  edge count profile (every 8th rung): %s"
          % "/".join("%d:%d" % (M, blks[M]["n_edge"])
                     for M in LAD[::8]))
    entries = entry_census([M * D for M in LAD], counts,
                           blks[M_PRE]["n_edge"])
    print("  entry table (baseline count %d at M = %d):"
          % (blks[M_PRE]["n_edge"], M_PRE))
    for n, x in entries:
        print("    level %2d: entry X = %.4f (M = %d)"
              % (n, x, int(round(x / D))))
    a_ok, a_det, gaps = cadence_match(entries, "candidate")
    if gaps:
        print("  inter-entry gaps DX = %s (mean %.4f); source DX = "
              "%s" % ("/".join("%.4f" % g for g in gaps),
                      float(np.mean(gaps)), list(SRC_DX)))
        print("  predicted next entry (REPORTED only): X ~ %.2f"
              % (entries[-1][1] + float(np.mean(gaps))))
    a_ok = gate("Z1-A MOVING-EDGE CADENCE: %s" % a_det, a_ok)

    # ---- Z1-B crossing
    print("\n-- Z1-B: boundary-pair gap profile (source analog: "
          "7/8 min gap %.4f at M = 1240)" % SRC_G78MIN)
    gprof = {M: blks[M]["g_bd"] for M in LAD
             if np.isfinite(blks[M]["g_bd"])}
    med_g = float(np.median(list(gprof.values())))
    m_min = min(gprof, key=gprof.get)
    print("  gap profile (every 16th rung): %s"
          % "  ".join("M=%d:%.4f" % (M, gprof[M])
                      for M in LAD[::16] if M in gprof))
    print("  ladder median %.4f; global min %.4f at M = %d "
          "(%.3f x median)" % (med_g, gprof[m_min], m_min,
                               gprof[m_min] / med_g))
    dips = []
    for n, xe in entries:
        near = [gprof[M] for M in gprof
                if abs(M * D - xe) <= W_ENTRY_X]
        if near:
            dips.append((n, xe, min(near)))
    for n, xe, gmin in dips:
        print("  entry level %d (X = %.4f): min gap within +-%g X "
              "= %.4f (%.3f x median)"
              % (n, xe, W_ENTRY_X, gmin, gmin / med_g))
    b_ok = gate("Z1-B AVOIDED CROSSING: min entry-adjacent gap = "
                "%.4f, bar <= %.4f (%g x ladder median %.4f)"
                % (min((d[2] for d in dips), default=float("inf")),
                   DIP_BAR * med_g, DIP_BAR, med_g),
                bool(dips) and min(d[2] for d in dips)
                <= DIP_BAR * med_g)

    # ---- Z1-C contact
    print("\n-- Z1-C: ram-odd contact direction (source: cos %.3f "
          "rung-stable; chance floor ~ sqrt(n_edge/K) ~ %.2f)"
          % (SRC_CONTACT,
             math.sqrt(blks[LAD[-1]]["n_edge"]
                       / float(blks[LAD[-1]]["K"]))))
    cos_all = [blks[M]["cos"] for M in LAD]
    print("  contact profile on LAST5: %s; ladder median %.4f, max "
          "%.4f" % ("  ".join("M=%d:%.4f" % (M, blks[M]["cos"])
                              for M in LAST5),
                    float(np.median(cos_all)), max(cos_all)))
    n_hit = sum(1 for M in LAST5 if blks[M]["cos"] >= CONTACT_BAR)
    c_ok = gate("Z1-C RAM-ODD CONTACT: cos >= %g on %d/%d of "
                "LAST5 (need >= %d)"
                % (CONTACT_BAR, n_hit, len(LAST5), CONTACT_RUNGS),
                n_hit >= CONTACT_RUNGS)

    # ---- Z1-D settled couplings
    print("\n-- Z1-D: settled coupling levels (drainage P bars "
          "verbatim; mu-normalized -- level identity with the "
          "source NOT gated)")
    qmap = {M: blks[M]["q"] for M in LAD}
    med_par = np.median(np.stack([qmap[M] for M in PARENT5]), axis=0)
    med_mid = np.median(np.stack([qmap[M] for M in MID5]), axis=0)
    med_top = np.median(np.stack([qmap[M] for M in TOP5]), axis=0)
    q_t5 = np.stack([qmap[M] for M in TOP5])
    spread = (q_t5.max(axis=0) - q_t5.min(axis=0)) \
        / np.maximum(q_t5.max(axis=0), QF_FLOOR)
    xs_h = np.array([M * D for M in HALF2])
    q_h = np.stack([qmap[M] for M in HALF2])
    print("  %-18s %-8s %-8s %-8s %6s %7s %6s %8s" %
          ("function", "parent", "mid", "top", "b/X", "spread",
           "type", "src-lvl"))
    n_p = 0
    for j, nm in enumerate(names):
        rows = [dict(XmR=float(x), mx=float(v))
                for x, v in zip(xs_h, q_h[:, j])]
        b, _res = hbp.fit_rate(rows)
        ty = "P" if (abs(b) <= P_SLOPE and med_top[j] >= P_FLOOR
                     and spread[j] <= P_SPREAD) else "U"
        n_p += int(ty == "P")
        src = ("%.4f" % DRAIN_LEVELS[nm]) if nm in DRAIN_LEVELS \
            else "--"
        print("  %-18s %.4f   %.4f   %.4f   %+5.3f  %5.3f    %s   %8s"
              % (nm, med_par[j], med_mid[j], med_top[j], b,
                 spread[j], ty, src))
    d_ok = gate("Z1-D SETTLED COUPLINGS: %d/14 functions type P "
                "(|b| <= %g, level >= %g, spread <= %g)"
                % (n_p, P_SLOPE, P_FLOOR, P_SPREAD), n_p == 14)
    qall = np.stack([qmap[M] for M in LAD])
    check("G1.9 boundedness: every q_f in [%.1e, %.4f] inside "
          "[-1e-12, 1 + %.0e]; max contact cos %.4f <= 1 + 1e-12"
          % (float(np.min(qall)), float(np.max(qall)), BOUND_TOL,
             max(cos_all)),
          float(np.min(qall)) >= -1.0e-12
          and float(np.max(qall)) <= 1.0 + BOUND_TOL
          and max(cos_all) <= 1.0 + 1.0e-12)

    # ---- controls
    cg_ok = control_cg()
    print("\n-- CS position-scramble control (deep comb, masses "
          "kept, seed %d)" % SEED_CS)
    rng = np.random.default_rng(SEED_CS)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_top, ka))
    cat_s, _dd = core.atom_lags_at(alpha_top, M_TOP, pos,
                                   mu_deep[:ka])
    control_measure(c_cont + cat_s, CTRL_LAD_CS, "CS scramble")
    print("\n-- CE Epstein control (x^2 + 5y^2, cap M = %d)"
          % EP_MMAX)
    r1 = epx.lattice_r1(EP_NCAP)
    bb = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(bb, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    catE, _dd = core.atom_lags_at(0.5 * EP_MMAX * D, EP_MMAX,
                                  np.log(supp.astype(float)),
                                  2.0 * lamE[supp]
                                  / np.sqrt(supp.astype(float)))
    control_measure(srp.continuum_lags(EP_MMAX) + catE,
                    CTRL_LAD_CE, "CE Epstein")
    _ = cg_ok

    # ---- runtime guard
    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
          % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

    # ---- verdict (preregistered decision order)
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CG", "CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CG", "CS", "CE")))
    sigs = dict(A=a_ok, B=b_ok, C=c_ok, D=d_ok)
    n_sig = sum(sigs.values())
    if not (guards_ok and controls_ok):
        verdict = "Z1-GATE-INVALID"
    elif n_sig == 4:
        verdict = "Z1-SIGNATURE-MATCH"
    elif n_sig >= 1:
        verdict = "Z1-SIGNATURE-PARTIAL"
    else:
        verdict = "Z1-SIGNATURE-ABSENT"

    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/4 (A=%s B=%s C=%s D=%s), GUARDS+CONTROLS "
          "%d/%d, runtime %.1f s"
          % (n_sig, *["P" if sigs[k] else "F" for k in "ABCD"],
             n_chk, len(CHECKS), time.time() - T_START))
    if verdict == "Z1-SIGNATURE-MATCH":
        print("CONSEQUENCE (stated plainly): the N2 truncation "
              "family carries the measured threshold structure "
              "natively in its self-adjoint operator frame -- the "
              "next Z1 module is the Weyl-M-function / boundary-"
              "triple construction on the candidate's edge band, "
              "with the entry rungs above as its cell boundaries.  "
              "NO RH claim.")
    elif verdict == "Z1-SIGNATURE-PARTIAL":
        print("CONSEQUENCE (stated plainly): the candidate family "
              "carries ONLY the signature(s) %s of the measured "
              "handover constraints; the failing signature(s) %s "
              "name the structure a Z1 boundary triple cannot get "
              "from J_K as-is and must add explicitly.  NO RH "
              "claim."
              % ([k for k in "ABCD" if sigs[k]],
                 [k for k in "ABCD" if not sigs[k]]))
    else:
        print("CONSEQUENCE (stated plainly): the candidate family "
              "lacks the measured threshold structure entirely -- "
              "the handover constraint list rules out the plain "
              "GNS/Jacobi family as the Z1 bulk operator; any "
              "future candidate must carry the Gram near-kernel "
              "band as genuine spectral structure (moving edge "
              "with widening cadence, edge collision, ram-odd "
              "contact).  NO RH claim.")
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
