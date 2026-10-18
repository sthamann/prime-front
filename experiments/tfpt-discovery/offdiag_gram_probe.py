#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""offdiag_gram_probe -- PRIME.PORT.RHP.FIBER.OFFDIAG_GRAM.01
(round 254): the OFF-DIAGONAL STRUCTURE of the exact quadratic
fiber form -- the operator-level compression test that r253 left
open.  r253 put the fiber target exactly on the tau-quotient
coordinate (D = tau^aug/tau, three routes 1e-11) and measured that
the U-basis Gram DIAGONAL carries only 19 percent of the
MAIN-SCRAMBLE world gap (share_dg = 0.190953), with the WRONG SIGN
on SCRAMBLE: the gap lives in the OFF-DIAGONAL terms of the full
quadratic form.  THIS round decomposes that form spectrally and in
atom-pair bands: T = <sigma0, G sigma0> with the exact CD kernel
difference G = K_N - K_8 as a symmetric ATOM matrix
  G_{jj'} = sum_{k=8}^{N-1} sign(h_k) phat_k(u_j) phat_k(u_j'),
  phat_k = pihat_k / sqrt|h_k|   (sealed symmetrization),
and asks the one question every previous compression attempt
failed: does ANY compact carrier exist -- a small eigenspace, a
band, a sign-coherence functional -- or is the incompressibility
now measured operator-spectrally on the exact tau coordinate?

EXPLORATION ONLY (2026-08-24).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r253 discipline): w = window (kz),
N_w = builder depth, n/k = chain degree; free pivots h_{w,k}
(k < N_w) are the proof objects and legitimate KERNEL inputs (the
r248 leg-C CD compression consumes them identically); the forced
pivot h_N is NEVER formed -- the phat recursion consumes alh_k
(k <= N-2) and gam_{k+1} = rows[k]["gam_next"] (k <= N-2) ONLY;
rows[N-1]["gam_next"] is never read.  sigma0 = sigma - (F_0/h_0)
mutilde (r248, c0 = Fv[0]/hv[0]).  Ground truth (T_true = St -
S_7, flip degrees) enters GATES only; the leg-C coherence battery
(the pre-readout candidate) consumes sigma0 weights + G entries
ONLY -- no T, no gap, no flip.  No zero/prime oracles anywhere
(AST firewall).  MACHINERY IMPORTED VERBATIM: r244 BH.wpack
(rho/S/chain bitwise), r253 SP.gram_block + the U-basis center
x0 = union hull midpoint (for the sealed 19-percent
reproduction), r243 PB.smooth_comb, v881 PIK.lambda_eps controls.

LEG A -- EXACT ATOM-PAIR SPLIT (anchor): per world build
T_mat = s^T G s over the sigma0 atom union (s_j = sigma0 weights,
border block first), T_diag = sum_j s_j^2 G_jj, T_off = s^T G° s
with G° = G minus its diagonal (independent evaluation).  GATES:
(a1) T_mat vs the bitwise chain T_true: rel <= 1e-9 on MAIN
  (w9, w13; scratch-measured 7.6e-15/9.2e-14), <= 1e-4 on the
  flipped controls (SCRAMBLE/EPSTEIN; the f64 chain floor,
  r253-a1 pattern; measured 7.1e-6/4.7e-8);
(a2) BORDER ROUTE: T_bord = s_b^T G s_b with s_b = border block
  only (centering invariance, r248): mutual consistency
  |T_bord/T_mat - 1| <= 1e-9 MAIN / 1e-4 controls;
(a3) SPLIT IDENTITY: |T_diag + T_off - T_mat| <= 1e-10 x gross
  (gross = |s|^T |G| |s|); symmetry ward max|G - G^T| = 0
  (outer-product build, bar 1e-12 x max|G|);
(a4) R253 REPRODUCTION: SP.gram_block Tpair (U-basis mode
  diagonal) at the sealed x0: share_dg = (Tpair_w9 - Tpair_SCR)
  / gap_true must reproduce 0.190953 (abs tol 2e-3) and the four
  Tpair records 12.111/14.078/10.425/12.202 (rel 1e-3) -- the
  19/81 mode split is anchored, the ATOM split (this round's
  new number) is measured beside it.

LEG B -- SPECTRAL COMPRESSION (the core): eigh of the symmetric
G (rank must equal N - 8); c_k = lambda_k <s, v_k>^2; eigen-route
gate |sum c_k - T_mat| <= 1e-9 x max(|T|, 1e-2 gross).
(b1) PROFILES: per world the |c|-sorted cumulative T-shares
  (K = 1..10 printed) and K80_own = min K with |cum_K/T - 1| <=
  0.2; POOLED GAP PROFILE: pool {c_k^MAIN} u {-c_k^SCR}, sort by
  |.|, K80_pool = min K with |cum_K/gap - 1| <= 0.2.  SEALED:
  the round's spectral-compression clause fires iff K80_pool <=
  10 (verdict SPECTRAL_COMPRESSIBLE(K, share)).
(b2) WHERE do the worlds separate -- 2x2 CROSS TABLE on the
  SORTED-UNION grid (amendment a1, disclosed below: the pos/neg
  ZONE PARTITION of the window atoms is world-dependent, only
  the underlying folded-grid position SET is shared -- admission
  gate: border bitwise identical + every world's window
  positions bitwise found in the union; embedding ward T[W,sW]
  vs own-grid T_mat <= 1e-9): T[W, W'] = s_{W'}^T G_W s_{W'}.
  SHAPLEY SPLIT (two-path mean, sealed): phi_op =
  ((T[M,sM]-T[C,sM]) + (T[M,sC]-T[C,sC]))/2 / gap, phi_mass =
  1 - phi_op.  Type WORLD_SPLIT_IN_OPERATOR iff phi_op >= 0.8,
  _IN_MASS iff phi_mass >= 0.8, else _MIXED.
  LAMBDA-vs-VECTOR inside the operator move (sealed convention:
  rank-match by |lambda| DESCENDING over the first N-8
  eigenpairs, signs carried): T_lswap = sum lam^C_(k) <s_M,
  v^M_(k)>^2, T_vswap = sum lam^M_(k) <s_M, v^C_(k)>^2;
  phi_lambda = ((T[M,sM]-T_lswap) + (T_vswap-T[C,sM]))/2 /
  (T[M,sM]-T[C,sM]); OPMOVE_IN_LAMBDA iff phi_lambda >= 0.8,
  _IN_VECTOR iff <= 0.2, else _MIXED.
(b3) N-TREND: participation dimension D_part = 1/sum p_k^2,
  p_k = |c_k|/sum|c_k|, on the FULL frame-A ladder h <= 900
  (the r248 42-rung ladder; MAIN worlds, free prefix positive
  gated).  Ladder route (MAIN only, all h_k > 0): c_k =
  <u_k, P s>^2 with eigh of the small B = P P^T (R x R, R =
  N - 8) -- gated against the atom-space eigh on w9 (D_part rel
  <= 1e-6, sum c rel <= 1e-9).  Per-rung chain ward T rel <=
  1e-6.  SEALED: log-log slope of D_part vs N + Spearman:
  IPR_TREND_EXTENSIVE iff slope >= 0.5 AND sp >= 0.5;
  IPR_TREND_SATURATING iff slope <= 0.2; else IPR_TREND_MIXED.

LEG C -- BAND / SIGN ANATOMY of the off-diagonal (C° = the
off-diagonal pair matrix C_{jj'} = s_j s_j' G_{jj'}, j != j'):
(c1) DYADIC BANDS on |u_j - u_j'|: d0 = median POSITIVE
  nearest-neighbor spacing of the sorted sigma0 atoms
  (world-own; POSITIVE sealed in the smoke pass, amendment a0:
  border and window atoms share bitwise grid positions, the raw
  median is zero); band 0 = dist < d0, band m = [2^{m-1} d0,
  2^m d0); signed and absolute band sums, MAIN vs SCRAMBLE
  (EPSTEIN INFO).
(c2) CANCELLATION: coherence X = |sum C°| / sum |C°| (inverse of
  the contract's Q_offdiag) on the sealed 3-statistic battery
  {full, near = dist < 8 d0, far = rest}; sep_SCR = max over the
  battery of |log10(X_MAIN / X_SCR)|.  X consumes s and G ONLY
  (pre-readout, the r250-R4 gate, third attempt).  SEALED:
  OFFDIAG_COHERENCE_FOUND(stat, dec) iff sep_SCR >= 1.0 decade.
(c3) (p,k)-CLASSES: window atoms live on the folded cosine grid
  x = cos(2 pi uf / L); lag index uf recovered by arccos
  (admission bar 1e-9); comb contributors of lag i = atoms
  u_j = log n_j with |i D - u_j| < D (the atom_lags triangular
  spline, primary contributor = max mass x spline weight,
  sealed); n_j = round(exp(u_j)) (admission bar 1e-9 rel),
  (p, k) by integer root extraction (NO oracle -- pure integer
  arithmetic on the world's own atom data); labels are
  WORLD-BLIND (unperturbed w9 comb, disclosed).  Atom classes:
  BORDER / ARCH (no contributor) / K1 (primary k = 1) / KHI
  (primary k >= 2).  Pair classes (priority): BORDER_PAIR >
  ARCH_PAIR > SAMEP (equal primary p) > HIPOW (any KHI) > K1K1.
  Per class: pair-count share, |C|-share, signed share, MAIN vs
  SCRAMBLE; enhancement e = |C|-share / count-share.  SEALED:
  EULER_STRUCTURE_VISIBLE iff e_SAMEP >= 10 OR |log10(share^M_
  SAMEP / share^S_SAMEP)| >= 1.0; _ABSENT iff e_SAMEP <= 2 AND
  that ratio <= 0.3; else _WEAK.

LEG D -- EPSTEIN ANOMALY ADJUDICATION (r253
EPSTEIN_FIBER_ANOMALOUS, the cheap side leg):
(d1) exact-split location: share_diag_E = (T_diag_E - T_diag_M)
  / (T_E - T_M) (atom split), spectral profile of EPSTEIN, and
  the M-vs-E cross table + lambda-vs-vector split (same sealed
  machinery as b2).
(d2) MECHANISM: k_dev = first k with |gam^E_k / gam^M_k - 1| >=
  0.5 (the chain-tail deviation onset, world data, sealed bar);
  E_early = |sum_{8 <= k < k_dev} (rho^E_k - rho^M_k)| /
  |T_E - T_M| (fiber deviation carried by degrees BELOW the
  chain deviation onset -- head-region leakage).  SEALED
  ADJUDICATION: ARTEFAKT_KERNEL_COUPLING iff phi_op(M, E) >=
  0.8 AND E_early <= 0.2 AND the border-route gate (a2) holds
  on EPSTEIN (the fiber consumes the base chain ONLY through
  the kernel K_N -- coupling is trivial-mechanical);
  GENUINE_BASE_FIBER_COUPLING iff phi_mass(M, E) >= 0.5 OR
  E_early >= 0.5; else EPSTEIN_COUPLING_MIXED.

LEG E -- FALSIFIERS + MUST-FAILS (each loud, chain-predicted):
SMOOTH null control: sigma0 == 0 self-alias, |T_mat| <= 1e-9 x
gross (abs mass-norm guard, r248 pattern; flips 25/21/27 gated).
(m1) SYMMETRIZATION WRONG (sign vector dropped, G+ = P^T P on
  SCRAMBLE): shift must equal 2 sum_{k >= 8, rho_k < 0} |rho_k|
  (rel 0.05) and exceed 1e3 x the f64 noise floor 1e-13 gross;
(m2) CENTERING OMITTED on the LEVEL-N kernel: T_N(sigma_border)
  - T_N(sigma0) = rho_0 exactly (window [0.5, 2.0] x rho_0,
  r248/r251 head);
(m3) LEVEL-8 SUBTRACTION FORGOTTEN: T_N(sigma0) - T_mat = Q_7 =
  S_7 - rho_0 exactly (rel 0.05, loudness floor as m1; the MAIN
  value ~ 2e-5 is the quiet zone -- disclosed, still 1e3 x
  above the noise floor); TOP-LEVEL SHIFT [K_{N-1} - K_8]:
  moves T by exactly rho_{N-1} (rel 0.05, loud);
(m4) CROSS-TABLE SWAPPED: the lambda-swap with REVERSED rank
  matching (ascending |lambda^SCR| against descending
  |lambda^M|) must move T_lswap by >= 100 x the eigen-route
  honest deviation -- the matching convention is load-bearing.

SEALED CONSTANTS: fiber windows (9, 13); controls on w9:
EPSTEIN, SCRAMBLE (seed 1), SMOOTH; flips 25/21/27; FIB_LO 8;
trend ladder = frame-A h <= 900; bars: T MAIN 1e-9 / controls
1e-4 / trend rungs 1e-6; border route 1e-9 / 1e-4; split 1e-10
gross; sym 1e-12; eigen route 1e-9; rank = N - 8 at 1e-10
rel-lambda cut; B-route ward 1e-6 / 1e-9; r253 reproduction
share 0.190953 +- 2e-3, Tpair rel 1e-3; K80 tol 0.2, compress
Kmax 10; Shapley bars 0.8/0.8; lambda/vector bars 0.8/0.2; union
embedding ward 1e-9; IPR slope 0.5/0.2, Spearman 0.5; d0 =
median positive nn spacing, near = 8 d0, sep bar 1.0 dec; class admission 1e-9/1e-9, Euler bars
e 10/2, ratio 1.0/0.3 dec; EPSTEIN k_dev bar 0.5, E_early
0.2/0.5, op 0.8, mass 0.5; SMOOTH guard 1e-9; must-fail rel
0.05, loudness 1e3 x 1e-13 gross (m4: 100 x eigen dev); runtime
<= 1800 s; smoke = w9 MAIN only (self legs: split, spectral,
bands, classes; controls, cross, trend, EPSTEIN, world
falsifiers skipped -- no strides: the full w9 pairing runs
inside smoke).

SEALED VERDICT FORM (frozen BEFORE evaluation, priority order):
  SPECTRAL_COMPRESSIBLE(K80_pool, share)     iff K80_pool <= 10
  / OFFDIAG_COHERENCE_FOUND(stat, dec)       iff sep_SCR >= 1.0
  / OFFDIAG_EXTENSIVE_CONFIRMED              iff neither fires
      and the IPR trend is not SATURATING (then the
      incompressibility is measured operator-spectrally on the
      exact tau coordinate: mincut-relevant program finding)
  / OFFDIAG_SATURATING_UNRESOLVED            (residual case)
+ WORLD_SPLIT_IN_<OPERATOR|MASS|MIXED>(phi_op)
+ OPMOVE_IN_<LAMBDA|VECTOR|MIXED>(phi_lambda)
+ IPR_TREND_<EXTENSIVE|SATURATING|MIXED>(slope, sp)
+ EULER_STRUCTURE_<VISIBLE|WEAK|ABSENT>
+ EPSTEIN: ARTEFAKT_KERNEL_COUPLING / GENUINE_BASE_FIBER_
  COUPLING / EPSTEIN_COUPLING_MIXED.
Honesty before beauty: a SPECTRAL_COMPRESSIBLE driven by the
SCRAMBLE side alone is typed as such (per-world K80 printed);
no verdict claims a bound mechanism; the budget bound and the
base law stay OPEN (r243 PAIRCORR_REENCODED, r247 B discipline,
r250 error map, r251 error formulas, r253 tau identity stand).

RECORD TABLES (frozen from calibration pass 2, 19/19 gates,
wall 8.7 s full / 0.1 s smoke; disclosed SMOKE/CALIBRATION
AMENDMENTS -- no bar and no verdict rule ever moved:
(a0-smoke) d0 = median POSITIVE nn spacing: the smoke pass
  measured that border and window atoms share bitwise folded-
  grid positions, so the raw median spacing is exactly zero;
(a1) the cross table moved to the SORTED-UNION embedding after
  pass 1 measured that the pos/neg zone partition of the window
  atoms is world-dependent: the sealed admission gate failed
  LOUDLY as designed (raw concat-order pairing gave the garbage
  value T[M,sSCR] = +1.23e6); the position SET is bitwise
  shared (|U| = 367, embedding ward 9.8e-15), the Shapley rule
  itself never moved):
CAL_VERDICT = OFFDIAG_EXTENSIVE_CONFIRMED +
WORLD_SPLIT_IN_OPERATOR(phi_op=1.12) +
OPMOVE_IN_LAMBDA(phi_lambda=14.45) +
IPR_TREND_EXTENSIVE(slope=0.95, sp=0.96) +
EULER_STRUCTURE_WEAK + EPSTEIN: ARTEFAKT_KERNEL_COUPLING.
Key numbers.  CENSUS: w9/w13 N = 184/168, A = 734/670 (border
367/335), T_true +4.3343/+4.1449; SCR -4.4942 (gap 8.8285),
EPST +0.7615; flips 25/21/27; ladder 42 rungs, N in [142, 878],
all free-prefix positive.  LEG A: T_mat vs chain 7.5e-15 (w9) /
9.1e-14 (w13) / 7.1e-6 (SCR, f64 chain floor) / 4.7e-8 (EPST);
border route mutual 9.1e-15 / 6.8e-6 / 8.7e-10; split identity
1.8e-17 gross; symmetry dev EXACTLY 0; Tpair reproduction
12.1107/14.0777/10.4248/12.2019 (worst rel 2.7e-5), share_dg =
0.190953 (r253 record hit exactly).  ATOM SPLIT (the round's
new anchor): T_diag +7.7050/+7.9634 (w9/w13), SCR +0.7635,
EPST +4.4259; T_off -3.3707/-3.8185/-5.2576/-3.6644; ATOM-diag
gap share 0.786, ATOM-off share 0.214 -- the atom diagonal is
the mode-space MIRROR (mode diag carries 19 percent, atom diag
79 percent; each single-index compression leaves the
complementary 4/5 resp. 1/5 in genuine pair structure).
LEG B (the round's headline): eigen route 1.6e-11, rank = N-8
exact on 4/4; per-world profiles -- MAIN w9 EXTENSIVE (top-10
T-share 0.492, K80_own 28, D_part 30.2 of 176; w13 alike:
0.515/30/29.5), SCRAMBLE COMPACT (K80_own = 2, top-1 share
1.418, D_part 4.3), EPSTEIN semi-compact (K80_own 6, D_part
8.0): the arithmetic-destroying surgery CONCENTRATES the
quadratic form onto ~2 eigendirections while MAIN spreads it
over ~30; POOLED GAP profile: top-1 share 0.722, then
oscillating (0.543..0.634 through K = 10), K80_pool = 20 > 10
=> NO compact carrier at the sealed Kmax --
SPECTRAL_COMPRESSIBLE does NOT fire (the near-compression sits
entirely on the SCRAMBLE side; MAIN stays extensive).  CROSS
TABLE (union grid): SCR: T[M,sM] +4.3343, T[M,sS] +9.9756,
T[S,sM] -0.9276, T[S,sS] -4.4941 -> phi_op = 1.118, phi_mass =
-0.118 => WORLD_SPLIT_IN_OPERATOR (the kernel/chain change
carries the world gap; the mass move alone OVERSHOOTS to +9.98
-- strong anti-correlated interaction, printed); lambda-vs-
vector: T_lswap +1.1607, T_vswap +147.95, phi_lambda = 14.45
=> the sealed >= 0.8 clause fires OPMOVE_IN_LAMBDA, with the
HONESTY NOTE (typed, no upgrade): the value sits far outside
[0, 1] -- the lambda/vector split is strongly NON-ADDITIVE
(swapping the frame alone explodes the form to +148): the
token reads 'the operator move does not survive the eigenvalue
swap', NOT 'a clean 100-percent lambda channel'.  IPR TREND
(42 rungs): D_part 24.9 .. 171.8, median D_part/(N-8) = 0.195,
log-log slope +0.95, Spearman +0.96 => IPR_TREND_EXTENSIVE:
the MAIN participation dimension grows ~ 0.2 N linearly --
r246/r248 extensivity now measured OPERATOR-SPECTRALLY on the
exact tau coordinate; chain ward 1.9e-11, B-route vs atom-eigh
4.1e-10.  LEG C: d0 = 6.07e-3; band tables printed (10 dyadic
bands; MAIN |C|-shares flat 0.163..0.077 with band-0 dominant,
SCRAMBLE shifts mass to mid bands 4-6 (0.155/0.218/0.121),
EPSTEIN to far bands 5-8 (max 0.247)); coherence battery X
(pre-readout): MAIN {full 3.62e-2, near 6.59e-2, far 6.40e-3},
SCR {1.64e-2, 3.63e-2, 6.50e-3} -> sep_SCR = 0.345 dec on
X_full < 1.0 => NO OFFDIAG_COHERENCE_FOUND (the r250-R4
pre-readout gate fails a THIRD time, honest) -- and the
DIRECTION is INVERTED: MAIN is LESS cancelled than SCRAMBLE
(X_full 3.6e-2 vs 1.6e-2), the 'MAIN systematically
extinguished' hypothesis fails in its sign; EPST sep 1.206 dec
(INFO: the EPSTEIN off-diagonal is 10x MORE cancelled than
MAIN -- the r253 anomaly reappears as a cancellation excess).
(p,k) CLASSES (world-blind labels; 367 window atoms = 256 ARCH
+ 90 K1 + 21 KHI; SAMEP count share 4.2e-4): |C|-shares MAIN:
BORDER_PAIR 0.806, ARCH_PAIR 0.160, K1K1 0.0219, HIPOW 0.0086,
SAMEP 3.74e-3 => e_SAMEP = 8.9 (just below the sealed VISIBLE
bar 10), M/S SAMEP share ratio 0.365 dec (between 0.3 and 1.0)
=> EULER_STRUCTURE_WEAK: same-p pairs carry ~ 9x their
combinatorial weight on MAIN and lose 0.37 dec under scramble
-- a weak but real Euler trace, below both sealed
visibility bars.  LEG D (EPSTEIN): T_E +0.7615 (dT -3.5728);
atom split T_diag_E +4.4259 => share_diag_E = 0.918: the
EPSTEIN deviation is DIAGONAL-heavy (OPPOSITE of SCRAMBLE,
whose gap is 79 percent diagonal too but with inverted
coherence); k_dev = 24 (first 50-percent gammahat deviation --
consistent with the flip at 25 WITHOUT reading it), E_early =
1.0e-6 (the head region k < 24 is fiber-silent EXACTLY as the
head-identical construction demands); cross M/E: T[M,sE]
+12.3502, T[E,sM] -0.8561 -> phi_op = 2.348, phi_mass =
-1.348, border route on EPST 8.7e-10 =>
ARTEFAKT_KERNEL_COUPLING by the sealed rule: the EPSTEIN fiber
anomaly is the kernel K_N consuming the perturbed gammahat
tail -- trivial-mechanical base->fiber coupling through the
chain, NOT a new layer (r252's orientation problem and the
fiber are the SAME layer seen through the kernel; phi_lambda
8.99 INFO, same non-additivity note).  FALSIFIERS: SMOOTH
|T|/gross = 4.6e-19 (bar 1e-9); m1 sign-drop (SCR) shift
+6594.1222 vs predicted +6594.1227 (rel 7.4e-8, 2.0e14 x
floor); m2 centering rho_0 ratio 1.0000 in [0.5, 2.0]; m3
level-8 forgotten dev 2.2e-11 rel Q_7 = 1.981e-5 (2.0e6 x
floor, quiet-zone disclosure), top-level shift vs rho_{N-1}
rel 2.7e-14 (1.5e10 x); m4 reversed lambda-matching moves
T_lswap by 2442 = 3.5e13 x the eigen dev.  READING (typed, no
upgrade): the compression question is now CLOSED on the
operator level -- the exact fiber form has NO compact spectral
carrier (K80_pool 20), NO pre-readout coherence separation
(0.345 dec, sign inverted), a linearly growing participation
dimension (0.2 N), and only a weak sub-bar Euler trace: the
incompressibility of the prime-pairing information is for the
first time measured OPERATOR-SPECTRALLY on the exact tau
coordinate (mincut-relevant program finding); the one
concentrated object is the SURGERY side (SCRAMBLE collapses
onto 2 eigendirections; EPSTEIN onto 6) -- arithmetic worlds
are spectrally spread, broken worlds are spectrally compact.
Runtime 8.7 s full, 0.1 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE.

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
import port_integrable_kernel_probe as PIK   # noqa: E402 v881
import principal_bessel_probe as PB          # noqa: E402 r243
import schlesinger_pairing_probe as SP       # noqa: E402 r253
import v563_paper2_readouts as core          # noqa: E402 READ-ONLY

FIB_WINDOWS = (9, 13)
FIB_LO = 8
TREND_HCAP = 900
T_MAIN_BAR = 1e-9
T_CTRL_BAR = 1e-4
T_TREND_BAR = 1e-6
BORD_MAIN_BAR = 1e-9
BORD_CTRL_BAR = 1e-4
SPLIT_BAR = 1e-10
SYM_BAR = 1e-12
EIG_ROUTE_BAR = 1e-9
RANK_CUT = 1e-10
BROUTE_DPART_BAR = 1e-6
BROUTE_SUM_BAR = 1e-9
EMB_BAR = 1e-9
SHARE_DG_REF = 0.190953
SHARE_DG_TOL = 2e-3
TPAIR_REF = {"w9": 12.111, "w13": 14.078, "SCR": 10.425,
             "EPST": 12.202}
TPAIR_TOL = 1e-3
K80_TOL = 0.2
COMPRESS_KMAX = 10
KSHOW = 10
SHAP_OP_BAR = 0.8
SHAP_MASS_BAR = 0.8
LAM_HI, LAM_LO = 0.8, 0.2
IPR_SLOPE_EXT = 0.5
IPR_SLOPE_SAT = 0.2
IPR_SP_BAR = 0.5
NEAR_D0 = 8.0
SEP_DEC_BAR = 1.0
NINT_BAR = 1e-9
UF_BAR = 1e-9
EULER_E_HI, EULER_E_LO = 10.0, 2.0
EULER_R_HI, EULER_R_LO = 1.0, 0.3
KDEV_BAR = 0.5
EARLY_ART_BAR = 0.2
EARLY_GEN_BAR = 0.5
EPST_OP_BAR = 0.8
EPST_MASS_BAR = 0.5
SM_GUARD = 1e-9
MF_REL = 0.05
MF_LOUD = 1e3
MF_NOISE = 1e-13
M4_LOUD = 100.0
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
CAL_VERDICT = (
    "OFFDIAG_EXTENSIVE_CONFIRMED + "
    "WORLD_SPLIT_IN_OPERATOR(phi_op=1.12) + "
    "OPMOVE_IN_LAMBDA(phi_lambda=14.45) + "
    "IPR_TREND_EXTENSIVE(slope=0.95, sp=0.96) + "
    "EULER_STRUCTURE_WEAK + EPSTEIN: ARTEFAKT_KERNEL_COUPLING")

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
    return (not bad), ("NO zero/prime oracles; the kernel consumes "
                       "the FREE chain (alh_k, gam_{k+1}, sign h_k, "
                       "k <= N-2) + atom positions/weights ONLY; "
                       "rows[N-1]['gam_next'] (the forced pivot) is "
                       "never read; T_true/flips enter gates only; "
                       "the leg-C battery is pre-readout (s, G "
                       "only); (p,k) labels come from integer root "
                       "extraction on the world's own atom data"
                       if not bad else "; ".join(bad))


# ------------------------------------------------ normalized chain
def phat_matrix(rows, nodes, n_hi):
    """phat_k(nodes) = pihat_k(nodes)/sqrt|h_k| for k = 0..n_hi-1
    via the sign-carried normalized three-term recursion; consumes
    alh_k (k <= n_hi-2) and gam_{k+1} = rows[k]['gam_next']
    (k <= n_hi-2) only -- the forced pivot gam at rows[n_hi-1] is
    NEVER read."""
    P = np.empty((n_hi, len(nodes)))
    h0 = rows[0]["sg_h"] * math.exp(rows[0]["lg_h"])
    P[0] = 1.0 / math.sqrt(abs(h0))
    if n_hi > 1:
        P[1] = (nodes - rows[0]["alh"]) * P[0] \
            / math.sqrt(abs(rows[0]["gam_next"]))
    for k in range(1, n_hi - 1):
        gk = rows[k - 1]["gam_next"]
        gk1 = rows[k]["gam_next"]
        P[k + 1] = ((nodes - rows[k]["alh"]) * P[k]
                    - math.copysign(math.sqrt(abs(gk)), gk)
                    * P[k - 1]) / math.sqrt(abs(gk1))
    return P


def world_build(p, want_P=False):
    """sigma0 atoms, weights, the exact CD-difference kernel as a
    symmetric atom matrix, and the split/route readouts."""
    d, dsm = p["d"], p["dsm"]
    N = p["N"]
    bx = np.concatenate([dsm["xs"], dsm["ys"]])
    bw = np.concatenate([dsm["ws"], -dsm["vs"]])
    wx = np.concatenate([d["xs"], d["ys"]])
    wu = np.concatenate([d["ws"], -d["vs"]])
    c0 = p["Fv"][0] / p["hv"][0]
    pos = np.concatenate([bx, wx])
    s = np.concatenate([bw, -c0 * wu])
    sg = np.array([p["rows"][k]["sg_h"] for k in range(N)])
    P = phat_matrix(p["rows"], pos, N)
    G = (P[FIB_LO:N].T * sg[FIB_LO:N]) @ P[FIB_LO:N]
    G8 = (P[:FIB_LO].T * sg[:FIB_LO]) @ P[:FIB_LO]
    sym_dev = float(np.max(np.abs(G - G.T)))
    T_true = p["St"] - float(p["S"][FIB_LO - 1])
    Gs = G @ s
    T_mat = float(s @ Gs)
    s_b = s.copy()
    s_b[len(bx):] = 0.0
    T_bord = float(s_b @ (G @ s_b))
    dG = np.diag(G).copy()
    T_diag = float((s * s) @ dG)
    Go = G.copy()
    np.fill_diagonal(Go, 0.0)
    T_off = float(s @ (Go @ s))
    gross = float(np.abs(s) @ (np.abs(G) @ np.abs(s)))
    out = dict(p=p, N=N, A=len(pos), nb=len(bx), pos=pos, s=s,
               s_b=s_b, c0=c0, G=G, G8=G8, sym_dev=sym_dev,
               T_true=T_true, T_mat=T_mat, T_bord=T_bord,
               T_diag=T_diag, T_off=T_off, gross=gross, wx=wx,
               wu=wu, bx=bx, bw=bw, dG=dG)
    if want_P:
        out["P"] = P
        out["sgv"] = sg
    del Go
    return out


def eig_block(W):
    lam, V = np.linalg.eigh(W["G"])
    proj = V.T @ W["s"]
    c = lam * proj * proj
    rank = int(np.sum(np.abs(lam)
                      > RANK_CUT * float(np.max(np.abs(lam)))))
    dev = abs(float(np.sum(c)) - W["T_mat"]) \
        / max(abs(W["T_mat"]), 1e-2 * W["gross"])
    W["lam"], W["V"], W["c"] = lam, V, c
    W["rank"], W["eig_dev"] = rank, dev
    return W


def profile_stats(c, denom):
    o = np.argsort(-np.abs(c))
    cs = np.cumsum(c[o])
    shares = cs / denom
    k80 = None
    for k in range(len(c)):
        if abs(shares[k] - 1.0) <= K80_TOL:
            k80 = k + 1
            break
    pk = np.abs(c) / max(float(np.sum(np.abs(c))), 1e-300)
    dpart = 1.0 / float(np.sum(pk * pk))
    return shares, (k80 if k80 is not None else len(c) + 1), dpart


def band_stats(W):
    pos = W["pos"]
    srt = np.sort(pos)
    dfs = np.diff(srt)
    d0 = float(np.median(dfs[dfs > 0.0]))
    Dm = np.abs(pos[:, None] - pos[None, :])
    C = (W["s"][:, None] * W["s"][None, :]) * W["G"]
    np.fill_diagonal(C, 0.0)
    off = ~np.eye(len(pos), dtype=bool)
    with np.errstate(divide="ignore"):
        bidx = np.where(Dm < d0, 0,
                        np.floor(np.log2(np.maximum(Dm / d0, 1.0))
                                 ).astype(np.int64) + 1)
    nb = int(bidx[off].max()) + 1
    sgn = np.bincount(bidx[off], weights=C[off], minlength=nb)
    ab = np.bincount(bidx[off], weights=np.abs(C[off]), minlength=nb)
    near = off & (Dm < NEAR_D0 * d0)
    far = off & ~ (Dm < NEAR_D0 * d0)

    def coh(mask):
        aa = float(np.sum(np.abs(C[mask])))
        return abs(float(np.sum(C[mask]))) / max(aa, 1e-300)

    X = dict(full=coh(off), near=coh(near), far=coh(far))
    return dict(d0=d0, sgn=sgn, ab=ab, X=X, C=C, Dm=Dm, off=off)


def base_exp(n):
    """(p, k) of a perfect power by pure integer root extraction
    (no oracle: the comb atoms ARE p^k by construction)."""
    n = int(n)
    if n < 4:
        return n, 1
    for m in range(int(math.log2(n)), 1, -1):
        b = int(round(n ** (1.0 / m)))
        for bb in (b - 1, b, b + 1):
            if bb >= 2 and bb ** m == n:
                return bb, m
    return n, 1


def atom_classes(W, uu, mm, M, D, L):
    """world-blind (p,k) labels of the sigma0 atoms: BORDER=0,
    ARCH=1, K1=2, KHI=3; primary p in pst (0 if none)."""
    A = W["A"]
    nb = W["nb"]
    cls = np.zeros(A, dtype=np.int64)
    pst = np.zeros(A, dtype=np.int64)
    nn = np.round(np.exp(uu)).astype(np.int64)
    dev_n = float(np.max(np.abs(np.exp(uu) - nn) / nn))
    pk = [base_exp(n) for n in nn]
    wpos = W["pos"][nb:]
    th = np.arccos(np.clip(wpos, -1.0, 1.0)) * L / (2.0 * math.pi)
    dev_uf = float(np.max(np.abs(th - np.round(th))))
    lag = np.round(th).astype(np.int64)
    order = np.argsort(uu)
    uus = uu[order]
    for j in range(A - nb):
        si = lag[j] * D
        lo = int(np.searchsorted(uus, si - D, side="right"))
        hi = int(np.searchsorted(uus, si + D, side="left"))
        best_w, best = -1.0, None
        for t in range(lo, hi):
            jj = int(order[t])
            v = 1.0 - abs(si - uu[jj]) / D
            if v > 0.0 and abs(mm[jj]) * v > best_w:
                best_w, best = abs(mm[jj]) * v, jj
        if best is None:
            cls[nb + j] = 1
        else:
            pp, kk = pk[best]
            cls[nb + j] = 2 if kk == 1 else 3
            pst[nb + j] = pp
    return cls, pst, dev_n, dev_uf


def pair_class_table(W, cls, pst, bs):
    """pair classes on the off-diagonal (priority BORDER > ARCH >
    SAMEP > HIPOW > K1K1); returns per-class (count share,
    |C| share, signed share of T_off)."""
    C, off = bs["C"], bs["off"]
    ci, cj = cls[:, None], cls[None, :]
    anyB = (ci == 0) | (cj == 0)
    anyA = (ci == 1) | (cj == 1)
    samep = (pst[:, None] == pst[None, :]) & (pst[:, None] > 0)
    anyH = (ci == 3) | (cj == 3)
    code = np.select([anyB, anyA, samep, anyH],
                     [0, 1, 2, 3], default=4)
    tot_n = float(np.sum(off))
    tot_a = float(np.sum(np.abs(C[off])))
    T_off = float(np.sum(C[off]))
    tab = {}
    for cid, name in ((0, "BORDER_PAIR"), (1, "ARCH_PAIR"),
                      (2, "SAMEP"), (3, "HIPOW"), (4, "K1K1")):
        m = off & (code == cid)
        tab[name] = (float(np.sum(m)) / tot_n,
                     float(np.sum(np.abs(C[m]))) / max(tot_a, 1e-300),
                     float(np.sum(C[m])) / max(abs(T_off), 1e-300)
                     * math.copysign(1.0, T_off))
    return tab


def shapley(T_MM, T_MC, T_CM, T_CC):
    gap = T_MM - T_CC
    phi_op = 0.5 * ((T_MM - T_CM) + (T_MC - T_CC)) \
        / (gap if gap != 0 else 1e-300)
    return gap, phi_op, 1.0 - phi_op


def cross_block(Wm, Wc):
    """2x2 cross table on the SORTED UNION grid (amendment a1:
    the positive/negative ZONE PARTITION of the window atoms is
    world-dependent, so the raw concat order is not shareable;
    the underlying folded-grid position SET is -- admission
    gated).  Embeds each world's sigma0 weights on the union,
    builds each world's kernel at the union positions, evaluates
    all four quadratic forms + the lambda/vector swaps."""
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
    GU = {}
    for key, W in (("M", Wm), ("C", Wc)):
        PU = phat_matrix(W["p"]["rows"], posU, W["N"])
        GU[key] = (PU[FIB_LO:W["N"]].T * W["sgv"][FIB_LO:W["N"]]) \
            @ PU[FIB_LO:W["N"]]
    T_MM = float(sM @ (GU["M"] @ sM))
    T_MC = float(sC @ (GU["M"] @ sC))
    T_CM = float(sM @ (GU["C"] @ sM))
    T_CC = float(sC @ (GU["C"] @ sC))
    emb_dev = max(abs(T_MM / Wm["T_mat"] - 1.0),
                  abs(T_CC / Wc["T_mat"] - 1.0))
    gap, phi_op, phi_ms = shapley(T_MM, T_MC, T_CM, T_CC)
    R = Wm["N"] - FIB_LO
    lamMf, VMf = np.linalg.eigh(GU["M"])
    lamCf, VCf = np.linalg.eigh(GU["C"])
    oM = np.argsort(-np.abs(lamMf))[:R]
    oC = np.argsort(-np.abs(lamCf))[:R]
    lamM, VM = lamMf[oM], VMf[:, oM]
    lamC, VC = lamCf[oC], VCf[:, oC]
    pM = VM.T @ sM
    pC = VC.T @ sM
    T_lswap = float(np.sum(lamC * pM * pM))
    T_vswap = float(np.sum(lamM * pC * pC))
    opmove = T_MM - T_CM
    phi_lam = 0.5 * ((T_MM - T_lswap) + (T_vswap - T_CM)) \
        / (opmove if opmove != 0 else 1e-300)
    return dict(T_MM=T_MM, T_MC=T_MC, T_CM=T_CM, T_CC=T_CC,
                gap=gap, phi_op=phi_op, phi_ms=phi_ms,
                T_lswap=T_lswap, T_vswap=T_vswap, phi_lam=phi_lam,
                ok_pos=ok_pos, emb_dev=emb_dev, lamC=lamC, pM=pM,
                nU=len(U))


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("offdiag_gram_probe -- PRIME.PORT.RHP.FIBER."
          "OFFDIAG_GRAM.01 (round 254)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 MAIN self legs only; controls, "
                        "cross, trend, EPSTEIN, world falsifiers "
                        "skipped; NO strides -- the full pairing "
                        "runs)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "kernel G_{jj'} = sum_{k=8}^{N-1} sign(h_k) phat_k(u_j) "
          "phat_k(u_j') (sealed symmetrization phat = pihat/"
          "sqrt|h|); split T = T_diag + T_off gated at %.0e gross; "
          "T-vs-chain bars %.0e MAIN / %.0e controls; eigen route "
          "%.0e, rank = N-8; K80 tol %.1f, compress Kmax %d; "
          "Shapley bars %.1f; lambda/vector %.1f/%.1f; IPR ladder "
          "h <= %d, slope bars %.1f/%.1f, sp %.1f; coherence "
          "battery {full, near < %.0f d0, far}, sep bar %.1f dec "
          "(pre-readout); Euler bars e %.0f/%.0f, ratio %.1f/%.1f "
          "dec; EPSTEIN k_dev bar %.1f, E_early %.1f/%.1f, op "
          "%.1f, mass %.1f; ALL verdict rules sealed BEFORE "
          "evaluation; fiber windows %s + controls on w9"
          % (SPLIT_BAR, T_MAIN_BAR, T_CTRL_BAR, EIG_ROUTE_BAR,
             K80_TOL, COMPRESS_KMAX, SHAP_OP_BAR, LAM_HI, LAM_LO,
             TREND_HCAP, IPR_SLOPE_EXT, IPR_SLOPE_SAT, IPR_SP_BAR,
             NEAR_D0, SEP_DEC_BAR, EULER_E_HI, EULER_E_LO,
             EULER_R_HI, EULER_R_LO, KDEV_BAR, EARLY_ART_BAR,
             EARLY_GEN_BAR, EPST_OP_BAR, EPST_MASS_BAR,
             str(FIB_WINDOWS)))

    # ---------------- S1: census + controls
    section("S1  CENSUS + CONTROLS")
    windows = (9,) if smoke else FIB_WINDOWS
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    ctrl = {}
    if not smoke:
        rr9c = core.build_window(9)
        N_E = int(math.floor(math.exp(2.0 * rr9c["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ug9, uw9 = PB.smooth_comb(rr9c["alpha"])
        ctrl_defs = (("EPSTEIN", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCRAMBLE", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=(ug9, uw9))))
        ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl) \
        if ctrl else True
    tt = "; ".join("%s: N=%d T_true=%+.4f"
                   % (t, p["N"],
                      p["St"] - float(p["S"][FIB_LO - 1]))
                   for t, p in packs.items())
    check("G10-census-controls", okC and okCf,
          "free prefix positive on %d/%d MAIN windows; %s; control "
          "flips re-derived %s"
          % (sum(1 for t in packs if packs[t]["nf"] is None),
             len(packs), tt,
             str({c: ctrl[c]["nf"] for c in ctrl}) if ctrl
             else "SMOKE-skipped"))

    # ---------------- S2: LEG A -- exact atom-pair split
    section("S2  LEG A -- EXACT ATOM-PAIR SPLIT (anchor)")
    Wd = {}
    world_list = list(packs.items())
    if not smoke:
        world_list += [("SCR", ctrl["SCRAMBLE"]),
                       ("EPST", ctrl["EPSTEIN"])]
    t_main = t_ctrl = 0.0
    b_main = b_ctrl = 0.0
    split_worst = sym_worst = 0.0
    for tag, p in world_list:
        W = world_build(p, want_P=(tag in ("w9", "SCR", "EPST")))
        Wd[tag] = W
        devT = abs(W["T_mat"] / W["T_true"] - 1.0)
        devB = abs(W["T_bord"] / W["T_mat"] - 1.0)
        if tag in packs:
            t_main = max(t_main, devT)
            b_main = max(b_main, devB)
        else:
            t_ctrl = max(t_ctrl, devT)
            b_ctrl = max(b_ctrl, devB)
        split_worst = max(split_worst,
                          abs(W["T_diag"] + W["T_off"] - W["T_mat"])
                          / max(W["gross"], 1e-300))
        sym_worst = max(sym_worst, W["sym_dev"]
                        / max(float(np.max(np.abs(W["G"]))), 1e-300))
        info("%-5s N=%d A=%d (border %d)  T_true %+.4f  T_mat dev "
             "%.1e  bord dev %.1e | T_diag %+.4f  T_off %+.4f  "
             "gross %.3g"
             % (tag, W["N"], W["A"], W["nb"], W["T_true"], devT,
                devB, W["T_diag"], W["T_off"], W["gross"]))
    check("G20-kernel-chain-routes",
          t_main <= T_MAIN_BAR and t_ctrl <= T_CTRL_BAR
          and b_main <= BORD_MAIN_BAR and b_ctrl <= BORD_CTRL_BAR
          and split_worst <= SPLIT_BAR and sym_worst <= SYM_BAR,
          "T_mat = s^T G s vs the bitwise chain: MAIN worst %.1e "
          "(bar %.0e), controls %.1e (floor bar %.0e); border "
          "route (centering invariance) mutual %.1e / %.1e; split "
          "identity %.1e gross (bar %.0e); symmetry %.1e (bar "
          "%.0e) -- the exact CD-difference kernel is implemented "
          "as a symmetric atom matrix at FULL depth"
          % (t_main, T_MAIN_BAR, t_ctrl, T_CTRL_BAR, b_main,
             b_ctrl, split_worst, SPLIT_BAR, sym_worst, SYM_BAR))
    tp = {}
    tp_worst = 0.0
    for tag in (list(packs) + (["SCR", "EPST"] if not smoke
                               else [])):
        p = Wd[tag]["p"]
        N = p["N"]
        xu = np.sort(np.concatenate([p["d"]["xs"], p["d"]["ys"]]))
        x0 = 0.5 * (float(xu[0]) + float(xu[-1]))
        B = float(p["S"][N - 2]) + 5.0 / 7.0
        gb = SP.gram_block(p, x0, N, B)
        tp[tag] = gb["Tpair"]
        ref = TPAIR_REF.get(tag)
        if ref is not None:
            tp_worst = max(tp_worst, abs(gb["Tpair"] / ref - 1.0))
    if not smoke:
        gap_true = Wd["w9"]["T_true"] - Wd["SCR"]["T_true"]
        share_dg = (tp["w9"] - tp["SCR"]) / gap_true
        ok_dg = abs(share_dg - SHARE_DG_REF) <= SHARE_DG_TOL
        dshare = (Wd["w9"]["T_diag"] - Wd["SCR"]["T_diag"]) \
            / gap_true
        check("G21-r253-reproduction",
              ok_dg and tp_worst <= TPAIR_TOL,
              "SP.gram_block Tpair %s -- share_dg = %.6f (r253 "
              "record %.6f, tol %.0e), Tpair worst rel %.1e (tol "
              "%.0e): the 19/81 MODE split reproduced; NEW ATOM "
              "split: diag gap share %.3f, OFF-diag gap share "
              "%.3f (the atom diagonal is the mode-space mirror)"
              % (str({t: round(v, 4) for t, v in tp.items()}),
                 share_dg, SHARE_DG_REF, SHARE_DG_TOL, tp_worst,
                 TPAIR_TOL, dshare, 1.0 - dshare))
    else:
        check("G21-r253-reproduction", tp_worst <= TPAIR_TOL,
              "SMOKE: Tpair w9 %.4f (rel %.1e vs r253 record); "
              "share_dg needs SCRAMBLE (skipped)"
              % (tp["w9"], tp_worst))

    # ---------------- S3: LEG B -- spectral compression
    section("S3  LEG B -- SPECTRAL COMPRESSION")
    eig_worst = 0.0
    rank_ok = True
    for tag in Wd:
        W = eig_block(Wd[tag])
        eig_worst = max(eig_worst, W["eig_dev"])
        rank_ok = rank_ok and (W["rank"] == W["N"] - FIB_LO)
    check("G30-eigen-route", eig_worst <= EIG_ROUTE_BAR and rank_ok,
          "eigh(G): |sum c_k - T_mat| worst %.1e (bar %.0e); rank "
          "= N - 8 on %d/%d worlds (cut %.0e rel-lambda) -- T = "
          "sum_k lambda_k <sigma0, v_k>^2 exact"
          % (eig_worst, EIG_ROUTE_BAR,
             sum(1 for t in Wd
                 if Wd[t]["rank"] == Wd[t]["N"] - FIB_LO),
             len(Wd), RANK_CUT))
    prof = {}
    for tag in Wd:
        W = Wd[tag]
        shares, k80, dpart = profile_stats(W["c"], W["T_mat"])
        prof[tag] = (shares, k80, dpart)
        info("%-5s top-K T-share (K=1..%d): %s | K80_own %s  "
             "D_part %.1f (of %d)"
             % (tag, KSHOW,
                " ".join("%.3f" % v for v in shares[:KSHOW]),
                str(k80), dpart, W["rank"]))
    if not smoke:
        pool = np.concatenate([Wd["w9"]["c"], -Wd["SCR"]["c"]])
        gshares, k80_pool, _dp = profile_stats(pool, gap_true)
        share_at = float(gshares[min(k80_pool, len(pool)) - 1])
        compress = k80_pool <= COMPRESS_KMAX
        check("G31-gap-spectral-profile", True,
              "POOLED GAP profile ({c^MAIN} u {-c^SCR}, gap "
              "%+.4f): top-K shares %s -> K80_pool = %s (share "
              "%.3f, tol %.1f) => %s; honesty: per-world K80_own "
              "MAIN %s vs SCR %s -- the compression location is "
              "printed, not hidden"
              % (gap_true,
                 " ".join("%.3f" % v for v in gshares[:KSHOW]),
                 str(k80_pool), share_at, K80_TOL,
                 "SPECTRAL_COMPRESSIBLE(K=%d)" % k80_pool
                 if compress else "no compact carrier (K80 > %d)"
                 % COMPRESS_KMAX, str(prof["w9"][1]),
                 str(prof["SCR"][1])))
    else:
        compress, k80_pool, share_at = False, None, float("nan")
        check("G31-gap-spectral-profile", True,
              "SMOKE: pooled gap profile skipped (needs SCRAMBLE)")
    # cross tables
    cross = {}
    if not smoke:
        emb_worst = 0.0
        for ct in ("SCR", "EPST"):
            cb = cross_block(Wd["w9"], Wd[ct])
            cross[ct] = cb
            emb_worst = max(emb_worst, cb["emb_dev"])
            info("%-5s cross (union grid, %d window positions): "
                 "T[M,sM] %+.4f  T[M,s%s] %+.4f  T[%s,sM] %+.4f  "
                 "T[%s,s%s] %+.4f | phi_op %.3f  phi_mass %.3f | "
                 "T_lswap %+.4f  T_vswap %+.4f  phi_lambda %.3f"
                 % (ct, cb["nU"], cb["T_MM"], ct, cb["T_MC"], ct,
                    cb["T_CM"], ct, ct, cb["T_CC"], cb["phi_op"],
                    cb["phi_ms"], cb["T_lswap"], cb["T_vswap"],
                    cb["phi_lam"]))
        cs = cross["SCR"]
        if cs["phi_op"] >= SHAP_OP_BAR:
            v_split = "WORLD_SPLIT_IN_OPERATOR(phi_op=%.2f)" \
                % cs["phi_op"]
        elif cs["phi_ms"] >= SHAP_MASS_BAR:
            v_split = "WORLD_SPLIT_IN_MASS(phi_mass=%.2f)" \
                % cs["phi_ms"]
        else:
            v_split = "WORLD_SPLIT_MIXED(%.2f/%.2f)" \
                % (cs["phi_op"], cs["phi_ms"])
        if cs["phi_lam"] >= LAM_HI:
            v_lam = "OPMOVE_IN_LAMBDA(phi_lambda=%.2f)" \
                % cs["phi_lam"]
        elif cs["phi_lam"] <= LAM_LO:
            v_lam = "OPMOVE_IN_VECTOR(phi_lambda=%.2f)" \
                % cs["phi_lam"]
        else:
            v_lam = "OPMOVE_IN_MIXED(phi_lambda=%.2f)" \
                % cs["phi_lam"]
        check("G32-cross-table",
              cross["SCR"]["ok_pos"] and cross["EPST"]["ok_pos"]
              and emb_worst <= EMB_BAR,
              "admission: sorted-union embedding (amendment a1: "
              "the pos/neg ZONE PARTITION is world-dependent, "
              "the position SET is bitwise shared) -- union "
              "T[W,sW] vs own-grid T_mat worst %.1e (bar %.0e); "
              "2x2 Shapley split (sealed two-path mean): %s + %s "
              "-- the interaction (mass move alone T[M,sSCR] = "
              "%+.3f vs T_MM %+.3f) is printed, not averaged "
              "away silently"
              % (emb_worst, EMB_BAR, v_split, v_lam,
                 cross["SCR"]["T_MC"], cross["SCR"]["T_MM"]))
    else:
        v_split = v_lam = "CROSS_SMOKE_NA"
        check("G32-cross-table", True, "SMOKE: skipped")
    # IPR N-trend ladder
    if not smoke:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= TREND_HCAP]
        Ns, dps = [], []
        tw = 0.0
        okL = True
        for kz in kzs:
            pL = BH.wpack(kz)
            okL = okL and (pL["nf"] is None)
            d, dsm = pL["d"], pL["dsm"]
            NL = pL["N"]
            bxL = np.concatenate([dsm["xs"], dsm["ys"]])
            bwL = np.concatenate([dsm["ws"], -dsm["vs"]])
            wxL = np.concatenate([d["xs"], d["ys"]])
            wuL = np.concatenate([d["ws"], -d["vs"]])
            c0L = pL["Fv"][0] / pL["hv"][0]
            posL = np.concatenate([bxL, wxL])
            sL = np.concatenate([bwL, -c0L * wuL])
            PL = phat_matrix(pL["rows"], posL, NL)[FIB_LO:NL]
            Bm = PL @ PL.T
            w = PL @ sL
            lamB, UB = np.linalg.eigh(Bm)
            cB = (UB.T @ w) ** 2
            T_tr = pL["St"] - float(pL["S"][FIB_LO - 1])
            tw = max(tw, abs(float(np.sum(cB)) / T_tr - 1.0))
            pkB = cB / max(float(np.sum(cB)), 1e-300)
            dps.append(1.0 / float(np.sum(pkB * pkB)))
            Ns.append(NL)
        # B-route ward vs the atom eigh on w9
        i9 = kzs.index(9) if 9 in kzs else None
        ward_ok = True
        ward_txt = "w9 not in ladder"
        if i9 is not None:
            dp_atom = prof["w9"][2]
            ward = abs(dps[i9] / dp_atom - 1.0)
            ward_ok = ward <= BROUTE_DPART_BAR
            ward_txt = "B-route vs atom-eigh D_part rel %.1e" % ward
        sl = float(np.polyfit(np.log(Ns), np.log(dps), 1)[0])
        sp = BH.spearman(dps, Ns)
        if sl >= IPR_SLOPE_EXT and sp >= IPR_SP_BAR:
            v_trend = "IPR_TREND_EXTENSIVE(slope=%.2f, sp=%.2f)" \
                % (sl, sp)
        elif sl <= IPR_SLOPE_SAT:
            v_trend = "IPR_TREND_SATURATING(slope=%.2f)" % sl
        else:
            v_trend = "IPR_TREND_MIXED(slope=%.2f, sp=%.2f)" \
                % (sl, sp)
        info("ladder %d rungs, N in [%d, %d]: D_part %.1f .. %.1f "
             "(med frac of N-8: %.3f)"
             % (len(kzs), min(Ns), max(Ns), min(dps), max(dps),
                float(np.median([dpv / (nv - FIB_LO)
                                 for dpv, nv in zip(dps, Ns)]))))
        check("G33-ipr-trend",
              okL and tw <= T_TREND_BAR and ward_ok,
              "participation dimension D_part = 1/sum p_k^2 on "
              "the frame-A ladder (h <= %d): log-log slope %+.2f "
              "(bars %.1f/%.1f), Spearman %+.2f (bar %.1f) => %s; "
              "per-rung chain ward worst %.1e (bar %.0e); %s "
              "(bar %.0e)"
              % (TREND_HCAP, sl, IPR_SLOPE_EXT, IPR_SLOPE_SAT, sp,
                 IPR_SP_BAR, v_trend, tw, T_TREND_BAR, ward_txt,
                 BROUTE_DPART_BAR))
    else:
        v_trend = "IPR_TREND_SMOKE_NA"
        check("G33-ipr-trend", True, "SMOKE: ladder skipped")

    # ---------------- S4: LEG C -- band / sign anatomy
    section("S4  LEG C -- BAND + SIGN ANATOMY (off-diagonal)")
    bands = {}
    for tag in (("w9",) if smoke else ("w9", "SCR", "EPST")):
        bands[tag] = band_stats(Wd[tag])
        bs = bands[tag]
        info("%-5s d0 %.3g  band |C|-shares: %s"
             % (tag, bs["d0"],
                " ".join("%.3f" % (v / max(float(np.sum(bs["ab"])),
                                           1e-300))
                         for v in bs["ab"])))
        info("%-5s band signed/|T_off|: %s"
             % (tag, " ".join("%+.3f"
                              % (v / max(abs(Wd[tag]["T_off"]),
                                         1e-300))
                              for v in bs["sgn"])))
    check("G40-band-tables", True,
          "dyadic band anatomy printed (d0 = median nn spacing, "
          "sealed); near = dist < %.0f d0 -- the off-diagonal "
          "mass distribution over distance is now measured per "
          "world" % NEAR_D0)
    for tag in bands:
        X = bands[tag]["X"]
        info("%-5s coherence X (pre-readout): full %.3e  near "
             "%.3e  far %.3e   (Q_off = 1/X: %.1f / %.1f / %.1f)"
             % (tag, X["full"], X["near"], X["far"],
                1.0 / max(X["full"], 1e-300),
                1.0 / max(X["near"], 1e-300),
                1.0 / max(X["far"], 1e-300)))
    if not smoke:
        seps = {st: abs(math.log10(
            max(bands["w9"]["X"][st], 1e-300)
            / max(bands["SCR"]["X"][st], 1e-300)))
            for st in ("full", "near", "far")}
        sep_scr = max(seps.values())
        best_stat = max(seps, key=seps.get)
        sep_ep = max(abs(math.log10(
            max(bands["w9"]["X"][st], 1e-300)
            / max(bands["EPST"]["X"][st], 1e-300)))
            for st in ("full", "near", "far"))
        coh_found = sep_scr >= SEP_DEC_BAR
        check("G41-coherence-separation", True,
              "sealed 3-statistic battery: sep_SCR = %.3f dec on "
              "'%s' (%s; bar %.1f) => %s; EPST sep %.3f (INFO); "
              "direction: MAIN X_full %.2e vs SCR %.2e (MAIN %s "
              "cancelled)"
              % (sep_scr, best_stat,
                 str({k: round(v, 3) for k, v in seps.items()}),
                 SEP_DEC_BAR,
                 "OFFDIAG_COHERENCE_FOUND" if coh_found
                 else "NO pre-readout separation >= 1 dec (r250-"
                 "R4 gate fails a third time, honest)", sep_ep,
                 bands["w9"]["X"]["full"],
                 bands["SCR"]["X"]["full"],
                 "MORE" if bands["w9"]["X"]["full"]
                 < bands["SCR"]["X"]["full"] else "LESS"))
    else:
        coh_found, sep_scr, best_stat = False, float("nan"), "NA"
        check("G41-coherence-separation", True, "SMOKE: skipped")
    # (p,k) classes
    rr9 = core.build_window(9)
    uu9 = np.asarray(rr9["uu"], float)
    mm9 = 2.0 * np.asarray(rr9["lam"], float)
    M9, D9 = rr9["M"], rr9["D"]
    L9 = 2 * M9 - 2
    cls, pst, dev_n, dev_uf = atom_classes(Wd["w9"], uu9, mm9,
                                           M9, D9, L9)
    ok_adm = dev_n <= NINT_BAR and dev_uf <= UF_BAR
    ctab = {}
    for tag in (("w9",) if smoke else ("w9", "SCR")):
        ctab[tag] = pair_class_table(Wd[tag], cls, pst, bands[tag])
        info("%-5s class (count | |C| | signed/T_off): %s"
             % (tag, "  ".join(
                 "%s %.2e|%.2e|%+.2e" % (k, v[0], v[1], v[2])
                 for k, v in ctab[tag].items())))
    ncls = [int(np.sum(cls[Wd["w9"]["nb"]:] == v))
            for v in (1, 2, 3)]
    e_samep = ctab["w9"]["SAMEP"][1] \
        / max(ctab["w9"]["SAMEP"][0], 1e-300)
    if not smoke:
        r_samep = abs(math.log10(
            max(ctab["w9"]["SAMEP"][1], 1e-300)
            / max(ctab["SCR"]["SAMEP"][1], 1e-300)))
    else:
        r_samep = 0.0
    if e_samep >= EULER_E_HI or r_samep >= EULER_R_HI:
        v_euler = "EULER_STRUCTURE_VISIBLE"
    elif e_samep <= EULER_E_LO and r_samep <= EULER_R_LO:
        v_euler = "EULER_STRUCTURE_ABSENT"
    else:
        v_euler = "EULER_STRUCTURE_WEAK"
    check("G42-pk-classes", ok_adm,
          "admission: n = round(exp(u)) integer to %.1e (bar "
          "%.0e), lag recovery to %.1e (bar %.0e); window atoms "
          "%d = ARCH %d + K1 %d + KHI %d (labels world-blind); "
          "e_SAMEP = %.3g (bars %.0f/%.0f), M/S |C|-share ratio "
          "%.3f dec (bars %.1f/%.1f) => %s"
          % (dev_n, NINT_BAR, dev_uf, UF_BAR,
             Wd["w9"]["A"] - Wd["w9"]["nb"], ncls[0], ncls[1],
             ncls[2], e_samep, EULER_E_HI, EULER_E_LO, r_samep,
             EULER_R_HI, EULER_R_LO, v_euler))

    # ---------------- S5: LEG D -- EPSTEIN adjudication
    section("S5  LEG D -- EPSTEIN ANOMALY ADJUDICATION")
    if not smoke:
        Wm, We = Wd["w9"], Wd["EPST"]
        dT = We["T_true"] - Wm["T_true"]
        sh_diag = (We["T_diag"] - Wm["T_diag"]) / dT
        rowsM, rowsE = Wm["p"]["rows"], We["p"]["rows"]
        NN = min(Wm["N"], We["N"])
        k_dev = None
        for k in range(NN - 1):
            gm = rowsM[k]["gam_next"]
            ge = rowsE[k]["gam_next"]
            if abs(ge / gm - 1.0) >= KDEV_BAR:
                k_dev = k + 1
                break
        drho = (np.asarray(We["p"]["rho"][:NN], float)
                - np.asarray(Wm["p"]["rho"][:NN], float))
        if k_dev is None or k_dev <= FIB_LO:
            e_early = 0.0
            early_txt = "k_dev <= 8 (vacuous)"
        else:
            e_early = abs(float(np.sum(drho[FIB_LO:k_dev]))) \
                / abs(dT)
            early_txt = "|sum_{8..%d} drho| = %.2e of |dT| %.4f" \
                % (k_dev - 1, abs(float(np.sum(
                    drho[FIB_LO:k_dev]))), abs(dT))
        ce = cross["EPST"]
        bord_ok = abs(We["T_bord"] / We["T_mat"] - 1.0) \
            <= BORD_CTRL_BAR
        if (ce["phi_op"] >= EPST_OP_BAR
                and e_early <= EARLY_ART_BAR and bord_ok):
            v_ep = "ARTEFAKT_KERNEL_COUPLING"
        elif (ce["phi_ms"] >= EPST_MASS_BAR
                or e_early >= EARLY_GEN_BAR):
            v_ep = "GENUINE_BASE_FIBER_COUPLING"
        else:
            v_ep = "EPSTEIN_COUPLING_MIXED"
        check("G50-epstein-location", True,
              "d1: T_E %+.4f (dT vs MAIN %+.4f); atom split "
              "T_diag_E %+.4f => share_diag_E = %.3f (off-diag "
              "share %.3f); spectral K80_own(EPST) %s, D_part "
              "%.1f" % (We["T_true"], dT, We["T_diag"], sh_diag,
                        1.0 - sh_diag, str(prof["EPST"][1]),
                        prof["EPST"][2]))
        check("G51-epstein-mechanism", True,
              "d2: k_dev = %s (first gammahat dev >= %.1f, world "
              "data); E_early = %.2e (%s; bars %.1f/%.1f); cross "
              "M/E phi_op %.3f (bar %.1f) phi_mass %.3f (bar "
              "%.1f); border route on EPST %.1e (bar %.0e); "
              "lambda-vs-vector phi_lambda %.3f (INFO) => %s -- "
              "the fiber consumes the base chain THROUGH the "
              "kernel K_N: %s"
              % (str(k_dev), KDEV_BAR, e_early, early_txt,
                 EARLY_ART_BAR, EARLY_GEN_BAR, ce["phi_op"],
                 EPST_OP_BAR, ce["phi_ms"], EPST_MASS_BAR,
                 abs(We["T_bord"] / We["T_mat"] - 1.0),
                 BORD_CTRL_BAR, ce["phi_lam"], v_ep,
                 "coupling is trivial-mechanical (r252 "
                 "orientation layer == fiber layer through the "
                 "kernel)" if v_ep == "ARTEFAKT_KERNEL_COUPLING"
                 else "a non-kernel channel carries it"))
    else:
        v_ep = "EPSTEIN_SKIPPED_SMOKE"
        check("G50-epstein-location", True, "SMOKE: skipped")
        check("G51-epstein-mechanism", True, "SMOKE: skipped")

    # ---------------- S6: falsifiers + must-fails
    section("S6  FALSIFIERS + MUST-FAILS")
    if not smoke:
        Wsm = world_build(ctrl["SMOOTH"])
        ok_sm = abs(Wsm["T_mat"]) <= SM_GUARD * Wsm["gross"]
        check("G60-smooth-self-alias", ok_sm,
              "SMOOTH (sigma0 == 0): |T_mat| = %.2e vs gross "
              "%.3g, ratio %.1e (bar %.0e)"
              % (abs(Wsm["T_mat"]), Wsm["gross"],
                 abs(Wsm["T_mat"]) / max(Wsm["gross"], 1e-300),
                 SM_GUARD))
    else:
        check("G60-smooth-self-alias", True, "SMOKE: skipped")
    # m2 + m3 on w9 (need K_N kernel = G + G8)
    W9 = Wd["w9"]
    GN = W9["G"] + W9["G8"]
    s9, sb9 = W9["s"], W9["s_b"]
    T_N_s0 = float(s9 @ (GN @ s9))
    T_N_sb = float(sb9 @ (GN @ sb9))
    rho9 = np.asarray(W9["p"]["rho"], float)
    noise9 = MF_NOISE * W9["gross"]
    m2_gap = T_N_sb - T_N_s0
    m2_ratio = m2_gap / float(rho9[0])
    ok_m2 = 0.5 <= m2_ratio <= 2.0
    q7 = float(np.sum(rho9[1:FIB_LO]))
    m3_gap = T_N_s0 - W9["T_mat"]
    ok_m3a = (abs(m3_gap / q7 - 1.0) <= MF_REL
              and q7 >= MF_LOUD * noise9)
    P9, sg9 = W9["P"], W9["sgv"]
    N9 = W9["N"]
    Gtop = (P9[FIB_LO:N9 - 1].T * sg9[FIB_LO:N9 - 1]) \
        @ P9[FIB_LO:N9 - 1]
    T_shift = W9["T_mat"] - float(s9 @ (Gtop @ s9))
    del Gtop
    rho_top = float(rho9[N9 - 1])
    ok_m3b = (abs(T_shift / rho_top - 1.0) <= MF_REL
              and rho_top >= MF_LOUD * noise9)
    if not smoke:
        Ws = Wd["SCR"]
        Ps, sgs = Ws["P"], Ws["sgv"]
        Ns_ = Ws["N"]
        Gplus = Ps[FIB_LO:Ns_].T @ Ps[FIB_LO:Ns_]
        T_plus = float(Ws["s"] @ (Gplus @ Ws["s"]))
        del Gplus
        rhoS = np.asarray(Ws["p"]["rho"][FIB_LO:], float)
        pred = 2.0 * float(np.sum(np.abs(rhoS[rhoS < 0.0])))
        m1_shift = T_plus - Ws["T_mat"]
        ok_m1 = (abs(m1_shift / pred - 1.0) <= MF_REL
                 and pred >= MF_LOUD * MF_NOISE * Ws["gross"])
        cs = cross["SCR"]
        lamC_rev = cs["lamC"][::-1]
        T_rev = float(np.sum(lamC_rev * cs["pM"] * cs["pM"]))
        m4_move = abs(T_rev - cs["T_lswap"])
        m4_floor = max(eig_worst * abs(W9["T_mat"]), 1e-300)
        ok_m4 = m4_move >= M4_LOUD * m4_floor
        check("G61-must-fails-fire",
              ok_m1 and ok_m2 and ok_m3a and ok_m3b and ok_m4,
              "m1 sign-drop (SCR): shift %+.4f vs predicted "
              "2 sum|rho<0| = %+.4f (rel %.1e, %.1e x floor); m2 "
              "centering: rho_0 ratio %.4f in [0.5, 2.0]; m3 "
              "level-8 forgotten: dev %.1e rel Q_7 = %.3e (%.1e "
              "x floor, quiet-zone disclosure); top-level shift "
              "vs rho_{N-1} rel %.1e (%.1e x floor); m4 reversed "
              "lambda-matching moves T_lswap by %.4g = %.1e x "
              "eigen dev (bar %.0f x)"
              % (m1_shift, pred, abs(m1_shift / pred - 1.0),
                 pred / max(MF_NOISE * Ws["gross"], 1e-300),
                 m2_ratio, abs(m3_gap / q7 - 1.0), q7,
                 q7 / max(noise9, 1e-300),
                 abs(T_shift / rho_top - 1.0),
                 rho_top / max(noise9, 1e-300), m4_move,
                 m4_move / m4_floor, M4_LOUD))
    else:
        check("G61-must-fails-fire", ok_m2 and ok_m3a and ok_m3b,
              "SMOKE (w9 only): m2 rho_0 ratio %.4f; m3 Q_7 dev "
              "%.1e / top-level rel %.1e; m1/m4 need SCRAMBLE "
              "(skipped)"
              % (m2_ratio, abs(m3_gap / q7 - 1.0),
                 abs(T_shift / rho_top - 1.0)))

    # ---------------- S7: verdict
    section("S7  VERDICT")
    check("G90-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact atom-pair split of the tau-coordinate "
          "fiber form, its full spectral decomposition with the "
          "compression adjudication, the operator-vs-mass world "
          "split, the band/coherence anatomy, the (p,k)-class "
          "census, and the EPSTEIN coupling adjudication")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        if compress:
            v_main = "SPECTRAL_COMPRESSIBLE(K=%d, share=%.3f)" \
                % (k80_pool, share_at)
        elif coh_found:
            v_main = "OFFDIAG_COHERENCE_FOUND(%s, %.2f dec)" \
                % (best_stat, sep_scr)
        elif "SATURATING" not in v_trend:
            v_main = "OFFDIAG_EXTENSIVE_CONFIRMED"
        else:
            v_main = "OFFDIAG_SATURATING_UNRESOLVED"
        verd = " + ".join([v_main, v_split, v_lam, v_trend,
                           v_euler, "EPSTEIN: " + v_ep])
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G91-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: the exact split, the spectral "
          "profiles and their world location, the cross-table "
          "mechanism split, the IPR trend, the coherence "
          "battery, the class census, the EPSTEIN adjudication; "
          "OPEN: any a-priori bound, the separation mechanism as "
          "a theorem, the budget bound and the base law "
          "(r243/r247/r250/r251/r253 stand); NO RH claim"
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
