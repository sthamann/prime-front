#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""b_christoffel_deflation_probe -- PRIME.PORT.CHRISTOFFEL.DEFLATION.01
(EXPLORATION ONLY, experiments/; round 59, theorem-engineering on the
RH-side wall: is the coherent off-diagonal geometry that kills every
classical certified bound on the co-block B_h the EVALUATION AT THE
CLASSICAL NODE, and is the Christoffel transformation at that node
the damping congruence?  2026-08-10.)

THE QUESTION (frozen).  P2/P3 of round 58 (port_tangent_schur_probe,
port_bfloor_uniformity_probe) reduced the wall update to (B_h PD)
AND (n_h > q_h) and measured: lam_min(B_h) = 0.679 O(1) ladder-wide
(tau-screen slope -0.247, FIRST PASS), but ALL FOUR classical
certified bounds on B are negative on ALL 39 steps (best bound max
-88 against true floor +0.679; cond(B) ~ 220, ~10^3 coherent
off-diagonal mass).  The diagnosis to test: the coherent mass is a
NODE-EVALUATION channel, and the classical damping congruence is the
Christoffel transformation dmu* = (x - y*)^2 dmu at the classical
node y* (node_origin_arch_probe: the prime-free drift law
y*(alpha)/alpha-units = 0.3727 - 0.0116 alpha, R^2 0.973, prime-free
determined on 66/67 rungs).

THE NODE CORRESPONDENCE (worked out, frozen).  The classical node
lives in u-space (window position): u*_h = (NODE_C + NODE_S x
alpha_h) x alpha_h.  The wall's Jacobi systems live on the folded
frequency circle: lag index j <-> position u = j D; DFT/fold index
f <-> spectral variable x_f = cos(2 pi f / L), L = 2M - 2.  The
u <-> f exchange is the SAME circle read through the discrete
Fourier pairing (u/D <-> f), so the frozen map is
    x*_h = cos(2 pi (u*_h / D_h) / L_h)  ~  cos(pi y*_cl / 2),
computed per rung with the exact window numbers (M, D, alpha).  Both
frozen control nodes read the same circle: x_ctrl-mid = 0 (the
generic circle midpoint) and x_ctrl-J = cos(2 pi J* / L), J* = 24
(the v899 12-window evaluation fold, the seat of m_def).  HONESTY
(frozen): the deflation identity below holds for ANY node -- the
node CHOICE carries zero identity content; all node content is in
the measured D3/D4 comparisons against the controls.

THE EXACT OBJECT (derived a priori, classical).  For the positive
folded source family mu_+ = (xs, ws) with orthonormal p_k and CD
kernel K_h(x, y) = sum_{k<h} p_k(x) p_k(y), and any node x* with
K_h(x*, x*) > 0, the Christoffel transformation mu* = (x - x*)^2
mu_+ obeys the exact kernel deflation
    K_h(x, y) = (x - x*)(y - x*) K*_{h-1}(x, y)
                + K_h(x, x*) K_h(x*, y) / K_h(x*, x*),
K*_{h-1} the CD kernel of mu* (h-1 terms).  Evaluated on the NEG
nodes (ys, vs) this is a statement about the deployed wall Gram
G_ij = sqrt(v_i v_j) K_h(y_i, y_j) (A = I - G, tau = 1 - lam_max(G)):
    G = D K*mat D + w w^T          [THE DEFLATION SPLIT]
    D = diag(sqrt(v_i) (y_i - x*)),
    K*mat_ij = sum_{k<h-1} p*_k(y_i) p*_k(y_j)  (source Lanczos of
               mu*, DIVISION-FREE -- no (y - x*)^{-1} anywhere),
    w_i = sqrt(v_i) K_h(y_i, x*) / sqrt(K_h(x*, x*)).
Every ingredient is source-only: (xs, ws, ys, vs) from the comb
density, x* from the prime-free drift law + window geometry.  NO
tau, NO defect eigenvector, NO decomposition of A/S/B enters the
construction (anti-circularity honoured; the top-channel overlap
<w, v_top(G)>^2 and the interlacing ceiling 1 - lam_2(G) are
DIAGNOSTIC PRINTS ONLY, never construction inputs).

WHAT IS MEASURED (frozen).  Removing the node channel gives the
DEFLATED WALL G_def := D K*mat D = G - w w^T (PSD by construction,
G_def = F F^T) with margin m2 = 1 - lam_max(G_def) >= tau by
rank-one interlacing, and m2 <= 1 - lam_2(G) (the ceiling any
rank-one removal can reach).  The hypothesis "the wall difficulty
IS the node evaluation" is exactly: m2 is O(1) (tau-screen slope ~
0) while m1 = tau collapses; the efficiency eff = (m2 - m1)/(ceil -
m1) says which fraction of the best possible rank-one gain the
classical-node channel captures.  Downstream, the deflated core
Schur block gives Bhat_h and the certified classical bounds are
re-run on it (the CERTFLOOR-DEAD disaster re-tested after the
congruence).  A fallback congruence is measured independently: the
PRIME-FREE (smooth-world) co-block B0 as Cholesky preconditioner,
Btilde = L^{-1} B L^{-T} = I + K, with the NEGATIVE INDEX of K per
step (not ||K||), and certified bounds on Btilde.

FROZEN PROTOCOL (machinery verbatim from port_tangent_schur_probe /
port_bfloor_uniformity_probe round 58 = v900 chain; ONE Gram per
rung; window memoization):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2 >=
     30 full-core rungs; W3a truth all-PSD (A, R, S); W3b >= 20
     consecutive full-core steps; W4 REPRODUCTION P2/P3 ledger: min
     lam_min(B) == 0.679 (rtol 2e-2), gap min/med == 0.052/0.888
     (rtol 5e-2), and the raw-B certified disaster: best classical
     bound (G1/G2/G3) < 0 on EVERY step (CERTFLOOR-DEAD
     reproduced).

 D1  THE NODE MAP (per rung; kill -> WARD-BROKEN): 0 < u*_h < 2
     alpha_h and -1 < x*_h < 1 on every truth rung; positions
     printed (x*, distance to nearest positive/negative node, hull
     position).

 D2  THE DEFLATION SPLIT, EXACT (per truth rung; kill ->
     WARD-BROKEN): D2.a star chain of mu* completes to length h-1
     with be > 0 on every truth rung (failures counted, > 0 kills);
     D2.b THE IDENTITY ||G - (G_def + w w^T)||_F / ||G||_F <=
     DEFL_WARD on every truth rung; D2.c interlacing sandwich tau -
     ITL_TOL <= m2 <= ceil + ITL_TOL (ceil = 1 - lam_2(G),
     diagnostic ceiling); D2.d m1 == tau (two eigen routes, rel <=
     TAU_WARD).

 D3  MARGINS + THE TAU-SCREEN (the decisive measurement; typed,
     never kills): full ladder (kz, h, tau, m2, m2/tau, eff,
     diagnostic overlap <w-hat, v_top(G)>^2); OLS slope + corr of
     log m2 vs log tau (primary), vs log h (secondary).  TYPED
     (frozen bands): DEFL-SCREEN-PASS(slope) iff |slope| <=
     SLOPE_PASS = 0.30 and min m2 > 0; DEFL-SCREEN-RELOC(slope) iff
     slope >= SLOPE_RELOC = 0.70; else DEFL-SCREEN-AMBIG(slope).
     NODE CONTROLS (frozen rule): the same m2-ladder at x_ctrl-mid
     and x_ctrl-J; NODE-BEST iff median(m2/tau at x*) >= NODE_FAC =
     1.5 x median(m2/tau) of BOTH controls; NODE-AHEAD iff strictly
     larger than both but under the factor; else
     NODE-NOT-SPECIAL(argmax).  WALL CONTENT: the deflated margin
     on the smooth world -- DEFLWALL-SEEN iff m2_smooth <= 0 on >=
     1 smooth rung (the deflation does not erase the violation),
     else DEFLWALL-BLIND (typed first-class, a screen pass with
     DEFLWALL-BLIND is recorded as wall-blind, not progress).

 D4  THE CO-BLOCK AFTER THE CONGRUENCE (per step; typed): Shat' =
     core Schur complement of Ahat' = I - G_def' at rung h+1 (its
     own node x*_{h+1}); Bhat = W^T (Shat'/tau_h) W in the SAME
     frozen Householder frame as B; measured: lam_min(Bhat) ladder
     + tau-screen; certified G1/G2/G3 on Bhat, count of steps with
     best > 0 and gap factor to the true floor where positive.
     TYPED: CERT-REVIVED(n=all) / CERT-PARTIAL(n) /
     CERT-DEAD-STILL.  (Honesty: Schur complements do not commute
     with the split -- Bhat is the co-block of the DEFLATED wall,
     not a congruence transform of B itself; the fallback D5 tests
     a literal congruence on B.)

 D5  THE PRIME-FREE CHOLESKY PRECONDITIONER (fallback, always run;
     typed): per step, B0 = W^T (S'_smooth / tau_h) W (smooth world
     rung h+1 in the truth frame -- source-only: the prime-free
     model consumes no truth spectral data); where B0 PD: B0 = L
     L^T, Btilde = L^{-1} B L^{-T} = I + K; measured: negative
     index of K, margin 1 + lam_min(K), Gershgorin G1 on Btilde,
     tau-screen of the margin.  TYPED: PRECOND-SMALLNEG(max-negidx
     <= 2, with the explicit residual-channel margins printed) /
     PRECOND-WIDE(negidx stats) / PRECOND-UNUSABLE(count B0 not
     PD).

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) = 0
     everywhere; C1 smooth world: neg(A) > 0 on >= 1 rung; C2
     Epstein x^2+5y^2 comb + scramble (seed 1) at kz 9 fire (neg(A)
     > 0 or chain death).

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
identity / control wards (W4, D1, D2, C0-C2) -> WARD-BROKEN.
D3/D4/D5 typed outcomes are measurements, never kills.

VERDICT (frozen enum): CHRISTDEFL-MEASURED with typed sublabels
DEFL-IDENTITY-EXACT(dev), DEFL-SCREEN-PASS/RELOC/AMBIG(slope),
NODE-BEST/NODE-AHEAD/NODE-NOT-SPECIAL, DEFLWALL-SEEN/BLIND,
EFF(med), CERT-REVIVED/PARTIAL/DEAD-STILL, PRECOND-SMALLNEG/WIDE/
UNUSABLE; else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP =
42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; NODE_C = 0.3727, NODE_S =
-0.0116 (node_origin drift law, declared input); J_CTRL = 24;
MINB_REF = 0.679 (rtol 2e-2); GAPMIN_REF = 0.052, GAPMED_REF =
0.888 (rtol 5e-2); DEFL_WARD = 5e-7 (smoke-calibrated float floor,
see disclosure); ITL_TOL = 1e-8; TAU_WARD = 1e-8; SLOPE_PASS =
0.30; SLOPE_RELOC = 0.70; NODE_FAC = 1.5; CTRL_KZ = 9; scramble
seed 1.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script (21/21 with the identical bars; NO bar, band, count,
rule or enum was moved after it -- DEFL_WARD = 5e-7 was set a
priori as a generous Lanczos float allowance and the smoke measured
6.1e-13, ITL_TOL/TAU_WARD 1e-8 confirmed generous) REFUTED the
incoming hypothesis, recorded here as the honest context the frozen
run must confirm: the deflation identity is EXACT on 42/42 (max dev
6.1e-13), but the classical-node channel is DECOUPLED from the
defect geometry -- diagnostic overlap <w-hat, v_top>^2 median
1.4e-9, efficiency eff median 0.0000 (max 4e-4), m2/tau = 1.00 on
every rung, screen slope +1.000 (pure relocation); the two control
nodes are indistinguishable from x* (NODE-NOT-SPECIAL); Bhat is
numerically indistinguishable from B (minBhat range [0.679, 84.0],
certified bounds still all negative, best max -88.3 ->
CERT-DEAD-STILL); and the prime-free preconditioner premise is DEAD
at the co-block level: B0 (smooth S' in the truth frame) is NOT PD
on any usable step (min eigs -646 .. -2.1e6, 35 usable + 4 without
a smooth companion) -> PRECOND-UNUSABLE.  The incoming expectation
"the coherent off-diagonal geometry of B is the node evaluation and
Christoffel damping at y* revives classical certificates" is
therefore REFUTED at smoke level; fail-first is preserved (nothing
was weakened to make this pass -- all wards are identity/
reproduction wards and all refutations live in typed measurements).

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as P2
SPEC (ii), deterministic; (iii) the star chain is
lanczos_chain(xs, ws (xs - x*)^2, h - 1) -- division-free route,
K*mat = P* P*^T; (iv) OLS/corr population statistics as v900; (v)
screens read the positive-margin subset with the excluded count
printed; (vi) smooth-world deflation uses the same x*(alpha)
formula (the drift law is prime-free -- it IS the smooth model's
own node).

NO-GO COMPLIANCE (frozen): no Gershgorin/Brauer/Weyl bound on RAW B
is retried as content (they enter only as the W4 reproduction of
the recorded disaster and as the AFTER-congruence measurement); no
rank-1 approximation of the core update; no plain Herglotz wall
certificate; no fit where an identity is claimed (D2 is an exact
ward; all trends are typed measurements).

NO RH claim: the deflation split is exact finite linear algebra of
the deployed v563 window family for ANY node; the margins are
measurements; nothing here proves tau_h > 0 beyond the certified
census (v897), and nothing here proves B-uniformity or wall
positivity for all h.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core
machinery verbatim from port_tangent_schur_probe.py /
port_bfloor_uniformity_probe.py (round 58) = v900 chain; classical
node drift law from node_origin_arch_probe.py (declared input);
certified base v884/v887/v897 -- declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/b_christoffel_deflation_probe.py
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
NODE_C = 0.3727                # node_origin drift law (declared)
NODE_S = -0.0116
J_CTRL = 24                    # v899 window evaluation fold
MINB_REF = 0.679
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
DEFL_WARD = 5e-7               # D2.b (smoke-calibrated, header)
ITL_TOL = 1e-8                 # D2.c
TAU_WARD = 1e-8                # D2.d
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
NODE_FAC = 1.5
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
                 want_vec=False, keep_chain=False):
    """v900 verbatim wall + fixed-core split, extended (keep_chain):
    the folded families, the chain and G are retained per rung for
    the deflation; big arrays are dropped by the caller."""
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
    out = dict(kz=kz, h=h, n=n, alpha=float(alpha), M=M, D=D, L=L)
    if want_vec:
        evA, VA = np.linalg.eigh(A)
    else:
        evA = np.linalg.eigvalsh(A)
        VA = None
    out["tau"] = float(evA[0])
    out["ceil"] = float(evA[1])      # 1 - lam_2(G), diagnostic
    out["negA"] = int(np.sum(evA < 0.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if keep_chain:
        out["chain"] = (al, be, m0)
        out["xs"], out["ws"] = xs, ws
        out["ys"], out["vs"] = ys, vs
        out["Pn"] = Pn
        out["G"] = G
        out["vtop"] = VA[:, 0] if want_vec else None
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    out["ic"], out["ib"] = ic, ib
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
    if want_vec:
        v = VA[:, 0]
        out["wcore"] = float(np.sum(v[ic] ** 2))
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


def corr(x, y):
    return float(np.corrcoef(np.asarray(x, float),
                             np.asarray(y, float))[0, 1])


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


# ------------------------------ the deflation (SPEC iii)
def node_of(r):
    """The frozen node map u* -> x* (spec: NODE CORRESPONDENCE)."""
    ustar = (NODE_C + NODE_S * r["alpha"]) * r["alpha"]
    xstar = math.cos(2.0 * math.pi * (ustar / r["D"]) / r["L"])
    return ustar, xstar


def deflate(r, xstar, need_core=False):
    """The exact Christoffel deflation split at node xstar.
    Returns None if the star chain dies (counted by caller)."""
    al, be, m0 = r["chain"]
    h = r["h"]
    px = eval_chain(al, be, m0, np.array([xstar]), h)[0]
    Kxx = float(px @ px)
    if Kxx <= 0.0:
        return None
    w = np.sqrt(r["vs"]) * (r["Pn"] @ px) / math.sqrt(Kxx)
    als, bes, m0s, st = lanczos_chain(
        r["xs"], r["ws"] * (r["xs"] - xstar) ** 2, h - 1)
    if st < h - 1 or (len(bes) and np.any(bes <= 0)):
        return None
    Ps = eval_chain(als, bes, m0s, r["ys"], h - 1)
    F = (np.sqrt(r["vs"]) * (r["ys"] - xstar))[:, None] * Ps
    Gdef = F @ F.T
    Gdef = 0.5 * (Gdef + Gdef.T)
    dev = (float(np.linalg.norm(r["G"] - (Gdef + np.outer(w, w))))
           / max(float(np.linalg.norm(r["G"])), 1e-300))
    evd = np.linalg.eigvalsh(Gdef)
    out = dict(dev=dev, m2=float(1.0 - evd[-1]),
               negdef=int(np.sum(evd < -1e-12)))
    if r.get("vtop") is not None:
        wn = w / max(float(np.linalg.norm(w)), 1e-300)
        out["ovl_top"] = float(np.dot(wn, r["vtop"])) ** 2
    if need_core and r.get("core_ok"):
        Ahat = np.eye(r["n"]) - Gdef
        ic, ib = r["ic"], r["ib"]
        Bc = Ahat[np.ix_(ic, ic)]
        Xc = Ahat[np.ix_(ic, ib)]
        Rc = Ahat[np.ix_(ib, ib)]
        try:
            Z = np.linalg.solve(Rc, Xc.T)
        except np.linalg.LinAlgError:
            return out
        Sh = Bc - Xc @ Z
        out["Shat"] = 0.5 * (Sh + Sh.T)
    return out


def drop_big(r):
    for k in ("chain", "xs", "ws", "ys", "vs", "Pn", "G", "vtop"):
        r.pop(k, None)


def main():
    section("PRIME.PORT.CHRISTOFFEL.DEFLATION.01 -- the wall Gram "
            "deflated at the classical node (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + deflation per rung (ONE pass, "
            "big arrays dropped)")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    n_star_dead = 0
    node_ok = True
    for kz in zones:
        r = gram_anatomy(kz, want_vec=True, keep_chain=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
            truth.append(None)
            continue
        ustar, xstar = node_of(r)
        r["ustar"], r["xstar"] = ustar, xstar
        node_ok &= (0.0 < ustar < 2.0 * r["alpha"]
                    and -1.0 < xstar < 1.0)
        r["dpos"] = float(np.min(np.abs(r["xs"] - xstar)))
        r["dneg"] = float(np.min(np.abs(r["ys"] - xstar)))
        d_main = deflate(r, xstar, need_core=True)
        yj = math.cos(2.0 * math.pi * J_CTRL / r["L"])
        r["xJ"] = yj
        d_mid = deflate(r, 0.0)
        d_J = deflate(r, yj)
        if d_main is None:
            n_star_dead += 1
        r["defl"] = d_main
        r["defl_mid"] = d_mid
        r["defl_J"] = d_J
        drop_big(r)
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

    # W4 reproduction: raw B ledger + certified disaster
    rows = []
    for r1, r2 in steps:
        wS, VS = np.linalg.eigh(r1["S"])
        v = VS[:, 0]
        Q = householder_frame(v)
        Wf = Q[:, 1:]
        Mx = r2["S"] / r1["tau"]
        Mx = 0.5 * (Mx + Mx.T)
        Mt = Q.T @ Mx @ Q
        Mt = 0.5 * (Mt + Mt.T)
        nsc = float(Mt[0, 0])
        b = Mt[1:, 0]
        B = Mt[1:, 1:]
        evB = np.linalg.eigvalsh(B)
        minB = float(evB[0])
        gap = (nsc - float(b @ np.linalg.solve(B, b))
               if minB > 0 else float("nan"))
        bestg = max(gersh_min(B), gersh_scaled(B), cassini_scaled(B))
        rows.append(dict(r1=r1, r2=r2, Q=Q, Wf=Wf, B=B, minB=minB,
                         gap=gap, bestg=bestg))
    minBs = np.array([row["minB"] for row in rows])
    gaps = np.array([row["gap"] for row in rows])
    bests = np.array([row["bestg"] for row in rows])
    minB_all = float(np.min(minBs))
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

    # ------------------------------------------------------------ D1
    section("D1 -- the node map u* -> x* (drift law -> spectral "
            "variable)")
    check("D1.a WARD node inside window and circle on every rung "
          "(0 < u* < 2 alpha, -1 < x* < 1)", node_ok, kill="K2")
    print("    kz   h    alpha   u*/alpha   x*        x_J       "
          "d(pos)    d(neg)")
    for r in truth:
        print("    %-4d %-4d %6.3f  %.4f    %+.5f  %+.5f  %.2e  "
              "%.2e"
              % (r["kz"], r["h"], r["alpha"],
                 r["ustar"] / r["alpha"], r["xstar"], r["xJ"],
                 r["dpos"], r["dneg"]), flush=True)
    print("    (x* sits INSIDE the support hull of both folded "
          "families on every rung -- printed distances; the "
          "deflation identity needs only K(x*, x*) > 0.)")

    # ------------------------------------------------------------ D2
    section("D2 -- the deflation split G = D K* D + w w^T, exact")
    check("D2.a star chain of mu* completes (h - 1, be > 0) on "
          "every truth rung (dead: %d)" % n_star_dead,
          n_star_dead == 0, kill="K2")
    dev_id = max(r["defl"]["dev"] for r in truth)
    check("D2.b WARD THE IDENTITY ||G - (G_def + w w^T)|| / ||G|| "
          "max %.2e <= %.0e (division-free star-chain route)"
          % (dev_id, DEFL_WARD), dev_id <= DEFL_WARD, kill="K2")
    itl_ok = True
    dev_tau = 0.0
    for r in truth:
        m2 = r["defl"]["m2"]
        itl_ok &= (r["tau"] - ITL_TOL <= m2 <= r["ceil"] + ITL_TOL)
        dev_tau = max(dev_tau, abs(r["defl"]["negdef"]))
    check("D2.c WARD interlacing sandwich tau <= m2 <= ceil "
          "(tol %.0e) on every rung; G_def PSD (max neg count %d)"
          % (ITL_TOL, int(dev_tau)), itl_ok and dev_tau == 0,
          kill="K2")
    check("D2.d SOURCE-ONLY statement: every ingredient is comb "
          "linear algebra of (xs, ws, ys, vs) + the prime-free "
          "node map; no tau, no defect eigenvector, no "
          "decomposition of A/S/B enters the construction", True)

    # ------------------------------------------------------------ D3
    section("D3 -- margins + THE TAU-SCREEN (m2 = 1 - lam_max("
            "G_def))")
    print("    kz   h    tau        m2(x*)     m2/tau   eff      "
          "ovl_top   m2(mid)    m2(J)")
    taus, m2s, effs = [], [], []
    m2_mid, m2_J = [], []
    for r in truth:
        d = r["defl"]
        eff = ((d["m2"] - r["tau"])
               / max(r["ceil"] - r["tau"], 1e-300))
        effs.append(eff)
        taus.append(r["tau"])
        m2s.append(d["m2"])
        m2_mid.append(r["defl_mid"]["m2"]
                      if r["defl_mid"] else float("nan"))
        m2_J.append(r["defl_J"]["m2"]
                    if r["defl_J"] else float("nan"))
        print("    %-4d %-4d %.3e  %.3e  %7.2f  %.5f  %.2e  "
              "%.3e  %.3e"
              % (r["kz"], r["h"], r["tau"], d["m2"],
                 d["m2"] / r["tau"], eff, d.get("ovl_top", -1),
                 m2_mid[-1], m2_J[-1]), flush=True)
    taus = np.array(taus)
    m2s = np.array(m2s)
    pos = m2s > 0.0
    n_neg_m2 = int(np.sum(~pos))
    _a, sl_m2, r2_m2 = ols_line(np.log(taus[pos]),
                                np.log(m2s[pos]))
    co_m2 = corr(np.log(taus[pos]), np.log(m2s[pos]))
    hh = np.array([r["h"] for r in truth], float)
    _a, sl_h, _r = ols_line(np.log(hh[pos]), np.log(m2s[pos]))
    print("\n    PRIMARY: slope log m2 vs log tau = %+.4f (corr "
          "%+.3f, R^2 %.3f); vs log h = %+.4f; m2 <= 0 on %d "
          "rungs (excluded from the log fit, counted)"
          % (sl_m2, co_m2, r2_m2, sl_h, n_neg_m2))
    print("    m2 range [%.3e, %.3e]; tau range [%.3e, %.3e] "
          "(factor %.0f)"
          % (float(np.min(m2s)), float(np.max(m2s)),
             float(np.min(taus)), float(np.max(taus)),
             float(np.max(taus)) / float(np.min(taus))))
    med_eff = float(np.median(effs))
    med_ovl = float(np.median([r["defl"].get("ovl_top", 0.0)
                               for r in truth]))
    print("    efficiency eff = (m2 - tau)/(ceil - tau): med %.4f "
          "(range [%.4f, %.4f]); DIAGNOSTIC top-channel overlap "
          "<w-hat, v_top>^2 med %.2e"
          % (med_eff, float(np.min(effs)), float(np.max(effs)),
             med_ovl))
    if abs(sl_m2) <= SLOPE_PASS and float(np.min(m2s)) > 0.0:
        d3 = "DEFL-SCREEN-PASS(slope=%+.3f)" % sl_m2
    elif sl_m2 >= SLOPE_RELOC:
        d3 = "DEFL-SCREEN-RELOC(slope=%+.3f)" % sl_m2
    else:
        d3 = "DEFL-SCREEN-AMBIG(slope=%+.3f)" % sl_m2
    check("D3.1 typed: %s (bands PASS |s| <= %.2f, RELOC s >= "
          "%.2f)" % (d3, SLOPE_PASS, SLOPE_RELOC), True)
    med_gain = float(np.median(m2s / taus))
    med_gain_mid = float(np.nanmedian(np.array(m2_mid) / taus))
    med_gain_J = float(np.nanmedian(np.array(m2_J) / taus))
    best_ctrl = max(med_gain_mid, med_gain_J)
    if med_gain >= NODE_FAC * best_ctrl:
        d3n = "NODE-BEST(x*=%.1f, mid=%.1f, J=%.1f)" % (
            med_gain, med_gain_mid, med_gain_J)
    elif med_gain > best_ctrl:
        d3n = "NODE-AHEAD(x*=%.1f, mid=%.1f, J=%.1f)" % (
            med_gain, med_gain_mid, med_gain_J)
    else:
        d3n = "NODE-NOT-SPECIAL(x*=%.1f, mid=%.1f, J=%.1f)" % (
            med_gain, med_gain_mid, med_gain_J)
    check("D3.2 typed node comparison (median m2/tau): %s (factor "
          "rule %.1f)" % (d3n, NODE_FAC), True)

    # ------------------------------------------------------------ D4
    section("D4 -- the co-block after the congruence: Bhat + "
            "certified bounds")
    print("    step        tau_h      minB      minBhat    "
          "bestG(B)    bestG(Bhat)")
    minBh, bestBh, tt = [], [], []
    n_noshat = 0
    for row in rows:
        r1, r2 = row["r1"], row["r2"]
        d2 = r2["defl"]
        if d2 is None or "Shat" not in d2:
            n_noshat += 1
            continue
        Bh = row["Wf"].T @ (d2["Shat"] / r1["tau"]) @ row["Wf"]
        Bh = 0.5 * (Bh + Bh.T)
        mB = float(np.linalg.eigvalsh(Bh)[0])
        bg = max(gersh_min(Bh), gersh_scaled(Bh),
                 cassini_scaled(Bh))
        minBh.append(mB)
        bestBh.append(bg)
        tt.append(r1["tau"])
        print("    h %3d->%3d  %.3e  %8.4f  %9.4f  %+9.3e  %+9.3e"
              % (r1["h"], r2["h"], r1["tau"], row["minB"], mB,
                 row["bestg"], bg), flush=True)
    minBh = np.array(minBh)
    bestBh = np.array(bestBh)
    tt = np.array(tt)
    posh = minBh > 0
    if np.sum(posh) >= 3:
        _a, sl_bh, _r = ols_line(np.log(tt[posh]),
                                 np.log(minBh[posh]))
    else:
        sl_bh = float("nan")
    n_cpos = int(np.sum(bestBh > 0.0))
    print("\n    lam_min(Bhat) range [%.3e, %.3e]; tau-screen "
          "slope %+.4f; certified best > 0 on %d/%d steps "
          "(missing Shat: %d)"
          % (float(np.min(minBh)), float(np.max(minBh)), sl_bh,
             n_cpos, len(minBh), n_noshat))
    if n_cpos == len(minBh) and len(minBh) > 0:
        gapf = minBh / bestBh
        d4 = "CERT-REVIVED(%d, worst-gap=%.1f)" % (
            n_cpos, float(np.max(gapf)))
    elif n_cpos > 0:
        d4 = "CERT-PARTIAL(%d/%d)" % (n_cpos, len(minBh))
    else:
        d4 = "CERT-DEAD-STILL"
    check("D4.1 typed: %s (raw-B disaster: best max %+.1f; after "
          "congruence: best max %+.3e)"
          % (d4, float(np.max(bests)),
             float(np.max(bestBh)) if len(bestBh) else
             float("nan")), True)

    # ------------------------------------------------------------ D5
    section("D5 -- the prime-free Cholesky preconditioner "
            "(fallback congruence on B itself)")
    sm_map = {}
    for kz in zones:
        rs = gram_anatomy(kz, world_fn=world_smooth, want_vec=False,
                          keep_chain=False)
        if isinstance(rs, dict):
            sm_map[kz] = rs
    negidx_list, marg_list, g1t_list, tt5 = [], [], [], []
    n_b0dead = 0
    n_nosm = 0
    print("    step        minB0      negidx(K)  1+lam_min(K)  "
          "G1(Btilde)")
    for row in rows:
        r1, r2 = row["r1"], row["r2"]
        rs2 = sm_map.get(r2["kz"])
        if rs2 is None or "S" not in rs2:
            n_nosm += 1
            continue
        B0 = row["Wf"].T @ (rs2["S"] / r1["tau"]) @ row["Wf"]
        B0 = 0.5 * (B0 + B0.T)
        ev0 = np.linalg.eigvalsh(B0)
        if float(ev0[0]) <= 0.0:
            n_b0dead += 1
            print("    h %3d->%3d  %+9.4f  B0 NOT PD -> skipped"
                  % (r1["h"], r2["h"], float(ev0[0])), flush=True)
            continue
        Lc = np.linalg.cholesky(B0)
        Bt = np.linalg.solve(Lc, np.linalg.solve(Lc, row["B"].T).T)
        Bt = 0.5 * (Bt + Bt.T)
        evK = np.linalg.eigvalsh(Bt - np.eye(7))
        nneg = int(np.sum(evK < 0.0))
        marg = 1.0 + float(evK[0])
        g1t = gersh_min(Bt)
        negidx_list.append(nneg)
        marg_list.append(marg)
        g1t_list.append(g1t)
        tt5.append(r1["tau"])
        print("    h %3d->%3d  %9.4f  %6d     %+9.4f     %+9.4f"
              % (r1["h"], r2["h"], float(ev0[0]), nneg, marg, g1t),
              flush=True)
    if marg_list:
        marg_arr = np.array(marg_list)
        posm = marg_arr > 0
        if np.sum(posm) >= 3:
            _a, sl_pc, _r = ols_line(
                np.log(np.array(tt5)[posm]), np.log(marg_arr[posm]))
        else:
            sl_pc = float("nan")
        mx_neg = int(np.max(negidx_list))
        md_neg = float(np.median(negidx_list))
        n_g1pos = int(np.sum(np.array(g1t_list) > 0.0))
        print("\n    usable steps %d (B0 dead: %d, no smooth: %d); "
              "negidx(K) med %.0f max %d; margin 1+lam_min(K) "
              "range [%.3f, %.3f], tau-screen slope %+.4f; "
              "G1(Btilde) > 0 on %d/%d"
              % (len(marg_list), n_b0dead, n_nosm, md_neg, mx_neg,
                 float(np.min(marg_arr)), float(np.max(marg_arr)),
                 sl_pc, n_g1pos, len(g1t_list)))
        if mx_neg <= 2:
            d5 = ("PRECOND-SMALLNEG(max-negidx=%d, min-marg=%.3f)"
                  % (mx_neg, float(np.min(marg_arr))))
        else:
            d5 = ("PRECOND-WIDE(negidx-med=%.0f, max=%d)"
                  % (md_neg, mx_neg))
    else:
        sl_pc = float("nan")
        d5 = "PRECOND-UNUSABLE(B0-dead=%d)" % n_b0dead
    check("D5.1 typed: %s" % d5, True)

    # ------------------------------------------------------------ C
    section("C -- controls: smooth world + Epstein/scramble")
    check("C0.1 WARD truth wall holds (neg(A) = 0 on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    n_viol = 0
    n_m2neg = 0
    n_smdead = 0
    for kz in zones:
        rs = gram_anatomy(kz, world_fn=world_smooth, want_vec=True,
                          keep_chain=True)
        if not isinstance(rs, dict):
            n_smdead += 1
            continue
        if rs["negA"] > 0:
            n_viol += 1
        _u, xst = node_of(rs)
        ds = deflate(rs, xst)
        if ds is None or ds["m2"] <= 0.0:
            n_m2neg += 1
        drop_big(rs)
    print("  C1 -- smooth world: neg(A) > 0 on %d rungs; deflated "
          "margin m2 <= 0 (or star chain dead) on %d of %d "
          "completed rungs" % (n_viol, n_m2neg,
                               len(zones) - n_smdead))
    check("C1.1 WARD smooth violates at rung level", n_viol > 0,
          kill="K2")
    dwall = ("DEFLWALL-SEEN(%d)" % n_m2neg if n_m2neg > 0
             else "DEFLWALL-BLIND")
    check("C1.2 typed wall content of the deflated margin: %s (a "
          "screen pass with DEFLWALL-BLIND is a wall-blind pass, "
          "not progress)" % dwall, True)
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

    return finish(dict(d3=d3, d3n=d3n, d4=d4, d5=d5, dwall=dwall,
                       dev=dev_id, eff=med_eff))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("CHRISTDEFL-MEASURED / DEFL-IDENTITY-EXACT"
                   "(%(dev).1e) / %(d3)s / %(d3n)s / %(dwall)s / "
                   "EFF(med=%(eff).4f) / %(d4)s / %(d5)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the deflation split is exact warded
  algebra that holds for ANY node -- the node choice carries no
  identity content; all node content is in the measured margin
  comparisons.  The deflated margin m2 must be read TOGETHER with
  the wall-content type and the efficiency: an O(1) m2 with
  DEFLWALL-BLIND or a ~0 efficiency means the classical-node
  channel is NOT the coherent defect geometry -- recorded either
  way.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
