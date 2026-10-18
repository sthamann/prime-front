#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v901 -- PRIME.PORT.TANGENT.SCHUR.01 + PRIME.PORT.BFLOOR.01 + PRIME.PORT.SIGNFREE.NORMALIZATION.01: THE WALL IN TANGENT-SCHUR COORDINATES -- the exact source-only split of the wall update (with B PD: wall PD <=> n - q > 0, two scalars), the measured O(1) co-block floor lam_min(B) = 0.679 ladder-wide with the FIRST substantive tau-screen PASS (slope -0.247), the honest CERTFLOOR-DEAD negative (every classical certified bound stays negative everywhere), and the sign-free de-circularized normalization ell = det(S)^{1/8} (the circularity of c = tau/tau' REMOVED, positivity NOT gained), ONE module from three probes (26/26 + 24/24 + 18/18 checks, zero fails, verdicts TANGENTSCHUR-MEASURED (SAFEBLOCK(minB=0.6790) / GAP(min=0.0520, med=0.8875) / RESCUE-MIXED(B-dead=12, gap<=0=0 of 12) / OFFMODE-IN-B / FAILSEAT-COBLOCK(med-ovl=0.000)) + BFLOOR-MEASURED (BFLOOR-SCREEN-PASS(slope=-0.247) / CERTFLOOR-DEAD / BSPEC-STABLE / BSEAT-ORTHOGONAL(med=0.0053)) + SIGNFREE-MEASURED (DECIRC-ACHIEVED(ELL-B(det-core)) / TAMEST(ELL-B(det-core), spread=250)); discovery probes port_tangent_schur_probe.py (round 57), port_bfloor_uniformity_probe.py (round 58), port_signfree_normalization_probe.py (round 57), 2026-08-10, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~12 s).  (1) THE EXACT SPLIT (port_tangent_schur, 26/26): along the soft direction v_h of S_h (backward spectral data only, Householder frame) the normalized update M_h = X_h + U_h = S_{h+1}/tau_h (ward 8.5e-16) obeys, with the co-block B > 0: M > 0 <=> n - q > 0 where n = v^T M v and q = b^T B^{-1} b -- all identities warded (det M = (n-q) det B at 2.8e-14; n - q = 1/(v^T M^{-1} v) at 3.8e-14; the PD equivalence boolean-exact on 39/39 steps); the source-side expressions n*ell = v^T S' v and q*ell = (W^T S' v)^T (W^T S' W)^{-1} (W^T S' v) verified at 8.4e-14 -- every ingredient is comb linear algebra at rungs h/h+1 plus backward spectral data, NO tau_{h+1}, NO forward sign: the gap sign is OUTPUT.  (2) THE B-FLOOR AND THE TAU-SCREEN (port_bfloor_uniformity, 24/24; the round-58 headline): min eig(B_h) = 0.679 ladder-wide, family in [0.679, 84.0] -- O(1) while tau falls by factor 552; THE TAU-SCREEN METHODOLOGY (frozen bands: PASS |slope| <= 0.30, RELOCATION slope >= 0.70): OLS slope of log lam_min(B) vs log tau = -0.247 (corr -0.35, R^2 0.12) -- the FIRST screen pass with wall content: B-uniformity is a genuinely easier subgoal, and after the exact split the entire residual difficulty of the wall sits in the two scalars n, q; COORDINATE HONESTY printed a priori: B lives in X-coordinates (division by tau_h); the unnormalized co-block tracks tau with slope +0.753 -- the O(1) floor in X IS the statement that the raw co-block scales exactly like tau; the screen pass is substantive because the coordinate is purely backward-normalized and the PD question coordinate-invariant.  (3) THE HONEST NEGATIVE (CERTFLOOR-DEAD): ALL FOUR classical certified bounds (Gershgorin raw/scaled, Brauer-Cassini, Weyl backward+step) are negative on ALL 39 steps (best bound-maximum -88.2 against the true floor +0.679; cond(B) quartiles 171/221/278) -- a certifiable B-floor needs a damping coordinate (congruence, e.g. exact LDL pivot chains), not better classical inequalities; the floor remains MEASURED, not certified.  (4) THE FAILURE-SEAT ANATOMY (refutation registered): at ALL 12 v900 rank-1 failure points the surrogate CO-BLOCK B_s itself loses PD (minB_s -4.2..-364 against the true floor +0.679) -- the q-branch is EMPTY; the 2.5-percent off-mode restores the co-block LINEARLY (lift +67.7..+479.0 along the failure direction), and the frame-invariant failure seat is ORTHOGONAL to the current critical direction (<z, v>^2 med 0.0003, max 0.104) and nearly orthogonal to the forward direction (overlap quartiles 0.0011/0.0053/0.0113): the soft channel and the B channel are two separate axes.  (5) THE SIGN-FREE NORMALIZATION (port_signfree_normalization, 18/18; circularity removed, positivity NOT gained): v900's coefficient c = tau/tau' reads the SIGN of tau_{h+1} -- exactly what is to be propagated; the transcription Y = S/ell, Y' = g (Y + V) with g = ell/ell' is EXACT (ward 1e-10) and SOURCE-ONLY, and the positivity margin is COORDINATE-INVARIANT (lam_min(Y-rel V) == lam_min(X-rel U) at 8.4e-13, min 0.0315 = the eta floor): the de-circularization sits entirely in the bookkeeping of the coefficients, said honestly; of four frozen candidates the winner (tamest among the bounded) is ELL-B = det(S)^{1/8} (kappa = ell/tau bounded, ratio 2.79, g-spread 250; the exact factorization c = g x (kappa'/kappa) relocates the unknown sign wholly into the source-side factor); NOTHING here proves tau_h > 0 beyond the v897 census.  CONTROLS FIRE in all three probes: the smooth-mass world violates at rung level and its machinery exits (32/32, 37/37); Epstein and scramble fire (neg(A) 55/37); v900/v892/v893 reproduction wards green (product law, eta floor 0.0315, exact update, k95 = 1, rank-1 counter 12/39).  NO RH claim; no marker moves; the two scalars n, q are the isolated hard object -- positivity ladder-wide is measured (v897-certified base), never assumed.

PROVENANCE: discovery probes port_tangent_schur_probe.py (26/26,
TANGENTSCHUR-MEASURED, SPEC v1 frozen pre-run, round 57, Spec-SHA
8836de88...), port_bfloor_uniformity_probe.py (24/24,
BFLOOR-MEASURED, SPEC v1 frozen pre-run, round 58, Spec-SHA
9fde4cff...), port_signfree_normalization_probe.py (18/18,
SIGNFREE-MEASURED, SPEC v1 frozen pre-run, round 57, Spec-SHA
ee51c086...), all 2026-08-10, re-run identically at promotion.
ROUND-31 EMBEDDING CONVENTION: frozen sources embedded BYTE-EXACT,
executed verbatim in isolated namespaces; printed spec SHAs
reproduce; byte-equality ward vs experiments/tfpt-discovery/ inside
the pattern gates.  All probes consume the READ-ONLY deployed core
v563_paper2_readouts.py and reproduce the v892/v893/v900 laws as
wards.

FIREWALL: no zeros, no prime-table oracles (AST firewalls inside
the probes); the B-floor is a MEASUREMENT (CERTFLOOR-DEAD is the
registered honest negative); the de-circularization moves
bookkeeping, not positivity; NO RH claim.  Python-only per
GATE.WOLFRAM.02.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source port_tangent_schur_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
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
'''

# ------------- frozen probe source port_bfloor_uniformity_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
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
'''

# ------------- frozen probe source port_signfree_normalization_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""port_signfree_normalization_probe -- PRIME.PORT.SIGNFREE.NORMALIZATION.01
(EXPLORATION ONLY, experiments/; round 57: de-circularize the v900
normalization -- the exact core update in a SIGN-FREE normalization
whose update coefficients never read tau_{h+1} or any wall sign.
2026-08-10.)

THE QUESTION (frozen).  v900 (PRIME.PORT.NORMALIZED.CORE.01,
promoted from normalized_core_update_probe round 55) proved the
EXACT update X_{h+1} = c_h (X_h + U_h) for the normalized 8x8 core
X_h = S_h / tau_h, with c_h = tau_h / tau_{h+1}.  That coordinate
is CIRCULAR for any propagation theorem: tau_{h+1} = lambda_min(
A_{h+1}) is the wall scale whose SIGN is the very thing to be
propagated -- the update coefficient reads the unknown.  This
probe transcribes the SAME exact update into sign-free coordinates
    Y_h := S_h / ell(S_h),
    Y_{h+1} = g_h (Y_h + V_h),   g_h := ell(S_h)/ell(S_{h+1}),
    V_h := (S_{h+1} - S_h)/ell(S_h),
where ell is a SOURCE-ONLY functional: computable from the comb
linear algebra (Gram + block solve) WITHOUT any lambda_min / sign
query of the wall, so that g_h contains NO forward-sign input.
The algebraic transcription is an identity for ANY nonzero ell;
the CONTENT is measured: which candidate ell (i) stays positive on
the whole ladder, (ii) keeps the family {Y_h} bounded, (iii) keeps
the coefficients g_h tame -- the de-circularization criterion is
(i) + exactness + (ii), the winner is the tamest.

HONEST FRAME (frozen, said up front): the one-step positivity
margin is SCALING-INVARIANT -- Y_h = (tau_h/ell_h) X_h and V_h =
(tau_h/ell_h) U_h, so lambda_min(Y^{-1/2} V Y^{-1/2}) ==
lambda_min(X^{-1/2} U X^{-1/2}) EXACTLY (warded below).  The
sign-free coordinates change NOTHING about the measured margins;
what changes is the BOOKKEEPING: every coefficient of the update
becomes a source-side functional, so a future invariant-region /
propagation theorem needs no forward tau-sign input in its
dynamics.  Also honest: S_h = B_h - Xc_h R_h^{-1} Xc_h^T needs the
EXTERIOR block R_h invertible -- the already-certified-safe outer
block (v893: lambda_min(R) >= c_R tau with trendless c_R = 210;
negR = 0 on every truth rung, reproduced here); and positivity of
a trace/determinant functional of S is a MEASURED fact, far weaker
than PD -- it does not presuppose the wall.

THE FOUR FROZEN CANDIDATES (all source-only; chosen from what the
v900 objects actually expose):
  ELL-A  TRACE-CORE       ell = tr(S_h)/8       (Schur-core trace)
  ELL-B  DET-CORE         ell = det(S_h)^{1/8}  (slogdet route;
         DEAD on a rung if the determinant sign is not +1 -- the
         sign is RECORDED, never presumed)
  ELL-C  TRACE-OUTER      ell = tr(R_h)/(n-8)   (trace of the
         certified-safe exterior block)
  ELL-D  QUAD-MASS        ell = sum_j v_j       (total mass of the
         folded NEG-node quadrature that carries A = I - E; a
         positive readout of the constructional measure, >= 0 by
         construction)

FROZEN PROTOCOL (2026-08-10; machinery verbatim from
normalized_core_update_probe (round 55) with gram_anatomy EXTENDED
by two scalars: tr(R) and sum(v); pipeline physics bit-identical):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 reachable rungs, all chains complete, all
     tau finite; W2 >= 30 full-core rungs; W3 truth all-PSD +
     >= 20 consecutive full-core steps; W4 deepcore product law
     max |lamS*wcore/tau - 1| <= 1e-6; W5 inheritance floor min
     eta_core = 0.0315 (tol 5.001e-5); W6 the v900 exact update
     reproduced: max rel ||X' - c(X+U)|| <= 1e-10, and the c-range
     [0.051, 19.50] reproduced at rtol 2e-2.

 N1  THE CIRCULARITY STATEMENT + THE TRANSCRIPTION (per candidate,
     per consecutive full-core step): WARDS (kill -> WARD-BROKEN):
       N1.a TRANSCRIPTION: ||Y' - g (Y + V)||_F / ||Y'||_F <=
            TRANS_WARD = 1e-10 on every step (candidates with
            ell > 0 on both rungs of the step);
       N1.b SCALING CONSISTENCY: ||Y - (tau/ell) X||_F /
            ||Y||_F <= SCAL_WARD = 1e-12 per rung (tau is used
            ONLY inside this crosscheck ward, never in the
            construction);
       N1.c MARGIN INVARIANCE: |lambda_min(Y^{-1/2} V Y^{-1/2}) -
            lambda_min(X^{-1/2} U X^{-1/2})| <= INV_WARD = 1e-8
            per step (the honest-frame identity, warded).

 N2  THE MEASUREMENTS (per candidate; all typed, never kill):
     (i)  POSITIVITY OF ell: count of full-core truth rungs with
          ell <= 0 (DET-CORE: sign != +1) -> ELL-DEAD(count) if
          any;
     (ii) BOUNDEDNESS of {Y_h}: log-log slope of lambda_max(Y_h)
          vs h, band |slope| <= SLOPE_BND = 0.15 (v900's frozen
          band); Frobenius diameter printed ->
          BOUNDED(diam) / UNBOUNDED(slope);
     (iii) SOURCE-ONLY EXPOSURE: kappa_h = ell_h / tau_h printed
          (min/max/ratio).  With tau = ell/kappa the circular
          coefficient factors EXACTLY as
              c_h = tau_h/tau_{h+1} = g_h x (kappa_{h+1}/kappa_h)
          -- a source-only coefficient times a coordinate factor;
          boundedness of kappa (and of its step ratio) is the
          de-circularization content, printed per candidate;
          corr(log g, log c) printed;
     (iv) TAMENESS: the coefficient range [min g, max g] and the
          spread ratio max(g)/min(g) (requires all g > 0, else
          candidate is coefficient-signed -> recorded).
     TYPED WINNER (frozen rule): among candidates with zero
     ELL-DEAD rungs, exact transcription, and BOUNDED family, the
     winner is argmin of the g-spread ratio -> DECIRC-ACHIEVED(
     winner) with TAMEST(winner, ratio); if no candidate passes ->
     DECIRC-OPEN.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth wall
     neg(A) = 0 on every rung.  C1 SMOOTH world (masses
     2 e^{u/2} du, verbatim): neg(A) > 0 on >= 1 rung AND the
     winner's Y-machinery must EXIT on the smooth family: on >= 1
     smooth full-core rung, S not PSD or ell <= 0 or the rung is
     rung-level violated (the sign-free normalization must NOT
     hide the smooth failure).  C2 Epstein x^2+5y^2 comb and
     scramble (seed 1) at kz 9: neg(A) > 0 or chain death on
     BOTH; the winner ell status there is printed.

KILLS: K1 a W1-W3 pipeline ward breaks -> PIPELINE-BROKEN; K2 a
reproduction/identity/control ward (W4-W6, N1.a-c, C0-C2) breaks
-> WARD-BROKEN.  N2 outcomes are measurements, never kills.

VERDICT (frozen enum): SIGNFREE-MEASURED with typed sublabels
DECIRC-ACHIEVED(ell) / DECIRC-OPEN, TAMEST(ell, ratio), and the
four per-candidate labels; else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,4,...,16); H_LADDER_MAX = 900;
N_RUNGS_EXP = 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20;
REPRO_PROD_BAR = 1e-6; REPRO_ETA_MIN = 0.0315; ROUND_TOL =
5.001e-5; XUPD_WARD = 1e-10; C_RANGE_REF = [0.051, 19.50] (rtol
2e-2); TRANS_WARD = 1e-10; SCAL_WARD = 1e-12; INV_WARD = 1e-8;
SLOPE_BND = 0.15; CTRL_KZ = 9; scramble seed 1.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script (18/18 with the identical bars; no bar, rule or
enum was tuned to it -- the winner rule above predates the run)
measured the picture that is frozen here as context: ELL-A/ELL-B
(core trace/determinant-root) TRACK tau -- kappa = ell/tau
bounded within ratio ~3.1/~2.8, families BOUNDED (slopes -0.020 /
-0.035) -- but their coefficients inherit the full c-spread
(g-spread ~421/~250, corr(log g, log c) ~ +0.96); ELL-C/ELL-D
are O(1) source functionals with TAME coefficients (spread
~1.3/~2.1) that do NOT track tau, so their Y-families inherit
tau's decay (slopes ~ -3.1/-3.4, UNBOUNDED).  The TRADE-OFF
(bounded family <-> tame coefficients) is the honest first-class
finding of this probe; the de-circularization itself (kappa and
its step ratio bounded for the core functionals) holds for BOTH
tau-tracking candidates.  All wards are identities,
deployed-ledger reproductions (v900 printed numbers) or controls
frozen a priori.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1:
(i) window memoization per (kz, seed) (v900 verbatim); (ii)
candidate ELL-B uses np.linalg.slogdet(S) and is DEAD on a rung
iff sign != +1.0; (iii) slopes/OLS as in v900 (population
statistics); (iv) the winner ladder table prints Y-diagnostics
for the winner only, summaries for the rest; (v) g-spread uses
only steps where both rung ells are positive.

NO RH claim: the sign-free transcription is exact bookkeeping on
the deployed v563 window ladder; nothing here proves tau_h > 0
beyond the certified census (v897), and the propagation theorem
(bounded g + margin > -1 for all h) remains open.  No marker
moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; full wall operator +
fixed-core split + exact update machinery verbatim from
normalized_core_update_probe.py (PRIME.PORT.NORMALIZED.CORE.01,
round 55; promoted as v900); exterior-reserve reading from v893
(PRIME.PORT.RELFLAG.01, c_R = 210); certified base v884/v887/v897
-- declared inputs, not re-run.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/port_signfree_normalization_probe.py
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
REPRO_PROD_BAR = 1e-6          # W4 deepcore product law
REPRO_ETA_MIN = 0.0315         # W5 deepcore eta_core floor
ROUND_TOL = 5.001e-5
XUPD_WARD = 1e-10              # W6 v900 exact update
C_MIN_REF, C_MAX_REF = 0.051, 19.50    # v900 printed c range
C_RANGE_RTOL = 2e-2
TRANS_WARD = 1e-10             # N1.a transcription
SCAL_WARD = 1e-12              # N1.b scaling consistency
INV_WARD = 1e-8                # N1.c margin invariance
SLOPE_BND = 0.15               # N2 boundedness band (v900)
CTRL_KZ = 9
R_SING_TOL_REL = 1e-10
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")
CAND_NAMES = ("ELL-A(tr-core)", "ELL-B(det-core)",
              "ELL-C(tr-outer)", "ELL-D(quad-mass)")

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
    """SPEC concretization (i): pure memoization of the
    deterministic core.build_window (v900 verbatim)."""
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
    """The 42 reachable rungs (christoffel_zone_envelope verbatim)."""
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
    """PNT-mean masses 2 e^{u/2} du (lattice_parametrix B1)."""
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


def world_smooth(uu, mm, rr):
    return uu, smooth_masses(uu)


def gram_anatomy(kz, world_fn=None, scramble_seed=None, comb=None,
                 want_vec=False):
    """v900 verbatim wall + fixed-core split, EXTENDED with two
    source-only scalars: tr(R) and the total NEG-quadrature mass
    sum(v) (bit-identical physics otherwise)."""
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
    out["mneg"] = float(np.sum(vs))            # EXTENSION (ELL-D)
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
    out["trR"] = float(np.trace(R))            # EXTENSION (ELL-C)
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


def inv_sqrt(M):
    w, V = np.linalg.eigh(M)
    return V @ np.diag(w ** -0.5) @ V.T


def ols_line(x, y):
    """OLS y = a + b x; returns (a, b, R^2)."""
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


def ell_values(r):
    """The four frozen source-only candidates on one rung.
    Returns list of (value or None); None = ELL-DEAD channel
    (ELL-B determinant sign != +1)."""
    S = r["S"]
    out = []
    out.append(float(np.trace(S)) / 8.0)                 # ELL-A
    sg, ld = np.linalg.slogdet(S)
    out.append(math.exp(ld / 8.0) if sg == 1.0 else None)  # ELL-B
    out.append(r["trR"] / float(r["n"] - 8))             # ELL-C
    out.append(r["mneg"])                                # ELL-D
    return out


def main():
    section("PRIME.PORT.SIGNFREE.NORMALIZATION.01 -- the exact "
            "core update in sign-free coordinates (EXPLORATION "
            "ONLY)")
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
    check("W3a WARD truth all-PSD (A, R, S) on every full-core "
          "rung", ok_psd, kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})
    prods = np.array([r["lamS"] * r["wcore"] / r["tau"]
                      for r in full])
    prod_dev = float(np.max(np.abs(prods - 1.0)))
    check("W4 REPRODUCTION deepcore product law: max "
          "|lamS*wcore/tau - 1| = %.3e <= %.0e"
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
    etas_core = []
    for r1, r2 in steps:
        Wi = inv_sqrt(r1["S"])
        etas_core.append(float(np.linalg.eigvalsh(
            Wi @ r2["S"] @ Wi)[0]))
    eta_min = float(np.min(etas_core))
    check("W5 REPRODUCTION deepcore inheritance floor: min "
          "eta_core %.4f == %.4f (tol %.1e)"
          % (eta_min, REPRO_ETA_MIN, ROUND_TOL),
          abs(eta_min - REPRO_ETA_MIN) <= ROUND_TOL, kill="K2")
    # W6: the v900 exact update in the circular coordinates
    for r in full:
        r["X"] = r["S"] / r["tau"]
    xrec_dev = 0.0
    u_list = []
    for r1, r2 in steps:
        c = r1["tau"] / r2["tau"]
        U = (r2["S"] - r1["S"]) / r1["tau"]
        Xn = c * (r1["X"] + U)
        xr = (float(np.linalg.norm(Xn - r2["X"]))
              / max(float(np.linalg.norm(r2["X"])), 1e-300))
        xrec_dev = max(xrec_dev, xr)
        u_list.append((c, U))
    cs = np.array([c for (c, _U) in u_list])
    ok_crange = (abs(float(np.min(cs)) / C_MIN_REF - 1.0)
                 <= C_RANGE_RTOL
                 and abs(float(np.max(cs)) / C_MAX_REF - 1.0)
                 <= C_RANGE_RTOL)
    check("W6 REPRODUCTION v900 exact update: max rel ||X' - "
          "c(X+U)|| %.2e <= %.0e; c range [%.5f, %.5f] == "
          "[%.3f, %.2f] (rtol %.0e)"
          % (xrec_dev, XUPD_WARD, float(np.min(cs)),
             float(np.max(cs)), C_MIN_REF, C_MAX_REF,
             C_RANGE_RTOL),
          xrec_dev <= XUPD_WARD and ok_crange, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ N1
    section("N1 -- THE CIRCULARITY + THE SIGN-FREE TRANSCRIPTION")
    print("    v900 coefficient c_h = tau_h/tau_{h+1}: READS the "
          "sign of tau_{h+1} -- the unknown to be propagated.")
    print("    sign-free: Y = S/ell(S), Y' = g (Y + V), g = "
          "ell_h/ell_{h+1}, V = DS/ell_h -- NO forward-sign "
          "input.")
    ncand = len(CAND_NAMES)
    ELL = np.full((len(full), ncand), np.nan)
    dead = np.zeros(ncand, dtype=int)
    for i, r in enumerate(full):
        for k, v in enumerate(ell_values(r)):
            if v is None:
                dead[k] += 1
            else:
                ELL[i, k] = v
    idx_of = {id(r): i for i, r in enumerate(full)}
    print("\n    the candidate ladder (full-core rungs):")
    print("    kz   h     tau        " + "  ".join(
        "%-11s" % nm for nm in CAND_NAMES))
    for i, r in enumerate(full):
        print("    %-4d %-4d %.3e  " % (r["kz"], r["h"], r["tau"])
              + "  ".join(("%11.4e" % ELL[i, k])
                          if np.isfinite(ELL[i, k]) else
                          "%11s" % "DEAD"
                          for k in range(ncand)), flush=True)

    trans_dev = np.zeros(ncand)
    scal_dev = np.zeros(ncand)
    inv_dev = np.zeros(ncand)
    gco = [[] for _ in range(ncand)]
    mX_list = []
    for (c, U), (r1, r2) in zip(u_list, steps):
        Wi = inv_sqrt(r1["X"])
        mX = float(np.linalg.eigvalsh(Wi @ U @ Wi)[0])
        mX_list.append(mX)
        i1, i2 = idx_of[id(r1)], idx_of[id(r2)]
        DS = r2["S"] - r1["S"]
        for k in range(ncand):
            e1, e2 = ELL[i1, k], ELL[i2, k]
            if not (np.isfinite(e1) and np.isfinite(e2)
                    and e1 > 0.0 and e2 > 0.0):
                continue
            g = e1 / e2
            gco[k].append(g)
            Y1 = r1["S"] / e1
            Y2 = r2["S"] / e2
            V = DS / e1
            tr = (float(np.linalg.norm(Y2 - g * (Y1 + V)))
                  / max(float(np.linalg.norm(Y2)), 1e-300))
            trans_dev[k] = max(trans_dev[k], tr)
            sc = (float(np.linalg.norm(
                Y1 - (r1["tau"] / e1) * r1["X"]))
                / max(float(np.linalg.norm(Y1)), 1e-300))
            scal_dev[k] = max(scal_dev[k], sc)
            Wy = inv_sqrt(Y1)
            mY = float(np.linalg.eigvalsh(Wy @ V @ Wy)[0])
            inv_dev[k] = max(inv_dev[k], abs(mY - mX))
    check("N1.a TRANSCRIPTION WARD: max rel ||Y' - g(Y+V)|| = "
          "%.2e <= %.0e (all candidates, all live steps)"
          % (float(np.max(trans_dev)), TRANS_WARD),
          float(np.max(trans_dev)) <= TRANS_WARD, kill="K2")
    check("N1.b SCALING WARD: max rel ||Y - (tau/ell) X|| = %.2e "
          "<= %.0e (tau used ONLY in this crosscheck)"
          % (float(np.max(scal_dev)), SCAL_WARD),
          float(np.max(scal_dev)) <= SCAL_WARD, kill="K2")
    check("N1.c MARGIN-INVARIANCE WARD: max |lam_min(Y-rel V) - "
          "lam_min(X-rel U)| = %.2e <= %.0e (the margin is "
          "coordinate-invariant, said honestly)"
          % (float(np.max(inv_dev)), INV_WARD),
          float(np.max(inv_dev)) <= INV_WARD, kill="K2")

    # ------------------------------------------------------------ N2
    section("N2 -- MEASUREMENTS: positivity, boundedness, "
            "source-only exposure, tameness (per candidate)")
    hh = np.array([r["h"] for r in full], float)
    labels = []
    passing = []
    for k, nm in enumerate(CAND_NAMES):
        col = ELL[:, k]
        livemask = np.isfinite(col)
        n_nonpos = int(dead[k] + np.sum(col[livemask] <= 0.0))
        if n_nonpos > 0:
            lab = "%s: ELL-DEAD(%d)" % (nm, n_nonpos)
            labels.append(lab)
            print("    %s -- %d rungs with ell <= 0 or dead "
                  "determinant sign" % (lab, n_nonpos))
            continue
        lamYmax = np.array([r["lamSmax"] / col[i]
                            for i, r in enumerate(full)])
        _, slope, _ = ols_line(np.log(hh), np.log(lamYmax))
        vecs = [r["S"].flatten() / col[i]
                for i, r in enumerate(full)]
        diam = 0.0
        for i in range(len(vecs)):
            for j in range(i + 1, len(vecs)):
                diam = max(diam, float(np.linalg.norm(
                    vecs[i] - vecs[j])))
        kap = np.array([col[i] / r["tau"]
                        for i, r in enumerate(full)])
        g = np.array(gco[k])
        gpos = bool(np.all(g > 0.0))
        gratio = (float(np.max(g)) / float(np.min(g))
                  if gpos else float("inf"))
        cg = corr(np.log(g), np.log(cs)) if gpos else float("nan")
        bounded = abs(slope) <= SLOPE_BND
        lab = ("%s: %s" % (nm,
               "BOUNDED(diam=%.3g, slope=%+.3f)" % (diam, slope)
               if bounded else "UNBOUNDED(slope=%+.3f)" % slope))
        labels.append(lab)
        print("    %s" % lab)
        print("      ell range [%.3e, %.3e]; kappa = ell/tau in "
              "[%.3e, %.3e] (ratio %.3g)"
              % (float(np.min(col)), float(np.max(col)),
                 float(np.min(kap)), float(np.max(kap)),
                 float(np.max(kap)) / float(np.min(kap))))
        print("      g = ell/ell' range [%.4f, %.4f], spread "
              "ratio %.3g, all g > 0: %s; corr(log g, log c) = "
              "%+.4f"
              % (float(np.min(g)), float(np.max(g)), gratio,
                 gpos, cg))
        print("      EXACT factorization: c_h = g_h x "
              "(kappa_{h+1}/kappa_h); kappa-ratio range "
              "[%.4f, %.4f]"
              % (float(np.min(kap[1:] / kap[:-1])),
                 float(np.max(kap[1:] / kap[:-1]))))
        if (bounded and gpos
                and trans_dev[k] <= TRANS_WARD):
            passing.append((k, gratio))
    if passing:
        kwin, ratio_win = min(passing, key=lambda t: t[1])
        winner = CAND_NAMES[kwin]
        decirc = "DECIRC-ACHIEVED(%s)" % winner
        tamest = "TAMEST(%s, spread=%.3g)" % (winner, ratio_win)
    else:
        kwin = None
        winner = None
        decirc = "DECIRC-OPEN"
        tamest = "TAMEST(n/a)"
    check("N2.1 typed: %s / %s" % (decirc, tamest), True)
    if kwin is not None:
        print("\n    the WINNER ladder (Y = S/ell, %s):" % winner)
        print("    kz   h     ell        lamin(Y)   lamax(Y)   "
              "kappa=ell/tau")
        for i, r in enumerate(full):
            e = ELL[i, kwin]
            print("    %-4d %-4d %.4e %10.6f %10.4f  %.4e"
                  % (r["kz"], r["h"], e, r["lamS"] / e,
                     r["lamSmax"] / e, e / r["tau"]), flush=True)
        print("\n    the sign-free update statement (measured "
              "constants): Y' = g (Y + V) with g source-only in "
              "[%.4f, %.4f];"
          % (float(np.min(gco[kwin])), float(np.max(gco[kwin]))))
        print("    PD propagates along the ladder iff 1 + "
              "lam_min(Y^{-1/2} V Y^{-1/2}) > 0 at every step "
              "(min measured %.4f) -- IDENTICAL margins to v900 "
              "(N1.c), but NO coefficient reads tau_{h+1}."
              % (1.0 + float(np.min(mX_list))))

    # ------------------------------------------------------------ C
    section("C -- controls: smooth world + Epstein/scramble")
    check("C0.1 WARD truth wall holds on every rung (neg(A) = 0)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    print("  C1 -- the smooth-mass world (2 e^{u/2} du):")
    sm = []
    for kz in zones:
        r = gram_anatomy(kz, world_fn=world_smooth)
        if r is not None:
            sm.append(r)
    n_viol = sum(1 for r in sm if r["negA"] > 0)
    n_exit = 0
    n_smfull = 0
    for r in sm:
        if not r.get("core_ok"):
            continue
        n_smfull += 1
        vals = ell_values(r)
        ew = (vals[kwin] if kwin is not None else vals[0])
        s_bad = r["negS"] > 0
        e_bad = (ew is None) or (ew <= 0.0)
        if s_bad or e_bad or r["negA"] > 0:
            n_exit += 1
    print("    %d rungs built; neg(A) > 0 on %d; winner "
          "Y-machinery exits (S not PSD / ell <= 0 / rung "
          "violated) on %d of %d full-core smooth rungs"
          % (len(sm), n_viol, n_exit, n_smfull))
    check("C1.1 WARD smooth violates at rung level (neg(A) > 0 "
          "somewhere)", n_viol > 0, kill="K2")
    check("C1.2 WARD winner Y-machinery exits on >= 1 smooth "
          "full-core rung (the sign-free normalization must not "
          "hide the failure)", n_exit >= 1, kill="K2")
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
            print("    %-9s: chain dies -> fires (frame death)"
                  % name)
            continue
        f = r["negA"] > 0
        fired_all &= f
        stat = "n/a"
        if r.get("core_ok"):
            vals = ell_values(r)
            ew = (vals[kwin] if kwin is not None else vals[0])
            stat = ("ell=%.3e negS=%d"
                    % (ew if ew is not None else float("nan"),
                       r["negS"]))
        print("    %-9s: tau %+.3e  neg(A) %d  [winner status: "
              "%s] -> %s"
              % (name, r["tau"], r["negA"], stat,
                 "FIRES" if f else "SILENT"), flush=True)
    check("C2.1 WARD both controls fire (neg(A) > 0 or chain "
          "death)", fired_all, kill="K2")

    return finish(dict(decirc=decirc, tamest=tamest,
                       labels=labels))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("SIGNFREE-MEASURED / %(decirc)s / %(tamest)s"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
        for lab in labels.get("labels", []):
            print("    " + lab)
    print("""
  HONEST FRAME (as frozen): the sign-free transcription is exact
  bookkeeping; the positivity margins are coordinate-invariant
  (N1.c) and NOTHING here proves tau_h > 0 beyond the certified
  census (v897).  The content is the measured de-circularization:
  which source-only ell keeps ell > 0, the family bounded and the
  coefficients tame -- so that a propagation theorem needs no
  forward tau-sign input in its dynamics.  NO RH claim.  No
  marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''


# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('port_tangent_schur_probe', _SRC_0, 26, (), 'TANGENTSCHUR-MEASURED', 0),
    ('port_bfloor_uniformity_probe', _SRC_1, 24, (), 'BFLOOR-MEASURED', 0),
    ('port_signfree_normalization_probe', _SRC_2, 18, (), 'SIGNFREE-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v901 -- PRIME.PORT.TANGENT.SCHUR.01 + PRIME.PORT.BFLOOR.01 + PRIME.PORT.SIGNFREE.NORMALIZATION.01: the wall in tangent-Schur coordinates -- exact split (wall PD <=> B PD AND n > q, source-only), B-floor 0.679 ladder-wide with tau-screen PASS (slope -0.247), CERTFLOOR-DEAD honest negative, and the sign-free de-circularized normalization ell = det(S)^{1/8} (circularity removed, positivity NOT gained)')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v901: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the residual difficulty of the wall sits in the two scalars n, q; the B-floor is measured, not certified; no positivity was gained anywhere')
    print("[%s] v901 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
