#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v905 -- PRIME.PORT.BFLOOR.PG.01 + PRIME.PORT.BFLOOR.PG.IVAL.01: THE CERTIFIED IDEAL-OBJECT SURFACE FLOOR OF THE B-HALF -- the B-half of the wall end-form closes as a certified surface theorem over the IDEAL source objects on the entire reachable 39-step ladder: B >= (1/2) P_G + c_dom I and P_G >= c_G I, hence B >= c_B I, every inequality decided in the v897 exact-rational certificate class, ONE module from two probes (21/21 + 25/25 checks, zero fails, verdicts BFLOORPG-MEASURED (EXC-ANATOMY(2: MARGINAL, STRUCTURAL) / CANONICAL-PG(V4, s=0.50, float-dom 39/39) / CG-CERTIFIED(39/39, min=0.4614) / DOM-CERTIFIED(39/39) / ASSEMBLY-CERTIFIED(39/39, min c_B=0.5914) / CERTIFIED-SURFACE-FLOOR-ACHIEVED) + BFLOORPGIVAL-MEASURED (CG-IVAL(39/39, min c_G=0.4614) / DOM-IVAL(39/39) / ASSEMBLY-IVAL(39/39, min c_B=0.5523, min survival 0.56549978, min r_pert=c_B/7=0.0789) / LADDER(dps 40/hi: 6, dps 40/std: 33; certified 39, refused-width 0, failed 0, skipped 0) / IVAL-SURFACE-FLOOR-ACHIEVED(s = 1/2)); discovery probes bfloor_pg_dominance_probe.py (round 62) and pg_chain_interval_rollout_probe.py (SPEC v3, round 63), 2026-08-10/11, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~135 s).  (1) THE FLOAT-LEVEL CHAIN (bfloor_pg_dominance, 21/21; the round-62 crack): after three dead certificate rounds (raw Gershgorin -88, Christoffel congruences -140..-154, moving-node congruence unbuildable) the missing piece was not a new congruence but the CERTIFICATE CLASS -- exact-rational LDL (Fraction arithmetic on the float64 entries, which ARE exact rationals; the v897 class) decides the chain on ALL 39/39 reachable steps: P_G (the source-only CD-Gram co-block of the wall's own positive chain, the round-61 crack) is PD with c_G min/med 0.4614/0.7748 AND -- the honest surprise -- Gershgorin-POSITIVE on P_G itself (min +0.33, 39/39): unlike B, P_G is classically certifiable, the single non-classical link is the dominance decision B - (1/2)P_G >= c_dom I; the frozen variant scan selects V4 = s = 1/2 canonically (39/39, min lam_min(B - P_G/2) = +0.179; the degree-8 kernel variant V1 is UNBUILDABLE 0/39); assembly c_B = c_G/2 + c_dom, min/med 0.5914/5.92, efficiency c_B/lam_min(B) min 0.871 (the chain pays <= 13 percent for its structure), entry-robustness radius min c_B/7 = 0.0845, tau-screen PASS (slope -0.256, R^2 0.123) = an O(1) tau-decorrelated floor; the 2 float-dominance exceptions live in P_G's top direction, not in the row-0 mass (kz 59/h 363 MARGINAL -0.08 x lam_min(B), kz 44/h 436 STRUCTURAL -0.47 x), both typed in-probe.  (2) THE INTERVAL ROLLOUT TO THE IDEAL OBJECTS (pg_chain_interval_rollout SPEC v3, 25/25; the round-63 deep closure): the same chain now holds over RIGOROUS OUTWARD ENCLOSURES of the ideal source objects -- the full pipeline (lags -> FFT density -> Lanczos chain -> frame -> Schur complements -> B) carried in interval arithmetic, fail-closed at every step (an interval too wide to decide REFUSES rather than passes); the v2 cure is a HIGH-ACCURACY LA TIER realized inside float64 by error-free transformations (Ogita-Rump TwoSum block accumulation, BLK_HI = 4; rigorous rounding radius gam(4)|A||B| + 2(nb+2)^2 u^2 |A||B| + 2u|mid| instead of gam(k) with k ~ 880..1760 -- factor ~150..300 on the LA noise floor, measured ~100x on max radS), which certifies exactly the 6 v2 width-refusals (h 534/679/839/841/859/878, c_B = 0.9488..13.4644, survival >= 0.9639); ladder (dps 40, std) 33 steps + (dps 40, hi) 6 steps, 0 refused / 0 failed / 0 skipped; IVAL-SURFACE-FLOOR-ACHIEVED: min c_B = 0.5523 on 39/39 ideal-object steps (93.4 percent of the float reference 0.5914, min step kz 44/h 436 unchanged), min survival 0.56549978, min perturbation radius r_pert = c_B/7 = 0.0789, tau-screen PASS (slope -0.226); all 33 v2-certified steps re-resolve on the byte-identical (40, std) path with IDENTICAL constants to every printed digit, and the float benchmark 39/39 min c_B^f64 = 0.5914 is reproduced exactly.  (3) HONEST SCOPE (typed everywhere): the theorem is a SURFACE statement -- certified on the reachable 39-step surface over the ideal source objects with the frozen-frame convention (Q, tau_1, s = 1/2 exact-rational constants of the statement); the h-uniformity beyond h ~ 900 is OPEN, every h beyond the surface is OPEN, and the n > q half of the end-form is UNTOUCHED and RH-hard.  CONTROLS: the identical exact machine REFUSES the smooth co-block B0 (35/35 float; interval census 0/35 certified, CERT-NEG 31, smooth refusals SMOOTH), Epstein (neg(A) 55) + scramble (37) fire, scramble-core dead -> disclosed skip; anti-circularity: P_G/variants/s source-only, float eigenvalues only as measurements/hints (the final exact PD verdict is re-decided at the returned lo); AST firewalls clean.  NO RH claim; no marker moves.

PROVENANCE: discovery probes bfloor_pg_dominance_probe.py (21/21,
BFLOORPG-MEASURED, SPEC v1 frozen pre-run, round 62 note CXLIV,
Spec-SHA ef61bc10..., 2026-08-10) and
pg_chain_interval_rollout_probe.py (25/25, BFLOORPGIVAL-MEASURED,
SPEC v3 -- the v3 amendment lives in the same probe file with the
v1/v2 census on protocol in its docstring, fail-first preserved,
no bar/band/enum moved -- round 63 note CLIII, Spec-SHA
eb68b6ed..., 2026-08-11), re-run identically at promotion.
ROUND-31 EMBEDDING CONVENTION: frozen sources embedded BYTE-EXACT,
executed verbatim in isolated namespaces; printed spec SHAs
reproduce; byte-equality ward vs experiments/tfpt-discovery/ inside
the pattern gates.  Both probes consume the READ-ONLY deployed core
v563_paper2_readouts.py and reproduce the v901 tangent-Schur
ledger (min lam_min(B) 0.679, gap 0.052/0.888, raw certificate
desaster -88.2) as wards.

FIREWALL: no zeros, no prime-table oracles (AST firewalls inside
the probes); the certificate class is v897 exact-rational LDL plus
rigorous outward interval enclosures -- fail-closed, refusals are
first-class; the surface is 39 steps, NOT all h; the n > q half is
untouched; NO RH claim.  Python-only per GATE.WOLFRAM.02.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source bfloor_pg_dominance_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bfloor_pg_dominance_probe -- PRIME.PORT.BFLOOR.PG.01
(EXPLORATION ONLY, experiments/; round 62, theorem-engineering on
the RH-side wall: the CRACK attempt on the B-half of the endform.
The round-61 finding B >= P_G (PSD order) on 37/39 steps -- P_G the
CD-Gram co-block of the rung's OWN positive chain, a source-only
object -- is turned into a per-step CERTIFIED chain
    B >= s P_G + c_dom I  and  P_G >= c_G I
    ==> B >= (s c_G + c_dom) I =: c_B I,
with EVERY inequality certified by EXACT-RATIONAL LDL (fraction
arithmetic on the float64 entries, which are exact rationals -- the
v897 certificate class: a sqrt-free Cholesky/LDL decision run in
exact arithmetic, no rounding anywhere in the decision path).
2026-08-10.)

THE OBJECT (rounds 58-61 verbatim).  P2/P3 reduced the wall update
to (B_h PD) AND (n_h > q_h) in the frozen Householder frame of the
core Schur complement S (8 core folds CORE_J, soft direction of S_1
rotated out; B = 7x7 co-block of Mt = Q^T (S_2/tau_1) Q).  Measured
lam_min(B) = 0.679 O(1) ladder-wide (port_bfloor_uniformity, tau-
screened).  THREE failed certification programs: raw classical
bounds (best -88, cert/floor -130), four Christoffel diagonal
congruences (cert/floor -140..-154, failure seated in row 0 of the
rotated co-block), the wandering-node congruence (T2/T3 unbuildable
in float, cond(Ec) ~ 6e17; negidx(B0) in {1,2,3} off-row-0).  THE
CRACK (bfloor_node_congruence F2b): P_G = co-block of Q^T G_core Q,
G_core[i,j] = sqrt(v_i v_j) sum_{k<h} p_k(y_i) p_k(y_j) (CD-kernel
Gram of the POSITIVE chain at the 8 core nodes) is PD on 39/39 and
B - P_G is PSD on 37/39 (negidx(K2) hist [37, 2], 1+lam_min(K2)
med +6.13) -- MEASURED, not certified; the classical G-battery on
the preconditioned Btil2 stayed dead (med -1.3e+03).  What was
missing is a certificate CLASS that decides a PSD question exactly
instead of bounding it by row sums.  That class exists on this
surface: the matrices are 7x7 with exact-rational (float64)
entries, so Sylvester/LDL in Fraction arithmetic is a RIGOROUS
decision procedure (v897 tier-1 pattern: exact integer/rational
pivots, no working-precision rounding in the decision path).

DECLARED CERTIFICATE CLASS + THE HONEST CAVEAT (frozen, first):
every certificate below is an exact-rational LDL statement about
the float64-COMPUTED matrices B_step and P_G_step: their entries
are exact rationals and the LDL decision is exact, so
"B >= c_B I" is a THEOREM about the computed surface objects, with
an explicit entrywise robustness radius r_pert = margin/7 (a
symmetric perturbation with max |dE_ij| <= r_pert cannot cross the
certified floor, |lam_min shift| <= ||dE||_2 <= 7 max|dE_ij|).
What is NOT enclosed here: the float pipeline that PRODUCES the
entries (FFT density, Lanczos chain, eigh frame, Schur solves) is
not interval arithmetic -- promoting the statement from the
computed matrices to the ideal real-arithmetic objects needs the
v897-style interval rollout of THIS pipeline (named open step).
The n > q half of the endform and every h beyond the 39-step
reachable surface stay open regardless.  NO RH claim.

FROZEN PROTOCOL (pipeline verbatim from
bfloor_node_congruence_probe = v900 chain; ONE Gram per rung;
window memoization):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2 >=
     30 full-core rungs; W3a truth all-PSD (A, R, S); W3b >= 20
     consecutive full-core steps; W4 REPRODUCTION P2/P3 ledger:
     min lam_min(B) == 0.679 (rtol 2e-2), gap min/med ==
     0.052/0.888 (rtol 5e-2), raw-B certified disaster (best bound
     < 0 on every step); W5 REPRODUCTION of THE CRACK: P_G PD on
     every step (float, PG_TOL) and float dominance
     negidx(B - P_G) = 0 on >= DOM_REPRO_MIN steps (round-61
     measured 37/39); W6 MACHINE WARD: the exact-rational LDL
     accepts a known PD matrix and refuses a known indefinite one.

 E1  THE 2 EXCEPTIONS + THE VARIANT SCAN (measured, typed):
     anatomy of every step with lam_min(B - P_G) < 0: (kz, h,
     alpha), lam_min(B - P_G), ratio to lam_min(B), row-0 share of
     the failing eigenvector, overlap with P_G's top eigenvector.
     TYPED per exception: MARGINAL iff |lam_min(B - P_G)| <=
     MARG_FRAC x lam_min(B), else STRUCTURAL.  Then the FROZEN
     source-only variant order (scan measured in float; NOTHING
     retuned after the scan):
       V0 = P_G (deployed: r2's own chain, CD degree < h, s = 1);
       V1 = P_G8 (CD degree < 8 -- the core-dimension kernel;
            disclosed risk: the 8-node/8-poly evaluation matrix
            was float rank-deficient in round 61, may not be PD);
       V2 = P_G(r1) (rung r1's chain evaluated at r2's core
            nodes, degree < h_1, s = 1);
       V3/V4/V5 = s P_G with s = 0.75 / 0.50 / 0.25.
     CANONICAL RULE (frozen a priori): the canonical pair
     (variant, s) is the FIRST in the order V0..V5 with float
     dominance on ALL steps; if none, the first among those with
     the maximal dominance count.  The scan is anatomy, not
     tuning: the assembly (E3) runs on the canonical pair
     regardless, and steps that fail are reported with seat/size.

 E2  THE CERTIFIED FLOOR ON P_G (canonical variant's P_G; per
     step): (i) CLASSICAL ROUTES, honest: the raw G-battery
     (Gershgorin / scaled / Cassini) on P_G; the Christoffel
     diagonal min_i v_i K_h(y_i, y_i); the node-separation
     constant h_sep = min_{i<j} |th_i - th_j| x h / (2 pi) (the
     Marcinkiewicz-Zygmund regime needs separation >> 1/h; the
     core folds sit at ~ 2/h -- measured, not claimed); the
     op-basis anatomy: off-diagonal mass of G_core after
     diagonal scaling (route (ii): in its own op basis the Gram
     is the moment matrix of the 8-node measure -- banded ONLY if
     the CD kernel decays between core folds; measured).  (ii)
     THE WORKHORSE: exact-rational LDL bisection for the largest
     certified c_G with P_G - c_G I PD (BIS_ITERS dyadic
     bisection steps on [0, min diag]; certificate = the PD
     decision at the final lo, re-run exactly).  Report certified
     c_G vs float lam_min(P_G) (efficiency) and vs the needed
     scale (s c_G vs float lam_min(B)).

 E3  THE ASSEMBLY (per step, canonical (variant, s)): certify
     c_dom = largest c with B - s P_G - c I PD by exact LDL
     bisection on [lo, min diag], lo = -s c_G (1 - 2^-20): PD at
     lo is REQUIRED for the chain to close (c_B = s c_G + c_dom >
     0); if PD fails at lo the step FAILS assembly (float
     lam_min(B - s P_G) and the deficit are printed as
     seat/size).  Headline counts: dominance-at-zero certified
     (exact PD of B - s P_G), assembly-certified c_B > 0, min/med
     c_B, c_B vs float lam_min(B) ratio (min/med), entrywise
     robustness radius min r_pert = c_B/7 (from the assembled
     floor: a perturbation argument needs the weaker of the two
     legs; r_pert reported per leg and assembled).  BENCHMARK
     (disclosed comparison, same certificate class): the direct
     exact-LDL floor c_dir on B itself -- the chain's value over
     the benchmark is STRUCTURE (a positive-measure object
     carries the floor), not size; both printed.  TAU-SCREEN
     (mandatory): OLS slope of log c_B vs log tau on the
     positive subset (bands PASS |s| <= 0.30 / RELOC >= 0.70 /
     AMBIG); c_B is expected O(1) tau-decorrelated like the
     measured floor.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) =
     0 everywhere; C1 smooth world neg(A) > 0 on >= 1 rung; C2
     Epstein x^2+5y^2 comb + scramble (seed 1) at kz 9 fire
     (neg(A) > 0 or frame death); C3 THE REFUSAL WARD: the exact
     LDL machine REFUSES the smooth world -- PD(B0) False on >=
     REFUSE_MIN of the usable steps (B0 = smooth co-block in the
     SAME truth frame; round-59/61 constraint B0 NOT PD); C4 the
     scramble core, where it exists, must break dominance or the
     floor (float lam_min(B_scr - P_G_scr) < 0 or B_scr not PD);
     disclosed skip if the scramble core dies (the refusal ward
     C3 carries the cannot-fake content).

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
ward / control failures (W4-W6, C0-C4) -> WARD-BROKEN.  All E1-E3
typed outcomes are measurements/certificates, never kills.

VERDICT (frozen enum): BFLOORPG-MEASURED with typed sublabels
EXC-ANATOMY(n_exc, MARGINAL/STRUCTURAL), CANONICAL-PG(Vk, s),
DOM-CERTIFIED(n/N), CG-CERTIFIED(min c_G),
ASSEMBLY-CERTIFIED(n/N, min c_B) and the headline
CERTIFIED-SURFACE-FLOOR-ACHIEVED(min c_B) [iff assembly n = N] /
CERTIFIED-SURFACE-FLOOR-PARTIAL(n/N) /
CERTIFIED-SURFACE-FLOOR-FAILED; else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2); PG_TOL
= 1e-12; DOM_REPRO_MIN = 35 (expected 37); MARG_FRAC = 0.25;
S_LIST = (("V0", "r2", None, 1.0), ("V1", "r2", 8, 1.0),
("V2", "r1", None, 1.0), ("V3", "r2", None, 0.75),
("V4", "r2", None, 0.50), ("V5", "r2", None, 0.25)) (variant,
chain, CD degree cap, s); BIS_ITERS = 40; REFUSE_MIN = 30;
SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; CTRL_KZ = 9; scramble seed
1.  Runtime cap declared: 20 min (exact-rational part).

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign, no spectral data of the TARGET B in any CONSTRUCTION
-- P_G, the variants and s are source-only (positive chain, r1
chain, frozen constants); float eigensolves of B and B - P_G
appear ONLY as measured floors/hints next to the certificates
(the bisection hint cannot affect a certificate's validity: the
final exact PD decision is re-run at the returned lo).  The
exact-rational LDL on B - s P_G and on B (benchmark) is the
DECLARED v897 certificate class, mandated for this probe; it is a
decision procedure, not a fit.

NO-GO COMPLIANCE (frozen): the classical G-battery on RAW B
enters ONLY as the W4 reproduction; no rank-1 approximation of
the core update; no plain Herglotz certificate; no fit where an
identity is claimed; the round-61 no-target-factorization rule is
AMENDED for this probe by explicit mandate: exact-rational LDL is
allowed as a CERTIFICATE (not as a construction) -- declared, not
silent.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script (21/21 with the identical bars; NO bar, band,
count, rule or enum was moved after it) measured: pipeline +
P2/P3 reproduction green (min lam_min(B) 0.679, gap
0.0520/0.8875, raw disaster best -88.2); THE CRACK REPRODUCED:
P_G PD 39/39, float dominance 37/39.  E1: the 2 exceptions are
ONE MARGINAL + ONE STRUCTURAL by the frozen typing (kz 59/h 363:
lam_min(B - P_G) = -7.3e-02 = -0.08 x lam_min(B), MARGINAL; kz
44/h 436: -3.2e-01 = -0.47 x lam_min(B), STRUCTURAL), both
negidx 1, and the failing eigenvector is NOT row-0-seated (row-0
share 0.125/0.460) but is ALIGNED WITH P_G'S TOP EIGENVECTOR
(overlap 0.997/0.990): the exception mechanism is P_G's top
direction slightly EXCEEDING B there, not the round-58-60
coherent row-0 channel.  V1 (CD degree < 8) is UNUSABLE 0/39
(P_G8 not PD in float -- the disclosed round-61 node-clustering
risk fired); V2 (r1 chain) is WORSE (30/39); V3 (s = 0.75)
reaches 38/39; V4 (s = 0.50) reaches 39/39 with min
lam_min(B - s P_G) = +0.179 -> the frozen rule selects V4.  E2
on P_G (V4 uses the deployed P_G): the classical G-battery is
POSITIVE on P_G itself -- best cert min/med +0.33/+0.76,
certified > 0 on 39/39 (an honest SURPRISE: P_G, unlike B, is
classically certifiable; h_sep med 0.50, off/diag mass med
0.20); the exact-LDL bisection certifies c_G on 39/39 (min/med
0.4614/0.7748, efficiency 1.000000).  E3: dominance at zero
exact-certified 39/39, assembly c_B > 0 on 39/39 with min c_B =
0.5914, med 5.92; c_B / lam_min(B) min/med 0.871/0.979;
benchmark c_dir min 0.679 (chain/benchmark min ratio 0.871 --
the chain pays <= 13% for its structure); robustness radius min
c_B/7 = 0.0845; tau-screen PASS(-0.256, R2 0.123) -- O(1),
tau-decorrelated.  Controls: smooth neg(A) > 0 on 42/42, C3
refusal 35/35, Epstein neg(A) = 55 fires, scramble neg(A) = 37
fires, scramble core dead -> C4 disclosed skip (C3 carries the
content).  Runtime 5.5 s (cap holds).  Fail-first preserved:
nothing was weakened; the canonical rule, exception typing and
all bars are exactly as frozen above.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as P2
SPEC (ii); (iii) chains via keep_chain; P_G variants via
eval_chain on the declared chain at r2's core nodes with the
declared degree cap; (iv) exact LDL = full symmetric Gaussian
elimination in Fraction arithmetic, PD iff all n pivots > 0
(Sylvester); shifts entered as exact dyadic Fractions of floats;
(v) bisection lo certified by a final exact re-decision; (vi)
negidx = count of eigenvalues < 0 (float sign, no tolerance);
(vii) OLS population statistics as v900; screens read positive
subsets.

NO RH claim: a certified c_B > 0 on all 39 steps is a SURFACE
theorem about the computed step matrices of the deployed ladder
(with the float-entry caveat above); it does NOT prove
B-uniformity in h, the n > q half, wall positivity beyond the
surface, or any tail statement.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
P_G machinery verbatim from bfloor_node_congruence_probe.py
(round 61) = v900 chain; certificate class pattern from
v897_certified_interval_ladder (declared input); positive
completed family from case_edge_christoffel_probe (declared
input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/bfloor_pg_dominance_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_LADDER_MAX = 900
N_RUNGS_EXP = 42
MIN_CORE_RUNGS = 30
MIN_STEPS = 20
MINB_REF = 0.679
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
PG_TOL = 1e-12
DOM_REPRO_MIN = 35
MARG_FRAC = 0.25
S_LIST = (("V0", "r2", None, 1.0),
          ("V1", "r2", 8, 1.0),
          ("V2", "r1", None, 1.0),
          ("V3", "r2", None, 0.75),
          ("V4", "r2", None, 0.50),
          ("V5", "r2", None, 0.25))
BIS_ITERS = 40
REFUSE_MIN = 30
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# --------------- pipeline, verbatim (bfloor_node_congruence_probe)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def ladder_zones():
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


def smooth_masses(uu):
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None,
                 keep_chain=False):
    """v900 verbatim wall + fixed-core split."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    A = np.eye(n) - G
    evA = np.linalg.eigvalsh(A)
    out = dict(kz=kz, h=h, n=n, alpha=float(alpha), M=M, D=D, L=L)
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    if keep_chain:
        out["chain"] = (al, be, m0)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["lamR"] = float(evR[0])
    out["negR"] = int(np.sum(evR < 0.0))
    Z = np.linalg.solve(R, Xc.T)
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["negS"] = int(np.sum(evS < 0.0))
    if keep_chain:
        out["y_core"] = np.array([ys[idx[j]] for j in CORE_J])
        out["v_core"] = np.array([vs[idx[j]] for j in CORE_J])
    return out


def householder_frame(v):
    n = len(v)
    v = v / float(np.linalg.norm(v))
    e1 = np.zeros(n)
    e1[0] = 1.0
    u = e1 - v
    nu = float(np.linalg.norm(u))
    if nu < 1e-14:
        return np.eye(n)
    u = u / nu
    Q = np.eye(n) - 2.0 * np.outer(u, u)
    if float(Q[:, 0] @ v) < 0:
        Q = -Q
    return Q


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


# ------------------------------ certified bounds (P3 verbatim)
def gersh_min(B):
    d = np.diag(B)
    r = np.sum(np.abs(B), axis=1) - np.abs(d)
    return float(np.min(d - r))


def gersh_scaled(B):
    d = np.diag(B)
    if float(np.min(d)) <= 0.0:
        return float("-inf")
    s = 1.0 / np.sqrt(d)
    C = B * np.outer(s, s)
    r = np.sum(np.abs(C), axis=1) - np.abs(np.diag(C))
    lamg = float(np.min(1.0 - r))
    return lamg * (float(np.min(d)) if lamg >= 0.0
                   else float(np.max(d)))


def cassini_scaled(B):
    d = np.diag(B)
    if float(np.min(d)) <= 0.0:
        return float("-inf")
    s = 1.0 / np.sqrt(d)
    C = B * np.outer(s, s)
    r = np.sum(np.abs(C), axis=1) - np.abs(np.diag(C))
    rr = np.sort(r)[::-1]
    lamc = 1.0 - math.sqrt(float(rr[0]) * float(rr[1]))
    return lamc * (float(np.min(d)) if lamc >= 0.0
                   else float(np.max(d)))


def best_cert(B):
    return max(gersh_min(B), gersh_scaled(B), cassini_scaled(B))


def screen(vals, taus):
    vals = np.asarray(vals, float)
    taus = np.asarray(taus, float)
    pos = vals > 0
    if int(np.sum(pos)) >= 3:
        _a, sl, r2 = ols_line(np.log(taus[pos]), np.log(vals[pos]))
    else:
        return "vacuous(pos=%d)" % int(np.sum(pos)), float("nan")
    lab = ("PASS" if abs(sl) <= SLOPE_PASS
           else "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
    return "%s(slope=%+.3f, R2=%.3f)" % (lab, sl, r2), sl


# ------------------------- the exact-rational LDL certificate class
def mat_fr(M):
    """float64 matrix -> exact-rational (Fraction) list of lists."""
    n = M.shape[0]
    return [[Fraction(float(M[i, j])) for j in range(n)]
            for i in range(n)]


def pd_exact(Afr, shift=Fraction(0)):
    """Exact Sylvester/LDL decision: is A - shift I PD?
    Full symmetric Gaussian elimination in Fraction arithmetic;
    PD iff all n pivots > 0.  Returns (ok, first_bad_pivot_idx)."""
    n = len(Afr)
    A = [[Afr[i][j] - (shift if i == j else 0) for j in range(n)]
         for i in range(n)]
    for k in range(n):
        p = A[k][k]
        if p <= 0:
            return False, k
        for i in range(k + 1, n):
            f = A[i][k] / p
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - f * A[k][j]
    return True, -1


def cert_floor_exact(Afr, lo, hi, iters=BIS_ITERS):
    """Largest certified c in [lo, hi] with A - c I PD (dyadic
    bisection; PD(c) is monotone decreasing in c).  Returns None
    if PD fails at lo; else the certified Fraction lo* (the PD
    decision at lo* is re-run exactly as the certificate)."""
    lo = Fraction(lo)
    hi = Fraction(hi)
    ok, _ = pd_exact(Afr, lo)
    if not ok:
        return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        ok, _ = pd_exact(Afr, mid)
        if ok:
            lo = mid
        else:
            hi = mid
    ok, _ = pd_exact(Afr, lo)
    assert ok
    return lo


def build_pg(w, which, degcap):
    """The source-only P_G co-block of one step (F2b verbatim,
    generalized to the declared chain and CD degree cap)."""
    r2 = w["r2"]
    src = r2 if which == "r2" else w["r1"]
    ch = src.get("chain")
    if ch is None:
        return None
    al, be, m0 = ch
    deg = src["h"] if degcap is None else min(degcap, src["h"])
    Pc = eval_chain(al, be, m0, r2["y_core"], deg)
    Gc = (np.sqrt(r2["v_core"])[:, None] * (Pc @ Pc.T)
          * np.sqrt(r2["v_core"])[None, :])
    Gc = 0.5 * (Gc + Gc.T)
    PG = (w["Q"].T @ Gc @ w["Q"])[1:, 1:]
    return 0.5 * (PG + PG.T)


def main():
    section("PRIME.PORT.BFLOOR.PG.01 -- B >= s P_G >= s c_G I: the "
            "exact-rational certified B-floor on the reachable "
            "surface (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Certificates are "
          "exact statements about the float64-computed step "
          "matrices (caveat block in spec).")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + P2/P3 + crack reproduction")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    sm_map = {}
    for kz in zones:
        r = gram_anatomy(kz, keep_chain=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
            truth.append(None)
            continue
        truth.append(r)
        rs = gram_anatomy(kz, world_fn=world_smooth,
                          keep_chain=True)
        if isinstance(rs, dict):
            sm_map[kz] = rs
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1c all tau finite",
          all(np.isfinite(r["tau"]) for r in truth), kill="K1")
    full = [r for r in truth if r["core_ok"]]
    check("W2 >= %d full-core rungs" % MIN_CORE_RUNGS,
          len(full) >= MIN_CORE_RUNGS,
          "%d full-core rungs" % len(full), kill="K1")
    ok_psd = all(r["negA"] == 0 and r["negR"] == 0
                 and r["negS"] == 0 for r in full)
    check("W3a WARD truth all-PSD (A, R, S)", ok_psd, kill="K1")
    steps = []
    for r1, r2 in zip(truth, truth[1:]):
        if not (r1.get("core_ok") and r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
        steps.append((r1, r2))
    check("W3b >= %d consecutive full-core steps" % MIN_STEPS,
          len(steps) >= MIN_STEPS, "%d steps" % len(steps),
          kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})
    rows = []
    for r1, r2 in steps:
        wS, VS = np.linalg.eigh(r1["S"])
        Q = householder_frame(VS[:, 0])
        Mt = Q.T @ (r2["S"] / r1["tau"]) @ Q
        Mt = 0.5 * (Mt + Mt.T)
        nsc = float(Mt[0, 0])
        b = Mt[1:, 0]
        B = Mt[1:, 1:]
        minB = float(np.linalg.eigvalsh(B)[0])
        gap = (nsc - float(b @ np.linalg.solve(B, b))
               if minB > 0 else float("nan"))
        rs2 = sm_map.get(r2["kz"])
        B0 = None
        if isinstance(rs2, dict) and "S" in rs2:
            M0 = Q.T @ (rs2["S"] / r1["tau"]) @ Q
            M0 = 0.5 * (M0 + M0.T)
            B0 = M0[1:, 1:]
        rows.append(dict(r1=r1, r2=r2, Q=Q, B=B, B0=B0, minB=minB,
                         gap=gap, tau=r1["tau"],
                         bestg=best_cert(B)))
    minB_all = float(np.min([w["minB"] for w in rows]))
    gaps = np.array([w["gap"] for w in rows])
    bests = np.array([w["bestg"] for w in rows])
    gmin, gmed = float(np.min(gaps)), float(np.median(gaps))
    ok_repro = (abs(minB_all / MINB_REF - 1.0) <= MINB_RTOL
                and abs(gmin / GAPMIN_REF - 1.0) <= GAP_RTOL
                and abs(gmed / GAPMED_REF - 1.0) <= GAP_RTOL
                and float(np.max(bests)) < 0.0)
    check("W4 REPRODUCTION P2/P3 ledger: min lam_min(B) %.4f == "
          "%.3f; gap min/med %.4f/%.4f == %.3f/%.3f; raw-B "
          "certified disaster (best max %+.1f < 0 on %d steps)"
          % (minB_all, MINB_REF, gmin, gmed, GAPMIN_REF,
             GAPMED_REF, float(np.max(bests)), len(rows)),
          ok_repro, kill="K2")
    # W5: the crack -- P_G PD + float dominance
    pg_ok = True
    n_dom0 = 0
    for w in rows:
        PG = build_pg(w, "r2", None)
        if PG is None:
            pg_ok = False
            continue
        evg = np.linalg.eigvalsh(PG)
        if float(evg[0]) <= PG_TOL:
            pg_ok = False
        w["PG0"] = PG
        Dm = 0.5 * ((w["B"] - PG) + (w["B"] - PG).T)
        evd = np.linalg.eigvalsh(Dm)
        w["lamD0"] = float(evd[0])
        w["negD0"] = int(np.sum(evd < 0.0))
        if w["negD0"] == 0:
            n_dom0 += 1
    check("W5 REPRODUCTION THE CRACK: P_G PD on every step; float "
          "dominance negidx(B - P_G) = 0 on %d/%d (>= %d; "
          "round-61: 37/39)" % (n_dom0, len(rows), DOM_REPRO_MIN),
          pg_ok and n_dom0 >= DOM_REPRO_MIN, kill="K2")
    ok_pd, _ = pd_exact(mat_fr(np.array([[2.0, 1.0], [1.0, 2.0]])))
    ok_ind, _ = pd_exact(mat_fr(np.array([[1.0, 2.0], [2.0, 1.0]])))
    check("W6 MACHINE WARD exact LDL: accepts PD, refuses "
          "indefinite", ok_pd and not ok_ind, kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- E1
    section("E1 -- the 2 exceptions + the frozen variant scan")
    exc = [w for w in rows if w["negD0"] > 0]
    exc_types = []
    for w in exc:
        Dm = 0.5 * ((w["B"] - w["PG0"]) + (w["B"] - w["PG0"]).T)
        evd, Ud = np.linalg.eigh(Dm)
        lam = float(evd[0])
        vfail = Ud[:, 0]
        row0 = float(vfail[0] ** 2)
        evp, Up = np.linalg.eigh(w["PG0"])
        ovl = float((vfail @ Up[:, -1]) ** 2)
        marginal = abs(lam) <= MARG_FRAC * w["minB"]
        t = "MARGINAL" if marginal else "STRUCTURAL"
        exc_types.append(t)
        print("    EXC kz %d h %d alpha %.2f: lam_min(B-P_G) "
              "%+.3e (= %+.2f x lam_min(B)); negidx %d; failing "
              "eigvec row-0 share %.3f; overlap with top(P_G) "
              "%.3f -> %s"
              % (w["r2"]["kz"], w["r2"]["h"], w["r2"]["alpha"],
                 lam, lam / w["minB"], w["negD0"], row0, ovl, t),
              flush=True)
    e1a = ("EXC-ANATOMY(%d exceptions: %s)"
           % (len(exc), ",".join(exc_types) if exc_types else "-"))
    check("E1.a typed: %s" % e1a, True)
    # frozen variant scan (float; measured)
    scan = {}
    for name, which, degcap, s in S_LIST:
        n_dom, lmin = 0, float("inf")
        usable = 0
        pgs = {}
        for i, w in enumerate(rows):
            PG = (w["PG0"] if (which, degcap) == ("r2", None)
                  else build_pg(w, which, degcap))
            if PG is None:
                continue
            evg = float(np.linalg.eigvalsh(PG)[0])
            if evg <= PG_TOL:
                continue
            usable += 1
            pgs[i] = PG
            Dm = w["B"] - s * PG
            Dm = 0.5 * (Dm + Dm.T)
            lam = float(np.linalg.eigvalsh(Dm)[0])
            lmin = min(lmin, lam)
            if lam >= 0.0:
                n_dom += 1
        scan[name] = dict(n_dom=n_dom, usable=usable, lmin=lmin,
                          s=s, which=which, degcap=degcap, pgs=pgs)
        print("    %s (chain=%s, deg=%s, s=%.2f): float dominance "
              "%d/%d usable (of %d steps); min lam_min(B - s P_G) "
              "%+.3e"
              % (name, which, str(degcap), s, n_dom, usable,
                 len(rows), lmin), flush=True)
    canon = None
    for name, _w, _d, _s in S_LIST:
        sc = scan[name]
        if sc["usable"] == len(rows) and sc["n_dom"] == len(rows):
            canon = name
            break
    if canon is None:
        best_n = max(sc["n_dom"] for sc in scan.values())
        for name, _w, _d, _s in S_LIST:
            if scan[name]["n_dom"] == best_n:
                canon = name
                break
    sc = scan[canon]
    e1b = ("CANONICAL-PG(%s, s=%.2f, float-dom %d/%d)"
           % (canon, sc["s"], sc["n_dom"], len(rows)))
    check("E1.b typed: %s (frozen first-in-order rule)" % e1b, True)

    # ----------------------------------------------------------- E2
    section("E2 -- the certified floor on P_G (canonical %s)"
            % canon)
    s_can = Fraction(sc["s"]).limit_denominator(4)
    cg_list, cg_float, taus = [], [], []
    bat, chr_d, hsep, offd = [], [], [], []
    ok_cg = True
    for i, w in enumerate(rows):
        PG = sc["pgs"].get(i)
        if PG is None:
            ok_cg = False
            continue
        w["PGc"] = PG
        # classical routes (measured/honest)
        bat.append(best_cert(PG))
        r2 = w["r2"]
        src = r2 if sc["which"] == "r2" else w["r1"]
        al, be, m0 = src["chain"]
        deg = (src["h"] if sc["degcap"] is None
               else min(sc["degcap"], src["h"]))
        Pc = eval_chain(al, be, m0, r2["y_core"], deg)
        Gc = (np.sqrt(r2["v_core"])[:, None] * (Pc @ Pc.T)
              * np.sqrt(r2["v_core"])[None, :])
        chr_d.append(float(np.min(np.diag(Gc))))
        th = np.arccos(np.clip(r2["y_core"], -1.0, 1.0))
        dth = np.abs(th[:, None] - th[None, :])
        np.fill_diagonal(dth, np.inf)
        hsep.append(float(np.min(dth)) * r2["h"] / (2.0 * math.pi))
        Dg = 1.0 / np.sqrt(np.diag(Gc))
        Cn = Gc * np.outer(Dg, Dg)
        offd.append(float((np.sum(np.abs(Cn)) - 8.0) / 8.0))
        # the workhorse: exact-rational bisection
        Afr = mat_fr(PG)
        hi = min(float(PG[k, k]) for k in range(7))
        cg = cert_floor_exact(Afr, Fraction(0), Fraction(hi))
        if cg is None or cg <= 0:
            # PD at 0 must hold (PG PD warded); cg == 0 possible
            # only if lam_min below dyadic resolution -- count as
            # uncertified
            ok_cg = False
            cg_list.append(None)
        else:
            cg_list.append(cg)
        cg_float.append(float(np.linalg.eigvalsh(PG)[0]))
        taus.append(w["tau"])
    n_cg = sum(1 for c in cg_list if c is not None)
    cgv = np.array([float(c) for c in cg_list if c is not None])
    print("    classical routes on P_G (honest): G-battery best "
          "cert min/med %+.2e/%+.2e (certified > 0 on %d/%d); "
          "Christoffel diag min med %.2e; node-separation h_sep "
          "med %.2f (MZ needs >> 1); off/diag mass med %.2f "
          "(banded iff << 1)"
          % (float(np.min(bat)), float(np.median(bat)),
             int(np.sum(np.array(bat) > 0)), len(bat),
             float(np.median(chr_d)), float(np.median(hsep)),
             float(np.median(offd))), flush=True)
    eff = cgv / np.array([f for c, f in zip(cg_list, cg_float)
                          if c is not None])
    print("    EXACT-LDL bisection: certified c_G > 0 on %d/%d; "
          "min/med c_G %.3e/%.3e; efficiency c_G/lam_min(P_G) "
          "min %.6f" % (n_cg, len(rows), float(np.min(cgv)),
                        float(np.median(cgv)), float(np.min(eff))),
          flush=True)
    e2 = "CG-CERTIFIED(%d/%d, min=%.3e)" % (n_cg, len(rows),
                                            float(np.min(cgv)))
    check("E2 typed: %s" % e2, True)

    # ----------------------------------------------------------- E3
    section("E3 -- the assembly: B >= s P_G + c_dom I >= c_B I "
            "(exact certificates per step)")
    n_dom_exact, n_asm = 0, 0
    cb_list, cb_ratio, cdir_list = [], [], []
    fail_seats = []
    for i, w in enumerate(rows):
        PG = w.get("PGc")
        cg = cg_list[i]
        if PG is None or cg is None:
            fail_seats.append((w, "no PG/c_G"))
            continue
        n = 7
        Bfr = mat_fr(w["B"])
        PGfr = mat_fr(PG)
        Dfr = [[Bfr[a][b] - s_can * PGfr[a][b] for b in range(n)]
               for a in range(n)]
        ok0, piv0 = pd_exact(Dfr)
        if ok0:
            n_dom_exact += 1
        lo = -s_can * cg * (Fraction(2 ** 20 - 1, 2 ** 20))
        hi = min(Dfr[k][k] for k in range(n))
        cdom = cert_floor_exact(Dfr, lo, hi)
        if cdom is None:
            lamD = float(np.linalg.eigvalsh(
                0.5 * ((w["B"] - sc["s"] * PG)
                       + (w["B"] - sc["s"] * PG).T))[0])
            deficit = float(s_can * cg) + lamD
            fail_seats.append((w, "PD fails at lo: float "
                               "lam_min(B - s P_G) %+.3e, deficit "
                               "s c_G + lam = %+.3e" % (lamD,
                                                        deficit)))
            continue
        cb = s_can * cg + cdom
        if cb > 0:
            n_asm += 1
        cb_list.append((w, float(cb), ok0))
        cb_ratio.append(float(cb) / w["minB"])
        # benchmark: direct exact floor on B
        cdir = cert_floor_exact(Bfr, Fraction(0),
                                min(Bfr[k][k] for k in range(n)))
        cdir_list.append(float(cdir) if cdir is not None else
                         float("nan"))
    cbv = np.array([c for _w, c, _o in cb_list])
    cdirv = np.array(cdir_list)
    scr_lab, _sl = screen([c for _w, c, _o in cb_list],
                          [w["tau"] for w, _c, _o in cb_list])
    print("    dominance at zero EXACT-certified on %d/%d; "
          "assembly c_B > 0 certified on %d/%d; min/med c_B "
          "%.4f/%.4f; c_B/lam_min(B) min/med %.4f/%.4f; benchmark "
          "direct c_dir min %.4f (chain vs benchmark min ratio "
          "%.4f); entrywise robustness radius min c_B/7 = %.4f; "
          "tau-screen %s"
          % (n_dom_exact, len(rows), n_asm, len(rows),
             float(np.min(cbv)) if len(cbv) else float("nan"),
             float(np.median(cbv)) if len(cbv) else float("nan"),
             float(np.min(cb_ratio)) if cb_ratio else float("nan"),
             float(np.median(cb_ratio)) if cb_ratio
             else float("nan"),
             float(np.nanmin(cdirv)) if len(cdirv) else
             float("nan"),
             (float(np.min(cbv / cdirv[:len(cbv)]))
              if len(cbv) and len(cdirv) else float("nan")),
             float(np.min(cbv)) / 7.0 if len(cbv) else
             float("nan"), scr_lab), flush=True)
    for w, seat in fail_seats:
        print("    ASSEMBLY-FAIL kz %d h %d: %s"
              % (w["r2"]["kz"], w["r2"]["h"], seat), flush=True)
    e3a = "DOM-CERTIFIED(%d/%d)" % (n_dom_exact, len(rows))
    e3b = ("ASSEMBLY-CERTIFIED(%d/%d, min c_B=%.4f)"
           % (n_asm, len(rows),
              float(np.min(cbv)) if len(cbv) else float("nan")))
    check("E3.a typed: %s" % e3a, True)
    check("E3.b typed: %s; screen %s" % (e3b, scr_lab), True)
    if n_asm == len(rows):
        headline = ("CERTIFIED-SURFACE-FLOOR-ACHIEVED(min c_B = "
                    "%.4f on %d/%d steps, canonical %s s=%.2f)"
                    % (float(np.min(cbv)), n_asm, len(rows),
                       canon, sc["s"]))
    elif n_asm > 0:
        headline = ("CERTIFIED-SURFACE-FLOOR-PARTIAL(%d/%d, min "
                    "c_B=%.4f)" % (n_asm, len(rows),
                                   float(np.min(cbv))))
    else:
        headline = "CERTIFIED-SURFACE-FLOOR-FAILED"
    check("E3.h typed headline: %s" % headline, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    check("C0.1 WARD truth wall holds (neg(A) = 0 on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    n_viol = sum(1 for kz in zones
                 if isinstance(sm_map.get(kz), dict)
                 and sm_map[kz]["negA"] > 0)
    check("C1 WARD smooth world violates (neg(A) > 0 on %d rungs)"
          % n_viol, n_viol > 0, kill="K2")
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {"Epstein": gram_anatomy(
               CTRL_KZ, comb=(np.log(nn.astype(float)),
                              2.0 * lamE_[nn]
                              / np.sqrt(nn.astype(float)))),
           "scramble": gram_anatomy(CTRL_KZ, scramble_seed=1,
                                    keep_chain=True)}
    fired_all = True
    for name, r in ctl.items():
        if not isinstance(r, dict):
            print("    %-9s: chain dies -> fires" % name)
            continue
        f = r["negA"] > 0
        fired_all &= f
        print("    %-9s: tau %+.3e  neg(A) %d -> %s"
              % (name, r["tau"], r["negA"],
                 "FIRES" if f else "SILENT"), flush=True)
    check("C2.1 WARD both controls fire", fired_all, kill="K2")
    # C3: the refusal ward -- exact LDL refuses the smooth co-block
    n_ref, n_use = 0, 0
    for w in rows:
        if w["B0"] is None:
            continue
        n_use += 1
        ok0, _ = pd_exact(mat_fr(0.5 * (w["B0"] + w["B0"].T)))
        if not ok0:
            n_ref += 1
    check("C3 WARD REFUSAL: exact LDL refuses the smooth co-block "
          "B0 on %d/%d usable steps (>= %d)"
          % (n_ref, n_use, REFUSE_MIN), n_ref >= REFUSE_MIN,
          kill="K2")
    # C4: scramble core, where it exists
    rsc = ctl["scramble"]
    c4_ok = True
    c4_msg = "scramble core dead -> skipped (disclosed; C3 " \
             "carries the content)"
    if isinstance(rsc, dict) and rsc.get("core_ok") \
            and "S" in rsc and rsc["lamS"] < 0.0:
        c4_ok = rsc["lamS"] < 0.0
        c4_msg = ("lam_min(S_scr) %.3e < 0 -> the scramble core "
                  "breaks the floor" % rsc["lamS"])
    check("C4 WARD scramble breaks dominance/floor: %s" % c4_msg,
          c4_ok, kill="K2")

    labels = dict(e1a=e1a, e1b=e1b, e2=e2, e3a=e3a, e3b=e3b,
                  headline=headline)
    return finish(labels)


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("BFLOORPG-MEASURED / %s / %s / %s / %s / %s / %s"
                   % (labels.get("e1a", "-"), labels.get("e1b", "-"),
                      labels.get("e2", "-"), labels.get("e3a", "-"),
                      labels.get("e3b", "-"),
                      labels.get("headline", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): every certificate above is an
  exact-rational LDL statement about the float64-COMPUTED step
  matrices (whose entries are exact rationals); the constructions
  (P_G, variants, s) are source-only.  What this does NOT prove:
  the interval enclosure of the pipeline that produced the
  entries (named open step, v897 pattern), B-uniformity for all
  h beyond the 39-step surface, the n > q half of the endform,
  or any tail statement.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source pg_chain_interval_rollout_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pg_chain_interval_rollout_probe -- PRIME.PORT.BFLOOR.PG.IVAL.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the INTERVAL ROLLOUT of the round-62 P_G chain.
The certified surface floor of bfloor_pg_dominance_probe (21/21,
CERTIFIED-SURFACE-FLOOR-ACHIEVED, min c_B = 0.5914 on 39/39 steps)
was an EXACT statement about the float64-COMPUTED step matrices;
THIS probe lifts it to the IDEAL source objects by rebuilding every
input of the chain as a rigorous outward-rounded enclosure and
re-deciding every inequality fail-closed.  2026-08-11.)

THE OBJECT (round 62 verbatim).  The chain, per reachable step
(r1, r2) of the deployed v563 window ladder:
    B >= s P_G + c_dom I  and  P_G >= c_G I
    ==> B >= (s c_G + c_dom) I =: c_B I,     s = 1/2 (canonical V4,
frozen by the round-62 scan; P_G = the source-only CD-Gram co-block
of r2's OWN positive chain at the 8 core folds).  B = 7x7 co-block
of Q^T (S_2/tau_1) Q in the frozen Householder frame; S = core
Schur complement of A = I - G on the folds CORE_J; G = the CD-Gram
of the degree-< h projection of the rung's positive folded measure
evaluated at the negative folds.

THE LIFT + THE FROZEN-FRAME CONVENTION (declared first).  What is
ENCLOSED (all analytic content): the window lags (archimedean GL-48
layer with its transcendentals AND the von-Mangoldt tent atoms),
the grid density, the signed folded measures, the CD-kernel Gram,
the co-block Schur complement, and P_G -- every matrix entry of
B_h and P_{G,h} becomes a rigorous interval about the ideal
real-arithmetic value.  What is FROZEN as exact rational constants
of the STATEMENT (not enclosed, declared): the Householder frame Q
(built from the float64 eigenvector of r1's S -- P2 SPEC (ii),
never from the target B), the scale tau_1 > 0 (a positive scalar
cannot change any PSD verdict; the constant c_B scales with it),
and the canonical pair (V4, s = 1/2).  THE BASIS TRICK: by the
basis invariance of the Christoffel-Darboux kernel, E M^{-1} E^T
is the SAME matrix for every degree-< h polynomial basis, so the
ideal CD-Gram is enclosed through the CHEBYSHEV basis
T_0..T_{h-1}, which at the fold nodes x = cos(2 pi j / L) (j
INTEGER) evaluates in CLOSED FORM T_k(x_j) = cos(2 pi k j / L) --
pure table lookups of mpmath-enclosed cosines, NO interval Lanczos
and NO interval recurrence anywhere -- against the IDEAL Chebyshev
moment Gram M = V^T diag(w) V with a VALIDATED lam_min(M) lower
bound.  The fold bookkeeping (which grid points carry
positive/negative density, hence the core/co split) is DECIDED by
certified interval signs, never assumed.

ENCLOSURE ARCHITECTURE (fail-closed; every step typed):
 N1  transcendental layer, mpmath.iv (v897 machinery verbatim):
     GL-48 node-enclosure lemma (Newton seeds mp dps 110, radius
     1e-90, definite P_48 sign change per node interval at iv dps
     120, pairwise disjoint, 2 in the interval weight sum); arch
     lags via native outward-rounded iv.exp/iv.expm1/iv.log with
     the near branch specialised to s = 0; tent atoms with
     per-atom loop-range rigour; atom masses 2 log(spf n)/sqrt(n)
     exactly transcendental; smooth-world masses 2 e^{u/2} du as
     intervals of the same layer.  Interval lag precision from the
     DECLARED LADDER dps 40 -> 80 -> 160 (per-step escalation on
     REFUSED-WIDTH only; the frozen run starts every step at 40).
 N2  linear-algebra layer, float64 midpoint-radius intervals with
     OUTWARD rounding (Rump/INTLAB bounds, declared model: IEEE-754
     binary64, round-to-nearest; matmul/dot error <= gam(k)|A||B|
     entrywise with gam(k) = (k+2)u/(1-(k+2)u), u = 2^-53, valid
     for every summation order incl. FMA/blocked BLAS; every
     radius formula outward-inflated by (1 + 2^-38) + 1e-300,
     asserted k <= 4000; np.sqrt correctly rounded per IEEE).
     Density d = cosine transform of the lag vector against an
     mpmath-enclosed cos table (the FFT of the deployed pipeline,
     evaluated as the same finite trigonometric sum; directed
     mpf -> f64 conversion keeps exact values exact); sign census
     per grid point with an mpmath.iv RESCUE for any straddling
     entry; folded measures by directed lo/hi arithmetic; V and E
     as closed-form Chebyshev cosine lookups (basis trick above);
     the moment Gram M = V^T W V with the VALIDATED lower bound
     mu_M <= lam_min over all members (float64 Cholesky + Higham
     backward bound |dA| <= gam(n+1)|L||L^T|, minus the radius
     row sum); the CD-Gram by the residual identity K = E F_f -
     F_f^T T_M + T_M^T M^{-1} T_M (F_f a float solve SEED, T_M =
     M F_f - E^T its interval residual; the remainder is PSD and
     <= ||T_M||^2/mu_M I -- a one-sided spectral slack); the
     Schur complement by the same residual identity Y = Z^T A_bb Z
     - Z^T T - T^T Z + T^T A_bb^{-1} T with the PSD remainder <=
     ||T||^2/mu I, mu a VALIDATED lower bound on lam_min(A_bb)
     (float64 Cholesky of A_bb - beta I; Higham backward bound
     |dA| <= gam(n+1)|L||L^T|, the v897 tier-2 validated-precision
     class, labelled honestly, never called exact); the spectral
     slacks propagate through the Schur complement by the
     variational bound S(A - P) >= S(A) - rho (1 + zeta^2) I.
     SMOOTH BRANCH (the control world): A_bb is INDEFINITE there
     (that IS the wall violation), so no PSD route exists -- the
     PSD K-remainder is absorbed ENTRYWISE (|P_ij| <= G_shi for
     0 <= P <= G_shi I) and the Schur remainder is bounded
     two-sidedly through a VERIFIED approximate inverse,
     ||A_bb^-1|| <= ||X_f|| / (1 - ||A_bb X_f - I||) (Neumann),
     fail-closed at ||A_bb X_f - I|| >= 1.
 N3  decision layer, EXACT-RATIONAL LDL (round-62 machine
     verbatim): every final PSD inequality is decided by Sylvester
     pivots in Fraction arithmetic on the enclosure MIDPOINTS
     shifted OUTWARD by the full rigorous allowance dn = (max row
     sum of the radius matrix) + (spectral slacks) x ||Q||^2 --
     so a certificate at shift dn is a theorem about EVERY member
     of the enclosure, in particular the ideal object.  A too-wide
     enclosure REFUSES (PD fails at dn but holds at 0), it never
     passes: per-step enum CERTIFIED / REFUSED-WIDTH(seat) /
     FAILED(seat) / SKIPPED-BUDGET, seats DENSITY-SIGN / FOLD-SET
     / MOMENT-GRAM / SCHUR-MU / PG / DOM.

FROZEN PROTOCOL (pipeline verbatim from bfloor_pg_dominance_probe
= v900 chain; ONE Gram per rung; window memoization):

 W   PIPELINE + ROUND-62 REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2 >=
     30 full-core rungs; W3a truth all-PSD; W3b >= 20 consecutive
     full-core steps; W4 P2/P3 ledger (min lam_min(B) 0.679 rtol
     2e-2, gap 0.052/0.888 rtol 5e-2, raw disaster); W5 the crack
     (P_G PD everywhere, float dominance >= 35/39); W6 exact-LDL
     machine ward; W7 ROUND-62 FLOAT BENCHMARK re-run on the
     frozen canonical pair (V4, s = 1/2): float-entry exact chain
     certificates on ALL steps with min c_B = 0.5914 (rtol 2e-2)
     -- the per-step reference c_B^f64 for the survival ratio.

 I   INTERVAL INFRASTRUCTURE: I1 the GL-48 node-enclosure lemma
     (kill); I2 INTERVAL-MACHINE WARD (controls-must-fire at
     machine level): the fail-closed certifier must CERTIFY a
     tight PD interval matrix, type REFUSED-WIDTH on the same
     midpoint with radius 10, and type FAILED on a tight
     indefinite midpoint (kill).

 E1  THE ENCLOSURE, per needed rung (truth rungs of every step
     target r2 + smooth rungs of every usable control step; arch
     lag intervals cached per (kz, dps)): rigor gates (kill ->
     WARD-BROKEN, they test the REIMPLEMENTATION, not the wall):
     E1.a interval lag midpoints == deployed float64 core lags at
     rel sup <= 1e-9 on every enclosed rung; E1.b NO fold-set
     contradiction: every interval-decided sign agrees with the
     deployed float64 mask, the post-mask fold sets and the core
     positions match exactly; undecided signs after the mpmath
     rescue are NOT a kill -- they refuse the step (seat
     DENSITY-SIGN / FOLD-SET).  Per-rung width diagnostics printed
     (delta, ||T_M||, K-slack, Y-slack, variational slack, max
     entry radius of S).

 E2  THE CERTIFIED CHAIN, per step (frozen frame Q, tau from W):
     (i) P_G >= c_G I with c_G > 0 exact-rational at allowance
     dn_PG; (ii) B - 1/2 P_G >= c_dom I at allowance dn_D with
     c_dom > -c_G/2 (1 - 2^-20) so the assembly closes; (iii)
     c_B = c_G/2 + c_dom > 0, plus the direct benchmark floor
     c_dir on B's own enclosure.  D = B - 1/2 P_G is enclosed as
     ONE expression (1/tau) I - (1/tau + 1/2) G_cc - (1/tau) Y (no
     radius double-counting).  Typed E2.a CG-IVAL(n/N, min c_G),
     E2.b DOM-IVAL(n/N), E2.c ASSEMBLY-IVAL(n/N, min c_B, min
     survival c_B/c_B^f64) + tau-screen (PASS |s| <= 0.30 / RELOC
     >= 0.70 / AMBIG), E2.h headline
     IVAL-SURFACE-FLOOR-ACHIEVED(min c_B) [iff all steps
     CERTIFIED] / -PARTIAL(n/N, seats) / -FAILED.

 E3  THE PRECISION LADDER (SPEC v3): every REFUSED-WIDTH step is
     retried along LADDER = (dps 40, std) -> (dps 40, hi) ->
     (dps 80, hi), where the hi tier replaces the plain mid-rad
     matmuls of the enclosure-critical products by the
     compensated-blocked products of mr_matmul_hi (roundoff
     radius gam(BLK_HI) instead of gam(k), see the v3 amendment;
     FAILED is genuine and never retried).  Typed census:
     (dps, tier) used per step, remaining refusals + seats.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) = 0
     everywhere; C1 smooth world neg(A) > 0 on >= 1 rung; C2
     Epstein x^2+5y^2 comb + scramble (seed 1) at kz 9 fire; C3
     THE INTERVAL REFUSAL WARD: the IDENTICAL interval machine on
     the smooth co-block B0 (same frame, same tau, same allowance
     algebra) certifies NO smooth step (kill if any is certified);
     CERT-NEG (exact-rational refusal of B0_mid + up I, proving
     lam_min(ideal B0) <= 0) expected on >= 30 of the usable
     steps, typed; C4 scramble core breaks dominance/floor where
     it exists (disclosed skip if the scramble core dies).

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
ward / control failures (W4-W7, I1-I2, E1.a-b, C0-C4) ->
WARD-BROKEN.  All E2/E3 typed outcomes are certificates or
refusals, never kills.

VERDICT (frozen enum): BFLOORPGIVAL-MEASURED with the typed
sublabels above and the headline; else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2); PG_TOL
= 1e-12; DOM_REPRO_MIN = 35; CBMIN_REF = 0.5914 (rtol 2e-2);
S_CANON = 1/2; LADDER = ((40, std), (40, hi), (80, hi)) [v3;
v1/v2: DPS_LADDER = (40, 80, 160)]; BLK_HI = 4; DPS_NODE = 120, NODE_R
= 1e-90, DPS_NEWTON = 110, GL_N = 48; WARD_REL = 1e-9; validated
mu bounds required > 0 at beta = 0.5 (retry 0.1) x the float hint
(fail-closed, seats MOMENT-GRAM / SCHUR-MU); MASK_EPS = 1e-300
(deployed mask constant); U = 2^-53, OUT = 1 + 2^-38, DIM_MAX =
4000; BIS_ITERS = 40; CERTNEG_MIN = 30;
SLOPE_PASS = 0.30, SLOPE_RELOC = 0.70; CTRL_KZ = 9, scramble seed
1; SOFT_BUDGET_S = 2400 (checked between steps only; remaining
steps typed SKIPPED-BUDGET -- partial coverage is an honest
result); runtime cap declared 45 min total.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign, no spectral data of the TARGET B in any CONSTRUCTION.
Float64 appears ONLY as (i) the frozen frame/scale/basis constants
declared above, (ii) solve SEEDS F_f, Z_f whose residuals are
enclosed (a wrong seed widens, never falsifies), (iii) bisection
and shift HINTS next to the certificates (the final exact PD
decision is re-run at the returned shift), (iv) the W-block
reproduction measurements.  No float eigensolve of any enclosed
object enters any enclosure or decision.

NO-GO COMPLIANCE (frozen): the classical G-battery on raw B enters
only as the W4 reproduction; no rank-1 approximation; no plain
Herglotz certificate; no fit anywhere -- every number below is an
identity, an enclosure, or an exact decision.  The round-61
no-target-factorization rule stays amended exactly as in round 62:
exact-rational LDL is a CERTIFICATE, not a construction.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing; fail-first
history preserved, house precedent): THREE smoke iterations on the
first 3 steps end-to-end (TFPT_IVAL_SMOKE=3) preceded the freeze;
each fix below changed the ENCLOSURE CONSTRUCTION only -- no bar,
band, count, success criterion or enum was weakened at any point,
and the wards stayed kill-level throughout.
  smoke 1: every step REFUSED at seat FOLD-SET -- the mpf -> f64
     conversion of the cosine table stepped outward
     unconditionally, so cos(0) = 1 became a nondegenerate
     interval and the exactly-zero fold-0 weight was undecidable
     against the deployed mask.  Fix: DIRECTED conversion (exact
     values stay exact).
  smoke 2: every step REFUSED at seat MOMENT-GRAM -- the v0 basis
     (the rung's frozen float Lanczos chain, evaluated by its
     three-term recurrence in interval arithmetic) hit the
     classical interval DEPENDENCY WIDENING of elliptic
     recurrences: V-entry radii ~ 1e+41 at h = 149 while the
     midpoints were correct to 1e-14 (the same
     precision-independent phenomenon v897's node lemma had to
     defeat).  Fix (pre-freeze design change, disclosed): the
     CHEBYSHEV basis, exact by CD basis-invariance, closed form
     T_k(x_j) = cos(2 pi k j / L) at the integer fold nodes --
     NO recurrence at all; the near-identity defect bound is
     replaced by the validated lam_min(M) bound (same Higham
     class as the A_bb bound).
  smoke 3: truth steps 3/3 CERTIFIED at dps 40 (survival
     0.9730/0.9794/0.9951 of the float c_B; lag wards <= 1.3e-14,
     zero sign rescues, mu_M >= 2.0e-4, max radius of S <=
     3.5e-7), but the smooth control REFUSED at seat SCHUR-MU:
     the smooth A_bb is INDEFINITE (lam_min ~ -1.4e+2 -- the wall
     violation itself), so the PSD Schur route is
     category-inapplicable on the control world.  Fix: the
     declared SMOOTH BRANCH (entrywise slack absorption +
     verified approximate inverse, N2 above); after it the smoke
     smooth control is CERT-NEG and the smoke run is 25/25.
SPEC v1 frozen 2026-08-11 after smoke 3 with SHA printed at
runtime; the frozen full run uses no TFPT_IVAL_SMOKE and no edits
beyond this disclosure block.

SPEC v2 AMENDMENT (2026-08-11, after the FULL v1 frozen run;
fail-first preserved, the v1 census is ON RECORD): the v1 full run
was an honest PARTIAL -- 25 checks, only C3 failing, headline
IVAL-SURFACE-FLOOR-PARTIAL(5/39, min c_B = 1.4137, min survival
0.7327): all 5 steps with h <= 199 CERTIFIED at dps 40; 18 steps
REFUSED-WIDTH(DOM), 16 REFUSED-WIDTH(SCHUR-MU), 0 FAILED, and 33
of 35 smooth controls width-refused (2 CERT-NEG); the dps ladder
40 -> 80 -> 160 cured NOTHING (the seat is not transcendental).
THE IDENTIFIED SEAT (the first-class result of the v1 run): the
raw Chebyshev moment matrix has lam_min ~ 1e-5..1e-3 on the deep
rungs, and the enclosure amplifies twice through it -- the
CD-residual slack ||T_M||^2/mu_M (F_f entries ~ 1/lam_min), and
the variational transfer zeta = ||A_bc||/mu with zeta^2 ~ 1e+8
multiplying G_shi.  TWO construction fixes, same certificate
class, no bar/band/enum/success criterion moved: (i) the basis is
PRECONDITIONED by the frozen float inverse Cholesky factor of the
float moment matrix (q = T L^-T, still a fixed exactly-known
basis, CD-invariant; M_q ~ I so mu_M ~ 1 and the kappa
amplification disappears); (ii) the variational zeta is bounded
through the actual solve, zeta <= (||Z_f|| + ||T||/mu + G_shi/mu)
/ (1 - G_shi/mu), instead of ||A_bc||/mu.  SPEC v2 frozen
2026-08-11 before its full run.

SPEC v3 AMENDMENT (2026-08-11, after the FULL v2 frozen run;
fail-first preserved, the v2 census is ON RECORD): the v2 full run
was 25/25 with headline IVAL-SURFACE-FLOOR-PARTIAL(33/39, min c_B
= 0.5523, min survival 0.5655): the 6 deepest steps h
534/679/839/841/859/878 (kz 82/67/43/50/64/52) REFUSED-WIDTH(DOM),
0 FAILED, and the dps rungs 80/160 again cured NOTHING.  THE
IDENTIFIED SEAT (first-class result of the v2 run): the float64
ROUNDING FLOOR of the mid-rad linear-algebra layer -- the
dominant S-entry radii (~1e-7..2.8e-7) come from the gam(k) matmul
roundoff terms with inner dimensions k ~ 880..1760 (the
preconditioning products, the moment Gram, the CD-residual
products, the Schur products, the density fold sum), and the DOM
decision multiplies them by 1/tau_1 ~ 1e+6..7e+6 on the deepest
steps; the missing factor is 2..30.  THE v3 CURE (the
higher-precision LA layer announced in the v2 report, realised
INSIDE float64 by error-free transformations, so the certificate
class is unchanged): a HIGH-ACCURACY TIER mr_matmul_hi for the
enclosure-critical products -- the midpoint product is computed in
blocks of inner size BLK_HI = 4 and accumulated across blocks with
the Ogita-Rump TwoSum compensation (Knuth's 6-op TwoSum is EXACT
under IEEE-754 round-to-nearest); the rigorous roundoff radius
drops from gam(k)|A||B| to gam(4)|A||B| + 2(nb+2)^2 u^2 |A||B| +
2u|mid| -- a ~150..300x reduction of the LA noise floor, still a
fully outward mid-rad enclosure, interval-input terms unchanged.
LADDER REDEFINED (disclosed; an escalation schedule, not a pass
bar): (dps 40, std) -> (dps 40, hi) -> (dps 80, hi), replacing the
recorded-inert dps 80/160 std rungs; certified steps still resolve
at the FIRST rung (std tier, code path byte-identical to v2), so
the v2 regression is carried by the full re-run itself.  The
SMOOTH control path stays at (dps 40, std) verbatim -- its refusal
behaviour is required unchanged (C3 bar untouched).  No bar, band,
count, enum or success criterion moved.  SPEC v3 frozen 2026-08-11
before its full run; pre-freeze sanity (disclosed): a throwaway
unit check of mr_matmul_hi against EXACT Fraction matrix products
on random matrices (enclosure containment + measured radius scale
vs mr_matmul), run before the freeze and not kept.

NO RH claim: a certified c_B > 0 on all 39 steps is a SURFACE
theorem about the IDEAL step objects of the deployed ladder in the
declared frozen frame; it does NOT prove B-uniformity in h, the
n > q half of the endform, wall positivity beyond the surface, or
any tail statement.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY (the only factorisation is
trial-division smallest-prime-factor recovery on the deployed atom
list, v897 precedent); RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core + P_G
machinery verbatim from bfloor_pg_dominance_probe.py (round 62);
interval transcendental layer verbatim from the v897 embedded
ball_arithmetic_ladder_probe (node lemma, arch, tents); exact
LDL machine verbatim from round 62; mid-rad bounds Rump/Higham
(declared model above).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/pg_chain_interval_rollout_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
from mpmath import iv, mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_LADDER_MAX = 900
N_RUNGS_EXP = 42
MIN_CORE_RUNGS = 30
MIN_STEPS = 20
MINB_REF = 0.679
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
PG_TOL = 1e-12
DOM_REPRO_MIN = 35
CBMIN_REF = 0.5914
CBMIN_RTOL = 2e-2
S_CANON = Fraction(1, 2)
DPS_LADDER = (40, 80, 160)          # v1/v2 ladder (recorded)
LADDER = ((40, "std"), (40, "hi"), (80, "hi"))   # SPEC v3 ladder
BLK_HI = 4                          # hi-tier block size (gam(4))
DPS_NODE = 120
DPS_NEWTON = 110
NODE_R = "1e-90"
GL_N = 48
WARD_REL = 1.0e-9
MASK_EPS = 1e-300
U = 2.0 ** -53
OUT = 1.0 + 2.0 ** -38
TINY = 1e-300
DIM_MAX = 4000
BIS_ITERS = 40
CERTNEG_MIN = 30
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
SOFT_BUDGET_S = 2400.0
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
SMOKE_N = int(os.environ.get("TFPT_IVAL_SMOKE", "0"))

CHECKS = []
KILLS = []
T0 = time.time()


def elapsed():
    return time.time() - T0


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# --------------- float pipeline, verbatim (round 62 = v900 chain),
# --------------- extended ONLY by extra bookkeeping fields
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > MASK_EPS
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"], n_zone=int(rr["n_zone"]),
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def ladder_zones():
    out_ = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out_.append(kz)
    return out_


def smooth_masses(uu):
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None,
                 keep_chain=False):
    """v900/round-62 verbatim wall + fixed-core split, extended by
    bookkeeping fields (c lags, fold ids, core positions) needed by
    the interval rollout wards."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_f = rr["c_ar"] + np.asarray(c_at, float)
    d = grid_density(c_f)
    L = 2 * M - 2
    xs, ws, uf_p = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    A = np.eye(n) - G
    evA = np.linalg.eigvalsh(A)
    out_ = dict(kz=kz, h=h, n=n, alpha=float(alpha), M=M, D=D, L=L,
                n_zone=rr["n_zone"], n_atom=rr["n_atom"],
                c_f=c_f, uf_p=np.asarray(uf_p, int),
                uf_n=np.asarray(uf_n, int))
    out_["tau"] = float(evA[0])
    out_["negA"] = int(np.sum(evA < 0.0))
    if keep_chain:
        out_["chain"] = (al, be, m0)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out_["core_ok"] = all(j in idx for j in CORE_J)
    if not out_["core_ok"]:
        return out_
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    out_["ic"] = ic
    B = A[np.ix_(ic, ic)]
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out_["lamR"] = float(evR[0])
    out_["negR"] = int(np.sum(evR < 0.0))
    Z = np.linalg.solve(R, Xc.T)
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out_["S"] = S
    out_["lamS"] = float(evS[0])
    out_["negS"] = int(np.sum(evS < 0.0))
    if keep_chain:
        out_["y_core"] = np.array([ys[idx[j]] for j in CORE_J])
        out_["v_core"] = np.array([vs[idx[j]] for j in CORE_J])
    return out_


def householder_frame(v):
    n = len(v)
    v = v / float(np.linalg.norm(v))
    e1 = np.zeros(n)
    e1[0] = 1.0
    u = e1 - v
    nu = float(np.linalg.norm(u))
    if nu < 1e-14:
        return np.eye(n)
    u = u / nu
    Q = np.eye(n) - 2.0 * np.outer(u, u)
    if float(Q[:, 0] @ v) < 0:
        Q = -Q
    return Q


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def screen(vals, taus):
    vals = np.asarray(vals, float)
    taus = np.asarray(taus, float)
    pos = vals > 0
    if int(np.sum(pos)) >= 3:
        _a, sl, r2 = ols_line(np.log(taus[pos]), np.log(vals[pos]))
    else:
        return "vacuous(pos=%d)" % int(np.sum(pos)), float("nan")
    lab = ("PASS" if abs(sl) <= SLOPE_PASS
           else "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
    return "%s(slope=%+.3f, R2=%.3f)" % (lab, sl, r2), sl


def build_pg(w, which, degcap):
    """The source-only P_G co-block of one step (round 62 verbatim)."""
    r2 = w["r2"]
    src = r2 if which == "r2" else w["r1"]
    ch = src.get("chain")
    if ch is None:
        return None
    al, be, m0 = ch
    deg = src["h"] if degcap is None else min(degcap, src["h"])
    Pc = eval_chain(al, be, m0, r2["y_core"], deg)
    Gc = (np.sqrt(r2["v_core"])[:, None] * (Pc @ Pc.T)
          * np.sqrt(r2["v_core"])[None, :])
    Gc = 0.5 * (Gc + Gc.T)
    PG = (w["Q"].T @ Gc @ w["Q"])[1:, 1:]
    return 0.5 * (PG + PG.T)


def gersh_min(B):
    d = np.diag(B)
    r = np.sum(np.abs(B), axis=1) - np.abs(d)
    return float(np.min(d - r))


# ------------------------- the exact-rational LDL machine (round 62)
def mat_fr(M):
    n = M.shape[0]
    return [[Fraction(float(M[i, j])) for j in range(n)]
            for i in range(n)]


def pd_exact(Afr, shift=Fraction(0)):
    """Exact Sylvester/LDL decision: is A - shift I PD?"""
    n = len(Afr)
    A = [[Afr[i][j] - (shift if i == j else 0) for j in range(n)]
         for i in range(n)]
    for k in range(n):
        p = A[k][k]
        if p <= 0:
            return False, k
        for i in range(k + 1, n):
            f = A[i][k] / p
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - f * A[k][j]
    return True, -1


def cert_floor_exact(Afr, lo, hi, iters=BIS_ITERS):
    """Largest certified c in [lo, hi] with A - c I PD (dyadic
    bisection; final decision re-run exactly)."""
    lo = Fraction(lo)
    hi = Fraction(hi)
    if hi < lo:
        hi = lo
    ok, _ = pd_exact(Afr, lo)
    if not ok:
        return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        ok, _ = pd_exact(Afr, mid)
        if ok:
            lo = mid
        else:
            hi = mid
    ok, _ = pd_exact(Afr, lo)
    assert ok
    return lo


def shifted_fr(M7, dn):
    F = mat_fr(M7)
    d = Fraction(float(dn))
    for i in range(len(F)):
        F[i][i] -= d
    return F


# ------------------------- transcendental layer (v897 verbatim)
def ivsplit(x):
    a, b = x._mpi_
    return mp.make_mpf(a), mp.make_mpf(b)


def imax0(x):
    lo, hi = ivsplit(x)
    z = mp.mpf(0)
    return iv.mpf([lo if lo > z else z, hi if hi > z else z])


def legendre_iv(n, x):
    p0, p1 = iv.mpf(1), x
    for k in range(2, n + 1):
        p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
    dp = n * (x * p1 - p0) / (x * x - 1)
    return p1, dp


def gl_newton_mp(n):
    xs = []
    tol = mp.mpf(10) ** (-(mp.dps - 6))
    for i in range(n):
        x = mp.cos(mp.pi * (i + mp.mpf(3) / 4) / (n + mp.mpf(1) / 2))
        for _ in range(80):
            p0, p1 = mp.mpf(1), x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < tol:
                break
        xs.append(x)
    return xs


def gl_nodes_enclosed(n):
    with mp.workdps(DPS_NEWTON):
        xs0 = gl_newton_mp(n)
        r = mp.mpf(NODE_R)
        pts = [(x0 - r, x0 + r) for x0 in xs0]
    iv.dps = DPS_NODE
    sign_ok = True
    X, W = [], []
    for lo_pt, hi_pt in pts:
        p_lo, _ = legendre_iv(n, iv.mpf(lo_pt))
        p_hi, _ = legendre_iv(n, iv.mpf(hi_pt))
        la, lb = ivsplit(p_lo)
        ha, hb = ivsplit(p_hi)
        s_lo = 1 if la > 0 else (-1 if lb < 0 else 0)
        s_hi = 1 if ha > 0 else (-1 if hb < 0 else 0)
        if s_lo * s_hi != -1:
            sign_ok = False
        Xi = iv.mpf([lo_pt, hi_pt])
        _, dpi = legendre_iv(n, Xi)
        X.append(Xi)
        W.append(2 / ((1 - Xi * Xi) * dpi * dpi))
    ends = [ivsplit(x) for x in X]
    order = sorted(range(n), key=lambda i: ends[i][0])
    disjoint = all(ends[order[k]][1] < ends[order[k + 1]][0]
                   for k in range(n - 1))
    wsum = iv.mpf(0)
    for w in W:
        wsum += w
    contains2 = iv.mpf(2) in wsum
    return X, W, dict(sign_ok=sign_ok, disjoint=disjoint,
                      contains2=contains2,
                      wsum_delta=float(ivsplit(wsum.delta)[1]))


def arch_lags_iv(M, D, glX, glW):
    """v897 verbatim: archimedean lags as intervals."""
    half = D / 2
    ratio = []
    e2w0 = []
    for k in range(M):
        base = k * D + half
        row = []
        for j in range(GL_N):
            w = base + half * glX[j]
            row.append(iv.exp(-w / 2) / (-iv.expm1(-2 * w)))
            if k == 0:
                e2w0.append(iv.exp(-2 * (base + half * glX[j])))
        ratio.append(row)
    w_below = [glW[j] * (1 + glX[j]) / 2 for j in range(GL_N)]
    w_above = [glW[j] * (1 - glX[j]) / 2 for j in range(GL_N)]
    out_ = [None] * M
    for i in range(1, M):
        acc = iv.mpf(0)
        rb, ra = ratio[i - 1], ratio[i]
        for j in range(GL_N):
            acc += w_below[j] * rb[j] + w_above[j] * ra[j]
        out_[i] = -half * acc
    tot = iv.mpf(0)
    for j in range(GL_N):
        S = imax0((1 - glX[j]) / 2)
        w = half + half * glX[j]
        num = e2w0[j] - S * iv.exp(-w / 2)
        tot += half * glW[j] * (num / (-iv.expm1(-2 * w)))
    out_[0] = (-(iv.euler + iv.log(iv.pi)) + 2 * tot
               - iv.log(-iv.expm1(-2 * D)))
    return out_


def atom_lags_iv(alpha, M, uu, mm):
    """v897 verbatim: T115 tent atoms as intervals."""
    D = 2 * alpha / M
    c = [iv.mpf(0)] * M
    range_ok = True
    for u_j, mu_j in zip(uu, mm):
        u_lo, _u_hi = ivsplit(u_j)
        if not u_lo > 0:
            range_ok = False
        t = u_j / D
        t_lo, t_hi = ivsplit(t)
        i0 = int(math.floor(float(mp.ldexp(
            mp.fadd(t_lo, t_hi, exact=True), -1))))
        if not (t_lo >= i0 - 1 and t_hi <= i0 + 1):
            range_ok = False
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1 - abs(i * D - u_j) / D
            c[i] = c[i] - mu_j * imax0(v) / 2
        c[0] = c[0] - mu_j * imax0(1 - u_j / D) / 2
    return c, range_ok


_SPF_CACHE = {}


def spf(n):
    if n in _SPF_CACHE:
        return _SPF_CACHE[n]
    d = 2
    while d * d <= n:
        if n % d == 0:
            _SPF_CACHE[n] = d
            return d
        d += 1
    _SPF_CACHE[n] = n
    return n


_ATOM_IV = {}


def atom_arrays_iv(ka, dps):
    """First ka interval atom positions/masses at the given dps
    (prefix cache per dps, v897 pattern)."""
    st = _ATOM_IV.setdefault(dps, {"uu": [], "mm": []})
    uu, mm = st["uu"], st["mm"]
    while len(uu) < ka:
        n = int(core._NN[len(uu)])
        p = spf(n)
        uu.append(iv.log(n))
        mm.append(2 * iv.log(p) / iv.sqrt(n))
    return uu[:ka], mm[:ka]


def smooth_masses_iv(uu_iv):
    n = len(uu_iv)
    du = [None] * n
    for i in range(1, n - 1):
        du[i] = (uu_iv[i + 1] - uu_iv[i - 1]) / 2
    du[0] = uu_iv[1] - uu_iv[0]
    du[-1] = uu_iv[-1] - uu_iv[-2]
    return [2 * iv.exp(u / 2) * d for u, d in zip(uu_iv, du)]


_ARCH_IV = {}


def lags_iv_rung(rw, world, dps):
    """Interval lag vector of one rung at the given dps.  Returns
    (list of iv lags, range_ok).  Arch cache per (kz, dps)."""
    iv.dps = dps
    M = rw["M"]
    alpha = iv.log(rw["n_zone"])
    key = (rw["kz"], dps)
    if key not in _ARCH_IV:
        D = 2 * alpha / M
        _ARCH_IV[key] = arch_lags_iv(M, D, _GLX, _GLW)
    c_ar = _ARCH_IV[key]
    ka = rw["n_atom"]
    uu, mm = atom_arrays_iv(ka, dps)
    if world == "smooth":
        mm = smooth_masses_iv(uu)
    c_at, range_ok = atom_lags_iv(alpha, M, uu, mm)
    return [a + b for a, b in zip(c_ar, c_at)], range_ok


def iv_to_midrad_arrays(clist):
    """iv list -> (mid, rad) float64 arrays with outward rounding."""
    n = len(clist)
    cm = np.empty(n)
    cr = np.empty(n)
    with mp.workdps(60):
        for i, x in enumerate(clist):
            lo, hi = ivsplit(x)
            midm = mp.ldexp(mp.fadd(lo, hi, exact=True), -1)
            mf = float(midm)
            r1 = mp.fsub(hi, mp.mpf(mf), exact=True)
            r2 = mp.fsub(mp.mpf(mf), lo, exact=True)
            rf = float(max(r1, r2, mp.mpf(0)))
            cm[i] = mf
            cr[i] = rf
    cr = cr * OUT + TINY
    return cm, cr


def mpf_to_f64_down(a):
    """Largest float64 <= a (exact when a is representable)."""
    f = float(a)
    return f if mp.mpf(f) <= a else float(np.nextafter(f, -np.inf))


def mpf_to_f64_up(b):
    """Smallest float64 >= b (exact when b is representable)."""
    f = float(b)
    return f if mp.mpf(f) >= b else float(np.nextafter(f, np.inf))


_CT_CACHE = {}


def cos_table(L, dps):
    """(lo, hi) arrays of cos(2 pi t / L), t = 0..L-1 (directed
    conversion: exact values, e.g. cos(0) = 1, stay exact)."""
    key = (L, dps)
    if key in _CT_CACHE:
        return _CT_CACHE[key]
    iv.dps = min(dps, 60)
    lo = np.empty(L)
    hi = np.empty(L)
    with mp.workdps(min(dps, 60) + 10):
        for t in range(L):
            x = iv.cos(2 * iv.pi * t / L)
            a, b = ivsplit(x)
            lo[t] = mpf_to_f64_down(a)
            hi[t] = mpf_to_f64_up(b)
    _CT_CACHE[key] = (lo, hi)
    return lo, hi


# ------------------------- f64 mid-rad interval kernels (N2 layer)
def gam(k):
    t = (k + 2.0) * U
    return t / (1.0 - t)


def out_r(r):
    return r * OUT + TINY


def nup(x):
    return np.nextafter(x, np.inf)


def ndown(x):
    return np.nextafter(x, -np.inf)


def mr_matmul(Am, Ar, Bm, Br):
    mid = Am @ Bm
    k = Am.shape[1]
    aA = np.abs(Am)
    aB = np.abs(Bm)
    rad = gam(k) * (aA @ aB)
    if (Br is not None) and (Ar is not None):
        rad = rad + aA @ Br + Ar @ (aB + Br)
    elif Br is not None:
        rad = rad + aA @ Br
    elif Ar is not None:
        rad = rad + Ar @ aB
    return mid, out_r(rad)


def mr_matmul_hi(Am, Ar, Bm, Br, blk=BLK_HI):
    """SPEC v3 high-accuracy tier: the midpoint product is computed
    in blocks of inner size blk, accumulated with the Ogita-Rump
    TwoSum compensation (Knuth's 6-op TwoSum is EXACT for IEEE-754
    round-to-nearest, any magnitudes; numpy evaluates each array op
    as a correctly rounded double operation).  Roundoff radius:
    per-block product error <= gam(blk) |A||B| (summed over blocks
    it stays <= gam(blk) |A||B| entrywise); the compensation stream
    E carries the EXACT add errors, its own accumulation and the
    final add are bounded by 2 (nb+2)^2 u^2 |A||B| + 2 u |mid|
    (nb = number of blocks; |partial sums| <= |A||B| entrywise up
    to factors absorbed in the constant 2 and the outward
    inflation).  Interval-input terms as in mr_matmul."""
    K = Am.shape[1]
    nbb = (K + blk - 1) // blk
    S = np.zeros((Am.shape[0], Bm.shape[1]))
    E = np.zeros_like(S)
    for i0 in range(0, K, blk):
        sl = slice(i0, min(i0 + blk, K))
        P = Am[:, sl] @ Bm[sl, :]
        T = S + P
        z = T - S
        e = (S - (T - z)) + (P - z)
        S = T
        E = E + e
    mid = S + E
    aA = np.abs(Am)
    aB = np.abs(Bm)
    absAB = aA @ aB
    rad = ((gam(blk) + 2.0 * ((nbb + 2.0) ** 2) * U * U) * absAB
           + 2.0 * U * np.abs(mid))
    if (Br is not None) and (Ar is not None):
        rad = rad + aA @ Br + Ar @ (aB + Br)
    elif Br is not None:
        rad = rad + aA @ Br
    elif Ar is not None:
        rad = rad + Ar @ aB
    return mid, out_r(rad)


def mr_add(Am, Ar, Bm, Br):
    mid = Am + Bm
    return mid, out_r(Ar + Br + U * np.abs(mid))


def mr_sub(Am, Ar, Bm, Br):
    mid = Am - Bm
    return mid, out_r(Ar + Br + U * np.abs(mid))


def mr_mul_elem(Am, Ar, Bm, Br):
    mid = Am * Bm
    rad = Ar * (np.abs(Bm) + Br) + np.abs(Am) * Br + U * np.abs(mid)
    return mid, out_r(rad)


def mr_scale(Am, Ar, s):
    mid = s * Am
    return mid, out_r(abs(s) * Ar + U * np.abs(mid))


def mr_scale_iv(Am, Ar, cm, cr):
    mid = cm * Am
    rad = cr * (np.abs(Am) + Ar) + abs(cm) * Ar + U * np.abs(mid)
    return mid, out_r(rad)


def mr_sym(Am, Ar):
    """Symmetric hull for an enclosure whose ideal value is
    symmetric: |X_ij - (Am_ij + Am_ji)/2| <= (Ar_ij + Ar_ji)/2."""
    mid = 0.5 * (Am + Am.T)
    rad = 0.5 * (Ar + Ar.T) + U * np.abs(mid)
    return mid, out_r(rad)


def lohi_to_mr(lo, hi):
    mid = lo + 0.5 * (hi - lo)
    rad = out_r(np.maximum(hi - mid, mid - lo))
    return mid, rad


def op_norm_ub(Am, Ar):
    """||X||_2 <= sqrt(||.||_1 ||.||_inf) for every |X| <= |Am|+Ar."""
    Aa = np.abs(Am) + (Ar if Ar is not None else 0.0)
    n1 = float(np.max(np.sum(Aa, axis=0)))
    ninf = float(np.max(np.sum(Aa, axis=1)))
    return float(out_r(math.sqrt(n1 * ninf)))


def rowsum_ub(Ar):
    return float(out_r(float(np.max(np.sum(Ar, axis=1)))))


def v_mul(am, ar, bm, br):
    m = am * bm
    return m, out_r(ar * (np.abs(bm) + br) + np.abs(am) * br
                    + U * np.abs(m))


def cheb_eval_table(folds, ncol, L, ctm, ctr):
    """The Chebyshev basis T_0..T_{ncol-1} at the fold nodes
    x = cos(2 pi j / L), j integer, by the CLOSED FORM
    T_k(cos th) = cos(k th): pure table lookups of the enclosed
    cosine values -- no recurrence, no dependency widening."""
    idx = (np.outer(np.asarray(folds, np.int64),
                    np.arange(ncol, dtype=np.int64)) % L)
    return ctm[idx], ctr[idx].copy()


def validated_lammin(Am, Ar, hint):
    """Rigorous lower bound on lam_min over ALL symmetric members
    of [Am +- Ar]: float64 Cholesky of Am - beta I plus the Higham
    backward bound |dA| <= gam(n+1) |L||L^T| (v897 tier-2
    validated-precision class), minus the radius row-sum bound.
    Returns None if no positive bound is achieved."""
    nn = Am.shape[0]
    for frac in (0.5, 0.1):
        beta = frac * hint
        if beta <= 0:
            break
        try:
            Lc = np.linalg.cholesky(Am - beta * np.eye(nn))
        except np.linalg.LinAlgError:
            continue
        ELc = np.abs(Lc)
        e_ch = float(out_r(gam(nn + 1)
                           * float(np.max(np.sum(ELc @ ELc.T,
                                                 axis=1)))))
        mu = beta - e_ch - rowsum_ub(Ar)
        return mu if mu > 0 else None
    return None


# ------------------------- the per-rung interval pipeline (E1)
_ENC_CACHE = {}


def enclose_rung(rw, world, dps, tier="std"):
    """One rung end to end as a rigorous enclosure.  rw = the float
    gram_anatomy dict (truth or smooth) extended with window data.
    tier = "std" (plain mr_matmul, gam(k)) or "hi" (SPEC v3
    compensated-blocked products, gam(BLK_HI)).
    Returns dict(ok, seat, ...) with SymInterval blocks."""
    key = (rw["kz"], world, dps, tier)
    if key in _ENC_CACHE:
        return _ENC_CACHE[key]
    t0 = time.time()
    res = _enclose_rung_inner(rw, world, dps, tier)
    res["t"] = time.time() - t0
    _ENC_CACHE[key] = res
    return res


def _enclose_rung_inner(rw, world, dps, tier="std"):
    M, L, h = rw["M"], rw["L"], rw["h"]
    assert max(M, L, h) <= DIM_MAX
    mm = mr_matmul_hi if tier == "hi" else mr_matmul
    # ---- N1: interval lags
    c_iv, range_ok = lags_iv_rung(rw, world, dps)
    if not range_ok:
        return dict(ok=False, seat="DENSITY-SIGN",
                    note="tent range rigour failed")
    cm, cr = iv_to_midrad_arrays(c_iv)
    cf = np.asarray(rw["c_f"], float)
    ward = float(np.max(np.abs(cm - cf)) / np.max(np.abs(cf)))
    # ---- density on the fold range j = 0..M-1 (even symmetry of
    # the ideal FFT input: d_j = d_{L-j} exactly)
    ctlo, cthi = cos_table(L, dps)
    ctm, ctr = lohi_to_mr(ctlo, cthi)
    wk = np.full(M, 2.0)
    wk[0] = 1.0
    wk[M - 1] = 1.0
    cwm, cwr = cm * wk, cr * wk          # x1 / x2: exact in f64
    J = (np.outer(np.arange(M, dtype=np.int64),
                  np.arange(M, dtype=np.int64)) % L)
    dm, dr = mm(ctm[J], ctr[J], cwm[:, None], cwr[:, None])
    dm, dr = dm.ravel(), dr.ravel()
    # ---- sign census + mpmath rescue
    pos = (dm - dr) > 0.0
    neg = (dm + dr) < 0.0
    und = ~(pos | neg)
    n_rescue = 0
    if np.any(und):
        iv.dps = dps
        for j in np.nonzero(und)[0]:
            acc = iv.mpf(0)
            for k in range(M):
                acc += (int(wk[k]) * c_iv[k]
                        * iv.cos(2 * iv.pi * ((int(j) * k) % L) / L))
            a, b = ivsplit(acc)
            if a > 0:
                pos[j] = True
            elif b < 0:
                neg[j] = True
            else:
                return dict(ok=False, seat="DENSITY-SIGN",
                            note="undecided sign at fold %d" % j,
                            ward=ward)
            mf = float(mp.ldexp(mp.fadd(a, b, exact=True), -1))
            dm[j] = mf
            dr[j] = float(out_r(max(float(b) - mf, mf - float(a),
                                    0.0)))
            n_rescue += 1
        und = ~(pos | neg)
    # ---- folded measures (directed lo/hi arithmetic)
    mult = np.full(M, 2.0)
    mult[0] = 1.0
    mult[M - 1] = 1.0
    fwlo = ndown(2.0 - 2.0 * cthi[:M])
    fwlo = np.maximum(fwlo, 0.0)
    fwhi = nup(2.0 - 2.0 * ctlo[:M])
    twoL = float(2 * L)

    def measure(mask, sgn):
        jj = np.nonzero(mask)[0]
        if sgn < 0:
            alo = np.maximum(-(dm[jj] + dr[jj]), 0.0)
            ahi = -(dm[jj] - dr[jj])
        else:
            alo = np.maximum(dm[jj] - dr[jj], 0.0)
            ahi = dm[jj] + dr[jj]
        wlo = ndown(ndown(alo * fwlo[jj]) * mult[jj] / twoL)
        whi = nup(nup(ahi * fwhi[jj]) * mult[jj] / twoL)
        keep = wlo > MASK_EPS
        drop = whi < MASK_EPS
        bad = ~(keep | drop)
        return jj[keep], wlo[keep], whi[keep], int(np.sum(bad))

    jp, pwlo, pwhi, badp = measure(pos, +1)
    jn, nwlo, nwhi, badn = measure(neg, -1)
    if badp or badn:
        return dict(ok=False, seat="FOLD-SET", ward=ward,
                    note="mask undecidable on %d folds"
                         % (badp + badn))
    fold_ok = (set(jp.tolist()) == set(rw["uf_p"].tolist())
               and set(jn.tolist()) == set(rw["uf_n"].tolist()))
    if not fold_ok:
        return dict(ok=False, seat="FOLD-SET", ward=ward,
                    fold_ok=False,
                    note="interval fold set != float fold set")
    # positive weights (nodes enter only through the cos table)
    wm, wr = lohi_to_mr(pwlo, pwhi)
    n = len(jn)
    # ---- Chebyshev basis by closed form at the fold nodes
    Vm, Vr = cheb_eval_table(jp, h, L, ctm, ctr)
    Em, Er = cheb_eval_table(jn, h, L, ctm, ctr)
    # ---- SPEC v2: precondition by the frozen float inverse
    # Cholesky factor of the float moment matrix (basis q = T L^-T,
    # exactly known, CD-invariant; kills the kappa(M_cheb)
    # amplification identified by the v1 full run)
    Mf = (Vm * wm[:, None]).T @ Vm
    Mf = 0.5 * (Mf + Mf.T)
    try:
        Lf = np.linalg.cholesky(Mf)
    except np.linalg.LinAlgError:
        return dict(ok=False, seat="MOMENT-GRAM", ward=ward,
                    n_rescue=n_rescue, mu_M=None)
    Cf = np.linalg.solve(Lf, np.eye(h)).T           # frozen float
    Vm, Vr = mm(Vm, Vr, Cf, None)
    Em, Er = mm(Em, Er, Cf, None)
    # ---- moment Gram M = V^T W V + validated lam_min bound
    Vwm, Vwr = v_mul(Vm, Vr, wm[:, None], wr[:, None])
    Mqm, Mqr = mm(Vwm.T, Vwr.T, Vm, Vr)
    Mqm, Mqr = mr_sym(Mqm, Mqr)
    lam_hint = float(np.linalg.eigvalsh(Mqm)[0])    # float HINT
    mu_M = validated_lammin(Mqm, Mqr, lam_hint)
    if mu_M is None:
        return dict(ok=False, seat="MOMENT-GRAM", ward=ward,
                    n_rescue=n_rescue, mu_M=None)
    # ---- CD-Gram K = E M^-1 E^T via the residual identity
    Ff = np.linalg.solve(Mqm, Em.T)                 # float SEED
    MFm, MFr = mm(Mqm, Mqr, Ff, None)
    TMm, TMr = mr_sub(MFm, MFr, Em.T, Er.T)
    tmn = op_norm_ub(TMm, TMr)
    K1m, K1r = mm(Em, Er, Ff, None)
    K2m, K2r = mm(Ff.T, None, TMm, TMr)
    Km, Kr = mr_sub(K1m, K1r, K2m, K2r)
    Km, Kr = mr_sym(Km, Kr)
    K_shi = float(out_r(tmn * tmn / mu_M))
    # ---- G = D_v K D_v ;  A = I - G
    svlo = ndown(np.sqrt(np.maximum(nwlo, 0.0)))
    svhi = nup(np.sqrt(nwhi))
    svm, svr = lohi_to_mr(svlo, svhi)
    Svm = np.outer(svm, svm)
    Svr = out_r(np.outer(svr, np.abs(svm) + svr)
                + np.outer(np.abs(svm), svr) + U * np.abs(Svm))
    Gm, Gr = mr_mul_elem(Km, Kr, Svm, Svr)
    G_shi = float(out_r(K_shi * float(nup(np.max(nwhi)))))
    if world == "smooth":
        # the PSD K-remainder P (0 <= P <= G_shi I) is absorbed
        # ENTRYWISE (|P_ij| <= sqrt(P_ii P_jj) <= G_shi): the
        # smooth A_bb is indefinite, so no variational route exists
        Gr = out_r(Gr + G_shi)
        G_shi = 0.0
    Am = np.eye(n) - Gm
    Ar = out_r(Gr + U * np.abs(Am))
    # ---- core / co split (jn ascending by construction)
    assert np.all(np.diff(jn) > 0)
    posmap = {int(f): i for i, f in enumerate(jn)}
    if not all(j in posmap for j in CORE_J):
        return dict(ok=False, seat="FOLD-SET", ward=ward,
                    note="core fold missing")
    ic = np.array([posmap[j] for j in CORE_J], dtype=int)
    if not np.array_equal(ic, rw["ic"]):
        return dict(ok=False, seat="FOLD-SET", ward=ward,
                    note="core positions != float core positions")
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset], dtype=int)
    nb = len(ib)
    Accm = Am[np.ix_(ic, ic)]
    Accr = Ar[np.ix_(ic, ic)]
    Abcm = Am[np.ix_(ib, ic)]
    Abcr = Ar[np.ix_(ib, ic)]
    Abbm = Am[np.ix_(ib, ib)]
    Abbr = Ar[np.ix_(ib, ib)]
    # ---- Schur remainder control:
    # truth: validated mu <= lam_min(A_bb) (Higham dpotrf bound,
    #        PSD remainder one-sided) + variational slack transfer;
    # smooth: A_bb is INDEFINITE (the wall violation), so the
    #        remainder is bounded through a VERIFIED approximate
    #        inverse ||A_bb^-1|| <= ||X_f||/(1 - ||A_bb X_f - I||)
    #        (Neumann), two-sided.
    if world == "smooth":
        Xf = np.linalg.inv(Abbm)                    # float SEED
        RXm, RXr = mr_matmul(Abbm, Abbr, Xf, None)
        REm, REr = mr_sub(RXm, RXr, np.eye(nb),
                          np.zeros((nb, nb)))
        eta = op_norm_ub(REm, REr)
        if eta >= 1.0:
            return dict(ok=False, seat="SCHUR-MU", ward=ward,
                        mu_M=mu_M, n_rescue=n_rescue)
        rinv = float(out_r(op_norm_ub(Xf, None) / (1.0 - eta)))
        mu_mem = mu_ideal = float("nan")
    else:
        mu_mem = validated_lammin(Abbm, Abbr, rw["lamR"])
        if mu_mem is None or mu_mem - G_shi <= 0.0:
            return dict(ok=False, seat="SCHUR-MU", ward=ward,
                        mu_M=mu_M, n_rescue=n_rescue)
        mu_ideal = mu_mem - G_shi
    # ---- Schur complement by the residual identity
    Zf = np.linalg.solve(Abbm, Abcm)                # float SEED
    AZm, AZr = mm(Abbm, Abbr, Zf, None)
    Tm, Tr = mr_sub(AZm, AZr, Abcm, Abcr)
    tn = op_norm_ub(Tm, Tr)
    ZAZm, ZAZr = mm(Zf.T, None, AZm, AZr)
    ZTm, ZTr = mm(Zf.T, None, Tm, Tr)
    Y1m, Y1r = mr_sub(ZAZm, ZAZr, ZTm, ZTr)
    Ym_, Yr_ = mr_sub(Y1m, Y1r, ZTm.T, ZTr.T)
    Ym_, Yr_ = mr_sym(Ym_, Yr_)
    if world == "smooth":
        rho_Y = float(out_r(tn * tn * rinv))
        svar = 0.0
        slo_S = shi_S = float(out_r(rho_Y))
    else:
        rho_Y = float(out_r(tn * tn / mu_mem))
        # SPEC v2 zeta: ||(X-P)_bb^-1 (X-P)_bc|| <=
        #   (||Z_f|| + ||T||/mu + G_shi/mu) / (1 - G_shi/mu)
        g_ratio = G_shi / mu_mem
        zeta = float(out_r((op_norm_ub(Zf, None) + tn / mu_mem
                            + g_ratio) / (1.0 - g_ratio)))
        svar = float(out_r(G_shi * (1.0 + zeta * zeta)))
        slo_S = float(out_r(rho_Y + svar))
        shi_S = 0.0
    Sm_, Sr_ = mr_sub(Accm, Accr, Ym_, Yr_)
    Sm_, Sr_ = mr_sym(Sm_, Sr_)
    Gccm = Gm[np.ix_(ic, ic)]
    Gccr = Gr[np.ix_(ic, ic)]
    return dict(ok=True, seat=None, ward=ward, mu_M=mu_M,
                n_rescue=n_rescue, tmn=tmn, K_shi=K_shi,
                rho_Y=rho_Y, svar=svar, mu_mem=mu_mem,
                mu_ideal=mu_ideal,
                Sm=Sm_, Sr=Sr_, slo_S=slo_S, shi_S=shi_S,
                Gccm=Gccm, Gccr=Gccr, shi_Gcc=G_shi,
                maxradS=float(np.max(Sr_)))


# ------------------------- step assembly + fail-closed decisions
def conj_mr(Qf, Dm, Dr):
    P1m, P1r = mr_matmul(Qf.T, None, Dm, Dr)
    M2m, M2r = mr_matmul(P1m, P1r, Qf, None)
    Mm, Mr = mr_sym(M2m, M2r)
    return Mm[1:, 1:], Mr[1:, 1:]


def assemble_step(w, enc):
    """7x7 enclosures of B, P_G and D = B - s P_G in the frozen
    frame, with the full rigorous allowances."""
    Qf, tau = w["Q"], w["tau"]
    c1m = 1.0 / tau
    c1r = float(out_r(U * abs(c1m)))
    q2 = float(out_r(op_norm_ub(Qf, None) ** 2))
    Bm, Br = mr_scale_iv(enc["Sm"], enc["Sr"], c1m, c1r)
    slo_B = float(out_r((c1m + c1r) * enc["slo_S"]))
    shi_B = float(out_r((c1m + c1r) * enc["shi_S"]))
    Pm, Pr = enc["Gccm"], enc["Gccr"]
    sPm, sPr = mr_scale(Pm, Pr, 0.5)
    Dm, Dr = mr_sub(Bm, Br, sPm, sPr)
    slo_D = float(out_r(slo_B + 0.5 * enc["shi_Gcc"]))
    B7m, B7r = conj_mr(Qf, Bm, Br)
    P7m, P7r = conj_mr(Qf, Pm, Pr)
    D7m, D7r = conj_mr(Qf, Dm, Dr)
    dn_B = float(out_r(rowsum_ub(B7r) + slo_B * q2))
    up_B = float(out_r(rowsum_ub(B7r) + shi_B * q2))
    dn_PG = float(out_r(rowsum_ub(P7r)))         # slo_PG = 0
    dn_D = float(out_r(rowsum_ub(D7r) + slo_D * q2))
    return dict(B7m=B7m, B7r=B7r, P7m=P7m, P7r=P7r, D7m=D7m,
                D7r=D7r, dn_B=dn_B, up_B=up_B, dn_PG=dn_PG,
                dn_D=dn_D, maxradB=float(np.max(B7r)))


def decide_chain(asm):
    """Fail-closed chain decision: (i) c_G, (ii) c_dom, (iii) c_B;
    exact-rational at the outward allowances."""
    PGfr = shifted_fr(asm["P7m"], asm["dn_PG"])
    hi = min(PGfr[k][k] for k in range(7))
    cG = cert_floor_exact(PGfr, Fraction(0), hi) if hi > 0 else None
    if cG is None or cG <= 0:
        okmid, _ = pd_exact(mat_fr(asm["P7m"]))
        return dict(enum="REFUSED-WIDTH" if okmid else "FAILED",
                    seat="PG", cG=None, cdom=None, cB=None,
                    cdir=None)
    Dfr = shifted_fr(asm["D7m"], asm["dn_D"])
    lo = -S_CANON * cG * Fraction(2 ** 20 - 1, 2 ** 20)
    hi2 = min(Dfr[k][k] for k in range(7))
    cdom = cert_floor_exact(Dfr, lo, hi2)
    if cdom is None:
        okmid, _ = pd_exact(mat_fr(asm["D7m"]), shift=lo)
        return dict(enum="REFUSED-WIDTH" if okmid else "FAILED",
                    seat="DOM", cG=cG, cdom=None, cB=None,
                    cdir=None)
    cB = S_CANON * cG + cdom
    Bfr = shifted_fr(asm["B7m"], asm["dn_B"])
    hib = min(Bfr[k][k] for k in range(7))
    cdir = (cert_floor_exact(Bfr, Fraction(0), hib)
            if hib > 0 else None)
    return dict(enum="CERTIFIED", seat=None, cG=cG, cdom=cdom,
                cB=cB, cdir=cdir)


def decide_smooth(asm):
    """The refusal side: the identical machine on the smooth B0.
    Returns 'CERTIFIED' (ward-breaking), 'CERT-NEG' or 'REFUSED'."""
    Bfr = shifted_fr(asm["B7m"], asm["dn_B"])
    hib = min(Bfr[k][k] for k in range(7))
    c = cert_floor_exact(Bfr, Fraction(0), hib) if hib > 0 else None
    if c is not None and c > 0:
        return "CERTIFIED"
    up = shifted_fr(asm["B7m"], -asm["up_B"])
    okup, _ = pd_exact(up)
    return "REFUSED" if okup else "CERT-NEG"


_GLX = _GLW = None


def main():
    global _GLX, _GLW
    section("PRIME.PORT.BFLOOR.PG.IVAL.01 -- the interval rollout "
            "of the certified P_G chain: B >= 1/2 P_G + c_dom I on "
            "the IDEAL surface objects (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Frozen-frame "
          "convention + fail-closed enums per spec.  Smoke mode: %s"
          % (("first %d steps" % SMOKE_N) if SMOKE_N else "OFF"))
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + round-62 reproduction")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    sm_map = {}
    for kz in zones:
        r = gram_anatomy(kz, keep_chain=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
            truth.append(None)
            continue
        truth.append(r)
        rs = gram_anatomy(kz, world_fn=world_smooth,
                          keep_chain=True)
        if isinstance(rs, dict):
            sm_map[kz] = rs
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1c all tau finite",
          all(np.isfinite(r["tau"]) for r in truth), kill="K1")
    full = [r for r in truth if r["core_ok"]]
    check("W2 >= %d full-core rungs" % MIN_CORE_RUNGS,
          len(full) >= MIN_CORE_RUNGS,
          "%d full-core rungs" % len(full), kill="K1")
    ok_psd = all(r["negA"] == 0 and r["negR"] == 0
                 and r["negS"] == 0 for r in full)
    check("W3a WARD truth all-PSD (A, R, S)", ok_psd, kill="K1")
    steps = []
    for r1, r2 in zip(truth, truth[1:]):
        if not (r1.get("core_ok") and r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
        steps.append((r1, r2))
    check("W3b >= %d consecutive full-core steps" % MIN_STEPS,
          len(steps) >= MIN_STEPS, "%d steps" % len(steps),
          kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], elapsed()))
    if KILLS:
        return finish({})
    rows = []
    for r1, r2 in steps:
        wS, VS = np.linalg.eigh(r1["S"])
        Q = householder_frame(VS[:, 0])
        Mt = Q.T @ (r2["S"] / r1["tau"]) @ Q
        Mt = 0.5 * (Mt + Mt.T)
        b = Mt[1:, 0]
        B = Mt[1:, 1:]
        minB = float(np.linalg.eigvalsh(B)[0])
        gap = (float(Mt[0, 0]) - float(b @ np.linalg.solve(B, b))
               if minB > 0 else float("nan"))
        rs2 = sm_map.get(r2["kz"])
        B0 = None
        if isinstance(rs2, dict) and "S" in rs2:
            M0 = Q.T @ (rs2["S"] / r1["tau"]) @ Q
            M0 = 0.5 * (M0 + M0.T)
            B0 = M0[1:, 1:]
        rows.append(dict(r1=r1, r2=r2, Q=Q, B=B, B0=B0, minB=minB,
                         gap=gap, tau=r1["tau"],
                         bestg=gersh_min(B)))
    minB_all = float(np.min([w["minB"] for w in rows]))
    gaps = np.array([w["gap"] for w in rows])
    bests = np.array([w["bestg"] for w in rows])
    gmin, gmed = float(np.min(gaps)), float(np.median(gaps))
    ok_repro = (abs(minB_all / MINB_REF - 1.0) <= MINB_RTOL
                and abs(gmin / GAPMIN_REF - 1.0) <= GAP_RTOL
                and abs(gmed / GAPMED_REF - 1.0) <= GAP_RTOL
                and float(np.max(bests)) < 0.0)
    check("W4 REPRODUCTION P2/P3 ledger: min lam_min(B) %.4f == "
          "%.3f; gap min/med %.4f/%.4f == %.3f/%.3f; raw-B "
          "Gershgorin disaster (best max %+.1f < 0 on %d steps)"
          % (minB_all, MINB_REF, gmin, gmed, GAPMIN_REF,
             GAPMED_REF, float(np.max(bests)), len(rows)),
          ok_repro, kill="K2")
    pg_ok = True
    n_dom0 = 0
    for w in rows:
        PG = build_pg(w, "r2", None)
        if PG is None:
            pg_ok = False
            continue
        evg = np.linalg.eigvalsh(PG)
        if float(evg[0]) <= PG_TOL:
            pg_ok = False
        w["PG0"] = PG
        Dm = 0.5 * ((w["B"] - PG) + (w["B"] - PG).T)
        evd = np.linalg.eigvalsh(Dm)
        if int(np.sum(evd < 0.0)) == 0:
            n_dom0 += 1
    check("W5 REPRODUCTION THE CRACK: P_G PD on every step; float "
          "dominance negidx(B - P_G) = 0 on %d/%d (>= %d)"
          % (n_dom0, len(rows), DOM_REPRO_MIN),
          pg_ok and n_dom0 >= DOM_REPRO_MIN, kill="K2")
    ok_pd, _ = pd_exact(mat_fr(np.array([[2.0, 1.0], [1.0, 2.0]])))
    ok_ind, _ = pd_exact(mat_fr(np.array([[1.0, 2.0], [2.0, 1.0]])))
    check("W6 MACHINE WARD exact LDL: accepts PD, refuses "
          "indefinite", ok_pd and not ok_ind, kill="K2")
    # W7: the round-62 float benchmark on the frozen canonical pair
    n_bf = 0
    cbf = []
    for w in rows:
        PG = w["PG0"]
        PGfr = mat_fr(PG)
        hi = min(PGfr[k][k] for k in range(7))
        cGf = cert_floor_exact(PGfr, Fraction(0), hi)
        cBf = None
        if cGf is not None and cGf > 0:
            Df = np.asarray(w["B"] - 0.5 * PG, float)
            Df = 0.5 * (Df + Df.T)
            Dfr = mat_fr(Df)
            lo = -S_CANON * cGf * Fraction(2 ** 20 - 1, 2 ** 20)
            hid = min(Dfr[k][k] for k in range(7))
            cdf = cert_floor_exact(Dfr, lo, hid)
            if cdf is not None:
                cBf = S_CANON * cGf + cdf
        if cBf is not None and cBf > 0:
            n_bf += 1
            w["cB_f64"] = float(cBf)
            cbf.append(float(cBf))
        else:
            w["cB_f64"] = float("nan")
    cbf_min = float(np.min(cbf)) if cbf else float("nan")
    check("W7 ROUND-62 FLOAT BENCHMARK: chain certified on %d/%d "
          "float steps, min c_B^f64 = %.4f == %.4f (rtol %.0e)"
          % (n_bf, len(rows), cbf_min, CBMIN_REF, CBMIN_RTOL),
          n_bf == len(rows)
          and abs(cbf_min / CBMIN_REF - 1.0) <= CBMIN_RTOL,
          kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ I
    section("I -- interval infrastructure")
    t0 = time.time()
    _GLX, _GLW, lemma = gl_nodes_enclosed(GL_N)
    print("    GL-%d node lemma: sign changes %s | disjoint %s | "
          "2 in weight sum %s | wsum width %.1e | %.1f s"
          % (GL_N, lemma["sign_ok"], lemma["disjoint"],
             lemma["contains2"], lemma["wsum_delta"],
             time.time() - t0), flush=True)
    check("I1 NODE LEMMA: definite P_%d sign change on every node "
          "interval, pairwise disjoint, 2 in the weight sum"
          % GL_N, lemma["sign_ok"] and lemma["disjoint"]
          and lemma["contains2"], kill="K2")
    # I2: interval-machine ward on synthetic 7x7 triples
    Ttight = np.eye(7) * 2.0 + 0.5
    w_asm = dict(B7m=Ttight, B7r=np.full((7, 7), 1e-12),
                 P7m=Ttight, P7r=np.full((7, 7), 1e-12),
                 D7m=Ttight, D7r=np.full((7, 7), 1e-12),
                 dn_B=1e-11, up_B=1e-11, dn_PG=1e-11, dn_D=1e-11)
    r_tight = decide_chain(w_asm)
    w_wide = dict(w_asm, dn_PG=1e3, dn_D=1e3, dn_B=1e3)
    r_wide = decide_chain(w_wide)
    Tind = np.eye(7) * 1.0
    Tind[0, 1] = Tind[1, 0] = 2.0
    w_ind = dict(w_asm, P7m=Tind, D7m=Tind, B7m=Tind)
    r_ind = decide_chain(w_ind)
    check("I2 INTERVAL-MACHINE WARD: tight PD -> CERTIFIED; wide "
          "-> REFUSED-WIDTH; indefinite -> FAILED  (got %s / %s / "
          "%s)" % (r_tight["enum"], r_wide["enum"], r_ind["enum"]),
          r_tight["enum"] == "CERTIFIED"
          and r_wide["enum"] == "REFUSED-WIDTH"
          and r_ind["enum"] == "FAILED", kill="K2")

    # ----------------------------------------------------------- E
    section("E1/E2/E3 -- enclosures + certified chain per step "
            "(v3 ladder %s; soft budget %.0f s between steps)"
            % (LADDER, SOFT_BUDGET_S))
    work = rows[:SMOKE_N] if SMOKE_N else rows
    results = []
    wards, folds_ok = [], True
    for w in work:
        if elapsed() > SOFT_BUDGET_S:
            results.append(dict(w=w, enum="SKIPPED-BUDGET",
                                seat=None, dps=None, dec=None,
                                asm=None, enc=None))
            continue
        r2 = w["r2"]
        outcome = None
        for dps, tier in LADDER:
            enc = enclose_rung(r2, "truth", dps, tier)
            if enc.get("ward") is not None:
                wards.append(enc["ward"])
            rung = "%d/%s" % (dps, tier)
            if not enc["ok"]:
                if enc.get("fold_ok") is False:
                    folds_ok = False
                outcome = dict(w=w, enum="REFUSED-WIDTH",
                               seat=enc["seat"], dps=rung, dec=None,
                               asm=None, enc=enc)
                continue
            asm = assemble_step(w, enc)
            dec = decide_chain(asm)
            outcome = dict(w=w, enum=dec["enum"], seat=dec["seat"],
                           dps=rung, dec=dec, asm=asm, enc=enc)
            if dec["enum"] != "REFUSED-WIDTH":
                break
        results.append(outcome)
        o = outcome
        extra = ""
        if o["enum"] == "CERTIFIED":
            d = o["dec"]
            surv = (float(d["cB"]) / w["cB_f64"]
                    if np.isfinite(w["cB_f64"]) else float("nan"))
            extra = ("c_G %.4f c_dom %+.4f c_B %.4f (f64 %.4f, "
                     "survival %.8f) c_dir %s"
                     % (float(d["cG"]), float(d["cdom"]),
                        float(d["cB"]), w["cB_f64"], surv,
                        ("%.4f" % float(d["cdir"]))
                        if d["cdir"] else "-"))
        elif o["seat"]:
            extra = "seat %s" % o["seat"]
        diag = ""
        if o.get("enc") and o["enc"].get("ok"):
            e = o["enc"]
            diag = (" | ward %.1e resc %d muM %.1e Kshi %.1e "
                    "rhoY %.1e svar %.1e radS %.1e radB %.1e "
                    "dnD %.1e"
                    % (e["ward"], e["n_rescue"], e["mu_M"],
                       e["K_shi"], e["rho_Y"], e["svar"],
                       e["maxradS"],
                       o["asm"]["maxradB"] if o["asm"] else -1,
                       o["asm"]["dn_D"] if o["asm"] else -1))
        print("    kz %-3d h %-4d dps %-6s %-14s %s%s  [t %.0fs]"
              % (r2["kz"], r2["h"], str(o["dps"]), o["enum"],
                 extra, diag, elapsed()), flush=True)
    n_att = sum(1 for o in results if o["enum"] != "SKIPPED-BUDGET")
    check("E1.a CROSS-IMPLEMENTATION WARD: interval lag midpoints "
          "== deployed float64 core lags at rel <= %.0e on every "
          "enclosed rung (max %.2e over %d enclosures)"
          % (WARD_REL, max(wards) if wards else 0.0, len(wards)),
          bool(wards) and max(wards) <= WARD_REL, kill="K2")
    check("E1.b NO fold-set contradiction on any enclosed rung",
          folds_ok, kill="K2")
    n_cert = sum(1 for o in results if o["enum"] == "CERTIFIED")
    n_ref = sum(1 for o in results if o["enum"] == "REFUSED-WIDTH")
    n_fail = sum(1 for o in results if o["enum"] == "FAILED")
    n_skip = sum(1 for o in results
                 if o["enum"] == "SKIPPED-BUDGET")
    cGs = [float(o["dec"]["cG"]) for o in results
           if o["enum"] == "CERTIFIED"]
    cBs = [float(o["dec"]["cB"]) for o in results
           if o["enum"] == "CERTIFIED"]
    surv = [float(o["dec"]["cB"]) / o["w"]["cB_f64"]
            for o in results if o["enum"] == "CERTIFIED"
            and np.isfinite(o["w"]["cB_f64"])]
    e2a = ("CG-IVAL(%d/%d, min c_G=%.4f)"
           % (len(cGs), len(work),
              min(cGs) if cGs else float("nan")))
    check("E2.a typed: %s" % e2a, True)
    e2b = "DOM-IVAL(%d/%d)" % (n_cert, len(work))
    check("E2.b typed: %s" % e2b, True)
    scr_lab, _sl = screen(cBs, [o["w"]["tau"] for o in results
                                if o["enum"] == "CERTIFIED"])
    e2c = ("ASSEMBLY-IVAL(%d/%d, min c_B=%.4f, min survival "
           "%.8f, min r_pert=c_B/7=%.4f)"
           % (n_cert, len(work),
              min(cBs) if cBs else float("nan"),
              min(surv) if surv else float("nan"),
              (min(cBs) / 7.0) if cBs else float("nan")))
    check("E2.c typed: %s; tau-screen %s" % (e2c, scr_lab), True)
    if n_cert == len(work):
        headline = ("IVAL-SURFACE-FLOOR-ACHIEVED(min c_B = %.4f "
                    "on %d/%d ideal-object steps, s = 1/2)"
                    % (min(cBs), n_cert, len(work)))
    elif n_cert > 0:
        seats = sorted({o["seat"] for o in results
                        if o["seat"] is not None})
        headline = ("IVAL-SURFACE-FLOOR-PARTIAL(%d/%d, min "
                    "c_B=%.4f, seats %s, skipped %d)"
                    % (n_cert, len(work),
                       min(cBs) if cBs else float("nan"),
                       ",".join(seats) if seats else "-", n_skip))
    else:
        headline = "IVAL-SURFACE-FLOOR-FAILED"
    check("E2.h typed headline: %s" % headline, True)
    dps_census = {}
    for o in results:
        dps_census[o["dps"]] = dps_census.get(o["dps"], 0) + 1
    e3 = ("LADDER(%s; certified %d, refused-width %d, failed %d, "
          "skipped %d)"
          % (", ".join("dps %s: %d" % (k, v)
                       for k, v in sorted(dps_census.items(),
                                          key=lambda t: str(t[0]))),
             n_cert, n_ref, n_fail, n_skip))
    check("E3 typed precision-ladder census: %s" % e3, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    check("C0.1 WARD truth wall holds (neg(A) = 0 on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    n_viol = sum(1 for kz in zones
                 if isinstance(sm_map.get(kz), dict)
                 and sm_map[kz]["negA"] > 0)
    check("C1 WARD smooth world violates (neg(A) > 0 on %d rungs)"
          % n_viol, n_viol > 0, kill="K2")
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {"Epstein": gram_anatomy(
               CTRL_KZ, comb=(np.log(nn.astype(float)),
                              2.0 * lamE_[nn]
                              / np.sqrt(nn.astype(float)))),
           "scramble": gram_anatomy(CTRL_KZ, scramble_seed=1,
                                    keep_chain=True)}
    fired_all = True
    for name, r in ctl.items():
        if not isinstance(r, dict):
            print("    %-9s: chain dies -> fires" % name)
            continue
        f = r["negA"] > 0
        fired_all &= f
        print("    %-9s: tau %+.3e  neg(A) %d -> %s"
              % (name, r["tau"], r["negA"],
                 "FIRES" if f else "SILENT"), flush=True)
    check("C2.1 WARD both controls fire", fired_all, kill="K2")
    # C3: the interval refusal ward on the smooth co-block
    n_cn, n_rf, n_ct, n_wd = 0, 0, 0, 0
    sm_work = [o for o in results
               if o["enum"] != "SKIPPED-BUDGET"
               and o["w"]["B0"] is not None]
    for o in sm_work:
        w = o["w"]
        rs2 = sm_map.get(w["r2"]["kz"])
        enc0 = enclose_rung(rs2, "smooth", DPS_LADDER[0], "std")
        if enc0.get("ward") is not None:
            wards.append(enc0["ward"])
        if not enc0["ok"]:
            n_wd += 1
            print("    SMOOTH kz %-3d h %-4d: enclosure refused "
                  "(seat %s) -> machine refuses"
                  % (w["r2"]["kz"], w["r2"]["h"], enc0["seat"]),
                  flush=True)
            continue
        asm0 = assemble_step(w, enc0)
        v = decide_smooth(asm0)
        n_cn += v == "CERT-NEG"
        n_rf += v == "REFUSED"
        n_ct += v == "CERTIFIED"
    check("C3 WARD INTERVAL REFUSAL: the identical interval "
          "machine certifies NO smooth co-block (certified %d of "
          "%d usable; CERT-NEG %d >= %d, refused %d, "
          "width-refused %d)"
          % (n_ct, len(sm_work), n_cn, CERTNEG_MIN, n_rf, n_wd),
          n_ct == 0 and n_cn >= (min(CERTNEG_MIN, len(sm_work))
                                 if SMOKE_N else CERTNEG_MIN),
          kill="K2")
    rsc = ctl["scramble"]
    c4_ok = True
    c4_msg = "scramble core dead -> skipped (disclosed; C3 " \
             "carries the content)"
    if isinstance(rsc, dict) and rsc.get("core_ok") \
            and "S" in rsc and rsc["lamS"] < 0.0:
        c4_ok = rsc["lamS"] < 0.0
        c4_msg = ("lam_min(S_scr) %.3e < 0 -> the scramble core "
                  "breaks the floor" % rsc["lamS"])
    check("C4 WARD scramble breaks dominance/floor: %s" % c4_msg,
          c4_ok, kill="K2")

    labels = dict(e2a=e2a, e2b=e2b, e2c=e2c, e3=e3,
                  headline=headline)
    return finish(labels)


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("BFLOORPGIVAL-MEASURED / %s / %s / %s / %s / %s"
                   % (labels.get("e2a", "-"), labels.get("e2b", "-"),
                      labels.get("e2c", "-"), labels.get("e3", "-"),
                      labels.get("headline", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): every CERTIFIED step above is an
  exact-rational LDL statement about EVERY member of a rigorous
  outward-rounded enclosure of the IDEAL step objects (ideal lags,
  density, measures, CD-Gram, Schur complement) in the DECLARED
  frozen frame (Q, tau_1, canonical s = 1/2; Chebyshev basis --
  the CD-Gram is basis-invariant, closed form at the fold nodes).
  Auxiliary norm bounds use the v897 validated-precision class
  (Higham Cholesky backward bound), labelled honestly.  What this
  does NOT prove: B-uniformity beyond the reachable surface, the
  n > q half of the endform, or any tail statement.  NO RH claim.
  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (elapsed(), n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('bfloor_pg_dominance_probe', _SRC_0, 21, (), 'BFLOORPG-MEASURED', 0),
    ('pg_chain_interval_rollout_probe', _SRC_1, 25, (), 'BFLOORPGIVAL-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v905 -- PRIME.PORT.BFLOOR.PG.01 + PRIME.PORT.BFLOOR.PG.IVAL.01: the certified ideal-object surface floor of the B-half -- B >= (1/2)P_G + c_dom I and P_G >= c_G I, hence B >= c_B I with c_B >= 0.5523, in v897 exact-rational certificate class over rigorous outward enclosures of the ideal source objects on all 39/39 reachable steps (float chain min c_B = 0.5914; Ogita-Rump hi-tier; 0 refused / 0 failed / 0 skipped)')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v905: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the floor is certified on the reachable 39-step surface over the ideal source objects; all h beyond the surface stay open; the n > q half is untouched and RH-hard')
    print("[%s] v905 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
