#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ub4_identity_or_measurement_probe -- PRIME.PORT.UB4.IDENTITY.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the DECISIVE follow-up to CLXXIII (UB4-CLOSED).
CLXXIII measured that the Jacobi diagonal equilibration E =
diag(Chat_ii^{-1/2}) is the ENTIRE story behind the surface-wide
source-only r = 4 moment certificate (pure Jacobi on B with NO
P_G: 39/39, med 0.636).  THE QUESTION OF THIS PROBE: is UB_4 < 1
after equilibration an IDENTITY / STRUCTURAL LAW of the ladder
class -- a classical statement about the off-diagonal mass of the
equilibrated form (Gershgorin / Brauer-Ostrowski / Frobenius
class) -- or a genuinely ARITHMETIC measurement?  2026-08-11.)

THE CANONICAL OBJECT (frozen).  For a symmetric matrix W with
positive diagonal let corr(W) = E W E, E = diag(W_ii^{-1/2}): the
CORRELATION FORM, unit diagonal BY CONSTRUCTION, r_ij =
W_ij / sqrt(W_ii W_jj).  corr is a congruence by an exactly
invertible diagonal, so inertia(corr(W)) == inertia(W) (Sylvester)
and UB_4(corr(W)) < 1 => n_+ = 8 => W > 0, exactly the CLXXIII
certificate logic.  KEY ANALYTIC SIMPLIFICATION (proved by ward
P2): the CLXXIII head-scale dial u is ELIMINATED -- corr of the
u-scaled form is u-INDEPENDENT (row/col scaling cancels), so the
whole CLXXIII u-grid collapses to a single canonical matrix per
step.  TWO FROZEN FORMS per step (same PD content, different
coordinates; both source-only, only matrix ENTRIES consumed):
  FS  the FOLD form  R = corr(S_2 / tau_1): the core Schur wall
      itself in fold coordinates (folds CORE_J), NO Householder
      frame, NO u, NO P_G -- the frame-free canonical object;
  FM  the FRAMED form R = corr(Mt), Mt = Q^T (S_2/tau_1) Q the
      deployed P2/P3 step matrix (head x0 = soft direction,
      co-block x1..x7) -- corr(Mt) == corr of the CLXXIII
      pure-Jacobi (VC) scaled form at EVERY u (ward P2).
WINNER (frozen rule): larger core census of UB_4 < 1 - CERT_EPS;
tie by smaller median of min(UB_4, cap); remaining tie FS < FM.

(a) THE ANALYTIC FORM (block P).  With R = I + O (O = the
off-diagonal correlation matrix, tr O = 0), the CMS moments are
EXACTLY binomial sums of the off-diagonal power sums p_j =
tr(O^j):  m_k = tr(R^k) = sum_j C(k,j) p_j,  p_0 = 8, p_1 = 0;
p_2 = 2 sum_{i<j} r_ij^2 is the off-diagonal L2 MASS, p_3 = 6
sum_{i<j<k} r_ij r_jk r_ki the triangle CYCLE SUM, etc.  So
UB_4 < 1 is EXACTLY the explicit inequality
    Psi_4(p_2, ..., p_8) < 1,
Psi_4 = the CMS node-0 canonical-representation mass built from
the binomial moments -- an inequality in the 28 off-diagonal
correlations r_ij, with the closed r = 1 tie (ward P4):
    UB_1(R) = 8 p_2 / (8 + p_2)  and  UB_1 < 1  <=>  p_2 < 8/7,
which is EXACTLY the classical traceless-Frobenius PD bound
lam_min(O) >= -sqrt(7 p_2 / 8) > -1 -- the r = 1 CMS class on the
equilibrated form IS the off-diagonal-L2 statement.  Wards:
P1 binomial moment identity to machine precision on all steps
(and |tr O| tiny); P2 u-invariance + corr(VC form) == corr(Mt);
P3 UB_4 from binomial-reconstructed moments == direct UB_4;
P4 the r = 1 closed-form tie.  Census of UB_4 per form; exact
NEWTON-STURM backstop (Fractions, diagonal congruence by exact
rationals Fraction(float(e_i))) on every winner core crosser
(kill); winner r_min histogram; tau-screen of winner margins;
P5b U-CONTENT census (typed, disclosed amendment A1): on every
core/deep resister of the scale-free form, the CLXXIII VC
best-u value next to it -- measuring exactly what certification
content the head-scale dial carries beyond the r_ij.

(b) THE STRUCTURAL TEST (block Q).  Classical candidates on the
winner form, each an unconditionally SOUND PD certificate:
  CAND-G   Gershgorin: g = max_i s_i, s_i = sum_{j!=i} |r_ij|;
           certifies iff g < 1 (lam_min(R) >= 1 - g);
  CAND-B   Brauer-Cassini (Ostrowski class): certifies iff
           max_{i<j} s_i s_j < 1 (lam_min >= 1 - max sqrt(s_i s_j));
  CAND-L2  traceless Frobenius: certifies iff p_2 < 8/7
           (== the r = 1 CMS bar, ward P4);
  CAND-DEC lag-correlation decay on FS (typed, not a
           certificate): per step the OLS slope of log(mean
           |r_ij| at fold-position lag d) vs d, d = 1..7.
BEFORE/AFTER: the same Gershgorin ratio on the RAW form (max_i
sum_{j!=i}|W_ij| / W_ii) next to g on corr(W) -- the round-60
probe (bfloor_christoffel_congruence) measured the raw-B battery
CERT-DEAD (best bound -88); this table shows exactly what
equilibration changed.  Per-candidate census core + deep,
certified bound vs the needed inequality, margins min/med/max.
BINDING ANATOMY: per step the top-|r_ij| pairs; the modal top-1
pair and its share of steps; the lag-1 share of p_2 (FS).

(c) THE ALL-H SHAPE (block H).  Dictionary ward H1 (kill): the
core block of A = I - G at the median step reproduces from the
CD-chain Christoffel kernel at the folded negative nodes
(B_core == I - sqrt(v_i v_j) sum_k P_ik P_jk to machine
precision) -- so every r_ij is an explicit arch+atom
lag-correlation functional of the deployed window data, Schur
complemented over the non-core folds.  The probe PRINTS the
sharpest all-h statement this program can now name (with the
measured constants and the binding pairs), and block D measures
its deep behavior: OLS trends of p_2, UB_4, max|r_ij|, g vs
log h across core + deep, and the deep binding-pair census.

(d) GATES.  Tau-screen on every margin family (winner margins;
best-candidate margins where the positive census allows).
WALL-BLINDNESS / discrimination: the criterion-level census on
the smooth and cosh control ladders (the CLXXIII seats DOM-FAIL
cannot exist here -- there is no dominance gate; the declared
expectation is that the discrimination moves to the corr
refusal seat diag <= 0 and to the UB_4 >= 1 bar itself, both
censused); Epstein + scramble fire at rung level (C2), scramble
core dead -> C4 disclosed, Epstein criterion-level NA (single
control rung, no step pair -- disclosed); SOUNDNESS (kill): no
certificate (UB_4 or classical candidate) on a step whose core
is not truly PD -- classical candidates are unconditionally
sound by construction, the CMS side is validity-warded (M1).
ANTI-CIRCULARITY: corr consumes only DIAGONAL + off-diagonal
ENTRIES of the computed step matrices -- no sigma_h, no defect
eigenvector, no target eigendata in any construction (FS is even
frame-free; FM's Householder frame is the deployed P2/P3 step
convention inherited verbatim); float eigensolves appear only in
soundness wards and printed context; the ward battery is
synthetic (seeded ward-RNG, declared).

FROZEN PROTOCOL (pipeline verbatim from CLXXIII =
ub4_congruence_upgrade_probe = CLXIV = CLXIII = CXLIV chain;
moment machine, guards, battery verbatim from CLXIV):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1-W3 ladder wards (42 rungs, >= 30 full-core,
     truth all-PSD, >= 20 steps); W4 P2/P3 ledger reproduction;
     W6 machine wards (exact LDL accepts PD / refuses
     indefinite).  NO P_G anywhere in this probe (declared): the
     construction is P_G-free, so the CXLIV dominance ward is
     out of scope here.

 M   MOMENT MACHINE WARDS (kill -> WARD-BROKEN): M1 validity
     battery (NW_RAND + NW_ARROW seeded matrices, declared
     ward-RNG; every non-refusing UB_r >= n_{<=0} - VAL_TOL);
     M2 r = 1 closed-form tie; M3 float NEWTON-STURM == eigh on
     the battery subsample.

 R0  PREDECESSOR REPRODUCTION (kill -> WARD-BROKEN): the CLXXIII
     pure-Jacobi arm VC (D = diag(B), co-block corr + frozen
     u-grid) reproduces census len(rows)/len(rows) and median
     UB_4 == 0.636 (rtol 5e-2).

 P   THE ANALYTIC FORM (wards P1-P4 kill; censuses typed).
 Q   THE STRUCTURAL CANDIDATES (typed).
 H   THE DICTIONARY + ALL-H STATEMENT (H1 kill; statement typed).
 D   DEEP BLIND HOLDOUT (typed + soundness kill): CLXXIII deep
     machinery verbatim (4e6 table byte-exact + kappa guard);
     winner form scored blind, exact backstop on deep crossers;
     candidate censuses + trends.
 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth; C1
     smooth fires; C2 Epstein + scramble at kz 9 fire; C3
     smooth-B0 exact refusal >= REFUSE_MIN; C4 scramble core
     disclosed; C5 cosh fires (smallest ladder amplitude);
     criterion-level census on smooth + cosh steps with refusal
     seats; C6 soundness kill.

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 reproduction /
machine / analytic / dictionary / backstop / soundness / control
wards (W4, W6, M1-M3, R0, P1-P4, WIN backstop, H1, D soundness,
C0-C6) -> WARD-BROKEN.  All census blocks are typed
measurements, never kills.

HONEST OUTCOMES (frozen enum, decided on the winner form):
  UB4-IDENTITY   -- some classical candidate (G / B / L2)
                    certifies on ALL core AND ALL deep steps:
                    the surface result is an identity-grade
                    theorem of the classical class, stated with
                    constants;
  UB4-STRUCTURED -- no classical closure, but the binding
                    correlations are organized: modal top-1 pair
                    share >= MODAL_MIN on core, OR median lag-1
                    share of p_2 >= LAG1_MIN (FS);
  UB4-ARITHMETIC -- the inequality is genuinely arithmetic: the
                    honest frontier, reported with the
                    binding-correlation anatomy.

VERDICT (frozen enum): UB4IDENT-MEASURED with typed sublabels
MACHINE-WARDED(...), REPRO(VC ...), ANALYTIC(...), FORMS(...),
WINNER(...), UCONTENT(...), RMIN(...), BACKSTOP(...),
CANDIDATES(...), BEFORE/AFTER(...), BINDING(...), OUTCOME(...),
ALLH(...), DEEP-SCORED(...), SCREEN(...), CONTROLS(...); else
PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2); R_MAX
= 4; U_GRID_J = 8 (2^j, j = -8..8, VC reproduction only);
CERT_EPS = 1e-6; RES_TOL = 1e-8; W_TOL = 1e-10; IMAG_TOL = 1e-8;
VAL_TOL = 1e-6; R1_TOL = 1e-8; NW_RAND = 500; NW_ARROW = 100;
WARD_SEED = 20260811 (declared ward-RNG); REFUSE_MIN = 30;
INJ_LADDER = (0.01, 0.1, 1.0); INJ_DELTA = 0.05; INJ_GAMMA0 =
10.0; TAB_EXT = 4_000_000; H_HOLD = (128, 2900); KZ_SCAN_MAX =
400; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; CTRL_KZ = 9; scramble
seed 1; REPRO_VC_MED = 0.636 (rtol 5e-2, census must be full);
BINOM_TOL = 1e-9 (rel); TRO_TOL = 1e-10; UINV_TOL = 1e-12;
CORR_TIE_TOL = 1e-12; UB_TIE_TOL = 1e-6 (rel); R1_TIE_TOL =
1e-10; DICT_TOL = 1e-10; MODAL_MIN = 0.5; LAG1_MIN = 0.5;
FLOOR_CAP = 1e9; L2_BAR = 8/7 exact; representative steps =
first/median/last by h; winner tie order FS < FM.  Runtime cap
declared: 15 min.

NO-GO COMPLIANCE (frozen): no rank-1 approximation of the core;
no fit where an identity is claimed; exact-rational decision
classes per the CXLIV mandate (every certification anchored by
the exact NEWTON-STURM backstop on the exact congruent form);
the Anthropic two-moment no-go is engaged head-on by ward P4:
the two-moment class on the equilibrated form IS p_2 < 8/7, and
the r_min histogram measures exactly how far beyond it the
certificate reads.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke
run of this script.  It ran green through every ward and every
census and CRASHED at the very last C-block label on a printf
argument-count bug (a pure formatting error in the CONTROLS
string; zero decisions, bars or censuses touched -- all C0-C5
wards and both criterion-level control censuses had already
printed).  TWO post-smoke edits, both disclosed: A1 (typed-only
addition, no bar/band/enum/rule moved) the P5b/D U-CONTENT
census -- the smoke measured that the scale-free forms do NOT
close the full surface (FS 2/39; FM 37/39 core, 23/27 deep)
while CLXXIII's u-grid VC arm closes 39/39 (R0 reproduced med
0.6365), so the head-scale dial demonstrably carries
certification content and the honest probe must print the VC
value on every resister; A2 the printf fix itself.  Smoke
numbers (all bars FROZEN BEFORE the smoke and unmoved):
pipeline min lam_min(B) 0.6790, gap 0.0520/0.8875; battery
2400/2400, r = 1 tie 0.0, NEWTON-STURM == eigh; R0 VC 39/39 med
0.6365; P1 binomial identity max rel dev 3.1e-16, |tr O| max
1.0e-15; P2 u-invariance 0.0 and corr(VC form) == corr(Mt)
4.4e-16 -- the u-grid provably collapses on the corr form; P3
UB tie 5.9e-08; P4 r = 1 closed-form tie 1.7e-16; FORMS FS 2/39
(med 1.31), FM 37/39 (med 0.7408), WINNER FM; backstop 37/37
exact PD; RMIN r3:6, r4:31, NONE:2; screen PASS(+0.043).  THE
HEADLINE IS A CLEAN NEGATIVE ON EVERY CLASSICAL CANDIDATE:
Gershgorin 0/39 (g 4.25/4.77/5.42 vs bar 1), Brauer 0/39 (med
4.68), L2 0/39 (p_2 13.8/18.7/23.9 vs bar 8/7) -- and since the
co-block correlation row sums alone exceed the bar at every
head scale, NO u rescues a classical certificate: UB_4 < 1 is
carried by the SIGNED cycle sums (p_3 med +59.3, p_4 med +247
against p_2 med 18.7), not by off-diagonal smallness;
BEFORE/AFTER raw Gershgorin med 23.0 -> corr med 4.77 (the
diagonal-scale spread was the bulk of the round-60 raw failure,
but a genuine ~4.8x coherent correlation mass remains above the
classical bar); BINDING modal top-1 pair x1-x2 share 0.769
(census x1-x2:30, x1-x3:8, x2-x3:1), lag-1 share of p_2 med
0.292, FS decay slope med -0.05 (R2 0.86: flat, NO lag-decay
law); OUTCOME on the frozen rule: UB4-STRUCTURED.  H1
dictionary ward 1.2e-15.  DEEP: 23/27 crossed (med 0.827,
backstop 23/23), candidates 0/27 everywhere, modal deep pair
x1-x2 share 0.81, trends all flat (log p_2 slope -0.01, log
UB_4 +0.02, g -0.04, max|r| -0.002).  CONTROLS C0-C5 green
(smooth fires 42/42, Epstein neg(A) 55, scramble neg(A) 37 ->
C4 disclosed skip, cosh A = 0.01 fires 39/42, C3 refusal
35/35); the criterion-level smooth/cosh censuses printed before
the label crash and the frozen run re-measures them.  Runtime
~111 s (cap holds).  A3 (disclosed): the FIRST frozen run
completed EVERY check green (0 FAIL; criterion-level controls:
smooth cert 0/32 with refuse diag<=0 x31 + UB_4 >= 1 x1, cosh
cert 1/39 on a truly-PD core, gersh-cert 0 everywhere) and then
crashed on a second printf argument-count bug in the final
VERDICT assembly line; the fix is again purely a format string
(one %s added), zero decisions, bars, censuses or enums
touched; the complete rerun below is the frozen run of record.
Fail-first preserved: nothing was weakened; enums, bars and
rules are exactly as frozen above.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1:
(i) window memoization per (kz, seed); (ii) Householder frame as
P2/CXLIV; (iii) moments by float matrix powers (k <= 8); CMS
construction, guards and fallback chain verbatim CLXIV; (iv) VC
reproduction u0 = drive/(6 n^2) if drive > 0 else t0/(7 n), grid
u0 2^j (CLXIV S2 convention, reproduction only -- the canonical
forms are u-free); (v) NEWTON-STURM exact backstop verbatim
CLXIV (squarefree + Sturm in Fractions, count in (-inf, 0], PD
iff count 0 and p(0) != 0), on R_exact = E_fr W_fr E_fr with
E_fr = diag(Fraction(float(W_ii^{-1/2}))); (vi) deep frame/gram
= deep_blind_holdout_probe verbatim; (vii) strict inequalities
in all exact decisions; (viii) lag positions on FS = index in
CORE_J (folds 2,4,...,16), lag d = position difference.

NO RH claim: every census here is a SURFACE measurement about
the float64-computed step matrices of the deployed ladder; a
crossing is (via the exact backstop) a theorem about the
computed step matrix, never about the ideal object; the all-h
statement is NAMED, not proved -- nothing here proves n > q
uniformity in h, the pipeline enclosure, or any tail statement.
No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control and the frozen-seed ward battery; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core
machinery verbatim from the CLXXIII = CLXIV = CLXIII = CXLIV
chain; moment machine verbatim from anthropic_moment_inertia
(CLXIV); deep machinery from deep_blind_holdout_probe; cosh
signature via CLXII; the raw-B classical battery context is
bfloor_christoffel_congruence (round 60, CERT-DEAD); Gershgorin,
Brauer-Cassini ovals, the traceless-Frobenius eigenvalue bound
and Jacobi equilibration are the declared classical methods.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/ub4_identity_or_measurement_probe.py
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
REPRO_VC_MED = 0.636
REPRO_RTOL = 5e-2
BINOM_TOL = 1e-9
TRO_TOL = 1e-10
UINV_TOL = 1e-12
CORR_TIE_TOL = 1e-12
UB_TIE_TOL = 1e-6
R1_TIE_TOL = 1e-10
DICT_TOL = 1e-10
MODAL_MIN = 0.5
LAG1_MIN = 0.5
FLOOR_CAP = 1e9
L2_BAR = 8.0 / 7.0
FORM_NAMES = ("FS", "FM")
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


# --------------- pipeline, verbatim (CLXXIII / CLXIV / CXLIV chain)
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
        out["Bcore"] = B.copy()
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


def cms_nodes_once(ms, r):
    """CLXIV cms_ub_once, additionally returning nodes/weights."""
    if r == 1:
        m0, m1, m2 = ms[0], ms[1], ms[2]
        if m2 <= 0:
            return None
        if m1 > 0:
            ub = m0 - m1 * m1 / m2
            return ub, np.array([0.0, m2 / m1]), np.array(
                [ub, m1 * m1 / m2])
        return m0, np.array([0.0]), np.array([m0])
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
    return float(np.sum(wts[nodes <= 0.0])), nodes, wts


def cms_ub_once(ms, r):
    got = cms_nodes_once(ms, r)
    return None if got is None else got[0]


def cms_ub(ms, r):
    for rr in range(r, 0, -1):
        ub = cms_ub_once(ms[:2 * rr + 1], rr)
        if ub is not None:
            return ub
    return None


def cms_detail(ms, r):
    for rr in range(r, 0, -1):
        got = cms_nodes_once(ms[:2 * rr + 1], rr)
        if got is not None:
            return (rr,) + got
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


# --------------- the VC reproduction arm (CLXXIII verbatim)
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
    try:
        Lc = np.linalg.cholesky(0.5 * (Dflt + Dflt.T))
    except np.linalg.LinAlgError:
        return None
    Li = np.linalg.solve(Lc, np.eye(7))
    Chat = Li @ w["B"] @ Li.T
    Chat = 0.5 * (Chat + Chat.T)
    chat = Li @ w["b"]
    return dict(Lc=Lc, Chat=Chat, chat=chat)


def ub_grid(nsc, cvec, Cmat, r):
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


def vc_value(w):
    """CLXXIII variant VC verbatim: D = diag(B), best-grid UB_4."""
    dg = np.diag(w["B"]).copy()
    if float(np.min(dg)) <= 0.0:
        return float("inf")
    cg = congruence_of(w, np.diag(dg))
    if cg is None:
        return float("inf")
    return ub_grid(w["nsc"], cg["chat"], cg["Chat"], R_MAX)


# ------------------- the correlation forms (this probe)
def corr_of(W):
    dg = np.diag(W).copy()
    if float(np.min(dg)) <= 0.0:
        return None
    e = 1.0 / np.sqrt(dg)
    R = e[:, None] * W * e[None, :]
    return 0.5 * (R + R.T)


def form_mat(w, fm):
    if fm == "FS":
        S = w["r2"]["S"] / w["tau"]
        return 0.5 * (S + S.T)
    return w["Mt"]


def opower_sums(R, kmax=2 * R_MAX):
    O = R - np.eye(R.shape[0])
    ps = [float(R.shape[0])]
    P = np.eye(R.shape[0])
    for _k in range(kmax):
        P = P @ O
        ps.append(float(np.trace(P)))
    return ps


def binom_moments(ps, kmax=2 * R_MAX):
    ms = []
    for k in range(kmax + 1):
        ms.append(float(sum(math.comb(k, j) * ps[j]
                            for j in range(k + 1))))
    return ms


def score_form(Mat):
    R = corr_of(Mat)
    if R is None:
        return dict(val=float("inf"), seat="diag<=0", R=None)
    ms = power_moments(R, 2 * R_MAX)
    ub = cms_ub(ms, R_MAX)
    if ub is None:
        return dict(val=float("inf"), seat="cms-refuse", R=R)
    return dict(val=ub, seat="", R=R)


def rmin_of_R(R):
    ms = power_moments(R, 2 * R_MAX)
    for r in range(1, R_MAX + 1):
        ub = cms_ub(ms[:2 * r + 1], r)
        if ub is not None and ub < 1.0 - CERT_EPS:
            return r
    return None


def gersh_stats(R):
    n = R.shape[0]
    Aabs = np.abs(R - np.eye(n))
    s = Aabs.sum(axis=1)
    g = float(np.max(s))
    br = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            br = max(br, float(s[i] * s[j]))
    return g, math.sqrt(br), s


def gersh_raw(W):
    n = W.shape[0]
    dg = np.diag(W)
    if float(np.min(dg)) <= 0.0:
        return float("inf")
    Aabs = np.abs(W - np.diag(dg))
    return float(np.max(Aabs.sum(axis=1) / dg))


def top_pairs(R, k=3):
    n = R.shape[0]
    off = []
    for i in range(n):
        for j in range(i + 1, n):
            off.append((abs(float(R[i, j])), i, j))
    off.sort(reverse=True)
    return off[:k]


def pair_label(fm, i, j):
    if fm == "FS":
        return "f%d-f%d" % (CORE_J[i], CORE_J[j])
    return "x%d-x%d" % (i, j)


def lag1_share(R):
    n = R.shape[0]
    p2 = 0.0
    l1 = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            v = 2.0 * float(R[i, j]) ** 2
            p2 += v
            if j - i == 1:
                l1 += v
    return (l1 / p2) if p2 > 0 else float("nan")


def decay_slope(R):
    n = R.shape[0]
    xs, ys = [], []
    for d in range(1, n):
        vals = [abs(float(R[i, i + d])) for i in range(n - d)]
        m = float(np.mean(vals))
        if m > 0:
            xs.append(float(d))
            ys.append(math.log(m))
    if len(xs) < 3:
        return float("nan"), float("nan")
    _a, sl, r2 = ols_line(xs, ys)
    return sl, r2


def backstop_corr_exact(Mat):
    """Exact NEWTON-STURM PD decision of corr(Mat): exact
    diagonal congruence by Fraction(float(e_i)) on the Fraction
    entries.  None on refusal."""
    dg = np.diag(Mat)
    if float(np.min(dg)) <= 0.0:
        return None
    n = Mat.shape[0]
    efr = [Fraction(float(1.0 / math.sqrt(float(dg[i]))))
           for i in range(n)]
    Mfr = mat_fr(Mat)
    Rfr = [[efr[i] * Mfr[i][j] * efr[j] for j in range(n)]
           for i in range(n)]
    return newton_sturm_pd_exact(Rfr)


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


def print_R_anatomy(R, fm, tag):
    n = R.shape[0]
    _g, _b, s = gersh_stats(R)
    print("      %s: R (unit diagonal; row sums s_i on the "
          "right):" % tag)
    labels = ([("f%d" % j) for j in CORE_J] if fm == "FS"
              else [("x%d" % i) for i in range(n)])
    for i in range(n):
        print("        %-3s %s | s_i %.3f"
              % (labels[i],
                 " ".join("%+.3f" % R[i, j] for j in range(n)),
                 s[i]))
    ps = opower_sums(R)
    print("        p_2..p_8: %s"
          % "  ".join("%+.3e" % x for x in ps[2:]))
    det = cms_detail(power_moments(R, 2 * R_MAX), R_MAX)
    if det is not None:
        rr, ub, nodes, wts = det
        print("        CMS r=%d: UB %.4f  nodes %s  weights %s"
              % (rr, ub,
                 " ".join("%+.3f" % x for x in nodes),
                 " ".join("%+.3f" % x for x in wts)))
    tp = top_pairs(R)
    print("        top |r_ij|: %s"
          % "  ".join("%s %.3f" % (pair_label(fm, i, j), a)
                      for a, i, j in tp))


def main():
    section("PRIME.PORT.UB4.IDENTITY.01 -- identity or "
            "measurement: the analytic form of UB_4 < 1 on the "
            "equilibrated congruent form, the classical "
            "candidates, the all-h shape (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  Float-level "
          "censuses with the CLXIV validity battery; every "
          "certification anchored by the exact NEWTON-STURM "
          "backstop on the exact congruent form.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + P2/P3 reproduction "
            "(P_G-free probe, declared)")
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
    ok_pd, _ = pd_exact(mat_fr(np.array([[2.0, 1.0], [1.0, 2.0]])))
    ok_ind, _ = pd_exact(mat_fr(np.array([[1.0, 2.0],
                                          [2.0, 1.0]])))
    check("W6 MACHINE WARDS: exact LDL accepts PD / refuses "
          "indefinite", ok_pd and not ok_ind, kill="K2")
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
    section("R0 -- CLXXIII reproduction (pure-Jacobi arm VC: "
            "co-block corr + frozen u-grid)")
    vc_vals = []
    n_vc = 0
    for w in rows:
        v = vc_value(w)
        vc_vals.append(min(v, FLOOR_CAP))
        if v < 1.0 - CERT_EPS:
            n_vc += 1
    vc_med = float(np.median(vc_vals))
    check("R0.1 WARD VC reproduces CLXXIII: census %d/%d (full) "
          "and med UB_4 %.4f == %.3f (rtol %.0e)"
          % (n_vc, len(rows), vc_med, REPRO_VC_MED, REPRO_RTOL),
          n_vc == len(rows)
          and abs(vc_med / REPRO_VC_MED - 1.0) <= REPRO_RTOL,
          kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ P
    section("P -- the analytic form: R = I + O, binomial moment "
            "identity, u-elimination, the two-form census")
    dev_binom = 0.0
    dev_tro = 0.0
    dev_uinv = 0.0
    dev_ctie = 0.0
    dev_ubtie = 0.0
    dev_r1tie = 0.0
    recs = {fm: [] for fm in FORM_NAMES}
    print("      kz    h   UB4-FS  UB4-FM    p2(FS)  g(FS)  "
          "brauer  sq(7p2/8)  gershRAW   lmin(R)")
    for w in rows:
        per = {}
        for fm in FORM_NAMES:
            Mat = form_mat(w, fm)
            rec = score_form(Mat)
            rec["Mat"] = Mat
            if rec["R"] is not None:
                R = rec["R"]
                ps = opower_sums(R)
                dev_tro = max(dev_tro, abs(ps[1]))
                ms_d = power_moments(R, 2 * R_MAX)
                ms_b = binom_moments(ps)
                for k in range(2 * R_MAX + 1):
                    dev_binom = max(
                        dev_binom, abs(ms_d[k] - ms_b[k])
                        / max(1.0, abs(ms_d[k])))
                ub_b = cms_ub(ms_b, R_MAX)
                if math.isfinite(rec["val"]) and ub_b is not None:
                    dev_ubtie = max(
                        dev_ubtie, abs(rec["val"] - ub_b)
                        / max(1.0, abs(rec["val"])))
                ub1 = cms_ub_once(ms_d[:3], 1)
                closed = 8.0 * ps[2] / (8.0 + ps[2])
                if ub1 is not None:
                    dev_r1tie = max(
                        dev_r1tie, abs(ub1 - closed)
                        / max(1.0, abs(closed)))
                rec["ps"] = ps
                g, br, _s = gersh_stats(R)
                rec["g"] = g
                rec["brauer"] = br
                rec["fro"] = math.sqrt(7.0 * ps[2] / 8.0)
                rec["graw"] = gersh_raw(Mat)
                rec["lmin"] = float(np.linalg.eigvalsh(R)[0])
                rec["top"] = top_pairs(R)
            per[fm] = rec
            recs[fm].append(rec)
        # u-elimination wards on FM (corr of VC scaled form)
        dgB = np.diag(w["B"]).copy()
        if float(np.min(dgB)) > 0.0 and per["FM"]["R"] is not None:
            cg = congruence_of(w, np.diag(dgB))
            if cg is not None:
                A0 = assemble_form(w["nsc"], cg["chat"],
                                   cg["Chat"])
                Rvc = corr_of(A0)
                if Rvc is not None:
                    dev_ctie = max(dev_ctie, float(np.max(
                        np.abs(Rvc - per["FM"]["R"]))))
                    for u in (0.25, 4.0):
                        Ru = corr_of(scaled(A0, u))
                        if Ru is not None:
                            dev_uinv = max(dev_uinv, float(np.max(
                                np.abs(Ru - Rvc))))
        fs, fm_ = per["FS"], per["FM"]
        print("    %4d %4d  %s  %s   %s  %s  %s   %s    %s   %s"
              % (w["r2"]["kz"], w["r2"]["h"],
                 fmt_ub(fs["val"]), fmt_ub(fm_["val"]),
                 ("%7.3f" % fs["ps"][2]) if "ps" in fs else "   ref",
                 ("%5.2f" % fs["g"]) if "g" in fs else "  ref",
                 ("%5.2f" % fs["brauer"]) if "brauer" in fs
                 else "  ref",
                 ("%5.2f" % fs["fro"]) if "fro" in fs else "  ref",
                 ("%7.2f" % fs["graw"]) if "graw" in fs
                 else "    ref",
                 ("%+.3f" % fs["lmin"]) if "lmin" in fs
                 else "  ref"), flush=True)
    check("P1 WARD binomial moment identity m_k = sum C(k,j) p_j "
          "on every step and form: max rel dev %.2e <= %.0e; "
          "|tr O| max %.2e <= %.0e"
          % (dev_binom, BINOM_TOL, dev_tro, TRO_TOL),
          dev_binom <= BINOM_TOL and dev_tro <= TRO_TOL,
          kill="K2")
    check("P2 WARD u-ELIMINATION: corr(scaled VC form, u) is "
          "u-independent (max dev %.2e <= %.0e) and == corr(Mt) "
          "(max dev %.2e <= %.0e) -- the CLXXIII u-grid collapses"
          % (dev_uinv, UINV_TOL, dev_ctie, CORR_TIE_TOL),
          dev_uinv <= UINV_TOL and dev_ctie <= CORR_TIE_TOL,
          kill="K2")
    check("P3 WARD UB_4 from binomial-reconstructed moments == "
          "direct UB_4: max rel dev %.2e <= %.0e"
          % (dev_ubtie, UB_TIE_TOL), dev_ubtie <= UB_TIE_TOL,
          kill="K2")
    check("P4 WARD r = 1 closed form UB_1 = 8 p_2/(8 + p_2) "
          "(max rel dev %.2e <= %.0e): UB_1 < 1 <=> p_2 < 8/7 "
          "== the traceless-Frobenius PD bar (the two-moment "
          "class IS the off-diagonal-L2 statement)"
          % (dev_r1tie, R1_TIE_TOL), dev_r1tie <= R1_TIE_TOL,
          kill="K2")
    cens = {}
    meds = {}
    for fm in FORM_NAMES:
        vals = [r["val"] for r in recs[fm]]
        cens[fm] = sum(1 for x in vals if x < 1.0 - CERT_EPS)
        meds[fm] = float(np.median([min(x, FLOOR_CAP)
                                    for x in vals]))
        print("    %s: census %d/%d  med UB_4 %.4g"
              % (fm, cens[fm], len(rows), meds[fm]))
    win = min(FORM_NAMES,
              key=lambda f: (-cens[f], meds[f],
                             FORM_NAMES.index(f)))
    wrecs = recs[win]
    n_win = cens[win]
    check("P5 typed: FORMS(FS %d/%d med %.4g; FM %d/%d med "
          "%.4g) / WINNER(%s)"
          % (cens["FS"], len(rows), meds["FS"], cens["FM"],
             len(rows), meds["FM"], win), True)
    # u-content census (A1, typed): what the CLXXIII head-scale
    # dial repairs beyond the scale-free correlation form
    n_urep = 0
    n_resist = 0
    for w, rec in zip(rows, recs["FM"]):
        if rec["val"] < 1.0 - CERT_EPS:
            continue
        n_resist += 1
        vcv = vc_value(w)
        if vcv < 1.0 - CERT_EPS:
            n_urep += 1
        print("    U-CONTENT core resister kz %d h %d: corr UB_4 "
              "%s  vs VC best-u UB_4 %s"
              % (w["r2"]["kz"], w["r2"]["h"], fmt_ub(rec["val"]),
                 fmt_ub(vcv)), flush=True)
    ucont_lab = ("UCONTENT(core FM resisters %d, u-dial repairs "
                 "%d)" % (n_resist, n_urep))
    check("P5b typed: %s -- the head scale is certification "
          "content beyond the scale-free r_ij" % ucont_lab, True)
    # exact backstop + soundness on every winner core crosser
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
        ns = backstop_corr_exact(rec["Mat"])
        if ns is not True or not pd_f:
            bs_ok = False
            print("    BACKSTOP SEAT kz %d h %d: exact %s, "
                  "eigh-PD %s" % (w["r2"]["kz"], w["r2"]["h"],
                                  ns, pd_f), flush=True)
        else:
            n_bs += 1
    check("P6 WARD exact NEWTON-STURM backstop certifies PD on "
          "every winner core crosser and eigh agrees: %d/%d"
          % (n_bs, n_cross), bs_ok, kill="K2")
    rmins = [rmin_of_R(r["R"]) for r in wrecs
             if r["R"] is not None]
    rmins = [r for r in rmins if r is not None]
    hist = {r: rmins.count(r) for r in range(1, R_MAX + 1)}
    rmin_lab = ("RMIN(%s%s)"
                % (",".join("r%d:%d" % (r, hist[r])
                            for r in range(1, R_MAX + 1)
                            if hist[r]),
                   (",NONE:%d" % (len(rows) - len(rmins)))
                   if len(rmins) < len(rows) else ""))
    check("P7 typed winner minimal-order census: %s (r = 1 <=> "
          "p_2 < 8/7 by P4)" % rmin_lab, True)
    scr_lab, _sl = screen(margins if margins else [0.0],
                          taus if taus else [1.0])
    check("P8 typed tau-screen of the winner margins (1 - UB_4): "
          "%s" % scr_lab, True)

    # ------------------------------------------------------------ Q
    section("Q -- the structural candidates: certified vs "
            "needed, before/after, binding anatomy")
    cand_core = {"GERSH": 0, "BRAUER": 0, "L2": 0}
    gs, brs, fros, p2s, graws = [], [], [], [], []
    cand_margins = {"GERSH": [], "BRAUER": [], "L2": []}
    for rec in wrecs:
        if "g" not in rec:
            continue
        gs.append(rec["g"])
        brs.append(rec["brauer"])
        fros.append(rec["fro"])
        p2s.append(rec["ps"][2])
        graws.append(rec["graw"])
        cand_margins["GERSH"].append(1.0 - rec["g"])
        cand_margins["BRAUER"].append(1.0 - rec["brauer"])
        cand_margins["L2"].append(1.0 - rec["fro"])
        if rec["g"] < 1.0:
            cand_core["GERSH"] += 1
        if rec["brauer"] < 1.0:
            cand_core["BRAUER"] += 1
        if rec["ps"][2] < L2_BAR:
            cand_core["L2"] += 1
    def mmm(a):
        return (float(np.min(a)), float(np.median(a)),
                float(np.max(a)))
    print("    certified-vs-needed on the winner form %s (all "
          "bars are < 1; L2 bar p_2 < 8/7 = %.4f):" % (win, L2_BAR))
    print("      CAND-G   Gershgorin max row sum g: min/med/max "
          "%.3f/%.3f/%.3f  -> certifies %d/%d"
          % (*mmm(gs), cand_core["GERSH"], len(gs)))
    print("      CAND-B   Brauer-Cassini max sqrt(s_i s_j): "
          "min/med/max %.3f/%.3f/%.3f  -> certifies %d/%d"
          % (*mmm(brs), cand_core["BRAUER"], len(brs)))
    print("      CAND-L2  sqrt(7 p_2/8): min/med/max "
          "%.3f/%.3f/%.3f  (p_2 %.3f/%.3f/%.3f)  -> certifies "
          "%d/%d" % (*mmm(fros), *mmm(p2s), cand_core["L2"],
                     len(fros)))
    print("      BEFORE/AFTER (Gershgorin ratio): raw form "
          "min/med/max %.2f/%.2f/%.2f  ->  corr %.3f/%.3f/%.3f "
          "(the round-60 raw-B battery seat)"
          % (*mmm(graws), *mmm(gs)))
    ba_lab = ("BEFORE/AFTER(gersh raw med %.1f -> corr med %.2f)"
              % (float(np.median(graws)), float(np.median(gs))))
    cand_lab = ("CANDIDATES(core G %d/%d, B %d/%d, L2 %d/%d)"
                % (cand_core["GERSH"], len(gs),
                   cand_core["BRAUER"], len(gs),
                   cand_core["L2"], len(gs)))
    check("Q1 typed: %s / %s" % (cand_lab, ba_lab), True)
    for cn in ("GERSH", "BRAUER", "L2"):
        lab, _s = screen(cand_margins[cn], taus[:len(
            cand_margins[cn])] if len(taus) >= len(
            cand_margins[cn]) else [w["tau"] for w in rows][
            :len(cand_margins[cn])])
        print("      screen of %s margins (1 - bound): %s"
              % (cn, lab))
    # binding anatomy
    top1 = {}
    lag1s = []
    decays = []
    for rec, w in zip(wrecs, rows):
        if "top" not in rec:
            continue
        a, i, j = rec["top"][0]
        lb = pair_label(win, i, j)
        top1[lb] = top1.get(lb, 0) + 1
    for rec in recs["FS"]:
        if rec["R"] is None:
            continue
        lag1s.append(lag1_share(rec["R"]))
        sl, r2d = decay_slope(rec["R"])
        if math.isfinite(sl):
            decays.append((sl, r2d))
    modal = max(top1.items(), key=lambda t: t[1]) if top1 else (
        "-", 0)
    modal_share = modal[1] / max(len(rows), 1)
    med_lag1 = float(np.median(lag1s)) if lag1s else float("nan")
    med_dec = (float(np.median([d[0] for d in decays]))
               if decays else float("nan"))
    med_dr2 = (float(np.median([d[1] for d in decays]))
               if decays else float("nan"))
    print("    binding anatomy (winner %s): top-1 pair census %s"
          % (win, sorted(top1.items(), key=lambda t: -t[1])))
    bind_lab = ("BINDING(modal %s share %.3f; lag-1 share of p_2 "
                "med %.3f; FS decay slope med %+.2f R2 %.2f)"
                % (modal[0], modal_share, med_lag1, med_dec,
                   med_dr2))
    check("Q2 typed: %s" % bind_lab, True)

    # ------------------------------------------------------------ H
    section("H -- the dictionary ward + the all-h statement + "
            "representative anatomy")
    wm = rows[len(rows) // 2]
    r2m = wm["r2"]
    al, be, m0 = r2m["chain"]
    Pc = eval_chain(al, be, m0, r2m["y_core"], r2m["h"])
    Gc = (np.sqrt(r2m["v_core"])[:, None] * (Pc @ Pc.T)
          * np.sqrt(r2m["v_core"])[None, :])
    dev_dict = float(np.max(np.abs(
        (np.eye(8) - Gc) - r2m["Bcore"])))
    check("H1 WARD dictionary: core block of A = I - G at the "
          "median step (kz %d) reproduces from the CD-chain "
          "Christoffel kernel at the folded negative nodes: "
          "max dev %.2e <= %.0e"
          % (r2m["kz"], dev_dict, DICT_TOL), dev_dict <= DICT_TOL,
          kill="K2")
    wvals = [r["val"] for r in wrecs]
    fin_w = [v for v in wvals if math.isfinite(v)]
    print("""
    ALL-H STATEMENT (the sharpest form this program can now
    name; NAMED, not proved):
      For every consecutive full-core step (r1, r2) of the
      deployed ladder: let S = core Schur complement of the rung
      wall A = I - G on the folds CORE_J (G = the CD-chain
      Christoffel-kernel Gram of the folded NEGATIVE arm of the
      arch+atom lag density; H1), tau_1 > 0 the previous rung
      floor, and R = corr(S / tau_1) = corr(S).  Then the 28
      off-diagonal correlations r_ij = S_ij / sqrt(S_ii S_jj)
      satisfy the explicit binomial-moment inequality
          Psi_4(p_2, ..., p_8) < 1,   p_j = tr((R - I)^j),
      i.e. UB_4(R) < 1, whence n_+ = 8 and the step wall M > 0
      (Sylvester + integrality).  The u-dial of CLXXIII is
      ELIMINATED (ward P2): this is ONE scale-free inequality
      per step in the r_ij alone.""")
    print("      measured core band: UB_4 %.3f..%.3f (med %.3f); "
          "p_2 %.2f..%.2f; the inequality is NOT first-order "
          "(candidates above): it is carried by the signed "
          "cycle sums p_3, p_5, ... against the L2 mass p_2."
          % (float(np.min(fin_w)), float(np.max(fin_w)),
             float(np.median(fin_w)), float(np.min(p2s)),
             float(np.max(p2s))))
    p3s = [rec["ps"][3] for rec in wrecs if "ps" in rec]
    p4s = [rec["ps"][4] for rec in wrecs if "ps" in rec]
    print("      cycle sums: p_3 min/med/max %.2f/%.2f/%.2f; "
          "p_4 %.2f/%.2f/%.2f" % (*mmm(p3s), *mmm(p4s)))
    allh_lab = ("ALLH(Psi_4(p_2..p_8) < 1 scale-free per step; "
                "core UB_4 %.2f..%.2f, p_2 med %.2f, p_3 med "
                "%+.2f)" % (float(np.min(fin_w)),
                            float(np.max(fin_w)),
                            float(np.median(p2s)),
                            float(np.median(p3s))))
    check("H2 typed: %s" % allh_lab, True)
    reps = [rows[0], rows[len(rows) // 2], rows[-1]]
    for w in reps:
        rec = wrecs[rows.index(w)]
        print("    kz %d h %d:" % (w["r2"]["kz"], w["r2"]["h"]))
        if rec["R"] is not None:
            print_R_anatomy(rec["R"], win, "winner %s" % win)

    # ------------------------------------------------------------ D
    section("D -- deep blind holdout (winner form, scored, no "
            "refits)")
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
          "inherited, declared)"
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
        dsteps.append(make_step(g1, g2))
    print("    deep census: %d new rungs, %d usable, %d steps  "
          "[%.1f s]" % (len(order), len(usable), len(dsteps),
                        time.time() - T0))
    n_dc = 0
    n_dbs = 0
    d_sound = True
    dvals = []
    dcand = {"GERSH": 0, "BRAUER": 0, "L2": 0}
    dtop1 = {}
    deep_rows = []
    n_durep = 0
    n_dresist = 0
    for w in dsteps:
        Mat = form_mat(w, win)
        rec = score_form(Mat)
        dvals.append(min(rec["val"], FLOOR_CAP))
        crossed = rec["val"] < 1.0 - CERT_EPS
        tag = ""
        info = ""
        if not crossed:
            n_dresist += 1
            vcv = vc_value(w)
            if vcv < 1.0 - CERT_EPS:
                n_durep += 1
            tag = "  [VC best-u %s]" % fmt_ub(vcv)
        if rec["R"] is not None:
            R = rec["R"]
            ps = opower_sums(R)
            g, br, _s = gersh_stats(R)
            if g < 1.0:
                dcand["GERSH"] += 1
            if br < 1.0:
                dcand["BRAUER"] += 1
            if ps[2] < L2_BAR:
                dcand["L2"] += 1
            a, i, j = top_pairs(R)[0]
            lb = pair_label(win, i, j)
            dtop1[lb] = dtop1.get(lb, 0) + 1
            deep_rows.append((w["r2"]["h"], ps[2], rec["val"],
                              g, a))
            info = ("  p2 %.2f  g %.2f  top %s %.3f"
                    % (ps[2], g, lb, a))
        if crossed:
            n_dc += 1
            pd_f = float(np.linalg.eigvalsh(w["Mt"])[0]) > 0.0
            ns = backstop_corr_exact(Mat)
            if ns is True and pd_f:
                n_dbs += 1
                tag = "  backstop PD"
            else:
                d_sound = False
                tag = "  BACKSTOP SEAT(exact %s, eigh %s)" % (
                    ns, pd_f)
        print("    DEEP kz %3d h %5d: UB_4 %s%s%s%s  [%.1f s]"
              % (w["r2"]["kz"], w["r2"]["h"], fmt_ub(rec["val"]),
                 (" (%s)" % rec["seat"]) if rec["seat"] else "",
                 info, tag, time.time() - T0), flush=True)
    check("D.s WARD deep soundness: exact backstop + eigh agree "
          "on every deep crosser (%d/%d)" % (n_dbs, n_dc),
          d_sound, kill="K2")
    dmodal = max(dtop1.items(), key=lambda t: t[1]) if dtop1 \
        else ("-", 0)
    dlab = ("DEEP-SCORED(winner %s crosses %d/%d, med UB_4 %.3g, "
            "backstop %d/%d; cand G %d B %d L2 %d; modal %s "
            "share %.2f; u-dial repairs %d/%d resisters)"
            % (win, n_dc, len(dsteps),
               float(np.median(dvals)) if dvals else float("nan"),
               n_dbs, n_dc, dcand["GERSH"], dcand["BRAUER"],
               dcand["L2"], dmodal[0],
               dmodal[1] / max(len(dsteps), 1), n_durep,
               n_dresist))
    check("D typed: %s" % dlab, True)
    # trends across core + deep
    hs_all = ([w["r2"]["h"] for w, rec in zip(rows, wrecs)
               if "ps" in rec]
              + [t[0] for t in deep_rows])
    p2_all = p2s + [t[1] for t in deep_rows]
    ub_all = ([rec["val"] for rec in wrecs if "ps" in rec]
              + [t[2] for t in deep_rows])
    g_all = gs + [t[3] for t in deep_rows]
    mr_all = ([rec["top"][0][0] for rec in wrecs if "top" in rec]
              + [t[4] for t in deep_rows])
    lh = np.log(np.asarray(hs_all, float))
    _a1, sl_p2, r2_p2 = ols_line(lh, np.log(p2_all))
    _a2, sl_ub, r2_ub = ols_line(lh, np.log(ub_all))
    _a3, sl_g, r2_g = ols_line(lh, np.asarray(g_all))
    _a4, sl_mr, r2_mr = ols_line(lh, np.asarray(mr_all))
    trend_lab = ("TRENDS(log p_2 ~ %+.2f log h R2 %.2f; log UB_4 "
                 "~ %+.2f R2 %.2f; g ~ %+.2f R2 %.2f; max|r| ~ "
                 "%+.3f R2 %.2f)"
                 % (sl_p2, r2_p2, sl_ub, r2_ub, sl_g, r2_g,
                    sl_mr, r2_mr))
    check("D.t typed: %s" % trend_lab, True)

    # -------------------------------------------------- OUTCOME
    identity_cand = [c for c in ("GERSH", "BRAUER", "L2")
                     if cand_core[c] == len(gs)
                     and dcand[c] == len(dsteps)]
    if identity_cand:
        outcome = ("UB4-IDENTITY(%s certifies %d/%d core + %d/%d "
                   "deep: an identity-grade classical theorem)"
                   % (identity_cand[0], len(gs), len(gs),
                      len(dsteps), len(dsteps)))
    elif modal_share >= MODAL_MIN or (
            math.isfinite(med_lag1) and med_lag1 >= LAG1_MIN):
        outcome = ("UB4-STRUCTURED(no classical closure; binding "
                   "correlations few and organized: modal %s "
                   "share %.2f, lag-1 share med %.2f)"
                   % (modal[0], modal_share, med_lag1))
    else:
        outcome = ("UB4-ARITHMETIC(no classical closure and no "
                   "organized binding structure; modal %s share "
                   "%.2f, lag-1 med %.2f)"
                   % (modal[0], modal_share, med_lag1))
    check("O typed: OUTCOME %s" % outcome, True)

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
    check("C2.1 WARD both controls fire (Epstein criterion-level "
          "NA: single control rung, no step pair -- disclosed)",
          fired_all, kill="K2")
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
        n_ccl = 0
        for g1, g2 in zip(clad, clad[1:]):
            if not (g1.get("core_ok") and g2.get("core_ok")):
                continue
            if "S" not in g1 or "S" not in g2:
                continue
            if g1["tau"] == 0.0:
                continue
            wc = make_step(g1, g2)
            n_ct += 1
            m_pd = float(np.linalg.eigvalsh(wc["Mt"])[0]) > 0.0
            n_pd += m_pd
            Mat = form_mat(wc, win)
            rec = score_form(Mat)
            if rec["seat"]:
                seats[rec["seat"]] = seats.get(rec["seat"], 0) + 1
            elif rec["val"] >= 1.0 - CERT_EPS:
                n_high += 1
            else:
                n_cert += 1
                if not m_pd:
                    c_sound = False
            if rec["R"] is not None:
                g, _b, _s = gersh_stats(rec["R"])
                if g < 1.0:
                    n_ccl += 1
                    if not m_pd:
                        c_sound = False
        seat_lab = ",".join("%s x%d" % (k, v)
                            for k, v in sorted(seats.items()))
        ctrl_labels.append("%s(cert %d/%d, UB4>=1 %d, refuse "
                           "[%s], gersh-cert %d, PD cores %d/%d)"
                           % (wname, n_cert, n_ct, n_high,
                              seat_lab, n_ccl, n_pd, n_ct))
        print("    %s control steps: %d built, %d certified, %d "
              "with UB_4 >= 1, refusal seats [%s], %d "
              "gersh-certified, %d truly PD cores"
              % (wname, n_ct, n_cert, n_high, seat_lab, n_ccl,
                 n_pd), flush=True)
    check("C6 SOUNDNESS WARD on control steps: no certificate "
          "(UB_4 or classical) on a non-PD core", c_sound,
          kill="K2")
    clab = " / ".join(ctrl_labels)
    check("C7 typed: CONTROLS(%s) -- the CLXXIII DOM-FAIL seat "
          "cannot exist here; the census shows where the "
          "discrimination now lives (diag<=0 refusal + the "
          "UB_4 bar itself)" % clab, True)

    return finish(dict(
        repro="REPRO(VC %d/%d med %.4f)" % (n_vc, len(rows),
                                            vc_med),
        analytic=("ANALYTIC(binom %.1e, trO %.1e, u-inv %.1e, "
                  "corr-tie %.1e, UB-tie %.1e, r1-tie %.1e)"
                  % (dev_binom, dev_tro, dev_uinv, dev_ctie,
                     dev_ubtie, dev_r1tie)),
        forms=("FORMS(FS %d/%d med %.4g; FM %d/%d med %.4g)"
               % (cens["FS"], len(rows), meds["FS"], cens["FM"],
                  len(rows), meds["FM"])),
        winner="WINNER(%s, %d/%d)" % (win, n_win, len(rows)),
        ucont=ucont_lab,
        rmin=rmin_lab,
        bs="BACKSTOP(%d/%d core, %d/%d deep)"
           % (n_bs, n_cross, n_dbs, n_dc),
        cand=cand_lab, ba=ba_lab, bind=bind_lab,
        outcome=outcome, allh=allh_lab, deep=dlab,
        trend=trend_lab, scr=scr_lab, ctrl=clab))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("UB4IDENT-MEASURED / MACHINE-WARDED / %s / %s "
                   "/ %s / %s / %s / %s / %s / %s / %s / %s / %s "
                   "/ %s / %s / %s / SCREEN %s / CONTROLS(%s)"
                   % (labels.get("repro", "-"),
                      labels.get("analytic", "-"),
                      labels.get("forms", "-"),
                      labels.get("winner", "-"),
                      labels.get("ucont", "-"),
                      labels.get("rmin", "-"),
                      labels.get("bs", "-"),
                      labels.get("cand", "-"),
                      labels.get("ba", "-"),
                      labels.get("bind", "-"),
                      labels.get("outcome", "-"),
                      labels.get("allh", "-"),
                      labels.get("deep", "-"),
                      labels.get("trend", "-"),
                      labels.get("scr", "-"),
                      labels.get("ctrl", "-")))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): every census is a float-level
  measurement (validity-warded, conservative refusals) about the
  computed step matrices; every crossing is anchored by the
  exact NEWTON-STURM backstop, i.e. a theorem about the
  float64-computed step matrix, never about the ideal object.
  The analytic form Psi_4(p_2..p_8) < 1 is an exact identity-
  level rewriting of the CLXXIII certificate; whether it HOLDS
  ladder-wide remains a measured surface fact.  The all-h
  statement is named, not proved.  Nothing here proves n > q
  uniformity in h, the pipeline enclosure, or any tail
  statement.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
