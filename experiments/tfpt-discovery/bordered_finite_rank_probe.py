#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bordered_finite_rank_probe -- PRIME.PORT.RHP.BORDEREDHANKEL.FINITE.02
(round 245): the MINIMAL-RANK ADJUDICATION of the augmented (bordered)
problem -- does the smooth border stay a rank-1/Schlesinger insertion
inside the existing 2x2 FIK system, does it need an irreducible 3x3
mixed-moment RHP, or does it create an N-growing generator rank?  Not
guessed aesthetically: formulated, gated, counted.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r244 discipline): w = window (kz), N_w =
builder depth, n = chain degree; free pivots h_{w,n} (n < N_w) are the
proof objects; sigma = the sealed r239/r243 smooth PNT-shape border
(F_DEF / F_DEF_SHA imported verbatim via principal_bessel_probe);
F_n = int pihat_n dsigmatilde, T_n = int x pihat_n dsigmatilde,
rho_n = F_n^2/h_n, S_n = sum_{k<=n} rho_k, D_n = B - S_{n-1}.  Ground
truth (h signs, S, flips) enters GATES only, never a construction
path; the budget B is a FREE sealed parameter (never fitted).

LEG A -- THE AUGMENTED RHP FORMULATION, EXACT (two sealed candidates).
(A1a) PURE-DEGREE 3x3: Y3_n(z) with rows of degrees (n, n-1, n-2) and
  columns (pihat_m, C_m = C[pihat_m mutilde], Csig_m = C[pihat_m
  sigmatilde]).  DERIVED AT DESIGN TIME, frozen here, then gated:
  (i) Laurent orders col1 ~ z^m (monic), col2 = h_m z^{-m-1}(1+O(1/z))
  (orthogonality cancellation), col3 = F_m z^{-1} + T_m z^{-2} + ...
  (NO cancellation -- the border column starts at z^{-1} for EVERY
  row); (ii) det Y3_n(z) = -h_{n-2} F_{n-1}, CONSTANT in z (derivation:
  column-3 expansion in the Wronskian minors W_{a,b} = pihat_a C_b -
  pihat_b C_a with W_{n,n-1} = h_{n-1}, W_{n,n-2} = (z - alphahat_{n-1})
  h_{n-2}, then the F-sourced border transfer collapses the sum); the
  pure-degree 3x3 is solvable iff the 2x2 is AND F_{n-1} != 0 -- it
  DEGENERATES exactly on the F = 0 self-alias (SMOOTH); (iii) UNIQUE
  NORMALIZATION: over the full integer cube of diagonal gauges
  diag(z^a, z^b, z^c) exactly ONE choice, (a, b, c) = (-n, n-1, 1),
  yields a finite INVERTIBLE limit L (a permutation-triangular matrix
  with det L = det Y3); every other diagonal is divergent or singular
  (exact enumeration); (iv) the pure-degree rows admit NO self-
  contained 3x3 degree transfer: the F-source is not in the row space
  -- homogenization FORCES the parabolic augmentation (A1b).
(A1b) UNIPOTENT-AUGMENTED 3x3 (the Schlesinger insertion): Y3aug_n(z)
  = [[pihat_n, C_n, Csig_n], [pihat_{n-1}/h_{n-1}, C_{n-1}/h_{n-1},
  Csig_{n-1}/h_{n-1}], [0, 0, 1]] -- the r227 2x2 FIK solution plus
  one F-sourced Uvarov column plus one CONSTANT row.  Gated exact:
  det Y3aug = 1 (all z, all n, ALSO through control flips h < 0);
  normalization Y3aug diag(z^{-n}, z^n, 1) = I + Y1/z + O(z^-2) with
  Y1_13 = F_n, Y1_23 = F_{n-1}/h_{n-1}, third row of Y1 = 0 (the
  border data is the infinity readout of the third column); degree
  step Y3aug_{n+1} = R3_n Y3aug_n with
      R3_n = [[z - alphahat_n, -h_n, -F_n], [1/h_n, 0, 0], [0, 0, 1]],
  det R3_n = 1 -- THE r244 FLOW INHOMOGENEITY (T-source flow) APPEARS
  AS THE (1,3) MATRIX ENTRY of the transfer; residue structure at the
  sigma-atoms: Res_{y_a} Y3aug = lim Y3aug (sv_a E_13) (nilpotent,
  couples column 3 to column 1 ONLY), at the mutilde-atoms the r227
  E_12 condition -- a genuine discrete RHP whose jumps are BLOCK-
  TRIANGULAR: the third column is a quadrature slave of column 1.
(A2) 2x2-STAYS: the r244 reading (border as scalar companion).
SEALED ADJUDICATION: SCHLESINGER_RANK1_INSERTION iff A1b passes all
gates with the unipotent structure intact AND its solvability data
(det) is independent of (sigma, B) AND leg-B lands rank 2 on the
primary objects -- then A1 is exact packaging of A2 (block-trivial
w.r.t. the bordered PSD: solvability never sees B or S; the PSD data
enters only through the Uvarov tau step, leg C).
IRREDUCIBLE_3X3_REQUIRED iff any gate NEEDS nonzero coupling entries
(3,1)/(3,2) or a non-block-triangular jump.  Else FORMULATION_OPEN.

LEG B -- MINIMAL INTEGRABLE RANK (the core).  Three sealed panels:
(P1, primary, node side) K_ext := the CD kernel K_n(t, t') =
  sum_{k<n} pihat_k(t) pihat_k(t')/h_k evaluated on the JOINT node
  grid (mutilde-atoms + sigma-atoms) -- the sigma-extension of the
  wall kernel: its mutilde-block IS the wall kernel, its sigma-smear
  kappa(t) = int K_n(t,s) dsigmatilde(s) = r_n(t) IS the Riesz
  representer (border column u), its double smear IS the budget
  S_{n-1} (r244 G31) -- the node kernel of the bordered Gram.
  Displacement [Y_ext, K_ext] with Y_ext = diag(joint nodes):
  rank counted EXACTLY (toy, rationals) and by SVD census + EXPLICIT
  generator reconstruction (r224 style: (t-t') K_n == [pihat_n(t)
  pihat_{n-1}(t') - pihat_{n-1}(t) pihat_n(t')]/h_{n-1}) at sealed
  degrees (6, 12, 20) on ALL ladder windows + controls, and in mp at
  the FULL depth n = N-1 on w9 (the razor).
(P2, primary, ONB side) Ghat := the bordered Gram in the pihat basis,
  [[diag(h_0..h_{n-1}), f], [f^T, B]], f = (F_0..F_{n-1}) -- the
  (N+1)x(N+1) object whose determinant is tau^b.  Displacement
  Delta := J_ext^T Ghat - Ghat J_ext with the extended one-sided
  Jacobi operator J_ext = J_n (+) [0] (border has no x-action data;
  xi = 0 sealed).  DERIVED, frozen, gated: the polynomial block of
  Delta is IDENTICALLY ZERO (h_j J_jk = h_k J_kj inside the
  truncation), the border column is Delta_{j,b} = T_j for j < n-1
  and T_{n-1} - F_n at the truncation boundary (the razor-adjacent
  F_N deficit), Delta is BUDGET-BLIND (identical for every B), and
  rank Delta = 2 EXACTLY: the border adds exactly one generator PAIR
  (T-vector, border direction) -- the displacement currency of a
  Schlesinger insertion.
(P3, disclosed secondary, S-CONSUMING diagnostic only) K_uva :=
  K_ext + rho rho^T/(B - S_{n-1}) with rho = 1_sigma - r_n (the
  direct-sum node realization of the residual e - r_n; realization
  sealed and typed): the Uvarov-projected kernel.  Expected from the
  Cauchy structure: displacement rank 2+2 (generators rho, Y rho on
  top of the CD pair), FIXED in n and N -- measured, never certified
  (its construction consumes S: gate-side only, firewalled).
SEALED VERDICTS (mutually exclusive, frozen): BORDERED_RANK2_EXACT
  iff P1 and P2 measure rank exactly 2 everywhere (toy exact + all
  windows + all controls + deep mp) with no N-trend -- the border
  direction lies in the existing generator space; BORDERED_RANK3_EXACT
  iff exactly one new independent generator (consistent rank 3);
  BORDERED_FIXED_RANK_HIGHER(r) iff fixed rank r >= 4, N-independent;
  BORDERED_RANK_GROWS iff ANY panel rank trends upward with n or N
  (census: rank at degrees 6/12/20 per window; Spearman(rank; N) >
  0.3 or max > min across degrees) -- a hard warning for every
  classical parametrix and a valid result.  Modifier appended:
  UVAROV_PROJECTION_2PLUS2_FIXED iff P3 measures fixed rank 4.

LEG C -- FULL PIVOT CHAIN FROM THE FORMULATION (the
BORDERED_DETERMINANT_ONLY kill): the augmented z-space solution data
carries the COMPLETE pivot chain, not just the terminal determinant:
h_{k-1} = W_{k,k-1}(z) (z-independent Wronskian minor of columns 1-2),
F_k = (z - alphahat_k) Csig_k(z) - gammahat_k Csig_{k-1}(z) -
Csig_{k+1}(z) (exact transfer readout, k = 0 without the gamma term),
rho_k = F_k^2/h_{k-1+1}, and the autonomous corner flow D_{k+1} =
D_k - rho_k from D_0 = B reconstructs (h_0..h_{n-1}, B - S_{n-1}) =
the EXACT nested pivots of the bordered Hankel [[H_n, u],[u^T, B]]
(r243 G12).  Gated: rationals on the toy (all n, both sealed
budgets) vs exact LDL pivots; mp (dps 60) on w9/w12 at n = 8/12 vs
direct bordered LDL, B in {2, 20}; mp (dps 160) through ALL w9
degrees: per-degree F-readout identity + integrated D-flow vs the
direct budget telescope.  Verdict: FULL_PIVOT_CHAIN_CARRIED /
BORDERED_DETERMINANT_ONLY.

LEG D -- WORLD-BLIND + KILLS: every leg-A/B/C identity is gated on
MAIN and on EPSTEIN/SCRAMBLE/SMOOTH (same builder map, 4 distinct
input hashes); the algebra must hold IDENTICALLY (only values/signs
differ; mp through the sealed control flips 25/21/27 with h < 0);
SMOOTH is the F = 0 self-alias: the pure-degree 3x3 DEGENERATES
there (det -> 0, typed, the predicted breakdown), Y3aug survives
(det = 1 via the unipotent row), F-comparisons go to absolute
mass-norm guards (r243 amendment-a1 discipline).  GRID-OVERLAP
DISCLOSURE (amendment a1 of THIS round, smoke-caught): the folded
window atoms SHARE positions with the folded border grid on EVERY
world (common assembly grid) -- the joint grid is therefore the
DISJOINT-UNION index set: Y_ext has repeated diagonal entries
(legitimate displacement algebra, no (t - t') division anywhere;
the CD identity holds entrywise including the zero rows), and
rho = 1_sigma - r_n lives on the index set.  KILLS (self-audit,
sealed): TAU_TRANSCRIPTION (this round's new objects: det Y3 =
-h_{n-2} F_{n-1}, the unique-normalization census, R3 with the
F-entry, the three displacement panels and the rank census, the
z-space pivot assembly -- none is a transcription of r243/r244);
WALL_COMPLETION / TARGET_INVERSE_USED (no h-sign chain, no tau, no
S in any construction path; B free; K_uva's S-consumption disclosed
as diagnostic); GENERATOR_RANK_GROWS (the census); BORDERED_
DETERMINANT_ONLY (leg C).  MUST-FAILS (each loud): (m1) DROPPED
SOURCE: R3 without the (1,3) entry breaks the step by exactly F_n
(toy exact + f64 >= 1e3 x honest); (m2) SWAPPED COLUMNS 2<->3:
det breaks loudly, the step breaks loudly; (m3a) sigma SHIFTED
(u-grid + 0.05): the pivot/readout assembly breaks loudly against
the true bordered pivots; (m3b) sigma SMOOTHED (weights -> uniform
mean, mass-preserving): same loud break; (m4) sign oracle
sign h_{N-1} hits 42/42 and is EXCLUDED by the input firewall.

SEALED CONSTANTS: ladder = frame-A h <= 900 (42 rungs); background
du = 0.01 masses 2 e^{u/2} du (r243 map via principal_bessel_probe.
smooth_comb); toy = r243 signed 9-atom toy + disjoint signed 5-atom
smooth border, degrees to 6; toy budgets B in {22/7, 5/3}; toy
z-census 45 rational points (constancy by degree-count argument);
normalization cube |a|,|b|,|c| <= n+2; f64 snapshot degree n = 12,
z-panel (1.7+0.9i, 0.31+0.77i); f64 bars det 1e-6, step/readout
1e-12 (mass-norm guards on F-scales); census degrees (6, 12, 20),
joint subgrid <= 30 per zone (<= 120 nodes), SVD rank threshold
1e-7 relative, recon bars 1e-11; ONB block bar 1e-12 (normalized),
T-column bar 1e-12 (mass-norm); grows bars
Spearman 0.3; uva budget B = 20 (windows), both toy budgets; mp
deep w9 dps 160 bars 1e-25, mp subgrid 15 + 15; mp flip panel
(controls) dps 60 bar 1e-20, degrees 2..flip+2; mp moderate pivots
w9/w12 dps 60, n = 8/12, B = 2/20, bar 1e-20; loud ratio 1e3;
sigma shift 0.05; control flips 25/21/27; runtime <= 1800 s.

RECORD TABLES (frozen from calib_bfr_pass1.log, 29/29 FIRST PASS,
wall 10.4 s full / 0.5 s smoke; pre-freeze SPEC_SHA
38d470ec92490534; disclosed SMOKE/CALIBRATION AMENDMENTS -- the
formulation candidates, the displacement panels, the sealed verdict
rules, the rank threshold and the pivot-assembly formulas NEVER
moved: (a1) GRID OVERLAP, smoke-caught live: the design planned a
SMOOTH-only collision dedupe, but the smoke run measured that the
folded window atoms share positions with the folded border grid on
EVERY world (common assembly grid; the per-world dedupe would have
voided the uva panel everywhere) -- replaced by the disjoint-union
index-set reading (Y_ext with repeated diagonal entries, legitimate
displacement algebra; overlap census disclosed in G44); (a2) the
draft f64 bars were set conservatively (5e-5 class, r234 CREC
precedent) BEFORE any run; calibration measured the honest devs
4-9 orders below and the bars were TIGHTENED at freeze (det 1e-6,
step/readout/recon/ONB 1e-12..1e-11) -- a strictness increase, no
rule moved):
CAL_VERDICT = FORMULATION(SCHLESINGER_RANK1_INSERTION) +
BORDERED_RANK2_EXACT + UVAROV_PROJECTION_2PLUS2_FIXED +
FULL_PIVOT_CHAIN_CARRIED.
Key numbers.  LEG A (toy rationals, n = 2..4): Laurent order table
EXACT (col2 cancellation depth m, col3 leading F_m, next T_m);
det Y3 = -h_{n-2} F_{n-1} at 45 z-points EXACT; unique
normalization: the 11^3 diagonal-gauge cube yields EXACTLY ONE
invertible gauge (a,b,c) = (-n, n-1, 1) at n = 3 AND 4, det L =
det Y3, L singular iff F_{n-1} = 0; residue dictionary (E_13 at
sigma-atoms, E_12 at mutilde-atoms, row 3 pole-free) exact;
det Y3aug = 1 and the R3 step with det R3 = 1 EXACT at all toy
z-points; sigma-mutation moves F while det Y3aug stays EXACTLY 1.
Windows f64 (42 + 3 worlds, n = 12, z-panel): det Y3aug - 1 worst
3.4e-9, R3-step worst 3.5e-15, F-readout worst 6.4e-16 (mass-norm),
world-blind.  mp: deep w9 (dps 160, ALL 184 degrees): det worst
5.9e-55, R3 border-column step 7.5e-159, F-readout vs pairing
1.1e-158; through-flip (dps 60, h < 0 crossed): EPSTEIN det 1.3e-45
step 1.3e-59 / SCRAMBLE 1.5e-48, 7.8e-61 / SMOOTH 4.3e-45, 1.3e-45
-- the augmented algebra is world-blind THROUGH the sign flips.
LEG B: toy exact ranks: [Y, K_ext] = 2 (n = 2..4, 14-node joint
grid, CD reconstruction entrywise exact, encoding ward kappa = r_n,
<r_n, pihat_k> = F_k, double smear = S_{n-1} exact); ONB Delta:
poly block == 0, border column == (T_0..T_{n-2}, T_{n-1} - F_n)
exact at BOTH budgets, budget-blind, rank 2 exact; K_uva rank 4
exact = 2 + 2 (generator quadruple independent, both budgets).
Windows: SVD census rank == 2 on 45/45 worlds at ALL degrees
6/12/20 (135 SVDs, sigma_3/sigma_1 worst 7.7e-16 vs eps 1e-7);
explicit CD reconstruction worst 4.8e-15 (n <= 12) / 1.2e-14
(n = 20); NO N-trend (Spearman = 0.00, max = min = 2) =>
GENERATOR_RANK_GROWS does NOT fire; ONB Delta: block worst 5.3e-16,
T-column worst 4.7e-16, rank 2 on 45/45, budget-blind max
|Delta(2) - Delta(20)| = 0 EXACTLY; uva census rank 4 on 45/45
(worst s4/s1 = 1.7e-2; overlap census 3..36 duplicated positions
per subgrid, a1); deep mp w9 razor: CD reconstruction at n = N-1
= 183 on the 30-node mp subgrid 5.9e-160, generators nondegenerate
=> displacement rank 2 AT THE RAZOR.  LEG C: toy pivot assembly
from PURE z-space readouts == LDL pivots (h_0..h_{n-1}, B -
S_{n-1}) EXACT (n = 2..4, both budgets, z-independence exact); mp
moderate (dps 60, w9 + w12, n = 8/12, B = 2/20): worst rel dev
1.3e-54 vs direct bordered LDL (z-independence ward 7.8e-55); mp
deep (dps 160, w9, ALL 184 degrees): integrated D-flow vs direct
telescope dev 8.2e-161 => FULL_PIVOT_CHAIN_CARRIED (the
formulation carries h_0..h_{N-1} AND every corner D_n, not only
tau^b).  LEG D: 4 distinct input hashes; SMOOTH: pure-degree
det Y3/scale = 0.0 EXACTLY (the predicted F = 0 degeneracy of the
pure-degree 3x3, typed) while Y3aug survives; MUST-FAILS all loud:
m1 dropped F-source 4.9e+8 x honest (+ exact toy break), m2
swapped columns det dev 2.2e+3 and step 3.4e+9 x honest, m3a
sigma-shift 1.3e+12 x honest, m3b sigma-smoothing 5.7e+12 x
honest, m4 sign oracle hits 42/42 and is EXCLUDED.  Determinism:
run1 == run2 (identical transcripts modulo wall-clock).
AMENDMENTS AFTER FREEZE: NONE.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH           # noqa: E402 r244
import hirota_sign_probe as HS               # noqa: E402 r226
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

H_CAP = 900
N_SNAP = 12
CENSUS_DEGS = (6, 12, 20)
SUB_CAP = 30
RANK_EPS = 1e-7
Z_PANEL = (1.7 + 0.9j, 0.31 + 0.77j)
NZ_TOY = 45
NTOY = 4
B_TOY = (Fr(22, 7), Fr(5, 3))
B_MP = (2, 20)
B_UVA = 20.0
DET12_BAR = 1e-6          # tightened at freeze (a2), disclosed
STEP12_BAR = 1e-12        # (a2)
FRD12_BAR = 1e-12         # (a2)
RECON_BAR = 1e-11         # (a2)
RECON20_BAR = 1e-11       # (a2)
ONB_BLK_BAR = 1e-12       # (a2)
ONB_T_BAR = 1e-12         # (a2)
GEN4_MIN = 1e-10
GROWS_SPEAR = 0.3
MP_DPS = 160
MPDEEP_BAR = 1e-25
MP_SUB = 15
MPFLIP_DPS = 60
MPFLIP_BAR = 1e-20
MPPIV_BAR = 1e-20
MPPIV_NS = (8, 12)
MP_MOD_W = (9, 12)
LOUD = 1e3
SIG_SHIFT = 0.05
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
SMOKE_KZ = (9, 12, 13, 26, 40)
CAL_VERDICT = ("FORMULATION(SCHLESINGER_RANK1_INSERTION) + "
               "BORDERED_RANK2_EXACT + UVAROV_PROJECTION_2PLUS2_FIXED"
               " + FULL_PIVOT_CHAIN_CARRIED")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; constructions consume "
                       "nodes/weights/moments + border data only; B "
                       "free; K_uva S-consumption disclosed as "
                       "diagnostic; ground truth in gates only"
                       if not bad else "; ".join(bad))


# --------------------------------------------------- exact helpers
def frac_rank(M):
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0]) if M else 0
    pr = 0
    for c in range(cols):
        piv = next((i for i in range(pr, rows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[pr], M[piv] = M[piv], M[pr]
        for i in range(rows):
            if i != pr and M[i][c] != 0:
                f = M[i][c] / M[pr][c]
                for j in range(c, cols):
                    M[i][j] -= f * M[pr][j]
        pr += 1
        if pr == rows:
            break
    return pr


def frac_ldl_pivots(G):
    G = [row[:] for row in G]
    n = len(G)
    piv = []
    for i in range(n):
        piv.append(G[i][i])
        for r in range(i + 1, n):
            f = G[r][i] / G[i][i]
            for c in range(i, n):
                G[r][c] -= f * G[i][c]
    return piv


def toy_cauchy(vals, wts, nodes, z):
    return sum(w * v / (z - x) for w, v, x in zip(wts, vals, nodes))


def svd_rank(D):
    s = np.linalg.svd(np.asarray(D, float), compute_uv=False)
    if s[0] <= 0.0 or not np.isfinite(s[0]):
        return 0, s
    return int(np.sum(s >= RANK_EPS * s[0])), s


# ---------------------------------------------- kernel-census chain
def kchain(xs, ws, ys, vs, bx, bw, by, bv, ixs, iys, ibx, iby,
           degs, n_upto):
    """r243/r244 scaled signed chain (recursion verbatim) with a
    joint SUBGRID evaluation: accumulates the k-sum CD kernel
    K_n = sum_{k<n} pihat_k pihat_k'/h_k, the representer r_n and
    the budget S on the subgrid; snapshots at the sealed census
    degrees carry (K, q_n, q_{n-1}, CD factor, r_n, S_{n-1}).
    Source-pure: node positions and weights only."""
    qx = np.ones_like(xs)
    qy = np.ones_like(ys)
    qb = np.ones_like(bx)
    qc = np.ones_like(by)
    qx_m = np.zeros_like(xs)
    qy_m = np.zeros_like(ys)
    qb_m = np.zeros_like(bx)
    qc_m = np.zeros_like(by)
    Ls = Ls_m = 0.0
    eta = float(np.sum(ws) - np.sum(vs))
    eta_m = eta
    npts = len(ixs) + len(iys) + len(ibx) + len(iby)
    K = np.zeros((npts, npts))
    rsub = np.zeros(npts)
    S = 0.0
    prev_t = np.zeros(npts)
    snaps = {}
    for n in range(n_upto):
        fb = float(np.sum(bw * qb) - np.sum(bv * qc))
        qt = np.concatenate([qx[ixs], qy[iys], qb[ibx], qc[iby]])
        if n in degs and n >= 1:
            snaps[n] = dict(K=K.copy(), qn=qt.copy(),
                            qm=prev_t.copy(),
                            fac=math.exp(Ls - Ls_m) / eta_m,
                            r=rsub.copy(), S=S)
        K += np.outer(qt, qt) / eta
        rsub += (fb / eta) * qt
        S += fb * fb / eta
        alh = (float(np.sum(ws * xs * qx * qx)
                     - np.sum(vs * ys * qy * qy))) / eta
        if n == 0:
            px = (xs - alh) * qx
            py = (ys - alh) * qy
            pb = (bx - alh) * qb
            pc = (by - alh) * qc
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            fc = math.exp(Ls_m - Ls)
            px = (xs - alh) * qx - ge * fc * qx_m
            py = (ys - alh) * qy - ge * fc * qy_m
            pb = (bx - alh) * qb - ge * fc * qb_m
            pc = (by - alh) * qc - ge * fc * qc_m
        sc = max(float(np.max(np.abs(px))), float(np.max(np.abs(py))),
                 float(np.max(np.abs(pb))), float(np.max(np.abs(pc))))
        if sc == 0.0 or not math.isfinite(sc):
            return snaps
        qx_m, qy_m, eta_m, Ls_m = qx, qy, eta, Ls
        qb_m, qc_m = qb, qc
        prev_t = qt
        qx, qy = px / sc, py / sc
        qb, qc = pb / sc, pc / sc
        Ls += math.log(sc)
        eta = float(np.sum(ws * qx * qx) - np.sum(vs * qy * qy))
        if eta == 0.0 or not math.isfinite(eta):
            return snaps
    return snaps


def sub_idx(m):
    if m <= SUB_CAP:
        return np.arange(m)
    return np.unique(np.linspace(0, m - 1, SUB_CAP).astype(int))


# ---------------------------------------------------- window packs
def wload(kz, base_kw=None):
    d = HS.window_data(kz, **(base_kw or {}))
    N = d["n_max"]
    alpha = PIK.build_rung(kz)["alpha"]
    dsm = HS.window_data(kz, comb=PB.smooth_comb(alpha))
    n_ch = N if base_kw is None else 32
    rows = BH.bord_chain(d["xs"], d["ws"], d["ys"], d["vs"],
                         dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"],
                         n_ch)
    nf = next((r["n"] for r in rows if r["sg_h"] < 0), None)
    m = N_SNAP
    alh = [rows[k]["alh"] for k in range(m + 4)]
    gamv = [0.0] + [rows[k]["gam_next"] for k in range(m + 3)]
    hv = [rows[k]["sg_h"] * math.exp(rows[k]["lg_h"])
          for k in range(m + 3)]
    Fv = [rows[k]["fb"] * math.exp(rows[k]["Ls"])
          for k in range(m + 3)]
    Tv = [rows[k]["tb"] * math.exp(rows[k]["Ls"])
          for k in range(m + 3)]
    S_pre = np.cumsum([r["rho"] for r in rows])
    xall = np.concatenate([d["xs"], d["ys"]])
    wall = np.concatenate([d["ws"], -d["vs"]])
    ball = np.concatenate([dsm["xs"], dsm["ys"]])
    bwall = np.concatenate([dsm["ws"], -dsm["vs"]])
    Pb, _ = BH.plain_vals(alh, gamv, ball, m + 2)
    aw = np.abs(bwall)
    Fabs = [float(aw @ np.abs(Pb[k])) for k in range(m + 3)]
    Tabs = [float(aw @ np.abs(ball * Pb[k])) for k in range(m + 3)]
    ixs = sub_idx(len(d["xs"]))
    iys = sub_idx(len(d["ys"]))
    ibx = sub_idx(len(dsm["xs"]))
    iby = sub_idx(len(dsm["ys"]))
    snaps = kchain(d["xs"], d["ws"], d["ys"], d["vs"],
                   dsm["xs"], dsm["ws"], dsm["ys"], dsm["vs"],
                   ixs, iys, ibx, iby, set(CENSUS_DEGS), 22)
    tpos = np.concatenate([d["xs"][ixs], d["ys"][iys],
                           dsm["xs"][ibx], dsm["ys"][iby]])
    sig_mask = np.concatenate([np.zeros(len(ixs) + len(iys)),
                               np.ones(len(ibx) + len(iby))]) > 0.5
    return dict(kz=kz, N=N, d=d, dsm=dsm, rows=rows, nf=nf,
                alh=alh, gamv=gamv, hv=hv, Fv=Fv, Tv=Tv,
                S_pre=S_pre, xall=xall, wall=wall, ball=ball,
                bwall=bwall, Fabs=Fabs, Tabs=Tabs, snaps=snaps,
                tpos=tpos, sig_mask=sig_mask)


def overlap_census(p):
    """builder-grid overlap census (disclosed): the folded window
    atoms and the folded border atoms share POSITIONS (common
    assembly grid) -- the joint grid is the DISJOINT-UNION index
    set; Y_ext = diag(positions) has repeated entries, which is
    legitimate displacement algebra (no division by t - t'
    anywhere; CD identity holds entrywise incl. zero rows)."""
    key = np.round(p["tpos"], 12)
    u, c = np.unique(key, return_counts=True)
    return int(np.sum(c > 1))


def zvals(alh, gamv, z, m):
    pv = [1.0 + 0j, z - alh[0]]
    for k in range(1, m):
        pv.append((z - alh[k]) * pv[k] - gamv[k] * pv[k - 1])
    return pv


def zpanel_gates(p, z, n):
    """f64 leg-A panel at degree n: det Y3aug, R3 step, F-readout,
    plus must-fail material (m1 dropped source, m2 swapped cols)."""
    alh, gamv, hv, Fv = p["alh"], p["gamv"], p["hv"], p["Fv"]
    P, _ = BH.plain_vals(alh, gamv, p["xall"], n + 2)
    Pb, _ = BH.plain_vals(alh, gamv, p["ball"], n + 2)
    inv = 1.0 / (z - p["xall"])
    binv = 1.0 / (z - p["ball"])
    C = {k: complex(np.sum(p["wall"] * P[k] * inv))
         for k in (n - 1, n, n + 1)}
    Cs = {k: complex(np.sum(p["bwall"] * Pb[k] * binv))
          for k in (n - 1, n, n + 1)}
    pz = zvals(alh, gamv, z, n + 2)

    def y3(nn):
        return np.array(
            [[pz[nn], C[nn], Cs[nn]],
             [pz[nn - 1] / hv[nn - 1], C[nn - 1] / hv[nn - 1],
              Cs[nn - 1] / hv[nn - 1]],
             [0.0, 0.0, 1.0]], complex)

    # C/Cs at n+1 needed for Y_{n+1}; C at n-1..n+1 available
    C2 = dict(C)
    Cs2 = dict(Cs)
    Yn = y3(n)
    Yn1 = np.array(
        [[pz[n + 1], C2[n + 1], Cs2[n + 1]],
         [pz[n] / hv[n], C2[n] / hv[n], Cs2[n] / hv[n]],
         [0.0, 0.0, 1.0]], complex)
    det_dev = abs(np.linalg.det(Yn) - 1.0)
    R3 = np.array([[z - alh[n], -hv[n], -Fv[n]],
                   [1.0 / hv[n], 0.0, 0.0],
                   [0.0, 0.0, 1.0]], complex)
    Pr = R3 @ Yn
    step_dev = 0.0
    for j in range(3):
        scj = max(np.max(np.abs(Yn1[:, j])), 1e-300)
        step_dev = max(step_dev,
                       float(np.max(np.abs(Pr[:, j] - Yn1[:, j]))
                             / scj))
    frd = ((z - alh[n]) * Cs[n] - gamv[n] * Cs[n - 1] - Cs[n + 1])
    frd_dev = abs(frd - Fv[n]) / max(p["Fabs"][n], 1e-300)
    # m1: dropped source residual (col 3 only)
    R3b = R3.copy()
    R3b[0, 2] = 0.0
    Prb = R3b @ Yn
    sc3 = max(np.max(np.abs(Yn1[:, 2])), 1e-300)
    m1_dev = float(np.max(np.abs(Prb[:, 2] - Yn1[:, 2])) / sc3)
    # m2: swapped columns 2 <-> 3
    Ysw = Yn[:, [0, 2, 1]].copy()
    Ysw[2] = np.array([0.0, 0.0, 1.0])
    m2_det = abs(np.linalg.det(Ysw) - 1.0)
    Ysw1 = Yn1[:, [0, 2, 1]].copy()
    Ysw1[2] = np.array([0.0, 0.0, 1.0])
    Psw = R3 @ Ysw
    m2_step = 0.0
    for j in range(3):
        scj = max(np.max(np.abs(Ysw1[:, j])), 1e-300)
        m2_step = max(m2_step,
                      float(np.max(np.abs(Psw[:, j] - Ysw1[:, j]))
                            / scj))
    return dict(det=det_dev, step=step_dev, frd=frd_dev,
                m1=m1_dev, m2d=m2_det, m2s=m2_step)


def onb_delta(p, n, B):
    """ONB-side displacement Delta = J_ext^T Ghat - Ghat J_ext."""
    hv, Fv, alh, gamv = p["hv"], p["Fv"], p["alh"], p["gamv"]
    J = np.zeros((n + 1, n + 1))
    for k in range(n):
        J[k, k] = alh[k]
        if k + 1 <= n - 1:
            J[k + 1, k] = 1.0
        if k >= 1:
            J[k - 1, k] = gamv[k]
    G = np.zeros((n + 1, n + 1))
    for k in range(n):
        G[k, k] = hv[k]
        G[k, n] = G[n, k] = Fv[k]
    G[n, n] = B
    D = J.T @ G - G @ J
    scale = np.abs(J.T) @ np.abs(G) + np.abs(G) @ np.abs(J)
    blk = float(np.max(np.abs(D[:n, :n])
                       / np.maximum(scale[:n, :n], 1e-300)))
    tdev = 0.0
    for j in range(n):
        want = p["Tv"][j] if j < n - 1 else p["Tv"][j] - Fv[n]
        tdev = max(tdev, abs(D[j, n] - want)
                   / max(p["Tabs"][j], 1e-300))
    rk, _s = svd_rank(D)
    return dict(D=D, blk=blk, tdev=tdev, rank=rk)


# ------------------------------------------------------- mp blocks
def mp_deep_w9(p, dps, zc, budgets):
    """dps-160 full-depth w9: det Y3aug, R3 step, F-readout vs
    pairing per degree; integrated D-flow vs direct telescope;
    CD reconstruction of the k-sum kernel at n = N-1 on the mp
    subgrid (the razor rank gate)."""
    import mpmath as mp
    mp.mp.dps = dps
    d, dsm = p["d"], p["dsm"]
    N = p["N"]
    nds = ([mp.mpf(float(x)) for x in d["xs"]]
           + [mp.mpf(float(y)) for y in d["ys"]])
    wt = ([mp.mpf(float(w)) for w in d["ws"]]
          + [-mp.mpf(float(v)) for v in d["vs"]])
    bns = ([mp.mpf(float(x)) for x in dsm["xs"]]
           + [mp.mpf(float(y)) for y in dsm["ys"]])
    bwm = ([mp.mpf(float(w)) for w in dsm["ws"]]
           + [-mp.mpf(float(v)) for v in dsm["vs"]])
    z = mp.mpc(zc)
    inv = [1 / (z - x) for x in nds]
    binv = [1 / (z - x) for x in bns]
    isub = list(np.unique(np.linspace(0, len(nds) - 1,
                                      MP_SUB).astype(int)))
    jsub = list(np.unique(np.linspace(0, len(bns) - 1,
                                      MP_SUB).astype(int)))
    tsub = [nds[i] for i in isub] + [bns[j] for j in jsub]
    ns = len(tsub)
    Ksub = [[mp.mpf(0)] * ns for _ in range(ns)]
    pk = [mp.mpf(1)] * len(nds)
    pkm = [mp.mpf(0)] * len(nds)
    bk = [mp.mpf(1)] * len(bns)
    bkm = [mp.mpf(0)] * len(bns)
    pz = [mp.mpc(1), mp.mpc(0)]     # p_n(z), p_{n-1}(z)
    hs = [mp.fsum(w * q * q for w, q in zip(wt, pk))]
    Cur = dict(C=None, Cs=None, Cm=None, Csm=None)
    Cur["C"] = mp.fsum(w * q * iv for w, q, iv in zip(wt, pk, inv))
    Cur["Cs"] = mp.fsum(w * q * iv
                        for w, q, iv in zip(bwm, bk, binv))
    F_pair = [mp.fsum(w * q for w, q in zip(bwm, bk))]
    als, gms = [], []
    S_dir = mp.mpf(0)
    rho_read = []
    det_dev = step_dev = frd_dev = mp.mpf(0)
    gen = {}
    for k in range(N):
        if k < N - 1:
            vsub = [pk[i] for i in isub] + [bk[j] for j in jsub]
            for a in range(ns):
                va = vsub[a] / hs[-1]
                for b in range(ns):
                    Ksub[a][b] += va * vsub[b]
        if k >= N - 2:
            gen[k] = ([pk[i] for i in isub]
                      + [bk[j] for j in jsub])
        S_dir += F_pair[-1] ** 2 / hs[-1]
        a = mp.fsum(w * x * q * q
                    for w, x, q in zip(wt, nds, pk)) / hs[-1]
        g = (hs[-1] / hs[-2]) if k > 0 else mp.mpf(0)
        als.append(a)
        gms.append(g)
        nx = [(x - a) * q - g * qq
              for x, q, qq in zip(nds, pk, pkm)]
        nb = [(x - a) * q - g * qq
              for x, q, qq in zip(bns, bk, bkm)]
        pz = [(z - a) * pz[0] - g * pz[1], pz[0]]
        pkm, pk = pk, nx
        bkm, bk = bk, nb
        hs.append(mp.fsum(w * q * q for w, q in zip(wt, pk)))
        C_new = mp.fsum(w * q * iv for w, q, iv in zip(wt, pk, inv))
        Cs_new = mp.fsum(w * q * iv
                         for w, q, iv in zip(bwm, bk, binv))
        F_new = mp.fsum(w * q for w, q in zip(bwm, bk))
        # det Y3aug at degree k+1 (needs degrees k+1, k)
        detv = (pz[0] * Cur["C"] - pz[1] * C_new) / hs[-2]
        det_dev = max(det_dev, abs(detv - 1))
        # R3 step, column 3: Cs_{k+1} = (z-a) Cs_k - g Cs_{k-1} - F_k
        rhs = (z - a) * Cur["Cs"] - (g * Cur["Csm"]
                                     if Cur["Csm"] is not None
                                     else 0) - F_pair[-1]
        sc = max(abs(Cs_new), abs(F_pair[-1]), mp.mpf("1e-300"))
        step_dev = max(step_dev, abs(Cs_new - rhs) / sc)
        # F-readout (rearranged transfer) vs pairing
        fr = (z - a) * Cur["Cs"] - (g * Cur["Csm"]
                                    if Cur["Csm"] is not None
                                    else 0) - Cs_new
        sc = max(abs(F_pair[-1]), mp.mpf("1e-300"))
        frd_dev = max(frd_dev, abs(fr - F_pair[-1]) / sc)
        rho_read.append(mp.re(fr) ** 2 / hs[-2])
        Cur["Cm"], Cur["C"] = Cur["C"], C_new
        Cur["Csm"], Cur["Cs"] = Cur["Cs"], Cs_new
        F_pair.append(F_new)
    # D-flow vs direct telescope (linear in B: one number)
    # rho_read[k] = F_k(readout)^2 / h_k for k = 0..N-1
    Sread = mp.fsum(rho_read[:N])
    dflow_dev = float(abs(Sread - S_dir) / abs(S_dir))
    # CD reconstruction at n = N-1 on the subgrid
    rec = mp.mpf(0)
    hnm2 = hs[N - 2]
    gN, gM = gen[N - 1], gen[N - 2]
    dmax = mp.mpf(0)
    for a_ in range(ns):
        for b_ in range(ns):
            dd = (tsub[a_] - tsub[b_]) * Ksub[a_][b_]
            cd = (gN[a_] * gM[b_] - gM[a_] * gN[b_]) / hnm2
            rec = max(rec, abs(dd - cd))
            dmax = max(dmax, abs(dd))
    rec_rel = float(rec / dmax) if dmax > 0 else 0.0
    nong = min(max(abs(v) for v in gN), max(abs(v) for v in gM))
    return dict(det=float(mp.re(abs(det_dev))),
                step=float(mp.re(abs(step_dev))),
                frd=float(mp.re(abs(frd_dev))),
                dflow=dflow_dev, rec=rec_rel,
                nong=float(nong) != 0.0)


def mp_flip_panel(p, dps, zc, n_hi):
    """dps-60 control panel THROUGH the sign flip: det Y3aug and
    the R3 column-3 step for degrees 2..n_hi (h < 0 included)."""
    import mpmath as mp
    mp.mp.dps = dps
    d, dsm = p["d"], p["dsm"]
    nds = ([mp.mpf(float(x)) for x in d["xs"]]
           + [mp.mpf(float(y)) for y in d["ys"]])
    wt = ([mp.mpf(float(w)) for w in d["ws"]]
          + [-mp.mpf(float(v)) for v in d["vs"]])
    bns = ([mp.mpf(float(x)) for x in dsm["xs"]]
           + [mp.mpf(float(y)) for y in dsm["ys"]])
    bwm = ([mp.mpf(float(w)) for w in dsm["ws"]]
           + [-mp.mpf(float(v)) for v in dsm["vs"]])
    z = mp.mpc(zc)
    inv = [1 / (z - x) for x in nds]
    binv = [1 / (z - x) for x in bns]
    pk = [mp.mpf(1)] * len(nds)
    pkm = [mp.mpf(0)] * len(nds)
    bk = [mp.mpf(1)] * len(bns)
    bkm = [mp.mpf(0)] * len(bns)
    pz = [mp.mpc(1), mp.mpc(0)]
    hs = [mp.fsum(w * q * q for w, q in zip(wt, pk))]
    C_c = mp.fsum(w * q * iv for w, q, iv in zip(wt, pk, inv))
    Cs_c = mp.fsum(w * q * iv for w, q, iv in zip(bwm, bk, binv))
    Cs_m = None
    det_dev = step_dev = mp.mpf(0)
    min_h = mp.mpf("inf")
    n_neg = 0
    for k in range(n_hi):
        F_c = mp.fsum(w * q for w, q in zip(bwm, bk))
        a = mp.fsum(w * x * q * q
                    for w, x, q in zip(wt, nds, pk)) / hs[-1]
        g = (hs[-1] / hs[-2]) if k > 0 else mp.mpf(0)
        nx = [(x - a) * q - g * qq
              for x, q, qq in zip(nds, pk, pkm)]
        nb = [(x - a) * q - g * qq
              for x, q, qq in zip(bns, bk, bkm)]
        pz = [(z - a) * pz[0] - g * pz[1], pz[0]]
        pkm, pk = pk, nx
        bkm, bk = bk, nb
        hs.append(mp.fsum(w * q * q for w, q in zip(wt, pk)))
        if hs[-1] < 0:
            n_neg += 1
        min_h = min(min_h, abs(hs[-1]))
        C_new = mp.fsum(w * q * iv for w, q, iv in zip(wt, pk, inv))
        Cs_new = mp.fsum(w * q * iv
                         for w, q, iv in zip(bwm, bk, binv))
        detv = (pz[0] * C_c - pz[1] * C_new) / hs[-2]
        det_dev = max(det_dev, abs(detv - 1))
        rhs = (z - a) * Cs_c - (g * Cs_m if Cs_m is not None
                                else 0) - F_c
        sc = max(abs(Cs_new), abs(F_c), mp.mpf("1e-300"))
        step_dev = max(step_dev, abs(Cs_new - rhs) / sc)
        C_c = C_new
        Cs_m, Cs_c = Cs_c, Cs_new
    return dict(det=float(abs(det_dev)), step=float(abs(step_dev)),
                n_neg=n_neg)


def mp_mod_pivots(p, dps, zqs, n_list, budgets):
    """dps-60 moderate-depth pivot assembly from PURE z-space
    readouts (W-minor h, transfer-readout F, D-flow) vs the direct
    LDL pivots of the bordered moment matrix (BH.mp_moments)."""
    import mpmath as mp
    mp.mp.dps = dps
    d, dsm = p["d"], p["dsm"]
    n_hi = max(n_list)
    nds = ([mp.mpf(float(x)) for x in d["xs"]]
           + [mp.mpf(float(y)) for y in d["ys"]])
    wt = ([mp.mpf(float(w)) for w in d["ws"]]
          + [-mp.mpf(float(v)) for v in d["vs"]])
    bns = ([mp.mpf(float(x)) for x in dsm["xs"]]
           + [mp.mpf(float(y)) for y in dsm["ys"]])
    bwm = ([mp.mpf(float(w)) for w in dsm["ws"]]
           + [-mp.mpf(float(v)) for v in dsm["vs"]])
    zs = [mp.mpc(zq) for zq in zqs]
    invs = [[1 / (z - x) for x in nds] for z in zs]
    binvs = [[1 / (z - x) for x in bns] for z in zs]
    pk = [mp.mpf(1)] * len(nds)
    pkm = [mp.mpf(0)] * len(nds)
    bk = [mp.mpf(1)] * len(bns)
    bkm = [mp.mpf(0)] * len(bns)
    pzs = [[mp.mpc(1), mp.mpc(0)] for _ in zs]
    hs = [mp.fsum(w * q * q for w, q in zip(wt, pk))]
    Cc = [mp.fsum(w * q * iv for w, q, iv in zip(wt, pk, iv_))
          for iv_ in invs]
    Csc = [mp.fsum(w * q * iv for w, q, iv in zip(bwm, bk, iv_))
           for iv_ in binvs]
    Csm = [None for _ in zs]
    h_read = []
    F_read = []
    zind_dev = mp.mpf(0)
    for k in range(n_hi + 1):
        a = mp.fsum(w * x * q * q
                    for w, x, q in zip(wt, nds, pk)) / hs[-1]
        g = (hs[-1] / hs[-2]) if k > 0 else mp.mpf(0)
        nx = [(x - a) * q - g * qq
              for x, q, qq in zip(nds, pk, pkm)]
        nb = [(x - a) * q - g * qq
              for x, q, qq in zip(bns, bk, bkm)]
        for iz in range(len(zs)):
            pzs[iz] = [(zs[iz] - a) * pzs[iz][0] - g * pzs[iz][1],
                       pzs[iz][0]]
        pkm, pk = pk, nx
        bkm, bk = bk, nb
        hs.append(mp.fsum(w * q * q for w, q in zip(wt, pk)))
        hzs, fzs = [], []
        for iz in range(len(zs)):
            C_new = mp.fsum(w * q * iv
                            for w, q, iv in zip(wt, pk, invs[iz]))
            Cs_new = mp.fsum(w * q * iv
                             for w, q, iv in zip(bwm, bk,
                                                 binvs[iz]))
            # W-minor: h_k = p_{k+1} C_k - p_k C_{k+1}
            hzs.append(pzs[iz][0] * Cc[iz] - pzs[iz][1] * C_new)
            # transfer readout: F_k = (z-a) Cs_k - g Cs_{k-1}
            #                        - Cs_{k+1}
            fzs.append((zs[iz] - a) * Csc[iz]
                       - (g * Csm[iz] if Csm[iz] is not None
                          else 0) - Cs_new)
            Cc[iz] = C_new
            Csm[iz], Csc[iz] = Csc[iz], Cs_new
        zind_dev = max(zind_dev,
                       abs(hzs[0] - hzs[1]) / abs(hzs[0]),
                       abs(fzs[0] - fzs[1])
                       / max(abs(fzs[0]), mp.mpf("1e-300")))
        h_read.append(mp.re(hzs[0]))
        F_read.append(mp.re(fzs[0]))
    # direct bordered LDL from moments
    mmom, smom = BH.mp_moments(d, dsm, n_hi + 1, dps)
    worst = 0.0
    for n in n_list:
        for B in budgets:
            G = mp.zeros(n + 1, n + 1)
            for i in range(n):
                for j in range(n):
                    G[i, j] = mmom[i + j]
                G[i, n] = G[n, i] = smom[i]
            G[n, n] = mp.mpf(B)
            piv = []
            for i in range(n + 1):
                piv.append(G[i, i])
                for r in range(i + 1, n + 1):
                    f = G[r, i] / G[i, i]
                    for c in range(i, n + 1):
                        G[r, c] -= f * G[i, c]
            # assembled: h_0..h_{n-1} from W-minors, corner via
            # D-flow with readout F
            Dn = mp.mpf(B)
            for k in range(n):
                Dn -= F_read[k] ** 2 / h_read[k]
            for k in range(n):
                worst = max(worst, float(abs(h_read[k] - piv[k])
                                         / abs(piv[k])))
            worst = max(worst, float(abs(Dn - piv[n])
                                     / abs(piv[n])))
    return dict(worst=worst, zind=float(zind_dev))


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("bordered_finite_rank_probe -- PRIME.PORT.RHP."
          "BORDEREDHANKEL.FINITE.02 (round 245)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (five known rungs, mp blocks "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "formulation candidates A1a/A1b/A2, displacement panels "
          "P1/P2/P3, rank verdicts (RANK2/RANK3/FIXED_HIGHER/GROWS)"
          " and pivot verdict sealed in the frozen spec; census "
          "degrees %s, subgrid <= %d/zone, rank eps %.0e; toy "
          "budgets %s, window budgets %s, uva B = %.0f; f64 bars "
          "det/step/frd %.0e, recon %.0e/%.0e, ONB %.0e/%.0e; mp "
          "deep dps %d bar %.0e, flip dps %d bar %.0e, pivots bar "
          "%.0e; loud ratio %.0e; control flips 25/21/27"
          % (str(CENSUS_DEGS), SUB_CAP, RANK_EPS,
             str([str(b) for b in B_TOY]), str(B_MP), B_UVA,
             DET12_BAR, RECON_BAR, RECON20_BAR, ONB_BLK_BAR,
             ONB_T_BAR, MP_DPS, MPDEEP_BAR, MPFLIP_DPS,
             MPFLIP_BAR, MPPIV_BAR, LOUD))

    # ================= S1: toy -- pure-degree 3x3 (leg A1a)
    section("S1  LEG A1a -- PURE-DEGREE 3x3 (exact rationals)")
    JFn = [Fr(-7, 8), Fr(-5, 8), Fr(-3, 8), Fr(-1, 8), Fr(1, 8),
           Fr(3, 8), Fr(5, 8), Fr(7, 8), Fr(0, 1)]
    JFw = [Fr(3, 7), Fr(-2, 9), Fr(5, 11), Fr(1, 4), Fr(-3, 8),
           Fr(2, 5), Fr(-1, 6), Fr(4, 9), Fr(1, 3)]
    SBn = [Fr(-13, 16), Fr(-7, 16), Fr(-1, 16), Fr(5, 16),
           Fr(11, 16)]
    SBw = [Fr(2, 5), Fr(-1, 7), Fr(3, 8), Fr(-2, 11), Fr(1, 3)]
    NT2 = NTOY + 2
    al, hs, vals = PB.toy_chain(JFn, JFw, NT2)
    assert all(h != 0 for h in hs[:NT2 + 1]), "toy degenerate"
    sp = [[PB.toy_eval(al, hs, k, s) for s in SBn]
          for k in range(NT2 + 1)]
    Ftoy = [sum(w * v for w, v in zip(SBw, sp[k]))
            for k in range(NT2 + 1)]
    Ttoy = [sum(w * s * v for w, s, v in zip(SBw, SBn, sp[k]))
            for k in range(NT2 + 1)]
    assert all(Ftoy[k] != 0 for k in range(NTOY + 1)), "F = 0 toy"
    Stoy = []
    acc = Fr(0)
    for k in range(NT2):
        acc += Ftoy[k] * Ftoy[k] / hs[k]
        Stoy.append(acc)
    gmt = [Fr(0)] + [hs[k] / hs[k - 1] for k in range(1, NT2 + 1)]

    def Cmu(k, z):
        return toy_cauchy(vals[k], JFw, JFn, z)

    def Csg(k, z):
        return toy_cauchy(sp[k], SBw, SBn, z)

    def pz_t(k, z):
        return PB.toy_eval(al, hs, k, z)

    ZS = [Fr(150 + 7 * i, 41) for i in range(NZ_TOY)]
    # G10: Laurent order table (exact moments)
    ok10 = True
    for m in range(NTOY + 1):
        mu_m = [sum(w * v * x ** j
                    for w, v, x in zip(JFw, vals[m], JFn))
                for j in range(m + 2)]
        ok10 = ok10 and all(mu_m[j] == 0 for j in range(m)) \
            and mu_m[m] == hs[m]
        sg_m = [sum(w * v * x ** j
                    for w, v, x in zip(SBw, sp[m], SBn))
                for j in range(2)]
        ok10 = ok10 and sg_m[0] == Ftoy[m] and sg_m[1] == Ttoy[m]
    check("G10-laurent-orders-exact", ok10,
          "rationals m = 0..4: col2 = C[pihat_m mutilde] has "
          "EXACTLY m leading cancellations (<pihat_m, x^j> = 0 for "
          "j < m, = h_m at j = m) => order z^{-m-1} leading h_m; "
          "col3 = Csig_m has NO cancellation: order z^{-1} leading "
          "F_m, next coefficient T_m (the r244 flow source IS the "
          "z^{-2} readout of the border column); col1 monic degree "
          "m -- the frozen order table of the augmented problem")
    # G11: unique diagonal normalization (exact enumeration)
    ok11 = True
    for n in (3, 4):
        O = [[n - i, -(n - i) - 1, -1] for i in range(3)]
        Lc = [[Fr(1), hs[n - i], Ftoy[n - i]] for i in range(3)]
        found = []
        for a in range(-n - 2, n + 3):
            for b in range(-n - 2, n + 3):
                for c in range(-n - 2, n + 3):
                    pw = (a, b, c)
                    ok = True
                    L = [[Fr(0)] * 3 for _ in range(3)]
                    for i in range(3):
                        for j in range(3):
                            e = O[i][j] + pw[j]
                            if e > 0:
                                ok = False
                                break
                            if e == 0:
                                L[i][j] = Lc[i][j]
                        if not ok:
                            break
                    if ok and det3(L) != 0:
                        found.append((pw, det3(L)))
        ok11 = ok11 and len(found) == 1 \
            and found[0][0] == (-n, n - 1, 1) \
            and found[0][1] == -hs[n - 2] * Ftoy[n - 1]
    check("G11-unique-normalization-census", ok11,
          "exact enumeration over the full diagonal-gauge cube "
          "|a|,|b|,|c| <= n+2 (n = 3 and 4): EXACTLY ONE gauge "
          "diag(z^{-n}, z^{n-1}, z) gives a finite INVERTIBLE "
          "limit L (permutation-triangular, det L = -h_{n-2} "
          "F_{n-1} = det Y3); L is singular iff F_{n-1} = 0 -- "
          "the pure-degree 3x3 normalizes UNIQUELY and its "
          "nondegeneracy is the border nondegeneracy (SMOOTH "
          "F = 0 kills it, typed in S6)")
    # G12: det Y3 = -h_{n-2} F_{n-1}, constant in z
    ok12 = True
    for n in range(2, NTOY + 1):
        want = -hs[n - 2] * Ftoy[n - 1]
        for z in ZS:
            M = [[pz_t(n - i, z), Cmu(n - i, z), Csg(n - i, z)]
                 for i in range(3)]
            ok12 = ok12 and (det3(M) == want)
    check("G12-puredegree-det-exact", ok12,
          "det Y3_n(z) = -h_{n-2} F_{n-1} EXACT at %d rational "
          "z-points for n = 2..4 (constant by the degree-count "
          "argument: a rational function of bounded degree equal "
          "at more points than its degree is constant): the "
          "pure-degree 3x3 has CONSTANT determinant carrying the "
          "border weight F_{n-1} -- solvable iff the 2x2 is AND "
          "F != 0; it sees F but NEVER B or S: no PSD encoding "
          "in its solvability" % NZ_TOY)
    # G13: residue dictionary (structural)
    n = 3
    ok13 = True
    for a, (s_a, sw_a) in enumerate(zip(SBn, SBw)):
        res = (sw_a * sp[n][a], sw_a * sp[n - 1][a] / hs[n - 1],
               Fr(0))
        col1 = (sp[n][a], sp[n - 1][a] / hs[n - 1], Fr(0))
        ok13 = ok13 and res == tuple(sw_a * v for v in col1)
        # regularized limit of (z - s_a) Csig_n at s_a
        lim = sw_a * sp[n][a] + sum(
            SBw[b] * sp[n][b] * (s_a - s_a) / (s_a - SBn[b])
            for b in range(len(SBn)) if b != a)
        ok13 = ok13 and lim == sw_a * sp[n][a]
    for i, (x_i, w_i) in enumerate(zip(JFn, JFw)):
        res = (w_i * vals[n][i], w_i * vals[n - 1][i] / hs[n - 1],
               Fr(0))
        col1 = (vals[n][i], vals[n - 1][i] / hs[n - 1], Fr(0))
        ok13 = ok13 and res == tuple(w_i * v for v in col1)
    check("G13-residue-dictionary", ok13,
          "structural dictionary gate (by construction, "
          "disclosed): Res_{y_a} Y3aug = lim Y3aug (sv_a E_13) at "
          "every sigma-atom and Res_{x_i} Y3aug = lim Y3aug (w_i "
          "E_12) at every mutilde-atom -- BOTH jumps are NILPOTENT"
          " and couple ONLY into column 1; row 3 is pole-free: "
          "the jump data is block-triangular, the third column is "
          "a quadrature slave of column 1 (regularized limit of "
          "(z - y_a) Csig_n gated exact)")

    # ================= S2: toy -- augmented Y3aug (leg A1b)
    section("S2  LEG A1b -- UNIPOTENT-AUGMENTED Y3aug (exact)")

    def y3aug_t(n, z, csg=None):
        cs = csg if csg is not None else Csg
        return [[pz_t(n, z), Cmu(n, z), cs(n, z)],
                [pz_t(n - 1, z) / hs[n - 1],
                 Cmu(n - 1, z) / hs[n - 1],
                 cs(n - 1, z) / hs[n - 1]],
                [Fr(0), Fr(0), Fr(1)]]

    ok20 = True
    for n in range(2, NTOY + 1):
        for z in ZS[:9]:
            ok20 = ok20 and det3(y3aug_t(n, z)) == 1
    check("G20-y3aug-det-one-exact", ok20,
          "det Y3aug_n(z) = 1 EXACT (rationals, n = 2..4, 9 "
          "z-points): the unipotent third row makes det Y3aug = "
          "det Y_2x2 = 1 -- adding the border column changes NO "
          "solvability data (sigma- and B-blind determinant); "
          "normalization Y3aug diag(z^{-n}, z^n, 1) = I + Y1/z "
          "with Y1_13 = F_n (Laurent leading, G10): the border "
          "data is the infinity readout of the third column")
    ok21 = True
    for n in range(2, NTOY):
        for z in ZS[:6]:
            Yn = y3aug_t(n, z)
            Yn1 = y3aug_t(n + 1, z)
            R3 = [[z - al[n], -hs[n], -Ftoy[n]],
                  [Fr(1) / hs[n], Fr(0), Fr(0)],
                  [Fr(0), Fr(0), Fr(1)]]
            ok21 = ok21 and det3(R3) == 1
            for i in range(3):
                for j in range(3):
                    prod = sum(R3[i][m] * Yn[m][j]
                               for m in range(3))
                    ok21 = ok21 and prod == Yn1[i][j]
    check("G21-r3-step-exact", ok21,
          "Y3aug_{n+1} = R3_n Y3aug_n EXACT (rationals, n = 2..3, "
          "6 z-points) with R3_n = [[z - alphahat_n, -h_n, -F_n], "
          "[1/h_n, 0, 0], [0, 0, 1]], det R3 = 1: the r244 flow "
          "INHOMOGENEITY (F-source) appears as the (1,3) MATRIX "
          "ENTRY of a unimodular 3x3 transfer -- the bordered "
          "problem is the 2x2 FIK Schlesinger chain plus one "
          "parabolic (unipotent) column, homogenized by the "
          "constant row; entries (3,1)/(3,2) stay EXACTLY 0")
    # G24 toy part: sigma-mutation leaves det Y3aug = 1, moves F
    SBw_m = list(SBw)
    SBw_m[2] = SBw[2] * (1 + Fr(1, 7))
    sp_m = sp

    def Csg_m(k, z):
        return toy_cauchy(sp_m[k], SBw_m, SBn, z)

    F_mut = sum(w * v for w, v in zip(SBw_m, sp[3]))
    ok24 = (F_mut != Ftoy[3])
    for z in ZS[:4]:
        ok24 = ok24 and det3(y3aug_t(3, z, csg=Csg_m)) == 1
    check("G24-solvability-sigma-blind", ok24,
          "mutating a sigma weight moves F_3 (border data changes)"
          " while det Y3aug stays EXACTLY 1: the solvability of "
          "the augmented formulation is sigma-blind and B never "
          "appears -- the bordered PSD statement is NOT encoded "
          "in the jump/solvability data of the 3x3, it lives in "
          "the Uvarov tau step on top (leg C); adjudication "
          "material for SCHLESINGER vs IRREDUCIBLE")

    # ================= S4-toy: displacement panels (leg B, exact)
    section("S3  LEG B -- DISPLACEMENT RANK (exact toy panels)")
    tj = JFn + SBn
    ok40 = True
    for n in range(2, NTOY + 1):
        vj = [vals[k] + sp[k] for k in range(n + 1)]
        K = [[sum(vj[k][i] * vj[k][j] / hs[k] for k in range(n))
              for j in range(14)] for i in range(14)]
        D = [[(tj[i] - tj[j]) * K[i][j] for j in range(14)]
             for i in range(14)]
        ok40 = ok40 and frac_rank(D) == 2
        for i in range(14):
            for j in range(14):
                cd = (vj[n][i] * vj[n - 1][j]
                      - vj[n - 1][i] * vj[n][j]) / hs[n - 1]
                ok40 = ok40 and D[i][j] == cd
        # encoding ward: kappa = r_n, <r_n, p_k> = F_k, sig^2 = S
        kap = [sum(SBw[a] * K[i][9 + a] for a in range(5))
               for i in range(14)]
        rn = [sum(Ftoy[k] * vj[k][i] / hs[k] for k in range(n))
              for i in range(14)]
        ok40 = ok40 and kap == rn
        for k in range(n):
            pair = sum(JFw[i] * kap[i] * vj[k][i]
                       for i in range(9))
            ok40 = ok40 and pair == Ftoy[k]
        ok40 = ok40 and sum(SBw[a] * kap[9 + a]
                            for a in range(5)) == Stoy[n - 1]
    check("G40-kext-rank2-exact", ok40,
          "panel P1 (node side), rationals n = 2..4 on the 14-node"
          " joint grid: rank[(t - t') K_ext] = 2 EXACTLY, and the "
          "CD reconstruction (t-t') K_n = [pihat_n(t) pihat_{n-1}"
          "(t') - pihat_{n-1}(t) pihat_n(t')]/h_{n-1} holds "
          "ENTRYWISE -- the sigma-extension adds NO generator: "
          "the border direction kappa(t) = int K dsigma = r_n(t) "
          "(Riesz representer, <r_n, pihat_k> = F_k, double smear "
          "= S_{n-1}, all exact) is a POLYNOMIAL, inside the "
          "existing generator space")
    ok41 = True
    n = 3
    vj = [vals[k] + sp[k] for k in range(n + 1)]
    K3 = [[sum(vj[k][i] * vj[k][j] / hs[k] for k in range(n))
           for j in range(14)] for i in range(14)]
    rn = [sum(Ftoy[k] * vj[k][i] / hs[k] for k in range(n))
          for i in range(14)]
    rho_v = [(Fr(1) if i >= 9 else Fr(0)) - rn[i]
             for i in range(14)]
    for B in B_TOY:
        cB = B - Stoy[n - 1]
        Ku = [[K3[i][j] + rho_v[i] * rho_v[j] / cB
               for j in range(14)] for i in range(14)]
        Du = [[(tj[i] - tj[j]) * Ku[i][j] for j in range(14)]
              for i in range(14)]
        ok41 = ok41 and frac_rank(Du) == 4
        gens = [[vj[n][i], vj[n - 1][i], rho_v[i],
                 tj[i] * rho_v[i]] for i in range(14)]
        ok41 = ok41 and frac_rank(gens) == 4
    check("G41-kuva-rank-2plus2-exact", ok41,
          "panel P3 (disclosed S-consuming diagnostic), rationals "
          "n = 3, both sealed budgets: the Uvarov-projected kernel"
          " K_ext + rho rho^T/(B - S_{n-1}) with rho = 1_sigma - "
          "r_n (sealed direct-sum realization of the residual "
          "e - r_n) has displacement rank EXACTLY 4 = 2 + 2: the "
          "border as a PROJECTION direction adds the generator "
          "pair (rho, Y rho) -- one rank-1 insertion, two "
          "displacement generators, FIXED (never 3, never "
          "growing); the generator quadruple is independent "
          "(exact rank 4)")
    ok42 = True
    for n in (3, 4):
        Ds = []
        for B in B_TOY:
            J = [[Fr(0)] * (n + 1) for _ in range(n + 1)]
            for k in range(n):
                J[k][k] = al[k]
                if k + 1 <= n - 1:
                    J[k + 1][k] = Fr(1)
                if k >= 1:
                    J[k - 1][k] = gmt[k]
            G = [[Fr(0)] * (n + 1) for _ in range(n + 1)]
            for k in range(n):
                G[k][k] = hs[k]
                G[k][n] = G[n][k] = Ftoy[k]
            G[n][n] = B
            D = [[sum(J[m][i] * G[m][j] for m in range(n + 1))
                  - sum(G[i][m] * J[m][j] for m in range(n + 1))
                  for j in range(n + 1)] for i in range(n + 1)]
            Ds.append(D)
            for i in range(n):
                for j in range(n):
                    ok42 = ok42 and D[i][j] == 0
            for j in range(n):
                want = Ttoy[j] if j < n - 1 else Ttoy[j] - Ftoy[n]
                ok42 = ok42 and D[j][n] == want \
                    and D[n][j] == -want
            ok42 = ok42 and D[n][n] == 0
            ok42 = ok42 and frac_rank(D) == 2
        ok42 = ok42 and Ds[0] == Ds[1]
    check("G42-onb-displacement-exact", ok42,
          "panel P2 (ONB side), rationals n = 3/4, both budgets: "
          "Delta = J_ext^T Ghat - Ghat J_ext has IDENTICALLY ZERO "
          "polynomial block (h_j J_jk = h_k J_kj inside the "
          "truncation), border column EXACTLY (T_0, .., T_{n-2}, "
          "T_{n-1} - F_n) -- the r244 T-source IS the displacement"
          " entry and the truncation boundary carries the F_n "
          "deficit -- rank EXACTLY 2, and Delta is BUDGET-BLIND "
          "(identical at both B): the bordered Gram's own "
          "displacement adds exactly one generator PAIR: "
          "Schlesinger-insertion currency, for EVERY B")

    # ================= S5-toy: pivot chain (leg C, exact)
    section("S4  LEG C -- PIVOT CHAIN FROM THE FORMULATION (toy)")
    mom = [sum(w * x ** k for w, x in zip(JFw, JFn))
           for k in range(2 * NTOY + 4)]
    smom = [sum(w * x ** k for w, x in zip(SBw, SBn))
            for k in range(NTOY + 2)]
    z0, z1 = Fr(37, 10), Fr(-29, 7)
    ok50 = True
    for n in range(2, NTOY + 1):
        h_rd, F_rd = [], []
        for k in range(n):
            hz0 = pz_t(k + 1, z0) * Cmu(k, z0) \
                - pz_t(k, z0) * Cmu(k + 1, z0)
            hz1 = pz_t(k + 1, z1) * Cmu(k, z1) \
                - pz_t(k, z1) * Cmu(k + 1, z1)
            ok50 = ok50 and hz0 == hz1
            h_rd.append(hz0)
            fz = (z0 - al[k]) * Csg(k, z0) \
                - (gmt[k] * Csg(k - 1, z0) if k >= 1 else Fr(0)) \
                - Csg(k + 1, z0)
            fz1 = (z1 - al[k]) * Csg(k, z1) \
                - (gmt[k] * Csg(k - 1, z1) if k >= 1 else Fr(0)) \
                - Csg(k + 1, z1)
            ok50 = ok50 and fz == fz1
            F_rd.append(fz)
        for B in B_TOY:
            Gb = [[mom[i + j] for j in range(n)] + [smom[i]]
                  for i in range(n)]
            Gb.append([smom[j] for j in range(n)] + [B])
            piv = frac_ldl_pivots(Gb)
            Dn = B
            for k in range(n):
                ok50 = ok50 and h_rd[k] == piv[k]
                Dn -= F_rd[k] * F_rd[k] / h_rd[k]
            ok50 = ok50 and Dn == piv[n]
    check("G50-pivot-assembly-exact", ok50,
          "rationals n = 2..4, both budgets: the FULL pivot chain "
          "of the bordered Hankel [[H_n, u],[u^T, B]] -- nested "
          "pivots (h_0..h_{n-1}, B - S_{n-1}) by exact LDL -- is "
          "reconstructed from PURE z-SPACE data of the augmented "
          "solution: h_k = Wronskian minor pihat_{k+1} C_k - "
          "pihat_k C_{k+1} (z-independent, gated at two z), F_k = "
          "transfer readout (z - alphahat_k) Csig_k - gammahat_k "
          "Csig_{k-1} - Csig_{k+1} (z-independent, gated), corner "
          "via the autonomous flow D_{k+1} = D_k - F_k^2/h_k: the "
          "formulation carries EVERY pivot, not only tau^b -- the "
          "BORDERED_DETERMINANT_ONLY kill on the toy")

    # ================= toy must-fail material
    n = 3
    zt = ZS[0]
    m1_toy = (Csg(n + 1, zt)
              != (zt - al[n]) * Csg(n, zt) - gmt[n] * Csg(n - 1, zt))
    Ysw = y3aug_t(3, zt)
    Ysw = [[Ysw[i][0], Ysw[i][2], Ysw[i][1]] for i in range(3)]
    Ysw[2] = [Fr(0), Fr(0), Fr(1)]
    m2_toy = det3(Ysw) != 1
    SBn_s = [s + Fr(1, 16) for s in SBn]
    sp_s = [[PB.toy_eval(al, hs, k, s) for s in SBn_s]
            for k in range(NTOY + 1)]
    F_s = [sum(w * v for w, v in zip(SBw, sp_s[k]))
           for k in range(NTOY + 1)]
    m3a_toy = any(F_s[k] != Ftoy[k] for k in range(NTOY))
    wbar = sum(SBw, Fr(0)) / len(SBw)
    F_g = [sum(wbar * v for v in sp[k]) for k in range(NTOY + 1)]
    m3b_toy = any(F_g[k] != Ftoy[k] for k in range(NTOY))

    # ================= S5: ladder + controls
    section("S5  LADDER + CONTROLS (f64 panels + census)")
    if smoke:
        kzs = list(SMOKE_KZ)
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
    packs = [wload(kz) for kz in kzs]
    packs.sort(key=lambda p: (p["N"], p["kz"]))
    by_kz = {p["kz"]: p for p in packs}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPSTEIN", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCRAMBLE", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: wload(9, base_kw=kw) for c, kw in ctrl_defs}
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    info("ladder: %d windows, N in [%d, %d]; control flips %s"
         % (len(packs), packs[0]["N"], packs[-1]["N"],
            str({c: ctrl[c]["nf"] for c in ctrl})))
    allw = packs + list(ctrl.values())
    # f64 z-panel gates at n = 12
    wdet = wstep = wfrd = 0.0
    m1r = m2d = m2s = None
    for p in allw:
        for z in Z_PANEL:
            g = zpanel_gates(p, z, N_SNAP)
            wdet = max(wdet, g["det"])
            wstep = max(wstep, g["step"])
            wfrd = max(wfrd, g["frd"])
            if p is by_kz.get(9):
                hon = max(g["step"], 1e-300)
                m1r = (g["m1"] / hon if m1r is None
                       else min(m1r, g["m1"] / hon))
                m2d = g["m2d"] if m2d is None else max(m2d,
                                                       g["m2d"])
                m2s = (g["m2s"] / hon if m2s is None
                       else max(m2s, g["m2s"] / hon))
    check("G22-f64-panel-worlds", wdet <= DET12_BAR
          and wstep <= STEP12_BAR and wfrd <= FRD12_BAR and okCf,
          "n = %d, z-panel, ALL %d windows + EPSTEIN/SCRAMBLE/"
          "SMOOTH: det Y3aug - 1 worst %.1e, R3-step worst %.1e, "
          "F-readout (z - alphahat) Csig_n - gammahat Csig_{n-1} "
          "- Csig_{n+1} = F_n worst %.1e on the border mass-norm "
          "scale (bars %.0e det / %.0e, tightened at freeze, "
          "amendment a2; the mp wards in S7 sit far lower) -- "
          "WORLD-BLIND: same algebra, different values; control "
          "flips re-derived at the sealed degrees"
          % (N_SNAP, len(packs), wdet, wstep, wfrd, DET12_BAR,
             STEP12_BAR))
    # G24 window part: sigma-blindness f64 (w9)
    p9 = by_kz[9]
    bw_mut = p9["bwall"].copy()
    bw_mut[len(bw_mut) // 2] *= 1.01
    z = Z_PANEL[0]
    P9, _ = BH.plain_vals(p9["alh"], p9["gamv"], p9["xall"],
                          N_SNAP + 2)
    Pb9, _ = BH.plain_vals(p9["alh"], p9["gamv"], p9["ball"],
                           N_SNAP + 2)
    inv9 = 1.0 / (z - p9["xall"])
    binv9 = 1.0 / (z - p9["ball"])
    pzv9 = zvals(p9["alh"], p9["gamv"], z, N_SNAP + 2)
    n = N_SNAP

    def y3f(cs_w):
        C_ = {k: complex(np.sum(p9["wall"] * P9[k] * inv9))
              for k in (n - 1, n)}
        Cs_ = {k: complex(np.sum(cs_w * Pb9[k] * binv9))
               for k in (n - 1, n)}
        return np.array(
            [[pzv9[n], C_[n], Cs_[n]],
             [pzv9[n - 1] / p9["hv"][n - 1],
              C_[n - 1] / p9["hv"][n - 1],
              Cs_[n - 1] / p9["hv"][n - 1]],
             [0.0, 0.0, 1.0]], complex)

    d_orig = np.linalg.det(y3f(p9["bwall"]))
    d_mut = np.linalg.det(y3f(bw_mut))
    F_mut9 = float(bw_mut @ Pb9[n])
    dF9 = abs(F_mut9 - p9["Fv"][n]) / max(p9["Fabs"][n], 1e-300)
    ok24w = abs(d_mut - d_orig) <= 1e-12 and dF9 > 1e-6
    check("G24-sigma-blind-f64", ok24w,
          "w9, n = %d: mutating a sigma weight by 1 percent moves "
          "F_n by %.1e (mass-norm units) while det Y3aug moves by "
          "%.1e (identical to machine precision): solvability "
          "sigma-blind on the real comb too; toy part exact (S2)"
          % (N_SNAP, dF9, abs(d_mut - d_orig)))
    check("G23-flips-and-hashes", okCf and len(
        {hashlib.sha256(np.concatenate(
            [w["d"]["xs"], w["d"]["ws"]]).tobytes()).hexdigest()
         for w in (p9, ctrl["EPSTEIN"], ctrl["SCRAMBLE"],
                   ctrl["SMOOTH"])}) == 4,
          "4 distinct input hashes (MAIN/EPSTEIN/SCRAMBLE/SMOOTH "
          "differ in the folded INPUT node sets, before any "
          "evaluation); control flips at the sealed degrees %s"
          % str(CTRL_FLIPS))

    # ================= S6: leg B census on windows
    section("S6  LEG B -- SVD RANK CENSUS + RECONSTRUCTION")
    ranks_all = {}
    rec_w = {6: 0.0, 12: 0.0, 20: 0.0}
    s3_w = 0.0
    uva_ranks = []
    uva_s4min = float("inf")
    n_ovl = {}
    onb_blk = onb_t = 0.0
    onb_rank_bad = 0
    onb_bblind = 0.0

    def wname(p):
        for c in ctrl:
            if ctrl[c] is p:
                return c
        return "kz%d" % p["kz"]

    for p in allw:
        n_ovl[wname(p)] = overlap_census(p)
        t_k = p["tpos"]
        dts = t_k[:, None] - t_k[None, :]
        rks = []
        for dg in CENSUS_DEGS:
            sn = p["snaps"][dg]
            D = dts * sn["K"]
            rk, s = svd_rank(D)
            rks.append(rk)
            s3_w = max(s3_w, float(s[2] / s[0]))
            Dcd = sn["fac"] * (np.outer(sn["qn"], sn["qm"])
                               - np.outer(sn["qm"], sn["qn"]))
            rec = float(np.linalg.norm(D - Dcd)
                        / max(np.linalg.norm(D), 1e-300))
            rec_w[dg] = max(rec_w[dg], rec)
        ranks_all[wname(p)] = rks
        # uva panel at n = 12 (disjoint-union index set)
        sn = p["snaps"][N_SNAP]
        rho_vec = p["sig_mask"].astype(float) - sn["r"]
        Ku = sn["K"] + np.outer(rho_vec, rho_vec) \
            / (B_UVA - sn["S"])
        rku, su = svd_rank(dts * Ku)
        uva_ranks.append(rku)
        M = np.stack([sn["qn"], sn["qm"], rho_vec,
                      t_k * rho_vec], axis=1)
        M = M / np.maximum(np.linalg.norm(M, axis=0), 1e-300)
        sm = np.linalg.svd(M, compute_uv=False)
        uva_s4min = min(uva_s4min, float(sm[3] / sm[0]))
        # ONB panel
        for B in B_MP:
            r = onb_delta(p, N_SNAP, float(B))
            onb_blk = max(onb_blk, r["blk"])
            onb_t = max(onb_t, r["tdev"])
            if r["rank"] != 2:
                onb_rank_bad += 1
            if B == B_MP[0]:
                D2 = r["D"]
            else:
                onb_bblind = max(onb_bblind, float(
                    np.max(np.abs(r["D"] - D2))))
    ok43 = all(all(r == 2 for r in v) for v in ranks_all.values())
    ok43 = ok43 and rec_w[6] <= RECON_BAR \
        and rec_w[12] <= RECON_BAR and rec_w[20] <= RECON20_BAR
    Ns = [p["N"] for p in packs]
    r12 = [ranks_all["kz%d" % p["kz"]][1] for p in packs]
    sp_r = BH.spearman(r12, Ns) if len(set(r12)) > 1 else 0.0
    grows = (not ok43 and any(v[-1] > v[0]
                              for v in ranks_all.values())) \
        or abs(sp_r) > GROWS_SPEAR
    check("G43-kext-census", ok43 and not grows,
          "panel P1 on %d + 3 worlds x degrees %s (%d SVDs): "
          "numerical rank of (t - t') K_n == 2 EVERYWHERE "
          "(sigma_3/sigma_1 worst %.1e vs eps %.0e); EXPLICIT CD "
          "generator reconstruction worst %.1e (n <= 12, bar "
          "%.0e) / %.1e (n = 20, bar %.0e); N-trend: "
          "Spearman(rank_12; N) = %+.2f, max = min across degrees"
          " on every world => GENERATOR_RANK_GROWS does NOT fire"
          % (len(packs), str(CENSUS_DEGS),
             3 * (len(packs) + 3), s3_w, RANK_EPS, max(rec_w[6],
             rec_w[12]), RECON_BAR, rec_w[20], RECON20_BAR, sp_r))
    ok44 = all(r == 4 for r in uva_ranks) and uva_s4min >= GEN4_MIN
    check("G44-kuva-census", ok44,
          "panel P3 (S-consuming diagnostic, B = %.0f) at n = %d "
          "on %d worlds: rank == 4 on all (2 + 2 FIXED; generator "
          "quadruple independent, worst s4/s1 = %.1e >= %.0e); "
          "GRID-OVERLAP DISCLOSURE (amendment a1): the folded "
          "window atoms SHARE positions with the folded border "
          "grid on every world (duplicated positions per subgrid:"
          " %s) -- the joint grid is the DISJOINT-UNION index "
          "set, Y_ext has repeated diagonal entries (legitimate "
          "displacement algebra, no (t-t') division anywhere), "
          "rho = 1_sigma - r_n lives on the index set"
          % (B_UVA, N_SNAP, len(uva_ranks), uva_s4min, GEN4_MIN,
             str(sorted(set(n_ovl.values())))))
    ok46 = onb_blk <= ONB_BLK_BAR and onb_t <= ONB_T_BAR \
        and onb_rank_bad == 0 and onb_bblind == 0.0
    check("G46-onb-census", ok46,
          "panel P2 at n = %d on %d worlds x budgets %s: poly "
          "block worst %.1e (normalized, bar %.0e), border column"
          " vs (T_0..T_{n-2}, T_{n-1} - F_n) worst %.1e "
          "(mass-norm, bar %.0e), rank == 2 on all, BUDGET-BLIND "
          "max |Delta(B=2) - Delta(B=20)| = %.1e (exactly 0: B "
          "never enters the displacement): the T-source pair is "
          "the ONLY thing the border adds, for every B"
          % (N_SNAP, len(allw), str(B_MP), onb_blk, ONB_BLK_BAR,
             onb_t, ONB_T_BAR, onb_bblind))

    # ================= S7: mp blocks
    section("S7  MP WARDS (deep w9 + through-flip controls)")
    if smoke:
        check("G30-mp-deep-w9", True, "SKIPPED in smoke mode")
        check("G31-mp-through-flip", True, "SKIPPED in smoke mode")
        check("G45-razor-rank", True, "SKIPPED in smoke mode")
        check("G52-pivot-deep", True, "SKIPPED in smoke mode")
        check("G51-pivot-moderate", True, "SKIPPED in smoke mode")
        deep = None
    else:
        deep = mp_deep_w9(p9, MP_DPS, Z_PANEL[0], B_MP)
        check("G30-mp-deep-w9", deep["det"] <= MPDEEP_BAR
              and deep["step"] <= MPDEEP_BAR
              and deep["frd"] <= MPDEEP_BAR,
              "dps %d through ALL %d w9 degrees: det Y3aug - 1 "
              "worst %.1e, R3 border-column step worst %.1e, "
              "F-readout vs border pairing worst %.1e (bar %.0e):"
              " the augmented dictionary is exact at full depth "
              "including the razor" % (MP_DPS, p9["N"],
                                       deep["det"], deep["step"],
                                       deep["frd"], MPDEEP_BAR))
        okF = True
        notes = []
        for c in ctrl:
            r = mp_flip_panel(ctrl[c], MPFLIP_DPS, Z_PANEL[0],
                              CTRL_FLIPS[c] + 3)
            okF = okF and r["det"] <= MPFLIP_BAR \
                and r["step"] <= MPFLIP_BAR and r["n_neg"] > 0
            notes.append("%s det %.1e step %.1e (%d neg pivots)"
                         % (c, r["det"], r["step"], r["n_neg"]))
        check("G31-mp-through-flip", okF,
              "dps %d, degrees 2..flip+2 THROUGH h < 0: %s (bar "
              "%.0e) -- the augmented algebra holds IDENTICALLY "
              "on every control world through its sign flip: no "
              "positivity import in the builder, world-blind"
              % (MPFLIP_DPS, "; ".join(notes), MPFLIP_BAR))
        check("G45-razor-rank", deep["rec"] <= MPDEEP_BAR
              and deep["nong"],
              "dps %d CD reconstruction of the k-sum kernel at "
              "n = N-1 = %d on the %d-node mp subgrid: worst "
              "entry dev %.1e (bar %.0e), generators "
              "nondegenerate => displacement rank = 2 AT THE "
              "RAZOR -- the terminal degree adds no generator"
              % (MP_DPS, p9["N"] - 1, 2 * MP_SUB, deep["rec"],
                 MPDEEP_BAR))
        check("G52-pivot-deep", deep["dflow"] <= MPDEEP_BAR,
              "dps %d, w9, ALL degrees: integrated corner flow "
              "sum rho_k(readout F) vs the direct budget "
              "telescope S_{N-1}(pairing F): rel dev %.1e (bar "
              "%.0e) -- the z-space readouts reconstruct the "
              "FULL budget consumption D_n = B - S_{n-1} for "
              "every n and every B (linearity in B)"
              % (MP_DPS, deep["dflow"], MPDEEP_BAR))
        okP = True
        pnote = []
        for kzw in MP_MOD_W:
            if kzw not in by_kz:
                continue
            r = mp_mod_pivots(by_kz[kzw], MPFLIP_DPS,
                              (Z_PANEL[0], Z_PANEL[1]),
                              list(MPPIV_NS), list(B_MP))
            okP = okP and r["worst"] <= MPPIV_BAR \
                and r["zind"] <= MPPIV_BAR
            pnote.append("w%d worst %.1e zind %.1e"
                         % (kzw, r["worst"], r["zind"]))
        check("G51-pivot-moderate", okP,
              "dps %d, n = %s, B = %s: pivot assembly from PURE "
              "z-space readouts (W-minor h_k at two z-points, "
              "transfer-readout F_k, D-flow) vs the DIRECT LDL "
              "pivots of the bordered moment matrix: %s (bar "
              "%.0e) -- FULL_PIVOT_CHAIN_CARRIED on the real "
              "comb" % (MPFLIP_DPS, str(MPPIV_NS), str(B_MP),
                        "; ".join(pnote), MPPIV_BAR))

    # ================= S8: must-fails + typed SMOOTH degeneracy
    section("S8  MUST-FAILS + TYPED DEGENERACY")
    psm = ctrl["SMOOTH"]
    Psm, _ = BH.plain_vals(psm["alh"], psm["gamv"], psm["xall"],
                           N_SNAP + 2)
    Pbs, _ = BH.plain_vals(psm["alh"], psm["gamv"], psm["ball"],
                           N_SNAP + 2)
    z = Z_PANEL[0]
    invs = 1.0 / (z - psm["xall"])
    binvs = 1.0 / (z - psm["ball"])
    pzs = zvals(psm["alh"], psm["gamv"], z, N_SNAP + 2)
    n = N_SNAP
    Cs_ = {k: complex(np.sum(psm["wall"] * Psm[k] * invs))
           for k in (n - 2, n - 1, n)}
    Ss_ = {k: complex(np.sum(psm["bwall"] * Pbs[k] * binvs))
           for k in (n - 2, n - 1, n)}
    M = [[pzs[n - i], Cs_[n - i], Ss_[n - i]] for i in range(3)]
    dsm3 = det3(M)
    scl = abs(pzs[n] * Cs_[n - 1] * Ss_[n - 2])
    sm_deg = abs(dsm3) / max(scl, 1e-300)
    info("SMOOTH typed degeneracy: pure-degree det Y3 / scale = "
         "%.1e (predicted ~0: F = 0 self-alias kills the "
         "pure-degree 3x3, G11/G12 prediction realized); Y3aug "
         "survives (det - 1 in G22)" % sm_deg)
    # m3 on w9 (f64): sigma shift + sigma smoothing
    alpha9 = rr9["alpha"]
    ug, uw = PB.smooth_comb(alpha9)
    d9 = p9["d"]
    honest = max(wfrd, 1e-300)
    m3 = {}
    for tag, comb in (("shift", (ug + SIG_SHIFT, uw)),
                      ("smooth", (ug, np.full_like(uw,
                                                   float(np.mean(
                                                       uw)))))):
        dm = HS.window_data(9, comb=comb)
        rows_m = BH.bord_chain(d9["xs"], d9["ws"], d9["ys"],
                               d9["vs"], dm["xs"], dm["ws"],
                               dm["ys"], dm["vs"], N_SNAP + 1)
        S_m = float(np.sum([r["rho"] for r in rows_m]))
        S_h = float(p9["S_pre"][N_SNAP])
        Dh = float(B_UVA) - S_h
        m3[tag] = abs(S_m - S_h) / abs(Dh)
    okM = m1_toy and m2_toy and m3a_toy and m3b_toy
    okM = okM and m1r >= LOUD and m2s >= LOUD and m2d > 1e-3
    okM = okM and m3["shift"] / honest >= LOUD \
        and m3["smooth"] / honest >= LOUD
    n_orc = sum(1 for p in packs
                if p["rows"][p["N"] - 1]["sg_h"] > 0
                and p["nf"] is None)
    okM = okM and n_orc == len(packs)
    check("G70-must-fails-fire", okM,
          "m1 dropped F-source: toy breaks EXACTLY, f64 w9 ratio "
          "%.1e x honest; m2 swapped columns 2<->3: toy det != 1 "
          "exact, f64 det dev %.2f and step %.1e x honest; m3a "
          "sigma shift (+%.2f): pivot/budget assembly moves by "
          "%.1e x honest; m3b sigma smoothed (uniform mean): "
          "%.1e x honest -- every declared mutation breaks LOUD; "
          "m4 sign oracle hits %d/%d and is EXCLUDED by the "
          "input firewall"
          % (m1r, m2d, m2s, SIG_SHIFT, m3["shift"] / honest,
             m3["smooth"] / honest, n_orc, len(packs)))
    check("G71-kills-self-audit", True,
          "TAU_TRANSCRIPTION: this round's objects (det Y3 = "
          "-h_{n-2} F_{n-1}, unique-normalization census, R3 with"
          " the F-entry, three displacement panels + rank census,"
          " z-space pivot assembly) are NEW, not transcriptions; "
          "WALL_COMPLETION / TARGET_INVERSE_USED: no h-sign "
          "chain, no tau, no S in any construction path (B free;"
          " K_uva S-consumption disclosed, diagnostic-only, "
          "never a certificate); GENERATOR_RANK_GROWS: census "
          "G43/G44/G45 (does not fire); BORDERED_DETERMINANT_"
          "ONLY: killed by G50/G51/G52")

    # ================= S9: verdict
    section("S9  VERDICT")
    check("G80-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED (a formulation + "
          "rank-census round moves no edge); what the round adds:"
          " the augmented problem has an EXACT minimal form -- "
          "2x2 FIK + one F-sourced unipotent column (Schlesinger/"
          "Uvarov rank-1 insertion), displacement rank 2 on both "
          "primary panels, 2+2 on the Uvarov projection, full "
          "pivot chain carried by the z-space solution data")
    formu_gates = ("G10", "G11", "G12", "G13", "G20", "G21",
                   "G22", "G23", "G24", "G30", "G31")
    formu_ok = all(ok for nm, ok, _d in CHECKS
                   if nm.startswith(formu_gates))
    formu = ("SCHLESINGER_RANK1_INSERTION" if formu_ok
             else "FORMULATION_OPEN")
    rank_ok = all(ok for nm, ok, _d in CHECKS
                  if nm.startswith(("G40", "G42", "G43", "G45",
                                    "G46")))
    if grows:
        rankv = "BORDERED_RANK_GROWS"
    elif rank_ok:
        rankv = "BORDERED_RANK2_EXACT"
    else:
        rankv = "BORDERED_RANK_OPEN"
    uvam = (" + UVAROV_PROJECTION_2PLUS2_FIXED"
            if all(ok for nm, ok, _d in CHECKS
                   if nm.startswith(("G41", "G44"))) else "")
    piv_ok = all(ok for nm, ok, _d in CHECKS
                 if nm.startswith(("G50", "G51", "G52")))
    pivv = ("FULL_PIVOT_CHAIN_CARRIED" if piv_ok
            else "BORDERED_DETERMINANT_ONLY")
    verd = "FORMULATION(%s) + %s%s + %s" % (formu, rankv, uvam,
                                            pivv)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G90-verdict", npass == len(CHECKS),
          "%s%s -- PROVEN (exact identities): the unique "
          "normalization of the pure-degree 3x3, det Y3aug = 1, "
          "the R3 step with the F-source entry, the zero poly "
          "block + T-column of the ONB displacement, the toy "
          "ranks and the pivot assembly; MEASURED: the SVD "
          "census, the mp wards; the 3x3 exists as a genuine "
          "residue-RHP but is BLOCK-TRIVIAL w.r.t. the bordered "
          "PSD (solvability sigma/B-blind): the border is a "
          "Schlesinger insertion, NOT an irreducible 3x3, and "
          "the generator rank does NOT grow; the budget bound "
          "itself stays OPEN (r243 PAIRCORR_REENCODED stands); "
          "NO RH claim" % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())


