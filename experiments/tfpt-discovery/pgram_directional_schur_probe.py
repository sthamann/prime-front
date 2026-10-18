#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pgram_directional_schur_probe -- PRIME.PORT.PG.SCHUR.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the ONE-THEOREM question on the n > q half.
2026-08-11.)

THE QUESTION (frozen).  P2/P3 split the wall update into (B_h PD)
AND (n_h > q_h) with q_h = b* B^{-1} b in the frozen Householder
frame (gap n - q min/med 0.052/0.888 on 39/39).  CXLIV certified
the B-half via the source-only chain B >= 1/2 P_G + c_dom I =: D
with P_G the CD-Gram co-block of the rung's OWN positive chain and
c_dom the exact-rational LDL-certified dominance shift (assembled
floor min c_B = 0.5914 > 0, so D is PD).  Loewner antitonicity of
the matrix inverse gives, from  B >= D > 0,
    B^{-1} <= D^{-1}  ==>  q = b* B^{-1} b <= b* D^{-1} b =: qbar,
so the STRONGER statement  n > qbar  SUFFICES for the wall.  Its
value: qbar is built from the P_G-dominated block D whose
DIRECTION content is source-only (positive-chain CD Gram plus the
identity) -- if n > qbar holds with an O(1) ladder, the open
problem reduces to controlling the P_G-dominated Schur block
uniformly in h instead of B itself.  This probe measures exactly:
  (a) delta_h = n_h - qbar_h on all reachable steps, and
      deltahat_h = delta_h / mu1(h), mu1(h) = 4 sin^2(pi/(2h+1))
      (the deployed KMS/Dirichlet parity gap, source-only);
  (b) THE VERDICT (frozen enums, below);
  (c) if OUTCOME-B: the monotone Woodbury hierarchy
      D_{k+1} = D_k + w_k w_k* with source-only components w_k;
  (d) controls + the exact Loewner ward q <= qbar everywhere.

EXACTNESS MODEL (frozen).  All decisions and the delta ladder are
computed in EXACT Fraction arithmetic on the float64-computed step
matrices (whose entries are exact rationals -- the v897/CXLIV
certificate class): Bfr = fr(B), Pfr = fr(0.5 * P_G) (halving a
float is exact), Kfr = Bfr - Pfr formed in Fractions, c_dom by
exact dyadic LDL bisection on Kfr, Dfr = Pfr + c_dom I, q and qbar
by exact Gaussian solves on Bfr and Dfr, delta = fr(n) - qbar
exact.  Float eigensolves appear ONLY as bisection hints and
printed context (a hint cannot affect a certificate: the final PD
decision is re-run exactly).  What is NOT enclosed: the float
pipeline that produces the entries (FFT density, Lanczos, eigh
frame, Schur solves) -- the interval rollout of that pipeline is a
CONCURRENT, separate work item and is deliberately NOT duplicated
here; this probe consumes the float-level chain only.  NO RH
claim.

FROZEN PROTOCOL (pipeline verbatim from
bfloor_pg_dominance_probe.py = CXLIV = v900 chain; ONE Gram per
rung; window memoization):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2 >=
     30 full-core rungs; W3a truth all-PSD (A, R, S); W3b >= 20
     consecutive full-core steps; W4 REPRODUCTION P2/P3 ledger:
     min lam_min(B) == 0.679 (rtol 2e-2), gap min/med ==
     0.052/0.888 (rtol 5e-2), raw-B certified disaster (best bound
     < 0 on every step); W5 REPRODUCTION of CXLIV V4: P_G PD on
     every step (float, PG_TOL) and float dominance
     negidx(B - 1/2 P_G) = 0 on >= DOMHALF_MIN steps (CXLIV
     measured 39/39, min lam_min +0.179); W6 MACHINE WARDS: the
     exact LDL accepts PD / refuses indefinite; the exact solver
     reproduces a known rational solution exactly.

 E1  THE EXACT LADDER (per step): c_dom = largest certified c
     with Kfr - c I PD (dyadic bisection, BIS_ITERS; lo = 0 if PD
     at 0, else lo = float hint minus LO_PAD relative padding --
     if PD fails at lo the step is typed D-FAIL); Dfr = Pfr +
     c_dom I; wards (kill -> WARD-BROKEN): E1.w1 exact Loewner
     q <= qbar on EVERY step (Fraction comparison, no tolerance);
     E1.w2 exact re-certification B - D PD on every step; E1.w3
     D PD (exact; expected everywhere since c_B > 0 in CXLIV --
     typed count, a failing step is D-FAIL, measured not killed).
     Printed ladder: kz, h, alpha, n, q, qbar, delta = n - qbar,
     deltahat = delta/mu1(h), qbar/q.

 E2  THE VERDICT (frozen a priori):
       OUTCOME-A  iff delta_h > 0 EXACTLY on all steps -- a
                  genuine new sufficient route; report the margin
                  ladder min/med and its tau-screen (OLS slope of
                  log delta vs log tau on the positive subset,
                  bands PASS |s| <= 0.30 / RELOC >= 0.70 / AMBIG);
       OUTCOME-B  iff delta_h <= 0 somewhere AND median(qbar/q)
                  <= QLOSS_BAR = 2.0 -- near miss; report the
                  deficit per failing step in units of n and of
                  mu1, then run E3;
       OUTCOME-C  iff median(qbar/q) > QLOSS_BAR -- the bound
                  loses O(1), route honestly dead; report median
                  and max qbar/q.
     The qbar/q ladder is printed for every outcome (bound
     quality is reported even when the route wins).

 E3  THE HIERARCHY (only if OUTCOME-B; per failing step): the
     monotone updates D_{k+1} = D_k + w_k w_k* with the
     source-only components the positive chain itself offers:
     w_k = sqrt(1/2) u_k, u_k = co-block of Q^T (sqrt(v_core)
     p_k(y_core)) -- the rank-1 CD-Gram summands of the REMAINING
     half of P_G, taken in ASCENDING chain degree k (frozen
     order; NEVER an eigenvector of B, never b, n or any target
     data in the selection).  Acceptance: exact LDL PD of
     B - D_{k+1} (a certificate decision, not a construction);
     rejected components are skipped, at most K_HIER candidates
     tried.  Each accepted update lowers qbar via
     Sherman-Morrison: qbar_{k+1} = qbar_k - z^2/(1 + w* D_k^{-1}
     w), z = w* D_k^{-1} b, VERIFIED against the direct solve to
     WOODBURY_TOL relative (machine-precision ward, kill ->
     WARD-BROKEN).  k*(h) = number of ACCEPTED components until
     delta > 0; typed KSTAR-ALL-REACHED(max k*, OLS slope of k*
     vs log h) / KSTAR-NOT-REACHED(count) -- bounded k* = a
     finite proof architecture for the tail; growing k* = honest
     relocation.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) =
     0 everywhere; C1 smooth world neg(A) > 0 on >= 1 rung; C2
     Epstein x^2+5y^2 comb + scramble (seed 1) at kz 9 fire
     (neg(A) > 0 or frame death); C3 THE DECLARED BREAK MODE of
     this route in the smooth world: B0 (smooth co-block, same
     truth frame) NOT PD by exact LDL on >= REFUSE_MIN usable
     steps -- the Loewner premise B >= D > 0 is unavailable, the
     route cannot even be stated there; C4 the scramble core,
     where it exists, must break the floor (disclosed skip if the
     scramble core dies; C3 carries the cannot-fake content).

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
ward / control failures (W4-W6, E1.w1, E1.w2, E3 Woodbury ward,
C0-C4) -> WARD-BROKEN.  All E-typed outcomes are measurements,
never kills.

VERDICT (frozen enum): PGSCHUR-MEASURED with typed sublabels
LOEWNER-WARDED(N/N exact), DFAIL(count), and exactly one of
OUTCOME-A(min delta, min deltahat, screen) /
OUTCOME-B(worst deficit/n, worst deficit/mu1, KSTAR-...) /
OUTCOME-C(med qbar/q, max qbar/q); else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2); PG_TOL
= 1e-12; S_HALF = 1/2 EXACT (the CXLIV canonical V4, frozen as
declared input -- no variant scan here); DOMHALF_MIN = 37
(expected 39); BIS_ITERS = 40; LO_PAD = 2^-10 relative; QLOSS_BAR
= 2.0; K_HIER = 64; WOODBURY_TOL = 1e-9; REFUSE_MIN = 30;
SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; CTRL_KZ = 9; scramble seed
1; mu1(h) = 4 sin^2(pi/(2h+1)) on r2's h.  Runtime cap declared:
8 min.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign, no spectral data of the TARGET B in any CONSTRUCTION
-- P_G and the hierarchy components are source-only (positive
chain at the core nodes, frozen constants); c_dom is a CERTIFIED
scalar obtained by the declared v897/CXLIV exact-LDL certificate
class on B - 1/2 P_G (a decision procedure, not a fit; the
direction content of D stays source-only: P_G plus the identity);
float eigensolves are hints/context only.  The hierarchy selects
components by frozen chain order, never by target data.

NO-GO COMPLIANCE (frozen): no rank-1 approximation of the core
update; no plain Herglotz certificate; no fit where an identity
is claimed; exact-rational LDL is allowed as a CERTIFICATE per
the CXLIV mandate -- declared, not silent.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): one smoke run
of this script (20/20 with the identical bars; NO bar, band,
count, rule or enum was moved after it) measured: pipeline +
P2/P3 + CXLIV reproduction green (min lam_min(B) 0.6790, gap
0.0520/0.8875, raw disaster best -88.2, P_G PD 39/39, float
half-dominance 39/39, min +0.179 reproduced).  E1: c_dom
certified with lo = 0 on 39/39 (no D-FAIL), D PD exact 39/39,
B - D PD re-certified 39/39, the exact Loewner ward q <= qbar
holds 39/39.  THE ANSWER IS OUTCOME-C, AND IT IS NOT CLOSE:
delta = n - qbar > 0 on only 1/39 steps (kz 60 h 388, +0.0926);
delta min/med -4071.4/-5.28; deltahat min/med -7.8e+07/-1.0e+05;
qbar/q min/med/max 4.39/91.3/408.2 -- the Loewner bound loses
TWO ORDERS OF MAGNITUDE, not O(1): D = 1/2 P_G + c_dom I is an
excellent FLOOR model of B (CXLIV: c_B/lam_min(B) med 0.979) but
a terrible INVERSE model along b, because q = b* B^{-1} b reads
B's full spectral geometry (B has O(10..1e4)-scale directions
that D truncates at its O(1) floor, so D^{-1} inflates exactly
the b-components that B^{-1} suppresses).  The delta tau-screen
is vacuous (pos = 1, disclosed).  E3 does not run (frozen:
hierarchy only on OUTCOME-B).  Controls: smooth neg(A) > 0 on
42/42, C3 refusal 35/35, Epstein neg(A) 55 fires, scramble
neg(A) 37 fires, scramble core dead -> C4 disclosed skip.
Runtime 4.3 s (cap holds).  Fail-first preserved: nothing was
weakened; the verdict rule, bars and enums are exactly as frozen
above.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as
P2/CXLIV; (iii) P_G via eval_chain on r2's own chain at r2's core
nodes, degree < h (CXLIV V0 direction, s = 1/2 by V4); (iv) exact
LDL = full symmetric Gaussian elimination in Fraction arithmetic,
PD iff all pivots > 0 (Sylvester); exact solver = Gaussian
elimination with partial pivoting in Fractions; (v) bisection lo
certified by a final exact re-decision; (vi) negidx = count of
float eigenvalues < 0; (vii) OLS population statistics as v900;
screens read positive subsets.

NO RH claim: delta > 0 (had it held) would be a SURFACE statement
about the computed step matrices of the deployed ladder; it does
not prove n > q uniformity in h, the pipeline enclosure, or any
tail statement.  OUTCOME-C is a route-mortality measurement.  No
marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
P_G machinery verbatim from bfloor_pg_dominance_probe.py (CXLIV);
P2/P3 split from port_tangent_schur_probe (declared input); mu1
parity geometry as moving_node_second_order_probe (CXLIII,
declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/pgram_directional_schur_probe.py
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
S_HALF = Fraction(1, 2)
DOMHALF_MIN = 37
BIS_ITERS = 40
LO_PAD = Fraction(1, 1024)
QLOSS_BAR = 2.0
K_HIER = 64
WOODBURY_TOL = 1e-9
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


# --------------- pipeline, verbatim (bfloor_pg_dominance_probe)
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


# ------------------------- the exact-rational certificate class
def mat_fr(M):
    """float64 matrix -> exact-rational (Fraction) list of lists."""
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
    bisection; final PD decision re-run exactly at the returned
    lo).  None if PD fails at lo."""
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


def solve_fr(Afr, bfr):
    """Exact Gaussian elimination with partial pivoting.
    Returns x with A x = b in Fractions, or None if singular."""
    n = len(Afr)
    A = [list(Afr[i]) + [bfr[i]] for i in range(n)]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(A[i][k]))
        if A[p][k] == 0:
            return None
        if p != k:
            A[k], A[p] = A[p], A[k]
        for i in range(k + 1, n):
            f = A[i][k] / A[k][k]
            for j in range(k, n + 1):
                A[i][j] = A[i][j] - f * A[k][j]
    x = [Fraction(0)] * n
    for i in range(n - 1, -1, -1):
        s = A[i][n]
        for j in range(i + 1, n):
            s = s - A[i][j] * x[j]
        x[i] = s / A[i][i]
    return x


def quad_fr(Afr, bfr):
    """Exact b* A^{-1} b in Fractions (None if singular)."""
    x = solve_fr(Afr, bfr)
    if x is None:
        return None
    s = Fraction(0)
    for bi, xi in zip(bfr, x):
        s = s + bi * xi
    return s


def build_pg(w):
    """The source-only P_G co-block (CXLIV V0 direction)."""
    r2 = w["r2"]
    ch = r2.get("chain")
    if ch is None:
        return None
    al, be, m0 = ch
    Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
    Gc = (np.sqrt(r2["v_core"])[:, None] * (Pc @ Pc.T)
          * np.sqrt(r2["v_core"])[None, :])
    Gc = 0.5 * (Gc + Gc.T)
    PG = (w["Q"].T @ Gc @ w["Q"])[1:, 1:]
    return 0.5 * (PG + PG.T)


def pg_components(w):
    """The rank-1 CD-Gram summands u_k of P_G (co-block frame),
    ascending chain degree k (frozen hierarchy order)."""
    r2 = w["r2"]
    al, be, m0 = r2["chain"]
    Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
    sq = np.sqrt(r2["v_core"])
    out = []
    for k in range(Pc.shape[1]):
        g = sq * Pc[:, k]
        out.append((w["Q"].T @ g)[1:])
    return out


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def main():
    section("PRIME.PORT.PG.SCHUR.01 -- n > qbar = b* D^{-1} b with "
            "D = 1/2 P_G + c_dom I: the directional Loewner route "
            "on the n > q half (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Exact statements are "
          "about the float64-computed step matrices (caveat block "
          "in spec); the pipeline interval rollout is a concurrent "
          "separate work item, NOT duplicated here.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + P2/P3 + CXLIV reproduction")
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
        rows.append(dict(r1=r1, r2=r2, Q=Q, B=B, b=b, nsc=nsc,
                         B0=B0, minB=minB, gap=gap, tau=r1["tau"],
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
    pg_ok = True
    n_dom = 0
    for w in rows:
        PG = build_pg(w)
        if PG is None:
            pg_ok = False
            continue
        if float(np.linalg.eigvalsh(PG)[0]) <= PG_TOL:
            pg_ok = False
        w["PG"] = PG
        Dm = w["B"] - 0.5 * PG
        Dm = 0.5 * (Dm + Dm.T)
        w["lamK_hint"] = float(np.linalg.eigvalsh(Dm)[0])
        if int(np.sum(np.linalg.eigvalsh(Dm) < 0.0)) == 0:
            n_dom += 1
    check("W5 REPRODUCTION CXLIV V4: P_G PD on every step; float "
          "dominance negidx(B - 1/2 P_G) = 0 on %d/%d (>= %d; "
          "CXLIV: 39/39, min +0.179)"
          % (n_dom, len(rows), DOMHALF_MIN),
          pg_ok and n_dom >= DOMHALF_MIN, kill="K2")
    ok_pd, _ = pd_exact(mat_fr(np.array([[2.0, 1.0], [1.0, 2.0]])))
    ok_ind, _ = pd_exact(mat_fr(np.array([[1.0, 2.0], [2.0, 1.0]])))
    xs = solve_fr([[Fraction(2), Fraction(1)],
                   [Fraction(1), Fraction(2)]],
                  [Fraction(1), Fraction(0)])
    ok_sol = (xs is not None and xs[0] == Fraction(2, 3)
              and xs[1] == Fraction(-1, 3))
    check("W6 MACHINE WARDS: exact LDL accepts PD / refuses "
          "indefinite; exact solver hits the known rational "
          "solution", ok_pd and not ok_ind and ok_sol, kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- E1
    section("E1 -- the exact ladder: c_dom, D, q, qbar, delta")
    n_loew, n_recert, n_dpd, n_dfail = 0, 0, 0, 0
    ladder = []
    print("      kz    h    alpha    n_h       q         qbar      "
          "delta      deltahat    qbar/q")
    for w in rows:
        n7 = 7
        Bfr = mat_fr(w["B"])
        Pfr = mat_fr(0.5 * w["PG"])
        Kfr = [[Bfr[i][j] - Pfr[i][j] for j in range(n7)]
               for i in range(n7)]
        hi = min(Kfr[k][k] for k in range(n7))
        ok0, _ = pd_exact(Kfr)
        if ok0:
            lo = Fraction(0)
        else:
            hint = Fraction(w["lamK_hint"])
            lo = hint - LO_PAD * max(Fraction(1), abs(hint))
            okl, _ = pd_exact(Kfr, lo)
            if not okl:
                n_dfail += 1
                print("    D-FAIL kz %d h %d: PD fails at padded "
                      "lo" % (w["r2"]["kz"], w["r2"]["h"]),
                      flush=True)
                continue
        cdom = cert_floor_exact(Kfr, lo, hi)
        if cdom is None:
            n_dfail += 1
            print("    D-FAIL kz %d h %d: bisection refused"
                  % (w["r2"]["kz"], w["r2"]["h"]), flush=True)
            continue
        Dfr = [[Pfr[i][j] + (cdom if i == j else 0)
                for j in range(n7)] for i in range(n7)]
        okD, _ = pd_exact(Dfr)
        if okD:
            n_dpd += 1
        else:
            n_dfail += 1
            print("    D-FAIL kz %d h %d: D not PD"
                  % (w["r2"]["kz"], w["r2"]["h"]), flush=True)
            continue
        okBD, _ = pd_exact(Kfr, cdom)
        if okBD:
            n_recert += 1
        bfr = [Fraction(float(x)) for x in w["b"]]
        nfr = Fraction(w["nsc"])
        q = quad_fr(Bfr, bfr)
        qbar = quad_fr(Dfr, bfr)
        if q is None or qbar is None:
            n_dfail += 1
            print("    D-FAIL kz %d h %d: singular solve"
                  % (w["r2"]["kz"], w["r2"]["h"]), flush=True)
            continue
        if q <= qbar:
            n_loew += 1
        delta = nfr - qbar
        mu1 = mu1_of(w["r2"]["h"])
        row = dict(w=w, cdom=cdom, q=q, qbar=qbar, delta=delta,
                   nfr=nfr, mu1=mu1, Dflt=0.5 * w["PG"]
                   + float(cdom) * np.eye(n7))
        ladder.append(row)
        print("    %4d %5d  %6.2f  %8.4f  %8.4f  %8.4f  %+9.4f  "
              "%+.3e  %6.3f"
              % (w["r2"]["kz"], w["r2"]["h"], w["r2"]["alpha"],
                 float(nfr), float(q), float(qbar), float(delta),
                 float(delta) / mu1, float(qbar / q)), flush=True)
    N = len(rows)
    check("E1.w1 WARD exact Loewner q <= qbar on %d/%d usable "
          "steps (Fraction comparison, no tolerance)"
          % (n_loew, len(ladder)), n_loew == len(ladder),
          kill="K2")
    check("E1.w2 WARD exact re-certification B - D PD on %d/%d"
          % (n_recert, len(ladder)), n_recert == len(ladder),
          kill="K2")
    check("E1.w3 typed: D PD exact on %d/%d, D-FAIL on %d "
          "(measured)" % (n_dpd, N, n_dfail), True)
    if KILLS or not ladder:
        return finish({})

    # ----------------------------------------------------------- E2
    section("E2 -- the frozen verdict rule")
    deltas = np.array([float(r["delta"]) for r in ladder])
    dhat = np.array([float(r["delta"]) / r["mu1"] for r in ladder])
    qr = np.array([float(r["qbar"] / r["q"]) for r in ladder])
    n_pos = sum(1 for r in ladder if r["delta"] > 0)
    med_qr = float(np.median(qr))
    print("    delta > 0 (exact) on %d/%d steps; delta min/med "
          "%+.4f/%+.4f; deltahat min/med %+.3e/%+.3e; qbar/q "
          "min/med/max %.3f/%.3f/%.3f"
          % (n_pos, len(ladder), float(deltas.min()),
             float(np.median(deltas)), float(dhat.min()),
             float(np.median(dhat)), float(qr.min()), med_qr,
             float(qr.max())), flush=True)
    scr_lab, _sl = screen(deltas, [r["w"]["tau"] for r in ladder])
    print("    tau-screen of delta (positive subset): %s"
          % scr_lab)
    if n_pos == len(ladder) and n_dfail == 0:
        outcome = ("OUTCOME-A(min delta=%+.4f, min deltahat="
                   "%+.3e, screen %s)"
                   % (float(deltas.min()), float(dhat.min()),
                      scr_lab))
        print("    READING: a genuine new sufficient route -- the "
              "open problem reduces to controlling the "
              "P_G-dominated block D uniformly in h.")
    elif med_qr <= QLOSS_BAR:
        outcome = "OUTCOME-B"
        for r in ladder:
            if r["delta"] <= 0:
                print("    DEFICIT kz %d h %d: |delta|/n %.3f, "
                      "|delta|/mu1 %.3e"
                      % (r["w"]["r2"]["kz"], r["w"]["r2"]["h"],
                         float(-r["delta"] / r["nfr"]),
                         float(-r["delta"]) / r["mu1"]),
                      flush=True)
    else:
        outcome = ("OUTCOME-C(med qbar/q=%.3f, max=%.3f)"
                   % (med_qr, float(qr.max())))
        print("    READING: the Loewner bound loses O(1) -- the "
              "route is honestly dead in this direction; D is a "
              "floor model of B, not an inverse model along b.")
    check("E2 typed: %s" % outcome, True)

    # ----------------------------------------------------------- E3
    section("E3 -- the Woodbury hierarchy (only on OUTCOME-B)")
    kstar_lab = "KSTAR-SKIPPED(frozen: hierarchy runs only on " \
                "OUTCOME-B)"
    if outcome == "OUTCOME-B":
        kstars, hs_k, n_nr = [], [], 0
        wood_ok = True
        for r in ladder:
            if r["delta"] > 0:
                continue
            w = r["w"]
            comps = pg_components(w)
            Dc = r["Dflt"].copy()
            qbar_c = float(r["qbar"])
            n_acc, tried = 0, 0
            reached = False
            for u in comps:
                if tried >= K_HIER:
                    break
                tried += 1
                wv = math.sqrt(0.5) * u
                Dn = Dc + np.outer(wv, wv)
                okd, _ = pd_exact(mat_fr(0.5 * (w["B"] - Dn
                                                + (w["B"]
                                                   - Dn).T)))
                if not okd:
                    continue
                x = np.linalg.solve(Dc, w["b"])
                y = np.linalg.solve(Dc, wv)
                z = float(wv @ x)
                den = 1.0 + float(wv @ y)
                qbar_w = qbar_c - z * z / den
                qbar_d = float(w["b"] @ np.linalg.solve(Dn,
                                                        w["b"]))
                rel = abs(qbar_w - qbar_d) / max(abs(qbar_d),
                                                 1e-30)
                if rel > WOODBURY_TOL:
                    wood_ok = False
                Dc, qbar_c = Dn, qbar_d
                n_acc += 1
                if w["nsc"] - qbar_c > 0:
                    reached = True
                    break
            if reached:
                kstars.append(n_acc)
                hs_k.append(w["r2"]["h"])
                print("    k* kz %d h %d: %d accepted components"
                      % (w["r2"]["kz"], w["r2"]["h"], n_acc),
                      flush=True)
            else:
                n_nr += 1
                print("    k* NOT-REACHED kz %d h %d (tried %d)"
                      % (w["r2"]["kz"], w["r2"]["h"], tried),
                      flush=True)
        check("E3.w WARD Sherman-Morrison identity <= %.0e "
              "relative on every accepted update" % WOODBURY_TOL,
              wood_ok, kill="K2")
        if kstars and n_nr == 0:
            _a, slk, r2k = ols_line(np.log(np.array(hs_k, float)),
                                    np.array(kstars, float))
            kstar_lab = ("KSTAR-ALL-REACHED(max=%d, med=%.1f, "
                         "slope vs log h %+.2f R2 %.2f)"
                         % (max(kstars),
                            float(np.median(kstars)), slk, r2k))
        else:
            kstar_lab = ("KSTAR-NOT-REACHED(%d of %d failing "
                         "steps)" % (n_nr, n_nr + len(kstars)))
    check("E3 typed: %s" % kstar_lab, True)

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
    n_ref, n_use = 0, 0
    for w in rows:
        if w["B0"] is None:
            continue
        n_use += 1
        ok0, _ = pd_exact(mat_fr(0.5 * (w["B0"] + w["B0"].T)))
        if not ok0:
            n_ref += 1
    check("C3 WARD DECLARED BREAK MODE: exact LDL refuses the "
          "smooth co-block B0 on %d/%d usable steps (>= %d) -- "
          "the Loewner premise B >= D > 0 dies in the smooth "
          "world" % (n_ref, n_use, REFUSE_MIN),
          n_ref >= REFUSE_MIN, kill="K2")
    rsc = ctl["scramble"]
    c4_ok = True
    c4_msg = "scramble core dead -> skipped (disclosed; C3 " \
             "carries the content)"
    if isinstance(rsc, dict) and rsc.get("core_ok") \
            and "S" in rsc and rsc["lamS"] < 0.0:
        c4_ok = rsc["lamS"] < 0.0
        c4_msg = ("lam_min(S_scr) %.3e < 0 -> the scramble core "
                  "breaks the floor" % rsc["lamS"])
    check("C4 WARD scramble breaks the floor: %s" % c4_msg,
          c4_ok, kill="K2")

    labels = dict(loew="LOEWNER-WARDED(%d/%d exact)"
                  % (n_loew, len(ladder)),
                  dfail="DFAIL(%d)" % n_dfail,
                  outcome=outcome, kstar=kstar_lab)
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
        VERDICT = ("PGSCHUR-MEASURED / %s / %s / %s / %s"
                   % (labels.get("loew", "-"),
                      labels.get("dfail", "-"),
                      labels.get("outcome", "-"),
                      labels.get("kstar", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): every exact statement above is about
  the float64-computed step matrices (whose entries are exact
  rationals); the D-direction is source-only (P_G plus identity),
  c_dom is a certified scalar of the declared certificate class.
  What this does NOT prove: the interval enclosure of the
  pipeline (concurrent separate work item), n > q uniformity in
  h beyond the reachable surface, or any tail statement.  NO RH
  claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
