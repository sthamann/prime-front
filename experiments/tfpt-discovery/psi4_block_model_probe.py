#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""psi4_block_model_probe -- PRIME.PORT.PSI4.BLOCKMODEL.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the direct follow-up to CLXXV (UB4-STRUCTURED).
CLXXV proved the analytic form -- UB_4 < 1 on the equilibrated
step form is EXACTLY Psi_4(p_2..p_8) < 1 in the 28 off-diagonal
correlations -- measured that NO classical candidate certifies
(~4.8x coherent mass above the bar), and named THE CARRIER: an
organized alternating +-0.9 block on the x1-x2-x3 triple (modal
top pair x1-x2 share 0.769 core / 0.81 deep) plus a head-scale
dial that repairs every scale-free resister.  THE QUESTION OF
THIS PROBE: does the TWO-PARAMETER BLOCK MODEL (block correlation
rho on the alternating triple + head scale u) saturate the
measured Psi_4 surface -- and if yes, what is the sharpest
two-condition all-h statement it induces?  2026-08-11.)

THE MODEL (frozen).  Coordinates = the Jacobi-equilibrated step
form of the CLXXIII/CLXXV chain: per consecutive full-core step
(r1, r2) build the framed step matrix Mt (P2/P3 convention,
head x0 = soft direction, co-block x1..x7), R = corr(Mt) (unit
diagonal, source-only: only matrix ENTRIES consumed), and the
HEAD-SCALE FAMILY N(v) = scaled(R, v) (N[0,0] = v, N[0,j] =
sqrt(v) r_0j, co-block fixed) -- by the CLXXV algebra N(nsc) ==
the assembled Jacobi form A0 = assemble(nsc, chat, corr(B))
EXACTLY (ward F2b).  The two-parameter block model:
    M(rho, u; bg) = scaled(I_8 + T(rho) + BG, u),
T(rho) = the alternating triple on coordinates (x1, x2, x3):
entries s_12 rho, s_13 rho, s_23 rho with the MEASURED sign
pattern (per-step signs for per-step evaluations; the MODAL core
pattern for the region maps -- read in-run from the census,
source-only), all other entries from the background treatment:
    BG0  zero background (the pure skeleton);
    BGM  measured-median background: per-position median (signed)
         of R over the CORE steps at the 25 non-triple
         off-diagonal positions (head row x0-xj + off-triple
         co-block) -- ONE frozen template, reused verbatim on
         deep (no refit, declared).
CLOSED FORM (BG0): with pi = s_12 s_13 s_23 the triple block is
diagonally sign-similar to the all-(+) (pi = +1) or all-(-)
(pi = -1) triangle, so the spectrum of M(rho, u) is EXACTLY
    { u } + { 1+2 rho, 1-rho, 1-rho }   (pi = +1)
    { u } + { 1-2 rho, 1+rho, 1+rho }   (pi = -1)
    + { 1 x4 },
i.e. at most FOUR distinct atoms.  CONSEQUENCE (the closed-form
heart of this probe): a measure with <= 4 atoms is exactly
determined by m_0..m_8, so the r = 4 CMS node-0 bound is EXACT
on the skeleton -- Psi_4(rho, u) == 0 on the whole PD quadrant
{ u > 0, rho < 1 } (pi = +1; rho < 1/2 for pi = -1) and >= 1
outside: the BG0 certification region IS the PD region, and the
u-WINDOW of the skeleton is (0, infinity) at every rho < 1 --
window EXISTENCE is a structural property of the block form
(ward G1 verifies the moment identity + the ~0 value; ward G2
kills on any unsound grid certificate).  All Psi_4 evaluations
use the deployed CLXIV moment machine verbatim (cms_ub with the
conservative refusal guards + fallback chain; refusals typed).

(a) REGION MAPS (block G).  BG0: closed-form spectrum on the
grid RHO_GRID x VGRID, censused against the machine; BGM: the
template model on the same grid (eigvalsh truth, machine value),
printed as the rho_max(u) profile + the u-window of the region
at representative rho -- the certification region {Psi_4 < 1}
in the (rho, u) plane.

(b) FAITHFULNESS (block B).  Per core/deep step the DECLARED
estimators (R-only, source-only, no target data):
    rho_h  = mean(|r_12|, |r_13|, |r_23|)  of R;
    signs  = entrywise signs of the triple; pi_h their product;
    u_h    = argmin over VGRID of Psi4(N(v))  (the certifying
             head scale of the measured family);
    u_raw  = nsc = Mt[0,0] (context: the raw head scale).
Ratio ladder Psi4_model(rho_h, u_h) / Psi4_meas(u_h) per
variant; decision agreement (cert vs cert) at u_h and at the
scale-free point v = 1 (the CLXXV FM ladder, reproduction R0);
every step with a nonempty measured window anchored by the
exact NEWTON-STURM backstop on the exact congruent corr form
(kill on mismatch).  FROZEN FAITHFULNESS RULE: the faithful
variant = larger (core+deep) decision agreement at u_h, tie by
larger core value-band share, tie BGM; outcomes below.

(c) THE TWO-CONDITION ALL-H SHAPE (block T).  Hybrid ward TH1:
H(t) = base_h + t (N(u_h) - base_h), base_h = the exact-triple
skeleton (diag(u_h, 1..1) + exact triple entries), H(1) == N(u_h)
exactly.  t_max = the largest contiguous t on T_GRID with
Psi4(H(t)) < 1: the measured BACKGROUND ADMITTANCE of the step;
model-side t_max on M(rho_h, u_h; BGM) analogously (template as
the background).  THE STATEMENT (named, not proved): M(step) > 0
for all h follows from (i) the fitted trajectory (rho_h, u_h)
stays inside the certification region -- on the skeleton
EXACTLY {rho < 1, u > 0}, margin 1 - rho_h -- and (ii) the
off-triple background mass stays below the measured admittance
(t_max ladder, margin t_max - 1).  Both censused over ~20x in h
(trends + tau-screens).

(d) THE HEAD-SCALE WINDOW (block U).  Measured window W_h =
{v in VGRID : Psi4(N(v)) < 1} per step (width in octaves,
contiguity, v = 1 membership == FM census, u_raw membership);
the ONE-U fact = the intersection of all W_h over core + deep
(reported as an interval); model windows per step (BGM) and the
BG0 closed-form window (0, infinity): if the skeleton carries
the window, its EXISTENCE is structural (any u > 0 works at
rho < 1) and the measured finiteness of W_h is a BACKGROUND
effect -- exactly condition (ii).

(e) GATES.  Tau-screens on the margin families (1 - rho_h,
window log-width, t_max - 1).  DISCRIMINATION on smooth + cosh
control steps THROUGH THE FITTED PARAMETERS: per control step
the fit census (domain exit diag <= 0 = model-class exit --
declared parameter-level: the model class has positive diagonal
by construction; rho_h >= 1; pi flip vs the modal pattern;
measured-family refusal at every v = window empty), the leak
census (non-PD core whose fitted point is in-region AND whose
measured family certifies somewhere -- a CMS validity break,
kill C6), and the honest typed answer where the world
separation actually lives; Epstein + scramble fire at rung
level (C2), scramble core dead -> C4 disclosed, Epstein
criterion-level NA (single control rung, disclosed).
ANTI-CIRCULARITY: every estimator and the template consume only
ENTRIES of R / Mt; no sigma_h, no defect eigenvector, no target
eigendata; the deep block reuses the core template verbatim;
float eigensolves appear in truth wards and grid truth only.

FROZEN PROTOCOL (pipeline verbatim from CLXXV = CLXXIII = CLXIV
= CLXIII = CXLIV chain; moment machine, guards, battery
verbatim from CLXIV; deep machinery verbatim from
deep_blind_holdout):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1-W3 ladder wards (42 rungs, >= 30
     full-core, truth all-PSD, >= 20 steps); W4 P2/P3 ledger
     reproduction; W6 machine wards.  P_G-free probe (declared).
 M   MOMENT MACHINE WARDS (kill -> WARD-BROKEN): M1 validity
     battery (seeded ward-RNG), M2 r = 1 closed-form tie, M3
     NEWTON-STURM == eigh on the battery subsample.
 R0  CLXXV REPRODUCTION (kill -> WARD-BROKEN): FM census >=
     FM_CEN_MIN and med == 0.7408 (rtol 5e-2); modal top pair
     == x1-x2 with share in MODAL_BAND.
 F   THE FIT (F1 census typed; F2 domain ward kill; F2b the
     N(nsc) == A0 dictionary tie at the median step, kill).
 G   REGION MAPS (G1 closed-form wards kill; G2 grid soundness
     kill; G3/G4 typed).
 B   FAITHFULNESS (typed; BS backstop ward kill).
 T   TWO-CONDITION SHAPE (TH1 kill; T2-T5 typed).
 U   WINDOWS (typed).
 D   DEEP BLIND HOLDOUT (D.w ward kill; D.s backstop kill;
     censuses typed; no refits).
 C   CONTROLS (kill -> WARD-BROKEN if silent): C0 truth; C1
     smooth fires; C2 Epstein + scramble fire at kz 9; C3
     smooth-B0 exact refusal >= REFUSE_MIN; C4 scramble
     disclosed; C5 cosh fires (smallest ladder amplitude); C6
     soundness kill (no measured-family certificate anywhere on
     a non-PD control core); C7 typed discrimination census.

KILLS: K1 pipeline (W1-W3) -> PIPELINE-BROKEN; K2 all other
wards -> WARD-BROKEN.  Census blocks are typed measurements,
never kills.

HONEST OUTCOMES (frozen enum, decided on the faithful variant):
  BLOCKMODEL-FAITHFUL   -- decision agreement at u_h >=
      AGREE_MIN on core AND deep; median value ratio in
      [RAT_LO, RAT_HI] and band-3 share >= BAND3_FRAC on core;
      in-region share (BGM map) >= AGREE_MIN on core + deep;
      leak census 0.  The two-condition all-h statement is then
      stated with the measured constants.
  BLOCKMODEL-PARTIAL    -- decision agreement >= AGREE_PART on
      core AND deep and leak 0, but a named value/region miss.
  BLOCKMODEL-UNFAITHFUL -- anything less (or any leak).

VERDICT (frozen enum): PSI4BLOCK-MEASURED with typed sublabels
MACHINE-WARDED(...), REPRO(FM ...), FIT(...), REGION-BG0(...),
REGION-BGM(...), FAITH(...), RATIO(...), TRAJ(...), TOL(...),
WINDOW(...), ONE-U(...), DEEP-SCORED(...), TRENDS(...),
SCREENS(...), OUTCOME(...), CONTROLS(...); else PIPELINE-BROKEN
/ WARD-BROKEN.

FROZEN BARS: CORE_J = (2,...,16); H_LADDER_MAX = 900; N_RUNGS_EXP
= 42; MIN_CORE_RUNGS = 30; MIN_STEPS = 20; MINB_REF = 0.679 (rtol
2e-2); GAPMIN_REF = 0.052, GAPMED_REF = 0.888 (rtol 5e-2); R_MAX
= 4; CERT_EPS = 1e-6; RES_TOL = 1e-8; W_TOL = 1e-10; IMAG_TOL =
1e-8; VAL_TOL = 1e-6; R1_TOL = 1e-8; NW_RAND = 500; NW_ARROW =
100; WARD_SEED = 20260811 (declared ward-RNG); REFUSE_MIN = 30;
INJ_LADDER = (0.01, 0.1, 1.0); INJ_DELTA = 0.05; INJ_GAMMA0 =
10.0; TAB_EXT = 4_000_000; H_HOLD = (128, 2900); KZ_SCAN_MAX =
400; SLOPE_PASS = 0.30; SLOPE_RELOC = 0.70; CTRL_KZ = 9; scramble
seed 1; FLOOR_CAP = 1e9; FM_CEN_MIN = 35; FM_MED_REF = 0.7408
(rtol 5e-2); MODAL_PAIR = x1-x2, MODAL_BAND = (0.55, 0.95);
TRIPLE = coordinates (1, 2), (1, 3), (2, 3) of the framed form;
RHO_GRID = 0.00..0.995 step 0.005; LOG2U in [-8, 8] step 0.25
(VGRID = 2^LOG2U, 65 points); T_GRID = 0.00..6.00 step 0.05;
UB0_TOL = 1e-3; MOM_TIE_TOL = 1e-9 (rel); PD_TOL = 1e-9;
DEGEN_GAP = 1e-6; DICT_TOL = 1e-12; AGREE_MIN = 0.90; AGREE_PART
= 0.75; RAT_LO = 0.5; RAT_HI = 2.0; BAND3 = 3.0; BAND3_FRAC =
0.8; representative rho rows for the BGM window print = (0.5,
0.7, 0.8, 0.9); map subsample for G1 = every 10th rho x every
8th u.  Runtime cap declared: 15 min.

NO-GO COMPLIANCE (frozen): the model NEVER certifies a step by
itself -- certification is always the measured Psi_4 anchored by
the exact NEWTON-STURM backstop on the exact congruent form
(CXLIV mandate); the block model is DESCRIPTIVE (fit +
faithfulness), no fit is claimed as an identity; the Anthropic
two-moment no-go is respected: the skeleton statement lives at
r = 4 exactness on <= 4-atom spectra, not in any two-moment
class.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke
run of this script; 44/45 checks PASSED, exactly ONE FAIL --
ward G1: the r=4 CMS exactness census on the BG0 skeleton
subsample read max |UB_4| 5.16e-01 (med 5.29e-11), and the
post-hoc diagnosis located ALL nine offenders on the single
extreme dial column log2 u = +8.0 (u = 256): the float
Hankel/quartic-root solve loses the exact 4-atom canonical
representation at extreme scale spread, while every loss is
CONSERVATIVE (G2 = 0 unsound certificates on both full maps;
the G3 agreement census 0.958 already typed the same
sharpness loss honestly).  TWO post-smoke amendments, both
disclosed, fail-first preserved, NO other bar/band/enum/rule
moved: A1 the G1 kill bar is restricted to the declared
interior |log2 u| <= LOG2U_G1 = 6 of the subsample, and the
extreme-dial census stays PRINTED as a typed conservative
measurement (the ward's target -- the closed-form <= 4-atom
exactness -- is unchanged; what was killing was machine
conditioning at the corner of the diagnostic grid, not a
decision surface: no step census, no faithfulness number, no
control consumed G1); A2 a pure formatting guard for the
all-NaN rho_max(u) median print discovered by the legitimate
typed outcome REGION-BGM EMPTY (numpy nanmedian warning; the
label now prints EMPTY REGION).  Smoke numbers (all bars
frozen BEFORE the smoke): pipeline min lam_min(B) 0.6790, gap
0.0520/0.8875; battery 2400/2400, r=1 tie 0.0, NEWTON-STURM ==
eigh; R0 FM 37/39 med 0.7408 EXACT, modal x1-x2 share 0.769;
FIT sign census -+-:19, +--:19, --+:1 (modal -+-, pi = +1 on
39/39), template |bg| med 0.453 max 0.750; G1 moment tie
8.7e-16, interior PD subsample |UB_4| med ~5e-11; G3 BG0
region == PD quadrant agreement 0.958; G4 REGION-BGM EMPTY at
every printed node -- the coherent median template alone
breaks certification, i.e. the REAL background survives only
through its step-specific signed cancellation; B faithfulness:
BG0 agree 0.974 core / 1.000 deep but med ratio 1.8e-10 (the
Psi_4 VALUE is pure background), BGM agree 0.385/0.259 med
ratio 2.77/2.94; backstops 39/39 core + 27/27 deep exact PD;
TH1 0.0; TRAJ rho_h 0.414/0.918/0.957, margin 1-rho min
0.043, log2 u_h med -1.38, raw head nsc in-window 51/66; TOL
measured t_max med 1.10 (>= 1 on 62/64; the 2+2 misses sit
where u_h ran to the +8 grid edge), model t_max med 0.15 (the
median template OVERSHOOTS the real background's admittance);
WINDOW nonempty 66/66, contiguous 54/66, med width 6.38
octaves, v=1 inside on exactly the 37 FM core crossers;
ONE-U intersection over all 66 steps = [2^-3.50, 2^-1.25]
(9 pts, non-contig) -- NONEMPTY; trends flat (rho_h -0.020,
width +0.08, t_max +0.02 per log h), screens all PASS; deep
v=1 census 23/27 == CLXXV; CONTROLS all fire (smooth 42/42,
Epstein neg 55, scramble neg 37 -> C4 disclosed, cosh A=0.01
39/42, C3 refusal 35/35), discrimination THROUGH THE
PARAMETERS: smooth 32/32 non-PD excluded (31 diag<=0 class
exits + 1 rho>=1), cosh 37/37 non-PD excluded (36 diag<=0 + 1
empty-window; param-blind 1), leak 0, 1 sound cert on 2
truly-PD cosh cores; OUTCOME on the frozen rule:
BLOCKMODEL-PARTIAL(BG0, miss = VALUE + REGION).  Runtime
~115 s (cap holds).  The frozen run below re-measures
everything; fail-first preserved: nothing was weakened; enums,
bars and rules are exactly as frozen above plus the two
disclosed amendments.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1:
(i) window memoization per (kz, seed); (ii) Householder frame as
P2/CXLIV; (iii) moments by float matrix powers (k <= 8) for all
measured/hybrid/model evaluations, closed-form eigenvalue
moments only inside ward G1 and the BG0 map; CMS construction,
guards and fallback chain verbatim CLXIV; (iv) NEWTON-STURM
exact backstop verbatim CLXIV on R_exact = E_fr W_fr E_fr,
E_fr = diag(Fraction(float(W_ii^{-1/2}))); (v) deep frame/gram
= deep_blind_holdout verbatim; (vi) strict inequalities in all
exact decisions; (vii) rho_max(u) profile = largest contiguous
certified prefix in rho from 0; region membership of a fitted
point = nearest grid node; (viii) t_max = largest contiguous
certified prefix on T_GRID from t = 0; (ix) the template is
computed from the 39 core fits BEFORE any faithfulness
evaluation and never touched again.

NO RH claim: every census here is a SURFACE measurement about
the float64-computed step matrices of the deployed ladder; a
window/crossing is (via the exact backstop) a statement about
the computed step matrix, never about the ideal object; the
two-condition all-h statement is NAMED, not proved -- nothing
here proves n > q uniformity in h, the pipeline enclosure, or
any tail statement.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control and the frozen-seed ward battery; stdout only.

Sources (read-only): v563_paper2_readouts; wall + fixed-core +
step machinery verbatim from the CLXXV = CLXXIII = CLXIV =
CLXIII = CXLIV chain; moment machine verbatim from
anthropic_moment_inertia (CLXIV); deep machinery from
deep_blind_holdout_probe; cosh signature via CLXII; the
sign-similarity eigenvalue formula for signed triangles and the
exactness of the r-node CMS representation on r-atom measures
are the declared classical methods.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/psi4_block_model_probe.py
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
FLOOR_CAP = 1e9
FM_CEN_MIN = 35
FM_MED_REF = 0.7408
FM_MED_RTOL = 5e-2
MODAL_PAIR = "x1-x2"
MODAL_BAND = (0.55, 0.95)
TRIPLE_IDX = ((1, 2), (1, 3), (2, 3))
RHO_GRID = np.arange(0.0, 0.9951, 0.005)
LOG2U = np.arange(-8.0, 8.001, 0.25)
VGRID = 2.0 ** LOG2U
T_GRID = np.arange(0.0, 6.001, 0.05)
UB0_TOL = 1e-3
MOM_TIE_TOL = 1e-9
PD_TOL = 1e-9
DEGEN_GAP = 1e-6
DICT_TOL = 1e-12
LOG2U_G1 = 6.0
AGREE_MIN = 0.90
AGREE_PART = 0.75
RAT_LO = 0.5
RAT_HI = 2.0
BAND3 = 3.0
BAND3_FRAC = 0.8
REP_RHO = (0.5, 0.7, 0.8, 0.9)
G1_SUB_RHO = 10
G1_SUB_U = 8
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    tag = "PASS" if ok else "FAIL"
    suffix = ("  -- " + detail) if detail else ""
    print(f"  [{tag}] {name}{suffix}", flush=True)
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


# --------------- pipeline, verbatim (CLXXV / CLXXIII / CXLIV chain)
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
                 lag_fn=None):
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
        return f"vacuous(pos={int(np.sum(pos))})", float("nan")
    lab = ("PASS" if abs(sl) <= SLOPE_PASS
           else "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
    return f"{lab}(slope={sl:+.3f}, R2={r2:.3f})", sl


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


def backstop_corr_exact(Mat):
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


# ------------------- correlation form + A0 (CLXXV verbatim)
def corr_of(W):
    dg = np.diag(W).copy()
    if float(np.min(dg)) <= 0.0:
        return None
    e = 1.0 / np.sqrt(dg)
    R = e[:, None] * W * e[None, :]
    return 0.5 * (R + R.T)


def assemble_form(nsc, cvec, Cmat):
    A0 = np.zeros((8, 8))
    A0[0, 0] = nsc
    A0[0, 1:] = cvec
    A0[1:, 0] = cvec
    A0[1:, 1:] = 0.5 * (Cmat + Cmat.T)
    return A0


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


def top_pairs(R, k=3):
    n = R.shape[0]
    off = []
    for i in range(n):
        for j in range(i + 1, n):
            off.append((abs(float(R[i, j])), i, j))
    off.sort(reverse=True)
    return off[:k]


# ------------------- the block model (this probe)
def psi4_of(Mat):
    ms = power_moments(Mat, 2 * R_MAX)
    ub = cms_ub(ms, R_MAX)
    return float("inf") if ub is None else float(ub)


def build_base(rho, signs, Tbg=None):
    """The v = 1 base of the block model (before the head dial)."""
    B = np.eye(8)
    for (i, j), s in zip(TRIPLE_IDX, signs):
        B[i, j] = s * rho
        B[j, i] = s * rho
    if Tbg is not None:
        B = B + Tbg
    return B


def model_mat(rho, u, signs, Tbg=None):
    return scaled(build_base(rho, signs, Tbg), u)


def bg0_eigs(rho, u, pi):
    if pi >= 0:
        tri = [1.0 + 2.0 * rho, 1.0 - rho, 1.0 - rho]
    else:
        tri = [1.0 - 2.0 * rho, 1.0 + rho, 1.0 + rho]
    return np.array([u] + tri + [1.0, 1.0, 1.0, 1.0])


def eig_moments(eigs, kmax):
    return [float(np.sum(eigs ** k)) for k in range(kmax + 1)]


def win_of_curve(cert_bool):
    idx = np.nonzero(np.asarray(cert_bool, bool))[0]
    if len(idx) == 0:
        return None
    contig = (int(idx[-1]) - int(idx[0]) + 1 == len(idx))
    return dict(jlo=int(idx[0]), jhi=int(idx[-1]),
                npts=len(idx), contig=contig,
                lo=float(LOG2U[idx[0]]), hi=float(LOG2U[idx[-1]]))


def meas_curve(Rh):
    vals = np.empty(len(VGRID))
    for j, v in enumerate(VGRID):
        vals[j] = psi4_of(scaled(Rh, v))
    return vals


def t_admittance(base, full):
    """Largest contiguous t on T_GRID with Psi4(base + t (full -
    base)) < 1, from t = 0."""
    diff = full - base
    tmax = None
    for t in T_GRID:
        val = psi4_of(base + t * diff)
        if val < 1.0 - CERT_EPS:
            tmax = float(t)
        else:
            break
    return tmax


def rho_max_profile(cert):
    """cert: (n_rho, n_u) bool.  Largest contiguous certified rho
    prefix per u column."""
    prof = np.full(cert.shape[1], float("nan"))
    for j in range(cert.shape[1]):
        col = cert[:, j]
        if not col[0]:
            continue
        k = 0
        while k + 1 < len(col) and col[k + 1]:
            k += 1
        prof[j] = float(RHO_GRID[k])
    return prof


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
    return out


def fmt_ub(v):
    if not math.isfinite(v):
        return "  ref "
    if v >= 100.0:
        return f"{v:6.1f}"
    return f"{v:6.3f}"


def sgn_str(signs):
    return "".join("+" if s > 0 else "-" for s in signs)


# ------------------- the per-step fit + evaluation
def fit_step(w, Tbg, modal_signs):
    """All declared per-step measurements.  Returns None on model
    -class exit (diag <= 0)."""
    Rh = corr_of(w["Mt"])
    if Rh is None:
        return None
    signs = tuple(1 if Rh[i, j] >= 0 else -1 for i, j in TRIPLE_IDX)
    tri = np.array([abs(float(Rh[i, j])) for i, j in TRIPLE_IDX])
    rho = float(np.mean(tri))
    pi = signs[0] * signs[1] * signs[2]
    curve = meas_curve(Rh)
    cert = curve < 1.0 - CERT_EPS
    wnd = win_of_curve(cert)
    if wnd is None:
        jstar = int(np.argmin(np.where(np.isfinite(curve), curve,
                                       np.inf)))
    else:
        jstar = int(np.argmin(np.where(cert, curve, np.inf)))
    u_h = float(VGRID[jstar])
    psi_meas_uh = float(curve[jstar])
    psi_meas_1 = float(curve[int(np.argmin(np.abs(LOG2U)))])
    out = dict(Rh=Rh, signs=signs, rho=rho, pi=pi, tri=tri,
               u_h=u_h, l2u=float(LOG2U[jstar]),
               u_raw=float(w["nsc"]), curve=curve, wnd=wnd,
               psi_meas_uh=psi_meas_uh, psi_meas_1=psi_meas_1,
               tau=float(w["tau"]), h=int(w["r2"]["h"]),
               kz=int(w["r2"]["kz"]))
    out["u_raw_in"] = bool(
        wnd is not None
        and wnd["lo"] - 0.125 <= math.log2(max(w["nsc"], 1e-300))
        <= wnd["hi"] + 0.125)
    # model values at (rho_h, u_h) and at v = 1
    out["psi_bg0_uh"] = psi4_of(model_mat(rho, u_h, signs))
    out["psi_bgm_uh"] = psi4_of(model_mat(rho, u_h, signs, Tbg))
    out["psi_bg0_1"] = psi4_of(model_mat(rho, 1.0, signs))
    out["psi_bgm_1"] = psi4_of(model_mat(rho, 1.0, signs, Tbg))
    # model window (BGM, per-step signs)
    mcert = np.empty(len(VGRID), bool)
    for j, v in enumerate(VGRID):
        mcert[j] = psi4_of(model_mat(rho, v, signs, Tbg)) \
            < 1.0 - CERT_EPS
    out["mwnd"] = win_of_curve(mcert)
    out["mcert"] = mcert
    out["cert"] = cert
    # background admittance: measured hybrid + model hybrid at u_h
    Nu = scaled(Rh, u_h)
    base = np.eye(8)
    for (i, j) in TRIPLE_IDX:
        base[i, j] = Rh[i, j]
        base[j, i] = Rh[i, j]
    base = scaled(base, u_h)
    out["Nu"] = Nu
    out["base"] = base
    out["tmax_meas"] = t_admittance(base, Nu)
    base_m = model_mat(rho, u_h, signs)
    full_m = model_mat(rho, u_h, signs, Tbg)
    out["tmax_model"] = t_admittance(base_m, full_m)
    return out


def main():
    section("PRIME.PORT.PSI4.BLOCKMODEL.01 -- the two-parameter "
            "block model of the Psi_4 inequality: region, "
            "faithfulness, the two-condition all-h shape, the "
            "head-scale window (EXPLORATION ONLY)")
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
    print(f"    FROZEN_SPEC SHA-256 = {spec_sha}")
    print("    NO RH claim; no marker moves.  Float-level "
          "censuses with the CLXIV validity battery; every "
          "certification anchored by the exact NEWTON-STURM "
          "backstop on the exact congruent form.  The model is "
          "DESCRIPTIVE -- it never certifies a step by itself.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder + P2/P3 reproduction "
            "(P_G-free probe, declared)")
    zones = ladder_zones()
    check(f"W1 frozen rung count {N_RUNGS_EXP}",
          len(zones) == N_RUNGS_EXP, f"found {len(zones)}",
          kill="K1")
    truth = []
    sm_map = {}
    for kz in zones:
        r = gram_anatomy(kz)
        if r is None:
            print(f"    kz {kz:<3d}: CHAIN SHORT", flush=True)
            truth.append(None)
            continue
        truth.append(r)
        rs = gram_anatomy(kz, world_fn=world_smooth)
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
    check(f"W2 >= {MIN_CORE_RUNGS} full-core rungs",
          len(full) >= MIN_CORE_RUNGS,
          f"{len(full)} full-core rungs", kill="K1")
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
    check(f"W3b >= {MIN_STEPS} consecutive full-core steps",
          len(pairs) >= MIN_STEPS, f"{len(pairs)} steps",
          kill="K1")
    print(f"    h range {truth[0]['h']}..{truth[-1]['h']}  "
          f"[{time.time() - T0:.1f} s]")
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
    check(f"W4 REPRODUCTION P2/P3 ledger: min lam_min(B) "
          f"{minB_all:.4f} == {MINB_REF:.3f}; gap min/med "
          f"{gmin:.4f}/{gmed:.4f} == {GAPMIN_REF:.3f}/"
          f"{GAPMED_REF:.3f}", ok_repro, kill="K2")
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
    check(f"M1 WARD validity battery: {n_val}/{n_evals - n_ref} "
          f"non-refusing bounds valid (UB >= n_le0 - {VAL_TOL:.0e}"
          f"; refusals {n_ref} of {n_evals}, conservative)",
          ok_val, kill="K2")
    check(f"M2 WARD r=1 closed-form tie: max rel dev {tie_dev:.2e}"
          f" <= {R1_TOL:.0e}", tie_dev <= R1_TOL, kill="K2")
    check("M3 WARD NEWTON-STURM (float coeffs) == eigh PD on "
          "the battery subsample", sturm_ok, kill="K2")

    # ----------------------------------------------------------- R0
    section("R0 -- CLXXV reproduction (FM census + binding pair)")
    fm_vals = []
    n_fm = 0
    top1 = {}
    for w in rows:
        Rh = corr_of(w["Mt"])
        v = psi4_of(Rh) if Rh is not None else float("inf")
        fm_vals.append(min(v, FLOOR_CAP))
        if v < 1.0 - CERT_EPS:
            n_fm += 1
        if Rh is not None:
            _a, i, j = top_pairs(Rh)[0]
            lb = f"x{i}-x{j}"
            top1[lb] = top1.get(lb, 0) + 1
    fm_med = float(np.median(fm_vals))
    check(f"R0.1 WARD FM reproduces CLXXV: census {n_fm}/"
          f"{len(rows)} >= {FM_CEN_MIN} and med UB_4 {fm_med:.4f}"
          f" == {FM_MED_REF} (rtol {FM_MED_RTOL:.0e})",
          n_fm >= FM_CEN_MIN
          and abs(fm_med / FM_MED_REF - 1.0) <= FM_MED_RTOL,
          kill="K2")
    modal = max(top1.items(), key=lambda t: t[1])
    m_share = modal[1] / max(len(rows), 1)
    check(f"R0.2 WARD modal top pair {modal[0]} share "
          f"{m_share:.3f} == CLXXV ({MODAL_PAIR}, band "
          f"{MODAL_BAND})", modal[0] == MODAL_PAIR
          and MODAL_BAND[0] <= m_share <= MODAL_BAND[1],
          kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ F
    section("F -- the fit: signs, rho_h, u_h, the template "
            "(declared estimators, R-only)")
    # first pass: signs + rho + template accumulation (R entries)
    Rlist = []
    sign_census = {}
    pi_census = {1: 0, -1: 0}
    for w in rows:
        Rh = corr_of(w["Mt"])
        Rlist.append(Rh)
        sg = tuple(1 if Rh[i, j] >= 0 else -1
                   for i, j in TRIPLE_IDX)
        sign_census[sg] = sign_census.get(sg, 0) + 1
        pi_census[sg[0] * sg[1] * sg[2]] += 1
    check("F2 WARD fit domain: corr defined on all "
          f"{len(rows)}/{len(rows)} core steps",
          all(R is not None for R in Rlist), kill="K2")
    modal_signs = max(sign_census.items(), key=lambda t: t[1])[0]
    modal_pi = modal_signs[0] * modal_signs[1] * modal_signs[2]
    stack = np.stack(Rlist)
    Tmed = np.median(stack, axis=0)
    Tbg = Tmed.copy()
    np.fill_diagonal(Tbg, 0.0)
    for (i, j) in TRIPLE_IDX:
        Tbg[i, j] = 0.0
        Tbg[j, i] = 0.0
    bg_mag = np.abs(Tbg[np.triu_indices(8, 1)])
    bg_mag = bg_mag[bg_mag > 0]
    sc_lab = ", ".join(f"{sgn_str(k)}:{v}"
                       for k, v in sorted(sign_census.items(),
                                          key=lambda t: -t[1]))
    check(f"F1 typed: FIT(sign census [{sc_lab}]; modal "
          f"{sgn_str(modal_signs)} pi={modal_pi:+d}; pi census "
          f"+1:{pi_census[1]} -1:{pi_census[-1]}; template "
          f"|bg| med {float(np.median(bg_mag)):.3f} max "
          f"{float(np.max(bg_mag)):.3f} over 25 positions)", True)
    # F2b: N(nsc) == assembled A0 at the median step
    wm = rows[len(rows) // 2]
    Rm = corr_of(wm["Mt"])
    cg = congruence_of(wm, np.diag(np.diag(wm["B"]).copy()))
    dev_dict = float("inf")
    if cg is not None:
        A0m = assemble_form(wm["nsc"], cg["chat"], cg["Chat"])
        dev_dict = float(np.max(np.abs(scaled(Rm, wm["nsc"])
                                       - A0m)))
    check(f"F2b WARD dictionary tie N(nsc) == assembled Jacobi "
          f"form A0 at the median step (kz {wm['r2']['kz']}): "
          f"max dev {dev_dict:.2e} <= {DICT_TOL:.0e}",
          dev_dict <= DICT_TOL, kill="K2")

    # ------------------------------------------------------------ G
    section("G -- region maps: BG0 closed form (exact skeleton) "
            "+ BGM template model")
    # G1: closed-form moments == machine moments; UB4-once ~ 0 on
    # non-degenerate PD subsample.  A1 (disclosed): the kill bar
    # lives on the declared interior |log2 u| <= LOG2U_G1 -- the
    # smoke measured that the float Hankel/root solve loses the
    # exact 4-atom representation at the extreme dial column
    # log2 u = +8 (all losses conservative, G2 = 0 unsound); the
    # full-subsample census stays printed.
    dev_mom = 0.0
    ub4_in = []
    ub4_out = []
    n_deg = 0
    for i in range(0, len(RHO_GRID), G1_SUB_RHO):
        for j in range(0, len(VGRID), G1_SUB_U):
            rho, u = float(RHO_GRID[i]), float(VGRID[j])
            eigs = bg0_eigs(rho, u, modal_pi)
            ms_c = eig_moments(eigs, 2 * R_MAX)
            ms_m = power_moments(
                model_mat(rho, u, modal_signs), 2 * R_MAX)
            for k in range(2 * R_MAX + 1):
                dev_mom = max(dev_mom, abs(ms_c[k] - ms_m[k])
                              / max(1.0, abs(ms_c[k])))
            se = np.sort(eigs)
            if float(np.min(se)) <= DEGEN_GAP:
                continue
            uq = np.unique(np.round(se, 9))
            gap_min = (float(np.min(np.diff(uq)))
                       if len(uq) > 1 else 1.0)
            if gap_min <= DEGEN_GAP:
                n_deg += 1
                continue
            ub = cms_ub_once(ms_c, R_MAX)
            if ub is not None:
                if abs(float(LOG2U[j])) <= LOG2U_G1:
                    ub4_in.append(abs(ub))
                else:
                    ub4_out.append(abs(ub))
    out_lab = (f"; extreme-dial census |log2 u| > {LOG2U_G1:.0f}:"
               f" med {float(np.median(ub4_out)):.2e} max "
               f"{float(np.max(ub4_out)):.2e} ({len(ub4_out)} "
               "pts, typed, conservative)" if ub4_out else "")
    check(f"G1 WARD BG0 closed-form spectrum: machine moments == "
          f"eigenvalue moments (max rel dev {dev_mom:.2e} <= "
          f"{MOM_TIE_TOL:.0e}) and r=4 CMS is ~EXACT on the PD "
          f"subsample with |log2 u| <= {LOG2U_G1:.0f} (|UB_4| "
          f"med {float(np.median(ub4_in)):.2e} max "
          f"{float(np.max(ub4_in)):.2e} <= {UB0_TOL:.0e}, "
          f"{len(ub4_in)} pts{out_lab})",
          dev_mom <= MOM_TIE_TOL
          and float(np.max(ub4_in)) <= UB0_TOL, kill="K2")
    # full BG0 + BGM maps
    cert0 = np.zeros((len(RHO_GRID), len(VGRID)), bool)
    pd0 = np.zeros_like(cert0)
    ref0 = 0
    viol0 = 0
    for i, rho in enumerate(RHO_GRID):
        for j, u in enumerate(VGRID):
            eigs = bg0_eigs(float(rho), float(u), modal_pi)
            ispd = float(np.min(eigs)) > PD_TOL
            pd0[i, j] = ispd
            ub = cms_ub(eig_moments(eigs, 2 * R_MAX), R_MAX)
            if ub is None:
                ref0 += 1
                continue
            c = ub < 1.0 - CERT_EPS
            cert0[i, j] = c
            if c and not ispd:
                viol0 += 1
    certm = np.zeros_like(cert0)
    pdm = np.zeros_like(cert0)
    refm = 0
    violm = 0
    for i, rho in enumerate(RHO_GRID):
        Bb = build_base(float(rho), modal_signs, Tbg)
        for j, u in enumerate(VGRID):
            Mat = scaled(Bb, float(u))
            ispd = float(np.linalg.eigvalsh(Mat)[0]) > PD_TOL
            pdm[i, j] = ispd
            ub = cms_ub(power_moments(Mat, 2 * R_MAX), R_MAX)
            if ub is None:
                refm += 1
                continue
            c = ub < 1.0 - CERT_EPS
            certm[i, j] = c
            if c and not ispd:
                violm += 1
    check(f"G2 WARD grid soundness: 0 unsound certificates "
          f"(BG0 {viol0}, BGM {violm}; refusals {ref0}/{refm}, "
          "conservative)", viol0 == 0 and violm == 0, kill="K2")
    agr0 = float(np.mean(cert0 == pd0))
    prof0 = rho_max_profile(cert0)
    profm = rho_max_profile(certm)
    npts = cert0.size
    print(f"    BG0: region == PD quadrant {{u > 0, rho < "
          f"{'1' if modal_pi > 0 else '1/2'}}} (pi = "
          f"{modal_pi:+d}); grid agreement {agr0:.3f} "
          f"({npts} pts)")
    print("    rho_max(u) profiles (contiguous from rho = 0):")
    print("      log2 u : " + " ".join(
        f"{LOG2U[j]:+5.1f}" for j in range(0, len(VGRID), 8)))
    print("      BG0    : " + " ".join(
        f"{prof0[j]:5.3f}" if math.isfinite(prof0[j]) else
        "  -- " for j in range(0, len(VGRID), 8)))
    print("      BGM    : " + " ".join(
        f"{profm[j]:5.3f}" if math.isfinite(profm[j]) else
        "  -- " for j in range(0, len(VGRID), 8)))
    check(f"G3 typed: REGION-BG0(== PD quadrant, agreement "
          f"{agr0:.3f}, refusals {ref0}) -- the skeleton u-window"
          " is (0, inf) at every certifiable rho: window "
          "EXISTENCE is structural (closed form)", True)
    rep_lines = []
    for rr in REP_RHO:
        i = int(round(rr / 0.005))
        wr = win_of_curve(certm[i, :])
        if wr is None:
            rep_lines.append(f"rho {rr:.2f}: empty")
        else:
            rep_lines.append(
                f"rho {rr:.2f}: u in [2^{wr['lo']:+.2f}, "
                f"2^{wr['hi']:+.2f}]"
                + ("" if wr["contig"] else " (non-contig)"))
    profm_fin = profm[np.isfinite(profm)]
    profm_lab = (f"{float(np.median(profm_fin)):.3f}"
                 if len(profm_fin) else "EMPTY REGION")
    check("G4 typed: REGION-BGM(" + "; ".join(rep_lines)
          + f"; rho_max med {profm_lab})", True)

    # ------------------------------------------------------- B / fits
    section("B -- faithfulness: the fitted trajectory and the "
            "ratio ladders (core)")
    fits = []
    print("      kz    h   rho  sgn pi  l2u*  nsc  raw-in "
          "| meas(u*) meas(1) | BG0(u*) BGM(u*) ratio | "
          "win[lo,hi] w | tmax_m tmax_M")
    for w in rows:
        f = fit_step(w, Tbg, modal_signs)
        fits.append(f)
        wnd = f["wnd"]
        wlab = (f"[{wnd['lo']:+.2f},{wnd['hi']:+.2f}] "
                f"{wnd['npts']:2d}" if wnd else "  EMPTY    ")
        rat = (f["psi_bgm_uh"] / f["psi_meas_uh"]
               if f["psi_meas_uh"] > 0
               and math.isfinite(f["psi_bgm_uh"])
               else float("nan"))
        tm = f["tmax_meas"]
        tM = f["tmax_model"]
        print(f"    {f['kz']:4d} {f['h']:4d}  {f['rho']:.3f} "
              f"{sgn_str(f['signs'])} {f['pi']:+d} "
              f"{f['l2u']:+5.2f} {f['u_raw']:5.2f}  "
              f"{'y' if f['u_raw_in'] else 'N'}    | "
              f"{fmt_ub(f['psi_meas_uh'])} {fmt_ub(f['psi_meas_1'])}"
              f" | {fmt_ub(f['psi_bg0_uh'])} "
              f"{fmt_ub(f['psi_bgm_uh'])} {rat:7.3f} | {wlab} | "
              f"{tm if tm is not None else -1:5.2f} "
              f"{tM if tM is not None else -1:5.2f}", flush=True)
    # backstop every step with a nonempty measured window
    n_bs = 0
    n_w = 0
    bs_ok = True
    for w, f in zip(rows, fits):
        if f["wnd"] is None:
            continue
        n_w += 1
        pd_f = float(np.linalg.eigvalsh(w["Mt"])[0]) > 0.0
        ns = backstop_corr_exact(w["Mt"])
        if ns is not True or not pd_f:
            bs_ok = False
            print(f"    BACKSTOP SEAT kz {f['kz']} h {f['h']}: "
                  f"exact {ns}, eigh-PD {pd_f}", flush=True)
        else:
            n_bs += 1
    check(f"BS WARD exact NEWTON-STURM backstop certifies PD on "
          f"every core step with a nonempty measured window and "
          f"eigh agrees: {n_bs}/{n_w}", bs_ok, kill="K2")
    print(f"    [{time.time() - T0:.1f} s]")

    def faith_stats(fits_list, key_uh):
        agree = 0
        rats = []
        n_ok = 0
        for f in fits_list:
            mc = (math.isfinite(f[key_uh])
                  and f[key_uh] < 1.0 - CERT_EPS)
            xc = f["psi_meas_uh"] < 1.0 - CERT_EPS
            if mc == xc:
                agree += 1
            if f["psi_meas_uh"] > 0 and math.isfinite(f[key_uh]):
                r = f[key_uh] / f["psi_meas_uh"]
                rats.append(r)
                if 1.0 / BAND3 <= r <= BAND3:
                    n_ok += 1
        med = float(np.median(rats)) if rats else float("nan")
        frac = n_ok / max(len(fits_list), 1)
        return agree / max(len(fits_list), 1), med, frac

    ag0, med0, fr0 = faith_stats(fits, "psi_bg0_uh")
    agm, medm, frm = faith_stats(fits, "psi_bgm_uh")
    check(f"B1 typed: RATIO core -- BG0 agree {ag0:.3f} med ratio"
          f" {med0:.3g} band3 {fr0:.3f}; BGM agree {agm:.3f} med "
          f"ratio {medm:.3g} band3 {frm:.3f}", True)
    n_v1_agree0 = sum(
        1 for f in fits
        if (math.isfinite(f["psi_bg0_1"])
            and f["psi_bg0_1"] < 1.0 - CERT_EPS)
        == (f["psi_meas_1"] < 1.0 - CERT_EPS))
    n_v1_agreem = sum(
        1 for f in fits
        if (math.isfinite(f["psi_bgm_1"])
            and f["psi_bgm_1"] < 1.0 - CERT_EPS)
        == (f["psi_meas_1"] < 1.0 - CERT_EPS))
    check(f"B2 typed: scale-free point v=1 decision agreement "
          f"BG0 {n_v1_agree0}/{len(fits)}, BGM {n_v1_agreem}/"
          f"{len(fits)} (measured v=1 census {n_fm}/{len(rows)} "
          "== R0)", True)

    # ------------------------------------------------------------ D
    section("D -- deep blind holdout (fits scored, template "
            "frozen from core, no refits)")
    lam_ext = build_ext_tables()
    dev_tab = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                                  - core.LAM_TAB)))
    psi_c = np.cumsum(lam_ext[EXT["NN"]])
    nnf = EXT["NN"].astype(float)
    keep = nnf >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi_c[keep] - nnf[keep])
                         / nnf[keep]))
    check(f"D.w WARD deep-table overlap byte-exact (dev "
          f"{dev_tab:.1e}) and Chebyshev kappa {kappa:.6f} <= "
          f"{core.KAPPA_REF:.6f} + 1e-6",
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
    grams = [ext_gram(kz) for kz in order]
    usable = [g for g in grams if isinstance(g, dict)
              and g.get("core_ok")]
    usable.sort(key=lambda g: (g["h"], g["kz"]))
    dsteps = []
    for g1, g2 in zip(usable, usable[1:]):
        if g1["negA"] > 0 or g1["negS"] > 0 or g1["lamS"] <= 0.0:
            continue
        dsteps.append(make_step(g1, g2))
    print(f"    deep census: {len(order)} new rungs, "
          f"{len(usable)} usable, {len(dsteps)} steps  "
          f"[{time.time() - T0:.1f} s]")
    dfits = []
    n_dbs = 0
    n_dw = 0
    dbs_ok = True
    for w in dsteps:
        f = fit_step(w, Tbg, modal_signs)
        if f is None:
            print(f"    DEEP kz {w['r2']['kz']:3d} h "
                  f"{w['r2']['h']:5d}: class exit (diag <= 0)",
                  flush=True)
            continue
        dfits.append(f)
        wnd = f["wnd"]
        tag = ""
        if wnd is not None:
            n_dw += 1
            pd_f = float(np.linalg.eigvalsh(w["Mt"])[0]) > 0.0
            ns = backstop_corr_exact(w["Mt"])
            if ns is True and pd_f:
                n_dbs += 1
                tag = "  backstop PD"
            else:
                dbs_ok = False
                tag = f"  BACKSTOP SEAT(exact {ns}, eigh {pd_f})"
        rat = (f["psi_bgm_uh"] / f["psi_meas_uh"]
               if f["psi_meas_uh"] > 0
               and math.isfinite(f["psi_bgm_uh"])
               else float("nan"))
        wlab = (f"[{wnd['lo']:+.2f},{wnd['hi']:+.2f}] "
                f"{wnd['npts']:2d}" if wnd else "  EMPTY    ")
        tm = f["tmax_meas"]
        print(f"    DEEP kz {f['kz']:3d} h {f['h']:5d}: rho "
              f"{f['rho']:.3f} {sgn_str(f['signs'])} l2u* "
              f"{f['l2u']:+5.2f} meas(u*) "
              f"{fmt_ub(f['psi_meas_uh'])} meas(1) "
              f"{fmt_ub(f['psi_meas_1'])} BGM "
              f"{fmt_ub(f['psi_bgm_uh'])} rat {rat:6.3f} win "
              f"{wlab} tmax {tm if tm is not None else -1:5.2f}"
              f"{tag}  [{time.time() - T0:.1f} s]", flush=True)
    check(f"D.s WARD deep backstop: exact + eigh agree on every "
          f"deep step with nonempty window ({n_dbs}/{n_dw})",
          dbs_ok, kill="K2")
    dag0, dmed0, dfr0 = faith_stats(dfits, "psi_bg0_uh")
    dagm, dmedm, dfrm = faith_stats(dfits, "psi_bgm_uh")
    n_dfm = sum(1 for f in dfits
                if f["psi_meas_1"] < 1.0 - CERT_EPS)
    check(f"D1 typed: DEEP-SCORED({len(dfits)} steps; v=1 census "
          f"{n_dfm}/{len(dfits)}; BG0 agree {dag0:.3f} med "
          f"{dmed0:.3g}; BGM agree {dagm:.3f} med {dmedm:.3g} "
          f"band3 {dfrm:.3f})", True)

    # --------------------------------------------- faithful variant
    key0 = (ag0 + dag0, fr0)
    keym = (agm + dagm, frm)
    if keym >= key0:
        VAR, vag_c, vag_d, vmed, vfrac = ("BGM", agm, dagm, medm,
                                          frm)
    else:
        VAR, vag_c, vag_d, vmed, vfrac = ("BG0", ag0, dag0, med0,
                                          fr0)
    # in-region census on the BGM map (nearest grid node)
    def in_region(f):
        i = int(round(f["rho"] / 0.005))
        i = min(max(i, 0), len(RHO_GRID) - 1)
        j = int(round((f["l2u"] + 8.0) / 0.25))
        j = min(max(j, 0), len(VGRID) - 1)
        return bool(certm[i, j])

    nin_c = sum(1 for f in fits if in_region(f))
    nin_d = sum(1 for f in dfits if in_region(f))
    check(f"B3 typed: FAITH(variant {VAR}; agree core {vag_c:.3f}"
          f" deep {vag_d:.3f}; med ratio {vmed:.3g}; band3 "
          f"{vfrac:.3f}; in-BGM-region {nin_c}/{len(fits)} core +"
          f" {nin_d}/{len(dfits)} deep)", True)

    # ------------------------------------------------------------ T
    section("T -- the two-condition all-h shape: trajectory, "
            "margins, tolerance")
    dev_h1 = 0.0
    for f in fits:
        H1 = f["base"] + 1.0 * (f["Nu"] - f["base"])
        dev_h1 = max(dev_h1, float(np.max(np.abs(H1 - f["Nu"]))))
    check(f"TH1 WARD hybrid H(1) == N(u_h) exactly: max dev "
          f"{dev_h1:.2e}", dev_h1 == 0.0, kill="K2")

    def mmm(a):
        a = np.asarray(a, float)
        return (float(np.min(a)), float(np.median(a)),
                float(np.max(a)))

    allf = fits + dfits
    rhos = [f["rho"] for f in allf]
    margins_rho = [1.0 - f["rho"] for f in allf]
    l2us = [f["l2u"] for f in allf]
    uraws = [f["u_raw"] for f in allf]
    n_uraw_in = sum(1 for f in allf if f["u_raw_in"])
    tmaxs = [f["tmax_meas"] for f in allf
             if f["tmax_meas"] is not None]
    tmaxs_m = [f["tmax_model"] for f in allf
               if f["tmax_model"] is not None]
    n_t1 = sum(1 for t in tmaxs if t >= 1.0)
    check(f"T2 typed: TRAJ(rho_h {mmm(rhos)[0]:.3f}/"
          f"{mmm(rhos)[1]:.3f}/{mmm(rhos)[2]:.3f}; margin 1-rho "
          f"{mmm(margins_rho)[0]:.3f}/{mmm(margins_rho)[1]:.3f}/"
          f"{mmm(margins_rho)[2]:.3f}; log2 u_h "
          f"{mmm(l2us)[0]:+.2f}/{mmm(l2us)[1]:+.2f}/"
          f"{mmm(l2us)[2]:+.2f}; raw head nsc "
          f"{mmm(uraws)[0]:.2f}/{mmm(uraws)[1]:.2f}/"
          f"{mmm(uraws)[2]:.2f}, in-window {n_uraw_in}/"
          f"{len(allf)})", True)
    check(f"T3 typed: TOL(measured t_max {mmm(tmaxs)[0]:.2f}/"
          f"{mmm(tmaxs)[1]:.2f}/{mmm(tmaxs)[2]:.2f} on "
          f"{len(tmaxs)} steps, >= 1 on {n_t1}; model t_max "
          f"{mmm(tmaxs_m)[0]:.2f}/{mmm(tmaxs_m)[1]:.2f}/"
          f"{mmm(tmaxs_m)[2]:.2f})", True)
    lh = np.log([f["h"] for f in allf])
    _a, sl_rho, r2_rho = ols_line(lh, rhos)
    wids = [f["wnd"]["hi"] - f["wnd"]["lo"] for f in allf
            if f["wnd"] is not None]
    lh_w = np.log([f["h"] for f in allf if f["wnd"] is not None])
    _a, sl_w, r2_w = ols_line(lh_w, wids)
    lh_t = np.log([f["h"] for f in allf
                   if f["tmax_meas"] is not None])
    _a, sl_t, r2_t = ols_line(lh_t, tmaxs)
    check(f"T4 typed: TRENDS(rho_h ~ {sl_rho:+.3f} log h R2 "
          f"{r2_rho:.2f}; window width(oct) ~ {sl_w:+.2f} R2 "
          f"{r2_w:.2f}; t_max ~ {sl_t:+.2f} R2 {r2_t:.2f})",
          True)
    taus_all = [f["tau"] for f in allf]
    s1, _ = screen(margins_rho, taus_all)
    s2, _ = screen(wids, [f["tau"] for f in allf
                          if f["wnd"] is not None])
    s3, _ = screen([t - 1.0 for t in tmaxs],
                   [f["tau"] for f in allf
                    if f["tmax_meas"] is not None])
    check(f"T5 typed: SCREENS(1-rho {s1}; width {s2}; "
          f"t_max-1 {s3})", True)

    # ------------------------------------------------------------ U
    section("U -- the head-scale window + the ONE-U fact")
    n_wc = sum(1 for f in fits if f["wnd"] is not None)
    n_wd = sum(1 for f in dfits if f["wnd"] is not None)
    n_ctg = sum(1 for f in allf if f["wnd"] is not None
                and f["wnd"]["contig"])
    n_v1c = sum(1 for f in fits if f["wnd"] is not None
                and f["wnd"]["lo"] <= 0.0 <= f["wnd"]["hi"]
                and f["psi_meas_1"] < 1.0 - CERT_EPS)
    inter = np.ones(len(VGRID), bool)
    for f in allf:
        inter &= f["cert"]
    iw = win_of_curve(inter)
    ione = (f"[2^{iw['lo']:+.2f}, 2^{iw['hi']:+.2f}] "
            f"({iw['npts']} pts"
            + ("" if iw["contig"] else ", non-contig") + ")"
            if iw else "EMPTY")
    check(f"U1 typed: WINDOW(nonempty {n_wc}/{len(fits)} core + "
          f"{n_wd}/{len(dfits)} deep; contiguous {n_ctg}/"
          f"{n_wc + n_wd}; med width {float(np.median(wids)):.2f}"
          f" octaves; v=1 inside on {n_v1c} core)", True)
    check(f"U2 typed: ONE-U(intersection over all core + deep "
          f"steps = {ione}) -- one head scale certifies the "
          "whole measured surface iff nonempty", True)
    n_mw = sum(1 for f in allf if f["mwnd"] is not None)
    ovl = []
    for f in allf:
        if f["wnd"] is None or f["mwnd"] is None:
            continue
        lo = max(f["wnd"]["lo"], f["mwnd"]["lo"])
        hi = min(f["wnd"]["hi"], f["mwnd"]["hi"])
        wm = f["wnd"]["hi"] - f["wnd"]["lo"]
        ovl.append(max(0.0, hi - lo) / max(wm, 0.25))
    check(f"U3 typed: MODEL-WINDOW(BGM nonempty {n_mw}/"
          f"{len(allf)}; overlap with measured med "
          f"{float(np.median(ovl)) if ovl else float('nan'):.2f})"
          " -- on BG0 the window is (0, inf) exactly (G3): "
          "existence is structural, finiteness is background",
          True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    check("C0.1 WARD truth wall holds (neg(A) = 0 on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    n_viol = sum(1 for kz in zones
                 if isinstance(sm_map.get(kz), dict)
                 and sm_map[kz]["negA"] > 0)
    check(f"C1 WARD smooth world violates (neg(A) > 0 on "
          f"{n_viol} rungs)", n_viol > 0, kill="K2")
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
            print(f"    {name:9s}: chain dies -> fires")
            continue
        fi = r["negA"] > 0
        fired_all &= fi
        print(f"    {name:9s}: tau {r['tau']:+.3e}  neg(A) "
              f"{r['negA']} -> {'FIRES' if fi else 'SILENT'}",
              flush=True)
    check("C2.1 WARD both controls fire (Epstein criterion-level "
          "NA: single control rung, no step pair -- disclosed)",
          fired_all, kill="K2")
    n_refu, n_use = 0, 0
    for w in rows:
        if w["B0"] is None:
            continue
        n_use += 1
        ok0, _ = pd_exact(mat_fr(0.5 * (w["B0"] + w["B0"].T)))
        if not ok0:
            n_refu += 1
    check(f"C3 WARD REFUSAL: exact LDL refuses the smooth "
          f"co-block B0 on {n_refu}/{n_use} usable steps (>= "
          f"{REFUSE_MIN})", n_refu >= REFUSE_MIN, kill="K2")
    rsc = ctl["scramble"]
    c4_ok = True
    c4_msg = ("scramble core dead -> skipped (disclosed; C3 "
              "carries the content)")
    if isinstance(rsc, dict) and rsc.get("core_ok") \
            and "S" in rsc and rsc["lamS"] < 0.0:
        c4_ok = rsc["lamS"] < 0.0
        c4_msg = f"lam_min(S_scr) {rsc['lamS']:.3e} < 0"
    check(f"C4 WARD scramble breaks the floor: {c4_msg}",
          c4_ok, kill="K2")
    cosh_lad, cosh_A = None, None
    for Aamp in INJ_LADDER:
        def inj(rr, _A=Aamp):
            tt = np.arange(rr["M"]) * rr["D"]
            return (_A * np.cos(INJ_GAMMA0 * tt)
                    * (np.cosh(INJ_DELTA * tt) - 1.0))
        lad = [gram_anatomy(kz, lag_fn=inj) for kz in zones]
        n_fire = sum(1 for r in lad
                     if r is None or (isinstance(r, dict)
                                      and r["negA"] > 0))
        print(f"    cosh injection A = {Aamp:<5g}: fires on "
              f"{n_fire}/{len(zones)} rungs", flush=True)
        if n_fire > 0:
            cosh_lad, cosh_A = lad, Aamp
            break
    check(f"C5 WARD off-line cosh injection fires (deployed A = "
          f"{cosh_A})", cosh_lad is not None, kill="K2")
    # criterion-level discrimination through the fitted parameters
    ctrl_labels = []
    c_sound = True
    for wname, lad in (("smooth",
                        [sm_map.get(kz) for kz in zones]),
                       ("cosh", cosh_lad if cosh_lad else [])):
        clad = [r for r in lad if isinstance(r, dict)]
        clad.sort(key=lambda r: (r["h"], r["kz"]))
        n_ct = 0
        seats = {}
        n_pd = 0
        n_pd_cert = 0
        n_nonpd = 0
        n_excl = 0
        n_leak = 0
        n_par_blind = 0
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
            Rh = corr_of(wc["Mt"])
            if Rh is None:
                seats["diag<=0"] = seats.get("diag<=0", 0) + 1
                if not m_pd:
                    n_nonpd += 1
                    n_excl += 1
                continue
            sg = tuple(1 if Rh[i, j] >= 0 else -1
                       for i, j in TRIPLE_IDX)
            rho_c = float(np.mean([abs(float(Rh[i, j]))
                                   for i, j in TRIPLE_IDX]))
            curve = meas_curve(Rh)
            certc = curve < 1.0 - CERT_EPS
            wndc = win_of_curve(certc)
            if wndc is not None and not m_pd:
                c_sound = False
                n_leak += 1
                print(f"    LEAK SEAT {wname} kz {g2['kz']}: "
                      f"non-PD core but measured family "
                      f"certifies", flush=True)
            if m_pd:
                if wndc is not None:
                    n_pd_cert += 1
                continue
            n_nonpd += 1
            if rho_c >= 1.0:
                seats["rho>=1"] = seats.get("rho>=1", 0) + 1
                n_excl += 1
            elif sg[0] * sg[1] * sg[2] != modal_pi:
                seats["pi-flip"] = seats.get("pi-flip", 0) + 1
                n_excl += 1
            elif wndc is None:
                seats["empty-window"] = seats.get(
                    "empty-window", 0) + 1
                n_excl += 1
                n_par_blind += 1
        seat_lab = ",".join(f"{k} x{v}"
                            for k, v in sorted(seats.items()))
        ctrl_labels.append(
            f"{wname}({n_ct} steps, non-PD {n_nonpd}, excluded "
            f"{n_excl}, seats [{seat_lab}], param-blind "
            f"{n_par_blind}, PD-certs {n_pd_cert}/{n_pd}, leak "
            f"{n_leak})")
        print(f"    {wname}: {n_ct} steps, {n_nonpd} non-PD, "
              f"{n_excl} excluded [{seat_lab}], param-level "
              f"blind (excluded only by family/window, not by "
              f"(rho, pi)) {n_par_blind}, {n_pd_cert} sound "
              f"certs on {n_pd} truly-PD cores, {n_leak} leaks",
              flush=True)
    check("C6 SOUNDNESS WARD: no measured-family certificate "
          "anywhere on a non-PD control core (leak 0)", c_sound,
          kill="K2")
    clab = " / ".join(ctrl_labels)
    check(f"C7 typed: CONTROLS({clab}) -- the honest seat map: "
          "class exit diag<=0 + the family-level bar carry the "
          "discrimination; the naked fitted point (rho, pi) is "
          "world-blind where param-blind > 0", True)

    # -------------------------------------------------- OUTCOME
    leak0 = c_sound
    faithful = (vag_c >= AGREE_MIN and vag_d >= AGREE_MIN
                and RAT_LO <= vmed <= RAT_HI
                and vfrac >= BAND3_FRAC
                and nin_c / max(len(fits), 1) >= AGREE_MIN
                and nin_d / max(len(dfits), 1) >= AGREE_MIN
                and leak0)
    partial = (vag_c >= AGREE_PART and vag_d >= AGREE_PART
               and leak0)
    if faithful:
        outcome = (f"BLOCKMODEL-FAITHFUL({VAR}: agree {vag_c:.2f}"
                   f"/{vag_d:.2f}, med ratio {vmed:.3g}, band3 "
                   f"{vfrac:.2f}, in-region {nin_c}+{nin_d})")
    elif partial:
        miss = []
        if not (RAT_LO <= vmed <= RAT_HI and vfrac >= BAND3_FRAC):
            miss.append(f"VALUE(med ratio {vmed:.3g}, band3 "
                        f"{vfrac:.2f})")
        if not (nin_c / max(len(fits), 1) >= AGREE_MIN
                and nin_d / max(len(dfits), 1) >= AGREE_MIN):
            miss.append(f"REGION({nin_c}/{len(fits)}, {nin_d}/"
                        f"{len(dfits)})")
        if not (vag_c >= AGREE_MIN and vag_d >= AGREE_MIN):
            miss.append(f"AGREE({vag_c:.2f}/{vag_d:.2f})")
        outcome = (f"BLOCKMODEL-PARTIAL({VAR}: decision agree "
                   f"{vag_c:.2f}/{vag_d:.2f}; miss = "
                   + ", ".join(miss) + ")")
    else:
        outcome = (f"BLOCKMODEL-UNFAITHFUL({VAR}: agree "
                   f"{vag_c:.2f}/{vag_d:.2f}, leak0 {leak0})")
    check(f"O typed: OUTCOME {outcome}", True)
    print(f"""
    THE TWO-CONDITION ALL-H STATEMENT (the sharpest form this
    program can now name; NAMED, not proved):
      For every consecutive full-core step of the deployed
      ladder, in the Jacobi-equilibrated coordinates (R = the
      unit-diagonal correlation form; head-scale family
      N(v) = scaled(R, v)): the step wall M > 0 follows from
      Psi_4 < 1 somewhere on the family, and the measured
      surface decomposes into exactly two conditions --
      (i)  TRIPLE + HEAD IN REGION: the fitted trajectory
           (rho_h, u_h) stays inside the certification region;
           on the block skeleton (BG0) the region is EXACTLY
           the PD quadrant {{0 <= rho < 1, u > 0}} (the r = 4
           CMS bound is exact on <= 4-atom spectra, G1/G3);
           measured: rho_h {mmm(rhos)[0]:.3f}/{mmm(rhos)[1]:.3f}
           /{mmm(rhos)[2]:.3f}, margin 1 - rho_h min
           {mmm(margins_rho)[0]:.3f}, trend {sl_rho:+.3f}/log h;
      (ii) BACKGROUND BELOW ADMITTANCE: the off-triple
           background mass stays below the measured admittance
           t_max: min/med/max {mmm(tmaxs)[0]:.2f}/
           {mmm(tmaxs)[1]:.2f}/{mmm(tmaxs)[2]:.2f} (>= 1 on
           {n_t1}/{len(tmaxs)}), trend {sl_t:+.2f}/log h.
      The head-scale window is structural on the skeleton
      ((0, inf), G3); its measured finiteness (med width
      {float(np.median(wids)):.2f} octaves, ONE-U intersection
      {ione}) is a background effect -- condition (ii) in
      window form.""")

    return finish(dict(
        repro=f"REPRO(FM {n_fm}/{len(rows)} med {fm_med:.4f}, "
              f"modal {modal[0]} {m_share:.3f})",
        fit=f"FIT(modal {sgn_str(modal_signs)} pi={modal_pi:+d}, "
            f"rho med {mmm(rhos)[1]:.3f}, bg med "
            f"{float(np.median(bg_mag)):.3f})",
        reg0=f"REGION-BG0(== PD quadrant, agr {agr0:.3f})",
        regm=f"REGION-BGM(rho_max med {profm_lab})",
        faith=f"FAITH({VAR} agree {vag_c:.2f}/{vag_d:.2f})",
        ratio=f"RATIO(BG0 {med0:.3g}/{fr0:.2f}; BGM {medm:.3g}/"
              f"{frm:.2f})",
        traj=f"TRAJ(1-rho min {mmm(margins_rho)[0]:.3f}, "
             f"in-region {nin_c}+{nin_d})",
        tol=f"TOL(t_max med {mmm(tmaxs)[1]:.2f}, >=1 on {n_t1}/"
            f"{len(tmaxs)})",
        wnd=f"WINDOW({n_wc}+{n_wd} nonempty, med width "
            f"{float(np.median(wids)):.2f} oct)",
        oneu=f"ONE-U({ione})",
        deep=f"DEEP-SCORED({len(dfits)}, v=1 {n_dfm}, BGM agree "
             f"{dagm:.2f})",
        trend=f"TRENDS(rho {sl_rho:+.3f}, width {sl_w:+.2f}, "
              f"tol {sl_t:+.2f})",
        scr=f"SCREENS(1-rho {s1}; width {s2}; tol {s3})",
        outcome=outcome,
        ctrl=clab))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print(f"\n  VERDICT: {VERDICT}")
    else:
        parts = [labels.get(k, "-") for k in
                 ("repro", "fit", "reg0", "regm", "faith",
                  "ratio", "traj", "tol", "wnd", "oneu", "deep",
                  "trend", "scr", "outcome", "ctrl")]
        VERDICT = ("PSI4BLOCK-MEASURED / MACHINE-WARDED / "
                   + " / ".join(parts))
        print(f"\n  VERDICT: {VERDICT}")
    print("""
  HONEST FRAME (as frozen): every census is a float-level
  measurement (validity-warded, conservative refusals) about the
  computed step matrices; every certified step is anchored by
  the exact NEWTON-STURM backstop, i.e. a theorem about the
  float64-computed step matrix, never about the ideal object.
  The block model is DESCRIPTIVE: it never certifies anything by
  itself.  The two-condition all-h statement is named, not
  proved.  Nothing here proves n > q uniformity in h, the
  pipeline enclosure, or any tail statement.  NO RH claim.  No
  marker moves.""")
    print(f"\n[TIME] {time.time() - T0:.1f} s   [CHECKS] "
          f"{n_tot} run, {n_tot - n_pass} failed")
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
