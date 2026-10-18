#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""anthropic_moment_inertia_probe -- PRIME.PORT.ANTHROPIC.MOMENTS.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the SECOND Anthropic-port probe -- higher
moments on the congruent core forms.  CLXIII measured that the
TWO-moment (rank-trace) criterion on the source-only congruence
certifies 0/39: the spread deficit 7 f0 - t0^2 eats the drive.
This probe asks the canonical next question: what is the MINIMAL
moment order r such that m_0..m_{2r}, m_k = tr(A^k) of the same
congruent forms, certifies n_+ = 8 (i.e. M > 0) through the
sharpest one-sided moment bound?  2026-08-11.)

THE MOMENT BOUND (frozen method, documented exactly).  Let mu =
sum_i delta_{lambda_i} be the spectral counting measure of the
8x8 congruent form A(u) (mass 8, unit atoms).  Given the power
moments m_0..m_{2r} only, the sharp upper bound on mu((-inf, 0])
over ALL nonnegative measures with these moments is the
Chebyshev-Markov-Stieltjes bound at t = 0, computed by the
canonical (principal) representation with a fixed node at 0:
  (i)  solve for the monic degree-r polynomial phi with
       mu[x phi(x) x^j] = 0 for j = 0..r-1 (an r x r linear
       system in the moments m_1..m_{2r});
  (ii) nodes = {0} union roots(phi); weights w_i from moment
       matching sum w_i x_i^k = m_k, k = 0..r (Vandermonde);
       the rule is then exact through degree 2r by construction;
  (iii) UB_r = sum of w_i over nodes x_i <= 0.
INTEGRALITY: mu is an integer counting measure, so UB_r < 1
forces n_{<=0} = 0, i.e. n_+ = 8, i.e. A(u) > 0, i.e. (Sylvester)
M > 0.  DEGENERATE / INVALID GUARDS (frozen, conservative): if
the linear system is singular, a root is materially complex, a
weight is below -W_TOL, or the moment-matching residual exceeds
RES_TOL relative, the construction REFUSES at this (step, r, u)
-- no certificate is ever granted by a failed construction; at
r = 1 the closed form UB_1 = m_0 - m_1^2/m_2 (m_1 > 0) is used,
which is EXACTLY the CLXIII rank-trace criterion (8 - UB_1 =
(tr A)^2/||A||_F^2), the built-in consistency tie.

THE EXACT BACKSTOP (NEWTON-STURM, typed honestly).  From the
EXACT rational congruent form A0 (the CLXIII source-only
congruence, Fraction entries), the characteristic polynomial is
computed exactly (Faddeev-LeVerrier == Newton's identities on
m_1..m_8), made squarefree, and the Sturm chain counts the
distinct roots in (-inf, 0]: count 0 AND p(0) != 0 certifies
M > 0 EXACTLY.  Typed declaration: this is the r = 4 information
class PLUS the fixed-dimension char-poly structure, and it is
the exact-LDL benchmark class IN DISGUISE (deciding PD of M was
always available to the v897 certificate class directly); its
route value here is the moment REPRESENTATION -- the same
decision is reached reading ONLY the eight power sums
m_1..m_8 of a source-only congruent form, and the anatomy block
prints what those moments read on the prime side.  It is
reported as a benchmark, not as new certification power.

FORMS (frozen): per step the two CLXIII congruent forms,
  S1 (whitened; TARGET EIGENDATA DECLARED, identity control):
     A0 = [[n, c*],[c, I_7]], c = B^{-1/2} b (float);
  S2 (source-only): A0 = [[n, chat*],[chat, Chat]], chat =
     Linv b, Chat = Linv B Linv^T, Linv from the float Cholesky
     of D = (1/2) P_G + c_dom I (CLXIII pipeline verbatim; float
     for the moment scans, exact Fractions for NEWTON-STURM).
Scale family A(u) = diag(sqrt(u), I) A0 diag(sqrt(u), I); u only
re-weights the head, inertia is u-invariant (u > 0).  FROZEN u
GRID per (step, form): base u0 = the rank-trace vertex
(S1: 7(n - q)/(6 n^2) if n > q else u_h; S2: drive/(6 n^2) if
drive > 0 else t0/(7 n)); grid u0 * 2^j, j = -8..8 (17 points);
CERT at (step, form, r) iff UB_r(u) < 1 - CERT_EPS for some grid
u (float level, declared; the exact object is the backstop).

FROZEN PROTOCOL (pipeline verbatim from CLXIII =
anthropic_ranktrace_core_probe = CXLIV chain):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1-W3 ladder wards (42 rungs, >= 30 full-core,
     truth all-PSD, >= 20 steps); W4 P2/P3 ledger reproduction;
     W5 CXLIV V4 reproduction (P_G PD, half-dominance >= 37);
     W6 machine wards (exact LDL / solver / triangular inverse).

 M   THE MOMENT MACHINE WARDS (kill -> WARD-BROKEN):
     M1 VALIDITY BATTERY: on NW_RAND = 500 seeded random
        symmetric 8x8 matrices (frozen seed, declared ward-RNG)
        plus NW_ARROW = 100 seeded degenerate arrow matrices
        (the S1 shape, Hankel-singular by construction), every
        non-refusing UB_r (r = 1..4) must satisfy UB_r >=
        n_{<=0}(A) - VAL_TOL -- the bound may never undercount
        the nonpositive spectrum;
     M2 R1-TIE: on the battery, the r = 1 bound ties the closed
        form m_0 - m_1^2/m_2 to R1_TOL relative (m_1 > 0 cases);
     M3 STURM WARD: NEWTON-STURM (float-coefficient version on
        the battery) agrees with the eigh sign count on every
        battery matrix; the EXACT version agrees with float eigh
        PD on every truth step (39/39).

 B   MINIMAL-ORDER CENSUS (the point; typed, never kill): per
     step and form, r_min = smallest r in {1,2,3,4} with CERT;
     the full table printed (UB_r best-over-grid per r); the
     histogram of r_min per form; stability across the ladder
     (r_min vs h); typed RMIN-S1(hist) / RMIN-S2(hist) with
     NONE(k) counting steps where even r = 4 fails at float
     level.  NEWTON-STURM exact census on S2 printed next to it
     (the benchmark: expected 39/39 == truth PD).

 A   MOMENT ANATOMY (typed): at the three frozen representative
     steps (first / median / last by h), print m_1..m_8 of the
     S2 form at u0, the block decomposition per k (head u^k n^k;
     coupling 2 u qhat-type terms via chat* Chat^{k-2} chat, j =
     0..k-2; co-block tr(Chat^k)), and the honest prime-side
     reading: every entry of (n, b, B) is a windowed comb
     functional (P2 T5 source-only expressions), so tr(A^k) is a
     polynomial in k-fold products of comb lag correlations --
     the reduced object the moment route actually reads; the
     wiring to the head/tail cartography (CXLVII) is NAMED as
     the follow-up, not computed here.

 G   ROUTE-GATE TYPING (frozen): r = 1 IS the Anthropic
     two-moment class (CLXIII measured 0/39 there); r >= 2 is
     genuinely more information (tr A^3, tr A^4 read 3- and
     4-fold lag correlations that no pair-correlation statistic
     contains); the minimal certifying r, if any, LOCATES the
     wall's information demand between the two-moment no-go
     class and the full-spectrum class (r = 4 + integrality ==
     benchmark).  Typed ROUTE-GATE(reading from the census).

 D   DEEP BLIND HOLDOUT (typed, never kill): the CLXIII deep
     machinery verbatim (4e6 table, byte-exact overlap ward +
     kappa guard, 28 new rungs, 27 steps); r_min census on both
     forms + NEWTON-STURM exact at depth; is r_min stable
     out-of-sample?  Typed DEEP-SCORED(...).

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) =
     0; C1 smooth fires; C2 Epstein + scramble at kz 9 fire; C3
     smooth-B0 refusal >= REFUSE_MIN; C4 scramble core disclosed;
     C5 cosh injection fires (CLXII rule, smallest amplitude).
     CRITERION-LEVEL (typed + kill): on smooth and cosh relaxed
     control steps, SOUNDNESS (kill): no (form, r, u) certificate
     may fire where the core M is not float eigh-PD, and the
     exact NEWTON-STURM must agree with the float eigh PD
     boolean; typed census per world (certified counts vs truly
     PD cores).

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
machine / validity / soundness / control wards (W4-W6, M1-M3,
C0-C5, soundness) -> WARD-BROKEN.  B/A/G/D censuses are typed
measurements, never kills.

VERDICT (frozen enum): ANTHROMOMENT-MEASURED with typed
sublabels MACHINE-WARDED(battery n/n, r1-tie, sturm),
RMIN-S1(hist), RMIN-S2(hist [, NONE(k)]),
NEWTONSTURM-BENCH(n/39 exact, class declared),
ANATOMY(3 steps), ROUTE-GATE(reading),
DEEP-SCORED(...), SCREEN(...), CONTROLS(...); else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2); PG_TOL
= 1e-12; DOMHALF_MIN = 37; BIS_ITERS = 40; R_MAX = 4; U_GRID_J =
8 (2^j, j = -8..8); CERT_EPS = 1e-6; RES_TOL = 1e-8; W_TOL =
1e-10; IMAG_TOL = 1e-8; VAL_TOL = 1e-6; R1_TOL = 1e-8; NW_RAND =
500; NW_ARROW = 100; WARD_SEED = 20260811 (declared ward-RNG);
REFUSE_MIN = 30; INJ_LADDER = (0.01, 0.1, 1.0); INJ_DELTA = 0.05;
INJ_GAMMA0 = 10.0; TAB_EXT = 4_000_000; H_HOLD = (128, 2900);
KZ_SCAN_MAX = 400; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; CTRL_KZ
= 9; scramble seed 1; representative steps = first/median/last by
h.  Runtime cap declared: 15 min.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign, no spectral data of the TARGET B or M in any S2
CONSTRUCTION (CLXIII declarations inherited verbatim: T0 from D =
(1/2) P_G + c_dom I, direction content source-only, c_dom a
certified scalar); the moment machine reads ONLY traces of
powers -- polynomial source-only functionals; polynomial root
finding acts on moment-derived companion matrices, never on the
target; S1's B^{-1/2} is DECLARED target eigendata (identity
control); float eigensolves of M appear only in soundness wards
and printed context; the ward battery is synthetic (seeded RNG,
declared) and never touches ladder data.

NO-GO COMPLIANCE (frozen): no rank-1 approximation; no plain
Herglotz certificate; no fit where an identity is claimed; the
exact-rational classes per the CXLIV mandate; the Anthropic
two-moment no-go is engaged head-on in the G block.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): one smoke run
of this script (29/29 with the identical bars; NO bar, band,
count, rule or enum was moved after it; the only post-smoke edit
is this disclosure block itself) measured: pipeline + P2/P3 +
CXLIV reproduction green (min lam_min(B) 0.6790, gap
0.0520/0.8875, P_G PD + half-dominance 39/39).  M: validity
battery 2400/2400 non-refusing bounds valid, 0 refusals; r = 1
closed-form tie exact (dev 0.0); float NEWTON-STURM == eigh on
the battery subsample.  B THE CENSUS: S1 (whitened identity
control) certifies at r = 1 on 39/39 (UB_1 range 0.07..0.84;
UB_2 already ~1e-2, UB_3/UB_4 ~ -0.000 -- the exact-quadrature
degenerate branch); S2 (source-only) NEVER certifies below r =
4 (UB_1 4.2..5.8, UB_2 2.1..3.5, UB_3 1.3..2.3) and at r = 4
certifies 7/39 (kz 13/33/27/25/26/55/24; UB_4 range 0.83..1.60
ladder-wide -- the moment relaxation lands NEAR the bar 1
everywhere but crosses it on only 7 steps); r_min-vs-log-h
slope +0.000 (all certifying steps at r = 4, constant -- R^2
vacuous); NEWTON-STURM exact 39/39 (== truth PD, benchmark
class as declared).  Tau-screen of the 7 margins PASS(+0.120,
R^2 0.103).  A: at all three representative steps the co-block
tr(Chat^k) dominates every moment (head and coupling 1..3
orders below) -- the moment budget is spent on the congruence
slack spectrum, consistent with the CLXIII loss anatomy.  G:
r = 1 certifies 0/39 (the Anthropic class, CLXIII confirmed);
the wall's demand sits at r = 4 near-threshold under this
congruence.  D: 28 new rungs, 27 steps blind; S1 r = 1 on
27/27; S2 r = 4 on 5/27 (NONE 22); NEWTON-STURM 27/27; the
r_min profile is stable out-of-sample.  Controls: smooth fires
42/42, Epstein neg(A) 55, scramble neg(A) 37 (core dead -> C4
disclosed skip), cosh A = 0.01 fires 39/42; C3 refusal 35/35;
criterion-level: smooth cert 0/32 (0 PD cores), cosh cert 2/39
with EXACTLY the 2 truly PD cores (sound; the certificates fire
only where the injected world's 8-fold core is genuinely PD);
NEWTON-STURM control mismatches 0.  Runtime 116.7 s (cap
holds).  Fail-first preserved: nothing was weakened; enums,
bars and rules are exactly as frozen above.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as
P2/CXLIV; (iii) P_G / D / Linv exactly as CLXIII; (iv) moments by
float matrix powers (k <= 8); (v) phi system solved by
numpy.linalg.solve; roots by numpy.roots; refusal on any guard
breach; degenerate fallback = reduce r by one down to the r = 1
closed form (each fallback level re-guarded); (vi) NEWTON-STURM:
exact Faddeev-LeVerrier char poly, squarefree via Fraction-poly
gcd, Sturm chain by polynomial remainders, count in (-inf, 0] =
V(-inf) - V(0), certify iff count 0 and p(0) != 0; (vii) deep
frame/gram = deep_blind_holdout_probe verbatim; (viii) strict
inequalities in all exact decisions.

NO RH claim: a minimal-order census is a SURFACE measurement
about the computed step matrices of the deployed ladder; the
NEWTON-STURM 39/39 (expected) is the benchmark class restated,
not a new theorem; nothing here proves n > q uniformity in h,
the pipeline enclosure, or any tail statement.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control and the frozen-seed ward battery; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
P_G + congruence machinery verbatim from
anthropic_ranktrace_core_probe (CLXIII) = bfloor_pg_dominance
(CXLIV) chain; deep machinery from deep_blind_holdout_probe;
cosh signature via CLXII; Chebyshev-Markov-Stieltjes canonical
representations are the declared classical method; the Anthropic
zeta-2/3 framing is the declared external method source.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/anthropic_moment_inertia_probe.py
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
DOMHALF_MIN = 37
BIS_ITERS = 40
R_MAX = 4
U_GRID_J = 8
CERT_EPS = 1e-6
RES_TOL = 1e-8
W_TOL = 1e-10
IMAG_TOL = 1e-8
VAL_TOL = 1e-6
R1_TOL = 1e-8
NW_RAND = 500
NW_ARROW = 100
WARD_SEED = 20260811
REFUSE_MIN = 30
INJ_LADDER = (0.01, 0.1, 1.0)
INJ_DELTA = 0.05
INJ_GAMMA0 = 10.0
TAB_EXT = 4_000_000
H_HOLD = (128, 2900)
KZ_SCAN_MAX = 400
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


# --------------- pipeline, verbatim (CLXIII / CXLIV chain)
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
                 keep_chain=False, lag_fn=None):
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm, rr)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    lags = rr["c_ar"] + np.asarray(c_at, float)
    if lag_fn is not None:
        lags = lags + lag_fn(rr)
    d = grid_density(lags)
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


# ------------------------- exact-rational machinery (CLXIII)
def mat_fr(M):
    n = M.shape[0]
    return [[Fraction(float(M[i, j])) for j in range(n)]
            for i in range(n)]


def pd_exact(Afr, shift=Fraction(0)):
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


def tri_inv_fr(Lflt):
    n = Lflt.shape[0]
    Lfr = mat_fr(Lflt)
    for i in range(n):
        if Lfr[i][i] <= 0:
            return None
    Linv = [[Fraction(0)] * n for _ in range(n)]
    for j in range(n):
        x = [Fraction(0)] * n
        for i in range(n):
            s = Fraction(1) if i == j else Fraction(0)
            for k in range(i):
                s -= Lfr[i][k] * x[k]
            x[i] = s / Lfr[i][i]
        for i in range(n):
            Linv[i][j] = x[i]
    return Linv


def build_pg(w):
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


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def make_step(r1, r2):
    wS, VS = np.linalg.eigh(r1["S"])
    Q = householder_frame(VS[:, 0])
    Mt = Q.T @ (r2["S"] / r1["tau"]) @ Q
    Mt = 0.5 * (Mt + Mt.T)
    return dict(r1=r1, r2=r2, Q=Q, Mt=Mt, nsc=float(Mt[0, 0]),
                b=Mt[1:, 0].copy(), B=Mt[1:, 1:].copy(),
                tau=r1["tau"])


def s2_congruence(w):
    """The CLXIII source-only congruence: returns (L, Linv_fr,
    cdom) or None with a refusal seat.  Float L; exact Linv."""
    n7 = 7
    PG = w.get("PG")
    if PG is None:
        return None, "no P_G"
    Bfr = mat_fr(w["B"])
    Pfr = mat_fr(0.5 * PG)
    Kfr = [[Bfr[i][j] - Pfr[i][j] for j in range(n7)]
           for i in range(n7)]
    ok0, _ = pd_exact(Kfr)
    if not ok0:
        return None, "DOM-FAIL"
    hi = min(Kfr[k][k] for k in range(n7))
    cdom = cert_floor_exact(Kfr, Fraction(0), hi)
    if cdom is None or cdom <= 0:
        return None, "c_dom refused"
    Dflt = 0.5 * PG + float(cdom) * np.eye(n7)
    try:
        Lc = np.linalg.cholesky(Dflt)
    except np.linalg.LinAlgError:
        return None, "chol refused"
    return (Lc, cdom), ""


def forms_of(w):
    """Float congruent forms per step: dict name -> (A0, u0).
    S1 whitened (identity control), S2 source-only."""
    out = {}
    B = w["B"]
    b = w["b"]
    nsc = w["nsc"]
    h2 = w["r2"]["h"]
    wB, VB = np.linalg.eigh(B)
    if float(wB[0]) > 0.0 and nsc > 0.0:
        c = (VB @ np.diag(wB ** -0.5) @ VB.T) @ b
        q = float(c @ c)
        A0 = np.zeros((8, 8))
        A0[0, 0] = nsc
        A0[0, 1:] = c
        A0[1:, 0] = c
        A0[1:, 1:] = np.eye(7)
        u0 = (7.0 * (nsc - q) / (6.0 * nsc ** 2) if nsc > q
              else 7.0 * mu1_of(h2) / (6.0 * nsc ** 2))
        out["S1"] = (A0, u0)
    cg, seat = s2_congruence(w)
    if cg is not None:
        Lc, cdom = cg
        Li = np.linalg.solve(Lc, np.eye(7))
        Chat = Li @ B @ Li.T
        chat = Li @ b
        A0 = np.zeros((8, 8))
        A0[0, 0] = nsc
        A0[0, 1:] = chat
        A0[1:, 0] = chat
        A0[1:, 1:] = 0.5 * (Chat + Chat.T)
        t0f = float(np.trace(Chat))
        qhf = float(chat @ chat)
        drive = nsc * t0f - 7.0 * qhf
        u0 = (drive / (6.0 * nsc ** 2) if drive > 0 and nsc > 0
              else t0f / (7.0 * max(nsc, 1e-300)))
        if u0 > 0:
            out["S2"] = (A0, u0)
        w["s2seat"] = "" if u0 > 0 else "u0 <= 0"
        w["cg"] = (Lc, cdom)
    else:
        w["s2seat"] = seat
    return out


def scaled(A0, u):
    A = A0.copy()
    A[0, 0] = u * A0[0, 0]
    su = math.sqrt(u)
    A[0, 1:] = su * A0[0, 1:]
    A[1:, 0] = su * A0[1:, 0]
    return A


def power_moments(A, kmax):
    ms = [float(A.shape[0])]
    P = np.eye(A.shape[0])
    for _k in range(kmax):
        P = P @ A
        ms.append(float(np.trace(P)))
    return ms


def cms_ub_once(ms, r):
    """One CMS/canonical-representation attempt at order r.
    Returns UB float or None (refusal)."""
    if r == 1:
        m0, m1, m2 = ms[0], ms[1], ms[2]
        if m2 <= 0:
            return None
        if m1 > 0:
            return m0 - m1 * m1 / m2
        return m0
    # solve for monic phi of degree r: sum_k c_k m_{k+j+1} = 0
    Asys = np.empty((r, r))
    rhs = np.empty(r)
    for j in range(r):
        for k in range(r):
            Asys[j, k] = ms[k + j + 1]
        rhs[j] = -ms[r + j + 1]
    try:
        cvec = np.linalg.solve(Asys, rhs)
    except np.linalg.LinAlgError:
        return None
    coeffs = np.concatenate([[1.0], cvec[::-1]])   # monic, np.roots
    rts = np.roots(coeffs)
    scale = max(1.0, float(np.max(np.abs(rts))))
    if float(np.max(np.abs(rts.imag))) > IMAG_TOL * scale:
        return None
    nodes = np.concatenate([[0.0], rts.real])
    V = np.vander(nodes, r + 1, increasing=True).T
    try:
        wts = np.linalg.solve(V, np.array(ms[:r + 1]))
    except np.linalg.LinAlgError:
        return None
    if float(np.min(wts)) < -W_TOL * max(1.0, ms[0]):
        return None
    # residual through degree 2r
    mscale = max(1.0, max(abs(x) for x in ms))
    for k in range(2 * r + 1):
        resid = abs(float(np.sum(wts * nodes ** k)) - ms[k])
        if resid > RES_TOL * mscale * max(
                1.0, float(np.max(np.abs(nodes))) ** k):
            return None
    return float(np.sum(wts[nodes <= 0.0]))


def cms_ub(ms, r):
    """Frozen fallback chain: try order r, then r-1, ... 1."""
    for rr in range(r, 0, -1):
        ub = cms_ub_once(ms, rr)
        if ub is not None:
            return ub
    return None


def rmin_census(A0, u0):
    """Minimal certifying r over the frozen u grid.  Returns
    (rmin or None, best UB per r)."""
    us = [u0 * 2.0 ** j for j in range(-U_GRID_J, U_GRID_J + 1)]
    best = {r: float("inf") for r in range(1, R_MAX + 1)}
    for u in us:
        if not (u > 0 and np.isfinite(u)):
            continue
        A = scaled(A0, u)
        ms = power_moments(A, 2 * R_MAX)
        for r in range(1, R_MAX + 1):
            ub = cms_ub(ms[:2 * r + 1], r)
            if ub is not None and ub < best[r]:
                best[r] = ub
    rmin = None
    for r in range(1, R_MAX + 1):
        if best[r] < 1.0 - CERT_EPS:
            rmin = r
            break
    return rmin, best


# --------------------- NEWTON-STURM (exact + float versions)
def charpoly_fr(Afr):
    """Exact Faddeev-LeVerrier char poly coefficients
    [1, c1, ..., cn] of the Fraction matrix (p(x) = x^n + c1
    x^{n-1} + ... + cn)."""
    n = len(Afr)
    Mk = [[Fraction(1) if i == j else Fraction(0)
           for j in range(n)] for i in range(n)]
    cs = [Fraction(1)]
    for k in range(1, n + 1):
        Mk = [[sum(Afr[i][t] * Mk[t][j] for t in range(n))
               for j in range(n)] for i in range(n)]
        tr = sum(Mk[i][i] for i in range(n))
        ck = -tr / k
        cs.append(ck)
        for i in range(n):
            Mk[i][i] += ck
    return cs


def poly_trim(p):
    while len(p) > 1 and p[0] == 0:
        p = p[1:]
    return p


def poly_deriv(p):
    n = len(p) - 1
    return [p[i] * (n - i) for i in range(n)] or [Fraction(0)]


def poly_rem(a, b):
    a = list(a)
    b = poly_trim(list(b))
    if len(b) == 1:
        return [Fraction(0)]
    while len(a) >= len(b):
        if a[0] == 0:
            a = a[1:]
            continue
        f = a[0] / b[0]
        for i in range(len(b)):
            a[i] = a[i] - f * b[i]
        a = a[1:]
    a = poly_trim(a) if a else [Fraction(0)]
    return a


def poly_gcd(a, b):
    a = poly_trim(list(a))
    b = poly_trim(list(b))
    while not (len(b) == 1 and b[0] == 0):
        a, b = b, poly_rem(a, b)
        b = poly_trim(b)
    return a


def sturm_nonpos_count(p):
    """Distinct real roots of p in (-inf, 0] via Sturm.
    p as Fraction coefficient list, leading first."""
    p = poly_trim(list(p))
    g = poly_gcd(p, poly_deriv(p))
    if len(g) > 1:
        # squarefree part
        q, rem = [], list(p)
        # exact polynomial division p / g
        num = list(p)
        den = g
        quo = []
        while len(num) >= len(den) and not (
                len(num) == 1 and num[0] == 0):
            f = num[0] / den[0]
            quo.append(f)
            for i in range(len(den)):
                num[i] = num[i] - f * den[i]
            num = num[1:]
            if not num:
                break
        p = poly_trim(quo) if quo else [Fraction(1)]
        del q, rem
    chain = [p, poly_trim(poly_deriv(p))]
    while not (len(chain[-1]) == 1 and chain[-1][0] == 0):
        r = poly_rem(chain[-2], chain[-1])
        r = poly_trim([-c for c in r])
        chain.append(r)
    chain = chain[:-1]

    def sgn_at_zero(q):
        return (1 if q[-1] > 0 else -1) if q[-1] != 0 else 0

    def sgn_at_minf(q):
        d = len(q) - 1
        s = 1 if q[0] > 0 else -1
        return s if d % 2 == 0 else -s

    def variations(sgns):
        sgns = [s for s in sgns if s != 0]
        return sum(1 for a, b in zip(sgns, sgns[1:]) if a != b)

    v_minf = variations([sgn_at_minf(q) for q in chain])
    v_zero = variations([sgn_at_zero(q) for q in chain])
    return v_minf - v_zero


def newton_sturm_pd_exact(Afr):
    """Exact: True iff the symmetric Fraction matrix is PD."""
    cs = charpoly_fr(Afr)
    if cs[-1] == 0:
        return False              # eigenvalue 0
    return sturm_nonpos_count(cs) == 0


def newton_sturm_pd_float(A):
    """Float-coefficient version for the ward battery."""
    Afr = mat_fr(A)
    return newton_sturm_pd_exact(Afr)


def s2_exact_form(w):
    """Exact Fraction A0 of the S2 congruence (for the exact
    backstop).  None with seat on refusal."""
    cg = w.get("cg")
    if cg is None:
        return None
    Lc, _cdom = cg
    Linv = tri_inv_fr(Lc)
    if Linv is None:
        return None
    n7 = 7
    Bfr = mat_fr(w["B"])
    bfr = [Fraction(float(x)) for x in w["b"]]
    BL = [[sum(Bfr[i][k] * Linv[j][k] for k in range(n7))
           for j in range(n7)] for i in range(n7)]
    Chat = [[sum(Linv[i][k] * BL[k][j] for k in range(n7))
             for j in range(n7)] for i in range(n7)]
    chat = [sum(Linv[i][k] * bfr[k] for k in range(n7))
            for i in range(n7)]
    A0 = [[Fraction(0)] * 8 for _ in range(8)]
    A0[0][0] = Fraction(w["nsc"])
    for i in range(n7):
        A0[0][i + 1] = chat[i]
        A0[i + 1][0] = chat[i]
        for j in range(n7):
            A0[i + 1][j + 1] = (Chat[i][j] + Chat[j][i]) / 2
    return A0


# --------------- deep machinery (deep_blind_holdout verbatim)
EXT = {}


def build_ext_tables():
    lam_ext = core.von_mangoldt_table(TAB_EXT)
    NN = np.nonzero(lam_ext > 0.0)[0]
    EXT["lam"] = lam_ext
    EXT["NN"] = NN
    EXT["U"] = np.log(NN.astype(float))
    EXT["MU"] = 2.0 * lam_ext[NN] / np.sqrt(NN.astype(float))
    EXT["G"] = np.diff(EXT["U"])
    return lam_ext


def ext_frame(kz):
    alpha = float(EXT["U"][kz])
    D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    ka = int(np.searchsorted(EXT["U"], 2.0 * alpha + 1.0e-14,
                             side="right"))
    return alpha, Mz, hz, ka


def ext_gram(kz):
    alpha, M, h, ka = ext_frame(kz)
    c_at, D = core.atom_lags_at(alpha, M, EXT["U"][:ka],
                                EXT["MU"][:ka])
    c_ar = np.asarray(core.arch_lags(M, D), float)
    c_lags = c_ar + np.asarray(c_at, float)
    d = grid_density(c_lags)
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
    out = dict(kz=kz, h=h, n=n, alpha=alpha, M=M)
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
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
    out["y_core"] = np.array([ys[idx[j]] for j in CORE_J])
    out["v_core"] = np.array([vs[idx[j]] for j in CORE_J])
    return out


def hist_label(rmins, n_total):
    hist = {}
    for r in rmins:
        hist[r] = hist.get(r, 0) + 1
    parts = []
    for r in range(1, R_MAX + 1):
        if hist.get(r):
            parts.append("r%d:%d" % (r, hist[r]))
    n_none = n_total - len(rmins)
    if n_none:
        parts.append("NONE:%d" % n_none)
    return ",".join(parts) if parts else "-"


def main():
    section("PRIME.PORT.ANTHROPIC.MOMENTS.01 -- higher-moment "
            "inertia counting on the congruent core forms: the "
            "minimal-order census (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Float-level moment "
          "bounds with a validity ward battery; the exact object "
          "is the NEWTON-STURM backstop (benchmark class, "
          "declared).")
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
    pairs = []
    for r1, r2 in zip(truth, truth[1:]):
        if not (r1.get("core_ok") and r2.get("core_ok")):
            continue
        if r1["lamS"] <= 0.0 or r1["negA"] > 0:
            continue
        pairs.append((r1, r2))
    check("W3b >= %d consecutive full-core steps" % MIN_STEPS,
          len(pairs) >= MIN_STEPS, "%d steps" % len(pairs),
          kill="K1")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})
    rows = []
    for r1, r2 in pairs:
        w = make_step(r1, r2)
        minB = float(np.linalg.eigvalsh(w["B"])[0])
        w["minB"] = minB
        w["gap"] = (w["nsc"] - float(w["b"] @ np.linalg.solve(
            w["B"], w["b"]))) if minB > 0 else float("nan")
        rs2 = sm_map.get(r2["kz"])
        w["B0"] = None
        if isinstance(rs2, dict) and "S" in rs2:
            M0 = w["Q"].T @ (rs2["S"] / r1["tau"]) @ w["Q"]
            M0 = 0.5 * (M0 + M0.T)
            w["B0"] = M0[1:, 1:]
        rows.append(w)
    minB_all = float(np.min([w["minB"] for w in rows]))
    gaps = np.array([w["gap"] for w in rows])
    gmin, gmed = float(np.min(gaps)), float(np.median(gaps))
    ok_repro = (abs(minB_all / MINB_REF - 1.0) <= MINB_RTOL
                and abs(gmin / GAPMIN_REF - 1.0) <= GAP_RTOL
                and abs(gmed / GAPMED_REF - 1.0) <= GAP_RTOL)
    check("W4 REPRODUCTION P2/P3 ledger: min lam_min(B) %.4f == "
          "%.3f; gap min/med %.4f/%.4f == %.3f/%.3f"
          % (minB_all, MINB_REF, gmin, gmed, GAPMIN_REF,
             GAPMED_REF), ok_repro, kill="K2")
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
        if int(np.sum(np.linalg.eigvalsh(Dm) < 0.0)) == 0:
            n_dom += 1
    check("W5 REPRODUCTION CXLIV V4: P_G PD on every step; float "
          "dominance negidx(B - 1/2 P_G) = 0 on %d/%d (>= %d)"
          % (n_dom, len(rows), DOMHALF_MIN),
          pg_ok and n_dom >= DOMHALF_MIN, kill="K2")
    ok_pd, _ = pd_exact(mat_fr(np.array([[2.0, 1.0], [1.0, 2.0]])))
    ok_ind, _ = pd_exact(mat_fr(np.array([[1.0, 2.0],
                                          [2.0, 1.0]])))
    xs = solve_fr([[Fraction(2), Fraction(1)],
                   [Fraction(1), Fraction(2)]],
                  [Fraction(1), Fraction(0)])
    ok_sol = (xs is not None and xs[0] == Fraction(2, 3)
              and xs[1] == Fraction(-1, 3))
    Ltest = np.array([[2.0, 0.0], [1.0, 4.0]])
    Li = tri_inv_fr(Ltest)
    ok_tri = (Li is not None
              and Li[0][0] == Fraction(1, 2) and Li[0][1] == 0
              and Li[1][0] == Fraction(-1, 8)
              and Li[1][1] == Fraction(1, 4))
    check("W6 MACHINE WARDS: exact LDL accepts PD / refuses "
          "indefinite; exact solver + triangular inverse hit "
          "known rational solutions",
          ok_pd and not ok_ind and ok_sol and ok_tri, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ M
    section("M -- the moment machine wards (validity battery, "
            "seeded ward-RNG, declared)")
    rng = np.random.default_rng(WARD_SEED)
    n_val = 0
    n_evals = 0
    n_ref = 0
    tie_dev = 0.0
    sturm_ok = True
    ok_val = True
    for i in range(NW_RAND + NW_ARROW):
        if i < NW_RAND:
            X = rng.normal(size=(8, 8))
            A = 0.5 * (X + X.T) * (10.0 ** rng.uniform(-2, 2))
        else:
            a0 = rng.normal() * (10.0 ** rng.uniform(-1, 2))
            cv = rng.normal(size=7) * (10.0 ** rng.uniform(-1, 1))
            A = np.zeros((8, 8))
            A[0, 0] = a0
            A[0, 1:] = cv
            A[1:, 0] = cv
            A[1:, 1:] = np.eye(7)
        ev = np.linalg.eigvalsh(A)
        n_le0 = int(np.sum(ev <= 0.0))
        ms = power_moments(A, 2 * R_MAX)
        for r in range(1, R_MAX + 1):
            ub = cms_ub(ms[:2 * r + 1], r)
            n_evals += 1
            if ub is None:
                n_ref += 1
                continue
            if ub < n_le0 - VAL_TOL:
                ok_val = False
            else:
                n_val += 1
            if r == 1 and ms[1] > 0:
                closed = ms[0] - ms[1] ** 2 / ms[2]
                tie_dev = max(tie_dev, abs(ub - closed)
                              / max(abs(closed), 1e-30))
        if i % 7 == 0:
            if newton_sturm_pd_float(A) != bool(ev[0] > 0.0):
                sturm_ok = False
    check("M1 WARD validity battery: %d/%d non-refusing bounds "
          "valid (UB >= n_le0 - %.0e; refusals %d of %d evals, "
          "conservative)" % (n_val, n_evals - n_ref, VAL_TOL,
                             n_ref, n_evals), ok_val, kill="K2")
    check("M2 WARD r=1 closed-form tie: max rel dev %.2e <= %.0e"
          % (tie_dev, R1_TOL), tie_dev <= R1_TOL, kill="K2")
    check("M3a WARD NEWTON-STURM (float coeffs) == eigh PD on "
          "the battery subsample", sturm_ok, kill="K2")

    # ---------------------------------------------------------- B
    section("B -- the minimal-order census (the point)")
    print("      kz    h    S1 UB(r=1..4) -> rmin    S2 "
          "UB(r=1..4) -> rmin    NEWTON-STURM(S2 exact)")
    rmins = {"S1": [], "S2": []}
    ns_cnt = 0
    ns_ok_all = True
    margins, taus = [], []
    rmin_h = []
    for w in rows:
        fs = forms_of(w)
        cells = {}
        for name in ("S1", "S2"):
            if name not in fs:
                cells[name] = ("refused(%s)"
                               % w.get("s2seat", "?"), None)
                continue
            A0, u0 = fs[name]
            rmin, best = rmin_census(A0, u0)
            cells[name] = ("[%s] -> %s"
                           % (" ".join("%.3f" % best[r]
                                       if np.isfinite(best[r])
                                       else "ref"
                                       for r in range(1,
                                                      R_MAX + 1)),
                              rmin if rmin else "NONE"), rmin)
            if rmin is not None:
                rmins[name].append(rmin)
                if name == "S2":
                    margins.append(1.0 - best[rmin])
                    taus.append(w["tau"])
                    rmin_h.append((w["r2"]["h"], rmin))
        ns = None
        A0x = s2_exact_form(w)
        if A0x is not None:
            ns = newton_sturm_pd_exact(A0x)
            m_pd = float(np.linalg.eigvalsh(w["Mt"])[0]) > 0.0
            if ns != m_pd:
                ns_ok_all = False
            if ns:
                ns_cnt += 1
        print("    %4d %5d  %-34s  %-34s  %s"
              % (w["r2"]["kz"], w["r2"]["h"], cells["S1"][0],
                 cells["S2"][0],
                 "PD" if ns else ("not-PD" if ns is not None
                                  else "refused")), flush=True)
    check("M3b WARD exact NEWTON-STURM == float eigh PD on every "
          "truth step", ns_ok_all, kill="K2")
    lab_s1 = "RMIN-S1(%s)" % hist_label(rmins["S1"], len(rows))
    lab_s2 = "RMIN-S2(%s)" % hist_label(rmins["S2"], len(rows))
    lab_ns = ("NEWTONSTURM-BENCH(%d/%d exact; r=4 class + "
              "char-poly structure == the exact-LDL benchmark "
              "class in disguise, declared)"
              % (ns_cnt, len(rows)))
    check("B typed: %s / %s / %s" % (lab_s1, lab_s2, lab_ns),
          True)
    if rmin_h:
        hs = np.array([float(h) for h, _r in rmin_h])
        rs = np.array([float(r) for _h, r in rmin_h])
        _a, sl_r, r2_r = ols_line(np.log(hs), rs)
        print("    S2 r_min vs log h: slope %+.3f (R^2 %.3f) -- "
              "stability read" % (sl_r, r2_r))
    scr_lab, _sl = screen(margins if margins else [0.0],
                          taus if taus else [1.0])
    check("B.s typed tau-screen of the S2 certificate margins "
          "(1 - UB at r_min): %s" % scr_lab, True)

    # ------------------------------------------------------------ A
    section("A -- moment anatomy at the three representative "
            "steps (first / median / last by h)")
    reps = [rows[0], rows[len(rows) // 2], rows[-1]]
    for w in reps:
        fs = forms_of(w)
        if "S2" not in fs:
            print("    kz %d h %d: S2 refused -> anatomy skipped"
                  % (w["r2"]["kz"], w["r2"]["h"]))
            continue
        A0, u0 = fs["S2"]
        A = scaled(A0, u0)
        ms = power_moments(A, 2 * R_MAX)
        Chat = A0[1:, 1:]
        chat = A0[1:, 0]
        nsc = A0[0, 0]
        print("    kz %d h %d (u0 = %.3e):"
              % (w["r2"]["kz"], w["r2"]["h"], u0))
        print("      m_k (k=1..8): %s"
              % "  ".join("%.4e" % x for x in ms[1:]))
        Pk = np.eye(7)
        for k in range(1, 2 * R_MAX + 1):
            head = (u0 * nsc) ** k
            cob = float(np.trace(
                np.linalg.matrix_power(Chat, k)))
            coup = ms[k] - head - cob
            if k <= 4:
                print("      k=%d: head %.3e  co-block tr(Chat^k) "
                      "%.3e  coupling %.3e" % (k, head, cob,
                                               coup))
        del Pk, chat
    print("    honest prime-side reading: every entry of (n, b, "
          "B) is a windowed comb functional (P2 T5); tr(A^k) is")
    print("    a polynomial in k-fold products of comb lag "
          "correlations -- tr A^3, tr A^4 read 3- and 4-fold lag")
    print("    correlations no pair-correlation statistic "
          "contains; the wiring to the head/tail cartography "
          "(CXLVII)")
    print("    is the NAMED follow-up, not computed here.")
    check("A typed: ANATOMY(3 steps printed)", True)

    # ------------------------------------------------------------ G
    section("G -- route-gate typing")
    n1 = sum(1 for r in rmins["S2"] if r == 1)
    n2p = sum(1 for r in rmins["S2"] if r >= 2)
    none_ct = len(rows) - len(rmins["S2"])
    gate = ("ROUTE-GATE(r=1 Anthropic class certifies %d/39; "
            "r>=2 certifies %d more; float-uncertified %d)"
            % (n1, n2p, none_ct))
    print("    r = 1 IS the two-moment Anthropic class (CLXIII "
          "measured 0/39 at the rank-trace vertex); r >= 2 is")
    print("    genuinely more information; the census above "
          "locates the wall's demand between the no-go class")
    print("    and the full-spectrum benchmark (NEWTON-STURM).")
    check("G typed: %s" % gate, True)

    # ------------------------------------------------------------ D
    section("D -- deep blind holdout (scored, no refits)")
    lam_ext = build_ext_tables()
    dev_tab = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                                  - core.LAM_TAB)))
    psi = np.cumsum(lam_ext[EXT["NN"]])
    nnf = EXT["NN"].astype(float)
    keep = nnf >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nnf[keep])
                         / nnf[keep]))
    check("D.w WARD deep-table overlap byte-exact (dev %.1e) and "
          "Chebyshev kappa %.6f <= %.6f + 1e-6 (fidelity battery "
          "inherited from CLX, declared)"
          % (dev_tab, kappa, core.KAPPA_REF),
          dev_tab == 0.0 and kappa <= core.KAPPA_REF + 1e-6,
          kill="K2")
    new_kz = []
    for kz in range(2, min(KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        alpha = float(EXT["U"][kz])
        X = math.exp(2.0 * alpha)
        if X > TAB_EXT:
            break
        if X <= core.ATOM_MAX:
            continue
        _a, _M, hh, _ka = ext_frame(kz)
        if not (H_HOLD[0] <= hh <= H_HOLD[1]):
            continue
        new_kz.append(kz)
    order = sorted(new_kz, key=lambda k: (ext_frame(k)[2], k))
    grams = []
    for kz in order:
        g = ext_gram(kz)
        grams.append(g)
    usable = [g for g in grams if isinstance(g, dict)
              and g.get("core_ok")]
    usable.sort(key=lambda g: (g["h"], g["kz"]))
    dsteps = []
    for g1, g2 in zip(usable, usable[1:]):
        if g1["negA"] > 0 or g1["negS"] > 0 or g1["lamS"] <= 0.0:
            continue
        w = make_step(g1, g2)
        w["PG"] = build_pg(w)
        dsteps.append(w)
    print("    deep census: %d new rungs, %d usable, %d steps  "
          "[%.1f s]" % (len(order), len(usable), len(dsteps),
                        time.time() - T0))
    drm = {"S1": [], "S2": []}
    dns = 0
    dns_ok = True
    for w in dsteps:
        fs = forms_of(w)
        cell = {}
        for name in ("S1", "S2"):
            if name not in fs:
                cell[name] = "refused"
                continue
            A0, u0 = fs[name]
            rmin, best = rmin_census(A0, u0)
            cell[name] = str(rmin) if rmin else "NONE"
            if rmin is not None:
                drm[name].append(rmin)
        ns = None
        A0x = s2_exact_form(w)
        if A0x is not None:
            ns = newton_sturm_pd_exact(A0x)
            m_pd = float(np.linalg.eigvalsh(w["Mt"])[0]) > 0.0
            if ns != m_pd:
                dns_ok = False
            if ns:
                dns += 1
        print("    DEEP kz %3d h %5d: rmin S1 %s  S2 %s  "
              "NEWTON-STURM %s"
              % (w["r2"]["kz"], w["r2"]["h"], cell["S1"],
                 cell["S2"],
                 "PD" if ns else ("not-PD" if ns is not None
                                  else "refused")), flush=True)
    check("D.s WARD exact NEWTON-STURM == float eigh PD on every "
          "deep step", dns_ok, kill="K2")
    dlab = ("DEEP-SCORED(rmin S1 %s; rmin S2 %s; NEWTON-STURM "
            "%d/%d)"
            % (hist_label(drm["S1"], len(dsteps)),
               hist_label(drm["S2"], len(dsteps)),
               dns, len(dsteps)))
    check("D typed: %s" % dlab, True)

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
    check("C3 WARD REFUSAL: exact LDL refuses the smooth co-block "
          "B0 on %d/%d usable steps (>= %d)"
          % (n_ref, n_use, REFUSE_MIN), n_ref >= REFUSE_MIN,
          kill="K2")
    rsc = ctl["scramble"]
    c4_ok = True
    c4_msg = "scramble core dead -> skipped (disclosed; C3 " \
             "carries the content)"
    if isinstance(rsc, dict) and rsc.get("core_ok") \
            and "S" in rsc and rsc["lamS"] < 0.0:
        c4_ok = rsc["lamS"] < 0.0
        c4_msg = ("lam_min(S_scr) %.3e < 0" % rsc["lamS"])
    check("C4 WARD scramble breaks the floor: %s" % c4_msg,
          c4_ok, kill="K2")
    cosh_lad, cosh_A = None, None
    for Aamp in INJ_LADDER:
        def inj(rr, _A=Aamp):
            tt = np.arange(rr["M"]) * rr["D"]
            return (_A * np.cos(INJ_GAMMA0 * tt)
                    * (np.cosh(INJ_DELTA * tt) - 1.0))
        lad = [gram_anatomy(kz, keep_chain=True, lag_fn=inj)
               for kz in zones]
        n_fire = sum(1 for r in lad
                     if r is None or (isinstance(r, dict)
                                      and r["negA"] > 0))
        print("    cosh injection A = %-5g: fires on %d/%d rungs"
              % (Aamp, n_fire, len(zones)), flush=True)
        if n_fire > 0:
            cosh_lad, cosh_A = lad, Aamp
            break
    check("C5 WARD off-line cosh injection fires (deployed A = "
          "%s)" % str(cosh_A), cosh_lad is not None, kill="K2")
    ctrl_labels = []
    c_sound = True
    for wname, lad in (("smooth",
                        [sm_map.get(kz) for kz in zones]),
                       ("cosh", cosh_lad if cosh_lad else [])):
        clad = [r for r in lad if isinstance(r, dict)]
        clad.sort(key=lambda r: (r["h"], r["kz"]))
        n_ct, n_cert, n_pd, n_ns_bad = 0, 0, 0, 0
        for g1, g2 in zip(clad, clad[1:]):
            if not (g1.get("core_ok") and g2.get("core_ok")):
                continue
            if "S" not in g1 or "S" not in g2:
                continue
            if g1["tau"] == 0.0 or "chain" not in g2 \
                    or "y_core" not in g2:
                continue
            wc = make_step(g1, g2)
            wc["PG"] = build_pg(wc)
            n_ct += 1
            m_pd = float(np.linalg.eigvalsh(wc["Mt"])[0]) > 0.0
            n_pd += m_pd
            fs = forms_of(wc)
            cert = False
            for name in ("S1", "S2"):
                if name not in fs:
                    continue
                A0, u0 = fs[name]
                rmin, _best = rmin_census(A0, u0)
                if rmin is not None:
                    cert = True
            if cert:
                n_cert += 1
                if not m_pd:
                    c_sound = False
            A0x = s2_exact_form(wc) if "cg" in wc else None
            if A0x is not None:
                if newton_sturm_pd_exact(A0x) != m_pd:
                    n_ns_bad += 1
                    c_sound = False
        ctrl_labels.append("%s(cert %d/%d, PD cores %d/%d)"
                           % (wname, n_cert, n_ct, n_pd, n_ct))
        print("    %s control steps: %d built, %d certified "
              "(any form/r), %d truly PD cores, NEWTON-STURM "
              "mismatches %d" % (wname, n_ct, n_cert, n_pd,
                                 n_ns_bad), flush=True)
    check("C6 SOUNDNESS WARD on control steps: no certificate on "
          "a non-PD core; exact backstop agrees with eigh",
          c_sound, kill="K2")
    clab = " / ".join(ctrl_labels)
    check("C7 typed: CONTROLS(%s)" % clab, True)

    return finish(dict(s1=lab_s1, s2=lab_s2, ns=lab_ns, gate=gate,
                       deep=dlab, scr=scr_lab, ctrl=clab))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("ANTHROMOMENT-MEASURED / MACHINE-WARDED / "
                   "%s / %s / %s / %s / %s / SCREEN %s / "
                   "CONTROLS(%s)"
                   % (labels.get("s1", "-"), labels.get("s2", "-"),
                      labels.get("ns", "-"),
                      labels.get("gate", "-"),
                      labels.get("deep", "-"),
                      labels.get("scr", "-"),
                      labels.get("ctrl", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the minimal-order census is a
  float-level measurement (validity-warded, conservative
  refusals) about the computed step matrices; the exact object
  is the NEWTON-STURM backstop, which is the benchmark class
  restated (declared), not new certification power.  The census
  locates the wall's information demand between the Anthropic
  two-moment class and the full spectrum; nothing here proves
  n > q uniformity in h, the pipeline enclosure, or any tail
  statement.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
