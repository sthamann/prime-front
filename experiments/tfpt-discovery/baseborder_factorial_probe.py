#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""baseborder_factorial_probe -- PRIME.PORT.FIBER.BASEBORDER.
FACTORIAL.01 (round 256): the CAUSAL base/border separation of the
two-stage fiber coupling T = <sigma0, G_N[mutilde] sigma0> (base
source -> kernel -> border source) BEFORE any further compression
search.  r254 measured the 2x2 MAIN x SCRAMBLE cross table on the
union grid WITHOUT a positivity firewall: T_MM +4.3343, T_MS
+9.9756, T_SM -0.9276, T_SS -4.4941, i.e. Delta_base +5.26,
Delta_border -5.64, Delta_int -9.21 (identity T_MM - T_SS =
Delta_base + Delta_border - Delta_int = 8.83 exact).  THE REVIEWER
CORE THEOREM (load-bearing for every fiber claim): while the base
is positive (h_k > 0 for 8 <= k < n) the kernel G_n = K_n - K_8 =
sum_{k=8}^{n-1} pihat_k(x) pihat_k(y) / h_k is PSD, hence T >= 0
for EVERY real border measure -- a negative T can ONLY arise from
kernel change, base indefiniteness, or mixed interaction, NEVER
from pure border permutation under a fixed positive kernel.  THIS
round (i) types every cell by that firewall, (ii) re-runs the
factorial on the COMMON POSITIVE PREFIX n* (where no kernel is
indefinite and the three effects are causally clean), (iii)
adjudicates sealed dominance verdicts, and (iv) re-adjudicates the
r254 headline (SCRAMBLE spectrally compact, K80_own = 2) as
possible BASE CONTAMINATION by the negative h-modes.

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r254 discipline): w = window (kz),
N_w = builder depth, n/k = chain degree; free pivots h_{w,k}
(k < N_w) are the proof objects and legitimate KERNEL inputs; the
forced pivot h_N is NEVER formed -- the phat recursion (imported
VERBATIM from r254 OG.phat_matrix) consumes alh_k (k <= N-2) and
gam_{k+1} = rows[k]["gam_next"] (k <= N-2) ONLY.  sigma0 = sigma -
(F_0/h_0) mutilde (r248).  Ground truth (T_true = St - S_7, flip
degrees, partial sums S_{n-1} - S_7) enters GATES only.  No
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r244 BH.wpack (rho/S/chain bitwise), r254
OG.world_build + OG.phat_matrix + OG.eig_block + OG.profile_stats
+ the r254-a1 SORTED-UNION embedding convention (adopted, not
re-derived: its admission gate -- border bitwise identical, every
world's window positions bitwise found in the union -- failed
LOUDLY on the raw concat order in r254 and is re-gated here),
r243 PB.smooth_comb, v881 PIK.lambda_eps controls.

LEG 0 -- POSITIVE-PREFIX FIREWALL (mandatory before everything):
per base world mu in {MAIN, SCRAMBLE, EPSTEIN, SMOOTH} the maximal
positive prefix degree pmax(mu) = first k in [8, N) with h_k < 0
(else N); T_n[mu, sigma] is typed POSITIVE_PREFIX iff n <=
pmax(mu) (all h_k > 0 for 8 <= k < n => G_n PSD => genuine
Hilbert-space interpretation, independent fiber falsifier) else
INDEFINITE_CONTINUATION (algebraically legitimate as a
tau-quotient object, NOT an independent fiber falsifier).  PSD
verification gate per world: lambda_min(G_pmax) on the own grid
>= -1e-10 x max(lambda_max, 1).

LEG A -- THE EXACT 2x2 WORLD CENSUS (MAIN x C for C in SCRAMBLE,
EPSTEIN, SMOOTH; base world fixes chain + kernel, border world
fixes sigma0; r254-a1 union embedding): cells T[W, sW'] = s_{W'}^T
G_W s_{W'}; effects Delta_base = T_MM - T_CM, Delta_border = T_MM
- T_MC, Delta_int = T_MM - T_MC - T_CM + T_CC; identity ward
Delta_base + Delta_border - Delta_int = T_MM - T_CC (rel 1e-12 of
the cell scale; it guards the EFFECT FORMULAS, and its must-fail
is a wrong-formula test, disclosed in leg E).  r254 PRIOR
verification (rel 2e-3): SCR cells +4.3343/+9.9756/-0.9276/
-4.4941; EPST cells T[M,sE] +12.3502, T[E,sM] -0.8561, T_EE
+0.7615.  FIREWALL-CLEANED RASTER: all four cells rebuilt with
BOTH kernels truncated at the common positive prefix n* =
min(pmax(M), pmax(C)) -- only there is the decomposition causally
clean (no kernel indefinite; every cell must be >= -1e-9 x gross).
Chain wards: diagonal cells at n* vs the bitwise partial sums
S_{n*-1} - S_7 (rel 1e-9 MAIN / 1e-4 controls / abs on SMOOTH).

SEALED ADJUDICATION (frozen BEFORE evaluation; MAIN x SCRAMBLE):
dominance factor DOM = 3; basis = the CLEANED raster (the causal
one); the raw full-depth Delta_border (MAIN kernel PSD at full
depth, hence also clean) enters the LOAD_BEARING rule as a second
mandatory condition.  Priority order:
  (1) BASE_KERNEL_ROTATION_DOMINATES  iff |Db*| >= 3 max(|Dbo*|,
      |Di*|)   => base and fiber not separable, vote COUPLEDTAU;
  (2) MIXED_INTERACTION_DOMINATES     iff |Di*| >= 3 max(|Db*|,
      |Dbo*|)  => the arithmetic lives in the nonlinear
      compatibility, vote tau^aug/tau as one indivisible
      full-source object;
  (3) BORDER_PAIRING_LOAD_BEARING     iff sign(Dbo) == sign(Gap)
      AND |Dbo|/|Gap| in [0.3, 3.0] on BOTH the raw full-depth
      MAIN-kernel border effect AND the cleaned-prefix border
      effect -- the sealed answer to the r254 prior (-5.64 vs Gap
      +8.83): a border move that OVERSHOOTS WITH THE WRONG SIGN
      does NOT count as load-bearing; only this verdict unlocks
      legs B-D;
  (4) EFFECTS_MIXED_COUPLEDTAU        (residual; also fired with
      note CLEANED_GAP_NULL if |Gap*| <= 1e-9 x gross).
CONTROL ADJUDICATION (EPSTEIN): CONTROL_FIBER_IS_BASE_
CONTAMINATION iff |Gap*| <= 0.2 x |Gap_raw| (the anomaly is
carried >= 80 percent by the indefinite continuation degrees) OR
|Dbo*| <= 0.1 x max(|Gap*|, 1e-12) (the border move contributes
nothing once both kernels are positive: the anomaly follows the
base choice entirely) -- then the EPSTEIN fiber anomaly may no
longer be cited as a fiber falsifier; else EPSTEIN_ANOMALY_
SURVIVES_PREFIX.  SMOOTH is the sealed NULL ANCHOR (sigma0 == 0):
its border cells must vanish (|T| <= 1e-9 x gross), its raster is
printed INFO, not adjudicated.

LEG A2 -- INVERSION ADJUDICATION (is the r254 SCRAMBLE compactness
K80_own = 2 carried by the NEGATIVE h-modes?): on the SCRAMBLE own
grid split G_SCR = G_pos + G_neg by the sign of h_k (mode split,
exact: |T_pos + T_neg - T_SS| <= 1e-9 x gross; T_pos >= -1e-9 x
gross by PSD of the positive part); reproduce K80_own(SCR) = 2
(r254 prior, |c|-sorted, tol 0.2); for the top-2 |c|-eigenpairs of
G_SCR measure f_neg = ||Q_neg^T v||^2 with Q_neg an orthonormal
basis (SVD, 1e-10 rel cut) of span{phat_k rows, h_k < 0} in atom
space.  SEALED: INVERSION_IS_BASE_CONTAMINATION iff mean f_neg
(top-2) >= 0.8 (the r254 headline 'surgery concentrates the form
onto ~2 eigendirections' is then a statement about the indefinite
base modes, not about a border discriminator -- downgraded);
INVERSION_GENUINE_FIND iff <= 0.2; else INVERSION_MIXED.

LEGS B-D (CONDITIONAL: run iff BORDER_PAIRING_LOAD_BEARING fires
by the sealed rule; else explicitly SKIPPED, their gates then do
not count) -- on the FIXED positive full-depth MAIN kernel, border
route s_b (r248 centering invariance, re-gated):
(B) EXCHANGE SWEEP over all admissible ADJACENT swaps (consecutive
  pairs of the position-sorted border block, d = s_i - s_j != 0):
  Delta T from the exact exchange formula (leg E gates its
  exactness unconditionally); EXCHANGE_MONOTONE_GO iff >= 0.99 of
  the nonzero Delta T share one sign (rearrangement/total-
  positivity characterization of the true pairing as an extremal
  assignment becomes reachable); EXCHANGE_SIGN_MIXED else (with
  the fraction printed).
(C) MONGE/TP TEST: four-point defects M_{i,i+1;k,k+1} = G_ik +
  G_jl - G_il - G_jk on the position-sorted border nodes, all
  ordered adjacent quadruples i < k: dominant-sign fraction >=
  0.99 => MONGE_TP_ORDER (theorematic closure of the exchange
  formula); < 0.90 => NO_EXCHANGE_ORDER (ends the class); else
  WEAK_ORDER.
(D) SOURCE-PURE SPECTRAL COMPRESSION: eigendirections of G_MAIN
  ordered by |lambda| DESCENDING (defined BEFORE any border
  readout -- no subspace choice after seeing sigma or the gap);
  K90/K99/K99.9 = first K with |cum c / T - 1| <= 0.1/0.01/0.001;
  FIXED_SPECTRAL_CARRIER iff K90 <= 10; LOG_SPECTRAL_CARRIER iff
  K90 <= 4 ln(N - 8); else EXTENSIVE_SPECTRAL_CARRIER.
DIAGNOSTIC (not proof-registered, appendix only): dyadic band
|C|-profiles in |u_i - u_j| for MAIN and SCRAMBLE (r254
band_stats, INFO lines only).

LEG E -- FALSIFIERS + MUST-FAILS (each loud, chain-predicted):
(e0) EXCHANGE FORMULA EXACT (unconditional, MAIN border route):
  T(sigma') - T(sigma) = 2 d [(G sigma)_j - (G sigma)_i] + d^2
  (G_ii + G_jj - 2 G_ij), d = sigma_i - sigma_j, verified against
  the direct re-evaluation on 64 evenly sampled adjacent swaps
  (bar 1e-10 x gross);
(mA) FIREWALL OMITTED (the explicit alias test): without leg 0
  the T_SM < 0 cell would be labeled a border effect; the alias
  dies because (i) lambda_min(G_SCR full) < 0 loudly (>= 1e3 x
  1e-13 x max(lambda_max, 1)), (ii) the positive-mode part obeys
  the PSD theorem s_M^T G_SCR_pos s_M >= -1e-9 x gross, (iii) the
  ENTIRE negativity sits in the h_k < 0 modes (T_SM_neg < 0,
  loud, mode split exact to 1e-9 x gross) -- kernel property, not
  border property;
(mW) EFFECT FORMULA BROKEN: Delta_int computed with the flipped
  CC sign must break the identity ward by exactly 2 |T_CC| (rel
  1e-9, loudness 1e3 x max(honest ward, 1e-13) x scale);
(mX) EXCHANGE FORMULA WRONG CROSS TERM (+2 G_ij instead of
  -2 G_ij) on the adjacent swap maximizing |4 d^2 G_ij|: must
  deviate from the direct route by >= 1e3 x max(honest worst
  deviation, 1e-13 x gross).

SEALED CONSTANTS: window w9; controls on w9: EPSTEIN, SCRAMBLE
(seed 1), SMOOTH (r254 definitions verbatim); flips re-derived
25/21/27; FIB_LO 8; chain wards 1e-9 MAIN / 1e-4 controls, SMOOTH
abs 1e-9 x gross; border route 1e-9 / 1e-4; sym 1e-12; PSD eig
bar 1e-10 rel; cell PSD floor 1e-9 x gross; embedding ward 1e-9
(SMOOTH CC abs); prior tol 2e-3 rel; identity ward 1e-12 rel
scale; DOM 3.0; LB band [0.3, 3.0] + sign; contamination bars
0.2 / 0.1; inversion bars 0.8 / 0.2, K80 tol 0.2, prior K80(SCR)
= 2; exchange bar 1e-10 x gross, 64 samples; monotone bars
0.99 / --; TP bars 0.99 / 0.90; carrier bars K90 <= 10 / <= 4 ln R;
must-fail rel 0.05 (unused numerics kept for style), loudness
1e3 x 1e-13; runtime <= 1800 s; smoke = w9 MAIN only (census,
leg-0 typing + PSD, exchange exactness, mW on a synthetic 2x2,
mX; rasters, controls, A2, alias skipped).

SEALED VERDICT FORM (frozen BEFORE evaluation):
  <BASE_KERNEL_ROTATION_DOMINATES | MIXED_INTERACTION_DOMINATES |
   BORDER_PAIRING_LOAD_BEARING | EFFECTS_MIXED_COUPLEDTAU>
+ A2: INVERSION_<IS_BASE_CONTAMINATION|GENUINE_FIND|MIXED>(f_neg)
+ EPST: <CONTROL_FIBER_IS_BASE_CONTAMINATION |
         EPSTEIN_ANOMALY_SURVIVES_PREFIX>
+ SMOOTH_NULL_ANCHOR_<OK|BROKEN>
+ <LEGS_BD_SKIPPED(reason) | LEGS_BD(exchange, monge, carrier)>.
Honesty before beauty: the verdict never converts an INDEFINITE_
CONTINUATION cell into a fiber falsifier; the budget bound and
the base law stay OPEN (r243/r247/r250/r251/r253/r254 stand).

RECORD TABLES (frozen from calibration pass 1, 21/21 gates, wall
0.6 s full / 0.1 s smoke; AMENDMENTS: NONE -- no bar and no
verdict rule moved after the seal):
CAL_VERDICT = EFFECTS_MIXED_COUPLEDTAU +
A2: INVERSION_IS_BASE_CONTAMINATION(f_neg=0.9311) +
EPST: CONTROL_FIBER_IS_BASE_CONTAMINATION +
SMOOTH_NULL_ANCHOR_OK + LEGS_BD_SKIPPED.
Key numbers.  CENSUS w9: N = 184, A = 734 (border 367) on all
four worlds; T_true MAIN +4.3343 / SCR -4.4942 / EPST +0.7615;
chain wards 7.5e-15 / 7.1e-6 / 4.7e-8 (f64 control floor),
border route 9.1e-15 / 6.8e-6, SMOOTH |T|/gross 4.6e-19; flips
re-derived 25/21/27.  LEG 0 TYPE TABLE (world -> pmax, neg
modes in [8, N)): MAIN 184 (0 neg, POSITIVE_PREFIX at full
depth), SCR 21 (37 neg), EPST 25 (55 neg), SMOOTH 27 (4 neg)
-- all controls INDEFINITE_CONTINUATION at full depth; every
own-grid prefix kernel PSD (worst -lambda_min rel 5.7e-16, bar
1e-10): the reviewer core theorem holds numerically.  LEG A
(|U| = 367 on all pairs, embedding wards worst 9.8e-15,
identity wards EXACTLY 0, cleaned chain wards 1.1e-11 MAIN /
2.1e-12 controls): SCR RAW +4.33432/+9.97557/-0.92761/-4.49413
(r254 priors hit, worst rel 4.9e-5) => Db +5.26193, Dbo
-5.64125, Di -9.20777, Gap +8.82844; SCR CLEANED (n* = 21, 13
modes, both kernels PSD): T_MM* +1.81873e-5, T_MS* +0.175915,
T_SM* +1.97101e-5, T_SS* +0.216069 => Db* -1.5228e-6, Dbo*
-0.175897, Di* +0.0401526, Gap* -0.216051.  THE CLEANED PICTURE
INVERTS THE PRIOR READING TWICE: (i) on the causally clean
prefix the BASE rotation is NULL (|Db*| = 1.5e-6: scrambling
the chain does not move the prefix fiber form at the MAIN
border) and the BORDER move carries the prefix gap (|Dbo*|/
|Gap*| = 0.814, sign consistent -- SCRAMBLE's border has MORE
prefix mass than MAIN's, Gap* < 0); (ii) but the RAW full-depth
border effect has the WRONG sign vs its gap (-5.64 vs +8.83),
so the sealed LOAD_BEARING rule (band + sign on raw AND
cleaned) does NOT fire, and neither |Db*| nor |Di*| reaches
factor-3 dominance => EFFECTS_MIXED_COUPLEDTAU by the sealed
priority; the tension (border dominant on the prefix, sign-
inconsistent at full depth) is printed, not upgraded.  EPST RAW
+4.33432/+12.35022/-0.85614/+0.76154 (priors hit) => Gap_raw
+3.57278; EPST CLEANED (n* = 25, 17 modes): T_MM* = T_ME* =
+2.81736e-5 (Dbo* = 1.3e-16: the EPSTEIN border is fiber-
IDENTICAL to MAIN on the common prefix -- head-identical
construction confirmed at the raster level), T_EM* = T_EE* =
+9.95937e-5, Gap* = -7.142e-5 = 2.0e-5 x |Gap_raw| <= 0.2
(crit1) AND crit2 => CONTROL_FIBER_IS_BASE_CONTAMINATION: the
r253/r254 EPSTEIN fiber anomaly lives ENTIRELY in the
indefinite continuation degrees k >= 25 and may no longer be
cited as an independent fiber falsifier.  SMOOTH raster
(n* = 27): border cells raw 7.1e-19 / cleaned 7.3e-20 x gross,
T[SMOOTH, sM] raw +1.22821 typed INDEFINITE_CONTINUATION =>
SMOOTH_NULL_ANCHOR_OK.  LEG A2: h-sign mode split of G_SCR (37
neg / 139 pos modes) exact to 1.5e-15 x gross: T_pos +3292.5670
(>= 0, PSD obeyed) + T_neg -3297.0611 = T_SS -4.4941 -- the two
mode classes cancel to 0.14 percent of their size, the net sign
is carried by the negative class (734x overshoot, printed);
K80_own(SCR) = 2 reproduced (r254 prior); top-2 |c|-eigenpairs
lambda -16305.1 / +2464418.6, c/T shares 1.418 / -0.350, f_neg
0.9376 / 0.9245 => mean 0.9311 >= 0.8 =>
INVERSION_IS_BASE_CONTAMINATION: the r254 'SCRAMBLE spectrally
compact K80 = 2' headline is a statement about the NEGATIVE
h-modes of the broken base (93 percent of the carrying
eigendirections live in the h<0 span), not a border
discriminator -- DOWNGRADED.  LEGS B-D: SKIPPED by the sealed
conditional (LB rule did not fire); band appendix printed
(MAIN flat 0.163..0.077, SCR mid-band shifted 0.155/0.218/
0.121 -- r254 reproduced as INFO).  LEG E: e0 exchange formula
vs direct on 64 sampled adjacent border swaps worst dev 1.2e-15
(gross 101, bar 1e-10 x gross); mA alias killed:
lambda_min(G_SCR full) = -2.948e+6 (1.0e+12 x floor), T_SM
-0.9276 = pos +204.6998 (>= -floor, PSD obeyed) + neg -205.6274
(2.0e+13 x floor), split exact 3.2e-15 x gross -- the T_SM
negativity is 100 percent an h<0-mode (KERNEL) property, never
a border effect; mW flipped-CC formula breaks the ward by
8.98825 = 2|T_CC| exactly (rel 0, 9.0e+9 x floor); mX wrong
cross term deviates 0.282 = 2.8e+10 x the honest floor.
READING (typed, no upgrade): the r254 factorial numbers were
correct but their causal reading was contaminated -- Delta_base
+5.26 and Delta_int -9.21 are INDEFINITE-KERNEL bookkeeping,
not causal effects; on the only causally clean surface (the
common positive prefix) the base rotation does nothing, the
border move is the sole carrier of a small sign-flipped gap,
and both control 'discoveries' (SCRAMBLE spectral compactness,
EPSTEIN fiber anomaly) are base contamination by negative
h-modes.  Consequence vote: COUPLEDTAU -- the MAIN-vs-SCRAMBLE
world gap at full depth is NOT separable into base and border
channels by any rule sealed this round; no exchange/Monge/
spectral pairing theorem is unlocked; tau^aug/tau stays one
indivisible full-source object.  Runtime 0.6 s full / 0.1 s
smoke; run1/run2 identical up to WALL.  AMENDMENTS AFTER
FREEZE: NONE.

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

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH           # noqa: E402 r244
import offdiag_gram_probe as OG              # noqa: E402 r254
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

FIB_LO = 8
assert FIB_LO == OG.FIB_LO
KZ = 9
T_MAIN_BAR = 1e-9
T_CTRL_BAR = 1e-4
BORD_MAIN_BAR = 1e-9
BORD_CTRL_BAR = 1e-4
SYM_BAR = 1e-12
SM_GUARD = 1e-9
PSD_EIG_BAR = 1e-10
CELL_PSD_FLOOR = 1e-9
EMB_BAR = 1e-9
PRIOR_TOL = 2e-3
WARD_ID_BAR = 1e-12
CHAIN_CLN_MAIN = 1e-9
CHAIN_CLN_CTRL = 1e-4
DOM_FACTOR = 3.0
LB_LO, LB_HI = 0.3, 3.0
CONTAM_GAP_BAR = 0.2
CONTAM_BORD_BAR = 0.1
INV_HI, INV_LO = 0.8, 0.2
K80_TOL = 0.2
PRIOR_K80_SCR = 2
NEG_RANK_CUT = 1e-10
EXG_BAR = 1e-10
EXG_SAMPLES = 64
MONO_GO = 0.99
TP_GO = 0.99
TP_NO = 0.90
K90_FIXED = 10
MF_LOUD = 1e3
MF_NOISE = 1e-13
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
PRIOR_SCR = {"MM": 4.3343, "MC": 9.9756, "CM": -0.9276,
             "CC": -4.4941}
PRIOR_EPST = {"MC": 12.3502, "CM": -0.8561, "CC": 0.7615}
CAL_VERDICT = (
    "EFFECTS_MIXED_COUPLEDTAU + "
    "A2: INVERSION_IS_BASE_CONTAMINATION(f_neg=0.9311) + "
    "EPST: CONTROL_FIBER_IS_BASE_CONTAMINATION + "
    "SMOOTH_NULL_ANCHOR_OK + LEGS_BD_SKIPPED")

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
    return (not bad), ("NO zero/prime oracles; kernels consume the "
                       "FREE chain (alh_k, gam_{k+1}, sign h_k, "
                       "k <= N-2) + atom positions/weights ONLY; "
                       "ground truth (T_true, flips, partial sums) "
                       "enters gates only"
                       if not bad else "; ".join(bad))


def pmax_of(p):
    """maximal positive prefix degree: first k in [FIB_LO, N) with
    h_k < 0, else N (leg-0 firewall coordinate)."""
    for k in range(FIB_LO, p["N"]):
        if p["rows"][k]["sg_h"] < 0.0:
            return k
    return p["N"]


def cell_type(pmax, depth):
    return ("POSITIVE_PREFIX" if depth <= pmax
            else "INDEFINITE_CONTINUATION")


def prefix_kernel_minmax(W, depth):
    P, sg = W["P"], W["sgv"]
    Gp = (P[FIB_LO:depth].T * sg[FIB_LO:depth]) @ P[FIB_LO:depth]
    ev = np.linalg.eigvalsh(Gp)
    return float(ev[0]), float(ev[-1])


def union_raster(Wm, Wc, nstar, want_alias=False):
    """r254-a1 sorted-union embedding (adopted, re-gated): the four
    factorial cells at full depth AND at the common positive prefix
    n*, with kernel eigenvalue extremes; optional h-sign mode split
    of the C kernel at full depth against the M border (alias)."""
    U = np.unique(np.concatenate([Wm["wx"], Wc["wx"]]))
    im = np.searchsorted(U, Wm["wx"])
    ic = np.searchsorted(U, Wc["wx"])
    ok_pos = (np.array_equal(Wm["bx"], Wc["bx"])
              and bool(np.all(U[im] == Wm["wx"]))
              and bool(np.all(U[ic] == Wc["wx"])))
    posU = np.concatenate([Wm["bx"], U])
    nbU = len(Wm["bx"])

    def s_emb(W, idx):
        sv = np.zeros(len(posU))
        sv[:nbU] = W["bw"]
        np.add.at(sv, nbU + idx, -W["c0"] * W["wu"])
        return sv

    sM, sC = s_emb(Wm, im), s_emb(Wc, ic)
    PM = OG.phat_matrix(Wm["p"]["rows"], posU, Wm["N"])
    PC = OG.phat_matrix(Wc["p"]["rows"], posU, Wc["N"])
    sgM, sgC = Wm["sgv"], Wc["sgv"]

    def kern(P, sg, dep):
        return (P[FIB_LO:dep].T * sg[FIB_LO:dep]) @ P[FIB_LO:dep]

    out = dict(ok_pos=ok_pos, nU=len(U), nstar=nstar)
    for lab, dm, dc in (("raw", Wm["N"], Wc["N"]),
                        ("cln", nstar, nstar)):
        GM = kern(PM, sgM, dm)
        GC = kern(PC, sgC, dc)
        cells = dict(MM=float(sM @ (GM @ sM)),
                     MC=float(sC @ (GM @ sC)),
                     CM=float(sM @ (GC @ sM)),
                     CC=float(sC @ (GC @ sC)))
        evM = np.linalg.eigvalsh(GM)
        evC = np.linalg.eigvalsh(GC)
        if lab == "raw":
            out["grossU"] = float(np.abs(sM) @ (np.abs(GM)
                                                @ np.abs(sM)))
        out[lab] = dict(cells=cells,
                        lmM=float(evM[0]), lxM=float(evM[-1]),
                        lmC=float(evC[0]), lxC=float(evC[-1]))
        del GM, GC
    if want_alias:
        sgt = sgC[FIB_LO:Wc["N"]]
        neg = np.nonzero(sgt < 0.0)[0] + FIB_LO
        pos = np.nonzero(sgt > 0.0)[0] + FIB_LO
        Gn = (PC[neg].T * sgC[neg]) @ PC[neg]
        Gp = (PC[pos].T * sgC[pos]) @ PC[pos]
        out["alias"] = dict(T_SM_neg=float(sM @ (Gn @ sM)),
                            T_SM_pos=float(sM @ (Gp @ sM)),
                            nneg=len(neg))
        del Gn, Gp
    return out


def effects(cells):
    Db = cells["MM"] - cells["CM"]
    Dbo = cells["MM"] - cells["MC"]
    Di = cells["MM"] - cells["MC"] - cells["CM"] + cells["CC"]
    gap = cells["MM"] - cells["CC"]
    scale = max(abs(v) for v in cells.values())
    ward = abs((Db + Dbo - Di) - gap) / max(scale, 1e-300)
    return dict(Db=Db, Dbo=Dbo, Di=Di, gap=gap, ward=ward,
                scale=scale)


def lb_ok(e):
    if e["Dbo"] * e["gap"] <= 0.0:
        return False
    r = abs(e["Dbo"]) / max(abs(e["gap"]), 1e-300)
    return LB_LO <= r <= LB_HI


def adjudicate(e_cln, e_raw, grossU):
    if abs(e_cln["gap"]) <= 1e-9 * grossU:
        return ("EFFECTS_MIXED_COUPLEDTAU(CLEANED_GAP_NULL)",
                "cleaned gap below floor -- no causal split")
    ab, abo, ai = (abs(e_cln["Db"]), abs(e_cln["Dbo"]),
                   abs(e_cln["Di"]))
    if ab >= DOM_FACTOR * max(abo, ai):
        return ("BASE_KERNEL_ROTATION_DOMINATES",
                "|Db*| %.4g >= %g x max(|Dbo*| %.4g, |Di*| %.4g)"
                % (ab, DOM_FACTOR, abo, ai))
    if ai >= DOM_FACTOR * max(ab, abo):
        return ("MIXED_INTERACTION_DOMINATES",
                "|Di*| %.4g >= %g x max(|Db*| %.4g, |Dbo*| %.4g)"
                % (ai, DOM_FACTOR, ab, abo))
    if lb_ok(e_raw) and lb_ok(e_cln):
        return ("BORDER_PAIRING_LOAD_BEARING",
                "sign-consistent |Dbo|/|Gap| in [%.1f, %.1f] on "
                "raw AND cleaned" % (LB_LO, LB_HI))
    return ("EFFECTS_MIXED_COUPLEDTAU",
            "no factor-%g dominance; LB rule raw=%s cln=%s "
            "(sign/band sealed: overshoot with wrong sign does "
            "NOT count)" % (DOM_FACTOR, lb_ok(e_raw),
                            lb_ok(e_cln)))


def exchange_pieces(W):
    G, sb, nb = W["G"], W["s_b"], W["nb"]
    order = np.argsort(W["pos"][:nb], kind="stable")
    Gs = G @ sb
    T0 = float(sb @ Gs)
    return G, sb, order, Gs, T0


def dt_formula(G, Gs, s, i, j, wrong=False):
    d = s[i] - s[j]
    cross = 2.0 * G[i, j] if wrong else -2.0 * G[i, j]
    return 2.0 * d * (Gs[j] - Gs[i]) \
        + d * d * (G[i, i] + G[j, j] + cross)


def dt_direct(G, s, T0, i, j):
    sw = s.copy()
    sw[i], sw[j] = s[j], s[i]
    return float(sw @ (G @ sw)) - T0


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("baseborder_factorial_probe -- PRIME.PORT.FIBER."
          "BASEBORDER.FACTORIAL.01 (round 256)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 MAIN only: census, leg-0, "
                        "exchange exactness, mW synthetic, mX; "
                        "rasters/controls/A2/alias skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "leg-0 typing POSITIVE_PREFIX iff depth <= pmax (first "
          "h-flip in [8, N)); PSD eig bar %.0e rel; cell PSD floor "
          "%.0e gross; r254-a1 union embedding adopted + re-gated "
          "(ward %.0e); priors rel %.0e; identity ward %.0e rel "
          "scale; ADJUDICATION SEALED: DOM %.1f on the CLEANED "
          "raster, LB band [%.1f, %.1f] + sign on raw AND cleaned "
          "(wrong-sign overshoot does NOT count), contamination "
          "bars %.1f/%.1f, inversion bars %.1f/%.1f (top-2 |c| "
          "eigenpairs vs h<0 mode span); legs B-D conditional on "
          "BORDER_PAIRING_LOAD_BEARING only; exchange bar %.0e "
          "gross, monotone %.2f, TP %.2f/%.2f, carrier K90 <= %d "
          "/ <= 4 ln R; must-fail loudness %.0e x %.0e"
          % (PSD_EIG_BAR, CELL_PSD_FLOOR, EMB_BAR, PRIOR_TOL,
             WARD_ID_BAR, DOM_FACTOR, LB_LO, LB_HI,
             CONTAM_GAP_BAR, CONTAM_BORD_BAR, INV_HI, INV_LO,
             EXG_BAR, MONO_GO, TP_GO, TP_NO, K90_FIXED,
             MF_LOUD, MF_NOISE))

    # ---------------- S1: census + worlds
    section("S1  CENSUS + WORLDS")
    packs = {"w9": BH.wpack(KZ)}
    ctrl = {}
    if not smoke:
        rr9c = core.build_window(KZ)
        N_E = int(math.floor(math.exp(2.0 * rr9c["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9c["alpha"])
        ctrl_defs = (("EPSTEIN", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCRAMBLE", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))))
        ctrl = {c: BH.wpack(KZ, base_kw=kw) for c, kw in ctrl_defs}
    okC = packs["w9"]["nf"] is None
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl) \
        if ctrl else True
    Wd = {"w9": OG.world_build(packs["w9"], want_P=True)}
    if not smoke:
        Wd["SCR"] = OG.world_build(ctrl["SCRAMBLE"], want_P=True)
        Wd["EPST"] = OG.world_build(ctrl["EPSTEIN"], want_P=True)
        Wd["SMOOTH"] = OG.world_build(ctrl["SMOOTH"], want_P=True)
    t_main = t_ctrl = b_main = b_ctrl = sym_worst = 0.0
    sm_ratio = 0.0
    for tag, W in Wd.items():
        sym_worst = max(sym_worst, W["sym_dev"]
                        / max(float(np.max(np.abs(W["G"]))),
                              1e-300))
        if tag == "SMOOTH":
            sm_ratio = abs(W["T_mat"]) / max(W["gross"], 1e-300)
            info("%-6s N=%d A=%d  |T_mat|/gross %.1e (null "
                 "anchor part 1)" % (tag, W["N"], W["A"],
                                     sm_ratio))
            continue
        devT = abs(W["T_mat"] / W["T_true"] - 1.0)
        devB = abs(W["T_bord"] / W["T_mat"] - 1.0)
        if tag == "w9":
            t_main, b_main = devT, devB
        else:
            t_ctrl = max(t_ctrl, devT)
            b_ctrl = max(b_ctrl, devB)
        info("%-6s N=%d A=%d (border %d)  T_true %+.4f  chain dev "
             "%.1e  border-route dev %.1e"
             % (tag, W["N"], W["A"], W["nb"], W["T_true"], devT,
                devB))
    ok_sm = (sm_ratio <= SM_GUARD) if not smoke else True
    check("G10-census-worlds",
          okC and okCf and t_main <= T_MAIN_BAR
          and t_ctrl <= T_CTRL_BAR and b_main <= BORD_MAIN_BAR
          and b_ctrl <= BORD_CTRL_BAR and sym_worst <= SYM_BAR
          and ok_sm,
          "MAIN free prefix positive; control flips re-derived %s; "
          "chain wards MAIN %.1e (bar %.0e) / controls %.1e (bar "
          "%.0e); border route %.1e / %.1e; symmetry %.1e (bar "
          "%.0e); SMOOTH null part 1: |T|/gross %s (bar %.0e)"
          % (str({c: ctrl[c]["nf"] for c in ctrl}) if ctrl
             else "SMOKE-skipped", t_main, T_MAIN_BAR, t_ctrl,
             T_CTRL_BAR, b_main, b_ctrl, sym_worst, SYM_BAR,
             ("%.1e" % sm_ratio) if not smoke else "skipped",
             SM_GUARD))

    # ---------------- S2: LEG 0 -- positive-prefix firewall
    section("S2  LEG 0 -- POSITIVE-PREFIX FIREWALL")
    pmax = {}
    psd_worst = 0.0
    for tag, W in Wd.items():
        pm = pmax_of(W["p"])
        pmax[tag] = pm
        sgt = W["sgv"][FIB_LO:W["N"]]
        nneg = int(np.sum(sgt < 0.0))
        lmin, lmax = prefix_kernel_minmax(W, pm)
        rel = -lmin / max(lmax, 1.0)
        psd_worst = max(psd_worst, rel)
        info("%-6s N=%d  pmax=%d  neg modes in [8,N): %d  "
             "type(T_N) = %-24s  prefix-kernel lambda_min %.2e "
             "(rel %.1e)"
             % (tag, W["N"], pm, nneg, cell_type(pm, W["N"]),
                lmin, rel))
    check("G11-leg0-typing-psd", psd_worst <= PSD_EIG_BAR,
          "firewall type table printed (world -> max positive "
          "prefix); every own-grid PREFIX kernel G_pmax is PSD: "
          "worst -lambda_min/max(lambda_max,1) = %.1e (bar %.0e) "
          "-- the reviewer core theorem holds numerically on "
          "every positive prefix" % (psd_worst, PSD_EIG_BAR))

    # ---------------- S3: LEG A -- factorial rasters
    section("S3  LEG A -- 2x2 WORLD CENSUS (raw + firewall-cleaned)")
    if not smoke:
        R = {}
        eff = {}
        adm_ok = True
        emb_worst = 0.0
        smcc_worst = 0.0
        prior_worst = 0.0
        psd_cell_worst = -1e300
        psd_kern_worst = 0.0
        ward_worst = 0.0
        chain_worst_m = chain_worst_c = sm_cln_worst = 0.0
        for ct in ("SCR", "EPST", "SMOOTH"):
            Wc = Wd[ct]
            nstar = min(pmax["w9"], pmax[ct])
            rb = union_raster(Wd["w9"], Wc, nstar,
                              want_alias=(ct == "SCR"))
            R[ct] = rb
            adm_ok = adm_ok and rb["ok_pos"] and nstar > FIB_LO
            emb_worst = max(emb_worst,
                            abs(rb["raw"]["cells"]["MM"]
                                / Wd["w9"]["T_mat"] - 1.0))
            if ct == "SMOOTH":
                smcc_worst = max(
                    abs(rb["raw"]["cells"]["CC"]) / rb["grossU"],
                    abs(rb["raw"]["cells"]["MC"]) / rb["grossU"])
                sm_cln_worst = max(
                    abs(rb["cln"]["cells"]["CC"]) / rb["grossU"],
                    abs(rb["cln"]["cells"]["MC"]) / rb["grossU"])
            else:
                emb_worst = max(emb_worst,
                                abs(rb["raw"]["cells"]["CC"]
                                    / Wc["T_mat"] - 1.0))
            eff[ct] = {lab: effects(rb[lab]["cells"])
                       for lab in ("raw", "cln")}
            ward_worst = max(ward_worst, eff[ct]["raw"]["ward"],
                             eff[ct]["cln"]["ward"])
            # PSD checks: MAIN kernel raw + both kernels cleaned
            psd_kern_worst = max(
                psd_kern_worst,
                -rb["raw"]["lmM"] / max(rb["raw"]["lxM"], 1.0),
                -rb["cln"]["lmM"] / max(rb["cln"]["lxM"], 1.0),
                -rb["cln"]["lmC"] / max(rb["cln"]["lxC"], 1.0))
            psd_cell_worst = max(
                psd_cell_worst,
                -rb["raw"]["cells"]["MC"] / rb["grossU"],
                *[-v / rb["grossU"]
                  for v in rb["cln"]["cells"].values()])
            # cleaned chain wards (diagonal cells vs partial sums)
            S_M = np.asarray(Wd["w9"]["p"]["S"], float)
            tgt_m = float(S_M[nstar - 1] - S_M[FIB_LO - 1])
            chain_worst_m = max(chain_worst_m,
                                abs(rb["cln"]["cells"]["MM"]
                                    / tgt_m - 1.0))
            if ct != "SMOOTH":
                S_C = np.asarray(Wc["p"]["S"], float)
                tgt_c = float(S_C[nstar - 1] - S_C[FIB_LO - 1])
                chain_worst_c = max(chain_worst_c,
                                    abs(rb["cln"]["cells"]["CC"]
                                        / tgt_c - 1.0))
            for lab in ("raw", "cln"):
                c = rb[lab]["cells"]
                e = eff[ct][lab]
                dep = ("N_M=%d/N_C=%d" % (Wd["w9"]["N"], Wc["N"])
                       ) if lab == "raw" else ("n*=%d" % nstar)
                typM = cell_type(pmax["w9"], Wd["w9"]["N"]
                                 if lab == "raw" else nstar)
                typC = cell_type(pmax[ct], Wc["N"]
                                 if lab == "raw" else nstar)
                info("%-6s %-3s (%s) MM %+.6g  MC %+.6g  CM %+.6g"
                     "  CC %+.6g | M-kernel %s / C-kernel %s"
                     % (ct, lab, dep, c["MM"], c["MC"], c["CM"],
                        c["CC"], typM, typC))
                info("%-6s %-3s Delta_base %+.6g  Delta_border "
                     "%+.6g  Delta_int %+.6g  Gap %+.6g  (ward "
                     "%.1e)" % (ct, lab, e["Db"], e["Dbo"],
                                e["Di"], e["gap"], e["ward"]))
        check("G20-raster-admission", adm_ok
              and emb_worst <= EMB_BAR and smcc_worst <= SM_GUARD,
              "r254-a1 union embedding re-gated on 3 pairs: "
              "border bitwise identical + window position sets "
              "found in union; |U| = %s; n* = %s (all > %d); "
              "embedding wards worst %.1e (bar %.0e); SMOOTH CC/"
              "MC abs %.1e (bar %.0e)"
              % (str({c: R[c]["nU"] for c in R}),
                 str({c: R[c]["nstar"] for c in R}), FIB_LO,
                 emb_worst, EMB_BAR, smcc_worst, SM_GUARD))
        for ct, pri in (("SCR", PRIOR_SCR), ("EPST", PRIOR_EPST)):
            for key, ref in pri.items():
                prior_worst = max(prior_worst,
                                  abs(R[ct]["raw"]["cells"][key]
                                      / ref - 1.0))
        check("G21-r254-priors", prior_worst <= PRIOR_TOL,
              "raw rasters vs the r254 records (SCR 4 cells + "
              "EPST 3 cells): worst rel %.1e (tol %.0e) -- the "
              "r254 cross table is verified, then TYPED: T_SM/"
              "T_SS/T_EM/T_EE are INDEFINITE_CONTINUATION cells "
              "(no independent fiber falsifiers), T_MM/T_MS/T_ME "
              "are POSITIVE_PREFIX" % (prior_worst, PRIOR_TOL))
        check("G22-psd-theorem-empirical",
              psd_kern_worst <= PSD_EIG_BAR
              and psd_cell_worst <= CELL_PSD_FLOOR,
              "kernel PSD (MAIN raw + all cleaned): worst "
              "-lambda_min rel %.1e (bar %.0e); every POSITIVE_"
              "PREFIX-typed cell >= -floor: worst -cell/gross "
              "%.1e (floor %.0e) -- T >= 0 for EVERY border "
              "measure under a positive kernel, empirically "
              "(T_MS raw %+.4f > 0 confirms the theorem)"
              % (psd_kern_worst, PSD_EIG_BAR, psd_cell_worst,
                 CELL_PSD_FLOOR,
                 R["SCR"]["raw"]["cells"]["MC"]))
        check("G23-identity-ward", ward_worst <= WARD_ID_BAR,
              "Delta_base + Delta_border - Delta_int = Gap on "
              "all 6 rasters: worst rel %.1e (bar %.0e)"
              % (ward_worst, WARD_ID_BAR))
        check("G24-cleaned-chain-wards",
              chain_worst_m <= CHAIN_CLN_MAIN
              and chain_worst_c <= CHAIN_CLN_CTRL
              and sm_cln_worst <= SM_GUARD,
              "cleaned diagonal cells vs the bitwise partial "
              "sums S_{n*-1} - S_7: MAIN worst %.1e (bar %.0e), "
              "controls %.1e (bar %.0e), SMOOTH abs %.1e (bar "
              "%.0e) -- the truncated kernels sit on the exact "
              "chain" % (chain_worst_m, CHAIN_CLN_MAIN,
                         chain_worst_c, CHAIN_CLN_CTRL,
                         sm_cln_worst, SM_GUARD))
        v_main, why = adjudicate(eff["SCR"]["cln"],
                                 eff["SCR"]["raw"],
                                 R["SCR"]["grossU"])
        e_r, e_c = eff["SCR"]["raw"], eff["SCR"]["cln"]
        check("G25-mainxscr-adjudication", True,
              "SEALED verdict on MAIN x SCRAMBLE: %s (%s); raw "
              "Db %+.4f Dbo %+.4f Di %+.4f Gap %+.4f vs cleaned "
              "Db* %+.6g Dbo* %+.6g Di* %+.6g Gap* %+.6g; "
              "|Dbo|/|Gap| raw %.3g (sign %s) cln %.3g (sign %s)"
              % (v_main, why, e_r["Db"], e_r["Dbo"], e_r["Di"],
                 e_r["gap"], e_c["Db"], e_c["Dbo"], e_c["Di"],
                 e_c["gap"],
                 abs(e_r["Dbo"]) / max(abs(e_r["gap"]), 1e-300),
                 "OK" if e_r["Dbo"] * e_r["gap"] > 0 else "WRONG",
                 abs(e_c["Dbo"]) / max(abs(e_c["gap"]), 1e-300),
                 "OK" if e_c["Dbo"] * e_c["gap"] > 0
                 else "WRONG"))
        ge_r = eff["EPST"]["raw"]["gap"]
        ge_c = eff["EPST"]["cln"]["gap"]
        dbo_c = eff["EPST"]["cln"]["Dbo"]
        crit1 = abs(ge_c) <= CONTAM_GAP_BAR * abs(ge_r)
        crit2 = abs(dbo_c) <= CONTAM_BORD_BAR * max(abs(ge_c),
                                                    1e-12)
        v_ep = ("CONTROL_FIBER_IS_BASE_CONTAMINATION"
                if (crit1 or crit2)
                else "EPSTEIN_ANOMALY_SURVIVES_PREFIX")
        check("G26-epstein-contamination", True,
              "EPSTEIN anomaly on the common positive prefix "
              "(n* = %d): |Gap*| = %.4g = %.3f x |Gap_raw| %.4g "
              "(bar %.1f, crit1 %s); |Dbo*| = %.3g vs %.1f x "
              "|Gap*| (crit2 %s) => %s"
              % (R["EPST"]["nstar"], abs(ge_c),
                 abs(ge_c) / max(abs(ge_r), 1e-300), abs(ge_r),
                 CONTAM_GAP_BAR, crit1, abs(dbo_c),
                 CONTAM_BORD_BAR, crit2, v_ep))
        v_sm = ("SMOOTH_NULL_ANCHOR_OK"
                if (smcc_worst <= SM_GUARD
                    and sm_cln_worst <= SM_GUARD)
                else "SMOOTH_NULL_ANCHOR_BROKEN")
        check("G27-smooth-null-anchor",
              v_sm == "SMOOTH_NULL_ANCHOR_OK",
              "SMOOTH border cells vanish raw %.1e / cleaned "
              "%.1e x gross (bar %.0e) -- the null world anchors "
              "the raster machinery: %s"
              % (smcc_worst, sm_cln_worst, SM_GUARD, v_sm))
    else:
        v_main, v_ep, v_sm = ("SMOKE_NO_ADJUDICATION",) * 3
        eff = {}
        R = {}
        for g in ("G20-raster-admission", "G21-r254-priors",
                  "G22-psd-theorem-empirical",
                  "G23-identity-ward", "G24-cleaned-chain-wards",
                  "G25-mainxscr-adjudication",
                  "G26-epstein-contamination",
                  "G27-smooth-null-anchor"):
            check(g, True, "SMOKE: skipped (needs controls)")

    # ---------------- S4: LEG A2 -- inversion adjudication
    section("S4  LEG A2 -- INVERSION ADJUDICATION (SCRAMBLE "
            "compactness)")
    if not smoke:
        Ws = OG.eig_block(Wd["SCR"])
        sgt = Ws["sgv"][FIB_LO:Ws["N"]]
        neg = np.nonzero(sgt < 0.0)[0] + FIB_LO
        pos = np.nonzero(sgt > 0.0)[0] + FIB_LO
        Pn, Pp = Ws["P"][neg], Ws["P"][pos]
        Gn = (Pn.T * Ws["sgv"][neg]) @ Pn
        Gp = (Pp.T * Ws["sgv"][pos]) @ Pp
        T_neg = float(Ws["s"] @ (Gn @ Ws["s"]))
        T_pos = float(Ws["s"] @ (Gp @ Ws["s"]))
        split_dev = abs(T_pos + T_neg - Ws["T_mat"]) \
            / max(Ws["gross"], 1e-300)
        shares, k80, dpart = OG.profile_stats(Ws["c"],
                                              Ws["T_mat"])
        check("G30-a2-mode-split",
              split_dev <= 1e-9
              and T_pos >= -CELL_PSD_FLOOR * Ws["gross"]
              and k80 == PRIOR_K80_SCR,
              "h-sign mode split of G_SCR (%d neg / %d pos "
              "modes): T_pos %+.4f (PSD: >= -floor) + T_neg "
              "%+.4f = T_SS %+.4f (dev %.1e x gross); the "
              "negative modes carry %.1f percent of T_SS; "
              "K80_own(SCR) = %d (r254 prior %d) reproduced"
              % (len(neg), len(pos), T_pos, T_neg, Ws["T_mat"],
                 split_dev, 100.0 * T_neg / Ws["T_mat"], k80,
                 PRIOR_K80_SCR))
        Qu, sv, _vt = np.linalg.svd(Pn.T, full_matrices=False)
        Q = Qu[:, sv > NEG_RANK_CUT * sv[0]]
        top = np.argsort(-np.abs(Ws["c"]))[:2]
        fn = [float(np.sum((Q.T @ Ws["V"][:, k]) ** 2))
              for k in top]
        mean_f = float(np.mean(fn))
        if mean_f >= INV_HI:
            v_inv = "INVERSION_IS_BASE_CONTAMINATION(f_neg=" \
                "%.4f)" % mean_f
        elif mean_f <= INV_LO:
            v_inv = "INVERSION_GENUINE_FIND(f_neg=%.4f)" % mean_f
        else:
            v_inv = "INVERSION_MIXED(f_neg=%.4f)" % mean_f
        check("G31-a2-inversion", True,
              "top-2 |c| eigenpairs of G_SCR: lambda %s, c/T "
              "shares %s, f_neg (overlap with the h<0 mode span, "
              "rank %d) %s => mean %.4f (bars %.1f/%.1f) => %s%s"
              % (str([round(float(Ws["lam"][k]), 1)
                      for k in top]),
                 str([round(float(Ws["c"][k] / Ws["T_mat"]), 3)
                      for k in top]), Q.shape[1],
                 str([round(f, 4) for f in fn]), mean_f, INV_HI,
                 INV_LO, v_inv,
                 " -- the r254 'SCRAMBLE spectrally compact' "
                 "headline is DOWNGRADED to base contamination"
                 if mean_f >= INV_HI else ""))
    else:
        v_inv = "A2_SMOKE_NA"
        check("G30-a2-mode-split", True, "SMOKE: skipped")
        check("G31-a2-inversion", True, "SMOKE: skipped")

    # ---------------- S5: LEGS B-D (conditional)
    section("S5  LEGS B-D (conditional on BORDER_PAIRING_"
            "LOAD_BEARING)")
    unlocked = (v_main == "BORDER_PAIRING_LOAD_BEARING")
    if unlocked:
        W9 = Wd["w9"]
        G, sb, order, Gs, T0 = exchange_pieces(W9)
        dts = []
        for t in range(len(order) - 1):
            i, j = int(order[t]), int(order[t + 1])
            if sb[i] == sb[j]:
                continue
            dts.append(dt_formula(G, Gs, sb, i, j))
        dts = np.asarray(dts)
        fpos = float(np.mean(dts > 0.0)) if len(dts) else 0.0
        frac = max(fpos, 1.0 - fpos)
        v_ex = ("EXCHANGE_MONOTONE_GO(frac=%.4f)" % frac
                if frac >= MONO_GO
                else "EXCHANGE_SIGN_MIXED(frac=%.4f)" % frac)
        nb = W9["nb"]
        Gss = G[np.ix_(order, order)]
        D2 = Gss[:-1, :-1] + Gss[1:, 1:] - Gss[:-1, 1:] \
            - Gss[1:, :-1]
        iu = np.triu_indices(nb - 1, k=1)
        vv = D2[iu]
        vv = vv[vv != 0.0]
        fp2 = float(np.mean(vv > 0.0)) if len(vv) else 0.0
        frac2 = max(fp2, 1.0 - fp2)
        if frac2 >= TP_GO:
            v_tp = "MONGE_TP_ORDER(frac=%.4f)" % frac2
        elif frac2 < TP_NO:
            v_tp = "NO_EXCHANGE_ORDER(frac=%.4f)" % frac2
        else:
            v_tp = "WEAK_ORDER(frac=%.4f)" % frac2
        OG.eig_block(W9)
        o = np.argsort(-np.abs(W9["lam"]))
        cum = np.cumsum(W9["c"][o]) / W9["T_mat"]

        def kfor(tol):
            w = np.nonzero(np.abs(cum - 1.0) <= tol)[0]
            return int(w[0]) + 1 if len(w) else len(cum) + 1

        k90, k99, k999 = kfor(0.1), kfor(0.01), kfor(0.001)
        Rk = W9["N"] - FIB_LO
        if k90 <= K90_FIXED:
            v_ca = "FIXED_SPECTRAL_CARRIER"
        elif k90 <= 4.0 * math.log(Rk):
            v_ca = "LOG_SPECTRAL_CARRIER"
        else:
            v_ca = "EXTENSIVE_SPECTRAL_CARRIER"
        v_ca += "(K90=%d, K99=%d, K99.9=%d of %d)" \
            % (k90, k99, k999, Rk)
        v_bd = "LEGS_BD(%s + %s + %s)" % (v_ex, v_tp, v_ca)
        check("G40-legsBD", True,
              "UNLOCKED: %d admissible adjacent border swaps, "
              "%s; %d Monge quadruples, %s; source-pure "
              "|lambda|-ordered carrier: %s"
              % (len(dts), v_ex, len(vv), v_tp, v_ca))
    else:
        v_bd = "LEGS_BD_SKIPPED(%s)" % v_main
        check("G40-legsBD", True,
              "SKIPPED by the sealed conditional: main verdict "
              "%s != BORDER_PAIRING_LOAD_BEARING -- no exchange/"
              "Monge/spectral pairing claim is registered; their "
              "gates do not count" % v_main)
    if not smoke:
        for tag in ("w9", "SCR"):
            bs = OG.band_stats(Wd[tag])
            tot = max(float(np.sum(bs["ab"])), 1e-300)
            info("APPENDIX %-4s d0 %.3g  dyadic band |C|-shares: "
                 "%s" % (tag, bs["d0"],
                         " ".join("%.3f" % (v / tot)
                                  for v in bs["ab"])))

    # ---------------- S6: LEG E -- falsifiers + must-fails
    section("S6  LEG E -- FALSIFIERS + MUST-FAILS")
    W9 = Wd["w9"]
    G, sb, order, Gs, T0 = exchange_pieces(W9)
    samp = np.unique(np.linspace(0, len(order) - 2,
                                 EXG_SAMPLES).astype(int))
    dev_h = 0.0
    best_load, best_pair = -1.0, None
    for t in samp:
        i, j = int(order[t]), int(order[t + 1])
        dd = sb[i] - sb[j]
        dev_h = max(dev_h, abs(dt_formula(G, Gs, sb, i, j)
                               - dt_direct(G, sb, T0, i, j)))
    for t in range(len(order) - 1):
        i, j = int(order[t]), int(order[t + 1])
        dd = sb[i] - sb[j]
        load = abs(4.0 * dd * dd * G[i, j])
        if load > best_load:
            best_load, best_pair = load, (i, j)
    i, j = best_pair
    dt_bad = dt_formula(G, Gs, sb, i, j, wrong=True)
    dt_dir = dt_direct(G, sb, T0, i, j)
    mx_dev = abs(dt_bad - dt_dir)
    mx_floor = MF_LOUD * max(dev_h, MF_NOISE * W9["gross"])
    ok_e0 = dev_h <= EXG_BAR * W9["gross"]
    ok_mx = mx_dev >= mx_floor
    check("G60-exchange-formula-mx",
          ok_e0 and ok_mx,
          "e0: exchange formula vs direct on %d sampled adjacent "
          "border swaps: worst dev %.1e (bar %.0e x gross %.3g); "
          "mX wrong cross term (+2G_ij) at the max-|4d^2 G_ij| "
          "swap: dev %.3g = %.1e x the honest floor (bar %.0e x)"
          % (len(samp), dev_h, EXG_BAR, W9["gross"], mx_dev,
             mx_dev / max(dev_h, MF_NOISE * W9["gross"]),
             MF_LOUD))
    if not smoke:
        cells = R["SCR"]["raw"]["cells"]
    else:
        cells = dict(MM=1.0, MC=2.0, CM=3.0, CC=4.0)
    e_ok = effects(cells)
    Di_bad = cells["MM"] - cells["MC"] - cells["CM"] - cells["CC"]
    resid = abs((e_ok["Db"] + e_ok["Dbo"] - Di_bad) - e_ok["gap"])
    pred = 2.0 * abs(cells["CC"])
    mw_floor = MF_LOUD * max(e_ok["ward"], MF_NOISE) \
        * e_ok["scale"]
    ok_mw = abs(resid / pred - 1.0) <= 1e-9 and resid >= mw_floor
    check("G61-mustfail-effect-formula", ok_mw,
          "mW flipped-CC interaction formula breaks the identity "
          "ward by %.6g vs predicted 2|T_CC| = %.6g (rel %.1e); "
          "loudness %.1e x floor%s"
          % (resid, pred, abs(resid / pred - 1.0),
             resid / max(mw_floor, 1e-300),
             " (SMOKE: synthetic 2x2)" if smoke else ""))
    if not smoke:
        al = R["SCR"]["alias"]
        cM = R["SCR"]["raw"]["cells"]["CM"]
        lmC = R["SCR"]["raw"]["lmC"]
        lxC = R["SCR"]["raw"]["lxC"]
        gU = R["SCR"]["grossU"]
        loud_neg = -lmC >= MF_LOUD * MF_NOISE * max(lxC, 1.0)
        split_dev = abs(al["T_SM_pos"] + al["T_SM_neg"] - cM) \
            / max(gU, 1e-300)
        pos_ok = al["T_SM_pos"] >= -CELL_PSD_FLOOR * gU
        neg_loud = -al["T_SM_neg"] >= MF_LOUD * MF_NOISE * gU
        check("G62-mustfail-alias", loud_neg and pos_ok
              and neg_loud and split_dev <= 1e-9,
              "FIREWALL-OMITTED alias killed: lambda_min(G_SCR "
              "full) = %.4g (%.1e x floor, loud); mode split of "
              "T_SM %+.4f = pos %+.4f (>= -floor, PSD obeyed) + "
              "neg %+.4f (< 0, %.1e x floor) exact to %.1e x "
              "gross -- the T_SM negativity is 100 percent an "
              "h<0-mode (KERNEL) property; labeling it a border "
              "effect without leg 0 would be the alias"
              % (lmC, -lmC / max(MF_NOISE * max(lxC, 1.0),
                                 1e-300), cM, al["T_SM_pos"],
                 al["T_SM_neg"],
                 -al["T_SM_neg"] / max(MF_NOISE * gU, 1e-300),
                 split_dev))
    else:
        check("G62-mustfail-alias", True,
              "SMOKE: skipped (needs SCRAMBLE)")

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G90-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the positive-prefix firewall typing of every "
          "factorial cell, the firewall-cleaned 2x2 census on "
          "the common positive prefix, the sealed base/border/"
          "interaction adjudication, the SCRAMBLE-inversion and "
          "EPSTEIN-anomaly re-adjudications, and the "
          "unconditional exchange-formula machinery")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        verd = " + ".join([v_main, "A2: " + v_inv,
                           "EPST: " + v_ep, v_sm, v_bd])
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G91-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: the firewall type table, both "
          "rasters with the three effects per world pair, the "
          "inversion and contamination adjudications, the "
          "exchange-formula gates; OPEN: any a-priori bound, the "
          "base law, the budget bound (r243/r247/r250/r251/r253/"
          "r254 stand); NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
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
