#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wall_gram_radau_probe -- PRIME.PORT.GRAM.COMPLETION.01 +
PRIME.PORT.RADAU.WEIGHT.01
(EXPLORATION ONLY, experiments/; round 59, theorem-engineering on the
RH-side wall: (a) does the wall matrix admit a source-only Gram
representation with a NONNEGATIVE weight -- the truncated-moment
completion question; (b) is the wall pivot a Gauss--Radau weight at
the prescribed classical node?  2026-08-10.)

PART (a) -- THE GRAM COMPLETION (derived a priori, classical).  The
deployed wall Gram G_ij = sqrt(v_i v_j) K_h(y_i, y_j) (A = I - G,
tau = 1 - lam_max(G)) has the same nonzero spectrum as H = Phi^T Phi
with Phi_ik = sqrt(v_i) p_k(y_i), and
    M0 := I_h - H  =  moment matrix of the SIGNED total comb measure
          nu = mu_+ - mu_-  in the mu_+-orthonormal chain basis:
    (M0)_kl = sum_f w_f^signed p_k(x_f) p_l(x_f)     [EXACT, warded
    two-route: pipeline algebra vs direct signed quadrature], and
    lam_min(M0) = tau  EXACTLY (spectrum tie, warded).
So the wall statement "A >= 0" IS the statement "the signed comb
measure nu is nonnegative on all SQUARES of degree <= 2h - 2".  THE
COMPLETION QUESTION: does nu admit a source-only Gram representation
M0 = F^T W F with W >= 0 -- equivalently (truncated K-moment problem
on [-1, 1], Lukacs): is nu nonnegative on the FULL cone of
polynomials >= 0 on [-1, 1] of degree <= 2h - 2?  By Lukacs every
such polynomial is sigma_0 + (1 - x^2) sigma_1 (even degree) or
(1 - x) sigma_1 + (1 + x) sigma_2 (odd), sigma_i sums of squares, so
the certificate is the PSD-ness of the LOCALIZED moment matrices
    M1x2 = int (1 - x^2) p_k p_l dnu,   Mm = int (1 - x) p_k p_l dnu,
    Mp   = int (1 + x) p_k p_l dnu      (sizes h - 1),
computed by DIRECT signed quadrature (division-free, source-only).
HONESTY (frozen): M0 >= 0 is the wall itself (reproduced, not new);
the localized floors are NOT implied by the wall ((1 - x^2) P^2 is
nonnegative on [-1, 1] but not a square at matched degree) -- their
signs and tau-screens are the NEW measured content.  A certified
completion means: at degree 2h - 2 the signed comb measure is
indistinguishable from a genuinely NONNEGATIVE measure on [-1, 1]
(Gram representation with W >= 0 exists); a failed floor kills that
reformulation at that rung -- typed either way, never a kill.

PART (b) -- THE RADAU WEIGHT (derived a priori, classical: Golub
1973).  For the positive folded source family mu_+ with Jacobi chain
(al, be, m0) and the prescribed classical node t = x*_h (the
prime-free drift law + window geometry, verbatim from
b_christoffel_deflation_probe), the Gauss--Radau matrix is
    J^R_{h+1} = tridiag(al_0..al_{h-1}, ALHAT; be_0..be_{h-1}),
    ALHAT = t + be_{h-1}^2 [(J_h - t I)^{-1}]_{h-1,h-1},
verified TWO-ROUTE: tridiagonal solve vs the DETERMINANT QUOTIENT
via the continued fraction r_k = (al_{k-1} - t) - be_{k-2}^2 /
r_{k-1} (r_k = det(J_k - t)/det(J_{k-1} - t); the resolvent entry is
1/r_h) -- the classical determinant-quotient/Jacobi-recurrence route
demanded by the spec.  The rule (theta_i, w_i = m0 q_{0i}^2) from
the spectral decomposition of J^R prescribes t as a node (warded).
EXACTNESS (honest formulation, amended at smoke -- see disclosure):
exactness in the orthonormal chain basis is the spectral TAUTOLOGY
sum_i w_i p_k(theta_i) p_l(theta_i) = (V V^T)_kl = delta_kl (the
shared recurrence gives sqrt(w_i) p_k(theta_i) = V_ki exactly), so
it certifies nothing; the WARDED exactness is the non-tautological
raw-moment reproduction against the SOURCE family, sum_i w_i
theta_i^j == sum_f ws_f xs_f^j for j <= J_MOM = 24 (exact for j <=
2h - 1 in exact arithmetic; numerically stable -- an exterior Radau
node has underflowing weight).  NONNEGATIVE weights and Cauchy
interlacing against the Gauss nodes of J_h hold AUTOMATICALLY
(symmetric tridiagonal with be > 0; warded as numerical sanity and
DECLARED automatic -- the honest reading is that the classical
positivity criteria cannot fail in this construction); what CAN be
informative is measured: the modified diagonal ALHAT (wild iff t
resonates with spec(J_h) -- distance printed), the prescribed-node
weight w* = w(t), its ratio to the Christoffel function lam_h(t) =
1/K_h(t, t) (classically w*/lam_h <= 1), and the tau-screen of w*.

THE PIVOT COMPARISON (frozen).  Is the wall pivot a Radau weight?
The recorded pivot ladder is the P2 step gap (gap min/med
0.052/0.888, reproduced in W4); the candidate is w*(x*) at the
step's target rung r2.  TYPED: RADAU-PIVOT-IDENTITY iff max rel dev
<= RATIO_ID = 1e-6; RADAU-PIVOT-TRACK iff corr(log gap, log w*) >=
TRACK_CORR = 0.90 and the log-log slope is in [0.7, 1.3];
else RADAU-PIVOT-UNRELATED(corr, slope).

ANTI-CIRCULARITY (frozen): every construction ingredient is comb
linear algebra of (xs, ws, ys, vs) + the chain (al, be, m0) + the
prime-free node map.  NO tau, NO defect eigenvector, NO
decomposition of A/S/B enters any construction; tau and the P2 gap
enter ONLY as measured comparanda in screens and G3.

FROZEN PROTOCOL (pipeline verbatim from b_christoffel_deflation_
probe / schur_ward_identity_probe = v900 chain; ONE Gram per rung;
window memoization; per-rung big arrays dropped):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2 >=
     30 full-core rungs; W3a truth all-PSD (A, R, S); W3b >= 20
     consecutive full-core steps; W4 REPRODUCTION P2/P3 ledger: min
     lam_min(B) == 0.679 (rtol 2e-2), gap min/med == 0.052/0.888
     (rtol 5e-2), raw-B certified disaster (best classical bound <
     0 on every step).

 G1  THE GRAM COMPLETION (part a): G1.a WARD two-route M0 (pipeline
     I - H vs direct signed quadrature) rel Frobenius dev <=
     M0_WARD on every rung (kill -> WARD-BROKEN); G1.b WARD
     lam_min(M0) == tau rel <= TAU2_WARD (spectrum tie; kill);
     G1.c the localized floors lam_min(M1x2), lam_min(Mm),
     lam_min(Mp) per rung (full ledger printed): TYPED
     GRAM-COMPLETION-CERTIFIED(min floor) iff ALL three floors >=
     -LOC_TOL on ALL truth rungs, else GRAM-COMPLETION-FAILS(counts
     per matrix); G1.d tau-screen of |lam_min(M1x2)| (MAGNITUDE,
     amended at smoke -- the sign lives in G1.c; sign counts
     printed): TYPED LOC-SCREEN-PASS iff |slope| <= SLOPE_PASS =
     0.30, RELOC iff slope >= SLOPE_RELOC = 0.70, else AMBIG (on a
     negative floor, RELOC means the VIOLATION collapses with tau,
     PASS means it is O(1)-persistent).

 G2  THE RADAU WEIGHT (part b): G2.a WARD ALHAT two-route
     (tridiagonal solve vs determinant-quotient continued fraction)
     rel <= DQ_WARD on every usable rung (kill); G2.b WARD the
     prescribed node is hit: min_i |theta_i - x*| <= NODE_HIT
     (kill); G2.c WARD raw-moment exactness vs the source family:
     max_j |sum_i w_i theta_i^j - sum_f ws_f xs_f^j| / m0 <=
     RAD_WARD for j <= J_MOM (kill); G2.d WARD classical
     consistency (automatic, sanity):
     all w_i >= 0 and Cauchy interlacing Gauss/Radau with tol
     ITL_TOL (kill); G2.e usable-rung census: rungs with dist(x*,
     spec(J_h)) < RES_TOL are DEGENERATE and skipped (counted; WARD
     >= MIN_RADAU = 30 usable rungs; kill -> PIPELINE-BROKEN);
     G2.f measured + typed: w* ladder, w*/lam_h(x*), ALHAT, dist;
     tau-screen of w*: RADAUW-SCREEN-PASS/RELOC/AMBIG (same bands).

 G3  THE PIVOT COMPARISON (typed, never kills): per step, P2 gap_k
     vs w*(r2_k): full ledger, max rel dev, corr + slope of logs;
     typed as frozen above.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) = 0
     everywhere; C1 smooth world neg(A) > 0 on >= 1 rung; C1.2
     typed LOCWALL: the localized floor lam_min(M1x2) on every
     smooth rung -- LOCWALL-SEEN(count < 0)/LOCWALL-BLIND (typed
     first-class; a completion certificate that also certifies the
     smooth world is wall-blind at the localized level); C2 Epstein
     x^2+5y^2 comb + scramble (seed 1) at kz 9 fire (neg(A) > 0 or
     chain death).

KILLS: K1 pipeline (W1-W3, G2.e) -> PIPELINE-BROKEN; K2
reproduction / identity / control wards (W4, G1.a, G1.b, G2.a-d,
C0-C2) -> WARD-BROKEN.  G1.c/G1.d/G2.f/G3/C1.2 typed outcomes are
measurements, never kills.

VERDICT (frozen enum): GRAMRADAU-MEASURED with typed sublabels
M0-IDENTITY-EXACT(dev), GRAM-COMPLETION-CERTIFIED(minfloor)/
GRAM-COMPLETION-FAILS(nx2/nm/np), LOC-SCREEN-PASS/RELOC/AMBIG
(slope), RADAU-EXACT(dev), RADAUW-SCREEN-PASS/RELOC/AMBIG(slope),
RADAU-PIVOT-IDENTITY/TRACK/UNRELATED, LOCWALL-SEEN/BLIND; else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP =
42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MIN_RADAU = 30; NODE_C =
0.3727, NODE_S = -0.0116 (node_origin drift law, declared input);
MINB_REF = 0.679 (rtol 2e-2); GAPMIN_REF = 0.052, GAPMED_REF =
0.888 (rtol 5e-2); M0_WARD = 1e-8; TAU2_WARD = 1e-8; LOC_TOL =
1e-10; DQ_WARD = 1e-6; NODE_HIT = 1e-9; RAD_WARD = 1e-8; J_MOM =
24; ITL_TOL = 1e-10; RES_TOL = 1e-10; RATIO_ID = 1e-6; TRACK_CORR
= 0.90;
TRACK_SLO = (0.7, 1.3); SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70;
CTRL_KZ = 9; scramble seed 1.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): TWO smoke runs.
Smoke 1 (22 pass / 1 fail) exposed a SPEC DEFECT, not a wall fact:
the originally spec'd exactness ward "sum_i w_i p_k(theta_i)
p_l(theta_i) = delta_kl" is (i) numerically infeasible at these
depths whenever ALHAT is exterior (the chain evaluated at an
exterior Radau node overflows -- measured garbage dev 2.4e-01) and
(ii) MATHEMATICALLY TAUTOLOGICAL: sqrt(w_i) p_k(theta_i) = V_ki
exactly (shared recurrence), so the sum is eigenvector
orthogonality and certifies nothing.  AMENDMENT 1 (disclosed): the
exactness ward was re-specified to the non-tautological raw-moment
reproduction vs the source family (j <= J_MOM = 24), and the float
bars were reset a priori for that route (RAD_WARD 1e-8, NODE_HIT
1e-9).  AMENDMENT 2 (disclosed): the G1.d screen was spec'd on the
positive-floor subset, which the smoke revealed to be EMPTY (all 42
M1x2 floors are negative); the screen now reads the MAGNITUDE
|lam_min(M1x2)| with sign counts printed -- the sign verdict lives
in G1.c unchanged.  No other bar, band, count, enum or typed rule
was moved; both amendments make the wards STRICTER in content
(fail-first preserved).  Smoke 2 (23/23) MEASURED, recorded as the
honest context the frozen run must confirm: (a) THE GRAM COMPLETION
FAILS on every rung -- lam_min(M1x2) < 0 on 42/42 and lam_min(Mm) <
0 on 42/42 (min floor -1.45e-04) while Mp passes 42/42: the signed
comb measure is NOT a nonnegative functional on the [-1,1]-positive
cone at degree 2h - 2, and the failure is LOCALIZED AT THE x = +1
EDGE (the low-frequency end where the comb nodes accumulate); the
violation magnitude runs AHEAD of tau (|floor|/tau med -12, growing
to -152 at depth; magnitude screen slope +0.306, R^2 0.482, AMBIG)
-- the wall is PSD on squares by an ever-thinner margin while
already failing the wider cone by an ever-FATTER relative margin;
(b) the Radau construction is exact (raw moments 3.8e-15,
determinant quotient 2.9e-13, node hit 2.2e-16, weights >= 0,
interlacing OK, 0 degenerate rungs, min dist(x*, spec J_h) 6.3e-06)
and w* = w(x*) is numerically the Christoffel function (w*/lam_h(
x*) med 0.9978): w* range [6.6e-05, 2.2e-03], tau-screen slope
+0.138 with R^2 0.089 (PASS band but tau-DEcorrelated -- a mu_+-
only object, no negative-family content); (c) the pivot comparison
is RADAU-PIVOT-UNRELATED (corr +0.211, slope +0.307; gap/w* spans
6e2..1e5): the P2 gap is NOT a Gauss--Radau weight at the classical
node; (d) the smooth control is LOCWALL-SEEN 42/42.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as P2
SPEC (ii) for the W4 reproduction only; (iii) localized matrices at
size h - 1 (degree budget 2h - 2 respected); (iv) OLS/corr
population statistics as v900; (v) screens read the positive subset
with the excluded count printed; (vi) the node map x* = cos(2 pi
(u*/D)/L), u* = (NODE_C + NODE_S alpha) alpha, verbatim from
b_christoffel_deflation_probe.

NO-GO COMPLIANCE (frozen): no Gershgorin/Brauer/Weyl bound on raw B
retried as content (W4 reproduction only); no rank-1 approximation
of the core update; no plain Herglotz wall certificate; no fit
where an identity is claimed (G1.a/b, G2.a-d are exact wards; the
OLS fits in G1.d/G2.f/G3 are typed trend measurements).

NO RH claim: the completion certificate is a statement about the
deployed v563 window family at finite degree per rung -- it does
not prove tau_h > 0 for all h and does not bound the localized
floors below by a positive constant; the Radau algebra is classical
for any chain.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids zetazero
/ nzeros / primerange / isprime / primepi / nextprime / prevprime);
v563 READ-ONLY; RNG only inside the declared scramble control;
stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core
machinery verbatim from port_tangent_schur_probe.py (round 58) =
v900 chain via b_christoffel_deflation_probe.py; classical node
drift law from node_origin_arch_probe.py (declared input); Golub
(1973) Radau construction; Lukacs representation + truncated
K-moment problem on [-1, 1] (classical).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wall_gram_radau_probe.py
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
MIN_RADAU = 30
NODE_C = 0.3727                # node_origin drift law (declared)
NODE_S = -0.0116
MINB_REF = 0.679
MINB_RTOL = 2e-2
GAPMIN_REF = 0.052
GAPMED_REF = 0.888
GAP_RTOL = 5e-2
M0_WARD = 1e-8                 # G1.a
TAU2_WARD = 1e-8               # G1.b
LOC_TOL = 1e-10                # G1.c
DQ_WARD = 1e-6                 # G2.a
NODE_HIT = 1e-9                # G2.b
RAD_WARD = 1e-8                # G2.c (raw moments, see header)
J_MOM = 24                     # G2.c degree slice
ITL_TOL = 1e-10                # G2.d
RES_TOL = 1e-10                # G2.e
RATIO_ID = 1e-6                # G3
TRACK_CORR = 0.90
TRACK_SLO = (0.7, 1.3)
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


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None,
                 keep_chain=False):
    """v900 verbatim wall + fixed-core split (chain retained on
    demand; caller drops big arrays)."""
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
        out["xs"], out["ws"] = xs, ws
        out["ys"], out["vs"] = ys, vs
        out["Pn"] = Pn
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


def corr(x, y):
    return float(np.corrcoef(np.asarray(x, float),
                             np.asarray(y, float))[0, 1])


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


# ------------------------------ probe machinery
def node_of(r):
    """The frozen node map u* -> x* (b_christoffel verbatim)."""
    ustar = (NODE_C + NODE_S * r["alpha"]) * r["alpha"]
    return math.cos(2.0 * math.pi * (ustar / r["D"]) / r["L"])


def moment_floors(r):
    """M0 two routes + the localized floors (signed quadrature)."""
    al, be, m0 = r["chain"]
    h = r["h"]
    xs, ws = r["xs"], r["ws"]
    ys, vs = r["ys"], r["vs"]
    Pn = r["Pn"]                       # at ys, h columns
    Px = eval_chain(al, be, m0, xs, h)
    H = (Pn * vs[:, None]).T @ Pn
    M0a = np.eye(h) - 0.5 * (H + H.T)
    Gp = (Px * ws[:, None]).T @ Px
    M0b = 0.5 * (Gp + Gp.T) - 0.5 * (H + H.T)
    dev = (float(np.linalg.norm(M0a - M0b))
           / max(float(np.linalg.norm(M0a)), 1e-300))
    lam0 = float(np.linalg.eigvalsh(M0a)[0])
    out = dict(dev=dev, lam0=lam0)
    hm = h - 1
    Pxm, Pnm = Px[:, :hm], Pn[:, :hm]
    for tag, gx, gy in (("x2", 1.0 - xs ** 2, 1.0 - ys ** 2),
                        ("m", 1.0 - xs, 1.0 - ys),
                        ("p", 1.0 + xs, 1.0 + ys)):
        Mloc = ((Pxm * (ws * gx)[:, None]).T @ Pxm
                - (Pnm * (vs * gy)[:, None]).T @ Pnm)
        Mloc = 0.5 * (Mloc + Mloc.T)
        out["lam_" + tag] = float(np.linalg.eigvalsh(Mloc)[0])
    return out


def radau_at(r, t):
    """Golub Radau at prescribed node t; two-route ALHAT.
    Returns None if t resonates with spec(J_h) (caller counts)."""
    al, be, m0 = r["chain"]
    h = r["h"]
    Jh = np.diag(al[:h]) + np.diag(be[:h - 1], 1) \
        + np.diag(be[:h - 1], -1)
    evJ = np.linalg.eigvalsh(Jh)
    dist = float(np.min(np.abs(evJ - t)))
    if dist < RES_TOL:
        return None
    rhs = np.zeros(h)
    rhs[-1] = be[h - 1] ** 2
    delta = np.linalg.solve(Jh - t * np.eye(h), rhs)
    alhat = t + float(delta[-1])
    # determinant quotient via continued fraction:
    # r_k = det(J_k - t)/det(J_{k-1} - t)
    rk = al[0] - t
    for k in range(1, h):
        rk = (al[k] - t) - be[k - 1] ** 2 / rk
    alhat_dq = t + be[h - 1] ** 2 / rk
    JR = np.zeros((h + 1, h + 1))
    JR[:h, :h] = Jh
    JR[h, h] = alhat
    JR[h - 1, h] = JR[h, h - 1] = be[h - 1]
    theta, V = np.linalg.eigh(JR)
    w = m0 * V[0, :] ** 2
    i_star = int(np.argmin(np.abs(theta - t)))
    hit = float(abs(theta[i_star] - t))
    # raw-moment exactness vs the source family (stable route;
    # the p-basis version is the spectral tautology, see header)
    xs, ws = r["xs"], r["ws"]
    exdev = 0.0
    mr = np.ones_like(theta)
    ms = np.ones_like(xs)
    for _j in range(J_MOM + 1):
        exdev = max(exdev, abs(float(w @ mr) - float(ws @ ms)) / m0)
        mr = mr * theta
        ms = ms * xs
    # Cauchy interlacing theta^R_i <= theta^G_i <= theta^R_{i+1}
    itl_ok = bool(np.all(theta[:h] <= evJ + ITL_TOL)
                  and np.all(evJ <= theta[1:] + ITL_TOL))
    pt = eval_chain(al, be, m0, np.array([t]), h)[0]
    lam_ch = 1.0 / float(pt @ pt)
    return dict(alhat=alhat,
                dq_dev=abs(alhat - alhat_dq) / max(abs(alhat), 1.0),
                dist=dist, hit=hit, exdev=exdev,
                wneg=int(np.sum(w < 0.0)), itl_ok=itl_ok,
                wstar=float(w[i_star]), lam_ch=lam_ch)


def drop_big(r):
    for k in ("chain", "xs", "ws", "ys", "vs", "Pn"):
        r.pop(k, None)


def main():
    section("PRIME.PORT.GRAM.COMPLETION.01 + PRIME.PORT.RADAU."
            "WEIGHT.01 -- Gram completion of the signed comb "
            "measure + the Radau weight at the classical node "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder (ONE pass: floors + Radau per "
            "rung, big arrays dropped) + P2/P3 reproduction")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    n_degen = 0
    for kz in zones:
        r = gram_anatomy(kz, keep_chain=True)
        if r is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
            truth.append(None)
            continue
        r["fl"] = moment_floors(r)
        r["xstar"] = node_of(r)
        r["rad"] = radau_at(r, r["xstar"])
        if r["rad"] is None:
            n_degen += 1
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
        bestg = max(gersh_min(B), gersh_scaled(B), cassini_scaled(B))
        rows.append(dict(r1=r1, r2=r2, minB=minB, gap=gap,
                         bestg=bestg))
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

    # ------------------------------------------------------------ G1
    section("G1 -- THE GRAM COMPLETION (localized moment floors of "
            "the signed comb measure)")
    dev0 = max(r["fl"]["dev"] for r in truth)
    check("G1.a WARD two-route M0 (pipeline I - H vs direct signed "
          "quadrature): max rel dev %.2e <= %.0e" % (dev0, M0_WARD),
          dev0 <= M0_WARD, kill="K2")
    tie = max(abs(r["fl"]["lam0"] - r["tau"])
              / max(abs(r["tau"]), 1e-300) for r in truth)
    check("G1.b WARD spectrum tie lam_min(M0) == tau: max rel dev "
          "%.2e <= %.0e" % (tie, TAU2_WARD), tie <= TAU2_WARD,
          kill="K2")
    print("    kz   h    tau        lam(M1x2)  ratio    lam(Mm)"
          "    lam(Mp)    w*         w*/lam_ch  alhat      "
          "dist(x*,J)")
    for r in truth:
        fl, rad = r["fl"], r["rad"]
        print("    %-4d %-4d %.3e  %+.3e %7.2f  %+.2e  %+.2e  "
              "%s"
              % (r["kz"], r["h"], r["tau"], fl["lam_x2"],
                 fl["lam_x2"] / r["tau"], fl["lam_m"], fl["lam_p"],
                 ("%.3e  %8.4f   %+9.3f  %.1e"
                  % (rad["wstar"], rad["wstar"] / rad["lam_ch"],
                     rad["alhat"], rad["dist"]))
                 if rad else "DEGENERATE"), flush=True)
    n_x2 = sum(1 for r in truth if r["fl"]["lam_x2"] < -LOC_TOL)
    n_m = sum(1 for r in truth if r["fl"]["lam_m"] < -LOC_TOL)
    n_p = sum(1 for r in truth if r["fl"]["lam_p"] < -LOC_TOL)
    minfloor = min(min(r["fl"]["lam_x2"], r["fl"]["lam_m"],
                       r["fl"]["lam_p"]) for r in truth)
    if n_x2 == 0 and n_m == 0 and n_p == 0:
        g1c = "GRAM-COMPLETION-CERTIFIED(minfloor=%.3e)" % minfloor
    else:
        g1c = ("GRAM-COMPLETION-FAILS(x2:%d, m:%d, p:%d)"
               % (n_x2, n_m, n_p))
    check("G1.c typed: %s (Lukacs cone at degree 2h - 2; W >= 0 "
          "Gram representation exists iff all floors >= -%.0e)"
          % (g1c, LOC_TOL), True)
    lx2 = np.array([r["fl"]["lam_x2"] for r in truth])
    taus = np.array([r["tau"] for r in truth])
    n_neg = int(np.sum(lx2 < 0))
    _a, sl_loc, r2_loc = ols_line(np.log(taus),
                                  np.log(np.abs(lx2)))
    print("\n    localized floor tau-screen (MAGNITUDE |lam(M1x2)|"
          "; sign counts %d-/%d+): slope vs log tau = %+.4f (R^2 "
          "%.3f); lam(M1x2)/tau med %.3f"
          % (n_neg, len(lx2) - n_neg, sl_loc, r2_loc,
             float(np.median(lx2 / taus))))
    if abs(sl_loc) <= SLOPE_PASS:
        g1d = "LOC-SCREEN-PASS(slope=%+.3f)" % sl_loc
    elif sl_loc >= SLOPE_RELOC:
        g1d = "LOC-SCREEN-RELOC(slope=%+.3f)" % sl_loc
    else:
        g1d = "LOC-SCREEN-AMBIG(slope=%+.3f)" % sl_loc
    check("G1.d typed: %s (bands PASS |s| <= %.2f, RELOC s >= "
          "%.2f)" % (g1d, SLOPE_PASS, SLOPE_RELOC), True)

    # ------------------------------------------------------------ G2
    section("G2 -- THE RADAU WEIGHT at the classical node")
    usable = [r for r in truth if r["rad"] is not None]
    check("G2.e usable-rung census: %d usable, %d degenerate "
          "(dist < %.0e); WARD >= %d usable"
          % (len(usable), n_degen, RES_TOL, MIN_RADAU),
          len(usable) >= MIN_RADAU, kill="K1")
    if KILLS:
        return finish({})
    dq = max(r["rad"]["dq_dev"] for r in usable)
    check("G2.a WARD ALHAT two-route (tridiagonal solve vs "
          "determinant-quotient continued fraction): max rel dev "
          "%.2e <= %.0e" % (dq, DQ_WARD), dq <= DQ_WARD, kill="K2")
    hit = max(r["rad"]["hit"] for r in usable)
    check("G2.b WARD prescribed node hit: max |theta* - x*| %.2e "
          "<= %.0e" % (hit, NODE_HIT), hit <= NODE_HIT, kill="K2")
    exd = max(r["rad"]["exdev"] for r in usable)
    check("G2.c WARD raw-moment exactness vs the source family "
          "(j <= %d): max dev %.2e <= %.0e"
          % (J_MOM, exd, RAD_WARD), exd <= RAD_WARD, kill="K2")
    n_wneg = sum(r["rad"]["wneg"] for r in usable)
    itl_all = all(r["rad"]["itl_ok"] for r in usable)
    check("G2.d WARD classical consistency (automatic for the "
          "symmetric tridiagonal construction, sanity): all "
          "weights >= 0 (neg count %d) and Gauss/Radau Cauchy "
          "interlacing" % n_wneg, n_wneg == 0 and itl_all,
          kill="K2")
    ws_ = np.array([r["rad"]["wstar"] for r in usable])
    tu = np.array([r["tau"] for r in usable])
    posw = ws_ > 0
    _a, sl_w, r2_w = ols_line(np.log(tu[posw]), np.log(ws_[posw]))
    rat_ch = np.array([r["rad"]["wstar"] / r["rad"]["lam_ch"]
                       for r in usable])
    print("    w* range [%.3e, %.3e]; tau-screen slope %+.4f (R^2 "
          "%.3f, %d excluded); w*/lam_ch(x*) med %.4f (range "
          "[%.4f, %.4f]); min dist(x*, spec J_h) %.2e"
          % (float(np.min(ws_)), float(np.max(ws_)), sl_w, r2_w,
             int(np.sum(~posw)), float(np.median(rat_ch)),
             float(np.min(rat_ch)), float(np.max(rat_ch)),
             float(np.min([r["rad"]["dist"] for r in usable]))))
    if abs(sl_w) <= SLOPE_PASS and bool(np.all(posw)):
        g2f = "RADAUW-SCREEN-PASS(slope=%+.3f)" % sl_w
    elif sl_w >= SLOPE_RELOC:
        g2f = "RADAUW-SCREEN-RELOC(slope=%+.3f)" % sl_w
    else:
        g2f = "RADAUW-SCREEN-AMBIG(slope=%+.3f)" % sl_w
    check("G2.f typed: %s (bands PASS |s| <= %.2f, RELOC s >= "
          "%.2f)" % (g2f, SLOPE_PASS, SLOPE_RELOC), True)

    # ------------------------------------------------------------ G3
    section("G3 -- THE PIVOT COMPARISON (P2 gap vs w* at the "
            "target rung)")
    print("    step        gap        w*(r2)     gap/w*")
    gg, ww = [], []
    for row in rows:
        rad2 = row["r2"]["rad"]
        if rad2 is None or rad2["wstar"] <= 0:
            continue
        gg.append(row["gap"])
        ww.append(rad2["wstar"])
        print("    h %3d->%3d  %.3e  %.3e  %9.3f"
              % (row["r1"]["h"], row["r2"]["h"], row["gap"],
                 rad2["wstar"], row["gap"] / rad2["wstar"]),
              flush=True)
    gg = np.array(gg)
    ww = np.array(ww)
    reldev = float(np.max(np.abs(gg / ww - 1.0)))
    co = corr(np.log(gg), np.log(ww))
    _a, sl_gw, _r = ols_line(np.log(ww), np.log(gg))
    print("\n    max rel dev |gap/w* - 1| = %.3f; corr(log gap, "
          "log w*) = %+.3f; slope log gap vs log w* = %+.3f"
          % (reldev, co, sl_gw))
    if reldev <= RATIO_ID:
        g3 = "RADAU-PIVOT-IDENTITY(dev=%.1e)" % reldev
    elif co >= TRACK_CORR and TRACK_SLO[0] <= sl_gw <= TRACK_SLO[1]:
        g3 = "RADAU-PIVOT-TRACK(corr=%+.3f, slope=%+.3f)" % (co,
                                                             sl_gw)
    else:
        g3 = "RADAU-PIVOT-UNRELATED(corr=%+.3f, slope=%+.3f)" % (
            co, sl_gw)
    check("G3.1 typed: %s (bands IDENTITY dev <= %.0e; TRACK corr "
          ">= %.2f and slope in [%.1f, %.1f])"
          % (g3, RATIO_ID, TRACK_CORR, TRACK_SLO[0], TRACK_SLO[1]),
          True)

    # ------------------------------------------------------------ C
    section("C -- controls: smooth world + Epstein/scramble")
    check("C0.1 WARD truth wall holds (neg(A) = 0 on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    n_viol = 0
    n_locneg = 0
    n_smdone = 0
    for kz in zones:
        rs = gram_anatomy(kz, world_fn=world_smooth,
                          keep_chain=True)
        if not isinstance(rs, dict):
            continue
        n_smdone += 1
        if rs["negA"] > 0:
            n_viol += 1
        fls = moment_floors(rs)
        if fls["lam_x2"] < -LOC_TOL:
            n_locneg += 1
        drop_big(rs)
    check("C1.1 WARD smooth violates at rung level (neg(A) > 0 on "
          "%d of %d rungs)" % (n_viol, n_smdone), n_viol > 0,
          kill="K2")
    lw = ("LOCWALL-SEEN(%d/%d)" % (n_locneg, n_smdone)
          if n_locneg > 0 else "LOCWALL-BLIND(0/%d)" % n_smdone)
    check("C1.2 typed: %s (the localized completion floor on the "
          "smooth world; SEEN = the certificate is wall-sensitive)"
          % lw, True)
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

    return finish(dict(dev0=dev0, g1c=g1c, g1d=g1d, exd=exd,
                       g2f=g2f, g3=g3, lw=lw))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("GRAMRADAU-MEASURED / M0-IDENTITY-EXACT"
                   "(%(dev0).1e) / %(g1c)s / %(g1d)s / RADAU-EXACT"
                   "(%(exd).1e) / %(g2f)s / %(g3)s / %(lw)s"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): a certified Gram completion says the
  signed comb measure is nonnegative on the full [-1,1]-positive
  cone at degree 2h - 2 -- a strictly stronger statement than the
  wall (squares only) at each rung, but its floor must be read with
  its tau-screen: a RELOC floor is the wall floor relocated, not a
  new margin.  The Radau construction has automatic positivity/
  interlacing -- the classical criteria cannot fail here; the
  content is in w*, its screen, and the pivot comparison.  NO RH
  claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
