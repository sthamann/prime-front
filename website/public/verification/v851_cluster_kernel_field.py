#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v851 -- PRIME.CELLCONE.KERNELFIELD.01 + PRIME.CLUSTER.MULT.01 + PRIME.CELLCONE.GRADEDKERNEL.01: the cluster route closed and the cone violations resolved into a GRADED kernel law -- the connected multiplicative cluster expansion is exact but its weights are position-geometric (route closed), the strict violation census wanders with the horizon while the depth-resolved census collapses onto a FIXED small-n kernel, and the skin-depth law D(X) ~ 0.75 X^-0.55 (R^2 0.99) turns the wandering into vanishing-depth skin -- the graded kernel+tail theorem candidate, registered [O], ONE module from three probes over one read-only parent (15 + 10 + 7 checks with the SIX frozen-honest FAILS S3.2/S4.1 (cluster) and S2.C1/S2.C2/S4.C1/S4.C2 (kernel-field controls) kept and pattern-gated, NOT refit; verdicts CLUSTERS-DIFFUSE, BOTH-PARTIAL, KERNEL-GRADED; discovery probes multiplicative_cluster_probe.py, cone_kernel_field_probe.py, graded_kernel_field_probe.py over the read-only parent cell_cone_transport_probe.py (protocol promoted in v847), 2026-08-07, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~9 s).  PART A, THE CLUSTER DECISION (route closed): the connected cluster expansion of the log-pivot EXISTS and resums EXACTLY (sympy telescoping on the Boolean lattice; the Moebius elimination -- disconnected 2-cluster weights identically zero -- exact; the 2^16-subset resummation ward 0.0e0; the weights ARE the connected correlation terms -tr(B^-1 E_i B^-1 E_j)), and the census is effectively finite-order (geometric ratio 0.084-0.59), but THE FROZEN QUESTION FAILS HONESTLY (S3.2, kept): the order-2 enrichment of multiplicatively connected pairs is E2 = 0.883 vs the frozen bar 3.0 with CI_conn 1.70 vs CI_disc 102.73 -- the margin does NOT concentrate on the connected sector; and the mass-fixed scramble does NOT collapse the enrichment (S4.1, kept): the connected weights were never arithmetic to begin with -- they are POSITION-GEOMETRIC (spline-read overlap in the 2-dim corner, which knows |u_i - u_j|, not p_i = p_j).  TYPED CLOSURE: the all-orders route THROUGH THIS PIVOT closes -- the 2x2 corner compression destroys the cluster-arithmetic before the expansion can see it; the Epstein h=2 comb separates cleanly (connected share 0.47-0.48 vs TRUE 0.008-0.016 -- its divisibility graph carries the class-group obstruction); the GUE-strand statement sharpens: the pairwise cluster data of the deployed corner is equally blind to multiplicativity.  PART B, THE FINITE KERNEL + THE MOVING CONE FIELD (BOTH-PARTIAL, the honest split): on the parent's completed-cell flow (wards: tau refs 1e-4, envelope min e1 = 4.8546 >= 4.331, telescoping 3.4e-15, cone exits reproduce 67/67 on BOTH groupings), STAGE 1 measures the strict (eps -> 0) violation census: it WANDERS -- P0 ~ X^1.03 (G1) / X^1.02 (G2) at R^2 1.00, relative position u_P0/(2 alpha) -> 0.98/0.99, max strict P0 = 244333/283607 vs the frozen cap 100 -- BUT the depth-resolved census does not: at relative depth 1e-2 the G1 kernel is bounded by n <= 73 on ALL 67 rungs; STAGE 2 builds a causal moving Lorentz tube field (axis from past states, opening from past angle readings, warm-up 12 cells, tau never enters the gate): the state direction transports CLEAN on all four rule x grouping combinations (0/355199 gated violations, cond <= 57.3, causal fence asserted at frozen spot cells) -- but all four stage-1/stage-2 must-break controls do NOT fire (S2.C1/S2.C2/S4.C1/S4.C2, kept as frozen FAILS): the fakes transport too, so the field is SELF-CALIBRATING and the transport is unclaimable as arithmetic teeth -- typed control surprise, consistent with the parent's inverted Epstein signature (the arithmetic sits IN the violations).  PART C, THE GRADED RESOLUTION (the round's positive core): the depth-eps censuses P0(eps, X) on G1 are RESOLVED on the upper interval {1e-1, 1e-2} (P0(1e-1) = 0 everywhere; P0(1e-2) <= 73 collapsing to {2,3} above alpha ~ 3.9) and wander below it, the skin depth obeys D(X) = 0.754 X^-0.548 (R^2 0.99, Kendall -1.00) with verified threshold X0(eps) = (eps/0.754)^(-1/0.548) (X0(1e-3) ~ 1.8e5, X0(1e-4) ~ 1.2e7), and the G2 mechanism is typed by contrast (interval-centroid offset ratio 1653x, running imbalance 39x -- delayed compensation spreads the violation mass);  THE CANDIDATE STATEMENT (verbatim, measured on 67 rungs, NOT proven, NOT uniform in eps, NOT an RH claim): 'for every eps > 0 there exist finite P0(eps), X0(eps) such that for every window X >= X0(eps) every state of the completed-cell flow beyond n = P0(eps) has relative depth <= eps' -- the strict census wanders as VANISHING-DEPTH SKIN, not kernel growth; registered PRIME.CELLCONE.GRADEDKERNEL.01 [O].  The stage-2 field is typed FIELD-STRUCTURAL-ONLY (the toothed gate compares flows through their OWN certified scales; a fake without a certified endpoint separates structurally, not dynamically); the scramble depth-profile control fires (2334 vs 0 skin cells at depth > 1e-2) and the Epstein in-cone anchor holds (median strict count 0).  Fixed-cone kernel layers and same-grade 2-dim corner cluster expansions are stop-listed; the named next object is the graded law itself.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes multiplicative_cluster_probe.py (15 run,
2 frozen-honest FAILS S3.2 + S4.1, exit 1, verdict CLUSTERS-DIFFUSE),
cone_kernel_field_probe.py (10 run, 4 frozen-honest control FAILS
S2.C1/S2.C2/S4.C1/S4.C2, exit 0, verdict BOTH-PARTIAL) and
graded_kernel_field_probe.py (7/7, verdict KERNEL-GRADED), all
2026-08-07, re-run identically at promotion over the READ-ONLY parent
cell_cone_transport_probe.py (embedded as a library; its own protocol
was promoted in v847 and is NOT re-gated here).  ROUND-31 EMBEDDING
CONVENTION: all four frozen sources are embedded BYTE-EXACT (raw
strings below) and executed verbatim in isolated module namespaces
registered under their canonical import names, so the probes' cross
imports resolve to the embedded copies -- the printed SPEC SHA-256
values reproduce exactly, and when the original files are present the
harness verifies byte-equality (provenance ward inside the pattern
gate).  The pattern gates encode the frozen expected censuses with
exactly the six FAILS above per the v829/v831/v843/v847
preregistered-honest precedent; the bars are NOT refit.  The original
probe files live verbatim in experiments/tfpt-discovery/.

FIREWALL: no zeros, no prime-table loaders (each probe carries and
passes its own AST firewall; gcd/divisor arithmetic is the admissible
Euler-product datum); v563 and the parent READ-ONLY; RNG only in the
declared scramble controls (seed 20260807).  NO RH claim.
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

# ------------- frozen probe sources (embedded BYTE-EXACT, raw strings)
_SRC_PARENT = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cell_cone_transport_probe -- PRIME.CELLCONE.TRANSPORT.01
(EXPLORATION ONLY, experiments/; work package D of the 2026-08-07
v5.4 strategy: the cell-wise Lorentz cone transport).

THE CORPUS NEGATIVES THIS BUILDS ON (cited, not re-adjudicated):
  * v758 keystone: the assembled certificate [continuum root (+)
    Kraus] is NOT mountable -- arch+pole PSD at no stage, the rescue
    is strictly CELL-ORDERED; additive continuum+atoms is the wrong
    granularity; the corrected target shape is the cell-wise cascade
    factorization (PRIME.PD.PERSISTENCE.01).
  * v773 (COCYCLE-DOMAIN-ONLY): the exact Moebius/Redheffer cell
    cocycle preserves the Nevanlinna/Stieltjes domain (zero breaches,
    PD cell blocks, monotone Loewner flow) but its renormalized
    objects do not converge -- structure without limit.
  * simpler_schur_recursion / layer kills: single prime layers are
    provably not positive; positivity is not additive over layers.
  * v807 (LORENTZ-COORDS-REVEAL + NULLSELECTOR-ALGEBRAIC): the
    signature-(1,2) determinant form q(t,x,y) = t^2 - x^2 - y^2 =
    4 det on the 2x2 lock blocks; the compiler vector (5,-3,4) =
    (g_car, -N_fam, |mu4|) is EXACTLY null, M(5,-3,4) =
    2 (1,2)^T (1,2); the deployed locking slope r is strictly
    monotone in alpha toward 2 (the ray edge hint).
  * v818/v829 + margin_law_probe (2026-08-07): Ah = B - S with
    margin tau = lambda_min(Ah) > 0 on all deployed rungs; tau_pnt =
    lambda_min(B - S_pnt) with the explicit zero-free density model
    (v583 convention U0 = 2 ln(-C_TH/4), GRID_PER_D = 4); certified
    envelope e1 = (tau/tau_pnt) h^{3/2} >= 4.335 on all rungs.

THE CONSTRUCTION (frozen): COMPLETED CELLS.  cell_n = (the prime-
power atom kick at n) + (its associated continuum-and-pole
increment).  In the deployed 2x2 lock coordinates the atom kick is
-lam_n Xhat_n (shipped reads) and the continuum/pole increment is
Chat_n = the S_pnt increment over the interval I_n assigned to atom
n (the growing e^{u/2} channel IS the pole channel in this frame --
the atom_pole_abel identification, cited).  TWO PREDECLARED GROUPING
RULES decide the intervals (the relational assignment):
  G1 (Abel/Stieltjes pairing, tail strand): atom j owns the
     continuum interval (u_{j-1}, u_j] ending AT its own position
     (u_0 := U0); the last atom additionally absorbs the tail
     (u_{K-1}, 2 alpha] -- the left Stieltjes pairing of dpsi with
     dx, cell = one increment of dE.
  G2 (relational mu*log mass matching): atom j owns the interval
     (v_{j-1}, v_j] where the cumulative continuum mass equals the
     cumulative atom mass, e^{v_j/2} = e^{U0/2} +
     (1/2) sum_{i<=j} Lambda(n_i)/sqrt(n_i), capped at 2 alpha; the
     remaining tail goes to the last cell.  Each prime power absorbs
     EXACTLY its own mass of smooth density (psi-inverse pairing --
     the multiplicative weight decides the continuum share).
Both rules PARTITION [U0, 2 alpha], so the completed flow
     A_k = Ah_pnt + sum_{j<=k} (Chat_j - lam_j Xhat_j)
telescopes EXACTLY from A_0 = Ah_pnt = B - S_pnt (the continuum
transversal) to A_K = B - S = Ah (the certified margin object) --
gated per rung (WARD_REL).  At stage k the state is exactly the
HYBRID window: arithmetic atoms below the moving horizon, smooth
density above it -- the completed window at every stage.

THE CELL MAP (frozen): each completed cell acts as the canonical
congruence update A_{k+1} = M_k^T A_k M_k with
     M_k = A_k^{-1/2} (I + Atil_k)^{1/2} A_k^{1/2},
     Atil_k = A_k^{-1/2} (Chat_k - lam_k Xhat_k) A_k^{-1/2},
which EXISTS iff I + Atil_k > 0 iff A_{k+1} > 0 (cone preservation
== admissibility of the Moebius/Redheffer square root).  Its induced
3x3 Lorentz action Phi_k on u = L(A) = (a11+a22, a11-a22, 2 a12)
satisfies the EXACT identity
     Phi_k^T J Phi_k = c_k J,   c_k = det(M_k)^2
                              = det(A_{k+1}) / det(A_k),
(J = diag(1,-1,-1); q(L(A)) = 4 det A) -- spot-gated numerically
(PHI_REL).  HONESTY, stated up front: because J is indefinite, the
literal matrix inequality Phi^T J Phi <= J holds ONLY at c = 1
(lambda_max(Phi^T J Phi - J) = max(c-1, 1-c) >= 0 for any c != 1);
the frozen operational J-CONTRACTIVITY reading is therefore the
ON-CONE one -- q(Phi v) <= q(v) for all v in the future cone L+,
which for the congruence map is EXACTLY c_k <= 1.  The frozen
per-cell J-DEFECT is jdef_k = c_k - 1 = det(A_{k+1})/det(A_k) - 1;
the literal lambda_max(Phi^T J Phi - J) is REPORTED alongside on the
spot-check cells with the identity named.

THE TEST (frozen; bars in FROZEN_SPEC below, sha256-hashed and
printed before any measurement):
  (a) per-cell: CONE PRESERVATION lambda_min(A_k) > 0 at every cell
      (incl. the base) and the J-defect census jdef_k <= JDEF_TOL;
  (b) the CASCADE: the composed flow stays in the future cone per
      rung; the distance to the null direction (dnull =
      q/(t^2+x^2+y^2)) and the angle to the compiler ray (5,-3,4)
      along the path and across the alpha-ordered ladder (does the
      ray appear as the asymptotic edge -- the locking-slope-2
      hint); the ray clause is the named sub-verdict
      RAY-EDGE-CONFIRMED / RAY-EDGE-OPEN and does NOT move the cone
      enum;
  (c) the INCOMPLETE contrast: the SAME flow with naive cells
      (atom kick alone, no continuum piece, same base Ah_pnt) must
      FAIL (cone exit) -- the corpus's additive-granularity negative
      reproduced as a flow; the ward that completion is load-bearing
      (its firing is mass-forced -- stated, not hidden: the
      information of this probe lives in the completed flow's path,
      the contrast is the bookkeeping ward).
CONTROLS (frozen fire rules in FROZEN_SPEC):
  C1 order swap (cells applied in decreasing u; endpoint identical
     by additivity -- checked): MEASURED, not gated (does order
     matter for the path?).
  C2 equal-weight scramble (same positions, every atom mass replaced
     by the ladder-mean mass, total matched; G1 pairing): must
     break.
  C3 Epstein x^2 + 5 y^2 comb (mass-matched, same completion, G1):
     must break; the u-positions of the breaks are censused (the
     Euler-product-sensitive cells).
  C4 removal of the continuum piece == (c).
  C5 wrong pole normalization (continuum density x WRONG_FAC = 2,
     self-consistent base B - 2 S_pnt; endpoint still telescopes to
     Ah): must break.
VERDICT ENUM (frozen, decision order):
  INVALID            -- any ward fails (no structural claim, exit 1).
  CELLS-PRESERVE-CONE -- BOTH groupings: cone preserved at EVERY
     cell on EVERY tested rung AND zero J-defect violations
     (jdef <= JDEF_TOL everywhere) AND the incomplete contrast
     breaks at >= MB_FRAC of rungs AND all must-break controls fire.
     The universal-cell-theorem candidate; the verdict then states
     exactly what the infinite statement would need.
  CONE-BROKEN        -- for BOTH groupings the completed flow exits
     the cone on >= 0.5 of the tested rungs (the completion rules do
     not produce admissible cells) -- typed which grouping failed
     where.
  CONE-PARTIAL       -- everything in between: some cells violate
     (typed census: p = 2?, prime powers k >= 2?, p mod 4,
     u-position decile), or a must-break control did not fire
     (control surprise, typed).
NO RH claim anywhere.  Cone preservation of a finite flow on 67
rungs is a FINITE measurement; nothing here bounds the infinite
ladder.  This probe writes no files; nothing outside experiments/
is touched; no ledger row, no paper edit.

FIREWALL: v563 imported READ-ONLY; mpmath used for the zero-free
constant C_TH = -2 zeta'(1/2)/zeta(1/2) ONLY; no zeta zero is read
anywhere (AST-checked); own spf sieve for the census typing (no
sympy.ntheory); NO RNG anywhere (all controls deterministic);
runtime cap 1800 s predeclared.

DECLARED IMPLEMENTATION CORRECTIONS (run 1 -> final run, 2026-08-07;
house disclosure precedent -- no bar, tolerance, grouping rule or
verdict enum changed; the FROZEN_SPEC hash is unchanged):
  (1) phi_spot PD guard: run 1 crashed at the spot gate because the
      completed flow's state at a spot cell is NOT PD (exactly the
      cone-exit event the census measures); the helper now returns
      None for non-PD states instead of inverting a singular root.
  (2) verdict validity logic: run 1's code wrongly folded the
      control-fire checks into the INVALID clause; the frozen spec
      text says INVALID only on WARD failure (S0.AST, S1.REF,
      S1.ENV, S1.TEL, S1.PHI) or runtime -- implemented as frozen.
      Controls/contrast remain gates for CELLS-PRESERVE-CONE only.
  (3) report-only additions: per-rung out-of-cone path census
      (number of out-of-cone states, first/last exit position,
      longest out-run) to type WHERE the completion fails, and the
      Epstein control surprise named in the verdict.
  Run-1 numbers carried honestly: wards all green (tau refs rel
  <= 6e-8, min e1 4.8546, telescoping 3.4e-15); BOTH groupings exit
  the cone on 67/67 rungs (first exit at cell 0 = the n = 2 atom);
  J-census G1 49.6% / G2 12.1% expanding cells; contrast fires
  67/67; equal-weight and wrong-norm fire 14/14; Epstein does NOT
  fire (0/14 exits, dnull 3.5x < 10x bar) -- the control surprise.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cell_cone_transport_probe.py
"""

import ast
import hashlib
import inspect
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)
from mpmath import mp, zeta, diff as mpdiff  # noqa: E402 (VALUES only)

FROZEN_SPEC = """\
PRIME.CELLCONE.TRANSPORT.01 spec v1 (2026-08-07, frozen before the
run).  Ladder: frame_a_zones minus h = 1292 (anomalous, v586) minus
incomplete combs (e^{2 alpha} > ATOM_MAX); full per-cell detail on
the 3 smallest-h rungs; controls on the stride-5 subset.  Objects:
Ah = B - S (shipped), tau = eig2_min(Ah); continuum model = v818
convention (U0 = 2 ln(-C_TH/4), C_TH = -2 zeta'(1/2)/zeta(1/2),
GRID_PER_D = 4, grid umax = 2 alpha + 1e-9, cumulative evaluated at
2 alpha); tau_pnt = eig2_min(B - S_pnt).  Completed flow: A_0 =
B - S_pnt; A_k = A_0 + sum_{j<=k} (Chat_j - lam_j Xhat_j); grouping
G1 = left Stieltjes intervals (U0, u_1], (u_1, u_2], ..., last cell
absorbs (u_{K-1}, 2 alpha]; G2 = mass-matched intervals e^{v_j/2} =
e^{U0/2} + 0.5 cumsum(mm)_j capped at 2 alpha, tail to last cell.
WARDS (all must pass; else INVALID): tau refs kz 9/12/13 =
5.984165e-4 / 4.351189e-4 / 5.637632e-4 rel <= 1e-4; envelope
e1 = (tau/tau_pnt) h^{3/2} >= 4.335*0.999 on ALL rungs; telescoping
|A_K - Ah|_max <= 1e-9 ||Ah||_max and |sum Chat - S_pnt|_max <=
1e-9 ||S_pnt||_max per rung per grouping; Phi spot identity
||Phi^T J Phi - c J||_max <= 1e-8 * max(c,1) and ||Phi L(A_k) -
L(A_{k+1})||max <= 1e-8 ||L(A_{k+1})|| on the spot cells (smallest
rung: cells 0, K/2, K-1, every 500th).  BARS: cone = lambda_min > 0
strictly at every cell incl. base; J-defect jdef_k =
det(A_{k+1})/det(A_k) - 1, violation iff jdef_k > JDEF_TOL = 1e-9;
MB_FRAC = 0.9 (incomplete contrast: fraction of rungs with cone
exit); CTRL_FRAC = 0.5 (controls, stride-5 subset); control fire =
[cone exit on >= CTRL_FRAC of subset rungs] OR [median over subset
of the path max |dnull| >= DNULL_FAC = 10 x the real completed
flow's]; RAY clause: RAY-EDGE-CONFIRMED iff Kendall(alpha, r_end)
>= 0.8 AND Kendall(alpha, angle_end to (5,-3,4)) <= -0.8 across the
ladder (sub-verdict only).  VERDICT (order): INVALID if any ward
fails or runtime > 1800 s; CELLS-PRESERVE-CONE iff both groupings
have zero cone exits and zero J-violations on all rungs AND
contrast >= MB_FRAC AND all must-break controls (C2, C3, C5) fire;
CONE-BROKEN iff both groupings exit the cone on >= 0.5 of rungs;
else CONE-PARTIAL (census typed: p = 2, k >= 2, p mod 4, u/2alpha
decile; control surprises named).  No prediction is frozen for the
per-cell J-census (measured as it falls); the incomplete contrast
is predicted to fire (mass-forced).  NO RH claim; writes nothing.
"""

GRID_PER_D = 4.0
STRIDE = 5
ANOMALOUS_H = 1292
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
TAU_REF_REL = 1.0e-4
ENV_C = 4.335
ENV_GUARD = 0.999
WARD_REL = 1.0e-9
PHI_REL = 1.0e-8
JDEF_TOL = 1.0e-9
MB_FRAC = 0.9
CTRL_FRAC = 0.5
DNULL_FAC = 10.0
KEN_BAR = 0.8
WRONG_FAC = 2.0
N_DETAIL = 3
RUNTIME_CAP = 1800.0
RAY = np.array([5.0, -3.0, 4.0])
J3 = np.diag([1.0, -1.0, -1.0])
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime", "find_zeros",
              "second_sheet_zero")

mp.dps = 30
C_TH = float(-2 * mpdiff(lambda s: zeta(s), 0.5) / zeta(0.5))
U0 = 2.0 * math.log(-C_TH / 4.0)

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in BANNED_IDS:
                return False
    return True


def kendall_tau(x, y):
    n = len(x)
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (x[j] - x[i]) * (y[j] - y[i])
            if s > 0:
                conc += 1
            elif s < 0:
                disc += 1
    return (conc - disc) / max(n * (n - 1) // 2, 1)


def spf_sieve(nmax):
    """Own smallest-prime-factor sieve (census typing only)."""
    s = np.zeros(nmax + 1, dtype=np.int64)
    for p in range(2, int(math.isqrt(nmax)) + 1):
        if s[p] == 0:
            s[p * p::p] = np.where(s[p * p::p] == 0, p, s[p * p::p])
    for n in range(2, nmax + 1):
        if s[n] == 0:
            s[n] = n
    return s


# ------------------------------------------------- continuum machinery
def pnt_grid(rr):
    """The v818 pnt cell grid: edges + 2x2 spline reads per cell."""
    Mz, D, alpha = rr["M"], rr["D"], rr["alpha"]
    delta = D / GRID_PER_D
    umax = 2.0 * alpha + 1e-9
    n_cells = int(math.ceil((umax - U0) / delta))
    edges = U0 + delta * np.arange(n_cells + 1)
    reads = np.empty((n_cells, 3))
    for j in range(n_cells):
        u_j = 0.5 * (edges[j] + edges[j + 1])
        reads[j, 0] = core.spline_project(rr["W11"], u_j, D, Mz)
        reads[j, 1] = core.spline_project(rr["W22"], u_j, D, Mz)
        reads[j, 2] = core.spline_project(rr["W12"], u_j, D, Mz)
    return edges, reads


def cum_reads(edges, reads, bpts):
    """Exact cumulative continuum 2x2 read (as (n,3) triples) up to
    each breakpoint: full cells by prefix sum, boundary cell by the
    exact clipped mass 2(e^{u/2} - e^{edge/2})."""
    e_half = np.exp(edges / 2.0)
    m_full = 2.0 * (e_half[1:] - e_half[:-1])
    pref = np.vstack([np.zeros(3),
                      np.cumsum(m_full[:, None] * reads, axis=0)])
    b = np.asarray(bpts, float)
    idx = np.clip(np.searchsorted(edges, b, side="right") - 1,
                  0, len(reads) - 1)
    part = 2.0 * (np.exp(b / 2.0) - e_half[idx])
    return pref[idx] + part[:, None] * reads[idx]


def breaks_G1(uu, alpha):
    """Left Stieltjes pairing: cell j ends at u_j; last cell absorbs
    the tail to 2 alpha."""
    b = np.array(uu, float)
    b[-1] = 2.0 * alpha
    return b


def breaks_G2(mm, alpha):
    """Mass-matched (mu*log relational) pairing: e^{v_j/2} = e^{U0/2}
    + 0.5 cumsum(mm)_j, capped at 2 alpha; tail to last cell."""
    v = 2.0 * np.log(math.exp(U0 / 2.0) + 0.5 * np.cumsum(mm))
    v = np.minimum(v, 2.0 * alpha)
    v[-1] = 2.0 * alpha
    return v


def cell_increments(edges, reads, bpts):
    """Chat_j triples for a partition given by breakpoints (b_0 = U0
    implicit): exact, telescoping to the full S_pnt."""
    cum = cum_reads(edges, reads, bpts)
    out = np.empty_like(cum)
    out[0] = cum[0]
    out[1:] = np.diff(cum, axis=0)
    return out


# ------------------------------------------------- the flow engine
def path_stats(A0_tri, deltas):
    """Vectorized path of A_k = A0 + cumsum(deltas); returns per-state
    arrays (K+1 incl. base) of the Lorentz/cone quantities and the
    per-cell J-defects (K)."""
    a11 = A0_tri[0] + np.concatenate([[0.0], np.cumsum(deltas[:, 0])])
    a22 = A0_tri[1] + np.concatenate([[0.0], np.cumsum(deltas[:, 1])])
    a12 = A0_tri[2] + np.concatenate([[0.0], np.cumsum(deltas[:, 2])])
    t = a11 + a22
    x = a11 - a22
    y = 2.0 * a12
    det = a11 * a22 - a12 ** 2
    R = np.hypot(0.5 * x, a12)
    lmin = 0.5 * t - R
    lmax = 0.5 * t + R
    q = t * t - x * x - y * y
    nrm2 = t * t + x * x + y * y
    dnull = q / np.maximum(nrm2, 1e-300)
    uvec = np.stack([t, x, y], axis=1)
    cosr = (uvec @ RAY) / np.maximum(
        np.linalg.norm(uvec, axis=1) * np.linalg.norm(RAY), 1e-300)
    ang = np.degrees(np.arccos(np.clip(cosr, -1.0, 1.0)))
    with np.errstate(divide="ignore", invalid="ignore"):
        jdef = det[1:] / np.where(det[:-1] != 0.0, det[:-1], np.nan) - 1.0
    r_dom = np.where(np.abs(a12) > 1e-300,
                     (lmax - a11) / np.where(a12 != 0.0, a12, 1.0),
                     np.where(a11 >= a22, 0.0, np.inf))
    return dict(a11=a11, a22=a22, a12=a12, t=t, det=det, lmin=lmin,
                lmax=lmax, dnull=dnull, ang=ang, jdef=jdef, r=r_dom)


def flow_summary(ps):
    lmin = ps["lmin"]
    cone_ok = bool(np.all(lmin > 0.0))
    first_exit = int(np.argmax(lmin <= 0.0)) if not cone_ok else -1
    out = lmin <= 0.0
    n_out = int(out.sum())
    last_out = int(len(out) - 1 - np.argmax(out[::-1])) if n_out else -1
    runs = 0
    if n_out:
        d = np.diff(out.astype(int))
        starts = np.where(d == 1)[0]
        runs = len(starts) + (1 if out[0] else 0)
    jd = ps["jdef"]
    valid = np.isfinite(jd)
    nviol = int(np.sum(jd[valid] > JDEF_TOL))
    return dict(cone_ok=cone_ok, first_exit=first_exit,
                n_out=n_out, frac_out=n_out / max(len(out), 1),
                last_out=last_out, n_out_runs=runs,
                min_lmin=float(np.min(lmin)),
                min_rel=float(np.min(lmin / np.maximum(ps["lmax"],
                                                       1e-300))),
                nviol=nviol, ncell=int(len(jd)),
                frac_viol=nviol / max(len(jd), 1),
                worst_jdef=float(np.nanmax(jd)) if len(jd) else 0.0,
                max_dnull=float(np.max(np.abs(ps["dnull"]))),
                dnull_end=float(ps["dnull"][-1]),
                r_end=float(ps["r"][-1]), ang_end=float(ps["ang"][-1]),
                ang_min=float(np.min(ps["ang"])),
                ang_argmin=float(np.argmin(ps["ang"]) /
                                 max(len(ps["ang"]) - 1, 1)))


# ------------------------------------------------- the Phi spot gate
def sqrt2(A):
    w, V = np.linalg.eigh(A)
    return V @ np.diag(np.sqrt(np.maximum(w, 0.0))) @ V.T


def tri_mat(tri):
    return np.array([[tri[0], tri[2]], [tri[2], tri[1]]])


def lorentz_of(M):
    """The 3x3 Lorentz action of the congruence X -> M^T X M in the
    (t, x, y) coordinates."""
    basis = (0.5 * np.eye(2), 0.5 * np.diag([1.0, -1.0]),
             np.array([[0.0, 0.5], [0.5, 0.0]]))
    Phi = np.empty((3, 3))
    for i, E in enumerate(basis):
        Y = M.T @ E @ M
        Phi[:, i] = (Y[0, 0] + Y[1, 1], Y[0, 0] - Y[1, 1],
                     2.0 * Y[0, 1])
    return Phi


def phi_spot(Aprev, Anext):
    """M_k, Phi_k and the exact-identity residuals for one cell.
    Returns None when the map does not exist (state not PD -- exactly
    the cone-exit event the census measures; declared robustness
    guard, no bar changed)."""
    if float(np.linalg.eigvalsh(Aprev)[0]) <= 0.0 \
            or float(np.linalg.eigvalsh(Anext)[0]) <= 0.0:
        return None
    S = sqrt2(Aprev)
    Sinv = np.linalg.inv(S)
    IA = np.eye(2) + Sinv @ (Anext - Aprev) @ Sinv
    wmin = float(np.linalg.eigvalsh(IA)[0])
    if wmin <= 0.0:
        return None
    M = Sinv @ sqrt2(IA) @ S
    Phi = lorentz_of(M)
    c = float(np.linalg.det(M)) ** 2
    res_id = float(np.max(np.abs(Phi.T @ J3 @ Phi - c * J3)))
    uP = np.array([Aprev[0, 0] + Aprev[1, 1], Aprev[0, 0] - Aprev[1, 1],
                   2.0 * Aprev[0, 1]])
    uN = np.array([Anext[0, 0] + Anext[1, 1], Anext[0, 0] - Anext[1, 1],
                   2.0 * Anext[0, 1]])
    res_map = float(np.max(np.abs(Phi @ uP - uN))) \
        / max(float(np.max(np.abs(uN))), 1e-300)
    lam_lit = float(np.max(np.linalg.eigvalsh(Phi.T @ J3 @ Phi - J3)))
    return dict(c=c, res_id=res_id, res_map=res_map, lam_lit=lam_lit)


# ------------------------------------------------- controls: Epstein
def epstein_atoms(alpha):
    """Atoms of the x^2 + 5 y^2 comb (n >= 2 represented): positions
    log n, raw masses r_Q(n)/sqrt(n) (v818 recipe, verbatim)."""
    Nmax = int(math.floor(math.exp(2.0 * alpha)))
    cnt = np.zeros(Nmax + 1)
    for xx in range(0, int(math.isqrt(Nmax)) + 1):
        rem = Nmax - xx * xx
        if rem < 0:
            break
        yy = np.arange(0, int(math.isqrt(rem // 5)) + 1)
        n = xx * xx + 5 * yy * yy
        mult = (2.0 if xx > 0 else 1.0) * np.where(yy > 0, 2.0, 1.0)
        np.add.at(cnt, n, mult)
    nn = np.nonzero(cnt[2:])[0] + 2
    return np.log(nn.astype(float)), cnt[nn] / np.sqrt(nn.astype(float))


def atom_reads(rr, uuX):
    """Per-atom 2x2 spline reads at custom positions (the build_window
    Xn recipe at explicit u)."""
    Mz, D = rr["M"], rr["D"]
    out = np.empty((len(uuX), 3))
    for i, u in enumerate(uuX):
        out[i, 0] = core.spline_project(rr["W11"], u, D, Mz)
        out[i, 1] = core.spline_project(rr["W22"], u, D, Mz)
        out[i, 2] = core.spline_project(rr["W12"], u, D, Mz)
    return out


def eig2_min(A):
    return float(np.linalg.eigvalsh(A)[0])


def main():
    spec_hash = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()
    g1_hash = hashlib.sha256(
        inspect.getsource(breaks_G1).encode()).hexdigest()
    g2_hash = hashlib.sha256(
        inspect.getsource(breaks_G2).encode()).hexdigest()
    print("=" * 78)
    print("PRIME.CELLCONE.TRANSPORT.01 -- completed cells as Lorentz "
          "cone transport")
    print("=" * 78)
    print(FROZEN_SPEC)
    print("SPEC sha256   : %s" % spec_hash)
    print("G1 rule sha256: %s" % g1_hash)
    print("G2 rule sha256: %s" % g2_hash)
    print("U0 = %.6f (C_TH = %.6f)" % (U0, C_TH))

    # ============================================================== S0
    print("\nS0 -- firewall")
    check("S0.AST no zero/prime-table loader (banned ids absent); "
          "mpmath = the zero-free constant C_TH only; no RNG anywhere",
          ast_zero_firewall(__file__))

    # ============================================================== S1
    print("\nS1 -- ladder + wards")
    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        rows.append(dict(rr=rr, kz=kz, h=rr["h"], alpha=rr["alpha"],
                         tau=eig2_min(rr["Ah"])))
    rows.sort(key=lambda w: w["alpha"])
    print("    %d regular complete rungs, alpha %.3f..%.3f, h %d..%d"
          % (len(rows), rows[0]["alpha"], rows[-1]["alpha"],
             min(w["h"] for w in rows), max(w["h"] for w in rows)))

    ref_ok = True
    ref_txt = []
    for kz, tref in TAU_REFS.items():
        tk = eig2_min(core.build_window(kz)["Ah"])
        rel = abs(tk - tref) / tref
        ref_ok = ref_ok and rel <= TAU_REF_REL
        ref_txt.append("kz%d %.6e (rel %.1e)" % (kz, tk, rel))
    check("S1.REF tau references reproduce margin_law: %s (bar %.0e)"
          % ("; ".join(ref_txt), TAU_REF_REL), ref_ok)

    # continuum grids + envelope ward + telescoping wards per rung
    env_min = float("inf")
    tel_worst = 0.0
    cw_worst = 0.0
    for w in rows:
        rr = w["rr"]
        edges, reads = pnt_grid(rr)
        w["edges"], w["reads"] = edges, reads
        S_pnt = tri_mat(cum_reads(edges, reads,
                                  [2.0 * rr["alpha"]])[0])
        w["S_pnt"] = S_pnt
        A0 = rr["B"] - S_pnt
        w["A0"] = A0
        w["tau_pnt"] = eig2_min(A0)
        e1 = (w["tau"] / w["tau_pnt"]) * w["h"] ** 1.5
        w["e1"] = e1
        env_min = min(env_min, e1)
        uu, lam, Xn = rr["uu"], rr["lam"], rr["Xn"]
        w["mm"] = 2.0 * lam
        for gname in ("G1", "G2"):
            b = (breaks_G1(uu, rr["alpha"]) if gname == "G1"
                 else breaks_G2(w["mm"], rr["alpha"]))
            Chat = cell_increments(edges, reads, b)
            csum = Chat.sum(axis=0)
            cw = float(np.max(np.abs(tri_mat(csum) - S_pnt))) \
                / max(float(np.max(np.abs(S_pnt))), 1e-300)
            cw_worst = max(cw_worst, cw)
            deltas = Chat - lam[:, None] * Xn
            A0t = (A0[0, 0], A0[1, 1], A0[0, 1])
            ps = path_stats(A0t, deltas)
            Aend = tri_mat((ps["a11"][-1], ps["a22"][-1],
                            ps["a12"][-1]))
            tel = float(np.max(np.abs(Aend - rr["Ah"]))) \
                / max(float(np.max(np.abs(rr["Ah"]))), 1e-300)
            tel_worst = max(tel_worst, tel)
            w[gname] = dict(breaks=b, deltas=deltas, ps=ps,
                            summ=flow_summary(ps))
    check("S1.ENV the certified envelope reproduces: min e1 = %.4f >= "
          "%.4f (= %.3f x %.3f) on all %d rungs"
          % (env_min, ENV_C * ENV_GUARD, ENV_C, ENV_GUARD, len(rows)),
          env_min >= ENV_C * ENV_GUARD)
    check("S1.TEL the completed flow TELESCOPES exactly per rung per "
          "grouping: worst |A_K - Ah| rel %.2e and worst "
          "|sum Chat - S_pnt| rel %.2e (bar %.0e) -- the completed "
          "cells are a PARTITION of the certified objects"
          % (tel_worst, cw_worst, WARD_REL),
          tel_worst <= WARD_REL and cw_worst <= WARD_REL)

    # Phi spot identity gate (smallest rung, G1)
    w0 = rows[0]
    ps0 = w0["G1"]["ps"]
    K0 = len(w0["G1"]["deltas"])
    spots = sorted(set([0, K0 // 2, K0 - 1]
                       + list(range(0, K0, 500))))
    worst_id = worst_map = 0.0
    lit_lines = []
    n_spot = 0
    for k in spots:
        Ap = tri_mat((ps0["a11"][k], ps0["a22"][k], ps0["a12"][k]))
        An = tri_mat((ps0["a11"][k + 1], ps0["a22"][k + 1],
                      ps0["a12"][k + 1]))
        sp = phi_spot(Ap, An)
        if sp is None:
            continue
        n_spot += 1
        worst_id = max(worst_id, sp["res_id"] / max(sp["c"], 1.0))
        worst_map = max(worst_map, sp["res_map"])
        if len(lit_lines) < 4:
            lit_lines.append("cell %d: c = %.6f, lam_max(Phi^TJPhi-J) "
                             "= %+.2e (= max(c-1,1-c) as derived)"
                             % (k, sp["c"], sp["lam_lit"]))
    check("S1.PHI the congruence/Lorentz identity holds on %d spot "
          "cells (smallest rung): worst ||Phi^TJPhi - cJ|| rel %.1e, "
          "worst |Phi L(A_k) - L(A_{k+1})| rel %.1e (bar %.0e)"
          % (n_spot, worst_id, worst_map, PHI_REL),
          worst_id <= PHI_REL and worst_map <= PHI_REL)
    print("    HONESTY (the literal J-inequality): "
          + "; ".join(lit_lines))
    print("    -> the frozen J-contractivity reading is ON-CONE: "
          "jdef = det-ratio - 1 <= 0.")

    # ============================================================== S2
    print("\nS2 -- the completed flow, per-rung census (both groupings)")
    spf = spf_sieve(int(core.ATOM_MAX) + 1)
    for gname in ("G1", "G2"):
        print("\n  grouping %s:" % gname)
        print("    %5s %7s %6s | %5s %10s %8s | %5s %6s %5s | %6s "
              "%8s | %7s %7s"
              % ("h", "alpha", "K", "cone", "min_lmin", "min_rel",
                 "n_out", "f_out", "1st", "nJvio", "fracJ",
                 "r_end", "ang_end"))
        for w in rows:
            s = w[gname]["summ"]
            print("    %5d %7.3f %6d | %5s %10.2e %8.1e | %5d %6.3f "
                  "%5d | %6d %8.4f | %7.4f %7.3f"
                  % (w["h"], w["alpha"], s["ncell"],
                     "IN" if s["cone_ok"] else "EXIT",
                     s["min_lmin"], s["min_rel"], s["n_out"],
                     s["frac_out"], s["first_exit"], s["nviol"],
                     s["frac_viol"], s["r_end"], s["ang_end"]))
    # per-cell detail on the smallest rungs (G1)
    print("\n  per-cell detail, %d smallest rungs (G1): first 12 cells "
          "+ 5 worst-jdef cells" % N_DETAIL)
    for w in sorted(rows, key=lambda v: v["h"])[:N_DETAIL]:
        ps = w["G1"]["ps"]
        jd = w["G1"]["ps"]["jdef"]
        uu = w["rr"]["uu"]
        nn = np.rint(np.exp(uu)).astype(np.int64)
        print("    rung h = %d (alpha %.3f, K = %d):"
              % (w["h"], w["alpha"], len(jd)))
        print("      %5s %8s %6s | %10s %10s %10s | %8s"
              % ("cell", "n", "u/2a", "lmin_k+1", "jdef", "dnull",
                 "r_k+1"))
        order = list(range(min(12, len(jd))))
        worst = list(np.argsort(-np.nan_to_num(jd, nan=-1e30))[:5])
        for k in order + [k for k in worst if k not in order]:
            print("      %5d %8d %6.3f | %10.2e %+10.2e %10.2e | %8.4f"
                  % (k, nn[k], uu[k] / (2 * w["alpha"]),
                     ps["lmin"][k + 1], jd[k], ps["dnull"][k + 1],
                     ps["r"][k + 1]))

    # census typing of J-violating cells (both groupings, all rungs)
    print("\n  J-defect census typing (jdef > %.0e), all rungs:"
          % JDEF_TOL)
    census = {}
    for gname in ("G1", "G2"):
        cls = dict(total=0, viol=0, p2=0, kge2=0, p1m4=0, p3m4=0,
                   dec=np.zeros(10))
        vd = np.zeros(10)
        td = np.zeros(10)
        for w in rows:
            jd = w[gname]["ps"]["jdef"]
            uu = w["rr"]["uu"]
            nn = np.rint(np.exp(uu)).astype(np.int64)
            frac = uu / (2.0 * w["alpha"])
            deci = np.clip((frac * 10).astype(int), 0, 9)
            viol = np.nan_to_num(jd, nan=-1e30) > JDEF_TOL
            cls["total"] += len(jd)
            cls["viol"] += int(viol.sum())
            np.add.at(td, deci, 1)
            np.add.at(vd, deci[viol], 1)
            for n in nn[viol]:
                p = int(spf[n])
                k = 0
                m = int(n)
                while m > 1:
                    m //= p
                    k += 1
                if p == 2:
                    cls["p2"] += 1
                elif p % 4 == 1:
                    cls["p1m4"] += 1
                else:
                    cls["p3m4"] += 1
                if k >= 2:
                    cls["kge2"] += 1
        with np.errstate(divide="ignore", invalid="ignore"):
            decf = np.where(td > 0, vd / np.maximum(td, 1), 0.0)
        census[gname] = cls
        print("    %s: %d/%d cells J-expand (%.1f%%); of the "
              "violators: p=2 %d, p=1(4) %d, p=3(4) %d, k>=2 %d; "
              "violation fraction by u/2alpha decile: %s"
              % (gname, cls["viol"], cls["total"],
                 100.0 * cls["viol"] / max(cls["total"], 1),
                 cls["p2"], cls["p1m4"], cls["p3m4"], cls["kge2"],
                 np.array2string(decf, precision=2)))

    # ============================================================== S3
    print("\nS3 -- the cascade / boundary-ray analysis")
    aas = [w["alpha"] for w in rows]
    ray_sub = {}
    for gname in ("G1", "G2"):
        r_end = [w[gname]["summ"]["r_end"] for w in rows]
        a_end = [w[gname]["summ"]["ang_end"] for w in rows]
        kt_r = kendall_tau(aas, r_end)
        kt_a = kendall_tau(aas, a_end)
        ok = kt_r >= KEN_BAR and kt_a <= -KEN_BAR
        ray_sub[gname] = ok
        argmins = [w[gname]["summ"]["ang_argmin"] for w in rows]
        print("    %s: r_end %.4f -> %.4f (Kendall vs alpha %+.3f), "
              "angle to (5,-3,4) %.3f -> %.3f deg (Kendall %+.3f); "
              "closest path approach to the ray at relative cell "
              "position median %.3f -- %s"
              % (gname, r_end[0], r_end[-1], kt_r, a_end[0],
                 a_end[-1], kt_a, float(np.median(argmins)),
                 "RAY-EDGE-CONFIRMED" if ok else "RAY-EDGE-OPEN"))
    print("    (sub-verdict only; the compiler ray (5,-3,4) is the "
          "exact null direction q = 0, v807)")

    # ============================================================== S4
    print("\nS4 -- the incomplete-cell contrast (must break; "
          "mass-forced, stated)")
    n_exit = 0
    exit_pos = []
    for w in rows:
        rr = w["rr"]
        deltas = -(rr["lam"][:, None] * rr["Xn"])
        ps = path_stats((w["A0"][0, 0], w["A0"][1, 1], w["A0"][0, 1]),
                        deltas)
        s = flow_summary(ps)
        if not s["cone_ok"]:
            n_exit += 1
            fe = s["first_exit"]
            exit_pos.append(rr["uu"][min(fe, len(rr["uu"]) - 1)]
                            / (2.0 * rr["alpha"]) if fe > 0 else 0.0)
    frac = n_exit / len(rows)
    check("S4.INC naive cells (atom kick alone, no continuum piece, "
          "same base Ah_pnt) EXIT the cone on %d/%d rungs (%.2f >= "
          "%.2f); first-exit u/2alpha median %.3f -- the corpus's "
          "additive-granularity negative reproduced: the completion "
          "is load-bearing"
          % (n_exit, len(rows), frac, MB_FRAC,
             float(np.median(exit_pos)) if exit_pos else float("nan")),
          frac >= MB_FRAC)

    # ============================================================== S5
    print("\nS5 -- controls (stride-%d subset, G1 pairing unless "
          "stated)" % STRIDE)
    sub = rows[::STRIDE]
    real_dnull_med = float(np.median(
        [w["G1"]["summ"]["max_dnull"] for w in sub]))

    # C1 order swap (measured, both groupings)
    print("  C1 order swap (cells applied in decreasing u; endpoint "
          "identical by additivity):")
    for gname in ("G1", "G2"):
        n_exit_sw = 0
        end_dev = 0.0
        for w in sub:
            deltas = w[gname]["deltas"][::-1]
            ps = path_stats((w["A0"][0, 0], w["A0"][1, 1],
                             w["A0"][0, 1]), deltas)
            s = flow_summary(ps)
            if not s["cone_ok"]:
                n_exit_sw += 1
            Aend = tri_mat((ps["a11"][-1], ps["a22"][-1],
                            ps["a12"][-1]))
            end_dev = max(end_dev,
                          float(np.max(np.abs(Aend - w["rr"]["Ah"])))
                          / float(np.max(np.abs(w["rr"]["Ah"]))))
        fwd_exits = sum(0 if w[gname]["summ"]["cone_ok"] else 1
                        for w in sub)
        print("    %s reversed: cone exits %d/%d (forward: %d/%d); "
              "endpoint dev %.1e -- ORDER %s for the path"
              % (gname, n_exit_sw, len(sub), fwd_exits, len(sub),
                 end_dev,
                 "MATTERS" if n_exit_sw != fwd_exits else
                 "does not decide cone membership"))

    def control_flow(w, uuX, lamX, XnX, cont_fac=1.0,
                     base_fac=1.0):
        """One control flow on rung w: custom atoms + G1 pairing;
        continuum scaled by cont_fac; base B - base_fac*S_pnt."""
        rr = w["rr"]
        b = breaks_G1(uuX, rr["alpha"])
        Chat = cont_fac * cell_increments(w["edges"], w["reads"], b)
        deltas = Chat - lamX[:, None] * XnX
        A0 = rr["B"] - base_fac * w["S_pnt"]
        ps = path_stats((A0[0, 0], A0[1, 1], A0[0, 1]), deltas)
        return flow_summary(ps)

    # C2 equal-weight scramble
    n_exit_eq = 0
    dn_eq = []
    for w in sub:
        rr = w["rr"]
        mm_eq = np.full(len(rr["uu"]),
                        float(np.sum(w["mm"])) / len(rr["uu"]))
        s = control_flow(w, rr["uu"], 0.5 * mm_eq, rr["Xn"])
        if not s["cone_ok"]:
            n_exit_eq += 1
        dn_eq.append(s["max_dnull"])
    eq_fire = (n_exit_eq / len(sub) >= CTRL_FRAC
               or float(np.median(dn_eq)) >= DNULL_FAC * real_dnull_med)
    check("S5.C2 [must-break] equal-weight scramble (positions kept, "
          "masses -> ladder mean, total matched): cone exits %d/%d, "
          "median path max|dnull| %.2e vs real %.2e (fire iff exits "
          ">= %.1f or dnull >= %.0fx) -- %s"
          % (n_exit_eq, len(sub), float(np.median(dn_eq)),
             real_dnull_med, CTRL_FRAC, DNULL_FAC,
             "fires" if eq_fire else "does NOT fire"), eq_fire)

    # C3 Epstein comb
    n_exit_ep = 0
    dn_ep = []
    ep_exit_pos = []
    for w in sub:
        rr = w["rr"]
        uuE, mE_raw = epstein_atoms(rr["alpha"])
        kap = float(np.sum(w["mm"])) / float(np.sum(mE_raw))
        XnE = atom_reads(rr, uuE)
        s = control_flow(w, uuE, 0.5 * kap * mE_raw, XnE)
        if not s["cone_ok"]:
            n_exit_ep += 1
            fe = s["first_exit"]
            ep_exit_pos.append(uuE[min(max(fe - 1, 0), len(uuE) - 1)]
                               / (2.0 * rr["alpha"]))
        dn_ep.append(s["max_dnull"])
    ep_fire = (n_exit_ep / len(sub) >= CTRL_FRAC
               or float(np.median(dn_ep)) >= DNULL_FAC * real_dnull_med)
    check("S5.C3 [must-break] Epstein x^2+5y^2 comb (mass-matched, "
          "same completion): cone exits %d/%d, median path "
          "max|dnull| %.2e; first-exit u/2alpha %s -- %s"
          % (n_exit_ep, len(sub), float(np.median(dn_ep)),
             ("median %.3f" % float(np.median(ep_exit_pos)))
             if ep_exit_pos else "n/a",
             "fires" if ep_fire else "does NOT fire"), ep_fire)

    # C5 wrong pole normalization
    n_exit_wr = 0
    for w in sub:
        rr = w["rr"]
        s = control_flow(w, rr["uu"], rr["lam"], rr["Xn"],
                         cont_fac=WRONG_FAC, base_fac=WRONG_FAC)
        if not s["cone_ok"]:
            n_exit_wr += 1
    wr_fire = n_exit_wr / len(sub) >= CTRL_FRAC
    check("S5.C5 [must-break] wrong pole normalization (continuum "
          "density x %.1f, self-consistent base B - %.1f S_pnt; "
          "endpoint still telescopes to Ah): cone exits %d/%d -- %s"
          % (WRONG_FAC, WRONG_FAC, n_exit_wr, len(sub),
             "fires" if wr_fire else "does NOT fire"), wr_fire)

    # ============================================================== S6
    print("\n" + "=" * 78)
    print("S6 -- VERDICT")
    print("=" * 78)
    runtime = time.time() - T0
    WARD_IDS = ("S0.AST", "S1.REF", "S1.ENV", "S1.TEL", "S1.PHI")
    ward_fails = [f for f in FAILS if f in WARD_IDS]
    valid = not ward_fails and runtime <= RUNTIME_CAP
    cone_all = {g: all(w[g]["summ"]["cone_ok"] for w in rows)
                for g in ("G1", "G2")}
    jzero = {g: census[g]["viol"] == 0 for g in ("G1", "G2")}
    exit_frac = {g: sum(0 if w[g]["summ"]["cone_ok"] else 1
                        for w in rows) / len(rows)
                 for g in ("G1", "G2")}
    contrast_ok = frac >= MB_FRAC
    controls_ok = eq_fire and ep_fire and wr_fire
    if not valid:
        verdict = "INVALID"
    elif (cone_all["G1"] and cone_all["G2"] and jzero["G1"]
          and jzero["G2"] and contrast_ok and controls_ok):
        verdict = "CELLS-PRESERVE-CONE"
    elif exit_frac["G1"] >= 0.5 and exit_frac["G2"] >= 0.5:
        verdict = "CONE-BROKEN"
    else:
        verdict = "CONE-PARTIAL"
    print("""
  VERDICT: %s
    cone preserved at every cell:  G1 %s (exit fraction %.2f), G2 %s
      (exit fraction %.2f)
    per-cell J-contraction (jdef <= %.0e): G1 %d/%d violations
      (%.1f%%), G2 %d/%d (%.1f%%)
    incomplete contrast fires: %s (%.2f of rungs)
    must-break controls: equal-weight %s, Epstein %s, wrong-norm %s
    ray sub-verdict: G1 %s, G2 %s
""" % (verdict,
       "YES" if cone_all["G1"] else "no", exit_frac["G1"],
       "YES" if cone_all["G2"] else "no", exit_frac["G2"],
       JDEF_TOL,
       census["G1"]["viol"], census["G1"]["total"],
       100.0 * census["G1"]["viol"] / max(census["G1"]["total"], 1),
       census["G2"]["viol"], census["G2"]["total"],
       100.0 * census["G2"]["viol"] / max(census["G2"]["total"], 1),
       "YES" if contrast_ok else "NO", frac,
       "fires" if eq_fire else "NO", "fires" if ep_fire else "NO",
       "fires" if wr_fire else "NO",
       "RAY-EDGE-CONFIRMED" if ray_sub["G1"] else "RAY-EDGE-OPEN",
       "RAY-EDGE-CONFIRMED" if ray_sub["G2"] else "RAY-EDGE-OPEN"))
    if verdict == "CONE-BROKEN":
        for g in ("G1", "G2"):
            fe = [w[g]["summ"]["first_exit"] for w in rows]
            fo = [w[g]["summ"]["frac_out"] for w in rows]
            nr = [w[g]["summ"]["n_out_runs"] for w in rows]
            lo = [w[g]["summ"]["last_out"]
                  / max(w[g]["summ"]["ncell"], 1) for w in rows]
            end_in = sum(1 for w in rows
                         if w[g]["ps"]["lmin"][-1] > 0.0)
            print("  TYPED (%s): first exit at cell index median %d "
                  "(the n = 2 cell if 0); fraction of path states "
                  "out of cone median %.3f; out-runs per rung median "
                  "%d; last out-of-cone state at relative position "
                  "median %.3f; endpoint back inside the cone on "
                  "%d/%d rungs (= the certified tau > 0)"
                  % (g, int(np.median(fe)), float(np.median(fo)),
                     int(np.median(nr)), float(np.median(lo)),
                     end_in, len(rows)))
    if not ep_fire:
        print("  CONTROL SURPRISE (typed, kept as frozen with its "
              "FAIL): the mass-matched Epstein comb does NOT break "
              "the cone transport while the TRUE von Mangoldt comb "
              "does -- the cone dips are driven by the true comb's "
              "own small-x fluctuation E(x) = psi(x) - x (the n = 2 "
              "cell), which the smoother Epstein representation "
              "numbers do not reproduce; the frozen must-break "
              "prediction pointed the wrong way.")
    if verdict == "CELLS-PRESERVE-CONE":
        print("""  WHAT THE INFINITE STATEMENT WOULD NEED (named exactly):
    (i)   the UNCONDITIONAL completed-cell inequality: for every
          prime power n, the completed increment Chat_n - lam_n
          Xhat_n keeps A > 0 and det non-increasing FROM THE
          CONSTRUCTION (an explicit inequality between the local
          von Mangoldt mass and its Stieltjes continuum share on the
          deployed reads) -- replacing this probe's measured census;
    (ii)  a uniform Birkhoff/Wojtkowski contraction modulus for the
          composed congruence flow in the Lorentz cone metric
          (the v773 missing piece, now on the 2x2 lock surface);
    (iii) the boundary transition: the composed flow's limit
          direction is the null ray (5,-3,4) with the transversal
          reserve tau > 0 at every finite stage -- the v818 amplifier
          floor rho > 0 restated as cone non-degeneracy.""")
    print("""
  HONESTY: this is a FINITE transport measurement on %d deployed
  rungs (2-mode lock compression).  Cone preservation of the
  completed flow is a statement about the hybrid window (atoms below
  the horizon, density above) -- it does NOT bound the infinite
  ladder, does NOT provide the uniform capture constant, and the
  per-cell J-census is measured, not derived.  The incomplete
  contrast is mass-forced (its firing confirms the bookkeeping, not
  arithmetic).  NO RH claim.""" % len(rows))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (runtime, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    print("[VERDICT] %s" % verdict)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

_SRC_CLUSTER = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""multiplicative_cluster_probe -- PRIME.CLUSTER.MULT.01
(EXPLORATION ONLY, experiments/; F5 of the 2026-08-07 evening plan:
the ALL-ORDERS route -- connected multiplicative clusters instead of
pair statistics).

THE PREMISE (frozen, read-only): the GUE strand's typed limit says
pair statistics saturate at second moments -- the true comb's
information beyond GUE is exactly what fakes lack.  The margin-law
census showed the excess is a growing cancellation (CI 5.7 -> 29.5,
diffuse at cell grade).  F5 asks whether the DIVISIBILITY GRAPH on
the window's events (nodes = prime powers; edges = shared prime
support / d | n) organizes a CLUSTER EXPANSION of the log-pivot --
the all-orders object pair correlation cannot see.

THE OBJECT: per rung the deployed corner block is A = B + sum_j
lam_j E_j (B = the arch-only structural 2x2, E_j = the per-event
read block, E_j = -Xn_j shipped; ward lambda_min(A) == tau_X ==
lambda_min(Ah)).  The log-pivot family: for a PD shift sigma,
    g_sigma(S) = log det(B + sigma I + sum_{j in S} lam_j E_j),
a set function on the event lattice.  The CLUSTER WEIGHTS are the
subset cumulants (Moebius inversion on the Boolean lattice):
    w(C) = sum_{S subset C} (-1)^{|C|-|S|} g_sigma(S),
the standard cluster/cumulant logic: (i) EXACT RESUMMATION
sum_{C} w(C) = g_sigma(full) (telescoping identity); (ii) w(C) = 0
whenever the events of C split into two non-interacting groups --
only CONNECTED correlation terms survive (the mixed-trace expansion
log det(B + sum lam_j E_j) = log det B + sum_k (-1)^{k+1}/k
tr((B^{-1} sum lam_j E_j)^k), each w(C) collecting exactly the
traces that touch EVERY member of C).  Both sympy-checked exactly,
then numeric.

THE PD FLOOR (typed before the run): the arch-only base B is
INDEFINITE at deployed scale (lambda_min(B) ~ -2.3 < 0 < tau_X),
so the expansion around the comb-blind base exists only above a
shift floor sigma_c; the sigma-ladder measures the floor and the
census runs at the smallest valid sigma* (all evaluated subsets PD).
The margin itself sits BELOW the floor -- if the census is
favorable, crossing that floor IS the control problem; typed.

THE CENSUS (kz 9 primary, orders <= 3 exhaustive; 16-event
sub-window lattice EXACT to order 16): order histogram (W1, W2,
W3, remainder R = Delta - W1 - W2 - W3 with Delta = g(full) -
g(empty)); the CONNECTIVITY split -- pair (i, j) multiplicatively
connected iff gcd(m_i, m_j) > 1 (for the prime-power comb: same
base prime; the divisibility relation coincides), 3-clusters
connected iff their gcd-graph is connected (>= 2 edges), exactly
one edge = MIXED (counted in the disconnected sector); per-sector
enrichment E2 = mean |w2| over connected pairs / mean |w2| over
disconnected pairs, sector cancellation indices CI_conn / CI_disc
(orders 2+3); per-prime connected aggregates (small primes exact);
dyadic band table (band(C) = floor(max_j u_j / ln 2) from the MASS
labels), signed band sums vs absolute mass -- band-wise coherence.

THE DISCRIMINATOR (the F5 point; anchors kz = 9, 12, 13, common
sigma* per anchor): TRUE comb (shipped reads) vs the mass-fixed
SCRAMBLE (seed 1, same mass labels, reads at scrambled positions --
the cluster structure must die if it is arithmetic) vs the h = 2
EPSTEIN comb x^2 + 5y^2 (first-ka support at own log positions,
deployed weights, unrouted -- its divisibility graph differs at the
class-group obstruction sites: composites represented while their
factors are not).  Measured per comb: E2, connected share of the
order-2 absolute mass, CI_conn / CI_disc, edge density of the
gcd-graph.

CONTROLS: the resummation ward (16-event lattice, machine
precision); the disconnected-cancellation ward (sympy exact +
float synthetic); the connected-correlation identity (sympy: the
mixed second derivative of w({i,j}) equals
-tr(B^{-1} E_i B^{-1} E_j)); tau_X / EXC regressions on the
anchors; the margin identity det A = tau_X lambda_max(A) at
sigma = 0; the read-convention ward (spline reads vs shipped Xn).

VERDICT (frozen): CLUSTERS-CARRY (connected concentration + band
summability + scramble collapse + Epstein fingerprint -- the
all-orders route has structure; the control gap typed) /
CLUSTERS-DIFFUSE (no connected concentration, E2 < 1.5 -- the
route closes; typed) / CLUSTERS-PARTIAL (bars split; typed which).
HONESTY: NO RH claim; nothing outside experiments/; no file
written; deployed-scale measurement in a 2-dim corner compression
-- a negative census closes THIS pivot's cluster route, not the
all-orders idea per se; typed in the verdict.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/multiplicative_cluster_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from itertools import combinations
from math import gcd

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.CLUSTER.MULT.01 spec v1 (2026-08-07, frozen before the run).
Object: per rung A(S) = B + sigma I + sum_{j in S} lam_j E_j with
E_j = -Xn_j (shipped) for the TRUE comb and E = -conv * spline
reads for SCR/EPS (conv from the read-convention ward, bar 1e-6
rel); g_sigma(S) = log det A(S); cluster weights w(C) =
sum_{S subset C} (-1)^{|C|-|S|} g(S).  PD shift ladder: sigma_0 =
1 + max(0, -lmin(B)) + max_comb sum_j lam_j ||E_j||_2; halving
until a census subset (orders <= 3 + full, all three combs) loses
PD (det <= 0 or tr <= 0); then 8 bisection steps; sigma* = last
valid.  Census: orders <= 3 exhaustive (triples capped 600000 --
skip typed if over); Delta = g(full) - g(empty); R = Delta - W1 -
W2 - W3.  Sub-window lattice: kz 9, first 16 events by mass, all
2^16 subsets, subset-Moebius transform; resummation ward rel 1e-8;
order histogram 1..16; geometric ratio rho_ord = median
|W_{k+1}/W_k| over k = 1..6.  Connectivity: conn2(i,j) iff
gcd(m_i, m_j) > 1 (mass labels); conn3 iff >= 2 gcd-edges; exactly
1 edge = MIXED (disconnected sector).  E2 = mean|w2|_conn /
mean|w2|_disc; CI_sector = sum|w| / |sum w| over orders 2+3 per
sector.  Bands: band(C) = floor(max_j log(m_j)/ln 2); T = W1 + W2
+ W3; band bar sum_b |S_b| <= 3 |T|.  Sympy wards (exact): 3-event
telescoping == 0; block-disconnected pair w == 0 while its
1-cluster product is nonzero; connected pair nonzero at numeric
substitution; mixed derivative d2 w/dl1 dl2 |_0 ==
-tr(B^{-1} E1 B^{-1} E2).  Float synthetic disconnected pair: |w|
<= 1e-12.  Controls: tau refs kz 9/12/13 = 5.984165e-4 /
4.351189e-4 / 5.637632e-4 rel 1e-4; EXC refs 2.28526 / 2.48552 /
2.52887 rel 1e-3; margin identity |det A - tau lmax| <= 1e-10
scale at sigma = 0; lambda_min(B + sum lam E) == lambda_min(Ah)
1e-9 scale.  Discriminator (anchors, common sigma*): SCR collapse
iff E2_scr <= E2_true / 3 on all anchors; EPS fingerprint iff
|log2(E2_eps / E2_true)| >= 1 OR conn-share ratio outside
[0.5, 2] on all anchors.  VERDICT: CLUSTERS-CARRY iff order bar
(|R| <= 0.05 |Delta| OR rho_ord <= 0.6) AND E2_true(kz9, sigma*)
>= 3 AND CI_conn <= CI_disc / 3 AND band bar AND SCR collapse AND
EPS fingerprint; CLUSTERS-DIFFUSE iff E2_true(kz9, sigma*) < 1.5;
else CLUSTERS-PARTIAL.  Scramble seed 1.  NO RH claim; writes
nothing.
"""

ANCHORS = (9, 12, 13)
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
EXC_REFS = {9: 2.28526, 12: 2.48552, 13: 2.52887}
SCR_SEED = 1
N_LATTICE = 16
N3_MAX = 600000
N_BISECT = 8
BAR_RESUM = 1.0e-8
BAR_CONV = 1.0e-6
BAR_TAU = 1.0e-4
BAR_EXC = 1.0e-3
BAR_ORDER = 0.05
BAR_RHO = 0.6
BAR_E2 = 3.0
BAR_E2_LOW = 1.5
BAR_CI_RATIO = 3.0
BAR_BAND = 3.0
X_EPS = 4096
LN2 = math.log(2.0)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


# ------------------------------------------------------------ helpers
def reads_at(rr, uus):
    Mz, D = rr["M"], rr["D"]
    out = np.empty((len(uus), 3))
    for j, u in enumerate(uus):
        out[j, 0] = core.spline_project(rr["W11"], float(u), D, Mz)
        out[j, 1] = core.spline_project(rr["W22"], float(u), D, Mz)
        out[j, 2] = core.spline_project(rr["W12"], float(u), D, Mz)
    return out


def specnorm2(a, c, b):
    m = 0.5 * (a + c)
    r = np.hypot(0.5 * (a - c), b)
    return np.maximum(np.abs(m + r), np.abs(m - r))


def sum2sq_free_support(count, cap):
    rep = np.zeros(cap + 1, dtype=np.int64)
    s = int(math.isqrt(cap)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= cap:
                rep[v] += 1
    return [n for n in range(2, cap + 1) if rep[n] > 0][:count]


_TRIPLE_CACHE = {}


def triple_idx(ka):
    if ka not in _TRIPLE_CACHE:
        _TRIPLE_CACHE[ka] = np.array(
            list(combinations(range(ka), 3)), dtype=np.int32)
    return _TRIPLE_CACHE[ka]


def cluster_census(B2, F, masses, sigma, do_triples=True):
    """Subset-cumulant census of g(S) = log det(B + sigma I +
    sum_S F_j) at orders <= 3.  F = (ka, 3) array of lam_j E_j in
    (a, c, b) layout.  Returns None if any evaluated subset loses
    positive-definiteness."""
    ka = F.shape[0]
    Ba = B2[0, 0] + sigma
    Bc = B2[1, 1] + sigma
    Bb = B2[0, 1]
    FA, FC, FB = F[:, 0], F[:, 1], F[:, 2]

    def dets(sa, sc, sb):
        det = (Ba + sa) * (Bc + sc) - (Bb + sb) ** 2
        tr = (Ba + sa) + (Bc + sc)
        return det, tr

    d0, t0 = dets(0.0, 0.0, 0.0)
    d1, t1 = dets(FA, FC, FB)
    dF, tF = dets(FA.sum(), FC.sum(), FB.sum())
    iu, ju = np.triu_indices(ka, k=1)
    d2, t2 = dets(FA[iu] + FA[ju], FC[iu] + FC[ju], FB[iu] + FB[ju])
    ok = (d0 > 0 and t0 > 0 and np.all(d1 > 0) and np.all(t1 > 0)
          and np.all(d2 > 0) and np.all(t2 > 0) and dF > 0 and tF > 0)
    d3 = t3 = tri = None
    if do_triples:
        tri = triple_idx(ka)
        i3, j3, k3 = tri[:, 0], tri[:, 1], tri[:, 2]
        d3, t3 = dets(FA[i3] + FA[j3] + FA[k3],
                      FC[i3] + FC[j3] + FC[k3],
                      FB[i3] + FB[j3] + FB[k3])
        ok = ok and np.all(d3 > 0) and np.all(t3 > 0)
    if not ok:
        return None
    g0 = math.log(d0)
    g1 = np.log(d1)
    g2 = np.log(d2)
    gF = math.log(dF)
    w1 = g1 - g0
    w2 = g2 - g1[iu] - g1[ju] + g0
    out = dict(g0=g0, gF=gF, delta=gF - g0, w1=w1, iu=iu, ju=ju,
               w2=w2, W1=float(np.sum(w1)), W2=float(np.sum(w2)))
    mm = np.asarray(masses, dtype=np.int64)
    conn2 = np.array([gcd(int(mm[a]), int(mm[b])) > 1
                      for a, b in zip(iu, ju)])
    out["conn2"] = conn2
    if do_triples:
        G2 = np.zeros((ka, ka))
        G2[iu, ju] = g2
        G2[ju, iu] = g2
        i3, j3, k3 = tri[:, 0], tri[:, 1], tri[:, 2]
        g3 = np.log(d3)
        w3 = (g3 - G2[i3, j3] - G2[i3, k3] - G2[j3, k3]
              + g1[i3] + g1[j3] + g1[k3] - g0)
        E2m = np.zeros((ka, ka), dtype=bool)
        E2m[iu, ju] = conn2
        E2m[ju, iu] = conn2
        ne3 = (E2m[i3, j3].astype(np.int8) + E2m[i3, k3]
               + E2m[j3, k3])
        out.update(w3=w3, tri=tri, ne3=ne3, W3=float(np.sum(w3)))
    return out


def census_stats(cs, masses):
    """Sector sums, enrichment, CIs, band table from a census."""
    mm = np.asarray(masses, dtype=np.int64)
    u = np.log(mm.astype(float))
    band1 = np.floor(u / LN2).astype(int)
    w1, w2, conn2 = cs["w1"], cs["w2"], cs["conn2"]
    iu, ju = cs["iu"], cs["ju"]
    W2c = float(np.sum(w2[conn2]))
    W2d = float(np.sum(w2[~conn2]))
    n_c, n_d = int(np.sum(conn2)), int(np.sum(~conn2))
    e2 = ((np.mean(np.abs(w2[conn2])) if n_c else 0.0)
          / max(np.mean(np.abs(w2[~conn2])), 1e-300))
    band2 = np.maximum(band1[iu], band1[ju])
    res = dict(W1=cs["W1"], W2=cs["W2"], W2c=W2c, W2d=W2d,
               n_c=n_c, n_d=n_d, e2=float(e2), delta=cs["delta"])
    sec_c = list(w2[conn2])
    sec_d = list(w2[~conn2])
    bands = {}
    for b, w in zip(band1, w1):
        bands.setdefault(int(b), []).append(float(w))
    for b, w in zip(band2, w2):
        bands.setdefault(int(b), []).append(float(w))
    if "w3" in cs:
        w3, tri, ne3 = cs["w3"], cs["tri"], cs["ne3"]
        conn3 = ne3 >= 2
        mix3 = ne3 == 1
        res.update(W3=cs["W3"], W3c=float(np.sum(w3[conn3])),
                   W3m=float(np.sum(w3[mix3])),
                   W3d=float(np.sum(w3[ne3 == 0])),
                   n3c=int(np.sum(conn3)))
        sec_c += list(w3[conn3])
        sec_d += list(w3[~conn3])
        band3 = np.max(band1[tri], axis=1)
        for b, w in zip(band3, w3):
            bands.setdefault(int(b), []).append(float(w))
    else:
        res.update(W3=0.0, W3c=0.0, W3m=0.0, W3d=0.0, n3c=0)
    sec_c = np.asarray(sec_c)
    sec_d = np.asarray(sec_d)
    res["CIc"] = float(np.sum(np.abs(sec_c))
                       / max(abs(np.sum(sec_c)), 1e-300))
    res["CId"] = float(np.sum(np.abs(sec_d))
                       / max(abs(np.sum(sec_d)), 1e-300))
    res["R"] = cs["delta"] - res["W1"] - res["W2"] - res["W3"]
    res["T"] = res["W1"] + res["W2"] + res["W3"]
    res["conn_share"] = (float(np.sum(np.abs(cs["w2"][conn2])))
                         / max(float(np.sum(np.abs(cs["w2"]))),
                               1e-300))
    res["bands"] = {b: (len(v), float(np.sum(v)),
                        float(np.sum(np.abs(v))))
                    for b, v in sorted(bands.items())}
    return res


# ================================================================= main
def main():
    section("PRIME.CLUSTER.MULT.01 -- connected multiplicative "
            "clusters of the log-pivot (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim; the census lives in the 2-dim corner "
          "compression above the PD floor; typed before the run: "
          "the arch-only base is indefinite, so the margin itself "
          "sits below the expansion floor.")

    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall: no zeta-zero / prime-table symbol "
          "(gcd / divisor arithmetic is the admissible Euler-"
          "product datum)", not bad,
          "found %s" % bad if bad else "clean")

    # ----------------------------------------------------- S1 frame
    section("S1 -- frame, anchors, read convention, margin identity")
    A = {}
    ok_tau = ok_exc = ok_mid = True
    conv = None
    conv_dev = None
    for kz in ANCHORS:
        rr = core.build_window(kz)
        B2 = np.asarray(rr["B"], float)
        Xn = np.asarray(rr["Xn"], float)
        lam = np.asarray(rr["lam"], float)
        uu = np.asarray(rr["uu"], float)
        nv = np.rint(np.exp(uu)).astype(np.int64)
        Amat = np.array([[B2[0, 0], B2[0, 1]], [B2[0, 1], B2[1, 1]]])
        Ee = -Xn  # E_j in (a, c, b) layout so A = B + sum lam E
        S = (lam[:, None] * Ee).sum(axis=0)
        Afull = Amat + np.array([[S[0], S[2]], [S[2], S[1]]])
        ev = np.linalg.eigvalsh(Afull)
        tau = float(ev[0])
        lmax = float(ev[1])
        tau_ah = float(np.linalg.eigvalsh(rr["Ah"])[0])
        lmB = float(np.linalg.eigvalsh(Amat)[0])
        ok_tau &= (abs(tau - TAU_REFS[kz]) / TAU_REFS[kz] <= BAR_TAU
                   and abs(tau - tau_ah) <= 1e-9
                   * max(1.0, abs(tau_ah)))
        ok_exc &= (abs((tau - lmB) - EXC_REFS[kz]) / EXC_REFS[kz]
                   <= BAR_EXC)
        detA = float(np.linalg.det(Afull))
        ok_mid &= abs(detA - tau * lmax) <= 1e-10 * max(1.0,
                                                        abs(detA))
        if conv is None:
            Xr = reads_at(rr, uu)
            sc = max(1.0, float(np.max(np.abs(Xn))))
            dp = float(np.max(np.abs(Xr - Xn))) / sc
            dn = float(np.max(np.abs(Xr + Xn))) / sc
            conv = 1.0 if dp <= dn else -1.0
            conv_dev = min(dp, dn)
        A[kz] = dict(rr=rr, B2=B2, lam=lam, uu=uu, nv=nv, Ee=Ee,
                     tau=tau, lmB=lmB, lmax=lmax)
    check("S1.1 [CONTROL] tau_X refs (rel 1e-4) AND lambda_min(B + "
          "sum lam E) == lambda_min(Ah) (1e-9) on anchors %s"
          % (ANCHORS,), ok_tau)
    check("S1.2 [CONTROL] EXC refs (tau - lambda_min(B), rel 1e-3) "
          "on all anchors -- the certified-ladder excess reproduced "
          "in the cluster frame", ok_exc)
    check("S1.3 [WARD] the margin identity at sigma = 0: det A == "
          "tau_X * lambda_max(A) (rel 1e-10) -- the margin IS the "
          "bottom factor of the pivot determinant", ok_mid)
    check("S1.4 [WARD] read convention: spline reads at the true "
          "positions match shipped Xn with sign %+d (dev %.1e <= "
          "%.0e) -- SCR/EPS reads enter in the same convention"
          % (int(conv), conv_dev, BAR_CONV), conv_dev <= BAR_CONV)
    print("    PD floor typed: lambda_min(B) = %.4f / %.4f / %.4f "
          "< 0 on kz = 9/12/13 -- the sigma = 0 subset lattice is "
          "NOT log-expandable around the arch base; the ladder "
          "below measures the floor."
          % (A[9]["lmB"], A[12]["lmB"], A[13]["lmB"]))

    # -------------------------------------- S2 construction wards
    section("S2 -- THE EXPANSION CONSTRUCTION: exact wards "
            "(sympy + lattice)")
    import sympy as sp
    l1, l2, l3 = sp.symbols("l1 l2 l3")
    Bs = sp.Matrix([[7, 1], [1, 5]])
    E1 = sp.Matrix([[2, 1], [1, 0]])
    E2s = sp.Matrix([[0, 1], [1, 3]])
    E3 = sp.Matrix([[1, -1], [-1, 2]])
    lams = (l1, l2, l3)
    Es = (E1, E2s, E3)

    def g_sym(S):
        M = Bs + sum((lams[j] * Es[j] for j in S), sp.zeros(2, 2))
        return sp.log(M.det())

    gtab = {frozenset(S): g_sym(S)
            for r in range(4) for S in combinations(range(3), r)}
    total = sp.S.Zero
    for r in range(4):
        for C in combinations(range(3), r):
            Cf = frozenset(C)
            for r2 in range(len(C) + 1):
                for S in combinations(C, r2):
                    total += (-1) ** (len(C) - len(S)) \
                        * gtab[frozenset(S)]
    resid = sp.simplify(total - gtab[frozenset((0, 1, 2))])
    check("S2.1 [SYMPY EXACT] the resummation identity on 3 "
          "symbolic events: sum over ALL clusters C of w(C) == "
          "g(full) (telescoping on the Boolean lattice) -- residual "
          "simplifies to %s" % resid, resid == 0)
    b1, b2, e1, e2 = sp.symbols("b1 b2 e1 e2", positive=True)
    w_disc = (sp.log((b1 + l1 * e1) * (b2 + l2 * e2))
              - sp.log((b1 + l1 * e1) * b2)
              - sp.log(b1 * (b2 + l2 * e2)) + sp.log(b1 * b2))
    w_disc_s = sp.simplify(sp.logcombine(w_disc, force=True))
    Mc = Bs + l1 * E1 + l2 * E2s
    w_conn = (sp.log(Mc.det()) - sp.log((Bs + l1 * E1).det())
              - sp.log((Bs + l2 * E2s).det()) + sp.log(Bs.det()))
    w_conn_val = float(w_conn.subs({l1: sp.Rational(1, 3),
                                    l2: sp.Rational(1, 5)}))
    check("S2.2 [SYMPY EXACT -- THE MOEBIUS ELIMINATION] the "
          "block-DISCONNECTED 2-cluster weight is IDENTICALLY zero "
          "(w = %s: the pair term cancels exactly against the "
          "product of 1-clusters) while a CONNECTED pair carries "
          "weight (%.6f != 0 at l = 1/3, 1/5) -- only connected "
          "clusters survive, the genuine cumulant structure"
          % (w_disc_s, w_conn_val),
          w_disc_s == 0 and abs(w_conn_val) > 1e-6)
    d2w = sp.diff(w_conn, l1, l2).subs({l1: 0, l2: 0})
    tr_ref = -(Bs.inv() * E1 * Bs.inv() * E2s).trace()
    check("S2.3 [SYMPY EXACT -- THE CONNECTED CORRELATION TERM] "
          "d^2 w({i,j}) / dl_i dl_j |_0 == -tr(B^{-1} E_i B^{-1} "
          "E_j) (residual %s) -- the cluster weights ARE the "
          "connected correlation terms of the events against the "
          "base" % sp.simplify(d2w - tr_ref),
          sp.simplify(d2w - tr_ref) == 0)
    Bn = np.array([[3.7, 0.0], [0.0, 2.1]])
    f1 = np.array([0.9, 0.0, 0.0])
    f2 = np.array([0.0, 1.3, 0.0])

    def gnum(fs):
        s = sum(fs, np.zeros(3))
        return math.log((Bn[0, 0] + s[0]) * (Bn[1, 1] + s[1])
                        - (Bn[0, 1] + s[2]) ** 2)

    w_syn = gnum([f1, f2]) - gnum([f1]) - gnum([f2]) + gnum([])
    check("S2.4 [FLOAT] synthetic disconnected pair cancels to "
          "machine precision (|w| = %.1e <= 1e-12) while its total "
          "increment %.4f is fully carried by the 1-clusters"
          % (abs(w_syn), gnum([f1, f2]) - gnum([])),
          abs(w_syn) <= 1e-12)

    # 16-event lattice at kz 9
    a9 = A[9]
    lam9, Ee9, nv9 = a9["lam"], a9["Ee"], a9["nv"]
    B29 = a9["B2"]
    F9 = lam9[:, None] * Ee9
    nrm_true = float(np.sum(lam9 * specnorm2(Ee9[:, 0], Ee9[:, 1],
                                             Ee9[:, 2])))
    sig0_9 = 1.0 + max(0.0, -a9["lmB"]) + nrm_true  # provisional
    idxL = np.arange(1 << N_LATTICE)
    bitsm = ((idxL[:, None] >> np.arange(N_LATTICE)) & 1)
    pop = bitsm.sum(axis=1)

    def lattice_orders(sigma):
        FL = F9[:N_LATTICE]
        SA = bitsm @ FL[:, 0]
        SC = bitsm @ FL[:, 1]
        SB = bitsm @ FL[:, 2]
        det = ((B29[0, 0] + sigma + SA) * (B29[1, 1] + sigma + SC)
               - (B29[0, 1] + SB) ** 2)
        tr = (B29[0, 0] + sigma + SA) + (B29[1, 1] + sigma + SC)
        if not (np.all(det > 0) and np.all(tr > 0)):
            return None
        g = np.log(det)
        w = g.copy()
        for i in range(N_LATTICE):
            bit = 1 << i
            has = (idxL & bit) != 0
            w[has] -= w[idxL[has] ^ bit]
        resum = abs(float(np.sum(w)) - float(g[-1]))
        Wk = np.array([float(np.sum(w[pop == k]))
                       for k in range(N_LATTICE + 1)])
        return resum, Wk, float(g[-1] - g[0])

    lat0 = lattice_orders(sig0_9)
    resum0, Wk0, dl0 = lat0
    check("S2.5 [THE RESUMMATION WARD, NUMERIC] kz 9 sub-window "
          "(first %d events, masses %d..%d, ALL 2^%d subsets): "
          "|sum_C w(C) - g(full)| = %.2e <= %.0e * scale -- the "
          "full expansion resums to the log-pivot exactly"
          % (N_LATTICE, int(nv9[0]), int(nv9[N_LATTICE - 1]),
             N_LATTICE, resum0, BAR_RESUM),
          resum0 <= BAR_RESUM * max(1.0, abs(dl0)))
    nz = [k for k in range(1, 8) if abs(Wk0[k]) > 0]
    ratios0 = [abs(Wk0[k + 1] / Wk0[k]) for k in nz
               if abs(Wk0[k]) > 1e-300 and k + 1 <= N_LATTICE]
    rho_ord0 = float(np.median(ratios0)) if ratios0 else 0.0
    print("    lattice order histogram at sigma_0 = %.3f "
          "(sub-window Delta = %+.5f):" % (sig0_9, dl0))
    for k in range(1, 9):
        print("      order %2d: W_k = %+12.3e   share %8.2e"
              % (k, Wk0[k], Wk0[k] / dl0 if dl0 else float("nan")))
    print("      orders 9..16 total: %+.3e; geometric ratio "
          "rho_ord (median |W_{k+1}/W_k|, k = 1..6) = %.4f"
          % (float(np.sum(Wk0[9:])), rho_ord0))

    # ------------------------------------- S3 sigma ladder + census
    section("S3 -- THE CENSUS: sigma ladder to the PD floor, "
            "orders <= 3, connectivity, bands (kz 9)")
    # build the three combs per anchor
    combs = {}
    for kz in ANCHORS:
        a = A[kz]
        rr = a["rr"]
        ka = len(a["lam"])
        uu_s = np.asarray(core.build_window(kz,
                                            scramble_seed=SCR_SEED)
                          ["uu"], float)
        E_scr = -conv * reads_at(rr, uu_s)
        me = sum2sq_free_support(ka, X_EPS)
        E_eps = -conv * reads_at(rr, np.log(np.array(me, float)))
        combs[kz] = {
            "TRUE": (a["lam"][:, None] * a["Ee"], a["nv"]),
            "SCR": (a["lam"][:, None] * E_scr, a["nv"]),
            "EPS": (a["lam"][:, None] * E_eps,
                    np.array(me, dtype=np.int64)),
        }
    sig_star = {}
    census_at_star = {}
    evo9 = []
    for kz in ANCHORS:
        a = A[kz]
        ka = len(a["lam"])
        do3 = math.comb(ka, 3) <= N3_MAX
        nrm_max = max(
            float(np.sum(specnorm2(F[:, 0], F[:, 1], F[:, 2])))
            for F, _m in combs[kz].values())
        sig0 = 1.0 + max(0.0, -a["lmB"]) + nrm_max

        def all_census(sigma):
            out = {}
            for name, (F, mm) in combs[kz].items():
                cs = cluster_census(a["B2"], F, mm, sigma,
                                    do_triples=do3)
                if cs is None:
                    return None
                out[name] = cs
            return out

        sig = sig0
        res = all_census(sig)
        assert res is not None, "sigma_0 not PD -- bound violated"
        lo_bad = None
        while True:
            nxt = sig / 2.0
            r2 = all_census(nxt)
            if r2 is None:
                lo_bad = nxt
                break
            sig, res = nxt, r2
            if kz == 9:
                evo9.append((sig, census_stats(res["TRUE"],
                                               combs[9]["TRUE"][1])))
            if sig < 1e-6 * sig0:
                break
        if lo_bad is not None:
            for _ in range(N_BISECT):
                mid = 0.5 * (sig + lo_bad)
                r2 = all_census(mid)
                if r2 is None:
                    lo_bad = mid
                else:
                    sig, res = mid, r2
        sig_star[kz] = (sig0, sig)
        census_at_star[kz] = res
        if not do3:
            print("    kz=%d: C(ka,3) = %d > cap %d -- order-3 "
                  "census SKIPPED (typed)"
                  % (kz, math.comb(ka, 3), N3_MAX))

    sig0_9r, sigs9 = sig_star[9]
    st9 = census_stats(census_at_star[9]["TRUE"],
                       combs[9]["TRUE"][1])
    print("    kz 9: sigma_0 = %.4f -> sigma* = %.6f (PD floor; "
          "|lambda_min(B)| = %.4f; base bottom eig at sigma*: "
          "%+.4e); the margin tau_X = %.4e sits BELOW the floor "
          "by construction" % (sig0_9r, sigs9, -a9["lmB"],
                               sigs9 + a9["lmB"], a9["tau"]))
    print("\n    TRUE-comb census evolution along the sigma "
          "ladder (kz 9, orders <= 3):")
    print("    %-10s %-11s %-11s %-11s %-11s %-8s %-6s %-8s %-8s"
          % ("sigma", "Delta", "W1", "W2", "W3", "|R|/|D|", "E2",
             "CI_conn", "CI_disc"))
    for sg, st in evo9 + [(sigs9, st9)]:
        print("    %-10.4f %+-11.4e %+-11.4e %+-11.4e %+-11.4e "
              "%-8.1e %-6.2f %-8.2f %-8.2f"
              % (sg, st["delta"], st["W1"], st["W2"], st["W3"],
                 abs(st["R"]) / max(abs(st["delta"]), 1e-300),
                 st["e2"], st["CIc"], st["CId"]))
    order_share = abs(st9["R"]) / max(abs(st9["delta"]), 1e-300)
    lat_s = lattice_orders(sigs9)
    if lat_s is not None:
        _rs, WkS, dlS = lat_s
        ratiosS = [abs(WkS[k + 1] / WkS[k]) for k in range(1, 7)
                   if abs(WkS[k]) > 1e-300]
        rho_ordS = float(np.median(ratiosS)) if ratiosS else 0.0
        print("    lattice at sigma*: orders 1..6 = %s; rho_ord = "
              "%.4f" % (["%+.2e" % WkS[k] for k in range(1, 7)],
                        rho_ordS))
    else:
        rho_ordS = rho_ord0
        print("    lattice at sigma*: NOT PD (sub-window loses "
              "positivity before the census set does) -- rho_ord "
              "taken from sigma_0 (typed)")
    order_ok = order_share <= BAR_ORDER or rho_ordS <= BAR_RHO
    check("S3.1 [ORDER HISTOGRAM] at sigma* the remainder beyond "
          "order 3 is |R|/|Delta| = %.3e (bar %.2f) and the exact "
          "sub-window ratio rho_ord = %.3f (bar %.2f): %s"
          % (order_share, BAR_ORDER, rho_ordS, BAR_RHO,
             "effectively finite-order / geometrically decaying -- "
             "the control problem is finite-dimensional per band"
             if order_ok else
             "the series is NOT effectively finite-order at the "
             "floor -- typed"), order_ok)
    conn_ok = (st9["e2"] >= BAR_E2
               and st9["CIc"] <= st9["CId"] / BAR_CI_RATIO)
    check("S3.2 [THE FROZEN QUESTION -- CONNECTIVITY] order-2 "
          "enrichment E2 = %.3f (connected pairs %d / %d, bar "
          ">= %.1f) and sector cancellation CI_conn = %.2f vs "
          "CI_disc = %.2f (bar: conn <= disc/%.0f): the margin %s"
          % (st9["e2"], st9["n_c"], st9["n_c"] + st9["n_d"],
             BAR_E2, st9["CIc"], st9["CId"], BAR_CI_RATIO,
             "LIVES in the connected sector" if conn_ok else
             "does NOT concentrate on the connected sector -- the "
             "cluster weights are position-geometric at this "
             "grade"), conn_ok)
    print("    sector sums at sigma*: W2_conn = %+.4e  W2_disc = "
          "%+.4e  W3_conn = %+.4e  W3_mixed = %+.4e  W3_disc = "
          "%+.4e  (tau_X = %.3e)"
          % (st9["W2c"], st9["W2d"], st9["W3c"], st9["W3m"],
             st9["W3d"], a9["tau"]))
    # per-prime connected aggregates (small primes exact)
    cs9 = census_at_star[9]["TRUE"]
    mm9 = combs[9]["TRUE"][1]
    spf9 = {}
    for m in mm9:
        m0 = int(m)
        p = 2
        while p * p <= m0 and m0 % p:
            p += 1
        spf9[m0] = p if m0 % p == 0 else m0
    prime_agg = {}
    for w, i, j, c in zip(cs9["w2"], cs9["iu"], cs9["ju"],
                          cs9["conn2"]):
        if c:
            p = spf9[int(mm9[i])]
            s, sa, n = prime_agg.get(p, (0.0, 0.0, 0))
            prime_agg[p] = (s + float(w), sa + abs(float(w)), n + 1)
    print("    per-prime connected 2-cluster aggregates (small "
          "primes exact):")
    for p in sorted(prime_agg):
        s, sa, n = prime_agg[p]
        print("      p = %-3d  n_pairs = %-3d  sum w2 = %+11.4e  "
              "sum |w2| = %10.4e" % (p, n, s, sa))
    topi = np.argsort(-np.abs(cs9["w2"]))[:6]
    print("    heaviest 2-clusters: %s"
          % ["(%d,%d)%s %+0.2e"
             % (mm9[cs9["iu"][t]], mm9[cs9["ju"][t]],
                "*" if cs9["conn2"][t] else " ",
                cs9["w2"][t]) for t in topi])
    bl = st9["bands"]
    sum_abs_bands = sum(abs(s) for _n, s, _sa in bl.values())
    band_ok = sum_abs_bands <= BAR_BAND * max(abs(st9["T"]), 1e-300)
    print("    dyadic band table (band = floor(max u / ln 2), "
          "orders 1..3, kz 9, sigma*):")
    print("      %-5s %-7s %-13s %-13s %-9s"
          % ("band", "n_C", "sum w", "sum |w|", "coherence"))
    for b, (n, s, sa) in bl.items():
        print("      %-5d %-7d %+-13.4e %-13.4e %-9.3f"
              % (b, n, s, sa, abs(s) / max(sa, 1e-300)))
    check("S3.3 [BAND SUMMABILITY] sum_b |S_b| = %.4e vs %.0f x "
          "|T| = %.4e: %s"
          % (sum_abs_bands, BAR_BAND,
             BAR_BAND * abs(st9["T"]),
             "the cluster series is band-wise summable (coherent "
             "within dyadic bands)" if band_ok else
             "band sums carry heavy cancellation ACROSS bands -- "
             "the typed absolute-divergence limit"), band_ok)

    # ------------------------------------------ S4 discriminator
    section("S4 -- THE THREE-COMB DISCRIMINATOR (anchors, common "
            "sigma*)")
    scr_ok = eps_ok = True
    e2_tab = {}
    for kz in ANCHORS:
        rowstats = {}
        for name in ("TRUE", "SCR", "EPS"):
            cs = census_at_star[kz][name]
            mm = combs[kz][name][1]
            rowstats[name] = census_stats(cs, mm)
        e2_tab[kz] = rowstats
        et, es, ee = (rowstats[n]["e2"] for n in ("TRUE", "SCR",
                                                  "EPS"))
        cst, css, cse = (rowstats[n]["conn_share"]
                         for n in ("TRUE", "SCR", "EPS"))
        dens = {n: rowstats[n]["n_c"]
                / max(rowstats[n]["n_c"] + rowstats[n]["n_d"], 1)
                for n in ("TRUE", "SCR", "EPS")}
        print("    kz=%d (sigma* = %.4f):" % (kz, sig_star[kz][1]))
        print("      %-5s %-7s %-11s %-11s %-9s %-9s %-9s"
              % ("comb", "E2", "connshare", "edgedens", "CI_c",
                 "CI_d", "Delta"))
        for n in ("TRUE", "SCR", "EPS"):
            r = rowstats[n]
            print("      %-5s %-7.3f %-11.4f %-11.4f %-9.2f %-9.2f "
                  "%+9.3e"
                  % (n, r["e2"], r["conn_share"], dens[n],
                     r["CIc"], r["CId"], r["delta"]))
        scr_ok &= es <= et / 3.0
        share_ratio = cse / max(cst, 1e-300)
        eps_ok &= (abs(math.log2(max(ee, 1e-300)
                                 / max(et, 1e-300))) >= 1.0
                   or share_ratio >= 2.0 or share_ratio <= 0.5)
    check("S4.1 [SCRAMBLE] the connected enrichment collapses "
          "under the mass-fixed scramble on all anchors (E2_scr <= "
          "E2_true / 3): %s -- %s"
          % (scr_ok,
             "the cluster structure is carried by the positions-"
             "with-arithmetic, not by the mass labels alone"
             if scr_ok else
             "the scramble does NOT collapse the enrichment: the "
             "connected weights were never arithmetic to begin "
             "with (position-geometry only)"), scr_ok)
    check("S4.2 [EPSTEIN h=2] the connected-cluster fingerprint "
          "differs from the true comb on all anchors (E2 factor 2 "
          "or conn-share factor 2): %s -- its divisibility graph "
          "carries the class-group obstruction (composites without "
          "their factors)" % eps_ok, eps_ok)

    # --------------------------------------------------- S5 verdict
    section("V -- FROZEN VERDICT + the control-problem shape / "
            "closure + honest consequence")
    controls_ok = not FAILS or all(
        f.startswith(("S3.", "S4.")) for f in FAILS)
    if (order_ok and conn_ok and band_ok and scr_ok and eps_ok):
        verdict = "CLUSTERS-CARRY"
    elif st9["e2"] < BAR_E2_LOW:
        verdict = "CLUSTERS-DIFFUSE"
    else:
        verdict = "CLUSTERS-PARTIAL"
    print("\n  VERDICT: %s   [order: %s | connectivity: %s | "
          "bands: %s | scramble: %s | epstein: %s | controls: %s]"
          % (verdict, "OK" if order_ok else "FAIL",
             "OK" if conn_ok else "FAIL",
             "OK" if band_ok else "FAIL",
             "OK" if scr_ok else "FAIL",
             "OK" if eps_ok else "FAIL",
             "OK" if controls_ok else "FAIL"))
    if verdict == "CLUSTERS-CARRY":
        print("""
  THE FINDING (report prominently): THE CONNECTED SECTOR CARRIES.
  The log-pivot's cluster expansion (exact cumulant lattice, wards
  S2) concentrates on the multiplicatively connected clusters, the
  concentration dies under the mass-fixed scramble, and the h = 2
  Epstein comb shows a distinct connected fingerprint -- the first
  quantitative object in the program that sees the ALL-ORDERS
  arithmetic beyond pair statistics.  THE CONTROL-PROBLEM SHAPE
  (typed, not claimed): a cofinal theorem needs per-band bounds on
  the connected cluster sums; the order-1 band sums are
  Lambda-weighted event masses per dyadic band (Chebyshev /
  Mertens-type sums: sum_{p <= x} log p / p^s-grade, classical and
  unconditional); the connected order-2 sums are same-prime
  geometric ladders (per-prime tails summable exactly, Mertens
  controls the sum over p); the DISCONNECTED sector needs a
  quadratic-form bound of large-sieve / Selberg-weight type per
  band pair.  THE HONEST GAP: (i) all bounds must be uniform in
  the band index along the ladder; (ii) the expansion lives above
  the PD floor sigma_c ~ |lambda_min(B)| while the margin sits at
  sigma = 0 -- crossing the floor (analytic continuation of the
  resummed series, or a floor-free pivot) IS the remaining control
  problem, not covered by the census.""")
    elif verdict == "CLUSTERS-DIFFUSE":
        print("""
  THE FINDING (the honest closure): NO CONNECTED CONCENTRATION.
  The cluster expansion exists and resums exactly (wards S2 all
  pass -- the construction is sound), but the weights ignore the
  divisibility graph: the enrichment of multiplicatively connected
  pairs is statistically absent, i.e. the 2-cluster weights are
  POSITION-GEOMETRIC (they measure spline-read overlap in the
  2-dim corner, which knows |u_i - u_j|, not p_i = p_j).  TYPED
  CLOSURE: the all-orders route THROUGH THIS PIVOT closes -- the
  corner compression to 2x2 destroys the cluster-arithmetic
  before the expansion can see it; any surviving all-orders route
  must expand an object that is not a 2-dim compression (the full
  Toeplitz determinant, or the per-prime block structure) -- a
  different construction, not a parameter change on this one.
  The GUE-strand statement sharpens: not only do pair statistics
  saturate; the pairwise CLUSTER data of the deployed corner is
  equally blind to multiplicativity.""")
    else:
        print("""
  THE FINDING: PARTIAL -- the bars split (see the flag list in the
  verdict line).  The failing bars localize exactly what the
  all-orders route lacks at this grade; the passing bars stand as
  measured structure.  Typed per bar above; no promotion.""")
    print("""
  HONEST FRAME: the census lives above the PD floor of the
  arch-indefinite base and inside a 2-dim corner compression; a
  favorable census is NOT a positivity statement along the ladder,
  and an unfavorable one closes only this pivot's cluster route.
  Nothing here is an RH-relevant bound.  NO RH claim.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

_SRC_KERNELFIELD = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""cone_kernel_field_probe -- PRIME.CELLCONE.KERNELFIELD.01
(EXPLORATION ONLY, experiments/; direct follow-up to the CONE-BROKEN
verdict of cell_cone_transport_probe / PRIME.CELLCONE.TRANSPORT.01,
2026-08-07 -- package D is NOT buried yet: two stages in one probe).

PARENT FINDINGS (cited, machinery imported READ-ONLY, bit for bit):
the completed-cell flow A_k = (B - S_pnt) + sum_{j<=k}(Chat_j -
lam_j Xhat_j) telescopes exactly but EXITS the fixed Lorentz cone on
67/67 rungs under both groupings, first exit at the n = 2 cell,
endpoint back inside on 67/67; G1 (Stieltjes) worst relative depth
shrinks along the ladder (-3.9e-2 -> -1.9e-3), G2 (mass-matched) has
deep long excursions; RAY-EDGE-CONFIRMED; the Epstein control did
NOT break (inverted signature: the dips are the true comb's own
psi(x) - x fluctuation).

STAGE 1 -- THE FINITE PRIME KERNEL (the 5-step protocol):
  (1) per rung and grouping, the exact violation positions (states
      with lambda_min <= 0 after a cell) and the LAST violating
      prime-power block P0(rung);
  (2) the renormalized base A_kernel = A_0 + sum_{n <= P0}(cells) is
      EXACT (it is the running state at the last violating cell --
      the flow is additive, so the per-rung tail-clean statement is
      BY CONSTRUCTION; stated openly, verified numerically);
  (3) the tail from the renormalized base preserves the cone
      per rung (by construction; asserted);
  (4) THE DECISIVE MEASUREMENT: does P0 stabilize or wander across
      the 67-rung depth ladder?  Typed laws: P0 vs X = e^{2 alpha}
      (log-log slope), u_{P0}/(2 alpha) (median + Kendall vs alpha),
      violation count vs K; plus the PREDECLARED depth-resolved
      census: violation at relative depth d iff lambda_min /
      lambda_max < -d for d in {0(strict), 1e-3, 1e-2, 1e-1} and the
      tau-relative census (lambda_min <= -tau_rung) -- the parent
      showed the strict late violations are thinner than the
      certified endpoint margin, so the depth-resolved kernel is the
      honest renormalization question;
  (5) KILL only if the violation position wanders unboundedly:
      frozen WANDER criterion = [median u_{P0}/(2 alpha) >= 0.5] AND
      [P0 at the top rung > P0_CAP]; frozen KERNEL-STABLE criterion
      = [max over rungs of strict P0 <= P0_CAP = 100 (in n)].
  Fixed-kernel prediction test (report): P0* = max strict P0 over
  the smallest third of the ladder; count tail violations n > P0*
  on the upper two thirds.

STAGE 2 -- THE MOVING LORENTZ CONE FIELD (F3):
  GEOMETRIC FACT stated up front (forces the design): congruence-
  image cones are USELESS here -- for any invertible 2x2 T the set
  {T X T^T : X >= 0} IS the PSD cone (Sylvester), so a moving cone
  must act on the Lorentz 3-vectors u = L(A) with G_m in GL(3) NOT
  of (scaled) Lorentz type.  Frozen field family: CIRCULAR TUBE
  CONES K_m = G_m L+ with G_m = R_m diag(1, tan th_m, tan th_m),
  R_m the rotation taking e_t to the past-only axis, th_m the
  half-opening; membership u_m in K_m <=> angle(u_m, axis_m) <=
  th_m.  cond(G_m) = max(tan th_m, cot th_m), tracked, bar
  COND_BAR = 100.  TWO PREDECLARED FIELD RULES (past-only):
    A (polar frame of the running state): axis_m = u_{m-1}/|u_{m-1}|
      (the previous state direction -- the polar frame of the
      renormalized running state, history only);
    B (mu*log-weighted frame): axis_m = normalized trailing
      mass-weighted mean sum w_j u_j over the last NW = 32 states
      j < m, w_j = Lambda(n_j)/sqrt(n_j) (the multiplicative weights
      anchor the frame -- heavier arithmetic cells count more; the
      base state carries the mean mass).
  ADAPTIVE OPENING (same rule both fields, frozen): th_m =
  clip(ANG_FAC x max of the trailing NW-window of past angle
  readings (rule A: increments angle(u_j, u_{j-1}); rule B: axis
  angles angle(u_j, axis_j)), ANG_MIN = 1 deg, 89 deg); a trailing
  window (not the all-time max) so that the warm-up spikes EXPIRE
  and the test is not vacuous.  WARM-UP: cells 1..NWARM = 12 (the
  parent's small-n dip zone n = 2..19) are the absorbed finite
  kernel -- measured, not gated; gated transport = cells NWARM+1..K.
  FIELD-RELATIVE J-DEFECT per gated cell: fdef_m = angle_m/th_m - 1
  (<= 0 required); FIELD TRANSPORTS iff zero gated violations on
  all rungs AND max cond <= COND_BAR.
  CAUSAL FENCE (no-tau-peeking, structural): th_m and axis_m are
  computed from index slices [:m] ONLY; asserted by explicit
  recomputation at frozen spot cells; tau_m / the current sign never
  enters the field construction (the gate reads only the angle
  history).  The set inclusion Phi_m(K_m) <= K_{m+1} is measured on
  the parent's congruence spot cells via the conjugated map Psi_m =
  G_{m+1}^{-1} Phi_m G_m over NRAY = 64 frozen boundary rays
  (report-only; the per-cell gate is state membership).

CONTROLS (frozen fire rules):
  stage 1: equal-weight scramble and wrong pole normalization
    (x WRONG_FAC = 2, self-consistent base) on the stride-5 subset:
    fire iff [strict violation count median >= CTRL_FAC = 3 x the
    real median] OR [base out of cone];
  stage 2 (rule A, G1, stride-5 subset): equal-weight scramble and
    wrong normalization must fire: [gated violation count median >=
    CTRL_FAC x max(real median, 1)] OR [median max post-warm-up
    increment >= CTRL_FAC x real median]; EPSTEIN x^2+5y^2 is a
    TYPED two-sided separation control (parent's inverted-signature
    caveat): DISTINGUISHABLE iff the median max post-warm-up
    increment differs from the real one by factor >= EP_SEP = 3 in
    EITHER direction, else control surprise (typed, does not gate).

VERDICT ENUM (frozen, decision order):
  INVALID           -- a ward fails (no structural claim, exit 1).
  KERNEL-TAIL-CLEAN -- strict kernel bounded (max P0 <= P0_CAP) for
      >= 1 grouping AND stage-1 must-breaks fire: the classical
      structure 'finite arithmetic kernel + cone-preserving tail'
      exists.
  FIELD-TRANSPORTS  -- stage 1 fails but >= 1 (field rule x
      grouping) achieves zero gated violations with cond <= COND_BAR
      AND stage-2 must-breaks fire: the moving relational cone
      carries the flow.
  BOTH-PARTIAL      -- any of (typed): (i) strict kernel bounded on
      >= 0.5 of rungs; (ii) the depth-1e-2 kernel bounded (max
      depth-resolved P0 <= P0_CAP on all rungs) -- the kernel exists
      after depth renormalization; (iii) a field rule reaches
      overall gated violation fraction <= 1e-3 with bounded cond;
      (iv) a passing stage would have fired but its must-break
      control did not (control surprise cap).
  KERNEL-WANDERS    -- the kill: strict positions wander (frozen
      criterion), no depth-renormalized kernel, no field transports.
NO RH claim.  Finite measurement on 67 rungs; nothing here bounds
the infinite ladder.  Writes no files; nothing outside experiments/.

FIREWALL: parent probe + v563 imported READ-ONLY (construction bit
for bit); mpmath only via the parent constant C_TH; no zeta zero
read (AST-checked, banned ids as parent); NO RNG anywhere; runtime
cap 1800 s predeclared.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/cone_kernel_field_probe.py
"""

import ast
import hashlib
import inspect
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import cell_cone_transport_probe as parent     # noqa: E402 (READ-ONLY)

FROZEN_SPEC = """\
PRIME.CELLCONE.KERNELFIELD.01 spec v1 (2026-08-07, frozen before the
run).  Ladder/objects/groupings = parent PRIME.CELLCONE.TRANSPORT.01
verbatim (67 rungs, Ah = B - S, A_0 = B - S_pnt, G1 Stieltjes / G2
mass-matched completed cells; parent module imported read-only).
WARDS (must pass, else INVALID): tau refs kz 9/12/13 rel <= 1e-4;
envelope min e1 >= 4.335*0.999; telescoping rel <= 1e-9 per rung per
grouping; parent regression: cone exit on 67/67 rungs for BOTH
groupings.  STAGE 1: violation = state after cell with lambda_min <=
0 (strict); P0(rung) = n of last violating cell; depth-resolved
censuses at rel depth lambda_min/lambda_max < -d, d in {1e-3, 1e-2,
1e-1}, plus tau-relative (lambda_min <= -tau_rung); laws: log P0 vs
2 alpha slope, u_P0/(2 alpha) median + Kendall, count vs K;
KERNEL-STABLE iff max strict P0 <= P0_CAP = 100 (in n); WANDER iff
median u_P0/(2 alpha) >= 0.5 AND top-rung P0 > P0_CAP; fixed-kernel
prediction: P0* = max strict P0 over the smallest third (alpha
order), tail violations n > P0* counted above.  STAGE 2: tube field
K_m = cone(axis_m, th_m); rule A axis = u_{m-1} direction; rule B
axis = trailing NW = 32 mass-weighted mean (w = Lambda/sqrt(n), base
weight = mean mass); th_m = clip(ANG_FAC = 2.0 x trailing-NW-window
max of past angle readings, ANG_MIN = 1 deg, 89 deg); warm-up NWARM
= 12 cells (measured, not gated); violation iff angle_m > th_m on a
gated cell; fdef = angle/th - 1; cond = max(tan th, cot th) <=
COND_BAR = 100; causal fence asserted at spot cells [NWARM+1, K/2,
K-1]; FIELD ok iff zero gated violations all rungs AND cond bound.
Psi-inclusion on parent spot cells over NRAY = 64 boundary rays =
report-only.  CONTROLS: stride 5; stage-1 fire = [strict count
median >= 3x real] OR [base out]; stage-2 fire (rule A, G1) =
[gated count median >= 3x max(real,1)] OR [median max post-warm
increment >= 3x real]; Epstein = typed two-sided separation, factor
EP_SEP = 3, does not gate.  VERDICT order: INVALID; KERNEL-TAIL-
CLEAN (strict kernel bounded >= 1 grouping + stage-1 fires);
FIELD-TRANSPORTS (>= 1 rule x grouping clean + cond ok + stage-2
fires); BOTH-PARTIAL ((i) strict kernel bounded on >= 0.5 rungs,
(ii) depth-1e-2 kernel bounded all rungs, (iii) field violation
fraction <= 1e-3 with cond ok, or (iv) control-surprise cap);
KERNEL-WANDERS else.  No prediction frozen for stage outcomes.
NO RH claim; writes nothing.
"""

STRIDE = 5
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
TAU_REF_REL = 1.0e-4
ENV_C = 4.335
ENV_GUARD = 0.999
WARD_REL = 1.0e-9
P0_CAP = 100
DEPTHS = (1.0e-3, 1.0e-2, 1.0e-1)
NWARM = 12
NW = 32
ANG_FAC = 2.0
ANG_MIN_DEG = 1.0
ANG_MAX_DEG = 89.0
COND_BAR = 100.0
CTRL_FAC = 3.0
EP_SEP = 3.0
NRAY = 64
WRONG_FAC = 2.0
KEN_BAR = 0.8
RUNTIME_CAP = 1800.0
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime", "find_zeros",
              "second_sheet_zero")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in BANNED_IDS:
                return False
    return True


def kendall_tau(x, y):
    n = len(x)
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (x[j] - x[i]) * (y[j] - y[i])
            if s > 0:
                conc += 1
            elif s < 0:
                disc += 1
    return (conc - disc) / max(n * (n - 1) // 2, 1)


def ols_loglog(x, y):
    lx = np.log(np.asarray(x, float))
    ly = np.log(np.abs(np.asarray(y, float)))
    b, q = np.polyfit(lx, ly, 1)
    pred = b * lx + q
    r2 = 1.0 - float(((ly - pred) ** 2).sum()) \
        / max(float(((ly - ly.mean()) ** 2).sum()), 1e-300)
    return float(b), r2


def uvecs_of(ps):
    """(K+1, 3) Lorentz state vectors from a parent path_stats dict."""
    t = ps["a11"] + ps["a22"]
    x = ps["a11"] - ps["a22"]
    y = 2.0 * ps["a12"]
    return np.stack([t, x, y], axis=1)


def angles_between(U, V):
    """Per-row angle in degrees between two (n,3) arrays."""
    nu = np.linalg.norm(U, axis=1)
    nv = np.linalg.norm(V, axis=1)
    c = np.einsum("ij,ij->i", U, V) / np.maximum(nu * nv, 1e-300)
    return np.degrees(np.arccos(np.clip(c, -1.0, 1.0)))


def trailing_max(arr, win):
    """max over the last `win` entries STRICTLY BEFORE each index
    (past-only); -inf where no history exists."""
    pad = np.concatenate([np.full(win, -np.inf), np.asarray(arr,
                                                            float)])
    sw = np.lib.stride_tricks.sliding_window_view(pad, win)
    # sw[i] = pad[i : i+win] = arr[i-win : i] -> past-only at index i
    return sw[:len(arr) + 1].max(axis=1)[:len(arr) + 1]


# ------------------------------------------------- the two field rules
def field_A_axes(U):
    """Rule A: axis_m = direction of u_{m-1} (PAST-only).  Input U =
    (K+1,3) states; output axes for cells m = 1..K as (K,3)."""
    return U[:-1]


def field_B_axes(U, w):
    """Rule B: axis_m = trailing NW-window mass-weighted mean of the
    states j < m (PAST-only); w = per-state weights (w[0] = base
    weight, w[j] = Lambda(n_j)/sqrt(n_j))."""
    K1 = len(U)
    cs = np.vstack([np.zeros(3), np.cumsum(w[:, None] * U, axis=0)])
    cw = np.concatenate([[0.0], np.cumsum(w)])
    m = np.arange(1, K1)                       # cells 1..K
    lo = np.maximum(m - NW, 0)
    num = cs[m] - cs[lo]
    den = cw[m] - cw[lo]
    return num / np.maximum(den[:, None], 1e-300)


def field_run(U, axes_rule, w=None):
    """One field pass: angle readings, past-only adaptive opening,
    gated violations.  Returns the per-cell arrays + summary."""
    if axes_rule == "A":
        axes = field_A_axes(U)
    else:
        axes = field_B_axes(U, w)
    ang = angles_between(U[1:], axes)          # angle reading, cell m
    tmax = trailing_max(ang, NW)[:-1]          # past-only, index m
    th = np.clip(ANG_FAC * tmax, ANG_MIN_DEG, ANG_MAX_DEG)
    fdef = ang / th - 1.0
    gated = np.arange(len(ang)) >= NWARM       # cells NWARM+1..K
    viol = gated & (ang > th)
    tanth = np.tan(np.radians(th[gated]))
    cond = (np.max(np.maximum(tanth, 1.0 / tanth))
            if gated.any() else 1.0)
    return dict(ang=ang, th=th, fdef=fdef, viol=viol, gated=gated,
                nviol=int(viol.sum()), ngate=int(gated.sum()),
                worst_fdef=float(np.max(fdef[gated]))
                if gated.any() else float("-inf"),
                max_inc=float(np.max(ang[gated]))
                if gated.any() else 0.0,
                cond=float(cond))


def causal_assert(U, rule, w, res):
    """Recompute th at frozen spot cells from explicit [:m] slices --
    the structural no-peeking assertion."""
    K = len(U) - 1
    spots = [NWARM + 1, K // 2, K - 1]
    for m in spots:                            # cell index 1-based m+1
        ang_hist = res["ang"][:m]              # readings of cells <= m
        tm = float(np.max(ang_hist[-NW:])) if len(ang_hist) else -np.inf
        th_ref = min(max(ANG_FAC * tm, ANG_MIN_DEG), ANG_MAX_DEG)
        if not math.isclose(th_ref, float(res["th"][m]),
                            rel_tol=1e-12, abs_tol=1e-12):
            return False
    return True


def rot_to(axis):
    """SO(3) rotation taking e_t = (1,0,0) to the unit axis."""
    a = axis / max(np.linalg.norm(axis), 1e-300)
    e = np.array([1.0, 0.0, 0.0])
    v = np.cross(e, a)
    c = float(e @ a)
    s = float(np.linalg.norm(v))
    if s < 1e-14:
        return np.eye(3) if c > 0 else np.diag([-1.0, -1.0, 1.0])
    vx = np.array([[0.0, -v[2], v[1]], [v[2], 0.0, -v[0]],
                   [-v[1], v[0], 0.0]])
    return np.eye(3) + vx + vx @ vx * ((1.0 - c) / (s * s))


def G_of(axis, th_deg):
    return rot_to(axis) @ np.diag([1.0, math.tan(math.radians(th_deg)),
                                   math.tan(math.radians(th_deg))])


def main():
    spec_hash = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()
    fa_hash = hashlib.sha256(
        inspect.getsource(field_A_axes).encode()).hexdigest()
    fb_hash = hashlib.sha256(
        inspect.getsource(field_B_axes).encode()).hexdigest()
    fr_hash = hashlib.sha256(
        inspect.getsource(field_run).encode()).hexdigest()
    print("=" * 78)
    print("PRIME.CELLCONE.KERNELFIELD.01 -- finite prime kernel + "
          "moving Lorentz cone field")
    print("=" * 78)
    print(FROZEN_SPEC)
    print("SPEC sha256       : %s" % spec_hash)
    print("field A sha256    : %s" % fa_hash)
    print("field B sha256    : %s" % fb_hash)
    print("field gate sha256 : %s" % fr_hash)
    print("parent G1/G2 sha256 (imported): %s / %s"
          % (hashlib.sha256(inspect.getsource(
              parent.breaks_G1).encode()).hexdigest()[:16],
             hashlib.sha256(inspect.getsource(
                 parent.breaks_G2).encode()).hexdigest()[:16]))

    # ============================================================== S0
    print("\nS0 -- firewall")
    check("S0.AST no zero/prime-table loader (banned ids absent); "
          "parent + v563 read-only; NO RNG",
          ast_zero_firewall(__file__))

    # ============================================================== S1
    print("\nS1 -- ladder + wards (parent construction, bit for bit)")
    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == parent.ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        rows.append(dict(rr=rr, kz=kz, h=rr["h"], alpha=rr["alpha"],
                         tau=parent.eig2_min(rr["Ah"])))
    rows.sort(key=lambda w: w["alpha"])
    print("    %d rungs, alpha %.3f..%.3f" % (len(rows),
                                              rows[0]["alpha"],
                                              rows[-1]["alpha"]))
    ref_ok = all(abs(parent.eig2_min(core.build_window(kz)["Ah"])
                     - tr) / tr <= TAU_REF_REL
                 for kz, tr in TAU_REFS.items())
    check("S1.REF tau references kz 9/12/13 reproduce (bar %.0e)"
          % TAU_REF_REL, ref_ok)

    env_min = float("inf")
    tel_worst = 0.0
    exit_ok = True
    for w in rows:
        rr = w["rr"]
        edges, reads = parent.pnt_grid(rr)
        w["edges"], w["reads"] = edges, reads
        S_pnt = parent.tri_mat(parent.cum_reads(
            edges, reads, [2.0 * rr["alpha"]])[0])
        w["S_pnt"] = S_pnt
        A0 = rr["B"] - S_pnt
        w["A0"] = A0
        w["tau_pnt"] = parent.eig2_min(A0)
        env_min = min(env_min, (w["tau"] / w["tau_pnt"])
                      * w["h"] ** 1.5)
        uu, lam, Xn = rr["uu"], rr["lam"], rr["Xn"]
        w["mm"] = 2.0 * lam
        w["nn"] = np.rint(np.exp(uu)).astype(np.int64)
        for g in ("G1", "G2"):
            b = (parent.breaks_G1(uu, rr["alpha"]) if g == "G1"
                 else parent.breaks_G2(w["mm"], rr["alpha"]))
            Chat = parent.cell_increments(edges, reads, b)
            deltas = Chat - lam[:, None] * Xn
            ps = parent.path_stats((A0[0, 0], A0[1, 1], A0[0, 1]),
                                   deltas)
            Aend = parent.tri_mat((ps["a11"][-1], ps["a22"][-1],
                                   ps["a12"][-1]))
            tel = float(np.max(np.abs(Aend - rr["Ah"]))) \
                / float(np.max(np.abs(rr["Ah"])))
            tel_worst = max(tel_worst, tel)
            if bool(np.all(ps["lmin"] > 0.0)):
                exit_ok = False
            w[g] = dict(ps=ps, U=uvecs_of(ps))
    check("S1.ENV envelope min e1 = %.4f >= %.4f" %
          (env_min, ENV_C * ENV_GUARD), env_min >= ENV_C * ENV_GUARD)
    check("S1.TEL telescoping worst rel %.2e (bar %.0e)"
          % (tel_worst, WARD_REL), tel_worst <= WARD_REL)
    check("S1.REG parent regression: the completed flow exits the "
          "fixed cone on every rung for BOTH groupings (the "
          "CONE-BROKEN input state)", exit_ok)

    # ============================================================== S2
    print("\nS2 -- STAGE 1: the finite prime kernel census")
    aas = [w["alpha"] for w in rows]
    stage1 = {}
    for g in ("G1", "G2"):
        print("\n  grouping %s:" % g)
        print("    %5s %7s %6s | %6s %8s %6s | %8s %8s %8s | %6s"
              % ("h", "alpha", "K", "nviol", "P0", "uP0/2a",
                 "P0@1e-3", "P0@1e-2", "P0@1e-1", "P0@tau"))
        P0s, upos, counts, Ks = [], [], [], []
        P0d_all = {d: [] for d in DEPTHS}
        for w in rows:
            ps = w[g]["ps"]
            lmin, lmax = ps["lmin"][1:], ps["lmax"][1:]
            rel = lmin / np.maximum(lmax, 1e-300)
            nn = w["nn"]
            strict = lmin <= 0.0
            nv = int(strict.sum())
            P0 = int(nn[np.where(strict)[0][-1]]) if nv else 0
            up = (w["rr"]["uu"][np.where(strict)[0][-1]]
                  / (2.0 * w["alpha"])) if nv else 0.0
            dP = {}
            for d in DEPTHS:
                mk = rel < -d
                dP[d] = int(nn[np.where(mk)[0][-1]]) if mk.any() else 0
                P0d_all[d].append(dP[d])
            mk_tau = lmin <= -w["tau"]
            P0tau = int(nn[np.where(mk_tau)[0][-1]]) \
                if mk_tau.any() else 0
            # step (3): tail from the renormalized base is clean by
            # construction -- verified:
            if nv:
                k_last = np.where(strict)[0][-1]
                assert bool(np.all(lmin[k_last + 1:] > 0.0))
            P0s.append(P0)
            upos.append(up)
            counts.append(nv)
            Ks.append(len(lmin))
            print("    %5d %7.3f %6d | %6d %8d %6.3f | %8d %8d %8d "
                  "| %6d"
                  % (w["h"], w["alpha"], len(lmin), nv, P0, up,
                     dP[DEPTHS[0]], dP[DEPTHS[1]], dP[DEPTHS[2]],
                     P0tau))
        sl_P0, r2_P0 = ols_loglog(
            [math.exp(2.0 * a) for a in aas],
            [max(p, 1) for p in P0s])
        sl_cnt, r2_cnt = ols_loglog(Ks, [max(c, 1) for c in counts])
        kt_up = kendall_tau(aas, upos)
        med_up = float(np.median(upos))
        third = max(len(rows) // 3, 1)
        P0_star = max(P0s[:third])
        tail_beyond = 0
        for i, w in enumerate(rows[third:], start=third):
            ps = w[g]["ps"]
            strict = ps["lmin"][1:] <= 0.0
            tail_beyond += int(np.sum(strict & (w["nn"] > P0_star)))
        stage1[g] = dict(P0s=P0s, med_up=med_up, kt_up=kt_up,
                         maxP0=max(P0s), sl_P0=sl_P0,
                         maxP0_d={d: max(P0d_all[d]) for d in DEPTHS},
                         counts=counts, P0_star=P0_star,
                         tail_beyond=tail_beyond)
        print("    LAW (%s): P0 ~ X^%.2f (R^2 %.2f, X = e^{2 alpha});"
              " count ~ K^%.2f (R^2 %.2f); u_P0/(2 alpha) median "
              "%.3f, Kendall vs alpha %+.3f; max strict P0 = %d "
              "(cap %d); depth-resolved max P0: %s; fixed-kernel "
              "prediction P0* = %d (smallest third) -> %d tail "
              "violations beyond it above"
              % (g, sl_P0, r2_P0, sl_cnt, r2_cnt, med_up, kt_up,
                 max(P0s), P0_CAP,
                 {("%.0e" % d): stage1[g]["maxP0_d"][d]
                  for d in DEPTHS}, P0_star, tail_beyond))
        print("    step (2)/(3) note: the flow is additive, so the "
              "per-rung tail-clean statement from the renormalized "
              "base A_kernel(P0) is BY CONSTRUCTION (asserted "
              "numerically above); the decisive content is the "
              "cross-depth stability of P0.")

    kernel_ok = {g: stage1[g]["maxP0"] <= P0_CAP for g in ("G1", "G2")}
    kernel_half = {g: (np.mean([p <= P0_CAP for p in stage1[g]["P0s"]])
                       >= 0.5) for g in ("G1", "G2")}
    kernel_depth = {g: stage1[g]["maxP0_d"][1.0e-2] <= P0_CAP
                    for g in ("G1", "G2")}
    wander = {g: (stage1[g]["med_up"] >= 0.5
                  and stage1[g]["P0s"][-1] > P0_CAP)
              for g in ("G1", "G2")}
    print("\n  STAGE-1 GATES: strict kernel bounded G1 %s / G2 %s; "
          "bounded on >= half the rungs G1 %s / G2 %s; depth-1e-2 "
          "kernel bounded G1 %s / G2 %s; WANDER criterion G1 %s / "
          "G2 %s"
          % (kernel_ok["G1"], kernel_ok["G2"], kernel_half["G1"],
             kernel_half["G2"], kernel_depth["G1"], kernel_depth["G2"],
             wander["G1"], wander["G2"]))

    # stage-1 controls (stride subset, G1 pairing)
    sub = rows[::STRIDE]
    real_cnt_med = float(np.median(
        [stage1["G1"]["counts"][i] for i in range(0, len(rows),
                                                  STRIDE)]))

    def ctrl_path(w, uuX, lamX, XnX, cont_fac=1.0, base_fac=1.0):
        rr = w["rr"]
        b = parent.breaks_G1(uuX, rr["alpha"])
        Chat = cont_fac * parent.cell_increments(w["edges"],
                                                 w["reads"], b)
        deltas = Chat - lamX[:, None] * XnX
        A0 = rr["B"] - base_fac * w["S_pnt"]
        return parent.path_stats((A0[0, 0], A0[1, 1], A0[0, 1]),
                                 deltas)

    def s1_stats(ps):
        strict = ps["lmin"][1:] <= 0.0
        return int(strict.sum()), bool(ps["lmin"][0] <= 0.0)

    eq_cnt, eq_base = [], 0
    wr_cnt, wr_base = [], 0
    eq_ps_cache, wr_ps_cache = [], []
    for w in sub:
        rr = w["rr"]
        mm_eq = np.full(len(rr["uu"]),
                        float(np.sum(w["mm"])) / len(rr["uu"]))
        ps_e = ctrl_path(w, rr["uu"], 0.5 * mm_eq, rr["Xn"])
        c, b = s1_stats(ps_e)
        eq_cnt.append(c)
        eq_base += b
        eq_ps_cache.append(ps_e)
        ps_w = ctrl_path(w, rr["uu"], rr["lam"], rr["Xn"],
                         cont_fac=WRONG_FAC, base_fac=WRONG_FAC)
        c, b = s1_stats(ps_w)
        wr_cnt.append(c)
        wr_base += b
        wr_ps_cache.append(ps_w)
    eq1_fire = (float(np.median(eq_cnt)) >= CTRL_FAC * real_cnt_med
                or eq_base > 0)
    wr1_fire = (float(np.median(wr_cnt)) >= CTRL_FAC * real_cnt_med
                or wr_base > 0)
    check("S2.C1 [must-break, stage 1] equal-weight scramble: strict "
          "violation count median %.0f vs real %.0f (x%.1f needed) "
          "or base out (%d rungs) -- %s"
          % (float(np.median(eq_cnt)), real_cnt_med, CTRL_FAC,
             eq_base, "fires" if eq1_fire else "does NOT fire"),
          eq1_fire)
    check("S2.C2 [must-break, stage 1] wrong pole normalization "
          "(x%.1f): count median %.0f, base out on %d/%d rungs -- %s"
          % (WRONG_FAC, float(np.median(wr_cnt)), wr_base, len(sub),
             "fires" if wr1_fire else "does NOT fire"), wr1_fire)

    # ============================================================== S3
    print("\nS3 -- STAGE 2: the moving Lorentz cone field "
          "(warm-up %d cells; gated tail)" % NWARM)
    field = {}
    causal_ok = True
    for g in ("G1", "G2"):
        for rule in ("A", "B"):
            key = "%s-%s" % (rule, g)
            nv_tot = ng_tot = 0
            per_rung_nv, worst_fdefs, max_incs, conds = [], [], [], []
            for w in rows:
                U = w[g]["U"]
                wgt = np.concatenate([[float(np.mean(w["mm"]))],
                                      w["mm"]])
                res = field_run(U, rule, w=wgt)
                if w is rows[0]:
                    causal_ok = causal_ok and causal_assert(
                        U, rule, wgt, res)
                nv_tot += res["nviol"]
                ng_tot += res["ngate"]
                per_rung_nv.append(res["nviol"])
                worst_fdefs.append(res["worst_fdef"])
                max_incs.append(res["max_inc"])
                conds.append(res["cond"])
                w.setdefault("field", {})[key] = res
            sl_inc, r2_inc = ols_loglog(aas, [max(v, 1e-12)
                                              for v in max_incs])
            field[key] = dict(
                nviol=nv_tot, ngate=ng_tot,
                frac=nv_tot / max(ng_tot, 1),
                rungs_clean=sum(1 for v in per_rung_nv if v == 0),
                worst_fdef=float(np.max(worst_fdefs)),
                med_fdef=float(np.median(worst_fdefs)),
                cond_max=float(np.max(conds)),
                med_maxinc=float(np.median(max_incs)),
                sl_inc=sl_inc, r2_inc=r2_inc)
            f = field[key]
            print("    rule %s on %s: gated violations %d / %d "
                  "(%.2e), clean rungs %d/%d; worst fdef %+.3f "
                  "(median per-rung worst %+.3f); max post-warm "
                  "angle reading median %.3f deg ~ alpha^%.2f (R^2 "
                  "%.2f); cond(G) max %.1f (bar %.0f)"
                  % (rule, g, f["nviol"], f["ngate"], f["frac"],
                     f["rungs_clean"], len(rows), f["worst_fdef"],
                     f["med_fdef"], f["med_maxinc"], f["sl_inc"],
                     f["r2_inc"], f["cond_max"], COND_BAR))
    check("S3.CAUSAL the field is past-only: opening th_m recomputed "
          "from explicit [:m] slices at the frozen spot cells, both "
          "rules (tau_m / the current sign never enters the "
          "construction -- the gate reads only the angle history)",
          causal_ok)

    # Psi set-inclusion on the parent spot cells (report-only)
    w0 = rows[0]
    ps0 = w0["G1"]["ps"]
    U0 = w0["G1"]["U"]
    resA = w0["field"]["A-G1"]
    phis = np.linspace(0.0, 2.0 * math.pi, NRAY, endpoint=False)
    rays = np.stack([np.ones(NRAY), np.cos(phis), np.sin(phis)],
                    axis=1)                     # L+ boundary rays
    incl_lines = []
    for k in range(NWARM, len(U0) - 2):
        Ap = parent.tri_mat((ps0["a11"][k], ps0["a22"][k],
                             ps0["a12"][k]))
        An = parent.tri_mat((ps0["a11"][k + 1], ps0["a22"][k + 1],
                             ps0["a12"][k + 1]))
        sp = parent.phi_spot(Ap, An)
        if sp is None:
            continue
        S = parent.sqrt2(Ap)
        Sinv = np.linalg.inv(S)
        IA = np.eye(2) + Sinv @ (An - Ap) @ Sinv
        M = Sinv @ parent.sqrt2(IA) @ S
        Phi = parent.lorentz_of(M)
        Gm = G_of(U0[k - 1], resA["th"][k - 1])
        Gn = G_of(U0[k], resA["th"][k])
        Psi = np.linalg.solve(Gn, Phi @ Gm)
        img = rays @ Psi.T
        qv = (img[:, 0] ** 2 - img[:, 1] ** 2 - img[:, 2] ** 2) \
            / np.maximum((img ** 2).sum(axis=1), 1e-300)
        incl_lines.append((k, float(qv.min()),
                           bool((img[:, 0] > 0).all())))
        if len(incl_lines) >= 5:
            break
    print("    Psi-inclusion (report-only, rule A/G1, first %d "
          "admissible spot cells over %d boundary rays): "
          "min boundary q-defect per cell: %s"
          % (len(incl_lines), NRAY,
             ", ".join("cell %d: %+.2e (t>0 %s)" % ln
                       for ln in incl_lines)))

    # ============================================================== S4
    print("\nS4 -- stage-2 controls (rule A, G1 pairing, stride "
          "subset)")
    real_gate_med = float(np.median(
        [rows[i]["field"]["A-G1"]["nviol"]
         for i in range(0, len(rows), STRIDE)]))
    real_inc_med = float(np.median(
        [rows[i]["field"]["A-G1"]["max_inc"]
         for i in range(0, len(rows), STRIDE)]))

    def field_ctrl(ps_list):
        cnts, incs = [], []
        for ps in ps_list:
            U = uvecs_of(ps)
            res = field_run(U, "A")
            cnts.append(res["nviol"])
            incs.append(res["max_inc"])
        return float(np.median(cnts)), float(np.median(incs))

    eq2_cnt, eq2_inc = field_ctrl(eq_ps_cache)
    wr2_cnt, wr2_inc = field_ctrl(wr_ps_cache)
    eq2_fire = (eq2_cnt >= CTRL_FAC * max(real_gate_med, 1.0)
                or eq2_inc >= CTRL_FAC * real_inc_med)
    wr2_fire = (wr2_cnt >= CTRL_FAC * max(real_gate_med, 1.0)
                or wr2_inc >= CTRL_FAC * real_inc_med)
    check("S4.C1 [must-break, stage 2] equal-weight scramble in the "
          "field: gated violation median %.0f (real %.0f), max-inc "
          "median %.2f deg (real %.2f) -- %s"
          % (eq2_cnt, real_gate_med, eq2_inc, real_inc_med,
             "fires" if eq2_fire else "does NOT fire"), eq2_fire)
    check("S4.C2 [must-break, stage 2] wrong normalization in the "
          "field: gated violation median %.0f, max-inc median %.2f "
          "deg -- %s"
          % (wr2_cnt, wr2_inc,
             "fires" if wr2_fire else "does NOT fire"), wr2_fire)

    ep_cnt, ep_inc = [], []
    for w in sub:
        rr = w["rr"]
        uuE, mE_raw = parent.epstein_atoms(rr["alpha"])
        kap = float(np.sum(w["mm"])) / float(np.sum(mE_raw))
        XnE = parent.atom_reads(rr, uuE)
        ps_ep = ctrl_path(w, uuE, 0.5 * kap * mE_raw, XnE)
        U = uvecs_of(ps_ep)
        res = field_run(U, "A")
        ep_cnt.append(res["nviol"])
        ep_inc.append(res["max_inc"])
    ep_inc_med = float(np.median(ep_inc))
    ratio = (max(ep_inc_med, 1e-12) / max(real_inc_med, 1e-12))
    ep_sep = ratio >= EP_SEP or ratio <= 1.0 / EP_SEP
    print("  S4.C3 [typed, two-sided] Epstein x^2+5y^2 in the field: "
        "gated violation median %.0f (real %.0f); max post-warm "
        "angle median %.3f deg vs real %.3f (ratio %.2f, "
        "separation bar %.1fx either way) -- %s"
        % (float(np.median(ep_cnt)), real_gate_med, ep_inc_med,
           real_inc_med, ratio, EP_SEP,
           "DISTINGUISHABLE (%s)"
           % ("Epstein rougher" if ratio > 1 else "Epstein smoother")
           if ep_sep else "NOT separated -- control surprise, typed "
           "(consistent with the parent's inverted signature)"))

    # ============================================================== S5
    print("\n" + "=" * 78)
    print("S5 -- VERDICT")
    print("=" * 78)
    runtime = time.time() - T0
    WARD_IDS = ("S0.AST", "S1.REF", "S1.ENV", "S1.TEL", "S1.REG",
                "S3.CAUSAL")
    ward_fails = [f for f in FAILS if f in WARD_IDS]
    valid = not ward_fails and runtime <= RUNTIME_CAP
    s1_ctrl = eq1_fire and wr1_fire
    s2_ctrl = eq2_fire and wr2_fire
    field_ok = {k: (field[k]["nviol"] == 0
                    and field[k]["cond_max"] <= COND_BAR)
                for k in field}
    field_near = {k: (field[k]["frac"] <= 1.0e-3
                      and field[k]["cond_max"] <= COND_BAR)
                  for k in field}
    kernel_pass = any(kernel_ok.values())
    field_pass = any(field_ok.values())
    partial = (any(kernel_half.values()) or any(kernel_depth.values())
               or any(field_near.values())
               or (kernel_pass and not s1_ctrl)
               or (field_pass and not s2_ctrl))
    if not valid:
        verdict = "INVALID"
    elif kernel_pass and s1_ctrl:
        verdict = "KERNEL-TAIL-CLEAN"
    elif field_pass and s2_ctrl:
        verdict = "FIELD-TRANSPORTS"
    elif partial:
        verdict = "BOTH-PARTIAL"
    else:
        verdict = "KERNEL-WANDERS"
    print("""
  VERDICT: %s
    stage 1 (strict kernel <= %d): G1 max P0 = %d %s, G2 max P0 = %d
      %s; wander criterion G1 %s / G2 %s; depth-1e-2 kernel bounded:
      G1 %s (max %d) / G2 %s (max %d)
    stage 2 (zero gated violations + cond <= %.0f):
      %s
    controls: stage 1 %s, stage 2 %s
""" % (verdict, P0_CAP,
       stage1["G1"]["maxP0"], "OK" if kernel_ok["G1"] else "FAIL",
       stage1["G2"]["maxP0"], "OK" if kernel_ok["G2"] else "FAIL",
       wander["G1"], wander["G2"],
       kernel_depth["G1"], stage1["G1"]["maxP0_d"][1e-2],
       kernel_depth["G2"], stage1["G2"]["maxP0_d"][1e-2],
       COND_BAR,
       "; ".join("%s: %s (viol %d/%d, cond %.1f)"
                 % (k, "CLEAN" if field_ok[k] else "fails",
                    field[k]["nviol"], field[k]["ngate"],
                    field[k]["cond_max"]) for k in sorted(field)),
       "fire" if s1_ctrl else "SURPRISE", 
       "fire" if s2_ctrl else "SURPRISE"))
    print("""  HONESTY: stage 1's per-rung tail-clean statement is additive
  bookkeeping; only the cross-depth stability of P0 carries content.
  Stage 2's transport is a bounded-angular-velocity statement about
  the state direction under a causal tube field -- it replaces
  positivity, it does not prove it; the field never sees tau_m, but
  the true comb's atom table is public arithmetic, so 'relational'
  means smooth/history summaries, not secrecy.  Finite measurement,
  67 rungs.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (runtime, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    print("[VERDICT] %s" % verdict)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

_SRC_GRADED = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""graded_kernel_field_probe -- PRIME.CELLCONE.GRADEDKERNEL.01
(EXPLORATION ONLY, experiments/; direct follow-up to the
BOTH-PARTIAL verdict of cone_kernel_field_probe /
PRIME.CELLCONE.KERNELFIELD.01, 2026-08-07: decide the graded-kernel
question and give the field teeth).

PARENT FINDINGS (cited; both parent probes imported READ-ONLY, the
construction is bit for bit theirs): the completed-cell flow exits
the fixed Lorentz cone on 67/67 rungs (both groupings); STRICT
violation positions wander with the horizon (P0 ~ X^1.03,
u_P0/(2 alpha) ~ 0.98); G1's violations of relative depth > 1e-2
are confined to n <= 73 on ALL rungs (collapsing to n = 3 at the
top of the 1e-3 census), while G2 has no bounded depth kernel; the
self-calibrating tube field transported cleanly but its must-break
controls also passed (the gate was self-calibrating -- no teeth).

STAGE 1 -- THE GRADED KERNEL LAW (adjudicated on G1, the Stieltjes
completion; G2 runs as the typed mechanism contrast):
  depth of a state = max(0, -lambda_min/lambda_max) (relative).
  (a) DEPTH PROFILE per rung: fit log(depth) vs log(n) on violating
      states (power law) and log(depth) vs n (exponential); the
      winning family by median R^2 is the typed law; plus the
      psi-fluctuation tracker: Spearman correlation between the
      violation depth and |F_k|, F_k = trace(A_k - A_0) = the flow's
      running scalar imbalance (the deployed-units psi(x)-x proxy;
      the inverted-Epstein finding predicts a positive correlation).
  (b) THE GRADED KERNEL FUNCTION P0(eps, X): last position n with
      depth > eps, per rung, for the frozen ladder eps = 1e-1..1e-6;
      per eps: gamma(eps) = log-log slope of max(P0,1) vs
      X = e^{2 alpha}, Kendall over the top half, and M_top(eps) =
      max P0 over the top third of the ladder; eps is RESOLVED iff
      M_top(eps) <= P0_CAP = 100 (the census has collapsed to the
      kernel at the top of the observed range).
      SKIN DEPTH LAW: D(X) = max depth over skin states (position
      u/(2 alpha) >= 0.5), fitted D ~ C X^{-theta}; the decay of D
      is the mechanism that resolves every fixed eps eventually,
      with the predicted threshold X0(eps) = (eps/C)^{-1/theta}.
      FROZEN PASS (KERNEL-GRADED): the resolved set is a nonempty
      UPPER interval of the eps ladder containing 1e-1 AND 1e-2,
      AND the skin decays (theta >= THETA_MIN = 0.1 with Kendall
      (log X, log D) <= -0.5) -- then 'finite kernel + tail' holds
      in the graded form with the typed non-uniform quantifier.
      FROZEN KILL (KERNEL-WANDERS-ALL-DEPTHS): the resolved set is
      EMPTY and every eps has top-half Kendall >= 0.5 (polynomial
      wandering at every depth).  MIXED otherwise (typed).
  (c) G2 MECHANISM: same profiles; plus the predeclared mechanism
      metrics: per-cell interval-centroid offset |mid(I_n) - u_n|
      (mass-matching spreads continuum mass away from the atom) and
      the running imbalance max |F| -- medians G2 vs G1, Spearman
      (offset, depth); the typed mechanism statement.

STAGE 2 -- FIELD TEETH (externally normalized gate):
  The parent field gate was self-calibrating; here every statistic
  is normalized by a FIXED external scale: the flow's OWN certified
  endpoint margin angle th_tau = deg(0.5 asin(clip(dnull_end,0,1))),
  dnull_end = q(u_end)/|u_end|^2 with q = 4 det = 4 tau lambda (the
  tau scale; wardened).  The scramble / Epstein fields are built by
  the SAME rule from THEIR data (their own endpoint scale).  FROZEN
  RULE FAMILY (rule-A tube increments, warm-up NWARM = 12 as the
  parent): T1 = max gated increment / th_tau; T2 = mean gated
  increment / th_tau; T3 = (count of gated increments > KAPPA = 10 x
  th_tau + 1)/ngate; T4 = D_skin/dnull_end (the depth census on the
  tau scale).  SEPARATION per rule = median Q(fake)/median Q(true)
  over the stride-5 subset; STRUCTURAL separation iff the fake's
  endpoint scale is undefined (dnull_end <= 0) on >= half the subset
  while the true is defined on all.  TEETH iff some rule achieves
  finite separation >= SEP = 10; structural-only separation is typed
  FIELD-STRUCTURAL-ONLY (the gate collapses to endpoint positivity
  -- honestly NOT field teeth); no rule >= SEP and no structural =>
  FIELD-NO-TEETH (the moving-cone route has no discriminating
  formulation at this granularity and closes).  If toothed: the
  transport is re-adjudicated = the true flow keeps zero
  self-calibrated membership violations (parent regression) AND
  Q_true x SEP <= Q_fake for the separating rule.  The common-scale
  ratio (both flows on the TRUE th_tau) is reported to type where
  the separation comes from.

CONTROLS: G1/G2 census regressions (frozen exact integers from the
parent run: G1 strict max P0 = 244333, G2 = 283607, G1 depth-1e-2
kernel max = 73, G2 = 77557, exits 67/67 both); scramble depth
profile must differ structurally (skin cells with depth > 1e-2:
median count >= 10 x max(true,1) on the subset); Epstein in-cone
anchor (median strict violation count == 0 on the subset, typed if
not); the tau-scale ward |q_end - 4 tau lambda| rel <= 1e-9.

VERDICT (frozen): KERNEL-GRADED (field sub-verdict typed
separately: FIELD-TOOTHED-TRANSPORTS / FIELD-TOOTHED-NO-TRANSPORT /
FIELD-STRUCTURAL-ONLY / FIELD-NO-TEETH) / KERNEL-WANDERS-ALL-DEPTHS
(the graded kill) / MIXED (typed).  INVALID on ward failure.
SYNTHESIS: the candidate depth-eps theorem verbatim if stage 1
passes, else the obituary.  NO RH claim; finite measurement on 67
rungs; writes nothing; nothing outside experiments/.

FIREWALL: parents + v563 imported READ-ONLY; no zero/prime-table
loaders (AST-checked); NO RNG; runtime cap 1800 s predeclared.

DECLARED IMPLEMENTATION CORRECTIONS (post-freeze, documented):
(1) the S3 interval-centroid computation initially assumed K+1
break edges; the parent convention is K right edges with the left
edge U0 implicit -- fixed to mid_j = (left_j + b_j)/2, left_1 = U0.
Purely a shape convention in a report-only mechanism metric.
(2) the tau-scale ward bar 1e-9 ignored the det-cancellation
conditioning: q_end = 4 det(A_end) at tau/lambda ~ 3e-8 amplifies
the 3.4e-15 telescoping noise by lambda/tau to ~5e-8 relative --
the identity is exact, the bar was mis-calibrated.  Corrected to
the conditioning-aware bar rel <= max(1e-9, 1e3 * eps_mach *
lambda_end/tau) per rung (a genuine normalization error would show
O(1)).  No structural bar changed; the first run's failure and this
correction are declared here.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/graded_kernel_field_probe.py
"""

import ast
import hashlib
import inspect
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core             # noqa: E402 (READ-ONLY)
import cell_cone_transport_probe as parent      # noqa: E402 (READ-ONLY)
import cone_kernel_field_probe as probe3        # noqa: E402 (READ-ONLY)

FROZEN_SPEC = """\
PRIME.CELLCONE.GRADEDKERNEL.01 spec v1 (2026-08-07, frozen before
the run).  Ladder/objects/groupings = PRIME.CELLCONE.TRANSPORT.01
verbatim (parents imported read-only).  depth = max(0, -lmin/lmax).
WARDS: tau refs kz 9/12/13 rel <= 1e-4; envelope >= 4.335*0.999;
telescoping rel <= 1e-9; tau-scale identity |q_end - 4 tau lambda|
rel <= 1e-9 per rung; census regressions EXACT (G1 strict maxP0
244333, G2 283607, G1 K(1e-2) 73, G2 K(1e-2) 77557, exits 67/67
both groupings).  STAGE 1 (adjudicated on G1): eps ladder {1e-1,
1e-2, 1e-3, 1e-4, 1e-5, 1e-6}; P0(eps, rung) = last n with depth >
eps; M_top(eps) = max over the top third (alpha order); RESOLVED
iff M_top <= P0_CAP = 100; skin = states with u/(2 alpha) >= 0.5;
D(rung) = max skin depth; fit log D vs log X -> theta;
KERNEL-GRADED iff resolved set = upper interval containing {1e-1,
1e-2} AND theta >= 0.1 AND Kendall(log X, log D) <= -0.5;
KERNEL-WANDERS-ALL-DEPTHS iff resolved set empty AND all-eps
top-half Kendall >= 0.5; MIXED else.  Depth profile: per-rung OLS
log depth vs log n (power) vs log depth vs n (exp), winner by
median R^2; psi-tracker = Spearman(depth, |F|) on violating cells
(subsample <= 2000, deterministic); mechanism metrics = interval
centroid offset + max |F|, G2 vs G1.  STAGE 2 (stride-5 subset,
rule-A tube, NWARM = 12): own-scale th_tau = deg(0.5 asin
clip(dnull_end, 0, 1)); rules T1 max-inc/th_tau, T2 mean-inc/
th_tau, T3 (count inc > 10 th_tau + 1)/ngate, T4 D_skin/dnull_end;
separation = med Q(scramble)/med Q(true), SEP = 10; structural iff
scramble dnull_end <= 0 on >= half subset & true defined on all;
FIELD-TOOTHED iff finite separation >= SEP for some rule;
structural-only => FIELD-STRUCTURAL-ONLY; else FIELD-NO-TEETH;
toothed transport iff parent membership regression clean AND
Q_true x SEP <= Q_fake.  Epstein: same rules, typed two-sided, bar
SEP, non-gating anchor (in-cone regression median strict count ==
0).  Scramble depth-profile control: median skin count depth >
1e-2 >= 10 x max(true median, 1).  VERDICT: KERNEL-GRADED (+ field
typed) / KERNEL-WANDERS-ALL-DEPTHS / MIXED; INVALID on wards.  No
prediction frozen for the outcomes.  NO RH claim; writes nothing.
"""

STRIDE = 5
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
TAU_REF_REL = 1.0e-4
ENV_C = 4.335
ENV_GUARD = 0.999
WARD_REL = 1.0e-9
REG_EXACT = dict(G1_strict=244333, G2_strict=283607,
                 G1_k2=73, G2_k2=77557)
EPS_LADDER = (1.0e-1, 1.0e-2, 1.0e-3, 1.0e-4, 1.0e-5, 1.0e-6)
P0_CAP = 100
SKIN_POS = 0.5
THETA_MIN = 0.1
KEN_BAR = 0.5
DEPTH_KER = 1.0e-2
NSUB = 2000
NWARM = probe3.NWARM
KAPPA = 10.0
SEP = 10.0
RUNTIME_CAP = 1800.0
BANNED_IDS = parent.BANNED_IDS if hasattr(parent, "BANNED_IDS") else (
    "zetazero", "nzeros", "primerange", "isprime", "primepi",
    "nextprime", "prevprime", "find_zeros", "second_sheet_zero")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in BANNED_IDS:
                return False
    return True


def kendall_tau(x, y):
    n = len(x)
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (x[j] - x[i]) * (y[j] - y[i])
            if s > 0:
                conc += 1
            elif s < 0:
                disc += 1
    return (conc - disc) / max(n * (n - 1) // 2, 1)


def spearman(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    rx -= rx.mean()
    ry -= ry.mean()
    d = math.sqrt(float((rx * rx).sum()) * float((ry * ry).sum()))
    return float((rx * ry).sum() / d) if d > 0 else 0.0


def ols_fit(x, y):
    """slope, intercept, R^2 of y on x."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    b, q = np.polyfit(x, y, 1)
    pred = b * x + q
    ssr = float(((y - pred) ** 2).sum())
    sst = max(float(((y - y.mean()) ** 2).sum()), 1e-300)
    return float(b), float(q), 1.0 - ssr / sst


def subsample(idx):
    if len(idx) <= NSUB:
        return idx
    sel = np.unique(np.linspace(0, len(idx) - 1, NSUB).astype(int))
    return idx[sel]


def dnull_end_of(ps):
    t = float(ps["a11"][-1] + ps["a22"][-1])
    x = float(ps["a11"][-1] - ps["a22"][-1])
    y = 2.0 * float(ps["a12"][-1])
    q = t * t - x * x - y * y
    return q / max(t * t + x * x + y * y, 1e-300), q


def skin_depth(ps, uu, alpha):
    depth = np.maximum(0.0, -ps["lmin"][1:]
                       / np.maximum(ps["lmax"][1:], 1e-300))
    skin = (uu / (2.0 * alpha)) >= SKIN_POS
    return (float(depth[skin].max()) if skin.any() else 0.0, depth,
            skin)


def toothed_stats(ps, uu, alpha):
    """Externally normalized field statistics for one flow (own
    endpoint scale).  Returns dict or scale=None if undefined."""
    U = probe3.uvecs_of(ps)
    res = probe3.field_run(U, "A")
    ang = res["ang"][res["gated"]]
    nd, _q = dnull_end_of(ps)
    D, _, _ = skin_depth(ps, uu, alpha)
    out = dict(nviol_self=res["nviol"], max_inc=float(ang.max()),
               mean_inc=float(ang.mean()), ngate=len(ang),
               nd=nd, D=D)
    if nd <= 0.0:
        out["scale"] = None
        return out
    th = math.degrees(0.5 * math.asin(min(1.0, nd)))
    out["scale"] = th
    out["T1"] = out["max_inc"] / th
    out["T2"] = out["mean_inc"] / th
    out["T3"] = (float(np.sum(ang > KAPPA * th)) + 1.0) / len(ang)
    out["T4"] = D / nd
    return out


def main():
    spec_hash = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()
    print("=" * 78)
    print("PRIME.CELLCONE.GRADEDKERNEL.01 -- graded kernel law + "
          "field teeth")
    print("=" * 78)
    print(FROZEN_SPEC)
    print("SPEC sha256          : %s" % spec_hash)
    print("toothed-gate sha256  : %s" % hashlib.sha256(
        inspect.getsource(toothed_stats).encode()).hexdigest())
    print("parent field sha256  : %s (reused read-only)"
          % hashlib.sha256(inspect.getsource(
              probe3.field_run).encode()).hexdigest()[:16])

    # ============================================================== S0
    print("\nS0 -- firewall")
    check("S0.AST no zero/prime-table loader; parents read-only; "
          "NO RNG", ast_zero_firewall(__file__))

    # ============================================================== S1
    print("\nS1 -- ladder + wards + exact census regressions")
    rows = []
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        if rr["h"] == parent.ANOMALOUS_H:
            continue
        if math.exp(2.0 * rr["alpha"]) > core.ATOM_MAX + 0.5:
            continue
        rows.append(dict(rr=rr, h=rr["h"], alpha=rr["alpha"],
                         X=math.exp(2.0 * rr["alpha"]),
                         tau=parent.eig2_min(rr["Ah"])))
    rows.sort(key=lambda w: w["alpha"])
    ref_ok = all(abs(parent.eig2_min(core.build_window(kz)["Ah"])
                     - tr) / tr <= TAU_REF_REL
                 for kz, tr in TAU_REFS.items())
    check("S1.REF tau references reproduce (bar %.0e)" % TAU_REF_REL,
          ref_ok)

    env_min = float("inf")
    tel_worst = 0.0
    tau_ward_worst = 0.0
    exit_ok = True
    for w in rows:
        rr = w["rr"]
        edges, reads = parent.pnt_grid(rr)
        w["edges"], w["reads"] = edges, reads
        S_pnt = parent.tri_mat(parent.cum_reads(
            edges, reads, [2.0 * rr["alpha"]])[0])
        w["S_pnt"] = S_pnt
        A0 = rr["B"] - S_pnt
        w["A0"] = A0
        env_min = min(env_min, (w["tau"] / parent.eig2_min(A0))
                      * w["h"] ** 1.5)
        uu, lam, Xn = rr["uu"], rr["lam"], rr["Xn"]
        w["mm"] = 2.0 * lam
        w["nn"] = np.rint(np.exp(uu)).astype(np.int64)
        lam_end = float(np.linalg.eigvalsh(rr["Ah"])[-1])
        for g in ("G1", "G2"):
            b = (parent.breaks_G1(uu, rr["alpha"]) if g == "G1"
                 else parent.breaks_G2(w["mm"], rr["alpha"]))
            Chat = parent.cell_increments(edges, reads, b)
            deltas = Chat - lam[:, None] * Xn
            ps = parent.path_stats((A0[0, 0], A0[1, 1], A0[0, 1]),
                                   deltas)
            Aend = parent.tri_mat((ps["a11"][-1], ps["a22"][-1],
                                   ps["a12"][-1]))
            tel_worst = max(tel_worst, float(np.max(np.abs(
                Aend - rr["Ah"]))) / float(np.max(np.abs(rr["Ah"]))))
            if bool(np.all(ps["lmin"] > 0.0)):
                exit_ok = False
            nd, q_end = dnull_end_of(ps)
            # conditioning-aware normalization (declared correction
            # (2)): the det cancellation amplifies fp noise by
            # lambda/tau
            bar_rung = max(WARD_REL, 1.0e3 * np.finfo(float).eps
                           * lam_end / w["tau"])
            tau_ward_worst = max(tau_ward_worst, (abs(
                q_end - 4.0 * w["tau"] * lam_end)
                / (4.0 * w["tau"] * lam_end)) / bar_rung)
            w[g] = dict(ps=ps, deltas=deltas, breaks=b, nd=nd)
    check("S1.ENV envelope min e1 = %.4f >= %.4f"
          % (env_min, ENV_C * ENV_GUARD), env_min >= ENV_C * ENV_GUARD)
    check("S1.TEL telescoping worst rel %.2e (bar %.0e)"
          % (tel_worst, WARD_REL), tel_worst <= WARD_REL)
    check("S1.TAU tau-scale identity q_end = 4 tau lambda, worst "
          "bar-normalized %.2e <= 1 (conditioning-aware bar, "
          "declared correction (2))" % tau_ward_worst,
          tau_ward_worst <= 1.0)

    # depth arrays + strict/graded censuses
    for w in rows:
        for g in ("G1", "G2"):
            ps = w[g]["ps"]
            depth = np.maximum(0.0, -ps["lmin"][1:]
                               / np.maximum(ps["lmax"][1:], 1e-300))
            w[g]["depth"] = depth
            w[g]["P0"] = {}
            for eps in EPS_LADDER:
                mk = depth > eps
                w[g]["P0"][eps] = int(w["nn"][np.where(mk)[0][-1]]) \
                    if mk.any() else 0
            strict = ps["lmin"][1:] <= 0.0
            w[g]["strict_P0"] = int(w["nn"][np.where(strict)[0][-1]]) \
                if strict.any() else 0
            F = np.cumsum(w[g]["deltas"][:, 0] + w[g]["deltas"][:, 1])
            w[g]["F"] = F
    reg_ok = (max(w["G1"]["strict_P0"] for w in rows)
              == REG_EXACT["G1_strict"]
              and max(w["G2"]["strict_P0"] for w in rows)
              == REG_EXACT["G2_strict"]
              and max(w["G1"]["P0"][DEPTH_KER] for w in rows)
              == REG_EXACT["G1_k2"]
              and max(w["G2"]["P0"][DEPTH_KER] for w in rows)
              == REG_EXACT["G2_k2"])
    check("S1.REG parent censuses reproduce EXACTLY (G1/G2 strict "
          "maxP0 %d/%d, depth-1e-2 kernels %d/%d) + exits 67/67"
          % (max(w["G1"]["strict_P0"] for w in rows),
             max(w["G2"]["strict_P0"] for w in rows),
             max(w["G1"]["P0"][DEPTH_KER] for w in rows),
             max(w["G2"]["P0"][DEPTH_KER] for w in rows)),
          reg_ok and exit_ok)

    # ============================================================== S2
    print("\nS2 -- STAGE 1: the graded kernel law")
    aas = [w["alpha"] for w in rows]
    Xs = [w["X"] for w in rows]
    third = max(len(rows) // 3, 1)
    half = len(rows) // 2
    stage1 = {}
    for g in ("G1", "G2"):
        print("\n  grouping %s -- P0(eps, X) census "
              "(eps columns %s):" % (g, ", ".join(
                  "%.0e" % e for e in EPS_LADDER)))
        print("    %5s %7s %9s | %s" % ("h", "alpha", "X", " ".join(
            "%8s" % ("P0@%.0e" % e) for e in EPS_LADDER)))
        for w in rows:
            print("    %5d %7.3f %9.0f | %s"
                  % (w["h"], w["alpha"], w["X"], " ".join(
                      "%8d" % w[g]["P0"][e] for e in EPS_LADDER)))
        res_eps = {}
        print("    per-eps laws:")
        for eps in EPS_LADDER:
            p0 = np.array([w[g]["P0"][eps] for w in rows], float)
            m_top = int(p0[-third:].max())
            nz = p0 > 0
            if nz.sum() >= 5:
                gam, _, r2 = ols_fit(np.log(np.array(Xs)[nz]),
                                     np.log(p0[nz]))
            else:
                gam, r2 = float("nan"), float("nan")
            kt = kendall_tau([math.log(x) for x in Xs[-half:]],
                             [math.log(max(v, 1.0))
                              for v in p0[-half:]])
            resolved = m_top <= P0_CAP
            res_eps[eps] = dict(m_top=m_top, gam=gam, kt=kt,
                                resolved=resolved,
                                gmax=int(p0.max()))
            print("      eps %.0e: global max P0 %8d, M_top %8d "
                  "-> %-11s gamma %5s (R^2 %s), top-half Kendall "
                  "%+.2f"
                  % (eps, int(p0.max()), m_top,
                     "RESOLVED" if resolved else "unresolved",
                     ("%.2f" % gam) if math.isfinite(gam) else "--",
                     ("%.2f" % r2) if math.isfinite(r2) else "--",
                     kt))
        # skin depth law
        Ds = []
        for w in rows:
            D, _, _ = skin_depth(w[g]["ps"], w["rr"]["uu"],
                                 w["alpha"])
            Ds.append(max(D, 1e-300))
        th_sl, th_ic, th_r2 = ols_fit(np.log(Xs), np.log(Ds))
        kt_D = kendall_tau([math.log(x) for x in Xs],
                           [math.log(d) for d in Ds])
        theta = -th_sl
        C_D = math.exp(th_ic)
        nd_ratio = float(np.median(
            [Ds[i] / max(rows[i][g]["nd"], 1e-300)
             for i in range(len(rows))]))
        print("    SKIN DEPTH LAW (%s): D(X) ~ %.3g * X^-%.3f "
              "(R^2 %.2f, Kendall %+.2f); median D/dnull_end = %.1f "
              "(the skin vs the certified tau scale); predicted "
              "X0(eps) = (eps/C)^(-1/theta): X0(1e-3) ~ %.1e, "
              "X0(1e-4) ~ %.1e"
              % (g, C_D, theta, th_r2, kt_D, nd_ratio,
                 (1e-3 / C_D) ** (-1.0 / theta) if theta > 0 else
                 float("inf"),
                 (1e-4 / C_D) ** (-1.0 / theta) if theta > 0 else
                 float("inf")))
        # depth profile law (a)
        sl_pow, r2_pow, r2_exp, sp_F = [], [], [], []
        for w in rows:
            depth = w[g]["depth"]
            idx = np.where(depth > 0.0)[0]
            if len(idx) < 8:
                continue
            idx = subsample(idx)
            ln_n = np.log(w["nn"][idx].astype(float))
            ln_d = np.log(depth[idx])
            b1, _, rp = ols_fit(ln_n, ln_d)
            _, _, re = ols_fit(w["nn"][idx].astype(float), ln_d)
            sl_pow.append(b1)
            r2_pow.append(rp)
            r2_exp.append(re)
            sp_F.append(spearman(depth[idx],
                                 np.abs(w[g]["F"][idx])))
        fam = "POWER" if np.median(r2_pow) >= np.median(r2_exp) \
            else "EXPONENTIAL"
        print("    DEPTH PROFILE (%s): depth(n) ~ n^%.2f (median "
              "slope; median R^2 power %.2f vs exp %.2f -> %s "
              "family); psi-tracker Spearman(depth, |F|) median "
              "%+.2f over rungs"
              % (g, float(np.median(sl_pow)),
                 float(np.median(r2_pow)), float(np.median(r2_exp)),
                 fam, float(np.median(sp_F))))
        stage1[g] = dict(res_eps=res_eps, theta=theta, C_D=C_D,
                         th_r2=th_r2, kt_D=kt_D,
                         sp_F=float(np.median(sp_F)),
                         slope_pow=float(np.median(sl_pow)), fam=fam)

    r1 = stage1["G1"]["res_eps"]
    flags = [r1[e]["resolved"] for e in EPS_LADDER]   # eps descending
    upper_interval = all(flags[:flags.index(False)]) \
        if False in flags else True
    nonempty_top2 = flags[0] and flags[1]
    decay_ok = (stage1["G1"]["theta"] >= THETA_MIN
                and stage1["G1"]["kt_D"] <= -KEN_BAR)
    graded = nonempty_top2 and upper_interval and decay_ok
    wander_all = (not any(flags)) and all(
        r1[e]["kt"] >= KEN_BAR for e in EPS_LADDER)
    print("\n  STAGE-1 GATES (G1): resolved flags %s (upper interval "
          "%s, {1e-1,1e-2} resolved %s); skin decay theta = %.3f "
          "(>= %.1f: %s), Kendall %+.2f (<= -%.1f: %s) => "
          "KERNEL-GRADED %s / WANDERS-ALL-DEPTHS %s"
          % (["%d" % f for f in flags], upper_interval, nonempty_top2,
             stage1["G1"]["theta"], THETA_MIN,
             stage1["G1"]["theta"] >= THETA_MIN, stage1["G1"]["kt_D"],
             KEN_BAR, stage1["G1"]["kt_D"] <= -KEN_BAR,
             graded, wander_all))

    # ============================================================== S3
    print("\nS3 -- the G2 mechanism (typed contrast)")
    off_med = {}
    sp_off = {}
    Fmax_med = {}
    for g in ("G1", "G2"):
        offs_all, sps, fmaxs = [], [], []
        for w in rows:
            b = w[g]["breaks"]
            # parent convention: b = the K right edges, left edge U0
            # implicit -- I_j = (left_j, b_j]
            left = np.concatenate([[parent.U0], b[:-1]])
            mid = 0.5 * (left + b)
            off = np.abs(mid - w["rr"]["uu"])
            offs_all.append(float(np.median(off)))
            fmaxs.append(float(np.max(np.abs(w[g]["F"]))))
            idx = np.where(w[g]["depth"] > 0.0)[0]
            if len(idx) >= 8:
                idx = subsample(idx)
                sps.append(spearman(off[idx], w[g]["depth"][idx]))
        off_med[g] = float(np.median(offs_all))
        sp_off[g] = float(np.median(sps))
        Fmax_med[g] = float(np.median(fmaxs))
    print("    interval-centroid offset |mid(I_n) - u_n| median: "
          "G1 %.4f vs G2 %.4f (ratio %.1f); Spearman(offset, depth) "
          "median: G1 %+.2f vs G2 %+.2f; running imbalance max |F| "
          "median: G1 %.3f vs G2 %.3f (ratio %.1f)"
          % (off_med["G1"], off_med["G2"],
             off_med["G2"] / max(off_med["G1"], 1e-300),
             sp_off["G1"], sp_off["G2"], Fmax_med["G1"],
             Fmax_med["G2"],
             Fmax_med["G2"] / max(Fmax_med["G1"], 1e-300)))
    print("    typed mechanism: G2's mass-matched intervals sit "
          "further from their atoms and carry a larger running "
          "imbalance -- the compensation is delayed, the violation "
          "mass spreads into the window instead of collapsing onto "
          "the small-n kernel (numbers above; kernel censuses in "
          "S2).")

    # ============================================================== S4
    print("\nS4 -- STAGE 2: field teeth (externally normalized "
          "gate, stride-%d subset)" % STRIDE)
    sub = rows[::STRIDE]

    def flow_ps(w, uuX, lamX, XnX):
        rr = w["rr"]
        b = parent.breaks_G1(uuX, rr["alpha"])
        Chat = parent.cell_increments(w["edges"], w["reads"], b)
        deltas = Chat - lamX[:, None] * XnX
        A0 = w["A0"]
        return parent.path_stats((A0[0, 0], A0[1, 1], A0[0, 1]),
                                 deltas)

    stats = dict(true=[], scr=[], eps=[])
    scr_strict, eps_strict = [], []
    scr_skin, true_skin = [], []
    for w in sub:
        rr = w["rr"]
        uu = rr["uu"]
        st_t = toothed_stats(w["G1"]["ps"], uu, w["alpha"])
        stats["true"].append(st_t)
        _, dep_t, skin_t = skin_depth(w["G1"]["ps"], uu, w["alpha"])
        true_skin.append(int(np.sum((dep_t > DEPTH_KER) & skin_t)))
        mm_eq = np.full(len(uu), float(np.sum(w["mm"])) / len(uu))
        ps_s = flow_ps(w, uu, 0.5 * mm_eq, rr["Xn"])
        stats["scr"].append(toothed_stats(ps_s, uu, w["alpha"]))
        scr_strict.append(int(np.sum(ps_s["lmin"][1:] <= 0.0)))
        _, dep_s, skin_s = skin_depth(ps_s, uu, w["alpha"])
        scr_skin.append(int(np.sum((dep_s > DEPTH_KER) & skin_s)))
        uuE, mE_raw = parent.epstein_atoms(rr["alpha"])
        kap = float(np.sum(w["mm"])) / float(np.sum(mE_raw))
        XnE = parent.atom_reads(rr, uuE)
        ps_e = flow_ps(w, uuE, 0.5 * kap * mE_raw, XnE)
        stats["eps"].append(toothed_stats(ps_e, uuE, w["alpha"]))
        eps_strict.append(int(np.sum(ps_e["lmin"][1:] <= 0.0)))

    true_def = [s for s in stats["true"] if s["scale"] is not None]
    scr_undef = sum(1 for s in stats["scr"] if s["scale"] is None)
    structural = (scr_undef >= len(sub) / 2.0
                  and len(true_def) == len(sub))
    print("    endpoint scales: true th_tau defined %d/%d (median "
          "%.2e deg); scramble undefined (endpoint out of cone) on "
          "%d/%d; Epstein undefined on %d/%d"
          % (len(true_def), len(sub),
             float(np.median([s["scale"] for s in true_def]))
             if true_def else float("nan"),
             scr_undef, len(sub),
             sum(1 for s in stats["eps"] if s["scale"] is None),
             len(sub)))

    seps, seps_ep = {}, {}
    for Tn in ("T1", "T2", "T3", "T4"):
        qt = [s[Tn] for s in stats["true"] if s["scale"] is not None]
        qs = [s[Tn] for s in stats["scr"] if s["scale"] is not None]
        qe = [s[Tn] for s in stats["eps"] if s["scale"] is not None]
        mt = float(np.median(qt)) if qt else float("nan")
        seps[Tn] = (float(np.median(qs)) / mt) if (qs and mt > 0) \
            else float("inf") if structural else float("nan")
        seps_ep[Tn] = (float(np.median(qe)) / mt) if (qe and mt > 0) \
            else float("nan")
        print("    rule %s: Q_true median %10.3g | scramble "
              "separation %8s | Epstein ratio %8s"
              % (Tn, mt,
                 ("%.2f" % seps[Tn]) if math.isfinite(seps[Tn])
                 else ("STRUCT" if structural else "--"),
                 ("%.2f" % seps_ep[Tn])
                 if math.isfinite(seps_ep[Tn]) else "--"))
    common = (float(np.median([s["max_inc"] for s in stats["scr"]]))
              / max(float(np.median([s["max_inc"]
                                     for s in stats["true"]])),
                    1e-300))
    print("    common-scale (true th_tau on both) max-inc ratio: "
          "%.2f -- where the separation does NOT come from"
          % common)

    finite_teeth = [Tn for Tn in seps
                    if math.isfinite(seps[Tn]) and seps[Tn] >= SEP]
    if finite_teeth:
        best = max(finite_teeth, key=lambda t: seps[t])
        member_ok = all(s["nviol_self"] == 0 for s in stats["true"])
        transport = member_ok and seps[best] >= SEP
        field_verdict = ("FIELD-TOOTHED-TRANSPORTS" if transport
                         else "FIELD-TOOTHED-NO-TRANSPORT")
        detail = ("rule %s separates x%.1f (bar %.0f); membership "
                  "regression %s" % (best, seps[best], SEP,
                                     "clean" if member_ok else
                                     "BROKEN"))
    elif structural:
        field_verdict = "FIELD-STRUCTURAL-ONLY"
        detail = ("scramble cannot define its own certified scale "
                  "(endpoint out on %d/%d) -- the gate collapses to "
                  "endpoint positivity, honestly NOT field teeth"
                  % (scr_undef, len(sub)))
    else:
        field_verdict = "FIELD-NO-TEETH"
        detail = ("best finite separation %.2f < %.0f; the "
                  "moving-cone route has no discriminating "
                  "formulation at this granularity and closes"
                  % (max(v for v in seps.values()
                         if math.isfinite(v)), SEP))
    print("    FIELD SUB-VERDICT: %s (%s)" % (field_verdict, detail))

    # ============================================================== S5
    print("\nS5 -- controls")
    scr_fire = (float(np.median(scr_skin))
                >= 10.0 * max(float(np.median(true_skin)), 1.0))
    check("S5.C1 [must-differ] scramble depth profile is "
          "scale-free/everywhere: median skin cells with depth > "
          "%.0e = %.0f vs true %.0f (x10 needed) -- %s"
          % (DEPTH_KER, float(np.median(scr_skin)),
             float(np.median(true_skin)),
             "fires" if scr_fire else "does NOT fire"), scr_fire)
    ep_incone = float(np.median(eps_strict)) == 0.0
    print("  S5.C2 [anchor, typed] Epstein in-cone regression: "
          "median strict violation count %.0f (0 expected) -- %s"
          % (float(np.median(eps_strict)),
             "reproduces (the contrast anchor holds)" if ep_incone
             else "SURPRISE, typed"))

    # ============================================================== S6
    print("\n" + "=" * 78)
    print("S6 -- VERDICT + SYNTHESIS")
    print("=" * 78)
    runtime = time.time() - T0
    WARD_IDS = ("S0.AST", "S1.REF", "S1.ENV", "S1.TEL", "S1.TAU",
                "S1.REG")
    ward_fails = [f for f in FAILS if f in WARD_IDS]
    valid = not ward_fails and runtime <= RUNTIME_CAP
    if not valid:
        verdict = "INVALID"
    elif graded:
        verdict = "KERNEL-GRADED"
    elif wander_all:
        verdict = "KERNEL-WANDERS-ALL-DEPTHS"
    else:
        verdict = "MIXED"
    print("\n  VERDICT: %s   (field: %s; scramble depth control %s; "
          "Epstein anchor %s)"
          % (verdict, field_verdict,
             "fires" if scr_fire else "SURPRISE",
             "holds" if ep_incone else "SURPRISE"))
    if verdict == "KERNEL-GRADED":
        print("""
  CANDIDATE STATEMENT (verbatim, the depth-eps cone; G1/Stieltjes
  completion; measured on 67 rungs, NOT proven, NOT uniform in eps,
  NOT an RH claim):
    "For every eps > 0 there exist finite P0(eps) and X0(eps) such
     that for every window X >= X0(eps), every state of the
     completed-cell flow beyond n = P0(eps) has relative depth
     -lambda_min/lambda_max <= eps.  Measured witnesses: P0(1e-1) =
     0, P0(1e-2) <= %d (collapsing to {2,3} above alpha ~ 3.9);
     skin depth D(X) ~ %.3g X^-%.3f (R^2 %.2f) predicts X0(eps) ~
     (eps/%.3g)^(-1/%.3f); the strict (eps -> 0) census wanders
     with the horizon (P0 ~ X^1.03 at relative position 0.98) --
     the wandering is vanishing-depth skin, not kernel growth."
  SURVIVES: the graded kernel law above + the exact congruence
  calculus (telescoping exact to 1e-13) + the ray cascade
  (RAY-EDGE-CONFIRMED, parent).  The fixed-cone layer statement
  stays dead; the field is typed %s."""
              % (REG_EXACT["G1_k2"], stage1["G1"]["C_D"],
                 stage1["G1"]["theta"], stage1["G1"]["th_r2"],
                 stage1["G1"]["C_D"], stage1["G1"]["theta"],
                 field_verdict))
    elif verdict == "KERNEL-WANDERS-ALL-DEPTHS":
        print("""
  OBITUARY: the violation positions grow polynomially in X at every
  depth of the eps ladder -- the wandering is real, not
  vanishing-depth noise; package D is dead in graded form too.
  What survives regardless: the exact congruence calculus and the
  ray cascade.  Field: %s.""" % field_verdict)
    else:
        print("""
  MIXED (typed above): the resolved set / decay law / wander flags
  disagree -- see the S2 gate line for exactly which clause failed;
  the field is typed %s.""" % field_verdict)
    print("""
  HONESTY: 'resolved' is an in-range statement (the census collapsed
  within the observed 67 rungs); the eps < 1e-2 rows are extrapolated
  only through the fitted D(X) law; the toothed gate compares flows
  through their OWN certified scales, so a fake without a certified
  endpoint separates structurally, not dynamically.  NO RH claim.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (runtime, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    print("[VERDICT] %s" % verdict)
    return 0 if valid else 1


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
    module namespace, registered in sys.modules under the probe's
    canonical import name (cross-probe READ-ONLY imports resolve to
    the embedded copies); capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
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


# exp_n = None marks a READ-ONLY library embed (exec only, no protocol
# run, no gate -- the parent's protocol is promoted and gated in v847)
_PLAN = (
    ("cell_cone_transport_probe", _SRC_PARENT, None, (), "", 0),
    ("multiplicative_cluster_probe", _SRC_CLUSTER, 15,
     ("S3.2", "S4.1"), "CLUSTERS-DIFFUSE", 1),
    ("cone_kernel_field_probe", _SRC_KERNELFIELD, 10,
     ("S2.C1", "S2.C2", "S4.C1", "S4.C2"), "BOTH-PARTIAL", 0),
    ("graded_kernel_field_probe", _SRC_GRADED, 7, (),
     "KERNEL-GRADED", 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print("v851 -- PRIME.CELLCONE.KERNELFIELD.01 + PRIME.CLUSTER."
          "MULT.01 +")
    print("PRIME.CELLCONE.GRADEDKERNEL.01 [O]")
    print("(the SIX frozen-honest FAILS S3.2, S4.1, S2.C1, S2.C2, "
          "S4.C1, S4.C2 are")
    print("EXPECTED and pattern-gated, NOT refit -- v829/v831/v843/"
          "v847 precedent;")
    print("the graded kernel law D(X) ~ 0.75 X^-0.55 is the round's "
          "positive core;")
    print("frozen protocols embedded byte-exact; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        if exp_n is None:
            print("EMBEDDED READ-ONLY LIBRARY: %s (protocol promoted "
                  "and gated in v847)" % name)
            print("-" * 74, flush=True)
            _out, _code, same = _exec_probe(name, src, run_entry=False)
            ok_lib = same is not False
            gates.append(ok_lib)
            print("[%s] LIBRARY GATE %s: definitions loaded, %s"
                  % ("PASS" if ok_lib else "FAIL", name,
                     "byte-exact vs experiments source" if same is True
                     else "embedded copy (source file not present)"
                     if same is None else "SOURCE MISMATCH"),
                  flush=True)
            continue
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
              exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v851: %d/%d gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print("NO RH claim; the strict census wanders as vanishing-depth "
          "skin, not kernel")
    print("growth -- the graded kernel+tail statement is a MEASURED "
          "theorem candidate")
    print("(PRIME.CELLCONE.GRADEDKERNEL.01 [O]), not a theorem; the "
          "field is")
    print("FIELD-STRUCTURAL-ONLY; fixed-cone kernel layers and same-"
          "grade corner")
    print("cluster expansions are stop-listed.")
    print("[%s] v851 VERDICT GATE: CLUSTERS-DIFFUSE + BOTH-PARTIAL + "
          "KERNEL-GRADED" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
