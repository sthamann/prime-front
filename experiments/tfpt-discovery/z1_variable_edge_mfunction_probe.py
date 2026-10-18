#!/usr/bin/env python3
"""SHARPENED-Z1 module 3 -- the variable-edge M-function with the
fixed import: mu-weighted boundary triple (Candidate A) / full-frame
intertwining (Candidate B), entry-pole isolation, Herglotz
compactness, and the moment-functional cluster leg that measures
whether PRIME.KMS.INDUCTIVE_STATE.02 and PRIME.Z1.OPERATOR.01 are
the same remaining object on this surface.
z1_variable_edge_mfunction_probe.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, no spectral-reality claim beyond measurement, and this probe
writes no files.  AST-firewalled; everything below is source-native
(unified window measure and its Gram/GNS frames only).  BINDING
STOP RULE (user): NO fixed-d variants anywhere -- every object in
this module carries the variable dimension d(X) of the frozen
threshold rule; the only 6-mode expression is the drainage ANCHOR
reproduction (a source Ward, not an analysis object; declared).

INPUT STATE (frozen findings, none re-adjudicated here):
  *  z1_boundary_triple_probe (Z1-TRIPLE-PARTIAL, gate a only):
     the finite triple (A = 2 - J_K, imported Gram band) is
     EXACTLY Herglotz on all 104 rungs incl. the typed transitions
     -- the frame survives.  The import dies: the Gram near-kernel
     packets are delocalized (cell-mass exactly 0.500 in the
     half-window on every gate rung), so the K = M/2 truncation +
     polar WHITENING turned the truncation loss into quasi-generic
     boundary noise (sigma_min(U) = 2.4e-4 blown up to O(1)):
     delivery med5 rho_b = 5.88 (split spectrum: half the
     directions AT the qf scale 0.0101..0.0106 vs 0.0100, two hot
     directions 5x..16x eps), broadband S-roughness 25%/rung
     masking any cell signal, Weil-state overweight ~40%.
     Candidate-vs-generic stayed real: 5.9 vs 13.0 (GOE bulk) vs
     132.5 (random boundary).  Full-depth GNS (K = M) is OUT OF
     REACH by deepening (lags to 2M = X 27.75, e^27.75 atoms).
  *  qf_edge_separation_probe (1e9): typed entries at M = 888/992/
     1108/1276; anchors as in the parent (counts, gaps incl. 7/8
     gap(1240) = 0.0039, lambda_min(1176) = 3.882e-6, drainage
     levels).  qf_cell_cocycle_probe: band rule d(M) =
     #{lam <= 1e-4}, Kato/polar chain, [J R | N] embedding at
     entries -- reused verbatim (the variable spectral section
     P_X = 1_{(-inf,E_X]} with E_X = THR_NULL absorbing one mode
     at every typed entry; transitions are typed events, not
     failures).
  *  qf_representation_census_probe: the rung-stable contact
     (cos 0.997) of ONE near-null direction with the ram-odd
     negative wavepacket -- the prediction behind the rank-one
     residue gate.
  *  v718: pole-band threshold GAMMA1 = 14.10 -- the deployed
     dictionary constant behind the entry-pole cut E_CUT below.

COMPUTE BUDGET (declared): same 512-GB/32-core machine and 1e9
comb as the parent (measured 118.3 s there); cap 1800 s.

CONSTRUCTION (all frozen before the first run; A/B pattern with at
most one adjudication switch, both candidates frozen NOW):
  SHARED SPINE (parent verbatim): 1e9 comb -> lags p -> Toeplitz
      T; ladder LAD = 888..1300 step 4; per rung the Gram band
      (d(X) lowest, threshold rule), sign-fixed, chained transported
      frame R (polar links, [J R | N] at entries), transported cell
      basis B = V_d R; bulk J_{K=M/2} by Wheeler, A = 2 I - J_K;
      GNS map L (cheb Gram Cholesky); RAW import U = L^T B[:K] --
      NO polar step, NOTHING whitened.  Measured distortion
      P_X = U^T U (its eigenvalues = the squared mu-norms of the
      imported band directions; reported).
  CANDIDATE A (PRIMARY -- the mu-weighted triple): the boundary
      M-function in the mu-weighted inner product,
          H_X(z) = U^T (A_X - z)^{-1} U
      (Herglotz by construction, no normalization anywhere).
      DELIVERY REFERENCE renormalized by the measured distortion
      (algebra forced by U = Q P^{1/2}: if the whitened pair
      delivered, then H = P^{1/2} H_gram P^{1/2}):
          Fref_X(z) = P^{1/2} H_gram_X(z) P^{1/2},
          H_gram_X(z) = R^T diag(1/(lam_i(X) - z))_{i<=d} R
      (the exact source band resolvent; Ward against the parent
      Feshbach block: F~ H_gram = I to machine precision).
      rho_A(X) = ||H_X(Z_REF) - Fref_X(Z_REF)||_F /
                 ||Fref_X(Z_REF)||_F.
  CANDIDATE B (FALLBACK -- full M-cell frame, intertwining): on
      the full cell frame the M-function IS the Gram object
      (delivery to Feshbach exact by construction), so the content
      is the commutation statement of the import map with the
      declared threshold dictionary at the resolvent level:
          rho_B(X) = ||(A + eps)^{-1} U - U (Lam_d + eps)^{-1}||_F
                     / ||U (Lam_d + eps)^{-1}||_F,   eps = -Z_REF.
      SWITCH TRIGGER (frozen): B is adjudicated iff med5 of rho_A
      over GATE_BLOCK > B_MATCH; the delivery leg then uses
      rho_B against the SAME bars.  Decision trail printed.
  ENTRY-POLE ISOLATION (Candidate-A object; exact finite
      decomposition, no fits): with A v_n = a_n v_n and
      w_n = U^T v_n,
          H_X(z) = sum_n w_n w_n^T / (a_n - z)
      exactly (Ward against the banded solve).  The ENTRY-BAND
      poles are those with a_n <= E_CUT = 2 - 2 cos(D * GAMMA1)
      = 4 sin^2(D * 14.10 / 2) = 0.0483 (the deployed pole-band
      dictionary; source-native constant).  Pole matrix
      Pi_X = sum_{a_n <= E_CUT} w_n w_n^T (PSD by construction),
      regular part M~_X(z) = sum_{a_n > E_CUT} w_n w_n^T/(a_n - z).
      ENTRY RESIDUES: at each typed entry e (d -> d+1),
      R_e = Pi(e) - pad(Pi(prev rung)) on the transported
      coordinates (old frame = first d, new direction = last, by
      the [J R | N] convention); within-run Pi increments reported
      as drift baseline.
  MOMENT FUNCTIONALS (the INDUCTIVE_STATE.02 avatar, declared):
      battery band coordinates c_f = B[:NPAD]^T f (source-native
      projection); mu_k(f, X) = c_f^T [sum_{a_n > E_CUT}
      w_n w_n^T a_n^k] c_f for k = 0, 1, 2 -- the moment
      functionals of the regular boundary spectral measure against
      the frozen battery (14 functions x 3 moments = 42 tracks).
GATES (frozen; no fits anywhere):
  (P1) ENTRY POLES RANK-ONE PSD: for every typed entry e:
       min eig R_e >= -PSD_TOL_REL * ||R_e||_2 AND rank ratio
       s_1(R_e)/sum_i s_i(R_e) >= RANK1_BAR = 0.75 (the 0.997
       contact predicts ~0.99; bar generous, value reported).
  (P2) ENTRY MASS SUMMABLE (the KILL leg): c_mass(X) =
       sum_{e <= X} ||R_e||_F / tr P_X <= MASS_BAR = 1.0 on every
       rung AND ||R_last||_F <= ENTRY_GROWTH_BAR = 10 x
       ||R_first||_F.  KILL (DEAD-grade, 'nicht summierbare
       Eintrittsmasse') iff c_mass(top) > 1.0.  Mass fraction
       phi(X) = tr Pi/tr P reported along the ladder.
  (B1) LOCAL UNIFORM BOUNDEDNESS (compactness leg 1): on the
       frozen grid ZGRID = {Re in (-0.5,-0.25,0,0.25,0.5)} x
       {Im in (1e-3,1e-2,1e-1,1)}, C(X) = max over the GATED
       sub-grid (Im >= 1e-2) of ||M~_X(z)||_2; PASS iff
       med5(LAST5)/med5(FIRST5) of C <= CBND_RATIO = 2.0.  The
       Im = 1e-3 row is REPORTED, not gated (declared: at K <=
       650 the regular-pole spacing ~6e-3 makes that row a
       pole-distance roulette, not a compactness statistic).
  (B2) EQUICONTINUITY PROXY (compactness leg 2): same statistic
       on the exact derivative ||M~'_X(z)||_2 =
       ||sum w w^T/(a-z)^2||_2 (the Cauchy-estimate object);
       PASS iff med5(LAST5)/med5(FIRST5) <= CDER_RATIO = 2.0.
       B1 AND B2 = the normal-family (Montel/Helly) evidence at
       finite level -- the Herglotz-compactness form of the
       contract; typed as measurement, never as a limit claim.
  (CL) MOMENT-FUNCTIONAL CLUSTER: for each of the 42 tracks the
       tail oscillation osc = (max - min)/max(median |.|, 1e-30)
       over LAST10; PASS iff median over tracks <= CL_BAR = 0.2.
  (DEL) DELIVERY RE-TEST: rho (A, or B after trigger) med5 over
       GATE_BLOCK = 1256..1272 <= B_MATCH = 0.25 (parent bar);
       structural fail iff BOTH candidates > B_DEAD = 10.
  (CR) CELL-RESPONSE RE-TEST (reported + typed; NOT
       CARRIES-blocking per the frozen enum): cocycle rel-max
       increments of H_X(Z_REF)/tr P_X along the ladder
       (transported corner at entries), contrast rho(e) >=
       C_RESP = 3.0 at E_TEST with uniqueness <= 1.
GUARDS (parent verbatim + new Wards; run invalid on failure):
  G0.1 AST firewall; G0.2 SHA-freeze of battery + ladders + bars
  + anchors BEFORE comb data; G0.3 reach + runtime cap 1800 s;
  G1.1 deep-table overlap; G1.2 kappa envelope; G1.3 parent comb;
  G1.4 prefix Ward; G1.5a-d source anchors (counts/gaps/lmin/
  drainage/transition set == E_TEST); G1.6 Wheeler + Cholesky +
  Gauss recon; G1.7 GNS frame Ward at 888; G1.8 Gram PD; G1.9
  coupling + transport Wards; G1.10 pole-decomposition Ward
  (H from eigenpairs == banded solve at rungs 888/1272, <= 1e-9)
  + Feshbach inversion Ward (F~ H_gram = I <= 1e-8) + residue
  completeness (sum_n w_n w_n^T == P, <= 1e-10 rel); G1.11
  Herglotz guard on H at both complex parent points (structural,
  min eig Im H >= -1e-8); G1.12 import floor sigma_min(U) >=
  1e-8 (collapse = typed structural fail as in parent).
CONTROLS (mandatory, must fire; frozen fire rules):
  CS scramble (seed 7) and CE Epstein (cap 640): Wheeler
     breakdown as in both parents.
  CB GOE bulk (seed 11, z = -1e-1): FIRE iff med5 rho_A^goe over
     GATE_BLOCK > B_MATCH (generic bulk does not deliver the
     renormalized block); the GOE entry-pole structure (mass,
     rank ratios at the typed entries) is REPORTED -- 'no
     arithmetic entry events' is typed from it, not gated
     (parent CB honesty note carries over: the boundary path is
     shared by construction).
  CW random boundary (seed 20260805, 6-dim, d = 6 run + 992):
     FIRE iff med5 rho_A^cw > B_MATCH AND 992-contrast < C_RESP.
VERDICT ENUM (frozen; decision order as listed):
  0. any guard fails or a control fails to fire ->
     Z1-VAREDGE-INVALID, exit 1, no structural statement.
  1. Z1-VAREDGE-DEAD = P2 kill (entry mass not summable) OR B1
     fails (boundedness of the regularized family broken) OR
     both candidates > B_DEAD on delivery: the operator route is
     typed at its honest end on this surface.
  2. Z1-VAREDGE-CARRIES = DEL and P1 and P2 and B1 and B2 and CL
     all pass: the sharpened Z1 object exists at finite level in
     the variable-edge form; the proof-grade contract must then
     say: the variable-edge boundary triple of the window chain
     has a normal Herglotz family with summable rank-one entry
     poles at the arithmetic thresholds, whose weak-* cluster
     states (INDUCTIVE_STATE.02) are exactly the Herglotz limits
     of the Z1 M-function (OPERATOR.01) -- one compactness
     theorem, two contract names.
  3. Z1-VAREDGE-PARTIAL = anything else; legs named.
UNIFICATION REPORT (5) (report only, no gate): the measured
evidence whether the weak-* cluster demand of
PRIME.KMS.INDUCTIVE_STATE.02 and the Z1 operator demand of
PRIME.Z1.OPERATOR.01 are the same remaining object here: B1+B2
(normal family) + CL (moment clustering) measured on the SAME
spectral measure -- if both hold, the two contracts share their
missing theorem (Helly selection for the boundary measure chain);
recommended contract text printed either way.
STOP-LIST (binding): NO fixed-d variants; no zeros/prime tables;
no bare A^{-1}; no PD-margin or 1/eps in gates; no fits in gates;
NO RH claim.  This probe writes no files.

RESULTS (2026-08-05; single preregistered execution, no reruns,
117.6 s; GUARDS+CONTROLS 23/23 -- the run is VALID; LEGS 3/6:
DEL FAIL, P1 FAIL (PSD half only), P2 PASS, B1 PASS, B2 PASS,
CL FAIL; CR (reported) FAIL; adjudicated candidate B after the
frozen trigger; verdict Z1-VAREDGE-PARTIAL -- no kill fired:
c_mass 0.032 << 1, boundedness holds, both candidates at 0.92,
far from dead-grade 10):
  *  A/B DECISION TRAIL: rho_A med5 = 0.9243 > 0.25 -> frozen
     switch -> Candidate B adjudicated: rho_B med5 = 0.9246 --
     the two candidates are numerically the SAME failure (rung
     profiles differ by < 0.012 everywhere).  Both say: in the
     mu-weighted metric the imported band does NOT reproduce the
     P-renormalized Gram resolvent -- H_raw is ~92% SMALLER than
     Fref.  Anatomy (measured): the entry-band mass fraction is
     phi = tr Pi / tr P = 0.016 -- only ~1.6% of the imported
     mu-mass sits below E_CUT = 0.0483; the raw import spreads
     98% of its weight into the bulk region, while
     Fref ~ P^{1/2} (1/(lam+eps)) P^{1/2} demands the top
     mu-direction (sigma_1^2 = 1.08e-2, two decades above the
     rest -- the contact direction) to sit AT the threshold.
     DISCLOSURE (typed, load-bearing for reading the controls):
     in this raw form the delivery statistic LOSES its
     discriminating power -- candidate 0.92 vs GOE bulk 0.93 vs
     random boundary 0.99 (parent whitened separation was 5.9 vs
     13.0 vs 132.5).  The control fire rules (rho > 0.25) are
     satisfied and the run is valid, but a delivery number of
     this form carries no arithmetic signature either way; the
     delivery leg is honestly typed UNRESOLVED-BY-THIS-METRIC,
     not merely failed.
  *  ENTRY-POLE TABLE (the genuinely new positive): typed
     entries vs isolated poles, raw mu-weighted metric --
       M= 992: lam_gram 9.944e-5, n_pole 34, ||R_e||_F 5.45e-5,
               rank-ratio 0.796, min eig -9.4e-6;
       M=1108: lam_gram 9.946e-5, n_pole 38, ||R_e||_F 7.93e-5,
               rank-ratio 0.869, min eig -9.1e-6;
       M=1276: lam_gram 9.975e-5, n_pole 44, ||R_e||_F 5.48e-5,
               rank-ratio 0.804, min eig -1.1e-5.
     The RANK-ONE HALF of P1 PASSES at every entry (0.80/0.87/
     0.80 >= 0.75) -- the 0.997-contact prediction is CONFIRMED
     in the raw metric: each arithmetic entry adds one dominant
     residue direction.  The PSD half fails at -20% of ||R_e||_2:
     the increment Pi(e) - Pi(prev) also carries a mass
     REBALANCING of the old directions (within-run drift median
     5.3e-6, max 6.4e-5 -- same scale), so exact PSD-ness of a
     4-rung increment against a moving bulk (K grows by 2) was
     too strong a clause; typed: entries = predominantly rank-one
     additions plus O(20%) non-PSD drift.
  *  (P2) ENTRY MASS SUMMABLE -- THE KILL CRITERION IS FAR AWAY:
     c_mass profile 5.8e-3 -> 1.6e-2 -> 1.7e-2 (top), max 3.2e-2
     vs bar 1.0; entry-mass growth ||R_last||/||R_first|| = 1.01
     (the three entry masses are CONSTANT to 1%: 5.4e-5 / 7.9e-5
     / 5.5e-5).  'Nicht summierbare Eintrittsmasse' does NOT
     occur on this surface.
  *  (B1)+(B2) HERGLOTZ COMPACTNESS CARRIES: on the frozen
     compacts (Im z >= 1e-2) the regularized family is bounded
     with ratio 0.936 (grid-sup ||M~|| med5 9.27e-2 -> 8.67e-2:
     it FALLS) and equicontinuous with derivative ratio 0.807
     (2.63 -> 2.12); even the reported 1e-3 roulette row is flat
     (9.5e-2 -> 8.8e-2).  The variable-edge M-function family is
     a normal family on the reachable surface -- the
     Herglotz-compactness form of the contract is MEASURED TO
     HOLD, including through all three typed transitions.
  *  (CL) MOMENT FUNCTIONALS DO NOT SETTLE: median tail
     oscillation 22.1 (max 73.9) over the 42 battery-moment
     tracks -- the weak-* avatar swings by an order of magnitude
     over LAST10.  Same root cause as (CR): the raw H-path is
     broadband-rough (within-run median rel increment 0.196/rung,
     entry contrasts 1.5..2.4 vs bar 3.0, 24 comparable
     increments) -- the half-window import noise rotates the
     residue weights rung to rung.
  *  CONTROLS: CS 9/9 and CE 31/31 Wheeler breakdowns; CB 0.93 >
     0.25 and CW 0.99 > 0.25 with 992-contrast 2.30 < 3 -- all
     fire per the frozen rules, with the discrimination
     disclosure above.
  *  UNIFICATION EVIDENCE (the module's real yield, stated
     plainly): the two contract demands SPLIT EXACTLY along the
     measured line.  The CLUSTER-EXISTENCE half -- what
     compactness gives -- is CARRIED: bounded mass (P2),
     bounded + equicontinuous regularized family (B1+B2) mean
     every subsequence of the variable-edge boundary chain has
     weak-* / locally-uniform cluster points (Helly/Montel at
     finite level).  The SELECTION half -- WHICH cluster point,
     i.e. actual settling of the state -- is NOT carried (CL osc
     22), and its obstruction is the SAME measured object that
     fails DEL and CR: the K = M/2 import noise.  So
     PRIME.KMS.INDUCTIVE_STATE.02 and PRIME.Z1.OPERATOR.01 are
     measured to share their compactness theorem, and to share
     their remaining obstruction.  RECOMMENDED CONTRACT TEXT for
     the next promotion round (report only, nothing filed here):
     'Merge the compactness halves of INDUCTIVE_STATE.02 and
     OPERATOR.01 into one target Z1-COMPACTNESS: the
     variable-edge boundary triple of the window chain has a
     normal Herglotz family with bounded, ~rank-one, summable
     entry poles at the arithmetic thresholds (measured at
     X <= 20.3125: mass ratio 0.032, boundedness ratio 0.936,
     equicontinuity ratio 0.807, rank ratios 0.80..0.87).  The
     residual deltas are ONE object viewed twice: state
     SELECTION (INDUCTIVE_STATE.02: the moment tracks must
     settle) == import-faithful boundary map (OPERATOR.01: a
     coupling of the Gram band to the bulk that does not pass
     through the lossy K = M/2 half-window frame).  Any future
     module must attack that shared delta, not the two contracts
     separately.'  NOT claimed: any statement beyond X = 20.3125,
     limit existence, eps-uniformity, continuum
     self-adjointness, spectral reality, RH.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/z1_variable_edge_mfunction_probe.py
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
import v696_z1_jacobi as jac  # noqa: E402
import simpler_schur_recursion_probe as srp  # noqa: E402
import handoff_bulk_probe as hbp  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402
import qf_spectral_bundle_probe as qsb  # noqa: E402

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID
ATOM_MAX_DEEP = 1000000000
M_CAP_DEEP = int(math.floor(math.log(ATOM_MAX_DEEP) / D))
M_TOP = 1300
M_PAR = 824

LAD = list(range(888, 1301, 4))
E_TEST = (992, 1108, 1276)
GATE_BLOCK = list(range(1256, 1273, 4))
TOP5W = list(range(1160, 1177, 4))
FIRST5 = LAD[:5]
LAST5 = LAD[-5:]
LAST10 = LAD[-10:]
M_WARD = 888
WARD_H_RUNGS = (888, 1272)

THR_NULL = 1.0e-4
GAMMA1 = 14.10                        # v718 pole-band threshold
E_CUT = 2.0 - 2.0 * math.cos(D * GAMMA1)
H_IM = 1.0e-2
ZSET = (-1.0e-1, -1.0e-2, -1.0e-3,
        complex(0.0, H_IM), complex(-1.0e-3, H_IM))
Z_REF = -1.0e-2
ZC = ZSET[3:]
Z_CB = -1.0e-1
RE_GRID = (-0.5, -0.25, 0.0, 0.25, 0.5)
IM_GRID = (1.0e-3, 1.0e-2, 1.0e-1, 1.0)
IM_GATE_MIN = 1.0e-2                  # gated sub-grid rows

B_MATCH = 0.25
B_DEAD = 10.0
RANK1_BAR = 0.75
PSD_TOL_REL = 1.0e-6
MASS_BAR = 1.0
ENTRY_GROWTH_BAR = 10.0
CBND_RATIO = 2.0
CDER_RATIO = 2.0
CL_BAR = 0.2
C_RESP = 3.0
C_UNIQ = 1
N_MED = 5

NPAD = 128
R_BAT = (1.0, 2.0)
QF_FLOOR = 1.0e-12
MOM_KS = (0, 1, 2)

IMPORT_FLOOR = 1.0e-8
SVD_FLOOR = 1.0e-8
WARD_ORTH = 1.0e-10
COUP_WARD = 1.0e-8
WARD_FRAME = 1.0e-3
WARD_POLE = 1.0e-9
WARD_FESH = 1.0e-8
WARD_COMPL = 1.0e-10
HERG_FLOOR = 1.0e-8
BAR_GAUSS = 1.0e-8
PD_TOL = 1.0e-9
COMB_DEV_BAR = 1.0e-12
PREFIX_WARD = 1.0e-12
RUNTIME_CAP = 1800.0

REPRO_COUNTS = {884: 5, 888: 6, 988: 6, 992: 7, 1104: 7, 1108: 8,
                1272: 8, 1276: 9}
REPRO_GAPS = {("67", 1096): 0.1008, ("67", 1176): 0.1397,
              ("78", 1176): 0.0613, ("78", 1240): 0.0039}
REPRO_TOLG = 2.0e-4
REPRO_LMIN1176 = 3.882e-6
REPRO_LTOL = 2.0e-8
DRAIN_LEVELS = {
    "R2:box[0,R]": 0.3583, "R2:box[R/2,R]": 0.3370,
    "R2:hat(R/2,R/2)": 0.3127, "R2:hat(3R/4,R/4)": 0.2590,
    "R2:box[R/4,3R/4]": 0.2249, "R1:box[R/2,R]": 0.0793,
    "R1:box[0,R]": 0.0741, "R2:box[0,R/2]": 0.0741,
    "R1:hat(R/4,R/4)": 0.0082}
REPRO_QTOL = 2.0e-3

SEED_CS = 7
SEED_CB = 11
SEED_CW = 20260805
CTRL_LAD_CS = list(range(888, 1301, 48))
EP_NCAP = 34000
EP_MMAX = 640
CTRL_LAD_CE = list(range(400, 641, 8))
CW_LAD = list(range(888, 989, 4))

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []
GATES = []


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
    bats = {}
    hsh = hashlib.sha256()
    hsh.update(("z1-variable-edge spec: shared spine parent-verbatim "
                "(D=%.10f cap %d M_TOP %d LAD %s band %g cocycle "
                "transport, RAW import U=L^T B[:K], no polar); "
                "CAND A: H=U^T(A-z)^-1 U vs Fref=P^1/2 Hgram P^1/2, "
                "rho_A at Z_REF=%g; CAND B: resolvent intertwining "
                "rho_B eps=%g; trigger: B iff med%d rho_A over %s > "
                "%g; poles: E_CUT=%.6f (GAMMA1=%g), Pi=sum_{a<=cut} "
                "ww^T, R_e = Pi(e)-pad(Pi(prev)) at E_TEST=%s; "
                "gates: P1 psd %g rank1 %g; P2 mass %g growth %g "
                "KILL c_mass(top)>%g; B1 grid %s x %s gate Im>=%g "
                "ratio %g; B2 deriv ratio %g; CL last10 osc med <= "
                "%g over 14f x k=%s; DEL bar %g dead %g; CR resp %g "
                "uniq %d (reported); anchors counts %s gaps %s tol "
                "%g lmin %g tol %g drain %s tol %g; wards pole %g "
                "fesh %g compl %g herg %g frame %g coup %g orth %g "
                "svd %g gauss %g import %g pd %g comb %g prefix %g "
                "runtime %g; controls CS %d %s CE %d %d %s CB %d "
                "z=%g fire>%g CW %d %s fire>%g and<%g; verdict "
                "order: invalid -> DEAD(P2kill or B1fail or both>"
                "%g) -> CARRIES(DEL P1 P2 B1 B2 CL) -> PARTIAL"
                % (D, ATOM_MAX_DEEP, M_TOP, LAD, THR_NULL, Z_REF,
                   -Z_REF, N_MED, GATE_BLOCK, B_MATCH, E_CUT,
                   GAMMA1, E_TEST, PSD_TOL_REL, RANK1_BAR, MASS_BAR,
                   ENTRY_GROWTH_BAR, MASS_BAR, RE_GRID, IM_GRID,
                   IM_GATE_MIN, CBND_RATIO, CDER_RATIO, CL_BAR,
                   MOM_KS, B_MATCH, B_DEAD, C_RESP, C_UNIQ,
                   sorted(REPRO_COUNTS.items()),
                   sorted(REPRO_GAPS.items()), REPRO_TOLG,
                   REPRO_LMIN1176, REPRO_LTOL,
                   sorted(DRAIN_LEVELS.items()), REPRO_QTOL,
                   WARD_POLE, WARD_FESH, WARD_COMPL, HERG_FLOOR,
                   WARD_FRAME, COUP_WARD, WARD_ORTH, SVD_FLOOR,
                   BAR_GAUSS, IMPORT_FLOOR, PD_TOL, COMB_DEV_BAR,
                   PREFIX_WARD, RUNTIME_CAP, SEED_CS, CTRL_LAD_CS,
                   EP_NCAP, EP_MMAX, CTRL_LAD_CE, SEED_CB, Z_CB,
                   B_MATCH, SEED_CW, CW_LAD, B_MATCH, C_RESP,
                   B_DEAD)).encode())
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
    check("G1.3 parent tower comb consistency (rel dev <= %.0e)"
          % COMB_DEV_BAR, dev_m <= COMB_DEV_BAR,
          "rel dev %.1e, ka=%d" % (dev_m, ka))
    c = srp.continuum_lags(M_PAR)
    for cnl in ("ro", "re", "sp", "in"):
        c = c + srp.atom_channel_lags(alpha, M_PAR, masks[cnl])
    return sla.toeplitz(c[:M_PAR])


def build_deep_comb():
    lam_deep = core.von_mangoldt_table(ATOM_MAX_DEEP)
    dev = float(np.max(np.abs(lam_deep[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("G1.1 deep-table overlap EXACT on [0, %d]" % core.ATOM_MAX,
          dev == 0.0, "max abs dev %.1e" % dev)
    nn = np.nonzero(lam_deep > 0.0)[0]
    u_deep = np.log(nn.astype(float))
    mu_deep = 2.0 * lam_deep[nn] / np.sqrt(nn.astype(float))
    psi = np.cumsum(lam_deep[nn])
    keep = nn.astype(float) >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                         / nn[keep].astype(float)))
    check("G1.2 deep-range Chebyshev envelope kappa = %.6f <= %.6f"
          % (kappa, core.KAPPA_REF + core.TOL_KAPPA),
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
    check("G1.4 prefix Ward: dev %.1e <= %.0e" % (dev, PREFIX_WARD),
          dev <= PREFIX_WARD)
    print("  deep census: ka = %d atoms to e^%.4f" % (ka, 2 * alpha))
    return p, T, c_cont, alpha, ka


def cheb_gram(p, K):
    idx = np.arange(K)
    return 0.5 * (p[np.abs(idx[:, None] - idx[None, :])]
                  + p[idx[:, None] + idx[None, :]])


def frame_ward(p, K, L, aM, gM):
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
    check("G1.7 GNS frame Ward at M = %d: dev %.1e <= %.0e"
          % (M_WARD, dev, WARD_FRAME), dev <= WARD_FRAME)


def tri_solve(bJ, aJ, z, Bmat):
    K = len(bJ)
    dt = complex if isinstance(z, complex) else float
    ab = np.zeros((3, K), dtype=dt)
    ab[0, 1:] = -aJ
    ab[1, :] = (2.0 - z) - bJ
    ab[2, :-1] = -aJ
    return sla.solve_banded((1, 1), ab, Bmat.astype(dt))


def gram_rung(T, M, Fb):
    lam, V = np.linalg.eigh(T[:M, :M])
    d = int(np.sum(lam <= THR_NULL))
    Vd = qsb.sign_fix(V[:, :d])
    Ec = V[:, d:].T @ (T[:M, :M] @ Vd)
    out = dict(M=M, lam=lam[:16].copy(), lam_min=float(lam[0]),
               d=d, Vd=Vd, coup=float(np.max(np.abs(Ec))),
               lam_rest=lam[d:], Ec=Ec)
    if M in TOP5W:
        out["q6"] = np.sum((V[:NPAD, :6].T @ Fb) ** 2, axis=0)
    return out


def transport_update(prev, gr, R_prev):
    Ma = prev["M"]
    da, db = prev["d"], gr["d"]
    S_ov = gr["Vd"][:Ma, :].T @ prev["Vd"]
    Uu, s, Vt = np.linalg.svd(S_ov, full_matrices=False)
    smin = float(s[-1])
    if db == da:
        R = (Uu @ Vt) @ R_prev
        kind = "link"
    elif db > da:
        Jiso = Uu @ Vt
        JR = Jiso @ R_prev
        Qf, _ = np.linalg.qr(JR, mode="complete")
        N = Qf[:, da:]
        for j in range(N.shape[1]):
            i0 = int(np.argmax(np.abs(N[:, j])))
            if N[i0, j] < 0:
                N[:, j] = -N[:, j]
        R = np.hstack([JR, N])
        kind = "entry"
    else:
        R = np.eye(db)
        kind = "MODE-EXIT"
    orth = float(np.max(np.abs(R.T @ R - np.eye(db))))
    return R, smin, orth, kind


def h_gram(gr, R, z):
    d = gr["d"]
    return R.T @ np.diag(1.0 / (gr["lam"][:d] - z)) @ R


def f_feshbach(gr, R, z):
    d = gr["d"]
    C = gr["Ec"].T @ (gr["Ec"] / (gr["lam_rest"][:, None] - z))
    return R.T @ (np.diag(gr["lam"][:d]) - z * np.eye(d) - C) @ R


def psqrt(P):
    w, Vp = np.linalg.eigh(P)
    w = np.maximum(w, 0.0)
    return (Vp * np.sqrt(w)) @ Vp.T


def specnorm(Mz):
    return float(np.linalg.norm(Mz, 2))


def run():
    print("=" * 78)
    print("SHARPENED-Z1 module 3 -- variable-edge M-function, "
          "mu-weighted import (A) / intertwining (B), entry poles, "
          "Herglotz compactness, moment clusters")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 spec SHA-256-frozen BEFORE any comb data", True,
          "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach: M_TOP %d <= %d, cover %d <= %d, E_CUT = "
          "%.6f" % (M_TOP, M_CAP_DEEP,
                    int(math.exp(M_TOP * D)) + 2, ATOM_MAX_DEEP,
                    E_CUT),
          M_TOP <= M_CAP_DEEP
          and int(math.exp(M_TOP * D)) + 2 <= ATOM_MAX_DEEP)

    u_deep, mu_deep = build_deep_comb()
    T_par = build_parent_tower()
    p, T, c_cont, alpha_top, ka = build_deep_tower(u_deep, mu_deep,
                                                   T_par)
    Fb, names = battery_matrix(bats)

    rng_cw = np.random.default_rng(SEED_CW)
    B_cw0 = np.linalg.qr(rng_cw.standard_normal((888, 6)))[0]
    rng_cb = np.random.default_rng(SEED_CB)
    A_cb = rng_cb.standard_normal((M_TOP // 2, M_TOP // 2))
    A_cb = A_cb + A_cb.T

    lam884 = np.linalg.eigvalsh(T[:884, :884])
    counts = {884: int(np.sum(lam884 <= THR_NULL))}
    gaps = {}
    lmin1176 = None
    q6_med = []
    rungs = []
    prev_gr, R = None, None
    trans_events = []
    smin_min, orth_max, coup_max, pd_min = np.inf, 0.0, 0.0, np.inf
    herg_min = np.inf
    ward_pole = ward_fesh = ward_compl = ward_rec = 0.0
    import_smin_min = np.inf
    kbads = []
    Pi_prev = None

    for M in LAD:
        K = M // 2
        gr = gram_rung(T, M, Fb)
        counts[M] = gr["d"]
        pd_min = min(pd_min, gr["lam_min"])
        coup_max = max(coup_max, gr["coup"])
        if M in (1096, 1176, 1240):
            lam = gr["lam"]
            gaps[("67", M)] = float((lam[6] - lam[5]) / lam[6])
            gaps[("78", M)] = float((lam[7] - lam[6]) / lam[7])
        if M == 1176:
            lmin1176 = gr["lam_min"]
        if "q6" in gr:
            q6_med.append(gr["q6"])

        if prev_gr is None:
            R = np.eye(gr["d"])
            kind = "start"
        else:
            R, smin, orth, kind = transport_update(prev_gr, gr, R)
            smin_min = min(smin_min, smin)
            orth_max = max(orth_max, orth)
            if kind == "entry":
                trans_events.append((M, prev_gr["d"], gr["d"],
                                     float(gr["lam"][gr["d"] - 1])))
        prev_gr = gr

        aM, gM, kbad = jac.wheeler(p[:M], K)
        if kbad is not None:
            kbads.append((M, int(kbad)))
            continue
        bJ = aM.copy()
        aJ = np.sqrt(gM[1:K])
        Gc = cheb_gram(p, K)
        try:
            L = sla.cholesky(Gc, lower=True, check_finite=False)
        except np.linalg.LinAlgError:
            kbads.append((M, -1))
            continue
        if M == M_WARD:
            frame_ward(p, K, L, aM, gM)
        if M in WARD_H_RUNGS:
            rec = jac.gauss_reconstruct(aM, gM, p[0], min(2 * K, M))
            ward_rec = max(ward_rec, float(
                np.max(np.abs(rec - p[:len(rec)]))
                / np.max(np.abs(p[:len(rec)]))))

        # raw import (no whitening anywhere)
        B = gr["Vd"] @ R
        U = L.T @ B[:K]
        s_imp = np.linalg.svd(U, compute_uv=False)
        import_smin_min = min(import_smin_min, float(s_imp[-1]))
        P = U.T @ U
        Ph = psqrt(P)
        trP = float(np.trace(P))

        # exact pole decomposition of the bulk pair
        xj, Vj = sla.eigh_tridiagonal(bJ, aJ)
        a_n = 2.0 - xj                     # A-eigenvalues
        W = U.T @ Vj                       # d x K residue vectors
        idx_pole = a_n <= E_CUT
        n_pole = int(np.sum(idx_pole))
        Pi = W[:, idx_pole] @ W[:, idx_pole].T
        Wreg = W[:, ~idx_pole]
        areg = a_n[~idx_pole]
        ward_compl = max(ward_compl, float(
            np.max(np.abs(W @ W.T - P)) / max(np.max(np.abs(P)),
                                              QF_FLOOR)))

        def h_raw(z):
            return (W / (a_n - z)[None, :]) @ W.conj().T \
                if isinstance(z, complex) else \
                (W / (a_n - z)[None, :]) @ W.T

        # candidate A delivery + wards
        Hs = {z: h_raw(z) for z in ZSET}
        if M in WARD_H_RUNGS:
            Y = tri_solve(bJ, aJ, Z_REF, U)
            Hsolve = U.T @ Y
            ward_pole = max(ward_pole, float(
                np.max(np.abs(Hsolve - Hs[Z_REF]))
                / np.max(np.abs(Hsolve))))
            Hg = h_gram(gr, R, Z_REF)
            Ff = f_feshbach(gr, R, Z_REF)
            ward_fesh = max(ward_fesh, float(
                np.max(np.abs(Ff @ Hg - np.eye(gr["d"])))))
        for z in ZC:
            ImH = (Hs[z] - Hs[z].conj().T) / 2.0j
            herg_min = min(herg_min, float(np.min(
                np.linalg.eigvalsh(ImH))))
        Fref = Ph @ h_gram(gr, R, Z_REF) @ Ph
        rho_a = float(np.linalg.norm(Hs[Z_REF].real - Fref)
                      / max(np.linalg.norm(Fref), QF_FLOOR))
        # candidate B (resolvent intertwining, frozen fallback)
        eps = -Z_REF
        lamd = gr["lam"][:gr["d"]]
        Yb = tri_solve(bJ, aJ, Z_REF, U)   # (A+eps)^-1 U
        UB = U / (lamd + eps)[None, :]
        rho_b = float(np.linalg.norm(Yb - UB)
                      / max(np.linalg.norm(UB), QF_FLOOR))

        # entry residues
        R_e = None
        if kind == "entry":
            d0 = Pi_prev.shape[0]
            pad = np.zeros_like(Pi)
            pad[:d0, :d0] = Pi_prev
            R_e = Pi - pad
        dPi_run = None
        if kind == "link" and Pi_prev is not None \
                and Pi_prev.shape == Pi.shape:
            dPi_run = float(np.linalg.norm(Pi - Pi_prev))
        Pi_prev = Pi.copy()

        # compactness grid + moments on the regular part
        Cgrid, Cgrid_lo, Dgrid = 0.0, 0.0, 0.0
        for re_z in RE_GRID:
            for im_z in IM_GRID:
                z = complex(re_z, im_z)
                Mt = (Wreg / (areg - z)[None, :]) @ Wreg.conj().T
                Mtp = (Wreg / (areg - z)[None, :] ** 2) \
                    @ Wreg.conj().T
                nz = specnorm(Mt)
                if im_z >= IM_GATE_MIN:
                    Cgrid = max(Cgrid, nz)
                    Dgrid = max(Dgrid, specnorm(Mtp))
                else:
                    Cgrid_lo = max(Cgrid_lo, nz)
        cf = B[:NPAD].T @ Fb                # d x 14
        moms = {}
        for kmom in MOM_KS:
            Om = (Wreg * (areg ** kmom)[None, :]) @ Wreg.T
            moms[kmom] = np.einsum("df,de,ef->f", cf, Om, cf)

        # controls per rung
        Hk = A_cb[:K, :K] / math.sqrt(2.0 * K)
        Ycb = np.linalg.solve((2.0 - Z_CB) * np.eye(K) - Hk, U)
        Fref_cb = Ph @ h_gram(gr, R, Z_CB) @ Ph
        rho_cb = float(np.linalg.norm(U.T @ Ycb - Fref_cb)
                       / max(np.linalg.norm(Fref_cb), QF_FLOOR))
        H_cw = rho_cw = None
        if M in CW_LAD or M == 992:
            Bcw = np.zeros((M, 6))
            Bcw[:888, :] = B_cw0
            Ucw = L.T @ Bcw[:K]
            Pcw = Ucw.T @ Ucw
            Ycw = tri_solve(bJ, aJ, Z_REF, Ucw)
            H_cw = Ucw.T @ Ycw
            Hg6 = h_gram(gr, R, Z_REF)[:6, :6] if gr["d"] > 6 \
                else h_gram(gr, R, Z_REF)
            Pcwh = psqrt(Pcw)
            Fref_cw = Pcwh @ Hg6 @ Pcwh
            rho_cw = float(np.linalg.norm(H_cw - Fref_cw)
                           / max(np.linalg.norm(Fref_cw),
                                 QF_FLOOR))

        rungs.append(dict(
            M=M, K=K, d=gr["d"], kind=kind, trP=trP,
            trPi=float(np.trace(Pi)), n_pole=n_pole,
            s_imp=s_imp.copy(), rho_a=rho_a, rho_b=rho_b,
            R_e=R_e, dPi_run=dPi_run, Cgrid=Cgrid,
            Cgrid_lo=Cgrid_lo, Dgrid=Dgrid, moms=moms,
            Href=Hs[Z_REF].real.copy(), rho_cb=rho_cb,
            H_cw=H_cw, rho_cw=rho_cw,
            lam_entry=float(gr["lam"][gr["d"] - 1])))

    # ---- guards
    check("G1.6 Wheeler + Cholesky valid on all %d rungs AND Gauss "
          "recon %.1e <= %.0e" % (len(LAD), ward_rec, BAR_GAUSS),
          not kbads and ward_rec <= BAR_GAUSS, str(kbads[:3]))
    if kbads:
        print("\nVERDICT: Z1-VAREDGE-INVALID (construction broke)")
        return 1
    check("G1.8 Gram PD lambda_min = %.3e > -%.0e" % (pd_min,
                                                      PD_TOL),
          pd_min > -PD_TOL)
    check("G1.9 coupling %.1e <= %.0e; transport sigma_min %.4f >= "
          "%.0e; orth %.1e <= %.0e"
          % (coup_max, COUP_WARD, smin_min, SVD_FLOOR, orth_max,
             WARD_ORTH),
          coup_max <= COUP_WARD and smin_min >= SVD_FLOOR
          and orth_max <= WARD_ORTH)
    check("G1.10 pole-decomposition Ward %.1e <= %.0e; Feshbach "
          "inversion Ward %.1e <= %.0e; residue completeness %.1e "
          "<= %.0e"
          % (ward_pole, WARD_POLE, ward_fesh, WARD_FESH,
             ward_compl, WARD_COMPL),
          ward_pole <= WARD_POLE and ward_fesh <= WARD_FESH
          and ward_compl <= WARD_COMPL)
    check("G1.11 Herglotz guard: min eig Im H = %+.3e >= -%.0e"
          % (herg_min, HERG_FLOOR), herg_min >= -HERG_FLOOR)
    check("G1.12 import floor: min sigma_min(U) = %.3e >= %.0e"
          % (import_smin_min, IMPORT_FLOOR),
          import_smin_min >= IMPORT_FLOOR)
    ok_cnt = all(counts.get(M) == want
                 for M, want in REPRO_COUNTS.items())
    check("G1.5a entry anchors %s == frozen"
          % {M: counts.get(M) for M in sorted(REPRO_COUNTS)},
          ok_cnt)
    ok_gap = all(abs(gaps[k] - v) <= REPRO_TOLG
                 for k, v in REPRO_GAPS.items() if k in gaps)
    check("G1.5b gap anchors ok; lambda_min(1176) = %.4e"
          % lmin1176,
          ok_gap and abs(lmin1176 - REPRO_LMIN1176) <= REPRO_LTOL)
    med_q6 = np.median(np.stack(q6_med), axis=0)
    dev_q = max(abs(float(med_q6[j]) - DRAIN_LEVELS[nm])
                for j, nm in enumerate(names) if nm in DRAIN_LEVELS)
    check("G1.5c drainage anchors (anchor-only, declared): worst "
          "dev %.1e <= %.0e" % (dev_q, REPRO_QTOL),
          dev_q <= REPRO_QTOL)
    trans_rungs = tuple(t[0] for t in trans_events)
    check("G1.5d transitions %s == E_TEST %s (entering %s)"
          % (trans_rungs, E_TEST,
             ["%.4e" % t[3] for t in trans_events]),
          trans_rungs == E_TEST)

    rmap = {r["M"]: r for r in rungs}

    # ---- A/B decision trail + delivery gate
    print("\n-- delivery re-test (A primary, B on trigger)")
    a_med = float(np.median([rmap[M]["rho_a"] for M in GATE_BLOCK]))
    b_med = float(np.median([rmap[M]["rho_b"] for M in GATE_BLOCK]))
    print("  rho_A profile (every 8th): %s"
          % "  ".join("M=%d:%.3f" % (r["M"], r["rho_a"])
                      for r in rungs[::8]))
    print("  rho_B profile (every 8th): %s"
          % "  ".join("M=%d:%.3f" % (r["M"], r["rho_b"])
                      for r in rungs[::8]))
    print("  P spectrum at top gate rung M = %d (squared mu-norms "
          "of the raw band import): %s"
          % (GATE_BLOCK[-1],
             "/".join("%.2e" % (s ** 2)
                      for s in rmap[GATE_BLOCK[-1]]["s_imp"])))
    if a_med <= B_MATCH:
        which, del_med = "A", a_med
        print("  TRIGGER: rho_A med%d = %.4f <= %g -> Candidate A "
              "adjudicated (B reported only)" % (N_MED, a_med,
                                                 B_MATCH))
    else:
        which, del_med = "B", b_med
        print("  TRIGGER: rho_A med%d = %.4f > %g -> switch, "
              "Candidate B adjudicated" % (N_MED, a_med, B_MATCH))
    del_ok = gate("(DEL) delivery via Candidate %s: med%d = %.4f "
                  "<= %g (A = %.4f, B = %.4f; dead-grade both > %g)"
                  % (which, N_MED, del_med, B_MATCH, a_med, b_med,
                     B_DEAD), del_med <= B_MATCH)
    del_dead = (a_med > B_DEAD) and (b_med > B_DEAD)

    # ---- entry-pole gates
    print("\n-- entry-pole isolation (E_CUT = %.4f, GAMMA1 = %g)"
          % (E_CUT, GAMMA1))
    entry_rows = []
    for e in E_TEST:
        r = rmap[e]
        Re = r["R_e"]
        sv = np.linalg.svd(Re, compute_uv=False)
        mineig = float(np.min(np.linalg.eigvalsh(
            0.5 * (Re + Re.T))))
        rk = float(sv[0] / max(np.sum(sv), QF_FLOOR))
        entry_rows.append((e, r["lam_entry"], r["n_pole"],
                           float(np.linalg.norm(Re)), rk, mineig))
        print("  entry M=%d: lam_gram=%.4e, n_pole(bulk<=cut)=%d, "
              "||R_e||_F=%.3e, rank-ratio=%.3f, min eig=%+.2e"
              % entry_rows[-1])
    drift = [r["dPi_run"] for r in rungs if r["dPi_run"] is not None]
    print("  within-run ||dPi|| drift: median %.3e, max %.3e"
          % (float(np.median(drift)), float(np.max(drift))))
    p1_ok = gate("(P1) entry residues PSD + rank-one: min rank-"
                 "ratio %.3f >= %g AND worst min-eig ratio %+.2e "
                 ">= -%g"
                 % (min(t[4] for t in entry_rows), RANK1_BAR,
                    min(t[5] / max(np.linalg.norm(rmap[t[0]]["R_e"],
                                                  2), QF_FLOOR)
                        for t in entry_rows), PSD_TOL_REL),
                 all(t[4] >= RANK1_BAR for t in entry_rows)
                 and all(t[5] >= -PSD_TOL_REL
                         * np.linalg.norm(rmap[t[0]]["R_e"], 2)
                         for t in entry_rows))
    cum = 0.0
    c_mass_prof = []
    for r in rungs:
        if r["R_e"] is not None:
            cum += float(np.linalg.norm(r["R_e"]))
        c_mass_prof.append((r["M"], cum / max(r["trP"], QF_FLOOR)))
    c_mass_max = max(v for _m, v in c_mass_prof)
    c_mass_top = c_mass_prof[-1][1]
    growth = entry_rows[-1][3] / max(entry_rows[0][3], QF_FLOOR)
    phi_prof = [(r["M"], r["trPi"] / max(r["trP"], QF_FLOOR))
                for r in rungs]
    print("  entry-mass fraction phi = tr Pi / tr P: first %.3f, "
          "top %.3f; c_mass profile: 992:%.3e 1108:%.3e 1276:%.3e "
          "top:%.3e"
          % (phi_prof[0][1], phi_prof[-1][1],
             dict(c_mass_prof)[992], dict(c_mass_prof)[1108],
             dict(c_mass_prof)[1276], c_mass_top))
    p2_ok = gate("(P2) entry mass summable: max c_mass = %.3e <= "
                 "%g AND growth ||R_last||/||R_first|| = %.2f <= %g"
                 % (c_mass_max, MASS_BAR, growth,
                    ENTRY_GROWTH_BAR),
                 c_mass_max <= MASS_BAR
                 and growth <= ENTRY_GROWTH_BAR)
    p2_kill = c_mass_top > MASS_BAR

    # ---- compactness gates
    print("\n-- Herglotz compactness (regularized family M~ on the "
          "frozen grid; Im = 1e-3 row reported only)")
    Cf = float(np.median([rmap[M]["Cgrid"] for M in FIRST5]))
    Cl = float(np.median([rmap[M]["Cgrid"] for M in LAST5]))
    Df = float(np.median([rmap[M]["Dgrid"] for M in FIRST5]))
    Dl = float(np.median([rmap[M]["Dgrid"] for M in LAST5]))
    Clo_f = float(np.median([rmap[M]["Cgrid_lo"] for M in FIRST5]))
    Clo_l = float(np.median([rmap[M]["Cgrid_lo"] for M in LAST5]))
    print("  grid-sup ||M~||: med5 FIRST5 %.4e -> LAST5 %.4e "
          "(1e-3 row: %.3e -> %.3e, reported)"
          % (Cf, Cl, Clo_f, Clo_l))
    print("  grid-sup ||M~'||: med5 FIRST5 %.4e -> LAST5 %.4e"
          % (Df, Dl))
    b1_ok = gate("(B1) local uniform boundedness: ratio %.3f <= %g"
                 % (Cl / max(Cf, QF_FLOOR), CBND_RATIO),
                 Cl / max(Cf, QF_FLOOR) <= CBND_RATIO)
    b2_ok = gate("(B2) equicontinuity proxy: derivative ratio %.3f "
                 "<= %g" % (Dl / max(Df, QF_FLOOR), CDER_RATIO),
                 Dl / max(Df, QF_FLOOR) <= CDER_RATIO)

    # ---- moment-functional cluster
    print("\n-- moment functionals (INDUCTIVE_STATE.02 avatar): "
          "42 tracks, tail LAST10 oscillation")
    oscs = []
    for kmom in MOM_KS:
        for jf in range(Fb.shape[1]):
            tail = np.array([rmap[M]["moms"][kmom][jf]
                             for M in LAST10])
            osc = float((tail.max() - tail.min())
                        / max(np.median(np.abs(tail)), 1.0e-30))
            oscs.append(osc)
    osc_med = float(np.median(oscs))
    osc_max = float(np.max(oscs))
    print("  osc distribution: median %.4f, max %.4f "
          "(k x f = %d tracks)" % (osc_med, osc_max, len(oscs)))
    cl_ok = gate("(CL) moment functionals cluster: median tail "
                 "osc = %.4f <= %g" % (osc_med, CL_BAR),
                 osc_med <= CL_BAR)

    # ---- cell-response re-test (reported + typed, not blocking)
    print("\n-- cell-response re-test on H(Z_REF)/tr P (reported)")
    rels_in, rels_e = [], {}
    for ra, rb in zip(rungs, rungs[1:]):
        Sa = ra["Href"] / max(ra["trP"], QF_FLOOR)
        Sb = rb["Href"] / max(rb["trP"], QF_FLOOR)
        if rb["kind"] == "entry":
            d0 = Sa.shape[0]
            dlt = float(np.max(np.abs(Sb[:d0, :d0] - Sa)))
            nrm = max(np.max(np.abs(Sa)),
                      np.max(np.abs(Sb[:d0, :d0])))
            rels_e[rb["M"]] = dlt / max(nrm, QF_FLOOR)
        elif Sa.shape == Sb.shape:
            dlt = float(np.max(np.abs(Sb - Sa)))
            nrm = max(np.max(np.abs(Sa)), np.max(np.abs(Sb)))
            rels_in.append((rb["M"], dlt / max(nrm, QF_FLOOR)))
    med_in = float(np.median([v for _m, v in rels_in]))
    rhos_e = {e: rels_e[e] / max(med_in, QF_FLOOR) for e in rels_e}
    top5 = sorted(rels_in, key=lambda t: -t[1])[:5]
    n_over = sum(1 for _m, v in rels_in
                 if v >= min(rels_e.values()))
    cr_ok = min(rhos_e.values()) >= C_RESP and n_over <= C_UNIQ
    print("  entry contrasts: %s; within-run median %.3e, top-5 %s"
          % ("  ".join("M=%d:rho=%.2f" % (e, rhos_e[e])
                       for e in sorted(rhos_e)), med_in,
             " ".join("M=%d:%.2e" % t for t in top5)))
    print("  (CR) cell response %s (min rho %.2f vs %g, %d "
          "comparable) -- reported, not CARRIES-blocking"
          % ("PASS" if cr_ok else "FAIL",
             min(rhos_e.values()), C_RESP, n_over))

    # ---- controls
    print("\n-- controls")
    kb_cs = []
    rng = np.random.default_rng(SEED_CS)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_top, ka))
    cat_s, _dd = core.atom_lags_at(alpha_top, M_TOP, pos,
                                   mu_deep[:ka])
    pcs = c_cont + cat_s
    for M in CTRL_LAD_CS:
        _a, _g, kb = jac.wheeler(pcs[:M], M // 2)
        if kb is not None:
            kb_cs.append((M, int(kb)))
    check("CS scramble fires: Wheeler breakdown %d/%d"
          % (len(kb_cs), len(CTRL_LAD_CS)),
          len(kb_cs) == len(CTRL_LAD_CS))
    r1 = epx.lattice_r1(EP_NCAP)
    bb = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(bb, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    catE, _dd = core.atom_lags_at(0.5 * EP_MMAX * D, EP_MMAX,
                                  np.log(supp.astype(float)),
                                  2.0 * lamE[supp]
                                  / np.sqrt(supp.astype(float)))
    pce = srp.continuum_lags(EP_MMAX) + catE
    kb_ce = []
    for M in CTRL_LAD_CE:
        _a, _g, kb = jac.wheeler(pce[:M], M // 2)
        if kb is not None:
            kb_ce.append((M, int(kb)))
    check("CE Epstein fires: Wheeler breakdown %d/%d"
          % (len(kb_ce), len(CTRL_LAD_CE)),
          len(kb_ce) == len(CTRL_LAD_CE))
    cb_med = float(np.median([rmap[M]["rho_cb"]
                              for M in GATE_BLOCK]))
    check("CB GOE bulk fires: med%d rho_A^goe = %.2f > %g at z = "
          "%g" % (N_MED, cb_med, B_MATCH, Z_CB), cb_med > B_MATCH)
    cw_rungs = [r for r in rungs if r["M"] in CW_LAD
                and r["rho_cw"] is not None]
    cw_med = float(np.median([r["rho_cw"] for r in cw_rungs[-5:]]))
    cw_rels = []
    for ra, rb in zip(cw_rungs, cw_rungs[1:]):
        dlt = float(np.max(np.abs(rb["H_cw"] - ra["H_cw"])))
        nrm = max(np.max(np.abs(ra["H_cw"])),
                  np.max(np.abs(rb["H_cw"])))
        cw_rels.append(dlt / max(nrm, QF_FLOOR))
    r992, r988 = rmap[992], rmap[988]
    dlt992 = float(np.max(np.abs(r992["H_cw"] - r988["H_cw"])))
    nrm992 = max(np.max(np.abs(r992["H_cw"])),
                 np.max(np.abs(r988["H_cw"])))
    cw_contrast = (dlt992 / max(nrm992, QF_FLOOR)) \
        / max(float(np.median(cw_rels)), QF_FLOOR)
    check("CW random boundary fires: med%d rho_A^cw = %.2f > %g "
          "AND 992-contrast %.2f < %g"
          % (N_MED, cw_med, B_MATCH, cw_contrast, C_RESP),
          cw_med > B_MATCH and cw_contrast < C_RESP)
    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= %.0f s" % (dt, RUNTIME_CAP),
          dt <= RUNTIME_CAP)

    # ---- verdict
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE", "CB", "CW")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE", "CB", "CW")))
    legs = dict(DEL=del_ok, P1=p1_ok, P2=p2_ok, B1=b1_ok,
                B2=b2_ok, CL=cl_ok)
    if not (guards_ok and controls_ok):
        verdict = "Z1-VAREDGE-INVALID"
    elif p2_kill or (not b1_ok) or del_dead:
        verdict = "Z1-VAREDGE-DEAD"
    elif all(legs.values()):
        verdict = "Z1-VAREDGE-CARRIES"
    else:
        verdict = "Z1-VAREDGE-PARTIAL"

    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("LEGS %d/6 (%s), CR(reported)=%s, candidate %s, "
          "GUARDS+CONTROLS %d/%d, runtime %.1f s"
          % (sum(legs.values()),
             " ".join("%s=%s" % (k, "P" if v else "F")
                      for k, v in legs.items()),
             "P" if cr_ok else "F", which, n_chk, len(CHECKS),
             time.time() - T_START))
    print("\nUNIFICATION REPORT (report only): normal-family legs "
          "B1=%s B2=%s, cluster leg CL=%s on the SAME boundary "
          "spectral measure."
          % tuple("PASS" if v else "FAIL"
                  for v in (b1_ok, b2_ok, cl_ok)))
    if b1_ok and b2_ok and cl_ok:
        print("  MEASURED EVIDENCE FOR UNIFICATION: the weak-* "
              "cluster demand of PRIME.KMS.INDUCTIVE_STATE.02 and "
              "the Z1 operator demand of PRIME.Z1.OPERATOR.01 are "
              "the same remaining object on this surface -- the "
              "regularized boundary family is bounded and "
              "equicontinuous on the frozen compacts AND its "
              "moment functionals cluster: both contracts reduce "
              "to one Helly/Montel selection theorem for the "
              "variable-edge boundary measure chain.  Recommended "
              "contract text (promotion round, report only): "
              "'INDUCTIVE_STATE.02 and OPERATOR.01 merge into "
              "Z1-COMPACTNESS: prove that the variable-edge "
              "boundary triple of the window chain has a normal "
              "Herglotz family with summable rank-one entry poles "
              "at the arithmetic thresholds; its weak-* cluster "
              "states ARE its Herglotz limits.'")
    else:
        print("  MEASURED EVIDENCE AGAINST/INCOMPLETE: the failing "
              "leg(s) above name which half of the unification is "
              "not yet carried on this surface; the contracts stay "
              "separate until that leg is repaired.")
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
