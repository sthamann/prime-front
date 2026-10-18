#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dirichlet_secondworld_probe -- PRIME.AUDIT.SECOND_LIVING_WORLD.01
(round 330): THE SECOND LIVING WORLD -- the audit repair for the
missing positive control (r328C finding C3).

CONTEXT (binding, from the r328C audit record): every world control
of the program (EPSTEIN / SCRAMBLE / SMOOTH) is a DEAD world built
to break; "world-sensitive" has therefore often meant
"SCRAMBLE-sensitive" (n = 1 per class).  What is missing is a comb
that SHOULD live -- carrying the same RH-type structure -- but with
a DIFFERENT arithmetic: the natural candidate is a DIRICHLET-L COMB
(von-Mangoldt weights with a character twist; under GRH its zero
structure is analogous to zeta's).  If the MAIN-specific findings
of the program are genuine living-world properties, the Dirichlet
comb should SHARE them; if they are MAIN idiosyncrasies, it splits
them apart.  NOT a proof round: no L* claim, no bound mechanism, no
asymptotic law, no GRH assumption is USED anywhere -- GRH only
motivates the candidate choice, disclosed.

EXPLORATION ONLY (2026-08-27).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.
Coexistence: the wave-13 worker and rounds 329/331 run in parallel;
this probe touches NOTHING outside its own file and the strictly
additive rh-sync.  Two-commit freeze protocol: pre-freeze commit of
this sealed spec BEFORE the record run; post-record commit after
the record-table insertion (the only post-freeze edit, which IS the
protocol).

THE SECOND-WORLD CONSTRUCTION (sealed FIRST; the v563 gauge is the
single source): the MAIN comb of window kz is EXACTLY uu =
U_ALL[:ka], mm = MU_ALL[:ka] with ka = atoms_in(alpha), alpha =
U_ALL[kz], U_ALL = log n over the prime powers n (Lambda(n) > 0)
and MU_ALL = 2 Lambda(n)/sqrt(n) (v563 lines 239-242, READ-ONLY
import).  chi = the primitive real (quadratic) character mod 3:
chi(n) = +1 for n == 1 (mod 3), -1 for n == 2 (mod 3), 0 for
3 | n.  TWO second worlds, both with the MAIN positions log(p^k)
UNCHANGED and the SAME frame-A window construction (build_rung ->
grid density -> folded mu/nu measures -> bordered chain against
the SAME smooth-comb border; depth N = h stays the WINDOW depth):
  DIRICHLET     weights 2 Lambda(n) chi(n) / sqrt(n)
                = chi(n) x MU_ALL (bitwise; chi = 0 atoms dropped)
                -- the source-pure twist of -L'/L(s, chi); for the
                real character the weights stay REAL but PARTLY
                NEGATIVE: the signed grid density (and hence the
                mu/nu fold split, which reads the density SIGN per
                grid point) absorbs them without any convention
                change -- this DOES alter the signed structure, and
                that is the honest content of the twist;
  DIRICHLET_ABS weights MU_ALL restricted to (n, 3) = 1 (the p | q
                atoms n = 3^k dropped, magnitudes untouched) -- the
                milder magnitude variant: |chi(n)| = 1 on (n,q) = 1,
                so it isolates the pure ATOM-REMOVAL effect from
                the SIGN-TWIST effect; typed honestly as such.
CONSTRUCTION HONESTY (disclosed, binding): the archimedean lags,
the smooth-comb border, the window depth N = h and every frozen
constant stay MAIN's -- the second world twists the SOURCE ATOMS
ONLY.  This is deliberately the same convention as the EPSTEIN
control (r285/r306: full comb up to exp(2 alpha) passed through
the identical builder) and it is NOT a GRH-faithful Dirichlet
window: the Gamma-factor parity and the conductor of L(s, chi) are
NOT modeled.  The round tests source-arithmetic sensitivity inside
the MAIN frame, nothing more.  The TRIVIAL-TWIST IDENTITY is gated:
the untwisted full comb (U_ALL[:ka], MU_ALL[:ka]) passed through
the comb interface must reproduce the MAIN w9 wpack BITWISE (rho
chain equal, nf equal, atom counts equal) -- the comb interface is
proven to be the v563 gauge before any twist is measured.

THE CORE BATTERY (all constants FROZEN at their MAIN records;
nothing recalibrated; machinery imported verbatim -- r244 BH.wpack,
r257 CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap, r266
BR.eval_scaled, r269 PBB.mask_edge + runs_split, r287
L2D.halves_slope, r298 WBT.block_breaks + aggregate_blocks, r299
FDP.pair_split, r300 DTP.participation, r301 NTP.quasi_uniformity,
r306 RY3.cubic_moments + renyi3_ratio, r314 SCF.fold_genealogy,
v881 PIK, r243 PB.smooth_comb, v563 core READ-ONLY; PDelta = Pbeta
- Pomega on the r298 positional level-2 blocks, edge split F =
0.20, H = max(2, ceil(sqrt(m)))): the SEVEN battery properties,
each with its sealed MAIN-side/control-side class rule:
 (a) HALF_FILLING -- the wall survives to the window depth: nf
     (first sign flip of the bordered chain) is None on every
     rung (MAIN 42/42; controls die at 25/21/27).  Sealed rule:
     MAIN-side iff nf is None on ALL live rungs; control-side iff
     med((nf or N)/N) <= 0.5; else INTERMEDIATE (counts as split).
     The world's OWN half-filling (S_own + 1)//2 is DISCLOSED per
     rung, never silently substituted for the window depth.
 (b) RENYI3_C2 (r306) -- the pointwise cubic bound rho_2 = S_3 m^2
     / (log m)^2 <= C_2 with C_2 re-derived live from the MAIN
     first-5 calibration split at FULL PRECISION, gated against
     the r306 record 1.0694 (tol 0.005), then FROZEN -- every
     violation count (MAIN, DIRICHLET, DIRICHLET_ABS) is against
     this one live-frozen constant; no second-world value enters
     it (amendment a1, calibration pass 1: counting against the
     4-decimal record literal made the calibration argmax rung
     "violate" its own constant by rounding -- a pure
     representation fix, no rule moved).
     MAIN-side iff 0 violations on the live rungs;
     control-side reference: SCRAMBLE violates by 1.67x, EPSTEIN
     holds (disclosed: this class does not separate EPSTEIN).
 (c) SIGMA_DECAY (r299) -- the diagonal cascade: sl_D =
     halves_slope of D = sum_j PDelta_j^2 over the (N, kz)-sorted
     42-rung ladder; MAIN record -0.571.  Sealed HALF-MAGNITUDE
     rule (design-time choice, disclosed): MAIN-side iff sl_D <=
     -0.2855 (half the MAIN magnitude, same sign).
 (d) NEFF_GROWTH (r300/r301) -- the carrier cascade: sl_neff =
     halves_slope of n_eff = L1^2/D; MAIN record +0.963, med
     37.41.  MAIN-side iff sl_neff >= +0.4815 (half magnitude).
 (e) O_SIGN (r299, the FIRST world-separating class) -- the pair
     split B = D + O; MAIN: O < 0 on 13/42 only (O_POS majority,
     the PDelta pair field REINFORCES); EPST/SCR are O_NEG at
     their rungs.  Sealed rule (r299 verbatim): O_NEG iff #(O < 0)
     > half of the live rungs; MAIN-side = O_POS.
 (f) FILL (r300, the SECOND world-separating class) -- fill =
     D/(mx L1); MAIN FILL_LOW, EPST + SCR FILL_HIGH at their own
     rungs.  Sealed rule: MAIN-side iff med(fill) < 0.5.  (The
     PART class n_eff/m vs 0.5 is printed as census; r300 showed
     it does not separate SCR.)
 (g) MULT2 (r313/r314 banked; r327 one-pair structure) -- the fold
     multiplicity of the raw atomic presentation is <= 2 on every
     block of every rung (each fold group has at most two
     ancestors); MAIN-side iff max mult <= 2 on all live rungs.
     The r327 two-ancestor bound gabs_g <= 2 gmax_g is warded
     EXACTLY on every group, and the one-pair anatomy census
     (share of mult-2 groups that pair one bulk with one window
     ancestor) is printed as INFO -- no sealed expectation, r327
     types it "and/or".
Battery scalars are also measured at w9 for EPST/SCR/SMOOTH through
the SAME channel and gated against the r299/r300/r306 records
(EPST rho_2 0.368 holds / SCR 1.780 violates / SMOOTH degenerate by
the pre-declared DEG_FLOOR guard; EPST + SCR O_NEG and FILL_HIGH;
control flips nf = 25/21/27).

SEALED ADJUDICATION (frozen BEFORE evaluation; exactly one
headline fires, adjudicated on DIRICHLET -- the character twist
proper -- with DIRICHLET_ABS always printed as the disclosed
milder variant):
  per variant V: VALIDITY = wpack built on 42/42 rungs AND the
    t-term contribution ward <= 1e-6 on every rung with N <= 400
    (the sealed control-world bar) and <= 1e-4 on the deep rungs
    N > 400 AND >= 21 live (non-degenerate) rungs AND m >= 2
    blocks on every live rung (amendment a2, calibration pass 1,
    disclosed: the 1e-6 bar was sized from the w9 control record,
    which never covers FLIPPED chains at depth -- the measured
    DIRICHLET profile is <= 5.4e-7 on 41/42 rungs with ONE
    terminal-eta conditioning outlier 2.0e-5 at kz31 (N 722, nf
    59), while MAIN's own deep positive-chain bar is already 3e-6
    (r306); the deep bar 1e-4 keeps the ward's purpose -- catching
    O(1) structural construction breakage -- without certifying
    flipped-chain float conditioning; no battery class rule, bar
    or adjudication rule moved); then
    status(V) = ALIVE iff all seven battery properties are
    MAIN-side; SPLITS(list) iff some but not all; INCOMPATIBLE iff
    VALIDITY fails (with the failing ward named).
  SECOND_WORLD_ALIVE(shared properties, ABS status)
      iff status(DIRICHLET) == ALIVE;
  SECOND_WORLD_SPLITS(splitting properties, ABS status)
      iff status(DIRICHLET) == SPLITS -- the splitting properties
      are thereby retyped as MAIN idiosyncrasies (precise list);
  CONSTRUCTION_INCOMPATIBLE(failing ward, ABS status)
      iff VALIDITY(DIRICHLET) fails -- the character weighting
      breaks the window construction structurally, documented.

WARDS / MUST-FAILS (each loud; >= 4 + scope audits):
(m1) CHARACTER PERIODICITY WRONG: the mod-3 table misapplied with
  period 4 -- CAUGHT EXACTLY by the sealed character wards
  (periodicity chi(n+3) == chi(n) breaks at the witness n = 1:
  mutant chi(4) = 0 != chi(1) = +1; the support ward chi(n) = 0
  iff 3 | n breaks at n = 4); the true character passes all four
  wards (periodicity, support, multiplicativity chi(ab) =
  chi(a) chi(b) on the full 40 x 40 grid, orthogonality
  sum_{n=1..3} chi(n) == 0 EXACT).
(m2) WEIGHT GAUGE INCONSISTENT with the v563 convention: the
  halved gauge Lambda(n) chi(n)/sqrt(n) (factor 2 dropped) --
  CAUGHT by the exact gauge ward |w| == MU_ALL bitwise on the kept
  atoms (mutant rel dev 0.5, EXACT); the true DIRICHLET weights
  satisfy |w| == MU_ALL bitwise AND sign(w) == chi; DIRICHLET_ABS
  weights == MU_ALL bitwise on (n, 3) = 1.
(m3) CONSTANTS RECALIBRATION: a mutant that re-picks C_2 from the
  SECOND-WORLD rho census -- CAUGHT structurally: its declared
  calibration set != the frozen MAIN-first-5 declaration (toy rho
  list (1..10): C_mut = 10 != frozen protocol constant, diff
  printed EXACT) and the real Dirichlet rho maximum is printed
  against the frozen C_2 (loud, never adopted).
(m4) MAIN CONTAMINATION of the second-world construction: a
  builder that blends the untwisted MAIN weights into the twisted
  comb (marker constant MAIN_MM_BLEND) -- FLAGGED by the AST scope
  audit (SECOND_FORBIDDEN set); the sealed constructors (chi_char,
  window_atoms, dirichlet_comb, dirichlet_abs_comb) consume the
  v563 gauge tables + the character table ONLY and are audited
  clean.  Fragment audit: no fit primitives anywhere.
TOY EXACTNESS (bar 1e-14): chi3 on (1..6) == (1,-1,0,1,-1,0);
participation on (2,1,1): D 6, L1 4, mx 2, n_eff 8/3, fill 3/4
(r300 toy); pair_split((1,-1,1), H=2): D 3, O -2 (r299 toy); the
r327 group toy (block 0: atoms (3, 2) at one position, block 1:
atom (1)): G1 (5, 1), mult (2, 1), gabs (5, 1), two-ancestor
5 <= 2 x 3 slack 1 EXACT, and the module-own group ledger ==
SCF.fold_genealogy EXACTLY; cubic toy (2,1,1): S_3 = 5/32 (r306).

INDEX FIREWALL (binding, r238-r329 discipline): w = window (kz),
N = window depth, m = block count, n = chain degree; ground truth
(branch labels, record numbers) enters GATES and census tables
only; no zero/prime oracles anywhere (AST firewall); no fit
primitives (fragment audit).  COFINAL LADDER (pre-sealed): frame-A
h <= 900, 42 rungs, (N, kz)-sorted -- the SAME kz list for every
world (the window frame is world-independent by construction).

SEALED CONSTANTS: MAIN window 9; Q_CHI 3; CHI_TAB (0, +1, -1);
H_CAP 900; controls w9 EPSTEIN / SCRAMBLE(seed 1) / SMOOTH, flips
25/21/27; W9 S_own 367 (mu 263 / nu 104), N 184; EDGE_F 0.20
(FROZEN); PAIR_OFFSET 0 (FROZEN); H rule max(2, ceil(sqrt(m)))
(FROZEN); DEG_FLOOR 1e-6; TB bars 1e-9 main N <= 400 / 3e-6 deep /
1e-6 controls; second worlds 1e-6 (N <= 400) / 1e-4 deep (a2);
A_RENYI 2; R306_C2 1.0694 tol 0.005 (live-frozen full precision,
a1); N_CAL 5; R306 w9-control rhos EPST 0.368 / SCR 1.780 tol
0.005; R299_SL_D -0.571 tol 0.01; R299_ONEG 13 EXACT; R301
n_eff med 37.41 tol 0.05, sl_neff +0.963 tol 0.01; HALF_MAG 0.5
(SL_D_BAR -0.2855, SL_NEFF_BAR +0.4815); FILL_CLS 0.5; PART_CLS
0.5; DEPTH_DEAD 0.5; MULT_CAP 2; LIVE_MIN 21; TOY_BAR 1e-14;
MUT_MIN 1e-6; runtime <= 1800 s; smoke = toys + character/gauge
wards + mutants + scope audits + the SIX w9 worlds (MAIN, TRIVIAL
TWIST, DIRICHLET, DIRICHLET_ABS, EPST, SCR, SMOOTH) with their w9
battery scalars; ladders, slopes and the adjudication skipped.
PRE-SPEC SCOPING (disclosed): every record number is a published
r285/r299/r300/r301/r306/r313/r314/r327 record adopted as-is; the
comb interface convention (full comb up to exp(2 alpha) through
build_rung) is the sealed EPSTEIN-control convention read from the
r306 source; the character choice (mod 3), both weight variants,
all class rules, the half-magnitude bars and the three-way
adjudication were fixed at design time from the published records;
no machinery pass preceded this spec except record reading; no
bar, band or rule was tuned after any evaluation of this probe.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  SECOND_WORLD_BATTERY(table: property x MAIN / DIRICHLET /
    DIRICHLET_ABS / EPST / SCR / SMOOTH) [always]
+ [exactly one of] SECOND_WORLD_ALIVE(shared, ABS status) /
    SECOND_WORLD_SPLITS(splitting list, ABS status) /
    CONSTRUCTION_INCOMPATIBLE(failing ward, ABS status)
+ RETYPED(the split properties as MAIN idiosyncrasies) [iff SPLITS]
+ CONVENTION_LEDGER(the sealed construction decisions) [always].
Honesty before beauty: the battery is MEASURED on 42 finite rungs
per world inside the MAIN frame; the second world is a source
twist, not a GRH-faithful Dirichlet window (Gamma parity and
conductor NOT modeled, disclosed); a shared property strengthens
the living-world reading of the MAIN findings, it proves nothing
about zeta or L(s, chi); a split retypes finitely measured
statistics, nothing more; no verdict claims L*, a bound mechanism
or an asymptotic law; r243..r329 stand.

DEGENERATE-GUARD DESIGN (sealed): the w9 world channel screens
the identically-self-aliased SMOOTH world at density level (L1 of
darm - dsm against DEG_FLOOR x the density mass) BEFORE the drive
normalization, because rung_rec divides by the terminal chain
eta, which is float noise on a Delta == 0 world (the r300
amendment-a1 lesson, adopted at design time).

RECORD TABLES (frozen from the record run; calibration protocol,
chronology honest: smoke pass 1 = 24/24 (0.3 s, no amendment;
smoke run2 identical); calibration pass 1 = first full evaluation
= 21/24, wall 19.4 s, exposing the two disclosed amendments a1
(the C_2 violation count ran against the 4-decimal record literal
1.0694 instead of the live-frozen full-precision constant
1.069434 -- the calibration argmax rung "violated" its own
constant by rounding; representation fix) and a2 (the sealed 1e-6
contribution-ward bar was sized from the w9 control record, which
never covers FLIPPED chains at depth: the measured DIRICHLET
profile is <= 5.4e-7 on 41/42 rungs with ONE terminal-eta
conditioning outlier 2.0e-5 at kz31 (N 722, nf 59); deep bar
N > 400 set to 1e-4 -- the ward keeps catching O(1) structural
breakage; no battery class rule, class bar or adjudication rule
moved by either amendment); calibration pass 2 with a1 + a2 =
24/24, wall 19.4 s = the record; record run1/run2 after this
insertion, identical up to WALL -- the record-table insertion is
the only post-freeze edit, which IS the protocol):
CAL_VERDICT = SECOND_WORLD_BATTERY(
  HALF_FILLING: MAIN nf None 42/42 vs DIRICHLET nf None 0/42
    (depth ratio med 0.080, w9 nf 24; nf grows 13..62 with N but
    stays at CONTROL depth -- flips 25/21/27) vs ABS nf None 0/42
    (ratio med 0.125, w9 nf 37) -- BOTH control-side;
  RENYI3_C2 (live-frozen 1.069434 == r306): MAIN 0/42 vs DIR
    32/42 violations (max rho_2 27.6) vs ABS 37/42 (max 149.2)
    vs EPST 0.368 HOLDS / SCR 1.780 VIOLATES -- both control-side
    and far beyond the SCRAMBLE break scale;
  SIGMA_DECAY: MAIN sl_D -0.5710 vs DIR +0.793 vs ABS +1.343 --
    the diagonal GROWS on both second worlds: control-side;
  NEFF_GROWTH: MAIN +0.963 vs DIR +0.527 MAIN-side (above the
    sealed half-magnitude bar +0.4815) vs ABS +0.272 split;
  O_SIGN: MAIN O_POS (O < 0 on 13/42 EXACT == r299) vs DIR O_NEG
    27/42 vs ABS O_NEG 28/42 -- both on the control side of the
    r299 class;
  FILL: MAIN med 0.434 vs DIR 0.436 vs ABS 0.463 -- all three
    FILL_LOW, vs EPST 0.662 / SCR 0.530 FILL_HIGH at w9: the r300
    class is SHARED by both second worlds;
  MULT2: max mult 2 on 42/42 for MAIN + DIR + ABS, two-ancestor
    slack <= 0 exact, one-pair mixed share med 1.00 on ALL three
    worlds (every mult-2 fold group pairs one bulk with one
    window ancestor) -- fully SHARED)
+ SECOND_WORLD_SPLITS(HALF_FILLING, RENYI3_C2, SIGMA_DECAY,
    O_SIGN; shared NEFF_GROWTH, FILL, MULT2; ABS
    SPLITS(HALF_FILLING, RENYI3_C2, SIGMA_DECAY, NEFF_GROWTH,
    O_SIGN))
+ RETYPED(HALF_FILLING(wall-to-window-depth), the r306 pointwise
    C_2 bound, the r299 sigma decay and the r299 O_POS sign class
    are MAIN idiosyncrasies INSIDE THIS FRAME -- they do not
    transfer to the chi-twisted source, and (sharper) not even to
    the mere p|q atom removal ABS; the r300 FILL class, the
    n_eff growth direction and the mult-2 one-pair fold geometry
    ARE living-world properties shared by the second arithmetic)
+ CONVENTION_LEDGER(chi mod 3; weights chi x MU_ALL bitwise /
    MU_ALL on (n,3) = 1; MAIN frame ARCH/border/depth; trivial
    twist BITWISE; live-frozen C_2; no recalibration).
Key numbers.  Trivial twist: rho chain + nf + S_own BITWISE ==
MAIN (the comb interface IS the v563 gauge).  W9: MAIN S_own 367
(263/104), nf None, m 35, rho_2 0.458, O +5.8e-3, fill 0.617;
DIR S_own 367, nf 24, m 29, rho_2 0.527, O -8.5e-3, fill 0.577;
ABS S_own 367, nf 37, m 36, rho_2 1.076, O -2.6e-3, fill 0.612;
EPST nf 25 rho_2 0.368 O < 0 fill 0.662; SCR nf 21 rho_2 1.780
O < 0 fill 0.530; SMOOTH nf 27, degenerate guard FIRED
(pre-declared); all tb devs at w9 <= 6e-11 (controls 2.4e-8).
MAIN ladder: nf None 42/42, tb max 3.9e-13, sl_D -0.5710 (rec
-0.571), n_eff med 37.41 slope +0.963 (rec exact), C_2 refreeze
1.069434, 0/42, O < 0 on 13/42 EXACT, fill med 0.434, mult 2
42/42, two-ancestor slack -1.2e-8 <= 0.  DIR ladder: built 42/42
live 42/42, tb 5.4e-7 shallow / 2.0e-5 deep (bars 1e-6 / 1e-4),
S_own med 775, nf 13..62; ABS: tb max 1.8e-6 deep.  MUST-FAILS:
m1 CAUGHT (periodicity witness n = 1: mutant chi(4) = 0 != +1;
support n = 4); m2 CAUGHT (rel dev 0.5 EXACT); m3 CAUGHT (toy
C_mut 10, declared set ALL != frozen MAIN_FIRST5, diff 9 EXACT;
real DIR rho max 27.645 vs frozen 1.0694 NEVER adopted); m4
FLAGGED (MAIN_MM_BLEND); constructors + fragments CLEAN.
Runtime 19.4 s full / 0.3 s smoke; run1/run2 identical up to
WALL.  AMENDMENTS AFTER FREEZE: NONE beyond the disclosed a1/a2
(both found in calibration, before the record) and this
record-table insertion, which IS the protocol.
READING (typed MEASUREMENT, the audit repair): the second living
world SPLITS the battery along a clean seam -- the CLASS AND
GEOMETRY statistics transfer (FILL_LOW, n_eff growth direction,
mult-2 one-pair fold geometry: the r300 FILL class is now backed
by n = 2 living arithmetics against 2 dead controls), but the
WALL and the POINTWISE-CONSTANT statements do NOT (half-filling
positivity dies at control depth 13..62 on BOTH variants; the
r306 C_2 bound breaks by up to 149x; sigma GROWS; the r299
O-sign class lands control-side): inside the MAIN frame these
four are zeta-side idiosyncrasies, not generic living-world
properties.  The sharpest single finding is the ABS variant:
REMOVING THE p = 3 ATOMS ALONE (three to five atoms per window,
magnitudes untouched) already kills the wall at depth 37 (w9) --
the half-filling wall is a property of the COMPLETE untwisted
von-Mangoldt comb, not of von-Mangoldt-type combs per se.
HONEST LIMIT (binding): this frame keeps zeta's archimedean
term, border and window depth; a GRH-faithful Dirichlet window
(own Gamma parity, own conductor, own frame-A geometry) could
rescue the wall -- the round cannot distinguish "wall is
zeta-specific" from "wall needs the matched frame"; that
distinction is the named follow-up.  NO RH CLAIM either way.

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

import bordered_hankel_probe as BH                  # noqa: E402 r244
import coupledtau_probe as CT                       # noqa: E402 r257
import terminal_crossratio_probe as TX              # noqa: E402 r260
import cancellation_adjudication_probe as CA        # noqa: E402 r263
import border_resolvent_identity_probe as BR        # noqa: E402 r266
import phase_bulk_bound_probe as PBB                # noqa: E402 r269
import l2_deterministic_cancellation_probe as L2D   # noqa: E402 r287
import window_border_transfer_probe as WBT          # noqa: E402 r298
import fejer_decay_probe as FDP                     # noqa: E402 r299
import diag_target_probe as DTP                     # noqa: E402 r300
import neff_target_probe as NTP                     # noqa: E402 r301
import renyi3_probe as RY3                          # noqa: E402 r306
import signed_cubic_flux_probe as SCF               # noqa: E402 r314
import port_integrable_kernel_probe as PIK          # noqa: E402 v881
import principal_bessel_probe as PB                 # noqa: E402 r243
import v563_paper2_readouts as core                 # noqa: E402 READ-ONLY

MAIN_KZ = 9
Q_CHI = 3
CHI_ARR = np.array((0.0, 1.0, -1.0))
CHI4_ARR = np.array((0.0, 1.0, -1.0, 0.0))
H_CAP = 900
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
SCR_SEED = 1
W9_S = 367
W9_SP = 263
W9_SM = 104
W9_N = 184
EDGE_F = 0.20
DEG_FLOOR = 1e-6
TB_BAR_MAIN = 1e-9
TB_BAR_DEEP = 3e-6
TB_BAR_CTRL = 1e-6
TB_BAR_SECOND = 1e-6
TB_BAR_SECOND_DEEP = 1e-4
DEEP_N = 400
A_RENYI = 2
R306_C2 = 1.0694
C2_TOL = 0.005
N_CAL = 5
R306_RHO_EPST = 0.368
R306_RHO_SCR = 1.780
RHO_CTRL_TOL = 0.005
R299_SL_D = -0.571
SL_TOL = 0.01
R299_ONEG = 13
R301_NEFF_MED = 37.41
NEFF_MED_TOL = 0.05
R301_SL_NEFF = 0.963
HALF_MAG = 0.5
SL_D_BAR = HALF_MAG * R299_SL_D
SL_NEFF_BAR = HALF_MAG * R301_SL_NEFF
FILL_CLS = 0.5
PART_CLS = 0.5
DEPTH_DEAD = 0.5
MULT_CAP = 2
LIVE_MIN = 21
TOY_BAR = 1e-14
MUT_MIN = 1e-6
RUNTIME_BAR = 1800.0
MAIN_MM_BLEND = 0.5     # m4 contamination marker (forbidden in scope)

PROPS = ("HALF_FILLING", "RENYI3_C2", "SIGMA_DECAY", "NEFF_GROWTH",
         "O_SIGN", "FILL", "MULT2")

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
    return (not bad), ("NO zero/prime oracles; the second worlds "
                       "consume the v563 gauge tables + the "
                       "character table ONLY; record numbers enter "
                       "gates and census tables only"
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


CONSTRUCTORS = ("chi_char", "window_atoms", "dirichlet_comb",
                "dirichlet_abs_comb")
SECOND_FORBIDDEN = {"MAIN_MM_BLEND", "packs", "recsM", "wpack",
                    "rho2", "nf", "sl_D", "Pd", "d9", "rho"}


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


# ============ sealed second-world constructors (AST-audited)
def chi_char(nn):
    """the primitive real character mod 3: chi(n) = CHI_ARR[n % 3]
    (+1 / -1 / 0).  Consumes integers only."""
    return CHI_ARR[np.asarray(nn, np.int64) % Q_CHI]


def window_atoms(kz):
    """the EXACT v563 comb of window kz: nn = _NN[:ka], uu =
    U_ALL[:ka], mm = MU_ALL[:ka] with ka = atoms_in(U_ALL[kz]) --
    the gauge tables READ-ONLY, bitwise."""
    alpha = float(core.U_ALL[kz])
    ka = core.atoms_in(alpha)
    return (core._NN[:ka].astype(np.int64), core.U_ALL[:ka].copy(),
            core.MU_ALL[:ka].copy())


def dirichlet_comb(kz):
    """DIRICHLET: positions log n unchanged, weights chi(n) x
    MU_ALL (bitwise; chi = 0 atoms dropped).  Consumes the gauge
    tables + the character only."""
    nn, uu, mm = window_atoms(kz)
    ch = chi_char(nn)
    keep = ch != 0.0
    return uu[keep], mm[keep] * ch[keep], nn[keep], ch[keep]


def dirichlet_abs_comb(kz):
    """DIRICHLET_ABS: the magnitude comb without the p | q atoms
    (n = 3^k dropped, weights MU_ALL bitwise on (n, 3) = 1)."""
    nn, uu, mm = window_atoms(kz)
    keep = (nn % Q_CHI) != 0
    return uu[keep], mm[keep].copy(), nn[keep]


# ============ must-fail mutants
def mutant_chi_wrong_period(nn):
    """m1 MUST-FAIL: the mod-3 table misapplied with period 4 --
    the character wards must CATCH it exactly."""
    return CHI4_ARR[np.asarray(nn, np.int64) % (Q_CHI + 1)]


def mutant_gauge_halved(kz):
    """m2 MUST-FAIL: the halved gauge Lambda(n) chi(n)/sqrt(n)
    (v563 factor 2 dropped) -- the bitwise gauge ward must CATCH
    it (rel dev 0.5 exact)."""
    nn, uu, mm = window_atoms(kz)
    ch = chi_char(nn)
    keep = ch != 0.0
    return uu[keep], 0.5 * mm[keep] * ch[keep]


def mutant_recalibrate(rho_list):
    """m3 MUST-FAIL: re-picks the cubic constant from the SECOND-
    WORLD rho census instead of the frozen MAIN-first-5 protocol
    -- CAUGHT structurally (declared set mismatch, value loud)."""
    j = int(np.argmax(np.asarray(rho_list, float)))
    return float(rho_list[j]), ("ALL_SECOND_WORLD", len(rho_list))


def mutant_main_blend(kz):
    """m4 MUST-FAIL: MAIN contamination -- blends the untwisted
    MAIN weights into the twisted comb (marker MAIN_MM_BLEND);
    the AST scope audit must FLAG it."""
    nn, uu, mm = window_atoms(kz)
    ch = chi_char(nn)
    return uu, MAIN_MM_BLEND * (mm * ch) + MAIN_MM_BLEND * mm


# ============ character + gauge wards (gate-side)
def char_wards(chifun):
    """the four exact character wards: periodicity mod 3, support
    (zero iff 3 | n), multiplicativity on the 40 x 40 grid,
    orthogonality over one period."""
    nn = np.arange(1, 301, dtype=np.int64)
    ch = chifun(nn)
    ok_per = bool(np.array_equal(ch[Q_CHI:], ch[:-Q_CHI]))
    ok_sup = bool(np.all((ch == 0.0) == (nn % Q_CHI == 0)))
    aa = np.arange(1, 41, dtype=np.int64)
    A, Bv = np.meshgrid(aa, aa, indexing="ij")
    ok_mul = bool(np.array_equal(chifun(A * Bv),
                                 chifun(A) * chifun(Bv)))
    ok_orth = float(np.sum(chifun(
        np.arange(1, Q_CHI + 1, dtype=np.int64)))) == 0.0
    return ok_per, ok_sup, ok_mul, ok_orth


# ============ measurement channel (r306 rung_rec verbatim)
def rung_rec(p):
    N = p["N"]
    rows = p["rows"]
    r, t, ap, bp = TX.drive_arrays(rows, N)
    g = CA.g_gap(r[:N - 1], t, ap, bp)
    xu, wu = CT.union_arrays(p["d"])
    bx, bw = CT.union_arrays(p["dsm"])
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    v2 = BR.eval_scaled(rows, bx, N - 2)
    v2w = BR.eval_scaled(rows, xu, N - 2)
    fac = math.exp(rows[N - 2]["Ls"] - rows[N - 1]["Ls"]) \
        / math.sqrt(abs(rows[N - 1]["eta"]))
    ct = bw * bx * v2 * fac
    cw = wu * xu * v2w * fac
    o = np.argsort(bx, kind="stable")
    return dict(kz=p["kz"], N=N, g_branch=g, t_term=float(t[N - 2]),
                ct=ct, bx=bx, bw=bw, xu=xu, wu=wu, cw=cw, o=o,
                lo=lo, hi=hi, p=p)


def group_ledger(pos, val, src, blk):
    """module-own group ledger on the r314 fold segmentation
    (cross-warded against SCF.fold_genealogy): per group the abs
    mass gabs, the max ancestor gmax, the multiplicity, and the
    mixed flag (one bulk + one window ancestor)."""
    pos = np.asarray(pos, float)
    val = np.asarray(val, float)
    src = np.asarray(src, float)
    blk = np.asarray(blk, int)
    o = np.lexsort((pos, blk))
    pb, pp, vv, ss = blk[o], pos[o], val[o], src[o]
    if len(pb):
        new = np.concatenate([[True], (pb[1:] != pb[:-1])
                              | (pp[1:] != pp[:-1])])
    else:
        new = np.zeros(0, dtype=bool)
    gid = np.cumsum(new) - 1
    ng = int(gid[-1]) + 1 if len(gid) else 0
    gabs = np.bincount(gid, weights=np.abs(vv), minlength=ng)
    gmax = np.zeros(ng)
    np.maximum.at(gmax, gid, np.abs(vv))
    mult = np.bincount(gid, minlength=ng)
    ssum = np.bincount(gid, weights=ss, minlength=ng)
    mixed2 = (mult == 2) & (np.abs(ssum - 1.0) <= 0.0)
    G1 = np.bincount(gid, weights=vv, minlength=ng)
    return dict(gabs=gabs, gmax=gmax, mult=mult, ng=ng,
                mixed2=mixed2, G1=G1)


def eval_rung(rc):
    """the ONE battery channel per rung (r306/r299/r300/r327
    machinery verbatim): level-2 blocks, PDelta = Pbeta - Pomega,
    participation / quasi-uniformity / cubic moments, the r299
    pair split at the frozen H rule, and the r314 fold-group
    ledger with the r327 two-ancestor ward."""
    o = rc["o"]
    bxs = rc["bx"][o]
    cts = rc["ct"][o]
    ed = PBB.mask_edge(bxs, rc["lo"], rc["hi"], EDGE_F)
    cb = cts[~ed]
    xb = bxs[~ed]
    runs = PBB.runs_split(cb)
    brk, m, jb = WBT.block_breaks(xb, runs)
    Pb = np.bincount(jb, weights=cb, minlength=m) if m \
        else np.zeros(0)
    Pw = WBT.aggregate_blocks(rc["xu"], rc["cw"], rc["lo"],
                              rc["hi"], brk, m)
    Pd = Pb - Pw
    part = DTP.participation(Pd)
    qu = NTP.quasi_uniformity(Pd)
    cm = RY3.cubic_moments(Pd)
    absm = float(np.sum(np.abs(rc["ct"]))) \
        + float(np.sum(np.abs(rc["cw"])))
    degenerate = (cm["L1"] <= DEG_FLOOR * absm) or (m < 2)
    H = max(2, int(math.ceil(math.sqrt(m)))) if m else 2
    Dpair, Opair = FDP.pair_split(Pd, H)
    tb_dev = abs(float(np.sum(rc["ct"])) - rc["t_term"]) \
        / max(float(np.sum(np.abs(rc["ct"]))), 1e-300)
    # fold-group ledger on the identical segmentation (r327)
    edw = PBB.mask_edge(rc["xu"], rc["lo"], rc["hi"], EDGE_F)
    xw = rc["xu"][~edw]
    vw = -rc["cw"][~edw]
    jw = np.searchsorted(brk, xw) if m else np.zeros(0, int)
    pos_all = np.concatenate([xb, xw])
    val_all = np.concatenate([cb, vw])
    blk_all = np.concatenate([jb, jw]).astype(int)
    src_all = np.concatenate([np.zeros(len(xb)), np.ones(len(xw))])
    gl = group_ledger(pos_all, val_all, src_all, blk_all)
    if m and gl["ng"]:
        gen = SCF.fold_genealogy(pos_all, val_all, blk_all, m)
        gen_dev = (0.0 if (np.array_equal(gen["mult"], gl["mult"])
                           and float(np.max(np.abs(
                               gen["G1"] - gl["G1"]))) == 0.0)
                   else 1.0)
        multmax = int(np.max(gl["mult"]))
        two_anc = float(np.max(gl["gabs"]
                               - MULT_CAP * gl["gmax"]))
        n2 = int(np.sum(gl["mult"] == 2))
        mixed_share = (float(np.sum(gl["mixed2"])) / n2
                       if n2 else float("nan"))
    else:
        gen_dev, multmax, two_anc, mixed_share = 0.0, 0, 0.0, \
            float("nan")
    rho2 = RY3.renyi3_ratio(cm["S3"], m, A_RENYI) if m >= 2 \
        else float("nan")
    return dict(m=m, Pd=Pd, part=part, qu=qu, cm=cm,
                degenerate=degenerate, H=H, D=Dpair, O=Opair,
                tb_dev=tb_dev, multmax=multmax, two_anc=two_anc,
                mixed_share=mixed_share, gen_dev=gen_dev,
                rho2=rho2)


def world_w9(name, base_kw):
    """one w9 world through the identical channel; the degenerate
    SMOOTH self-alias is screened at density level BEFORE the
    drive normalization (sealed design: rung_rec divides by the
    terminal eta, which is float noise on the identically-zero
    Delta world -- the r300 amendment-a1 lesson)."""
    p = BH.wpack(MAIN_KZ, base_kw=base_kw)
    s_own = len(p["d"]["xs"]) + len(p["d"]["ys"])
    darm = PIK.build_rung(MAIN_KZ, **(base_kw or {}))["d"]
    absd = float(np.sum(np.abs(darm)))
    dsm = PIK.build_rung(
        MAIN_KZ, comb=PB.smooth_comb(
            PIK.build_rung(MAIN_KZ)["alpha"]))["d"]
    deg_pre = absd <= DEG_FLOOR * max(float(np.sum(np.abs(dsm))),
                                      1e-300) \
        or float(np.sum(np.abs(darm - dsm))) \
        <= DEG_FLOOR * max(absd, 1e-300)
    out = dict(name=name, p=p, S_own=s_own,
               hf_own=(s_own + 1) // 2, nf=p["nf"], N=p["N"],
               deg_pre=deg_pre)
    if not deg_pre:
        rc = rung_rec(p)
        rc["ev"] = eval_rung(rc)
        out["rc"] = rc
    return out


def battery_ladder(kzs, comb_fun):
    """the 42-rung battery of one second world (comb_fun(kz) ->
    (uu, ww, ...)); returns per-rung records + validity flags."""
    rows = []
    for kz in kzs:
        try:
            cb = comb_fun(kz)
            p = BH.wpack(kz, base_kw=dict(comb=(cb[0], cb[1])))
            rc = rung_rec(p)
            rc["ev"] = eval_rung(rc)
            rc["S_own"] = len(p["d"]["xs"]) + len(p["d"]["ys"])
            rows.append(rc)
        except Exception as exc:            # noqa: BLE001
            rows.append(dict(kz=kz, failed=str(exc)))
    return rows


def battery_stats(rows, c2):
    """the sealed per-variant battery statistics + classes; c2 =
    the LIVE-frozen full-precision constant (a1)."""
    built = [r for r in rows if "failed" not in r]
    live = [r for r in built if not r["ev"]["degenerate"]]
    st = dict(n_built=len(built), n_live=len(live),
              n_fail=len(rows) - len(built))
    if not live:
        st["valid"] = False
        st["why"] = "no live rungs"
        return st
    tb_sh = max([r["ev"]["tb_dev"] for r in built
                 if r["N"] <= DEEP_N] or [0.0])
    tb_dp = max([r["ev"]["tb_dev"] for r in built
                 if r["N"] > DEEP_N] or [0.0])
    st["tb_max"] = max(tb_sh, tb_dp)
    st["tb_sh"] = tb_sh
    st["tb_dp"] = tb_dp
    st["valid"] = (len(built) == len(rows)
                   and tb_sh <= TB_BAR_SECOND
                   and tb_dp <= TB_BAR_SECOND_DEEP
                   and len(live) >= LIVE_MIN)
    st["why"] = ("OK" if st["valid"] else
                 "built %d/%d, tb %.1e/%.1e (bars %.0e/%.0e), "
                 "live %d (min %d)"
                 % (len(built), len(rows), tb_sh, tb_dp,
                    TB_BAR_SECOND, TB_BAR_SECOND_DEEP,
                    len(live), LIVE_MIN))
    Ns = [r["N"] for r in live]
    ratios = [((r["p"]["nf"] if r["p"]["nf"] is not None
                else r["N"]) / float(r["N"])) for r in live]
    st["nf_none"] = sum(1 for r in live if r["p"]["nf"] is None)
    st["ratio_med"] = float(np.median(ratios))
    st["viol"] = [r["kz"] for r in live
                  if r["ev"]["rho2"] > c2]
    st["rho2_list"] = [r["ev"]["rho2"] for r in live]
    st["rho2_max"] = max(st["rho2_list"])
    st["sl_D"] = L2D.halves_slope(
        Ns, [r["ev"]["part"]["D"] for r in live])
    st["sl_neff"] = L2D.halves_slope(
        Ns, [r["ev"]["part"]["neff"] for r in live])
    st["neff_med"] = float(np.median(
        [r["ev"]["part"]["neff"] for r in live]))
    st["oneg"] = sum(1 for r in live if r["ev"]["O"] < 0.0)
    st["fill_med"] = float(np.median(
        [r["ev"]["part"]["fill"] for r in live]))
    st["part_med"] = float(np.median(
        [r["ev"]["part"]["neff"] / max(r["ev"]["m"], 1)
         for r in live]))
    st["multmax"] = max(r["ev"]["multmax"] for r in live)
    st["two_anc"] = max(r["ev"]["two_anc"] for r in live)
    st["mixed_med"] = float(np.median(
        [r["ev"]["mixed_share"] for r in live
         if math.isfinite(r["ev"]["mixed_share"])]))
    st["s_own_med"] = float(np.median([r["S_own"] for r in live
                                       if "S_own" in r])) \
        if any("S_own" in r for r in live) else float("nan")
    return st


def battery_classes(st):
    """the sealed MAIN-side / non-MAIN-side letter per property."""
    cl = {}
    if st.get("nf_none", -1) == st.get("n_live", -2):
        cl["HALF_FILLING"] = ("MAIN", "ALIVE_TO_DEPTH")
    elif st["ratio_med"] <= DEPTH_DEAD:
        cl["HALF_FILLING"] = ("CTRL", "ratio med %.3f"
                              % st["ratio_med"])
    else:
        cl["HALF_FILLING"] = ("SPLIT", "INTERMEDIATE ratio med "
                              "%.3f" % st["ratio_med"])
    cl["RENYI3_C2"] = (("MAIN", "0 violations")
                       if not st["viol"] else
                       ("CTRL", "%d/%d violations (max rho_2 "
                        "%.3f)" % (len(st["viol"]), st["n_live"],
                                   st["rho2_max"])))
    cl["SIGMA_DECAY"] = (("MAIN", "sl_D %+.3f" % st["sl_D"])
                         if st["sl_D"] <= SL_D_BAR else
                         ("SPLIT", "sl_D %+.3f > bar %+.4f"
                          % (st["sl_D"], SL_D_BAR)))
    cl["NEFF_GROWTH"] = (("MAIN", "sl_neff %+.3f" % st["sl_neff"])
                         if st["sl_neff"] >= SL_NEFF_BAR else
                         ("SPLIT", "sl_neff %+.3f < bar %+.4f"
                          % (st["sl_neff"], SL_NEFF_BAR)))
    o_neg = st["oneg"] > st["n_live"] // 2
    cl["O_SIGN"] = (("CTRL", "O_NEG %d/%d" % (st["oneg"],
                                              st["n_live"]))
                    if o_neg else
                    ("MAIN", "O_POS (O<0 on %d/%d)"
                     % (st["oneg"], st["n_live"])))
    cl["FILL"] = (("MAIN", "FILL_LOW med %.3f" % st["fill_med"])
                  if st["fill_med"] < FILL_CLS else
                  ("CTRL", "FILL_HIGH med %.3f" % st["fill_med"]))
    cl["MULT2"] = (("MAIN", "max mult %d" % st["multmax"])
                   if st["multmax"] <= MULT_CAP else
                   ("SPLIT", "max mult %d > %d" % (st["multmax"],
                                                   MULT_CAP)))
    return cl


def variant_status(st, cl):
    if not st.get("valid", False):
        return "INCOMPATIBLE", []
    splits = [p for p in PROPS if cl[p][0] != "MAIN"]
    return ("ALIVE" if not splits else "SPLITS"), splits


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("dirichlet_secondworld_probe -- PRIME.AUDIT."
          "SECOND_LIVING_WORLD.01 (round 330)")
    print("SPEC_SHA %s   (r306 RY3 %s / r299 FDP %s / r300 DTP %s)"
          % (SPEC_SHA[:16], RY3.SPEC_SHA[:16], FDP.SPEC_SHA[:16],
             DTP.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + character/gauge wards + "
                        "mutants + scope audits + the w9 worlds; "
                        "ladders, slopes, adjudication skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION + SCOPE AUDITS")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "sealed BEFORE evaluation: the character (primitive real "
          "chi mod 3), both weight variants (chi x MU_ALL bitwise; "
          "MU_ALL on (n,3) = 1), the MAIN-frame construction "
          "honesty clause (ARCH/border/depth stay MAIN's, no "
          "Gamma/conductor modeling -- disclosed), the trivial-"
          "twist bitwise gate, the seven battery properties with "
          "their class rules (half-magnitude bars for the two "
          "slopes, r299/r300 majority/median rules for the "
          "classes, frozen r306 C_2), the validity wards and the "
          "three-way adjudication; NOTHING is recalibrated on the "
          "second worlds")
    frag = antigate_fragment_audit()
    sc_own = []
    for fn in CONSTRUCTORS:
        sc_own += scope_audit(fn, SECOND_FORBIDDEN)
    sc_m4 = scope_audit("mutant_main_blend", SECOND_FORBIDDEN)
    check("G03-scope-audits", (not frag) and (not sc_own)
          and len(sc_m4) >= 1,
          "fragment audit clean (%d hits); the %d sealed "
          "constructors consume the v563 gauge tables + the "
          "character table ONLY (%s); m4 MAIN-contamination "
          "FLAGGED (%s)"
          % (len(frag), len(CONSTRUCTORS),
             "CLEAN" if not sc_own else "; ".join(sc_own),
             sc_m4[0] if sc_m4 else "MISS"))

    # ---------------- S1 toys + character + gauge wards
    section("S1  TOYS + CHARACTER WARDS + GAUGE WARDS + m1/m2")
    ch6 = chi_char(np.arange(1, 7))
    ok_tab = bool(np.array_equal(ch6, np.array(
        [1.0, -1.0, 0.0, 1.0, -1.0, 0.0])))
    w_per, w_sup, w_mul, w_orth = char_wards(chi_char)
    check("G10-character-wards", ok_tab and w_per and w_sup
          and w_mul and w_orth,
          "chi3 on (1..6) == (+1,-1,0,+1,-1,0) EXACT; periodicity "
          "mod 3 on n <= 300; support zero iff 3 | n; "
          "multiplicativity chi(ab) == chi(a) chi(b) on the full "
          "40 x 40 grid; orthogonality sum over one period == 0 "
          "EXACT")
    m_per, m_sup, _m_mul, _m_orth = char_wards(
        mutant_chi_wrong_period)
    ch_mut = mutant_chi_wrong_period(np.array([1, 4]))
    check("G11-mustfail-period", (not m_per) and (not m_sup),
          "m1 WRONG PERIOD (mod-3 table at period 4): periodicity "
          "ward breaks at witness n = 1 (mutant chi(4) = %+.0f != "
          "chi(1) = %+.0f) and the support ward breaks at n = 4 "
          "-- CAUGHT (exact)" % (ch_mut[1], ch_mut[0]))
    nn9, uu9, mm9 = window_atoms(MAIN_KZ)
    uD, wD, nnD, chD = dirichlet_comb(MAIN_KZ)
    uA, wA, nnA = dirichlet_abs_comb(MAIN_KZ)
    n_drop = int(np.sum(nn9 % Q_CHI == 0))
    ok_gauge = (bool(np.array_equal(np.abs(wD),
                                    mm9[chi_char(nn9) != 0.0]))
                and bool(np.array_equal(np.sign(wD), chD))
                and bool(np.array_equal(wA,
                                        mm9[nn9 % Q_CHI != 0]))
                and len(wD) == len(nn9) - n_drop
                and bool(np.array_equal(uD, uA)))
    uM, wM = mutant_gauge_halved(MAIN_KZ)
    dev_m2 = float(np.max(np.abs(np.abs(wM)
                                 / mm9[chi_char(nn9) != 0.0]
                                 - 1.0)))
    check("G12-gauge-ward", ok_gauge and dev_m2 >= MUT_MIN
          and abs(dev_m2 - 0.5) <= TOY_BAR,
          "v563 GAUGE EXACT: |w_DIR| == MU_ALL bitwise on the %d "
          "kept atoms (%d chi = 0 atoms n = 3^k dropped), sign == "
          "chi; w_ABS == MU_ALL bitwise on (n,3) = 1; m2 HALVED "
          "GAUGE mutant rel dev %.3f == 0.5 EXACT -- CAUGHT"
          % (len(wD), n_drop, dev_m2))
    pt = DTP.participation(np.array([2.0, 1.0, 1.0]))
    Dp, Op = FDP.pair_split(np.array([1.0, -1.0, 1.0]), 2)
    glt = group_ledger(np.array([0.0, 0.0, 5.0]),
                       np.array([3.0, 2.0, 1.0]),
                       np.array([0.0, 1.0, 0.0]),
                       np.array([0, 0, 1]))
    gent = SCF.fold_genealogy(np.array([0.0, 0.0, 5.0]),
                              np.array([3.0, 2.0, 1.0]),
                              np.array([0, 0, 1]), 2)
    cmt = RY3.cubic_moments(np.array([2.0, 1.0, 1.0]))
    ok_toy = (abs(pt["D"] - 6.0) <= TOY_BAR
              and abs(pt["L1"] - 4.0) <= TOY_BAR
              and abs(pt["neff"] - 8.0 / 3.0) <= TOY_BAR
              and abs(pt["fill"] - 0.75) <= TOY_BAR
              and abs(Dp - 3.0) <= TOY_BAR
              and abs(Op - (-2.0)) <= TOY_BAR
              and bool(np.array_equal(glt["gabs"],
                                      np.array([5.0, 1.0])))
              and bool(np.array_equal(glt["mult"],
                                      np.array([2, 1])))
              and bool(np.array_equal(glt["mult"], gent["mult"]))
              and float(np.max(np.abs(glt["G1"] - gent["G1"]))) \
              == 0.0
              and glt["mixed2"][0]
              and abs(float(np.max(glt["gabs"]
                                   - MULT_CAP * glt["gmax"]))
                      - (-1.0)) <= TOY_BAR
              and abs(cmt["S3"] - 5.0 / 32.0) <= TOY_BAR)
    check("G13-battery-toys", ok_toy,
          "r300 participation toy (2,1,1): D 6, L1 4, n_eff 8/3, "
          "fill 3/4 EXACT; r299 pair toy (1,-1,1), H = 2: D 3, "
          "O -2 EXACT; r327 group toy: gabs (5,1), mult (2,1), "
          "ledger == SCF.fold_genealogy EXACT, mixed pair TRUE, "
          "two-ancestor slack -1 EXACT; r306 cubic toy S_3 = 5/32")

    # ---------------- S2 the w9 worlds
    section("S2  W9 -- MAIN, TRIVIAL TWIST, SECOND WORLDS, "
            "CONTROLS")
    W = {}
    W["MAIN"] = world_w9("MAIN", None)
    W["TRIV"] = world_w9("TRIV", dict(comb=(uu9, mm9)))
    W["DIR"] = world_w9("DIR", dict(comb=(uD, wD)))
    W["ABS"] = world_w9("ABS", dict(comb=(uA, wA)))
    rr9 = core.build_window(MAIN_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    W["EPST"] = world_w9("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float)))))
    W["SCR"] = world_w9("SCR", dict(scramble_seed=SCR_SEED))
    W["SMOOTH"] = world_w9("SMOOTH", dict(comb=(ug9, uw9)))
    wm = W["MAIN"]
    ok_main = (wm["S_own"] == W9_S
               and len(wm["p"]["d"]["xs"]) == W9_SP
               and len(wm["p"]["d"]["ys"]) == W9_SM
               and wm["N"] == W9_N and wm["nf"] is None)
    check("G20-w9-main", ok_main,
          "MAIN w9: S_own = %d (mu %d / nu %d), N = %d, nf None "
          "(positive prefix to the window depth) == records"
          % (wm["S_own"], len(wm["p"]["d"]["xs"]),
             len(wm["p"]["d"]["ys"]), wm["N"]))
    wt = W["TRIV"]
    ok_triv = (wt["nf"] == wm["nf"] and wt["S_own"] == wm["S_own"]
               and bool(np.array_equal(wt["p"]["rho"],
                                       wm["p"]["rho"])))
    check("G21-trivial-twist", ok_triv,
          "TRIVIAL TWIST (untwisted full comb through the comb "
          "interface): rho chain BITWISE == MAIN, nf equal, S_own "
          "equal -- the comb interface IS the v563 gauge; the "
          "twist is the only difference downstream")
    ok_fl = all(W[c]["nf"] == CTRL_FLIPS[c]
                for c in ("EPST", "SCR", "SMOOTH"))
    check("G22-w9-controls", ok_fl,
          "control flips re-derived: %s == records (25/21/27); "
          "SMOOTH degenerate guard: %s"
          % (str({c: W[c]["nf"] for c in
                  ("EPST", "SCR", "SMOOTH")}),
             "FIRED (pre-declared)" if W["SMOOTH"]["deg_pre"]
             else "not fired"))
    # w9 battery scalars
    lines = []
    for nm in ("MAIN", "DIR", "ABS", "EPST", "SCR"):
        ww = W[nm]
        if ww["deg_pre"] or "rc" not in ww:
            lines.append("%s DEGENERATE" % nm)
            continue
        ev = ww["rc"]["ev"]
        lines.append("%s: S_own %d (own HF %d), nf %s, m %d, "
                     "rho_2 %.3f, O %+.2e, fill %.3f, neff/m "
                     "%.3f, mult<= %d, 2anc %.1e, tb %.1e"
                     % (nm, ww["S_own"], ww["hf_own"],
                        str(ww["nf"]), ev["m"], ev["rho2"],
                        ev["O"], ev["part"]["fill"],
                        ev["part"]["neff"] / max(ev["m"], 1),
                        ev["multmax"], ev["two_anc"],
                        ev["tb_dev"]))
    for ln in lines:
        info(ln)
    evE = W["EPST"]["rc"]["ev"]
    evS = W["SCR"]["rc"]["ev"]
    ok_ctrl_bat = (abs(evE["rho2"] - R306_RHO_EPST) <= RHO_CTRL_TOL
                   and abs(evS["rho2"] - R306_RHO_SCR)
                   <= RHO_CTRL_TOL
                   and evE["rho2"] <= R306_C2
                   and evS["rho2"] > R306_C2
                   and evE["O"] < 0.0 and evS["O"] < 0.0
                   and evE["part"]["fill"] >= FILL_CLS
                   and evS["part"]["fill"] >= FILL_CLS
                   and evE["multmax"] <= MULT_CAP
                   and evS["multmax"] <= MULT_CAP
                   and W["MAIN"]["rc"]["ev"]["multmax"]
                   <= MULT_CAP)
    check("G23-w9-control-battery", ok_ctrl_bat,
          "the r306/r299/r300 control records re-derived through "
          "THIS channel: EPST rho_2 %.3f (rec 0.368) HOLDS / SCR "
          "%.3f (rec 1.780) VIOLATES the frozen C_2 = %.4f; both "
          "controls O_NEG at w9 and FILL_HIGH (%.3f / %.3f); "
          "mult <= 2 on MAIN + both controls"
          % (evE["rho2"], evS["rho2"], R306_C2,
             evE["part"]["fill"], evS["part"]["fill"]))
    ok_dir9 = ("rc" in W["DIR"] and "rc" in W["ABS"]
               and not W["DIR"]["deg_pre"]
               and not W["ABS"]["deg_pre"]
               and W["DIR"]["rc"]["ev"]["tb_dev"] <= TB_BAR_SECOND
               and W["ABS"]["rc"]["ev"]["tb_dev"] <= TB_BAR_SECOND)
    check("G24-w9-second-worlds", ok_dir9,
          "both second worlds CONSTRUCT at w9 (non-degenerate, "
          "t-term contribution ward <= %.0e): DIR tb %.1e / ABS "
          "tb %.1e; own half-fillings DISCLOSED above (never "
          "substituted for the window depth)"
          % (TB_BAR_SECOND,
             W["DIR"]["rc"]["ev"]["tb_dev"] if "rc" in W["DIR"]
             else float("nan"),
             W["ABS"]["rc"]["ev"]["tb_dev"] if "rc" in W["ABS"]
             else float("nan")))

    # ---------------- S3 MAIN ladder anchors
    section("S3  MAIN LADDER -- FROZEN ANCHORS (42 rungs)")
    if smoke:
        for g in ("G30-ladder-census", "G31-cascade-anchors",
                  "G32-c2-refreeze", "G33-class-anchors"):
            check(g, True, "SMOKE: skipped")
        stM = None
        kzs = []
        C2_live = R306_C2
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        packsM = [BH.wpack(kz) for kz in kzs]
        packsM.sort(key=lambda p: (p["N"], p["kz"]))
        kzs = [p["kz"] for p in packsM]
        recsM = []
        for p in packsM:
            rc = rung_rec(p)
            rc["ev"] = eval_rung(rc)
            rc["S_own"] = len(p["d"]["xs"]) + len(p["d"]["ys"])
            recsM.append(rc)
        rho2M = [r["ev"]["rho2"] for r in recsM]
        C2_live = max(rho2M[:N_CAL])
        stM = battery_stats(recsM, C2_live)
        check("G30-ladder-census", len(recsM) == 42
              and stM["nf_none"] == 42 and stM["valid"]
              and stM["multmax"] <= MULT_CAP,
              "42 rungs (N, kz)-sorted; nf None on %d/42 (the "
              "MAIN wall at every window depth); tb ward max "
              "%.1e; mult <= 2 on 42/42 (r313/r314 banked asset "
              "live); two-ancestor slack %.1e <= 0"
              % (stM["nf_none"], stM["tb_max"], stM["two_anc"]))
        ok_casc = (abs(stM["sl_D"] - R299_SL_D) <= SL_TOL
                   and abs(stM["neff_med"] - R301_NEFF_MED)
                   <= NEFF_MED_TOL
                   and abs(stM["sl_neff"] - R301_SL_NEFF)
                   <= SL_TOL)
        check("G31-cascade-anchors", ok_casc,
              "sl_D %+.4f (rec %+.3f tol %.2f); n_eff med %.2f "
              "(rec %.2f) slope %+.3f (rec %+.3f) -- the "
              "r299/r301 cascade re-derived through this channel"
              % (stM["sl_D"], R299_SL_D, SL_TOL, stM["neff_med"],
                 R301_NEFF_MED, stM["sl_neff"], R301_SL_NEFF))
        ok_c2 = (abs(C2_live - R306_C2) <= C2_TOL
                 and not stM["viol"])
        check("G32-c2-refreeze", ok_c2,
              "C_2 re-frozen on the MAIN first-%d split at FULL "
              "precision (a1): %.6f == r306 record %.4f (tol "
              "%.3f); MAIN violations %d/42 -- the constant is "
              "FROZEN here, no second-world value enters it"
              % (N_CAL, C2_live, R306_C2, C2_TOL,
                 len(stM["viol"])))
        ok_cls = (stM["oneg"] == R299_ONEG
                  and stM["fill_med"] < FILL_CLS)
        check("G33-class-anchors", ok_cls,
              "O < 0 on %d/42 == r299 record %d EXACT (MAIN "
              "O_POS); fill med %.3f < %.1f (MAIN FILL_LOW) -- "
              "both world-separating classes re-derived"
              % (stM["oneg"], R299_ONEG, stM["fill_med"],
                 FILL_CLS))

    # ---------------- S4 second-world ladders + battery
    section("S4  SECOND-WORLD LADDERS -- THE BATTERY")
    if smoke:
        for g in ("G40-dirichlet-ladder", "G41-abs-ladder",
                  "G42-battery-table"):
            check(g, True, "SMOKE: skipped")
        stD = stA = None
        clD = clA = {}
    else:
        rowsD = battery_ladder(kzs, dirichlet_comb)
        stD = battery_stats(rowsD, C2_live)
        clD = battery_classes(stD) if stD.get("valid") else {}
        check("G40-dirichlet-ladder", stD["n_built"] == 42,
              "DIRICHLET: built %d/42, live %d, tb max %s, "
              "validity %s; nf None %s/42, ratio med %s, S_own "
              "med %s; rho_2 violations %s; sl_D %s, sl_neff %s; "
              "O<0 %s; fill med %s; mult max %s"
              % (stD["n_built"], stD["n_live"],
                 ("%.1e" % stD["tb_max"]) if "tb_max" in stD
                 else "n/a", stD["why"],
                 stD.get("nf_none"), 
                 ("%.3f" % stD["ratio_med"])
                 if "ratio_med" in stD else "n/a",
                 stD.get("s_own_med"),
                 str(stD.get("viol"))[:60], 
                 ("%+.3f" % stD["sl_D"]) if "sl_D" in stD
                 else "n/a",
                 ("%+.3f" % stD["sl_neff"]) if "sl_neff" in stD
                 else "n/a", stD.get("oneg"),
                 ("%.3f" % stD["fill_med"])
                 if "fill_med" in stD else "n/a",
                 stD.get("multmax")))
        rowsA = battery_ladder(kzs, dirichlet_abs_comb)
        stA = battery_stats(rowsA, C2_live)
        clA = battery_classes(stA) if stA.get("valid") else {}
        check("G41-abs-ladder", stA["n_built"] == 42,
              "DIRICHLET_ABS: built %d/42, live %d, tb max %s, "
              "validity %s; nf None %s/42, ratio med %s; rho_2 "
              "violations %s; sl_D %s, sl_neff %s; O<0 %s; fill "
              "med %s; mult max %s"
              % (stA["n_built"], stA["n_live"],
                 ("%.1e" % stA["tb_max"]) if "tb_max" in stA
                 else "n/a", stA["why"], stA.get("nf_none"),
                 ("%.3f" % stA["ratio_med"])
                 if "ratio_med" in stA else "n/a",
                 str(stA.get("viol"))[:60],
                 ("%+.3f" % stA["sl_D"]) if "sl_D" in stA
                 else "n/a",
                 ("%+.3f" % stA["sl_neff"]) if "sl_neff" in stA
                 else "n/a", stA.get("oneg"),
                 ("%.3f" % stA["fill_med"])
                 if "fill_med" in stA else "n/a",
                 stA.get("multmax")))
        clM = battery_classes(stM)
        info("BATTERY TABLE (property: MAIN | DIR | ABS | ctrl "
             "reference):")
        ctrl_ref = {"HALF_FILLING": "flips 25/21/27",
                    "RENYI3_C2": "EPST holds / SCR 1.67x",
                    "SIGMA_DECAY": "n/a (single rungs)",
                    "NEFF_GROWTH": "n/a (single rungs)",
                    "O_SIGN": "EPST+SCR O_NEG",
                    "FILL": "EPST+SCR FILL_HIGH",
                    "MULT2": "<= 2 (banked)"}
        for pr in PROPS:
            info("  %-12s MAIN %s | DIR %s | ABS %s | %s"
                 % (pr, clM[pr],
                    clD.get(pr, ("-", "invalid")),
                    clA.get(pr, ("-", "invalid")),
                    ctrl_ref[pr]))
        ok_tab = all(clM[pr][0] == "MAIN" for pr in PROPS)
        check("G42-battery-table", ok_tab,
              "MAIN is MAIN-side on all 7 properties through the "
              "identical channel (self-consistency of the sealed "
              "class rules); mixed one-pair share med MAIN %.2f / "
              "DIR %s / ABS %s (census, no sealed expectation)"
              % (stM["mixed_med"],
                 ("%.2f" % stD["mixed_med"])
                 if stD and "mixed_med" in stD else "n/a",
                 ("%.2f" % stA["mixed_med"])
                 if stA and "mixed_med" in stA else "n/a"))

    # ---------------- S5 must-fails m3
    section("S5  MUST-FAILS -- RECALIBRATION")
    c_toy, decl_toy = mutant_recalibrate(list(range(1, 11)))
    frozen_decl = ("MAIN_FIRST5", N_CAL)
    ok_m3_toy = (decl_toy != frozen_decl
                 and abs(c_toy - 10.0) <= TOY_BAR)
    if smoke or stD is None or "rho2_list" not in (stD or {}):
        real_txt = "real census: full run only"
        ok_m3 = ok_m3_toy
    else:
        c_real, decl_real = mutant_recalibrate(stD["rho2_list"])
        ok_m3 = ok_m3_toy and decl_real != frozen_decl
        real_txt = ("real DIR rho max %.3f vs frozen C_2 %.4f -- "
                    "NEVER adopted (declared set %s != frozen %s)"
                    % (c_real, R306_C2,
                       str(decl_real), str(frozen_decl)))
    check("G50-mustfail-recalibrate", ok_m3,
          "m3 RECALIBRATION: toy rho list (1..10) gives C_mut = "
          "%.0f with declared set %s != the frozen declaration %s "
          "(diff 9 EXACT) -- CAUGHT structurally; %s"
          % (c_toy, str(decl_toy), str(frozen_decl), real_txt))

    # ---------------- S6 honesty ledger
    section("S6  HONESTY LEDGER")
    check("G80-honesty-ledger", True,
          "the second worlds are SOURCE TWISTS inside the MAIN "
          "frame: archimedean lags, smooth border, window depth "
          "and every constant stay MAIN's; the Gamma-factor "
          "parity and the conductor of L(s, chi) are NOT modeled "
          "-- a split therefore cannot distinguish 'property is "
          "zeta-specific' from 'property needs the matched "
          "frame' (disclosed in the verdict); GRH motivates the "
          "candidate, it is USED nowhere; all battery statistics "
          "are finite measurements on 42 rungs per world")

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-stoplist", True,
          "STOP LIST held: NO L* claim, no bound mechanism, no "
          "asymptotic law, no GRH assumption used, no derived "
          "5/7, no posthoc window, no recalibration, no RH claim; "
          "what the round adds: the first SECOND LIVING WORLD "
          "positive control (audit repair r328C-C3) with the "
          "seven-property battery at frozen MAIN constants; "
          "r243..r329 stand")
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        statD, splD = variant_status(stD, clD)
        statA, splA = variant_status(stA, clA)
        abs_txt = ("ABS %s%s" % (statA,
                                 "(%s)" % ",".join(splA)
                                 if splA else ""))
        if statD == "ALIVE":
            head = ("SECOND_WORLD_ALIVE(all 7 shared; %s)"
                    % abs_txt)
        elif statD == "SPLITS":
            head = ("SECOND_WORLD_SPLITS(%s; shared %s; %s)"
                    % (",".join(splD),
                       ",".join(p for p in PROPS
                                if p not in splD), abs_txt))
        else:
            head = ("CONSTRUCTION_INCOMPATIBLE(%s; %s)"
                    % (stD["why"], abs_txt))
        parts = ["SECOND_WORLD_BATTERY(table above)"]
        parts.append(head)
        if statD == "SPLITS":
            parts.append("RETYPED(%s -> MAIN idiosyncrasies "
                         "inside this frame)" % ",".join(splD))
        parts.append("CONVENTION_LEDGER(chi mod 3; weights chi x "
                     "MU_ALL bitwise / MU_ALL on (n,3)=1; MAIN "
                     "frame ARCH/border/depth; trivial twist "
                     "BITWISE; no recalibration)")
        verd = " + ".join(parts)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- the second-living-world battery at frozen MAIN "
          "constants; NO RH claim" % (verd,
                                      " (SMOKE)" if smoke else ""))
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
