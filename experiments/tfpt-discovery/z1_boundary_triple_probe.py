#!/usr/bin/env python3
"""SHARPENED-Z1 module 2 -- the boundary triple: J_K bulk + Gram
near-kernel boundary space; does its Weyl M-function deliver the qf
block, show the cell structure at the measured entry rungs, and does
the relative trace object of the pair track the deployed Weil
functional?  z1_boundary_triple_probe.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, no spectral-reality claim beyond measurement, and this probe
writes no files.  The construction path is AST-firewalled against
prime/zero identifiers; everything below is source-native (built
from the unified window measure and its Gram/GNS frames only).

INPUT STATE (frozen findings, none re-adjudicated here):
  *  z1_edge_signature_probe (Z1-SIGNATURE-PARTIAL, gates B/C/D):
     the N2 GNS/Jacobi family carries edge collisions (min
     boundary-pair gap 0.0032 vs source 0.0039), the ram-odd
     contact in its threshold band (cos 0.977..0.989 on LAST5),
     and settled positive battery couplings (14/14 P) -- but NOT
     the widening moving-edge cadence (its edge census is regular
     quadrature filling).  Constraint stated there: the cell
     structure must be imported as boundary data from the Gram
     near-kernel; this module is that construction.
  *  qf_edge_separation_probe (1e9 comb): source near-kernel
     entries at M = 888/992/1108/1276; avoided 7/8 crossing, gap
     0.0039 at M = 1240; anchors 6/7 gap(1096) = 0.1008,
     6/7(1176) = 0.1397, 7/8(1176) = 0.0613, lambda_min(1176) =
     3.882e-6, deep count 1 throughout.
  *  qf_cell_cocycle_probe (COCYCLE-DOMAIN-ONLY): the frozen band
     rule d(M) = #{lam <= 1e-4} with typed transitions; the
     Kato/polar transported frame with dimension embedding
     R' = [J R | N] at entries (J = thin-SVD polar isometry of the
     band overlap, N = sign-fixed orthonormal complement); the
     Nevanlinna/Stieltjes domain points z = i h, -1e-3 + i h
     (h = 1e-2) and eps in (1e-1, 1e-2, 1e-3).  These conventions
     are reused verbatim.
  *  qf_feshbach_effective_probe / qf_edge_separation_probe: the
     transported effective block F~_X(z) = R^T [Lambda_d(X) - z -
     C_d(z)] R with the MEASURED Schur correction C_d(z) =
     E_c^T diag(1/(lam_c - z)) E_c (machine scale, P A Q = 0
     coupling Ward) -- rebuilt here rung by rung, the reference
     object of the delivery gate.

COMPUTE-BUDGET DECLARATION (checked BEFORE this spec was frozen;
machine facts only, no spectra consulted): hw.memsize = 512 GB,
32 cores -- this is the benchmark machine of the edge probe (1e9
sieve 12.3 s / 13.5 GB peak; tents 8.0e5 atoms/s).  The deep cap is
therefore frozen at ATOM_MAX_DEEP = 1e9 so that the 9th entry at
M = 1276 is inside the gated ladder; M_TOP = 1300 (X = 20.3125,
sieve cover exp(20.3125) + 2 = 661,740,976 <= 1e9; M_CAP =
floor(64 ln 1e9) = 1326).  Runtime cap 1800 s predeclared.

CONSTRUCTION (all frozen before the first run):
  BULK: the N2 truncation family exactly as in the signature probe:
      at dyadic rung M (D = 1/64, X = M*D), K = M/2, Chebyshev
      moments p[:M] -> jac.wheeler -> orthonormal Jacobi J_K (v696/
      v718 machinery verbatim); GNS frame map c = L^T f with
      G_c[j,k] = (p_|j-k| + p_{j+k})/2 = L L^T (frame Ward at
      M = 888 as before).  DECLARED THRESHOLD DICTIONARY: the bulk
      operator of the triple is A_X := 2 I - J_K -- positive, with
      its threshold at 0 = the band edge x = 2 (the edge whose
      census carried the signature probe's gates B/C).  The Gram
      route's spectral parameter z -> 0- (below its near-kernel at
      0) and the triple's z -> 0- (below the bulk threshold at 0)
      are identified at the SAME z; this dictionary is DECLARED,
      not derived -- gate (b) is precisely the measurement of it.
  BOUNDARY SPACE: per rung, the transported Gram near-kernel band:
      d(M) = #{lam_i(T[:M,:M]) <= THR_NULL = 1e-4} (cocycle band
      rule verbatim; typed transitions expected exactly at the
      frozen entries 992 / 1108 / 1276); band basis V_d sign-fixed,
      chained frame R by Kato/polar links, dimension embedding
      R' = [J R | N] at entries (cocycle convention verbatim);
      transported cell basis B_X = V_d R (reference coordinates).
      IMPORT into the candidate frame: U_X = L^T B_X[:K] (the
      predeclared cell->cos avatar of the parent probes), polar
      factorization U = Q^ P (Q^ = the mu-orthonormal boundary
      frame, P = the import distortion, reported); import floor
      sigma_min(U) >= 1e-8 else typed IMPORT-COLLAPSE (delivery
      structurally impossible in the candidate frame).
  WEYL M-FUNCTION (frozen convention, stated exactly):
      H_X(z) := Q^_X^T (A_X - z)^{-1} Q^_X        (Herglotz leg)
      S_X(z) := H_X(z)^{-1}                        (delivered block)
      -- the Krein/Weyl M-function of the finite restriction-
      extension pair: S_X(z) equals the Schur complement of A - z
      onto the boundary space in any adapted orthonormal frame
      (block-inverse identity), so S is the triple's effective
      boundary operator and F~ is its Gram-route counterpart; both
      anti-Herglotz, both evaluated on the frozen z set
      ZSET = (-1e-1, -1e-2, -1e-3, i h, -1e-3 + i h), h = 1e-2,
      Z_REF = -1e-2 (edge-probe reference cell).  Wards: banded-
      solve residual <= 1e-9; S H = I <= 1e-8; H against a dense
      eigendecomposition evaluation at rungs 888 and 1272
      (<= 1e-9).
GATES (frozen; oscillation-aware where profiles are gated):
  (a) HERGLOTZ: min eig Im H_X(z) >= -1e-8 at both complex z on
      EVERY rung (structural; exact for a self-adjoint pair --
      a violation beyond 1e-6 is DEAD-grade).  Im S <= +1e-8
      (anti-Herglotz) reported as Ward.
  (b) QF-BLOCK DELIVERY (the identification gate): rho_b(X) =
      ||S_X(Z_REF) - F~_X(Z_REF)||_F / ||F~_X(Z_REF)||_F, both in
      the SAME transported reference coordinates; PASS iff med5
      over GATE_BLOCK = 1256..1272 (the last five rungs of the
      completed d = 8 run) <= B_MATCH = 0.25; STRUCTURAL FAIL
      (DEAD-grade) iff med5 > B_DEAD = 10 or import collapse --
      i.e. the boundary space does not ride the bulk threshold at
      all.  Full z-profile, eigenvalue tables and import health
      reported; the d = 9 frontier tail reported unadjudicated.
  (c) CELL STRUCTURE: relative max-entry increments of S(Z_REF)
      along the chained ladder (cocycle normalizer verbatim:
      rel_k = ||S_{k+1} - S_k||_max / max(||S_k||_max,
      ||S_{k+1}||_max); at a transition the compare is on the
      transported-old-frame corner S'[:d,:d], cocycle convention).
      Contrast statistic: rho(e) = rel(entry increment at e) /
      median(rel over all non-transition increments), for the
      frozen entry set E_TEST = (992, 1108, 1276).  PASS iff
      min_e rho(e) >= C_RESP = 3.0 AND at most 1 non-transition
      increment reaches min_e rel(e).  (All non-transition
      increments serve as the contrast population -- deterministic
      and stronger than a random-rung sample; deviation from the
      task wording declared.)  Known risk, typed up front: the
      Gram census entries are threshold bookkeeping, while the
      band's dynamical events are the crossings (gap bottoms
      1096..1100, 1240); if the response sits there instead, (c)
      fails with that named lesson.
  (d) TRACE-FORMULA PRECURSOR (measurement, typed so): battery
      autocorrelation polynomials g_f(x) = a_0(f) +
      2 sum_d a_d(f) T_d(x/2) (hbp battery verbatim, NPAD = 128;
      a_d(f) = autocorrelation lags of the padded cell vector).
      Ward (Gauss/Weil identity, the finite trace formula of the
      bulk): the GNS state omega(g_f) = sum_j p_0 U[0,j]^2
      g_f(x_j) equals the deployed Weil-functional evaluation
      w_f = a_0 p_0 + 2 sum_d a_d p_d at rel dev <= 1e-8 (checked
      at rungs 888/1108/1300).  GATE (the pair leg): the DECOUPLED
      system (bulk with the boundary condition cutting the
      boundary space off: J_D = P J P + P_perp J P_perp,
      P = Q^ Q^^T) must still track Weil:
      err_d(X) = sum_f |omega_D(g_f) - w_f| / sum_f |w_f|;
      PASS iff med5(GATE_BLOCK) <= D_LEVEL = 0.05 AND the
      second-half trend is falling-or-flat (hbp.fit_rate b >=
      -0.01 per X; b > 0 = falling, reported).
GUARDS (must pass or the run is invalid):
  G0.1 AST firewall; G0.2 SHA-256 freeze of battery bytes +
       ladders + bars + anchors BEFORE any comb data is built;
       G0.3 reach census + runtime cap;
  G1.1 deep-table overlap == deployed EXACTLY; G1.2 Chebyshev
       envelope kappa <= KAPPA_REF + 1e-6 over [100, 1e9]; G1.3
       parent tower comb consistency (<= 1e-12); G1.4 prefix Ward
       (<= 1e-12);
  G1.5 source anchors: (a) counts 884:5 888:6 988:6 992:7 1104:7
       1108:8 1272:8 1276:9 (the 9th entry INSIDE the ladder);
       (b) 6/7 gap(1096) = 0.1008, 6/7(1176) = 0.1397, 7/8(1176) =
       0.0613, 7/8(1240) = 0.0039 (each +- 2e-4);
       lambda_min(1176) = 3.882e-6 +- 2e-8; (c) drainage settled
       levels med5(1160..1176) reproduce the nine frozen values
       +- 2e-3; (d) measured transition set == frozen E_TEST;
  G1.6 Wheeler kbad None on every rung + Gauss moment
       reconstruction <= 1e-8 at 888/1108/1300; G1.7 GNS frame
       Ward at 888 (<= 1e-3); G1.8 Cholesky PD every rung +
       measured Gram PD lambda_min > -1e-9; G1.9 coupling Ward
       max |E_c| <= 1e-8 and transport Wards (sigma_min >= 1e-8,
       ||R^T R - I|| <= 1e-10); G1.10 resolvent/Schur Wards as
       declared above; G1.11 Gauss/Weil state identity <= 1e-8.
CONTROLS (mandatory, must fire):
  CS  position scramble (1e9 comb, masses kept, seed 7, rungs
      888..1300 step 48): FIRE iff the bulk construction breaks
      (Wheeler kbad) on some rung -- measured signature of a
      non-state measure (v718 Levinson breakdown).
  CE  Epstein x^2 + 5y^2 (cap M = 640, rungs 400..640 step 8):
      same fire rule.
  CB  GOE BULK (seed 11): the SAME imported boundary frames Q^_X,
      bulk replaced by A_goe = 2 I - (A + A^T)[:K,:K]/sqrt(2K)
      (principal-truncation family); evaluated at z = -1e-1 (clear
      of the GOE edge fluctuation scale K^{-2/3}).  FIRE iff
      rho_b^goe = med5(GATE_BLOCK) of ||S_goe - F~(-1e-1)||_F /
      ||F~(-1e-1)||_F > B_MATCH -- a generic bulk must NOT deliver
      the qf block.  DECLARED DEVIATION from the task wording
      ("no cell response at the entry rungs"): the (c)-response
      travels with the boundary path Q^_X, which CB shares by
      design, so gating CB on absent response would let a
      boundary-driven response invalidate the run spuriously; the
      GOE cell-response contrast IS computed and REPORTED, and its
      reading (bulk-mediated vs boundary-driven response) is typed
      into the verdict either way.
  CW  WRONG BOUNDARY (seed 20260805): 6 fixed random orthonormal
      cell vectors (R^888, zero-padded), same import pipeline, on
      the d = 6 run 888..988 plus the 992 transition evaluation;
      FIRE iff [med5 of rho_b^cw over the last 5 rungs of the
      d = 6 run > B_MATCH] AND [the CW contrast at 992 < C_RESP]
      -- a random band must neither deliver the block nor respond
      at the entry.
VERDICT ENUM (frozen; decision order as listed):
  0. any guard fails or a control fails to fire -> printed as
     Z1-TRIPLE-INVALID, exit 1, no structural statement follows.
  1. Z1-TRIPLE-DEAD  = (a) violated beyond 1e-6 OR (b) structural
     fail (med5 rho_b > 10, or import collapse): the sharpened Z1
     form is wrong as constructed; what the failure teaches is
     typed from the anatomy (which frame kills it).
  2. Z1-TRIPLE-CARRIES = (a) and (b) and (c) and (d) all pass: the
     sharpened Z1 object exists at finite level -- the boundary
     triple with Gram-band boundary data delivers the qf block,
     shows the cell structure, and its relative trace object
     tracks Weil; what a proof-grade Z1 still needs is named:
     (i) a continuum boundary triple whose minimal/maximal domains
     reproduce this finite pair with a self-adjointness proof,
     (ii) the z -> 0 Nevanlinna boundary limit of M (the cocycle
     module's open leg), (iii) the relative trace formula at
     theorem level (Krein spectral shift vs the Weil measure,
     currently a measured tracking).
  3. Z1-TRIPLE-PARTIAL = anything else: the passing legs are named
     as the surviving interface, the failing legs as the missing
     structure.
STOP-LIST (binding, inherited): no zeros/prime tables anywhere; no
bare A^{-1} (every resolvent at frozen z with |z| >= 1e-3 or
Im z = h); no PD-margin or 1/eps in any gate; no fits in gates
beyond the declared bounded-statistic slope (hbp.fit_rate, gate d);
the delivery and contrast gates are fit-free; NO RH claim.  This
probe writes no files.  Runtime cap 1800 s.

RESULTS (2026-08-05; single preregistered execution, no reruns,
118.3 s; GUARDS+CONTROLS 23/23 -- the run is VALID; GATES 1/4,
a = PASS, b/c/d = FAIL; b not structural: med5 rho_b = 5.88 <
dead-grade 10; verdict Z1-TRIPLE-PARTIAL):
  *  CONSTRUCTION CLEAN THROUGH EVERY WARD: 1e9 comb (kappa
     0.038821, 34.4M atoms to e^20.3125), all edge-probe anchors
     reproduce EXACTLY on the extended ladder (counts incl. the
     9th entry at 1276; 7/8 gap(1240) = 0.0039; lambda_min(1176)
     = 3.8825e-6; drainage dev 4.9e-5), typed transitions at
     992/1108/1276 with entering eigenvalues 9.944e-5/9.946e-5/
     9.975e-5; resolvent/Schur/dense-H/Gauss-Weil Wards all <=
     2.3e-12.  Notably the transported band SUBSPACE moves
     smoothly (chain sigma_min = 0.9979 over all 103 links,
     including through the 7/8 crossing region): the Gram-side
     boundary path is tame; everything rough below is import-
     side.
  *  (a) HERGLOTZ PASSES EXACTLY: min eig Im H = +0.216 over all
     104 rungs x both complex z (floor -1e-8 never approached);
     Im S anti-Herglotz Ward clean (max eig -1.0e-2 < 0).  The
     pair (A = 2 - J_K, imported Gram band) is a genuine finite
     Weyl/Krein triple on every rung including all three typed
     transitions.
  *  (b) DELIVERY FAILS AT med5 rho_b = 5.88 (bar 0.25, dead 10)
     -- WITH A SPLIT SPECTRUM ANATOMY.  At the top gate rung
     (M = 1272, d = 8): eig S(-1e-2) = 0.0101/0.0102/0.0105/
     0.0106 | 0.0184/0.0214 | 0.0485/0.1611 vs F~ = 0.0100..
     0.0101.  HALF the boundary directions ride the bulk
     threshold at the qf scale (within 1..6% of eps) -- the
     identification dictionary is not empty -- but two directions
     carry 5x..16x eps of bulk energy and dominate the Frobenius
     statistic.  The z-ladder types it as a genuine mismatch, not
     a cell artifact (rho = 1.00 at z = -1e-1, 5.33 at -1e-2,
     41.3 at -1e-3: grows exactly as 1/|z| -- a fixed energy
     excess).  Import anatomy (the cause, measured): cell-mass of
     the transported band in the first K = M/2 cells is 0.500 on
     every gate rung (the near-null packets are DELOCALIZED
     across the full M-cell window), and sigma_min(U) = 2.4e-4..
     1e-3: the [:K] truncation keeps half of each packet, and the
     polar whitening renormalizes near-collapsed mu-norm remnants
     by ~1e3 into O(1) boundary directions that then behave
     quasi-generically.  Candidate-vs-generic separation is still
     real and large: 5.9 (candidate) vs 13.0 (GOE bulk, coarse
     cell) vs 132.5 (random boundary) -- the arithmetic import
     retains structure, but not at the frozen identification bar.
  *  (c) NO CELL RESPONSE -- and NOT at the crossings either: the
     predeclared risk fired in a sharper form.  Entry contrasts
     rho(992/1108/1276) = 1.54/2.02/1.04 (bar 3.0), 49 of 100
     within-run increments comparable; the S-path roughness is
     BROADBAND (median rel increment 0.25 per rung; top-5 at
     M = 996/920/1116/936/1004, not concentrated at entries or
     at the 1096..1100 / 1240 crossing rungs).  Since the Gram
     boundary path itself is smooth (sigma_min 0.998 per link),
     the roughness is import-truncation noise: the whitened
     remnant directions rotate erratically rung-to-rung and mask
     any cell signal in M.
  *  (d) THE DECOUPLED PAIR DOES NOT TRACK WEIL: err_d = 0.24..
     0.78 across the ladder, med5(GATE_BLOCK) = 0.388 (bar 0.05),
     trend flat (b = -0.003/X).  Cutting the imported band out of
     the bulk moves the battery Weil-state evaluation by ~40%:
     the polar-whitened boundary directions carry large GNS state
     weight -- same root cause as (b).  (The bulk trace formula
     itself is exact: Gauss/Weil state identity 2.3e-12.)
  *  CONTROLS ALL FIRE: CS Wheeler breakdown 9/9 rungs (kbad 16
     at 888); CE 31/31 (kbad 27 at 400); CB GOE bulk med5
     rho_b^goe = 12.97 >> 0.25 (generic bulk does not deliver);
     CW random boundary med5 rho_b^cw = 132.5 AND 992-contrast
     1.19 < 3 (random band neither delivers nor responds).
  *  CONSEQUENCE FOR THE Z1 PROGRAMME (stated plainly): the
     sharpened Z1 object survives as a FRAME and dies as an
     IMPORT.  What stands: the finite boundary triple exists and
     is exactly Herglotz; half its boundary spectrum already sits
     on the qf block at the right scale; bulk Gauss/Weil trace
     identity exact; all of it arithmetic-specific under
     controls.  What the failure teaches, typed: the Gram
     near-kernel packets live on the FULL M-cell window
     (cell-mass exactly 1/2 in the half-window, every rung), so
     any K = M/2 GNS import truncates them and the polar
     whitening turns the truncation loss into quasi-generic
     boundary noise that kills delivery (b), masks the cell
     structure (c), and overweights the boundary in the state
     (d).  The next Z1 module must couple the frames WITHOUT
     whitening: either (1) the mu-weighted triple -- use the raw
     import U = L^T B[:K] (no polar) and compare against the
     P-conjugated Gram block, i.e. renormalize the reference by
     the MEASURED import distortion (source-native, declarable);
     or (2) pose the triple on the full M-cell frame directly
     (Toeplitz bulk + Gram band, where the Gram route already
     owns the Feshbach block) and demand instead an INTERTWINING
     with J_K's spectral data -- the delivery gate becomes a
     commutation statement rather than an entrywise match.  A
     full-depth GNS frame (K = M) is stated to be OUT OF REACH by
     deepening (needs lags to 2M, X = 27.75 at the first entry,
     e^27.75 atoms).  NOT claimed: anything beyond X = 20.3125,
     eps-uniformity, continuum self-adjointness, spectral
     reality, RH.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/z1_boundary_triple_probe.py
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
import qf_spectral_bundle_probe as qsb  # noqa: E402  (sign_fix)

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID                        # 1/64, dyadic float-exact
ATOM_MAX_DEEP = 1000000000           # deep comb cap (1e9, declared)
M_CAP_DEEP = int(math.floor(math.log(ATOM_MAX_DEEP) / D))   # 1326
M_TOP = 1300                         # deepest rung (X = 20.3125)
M_PAR = 824                          # parent cap (prefix Ward)

LAD = list(range(888, 1301, 4))      # 104 rungs, X = 13.875..20.3125
E_TEST = (992, 1108, 1276)           # frozen entry/transition rungs
GATE_BLOCK = list(range(1256, 1273, 4))       # last 5 of the d=8 run
TOP5W = list(range(1160, 1177, 4))   # drainage-anchor rungs
HALF2 = LAD[len(LAD) // 2:]          # second-half trend block
M_WARD = 888                         # GNS frame Ward rung
WARD_H_RUNGS = (888, 1272)           # dense-H Ward rungs
WARD_D_RUNGS = (888, 1108, 1300)     # Gauss/Weil + recon Ward rungs

THR_NULL = 1.0e-4                    # band rule threshold (cocycle)
H_IM = 1.0e-2
ZSET = (-1.0e-1, -1.0e-2, -1.0e-3,
        complex(0.0, H_IM), complex(-1.0e-3, H_IM))
Z_REF = -1.0e-2                      # delivery reference cell
ZC = ZSET[3:]                        # Herglotz points
Z_CB = -1.0e-1                       # GOE-bulk control cell

HERG_FLOOR = 1.0e-8                  # gate (a)
HERG_DEAD = 1.0e-6                   # DEAD-grade violation
B_MATCH = 0.25                       # gate (b) med5 bar
B_DEAD = 10.0                        # gate (b) structural-fail bar
C_RESP = 3.0                         # gate (c) contrast bar
C_UNIQ = 1                           # gate (c) uniqueness allowance
D_LEVEL = 0.05                       # gate (d) med5 level bar
D_SLOPE_MIN = -0.01                  # gate (d) trend floor (b >= )
N_MED = 5

NPAD = 128                           # battery support in cells
R_BAT = (1.0, 2.0)
QF_FLOOR = 1.0e-12

IMPORT_FLOOR = 1.0e-8                # import collapse floor
SVD_FLOOR = 1.0e-8                   # K4 transport kill floor
WARD_ORTH = 1.0e-10                  # R orthogonality
COUP_WARD = 1.0e-8                   # coupling |E_c| Ward
WARD_FRAME = 1.0e-3                  # GNS frame Ward
WARD_SOLVE = 1.0e-9                  # banded-solve residual
WARD_SH = 1.0e-8                     # S H = I Ward
WARD_HDENSE = 1.0e-9                 # dense-H Ward
WARD_GAUSSW = 1.0e-8                 # Gauss/Weil state identity
BAR_GAUSS = 1.0e-8                   # moment reconstruction
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
CW_LAD = list(range(888, 989, 4))    # d = 6 run for CW

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
    hsh.update(("z1-boundary-triple spec: bulk A = 2I - J_{K=M/2} "
                "(v718 machinery, dyadic D=%.10f), deep cap %d "
                "(512-GB machine declared), M_TOP=%d, LAD=%s; band "
                "rule d(M)=#{lam<=%g} cocycle verbatim, transitions "
                "R'=[JR|N]; import U=L^T B[:K], polar, floor %g; "
                "M-function H=Q^T(A-z)^-1 Q, S=H^-1, ZSET=%s, "
                "Z_REF=%g; gates: (a) Herglotz >= -%g (dead %g); "
                "(b) rho_b med5 over %s <= %g (dead > %g); (c) "
                "rel-increment contrast rho(e) >= %g on E_TEST=%s, "
                "uniqueness <= %d, cocycle normalizer verbatim; "
                "(d) err_d med5 <= %g AND fit_rate b >= %g over "
                "HALF2, battery autocorr g_f, Gauss/Weil ward %g; "
                "wards: solve %g, SH %g, denseH %g at %s, frame %g "
                "at %d, coup %g, orth %g, svd %g, recon %g at %s; "
                "anchors: counts %s, gaps %s tol %g, lmin1176 %g "
                "tol %g, drain %s tol %g; guards comb %g prefix %g "
                "pd %g runtime %g; controls: CS seed %d rungs %s, "
                "CE cap %d M %d rungs %s, CB GOE seed %d z=%g fire "
                "rho_b>%g (declared deviation: response reported "
                "not gated), CW seed %d rungs %s fire rho_b>%g AND "
                "contrast<%g; verdict: invalid -> DEAD(a>%g or "
                "b>%g or import collapse) -> CARRIES(abcd) -> "
                "PARTIAL"
                % (D, ATOM_MAX_DEEP, M_TOP, LAD, THR_NULL,
                   IMPORT_FLOOR, ZSET, Z_REF, HERG_FLOOR, HERG_DEAD,
                   GATE_BLOCK, B_MATCH, B_DEAD, C_RESP, E_TEST,
                   C_UNIQ, D_LEVEL, D_SLOPE_MIN, WARD_GAUSSW,
                   WARD_SOLVE, WARD_SH, WARD_HDENSE, WARD_H_RUNGS,
                   WARD_FRAME, M_WARD, COUP_WARD, WARD_ORTH,
                   SVD_FLOOR, BAR_GAUSS, WARD_D_RUNGS,
                   sorted(REPRO_COUNTS.items()),
                   sorted(REPRO_GAPS.items()), REPRO_TOLG,
                   REPRO_LMIN1176, REPRO_LTOL,
                   sorted(DRAIN_LEVELS.items()), REPRO_QTOL,
                   COMB_DEV_BAR, PREFIX_WARD, PD_TOL, RUNTIME_CAP,
                   SEED_CS, CTRL_LAD_CS, EP_NCAP, EP_MMAX,
                   CTRL_LAD_CE, SEED_CB, Z_CB, B_MATCH, SEED_CW,
                   CW_LAD, B_MATCH, C_RESP, HERG_DEAD, B_DEAD)
                ).encode())
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
    check("G1.1 deep-table overlap: 1e9 von Mangoldt table == "
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
          "[%.0f, %d] <= %.6f"
          % (kappa, core.KAPPA_X0, ATOM_MAX_DEEP,
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
    check("G1.4 prefix Ward: deep tower leading %d block == parent "
          "tower, max abs dev %.1e <= %.0e"
          % (M_PAR, dev, PREFIX_WARD), dev <= PREFIX_WARD)
    print("  deep census: ka = %d atoms to e^%.4f" % (ka, 2 * alpha))
    return p, T, c_cont, alpha, ka


# ------------------------------------------------ candidate frame
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
    check("G1.7 GNS frame Ward at M = %d (K = %d): dev %.1e <= "
          "%.0e" % (M_WARD, K, dev, WARD_FRAME), dev <= WARD_FRAME)


def tri_solve(bJ, aJ, z, Bmat):
    """(A - z) Y = Bmat with A = 2 - J tridiagonal, via banded LU."""
    K = len(bJ)
    cplx = isinstance(z, complex)
    dt = complex if cplx else float
    ab = np.zeros((3, K), dtype=dt)
    ab[0, 1:] = -aJ
    ab[1, :] = (2.0 - z) - bJ
    ab[2, :-1] = -aJ
    return sla.solve_banded((1, 1), ab, Bmat.astype(dt))


def cheb_eval(a_all, x):
    """g_f(x) = a_0 + 2 sum_d a_d T_d(x/2) for all battery rows."""
    y = x / 2.0
    t_prev = np.ones_like(x)
    t_cur = y.copy()
    acc = np.outer(a_all[:, 0], t_prev)
    for dd in range(1, a_all.shape[1]):
        acc += 2.0 * np.outer(a_all[:, dd], t_cur)
        t_prev, t_cur = t_cur, x * t_cur - t_prev
    return acc


# ------------------------------------------------ per-rung machinery
def gram_rung(T, M, want_q6=False, Fb=None):
    lam, V = np.linalg.eigh(T[:M, :M])
    d = int(np.sum(lam <= THR_NULL))
    Vd = qsb.sign_fix(V[:, :d])
    Ec = V[:, d:].T @ (T[:M, :M] @ Vd)
    out = dict(M=M, lam=lam[:16].copy(), lam_min=float(lam[0]),
               d=d, Vd=Vd, coup=float(np.max(np.abs(Ec))),
               lam_rest=lam[d:], Ec=Ec)
    if want_q6 and Fb is not None:
        out["q6"] = np.sum((V[:NPAD, :6].T @ Fb) ** 2, axis=0)
    return out


def f_tilde(gr, R, z):
    """Transported Gram effective block (Feshbach machinery
    verbatim): R^T [Lambda_d - z - C_d(z)] R."""
    d = gr["d"]
    lam_d = gr["lam"][:d]
    C = gr["Ec"].T @ (gr["Ec"] / (gr["lam_rest"][:, None] - z))
    core_blk = np.diag(lam_d).astype(complex) \
        - z * np.eye(d) - C
    out = R.T @ core_blk @ R
    return out.real if not isinstance(z, complex) else out


def transport_update(prev, gr, R_prev):
    """Cocycle transition convention verbatim."""
    Ma, Mb = prev["M"], gr["M"]
    da, db = prev["d"], gr["d"]
    S_ov = gr["Vd"][:Ma, :].T @ prev["Vd"]        # (db x da)
    Uu, s, Vt = np.linalg.svd(S_ov, full_matrices=False)
    smin = float(s[-1])
    if db == da:
        R = (Uu @ Vt) @ R_prev
        kind = "link"
    elif db > da:
        Jiso = Uu @ Vt                             # (db x da) isometry
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


# ------------------------------------------------ run
def run():
    print("=" * 78)
    print("SHARPENED-Z1 module 2 -- boundary triple: J_K bulk + "
          "Gram near-kernel boundary (1e9 comb, X <= %.4f)"
          % (M_TOP * D))
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall", not hits, str(hits))
    bats, spec_sha = freeze_spec()
    check("G0.2 battery + ladders + bars + anchors SHA-256-frozen "
          "BEFORE any comb data is built", True,
          "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP = %d <= %d; sieve cover %d <= "
          "%d; runtime cap %.0f s"
          % (M_TOP, M_CAP_DEEP, int(math.exp(M_TOP * D)) + 2,
             ATOM_MAX_DEEP, RUNTIME_CAP),
          M_TOP <= M_CAP_DEEP
          and int(math.exp(M_TOP * D)) + 2 <= ATOM_MAX_DEEP)

    # ---- combs + towers strictly after the freeze
    u_deep, mu_deep = build_deep_comb()
    T_par = build_parent_tower()
    p, T, c_cont, alpha_top, ka = build_deep_tower(u_deep, mu_deep,
                                                   T_par)
    Fb, names = battery_matrix(bats)
    a_all = np.stack([np.correlate(Fb[:, j], Fb[:, j], "full")
                      [NPAD - 1:] for j in range(Fb.shape[1])])
    w_f = a_all[:, 0] * p[0] + 2.0 * (a_all[:, 1:] @ p[1:NPAD])

    # ---- CW boundary (frozen random band)
    rng_cw = np.random.default_rng(SEED_CW)
    B_cw0 = np.linalg.qr(rng_cw.standard_normal((888, 6)))[0]

    # ---- CB bulk (frozen GOE draw at top K)
    rng_cb = np.random.default_rng(SEED_CB)
    A_cb = rng_cb.standard_normal((M_TOP // 2, M_TOP // 2))
    A_cb = A_cb + A_cb.T

    # ---- main ladder (single pass)
    lam884 = np.linalg.eigvalsh(T[:884, :884])
    counts = {884: int(np.sum(lam884 <= THR_NULL))}
    gaps = {}
    q6_med = []
    rungs = []
    prev_gr, R = None, None
    trans_events = []
    smin_min, orth_max, coup_max, pd_min = np.inf, 0.0, 0.0, np.inf
    herg_min, antih_max = np.inf, -np.inf
    ward_solve = ward_sh = 0.0
    ward_hd = ward_gw = ward_rec = 0.0
    import_smin_min = np.inf
    kbads = []

    for M in LAD:
        K = M // 2
        gr = gram_rung(T, M, want_q6=(M in TOP5W), Fb=Fb)
        counts[M] = gr["d"]
        pd_min = min(pd_min, gr["lam_min"])
        coup_max = max(coup_max, gr["coup"])
        if M in (1096, 1176, 1240):
            lam = gr["lam"]
            gaps[("67", M)] = float((lam[6] - lam[5]) / lam[6])
            gaps[("78", M)] = float((lam[7] - lam[6]) / lam[7])
        if M == 1176:
            lmin1176 = gr["lam_min"]
        if M in TOP5W:
            q6_med.append(gr["q6"])

        # transport
        if prev_gr is None:
            R = np.eye(gr["d"])
            kind = "start"
        else:
            R, smin, orth, kind = transport_update(prev_gr, gr, R)
            smin_min = min(smin_min, smin)
            orth_max = max(orth_max, orth)
            if kind == "entry":
                trans_events.append(
                    (M, prev_gr["d"], gr["d"],
                     float(gr["lam"][gr["d"] - 1])))
        prev_gr = gr

        # bulk
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
        if M in WARD_D_RUNGS:
            rec = jac.gauss_reconstruct(aM, gM, p[0],
                                        min(2 * K, M))
            ward_rec = max(ward_rec, float(
                np.max(np.abs(rec - p[:len(rec)]))
                / np.max(np.abs(p[:len(rec)]))))

        # import
        B = gr["Vd"] @ R
        U = L.T @ B[:K]
        Uu, s_imp, Vt = np.linalg.svd(U, full_matrices=False)
        Qh = Uu @ Vt
        import_smin_min = min(import_smin_min, float(s_imp[-1]))
        cellmass = float(np.sum(B[:K] ** 2) / np.sum(B ** 2))

        # M-function on ZSET
        Hs, Ss, Fts, rhos = {}, {}, {}, {}
        for z in ZSET:
            Y = tri_solve(bJ, aJ, z, Qh)
            res = float(np.max(np.abs(
                ((2.0 - z) * Y - (np.diag(bJ) @ Y
                                  + np.concatenate(
                                      [aJ[:, None] * Y[1:],
                                       np.zeros((1, Y.shape[1]),
                                                Y.dtype)])
                                  + np.concatenate(
                                      [np.zeros((1, Y.shape[1]),
                                                Y.dtype),
                                       aJ[:, None] * Y[:-1]])))
                 - Qh)))
            ward_solve = max(ward_solve, res)
            H = Qh.T @ Y
            H = 0.5 * (H + (H.T if not isinstance(z, complex)
                            else H.T))
            S = np.linalg.inv(H)
            ward_sh = max(ward_sh, float(np.max(np.abs(
                S @ H - np.eye(gr["d"])))))
            Ft = f_tilde(gr, R, z)
            Hs[z], Ss[z], Fts[z] = H, S, Ft
            rhos[z] = float(np.linalg.norm(S - Ft)
                            / max(np.linalg.norm(Ft), QF_FLOOR))
        for z in ZC:
            ImH = (Hs[z] - Hs[z].conj().T) / 2.0j
            herg_min = min(herg_min, float(np.min(
                np.linalg.eigvalsh(ImH))))
            ImS = (Ss[z] - Ss[z].conj().T) / 2.0j
            antih_max = max(antih_max, float(np.max(
                np.linalg.eigvalsh(ImS))))
        if M in WARD_H_RUNGS:
            xj, Uj = sla.eigh_tridiagonal(bJ, aJ)
            z0 = ZC[0]
            QU = Uj.T @ Qh
            H2 = QU.T @ (QU / (2.0 - z0 - xj)[:, None])
            ward_hd = max(ward_hd, float(np.max(np.abs(
                H2 - Hs[z0])) / np.max(np.abs(H2))))

        # trace leg
        Jf = np.diag(bJ) + np.diag(aJ, 1) + np.diag(aJ, -1)
        Pq = Qh @ Qh.T
        Pc = np.eye(K) - Pq
        JD = Pq @ Jf @ Pq + Pc @ Jf @ Pc
        xD, UD = np.linalg.eigh(0.5 * (JD + JD.T))
        wD = p[0] * UD[0, :] ** 2
        om_D = cheb_eval(a_all, xD) @ wD
        errd = float(np.sum(np.abs(om_D - w_f))
                     / np.sum(np.abs(w_f)))
        if M in WARD_D_RUNGS:
            xg, Ug = sla.eigh_tridiagonal(bJ, aJ)
            wg = p[0] * Ug[0, :] ** 2
            om = cheb_eval(a_all, xg) @ wg
            ward_gw = max(ward_gw, float(np.max(
                np.abs(om - w_f) / np.abs(w_f))))

        # CB (GOE bulk, same boundary)
        Hk = A_cb[:K, :K] / math.sqrt(2.0 * K)
        Ycb = np.linalg.solve((2.0 - Z_CB) * np.eye(K) - Hk, Qh)
        Scb = np.linalg.inv(Qh.T @ Ycb)
        rho_cb = float(np.linalg.norm(Scb - Fts[Z_CB])
                       / np.linalg.norm(Fts[Z_CB]))

        # CW (random boundary, true bulk) on the d = 6 run + 992
        S_cw = rho_cw = None
        if M in CW_LAD or M == 992:
            Bcw = np.zeros((M, 6))
            Bcw[:888, :] = B_cw0
            Ucw = L.T @ Bcw[:K]
            Uu2, s2, Vt2 = np.linalg.svd(Ucw, full_matrices=False)
            Qcw = Uu2 @ Vt2
            Ycw = tri_solve(bJ, aJ, Z_REF, Qcw)
            S_cw = np.linalg.inv(Qcw.T @ Ycw)
            Ft6 = Fts[Z_REF][:6, :6] if gr["d"] > 6 \
                else Fts[Z_REF]
            rho_cw = float(np.linalg.norm(S_cw - Ft6)
                           / np.linalg.norm(Ft6))

        rungs.append(dict(M=M, K=K, d=gr["d"], kind=kind,
                          S_ref=Ss[Z_REF].real.copy(),
                          rho=dict(rhos), errd=errd,
                          rho_cb=rho_cb, S_cw=S_cw, rho_cw=rho_cw,
                          s_imp=s_imp.copy(), cellmass=cellmass,
                          eigS=np.sort(np.linalg.eigvalsh(
                              0.5 * (Ss[Z_REF].real
                                     + Ss[Z_REF].real.T))),
                          eigF=np.sort(np.linalg.eigvalsh(
                              0.5 * (Fts[Z_REF].real
                                     + Fts[Z_REF].real.T)))))

    # ---- construction guards
    check("G1.6 Wheeler + Cholesky valid on every rung (%d) AND "
          "Gauss reconstruction %.1e <= %.0e"
          % (len(LAD), ward_rec, BAR_GAUSS),
          not kbads and ward_rec <= BAR_GAUSS, str(kbads[:3]))
    if kbads:
        print("\nVERDICT: Z1-TRIPLE-INVALID (construction broke)")
        return 1
    check("G1.8 measured Gram PD: lambda_min = %.3e > -%.0e"
          % (pd_min, PD_TOL), pd_min > -PD_TOL)
    check("G1.9 coupling Ward max |E_c| = %.1e <= %.0e; transport "
          "sigma_min = %.6f >= %.0e; orthogonality %.1e <= %.0e"
          % (coup_max, COUP_WARD, smin_min, SVD_FLOOR, orth_max,
             WARD_ORTH),
          coup_max <= COUP_WARD and smin_min >= SVD_FLOOR
          and orth_max <= WARD_ORTH)
    check("G1.10 resolvent/Schur Wards: banded residual %.1e <= "
          "%.0e; S H - I %.1e <= %.0e; dense-H %.1e <= %.0e"
          % (ward_solve, WARD_SOLVE, ward_sh, WARD_SH, ward_hd,
             WARD_HDENSE),
          ward_solve <= WARD_SOLVE and ward_sh <= WARD_SH
          and ward_hd <= WARD_HDENSE)
    check("G1.11 Gauss/Weil state identity: max rel dev %.1e <= "
          "%.0e at rungs %s" % (ward_gw, WARD_GAUSSW,
                                WARD_D_RUNGS),
          ward_gw <= WARD_GAUSSW)
    check("G1.12 import health: min sigma_min(U) = %.3e >= %.0e "
          "(no import collapse)" % (import_smin_min, IMPORT_FLOOR),
          import_smin_min >= IMPORT_FLOOR)

    # ---- anchors
    ok_cnt = all(counts.get(M) == want
                 for M, want in REPRO_COUNTS.items())
    check("G1.5a source entry anchors: counts %s == frozen"
          % {M: counts.get(M) for M in sorted(REPRO_COUNTS)},
          ok_cnt)
    ok_gap = all(abs(gaps[k] - v) <= REPRO_TOLG
                 for k, v in REPRO_GAPS.items() if k in gaps)
    check("G1.5b gap anchors: %s vs frozen %s (tol %.0e); "
          "lambda_min(1176) = %.4e (tol %.0e)"
          % ({k: round(gaps[k], 4) for k in sorted(gaps)},
             sorted(REPRO_GAPS.items()), REPRO_TOLG, lmin1176,
             REPRO_LTOL),
          ok_gap and abs(lmin1176 - REPRO_LMIN1176) <= REPRO_LTOL)
    med_q6 = np.median(np.stack(q6_med), axis=0)
    dev_q = max(abs(float(med_q6[j]) - DRAIN_LEVELS[nm])
                for j, nm in enumerate(names) if nm in DRAIN_LEVELS)
    check("G1.5c drainage-level anchors: worst dev %.1e <= %.0e"
          % (dev_q, REPRO_QTOL), dev_q <= REPRO_QTOL)
    trans_rungs = tuple(t[0] for t in trans_events)
    check("G1.5d measured transition set %s == frozen E_TEST %s "
          "(entering eigenvalues %s)"
          % (trans_rungs, E_TEST,
             ["%.4e" % t[3] for t in trans_events]),
          trans_rungs == E_TEST)

    # ---- gate (a) Herglotz
    a_ok = gate("(a) HERGLOTZ: min eig Im H = %+.3e >= -%.0e over "
                "all rungs x both complex z (anti-Herglotz Ward "
                "max eig Im S = %+.3e)"
                % (herg_min, HERG_FLOOR, antih_max),
                herg_min >= -HERG_FLOOR)
    a_dead = herg_min < -HERG_DEAD

    # ---- gate (b) delivery
    print("\n-- (b) qf-block delivery: rho_b(X) = ||S - F~||_F / "
          "||F~||_F at Z_REF = %g (both in transported reference "
          "coordinates)" % Z_REF)
    rmap = {r["M"]: r for r in rungs}
    print("  rho_b profile (every 8th rung): %s"
          % "  ".join("M=%d:%.3f" % (r["M"], r["rho"][Z_REF])
                      for r in rungs[::8]))
    zt = rungs[-1]
    print("  z-profile at top rung M = %d (d = %d): %s"
          % (zt["M"], zt["d"],
             "  ".join("z=%s:%.4f" % (z, zt["rho"][z])
                       for z in ZSET)))
    gb = rmap[GATE_BLOCK[-1]]
    print("  eig S(Z_REF) top gate rung M = %d: %s"
          % (gb["M"], "/".join("%.4f" % v for v in gb["eigS"])))
    print("  eig F~(Z_REF) same rung:          %s"
          % "/".join("%.4f" % v for v in gb["eigF"]))
    print("  import health on GATE_BLOCK: sigma_min(U) %s; "
          "cell-mass %s"
          % ("/".join("%.3f" % rmap[M]["s_imp"][-1]
                      for M in GATE_BLOCK),
             "/".join("%.3f" % rmap[M]["cellmass"]
                      for M in GATE_BLOCK)))
    b_med = float(np.median([rmap[M]["rho"][Z_REF]
                             for M in GATE_BLOCK]))
    tail9 = [r for r in rungs if r["d"] == 9]
    if tail9:
        print("  d = 9 frontier tail (reported, unadjudicated): "
              "rho_b = %s"
              % "/".join("%.3f" % r["rho"][Z_REF] for r in tail9))
    b_ok = gate("(b) QF-BLOCK DELIVERY: med%d over %s of rho_b = "
                "%.4f <= %g (structural-fail bar %g)"
                % (N_MED, GATE_BLOCK, b_med, B_MATCH, B_DEAD),
                b_med <= B_MATCH)
    b_dead = (b_med > B_DEAD) or (import_smin_min < IMPORT_FLOOR)

    # ---- gate (c) cell response
    print("\n-- (c) cell structure: relative S(Z_REF) increments "
          "(cocycle normalizer), contrast at E_TEST = %s"
          % (E_TEST,))
    rels_in, rels_e = [], {}
    for ra, rb in zip(rungs, rungs[1:]):
        Sa, Sb = ra["S_ref"], rb["S_ref"]
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
    rhos_e = {e: rels_e[e] / med_in for e in rels_e}
    top5 = sorted(rels_in, key=lambda t: -t[1])[:5]
    print("  within-run increments: median rel = %.4e over %d; "
          "top-5: %s"
          % (med_in, len(rels_in),
             "  ".join("M=%d:%.3e" % t for t in top5)))
    print("  entry increments: %s"
          % "  ".join("M=%d: rel %.3e (rho %.2f)"
                      % (e, rels_e[e], rhos_e[e])
                      for e in sorted(rels_e)))
    min_rho = min(rhos_e.values()) if rhos_e else 0.0
    min_rel_e = min(rels_e.values()) if rels_e else np.inf
    n_over = sum(1 for _m, v in rels_in if v >= min_rel_e)
    c_ok = gate("(c) CELL RESPONSE: min entry contrast rho = %.2f "
                ">= %g AND non-transition increments reaching it "
                "= %d <= %d"
                % (min_rho, C_RESP, n_over, C_UNIQ),
                min_rho >= C_RESP and n_over <= C_UNIQ)

    # ---- gate (d) trace precursor
    print("\n-- (d) trace-formula precursor: decoupled pair vs "
          "deployed Weil evaluation (battery-summed)")
    errs = [(r["M"] * D, r["errd"]) for r in rungs]
    print("  err_d profile (every 8th rung): %s"
          % "  ".join("M=%d:%.2e" % (r["M"], r["errd"])
                      for r in rungs[::8]))
    d_med = float(np.median([rmap[M]["errd"] for M in GATE_BLOCK]))
    rows = [dict(XmR=x, mx=v) for x, v in errs
            if int(round(x / D)) in [r["M"] for r in rungs]
            and x >= HALF2[0] * D]
    b_tr, _res = hbp.fit_rate(rows)
    d_ok = gate("(d) TRACE PRECURSOR: med%d(GATE_BLOCK) err_d = "
                "%.3e <= %g AND second-half trend b = %+.3f/X >= "
                "%g (b > 0 = falling)"
                % (N_MED, d_med, D_LEVEL, b_tr, D_SLOPE_MIN),
                d_med <= D_LEVEL and b_tr >= D_SLOPE_MIN)

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
    check("CS scramble control fires: Wheeler breakdown on %d/%d "
          "rungs (first kbad %s)" % (len(kb_cs), len(CTRL_LAD_CS),
                                     kb_cs[0] if kb_cs else "--"),
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
    check("CE Epstein control fires: Wheeler breakdown on %d/%d "
          "rungs (first kbad %s)" % (len(kb_ce), len(CTRL_LAD_CE),
                                     kb_ce[0] if kb_ce else "--"),
          len(kb_ce) == len(CTRL_LAD_CE))

    cb_med = float(np.median([rmap[M]["rho_cb"]
                              for M in GATE_BLOCK]))
    check("CB GOE-bulk control fires: med%d rho_b^goe = %.2f > %g "
          "at z = %g (generic bulk does not deliver)"
          % (N_MED, cb_med, B_MATCH, Z_CB), cb_med > B_MATCH)

    cw_rungs = [r for r in rungs if r["M"] in CW_LAD
                and r["rho_cw"] is not None]
    cw_last5 = [r["rho_cw"] for r in cw_rungs[-5:]]
    cw_med = float(np.median(cw_last5))
    cw_pairs = [(ra, rb) for ra, rb in zip(cw_rungs, cw_rungs[1:])]
    cw_rels = []
    for ra, rb in cw_pairs:
        dlt = float(np.max(np.abs(rb["S_cw"] - ra["S_cw"])))
        nrm = max(np.max(np.abs(ra["S_cw"])),
                  np.max(np.abs(rb["S_cw"])))
        cw_rels.append(dlt / max(nrm, QF_FLOOR))
    r992 = rmap.get(992)
    r988 = rmap.get(988)
    dlt992 = float(np.max(np.abs(r992["S_cw"] - r988["S_cw"])))
    nrm992 = max(np.max(np.abs(r992["S_cw"])),
                 np.max(np.abs(r988["S_cw"])))
    cw_contrast = (dlt992 / max(nrm992, QF_FLOOR)) \
        / max(float(np.median(cw_rels)), QF_FLOOR)
    check("CW wrong-boundary control fires: med%d rho_b^cw = %.2f "
          "> %g AND contrast at 992 = %.2f < %g"
          % (N_MED, cw_med, B_MATCH, cw_contrast, C_RESP),
          cw_med > B_MATCH and cw_contrast < C_RESP)

    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= predeclared cap %.0f s"
          % (dt, RUNTIME_CAP), dt <= RUNTIME_CAP)

    # ---- verdict
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE", "CB", "CW")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE", "CB", "CW")))
    sigs = dict(a=a_ok, b=b_ok, c=c_ok, d=d_ok)
    if not (guards_ok and controls_ok):
        verdict = "Z1-TRIPLE-INVALID"
    elif a_dead or b_dead:
        verdict = "Z1-TRIPLE-DEAD"
    elif all(sigs.values()):
        verdict = "Z1-TRIPLE-CARRIES"
    else:
        verdict = "Z1-TRIPLE-PARTIAL"

    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/4 (a=%s b=%s c=%s d=%s), GUARDS+CONTROLS "
          "%d/%d, runtime %.1f s"
          % (sum(sigs.values()),
             *["P" if sigs[k] else "F" for k in "abcd"],
             n_chk, len(CHECKS), time.time() - T_START))
    if verdict == "Z1-TRIPLE-CARRIES":
        print("CONSEQUENCE (stated plainly): the sharpened Z1 "
              "object exists at finite level -- Herglotz triple, "
              "qf-block delivery, cell structure, Weil tracking.  "
              "A proof-grade Z1 still needs the continuum triple "
              "with self-adjointness, the z -> 0 Nevanlinna "
              "boundary limit, and the relative trace formula at "
              "theorem level.  NO RH claim.")
    elif verdict == "Z1-TRIPLE-DEAD":
        print("CONSEQUENCE (stated plainly): the sharpened Z1 form "
              "is wrong as constructed (Herglotz or delivery "
              "fails structurally); the failure anatomy above "
              "types what must change.  NO RH claim.")
    else:
        print("CONSEQUENCE (stated plainly): the triple carries "
              "the legs %s and misses %s; the failing legs name "
              "the structure the next module must add.  NO RH "
              "claim."
              % ([k for k in "abcd" if sigs[k]],
                 [k for k in "abcd" if not sigs[k]]))
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
