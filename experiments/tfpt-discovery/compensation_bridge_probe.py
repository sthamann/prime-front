#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""compensation_bridge_probe -- PRIME.PORT.COMPBRIDGE.01
(EXPLORATION ONLY, experiments/; round 54, named object (a) from
CXI: are the CD-level compensation identity of v872 and the
inheritance-level geometry/atom opposition of round 53 two readings
of ONE identity?  2026-08-09.)

THE QUESTION (frozen): v872 (PRIME.CD.DAMPING.COMPENSATION.01)
decomposes the STATIC wall at one rung EXACTLY into indefinite
cross-measure Jacobi geometry plus PSD arithmetic Christoffel
damping, I - C*C = T_1 + T_2 with T_1 = I - U*U and T_2 =
U*(I - D_-^2)U, with near-cancellation at the soft direction
leaving tau (kz9: -0.0328 + 0.0330 = 1.68e-4 = tau).  Round 53
(PRIME.PORT.RATIOSOURCE.01) decomposes the DYNAMIC step between
rungs into geometry re-test + atom block, delta_v = GEO_v + ATOM_v,
with sign(GEO_v) opposing sign(ATOM_v) on 28/28 dangerous steps and
near-cancellation leaving the O(1) ratio (BOUND-BY-COHERENCE).
HYPOTHESIS (frozen): the step decomposition is the DIFFERENCE of
the static decomposition -- Delta(wall) = Delta(T_1) + Delta(T_2)
-- and the measured GEO/ATOM opposition is Delta(T_1) vs Delta(T_2)
in disguise: the geometry increment carries Delta T_1, the atom
block carries Delta T_2, and their opposition IS the differentiated
compensation.

THE FROZEN CHOICE (the common object; derived and frozen BEFORE the
run): v872 lives on the plus/state side (h x h pencil frame); the
round-53 window lives on the folded NEGATIVE nodes, where the
round-53 kernel is E = CC* and the compressed base is A = I - C_J =
Schur[(I - E)] on the 12 aliases JWIN.  With C = D_- U and D_+ = I
(the v870 Gauss frame theorems), the SAME two named source objects
transport to the minus side EXACTLY:

    I - CC*  =  D_-(I - UU*)D_-  +  (I - D_-^2)
             =        T~_1        +      T~_2 ,

and in E coordinates  T~_1 = diag(E) - E  (the pure off-diagonal
cross-measure Jacobi kernel; indefinite)  and  T~_2 = I - diag(E)
(the diagonal arithmetic Christoffel damping; diag(E) = D_-^2, PSD
iff max D_- <= 1 -- the v870 ladder-wide bound 0.997041).  The
12-window compression is the Schur CONGRUENCE  A = X^T (I - E) X
with X = [I; -S_oo^{-1} S_ow] built from the FULL S = I - E (shared
by both terms -- the unique congruence that reproduces the Schur
complement and treats the two terms symmetrically), giving the
EXACT static split  A = A_1 + A_2  per rung and the EXACT
differentiated identity  Delta_h = DC = Delta A_1 + Delta A_2  per
step.  B0 wards this reading against the GENUINE v872 construction
(gauss_node_unitary machinery READ-ONLY: U, D_-, C^G, the plus-side
split, the soft-direction ledger) at the v872 ledger rungs
{9, 12, 40}.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run):

 W   PIPELINE WARDS (kill -> PIPELINE-BROKEN): W1 >= 30 truth
     rungs; W1b atom prefix law exact; W2 jav == JWIN in order on
     every truth full-window rung; W3 >= 20 truth full-window
     pairs, all bases PD.  W5 LINEARITY WARD (kill -> WARD-BROKEN):
     own per-atom tent rows reassemble the deployed alias density,
     max rel dev <= 1e-9 truth AND smooth (round-53 verbatim).

 R0  ROUND-53 ANCHOR (kill -> WARD-BROKEN; verbatim refs): (a)
     symmetrization <= 1e-12, (b) reconstruction <= 1e-10, (c)
     Rayleigh identity <= 1e-9, (d) ledger 31 pairs / min eta
     0.0050 / max(-lam) 0.9950 (tol 5.001e-5) / med eta 0.29 (tol
     5.001e-3), (e) slopes eta +0.108, tau -2.74, b_d -3.716, b_a
     -3.456 (round-52/53 tolerances).

 B0  THE v872 RECONSTRUCTION (the frame bridge; rungs {9, 12, 40};
     kill -> WARD-BROKEN): via gauss_node_unitary (READ-ONLY):
     minus arm measure-tight; fold-index sets identical to the
     round-53 negative nodes; GAUGE EQUIVALENCE (spec v2(a)): the
     gnu minus frame rows F[g, k] = e^{-i th k} - e^{-i th(2h-1-k)}
     = 2i e^{-i th (2h-1)/2} sin((h - 1/2 - k) th) carry the
     th-dependent unimodular phase Phi = diag(e^{-i th_g (2h-1)/2})
     relative to the real polynomial frame of the round-53 kernel,
     so CC* = Phi E_53 Phi* EXACTLY (a diagonal unitary gauge:
     T~_2 invariant, T~_1 off-diagonals rotated) -- warded as
     ||Re(Phi* CC* Phi) - E_53||/||E_53|| <= 1e-8 with the residual
     imaginary part <= 1e-9; max |diag(E_53) - D_-^2| <= 1e-8;
     ||Re(Phi* D_-(I - UU*)D_- Phi) - (diag(E_53) -
     E_53)||/||E_53|| <= 1e-8; plus-side v872 W1 split rel <= 1e-6;
     SOFT LEDGER: (t_1, t_2) at e_soft^G within 5.001e-5 of the
     v872 prints (kz9 -0.0328/+0.0330, kz12 -0.0743/+0.0744, kz40
     -0.0121/+0.0121), the sums within the print-rounding radius of
     1.68e-4 / 7.65e-5 / 6.66e-7, |s_1 + s_2 - tau| <= max(1e-10,
     1e-6 tau) (spec v2(b)), kappa(kz9) in [2.6, 2.8].

 B1  THE STATIC SPLIT ALONG THE LADDER (kill -> WARD-BROKEN): per
     truth full-window rung  ||A_1 + A_2 - A_brg||_F <= 1e-12
     (exact linearity of the congruence) and ||A_brg - (I -
     C_J)||_F <= 1e-6 (the two Schur routes agree; absolute
     Frobenius on O(1) matrices, measured max printed -- the
     deep-rung conditioning note is typed in SPEC v1(iv)); truth
     max diag(E) <= 1 + 1e-9 on EVERY built rung (T~_2 PSD: the
     v870 damping bound; ladder max sqrt printed vs 0.997041).

 B2  THE DIFFERENTIATED IDENTITY (the decisive correlation): per
     dangerous step (lambda_min < 0) with nonempty moving block
     (count warded == 28, opposition census warded == 28/28 -- the
     round-53 citations): g_1 = v^T Delta A_1 v, g_2 = v^T Delta
     A_2 v (v = v_min of H, round-51 convention); SUM WARD (kill ->
     WARD-BROKEN): |g_1 + g_2 - v^T Delta A_brg v| <= 1e-12 per
     step.  THE TWO CORRELATIONS (Pearson, signed, across the 28
     steps): c_1 = corr(GEO_v, g_1), c_2 = corr(ATOM_v, g_2);
     per-step ratio tables g_1/GEO_v and g_2/ATOM_v printed; the
     crossed pairings corr(GEO_v, g_2), corr(ATOM_v, g_1) and the
     transport corr(delta_v, dbrg) printed REPORT-ONLY (the
     density->operator orientation is a frame convention, hence the
     bar is on |c_i| with equal signs).  TYPED (never kills):
     BRIDGE-IDENTIFIED iff |c_1| >= 0.9 AND |c_2| >= 0.9 AND
     sign(c_1) == sign(c_2) AND both median |ratios| in [0.2, 5.0]
     (the O(1) bar); BRIDGE-PARTIAL iff exactly one correlation
     passes, or both pass but a sign/ratio leg fails (typed);
     BRIDGE-DISTINCT iff both correlations < 0.9 (honest -- the two
     compensations are genuinely different structures).

 B3  THE UNIFIED READING: if BRIDGE-IDENTIFIED, the inheritance
     margin eta = 1 + lambda_min(H) becomes the DIFFERENTIATED v872
     statement:  eta > 0  <=>  v^T Delta T~_2 v  >  -v^T Delta T~_1
     v - v^T A_a v  (the damping increment dominates the geometry
     increment at the dangerous direction, relative to the standing
     wall energy); the per-step ledger (a_h, g_1, g_2, a + g_1 +
     g_2 = eta a_h, eta) printed with min/median margins.  If
     BRIDGE-PARTIAL/DISTINCT: state plainly which parts do not
     match (failed correlations, crossed pairings, ratio medians).

 C   CONTROLS: (C2, kill -> WARD-BROKEN) smooth-world reproduction
     28 full-window pairs, 0 PD bases (round-53 refs); the smooth
     rungs feed the SAME split.  (C3, typed) THE DIFFERENTIATED
     SMOOTH CONTRAST: static census (# smooth rungs with max
     diag(E_s) > 1: does the false world break the damping sign,
     the v872-control analogue) + per crossing step (1 + Re mu_min
     < 0) the sign census of (g_1, g_2); TYPED by deterministic
     order: DIFF-NOCROSS if no crossing step; DIFF-DAMPING-BREAKS
     iff g_2 < 0 on >= 2/3 of crossing steps; else
     DIFF-GEOMETRY-BREAKS iff g_1 < 0 on >= 2/3; else DIFF-MIXED;
     truth-side sign censuses and the non-crossing specificity
     census printed alongside.  (C1, kill -> WARD-BROKEN) Epstein
     (x^2+5y^2) + scramble (seed 1) at kz 9: the compressed frame
     must die (exterior supercritical OR lam(C_J) > 1 OR window
     unavailable); max diag(E) reported if built (the damping-sign
     break of the v872 controls).

KILLS: K1 a W pipeline ward breaks -> PIPELINE-BROKEN; KW an R0 /
B0 / B1 / B2-sum / C2 / C1 ward breaks -> WARD-BROKEN.  The B2
bridge label and the C3 smooth label are TYPED, never kill.

VERDICT (frozen enum): COMPBRIDGE-MEASURED / <BRIDGE-IDENTIFIED |
BRIDGE-PARTIAL | BRIDGE-DISTINCT> / <DIFF-*>; else PIPELINE-BROKEN
/ WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX 900; JWIN (2,...,24); MIN_RUNGS 30;
MIN_PAIRS 20; ASYM 1e-12; RECON 1e-10; RAY 1e-9; LIN 1e-9; TOL4
5.001e-5, TOL3 5.001e-4, TOL2 5.001e-3; round-53 refs 31 / 0.0050 /
0.9950 / 0.29 / +0.108 / -2.74 / -3.716 / -3.456 / 28 smooth pairs
/ 0 PD; N_BLK 28, OPP 28/28; WB_LIN 1e-12, WB_SCHUR 1e-6 (Fro),
SUM_WARD 1e-12, DM_BAR 1 + 1e-9; B0: E_MATCH 1e-8 (gauged),
IM_GAUGE 1e-9, DIAG_MATCH 1e-8, MSPLIT 1e-8 (gauged), W1P 1e-6,
soft-ledger tolerances TOL4 on t-terms and half-ulp of the printed
sums (5.001e-7 / 5.001e-8 / 5.001e-10), TAU_ABS 1e-10 with TAU_REL
1e-6, KAPPA9 [2.6, 2.8]; CORR_BAR 0.9; RAT_LO 0.2, RAT_HI 5.0;
smooth attribution 2/3; CTRL_KZ 9; scramble seed 1.

SPEC v1 (2026-08-09, frozen + SHA-hashed before the first run);
mechanical concretizations frozen with it: (i) the B2 correlation /
ratio set is the lambda_min < 0 steps with nonempty moving block
(ATOM_v == 0 identically on empty blocks; excluded, counted); (ii)
build_window results cached per kz, shared truth/smooth, tent
matrices mass-free and shared (round-53 SPEC v1(i) verbatim); (iii)
E is stored only at the B0 rungs (memory); the split (A_1, A_2,
A_brg) is computed inside the rung builder and E discarded; (iv)
NOISE FLOOR note: A_brg and I - C_J are two solver routes through
S_oo; their per-step difference bounds |dbrg - d_53| ~ 1e-9..1e-6
absolute, so deep-rung d values below that floor carry visible
relative discrepancy -- both columns are printed and the
correlations are magnitude-dominated by the shallow steps (typed,
never kills beyond WB_SCHUR); (v) all Pearson correlations on raw
signed per-step values; (vi) smooth general-branch eigenvector
deaths counted and skipped (round-53 verbatim).

SPEC v2 (2026-08-09, after run 1; fail-first preserved -- run 1's
B0.1/B0.2 FAILs stand as the honest record of the v1 bars; no B2 /
B1 / R0 / C bar or typed label touched; run 1 typed
BRIDGE-DISTINCT under identical B2 bars): (a) THE GAUGE: run 1
measured ||E_53 - Re-part(gnu kernel)||rel ~ 0.35 with the
DIAGONAL matching at 1e-13 and all gnu-internal wards at 1e-13 --
the mismatch is exactly the derived diagonal unitary Phi above
(the gnu exponential-difference frame vs the real Chebyshev-IV
polynomial frame of the Lanczos path); v2 wards the gauge-
transported equality (bar 1e-8) instead of the ungauged real
part, and drops the now-redundant ungauged E_gnu assembly.  (b)
THE TAU BAR: the v1 relative bar 1e-6 on |s_1 + s_2 - tau| demands
6.7e-13 absolute at kz40 (tau = 6.66e-7), below the h = 591
quadrature floor (measured 1.5e-12 absolute); v2 bar max(1e-10,
1e-6 tau) -- kz9/kz12 unaffected.  (c) B2 gains the
DIFFERENTIATED-OPPOSITION census (REPORT-ONLY): run 1's B3 ledger
shows sign(g_1) opposite sign(g_2) with |g_1 + g_2| orders below
|g_1|, |g_2| on the dangerous steps -- the differentiated v872
compensation EXISTS at the operator level (opposition +
near-cancellation leaving eta a_h) even though it is NOT the
GEO/ATOM split; the census (opposition count, median cancellation
ratio |g_1 + g_2| / (|g_1| + |g_2|)) makes it a printed number.

NO RH claim: exact finite-dimensional identities and measured
correlations on the deployed v563 ladder are statements about
finite window truncations, not about zeros.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids zetazero
/ nzeros / primerange / isprime / primepi / nextprime / prevprime);
no sieve needed (deployed U_ALL / MU_ALL prefix tables only); v563
READ-ONLY; gauss_node_unitary_probe READ-ONLY; RNG only inside the
declared scramble control; stdout only; writes nothing.

Sources (read-only): v563_paper2_readouts (build_window,
atom_lags_at, arch_lags, prefix law -- verbatim);
ratio_euler_projection_probe.py (PRIME.PORT.RATIOSOURCE.01, round
53: pipeline, congruence, GEO/ATOM projection, smooth world,
controls -- verbatim); relative_congruence_probe.py /
eta_margin_source_probe.py lineage via round 53;
gauss_node_unitary_probe.py (PRIME.CONTRACTOR.GAUSSNODE.01, gated
in v870) for the B0 reconstruction; v872_damping_compensation.py
(the promoted identity + printed ledger refs; cited, not re-run).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/compensation_bridge_probe.py
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
import gauss_node_unitary_probe as gnu     # noqa: E402  (READ-ONLY)

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
NJ = len(JWIN)
MIN_RUNGS = 30
MIN_PAIRS = 20
MIN_COMMON_J = 8
ASYM_WARD = 1e-12
RECON_WARD = 1e-10
RAY_WARD = 1e-9
LIN_WARD = 1e-9
TOL4 = 5.001e-5
TOL3 = 5.001e-4
TOL2 = 5.001e-3
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

# round-53 anchor refs (verbatim)
REF_N_TRUTH_PAIRS = 31
REF_TRUTH_MINETA = 0.0050
REF_TRUTH_MAXNEG = 0.9950
REF_TRUTH_MEDETA = 0.29
REF_SLOPE_ETA = +0.108
REF_SLOPE_TAU = -2.74
REF_SLOPE_D = -3.716
REF_SLOPE_A = -3.456
REF_N_SMOOTH_PAIRS = 28
REF_SMOOTH_PD = 0
REF_N_BLK = 28
REF_N_OPP = 28

# bridge bars
WB_LIN = 1e-12
WB_SCHUR = 1e-6
SUM_WARD = 1e-12
DM_BAR = 1.0 + 1e-9
E_MATCH = 1e-8
IM_GAUGE = 1e-9
DIAG_MATCH = 1e-8
MSPLIT_MATCH = 1e-8
W1P_WARD = 1e-6
TAU_REL = 1e-6
TAU_ABS = 1e-10
CORR_BAR = 0.9
RAT_LO = 0.2
RAT_HI = 5.0
KAPPA9 = (2.6, 2.8)
B0_RUNGS = (9, 12, 40)
# v872 printed soft-direction ledger: kz -> (t1, t2, sum, sum-tol)
REF_SOFT = {9: (-0.0328, +0.0330, 1.68e-4, 5.001e-7),
            12: (-0.0743, +0.0744, 7.65e-5, 5.001e-8),
            40: (-0.0121, +0.0121, 6.66e-7, 5.001e-10)}
REF_DM_LADDER = 0.997041   # v870/v872 ladder-wide max D_- (report)

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


# --------- pipeline, verbatim from round 53 (ratio_euler_projection)
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


def window_split(E, iwl):
    """THE FROZEN CHOICE: Schur congruence of the minus-side v872
    split.  S = I - E; X = [I at window rows; -S_oo^{-1} S_ow at
    the rest]; A_1 = X^T (diag(E) - E) X (geometry), A_2 = X^T
    (I - diag(E)) X (damping), A_brg = X^T S X."""
    r = E.shape[0]
    iol = [k for k in range(r) if k not in set(iwl)]
    S = np.eye(r) - E
    Y = np.linalg.solve(S[np.ix_(iol, iol)], S[np.ix_(iol, iwl)])
    X = np.zeros((r, NJ))
    X[iwl] = np.eye(NJ)
    X[iol] = -Y
    dE = np.diag(E).copy()
    A1 = X.T @ (dE[:, None] * X - E @ X)
    A2 = X.T @ ((1.0 - dE)[:, None] * X)
    Ab = X.T @ (S @ X)
    A1 = 0.5 * (A1 + A1.T)
    A2 = 0.5 * (A2 + A2.T)
    Ab = 0.5 * (Ab + Ab.T)
    return A1, A2, Ab, float(np.max(dE))


def rung_rec(kz, scramble_seed=None, comb=None, rr_cache=None,
             store_e=False):
    """One rung: build (verbatim round-53 path), window compression,
    alias-density bookkeeping AND the minus-side v872 split
    compressed to the 12-window (SPEC v1(iii))."""
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
    darch = grid_density(c_ar)
    L = 2 * M - 2
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, alpha=alpha, M=M, D=D, L=L,
               n_atom=len(uu), uu=uu, mm=mm,
               dJ=d[list(JWIN)].copy(),
               darchJ=darch[list(JWIN)].copy(),
               lamE=float(np.linalg.eigvalsh(E)[-1]),
               maxDm2=float(np.max(np.diag(E))))
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
        if out["full"]:
            A1, A2, Ab, _mx = window_split(E, iw)
            out["A1"], out["A2"], out["Ab"] = A1, A2, Ab
            out["wb_lin"] = float(np.linalg.norm(A1 + A2 - Ab))
            out["wb_schur"] = float(np.linalg.norm(
                Ab - (np.eye(NJ) - CJ)))
    if store_e:
        out["E"] = E
        out["ufn"] = [int(j) for j in uf_n]
    return out


def eps_comb(rr):
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
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


# ------------------------------------- the exact linear atom level
def tent_alias_G(uu, alpha, M):
    """Mass-free tent-row alias tests (round-53 verbatim)."""
    uu = np.asarray(uu, float)
    D = 2.0 * alpha / M
    L = 2 * M - 2
    th = 2.0 * math.pi * np.array(JWIN, float) / L
    G = np.zeros((len(uu), NJ))
    i0 = np.floor(uu / D).astype(int)
    for off in range(-2, 3):
        ii = i0 + off
        w = 1.0 - np.abs(ii * D - uu) / D
        m = (ii >= 0) & (ii < M) & (w > 0.0)
        if not np.any(m):
            continue
        iv = ii[m]
        cosmat = np.cos(np.outer(iv.astype(float), th))
        fac = 2.0 * cosmat
        fac[iv == 0, :] = 1.0
        sel = iv == M - 1
        fac[sel, :] = cosmat[sel, :]
        G[m, :] += w[m][:, None] * fac
    for n in np.nonzero(uu < D)[0]:      # deployed reflection branch
        u_j = float(uu[n])
        for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
            v = 1.0 - (i * D + u_j) / D
            if v > 0.0:
                gfac = (1.0 if i == 0 else
                        np.cos((M - 1) * th) if i == M - 1
                        else 2.0 * np.cos(i * th))
                G[n, :] += v * gfac
    return G


def lin_dev(rec, G):
    rhs = -0.5 * (rec["mm"] @ G)
    lhs = rec["dJ"] - rec["darchJ"]
    return float(np.max(np.abs(lhs - rhs)
                        / np.maximum(1.0, np.abs(rec["dJ"]))))


def step_projection(ra, rb, v, Ga, Gb):
    """GEO/ATOM split of the v-tested alias density increment
    (round-53 verbatim, trimmed to the fields used here)."""
    v2 = np.asarray(v, float) ** 2
    ka, kb = ra["n_atom"], rb["n_atom"]
    klo, khi = min(ka, kb), max(ka, kb)
    flow = "ENTER" if kb > ka else "LEAVE" if kb < ka else "NONE"
    host = rb if kb > ka else ra
    Gh = Gb if kb > ka else Ga
    sigma = -1.0 if kb > ka else 1.0
    dv = float(np.sum(v2 * (ra["dJ"] - rb["dJ"])))
    out = dict(flow=flow, nblk=khi - klo, dv=dv)
    if khi > klo:
        mmb = host["mm"][klo:khi]
        cvec = sigma * (-0.5) * mmb * (Gh[klo:khi] @ v2)
        out["atom"] = float(np.sum(cvec))
    else:
        out["atom"] = 0.0
    out["geo"] = dv - out["atom"]
    return out


def add_bridge_terms(row, ra, rb, v):
    """B2: the differentiated split projected on v (exact)."""
    if "A1" in ra and "A1" in rb:
        row["g1"] = float(v @ ((rb["A1"] - ra["A1"]) @ v))
        row["g2"] = float(v @ ((rb["A2"] - ra["A2"]) @ v))
        row["dbrg"] = float(v @ ((rb["Ab"] - ra["Ab"]) @ v))
        row["sumdev"] = abs(row["g1"] + row["g2"] - row["dbrg"])


def truth_pairs(rungs, Gs):
    """Round-51/52/53 congruence + minimizer + projections."""
    rows = []
    n_skip = 0
    n = NJ
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        Aa = np.eye(n) - ra["CJ"]
        Ab = np.eye(n) - rb["CJ"]
        DC = ra["CJ"] - rb["CJ"]           # A_{h+1} = A_h + DC
        ew, Vw = np.linalg.eigh(Aa)
        row = dict(ha=ra["h"], hb=rb["h"], kza=ra["kz"],
                   kzb=rb["kz"], pd=bool(ew[0] > 0.0),
                   tau=float(ew[0]))
        if not row["pd"]:
            rows.append(row)
            continue
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
                      / max(float(np.linalg.norm(Ab)), 1e-300))
        row["lam_min"] = float(lam[0])
        row["eta"] = 1.0 + float(lam[0])
        vmin = Wisq @ U[:, 0]
        vmin = vmin / float(np.linalg.norm(vmin))
        row["a_h"] = float(vmin @ (Aa @ vmin))
        row["d_h"] = float(vmin @ (DC @ vmin))
        row["ray_dev"] = (abs(row["d_h"] / row["a_h"]
                              - row["lam_min"])
                          / max(1.0, abs(row["lam_min"])))
        row.update(step_projection(ra, rb, vmin,
                                   Gs[ra["kz"]], Gs[rb["kz"]]))
        add_bridge_terms(row, ra, rb, vmin)
        rows.append(row)
    return rows, n_skip


def smooth_pairs(rungs, Gs):
    """Smooth full-window pairs, general branch (round-53
    verbatim) + the differentiated split terms."""
    rows = []
    n_skip = n_vdead = 0
    n = NJ
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        if not (ra.get("full") and rb.get("full")):
            n_skip += 1
            continue
        Aa = np.eye(n) - ra["CJ"]
        DC = ra["CJ"] - rb["CJ"]
        ew = np.linalg.eigvalsh(Aa)
        row = dict(ha=ra["h"], hb=rb["h"], pd=bool(ew[0] > 0.0))
        mu, Vg = np.linalg.eig(np.linalg.solve(Aa, DC))
        i_min = int(np.argmin(mu.real))
        row["mu_min"] = float(mu[i_min].real)
        vs = np.real(Vg[:, i_min])
        nv = float(np.linalg.norm(vs))
        if nv < 1e-12:
            n_vdead += 1
            rows.append(row)
            continue
        vs = vs / nv
        row["a_h"] = float(vs @ (Aa @ vs))
        row["d_h"] = float(vs @ (DC @ vs))
        row.update(step_projection(ra, rb, vs,
                                   Gs[ra["kz"]], Gs[rb["kz"]]))
        add_bridge_terms(row, ra, rb, vs)
        rows.append(row)
    return rows, n_skip, n_vdead


def ols(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    b = float(np.cov(x, y, bias=True)[0, 1] / np.var(x))
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def med(v):
    v = [x for x in v if np.isfinite(x)]
    return float(np.median(v)) if v else float("nan")


# ------------------------------------------- B0: v872 reconstruction
def b0_reconstruct(kz, rec):
    """Rebuild the genuine v872 objects (gnu READ-ONLY) at one
    ledger rung and ward the minus-side reading against them."""
    b = gnu.build_rung(kz)
    go = gnu.gauss_objects(b)
    if go["fail"] or len(go["thp"]) != b["h"]:
        return None
    sp = gnu.softport(b)
    h = b["h"]
    U = go["U"]
    Dm = go["Dm"]
    C = go["CG"]
    ImCC = np.eye(h) - C.conj().T @ C
    ImCC = 0.5 * (ImCC + ImCC.conj().T)
    T1p = np.eye(h) - U.conj().T @ U
    T1p = 0.5 * (T1p + T1p.conj().T)
    T2p = U.conj().T @ ((1.0 - Dm ** 2)[:, None] * U)
    T2p = 0.5 * (T2p + T2p.conj().T)
    w1p = float(np.linalg.norm(T1p + T2p - ImCC)
                / np.linalg.norm(ImCC))
    Q = go["BpG"] @ b["Rm"]
    esG = Q @ sp["esoft"]
    v = np.exp(0.5 * np.arange(h) * b["D"])
    v = v / np.linalg.norm(v)
    wpole = b["Rp"] @ v
    wpole = wpole / np.linalg.norm(wpole)
    pG = Q @ wpole
    pG = pG / np.linalg.norm(pG)
    y = np.linalg.solve(ImCC, pG)
    s = 1.0 / float(np.real(np.vdot(pG, y)))
    kap = s / sp["lam1"]
    s1 = float(np.real(np.vdot(esG, T1p @ esG)))
    s2 = float(np.real(np.vdot(esG, T2p @ esG)))
    # ---- minus side: the gauge-transported frozen-choice objects
    thm, wSm, modem = gnu.arm_gauss_system(b, -1)
    # gnu fold indices of the minus nodes
    _xs, _ws, thu = gnu.folded_arm_measure(b, -1)
    folds = [int(round(t * b["L"] / (2.0 * math.pi))) for t in thu]
    r53 = rec["E"]
    same_nodes = (folds == rec["ufn"])
    # the derived diagonal gauge (spec v2(a)):
    # F rows = 2i e^{-i th (2h-1)/2} sin((h-1/2-k) th)
    ph = np.exp(-1j * thm * (2.0 * h - 1.0) / 2.0)
    CCH = C @ C.conj().T                       # complex Hermitian
    Mg = ph.conj()[:, None] * CCH * ph[None, :]
    nR = max(1.0, float(np.max(np.abs(Mg.real))))
    im_rel = float(np.max(np.abs(Mg.imag))) / nR
    nE = max(float(np.linalg.norm(r53)), 1e-300)
    e_match = (float(np.linalg.norm(Mg.real - r53)) / nE
               if same_nodes else float("inf"))
    dm2_dev = (float(np.max(np.abs(np.diag(r53) - Dm ** 2)))
               if same_nodes else float("inf"))
    UUH = U @ U.conj().T
    T1m = Dm[:, None] * (np.eye(len(thm)) - UUH) * Dm[None, :]
    T1g = (ph.conj()[:, None] * T1m * ph[None, :]).real
    msplit = (float(np.linalg.norm(
        T1g - (np.diag(np.diag(r53)) - r53))) / nE
        if same_nodes else float("inf"))
    return dict(kz=kz, h=h, modem=modem, im_rel=im_rel,
                same_nodes=same_nodes, e_match=e_match,
                dm2_dev=dm2_dev, msplit=msplit,
                w1p=w1p, s1=s1, s2=s2, tau=sp["lam1"], kap=kap)


def main():
    section("PRIME.PORT.COMPBRIDGE.01 -- is the round-53 GEO/ATOM "
            "opposition the\ndifferentiated v872 compensation "
            "identity?  (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles; "
          "deployed prefix tables only)", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the ladders (truth + smooth; the split "
            "A = A_1 + A_2 per full rung)")
    rungs, srungs = [], []
    rrs, Gs = {}, {}
    n_smooth_dead = 0
    for kz in core.frame_a_zones():
        rr = core.build_window(kz)
        r = rung_rec(kz, rr_cache=rr,
                     store_e=(kz in B0_RUNGS))
        if not isinstance(r, dict):
            continue
        rrs[kz] = rr
        Gs[kz] = tent_alias_G(r["uu"], r["alpha"], r["M"])
        rungs.append(r)
        uu = np.asarray(rr["uu"], float)
        rs = rung_rec(kz, comb=(uu, smooth_masses(uu)),
                      rr_cache=rr)
        if isinstance(rs, dict):
            srungs.append(rs)
        else:
            n_smooth_dead += 1
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    srungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth: %d rungs, h %d .. %d | smooth-mass: %d "
          "rungs, %d chain/window deaths  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             len(srungs), n_smooth_dead, time.time() - T0))
    pref_dev = max(float(np.max(np.abs(
        2.0 * np.asarray(rr["lam"], float)
        - np.asarray(core.MU_ALL, float)[:int(rr["n_atom"])])))
        for rr in rrs.values())
    check("W1 >= %d truth rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W1b atom prefix law exact (max |mm - MU_ALL prefix| "
          "%.1e == 0)" % pref_dev, pref_dev == 0.0, kill="K1")
    jav_ok = all(r["jav"] == list(JWIN) for r in rungs
                 if r.get("full"))
    check("W2 coordinate freeze: jav == JWIN in order on every "
          "truth full-window rung", jav_ok, kill="K1")
    lin_t = max(lin_dev(r, Gs[r["kz"]]) for r in rungs)
    lin_s = max(lin_dev(r, Gs[r["kz"]]) for r in srungs)
    check("W5 LINEARITY WARD: own per-atom tent rows reassemble "
          "the deployed alias density (max rel dev truth %.1e, "
          "smooth %.1e <= %.0e)" % (lin_t, lin_s, LIN_WARD),
          lin_t <= LIN_WARD and lin_s <= LIN_WARD, kill="KW")
    if KILLS:
        return finish({})

    trows_all, n_skip_t = truth_pairs(rungs, Gs)
    trows = [r for r in trows_all if r["pd"]]
    check("W3 >= %d truth full-window pairs (%d skips), all "
          "bases PD" % (MIN_PAIRS, n_skip_t),
          len(trows) >= MIN_PAIRS
          and len(trows) == len(trows_all),
          "%d pairs" % len(trows), kill="K1")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ R0
    section("R0 -- the round-53 anchor (%d truth pairs)"
            % len(trows))
    asym_max = float(np.max([r["asym"] for r in trows]))
    rec_max = float(np.max([r["rec"] for r in trows]))
    ray_max = float(np.max([r["ray_dev"] for r in trows]))
    check("R0.a SYMMETRIZATION WARD: max ||H - H^T||/||H|| "
          "%.2e <= %.0e" % (asym_max, ASYM_WARD),
          asym_max <= ASYM_WARD, kill="KW")
    check("R0.b RECONSTRUCTION WARD: max rel "
          "||A^{1/2}(I+H)A^{1/2} - A_{h+1}|| %.2e <= %.0e"
          % (rec_max, RECON_WARD), rec_max <= RECON_WARD,
          kill="KW")
    check("R0.c RAYLEIGH IDENTITY WARD: max |vDv/vAv - lam_min| "
          "%.2e <= %.0e" % (ray_max, RAY_WARD),
          ray_max <= RAY_WARD, kill="KW")
    etas = np.array([r["eta"] for r in trows])
    min_eta = float(np.min(etas))
    med_eta = float(np.median(etas))
    max_neg = float(np.max([-r["lam_min"] for r in trows]))
    check("R0.d LEDGER: %d pairs == %d, min eta %.4f == %.4f, "
          "max(-lam_min) %.4f == %.4f (tol %.0e), med eta %.4f "
          "== %.2f (tol %.0e)"
          % (len(trows), REF_N_TRUTH_PAIRS, min_eta,
             REF_TRUTH_MINETA, max_neg, REF_TRUTH_MAXNEG, TOL4,
             med_eta, REF_TRUTH_MEDETA, TOL2),
          len(trows) == REF_N_TRUTH_PAIRS
          and abs(min_eta - REF_TRUTH_MINETA) <= TOL4
          and abs(max_neg - REF_TRUTH_MAXNEG) <= TOL4
          and abs(med_eta - REF_TRUTH_MEDETA) <= TOL2,
          kill="KW")
    lha = np.log([r["ha"] for r in trows])
    _, b_eta, _ = ols(lha, np.log(etas))
    _, b_tau, _ = ols(lha, np.log([r["tau"] for r in trows]))
    neg = [r for r in trows if r["lam_min"] < 0.0]
    lhn = np.log([r["ha"] for r in neg])
    _, b_d, _ = ols(lhn, np.log([abs(r["d_h"]) for r in neg]))
    _, b_a, _ = ols(lhn, np.log([r["a_h"] for r in neg]))
    check("R0.e SLOPES: eta %+0.4f == %+0.3f (tol %.0e), tau "
          "%+0.4f == %+0.2f (tol %.0e), b_d %+0.4f == %+0.3f, "
          "b_a %+0.4f == %+0.3f (tol %.0e)"
          % (b_eta, REF_SLOPE_ETA, TOL3, b_tau, REF_SLOPE_TAU,
             TOL2, b_d, REF_SLOPE_D, b_a, REF_SLOPE_A, TOL3),
          abs(b_eta - REF_SLOPE_ETA) <= TOL3
          and abs(b_tau - REF_SLOPE_TAU) <= TOL2
          and abs(b_d - REF_SLOPE_D) <= TOL3
          and abs(b_a - REF_SLOPE_A) <= TOL3, kill="KW")
    print("    dangerous-direction subset: lambda_min < 0 on "
          "%d/%d steps" % (len(neg), len(trows)))

    # ------------------------------------------------------------ B0
    section("B0 -- the v872 reconstruction at the ledger rungs "
            "%s (the frame bridge)" % (B0_RUNGS,))
    b0_ok = True
    led_ok = True
    for kz in B0_RUNGS:
        rec = next((r for r in rungs if r["kz"] == kz), None)
        if rec is None or "E" not in rec:
            check("B0 kz %d rung unavailable" % kz, False,
                  kill="KW")
            b0_ok = False
            continue
        g = b0_reconstruct(kz, rec)
        if g is None:
            check("B0 kz %d gnu Gauss system failed" % kz, False,
                  kill="KW")
            b0_ok = False
            continue
        wok = (g["modem"] == "measure-tight" and g["same_nodes"]
               and g["im_rel"] <= IM_GAUGE
               and g["e_match"] <= E_MATCH
               and g["dm2_dev"] <= DIAG_MATCH
               and g["msplit"] <= MSPLIT_MATCH
               and g["w1p"] <= W1P_WARD)
        b0_ok &= wok
        print("    kz %-3d h %-4d: minus arm %s, nodes %s | "
              "||Phi* CC* Phi - E53||rel %.1e (Im %.1e) | "
              "max|diagE - D-^2| %.1e |\n              "
              "||Phi* D-(I-UU*)D- Phi - (diagE - E)||rel %.1e | "
              "plus W1 %.1e"
              % (kz, g["h"], g["modem"],
                 "MATCH" if g["same_nodes"] else "MISMATCH",
                 g["e_match"], g["im_rel"], g["dm2_dev"],
                 g["msplit"], g["w1p"]))
        t1r, t2r, sref, stol = REF_SOFT[kz]
        sums = g["s1"] + g["s2"]
        taurel = abs(sums - g["tau"]) / max(g["tau"], 1e-300)
        lok = (abs(g["s1"] - t1r) <= TOL4
               and abs(g["s2"] - t2r) <= TOL4
               and abs(sums - sref) <= stol
               and abs(sums - g["tau"])
               <= max(TAU_ABS, TAU_REL * g["tau"]))
        led_ok &= lok
        print("              soft ledger: t1 %+.4f (ref %+.4f), "
              "t2 %+.4f (ref %+.4f), sum %.2e (ref %.2e) ~ tau "
              "%.2e (rel dev %.1e)"
              % (g["s1"], t1r, g["s2"], t2r, sums, sref,
                 g["tau"], taurel))
        if kz == 9:
            led_ok &= (KAPPA9[0] <= g["kap"] <= KAPPA9[1])
            print("              kappa(kz9) = %.3f (band [%.1f, "
                  "%.1f])" % (g["kap"], *KAPPA9))
    check("B0.1 [FRAME BRIDGE] the round-53 kernel E IS the v872 "
          "CC* up to the derived diagonal gauge Phi, its diagonal "
          "IS D_-^2, the minus-side split IS D_-(I-UU*)D_- + "
          "(I-D_-^2); plus-side W1 holds", b0_ok, kill="KW")
    check("B0.2 [SOFT LEDGER] the v872 soft-direction two-term "
          "ledger (t1, t2, sum ~ tau) and kappa(kz9) reproduced "
          "at print rounding", led_ok, kill="KW")

    # ------------------------------------------------------------ B1
    section("B1 -- the static split along the ladder (A = A_1 + "
            "A_2 on the 12-window)")
    full_t = [r for r in rungs if "A1" in r]
    wb_lin_max = max(r["wb_lin"] for r in full_t)
    wb_schur_max = max(r["wb_schur"] for r in full_t)
    check("B1.1 [LINEARITY] ||A_1 + A_2 - A_brg||_F %.1e <= "
          "%.0e on every full truth rung (%d rungs; the "
          "congruence is exactly additive)"
          % (wb_lin_max, WB_LIN, len(full_t)),
          wb_lin_max <= WB_LIN, kill="KW")
    check("B1.2 [SCHUR ROUTE] ||A_brg - (I - C_J)||_F %.1e <= "
          "%.0e on every full truth rung (two solver routes; "
          "SPEC v1(iv) noise floor)"
          % (wb_schur_max, WB_SCHUR),
          wb_schur_max <= WB_SCHUR, kill="KW")
    dm2_max = max(r["maxDm2"] for r in rungs)
    check("B1.3 [DAMPING SIGN] truth max diag(E) = D_-^2 <= 1 + "
          "1e-9 on every built rung (ladder max D_- = %.6f vs "
          "v870/v872 ladder bound %.6f) -- T~_2 and hence A_2 "
          "PSD" % (math.sqrt(dm2_max), REF_DM_LADDER),
          dm2_max <= DM_BAR, kill="KW")

    # ------------------------------------------------------------ B2
    sel = [r for r in neg if r["nblk"] > 0]
    section("B2 -- THE DIFFERENTIATED IDENTITY (%d dangerous "
            "steps with moving block)" % len(sel))
    n_opp = sum(1 for r in sel if r["geo"] * r["atom"] < 0.0)
    check("B2.1 [ROUND-53 CENSUS] %d/%d nonempty-block dangerous "
          "steps == %d, GEO/ATOM opposition on %d == %d/%d"
          % (len(sel), len(neg), REF_N_BLK, n_opp, REF_N_OPP,
             REF_N_BLK),
          len(sel) == REF_N_BLK and n_opp == REF_N_OPP,
          kill="KW")
    sum_max = max(r["sumdev"] for r in trows if "sumdev" in r)
    check("B2.2 [SUM WARD] |g_1 + g_2 - v^T Delta A_brg v| %.1e "
          "<= %.0e on every step (the differentiated identity "
          "is exact)" % (sum_max, SUM_WARD),
          sum_max <= SUM_WARD, kill="KW")
    print("\n    step        flow   GEO_v       g1=vDT1v    "
          "g1/GEO   ATOM_v      g2=vDT2v    g2/ATOM  d_53"
          "        d_brg")
    rat1, rat2 = [], []
    for r in sel:
        q1 = r["g1"] / r["geo"]
        q2 = r["g2"] / r["atom"]
        rat1.append(q1)
        rat2.append(q2)
        print("    h %3d->%3d  %-5s %+.3e  %+.3e  %+7.3f  "
              "%+.3e  %+.3e  %+7.3f  %+.2e  %+.2e"
              % (r["ha"], r["hb"], r["flow"], r["geo"], r["g1"],
                 q1, r["atom"], r["g2"], q2, r["d_h"],
                 r["dbrg"]))
    GEO = np.array([r["geo"] for r in sel])
    ATM = np.array([r["atom"] for r in sel])
    G1 = np.array([r["g1"] for r in sel])
    G2 = np.array([r["g2"] for r in sel])
    DV = np.array([r["dv"] for r in sel])
    DB = np.array([r["dbrg"] for r in sel])
    c1 = float(np.corrcoef(GEO, G1)[0, 1])
    c2 = float(np.corrcoef(ATM, G2)[0, 1])
    x12 = float(np.corrcoef(GEO, G2)[0, 1])
    x21 = float(np.corrcoef(ATM, G1)[0, 1])
    ctr = float(np.corrcoef(DV, DB)[0, 1])
    mr1 = med([abs(q) for q in rat1])
    mr2 = med([abs(q) for q in rat2])
    print("\n    THE TWO DECISIVE CORRELATIONS: corr(GEO_v, "
          "Delta T_1) = %+0.4f | corr(ATOM_v, Delta T_2) = "
          "%+0.4f" % (c1, c2))
    print("    crossed pairings (report): corr(GEO_v, Delta T_2)"
          " = %+0.4f | corr(ATOM_v, Delta T_1) = %+0.4f"
          % (x12, x21))
    print("    transport (report): corr(delta_v, dbrg) = %+0.4f"
          % ctr)
    print("    ratio medians: med|g1/GEO| = %.4f | med|g2/ATOM| "
          "= %.4f (O(1) band [%.1f, %.1f])"
          % (mr1, mr2, RAT_LO, RAT_HI))
    n_gopp = int(np.sum(G1 * G2 < 0.0))
    gcanc = [abs(r["g1"] + r["g2"])
             / (abs(r["g1"]) + abs(r["g2"])) for r in sel
             if abs(r["g1"]) + abs(r["g2"]) > 0.0]
    print("    DIFFERENTIATED-OPPOSITION census (SPEC v2(c), "
          "report): sign(g1) opposite sign(g2) on %d/%d steps; "
          "cancellation |g1+g2|/(|g1|+|g2|) med %.2e max %.2e "
          "-- the operator-level differentiated compensation"
          % (n_gopp, len(sel), med(gcanc),
             float(np.max(gcanc))))
    p1 = abs(c1) >= CORR_BAR
    p2 = abs(c2) >= CORR_BAR
    sign_ok = (c1 * c2 > 0.0)
    ratio_ok = (RAT_LO <= mr1 <= RAT_HI
                and RAT_LO <= mr2 <= RAT_HI)
    if p1 and p2 and sign_ok and ratio_ok:
        bridge = "BRIDGE-IDENTIFIED"
    elif p1 or p2:
        legs = []
        if not p1:
            legs.append("corr(GEO,DT1) %.2f < %.1f" % (c1,
                                                       CORR_BAR))
        if not p2:
            legs.append("corr(ATOM,DT2) %.2f < %.1f" % (c2,
                                                        CORR_BAR))
        if p1 and p2 and not sign_ok:
            legs.append("sign mismatch")
        if p1 and p2 and not ratio_ok:
            legs.append("ratios not O(1): %.3f / %.3f"
                        % (mr1, mr2))
        bridge = "BRIDGE-PARTIAL (%s)" % "; ".join(legs)
    else:
        bridge = "BRIDGE-DISTINCT"
    check("B2.3 typed: %s (|c1| %.4f, |c2| %.4f vs bar %.1f; "
          "ratio medians %.3f / %.3f vs [%.1f, %.1f])"
          % (bridge, abs(c1), abs(c2), CORR_BAR, mr1, mr2,
             RAT_LO, RAT_HI), True)

    # ------------------------------------------------------------ B3
    section("B3 -- the unified reading")
    print("    step        a_h       g1=vDT1v    g2=vDT2v    "
          "a+g1+g2     eta")
    for r in neg:
        if "g1" not in r:
            continue
        print("    h %3d->%3d  %.4f   %+.3e  %+.3e  %+.3e  %.4f"
              % (r["ha"], r["hb"], r["a_h"], r["g1"], r["g2"],
                 r["a_h"] + r["g1"] + r["g2"], r["eta"]))
    margins = [r["a_h"] + r["g1"] + r["g2"] for r in neg
               if "g1" in r]
    if bridge == "BRIDGE-IDENTIFIED":
        print("""
    THE UNIFIED INEQUALITY (measured): on every dangerous step
      eta = 1 + lambda_min(H) > 0
        <=>  v^T Delta T~_2 v  >  - v^T Delta T~_1 v - v^T A_a v,
    i.e. the ARITHMETIC DAMPING INCREMENT dominates the JACOBI
    GEOMETRY INCREMENT at the dangerous direction, relative to the
    standing wall energy -- the round-53 GEO/ATOM opposition IS the
    differentiated v872 compensation.  Ledger: min margin
    a + g1 + g2 = %.3e, median %.3e; min eta %.4f.""" % (
            min(margins), med(margins), min_eta))
    else:
        print("""
    NO unified statement is claimed (typed %s): the per-step
    ledger above is the honest record; min margin a + g1 + g2 =
    %.3e, min eta %.4f.  The mismatch is stated in B2/V.""" % (
            bridge.split()[0], min(margins), min_eta))

    # ------------------------------------------------------------ C
    section("C -- controls")
    srows, n_skip_s, n_vdead = smooth_pairs(srungs, Gs)
    n_pd_s = sum(1 for r in srows if r["pd"])
    check("C2 smooth reproduction: %d pairs == %d (%d skips, %d "
          "eigenvector deaths), PD bases %d == %d"
          % (len(srows), REF_N_SMOOTH_PAIRS, n_skip_s, n_vdead,
             n_pd_s, REF_SMOOTH_PD),
          len(srows) == REF_N_SMOOTH_PAIRS
          and n_pd_s == REF_SMOOTH_PD, kill="KW")
    sdm = [r["maxDm2"] for r in srungs]
    n_sbrk = sum(1 for x in sdm if x > 1.0)
    print("\n  C3 -- the differentiated smooth contrast:")
    print("    static: max diag(E_s) > 1 on %d/%d smooth rungs "
          "(max D_-^2 = %.4f vs truth ladder max %.6f) -- %s"
          % (n_sbrk, len(srungs), max(sdm), dm2_max,
             "the smooth world BREAKS the damping sign statically"
             if n_sbrk else "the smooth world KEEPS the damping "
             "sign statically"))
    s_ok = [r for r in srows if "g1" in r]
    cross = [r for r in s_ok if 1.0 + r["mu_min"] < 0.0]
    ncross = [r for r in s_ok if 1.0 + r["mu_min"] >= 0.0]
    print("    step        1+mu_min   a_s        g1_s        "
          "g2_s        a+g1+g2")
    for r in s_ok:
        print("    h %3d->%3d  %+8.3f   %+.3e  %+.3e  %+.3e  "
              "%+.3e"
              % (r["ha"], r["hb"], 1.0 + r["mu_min"], r["a_h"],
                 r["g1"], r["g2"],
                 r["a_h"] + r["g1"] + r["g2"]))
    tg1n = sum(1 for r in neg if "g1" in r and r["g1"] < 0.0)
    tg2n = sum(1 for r in neg if "g1" in r and r["g2"] < 0.0)
    cg1n = sum(1 for r in cross if r["g1"] < 0.0)
    cg2n = sum(1 for r in cross if r["g2"] < 0.0)
    ng2n = sum(1 for r in ncross if r["g2"] < 0.0)
    print("    sign censuses: truth dangerous steps g1 < 0 on "
          "%d/%d, g2 < 0 on %d/%d | smooth CROSSING steps "
          "(%d): g1 < 0 on %d, g2 < 0 on %d | smooth "
          "non-crossing (%d): g2 < 0 on %d"
          % (tg1n, len([r for r in neg if "g1" in r]), tg2n,
             len([r for r in neg if "g1" in r]), len(cross),
             cg1n, cg2n, len(ncross), ng2n))
    if not cross:
        smooth_label = "DIFF-NOCROSS"
    elif cg2n * 3 >= 2 * len(cross):
        smooth_label = "DIFF-DAMPING-BREAKS"
    elif cg1n * 3 >= 2 * len(cross):
        smooth_label = "DIFF-GEOMETRY-BREAKS"
    else:
        smooth_label = "DIFF-MIXED"
    check("C3 typed: %s (crossing steps: g2 < 0 on %d/%d, g1 < "
          "0 on %d/%d; 2/3 rule)"
          % (smooth_label, cg2n, len(cross), cg1n, len(cross)),
          True)
    print("\n  C1 -- Epstein/scramble (kz %d, frame must die):"
          % CTRL_KZ)
    ok1 = True
    for nmc, kw in (("Epstein",
                     dict(comb=eps_comb(rrs[CTRL_KZ]),
                          rr_cache=rrs[CTRL_KZ])),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = rung_rec(CTRL_KZ, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
            continue
        extra = " | max diag(E) = %.3f (damping sign %s)" % (
            rc["maxDm2"], "BROKEN" if rc["maxDm2"] > 1.0
            else "kept")
        if "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES%s"
                  % (nmc, extra))
            continue
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        ok1 &= fired
        print("    %-8s: lam(out) %.3e | lam(C_J) %.3e -> fires "
              "via %s%s"
              % (nmc, rc["lamO"], rc["lamC"],
                 "EXTERIOR" if rc["lamO"] > 1.0 else
                 "WINDOW" if rc["lamC"] > 1.0 else "NOTHING",
                 extra))
    check("C1 CONTROLS FIRE (frame death or supercriticality)",
          ok1, kill="KW")

    return finish(dict(bridge=bridge, smooth=smooth_label,
                       c1=c1, c2=c2, mr1=mr1, mr2=mr2,
                       min_eta=min_eta,
                       minmarg=min(margins)))


def finish(lab):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("COMPBRIDGE-MEASURED / %(bridge)s / %(smooth)s"
                   % lab)
        print("\n  VERDICT: %s" % VERDICT)
        print("  (corr(GEO, DT1) %(c1)+.4f, corr(ATOM, DT2) "
              "%(c2)+.4f; ratio medians %(mr1).3f / %(mr2).3f; "
              "min eta %(min_eta).4f, min margin a+g1+g2 "
              "%(minmarg).3e)" % lab)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
