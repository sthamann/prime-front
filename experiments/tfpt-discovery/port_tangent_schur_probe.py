#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_tangent_schur_probe -- PRIME.PORT.TANGENT.SCHUR.01
(EXPLORATION ONLY, experiments/; round 57: the full normalized
update M_h = X_h + U_h in Schur tangent coordinates along the
soft/critical direction -- two scalars n_h, q_h carry the
positivity, and the v900 rank-1 failure is located in them.
2026-08-10.)

THE QUESTION (frozen).  v900 (PRIME.PORT.NORMALIZED.CORE.01 +
PRIME.PORT.GRAPH.REGION.01) proved the exact update X' = c (X + U)
and registered the honest negative: the dominant U-mode M1 (97.5
percent of the U-energy) is PSD, and the rank-1 surrogate
U ~ alpha M1 is margin-negative at 12 of 39 transitions where the
TRUE update stays positive -- the positivity is carried by the
2.5-percent off-mode.  This probe splits the full update matrix
M_h := X_h + U_h  (exact: M_h = S_{h+1}/tau_h)
along the CURRENT soft/critical direction v_h (the lambda_min
eigenvector of S_h -- backward-only spectral data of rung h) into
    Q_h = [v_h, W_h] orthonormal,   M = [[n, b^T], [b, B]]
(n = v^T M v scalar, b = W^T M v, B = W^T M W the 7x7 co-block)
and verifies EXACTLY: if B > 0 then  M > 0  <=>  n - q > 0  with
q = b^T B^{-1} b (Schur), equivalently n - q = 1/(v^T M^{-1} v)
and det M = (n - q) det B.  Measured across ALL transitions:
(a) the SAFE-BLOCK premise -- min eig(B_h) ladder-wide; (b) the
two scalars n_h, q_h and the gap n - q; (c) the rank-1 diagnosis
RELOCATED into the scalars: at the 12 v900-failing transitions,
what do n, q of the surrogate do, and which part of q the
off-mode enters (linear vs quadratic anatomy); (d) the scalars as
SOURCE-ONLY functionals: n_h ell_h = v_h^T S_{h+1} v_h and
q_h ell_h = (W^T S_{h+1} v)^T (W^T S_{h+1} W)^{-1} (W^T S_{h+1} v)
with ell = det(S_h)^{1/8} -- the P1 winner normalization
(PRIME.PORT.SIGNFREE.NORMALIZATION.01, DECIRC-ACHIEVED(ELL-B)):
every ingredient is comb linear algebra at rungs h and h+1 plus
backward spectral data; NO tau_{h+1}, NO forward wall sign enters
-- the sign of the gap is an OUTPUT.

COORDINATES (frozen): the primary tables are in v900's original
X-coordinates (M_X = X + U = S'/tau_h; comparison to the printed
v900 ledger); the sign-free reading M_Y = Y + V = S'/ell_h is
tied to it by the EXACT scaling (n - q)_Y = (n - q)_X (tau_h /
ell_h), warded, and its gap ladder is printed in summary.

FROZEN PROTOCOL (2026-08-10; machinery verbatim from
normalized_core_update_probe / core_graph_region_probe, round
55/56; gram_anatomy extended by tr(R), sum(v) as in P1):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2
     >= 30 full-core rungs; W3 all-PSD + >= 20 steps; W4 deepcore
     product law <= 1e-6; W5 eta floor 0.0315 (tol 5.001e-5); W6
     exact update ||X' - c(X+U)|| <= 1e-10 and c range [0.051,
     19.50] (rtol 2e-2); W7 u-anatomy: k95 == 1 and top-mode
     share >= 0.90 (v900 printed 0.975).

 T1  THE EXACT SCHUR IDENTITIES (per step; kill -> WARD-BROKEN):
       T1.a  M_X == S_{h+1}/tau_h, rel <= MID_WARD = 1e-12;
       T1.b  det M == (n - q) det B, rel <= DET_WARD = 1e-10
             (slogdet route), on steps with B PD;
       T1.c  n - q == 1/(v^T M^{-1} v), rel <= PIV_WARD = 1e-9;
       T1.d  PD(M) (eigvalsh) <=> (B PD and n - q > 0), exact
             boolean agreement on every step;
       T1.e  SCALING: (n-q)_Y == (n-q)_X (tau_h/ell_h), rel <=
             SCL_WARD = 1e-10 (ell = det(S_h)^{1/8}, P1 winner).

 T2  THE SAFE-BLOCK PREMISE (measured, typed): min eig(B_h) over
     all steps, the ladder printed, plus the exposure ratio
     mineig(B_h)/lam_min(M_h) per step (how much safer the
     co-block is than the whole).  TYPED: SAFEBLOCK(minB) iff B_h
     PD on every step, else SAFEBLOCK-BROKEN(count).

 T3  THE TWO SCALARS (measured, typed): full ladder n_h, q_h,
     gap_h = n_h - q_h (X-coordinates), gap ladder in Y printed
     in summary; consistency print: gap > 0 on every step is
     EQUIVALENT (T1.d, B PD) to the known truth positivity --
     no new positivity is claimed.  TYPED: GAP(min, med).

 T4  THE RANK-1 DIAGNOSIS IN THE SCALARS (the v900 negative,
     relocated): frozen mode M1 = unvec36 of the top right
     singular vector of {vec36(U_h)} (sign: mean <U, M1> >= 0),
     alpha_h = <U_h, M1>_F; surrogate margins c_h (1 +
     lam_min(X^{-1/2} (alpha M1) X^{-1/2})).  WARD (kill ->
     WARD-BROKEN): the count of margin-negative surrogate steps
     == RK1_NEG_REF = 12 of 39 (v900/graph-region printed
     ledger).  At each failing step split the surrogate M_s = X +
     alpha M1 in the SAME frozen basis: n_s, q_s, gap_s, min
     eig(B_s); print the table true-vs-surrogate.  TWO ANATOMY
     BRANCHES (both frozen; which one carries data is measured):
     (q-branch, for failing steps with B_s PD) with db = W^T
     U_perp v, dB = W^T U_perp W, U_perp = U - alpha M1,
       n_t - n_s = v^T U_perp v                      [n-shift]
       q_mix := b_t^T B_s^{-1} b_t;
       q_t - q_s = [2 b_s^T B_s^{-1} db + db^T B_s^{-1} db]
                   (pure b-change at frozen B_s: linear +
                    QUADRATIC parts printed separately)
                 + [q_t - q_mix]  (B-change part),
     warded to recompose (rel <= RES_WARD = 1e-9);
     (B-branch, for failing steps with B_s NOT PD) the co-block
     restoration is LINEAR in the off-mode: B_t = B_s + dB;
     print min eig(B_s), min eig(B_t), the lift along the failing
     direction w_s (the B_s-soft unit vector): w_s^T dB w_s and
     w_s^T B_t w_s, and the co-block sizes ||dB||_F vs
     ||W^T (alpha M1) W||_F.  THE FRAME-INVARIANT SEAT: per
     failing step the most-negative eigenvector z of M_s and its
     overlap <z, v_h>^2 with the current soft direction -- where
     does the rank-1 truncation destroy positivity?  TYPED
     (frozen rules): RESCUE-IN-GAP iff at EVERY failing step B_s
     stays PD and gap_s <= 0 < gap_t; else RESCUE-MIXED(nB,
     ngap).  OFFMODE-IN-Q iff median |q_t - q_s| > median |n_t -
     n_s| over the q-branch steps, OFFMODE-IN-N if the reverse,
     OFFMODE-IN-B iff the q-branch is EMPTY (all failures in the
     co-block).  FAILSEAT-COBLOCK / FAILSEAT-SOFT /
     FAILSEAT-MIXED: median overlap <z, v_h>^2 < 0.5 / >= 0.5 /
     bimodal (any step on the other side of the bar), bar frozen
     at OVL_BAR = 0.5.

 T5  SOURCE-ONLY EXPRESSIONS (kill -> WARD-BROKEN): per step
     verify n ell == v^T S' v and q ell == (W^T S' v)^T (W^T S'
     W)^{-1} (W^T S' v) (rel <= SRC_WARD = 1e-10), ell =
     det(S_h)^{1/8}; the honest statement printed: v_h, W_h are
     rung-h spectral data (backward), S' is comb linear algebra
     at rung h+1, ell is source-only (P1) -- no forward sign
     enters the EXPRESSIONS; their positivity is the output.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) =
     0 everywhere; C1 smooth world: neg(A) > 0 on >= 1 rung AND
     the tangent machinery exits on >= 1 smooth full-core rung
     (S not PSD or B-block not PD or gap <= 0 at the smooth
     step); C2 Epstein + scramble (seed 1) at kz 9 fire (neg(A)
     > 0 or chain death).

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
identity / control wards (W4-W7, T1, T4-count, T5, C0-C2) ->
WARD-BROKEN.  T2/T3/T4 typed outcomes are measurements.

VERDICT (frozen enum): TANGENTSCHUR-MEASURED with typed sublabels
SAFEBLOCK(minB) / SAFEBLOCK-BROKEN(count), GAP(min, med),
RESCUE-IN-GAP / RESCUE-MIXED(nB, ngap), OFFMODE-IN-Q /
OFFMODE-IN-N / OFFMODE-IN-B, FAILSEAT-COBLOCK / FAILSEAT-SOFT /
FAILSEAT-MIXED; else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; REPRO_PROD_BAR = 1e-6;
REPRO_ETA_MIN = 0.0315; ROUND_TOL = 5.001e-5; XUPD_WARD = 1e-10;
C_RANGE_REF = [0.051, 19.50] (rtol 2e-2); K95_EXP = 1;
M1_SHARE_BAR = 0.90; RK1_NEG_REF = 12; MID_WARD = 1e-12; DET_WARD
= 1e-10; PIV_WARD = 1e-9; SCL_WARD = 1e-10; RES_WARD = 1e-9;
SRC_WARD = 1e-10; OVL_BAR = 0.5; CTRL_KZ = 9; scramble seed 1.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): the smoke run
of this script (26/26 with identical wards) REFUTED the incoming
expectation and reshaped ONLY the T4 anatomy branches, before the
freeze: the incoming plan expected the rank-1 failure to live in
the scalars (gap_s <= 0 with B_s PD -- "the off-mode enters q
quadratically and rescues the sign"); the smoke run measured
instead that at ALL 12 failing steps the surrogate CO-BLOCK B_s
itself loses PD (min eig down to ~ -364 while the true co-block
floor stays ~ +0.68) -- the q-branch was EMPTY.  In response the
B-branch anatomy and the frame-invariant FAILSEAT overlap
measurement were ADDED to the spec (above) before freezing; no
ward, bar, count or enum of the original protocol was weakened,
and the refuted expectation is recorded here as the honest
outcome to be confirmed by the frozen run.  All frozen constants
are v900/graph-region printed-ledger values and exact-identity
bars.  P1's winner normalization (ELL-B, det-core) is a declared
input from the recorded P1 run of the same day.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1:
(i) window memoization per (kz, seed); (ii) the orthonormal
completion W_h is the Householder frame mapping e_1 -> v_h
(deterministic); (iii) dead steps for T1.b/T5 (B or B_src not PD)
are excluded from the rel-dev max and COUNTED (printed); (iv)
slopes/statistics as in v900; (v) the failing-step table prints
all 12 rows; (vi) vec36 Frobenius-isometric as in v900.

NO RH claim: the Schur split is exact finite linear algebra on
the deployed v563 window ladder; the gap ladder is a measurement,
its positivity for all h is NOT proved (equivalent to the wall);
no marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
exact-update machinery verbatim from normalized_core_update_probe
.py (round 55, promoted v900); rank-1 surrogate construction
verbatim from core_graph_region_probe.py (round 56, promoted
v900); sign-free normalization from
port_signfree_normalization_probe.py (P1, round 57, declared
input); certified base v884/v887/v897 -- declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_tangent_schur_probe.py
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
REPRO_PROD_BAR = 1e-6
REPRO_ETA_MIN = 0.0315
ROUND_TOL = 5.001e-5
XUPD_WARD = 1e-10
C_MIN_REF, C_MAX_REF = 0.051, 19.50
C_RANGE_RTOL = 2e-2
K95_EXP = 1                    # W7 (v900)
M1_SHARE_BAR = 0.90            # W7 (v900 printed 0.975)
U_ENERGY = 0.95
RK1_NEG_REF = 12               # T4 (v900/graph-region ledger)
MID_WARD = 1e-12               # T1.a
DET_WARD = 1e-10               # T1.b
PIV_WARD = 1e-9                # T1.c
SCL_WARD = 1e-10               # T1.e
RES_WARD = 1e-9                # T4 recomposition
SRC_WARD = 1e-10               # T5
OVL_BAR = 0.5                  # T4 FAILSEAT overlap bar
CTRL_KZ = 9
R_SING_TOL_REL = 1e-10
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


# --------------- pipeline, verbatim (normalized_core_update_probe)
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
                 want_vec=False):
    """v900 verbatim wall + fixed-core split (P1 extension)."""
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
    out = dict(kz=kz, h=h, n=n, alpha=float(alpha))
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
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["lamR"] = float(evR[0])
    out["negR"] = int(np.sum(evR < 0.0))
    out["Rsing"] = bool(float(np.min(np.abs(evR)))
                        < R_SING_TOL_REL
                        * float(np.max(np.abs(evR))))
    Z = np.linalg.solve(R, Xc.T)
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["lamSmax"] = float(evS[-1])
    out["negS"] = int(np.sum(evS < 0.0))
    if want_vec:
        v = VA[:, 0]
        out["wcore"] = float(np.sum(v[ic] ** 2))
    return out


_NCORE = len(CORE_J)
_TRIU = [(i, j) for i in range(_NCORE) for j in range(i, _NCORE)]
_SQ2 = math.sqrt(2.0)


def vec36(M):
    return np.array([M[i, j] * (1.0 if i == j else _SQ2)
                     for (i, j) in _TRIU])


def unvec36(v):
    M = np.zeros((_NCORE, _NCORE))
    for k, (i, j) in enumerate(_TRIU):
        if i == j:
            M[i, i] = v[k]
        else:
            M[i, j] = M[j, i] = v[k] / _SQ2
    return M


def inv_sqrt(M):
    w, V = np.linalg.eigh(M)
    return V @ np.diag(w ** -0.5) @ V.T


def householder_frame(v):
    """SPEC (ii): deterministic orthonormal Q with Q[:, 0] = v
    (Householder mapping e_1 -> v)."""
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
    # columns: Q e_1 = v exactly (reflection)
    if float(Q[:, 0] @ v) < 0:
        Q = -Q
    return Q


def schur_scalars(Mm, Q):
    """(n, b, B, q or None, gap or None, B_pd) in the frame Q."""
    Mt = Q.T @ Mm @ Q
    Mt = 0.5 * (Mt + Mt.T)
    nsc = float(Mt[0, 0])
    b = Mt[1:, 0].copy()
    B = Mt[1:, 1:].copy()
    evB = np.linalg.eigvalsh(B)
    B_pd = float(evB[0]) > 0.0
    if not B_pd:
        return nsc, b, B, None, None, False, float(evB[0])
    q = float(b @ np.linalg.solve(B, b))
    return nsc, b, B, q, nsc - q, True, float(evB[0])


def ell_det(S):
    sg, ld = np.linalg.slogdet(S)
    return math.exp(ld / 8.0) if sg == 1.0 else None


def main():
    section("PRIME.PORT.TANGENT.SCHUR.01 -- the update in Schur "
            "tangent coordinates (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + v900 reproduction wards")
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
    check("W1c all tau finite",
          all(np.isfinite(r["tau"]) for r in truth), kill="K1")
    full = [r for r in truth if r["core_ok"]]
    check("W2 >= %d full-core rungs" % MIN_CORE_RUNGS,
          len(full) >= MIN_CORE_RUNGS,
          "%d full-core rungs" % len(full), kill="K1")
    ok_psd = all(r["negA"] == 0 and r["negR"] == 0
                 and r["negS"] == 0 for r in full)
    check("W3a WARD truth all-PSD (A, R, S)", ok_psd, kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})
    prods = np.array([r["lamS"] * r["wcore"] / r["tau"]
                      for r in full])
    prod_dev = float(np.max(np.abs(prods - 1.0)))
    check("W4 REPRODUCTION deepcore product law %.3e <= %.0e"
          % (prod_dev, REPRO_PROD_BAR), prod_dev <= REPRO_PROD_BAR,
          kill="K2")
    steps = []
    for r1, r2 in zip(truth, truth[1:]):
        if (r1 is None or r2 is None or not r1.get("core_ok")
                or not r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
        steps.append((r1, r2))
    check("W3b >= %d consecutive full-core steps" % MIN_STEPS,
          len(steps) >= MIN_STEPS, "%d steps" % len(steps),
          kill="K1")
    etas = []
    for r1, r2 in steps:
        Wi = inv_sqrt(r1["S"])
        etas.append(float(np.linalg.eigvalsh(
            Wi @ r2["S"] @ Wi)[0]))
    eta_min = float(np.min(etas))
    check("W5 REPRODUCTION eta floor %.4f == %.4f (tol %.1e)"
          % (eta_min, REPRO_ETA_MIN, ROUND_TOL),
          abs(eta_min - REPRO_ETA_MIN) <= ROUND_TOL, kill="K2")
    for r in full:
        r["X"] = r["S"] / r["tau"]
    xrec_dev = 0.0
    u_list = []
    for r1, r2 in steps:
        c = r1["tau"] / r2["tau"]
        U = (r2["S"] - r1["S"]) / r1["tau"]
        xr = (float(np.linalg.norm(c * (r1["X"] + U) - r2["X"]))
              / max(float(np.linalg.norm(r2["X"])), 1e-300))
        xrec_dev = max(xrec_dev, xr)
        u_list.append((c, U))
    cs = np.array([c for (c, _U) in u_list])
    ok_crange = (abs(float(np.min(cs)) / C_MIN_REF - 1.0)
                 <= C_RANGE_RTOL
                 and abs(float(np.max(cs)) / C_MAX_REF - 1.0)
                 <= C_RANGE_RTOL)
    check("W6 REPRODUCTION exact update %.2e <= %.0e; c range "
          "[%.5f, %.5f]" % (xrec_dev, XUPD_WARD,
                            float(np.min(cs)), float(np.max(cs))),
          xrec_dev <= XUPD_WARD and ok_crange, kill="K2")
    Umat = np.array([vec36(U) for (_c, U) in u_list])
    _uu, sv, vt = np.linalg.svd(Umat, full_matrices=False)
    en = sv ** 2
    cum = np.cumsum(en) / float(np.sum(en))
    k95 = int(np.argmax(cum >= U_ENERGY)) + 1
    share1 = float(en[0] / np.sum(en))
    check("W7 REPRODUCTION u-anatomy: k95 == %d (found %d), "
          "top-mode share %.4f >= %.2f"
          % (K95_EXP, k95, share1, M1_SHARE_BAR),
          k95 == K95_EXP and share1 >= M1_SHARE_BAR, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------- T1-T3
    section("T1-T3 -- the Schur tangent split along the soft "
            "direction (all %d steps)" % len(steps))
    print("    frame: v_h = lam_min eigenvector of S_h "
          "(backward-only); Householder completion (SPEC ii).")
    dev_mid = dev_det = dev_piv = dev_scl = dev_src = 0.0
    equiv_ok = True
    nB_dead = 0
    rows = []
    for (c, U), (r1, r2) in zip(u_list, steps):
        wS, VS = np.linalg.eigh(r1["S"])
        v = VS[:, 0]
        Q = householder_frame(v)
        Mx = r1["X"] + U
        Mx = 0.5 * (Mx + Mx.T)
        # T1.a exactness M_X == S'/tau
        mid = (float(np.linalg.norm(Mx - r2["S"] / r1["tau"]))
               / max(float(np.linalg.norm(Mx)), 1e-300))
        dev_mid = max(dev_mid, mid)
        nsc, b, B, q, gap, B_pd, minB = schur_scalars(Mx, Q)
        evM = np.linalg.eigvalsh(Mx)
        M_pd = float(evM[0]) > 0.0
        if B_pd:
            # T1.b det identity
            sgM, ldM = np.linalg.slogdet(Mx)
            sgB, ldB = np.linalg.slogdet(B)
            if gap > 0 and sgM == 1.0 and sgB == 1.0:
                dev_det = max(dev_det, abs(
                    ldM - (math.log(gap) + ldB)))
            # T1.c pivot route
            piv = 1.0 / float(v @ np.linalg.solve(Mx, v))
            dev_piv = max(dev_piv, abs(piv - gap)
                          / max(abs(gap), 1e-300))
            # T1.d equivalence
            equiv_ok &= (M_pd == (gap > 0.0))
        else:
            nB_dead += 1
            equiv_ok &= (not M_pd)     # B not PD => M not PD
        # T1.e sign-free scaling + T5 source-only expressions
        ell = ell_det(r1["S"])
        if ell is not None and B_pd:
            gap_y = gap * (r1["tau"] / ell)
            Sp = r2["S"]
            n_src = float(v @ Sp @ v) / ell
            Wf = Q[:, 1:]
            b_src = (Wf.T @ Sp @ v) / ell
            B_src = (Wf.T @ Sp @ Wf) / ell
            q_src = float(b_src @ np.linalg.solve(B_src, b_src))
            gap_src = n_src - q_src
            dev_scl = max(dev_scl, abs(
                gap_y - gap_src) / max(abs(gap_y), 1e-300))
            dev_src = max(dev_src,
                          abs(n_src - nsc * r1["tau"] / ell)
                          / max(abs(n_src), 1e-300),
                          abs(q_src - q * r1["tau"] / ell)
                          / max(abs(q_src), 1e-300))
        rows.append(dict(r1=r1, r2=r2, c=c, U=U, v=v, Q=Q, Mx=Mx,
                         n=nsc, q=q, gap=gap, B_pd=B_pd,
                         minB=minB, lamM=float(evM[0])))
    check("T1.a WARD M_X == S'/tau: max rel %.2e <= %.0e"
          % (dev_mid, MID_WARD), dev_mid <= MID_WARD, kill="K2")
    check("T1.b WARD det M == (n - q) det B: max |log dev| %.2e "
          "<= %.0e" % (dev_det, DET_WARD), dev_det <= DET_WARD,
          kill="K2")
    check("T1.c WARD n - q == 1/(v^T M^{-1} v): max rel %.2e <= "
          "%.0e" % (dev_piv, PIV_WARD), dev_piv <= PIV_WARD,
          kill="K2")
    check("T1.d WARD PD(M) <=> (B PD and n - q > 0) on every "
          "step (B-dead steps: %d, counted)" % nB_dead, equiv_ok,
          kill="K2")
    check("T1.e WARD sign-free scaling (n-q)_Y == (n-q)_X "
          "tau/ell: max rel %.2e <= %.0e" % (dev_scl, SCL_WARD),
          dev_scl <= SCL_WARD, kill="K2")
    check("T5 WARD source-only expressions n ell == v^T S' v, "
          "q ell == Schur(S'): max rel %.2e <= %.0e"
          % (dev_src, SRC_WARD), dev_src <= SRC_WARD, kill="K2")
    print("    T5 honest reading: v_h, W_h = rung-h spectral "
          "data (backward); S' = comb linear algebra at rung "
          "h+1; ell = det(S_h)^{1/8} source-only (P1) -- no "
          "forward sign enters the expressions.")

    print("\n    THE LADDER (X-coordinates; gap = n - q):")
    print("    step        n          q          gap        "
          "minB      minB/lamM  lamM")
    gaps = []
    minBs = []
    for row in rows:
        gaps.append(row["gap"])
        minBs.append(row["minB"])
        print("    h %3d->%3d  %9.4f  %9.4f  %9.4f  %9.4f  "
              "%8.2f  %8.4f"
              % (row["r1"]["h"], row["r2"]["h"], row["n"],
                 row["q"], row["gap"], row["minB"],
                 row["minB"] / max(row["lamM"], 1e-300),
                 row["lamM"]), flush=True)
    minB_all = float(np.min(minBs))
    t2 = ("SAFEBLOCK(minB=%.4f)" % minB_all if nB_dead == 0
          else "SAFEBLOCK-BROKEN(%d)" % nB_dead)
    check("T2.1 typed: %s (exposure minB/lamM range [%.1f, "
          "%.1f])" % (t2,
                      float(np.min([r["minB"] / r["lamM"]
                                    for r in rows])),
                      float(np.max([r["minB"] / r["lamM"]
                                    for r in rows]))), True)
    gmin, gmed = (float(np.min(gaps)), float(np.median(gaps)))
    ells = [ell_det(row["r1"]["S"]) for row in rows]
    gap_y = [row["gap"] * row["r1"]["tau"] / e
             for row, e in zip(rows, ells)]
    t3 = "GAP(min=%.4f, med=%.4f)" % (gmin, gmed)
    check("T3.1 typed: %s; sign-free gap_Y range [%.3e, %.3e]; "
          "gap > 0 on %d/%d (== truth PD via T1.d, no new claim)"
          % (t3, float(np.min(gap_y)), float(np.max(gap_y)),
             int(np.sum(np.array(gaps) > 0.0)), len(gaps)), True)

    # ------------------------------------------------------------ T4
    section("T4 -- the v900 rank-1 failure, relocated into the "
            "scalars")
    m1v = vt[0].copy()
    M1 = unvec36(m1v)
    alphas = np.array([float(np.sum(vec36(U) * m1v))
                       for (_c, U) in u_list])
    if float(np.mean(alphas)) < 0.0:
        m1v, M1, alphas = -m1v, -M1, -alphas
    m_rk1 = []
    for (c, U), a, (r1, _r2) in zip(u_list, alphas, steps):
        Wi = inv_sqrt(r1["X"])
        m_rk1.append(c * (1.0 + float(np.linalg.eigvalsh(
            Wi @ (a * M1) @ Wi)[0])))
    m_rk1 = np.array(m_rk1)
    n_neg = int(np.sum(m_rk1 <= 0.0))
    check("T4.a WARD REPRODUCTION rank-1 surrogate margin-"
          "negative count %d == %d of %d (v900 ledger)"
          % (n_neg, RK1_NEG_REF, len(m_rk1)),
          n_neg == RK1_NEG_REF, kill="K2")
    fail_idx = np.where(m_rk1 <= 0.0)[0]
    print("\n    the %d failing steps -- true vs surrogate "
          "scalars (same frozen frame):" % len(fail_idx))
    print("    step        n_t       q_t       gap_t     "
          "n_s       q_s       gap_s     minB_s   dn=n_t-n_s "
          "dq=q_t-q_s")
    n_gap_fail = 0
    n_B_fail = 0
    dns, dqs = [], []
    rec_dev = 0.0
    parts_tbl = []
    bside_tbl = []
    ovls = []
    for i in fail_idx:
        row = rows[i]
        a = alphas[i]
        U = u_list[i][1]
        Ms = row["r1"]["X"] + a * M1
        Ms = 0.5 * (Ms + Ms.T)
        ns_, bs_, Bs_, qs_, gaps_, Bs_pd, minBs_ = schur_scalars(
            Ms, row["Q"])
        # frame-invariant seat: most-negative direction of M_s
        evMs, VMs = np.linalg.eigh(Ms)
        z = VMs[:, 0]
        ovl = float(np.dot(z, row["v"])) ** 2
        ovls.append(ovl)
        v = row["v"]
        Wf = row["Q"][:, 1:]
        Up = U - a * M1
        dB = Wf.T @ Up @ Wf
        if not Bs_pd:
            n_B_fail += 1
            wBs, VBs = np.linalg.eigh(Bs_)
            ws_ = VBs[:, 0]
            Bt = Wf.T @ row["Mx"] @ Wf
            lift = float(ws_ @ dB @ ws_)
            after = float(ws_ @ Bt @ ws_)
            bside_tbl.append((row, minBs_,
                              float(np.linalg.eigvalsh(Bt)[0]),
                              lift, after,
                              float(np.linalg.norm(dB)),
                              float(np.linalg.norm(
                                  Wf.T @ (a * M1) @ Wf)), ovl))
            print("    h %3d->%3d  surrogate B NOT PD (minB "
                  "%.4f) -> B-branch; seat overlap <z, v>^2 = "
                  "%.4f"
                  % (row["r1"]["h"], row["r2"]["h"], minBs_,
                     ovl))
            continue
        if gaps_ <= 0.0:
            n_gap_fail += 1
        dn = row["n"] - ns_
        dq = row["q"] - qs_
        dns.append(dn)
        dqs.append(dq)
        # q-branch off-mode anatomy
        db = Wf.T @ Up @ v
        b_t = Wf.T @ row["Mx"] @ v
        lin = 2.0 * float(bs_ @ np.linalg.solve(Bs_, db))
        quad = float(db @ np.linalg.solve(Bs_, db))
        q_mix = float(b_t @ np.linalg.solve(Bs_, b_t))
        bpart = q_mix - qs_
        Bpart = row["q"] - q_mix
        rec_dev = max(rec_dev, abs((lin + quad) - bpart)
                      / max(abs(bpart), 1e-300))
        parts_tbl.append((row, dn, lin, quad, Bpart))
        print("    h %3d->%3d  %8.4f  %8.4f  %8.4f  %8.4f  "
              "%8.4f  %8.4f  %8.4f  %+8.4f  %+8.4f"
              % (row["r1"]["h"], row["r2"]["h"], row["n"],
                 row["q"], row["gap"], ns_, qs_, gaps_, minBs_,
                 dn, dq), flush=True)
    check("T4.b WARD off-mode q-anatomy recomposition (b-part == "
          "linear + quadratic): max rel %.2e <= %.0e (q-branch "
          "steps: %d; empty branch => vacuous, disclosed)"
          % (rec_dev, RES_WARD, len(parts_tbl)),
          rec_dev <= RES_WARD, kill="K2")
    if parts_tbl:
        print("\n    q-branch off-mode anatomy (q-shift parts; "
              "U_perp = U - alpha M1):")
        print("    step        dn(n-shift)  q b-linear  "
              "q b-QUAD   q B-part")
        for row, dn, lin, quad, Bpart in parts_tbl:
            print("    h %3d->%3d  %+10.4f  %+10.4f  %+10.4f  "
                  "%+10.4f"
                  % (row["r1"]["h"], row["r2"]["h"], dn, -lin,
                     -quad, -Bpart), flush=True)
    if bside_tbl:
        print("\n    B-branch anatomy (co-block restoration is "
              "LINEAR in the off-mode: B_t = B_s + dB):")
        print("    step        minB_s      minB_t    "
              "w^T dB w    w^T B_t w   |dB|_F     |aM1_B|_F  "
              "<z,v>^2")
        for (row, mBs, mBt, lift, after, ndB, nM1B,
             ovl) in bside_tbl:
            print("    h %3d->%3d  %9.3f  %9.4f  %+9.3f  "
                  "%+9.4f  %9.3f  %9.3f  %7.4f"
                  % (row["r1"]["h"], row["r2"]["h"], mBs, mBt,
                     lift, after, ndB, nM1B, ovl), flush=True)
    if n_B_fail == 0 and n_gap_fail == len(fail_idx):
        t4a = "RESCUE-IN-GAP"
    else:
        t4a = ("RESCUE-MIXED(B-dead=%d, gap<=0=%d of %d)"
               % (n_B_fail, n_gap_fail, len(fail_idx)))
    med_dq = float(np.median(np.abs(dqs))) if dqs else 0.0
    med_dn = float(np.median(np.abs(dns))) if dns else 0.0
    if not parts_tbl:
        t4b = "OFFMODE-IN-B"
    elif med_dq > med_dn:
        t4b = "OFFMODE-IN-Q"
    else:
        t4b = "OFFMODE-IN-N"
    med_ovl = float(np.median(ovls))
    lo_all = all(o < OVL_BAR for o in ovls)
    hi_all = all(o >= OVL_BAR for o in ovls)
    if lo_all:
        t4c = "FAILSEAT-COBLOCK(med-ovl=%.3f)" % med_ovl
    elif hi_all:
        t4c = "FAILSEAT-SOFT(med-ovl=%.3f)" % med_ovl
    else:
        t4c = "FAILSEAT-MIXED(med-ovl=%.3f)" % med_ovl
    check("T4.c typed: %s / %s / %s (med |dq| %.4f vs med |dn| "
          "%.4f; seat overlaps med %.4f, range [%.4f, %.4f])"
          % (t4a, t4b, t4c, med_dq, med_dn, med_ovl,
             float(np.min(ovls)), float(np.max(ovls))), True)
    print("    reading (channel-aware, from the measured "
          "counts): the incoming expectation 'gap fails while "
          "B stays safe' holds at %d of %d failing steps; at %d "
          "the surrogate CO-BLOCK itself loses PD and the "
          "off-mode restores it LINEARLY (B_t = B_s + dB) -- "
          "truncating the 2.5%%-energy off-mode destroys "
          "positivity in directions the soft-mode split calls "
          "safe.  The seat overlaps <z, v>^2 quantify how far "
          "the failure sits from the current critical direction."
          % (n_gap_fail, len(fail_idx), n_B_fail))

    # ------------------------------------------------------------ C
    section("C -- controls: smooth world + Epstein/scramble")
    check("C0.1 WARD truth wall holds (neg(A) = 0 on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    print("  C1 -- the smooth-mass world:")
    sm = []
    for kz in zones:
        r = gram_anatomy(kz, world_fn=world_smooth)
        if r is not None:
            sm.append(r)
    sm.sort(key=lambda r: (r["h"], r["kz"]))
    n_viol = sum(1 for r in sm if r["negA"] > 0)
    n_exit = 0
    n_pairs = 0
    for ra, rb in zip(sm, sm[1:]):
        if not (ra.get("core_ok") and rb.get("core_ok")):
            continue
        n_pairs += 1
        if ra["negS"] > 0 or rb["negS"] > 0 or ra["negA"] > 0:
            n_exit += 1
            continue
        wS, VS = np.linalg.eigh(ra["S"])
        Q = householder_frame(VS[:, 0])
        tau_a = ra["tau"]
        if tau_a == 0.0:
            n_exit += 1
            continue
        Msm = rb["S"] / tau_a
        _n, _b, _B, _q, gap_s, B_pd, _mB = schur_scalars(
            0.5 * (Msm + Msm.T), Q)
        if (not B_pd) or (gap_s is not None and gap_s <= 0.0) \
                or tau_a < 0.0:
            n_exit += 1
    print("    %d rungs; neg(A) > 0 on %d; tangent machinery "
          "exits on %d of %d smooth full-core steps"
          % (len(sm), n_viol, n_exit, n_pairs))
    check("C1.1 WARD smooth violates at rung level", n_viol > 0,
          kill="K2")
    check("C1.2 WARD tangent machinery exits on >= 1 smooth "
          "step", n_exit >= 1, kill="K2")
    print("  C2 -- Epstein + scramble at kz %d:" % CTRL_KZ)
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
    for name, r in ctl.items():
        if r is None:
            print("    %-9s: chain dies -> fires" % name)
            continue
        f = r["negA"] > 0
        fired_all &= f
        print("    %-9s: tau %+.3e  neg(A) %d -> %s"
              % (name, r["tau"], r["negA"],
                 "FIRES" if f else "SILENT"), flush=True)
    check("C2.1 WARD both controls fire", fired_all, kill="K2")

    return finish(dict(t2=t2, t3=t3, t4a=t4a, t4b=t4b, t4c=t4c))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("TANGENTSCHUR-MEASURED / %(t2)s / %(t3)s / "
                   "%(t4a)s / %(t4b)s / %(t4c)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the Schur split is exact warded
  linear algebra; gap > 0 on the ladder is EQUIVALENT to the
  known truth positivity (T1.d) -- nothing new is claimed
  positive.  The content is (a) the measured safe-block floor,
  (b) the two-scalar reduction with source-only expressions (no
  forward tau-sign input), and (c) the v900 rank-1 failure
  located in the scalars with its off-mode q-anatomy.  NO RH
  claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
