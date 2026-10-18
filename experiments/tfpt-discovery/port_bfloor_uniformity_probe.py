#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_bfloor_uniformity_probe -- PRIME.PORT.BFLOOR.01
(EXPLORATION ONLY, experiments/; round 58: the co-block floor as a
target of its own -- lam_min(B_h) ladder-wide, the TAU-SCREEN
applied to it, certified classical lower bounds, and the structural
anatomy of B.  2026-08-10.)

THE QUESTION (frozen).  P2 of round 57 (port_tangent_schur_probe,
PRIME.PORT.TANGENT.SCHUR.01) reduced the wall update to
(B_h PD) AND (n_h > q_h) via the exact Schur split of
M_h = X_h + U_h = S_{h+1}/tau_h along the current soft direction
v_h of S_h, and MEASURED the safe-block floor min eig(B_h) = 0.679
ladder-wide -- measured, not proven.  THE META-CRITERION of this
round (frozen): five exact reformulations in a row have RELOCATED
the difficulty instead of reducing it, and that is measurable -- a
candidate route is a RELOCATION iff its own distance-to-violation
scales like tau_h (the wall margin).  THE TAU-SCREEN: corr and
log-log OLS slope of the candidate margin vs tau_h across the
ladder; slope ~ +1 -> relocation (recorded honestly); slope ~ 0
with an O(1) floor -> the first route that passes the screen
(flagged).  Applied here to lam_min(B_h):
 (a) if the B-floor does NOT track tau (slope ~ 0, floor O(1)),
     B-uniformity is a genuinely easier sub-target and the whole
     remaining difficulty sits in the two scalars n, q -- a real
     structural gain;
 (b) if it tracks tau, relocation again -- recorded either way.
HONEST COORDINATE NOTE (frozen, said up front): B_h is deployed in
X-coordinates, B = W^T (S_{h+1}/tau_h) W -- the division by tau_h
is part of the coordinate.  The screen is applied to the DEPLOYED
B (frozen primary), and the unnormalized co-block
lam_min(W^T S_{h+1} W) and the sign-free reading (x tau_h/ell_h,
ell = det(S_h)^{1/8}, the P1 winner) are printed next to it -- an
O(1) B-floor in X-coordinates means the unnormalized co-block
floor scales EXACTLY like tau (printed, not hidden).

FROZEN PROTOCOL (2026-08-10; machinery verbatim from
port_tangent_schur_probe (round 57), which is verbatim from
normalized_core_update_probe / core_graph_region_probe (v900);
gram_anatomy carries the P1 extensions tr(R), sum(v)):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2
     >= 30 full-core rungs; W3 all-PSD + >= 20 consecutive steps;
     W4 deepcore product law <= 1e-6; W5 eta floor 0.0315 (tol
     5.001e-5); W6 exact update ||X' - c(X+U)|| <= 1e-10 and c
     range [0.051, 19.50] (rtol 2e-2); W7 u-anatomy k95 == 1 and
     top-mode share >= 0.90.

 B1  THE B-LADDER (per step; kill -> WARD-BROKEN):
       B1.a  M_X == S_{h+1}/tau_h, rel <= MID_WARD = 1e-12;
       B1.b  PD(M) <=> (B PD and n - q > 0), exact boolean per
             step (P2 reproduction);
       B1.c  REPRODUCTION: min_h lam_min(B_h) == 0.679 (rtol
             2e-2) and gap min/med == 0.052/0.888 (rtol 5e-2)
             against the recorded P2 ledger;
       B1.d  FRAME ORTHOGONALITY: the B-minimizing vector mapped
             back, u = W w_min, obeys <u, v_h>^2 <= OVL0_WARD =
             1e-18 (constructional exactness of the Householder
             frame, warded not assumed).

 B2  THE TAU-SCREEN (the decisive measurement; typed, never
     kills): OLS slope + corr of log lam_min(B_h) vs log tau_h
     over all steps; secondary prints: slope vs log tau_{h+1},
     vs log h; the unnormalized co-block slope (lam_min(W^T S'
     W) vs tau) and the sign-free reading (x tau/ell).  TYPED
     (frozen rules): BFLOOR-SCREEN-PASS(slope) iff |slope| <=
     SLOPE_PASS = 0.30 AND min lam_min(B) > 0; BFLOOR-SCREEN-
     RELOC(slope) iff slope >= SLOPE_RELOC = 0.70; else
     BFLOOR-SCREEN-AMBIG(slope).

 B3  CERTIFIED CLASSICAL LOWER BOUNDS on lam_min(B_h) (per step;
     measured, typed): G1 Gershgorin min_i (b_ii - r_i); G2
     scaled Gershgorin: with C = D^{-1/2} B D^{-1/2}, D =
     diag(B), lamG(C) = min_i (1 - r_i(C)), bound = lamG(C) x
     (min diag if lamG >= 0 else max diag); G3 Brauer-Cassini on
     C (pairs): (1 - max_{i<j} sqrt(r_i r_j)) mapped as G2; G4
     backward + step (Weyl): lam_min(W^T X_h W) - ||W^T U_h W||_2
     (backward co-block floor minus the exact step-increment
     norm; float-assisted eigs, labelled).  Reported: best bound
     per step, count of steps with best > 0, gap factor
     lam_min(B)/best on the positive steps (quartiles + worst).
     TYPED: CERTFLOOR-POSITIVE(n, worst-gap) iff best > 0 on all
     steps, CERTFLOOR-PARTIAL(n) if on some, CERTFLOOR-DEAD if
     none.

 B4  STRUCTURE OF B (measured): dimension (7 on every step,
     printed); spectrum shape per step (lam_min, lam_max, cond);
     drift: OLS slope of log lam_min(B) vs log h (converge vs
     drift, band |slope| <= 0.15 as v900's boundedness band --
     typed BSPEC-STABLE / BSPEC-DRIFT(slope)); the minimizer
     seat: <u, v_h>^2 (== 0 constructional, warded in B1.d) and
     <u, v_{h+1}>^2 vs the FORWARD soft direction (quartiles
     printed; typed BSEAT-ORTHOGONAL(med) iff median < 0.5 else
     BSEAT-FORWARD(med) -- the P2 refutation said the failure
     seat is orthogonal to the CURRENT soft direction; here the
     forward overlap is the new measurement).

 T4  SURROGATE REGRESSION (kill -> WARD-BROKEN): the v900 rank-1
     surrogate margin-negative count == 12 of 39 AND the
     surrogate co-block B_s is NOT PD at ALL 12 failing steps
     (the P2 refutation reproduced: the failure lives in B
     itself; min eig(B_s) per failing step printed).

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) =
     0 everywhere; C1 smooth world: neg(A) > 0 on >= 1 rung AND
     the B-machinery exits on >= 1 smooth step (S not PSD or B
     not PD or gap <= 0); C2 Epstein + scramble (seed 1) at kz 9
     fire (neg(A) > 0 or chain death).

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
identity / control wards (W4-W7, B1, T4, C0-C2) -> WARD-BROKEN.
B2/B3/B4 typed outcomes are measurements, never kills.

VERDICT (frozen enum): BFLOOR-MEASURED with typed sublabels
BFLOOR-SCREEN-PASS(slope) / BFLOOR-SCREEN-RELOC(slope) /
BFLOOR-SCREEN-AMBIG(slope), CERTFLOOR-POSITIVE(n, gap) /
CERTFLOOR-PARTIAL(n) / CERTFLOOR-DEAD, BSPEC-STABLE /
BSPEC-DRIFT(slope), BSEAT-ORTHOGONAL(med) / BSEAT-FORWARD(med);
else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900 (the
certified v897 census cap -- deeper rungs are NOT deployed and
stay excluded, disclosed); N_RUNGS_EXP = 42; MIN_CORE_RUNGS = 30;
MIN_STEPS = 20; REPRO_PROD_BAR = 1e-6; REPRO_ETA_MIN = 0.0315;
ROUND_TOL = 5.001e-5; XUPD_WARD = 1e-10; C_RANGE_REF = [0.051,
19.50] (rtol 2e-2); K95_EXP = 1; M1_SHARE_BAR = 0.90; MID_WARD =
1e-12; OVL0_WARD = 1e-18; MINB_REF = 0.679 (rtol 2e-2);
GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2); RK1_NEG_REF =
12; BDEAD_REF = 12; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70;
BSPEC_BND = 0.15; SEAT_BAR = 0.5; CTRL_KZ = 9; scramble seed 1.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script (24/24 with the identical bars; no bar, rule or
enum was tuned to it -- the screen bands, the certified-bound
list and the typed rules above predate the run) measured the
picture that is frozen here as context: lam_min(B_h) in [0.679,
83.99] with tau-screen slope -0.247 (corr -0.346, R^2 0.119)
while tau spans a factor 552 -- inside the PASS band with an
O(1) floor; the unnormalized co-block tracks tau at slope +0.753
(the coordinate honesty note above is exactly what happens); ALL
FOUR classical certified bounds G1-G4 are NEGATIVE on every step
(best-bound max -88.2; the Gershgorin-type off-diagonal mass at
core scale ~10^3 overwhelms the 0.679 floor) -> CERTFLOOR-DEAD;
the B-minimizer is orthogonal to v_h (warded) and its forward
overlap <u, v_{h+1}>^2 has median 0.0053 (max 0.066); the
surrogate co-block is dead at all 12 failing steps (minB_s
-4.19 .. -363.7, the P2 range reproduced).  No census count, no
enum, no typed rule was changed after the smoke run.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as P2
SPEC (ii), deterministic; (iii) OLS/corr population statistics as
v900; (iv) G4 spectral norm via eigvalsh of the symmetrized
increment co-block; (v) the screen's primary regressor is tau_h
(the step's base rung), secondaries printed.

NO RH claim: lam_min(B_h) > 0 ladder-wide is a MEASUREMENT on the
deployed v563 window ladder (equivalent content to part of the
wall via the P2 split); the screen slope is a scaling diagnostic;
nothing here proves B-uniformity for all h, and nothing here
proves tau_h > 0 beyond the certified census (v897).  No marker
moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
exact-update + Schur-tangent machinery verbatim from
port_tangent_schur_probe.py (P2, round 57); rank-1 surrogate
construction verbatim from core_graph_region_probe.py (round 56,
promoted v900); sign-free normalization ELL-B from
port_signfree_normalization_probe.py (P1, round 57, declared
input); certified base v884/v887/v897 -- declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_bfloor_uniformity_probe.py
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
K95_EXP = 1
M1_SHARE_BAR = 0.90
U_ENERGY = 0.95
MID_WARD = 1e-12               # B1.a
OVL0_WARD = 1e-18              # B1.d frame orthogonality
MINB_REF = 0.679               # B1.c (P2 printed ledger)
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052             # B1.c (P2 printed ledger)
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
RK1_NEG_REF = 12               # T4 (v900 ledger)
BDEAD_REF = 12                 # T4 (P2 printed ledger)
SLOPE_PASS = 0.30              # B2 screen bands (frozen a priori)
SLOPE_RELOC = 0.70
BSPEC_BND = 0.15               # B4 drift band (v900)
SEAT_BAR = 0.5                 # B4 seat bar
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


# --------------- pipeline, verbatim (port_tangent_schur_probe)
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
    """v900 verbatim wall + fixed-core split (P1/P2 extension)."""
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
    """P2 SPEC (ii): deterministic orthonormal Q with Q[:, 0] = v."""
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


def schur_scalars(Mm, Q):
    """(n, b, B, q or None, gap or None, B_pd, minB) in frame Q."""
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


def corr(x, y):
    return float(np.corrcoef(np.asarray(x, float),
                             np.asarray(y, float))[0, 1])


# ------------------------------ B3: certified classical bounds
def gersh_min(B):
    """G1: min_i (b_ii - sum_{j != i} |b_ij|)."""
    d = np.diag(B)
    r = np.sum(np.abs(B), axis=1) - np.abs(d)
    return float(np.min(d - r))


def gersh_scaled(B):
    """G2: B = D^{1/2} C D^{1/2}; certified lower bound via
    Gershgorin on C (returns -inf if a diagonal entry <= 0)."""
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
    """G3: Brauer-Cassini ovals on C (unit diagonal): lam_min(C)
    >= 1 - max_{i<j} sqrt(r_i r_j); mapped as G2."""
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


def main():
    section("PRIME.PORT.BFLOOR.01 -- the co-block floor as its own "
            "target + the tau-screen (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + v900/P2 reproduction wards")
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

    # ------------------------------------------------------------ B1
    section("B1 -- THE B-LADDER (all %d steps; frame: v_h soft "
            "direction of S_h, Householder completion)" % len(steps))
    dev_mid = 0.0
    equiv_ok = True
    ovl0_max = 0.0
    rows = []
    for (c, U), (r1, r2) in zip(u_list, steps):
        wS, VS = np.linalg.eigh(r1["S"])
        v = VS[:, 0]
        Q = householder_frame(v)
        Mx = r1["X"] + U
        Mx = 0.5 * (Mx + Mx.T)
        mid = (float(np.linalg.norm(Mx - r2["S"] / r1["tau"]))
               / max(float(np.linalg.norm(Mx)), 1e-300))
        dev_mid = max(dev_mid, mid)
        nsc, b, B, q, gap, B_pd, minB = schur_scalars(Mx, Q)
        evM = np.linalg.eigh(Mx)
        M_pd = float(evM[0][0]) > 0.0
        if B_pd:
            equiv_ok &= (M_pd == (gap > 0.0))
        else:
            equiv_ok &= (not M_pd)
        evB, VB = np.linalg.eigh(B)
        wmin = VB[:, 0]
        Wf = Q[:, 1:]
        u8 = Wf @ wmin
        ovl0 = float(np.dot(u8, v)) ** 2
        ovl0_max = max(ovl0_max, ovl0)
        wS2, VS2 = np.linalg.eigh(r2["S"])
        vfwd = VS2[:, 0]
        ovlf = float(np.dot(u8, vfwd)) ** 2
        # unnormalized + sign-free co-block floors
        minB_un = minB * r1["tau"]           # W^T S' W (exact scale)
        ell = ell_det(r1["S"])
        minB_y = (minB * r1["tau"] / ell) if ell else float("nan")
        # certified bounds
        g1 = gersh_min(B)
        g2 = gersh_scaled(B)
        g3 = cassini_scaled(B)
        Xco = Wf.T @ r1["X"] @ Wf
        Uco = Wf.T @ U @ Wf
        Uco = 0.5 * (Uco + Uco.T)
        g4 = (float(np.linalg.eigvalsh(Xco)[0])
              - float(np.max(np.abs(np.linalg.eigvalsh(Uco)))))
        rows.append(dict(r1=r1, r2=r2, B=B, minB=minB,
                         maxB=float(evB[-1]),
                         cond=float(evB[-1]) / minB
                         if minB > 0 else float("inf"),
                         gap=gap, B_pd=B_pd, minB_un=minB_un,
                         minB_y=minB_y, g1=g1, g2=g2, g3=g3,
                         g4=g4, ovlf=ovlf,
                         lamM=float(evM[0][0])))
    check("B1.a WARD M_X == S'/tau: max rel %.2e <= %.0e"
          % (dev_mid, MID_WARD), dev_mid <= MID_WARD, kill="K2")
    check("B1.b WARD PD(M) <=> (B PD and n - q > 0) on every step",
          equiv_ok, kill="K2")
    nB_dead = sum(1 for row in rows if not row["B_pd"])
    minBs = np.array([row["minB"] for row in rows])
    gaps = np.array([row["gap"] if row["gap"] is not None
                     else float("nan") for row in rows])
    minB_all = float(np.min(minBs))
    gmin, gmed = (float(np.min(gaps)), float(np.median(gaps)))
    ok_repro = (nB_dead == 0
                and abs(minB_all / MINB_REF - 1.0) <= MINB_RTOL
                and abs(gmin / GAPMIN_REF - 1.0) <= GAP_RTOL
                and abs(gmed / GAPMED_REF - 1.0) <= GAP_RTOL)
    check("B1.c REPRODUCTION P2 ledger: min lam_min(B) %.4f == "
          "%.3f (rtol %.0e); gap min/med %.4f/%.4f == %.3f/%.3f "
          "(rtol %.0e); B-dead steps %d == 0"
          % (minB_all, MINB_REF, MINB_RTOL, gmin, gmed,
             GAPMIN_REF, GAPMED_REF, GAP_RTOL, nB_dead),
          ok_repro, kill="K2")
    check("B1.d WARD frame orthogonality <u, v_h>^2 max %.2e <= "
          "%.0e (u = W w_min, constructional)"
          % (ovl0_max, OVL0_WARD), ovl0_max <= OVL0_WARD,
          kill="K2")

    print("\n    THE B-LADDER (X-coordinates; certified floors "
          "G1..G4; unnormalized/sign-free floors):")
    print("    step        tau_h      minB     maxB     cond   "
          " minB*tau   minB*t/l   bestG      ovl_fwd")
    for row in rows:
        bg = max(row["g1"], row["g2"], row["g3"], row["g4"])
        print("    h %3d->%3d  %.3e %8.4f %8.1f %8.1f  "
              "%.3e  %.3e  %+9.3e  %.5f"
              % (row["r1"]["h"], row["r2"]["h"], row["r1"]["tau"],
                 row["minB"], row["maxB"], row["cond"],
                 row["minB_un"], row["minB_y"], bg, row["ovlf"]),
              flush=True)

    # ------------------------------------------------------------ B2
    section("B2 -- THE TAU-SCREEN on lam_min(B_h)")
    taus = np.array([row["r1"]["tau"] for row in rows])
    taus2 = np.array([row["r2"]["tau"] for row in rows])
    hh = np.array([row["r1"]["h"] for row in rows], float)
    _a, sl_tau, r2_tau = ols_line(np.log(taus), np.log(minBs))
    co_tau = corr(np.log(taus), np.log(minBs))
    _a, sl_tau2, _r = ols_line(np.log(taus2), np.log(minBs))
    _a, sl_h, _r = ols_line(np.log(hh), np.log(minBs))
    un = np.array([row["minB_un"] for row in rows])
    _a, sl_un, _r = ols_line(np.log(taus), np.log(un))
    print("    PRIMARY: slope log lam_min(B) vs log tau_h = "
          "%+.4f (corr %+.3f, R^2 %.3f)" % (sl_tau, co_tau, r2_tau))
    print("    secondary: vs log tau_{h+1} = %+.4f; vs log h = "
          "%+.4f" % (sl_tau2, sl_h))
    print("    coordinate honesty: unnormalized co-block "
          "lam_min(W^T S' W) vs tau: slope %+.4f (the X-floor "
          "O(1) <=> the raw co-block scales like tau)" % sl_un)
    print("    lam_min(B) range [%.4f, %.4f]; tau range "
          "[%.3e, %.3e] (factor %.0f)"
          % (float(np.min(minBs)), float(np.max(minBs)),
             float(np.min(taus)), float(np.max(taus)),
             float(np.max(taus)) / float(np.min(taus))))
    if abs(sl_tau) <= SLOPE_PASS and minB_all > 0.0:
        b2 = "BFLOOR-SCREEN-PASS(slope=%+.3f)" % sl_tau
    elif sl_tau >= SLOPE_RELOC:
        b2 = "BFLOOR-SCREEN-RELOC(slope=%+.3f)" % sl_tau
    else:
        b2 = "BFLOOR-SCREEN-AMBIG(slope=%+.3f)" % sl_tau
    check("B2.1 typed: %s (bands: PASS |s| <= %.2f, RELOC s >= "
          "%.2f)" % (b2, SLOPE_PASS, SLOPE_RELOC), True)

    # ------------------------------------------------------------ B3
    section("B3 -- certified classical lower bounds vs the true "
            "floor")
    names = ("G1 Gershgorin", "G2 scaled-Gershgorin",
             "G3 Brauer-Cassini", "G4 backward+step (Weyl)")
    cols = [np.array([row[k] for row in rows])
            for k in ("g1", "g2", "g3", "g4")]
    for nm, col in zip(names, cols):
        npos = int(np.sum(col > 0.0))
        print("    %-24s: min %+.3e  max %+.3e  positive on "
              "%d/%d" % (nm, float(np.min(col)),
                         float(np.max(col)), npos, len(rows)))
    best = np.maximum.reduce(cols)
    n_pos = int(np.sum(best > 0.0))
    if n_pos == len(rows):
        gapf = minBs / best
        b3 = ("CERTFLOOR-POSITIVE(%d, worst-gap=%.1f)"
              % (n_pos, float(np.max(gapf))))
        print("    best certified floor per step positive on ALL "
              "steps; gap factor lam_min(B)/best quartiles "
              "%.1f/%.1f/%.1f, worst %.1f"
              % tuple(list(np.percentile(gapf, [25, 50, 75]))
                      + [float(np.max(gapf))]))
    elif n_pos > 0:
        pos = best > 0.0
        gapf = minBs[pos] / best[pos]
        b3 = "CERTFLOOR-PARTIAL(%d)" % n_pos
        print("    best certified floor positive on %d/%d steps "
              "only (gap factor there: med %.1f, worst %.1f); "
              "worst-case best bound %.3e vs true floor %.4f"
              % (n_pos, len(rows), float(np.median(gapf)),
                 float(np.max(gapf)), float(np.min(best)),
                 minB_all))
    else:
        b3 = "CERTFLOOR-DEAD"
        print("    NO classical certified bound reaches a "
              "positive floor anywhere (worst best-bound %.3e "
              "vs true floor %.4f)"
              % (float(np.min(best)), minB_all))
    check("B3.1 typed: %s (true floor %.4f, ref 0.679)"
          % (b3, minB_all), True)

    # ------------------------------------------------------------ B4
    section("B4 -- structure of B: spectrum, drift, minimizer "
            "seat")
    conds = np.array([row["cond"] for row in rows])
    print("    dim(B) = 7 on every step (constructional); "
          "spectrum: lam_min quartiles %.3f/%.3f/%.3f; lam_max "
          "quartiles %.0f/%.0f/%.0f; cond quartiles "
          "%.0f/%.0f/%.0f"
          % tuple(list(np.percentile(minBs, [25, 50, 75]))
                  + list(np.percentile(
                      [row["maxB"] for row in rows], [25, 50, 75]))
                  + list(np.percentile(conds, [25, 50, 75]))))
    bspec = ("BSPEC-STABLE" if abs(sl_h) <= BSPEC_BND
             else "BSPEC-DRIFT(slope=%+.3f)" % sl_h)
    print("    drift: slope log lam_min(B) vs log h = %+.4f "
          "(band %.2f) -> %s" % (sl_h, BSPEC_BND, bspec))
    ovlf = np.array([row["ovlf"] for row in rows])
    med_ovlf = float(np.median(ovlf))
    print("    minimizer seat: <u, v_h>^2 == 0 warded (B1.d); "
          "<u, v_{h+1}>^2 quartiles %.5f/%.5f/%.5f (max %.4f)"
          % tuple(list(np.percentile(ovlf, [25, 50, 75]))
                  + [float(np.max(ovlf))]))
    bseat = ("BSEAT-ORTHOGONAL(med=%.4f)" % med_ovlf
             if med_ovlf < SEAT_BAR
             else "BSEAT-FORWARD(med=%.4f)" % med_ovlf)
    check("B4.1 typed: %s / %s" % (bspec, bseat), True)

    # ------------------------------------------------------------ T4
    section("T4 -- surrogate regression: the rank-1 failure lives "
            "in B (P2 refutation reproduced)")
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
    check("T4.a WARD REPRODUCTION rank-1 margin-negative count "
          "%d == %d of %d" % (n_neg, RK1_NEG_REF, len(m_rk1)),
          n_neg == RK1_NEG_REF, kill="K2")
    fail_idx = np.where(m_rk1 <= 0.0)[0]
    n_bdead = 0
    print("    failing steps: surrogate co-block min eig "
          "(B_s = W^T (X + alpha M1) W):")
    for i in fail_idx:
        row = rows[i]
        a = alphas[i]
        Ms = row["r1"]["X"] + a * M1
        Ms = 0.5 * (Ms + Ms.T)
        wS, VS = np.linalg.eigh(row["r1"]["S"])
        Q = householder_frame(VS[:, 0])
        _n, _b, _B, _q, _g, Bs_pd, minBs_ = schur_scalars(Ms, Q)
        if not Bs_pd:
            n_bdead += 1
        print("    h %3d->%3d  minB_s %+9.3f  (true minB "
              "%+.4f)" % (row["r1"]["h"], row["r2"]["h"], minBs_,
                          row["minB"]), flush=True)
    check("T4.b WARD surrogate co-block NOT PD at ALL failing "
          "steps: %d == %d" % (n_bdead, BDEAD_REF),
          n_bdead == BDEAD_REF, kill="K2")

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
    print("    %d rungs; neg(A) > 0 on %d; B-machinery exits on "
          "%d of %d smooth full-core steps"
          % (len(sm), n_viol, n_exit, n_pairs))
    check("C1.1 WARD smooth violates at rung level", n_viol > 0,
          kill="K2")
    check("C1.2 WARD B-machinery exits on >= 1 smooth step",
          n_exit >= 1, kill="K2")
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

    return finish(dict(b2=b2, b3=b3, bspec=bspec, bseat=bseat))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("BFLOOR-MEASURED / %(b2)s / %(b3)s / %(bspec)s "
                   "/ %(bseat)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): lam_min(B_h) > 0 ladder-wide is a
  MEASUREMENT, equivalent in content to part of the wall via the
  exact P2 split -- nothing new is claimed positive.  The content
  is (a) the tau-screen verdict on the deployed B-floor (with the
  coordinate honesty print: an O(1) X-floor means the raw
  co-block scales exactly like tau), (b) the measured distance
  between classical certified bounds and the true floor, and (c)
  the structural anatomy of B.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
