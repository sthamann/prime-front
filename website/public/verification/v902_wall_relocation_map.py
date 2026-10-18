#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v902 -- PRIME.CASE.EDGE.CHRISTOFFEL.01 + PRIME.PORT.GRAM.COMPLETION.01 + PRIME.PORT.RADAU.WEIGHT.01: THE WALL RELOCATION MAP -- the exact positive-weight rewrite of the soft pivot (1/d_12 = 1 + Sum W Q^2 - beta with W > 0 and beta >= 0 EXACTLY) together with the measured relocation diagnosis (1 - r TRACKS tau, slope +1.008: the uniform q < 1 target is the wall's own PD premise quantified, NOT an independent positivity source), and the moment-matrix identity of the wall vs the signed comb measure with the x = +1 edge obstruction (the Gram completion with W >= 0 fails on EVERY rung at the low-frequency edge while the Radau construction at the classical node is exact algebra), ONE module from two probes (22/22 + 23/23 checks, zero fails, verdicts EDGECHRISTOFFEL-MEASURED (REWRITE-EXACT / RATIO-BELOW-ONE(max-r-SENS=0.999950) / BETA-SEAT-SPREAD(med-self=0.475) / SAMEMEASURE-FAMILY(min-Jaccard=0.6776)) + GRAMRADAU-MEASURED (M0-IDENTITY-EXACT(4.9e-13) / GRAM-COMPLETION-FAILS(x2:42, m:42, p:0) / LOC-SCREEN-AMBIG(slope=+0.306) / RADAU-EXACT(3.8e-15) / RADAUW-SCREEN-PASS(slope=+0.138) / RADAU-PIVOT-UNRELATED(corr=+0.211) / LOCWALL-SEEN(42/42)); discovery probes case_edge_christoffel_probe.py (round 57) and wall_gram_radau_probe.py (round 59 wall-probe 3), 2026-08-10, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~14 s).  TYPED EXPLICITLY AS A RELOCATION/MECHANISM MAP, NOT PROGRESS: every identity here is a coordinate change of the wall's own PD premise; nothing gains positivity.  (1) THE EXACT REWRITE (case_edge_christoffel, 22/22): with q = (I-G)^{-1} p_* and Q = p^T q = K_sigma(y_*, .) (the sigma-reproducing kernel at the soft node) the v899 pivot identity splits EXACTLY into 1/d_12 = 1 + Sum_m (v_* w_m) Q(x_m)^2 - beta, beta = v_* nu_-[Q^2] >= 0; W_{h,m} = v_* w_m > 0 EXACTLY (min 9.7e-14, no tolerance), every beta term >= 0, self-term beta_{j*} = m_def^2 exact (5.8e-16); the identity verified against the INDEPENDENT slogdet route on all 37 full-window rungs (cancellation-aware ward).  (2) THE RELOCATION DIAGNOSIS (the honest core): the decisive ratio r_h = beta/(1 + SPOS) runs from 0.868 (h 142) to 0.99995007 (SENS max); EXACTLY 1 - r = (1/d_12)/(1 + SPOS); OLS slope of log(1 - r) vs log tau_full = +1.008 ((1-r)/tau quartiles 396/795/1311): r < 1 on EVERY deployed rung, but the distance to 1 IS tau -- pure RELOCATION; the Rayleigh fence r <= (1 - tau_full) SPOS/(1 + SPOS) holds with 0 violations (med saturation 0.9992) and is 147x tighter than the classical Christoffel trace bound; beta is WINDOW-SEATED (top-10 nodes med 0.993, 12-window coordinates med 0.988, self-term med 0.475); the two v899 halves read the SAME folded cosine quadrature family (support Jaccard 0.68-0.73; d1-exclusive mass EXACTLY 0 on all 37 -- the fluctuation flip d1 < 0 < d0 creates exactly the NEG support on which beta and the wall live).  (3) THE MOMENT-MATRIX IDENTITY AND THE EDGE OBSTRUCTION (wall_gram_radau, 23/23): M0 = I - H is EXACTLY the moment matrix of the signed comb measure nu = mu_+ - mu_- in the chain basis (two-route ward 4.9e-13; spectrum tie lam_min(M0) = tau at 5.2e-9) -- the wall statement IS 'nu >= 0 on squares of degree <= 2h-2'; but the Lukacs extension to the FULL [-1,1] positivity cone fails MEASURABLY on every rung: lam_min(M1x2) < 0 on 42/42 AND lam_min(Mm) < 0 on 42/42 (min -1.45e-04) while Mp = (1+x)-localization passes 42/42 -- the obstruction sits at the LOW-FREQUENCY x = +1 edge where the comb nodes accumulate; the violation magnitude OUTRUNS the wall margin (|floor|/tau med -12, to -152 at depth): there is NO source-only Gram representation M0 = F^T W F with W >= 0 at matched degree.  (4) THE RADAU PART (honest positive): the Golub construction at the classical node x* is exact (determinant quotient vs tridiagonal solve 2.9e-13, raw moments 3.8e-15, node hit 2.2e-16; weights >= 0 + Cauchy interlacing AUTOMATIC -- the classical positivity criteria CANNOT fail in this construction, declared honestly), and w*(x*) IS numerically the Christoffel function (w*/lambda_h(x*) med 0.9978) -- a pure mu_+ object with zero negative-family content; the P2 pivot is NOT a Radau weight (gap/w* spans 6e2..1e5).  SMOKE AMENDMENTS disclosed in-probe (fail-first preserved, wards TIGHTENED): the originally specified p-basis exactness ward was mathematically TAUTOLOGICAL and float-impossible at exterior ALHAT -> re-specified to raw-moment reproduction j <= 24; the G1.d screen read the positive floor subset which is EMPTY -> reads the magnitude.  CONTROLS FIRE in both probes: the smooth world breaks both premises (sigma indefinite + ratio-bound break; completion-fail is wall-sensitive: smooth LOCWALL-SEEN 42/42); Epstein (neg(A) 55) + scramble (37) fire; v899/christoffel_ratio reproduction wards green (deflation chain 2.0e-11, c-quartiles 1163/2117/2930, c(kz21) = 50667).  NO RH claim; no marker moves; closing the r_h route honestly means bounding tau from below -- the same single open object as everywhere, said, not hidden.

PROVENANCE: discovery probes case_edge_christoffel_probe.py (22/22,
EDGECHRISTOFFEL-MEASURED, SPEC frozen pre-run with the disclosed
cancellation-aware bar amendment, round 57, Spec-SHA 7a460405...)
and wall_gram_radau_probe.py (23/23, GRAMRADAU-MEASURED, SPEC
frozen pre-run with the two disclosed smoke amendments, round 59,
Spec-SHA dac37dfa...), both 2026-08-10, re-run identically at
promotion.  ROUND-31 EMBEDDING CONVENTION: frozen sources embedded
BYTE-EXACT, executed verbatim in isolated namespaces; printed spec
SHAs reproduce; byte-equality ward vs experiments/tfpt-discovery/
inside the pattern gates.  Both probes consume the READ-ONLY
deployed core v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles (AST firewalls inside
the probes); this module is a RELOCATION/MECHANISM MAP -- it
registers WHERE the wall's difficulty lives (the NEG support, the
x = +1 edge, the tau-tracking ratio), it does NOT narrow it; NO RH
claim.  Python-only per GATE.WOLFRAM.02.
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

# ------------- frozen probe source case_edge_christoffel_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""case_edge_christoffel_probe -- PRIME.CASE.EDGE.CHRISTOFFEL.01
(EXPLORATION ONLY, experiments/; round 57, the priority-1 item: do
the two v899 halves read the same measure?  The signed-functional
pivot identity is rewritten as a POSITIVE-WEIGHT norm square minus
an explicit nonnegative remainder, verified exactly, and the
decisive ratio is measured ladder-wide.  2026-08-10.)

THE QUESTION (frozen).  v899 holds two halves: (i) the softest
pivot of the wall window is EXACTLY a deflated-Christoffel
evaluation of the SIGNED functional sigma = mu_+ - nu_-,
    1/d_12,h = 1 + v_* K_sigma(y_*, y_*)
(christoffel_ratio_probe, round 55 -- the positivity premise of
sigma is the wall's own PD premise, an honesty fence); (ii) the
periodic full-weight completion makes the pair-kernel frequency
weights W_{f,m} >= 0 exactly, a genuine norm square, at the price
of an explicit boundary term (edge_defect_kill_probe, round 56;
carried max |beta_pair|/margin~ = 0.21).  DO THESE TWO READ THE
SAME MEASURE -- can the pivot identity itself be rewritten as
    1/d_12,h = 1 + sum_m W_{h,m} |P_h(t_{h,m})|^2 - beta_h,
with ALL W_{h,m} >= 0 and beta_h an explicit nonnegative
endpoint/boundary-side term?

THE CONSTRUCTION (frozen; exact algebra derived a priori).  On
the full wall A = I - E, E = B B^T (christoffel_ratio (iii)
verbatim): G = B^T B is the Gram of nu_- in the mu_+-orthonormal
basis p_k; with p_* = p(y_*) and
    q := (I_h - G)^{-1} p_*,   Q(t) := p(t)^T q = K_sigma(y_*, t)
(the sigma-reproducing kernel at the soft node: (I-G) q = p_* is
exactly sigma[Q p_k] = p_k(y_*) for all k < h), the reproducing
property gives sigma[Q^2] = Q(y_*) = p_*^T q = m_def / v_*, and
sigma[Q^2] = mu_+[Q^2] - nu_-[Q^2] splits the pivot identity
EXACTLY into
    1/d_12 = 1 + SPOS_h - beta_h,
    SPOS_h = v_* mu_+[Q^2] = sum_s (v_* w_s) Q(x_s)^2   [W >= 0]
    beta_h = v_* nu_-[Q^2] = sum_j (v_* v_j) Q(y_j)^2   [>= 0],
i.e. W_{h,m} := v_* w_m (product of two constructional
nonnegative quadrature weights), P_h := Q, t_{h,m} := x_m -- the
POSITIVE part of the SAME folded cosine family the pair-kernel
weights read, and beta_h is carried ENTIRELY by the NEG-node
support (the boundary side of the same family, where the wall
operator lives), with the exact self-term beta_{h,j*} = m_def^2.
SO THE FROZEN ANSWER SHAPE: YES as an exact rewrite over the same
constructional family (measured below, incl. the d1-vs-d0
endpoint mismatch between the two v899 halves), and the price is
the measured ratio
    r_h := beta_h / (1 + SPOS_h)  in [0, 1)  on PD rungs,
with the EXACT complements 1 - r_h = (1/d_12)/(1 + SPOS_h) and
the Rayleigh fence r_h <= (1 - tau_full) SPOS/(1 + SPOS) < 1 --
the fence is the wall's own PD premise made quantitative: the
open uniform target q < 1 is EQUIVALENT on this surface to a
lower bound on tau_full.  Said plainly, incl. the plan nuance:
the incoming plan's "<= ~0.21" belongs to the PAIR-contract
boundary carry (v899(3)), a DIFFERENT functional; the decisive
ratio here is r_h and is expected to approach 1 at the rate of
tau -- the measurement below quantifies exactly that.

FROZEN PROTOCOL (machinery verbatim from christoffel_ratio_probe
round 55; PNT continuum lags verbatim from edge_defect_kill_probe
round 56 for the E4 endpoint comparison):

 W   PIPELINE + REPRODUCTION WARDS (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W0 truth ladder == 42 rungs; W0c full-window
     census == 37; W-C1a d_12 minor-quotient == inverse route
     (rel <= 1e-9, minor signs +1); W-C1c deflation chain 1/d_12
     == 1 + m_def (conditioning-aware bar, verbatim); W-C1d
     c >= 1 and tau_12 > 0 on every full rung; W-C1f c-quartile
     reproduction 1163/2117/2930 and c(kz21) = 50667 at h = 371
     (rtol 2e-2); W-SPOT (2 shallowest full rungs): the folded
     positive measure == (qt_f d1_f)_{d1 > 0} EXACTLY (rel <=
     1e-12) -- the 'same constructional family' claim warded
     against the pair-kernel quadrature rule.

 E1  THE REWRITE, EXACTLY (per full-window rung; kill ->
     WARD-BROKEN):
       E1.a  SPOS two routes: v_* |q|^2 (orthonormality route)
             == explicit quadrature sum_s (v_* w_s)(P_pos_s q)^2,
             rel <= QUAD_WARD;
       E1.b  beta two routes: v_* q^T G q == explicit sum_j
             (v_* v_j)(P_neg_j q)^2, rel <= GEXACT_WARD;
       E1.c  THE IDENTITY: 1/d_12 == 1 + SPOS - beta against the
             INDEPENDENT 12-window slogdet route, rel <=
             bar_h = max(CHR_WARD_FLOOR, CANC_FAC x EPS x
             (1 + SPOS + beta) x d_12) per rung (the honest
             cancellation floor: SPOS and beta are individually
             large and their difference is 1/d_12 - 1);
       E1.d  NONNEGATIVITY, EXACT: min_m W_{h,m} > 0 and every
             beta term >= 0 (squares times constructional
             weights; exact float signs, no tolerance);
       E1.e  SELF-TERM: the j* contribution to beta ==
             m_def^2 exactly (rel <= SELF_WARD).

 E2  THE DECISIVE RATIO (measured, typed): the full ladder (kz,
     h, m_def, SPOS, beta, r_h, 1 - r_h, (1-r_h)/tau_full,
     fence); WARDS (kill -> WARD-BROKEN): E2.a the complement
     identity 1 - r == (1/d_12)/(1 + SPOS), rel <= the SAME
     cancellation-aware bar as E1.c (1 - r inherits the
     SPOS - beta cancellation floor exactly);
     E2.b the Rayleigh fence r <= (1 - tau_full) SPOS/(1 + SPOS)
     (exact algebra, slack printed).  MEASURED: max r RAW (37)
     and SENS (kz-21 excluded, round-53 rule); OLS slope of
     log(1 - r) vs log tau_full and vs log h; quartiles of
     (1 - r)/tau_full.  TYPED (never kills): RATIO-BELOW-ONE(max
     r SENS) -- with the honest print that 1 - r_h tracks
     tau_full (the uniform q < 1 target is NOT achieved as an
     independent statement; it is the wall in new clothes,
     quantified).

 E3  WHERE beta LOCALIZES (measured): per rung the top
     beta-contribution anatomy -- self-term share m_def^2/beta,
     top-node fold index vs j* (= window coordinate 12), top-10
     node share, share carried by the 12-window coordinates
     JWIN; the CLASSICAL EVALUATION CONTROL: per neg node
     Q(y_j)^2 <= K_mu(y_j, y_j) |q|^2 (Cauchy-Schwarz in the
     mu_+ inner product; ward, exact up to CS_TOL) and the two
     aggregate bounds compared: beta / [v_* (1 - tau_full)
     |q|^2] (Rayleigh, sharp side) vs beta / [v_* tr(G) |q|^2]
     (classical evaluation bound; slack = how lossy the
     classical Christoffel evaluation inequality is here).
     TYPED: BETA-SEAT-SOFT(med self-share) iff the median
     self-term share >= 0.5, else BETA-SEAT-SPREAD(med).

 E4  THE SAME-MEASURE COMPARISON (the two v899 halves; measured,
     typed): per full-window rung build the t = 0 endpoint
     density d0 (arch + closed-form PNT continuum lags, verbatim
     cont_lags) next to the deployed truth density d1; the
     pair-kernel weights of v899(2)/(3) read the family
     (x_f, qt_f d0_f)_{d0 > 0}; the pivot rewrite reads
     (x_f, qt_f d1_f)_{d1 > 0} (W-SPOT ward) x v_*.  Measured
     per rung: positive-support overlap |{d0>0} cap {d1>0}| /
     |union|, the weight ratio stats on the common support, the
     exclusive-node mass shares; the round-50 heavy rungs kz
     {12, 13, 26, 40} printed as rows (kz 9 is below the 42-rung
     census floor h = 142 -- disclosed, not comparable here).
     TYPED: SAMEMEASURE-FAMILY(min overlap) -- same folded
     cosine quadrature family, same weight rule, DIFFERENT
     endpoint density (d1 truth vs d0 smooth reference) and
     different integrand (Q^2 vs p_{0,m}^2); if E1 had failed
     (any W < 0 or identity broken) the type would be
     SAMEMEASURE-OBSTRUCTED(channel) with the exact obstruction
     printed -- first-class outcome either way.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C-S smooth world
     (B1 masses, verbatim): sigma indefinite (tau_full < 0) on
     >= 1 smooth rung AND the rewrite's ratio bound breaks off
     the truth comb -- on >= 1 smooth full-window rung r >= 1 or
     tau_12 <= 0 or d_12 <= 0; C-E Epstein x^2+5y^2 comb +
     scramble (seed 1) at kz 9: frame death or neg(A) > 0 or
     tau_12 <= 0; channel printed.

KILLS: KP a W pipeline ward breaks -> PIPELINE-BROKEN; KW an
E1/E2 ward or control breaks -> WARD-BROKEN.  E2/E3/E4 typed
labels report, never kill.

VERDICT (frozen enum): EDGECHRISTOFFEL-MEASURED with typed
sublabels REWRITE-EXACT, RATIO-BELOW-ONE(max r), BETA-SEAT-SOFT /
BETA-SEAT-SPREAD, SAMEMEASURE-FAMILY(overlap) /
SAMEMEASURE-OBSTRUCTED(channel); else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS: H_DEEP_MAX = 900; JWIN = (2,...,24); NW = 12;
N_RUNGS_EXP = 42; N_FULLWIN_FROZEN = 37; KZ_STAR = 21; H_STAR =
371; REF_C21 = 50667, REF_Q25/MED/Q75 = 1163/2117/2930 (rtol
2e-2); ID_WARD = 1e-9; CHR_WARD_FLOOR = 1e-8; CHR_COND_FAC =
1e3; CGE1_WARD = 1e-9; N_SPOT = 2; H_SPOT_MAX = 150; MEAS_WARD =
1e-12; QUAD_WARD = 1e-6; GEXACT_WARD = 1e-10; CANC_FAC = 1e4;
SELF_WARD = 1e-8; CS_TOL = 1e-10; SEAT_BAR = 0.5; HEAVY_SHARED =
(12, 13, 26, 40); CTRL_KZ = 9; scramble seed 1; EPS =
2.220446049250313e-16.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): one smoke run
of this script with the identical construction fixed the
float-floor bars that could not be set a priori and NEVER
weakened an exact claim (E1.d nonnegativity stays exact, zero
tolerance): (i) QUAD_WARD 1e-6 (smoke max 9.2e-13; the Lanczos
orthonormality floor under a 1/tau_full-amplified q); (ii)
SELF_WARD 1e-8 (smoke 5.8e-16); (iii) the E2.a complement
identity FAILED its naive first bar 1e-10 at smoke max rel
7.6e-9 -- correctly: 1 - r inherits the SPOS - beta cancellation
EXACTLY, so its bar was changed to the SAME cancellation-aware
form as E1.c (fail-first preserved: the smoke FAIL is recorded
here, no measured quantity moved); (iv) CANC_FAC was raised 1e3
-> 1e4 after the smoke run showed worst dev/bar 0.761 (an
honest-margin widening of a float floor, not a content bar).
The smoke run also confirmed the a-priori expectation printed in
the construction paragraph (r_h -> 1 with 1 - r_h tracking
tau_full; smoke max r SENS = 0.99995).  No census count, no
enum, no typed rule was changed after the smoke run.

SPEC v1 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
window memoization per (kz, seed); (ii) ONE Gram per rung, the
factor-Gram spectral identity for tau_full (christoffel_ratio
verbatim); (iii) q via one symmetric solve of (I - G); P_pos =
eval_chain at the positive nodes (same chain); (iv) SENS
statistics = leave-kz-21-out (round-53 rule), raw always printed;
(v) E4 support sets are {1 <= f <= F-2 : d > 0} (f = 0 and the
top fold carry zero or endpoint qt weight; the folded family of
the pivot rewrite is warded against exactly this rule in W-SPOT);
(vi) slogdet signs warded +1.

NO RH claim: the rewrite is exact finite linear algebra on the
deployed v563 window family; W >= 0 and beta >= 0 are
constructional; NOTHING here proves r_h <= q < 1 uniformly --
the measured fence says that statement IS the wall's PD premise
quantitatively.  The pair-correlation-class conditionality of
the diagonal route (v889/v899) is untouched.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.

Sources (read-only): v563_paper2_readouts; wall/window/deflation
machinery verbatim from christoffel_ratio_probe.py (round 55,
promoted v899); PNT continuum closed-form lags verbatim from
edge_defect_kill_probe.py (round 56, promoted v899); pair-kernel
weight family per kernel_sos_probe / edge_defect_kill_probe
(declared reading, not rebuilt); v884/v887/v897 certified base --
declared inputs.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/case_edge_christoffel_probe.py
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

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
NW = 12
N_RUNGS_EXP = 42
N_FULLWIN_FROZEN = 37
KZ_STAR = 21
H_STAR = 371
REF_C21 = 50667.0
REF_Q25, REF_MED, REF_Q75 = 1163.0, 2117.0, 2930.0
REF_RTOL = 2e-2
ID_WARD = 1e-9
CHR_WARD_FLOOR = 1e-8
CHR_COND_FAC = 1e3
CGE1_WARD = 1e-9
N_SPOT = 2
H_SPOT_MAX = 150
MEAS_WARD = 1e-12              # W-SPOT folded == qt d
QUAD_WARD = 1e-6               # E1.a (smoke-fixed, see header)
GEXACT_WARD = 1e-10            # E1.b
CANC_FAC = 1e4                 # E1.c/E2.a cancellation factor
SELF_WARD = 1e-8               # E1.e (smoke-fixed)
CS_TOL = 1e-10                 # E3 Cauchy-Schwarz tolerance
SEAT_BAR = 0.5                 # E3 typing bar
HEAVY_SHARED = (12, 13, 26, 40)
CTRL_KZ = 9
EPS = 2.220446049250313e-16
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


# --------- pipeline, verbatim (christoffel_ratio_probe chain)
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


def smooth_masses(uu):
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) \
        * cell_widths(np.asarray(uu, float))


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


def _prim(u, A, B):
    """Primitive of (A + B u) 2 e^{u/2} (edge_defect verbatim)."""
    return 4.0 * np.exp(0.5 * u) * (A + B * (u - 2.0))


def cont_lags(alpha, M, seg_lo, seg_hi, seg_sc):
    """Closed-form PNT tent lags (edge_defect verbatim)."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    for lo, hi, sc in zip(seg_lo, seg_hi, seg_sc):
        i0 = max(0, int(math.floor(lo / D)) - 1)
        i1 = min(M - 1, int(math.ceil(hi / D)) + 1)
        ii = np.arange(i0, i1 + 1, dtype=float)
        val = np.zeros(len(ii))
        a = np.maximum((ii - 1.0) * D, lo)
        b = np.minimum(ii * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 - ii[m], 1.0 / D)
                   - _prim(a[m], 1.0 - ii[m], 1.0 / D))
        a = np.maximum(ii * D, lo)
        b = np.minimum((ii + 1.0) * D, hi)
        m = b > a
        val[m] += (_prim(b[m], 1.0 + ii[m], -1.0 / D)
                   - _prim(a[m], 1.0 + ii[m], -1.0 / D))
        if i0 == 0:
            a0, b0 = max(0.0, lo), min(D, hi)
            if b0 > a0:
                val[0] += (_prim(b0, 1.0, -1.0 / D)
                           - _prim(a0, 1.0, -1.0 / D))
        c[i0:i1 + 1] -= 0.5 * sc * val
    return c


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


def anatomy(kz, scramble_seed=None, comb=None, keep_all=False):
    """One rung -> Gram, 12-window compression, deflated mass
    (christoffel_ratio verbatim), EXTENDED (keep_all): the folded
    positive/negative measures, the chain, Pn and G are retained
    for the E1 rewrite."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    d = grid_density(rr["c_ar"] + np.asarray(c_at, float))
    L = 2 * M - 2
    xs, ws, uf_p = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    B = np.sqrt(vs)[:, None] * Pn
    E = B @ B.T
    E = 0.5 * (E + E.T)
    n = E.shape[0]
    out = dict(kz=kz, h=h, n=n, M=M, L=L, D=D,
               alpha=float(alpha))
    G = B.T @ B
    G = 0.5 * (G + G.T)
    egG = np.linalg.eigvalsh(G)
    out["tau_full"] = float(1.0 - egG[-1])
    out["negA"] = int(np.sum(egG > 1.0))
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if out["full"]:
        iw = [idx[j] for j in jav]
        io = [k for k in range(n) if k not in set(iw)]
        IO = np.eye(len(io)) - E[np.ix_(io, io)]
        try:
            CJ = (E[np.ix_(iw, iw)]
                  + E[np.ix_(iw, io)] @ np.linalg.solve(
                      IO, E[np.ix_(io, iw)]))
            out["CJ"] = 0.5 * (CJ + CJ.T)
        except np.linalg.LinAlgError:
            out["full"] = False
    if out["full"]:
        jstar = idx[JWIN[-1]]
        p = Pn[jstar]
        qvec = np.linalg.solve(np.eye(h) - G, p)
        out["jstar"] = jstar
        out["vstar"] = float(vs[jstar])
        out["m_def"] = float(vs[jstar] * (p @ qvec))
        if keep_all:
            out["qvec"] = qvec
            out["Pn"] = Pn
            out["G"] = G
            out["vs"] = vs
            out["ws"] = ws
            out["xs"] = xs
            out["uf_p"] = uf_p
            out["uf_n"] = uf_n
            out["chain"] = (al, be, m0)
            out["d1"] = d
    return out


def win_attrs(r):
    """12-window objects (christoffel_ratio verbatim, trimmed)."""
    A = np.eye(NW) - r["CJ"]
    sg12, ld12 = np.linalg.slogdet(A)
    sg11, ld11 = np.linalg.slogdet(A[:11, :11])
    r["sg_ok"] = (sg12 == 1.0 and sg11 == 1.0)
    r["d12"] = math.exp(ld12 - ld11) * sg12 * sg11
    ew = np.linalg.eigvalsh(A)
    r["tau12"] = float(ew[0])
    Ainv = np.linalg.inv(A)
    r["a1212"] = float(Ainv[11, 11])
    r["c"] = r["d12"] / r["tau12"] if r["tau12"] != 0.0 \
        else float("inf")
    r["dev_inv"] = (abs(r["d12"] - 1.0 / r["a1212"])
                    / max(abs(r["d12"]), 1e-300))
    r["dev_chr"] = (abs(1.0 / r["d12"] - (1.0 + r["m_def"]))
                    / max(abs(1.0 / r["d12"]), 1e-300))
    return r


def quartiles(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return float(q[0]), float(q[1]), float(q[2])


def ols_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    xm, ym = float(np.mean(x)), float(np.mean(y))
    return float(np.sum((x - xm) * (y - ym))
                 / np.sum((x - xm) ** 2))


def main():
    section("PRIME.CASE.EDGE.CHRISTOFFEL.01 -- the pivot identity "
            "as a positive norm square minus an explicit "
            "remainder (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- ladders + reproduction wards (christoffel_ratio "
            "chain, ONE Gram per rung)")
    truth, smooth = [], []
    n_toodeep, n_dead_t, n_dead_s = 0, 0, 0
    for kz in core.frame_a_zones():
        r = anatomy(kz, keep_all=True)
        if r == "TOO-DEEP":
            n_toodeep += 1
            continue
        if r is None:
            n_dead_t += 1
            continue
        truth.append(r)
        uu = window_of(kz)["uu"]
        rs = anatomy(kz, comb=(uu, smooth_masses(uu)))
        if isinstance(rs, dict):
            smooth.append(rs)
        else:
            n_dead_s += 1
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    smooth.sort(key=lambda r: (r["h"], r["kz"]))
    print("    truth %d rungs (h %d..%d; %d TOO-DEEP, %d dead) | "
          "smooth %d rungs (%d dead)  [%.1f s]"
          % (len(truth), truth[0]["h"], truth[-1]["h"], n_toodeep,
             n_dead_t, len(smooth), n_dead_s, time.time() - T0))
    check("W0 truth ladder == %d rungs" % N_RUNGS_EXP,
          len(truth) == N_RUNGS_EXP, "%d" % len(truth), kill="KP")
    fullw = [r for r in truth if r.get("full") and "CJ" in r]
    check("W0c full-window census %d == %d"
          % (len(fullw), N_FULLWIN_FROZEN),
          len(fullw) == N_FULLWIN_FROZEN, kill="KP")
    if KILLS:
        return finish({})
    for r in fullw:
        win_attrs(r)
    sg_all = all(r["sg_ok"] for r in fullw)
    dev_inv = max(r["dev_inv"] for r in fullw)
    check("W-C1a d_12 minor-quotient == inverse route: max rel "
          "%.1e <= %.0e; minor signs +1: %s"
          % (dev_inv, ID_WARD, sg_all),
          dev_inv <= ID_WARD and sg_all, kill="KW")
    chr_worst = max(r["dev_chr"]
                    / max(CHR_WARD_FLOOR,
                          CHR_COND_FAC * EPS / r["tau_full"])
                    for r in fullw)
    check("W-C1c deflation chain 1/d_12 == 1 + m_def: worst "
          "dev/bar %.3f <= 1 (max rel %.1e)"
          % (chr_worst, max(r["dev_chr"] for r in fullw)),
          chr_worst <= 1.0, kill="KW")
    c_min = min(r["c"] for r in fullw)
    tau_min = min(r["tau12"] for r in fullw)
    check("W-C1d c >= 1 (min %.3f) and tau_12 > 0 (min %.3e)"
          % (c_min, tau_min),
          c_min >= 1.0 - CGE1_WARD and tau_min > 0.0, kill="KW")
    cs = np.array([r["c"] for r in fullw])
    q1, q2, q3 = quartiles(cs)
    star = [r for r in fullw if r["kz"] == KZ_STAR]
    c21 = star[0]["c"] if star else float("nan")
    h21 = star[0]["h"] if star else -1
    check("W-C1f REPRODUCTION c-quartiles %.0f/%.0f/%.0f == "
          "%.0f/%.0f/%.0f, c(kz%d) %.0f == %.0f at h %d "
          "(rtol %.0e)"
          % (q1, q2, q3, REF_Q25, REF_MED, REF_Q75, KZ_STAR, c21,
             REF_C21, h21, REF_RTOL),
          abs(q1 / REF_Q25 - 1.0) <= REF_RTOL
          and abs(q2 / REF_MED - 1.0) <= REF_RTOL
          and abs(q3 / REF_Q75 - 1.0) <= REF_RTOL
          and abs(c21 / REF_C21 - 1.0) <= REF_RTOL
          and h21 == H_STAR, kill="KW")
    # W-SPOT: the folded positive measure == (qt d1)_{d1>0}
    spot = [r for r in fullw if r["h"] <= H_SPOT_MAX][:N_SPOT]
    dev_meas = 0.0
    for r in spot:
        L, M = r["L"], r["M"]
        F = L // 2 + 1
        d1F = r["d1"][:F]
        ff = np.arange(F)
        mult = np.where((ff == 0) | (ff == L // 2), 1.0, 2.0)
        qt = mult * 4.0 * np.sin(math.pi * ff / L) ** 2 \
            / (2.0 * L)
        wq = {int(f): float(qt[f] * d1F[f]) for f in range(1, F)
              if d1F[f] > 0.0}
        wf = {int(f): float(w) for f, w in zip(r["uf_p"],
                                               r["ws"])}
        keys = set(wq) | set(k for k in wf if k >= 1)
        for f in keys:
            a_, b_ = wq.get(f, 0.0), wf.get(f, 0.0)
            dev_meas = max(dev_meas, abs(a_ - b_)
                           / max(abs(a_), abs(b_), 1e-300))
    check("W-SPOT folded positive measure == (qt_f d1_f)_{d1>0} "
          "on %d spot rungs: max rel %.1e <= %.0e (the SAME "
          "quadrature family as the pair-kernel weights)"
          % (len(spot), dev_meas, MEAS_WARD),
          len(spot) == N_SPOT and dev_meas <= MEAS_WARD,
          kill="KW")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ E1
    section("E1 -- THE REWRITE: 1/d_12 = 1 + sum W |Q|^2 - beta "
            "(exact, per full rung)")
    dev_quad = dev_gex = dev_id = dev_self = 0.0
    minW_all = float("inf")
    minbt_all = float("inf")
    for r in fullw:
        q = r["qvec"]
        al, be, m0 = r["chain"]
        h = r["h"]
        v_ = r["vstar"]
        # E1.a SPOS two routes
        spos_o = v_ * float(q @ q)
        Ppos = eval_chain(al, be, m0, r["xs"], h)
        Qpos = Ppos @ q
        spos_q = v_ * float(r["ws"] @ (Qpos * Qpos))
        dev_quad = max(dev_quad, abs(spos_o - spos_q)
                       / max(abs(spos_o), 1e-300))
        # E1.b beta two routes
        beta_g = v_ * float(q @ (r["G"] @ q))
        Qneg = r["Pn"] @ q
        bterms = v_ * r["vs"] * (Qneg * Qneg)
        beta_q = float(np.sum(bterms))
        dev_gex = max(dev_gex, abs(beta_g - beta_q)
                      / max(abs(beta_g), 1e-300))
        # E1.c identity vs the independent 12-window route
        lhs = 1.0 / r["d12"]
        rhs = 1.0 + spos_q - beta_q
        bar = max(CHR_WARD_FLOOR,
                  CANC_FAC * EPS * (1.0 + spos_q + beta_q)
                  * r["d12"])
        dev_id = max(dev_id, (abs(lhs - rhs) / abs(lhs)) / bar)
        # E1.d exact nonnegativity
        minW_all = min(minW_all, v_ * float(np.min(r["ws"])))
        minbt_all = min(minbt_all, float(np.min(bterms)))
        # E1.e self-term == m_def^2
        bself = float(bterms[r["jstar"]])
        dev_self = max(dev_self, abs(bself - r["m_def"] ** 2)
                       / max(r["m_def"] ** 2, 1e-300))
        r["SPOS"] = spos_q
        r["beta"] = beta_q
        r["bterms"] = bterms
        r["bself"] = bself
        r["normq2"] = float(q @ q)
    check("E1.a SPOS orthonormality route == explicit quadrature "
          "route: max rel %.1e <= %.0e" % (dev_quad, QUAD_WARD),
          dev_quad <= QUAD_WARD, kill="KW")
    check("E1.b beta Gram route == explicit node route: max rel "
          "%.1e <= %.0e" % (dev_gex, GEXACT_WARD),
          dev_gex <= GEXACT_WARD, kill="KW")
    check("E1.c THE IDENTITY 1/d_12 == 1 + SPOS - beta vs the "
          "independent slogdet route: worst dev/bar %.3f <= 1 "
          "(cancellation-aware bar, see spec)" % dev_id,
          dev_id <= 1.0, kill="KW")
    check("E1.d NONNEGATIVITY EXACT: min W_{h,m} = %.3e > 0 and "
          "min beta term = %.3e >= 0 (no tolerance)"
          % (minW_all, minbt_all),
          minW_all > 0.0 and minbt_all >= 0.0, kill="KW")
    check("E1.e self-term beta_{j*} == m_def^2: max rel %.1e <= "
          "%.0e" % (dev_self, SELF_WARD), dev_self <= SELF_WARD,
          kill="KW")
    check("E1.f typed: REWRITE-EXACT (the two v899 halves DO "
          "read one measure family: positive part -> the norm "
          "square, negative part -> beta)", True)

    # ------------------------------------------------------------ E2
    section("E2 -- THE DECISIVE RATIO r_h = beta/(1 + SPOS)")
    dev_comp = 0.0
    fence_viol = 0
    rows = []
    print("    kz   h    m_def      SPOS       beta       "
          "r_h        1-r_h      (1-r)/tau  fence-r")
    for r in fullw:
        rh = r["beta"] / (1.0 + r["SPOS"])
        comp = (1.0 / r["d12"]) / (1.0 + r["SPOS"])
        bar = max(CHR_WARD_FLOOR,
                  CANC_FAC * EPS * (1.0 + r["SPOS"] + r["beta"])
                  * r["d12"])
        dev_comp = max(dev_comp, (abs((1.0 - rh) - comp)
                                  / max(abs(comp), 1e-300))
                       / bar)
        fence = ((1.0 - r["tau_full"]) * r["SPOS"]
                 / (1.0 + r["SPOS"]))
        if rh > fence * (1.0 + 1e-12):
            fence_viol += 1
        r["r_h"] = rh
        r["fence"] = fence
        rows.append(r)
        print("    %-4d %-4d %.3e  %.3e  %.3e  %.6f  %.3e  "
              "%8.3f  %.3e%s"
              % (r["kz"], r["h"], r["m_def"], r["SPOS"],
                 r["beta"], rh, 1.0 - rh,
                 (1.0 - rh) / r["tau_full"], fence - rh,
                 "   <-- kz-21" if r["kz"] == KZ_STAR else ""),
              flush=True)
    check("E2.a complement identity 1 - r == (1/d_12)/(1 + "
          "SPOS): worst dev/bar %.3f <= 1 (cancellation-aware "
          "bar as E1.c)" % dev_comp, dev_comp <= 1.0, kill="KW")
    check("E2.b Rayleigh fence r <= (1 - tau_full) SPOS/(1 + "
          "SPOS) on every rung (violations: %d)" % fence_viol,
          fence_viol == 0, kill="KW")
    rr_all = np.array([r["r_h"] for r in rows])
    sens = [r for r in rows if r["kz"] != KZ_STAR]
    rr_s = np.array([r["r_h"] for r in sens])
    one_m = 1.0 - rr_all
    ratio_tau = np.array([(1.0 - r["r_h"]) / r["tau_full"]
                          for r in rows])
    sl_tau = ols_slope(np.log([r["tau_full"] for r in rows]),
                       np.log(one_m))
    sl_h = ols_slope(np.log([r["h"] for r in rows]),
                     np.log(one_m))
    qa, qb, qc = quartiles(ratio_tau)
    print("\n    max r RAW = %.8f (%d rungs) | SENS = %.8f (%d); "
          "min r = %.6f"
          % (float(np.max(rr_all)), len(rr_all),
             float(np.max(rr_s)), len(rr_s),
             float(np.min(rr_all))))
    print("    trend: OLS slope log(1-r) vs log tau_full = "
          "%+.4f; vs log h = %+.4f" % (sl_tau, sl_h))
    print("    (1-r)/tau_full quartiles: %.2f / %.2f / %.2f "
          "(range [%.2f, %.2f])"
          % (qa, qb, qc, float(np.min(ratio_tau)),
             float(np.max(ratio_tau))))
    print("    HONEST READING: r < 1 on every deployed rung, "
          "but 1 - r_h TRACKS tau_full (slope ~ 1) -- the "
          "uniform q < 1 target is the wall's PD premise "
          "quantified, NOT an independent gain.")
    e2 = "RATIO-BELOW-ONE(max-r-SENS=%.6f)" % float(np.max(rr_s))
    check("E2.c typed: %s" % e2, True)

    # ------------------------------------------------------------ E3
    section("E3 -- WHERE beta LOCALIZES + the classical "
            "evaluation control")
    cs_worst = 0.0
    selfsh = []
    winsh = []
    top10 = []
    ray_r = []
    cls_r = []
    print("    kz   h    self-share top-fold(j*?)  top10-share "
          "JWIN-share  beta/Rayleigh beta/classical")
    for r in rows:
        bt = r["bterms"]
        beta = r["beta"]
        share_self = r["bself"] / beta
        selfsh.append(share_self)
        order = np.argsort(-bt)
        tf = int(r["uf_n"][order[0]])
        t10 = float(np.sum(bt[order[:10]]) / beta)
        top10.append(t10)
        jw = set(JWIN)
        wsh = float(np.sum([b for b, f in zip(bt, r["uf_n"])
                            if int(f) in jw]) / beta)
        winsh.append(wsh)
        # Cauchy-Schwarz per node: Q(y)^2 <= K_mu(y,y) |q|^2
        Kmu = np.sum(r["Pn"] ** 2, axis=1)
        Qn2 = (r["Pn"] @ r["qvec"]) ** 2
        cs_worst = max(cs_worst, float(np.max(
            Qn2 / (Kmu * r["normq2"]))))
        rayb = (r["vstar"] * (1.0 - r["tau_full"]) * r["normq2"])
        clsb = (r["vstar"] * float(np.trace(r["G"]))
                * r["normq2"])
        ray_r.append(beta / rayb)
        cls_r.append(beta / clsb)
        print("    %-4d %-4d %.6f   %5d (%s)     %.4f      "
              "%.4f      %.6f      %.3e"
              % (r["kz"], r["h"], share_self, tf,
                 "=j*" if order[0] == r["jstar"] else "no",
                 t10, wsh, ray_r[-1], cls_r[-1]), flush=True)
    check("E3.a Cauchy-Schwarz evaluation control Q(y)^2 <= "
          "K_mu(y,y) |q|^2: worst ratio %.6f <= 1 + %.0e"
          % (cs_worst, CS_TOL), cs_worst <= 1.0 + CS_TOL,
          kill="KW")
    med_self = float(np.median(selfsh))
    print("\n    self-term share m_def^2/beta: med %.4f (range "
          "[%.4f, %.4f]); top-10 share med %.4f; JWIN share med "
          "%.4f" % (med_self, float(np.min(selfsh)),
                    float(np.max(selfsh)),
                    float(np.median(top10)),
                    float(np.median(winsh))))
    print("    aggregate bounds: beta/Rayleigh med %.4f (sharp "
          "side; = the fence content) vs beta/classical-trace "
          "med %.3e (the classical Christoffel evaluation "
          "inequality is %.0fx lossier here)"
          % (float(np.median(ray_r)), float(np.median(cls_r)),
             float(np.median(ray_r)) / max(float(np.median(
                 cls_r)), 1e-300)))
    e3 = ("BETA-SEAT-SOFT(med-self=%.3f)" % med_self
          if med_self >= SEAT_BAR
          else "BETA-SEAT-SPREAD(med-self=%.3f)" % med_self)
    check("E3.b typed: %s" % e3, True)

    # ------------------------------------------------------------ E4
    section("E4 -- THE SAME-MEASURE COMPARISON (pivot rewrite "
            "family vs pair-kernel family)")
    print("    pivot rewrite reads (x_f, qt_f d1_f)_{d1>0} x v_* "
          "(truth endpoint); pair-kernel weights read "
          "(x_f, qt_f d0_f)_{d0>0} (t = 0 endpoint).")
    print("    kz 9 of the round-50 heavy set is below the "
          "42-rung census floor (h = 142) -- disclosed, not "
          "comparable here.")
    ovls = []
    print("    kz   h    |P1|   |P0|   overlap  Jaccard  "
          "wratio med [min, max]   excl-mass d1  excl-mass d0")
    for r in rows:
        L, M = r["L"], r["M"]
        F = L // 2 + 1
        w = window_of(r["kz"])
        c0 = cont_lags(r["alpha"], M, [0.0],
                       [2.0 * r["alpha"]], [1.0])
        d0F = grid_density(w["c_ar"] + c0)[:F]
        d1F = r["d1"][:F]
        ff = np.arange(1, F - 1)
        qt = 2.0 * 4.0 * np.sin(math.pi * ff / L) ** 2 \
            / (2.0 * L)
        p1 = ff[d1F[1:F - 1] > 0.0]
        p0 = ff[d0F[1:F - 1] > 0.0]
        s1, s0 = set(p1.tolist()), set(p0.tolist())
        com = np.array(sorted(s1 & s0), dtype=int)
        jac = len(com) / max(len(s1 | s0), 1)
        ovls.append(jac)
        w1 = qt[com - 1] * d1F[com]
        w0 = qt[com - 1] * d0F[com]
        rat = w1 / w0
        m1 = float(np.sum(qt[p1 - 1] * d1F[p1]))
        m0_ = float(np.sum(qt[p0 - 1] * d0F[p0]))
        ex1 = np.array(sorted(s1 - s0), dtype=int)
        ex0 = np.array(sorted(s0 - s1), dtype=int)
        xm1 = (float(np.sum(qt[ex1 - 1] * d1F[ex1])) / m1
               if len(ex1) else 0.0)
        xm0 = (float(np.sum(qt[ex0 - 1] * d0F[ex0])) / m0_
               if len(ex0) else 0.0)
        hv = "  <-- round-50 heavy" if r["kz"] in HEAVY_SHARED \
            else ""
        print("    %-4d %-4d %5d  %5d  %5d    %.4f   %.4f "
              "[%.3f, %.3f]   %.2e      %.2e%s"
              % (r["kz"], r["h"], len(s1), len(s0), len(com),
                 jac, float(np.median(rat)), float(np.min(rat)),
                 float(np.max(rat)), xm1, xm0, hv), flush=True)
    min_ovl = float(np.min(ovls))
    e4 = "SAMEMEASURE-FAMILY(min-Jaccard=%.4f)" % min_ovl
    check("E4.1 typed: %s -- same folded cosine quadrature "
          "family and weight rule (W-SPOT exact), different "
          "endpoint density (d1 vs d0) and integrand (Q^2 vs "
          "p_{0,m}^2); beta lives on the complementary NEG "
          "support" % e4, True)

    # ------------------------------------------------------------ C
    section("C -- controls: the rewrite must break off the truth "
            "comb")
    sneg = [r for r in smooth if r["tau_full"] < 0.0]
    sfull = [r for r in smooth if r.get("full") and "CJ" in r]
    n_break = 0
    for r in sfull:
        A = np.eye(NW) - r["CJ"]
        tau12s = float(np.linalg.eigvalsh(A)[0])
        sg, ld = np.linalg.slogdet(A)
        d12s = None
        if sg != 0.0:
            sg11, ld11 = np.linalg.slogdet(A[:11, :11])
            if sg11 != 0.0:
                d12s = math.exp(ld - ld11) * sg * sg11
        fired = (tau12s <= 0.0 or (d12s is not None
                                   and d12s <= 0.0))
        if fired:
            n_break += 1
    print("  C-S smooth: sigma indefinite (tau_full < 0) on "
          "%d/%d rungs (first h = %s); rewrite ratio bound "
          "breaks (tau_12 <= 0 or d_12 <= 0 <=> r >= 1) on "
          "%d/%d full-window rungs"
          % (len(sneg), len(smooth),
             sneg[0]["h"] if sneg else "n/a", n_break,
             len(sfull)))
    check("C-S smooth world breaks both premises (>= 1 each)",
          len(sneg) >= 1 and n_break >= 1, kill="KW")
    print("  C-E Epstein + scramble at kz %d:" % CTRL_KZ)
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ok_c = True
    for nmc, kw in (("Epstein",
                     dict(comb=(np.log(nn.astype(float)),
                                2.0 * lamE_[nn]
                                / np.sqrt(nn.astype(float))))),
                    ("scramble", dict(scramble_seed=1))):
        try:
            rc = anatomy(CTRL_KZ, **kw)
        except (np.linalg.LinAlgError, AssertionError):
            rc = None
        if not isinstance(rc, dict):
            print("       %-8s: chain dies (%r) -> FIRES" %
                  (nmc, rc))
            continue
        tau12c = None
        if rc.get("full") and "CJ" in rc:
            tau12c = float(np.linalg.eigvalsh(
                np.eye(NW) - rc["CJ"])[0])
        fired = (rc["negA"] > 0
                 or (tau12c is not None and tau12c <= 0.0))
        ok_c &= fired
        print("       %-8s: neg(A) %d | tau_12 %s -> %s"
              % (nmc, rc["negA"],
                 ("%+.3e" % tau12c) if tau12c is not None
                 else "n/a", "FIRES" if fired else "SILENT"))
    check("C-E controls fire", ok_c, kill="KW")

    return finish(dict(e2=e2, e3=e3, e4=e4))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"KP": "PIPELINE-BROKEN",
                   "KW": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("EDGECHRISTOFFEL-MEASURED / REWRITE-EXACT / "
                   "%(e2)s / %(e3)s / %(e4)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the rewrite is exact warded algebra
  -- the pivot identity IS a positive-weight norm square over
  the constructional folded family minus an explicit nonnegative
  NEG-support remainder beta, with the exact self-term m_def^2.
  W >= 0 costs nothing here (unlike the pair contract, no
  boundary fold was needed); the price sits ENTIRELY in the
  ratio r_h = beta/(1 + SPOS), whose distance from 1 is warded
  EXACTLY to (1/d_12)/(1 + SPOS) and tracks tau_full: the
  uniform q < 1 target is the wall's PD premise in these
  coordinates, quantified -- NOT an independent positivity
  source.  The diagonal route stays conditional per v889/v899.
  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source wall_gram_radau_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
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
    ('case_edge_christoffel_probe', _SRC_0, 22, (), 'EDGECHRISTOFFEL-MEASURED', 0),
    ('wall_gram_radau_probe', _SRC_1, 23, (), 'GRAMRADAU-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v902 -- PRIME.CASE.EDGE.CHRISTOFFEL.01 + PRIME.PORT.GRAM.COMPLETION.01 + PRIME.PORT.RADAU.WEIGHT.01: the wall relocation map -- 1/d_12 = 1 + Sum W Q^2 - beta exact (W > 0, beta >= 0) with the relocation diagnosis 1 - r ~ tau (slope +1.008); the wall IS the moment matrix of the signed comb measure, and the W >= 0 Gram completion fails at the x = +1 edge on every rung')
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
    print("v902: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print("a relocation/mechanism map, NOT progress: every identity is a coordinate change of the wall's own PD premise; the obstruction seat (NEG support, x = +1 edge) is registered, not removed")
    print("[%s] v902 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
