#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v895 -- PRIME.PORT.FACTORAVOID.01 + PRIME.PORT.DEEPCORE.01: THE COLLECTIVITY OF THE ARITHMETIC -- factor avoidance is structural and one-sided (the norm-bound shape does not exist) and the surviving deep-core remnant is carried by the ENTIRE multiplicative von Mangoldt comb, ONE module from two probes (18/18 + 12/12 checks, zero fails, verdicts FACTORAVOID-MEASURED (AVOIDANCE-STRUCTURAL / SPLIT-DEGENERATE / GRAIN-NONDECOMPOSITIONAL) + DEEPCORE-MEASURED; discovery probes factor_avoidance_euler_probe.py (SPEC v2/v3), deepcore_anatomy_probe.py, round 50, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~31 s).  (1) FACTOR AVOIDANCE IS STRUCTURAL (factoravoid, follow-up (b) of the tau anatomy v890): WHY the truth ladder keeps every determinant factor Q_h = prod_i (1 + mu_i) away from -1 while every smooth control crosses -- anatomy (A) SIZE is dead: the norm-bound shape rho(W^{-1} Delta C) < 1 does NOT exist on truth (rho >= 1 on steps of the ladder); the TRUE law is ONE-SIDED: max over all 31 truth steps of (-min mu) = 0.9950 < 1 -- the factors approach -1 from the safe side and never reach it, an avoidance of ONE spectral edge, not a two-sided smallness (exactly the theorem shape v892 confirms by the hermitian congruence); the geometry/atom split of the increment is EXACTLY DEGENERATE -- the atom cutoff is slaved to the tent edge, so the moving block carries BITWISE ZERO of the increment through its own tents (LEAVE: bitwise zero; ENTER: baseline frame-dead; SPEC v2 hybrid trichotomy bookkeeping); and the per-prime leave-one-out responses are NON-DECOMPOSITIONAL (sum_p rho_p ~ 1e4 against rho_tot ~ 1..4; the SPEC v3 validity precondition fires), reported honestly as a LEVERAGE census of the window operators -- single primes lever the increment by factors up to 987x -- so the avoidance is a property of the COLLECTIVE comb, not of any per-prime cascade term.  (2) THE DEEP-CORE ANATOMY (deepcore, follow-up (c) of the Moebius kill battery v891): the surviving fit-free gauge-free arithmetic remnant of the cross-ratio firewall lives on the FIXED even alias set {2, 4, ..., 16} of the folded neg grid -- the port core at the Bessel-normal coordinates a_m = pi^2 m^2 matched to 0.1 percent, with the coherence knee at k* = 10; and ALL FOUR frozen surgeries KILL the signal -- edge-smoothing, interior smoothing, echo removal, and wrong-Lambda substitution -- so the signal is the ENTIRE multiplicative von Mangoldt comb: NO smaller or smoother sub-object (edge zone, interior zone, echo subset, non-multiplicative masses) carries it.  NET: the arithmetic of the wall is COLLECTIVE at both levels measured -- the one-step factor law is one-sided and non-decompositional over primes, and the deep-core coherence needs the whole comb; this is the measured ground on which v892's fixed 8x8 Schur core stands.  NO RH claim; no marker moves; leverage censuses and surgery kills are measurements on compressed truncations, not theorems about zeros.  Float64 on the deployed v563 machinery (READ-ONLY); no zeros, no prime oracles (AST firewalls inside the probes); RNG only in declared scramble controls.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes factor_avoidance_euler_probe.py
(18/18, FACTORAVOID-MEASURED, SPEC v2 after run 1: the Q < 0
smooth count anchored to the predecessor's PRINTED C2 ledger (the
round-50 brief's "13x" was a transcription slip), two ward anchors
and the degenerate-split hybrid trichotomy documented -- no bar
moved to rescue anything; SPEC v3 after run 2: the A3 grain typing
gains the decomposition-validity precondition after run 2 measured
the leave-outs NON-DECOMPOSITIONAL -- every run-2 raw number
stands and is reprinted unchanged), deepcore_anatomy_probe.py
(12/12, DEEPCORE-MEASURED, frozen + SHA-hashed before first run),
both round 50, 2026-08-09, re-run identically at promotion.
ROUND-31 EMBEDDING CONVENTION: frozen sources embedded BYTE-EXACT,
executed verbatim in isolated namespaces; printed spec SHAs
reproduce; byte-equality ward vs experiments/tfpt-discovery/
inside the pattern gates.  All probes consume the READ-ONLY
deployed core v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles; all fail-first spec
amendments preserved; the leverage census is typed as a census,
NOT a decomposition; surgery kills are negative controls of the
remnant, not positivity claims.  NO RH claim.
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

# ------------- frozen probe source factor_avoidance_euler_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""factor_avoidance_euler_probe -- PRIME.PORT.FACTORAVOID.01
(EXPLORATION ONLY, experiments/; round 50, follow-up (b) of the
tau_mobius_factor run: WHY does the truth ladder keep every
determinant factor away from -1 while every smooth-world control
crosses?  Factor anatomy vs the exact Euler cascade structure.
2026-08-09.)

THE QUESTION (frozen): tau_mobius_factor_probe measured the exact
factorization Q_h = det(W_{h+1})/det(W_h) = prod_i (1 + mu_i),
mu_i = eig(W_h^{-1} Delta C) on the 12x12 window (truth: 0
crossings on 31/31 steps, min 1+mu = 0.0050; smooth-mass world:
crossings on 22/28 steps, first at h 210->218).  The rung
increment Delta C is driven by (i) window geometry change
(alpha, D, M shift) and (ii) the entering/leaving prime atoms
(euler_scattering: the window comb IS the tent-weighted
per-prime Blaschke cascade, bitwise).  Three candidate anatomies
for the truth's factor avoidance: (A) SIZE -- a norm bound
rho(W^{-1} Delta C) < 1 per step; (B) STRUCTURE -- rho > 1
sometimes but the crossings still avoided; (C) CANCELLATION
between the geometry part and the atom part.

THE MINI-THEOREM (stated up front; elementary): let W_h = I - C_J
be symmetric POSITIVE DEFINITE and Delta C symmetric, with
W_{h+1} = W_h + Delta C.  Then W_h^{-1} Delta C is similar to the
SYMMETRIC matrix S = W_h^{-1/2} Delta C W_h^{-1/2}, so its
eigenvalues mu_i are REAL, and W_{h+1} = W_h^{1/2} (I + S)
W_h^{1/2}.  Hence
    rho(W_h^{-1} Delta C) < 1
      ==>  every mu_i lies in (-1, 1)
      ==>  every factor 1 + mu_i > 0
      ==>  Q_h > 0  AND  W_{h+1} is again positive definite --
positivity inheritance in ONE step, from ONE norm bound.
Conversely a factor crossing (some 1 + mu_i < 0) forces
rho >= |mu_i| > 1.  (Remark for the indefinite branch: for REAL
W_h the mu-spectrum is closed under conjugation, so rho < 1
still forces Q_h = prod(1 + mu_i) > 0 -- real mu in (-1, 1) give
positive factors, complex ones pair into |1 + mu|^2 -- but the
PD inheritance needs W_h PD.)  If the truth ladder has rho < 1
on every step, the induction theorem shape is a NORM BOUND on
W^{-1} Delta C; the ONE-SIDED weakening min_i mu_i > -1 is
exactly PD inheritance itself (no norm reduction).

THE LADDER (frozen, tau_mobius_factor verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive FULL-WINDOW pairs (both rungs carry all 12 indices
of J = {2, 4, ..., 24}; typed skips counted); truth + smooth-
mass world (B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n,
midpoint cells, lattice_parametrix verbatim); Epstein/scramble
frame status reported (C1).

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 A0  REPRODUCTION WARD (kill -> WARD-BROKEN): the tau_mobius
     T1/C2 census must reproduce at print precision: truth 31
     full-window pairs, 0 crossing steps, ladder min(1 + mu) =
     0.0050 (tol 5.001e-5); smooth 28 full-window pairs, 22
     crossing steps (Q < 0 or a real factor < 0), first
     crossing at h 210 -> 218, Q < 0 count == predecessor
     ledger.  Factorization ward |prod(1 + mu) - Q| <= 1e-10
     rel on truth (kill), <= 1e-8 on smooth (report).

 A1  THE NORM LEDGER: per full-window step, in the exact
     symmetric gauge (truth; PD branch) or the general eigen
     branch (smooth, W possibly indefinite):
       rho = rho(W_h^{-1} Delta C),  ||W_h^{-1}||_2,
       ||Delta C||_2, and the naive product bound
       ||W_h^{-1}||_2 ||Delta C||_2 >= rho;
     plus the atom-flow direction of the step (ENTER/LEAVE,
     from the deployed prefix law).  CENSUS: (i) truth -- is
     rho < 1 on ALL steps (then Q > 0 AND PD inheritance follow
     algebraically per step by the mini-theorem)?  The
     ONE-SIDED census printed separately: max_steps(-min mu)
     (the dangerous side) vs max_steps(max mu) (the harmless
     side).  (ii) smooth -- the crossing correspondence table:
     per step, rho vs the crossing flag; the 2x2 census
     (crossing x rho >= 1).  Crossing ==> rho > 1 is automatic
     (theorem); the informative cell is rho >= 1 WITHOUT
     crossing (the harmless mu > +1 side, counted per world).

 A2  THE DECOMPOSITION (geometry vs atoms): the deployed atom
     set at zone kz is the exact PREFIX U_ALL[:ka(alpha)], so
     between consecutive rungs a suffix block of prime-power
     atoms ENTERS (alpha up) or LEAVES (alpha down).  FROZEN
     CONSTRUCTION: hybrid H = rung (h+1)'s window geometry
     (alpha, M, D of zone b) with rung h's atom SET (comb
     override, deployed builder path bit for bit); split
       Delta_geom  := C_J(a) - C_J(H)
       Delta_atoms := C_J(H) - C_J(b);
     TELESCOPING WARD (kill -> WARD-BROKEN): ||Delta_geom +
     Delta_atoms - Delta C||_F <= 1e-10 * max(1, ||C_J(a)||_F)
     on every step where H builds.  Per step where both parts
     are nonzero: rho_geom, rho_atoms (A1 gauge), alignment
     cos<S_geom, S_atoms>_F in the symmetric gauge, and the
     cancellation index rho_tot / (rho_geom + rho_atoms).

 A3  THE PER-PRIME GRAIN (the Euler question): frozen step
     subset = the 5 MEDIUM truth steps (the middle five of the
     truth full-window step list sorted by h) + the smooth
     world's FIRST crossing step.  Atoms grouped by base prime
     p (positions are log p^k; base recovered by own trial
     division -- v882 own-sieve precedent; every atom MUST
     parse as a prime power, ward).  Per-prime anatomy of the
     step increment (SPEC v2 object, see amendments): the
     LEAVE-ONE-PRIME-OUT response
       Delta_p := (C_a - C_b) - (C_a^{-p} - C_b^{-p}),
     C^{-p} = the rung rebuilt with prime p's full atom group
     deleted (deployed builder, comb override; each world's
     mass convention), for the NP_TOP = 8 largest in-window-
     mass primes of the union prefix; rho_p in the A1 gauge vs
     the step's W_a; the additivity defect ||Delta C - sum_p
     Delta_p||_F / ||Delta C||_F reported (nonlinear
     interaction share, no exactness claimed).  GRAIN TYPE per
     step (frozen bars, SPEC v3 validity precondition): the
     typing REQUIRES a decompositional response -- at least
     NP_TOP/2 = 4 surviving leave-outs (else
     GRAIN-UNDERSAMPLED) and additivity defect <= 1 (else
     GRAIN-NONDECOMPOSITIONAL: the responses are then a
     LEVERAGE census of the window operators, not a
     decomposition of the increment, and are reported as
     such).  Where valid: with top share = max_p rho_p /
     sum_p rho_p over the resolved primes -- GRAIN-DIFFUSE iff
     top share <= 0.5; GRAIN-COHERENT iff >= 0.8; else
     GRAIN-INTERMEDIATE; single share = max_p rho_p / rho_tot
     printed.  Leave-out builds that die are typed
     LEAVEOUT-DEAD (skipped, counted).

 A4  TYPED VERDICT SUBLABELS (frozen bars): with f = fraction
     of truth steps with rho < 1:  AVOIDANCE-NORM iff f = 1
     (the theorem shape exists); AVOIDANCE-MIXED iff
     0.9 <= f < 1; AVOIDANCE-STRUCTURAL iff f < 0.9 (avoided
     without the norm bound -- subtler); plus the A2 split
     labels and the A3 grain labels.

 C   CONTROLS: (C1, kz 9, must fire, kill -> CONTROL-DEAD)
     Epstein (lambda_eps recursion comb) + scramble (seed 1):
     the compressed frame must die (exterior supercritical OR
     lam(C_J) > 1 OR window unavailable); channel reported.
     (C2) the SMOOTH-MASS world is the PRIMARY embedded control
     here; its detection (crossings present) is ward-anchored
     in A0 -- if the smooth ladder shows no crossing the probe
     is CONTROL-DEAD.

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 >= 30 truth
     rungs; W1b the atom prefix law exact; W2 det(W) > 0 on
     every truth full-window rung; W3 >= 20 truth full-window
     pairs; W4 the A2 construction DECIDED on every truth step
     (exact split computed, or hybrid frame death recorded
     with its channel).

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW the
factorization / reproduction / telescoping / grain-parse ward
breaks -> WARD-BROKEN; K3 controls silent -> CONTROL-DEAD.

VERDICT (frozen enum): FACTORAVOID-MEASURED with typed sublabels
AVOIDANCE-NORM / AVOIDANCE-MIXED / AVOIDANCE-STRUCTURAL (A4),
the A2 split labels, the A3 grain labels; else PIPELINE-BROKEN /
WARD-BROKEN / CONTROL-DEAD.

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- every
run-1 measurement stands, no bar was moved to rescue a failing
measurement; two ward anchors and one degenerate-object
bookkeeping were amended, documented here):

 (i)   A0.3 Q < 0 count: the round-50 brief said "Q flips 13x";
       the predecessor's PRINTED C2 ledger (re-run, matched row
       for row against this probe's smooth table, identical Q
       values) has Q < 0 on 16 of 28 steps.  The ward is
       anchored to the verified predecessor output:
       REF_SMOOTH_QNEG = 16.  All other reference numbers
       (31/0/0.0050; 28/22/210->218) confirmed unchanged.

 (ii)  A2 DEGENERACY DISCOVERED (run 1, kept as the measured
       answer): the deployed atoms_in cutoff (u <= 2 alpha) is
       SLAVED to the tent support edge (atom_lags_at uses
       D = 2 alpha / M, so cells cover exactly [0, 2 alpha],
       and an atom at u > 2 alpha contributes EXACTLY ZERO
       weight).  Consequences, both measured in run 1: on every
       LEAVING step Delta_atoms == 0 BITWISE (the moving atoms
       are invisible to the smaller window -- hybrid H equals
       rung b's build bit for bit), and on every ENTERING step
       the hybrid H (grown window WITHOUT its new atoms) FRAME-
       DIES -- the grown window cannot even be built without
       its new atoms.  There is NO separable atom channel:
       option (C) CANCELLATION is structurally dead; the whole
       increment is the geometry re-test of the full comb.  v2
       therefore replaces the v1 dominance/alignment/
       cancellation ladder labels (meaningless on a one-channel
       ladder) by the per-step trichotomy ATOM-NIL /
       FRAME-REQUIRES-ATOMS / SPLIT-NONDEGENERATE with
       censuses (any nondegenerate step still gets the full v1
       row), and W4 becomes the decision census above.  Run-1
       v1-W4 ("split available on >= 0.8") is superseded as a
       bookkeeping error: hybrid frame death IS a decision, not
       a pipeline failure.

 (iii) A3 OBJECT REPLACED (documented): the v1 cumulative
       per-prime ladder of the moving block is answered
       EXACTLY by (ii): the moving atoms carry ZERO of the
       increment through their own tents (leaving steps:
       bitwise zero, verified in run 1 -- all rho_p = 0,
       endpoint dev 0.0e0; entering steps: baseline frame-
       dead).  That IS the Euler-grain answer to the as-posed
       question, and it is printed.  The per-prime anatomy is
       re-posed in the one surviving nondegenerate sense: the
       LEAVE-ONE-PRIME-OUT step response defined in A3 above.
       The v1 cumulative machinery and its telescoping ward
       are retired with it; the parse ward stays.

SPEC v3 (2026-08-09, after run 2; fail-first preserved -- every
run-2 raw number stands and is reprinted unchanged):

 (iv)  A3 GRAIN TYPING gains the decomposition-validity
       precondition stated in A3 above.  Run 2 measured the
       leave-out responses to be NON-DECOMPOSITIONAL: on the
       truth steps sum_p rho_p ~ 1e4 against rho_tot ~ 1-4 and
       additivity defect ~ 1e3 (removing ONE small prime moves
       the window operators by orders of magnitude more than
       the whole step increment -- the response is frame
       leverage, not increment grain), and on the smooth
       crossing step 5 of 8 leave-outs frame-died (defect 8.2,
       3 survivors).  The v2 labels GRAIN-DIFFUSE /
       GRAIN-COHERENT computed on these responses are VOIDED
       as bookkeeping (they typed shares of the wrong object);
       v3 types them GRAIN-NONDECOMPOSITIONAL /
       GRAIN-UNDERSAMPLED and keeps the numbers as a leverage
       census.  THE HONEST A3 ANSWER: the per-prime grain of
       the step increment is NOT accessible in the deployed
       nonlinear pipeline -- the moving-block channel is
       exactly nil (v1/A2), and single-prime deletions do not
       linearize; avoidance and crossing are properties of the
       COLLECTIVE window re-test, not of any single prime's
       move.

 (v)   A2 smooth-world bookkeeping note: 5 smooth LEAVING
       steps type SPLIT-NONDEGENERATE with a TINY atom part
       (||Delta_atoms||_F ~ 1e-12..1e-11, rho_atom ~ 1e-10..
       1e-8): the
       B1 smooth masses are recomputed per lattice (midpoint
       cells), so deleting the moving suffix shifts the LAST
       retained cell's width -- a boundary-cell mass artifact
       of the smooth convention, not a tent contribution of
       the moving atoms (truth masses are per-atom, hence
       bitwise ATOM-NIL there).  Printed with ||Delta_atoms||
       so the scale is visible.

NO RH claim -- a per-step spectral measurement on compressed
window truncations is a statement about the deployed ladder,
not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); the A3 grouping uses an OWN trial-division smallest-
prime-factor routine (allowed, v882 own-sieve precedent),
documented here; v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts (U_ALL / MU_ALL prefix
law, build_window, atom_lags_at, arch_lags -- read verbatim);
window compression + exact quotient factorization + smooth-mass
world verbatim from tau_mobius_factor_probe.py
(PRIME.PORT.TAU.MOEBIUS.01) via port_schur_cocycle_probe.py and
lattice_parametrix_probe.py (B1); euler_scattering_source_probe
(PRIME.EULER.SCATTER.01: the atom table IS the Euler grouping,
exact -- the license for the per-prime grain).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/factor_avoidance_euler_probe.py
"""

import ast
import hashlib
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

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
MIN_RUNGS = 30
MIN_PAIRS_T1 = 20
MIN_COMMON_J = 8
FACT_WARD = 1e-10           # truth factorization ward (kill)
FACT_WARD_SMOOTH = 1e-8     # smooth factorization ward (report)
SPLIT_WARD = 1e-10          # A2 telescoping ward (kill)
NP_TOP = 8                  # A3 leave-out primes
MEDIUM_N = 5                # A3 medium truth steps
GRAIN_DIFFUSE_BAR = 0.5     # A3
GRAIN_COHERENT_BAR = 0.8    # A3
DEFECT_BAR = 1.0            # A3 v3 decomposition-validity bar
MIN_LO_ALIVE = NP_TOP // 2  # A3 v3 undersampling bar
MIXED_FRAC = 0.9            # A4
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# A0 reproduction ward (tau_mobius_factor_probe printed ledger,
# re-verified; SPEC v2 (i))
REF_N_TRUTH_PAIRS = 31
REF_TRUTH_CROSS = 0
REF_TRUTH_MINFAC = 0.0050
REF_N_SMOOTH_PAIRS = 28
REF_SMOOTH_CROSS = 22
REF_SMOOTH_FIRST = (210, 218)
REF_SMOOTH_QNEG = 16
ROUND_TOL = 5.001e-5

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


# --------- pipeline, verbatim from tau_mobius_factor_probe
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
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


def build_rung(kz, scramble_seed=None, comb=None, rr_cache=None):
    rr = (rr_cache if rr_cache is not None
          else core.build_window(kz, scramble_seed=scramble_seed))
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h)


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


def rung_win(kz, scramble_seed=None, comb=None, rr_cache=None):
    """One rung -> 12x12 window compression (tau_mobius_factor
    rung_all verbatim, MINUS the dressed-port/IIKS block which
    does not feed C_J)."""
    b = build_rung(kz, scramble_seed=scramble_seed, comb=comb,
                   rr_cache=rr_cache)
    h, L = b["h"], b["L"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, alpha=b["alpha"],
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["CJ"] = CJ
        out["jav"] = jav
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    return out


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


# ------------------------------------------- smooth-mass world (B1)
def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smooth_masses(uu):
    """B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n (verbatim)."""
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


# ------------------------------------------- factor machinery
def logdet_sgn(W):
    sgn, ld = np.linalg.slogdet(W)
    return float(sgn), float(ld)


def pd_gauge(Wa):
    """W_a^{-1/2} for symmetric PD W_a, else None."""
    ew, Vw = np.linalg.eigh(Wa)
    if ew[0] <= 0.0:
        return None, ew
    return Vw @ np.diag(ew ** -0.5) @ Vw.T, ew


def sym_mu(Wisq, D):
    """Exact real spectrum of W^{-1}D in the symmetric gauge."""
    S = Wisq @ D @ Wisq
    return np.linalg.eigvalsh(0.5 * (S + S.T))


def gen_mu(Wa, D):
    """General (complex-capable) spectrum of Wa^{-1} D."""
    try:
        return np.linalg.eig(np.linalg.solve(Wa, D))[0]
    except np.linalg.LinAlgError:
        return None


def mu_stats(mu):
    """(rho, min real factor, max real mu, n real fac < 0, near)."""
    mu = np.asarray(mu, complex)
    rho = float(np.max(np.abs(mu))) if len(mu) else 0.0
    real_m = np.abs(mu.imag) <= 1e-9 * (1.0 + np.abs(mu))
    mur = mu.real[real_m]
    fac_r = 1.0 + mur
    mn = float(np.min(fac_r)) if len(fac_r) else float("nan")
    mx = float(np.max(mur)) if len(mur) else float("nan")
    return (rho, mn, mx, int(np.sum(fac_r < 0.0)),
            int(np.sum(np.abs(fac_r) < 0.1)))


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


# ------------------------------------------- own prime machinery
def spf_own(n):
    """Own trial-division smallest prime factor (v882 own-sieve
    precedent; no oracle imports)."""
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n


def prime_power_base(u):
    """Base prime p of the atom at position u = log(p^k); None if
    the recovered integer is not a prime power (ward)."""
    n = int(round(math.exp(u)))
    if n < 2 or abs(math.exp(u) - n) > 1e-6 * n:
        return None
    p = spf_own(n)
    m = n
    while m % p == 0:
        m //= p
    return p if m == 1 else None


# ------------------------------------------------------------- pairs
def factor_pairs(rungs, rrs, general=False):
    """Consecutive full-window pairs with the exact factorization
    + the A1 norm ledger.  Rows keep rung references for A2/A3."""
    rows = []
    n_skip = 0
    for k, (ra, rb) in enumerate(zip(rungs[:-1], rungs[1:])):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        n = len(JWIN)
        Wa = np.eye(n) - ra["CJ"]
        Wb = np.eye(n) - rb["CJ"]
        sga, lda = logdet_sgn(Wa)
        sgb, ldb = logdet_sgn(Wb)
        Q = sga * sgb * math.exp(ldb - lda)
        DC = ra["CJ"] - rb["CJ"]           # W_b = W_a + DC
        Wisq, ewa = pd_gauge(Wa)
        if general or Wisq is None:
            mu = gen_mu(Wa, DC)
            if mu is None:
                n_skip += 1
                continue
            gauge = "GEN"
        else:
            mu = sym_mu(Wisq, DC)
            gauge = "SYM"
        prod = complex(np.prod(1.0 + np.asarray(mu, complex)))
        dev = abs(prod - Q) / max(abs(Q), 1e-300)
        rho, min_fac, max_mu, n_neg, n_near = mu_stats(mu)
        winv = 1.0 / float(np.min(np.abs(ewa)))
        dcn = float(np.max(np.abs(np.linalg.eigvalsh(
            0.5 * (DC + DC.T)))))
        ka = int(rrs[ra["kz"]]["n_atom"])
        kb = int(rrs[rb["kz"]]["n_atom"])
        rows.append(dict(
            k=k, ra=ra, rb=rb, ha=ra["h"], hb=rb["h"],
            kza=ra["kz"], kzb=rb["kz"], ka=ka, kb=kb,
            flow=("ENTER" if kb > ka else
                  "LEAVE" if kb < ka else "NONE"),
            Q=Q, dev=dev, rho=rho, min_fac=min_fac,
            max_mu=max_mu, n_neg=n_neg, n_near=n_near,
            winv=winv, dcn=dcn, bound=winv * dcn,
            Wisq=Wisq, Wa=Wa, DC=DC, gauge=gauge,
            pd=bool(Wisq is not None),
            cross=bool(Q < 0.0 or (np.isfinite(min_fac)
                                   and min_fac < 0.0))))
    return rows, n_skip


def part_rho(row, D):
    """rho of W_a^{-1} D in the row's A1 gauge."""
    if row["gauge"] == "SYM":
        mu = sym_mu(row["Wisq"], D)
    else:
        mu = gen_mu(row["Wa"], D)
        if mu is None:
            return float("nan")
    return float(np.max(np.abs(mu))) if len(mu) else 0.0


def align_cos(row, Dg, Da):
    """Alignment cosine (symmetric gauge if PD, else raw)."""
    if row["gauge"] == "SYM":
        Sg = row["Wisq"] @ Dg @ row["Wisq"]
        Sa = row["Wisq"] @ Da @ row["Wisq"]
    else:
        Sg, Sa = Dg, Da
    ng = float(np.linalg.norm(Sg))
    na = float(np.linalg.norm(Sa))
    if ng <= 0.0 or na <= 0.0:
        return float("nan")
    return float(np.sum(Sg * Sa) / (ng * na))


def comb_of(idx_set, world):
    """Comb arrays for an index set into U_ALL (frozen: truth =
    deployed masses; smooth = B1 masses recomputed on the set's
    own lattice, the per-rung smooth convention)."""
    ii = np.array(sorted(idx_set), dtype=int)
    uu = np.asarray(core.U_ALL, float)[ii]
    if world == "truth":
        return uu, np.asarray(core.MU_ALL, float)[ii]
    return uu, smooth_masses(uu)


def death_channel(hy):
    """Classify a failed hybrid/leave-out build."""
    if not isinstance(hy, dict):
        return "CHAIN-DEATH"
    if "CJ" not in hy:
        return "WINDOW-LOST"
    if not hy.get("full"):
        return "PARTIAL-WINDOW"
    return None


def main():
    section("PRIME.PORT.FACTORAVOID.01 -- factor avoidance vs the "
            "Euler cascade anatomy (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (own trial division, no "
          "oracles)", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth + smooth-mass ladders (all "
            "frame-A zones, h <= %d)" % H_DEEP_MAX)
    rungs, srungs = [], []
    rrs = {}
    n_smooth_dead = 0
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        r = rung_win(kz, rr_cache=rr)
        if not isinstance(r, dict):
            continue
        rrs[kz] = rr
        rungs.append(r)
        uu = np.asarray(rr["uu"], float)
        rs = rung_win(kz, comb=(uu, smooth_masses(uu)),
                      rr_cache=rr)
        if isinstance(rs, dict):
            srungs.append(rs)
        else:
            n_smooth_dead += 1
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    srungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs, h %d .. %d | smooth-mass: %d "
          "rungs, %d chain/window deaths"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             len(srungs), n_smooth_dead))
    pref_dev = max(float(np.max(np.abs(
        2.0 * np.asarray(rr["lam"], float)
        - np.asarray(core.MU_ALL, float)[:int(rr["n_atom"])])))
        for rr in rrs.values())
    check("W1 >= %d truth rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W1b atom prefix law exact (max |mm - MU_ALL prefix| "
          "%.1e == 0)" % pref_dev, pref_dev == 0.0, kill="K1")

    # ------------------------------------------------------- A0/A1
    trows, n_skip_t = factor_pairs(rungs, rrs, general=False)
    srows, n_skip_s = factor_pairs(srungs, rrs, general=True)
    section("A1 -- THE NORM LEDGER, truth (%d full-window pairs; "
            "%d typed skips)" % (len(trows), n_skip_t))
    print("    rho = rho(W_h^{-1} Delta C) in the exact "
          "symmetric gauge; bound = ||W^{-1}||_2 ||Delta C||_2")
    print("    step        flow    rho     rho<1  ||W^-1||    "
          "||dC||    bound     bnd<1  min(1+mu) max(mu)  near")
    for r in trows:
        print("    h %3d->%3d %-5s %8.4f  %-5s  %9.1f   %.5f  "
              "%9.1f  %-5s  %+.4f   %+8.3f   %d"
              % (r["ha"], r["hb"], r["flow"], r["rho"],
                 str(r["rho"] < 1.0), r["winv"], r["dcn"],
                 r["bound"], str(r["bound"] < 1.0),
                 r["min_fac"], r["max_mu"], r["n_near"]))
    pd_ok = all(r["pd"] for r in trows)
    check("W2 det(W) > 0 and W PD on every truth full-window "
          "rung (all pairs SYM gauge)", pd_ok, kill="K1")
    check("W3 >= %d truth full-window pairs" % MIN_PAIRS_T1,
          len(trows) >= MIN_PAIRS_T1, "%d" % len(trows),
          kill="K1")
    dev_max = float(np.max([r["dev"] for r in trows]))
    check("A0.1 truth factorization ward: max rel dev %.2e <= "
          "%.0e" % (dev_max, FACT_WARD), dev_max <= FACT_WARD,
          kill="KW")
    n_cross_t = sum(1 for r in trows if r["cross"])
    minfac_t = float(np.min([r["min_fac"] for r in trows]))
    check("A0.2 REPRODUCTION (truth): %d pairs == %d, %d "
          "crossings == %d, ladder min(1+mu) %.4f == %.4f "
          "(tol %.1e)"
          % (len(trows), REF_N_TRUTH_PAIRS, n_cross_t,
             REF_TRUTH_CROSS, minfac_t, REF_TRUTH_MINFAC,
             ROUND_TOL),
          len(trows) == REF_N_TRUTH_PAIRS
          and n_cross_t == REF_TRUTH_CROSS
          and abs(minfac_t - REF_TRUTH_MINFAC) <= ROUND_TOL,
          kill="KW")
    rho_t = np.array([r["rho"] for r in trows])
    n_lt1 = int(np.sum(rho_t < 1.0))
    n_bnd = sum(1 for r in trows if r["bound"] < 1.0)
    frac_lt1 = n_lt1 / float(len(trows))
    neg_side = float(np.max([1.0 - r["min_fac"] for r in trows]))
    pos_side = float(np.max([r["max_mu"] for r in trows]))
    n_harmless = sum(1 for r in trows
                     if r["rho"] >= 1.0 and r["min_fac"] > 0.0)
    print("\n    TRUTH CENSUS: rho < 1 on %d/%d steps (max rho "
          "%.4f); naive product bound < 1 on %d/%d"
          % (n_lt1, len(trows), float(np.max(rho_t)), n_bnd,
             len(trows)))
    print("    ONE-SIDED CENSUS: dangerous side max(-min mu) = "
          "%.4f (< 1 on ALL steps: %s); harmless side"
          % (neg_side, neg_side < 1.0))
    print("    max(mu) up to %+.3f; ALL %d rho >= 1 steps are "
          "harmless-side (min factor > 0 there: %s)"
          % (pos_side, len(trows) - n_lt1,
             n_harmless == len(trows) - n_lt1))
    print("    rho ladder: %s" % quart(rho_t))
    check("A1.1 truth rho census reported (rho < 1 on %d/%d)"
          % (n_lt1, len(trows)), True)

    section("A1 -- THE NORM LEDGER, smooth-mass world (%d pairs; "
            "%d typed skips) + crossing correspondence"
            % (len(srows), n_skip_s))
    print("    step        flow    rho     rho<1  W_a PD  "
          "min(1+mu)  cross  Q")
    for r in srows:
        print("    h %3d->%3d %-5s %9.4f %-5s  %-5s   %s   "
              "%-5s  %+.3e%s"
              % (r["ha"], r["hb"], r["flow"], r["rho"],
                 str(r["rho"] < 1.0), str(r["pd"]),
                 ("%+9.4f" % r["min_fac"])
                 if np.isfinite(r["min_fac"]) else "    n/a  ",
                 str(r["cross"]), r["Q"],
                 "  <-- CROSSING" if r["cross"] else ""))
    sdev_max = float(np.max([r["dev"] for r in srows]))
    print("    smooth factorization ward (general eig): max rel "
          "dev %.2e vs %.0e (%s)"
          % (sdev_max, FACT_WARD_SMOOTH,
             "ok" if sdev_max <= FACT_WARD_SMOOTH
             else "EXCEEDED -- reported"))
    n_cross_s = sum(1 for r in srows if r["cross"])
    n_qneg = sum(1 for r in srows if r["Q"] < 0.0)
    first_s = next((r for r in srows if r["cross"]), None)
    first_hh = ((first_s["ha"], first_s["hb"])
                if first_s is not None else (-1, -1))
    check("A0.3 REPRODUCTION (smooth): %d pairs == %d, %d "
          "crossing steps == %d, first at h %d->%d == %d->%d, "
          "Q < 0 on %d == %d (predecessor ledger, SPEC v2 (i))"
          % (len(srows), REF_N_SMOOTH_PAIRS, n_cross_s,
             REF_SMOOTH_CROSS, first_hh[0], first_hh[1],
             REF_SMOOTH_FIRST[0], REF_SMOOTH_FIRST[1],
             n_qneg, REF_SMOOTH_QNEG),
          len(srows) == REF_N_SMOOTH_PAIRS
          and n_cross_s == REF_SMOOTH_CROSS
          and first_hh == REF_SMOOTH_FIRST
          and n_qneg == REF_SMOOTH_QNEG, kill="KW")
    c11 = sum(1 for r in srows if r["cross"] and r["rho"] >= 1.0)
    c10 = sum(1 for r in srows if r["cross"] and r["rho"] < 1.0)
    c01 = sum(1 for r in srows
              if not r["cross"] and r["rho"] >= 1.0)
    c00 = sum(1 for r in srows
              if not r["cross"] and r["rho"] < 1.0)
    print("\n    2x2 CENSUS (smooth): cross & rho>=1: %d | cross "
          "& rho<1: %d | no-cross & rho>=1: %d | no-cross & "
          "rho<1: %d" % (c11, c10, c01, c00))
    print("    (crossing ==> rho > 1 is the theorem direction; "
          "the harmless cell is no-cross & rho>=1.)")
    check("A1.2 smooth correspondence: every crossing step has "
          "rho >= 1 (%d/%d)" % (c11, n_cross_s), c10 == 0)

    print("\n    THE MINI-THEOREM (stated): W_h symmetric PD + "
          "Delta C symmetric ==> mu real (symmetric")
    print("    similarity), and rho(W_h^{-1} Delta C) < 1 ==> "
          "every 1 + mu_i > 0 ==> Q_h > 0 AND W_{h+1} PD.")
    print("    A crossing forces rho > 1.  Truth rho < 1 "
          "everywhere would make avoidance a NORM BOUND.")

    # ------------------------------------------------------------ A2
    section("A2 -- THE DECOMPOSITION Delta C = Delta_geom + "
            "Delta_atoms (hybrid builds; SPEC v2 trichotomy)")
    print("    hybrid H = geometry(b) + atom set(a); Delta_geom "
          "= C(a) - C(H); Delta_atoms = C(H) - C(b)")

    def split_decide(rows, world):
        dec = []
        tel_max = 0.0
        for r in rows:
            ka = r["ka"]
            hy = rung_win(r["kzb"],
                          comb=comb_of(range(ka), world),
                          rr_cache=rrs[r["kzb"]])
            ch = death_channel(hy)
            if ch is not None:
                dec.append(dict(r=r, typ="FRAME-REQUIRES-ATOMS",
                                chan=ch))
                continue
            Dg = r["ra"]["CJ"] - hy["CJ"]
            Da = hy["CJ"] - r["rb"]["CJ"]
            tel_max = max(tel_max, float(
                np.linalg.norm(Dg + Da - r["DC"]))
                / max(1.0, float(np.linalg.norm(r["ra"]["CJ"]))))
            if float(np.linalg.norm(Da)) == 0.0:
                dec.append(dict(r=r, typ="ATOM-NIL", hyCJ=hy["CJ"],
                                Dg=Dg, Da=Da))
            else:
                dec.append(dict(
                    r=r, typ="SPLIT-NONDEGENERATE", hyCJ=hy["CJ"],
                    Dg=Dg, Da=Da, rg=part_rho(r, Dg),
                    ra_=part_rho(r, Da), al=align_cos(r, Dg, Da)))
        return dec, tel_max

    def split_report(name, rows, world):
        dec, tel_max = split_decide(rows, world)
        n_nil = sum(1 for d in dec if d["typ"] == "ATOM-NIL")
        n_dead = sum(1 for d in dec
                     if d["typ"] == "FRAME-REQUIRES-ATOMS")
        n_non = len(dec) - n_nil - n_dead
        print("\n    %s: %d steps -> ATOM-NIL %d | FRAME-"
              "REQUIRES-ATOMS %d | SPLIT-NONDEGENERATE %d"
              % (name, len(dec), n_nil, n_dead, n_non))
        for d in dec:
            r = d["r"]
            if d["typ"] == "FRAME-REQUIRES-ATOMS":
                print("    h %3d->%3d %-5s FRAME-REQUIRES-ATOMS "
                      "(%s): grown window w/o its new atoms "
                      "does not build"
                      % (r["ha"], r["hb"], r["flow"], d["chan"]))
            elif d["typ"] == "ATOM-NIL":
                print("    h %3d->%3d %-5s ATOM-NIL: "
                      "||Delta_atoms||_F == 0 bitwise; "
                      "rho_geom = rho_tot = %.4f"
                      % (r["ha"], r["hb"], r["flow"], r["rho"]))
            else:
                print("    h %3d->%3d %-5s NONDEGENERATE: "
                      "rho_geom %.4f rho_atom %.2e "
                      "(||Da|| %.1e) align %+.3f"
                      % (r["ha"], r["hb"], r["flow"], d["rg"],
                         d["ra_"],
                         float(np.linalg.norm(d["Da"])),
                         d["al"]))
        if n_non and world == "smooth":
            print("    (smooth NONDEGENERATE rows: boundary-"
                  "cell mass artifact of the per-lattice B1 "
                  "convention, SPEC v3 (v).)")
        return dec, tel_max, (n_nil, n_dead, n_non)

    tdec, tel_t, tcns = split_report("TRUTH", trows, "truth")
    sdec, tel_s, scns = split_report("SMOOTH", srows, "smooth")
    n_flow_mismatch = sum(
        1 for d in tdec + sdec
        if (d["typ"] == "ATOM-NIL" and d["r"]["flow"] == "ENTER")
        or (d["typ"] == "FRAME-REQUIRES-ATOMS"
            and d["r"]["flow"] == "LEAVE"))
    print("\n    STRUCTURAL STATEMENT (exact): the deployed atom "
          "cutoff u <= 2 alpha is SLAVED to the tent")
    print("    support edge M*D = 2 alpha, so a LEAVING block is "
          "invisible to the smaller window (atom part")
    print("    exactly zero) and an ENTERING block is load-"
          "bearing for the grown window (hybrid frame dies).")
    print("    There is NO separable atom channel; option (C) "
          "CANCELLATION is structurally dead.  Type/flow")
    print("    correspondence violated on %d steps."
          % n_flow_mismatch)
    check("W4 A2 decided on every step (truth %d + smooth %d)"
          % (len(tdec), len(sdec)),
          len(tdec) == len(trows) and len(sdec) == len(srows),
          kill="K1")
    tel_max = max(tel_t, tel_s)
    check("A2.1 TELESCOPING WARD (where H builds): max rel "
          "|Dg + Da - DC| %.2e <= %.0e" % (tel_max, SPLIT_WARD),
          tel_max <= SPLIT_WARD, kill="KW")
    a2_lab_t = ("SPLIT-DEGENERATE(nil %d, framedead %d)"
                % tcns[:2] if tcns[2] == 0
                else "SPLIT-PARTLY-NONDEGENERATE(%d)" % tcns[2])
    check("A2.2 truth split typed: %s" % a2_lab_t, True)

    # ------------------------------------------------------------ A3
    section("A3 -- THE PER-PRIME GRAIN (5 medium truth steps + "
            "the smooth first crossing step; SPEC v2 leave-out)")
    print("    v1 answer (kept, exact): the moving block carries "
          "ZERO of the increment through its own tents")
    print("    (LEAVE: bitwise zero; ENTER: baseline frame-dead)."
          "  v2 object: Delta_p = (C_a - C_b) -")
    print("    (C_a^{-p} - C_b^{-p}), leave-one-prime-out of the "
          "%d largest in-window-mass primes." % NP_TOP)
    tdec_by_k = {d["r"]["k"]: d for d in tdec}
    i0 = (len(trows) - MEDIUM_N) // 2
    a3_jobs = [("truth", trows[i]) for i in
               range(i0, i0 + MEDIUM_N)]
    if first_s is not None:
        a3_jobs.append(("smooth", first_s))
    grain_truth, grain_smooth = [], []
    parse_ok = True
    for world, r in a3_jobs:
        d2 = tdec_by_k.get(r["k"]) if world == "truth" else None
        ka, kb = r["ka"], r["kb"]
        ku = max(ka, kb)
        groups = {}
        for i in range(ku):
            p = prime_power_base(float(core.U_ALL[i]))
            if p is None:
                parse_ok = False
                continue
            groups.setdefault(p, []).append(i)
        masses = {p: float(np.sum(np.abs(
            np.asarray(core.MU_ALL, float)[g])))
            for p, g in groups.items()}
        order = sorted(groups, key=lambda p: -masses[p])[:NP_TOP]
        mtot = sum(masses.values())
        print("\n  %s h %d->%d (kz %d->%d, %s %d atoms; v1 "
              "moving-block answer: %s)"
              % (world.upper(), r["ha"], r["hb"], r["kza"],
                 r["kzb"], r["flow"], abs(kb - ka),
                 (d2["typ"] if d2 is not None else
                  "see A2 smooth census")))
        rows_p = []
        n_lo_dead = 0
        for p in order:
            gset = set(groups[p])
            ca = rung_win(r["kza"],
                          comb=comb_of(
                              [i for i in range(ka)
                               if i not in gset], world),
                          rr_cache=rrs[r["kza"]])
            cb = rung_win(r["kzb"],
                          comb=comb_of(
                              [i for i in range(kb)
                               if i not in gset], world),
                          rr_cache=rrs[r["kzb"]])
            if (death_channel(ca) is not None
                    or death_channel(cb) is not None):
                n_lo_dead += 1
                print("    p %-6d LEAVEOUT-DEAD (a: %s, b: %s)"
                      % (p, death_channel(ca) or "ok",
                         death_channel(cb) or "ok"))
                continue
            Dp = r["DC"] - (ca["CJ"] - cb["CJ"])
            rows_p.append((p, len(groups[p]),
                           masses[p] / mtot, part_rho(r, Dp),
                           Dp))
        if not rows_p:
            print("    A3-UNAVAILABLE (all leave-outs dead)")
            continue
        sum_p = sum(x[3] for x in rows_p)
        top = max(x[3] for x in rows_p)
        top_share = top / sum_p if sum_p > 0 else float("nan")
        single = top / r["rho"] if r["rho"] > 0 else float("nan")
        resid = r["DC"] - sum((x[4] for x in rows_p),
                              np.zeros_like(r["DC"]))
        resid_share = (float(np.linalg.norm(resid))
                       / max(float(np.linalg.norm(r["DC"])),
                             1e-300))
        print("    p       n_pow  mass%%   rho_p     rho_p/sum")
        for p, npow, ms, rp, _ in rows_p:
            print("    %-7d %4d   %5.1f   %8.4f  %.3f"
                  % (p, npow, 100.0 * ms, rp,
                     rp / sum_p if sum_p > 0 else 0.0))
        if len(rows_p) < MIN_LO_ALIVE:
            gtype = "GRAIN-UNDERSAMPLED"
        elif resid_share > DEFECT_BAR:
            gtype = "GRAIN-NONDECOMPOSITIONAL"
        else:
            gtype = ("GRAIN-DIFFUSE"
                     if top_share <= GRAIN_DIFFUSE_BAR
                     else "GRAIN-COHERENT"
                     if top_share >= GRAIN_COHERENT_BAR
                     else "GRAIN-INTERMEDIATE")
        print("    sum_p rho_p %.4f | rho_tot %.4f | top share "
              "%.3f | single share %.3f | additivity defect "
              "||resid||/||DC|| %.3f | leave-out dead %d -> %s"
              % (sum_p, r["rho"], top_share, single,
                 resid_share, n_lo_dead, gtype))
        if gtype in ("GRAIN-NONDECOMPOSITIONAL",
                     "GRAIN-UNDERSAMPLED"):
            print("    (v3: responses are frame LEVERAGE, not "
                  "increment grain -- shares not typed as "
                  "anatomy.)")
        (grain_truth if world == "truth"
         else grain_smooth).append(gtype)
    check("A3.1 grain parse ward: every window atom is a prime "
          "power (own trial division)", parse_ok, kill="KW")
    gt = (max(set(grain_truth), key=grain_truth.count)
          if grain_truth else "GRAIN-UNAVAILABLE")
    gs = grain_smooth[0] if grain_smooth else "GRAIN-UNAVAILABLE"
    print("\n    GRAIN ANSWER (v3): moving-block channel = "
          "EXACTLY NIL (v1, A2); leave-out anatomy: truth")
    print("    (modal of %d steps) = %s | smooth crossing "
          "step = %s" % (len(grain_truth), gt, gs))
    print("    PLAIN: the per-prime grain of the step increment "
          "is NOT accessible -- no single prime's move")
    print("    carries the avoidance or the crossing; both live "
          "in the COLLECTIVE window re-test.")
    check("A3.2 grain typed: truth %s, smooth-cross %s"
          % (gt, gs), True)

    # ------------------------------------------------------------ A4
    section("A4 -- TYPED AVOIDANCE")
    avoid = ("AVOIDANCE-NORM" if frac_lt1 == 1.0 else
             "AVOIDANCE-MIXED" if frac_lt1 >= MIXED_FRAC else
             "AVOIDANCE-STRUCTURAL")
    print("    truth rho < 1 on %d/%d (frac %.3f; bars: NORM = "
          "1.0, MIXED >= %.2f)" % (n_lt1, len(trows), frac_lt1,
                                   MIXED_FRAC))
    check("A4.1 typed: %s" % avoid, True)
    if avoid == "AVOIDANCE-NORM":
        print("\n    PLAIN STATEMENT (typed, not claimed): the "
              "induction theorem shape is a NORM BOUND --")
        print("    rho(W_h^{-1} Delta C_h) < 1 per step forces "
              "1 + mu_i > 0 for every factor, hence Q_h > 0")
        print("    and W_{h+1} PD, by the symmetric-similarity "
              "mini-theorem above.")
    else:
        print("\n    PLAIN STATEMENT (typed, not claimed): the "
              "norm-bound theorem shape FAILS -- rho is >= 1")
        print("    on %d/%d truth steps, always via the HARMLESS "
              "side (max mu up to %+.2f, min factor still"
              % (len(trows) - n_lt1, len(trows), pos_side))
        print("    > 0 there).  The avoidance is ONE-SIDED: "
              "max(-min mu) = %.4f < 1 across the ladder."
              % neg_side)
        print("    The inheritance statement is the one-sided "
              "bound lambda_min(W^{-1/2} DC W^{-1/2}) > -1,")
        print("    which IS PD inheritance itself -- no "
              "reduction to a two-sided operator norm.")

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C1 -- Epstein/scramble (kz %d, frame must die):"
          % CTRL_KZ)
    ok1 = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = rung_win(CTRL_KZ, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
            continue
        if "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES"
                  % nmc)
            continue
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        ok1 &= fired
        print("    %-8s: lam(out) %.3e | lam(C_J) %.3e -> fires "
              "via %s"
              % (nmc, rc["lamO"], rc["lamC"],
                 "EXTERIOR" if rc["lamO"] > 1.0 else
                 "WINDOW" if rc["lamC"] > 1.0 else "NOTHING"))
    check("C1 CONTROLS FIRE (frame death or supercriticality)",
          ok1, kill="K3")
    print("  C2 -- smooth-mass world: PRIMARY embedded control; "
          "crossings ward-anchored in A0.3 (%d crossing steps)."
          % n_cross_s)
    check("C2 smooth detector fired (%d crossings)" % n_cross_s,
          n_cross_s > 0, kill="K3")

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("FACTORAVOID-MEASURED / %s / %s / "
                   "GRAIN(truth=%s, smoothcross=%s)"
                   % (avoid, a2_lab_t, gt, gs))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (truth rho < 1 on %d/%d, max rho %.4f, one-"
              "sided margin max(-min mu) %.4f; smooth 2x2 = "
              "%d/%d/%d/%d)"
              % (n_lt1, len(trows), float(np.max(rho_t)),
                 neg_side, c11, c10, c01, c00))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source deepcore_anatomy_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deepcore_anatomy_probe -- PRIME.PORT.DEEPCORE.01 (EXPLORATION
ONLY, experiments/; round 50, follow-up (c) of the Moebius kill
battery: dissect the surviving arithmetic remnant, 2026-08-09).

THE QUESTION (frozen): the round-48 Moebius firewall
(mobius_crossratio_firewall_probe, PRIME.PORT.MOEBIUS.
CRFIREWALL.01) killed the full-coverage cross-ratio invariance
(CR-DEAD) but its report-only DEEP-CORE sub-battery survived at
certificate level: the 8 DEEPEST common port nodes of consecutive
rungs carry cross-ratio coherence med ~ 4.3e-4 in the raw carrier
r = g/f -- fit-free and gauge-free -- while the smooth-mass world
(PNT-mean masses 2 e^{u/2} du on the true prime-power lattice)
loses it (~ 2.7e-2).  This probe dissects the remnant: WHICH
nodes, WHICH Lambda signal, WHAT structure carries it.

THE COMB (frozen, v563 verbatim): atoms at u_n = log n on the
prime powers n = p^k with masses 2 Lambda(n) / sqrt(n); a window
at zone kz covers u in (0, 2 alpha], alpha = U_ALL[kz].  The
carrier pairs (g_j, f_j) are the IIKS generators of the dressed
port commutator [Y, D_P] (port_schur_cocycle / iiks_gauge_firewall
extraction, SPEC v2, verbatim), in the frozen one-point SO(2)
extraction gauge (a chordal isometry: cross-ratios are exactly
gauge-free).  The ladder: all frame-A zones with h <= 900 sorted
by (h, kz); consecutive pairs (k = 1) with >= 8 common port alias
indices.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; all bars frozen before the run):

 D1  NODE IDENTIFICATION: per k = 1 step print the 8 deepest
     common alias indices (the deep core) -- the census along the
     ladder; the alias frequency table; the modal deep-8 set and
     the fraction of steps whose deep core equals it exactly.
     TYPED: ALIAS-FIXED iff >= 90% of steps carry the identical
     modal set; ALIAS-DRIFTING otherwise.  Explicitly compared to
     the even set {2, 4, ..., 16}.  ANATOMY on three
     representative rungs (shallowest / middle / deepest): alias
     j, y_j, tau_j, and the Bessel-normal coordinate a_m =
     2 h^2 (1 - y_m) against pi^2 m^2 (christoffel H5
     cross-reference: on the folded grid y = cos(2 pi j / L),
     L ~ 4h, so alias j = 2m sits at a_m ~ pi^2 m^2 -- the port
     core).  TYPED (deepest rung): PORTCORE-MATCH iff
     max_m |a_m / (pi^2 m^2) - 1| <= 0.10 over m = 1..8;
     PORTCORE-OFF otherwise.

 D2  COHERENCE PROFILE: the deep-core cross-ratio battery
     (machinery verbatim from the firewall probe: conditioning
     min pairwise chordal >= 1e-3 x within-quadruple spread on
     both rungs, |cr| in [1e-3, 1e3] both rungs, top 200
     best-conditioned survivors, Dcr = |cr' - cr| / (1 + |cr|))
     as a function of the node-set size k in {4, 6, 8, 10, 12,
     16} (the k deepest common nodes; steps with < k common
     nodes are typed skips for that k).  Pooled ladder median
     per k, plus the per-ladder-third medians (steps split into
     three contiguous thirds).  TYPED: CORE-SHARP iff some
     consecutive pooled-median jump med(k_{i+1}) / med(k_i) >=
     5.0 with med(k_i) <= 0.02 (a clear knee; k* = k_i is the
     last coherent size); CORE-GRADED otherwise.

 D3  LAMBDA SIGNAL (perturbation anatomy): rebuild the FULL
     ladder under frozen surgical modifications of the comb and
     recompute the deep-core (k = 8) defect pooled median:
       (i)   EDGE-SMOOTH: masses replaced by the PNT-mean
             2 e^{u/2} du ONLY in the last log-unit of the
             window support, u > 2 alpha - 1 (du = midpoint cell
             widths of the full lattice, lattice_parametrix B1
             verbatim); interior masses kept.
       (ii)  INTERIOR-SMOOTH: the complement -- masses smoothed
             for u <= 2 alpha - 1, the last log-unit kept true.
       (iii) ATOMS-ONLY: prime-power tails removed -- keep only
             the k = 1 atoms (n prime), drop all p^k with k >= 2
             (the Euler-echo test: euler_scattering_source typed
             the powers as the ECHOES of the per-prime
             scatterers; if the coherence needs them it is a
             genuinely multiplicative signal).
       (iv)  WRONG-LAMBDA: masses 2 log(n) / sqrt(n) at every
             prime power -- the freeze Lambda(p^k) -> log(p^k) =
             log n (positions and rough size preserved, the
             arithmetic value log p destroyed; differs from
             truth only on the k >= 2 atoms, by the factor k).
     Prime identification WITHOUT any oracle: n is a k = 1 atom
     iff Lambda(n) = log n (|LAM_TAB[n] - log n| < 1e-9 on the
     pipeline's own von-Mangoldt table).  Per world the frozen
     reading: KEEPS iff pooled med <= 2e-3 (certificate level,
     the truth reproduction bar); KILLS iff pooled med > 0.02
     (the firewall's reading bar); DEGRADED otherwise.  The
     typed table is the signal's address.

 D4  MINIMAL OBJECT (report, assembled from D1-D3 flags): the
     smallest frozen object that carries the coherence -- the
     named contract candidate for the next round.

 C   CONTROLS/WARDS: (C1, decisive ward) the SMOOTH-MASS world
     (all masses 2 e^{u/2} du): its deep-core (k = 8) median
     must reproduce the round-48 kill, > 0.02 (observed 2.7e-2);
     the TRUTH deep-core median must reproduce the certificate,
     <= 2e-3 (observed 4.3e-4).  Either side failing ->
     WARD-BROKEN (the probe does not reproduce the object it
     claims to dissect).  (C2, must fire) scramble (seed 1, kz
     9): frame death (window unavailable or lam out-block > 1 or
     lam(C_J) > 1), channel reported; silent -> WARD-BROKEN.

 W   PIPELINE WARDS: W1 >= 30 truth rungs built; W2 [Y, D_P]
     rank 2 on every truth rung (s3/s1 <= 1e-10); W3 >= 30
     k = 1 steps with >= 8 common port aliases.

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; K2 a C ward
breaks (truth not certificate / smooth not dead / scramble
silent) -> WARD-BROKEN.

VERDICT (frozen enum): DEEPCORE-MEASURED with typed sublabels
ALIAS-FIXED / ALIAS-DRIFTING (D1), PORTCORE-MATCH / PORTCORE-OFF
(D1), CORE-SHARP(k*) / CORE-GRADED (D2), and the D3 kill list
(per world KEEPS / DEGRADED / KILLS); else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS: DC_CERT = 2e-3; DC_DEAD = 0.02; KNEE_FACTOR = 5.0;
ALIAS_FIXED_FRAC = 0.90; PORTCORE_TOL = 0.10; EDGE_LOGU = 1.0;
K_PROFILE = (4, 6, 8, 10, 12, 16); PRIME_ID_TOL = 1e-9; battery
conditioning / caps verbatim from the firewall probe.

SPEC v2 AMENDMENTS (documented before the run; fail-first
preserved): (i) core.build_window(kz) results are MEMOIZED per
(kz, seed) as a slim dict (h, M, D, alpha, uu, lam) plus the
deterministic archimedean lag vector -- pure memoization of a
deterministic function, bit-identical physics, needed because six
ladders (truth + 4 surgeries + smooth) share the same windows;
(ii) the frame channel (window compression lamO / lamC and
lam(E)) is computed ONLY for the declared scramble control -- it
never feeds the carrier, and the firewall probe used it only for
its controls; (iii) the D2 battery at size k admits only steps
with >= k common nodes (else 'the k deepest' is undefined);
per-k step counts printed; (iv) prime/prime-power identification
uses the pipeline's own LAM_TAB (Lambda(n) = log n test) -- no
sieve and no oracle identifiers; (v) the knee rule and all
reading bars are concretized numerically above, frozen before
the first run.

NO RH claim -- deep-core cross-ratio coherence of a compressed-
truncation carrier is a numerical measurement, not a theorem
about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; carrier extraction
verbatim from port_schur_cocycle_probe.py / iiks_gauge_firewall_
probe.py; deep-core sub-battery verbatim from mobius_crossratio_
firewall_probe.py (PRIME.PORT.MOEBIUS.CRFIREWALL.01); smooth-mass
B1 world from lattice_parametrix_probe.py; per-prime comb reading
from euler_scattering_source_probe.py; port-alias Bessel profile
from christoffel_hypotheses_probe.py (H5).  IIKS =
Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deepcore_anatomy_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from collections import Counter
from itertools import combinations

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
MIN_RUNGS = 30
MIN_STEPS = 30
MIN_COMMON_J = 8
RANK_BAR = 1e-10
CTRL_KZ = 9

COND_SEP_FRAC = 1e-3              # within-tuple conditioning
CR_ABS_LO, CR_ABS_HI = 1e-3, 1e3  # |cr| window (both rungs)
QUAD_ACCEPT_CAP = 200             # best-conditioned survivors
DEEP_CORE_N = 8                   # the round-48 deep core
K_PROFILE = (4, 6, 8, 10, 12, 16)
DC_CERT = 2e-3                    # certificate reproduction bar
DC_DEAD = 0.02                    # the firewall's reading bar
KNEE_FACTOR = 5.0                 # D2 knee jump factor
ALIAS_FIXED_FRAC = 0.90           # D1 modal-set fraction
PORTCORE_TOL = 0.10               # D1 a_m vs pi^2 m^2 (deepest)
EDGE_LOGU = 1.0                   # D3 edge = last log-unit
PRIME_ID_TOL = 1e-9               # Lambda(n) = log n test
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


# --------- pipeline, verbatim from the firewall probe (memoized)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    """Midpoint cells (lattice_parametrix verbatim; smooth mass)."""
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    """SPEC v2 amendment (i): pure memoization of the
    deterministic core.build_window(kz) -- slim dict + the
    archimedean lag vector; physics bit-identical."""
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


def build_rung(kz, scramble_seed=None, world_fn=None):
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha = rr["M"], rr["D"], rr["alpha"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=rr["h"])


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


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (SPEC v2 extraction,
    verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN EXTRACTION GAUGE (lax2 verbatim): SO(2) rotation
    pinning the deepest port node -- a chordal isometry, so the
    cross-ratio battery is exactly gauge-free."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, need_frame=False, **kw):
    """One heavy build per rung (firewall verbatim; SPEC v2
    amendment (ii): the frame channel only for the declared
    control)."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, L=L, D=D, alpha=b["alpha"])
    if need_frame:
        out["lamE"] = float(np.linalg.eigvalsh(E)[-1])
        idx = {int(j): k for k, j in enumerate(uf_n)}
        jav = [j for j in JWIN if j in idx]
        if len(jav) >= MIN_COMMON_J:
            iw = [idx[j] for j in jav]
            io = [k for k in range(E.shape[0])
                  if k not in set(iw)]
            Eo = E[np.ix_(io, io)]
            IO = np.eye(len(io)) - Eo
            CJ = (E[np.ix_(iw, iw)]
                  + E[np.ix_(iw, io)] @ np.linalg.solve(
                      IO, E[np.ix_(io, iw)]))
            CJ = 0.5 * (CJ + CJ.T)
            out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
            out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) >= 4 and len(ib) >= 1:
        P = E[np.ix_(ip, ip)]
        X = E[np.ix_(ip, ib)]
        R = E[np.ix_(ib, ib)]
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        Y = np.diag(ys[ip])
        C = Y @ DP - DP @ Y
        f, g, sv = antisym_generators(C)
        f, g = gauge_fix(f, g, uf_n[ip])
        out["f"], out["g"] = f, g
        out["jp"], out["yp"] = uf_n[ip], ys[ip]
        out["taup"] = tau_m[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- RP^1 machinery (verbatim)
def unit_pairs(g, f):
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chord_mat(P):
    return np.abs(P[:, None, 0] * P[None, :, 1]
                  - P[:, None, 1] * P[None, :, 0])


def sdet(p, q):
    return float(p[0] * q[1] - p[1] * q[0])


def cross_ratio(P, i, j, k, l):
    den = sdet(P[i], P[l]) * sdet(P[j], P[k])
    if abs(den) < 1e-300:
        return None
    return (sdet(P[i], P[k]) * sdet(P[j], P[l])) / den


def pair_pairs(ra, rb):
    """Raw unit pairs on the sorted common port alias indices."""
    com, ia, ib = np.intersect1d(ra.get("jp", []),
                                 rb.get("jp", []),
                                 return_indices=True)
    if len(com) < MIN_COMMON_J:
        return None
    Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
    Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
    return Pa, Pb, com


def core_battery(Pa, Pb, core_n):
    """The deep-core quadruple battery (firewall verbatim,
    core_n deepest common nodes): full enumeration, conditioning
    on both rungs, top QUAD_ACCEPT_CAP survivors."""
    nodes = np.arange(core_n)
    Da, Db = chord_mat(Pa), chord_mat(Pb)
    cands = []
    for q in combinations(nodes.tolist(), 4):
        qi = list(q)
        score = 1.0
        ok = True
        for Dm in (Da, Db):
            sub = Dm[np.ix_(qi, qi)]
            vals = sub[np.triu_indices(4, 1)]
            spread = float(np.max(vals))
            if spread < 1e-300 or float(np.min(vals)) \
                    < COND_SEP_FRAC * spread:
                ok = False
                break
            score = min(score, float(np.min(vals)))
        if not ok:
            continue
        cra = cross_ratio(Pa, *q)
        crb = cross_ratio(Pb, *q)
        if (cra is None or crb is None
                or not (CR_ABS_LO <= abs(cra) <= CR_ABS_HI)
                or not (CR_ABS_LO <= abs(crb) <= CR_ABS_HI)):
            continue
        cands.append((score, q,
                      abs(crb - cra) / (1.0 + abs(cra))))
    cands.sort(key=lambda sqd: (-sqd[0], sqd[1]))
    return [d for _s, _q, d in cands[:QUAD_ACCEPT_CAP]]


def deep_battery(rungs, core_n):
    """Pooled deep-core cr-defects over all k = 1 steps with
    >= core_n common nodes (SPEC v2 amendment (iii))."""
    pooled, per_step, n_skip = [], [], 0
    for i in range(len(rungs) - 1):
        pp = pair_pairs(rungs[i], rungs[i + 1])
        if pp is None or len(pp[2]) < core_n:
            n_skip += 1
            continue
        dfs = core_battery(pp[0], pp[1], core_n)
        if not dfs:
            n_skip += 1
            continue
        pooled.extend(dfs)
        per_step.append((rungs[i]["h"], rungs[i + 1]["h"], dfs))
    return pooled, per_step, n_skip


def q_stats(v):
    a = np.asarray(v, float)
    return (float(np.median(a)), float(np.percentile(a, 90)),
            float(np.max(a)))


def build_ladder(world_fn=None):
    rungs = []
    rk_max = 0.0
    for kz in core.frame_a_zones():
        r = rung_all(kz, world_fn=world_fn)
        if not isinstance(r, dict) or "f" not in r:
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    return rungs, rk_max


# ------------------------------------------- D3 frozen mass worlds
def atoms_of(rr):
    """The prime-power values n of the window's atoms (READ-ONLY
    v563 table; positions are u = log n)."""
    return core._NN[:rr["n_atom"]].astype(float)


def k1_mask(nn):
    """k = 1 atoms: n prime iff Lambda(n) = log n on the
    pipeline's own von-Mangoldt table (no oracle)."""
    lam_n = core.LAM_TAB[nn.astype(int)]
    return np.abs(lam_n - np.log(nn)) < PRIME_ID_TOL


def smooth_masses(uu):
    """PNT-mean masses 2 e^{u/2} du (lattice_parametrix B1)."""
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_edge_smooth(uu, mm, rr):
    mm2 = mm.copy()
    sel = uu > 2.0 * rr["alpha"] - EDGE_LOGU
    mm2[sel] = smooth_masses(uu)[sel]
    return uu, mm2


def world_interior_smooth(uu, mm, rr):
    mm2 = mm.copy()
    sel = uu <= 2.0 * rr["alpha"] - EDGE_LOGU
    mm2[sel] = smooth_masses(uu)[sel]
    return uu, mm2


def world_atoms_only(uu, mm, rr):
    keep = k1_mask(atoms_of(rr))
    return uu[keep], mm[keep]


def world_wrong_lambda(uu, mm, rr):
    nn = atoms_of(rr)
    return uu, 2.0 * np.log(nn) / np.sqrt(nn)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


D3_WORLDS = (("EDGE-SMOOTH", world_edge_smooth),
             ("INTERIOR-SMOOTH", world_interior_smooth),
             ("ATOMS-ONLY", world_atoms_only),
             ("WRONG-LAMBDA", world_wrong_lambda))


def world_label(med):
    if med <= DC_CERT:
        return "KEEPS"
    if med > DC_DEAD:
        return "KILLS"
    return "DEGRADED"


def main():
    section("PRIME.PORT.DEEPCORE.01 -- anatomy of the surviving "
            "deep-core cross-ratio coherence (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; fit-free, gauge-free battery; no "
          "marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth ladder (all frame-A zones, "
            "h <= %d; machinery verbatim)" % H_DEEP_MAX)
    rungs, rk_max = build_ladder()
    print("    %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 %.1e  "
          "(%.1f s)"
          % (len(rungs), rungs[0]["h"] if rungs else -1,
             rungs[-1]["h"] if rungs else -1, rk_max,
             time.time() - T0))
    check("W1 >= %d rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= %.0e)"
          % (rk_max, RANK_BAR), rk_max <= RANK_BAR, kill="K1")

    # ------------------------------------------------------------ D1
    section("D1 -- NODE IDENTIFICATION: the deep-core census "
            "along the ladder")
    step_cores = []
    print("    per-step deep core (8 smallest common aliases):")
    for i in range(len(rungs) - 1):
        pp = pair_pairs(rungs[i], rungs[i + 1])
        if pp is None:
            continue
        com = pp[2]
        core8 = tuple(int(j) for j in com[:DEEP_CORE_N])
        step_cores.append(core8)
        print("    h %3d->%3d  n_com %2d  deep-8 %s"
              % (rungs[i]["h"], rungs[i + 1]["h"], len(com),
                 list(core8)))
    check("W3 >= %d k=1 steps with >= %d common aliases"
          % (MIN_STEPS, MIN_COMMON_J),
          len(step_cores) >= MIN_STEPS,
          "%d steps" % len(step_cores), kill="K1")
    freq = Counter(j for c8 in step_cores for j in c8)
    print("\n    alias frequency in the deep-8 (over %d steps):"
          % len(step_cores))
    for j, n in sorted(freq.items()):
        print("      alias j = %3d : %3d / %d steps"
              % (j, n, len(step_cores)))
    modal = tuple(sorted(j for j, _n in freq.most_common(
        DEEP_CORE_N)))
    frac_modal = (sum(1 for c8 in step_cores if c8 == modal)
                  / max(len(step_cores), 1))
    evens = tuple(range(2, 2 * DEEP_CORE_N + 1, 2))
    d1_alias = ("ALIAS-FIXED" if frac_modal >= ALIAS_FIXED_FRAC
                else "ALIAS-DRIFTING")
    print("    modal deep-8 set: %s  (exact in %.0f%% of steps; "
          "bar %.0f%%)"
          % (list(modal), 100 * frac_modal,
             100 * ALIAS_FIXED_FRAC))
    print("    even set {2..16}? %s"
          % ("YES -- the j = 2..16 evens" if modal == evens
             else "no"))
    check("D1.1 typed: %s" % d1_alias, True)

    print("\n    anatomy at three representative rungs "
          "(a_m = 2 h^2 (1 - y_m) vs pi^2 m^2):")
    reps = [rungs[0], rungs[len(rungs) // 2], rungs[-1]]
    dev_deepest = float("inf")
    for r in reps:
        h = r["h"]
        n8 = min(DEEP_CORE_N, len(r["jp"]))
        print("    kz %-3d h %4d (L %5d, D %.4f):"
              % (r["kz"], h, r["L"], r["D"]))
        devs = []
        for m in range(1, n8 + 1):
            j = int(r["jp"][m - 1])
            y = float(r["yp"][m - 1])
            tau = float(r["taup"][m - 1])
            a = 2.0 * h * h * (1.0 - y)
            ref = (math.pi ** 2) * m * m
            devs.append(abs(a / ref - 1.0))
            print("      m %d  alias j %3d  y %.6f  tau %8.4f  "
                  "a_m %9.3f  a_m/(pi^2 m^2) %.4f"
                  % (m, j, y, tau, a, a / ref))
        if r is rungs[-1]:
            dev_deepest = max(devs) if devs else float("inf")
    d1_core = ("PORTCORE-MATCH" if dev_deepest <= PORTCORE_TOL
               else "PORTCORE-OFF")
    print("    deepest rung: max_m |a_m/(pi^2 m^2) - 1| = %.3f "
          "(bar %.2f)" % (dev_deepest, PORTCORE_TOL))
    check("D1.2 typed: %s (the a_m = pi^2 m^2 port core)"
          % d1_core, True)

    # ------------------------------------------------------------ D2
    section("D2 -- COHERENCE PROFILE vs node-set size k "
            "(deepest k common nodes)")
    meds_k = {}
    truth_dc_med = float("inf")
    for kn in K_PROFILE:
        pooled, per_step, n_skip = deep_battery(rungs, kn)
        if not pooled:
            print("    k = %2d : no measurable steps" % kn)
            continue
        m, q90, mx = q_stats(pooled)
        meds_k[kn] = m
        thirds = np.array_split(np.arange(len(per_step)), 3)
        tmeds = []
        for t in thirds:
            vals = [d for ii in t for d in per_step[ii][2]]
            tmeds.append(float(np.median(vals)) if vals
                         else float("nan"))
        print("    k = %2d : %3d steps (%2d skips)  %5d quads  "
              "med %.2e  q90 %.2e  max %.2e | thirds %s"
              % (kn, len(per_step), n_skip, len(pooled), m, q90,
                 mx, "  ".join("%.2e" % v for v in tmeds)))
        if kn == DEEP_CORE_N:
            truth_dc_med = m
    knee_k, knee_ratio = None, 0.0
    ks = [k for k in K_PROFILE if k in meds_k]
    for a, b in zip(ks, ks[1:]):
        r = meds_k[b] / max(meds_k[a], 1e-300)
        if (r >= KNEE_FACTOR and meds_k[a] <= DC_DEAD
                and r > knee_ratio):
            knee_k, knee_ratio = a, r
    d2_type = ("CORE-SHARP(k*=%d)" % knee_k if knee_k is not None
               else "CORE-GRADED")
    print("    knee scan (jump >= x%.0f with coherent pre-knee "
          "<= %.2f): %s%s"
          % (KNEE_FACTOR, DC_DEAD, d2_type,
             ("  (jump x%.1f at k %d -> %d)"
              % (knee_ratio, knee_k,
                 ks[ks.index(knee_k) + 1]))
             if knee_k is not None else ""))
    check("D2.1 typed: %s" % d2_type, True)

    # ------------------------------------------------------------ D3
    section("D3 -- LAMBDA SIGNAL: surgical mass worlds, deep-core "
            "(k = %d) defect" % DEEP_CORE_N)
    d3 = {}
    rows = [("TRUTH", truth_dc_med, len(rungs), "reference")]
    for name, fn in D3_WORLDS:
        t1 = time.time()
        w_rungs, w_rk = build_ladder(world_fn=fn)
        pooled, per_step, n_skip = deep_battery(w_rungs,
                                                DEEP_CORE_N)
        med = q_stats(pooled)[0] if pooled else float("inf")
        d3[name] = med
        rows.append((name, med, len(w_rungs),
                     "%d steps, %d skips, worst s3/s1 %.1e, "
                     "%.0f s" % (len(per_step), n_skip, w_rk,
                                 time.time() - t1)))
        print("    %-16s med %.2e  (%s)"
              % (name, med, rows[-1][3]), flush=True)
    print("\n    THE SURGICAL TABLE (bars: KEEPS <= %.0e / "
          "KILLS > %.2f):" % (DC_CERT, DC_DEAD))
    print("    %-16s %-10s %s" % ("world", "dc-median", "reading"))
    d3_labels = {}
    for name, med, _nr, _det in rows:
        lab = ("reference" if name == "TRUTH"
               else world_label(med))
        if name != "TRUTH":
            d3_labels[name] = lab
        print("    %-16s %.2e   %s" % (name, med, lab))
    killers = [n for n, l in d3_labels.items() if l == "KILLS"]
    keepers = [n for n, l in d3_labels.items() if l == "KEEPS"]
    check("D3.1 surgical table typed (killers: %s)"
          % (", ".join(killers) if killers else "none"), True)

    # ------------------------------------------------------------ C
    section("C -- controls / wards")
    print("  C1 the smooth-mass world (all masses 2 e^{u/2} du) "
          "-- the round-48 ward:")
    sm_rungs, sm_rk = build_ladder(world_fn=world_smooth)
    sm_pooled, sm_steps, sm_skip = deep_battery(sm_rungs,
                                                DEEP_CORE_N)
    sm_med = q_stats(sm_pooled)[0] if sm_pooled else float("inf")
    print("    smooth ladder: %d rungs (worst s3/s1 %.1e); "
          "deep-core med %.2e over %d steps (%d skips)"
          % (len(sm_rungs), sm_rk, sm_med, len(sm_steps),
             sm_skip))
    print("    round-48 reproduction: truth %.2e (was 4.3e-4) vs "
          "smooth %.2e (was 2.7e-2)" % (truth_dc_med, sm_med))
    check("C1.1 WARD truth deep-core certificate (med %.2e <= "
          "%.0e)" % (truth_dc_med, DC_CERT),
          truth_dc_med <= DC_CERT, kill="K2")
    check("C1.2 WARD smooth deep-core dead (med %.2e > %.2f)"
          % (sm_med, DC_DEAD), sm_med > DC_DEAD, kill="K2")

    print("\n  C2 scramble (seed 1, kz %d) -- frame death must "
          "fire:" % CTRL_KZ)
    rc = rung_all(CTRL_KZ, scramble_seed=1, need_frame=True)
    if not isinstance(rc, dict):
        fired = True
        print("    scramble: rung not built (%r) -> FRAME DIES"
              % (rc,))
    elif "lamC" not in rc:
        fired = True
        print("    scramble: window unavailable -> FRAME DIES")
    else:
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        print("    scramble: lam(out) %.3e | lam(C_J) %.3e | "
              "lam(E) %.3e -> %s"
              % (rc["lamO"], rc["lamC"], rc["lamE"],
                 "fires via %s" % ("EXTERIOR" if rc["lamO"] > 1.0
                                   else "WINDOW")
                 if fired else "SILENT"))
    check("C2.1 WARD scramble frame death fires", fired,
          kill="K2")

    # ------------------------------------------------------------ D4
    section("D4 -- THE MINIMAL OBJECT (report)")
    ek = d3_labels.get("EDGE-SMOOTH") == "KILLS"
    ik = d3_labels.get("INTERIOR-SMOOTH") == "KILLS"
    if ek and ik:
        region = ("the true Lambda masses across the WHOLE comb "
                  "(both partial smoothings kill)")
    elif ek:
        region = ("the true Lambda masses in the LAST LOG-UNIT "
                  "u in (2 alpha - 1, 2 alpha] (edge smoothing "
                  "kills, interior smoothing does not)")
    elif ik:
        region = ("the true Lambda masses in the INTERIOR u <= "
                  "2 alpha - 1 (interior smoothing kills, edge "
                  "smoothing does not)")
    else:
        region = ("no single radial region (neither partial "
                  "smoothing alone kills)")
    if d3_labels.get("ATOMS-ONLY") == "KEEPS":
        mult = ("the k = 1 prime atoms SUFFICE (the p^k echoes "
                "are not load-bearing)")
    elif d3_labels.get("ATOMS-ONLY") == "KILLS":
        mult = ("the p^k (k >= 2) Euler echoes are REQUIRED -- a "
                "genuinely multiplicative signal")
    else:
        mult = ("the p^k echoes matter but do not fully kill "
                "(ATOMS-ONLY degraded)")
    if d3_labels.get("WRONG-LAMBDA") == "KEEPS":
        val = ("the Lambda VALUES are not load-bearing beyond "
               "position + rough size (wrong-Lambda keeps)")
    elif d3_labels.get("WRONG-LAMBDA") == "KILLS":
        val = ("the exact Lambda(p^k) = log p values are "
               "load-bearing (wrong-Lambda kills)")
    else:
        val = "the Lambda values matter partially (degraded)"
    node_txt = ("the FIXED alias set %s" % (list(modal),)
                if d1_alias == "ALIAS-FIXED"
                else "a drifting deep-8 alias set")
    core_txt = ("%s port core (a_m = pi^2 m^2, m = 1..8)"
                % ("the" if d1_core == "PORTCORE-MATCH"
                   else "NOT the"))
    print("    nodes   : %s = %s" % (node_txt, core_txt))
    print("    profile : %s" % d2_type)
    print("    region  : %s" % region)
    print("    atoms   : %s" % mult)
    print("    values  : %s" % val)
    print("\n    MINIMAL OBJECT (contract candidate for the next "
          "round):")
    print("      the cross-ratio coherence of the carrier r = "
          "g/f on %s,"
          % ("the deep-8 port aliases %s" % (list(modal),)
             if d1_alias == "ALIAS-FIXED" else
             "the 8 deepest common port aliases"))
    print("      carried by %s;" % region)
    print("      %s; %s." % (mult, val))
    check("D4.1 minimal object stated", True)

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        d3_str = ", ".join("%s=%s" % (n, d3_labels[n])
                           for n, _f in D3_WORLDS)
        VERDICT = ("DEEPCORE-MEASURED / %s / %s / %s / [%s]"
                   % (d1_alias, d1_core, d2_type, d3_str))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (truth dc med %.2e; smooth ward %.2e; modal "
              "deep-8 %s)"
              % (truth_dc_med, sm_med, list(modal)))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
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
    ('factor_avoidance_euler_probe', _SRC_0, 18, (), 'FACTORAVOID-MEASURED', 0),
    ('deepcore_anatomy_probe', _SRC_1, 12, (), 'DEEPCORE-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v895 -- PRIME.PORT.FACTORAVOID.01 + PRIME.PORT.DEEPCORE.01: the collectivity of the arithmetic -- factor avoidance is structural and one-sided, and the deep-core remnant is the ENTIRE multiplicative von Mangoldt comb')
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
    print("v895: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the arithmetic is collective: no norm bound, no per-prime decomposition, no smaller object -- one-sided avoidance of one spectral edge by the whole comb')
    print("[%s] v895 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
