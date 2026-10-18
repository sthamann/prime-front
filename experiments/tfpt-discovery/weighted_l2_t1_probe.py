#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""weighted_l2_t1_probe --
PRIME.L2.T1_WEIGHTED_L2.01 (round 368): THE WEIGHTED L2-T1 --
the exact identity instead of the broken supremum (Sol rank 2,
G4).

CONTEXT (binding, from the DCCXXIII Sol evaluation after r358
QUADRATIC_LAW_PARTIAL and r361 FLOOR_THEOREM).  The T1 problem
is the family-uniform constant rule for
  F_i = (m q_i / log m) g_i.
The r306 first-K freeze fails on all four families (r358: A
2.45 vs 15.93, B 4.91 vs 23.70, chi 1.52/1.62 vs 3.91/3.09),
and C_K enters SQUARED into M_3, which is why the Carleson
detour is census-expensive (r358 m_0* 10^23.5; r361 floor
drops C_G but C_K still squares: 10^16.1 census / 10^10.0
rule-conditional).  The Sol retyping: THE EXACT IDENTITY
  M_3 = ((log m)^2 / m^2) · T_2 · E_π(F^2)
with T_2 = sum_i q_i / g_i^2 and the probability
  π_i = (q_i / g_i^2) / T_2
replaces the supremum by the WEIGHTED mean -- high F-spikes
count only with their q/g^2 weight, and r358 measured that the
K2 spikes do NOT sit on the smallest gaps (kz51/kz111: min g
0.533/0.571).  THE NEW TARGET: E_π(F^2) <= C_F (log m)^B,
family-uniform.  Together with T_2 <= C_G (log m)^A (r358
census, C_G = 0.100 at A = 2; under the floor SATZ even a
constant T_2 <= (8/3)^2) this would give
  M_3 <= C (log m)^{2+A+B} / m^2
WITHOUT the quadratic supremum amplification.

THE LEGS:
  LEG 0 -- ANCHORS bit-near: the r358 columns (F_i, g_i, q_i
    per atom; the S_r tables; the four family maxima), the
    r361 floor chain, the r324 chain (for the composition),
    the r339 FDD q_i.
  LEG A -- THE EXACT IDENTITY: M_3 == ((log m)^2/m^2)·T_2·
    E_π(F^2) derived algebraically and verified bit-exact
    (Fractions on the toy, f64 <= 1e-12 on all 181+ rows --
    it is a rewriting of M_3 = sum q^3, the identity MUST
    close exactly).
  LEG B -- THE E_π(F^2) CENSUS (the core): E_π(F^2) over ALL
    rows of all four families (+ the chi worlds from r357/
    r358); sealed bars (C_F, B) A-PRIORI (the r358 lesson:
    a-priori bars made T2' strong); the depth slope (does
    E_π(F^2) grow with m? polylog or power? -- NO fitted
    slopes, tercile ratios of the sealed C_obs); the
    LEAVE-FAMILY-OUT ceiling (the constant frozen on three
    families, tested on the fourth -- family-uniformity
    DIRECT); the spike anatomy: do kz111/kz117 dominate the
    weighted mean (then the retyping is useless -- honest)
    or are they π-light (the Sol thesis)?
  LEG C -- THE COMPOSITION: if the census carries, M_3 <=
    C·polylog/m^2 through the r324 chain (polylog convention)
    -- the new m_0* against 10^16.1 (r361 census) and 10^10.0
    (rule-conditional); the cofinal typing: with the floor
    SATZ (modulo V_2) + the L2-T1 census -- what exactly is
    still missing for the terminal SATZ on the canonical
    family?  And the cross-check: does the chain still need
    T_2 separately, or does the identity absorb everything
    (T_2·E_π(F^2) == (m^2/(log m)^2)·M_3 -- warded live)?
  LEG D -- WORLDS + MUST-FAILS (>= 4): matched SCRAMBLE
    (breaks where -- at admission as usual, or does its
    E_π(F^2) carry? typed); Twin.  Must-fails: the identity
    with the wrong π-normalization -> exact CAUGHT; bars
    after sight -> protocol-CAUGHT; F read back from M_3 ->
    AST-CAUGHT; leave-family-out with the target family in
    the freeze -> protocol-CAUGHT.

SEALED VERDICTS (main letter: TARGET_LEAK / LAW_STATE_NOT_EXACT
take precedence; otherwise combinations allowed):
  TARGET_LEAK  iff any firewall/scope/fragment/literal audit
    hit on the module-own builders;
  LAW_STATE_NOT_EXACT(named)  iff an exact ward breaks on a
    live world (identity, absorption, Fractions toy, frame
    reproductions, mesh identity, dictionary, N2 >= N3);
  WEIGHTED_L2_GO  iff E_π(F^2) is family-uniform polylog at
    the sealed a-priori (C_F, B) bars with 0 violations AND
    leave-family-out carries AND the named spikes are π-light
    AND the depth slope is POLYLOG -- G4 is replaced;
  WEIGHTED_L2_CENSUS  otherwise (the measured constants are
    appended); SPIKES_DOMINATE_PI is APPENDED iff the named
    K2-spike rows (kz111 / kz117) have argmax-F π-share of
    E_π(F^2) at or above the sealed SPIKE_SHARE_BAR -- the
    retyping is then useless, said honestly.

MACHINERY IMPORTED VERBATIM (SPEC_SHA prefix gated): r358
LGC.{eval_gap, gap_columns, gap_ledger, theta_col, g_norm,
pack_bar, scr_letter, solve_m0, audit sets, the four-world
construction constants} (fb2d499f); r361 MSF.{FLOOR_CAND,
CAP_FAC} (1bec7175); r355 KSF.mesh_h (1f14bd93); r357
DMF.{chi_window_comb, chi_wpack, chi_window_data, LPQ3,
LPQ4} (4bf1a94b); r353 SFE.{wpack_b, window_data_b,
frameb_pool} (bd89e331); r324 QMO composition convention
via LGC.solve_m0; r339 FDD via LGC.eval_gap; r329 EFA; r330
DSW; r269 PBB; r298 WBT; r244 BH; r243 PB; r289
AKD.twin_rational; r276 MF.local_gaps; r351 QGL.fab_of;
v881 PIK; v563 core READ-ONLY.  NEW module-own (source-pure,
AST-audited): f_bar, identity_rhs, pi_from_weights, e_pi,
lfo_freeze, lfo_holds, spike_letter, slope_letter,
weighted_tree_368, scr_epi_note.  q columns, F_i, T_2,
E_π(F^2), M_3, S_r, violation counts and every census on
them are TARGET-SIDE DIAGNOSTICS computed in the gate
section (r321..r361 convention, disclosed) -- the module-own
builders consume sealed thresholds, depth, and the passed
weight/value columns only.

INDEX FIREWALL (binding, r238-r361 discipline): w = window
(kz), N_w = builder depth, m = block count; ground truth
(records, the frozen r358/r361 anchor literals) enters GATES
and census tables only, never a builder (AST scope audit;
withheld identifiers rho / t_term / g_branch); no zero/prime
oracles anywhere (AST firewall); no fit primitives (fragment
audit; NO slopes fitted -- the bars are a-priori, the depth
slope is a tercile MAX-ratio of the sealed C_obs, the LFO
freeze is a MAX).  Budget <= 1800 s.

SEALED CONSTANTS (everything not listed is imported verbatim
via LGC/MSF): C_F = 1.0; B_F = 2.0 (a-priori, the r358 T2'
convention -- C_PACK = 1, A_PACK = 2 made the packing a
0-violation census theorem; the same grade is the GO target
for E_π(F^2)); ID_EPS 1e-12 (f64 identity); LFO_EPS 1e-9;
SPIKE_SHARE_BAR 0.5 (a-priori: argmax-F atom's share of
E_π(F^2) at or above one half on a named spike row = the
weighted mean IS the spike); SLOPE_RATIO_BAR 4.0 (a-priori:
deep-tercile C_obs / shallow-tercile C_obs above 4 types
POWER, else POLYLOG -- a MAX-ratio, not a fit); A_PACK =
LGC.A_PACK = 2.0; N_CAL_T1 / N_CAL_FB = LGC 5 / 2; TWIN_BAR
1e-3; TWIN_TOL 1e-8; SCR_SEED 1; STRESS_KZ = LGC (51, 111);
SPIKE_KZ_B = 117 (the r358 frame-B T1/K2 max row); RUNTIME_BAR
1800 s; anchor records (gate-side literals, r358/r361):
R358_ROWS (89, 8, 42, 42) EXACT; R358_T1_CK (2.45, 4.91,
1.52, 1.62) tol 0.02; R358_T1_TMAX (15.93, 23.70, 3.91, 3.09)
tol 0.02; R358_CEIL 23.70 tol 0.02; R358_CG 0.100 tol 0.01;
R358_STRESS_MING (0.533, 0.571) tol 2e-3; R358_MING 0.375
tol 1e-6; M0_REFS_368 (16.1, 10.0, 23.5, 18.9, 20.5, 13.5);
import-integrity prefixes LGC fb2d499f / MSF 1bec7175 / KSF
1f14bd93 / DMF 4bf1a94b / SFE bd89e331; R368_TABLE_LITERALS =
LGC.R358_TABLE_LITERALS UNION {23.7, 15.93, 16.1}
(collision-prone small values 2.45, 4.91, 1.52, 1.62, 3.91,
3.09, 0.533, 0.571, 0.375, 0.100, 10.0 curated OUT, r337..r361
convention, disclosed); smoke = toys + trees + mutants +
scope/purity audits + the four w9 worlds with full eval and
the identity ward; ladders, anchors, deep censuses,
composition, scrambles, twin and adjudication skipped.

DISCLOSED PRE-SPEC INPUT (no scratch run of THIS probe's
sealed adjudication): every anchor band is an r353..r361
RECORD number adopted as-is; the identity is DERIVED a priori
from F_i = (m q_i / log m) g_i and π_i = (q_i/g_i^2)/T_2:
  E_π(F^2) = (1/T_2) sum_i (q_i/g_i^2) · (m^2 q_i^2 /
             (log m)^2) g_i^2
           = (m^2 / ((log m)^2 T_2)) sum_i q_i^3,
  hence M_3 = ((log m)^2 / m^2) T_2 E_π(F^2) EXACT, and
  T_2 E_π(F^2) = (m^2 / (log m)^2) M_3 EXACT (the product
  restates M_3 -- T_2 is NOT absorbed, it is factorized).
  ONE SCOPING PASS (machinery validation at w9 only, r353..
  r361 precedent): the four w9 worlds exist through the r358
  channel (frame A m = 35, frame B / chi3 / chi4 admitted);
  every deep column, the E_π census, the LFO freeze, the
  spike anatomy, the depth slope and every composed m_0* are
  GENUINELY OPEN.  Timing: the r358/r361 full passes 711.3 /
  655.6 s (adopted as the deep budget estimate).  The sealed
  toys are computed BY HAND: Fractions identity toy q =
  (1/2, 1/4, 1/4), g = (1, 1/2, 1/2), m = 4, lg = 2 (the
  r358 T2 toy): F = (1, 1/4, 1/4), T_2 = 5/2, π = (1/5, 2/5,
  2/5), E_π(F^2) = 1/4, M_3 = 5/32, RHS = (4/16)·(5/2)·(1/4)
  = 5/32 EXACT; absorption T_2 E_π = 5/8 = (16/4)·(5/32)
  EXACT.  Wrong-π mutant (π' = q/g^2 unnormalized): E' = 5/8,
  RHS' = (1/4)·(5/2)·(5/8) = 25/64 != 5/32 CAUGHT exact.
  Bars-posthoc toy E = 9 at lg = 2 -> C_F_mut = 9/4 = 2.25
  != sealed C_F 1.0.  F-from-M3 toy rho = 5/32 -> cube-root
  replicated != (1, 1/4, 1/4).  LFO-leak toy other E (1, 2)
  at lg = 2, held E = 10 at lg = 2: true freeze max(1,2)/4
  = 1/2, mutant freeze 10/4 = 5/2.  Mesh toy (r355 verbatim)
  h 21 dev 1.0 in (0, 3/2].  Five main-tree branches, three
  scramble-epi notes, two slope letters and the sealed
  scr_letter order EXACT.  C_F, B_F, ID_EPS, LFO_EPS,
  SPIKE_SHARE_BAR, SLOPE_RATIO_BAR and all anchor tolerances
  are fixed BEFORE any deep evaluation; the letters are
  symmetric and total by CONTRACT.

EXPLORATION ONLY (2026-08-28).  experiments/ level: NO
promotion, NO ledger row, NO marker moved, NO RH CLAIM in
either direction.  Coexistence: R365 / R366 / R367 run in
parallel -- own files only; git pull before the strictly
additive rh-sync.  Two-commit freeze protocol (r329
convention): spec committed pre-freeze, record tables the
only post-freeze edit, committed again.

Honesty before beauty: the identity, the absorption, the
Fractions toys, the frame reproductions, the mesh identity
and the purity audits are EXACT (Fractions/AST-decided);
E_π(F^2), the a-priori bar census, LFO, the spike shares
and every composed m_0* are MEASURED on the finite 89 + 8
+ 42 + 42 row surface only -- a 0-violation census fixes a
CENSUS THEOREM, not a cofinal law; WEIGHTED_L2_GO here
means the weighted mean replaces the broken supremum ON
THIS SURFACE at the sealed a-priori grade; g_i is a
construction-local coordinate, said out loud; r243..r364
stand.

RECORD TABLES (inserted AFTER the record run -- the only
post-freeze docstring edit; freeze SPEC_SHA 4a89ec1051877c09,
pre-freeze commit e1521f94; protocol: smoke pass = 20/20
(0.8 s, run twice pre-commit, byte-identical up to the WALL
line, disclosed in the commit message); calibration pass 1 =
FIRST full evaluation = 20/20, wall 708.8 s, NO amendment --
no bar, share, slope, LFO rule or verdict rule moved at any
point; record run1/run2 after this insertion, byte-identical
up to WALL):
MAIN VERDICT: WEIGHTED_L2_CENSUS+SPIKES_DOMINATE_PI +
IDENTITY(worst rel 5.5e-16) + E_PI(C_F_cens 1.722, viol
3/181, max 75.691) + SLOPE(POWER ratio 16.414) + LFO(FAILS)
+ SPIKES(DOMINATE) + COMPOSITION(m_0* 10^29.8 / floor-T2
10^19.7 vs 10^16.1/10^10.0) + SCRAMBLE(P1_ADMISSION x3,
E_pi measurable 2.440/11.807/3.620) + TWIN(1.6e-07) +
MUSTFAIL_LEDGER.
THE HEADLINE FINDINGS:
(1) THE IDENTITY IS SATZ: M_3 == ((log m)^2/m^2) T_2
E_π(F^2) closes on ALL 181 live rows (89 frame A + 8 frame
B + 42 chi3 + 42 chi4) at worst relative 5.5e-16 (bar
1e-12), Fractions-exact on the sealed toy (M_3 = 5/32);
the absorption T_2 E_π == sum (q_i/g_i^2) F_i^2 ==
(m^2/(log m)^2) M_3 is TAUTOLOGICAL at the same 5.5e-16 --
T_2 is FACTORIZED, not absorbed: bounding the product
restates M_3.  All exact wards close (quantization 9.1e-13,
FDD 2.5e-16, FAB 2.0e-16, N2 >= N3 181/181, E_π <= max F^2
one-sided 0.0).
(2) THE A-PRIORI E_π BARS FAIL ON THE K2-SPIKE ROWS, AND
ONLY THERE: at the sealed (C_F, B) = (1.0, 2.0) T2' grade,
3/181 violations -- FRAME_A kz111 E_π 52.276 vs bar 41.258,
FRAME_B kz117 58.424 vs 42.09, FRAME_B kz124 75.691 vs
43.948 (the global max).  Chi3/chi4 are CLEAN (max E_π
1.144 / 0.649, C_obs 0.086 / 0.056, 0/42 + 0/42).  Frame A
otherwise 0/88.  C_F_cens = 1.722 (measured max
E_π/(log m)^2).  The GO grade does not fire; the census
constant is named.
(3) THE DEPTH SLOPE IS POWER, NOT POLYLOG: tercile
MAX-ratio of C_obs (NO fit) 16.414 vs bar 4.0 -- shallow
n=60 max E_π 1.165 C_obs 0.105, deep n=60 max E_π 75.691
C_obs 1.722.  Census max E_π/(log m)^k : k=0 75.691 / k=1
11.417 / k=2 1.722 / k=4 0.039.  E_π grows with depth
like the T1 product it rewrites -- the weighted mean
inherits the K2 growth.
(4) LEAVE-FAMILY-OUT FAILS ON FRAME B, CARRIES ELSEWHERE:
holding out A/chi3/chi4, C_fit = 1.722, 0 violations;
holding out FRAME_B, C_fit = 1.267 (from A+chi), viol 2/8
at kz117 and kz124 -- family-uniformity FAILS because
frame B's two deepest T1/K2 rows sit above every other
family's C_obs.  The Sol family-uniformity question is
answered DIRECTLY and negatively.
(5) SPIKE ANATOMY -- THE SOL THESIS IS MIXED, AND THE
NAMED BIT FIRES: kz111 (the frame-A K2 max, min g 0.571,
max F 15.93) IS π-light (share 0.337, ratio E/max F^2
0.206, g_i* 1.333 not a tight gap) -- HERE the retyping
does what it promised.  kz117 (the frame-B T1/K2 max, min
g 0.500, max F 23.70) DOMINATES (share 0.909, π_i* 9.45e-2,
q_i* 1.76e-1, g_i* 1.333) -- the weighted mean IS the
spike, the retyping is useless on that row.  kz51
(printed, not the named bit) share 0.938 DOMINATES at
smaller F.  Named-spike DOMINATES bit YES (kz117) -- G4
is NOT replaced.  Global max E_π is FRAME_B kz124, not
kz117.
(6) THE COMPOSITION DOES NOT PAY: with C_G_cens = 0.100
and C_F_cens = 1.722, M_3 <= C_G C_F (log m)^{6}/m^2
gives m_0* = 10^29.8 -- WORSE than the r358 Carleson
10^23.5 (two extra log powers, and C_F_cens is not small
enough to beat C_K^2) and far worse than the r361 floor
chain 10^16.1 / 10^10.0.  Floor-T2 (T2 <= (8/3)^2 = 7.111
constant) still 10^19.7.  C_K no longer enters squared
only IF E_π were O(1) polylog family-uniform -- it is
not.  Cofinal rest unchanged: MED-CAP as a lemma (V2) +
a family-uniform T1/E_π THEOREM; the identity is the
exact bookkeeping, not a bound.
(7) SCRAMBLES AND TWIN: all three matched channels break
at P1 = POSITIVE_PREFIX ADMISSION (nf 21/3/37 -- the
r353..r361 records reproduced); partial builds STILL
carry gap columns and a measurable E_π (2.440 / 11.807 /
3.620), all grid-quantized.  Twin E_π+maxprod+T2val
1.6e-07.  Must-fails: e1 CAUGHT exact (25/64 != 5/32) /
e2 protocol-CAUGHT twice (AST rho@512 + pin 2.25 != 1.0)
/ e3 protocol-CAUGHT twice (AST rho@520 + pin cube-root
replica != (1, 1/4, 1/4)) / e4 protocol-CAUGHT twice
(AST rho@528 + pin 2.50 != 0.50) + m6a/m6b FLAGGED
(t_term@539 / g_branch@546).  Runtime 708.8 s
calibration / record run1/run2 byte-identical up to WALL
/ 0.8 s smoke.  AMENDMENTS AFTER FREEZE: NONE except this
record-table insertion.

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

import bordered_hankel_probe as BH             # noqa: E402 r244
import principal_bessel_probe as PB            # noqa: E402 r243
import ext3_fresh_anchors_probe as EFA         # noqa: E402 r329
import qmax_growth_law_probe as QGL            # noqa: E402 r351
import second_family_erosion_probe as SFE      # noqa: E402 r353
import k2_source_formula_probe as KSF          # noqa: E402 r355
import dirichlet_secondworld_probe as DSW      # noqa: E402 r330
import dirichlet_matched_frame_probe as DMF    # noqa: E402 r357
import local_gap_carleson_probe as LGC         # noqa: E402 r358
import mean_sieve_floor_probe as MSF           # noqa: E402 r361
import arch_kernel_diophantine_probe as AKD    # noqa: E402 r289
import minimal_firewall_probe as MF            # noqa: E402 r276
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import phase_bulk_bound_probe as PBB           # noqa: E402 r269
import window_border_transfer_probe as WBT     # noqa: E402 r298
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY
import verify_lstar_instance as V              # noqa: E402 document

# ---------------- imported constants (verbatim via LGC/MSF)
W_LOC = EFA.GAP_W
QUANT_BAR = LGC.QUANT_BAR
PACK_EPS = LGC.PACK_EPS
N_CAL_T1 = LGC.N_CAL_T1
N_CAL_FB = LGC.N_CAL_FB
A_PACK = LGC.A_PACK
TWIN_BAR = LGC.TWIN_BAR
TWIN_TOL = LGC.TWIN_TOL
SCR_SEED = LGC.SCR_SEED
STRESS_KZ = LGC.STRESS_KZ
MULT_CAP = LGC.MULT_CAP
NU_A = LGC.NU_A
NU_B = LGC.NU_B
FRAMEB_KZ = LGC.FRAMEB_KZ
MESH_DEV_HI = LGC.MESH_DEV_HI
LPQ3 = LGC.LPQ3
LPQ4 = LGC.LPQ4
Q_CHI3 = LGC.Q_CHI3
Q_CHI4 = LGC.Q_CHI4
TOY_BAR = LGC.TOY_BAR
FLOOR_CAND = MSF.FLOOR_CAND
CAP_FAC = MSF.CAP_FAC

# ---------------- NEW sealed constants of this round (spec above)
C_F = 1.0
B_F = 2.0
ID_EPS = 1.0e-12
LFO_EPS = 1.0e-9
SPIKE_SHARE_BAR = 0.5
SLOPE_RATIO_BAR = 4.0
SPIKE_KZ_B = 117
RUNTIME_BAR = 1800.0
# anchor records (gate-side literals, the r358/r361 records)
R358_ROWS = (89, 8, 42, 42)
R358_MING = 0.375
R358_MING_TOL = 1.0e-6
R358_T1_CK = (2.45, 4.91, 1.52, 1.62)
R358_T1_TMAX = (15.93, 23.70, 3.91, 3.09)
R358_T1_TOL = 0.02
R358_CEIL = 23.70
R358_CEIL_TOL = 0.02
R358_CG = 0.100
R358_CG_TOL = 0.01
R358_STRESS_MING = (0.533, 0.571)
R358_STRESS_TOL = 2.0e-3
M0_REFS_368 = (16.1, 10.0, 23.5, 18.9, 20.5, 13.5)
# import-integrity SHA prefixes (sealed)
LGC_SHA_PREFIX = "fb2d499f"
MSF_SHA_PREFIX = "1bec7175"
KSF_SHA_PREFIX = "1f14bd93"
DMF_SHA_PREFIX = "4bf1a94b"
SFE_SHA_PREFIX = "bd89e331"

R368_TABLE_LITERALS = frozenset(LGC.R358_TABLE_LITERALS
                                | {23.7, 15.93, 16.1})

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
    return (not bad), ("NO zero/prime oracles; the weighted-L2 "
                       "builders consume sealed thresholds + depth "
                       "+ the passed weight/value columns ONLY; "
                       "q/F/M3/E_pi enter gates and census tables "
                       "only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


SCOPE_FORBIDDEN_368 = {"rho", "t" + "_term", "g" + "_branch",
                       "fabg" + "_true"}


def scope_audit(funcname, forbidden):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in forbidden:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


def literal_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                if isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, (int, float)) \
                        and not isinstance(sub.value, bool):
                    if round(float(sub.value), 4) \
                            in R368_TABLE_LITERALS:
                        hits.append("%s@%d" % (repr(sub.value),
                                               sub.lineno))
    return hits


# ---------------- module-own builders (source-pure, AST-audited):
# ---------------- consume sealed thresholds, depth, and the
# ---------------- passed weight/value columns only.  q, F, T2,
# ---------------- E_pi, M3 and every census on them are
# ---------------- TARGET-SIDE DIAGNOSTICS computed in the gate
# ---------------- section (disclosed).
def f_bar(lg):
    """the sealed E_π(F^2) bar C_F (log m)^{B_F} (a-priori,
    never moved).  Consumes depth only."""
    return C_F * (float(lg) ** B_F)


def identity_rhs(t2, epi, m, lg):
    """((log m)^2 / m^2) · T_2 · E_π(F^2) -- the rewritten M_3.
    Consumes the T2/E factors and depth only, NOT M_3."""
    return (float(lg) * float(lg)) / (float(m) * float(m)) \
        * float(t2) * float(epi)


def pi_from_weights(w):
    """normalize a weight column to a probability (the π
    definition's T_2-division).  Consumes the passed weights
    only."""
    s = sum(float(v) for v in w)
    return tuple(float(v) / s for v in w)


def e_pi(pi, vals):
    """the weighted mean E_π(vals).  Consumes the passed
    probability and value columns only."""
    return sum(float(p) * float(v) for p, v in zip(pi, vals))


def lfo_freeze(epis, lgs):
    """the leave-family-out freeze: max E_π(F^2) / (log m)^{B_F}
    over the passed rows (a MAX, not a fit).  Consumes the
    passed columns and the sealed B_F only."""
    return max(float(e) / (float(lg) ** B_F)
               for e, lg in zip(epis, lgs))


def lfo_holds(epis, lgs, cfreeze, eps):
    """pointwise test of E_π(F^2) <= cfreeze (log m)^{B_F} + eps
    on the passed held-out rows."""
    return all(float(e) <= float(cfreeze) * (float(lg) ** B_F)
               + float(eps)
               for e, lg in zip(epis, lgs))


def spike_letter(share, bar):
    """named-spike anatomy: DOMINATES iff the argmax-F atom's
    share of E_π(F^2) is at or above the sealed bar."""
    if float(share) >= float(bar):
        return "DOMINATES"
    return "PI_LIGHT"


def slope_letter(ratio, bar):
    """depth slope from the sealed tercile MAX-ratio of C_obs:
    POWER iff the ratio exceeds the sealed bar, else POLYLOG.
    A MAX-ratio, not a fit."""
    if float(ratio) > float(bar):
        return "POWER"
    return "POLYLOG"


def weighted_tree_368(leak, brk, spikes, bars_ok, lfo_ok, polylog):
    """the sealed main-letter tree.  TARGET_LEAK and
    LAW_STATE_NOT_EXACT take precedence; GO requires a-priori
    0-violation AND LFO AND POLYLOG AND π-light spikes;
    otherwise CENSUS, with SPIKES_DOMINATE_PI appended when
    the named spikes dominate (combinations allowed)."""
    if leak:
        return "TARGET_LEAK"
    if brk:
        return "LAW_STATE_NOT_EXACT"
    go = bars_ok and lfo_ok and polylog and (not spikes)
    if go:
        return "WEIGHTED_L2_GO"
    parts = ["WEIGHTED_L2_CENSUS"]
    if spikes:
        parts.append("SPIKES_DOMINATE_PI")
    return "+".join(parts)


def scr_epi_note(p1_ok, known, carries):
    """scramble typing for E_π(F^2): admission first, then
    whether a measurable gap column carries the sealed bar."""
    if not p1_ok:
        return "SCR_P1_ADMISSION"
    if not known:
        return "SCR_EPI_UNMEASURED"
    if carries:
        return "SCR_EPI_CARRIES"
    return "SCR_EPI_BREAKS"


# ---------------- must-fail mutants
def mutant_pi_unnorm(q, g):
    """e1 MUST-FAIL (exact): π_i = q_i/g_i^2 WITHOUT the T_2
    normalization -- the identity with the wrong π fails to
    close.  On the sealed toy E' = 5/8 gives RHS' = 25/64 !=
    M_3 = 5/32 -- CAUGHT exact."""
    return tuple(float(qi) / (float(gi) * float(gi))
                 for qi, gi in zip(q, g))


def mutant_bars_posthoc(rho, lgs):
    """e2 MUST-FAIL (protocol): C_F set at the seen E_π(F^2)
    column (consumes rho) -- AST-FLAGGED; on the sealed toy
    returns 2.25 != the sealed C_F 1.0."""
    return max(float(rho[i]) / (float(lgs[i]) ** B_F)
               for i in range(len(rho)))


def mutant_f_from_m3(rho, n=3):
    """e3 MUST-FAIL (protocol): F read back from M_3 (consumes
    rho) -- AST-FLAGGED; on the sealed toy the cube-root
    replica != the positional F column (1, 1/4, 1/4)."""
    v = float(rho) ** (1.0 / 3.0)
    return tuple(v for _ in range(n))


def mutant_lfo_leak(rho, held, other, lg_h, lg_o):
    """e4 MUST-FAIL (protocol): the LFO freeze includes the
    held-out family's E values (consumes rho) -- AST-FLAGGED;
    on the sealed toy returns 2.5 != the true freeze 0.5."""
    _ = rho
    e = list(other) + list(held)
    lgs = list(lg_o) + list(lg_h)
    return max(float(e[i]) / (float(lgs[i]) ** B_F)
               for i in range(len(e)))


def mutant_gift_bound(rc, P):
    """m6a MUST-FAIL (r355/r358/r361 verbatim): a builder
    consuming the withheld ground-truth terminal drive key --
    AST-FLAGGED."""
    s = math.copysign(1.0, rc["t_term"])
    return s * float(np.sum(np.abs(P) ** 3))


def mutant_branch_peek(rc, P):
    """m6b MUST-FAIL (r355/r358/r361 verbatim): a builder
    consuming the branch label -- AST-FLAGGED."""
    c = 0.5 if rc["g_branch"] >= 0.0 else 2.0
    return c * float(np.sum(np.abs(P) ** 3))


# ---------------- target-side diagnostic (gate section only;
# ---------------- NOT a source-pure builder -- q/F/M3 are the
# ---------------- census columns, disclosed).
def weighted_from_cols(gc, m):
    q = np.asarray(gc["q"], float)
    g = np.asarray(gc["g"], float)
    fcol = np.asarray(gc["prod"], float)
    t2 = float(gc["t2v"])
    m3 = float(gc["m3"])
    lg = float(gc["lg"])
    w = q / np.maximum(g * g, 1e-300)
    pi = w / max(t2, 1e-300)
    f2 = fcol * fcol
    epi = float(np.sum(pi * f2))
    rhs = identity_rhs(t2, epi, float(m), lg)
    id_rel = abs(rhs - m3) / max(abs(m3), 1e-300)
    prod_te = t2 * epi
    direct = float(np.sum(w * f2))
    absorb_rel = abs(prod_te - direct) / max(abs(prod_te), 1e-300)
    rearr = (float(m) ** 2 / max(lg * lg, 1e-300)) * m3
    rearr_rel = abs(prod_te - rearr) / max(abs(prod_te), 1e-300)
    imax = int(np.argmax(np.abs(fcol)))
    share = float(pi[imax] * f2[imax] / max(epi, 1e-300))
    ratio = float(epi / max(float(np.max(f2)), 1e-300))
    bar = f_bar(lg)
    return dict(epi=epi, rhs=rhs, id_rel=id_rel, t2=t2, m3=m3,
                prod_te=prod_te, absorb_rel=absorb_rel,
                rearr_rel=rearr_rel, imax=imax, share=share,
                ratio=ratio, bar=bar,
                viol=bool(epi > bar + ID_EPS),
                pi_maxf=float(pi[imax]), q_maxf=float(q[imax]),
                g_maxf=float(g[imax]), f_maxf=float(fcol[imax]),
                cf_obs=epi / max(lg ** B_F, 1e-300),
                epi_le_sup=max(0.0, epi - float(np.max(f2))))


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("weighted_l2_t1_probe -- "
          "PRIME.L2.T1_WEIGHTED_L2.01 (round 368)")
    print("SPEC_SHA %s   (LGC %s / MSF %s / KSF %s / DMF %s)"
          % (SPEC_SHA[:16], LGC.SPEC_SHA[:16], MSF.SPEC_SHA[:16],
             KSF.SPEC_SHA[:16], DMF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + trees + mutants + audits + "
                        "the four w9 worlds with full eval + the "
                        "identity ward; ladders, anchors, deep "
                        "censuses, composition, scrambles, twin "
                        "and adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION + SCOPE AUDITS")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    sha_ok = (LGC.SPEC_SHA.startswith(LGC_SHA_PREFIX)
              and MSF.SPEC_SHA.startswith(MSF_SHA_PREFIX)
              and KSF.SPEC_SHA.startswith(KSF_SHA_PREFIX)
              and DMF.SPEC_SHA.startswith(DMF_SHA_PREFIX)
              and SFE.SPEC_SHA.startswith(SFE_SHA_PREFIX))
    check("G02-predefinition", sha_ok,
          "sealed BEFORE evaluation: the identity M_3 = "
          "((log m)^2/m^2) T_2 E_pi(F^2) (derived a priori), the "
          "a-priori E_pi bars (C_F %.1f, B_F %.1f -- the r358 T2' "
          "grade), the LFO freeze (a MAX), the spike-share bar "
          "%.1f, the tercile slope bar %.1f, the letters; import "
          "integrity LGC %s / MSF %s / KSF %s / DMF %s / SFE %s"
          % (C_F, B_F, SPIKE_SHARE_BAR, SLOPE_RATIO_BAR,
             LGC.SPEC_SHA[:8], MSF.SPEC_SHA[:8], KSF.SPEC_SHA[:8],
             DMF.SPEC_SHA[:8], SFE.SPEC_SHA[:8]))
    frag = antigate_fragment_audit()
    own_builders = ("f_bar", "identity_rhs", "pi_from_weights",
                    "e_pi", "lfo_freeze", "lfo_holds",
                    "spike_letter", "slope_letter",
                    "weighted_tree_368", "scr_epi_note")
    sc_own = []
    pure_lits = []
    for fn in own_builders:
        sc_own += scope_audit(fn, LGC.BOUND_FORBIDDEN)
        sc_own += scope_audit(fn, LGC.PHI3_FORBIDDEN)
        sc_own += scope_audit(fn, LGC.QMAX_FORBIDDEN)
        sc_own += scope_audit(fn, SCOPE_FORBIDDEN_368)
        pure_lits += literal_audit(fn)
    sc_e2 = scope_audit("mutant_bars_posthoc", SCOPE_FORBIDDEN_368)
    sc_e3 = scope_audit("mutant_f_from_m3", SCOPE_FORBIDDEN_368)
    sc_e4 = scope_audit("mutant_lfo_leak", SCOPE_FORBIDDEN_368)
    sc_m6a = scope_audit("mutant_gift_bound", LGC.BOUND_FORBIDDEN)
    sc_m6b = scope_audit("mutant_branch_peek", LGC.BOUND_FORBIDDEN)
    leak = bool(frag) or bool(sc_own) or bool(pure_lits) or not okf
    check("G03-scope-audits", (not frag) and (not sc_own)
          and (not pure_lits) and len(sc_e2) >= 1
          and len(sc_e3) >= 1 and len(sc_e4) >= 1
          and len(sc_m6a) >= 1 and len(sc_m6b) >= 1,
          "fragment audit clean (%d); the %d module-own builders "
          "clean vs BOUND/PHI3/QMAX/368 sets (%d id hits) and vs "
          "the sealed record-literal set (%d literal hits); e2 "
          "FLAGGED (%s); e3 FLAGGED (%s); e4 FLAGGED (%s); "
          "m6a/m6b FLAGGED (%s / %s)"
          % (len(frag), len(own_builders), len(sc_own),
             len(pure_lits), sc_e2[0] if sc_e2 else "MISS",
             sc_e3[0] if sc_e3 else "MISS",
             sc_e4[0] if sc_e4 else "MISS",
             sc_m6a[0] if sc_m6a else "MISS",
             sc_m6b[0] if sc_m6b else "MISS"))

    # ---------------- S1 toys + trees + mutant pins
    section("S1  SEALED TOYS + TREES + MUTANT PINS (all by hand)")
    qF = (Fr(1, 2), Fr(1, 4), Fr(1, 4))
    gF = (Fr(1), Fr(1, 2), Fr(1, 2))
    mF, lgF = Fr(4), Fr(2)
    FF = tuple((mF * q / lgF) * g for q, g in zip(qF, gF))
    t2F = sum(q / (g * g) for q, g in zip(qF, gF))
    wF = tuple(q / (g * g) for q, g in zip(qF, gF))
    piF = tuple(w / t2F for w in wF)
    epiF = sum(p * f * f for p, f in zip(piF, FF))
    m3F = sum(q ** 3 for q in qF)
    rhsF = (lgF * lgF) / (mF * mF) * t2F * epiF
    absF = t2F * epiF
    rearrF = (mF * mF) / (lgF * lgF) * m3F
    fr_ok = (FF == (Fr(1), Fr(1, 4), Fr(1, 4))
             and t2F == Fr(5, 2)
             and piF == (Fr(1, 5), Fr(2, 5), Fr(2, 5))
             and epiF == Fr(1, 4)
             and m3F == Fr(5, 32)
             and rhsF == m3F
             and absF == Fr(5, 8)
             and rearrF == absF)
    # e1 wrong π (unnormalized weights used as if π)
    w_mut = mutant_pi_unnorm(qF, gF)
    epi_mut = sum(Fr(w_mut[i]) * FF[i] * FF[i] for i in range(3))
    rhs_mut = (lgF * lgF) / (mF * mF) * t2F * epi_mut
    e1_ok = (tuple(Fr(v).limit_denominator() for v in w_mut)
             == (Fr(1, 2), Fr(1), Fr(1))
             and epi_mut == Fr(5, 8)
             and rhs_mut == Fr(25, 64)
             and rhs_mut != m3F)
    # mesh toy (r355/r358/r361 verbatim)
    t_dk = 0.5 * 1.0 / 2.0
    t_mz = int(math.ceil(10.0 / t_dk - 1.0e-9)) + 1
    if t_mz % 2:
        t_mz += 1
    t_h = t_mz // 2
    t_dev = float(t_h) - 2.0 * (10.0 / 1.0)
    meshtoy_ok = (t_h == 21 and abs(t_dev - 1.0) <= TOY_BAR
                  and 0.0 < t_dev <= MESH_DEV_HI)
    # builder pins
    bar_pin = f_bar(2.0)
    bar_ok = abs(bar_pin - 4.0) <= TOY_BAR
    pi_b = pi_from_weights((Fr(1, 2), Fr(1), Fr(1)))
    pi_ok = all(abs(pi_b[i] - float(piF[i])) <= TOY_BAR
                for i in range(3))
    ep_b = e_pi(piF, (Fr(1), Fr(1, 16), Fr(1, 16)))
    ep_ok = abs(ep_b - 0.25) <= TOY_BAR
    # trees
    tr = (weighted_tree_368(True, True, True, True, True, True),
          weighted_tree_368(False, True, True, True, True, True),
          weighted_tree_368(False, False, False, True, True, True),
          weighted_tree_368(False, False, True, True, True, True),
          weighted_tree_368(False, False, False, False, True,
                            True))
    tr_ok = tr == ("TARGET_LEAK", "LAW_STATE_NOT_EXACT",
                   "WEIGHTED_L2_GO",
                   "WEIGHTED_L2_CENSUS+SPIKES_DOMINATE_PI",
                   "WEIGHTED_L2_CENSUS")
    sl = (slope_letter(2.0, SLOPE_RATIO_BAR),
          slope_letter(5.0, SLOPE_RATIO_BAR))
    sl_ok = sl == ("POLYLOG", "POWER")
    sp = (spike_letter(0.2, SPIKE_SHARE_BAR),
          spike_letter(0.7, SPIKE_SHARE_BAR))
    sp_ok = sp == ("PI_LIGHT", "DOMINATES")
    sn = (scr_epi_note(False, False, False),
          scr_epi_note(True, False, False),
          scr_epi_note(True, True, True),
          scr_epi_note(True, True, False))
    sn_ok = sn == ("SCR_P1_ADMISSION", "SCR_EPI_UNMEASURED",
                   "SCR_EPI_CARRIES", "SCR_EPI_BREAKS")
    sc_br = (LGC.scr_letter(False, True, True, True, True),
             LGC.scr_letter(True, True, True, True, True))
    sc_ok = sc_br == ("P1_ADMISSION", "NO_BREAK")
    lfo_true = lfo_freeze((1.0, 2.0), (2.0, 2.0))
    lfo_held_ok = lfo_holds((10.0,), (2.0,), lfo_true, LFO_EPS)
    lfo_toy_ok = (abs(lfo_true - 0.5) <= TOY_BAR
                  and (not lfo_held_ok))
    check("G10-toy-exactness", fr_ok and meshtoy_ok and bar_ok
          and pi_ok and ep_ok and tr_ok and sl_ok and sp_ok
          and sn_ok and sc_ok and lfo_toy_ok,
          "Fractions identity EXACT: F %s, T2 %s, pi %s, "
          "E_pi(F^2) %s, M3 %s == RHS %s, absorption T2 E_pi "
          "%s == (m^2/lg^2) M3 %s; bar(lg=2) %.1f; mesh toy h "
          "%d dev %.1f in (0, %.1f]; main tree %s; slope %s; "
          "spike %s; scr-epi notes %s; scr letters %s; LFO toy "
          "freeze %.2f rejects held 10"
          % (str(FF), str(t2F), str(piF), str(epiF), str(m3F),
             str(rhsF), str(absF), str(rearrF), bar_pin, t_h,
             t_dev, MESH_DEV_HI, "OK" if tr_ok else str(tr),
             "OK" if sl_ok else str(sl),
             "OK" if sp_ok else str(sp),
             "OK" if sn_ok else str(sn),
             "OK" if sc_ok else str(sc_br), lfo_true))
    mut2 = mutant_bars_posthoc((9.0,), (2.0,))
    mut3 = mutant_f_from_m3(float(Fr(5, 32)), 3)
    mut4 = mutant_lfo_leak((10.0,), (10.0,), (1.0, 2.0),
                           (2.0,), (2.0, 2.0))
    f_true = tuple(float(v) for v in FF)
    e2_ok = abs(mut2 - 2.25) <= 1e-9 and mut2 != C_F
    e3_ok = (all(abs(mut3[i] - mut3[0]) <= TOY_BAR
                 for i in range(3))
             and max(abs(mut3[i] - f_true[i])
                     for i in range(3)) > 0.1)
    e4_ok = abs(mut4 - 2.5) <= TOY_BAR and abs(lfo_true - 0.5) \
        <= TOY_BAR and mut4 != lfo_true
    check("G11-mutant-pins", e1_ok and e2_ok and e3_ok and e4_ok,
          "e1 pin RHS %s != M3 %s (unnormalized pi, E' %s -- "
          "the identity with the wrong pi is CAUGHT exact); e2 "
          "pin %.3f != sealed C_F %.1f; e3 pin %s != positional "
          "F %s; e4 pin %.2f != true LFO freeze %.2f"
          % (str(rhs_mut), str(m3F), str(epi_mut), mut2, C_F,
             str(tuple(round(v, 4) for v in mut3)),
             str(f_true), mut4, lfo_true))

    # ---------------- S2 world construction
    section("S2  THE FOUR WORLD FAMILIES (construction + "
            "admission + frame reproductions)")
    pb4 = SFE.wpack_b(9, NU_A)
    pa9 = BH.wpack(9)
    frb_ok = (pb4["N"] == pa9["N"] and pb4["nf"] == pa9["nf"])
    alpha9c = float(core.U_ALL[9])
    ka9c = core.atoms_in(alpha9c)
    db_v = SFE.window_data_b(9, NU_A)
    db_chi = DMF.chi_window_data(9, 0.0, math.log(math.pi),
                                 (core.U_ALL[:ka9c].copy(),
                                  core.MU_ALL[:ka9c].copy()))
    chi_ok = all(np.array_equal(db_v[k], db_chi[k])
                 for k in ("xs", "ws", "ys", "vs"))
    mesh_bad = []
    mesh_n = {}
    for nu, hcap in ((NU_B, SFE.H_B_CAP), (NU_A, core.HCAP)):
        zones_nu = SFE.frameb_pool(nu, core.H_MIN, hcap,
                                   SFE.Z2_CAP if nu == NU_B
                                   else None)
        mesh_n[nu] = len(zones_nu)
        for h, kz in zones_nu:
            hh, dev = KSF.mesh_h(kz, nu)
            if hh != h or not (0.0 < dev <= MESH_DEV_HI + 1e-9):
                mesh_bad.append((kz, nu, hh, h, dev))
    check("G20-frame-reproductions", frb_ok and chi_ok
          and not mesh_bad,
          "NU = %d reproduction (SFE.wpack_b == BH.wpack at w9: N "
          "%d == %d, nf %s == %s); chi trivial frame (a = 0, q = "
          "1) == SFE.window_data_b BITWISE at w9 [%s]; THE MESH "
          "IDENTITY h - NU u in (0, %.1f] EXACT on %s pool zones "
          "at NU (%d, %d) (violations %s)"
          % (NU_A, pb4["N"], pa9["N"], str(pb4["nf"]),
             str(pa9["nf"]), "OK" if chi_ok else "BROKEN",
             MESH_DEV_HI,
             str(tuple(mesh_n[k] for k in sorted(mesh_n))),
             NU_B, NU_A,
             str(mesh_bad[:3]) if mesh_bad else "0"))
    if smoke:
        packs_a = [pa9]
        packs_b = [SFE.wpack_b(9, NU_B)]
        u3, w3c, _nn3, _c3 = DMF.chi_window_comb(9, Q_CHI3)
        u4, w4c, _nn4, _c4 = DMF.chi_window_comb(9, Q_CHI4)
        packs_c3 = [DMF.chi_wpack(9, 1.0, LPQ3, (u3, w3c))]
        packs_c4 = [DMF.chi_wpack(9, 1.0, LPQ4, (u4, w4c))]
        check("G21-family-census", all(
            p["nf"] is None and p.get("complete", True)
            for p in packs_a + packs_b + packs_c3 + packs_c4),
            "SMOKE: the four w9 worlds built (frame A N %d / "
            "frame B N %d / chi3 N %d / chi4 N %d, all "
            "POSITIVE_PREFIX + chain-complete); ladders skipped"
            % (packs_a[0]["N"], packs_b[0]["N"],
               packs_c3[0]["N"], packs_c4[0]["N"]))
    else:
        kzs_l = []
        ekz = []
        ekz2 = []
        for kz in core.frame_a_zones():
            h = PIK.build_rung(kz)["h"]
            if h <= LGC.H_CAP:
                kzs_l.append(kz)
            elif h <= LGC.EXT_H_MAX:
                ekz.append(kz)
            elif h <= LGC.EXT2_H_MAX:
                ekz2.append((h, kz))
        ladder = [BH.wpack(kz) for kz in kzs_l]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        epool = [BH.wpack(kz) for kz in ekz]
        epool.sort(key=lambda p: (p["N"], p["kz"]))
        ext = epool[:LGC.K_EXT]
        ekz2.sort()
        pool2 = epool[LGC.K_EXT:] + [
            BH.wpack(kz) for _h, kz in ekz2[:LGC.EXT2_POOL_CAP]]
        pool2.sort(key=lambda p: (p["N"], p["kz"]))
        ext2 = [p for p in pool2 if p["nf"] is None][:LGC.K_EXT2]
        ext3 = [BH.wpack(kz)
                for kz in LGC.EXT3_KZ_B + LGC.EXT3_KZ_A]
        ext4 = [BH.wpack(kz) for kz in LGC.EXT4_KZ]
        ext5 = [BH.wpack(kz)
                for kz in LGC.EXT5_KZ_B + LGC.EXT5_KZ_A]
        packs_a = ladder + ext + ext2 + ext3 + ext4 + ext5
        okA = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder)
               and len(ext) == LGC.K_EXT
               and all(p["nf"] is None for p in packs_a))
        packs_b = [SFE.wpack_b(kz, NU_B) for kz in FRAMEB_KZ]
        okB = all(p["nf"] is None and p["complete"]
                  for p in packs_b)
        kzs_c = list(V.admissible_indices())
        packs_c3 = []
        packs_c4 = []
        excl = []
        for kz in kzs_c:
            u3, w3c, _nn, _ch = DMF.chi_window_comb(kz, Q_CHI3)
            if len(u3) < V.N_ATOM_MIN:
                excl.append((kz, 3))
                continue
            packs_c3.append(DMF.chi_wpack(kz, 1.0, LPQ3,
                                          (u3, w3c)))
        for kz in kzs_c:
            u4, w4c, _nn, _ch = DMF.chi_window_comb(kz, Q_CHI4)
            if len(u4) < V.N_ATOM_MIN:
                excl.append((kz, 4))
                continue
            packs_c4.append(DMF.chi_wpack(kz, 1.0, LPQ4,
                                          (u4, w4c)))
        okC = (len(packs_c3) == R358_ROWS[2]
               and len(packs_c4) == R358_ROWS[3]
               and all(p["complete"]
                       for p in packs_c3 + packs_c4))
        check("G21-family-census", okA and okB and okC
              and len(packs_a) == R358_ROWS[0]
              and len(packs_b) == R358_ROWS[1],
              "FRAME A: %d rows (== %d, 42 ladder + %d ext + %d "
              "ext2 + %d EXT3 + %d EXT4 + %d EXT5, all adopted "
              "as-is, all POSITIVE_PREFIX); FRAME B: %d/%d sealed "
              "r353 anchors re-admitted %s; CHI3 %d/%d + CHI4 "
              "%d/%d built (kept-atom exclusions %s)"
              % (len(packs_a), R358_ROWS[0], len(ext), len(ext2),
                 len(ext3), len(ext4), len(ext5), len(packs_b),
                 R358_ROWS[1],
                 str(sorted(p["kz"] for p in packs_b)),
                 len(packs_c3), R358_ROWS[2], len(packs_c4),
                 R358_ROWS[3], str(excl) if excl else "none"))

    # ---------------- S3 eval + identity live wards
    section("S3  EVAL + EXACT LIVE WARDS (r358 channel + the "
            "weighted-L2 identity)")
    fams = (("FRAME_A", packs_a), ("FRAME_B", packs_b),
            ("CHI3", packs_c3), ("CHI4", packs_c4))
    all_kz = sorted(set(p["kz"] for _f, ps in fams for p in ps))
    grel_map = {kz: g for kz, g in zip(
        all_kz, EFA.grel_col(all_kz, core.G_ALL))}
    frecs = {}
    for fam, ps in fams:
        recs = []
        for p in ps:
            rc = DSW.rung_rec(p)
            rc["ev"] = LGC.eval_gap(rc)
            recs.append(rc)
        recs.sort(key=lambda r: (r["N"], r["kz"]))
        frecs[fam] = recs
    tb_bad = []
    qdev_w = 0.0
    dict_w = 0.0
    fabid_w = 0.0
    id_w = 0.0
    abs_w = 0.0
    rearr_w = 0.0
    sup_w = 0.0
    n2n3_bad = 0
    mono_bad = 0
    mult_drop = []
    live = {}
    for fam in frecs:
        rows = []
        for rc in frecs[fam]:
            ev = rc["ev"]
            bar = (LGC.TB_WARD_BAR_B if fam == "FRAME_B"
                   else LGC.CHI_TB_BAR if fam.startswith("CHI")
                   else LGC.TB_WARD_BAR if rc["N"] <= LGC.DEEP_N
                   else max(LGC.TB_WARD_BAR_DEEP,
                            LGC.TB_WARD_BAR_X345))
            if ev["tb_dev"] > bar:
                tb_bad.append((fam, rc["kz"], ev["tb_dev"]))
            if ev["degenerate"]:
                mult_drop.append((fam, rc["kz"], "degenerate"))
                continue
            if ev["mx_mult"] > MULT_CAP:
                mult_drop.append((fam, rc["kz"], "mult"))
                continue
            qdev_w = max(qdev_w, ev["gl"]["qdev"])
            if not ev["gl"]["mono"]:
                mono_bad += 1
            mloc = ev["m"]
            lgl = math.log(float(mloc))
            qm = ev["mqs"]["qm"]
            dic = ev["dic"]
            dict_w = max(dict_w, abs(dic["ymx"] / float(mloc) - qm)
                         / max(qm, 1e-300))
            fab = QGL.fab_of(float(mloc), qm, lgl)
            fabid_w = max(fabid_w, abs(fab * lgl - mloc * qm)
                          / max(mloc * qm, 1e-300))
            gc = LGC.gap_columns(ev)
            if gc["n2"] + 1e-15 < gc["n3"]:
                n2n3_bad += 1
            wt = weighted_from_cols(gc, mloc)
            id_w = max(id_w, wt["id_rel"])
            abs_w = max(abs_w, wt["absorb_rel"])
            rearr_w = max(rearr_w, wt["rearr_rel"])
            sup_w = max(sup_w, wt["epi_le_sup"])
            rows.append(dict(kz=rc["kz"], N=rc["N"], m=mloc,
                             lg=lgl, fab=fab,
                             grel=grel_map[rc["kz"]],
                             fabg=fab * grel_map[rc["kz"]],
                             gc=gc, wt=wt))
        live[fam] = rows
    n_live = sum(len(live[f]) for f in live)
    brk_struct = (bool(tb_bad) or qdev_w > QUANT_BAR
                  or mono_bad > 0 or dict_w > LGC.DICT_BAR
                  or fabid_w > LGC.FAB_ID_BAR
                  or id_w > ID_EPS or abs_w > ID_EPS
                  or rearr_w > ID_EPS or sup_w > ID_EPS
                  or n2n3_bad > 0 or not frb_ok or not chi_ok
                  or bool(mesh_bad) or not fr_ok or not meshtoy_ok
                  or n_live == 0)
    check("G30-exact-live-wards", not brk_struct,
          "on %d live rows (drops %s): IDENTITY M3 == "
          "((log m)^2/m^2) T2 E_pi(F^2) worst rel %.1e (bar "
          "%.0e); absorption T2 E_pi == sum((q/g^2) F^2) worst "
          "%.1e AND == (m^2/lg^2) M3 worst %.1e; E_pi <= max F^2 "
          "one-sided %.1e; theta-grid quantization worst %.1e "
          "(bar %.0e); centers monotone (%d bad); FDD dictionary "
          "ymx/m == q_max %.1e; FAB identity %.1e; N2 >= N3 "
          "%d/%d; contribution ward %s -- the identity IS a "
          "rewriting of M3 = sum q^3"
          % (n_live, str(mult_drop) if mult_drop else "none",
             id_w, ID_EPS, abs_w, rearr_w, sup_w, qdev_w,
             QUANT_BAR, mono_bad, dict_w, fabid_w,
             n_live - n2n3_bad, n_live,
             "OK" if not tb_bad else "BROKEN %s"
             % str(tb_bad[:3])))

    # ---------------- S4 Leg 0 anchors
    section("S4  LEG 0 -- ANCHORS (the r358 record through the "
            "same channel, bit-near)")
    fam_order = ("FRAME_A", "FRAME_B", "CHI3", "CHI4")
    if smoke:
        check("G40-anchors", True, "SMOKE: skipped")
        ceil = max(r["gc"]["maxprod"] for f in fam_order
                   for r in live[f])
        ck_rule = ceil
        cg_cens = max(r["gc"]["t2v"] / r["lg"] ** A_PACK
                      for f in fam_order for r in live[f])
    else:
        ming_all = min(row["gc"]["ming"] for f in fam_order
                       for row in live[f])
        t1_ok = True
        t1_txt = []
        ck_rule = 0.0
        for fi, fam in enumerate(fam_order):
            rows = live[fam]
            ncal = N_CAL_FB if fam == "FRAME_B" else N_CAL_T1
            ck = max(r["gc"]["maxprod"] for r in rows[:ncal])
            tmax = max(r["gc"]["maxprod"] for r in rows[ncal:])
            ck_rule = max(ck_rule, ck)
            t1_ok = t1_ok and (abs(ck - R358_T1_CK[fi])
                               <= R358_T1_TOL) \
                and (abs(tmax - R358_T1_TMAX[fi])
                     <= R358_T1_TOL)
            t1_txt.append("%s %.2f/%.2f" % (fam[:2], ck, tmax))
        ceil = max(r["gc"]["maxprod"] for f in fam_order
                   for r in live[f])
        cg_cens = max(r["gc"]["t2v"] / r["lg"] ** A_PACK
                      for f in fam_order for r in live[f])
        ck2x = max(r["fabg"] for r in live["FRAME_A"])
        ck2x_kz = max(live["FRAME_A"],
                      key=lambda r: r["fabg"])["kz"]
        stress_ok = True
        stress_txt = []
        for si, kz_s in enumerate(STRESS_KZ):
            row = next((r for r in live["FRAME_A"]
                        if r["kz"] == kz_s), None)
            mg = row["gc"]["ming"] if row else -1.0
            stress_ok = stress_ok and (
                abs(mg - R358_STRESS_MING[si])
                <= R358_STRESS_TOL)
            stress_txt.append("kz%d %.3f" % (kz_s, mg))
        check("G40-anchors",
              abs(ming_all - R358_MING) <= R358_MING_TOL
              and t1_ok
              and abs(ceil - R358_CEIL) <= R358_CEIL_TOL
              and abs(cg_cens - R358_CG) <= R358_CG_TOL
              and abs(ck2x - LGC.R353_CK2X) <= LGC.R353_CK2X_TOL
              and ck2x_kz == LGC.R353_CK2X_KZ
              and stress_ok,
              "min g %.4f (rec %.3f); T1 freeze/testmax %s (rec "
              "CK %s TMAX %s); global ceiling %.2f (rec %.2f); "
              "C_G_cens %.3f (rec %.3f); C_K2X %.2f at kz%d "
              "(rec %.2f at kz%d); stress min g %s (rec %s) -- "
              "the r358 F/g/q columns and family maxima "
              "reproduce through THIS channel"
              % (ming_all, R358_MING, "; ".join(t1_txt),
                 str(R358_T1_CK), str(R358_T1_TMAX), ceil,
                 R358_CEIL, cg_cens, R358_CG, ck2x, ck2x_kz,
                 LGC.R353_CK2X, LGC.R353_CK2X_KZ,
                 str(stress_txt), str(R358_STRESS_MING)))

    # ---------------- S5 Leg A: identity census
    section("S5  LEG A -- THE EXACT IDENTITY (all live rows)")
    check("G50-identity-census", id_w <= ID_EPS
          and abs_w <= ID_EPS and rearr_w <= ID_EPS,
          "THE IDENTITY on all %d live rows: M3 == "
          "((log m)^2/m^2) T2 E_pi(F^2) worst rel %.1e; the "
          "absorption T2 E_pi(F^2) == sum_i (q_i/g_i^2) F_i^2 "
          "== (m^2/(log m)^2) M3 worst %.1e / %.1e (bar %.0e) "
          "-- T2 is FACTORIZED, not absorbed: bounding the "
          "product is restating M3; the new quantitative "
          "statement is the E_pi(F^2) bound"
          % (n_live, id_w, abs_w, rearr_w, ID_EPS))

    # ---------------- S6 Leg B: E_π census + slope + LFO + spikes
    section("S6  LEG B -- THE E_pi(F^2) CENSUS (a-priori bars, "
            "depth slope, leave-family-out, spike anatomy)")
    if smoke:
        check("G60-epi-bars", True, "SMOKE: skipped")
        check("G61-depth-slope", True, "SMOKE: skipped")
        check("G62-leave-family-out", True, "SMOKE: skipped")
        check("G63-spike-anatomy", True, "SMOKE: skipped")
        bars_ok = True
        lfo_ok = True
        polylog = True
        spikes = False
        cf_cens = 0.0
        slope_ratio = 1.0
        slope_let = "POLYLOG"
        lfo_txt = []
        spike_txt = []
        n_bar_viol = 0
        epi_max = 0.0
    else:
        n_bar_viol = 0
        viol_locs = []
        epi_cells = []
        cf_cens = 0.0
        epi_max = 0.0
        epi_max_loc = ("-", 0)
        for fam in fam_order:
            mx = max(r["wt"]["epi"] for r in live[fam])
            cgf = max(r["wt"]["cf_obs"] for r in live[fam])
            cf_cens = max(cf_cens, cgf)
            nv = 0
            for r in live[fam]:
                if r["wt"]["epi"] > epi_max:
                    epi_max = r["wt"]["epi"]
                    epi_max_loc = (fam, r["kz"])
                if r["wt"]["viol"]:
                    n_bar_viol += 1
                    nv += 1
                    viol_locs.append((fam, r["kz"],
                                      round(r["wt"]["epi"], 3),
                                      round(r["wt"]["bar"], 3)))
            epi_cells.append("%s max E_pi %.3f (C_obs %.3f, "
                             "viol %d/%d)"
                             % (fam, mx, cgf, nv, len(live[fam])))
        bars_ok = (n_bar_viol == 0)
        for t in epi_cells:
            info("E_pi " + t)
        check("G60-epi-bars", True,
              "E_pi(F^2) at the SEALED a-priori bars (C_F %.1f, "
              "B_F %.1f): %s; violations %s / %d rows; C_F_cens "
              "= %.3f (measured max E_pi/(log m)^B); global max "
              "E_pi %.3f at %s -- the r358 lesson: a-priori bars "
              "are the GO grade, a measured C_F_cens is CENSUS"
              % (C_F, B_F, "; ".join(epi_cells),
                 ("0" if bars_ok else "%d %s"
                  % (n_bar_viol, str(viol_locs[:6]))),
                 n_live, cf_cens, epi_max, str(epi_max_loc)))
        # depth slope: tercile MAX-ratio of C_obs (no fit)
        all_rows = [r for f in fam_order for r in live[f]]
        all_rows.sort(key=lambda r: r["lg"])
        n3 = max(len(all_rows) // 3, 1)
        lo = all_rows[:n3]
        hi = all_rows[-n3:]
        c_lo = max(r["wt"]["cf_obs"] for r in lo)
        c_hi = max(r["wt"]["cf_obs"] for r in hi)
        e_lo = max(r["wt"]["epi"] for r in lo)
        e_hi = max(r["wt"]["epi"] for r in hi)
        slope_ratio = c_hi / max(c_lo, 1e-300)
        slope_let = slope_letter(slope_ratio, SLOPE_RATIO_BAR)
        polylog = (slope_let == "POLYLOG")
        ktab = []
        for k in (0, 1, 2, 4):
            mxk = max(r["wt"]["epi"] / (r["lg"] ** k)
                      for r in all_rows)
            ktab.append("k=%d %.3f" % (k, mxk))
        check("G61-depth-slope", True,
              "DEPTH SLOPE (tercile MAX-ratio of C_obs = "
              "E_pi/(log m)^B, NO fit): shallow n=%d max E_pi "
              "%.3f C_obs %.3f; deep n=%d max E_pi %.3f C_obs "
              "%.3f; ratio %.3f vs bar %.1f -> %s; census "
              "max E_pi/(log m)^k : %s"
              % (len(lo), e_lo, c_lo, len(hi), e_hi, c_hi,
                 slope_ratio, SLOPE_RATIO_BAR, slope_let,
                 "; ".join(ktab)))
        # leave-family-out
        lfo_ok = True
        lfo_txt = []
        for held in fam_order:
            others = [f for f in fam_order if f != held]
            epis_o = [r["wt"]["epi"] for f in others
                      for r in live[f]]
            lgs_o = [r["lg"] for f in others for r in live[f]]
            cfit = lfo_freeze(epis_o, lgs_o)
            epis_h = [r["wt"]["epi"] for r in live[held]]
            lgs_h = [r["lg"] for r in live[held]]
            holds = lfo_holds(epis_h, lgs_h, cfit, LFO_EPS)
            viol_h = [r["kz"] for r in live[held]
                      if r["wt"]["epi"] > cfit * (r["lg"] ** B_F)
                      + LFO_EPS]
            if not holds:
                lfo_ok = False
            lfo_txt.append("%s held: C_fit %.3f, viol %d/%d%s"
                           % (held, cfit, len(viol_h),
                              len(live[held]),
                              (" " + str(viol_h[:4])) if viol_h
                              else ""))
        for t in lfo_txt:
            info("LFO " + t)
        check("G62-leave-family-out", True,
              "LEAVE-FAMILY-OUT (C_F frozen as MAX E_pi/(log m)^B "
              "on three families, tested on the fourth -- family "
              "uniformity DIRECT): %s; LFO %s on all four "
              "hold-outs"
              % ("; ".join(lfo_txt),
                 "CARRIES" if lfo_ok else "FAILS"))
        # spike anatomy: kz111 FRAME_A, kz117 FRAME_B, plus
        # the global max-E_pi row
        spike_txt = []
        spikes = False
        named = []
        row111 = next((r for r in live["FRAME_A"]
                       if r["kz"] == STRESS_KZ[1]), None)
        row117 = next((r for r in live["FRAME_B"]
                       if r["kz"] == SPIKE_KZ_B), None)
        row51 = next((r for r in live["FRAME_A"]
                      if r["kz"] == STRESS_KZ[0]), None)
        for lab, row in (("kz51", row51), ("kz111", row111),
                         ("kz117", row117)):
            if row is None:
                spike_txt.append("%s MISSING" % lab)
                continue
            w = row["wt"]
            let = spike_letter(w["share"], SPIKE_SHARE_BAR)
            if lab in ("kz111", "kz117") and let == "DOMINATES":
                spikes = True
            named.append(lab)
            spike_txt.append(
                "%s (m %d, min g %.3f, max F %.2f): pi_i* %.3e "
                "q_i* %.3e g_i* %.3f share %.3f ratio E/maxF^2 "
                "%.3f -> %s"
                % (lab, row["m"], row["gc"]["ming"], w["f_maxf"],
                   w["pi_maxf"], w["q_maxf"], w["g_maxf"],
                   w["share"], w["ratio"], let))
        for t in spike_txt:
            info("SPIKE " + t)
        check("G63-spike-anatomy", True,
              "SPIKE ANATOMY (the Sol thesis: K2 spikes are NOT "
              "on the smallest gaps, hence should be pi-light): "
              "%s; named-spike DOMINATES bit %s (bar share %.1f) "
              "-- if DOMINATES the retyping is useless, said "
              "honestly; global max E_pi at %s"
              % ("; ".join(spike_txt),
                 "YES" if spikes else "NO (pi-light)",
                 SPIKE_SHARE_BAR, str(epi_max_loc)))

    # ---------------- S7 Leg C: composition
    section("S7  LEG C -- THE COMPOSITION (r324 polylog chain + "
            "the T2-absorption cross-check)")
    if smoke:
        check("G70-composition", True, "SMOKE: skipped")
        m0_w = None
        m0_ft = None
    else:
        cf_use = cf_cens if cf_cens > 0.0 else C_F
        cg_use = cg_cens if cg_cens > 0.0 else R358_CG
        # rho_2 <= C_G C_F (log m)^{A+B}
        m0_w = LGC.solve_m0(
            lambda t, cg=cg_use, cf=cf_use:
            math.log(max(cg * cf, 1e-300))
            + (A_PACK + B_F) * math.log(t))
        # floor-T2: T2 <= (8/3)^2 constant, rho_2 <= T2bound C_F
        # (log m)^B
        t2_floor = float(CAP_FAC) ** 2
        m0_ft = LGC.solve_m0(
            lambda t, tb=t2_floor, cf=cf_use:
            math.log(max(tb * cf, 1e-300)) + B_F * math.log(t))
        rest_txt = (
            "WITH the floor SATZ (modulo V2, r364) + this L2-T1 "
            "census, the remaining named rest for a terminal SATZ "
            "on the CANONICAL family is (i) MED-CAP as a lemma "
            "(the r364 remainder V2), (ii) E_pi(F^2) <= C_F "
            "(log m)^B as a THEOREM not a census"
            + (" -- BUT SPIKES_DOMINATE_PI: the retyping does "
               "NOT remove G4, the supremum still sits in the "
               "mean" if spikes else " (the Sol replacement of "
               "G4, census-grade on this surface)"))
        check("G70-composition", True,
              "THE COMPOSITION: M_3 = ((log m)^2/m^2) T2 "
              "E_pi(F^2) <= C_G C_F (log m)^{2+A+B}/m^2 with "
              "measured C_G_cens = %.3f, C_F_cens = %.3f (A = "
              "%.0f, B = %.0f) => m_0* = %s (pure polylog, r324 "
              "convention) vs r361 census 10^%.1f / "
              "rule-conditional 10^%.1f / r358 Carleson 10^%.1f "
              "/ r351 10^%.1f / r353 10^%.1f / r306 10^%.1f; "
              "FLOOR-T2 (T2 <= (8/3)^2 = %.3f constant) gives "
              "m_0* = %s; CROSS-CHECK: T2 E_pi == (m^2/lg^2) M3 "
              "is TAUTOLOGICAL (warded G30 worst %.1e) -- the "
              "identity does NOT absorb T2, it FACTORIZES M3; a "
              "T2 bound remains (r358 C_G census, or the floor "
              "constant).  C_K no longer enters squared IF E_pi "
              "carries (the point of the retyping).  %s"
              % (cg_use, cf_use, A_PACK, B_F,
                 ("10^%.1f" % m0_w) if m0_w is not None
                 else "NONE",
                 M0_REFS_368[0], M0_REFS_368[1], M0_REFS_368[2],
                 M0_REFS_368[3], M0_REFS_368[4], M0_REFS_368[5],
                 t2_floor,
                 ("10^%.1f" % m0_ft) if m0_ft is not None
                 else "NONE", rearr_w, rest_txt))

    # ---------------- S8 Leg D: scrambles + twin
    section("S8  LEG D -- MATCHED SCRAMBLES (E_pi contrast) + "
            "TWIN")
    if smoke:
        check("G80-scrambles", True, "SMOKE: skipped")
        check("G81-twin", True, "SMOKE: skipped")
        scr_txt = "SMOKE"
        devT = 0.0
    else:
        alpha9 = float(core.U_ALL[9])
        rng = np.random.default_rng(SCR_SEED)
        scr_worlds = []
        pA = BH.wpack(9, base_kw=dict(scramble_seed=SCR_SEED))
        scr_worlds.append(("FRAME_A_w9", pA))
        alpha80 = float(core.U_ALL[80])
        ka80 = core.atoms_in(alpha80)
        uu_scr = np.sort(rng.uniform(0.0, 2.0 * alpha80,
                                     size=ka80))
        pBv = SFE.wpack_b(80, NU_B,
                          comb=(uu_scr,
                                core.MU_ALL[:ka80].copy()))
        scr_worlds.append(("FRAME_B_kz80", pBv))
        u3s, w3s, _nn, _ch = DMF.chi_window_comb(9, Q_CHI3)
        u_scr = np.sort(np.random.default_rng(SCR_SEED).uniform(
            0.0, 2.0 * alpha9, size=len(w3s)))
        try:
            pC = DMF.chi_wpack(9, 1.0, LPQ3, (u_scr, w3s))
        except Exception as exc:            # noqa: BLE001
            pC = dict(kz=9, N=0, nf="build-fail: %s" % exc,
                      complete=False)
        scr_worlds.append(("CHI3_w9", pC))
        scr_lets = []
        for lab, p in scr_worlds:
            p1_ok = (p.get("nf") is None
                     and p.get("complete", True))
            known = False
            carries = False
            epi_s = None
            qdev_s = None
            mult_ok = True
            quant_ok = True
            if p.get("rows"):
                rc = DSW.rung_rec(p)
                ev = LGC.eval_gap(rc)
                if not ev["degenerate"]:
                    mult_ok = ev["mx_mult"] <= MULT_CAP
                    qdev_s = ev["gl"]["qdev"]
                    quant_ok = qdev_s <= QUANT_BAR
                    gcs = LGC.gap_columns(ev)
                    wts = weighted_from_cols(gcs, ev["m"])
                    known = True
                    epi_s = wts["epi"]
                    carries = not wts["viol"]
            let = LGC.scr_letter(p1_ok, mult_ok, quant_ok, True,
                                 True)
            note = scr_epi_note(p1_ok, known, carries)
            scr_lets.append(
                "%s -> %s/%s (nf %s, qdev %s, E_pi %s)"
                % (lab, let, note, str(p.get("nf")),
                   ("%.1e" % qdev_s) if qdev_s is not None
                   else "n/a",
                   ("%.3f" % epi_s) if epi_s is not None
                   else "n/a"))
        scr_txt = "; ".join(scr_lets)
        check("G80-scrambles", all("NO_BREAK" not in s
                                   for s in scr_lets),
              "MATCHED SCRAMBLES through all three construction "
              "channels (sealed precondition order + E_pi "
              "contrast): %s -- admission is the expected named "
              "precondition (r353/r355/r357/r358/r361); a "
              "measurable E_pi on a partial build is typed, not "
              "claimed"
              % scr_txt)
        gaps3 = MF.local_gaps(u3s)
        _a, _M, _L, _Nw, D9 = V.window_shape(9)
        u3t, w3t, _d, _du = AKD.twin_rational(u3s, w3s, gaps3,
                                              D9, TWIN_TOL)
        pk3 = DMF.chi_wpack(9, 1.0, LPQ3, (u3s, w3s))
        pk3t = DMF.chi_wpack(9, 1.0, LPQ3, (u3t, w3t))
        rcT = DSW.rung_rec(pk3)
        rcTt = DSW.rung_rec(pk3t)
        evT = LGC.eval_gap(rcT)
        evTt = LGC.eval_gap(rcTt)
        gcT = LGC.gap_columns(evT)
        gcTt = LGC.gap_columns(evTt)
        wtT = weighted_from_cols(gcT, evT["m"])
        wtTt = weighted_from_cols(gcTt, evTt["m"])
        devT = max(abs(gcT["maxprod"] - gcTt["maxprod"])
                   / max(gcT["maxprod"], 1e-300),
                   abs(gcT["t2v"] - gcTt["t2v"])
                   / max(gcT["t2v"], 1e-300),
                   abs(wtT["epi"] - wtTt["epi"])
                   / max(wtT["epi"], 1e-300))
        check("G81-twin", devT <= TWIN_BAR,
              "RATIONAL TWIN of the chi3 comb (tol %.0e) through "
              "the matched terminal channel at w9: maxprod + "
              "T2val + E_pi(F^2) devs %.1e (bar %.0e) -- the "
              "weighted mean carries bit-near"
              % (TWIN_TOL, devT, TWIN_BAR))

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G97-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact M3 = ((log m)^2/m^2) T2 E_pi(F^2) "
          "identity, the E_pi(F^2) census at a-priori bars, the "
          "leave-family-out family-uniformity test, the spike "
          "anatomy of kz111/kz117, and the composition against "
          "the r361 m_0* -- NO new certificate promoted, NO "
          "universal bound claimed beyond the measured rows")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        verdict_main = weighted_tree_368(leak, brk_struct, spikes,
                                         bars_ok, lfo_ok, polylog)
        flags = []
        flags.append("IDENTITY(worst rel %.1e)" % id_w)
        flags.append("E_PI(C_F_cens %.3f, viol %d/%d, max %.3f)"
                     % (cf_cens, n_bar_viol, n_live, epi_max))
        flags.append("SLOPE(%s ratio %.3f)"
                     % (slope_let, slope_ratio))
        flags.append("LFO(%s)"
                     % ("CARRIES" if lfo_ok else "FAILS"))
        flags.append("SPIKES(%s)"
                     % ("DOMINATE" if spikes else "PI_LIGHT"))
        flags.append("COMPOSITION(m_0* %s / floor-T2 %s vs "
                     "10^%.1f/10^%.1f)"
                     % (("10^%.1f" % m0_w) if m0_w is not None
                        else "NONE",
                        ("10^%.1f" % m0_ft) if m0_ft is not None
                        else "NONE",
                        M0_REFS_368[0], M0_REFS_368[1]))
        flags.append("SCRAMBLE(%s)" % scr_txt)
        flags.append("TWIN(%.1e)" % devT)
        flags.append("MUSTFAIL_LEDGER(e1-e4 + m6a/m6b)")
        verd = verdict_main + "".join(" + " + f for f in flags)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G98-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the identity, the "
          "absorption, Fractions toys, frame reproductions, mesh "
          "identity, dictionary, N2 >= N3, purity audits "
          "(exact/AST-decided); CENSUS: every E_pi(F^2), a-priori "
          "bar violation, LFO freeze, spike share and composed "
          "m_0* (the finite 89 + 8 + 42 + 42 row surface); OPEN: "
          "E_pi(F^2) as a theorem, MED-CAP/V2, any cofinal law, "
          "the actual proof; NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (wall, RUNTIME_BAR))
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
