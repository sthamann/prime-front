#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v892 -- PRIME.PORT.RELCONG.01 + PRIME.PORT.PIVOTFACTOR.01 + PRIME.PORT.EULER.ROUCHE.01 + PRIME.PORT.DEEPCORE.SCHUR.01: THE CLOSURE ARCHITECTURE OF THE WALL -- the exact hermitian congruence with its non-decaying inheritance margin, the flag/pivot chain, the honest two-sided Rouche kill, and the fixed 8x8 Schur-core reduction, ONE module from four probes (16/16 + 15/15 + 14/14 + 16/16 checks, zero fails, verdicts RELCONG-MEASURED (MARGIN-UNEXPLAINED / RHO-MISLEADING / SMOOTH-DISCRIMINATES) + PIVOTFACTOR-MEASURED (truth FLAG-POSITIVE / smooth FLAG-VIOLATED / PIVOT-GRAIN-NONDECOMPOSITIONAL) + ROUCHE-MEASURED (ROUCHE-FAILS on both contours / ROUCHE-NONDISCRIMINATING) + DEEPCORESCHUR-MEASURED (SCHUR-TAU-TIED / CORE-INHERITS / CORE-SEES-SMOOTH / CORE-GRAIN-DEAD); discovery probes relative_congruence_probe.py (SPEC v2), pivot_factor_probe.py (SPEC v2), euler_rouche_probe.py (SPEC v2), deepcore_schur_reduction_probe.py (SPEC v2), round 51, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~25 s).  (1) THE EXACT HERMITIAN CONGRUENCE (relcong, reviewer priority 1): the inheritance step is made EXACT and COMPLETE -- A_{h+1} = A_h^{1/2} (I + H_h) A_h^{1/2} with H_h = A_h^{-1/2} Delta_h A_h^{-1/2} hermitian (congruence ward at machine precision on every step), so by Sylvester's law of inertia PD inheritance is EXACTLY the margin sign eta_h := 1 + lambda_min(H_h) > 0; the measured eta ladder does NOT decay -- min eta = 0.0050, power-law slope +0.108 in h -- while the wall scalar tau_h = lambda_min(A_h) collapses at slope -2.74; the earlier spectral-radius reading rho(W^{-1} Delta C) is exposed as the statistic of a NON-NORMAL operator (kappa(V) >> 1, ||M||_2 > rho, the symmetric part can pass -1 with NO crossing -- rho was misleading and norm reasoning on W^{-1} Delta C was the wrong frame; SPEC v2 report-only clarifications), and the smooth-mass control does not even keep the congruence's PD premise: CONE-EXITED on 28/28 full-window steps; the round-51 typing MARGIN-UNEXPLAINED (every single-source regression R^2 <= 0.103) is the honest state at this round -- the source is measured in v893.  (2) THE FLAG/PIVOT CHAIN (pivotfactor, reviewer priority 2, potentially the shortest real induction of the program): on the 12x12 window A_h = I - C_J(h) the pivot factorization d_{k,h+1} = d_{k,h} (1 + mu_{k,h}) is an exact identity (warded) and the CONTENT is the sign -- ALL 12 unpivoted-LDL pivot quotients are positive on ALL 31/31 truth steps (the flag quotient chain Q_k > 0 for every k: PD inheritance by pure algebra, no norm bound, no spectral gauge); the dangerous soft flag k = 12 carries the collapse scale with ladder min Q_12 = 2.059e-14, but the sign is DECIDABLE: min over truth rungs of lam_min/(12 eps lam_max) = 6.4e9 against the frozen 1e3 bar (SPEC v2 (ii)); the smooth world violates the chain already at the BULK flags k = 1 and k = 3, not at the soft flag.  (3) THE HONEST ROUCHE KILL (rouche, reviewer priority 3): the two-sided matrix-Rouche route is dead -- the contour norm M_h = sup_Gamma ||A_h(s)^{-1} Delta_h(s)||_2 reaches M >= 1 on 22 of 31 truth steps, INCLUDING the off-cap restriction Re s < 1 and the exact cap-point lower bound (SPEC v2 (i)-(iii)), so no one-norm contour bound can force the corridor zero count; the norm-bound theorem SHAPE is the wrong shape: inheritance on the truth ladder is ONE-SIDED (the eta/factor-avoidance direction), not two-sided contour-uniform -- exactly consistent with (1) and with v895's AVOIDANCE-STRUCTURAL.  (4) THE 8x8 SCHUR-CORE REDUCTION (deepcore schur, reviewer priority 4): the wall IS the fixed Schur core -- splitting the FULL wall operator A_h = I - E_h along the fixed deep-core aliases {2, 4, ..., 16} (the round-50 remnant, v895), the Schur complement S_h satisfies lambda_min(S_h) * w_core / tau_h = 1 within 8.4e-8 with core weight w_core >= 0.999937 on all 41 reachable rungs (the wall collapses to ONE fixed 8x8 matrix family); the exterior block R_h stays uniformly PD with its ABSOLUTE margin shrinking like h^-2.865 while the RELATIVE margin lambda_min(R_h)/tau_h is TRENDLESS in the band ~210..2200 -- the relative conditioning that v893 makes lawful; core inheritance has 0 crossings with eta_core min 0.0315 (median 0.398), and the per-prime grain is dead at fixed dimension.  NET: the closure architecture of the wall is RELATIVE and ONE-SIDED -- an exact congruence with a bounded margin at every level (full window, flag chain, fixed 8x8 core) while the two-sided norm route is measured dead; the named open piece is the tau-sign inheritance in bounded-margin form (v893 prints the skeleton).  NO RH claim; no marker moves; measured ladders on compressed truncations are measurements, not theorems about zeros.  Float64 on the deployed v563 machinery (READ-ONLY); no zeros, no prime oracles (AST firewalls inside the probes); RNG only in declared scramble controls.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes relative_congruence_probe.py (16/16,
RELCONG-MEASURED, SPEC v2: after an all-green run 1, two
REPORT-ONLY clarifications -- the kappa(V) column-scaling
bookkeeping of the R3 transport bound and the empty smooth
PD-branch print; no bar, no object, no number moved),
pivot_factor_probe.py (15/15, PIVOTFACTOR-MEASURED, SPEC v2:
display-only scientific-notation prints after run 1 printed the
load-bearing minimum 2.059e-14 as "0.0000", plus the frozen
sign-decidability precondition (ii); every run-1/2 raw number
stands), euler_rouche_probe.py (14/14, ROUCHE-MEASURED, SPEC v2:
adds the exact cap-point report, the off-cap sup and the Gamma_B
corridor census and strengthens one typing condition -- it rescues
nothing), deepcore_schur_reduction_probe.py (16/16,
DEEPCORESCHUR-MEASURED, SPEC v2: three transparency-only print
repairs after an already 16/16-green run 1, run-1 and run-2
verdicts identical), all round 51, 2026-08-09, re-run identically
at promotion.  ROUND-31 EMBEDDING CONVENTION: frozen sources
embedded BYTE-EXACT, executed verbatim in isolated namespaces;
printed spec SHAs reproduce; byte-equality ward vs
experiments/tfpt-discovery/ inside the pattern gates.  All probes
consume the READ-ONLY deployed core v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles; all fail-first spec
amendments preserved; killed routes stay killed and bounded
margins are typed as measurements -- the tau-sign inheritance in
bounded-margin form stays the named open statement.  NO RH claim.
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

# ------------- frozen probe source relative_congruence_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""relative_congruence_probe -- PRIME.PORT.RELCONG.01
(EXPLORATION ONLY, experiments/; round 51, reviewer priority 1:
make round 50's one-sided law EXACT and COMPLETE -- the clean
inheritance form A_{h+1} = A_h^{1/2} (I + H_h) A_h^{1/2} with
H_h hermitian, plus full non-normality diagnostics and the
margin ladder.  2026-08-09.)

THE QUESTION (frozen): factor_avoidance_euler_probe (round 50)
measured the one-sided law max_steps(-min mu) = 0.9950 < 1 on all
31 truth steps, mu = eigenvalues of W^{-1} Delta C with
W = A_h = I - C_J(h) symmetric PD on truth and Delta C symmetric.
The reviewer's point: W^{-1} Delta C is similar to the HERMITIAN
H_h = A_h^{-1/2} Delta_h A_h^{-1/2} -- make this exact and
complete.  The clean object is the CONGRUENCE, not the
non-normal product; rho(W^{-1} Delta C) was a statistic of a
non-normal operator and must be audited as such.

THE HERMITIAN INHERITANCE MINI-THEOREM (stated up front;
elementary, and the R5 deliverable): let A_h be symmetric
positive definite and Delta_h symmetric, with
A_{h+1} = A_h + Delta_h.  Put
    H_h := A_h^{-1/2} Delta_h A_h^{-1/2}    (hermitian -- here
                                             real symmetric).
Then EXACTLY
    A_{h+1} = A_h^{1/2} (I + H_h) A_h^{1/2},
a *congruence* of I + H_h.  By Sylvester's law of inertia
A_{h+1} is positive definite  <=>  I + H_h is positive definite
<=>  lambda_min(H_h) > -1  <=>  eta_h := 1 + lambda_min(H_h) > 0.
Moreover A_h^{-1} Delta_h = A_h^{-1/2} H_h A_h^{1/2}, so
W^{-1} Delta C is SIMILAR to H_h: its spectrum is exactly real
and equals eig(H_h) -- round 50's mu-ledger was the spectrum of
this hermitian object seen through a non-normal similarity.
THE FULL LADDER INDUCTION therefore reduces to
  (i)  one certified base rung A_{h0} PD (exists: v884 certified
       head positivity / v887 certified ladder), and
  (ii) THE MARGIN INEQUALITY (the named inequality):
           eta_h = 1 + lambda_min(H_h) > 0   for every step h.
The probe measures the finite shadow of (ii) on the deployed
ladder and asks whether eta_h is LAWFUL (predictable from step
sources) or merely measured.

THE LADDER (frozen, factor_avoidance verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive FULL-WINDOW pairs (both rungs carry all 12 indices
of J = {2, 4, ..., 24}; typed skips counted); truth + smooth-
mass world (B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n,
midpoint cells, lattice_parametrix verbatim); Epstein/scramble
frame status reported (C1).

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 R1  THE EXACT CONGRUENCE (per truth full-window step):
     A_h = I - C_J(h) (12x12), Delta_h = C_J(h) - C_J(h+1) so
     A_{h+1} = A_h + Delta_h; symmetric eigendecomposition
     A_h = V diag(w) V^T (eigh), A_h^{+-1/2} = V diag(w^{+-1/2})
     V^T; H_h = A_h^{-1/2} Delta_h A_h^{-1/2}.  WARDS (kill ->
     WARD-BROKEN):
       R1.a SYMMETRIZATION: ||H - H^T||_F / ||H||_F <= 1e-12
            on every step (exact hermitian object);
       R1.b RECONSTRUCTION: ||A_h^{1/2} (I + H_h) A_h^{1/2}
            - A_{h+1}||_F / ||A_{h+1}||_F <= 1e-10 (the exact
            identity);
       R1.c SIMILARITY: sorted eig(H_h) == sorted real parts of
            eig(W^{-1} Delta C) (general nonsymmetric solver)
            within 1e-9 relative, and max |Im mu| <= 1e-9
            (1 + |mu|) -- this pins round 50's mu-ledger to the
            hermitian spectrum;
       R1.d REPRODUCTION (round-50 ledger): 31 truth full-window
            pairs, 0 crossings, min eta = 0.0050 and
            max(-lambda_min(H)) = 0.9950 (print precision, tol
            5.001e-5).

 R2  THE MARGIN LADDER (the deliverable): per step
     eta_h = 1 + lambda_min(H_h); the FULL ladder printed with
     h, flow, lambda_min, eta, tau_h = lambda_min(A_h), the
     spectral gap g_h = lambda_2(A_h) - lambda_min(A_h),
     ||Delta_h||_F, the moving-block atom mass, and the
     soft-mode overlap |<v_min, s_h>| (v_min = A_h^{-1/2}-
     transported normalized minimizing eigenvector of H_h,
     s_h = eigenvector of A_h at its smallest eigenvalue).
     TREND (leave-last-third-out, frozen): sort by h, fit OLS
     on the first ceil(2n/3) steps, score RMSE on the held-out
     last third, for the three frozen candidates
       POWER  log eta ~ a + b log h,
       LOG    log eta ~ a + b log log h,
       EXP    log eta ~ a + b h;
     report in-sample R^2 + held-out RMSE, best = smallest
     held-out RMSE; and the shrink comparison: the POWER slope
     of eta vs the POWER slopes of tau_h, g_h, ||Delta_h||_F
     (does eta shrink like tau? like the gap?).
     THE SOURCE QUESTION (frozen table): corr(log eta, z) and
     R^2 = corr^2 for z in { log(moving-block atom mass),
     log ||Delta_h||_F, log tau_h, log g_h, ovl (raw) }.
     TYPED: MARGIN-LAWFUL iff some single source reaches
     R^2 >= 0.8; MARGIN-UNEXPLAINED otherwise (honest).

 R3  NON-NORMALITY DIAGNOSTICS (the reviewer's mandated
     additions, per truth step, for M = W^{-1} Delta C computed
     by the general solver): ||M||_2 (operator norm, largest
     singular value), lambda_min of the symmetric part
     (M + M^T)/2, the eigenvector condition number kappa(V) of
     M (2-norm cond of the eig eigenvector matrix), printed
     alongside rho(M) = max |mu| and the bound check
     kappa(V) <= sqrt(cond(A_h)) (similarity transport).  THE
     CENSUS: per-step non-normality ratio ||M||_2 / rho; typed
     RHO-MISLEADING iff the ratio >= NN_RATIO_BAR = 3 on >= 1/2
     of the steps (rho then materially understates the operator
     as a NORM statistic), RHO-FAITHFUL otherwise.  STATED
     EITHER WAY: the spectrum itself was always exact (R1.c
     similarity) -- what non-normality breaks is norm reasoning
     (||M||_2, transient growth, symmetric-part bounds), and
     the honest object carrying the inheritance is the
     hermitian H_h.

 R4  THE SMOOTH WORLD (same ladder, B1 smooth masses): per
     full-window step, if A_h is PD the same H_h ladder
     (lambda_min, eta); if A_h is NOT PD the real congruence
     form is unavailable -- typed CONE-EXITED and counted (the
     general-branch crossing flag still computed, predecessor
     verbatim).  WHERE DOES lambda_min(H) CROSS -1: first
     eta < 0 step printed.  WARD (kill -> WARD-BROKEN,
     round-50 ledger): 28 smooth full-window pairs, 22 crossing
     steps (Q < 0 or a real factor < 0), first crossing at
     h 210 -> 218, Q < 0 on 16 steps.  THE CONTRAST: truth
     min eta vs smooth min eta (PD steps) and the count of
     smooth eta < 0 -- the discriminating gap, printed.  TYPED:
     SMOOTH-DISCRIMINATES iff truth min eta > 0 AND (some
     smooth PD step has eta < 0 OR some smooth step is
     CONE-EXITED); SMOOTH-NONDISCRIMINATING otherwise.

 R5  THE MINI-THEOREM, NUMERICALLY (report + ward): on every
     truth step verify that eta_h > 0 AND the reconstructed
     A_{h+1} = A_h^{1/2}(I + H_h)A_h^{1/2} has
     lambda_min > 0 (Sylvester inheritance, one step, exact);
     print the induction statement with the measured eta ladder
     as its finite shadow: certified base (v884/v887) +
     eta_h > 0 for all h  =>  A_h PD for all h.  No claim
     beyond the deployed ladder.

 C   CONTROLS: (C1, kz 9, must fire, kill -> CONTROL-DEAD)
     Epstein (lambda_eps recursion comb) + scramble (seed 1):
     the compressed frame must die (exterior supercritical OR
     lam(C_J) > 1 OR window unavailable); channel reported.
     (C2) the SMOOTH-MASS world is the PRIMARY embedded
     control; its detection (crossings present) is
     ward-anchored in R4 -- if the smooth ladder shows no
     crossing the probe is CONTROL-DEAD.

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 >= 30 truth
     rungs; W1b the atom prefix law exact; W2 A_h symmetric PD
     on every truth full-window rung; W3 >= 20 truth
     full-window pairs.

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; KW an R1/R4
reproduction / symmetrization / reconstruction / similarity
ward breaks -> WARD-BROKEN; K3 controls silent -> CONTROL-DEAD.

VERDICT (frozen enum): RELCONG-MEASURED with typed sublabels
MARGIN-LAWFUL / MARGIN-UNEXPLAINED (R2), RHO-MISLEADING /
RHO-FAITHFUL (R3), SMOOTH-DISCRIMINATES /
SMOOTH-NONDISCRIMINATING (R4); else PIPELINE-BROKEN /
WARD-BROKEN / CONTROL-DEAD.

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- run 1
passed ALL 16 checks; no bar was moved and every run-1 number
stands; two REPORT-ONLY prints are documented/clarified):

 (i)  R3 kappa bound bookkeeping: the transport inequality
      kappa(V) <= sqrt(cond A_h) holds for the OPTIMALLY
      COLUMN-SCALED diagonalizer of W^{-1}Delta (the
      A_h^{1/2}-transported orthonormal eigenbasis);
      np.linalg.eig returns UNIT columns, whose condition
      number can exceed the optimal one by the column-scaling
      ambiguity (run 1 measured excesses of order 10%, e.g.
      kappa 84.3 vs bound 80.0 at h 149->151).  The print is
      annotated accordingly; the raw kappa numbers stand and
      the diagnostic remains report-only (never a ward).

 (ii) R4 zero-PD bookkeeping: run 1 measured that A_h is
      indefinite on EVERY smooth full-window pair (28/28
      CONE-EXITED; the smooth pair ladder only begins at
      h 210, after 13 typed skips) -- the measured answer to
      "where does lambda_min(H) cross -1" is that the smooth
      world exits the PD cone BEFORE its full-window pair
      ladder even starts, so the PD-branch eta ladder is
      EMPTY there.  The contrast print handles the empty PD
      branch explicitly ("none" instead of nan); the
      SMOOTH-DISCRIMINATES typing bar (frozen in R4) already
      covered this case via the CONE-EXITED count and is
      unchanged.

NO RH claim -- a per-step congruence measurement on compressed
window truncations is a statement about the deployed ladder,
not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts (U_ALL / MU_ALL
prefix law, build_window, atom_lags_at, arch_lags -- read
verbatim); window compression + smooth-mass world verbatim from
factor_avoidance_euler_probe.py (PRIME.PORT.FACTORAVOID.01,
round 50) via tau_mobius_factor_probe.py
(PRIME.PORT.TAU.MOEBIUS.01, the exact quotient identity) and
lattice_parametrix_probe.py (B1); certified base rungs:
v884_certified_head_positivity / v887_certified_ladder_complete
(cited as the induction base, not re-run here).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/relative_congruence_probe.py
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
MIN_PAIRS = 20
MIN_COMMON_J = 8
ASYM_WARD = 1e-12           # R1.a symmetrization (kill)
RECON_WARD = 1e-10          # R1.b reconstruction (kill)
SIM_WARD = 1e-9             # R1.c similarity (kill)
R2_BAR = 0.8                # R2 MARGIN-LAWFUL bar
HOLDOUT_FRAC = 3            # R2 leave-last-1/3-out
NN_RATIO_BAR = 3.0          # R3 non-normality ratio bar
NN_STEP_FRAC = 0.5          # R3 RHO-MISLEADING step fraction
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# R1.d / R4 reproduction wards (factor_avoidance_euler_probe +
# tau_mobius_factor_probe printed ledgers, round 50)
REF_N_TRUTH_PAIRS = 31
REF_TRUTH_CROSS = 0
REF_TRUTH_MINETA = 0.0050
REF_TRUTH_MAXNEG = 0.9950
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


# --------- pipeline, verbatim from factor_avoidance_euler_probe
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
    """One rung -> 12x12 window compression (factor_avoidance
    verbatim)."""
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


# ------------------------------------------- congruence machinery
def logdet_sgn(W):
    sgn, ld = np.linalg.slogdet(W)
    return float(sgn), float(ld)


def congruence_pairs(rungs, rrs):
    """Consecutive full-window pairs: the exact congruence (PD
    branch), the general nonsymmetric branch (R1.c / R3), and the
    round-50 crossing flag (both worlds, predecessor verbatim)."""
    rows = []
    n_skip = 0
    n = len(JWIN)
    for k, (ra, rb) in enumerate(zip(rungs[:-1], rungs[1:])):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        Aa = np.eye(n) - ra["CJ"]
        Ab = np.eye(n) - rb["CJ"]
        DC = ra["CJ"] - rb["CJ"]           # A_{h+1} = A_h + DC
        sga, lda = logdet_sgn(Aa)
        sgb, ldb = logdet_sgn(Ab)
        Q = sga * sgb * math.exp(ldb - lda)
        ka = int(rrs[ra["kz"]]["n_atom"])
        kb = int(rrs[rb["kz"]]["n_atom"])
        blk = np.asarray(core.MU_ALL, float)[min(ka, kb):
                                             max(ka, kb)]
        row = dict(k=k, ha=ra["h"], hb=rb["h"], kza=ra["kz"],
                   kzb=rb["kz"], ka=ka, kb=kb,
                   flow=("ENTER" if kb > ka else
                         "LEAVE" if kb < ka else "NONE"),
                   blkmass=float(np.sum(np.abs(blk))),
                   dnorm=float(np.linalg.norm(DC)), Q=Q)
        # ---- general nonsymmetric branch (always; R1.c / R3)
        Mg = np.linalg.solve(Aa, DC)
        mu, Vg = np.linalg.eig(Mg)
        rho = float(np.max(np.abs(mu))) if len(mu) else 0.0
        real_m = np.abs(mu.imag) <= 1e-9 * (1.0 + np.abs(mu))
        fac_r = 1.0 + mu.real[real_m]
        row.update(
            mu=mu, rho=rho,
            imax=float(np.max(np.abs(mu.imag)
                              / (1.0 + np.abs(mu)))),
            opn=float(np.linalg.norm(Mg, 2)),
            symp=float(np.linalg.eigvalsh(
                0.5 * (Mg + Mg.T))[0]),
            kapV=float(np.linalg.cond(Vg)),
            min_fac=(float(np.min(fac_r)) if len(fac_r)
                     else float("nan")),
            cross=bool(Q < 0.0
                       or (len(fac_r)
                           and float(np.min(fac_r)) < 0.0)))
        # ---- exact congruence branch (A_h PD only)
        ew, Vw = np.linalg.eigh(Aa)
        row["pd"] = bool(ew[0] > 0.0)
        row["tau"] = float(ew[0])
        row["gap"] = float(ew[1] - ew[0])
        row["condA"] = (float(ew[-1] / ew[0]) if ew[0] > 0.0
                        else float("inf"))
        if row["pd"]:
            Wisq = Vw @ np.diag(ew ** -0.5) @ Vw.T
            Wsq = Vw @ np.diag(ew ** 0.5) @ Vw.T
            H = Wisq @ DC @ Wisq
            nH = float(np.linalg.norm(H))
            row["asym"] = (float(np.linalg.norm(H - H.T))
                           / max(nH, 1e-300))
            Hs = 0.5 * (H + H.T)
            lam, U = np.linalg.eigh(Hs)
            recon = Wsq @ (np.eye(n) + Hs) @ Wsq
            row["rec"] = (float(np.linalg.norm(recon - Ab))
                          / max(float(np.linalg.norm(Ab)),
                                1e-300))
            row["recon_min"] = float(np.linalg.eigvalsh(
                0.5 * (recon + recon.T))[0])
            row["lam_min"] = float(lam[0])
            row["eta"] = 1.0 + float(lam[0])
            row["sim"] = (float(np.max(np.abs(
                np.sort(lam) - np.sort(mu.real))))
                / max(1.0, float(np.max(np.abs(lam)))))
            vmin = Wisq @ U[:, 0]
            vmin = vmin / float(np.linalg.norm(vmin))
            row["ovl"] = float(abs(vmin @ Vw[:, 0]))
        rows.append(row)
    return rows, n_skip


def corr_or_nan(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    m = np.isfinite(x) & np.isfinite(y)
    if int(np.sum(m)) < 3 or np.std(x[m]) == 0 or np.std(y[m]) == 0:
        return float("nan")
    return float(np.corrcoef(x[m], y[m])[0, 1])


def ols(x, y):
    """OLS y = a + b x; returns (a, b, R^2)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    b = float(np.cov(x, y, bias=True)[0, 1] / np.var(x))
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


def main():
    section("PRIME.PORT.RELCONG.01 -- the exact hermitian "
            "congruence + the margin ladder (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

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

    trows, n_skip_t = congruence_pairs(rungs, rrs)
    srows, n_skip_s = congruence_pairs(srungs, rrs)

    # ------------------------------------------------------------ R1
    section("R1 -- THE EXACT CONGRUENCE  A_{h+1} = A_h^{1/2} "
            "(I + H_h) A_h^{1/2}  (%d truth pairs; %d skips)"
            % (len(trows), n_skip_t))
    print("    H_h = A_h^{-1/2} Delta_h A_h^{-1/2}; wards: "
          "sym %.0e, recon %.0e, similarity %.0e"
          % (ASYM_WARD, RECON_WARD, SIM_WARD))
    check("W2 A_h symmetric PD on every truth full-window rung",
          all(r["pd"] for r in trows), kill="K1")
    check("W3 >= %d truth full-window pairs" % MIN_PAIRS,
          len(trows) >= MIN_PAIRS, "%d" % len(trows), kill="K1")
    asym_max = float(np.max([r["asym"] for r in trows]))
    rec_max = float(np.max([r["rec"] for r in trows]))
    sim_max = float(np.max([r["sim"] for r in trows]))
    imax = float(np.max([r["imax"] for r in trows]))
    check("R1.a SYMMETRIZATION WARD: max ||H - H^T||/||H|| "
          "%.2e <= %.0e" % (asym_max, ASYM_WARD),
          asym_max <= ASYM_WARD, kill="KW")
    check("R1.b RECONSTRUCTION WARD: max rel "
          "||A^{1/2}(I+H)A^{1/2} - A_{h+1}|| %.2e <= %.0e"
          % (rec_max, RECON_WARD), rec_max <= RECON_WARD,
          kill="KW")
    check("R1.c SIMILARITY WARD: eig(H) == eig(W^{-1}Delta), "
          "max dev %.2e <= %.0e; max rel |Im mu| %.2e <= %.0e"
          % (sim_max, SIM_WARD, imax, SIM_WARD),
          sim_max <= SIM_WARD and imax <= SIM_WARD, kill="KW")
    etas = np.array([r["eta"] for r in trows])
    n_cross_t = sum(1 for r in trows if r["cross"])
    min_eta = float(np.min(etas))
    max_neg = float(np.max([-r["lam_min"] for r in trows]))
    check("R1.d REPRODUCTION (round-50 ledger): %d pairs == %d, "
          "%d crossings == %d, min eta %.4f == %.4f, "
          "max(-lam_min) %.4f == %.4f (tol %.1e)"
          % (len(trows), REF_N_TRUTH_PAIRS, n_cross_t,
             REF_TRUTH_CROSS, min_eta, REF_TRUTH_MINETA,
             max_neg, REF_TRUTH_MAXNEG, ROUND_TOL),
          len(trows) == REF_N_TRUTH_PAIRS
          and n_cross_t == REF_TRUTH_CROSS
          and abs(min_eta - REF_TRUTH_MINETA) <= ROUND_TOL
          and abs(max_neg - REF_TRUTH_MAXNEG) <= ROUND_TOL,
          kill="KW")
    print("\n    THE EXACT FORM ESTABLISHED: on every truth step "
          "H_h is hermitian (real symmetric), the")
    print("    congruence identity reconstructs A_{h+1} to %.1e, "
          "and round 50's mu-ledger IS the" % rec_max)
    print("    hermitian spectrum eig(H_h) seen through the "
          "similarity W^{-1}Delta = A^{-1/2} H A^{1/2}.")

    # ------------------------------------------------------------ R2
    section("R2 -- THE MARGIN LADDER  eta_h = 1 + "
            "lambda_min(H_h)")
    print("    step        flow    lam_min    eta       tau_h"
          "      gap_h      ||D||_F   blkmass   ovl(soft)")
    for r in trows:
        print("    h %3d->%3d %-5s  %+.4f   %.4f   %.3e  %.3e"
              "  %.5f   %8.3f  %.3f"
              % (r["ha"], r["hb"], r["flow"], r["lam_min"],
                 r["eta"], r["tau"], r["gap"], r["dnorm"],
                 r["blkmass"], r["ovl"]))
    print("\n    eta ladder: %s | min %.4f (h %d->%d)"
          % (quart(etas), min_eta,
             trows[int(np.argmin(etas))]["ha"],
             trows[int(np.argmin(etas))]["hb"]))

    # trend fit, leave-last-third-out
    hs = np.array([r["ha"] for r in trows], float)
    order = np.argsort(hs)
    hs_o = hs[order]
    ly_o = np.log(etas[order])
    n_all = len(hs_o)
    n_fit = int(math.ceil(2.0 * n_all / HOLDOUT_FRAC))
    cands = (("POWER log eta ~ a + b log h", np.log(hs_o)),
             ("LOG   log eta ~ a + b log log h",
              np.log(np.log(hs_o))),
             ("EXP   log eta ~ a + b h", hs_o))
    print("\n    TREND (fit first %d steps by h, score RMSE on "
          "the held-out last %d):" % (n_fit, n_all - n_fit))
    best = None
    for name, x in cands:
        a, b, r2 = ols(x[:n_fit], ly_o[:n_fit])
        rmse = float(np.sqrt(np.mean(
            (ly_o[n_fit:] - a - b * x[n_fit:]) ** 2)))
        print("      %-33s b %+8.4f  R^2(in) %6.3f  "
              "RMSE(out) %.4f" % (name, b, r2, rmse))
        if best is None or rmse < best[1]:
            best = (name.split()[0], rmse, b)
    _, b_tau, _ = ols(np.log(hs_o),
                      np.log([trows[i]["tau"] for i in order]))
    _, b_gap, _ = ols(np.log(hs_o),
                      np.log([trows[i]["gap"] for i in order]))
    _, b_dn, _ = ols(np.log(hs_o),
                     np.log([trows[i]["dnorm"] for i in order]))
    _, b_eta, _ = ols(np.log(hs_o), ly_o)
    print("    best held-out candidate: %s (RMSE %.4f)"
          % (best[0], best[1]))
    print("    SHRINK COMPARISON (full-ladder power slopes vs "
          "h): eta %+0.3f | tau %+0.3f | gap %+0.3f | "
          "||D||_F %+0.3f" % (b_eta, b_tau, b_gap, b_dn))

    print("\n    THE SOURCE QUESTION: corr(log eta, z) and "
          "R^2 = corr^2 (bar %.2f):" % R2_BAR)
    leta = np.log(etas)
    sources = (
        ("log blkmass (moving-block atom mass)",
         np.log(np.maximum([r["blkmass"] for r in trows],
                           1e-300))),
        ("log ||Delta||_F (window increment)",
         np.log([r["dnorm"] for r in trows])),
        ("log tau_h (min eig A_h)",
         np.log([r["tau"] for r in trows])),
        ("log gap_h (eig2 - eig1 of A_h)",
         np.log([r["gap"] for r in trows])),
        ("ovl (soft-mode overlap, raw)",
         np.array([r["ovl"] for r in trows])))
    best_r2, best_src = -1.0, "none"
    for name, z in sources:
        c = corr_or_nan(leta, z)
        r2 = c * c if np.isfinite(c) else float("nan")
        print("      %-38s corr %+7.3f  R^2 %6.3f"
              % (name, c if np.isfinite(c) else float("nan"),
                 r2 if np.isfinite(r2) else float("nan")))
        if np.isfinite(r2) and r2 > best_r2:
            best_r2, best_src = r2, name
    margin_lab = ("MARGIN-LAWFUL" if best_r2 >= R2_BAR
                  else "MARGIN-UNEXPLAINED")
    print("    best single source: %s (R^2 %.3f)"
          % (best_src, best_r2))
    check("R2.1 typed: %s (best R^2 %.3f vs bar %.2f)"
          % (margin_lab, best_r2, R2_BAR), True)

    # ------------------------------------------------------------ R3
    section("R3 -- NON-NORMALITY DIAGNOSTICS for "
            "M = W^{-1} Delta C (general solver)")
    print("    step        rho      ||M||_2   ||M||/rho  "
          "lam_min(sym part)  kappa(V)   sqrt(cond A)  eta")
    nn_flags = []
    kap_bound_ok = True
    for r in trows:
        ratio = r["opn"] / max(r["rho"], 1e-300)
        nn_flags.append(ratio >= NN_RATIO_BAR)
        kb = math.sqrt(r["condA"])
        kap_bound_ok &= (r["kapV"] <= kb * (1.0 + 1e-6))
        print("    h %3d->%3d %7.4f  %8.4f  %8.2f   %+12.4f"
              "       %8.2f   %8.2f     %.4f"
              % (r["ha"], r["hb"], r["rho"], r["opn"], ratio,
                 r["symp"], r["kapV"], kb, r["eta"]))
    n_nn = sum(nn_flags)
    ratios = [r["opn"] / max(r["rho"], 1e-300) for r in trows]
    symp_min = float(np.min([r["symp"] for r in trows]))
    kap_med = float(np.median([r["kapV"] for r in trows]))
    rho_lab = ("RHO-MISLEADING"
               if n_nn >= NN_STEP_FRAC * len(trows)
               else "RHO-FAITHFUL")
    print("\n    CENSUS: ||M||_2/rho >= %.1f on %d/%d steps "
          "(ratio ladder: %s);" % (NN_RATIO_BAR, n_nn,
                                   len(trows), quart(ratios)))
    print("    median kappa(V) %.1f (transport bound kappa <= "
          "sqrt(cond A) holds on all steps: %s;"
          % (kap_med, kap_bound_ok))
    print("    unit-column eig basis -- the bound is for the "
          "optimally scaled diagonalizer, so excess")
    print("    is column-scaling ambiguity, SPEC v2 (i); "
          "report-only);")
    print("    lambda_min of the symmetric part reaches %+0.3f "
          "(can pass -1 with NO crossing -- the" % symp_min)
    print("    non-normal signature: symmetric-part bounds are "
          "NOT the inheritance criterion).")
    print("    STATED: the operator IS non-normal (kappa(V) >> 1"
          ", ||M||_2 > rho), so rho and any norm")
    print("    reasoning on W^{-1}Delta were the wrong "
          "instruments for margins; the SPECTRUM round 50")
    print("    reported was nevertheless exact (R1.c), and the "
          "honest carrier of the inheritance is the")
    print("    hermitian H_h, where lambda_min IS the margin.")
    check("R3.1 typed: %s (%d/%d steps with ||M||/rho >= %.1f)"
          % (rho_lab, n_nn, len(trows), NN_RATIO_BAR), True)

    # ------------------------------------------------------------ R4
    section("R4 -- THE SMOOTH WORLD (%d pairs; %d skips): where "
            "does lambda_min(H) cross -1?"
            % (len(srows), n_skip_s))
    print("    step        A_h PD  lam_min(H)  eta        "
          "cross  Q")
    first_eta_neg = None
    n_cone = 0
    for r in srows:
        if r["pd"]:
            if r["eta"] < 0.0 and first_eta_neg is None:
                first_eta_neg = r
            print("    h %3d->%3d  yes    %+9.4f  %+9.4f   "
                  "%-5s  %+.3e%s"
                  % (r["ha"], r["hb"], r["lam_min"], r["eta"],
                     str(r["cross"]), r["Q"],
                     "  <-- CROSSING" if r["cross"] else ""))
        else:
            n_cone += 1
            print("    h %3d->%3d  NO     CONE-EXITED (real "
                  "congruence unavailable)   %-5s  %+.3e%s"
                  % (r["ha"], r["hb"], str(r["cross"]), r["Q"],
                     "  <-- CROSSING" if r["cross"] else ""))
    n_cross_s = sum(1 for r in srows if r["cross"])
    n_qneg = sum(1 for r in srows if r["Q"] < 0.0)
    first_s = next((r for r in srows if r["cross"]), None)
    first_hh = ((first_s["ha"], first_s["hb"])
                if first_s is not None else (-1, -1))
    check("R4.1 REPRODUCTION (round-50 smooth ledger): %d pairs "
          "== %d, %d crossings == %d, first at h %d->%d == "
          "%d->%d, Q < 0 on %d == %d"
          % (len(srows), REF_N_SMOOTH_PAIRS, n_cross_s,
             REF_SMOOTH_CROSS, first_hh[0], first_hh[1],
             REF_SMOOTH_FIRST[0], REF_SMOOTH_FIRST[1], n_qneg,
             REF_SMOOTH_QNEG),
          len(srows) == REF_N_SMOOTH_PAIRS
          and n_cross_s == REF_SMOOTH_CROSS
          and first_hh == REF_SMOOTH_FIRST
          and n_qneg == REF_SMOOTH_QNEG, kill="KW")
    s_pd = [r for r in srows if r["pd"]]
    s_eta_neg = [r for r in s_pd if r["eta"] < 0.0]
    s_min_eta = (float(np.min([r["eta"] for r in s_pd]))
                 if s_pd else float("nan"))
    if first_eta_neg is not None:
        print("\n    FIRST lambda_min(H) < -1 (PD branch): "
              "h %d->%d (eta %+0.4f)"
              % (first_eta_neg["ha"], first_eta_neg["hb"],
                 first_eta_neg["eta"]))
    print("    CONTRAST: truth min eta = %+0.4f (all %d steps "
          "> 0) vs smooth min eta = %s on %d PD"
          % (min_eta, len(trows),
             ("%+0.4f" % s_min_eta) if s_pd else
             "none (empty PD branch, SPEC v2 (ii))",
             len(s_pd)))
    print("    steps (eta < 0 on %d of them) + %d CONE-EXITED "
          "steps (A_h itself indefinite -- the smooth"
          % (len(s_eta_neg), n_cone))
    print("    world does not even keep the congruence's PD "
          "premise).  The discriminating gap is the")
    print("    margin sign: truth stays a strictly positive "
          "eta ladder; smooth crosses and exits.")
    smooth_lab = ("SMOOTH-DISCRIMINATES"
                  if (min_eta > 0.0
                      and (len(s_eta_neg) > 0 or n_cone > 0))
                  else "SMOOTH-NONDISCRIMINATING")
    check("R4.2 typed: %s (smooth eta < 0 on %d PD steps, "
          "CONE-EXITED on %d)"
          % (smooth_lab, len(s_eta_neg), n_cone), True)

    # ------------------------------------------------------------ R5
    section("R5 -- THE HERMITIAN INHERITANCE MINI-THEOREM, "
            "numerically")
    rec_pd_ok = all(r["recon_min"] > 0.0 for r in trows)
    eta_pos_ok = all(r["eta"] > 0.0 for r in trows)
    rec_min_min = float(np.min([r["recon_min"] for r in trows]))
    check("R5.1 one-step Sylvester inheritance verified: eta_h "
          "> 0 on all %d steps AND reconstructed A_{h+1} PD "
          "(min eig %+0.3e > 0) on all steps"
          % (len(trows), rec_min_min),
          rec_pd_ok and eta_pos_ok)
    print("\n    THE MINI-THEOREM (exact): A_h PD, Delta_h "
          "symmetric, A_{h+1} = A_h + Delta_h,")
    print("    H_h = A_h^{-1/2} Delta_h A_h^{-1/2}  ==>  "
          "A_{h+1} = A_h^{1/2}(I + H_h)A_h^{1/2}, and by")
    print("    Sylvester congruence  A_{h+1} PD  <=>  "
          "lambda_min(H_h) > -1  <=>  eta_h > 0.")
    print("    THE FULL LADDER INDUCTION reduces to:")
    print("      (i)  ONE certified base rung A_{h0} PD "
          "(exists: v884 certified head positivity /")
    print("           v887 certified ladder -- cited, not "
          "re-run);")
    print("      (ii) THE MARGIN INEQUALITY: eta_h = 1 + "
          "lambda_min(H_h) > 0 for every step h.")
    print("    FINITE SHADOW (measured, this run): eta_h > 0 on "
          "%d/%d deployed steps; min eta = %.4f"
          % (int(np.sum(etas > 0.0)), len(trows), min_eta))
    print("    at h %d->%d; margin trend and sources in R2 "
          "(typed %s).  NO claim beyond the ladder."
          % (trows[int(np.argmin(etas))]["ha"],
             trows[int(np.argmin(etas))]["hb"], margin_lab))

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
          "crossings ward-anchored in R4.1 (%d crossing steps)."
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
        VERDICT = ("RELCONG-MEASURED / %s / %s / %s"
                   % (margin_lab, rho_lab, smooth_lab))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (min eta %.4f on %d truth steps; best source "
              "R^2 %.3f (%s); ||M||/rho >= %.1f on %d/%d;"
              % (min_eta, len(trows), best_r2, best_src,
                 NN_RATIO_BAR, n_nn, len(trows)))
        print("   smooth: eta < 0 on %d PD steps + %d "
              "CONE-EXITED, first crossing h %d->%d)"
              % (len(s_eta_neg), n_cone, first_hh[0],
                 first_hh[1]))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source pivot_factor_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pivot_factor_probe -- PRIME.PORT.PIVOTFACTOR.01
(EXPLORATION ONLY, experiments/; round 51, reviewer priority 2:
the pivot factorization of PD inheritance -- do the 12 LDL^T
pivots of A_h = I - C_h factor rung-to-rung as d_{k,h+1} =
d_{k,h} (1 + mu_{k,h}) with every 1 + mu_{k,h} > 0 on truth?
Potentially the SHORTEST real induction of the program.
2026-08-09.)

THE ALGEBRA (frozen; elementary and exact).  For symmetric A
with nonvanishing leading principal minors tau^(k), the
unpivoted LDL^T factorization exists and its pivots are the
minor quotients
    d_k = tau^(k) / tau^(k-1),        tau^(0) := 1.
Between consecutive rungs the pivot ratio is therefore
    r_{k,h} := d_{k,h+1} / d_{k,h}
             = ( tau^(k)_{h+1} tau^(k-1)_h )
               / ( tau^(k)_h tau^(k-1)_{h+1} )
             = Q_k / Q_{k-1},
    Q_k := tau^(k)_{h+1} / tau^(k)_h    (leading-minor quotient,
                                         Q_0 := 1),
so with mu_{k,h} := r_{k,h} - 1 the factorization
    d_{k,h+1} = d_{k,h} (1 + mu_{k,h})
is an IDENTITY (warded, never the content).  The CONTENT is the
sign: since Q_k = prod_{j<=k} r_j,
    1 + mu_{k,h} > 0 for ALL k   <=>   Q_k > 0 for ALL k
(the FLAG QUOTIENT CHAIN), and then d > 0 and r > 0 imply
d' > 0 for every k SIMULTANEOUSLY -- PD inheritance by pure
algebra, no norm bound, no spectral gauge.  THE PIVOT INDUCTION
(P5, statement): base d_{k,H0} > 0 at the first rung (v884 /
v887 certify A = I - C PD at the base -- declared input, not
re-run) + Q_{k,h} > 0 for all k on all steps h  =>  d_{k,h} > 0
on the whole ladder.  Its finite shadow is the P2 census; the
single open inequality is min_k Q_{k,h} > 0.  This is the
per-flag strengthening of the round-CVII scalar Q_12 > 0
(tau_mobius_factor: truth Q_12 > 0 on 31/31; smooth-mass world
Q_12 < 0 on 16/28).

THE LADDER (frozen, factor_avoidance_euler verbatim): all
frame-A zones (core.frame_a_zones()) with h <= 900, sorted by
(h, kz); consecutive FULL-WINDOW pairs (both rungs carry all 12
indices of J = {2, 4, ..., 24}; typed skips counted); truth +
smooth-mass world (B1 LATTICE-SMOOTH masses m_n = 2 e^{u_n/2}
du_n, midpoint cells, lattice_parametrix verbatim);
Epstein/scramble frame status reported (C1).  v563 READ-ONLY.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 P1  THE PIVOT LADDERS: per truth full-window rung the 12
     unpivoted-LDL^T pivots d_{k,h} of A_h = I - C_h (own
     factorization routine).  Ward W1 (kill -> WARD-BROKEN):
     d_{k,h} == tau^(k)_h / tau^(k-1)_h against the hirota-
     probe minor ladder (np.linalg.det of the nested leading
     sections, the port_tau_hirota object) -- scaled deviation
     |d_ldl - d_minor| / max(|d_ldl|, |d_minor|, 1e-300)
     <= 1e-10 on every rung and every k.  Pivot sign census
     printed (hirota reproduction: all 12 pivots positive on
     37/37 rungs <=> MINORS-POSITIVE).  Per step the ratios
     r_{k,h} = d_{k,h+1} / d_{k,h}; the 12 ratio ladders
     printed compactly (min / q25 / med / q75 / max per k over
     the truth steps).

 P2  THE IDENTITY + THE FLAG CENSUS (the new content): per
     truth step and per k, Q_k from slogdet of the leading
     k x k sections (sign * exp(logdet difference); numerically
     independent route).  Ward W2 (kill -> WARD-BROKEN): the
     EXACT identity r_{k,h} = Q_k / Q_{k-1} -- scaled deviation
     <= 1e-9 on every step and every k.  CENSUS (typed, never
     kills): FLAG-POSITIVE iff Q_{k,h} > 0 for EVERY k = 1..12
     on EVERY truth step (then the pivot induction closes over
     the measured ladder); else FLAG-VIOLATED with the (step,
     k) census.  Per-k margins printed: min_h Q_{k,h} and
     quartiles.

 P3  THE SMOOTH CONTRAST: the same flag census on the smooth-
     mass world.  Reproduction ward A0 (kill -> WARD-BROKEN):
     truth pairs == 31, smooth pairs == 28, truth Q_12 > 0 on
     31/31, smooth Q_12 < 0 on exactly 16/28 (tau_mobius /
     factor_avoidance printed ledgers).  At every smooth flag-
     crossing step the CROSSING DEPTH PROFILE: the violated
     flag set {k : Q_k <= 0}, its minimal element (does the
     violation enter at the soft flag k = 12 or in the bulk?),
     the census over steps printed.  Truth-vs-smooth contrast:
     min_k min_h Q_{k,h} per world.

 P4  THE PER-PRIME QUESTION (report only): at the 3 frozen
     MEDIUM truth steps (the middle three of the truth full-
     window step list sorted by h), the LEAVE-ONE-PRIME-OUT
     response of the pivot ratios: for each of the NP_TOP = 6
     largest in-window-mass base primes p (atoms grouped by own
     trial division, v882 own-sieve precedent; every atom must
     parse as a prime power -- ward, kill -> WARD-BROKEN),
     rebuild BOTH rungs without p's full atom group (deployed
     builder, comb override, truth masses) and form the pivot-
     ratio response R_p = max_k |r^{-p}_{k} / r_{k} - 1|.
     Frozen reading bars (round-50 finding of frame leverage is
     the declared prior): step scale s0 = max_k |r_{k} - 1|;
     PIVOT-GRAIN-NONDECOMPOSITIONAL iff sum_p R_p > 10 * s0
     (the responses are frame leverage, not increment grain);
     PIVOT-GRAIN-UNDERSAMPLED iff < 3 leave-outs survive
     (LEAVEOUT-DEAD typed, counted); else the share reading
     (top share > 0.8 coherent / < 0.5 diffuse).  If
     nondecompositional on the modal step, SAY SO and close the
     per-prime reading for pivots too.

 P5  THE INDUCTION STATEMENT (print): base + flag chain =>
     ladder positivity (the algebra above); its finite shadow
     is the P2 census.  The open inequality min_k Q_{k,h} > 0
     printed as a ladder (per step: min_k Q_k and argmin k)
     with the margin trend (median of min_k Q_k, first half vs
     second half of the steps in h-order).

 C   CONTROLS: (C2, PRIMARY, kill -> CONTROL-DEAD) the smooth-
     mass world must show flag violations (the detector must
     fire on the control world; anchored numerically in A0).
     (C1, kz 9, must fire, kill -> CONTROL-DEAD) Epstein
     (lambda_eps recursion comb) + scramble (seed 1): the
     compressed frame must die (exterior supercritical OR
     lam(C_J) > 1 OR window unavailable); channel reported.

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W0 >= 30 truth
     rungs; W0b the atom prefix law exact; W0c truth full-
     window rung census == 37 (hirota census).

KILLS: KP pipeline ward breaks -> PIPELINE-BROKEN; KW ward
breaks (W1 pivot==minor / W2 identity / A0 reproduction / P4
prime parse) -> WARD-BROKEN; KC controls silent ->
CONTROL-DEAD.  P2/P3 censuses and P4 readings are TYPED /
reported, never kill.

VERDICT (frozen enum): PIVOTFACTOR-MEASURED (+ typed:
FLAG-POSITIVE / FLAG-VIOLATED(k-profile) /
FLAG-UNDECIDABLE(ratio) per world (SPEC v2 (ii)), the P4
grain label) / PIPELINE-BROKEN / WARD-BROKEN / CONTROL-DEAD.

SPEC v2 (2026-08-09, after runs 1-2; fail-first preserved --
every run-1/2 raw number stands and is reprinted unchanged; no
bar was moved to rescue a failing measurement):

 (i)   DISPLAY ONLY: the P2/P5 margin prints moved from fixed
       (%.4f) to scientific notation after run 1 printed the
       load-bearing ladder minimum (min_k min_h Q =
       2.059e-14 > 0) as "0.0000".  No bar, no object changed.

 (ii)  SIGN DECIDABILITY PRECONDITION added after run 2: the
       ladder min Q_12 = 2.1e-14 is a quotient of determinants
       14 orders apart, so the census sign is trustworthy only
       if every participating minor's sign sits above the
       floating-point noise floor.  New diagnostic (printed +
       typing precondition, frozen): per full-window rung,
       lam_min(A_h) from eigh (backward stable; absolute
       eigenvalue error ~ eps ||A||) against the floor
       NW * eps * lam_max(A_h); by Cauchy interlacing
       lam_min(A[:k,:k]) >= lam_min(A) for every leading
       section, so ONE floor per rung covers all 12 flags.
       The truth census is typed FLAG-POSITIVE only if the
       minimal decidability ratio over the truth rungs
       >= DECIDE_BAR = 1e3; else FLAG-UNDECIDABLE(ratio).
       (Smooth world: A indefinite, interlacing gives no
       |lambda| floor per section -- the smooth min |lambda|
       ratio is REPORTED, the smooth typing keeps its census.)
       Measured out-of-band before freezing: worst truth ratio
       6.4e9 -- decisively decidable.

HONEST FRAME: the factorization d' = d (1 + mu) is an identity
-- warded bookkeeping, zero content.  The content is the SIGN
census of the flag quotient chain Q_k on the measured ladder,
and the census is FINITE: it certifies the deployed rungs, it
does NOT prove the open inequality min_k Q_{k,h} > 0 beyond
them.  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); the P4 grouping uses an OWN trial-division
smallest-prime-factor routine (v882 own-sieve precedent);
v563 READ-ONLY; RNG only inside the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts (build_window,
atom_lags_at, arch_lags, U_ALL / MU_ALL prefix law -- verbatim);
window compression + ladder scope + smooth-mass world verbatim
from factor_avoidance_euler_probe.py (PRIME.PORT.FACTORAVOID.01)
via tau_mobius_factor_probe / port_schur_cocycle_probe /
lattice_parametrix_probe; port_tau_hirota_probe
(PRIME.PORT.HIROTA.01: the minor ladder object + the 37-rung
census + MINORS-POSITIVE, the P1 ward anchor); v884/v887
(base-rung PD certificate -- declared input, not re-run).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/pivot_factor_probe.py
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
NW = 12
MIN_RUNGS = 30
N_FULLWIN_FROZEN = 37       # hirota-probe truth census
MIN_COMMON_J = 8
PIV_WARD = 1e-10            # W1 pivot == minor quotient (kill)
ID_WARD = 1e-9              # W2 r_k == Q_k/Q_{k-1} (kill)
NP_TOP = 6                  # P4 leave-out primes
MEDIUM_N = 3                # P4 medium truth steps
LEV_BAR = 10.0              # P4 leverage bar (vs step scale)
MIN_LO_ALIVE = 3            # P4 undersampling bar
GRAIN_DIFFUSE_BAR = 0.5     # P4 share bars (where valid)
GRAIN_COHERENT_BAR = 0.8
DECIDE_BAR = 1e3            # SPEC v2 (ii) sign decidability
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# A0 reproduction anchors (tau_mobius_factor /
# factor_avoidance_euler printed ledgers, re-verified there)
REF_N_TRUTH_PAIRS = 31
REF_N_SMOOTH_PAIRS = 28
REF_TRUTH_Q12_NEG = 0
REF_SMOOTH_Q12_NEG = 16

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


# --------- pipeline, verbatim from factor_avoidance_euler_probe
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
    """One rung -> 12x12 window compression (factor_avoidance
    verbatim)."""
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


def comb_of(idx_set, world):
    """Comb arrays for an index set into U_ALL (truth = deployed
    masses; smooth = B1 masses on the set's own lattice)."""
    ii = np.array(sorted(idx_set), dtype=int)
    uu = np.asarray(core.U_ALL, float)[ii]
    if world == "truth":
        return uu, np.asarray(core.MU_ALL, float)[ii]
    return uu, smooth_masses(uu)


def death_channel(hy):
    """Classify a failed rebuild."""
    if not isinstance(hy, dict):
        return "CHAIN-DEATH"
    if "CJ" not in hy:
        return "WINDOW-LOST"
    if not hy.get("full"):
        return "PARTIAL-WINDOW"
    return None


# ------------------------------------------- pivot machinery (new)
def ldl_pivots(A):
    """Unpivoted LDL^T pivots of symmetric A (own routine); None
    on an exactly-zero pivot."""
    n = A.shape[0]
    L = np.zeros((n, n))
    d = np.zeros(n)
    for j in range(n):
        d[j] = A[j, j] - float(np.sum(L[j, :j] ** 2 * d[:j]))
        if d[j] == 0.0:
            return None
        L[j, j] = 1.0
        for i in range(j + 1, n):
            L[i, j] = (A[i, j] - float(
                np.sum(L[i, :j] * L[j, :j] * d[:j]))) / d[j]
    return d


def lead_minors(A):
    """tau^(k), k = 0..NW (tau^(0) = 1), np.linalg.det route --
    the port_tau_hirota minor-ladder object."""
    t = [1.0]
    for k in range(1, NW + 1):
        t.append(float(np.linalg.det(A[:k, :k])))
    return np.array(t)


def lead_slogdets(A):
    """(sign, logdet) of the leading k x k sections, k = 0..NW
    (numerically independent route for the Q_k quotients)."""
    out = [(1.0, 0.0)]
    for k in range(1, NW + 1):
        sg, ld = np.linalg.slogdet(A[:k, :k])
        out.append((float(sg), float(ld)))
    return out


def rung_pivots(r):
    """Attach A = I - C_J, minors, pivots, slogdets to a rung."""
    A = np.eye(NW) - r["CJ"]
    taus = lead_minors(A)
    dmin = taus[1:] / taus[:-1]         # minor-quotient pivots
    dldl = ldl_pivots(A)
    dev = (float(np.max(np.abs(dldl - dmin)
                        / np.maximum(np.maximum(np.abs(dldl),
                                                np.abs(dmin)),
                                     1e-300)))
           if dldl is not None else float("inf"))
    ew = np.linalg.eigvalsh(A)
    r["A"] = A
    r["taus"] = taus
    r["piv"] = dmin
    r["piv_dev"] = dev
    r["sld"] = lead_slogdets(A)
    r["lam_min"] = float(ew[0])
    r["lam_absmin"] = float(np.min(np.abs(ew)))
    r["lam_max"] = float(ew[-1])
    return r


def flag_rows(rungs):
    """Consecutive full-window pairs -> pivot ratios r_k, flag
    quotients Q_k, identity deviation, violated-flag set."""
    rows = []
    n_skip = 0
    for t, (ra, rb) in enumerate(zip(rungs[:-1], rungs[1:])):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        rk = rb["piv"] / ra["piv"]
        Q = np.zeros(NW + 1)
        Q[0] = 1.0
        for k in range(1, NW + 1):
            sga, lda = ra["sld"][k]
            sgb, ldb = rb["sld"][k]
            Q[k] = sga * sgb * math.exp(ldb - lda)
        dev = 0.0
        for k in range(1, NW + 1):
            qq = Q[k] / Q[k - 1] if Q[k - 1] != 0.0 else float(
                "inf")
            dev = max(dev, abs(rk[k - 1] - qq)
                      / max(abs(rk[k - 1]), abs(qq), 1e-300))
        viol = [k for k in range(1, NW + 1) if Q[k] <= 0.0]
        rows.append(dict(t=t, ra=ra, rb=rb, ha=ra["h"],
                         hb=rb["h"], kza=ra["kz"], kzb=rb["kz"],
                         rk=rk, Q=Q[1:], id_dev=dev, viol=viol,
                         minQ=float(np.min(Q[1:])),
                         argminQ=int(np.argmin(Q[1:])) + 1))
    return rows, n_skip


def quart_row(v):
    v = np.asarray(v, float)
    q = np.percentile(v, [25, 50, 75])
    return (float(np.min(v)), q[0], q[1], q[2],
            float(np.max(v)))


def main():
    section("PRIME.PORT.PIVOTFACTOR.01 -- the pivot factorization "
            "d_{k,h+1} = d_{k,h}(1 + mu_{k,h}) of PD inheritance "
            "(EXPLORATION ONLY)")
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
    check("W0 >= %d truth rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="KP")
    check("W0b atom prefix law exact (max |mm - MU_ALL prefix| "
          "%.1e == 0)" % pref_dev, pref_dev == 0.0, kill="KP")
    n_full_t = sum(1 for r in rungs if r.get("full"))
    check("W0c truth full-window census %d == %d (hirota frozen)"
          % (n_full_t, N_FULLWIN_FROZEN),
          n_full_t == N_FULLWIN_FROZEN, kill="KP")

    # ------------------------------------------------------------ P1
    section("P1 -- THE PIVOT LADDERS: unpivoted LDL^T pivots "
            "d_{k,h} of A_h = I - C_h + ward vs the minor "
            "quotients (truth)")
    w1_max = 0.0
    n_piv_neg = 0
    for r in rungs:
        if not r.get("full"):
            continue
        rung_pivots(r)
        w1_max = max(w1_max, r["piv_dev"])
        n_piv_neg += int(np.sum(r["piv"] <= 0.0))
    for r in srungs:
        if r.get("full"):
            rung_pivots(r)
    s_dev = max((r["piv_dev"] for r in srungs if r.get("full")),
                default=0.0)
    check("W1 PIVOT == MINOR QUOTIENT on every truth full-window "
          "rung and every k: max scaled dev %.1e <= %.0e"
          % (w1_max, PIV_WARD), w1_max <= PIV_WARD, kill="KW")
    print("    (smooth-world LDL vs minors, reported: max dev "
          "%.1e -- indefinite unpivoted LDL, no bar)" % s_dev)
    check("P1.0 pivot sign census (hirota MINORS-POSITIVE "
          "reproduction): nonpositive pivots %d == 0 on %d/%d "
          "rungs" % (n_piv_neg, n_full_t, n_full_t),
          n_piv_neg == 0)

    trows, n_skip_t = flag_rows(rungs)
    srows, n_skip_s = flag_rows(srungs)
    print("\n    truth steps: %d full-window pairs (%d typed "
          "skips) | smooth steps: %d (%d skips)"
          % (len(trows), n_skip_t, len(srows), n_skip_s))
    print("\n    THE 12 RATIO LADDERS r_{k,h} = d_{k,h+1} / "
          "d_{k,h} (truth, %d steps):" % len(trows))
    print("    %-3s %-9s %-9s %-9s %-9s %-9s %s"
          % ("k", "min", "q25", "med", "q75", "max", "min>0"))
    for k in range(NW):
        vv = [row["rk"][k] for row in trows]
        mn, q1, q2, q3, mx = quart_row(vv)
        print("    %-3d %-9.4f %-9.4f %-9.4f %-9.4f %-9.4f %s"
              % (k + 1, mn, q1, q2, q3, mx, mn > 0.0))

    # ------------------------------------------------------------ P2
    section("P2 -- THE IDENTITY r_k = Q_k / Q_{k-1} (warded) + "
            "THE FLAG QUOTIENT CENSUS Q_k > 0 (truth)")
    id_max_t = max(row["id_dev"] for row in trows)
    id_max_s = max(row["id_dev"] for row in srows)
    check("W2 IDENTITY r_{k,h} == Q_k / Q_{k-1} on every truth "
          "step and every k: max scaled dev %.1e <= %.0e"
          % (id_max_t, ID_WARD), id_max_t <= ID_WARD, kill="KW")
    print("    (smooth identity dev, same algebra: max %.1e -- "
          "reported)" % id_max_s)
    print("\n    per-k flag-quotient margins over the %d truth "
          "steps:" % len(trows))
    print("    %-3s %-11s %-11s %-11s %-11s %s"
          % ("k", "min Q_k", "q25", "med", "q75", "min>0"))
    for k in range(NW):
        vv = [row["Q"][k] for row in trows]
        mn, q1, q2, q3, _ = quart_row(vv)
        print("    %-3d %-11.3e %-11.3e %-11.3e %-11.3e %s"
              % (k + 1, mn, q1, q2, q3, mn > 0.0))
    eps = float(np.finfo(float).eps)
    dec_t = min(r["lam_min"] / (NW * eps * r["lam_max"])
                for r in rungs if r.get("full"))
    print("\n    SIGN DECIDABILITY (SPEC v2 (ii)): min over "
          "truth rungs of lam_min(A) / (12 eps lam_max(A)) = "
          "%.1e (bar %.0e; Cauchy interlacing covers all 12 "
          "flags per rung)" % (dec_t, DECIDE_BAR))
    t_viol = [(row["ha"], row["hb"], row["viol"])
              for row in trows if row["viol"]]
    if dec_t < DECIDE_BAR:
        flag_t = "FLAG-UNDECIDABLE(ratio=%.1e)" % dec_t
    elif not t_viol:
        flag_t = "FLAG-POSITIVE"
    else:
        flag_t = "FLAG-VIOLATED(%s)" % t_viol
    minQ_t = float(np.min([row["minQ"] for row in trows]))
    check("P2.s truth flag census typed %s -- Q_k > 0 for all "
          "k = 1..12 on %d/%d steps; min_k min_h Q = %.3e"
          % (flag_t, len(trows) - len(t_viol), len(trows),
             minQ_t), True)

    # ------------------------------------------------------------ P3
    section("P3 -- THE SMOOTH CONTRAST: the same flag census on "
            "the smooth-mass world + the crossing depth profile")
    n_q12neg_t = sum(1 for row in trows if row["Q"][NW - 1] < 0.0)
    n_q12neg_s = sum(1 for row in srows if row["Q"][NW - 1] < 0.0)
    check("A0 REPRODUCTION: truth pairs %d == %d, smooth pairs "
          "%d == %d, truth Q_12 < 0 on %d == %d, smooth Q_12 < 0 "
          "on %d == %d (predecessor ledgers)"
          % (len(trows), REF_N_TRUTH_PAIRS, len(srows),
             REF_N_SMOOTH_PAIRS, n_q12neg_t, REF_TRUTH_Q12_NEG,
             n_q12neg_s, REF_SMOOTH_Q12_NEG),
          len(trows) == REF_N_TRUTH_PAIRS
          and len(srows) == REF_N_SMOOTH_PAIRS
          and n_q12neg_t == REF_TRUTH_Q12_NEG
          and n_q12neg_s == REF_SMOOTH_Q12_NEG, kill="KW")
    s_cross = [row for row in srows if row["viol"]]
    print("\n    smooth flag-crossing steps: %d/%d"
          % (len(s_cross), len(srows)))
    print("    step        min_k Q_k  argmin  violated flags "
          "{k : Q_k <= 0}")
    for row in s_cross:
        print("    h %3d->%3d  %+9.3e  k=%-4d %s"
              % (row["ha"], row["hb"], row["minQ"],
                 row["argminQ"], row["viol"]))
    depth = {}
    for row in s_cross:
        kmin = min(row["viol"])
        depth[kmin] = depth.get(kmin, 0) + 1
    n_soft = sum(1 for row in s_cross if row["viol"] == [NW])
    print("\n    CROSSING DEPTH PROFILE (minimal violated flag "
          "per step): %s"
          % (sorted(depth.items()) if depth else "none"))
    print("    soft-flag-only steps (violated set == {12}): "
          "%d/%d -- the violation %s"
          % (n_soft, len(s_cross),
             "enters at the soft flag k = 12 only"
             if n_soft == len(s_cross) else
             "reaches the BULK flags (k < 12)"))
    dec_s = min(r["lam_absmin"] / (NW * eps * r["lam_max"])
                for r in srungs if r.get("full"))
    print("\n    (smooth sign decidability, REPORTED per SPEC "
          "v2 (ii): min |lambda|(A) / (12 eps lam_max) = %.1e "
          "-- no interlacing floor on indefinite A)" % dec_s)
    minQ_s = (float(np.min([row["minQ"] for row in srows]))
              if srows else float("nan"))
    flag_s = ("FLAG-POSITIVE" if not s_cross else
              "FLAG-VIOLATED(depth=%s)" % sorted(depth.items()))
    check("P3.s smooth flag census typed %s -- %d/%d crossing "
          "steps" % (flag_s, len(s_cross), len(srows)), True)
    print("\n    TRUTH-vs-SMOOTH CONTRAST: min_k min_h Q_k = "
          "%+.3e (truth, positive) vs %+.3e (smooth)"
          % (minQ_t, minQ_s))

    # ------------------------------------------------------------ P4
    section("P4 -- THE PER-PRIME QUESTION (report only): leave-"
            "one-prime-out response of the pivot ratios at %d "
            "frozen medium truth steps" % MEDIUM_N)
    print("    (declared prior: round-50 factor_avoidance found "
          "leave-out responses to be FRAME LEVERAGE, not")
    print("    increment grain -- sum_p rho_p ~ 1e4 vs rho_tot "
          "~ 1-4.  Frozen bar here: NONDECOMPOSITIONAL iff")
    print("    sum_p R_p > %.0f x step scale s0 = max_k "
          "|r_k - 1|.)" % LEV_BAR)
    i0 = (len(trows) - MEDIUM_N) // 2
    parse_ok = True
    grain = []
    for row in trows[i0:i0 + MEDIUM_N]:
        ka = int(rrs[row["kza"]]["n_atom"])
        kb = int(rrs[row["kzb"]]["n_atom"])
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
        s0 = float(np.max(np.abs(row["rk"] - 1.0)))
        print("\n  TRUTH h %d->%d (kz %d->%d; step scale s0 = "
              "max_k |r_k - 1| = %.4f)"
              % (row["ha"], row["hb"], row["kza"], row["kzb"],
                 s0))
        print("    p       n_pow  R_p = max_k |r^-p_k / r_k - 1|"
              "   sign flips")
        resp = []
        n_dead = 0
        for p in order:
            gset = set(groups[p])
            ca = rung_win(row["kza"],
                          comb=comb_of([i for i in range(ka)
                                        if i not in gset],
                                       "truth"),
                          rr_cache=rrs[row["kza"]])
            cb = rung_win(row["kzb"],
                          comb=comb_of([i for i in range(kb)
                                        if i not in gset],
                                       "truth"),
                          rr_cache=rrs[row["kzb"]])
            if (death_channel(ca) is not None
                    or death_channel(cb) is not None):
                n_dead += 1
                print("    %-7d LEAVEOUT-DEAD (a: %s, b: %s)"
                      % (p, death_channel(ca) or "ok",
                         death_channel(cb) or "ok"))
                continue
            rung_pivots(ca)
            rung_pivots(cb)
            rkp = cb["piv"] / ca["piv"]
            n_flip = int(np.sum((rkp > 0) != (row["rk"] > 0)))
            Rp = float(np.max(np.abs(rkp / row["rk"] - 1.0)))
            resp.append((p, Rp))
            print("    %-7d %4d   %-32.4f %d"
                  % (p, len(groups[p]), Rp, n_flip))
        if len(resp) < MIN_LO_ALIVE:
            gt = "PIVOT-GRAIN-UNDERSAMPLED"
        else:
            sum_R = sum(x[1] for x in resp)
            top = max(x[1] for x in resp)
            lev = sum_R / max(s0, 1e-300)
            if lev > LEV_BAR:
                gt = "PIVOT-GRAIN-NONDECOMPOSITIONAL"
            else:
                share = top / sum_R
                gt = ("PIVOT-GRAIN-DIFFUSE"
                      if share <= GRAIN_DIFFUSE_BAR
                      else "PIVOT-GRAIN-COHERENT"
                      if share >= GRAIN_COHERENT_BAR
                      else "PIVOT-GRAIN-INTERMEDIATE")
            print("    sum_p R_p = %.4f | s0 = %.4f | leverage "
                  "ratio %.1f (bar %.0f) | dead %d -> %s"
                  % (sum_R, s0, lev, LEV_BAR, n_dead, gt))
        grain.append(gt)
    check("P4.1 prime parse ward: every window atom is a prime "
          "power (own trial division)", parse_ok, kill="KW")
    gmodal = (max(set(grain), key=grain.count)
              if grain else "PIVOT-GRAIN-UNAVAILABLE")
    check("P4.s pivot grain typed (modal of %d steps): %s"
          % (len(grain), gmodal), True)
    if gmodal == "PIVOT-GRAIN-NONDECOMPOSITIONAL":
        print("""
    THE PER-PRIME READING IS CLOSED FOR PIVOTS TOO: exactly as
    in round 50, removing ONE prime moves the window operators
    (and hence every pivot ratio) by far more than the whole
    step does -- the leave-out response is FRAME LEVERAGE of
    the collective window re-test, not a per-prime
    decomposition of the flag increments mu_{k,h}.  The flag
    chain Q_k is a property of the collective comb; no
    single-prime channel carries it.""")

    # ------------------------------------------------------------ P5
    section("P5 -- THE PIVOT INDUCTION (statement + the open "
            "inequality's ladder)")
    print("""
    STATEMENT (algebra, no proof of the open part): base
    d_{k,H0} > 0 (v884/v887 certify A = I - C PD at the base
    rung -- declared input) + Q_{k,h} > 0 for all k = 1..12 on
    every step h  =>  d_{k,h} = d_{k,H0} prod_h (1 + mu_{k,h})
    > 0 for all k on the whole ladder -- PD inheritance by pure
    algebra.  The P2 census is the FINITE SHADOW of this
    induction on the measured ladder; the OPEN INEQUALITY is
    min_k Q_{k,h} > 0 beyond it.""")
    print("    the open inequality's ladder (truth, per step):")
    print("    %-12s %-11s %s" % ("step", "min_k Q_k", "argmin"))
    mins = []
    for row in trows:
        mins.append(row["minQ"])
        print("    h %3d->%3d   %-11.3e k=%d"
              % (row["ha"], row["hb"], row["minQ"],
                 row["argminQ"]))
    nh = len(mins) // 2
    m1 = float(np.median(mins[:nh]))
    m2 = float(np.median(mins[nh:]))
    print("\n    MARGIN TREND: median min_k Q_k = %.3e (first "
          "%d steps) vs %.3e (last %d) -- %s with depth; "
          "ladder min %.3e"
          % (m1, nh, m2, len(mins) - nh,
             "tightening" if m2 < m1 else "stable/widening",
             minQ_t))
    check("P5.1 induction shadow reported (min_k min_h Q = %.3e "
          "> 0: %s)" % (minQ_t, minQ_t > 0.0), True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C2 -- smooth-mass world (PRIMARY): the flag "
          "detector must fire on the control world.")
    check("C2 smooth flag violations present (%d/%d crossing "
          "steps)" % (len(s_cross), len(srows)),
          len(s_cross) > 0, kill="KC")
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
          ok1, kill="KC")

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN", "KW": "WARD-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("PIVOTFACTOR-MEASURED / truth %s / smooth %s "
                   "/ %s" % (flag_t, flag_s, gmodal))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (truth min_k min_h Q = %.3e > 0; smooth min "
              "%.3e; smooth crossings %d/%d)"
              % (minQ_t, minQ_s, len(s_cross), len(srows)))
    print("""
  HONEST FRAME (as frozen): the factorization d' = d (1 + mu)
  is an identity -- warded bookkeeping, zero content.  The
  content is the SIGN census of the flag quotient chain Q_k on
  the measured ladder; it is FINITE and certifies only the
  deployed rungs.  The open inequality min_k Q_{k,h} > 0 beyond
  the ladder is NOT proved here.  NO RH claim.  No marker
  moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source euler_rouche_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""euler_rouche_probe -- PRIME.PORT.EULER.ROUCHE.01
(EXPLORATION ONLY, experiments/; round 51, reviewer priority 3:
the matrix-Rouche form of corridor inheritance -- can ONE norm
bound on a contour force the Euler extension step h -> h+1 to
preserve the determinant-zero count inside the corridor?
2026-08-09.)

THE QUESTION (frozen).  port_sflow_toda_probe measured: the
truth corridor is pole-free on s in [0, 1] -- for A_h(s) =
I - s C_h on the fixed 12-window the first determinant zero
sits at s*_h = 1/lam_max(C_h) > 1 on every full-window rung,
while the smooth-mass world violates its wall (s* <= 1).
factor_avoidance_euler_probe measured the one-step increments
Delta C = C_{h+1} - C_h.  THE ROUCHE FORM asked here: on a
closed contour Gamma enclosing the physical corridor [0, 1],
does
    M_h := sup_{s in Gamma} ||A_h(s)^{-1} Delta_h(s)||_2 < 1,
    Delta_h(s) := A_{h+1}(s) - A_h(s) = -s (C_{h+1} - C_h)
hold on truth?  THE ROUCHE STATEMENT (exact, elementary): if
A_h(s) is invertible for every s on Gamma and M_h < 1, then
det A_{h+1} = det A_h * det(I + A_h^{-1} Delta_h) and the
homotopy A^(t) := A_h + t Delta_h (t in [0, 1]) satisfies
||A_h^{-1} t Delta_h|| <= t M_h < 1 on Gamma, so det A^(t)(s)
!= 0 for every s on Gamma and every t; the argument-principle
count of determinant zeros of A^(t) inside Gamma is a
continuous integer in t, hence CONSTANT: A_h and A_{h+1} have
the SAME zero count inside Gamma.  On truth that count is 0 --
NO Euler extension step can pull a pole into the corridor
while the sup bound holds.  Delta is s-PROPORTIONAL in this
affine family: the |s| factor is carried exactly.  The mirror
question: does the SAME mechanism FAIL (M >= 1 / contour
undrawable) on the smooth world exactly where its corridor
actually contains zeros?

CONTOUR-CHOICE HONESTY (stated up front, frozen): Gamma is the
rectangle Re s in [-delta_0, 1 + delta_1], Im s in [-b, +b],
delta_0 = 0.1, b = 0.3.  Variant A (TARGET-INFORMED): per pair
delta_1 = min over the two rungs of (s*_h - 1)/2.  This uses
the TARGET rung's pole location -- fine for the MEASUREMENT
(we ask whether the mechanism exists), but a self-contained
theorem must choose the contour from the source side.  Variant
B (FIXED): one contour for the whole ladder with delta_1^fix =
tau-law/2 -- the h-trend law log(s*_h - 1) = c0 + c1 log h
(the PRIME.PORT.SFLOW.01 S4 pole-distance law) evaluated at
the deepest ladder depth h_max, halved:
    delta_1^fix = exp(c0) * h_max^c1 / 2.
HONEST LIMIT of variant B: the law's coefficients are fitted
across the whole truth ladder, so it is source-legitimate in
FORM only (a single fixed contour, no per-target pole is
consulted); a self-contained theorem needs the margin law
itself derived from the source side (open).  Both variants are
frozen and both are reported.

THE LADDER (frozen, factor_avoidance verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive FULL-WINDOW pairs (both rungs carry all 12 indices
of J = {2, 4, ..., 24}); truth + smooth-mass world (B1
LATTICE-SMOOTH masses m_n = 2 e^{u_n/2} du_n, midpoint cells,
lattice_parametrix verbatim); Epstein/scramble frame status
reported (C1).

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 G1  THE CONTOUR: per truth full-window rung the exact pole
     s*_h = 1/lam_max(C_h) (symmetric eig; sflow identity
     (iii)); LS fit of log(s*_h - 1) vs log h over the truth
     full-window rungs -> delta_1^fix as above; per pair the
     variant-A delta_1.  Discretization (frozen, 80 points,
     denser near s = 1 + delta_1): right edge 32 points at
     Im = b*v|v|, v uniform in [-1, 1] (quadratic clustering
     toward the real axis); top and bottom edges 20 points
     each at Re = (1+delta_1) - (1+delta_1+delta_0)(1-t)^2,
     t uniform in [0, 1] (clustering toward the right corner);
     left edge 8 points uniform.

 G2  THE SUP LEDGER: per full-window step and per contour
     variant M_h = max over the 80 frozen points of
     |s| * ||(I - s C_h)^{-1} (C_{h+1} - C_h)||_2 (exact
     complex solve + spectral norm; the -s factor of Delta
     carried via |s|), plus min_Gamma sigma_min(A_h) (the
     invertibility margin of the Rouche premise).  CENSUS:
     truth M_h < 1 on all steps?  Print the full M ladder,
     its max, and WHERE the sup is attained (region tag:
     RIGHT-CAP = Re s >= 1, the honest bottleneck near the
     nearly singular cap).  If M >= 1 only with the sup at
     the RIGHT-CAP, the contour choice is the issue:
     CONTOUR-LIMITED (typed per variant).  On the smooth
     world, variant A is UNDRAWABLE on a pair whose corridor
     is already broken (min s* <= 1 gives delta_1 <= 0: no
     rectangle of this family encloses [0, 1] without
     swallowing the real pole) -- typed POLE-IN-CORRIDOR,
     itself a detection.

 G3  THE ZERO-COUNT VERIFICATION (5 frozen steps = the middle
     five of the truth step list sorted by h, the
     factor_avoidance MEDIUM_N rule; both variants): count
     determinant zeros of A_h and A_{h+1} inside Gamma by the
     argument principle, N = (1/2 pi i) closed-int of
     d/ds log det A = -tr[A(s)^{-1} C] (the sflow variational
     identity continued to complex s; trace route), integrated
     by composite 16-point Gauss-Legendre with geometric panel
     grading toward the pole-nearest contour point.  WARDS
     (kill KW): (i) trace vs spectral integrand agreement at
     3 frozen contour nodes, rel <= 1e-9; (ii) |N - nearest
     integer| <= 1e-6; (iii) the integer equals the EXACT
     eigenvalue census #{i: 1/lam_i(C) inside Gamma}; (iv)
     the pair counts are EQUAL whenever M_h < 1 (the Rouche
     conclusion).  A pole within 1e-9 of the contour edge is
     typed BOUNDARY-POLE and exempted from (ii)-(iv) (honesty
     guard; census printed).  REPORT-ONLY extra: the same
     integral on the smooth world's first corridor-broken
     step (variant B) -- the count must show the zeros.

 G4  THE SMOOTH WORLD: same G2 ledgers per variant, plus per
     rung the exact zero census inside Gamma_B and the
     corridor-broken flag (min(s*_a, s*_b) <= 1).  CENSUSES:
     (i) where is M >= 1; (ii) where does the corridor
     actually contain zeros; (iii) the 2x2 of zero-count
     CHANGE across the step (census_a != census_b) vs M >= 1
     -- count change with M < 1 would CONTRADICT the theorem
     (ward-grade, printed; the contrapositive direction).
     DETECTION (frozen): a corridor-broken smooth step is
     DETECTED under variant A iff POLE-IN-CORRIDOR or M >= 1;
     under variant B iff M >= 1 or a nonzero census inside
     Gamma_B on either rung.  ROUCHE-DISCRIMINATES iff truth
     all-passes under at least one variant AND under that same
     variant every corridor-broken smooth step is detected AND
     every zero-count-change step has M >= 1.

 G5  TYPED (frozen): per variant ROUCHE-HOLDS(variant) iff
     truth M < 1 on ALL steps; CONTOUR-LIMITED(variant) iff
     violations exist but EVERY violating step attains its sup
     at the RIGHT-CAP (Re s >= 1); ROUCHE-FAILS(variant)
     otherwise.  Plus ROUCHE-DISCRIMINATES /
     ROUCHE-NONDISCRIMINATING per G4, and the honest analysis
     of which contour variant is source-legitimate (variant A
     is not; variant B in form only, see above).

 C   CONTROLS: the SMOOTH-MASS world is the PRIMARY embedded
     control -- it must have at least one corridor-broken step
     (kill KC -> CONTROL-DEAD); Epstein/scramble (kz 9) frame
     status REPORTED (frame death / exterior supercritical /
     window supercritical; report-only per this contract).

 W   PIPELINE + REPRODUCTION WARDS: W1 truth full-window rung
     census == 37 (sflow P0.1; kill KP -> PIPELINE-BROKEN);
     W2 truth consecutive full-window pairs == 31 and W3
     smooth pairs == 28 (factor_avoidance printed ledger; kill
     KW); W4 truth s*_h > 1 on every full-window rung (sflow
     S3/S4 CORRIDOR-CLEAR + pole table; kill KW).

KILLS: KP pipeline -> PIPELINE-BROKEN; KW wards (reproduction /
integrand / integer / census / pair-equality) -> WARD-BROKEN;
KC smooth control silent -> CONTROL-DEAD.

VERDICT (frozen enum): ROUCHE-MEASURED (+ typed sublabels per
variant ROUCHE-HOLDS(variant) / CONTOUR-LIMITED /
ROUCHE-FAILS, plus ROUCHE-DISCRIMINATES /
ROUCHE-NONDISCRIMINATING) / PIPELINE-BROKEN / WARD-BROKEN /
CONTROL-DEAD.

HONEST FRAME: M < 1 on a finite ladder is a MEASUREMENT of the
mechanism's existence, not a theorem -- the bound must be
DERIVED (and the variant-B margin law derived from the source
side) before anything is claimed; the zero-count identity and
the pole census are exact algebra whose wards protect the
bookkeeping only.  NO RH claim.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- the
frozen 80-point grid, all bars, and every run-1 number stand
unchanged; v2 only ADDS reports and STRENGTHENS one typing
condition, it rescues nothing):

 (i)   GRID HONESTY AT THE CAP: the frozen right edge samples
       Im = b*v|v| with 32 EVEN-count points, so no grid point
       lies exactly on the real axis (nearest |Im s| = b/31^2
       ~ 3.1e-4).  With truth margins s* - 1 ~ 1e-7..1e-4 the
       printed M is therefore a LOWER bound of the continuum
       sup (run 1: min_Gamma sigma_min(A) ~ 3.1e-4 was set by
       the grid, not by the pole).  v2 adds the EXACT cap-point
       report M_cap = |s| ||A^{-1} Delta(s)|| at s = 1 +
       delta_1 + 0i (the sup lower bound at the nearest
       contour point to the pole) per step and variant.

 (ii)  CONTOUR-LIMITED STRENGTHENED: run 1 typed
       CONTOUR-LIMITED from the sup LOCATION only.  v2
       additionally requires the OFF-CAP sup (the max of the
       same ledger restricted to the frozen grid points with
       Re s < 1) to be < 1 on EVERY truth step of that
       variant; otherwise ROUCHE-FAILS.  This is a stricter
       bar, applied to the same run-1 grid values.

 (iii) OFF-CAP DIAGNOSTIC CENSUS (report-only, both worlds):
       M_off per step and variant.  HONEST LIMIT stated: an
       off-cap bound gives NO Rouche conclusion (the premise
       needs the whole contour); this census only locates
       where the mechanism is starved.

 (iv)  GAMMA_B CORRIDOR CENSUS ON ALL TRUTH RUNGS (exact
       algebra, report + ward-grade print): d1_fix = 8.07e-8
       sits BELOW the smallest measured truth margin (1.42e-7)
       by a factor of only ~1.8 -- v2 prints the exact zero
       census inside Gamma_B for every truth full-window rung
       (must be 0 throughout for the variant-B corridor to be
       meaningful) and the margin/d1_fix ratio.

Sources (read-only): v563_paper2_readouts (build_window /
atom_lags_at / arch_lags / frame_a_zones, verbatim);
factor_avoidance_euler_probe.py (ladder + 12-window pipeline +
smooth-mass world, VERBATIM; pair censuses = reproduction
anchor); port_sflow_toda_probe.py (pole identity s* =
1/lam_max, variational identity d/ds log det = -tr[A^{-1}C],
S4 h-trend law = the variant-B seed).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/euler_rouche_probe.py
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
NW = 12
MIN_COMMON_J = 8

# contour (frozen)
D0 = 0.1                    # delta_0, left margin
B_IM = 0.3                  # +/- imaginary half-height
N_RIGHT, N_TOP, N_BOT, N_LEFT = 32, 20, 20, 8   # 80 points
RIGHT_CAP_RE = 1.0          # sup-location region tag bar

# argument principle (frozen)
GL_N = 16                   # Gauss-Legendre nodes per panel
K_MAX = 45                  # geometric grading depth cap
G3_N = 5                    # medium-5 rule (factor_avoidance)
INT_WARD = 1e-6             # integer ward
SPEC_WARD = 1e-9            # trace-vs-spectral integrand ward
EDGE_GUARD = 1e-9           # BOUNDARY-POLE exemption distance

# reproduction anchors (predecessor printed ledgers)
REF_N_FULLWIN = 37          # sflow P0.1
REF_N_TRUTH_PAIRS = 31      # factor_avoidance A0.2
REF_N_SMOOTH_PAIRS = 28     # factor_avoidance A0.3

CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
AMENDMENTS = []
T0 = time.time()

GLX, GLW = np.polynomial.legendre.leggauss(GL_N)


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


# --------- pipeline, VERBATIM from factor_avoidance_euler_probe
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
    """One rung -> 12x12 window compression (factor_avoidance
    rung_win VERBATIM)."""
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


# ------------------------------------- contour + Rouche machinery
def s_star_of(C):
    """Exact first positive determinant zero of I - sC (sflow
    identity (iii)): s* = 1/lam_max, inf if lam_max <= 0."""
    lam_mx = float(np.max(np.linalg.eigvalsh(C)))
    return ((1.0 / lam_mx) if lam_mx > 0.0 else float("inf")),\
        lam_mx


def gamma_points(d1):
    """Frozen 80-point discretization of the rectangle boundary,
    denser near s = 1 + d1 (G1)."""
    x_r = 1.0 + d1
    pts = []
    v = np.linspace(-1.0, 1.0, N_RIGHT)
    pts += [complex(x_r, B_IM * vv * abs(vv)) for vv in v]
    t = np.linspace(0.0, 1.0, N_TOP)
    xs = x_r - (x_r + D0) * (1.0 - t) ** 2
    pts += [complex(x, B_IM) for x in xs]
    pts += [complex(x, -B_IM) for x in xs]
    for yy in np.linspace(-B_IM, B_IM, N_LEFT):
        pts.append(complex(-D0, yy))
    return np.asarray(pts, complex)


def region_tag(s):
    if s.real >= RIGHT_CAP_RE:
        return "RIGHT-CAP"
    if abs(s.real + D0) <= 1e-12:
        return "LEFT-EDGE"
    return "TOP/BOT"


def sup_ledger(Ca, Dmat, pts):
    """M = sup_Gamma ||A^{-1} Delta(s)||_2 with Delta(s) = -s D;
    plus the invertibility margin min_Gamma sigma_min(A) and the
    OFF-CAP sup restricted to Re s < 1 (SPEC v2 (ii)/(iii))."""
    Iw = np.eye(NW)
    M, s_at = -1.0, None
    Moff, s_off = -1.0, None
    smin, s_sm = float("inf"), None
    for s in pts:
        A = Iw - s * Ca
        sv = np.linalg.svd(A, compute_uv=False)
        if sv[-1] < smin:
            smin, s_sm = float(sv[-1]), s
        m = abs(s) * float(np.linalg.norm(
            np.linalg.solve(A, Dmat), 2))
        if m > M:
            M, s_at = m, s
        if s.real < RIGHT_CAP_RE and m > Moff:
            Moff, s_off = m, s
    return M, s_at, smin, s_sm, Moff, s_off


def cap_point(Ca, Dmat, d1):
    """EXACT cap-point value at s = 1 + d1 + 0i (SPEC v2 (i)):
    the nearest contour point to the real pole; a lower bound
    of the continuum sup."""
    s = 1.0 + d1
    A = np.eye(NW) - s * Ca
    sv = np.linalg.svd(A, compute_uv=False)
    return (s * float(np.linalg.norm(np.linalg.solve(A, Dmat),
                                     2)), float(sv[-1]))


def real_poles(C):
    ev = np.linalg.eigvalsh(C)
    return [1.0 / float(v) for v in ev if abs(v) > 1e-14]


def census_inside(C, d1):
    """EXACT zero census of det(I - sC) inside Gamma(d1) plus the
    minimal pole distance to the vertical edges."""
    x_r = 1.0 + d1
    n = 0
    dmin = float("inf")
    for p in real_poles(C):
        dmin = min(dmin, abs(p - x_r), abs(p + D0))
        if -D0 < p < x_r:
            n += 1
    return n, dmin


def _ell_trace(zs, C):
    """d/ds log det(I - sC) = -tr[(I - sC)^{-1} C] (sflow
    variational identity, complex s; trace route)."""
    Iw = np.eye(NW)
    out = np.empty(len(zs), complex)
    for i, z in enumerate(zs):
        out[i] = -np.trace(np.linalg.solve(Iw - z * C, C))
    return out


def _ell_spectral(zs, C):
    ev = np.linalg.eigvalsh(C)[:, None]
    return np.sum(-ev / (1.0 - zs[None, :] * ev), axis=0)


def _seg_dist(p, z0, z1):
    dz = z1 - z0
    t = ((p - z0) * dz.conjugate()).real / abs(dz) ** 2
    t = min(1.0, max(0.0, t))
    return abs(p - (z0 + t * dz))


def _graded_panels(z0, z1, poles, toward):
    """Geometric panel grading toward the pole-nearest end of the
    segment ('end'/'start'); uniform 4 panels if toward is None."""
    L = abs(z1 - z0)
    if toward is None:
        us = np.linspace(0.0, 1.0, 5)
    else:
        d = max(min((_seg_dist(p, z0, z1) for p in poles),
                    default=L), 1e-9)
        K = int(min(K_MAX, max(4, math.ceil(
            math.log2(max(L / d, 2.0))))))
        us = np.concatenate(
            ([0.0], 1.0 - 2.0 ** -np.arange(1, K + 1), [1.0]))
        if toward == "start":
            us = 1.0 - us[::-1]
    return [(z0 + (z1 - z0) * a, z0 + (z1 - z0) * b)
            for a, b in zip(us[:-1], us[1:])]


def count_zeros_numeric(C, d1):
    """Argument-principle zero count of det(I - sC) inside
    Gamma(d1): composite Gauss-Legendre on the graded rectangle
    boundary, counterclockwise."""
    x_r = 1.0 + d1
    poles = real_poles(C)
    bl = complex(-D0, -B_IM)
    br = complex(x_r, -B_IM)
    tr = complex(x_r, B_IM)
    tl = complex(-D0, B_IM)
    rc = complex(x_r, 0.0)
    sides = ((bl, br, "end"),      # bottom, pole-nearest right
             (br, rc, "end"),      # right lower half -> center
             (rc, tr, "start"),    # right upper half <- center
             (tr, tl, "start"),    # top, pole-nearest right
             (tl, bl, None))       # left, far from all poles
    tot = 0.0 + 0.0j
    for z0, z1, toward in sides:
        for a, b in _graded_panels(z0, z1, poles, toward):
            mid = 0.5 * (a + b)
            half = 0.5 * (b - a)
            tot += half * np.sum(GLW * _ell_trace(
                mid + half * GLX, C))
    return tot / (2.0j * math.pi)


def fmt_s(s):
    return "%.4f%+.4fi" % (s.real, s.imag)


def main():
    section("PRIME.PORT.EULER.ROUCHE.01 -- matrix-Rouche corridor "
            "inheritance: sup_Gamma ||A_h^{-1} Delta_h|| < 1 "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ P0
    section("P0 -- build the truth + smooth-mass ladders (all "
            "frame-A zones, h <= %d; pipeline VERBATIM)"
            % H_DEEP_MAX)
    rungs, srungs = [], []
    n_smooth_dead = 0
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        r = rung_win(kz, rr_cache=rr)
        if not isinstance(r, dict):
            continue
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
    full_t = [r for r in rungs if r.get("full")]
    print("    truth: %d rungs (%d full-window), h %d .. %d | "
          "smooth: %d rungs, %d chain/window deaths"
          % (len(rungs), len(full_t), rungs[0]["h"],
             rungs[-1]["h"], len(srungs), n_smooth_dead))
    check("W1 truth full-window rung census %d == %d (sflow "
          "P0.1 anchor)" % (len(full_t), REF_N_FULLWIN),
          len(full_t) == REF_N_FULLWIN, kill="KP")

    def make_pairs(rr_list):
        rows = []
        for ra, rb in zip(rr_list[:-1], rr_list[1:]):
            if not (ra.get("full") and rb.get("full")):
                continue
            Ca, Cb = ra["CJ"], rb["CJ"]
            ssa, _ = s_star_of(Ca)
            ssb, _ = s_star_of(Cb)
            rows.append(dict(ha=ra["h"], hb=rb["h"],
                             kza=ra["kz"], kzb=rb["kz"],
                             Ca=Ca, Cb=Cb, D=Cb - Ca,
                             ssa=ssa, ssb=ssb))
        return rows

    tpairs = make_pairs(rungs)
    spairs = make_pairs(srungs)
    check("W2 truth consecutive full-window pairs %d == %d "
          "(factor_avoidance anchor)"
          % (len(tpairs), REF_N_TRUTH_PAIRS),
          len(tpairs) == REF_N_TRUTH_PAIRS, kill="KW")
    check("W3 smooth pairs %d == %d (factor_avoidance anchor)"
          % (len(spairs), REF_N_SMOOTH_PAIRS),
          len(spairs) == REF_N_SMOOTH_PAIRS, kill="KW")
    if KILLS:
        return finish("n/a")

    # ------------------------------------------------------------ G1
    section("G1 -- THE CONTOUR: rectangle Re s in [-%.1f, 1 + "
            "delta_1], Im s in [-%.1f, +%.1f]; variant A "
            "(target-informed) vs variant B (fixed, tau-law/2)"
            % (D0, B_IM, B_IM))
    hs, margins = [], []
    n_out = 0
    for r in full_t:
        ss, _ = s_star_of(r["CJ"])
        if ss > 1.0:
            n_out += 1
            if math.isfinite(ss):
                hs.append(float(r["h"]))
                margins.append(ss - 1.0)
    check("W4 truth pole outside the corridor (s* > 1) on "
          "%d/%d full-window rungs (sflow S3/S4 anchor)"
          % (n_out, len(full_t)), n_out == len(full_t),
          kill="KW")
    if KILLS:
        return finish("n/a")
    c1, c0 = np.polyfit(np.log(hs), np.log(margins), 1)
    h_max = max(hs)
    d1_fix = 0.5 * math.exp(c0) * h_max ** c1
    mq = np.percentile(margins, [0, 25, 50, 75, 100])
    print("    truth margins s* - 1: min %.4e  q25 %.4e  med "
          "%.4e  q75 %.4e  max %.4e" % tuple(mq))
    print("    h-trend law (sflow S4 seed): log(s* - 1) = "
          "%+.4f %+.4f log h  -> predicted margin at h_max = "
          "%d: %.4e" % (c0, c1, int(h_max),
                        math.exp(c0) * h_max ** c1))
    print("    variant B FIXED delta_1^fix = tau-law/2 = %.6e "
          "(one contour for the whole ladder)" % d1_fix)
    print("    variant A per pair: delta_1 = min(s*_h, "
          "s*_{h+1} - 1)/2 -- TARGET-INFORMED (honest note: "
          "fine for the")
    print("    measurement, NOT source-legitimate for a "
          "theorem; variant B is source-legitimate in FORM "
          "only, its law is")
    print("    fitted across the ladder -- the margin law "
          "itself must be derived for a self-contained "
          "statement).")
    gammaB = gamma_points(d1_fix)
    # SPEC v2 (iv): Gamma_B corridor census on ALL truth rungs
    nz_B = 0
    for r in full_t:
        nz_B += census_inside(r["CJ"], d1_fix)[0]
    ratio = min(margins) / d1_fix
    print("    v2 (iv) Gamma_B truth census: %d determinant "
          "zeros inside Gamma_B over all %d truth rungs "
          "(min margin / delta_1^fix = %.2f)"
          % (nz_B, len(full_t), ratio))
    check("G1.v2 Gamma_B encloses a zero-free truth corridor "
          "(0 zeros on all %d rungs)" % len(full_t), nz_B == 0)
    AMENDMENTS.append("v2(i) exact cap-point report added "
                      "(even-count right edge has no real-axis "
                      "sample; grid M is a lower bound)")
    AMENDMENTS.append("v2(ii) CONTOUR-LIMITED strengthened: "
                      "off-cap sup < 1 required on all steps")
    AMENDMENTS.append("v2(iii) off-cap diagnostic census, both "
                      "worlds (report-only, no Rouche "
                      "conclusion)")
    AMENDMENTS.append("v2(iv) Gamma_B truth corridor census on "
                      "all rungs")

    # ------------------------------------------------------------ G2
    section("G2 -- THE SUP LEDGER, truth (%d steps): M = "
            "sup_Gamma |s| ||(I - s C_h)^{-1} (C_{h+1} - "
            "C_h)||_2, both variants" % len(tpairs))

    TAG_SHORT = {"RIGHT-CAP": "RC", "TOP/BOT": "TB",
                 "LEFT-EDGE": "LE"}

    def measure(row):
        d1A = 0.5 * (min(row["ssa"], row["ssb"]) - 1.0)
        if d1A > 0.0 and math.isfinite(d1A):
            MA, sA, smA, _, MoA, _ = sup_ledger(
                row["Ca"], row["D"], gamma_points(d1A))
            McA, _ = cap_point(row["Ca"], row["D"], d1A)
        else:
            MA, sA, smA, MoA, McA = (None,) * 5  # POLE-IN-CORRIDOR
        MB, sB, smB, _, MoB, _ = sup_ledger(row["Ca"], row["D"],
                                            gammaB)
        McB, _ = cap_point(row["Ca"], row["D"], d1_fix)
        row.update(d1A=d1A, MA=MA, sA=sA, smA=smA, MoA=MoA,
                   McA=McA, MB=MB, sB=sB, smB=smB, MoB=MoB,
                   McB=McB)

    print("    (M = grid sup, LOWER bound of the continuum sup; "
          "Moff = sup over Re s < 1; Mcap = exact value at s = "
          "1 + delta_1, v2)")
    print("    step        delta1(A)  M_A       Moff_A   "
          "Mcap_A     M_B       Moff_B   Mcap_B     sup A/B")
    for row in tpairs:
        measure(row)
        print("    h %3d->%3d  %.4e %9.4f  %7.4f  %.3e  "
              "%9.4f  %7.4f  %.3e  %s/%s"
              % (row["ha"], row["hb"], row["d1A"], row["MA"],
                 row["MoA"], row["McA"], row["MB"], row["MoB"],
                 row["McB"], TAG_SHORT[region_tag(row["sA"])],
                 TAG_SHORT[region_tag(row["sB"])]))
    violA = [r for r in tpairs if r["MA"] >= 1.0]
    violB = [r for r in tpairs if r["MB"] >= 1.0]
    MAmax = max(r["MA"] for r in tpairs)
    MBmax = max(r["MB"] for r in tpairs)
    MoAmax = max(r["MoA"] for r in tpairs)
    MoBmax = max(r["MoB"] for r in tpairs)
    smin_grid = min(r["smA"] for r in tpairs)
    print("\n    TRUTH CENSUS: variant A M < 1 on %d/%d (max M "
          "%.4f) | variant B M < 1 on %d/%d (max M %.4f)"
          % (len(tpairs) - len(violA), len(tpairs), MAmax,
             len(tpairs) - len(violB), len(tpairs), MBmax))
    print("    OFF-CAP (v2): max Moff_A = %.4f, max Moff_B = "
          "%.4f over all truth steps (< 1 on %d/%d and %d/%d)"
          % (MoAmax, MoBmax,
             sum(1 for r in tpairs if r["MoA"] < 1.0),
             len(tpairs),
             sum(1 for r in tpairs if r["MoB"] < 1.0),
             len(tpairs)))
    print("    CAP HONESTY (v2): grid min sigma_min(A) = %.2e "
          "is set by the nearest-to-axis grid point (|Im s| = "
          "b/31^2 = %.1e)," % (smin_grid, B_IM / 31.0 ** 2))
    print("    not by the pole; the exact cap values Mcap "
          "(range %.2e .. %.2e for A) show the continuum sup "
          "-- the M ledger is a lower bound."
          % (min(r["McA"] for r in tpairs),
             max(r["McA"] for r in tpairs)))
    for nm, viol in (("A", violA), ("B", violB)):
        if viol:
            tags = [region_tag(r["sA" if nm == "A" else "sB"])
                    for r in viol]
            print("    variant %s violations (%d): first/worst "
                  "%s; sup regions %s"
                  % (nm, len(viol),
                     ["h%d->%d M=%.3f" % (r["ha"], r["hb"],
                      r["MA" if nm == "A" else "MB"])
                      for r in (viol[0], max(
                          viol, key=lambda r:
                          r["MA" if nm == "A" else "MB"]))],
                     sorted(set(tags))))

    def variant_type(viol, skey, mkey):
        """SPEC v2 (ii): CONTOUR-LIMITED needs sup location at
        the RIGHT-CAP on every violation AND off-cap sup < 1
        on EVERY step."""
        if not viol:
            return "ROUCHE-HOLDS"
        if (all(region_tag(r[skey]) == "RIGHT-CAP"
                for r in viol)
                and all(r[mkey] < 1.0 for r in tpairs)):
            return "CONTOUR-LIMITED"
        return "ROUCHE-FAILS"

    typA = variant_type(violA, "sA", "MoA")
    typB = variant_type(violB, "sB", "MoB")
    check("G2.s truth typed (v2 bars): variant A %s, variant "
          "B %s" % (typA, typB), True)

    # ------------------------------------------------------------ G3
    section("G3 -- ZERO-COUNT VERIFICATION (argument principle, "
            "%d frozen medium steps, both variants): N = "
            "(1/2pi i) closed-int -tr[A^{-1}C] ds" % G3_N)
    i0 = (len(tpairs) - G3_N) // 2
    g3 = tpairs[i0:i0 + G3_N]
    print("    frozen steps (medium-5 rule): %s"
          % ["h%d->%d" % (r["ha"], r["hb"]) for r in g3])
    w_spec = 0.0
    w_int = 0.0
    ok_census = True
    ok_equal = True
    n_bpole = 0
    print("\n    step        var  rung  N_num (re, |im|)      "
          "int-err   N_exact  pair-equal (M<1)")
    for row in g3:
        for vn, d1, M in (("A", row["d1A"], row["MA"]),
                          ("B", d1_fix, row["MB"])):
            nints = []
            for side_nm, C in (("h  ", row["Ca"]),
                               ("h+1", row["Cb"])):
                Nnum = count_zeros_numeric(C, d1)
                nint = int(round(Nnum.real))
                err = abs(Nnum - nint)
                nex, dmin = census_inside(C, d1)
                if dmin < EDGE_GUARD:
                    n_bpole += 1
                    print("    h %3d->%3d  %s   %s   "
                          "BOUNDARY-POLE (pole within %.0e of "
                          "the edge; census %d) -- ward exempt"
                          % (row["ha"], row["hb"], vn, side_nm,
                             EDGE_GUARD, nex))
                    continue
                w_int = max(w_int, err)
                ok_census &= (nint == nex)
                nints.append(nint)
                print("    h %3d->%3d  %s   %s   %+9.6f  %.1e   "
                      "%.1e   %d        %s"
                      % (row["ha"], row["hb"], vn, side_nm,
                         Nnum.real, abs(Nnum.imag), err, nex,
                         "-"))
            if len(nints) == 2 and M < 1.0:
                eq = (nints[0] == nints[1])
                ok_equal &= eq
                print("      -> pair counts %d == %d under M = "
                      "%.4f < 1: %s" % (nints[0], nints[1], M,
                                        eq))
            # integrand ward at 3 frozen nodes (rung h)
            zs = gamma_points(d1)[[0, 40, 79]]
            lt = _ell_trace(zs, row["Ca"])
            lsp = _ell_spectral(zs, row["Ca"])
            w_spec = max(w_spec, float(np.max(
                np.abs(lt - lsp)
                / np.maximum(np.abs(lt), 1e-30))))
    check("G3.W1 integrand trace vs spectral, worst rel %.1e "
          "<= %.0e" % (w_spec, SPEC_WARD), w_spec <= SPEC_WARD,
          kill="KW")
    check("G3.W2 argument-principle count integer at %.0e "
          "(worst dev %.1e; %d BOUNDARY-POLE exemptions)"
          % (INT_WARD, w_int, n_bpole), w_int <= INT_WARD,
          kill="KW")
    check("G3.W3 numeric count == exact eigenvalue census on "
          "every warded rung/variant", ok_census, kill="KW")
    check("G3.W4 Rouche conclusion verified: pair counts EQUAL "
          "whenever M < 1", ok_equal, kill="KW")

    # ------------------------------------------------------------ G4
    section("G4 -- THE SMOOTH WORLD (%d steps): same ledgers; "
            "corridor-broken census; does the mechanism DETECT "
            "the failures?" % len(spairs))
    print("    step        s*_a     s*_b     broken  variant A"
          "            M_B       sup at (B)            zeros "
          "in Gamma_B (a,b)")
    n_broken = 0
    n_MB_ge1 = 0
    det_A_all = True
    det_B_all = True
    n_change = 0
    n_change_Mlt1 = 0
    first_broken = None
    for row in spairs:
        measure(row)
        za, _ = census_inside(row["Ca"], d1_fix)
        zb, _ = census_inside(row["Cb"], d1_fix)
        row.update(za=za, zb=zb)
        broken = min(row["ssa"], row["ssb"]) <= 1.0
        row["broken"] = broken
        if broken:
            n_broken += 1
            if first_broken is None:
                first_broken = row
        if row["MB"] >= 1.0:
            n_MB_ge1 += 1
        if za != zb:
            n_change += 1
            if row["MB"] < 1.0:
                n_change_Mlt1 += 1
        pic = row["MA"] is None
        a_str = ("POLE-IN-CORRIDOR    " if pic
                 else "M_A %8.4f %-7s"
                 % (row["MA"], region_tag(row["sA"])))
        if broken:
            det_A = pic or (row["MA"] is not None
                            and row["MA"] >= 1.0)
            det_B = (row["MB"] >= 1.0) or (za + zb > 0)
            det_A_all &= det_A
            det_B_all &= det_B
        print("    h %3d->%3d  %7.4f  %7.4f  %-5s   %s %9.4f  "
              "%s %-9s %d,%d"
              % (row["ha"], row["hb"],
                 min(row["ssa"], 99.0), min(row["ssb"], 99.0),
                 str(broken), a_str, row["MB"],
                 fmt_s(row["sB"]), region_tag(row["sB"]),
                 za, zb))
    n_picA = sum(1 for r in spairs if r["MA"] is None)
    print("\n    SMOOTH CENSUS: corridor-broken on %d/%d steps; "
          "variant A undrawable (POLE-IN-CORRIDOR) on %d; "
          "M_B >= 1 on %d" % (n_broken, len(spairs), n_picA,
                              n_MB_ge1))
    n_off_s = sum(1 for r in spairs if r["MoB"] >= 1.0)
    print("    OFF-CAP DIAGNOSTIC (v2, report-only -- no "
          "Rouche conclusion off a full contour): smooth "
          "Moff_B >= 1 on %d/%d steps (max %.3f); truth had "
          "max Moff = %.4f/%.4f (A/B)"
          % (n_off_s, len(spairs),
             max(r["MoB"] for r in spairs), MoAmax, MoBmax))
    print("    zero-count CHANGE across the step on %d steps; "
          "change with M_B < 1 (would contradict the theorem): "
          "%d" % (n_change, n_change_Mlt1))
    check("G4.W theorem contrapositive on smooth: every "
          "zero-count change has M_B >= 1 (%d/%d)"
          % (n_change - n_change_Mlt1, n_change),
          n_change_Mlt1 == 0, kill="KW")
    if first_broken is not None:
        row = first_broken
        print("\n    REPORT-ONLY: argument-principle integral "
              "on the smooth FIRST broken step h %d->%d "
              "(variant B):" % (row["ha"], row["hb"]))
        for side_nm, C, zx in (("h  ", row["Ca"], row["za"]),
                               ("h+1", row["Cb"], row["zb"])):
            Nn = count_zeros_numeric(C, d1_fix)
            print("      rung %s: N_num = %+9.6f%+9.2ei "
                  "(exact census %d)"
                  % (side_nm, Nn.real, Nn.imag, zx))
    truth_pass = {"A": not violA, "B": not violB}
    disc = None
    for vn in ("A", "B"):
        if not truth_pass[vn]:
            continue
        if vn == "A" and det_A_all and n_broken > 0:
            disc = "A"
            break
        if vn == "B" and det_B_all and n_broken > 0 \
                and n_change_Mlt1 == 0:
            disc = "B"
            break
    sub_disc = ("ROUCHE-DISCRIMINATES(variant %s)" % disc
                if disc else "ROUCHE-NONDISCRIMINATING")
    check("G4.s discrimination typed: %s (truth all-pass A=%s "
          "B=%s; smooth broken steps detected A=%s B=%s)"
          % (sub_disc, truth_pass["A"], truth_pass["B"],
             det_A_all, det_B_all), True)

    # ------------------------------------------------------------ G5
    section("G5 -- TYPED OUTCOME + the contour-legitimacy "
            "analysis")
    print("    variant A (target-informed): %s | variant B "
          "(fixed, tau-law/2): %s | %s"
          % (typA, typB, sub_disc))
    print("""
    HONEST ANALYSIS (frozen frame): variant A consults the
    TARGET rung's pole to place the right edge -- it can only
    ever certify what the target already reveals; it measures
    whether the Rouche MECHANISM exists, nothing more.
    Variant B is a single fixed contour (no per-target pole is
    consulted), so the Rouche step is source-legitimate GIVEN
    the contour -- but its delta_1^fix is calibrated by the
    ladder-wide h-trend law, which itself is fitted on target
    data.  A self-contained inheritance theorem therefore
    needs (i) the margin law derived (not fitted), and (ii)
    the sup bound M < 1 derived from the increment structure.
    Both remain open; this probe only measures whether the
    bound is TRUE on the deployed ladder.""")

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C2 -- smooth-mass world (PRIMARY): corridor-broken "
          "on %d/%d steps." % (n_broken, len(spairs)))
    check("C2 smooth control fires (>= 1 corridor-broken step)",
          n_broken > 0, kill="KC")
    print("  C1 -- Epstein/scramble frame status (kz %d, "
          "report-only per contract):" % CTRL_KZ)
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = rung_win(CTRL_KZ, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
        elif "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES"
                  % nmc)
        else:
            ssc, lamc = s_star_of(rc["CJ"])
            print("    %-8s: lam(out) %.3e | lam(C_J) %.3e | "
                  "pole s* = %.4f -> %s"
                  % (nmc, rc["lamO"], rc["lamC"], ssc,
                     "EXTERIOR supercritical"
                     if rc["lamO"] > 1.0 else
                     "WINDOW supercritical / pole inside"
                     if rc["lamC"] > 1.0 or ssc <= 1.0
                     else "silent (reported)"))

    typed = ("A: %s, B: %s, %s" % (typA, typB, sub_disc))
    return finish(typed)


def finish(typed):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN", "KW": "WARD-BROKEN",
                   "KC": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = "ROUCHE-MEASURED"
        print("\n  VERDICT: %s (%s)" % (VERDICT, typed))
    print("\n  SPEC v2 amendments (fail-first preserved): %s"
          % ("; ".join(AMENDMENTS) if AMENDMENTS else "none"))
    print("""
  HONEST FRAME (as frozen): the Rouche step, the zero-count
  identity and the pole census are exact algebra -- the wards
  protect the bookkeeping.  The measured content is (a)
  whether ONE contour sup bound M < 1 holds on every truth
  step (then no Euler extension step can pull a pole into the
  corridor, per step, on this finite ladder), (b) whether the
  same mechanism fails on the smooth world exactly where its
  corridor breaks, and (c) the honest fact that neither
  contour variant is yet source-derived.  NO RH claim.  No
  marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source deepcore_schur_reduction_probe (embedded BYTE-EXACT, raw string)
_SRC_3 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deepcore_schur_reduction_probe -- PRIME.PORT.DEEPCORE.SCHUR.01
(EXPLORATION ONLY, experiments/; round 51, reviewer priority 4:
does the fixed 8-node deep core + a uniform outside margin reduce
the whole wall to a FIXED 8x8 Schur family S_h > 0?, 2026-08-09).

THE QUESTION (frozen): round 50 (deepcore_anatomy_probe,
PRIME.PORT.DEEPCORE.01) identified the arithmetic remnant as the
FIXED even alias set {2, 4, ..., 16} on the folded neg grid -- the
port core at the Bessel-normal coordinates a_m = pi^2 m^2, m =
1..8.  If the wall operator, split along that fixed core, has a
UNIFORMLY positive-definite outside block, then by the Schur
complement / Haynsworth reduction the entire cofinal wall demand
collapses to the positivity of ONE fixed 8x8 matrix family S_h --
the RH wand as a fixed-dimension statement.  This probe measures
the two ingredients honestly on the full ladder.

THE WALL OPERATOR (frozen choice, stated per the contract): the
FULL wall operator is used -- A_h = I - E_h with E_h the plain
Carleson Gram on ALL folded neg nodes (port_schur_reduction round-
38 v2 object, gauge-equivalent to the embedding E; lam_max(E_h) =
1 - tau_h, the wall <=> A_h >= 0).  The full operator is feasible
(the folded neg grid carries O(h) <= ~1800 nodes; dense
eigensolves are cheap), so the deployed port+bulk two-stage
structure of port_schur_reduction is NOT needed and NOT used --
one split, along the deep core, of the whole operator.

THE BLOCK SPLIT (frozen): A_h = [[B_h, X_h], [X_h^T, R_h]] with
B_h = the 8x8 block at the grid indices of the fixed core aliases
CORE_J = {2, 4, 6, 8, 10, 12, 14, 16} (folded index j on the neg
grid), R_h = everything else, X_h the coupling.  S_h = B_h - X_h
R_h^{-1} X_h^T is the 8x8 Schur core.

DIAGONAL-VS-OPERATOR MARGIN HONESTY NOTE (frozen into the
protocol): christoffel_zone_envelope_probe froze theta* = 0.700
with a deep-half OUTSIDE testing margin +0.0214 -- but that number
is an envelope of the DIAGONAL testing quotients T_m = nu~_m
K_h(y_m, y_m), NOT an operator lower bound for the block R_h.  The
operator margin lambda_min(R_h) is a different (and by eigenvalue
interlacing possibly far smaller) quantity: interlacing only
guarantees lambda_min(R_h) >= tau_h.  The reviewer's hope R_h >=
0.0214 I is therefore measured FRESH here and compared honestly;
the diagonal 0.0214 is printed as a REFERENCE ONLY, never as a
bound.

THE LADDER (frozen, christoffel_zone_envelope verbatim):
core.frame_a_zones() restricted to h <= 900 via the closed M_k
formula -- the 42 reachable rungs, sorted by (h, kz); consecutive
pairs (k = 1) for the inheritance ladder.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before the first
run; all bars frozen before the run):

 B1  THE OUTSIDE BLOCK: per rung lambda_min(R_h) (full ladder
     printed) with the ratio lambda_min(R_h)/tau_h and the
     diagonal reference DIAG_REF = 0.0214.  Log-log slope of
     lambda_min(R_h) vs h over the ladder.  TYPED:
     OPERATOR-MARGIN-UNIFORM(r0) iff min_h lambda_min(R_h) >=
     R_UNIF_BAR = 1e-3 AND slope >= SLOPE_TOL = -0.10 (candidate
     uniform floor r0 = the measured min); else
     OPERATOR-MARGIN-SHRINKS(slope) with the trend printed.

 B2  THE SCHUR CORE: S_h = B_h - X_h R_h^{-1} X_h^T (8x8) on
     every full-core rung.  WARDS (Haynsworth inertia
     bookkeeping): the integer identity neg(A_h) = neg(R_h) +
     neg(S_h) on every evaluable rung (truth, smooth AND both
     controls; rungs with min |eig(R_h)| < R_SING_TOL_REL x
     max |eig(R_h)| are typed SINGULAR-SKIP for the identity --
     the inertia formula needs R nonsingular, and the guard is
     relative because the controls carry eigenvalues of order
     10^3); on truth additionally all
     three PSD (A_h PD <=> R_h PD and S_h PD).  THE WALL IN 8x8:
     lambda_min(S_h) ladder, the ratio lambda_min(S_h)/tau_h, and
     the Pearson correlation of log lambda_min(S_h) vs log tau_h
     across the ladder.  (Anatomy, report only: the soft-mode
     core mass w_core = ||v_top(E_h)|_core||^2; the exact
     asymptotic expectation is lambda_min(S_h) ~ tau_h / w_core
     as tau -> 0, printed as the product check
     lambda_min(S_h) * w_core / tau_h.)  TYPED:
     SCHUR-TAU-TIED(corr, med ratio) iff corr >= TIED_CORR =
     0.99; else SCHUR-TAU-LOOSE(corr).

 B3  THE CORE INHERITANCE (fixed dimension): per consecutive
     full-core pair with S_h PD, H_core = S_h^{-1/2} (S_{h+1} -
     S_h) S_h^{-1/2} and eta_core = 1 + lambda_min(H_core) =
     lambda_min(S_h^{-1/2} S_{h+1} S_h^{-1/2}) (> 0 <=> S_{h+1}
     PD given S_h PD -- the inheritance margin in relative form).
     Ladder printed; census of crossings (eta_core <= 0).  TYPED
     (truth): CORE-INHERITS iff zero crossings, else
     CORE-CROSSES(n).  THE SMOOTH WORLD (masses 2 e^{u/2} du on
     the true lattice, lattice_parametrix B1 / deepcore_anatomy
     verbatim): same census; steps whose base S_h is not PD (or
     whose rung already has neg(A) > 0) are counted separately as
     rung-level failures n_hard.  TYPED:
     CORE-SEES-SMOOTH(n_cross, n_hard) iff n_cross + n_hard > 0;
     else CORE-BLIND-TO-SMOOTH (an honest finding: the smooth
     failure would then live outside the fixed core).

 B4  THE PER-PRIME GRAIN ON FIXED DIMENSION: at the 5 frozen
     heavy rungs kz GRAIN_KZ = {9, 12, 13, 26, 40}, the
     leave-one-prime-out response of S_h for the frozen primes
     GRAIN_PRIMES = {2, 3, 5, 7, 11}: the comb with ALL powers
     p^k of the one prime p removed (power identification by the
     explicit power list of the hard-coded p -- no oracle),
     D_p = S_h(without p) - S_h; plus the joint removal D_all =
     S_h(without all five) - S_h.  Report per rung: ||D_p||_F,
     the relative resolution ||D_p||_F / ||S_h||_F,
     lambda_min(S_h without p), and the ADDITIVITY DEFECT
     ||D_all - sum_p D_p||_F / ||D_all||_F.  TYPED:
     CORE-GRAIN-ACCESSIBLE(max defect) iff on ALL 5 rungs every
     response is resolved (rel >= RESOLVE_BAR = 1e-9), every
     modified world keeps the full core frame, and the additivity
     defect <= GRAIN_DEF_BAR = 0.20; else CORE-GRAIN-DEAD(reason).

 B5  THE REDUCTION STATEMENT (printed, with the measured
     numbers): IF lambda_min(R_h) >= r_0 > 0 uniformly in h
     (measured candidate r_0 = the B1 floor) THEN by Haynsworth
     the wall A_h >= 0 is EQUIVALENT to S_h >= 0 for the FIXED
     8x8 family -- the RH wand as a fixed-dimension statement.
     Its finite shadow = the B2/B3 ladders; the open pieces = the
     uniform R-margin theorem and the core inheritance.

 C   CONTROLS/WARDS: (C1, primary) the SMOOTH-MASS world must
     violate somewhere -- at rung level (some neg(A_h) > 0, the
     Haynsworth ledger then LOCATES the negative directions:
     typed VIOLATION-IN-R / VIOLATION-IN-S / VIOLATION-MIXED
     over the violating rungs) or, failing that, at flow level
     (B3-smooth n_cross > 0, typed VIOLATION-IN-FLOW).  Silent on
     both -> WARD-BROKEN.  (C2, must fire) Epstein x^2+5y^2 comb
     and scramble (seed 1) at kz 9: lam(E) > 1 (neg(A) > 0) on
     both, with the inertia localization printed; either silent
     -> WARD-BROKEN.  (C0, truth anchor) the truth wall holds on
     every rung (neg(A_h) = 0, tau_h > 0) -- the established
     object being reduced; a miss -> WARD-BROKEN.

 W   PIPELINE WARDS: W1 exactly 42 reachable rungs and every
     chain completes; W2 all tau finite; W3 >= 30 rungs carry the
     full core alias set (rungs missing a core alias are typed
     CORE-INCOMPLETE skips, printed).

KILLS: K1 a W ward breaks -> PIPELINE-BROKEN; K2 a C ward breaks
(truth wall broken / Haynsworth integer identity broken on an
evaluable rung / smooth silent on both channels / a C2 control
silent) -> WARD-BROKEN.

VERDICT (frozen enum): DEEPCORESCHUR-MEASURED with typed
sublabels OPERATOR-MARGIN-UNIFORM(r0) / OPERATOR-MARGIN-SHRINKS
(slope) (B1), SCHUR-TAU-TIED / SCHUR-TAU-LOOSE (B2),
CORE-INHERITS / CORE-CROSSES(n) + CORE-SEES-SMOOTH /
CORE-BLIND-TO-SMOOTH (B3), CORE-GRAIN-ACCESSIBLE /
CORE-GRAIN-DEAD (B4); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,4,6,8,10,12,14,16); H_LADDER_MAX = 900;
N_RUNGS_EXP = 42; MIN_CORE_RUNGS = 30; DIAG_REF = 0.0214
(reference only, diagonal object); R_UNIF_BAR = 1e-3; SLOPE_TOL =
-0.10; TIED_CORR = 0.99; R_SING_TOL_REL = 1e-10; GRAIN_KZ =
(9,12,13,26,40); GRAIN_PRIMES = (2,3,5,7,11); GRAIN_DEF_BAR =
0.20; RESOLVE_BAR = 1e-9; CTRL_KZ = 9; scramble seed 1.

SPEC AMENDMENTS (documented; fail-first preserved):
  v1 (2026-08-09, frozen pre-run): everything above.  Mechanical
     concretizations frozen with v1: (i) core.build_window
     results are MEMOIZED per (kz, seed) exactly as in
     deepcore_anatomy_probe (pure memoization of a deterministic
     function, bit-identical physics; several worlds share the
     same windows); (ii) negative-eigenvalue counts use the
     strict eig < 0.0 reading (port_schur_reduction precedent);
     (iii) the B3 smooth census requires only the BASE S_h of a
     step to be PD (an indefinite successor is precisely what
     eta_core <= 0 detects); (iv) B4 prime-power removal uses the
     explicit power list {p, p^2, ...} <= max atom of the
     hard-coded prime p -- no primality oracle is ever invoked;
     (v) the Haynsworth SINGULAR-SKIP guard is RELATIVE
     (R_SING_TOL_REL) because control-world blocks carry
     eigenvalues of order 10^3.
  v2 (2026-08-09, after run 1 -- which was already 16/16 green
     with the full typed verdict): THREE transparency-only print
     repairs, no bar, no object, no typed label moved (run-1 and
     run-2 verdicts identical): (a) the B2 summary additionally
     prints max |lamS/tau - 1|, max |lamS*wcore/tau - 1| and min
     wcore at full precision -- run 1 showed the decisive
     correspondence as '1.000' everywhere and the deviation scale
     was invisible; (b) the B4 dead-label aggregates ALL observed
     failure reasons instead of the first (run 1 typed only
     'base frame loss' although the surviving rungs also broke
     the additivity bar by x8-x18); (c) skipped ledger entries
     print 'n/a' instead of the sentinel -1.

NO RH claim: lambda_min ladders of finite-h blocks and an 8x8
Schur family are numerical measurements on the deployed v563
window ladder; the uniform R-margin and the core inheritance
remain open theorems, and no marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; wall Gram + Haynsworth
ledger verbatim from port_schur_reduction_probe.py
(PRIME.PORT.SCHUR.01); fixed core aliases from
deepcore_anatomy_probe.py (PRIME.PORT.DEEPCORE.01); ladder +
diagonal margin context from christoffel_zone_envelope_probe.py
(PRIME.CASE.ZONESPLIT.01, theta* = 0.700); smooth-mass world from
lattice_parametrix_probe.py (B1); Epstein control comb verbatim
from port_schur_reduction_probe.py.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deepcore_schur_reduction_probe.py
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

CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
H_LADDER_MAX = 900
N_RUNGS_EXP = 42
MIN_CORE_RUNGS = 30
DIAG_REF = 0.0214              # christoffel diagonal deep-half inf
R_UNIF_BAR = 1e-3              # B1 uniform-floor bar (operator)
SLOPE_TOL = -0.10              # B1 shrink-trend tolerance
TIED_CORR = 0.99               # B2 log-log correlation bar
R_SING_TOL_REL = 1e-10         # Haynsworth relative guard (v2)
GRAIN_KZ = (9, 12, 13, 26, 40)
GRAIN_PRIMES = (2, 3, 5, 7, 11)
GRAIN_DEF_BAR = 0.20
RESOLVE_BAR = 1e-9
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


# --------------- pipeline, verbatim (port_schur_reduction / deepcore)
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
    """SPEC concretization (i): pure memoization of the
    deterministic core.build_window (deepcore_anatomy verbatim)."""
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
    """The 42 reachable rungs (christoffel_zone_envelope verbatim)."""
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
    """PNT-mean masses 2 e^{u/2} du (lattice_parametrix B1)."""
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


def world_drop_primes(primes):
    """B4: remove ALL powers p^k of the listed hard-coded primes
    (explicit power lists -- no oracle)."""
    def fn(uu, mm, rr):
        nn = core._NN[:rr["n_atom"]].astype(np.int64)
        mx = int(nn.max())
        drop = np.zeros(len(nn), bool)
        for p in primes:
            pows, v = [], p
            while v <= mx:
                pows.append(v)
                v *= p
            drop |= np.isin(nn, np.asarray(pows, dtype=np.int64))
        keep = ~drop
        return uu[keep], mm[keep]
    return fn


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None,
                 want_vec=False):
    """Full wall operator A = I - E on the folded neg grid + the
    fixed-core block split, inertia ledger and Schur core."""
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
    out = dict(kz=kz, h=h, n=n)
    if want_vec:
        evA, VA = np.linalg.eigh(A)
    else:
        evA = np.linalg.eigvalsh(A)
        VA = None
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    X = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["lamR"] = float(evR[0])
    out["negR"] = int(np.sum(evR < 0.0))
    out["Rsing"] = bool(float(np.min(np.abs(evR)))
                        < R_SING_TOL_REL
                        * float(np.max(np.abs(evR))))
    S = B - X @ np.linalg.solve(R, X.T)
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["negS"] = int(np.sum(evS < 0.0))
    if want_vec:
        v = VA[:, 0]                    # soft mode of the wall
        out["wcore"] = float(np.sum(v[ic] ** 2))
    return out


def hayns_ok(r):
    """Integer Haynsworth identity on an evaluable rung
    (None = SINGULAR-SKIP, concretization v2: relative guard)."""
    if not r.get("core_ok", False):
        return None
    if r["Rsing"]:
        return None
    return r["negA"] == r["negR"] + r["negS"]


def inherit_ladder(rungs, tag):
    """B3: eta_core = lam_min(S^-1/2 S' S^-1/2) per consecutive
    full-core pair with PD base S; returns (rows, n_cross,
    n_hard, n_skip)."""
    rows, n_cross, n_hard, n_skip = [], 0, 0, 0
    for r1, r2 in zip(rungs, rungs[1:]):
        if (r1 is None or r2 is None
                or not r1.get("core_ok") or not r2.get("core_ok")):
            n_skip += 1
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            n_hard += 1
            continue
        w, V = np.linalg.eigh(r1["S"])
        Wm = V @ np.diag(1.0 / np.sqrt(w)) @ V.T
        eta = float(np.linalg.eigvalsh(
            Wm @ r2["S"] @ Wm)[0])
        rows.append((r1["h"], r2["h"], eta - 1.0, eta))
        if eta <= 0.0:
            n_cross += 1
    print("    [%s] %d steps computable, %d crossings "
          "(eta_core <= 0), %d rung-level failures, %d skips"
          % (tag, len(rows), n_cross, n_hard, n_skip))
    return rows, n_cross, n_hard, n_skip


def main():
    section("PRIME.PORT.DEEPCORE.SCHUR.01 -- the fixed 8x8 Schur "
            "reduction of the wall (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; full wall operator A = I - E; the "
          "diagonal 0.0214 is a REFERENCE, not an operator bound.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder (42 reachable rungs, h <= %d)"
            % H_LADDER_MAX)
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    for kz in zones:
        r = gram_anatomy(kz, want_vec=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
        truth.append(r)
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    fin = all(np.isfinite(r["tau"]) for r in truth)
    check("W2 all tau finite", fin, kill="K1")
    full = [r for r in truth if r["core_ok"]]
    n_inc = len(truth) - len(full)
    check("W3 >= %d full-core rungs (CORE-INCOMPLETE skips: %d)"
          % (MIN_CORE_RUNGS, n_inc), len(full) >= MIN_CORE_RUNGS,
          "%d full-core rungs" % len(full), kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})

    # ------------------------------------------------- B1 + B2 table
    section("B1/B2 -- THE LADDER: lam_min(R_h), the Schur core "
            "lam_min(S_h), tau_h  (diagonal ref %.4f)" % DIAG_REF)
    print("    kz   h     n    tau        lamR       lamR/tau   "
          "lamS       lamS/tau  S*w/tau  wcore  neg A/R/S Hay")
    hay_all = True
    for r in full:
        hk = hayns_ok(r)
        if hk is False:
            hay_all = False
        prod = (r["lamS"] * r["wcore"] / r["tau"]
                if r["tau"] > 0 else float("nan"))
        print("    %-4d %-4d %-5d %.3e %.3e %9.2f  %.3e %8.3f  "
              "%7.3f  %.3f  %d/%d/%d  %s"
              % (r["kz"], r["h"], r["n"], r["tau"], r["lamR"],
                 r["lamR"] / r["tau"] if r["tau"] > 0 else
                 float("nan"), r["lamS"],
                 r["lamS"] / r["tau"] if r["tau"] > 0 else
                 float("nan"), prod, r["wcore"], r["negA"],
                 r["negR"], r["negS"],
                 {True: "ok", False: "BRK", None: "skip"}[hk]),
              flush=True)

    # B1 typed
    hh = np.array([r["h"] for r in full], float)
    lamR = np.array([r["lamR"] for r in full], float)
    r0 = float(np.min(lamR))
    if np.all(lamR > 0.0):
        slope = float(np.polyfit(np.log(hh), np.log(lamR), 1)[0])
    else:
        slope = float("nan")
    ok_unif = (r0 >= R_UNIF_BAR
               and np.isfinite(slope) and slope >= SLOPE_TOL)
    b1 = ("OPERATOR-MARGIN-UNIFORM(r0=%.3e)" % r0 if ok_unif
          else "OPERATOR-MARGIN-SHRINKS(slope=%+.3f)" % slope)
    print("\n    B1: min lam_min(R) = %.3e (bar %.0e), log-log "
          "slope vs h %+.3f (tol %+.2f)"
          % (r0, R_UNIF_BAR, slope, SLOPE_TOL))
    print("    B1 honesty: diagonal deep-half ref %.4f (T_m "
          "envelope, theta*=0.700) -- measured OPERATOR floor is "
          "%.3e = %.3f x the diagonal reference"
          % (DIAG_REF, r0, r0 / DIAG_REF))
    check("B1.1 typed: %s" % b1, True)

    # B2 typed
    tau = np.array([r["tau"] for r in full], float)
    lamS = np.array([r["lamS"] for r in full], float)
    msk = (tau > 0.0) & (lamS > 0.0)
    corr = (float(np.corrcoef(np.log(tau[msk]),
                              np.log(lamS[msk]))[0, 1])
            if int(np.sum(msk)) >= 3 else float("nan"))
    ratio_med = float(np.median(lamS[msk] / tau[msk]))
    b2 = ("SCHUR-TAU-TIED(corr=%.4f, med S/tau=%.2f)"
          % (corr, ratio_med)
          if np.isfinite(corr) and corr >= TIED_CORR
          else "SCHUR-TAU-LOOSE(corr=%.4f)" % corr)
    prods = np.array([r["lamS"] * r["wcore"] / r["tau"]
                      for r in full if r["tau"] > 0])
    wcs = np.array([r["wcore"] for r in full])
    print("    B2: corr(log lamS, log tau) = %.4f (bar %.2f); "
          "lamS/tau med %.6f range [%.6f, %.6f]"
          % (corr, TIED_CORR, ratio_med,
             float(np.min(lamS[msk] / tau[msk])),
             float(np.max(lamS[msk] / tau[msk]))))
    print("    B2 deviations (v2 transparency): max |lamS/tau-1| "
          "= %.3e; product lamS*wcore/tau med %.6f, max |.-1| = "
          "%.3e; min wcore = %.6f"
          % (float(np.max(np.abs(lamS[msk] / tau[msk] - 1.0))),
             float(np.median(prods)),
             float(np.max(np.abs(prods - 1.0))),
             float(np.min(wcs))))
    check("B2.1 typed: %s" % b2, True)
    check("B2.2 WARD truth all-PSD (A, R, S) on every full-core "
          "rung",
          all(r["negA"] == 0 and r["negR"] == 0 and r["negS"] == 0
              for r in full), kill="K2")

    # ------------------------------------------------------------ B3
    section("B3 -- CORE INHERITANCE: eta_core = "
            "lam_min(S_h^-1/2 S_h+1 S_h^-1/2) (fixed 8x8 frame)")
    rows_t, ncr_t, nh_t, nsk_t = inherit_ladder(truth, "TRUTH")
    for h1, h2, lmH, eta in rows_t:
        print("    h %3d->%3d  lam_min(H_core) %+.4e  eta_core "
              "%.6f" % (h1, h2, lmH, eta))
    b3t = ("CORE-INHERITS" if ncr_t == 0
           else "CORE-CROSSES(n=%d)" % ncr_t)
    if rows_t:
        etas = [e for *_x, e in rows_t]
        print("    truth eta_core: min %.4f med %.4f max %.4f"
              % (min(etas), float(np.median(etas)), max(etas)))
    check("B3.1 typed (truth): %s" % b3t, True)

    print("\n    the smooth world (masses 2 e^{u/2} du):")
    sm = []
    for kz in zones:
        sm.append(gram_anatomy(kz, world_fn=world_smooth))
    sm = [r for r in sm if r is not None]
    sm.sort(key=lambda r: (r["h"], r["kz"]))
    rows_s, ncr_s, nh_s, nsk_s = inherit_ladder(sm, "SMOOTH")
    b3s = ("CORE-SEES-SMOOTH(n_cross=%d, n_hard=%d)"
           % (ncr_s, nh_s) if (ncr_s + nh_s) > 0
           else "CORE-BLIND-TO-SMOOTH")
    check("B3.2 typed (smooth): %s" % b3s, True)

    # ------------------------------------------------------------ C1
    section("C1 -- WARD: the smooth world must violate; the "
            "ledger locates the failure")
    viol = [r for r in sm if r["negA"] > 0]
    print("    smooth ladder: %d rungs built, %d with neg(A) > 0"
          % (len(sm), len(viol)))
    loc = "none"
    if viol:
        for r in viol[:12]:
            hk = hayns_ok(r)
            print("      kz %-3d h %4d: neg(A) %d = neg(R) %s + "
                  "neg(S) %s  (tau %.3e, Hayns %s)"
                  % (r["kz"], r["h"], r["negA"],
                     r.get("negR", "n/a") if hk is not None
                     else "n/a",
                     r.get("negS", "n/a") if hk is not None
                     else "n/a", r["tau"],
                     {True: "ok", False: "BROKEN",
                      None: "skip"}[hk]))
        if len(viol) > 12:
            print("      ... (%d more violating rungs)"
                  % (len(viol) - 12))
        in_r = sum(1 for r in viol if r.get("negR", 0) > 0)
        in_s = sum(1 for r in viol if r.get("negS", 0) > 0)
        if in_r > 0 and in_s == 0:
            loc = "VIOLATION-IN-R"
        elif in_s > 0 and in_r == 0:
            loc = "VIOLATION-IN-S"
        else:
            loc = "VIOLATION-MIXED"
    elif ncr_s > 0:
        loc = "VIOLATION-IN-FLOW"
    fired = bool(viol) or ncr_s > 0
    print("    location: %s" % loc)
    check("C1.1 WARD smooth violates (rung level or flow level): "
          "%s" % loc, fired, kill="K2")
    check("C0.1 WARD truth wall holds on every rung (neg(A) = 0)",
          all(r["negA"] == 0 for r in truth), kill="K2")

    # ------------------------------------------------------------ B4
    section("B4 -- PER-PRIME GRAIN on the fixed 8x8 core "
            "(leave-one-prime-out at kz %s; primes %s)"
            % (GRAIN_KZ, GRAIN_PRIMES))
    grain_ok = True
    grain_defects = []
    grain_reasons = []
    by_kz = {r["kz"]: r for r in full}
    for kz in GRAIN_KZ:
        base = by_kz.get(kz)
        if base is None:
            grain_ok = False
            grain_reasons.append("base frame loss")
            print("    kz %-3d: BASE FRAME LOSS (core incomplete)"
                  % kz)
            continue
        S0 = base["S"]
        nS0 = float(np.linalg.norm(S0))
        Dsum = np.zeros_like(S0)
        print("    kz %-3d h %4d (lam_min S %.3e):"
              % (kz, base["h"], base["lamS"]))
        all_res = True
        frame_loss = False
        for p in GRAIN_PRIMES:
            rp = gram_anatomy(kz,
                              world_fn=world_drop_primes((p,)))
            if rp is None or not rp.get("core_ok"):
                frame_loss = True
                print("      drop p=%-2d : FRAME LOSS" % p)
                continue
            Dp = rp["S"] - S0
            Dsum += Dp
            rel = float(np.linalg.norm(Dp)) / nS0
            all_res &= rel >= RESOLVE_BAR
            print("      drop p=%-2d : ||D_p||_F %.3e  rel %.3e  "
                  "lam_min(S\\p) %+.3e" % (p, np.linalg.norm(Dp),
                                           rel, rp["lamS"]))
        ra = gram_anatomy(kz,
                          world_fn=world_drop_primes(GRAIN_PRIMES))
        if ra is None or not ra.get("core_ok") or frame_loss:
            grain_ok = False
            grain_reasons.append("frame loss")
            print("      joint drop: FRAME LOSS -> GRAIN-DEAD "
                  "at this rung")
            continue
        Dall = ra["S"] - S0
        defect = (float(np.linalg.norm(Dall - Dsum))
                  / max(float(np.linalg.norm(Dall)), 1e-300))
        grain_defects.append(defect)
        print("      joint drop: ||D_all||_F %.3e  additivity "
              "defect %.4f (bar %.2f)  lam_min(S\\all) %+.3e"
              % (np.linalg.norm(Dall), defect, GRAIN_DEF_BAR,
                 ra["lamS"]), flush=True)
        if not all_res:
            grain_ok = False
            grain_reasons.append("response unresolved")
        if defect > GRAIN_DEF_BAR:
            grain_ok = False
            grain_reasons.append("additivity defect > bar")
    reasons = " + ".join(sorted(set(grain_reasons))) \
        if grain_reasons else "no rung evaluable"
    b4 = ("CORE-GRAIN-ACCESSIBLE(max defect=%.4f)"
          % (max(grain_defects) if grain_defects else
             float("nan"))
          if grain_ok and grain_defects
          else "CORE-GRAIN-DEAD(%s)" % reasons)
    check("B4.1 typed: %s" % b4, True)

    # ------------------------------------------------------------ C2
    section("C2 -- controls at kz %d: Epstein + scramble frame "
            "status" % CTRL_KZ)
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {"Epstein": gram_anatomy(
               CTRL_KZ, comb=(np.log(nn.astype(float)),
                              2.0 * lamE_[nn]
                              / np.sqrt(nn.astype(float)))),
           "scramble": gram_anatomy(CTRL_KZ, scramble_seed=1)}
    fired_all = True
    hay_ctl = True
    for name, r in ctl.items():
        if r is None:
            print("    %-9s: chain dies -> fires (frame death)"
                  % name)
            continue
        f = r["negA"] > 0
        fired_all &= f
        hk = hayns_ok(r)
        if hk is False:
            hay_ctl = False
        print("    %-9s: tau %+.3e  neg(A) %d = neg(R) %s + "
              "neg(S) %s  Hayns %s -> %s"
              % (name, r["tau"], r["negA"],
                 r.get("negR", "-"), r.get("negS", "-"),
                 {True: "ok", False: "BROKEN",
                  None: "skip"}[hk],
                 "FIRES" if f else "SILENT"), flush=True)
    check("C2.1 WARD both controls fire (neg(A) > 0)", fired_all,
          kill="K2")
    hay_sm = all(hayns_ok(r) is not False for r in sm)
    check("B2.3 WARD Haynsworth integer identity on every "
          "evaluable rung (truth/smooth/controls)",
          hay_all and hay_sm and hay_ctl, kill="K2")

    # ------------------------------------------------------------ B5
    section("B5 -- THE REDUCTION STATEMENT (measured shadow)")
    print("    IF  lam_min(R_h) >= r_0 > 0 uniformly in h "
          "(measured candidate r_0 = %.3e; typed %s)" % (r0, b1))
    print("    THEN (Haynsworth, warded above)  the wall "
          "A_h >= 0  <=>  S_h >= 0 for the FIXED 8x8 family")
    print("    at the core aliases %s -- the RH wand as a "
          "fixed-dimension statement." % (list(CORE_J),))
    print("    finite shadow: the B2 ladder (lam_min(S) ~ "
          "tau-scale: %s) and the B3 inheritance (%s)."
          % (b2, b3t))
    print("    open pieces: (1) the uniform R-margin theorem "
          "(B1 measured: %s -- the diagonal +%.4f envelope does "
          "NOT transfer to the operator block as measured); "
          "(2) the core inheritance theorem." % (b1, DIAG_REF))
    check("B5.1 reduction statement printed", True)

    return finish(dict(b1=b1, b2=b2, b3t=b3t, b3s=b3s, b4=b4,
                       loc=loc))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("DEEPCORESCHUR-MEASURED / %(b1)s / %(b2)s / "
                   "%(b3t)s / %(b3s)s / %(b4)s [%(loc)s]"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
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
    ('relative_congruence_probe', _SRC_0, 16, (), 'RELCONG-MEASURED', 0),
    ('pivot_factor_probe', _SRC_1, 15, (), 'PIVOTFACTOR-MEASURED', 0),
    ('euler_rouche_probe', _SRC_2, 14, (), 'ROUCHE-MEASURED', 0),
    ('deepcore_schur_reduction_probe', _SRC_3, 16, (), 'DEEPCORESCHUR-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v892 -- PRIME.PORT.RELCONG.01 + PRIME.PORT.PIVOTFACTOR.01 + PRIME.PORT.EULER.ROUCHE.01 + PRIME.PORT.DEEPCORE.SCHUR.01: the closure architecture of the wall -- the exact hermitian congruence with its non-decaying margin, the flag/pivot chain, the honest Rouche kill, and the fixed 8x8 Schur-core reduction')
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
    print("v892: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the closure is relative and one-sided: exact congruence with bounded margins at every level; the two-sided norm route is measured dead')
    print("[%s] v892 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
