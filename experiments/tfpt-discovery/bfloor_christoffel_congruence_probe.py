#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bfloor_christoffel_congruence_probe --
PRIME.PORT.BFLOOR.CONGRUENCE.02
(EXPLORATION ONLY, experiments/; round 60, theorem-engineering on
the RH-side wall: SECOND attempt at a certified B-floor, informed
by two round-59 facts -- the node channel is DECOUPLED from the
defect (b_christoffel_deflation_probe: rank-1 efficiency 0.0000,
deflated margin pure relocation) and the Radau weight at the
classical node IS numerically the Christoffel function lambda_h
and tau-DEcorrelated (wall_gram_radau_probe: w*/lam_h med 0.9978,
screen R^2 0.089).  THE QUESTION: does the CHRISTOFFEL-FUNCTION
CONGRUENCE at the core nodes revive the classical certified
bounds on the co-block B?  2026-08-10.)

THE OBJECT (round-58/59 verbatim).  P2/P3 reduced the wall update
to (B_h PD) AND (n_h > q_h) in the frozen Householder frame of
the core Schur complement S (8 core folds CORE_J, soft direction
of S_1 rotated out; B = 7x7 co-block of Mt = Q^T (S_2/tau_1) Q).
Measured: lam_min(B) = 0.679 O(1) ladder-wide, but ALL classical
certified bounds on the RAW B are negative on ALL steps (best
max -88; cond(B) ~ 220, coherent off-diagonal mass).

THE CONGRUENCE (frozen; the honest formulation).  The core
coordinates of S are node coordinates: fold j in CORE_J <-> node
y_j = cos(2 pi j / L).  A node-diagonal damping D = diag(g(y_j))
acts on the CORE SURFACE: Stil_r = D_r S_r D_r (a congruence: by
Sylvester, Stil PSD <=> S PSD -- the wall content is untouched
and CANNOT be faked; warded).  Schur frames do not commute with
diagonal damping, so the P2 split is REBUILT in the damped
coordinates (the same cut degree of freedom P2 itself exercises):
Qtil = Householder(soft vector of Stil_1), Mtil = Qtil^T
(Stil_2/tau_1) Qtil, Btil = Mtil[1:, 1:], ntil = Mtil[0, 0].
Certified bounds (G1 Gershgorin / G2 scaled Gershgorin-diagonal
dominance / G3 Brauer-Cassini, the recorded P3 battery) are
re-run on Btil -- allowed now because the congruence is NEW; a
certified Btil floor + explicit ntil > qtil certifies Mtil PSD
<=> S_2 PSD.  SAID PLAINLY (frozen): Btil is NOT literally
D B D -- the literal diagonal congruence of B in the rotated
frame has no node meaning; the node-diagonal congruence lives on
S and the split is rebuilt (this is the natural reading of the
damping-congruence program on this surface, frozen a priori).

THE FROZEN VARIANT LIST (all source-only: comb linear algebra of
(xs, ws, ys, vs) + the chain; NO tau, NO defect eigenvector, NO
spectral data of A enters any D):
  V1  g_j = lambda_h(y_j)^{+1/2}   (Christoffel damping)
  V2  g_j = lambda_h(y_j)^{-1/2}   (inverse Christoffel)
  V3  g_j = T_j^{+1/2}, T_j = v_j K_h(y_j, y_j)  (the Gram
      diagonal at the core node -- the natural Jacobi variant:
      A_jj = 1 - T_j)
  V4  g_j = lambda_h^{smooth}(y_j)^{+1/2}  (PRIME-FREE: the
      Christoffel function of the smooth-world chain at the same
      rung -- the construction never touches the true comb)
(lambda_h(y) = 1 / K_h(y, y), K_h the CD-kernel diagonal of the
rung's own positive chain; the plain diagonal scaling of B is
ALREADY in the battery as G2 -- recorded, not a new variant.)

WHAT IS MEASURED (frozen; typed, never kills): per variant the
step ladder of lam_min(Btil), cond(Btil), off-diagonal mass
odm = ||offdiag||_F / ||diag||_F, max off-diagonal correlation,
certified best bound bg = max(G1, G2, G3)(Btil), the gap half
ntil - qtil where Btil is PD, and the tau-screen of the certified
floor (slope of log bg vs log tau_1 on the positive subset;
bands PASS |s| <= 0.30 / RELOC >= 0.70 / else AMBIG).  TYPED per
variant: CERT-ACHIEVED(all steps, min bg) / CERT-PARTIAL(n/N) /
CERT-DEAD.  If ALL variants fail: WHERE the off-diagonal mass
survives -- the worst-Gershgorin-row histogram and the med max
off-diagonal correlation per variant (printed).

FROZEN PROTOCOL (pipeline verbatim from
b_christoffel_deflation_probe = v900 chain; ONE Gram per rung;
window memoization; big arrays dropped after use):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2
     >= 30 full-core rungs; W3a truth all-PSD (A, R, S); W3b >=
     20 consecutive full-core steps; W4 REPRODUCTION P2/P3
     ledger: min lam_min(B) == 0.679 (rtol 2e-2), gap min/med ==
     0.052/0.888 (rtol 5e-2), raw-B certified disaster (best
     bound < 0 on every step).

 G1  THE CONGRUENCE WARDS (kill -> WARD-BROKEN): G1.a node values
     y_j == the folded NEG node at fold j (exact index tie, max
     dev <= NODE_TIE); G1.b PSD equivalence: lam_min(Mtil) > 0 on
     every truth step for every variant (Sylvester; S_2 PSD is
     warded in W3) AND full signature tie on the first SIG_SPOT
     steps (eig sign counts of Mtil == of Stil_2/tau_1 == of
     S_2/tau_1); G1.c D finite and positive on every step
     (K_h(y, y) > 0).

 G2  THE MEASUREMENT (typed as frozen above), one subsection per
     variant V1..V4; V4 skips steps whose smooth companion rung
     has no complete chain/core (counted).

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) =
     0 everywhere; C1 smooth world neg(A) > 0 on >= 1 rung; C2
     Epstein x^2+5y^2 comb + scramble (seed 1) at kz 9 fire
     (neg(A) > 0 or chain death); C3 SIGNATURE HONESTY on the
     scramble: where the scramble rung carries a core S with
     lam_min(S) < 0, the V1 congruence CANNOT flip it
     (lam_min(Stil) < 0 still) -- the congruence cannot
     manufacture positivity (skipped with disclosure if the
     scramble core dies; the Sylvester ward G1.b already carries
     the content on truth).

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
congruence / control wards (W4, G1, C0-C3) -> WARD-BROKEN.  All
G2-typed outcomes are measurements, never kills.

VERDICT (frozen enum): BFLOORCONG-MEASURED with typed sublabels
CONG-EXACT (wards), V1-/V2-/V3-/V4-CERT-<ACHIEVED(minbg) |
PARTIAL(n/N) | DEAD>, BEST(variant, min bg, screen), and the
headline CERTIFIED-BFLOOR-ACHIEVED / CERTIFIED-BFLOOR-FAILED
(where the mass survives); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2);
NODE_TIE = 1e-12; SIG_SPOT = 3; SLOPE_PASS = 0.30; SLOPE_RELOC =
0.70; CTRL_KZ = 9; scramble seed 1.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): TWO smoke
runs (20/20 both; identical bars; NO bar, band, count, enum or
typed rule was moved).  Smoke 1 exposed a PRESENTATION defect:
the raw best-bound numbers are SCALE-DEPENDENT (the Christoffel
damping shrinks the whole co-block, so V1's best bound
-3.79e-04 looks "close to zero" while being as hopeless as the
raw -88 relative to its own floor).  AMENDMENT (disclosed): the
scale-invariant ratio cert/floor was added to the per-variant
print and the FAILED-headline payload now reports it (enum names
unchanged; a pure honesty upgrade -- fail-first preserved).
Smoke 2 MEASURED, recorded as the honest context the frozen run
must confirm: the Christoffel-function congruence does NOT
revive the classical certificates -- all four variants are
CERT-DEAD (certified best bound < 0 on 39/39 steps each), and in
the scale-invariant reading the congruence is NOT even a partial
decoherer: cert/floor med -153.5 (V1) / -151.2 (V2) / -148.8
(V3) / -140.5 (V4) vs raw -130 -- every frozen damping leaves
the relative certified gap AT or slightly WORSE than raw;
cond(Btil) med 214..229 vs raw 220 (no compression), odm med
1.17..1.24, max off-diagonal correlation med 0.958..0.960
(untouched); the failure is FRAME-CONCENTRATED, not node-local:
the worst scaled-Gershgorin row is row 0 of the co-block --
the first co-direction after the soft rotation -- on 39/39
steps in EVERY variant (hist [39,0,0,0,0,0,0]); the PRIME-FREE
V4 tracks the true-comb V1 closely (med -140.5 vs -153.5: the
damping content is smooth -- consistent with the round-59
tau-decorrelation of the Radau/Christoffel weight); the true
floors stay positive on all steps (V3 min 6.65e-01 ~ the raw
0.679; V1/V4 floors are the same object rescaled to ~1.9e-06);
CERT screens vacuous (positive subset 0, printed); wards exact
(node tie 0.0, PSD equivalence + signature tie 3/3, damping
finite/positive 0 dead); controls: smooth neg(A) > 0 on 42/42,
Epstein neg(A) = 55, scramble neg(A) = 37; the scramble core
dies at kz 9 so C3 falls back to its disclosed skip (the
Sylvester ward G1.b carries the cannot-fake-positivity content
on truth).  Headline at smoke: CERTIFIED-BFLOOR-FAILED(best rel
cert/floor med -140.5 at V4 vs raw -130).  Fail-first preserved:
nothing was weakened; all typed outcomes are measurements.

SPEC v2 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v2: (i)
window memoization per (kz, seed); (ii) Householder frame as P2
SPEC (ii), deterministic, applied to Stil_1's soft vector; (iii)
lambda_h(y) = 1/(p(y)^T p(y)) with p from the rung's own chain
(h terms), smooth variant from the smooth-world chain of the SAME
kz; (iv) OLS population statistics as v900; screens read the
positive subset with excluded counts printed; (v) cond and odm on
Btil as printed; the worst-row histogram over co-block indices
0..6.

NO-GO COMPLIANCE (frozen): the Gershgorin/Cassini battery on RAW
B enters ONLY as the W4 reproduction of the recorded disaster;
the battery on Btil is allowed because the congruence is new (the
round-58 no-go bans the RAW retry); no rank-1 approximation; no
plain Herglotz certificate; no fit where an identity is claimed.

NO RH claim: a certified Btil floor would certify single steps of
the deployed ladder only (together with the explicit gap half);
nothing here proves B-uniformity, wall positivity for all h, or
any tail statement.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core
machinery verbatim from b_christoffel_deflation_probe.py /
port_tangent_schur_probe.py / port_bfloor_uniformity_probe.py
(rounds 58-59) = v900 chain; the Radau/Christoffel identification
from wall_gram_radau_probe.py + case_edge_christoffel_probe.py
(round 59, declared inputs).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/bfloor_christoffel_congruence_probe.py
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
NODE_TIE = 1e-12
SIG_SPOT = 3
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
VARIANTS = ("V1", "V2", "V3", "V4")

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


# --------------- pipeline, verbatim (b_christoffel_deflation)
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
        out["ysv"] = (ys, vs)
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


def max_offdiag_corr(B):
    d = np.sqrt(np.maximum(np.diag(B), 1e-300))
    C = np.abs(B) / np.outer(d, d)
    np.fill_diagonal(C, 0.0)
    return float(np.max(C))


def damping(r, variant, sm=None):
    """The frozen node-diagonal D for one rung (None if
    unavailable)."""
    y = r["y_core"]
    if variant == "V4":
        if sm is None or "chain" not in sm:
            return None
        al, be, m0 = sm["chain"]
        P = eval_chain(al, be, m0, y, sm["h"])
    else:
        al, be, m0 = r["chain"]
        P = eval_chain(al, be, m0, y, r["h"])
    K = np.sum(P * P, axis=1)
    if np.any(~np.isfinite(K)) or np.any(K <= 0.0):
        return None
    lam_ch = 1.0 / K
    if variant == "V1" or variant == "V4":
        g = np.sqrt(lam_ch)
    elif variant == "V2":
        g = 1.0 / np.sqrt(lam_ch)
    else:
        g = np.sqrt(r["v_core"] * K)
    if np.any(~np.isfinite(g)) or np.any(g <= 0.0):
        return None
    return g


def main():
    section("PRIME.PORT.BFLOOR.CONGRUENCE.02 -- the Christoffel "
            "node congruence on the co-block surface "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + P2/P3 reproduction")
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
        rows.append(dict(r1=r1, r2=r2, B=B, minB=minB, gap=gap,
                         bestg=best_cert(B),
                         cond=float(np.linalg.cond(B))))
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
          "certified disaster reproduced (best bound max %+.1f < "
          "0 on all %d steps; med cond(B) %.1f)"
          % (minB_all, MINB_REF, gmin, gmed, GAPMIN_REF,
             GAPMED_REF, float(np.max(bests)), len(rows),
             float(np.median([w["cond"] for w in rows]))),
          ok_repro, kill="K2")

    # ------------------------------------------------------------ G1
    section("G1 -- congruence wards (node tie, PSD equivalence, "
            "signature)")
    tie = 0.0
    for r in full:
        yj = np.cos(2.0 * math.pi * np.array(CORE_J, float)
                    / r["L"])
        tie = max(tie, float(np.max(np.abs(yj - r["y_core"]))))
    check("G1.a WARD node tie y_core == cos(2 pi j / L): max dev "
          "%.2e <= %.0e" % (tie, NODE_TIE), tie <= NODE_TIE,
          kill="K2")
    var_rows = {v: [] for v in VARIANTS}
    d_dead = {v: 0 for v in VARIANTS}
    psd_ok = True
    sig_ok = True
    for irow, (r1, r2) in enumerate(steps):
        for v in VARIANTS:
            g1 = damping(r1, v, sm=sm_map.get(r1["kz"]))
            g2 = damping(r2, v, sm=sm_map.get(r2["kz"]))
            if g1 is None or g2 is None:
                d_dead[v] += 1
                continue
            St1 = (g1[:, None] * r1["S"]) * g1[None, :]
            St2 = (g2[:, None] * r2["S"]) * g2[None, :]
            St1 = 0.5 * (St1 + St1.T)
            St2 = 0.5 * (St2 + St2.T)
            wS, VS = np.linalg.eigh(St1)
            Q = householder_frame(VS[:, 0])
            Mt = Q.T @ (St2 / r1["tau"]) @ Q
            Mt = 0.5 * (Mt + Mt.T)
            evM = np.linalg.eigvalsh(Mt)
            psd_ok &= float(evM[0]) > 0.0
            if irow < SIG_SPOT:
                evS2 = np.linalg.eigvalsh(r2["S"] / r1["tau"])
                sig_ok &= (int(np.sum(evM > 0))
                           == int(np.sum(evS2 > 0)))
            nsc = float(Mt[0, 0])
            b = Mt[1:, 0]
            B = Mt[1:, 1:]
            minB = float(np.linalg.eigvalsh(B)[0])
            gap = (nsc - float(b @ np.linalg.solve(B, b))
                   if minB > 0 else float("nan"))
            dg = np.abs(np.diag(B))
            off = B - np.diag(np.diag(B))
            var_rows[v].append(dict(
                tau=r1["tau"], h2=r2["h"], minB=minB, gap=gap,
                bg=best_cert(B), cond=float(np.linalg.cond(B)),
                odm=float(np.linalg.norm(off)
                          / max(np.linalg.norm(np.diag(dg)),
                                1e-300)),
                moc=max_offdiag_corr(B),
                wrow=worst_gersh_row(B)))
    check("G1.b WARD PSD equivalence + signature: lam_min(Mtil) > "
          "0 on every truth step, all variants; signature tie on "
          "%d spot steps" % SIG_SPOT, psd_ok and sig_ok,
          kill="K2")
    check("G1.c WARD damping finite/positive (dead: %s)"
          % d_dead, all(d_dead[v] == 0 for v in ("V1", "V2", "V3")),
          kill="K2")

    # ------------------------------------------------------------ G2
    section("G2 -- the measurement per variant")
    labels = {}
    best_var, best_min = None, float("-inf")
    for v in VARIANTS:
        rowsv = var_rows[v]
        if not rowsv:
            labels[v] = "%s-CERT-DEAD(no steps)" % v
            continue
        bg = np.array([x["bg"] for x in rowsv])
        mb = np.array([x["minB"] for x in rowsv])
        tt = np.array([x["tau"] for x in rowsv])
        n_pos = int(np.sum(bg > 0))
        posm = bg > 0
        if np.sum(posm) >= 3:
            _a, sl, r2f = ols_line(np.log(tt[posm]),
                                   np.log(bg[posm]))
            scr = "slope %+.3f (R^2 %.3f)" % (sl, r2f)
        else:
            scr = "screen vacuous (positive subset %d)" % n_pos
        wr = np.bincount([x["wrow"] for x in rowsv], minlength=7)
        relg = bg / np.maximum(mb, 1e-300)
        print("  %s: certified > 0 on %d/%d; best bound min/med/"
              "max %+.2e/%+.2e/%+.2e; lam_min(Btil) min %.3e; "
              "SCALE-INVARIANT cert/floor med %+.1f (raw ref "
              "-130); cond med %.1f; odm med %.2f; max offdiag "
              "corr med %.3f; worst-row hist %s; %s"
              % (v, n_pos, len(rowsv), float(np.min(bg)),
                 float(np.median(bg)), float(np.max(bg)),
                 float(np.min(mb)), float(np.median(relg)),
                 float(np.median([x["cond"] for x in rowsv])),
                 float(np.median([x["odm"] for x in rowsv])),
                 float(np.median([x["moc"] for x in rowsv])),
                 wr.tolist(), scr), flush=True)
        if n_pos == len(rowsv):
            labels[v] = "%s-CERT-ACHIEVED(min=%.3e)" % (
                v, float(np.min(bg)))
        elif n_pos > 0:
            labels[v] = "%s-CERT-PARTIAL(%d/%d)" % (v, n_pos,
                                                    len(rowsv))
        else:
            labels[v] = "%s-CERT-DEAD" % v
        if float(np.median(relg)) > best_min:
            best_min = float(np.median(relg))
            best_var = v
    for v in VARIANTS:
        check("G2.%s typed: %s" % (v, labels[v]), True)
    n_ach = sum(1 for v in VARIANTS
                if "ACHIEVED" in labels.get(v, ""))
    headline = ("CERTIFIED-BFLOOR-ACHIEVED(%d variants)" % n_ach
                if n_ach else
                "CERTIFIED-BFLOOR-FAILED(best rel cert/floor med "
                "%+.1f at %s vs raw -130)" % (best_min, best_var))
    check("G2.h typed headline: %s" % headline, True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    check("C0.1 WARD truth wall holds (neg(A) = 0 on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    n_viol = sum(1 for kz in zones
                 if isinstance(sm_map.get(kz), dict)
                 and sm_map[kz]["negA"] > 0)
    check("C1 WARD smooth world violates (neg(A) > 0 on %d "
          "rungs)" % n_viol, n_viol > 0, kill="K2")
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
        g = damping(rsc, "V1")
        if g is not None:
            St = (g[:, None] * rsc["S"]) * g[None, :]
            lam_t = float(np.linalg.eigvalsh(
                0.5 * (St + St.T))[0])
            c3_ok = lam_t < 0.0
            c3_msg = ("lam_min(S_scr) %.3e -> lam_min(Stil_scr) "
                      "%.3e stays negative" % (rsc["lamS"], lam_t))
    check("C3 WARD the congruence cannot manufacture positivity "
          "on the scramble: %s" % c3_msg, c3_ok, kill="K2")

    labels["headline"] = headline
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
        VERDICT = ("BFLOORCONG-MEASURED / CONG-EXACT / %s / %s / "
                   "%s / %s / %s"
                   % (labels.get("V1", "-"), labels.get("V2", "-"),
                      labels.get("V3", "-"), labels.get("V4", "-"),
                      labels.get("headline", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the node-diagonal congruence is
  PSD-equivalent to the core surface (Sylvester, warded) -- it
  cannot fake the wall and it cannot lose it; the only question
  is whether classical certificates SEE the floor in the damped
  coordinates.  A CERT-DEAD outcome names the seat of the
  surviving off-diagonal mass; a CERT-ACHIEVED floor would
  certify single deployed steps only (with the explicit gap
  half), never uniformity in h.  NO RH claim.  No marker
  moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
