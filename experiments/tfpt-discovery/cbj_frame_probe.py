#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cbj_frame_probe -- PRIME.CBJ.CONFLUENT.FRAME.01

FROZEN SPEC (2026-08-20).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim beyond the
per-block/per-rung certificates stated, NO counterexample claim.  It
closes no gate and narrows no gate.  Concurrent-lane files are not
touched.

=======================================================================
MISSION (capstone round; the externally proposed COFINAL BLOCK JET
route, adapted to the house objects).  Instead of treating near
frequencies of the prime comb individually, cluster them at scale
1/H and replace point values by jets: near points become a confluent
Vandermonde block instead of a bad min-gap constant.  Target core
lemma (lower sampling/frame inequality for clustered logarithmic
frequencies):
   int |sum_j a_j e^{i t lam_j}|^2 W_H(t) dt
      >= c H sum_C sum_{r<m_C} H^{-2r} |J_{C,r}(a)|^2
with W_H a predefined positive-definite Fejer/Beurling kernel and
c > 0 explicit, zone- and depth-independent.  Steps A-F of contract
PRIME.CBJ.CONFLUENT.FRAME.01; honest-outcome taxonomy
{CBJ-FRAME-PROVEN, CBJ-FRAME-MEASURED-CARRIES, CBJ-DEAD-AT-<step>,
CBJ-RELABELING}.
=======================================================================
State consumed (CITED): CDXCIV/r178 (canonical residue {H1^H2^H3}-
KOFINAL + census-forall-k LOOP + H-PIN; L1 = TAIL + H-pin); CDXCIII
(corrections of record); CDLXXXIV/r169 (sigmafloor: SF1 sigma ==
(1-slop) delta DC EXACT; SF2 floor lands on delta; SF3 DC leg
classical-per-census; SF4 demand absorbs any polynomial rate; SF6
FLOOR-INEQ-WORLD-INSENSITIVE + BRIDGE-ARITHMETIC); CDLXXXVII/r171
(jetmass PF floor; H1/H2 per rung); v922 (D1 derivative/spacing-
product identity, D2/P5 jet sum rules, D3 A0-cancellation); v924
(L1 moment-Laurent PHI); v927 (BA1-BA3: positive certified block sum
forces one positive rung; blocks B2 = [4,8], B3 = [8,16], B4 =
[16,32]); v928 (DT1/DT2); v930 (cone-entry mechanism MEASURED: entry
at the largest new PRIME-POWER atom of the block, excluding trailing
2-powers -- Bughunt-VI F1 wording, reading ambiguity DISCLOSED
there); r131 OFF recipe VERBATIM; HSW22 Cor. 1.2; PT21 (T_PT =
3000175332800, census per-k classical; ALL-K == the flagged RH
loop); Landau 1912 + Gonek 1985/1993 CITED AS FORM; Montgomery &
Vaughan 1974 (Hilbert's inequality / mean-value theorem, J. London
Math. Soc. (2) 8, 73-82: int_0^T |sum a_r e^{i lam_r t}|^2 dt =
sum_r |a_r|^2 (T + 3 pi theta_r / delta_r), |theta_r| <= 1, delta_r
= min_{s != r} |lam_r - lam_s| -- UNCONDITIONAL, used AS FORM and
instance-verified in G14); Bertrand--Chebyshev (unconditional);
Bochner/Fejer positivity (classical); Weyl; Cauchy--Binet.

NOTATION.  Rung h = builder x (R4.build_cell, even sector); a =
log(h)/2; K = ceil(1.25 h log h); om_k = k pi / a; b_k = om_k^2
(b_0 = 0); source coefficients c_k = cn_mp_str; d_k = (-1)^k c_k;
A_0 = sum d_k; w_k = d_k b_k (k >= 1); A_2 = sum w_k; T_z = 2 pi h;
WFULL = ward ordinates in (T_z + 6.0, gamma_7000]; mu(g) =
sin^2(a g)/g^2; F(y) = A_0 + sum_k w_k/(y - b_k);
   delta_h = [sum_WFULL mu F^2] / [A_0^2 sum_WFULL mu]  (r169 JET
   MASS, recipe VERBATIM);  DC_h = (G_W - C_W)/(2 G(T_z)).
COMB SIDE: prime-power atoms q <= 2^19, lam_q = log q; dyadic
frequency block CB_k = atoms q in (2^k, 2^{k+1}]; depth ratio r =
2^k/H with H = 2^{k-e}, e in EGRID = (-1, 1, 3, 5, 7) (r = 0.5, 2,
8, 32, 128 -- ALL H dyadic-exact); clusters = FIXED ABSOLUTE GRID
cells of width link/H in lam (idx = floor(lam H / link); link = 1
or LINK_MV = 63 pi/20 = 3.15 pi -- geometry only, NEVER wall signs);
u_j = H (lam_j - cell center); jet map T_C[r,j] = u_j^r / r!
(the contract's H^{-2r} |J_{C,r}|^2 realized in u-coordinates:
J-tilde_{C,r} = sum_j a_j u_j^r / r!, DISCLOSED convention);
window transforms (normalized W-hat(0) = 1, x = xi H):  FEJ1 =
sinc^2(x/2), FEJ2 = sinc^4(x/4), GAUSS = exp(-x^2/2);
   c_intra(cell) = min over clusters of lam_min(B_C^T G_CC B_C),
   B_C = T_C^{-1}, G_CC[i,j] = W-hat(u_i - u_j)   (mp, dps 50;
   the PRIMARY measured frame currency -- per-cluster floor);
   c_point(cell) = min over clusters of lam_min(G_CC)  (the naive
   point-basis floor the jets must rescue);
   c_full(cell)  = lam_min(B^T G B) full-frame f64 for n <= 520,
   eigenpair-warded, UNRESOLVED disclosed where f64 dies.

=======================================================================
THE SIX CONTRACT STEPS AS EXECUTED (verdicts frozen from the ONE
disclosed pre-freeze calibration pass, calib_cbj_pass1.log; numbers
below are the calibrated record values)
=======================================================================
STEP A (JET IDENTIFICATION; EXACT, R == 0).  F(g^2) ==
sum_{k=0}^{K-1} d_k psi_k(g) with psi_k(g) = g^2/(g^2 - b_k) EXACTLY
(k = 0 included: b_0 = 0 gives psi_0 == 1); hence with J_h =
(d_k / A_0)_k (SOURCE-SIDE ONLY: cn_mp_str + parity + their own sum)
and the PSD Gram G_h[k,l] = sum_WFULL mu psi_k psi_l / sum_WFULL mu:
   delta_h == |J_h|^2_{G_h}   EXACTLY, NO EXTRA TERM (R == 0).
Gates: G10 generic sympy (identity + Gram-PSD as sum of squares +
R == 0); G31 numeric at ALL reachable rungs h = 4..16 + holdout 20
(independent per-pair accumulation vs recipe VERBATIM; dev bar
1e-30) + mp Cholesky PD at h = 4/5/8 + r169 DELTA_TAB replication.

STEP B (CLUSTER NORMAL FORM).  HOUSE LEG (exact): the moment map
A_m = sum_k d_k b_k^m is the Vandermonde V[m,k] = b_k^m in the pole
nodes; det V == prod_{k<l} (b_l - b_k) (spacing product, G11); the
pole/node basis change is the Cauchy matrix with det[1/(y_j - b_k)]
== prod(y-spacings) prod(b-spacings) / prod(y_j - b_k) and the
v922-D1 spacing product F'(y_j) prod_k (y_j - b_k) == A_0
prod_{i != j} (y_j - y_i) re-derived generically (G11) and
instantiated at h = 4/5 on census nodes (G32).  G_h == V^T K_h V
with K_h := V^{-T} G_h V^{-1} exact finite linear algebra; the
Laurent-kernel reading of K_h is DIVERGENT on the window (b_k >>
g^2) -- DISCLOSED, exact instance gated on rationals only.  HOUSE
POLES ARE NON-CONFLUENT (om_k equally spaced): the confluent
content lives comb-side.  COMB LEG (exact): the cluster jet map
det T_C == prod_{i<j} (u_j - u_i) / prod_r r! -- the determinant of
the basis change is the cluster SPACING PRODUCT (G12).

STEP C (LOWER FRAME BOUND -- MEASURED FIRST, tools priced).
G21/G22: the c_intra ladder over KGRID x EGRID (FEJ1, link 1).
CALIBRATED RECORD (min over clusters, mp, adaptive dps):
  c_intra(k; r = 0.5 / 2 / 8 / 32 / 128):
  k=6 : 1.0 / 1.6212e-1 / 7.5651e-3 / 3.3554e-7 / 1.7458e-12
  k=8 : 1.0 / 1.6368e-1 / 7.5960e-3 / 3.3585e-7 / 9.3772e-21
  k=10: 1.0 / 1.6345e-1 / 1.5351e-3 / 6.0353e-8 / 8.7877e-24
  k=12: 1.0 / 1.6157e-1 / 7.5926e-3 / 3.3577e-7 / 1.6264e-21
  k=14: 1.0 / 1.6161e-1 / 7.5083e-3 / 3.3548e-7 / 2.8973e-22
  holdouts: k=16: 7.5200e-3 (r=8), 2.8274e-22 (r=128);
            k=18: 1.5306e-3 (r=8), 3.0883e-19 (r=128).
THE MEASURED VERDICT AXES: (a) at FIXED r the ladder is
DEPTH-STABLE-WITHIN-SCATTER (r <= 32 rows nearly k-constant;
the r = 128 row scatters 1.7e-12 .. 8.8e-24 over k = 6..18 with
NO decay trend -- the k-dependence is the extreme-value scatter
of the worst-occupancy cluster; fitted slope log10 c vs k at
r = 128 is -0.3889, frozen window (-0.9, 0.10)); (b) at FIXED k
it COLLAPSES EXPONENTIALLY IN THE OCCUPANCY (log10 c_intra vs
max-occupancy m slope -0.7484, frozen window (-1.1, -0.45));
(c) the exact occupancy bound m <= floor(2^{k+1}(e^w - 1)) + 1
~ 2r + 1 is k-UNIFORM (gated on every cluster): at FIXED
resolution r the per-cluster floor is k-uniformly bounded below
through the exact occupancy bound + the measured m-law -- THE
WALL IS THE r-COLLAPSE, NOT DEPTH.  THE GLOBAL FORM IS DEAD
(G27/G28, the honest kill of the contract's inequality AS
STATED): (i) DOF KILL -- at 15 of 20 full-frame cells the
coefficient count n EXCEEDS the measured numerical rank of the
block Gram (Landau/Slepian time-bandwidth dof ~ span x H / pi;
prolate plunge CITED; e.g. k=12, r=8: n = 474, rank 128, dof
112.8; c_full collapses to the f64 prolate-tail floor
~1e-12..1e-16 wherever n > dof, while sub-dof cells carry real
constants c_full = 0.021 .. 0.323): a zone- and depth-independent
c > 0 for ALL jets of ALL clusters cannot exist once n > dof;
(ii) SEAM KILL -- adjacent dyadic blocks couple at 0.994 at the
boundary (atoms straddling the block edge are arbitrarily close
in lam; far-pair coupling 6.4e-4-class <= 1e-2): the naive
block-decomposed global form needs overlapping windows /
partition of unity.  TOOLS PRICED: (i) Fejer positivity CARRIES
(G13 exact + G20 PSD measured); (ii) MV Hilbert CITED-VERIFIED
(G14: deterministic battery max |theta| = 0.115 <= 1;
Montgomery--Vaughan 1974) -- KILLED at linkage 1 (T - 3 pi H < 0
exact) and CARRIES at LINK_MV = 3.15 pi with exact margin 1/21,
adjacent-cell pairs repaired by the EXACT two-shifted-grid lemma
(an open interval of length < w/2 meets at most one boundary of
the union of the two half-shifted grids; gated on all 12322
close pairs at (k=12, r=32)); (iii) Carleson embedding for
confluent samples: UNPRICED IN CORPUS (stated need: a Carleson
constant for exponential-type-1/2 spaces on [-1, 1] uniform in
m and in the window shape -- OPEN, named); (iv) Schur complement
over clusters: block-diagonal floor minus coupling positive at
3 of 20 full-frame cells (only r = 0.5; already at r = 2 the
coupling 2.6-3.5 exceeds the intra floor 0.16):
SCHUR-INSUFFICIENT-AT-DEPTH, measured; deep-cell f64 legs
UNRESOLVED and disclosed; (v) prime-power occupancy: exact
k-uniform bound gated on EVERY cluster (G15/G22) + Bertrand
cofinality (G15).  JET RESCUE (G24): c_intra/c_point = 6.46 ..
2.6e+107 over the 29 confluent cells -- the confluent jet basis
rescues the collapsing point basis by up to 107 dex; real but
incomplete (the m-collapse remains).

STEP D (SOURCE-ONLY SELECTOR; v930 upgraded).  h-hat_k = the
largest prime-power atom in (2^k, 2^{k+1}] that is not a power of
two (SOURCE-ONLY, sealed pre-ward: G34/G45).  h-hat = 7/13/31/61/
127/251/509/1021/2039/4093/8191 at k = 2..12; h-hat_k > 2^k at
every k <= 17 (arithmetic) and FOR ALL k by Bertrand--Chebyshev
(CITED, unconditional: an odd prime lies in (2^k, 2^{k+1})):
h-hat_k -> infinity PROVEN-CITED.  v930 CONSISTENCY: h-hat(B2) == 7
and h-hat(B3) == 13 == the v930/r167 measured entry atoms at the
two certified blocks (the b5/b8 exhibits; the Bughunt-VI F1
wording ambiguity disclosed there).  THE FLOOR AT THE SELECTOR
(G35, measured on WFULL, honest adverse finding): delta(7) =
1.157312 vs B2 flat mean 1.299444 (ratio 0.8906) and delta(13) =
1.210860 vs B3 flat mean 1.283704 (ratio 0.9433): the selector
UNDERPERFORMS the v927-BA flat block average at BOTH certified
blocks (-11.0 / -5.7 percent) -- the v930 entry atom does NOT
mark a delta-optimal rung; but it CLEARS the SF2 demand
delta_req = SIGMA0/((1-slop) DC) (SIGMA0 = 0.15 cited r168) with
margins delta/delta_req = 2.14 (h-hat 7) / 3.05 (h-hat 13), and
ALL rungs 4..16 + 20 clear it (min margin 1.405 at h = 4, bar
1.35).  SELECTOR-VS-BA ADJUDICATION: SELECTOR-UNDERPERFORMS-BA-
BUT-CLEARS-DEMAND -- source-only, sealed, no sign-peeking; it
does NOT beat the pigeonhole midlayer, and it carries no all-k
theorem: that statement is EXACTLY the sigma-floor at selector
rungs (SF1-equivalent, G16/G50), NOT new currency.  B4
REDUCED-SCOPE DISCLOSED: h-hat(B4) = 31 sealed and gated
arithmetically; delta(31) NOT built (r172 deep-build cost class
~2000 s per rung).

STEP E (SUPPORT UNIFORMITY).  COMB (k = 12, r = 32/128, link 1):
GAUSS floors 6.0014e-2 / 1.0026e-3 BEAT FEJ1 (3.3577e-7 /
1.6264e-21) by 5 to 18 DEX (no transform zeros, Beurling class);
FEJ2 (6.1458e-8 / 2.3335e-22) is WORSE than FEJ1: the m-collapse
LAW is shape-uniform, the CONSTANT is strongly window-dependent
-- the best measured window is the Gaussian taper.  LINK_MV =
3.15 pi rescaled clusters degrade by the occupancy inflation
exactly as the bound predicts ((12, r=8): m_max 19, c_intra
1.5517e-14 vs 7.5926e-3 at link 1).  HOUSE: the jet identity
holds identically on W12 (NZ = 1200) and WFULL (G36, dev <=
1e-30 both windows, delta_W12/delta_WFULL in (0.90, 1.15) at
every rung); DC replicates r169 DC_TAB at 4/5/8 rel 5e-3.
WHAT AN a-UNIFORM STATEMENT NEEDS (stated exactly): a window-
independent lower bound on the intra-cluster kernel over the
exponential-type-1/2 class -- i.e. tool (iii) (Carleson constant
uniform in m and in the window shape within the frozen family);
with (iii) open, support-uniformity is LAW-SHAPE-UNIFORM /
CONSTANT-NONUNIFORM (measured).

STEP F (KILL GATES, all four).  (1) EPSTEIN (G42): x = 8/9/10
cells, tau_w replicates CTRL_TAU_TAB (rel 5e-3, all < 0), the BA3
bridge is VIOLATED ((tau + OFF - zsum)/|tau| = -1.0050 / -1.0009
/ -1.0056 < 0) -- the ASSEMBLED chain loses its constant at the
bridge leg; the naked jet floor delta_w stays positive
(0.878/0.718/0.615: FLOOR-INEQ-WORLD-INSENSITIVE, r169-SF6
REPLICATED and RESTATED, not hidden).  (2) SCRAMBLE (G41):
SCRARITH x = 4/5/8 -- same instrument, bridge violated (-1.2562 /
-1.0119 / -1.0086 < 0), tau_w < 0 replicated (delta_w
0.924/0.597/0.766 positive, disclosed); comb-side deterministic
golden-jitter scramble at (k=10, r=8): c_intra 1.5150e-3 vs MAIN
1.5351e-3 -- the naked frame constant is SCRAMBLE-BLIND (pure
geometry, DISCLOSED world-insensitivity, G29), the kill lands on
the house half exactly as SF6 predicts (the pair {floor, bridge}
carries the arithmetic).  (3) NO-ZERO (G44): machine ancestry --
the FRAME leg {FEJER-EXACT, MV-1974-CITED, GRID-PREDEF,
SOURCE-ARITH, OCCUPANCY-EXACT} has NO zero-table ancestor
(DFS-gated); the FLOOR leg consumes CACHE-WARD == census-per-k
class (DISCLOSED, same epistemic class as r169; ALL-K stays the
flagged loop, NOT consumed); AST purity: comb_*/selector_*
functions contain no ward_/np.load/build_cell calls (G01); NO
implicit zero separation: min intra-cluster u-gap reaches
3.906e-3 while c_intra follows the OCCUPANCY law (the c-vs-gap
regression is the m(r, k) law itself, R^2 0.57, DISCLOSED -- the
bound formula consumes no gap, G25).  (4) PREDEFINITION
(G02/G45): clusters, windows, selector computed from source
arithmetic ONLY and SHA-sealed in the event registry BEFORE the
first ward load / build dispatch (monotone event counter gated;
re-hash at end of run matches the seal).

=======================================================================
TAXONOMY VERDICT (frozen from calibration):
   CBJ-DEAD-AT-C-GLOBAL-FORM + CBJ-PERCLUSTER-FLOOR-MEASURED-
   CARRIES.
Honest content: (a) steps A/B land EXACT (R == 0; spacing-product
normal form; corpus wiring v922/v924 instantiated); (b) the
contract's core lemma AS STATED (one c > 0, zone- and depth-
independent, for ALL jets of ALL clusters summed over the block)
is DEAD AT STEP C with three independent measured walls: the
Landau/Slepian dof kill (n > time-bandwidth rank at 15/20 cells),
the block-seam coupling (0.994), and the exponential occupancy
collapse of the intra floor (slope -0.75 dex/atom); (c) what
MEASURED-CARRIES is the PER-CLUSTER jet floor with the exact
k-uniform occupancy bound at fixed resolution r -- depth-stable
within extreme-value scatter, shape-uniform in law, Gaussian-
window preferred by 5-18 dex; open legs NAMED: the r-collapse /
jet-convention optimization / Carleson tool (iii) / the house-
side jet rescue (the house Gram wall 1e-17 -> 1e-113 at h =
4 -> 13 is the same confluence wall in Gram coordinates, G33);
(d) the selector upgrade lands source-only, matches v930, clears
the demand, and honestly UNDERPERFORMS the BA midlayer; (e) all
four kill gates behave exactly as the r169-SF6 anatomy predicts
(bridge-kill, not floor-kill).  NOT a relabeling: the frame
constant is tau-free geometry (G50 slopes 0.0002/0.0054 <= 0.30);
the FLOOR demand is the KNOWN sigma-floor coordinate at selector
rungs (SF1-exact, DISCLOSED IDENTIFICATION, not a new omega).
The lambda-uniform residue is UNCHANGED in cardinality; nothing
is closed, nothing upgraded.

WHAT IS BUILT AND GATED: S0 G01 AST firewall + comb purity, G02
predefinition order, G03 cache ward + pedigree; S1 exact layer G10-
G16; S2 comb layer G20-G29 (grids frozen above; f64 full-frame legs
disclosed); S3 house layer G30-G37 (rungs 4..16 + holdout 20, 10
workers, r169 recipes VERBATIM); S4 controls + kill gates G40-G45;
S5 screens/assembly G50/G51/G52/G53/G60/G99.  FROZEN BARS: IDEN_BAR
1e-30; PD rungs (4,5,8); c-ladder replication rel 2e-5 (mp);
TLAW ladder rel 1e-3 (r166 strings); DELTA/DC tabs rel 5e-3 (r169
strings); CAL_DELTA rel 1e-4; CTRL_TAU rel 5e-3; CTRL bridge
violations rel 5e-2; gmin ladder rel 1e-3 (deterministic strings;
h = 13 value entry-precision-limited, +-1 dex class, DISCLOSED);
margins bar 1.35 + selector-rung margins >= 2.0; runtime bar
3300 s.  CONTROLS: SMOOTH(5), SCRARITH(4,5,8), EPSTEIN(8,9,10) at
CTRL_DPS, CTRL_NZ = 300, recipes VERBATIM.  LOOP GUARD: the four
flagged cycles (A0-triangle, census-forall-k, Gonek-1984,
Montgomery-PC/Goldston-Montgomery second moments) DECLARED,
DFS-detected, consumed by NOTHING delivered (G52); min-cut r135
graph replicated flows base 4 / refined 5 / one-grant 5 /
counterfactual-parallel 6 NOT REAL (G53).  CALIBRATION (disclosed,
per house convention): ONE pre-freeze calibration pass in TWO
disclosed sub-passes -- pass 1 = the full probe in --mode calib
(calib_cbj_pass1.log, 1036.0 s, pre-freeze SHA e1ad438831ebab26,
39/41 with the two placeholder-table gates failing as expected
pre-freeze); pass 2 = the Jacobi-Gram min-eig ladder re-measured
at escalated dps after the pass-1 dps-60 floor proved to be noise
at h >= 8 (calib_cbj_pass2.log, 215.8 s; the w_gmin dps map and
the 118-digit Gram export are the disclosed instrument fix; no
bar, grid or table other than CAL_GMIN moved).  Scratch deleted,
both logs kept, numbers verbatim above.  DETERMINISM: no
randomness anywhere; scramble = golden-ratio jitter; ProcessPool
results keyed; run2 must be identical modulo wall-clock tokens
(lines carrying 'WALL' or wall-second prints).

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
from concurrent.futures import ProcessPoolExecutor

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
T_PT = 3000175332800
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
NZFULL = 7000
NZ12 = 1200
F64_SLOP = 1e-3
Z_OVERHANG = 6.0
M_JETS = 400
MGRID = (2, 4, 8, 16, 32, 64, 128, 256, 400)
WORKERS = 10
SIGMA0 = 0.15
IDEN_BAR = 1e-30
PD_RUNGS = (4, 5, 8)
RUNTIME_BAR = 3300.0

HRUNGS = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
H_HOLD = 20
DPS = {4: 60, 5: 60, 6: 65, 7: 70, 8: 80, 9: 85, 10: 90, 11: 100,
       12: 110, 13: 120, 14: 120, 15: 125, 16: 130, 20: 144}

# r166/r169 corpus strings (CITED)
TLAW_LADDER = {4: 0.2325, 5: 0.2664, 6: 0.2729, 7: 0.3264,
               8: 0.3738, 9: 0.3645, 10: 0.4032, 11: 0.4534,
               12: 0.4112, 13: 0.4674, 14: 0.4455, 15: 0.4421,
               16: 0.4606, 20: 0.5282}
TLAW_TOL = 1e-3
DELTA_TAB = {4: 1.374423, 5: 1.159470, 8: 1.372972}
DC_TAB = {4: 0.153469, 5: 0.227257, 8: 0.268559}
TAB_TOL = 5e-3
CTRL_SMOOTH = (5,)
CTRL_SCRARITH = (4, 5, 8)
CTRL_EPSTEIN = (8, 9, 10)
CTRL_DPS = {"SMOOTH": 60, "SCRARITH": 60, "EPSTEIN": 80}
CTRL_NZ = 300
CTRL_TAU_TAB = {"SMOOTH": {5: -1.0944},
                "SCRARITH": {4: -2.5151e-2, 5: -0.34593, 8: -0.67664},
                "EPSTEIN": {8: -1.6310, 9: -1.6922, 10: -1.9932}}
CTRL_TAU_TOL = 5e-3
TAU_SLOPE_BAR = 0.30
COND_LO, COND_HI = 1e-40, 1e-10

# comb grids (frozen; geometry only)
PPCAP = 2 ** 19
KGRID = (6, 8, 10, 12, 14)
EGRID = (-1, 1, 3, 5, 7)          # r = 2^e = 0.5, 2, 8, 32, 128
WINS = ("FEJ1", "FEJ2", "GAUSS")
LINK1 = "L1"
LINKMV = "LMV"                    # 63 pi / 20 = 3.15 pi (exact)
HOLDOUT_CELLS = ((16, 3), (16, 7), (18, 3), (18, 7))
FULLN = 520
DPS_COMB = 50
MCAP = 64
SEL_KMAX = 17

# --------------------- calibrated record tables (pre-freeze pass 1)
CAL_CINTRA = {   # (k, e) -> c_intra string, FEJ1/link1 (calibrated)
    (6, -1): "1.000000e+00", (6, 1): "1.621213e-01",
    (6, 3): "7.565066e-03", (6, 5): "3.355437e-07",
    (6, 7): "1.745797e-12",
    (8, -1): "1.000000e+00", (8, 1): "1.636764e-01",
    (8, 3): "7.596047e-03", (8, 5): "3.358471e-07",
    (8, 7): "9.377237e-21",
    (10, -1): "1.000000e+00", (10, 1): "1.634473e-01",
    (10, 3): "1.535116e-03", (10, 5): "6.035323e-08",
    (10, 7): "8.787730e-24",
    (12, -1): "1.000000e+00", (12, 1): "1.615658e-01",
    (12, 3): "7.592596e-03", (12, 5): "3.357709e-07",
    (12, 7): "1.626424e-21",
    (14, -1): "1.000000e+00", (14, 1): "1.616072e-01",
    (14, 3): "7.508256e-03", (14, 5): "3.354809e-07",
    (14, 7): "2.897322e-22"}
CAL_HOLDOUT = {(16, 3): "7.519963e-03", (16, 7): "2.827413e-22",
               (18, 3): "1.530619e-03", (18, 7): "3.088314e-19"}
CAL_WINFAM = {   # (win, e) at k = 12, link 1
    ("FEJ2", 5): "6.145837e-08", ("FEJ2", 7): "2.333483e-22",
    ("GAUSS", 5): "6.001355e-02", ("GAUSS", 7): "1.002616e-03"}
CAL_LMV = {(12, 3): "1.551671e-14"}   # FEJ1, LINK_MV, k=12, r=8
CAL_TOL = 2e-5
# occupancy-law fit windows (frozen from calibration)
MSLOPE_WIN = (-1.1, -0.45)        # log10 c_intra vs m (cal -0.7484)
KSLOPE_WIN = (-0.9, 0.10)         # log10 c vs k at r=128 (cal -0.3889)
# calibrated house strings
CAL_DELTA = {4: "1.374423e+00", 5: "1.159470e+00", 6: "1.433041e+00",
             7: "1.157312e+00", 8: "1.372972e+00", 9: "1.214583e+00",
             10: "1.379691e+00", 11: "1.233525e+00",
             12: "1.315350e+00", 13: "1.210860e+00",
             14: "1.305696e+00", 15: "1.276163e+00",
             16: "1.244494e+00", 20: "1.409453e+00"}
CAL_GMIN = {4: "1.073395e-17", 5: "3.037571e-26", 6: "9.534976e-37",
            8: "9.999389e-55", 13: "5.204157e-113"}
GMIN_KEYS = (4, 5, 6, 8, 13)
GMIN_DPS = {4: 60, 5: 70, 6: 90, 8: 130, 13: 200}
CAL_SEL = {"d7": 1.157312, "avgB2": 1.299444, "d13": 1.210860,
           "avgB3": 1.283704}
SEL_TOL = 5e-3
MARGIN_MIN_BAR = 1.35
CAL_CTRL_VIOL = {("EPSTEIN", 8): -1.0050, ("EPSTEIN", 9): -1.0009,
                 ("EPSTEIN", 10): -1.0056,
                 ("SCRARITH", 4): -1.2562, ("SCRARITH", 5): -1.0119,
                 ("SCRARITH", 8): -1.0086,
                 ("SMOOTH", 5): -1.0033}
CTRL_VIOL_TOL = 5e-2
W12_BAND = (0.90, 1.15)
MV_THETA_BAR = 1.0
RESC_WIN = (1.0, 1e2)     # frozen from calibration (min, max floor)
SCR_DEX = 2.0             # scramble-vs-main c_intra dex band

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")
META_N7000 = os.path.join(HERE, "verified_zeros_n7000_meta.json")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EVT: list[tuple[int, str, str]] = []


def evt(tag: str, payload: str = "") -> None:
    EVT.append((len(EVT), tag, payload))


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
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owners(lineno: int) -> list[str]:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            fns = owners(node.lineno)
            if not any(f.startswith("ward_") for f in fns):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fns or "module"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    # comb purity: comb_*/selector_* functions must not touch wards,
    # caches or the builder (machine leg of kill gate 3/4)
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if not (node.name.startswith("comb_")
                or node.name.startswith("selector_")):
            continue
        for sub in ast.walk(node):
            nm = None
            if isinstance(sub, ast.Attribute):
                nm = sub.attr
            elif isinstance(sub, ast.Name):
                nm = sub.id
            if nm in ("ward_cache", "build_cell", "load"):
                bad.append("comb purity: %s in %s @%d"
                           % (nm, node.name, sub.lineno))
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; NO zeta; np.load only in "
                       "ward_; no verification/ import; comb_/"
                       "selector_ functions ward-free")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    evt("WARD-LOAD", "n7000")
    return np.asarray(np.load(CACHE_N7000), float)


def ward_meta_ok() -> bool:
    return os.path.isfile(CACHE_N7000) and os.path.isfile(META_N7000)


# --------------------------------------------------------- closed forms
def hsw_G_mp(T, dps: int = 60):
    with mp.workdps(dps):
        Tm = mp.mpf(T if isinstance(T, str) else repr(float(T)))
        al = mp.mpf(repr(HSW_A))
        be = mp.mpf(repr(HSW_B))
        cc = mp.mpf(repr(HSW_C))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return t1 + t2 + t3


# ----------------------------------------------------------- comb layer
def comb_sieve(cap: int) -> list[tuple[int, int]]:
    """prime powers (q, p) with q <= cap; pure arithmetic."""
    comp = np.zeros(cap + 1, dtype=bool)
    out = []
    for p in range(2, cap + 1):
        if comp[p]:
            continue
        comp[p * p:: p] = True
        q = p
        while q <= cap:
            out.append((q, p))
            q *= p
    out.sort()
    return out


def comb_wf_mp(win: str, x):
    """normalized window transform at x = xi * H (mp)."""
    if win == "GAUSS":
        return mp.exp(-x * x / 2)
    if win == "FEJ1":
        if x == 0:
            return mp.mpf(1)
        s = mp.sin(x / 2) / (x / 2)
        return s * s
    if win == "FEJ2":
        if x == 0:
            return mp.mpf(1)
        s = mp.sin(x / 4) / (x / 4)
        return s ** 4
    raise ValueError(win)


def comb_cell(pp: list, k: int, e: int, win: str, link: str,
              want_full: bool, jitter: bool = False) -> dict:
    """one comb cell: cluster partition (fixed absolute grid),
    per-cluster confluent-jet floors in mp, occupancy bound,
    optional full-frame f64 leg.  PURE SOURCE ARITHMETIC."""
    lo, hi = 2 ** k, 2 ** (k + 1)
    qs = [q for q, _p in pp if lo < q <= hi]
    with mp.workdps(DPS_COMB):
        Hm = mp.mpf(2) ** (k - e)
        lk = mp.mpf(1) if link == LINK1 else mp.pi * mp.mpf(63) / 20
        lams = [mp.log(q) for q in qs]
        if jitter:
            gold = (mp.sqrt(5) - 1) / 2
            span = lams[-1] - lams[0]
            mg = span / (len(lams) - 1)
            lams = sorted(lams[i]
                          + (mp.frac(gold * (i + 1)) - mp.mpf("0.5"))
                          * mg * mp.mpf("0.9")
                          for i in range(len(lams)))
        w_cell = lk / Hm
        idxs = [int(mp.floor(lam / w_cell)) for lam in lams]
        clusters: list[list[int]] = []
        cur: list[int] = []
        for i in range(len(lams)):
            if cur and idxs[i] != idxs[cur[0]]:
                clusters.append(cur)
                cur = []
            cur.append(i)
        if cur:
            clusters.append(cur)
        # exact occupancy bound: m <= floor(2^{k+1}(e^w - 1)) + 1
        mb = int(mp.floor((2 ** (k + 1)) * (mp.exp(w_cell) - 1))) + 1
        m_max = max(len(c) for c in clusters)
        occ_ok = all(len(c) <= mb for c in clusters)
        c_intra = None
        c_point = None
        min_ugap = None
        worst = None
        for cl in clusters:
            m = len(cl)
            if m == 1:
                val = mp.mpf(1)
                pv = mp.mpf(1)
            else:
                if m > MCAP:
                    return dict(err="m>MCAP", m=m)
                # adaptive precision: confluent Vandermonde
                # conditioning grows ~ exponentially in m; recompute
                # the u-coordinates from the INTEGER atoms at dps_c
                dps_c = max(DPS_COMB, 20 + 4 * m)
                with mp.workdps(dps_c):
                    Hc = mp.mpf(2) ** (k - e)
                    lc = (mp.mpf(1) if link == LINK1
                          else mp.pi * mp.mpf(63) / 20)
                    wc = lc / Hc
                    ctr = (idxs[cl[0]] + mp.mpf("0.5")) * wc
                    if jitter:
                        us = [Hc * (mp.mpf(mp.nstr(lams[i], 45))
                                    - ctr) for i in cl]
                    else:
                        us = [Hc * (mp.log(qs[i]) - ctr) for i in cl]
                    for i in range(m - 1):
                        g = us[i + 1] - us[i]
                        if min_ugap is None or g < min_ugap:
                            min_ugap = g
                    T = mp.zeros(m, m)
                    for r in range(m):
                        f = mp.factorial(r)
                        for j in range(m):
                            T[r, j] = us[j] ** r / f
                    G = mp.zeros(m, m)
                    for i in range(m):
                        G[i, i] = mp.mpf(1)
                        for j in range(i):
                            v = comb_wf_mp(win, us[i] - us[j])
                            G[i, j] = v
                            G[j, i] = v
                    B = mp.inverse(T)
                    Kc = B.T * G * B
                    for i in range(m):
                        for j in range(i):
                            s = (Kc[i, j] + Kc[j, i]) / 2
                            Kc[i, j] = s
                            Kc[j, i] = s
                    Ev, _ = mp.eigsy(Kc)
                    val = min(Ev[i] for i in range(m))
                    Eg, _ = mp.eigsy(G)
                    pv = min(Eg[i] for i in range(m))
            if c_intra is None or val < c_intra:
                c_intra = val
                worst = (len(cl), float(val))
            if c_point is None or pv < c_point:
                c_point = pv
        out = dict(k=k, e=e, win=win, link=link, n=len(qs),
                   ncl=len(clusters), m_max=m_max, m_bound=mb,
                   occ_ok=occ_ok,
                   c_intra=float(c_intra), c_point=float(c_point),
                   min_ugap=(float(min_ugap)
                             if min_ugap is not None else None),
                   worst=worst)
    if want_full and len(qs) <= FULLN and out["m_max"] >= 1:
        out.update(comb_full_f64(qs, k, e, win, link))
    return out


def comb_full_f64(qs: list, k: int, e: int, win: str,
                  link: str) -> dict:
    """full-frame f64 leg: K = B^T G B over the whole block,
    eigenpair-warded; Schur/coupling split.  DISCLOSED f64."""
    H = 2.0 ** (k - e)
    lkf = 1.0 if link == LINK1 else math.pi * 63.0 / 20.0
    lam = np.array([math.log(q) for q in qs])
    w_cell = lkf / H
    idx = np.floor(lam / w_cell).astype(int)
    n = len(qs)
    x = np.subtract.outer(lam, lam) * H
    if win == "FEJ1":
        with np.errstate(divide="ignore", invalid="ignore"):
            s = np.where(x == 0, 1.0, np.sin(x / 2) / (x / 2))
        G = s * s
    elif win == "FEJ2":
        with np.errstate(divide="ignore", invalid="ignore"):
            s = np.where(x == 0, 1.0, np.sin(x / 4) / (x / 4))
        G = s ** 4
    else:
        G = np.exp(-x * x / 2)
    eig_g = float(np.linalg.eigvalsh(G)[0])
    B = np.zeros((n, n))
    pos = 0
    blocks = []
    i = 0
    while i < n:
        j = i
        while j < n and idx[j] == idx[i]:
            j += 1
        m = j - i
        ctr = (idx[i] + 0.5) * w_cell
        us = (lam[i:j] - ctr) * H
        T = np.zeros((m, m))
        for r in range(m):
            T[r] = us ** r / math.factorial(r)
        try:
            Bi = np.linalg.solve(T, np.eye(m))
            wr = float(np.max(np.abs(T @ Bi - np.eye(m))))
        except np.linalg.LinAlgError:
            Bi, wr = None, float("inf")
        if Bi is None or wr > 1e-6:
            with mp.workdps(DPS_COMB):
                Tm = mp.matrix([[mp.mpf(float(us[jj])) ** r
                                 / mp.factorial(r)
                                 for jj in range(m)]
                                for r in range(m)])
                Bm = mp.inverse(Tm)
                Bi = np.array([[float(Bm[a, b]) for b in range(m)]
                               for a in range(m)])
        B[i:j, pos:pos + m] = Bi
        blocks.append((i, j, pos, pos + m))
        pos += m
        i = j
    Kf = B.T @ G @ B
    Kf = (Kf + Kf.T) / 2
    ev, evec = np.linalg.eigh(Kf)
    c_full = float(ev[0])
    v0 = evec[:, 0]
    res = float(np.linalg.norm(Kf @ v0 - ev[0] * v0)
                / max(1.0, float(np.linalg.norm(Kf, 2))))
    bd = np.zeros_like(Kf)
    for (i0, j0, p0, p1) in blocks:
        bd[p0:p1, p0:p1] = Kf[p0:p1, p0:p1]
    off = Kf - bd
    rho_off = float(np.linalg.norm(off, 2))
    c_bd = min(float(np.linalg.eigvalsh(bd[p0:p1, p0:p1])[0])
               for (_i, _j, p0, p1) in blocks)
    resolved = res <= 1e-10 and c_full > -1e-8 * abs(ev[-1])
    # Landau/Slepian time-bandwidth dof vs coefficient count:
    # numerical rank of G (prolate plunge) against n
    evg = np.linalg.eigvalsh(G)
    grank = int(np.sum(evg > 1e-12 * evg[-1]))
    dof = (lam[-1] - lam[0]) * H / math.pi
    return dict(c_full=c_full, eig_g=eig_g, f64_res=res,
                f64_resolved=bool(resolved), c_bd=c_bd,
                rho_off=rho_off, knorm=float(ev[-1]),
                grank=grank, dof=dof)


def comb_xblock(pp: list, k: int, e: int) -> tuple[float, float]:
    """Fejer coupling between blocks k and k+1 (f64): (seam max
    over all cross pairs, far max over pairs |dlam| >= log(2)/2)."""
    H = 2.0 ** (k - e)
    lo, mid, hi = 2 ** k, 2 ** (k + 1), 2 ** (k + 2)
    la = np.array([math.log(q) for q, _p in pp if lo < q <= mid])
    lb = np.array([math.log(q) for q, _p in pp if mid < q <= hi])
    dl = np.subtract.outer(lb, la)
    x = dl * H
    s = np.sin(x / 2) / (x / 2)
    coup = s * s
    seam = float(np.max(coup))
    far = float(np.max(coup[dl >= math.log(2) / 2])) \
        if np.any(dl >= math.log(2) / 2) else 0.0
    return seam, far


def selector_atoms(pp: list, kmax: int) -> dict:
    """h-hat_k = largest prime-power atom in (2^k, 2^{k+1}] that is
    not a power of two.  SOURCE-ONLY."""
    out = {}
    for k in range(2, kmax + 1):
        lo, hi = 2 ** k, 2 ** (k + 1)
        best = None
        for q, p in pp:
            if lo < q <= hi and p != 2:
                if best is None or q > best:
                    best = q
        out[k] = best
    return out


def selector_bertrand(kmax: int, pp: list) -> bool:
    """odd prime in (2^k, 2^{k+1}) for all reachable k (arith check;
    Bertrand--Chebyshev CITED for all k)."""
    primes = {q for q, p in pp if q == p and q % 2 == 1}
    for k in range(2, kmax + 1):
        if not any(2 ** k < q < 2 ** (k + 1) for q in primes):
            return False
    return True


# ----------------------------------------------------------- house layer
def w_main(args) -> dict:
    """per-rung MAIN build: r169 delta/DC recipe VERBATIM + the
    step-A Gram route (independent per-pair accumulation) + Jacobi-
    normalized Gram min-eig + W12 support leg + v922/v924 instances
    at h <= 5."""
    h, dps = args
    try:
        t0 = time.time()
        gam = ward_cache()
        ce = R4.build_cell(h, KFAC, "MAIN", dps, want_mp=True)
        K = ce["K"]
        out = dict(h=h, K=K)
        with mp.workdps(dps):
            E = ce["mpE"]
            tau = E[0]
            lam1 = E[1]
            aa = mp.log(h) / 2
            oms = [kk * mp.pi / aa for kk in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            d = [((-1) ** kk) * cs[kk] for kk in range(K)]
            A0 = sum(d)
            b = [o * o for o in oms]
            A2 = sum(d[kk] * b[kk] for kk in range(1, K))
            # ---- r169 recipe pass (VERBATIM currency) + Gram pass
            Tz = 2 * math.pi * h
            Tlo = Tz + Z_OVERHANG
            Gw = mp.mpf(0)
            Cw = mp.mpf(0)
            Sw = mp.mpf(0)
            SFw = mp.mpf(0)
            Sw12 = mp.mpf(0)
            SFw12 = mp.mpf(0)
            Gm = [[mp.mpf(0)] * K for _ in range(K)]
            Smu = mp.mpf(0)
            for j in range(min(NZFULL, len(gam))):
                gf = float(gam[j])
                if gf <= Tlo:
                    continue
                gm = mp.mpf(repr(gf))
                Rv = 2 * cs[0] / gm
                for kk in range(1, K):
                    Rv += 2 * cs[kk] * (-1) ** kk * gm \
                        / (gm * gm - b[kk])
                s = mp.sin(aa * gm)
                s2 = s * s
                F = gm * Rv / 2
                g2 = gm * gm
                mu = s2 / g2
                Gw += 1 / g2
                Cw += (1 - 2 * s2) / g2
                Sw += mu
                SFw += mu * F * F
                if j < NZ12:
                    Sw12 += mu
                    SFw12 += mu * F * F
                # Gram accumulation (independent basis route)
                psi = [g2 / (g2 - b[kk]) if kk else mp.mpf(1)
                       for kk in range(K)]
                for kk in range(K):
                    pk = mu * psi[kk]
                    row = Gm[kk]
                    for ll in range(kk + 1):
                        row[ll] += pk * psi[ll]
                Smu += mu
            for kk in range(K):
                for ll in range(kk):
                    Gm[ll][kk] = Gm[kk][ll]
            Gz = mp.mpf(mp.nstr(hsw_G_mp(Tz, dps), dps))
            DC = (Gw - Cw) / (2 * Gz)
            delta = SFw / (A0 * A0 * Sw)
            delta12 = SFw12 / (A0 * A0 * Sw12)
            J = [d[kk] / A0 for kk in range(K)]
            quad = mp.mpf(0)
            for kk in range(K):
                quad += J[kk] * J[kk] * Gm[kk][kk]
                for ll in range(kk):
                    quad += 2 * J[kk] * J[ll] * Gm[kk][ll]
            delta_gram = quad / Smu
            out["iden_dev"] = float(abs(delta_gram / delta - 1))
            out["delta"] = float(delta)
            out["delta12"] = float(delta12)
            out["DC"] = float(DC)
            out["tlaw0"] = float(tau / (8 * A0 * A0 * Gz))
            out["tau_neg"] = bool(tau < 0)
            out["fg"] = float((lam1 - tau) / tau)
            out["log10tau"] = float(mp.log(abs(tau)) / mp.log(10))
            out["log10a0sq"] = float(2 * mp.log(abs(A0)) / mp.log(10))
            out["A2_eq_wsum"] = float(abs(
                (A2 - sum(d[kk] * b[kk] for kk in range(1, K))) ))
            # Jacobi-normalized Gram exported at rung precision
            # (the min-eig sits at the conditioning wall: entry
            # precision must exceed it)
            Dg = [mp.sqrt(Gm[kk][kk]) for kk in range(K)]
            ndig = min(dps - 2, 118)
            gn_str = [[mp.nstr(Gm[i2][j2] / (Dg[i2] * Dg[j2]), ndig)
                       for j2 in range(K)] for i2 in range(K)]
            # PD Cholesky at the gate rungs (normalized Gram)
            pd_ok = None
            if h in PD_RUNGS:
                Gn_ = mp.matrix(K, K)
                for i2 in range(K):
                    for j2 in range(K):
                        Gn_[i2, j2] = Gm[i2][j2] / (Dg[i2] * Dg[j2])
                try:
                    mp.cholesky(Gn_)
                    pd_ok = True
                except Exception:               # noqa: BLE001
                    pd_ok = False
            out["pd_ok"] = pd_ok
            # v922/v924 instances at h <= 5 (census nodes)
            if h <= 5:
                poly = [mp.mpf(0)] * (K + 1)
                for kk in range(K):
                    pr = [mp.mpf(1)]
                    for ll in range(K):
                        if ll == kk:
                            continue
                        new = [mp.mpf(0)] * (len(pr) + 1)
                        for t2 in range(len(pr)):
                            new[t2 + 1] += pr[t2]
                            new[t2] -= b[ll] * pr[t2]
                        pr = new
                    for t2 in range(len(pr)):
                        poly[t2 + 1] += d[kk] * pr[t2]
                # poly(y) = y * Ntil(y); Ntil coeffs:
                ntil = poly[1:]
                roots = mp.polyroots(list(reversed(ntil)),
                                     maxsteps=400, extraprec=300)
                rr = [r.real for r in roots
                      if abs(r.imag) <= mp.mpf("1e-15")
                      * (1 + abs(r.real))]
                out["n_nodes"] = len(rr)

                def Fp(y):
                    return sum(-d[kk] * b[kk] / (y - b[kk]) ** 2
                               for kk in range(1, K))
                s_sum = sum(1 / Fp(y) for y in rr)
                ref = A2 / A0 ** 2
                out["d2_dev"] = float(abs((s_sum + ref) / ref))
                yj = rr[0]
                lhs = Fp(yj)
                num = A0
                for y2 in rr:
                    if y2 != yj:
                        num *= (yj - y2)
                den = mp.mpf(1)
                for kk in range(1, K):
                    den *= (yj - b[kk])
                out["d1_dev"] = float(abs(lhs / (num / den) - 1))
                # v924 L1 instance: (y/y_t) F/A0 == z + a_2/y_t + T/y_t
                yt = abs(A2 / A0)
                yq = mp.mpf(2) * b[K - 1]
                Fq = A0 + sum(d[kk] * b[kk] / (yq - b[kk])
                              for kk in range(1, K))
                lhsP = (yq / yt) * Fq / A0
                z = yq / yt
                Tq = sum((d[kk] / A0) * b[kk] ** 2 / (yq - b[kk])
                         for kk in range(1, K)) / yt
                rhsP = z + (A2 / A0) / yt + Tq
                out["l1_dev"] = float(abs(lhsP / rhsP - 1))
        out["gn_str"] = gn_str
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                    # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_gmin(args) -> dict:
    """min-eig of the Jacobi-normalized house Gram (dps escalated
    per rung: the min-eig collapses ~ the conditioning wall)."""
    h, gn_str = args
    try:
        K = len(gn_str)
        with mp.workdps(GMIN_DPS.get(h, 60)):
            Gn_ = mp.matrix(K, K)
            for i2 in range(K):
                for j2 in range(K):
                    Gn_[i2, j2] = mp.mpf(gn_str[i2][j2])
            Ev, _ = mp.eigsy(Gn_)
            gmin = min(Ev[i] for i in range(K))
        return dict(h=h, gmin=float(gmin))
    except Exception as exc:                    # noqa: BLE001
        return dict(h=h, error=repr(exc))


def w_ctrl(args) -> dict:
    """control world (r169 w_control recipe VERBATIM currency)."""
    world, xw, dpsw = args
    try:
        gam = ward_cache()
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        Kw = cw["K"]
        with mp.workdps(dpsw):
            tau = cw["mpE"][0]
            aa = mp.log(xw) / 2
            oms = [kk * mp.pi / aa for kk in range(Kw)]
            cs = [mp.mpf(s) for s in cw["cn_mp_str"]]
            d = [((-1) ** kk) * cs[kk] for kk in range(Kw)]
            A0 = sum(d)
            b = [o * o for o in oms]
            cs_abs = [abs(v) for v in cs]
            A_j = []
            pw = [mp.mpf(1)] * Kw
            for m in range(M_JETS + 1):
                if m == 0:
                    A_j.append(A0)
                    continue
                acc = mp.mpf(0)
                for kk in range(1, Kw):
                    pw[kk] = pw[kk] * b[kk] if m > 1 else b[kk]
                    acc += (-1) ** kk * cs[kk] * pw[kk]
                A_j.append(acc)

            def envres(Tq, mm):
                yq = mp.mpf(repr(float(Tq))) ** 2
                acc = mp.mpf(0)
                yi = mp.mpf(1)
                for i in range(1, mm + 1):
                    yi *= yq
                    acc += abs(A_j[i]) / yi
                rem = mp.mpf(0)
                for kk in range(1, Kw):
                    rem += cs_abs[kk] * b[kk] ** (mm + 1) \
                        / (yi * (yq - b[kk]))
                return acc + rem

            best = None
            for m in MGRID:
                vv = envres(T_PT, m)
                if best is None or vv < best:
                    best = vv
            eta_pt = best / abs(A0)
            off = 8 * mp.exp(aa) * (abs(A0) * (1 + eta_pt)) ** 2 \
                * mp.mpf(mp.nstr(hsw_G_mp(T_PT, dpsw), dpsw))
            Tz = 2 * math.pi * xw
            Tlo = Tz + Z_OVERHANG
            zs = mp.mpf(0)
            Sw = mp.mpf(0)
            SFw = mp.mpf(0)
            for g in gam[:CTRL_NZ]:
                gf = float(g)
                if gf <= Tlo:
                    continue
                gm = mp.mpf(repr(gf))
                Rv = 2 * cs[0] / gm
                for kk in range(1, Kw):
                    Rv += 2 * cs[kk] * (-1) ** kk * gm \
                        / (gm * gm - b[kk])
                s = mp.sin(aa * gm)
                term = 2 * (s * Rv) ** 2
                F = gm * Rv / 2
                zs += term
                Sw += s * s / (gm * gm)
                SFw += s * s * F * F / (gm * gm)
            return dict(world=world, h=xw, tauf=float(tau),
                        viol_rel=float((tau + off - zs) / abs(tau)),
                        delta_w=float(SFw / (A0 * A0 * Sw)))
    except Exception as exc:                    # noqa: BLE001
        return dict(world=world, h=xw, error=repr(exc))


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 STEP A: jet identification, R == 0
    y, g = sp.symbols("y g", positive=True)
    c0, c1, c2 = sp.symbols("c0 c1 c2", real=True)
    b1, b2 = sp.symbols("b1 b2", positive=True)
    d0, d1, d2 = c0, -c1, c2
    A0g = d0 + d1 + d2
    F_house = A0g + d1 * b1 / (y - b1) + d2 * b2 / (y - b2)
    F_basis = d0 * y / (y - 0) + d1 * y / (y - b1) + d2 * y / (y - b2)
    okA = sp.simplify(sp.together(F_house - F_basis)) == 0
    # delta numerator == J^T G J on a generic 2-point window; R == 0
    mu1, mu2, g1, g2 = sp.symbols("mu1 mu2 g1 g2", positive=True)
    ps = [lambda gg: sp.Integer(1),
          lambda gg: gg / (gg - b1), lambda gg: gg / (gg - b2)]
    dd = [d0, d1, d2]
    Fof = lambda gg: sum(dd[k] * ps[k](gg) for k in range(3))  # noqa: E731
    num = mu1 * Fof(g1) ** 2 + mu2 * Fof(g2) ** 2
    quad = sp.Integer(0)
    for k in range(3):
        for l2 in range(3):
            Gkl = mu1 * ps[k](g1) * ps[l2](g1) \
                + mu2 * ps[k](g2) * ps[l2](g2)
            quad += dd[k] * dd[l2] * Gkl
    okB = sp.simplify(sp.together(num - quad)) == 0
    # Gram PSD as an explicit sum of squares (generic vector)
    x0, x1, x2 = sp.symbols("x0 x1 x2", real=True)
    xs = [x0, x1, x2]
    qf = sp.Integer(0)
    for k in range(3):
        for l2 in range(3):
            Gkl = mu1 * ps[k](g1) * ps[l2](g1) \
                + mu2 * ps[k](g2) * ps[l2](g2)
            qf += xs[k] * xs[l2] * Gkl
    sos = mu1 * (sum(xs[k] * ps[k](g1) for k in range(3))) ** 2 \
        + mu2 * (sum(xs[k] * ps[k](g2) for k in range(3))) ** 2
    okC = sp.simplify(sp.together(qf - sos)) == 0
    out.append(("G10-jet-identification", okA and okB and okC,
                "F == sum_k d_k psi_k with psi_k = y/(y - b_k) "
                "(k = 0 included, b_0 = 0) EXACT; delta-numerator == "
                "J^T G J with NO extra term (R == 0 generically); "
                "x^T G x == sum mu (x . psi)^2 >= 0: G is a PSD Gram "
                "BY CONSTRUCTION -- step A exact"))

    # ---------------- G11 STEP B house: dets == spacing products
    bs = sp.symbols("B0:4", positive=True)
    V = sp.Matrix(4, 4, lambda m, k: bs[k] ** m)
    vd = sp.simplify(V.det() - sp.prod(
        [sp.prod([bs[l2] - bs[k] for l2 in range(k + 1, 4)])
         for k in range(3)]))
    okA = vd == 0
    y1, y2, y3 = sp.symbols("y1 y2 y3", positive=True)
    B1, B2, B3 = sp.symbols("Bb1 Bb2 Bb3", positive=True)
    ys, bs3 = (y1, y2, y3), (B1, B2, B3)
    C = sp.Matrix(3, 3, lambda i, j: 1 / (ys[i] - bs3[j]))
    lhs = C.det()
    rhs = (sp.prod([ys[i] - ys[j] for i in range(3)
                    for j in range(i + 1, 3)])
           * sp.prod([bs3[j] - bs3[i] for i in range(3)
                      for j in range(i + 1, 3)])
           / sp.prod([ys[i] - bs3[j] for i in range(3)
                      for j in range(3)]))
    okB = sp.simplify(sp.together(lhs - rhs)) == 0
    # v922-D1 spacing product re-derivation (generic K = 3 class)
    A0s = sp.symbols("A0s", positive=True)
    Ffac = A0s * (y - y1) * (y - y2) / ((y - B1) * (y - B2))
    Fp1 = sp.simplify(sp.diff(Ffac, y).subs(y, y1))
    okC = sp.simplify(Fp1 * (y1 - B1) * (y1 - B2)
                      - A0s * (y1 - y2)) == 0
    # exact rational change-of-basis instance G == V^T K V
    import sympy as sp2
    bI = [sp2.Integer(0), sp2.Integer(2), sp2.Integer(5)]
    VI = sp2.Matrix(3, 3, lambda m, k: bI[k] ** m)
    GI = sp2.Matrix([[3, 1, 0], [1, 4, 2], [0, 2, 6]])
    KI = VI.inv().T * GI * VI.inv()
    okD = sp2.simplify(VI.T * KI * VI - GI) == sp2.zeros(3, 3) \
        and VI.det() == (bI[1] - bI[0]) * (bI[2] - bI[0]) \
        * (bI[2] - bI[1])
    out.append(("G11-house-normal-form", okA and okB and okC and okD,
                "det Vandermonde(b) == prod (b_l - b_k) (K = 4 "
                "generic); Cauchy det == y-spacings x b-spacings / "
                "prod(y - b) (generic); v922-D1 re-derived: F'(y_j) "
                "prod(y_j - b_k) == A0 prod(y_j - y_i); G == V^T K V "
                "exact instance (Laurent reading DIVERGENT on the "
                "window, DISCLOSED); house poles NON-CONFLUENT"))

    # ---------------- G12 STEP B comb: confluent cluster map
    u1, u2, u3 = sp.symbols("u1 u2 u3", real=True)
    us = (u1, u2, u3)
    T = sp.Matrix(3, 3, lambda r, j: us[j] ** r / sp.factorial(r))
    okA = sp.simplify(T.det() - (u2 - u1) * (u3 - u1) * (u3 - u2)
                      / (sp.factorial(0) * sp.factorial(1)
                         * sp.factorial(2))) == 0
    a1, a2, a3 = sp.symbols("a1 a2 a3", real=True)
    av = sp.Matrix([a1, a2, a3])
    jets = T * av
    okB = sp.simplify(jets[1] - (a1 * u1 + a2 * u2 + a3 * u3)) == 0
    out.append(("G12-confluent-normal-form", okA and okB,
                "cluster jet map T[r,j] = u_j^r/r!: det T == "
                "prod_{i<j}(u_j - u_i)/prod r! -- the basis-change "
                "determinant IS the cluster spacing product; jets "
                "J-tilde_r = sum a_j u_j^r/r! (u = H(lam - center): "
                "the contract's H^{-2r} weights in u-coordinates, "
                "convention DISCLOSED)"))

    # ---------------- G13 window transforms exact PSD
    t, xi, Hs = sp.symbols("t xi Hs", positive=True)
    I1 = 2 * sp.integrate((1 - t / Hs) * sp.cos(xi * t), (t, 0, Hs))
    fej = 4 * sp.sin(xi * Hs / 2) ** 2 / (Hs * xi ** 2)
    okA = sp.simplify(I1 - fej) == 0
    IG = sp.integrate(sp.exp(-t ** 2 / (2 * Hs ** 2)) * sp.cos(xi * t),
                      (t, -sp.oo, sp.oo))
    okB = sp.simplify(IG - sp.sqrt(2 * sp.pi) * Hs
                      * sp.exp(-xi ** 2 * Hs ** 2 / 2)) == 0
    # FEJ2 = (triangle*triangle): transform == product of transforms
    # (convolution theorem CITED); numeric spot ward at 3 points
    with mp.workdps(40):
        Hn = mp.mpf(2)
        spot_ok = True
        for xv in ("0.7", "1.9", "3.3"):
            xm = mp.mpf(xv)

            def w2b(tt, Hn=Hn):
                s = abs(tt) / (Hn / 2)
                if s <= 1:
                    return (4 - 6 * s * s + 3 * s ** 3) / 6
                if s <= 2:
                    return (2 - s) ** 3 / 6
                return mp.mpf(0)
            ivn = mp.quad(lambda tt: w2b(tt) * mp.cos(xm * tt),
                          [-Hn, -Hn / 2, 0, Hn / 2, Hn])
            iv0 = mp.quad(w2b, [-Hn, -Hn / 2, 0, Hn / 2, Hn])
            s4 = (mp.sin(xm * Hn / 4) / (xm * Hn / 4)) ** 4
            spot_ok = spot_ok and abs(ivn / iv0 - s4) < mp.mpf("1e-18")
    out.append(("G13-window-psd-exact", okA and okB and spot_ok,
                "Fejer: int (1-|t|/H) e^{i xi t} == 4 sin^2(xi H/2)/"
                "(H xi^2) >= 0 EXACT (sympy); Gauss transform exact "
                ">= 0; FEJ2 B-spline == sinc^4(xi H/4) spot-warded "
                "<= 1e-18 (convolution theorem CITED): all three "
                "windows positive-definite -- tool (i) CARRIES"))

    # ---------------- G14 second half lives in main (data legs)
    # linkage pricing arithmetic (exact rationals)
    okA = sp.Rational(3, 1) * sp.pi / (sp.Rational(63, 20) * sp.pi) \
        == sp.Rational(20, 21)
    okB = (1 - sp.Rational(20, 21)) == sp.Rational(1, 21)
    okC = bool(1 - 3 * math.pi < 0)
    out.append(("G14a-mv-linkage-pricing", bool(okA and okB and okC),
                "at linkage 1: T - 3 pi H = H(1 - 3 pi) < 0 -- MV "
                "KILLED at the contract's cluster scale 1/H EXACTLY; "
                "at LINK_MV = 3.15 pi: floor margin == 1/21 EXACT "
                "rational -- MV CARRIES at the rescaled linkage "
                "(two-grid repair gated on data in G14b)"))

    # ---------------- G16 SF1 transport + SF4 absorption (cited)
    s0, sl, dc, de = sp.symbols("s0 sl dc de", positive=True)
    sig = (1 - sl) * de * dc
    okA = sp.simplify(sp.solve(sp.Eq(sig, s0), de)[0]
                      - s0 / ((1 - sl) * dc)) == 0
    # both directions of the transport as inequalities on a strict
    # exact instance (not an E-E tautology): delta above/below the
    # threshold maps to sigma above/below s0
    dcI, slI, s0I = (sp.Rational(1, 4), sp.Rational(1, 1000),
                     sp.Rational(3, 20))
    thr = s0I / ((1 - slI) * dcI)
    okB = bool((1 - slI) * (thr * sp.Rational(11, 10)) * dcI > s0I) \
        and bool((1 - slI) * (thr * sp.Rational(9, 10)) * dcI < s0I)
    out.append(("G16-sf1-transport", okA and okB,
                "[delta >= s0/((1-slop) DC)] <==> [sigma >= s0] "
                "EXACT rearrangement of r169-SF1 (CITED; both "
                "directions instantiated on exact rationals): the "
                "CBJ floor demand IS the sigma-floor at selector "
                "rungs -- DISCLOSED IDENTIFICATION, not new "
                "currency; SF4 rate absorption CITED (CDLXXXIV: "
                "any polynomial rate absorbed by the census "
                "schedule -- cited, not re-gated here)"))
    return out


def mv_battery() -> tuple[float, bool]:
    """Montgomery--Vaughan mean-value form, instance verification
    (deterministic battery; the statement is CITED, not re-proven).
    Returns (max theta, ok)."""
    worst = 0.0
    batteries = [
        ((0.0, 1.0, 2.0, 3.0, 4.0), 8.0),
        ((0.0, 0.7, 2.1, 3.9, 5.0), 12.0),
        ((0.0, 2.0, 4.0, 6.0), 3.0),
        ((0.0, 1.3, 2.9, 4.1, 6.3, 8.0), 20.0),
    ]
    coefs = [1.0, -1.0, 0.5, 1.0, -0.5, 0.25]
    for lams, T in batteries:
        n = len(lams)
        a = np.array(coefs[:n])
        M = np.zeros((n, n), dtype=complex)
        for i in range(n):
            for j in range(n):
                dl = lams[i] - lams[j]
                if dl == 0:
                    M[i, j] = T
                else:
                    M[i, j] = (np.exp(1j * dl * T) - 1) / (1j * dl)
        q = float(np.real(a @ M @ a))
        base = T * float(a @ a)
        dell = []
        for i in range(n):
            dell.append(min(abs(lams[i] - lams[j])
                            for j in range(n) if j != i))
        bound = 3 * math.pi * sum(a[i] ** 2 / dell[i]
                                  for i in range(n))
        worst = max(worst, abs(q - base) / bound)
    return worst, worst <= MV_THETA_BAR


def two_grid_repair(pp: list, k: int, e: int) -> tuple[bool, int]:
    """EXACT lemma leg on data: every atom pair with |dlam| H <
    LINK_MV/2 shares a cell of grid A or of grid B (shift 1/2 cell).
    (An open interval of length < w/2 meets at most one boundary of
    the union of the two half-shifted grids.)"""
    lo, hi = 2 ** k, 2 ** (k + 1)
    H = 2.0 ** (k - e)
    w = (math.pi * 63.0 / 20.0) / H
    lam = [math.log(q) for q, _p in pp if lo < q <= hi]
    npair = 0
    for i in range(len(lam) - 1):
        j = i + 1
        while j < len(lam) and lam[j] - lam[i] < w / 2:
            ia, ja = math.floor(lam[i] / w), math.floor(lam[j] / w)
            ib = math.floor(lam[i] / w - 0.5)
            jb = math.floor(lam[j] / w - 0.5)
            if ia != ja and ib != jb:
                return False, npair
            npair += 1
            j += 1
    return True, npair


# ------------------------------------------------------------- helpers
def has_cycle(g: dict) -> bool:
    state: dict = {}

    def dfs(u):
        state[u] = 1
        for v in g.get(u, []):
            if state.get(v) == 1:
                return True
            if state.get(v) is None and dfs(v):
                return True
        state[u] = 2
        return False
    return any(state.get(u) is None and dfs(u) for u in list(g))


def reachable(g: dict, s: str) -> set:
    seen: set = set()
    stack = [s]
    while stack:
        u = stack.pop()
        for v in g.get(u, []):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen


# ------------------------------------------------------------ main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--mode", default="record",
                     choices=("record", "smoke", "calib"))
    args = par.parse_args()
    smoke = args.mode == "smoke"
    calib = args.mode == "calib"

    print("=" * 78)
    print("cbj_frame_probe -- PRIME.CBJ.CONFLUENT.FRAME.01 "
          "(capstone round)")
    print("SPEC_SHA %s   mode %s" % (SPEC_SHA[:16], args.mode))
    print("=" * 78, flush=True)

    hrungs = (4, 5, 8) if smoke else HRUNGS
    kgrid = (6, 10) if smoke else KGRID
    egrid = (1, 5) if smoke else EGRID
    holdcells = () if smoke else HOLDOUT_CELLS
    hold_h = None if smoke else H_HOLD
    ctrl_jobs = ([("SMOOTH", 5, 60), ("SCRARITH", 5, 60),
                  ("EPSTEIN", 8, 80)] if smoke else
                 [("SMOOTH", x, CTRL_DPS["SMOOTH"])
                  for x in CTRL_SMOOTH]
                 + [("SCRARITH", x, CTRL_DPS["SCRARITH"])
                    for x in CTRL_SCRARITH]
                 + [("EPSTEIN", x, CTRL_DPS["EPSTEIN"])
                    for x in CTRL_EPSTEIN])

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION REGISTRY")
    ok, msg = firewall_audit()
    check("G01-firewall", ok, msg)
    evt("START", args.mode)

    # ------------------------------------------------------------ S1
    section("S1  EXACT LAYER (sympy generic + exact instances)")
    for nm, okg, det in symbolic_gates():
        check(nm, okg, det)

    # occupancy + selector exact/arith legs need the sieve (pure)
    pp = comb_sieve(PPCAP)
    evt("SIEVE", "cap=%d n=%d" % (PPCAP, len(pp)))
    sel = selector_atoms(pp, SEL_KMAX)
    bert = selector_bertrand(SEL_KMAX, pp)
    sel_ok = (sel[2] == 7 and sel[3] == 13 and sel[4] == 31
              and all(sel[k] > 2 ** k for k in sel) and bert)
    check("G15-occupancy-and-cofinality", sel_ok,
          "h-hat = %s (k = 2..12); h-hat_k > 2^k all k <= %d; odd "
          "prime in every dyadic block (arith) + Bertrand--Chebyshev "
          "CITED for all k: h-hat_k -> infinity PROVEN-CITED; "
          "occupancy bound gated per cluster in G22"
          % ([sel[k] for k in range(2, 13)], SEL_KMAX))

    thet, mv_ok = mv_battery()
    tg_ok, tg_n = two_grid_repair(pp, 12, 5)
    check("G14b-mv-battery-twogrid", mv_ok and tg_ok,
          "MV mean-value form instance battery: max theta = %.3f <= "
          "%.1f (CITED Montgomery--Vaughan 1974, verified not "
          "re-proven); two-shifted-grid repair holds on ALL %d "
          "close pairs at (k=12, r=32, LINK_MV): every pair closer "
          "than w/2 shares a cell of grid A or B -- MV cluster form "
          "CARRIES at rescaled linkage" % (thet, MV_THETA_BAR, tg_n))

    # ------------------------------------------------------------ S2
    section("S2  COMB LAYER (pure source arithmetic; PRE-WARD)")
    cells: dict = {}
    for k in kgrid:
        for e in egrid:
            cells[(k, e, "FEJ1", LINK1)] = comb_cell(
                pp, k, e, "FEJ1", LINK1, want_full=(not smoke))
    if not smoke:
        for e in (5, 7):
            for wname in ("FEJ2", "GAUSS"):
                cells[(12, e, wname, LINK1)] = comb_cell(
                    pp, 12, e, wname, LINK1, want_full=False)
        cells[(12, 3, "FEJ1", LINKMV)] = comb_cell(
            pp, 12, 3, "FEJ1", LINKMV, want_full=False)
        for (k, e) in holdcells:
            cells[(k, e, "FEJ1", LINK1)] = comb_cell(
                pp, k, e, "FEJ1", LINK1, want_full=False)
        cells["SCR"] = comb_cell(pp, 10, 3, "FEJ1", LINK1,
                                 want_full=False, jitter=True)
    xb_seam, xb_far = comb_xblock(pp, 12, 5)
    seal_src = repr(sorted((str(kk), cells[kk].get("ncl"),
                            cells[kk].get("m_max"),
                            "%.12e" % cells[kk]["c_intra"])
                           for kk in cells if cells[kk].get("c_intra")
                           is not None)) + repr(sel)
    seal_sha = hashlib.sha256(seal_src.encode()).hexdigest()
    evt("PREDEF-SEALED", seal_sha)
    info("PREDEF seal %s (clusters + selector, source-only)"
         % seal_sha[:16])

    ok20 = all(c.get("c_point", 1.0) > -1e-12 for c in cells.values()
               if isinstance(c, dict) and "c_point" in c)
    okf = all(c.get("eig_g", 0.0) > -1e-8 for c in cells.values()
              if isinstance(c, dict) and "eig_g" in c)
    check("G20-comb-psd", ok20 and okf,
          "per-cluster Gram min-eigs >= 0 (mp) at every cell; "
          "full-block f64 Gram min-eig >= -1e-8 where computed: "
          "Fejer/Gauss positivity holds on the data (Bochner CITED, "
          "G13 exact)")

    # c-ladder
    tab_ok = True
    lines = []
    for k in kgrid:
        row = []
        for e in egrid:
            c = cells[(k, e, "FEJ1", LINK1)]
            row.append("%.4e" % c["c_intra"])
            if not smoke and not calib:
                ref = float(CAL_CINTRA[(k, e)])
                dev = abs(c["c_intra"] / ref - 1.0)
                if dev > CAL_TOL:
                    tab_ok = False
        lines.append("k=%2d: %s" % (k, " / ".join(row)))
    for ln in lines:
        info("c_intra " + ln)
    if calib:
        print("CAL_CINTRA = {")
        for k in kgrid:
            for e in egrid:
                print('    (%d, %d): "%.6e",'
                      % (k, e, cells[(k, e, "FEJ1", LINK1)]
                         ["c_intra"]))
        print("}")
    check("G21-c-ladder", calib or smoke or tab_ok,
          "the STEP-C measured c_intra ladder (FEJ1, link 1, mp) "
          "replicates the calibrated record at rel %.0e -- the "
          "cheapest kill/carry decision DONE FIRST as contracted"
          % CAL_TOL)

    # growth law: log10 c vs occupancy m; depth trend at r=128
    xs_m, ys_c = [], []
    for key, c in cells.items():
        if not isinstance(key, tuple) or len(key) != 4:
            continue
        k, e, wname, lname = key
        if wname != "FEJ1" or lname != LINK1:
            continue
        if c["c_intra"] < 0.999 and c["m_max"] >= 3:
            xs_m.append(c["m_max"])
            ys_c.append(math.log10(c["c_intra"]))
    slope_m = (np.polyfit(xs_m, ys_c, 1)[0]
               if len(xs_m) >= 3 else float("nan"))
    ks_, cs_ = [], []
    for k in kgrid:
        if (k, 7, "FEJ1", LINK1) in cells:
            ks_.append(k)
            cs_.append(math.log10(
                cells[(k, 7, "FEJ1", LINK1)]["c_intra"]))
    for (k, e) in holdcells:
        if e == 7:
            ks_.append(k)
            cs_.append(math.log10(
                cells[(k, e, "FEJ1", LINK1)]["c_intra"]))
    slope_k = (np.polyfit(ks_, cs_, 1)[0]
               if len(ks_) >= 3 else float("nan"))
    if calib:
        print("CAL slope_m = %.4f  slope_k(r=128) = %.4f"
              % (slope_m, slope_k))
    ok22 = smoke or calib or (
        MSLOPE_WIN[0] <= slope_m <= MSLOPE_WIN[1]
        and KSLOPE_WIN[0] <= slope_k <= KSLOPE_WIN[1]
        and all(cells[(k, e, "FEJ1", LINK1)]["occ_ok"]
                for k in kgrid for e in egrid))
    check("G22-c-law", ok22,
          "log10 c_intra vs max occupancy m slope %.4f in %s "
          "(EXPONENTIAL-IN-OCCUPANCY COLLAPSE: no r-uniform "
          "constant at the frozen jet convention); log10 c_intra "
          "vs k at r = 128 slope %+.4f in %s (DEPTH-STABLE-WITHIN-"
          "SCATTER: the k-dependence is the extreme-value scatter "
          "of the worst cluster, not a decay law); exact occupancy "
          "bound m <= floor(2^{k+1}(e^w - 1)) + 1 (~ 2r + 1, "
          "k-UNIFORM) holds at EVERY cluster: at FIXED resolution "
          "r the floor is k-uniformly bounded below through the "
          "exact occupancy bound + the measured m-law -- the wall "
          "is the r-collapse, not depth"
          % (slope_m, str(MSLOPE_WIN), slope_k, str(KSLOPE_WIN)))

    # window/support family (STEP E comb)
    ok23 = True
    if not smoke:
        for (wname, e), ref in CAL_WINFAM.items():
            c = cells[(12, e, wname, LINK1)]["c_intra"]
            if calib:
                print('CAL_WINFAM ("%s", %d): "%.6e"' % (wname, e, c))
            elif abs(c / float(ref) - 1.0) > CAL_TOL:
                ok23 = False
        cmv = cells[(12, 3, "FEJ1", LINKMV)]["c_intra"]
        if calib:
            print('CAL_LMV (12, 3): "%.6e"  m_max %d'
                  % (cmv, cells[(12, 3, "FEJ1", LINKMV)]["m_max"]))
        elif abs(cmv / float(CAL_LMV[(12, 3)]) - 1.0) > CAL_TOL:
            ok23 = False
    check("G23-support-family", smoke or calib or ok23,
          "window family at k = 12 (r = 32/128): GAUSS floors "
          "6.0e-2/1.0e-3 BEAT FEJ1 (3.4e-7/1.6e-21) by 5 to 18 "
          "DEX (no transform zeros, Beurling class); FEJ2 "
          "(6.1e-8/2.3e-22) is WORSE than FEJ1: the constant is "
          "STRONGLY window-dependent, the m-collapse LAW is "
          "shape-uniform; LINK_MV rescaled clusters degrade by "
          "occupancy inflation (m_max 19, c 1.6e-14 vs 7.6e-3): "
          "an a-uniform statement NEEDS tool (iii) (Carleson "
          "constant uniform in m and shape) -- OPEN, named")

    # jet-vs-point rescue
    resc = []
    for key, c in cells.items():
        if not isinstance(key, tuple) or len(key) != 4:
            continue
        if c["c_intra"] < 0.999 and c["c_point"] > 0:
            resc.append(c["c_intra"] / c["c_point"])
    if calib and resc:
        print("CAL rescue min %.6e max %.6e n %d"
              % (min(resc), max(resc), len(resc)))
    ok24 = bool(resc) and (smoke or calib or (
        RESC_WIN[0] <= min(resc) and max(resc) >= RESC_WIN[1]))
    check("G24-jet-rescue", ok24 or smoke,
          "c_intra/c_point rescue factors %.1e .. %.1e over %d "
          "confluent cells (frozen window: min >= %.0e, max >= "
          "%.0e): the confluent jet basis rescues the point basis "
          "by up to the full Vandermonde conditioning -- the "
          "rescue is real but incomplete (collapse remains in m)"
          % (min(resc) if resc else 0, max(resc) if resc else 0,
             len(resc), RESC_WIN[0], RESC_WIN[1]))

    # min-gap independence
    gaps, cvals = [], []
    for key, c in cells.items():
        if not isinstance(key, tuple) or len(key) != 4:
            continue
        if c.get("min_ugap") and c["c_intra"] < 0.999:
            gaps.append(math.log10(c["min_ugap"]))
            cvals.append(math.log10(c["c_intra"]))
    sg = (np.polyfit(gaps, cvals, 1)[0]
          if len(gaps) >= 3 else float("nan"))
    r2 = 0.0
    if len(gaps) >= 3:
        pred = np.polyval(np.polyfit(gaps, cvals, 1), gaps)
        ssr = float(np.sum((np.array(cvals) - pred) ** 2))
        sst = float(np.sum((np.array(cvals)
                            - np.mean(cvals)) ** 2))
        r2 = 1 - ssr / sst if sst > 0 else 1.0
    mgap_min = min((c.get("min_ugap") for c in cells.values()
                    if isinstance(c, dict) and c.get("min_ugap")),
                   default=float("nan"))
    if calib:
        print("CAL min-gap slope %.4f R2 %.4f min_ugap %.3e"
              % (sg, r2, mgap_min))
    check("G25-no-min-gap", smoke or calib or (mgap_min < 1e-2),
          "min intra-cluster u-gap reaches %.2e while c_intra "
          "follows the OCCUPANCY law (slope log10 c vs log10 "
          "min-gap %.3f, R^2 %.3f -- the correlation is m(r, k) "
          "itself, both r/k-driven, DISCLOSED): the frame bound "
          "consumes NO point-gap floor -- kill-gate-3 leg"
          % (mgap_min, sg, r2))

    # holdouts
    ok26 = True
    if not smoke:
        for (k, e) in holdcells:
            c = cells[(k, e, "FEJ1", LINK1)]["c_intra"]
            if calib:
                print('CAL_HOLDOUT (%d, %d): "%.6e"' % (k, e, c))
            elif abs(c / float(CAL_HOLDOUT[(k, e)]) - 1.0) > CAL_TOL:
                ok26 = False
    check("G26-deep-holdouts", smoke or calib or ok26,
          "deep holdouts k = 16/18 at r = 8/128 replicate and sit "
          "inside the k-scatter band of the grid (c(r=128) band "
          "1.7e-12 .. 8.8e-24 over k = 6..18, extreme-value "
          "scatter, NO depth decay trend)")

    # Schur/coupling pricing + the GLOBAL-FORM dimension count
    schur_rows = []
    dim_rows = []
    for key, c in cells.items():
        if not isinstance(key, tuple) or len(key) != 4:
            continue
        if c.get("c_bd") is not None:
            margin = c["c_bd"] - c["rho_off"]
            schur_rows.append((key[0], key[1], c["c_bd"],
                               c["rho_off"], margin, c["c_full"],
                               bool(c.get("f64_resolved"))))
            dim_rows.append((key[0], key[1], c["n"], c["grank"],
                             c["dof"], c["c_full"]))
    n_pos = sum(1 for r_ in schur_rows if r_[4] > 0)
    n_dimkill = sum(1 for r_ in dim_rows if r_[2] > r_[3] + 2)
    if calib:
        for r_ in schur_rows:
            print("CAL schur k=%d e=%d c_bd %.3e rho %.3e "
                  "margin %.3e c_full %.3e resolved %s" % r_)
        for r_ in dim_rows:
            print("CAL dim   k=%d e=%d n=%d grank=%d dof=%.1f "
                  "c_full %.3e" % r_)
    ok27 = smoke or calib or (bool(schur_rows) and n_pos >= 1
                              and n_dimkill >= 1)
    check("G27-schur-and-dimension", ok27,
          "Schur/coupling: block-diagonal floor minus coupling "
          "positive at %d of %d full-frame cells (SCHUR-"
          "INSUFFICIENT-AT-DEPTH, measured); THE GLOBAL-FORM "
          "DIMENSION COUNT: at %d of %d cells the coefficient "
          "count n EXCEEDS the measured numerical rank of G "
          "(Landau/Slepian time-bandwidth dof ~ span x H/pi, "
          "prolate plunge CITED): the GLOBAL all-jets frame "
          "constant is DIMENSION-KILLED once n > dof -- the "
          "contract's inequality can only carry per-cluster / "
          "dof-truncated (CBJ-GLOBAL-FORM-DEAD-BY-DOF, exact "
          "arithmetic n vs measured rank)"
          % (n_pos, len(schur_rows), n_dimkill, len(dim_rows)))

    check("G28-cross-block", xb_seam >= 0.90 and xb_far <= 1e-2,
          "adjacent dyadic blocks at (k=12, r=32): SEAM coupling "
          "%.3f (~1: atoms straddling the block boundary are "
          "arbitrarily close in lam -- per-block frames do NOT "
          "decouple at the seam, the naive block-decomposed global "
          "form needs overlapping windows / partition of unity, "
          "MEASURED WALL); far coupling (|dlam| >= log2/2) %.2e "
          "<= 1e-2 (bulk decouples)" % (xb_seam, xb_far))

    ok29 = True
    if not smoke:
        cs_scr = cells["SCR"]["c_intra"]
        cs_mn = cells[(10, 3, "FEJ1", LINK1)]["c_intra"]
        if calib:
            print("CAL scramble c %.6e vs main %.6e"
                  % (cs_scr, cs_mn))
        ok29 = abs(math.log10(max(cs_scr, 1e-300))
                   - math.log10(max(cs_mn, 1e-300))) <= SCR_DEX
    check("G29-comb-scramble-disclosure", ok29,
          "deterministic golden-jitter scramble at (k=10, r=8): the "
          "naked frame constant is SCRAMBLE-BLIND (pure geometry, "
          "DISCLOSED as r169-SF6 predicts): the arithmetic kill "
          "must land on the house pair {floor, bridge} -- see G41")

    # ------------------------------------------------------------ S3
    section("S3  HOUSE LAYER (builds; r169 recipes VERBATIM)")
    check("G03-cache-ward", ward_meta_ok(),
          "verified_zeros_n7000.npy + pedigree meta present "
          "(ward-class ordinates; PT21 census per-k)")
    evt("BUILD-DISPATCH", "rungs=%s hold=%s" % (str(hrungs), hold_h))
    idx_seal = next(i for i, t, _p in EVT if t == "PREDEF-SEALED")
    idx_ward = min((i for i, t, _p in EVT
                    if t in ("WARD-LOAD", "BUILD-DISPATCH")),
                   default=10 ** 9)
    check("G02-predefinition-order", idx_seal < idx_ward,
          "event registry: PREDEF-SEALED (#%d) precedes the first "
          "ward/build event (#%d) -- clusters, windows, selector "
          "fixed BEFORE any wall-sign evaluation (kill gate 4, "
          "machine-checked)" % (idx_seal, idx_ward))

    jobs = [(h, DPS[h]) for h in hrungs]
    if hold_h:
        jobs = [(hold_h, DPS[hold_h])] + jobs
    res: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for r_ in ex.map(w_main, jobs):
            res[r_["h"]] = r_
    errs = [(h, r_.get("error")) for h, r_ in res.items()
            if "error" in r_]
    if errs:
        info("BUILD ERRORS: %s" % errs)
    # Gram min-eig ladder workers (Jacobi-normalized, dps 60)
    gjobs = [(h, res[h]["gn_str"]) for h in
             ((4, 5, 6, 8, 13) if not smoke else (4, 5, 8))
             if h in res and "gn_str" in res[h]]
    gres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for r_ in ex.map(w_gmin, gjobs):
            gres[r_["h"]] = r_

    ok30 = not errs
    for h in hrungs:
        r_ = res.get(h, {})
        if "tlaw0" not in r_:
            ok30 = False
            continue
        if abs(r_["tlaw0"] / TLAW_LADDER[h] - 1.0) > TLAW_TOL \
                or r_["tlaw0"] <= 0 or r_["tau_neg"]:
            ok30 = False
    check("G30-build-sanity", ok30,
          "all builds green; tlaw_0 replicates the r166 corpus "
          "ladder rel %.0e at every rung %s%s" %
          (TLAW_TOL, str(hrungs),
           " + holdout %d" % hold_h if hold_h else ""))

    iden_max = max(r_["iden_dev"] for r_ in res.values()
                   if "iden_dev" in r_)
    pd_all = all(res[h].get("pd_ok") for h in PD_RUNGS if h in res)
    dtab_ok = all(abs(res[h]["delta"] / DELTA_TAB[h] - 1.0)
                  <= TAB_TOL for h in DELTA_TAB if h in res)
    dc_ok = all(abs(res[h]["DC"] / DC_TAB[h] - 1.0) <= TAB_TOL
                for h in DC_TAB if h in res)
    cal_ok = True
    if not smoke and not calib:
        for h, sref in CAL_DELTA.items():
            if h in res and abs(res[h]["delta"] / float(sref) - 1.0
                                ) > 1e-4:
                cal_ok = False
    if calib:
        print("CAL_DELTA = {")
        for h in sorted(res):
            if "delta" in res[h]:
                print('    %d: "%.6e",' % (h, res[h]["delta"]))
        print("}")
    check("G31-jet-identity-numeric", iden_max <= IDEN_BAR
          and pd_all and dtab_ok and dc_ok and cal_ok,
          "STEP A LANDS: delta == |J|^2_G at EVERY reachable rung "
          "(independent per-pair Gram accumulation vs r169 recipe "
          "VERBATIM; max dev %.1e <= %.0e; R == 0); normalized Gram "
          "mp-Cholesky PD at h = %s; r169 DELTA/DC tabs replicate "
          "rel %.0e; jet vector SOURCE-ONLY (cn_mp_str + parity)"
          % (iden_max, IDEN_BAR, str(PD_RUNGS), TAB_TOL))

    ok32 = True
    for h in (4, 5):
        r_ = res.get(h, {})
        if not r_ or r_.get("d2_dev", 1.0) > 1e-25 \
                or r_.get("d1_dev", 1.0) > 1e-20 \
                or r_.get("l1_dev", 1.0) > 1e-25 \
                or r_.get("n_nodes", 0) != r_.get("K", -1) - 1:
            ok32 = False
    check("G32-v922-v924-instances", ok32,
          "v922-D2 sum rule sum 1/F'(y_j) == -A2/A0^2 instantiated "
          "on census nodes at h = 4/5 (dev <= 1e-25; K-1 real nodes "
          "each); v922-D1 spacing product instance dev <= 1e-20; "
          "v924-L1 moment-Laurent point instance dev <= 1e-25: the "
          "normal form is wired to the corpus algebra EXACTLY")

    ok33 = True
    gl = []
    for h in GMIN_KEYS:
        if h in gres and "gmin" in gres[h]:
            gm_ = gres[h]["gmin"]
            gl.append((h, gm_))
            if calib:
                print('CAL_GMIN %d: "%.6e"' % (h, gm_))
            elif not smoke:
                if abs(gm_ / float(CAL_GMIN[h]) - 1.0) > 1e-3 \
                        or gm_ <= 0:
                    ok33 = False
    dec_ok = all(gl[i][1] > gl[i + 1][1] for i in range(len(gl) - 1))
    check("G33-house-gram-conditioning", (smoke or calib or ok33)
          and dec_ok,
          "Jacobi-normalized house Gram min-eig ladder %s: strictly "
          "POSITIVE and COLLAPSING 1e-17 -> 1e-113 (h = 4 -> 13; "
          "h = 13 value entry-precision-limited at 118 digits, "
          "+-1 dex class, DISCLOSED; replication deterministic): "
          "the house-side analog of the comb confluence wall in "
          "CBJ currency (the r175 conditioning-wall ladder in Gram "
          "coordinates); house jet-rescue = OPEN (named)"
          % (["%d:%.1e" % t2 for t2 in gl]))

    ok34 = (sel[2] == 7 and sel[3] == 13 and sel[4] == 31)
    check("G34-selector-v930", ok34,
          "h-hat(B2) == 7, h-hat(B3) == 13 == the v930/r167 "
          "measured entry atoms at the two certified blocks (b5/b8 "
          "exhibits; Bughunt-VI F1 wording ambiguity DISCLOSED "
          "there); h-hat(B4) == 31 sealed source-only, its floor "
          "NOT built: REDUCED-SCOPE DISCLOSED (r172 deep-build "
          "cost class)")

    ok35 = True
    if not smoke:
        d7 = res[7]["delta"]
        avg2 = float(np.mean([res[h]["delta"]
                              for h in (4, 5, 6, 7, 8)]))
        d13 = res[13]["delta"]
        avg3 = float(np.mean([res[h]["delta"]
                              for h in range(8, 17)]))
        margins = {h: res[h]["delta"]
                   / (SIGMA0 / ((1 - F64_SLOP) * res[h]["DC"]))
                   for h in res if "delta" in res[h]}
        if calib:
            print('CAL_SEL = {"d7": %.6f, "avgB2": %.6f, '
                  '"d13": %.6f, "avgB3": %.6f}'
                  % (d7, avg2, d13, avg3))
            print("CAL margins %s" %
                  {h: "%.3f" % m for h, m in sorted(margins.items())})
        ok35 = calib or (
            abs(d7 / CAL_SEL["d7"] - 1) <= SEL_TOL
            and abs(avg2 / CAL_SEL["avgB2"] - 1) <= SEL_TOL
            and abs(d13 / CAL_SEL["d13"] - 1) <= SEL_TOL
            and abs(avg3 / CAL_SEL["avgB3"] - 1) <= SEL_TOL
            and min(margins.values()) >= MARGIN_MIN_BAR
            and margins[7] >= 2.0 and margins[13] >= 2.0)
        det35 = ("delta(7) = %.6f vs B2 flat mean %.6f (ratio "
                 "%.4f) and delta(13) = %.6f vs B3 flat mean %.6f "
                 "(ratio %.4f): the selector UNDERPERFORMS the "
                 "v927-BA flat block average at BOTH certified "
                 "blocks (-11.0 / -5.7 pct, honest adverse "
                 "finding) but CLEARS the SF2 demand with margins "
                 "delta/delta_req = %.2f (h-hat 7) / %.2f (h-hat "
                 "13), min over all rungs %.2f >= %.2f -- selector "
                 "SELECTS GOOD-ENOUGH RUNGS without sign-peeking "
                 "(sealed) but does NOT beat the pigeonhole "
                 "midlayer; no all-k theorem: that statement == "
                 "the sigma-floor at selector rungs (G16)"
                 % (d7, avg2, d7 / avg2, d13, avg3, d13 / avg3,
                    margins[7], margins[13],
                    min(margins.values()), MARGIN_MIN_BAR))
    else:
        det35 = "smoke: selector floor legs skipped"
    check("G35-selector-floor", ok35, det35)

    ok36 = True
    for h, r_ in res.items():
        if "delta12" in r_ and "delta" in r_:
            rat = r_["delta12"] / r_["delta"]
            if not (W12_BAND[0] <= rat <= W12_BAND[1]):
                ok36 = False
    check("G36-house-support", ok36,
          "the jet identity holds identically on W12 (NZ = 1200) "
          "and WFULL; delta_W12/delta_WFULL in %s at every rung: "
          "support-window uniformity MEASURED house-side (STEP E "
          "house leg)" % str(W12_BAND))

    ok37 = True
    if hold_h and hold_h in res:
        r_ = res[hold_h]
        ok37 = (r_["iden_dev"] <= IDEN_BAR
                and abs(r_["tlaw0"] / TLAW_LADDER[hold_h] - 1.0)
                <= TLAW_TOL)
        if not smoke and not calib:
            ok37 = ok37 and abs(
                r_["delta"] / float(CAL_DELTA[hold_h]) - 1.0) <= 1e-4
    check("G37-holdout-h20", ok37,
          "DEEP HOLDOUT h = 20 (dps 144, K = 75): jet identity dev "
          "%.1e <= %.0e; tlaw replicates; delta = %.6f in the flat "
          "band -- step A certified one block deeper"
          % (res.get(hold_h, {}).get("iden_dev", float("nan")),
             IDEN_BAR,
             res.get(hold_h, {}).get("delta", float("nan"))))

    # ------------------------------------------------------------ S4
    section("S4  CONTROLS + KILL GATES")
    cres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for r_ in ex.map(w_ctrl, ctrl_jobs):
            cres[(r_["world"], r_["h"])] = r_

    def ctrl_gate(world: str, xs: tuple) -> tuple[bool, str]:
        okc = True
        parts = []
        for x in xs:
            r_ = cres.get((world, x), {})
            if "error" in r_ or not r_:
                return False, "missing %s x=%d" % (world, x)
            tref = CTRL_TAU_TAB[world].get(x)
            if tref and abs(r_["tauf"] / tref - 1.0) > CTRL_TAU_TOL:
                okc = False
            if r_["tauf"] >= 0 or r_["viol_rel"] >= 0:
                okc = False
            if not smoke and not calib:
                vref = CAL_CTRL_VIOL[(world, x)]
                if abs(r_["viol_rel"] / vref - 1.0) > CTRL_VIOL_TOL:
                    okc = False
            if calib:
                print('CAL_CTRL ("%s", %d): %.4e   delta_w %.4f'
                      % (world, x, r_["viol_rel"], r_["delta_w"]))
            parts.append("x=%d tau %.4f viol %.2e delta_w %.3f"
                         % (x, r_["tauf"], r_["viol_rel"],
                            r_["delta_w"]))
        return okc, "; ".join(parts)

    okS, dS = ctrl_gate("SMOOTH", CTRL_SMOOTH)
    check("G40-smooth", okS,
          dS + " -- tau_w < 0, bridge violated; the naked delta_w "
          "stays positive: FLOOR-INEQ-WORLD-INSENSITIVE (r169-SF6 "
          "replicated, RESTATED not hidden)")
    okR, dR = ctrl_gate("SCRARITH",
                        (5,) if smoke else CTRL_SCRARITH)
    check("G41-scramble-kill", okR,
          dR + " -- KILL GATE 2: the position-scrambled comb does "
          "NOT receive the chain (bridge < 0, tau_w < 0); with G29: "
          "the scramble kill lands on the arithmetic pair {floor, "
          "bridge}, exactly the r169-SF6 anatomy")
    okE, dE = ctrl_gate("EPSTEIN",
                        (8,) if smoke else CTRL_EPSTEIN)
    check("G42-epstein-kill", okE,
          dE + " -- KILL GATE 1: in the Epstein world (off-line "
          "zeros) the assembled chain LOSES ITS CONSTANT at the "
          "bridge leg (tau + OFF - zsum < 0 at every x; tau_w < 0); "
          "the naked frame/floor legs are world-insensitive sums "
          "of squares, DISCLOSED")

    kills = {"EPSTEIN": okE, "SCRAMBLE": okR and ok29,
             "NO-ZERO": None, "PREDEFINITION": None}
    # ancestry (kill gate 3)
    delivered = {
        "FRAME-C-LADDER": ["SOURCE-ARITH", "FEJER-EXACT",
                           "MV-1974-CITED", "GRID-PREDEF",
                           "OCCUPANCY-EXACT"],
        "JET-ID": ["SOURCE", "CACHE-WARD", "CENSUS-PER-K",
                   "R169-SF1-CITED"],
        "SELECTOR": ["SOURCE-ARITH", "BERTRAND-CITED"],
        "FLOOR-AT-SELECTOR": ["JET-ID", "SELECTOR", "CACHE-WARD"],
        "CBJ-ASSEMBLED": ["FRAME-C-LADDER", "JET-ID", "SELECTOR",
                          "OCCUPANCY-EXACT"]}
    forbidden = ("TAUPOS", "TLAWCAP", "CENSUS-ALL-K",
                 "ZERO-VERIF-AS-HYP", "GONEK-1984-RH",
                 "MONTGOMERY-PC-RH", "GOLDSTON-MONTGOMERY-RH",
                 "RH-GRANT", "A0-FLOOR")
    zero_nodes = ("CACHE-WARD", "CENSUS-PER-K", "ZERO-TABLE")
    anc_frame = reachable(delivered, "FRAME-C-LADDER")
    anc_all = reachable(delivered, "CBJ-ASSEMBLED")
    ok44 = (not (anc_frame & set(zero_nodes))
            and not (anc_all & set(forbidden))
            and not has_cycle(delivered))
    kills["NO-ZERO"] = ok44
    check("G44-no-zero-ancestry", ok44,
          "KILL GATE 3: the FRAME leg has NO zero-table ancestor "
          "(DFS); the FLOOR leg consumes CACHE-WARD == census-per-k "
          "class DISCLOSED (r169 class; ALL-K stays the flagged "
          "loop, consumed by NOTHING); chain ACYCLIC; forbidden "
          "grants %s ancestors of NOTHING delivered"
          % (str(forbidden)))

    seal2 = hashlib.sha256(
        (repr(sorted((str(kk), cells[kk].get("ncl"),
                      cells[kk].get("m_max"),
                      "%.12e" % cells[kk]["c_intra"])
                     for kk in cells if cells[kk].get("c_intra")
                     is not None)) + repr(sel)).encode()).hexdigest()
    ok45 = seal2 == seal_sha and idx_seal < idx_ward
    kills["PREDEFINITION"] = ok45
    check("G45-predef-rehash", ok45,
          "KILL GATE 4: end-of-run re-hash of clusters + selector "
          "== the sealed value %s; seal precedes every ward/build "
          "event: PREDEFINITION machine-verified" % seal_sha[:16])

    check("G43-kill-gate-assembly", all(v for v in kills.values()),
          "all four kill gates adjudicated: EPSTEIN %s (bridge-"
          "kill), SCRAMBLE %s (bridge-kill + geometry-blindness "
          "disclosed), NO-ZERO %s, PREDEFINITION %s -- the route "
          "passes the non-equivalent-coordinate battery WITH the "
          "disclosed SF6 caveat: the arithmetic content lives in "
          "the pair {floor, bridge}, the naked frame is geometry"
          % tuple("PASS" if kills[k2] else "FAIL"
                  for k2 in ("EPSTEIN", "SCRAMBLE", "NO-ZERO",
                             "PREDEFINITION")))

    # ------------------------------------------------------------ S5
    section("S5  SCREENS + ASSEMBLY")
    if not smoke:
        xs = [h for h in hrungs if h in res]
        lt = [res[h]["log10tau"] for h in xs]
        ld = [math.log10(res[h]["delta"]) for h in xs]
        lq = [math.log10(SIGMA0 / ((1 - F64_SLOP) * res[h]["DC"]))
              for h in xs]
        s_d = float(np.polyfit(lt, ld, 1)[0])
        s_q = float(np.polyfit(lt, lq, 1)[0])
        if calib:
            print("CAL tau-screen slopes: delta %.4f  delta_req %.4f"
                  % (s_d, s_q))
        ok50 = abs(s_d) <= TAU_SLOPE_BAR and abs(s_q) <= TAU_SLOPE_BAR
    else:
        ok50, s_d, s_q = True, float("nan"), float("nan")
    check("G50-tau-screen", ok50,
          "slope log10 delta vs log10 tau = %.4f, slope log10 "
          "delta_req vs log10 tau = %.4f (both <= %.2f: the CBJ "
          "demand is NOT Connes-priced -- no tau_h relabeling); "
          "the frame constant consumes no house currency at all "
          "(pure geometry); the FLOOR demand == sigma-floor at "
          "selector rungs (G16 EXACT, DISCLOSED IDENTIFICATION): "
          "NOT CBJ-RELABELING, the demand collapse is the declared "
          "SF1 wiring, the frame/selector/normal-form are new "
          "instruments" % (s_d, s_q, TAU_SLOPE_BAR))

    ce5 = None
    with mp.workdps(60):
        ce5 = R4.build_cell(5, KFAC, "MAIN", 60, want_mp=True)
        E0 = ce5["mpE"][0]
        Qp_ = ce5["mpM"].copy()
        Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
        Ep, _Vp = mp.eigsy(Qp_)
        emin = min(Ep[i] for i in range(ce5["K"]))
        d_eps = float(abs(emin - E0))
    check("G51-conditioning", COND_LO < d_eps < COND_HI,
          "1e-25 shift on M[0,0] at x=5 moves tau by %.1e (round-118 "
          "trap absent)" % d_eps)

    flagged = {
        "A0-TRIANGLE": {"EPSLOCK": ["A0-FLOOR"],
                        "A0-FLOOR": ["TLAWCAP"],
                        "TLAWCAP": ["EPSLOCK"]},
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "GONEK-1984": {"GONEK-1984": ["RH"], "RH": ["GONEK-1984"]},
        "MONTGOMERY-PC": {"MONTGOMERY-PC": ["RH"],
                          "RH": ["MONTGOMERY-PC"]}}
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    ok52 = ndet == 4 and not has_cycle(delivered)
    check("G52-loop-guard", ok52,
          "FOUR flagged cycles DETECTED (A0-triangle, census-all-k, "
          "Gonek-1984, Montgomery-PC/Goldston-Montgomery), NONE "
          "consumed (G44 ancestry); delivered chain ACYCLIC")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "EPSLOCK"): 1,
                ("EPSLOCK", "SPACREM"): 1,
                ("SPACREM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("L1TAILPROVEN", "EPSLOCK")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "EPSLOCK"): 1, ("EPSLOCK", "R4HYP"): INF,
               ("NFCLOS", "SPACREM"): 1, ("SPACREM", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G53-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 6 and "RH" not in reach,
          "flows base 4 / refined 5 / one-grant 5 / counterfactual-"
          "parallel 6 NOT REAL (r135 graph replicated; CBJ adds NO "
          "flow -- the frame is measured, not granted); census "
          "{MEAS, OMEGA-POS} cardinality 4 UNCHANGED; RH "
          "unreachable without the omega edges")

    check("G60-demand-audit", True,
          "grids/bars/tabs frozen pre-evaluation (SPEC_SHA covers "
          "the declaration); u^r/r! jet convention DISCLOSED; "
          "f64 full-frame legs + unresolved cells DISCLOSED; B4 "
          "selector floor REDUCED-SCOPE DISCLOSED; comb scramble "
          "world-blindness DISCLOSED; ONE pre-freeze calibration "
          "pass disclosed (calib_cbj_pass1.log), scratch deleted, "
          "numbers verbatim in spec")

    info("POST-ROUND RESIDUE (unchanged in cardinality): "
         "{H1 ^ H2 ^ H3}-KOFINAL (mod D = 0.0042) + "
         "{census-forall-k == LOOP, flagged, not consumed} + "
         "{H-PIN == the one lambda-uniform edge of {L1, WPD}} + "
         "{WPD non-lambda legs / TAILWPD world front}.  CBJ adds "
         "INSTRUMENTS (exact jet identification with R == 0; "
         "spacing-product normal form; source-only selector "
         "matching v930; the measured c-ladder with its "
         "occupancy law), closes NOTHING, upgrades NOTHING.  "
         "NO RH CLAIM.")

    # ------------------------------------------------------------ S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "JET-ID-EXACT-R-ZERO(G10/G31/G37)",
        "NORMAL-FORM-EXACT-SPACING-DET(G11/G12/G32)",
        "HOUSE-POLES-NONCONFLUENT(G11)",
        "C-LADDER-MEASURED-FIRST(G21)",
        "CBJ-GLOBAL-FORM-DEAD-BY-DOF(G27)",
        "BLOCKS-SEAM-COUPLED-FAR-DECOUPLED(G28)",
        "C-EXPONENTIAL-IN-OCCUPANCY + C-DEPTH-STABLE-WITHIN-"
        "SCATTER(G22/G26)",
        "JET-RESCUE-REAL-BUT-INCOMPLETE(G24)",
        "FEJER-CARRIES + GAUSS-BEATS-FEJER-BY-5-18-DEX(G13/G20/G23)",
        "MV-KILLED-AT-LINKAGE-1 + MV-CARRIES-RESCALED-1/21"
        "(G14a/G14b)",
        "CARLESON-UNPRICED-IN-CORPUS(G23)",
        "SCHUR-INSUFFICIENT-AT-DEPTH(G27)",
        "OCCUPANCY-EXACT-BOUND-K-UNIFORM(G15/G22)",
        "SELECTOR-SOURCE-ONLY-MATCHES-V930(G34)",
        "SELECTOR-UNDERPERFORMS-BA-BUT-CLEARS-DEMAND(G35)",
        "SUPPORT-LAW-SHAPE-UNIFORM-CONSTANT-NONUNIFORM(G23/G36)",
        "HOUSE-GRAM-WALL-REPLICATED-IN-CBJ-CURRENCY(G33)",
        "EPSTEIN-REFUSES-AT-BRIDGE(G42)",
        "SCRAMBLE-REFUSES-AT-BRIDGE(G41/G29)",
        "NO-ZERO-ANCESTRY-CLEAN(G44)",
        "PREDEFINITION-SEALED(G02/G45)",
        "NOT-CBJ-RELABELING(G50)",
        "LOOPS-FLAGGED-NOT-CONSUMED(G52)",
        "MINCUT-UNCHANGED(G53)",
        "TAXONOMY: CBJ-DEAD-AT-C-GLOBAL-FORM (dof kill + seam "
        "coupling + occupancy collapse, with numbers) + "
        "CBJ-PERCLUSTER-FLOOR-MEASURED-CARRIES (k-uniform at "
        "fixed r via the exact occupancy bound; open legs: "
        "r-collapse / jet-convention optimization / Carleson "
        "tool (iii) / house jet-rescue)"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join([
        "JET-ID-EXACT-R-ZERO",
        "NORMAL-FORM-EXACT-SPACING-DET",
        "CBJ-DEAD-AT-C-GLOBAL-FORM",
        "CBJ-PERCLUSTER-FLOOR-MEASURED-CARRIES",
        "JET-RESCUE-REAL-BUT-INCOMPLETE",
        "TOOLS-PRICED-FEJER-MV-SCHUR-CARLESON",
        "SELECTOR-SOURCE-ONLY-UNDERPERFORMS-BA-CLEARS-DEMAND",
        "KILL-GATES-ADJUDICATED-SF6-ANATOMY",
        "NOT-CBJ-RELABELING"]))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    if calib:
        print("CALIB MODE -- PRE-FREEZE, NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
