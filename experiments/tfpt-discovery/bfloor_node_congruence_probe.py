#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bfloor_node_congruence_probe -- PRIME.PORT.BFLOOR.CONGRUENCE.03
(EXPLORATION ONLY, experiments/; round 61, theorem-engineering on
the RH-side wall: THIRD attempt at a certified B-floor.  New element
vs rounds 59/60: the congruence lives on the B-BLOCK in the tangent
frame and FOLLOWS THE WANDERING NODE -- T_h built from the Jacobi
matrix of the positive reference measure shifted by the per-rung
classical node y*_h; plus the MANDATED fallback that handles the
B0-not-PD constraint (|B0|-functional calculus / the positive
completed measure's block) with the NEGATIVE INDEX per step and the
explicit small Schur-determinant reduction.  2026-08-10.)

THE OBJECT (rounds 58-60 verbatim).  P2/P3 reduced the wall update
to (B_h PD) AND (n_h > q_h) in the frozen Householder frame of the
core Schur complement S (8 core folds CORE_J, soft direction of S_1
rotated out; B = 7x7 co-block of Mt = Q^T (S_2/tau_1) Q).  Measured:
lam_min(B) = 0.679 O(1) ladder-wide, ALL classical certified bounds
on raw B negative on ALL steps (best max -88, cert/floor -130);
round-59 node DEFLATION: exact but zero leverage (relocation
+1.000); round-60 Christoffel node DAMPING: CERT-DEAD, cert/floor
-140..-154, failure frame-concentrated in ROW 0 of the co-block on
39/39; and the CRITICAL CONSTRAINT from b_christoffel_deflation:
the prime-free co-block B0 is NOT PD (min eigs -646..-2.1e6) -- a
naive real B_smooth^{-1/2} does not exist.

THE NODE CONGRUENCE (frozen).  Per step (r1, r2): the positive
reference measure is the completed positive family of the rung's
own chain (the mu_+ Lanczos data (al, be, m0) of case_edge /
christoffel_ratio -- xs, ws of the folded density); J_h = its Jacobi
matrix; y*_h = the per-rung classical node mapped to the spectral
variable, u* = (NODE_C + NODE_S alpha) alpha (node_origin declared
law), y* = cos(2 pi u* / (L D)).  The frozen T-variant list (all
source-only; NO tau, NO defect eigenvector, NO spectral data of the
TARGET B enters any T):
  T1  node-diagonal shift: T8 = Q^T diag(y_core - y*) Q, T = the
      7x7 co-block T8[1:, 1:] (the rank-structured version: T acts
      only on the co-block coordinates).  HONESTY NOTE (frozen a
      priori): the core folds j = 2..16 sit at y_j ~ 1 - O(j^2/L^2)
      -- all NEAR +1 -- while y* ~ 0.85, so diag(y_core - y*) is
      NEARLY SCALAR; T1 is expected to change the scale-invariant
      picture by little; measured anyway (the clean-negative
      candidate).
  T2  Jacobi-block shift in node coordinates: J8 = leading 8x8
      block of J_h (rung r2's own positive chain), Ec[j, i] =
      sqrt(v_core_j) p_i(y_core_j) (i < 8; the core evaluation
      matrix of the SAME chain), T_node = Ec (J8 - y* I) Ec^{-1},
      T8 = Q^T T_node Q, T = T8[1:, 1:].  cond(Ec) printed; the
      variant is typed UNUSABLE if cond(Ec) > COND_MAX (the core
      nodes cluster at +1 -- disclosed risk).
  T3  = T2 with the PRIME-FREE smooth companion chain (same kz;
      the round-60 V4 pattern: does prime-free damping content
      track the true one).
For each usable T: Bhat = T^{-T} B T^{-1} (so B = T^T Bhat T
EXACTLY by construction; wards = invertibility/conditioning +
round-trip + signature tie).  Measured per variant: lam_min(Bhat)
floor, certified best bound bg = max(G1, G2, G3)(Bhat), the
SCALE-INVARIANT cert/floor ratio (raw reference -130), cond, worst
scaled-Gershgorin row histogram, tau-screen of bg on the positive
subset (bands PASS |s| <= 0.30 / RELOC >= 0.70 / AMBIG).  TYPED:
Tk-CERT-ACHIEVED(min bg) / Tk-CERT-PARTIAL(n/N) / Tk-CERT-DEAD /
Tk-UNUSABLE(reason).

THE FALLBACK (frozen; the B0-not-PD constraint handled).  Per step:
B0 = co-block of Q^T (S_smooth,2 / tau_1) Q (smooth companion of
r2 in the SAME truth frame -- source-only: the prime-free model
consumes no truth spectral data; steps without a smooth core are
counted and skipped).
  F1  THE INDEX ANATOMY of B0: negidx(B0) per step; alignment of
      the negative eigenvector(s) with co-block row 0 (share of
      squared mass on coordinate 0, summed over the negative
      eigenspace) -- does the index sit where round 60 localized
      the failure?
  F2  |B0|-SYMMETRIZATION (the functional-calculus fix of the
      real-sqrt obstruction): |B0| = U |diag| U^T via eigh(B0)
      (source-only), Btil = |B0|^{-1/2} B |B0|^{-1/2} = I + K;
      measured: negidx(K) per step (NOT ||K||), margin
      1 + lam_min(K), certified G-battery on Btil, cert/floor.
      A PRIORI NOTE (frozen): |B0|^{-1/2} B0 |B0|^{-1/2} =
      sign(B0), so K ~ sign(B0) - I + (prime correction): the
      negative index of K is expected to REPRODUCE negidx(B0) --
      the measurement is whether it is a SMALL CONSTANT and where
      it sits.
  F2b THE POSITIVE COMPLETED MEASURE'S BLOCK (the alternative the
      constraint names): P_G = co-block of Q^T G_core Q with
      G_core[i, j] = sqrt(v_i v_j) sum_{k<h} p_k(y_i) p_k(y_j)
      (the CD-kernel Gram of the positive chain at the core nodes
      -- PD by construction, warded); Btil2 = P_G^{-1/2} B
      P_G^{-1/2} = I + K2; same measurements.
  F3  THE SMALL SCHUR REDUCTION (only meaningful if the index is
      small): split the co-block coordinates by the NEGATIVE
      eigenspace W- of B0 (dim r0; source-only frame): B is PD
      iff Bp = B|W+ is PD and the explicit r0 x r0 Schur
      complement S_small = B|W- - C^T Bp^{-1} C is PD.  Measured:
      certified bg(Bp) (G-battery; cert/floor vs lam_min(Bp)),
      the explicit S_small eigenvalues (= the incompressible
      margin; for r0 = 1 a scalar determinant), counts of steps
      where (bg(Bp) > 0) AND (S_small PD), and the tau-screen of
      min eig(S_small).  TYPED: SCHUR-REDUCED(r0 stats, counts,
      screen) / SCHUR-WIDE(negidx too large) -- an honest
      mechanism statement either way.

FROZEN PROTOCOL (pipeline verbatim from
bfloor_christoffel_congruence_probe = v900 chain; ONE Gram per
rung; window memoization):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2 >=
     30 full-core rungs; W3a truth all-PSD (A, R, S); W3b >= 20
     consecutive full-core steps; W4 REPRODUCTION P2/P3 ledger:
     min lam_min(B) == 0.679 (rtol 2e-2), gap min/med ==
     0.052/0.888 (rtol 5e-2), raw-B certified disaster (best bound
     < 0 on every step); W5 REPRODUCTION of the constraint: B0
     NOT PD on >= 30 of the usable steps (the round-59 finding
     this probe is built around).

 G1  CONGRUENCE WARDS (kill -> WARD-BROKEN): G1.a node mapping
     y* in (-1, 1) and min_j |y_core_j - y*| > 0 on every step;
     G1.b round-trip |B - T^T Bhat T| <= RT_WARD x ||B|| for every
     usable T; G1.c signature tie: eig sign counts of Bhat == of B
     on the first SIG_SPOT steps per usable variant (congruence
     cannot fake the floor); G1.d P_G PD on every step (positive
     chain Gram).

 G2  THE MEASUREMENT (typed as frozen above): T1/T2/T3, then
     F1/F2/F2b/F3.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) =
     0 everywhere; C1 smooth world neg(A) > 0 on >= 1 rung; C2
     Epstein x^2+5y^2 comb + scramble (seed 1) at kz 9 fire; C3
     the congruence cannot manufacture positivity on the scramble
     core where it exists (disclosed skip if the scramble core
     dies -- the signature ward G1.c carries the content on
     truth).

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
congruence / control wards (W4, W5, G1, C0-C3) -> WARD-BROKEN.
All G2-typed outcomes are measurements, never kills.

VERDICT (frozen enum): BFLOORNODE-MEASURED with typed sublabels
T1/T2/T3-CERT-<ACHIEVED | PARTIAL | DEAD | UNUSABLE>,
B0-NEGIDX(med/max, row0-share), PRECOND-NEGIDX(K: med/max; K2:
med/max), SCHUR-REDUCED(...) / SCHUR-WIDE(...), and the headline
CERTIFIED-BFLOOR-ACHIEVED / CERTIFIED-BFLOOR-FAILED(mechanism);
else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2);
NODE_C = 0.3727, NODE_S = -0.0116 (node_origin declared input);
COND_MAX = 1e12; RT_WARD = 1e-9; SIG_SPOT = 3; PG_TOL = 1e-12;
B0_MIN_DEAD = 30; SMALL_IDX = 2; SLOPE_PASS = 0.30; SLOPE_RELOC =
0.70; CTRL_KZ = 9; scramble seed 1.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign, no factorization of the TARGET B as a certificate --
every T, |B0|^{-1/2}, P_G^{-1/2} and the F3 splitting frame are
built from source-only data (positive chain, smooth world, node
law, deployed frame); eigh(B), eigh(Bhat), eigh(Btil) appear ONLY
as measured floors next to the certified bounds.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script (25/25 with the identical bars; NO bar, band,
count, rule or enum was moved after it; one separate diagnostic
snippet measured the T2/T3 death channel, recorded here) measured,
recorded as the honest context the frozen run must confirm --
INCLUDING one refuted a priori expectation, frozen as such:
pipeline + P2/P3 reproduction green; W5 constraint reproduced --
B0 NOT PD on 35/35 usable steps (4 steps lack a smooth core).
THE NODE CONGRUENCE IS A THIRD CLEAN NEGATIVE, with a new twist:
T1 is nearly scalar exactly as frozen (y* in [0.8628, 0.8866] vs
core span reaching [0.9857, 0.9998]; cert/floor med -150.6, the
round-60 picture; worst row STILL row 0 on 39/39; floor rescaled
to 46.4); T2/T3 are UNUSABLE on 39/39 -- the death channel is
cond(Ec) ~ 6e+17..1.7e+18 >> COND_MAX (diagnostic: the 8 core
nodes cluster so tightly at +1 that the 8-polynomial chain
evaluation matrix is numerically RANK-DEFICIENT in float; the
Jacobi-block node congruence cannot even be BUILT on this surface
-- a structural, not tuning, failure; disclosed risk fired).  THE
INDEX ANATOMY IS THE SHARP RESULT: negidx(B0) histogram
[0, 10, 19, 6] (med 2, max 3; min eig -2.1e+06..-4.7e+02), and
the negative eigenspace is NOT row-0-seated (row-0 share med
0.287 -- the B0 index and the round-60 cert-failure row are
DIFFERENT objects).  REFUTED EXPECTATION: the |B0|-route does NOT
reproduce sign(B0) -- the B0 SCALE dominates: Btil = I + K has
negidx(K) = 7 on 32/35 (med 7, i.e. ALL eigenvalues of Btil below
1, med floor 1+lam_min(K) = +0.002 in [0.001, 0.008] -- Btil PD
everywhere but scale-crushed), cert > 0 on 0/35 (best med
-3.3e-02).  The POSITIVE-BLOCK route is the honest surprise: P_G
PD on 39/39 (G1.d) and negidx(K2) = 0 on 37/39 (hist [37, 2]),
1 + lam_min(K2) med +6.13 -- B dominates the positive-chain CD
Gram co-block in the PSD order on 37/39 steps (MEASURED, not
certified: cert on Btil2 still dead, med -1.3e+03).  F3 SCHUR
REDUCTION (r0 <= 2 on 29/35): the certified half bg(Bp) > 0 on
1/29 with cert/floor med -11.5 (an order better than raw -130,
still dead); the explicit half S_small PD on 29/29 (min eig
1.02, med 37.5; screen PASS(+0.060, R^2 0.002) --
tau-DEcorrelated O(1) incompressible margin).  MECHANISM: the
obstruction is NOT the B0 index (small, repairable, off-row-0);
it is the row-0 coherent mass of rounds 58-60, and it sits in
the POSITIVE part Bp.  Headline CERTIFIED-BFLOOR-FAILED.
Controls: smooth neg(A) > 0 on 42/42, Epstein neg(A) = 55,
scramble neg(A) = 37, scramble core dead -> C3 disclosed skip.
Fail-first preserved: nothing was weakened; all typed outcomes
are measurements.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as P2
SPEC (ii); (iii) chains via keep_chain, J8/Ec from rung r2's own
chain (T3: the smooth companion's chain of the same kz), y* from
rung r2's (alpha, L, D); (iv) |B0|^{-1/2} and P_G^{-1/2} via eigh
of the source-only matrix (absolute values / positive roots);
(v) OLS population statistics as v900; screens read positive
subsets with excluded counts printed; (vi) negidx = count of
eigenvalues < 0 (float sign, no tolerance).

NO-GO COMPLIANCE (frozen): the G-battery on RAW B enters ONLY as
the W4 reproduction; the battery on Bhat/Btil/Bp is allowed
because every congruence/preconditioner/split is NEW and
source-only; no rank-1 approximation of the core update; no plain
Herglotz certificate; no fit where an identity is claimed.

NO RH claim: a certified floor would certify single deployed steps
only (with the explicit gap half); nothing here proves
B-uniformity, wall positivity for all h, or any tail statement.
No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core
machinery verbatim from bfloor_christoffel_congruence_probe.py /
b_christoffel_deflation_probe.py / port_tangent_schur_probe.py
(rounds 58-60) = v900 chain; node law from node_origin_arch_probe
(declared input); positive completed family from
case_edge_christoffel_probe (declared input).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/bfloor_node_congruence_probe.py
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
MIN_STEPS = 20
MINB_REF = 0.679
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
NODE_C = 0.3727
NODE_S = -0.0116
COND_MAX = 1e12
RT_WARD = 1e-9
SIG_SPOT = 3
PG_TOL = 1e-12
B0_MIN_DEAD = 30
SMALL_IDX = 2
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


# --------------- pipeline, verbatim (bfloor_christoffel_congruence)
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


def worst_gersh_row(B):
    d = np.diag(B)
    s = 1.0 / np.sqrt(np.maximum(d, 1e-300))
    C = B * np.outer(s, s)
    r = np.sum(np.abs(C), axis=1) - np.abs(np.diag(C))
    return int(np.argmax(r))


def inv_sqrt_abs(B):
    """|B|^{-1/2} via eigh -- source-only functional calculus."""
    w, U = np.linalg.eigh(B)
    aw = np.abs(w)
    if float(np.min(aw)) <= 0.0:
        return None
    return (U / np.sqrt(aw)) @ U.T


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


def main():
    section("PRIME.PORT.BFLOOR.CONGRUENCE.03 -- the wandering-node "
            "Jacobi congruence + the B0-index fallback "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + P2/P3 reproduction + the B0 "
            "constraint")
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
        # B0: smooth companion of r2 in the SAME truth frame
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
    usable = [w for w in rows if w["B0"] is not None]
    negidx0 = [int(np.sum(np.linalg.eigvalsh(w["B0"]) < 0.0))
               for w in usable]
    n_dead0 = sum(1 for k in negidx0 if k > 0)
    check("W5 REPRODUCTION the B0 constraint: B0 NOT PD on %d/%d "
          "usable steps (>= %d; %d steps without smooth core)"
          % (n_dead0, len(usable), B0_MIN_DEAD,
             len(rows) - len(usable)),
          n_dead0 >= B0_MIN_DEAD, kill="K2")

    # ------------------------------------------------------------ G1
    section("G1 -- congruence wards + the node mapping")
    ystars = []
    ok_node = True
    for w in rows:
        r2 = w["r2"]
        ustar = (NODE_C + NODE_S * r2["alpha"]) * r2["alpha"]
        yst = math.cos(2.0 * math.pi * ustar
                       / (r2["L"] * r2["D"]))
        w["ystar"] = yst
        ystars.append(yst)
        yc = w["r2"]["y_core"] if "y_core" in w["r2"] else None
        if yc is None:
            ok_node = False
            continue
        ok_node &= (-1.0 < yst < 1.0
                    and float(np.min(np.abs(yc - yst))) > 0.0)
    yc0 = rows[0]["r2"]["y_core"]
    check("G1.a WARD node mapping: y* in (-1, 1) and off the core "
          "nodes on every step (y* range [%.4f, %.4f]; core span "
          "example [%.4f, %.4f])"
          % (min(ystars), max(ystars), float(np.min(yc0)),
             float(np.max(yc0))), ok_node, kill="K2")

    # build the T-variants per step
    VAR = ("T1", "T2", "T3")
    var_rows = {v: [] for v in VAR}
    rt_dev = 0.0
    sig_ok = True
    condec = {"T2": [], "T3": []}
    n_unus = {v: 0 for v in VAR}
    for irow, w in enumerate(rows):
        r2 = w["r2"]
        Q, B, yst = w["Q"], w["B"], w["ystar"]
        yc = r2["y_core"]
        vc = r2["v_core"]
        for v in VAR:
            if v == "T1":
                T8 = Q.T @ np.diag(yc - yst) @ Q
            else:
                if v == "T2":
                    ch = r2.get("chain")
                else:
                    smr = sm_map.get(r2["kz"])
                    ch = (smr or {}).get("chain")
                    if ch is not None and not smr.get("core_ok",
                                                      False):
                        pass
                if ch is None:
                    n_unus[v] += 1
                    continue
                al, be, m0 = ch
                if len(al) < 8 or len(be) < 7:
                    n_unus[v] += 1
                    continue
                J8 = (np.diag(al[:8])
                      + np.diag(be[:7], 1) + np.diag(be[:7], -1))
                P8 = eval_chain(al, be, m0, yc, 8)
                Ec = np.sqrt(vc)[:, None] * P8
                cE = float(np.linalg.cond(Ec))
                condec[v].append(cE)
                if cE > COND_MAX:
                    n_unus[v] += 1
                    continue
                Tn = Ec @ (J8 - yst * np.eye(8)) @ np.linalg.inv(Ec)
                T8 = Q.T @ Tn @ Q
            T = T8[1:, 1:]
            cT = float(np.linalg.cond(T))
            if not np.isfinite(cT) or cT > COND_MAX:
                n_unus[v] += 1
                continue
            Ti = np.linalg.inv(T)
            Bhat = Ti.T @ B @ Ti
            Bhat = 0.5 * (Bhat + Bhat.T)
            rt = float(np.linalg.norm(B - T.T @ Bhat @ T)
                       / max(np.linalg.norm(B), 1e-300))
            rt_dev = max(rt_dev, rt)
            evh = np.linalg.eigvalsh(Bhat)
            if irow < SIG_SPOT:
                evb = np.linalg.eigvalsh(B)
                sig_ok &= (int(np.sum(evh > 0))
                           == int(np.sum(evb > 0)))
            var_rows[v].append(dict(
                tau=w["tau"], minBh=float(evh[0]),
                bg=best_cert(Bhat), cond=float(np.linalg.cond(
                    Bhat)), wrow=worst_gersh_row(Bhat)))
    check("G1.b WARD round-trip B == T^T Bhat T on every usable "
          "T: max rel dev %.2e <= %.0e" % (rt_dev, RT_WARD),
          rt_dev <= RT_WARD, kill="K2")
    check("G1.c WARD signature tie on %d spot steps per usable "
          "variant" % SIG_SPOT, sig_ok, kill="K2")

    # ------------------------------------------------------------ G2
    section("G2a -- the node congruences T1/T2/T3")
    labels = {}
    for v in VAR:
        rowsv = var_rows[v]
        if not rowsv:
            labels[v] = "%s-UNUSABLE(%d dead)" % (v, n_unus[v])
            check("G2.%s typed: %s" % (v, labels[v]), True)
            continue
        bg = np.array([x["bg"] for x in rowsv])
        mb = np.array([x["minBh"] for x in rowsv])
        tt = np.array([x["tau"] for x in rowsv])
        relg = bg / np.maximum(mb, 1e-300)
        scr_lab, _sl = screen(bg, tt)
        wr = np.bincount([x["wrow"] for x in rowsv], minlength=7)
        n_pos = int(np.sum(bg > 0))
        extra = ""
        if v in condec and condec[v]:
            extra = ("; cond(Ec) med %.1e max %.1e"
                     % (float(np.median(condec[v])),
                        float(np.max(condec[v]))))
        print("  %s: certified > 0 on %d/%d (unusable %d); best "
              "bound min/med %+.2e/%+.2e; floor lam_min(Bhat) min "
              "%.3e; SCALE-INVARIANT cert/floor med %+.1f (raw "
              "-130); cond(Bhat) med %.1f; worst-row hist %s; "
              "screen %s%s"
              % (v, n_pos, len(rowsv), n_unus[v], float(np.min(
                  bg)), float(np.median(bg)), float(np.min(mb)),
                 float(np.median(relg)),
                 float(np.median([x["cond"] for x in rowsv])),
                 wr.tolist(), scr_lab, extra), flush=True)
        if n_pos == len(rowsv):
            labels[v] = "%s-CERT-ACHIEVED(min=%.3e)" % (
                v, float(np.min(bg)))
        elif n_pos > 0:
            labels[v] = "%s-CERT-PARTIAL(%d/%d)" % (v, n_pos,
                                                    len(rowsv))
        else:
            labels[v] = "%s-CERT-DEAD(rel=%+.1f)" % (
                v, float(np.median(relg)))
        check("G2.%s typed: %s" % (v, labels[v]), True)

    section("G2b -- the fallback: B0 index anatomy + "
            "preconditioners + small Schur reduction")
    # F1: index anatomy of B0
    idx_rows = []
    for w in usable:
        ev0, U0 = np.linalg.eigh(w["B0"])
        neg = ev0 < 0.0
        r0 = int(np.sum(neg))
        share0 = (float(np.sum(U0[0, neg] ** 2)) if r0 > 0
                  else float("nan"))
        idx_rows.append(dict(w=w, r0=r0, ev0=ev0, U0=U0,
                             share0=share0, tau=w["tau"]))
    r0s = np.array([x["r0"] for x in idx_rows])
    sh0 = np.array([x["share0"] for x in idx_rows
                    if np.isfinite(x["share0"])])
    f1 = ("B0-NEGIDX(med=%.0f, max=%d, row0-share med %.3f)"
          % (float(np.median(r0s)), int(np.max(r0s)),
             float(np.median(sh0)) if len(sh0) else float("nan")))
    print("    negidx(B0) histogram: %s; min eig(B0) range "
          "[%.1e, %.1e]; negative-eigenspace row-0 share med %.3f"
          % (np.bincount(r0s).tolist(),
             float(np.min([x["ev0"][0] for x in idx_rows])),
             float(np.max([x["ev0"][0] for x in idx_rows])),
             float(np.median(sh0)) if len(sh0) else float("nan")))
    check("F1 typed: %s -- does the index sit on the round-60 "
          "row 0?" % f1, True)
    # F2: |B0| symmetrization
    ki, marg, bgt = [], [], []
    for x in idx_rows:
        Sm = inv_sqrt_abs(x["w"]["B0"])
        if Sm is None:
            continue
        Bt = Sm @ x["w"]["B"] @ Sm
        Bt = 0.5 * (Bt + Bt.T)
        evK = np.linalg.eigvalsh(Bt - np.eye(7))
        ki.append(int(np.sum(evK < 0.0)))
        marg.append(1.0 + float(evK[0]))
        bgt.append(best_cert(Bt))
    ki = np.array(ki)
    f2 = ("PRECOND-NEGIDX-K(med=%.0f, max=%d; margin med %+.3f; "
          "cert>0 on %d/%d)"
          % (float(np.median(ki)), int(np.max(ki)),
             float(np.median(marg)), int(np.sum(np.array(bgt) >
                                               0)), len(ki)))
    print("    |B0|-route: negidx(K) hist %s; 1+lam_min(K) med "
          "%+.3f range [%.3f, %.3f]; certified best on Btil "
          "min/med %+.2e/%+.2e"
          % (np.bincount(ki).tolist(), float(np.median(marg)),
             float(np.min(marg)), float(np.max(marg)),
             float(np.min(bgt)), float(np.median(bgt))))
    check("F2 typed: %s" % f2, True)
    # F2b: positive completed measure's block
    k2i, marg2, bgt2 = [], [], []
    pg_ok = True
    for w in rows:
        r2 = w["r2"]
        ch = r2.get("chain")
        if ch is None:
            continue
        al, be, m0 = ch
        Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
        Gc = (np.sqrt(r2["v_core"])[:, None] * (Pc @ Pc.T)
              * np.sqrt(r2["v_core"])[None, :])
        Gc = 0.5 * (Gc + Gc.T)
        PG = (w["Q"].T @ Gc @ w["Q"])[1:, 1:]
        PG = 0.5 * (PG + PG.T)
        evg = np.linalg.eigvalsh(PG)
        if float(evg[0]) <= PG_TOL:
            pg_ok = False
            continue
        Sm = inv_sqrt_abs(PG)
        Bt = Sm @ w["B"] @ Sm
        Bt = 0.5 * (Bt + Bt.T)
        evK = np.linalg.eigvalsh(Bt - np.eye(7))
        k2i.append(int(np.sum(evK < 0.0)))
        marg2.append(1.0 + float(evK[0]))
        bgt2.append(best_cert(Bt))
    check("G1.d WARD P_G (positive-chain CD Gram co-block) PD on "
          "every step", pg_ok, kill="K2")
    k2i = np.array(k2i)
    f2b = ("PRECOND-NEGIDX-K2(med=%.0f, max=%d; cert>0 on %d/%d)"
           % (float(np.median(k2i)), int(np.max(k2i)),
              int(np.sum(np.array(bgt2) > 0)), len(k2i)))
    print("    P_G-route: negidx(K2) hist %s; 1+lam_min(K2) med "
          "%+.3f; certified best on Btil2 min/med %+.2e/%+.2e"
          % (np.bincount(k2i).tolist(), float(np.median(marg2)),
             float(np.min(bgt2)), float(np.median(bgt2))))
    check("F2b typed: %s" % f2b, True)
    # F3: small Schur reduction in the B0 negative eigenframe
    small = [x for x in idx_rows if 0 < x["r0"] <= SMALL_IDX]
    if len(small) < len(idx_rows) // 2:
        f3 = ("SCHUR-WIDE(negidx > %d on %d/%d steps)"
              % (SMALL_IDX, len(idx_rows) - len(small),
                 len(idx_rows)))
        check("F3 typed: %s" % f3, True)
        ssc_lab = "n/a"
    else:
        bgp, ssm, taus3, okred = [], [], [], 0
        relp = []
        for x in small:
            w = x["w"]
            neg = x["ev0"] < 0.0
            Um = x["U0"][:, neg]
            Up = x["U0"][:, ~neg]
            Bp = Up.T @ w["B"] @ Up
            Bp = 0.5 * (Bp + Bp.T)
            Bm = Um.T @ w["B"] @ Um
            Cx = Up.T @ w["B"] @ Um
            Ss = Bm - Cx.T @ np.linalg.solve(Bp, Cx)
            Ss = 0.5 * (Ss + Ss.T)
            evs = np.linalg.eigvalsh(Ss)
            bgp.append(best_cert(Bp))
            relp.append(best_cert(Bp)
                        / max(float(np.linalg.eigvalsh(Bp)[0]),
                              1e-300))
            ssm.append(float(evs[0]))
            taus3.append(w["tau"])
            if best_cert(Bp) > 0 and float(evs[0]) > 0:
                okred += 1
        ssm = np.array(ssm)
        bgp = np.array(bgp)
        ssc_lab, _sl = screen(ssm, taus3)
        print("    F3 (r0 <= %d on %d/%d): certified bg(Bp) > 0 "
              "on %d/%d (cert/floor med %+.1f); S_small min eig "
              "> 0 on %d/%d (min %.2e, med %.2e); BOTH on %d/%d; "
              "S_small screen %s"
              % (SMALL_IDX, len(small), len(idx_rows),
                 int(np.sum(bgp > 0)), len(small),
                 float(np.median(relp)),
                 int(np.sum(ssm > 0)), len(small),
                 float(np.min(ssm)), float(np.median(ssm)),
                 okred, len(small), ssc_lab))
        f3 = ("SCHUR-REDUCED(r0<=%d on %d/%d; cert-half %d/%d; "
              "explicit-half %d/%d; screen %s)"
              % (SMALL_IDX, len(small), len(idx_rows),
                 int(np.sum(bgp > 0)), len(small),
                 int(np.sum(ssm > 0)), len(small), ssc_lab))
        check("F3 typed: %s" % f3, True)
    n_ach = sum(1 for v in VAR if "ACHIEVED" in labels.get(v, ""))
    headline = ("CERTIFIED-BFLOOR-ACHIEVED(%d)" % n_ach if n_ach
                else "CERTIFIED-BFLOOR-FAILED(node congruence + "
                "index fallback both leave the certified half "
                "dead)")
    check("G2.h typed headline: %s" % headline, True)

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
    rsc = ctl["scramble"]
    c3_ok = True
    c3_msg = "scramble core dead -> skipped (disclosed)"
    if isinstance(rsc, dict) and rsc.get("core_ok") \
            and "S" in rsc and rsc["lamS"] < 0.0:
        yc = rsc["y_core"]
        Dm = np.diag(yc - float(np.mean(yc)) + 0.15)
        St = Dm @ rsc["S"] @ Dm
        lam_t = float(np.linalg.eigvalsh(0.5 * (St + St.T))[0])
        c3_ok = lam_t < 0.0
        c3_msg = ("lam_min(S_scr) %.3e -> congruence keeps it "
                  "negative (%.3e)" % (rsc["lamS"], lam_t))
    check("C3 WARD congruence cannot manufacture positivity on "
          "the scramble: %s" % c3_msg, c3_ok, kill="K2")

    labels["headline"] = headline
    labels["f1"] = f1
    labels["f2"] = f2
    labels["f2b"] = f2b
    labels["f3"] = f3
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
        VERDICT = ("BFLOORNODE-MEASURED / %s / %s / %s / %s / %s "
                   "/ %s / %s"
                   % (labels.get("T1", "-"), labels.get("T2", "-"),
                      labels.get("T3", "-"), labels.get("f1", "-"),
                      labels.get("f2", "-"),
                      labels.get("f3", "-"),
                      labels.get("headline", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): every congruence/preconditioner here
  is source-only and signature-preserving -- it cannot fake the
  wall and cannot lose it; the question is whether classical
  certificates SEE the O(1) floor in the new coordinates, and
  where the incompressible mass sits.  A third clean negative
  with a sharp mechanism (the index anatomy) is a first-class
  outcome.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
