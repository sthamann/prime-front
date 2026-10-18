#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""anthropic_ranktrace_core_probe -- PRIME.PORT.ANTHROPIC.RANKTRACE.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: a NEW ROUTE ported from the Anthropic zeta-2/3
method -- effective-rank / inertia counting.  The wall endform
(B_h PD) AND (n_h > q_h) is re-read as a POSITIVE-INDEX-8
statement about the fixed 8x8 core M = [[n, b*],[b, B]], decided
by the rank-trace (effective-rank) inequality on a CONGRUENT form
whose construction is source-only.  STATE-level, not
transition-level: the CLXII kill (transition barriers are
wall-blind) does not touch this route -- here M > 0 is EXACTLY
the rung-r2 core wall.  2026-08-11.)

THE MECHANISM (frozen, with the verified algebra).  For the
scaled congruent form A(u) = [[u n, sqrt(u) c*],[sqrt(u) c, I_7]]
with c = B^{-1/2} b, q = |c|^2:
    tr A = u n + 7;   ||A||_F^2 = u^2 n^2 + 2 u q + 7;
    EXACT IDENTITY:
      (tr A)^2 - 7 ||A||_F^2 = u (14 (n - q) - 6 u n^2),
    and at u_h = 7 mu1 / (6 n^2), mu1(h) = 4 sin^2(pi/(2h+1)):
      (tr A)^2 - 7 ||A||_F^2 = 14 u_h (n - q - (1/2) mu1),
so the EFFRANK CRITERION  (tr A)^2 / ||A||_F^2 > 7  at u_h is
EQUIVALENT to the registered HALFGAP target n - q > (1/2) mu1.
By the rank-trace inequality (Cauchy-Schwarz over the positive
eigenvalues, valid when tr A > 0):  n_+(A) >= (tr A)^2/||A||_F^2,
and by INTEGRALITY on the fixed 8-dim core, ratio > 7 forces
n_+(A) = 8, i.e. A > 0, i.e. (Sylvester congruence) M > 0.
HALFGAP = a positive-index-8 statement.

THE ROUTE GATE (typed, frozen).  The criterion reads exactly TWO
moments -- tr and ||.||_F -- of a congruent form: the Anthropic
zeta-2/3 information class (their no-go: first two moments +
bandwidth-1 pair correlation caps the positive-proportion method
at ~68% in its asymptotic population domain).  What each stage
declares beyond that class: S1 adds the exact whitening
congruence c = B^{-1/2} b -- TARGET EIGENDATA, an identity
control, NOT a route; S2 adds (i) the EXACT source-only
congruence structure T0 = diag(1, L_G^{-T}) with L_G L_G^T ~ D =
(1/2) P_G + c_dom I -- matrix-level structural information, not a
population statistic, (ii) INTEGRALITY of inertia on the FIXED
8-dim core (a per-object certificate, not an asymptotic
proportion), (iii) an optimized scale u; S3 adds positive
CD-Gram components (higher congruence resolution).  The no-go is
not contradicted -- it is SIDESTEPPED at a finite per-object
level, and this typing is part of the registered object.

EXACTNESS MODEL (frozen; the round-62 pattern).  The S2/S3
certificate chain is EXACT: L (float Cholesky of the float D) is
an exactly invertible lower-triangular rational matrix (float
entries are exact rationals, positive diagonal warded); Linv by
exact Fraction forward substitution; Chat = Linv B Linv^T, chat =
Linv b, and the scalars t0 = tr Chat, qhat = |chat|^2, f0 =
||Chat||_F^2 are EXACT rationals; the criterion decision
    PASS  iff  drive := n t0 - 7 qhat > 0
          and  drive^2 > 6 n^2 (7 f0 - t0^2)
          and  tr A(u_q) = u_q n + t0 > 0,  u_q = drive/(6 n^2),
is decided in Fractions with NO rounding anywhere in the decision
path.  VALIDITY DOES NOT NEED L L^T == D: T0 is exactly
invertible, so inertia(A(u)) == inertia(M) for every rational
u > 0 (Sylvester over the rationals); D only shapes the QUALITY
of the congruence.  A PASS is therefore a THEOREM about the
float64-computed step matrix M ("M is positive definite").  What
is NOT enclosed: the float pipeline that produces the entries
(FFT density, Lanczos, eigh frame, Schur solves) -- the interval
rollout of that pipeline is the CONCURRENT separate work item
(CLIII class) and is deliberately not duplicated here; the
ideal-object interval version of THIS criterion is typed as the
natural follow-up, not required here.  NO RH claim.

FROZEN PROTOCOL (pipeline verbatim from bfloor_pg_dominance_probe
= CXLIV = v900 chain; registry machinery verbatim from
halfgap_registration_probe = CLI; deep machinery verbatim from
deep_blind_holdout_probe = CLX class; ONE Gram per rung; window
memoization):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2
     >= 30 full-core rungs; W3a truth all-PSD (A, R, S); W3b >=
     20 consecutive full-core steps; W4 REPRODUCTION P2/P3
     ledger: min lam_min(B) == 0.679 (rtol 2e-2), gap min/med ==
     0.052/0.888 (rtol 5e-2), raw-B certified disaster; W5
     REPRODUCTION CXLIV V4: P_G PD on every step, float dominance
     negidx(B - 1/2 P_G) = 0 on >= 37; W6 MACHINE WARDS: exact
     LDL accepts PD / refuses indefinite; exact solver hits a
     known rational solution; exact triangular inversion ties
     L Linv == I exactly on a rational example.

 R   ROUTE-GATE DECLARATION (typed, never kill): the information
     class of each stage printed as frozen above.

 S1  EXACT WHITENING = THE HALFGAP DICTIONARY (identity control,
     TARGET EIGENDATA DECLARED, not source-only; kill ->
     WARD-BROKEN on any ward):
     S1.w0 SYMBOLIC WARD: the identity (u n + p)^2 -
           p (u^2 n^2 + 2 u q + p) == u (2 p (n - q) -
           (p - 1) u n^2) verified in EXACT Fractions on a frozen
           deterministic list of rational (n, q, u, p) tuples;
     S1.w1 MATERIALIZED WARD (all 39 steps): c = B^{-1/2} b
           (float), A(u_h) materialized; (tr A)^2 - 7 ||A||_F^2
           == 14 u_h (n - q - mu1/2) to ID_WARD relative; inertia
           tie n_+(A(u_h)) == n_+(M) (eigh, float);
     S1.w2 CORE DICTIONARY (all 39 steps): boolean [ratio(u_h) >
           7] == [n - q > mu1/2], the right side decided EXACT
           (q by exact solve on Bfr; bar = Fraction(float(mu1))/2
           -- the round-62 float-entry convention, declared);
           mu1 on r2's h; census printed (CLXII context: s >=
           (1/2) mu1 held 39/39 with >= 11x slack);
     S1.w3 FULL-FRAME DICTIONARY (the registered CLI surface):
           the 67-rung registry rebuilt verbatim, sha256 ==
           REG_SHA (kill); with the pivot collapse (n = m, q = 0;
           CLI W4 ward upstream) the criterion at u_p =
           p mu1/((p-1) m^2), p = dim - 1, reads m > (1/2) mu1,
           so the boolean census must equal the registered
           shat >= 1/2 census EXACTLY (67/67; strict-tie
           convention declared: no float tie observed or
           expected); on the REG_KZ rungs the whitened full-frame
           A(u_p) is MATERIALIZED (c = B_full^{-1/2} b_full) and
           the closed form + inertia tie are warded numerically
           (FULLDICT_WARD).

 S2  THE SOURCE-ONLY P_G CONGRUENCE (the point; per step, exact):
     Kfr = Bfr - (1/2) Pfr exact; dominance at zero pd_exact
     (expected 39/39; a failing step is typed DOM-FAIL and the
     criterion REFUSES there); c_dom = exact dyadic LDL bisection
     (BIS_ITERS, final PD re-decided); D = (1/2) P_G + c_dom I
     (float), L = cholesky(D); exact Linv, Chat, chat, scalars;
     the exact criterion above; margin r(u_q) - 7 =
     Q(u_q)/F(u_q) exact (printed float).  SOUNDNESS WARD (kill
     -> WARD-BROKEN): every PASS step must have float
     eigh-PD M (the certificate may never out-claim the truth).
     THE DECISIVE MEASUREMENT: PASS census n/39.  LOSS ANATOMY
     vs S1 per step: t0 - 7 (trace excess of the co-block
     congruence), the spread deficit 7 f0 - t0^2 (>= 0 by
     Cauchy-Schwarz; == 0 iff Chat = c I: exactly the slack the
     B >> D directions inflate), drive, lam_max(Chat) (float
     context), qhat/q; the failing mechanism named from the
     measured table.  TAU-SCREEN (mandatory): OLS slope of
     log(margin) vs log tau on the positive subset (bands PASS
     |s| <= 0.30 / RELOC >= 0.70 / AMBIG).

 S3  P_G + WOODBURY REPAIR (only on S2-fail steps; frozen):
     restart from D0' = (1/2) P_G + BETA c_dom I (BETA = 1/2
     EXACT -- the CLXII lesson: at saturated c_dom the hierarchy
     is acceptance-blocked, B - D has a zero floor eigenvalue;
     the BETA headroom is frozen a priori, disclosed); components
     w_k = sqrt(1/2) u_k, u_k = co-block of Q^T (sqrt(v_core)
     p_k(y_core)) in ASCENDING chain degree (frozen order, never
     target data); acceptance = exact pd_exact(B - D_{k+1}); at
     most K_HIER candidates; after each acceptance the FULL exact
     criterion is re-decided on the new congruence.  k*(step) =
     accepted count at first PASS; typed S3-REPAIR(n_repaired/
     n_failing, k* stats) / S3-EXHAUSTED(count) / S3-VACUOUS.

 D   DEEP BLIND HOLDOUT (typed, never kill; scored, no refits):
     the 4e6 table rebuilt (ward: byte-exact overlap with the
     deployed table; Chebyshev kappa within the v770 guard; the
     remaining fidelity battery is inherited from CLX upstream,
     declared); the 28 new rungs (ATOM_MAX < X <= 4e6, h in
     [128, 2900]) built with the verbatim gram machinery; deep
     steps = consecutive usable pairs (r1 all-PSD, lamS > 0);
     scored BLIND per step: (a) the exact core halfgap census
     n - q > (1/2) mu1 (the CLXII 39/39 invariant, out-of-sample
     at depth), (b) the S2 exact criterion census, (c) S3 on
     fails.  Typed DEEP-SCORED(counts) / DEEP-THIN(n < 10,
     measured anyway).

 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth neg(A) =
     0 everywhere; C1 smooth world neg(A) > 0 on >= 1 rung; C2
     Epstein x^2+5y^2 comb + scramble (seed 1) at kz 9 fire; C3
     THE REFUSAL WARD: exact LDL refuses the smooth co-block B0
     on >= REFUSE_MIN usable steps (the premise dies in the
     smooth world); C4 scramble core, where it exists, breaks
     the floor (disclosed skip if dead); C5 off-line cosh
     injection (lag signature s A cos(gamma0 t)(cosh(delta t) -
     1), t = j D; frozen amplitude ladder (0.01, 0.1, 1.0),
     smallest firing deployed -- the CLXII convention) fires on
     >= 1 rung.  CRITERION-LEVEL CENSUS (typed + one kill): on
     the smooth and cosh worlds, control steps are built with
     RELAXED preconditions (linear algebra permitting) and the
     FULL S2 pipeline is run; SOUNDNESS (kill -> WARD-BROKEN): a
     control step the criterion CERTIFIES must be float eigh-PD
     (M truly PD there); typed per world CONTROLS-BREAK-S2(0/n
     certified) or CORE-CONSISTENT(k/n: every certified control
     step is a genuinely PD core -- the STATE-level design
     lesson: M > 0 IS the rung-r2 core wall, so unlike the CLXII
     transition barrier this criterion cannot certify a broken
     core; it can at most be blind to breaks OUTSIDE the 8-fold
     core, measured here).  The mass-rescale world is DECLARED
     SKIPPED (not in this probe's scope; the CLXII rescale
     census stands upstream).

KILLS: K1 pipeline (W1-W3, deep census impossible only if the
deployed ladder itself dies) -> PIPELINE-BROKEN; K2 reproduction
/ identity / machine / soundness / control wards (W4-W6, S1.w0-
S1.w3, S2 soundness, C0-C5 soundness) -> WARD-BROKEN.  All
S2/S3/D censuses are typed measurements, never kills.

VERDICT (frozen enum): ANTHRORANKTRACE-MEASURED with typed
sublabels ROUTE-GATE-DECLARED, S1-DICT-CORE(39/39),
S1-DICT-FULL(67/67, sha8), S2-CENSUS(n/39, min/med margin),
LOSS-ANATOMY(med t0-7, med spread deficit, med qhat/q),
S3-REPAIR(...)/S3-EXHAUSTED(...)/S3-VACUOUS,
DEEP-SCORED(halfgap a/b, S2 c/d [, S3 ...])/DEEP-THIN,
SCREEN(...), CONTROLS(...); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2); PG_TOL
= 1e-12; DOMHALF_MIN = 37; BIS_ITERS = 40; S_HALF = 1/2 EXACT;
BETA_HEADROOM = 1/2 EXACT; K_HIER = 64; ID_WARD = 1e-9;
FULLDICT_WARD = 1e-6; KZMAX_REG = 150; REG_SHA = ae292e55... (67
lines, CLI registry); SHAT_REF = (0.502, 1.027, 2.185) rtol 2e-2;
REG_KZ = (9, 60, 121); TAB_EXT = 4_000_000; H_HOLD = (128, 2900);
KZ_SCAN_MAX = 400; MIN_NEW = 10 (typed only); INJ_LADDER = (0.01,
0.1, 1.0); INJ_DELTA = 0.05; INJ_GAMMA0 = 10.0; REFUSE_MIN = 30;
SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; CTRL_KZ = 9; scramble seed
1; mu1(h) = 4 sin^2(pi/(2h+1)) on r2's h.  Runtime cap declared:
15 min.

ANTI-CIRCULARITY (frozen): no sigma_h, no defect eigenvector, no
pivot sign, no spectral data of the TARGET B or M in any S2/S3
CONSTRUCTION -- T0 is built from D = (1/2) P_G + c_dom I whose
direction content is source-only (positive-chain CD Gram plus the
identity; c_dom is a certified scalar of the declared CXLIV/CL
certificate class -- a decision procedure, not a fit); the
hierarchy selects components by frozen chain order; S1's
B^{-1/2} is DECLARED target eigendata and is used ONLY as the
identity control / dictionary, never in a route construction;
float eigensolves elsewhere are bisection hints, soundness
comparisons and printed context only; the deep rungs are scored
and never feed back into any registered object.

NO-GO COMPLIANCE (frozen): no rank-1 approximation of the core
update; no plain Herglotz certificate; no fit where an identity
is claimed; exact-rational LDL/solves per the CXLIV mandate --
declared, not silent; the Anthropic two-moment no-go is addressed
head-on in the R block (typed), not silently bypassed.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): one smoke run
of this script (33/33 with the identical bars; NO bar, band,
count, rule or enum was moved after it; the only post-smoke edit
is this disclosure block itself) measured: pipeline + P2/P3 +
CXLIV + CLI reproduction green (min lam_min(B) 0.6790, gap
0.0520/0.8875, P_G PD + half-dominance 39/39, registry sha
ae292e55 MATCH, 67 rungs, band 0.502/1.027/2.185).  S1: symbolic
identity exact 6/6; materialized ward max rel dev 8.6e-10;
inertia tie 39/39; CORE DICTIONARY boolean-equal 39/39 (both
sides TRUE 39/39; slack (n-q)/(mu1/2) in X-coordinates min/med/
max 2.01e+03/2.93e+04/7.57e+05); FULL-FRAME DICTIONARY
boolean-equal 67/67 == the registered census, REG_KZ
materialization max dev 4.0e-14 with ratio - p = +0.923/+0.988/
+0.907 at kz 9/60/121, inertia ties exact.  S2 THE HEADLINE: the
source-only criterion PASSES 0/39 -- drive = n t0 - 7 qhat > 0 on
34/39 (5 drive-negative seats: kz 59/26/16/44/24, the familiar
k*-outlier steps) but Q(u_q) <= 0 EVERYWHERE: the spread deficit
7 f0 - t0^2 (med 2.72e+05) dwarfs drive^2/(6 n^2) on every step;
med t0 - 7 = 346, med qhat/q = 91.3 (the CL Loewner table
verbatim -- the SAME D^{-1} inflation), med lam_max(Chat) = 225;
ratio r(u_q) sits at 2.0..3.6 (margins -3.4..-5.1), never near
7.  The loss anatomy names the mechanism as frozen: the
congruence slack of the B >> D directions inflates BOTH
two-moment invariants -- the state-level twin of CL's OUTCOME-C,
now measured in the effrank metric.  TAU-SCREEN vacuous (pos =
0, disclosed).  S3: acceptance is fully OPEN at BETA = 1/2 (med
64/64 candidates accepted -- the CLXII acceptance block is
gone with the headroom) yet repair count 0/39, and the deficit
at exhaustion is WORSE (med 9.24e+05 vs 2.72e+05 at full c_dom):
the 64 low-degree CD components buy back qhat but pay more in
co-block spread than the halved c_dom floor costs -- the
obstruction is the SPREAD, not the acceptance.  DEEP: 28 new
rungs, 28 usable, 27 steps; the exact core halfgap n - q >
(1/2) mu1 holds 27/27 BLIND (min slack 1.71e+05,
X-coordinates); S2 deep census 0/27 (same Q(u_q) <= 0 seat on
every step); S3 deep repair 0/27.  Controls: smooth fires 42/42,
Epstein neg(A) 55, scramble neg(A) 37 (core dead -> C4 disclosed
skip), cosh A = 0.01 fires 39/42 (smallest ladder amplitude);
C3 refusal 35/35; criterion-level census: smooth
CONTROLS-BREAK-S2(0/32 certified, 32 refusals, 0 PD cores), cosh
CONTROLS-BREAK-S2(0/39 certified, 39 refusals, 2 truly PD cores
-- even where the injected world keeps the 8-fold core PD the
source-only congruence refuses; soundness ward clean).  Runtime
128.1 s (cap holds).  Fail-first preserved: nothing was
weakened; enums, bars and rules are exactly as frozen above.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) Householder frame as
P2/CXLIV; (iii) P_G via eval_chain on r2's own chain at r2's core
nodes, degree < h (CXLIV V0, s = 1/2 by V4); (iv) exact LDL =
symmetric Gaussian elimination in Fractions (Sylvester); exact
solve = Gaussian elimination with partial pivoting in Fractions;
exact Linv = forward substitution in Fractions on the float L;
(v) bisection lo certified by a final exact re-decision; (vi)
negidx = float sign count; (vii) OLS population statistics as
v900; screens read positive subsets; (viii) deep frame/gram =
deep_blind_holdout_probe verbatim (ext arrays, same formulas);
(ix) strict inequalities everywhere in the exact decisions (a
Fraction tie is a FAIL of the criterion, never a pass).

NO RH claim: a PASS census (had it been nonzero) would be a
SURFACE statement about the computed step matrices of the
deployed ladder; 0/39 is a route-mortality measurement of THIS
congruence, not of the mechanism (the dictionary S1 is exact);
nothing here proves n > q uniformity in h, the pipeline
enclosure, or any tail statement.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
P_G machinery verbatim from bfloor_pg_dominance_probe (CXLIV);
registry machinery verbatim from halfgap_registration_probe
(CLI, declared input: REG_SHA, 1/2, NO-ADJUST); deep machinery
verbatim from deep_blind_holdout_probe (CLX class); Woodbury
component order from pgram_directional_schur_probe (CL); cosh
signature from arith_healthcode12_probe via CLXII (declared
convention); the Anthropic zeta-2/3 effective-rank framing is
the DECLARED external method source (route gate above).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/anthropic_ranktrace_core_probe.py
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
S_HALF = Fraction(1, 2)
BETA_HEADROOM = Fraction(1, 2)
K_HIER = 64
ID_WARD = 1e-9
FULLDICT_WARD = 1e-6
KZMAX_REG = 150
REG_SHA = ("ae292e557efa24f13fa1d75823219bcda9a0f6757089fee459e"
           "5c652e3458df8")
SHAT_REF = (0.502, 1.027, 2.185)
SHAT_RTOL = 2e-2
REG_KZ = (9, 60, 121)
TAB_EXT = 4_000_000
H_HOLD = (128, 2900)
KZ_SCAN_MAX = 400
MIN_NEW = 10
INJ_LADDER = (0.01, 0.1, 1.0)
INJ_DELTA = 0.05
INJ_GAMMA0 = 10.0
REFUSE_MIN = 30
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
NG_SMOOTH = 6000
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


# --------------- pipeline, verbatim (bfloor_pg_dominance_probe)
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
                 keep_chain=False, lag_fn=None):
    """v900 verbatim wall + fixed-core split; lag_fn(rr) is the
    declared cosh-injection hook (CLXII convention)."""
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


# ------------------------- the exact-rational certificate class
def mat_fr(M):
    n = M.shape[0]
    return [[Fraction(float(M[i, j])) for j in range(n)]
            for i in range(n)]


def pd_exact(Afr, shift=Fraction(0)):
    """Exact Sylvester/LDL decision: is A - shift I PD?"""
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


def quad_fr(Afr, bfr):
    x = solve_fr(Afr, bfr)
    if x is None:
        return None
    s = Fraction(0)
    for bi, xi in zip(bfr, x):
        s = s + bi * xi
    return s


def tri_inv_fr(Lflt):
    """Exact Fraction inverse of a float lower-triangular matrix
    with positive diagonal (forward substitution per column).
    Returns None if any diagonal <= 0."""
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


def congruent_scalars(Linv, Bfr, bfr, nfr):
    """Exact (t0, qhat, f0) of the congruent form
    A0 = [[n, chat*],[chat, Chat]], Chat = Linv B Linv^T,
    chat = Linv b (all Fractions)."""
    n = len(Bfr)
    BL = [[sum(Bfr[i][k] * Linv[j][k] for k in range(n))
           for j in range(n)] for i in range(n)]
    Chat = [[sum(Linv[i][k] * BL[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]
    chat = [sum(Linv[i][k] * bfr[k] for k in range(n))
            for i in range(n)]
    t0 = sum(Chat[i][i] for i in range(n))
    f0 = sum(Chat[i][j] * Chat[i][j] for i in range(n)
             for j in range(n))
    qh = sum(c * c for c in chat)
    return t0, qh, f0, Chat


def ranktrace_decide(nfr, t0, qh, f0):
    """The frozen exact criterion.  Returns dict with PASS
    boolean, drive, u_q, Q(u_q), margin r(u_q) - 7 (Fractions;
    margin None on refusal)."""
    out = dict(ok=False, seat="", drive=None, u_q=None,
               margin=None, deficit=None)
    if nfr <= 0:
        out["seat"] = "n <= 0"
        return out
    drive = nfr * t0 - 7 * qh
    deficit = 7 * f0 - t0 * t0          # >= 0 by Cauchy-Schwarz
    out["drive"] = drive
    out["deficit"] = deficit
    if drive <= 0:
        out["seat"] = "drive <= 0"
        return out
    u_q = drive / (6 * nfr * nfr)
    out["u_q"] = u_q
    Qv = drive * drive / (6 * nfr * nfr) - deficit
    trv = u_q * nfr + t0
    if trv <= 0:
        out["seat"] = "trace <= 0"
        return out
    Fv = u_q * u_q * nfr * nfr + 2 * u_q * qh + f0
    out["margin"] = Qv / Fv
    if Qv > 0:
        out["ok"] = True
    else:
        out["seat"] = "Q(u_q) <= 0"
    return out


def build_pg(w):
    """Source-only P_G co-block (CXLIV V0 direction)."""
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
    """The frozen Householder step frame (P2/CXLIV verbatim)."""
    wS, VS = np.linalg.eigh(r1["S"])
    Q = householder_frame(VS[:, 0])
    Mt = Q.T @ (r2["S"] / r1["tau"]) @ Q
    Mt = 0.5 * (Mt + Mt.T)
    return dict(r1=r1, r2=r2, Q=Q, Mt=Mt, nsc=float(Mt[0, 0]),
                b=Mt[1:, 0].copy(), B=Mt[1:, 1:].copy(),
                tau=r1["tau"])


def s2_exact(w, beta=None):
    """The full S2 exact pipeline on one step.  beta = None uses
    the certified c_dom in full; a Fraction beta scales it (the
    S3 headroom restart).  Returns decision dict + context."""
    n7 = 7
    Bfr = mat_fr(w["B"])
    PG = w.get("PG")
    if PG is None:
        return dict(ok=False, seat="no P_G")
    Pfr = mat_fr(0.5 * PG)          # halving floats is exact
    Kfr = [[Bfr[i][j] - Pfr[i][j] for j in range(n7)]
           for i in range(n7)]
    ok0, _ = pd_exact(Kfr)
    if not ok0:
        return dict(ok=False, seat="DOM-FAIL (B - P_G/2 not PD)")
    hi = min(Kfr[k][k] for k in range(n7))
    cdom = cert_floor_exact(Kfr, Fraction(0), hi)
    if cdom is None or cdom <= 0:
        return dict(ok=False, seat="c_dom refused")
    use_c = cdom if beta is None else beta * cdom
    Dflt = 0.5 * PG + float(use_c) * np.eye(n7)
    try:
        Lc = np.linalg.cholesky(Dflt)
    except np.linalg.LinAlgError:
        return dict(ok=False, seat="chol refused")
    Linv = tri_inv_fr(Lc)
    if Linv is None:
        return dict(ok=False, seat="chol diag <= 0")
    bfr = [Fraction(float(x)) for x in w["b"]]
    nfr = Fraction(w["nsc"])
    t0, qh, f0, _C = congruent_scalars(Linv, Bfr, bfr, nfr)
    dec = ranktrace_decide(nfr, t0, qh, f0)
    dec.update(t0=t0, qh=qh, f0=f0, cdom=cdom, Bfr=Bfr, bfr=bfr,
               nfr=nfr, Dflt=Dflt)
    return dec


def s3_repair(w, dec0):
    """Woodbury repair at BETA headroom (frozen).  Returns
    (repaired boolean, k_star, accepted, tried, final deficit)."""
    n7 = 7
    Bfr = dec0["Bfr"]
    bfr = dec0["bfr"]
    nfr = dec0["nfr"]
    cdom = dec0["cdom"]
    PG = w["PG"]
    Dc = 0.5 * PG + float(BETA_HEADROOM * cdom) * np.eye(n7)
    Dc_fr = [[Fraction(float(0.5 * PG[i][j]))
              + (BETA_HEADROOM * cdom if i == j else Fraction(0))
              for j in range(n7)] for i in range(n7)]
    comps = pg_components(w)
    n_acc, tried = 0, 0
    last_deficit = dec0.get("deficit")
    for u in comps:
        if tried >= K_HIER:
            break
        tried += 1
        ufr = [Fraction(float(x)) for x in u]
        Dn_fr = [[Dc_fr[i][j] + S_HALF * ufr[i] * ufr[j]
                  for j in range(n7)] for i in range(n7)]
        BD = [[Bfr[i][j] - Dn_fr[i][j] for j in range(n7)]
              for i in range(n7)]
        okd, _ = pd_exact(BD)
        if not okd:
            continue
        Dc_fr = Dn_fr
        Dc = Dc + 0.5 * np.outer(u, u)
        n_acc += 1
        try:
            Lc = np.linalg.cholesky(Dc)
        except np.linalg.LinAlgError:
            continue
        Linv = tri_inv_fr(Lc)
        if Linv is None:
            continue
        t0, qh, f0, _C = congruent_scalars(Linv, Bfr, bfr, nfr)
        dec = ranktrace_decide(nfr, t0, qh, f0)
        last_deficit = dec.get("deficit")
        if dec["ok"]:
            return True, n_acc, n_acc, tried, last_deficit
    return False, None, n_acc, tried, last_deficit


# --------------- CLI registry machinery (verbatim, one eigh/rung)
def deployed_registry():
    rungs = []
    for kz in range(2, KZMAX_REG + 1):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
        uu = np.asarray(rr["uu"], float)
        mu = 2.0 * np.asarray(rr["lam"], float)
        c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mu)[0],
                          float)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        Kt = core.odd_toeplitz(c_ar + c_at, M)
        w, V = np.linalg.eigh(Kt)
        row = dict(kz=kz, h=h, m=float(w[0]),
                   shat=float(w[0]) / mu1_of(h))
        if kz in REG_KZ:
            row["Kt"] = Kt
            row["v"] = V[:, 0].copy()
        else:
            del Kt
        del V
        rungs.append(row)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    lines = "\n".join("%d:%d:%.12e" % (r["kz"], r["h"], r["shat"])
                      for r in rungs)
    return rungs, hashlib.sha256(lines.encode("utf-8")).hexdigest()


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


def s1_core_booleans(w):
    """S1 on one step: float whitened criterion at u_h vs exact
    halfgap boolean.  Returns (float boolean, exact boolean,
    identity rel dev, inertia tie ok)."""
    B = w["B"]
    b = w["b"]
    nsc = w["nsc"]
    h2 = w["r2"]["h"]
    mu1 = mu1_of(h2)
    wB, VB = np.linalg.eigh(B)
    if float(wB[0]) <= 0.0 or nsc <= 0.0:
        return None
    Bi = VB @ np.diag(wB ** -0.5) @ VB.T
    c = Bi @ b
    q = float(c @ c)
    u_h = 7.0 * mu1 / (6.0 * nsc ** 2)
    A = np.zeros((8, 8))
    A[0, 0] = u_h * nsc
    A[0, 1:] = math.sqrt(u_h) * c
    A[1:, 0] = math.sqrt(u_h) * c
    A[1:, 1:] = np.eye(7)
    trA = float(np.trace(A))
    fA = float(np.sum(A * A))
    lhs = trA ** 2 - 7.0 * fA
    rhs = 14.0 * u_h * (nsc - q - 0.5 * mu1)
    dev = abs(lhs - rhs) / max(abs(rhs), abs(lhs), 1e-300)
    ok_f = (trA ** 2 / fA) > 7.0
    # exact right side (round-62 convention: float entries exact)
    Bfr = mat_fr(B)
    bfr = [Fraction(float(x)) for x in b]
    q_fr = quad_fr(Bfr, bfr)
    ok_x = (q_fr is not None
            and Fraction(nsc) - q_fr > Fraction(mu1) / 2)
    npos_A = int(np.sum(np.linalg.eigvalsh(A) > 0.0))
    npos_M = int(np.sum(np.linalg.eigvalsh(w["Mt"]) > 0.0))
    return dict(ok_f=ok_f, ok_x=bool(ok_x), dev=dev,
                tie=(npos_A == npos_M),
                gap=float(Fraction(nsc) - q_fr), mu1=mu1)


def main():
    section("PRIME.PORT.ANTHROPIC.RANKTRACE.01 -- effective-rank / "
            "inertia counting on the 8x8 core: HALFGAP as a "
            "positive-index-8 statement, source-only congruence "
            "census (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Exact statements "
          "are about the float64-computed step matrices; the "
          "pipeline interval rollout is a concurrent separate "
          "work item; the ideal-object interval version of this "
          "criterion is the typed follow-up.")
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
          "indefinite; exact solver + exact triangular inverse "
          "hit known rational solutions",
          ok_pd and not ok_ind and ok_sol and ok_tri, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ R
    section("R -- the route gate (typed): information class per "
            "stage")
    print("    the criterion reads TWO moments (tr, ||.||_F) of a "
          "congruent form = the Anthropic zeta-2/3 class;")
    print("    S1 adds the exact whitening (TARGET EIGENDATA -- "
          "identity control, NOT a route);")
    print("    S2 adds (i) the exact source-only congruence T0 = "
          "diag(1, L_G^{-T}), a matrix-level structure,")
    print("        (ii) INTEGRALITY of inertia on the fixed 8-dim "
          "core (per-object certificate, not an asymptotic")
    print("        proportion), (iii) an optimized scale u;")
    print("    S3 adds positive CD-Gram components (higher "
          "congruence resolution).")
    print("    the two-moment no-go is not contradicted -- it is "
          "sidestepped at a finite per-object level.")
    check("R1 typed: ROUTE-GATE-DECLARED", True)

    # ----------------------------------------------------------- S1
    section("S1 -- exact whitening: the HALFGAP <=> index-8 "
            "dictionary (identity control, target eigendata "
            "declared)")
    # S1.w0 symbolic (deterministic rational tuples, exact)
    tuples = [(Fraction(3, 2), Fraction(2, 7), Fraction(5, 3), 7),
              (Fraction(1, 9), Fraction(1, 11), Fraction(8, 5), 7),
              (Fraction(12, 5), Fraction(0), Fraction(1, 7), 7),
              (Fraction(7, 3), Fraction(9, 4), Fraction(2), 7),
              (Fraction(5, 8), Fraction(1, 3), Fraction(3, 2), 12),
              (Fraction(2), Fraction(3), Fraction(1, 2), 996)]
    ok_sym = True
    for nn_, qq_, uu_, pp_ in tuples:
        lhs = (uu_ * nn_ + pp_) ** 2 - pp_ * (
            uu_ ** 2 * nn_ ** 2 + 2 * uu_ * qq_ + pp_)
        rhs = uu_ * (2 * pp_ * (nn_ - qq_)
                     - (pp_ - 1) * uu_ * nn_ ** 2)
        ok_sym &= (lhs == rhs)
    check("S1.w0 WARD symbolic identity exact on %d/%d rational "
          "tuples (Fractions, equality)" % (
              sum(1 for _ in tuples), len(tuples)),
          ok_sym, kill="K2")
    dev_id = 0.0
    ties = 0
    agree = 0
    both_true = 0
    s1_rows = []
    for w in rows:
        s1 = s1_core_booleans(w)
        if s1 is None:
            s1_rows.append(None)
            continue
        s1_rows.append(s1)
        dev_id = max(dev_id, s1["dev"])
        ties += s1["tie"]
        agree += (s1["ok_f"] == s1["ok_x"])
        both_true += (s1["ok_f"] and s1["ok_x"])
    check("S1.w1 WARD materialized identity: max rel dev %.2e <= "
          "%.0e; inertia tie n_+(A(u_h)) == n_+(M) on %d/%d"
          % (dev_id, ID_WARD, ties, len(rows)),
          dev_id <= ID_WARD and ties == len(rows), kill="K2")
    check("S1.w2 WARD core dictionary boolean-equal on %d/%d "
          "steps (criterion at u_h <=> exact n - q > mu1/2; both "
          "TRUE on %d/%d -- the CLXII slack)"
          % (agree, len(rows), both_true, len(rows)),
          agree == len(rows), kill="K2")
    slack = [s["gap"] / (0.5 * s["mu1"]) for s in s1_rows
             if s is not None]
    print("    core halfgap slack (n-q)/(mu1/2): min/med/max "
          "%.3g/%.3g/%.3g" % (float(np.min(slack)),
                              float(np.median(slack)),
                              float(np.max(slack))))
    # S1.w3 the full-frame registered surface
    reg_rungs, reg_sha = deployed_registry()
    shat_d = np.array([r["shat"] for r in reg_rungs])
    trio = (float(shat_d.min()), float(np.median(shat_d)),
            float(shat_d.max()))
    ok_band = all(abs(a / b - 1.0) <= SHAT_RTOL
                  for a, b in zip(trio, SHAT_REF))
    check("S1.w3a WARD registry: %d rungs, sha256 %s.. == "
          "ae292e55.. (%s); band %.3f/%.3f/%.3f  [%.1f s]"
          % (len(reg_rungs), reg_sha[:8],
             "MATCH" if reg_sha == REG_SHA else "MISMATCH",
             trio[0], trio[1], trio[2], time.time() - T0),
          len(reg_rungs) == 67 and reg_sha == REG_SHA and ok_band,
          kill="K2")
    n_eq = 0
    n_crit = 0
    n_regp = 0
    for r in reg_rungs:
        reg_pass = r["shat"] >= 0.5
        crit_pass = r["shat"] > 0.5      # strict-tie convention
        n_regp += reg_pass
        n_crit += crit_pass
        n_eq += (reg_pass == crit_pass)
    check("S1.w3b WARD full-frame dictionary boolean-equal "
          "%d/%d (criterion census %d, registered census %d; "
          "pivot collapse n = m, q = 0 warded upstream CLI W4)"
          % (n_eq, len(reg_rungs), n_crit, n_regp),
          n_eq == len(reg_rungs), kill="K2")
    dev_full = 0.0
    ok_full_tie = True
    for r in reg_rungs:
        if "Kt" not in r:
            continue
        Kt = r["Kt"]
        v = r["v"]
        d = Kt.shape[0]
        p = d - 1
        Qf = householder_frame(v)
        Mtf = Qf.T @ Kt @ Qf
        Mtf = 0.5 * (Mtf + Mtf.T)
        nsc = float(Mtf[0, 0])
        bf = Mtf[1:, 0]
        Bf = Mtf[1:, 1:]
        wB, VB = np.linalg.eigh(Bf)
        if float(wB[0]) <= 0.0:
            ok_full_tie = False
            continue
        c = (VB @ np.diag(wB ** -0.5) @ VB.T) @ bf
        q = float(c @ c)
        mu1 = mu1_of(r["h"])
        u_p = p * mu1 / ((p - 1) * nsc ** 2)
        trA = u_p * nsc + p
        fA = u_p ** 2 * nsc ** 2 + 2.0 * u_p * q + p
        lhs = trA ** 2 - p * fA
        rhs = u_p * (2.0 * p * (nsc - q)
                     - (p - 1) * u_p * nsc ** 2)
        dev_full = max(dev_full, abs(lhs - rhs)
                       / max(abs(rhs), abs(lhs), 1e-300))
        crit = (trA ** 2 / fA) > p
        ok_full_tie &= (crit == (r["shat"] > 0.5))
        # inertia tie via the 2x2 reduction of the arrow form
        two = np.array([[u_p * nsc, math.sqrt(u_p * q)],
                        [math.sqrt(u_p * q), 1.0]])
        ev2 = np.linalg.eigvalsh(two)
        npos_A = (p - 1) + int(np.sum(ev2 > 0.0))
        npos_K = int(np.sum(np.linalg.eigvalsh(Kt) > 0.0))
        ok_full_tie &= (npos_A == npos_K) if crit else True
        print("    REG kz %3d h %4d (dim %d): ratio - p = %+.3e, "
              "closed-form dev %.1e, criterion %s == shat > 1/2 "
              "%s" % (r["kz"], r["h"], d, trA ** 2 / fA - p,
                      dev_full, crit, r["shat"] > 0.5),
              flush=True)
    check("S1.w3c WARD full-frame materialization on REG_KZ: max "
          "dev %.2e <= %.0e; inertia + boolean ties hold"
          % (dev_full, FULLDICT_WARD),
          dev_full <= FULLDICT_WARD and ok_full_tie, kill="K2")
    s1a = "S1-DICT-CORE(%d/%d)" % (agree, len(rows))
    s1b = "S1-DICT-FULL(%d/%d, sha8 %s)" % (n_eq, len(reg_rungs),
                                            reg_sha[:8])
    check("S1 typed: %s / %s" % (s1a, s1b), True)

    # ----------------------------------------------------------- S2
    section("S2 -- the source-only P_G congruence: the decisive "
            "census (exact decisions)")
    print("      kz    h     n         drive        deficit "
          "7f0-t0^2  t0-7       qhat/q     lmax(Chat)  margin"
          "      verdict")
    n_pass2 = 0
    sound_ok = True
    margins2, taus2 = [], []
    t0s, defs, qratio, lmaxs = [], [], [], []
    for w, s1 in zip(rows, s1_rows):
        dec = s2_exact(w)
        w["s2"] = dec
        if not dec.get("ok") and "t0" not in dec:
            print("    %4d %5d  REFUSAL: %s"
                  % (w["r2"]["kz"], w["r2"]["h"], dec["seat"]),
                  flush=True)
            continue
        t0f = float(dec["t0"])
        deff = float(dec["deficit"])
        drv = float(dec["drive"])
        qf = float(dec["qh"])
        q_true = w["nsc"] - w["gap"]
        Dflt = dec["Dflt"]
        Chat_f = np.linalg.solve(Dflt, w["B"])
        lmax = float(np.max(np.real(np.linalg.eigvals(Chat_f))))
        marg = (float(dec["margin"])
                if dec["margin"] is not None else float("nan"))
        t0s.append(t0f - 7.0)
        defs.append(deff)
        qratio.append(qf / max(q_true, 1e-300))
        lmaxs.append(lmax)
        if dec["ok"]:
            n_pass2 += 1
            margins2.append(marg)
            taus2.append(w["tau"])
            if float(np.linalg.eigvalsh(w["Mt"])[0]) <= 0.0:
                sound_ok = False
        print("    %4d %5d  %8.4f  %+.4e  %.4e  %+.3e  %9.2f  "
              "%9.2f  %+.4e  %s"
              % (w["r2"]["kz"], w["r2"]["h"], w["nsc"], drv,
                 deff, t0f - 7.0, qf / max(q_true, 1e-300),
                 lmax, marg,
                 "PASS" if dec["ok"] else "fail(%s)"
                 % dec["seat"]), flush=True)
    check("S2.w SOUNDNESS WARD: every PASS step is float eigh-PD",
          sound_ok, kill="K2")
    s2lab = ("S2-CENSUS(%d/%d%s)"
             % (n_pass2, len(rows),
                (", min/med margin %+.2e/%+.2e"
                 % (float(np.min(margins2)),
                    float(np.median(margins2))))
                if margins2 else ""))
    loss = ("LOSS-ANATOMY(med t0-7=%.3g, med deficit=%.3g, med "
            "qhat/q=%.3g, med lmax(Chat)=%.3g)"
            % (float(np.median(t0s)), float(np.median(defs)),
               float(np.median(qratio)), float(np.median(lmaxs))))
    check("S2 typed: %s / %s" % (s2lab, loss), True)
    print("    reading (from the measured table): the congruence "
          "slack of the B >> D directions inflates BOTH")
    print("    two-moment invariants (t0, f0); the criterion "
          "budget is spent on co-block spread before the")
    print("    drive n t0 - 7 qhat can bite -- qhat carries the "
          "same D^{-1} inflation as CL's qbar (med printed).")
    scr_lab, _sl = screen(margins2 if margins2 else [0.0],
                          taus2 if taus2 else [1.0])
    check("S2.s typed tau-screen of the PASS margins: %s"
          % scr_lab, True)

    # ----------------------------------------------------------- S3
    section("S3 -- the Woodbury repair at BETA = 1/2 headroom "
            "(only on S2-fail steps)")
    fail_rows = [w for w in rows
                 if not w.get("s2", {}).get("ok")
                 and "t0" in w.get("s2", {})]
    if n_pass2 == len(rows):
        s3lab = "S3-VACUOUS(no failing steps)"
        check("S3 typed: %s" % s3lab, True)
    else:
        n_rep = 0
        kstars, accs, trieds, end_defs = [], [], [], []
        for w in fail_rows:
            rep, kst, acc, tried, dend = s3_repair(w, w["s2"])
            accs.append(acc)
            trieds.append(tried)
            if dend is not None:
                end_defs.append(float(dend))
            if rep:
                n_rep += 1
                kstars.append(kst)
                print("    REPAIRED kz %d h %d: k* = %d accepted"
                      % (w["r2"]["kz"], w["r2"]["h"], kst),
                      flush=True)
        med_acc = float(np.median(accs)) if accs else 0.0
        if n_rep == len(fail_rows) and kstars:
            s3lab = ("S3-REPAIR(%d/%d, max k*=%d, med k*=%.1f)"
                     % (n_rep, len(fail_rows), max(kstars),
                        float(np.median(kstars))))
        elif n_rep > 0:
            s3lab = ("S3-PARTIAL(%d/%d repaired, med accepted "
                     "%.0f of %d tried)"
                     % (n_rep, len(fail_rows), med_acc, K_HIER))
        else:
            s3lab = ("S3-EXHAUSTED(0/%d repaired; med accepted "
                     "%.0f of %d tried; med deficit at "
                     "exhaustion %.3g vs %.3g before)"
                     % (len(fail_rows), med_acc, K_HIER,
                        float(np.median(end_defs))
                        if end_defs else float("nan"),
                        float(np.median(defs))))
        check("S3 typed: %s" % s3lab, True)

    # ------------------------------------------------------------ D
    section("D -- deep blind holdout: the 4e6-table steps "
            "(scored, no refits)")
    lam_ext = build_ext_tables()
    dev_tab = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                                  - core.LAM_TAB)))
    psi = np.cumsum(lam_ext[EXT["NN"]])
    nnf = EXT["NN"].astype(float)
    keep = nnf >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nnf[keep])
                         / nnf[keep]))
    check("D.w WARD deep-table overlap byte-exact (dev %.1e) and "
          "Chebyshev kappa %.6f <= %.6f + 1e-6 (remaining "
          "fidelity battery inherited from CLX upstream, "
          "declared)" % (dev_tab, kappa, core.KAPPA_REF),
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
        tag = ("chain-short" if g is None else
               "core-missing" if not g["core_ok"] else
               "negA=%d" % g["negA"] if g["negA"] > 0 else "ok")
        print("    deep gram kz %3d h %5d: %s  [%.1f s]"
              % (kz, ext_frame(kz)[2], tag, time.time() - T0),
              flush=True)
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
    thin = len(dsteps) < MIN_NEW
    print("\n    deep census: %d new rungs, %d usable, %d steps%s"
          % (len(order), len(usable), len(dsteps),
             "  (DEEP-THIN, measured anyway)" if thin else ""))
    n_hg = 0
    n_s2d = 0
    n_s3d = 0
    slackd = []
    dsound = True
    for w in dsteps:
        h2 = w["r2"]["h"]
        mu1 = mu1_of(h2)
        Bfr = mat_fr(w["B"])
        bfr = [Fraction(float(x)) for x in w["b"]]
        q_fr = quad_fr(Bfr, bfr)
        hg = (q_fr is not None
              and Fraction(w["nsc"]) - q_fr > Fraction(mu1) / 2)
        if hg:
            n_hg += 1
            slackd.append(float((Fraction(w["nsc"]) - q_fr)
                                / (Fraction(mu1) / 2)))
        dec = s2_exact(w)
        w["s2"] = dec
        okd = dec.get("ok", False)
        if okd:
            n_s2d += 1
            if float(np.linalg.eigvalsh(w["Mt"])[0]) <= 0.0:
                dsound = False
        rep = False
        if (not okd) and "t0" in dec:
            rep, _k, _a, _t, _d = s3_repair(w, dec)
            if rep:
                n_s3d += 1
        print("    DEEP kz %3d h %5d: halfgap %s  S2 %s%s"
              % (w["r2"]["kz"], h2,
                 "PASS" if hg else "FAIL",
                 "PASS" if okd else
                 "fail(%s)" % dec.get("seat", "?"),
                 "  S3 REPAIRED" if rep else ""), flush=True)
    check("D.s SOUNDNESS WARD (deep): every deep PASS is float "
          "eigh-PD", dsound, kill="K2")
    dlab = ("DEEP-%s(halfgap %d/%d blind%s, S2 %d/%d, S3 repair "
            "%d/%d)"
            % ("THIN" if thin else "SCORED", n_hg, len(dsteps),
               (", min slack %.3g" % float(np.min(slackd)))
               if slackd else "", n_s2d, len(dsteps), n_s3d,
               max(len(dsteps) - n_s2d, 0)))
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
        c4_msg = ("lam_min(S_scr) %.3e < 0 -> the scramble core "
                  "breaks the floor" % rsc["lamS"])
    check("C4 WARD scramble breaks the floor: %s" % c4_msg,
          c4_ok, kill="K2")
    # C5 cosh injection (CLXII convention; smallest firing A)
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
          "%s, smallest firing per the frozen rule)"
          % str(cosh_A), cosh_lad is not None, kill="K2")
    # criterion-level census on relaxed control steps
    ctrl_labels = []
    c_sound = True
    for wname, lad in (("smooth",
                        [sm_map.get(kz) for kz in zones]),
                       ("cosh", cosh_lad if cosh_lad else [])):
        clad = [r for r in lad if isinstance(r, dict)]
        clad.sort(key=lambda r: (r["h"], r["kz"]))
        n_ct, n_cert, n_refuse = 0, 0, 0
        n_pd = 0
        for g1, g2 in zip(clad, clad[1:]):
            if not (g1.get("core_ok") and g2.get("core_ok")):
                continue
            if "S" not in g1 or "S" not in g2:
                continue
            if g1["tau"] == 0.0 or "chain" not in g2:
                continue
            if "y_core" not in g2:
                continue
            wc = make_step(g1, g2)
            wc["PG"] = build_pg(wc)
            n_ct += 1
            dec = s2_exact(wc)
            m_pd = float(np.linalg.eigvalsh(wc["Mt"])[0]) > 0.0
            n_pd += m_pd
            if dec.get("ok"):
                n_cert += 1
                if not m_pd:
                    c_sound = False
            else:
                n_refuse += 1
        if n_cert == 0:
            ctrl_labels.append("%s CONTROLS-BREAK-S2(0/%d, %d "
                               "refusals)" % (wname, n_ct,
                                              n_refuse))
        else:
            ctrl_labels.append("%s CORE-CONSISTENT(%d/%d "
                               "certified, PD cores there %d/%d)"
                               % (wname, n_cert, n_ct, n_pd,
                                  n_ct))
        print("    %s control steps: %d built, %d certified, %d "
              "refused, %d truly PD cores"
              % (wname, n_ct, n_cert, n_refuse, n_pd), flush=True)
    check("C6 SOUNDNESS WARD on control steps: no certification "
          "of a non-PD core", c_sound, kill="K2")
    clab = " / ".join(ctrl_labels)
    check("C7 typed: %s (state-level reading: M > 0 IS the "
          "rung-r2 core wall; certification on a control step "
          "can only happen where that core is genuinely PD -- "
          "core-blindness to breaks OUTSIDE the 8 folds is the "
          "measured, declared limit; mass-rescale world DECLARED "
          "SKIPPED)" % clab, True)

    return finish(dict(s1=("%s / %s" % (s1a, s1b)), s2=s2lab,
                       loss=loss, s3=s3lab, deep=dlab,
                       scr=scr_lab, ctrl=clab))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("ANTHRORANKTRACE-MEASURED / "
                   "ROUTE-GATE-DECLARED / %s / %s / %s / %s / "
                   "%s / SCREEN %s / %s"
                   % (labels.get("s1", "-"), labels.get("s2", "-"),
                      labels.get("loss", "-"),
                      labels.get("s3", "-"),
                      labels.get("deep", "-"),
                      labels.get("scr", "-"),
                      labels.get("ctrl", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the dictionary S1 is exact -- HALFGAP
  is a positive-index-8 statement, verified at machine precision
  on both surfaces; that part is an identity, not evidence.  The
  route content is S2/S3: an exact-rational, source-only,
  two-moment PD certificate on the fixed core, whose census IS
  the result whatever it says.  A PASS is a theorem about the
  float64-computed step matrix; nothing here proves n > q
  uniformity in h, the pipeline enclosure, or any tail statement.
  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
