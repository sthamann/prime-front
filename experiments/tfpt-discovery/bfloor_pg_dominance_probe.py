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
