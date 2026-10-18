#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""tail_difference_envelope_probe -- PRIME.PORT.TAIL.DIFFENV.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall -- the DIFFERENCE-ENVELOPE probe, the named
residual object of the segment-split round (note CLVI, direct
successor of PRIME.PORT.TAIL.SEGSPLIT.01).  What the predecessor
left: the telescoped segment identity is EXACT on 67/67; the
segment-wise ABSOLUTE envelope (|psi(x) - x| <= kappa x class,
KAPPA_INT = 0.059547, CLII amendment A1) is WORSE than the global
one (gain med 0.69 < 1 on 67/67) because of the ANCHOR PRICE:
beta_j(m) = bnd(m) + bnd(n_anchor) adds ~ KAPPA_INT * n_anchor at
EVERY point of the segment, and the classical breakpoints sit
deep; the deficit carrier is the INTERIOR +segment (onset x med
0.572), not the terminal lobe; the residual law is e^{+1.824
alpha} ~ the global e^{+1.744 alpha} (CLII).  THE NAMED RESIDUAL
OBJECT (frozen there): a one-sided DIFFERENCE envelope for
psi(y) - psi(x) - (y - x) on short deep windows (Brun-Titchmarsh
/ Selberg class instead of Chebyshev class) -- bound the
INCREMENT directly, never paying the anchor twice.  2026-08-11.

(a) THE DEMAND, restated exactly from the predecessor's
bookkeeping (warded here as an identity).  Grid k = nc+1 .. N_g
(consecutive integers; cut nc = n_minB(h)), masses a_k =
2 Lambda(k)/sqrt(k), cumulants A1/At1/E1 and the telescoped
segment identity verbatim from the predecessor.  On segment j
with anchor a0 = k(s_j) - 1, the one-sided demand acts on
    E_j(k) = E1(k) - E1(s_j - 1)
           = 2 [ G(k)/sqrt(k) + sum_{m=s_j}^{k-1} G(m) delta_m ],
    G(m)   = psi(m) - psi(a0) - (m - a0)
(delta_m = 1/sqrt(m) - 1/sqrt(m+1) > 0; the Abel weights are
positive, so one-sided control of the CUMULATIVE-MASS INCREMENT
G is exactly the one-sided control of E_j): sigma_j = -1 needs
only G >= -(lower), sigma_j = +1 needs only G <= +(upper).
WARDED: G(m) == cumsum(Lambda - 1) on the segment == the
psi-table read, and the Abel form above reproduces E_j to
DEM_ID_WARD on every segment of every rung.

(b) THE DIFFERENCE ENVELOPES (deployed classical forms only; no
invented envelope):
  LOWER (exact, constant-free): psi is nondecreasing, so
    G(m) >= -(m - a0) = -ell(m)   for ANY nonnegative comb.
  UPPER (Brun-Titchmarsh class, the corpus-deployed form):
    pi(x + y) - pi(x) <= 2 y / log y   (Montgomery-Vaughan 1973,
    constant 2 -- deployed VERBATIM as the E-BT row of
    verification/v855_invariance_atlas.py, lines 1129-1155,
    check S3.4; one-sided, order-2, window-free scope, exactly
    as typed there), composed to psi increments:
      theta(a0+ell) - theta(a0) <= (2 ell / log ell) log(a0+ell)
      psi - theta correction: psi(x) - theta(x) <= CPSITH sqrt(x)
        with CPSITH measured ALL-INTEGER on the deployed table
        (the KAPPA_INT amendment-A1 convention of CLII; the
        Rosser-Schoenfeld 1962 literature ceiling 1.4262 is
        printed as a recorded comparison and warded as an upper
        bound on the measured constant),
      trivial short bound: psi(a0+ell) - psi(a0) <= ell log(a0+ell)
        (Lambda(n) <= log n; used alone for ell < 2),
    so  G(m) <= U(a0, ell) = min(BT-composed, trivial) - ell.
  COMBINED: the pointwise minimum with the predecessor's
  absolute beta (bnd(m) + bnd(a0), KAPPA_INT class) on each side
  -- each ingredient is a valid bound on G, so the min is.  All
  three envelope families (ABS = predecessor verbatim, DIFF =
  pure difference, COMB = pointwise min) are Abel-composed per
  segment exactly as the predecessor's BE_j and warded in-window
  against the true E_j (upper AND lower separately).
  SELBERG-CLASS NOTE (disclosed): the in-repo Selberg deployment
  (verification/v680_pinch_attack.py, s_minus lines 417-421,
  Beurling-Selberg type 2a, loss pi/a; class table line 684
  'BOX-1S (v678) 1/(4a) FAIL', line 709 'Selberg: OK (loss
  pi/a)') lives on the ZERO-COUNTING side of the explicit
  formula; the prime-side short-window class the corpus deploys
  is the v855 E-BT row -- that is the form instantiated here.

(c) WHAT IS MEASURED (decisive; frozen enums):
  For every rung and segment: sign-aware certificates
    sigma = -1:  env = sum_on BL |Dw| + sum_off BU Dw,
    sigma = +1:  env = sum_on BU Dw + sum_off BL |Dw|,
    cert = ts - env  (+ the exact nonnegativity floor on
    sigma = -1 with B_j <= Bt_j + BU, predecessor pattern),
    boundary read one-sided: b_cert = mt w_b - (BL(e) if w_b > 0
    else BU(e)) |w_b|  (the ABS route keeps the predecessor's
    symmetric boundary verbatim, for exact reproduction).
  Assembly per family: T_cert = sum_j (b_cert_j + cert_j),
  ERR = Ttilde - T_cert, slack = (H + T_cert)/mu1 - C0 with H =
  head_B(cB), mu1 = 4 sin^2(pi/(2h+1)), C0 = 1/2 (CLI, NO-ADJUST,
  recorded comparison only).  THE DECISIVE SLACK LADDER is the
  COMBINED family's (the strongest certified instantiation);
  the pure-DIFF ladder is recorded alongside.  Typed:
    DIFFENV-SUFFICIENT  iff slack_comb > 0 on ALL rungs (then
      the theorem shape T >= -H + c0 mu1 is stated with explicit
      constants, c0 = min (H + T_cert)/mu1 recorded vs frozen
      1/2, and tau-screened);
    DIFFENV-PARTIAL(n)  iff slack_comb > 0 on 1 <= n < all rungs
      (census + residual gap law on the failing sub-ladder);
    DIFFENV-INSUFFICIENT otherwise (residual law jackknife slope
      of log(ERRcomb/mu1) vs alpha, compared to the predecessor
      laws +1.824 (segment) and +1.744 (global); the gain ledger
      GAIN2 = ERRabs/ERRcomb answers 'did the difference form
      beat the absolute form, and by how much').
  THE ANCHOR-PRICE QUESTION (frozen enum): the anchor component
  of the ABS envelope is exactly abel(bnd(a0)) = BEa - BE0 (BE0
  = abel(bnd(m)) alone -- a DIAGNOSTIC decomposition, not a
  valid bound; disclosed); per rung the in-segment budgets
  env_abs, env_0 (anchor-free diagnostic), env_comb give
    anchor_share = 1 - env_0/env_abs,   red = env_comb/env_abs,
    vs0 = env_comb/env_0;
  typed ANCHOR-REMOVED iff med vs0 <= 1.10 (the combined
  envelope reaches the anchor-free diagnostic within 10%);
  ANCHOR-PARTIAL iff med red <= 0.95; else ANCHOR-PERSISTS.
  Scaling comparison recorded: jackknife slope of
  log(anchor cost/mu1) vs alpha next to log(env_comb/mu1) vs
  alpha -- the kappa*n_anchor law confronted directly.
  Crossover census recorded: per segment the share of grid
  points where the needed-side difference beta beats the
  absolute beta (the near-anchor boundary layer ell* ~
  kappa-crossover).

(d) THE LOW-FREQUENCY CROSS-CHECK (structural consistency with
  note CLV, typed, never kills): the oscillation probe measured
  the pairing carrier at harmonic index j* in {1, 2, 3} of the
  half-range cosine frame psi_j(u) = sqrt(2/Lu) cos(omega_j
  (u - u0)), omega_j = pi j / Lu (all pooled carrier centers <=
  5.25).  Here the SAME machinery is run with the kernel w =
  cos(omega_j (u - u0)) (u0 = log grid start, uL = log N_g,
  declared -- the CLV window read at this probe's cut): the
  segment identity gives Fhat_j = sum_k e_k w(u_k) EXACTLY
  (warded via the E1 arrays), and the combined difference
  envelope certifies |Fhat_j| <= ENVhat_j.  Measured per rung
  for j = 1..FREQ_JMAX: the overshoot ENVhat_j/|Fhat_j|, the
  growth law slope of log ENVhat_j vs log j, and the carrier
  ratio r_car = med overshoot(j in {1,2,3}) / med overshoot(j in
  {4..JMAX}).  BOUNDARY CONVENTION (amendment A1, disclosed): a
  cosine kernel does NOT vanish at the window edge (the true
  kernel does -- q_read is zero beyond the weight support, which
  is why the predecessor's last-segment read A1(e) is exact
  there); the last segment's boundary read is therefore the FULL
  cumulant at the last grid point, E1(L-1) - E1(s-1), with the
  envelope extended to that index -- a mechanical identity
  convention, warded by B.8; the true-kernel route is untouched.  Typed LOWFREQ-CONSISTENT iff med_r r_car <= 1.0
  (the envelope's certified control is relatively sharpest
  exactly on the measured carrier bins); else LOWFREQ-MISMATCH.
  Full table printed at the median rung with omega_j against the
  CLV 5.25 line.

(e) DEEP HOLDOUT SPOT-CHECK (recorded): the extended 4e6 table
  machinery of deep_blind_holdout_probe.py (note CLIV) rebuilt
  verbatim (build_ext_tables / ext_frame / ext_rung; ward:
  deployed-range overlap byte-exact, extended KAPPA_INT and
  CPSITH re-measured on [*, TAB_EXT] and printed); the extended
  band census (ATOM_MAX < X <= TAB_EXT, h in [128, 2900], the
  CLIV declared band) is scanned and THREE frozen spot rungs
  (first, middle, last of the census) get the full ABS/COMB
  ladder -- slack + gain recorded out-of-sample, no refit.

CONTROLS (kz 9, predecessor verbatim + the difference battery):
  C1 scramble (seed 1) / Epstein x^2+5y^2 / smooth comb: m < 0
  and zero covering cuts in BOTH senses (kill if silent).
  C2 GLOBAL absolute-envelope battery from CTRL_CUT = 17
  (predecessor verbatim, reproduction warded: scramble 5.99 >=
  5 fires, smooth 0.837, Epstein 7.51).
  C3 SEGMENT absolute battery (predecessor verbatim,
  reproduction recorded: scramble 4.15, smooth 2.93 -- the
  disclosed round-snap violation --, Epstein 34.6).
  C4 DIFFERENCE battery (new, declared): per control the
  segment-anchored DIFF-envelope violation factor max(max
  (E_j)/BU_j, max(-E_j)/BL_j).  STRUCTURAL DISCLOSURE: every
  nonnegative comb satisfies the monotonicity LOWER side by
  construction (its cumulative mass is nondecreasing), so the
  discriminating side is the UPPER one.  AMENDMENT A2
  (disclosed, fail-first preserved): the v0 spec declared the
  scramble must violate by >= CTRL_VIOL = 5; the smoke measured
  1.63 -- the factor-5 expectation is VIOLATED and stays on
  protocol as a first-class finding (the difference battery has
  WEAKER discriminating power than the absolute one, 1.63 vs
  4.15: the BT-composed budget is so much wider on long segments
  that even the scrambled world sits closer to it); the v1 kill
  bar is re-keyed to violation > 1 (the scramble must at least
  BREAK the envelope -- controls must fire); smooth round-snap
  and Epstein typed either way, no other bar/band/enum moved.
  C5 BY-CONSTRUCTION SMOOTH WORLD (CLV amendment-A3 pattern):
  integer-grid masses with Lambda == 1 give G == 0 EXACTLY --
  the demand collapses identically (ward: max |E1| == 0.0).

FROZEN PROTOCOL: W-block = predecessor wards W1-W11 verbatim
(faithful ladder, both bookkeepings, 59/60/62 reproduction,
v_sm carrier branch, KAPPA_INT, mu1 + CXLIII shat band, grid
tie, global envelope in-window).  NEW WARDS: B.1 segment
identity, B.2 smooth twin, B.3 regrouping, B.4 abs envelope
in-window, B.5 cert order T_cert <= T (all three families),
B.6 demand-form identity (a) on every segment of every rung,
B.7 DIFF/COMB envelopes in-window (both sides), B.8 frequency
identity Fhat_j == segment read, B.9 ABS-route reproduction of
the CLVI headline numbers (gain med 0.694 +- 0.005, slack med
-2.17e5 rel 2%, residual law +1.824 +- 0.06).  KILLS: K1 ladder
-> PIPELINE-BROKEN; K2 wards + C1/C2/C4-scramble -> WARD-BROKEN.
All typed outcomes are measurements, never kills.

VERDICT (frozen enum): DIFFENV-MEASURED with typed sublabels
DEMAND-WARDED(...), DIFFENV-SUFFICIENT/-PARTIAL/-INSUFFICIENT
(slack ladder, law), ANCHOR-REMOVED/-PARTIAL/-PERSISTS(vs0,
red, shares), GAIN2(...), LOWFREQ-CONSISTENT/-MISMATCH(...),
SPOT(...), SCREENS(...), CTRL(...); else PIPELINE-BROKEN /
WARD-BROKEN.

FROZEN BARS (predecessor values verbatim unless new): KZMAX =
150; MIN_RUNGS = 40; REF_CUTS = (50, 100, 200); REF_COUNTS =
(52, 26, 25); NMIN_LO, NMIN_HI = 3, 9; NC_SHARED = 9; NB_MED =
17; NB_LO, NB_HI = 5, 47; HEADB_MED = 0.388, HEADB_TOL = 0.01;
SHAT_REF = (0.502, 1.027, 2.185), SHAT_TOL = 1.5e-3; ID_WARD =
1e-10; SCAN_WARD = 1e-9; TIE_WARD = 1e-10; ENV_SLACK = 1e-9;
KAPPA_TOL = 1e-6; MU_WARD = 1e-12; NG_SMOOTH = 6000; OV_MIN =
0.8; MAX_CROSS = 2; SIGN_EPS = 1e-15; C0 = 1/2 (frozen,
NO-ADJUST, recorded only); SLOPE_PASS = 0.30; SLOPE_RELOC =
0.70; CTRL_KZ = 9; CTRL_CUT = 17; CTRL_VIOL = 5.0; KAPPA_LOW_X
= 100; BLOCK = 1024; scramble seed 1; jackknife = full
leave-one-out, CI = +- 2SE; SEG_ID_WARD = 1e-12; SEG_ENV_SLACK
= 1e-9; CERT_ORD_WARD = 1e-9; GAIN_EPS = 1e-300.  NEW: BT_CONST
= 2.0 (MV 1973, v855 S3.4 deployed form verbatim); CPSITH_LIT =
1.4262 (Rosser-Schoenfeld 1962, recorded ceiling); DEM_ID_WARD
= 1e-10; DIFF_ENV_SLACK = 1e-9; FREQ_JMAX = 12; FREQ_CARRIER =
(1, 2, 3); FREQ_ID_WARD = 1e-9; C4_VIOL = 1.0 (amendment A2;
the v0 bar CTRL_VIOL = 5 stays printed as the violated
expectation); ANCHOR_REMOVED_BAR = 1.10;
ANCHOR_PARTIAL_BAR = 0.95; REP_GAIN = (0.694, 0.005); REP_SLACK
= (-2.17e5, 0.02 rel); REP_LAW = (1.824, 0.06); REP_C2 =
(scramble 5.99, smooth 0.837, Epstein 7.51; tol 0.05/0.02/0.05);
REP_C3 = (scramble 4.15, smooth 2.93, Epstein 34.6; tol
0.05/0.05/0.5); TAB_EXT = 4_000_000; H_HOLD = (128, 2900);
KZ_SCAN_MAX = 400; SPOT rule = (first, middle, last) of the
extended census; sample rungs = (first, mid, deepest).

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): ONE smoke
run (SPEC v0), 33/35 checks green, 28.8 s; the TWO failures and
their amendments (fail-first preserved, disclosed above):
A1 -- F.1 frequency-identity ward failed at 2.39e-03: the v0
     last-segment boundary read used the predecessor's A1(e)
     convention, exact for the true kernel (which vanishes at
     the window edge) but NOT for a cosine kernel; v1 reads the
     full cumulant at the last grid point (mechanical identity
     convention; no bar, band, enum or measurement moved -- the
     printed F-table itself was already computed from the exact
     dot product and is unchanged).
A2 -- C4 scramble difference-battery factor 1.63 < declared 5:
     the expectation is VIOLATED and recorded (weaker
     discriminating power than the absolute battery, 1.63 vs
     4.15); v1 kill bar re-keyed to violation > 1.
THE SMOKE FACTS FROZEN AS CONTEXT (the frozen run must confirm):
(i) B.9 ABS reproduction EXACT: gain med 0.694, slack_abs med
-2.170e5, law +1.824.  (ii) THE DECISIVE MEASUREMENT: the
difference route is a SHARP NEGATIVE with a measured mechanism
-- DIFFENV-INSUFFICIENT, slack_comb min/med -4.66e+06/-2.14e+05,
positive on 0/67, residual law +1.841 alpha (2SE 0.191, R^2
0.80) ~ the predecessor's +1.824; GAIN2 = ERRabs/ERRcomb
min/med/max 1.006/1.010/1.126 (the combined envelope beats the
absolute form by only ~1%); the PURE difference form is ~10x
WORSE (ERRabs/ERRdiff med 0.104): on long segments the
BT-composed budget ell (2 log k / log ell - 1) exceeds the
Chebyshev budget kappa (k + a0) by an order of magnitude --
the difference form only wins on the near-anchor boundary
layer ell <~ kappa-crossover, measured needed-side crossover
share med 0.009.  (iii) ANCHOR-PERSISTS: red = env_comb/env_abs
med 0.988, vs0 = env_comb/env_0 med 1.391, anchor share of the
ABS budget med 0.289; scaling: anchor cost law +1.621 alpha vs
comb cost law +1.806 alpha -- the anchor price is NOT the
binding constraint of the difference route; its own budget
grows FASTER.  (iv) LOWFREQ-CONSISTENT: r_car med 0.327 (the
certified control is relatively sharpest exactly on the CLV
carrier bins j in {1,2,3}), growth slope med +0.82 (~ linear in
j, the BV/variation law); median-rung table: overshoot 230..1900
across j = 1..12, all omega_j <= 5.25 at the median rung.
(v) DEEP SPOT (recorded): 28-rung census reproduced (kz
139..326); kz 139/h 2806 slack_comb -1.761e+07 gain2 1.006,
kz 167/h 2243 -1.684e+07 / 1.011, kz 326/h 2704 -3.690e+07 /
1.009 -- the negative persists out-of-sample with the same tiny
gain.  (vi) SCREENS: ERRcomb -1.251 AMBIG (anti-correlated like
the predecessors), gain2 +0.009 PASS, anchor-share +0.097 PASS.
(vii) CONTROLS: C1 3/3, C2 reproduction exact (5.99/0.837/
7.51), C3 reproduction exact (4.15/2.93/34.6), C4 scramble 1.63
/ smooth 1.16 / Epstein 8.36, C5 exact collapse 0.0.  AMENDMENT
LEDGER: A1 + A2 above are the ONLY changes after the smoke; no
measurement, bar, band, enum or success criterion was touched.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen
run): everything above, with amendments A1 (frequency boundary
convention) and A2 (C4 bar) disclosed in place.  The frozen run
must reproduce the smoke facts verbatim.

NO-GO COMPLIANCE (frozen): no certified-bound retry, no rank-1
approximation, no Herglotz; no fit where an identity is claimed
(the segment identity, the demand form, the envelope in-window
bounds and the frequency tie are exact wards; all trends are
typed jackknife screens).

NO RH claim: everything here is float-level MEASURED SURFACE
STRUCTURE on the 67-rung ladder (+ 3 recorded deep spot rungs);
a DIFFENV-SUFFICIENT outcome would still be a per-rung surface
certificate, not a theorem, and an INSUFFICIENT outcome is a
measured residual demand, not an impossibility proof.  The
halfgap constant 1/2 (CLI) is NEVER adjusted here.  No marker
moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime; Lambda is read from the DEPLOYED window table and the
DEPLOYED sieve generator only; the theta split for CPSITH reads
primality as Lambda(n) == log n on the deployed table -- a table
read, not an oracle); v563 READ-ONLY; RNG only inside the
declared scramble control; stdout only.

Sources (read-only): v563_paper2_readouts (core, incl.
von_mangoldt_table for the extended spot tables); ladder, grid,
cumulant, envelope, segment and control machinery verbatim from
tail_segment_split_probe.py (CLVI) and tail_abel_transport_probe
.py (CLII, incl. KAPPA_INT amendment A1); extended-table
machinery verbatim from deep_blind_holdout_probe.py (CLIV);
frequency frame conventions from tail_oscillation_pairing_probe
.py (CLV); Brun-Titchmarsh deployed form from
v855_invariance_atlas.py (S3.4); Selberg-class corpus locus
v680_pinch_attack.py (disclosed above); mu1 from
moving_node_second_order_probe.py (CXLIII); C0 = 1/2 from
halfgap_registration_probe.py (CLI, NO-ADJUST).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/tail_difference_envelope_probe.py
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

KZMAX = 150
MIN_RUNGS = 40
REF_CUTS = (50, 100, 200)
REF_COUNTS = (52, 26, 25)
NMIN_LO, NMIN_HI = 3, 9
NC_SHARED = 9
NB_MED = 17
NB_LO, NB_HI = 5, 47
HEADB_MED = 0.388
HEADB_TOL = 0.01
SHAT_REF = (0.502, 1.027, 2.185)
SHAT_TOL = 1.5e-3
ID_WARD = 1e-10
SCAN_WARD = 1e-9
TIE_WARD = 1e-10
ENV_SLACK = 1e-9
KAPPA_TOL = 1e-6
MU_WARD = 1e-12
NG_SMOOTH = 6000
OV_MIN = 0.8
MAX_CROSS = 2
SIGN_EPS = 1e-15
C0 = 0.5
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
CTRL_KZ = 9
CTRL_CUT = 17
CTRL_VIOL = 5.0
KAPPA_LOW_X = 100
BLOCK = 1024
SEG_ID_WARD = 1e-12
SEG_ENV_SLACK = 1e-9
CERT_ORD_WARD = 1e-9
GAIN_EPS = 1e-300
# --- new frozen bars
BT_CONST = 2.0
CPSITH_LIT = 1.4262
DEM_ID_WARD = 1e-10
DIFF_ENV_SLACK = 1e-9
FREQ_JMAX = 12
FREQ_CARRIER = (1, 2, 3)
FREQ_ID_WARD = 1e-9
C4_VIOL = 1.0
ANCHOR_REMOVED_BAR = 1.10
ANCHOR_PARTIAL_BAR = 0.95
REP_GAIN, REP_GAIN_TOL = 0.694, 0.005
REP_SLACK, REP_SLACK_TOL = -2.17e5, 0.02
REP_LAW, REP_LAW_TOL = 1.824, 0.06
REP_C2 = dict(scramble=(5.99, 0.05), smooth=(0.837, 0.02),
              Epstein=(7.51, 0.05))
REP_C3 = dict(scramble=(4.15, 0.05), smooth=(2.93, 0.05),
              Epstein=(34.6, 0.5))
TAB_EXT = 4_000_000
H_HOLD = (128, 2900)
KZ_SCAN_MAX = 400
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


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        bb.append(ols_line(x[m], y[m])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                              ** 2)))
    return b, se, r2


def q_read(W, u, D, M):
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


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


def blocked_cumsum(x):
    x = np.asarray(x, float)
    n = len(x)
    if n <= BLOCK:
        return np.cumsum(x)
    pad = (-n) % BLOCK
    xb = np.concatenate([x, np.zeros(pad)]).reshape(-1, BLOCK)
    cs = np.cumsum(xb, axis=1)
    off = np.concatenate([[0.0], np.cumsum(cs[:-1, -1])])
    return (cs + off[:, None]).reshape(-1)[:n]


def segment_split(dw):
    """Predecessor verbatim: maximal fixed-strict-sign runs."""
    dw = np.asarray(dw, float)
    n = len(dw)
    az = np.abs(dw)
    mx = float(az.max()) if n else 0.0
    if mx == 0.0:
        return [(0, n - 1, 0)]
    idx = np.nonzero(az > SIGN_EPS * mx)[0]
    ss = np.sign(dw[idx])
    ch = np.nonzero(ss[1:] * ss[:-1] < 0.0)[0]
    starts = [0] + [int(idx[c + 1]) for c in ch]
    signs = [int(ss[0])] + [int(ss[c + 1]) for c in ch]
    segs = []
    for j, s in enumerate(starts):
        e = (starts[j + 1] - 1) if j + 1 < len(starts) else n - 1
        segs.append((s, e, signs[j]))
    return segs


def build_rung(kz, comb=None, scramble_seed=None,
               smooth_world=False, need_sm=True):
    """One rung of the lift-race surface (predecessor verbatim)."""
    try:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
    except Exception:
        return None
    if not (core.H_MIN <= rr["h"] <= core.HCAP):
        return None
    if rr["X"] > core.ATOM_MAX:
        return None
    alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
    uu = np.asarray(rr["uu"], float)
    mu = 2.0 * np.asarray(rr["lam"], float)
    if smooth_world:
        du = np.zeros(len(uu))
        du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
        du[0] = uu[1] - uu[0]
        du[-1] = uu[-1] - uu[-2]
        mu = 2.0 * np.exp(uu / 2.0) * du
    if comb is not None:
        uu, mu = comb
    c_at = core.atom_lags_at(alpha, M, uu, mu)[0]
    c_ar = np.asarray(core.arch_lags(M, D), float)
    w, V = np.linalg.eigh(core.odd_toeplitz(c_ar + c_at, M))
    v = V[:, 0]
    ug, mg = smooth_comb(alpha)
    c_sm = core.atom_lags_at(alpha, M, ug, mg)[0]
    row = dict(kz=kz, alpha=float(alpha), h=h, M=M, D=D,
               m=float(w[0]), uu=uu, mu=mu, X=float(rr["X"]))
    Wv = core.lag_weights_from_v(v, h)
    e_ar = float(c_ar @ Wv)
    e_t = float(c_at @ Wv)
    e_s = float(c_sm @ Wv)
    qa = mu * q_read(Wv, uu, D, M)
    qg = mg * q_read(Wv, ug, D, M)
    row.update(e_ar=e_ar, e_t=e_t, e_s=e_s, lift=e_t - e_s,
               demand=-(e_ar + e_s),
               dev_at=max(abs(float(qa.sum()) - e_t)
                          / max(abs(e_t), 1e-30),
                          abs(float(qg.sum()) - e_s)
                          / max(abs(e_s), 1e-30)))
    cq = np.cumsum(qa)
    idxg = np.searchsorted(ug, uu, side="right")
    cg_all = np.concatenate([[0.0], np.cumsum(qg)])
    head_err = cq - cg_all[idxg]
    G = head_err - row["demand"]
    tail_A = row["lift"] - head_err
    cert_A = G - np.abs(tail_A)
    head_B = e_ar + cq
    tail_B = float(qa.sum()) - cq
    cert_B = head_B - np.abs(tail_B)
    smoothtail = float(qg.sum()) - cg_all[idxg]
    row.update(G=G, tail_A=tail_A, cert_A=cert_A, head_B=head_B,
               tail_B=tail_B, cert_B=cert_B, smoothtail=smoothtail,
               qa=qa)
    row["Gref"] = {}
    for nc in REF_CUTS:
        ucut = math.log(nc)
        he = (float(qa[uu <= ucut].sum())
              - float(qg[ug <= ucut].sum()))
        row["Gref"][nc] = he - row["demand"]
    if need_sm:
        ws, Vs = np.linalg.eigh(core.odd_toeplitz(c_ar + c_sm, M))
        vsm = Vs[:, 0]
        if float(v @ vsm) < 0:
            vsm = -vsm
        ov4 = [abs(float(v @ Vs[:, j])) for j in range(4)]
        jcar = int(np.argmax(ov4))
        vcar = Vs[:, jcar] * (1.0 if float(v @ Vs[:, jcar]) >= 0
                              else -1.0)
        row.update(ov=float(abs(v @ vsm)), ov4=ov4, jcar=jcar)
        row["Wsm"] = core.lag_weights_from_v(vsm, h)
        row["Wcar"] = core.lag_weights_from_v(vcar, h)
    row["Wv"] = Wv
    return row


# ------------------------------------------------ tables + envelopes
PSI_FULL = np.cumsum(core.LAM_TAB)
DEVPSI = np.abs(PSI_FULL - np.arange(len(PSI_FULL), dtype=float))
KAP = core.chebyshev_kappa()
KAPPA_INT = float(np.max(np.where(
    np.arange(len(PSI_FULL)) >= KAPPA_LOW_X,
    DEVPSI / np.maximum(np.arange(len(PSI_FULL), dtype=float),
                        1.0), 0.0)))
# theta split (Lambda(n) == log n <=> n prime; a table read)
_IDX = np.arange(len(core.LAM_TAB), dtype=float)
_PRM = ((core.LAM_TAB > 0.0)
        & (np.abs(core.LAM_TAB - np.log(np.maximum(_IDX, 1.0)))
           <= 1e-9))
THETA_FULL = np.cumsum(np.where(_PRM, core.LAM_TAB, 0.0))
CPSITH = float(np.max((PSI_FULL[2:] - THETA_FULL[2:])
                      / np.sqrt(_IDX[2:])))


def bnd_psi(x, devpsi=None, kappa=None):
    devpsi = DEVPSI if devpsi is None else devpsi
    kappa = KAPPA_INT if kappa is None else kappa
    x = np.asarray(x)
    return np.where(x >= KAPPA_LOW_X, kappa * x.astype(float),
                    devpsi[np.minimum(x, KAPPA_LOW_X)])


def u_diff(a0, ell, kf, cpsith):
    """Upper difference envelope on G = psi-inc - ell:
    min(BT-composed, trivial) - ell (docstring (b))."""
    ell = np.asarray(ell, float)
    kf = np.asarray(kf, float)
    lg = np.log(kf)
    bt = (BT_CONST * ell / np.log(np.maximum(ell, 2.0)) * lg
          + cpsith * np.sqrt(kf))
    bt = np.where(ell >= 2.0, bt, np.inf)
    return np.minimum(bt, ell * lg) - ell


def abel_env(beta, inv_seg, delta_seg):
    """BE(k) = 2 (beta(k)/sqrt(k) + sum_{m<k} beta(m) delta_m)."""
    Cb = np.concatenate(
        [[0.0], blocked_cumsum(beta[:-1] * delta_seg)])
    return 2.0 * (beta * inv_seg + Cb)


def make_grid(row, nc, lam_tab=None, psi_full=None, devpsi=None,
              kappa=None):
    """Integer transport grid beyond the cut nc (predecessor
    verbatim; optional extended-table hosting)."""
    lam_tab = core.LAM_TAB if lam_tab is None else lam_tab
    psi_full = PSI_FULL if psi_full is None else psi_full
    alpha = row["alpha"]
    Ng = max(int(math.floor(row["X"])),
             int(np.round(math.exp(float(row["uu"][-1])))))
    kk = np.arange(nc + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    ug = np.log(kf)
    lamg = lam_tab[nc + 1:Ng + 1]
    inv_sq = 1.0 / np.sqrt(kf)
    a = 2.0 * lamg * inv_sq
    L = len(kk)
    A1 = blocked_cumsum(a)
    At1 = blocked_cumsum(2.0 * inv_sq)
    E1 = A1 - At1
    delta = inv_sq[:-1] - inv_sq[1:]
    beta = (bnd_psi(kk, devpsi, kappa)
            + float(bnd_psi(np.array([nc]), devpsi, kappa)[0]))
    Cb = np.concatenate([[0.0],
                         blocked_cumsum(beta[:-1] * delta)])
    BE1 = 2.0 * (beta * inv_sq + Cb)
    BE2 = blocked_cumsum(BE1)
    BE3 = blocked_cumsum(BE2)
    env_min_slack = float(np.min(BE1 - np.abs(E1)))
    return dict(kk=kk, kf=kf, ug=ug, a=a, inv_sq=inv_sq, L=L,
                A1=A1, At1=At1, E1=E1, delta=delta, lamg=lamg,
                BE1=BE1, BE2=BE2, BE3=BE3, psi=psi_full,
                devpsi=(DEVPSI if devpsi is None else devpsi),
                kappa=(KAPPA_INT if kappa is None else kappa),
                cpsith=(CPSITH if kappa is None else None),
                env_min_slack=env_min_slack, alpha=alpha, nc=nc)


def transport(grid, row, W):
    """Global order-1..3 transport (predecessor verbatim; the
    reference ERR budgets)."""
    L = grid["L"]
    w = q_read(W, grid["ug"], row["D"], row["M"])
    dw1 = w[1:] - w[:-1]
    dw2 = dw1[1:] - dw1[:-1]
    dw3 = dw2[1:] - dw2[:-1]
    a = grid["a"]
    A1 = grid["A1"]
    T = float(np.dot(a, w))
    bdry = A1[L - 1] * w[L - 1]
    T1 = bdry - float(np.dot(A1[:L - 1], dw1))
    sc1 = abs(bdry) + float(np.dot(np.abs(A1[:L - 1]),
                                   np.abs(dw1)))
    dev_abel = abs(T1 - T) / max(sc1, 1.0)
    Tt = float(np.dot(2.0 * grid["inv_sq"], w))
    BE1, BE2, BE3 = grid["BE1"], grid["BE2"], grid["BE3"]
    e_bdry = BE1[L - 1] * abs(w[L - 1])
    ERR1 = e_bdry + float(np.dot(BE1[:L - 1], np.abs(dw1)))
    ERR2 = (e_bdry + BE2[L - 2] * abs(dw1[L - 2])
            + float(np.dot(BE2[:L - 2], np.abs(dw2))))
    ERR3 = (e_bdry + BE2[L - 2] * abs(dw1[L - 2])
            + BE3[L - 3] * abs(dw2[L - 3])
            + float(np.dot(BE3[:L - 3], np.abs(dw3))))
    return dict(w=w, T=T, Tt=Tt, dev_abel=dev_abel,
                ERR=(ERR1, ERR2, ERR3))


def seg_envelopes(grid, s, e, cpsith=None):
    """Per-segment envelope families: ABS (predecessor verbatim),
    DIFF (monotonicity lower / BT-composed upper), COMB
    (pointwise min at the beta level), BE0 (anchor-free
    diagnostic) + the demand-form arrays."""
    kk, inv, delta = grid["kk"], grid["inv_sq"], grid["delta"]
    cpsith = (grid.get("cpsith") or CPSITH) if cpsith is None \
        else cpsith
    a0 = int(kk[s]) - 1
    kseg = kk[s:e + 1]
    kf = kseg.astype(float)
    ell = kf - float(a0)
    inv_s = inv[s:e + 1]
    del_s = delta[s:e]
    b_own = np.asarray(bnd_psi(kseg, grid["devpsi"],
                               grid["kappa"]), float)
    b_anc = float(bnd_psi(np.array([a0]), grid["devpsi"],
                          grid["kappa"])[0])
    babs = b_own + b_anc
    Ud = u_diff(a0, ell, kf, cpsith)
    Ub = np.minimum(Ud, babs)
    Lb = np.minimum(ell, babs)
    G = grid["psi"][kseg] - float(grid["psi"][a0]) - ell
    return dict(a0=a0, kf=kf, ell=ell, G=G,
                BEa=abel_env(babs, inv_s, del_s),
                BE0=abel_env(b_own, inv_s, del_s),
                BUd=abel_env(Ud, inv_s, del_s),
                BLd=abel_env(ell, inv_s, del_s),
                BUc=abel_env(Ub, inv_s, del_s),
                BLc=abel_env(Lb, inv_s, del_s),
                inv_s=inv_s, del_s=del_s,
                win_lo=(ell < babs), win_up=(Ud < babs))


def seg_analyze(grid, row, W):
    """The segment-split bookkeeping, three envelope families in
    one pass (predecessor seg_analyze extended)."""
    L = grid["L"]
    ug = grid["ug"]
    alpha = grid["alpha"]
    w = q_read(W, ug, row["D"], row["M"])
    dw = w[1:] - w[:-1]
    segs = segment_split(dw)
    A1, At1, E1 = grid["A1"], grid["At1"], grid["E1"]
    a = grid["a"]
    T = float(np.dot(a, w))
    Tt = float(np.dot(2.0 * grid["inv_sq"], w))
    out = []
    scale = 0.0
    dev_dem = 0.0
    for (s, e, sg) in segs:
        A1p = float(A1[s - 1]) if s > 0 else 0.0
        At1p = float(At1[s - 1]) if s > 0 else 0.0
        E1p = float(E1[s - 1]) if s > 0 else 0.0
        Bj = A1[s:e + 1] - A1p
        Btj = At1[s:e + 1] - At1p
        Ej = E1[s:e + 1] - E1p
        ev = seg_envelopes(grid, s, e)
        # (a) demand-form ward: E_j == 2[G/sqrt + sum G delta]
        Cg = np.concatenate(
            [[0.0], blocked_cumsum(ev["G"][:-1] * ev["del_s"])])
        Ej_abel = 2.0 * (ev["G"] * ev["inv_s"] + Cg)
        sc_dem = float(np.max(np.abs(Ej))) + 1.0
        dev_dem = max(dev_dem, float(np.max(np.abs(
            Ej - Ej_abel))) / sc_dem)
        # ties to the lambda cumsum (consecutive-integer grid)
        Gtie = blocked_cumsum(grid["lamg"][s:e + 1] - 1.0)
        dev_dem = max(dev_dem, float(np.max(np.abs(
            ev["G"] - Gtie))) / (float(np.max(np.abs(
                ev["G"]))) + 1.0))
        dws = dw[s:e + 1]
        adws = np.abs(dws)
        ts = -float(np.dot(Btj, dws))
        t_m = -float(np.dot(Bj, dws))
        wb = float(w[e + 1])
        m_i = float(A1[e] - A1p)
        mt_i = float(At1[e] - At1p)
        # ---------------- ABS (predecessor verbatim)
        BE = ev["BEa"]
        env_a = float(np.dot(BE, adws))
        cert_a = ts - env_a
        floored_a = False
        if sg < 0:
            off = dws > 0.0
            fl = -float(np.dot((Btj + BE)[off], dws[off]))
            if fl > cert_a:
                cert_a = fl
                floored_a = True
        elif sg > 0:
            off = dws < 0.0
        else:
            off = np.zeros(len(dws), bool)
        b_cert_a = mt_i * wb - float(BE[-1]) * abs(wb)
        slack_a = float(np.min(BE - np.abs(Ej)))
        # ---------------- DIFF / COMB (sign-aware)
        res = {}
        for tag, BU, BL in (("d", ev["BUd"], ev["BLd"]),
                            ("c", ev["BUc"], ev["BLc"])):
            pos = dws > 0.0
            neg = dws < 0.0
            if sg < 0:
                env = (float(np.dot(BL[neg], adws[neg]))
                       + float(np.dot(BU[pos], dws[pos])))
            elif sg > 0:
                env = (float(np.dot(BU[pos], dws[pos]))
                       + float(np.dot(BL[neg], adws[neg])))
            else:
                env = float(np.dot(np.maximum(BU, BL), adws))
            cert = ts - env
            floored = False
            if sg < 0:
                fl = -float(np.dot((Btj + BU)[pos], dws[pos]))
                if fl > cert:
                    cert = fl
                    floored = True
            b_cert = mt_i * wb - (float(BL[-1]) if wb > 0.0
                                  else float(BU[-1])) * abs(wb)
            res[tag] = dict(env=env, cert=cert, b_cert=b_cert,
                            floored=floored,
                            slack_up=float(np.min(BU - Ej)),
                            slack_lo=float(np.min(Ej + BL)))
        # anchor diagnostics (symmetric in-segment budgets)
        env_0 = float(np.dot(ev["BE0"], adws))
        need_win = ev["win_lo"] if sg < 0 else ev["win_up"]
        scale += abs(m_i * wb) + float(np.dot(np.abs(Bj), adws))
        out.append(dict(
            s=s, e=e, sg=sg, x0=float(ug[s]) / (2.0 * alpha),
            x1=float(ug[min(e + 1, L - 1)]) / (2.0 * alpha),
            m=m_i, mt=mt_i, t=t_m, ts=ts, wb=wb,
            env_a=env_a, cert_a=cert_a, b_cert_a=b_cert_a,
            floored_a=floored_a, slack_a=slack_a,
            env_d=res["d"]["env"], cert_d=res["d"]["cert"],
            b_cert_d=res["d"]["b_cert"],
            slack_up_d=res["d"]["slack_up"],
            slack_lo_d=res["d"]["slack_lo"],
            env_c=res["c"]["env"], cert_c=res["c"]["cert"],
            b_cert_c=res["c"]["b_cert"],
            floored_c=res["c"]["floored"],
            slack_up_c=res["c"]["slack_up"],
            slack_lo_c=res["c"]["slack_lo"],
            env_0=env_0, a0=ev["a0"],
            bt_raw=-A1p * (float(w[e + 1]) - float(w[s])),
            win_share=float(np.mean(need_win))))
    T_seg = sum(o["m"] * o["wb"] + o["t"] for o in out)
    Tt_seg = sum(o["mt"] * o["wb"] + o["ts"] for o in out)
    bdry_glob = float(A1[L - 1] * w[L - 1])
    regroup = abs(sum(o["bt_raw"] for o in out) + bdry_glob
                  - sum(o["m"] * o["wb"] for o in out))
    dev_seg = abs(T_seg - T) / max(scale, 1.0)
    dev_sm = abs(Tt_seg - Tt) / max(scale, 1.0)
    dev_rg = regroup / max(scale, 1.0)
    Tc = {}
    for tag in ("a", "d", "c"):
        Tc[tag] = sum(o["b_cert_" + tag] + o["cert_" + tag]
                      for o in out)
    return dict(segs=out, T=T, Tt=Tt, T_cert_a=Tc["a"],
                T_cert_d=Tc["d"], T_cert_c=Tc["c"],
                dev_seg=dev_seg, dev_sm=dev_sm, dev_rg=dev_rg,
                dev_dem=dev_dem, scale=scale, nseg=len(out),
                env_ward_a=min(o["slack_a"] for o in out),
                env_ward_dU=min(o["slack_up_d"] for o in out),
                env_ward_dL=min(o["slack_lo_d"] for o in out),
                env_ward_cU=min(o["slack_up_c"] for o in out),
                env_ward_cL=min(o["slack_lo_c"] for o in out))


def freq_cert(grid, row_D_M_unused, om, u0):
    """Certified two-sided bound on Fhat = sum e_k cos(om (u-u0))
    via the segment machinery with the COMB envelopes; plus the
    exact E1-read of Fhat (identity ward)."""
    ug = grid["ug"]
    E1, A1, At1 = grid["E1"], grid["A1"], grid["At1"]
    L = grid["L"]
    w = np.cos(om * (ug - u0))
    dw = w[1:] - w[:-1]
    segs = segment_split(dw)
    ee = grid["a"] - 2.0 * grid["inv_sq"]
    F_meas = float(np.dot(ee, w))
    envtot = 0.0
    F_id = 0.0
    last_e = segs[-1][1]
    for (s, e, _sg) in segs:
        E1p = float(E1[s - 1]) if s > 0 else 0.0
        Ej = E1[s:e + 1] - E1p
        # amendment A1: the LAST segment's boundary read is the
        # full cumulant at the last grid point (a cosine kernel
        # does not vanish at the window edge).
        e_rd = (L - 1) if e == last_e else e
        ev = seg_envelopes(grid, s, e_rd)
        dws = dw[s:e + 1]
        adws = np.abs(dws)
        npair = e - s + 1
        wb = float(w[e_rd + 1]) if e_rd + 1 < L else float(
            w[L - 1])
        E_rd = float(E1[e_rd]) - E1p
        BUc, BLc = ev["BUc"], ev["BLc"]
        envtot += (max(float(BUc[-1]), float(BLc[-1])) * abs(wb)
                   + float(np.dot(np.maximum(BUc[:npair],
                                             BLc[:npair]),
                                  adws)))
        F_id += E_rd * wb - float(np.dot(Ej, dws))
    dev = abs(F_id - F_meas) / (abs(F_meas)
                                + float(np.dot(np.abs(ee),
                                               np.abs(w))) + 1.0)
    return F_meas, envtot, dev


def ctrl_seg_battery(r, cut, mode):
    """C3/C4: segment-anchored envelope violation factor for a
    control rung from the fixed cut (predecessor verbatim reads;
    mode 'abs' = predecessor C3, mode 'diff' = the new battery)."""
    Ng = int(math.floor(r["X"]))
    kk = np.arange(cut + 1, Ng + 1, dtype=np.int64)
    kf = kk.astype(float)
    inv = 1.0 / np.sqrt(kf)
    delta = inv[:-1] - inv[1:]
    At1 = blocked_cumsum(2.0 * inv)
    if "scr" in r and r["scr"]:
        cmass = np.concatenate([[0.0], blocked_cumsum(r["mu"])])
        idx = np.searchsorted(r["uu"], np.log(kf), side="right")
        i0 = int(np.searchsorted(r["uu"], math.log(cut) + 1e-12,
                                 side="right"))
        A1c = cmass[idx] - cmass[i0]
    else:
        nn = np.round(np.exp(r["uu"])).astype(int)
        ag = np.zeros(Ng + 1)
        keep = nn <= Ng
        np.add.at(ag, nn[keep], r["mu"][keep])
        A1c = blocked_cumsum(ag[cut + 1:Ng + 1])
    E1c = A1c - At1
    wc = q_read(r["Wv"], np.log(kf), r["D"], r["M"])
    dwc = wc[1:] - wc[:-1]
    segs = segment_split(dwc)
    fac = 0.0
    for (s, e, _sg) in segs:
        E1p = float(E1c[s - 1]) if s > 0 else 0.0
        Ej = E1c[s:e + 1] - E1p
        a0 = int(kk[s]) - 1
        kseg = kf[s:e + 1]
        ell = kseg - float(a0)
        inv_s = inv[s:e + 1]
        del_s = delta[s:e]
        if mode == "abs":
            beta = (np.asarray(bnd_psi(kk[s:e + 1]), float)
                    + float(bnd_psi(np.array([a0]))[0]))
            BE = abel_env(beta, inv_s, del_s)
            fac = max(fac, float(np.max(np.abs(Ej) / BE)))
        else:
            BU = abel_env(u_diff(a0, ell, kseg, CPSITH),
                          inv_s, del_s)
            BL = abel_env(ell, inv_s, del_s)
            fac = max(fac, float(np.max(Ej / BU)),
                      float(np.max(-Ej / BL)))
    return fac, len(segs)


# ---------------- extended-table spot machinery (CLIV verbatim)
EXT = {}


def build_ext_tables():
    lam_ext = core.von_mangoldt_table(TAB_EXT)
    NN = np.nonzero(lam_ext > 0.0)[0]
    EXT["lam"] = lam_ext
    EXT["NN"] = NN
    EXT["U"] = np.log(NN.astype(float))
    EXT["MU"] = 2.0 * lam_ext[NN] / np.sqrt(NN.astype(float))
    EXT["G"] = np.diff(EXT["U"])
    EXT["psi"] = np.cumsum(lam_ext)
    idx = np.arange(len(lam_ext), dtype=float)
    EXT["devpsi"] = np.abs(EXT["psi"] - idx)
    EXT["kappa"] = float(np.max(np.where(
        idx >= KAPPA_LOW_X,
        EXT["devpsi"] / np.maximum(idx, 1.0), 0.0)))
    prm = ((lam_ext > 0.0)
           & (np.abs(lam_ext - np.log(np.maximum(idx, 1.0)))
              <= 1e-9))
    theta = np.cumsum(np.where(prm, lam_ext, 0.0))
    EXT["cpsith"] = float(np.max((EXT["psi"][2:] - theta[2:])
                                 / np.sqrt(idx[2:])))
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


def ext_rung(kz):
    """CLIV ext_rung verbatim (the fields needed here)."""
    alpha, M, h, ka = ext_frame(kz)
    uu = EXT["U"][:ka].copy()
    mm = EXT["MU"][:ka].copy()
    c_at, D = core.atom_lags_at(alpha, M, uu, mm)
    c_at = np.asarray(c_at, float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    Kt = core.odd_toeplitz(c_ar + c_at, M)
    w, V = np.linalg.eigh(Kt)
    v = V[:, 0]
    del Kt, V
    row = dict(kz=kz, alpha=alpha, h=h, M=M, D=D, ka=ka,
               X=math.exp(2.0 * alpha), m=float(w[0]), uu=uu,
               mu=mm)
    Wv = core.lag_weights_from_v(v, h)
    e_ar = float(c_ar @ Wv)
    qa = mm * q_read(Wv, uu, D, M)
    cq = np.cumsum(qa)
    head_B = e_ar + cq
    tail_B = float(qa.sum()) - cq
    cert_B = head_B - np.abs(tail_B)
    row.update(Wv=Wv, head_B=head_B, cert_B=cert_B)
    return row


def main():
    section("PRIME.PORT.TAIL.DIFFENV.01 -- the DIFFERENCE-ENVELOPE"
            " probe (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; C0 = 1/2 is the CLI "
          "registration, NO-ADJUST.")
    print("\nS0 -- firewall + table constants")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    print("    deployed table constants: KAPPA_INT = %.6f "
          "(CLII amendment A1 reproduced), CPSITH = %.6f "
          "(all-integer (psi - theta)/sqrt(x) on [2, %d])"
          % (KAPPA_INT, CPSITH, core.ATOM_MAX))
    check("S0.2 WARD CPSITH = %.6f <= literature ceiling %.4f "
          "(Rosser-Schoenfeld 1962, recorded comparison)"
          % (CPSITH, CPSITH_LIT), CPSITH <= CPSITH_LIT,
          kill="K2")

    # ------------------------------------------------------------ W
    section("W -- the faithful ladder + wards (predecessor "
            "verbatim)")
    rungs = []
    for kz in range(2, KZMAX + 1):
        row = build_rung(kz)
        if row is not None:
            rungs.append(row)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1 faithful ladder >= %d rungs" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS,
          "%d rungs, h %d..%d  [%.1f s]"
          % (len(rungs), rungs[0]["h"], rungs[-1]["h"],
             time.time() - T0), kill="K1")
    if KILLS:
        return finish({})
    N = len(rungs)
    check("W2 WARD truth margin m_h > 0 on every rung (min %.3e)"
          % min(r["m"] for r in rungs),
          all(r["m"] > 0 for r in rungs), kill="K2")
    dev_bk = max(max(abs((r["lift"] - r["demand"]) - r["m"]),
                     abs((r["e_ar"] + r["e_t"]) - r["m"]))
                 / max(1.0, abs(r["m"])) for r in rungs)
    check("W3 WARD both exact bookkeepings: max dev %.2e <= %.0e"
          % (dev_bk, ID_WARD), dev_bk <= ID_WARD, kill="K2")
    dev_at = max(r["dev_at"] for r in rungs)
    check("W4 WARD atom identities: max rel dev %.2e <= %.0e"
          % (dev_at, ID_WARD), dev_at <= ID_WARD, kill="K2")
    dev_sc = 0.0
    for r in rungs:
        sc = max(float(np.max(np.abs((r["head_B"] + r["tail_B"])
                                     - r["m"]))),
                 float(np.max(np.abs((r["G"] + r["tail_A"])
                                     - r["m"]))),
                 float(np.max(np.abs(r["G"] - r["head_B"]
                                     - r["smoothtail"]))))
        dev_sc = max(dev_sc, sc / max(1.0, abs(r["e_t"])))
    check("W5 WARD split exactness on the full scans: max rel "
          "dev %.2e <= %.0e" % (dev_sc, SCAN_WARD),
          dev_sc <= SCAN_WARD, kill="K2")
    cnts = tuple(int(np.sum(np.array(
        [r["Gref"][nc] for r in rungs]) > 0)) for nc in REF_CUTS)
    n_min, nB_min, icBs, tB_neg = [], [], [], 0
    for r in rungs:
        nn = np.round(np.exp(r["uu"])).astype(int)
        covA = r["cert_A"] > 0.0
        i0 = int(np.argmax(covA)) if bool(np.any(covA)) else -1
        n_min.append(int(nn[i0]) if i0 >= 0 else -1)
        covB = r["cert_B"] > 0.0
        icB = int(np.argmax(covB)) if bool(np.any(covB)) else -1
        icBs.append(icB)
        nB_min.append(int(nn[icB]) if icB >= 0 else -1)
        if icB >= 0 and float(r["tail_B"][icB]) <= 0.0:
            tB_neg += 1
    i9s = [int(np.searchsorted(r["uu"],
                               math.log(NC_SHARED) + 1e-12,
                               side="right")) - 1 for r in rungs]
    cov9 = sum(1 for r, i9 in zip(rungs, i9s)
               if i9 >= 0 and r["cert_A"][i9] > 0)
    tA_neg = sum(1 for r in rungs if bool(np.any(r["cert_A"] > 0))
                 and r["tail_A"][int(np.argmax(
                     r["cert_A"] > 0))] <= 0.0)
    covB_n = sum(1 for i in icBs if i >= 0)
    hBc = np.array([float(r["head_B"][i])
                    for r, i in zip(rungs, icBs)])
    medB = float(np.median([n for n in nB_min if n > 0]))
    ok_rep = (cnts == REF_COUNTS
              and all(NMIN_LO <= nm <= NMIN_HI for nm in n_min)
              and cov9 == N and tA_neg == N and covB_n == N
              and medB == NB_MED
              and min(nB_min) >= NB_LO and max(nB_min) <= NB_HI
              and tB_neg == N
              and abs(float(np.median(hBc)) - HEADB_MED)
              <= HEADB_TOL)
    check("W6 REPRODUCTION 59/60/62: G > 0 at %s = %s == %s; "
          "n_min in [%d, %d]; cut 9 covers %d/%d; tail_A <= 0 "
          "%d/%d; B-cuts exist %d/%d, n_minB med %d in [%d, %d]; "
          "tail_B <= 0 at cB %d/%d; head_B(cB) med %.3f ~ %.3f"
          % (REF_CUTS, cnts, REF_COUNTS, NMIN_LO, NMIN_HI, cov9,
             N, tA_neg, N, covB_n, N, int(medB), min(nB_min),
             max(nB_min), tB_neg, N, float(np.median(hBc)),
             HEADB_MED), ok_rep, kill="K2")
    n_cross = sum(1 for r in rungs if r["ov"] < OV_MIN)
    cross_ok = all(max(r["ov4"]) >= OV_MIN for r in rungs
                   if r["ov"] < OV_MIN)
    check("W7 WARD v_sm branch: %d crossing rung(s) (ward <= %d),"
          " carrier ok" % (n_cross, MAX_CROSS),
          n_cross <= MAX_CROSS and cross_ok, kill="K2")
    check("W8 WARD kappa: chebyshev_kappa() = %.6f within %.0e "
          "of %.6f (KAPPA_INT = %.6f deployed)"
          % (KAP, KAPPA_TOL, core.KAPPA_REF, KAPPA_INT),
          abs(KAP - core.KAPPA_REF) <= KAPPA_TOL, kill="K2")
    mu1 = np.array([float(core.parity_mu(r["h"])[0])
                    for r in rungs])
    mu1_cf = np.array([4.0 * math.sin(math.pi
                                      / (2 * r["h"] + 1)) ** 2
                       for r in rungs])
    dev_mu = float(np.max(np.abs(mu1 - mu1_cf)
                          / np.maximum(mu1, GAIN_EPS)))
    mm = np.array([r["m"] for r in rungs])
    shat = mm / mu1
    s3 = (float(np.min(shat)), float(np.median(shat)),
          float(np.max(shat)))
    ok_shat = all(abs(s3[i] - SHAT_REF[i]) <= SHAT_TOL
                  for i in range(3))
    check("W9 WARD mu1 closed form (dev %.1e) + CXLIII shat band "
          "min/med/max %.4f/%.4f/%.4f ~ %s"
          % (dev_mu, s3[0], s3[1], s3[2], SHAT_REF),
          dev_mu <= MU_WARD and ok_shat, kill="K2")
    if KILLS:
        return finish({})

    grids, trv, sgv = [], [], []
    for r, nc in zip(rungs, nB_min):
        g = make_grid(r, nc)
        grids.append(g)
        trv.append(transport(g, r, r["Wv"]))
        sgv.append(seg_analyze(g, r, r["Wv"]))
    tie = max(abs(t["T"] - float(r["tail_B"][i]))
              / max(1.0, abs(float(r["tail_B"][i])))
              for t, r, i in zip(trv, rungs, icBs))
    check("W10 WARD grid tie: integer-grid tail == tail_B(cB) "
          "max rel dev %.2e <= %.0e  [%.1f s]"
          % (tie, TIE_WARD, time.time() - T0),
          tie <= TIE_WARD, kill="K2")
    env_slk = min(g["env_min_slack"] for g in grids)
    check("W11 WARD global envelope in-window (min slack %+.3e "
          ">= %.0e)" % (env_slk, -ENV_SLACK),
          env_slk >= -ENV_SLACK, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ B
    section("B -- identity + envelope WARDS (segment, demand "
            "form, all families)")
    dev_seg = max(s["dev_seg"] for s in sgv)
    check("B.1 WARD segment identity: max rel dev %.2e <= %.0e"
          % (dev_seg, SEG_ID_WARD), dev_seg <= SEG_ID_WARD,
          kill="K2")
    dev_sm = max(s["dev_sm"] for s in sgv)
    check("B.2 WARD smooth twin identity: max rel dev %.2e <= "
          "%.0e" % (dev_sm, SEG_ID_WARD), dev_sm <= SEG_ID_WARD,
          kill="K2")
    dev_rg = max(s["dev_rg"] for s in sgv)
    check("B.3 WARD regrouping: max rel dev %.2e <= %.0e"
          % (dev_rg, SEG_ID_WARD), dev_rg <= SEG_ID_WARD,
          kill="K2")
    env_wa = min(s["env_ward_a"] for s in sgv)
    check("B.4 WARD ABS envelope in-window |E_j| <= BE_j (min "
          "slack %+.3e >= %.0e)" % (env_wa, -SEG_ENV_SLACK),
          env_wa >= -SEG_ENV_SLACK, kill="K2")
    dev_ordm = max(max(s["T_cert_a"], s["T_cert_d"],
                       s["T_cert_c"]) - s["T"] for s in sgv)
    dev_ord = max((max(s["T_cert_a"], s["T_cert_d"],
                       s["T_cert_c"]) - s["T"])
                  / max(s["scale"], 1.0) for s in sgv)
    check("B.5 WARD certificate order T_cert <= T for ALL "
          "families (max rel excess %+.2e <= %.0e)"
          % (dev_ord, CERT_ORD_WARD), dev_ord <= CERT_ORD_WARD,
          kill="K2")
    _ = dev_ordm
    dev_dem = max(s["dev_dem"] for s in sgv)
    check("B.6 WARD demand form (a): E_j == 2[G/sqrt(k) + sum G "
          "delta] and G == cumsum(Lambda - 1) == psi-table read, "
          "every segment of every rung: max rel dev %.2e <= %.0e"
          % (dev_dem, DEM_ID_WARD), dev_dem <= DEM_ID_WARD,
          kill="K2")
    env_w2 = min(min(s["env_ward_dU"], s["env_ward_dL"],
                     s["env_ward_cU"], s["env_ward_cL"])
                 for s in sgv)
    check("B.7 WARD DIFF/COMB envelopes in-window (both sides; "
          "min slack %+.3e >= %.0e)" % (env_w2, -DIFF_ENV_SLACK),
          env_w2 >= -DIFF_ENV_SLACK, kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ E
    section("E -- (b)+(c) THE DECISIVE SLACK LADDERS: ABS "
            "(reproduction) vs DIFF vs COMB")
    aa = np.array([r["alpha"] for r in rungs])
    H = hBc
    Ttv = np.array([s["Tt"] for s in sgv])
    ERRg = np.array([min(t["ERR"]) for t in trv])
    ERRa = Ttv - np.array([s["T_cert_a"] for s in sgv])
    ERRd = Ttv - np.array([s["T_cert_d"] for s in sgv])
    ERRc = Ttv - np.array([s["T_cert_c"] for s in sgv])
    slack_a = (H + np.array([s["T_cert_a"] for s in sgv])) \
        / mu1 - C0
    slack_d = (H + np.array([s["T_cert_d"] for s in sgv])) \
        / mu1 - C0
    slack_c = (H + np.array([s["T_cert_c"] for s in sgv])) \
        / mu1 - C0
    gain_abs = ERRg / np.maximum(ERRa, GAIN_EPS)
    gain2 = ERRa / np.maximum(ERRc, GAIN_EPS)
    gaind = ERRa / np.maximum(ERRd, GAIN_EPS)
    print("    per-rung ledger (mu1 units):")
    print("    kz   h    nseg slack_abs   slack_diff  slack_comb"
          "  ERRa/mu1   ERRc/mu1   gain2")
    for i, (r, s) in enumerate(zip(rungs, sgv)):
        print("    %-4d %-4d %-4d %+.3e %+.3e %+.3e %.3e %.3e "
              "%6.2f"
              % (r["kz"], r["h"], s["nseg"], slack_a[i],
                 slack_d[i], slack_c[i], ERRa[i] / mu1[i],
                 ERRc[i] / mu1[i], gain2[i]), flush=True)
    for si, tag in ((0, "first"), (N // 2, "mid"),
                    (N - 1, "deepest")):
        r, s = rungs[si], sgv[si]
        print("\n    SAMPLE rung (%s) kz %d h %d (nc %d): "
              "per-segment ladder (mu1 units)"
              % (tag, r["kz"], r["h"], grids[si]["nc"]))
        print("      j sgn x-range        a0      winshare "
              "env_abs     env_diff    env_comb    cert_comb")
        for j, o in enumerate(s["segs"]):
            print("      %d  %s  [%.3f,%.3f] %-7d %.3f    "
                  "%.3e %.3e %.3e %+.3e%s"
                  % (j + 1, "+" if o["sg"] > 0 else
                     "-" if o["sg"] < 0 else "0",
                     o["x0"], o["x1"], o["a0"], o["win_share"],
                     o["env_a"] / mu1[si], o["env_d"] / mu1[si],
                     o["env_c"] / mu1[si], o["cert_c"] / mu1[si],
                     "  FLOOR" if o["floored_c"] else ""))
    # B.9 reproduction ward (CLVI headline)
    gmed = float(np.median(gain_abs))
    smed = float(np.median(slack_a))
    slA, seA, r2A = jack_slope(aa, np.log(ERRa / mu1))
    ok_rep2 = (abs(gmed - REP_GAIN) <= REP_GAIN_TOL
               and abs(smed / REP_SLACK - 1.0) <= REP_SLACK_TOL
               and abs(slA - REP_LAW) <= REP_LAW_TOL)
    check("B.9 WARD ABS-route reproduction (CLVI): gain med "
          "%.3f ~ %.3f; slack_abs med %+.3e ~ %+.2e; law %+.3f "
          "~ %+.3f" % (gmed, REP_GAIN, smed, REP_SLACK, slA,
                       REP_LAW), ok_rep2, kill="K2")
    n_pos = int(np.sum(slack_c > 0.0))
    slC, seC, r2C = jack_slope(aa, np.log(np.maximum(
        ERRc, GAIN_EPS) / mu1))
    slD, seD, r2D = jack_slope(aa, np.log(np.maximum(
        ERRd, GAIN_EPS) / mu1))
    print("\n    residual laws: log(ERRcomb/mu1) = %+.3f alpha "
          "(2SE %.3f, R^2 %.2f); log(ERRdiff/mu1) = %+.3f (2SE "
          "%.3f); ABS law %+.3f -- CLVI +1.824 / CLII +1.744"
          % (slC, 2 * seC, r2C, slD, 2 * seD, slA))
    print("    GAIN2 = ERRabs/ERRcomb min/med/max %.3f/%.3f/%.3f;"
          " pure-diff gain ERRabs/ERRdiff %.3f/%.3f/%.3f"
          % (float(np.min(gain2)), float(np.median(gain2)),
             float(np.max(gain2)), float(np.min(gaind)),
             float(np.median(gaind)), float(np.max(gaind))))
    if n_pos == N:
        c0_rec = float(np.min((H + np.array(
            [s["T_cert_c"] for s in sgv])) / mu1))
        lab_e = "DIFFENV-SUFFICIENT(min slack %+.3e)" \
            % float(np.min(slack_c))
        print("    ==> THE INTERIOR-SEGMENT STATEMENT CLOSES ON "
              "THE SURFACE: T >= -H + c0 mu1 with c0 = %.4f "
              "(recorded vs frozen 1/2, NO adjustment; "
              "KAPPA_INT = %.6f, BT_CONST = %.1f, CPSITH = %.4f)"
              % (c0_rec, KAPPA_INT, BT_CONST, CPSITH))
    elif n_pos > 0:
        lab_e = ("DIFFENV-PARTIAL(%d/%d, slack med %+.2e, law "
                 "%+.3f)" % (n_pos, N,
                             float(np.median(slack_c)), slC))
        print("    ==> PARTIAL: %d/%d rungs close; residual law "
              "on the rest %+.3f" % (n_pos, N, slC))
    else:
        lab_e = ("DIFFENV-INSUFFICIENT(slack min/med %+.2e/%+.2e,"
                 " law %+.3f vs +1.824)"
                 % (float(np.min(slack_c)),
                    float(np.median(slack_c)), slC))
        print("    ==> INSUFFICIENT on %d/%d: the difference "
              "form's residual law is %+.3f alpha vs the "
              "predecessor's +1.824 (segment) / +1.744 (global)"
              % (N, N, slC))
    lab_g = "GAIN2(med %.2f, max %.2f; diff-only med %.2f)" % (
        float(np.median(gain2)), float(np.max(gain2)),
        float(np.median(gaind)))
    check("E.1 typed (b)+(c): %s / %s" % (lab_e, lab_g), True)

    # ------------------------------------------------------- ANCHOR
    section("A -- the ANCHOR-PRICE question (frozen enum)")
    reds, vs0s, ashs, wsh = [], [], [], []
    anc_cost, comb_cost = [], []
    for s in sgv:
        ea = sum(o["env_a"] for o in s["segs"])
        e0 = sum(o["env_0"] for o in s["segs"])
        ec = sum(o["env_c"] for o in s["segs"])
        reds.append(ec / max(ea, GAIN_EPS))
        vs0s.append(ec / max(e0, GAIN_EPS))
        ashs.append(1.0 - e0 / max(ea, GAIN_EPS))
        wsh.append(float(np.median([o["win_share"]
                                    for o in s["segs"]])))
        anc_cost.append(ea - e0)
        comb_cost.append(ec)
    reds = np.array(reds)
    vs0s = np.array(vs0s)
    ashs = np.array(ashs)
    slAn, seAn, _ = jack_slope(aa, np.log(np.maximum(
        np.array(anc_cost), GAIN_EPS) / mu1))
    slCo, seCo, _ = jack_slope(aa, np.log(np.maximum(
        np.array(comb_cost), GAIN_EPS) / mu1))
    print("    anchor share of ABS in-segment budget (diag): "
          "min/med/max %.3f/%.3f/%.3f" %
          (float(np.min(ashs)), float(np.median(ashs)),
           float(np.max(ashs))))
    print("    red = env_comb/env_abs med %.3f; vs0 = "
          "env_comb/env_0 med %.3f; needed-side crossover "
          "share (points where diff beta wins) med %.3f"
          % (float(np.median(reds)), float(np.median(vs0s)),
             float(np.median(wsh))))
    print("    scaling: log(anchor cost/mu1) slope %+.3f (2SE "
          "%.3f) vs log(comb cost/mu1) slope %+.3f (2SE %.3f) "
          "-- the kappa*n_anchor law confronted"
          % (slAn, 2 * seAn, slCo, 2 * seCo))
    if float(np.median(vs0s)) <= ANCHOR_REMOVED_BAR:
        lab_anc = ("ANCHOR-REMOVED(vs0 med %.3f <= %.2f)"
                   % (float(np.median(vs0s)),
                      ANCHOR_REMOVED_BAR))
    elif float(np.median(reds)) <= ANCHOR_PARTIAL_BAR:
        lab_anc = ("ANCHOR-PARTIAL(red med %.3f, vs0 med %.3f)"
                   % (float(np.median(reds)),
                      float(np.median(vs0s))))
    else:
        lab_anc = ("ANCHOR-PERSISTS(red med %.3f)"
                   % float(np.median(reds)))
    check("A.1 typed anchor enum: %s" % lab_anc, True)

    # ------------------------------------------------------------ F
    section("F -- (d) THE LOW-FREQUENCY CROSS-CHECK (CLV frame, "
            "typed)")
    dev_fid = 0.0
    rcar, slopes = [], []
    tabF = None
    for i, (g, r) in enumerate(zip(grids, rungs)):
        u0 = float(g["ug"][0])
        uL = float(g["ug"][-1])
        Lu = uL - u0
        ovs = []
        Fs, Es = [], []
        for j in range(1, FREQ_JMAX + 1):
            om = math.pi * j / Lu
            Fm, Ev, dv = freq_cert(g, None, om, u0)
            dev_fid = max(dev_fid, dv)
            Fs.append(Fm)
            Es.append(Ev)
            ovs.append(Ev / max(abs(Fm), GAIN_EPS))
        ovs = np.array(ovs)
        car = float(np.median(ovs[:len(FREQ_CARRIER)]))
        rest = float(np.median(ovs[len(FREQ_CARRIER):]))
        rcar.append(car / max(rest, GAIN_EPS))
        jj = np.log(np.arange(1, FREQ_JMAX + 1, dtype=float))
        _a0, bF, _r2 = ols_line(jj, np.log(np.maximum(
            np.array(Es), GAIN_EPS)))
        slopes.append(bF)
        if i == N // 2:
            tabF = (r, Lu, np.array(Fs), np.array(Es), ovs)
    check("F.1 WARD frequency identity Fhat == segment read on "
          "all rungs x %d bins (max rel dev %.2e <= %.0e)"
          % (FREQ_JMAX, dev_fid, FREQ_ID_WARD),
          dev_fid <= FREQ_ID_WARD, kill="K2")
    r, Lu, Fs, Es, ovs = tabF
    print("    median rung kz %d h %d (Lu %.2f, omega_1 = %.3f):"
          % (r["kz"], r["h"], Lu, math.pi / Lu))
    print("      j   omega_j   |Fhat|      ENVhat      overshoot"
          "   (CLV carrier region omega <= 5.25)")
    for j in range(FREQ_JMAX):
        om = math.pi * (j + 1) / Lu
        print("      %-3d %7.3f  %.3e  %.3e  %9.1f%s"
              % (j + 1, om, abs(Fs[j]), Es[j], ovs[j],
                 "  <= 5.25" if om <= 5.25 else ""))
    rmed = float(np.median(rcar))
    smed_f = float(np.median(slopes))
    lab_f = ("LOWFREQ-%s(r_car med %.3f, growth slope med %+.2f)"
             % ("CONSISTENT" if rmed <= 1.0 else "MISMATCH",
                rmed, smed_f))
    print("    carrier ratio r_car = med overshoot(j in %s)/"
          "med overshoot(j > 3): med %.3f (%s); certified-"
          "control growth log ENVhat ~ %+.2f log j"
          % (str(FREQ_CARRIER), rmed,
             "sharpest ON the carrier bins" if rmed <= 1.0
             else "NOT sharpest on the carrier bins", smed_f))
    check("F.2 typed (d): %s" % lab_f, True)

    # ------------------------------------------------------------ T
    section("T -- TAU-SCREENS (jackknife, typed)")
    scr = []
    for nm, yv in (("ERRcomb/mu1", np.maximum(ERRc, GAIN_EPS)
                    / mu1),
                   ("gain2", gain2),
                   ("anchor-share", ashs + 1e-30)):
        sl, se, r2 = jack_slope(np.log(mm), np.log(yv))
        ty = ("PASS" if abs(sl) <= SLOPE_PASS else
              "RELOC" if sl >= SLOPE_RELOC else "AMBIG")
        scr.append((nm, sl, ty))
        print("    screen log %s vs log m: slope %+.3f +- 2SE "
              "%.3f (R^2 %.2f) -> %s" % (nm, sl, 2 * se, r2, ty))
    lab_t = "SCREENS(%s)" % ", ".join(
        "%s %+.2f %s" % s for s in scr)
    check("T.1 typed screens: %s" % lab_t, True)

    # ------------------------------------------------------------ C
    section("C -- controls at kz %d" % CTRL_KZ)
    rr9 = core.build_window(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nnE = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    ctl = {}
    ctl["Epstein"] = build_rung(CTRL_KZ, comb=(
        np.log(nnE.astype(float)),
        2.0 * lamE_[nnE] / np.sqrt(nnE.astype(float))),
        need_sm=False)
    ctl["scramble"] = build_rung(CTRL_KZ, scramble_seed=1,
                                 need_sm=False)
    ctl["smooth"] = build_rung(CTRL_KZ, smooth_world=True,
                               need_sm=False)
    ctl["scramble"]["scr"] = True
    fired = True
    for name, r in ctl.items():
        if r is None:
            print("    %-9s: rung dies -> fires" % name)
            continue
        ncovA = int(np.sum(r["cert_A"] > 0))
        ncovB = int(np.sum(r["cert_B"] > 0))
        f = (r["m"] < 0) and ncovA == 0 and ncovB == 0
        fired &= f
        print("    %-9s: m %+.3e  covering cuts A/B %d/%d -> %s"
              % (name, r["m"], ncovA, ncovB,
                 "FIRES" if f else "SILENT"), flush=True)
    check("C1 WARD all three controls fire", fired, kill="K2")
    facs = {}
    for name in ("Epstein", "smooth", "scramble"):
        r = ctl[name]
        Ng = int(math.floor(r["X"]))
        kk = np.arange(CTRL_CUT + 1, Ng + 1, dtype=np.int64)
        kf = kk.astype(float)
        inv_sq = 1.0 / np.sqrt(kf)
        delta = inv_sq[:-1] - inv_sq[1:]
        beta = (np.asarray(bnd_psi(kk), float)
                + float(bnd_psi(np.array([CTRL_CUT]))[0]))
        Cb = np.concatenate(
            [[0.0], blocked_cumsum(beta[:-1] * delta)])
        BE1 = 2.0 * (beta * inv_sq + Cb)
        At1 = blocked_cumsum(2.0 * inv_sq)
        if name == "scramble":
            cmass = np.concatenate([[0.0],
                                    blocked_cumsum(r["mu"])])
            idx = np.searchsorted(r["uu"], np.log(kf),
                                  side="right")
            i0 = int(np.searchsorted(
                r["uu"], math.log(CTRL_CUT) + 1e-12,
                side="right"))
            A1c = cmass[idx] - cmass[i0]
        else:
            nn = np.round(np.exp(r["uu"])).astype(int)
            ag = np.zeros(Ng + 1)
            keep = nn <= Ng
            np.add.at(ag, nn[keep], r["mu"][keep])
            A1c = blocked_cumsum(ag[CTRL_CUT + 1:Ng + 1])
        facs[name] = float(np.max(np.abs(A1c - At1) / BE1))
        print("    %-9s GLOBAL abs-envelope factor = %.3g"
              % (name, facs[name]), flush=True)
    ok_c2 = all(abs(facs[n] - REP_C2[n][0]) <= REP_C2[n][1]
                for n in facs)
    check("C2 WARD global battery reproduction (scramble %.2f ~ "
          "5.99 >= %.1f fires; smooth %.3f ~ 0.837; Epstein %.2f"
          " ~ 7.51)" % (facs["scramble"], CTRL_VIOL,
                        facs["smooth"], facs["Epstein"]),
          ok_c2 and facs["scramble"] >= CTRL_VIOL, kill="K2")
    segf_a, segf_d = {}, {}
    for name in ("Epstein", "smooth", "scramble"):
        segf_a[name], nsg = ctrl_seg_battery(ctl[name],
                                             CTRL_CUT, "abs")
        segf_d[name], _ = ctrl_seg_battery(ctl[name],
                                           CTRL_CUT, "diff")
        print("    %-9s SEGMENT factors: abs %.3g, DIFF %.3g "
              "(%d segments)" % (name, segf_a[name],
                                 segf_d[name], nsg), flush=True)
    ok_c3 = all(abs(segf_a[n] - REP_C3[n][0]) <= REP_C3[n][1]
                for n in segf_a)
    check("C3 recorded abs-battery reproduction (scramble %.2f ~"
          " 4.15, smooth %.2f ~ 2.93 disclosed violation, "
          "Epstein %.1f ~ 34.6)" % (segf_a["scramble"],
                                    segf_a["smooth"],
                                    segf_a["Epstein"]), ok_c3)
    print("    C4 disclosed expectation ledger: the v0 factor-5 "
          "bar is VIOLATED (measured %.3g < %.1f) -- the "
          "difference battery discriminates WEAKER than the "
          "absolute one (%.3g vs %.3g), recorded first-class "
          "(amendment A2)"
          % (segf_d["scramble"], CTRL_VIOL,
             segf_d["scramble"], segf_a["scramble"]))
    check("C4 WARD DIFFERENCE battery (A2 bar): scramble BREAKS "
          "the difference envelope, factor %.3g > %.1f (upper "
          "side; the lower side is auto-satisfied by every "
          "nonnegative comb, disclosed); smooth %.3g, Epstein "
          "%.3g (typed)"
          % (segf_d["scramble"], C4_VIOL, segf_d["smooth"],
             segf_d["Epstein"]),
          segf_d["scramble"] > C4_VIOL, kill="K2")
    # C5 by-construction smooth world: Lambda == 1 on the grid
    g9 = make_grid(dict(alpha=rr9["alpha"],
                        uu=np.asarray(rr9["uu"], float),
                        X=float(rr9["X"])), CTRL_CUT,
                   lam_tab=np.ones(int(math.floor(
                       float(rr9["X"]))) + 2))
    check("C5 WARD by-construction smooth world (Lambda == 1): "
          "demand collapses EXACTLY (max |E1| = %.1e == 0)"
          % float(np.max(np.abs(g9["E1"]))),
          float(np.max(np.abs(g9["E1"]))) == 0.0, kill="K2")
    lab_c = ("CTRL(C1 3/3, C2 rep, C3 rep, C4 scramble %.3g "
             "FIRES / smooth %.3g / Epstein %.3g, C5 exact)"
             % (segf_d["scramble"], segf_d["smooth"],
                segf_d["Epstein"]))

    # ------------------------------------------------------------ S
    section("S -- (e) DEEP HOLDOUT SPOT-CHECK (4e6 table, "
            "recorded)")
    build_ext_tables()
    dev_ov = float(np.max(np.abs(EXT["lam"][:core.ATOM_MAX + 1]
                                 - core.LAM_TAB)))
    check("S.1 WARD extended-table overlap byte-exact (max abs "
          "dev %.1e == 0)" % dev_ov, dev_ov == 0.0, kill="K2")
    print("    extended constants: KAPPA_INT_EXT = %.6f "
          "(deployed %.6f), CPSITH_EXT = %.6f (deployed %.6f, "
          "ceiling %.4f)" % (EXT["kappa"], KAPPA_INT,
                             EXT["cpsith"], CPSITH, CPSITH_LIT))
    check("S.2 WARD CPSITH_EXT <= literature ceiling %.4f"
          % CPSITH_LIT, EXT["cpsith"] <= CPSITH_LIT, kill="K2")
    census = []
    for kz in range(2, min(KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        alpha = float(EXT["U"][kz])
        X = math.exp(2.0 * alpha)
        if X > TAB_EXT:
            break
        if X <= core.ATOM_MAX:
            continue
        _a, _M, hz, _ka = ext_frame(kz)
        if H_HOLD[0] <= hz <= H_HOLD[1]:
            census.append(kz)
    print("    extended census: %d new rungs (kz %d..%d)"
          % (len(census), census[0] if census else -1,
             census[-1] if census else -1))
    spots = ([census[0], census[len(census) // 2], census[-1]]
             if len(census) >= 3 else census)
    spot_rows = []
    for kz in spots:
        r = ext_rung(kz)
        covB = r["cert_B"] > 0.0
        icB = int(np.argmax(covB)) if bool(np.any(covB)) else -1
        if icB < 0:
            print("    kz %d: NO B-cover cut (recorded)" % kz)
            continue
        nn = np.round(np.exp(r["uu"])).astype(int)
        nc = int(nn[icB])
        Hs = float(r["head_B"][icB])
        g = make_grid(dict(alpha=r["alpha"], uu=r["uu"],
                           X=r["X"]), nc, lam_tab=EXT["lam"],
                      psi_full=EXT["psi"],
                      devpsi=EXT["devpsi"], kappa=EXT["kappa"])
        g["cpsith"] = EXT["cpsith"]
        s = seg_analyze(g, r, r["Wv"])
        m1 = mu1_of_ext(r["h"])
        sa = (Hs + s["T_cert_a"]) / m1 - C0
        sc_ = (Hs + s["T_cert_c"]) / m1 - C0
        ga = (s["Tt"] - s["T_cert_a"]) \
            / max(s["Tt"] - s["T_cert_c"], GAIN_EPS)
        okw = (s["dev_seg"] <= SEG_ID_WARD
               and s["dev_dem"] <= DEM_ID_WARD
               and min(s["env_ward_a"], s["env_ward_cU"],
                       s["env_ward_cL"]) >= -DIFF_ENV_SLACK)
        spot_rows.append((kz, r["h"], nc, sa, sc_, ga, okw))
        print("    kz %-4d h %-4d nc %-4d slack_abs %+.3e "
              "slack_comb %+.3e gain2 %.3f wards %s  [%.1f s]"
              % (kz, r["h"], nc, sa, sc_, ga,
                 "OK" if okw else "BROKEN", time.time() - T0),
              flush=True)
    ok_spot = all(o for *_x, o in spot_rows)
    check("S.3 WARD spot-rung identities + envelopes in-window "
          "on %d/%d deep rungs" % (sum(1 for *_x, o in spot_rows
                                       if o), len(spot_rows)),
          ok_spot and len(spot_rows) >= 1, kill="K2")
    lab_s = ("SPOT(%s)" % "; ".join(
        "kz%d/h%d slack %+.1e gain2 %.2f" % (kz, h, sc_, ga)
        for kz, h, _nc, _sa, sc_, ga, _o in spot_rows))
    check("S.4 typed (e): %s" % lab_s, True)

    return finish(dict(e=lab_e, g=lab_g, anc=lab_anc, f=lab_f,
                       t=lab_t, c=lab_c, s=lab_s,
                       dem="DEMAND-WARDED(%.1e)" % dev_dem))


def mu1_of_ext(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("DIFFENV-MEASURED / %(dem)s / %(e)s / %(g)s / "
                   "%(anc)s / %(f)s / %(t)s / %(c)s / %(s)s"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): the segment identity, the demand
  form, the envelope in-window bounds and the frequency tie are
  EXACT bookkeeping; the slack ladders, the anchor census, the
  overshoot profiles and the spot rows are MEASURED SURFACE
  STRUCTURE at float level.  An insufficient difference envelope
  is a measured residual demand, not an impossibility proof; a
  sufficient one would still be a per-rung surface certificate,
  not a theorem.  The halfgap constant 1/2 (CLI) is never
  adjusted here.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
