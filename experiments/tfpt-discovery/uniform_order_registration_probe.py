#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""uniform_order_registration_probe -- PRIME.ONEBADMODE.UNIFORM.ORDER.01
(EXPLORATION ONLY, experiments/; theorem-engineering on the RH-side
wall: the REGISTRATION -- not the celebration -- of the UNIFORM-ORDER
conjecture for the canonically Jacobi-equilibrated wall matrices.
2026-08-12.)

THE OBJECT.  CCVII (onebadmode_moments_probe) measured the one-bad-mode
Chebyshev moment certificate tr p_r(M_h) < 1 on the full combined
ladder (40 surface + 1 bridge + 27 deep steps) with r* = 14/30/119 and
identified the order price as the SPECTRAL WIDTH of the raw wall
matrix in tau units (r* = 0.544 sqrt(lam_max/c_B)); CLXXIII
(ub4_congruence_upgrade_probe) showed the diagonal-scale spread IS
that width and that the source-only Jacobi diagonal congruence
E = diag(d_i^{-1/2}), d_i the FLOAT diagonal of the computed matrix,
kills it.  THIS probe composes the two and REGISTERS the uniform-order
conjecture as a frozen falsification target in the HALFGAP pattern
(halfgap_registration_probe = the registered inequality with a frozen
constant, an explicit no-tuning clause, and blind holdouts):

    CONJECTURE (UNIFORM-ORDER):  EXISTS r0 < oo  s.t.  FOR ALL h
    (every faithful rung of the deployed family):
        tr p_{r0}( M~_h ) < 1,
    M~_h = E_h M_h E_h,  E_h = diag( (M_h)_ii^{-1/2} )
    the canonical CLXXIII Jacobi equilibration (float diagonal
    entries of the computed tau-unit wall matrix; entry reads only,
    source-only), p the squared scaled Chebyshev separator family
    with per-rung SOURCE-ONLY constants (c_h, L_h) by the frozen
    rule below.

THE IMPLICATION THEOREM (elementary; the chain is NOT the open part):
 (i)  p_r(x) = [T_r(m(x))/T_r(m(0))]^2, m(x) = (2x-(L+c))/(L-c),
      0 < c < L: p_r >= 0 everywhere (a square); p_r(0) = 1, |m| is
      decreasing on x <= 0 with |m(x)| >= |m(0)| > 1 and |T_r|
      increasing on [1, oo)  =>  p_r >= 1 on x <= 0.
 (ii) tr p_{r0}(M~) < 1  =>  M~ has no eigenvalue <= 0 (one
      nonpositive eigenvalue alone contributes >= 1 and every other
      eigenvalue contributes >= 0)  =>  M~ > 0.
 (iii) M~ = E M E with E invertible  =>  (Sylvester) M > 0  =>  the
      wall inequality at that h.
 (iv) FEASIBILITY (not soundness): the equilibrated B-block floor
      (Gershgorin, entry-level, or the transported cited floor) +
      Cauchy interlacing lam_2(M~) >= lam_1(B~) put the 7 bulk
      eigenvalues in [c, L]; then tr p_r(M~) <= p_r(lam_min) +
      7 eps_r, so a FIXED r0 suffices uniformly iff the equilibrated
      margin admits it.  The open content of the conjecture is
      therefore EXACTLY the uniform arithmetic trace inequality --
      the same supply class as HALFGAP (CCVII typed the moment route
      DISGUISE-MIXED with dn*/s med 0.354 IN-GRADE; no independence
      claim is made here).

FALSIFICATION CRITERION (part of the registered object): ONE true
faithful rung with tr p_{r0}(M~_h) >= 1 kills the registered
conjecture, full stop.

THE FROZEN NO-TUNING CLAUSE (recorded verbatim, first): r0 is FROZEN
by the rule "r_need := max over the 41 SURFACE + BRIDGE steps of the
minimal certifying order r*_eq; r0 := the smallest power of two
STRICTLY greater than r_need" -- chosen on the surface subset ONLY,
before the deep block enters any choice.  A later miss on any rung --
holdout or otherwise -- is a FAIL of the registered conjecture; it
must NOT be repaired by raising r0, by changing the equilibration or
the (c_h, L_h) rule, by reweighting, or by excluding rungs.  A failed
registration is a first-class result and gets reported as such.

THE RATIONAL COMPANION (registered by citation, not recomputed):
CCXXV (zolotarev_phase_filter_probe, SPEC-SHA e8f7e766) certified all
68 steps of the SAME ladder in the RAW form with ONE fixed proper
Zolotarev filter of m0 = 8 conjugate pole pairs (census m = 1..8:
0/0/0/3/53/65/67/68).  Per the program lead's contract text the
POLYNOMIAL form above is the PRIMARY registered object; m0 = 8 is
registered as the RATIONAL COMPANION falsification target on the raw
form, with the same no-tuning clause (a true rung with
tr R_{m0=8}(M_h) >= 1 kills the companion; not repairable).

FROZEN SOURCE-ONLY (c_h, L_h) RULE: with B~ the trailing 7x7 block of
M~ (unit diagonal up to roundoff),
    g_h := 1 - max_i sum_{j != i} |B~_ij|      (Gershgorin floor of
           B~; a THEOREM-level lower bound on lam_1(B~), entry reads
           only, unconditional),
    t_h := c_B / max_i B_ii                    (the CLIII floor c_B =
           0.5523 CITED, transported through the congruence: for
           lam_1(B) >= c_B > 0, x^T E_B B E_B x >= c_B |E_B x|^2 >=
           (c_B / max_i B_ii) |x|^2; raw diagonal entry reads only;
           VALID as a floor only where the premise lam_1(B) >= c_B
           holds -- surface = CLIII certified range, deep = float,
           bridge = the known CCVII premise crack, typed),
    L_h := min(Gershgorin, Frobenius)(M~) * (1 + 2^-40),
    c_h := max of the candidates {g_h, t_h} that lie in (0, L_h);
           no valid candidate => the step is typed CEQ-REFUSED (no
           certificate claimed; sound).
Soundness of the certificate needs NO floor premise (any 0 < c < L
works in (i)-(iii)); the floors power feasibility and are typed per
rung: GERSH-CERT (unconditional entry-level) / TRANSPORT (needs the
cited premise) / FLOAT (measured lam_1(B~), diagnostic only).

FROZEN PROTOCOL (ladder machinery imported READ-ONLY from
onebadmode_moments_probe = CCVII = CCIII/CLXII/CLIV/CXLIV/v900 chain):

 W   LADDER + REPRODUCTION (kill -> PIPELINE-BROKEN / WARD-BROKEN):
     W1 42 surface rungs, chains complete; W2 P2/P3 ledger (min
     lam_min(B_tau) 0.679 rtol 2e-2, gap min/med 0.052/0.888 rtol
     5e-2); W3 deep table overlap 0 + 28 deep zones; W4 28 deep
     truth rungs; W5 deep floor 1.6610 (rtol 2e-2); W6 combined 68 =
     40 surf + 1 bridge + 27 deep; W7 RAW r* REPRODUCTION: the CCVII
     tier-src census recomputed verbatim (c = c_B, L = L_src(M)),
     min/med/max == 14/30/119 EXACT (kill).

 Q   THE CANONICAL FORM (kill -> WARD-BROKEN): Q1 diag(M) > 0 on
     every truth step; Q2 unit diagonal |diag(M~) - 1| <= 1e-13;
     Q3 SYLVESTER ward: the signed eigenvalue census of M~ equals
     that of M on every truth step (zero band 1e-10 relative);
     Q4 block tie: M~[1:,1:] == E_B B E_B to 1e-13; Q5 INTERLACING
     ward lam_2(M~) >= lam_1(B~) - 1e-10 normalized; Q6 FLOOR
     validity wards g_h <= lam_1(B~) + 1e-10 everywhere and t_h <=
     lam_1(B~) + 1e-10 on premise-holding steps, + the floor census
     (GERSH-CERT / TRANSPORT / FLOAT counts per segment, c_h band);
     Q7 L-soundness L_h >= lam_max(M~) on every step + the
     compression census (lam_max(M~) vs lam_max(M), the separator
     condition (L/c)_eq vs (L/c)_raw in dex).

 T   THE EQUILIBRATED ORDER LADDER (typed): per step r*_eq (smallest
     r <= R_MAX with finite tr p_r(M~) < 1), census per segment,
     min/med/max, margins at r*_eq, the h-trend (jackknife OLS of
     r*_eq vs ln h; RSTAR-FLAT / GROWING / AMBIG at bar 0.5 as
     CCVII), the per-step compression ratio r*_raw / r*_eq, the
     r*-law seat kappa on sqrt(lam_max(M~)/c_h), and (A1) the
     ORACLE-TIER diagnostic: r*_orc with c = float lam_1(B~)
     (eigendata, declared diagnostic, the CCVII oracle-tier
     pattern) + the condition-gain census (lam_min/lam_max)_eq vs
     raw in dex -- the split that says WHERE the equilibration
     compression sits and what the source-only floor costs.

 R   THE REGISTRATION (typed, never kill): R1 the frozen clause
     verbatim (rule, no-tuning, falsification criterion); R2 r_need
     + r0 on the 41-step choice set, census at r0 (all 41 must
     certify AT r0; else REGISTRATION-BLOCKED typed), margins at r0;
     R3 the companion m0 = 8 (CCXXV cited); R4 the registered-
     surface hash: SHA-256 over "kz:h:trp_r0(%.12e)" lines of the
     choice set -- the frozen registry future holdouts diff against;
     R5 the registration text printed verbatim (conjecture,
     implication theorem, falsification criterion, honest typing).

 H   THE BLIND DEEP TEST (typed): the 27 deep steps evaluated at r0,
     PASS iff tr p_{r0}(M~) < 1, scored per rung, no refits, no
     exclusions; failures listed individually; the verdict never
     edits the registration.  HONESTY: these deep rungs were
     consumed by CCVII/CCXXV censuses before this probe existed;
     blindness here is with respect to the r0 CHOICE (a function of
     the surface registry only, by the frozen rule), not first-ever
     sight of the rungs -- said plainly, not hidden.

 M   MACHINE WARDS (kill -> WARD-BROKEN): M1 separator facts on
     float grids at the 3 representative equilibrated (c_h, L_h)
     pairs (first/median/last OK step by h), every r in R_SUBSET:
     p_r >= 1 - 1e-9 on 101 points of [-2c, 0]; -1e-12 <= p_r <=
     eps_r (1+1e-9) on 401 points of [c, L]; |p_r(0) - 1| <= 1e-12;
     M2 trace-route tie (stable matrix route == eigensum truth
     reference) rel <= 1e-9 on every OK step, every r in R_SUBSET;
     M3 EXACT-RATIONAL ANCHOR (A3, the CCVII M4b seat): the
     certifying decision tr p_{r*_eq}(M~) < 1 confirmed
     exact-rationally (Fractions on the float-committed entries and
     per-step constants, v897 class) on every step with r*_eq <=
     EXACT_CAP = 64 (kill on any disagreement outside the 1e-9
     borderline band); steps beyond the cap typed FLOAT-ONLY
     (counted, min margin printed); the r0 decision itself is typed
     FLOAT-ONLY when r0 > EXACT_CAP (declared; the anchor class is
     established at r*_eq and the separator soundness facts hold
     for every order).

 D   THE SUPPLY TYPING (typed): D1 tau-screens of the margin
     1 - tr p_{r0} and of the margin at r*_eq (PASS |slope| <= 0.30
     / RELOC >= 0.70 / AMBIG); D2 (A2, the CCVII D-b seat) the
     equilibrated n-read sensitivity dn* = margin(r*_eq) /
     |d tr p_{r*_eq}(M~)/dn| by central finite differences THROUGH
     the frozen construction rule (the raw pivot entry M_00 = n is
     perturbed, E and (c_h, L_h) are rebuilt verbatim; two declared
     relative steps 1e-6/1e-7, the step agreement printed),
     normalized by the raw Schur gap s = n - b^T B^-1 b; med dn*/s
     typed against SUPPLY_GRADE = [0.1, 10] -- the honest typing
     prints that the open content is the same supply class as
     HALFGAP (CCVII DISGUISE-MIXED cited).

 E   CONTROLS (rung-level silence kill -> WARD-BROKEN): E1 smooth
     fires; E2 scramble (seed 1) fires; E3 Epstein x^2+5y^2 fires at
     kz 9 (step-level Epstein O(X^2) DECLARED SKIPPED, predecessor
     pattern); E4 cosh injection A = 0.01 fires; E5 the equilibrated
     certificate on false worlds (relaxed steps): census of tau <= 0
     refusals, diag(M) <= 0 refusals (EQUILIBRATION-REFUSED: itself
     a PD refutation -- a nonpositive diagonal entry certifies
     non-PD; typed, counted), CEQ refusals, eig-indefinite steps,
     RAW certificates at ANY r <= R_MAX (must be 0 on every
     eig-indefinite step; min finite tr p_r >= 1 - 1e-9, overflow
     read as +inf, declared) and certificates at r0; genuinely-PD
     control cores (the known CLXII/CCVII cosh exceptions kz 23/13)
     eig-confirmed and listed, never hidden.

 F   SCREENS + VERDICT assembly.

KILLS: K1 pipeline/counts (W1, W3, W4, W6) -> PIPELINE-BROKEN; K2
reproduction / machine / theorem / control-firing wards (W2, W5, W7,
Q1-Q7, M1-M3, E1-E5 as marked) -> WARD-BROKEN.  R/H/T/D and every
census are typed measurements, never kills.

VERDICT (frozen enum): UNIFORM-ORDER-REGISTERED iff the 41-step
choice set certifies at r0 and all wards hold, with typed sublabels
REG-FROZEN(r0, NEXTPOW2-rule, NO-TUNE), COMPANION(m0 = 8, CCXXV
cited), CENSUS(r*_eq per segment), COMPRESSION(vs raw),
FLOOR(census), BLIND-DEEP(n/27 -- a fail here is typed
BLIND-DEEP-FAIL and reported, never repaired), REGISTRY(sha8),
SUPPLY(...), CONTROLS(...), SCREENS(...); REGISTRATION-BLOCKED iff
some choice-set step does not certify at r0 (or r*_eq > R_MAX);
else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: NDIM = 8; CB_CITED = Fraction(5523, 10000) (CLIII,
cited, printed, not re-proved; certified range = 39 surface steps
h <= 900, own frame, tau units); R_MAX = 400; R_SUBSET = the CCVII
subset {1..24, 32, 48, 64, 96, 128, 160, 200, 256, 320, 400};
EXACT_CAP = 64; RSTAR_RAW_REF = (14, 30, 119) EXACT; L_INFLATE =
1 + 2^-40; DIAG_TOL = 1e-13; INERTIA_RELTOL = 1e-10; ILACE_TOL =
1e-10; FLOOR_TOL = 1e-10; SOUND_TOL = 1e-9; TIE_WARD = 1e-9;
GRID_NEG_TOL = 1e-9; GRID_BULK_TOL = 1e-9; P0_TOL = 1e-12;
BORDER_BAND = 1e-9; RSTAR_BAR = 0.5 per ln h; SLOPE_PASS = 0.30,
SLOPE_RELOC = 0.70; SUPPLY_GRADE = (0.1, 10.0); DN_REL_STEPS =
(1e-6, 1e-7); CTRL_KZ = 9; scramble seed 1; cosh INJ_A = 0.01,
INJ_DELTA = 0.05, INJ_GAMMA0 = 10.0 (CLXII deployed, cited); CMP_M0
= 8 (CCXXV cited); runtime cap declared: 25 min.

EXACTNESS MODEL (frozen): float-level probe on the float64-computed
step matrices; the equilibration diagonal, the floors g_h/t_h and
L_h are ENTRY READS of those float matrices (source-only; float
entries are exact rationals, the round-62 convention); the r0
certificate decisions are anchored exact-rationally on the float
entries and float-committed per-step constants (v897 class); the
separator soundness facts hold for EVERY 0 < c < L, so the anchoring
constants need no enclosure; eigendata of M / M~ appear ONLY in
truth-reference wards, floor diagnostics and control typing, never
in any certificate construction; the deep ladder is FLOAT-LEVEL
(CLIV limit, inherited).  What is NOT enclosed: the float pipeline
producing the entries.  A finite ladder proves nothing at other h.
NO RH claim anywhere.

ANTI-CIRCULARITY (frozen): no zeros, no prime oracles (AST scan;
banned ids zetazero / nzeros / primerange / isprime / primepi /
nextprime / prevprime); v563 READ-ONLY through the CCVII import; RNG
only inside the declared scramble control; stdout only, no artifact;
the equilibration and both floors and both L bounds consume matrix
ENTRIES and the cited c_B only -- never eigendata of the target; r0
is fixed by the frozen surface-only rule before the deep block
enters any choice.

SMOKE-RUN DISCLOSURE (2026-08-12, before freezing; fail-first
history preserved).  SMOKE-1 (SPEC v0, first full passage, 102.2 s,
36/36 GREEN, no kills): ladder reproduced exactly (42 surface
rungs, 28/28 deep, 68 = 40 + 1 + 27; P2/P3 0.6790/0.0520/0.8875;
deep floor 1.6610; W7 raw r* census 14/30/119 EXACT); all Q wards
green (unit diagonal, Sylvester census tie 68/68, block tie,
interlacing, floor validity, L-soundness).  THE CENSORING-FREE
HEADLINE, AND IT CONTRADICTS THE A-PRIORI EXPECTATION: with the
frozen source-only (c_h, L_h) rule the equilibrated order does NOT
compress -- GERSH-CERT 0/68 (the Gershgorin floor of B~ is negative
on every step), so c_h fell to the transported floor t_h =
c_B/max_i B_ii ~ 2.3e-5..2.3e-2 everywhere, and r*_eq = 11/39/230
(surf max 230 at kz 16 h 434, bridge 11, deep max 98), compression
ratio r*_raw/r*_eq 0.26/0.82/3.45, RSTAR-AMBIG (slope -2.640 +/-
2SE 6.845, R2 0.006), kappa 0.476 on sqrt(lam_max(M~)/c_h) (R2
0.869): THE RAW DIAGONAL-SCALE SPREAD RELOCATES INTO THE FLOOR
KNOWLEDGE INSTEAD OF DISAPPEARING.  Registration by the frozen
rule: r_need = 230, r0 = 256, choice set 41/41 AT r0, margins at r0
dex -1.899/-0.000/-0.000, registry sha256 09c14c8f...; blind deep
27/27 PASS at r0 (margins dex -0.037/-0.000/-0.000).  Machine: M1
grids 0-defect, M2 tie 1.73e-13; controls fire 4/4 (smooth 42,
scramble 42, Epstein 55, cosh 39 rungs), E5: smooth 32 steps all
tau-refused, scramble 21 all tau-refused, cosh 36 tau-refused + 1
eig-indefinite with 0 RAW certs (min finite indefinite trace
2.656), the two genuinely-PD cosh cores kz 23/13 certify (eig
lam_min +0.530/+1.041, eig-confirmed, CLXII/CCVII exception class,
sound); margin screens PASS(-0.008)/PASS(+0.009).  The smoke D-b
(dn* at r0) returned med dn*/s 8.8e4 with fd step agreement only
1.2e-4 -- at r0 = 256 the trace is suppressed to ~1e-30 and the
finite difference is float-noise-dominated: a vacuous measurement,
disclosed, and the reason for A2 below.
PRE-FREEZE FLOOR DIAGNOSTIC (disclosed; temporary side script,
deleted after use): on the same 68-step ladder the Frobenius floor
1 - ||offdiag(B~)||_F is ALSO negative on 68/68 (-3.75..-2.29) --
NO entry-level floor of the equilibrated co-block exists, so the
frozen c-rule was left UNCHANGED (nothing to add); the float
lam_1(B~) is 0.0094..0.101, lam_min(M~) 8.77e-3..0.100, lam_max(M~)
4.07..5.52, and the ORACLE tier (c = float lam_1(B~), eigendata)
gives r*_orc = 5/9/18 with condition gain (lam_min/lam_max)_eq vs
raw dex +0.30/+1.01/+1.57: the equilibration compression IS real
(the lead's expectation holds SPECTRALLY) but on this ladder only
eigendata can harvest it -- the source-only price is exactly the
floor knowledge.
AMENDMENTS (disclosed, applied before the freeze; the smoke-1
numbers above are ON RECORD, nothing hidden):
  * A1 (measurement added): the ORACLE-TIER diagnostic r*_orc and
    the condition-gain census are added to T -- they quantify the
    a-priori compression expectation and its source-only blocker.
  * A2 (seat of dn*): the n-read sensitivity is evaluated at r*_eq
    (the CCVII D-b seat, where the margin is O(1) and the finite
    difference is resolved) instead of at the padded r0, where the
    smoke showed it float-noise-vacuous; the r0 margin screen is
    unchanged.
  * A3 (anchor seat / cost): the exact-rational confirmation is
    anchored at r*_eq <= EXACT_CAP = 64 per step (the CCVII M4b
    pattern verbatim; the dyadic moment cost at 2 r0 = 512 would
    explode) and the r0 = 256 decision is typed FLOAT-ONLY,
    declared.
No success bar, ward tolerance, control, screen band, floor rule,
(c_h, L_h) rule, registration clause, r0 rule or enum RULE was
changed beyond the three disclosed amendments.
SMOKE-2 (post-A1/A2/A3, 134.4 s): 36/36 GREEN; every smoke-1
measurement reproduced identically (r*_eq 11/39/230, r_need 230 at
kz 16 h 434, r0 = 256, choice 41/41, registry sha 09c14c8f, blind
deep 27/27, controls, M1 0-defect, M2 1.73e-13); the amended
measurements: ORACLE-DIAG r*_orc 5/9/18, condition gain dex
+0.296/+1.006/+1.565, source-only floor price r*eq/r*orc
1.0/4.1/17.7; the equilibrated separator condition is itself WORSE
than raw ((L/c)_eq vs (L/c)_raw dex +0.191/+0.334/+0.547 -- the
floor collapsed more than L); exact anchor 57 agree + 11 FLOAT-ONLY
beyond cap (min margin 9.6e-3) + 0 disagree; D2 at r*_eq: dn*/s dex
-1.991/-0.248/+1.457 med 0.565 HALFGAP-GRADE (fd agreement 3.6e-4),
dn* screen PASS(-0.032) -- the equilibrated certificate consumes
the SAME n-read supply class as HALFGAP, exactly the honest typing
frozen in the spec (raw-form CCVII was 0.354).  The frozen run
below changes only this disclosure block and the SPEC SHA.

SPEC v1 (2026-08-12, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
ladder, frames, deep extension, controls, separator + exact-tier
machinery imported READ-ONLY from onebadmode_moments_probe;
(ii) steps sorted by (h, kz); representative steps = OK-step indices
(0, n//2, n-1) by h; (iii) r*_of(table) = first r with finite
value < 1; nextpow2-strict(x) = 1 << (bit_length(x)); (iv) OLS +
leave-one-out jackknife and the screen bands as CCVII; (v) the
registry hash over "%d:%d:%.12e" % (kz2, h2, trp_r0) lines joined by
newlines, choice set in (h, kz) order.

NO RH claim: the registration is a falsifiability device; the
implication chain is elementary and the entire open content is the
uniform arithmetic trace inequality on the equilibrated ladder --
same supply class as HALFGAP, cited, no independence claim;
certification on finitely many float64 rungs proves nothing about
other h, the ideal objects, or any tail statement.  No marker moves.

Sources (read-only): onebadmode_moments_probe (CCVII; ladder + frame
+ separator + exact tier machinery, verbatim import); Jacobi
equilibration = the declared CLXXIII canonical scaling
(ub4_congruence_upgrade_probe); B-floor constant CITED from
pg_chain_interval_rollout_probe (CLIII); deep floor CITED from
deep_blind_holdout_probe (CLIV); the registration pattern from
halfgap_registration_probe (HALFGAP); the rational companion CITED
from zolotarev_phase_filter_probe (CCXXV).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/uniform_order_registration_probe.py
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
sys.path.insert(0, _HERE)

import onebadmode_moments_probe as ob  # noqa: E402  (READ-ONLY CCVII)

NDIM = 8
CB_CITED = Fraction(5523, 10000)
CB_F = float(CB_CITED)
R_MAX = 400
R_SUBSET = ob.R_SUBSET
EXACT_CAP = 64
RSTAR_RAW_REF = (14, 30, 119)
DIAG_TOL = 1e-13
INERTIA_RELTOL = 1e-10
ILACE_TOL = 1e-10
FLOOR_TOL = 1e-10
SOUND_TOL = 1e-9
TIE_WARD = 1e-9
GRID_NEG_TOL = 1e-9
GRID_BULK_TOL = 1e-9
P0_TOL = 1e-12
BORDER_BAND = 1e-9
RSTAR_BAR = 0.5
SUPPLY_GRADE = (0.1, 10.0)
DN_REL_STEPS = (1e-6, 1e-7)
CTRL_KZ = 9
SCR_SEED = 1
CMP_M0 = 8
ZOLO_SHA8 = "e8f7e766"
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


def nextpow2_strict(x):
    """Smallest power of two STRICTLY greater than x (frozen rule)."""
    return 1 << int(x).bit_length()


def rstar_of(tab):
    if tab is None:
        return None
    for r in range(1, R_MAX + 1):
        if np.isfinite(tab[r]) and tab[r] < 1.0:
            return r
    return None


def equilibrate(Mt):
    """The canonical CLXXIII Jacobi congruence M~ = E M E,
    E = diag(M_ii^{-1/2}) from the FLOAT diagonal (entry reads
    only).  None iff min diag <= 0."""
    dg = np.diag(Mt).copy()
    if float(np.min(dg)) <= 0.0:
        return None, None
    e = 1.0 / np.sqrt(dg)
    return ob.sym(e[:, None] * Mt * e[None, :]), e


def source_constants(Meq, Braw_diag_max, lamB1_raw):
    """The frozen source-only (c_h, L_h) rule on the equilibrated
    matrix.  Returns dict with g, t, c, L, seat or None (CEQ-REFUSED).
    Floor-certificate seat: GERSH (unconditional) beats TRANSPORT
    beats nothing; the seat records which candidate WON c_h and
    whether the transported premise holds (typed elsewhere)."""
    Beq = Meq[1:, 1:]
    off = np.abs(Beq) - np.diag(np.diag(np.abs(Beq)))
    g = 1.0 - float(np.max(np.sum(off, axis=1)))
    t = CB_F / Braw_diag_max
    L = min(ob.gersh_bound(Meq), ob.fro_bound(Meq)) * ob.L_INFLATE
    cands = [(v, s) for v, s in ((g, "GERSH"), (t, "TRANSPORT"))
             if 0.0 < v < L]
    if not cands:
        return None
    c, seat = max(cands)
    return dict(g=g, t=t, c=c, L=L, seat=seat,
                premise=bool(lamB1_raw >= CB_F))


def assemble(st):
    """Raw tau-unit assembly (CCVII verbatim fields) + the canonical
    equilibration + the frozen source-only constants."""
    tau = st["tau"]
    if tau <= 0.0:
        st["status"] = "REFUSED-TAU"
        return st
    Mt = ob.sym(st["Q"].T @ (st["r2"]["S"] / tau) @ st["Q"])
    st["Mt"] = Mt
    nn, b, B = ob.split_parts(Mt)
    st["n0"], st["bvec"], st["Bblk"] = nn, b, B
    st["lamB1"] = float(np.linalg.eigvalsh(B)[0])
    try:
        st["gap"] = nn - float(b @ np.linalg.solve(B, b))
    except np.linalg.LinAlgError:
        st["gap"] = float("nan")
    st["eigs"] = np.linalg.eigvalsh(Mt)          # truth reference
    st["L_raw"] = min(ob.gersh_bound(Mt),
                      ob.fro_bound(Mt)) * ob.L_INFLATE
    if st["L_raw"] <= CB_F * (1.0 + 1e-6):
        st["status"] = "REFUSED-L"
        return st
    Meq, e = equilibrate(Mt)
    if Meq is None:
        st["status"] = "REFUSED-DIAG"
        return st
    st["Meq"], st["Evec"] = Meq, e
    st["eigs_eq"] = np.linalg.eigvalsh(Meq)      # truth reference
    st["lamB1_eq"] = float(np.linalg.eigvalsh(Meq[1:, 1:])[0])
    sc = source_constants(Meq, float(np.max(np.diag(B))),
                          st["lamB1"])
    if sc is None:
        st["status"] = "REFUSED-CEQ"
        return st
    st.update(g_eq=sc["g"], t_eq=sc["t"], c_eq=sc["c"],
              L_eq=sc["L"], c_seat=sc["seat"],
              premise=sc["premise"])
    st["status"] = "OK"
    return st


def eq_trace_at(Mt_raw, r):
    """tr p_r(M~) through the FROZEN construction rule applied
    verbatim to a raw tau-unit matrix (used by the dn* finite
    difference).  None on any refusal."""
    Meq, _e = equilibrate(Mt_raw)
    if Meq is None:
        return None
    _nn, _b, B = ob.split_parts(Mt_raw)
    lamB1 = float(np.linalg.eigvalsh(B)[0])
    sc = source_constants(Meq, float(np.max(np.diag(B))), lamB1)
    if sc is None:
        return None
    with np.errstate(over="ignore", invalid="ignore"):
        tab, _ = ob.sep_traces(Meq, sc["c"], sc["L"], r)
    return tab[r] if np.isfinite(tab[r]) else None


def signed_census(eigs, reltol):
    scale = max(1.0, float(np.max(np.abs(eigs))))
    neg = int(np.sum(eigs < -reltol * scale))
    pos = int(np.sum(eigs > reltol * scale))
    return neg, pos


def fmt3(v, fmt="%+.3f"):
    v = np.asarray(v, float)
    return "/".join(fmt % x for x in (float(np.min(v)),
                                      float(np.median(v)),
                                      float(np.max(v))))


def build_truth_ladder():
    section("W -- CCVII ladder reproduction (read-only machinery) + "
            "the RAW r* census")
    zones = ob.ladder_zones()
    ok = check("W1 surface rung census %d == %d"
               % (len(zones), ob.N_RUNGS_EXP),
               len(zones) == ob.N_RUNGS_EXP, kill="K1")
    surface = [ob.build_rung("surf", kz, with_split=False)
               for kz in zones]
    check("W1b all surface chains complete",
          all(r is not None for r in surface), kill="K1")
    if KILLS:
        return zones, []
    surface_h = sorted(surface, key=lambda r: (r["h"], r["kz"]))
    steps_s = ob.make_steps(surface_h)
    for st in steps_s:
        assemble(st)
    ok_s = [st for st in steps_s if st["status"] == "OK"]
    minB = min(st["lamB1"] for st in ok_s)
    gaps = np.asarray([st["gap"] for st in ok_s])
    check("W2 P2/P3 reproduction: minB %.4f == %.3f; gap min/med "
          "%.4f/%.4f == %.3f/%.3f"
          % (minB, ob.MINB_REF, float(np.min(gaps)),
             float(np.median(gaps)), ob.GAPMIN_REF, ob.GAPMED_REF),
          (abs(minB / ob.MINB_REF - 1.0) <= ob.MINB_RTOL
           and abs(float(np.min(gaps)) / ob.GAPMIN_REF - 1.0)
           <= ob.GAP_RTOL
           and abs(float(np.median(gaps)) / ob.GAPMED_REF - 1.0)
           <= ob.GAP_RTOL), kill="K2")
    lam_ext = ob.build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:ob.core.ATOM_MAX + 1]
                              - ob.core.LAM_TAB)))
    dz = ob.deep_zone_census()
    check("W3 deep table overlap %.1e == 0; deep census %d == %d"
          % (dev, len(dz), ob.N_DEEP_EXP),
          dev == 0.0 and len(dz) == ob.N_DEEP_EXP, kill="K1")
    if KILLS:
        return zones, []
    deep = []
    for kz, hz in sorted(dz, key=lambda p: (p[1], p[0])):
        if time.time() - T0 > ob.SOFT_BUDGET_S:
            break
        r = ob.build_rung("deep", kz, with_split=False)
        if r is not None:
            deep.append(r)
        print("    deep kz %-4d h %-5d %s  [%.0f s]"
              % (kz, hz, "OK" if r is not None else "SHORT",
                 time.time() - T0), flush=True)
    deep_ok = [r for r in deep if r["core_ok"] and r["negA"] == 0
               and r.get("lamS", -1.0) > 0.0]
    check("W4 deep truth rungs %d == %d" % (len(deep_ok),
                                            ob.N_DEEP_EXP),
          len(deep_ok) == ob.N_DEEP_EXP, kill="K1")
    if KILLS:
        return zones, []
    deep_h = sorted(deep_ok, key=lambda r: (r["h"], r["kz"]))
    steps_d = ob.make_steps(deep_h)
    for st in steps_d:
        assemble(st)
    ok_d = [st for st in steps_d if st["status"] == "OK"]
    minB_d = min(st["lamB1"] for st in ok_d)
    check("W5 CLIV deep own-frame floor %.4f == %.4f (rtol %g)"
          % (minB_d, ob.DEEP_MINB_REF, ob.DEEP_MINB_RTOL),
          abs(minB_d / ob.DEEP_MINB_REF - 1.0) <= ob.DEEP_MINB_RTOL,
          kill="K2")
    comb = sorted([r for r in surface_h if r["core_ok"]] + deep_h,
                  key=lambda r: (r["h"], r["kz"]))
    steps_c = ob.make_steps(comb)
    for st in steps_c:
        assemble(st)
    ok_c = [st for st in steps_c if st["status"] == "OK"]
    segs = [ob.seg_of(st) for st in ok_c]
    check("W6 combined ladder 68 = surf %d + bridge %d + deep %d"
          % (segs.count("surf"), segs.count("bridge"),
             segs.count("deep")),
          (len(ok_c) == 68 and segs.count("surf") == 40
           and segs.count("bridge") == 1
           and segs.count("deep") == 27), kill="K1")
    if KILLS:
        return zones, []
    # W7 the raw CCVII tier-src census, recomputed verbatim
    for st in ok_c:
        with np.errstate(over="ignore", invalid="ignore"):
            st["trp_raw"], _ = ob.sep_traces(st["Mt"], CB_F,
                                             st["L_raw"], R_MAX)
        st["rstar_raw"] = rstar_of(st["trp_raw"])
    raw = [st["rstar_raw"] for st in ok_c]
    ok_raw = all(r is not None for r in raw)
    trio = ((int(min(raw)), int(np.median(raw)), int(max(raw)))
            if ok_raw else (-1, -1, -1))
    check("W7 RAW r* reproduction (CCVII tier-src): min/med/max "
          "%d/%d/%d == %d/%d/%d EXACT"
          % (trio + RSTAR_RAW_REF),
          ok_raw and trio == RSTAR_RAW_REF, kill="K2")
    return zones, ok_c


def main():
    section("PRIME.ONEBADMODE.UNIFORM.ORDER.01 -- REGISTRATION of "
            "the uniform-order conjecture on the Jacobi-equilibrated "
            "wall (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.  c_B = %.4f CITED "
          "(CLIII certified surface; CLIV deep float; CCVII bridge "
          "crack typed).  Float-level probe; r0 decisions anchored "
          "exact-rationally (v897 class)." % CB_F)
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    zones, ok_c = build_truth_ladder()
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ Q
    section("Q -- the canonical form: equilibration wards + floors "
            "+ compression")
    n_diag = sum(1 for st in ok_c if "Meq" in st)
    check("Q1 WARD diag(M) > 0 on every truth step (%d/%d)"
          % (n_diag, len(ok_c)), n_diag == len(ok_c), kill="K2")
    ud = max(float(np.max(np.abs(np.diag(st["Meq"]) - 1.0)))
             for st in ok_c)
    check("Q2 WARD unit diagonal |diag(M~)-1| max %.2e <= %.0e"
          % (ud, DIAG_TOL), ud <= DIAG_TOL, kill="K2")
    n_syl = sum(1 for st in ok_c
                if signed_census(st["eigs"], INERTIA_RELTOL)
                == signed_census(st["eigs_eq"], INERTIA_RELTOL))
    check("Q3 WARD Sylvester: signed eig census(M~) == census(M) on "
          "%d/%d steps" % (n_syl, len(ok_c)),
          n_syl == len(ok_c), kill="K2")
    bt = 0.0
    for st in ok_c:
        eB = st["Evec"][1:]
        bt = max(bt, float(np.max(np.abs(
            st["Meq"][1:, 1:]
            - eB[:, None] * st["Bblk"] * eB[None, :]))))
    check("Q4 WARD block tie M~[1:,1:] == E_B B E_B max %.2e <= "
          "%.0e" % (bt, DIAG_TOL), bt <= DIAG_TOL, kill="K2")
    il = min((float(st["eigs_eq"][1]) - st["lamB1_eq"])
             / max(1.0, abs(st["lamB1_eq"])) for st in ok_c)
    check("Q5 WARD interlacing lam_2(M~) >= lam_1(B~) (worst "
          "normalized %+.2e >= -%.0e)" % (il, ILACE_TOL),
          il >= -ILACE_TOL, kill="K2")
    g_ok = min(st["lamB1_eq"] - st["g_eq"] for st in ok_c)
    prem = [st for st in ok_c if st["premise"]]
    t_ok = min(st["lamB1_eq"] - st["t_eq"] for st in prem)
    check("Q6 WARD floor validity: lam1(B~) - g worst %+.2e >= "
          "-%.0e (all %d); lam1(B~) - t worst %+.2e >= -%.0e on %d "
          "premise steps" % (g_ok, FLOOR_TOL, len(ok_c), t_ok,
                             FLOOR_TOL, len(prem)),
          g_ok >= -FLOOR_TOL and t_ok >= -FLOOR_TOL, kill="K2")
    n_gc = sum(1 for st in ok_c if st["g_eq"] > 0)
    n_gwin = sum(1 for st in ok_c if st["c_seat"] == "GERSH")
    print("    floor census: Gershgorin floor of B~ POSITIVE on "
          "%d/%d (unconditional entry-level certificate); GERSH "
          "wins c_h on %d/%d, TRANSPORT on %d; premise lam1(B) >= "
          "c_B holds on %d/%d (bridge crack: %d)"
          % (n_gc, len(ok_c), n_gwin, len(ok_c),
             len(ok_c) - n_gwin, len(prem), len(ok_c),
             sum(1 for st in ok_c if not st["premise"])))
    print("    c_h band %s   float lam_1(B~) band %s"
          % (fmt3([st["c_eq"] for st in ok_c], "%.4f"),
             fmt3([st["lamB1_eq"] for st in ok_c], "%.4f")))
    check("Q6b typed: FLOOR(GERSH-CERT %d/%d, TRANSPORT-win %d, "
          "premise %d/%d)" % (n_gc, len(ok_c), len(ok_c) - n_gwin,
                              len(prem), len(ok_c)), True)
    l_ok = sum(1 for st in ok_c
               if st["L_eq"] >= float(st["eigs_eq"][-1]))
    check("Q7 WARD L-soundness L_h >= lam_max(M~) on %d/%d"
          % (l_ok, len(ok_c)), l_ok == len(ok_c), kill="K2")
    lmx = [float(st["eigs_eq"][-1]) for st in ok_c]
    cond_dex = [math.log10((st["L_eq"] / st["c_eq"])
                           / (st["L_raw"] / CB_F)) for st in ok_c]
    print("    compression: lam_max(M~) band %s (raw %s); "
          "(L/c)_eq vs (L/c)_raw dex %s; L_h band %s"
          % (fmt3(lmx, "%.3f"),
             fmt3([float(st["eigs"][-1]) for st in ok_c], "%.3g"),
             fmt3(cond_dex), fmt3([st["L_eq"] for st in ok_c],
                                  "%.3f")))
    check("Q7b typed: COMPRESSION((L/c) dex %s)" % fmt3(cond_dex),
          True)

    # ------------------------------------------------------------ T
    section("T -- the equilibrated order ladder (+ the oracle-tier "
            "diagnostic, A1)")
    for st in ok_c:
        with np.errstate(over="ignore", invalid="ignore"):
            st["trp_eq"], st["t0_eq"] = ob.sep_traces(
                st["Meq"], st["c_eq"], st["L_eq"], R_MAX)
        st["rstar_eq"] = rstar_of(st["trp_eq"])
        c_orc = st["lamB1_eq"]        # eigendata, DIAGNOSTIC only
        if 0.0 < c_orc < st["L_eq"]:
            with np.errstate(over="ignore", invalid="ignore"):
                tab_o, _ = ob.sep_traces(st["Meq"], c_orc,
                                         st["L_eq"], R_MAX)
            st["rstar_orc"] = rstar_of(tab_o)
        else:
            st["rstar_orc"] = None
    print("    seg    h1->h2      c_h     L_h    r*eq r*raw r*orc "
          "ratio  trp(r*eq)  margin(dex)")
    for st in ok_c:
        r = st["rstar_eq"]
        mg = (1.0 - st["trp_eq"][r]) if r is not None else None
        st["margin_eq"] = mg
        print("    %-6s %4d->%-4d %7.4f %6.3f  %-4s %-5s %-5s %-5s "
              "%9s %10s"
              % (ob.seg_of(st), st["r1"]["h"], st["r2"]["h"],
                 st["c_eq"], st["L_eq"],
                 r if r is not None else ">%d" % R_MAX,
                 st["rstar_raw"],
                 st["rstar_orc"] if st["rstar_orc"] is not None
                 else "-",
                 ("%.2f" % (st["rstar_raw"] / r)) if r else "-",
                 "%.4f" % st["trp_eq"][r] if r is not None
                 else "n/a",
                 "%+.3f" % math.log10(mg) if mg and mg > 0
                 else "n/a"), flush=True)
    cert = [st for st in ok_c if st["rstar_eq"] is not None]
    uncert = [st for st in ok_c if st["rstar_eq"] is None]
    cen = {}
    for sg in ("surf", "bridge", "deep"):
        sub = [st for st in ok_c if ob.seg_of(st) == sg]
        rr = [st["rstar_eq"] for st in sub
              if st["rstar_eq"] is not None]
        cen[sg] = (len(rr), len(sub), max(rr) if rr else -1)
    rst = np.array([st["rstar_eq"] for st in cert], float)
    t_cen = ("CENSUS(surf %d/%d max %d, bridge %d/%d max %d, deep "
             "%d/%d max %d; r*eq min/med/max %d/%d/%d)"
             % (cen["surf"] + cen["bridge"] + cen["deep"]
                + (int(rst.min()), int(np.median(rst)),
                   int(rst.max()))))
    print("    " + t_cen)
    if uncert:
        print("    UNCERTIFIED (r*eq > %d): %s" % (R_MAX, ", ".join(
            "h %d (%s)" % (st["r2"]["h"], ob.seg_of(st))
            for st in uncert)))
    ratio = [st["rstar_raw"] / st["rstar_eq"] for st in cert]
    t_cmp = ("COMPRESSION-RSTAR(r*raw/r*eq %s; raw census "
             "%d/%d/%d cited == recomputed)"
             % ((fmt3(ratio, "%.2f"),) + RSTAR_RAW_REF))
    print("    " + t_cmp)
    sl, se, r2t = ob.jack_slope(
        [math.log(st["r2"]["h"]) for st in cert], rst)
    rlab = ("RSTAR-GROWING" if sl - 2 * se > RSTAR_BAR
            else "RSTAR-FLAT" if sl + 2 * se < RSTAR_BAR
            else "RSTAR-AMBIG")
    t_h = ("RSTAR(%s: slope %+.3f +/- 2SE %.3f per ln h, R2 %.3f, "
           "bar %.2f)" % (rlab, sl, 2 * se, r2t, RSTAR_BAR))
    print("    " + t_h)
    sq = np.array([math.sqrt(float(st["eigs_eq"][-1]) / st["c_eq"])
                   for st in cert])
    kap = float(np.sum(sq * rst) / np.sum(sq * sq))
    _a, sl_sq, r2_sq = ob.ols_line(sq, rst)
    t_law = ("RSTAR-LAW(kappa %.3f on sqrt(lam_max(M~)/c_h), OLS "
             "slope %.3f R2 %.3f)" % (kap, sl_sq, r2_sq))
    print("    " + t_law)
    # A1: the oracle tier (eigendata, diagnostic) + condition gain
    orcs = [st["rstar_orc"] for st in ok_c
            if st["rstar_orc"] is not None]
    gain_dex = [math.log10(
        (float(st["eigs_eq"][0]) / float(st["eigs_eq"][-1]))
        / (float(st["eigs"][0]) / float(st["eigs"][-1])))
        for st in ok_c]
    price = [st["rstar_eq"] / st["rstar_orc"] for st in ok_c
             if st["rstar_eq"] is not None
             and st["rstar_orc"] is not None]
    t_orc = ("ORACLE-DIAG(r*orc min/med/max %d/%d/%d [c = float "
             "lam1(B~), eigendata, diagnostic]; condition gain "
             "(lam_min/lam_max)_eq vs raw dex %s; source-only "
             "floor price r*eq/r*orc %s)"
             % (int(min(orcs)), int(np.median(orcs)),
                int(max(orcs)), fmt3(gain_dex),
                fmt3(price, "%.1f")))
    print("    " + t_orc)
    check("T typed: %s + %s + %s + %s + %s"
          % (t_cen, t_cmp, t_h, t_law, t_orc), True)

    # ------------------------------------------------------------ R
    section("R -- the registration (frozen clause, r0, companion, "
            "registry)")
    choice = [st for st in ok_c if ob.seg_of(st) != "deep"]
    blind = [st for st in ok_c if ob.seg_of(st) == "deep"]
    print("    R1 THE FROZEN CLAUSE (verbatim, part of the "
          "registered object):")
    print("       r_need := max over the %d SURFACE + BRIDGE steps "
          "of r*_eq; r0 := smallest power of two" % len(choice))
    print("       STRICTLY greater than r_need (declared safety "
          "factor).  r0 is chosen on the surface subset")
    print("       ONLY.  NO-TUNING: a later miss on ANY rung is a "
          "FAIL of the registered conjecture, full stop;")
    print("       not repairable by raising r0, changing the "
          "equilibration or the (c_h, L_h) rule, by")
    print("       reweighting, or by excluding rungs.  "
          "FALSIFICATION: one true rung with tr p_r0(M~) >= 1")
    print("       kills it.")
    check("R1 typed: REG-FROZEN(NEXTPOW2-strict rule, NO-TUNE, "
          "surface-only choice)", True)
    ch_rs = [st["rstar_eq"] for st in choice]
    if any(r is None for r in ch_rs):
        n_bad = sum(1 for r in ch_rs if r is None)
        check("R2 typed: REGISTRATION-BLOCKED(%d choice steps "
              "uncertified at R_MAX %d)" % (n_bad, R_MAX), True)
        return finish(dict(head="REGISTRATION-BLOCKED(UNCERT %d)"
                           % n_bad))
    r_need = max(ch_rs)
    r0 = nextpow2_strict(r_need)
    tight = max(choice, key=lambda st: st["rstar_eq"])
    for st in ok_c:
        st["trp_r0"] = st["trp_eq"][r0] if r0 <= R_MAX \
            else float("inf")
        st["margin_r0"] = 1.0 - st["trp_r0"]
    n_ch = sum(1 for st in choice
               if np.isfinite(st["trp_r0"]) and st["trp_r0"] < 1.0)
    ch_mrg = [math.log10(st["margin_r0"]) for st in choice
              if st["margin_r0"] > 0]
    print("    R2 r_need = %d (tightest choice step kz %d h %d), "
          "r0 = %d; choice set %d/%d certify AT r0; margins at r0 "
          "dex %s"
          % (r_need, tight["r2"]["kz"], tight["r2"]["h"], r0,
             n_ch, len(choice), fmt3(ch_mrg)))
    reg_ok = n_ch == len(choice)
    check("R2 typed: %s"
          % ("REG-SET-PASS(%d/%d at r0 = %d)"
             % (n_ch, len(choice), r0) if reg_ok
             else "REGISTRATION-BLOCKED(%d/%d at r0 = %d)"
             % (n_ch, len(choice), r0)), True)
    print("    R3 THE RATIONAL COMPANION (cited, not recomputed): "
          "m0 = %d fixed proper Zolotarev pole pairs" % CMP_M0)
    print("       certify 68/68 on the RAW form (CCXXV, SPEC-SHA "
          "%s..., census m=1..8: 0/0/0/3/53/65/67/68);" % ZOLO_SHA8)
    print("       registered as the COMPANION falsification target "
          "with the same no-tuning clause; the")
    print("       polynomial form above is PRIMARY per the lead's "
          "contract text.")
    check("R3 typed: COMPANION(m0 = %d, CCXXV cited)" % CMP_M0,
          True)
    reg_lines = "\n".join("%d:%d:%.12e" % (st["r2"]["kz"],
                                           st["r2"]["h"],
                                           st["trp_r0"])
                          for st in choice)
    reg_sha = hashlib.sha256(reg_lines.encode("utf-8")).hexdigest()
    print("    R4 registered-surface sha256 = %s (%d lines)"
          % (reg_sha, len(choice)))
    check("R4 typed: registry frozen (sha8 %s)" % reg_sha[:8], True)
    print("    R5 THE REGISTRATION TEXT (verbatim, frozen):")
    print("       CONJECTURE (UNIFORM-ORDER): EXISTS r0 < oo s.t. "
          "FOR ALL h: tr p_r0(M~_h) < 1, with")
    print("       M~_h = E_h M_h E_h, E_h = diag((M_h)_ii^{-1/2}) "
          "the canonical CLXXIII Jacobi equilibration")
    print("       and p the frozen separator family with the "
          "source-only per-rung (c_h, L_h) rule; r0 = %d" % r0)
    print("       FROZEN by the surface-only rule above.  "
          "IMPLICATION (elementary): separator facts (p >= 0")
    print("       everywhere, p >= 1 on x <= 0) + trace bound => "
          "n_+(M~) full => M~ > 0 => (Sylvester, E")
    print("       invertible) M > 0 => the wall at h; interlacing "
          "+ the B~-floor power FEASIBILITY only.")
    print("       FALSIFICATION: one true rung with tr p_r0(M~) >= "
          "1 kills it.  HONEST TYPING: the open")
    print("       content is EXACTLY the uniform arithmetic trace "
          "inequality -- same supply class as")
    print("       HALFGAP (CCVII DISGUISE-MIXED, dn*/s med 0.354 "
          "cited); NO independence claim.")
    check("R5 typed: REGISTRATION-TEXT-FROZEN", True)

    # ------------------------------------------------------------ H
    section("H -- the blind deep test at r0 (CLIV holdout style)")
    print("    protocol: the %d deep steps evaluated at r0 = %d "
          "with THIS pipeline verbatim; PASS iff" % (len(blind), r0))
    print("    tr p_r0(M~) < 1, scored per rung; no refits, no "
          "exclusions; fails listed individually;")
    print("    the verdict never edits the registration.  HONESTY: "
          "these deep rungs were consumed by")
    print("    CCVII/CCXXV censuses before this probe; blindness is "
          "w.r.t. the r0 CHOICE (surface-only")
    print("    frozen rule), not first-ever sight of the rungs.")
    n_bl = 0
    bl_mrg = []
    for st in blind:
        pas = np.isfinite(st["trp_r0"]) and st["trp_r0"] < 1.0
        if pas:
            n_bl += 1
            if st["margin_r0"] > 0:
                bl_mrg.append(math.log10(st["margin_r0"]))
        else:
            print("    H FAIL kz %d h %d: tr p_r0 = %.6f >= 1"
                  % (st["r2"]["kz"], st["r2"]["h"], st["trp_r0"]))
    blab = ("BLIND-DEEP-PASS(%d/%d, margins dex %s)"
            % (n_bl, len(blind), fmt3(bl_mrg))
            if n_bl == len(blind)
            else "BLIND-DEEP-FAIL(%d/%d) -- FIRST-CLASS RESULT"
            % (len(blind) - n_bl, len(blind)))
    print("    " + blab)
    check("H typed: %s" % blab, True)

    # ------------------------------------------------------------ M
    section("M -- machine wards (grids, route tie, exact-rational "
            "anchor at r0)")
    rep_idx = (0, len(ok_c) // 2, len(ok_c) - 1)
    worst_neg, worst_bulk, worst_p0 = 0.0, 0.0, 0.0
    for i in rep_idx:
        st = ok_c[i]
        c, L = st["c_eq"], st["L_eq"]
        m0 = -(L + c) / (L - c)
        t0lad = ob.cheb_scalar_ladder(m0, R_MAX)
        xs_neg = np.linspace(-2.0 * c, 0.0, 101)
        xs_blk = np.linspace(c, L, 401)
        for r in R_SUBSET:
            eps_r = 1.0 / t0lad[r] ** 2
            pn = np.array([ob.sep_scalar(x, c, L, r, t0lad)
                           for x in xs_neg])
            pb = np.array([ob.sep_scalar(x, c, L, r, t0lad)
                           for x in xs_blk])
            worst_neg = max(worst_neg, float(np.max(1.0 - pn)))
            worst_bulk = max(
                worst_bulk,
                float(np.max(pb - eps_r * (1.0 + GRID_BULK_TOL))),
                float(np.max(-pb)))
            worst_p0 = max(worst_p0,
                           abs(ob.sep_scalar(0.0, c, L, r, t0lad)
                               - 1.0))
    check("M1 WARD separator facts on grids (3 rep equilibrated "
          "pairs, R_SUBSET): neg-side 1-p max %.2e <= %.0e; bulk "
          "excess max %.2e <= 0; |p(0)-1| max %.2e <= %.0e"
          % (worst_neg, GRID_NEG_TOL, worst_bulk, worst_p0, P0_TOL),
          worst_neg <= GRID_NEG_TOL and worst_bulk <= 0.0
          and worst_p0 <= P0_TOL, kill="K2")
    tie_max = 0.0
    for st in ok_c:
        t0lad = st["t0_eq"]
        for r in R_SUBSET:
            te = sum(ob.sep_scalar(float(x), st["c_eq"],
                                   st["L_eq"], r, t0lad)
                     for x in st["eigs_eq"])
            tie_max = max(tie_max, abs(st["trp_eq"][r] - te)
                          / max(abs(te), 1.0))
    check("M2 WARD trace-route tie (stable == eig-sum) max rel "
          "%.2e <= %.0e on %d steps x %d orders"
          % (tie_max, TIE_WARD, len(ok_c), len(R_SUBSET)),
          tie_max <= TIE_WARD, kill="K2")
    # A3: exact-rational anchor at r*_eq (CCVII M4b pattern); the
    # r0 decision itself is typed FLOAT-ONLY when r0 > EXACT_CAP.
    n_ag, n_bd, n_dis, n_fonly = 0, 0, 0, 0
    fonly_m = []
    for st in ok_c:
        r = st["rstar_eq"]
        if r is None:
            continue
        if r > EXACT_CAP:
            n_fonly += 1
            fonly_m.append(st["margin_eq"])
            continue
        momT, momE = ob.moments_int(st["Meq"], 2 * r)
        w, R0c = ob.sep_poly_int(r, st["c_eq"], st["L_eq"])
        lt1, _ratF = ob.exact_decision_int(w, R0c, momT, momE)
        flt1 = st["trp_eq"][r] < 1.0
        if lt1 == flt1:
            n_ag += 1
        elif abs(st["trp_eq"][r] - 1.0) <= BORDER_BAND:
            n_bd += 1
        else:
            n_dis += 1
    check("M3 WARD exact-rational anchor at r*_eq <= %d: %d agree, "
          "%d borderline, %d disagree == 0; FLOAT-ONLY beyond cap "
          "%d (min margin %s); r0 = %d decision %s (declared A3)"
          % (EXACT_CAP, n_ag, n_bd, n_dis, n_fonly,
             "%.3e" % min(fonly_m) if fonly_m else "n/a", r0,
             "exact-anchored" if r0 <= EXACT_CAP else "FLOAT-ONLY"),
          n_dis == 0, kill="K2")

    # ------------------------------------------------------------ D
    section("D -- supply typing: tau-screens + the equilibrated "
            "n-read sensitivity")
    taus = [st["tau"] for st in ok_c]
    scr0, _ = ob.screen([st["margin_r0"] for st in ok_c], taus)
    scrS, _ = ob.screen([st["margin_eq"] for st in cert],
                        [st["tau"] for st in cert])
    print("    D1 margin @ r0  : %s" % scr0)
    print("       margin @ r*eq: %s" % scrS)
    ratios = []
    step_dev = 0.0
    for st in ok_c:
        r = st["rstar_eq"]           # A2: sensitivity at r*_eq
        if r is None or st["margin_eq"] is None \
                or not st["gap"] > 0:
            continue
        sc0 = max(1.0, abs(st["n0"]))
        gs = []
        for rel in DN_REL_STEPS:
            dvals = []
            for sgn in (+1.0, -1.0):
                Mp = st["Mt"].copy()
                Mp[0, 0] += sgn * rel * sc0
                tv = eq_trace_at(Mp, r)
                dvals.append(tv)
            if any(v is None for v in dvals):
                gs.append(None)
                continue
            gs.append((dvals[0] - dvals[1]) / (2.0 * rel * sc0))
        if any(g is None or g == 0.0 for g in gs):
            continue
        step_dev = max(step_dev, abs(gs[0] / gs[1] - 1.0))
        dn = st["margin_eq"] / abs(gs[0])
        st["dnstar"] = dn
        ratios.append(dn / st["gap"])
    ratios = np.array(ratios)
    med_ratio = float(np.median(ratios))
    in_grade = SUPPLY_GRADE[0] <= med_ratio <= SUPPLY_GRADE[1]
    scrDn, _ = ob.screen([st.get("dnstar", float("nan"))
                          for st in ok_c if "dnstar" in st],
                         [st["tau"] for st in ok_c
                          if "dnstar" in st])
    d2 = ("SUPPLY-AT-RSTAR(dn*/s dex %s, med %.3f -> %s; dn* "
          "screen %s; fd step agreement worst %.1e; A2)"
          % (fmt3(np.log10(ratios)), med_ratio,
             "HALFGAP-GRADE" if in_grade else "OUT-OF-GRADE",
             scrDn, step_dev))
    print("    D2 " + d2)
    print("    HONEST TYPING: the conjecture's open content is the "
          "uniform arithmetic trace inequality;")
    print("    CCVII typed the raw moment route DISGUISE-MIXED "
          "(dn*/s med 0.354 IN-GRADE) -- the same")
    print("    supply class as HALFGAP; NO independence claim.")
    check("D typed: %s + SAME-SUPPLY-CLASS-AS-HALFGAP(cited)" % d2,
          True)

    # ------------------------------------------------------------ E
    section("E -- controls (rung firing + the equilibrated "
            "certificate on false worlds)")
    worlds = {}
    sm = [ob.build_rung("surf", kz, world="smooth") for kz in zones]
    n_f = sum(1 for r in sm if isinstance(r, dict)
              and r["negA"] > 0)
    check("E1 WARD smooth world fires (neg(A) > 0 on %d rungs)"
          % n_f, n_f > 0, kill="K2")
    worlds["smooth"] = sm
    scw = [ob.build_rung("surf", kz, scramble_seed=SCR_SEED)
           for kz in zones]
    n_f = sum(1 for r in scw if r is None
              or (isinstance(r, dict) and r["negA"] > 0))
    check("E2 WARD scramble fires (%d rungs)" % n_f, n_f > 0,
          kill="K2")
    worlds["scramble"] = scw
    rr9 = ob.window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = ob.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    rE = ob.build_rung("surf", CTRL_KZ,
                       comb=(np.log(nn.astype(float)),
                             2.0 * lamE_[nn]
                             / np.sqrt(nn.astype(float))))
    eps_fire = (rE is None) or rE["negA"] > 0
    check("E3 WARD Epstein comb fires at kz %d (neg(A) %s); "
          "step-level Epstein DECLARED SKIPPED (O(X^2), "
          "predecessor pattern)"
          % (CTRL_KZ, rE["negA"] if isinstance(rE, dict)
             else "chain death"), eps_fire, kill="K2")

    def inj(rr):
        tt = np.arange(rr["M"]) * rr["D"]
        return (ob.INJ_A * np.cos(ob.INJ_GAMMA0 * tt)
                * (np.cosh(ob.INJ_DELTA * tt) - 1.0))
    cosh_w = [ob.build_rung("surf", kz, lag_fn=inj) for kz in zones]
    n_f = sum(1 for r in cosh_w if r is None
              or (isinstance(r, dict) and r["negA"] > 0))
    check("E4 WARD cosh injection A = %g fires (%d rungs)"
          % (ob.INJ_A, n_f), n_f > 0, kill="K2")
    worlds["cosh"] = cosh_w

    sound_min = float("inf")
    n_leak = 0
    e5_rows = []
    for name, lad in worlds.items():
        rungs_w = sorted([r for r in lad if isinstance(r, dict)],
                         key=lambda r: (r["h"], r["kz"]))
        steps_w = ob.make_steps(rungs_w, relax=True)
        n_tau, n_dg, n_ceq = 0, 0, 0
        n_ind, n_raw, n_r0 = 0, 0, 0
        pd_exc = []
        for st in steps_w:
            assemble(st)
            if st["status"] == "REFUSED-TAU":
                n_tau += 1
                continue
            if st["status"] == "REFUSED-DIAG":
                n_dg += 1        # itself a PD refutation, typed
                continue
            if st["status"] == "REFUSED-CEQ":
                n_ceq += 1
                continue
            if st["status"] != "OK":
                continue
            with np.errstate(over="ignore", invalid="ignore"):
                trp, _ = ob.sep_traces(st["Meq"], st["c_eq"],
                                       st["L_eq"], R_MAX)
            fin = [trp[r] for r in range(1, R_MAX + 1)
                   if np.isfinite(trp[r])]
            raw = bool(fin) and min(fin) < 1.0
            at0 = (np.isfinite(trp[r0]) and trp[r0] < 1.0
                   if r0 <= R_MAX else False)
            lam_min = float(st["eigs"][0])
            indef = lam_min <= -1e-10 * max(1.0,
                                            float(st["eigs"][-1]))
            if indef:
                n_ind += 1
                if fin:
                    sound_min = min(sound_min, min(fin))
                if raw:
                    n_leak += 1
            if raw:
                n_raw += 1
                if not indef:
                    pd_exc.append((st["r2"]["kz"], lam_min))
            if at0:
                n_r0 += 1
        e5_rows.append((name, len(steps_w), n_tau, n_dg, n_ceq,
                        n_ind, n_raw, n_r0, pd_exc))
    print("\n    E5 the equilibrated certificate on false worlds "
          "(relaxed steps):")
    for (name, ns, ntau, ndg, nceq, nind, nraw, nr0,
         exc) in e5_rows:
        print("    %-9s: steps %2d  tau<=0 %2d  diag-refused %2d "
              "(PD-refuting)  ceq-refused %2d  eig-indef %2d  "
              "RAW %2d  @r0 %2d"
              % (name, ns, ntau, ndg, nceq, nind, nraw, nr0),
              flush=True)
        for kz, lm in exc:
            print("      PD-exception kz %d: eig lam_min %+.3e > 0 "
                  "(genuinely PD control core, cert SOUND)"
                  % (kz, lm))
    check("E5 WARD soundness on eig-indefinite control steps: RAW "
          "certs there %d == 0; min finite tr p_r %s >= 1 - %.0e"
          % (n_leak, "%.3e" % sound_min
             if np.isfinite(sound_min) else "inf", SOUND_TOL),
          n_leak == 0 and (not np.isfinite(sound_min)
                           or sound_min >= 1.0 - SOUND_TOL),
          kill="K2")
    e5 = " ".join("%s[RAW %d, @r0 %d, PDexc %d]"
                  % (name, nraw, nr0, len(exc))
                  for (name, _ns, _t, _d, _c, _i, nraw, nr0,
                       exc) in e5_rows)
    check("E5b typed: CONTROLS-SEPARATE(%s)" % e5, True)

    # ------------------------------------------------------------ F
    section("F -- screens + verdict assembly")
    scr_lab = ("SCREENS(m@r0 %s | m@r* %s | dn* %s)"
               % (scr0.split("(")[0], scrS.split("(")[0],
                  scrDn.split("(")[0]))
    print("    " + scr_lab)
    check("F1 typed: %s" % scr_lab, True)

    head = ("UNIFORM-ORDER-REGISTERED(r0 = %d, choice %d/%d, %s)"
            % (r0, n_ch, len(choice), blab.split("(")[0])
            if reg_ok else
            "REGISTRATION-BLOCKED(%d/%d at r0 = %d)"
            % (n_ch, len(choice), r0))
    return finish(dict(
        head=head,
        reg="REG-FROZEN(r0 = %d, NEXTPOW2-strict, NO-TUNE, "
            "registry sha8 %s)" % (r0, reg_sha[:8]),
        comp="COMPANION(m0 = %d, CCXXV %s cited)" % (CMP_M0,
                                                     ZOLO_SHA8),
        cen=t_cen, cmpr=t_cmp, rst=t_h, law=t_law, orc=t_orc,
        flo="FLOOR(GERSH-CERT %d/%d, TRANSPORT-win %d/%d, premise "
            "%d/%d)" % (n_gc, len(ok_c), len(ok_c) - n_gwin,
                        len(ok_c),
                        sum(1 for st in ok_c if st["premise"]),
                        len(ok_c)),
        bl=blab, sup=d2, e5="CONTROLS-SEPARATE(%s)" % e5,
        scr=scr_lab))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = " / ".join(labels.get(k, "-") for k in
                             ("head", "reg", "comp", "cen", "cmpr",
                              "rst", "law", "orc", "flo", "bl",
                              "sup", "e5", "scr"))
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): this is a REGISTRATION, not a result:
  the uniform-order conjecture EXISTS r0 FORALL h: tr p_r0(M~_h) < 1
  is registered with r0 frozen by a surface-only rule and an
  explicit no-tuning clause; the implication chain (interlacing +
  separator + trace bound + Sylvester => wall) is elementary; the
  ENTIRE open content is the uniform arithmetic trace inequality on
  the equilibrated ladder -- the same supply class as HALFGAP
  (CCVII DISGUISE-MIXED cited), no independence claim; every census
  is float-level on a deployed finite ladder (r0 decisions anchored
  exact-rationally); certification on finitely many rungs proves
  nothing at other h.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
