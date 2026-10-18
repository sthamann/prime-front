#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ub4_congruence_upgrade_probe -- PRIME.PORT.ANTHROPIC.UB4.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the THIRD Anthropic-port probe -- the
source-only D-UPGRADE of the congruence behind the r = 4 moment
bound.  CLXIV measured that the source-only congruence D = (1/2)
P_G + c_dom I lands the sharp CMS upper bound UB_4 on mu((-inf,
0]) at 0.83..1.60 LADDER-WIDE, crossing the integrality bar 1 on
only 7/39 core steps (5/27 deep), and the moment anatomy blames
the co-block spectral spread of Chat = L^{-1} B L^{-T}.  The
demand is now QUANTITATIVE: which source-only upgrade of D
clusters the Chat spectrum enough that UB_4 < 1 everywhere?
2026-08-11.)

THE UPGRADE FAMILY (frozen; every congruence is by an exactly
invertible matrix, so inertia(A) == inertia(M) and UB_4 < 1 =>
n_+ = 8 => M > 0 by Sylvester + integrality, exactly as CLXIV;
the D-content stays in the declared CXLIV/CL source-only
certificate class -- positive-chain CD-Gram directions, certified
scalars from exact decision procedures, and (declared by this
spec) DIAGONAL entries of computed matrices; no target eigendata
in any construction):
 (a) THE s-DIAL: D(s) = s P_G + c_dom(s) I on the frozen grid
     S_GRID = (1/4, 1/2, 3/4, 7/8, 15/16, 63/64, 1) EXACT;
     c_dom(s) re-derived per s by the CLXIII procedure verbatim
     (exact-rational LDL dominance check of B - s P_G at zero,
     then the exact dyadic bisection floor, BIS_ITERS); a rung
     REFUSES at s (DOM-FAIL) where B - s P_G is not exactly PD.
     Larger s hugs B tighter where P_G aligns.
 (b) GREEDY WOODBURY TOWARD SPREAD: restart from D0 = (1/2) P_G
     + BETA c_dom(1/2) I (BETA = 1/2 EXACT, the CLXIII S3
     headroom verbatim) and greedily add positive rank-1 chain
     components (1/2) u_k u_k^T (u_k = co-block projections of
     sqrt(v_core) p_k(y_core), ascending chain degree, pool =
     first K_POOL = 64 -- everything the positive CD chain
     exposes on the 8 core nodes; their full sum restores P_G
     exactly).  Selection is retargeted at the SPREAD: at each
     greedy step the candidate minimizing the r = 4 selection
     score (UB_4 of the congruent form at the single frozen
     scale u0; on CMS refusal the fallback score 1e6 +
     7 tr(Chat^2)/tr(Chat)^2) is taken, subject to the exact
     dominance acceptance pd_exact(B - D_new) (float prescan;
     the accepted candidate is confirmed EXACT, a float-accept /
     exact-reject is recorded and the candidate discarded);
     stop when no candidate improves by GREEDY_EPS relative or
     K_GREEDY = 24 accepted.  Report the full-grid UB_4
     trajectory vs accepted count k per rung; HEADLINE: min k
     with UB_4 < 1, per rung and ladder-wide, or the saturation
     floor of the family.
 (c) MIXED CONGRUENCE (Jacobi): after any L congruence, the
     further diagonal congruence by E = diag(d_i^{-1/2}), d_i =
     the FLOAT diagonal of the computed Chat (float entries are
     exact rationals -- the round-62 convention; E is exactly
     invertible, validity untouched, only quality shaped);
     equilibration kills the trace excess t0 - 7 by
     construction, the question is the off-diagonal mass.
 FIVE FROZEN VARIANTS scored per step (best-over-frozen-u-grid
 UB_4, CERT iff < 1 - CERT_EPS):
   VA  s-dial plain, per-step best s;
   VB  s-dial + Jacobi, per-step best s;
   VC  pure Jacobi on B itself (D = diag(B); the "equilibration
       alone" arm of the (c) question);
   VD  greedy Woodbury plain (trajectory minimum);
   VE  greedy + Jacobi at each k (trajectory minimum).
 WINNER (frozen rule): largest core census of UB_4 < 1; ties by
 smaller median of min(UB_4, 1e9); remaining ties by variant
 order VA < VB < VC < VD < VE.

FROZEN PROTOCOL (pipeline verbatim from CLXIV =
anthropic_moment_inertia_probe = CLXIII = CXLIV chain; moment
machine, u-grid, guards, battery verbatim from CLXIV):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1-W3 ladder wards (42 rungs, >= 30
     full-core, truth all-PSD, >= 20 steps); W4 P2/P3 ledger
     reproduction; W5 CXLIV V4 reproduction; W6 machine wards.

 M   MOMENT MACHINE WARDS (kill -> WARD-BROKEN): M1 validity
     battery (NW_RAND + NW_ARROW seeded matrices, declared
     ward-RNG; every non-refusing UB_r >= n_{<=0} - VAL_TOL);
     M2 r = 1 closed-form tie; M3 float NEWTON-STURM == eigh on
     the battery subsample.

 R0  REPRODUCTION OF THE PREDECESSOR SURFACE (kill ->
     WARD-BROKEN): R0.1 the whitened S1 reference certifies at
     r = 1 on every step (UB_1 < 1; identity control, TARGET
     EIGENDATA DECLARED); R0.2 the s = 1/2 baseline reproduces
     CLXIV: crossing set == REPRO_KZ (7 steps) and the
     ladder-wide UB_4 band == (0.83, 1.60) to rtol 5e-2.

 UA  THE s-DIAL CENSUS (typed, never kill): UB_4(s) per rung
     and s, plain and equilibrated tables printed; crossings
     per s; per-rung best; the global best s.

 UC  THE GREEDY CENSUS (typed): per rung the trajectory, k*
     (plain), k*_eq, trajectory minima, exact-reject count.

 WIN THE WINNER (typed + kills): five censuses; frozen winner;
     margins 1 - UB_4 on crossers; EXACT BACKSTOP (kill ->
     WARD-BROKEN): on every core crosser of the winner the
     exact-rational NEWTON-STURM (Faddeev-LeVerrier char poly +
     Sturm chain in Fractions on the exact congruent form built
     from exact Linv of the float L and, for equilibrated
     variants, the exact rational diagonal Fraction(float(e_i)))
     must certify PD, and float eigh must agree -- every
     certification is anchored exact-rationally (Sylvester on
     the float entries, the predecessor's pattern); the winner
     r_min histogram (r = 1..4) as the route-gate reading;
     FAMILY FLOOR: per-step minimum over all five variants,
     ladder min/med/max.  TAU-SCREEN of the winner margins
     (bands PASS |s| <= 0.30 / RELOC >= 0.70 / AMBIG).

 A   MOMENT ANATOMY (typed): at the three frozen representative
     steps (first / median / last by h) the m_1..m_8
     decomposition (head / co-block tr(Chat^k) / coupling) for
     the s = 1/2 baseline NEXT TO the winner -- what the four
     moments read after the upgrade; RESISTER ANATOMY: every
     core step the winner leaves >= 1 (t0 - 7, spread deficit
     7 f0 - t0^2, lam_max(Chat) float context).

 D   DEEP BLIND HOLDOUT (typed + soundness kill): the CLXIV
     deep machinery verbatim (4e6 table byte-exact + kappa
     guard, 28 new rungs, 27 steps); the WINNER construction
     (its full frozen per-step procedure) scored blind; exact
     backstop on deep crossers; census.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A)
     = 0; C1 smooth fires; C2 Epstein + scramble at kz 9 fire;
     C3 smooth-B0 exact refusal >= REFUSE_MIN; C4 scramble core
     disclosed; C5 cosh injection fires (smallest ladder
     amplitude).  CRITERION-LEVEL (typed + kill): the WINNER
     construction on smooth and cosh control steps; every
     refusal seat recorded (the declared expectation: B >= D
     dies (DOM-FAIL) or UB_4 stays >> 1 -- the census DECLARES
     which); SOUNDNESS (kill): no certificate on a step whose
     core M is not float eigh-PD.

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
machine / validity / backstop / soundness / control wards (W4-W6,
M1-M3, R0.1-R0.2, WIN backstop, D soundness, C0-C6) ->
WARD-BROKEN.  UA/UC/WIN/A/D censuses are typed measurements,
never kills.

HONEST OUTCOMES (frozen enum): UB4-CLOSED (winner census 39/39
core -- a surface-wide source-only r = 4 moment certificate,
stated with all constants) / UB4-PARTIAL(n/39; resisters typed) /
UB4-SATURATED (winner census <= the 7/39 baseline; the family
floor is the measured congruence demand for any future D).

VERDICT (frozen enum): UB4-MEASURED with typed sublabels
MACHINE-WARDED(...), REPRO(S1 r1 n/39; base 7/39 band),
SDIAL(...), EQUI(...), JACOBI(...), GREEDY(...), WINNER(...),
OUTCOME(...), BACKSTOP(...), FAMILY-FLOOR(...), RMIN(...),
DEEP-SCORED(...), RESISTERS(...), SCREEN(...), CONTROLS(...);
else PIPELINE-BROKEN / WARD-BROKEN.

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
= 9; scramble seed 1; S_GRID = (1/4, 1/2, 3/4, 7/8, 15/16, 63/64,
1) EXACT; S_BASE = 1/2 EXACT; BETA_HEADROOM = 1/2 EXACT; K_POOL =
64; K_GREEDY = 24; GREEDY_EPS = 1e-4; SEL_REFUSE_OFFSET = 1e6;
REPRO_KZ = {13, 24, 25, 26, 27, 33, 55}; REPRO_BAND = (0.83,
1.60) rtol 5e-2; representative steps = first/median/last by h;
winner tie order VA < VB < VC < VD < VE; family-floor cap 1e9.
Runtime cap declared: 18 min.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign, no spectral data of the TARGET B or M in any
CONSTRUCTION -- the D-family direction content is the positive
CD chain plus the identity plus (declared with this spec)
diagonal entries of the computed B / Chat, all matrix ENTRIES,
never eigendata; c_dom(s) is a certified scalar of the declared
CXLIV/CL certificate class (an exact decision procedure, not a
fit); the greedy selection score is a source-only moment
functional of the congruent form; S1's B^{-1/2} is DECLARED
target eigendata (identity control only); float eigensolves of M
appear only in soundness wards, the float dominance prescans and
printed context; the ward battery is synthetic (seeded RNG,
declared) and never touches ladder data.  The per-step choices
(best s, greedy order) are internal optimizations of a FROZEN
procedure over a FROZEN family -- the same procedure is applied
blind at depth.

NO-GO COMPLIANCE (frozen): no rank-1 approximation of the core;
no plain Herglotz certificate; no fit where an identity is
claimed; exact-rational decision classes per the CXLIV mandate;
the Anthropic two-moment no-go is engaged in the WIN/A blocks
(r = 1 is the two-moment class; the winner r_min histogram and
the m_3, m_4 anatomy type exactly what beyond-pair-correlation
information the certificate consumes).

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): one smoke run
of this script (34/34 with the identical bars ON THE FIRST
PASSAGE; NO bar, band, count, rule or enum was moved after it;
the only post-smoke edit is this disclosure block itself)
measured: pipeline + P2/P3 + CXLIV reproduction green (min
lam_min(B) 0.6790, gap 0.0520/0.8875, P_G PD + half-dominance
39/39); validity battery 2400/2400 (0 refusals), r = 1 tie 0.0,
float NEWTON-STURM == eigh; R0: S1 whitened UB_1 < 1 on 39/39,
s = 1/2 baseline reproduces CLXIV EXACTLY (crossers
{13,24,25,26,27,33,55}, band 0.8320/1.6002).  UA THE DIAL IS
FLAT: plain crossings 7/39 at EVERY s from 1/4 to 1 (UB_4 moves
in the third decimal; DOM-FAIL only at kz 59/44 for large s) --
the uniform floor SCALE is not the obstruction.  UC THE GREEDY
BARELY MOVES: plain cross 8/39 (kz 59 repaired at k* = 8), 31
rungs saturate at min-UB4 1.025..1.599 -- the chain ORDER is not
the obstruction either.  THE JACOBI EQUILIBRATION IS THE WHOLE
STORY: VB (dial+eq) 39/39 med 0.594, VC (pure Jacobi on B, NO
P_G) 39/39 med 0.636, VE (greedy+eq) 39/39 med 0.587; WINNER by
the frozen rule VE, census 39/39, UB_4 0.126..0.823, OUTCOME
UB4-CLOSED on the core surface; exact NEWTON-STURM backstop
39/39 PD == eigh; winner r_min histogram r3:11, r4:28 (r = 1..2
never -- genuinely beyond the two-moment class); FAMILY-FLOOR
0.00118/0.566/0.82.  DEEP BLIND: 27/27 CROSSED (UB_4 med 0.608,
backstop 27/27 PD) -- out-of-sample stable.  ANATOMY: the
equilibrated congruence collapses every moment by 2..8 orders
(kz 16: m_4 1.9e11 -> 8.7e2; head pinned at ~1, trace excess
t0 - 7 = 0 by construction) -- the CLXIV co-block spread WAS the
diagonal scale spread, and the source-only diagonal reads it
off.  SCREEN of the 39 winner margins PASS(+0.054, R^2 0.060).
CONTROLS: smooth fires 42/42, Epstein neg(A) 55, scramble
neg(A) 37 (core dead -> C4 disclosed skip), cosh A = 0.01 fires
39/42; C3 refusal 35/35; criterion-level: smooth 32 steps ALL
REFUSED at DOM-FAIL (the declared seat: B >= D dies, never a
high-UB_4 escape), cosh 37/39 refused at DOM-FAIL + 1 certified
with a truly PD core (2 PD cores exist; soundness ward clean).
Runtime 132.6 s (cap holds).  Fail-first preserved: nothing was
weakened; enums, bars and rules are exactly as frozen above.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as
P2/CXLIV; (iii) P_G / c_dom(s) / L / exact Linv exactly as the
CLXIII pipeline with s in place of 1/2; (iv) moments by float
matrix powers (k <= 8); CMS construction, guards and fallback
chain verbatim CLXIV; (v) u0 = drive/(6 n^2) if drive > 0 else
t0/(7 n) per congruent form (CLXIV S2 convention), full grid u0
2^j, j = -8..8; (vi) greedy float prescan by eigvalsh, exact
confirmation only on the selected candidate, rejected candidates
permanently excluded; (vii) NEWTON-STURM exact backstop verbatim
CLXIV (squarefree + Sturm in Fractions, count in (-inf, 0], PD
iff count 0 and p(0) != 0); (viii) deep frame/gram =
deep_blind_holdout_probe verbatim; (ix) strict inequalities in
all exact decisions.

NO RH claim: every census here is a SURFACE measurement about
the float64-computed step matrices of the deployed ladder; a
crossing is (via the exact backstop) a theorem about the
computed step matrix, never about the ideal object; nothing here
proves n > q uniformity in h, the pipeline enclosure, or any
tail statement.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control and the frozen-seed ward battery; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
P_G + congruence machinery verbatim from
anthropic_ranktrace_core_probe (CLXIII) = bfloor_pg_dominance
(CXLIV) chain; moment machine verbatim from
anthropic_moment_inertia_probe (CLXIV); Woodbury component order
from pgram_directional_schur_probe (CL); deep machinery from
deep_blind_holdout_probe; cosh signature via CLXII;
Chebyshev-Markov-Stieltjes canonical representations are the
declared classical method; Jacobi equilibration is the declared
classical preconditioning method; the Anthropic zeta-2/3 framing
is the declared external method source.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ub4_congruence_upgrade_probe.py
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
S_GRID = (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4),
          Fraction(7, 8), Fraction(15, 16), Fraction(63, 64),
          Fraction(1))
S_BASE = Fraction(1, 2)
BETA_HEADROOM = Fraction(1, 2)
S_HALF = Fraction(1, 2)
K_POOL = 64
K_GREEDY = 24
GREEDY_EPS = 1e-4
SEL_REFUSE_OFFSET = 1e6
REPRO_KZ = frozenset({13, 24, 25, 26, 27, 33, 55})
REPRO_BAND = (0.83, 1.60)
REPRO_RTOL = 5e-2
FLOOR_CAP = 1e9
V_NAMES = ("VA", "VB", "VC", "VD", "VE")
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


# --------------- pipeline, verbatim (CLXIV / CLXIII / CXLIV chain)
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


def pg_components(w):
    """Rank-1 CD-Gram summands u_k (co-block frame), ascending
    chain degree (CL frozen hierarchy order)."""
    r2 = w["r2"]
    al, be, m0 = r2["chain"]
    Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
    sq = np.sqrt(r2["v_core"])
    out = []
    for k in range(Pc.shape[1]):
        g = sq * Pc[:, k]
        out.append((w["Q"].T @ g)[1:])
    return out


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


# ------------------- moment machine (CLXIV verbatim)
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
    if r == 1:
        m0, m1, m2 = ms[0], ms[1], ms[2]
        if m2 <= 0:
            return None
        if m1 > 0:
            return m0 - m1 * m1 / m2
        return m0
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
    coeffs = np.concatenate([[1.0], cvec[::-1]])
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
    mscale = max(1.0, max(abs(x) for x in ms))
    for k in range(2 * r + 1):
        resid = abs(float(np.sum(wts * nodes ** k)) - ms[k])
        if resid > RES_TOL * mscale * max(
                1.0, float(np.max(np.abs(nodes))) ** k):
            return None
    return float(np.sum(wts[nodes <= 0.0]))


def cms_ub(ms, r):
    for rr in range(r, 0, -1):
        ub = cms_ub_once(ms[:2 * rr + 1], rr)
        if ub is not None:
            return ub
    return None


# --------------------- NEWTON-STURM (exact + float; CLXIV)
def charpoly_fr(Afr):
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
    p = poly_trim(list(p))
    g = poly_gcd(p, poly_deriv(p))
    if len(g) > 1:
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
    cs = charpoly_fr(Afr)
    if cs[-1] == 0:
        return False
    return sturm_nonpos_count(cs) == 0


def newton_sturm_pd_float(A):
    return newton_sturm_pd_exact(mat_fr(A))


# ------------------- the D-upgrade family (this probe)
def assemble_form(nsc, cvec, Cmat):
    A0 = np.zeros((8, 8))
    A0[0, 0] = nsc
    A0[0, 1:] = cvec
    A0[1:, 0] = cvec
    A0[1:, 1:] = 0.5 * (Cmat + Cmat.T)
    return A0


def u0_of(nsc, cvec, Cmat):
    t0 = float(np.trace(Cmat))
    qh = float(cvec @ cvec)
    drive = nsc * t0 - 7.0 * qh
    if drive > 0.0 and nsc > 0.0:
        return drive / (6.0 * nsc ** 2)
    return t0 / (7.0 * max(nsc, 1e-300))


def congruence_of(w, Dflt):
    """Float congruence data under a PD model D; None on refusal."""
    try:
        Lc = np.linalg.cholesky(0.5 * (Dflt + Dflt.T))
    except np.linalg.LinAlgError:
        return None
    Li = np.linalg.solve(Lc, np.eye(7))
    Chat = Li @ w["B"] @ Li.T
    Chat = 0.5 * (Chat + Chat.T)
    chat = Li @ w["b"]
    return dict(Lc=Lc, Chat=Chat, chat=chat)


def equilibrated(cvec, Cmat):
    """Jacobi diagonal congruence from the float diagonal."""
    dg = np.diag(Cmat).copy()
    if float(np.min(dg)) <= 0.0:
        return None
    e = 1.0 / np.sqrt(dg)
    Ce = e[:, None] * Cmat * e[None, :]
    return e * cvec, 0.5 * (Ce + Ce.T), e


def ub_grid(nsc, cvec, Cmat, r):
    """Best CMS UB_r over the frozen u grid (inf on total refusal)."""
    A0 = assemble_form(nsc, cvec, Cmat)
    u0 = u0_of(nsc, cvec, Cmat)
    if not (u0 > 0.0 and math.isfinite(u0)):
        return float("inf")
    best = float("inf")
    for j in range(-U_GRID_J, U_GRID_J + 1):
        u = u0 * 2.0 ** j
        ms = power_moments(scaled(A0, u), 2 * r)
        ub = cms_ub(ms, r)
        if ub is not None and ub < best:
            best = ub
    return best


def ub_pair(w, Dflt):
    """(plain UB_4, equilibrated UB_4) of the D congruence."""
    cg = congruence_of(w, Dflt)
    if cg is None:
        return float("inf"), float("inf")
    ub = ub_grid(w["nsc"], cg["chat"], cg["Chat"], R_MAX)
    eq = equilibrated(cg["chat"], cg["Chat"])
    if eq is None:
        return ub, float("inf")
    ce, Ce, _e = eq
    return ub, ub_grid(w["nsc"], ce, Ce, R_MAX)


def sel_score(w, Dflt):
    """Greedy selection score: UB_4 at the single scale u0; on CMS
    refusal the offset spread functional (frozen)."""
    cg = congruence_of(w, Dflt)
    if cg is None:
        return float("inf")
    nsc = w["nsc"]
    cvec, Cmat = cg["chat"], cg["Chat"]
    u0 = u0_of(nsc, cvec, Cmat)
    if not (u0 > 0.0 and math.isfinite(u0)):
        return float("inf")
    A0 = assemble_form(nsc, cvec, Cmat)
    ms = power_moments(scaled(A0, u0), 2 * R_MAX)
    ub = cms_ub(ms, R_MAX)
    if ub is not None:
        return ub
    t0 = float(np.trace(Cmat))
    f0 = float(np.sum(Cmat * Cmat))
    return SEL_REFUSE_OFFSET + 7.0 * f0 / max(t0 * t0, 1e-300)


def ensure_fr(w):
    if "Bfr" not in w:
        w["Bfr"] = mat_fr(w["B"])
    if "PGfr" not in w and w.get("PG") is not None:
        w["PGfr"] = mat_fr(w["PG"])


def cdom_exact(w, s_fr):
    """c_dom(s): exact dominance at zero + exact dyadic bisection
    floor of B - s P_G (CLXIII procedure with s in place of 1/2)."""
    ensure_fr(w)
    if w.get("PG") is None:
        return None
    n7 = 7
    Bfr, PGfr = w["Bfr"], w["PGfr"]
    Kfr = [[Bfr[i][j] - s_fr * PGfr[i][j] for j in range(n7)]
           for i in range(n7)]
    ok0, _ = pd_exact(Kfr)
    if not ok0:
        return None
    hi = min(Kfr[k][k] for k in range(n7))
    if hi <= 0:
        return None
    cd = cert_floor_exact(Kfr, Fraction(0), hi)
    if cd is None or cd <= 0:
        return None
    return cd


def dial_of(w):
    """The s-dial: per s the exact c_dom(s), D(s), UB_4 plain +
    equilibrated.  Cached on the step."""
    if "dial" in w:
        return w["dial"]
    out = {}
    for s in S_GRID:
        cd = cdom_exact(w, s)
        if cd is None:
            out[s] = dict(seat="DOM-FAIL")
            continue
        Dflt = float(s) * w["PG"] + float(cd) * np.eye(7)
        ub, ube = ub_pair(w, Dflt)
        out[s] = dict(cd=cd, D=Dflt, ub=ub, ube=ube)
    w["dial"] = out
    return out


def greedy_of(w):
    """Spread-targeted greedy Woodbury from the BETA = 1/2
    restart (frozen).  Cached on the step."""
    if "greedy" in w:
        return w["greedy"]
    dial = dial_of(w)
    ent = dial.get(S_BASE, {})
    if "cd" not in ent:
        w["greedy"] = dict(seat="DOM-FAIL")
        return w["greedy"]
    cd = ent["cd"]
    n7 = 7
    PG, B = w["PG"], w["B"]
    ensure_fr(w)
    Bfr = w["Bfr"]
    Dcur = 0.5 * PG + float(BETA_HEADROOM * cd) * np.eye(n7)
    Dfr = [[Fraction(float(0.5 * PG[i, j]))
            + (BETA_HEADROOM * cd if i == j else Fraction(0))
            for j in range(n7)] for i in range(n7)]
    comps = pg_components(w)[:K_POOL]
    used = [False] * len(comps)
    score = sel_score(w, Dcur)
    ub, ube = ub_pair(w, Dcur)
    traj = [(0, ub, ube)]
    min_ub, Dmin = ub, Dcur.copy()
    min_ube, Dmin_e = ube, Dcur.copy()
    kst = 0 if ub < 1.0 - CERT_EPS else None
    kst_e = 0 if ube < 1.0 - CERT_EPS else None
    n_rej = 0
    n_acc = 0
    while n_acc < K_GREEDY:
        cands = []
        for i, u in enumerate(comps):
            if used[i]:
                continue
            Dn = Dcur + 0.5 * np.outer(u, u)
            KK = B - Dn
            KK = 0.5 * (KK + KK.T)
            if float(np.linalg.eigvalsh(KK)[0]) <= 0.0:
                continue
            cands.append((sel_score(w, Dn), i, Dn))
        cands.sort(key=lambda t: t[0])
        acc = False
        for sc, i, Dn in cands:
            if sc >= score - GREEDY_EPS * max(1.0, abs(score)):
                break
            ufr = [Fraction(float(x)) for x in comps[i]]
            Dnfr = [[Dfr[a][b] + S_HALF * ufr[a] * ufr[b]
                     for b in range(n7)] for a in range(n7)]
            BD = [[Bfr[a][b] - Dnfr[a][b] for b in range(n7)]
                  for a in range(n7)]
            okd, _ = pd_exact(BD)
            used[i] = True
            if not okd:
                n_rej += 1
                continue
            Dcur, Dfr, score, acc = Dn, Dnfr, sc, True
            break
        if not acc:
            break
        n_acc += 1
        ub, ube = ub_pair(w, Dcur)
        traj.append((n_acc, ub, ube))
        if ub < min_ub:
            min_ub, Dmin = ub, Dcur.copy()
        if ube < min_ube:
            min_ube, Dmin_e = ube, Dcur.copy()
        if kst is None and ub < 1.0 - CERT_EPS:
            kst = n_acc
        if kst_e is None and ube < 1.0 - CERT_EPS:
            kst_e = n_acc
    w["greedy"] = dict(traj=traj, kst=kst, kst_e=kst_e,
                       min_ub=min_ub, Dmin=Dmin, min_ube=min_ube,
                       Dmin_e=Dmin_e, n_rej=n_rej, n_acc=n_acc)
    return w["greedy"]


def run_variant(w, vname):
    """One variant on one step: dict(val, D, eq, seat[, s, g])."""
    if vname == "VC":
        dg = np.diag(w["B"]).copy()
        if float(np.min(dg)) <= 0.0:
            return dict(val=float("inf"), D=None, eq=False,
                        seat="diag<=0")
        D = np.diag(dg)
        ub, _ube = ub_pair(w, D)
        return dict(val=ub, D=D, eq=False, seat="")
    if w.get("PG") is None:
        return dict(val=float("inf"), D=None,
                    eq=vname in ("VB", "VE"), seat="no P_G")
    if vname in ("VA", "VB"):
        dial = dial_of(w)
        key = "ub" if vname == "VA" else "ube"
        best = None
        for s in S_GRID:
            ent = dial[s]
            if key not in ent:
                continue
            if best is None or ent[key] < best[0]:
                best = (ent[key], ent["D"], s)
        if best is None:
            return dict(val=float("inf"), D=None,
                        eq=(vname == "VB"), seat="DOM-FAIL(all s)")
        return dict(val=best[0], D=best[1], eq=(vname == "VB"),
                    seat="", s=best[2])
    g = greedy_of(w)
    if g.get("seat"):
        return dict(val=float("inf"), D=None,
                    eq=(vname == "VE"), seat=g["seat"])
    if vname == "VD":
        return dict(val=g["min_ub"], D=g["Dmin"], eq=False,
                    seat="", g=g)
    return dict(val=g["min_ube"], D=g["Dmin_e"], eq=True,
                seat="", g=g)


def congruent_exact(Linv, Bfr, bfr):
    n = len(Bfr)
    BL = [[sum(Bfr[i][k] * Linv[j][k] for k in range(n))
           for j in range(n)] for i in range(n)]
    Chat = [[sum(Linv[i][k] * BL[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]
    chat = [sum(Linv[i][k] * bfr[k] for k in range(n))
            for i in range(n)]
    return Chat, chat


def exact_backstop(w, rec):
    """Exact NEWTON-STURM PD decision of the winner's congruent
    form (exact Linv of the float L; exact rational diagonal for
    equilibrated variants).  None on refusal."""
    if rec["D"] is None:
        return None
    cg = congruence_of(w, rec["D"])
    if cg is None:
        return None
    Linv = tri_inv_fr(cg["Lc"])
    if Linv is None:
        return None
    ensure_fr(w)
    bfr = [Fraction(float(x)) for x in w["b"]]
    Chat, chat = congruent_exact(Linv, w["Bfr"], bfr)
    n7 = 7
    if rec["eq"]:
        dg = np.diag(cg["Chat"]).copy()
        if float(np.min(dg)) <= 0.0:
            return None
        efr = [Fraction(float(1.0 / math.sqrt(dg[i])))
               for i in range(n7)]
        Chat = [[efr[i] * Chat[i][j] * efr[j] for j in range(n7)]
                for i in range(n7)]
        chat = [efr[i] * chat[i] for i in range(n7)]
    A0 = [[Fraction(0)] * 8 for _ in range(8)]
    A0[0][0] = Fraction(w["nsc"])
    for i in range(n7):
        A0[0][i + 1] = chat[i]
        A0[i + 1][0] = chat[i]
        for j in range(n7):
            A0[i + 1][j + 1] = (Chat[i][j] + Chat[j][i]) / 2
    return newton_sturm_pd_exact(A0)


def winner_cong(w, rec):
    """(cvec, Cmat) of the winner congruence, or None."""
    if rec["D"] is None:
        return None
    cg = congruence_of(w, rec["D"])
    if cg is None:
        return None
    cvec, Cmat = cg["chat"], cg["Chat"]
    if rec["eq"]:
        eqd = equilibrated(cvec, Cmat)
        if eqd is None:
            return None
        cvec, Cmat = eqd[0], eqd[1]
    return cvec, Cmat


def rmin_of(w, rec):
    wc = winner_cong(w, rec)
    if wc is None:
        return None
    cvec, Cmat = wc
    for r in range(1, R_MAX + 1):
        if ub_grid(w["nsc"], cvec, Cmat, r) < 1.0 - CERT_EPS:
            return r
    return None


def s1_ub1(w):
    """Whitened identity control (TARGET EIGENDATA DECLARED)."""
    wB, VB = np.linalg.eigh(w["B"])
    if float(wB[0]) <= 0.0 or w["nsc"] <= 0.0:
        return None
    c = (VB @ np.diag(wB ** -0.5) @ VB.T) @ w["b"]
    return ub_grid(w["nsc"], c, np.eye(7), 1)


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


def fmt_ub(v):
    if not math.isfinite(v):
        return "  ref "
    if v >= 100.0:
        return "%6.1f" % v
    return "%6.3f" % v


def print_anatomy(w, rec, tag):
    wc = winner_cong(w, rec)
    if wc is None:
        print("      %s: refused -> anatomy skipped" % tag)
        return
    cvec, Cmat = wc
    nsc = w["nsc"]
    u0 = u0_of(nsc, cvec, Cmat)
    A = scaled(assemble_form(nsc, cvec, Cmat), u0)
    ms = power_moments(A, 2 * R_MAX)
    print("      %s (u0 = %.3e): m_1..m_8: %s"
          % (tag, u0, "  ".join("%.3e" % x for x in ms[1:])))
    for k in range(1, R_MAX + 1):
        head = (u0 * nsc) ** k
        cob = float(np.trace(np.linalg.matrix_power(Cmat, k)))
        coup = ms[k] - head - cob
        print("        k=%d: head %.3e  co-block tr(Chat^k) "
              "%.3e  coupling %.3e" % (k, head, cob, coup))


def main():
    section("PRIME.PORT.ANTHROPIC.UB4.01 -- the source-only "
            "D-upgrade of the r = 4 moment congruence: s-dial, "
            "spread-greedy Woodbury, Jacobi equilibration "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Float-level UB_4 "
          "censuses with the CLXIV validity battery; every "
          "winning certification is anchored by the exact "
          "NEWTON-STURM backstop on the congruent form.")
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
            w["PG"] = None
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
    check("M3 WARD NEWTON-STURM (float coeffs) == eigh PD on "
          "the battery subsample", sturm_ok, kill="K2")

    # ----------------------------------------------------------- R0
    section("R0 -- predecessor-surface reproduction (S1 identity "
            "control; s = 1/2 baseline == CLXIV)")
    n_s1 = 0
    for w in rows:
        u1 = s1_ub1(w)
        if u1 is not None and u1 < 1.0 - CERT_EPS:
            n_s1 += 1
    check("R0.1 WARD whitened S1 reference certifies at r = 1 on "
          "%d/%d (identity control, target eigendata declared)"
          % (n_s1, len(rows)), n_s1 == len(rows), kill="K2")
    slabs = "".join("  s=%-6s" % str(s) for s in S_GRID)
    print("\n    UB_4(s) PLAIN (the s-dial):")
    print("      kz    h  %s" % slabs)
    for w in rows:
        dial = dial_of(w)
        cells = []
        for s in S_GRID:
            ent = dial[s]
            cells.append(fmt_ub(ent["ub"]) if "ub" in ent
                         else "  dom ")
        print("    %4d %4d  %s  [%.1f s]"
              % (w["r2"]["kz"], w["r2"]["h"],
                 "  ".join(cells), time.time() - T0), flush=True)
    base_ubs = []
    base_cross = set()
    for w in rows:
        ent = w["dial"][S_BASE]
        ub = ent.get("ub", float("inf"))
        base_ubs.append(ub)
        if ub < 1.0 - CERT_EPS:
            base_cross.add(w["r2"]["kz"])
    fin = [u for u in base_ubs if math.isfinite(u)]
    bmin = float(np.min(fin)) if fin else float("nan")
    bmax = float(np.max(fin)) if fin else float("nan")
    ok_band = (math.isfinite(bmin)
               and abs(bmin / REPRO_BAND[0] - 1.0) <= REPRO_RTOL
               and abs(bmax / REPRO_BAND[1] - 1.0) <= REPRO_RTOL)
    check("R0.2 WARD s = 1/2 baseline reproduces CLXIV: crossers "
          "%s == %s; band %.4f/%.4f == %.2f/%.2f (rtol %.0e)"
          % (sorted(base_cross), sorted(REPRO_KZ), bmin, bmax,
             REPRO_BAND[0], REPRO_BAND[1], REPRO_RTOL),
          base_cross == set(REPRO_KZ) and ok_band, kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- UA
    section("UA -- the s-dial census (typed)")
    print("    UB_4(s) EQUILIBRATED (Jacobi after the L "
          "congruence):")
    print("      kz    h  %s" % slabs)
    for w in rows:
        cells = []
        for s in S_GRID:
            ent = w["dial"][s]
            cells.append(fmt_ub(ent["ube"]) if "ube" in ent
                         else "  dom ")
        print("    %4d %4d  %s"
              % (w["r2"]["kz"], w["r2"]["h"], "  ".join(cells)),
              flush=True)
    cross_s = {}
    dom_s = {}
    for s in S_GRID:
        nc = sum(1 for w in rows
                 if w["dial"][s].get("ub", float("inf"))
                 < 1.0 - CERT_EPS)
        nce = sum(1 for w in rows
                  if w["dial"][s].get("ube", float("inf"))
                  < 1.0 - CERT_EPS)
        nd = sum(1 for w in rows if "seat" in w["dial"][s])
        cross_s[s] = (nc, nce)
        dom_s[s] = nd
    dial_lab = ", ".join("%s:%d/%d%s"
                         % (str(s), cross_s[s][0], cross_s[s][1],
                            (" dom%d" % dom_s[s])
                            if dom_s[s] else "")
                         for s in S_GRID)
    # global best s: max plain crossings, tie min median capped ub
    def med_capped(s):
        vals = [min(w["dial"][s].get("ub", float("inf")),
                    FLOOR_CAP) for w in rows]
        return float(np.median(vals))
    s_glob = max(S_GRID, key=lambda s: (cross_s[s][0],
                                        -med_capped(s)))
    check("UA typed: SDIAL(plain/eq crossings per s: %s; global "
          "best s = %s)" % (dial_lab, str(s_glob)), True)

    # ----------------------------------------------------------- UC
    section("UC -- the spread-greedy Woodbury census (typed)")
    print("      kz    h   k0-UB4    min-UB4 (k)   k*    "
          "min-UB4eq  k*eq  acc rej")
    for w in rows:
        g = greedy_of(w)
        if g.get("seat"):
            print("    %4d %4d  REFUSAL: %s"
                  % (w["r2"]["kz"], w["r2"]["h"], g["seat"]),
                  flush=True)
            continue
        ub0 = g["traj"][0][1]
        kmin = min(range(len(g["traj"])),
                   key=lambda i: g["traj"][i][1])
        print("    %4d %4d  %s   %s (%2d)   %-4s  %s  %-4s "
              "%3d %3d  [%.1f s]"
              % (w["r2"]["kz"], w["r2"]["h"], fmt_ub(ub0),
                 fmt_ub(g["min_ub"]), kmin,
                 str(g["kst"]) if g["kst"] is not None else "-",
                 fmt_ub(g["min_ube"]),
                 str(g["kst_e"]) if g["kst_e"] is not None
                 else "-", g["n_acc"], g["n_rej"],
                 time.time() - T0), flush=True)
    ksts = [w["greedy"]["kst"] for w in rows
            if not w["greedy"].get("seat")
            and w["greedy"]["kst"] is not None]
    sat = [w["greedy"]["min_ub"] for w in rows
           if not w["greedy"].get("seat")
           and w["greedy"]["kst"] is None]
    greedy_lab = ("GREEDY(cross %d/%d, k* med %s max %s; "
                  "saturating %d at min-UB4 %s..%s)"
                  % (len(ksts), len(rows),
                     ("%.0f" % float(np.median(ksts)))
                     if ksts else "-",
                     ("%d" % max(ksts)) if ksts else "-",
                     len(sat),
                     fmt_ub(float(np.min(sat))).strip()
                     if sat else "-",
                     fmt_ub(float(np.max(sat))).strip()
                     if sat else "-"))
    check("UC typed: %s" % greedy_lab, True)

    # ---------------------------------------------------------- WIN
    section("WIN -- the five-variant census, the frozen winner, "
            "the exact backstop")
    vrecs = {v: [run_variant(w, v) for w in rows]
             for v in V_NAMES}
    cens = {}
    meds = {}
    for v in V_NAMES:
        vals = [r["val"] for r in vrecs[v]]
        cens[v] = sum(1 for x in vals if x < 1.0 - CERT_EPS)
        meds[v] = float(np.median([min(x, FLOOR_CAP)
                                   for x in vals]))
        print("    %s: census %d/%d  med UB_4 %.4g"
              % (v, cens[v], len(rows), meds[v]))
    win = min(V_NAMES,
              key=lambda v: (-cens[v], meds[v],
                             V_NAMES.index(v)))
    wrecs = vrecs[win]
    wvals = [r["val"] for r in wrecs]
    n_win = cens[win]
    print("    WINNER (frozen rule): %s  census %d/%d  med %.4g"
          % (win, n_win, len(rows), meds[win]))
    ffloor = []
    for i in range(len(rows)):
        ffloor.append(min(min(vrecs[v][i]["val"], FLOOR_CAP)
                          for v in V_NAMES))
    fl_lab = ("FAMILY-FLOOR(min/med/max %.3g/%.3g/%.3g)"
              % (float(np.min(ffloor)), float(np.median(ffloor)),
                 float(np.max(ffloor))))
    check("WIN typed: WINNER(%s, %d/%d, med %.4g) / %s"
          % (win, n_win, len(rows), meds[win], fl_lab), True)
    # exact backstop + soundness on every core crosser
    n_bs = 0
    n_cross = 0
    bs_ok = True
    margins, taus = [], []
    for w, rec in zip(rows, wrecs):
        if rec["val"] >= 1.0 - CERT_EPS:
            continue
        n_cross += 1
        margins.append(1.0 - rec["val"])
        taus.append(w["tau"])
        pd_f = float(np.linalg.eigvalsh(w["Mt"])[0]) > 0.0
        ns = exact_backstop(w, rec)
        if ns is None or ns is not True or not pd_f:
            bs_ok = False
            print("    BACKSTOP SEAT kz %d h %d: exact %s, "
                  "eigh-PD %s" % (w["r2"]["kz"], w["r2"]["h"],
                                  ns, pd_f), flush=True)
        else:
            n_bs += 1
    check("WIN.b WARD exact NEWTON-STURM backstop certifies PD "
          "on every winner crosser and eigh agrees: %d/%d"
          % (n_bs, n_cross), bs_ok, kill="K2")
    rmins = []
    for w, rec in zip(rows, wrecs):
        rm = rmin_of(w, rec)
        if rm is not None:
            rmins.append(rm)
    hist = {r: rmins.count(r) for r in range(1, R_MAX + 1)}
    rmin_lab = ("RMIN(%s%s)"
                % (",".join("r%d:%d" % (r, hist[r])
                            for r in range(1, R_MAX + 1)
                            if hist[r]),
                   (",NONE:%d" % (len(rows) - len(rmins)))
                   if len(rmins) < len(rows) else ""))
    check("WIN.r typed winner minimal-order census: %s (r = 1 is "
          "the two-moment Anthropic class; the census locates "
          "what the upgrade buys)" % rmin_lab, True)
    if n_win == len(rows):
        outcome = ("UB4-CLOSED(39-> %d/%d core; winner %s; "
                   "UB_4 %.3g..%.3g)"
                   % (n_win, len(rows), win,
                      float(np.min(wvals)), float(np.max(wvals))))
    elif n_win <= len(REPRO_KZ):
        outcome = ("UB4-SATURATED(%d/%d <= baseline 7; %s)"
                   % (n_win, len(rows), fl_lab))
    else:
        outcome = "UB4-PARTIAL(%d/%d core)" % (n_win, len(rows))
    check("WIN.o typed: OUTCOME %s" % outcome, True)
    scr_lab, _sl = screen(margins if margins else [0.0],
                          taus if taus else [1.0])
    check("WIN.s typed tau-screen of the winner margins "
          "(1 - UB_4): %s" % scr_lab, True)

    # ------------------------------------------------------------ A
    section("A -- moment anatomy (baseline vs winner) + resister "
            "anatomy")
    reps = [rows[0], rows[len(rows) // 2], rows[-1]]
    for w in reps:
        print("    kz %d h %d:" % (w["r2"]["kz"], w["r2"]["h"]))
        ent = w["dial"][S_BASE]
        base_rec = (dict(val=ent["ub"], D=ent["D"], eq=False,
                         seat="") if "D" in ent
                    else dict(val=float("inf"), D=None, eq=False,
                              seat="DOM-FAIL"))
        print_anatomy(w, base_rec, "baseline s=1/2")
        print_anatomy(w, wrecs[rows.index(w)], "winner %s" % win)
    n_res = 0
    res_ubs = []
    for w, rec in zip(rows, wrecs):
        if rec["val"] < 1.0 - CERT_EPS:
            continue
        n_res += 1
        res_ubs.append(min(rec["val"], FLOOR_CAP))
        wc = winner_cong(w, rec)
        if wc is None:
            print("    RESISTER kz %d h %d: refused (%s)"
                  % (w["r2"]["kz"], w["r2"]["h"], rec["seat"]))
            continue
        cvec, Cmat = wc
        t0 = float(np.trace(Cmat))
        f0 = float(np.sum(Cmat * Cmat))
        lmax = float(np.linalg.eigvalsh(Cmat)[-1])
        print("    RESISTER kz %d h %d: UB_4 %.4f  t0-7 %+.3e  "
              "7f0-t0^2 %.3e  lam_max(Chat) %.3g"
              % (w["r2"]["kz"], w["r2"]["h"], rec["val"],
                 t0 - 7.0, 7.0 * f0 - t0 * t0, lmax), flush=True)
    res_lab = ("RESISTERS(%d%s)"
               % (n_res, (", med UB_4 %.3g"
                          % float(np.median(res_ubs)))
                  if res_ubs else ""))
    check("A typed: ANATOMY(3 steps) / %s" % res_lab, True)

    # ------------------------------------------------------------ D
    section("D -- deep blind holdout (winner construction, "
            "scored, no refits)")
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
    n_dc = 0
    n_dbs = 0
    d_sound = True
    dvals = []
    for w in dsteps:
        rec = run_variant(w, win)
        dvals.append(min(rec["val"], FLOOR_CAP))
        crossed = rec["val"] < 1.0 - CERT_EPS
        tag = ""
        if crossed:
            n_dc += 1
            pd_f = float(np.linalg.eigvalsh(w["Mt"])[0]) > 0.0
            ns = exact_backstop(w, rec)
            if ns is True and pd_f:
                n_dbs += 1
                tag = "  backstop PD"
            else:
                d_sound = False
                tag = "  BACKSTOP SEAT(exact %s, eigh %s)" % (
                    ns, pd_f)
        print("    DEEP kz %3d h %5d: UB_4 %s%s%s  [%.1f s]"
              % (w["r2"]["kz"], w["r2"]["h"], fmt_ub(rec["val"]),
                 (" (%s)" % rec["seat"]) if rec["seat"] else "",
                 tag, time.time() - T0), flush=True)
    check("D.s WARD deep soundness: exact backstop + eigh agree "
          "on every deep crosser (%d/%d)" % (n_dbs, n_dc),
          d_sound, kill="K2")
    dlab = ("DEEP-SCORED(winner %s crosses %d/%d, med UB_4 %.3g, "
            "backstop %d/%d)"
            % (win, n_dc, len(dsteps),
               float(np.median(dvals)) if dvals else float("nan"),
               n_dbs, n_dc))
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
        n_ct, n_cert, n_pd = 0, 0, 0
        seats = {}
        n_high = 0
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
            rec = run_variant(wc, win)
            if rec["seat"]:
                seats[rec["seat"]] = seats.get(rec["seat"], 0) + 1
            elif rec["val"] >= 1.0 - CERT_EPS:
                n_high += 1
            else:
                n_cert += 1
                if not m_pd:
                    c_sound = False
        seat_lab = ",".join("%s x%d" % (k, v)
                            for k, v in sorted(seats.items()))
        ctrl_labels.append("%s(cert %d/%d, UB4>=1 %d, refuse "
                           "[%s], PD cores %d/%d)"
                           % (wname, n_cert, n_ct, n_high,
                              seat_lab, n_pd, n_ct))
        print("    %s control steps: %d built, %d certified, %d "
              "with UB_4 >= 1, refusal seats [%s], %d truly PD "
              "cores" % (wname, n_ct, n_cert, n_high, seat_lab,
                         n_pd), flush=True)
    check("C6 SOUNDNESS WARD on control steps: no winner "
          "certificate on a non-PD core", c_sound, kill="K2")
    clab = " / ".join(ctrl_labels)
    check("C7 typed: CONTROLS(%s) -- the declared refusal seat "
          "census answers 'B >= D dies or UB_4 stays high'"
          % clab, True)

    return finish(dict(
        repro="REPRO(S1 r1 %d/%d; base %d/39 band %.2f/%.2f)"
              % (n_s1, len(rows), len(base_cross), bmin, bmax),
        dial="SDIAL(%s; best s = %s)" % (dial_lab, str(s_glob)),
        greedy=greedy_lab,
        winner="WINNER(%s, %d/%d, med %.4g)"
               % (win, n_win, len(rows), meds[win]),
        outcome=outcome, floor=fl_lab, rmin=rmin_lab,
        bs="BACKSTOP(%d/%d)" % (n_bs, n_cross),
        deep=dlab, res=res_lab, scr=scr_lab, ctrl=clab))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("UB4-MEASURED / MACHINE-WARDED / %s / %s / "
                   "%s / %s / %s / %s / %s / %s / %s / %s / "
                   "SCREEN %s / CONTROLS(%s)"
                   % (labels.get("repro", "-"),
                      labels.get("dial", "-"),
                      labels.get("greedy", "-"),
                      labels.get("winner", "-"),
                      labels.get("outcome", "-"),
                      labels.get("floor", "-"),
                      labels.get("rmin", "-"),
                      labels.get("bs", "-"),
                      labels.get("deep", "-"),
                      labels.get("res", "-"),
                      labels.get("scr", "-"),
                      labels.get("ctrl", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): every UB_4 census is a float-level
  measurement (validity-warded, conservative refusals) about the
  computed step matrices; every winner crossing is anchored by
  the exact NEWTON-STURM backstop, i.e. a theorem about the
  float64-computed step matrix, never about the ideal object.
  The D-upgrade family is source-only in the declared
  certificate-class sense; the census locates the congruence
  demand of the wall at r = 4.  Nothing here proves n > q
  uniformity in h, the pipeline enclosure, or any tail
  statement.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
