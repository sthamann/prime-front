#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""schur_ward_identity_probe -- PRIME.PORT.SCHUR.WARD.01
(EXPLORATION ONLY, experiments/; round 59, theorem-engineering on the
RH-side wall: the exact flow law of the Schur pivot along the ladder
-- is the arithmetic hub a linear inflow, is the geometric demand an
exact nonnegative adaptation energy, does the leading difference
cancel structurally, and what is the tau-screen of the second-order
correction?  2026-08-10.)

THE IDENTITY (derived a priori, exact for ANY symmetric M, M_+ with
B, B_+ invertible; completion of the square).  Partition M = [[n,
b^T], [b, B]], pivot s = n - b^T B^{-1} b, optimizer x = B^{-1} b.
Write b_+ - B_+ x = Delta b - Delta B x =: r (Delta = the step).
Then EXACTLY
    s_+ - s = Delta n - 2 <x, Delta b> + <x, Delta B x>
              - |Delta b - Delta B x|^2_{B_+^{-1}}       [SCHUR-WARD]
where |r|^2_{B_+^{-1}} = r^T B_+^{-1} r.  Structure (also exact):
with e = (1, -x) the FROZEN old optimizer, the linear part is
    LIN = e^T (M_+ - M) e,
so the identity reads s_+ = e^T M_+ e - ADAP, ADAP = |r|^2_{B_+^{-1}}
>= 0 whenever B_+ > 0: the pivot flow = first-order inflow along the
frozen optimizer MINUS an exact nonnegative ADAPTATION ENERGY of the
new optimizer (variational: s_+ = min over completions <= e^T M_+
e).  Second route for the pivot (frame-free): s = 1 / (M^{-1})_{00}.

THE MAPPING TO THE LADDER (frozen).  P2 (port_tangent_schur_probe,
round 58) split the wall update M_k = S(r2_k)/tau(r1_k) in the
Householder frame of the soft direction of S(r1_k) into the
arithmetic HUB n_k, the inflow column b_k, the co-block B_k, the
geometric DEMAND q_k = b_k^T B_k^{-1} b_k and the GAP = pivot s_k =
n_k - q_k (ledger: gap min/med 0.052/0.888, min lam_min(B) 0.679).
TWO ROUTES, both identity-warded:
 (i)  RAW TRIPLES (PRIMARY for the typed answers c, d): consecutive
      full-core PD rungs (rA, rB, rC); frame Q_A from the soft
      direction of S(rA); N = Q_A^T S(rB) Q_A -> N_+ = Q_A^T S(rC)
      Q_A.  The transition S(rB) -> S(rC) is the physical ladder
      flow with NO tau normalization jitter; the frame is FROZEN at
      the earlier rung (b != 0, nondegenerate).
 (ii) NORMALIZED STEP PAIRS (the P2 hub/demand dictionary,
      SECONDARY): consecutive steps sharing the middle rung, step k
      = (r1, r2), step k+1 = (r2, r3); BOTH matrices in the SHARED
      frame Q_k of step k: M = Q_k^T (S(r2)/tau(r1)) Q_k, M_+ =
      Q_k^T (S(r3)/tau(r2)) Q_k.  (The pivot is frame-covariant --
      s(M, v) = 1/<v, M^{-1} v> -- the shared frame only fixes the
      bookkeeping; own-frame vs shared-frame pivot printed as the
      frame-drift diagnostic.)
HONESTY (frozen): the identity holds for ANY pair of symmetric
matrices -- it carries no wall content by itself; ALL wall content
is in the measured signs, magnitudes, cancellation ratios and
tau-screens of its terms, and in the smooth-world control (does the
DEMAND term stop being an energy when the wall is violated?).

THE FOUR QUESTIONS (frozen; typed, never kill):
 (a) HUB INFLOW: is the arithmetic hub n_k a linear inflow?  OLS of
     the P2 hub n_k vs alpha(r2_k) across steps (own P2 frame,
     ledger route): HUB-LINEAR iff R^2 >= R2_LIN = 0.90, else
     HUB-NOT-LINEAR(R^2); tau-screen slope of n_k and the raw-route
     hub n_B = <v_A, S(rB) v_A> vs alpha printed as diagnostics.
 (b) DEMAND = ADAPTATION ENERGY: ADAP >= 0 EXACTLY on the truth
     side (B_+ > 0 warded).  Typed DEMAND-ENERGY-EXACT(min ADAP)
     after the numerical ward min ADAP >= -ADAP_TOL x scale.
 (c) LEADING CANCELLATION: rho = |Delta s| / (|LIN| + ADAP) per raw
     triple.  CANCEL-STRUCTURAL iff median rho <= RHO_STRUCT =
     0.10; CANCEL-PARTIAL iff <= RHO_PART = 0.50; else CANCEL-NONE.
     (Normalized-route rho printed.)
 (d) SECOND-ORDER CORRECTION: ADAP > 0 sign (exact), tau-screen of
     ADAP on raw triples: log ADAP vs log tau(rB) OLS slope;
     ADAP-SCREEN-PASS iff |slope| <= SLOPE_PASS = 0.30,
     ADAP-SCREEN-RELOC iff slope >= SLOPE_RELOC = 0.70, else
     ADAP-SCREEN-AMBIG.  Delta s sign counts printed (both routes).

FROZEN PROTOCOL (pipeline verbatim from port_tangent_schur_probe /
b_christoffel_deflation_probe = v900 chain; ONE Gram per rung;
window memoization):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2 >=
     30 full-core rungs; W3a truth all-PSD (A, R, S); W3b >= 20
     consecutive full-core steps; W4 REPRODUCTION P2/P3 ledger: min
     lam_min(B) == 0.679 (rtol 2e-2), gap min/med == 0.052/0.888
     (rtol 5e-2), raw-B certified disaster (best classical bound <
     0 on every step).

 P   TRANSITION CENSUS (kill -> PIPELINE-BROKEN): P1 >= MIN_PAIRS =
     15 step pairs sharing the middle rung; P2 >= MIN_TRIPLES = 15
     raw triples of consecutive full-core PD rungs.

 I1  THE IDENTITY, EXACT (kill -> WARD-BROKEN): per raw triple and
     per normalized pair: B and B_+ PD (truth side); identity
     deviation |(s_+ - s) - (LIN - ADAP)| / max(|s| + |s_+|, 1)
     <= ID_WARD; two-route pivot |1/(M^{-1})_{00} - (n - b^T B^{-1}
     b)| rel <= S2_WARD on every transition; ADAP >= -ADAP_TOL x
     scale.

 I2  THE FOUR TYPED ANSWERS (a)-(d) as frozen above; never kill.

 I3  FRAME-DRIFT DIAGNOSTICS (prints only): consecutive soft-
     direction overlap <v_k, v_{k+1}>^2; own-frame vs shared-frame
     pivot ratio for the second step of each pair.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) = 0;
     C1 smooth world neg(A) > 0 on >= 1 rung; C1.2 typed
     ENERGY-WALL: on smooth raw triples, count where B or B_+ is
     NOT PD (the demand stops being an energy) -> ENERGY-WALL-
     SEEN(count)/ENERGY-WALL-BLIND (typed first-class; the identity
     still holds algebraically wherever B, B_+ are invertible --
     deviation printed); C2 Epstein x^2+5y^2 comb + scramble (seed
     1) at kz 9 fire.

KILLS: K1 pipeline (W1-W3, P) -> PIPELINE-BROKEN; K2 reproduction /
identity / control wards (W4, I1, C0-C2) -> WARD-BROKEN.  I2/I3/C1.2
typed outcomes are measurements, never kills.

VERDICT (frozen enum): SCHURWARD-MEASURED with typed sublabels
WARD-IDENTITY-EXACT(maxdev), HUB-LINEAR/HUB-NOT-LINEAR(R^2),
DEMAND-ENERGY-EXACT(min), CANCEL-STRUCTURAL/PARTIAL/NONE(med rho),
ADAP-SCREEN-PASS/RELOC/AMBIG(slope), ENERGY-WALL-SEEN/BLIND; else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP =
42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MIN_PAIRS = 15; MIN_TRIPLES
= 15; MINB_REF = 0.679 (rtol 2e-2); GAPMIN_REF = 0.052, GAPMED_REF =
0.888 (rtol 5e-2); ID_WARD = 1e-8; S2_WARD = 1e-8; ADAP_TOL = 1e-10;
R2_LIN = 0.90; RHO_STRUCT = 0.10; RHO_PART = 0.50; SLOPE_PASS =
0.30; SLOPE_RELOC = 0.70; CTRL_KZ = 9; scramble seed 1.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run of
this script (22/22 with the identical bars; NO bar, band, count,
rule or enum was moved after it -- ID_WARD/S2_WARD = 1e-8 were set a
priori and the smoke measured max identity deviation 5.4e-20 (raw) /
2.5e-15 (normalized) and two-route pivot deviation 2.7e-15, ADAP_TOL
generous vs measured min ADAP +1.7e-08) measured, recorded here as
the honest context the frozen run must confirm: (a) the P2 hub is
NOT a linear inflow in alpha at step level (R^2 0.181, slope -3.31;
tau-screen slope of n_k -0.307; the raw-route hub R^2 0.444 -- the
step-level hub is jitter-dominated, honest negative for mapping a);
(b) the demand IS an exact nonnegative adaptation energy on the
truth side (min ADAP raw +1.7e-08, normalized +2.1e-02, B and B_+
PD on 37/37 raw + 37/37 normalized); (c) the leading difference
does NOT cancel structurally (raw median rho 0.781 -> CANCEL-NONE,
range [0.162, 1.000]; normalized median 1.000; STRUCTURAL note: on
down-flow transitions LIN < 0 forces rho = 1 exactly, since |Delta
s| = |LIN| + ADAP there -- the pivot flow is the same order as its
ingredients, no hub/demand cancellation at transition level); (d)
ADAP > 0 exact, raw tau-screen slope +0.613 with R^2 0.326 ->
ADAP-SCREEN-AMBIG (neither an O(1) demand floor nor clean
relocation; normalized slope -0.387); Delta s signs raw 18+/19-,
normalized 16+/21- (the pivot flow has NO stable sign); frame drift
is small (soft-direction overlap med 0.9921, min 0.9320; shared- vs
own-frame pivot ratio med 0.9996); the ENERGY-WALL control is SEEN
35/35 (every smooth raw triple has B or B_+ NOT PD -- the demand
term stops being an energy exactly where the wall is violated;
identity still exact 1.8e-13 where invertible).  Fail-first is
preserved: nothing was weakened; all four answers live in typed
measurements, the wards are identity/reproduction wards only.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as P2 SPEC
(ii), deterministic; (iii) OLS/corr population statistics as v900;
(iv) screens read the positive subset with the excluded count
printed; (v) pivot routes via np.linalg.solve / inv, symmetrized
inputs.

NO-GO COMPLIANCE (frozen): no Gershgorin/Brauer/Weyl bound on raw B
retried as content (W4 reproduction only); no rank-1 approximation
of the core update; no plain Herglotz wall certificate; no fit where
an identity is claimed (I1 is an exact ward; the OLS fits in I2 are
typed trend measurements, never identity claims).

NO RH claim: the Schur-Ward identity is exact finite linear algebra
for any symmetric pair -- it proves nothing about tau_h > 0 or
B-uniformity; the four answers are measurements on the deployed v563
window family.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids zetazero
/ nzeros / primerange / isprime / primepi / nextprime / prevprime);
v563 READ-ONLY; RNG only inside the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core
machinery verbatim from port_tangent_schur_probe.py (round 58) =
v900 chain via b_christoffel_deflation_probe.py; hub/demand
dictionary from port_tangent_schur_probe / arithmetic_lift_race_
probe (declared context).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/schur_ward_identity_probe.py
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
MIN_PAIRS = 15
MIN_TRIPLES = 15
MINB_REF = 0.679
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
ID_WARD = 1e-8
S2_WARD = 1e-8
ADAP_TOL = 1e-10
R2_LIN = 0.90
RHO_STRUCT = 0.10
RHO_PART = 0.50
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


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None):
    """v900 verbatim wall + fixed-core split (S retained per rung)."""
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
    return out


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


# ------------------------------ certified bounds (W4 repro only)
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


# ------------------------------ the Schur-Ward machinery
def split_parts(Mt):
    return float(Mt[0, 0]), Mt[1:, 0].copy(), Mt[1:, 1:].copy()


def to_frame(S, Q):
    Mt = Q.T @ S @ Q
    return 0.5 * (Mt + Mt.T)


def ward_transition(Mt, Mt2):
    """The exact SCHUR-WARD decomposition of the pivot flow.
    Returns None if B or B_+ is singular (caller counts)."""
    n, b, B = split_parts(Mt)
    n2, b2, B2 = split_parts(Mt2)
    evB = np.linalg.eigvalsh(B)
    evB2 = np.linalg.eigvalsh(B2)
    out = dict(minB=float(evB[0]), minB2=float(evB2[0]))
    try:
        x = np.linalg.solve(B, b)
        x2 = np.linalg.solve(B2, b2)
    except np.linalg.LinAlgError:
        return None
    s = n - float(b @ x)
    s2 = n2 - float(b2 @ x2)
    dn = n2 - n
    db = b2 - b
    dB = B2 - B
    lin = dn - 2.0 * float(x @ db) + float(x @ (dB @ x))
    r = db - dB @ x
    try:
        adap = float(r @ np.linalg.solve(B2, r))
    except np.linalg.LinAlgError:
        return None
    scale = max(abs(s) + abs(s2), 1.0)
    dev = abs((s2 - s) - (lin - adap)) / scale
    # two-route pivot (frame-free): s = 1 / (M^{-1})_{00}
    try:
        s_r2 = 1.0 / float(np.linalg.inv(Mt)[0, 0])
        dev_s2 = abs(s_r2 - s) / max(abs(s), 1e-300)
    except np.linalg.LinAlgError:
        dev_s2 = float("inf")
    out.update(n=n, s=s, s2=s2, ds=s2 - s, lin=lin, adap=adap,
               dev=dev, dev_s2=dev_s2,
               rho=abs(s2 - s) / max(abs(lin) + adap, 1e-300))
    return out


def main():
    section("PRIME.PORT.SCHUR.WARD.01 -- the exact flow law of the "
            "Schur pivot (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder (ONE pass) + P2/P3 reproduction")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    for kz in zones:
        r = gram_anatomy(kz)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
            truth.append(None)
            continue
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

    # W4 reproduction: P2 hub/demand/gap ledger + certified disaster
    rows = []
    for r1, r2 in steps:
        wS, VS = np.linalg.eigh(r1["S"])
        v = VS[:, 0]
        Q = householder_frame(v)
        Mt = to_frame(r2["S"] / r1["tau"], Q)
        nsc, b, B = split_parts(Mt)
        evB = np.linalg.eigvalsh(B)
        minB = float(evB[0])
        q = (float(b @ np.linalg.solve(B, b)) if minB > 0
             else float("nan"))
        gap = nsc - q
        bestg = max(gersh_min(B), gersh_scaled(B), cassini_scaled(B))
        rows.append(dict(r1=r1, r2=r2, Q=Q, Mt=Mt, n=nsc, q=q,
                         minB=minB, gap=gap, bestg=bestg))
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
          "certified disaster reproduced (best bound max %+.1f < 0 "
          "on all %d steps)"
          % (minB_all, MINB_REF, gmin, gmed, GAPMIN_REF, GAPMED_REF,
             float(np.max(bests)), len(rows)),
          ok_repro, kill="K2")

    # ------------------------------------------------------------ P
    section("P -- transition census (pairs + raw triples)")
    pairs = []
    for w1, w2 in zip(rows, rows[1:]):
        if w1["r2"] is w2["r1"]:
            pairs.append((w1, w2))
    check("P1 >= %d step pairs sharing the middle rung" % MIN_PAIRS,
          len(pairs) >= MIN_PAIRS, "%d pairs" % len(pairs),
          kill="K1")
    triples = []
    for rA, rB, rC in zip(truth, truth[1:], truth[2:]):
        if not (rA.get("core_ok") and rB.get("core_ok")
                and rC.get("core_ok")):
            continue
        if min(rA["lamS"], rB["lamS"], rC["lamS"]) <= 0.0:
            continue
        triples.append((rA, rB, rC))
    check("P2 >= %d raw triples of consecutive full-core PD rungs"
          % MIN_TRIPLES, len(triples) >= MIN_TRIPLES,
          "%d triples" % len(triples), kill="K1")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ I1
    section("I1 -- THE IDENTITY, exact on both routes")
    raw = []
    print("    RAW TRIPLES (frame of rA; S(rB) -> S(rC), no "
          "normalization):")
    print("    hA->hB->hC     s          s_+        LIN        "
          "ADAP       rho     dev")
    for rA, rB, rC in triples:
        wS, VS = np.linalg.eigh(rA["S"])
        Q = householder_frame(VS[:, 0])
        t = ward_transition(to_frame(rB["S"], Q),
                            to_frame(rC["S"], Q))
        if t is None:
            continue
        t["rA"], t["rB"], t["rC"] = rA, rB, rC
        raw.append(t)
        print("    %3d->%3d->%3d  %+.3e %+.3e %+.3e %.3e  %6.3f  "
              "%.1e"
              % (rA["h"], rB["h"], rC["h"], t["s"], t["s2"],
                 t["lin"], t["adap"], t["rho"], t["dev"]),
              flush=True)
    norm = []
    for w1, w2 in pairs:
        # shared frame of step k: M_+ expressed in Q_k
        Mt2 = to_frame(w2["r2"]["S"] / w2["r1"]["tau"], w1["Q"])
        t = ward_transition(w1["Mt"], Mt2)
        if t is None:
            continue
        t["w1"], t["w2"] = w1, w2
        norm.append(t)
    ok_pd = (all(t["minB"] > 0 and t["minB2"] > 0 for t in raw)
             and all(t["minB"] > 0 and t["minB2"] > 0
                     for t in norm))
    check("I1.a WARD B and B_+ PD on every truth transition "
          "(raw %d/%d, normalized %d/%d)"
          % (sum(1 for t in raw if t["minB2"] > 0), len(raw),
             sum(1 for t in norm if t["minB2"] > 0), len(norm)),
          ok_pd and len(raw) == len(triples)
          and len(norm) == len(pairs), kill="K2")
    dev_raw = max(t["dev"] for t in raw)
    dev_nrm = max(t["dev"] for t in norm)
    check("I1.b WARD THE IDENTITY s_+ - s = LIN - ADAP: max dev "
          "raw %.2e, normalized %.2e <= %.0e"
          % (dev_raw, dev_nrm, ID_WARD),
          max(dev_raw, dev_nrm) <= ID_WARD, kill="K2")
    dev_s2 = max(max(t["dev_s2"] for t in raw),
                 max(t["dev_s2"] for t in norm))
    check("I1.c WARD two-route pivot s = n - b^T B^{-1} b = "
          "1/(M^{-1})_00: max rel dev %.2e <= %.0e"
          % (dev_s2, S2_WARD), dev_s2 <= S2_WARD, kill="K2")
    min_adap = min(min(t["adap"] for t in raw),
                   min(t["adap"] for t in norm))
    check("I1.d WARD ADAP >= 0 on the truth side (min %.2e >= "
          "-%.0e)" % (min_adap, ADAP_TOL), min_adap >= -ADAP_TOL,
          kill="K2")

    # ------------------------------------------------------------ I2
    section("I2 -- the four typed answers")
    # (a) hub inflow
    ns = np.array([w["n"] for w in rows])
    als = np.array([w["r2"]["alpha"] for w in rows])
    tts = np.array([w["r1"]["tau"] for w in rows])
    _a, sl_na, r2_na = ols_line(als, ns)
    _a, sl_nt, _r = ols_line(np.log(tts), np.log(np.abs(ns)))
    nB = np.array([t["n"] for t in raw])
    alB = np.array([t["rB"]["alpha"] for t in raw])
    _a, sl_nBa, r2_nBa = ols_line(alB, nB)
    print("    (a) hub: P2 hub n_k vs alpha slope %+.3f R^2 %.3f; "
          "tau-screen slope of n_k %+.3f; raw hub <v_A, S(rB) v_A> "
          "vs alpha R^2 %.3f"
          % (sl_na, r2_na, sl_nt, r2_nBa))
    if r2_na >= R2_LIN:
        i2a = "HUB-LINEAR(R2=%.3f, slope=%+.3f)" % (r2_na, sl_na)
    else:
        i2a = "HUB-NOT-LINEAR(R2=%.3f)" % r2_na
    check("I2.a typed: %s (band R^2 >= %.2f)" % (i2a, R2_LIN), True)
    # (b) demand = adaptation energy
    i2b = "DEMAND-ENERGY-EXACT(min=%.1e raw, %.1e norm)" % (
        min(t["adap"] for t in raw), min(t["adap"] for t in norm))
    check("I2.b typed: %s (exact nonnegativity warded in I1.d; "
          "B_+ PD warded in I1.a)" % i2b, True)
    # (c) leading cancellation
    rho_raw = float(np.median([t["rho"] for t in raw]))
    rho_nrm = float(np.median([t["rho"] for t in norm]))
    if rho_raw <= RHO_STRUCT:
        i2c = "CANCEL-STRUCTURAL(med-rho=%.3f)" % rho_raw
    elif rho_raw <= RHO_PART:
        i2c = "CANCEL-PARTIAL(med-rho=%.3f)" % rho_raw
    else:
        i2c = "CANCEL-NONE(med-rho=%.3f)" % rho_raw
    print("    (c) rho = |Delta s|/(|LIN| + ADAP): raw med %.3f "
          "(range [%.3f, %.3f]); normalized med %.3f"
          % (rho_raw, float(np.min([t["rho"] for t in raw])),
             float(np.max([t["rho"] for t in raw])), rho_nrm))
    check("I2.c typed: %s (bands STRUCTURAL <= %.2f, PARTIAL <= "
          "%.2f; PRIMARY = raw triples)" % (i2c, RHO_STRUCT,
                                            RHO_PART), True)
    # (d) second-order correction: sign + tau-screen
    ad_raw = np.array([t["adap"] for t in raw])
    tau_B = np.array([t["rB"]["tau"] for t in raw])
    posa = ad_raw > 0
    _a, sl_ad, r2_ad = ols_line(np.log(tau_B[posa]),
                                np.log(ad_raw[posa]))
    ad_nrm = np.array([t["adap"] for t in norm])
    tau_n = np.array([t["w2"]["r1"]["tau"] for t in norm])
    posn = ad_nrm > 0
    _a, sl_adn, _r = ols_line(np.log(tau_n[posn]),
                              np.log(ad_nrm[posn]))
    ds_raw = np.array([t["ds"] for t in raw])
    ds_nrm = np.array([t["ds"] for t in norm])
    print("    (d) ADAP raw range [%.2e, %.2e], tau-screen slope "
          "%+.4f (R^2 %.3f, %d excluded); normalized slope %+.4f; "
          "Delta s signs raw %d+/%d-, normalized %d+/%d-"
          % (float(np.min(ad_raw)), float(np.max(ad_raw)), sl_ad,
             r2_ad, int(np.sum(~posa)), sl_adn,
             int(np.sum(ds_raw > 0)), int(np.sum(ds_raw < 0)),
             int(np.sum(ds_nrm > 0)), int(np.sum(ds_nrm < 0))))
    if abs(sl_ad) <= SLOPE_PASS:
        i2d = "ADAP-SCREEN-PASS(slope=%+.3f)" % sl_ad
    elif sl_ad >= SLOPE_RELOC:
        i2d = "ADAP-SCREEN-RELOC(slope=%+.3f)" % sl_ad
    else:
        i2d = "ADAP-SCREEN-AMBIG(slope=%+.3f)" % sl_ad
    check("I2.d typed: %s (bands PASS |s| <= %.2f, RELOC s >= "
          "%.2f; PRIMARY = raw triples vs tau(rB))"
          % (i2d, SLOPE_PASS, SLOPE_RELOC), True)

    # ------------------------------------------------------------ I3
    section("I3 -- frame-drift diagnostics (prints only)")
    ovl = []
    for rA, rB in zip(full, full[1:]):
        _w, VA = np.linalg.eigh(rA["S"])
        _w, VB = np.linalg.eigh(rB["S"])
        ovl.append(float(VA[:, 0] @ VB[:, 0]) ** 2)
    ratio = [t["s2"] / t["w2"]["gap"] for t in norm
             if np.isfinite(t["w2"]["gap"]) and t["w2"]["gap"] != 0]
    print("    consecutive soft-direction overlap <v_k, v_k+1>^2: "
          "med %.4f, min %.4f; shared-frame vs own-frame pivot of "
          "the second step: med ratio %.4f (range [%.4f, %.4f])"
          % (float(np.median(ovl)), float(np.min(ovl)),
             float(np.median(ratio)), float(np.min(ratio)),
             float(np.max(ratio))))

    # ------------------------------------------------------------ C
    section("C -- controls: smooth world + Epstein/scramble")
    check("C0.1 WARD truth wall holds (neg(A) = 0 on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    sm = []
    n_viol = 0
    for kz in zones:
        rs = gram_anatomy(kz, world_fn=world_smooth)
        if not isinstance(rs, dict):
            continue
        if rs["negA"] > 0:
            n_viol += 1
        if rs.get("core_ok") and "S" in rs:
            sm.append(rs)
    check("C1.1 WARD smooth violates at rung level (neg(A) > 0 on "
          "%d rungs)" % n_viol, n_viol > 0, kill="K2")
    sm.sort(key=lambda r: (r["h"], r["kz"]))
    n_dead = 0
    n_tr = 0
    dev_sm = 0.0
    for rA, rB, rC in zip(sm, sm[1:], sm[2:]):
        n_tr += 1
        _w, VS = np.linalg.eigh(rA["S"])
        Q = householder_frame(VS[:, 0])
        t = ward_transition(to_frame(rB["S"], Q),
                            to_frame(rC["S"], Q))
        if t is None or t["minB"] <= 0 or t["minB2"] <= 0:
            n_dead += 1
            if t is not None:
                dev_sm = max(dev_sm, t["dev"])
        else:
            dev_sm = max(dev_sm, t["dev"])
    ew = ("ENERGY-WALL-SEEN(%d/%d)" % (n_dead, n_tr) if n_dead > 0
          else "ENERGY-WALL-BLIND(0/%d)" % n_tr)
    print("  C1.2 -- smooth raw triples: B or B_+ NOT PD on %d of "
          "%d (the demand term stops being an energy exactly where "
          "the wall is violated); identity where invertible: max "
          "dev %.1e" % (n_dead, n_tr, dev_sm))
    check("C1.2 typed: %s" % ew, True)
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
        if not isinstance(r, dict):
            print("    %-9s: chain dies -> fires" % name)
            continue
        f = r["negA"] > 0
        fired_all &= f
        print("    %-9s: tau %+.3e  neg(A) %d -> %s"
              % (name, r["tau"], r["negA"],
                 "FIRES" if f else "SILENT"), flush=True)
    check("C2.1 WARD both controls fire", fired_all, kill="K2")

    return finish(dict(dev=max(dev_raw, dev_nrm), i2a=i2a, i2b=i2b,
                       i2c=i2c, i2d=i2d, ew=ew))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("SCHURWARD-MEASURED / WARD-IDENTITY-EXACT"
                   "(%(dev).1e) / %(i2a)s / %(i2b)s / %(i2c)s / "
                   "%(i2d)s / %(ew)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the Schur-Ward identity is exact linear
  algebra for ANY symmetric pair -- it carries no wall content by
  itself.  All wall content is in the measured signs, cancellation
  ratios and tau-screens of its terms and in the smooth-world
  ENERGY-WALL control.  A RELOC screen on ADAP means the adaptation
  energy collapses with tau (relocation, not an O(1) demand floor)
  -- recorded either way.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
