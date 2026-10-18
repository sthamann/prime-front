#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bughunt8_probe -- PRIME.BUGHUNT8.01

FROZEN SPEC (2026-08-20).  EXPLORATION ONLY.  Eighth adversarial
audit: the discovery rounds 176-182 (r176 = bughunt7_probe [audit the
auditor + the corrections-of-record application], r177 =
manifold_invariance_probe, r178 = l1wpd_closure_probe, r179 =
dbn_heatflow_probe, r180 = cbj_frame_probe, r181 = cbj_subdof_probe,
r182 = alignment_law_probe; notes CDXCII-D (492-500) plus the
wave-five promotion note CDXCVIII).  Predecessors
r87/r109/r130/r149/r164/r170/r176.  This probe writes NOTHING but
stdout, reads the frozen corpus READ-ONLY (probe sources as text,
kept run/smoke/calib logs, next.txt, verification/v931-v935 and the
two TeX surfaces AS TEXT for the wave-five adoption audit, pinned
read-only `git show`), imports NO frozen probe, and makes NO RH CLAIM
in either direction.  Every confirmed finding carries at least one
falsifiable gate.

METHOD (bughunt I-VII standard): source/note/log conjunctions for
every wording finding; OWN re-implementations for every numeric
re-check (own sympy derivations on own symbols, own prime-power
sieve, own AND-fire/DFS graph semantics, own diff normalizer, own
drawdown/cofinal arithmetic, own CS-gap/dof/MV arithmetic); expensive
claims audited on the kept record logs, cheap claims re-run inline.
External literature verification (web, 2026-08-20) pinned in this
spec: Polymath15, Res. Math. Sci. 6:31 (2019), H_t(z) = int e^{tu^2}
Phi(u) cos(zu) du, Lambda <= 0.22 UNCONDITIONAL (the 2020 improvement
Lambda <= 0.2 via the Platt-Trudgian verification exists; r179's use
of 0.22 is the CONSERVATIVE choice -- every kill ratio only grows
with a smaller window); Rodgers-Tao, Forum Math. Pi 8 (2020) e6,
Lambda >= 0; Newman, Proc. AMS 61 (1976) 245-251; de Bruijn, Duke
Math. J. 17 (1950) 197-226; Ortega-Cerda & Seip, "Fourier frames",
Ann. of Math. (2) 155 (2002), no. 3, 789-806 (the Carleson-box
condition characterizes the UPPER/Bessel inequality; the lower/
sampling half needs the density leg -- r181's direction adjudication
is correct); Montgomery & Vaughan, J. London Math. Soc. (2) 8 (1974)
73-82 (mean-value form with 3 pi/delta, unconditional).

=======================================================================
FINDINGS LEDGER (the deliverable; severity frozen; gates named)
=======================================================================
BH8-F1 [MAJOR][X1 core: wall-identity stated as object-identity;
  vacuous-gate carrier; NO VERDICT FLIP]  r182's terminal residue
  adjudication "SAME-WALL-NOT-NEW-OBJECT" (spec verdict enum
  FLOOR-FORM-SAME-WALL-AS-THETAINF-HPIN; note D: "seine Floor-Form
  landet auf der BEKANNTEN theta_inf/H-pin-Mauer statt eine neue zu
  eroeffnen") states a CLASS-level convergence as a formal-object
  identity.  The exact object list (X1 deliverable): (W1) r175
  theta_inf face == the classical-evaluation cap on
  |A_2(c)/A_0(c)|/T_z^4 (OPEN-NONPERTURBATIVE-VARIATIONAL); (W2)
  r178 H-pin Omega-a == EPS-LOCK, eps_bar <= poly(x)|A_0|sqrt(G),
  equivalently the tau/A_0^2 cap; (W3) r181's named debt == control
  of the deep-spectrum jet mass sum_{deep} lam_i s_i^2 (the
  ill-conditioned subspace); (W4) r182's floor form == per-mode
  lower bounds on the quotient |N_i(d)|/|A_0(d)|.  These are FOUR
  DISTINCT FORMAL STATEMENTS (different functionals, different
  quantifiers) sharing a machine-namable CLASS: the same source
  object (the argmin eigenvector d of the prime-loaded wall M -- the
  single nonlinear link), the A_0-quotient shape, the
  nonperturbative-variational typing, and the adjacent A0-triangle
  loop.  NO round machine-checks any pairwise identity; r178's own
  spec adjudicates the closest pair EXPLICITLY as "same
  conditioning-walled quotient class as theta_inf, DISTINCT
  statement" -- and r182 contains NO formalization of either W1 or
  W2 (machine-grepped: no eps_bar, no 0.155/THETA_BAR anywhere in
  its source).  The carrying gate G51-floor-form-same-wall is
  check(..., True, ...) -- a hardcoded always-PASS adjudication
  gate inside the 37/37 count whose own detail text says "the SAME
  nonperturbative-variational CLASS".  THE RESIDUE CONCLUSION "no
  new edge" SURVIVES on a different, machine-checked ground: G44
  names the floor route {A0-FLOOR, VARIATIONAL-QUOTIENT-WALL} and
  EXCLUDES it from the delivered set -- an optional upgrade route
  consumed by nothing is not a residue edge.  CORRECTION OF RECORD
  (proposed wording): replace "SAME-WALL-NOT-NEW-OBJECT" by
  "SAME-CLASS-NOT-NEW-EDGE: dieselbe Variationsquotienten-KLASSE
  wie theta_inf (r175) und H-pin Omega-a (r178: DISTINKTE
  Statements) -- vier distinkte formale Statements ueber demselben
  Quell-Objekt (Wall-Argmin-Strahl d, der eine nichtlineare Link)
  in A_0-Quotientenform; KEIN neuer Residuum-Edge, weil die
  Floor-Route optional und maschinell aus dem Delivered-Set
  ausgeschlossen ist (G44), NICHT weil das Objekt identisch waere."
  GATE: G10.
BH8-F2 [MINOR][round-numbering drift on the promotion-record and
  head-note surfaces -- X2]  The canonical round numbering is fixed
  by the freeze-commit subjects (pinned read-only): 176 = bughunt7,
  177 = manifold, 178 = l1wpd, 179 = dbn, 180 = cbj_frame, 181 =
  cbj_subdof, 182 = alignment; the corrections commit (9846c2ae)
  carries NO round number.  Against this: (i) note CDXCVIII (wave
  five) calls the corrections application "Runde 177/CDXCIII";
  (ii) CDXCVIII enumerates "die Runden 176-180 (Bughunt VII selbst
  + Manifold-Invarianz + de Bruijn-Newman + Non-Clifford +
  CBJ-Frame, Noten CDXCII-CDXCVII)" -- OMITTING the l1wpd round
  (r178, note CDXCIV, inside the very note range it cites) and
  IMPORTING "Non-Clifford" (the independent session's untracked
  lane, nonclifford_prime_probe.py; exactly ONE mention in all of
  next.txt, no numbered note); (iii) note D attributes the dBN
  instruments to "r176" ("Hellmann-Feynman-Klasse,
  r176-dBN-Instrumente") -- dBN is r179, r176 is Bughunt VII.  No
  verdict content rides on the numbering; the promotion-record note
  misidentifies which rounds await Bughunt VIII.  CORRECTION:
  corrections = unnumbered application commit; rounds 176-182 as
  above; "r176-dBN" reads "r179-dBN".  GATE: G11.
BH8-F3 [MINOR][adjudication-as-vacuous-gate -- BH6-F3/BH7-F8 class
  recurrence on the LIVE terminal-residue surface]  r182's
  G51-floor-form-same-wall is check("G51...", True, ...): it cannot
  fail, yet it carries the round's residue adjudication token and
  counts into 37/37 PASS.  Context scan (own flat-source scan of
  all seven round probes): the check(..., True) pattern also
  appears as the established G60-demand-audit disclosure gate
  (r178-r182) and r182's G14-law-machinery-predefined declaration
  (whose enforcement lives in the REAL gate G45 seal-rehash), plus
  smoke-only branches (G54-tau-screen-smoke, not verdict-bearing).
  The DISCLOSURE-gate pattern is house-conventional; G51 is NOT a
  disclosure -- it is the adjudication of BH8-F1.  Similarly r182's
  G12 okA/okB legs verify additivity/scale-invariance of an
  explicitly linear coded form (tautological given the form; the
  load-bearing content -- Gram source-freeness and the definitional
  identity s_i A_0 == <v_i, D d>/sqrt(Smu) -- is properly gated in
  G11/G21/G22/G24).  CORRECTION: re-type G51 (and, when externally
  cited, the G60 family) DEFINITIONAL/ADJUDICATION per the BH6-F3
  convention; the F1 correction supplies the honest wording.
  GATE: G12.
BH8-F4 [NOTE][r182 record gates are replication-typed; timeline
  VERIFIED CLEAN]  The five placeholder retypings disclosed "at
  freeze" are fully reconstructible from the kept pre-freeze
  calibration log (calib_alaw_pass1.log, SPEC 74dd4432235aab7f):
  the five calibration FAILs are exactly the five placeholder gates
  {G32, G34, G35, G36, G50}; all 14 record alphas appear verbatim
  as CAL_ALPHA lines; the witness costs/tails/ratios appear as
  CAL_WIT lines (5.3e-07/-5.2069/999.3 and 8.2e-14/-3.0214/1000.9);
  the frozen overshoot table {3.41, 10.14} derives EXACTLY from the
  calibration G46 detail margins 5445.98/41892338390.79 via
  log10(margin_law/margin_raw) with the r180 raw margins 2.14/3.05
  (own arithmetic: 3.4057/10.1378, abs dev <= 0.005); the record
  runs at the final SHA are deterministic reproductions.  NOTHING
  was retyped after record data -- the retyping is calibration ->
  freeze -> record, house-legal and disclosed.  The honest typing
  consequence (this note): the ALPHA_BAND (0.38, 0.54) is a
  DESCRIPTIVE band drawn at freeze around the measured alphas
  [0.3988, 0.5232], and the record law-gates are REPLICATION gates
  (the spec itself says "record values below ARE the calibrated
  numbers") -- external citation should say "measured envelope
  band", not "predicted band".  GATE: G13.
BH8-F5 [NOTE][note/commit packaging quirks -- X2 lineage]  (i) The
  r179 dBN note CDXCVI rode in the r177 freeze commit (59de0afb
  adds CDXCV + CDXCVI), and the r179 probe was committed LATER
  (c423f0e5, probe file ONLY, no note): note-before-probe commit
  order, content and position intact; (ii) the wave-five note
  CDXCVIII rode in the r181 commit (0f2a76c4 adds CDXCIX +
  CDXCVIII) while the wave-five surface commit (4c5b0867) touched
  no next.txt -- the CDXCVII -> CDXCVIII numeral slot is owned by
  the wave-five lane, position in the file strictly descending,
  content integrity verified.  Both cross-ridings are consistent
  with the notes' own head-numeral disclosures.  GATE: G14.
BH8-F6 [NOTE][residue-form wobble across the arc -- X4]  r178
  (CDXCIV) refined the pair item to "{H-PIN == die eine
  lambda-uniforme Kante des Paars {L1, WPD}} + {WPD-nicht-lambda-
  Beine/TAILWPD}" and recommended the refined form for future
  rounds (lever (b)); r180 (CDXCVII), r181 (CDXCIX) and r182 (D)
  adopt it; but r179 (CDXCVI, written AFTER CDXCIV) reverts to the
  coarse pair form "{L1 = TAIL bewiesen + H-pin offen, WPD offen}"
  without the CDXCV-style parallel-lane disclosure.  Cardinality-
  identical, nothing wrong (the coarse form is the CDXCIII
  canonical form); bookkeeping wobble on the residue surface.  The
  wave-five surfaces correctly carry the CDXCIII canonical form --
  the final form FOR THE PROMOTED ARC (rounds 171-175, which
  pre-date the r178 refinement).  GATE: G15.
BH8-F7 [NOTE][r177 price-ladder margin: measured vs proven split]
  The "30-33 orders above the 1e-25 bar" refuter-price ladder is
  the measured FIRST-ORDER-EXACT instrument minimum (weighted-LS
  surrogate global minimum + exact candidate re-evaluation + the
  EIGF == EIG8 == EIG2 saturation); the PROVEN refuter floor is the
  b*(h) schedule, i.e. margins of only 23.8/21.7/15.7/4.4 orders
  above the bar at h = 4/5/8/13 (own arithmetic: log10 b* + 25) and
  NONE at h >= 16 -- the CS-GAP ladder 6.32/9.00/15.79/28.19/35.61
  (own recompute from the frozen PRICE_EIGF/BSTAR tabs, abs 0.02)
  is exactly the unproven headroom.  All surfaces type the ladder
  GEMESSEN and disclose the first-order scope; the delivered DK
  exclusion theorem is INDEPENDENT of the ladder.  Adjudicated:
  NOT-AN-OPTIMIZER-ARTIFACT within the stated scope (the surrogate
  minimum is the exact global minimum of the linearized problem;
  candidates re-evaluated exactly; my own structural check: any
  feasible refuter mixes eigenmodes at O(1) fraction, so its
  residual carries the FG-scale ~ 1e4-1e5 x tau seen in the
  ladder's first rung).  External citation should pair the
  measured 30-33 with the proven b*-schedule margins.  GATE: G16.

CHECKED CLEAN (adversarially, no finding): the BH7 corrections of
record are FAITHFULLY APPLIED (five comment blocks OUTSIDE the frozen
docstrings; all five r171-r175 SPEC_SHAs recomputed byte-identical;
F1 blocks on exactly {r172, r173, r174, r175}, F3 on r171 only, F4 on
r173 only, F2/F7 on r175 only; F5/F6/F8 note-only exactly as CDXCIII
disclosed; every block quotes its unchanged SHA); the wave-five
surfaces ADOPT the corrections verbatim (all five v931-v935 modules
carry the {H1 AND H2 AND H3} triple; v931 the DEFINITIONAL retype;
v933 the mod-D qualifier D = 0.004183 AND the DK-radius scoping
"gated h <= 13, measured to h = 20"; v935 the MEASURED-LAW
extrapolation typing; tfpt_3 carries triple + mod-D + DK-scope +
measured-law in the five veri blocks; tfpt_prime_front carries the
triple twice; all five promo_rerun logs green at the record SHAs with
record gate counts); BUGHUNT7 ITSELF RE-VERIFIED (own drawdown
recompute D = 0.004183 at (14, 19) from the cited r172 ladder; own
bar-cofinal-with-limsup>bar counterexample on DIFFERENT numbers; own
AND-fire re-demonstration of BH7-F1 on the declared chain; BH7
run1/run2 raw diff 0 as note CDXCII claims; smoke1 17/21 at
8a488f1c079f13a3 with fail set exactly {G13, G24, G25, G29} == the
four disclosed instrument bugs); r177 AMENDMENTS LEGITIMATE (run1/2/3
fail EXACTLY G41 and only G41; the A1/A2/A3 story numbers verbatim in
the kept logs: run1 h24 zmin/zm 2.065e+11 + ba3min -1.918e+11, run2
h24 3.394e-09 + ba3min +1.000, run3 h16 drift 1.77e-02; the A3
retype FEASIBLE-UPPER-VALUE is MONOTONE-SAFE -- own check: the BA3
residual (tau + OFF - z)/tau is strictly decreasing in z for tau > 0,
so a smaller true minimum makes the exhibited-passer conclusion
STRICTLY stronger, and the BA3-PASSING-REFUTER-EXISTS claim needs
only the exhibited FEASIBLE point with its measured residual -- no
minimization at all); r177 DK SCOPE HONESTLY SEPARATED on all
surfaces (spec: "covers h <= 13 at frozen bar"; note CDXCV: gated
h <= 13 / measured-residual to h = 20 / h = 24 uncovered; v933 +
the r173 correction block carry the same split); r178 NAME-COLLISION
handling CLEAN downstream (rounds 179-182 and v931-v935 contain NO
r133 ball-matching H1/H2/H3 use -- machine-grepped; every downstream
H1/H2/H3 is the r171 jet family or the disambiguated H123M label);
r178 WPD-LAMBDA-EDGE == H-PIN is DEMONSTRATED-AT-DECLARED-EDGES, not
asserted (own AND-fire replication: {EPSLOCK, SPACREM, H123M} fire
HPIN, {HPIN, THEOREM-A, DCS-357} fire WPD-BATTERY, the jet-triple
grants fire PF/HCOF but NOT HPIN/WPD -- and the two load-bearing
edges are corpus theorems replicated in-round: x_0 = 121/112 own
integer scan class, 357 D_cs cells; the middle-a and tail legs are
carried separately, so the "==" is a label consolidation of the
lambda-uniform CONTENT only, disclosed); r179 FACTOR-4 LEMMA CORRECT
(own sympy: the polynomial heat operator E_t = sum (-t)^m d^{2m}/m!
satisfies E_t[p](2w) == E_{t/4}[p(2 .)](w) on a generic quartic; own
exact-rational 3-zero toy: the gamma-unit drift dgamma_1/dt_gamma ==
sum_k 4 gamma_1/(gamma_1^2 - gamma_k^2) + 1/gamma_1 EQUALS the
transported x-side ODE 2 sum 2/(x_1 - x_k) over the mirrored zero set
+-2 gamma -- the factor 4 threads the drift exactly); r179 trace law
re-derived OWN (generic quartic, T = 4y d^2 + 2d, trace slope ==
2d(2d-1) == 56); r179 FLOW-P scoping honest (the exact semigroup acts
on the DERIVED census polynomial; the source-face identity is
DEFINED-AS-FORM, "not a claimed identity" in G60; the three-face
inequivalence 1e9+ is the round's own headline); r179 HF derivatives
on the RIGHT objects (dtau = v0' dM v0 with normalized ground pair;
dc = sum_{i>0} (v_i' dM v0)/(E0 - E_i) v_i -- textbook first order);
r180 DOF CONVENTION CORRECT (own sieve: block k = 12 has n == 474
prime-power atoms; dof = span x H/pi == 112.8 at H = 512 -- the
length-2H window makes span x 2H/(2 pi) == span x H/pi: no off-by-2pi);
r180 MV MARGIN EXACT (own rationals: 3 pi/(63 pi/20) == 20/21,
margin 1 - 20/21 == 1/21; at link 1 the budget H(1 - 3 pi) < 0);
r180 BERTRAND SUFFICIENT for the selector sequence (own argument +
sieve: any Bertrand prime in (2^k, 2^{k+1}) is odd for k >= 2, hence
a valid non-2-power prime-power atom, so the set is nonempty for all
k and h-hat_k > 2^k -> oo; own selector ladder k = 2..12 ==
7/13/31/61/127/251/509/1021/2039/4093/8191, nonempty through k = 17);
r180 JET-RESCUE LIKE-WITH-LIKE (c_intra and c_point are min over the
SAME clusters of lam_min on the SAME G_CC, jet basis vs point basis;
the jet-convention covariance of the 107-dex figure is disclosed in
the round's own lever (a)); r181 A1 CLEAN (own diff: run1 vs run3
outputs IDENTICAL modulo SPEC_SHA + wall-clock tokens -- the
post-record spec-TEXT amendment moved nothing executable; own sympy:
the FEJ1 confluent-limit constant is -What''(0) == 1/6 for What ==
sinc^2(x/2), and 1/12 was the series coefficient -- the amendment
corrects a real transcription slip); r181 CUT PREDEFINED SOURCE-FREE
(the 1e-12 cut lives on the eigenvalues of the source-free Jacobi
Gram, sealed pre-ward with end-rehash; calibration fail set exactly
{G50} as disclosed); r181 OCS DIRECTION CORRECT (web-pinned above);
X5 MEASURED-CARRIES CHAIN CUSTODY CLEAN (r180 measures the unscoped
margins on WFULL/gamma_7000 with the r169 SF1/SF2 recipe -- min
1.405 at h = 4, selector margins 2.14/3.05; r181 RE-MEASURES the
same delta/delta_req on the same instrument and replicates the r180
strings, its margin_sub crossover table carrying 1.405/1.142/
8.020e-03; r182 RE-MEASURES the selector margins fresh and gates
them against the replicated r180 strings 2.14/3.05: same frozen
instrument, three independent re-measurements, nothing stale);
determinism: all seven record pairs re-diffed OWN (raw 0/4/3/4/2/2/2
line pairs, timing-normalized EMPTY -- the notes claim exactly this
where they state a count; CDXCIV states no raw count, measured 3).

X-VERDICTS (the contract deliverables):
X1 WALL-IDENTITY: CLASS-NOT-OBJECT.  The four wall statements
  (theta_inf face, H-pin Omega-a, r181 subspace debt, r182 floor
  quotient) are pairwise DISTINCT formal objects; NO machine gate
  anywhere checks an identity; r178 explicitly adjudicates the
  closest pair DISTINCT; r182 formalizes neither counterpart.  What
  IS machine-supported: one shared source object (the wall argmin
  ray d -- the single nonlinear link, exhibited exactly in
  r178/r182), the A_0-quotient shape, the shared typing, the
  adjacent A0-triangle loop; and r181/r182 measure the SAME object
  at the instrument level (the s_i mass distribution).  The r182
  residue conclusion "no new edge" SURVIVES via the G44 exclusion
  (optional route, delivered-set-excluded), NOT via identity:
  BH8-F1 correction of record required.
X2 NOTE NUMERALS: CDXCII-D (492-500) collision-free, gap-free,
  strictly descending, attribution exact (each round note names its
  probe file; CDXCIII names all five corrected probes; CDXCVIII
  names the five modules).  Cross-ridings verified position- and
  content-exact: CDXCVI rode in the r177 commit (r179's own commit
  is probe-only), CDXCVIII rode in the r181 commit (the wave-five
  surface commit touches no next.txt) -- the CDXCVII -> CDXCVIII
  slot is wave-five-owned.  ROUND-NUMBERING DRIFT = BH8-F2.
X3 SPEC_SHA INTEGRITY: all SEVEN round probes hash to their claimed
  SPEC_SHAs; all FIVE corrected r171-r175 probes hash UNCHANGED
  after the correction commit (blocks outside the docstrings,
  ast-clean); all 30 kept smoke/calib/run logs match the disclosed
  amendment/smoke-fix lineages gate-exactly (every FAIL row matches
  its disclosed root cause).
X4 RESIDUE TRANSPORT: consistent r176 -> r182.  CDXCIII fixes the
  canonical triple form; CDXCIV refines the pair item (H-PIN the
  one lambda-uniform edge); CDXCV carries the canonical form with
  the parallel-lane disclosure; CDXCVI reverts to the coarse form
  (BH8-F6 wobble, cardinality-identical); CDXCVII/CDXCIX/D adopt
  the refined form; wave five carries the CDXCIII canonical form
  (correct for the promoted 171-175 arc).  L1 = TAIL proven + H-pin
  open REMAINS ACCURATE: r178's machine status audit found no
  silent closure and every later round re-affirms "NICHTS
  geschlossen"; nothing reopened.
X5 MEASURED-CARRIES CHAIN: custody clean (see CHECKED CLEAN).  The
  margins {>= 1.405 unscoped; 2.14/3.05 selector} originate in
  r180's G35 measurement and are independently RE-MEASURED (not
  merely cited) by r181 (delta/DC replication + margin_sub table)
  and r182 (G46), all on the same frozen instrument (R4.build_cell
  + r169 SF1/SF2 recipe + WFULL gamma_7000 ward window + SIGMA0 =
  0.15).  No stale number found.

CORRECTIONS OF RECORD RECOMMENDED (per r87/r97/r130 convention NOT
retro-edited): (K1) BH8-F1 wording on the r182/D surfaces
(SAME-CLASS-NOT-NEW-EDGE, exclusion-grounded); (K2) BH8-F2 numbering
(corrections commit unnumbered; rounds 176-182 canonical; l1wpd is
r178; Non-Clifford out-of-lane; "r176-dBN" -> "r179-dBN"); (K3)
BH8-F3 retype G51 DEFINITIONAL/ADJUDICATION; (K4) BH8-F4 cite the
alpha band as measured-descriptive; (K5) BH8-F7 external citations
pair the measured 30-33 orders with the proven b*-schedule margins.

FROZEN NUMERICS (audit pins; sources = frozen record logs/specs):
SHAS7 = {bh7: 5a081ea1327f198a, mi: af86ec3b097ae8c4, l1wpd:
0e306146bebbd9be, dbn: 67eaf86c7bfa7d84, cbj: d7fbf2d956184674,
subdof: 2db82c76ce5f067c, alaw: e4cdb9a932093196}.  SHAS5 = {jmf:
57de8b2a83677a9c, tt: cf27df22aa5dffbf, h3c: 876dafc977d3d8fc, gp:
3050678b352eaa9a, tip: 3044558e5fa52e01}.  PRE_SHAS = {bh7:
8a488f1c079f13a3; mi: 642da05e6791d466 -> 5a0bfabf31ce4f07 ->
66ebfd30613add44 -> b16ec9c162bfe6d7; dbn: 5b49b4009c068c17; cbj
calib: e1ad438831ebab26; subdof: 8c7e7644a83618da ->
8d801d0a3baac7e1; alaw: 74dd4432235aab7f}.  RAW_DIFFS = {bh7: 0,
mi: 4, l1wpd: 3, dbn: 4, cbj: 2, subdof: 2, alaw: 2}, normalized 0;
A1_CROSS (subdof run1 vs run3, +SHA-normalized) raw 3 -> 0.
COMMITS = {r176: 827d9682, corr: 9846c2ae, r177: 59de0afb, r178:
8336a6be, r179: c423f0e5, r180: d35c104f, r181: 0f2a76c4, wave5:
4c5b0867, r182: 2e7e97e1}.  YT_R172 (25 rungs, cited ladder) as in
code; D_STR = 0.004183 at (14, 19), rel 5e-3.  PRICE_EIGF_TAB =
{4: 1.353657e5, 5: 4.696766e5, 8: 2.844554e6, 13: 3.820643e7,
16: 9.467704e7}; BSTAR_TAB = {4: -1.1890, 5: -3.3241, 8: -9.3405,
13: -20.6087, 16: -27.6292}; CSGAP_STR = (6.32, 9.00, 15.79, 28.19,
35.61) abs 0.02; PROVEN_MARGINS = (23.81, 21.68, 15.66, 4.39) abs
0.02.  ALPHAS = (0.5232, 0.3988, 0.4644, 0.4508, 0.4440, 0.4781,
0.4858, 0.4860, 0.5111, 0.5190, 0.5223, 0.5092, 0.4765, 0.4261) at
h = 4..16 + 20; ALPHA_BAND = (0.38, 0.54); OVERSHOOT_DERIV: log10(
5445.98/2.14) == 3.41 abs 0.01, log10(41892338390.79/3.05) == 10.14
abs 0.01; WIT_CAL = ((5.3e-07, -5.2069, 999.3), (8.2e-14, -3.0214,
1000.9)).  ALAW_CALIB_FAILS = {G32-law-ladder, G34-law-form,
G35-law-predicts-ladder, G36-eigenvector-anatomy, G50-tau-screen};
ALAW_SMOKE1_FAILS = {G24-linearity-instance-and-witness};
SUBDOF_CALIB_FAILS = {G50-tau-screen}; BH7_SMOKE1_FAILS =
{G13-f4-manifold-scope, G24-pf2-concavity-own,
G25-pointwise-coverage, G29-bridge-instrument-own}; MI_RUN_FAILS =
{run1: G41, run2: G41, run3: G41}.  MI_A_NUMBERS = {run1:
("zmin/zm 2.065e+11", "ba3min -1.918e+11"), run2: "zmin/zm
3.394e-09", run3: "1.77e-02"}.  SELECTOR = (7, 13, 31, 61, 127,
251, 509, 1021, 2039, 4093, 8191) at k = 2..12; N_K12 = 474;
DOF_K12_R8 = 112.8 rel 2e-2; H_K12_R8 = 512.  GATE_TAB (lineage) in
code.  X5_STRINGS in code (r180/r181/r182 record-log margin rows).
PROMO_LOGS = {jmf: 36/36, tt: 33/33, h3c: 36/36, gp: 20/20, tip:
28/28} at SHAS5.  NOTE_SCOPE = 492..500.  RUNTIME_BAR = 600 s.
Deterministic: no RNG; git reads pinned read-only.  Amendments
after the frozen run, if any, are appended as numbered AMENDMENT
blocks.

VERDICT ENUM (frozen): BUGHUNT8-FINDINGS(7: 1 MAJOR / 2 MINOR /
4 NOTE) + WALL-IDENTITY-CLASS-NOT-OBJECT(F1/X1) +
NO-NEW-EDGE-SURVIVES-VIA-EXCLUSION(X1) +
ROUND-NUMBERING-DRIFT(F2/X2) + VACUOUS-ADJUDICATION-GATE(F3) +
RETYPE-TIMELINE-CLEAN(F4) + CROSS-RIDINGS-VERIFIED(F5/X2) +
RESIDUE-FORM-WOBBLE(F6/X4) + PRICE-LADDER-MEASURED-VS-PROVEN-
SPLIT(F7) + CORRECTIONS-FAITHFULLY-APPLIED(r176) +
WAVE-FIVE-ADOPTION-VERBATIM + BH7-REVERIFIED-CORRECT +
AMENDMENTS-LEGITIMATE-MONOTONE-SAFE(r177) +
NAME-COLLISION-CLEAN-DOWNSTREAM(r178) +
WPD-HPIN-CONSOLIDATION-DEMONSTRATED(r178) +
FACTOR-4-CORRECT(r179) + DOF-MV-BERTRAND-CORRECT(r180) +
A1-CLEAN-FEJ1-ONE-SIXTH(r181) + NUMERALS-CLEAN(X2) +
LINEAGE-CLEAN(X3) + RESIDUE-TRANSPORT-CONSISTENT(X4) +
MEASURED-CARRIES-CUSTODY-CLEAN(X5) + LITERATURE-PINS-EXACT.
NO verdict of rounds 176-182 flips.

SMOKE-STAGE FIX (pre-record, disclosed; smoke1 = 17/20 at the
first-freeze SPEC_SHA b38a00f289a551b0, log kept as
bughunt8_probe.smoke1.log; NO record run existed yet).  THREE
instrument bugs in the AUDIT CODE itself, no bar, class, finding or
criterion moved anywhere: (a) the G10 flat-source conjunction for
the G51 detail text matched across adjacent Python string literals
whose quote pairs survive whitespace-stripping ("theSAME"" ...") --
fixed by stripping quote characters from the flat copy (the frozen
text is unchanged and contains the string); (b) the G13 overshoot
regex matched the FIRST h7:/h13: tokens in the calibration log,
which belong to the earlier PRED-deviation table -- fixed by
anchoring to the G46 "margins ['h7:...', 'h13:...']" form; (c) the
G29 unscoped-min conjunction used the docstring token 1.405 against
the record log, which prints the 2dp form "min over all rungs 1.40
>= 1.35" -- fixed by matching the log form in the log and the 1.405
string in the frozen spec.  All three fixes verified in isolation;
smoke2 at the fixed SHA must be clean.

AST FIREWALL: no zero-oracle names; no z-function use; no np.load;
no import of verification/ or of any frozen probe; git reads pinned
read-only.  NO RH CLAIM.  EXPLORATION ONLY.

AMENDMENT 1 (post-record, disclosed; run1/run2 = 20/20 at SPEC_SHA
08ec7833773ebc32, logs kept as bughunt8_probe.run1/run2.log -- the
record itself was GREEN; the failing condition arose only AFTER the
record, when THIS round's own research note DI landed in next.txt).
ROOT CAUSE (instrument self-reference, own audit code): the G11 leg
nxt.count("Non-Clifford") == 1 froze a WHOLE-FILE token count; the
bughunt8 note DI necessarily names the token twice (finding F2 +
correction K2), so the frozen count broke on the auditor's own
deliverable -- a self-reference hazard, not a corpus change (the
audited notes CDXCII-D are byte-identical).  FIX: the count is
scoped to the AUDITED note lines CDXCII-D (sum over the nine parsed
note lines == 1 -- exactly the claim: one mention inside the audited
range, in CDXCVIII, and no numbered note for the lane).  NO bar,
class, finding or criterion moved; F2 unchanged.  run3/run4 at this
amended SHA are the post-amendment records; all logs kept.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
NEXT = os.path.join(HERE, "..", "next.txt")
VERI = os.path.join(REPO, "verification")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

SHAS7 = {
    "bh7": ("bughunt7_probe.py", "5a081ea1327f198a"),
    "mi": ("manifold_invariance_probe.py", "af86ec3b097ae8c4"),
    "l1wpd": ("l1wpd_closure_probe.py", "0e306146bebbd9be"),
    "dbn": ("dbn_heatflow_probe.py", "67eaf86c7bfa7d84"),
    "cbj": ("cbj_frame_probe.py", "d7fbf2d956184674"),
    "subdof": ("cbj_subdof_probe.py", "2db82c76ce5f067c"),
    "alaw": ("alignment_law_probe.py", "e4cdb9a932093196"),
}
SHAS5 = {
    "jmf": ("jetmass_floor_probe.py", "57de8b2a83677a9c"),
    "tt": ("toproot_theta_probe.py", "cf27df22aa5dffbf"),
    "h3c": ("h3_cofinal_probe.py", "876dafc977d3d8fc"),
    "gp": ("gonek_pricing_probe.py", "3050678b352eaa9a"),
    "tip": ("thetainf_pin_probe.py", "3044558e5fa52e01"),
}
# log -> (SPEC_SHA in log, gates string)
LOG_TAB = {
    "bughunt7_probe.smoke1.log": ("8a488f1c079f13a3", "17/21"),
    "bughunt7_probe.smoke2.log": ("5a081ea1327f198a", "21/21"),
    "bughunt7_probe.run1.log": ("5a081ea1327f198a", "21/21"),
    "bughunt7_probe.run2.log": ("5a081ea1327f198a", "21/21"),
    "manifold_invariance_probe.smoke1.log":
        ("642da05e6791d466", "37/38"),
    "manifold_invariance_probe.smoke2.log":
        ("5a0bfabf31ce4f07", "38/38"),
    "manifold_invariance_probe.run1.log":
        ("5a0bfabf31ce4f07", "38/39"),
    "manifold_invariance_probe.run2.log":
        ("66ebfd30613add44", "38/39"),
    "manifold_invariance_probe.run3.log":
        ("b16ec9c162bfe6d7", "38/39"),
    "manifold_invariance_probe.run4.log":
        ("af86ec3b097ae8c4", "39/39"),
    "manifold_invariance_probe.run5.log":
        ("af86ec3b097ae8c4", "39/39"),
    "l1wpd_closure_probe.smoke1.log": ("0e306146bebbd9be", "25/25"),
    "l1wpd_closure_probe.run1.log": ("0e306146bebbd9be", "29/29"),
    "l1wpd_closure_probe.run2.log": ("0e306146bebbd9be", "29/29"),
    "dbn_heatflow_probe.smoke1.log": ("5b49b4009c068c17", "25/26"),
    "dbn_heatflow_probe.smoke2.log": ("67eaf86c7bfa7d84", "26/26"),
    "dbn_heatflow_probe.run1.log": ("67eaf86c7bfa7d84", "26/26"),
    "dbn_heatflow_probe.run2.log": ("67eaf86c7bfa7d84", "26/26"),
    "calib_cbj_pass1.log": ("e1ad438831ebab26", "39/41"),
    "cbj_frame_probe.smoke1.log": ("d7fbf2d956184674", "41/41"),
    "cbj_frame_probe.run1.log": ("d7fbf2d956184674", "41/41"),
    "cbj_frame_probe.run2.log": ("d7fbf2d956184674", "41/41"),
    "cbj_subdof_probe.smoke1.log": ("8c7e7644a83618da", "26/36"),
    "calib_subdof_pass1.log": ("8c7e7644a83618da", "36/37"),
    "cbj_subdof_probe.run1.log": ("8d801d0a3baac7e1", "37/37"),
    "cbj_subdof_probe.run2.log": ("8d801d0a3baac7e1", "37/37"),
    "cbj_subdof_probe.smoke2.log": ("8d801d0a3baac7e1", "37/37"),
    "cbj_subdof_probe.run3.log": ("2db82c76ce5f067c", "37/37"),
    "cbj_subdof_probe.run4.log": ("2db82c76ce5f067c", "37/37"),
    "cbj_subdof_probe.smoke3.log": ("2db82c76ce5f067c", "37/37"),
    "alignment_law_probe.smoke1.log": ("74dd4432235aab7f", "36/37"),
    "calib_alaw_pass1.log": ("74dd4432235aab7f", "32/37"),
    "alignment_law_probe.smoke2.log": ("e4cdb9a932093196", "37/37"),
    "alignment_law_probe.run1.log": ("e4cdb9a932093196", "37/37"),
    "alignment_law_probe.run2.log": ("e4cdb9a932093196", "37/37"),
}
DIFF_PAIRS = {
    "bh7": ("bughunt7_probe.run1.log", "bughunt7_probe.run2.log", 0),
    "mi": ("manifold_invariance_probe.run4.log",
           "manifold_invariance_probe.run5.log", 4),
    "l1wpd": ("l1wpd_closure_probe.run1.log",
              "l1wpd_closure_probe.run2.log", 3),
    "dbn": ("dbn_heatflow_probe.run1.log",
            "dbn_heatflow_probe.run2.log", 4),
    "cbj": ("cbj_frame_probe.run1.log", "cbj_frame_probe.run2.log", 2),
    "subdof": ("cbj_subdof_probe.run3.log",
               "cbj_subdof_probe.run4.log", 2),
    "alaw": ("alignment_law_probe.run1.log",
             "alignment_law_probe.run2.log", 2),
}
PROMO_LOGS = {
    "jetmass_floor_probe.promo_rerun.log":
        ("57de8b2a83677a9c", "36/36"),
    "toproot_theta_probe.promo_rerun.log":
        ("cf27df22aa5dffbf", "33/33"),
    "h3_cofinal_probe.promo_rerun.log":
        ("876dafc977d3d8fc", "36/36"),
    "gonek_pricing_probe.promo_rerun.log":
        ("3050678b352eaa9a", "20/20"),
    "thetainf_pin_probe.promo_rerun.log":
        ("3044558e5fa52e01", "28/28"),
}
COMMITS = {"r176": "827d9682", "corr": "9846c2ae", "r177": "59de0afb",
           "r178": "8336a6be", "r179": "c423f0e5", "r180": "d35c104f",
           "r181": "0f2a76c4", "wave5": "4c5b0867", "r182": "2e7e97e1"}
# cited r172 ladder (r171/r172 record strings; BH7 pin replicated OWN)
YT_R172 = {4: 4.2532, 5: 4.7858, 6: 5.1092, 7: 5.4003, 8: 5.6197,
           9: 5.8273, 10: 6.0322, 11: 6.1957, 12: 6.3775, 13: 6.5057,
           14: 6.6664, 15: 6.7625, 16: 6.8847, 17: 6.9876, 18: 7.0996,
           19: 7.1728, 20: 7.2745, 21: 7.3667, 22: 7.4493, 23: 7.5210,
           24: 7.6035, 25: 7.6678, 26: 7.7367, 27: 7.8077, 28: 7.8687}
D_STR = 0.004183
D_ARG = (14, 19)
PRICE_EIGF_TAB = {4: 1.353657e5, 5: 4.696766e5, 8: 2.844554e6,
                  13: 3.820643e7, 16: 9.467704e7}
BSTAR_TAB = {4: -1.1890, 5: -3.3241, 8: -9.3405, 13: -20.6087,
             16: -27.6292}
CSGAP_STR = (6.32, 9.00, 15.79, 28.19, 35.61)
PROVEN_MARGINS = (23.81, 21.68, 15.66, 4.39)
ALPHAS = ("0.5232", "0.3988", "0.4644", "0.4508", "0.4440", "0.4781",
          "0.4858", "0.4860", "0.5111", "0.5190", "0.5223", "0.5092",
          "0.4765", "0.4261")
ALPHA_H = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20)
ALPHA_BAND = (0.38, 0.54)
ALAW_CALIB_FAILS = {"G32-law-ladder", "G34-law-form",
                    "G35-law-predicts-ladder",
                    "G36-eigenvector-anatomy", "G50-tau-screen"}
ALAW_SMOKE1_FAILS = {"G24-linearity-instance-and-witness"}
SUBDOF_CALIB_FAILS = {"G50-tau-screen"}
BH7_SMOKE1_FAILS = {"G13-f4-manifold-scope", "G24-pf2-concavity-own",
                    "G25-pointwise-coverage",
                    "G29-bridge-instrument-own"}
SELECTOR = (7, 13, 31, 61, 127, 251, 509, 1021, 2039, 4093, 8191)
N_K12 = 474
DOF_K12_R8 = 112.8
H_K12_R8 = 512
NOTE_SCOPE = tuple(range(492, 501))
STR_TOL = 5e-3
RUNTIME_BAR = 600.0

CHECKS: list[tuple[str, bool, str]] = []
EDGE_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-38s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok and kind == "edge":
        EDGE_FAILS.append(name)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(t: str) -> None:
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def rd(name: str) -> str:
    return open(os.path.join(HERE, name), "r", encoding="utf-8").read()


def rdr(relpath: str) -> str:
    return open(os.path.join(REPO, relpath), "r",
                encoding="utf-8").read()


def nsp(text: str) -> str:
    """whitespace-normalized copy (BH7 smoke lesson)."""
    return re.sub(r"\s+", " ", text)


def flat(text: str) -> str:
    return re.sub(r"\s+", "", text)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point", "zet" + "a"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        if nm.lower() in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load @%d" % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification") or m.endswith("_probe"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; no z-function use; no np.load; "
                       "no verification/ or frozen-probe import; git "
                       "reads pinned read-only")


# --------------------------------------------------------- own helpers
def spec_sha_of(pyfile: str) -> str:
    doc = ast.get_docstring(ast.parse(rd(pyfile)), clean=False)
    return hashlib.sha256(doc.encode("utf-8")).hexdigest()[:16]


def normalize_timing(text: str, sha: bool = False) -> str:
    text = re.sub(r"\b\d+(?:\.\d+)?\s?s\b", "S", text)
    text = re.sub(r"runtime \S+", "runtime S", text)
    if sha:
        text = re.sub(r"SPEC_SHA [a-f0-9]{16}", "SPEC_SHA X", text)
    return text


def raw_diff_lines(a: str, b: str) -> int:
    la, lb = a.splitlines(), b.splitlines()
    n = sum(1 for x, y in zip(la, lb) if x != y)
    return n + abs(len(la) - len(lb))


def fails_of(logtext: str) -> set:
    return set(re.findall(r"\[FAIL\] (\S+)", logtext))


ROMAN = (("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
         ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
         ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1))


def roman_to_int(s: str) -> int:
    i, v = 0, 0
    while i < len(s):
        for sym, val in ROMAN:
            if s.startswith(sym, i):
                v += val
                i += len(sym)
                break
        else:
            raise ValueError(s)
    return v


def note_line(nxt: str, numeral: str) -> str:
    for line in nxt.splitlines():
        if line.startswith("# ") and ("(%s)" % numeral) in line[:40]:
            return line
    return ""


def git(args: list[str]) -> str:
    return subprocess.run(["git", "-C", REPO] + args,
                          capture_output=True, text=True,
                          check=True).stdout


def prime_powers_upto(n: int):
    comp = bytearray(n + 1)
    out = []
    for p in range(2, n + 1):
        if comp[p]:
            continue
        for m in range(p * p, n + 1, p):
            comp[m] = 1
        q = p
        while q <= n:
            out.append((q, p))
            q *= p
    return out


def and_fire(g: dict, seeds: set) -> set:
    """AND semantics: node fires iff ALL its declared parents fired."""
    parents: dict = {}
    nodes = set(g)
    for u, vs in g.items():
        for v in vs:
            parents.setdefault(u, set())
        parents[u] = set(vs)
        nodes.update(vs)
    fired = set(seeds)
    changed = True
    while changed:
        changed = False
        for n in sorted(nodes - fired):
            ps = parents.get(n)
            if ps and all(p in fired for p in ps):
                fired.add(n)
                changed = True
    return fired


def reachable(g: dict, src: str) -> set:
    seen = {src}
    st = [src]
    while st:
        u = st.pop()
        for v in g.get(u, ()):
            if v not in seen:
                seen.add(v)
                st.append(v)
    return seen


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("bughunt8_probe -- PRIME.BUGHUNT8.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    section("S0  FIREWALL + SOURCES + NUMERALS")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")

    srcs = {k: rd(f) for k, (f, _s) in {**SHAS7, **SHAS5}.items()}
    nxt = open(NEXT, encoding="utf-8").read()
    notes = {n: note_line(nxt, num) for n, num in
             [(492, "CDXCII"), (493, "CDXCIII"), (494, "CDXCIV"),
              (495, "CDXCV"), (496, "CDXCVI"), (497, "CDXCVII"),
              (498, "CDXCVIII"), (499, "CDXCIX"), (500, "D")]}

    heads = re.findall(r"^# \d{4}-\d{2}-\d{2} \(([CDLXVIM]+)\)",
                       nxt, re.M)
    nums = [roman_to_int(h) for h in heads]
    in_scope = [n for n in nums if n in set(NOTE_SCOPE)]
    attrib = {492: "bughunt7_probe.py",
              494: "l1wpd_closure_probe.py",
              495: "manifold_invariance_probe.py",
              496: "dbn_heatflow_probe.py",
              497: "cbj_frame_probe.py",
              499: "cbj_subdof_probe.py",
              500: "alignment_law_probe.py"}
    ok02 = (len(in_scope) == len(set(in_scope))
            and set(NOTE_SCOPE) <= set(in_scope)
            and all(in_scope[i] > in_scope[i + 1]
                    for i in range(len(in_scope) - 1))
            and max(nums) >= 500
            and all(fn in notes[n] for n, fn in attrib.items())
            and all(f in notes[493] for f in
                    ("jetmass_floor_probe.py", "toproot_theta_probe.py",
                     "h3_cofinal_probe.py", "gonek_pricing_probe.py",
                     "thetainf_pin_probe.py"))
            and all(m in notes[498] for m in
                    ("v931_jetmass_floor_theorems.py",
                     "v932_toproot_theta_statement.py",
                     "v933_h3_cofinal_adjudication.py",
                     "v934_gonek_pricing_unconditional.py",
                     "v935_thetainf_landau_bridge.py"))
            and "CDXCII war der Stand" in notes[493]
            and "CDXCIII war der Stand" in notes[494]
            and "CDXCIV" in notes[495] and "CDXCV" in notes[496]
            and "CDXCVI (dBN-Lane) war der Stand" in notes[497]
            and "CDXCVIII (fünfte Promotionswelle) war der Stand"
            in notes[499]
            and "CDXCIX war der Stand" in notes[500])
    check("G02-numerals-x2", ok02,
          "numerals CDXCII..D (492..500) present, unique, strictly "
          "descending, head >= 500 (head %d); every round note names "
          "its probe file; CDXCIII names all five corrected probes; "
          "CDXCVIII names all five promoted modules; every head-"
          "numeral chain disclosure exact: X2 numerals CLEAN"
          % max(nums))

    # ------------------------------------------------- S1 findings
    section("S1  FINDINGS F1-F7 (machine checks)")

    # G10 -- F1 wall identity: class not object
    al_src, l1_src = srcs["alaw"], srcs["l1wpd"]
    al_flat, l1_nsp = flat(al_src), nsp(l1_src)
    walls = {
        "W1-thetainf": ("limsup |A2(c)/A0(c)|/Tz^4 <= 0.155",
                        "classical-evaluation face", "r175"),
        "W2-hpin-oma": ("eps_bar <= poly(x)|A0|sqrt(G) "
                        "(tau/A0^2 cap)", "lambda-uniform", "r178"),
        "W3-subspace": ("sum_(deep i) lam_i s_i^2 control",
                        "per selector rung", "r181"),
        "W4-floorform": ("|N_i(d)|/|A0(d)| >= f(lam_i) per mode",
                         "lambda-uniform", "r182")}
    pairwise_distinct = all(
        walls[a][0] != walls[b][0]
        for a in walls for b in walls if a < b)
    delivered = {
        "GRAM-GEOM": ["CACHE-WARD", "GEOMETRY"],
        "STEPA-EXACT": ["SOURCE", "CACHE-WARD", "CENSUS-PER-K"],
        "PROJ-LINEAR-EXACT": ["GRAM-GEOM"],
        "LAW-MEASURED": ["STEPA-EXACT", "GRAM-GEOM", "SOURCE"],
        "LAW-FORM-FROZEN": ["LAW-MEASURED"],
        "COMPOSED-MARGIN-MEAS": ["LAW-FORM-FROZEN",
                                 "DC-CLASSICAL-PER-CENSUS",
                                 "SIGMA0-CITED"]}
    named_floor = {"LAW-FLOOR-ROUTE": ["A0-FLOOR",
                                       "VARIATIONAL-QUOTIENT-WALL",
                                       "LAW-FORM-FROZEN"]}
    floor_not_delivered = all(
        "LAW-FLOOR-ROUTE" not in reachable(delivered, n)
        for n in delivered)
    ok10 = (pairwise_distinct and floor_not_delivered
            and "A0-FLOOR" in reachable(named_floor, "LAW-FLOOR-ROUTE")
            and 'check("G51-floor-form-same-wall",True,' in al_flat
            and "SAMEnonperturbative-variationalclassastheta_inf"
            in al_flat.replace('"', "")
            and "SAME-WALL-NOT-NEW-OBJECT" in al_flat
            and "same conditioning-walled quotient class as "
                "theta_inf, DISTINCT statement" in l1_nsp
            and "DISTINKTES Statement" in notes[494]
            and "SAME-WALL-NOT-NEW-OBJECT" in notes[500]
            and "eps_bar" not in al_src
            and "0.155" not in al_src
            and "THETA_BAR" not in al_src
            and '"LAW-FLOOR-ROUTE":["A0-FLOOR",'
                '"VARIATIONAL-QUOTIENT-WALL"' in al_flat
            and "EXCLUDED from the delivered set" in nsp(al_src))
    check("G10-f1-wall-class-not-object", ok10,
          "X1 CORE: the four wall statements are pairwise DISTINCT "
          "formal objects (own list); r182's carrying gate G51 is "
          "check(..., True) whose own detail says 'the SAME "
          "nonperturbative-variational CLASS' while the token says "
          "SAME-WALL-NOT-NEW-OBJECT; r178 adjudicates the closest "
          "pair 'same class, DISTINCT statement'; r182 formalizes "
          "NEITHER counterpart (no eps_bar/0.155/THETA_BAR in its "
          "source); the 'no new edge' conclusion survives via the "
          "REAL G44 exclusion (floor route named + delivered-set-"
          "excluded, own DFS): BH8-F1 CONFIRMED [MAJOR, correction "
          "of record, no verdict flip]")

    # G11 -- F2 round-numbering drift (git-pinned)
    subj = {k: git(["show", "-s", "--format=%s", c])
            for k, c in COMMITS.items()}
    ok11 = (all(("round %d" % n) in subj[k] for k, n in
                [("r176", 176), ("r177", 177), ("r178", 178),
                 ("r179", 179), ("r180", 180), ("r181", 181),
                 ("r182", 182)])
            and "corrections of record" in subj["corr"]
            and "round 177" not in subj["corr"]
            and "promotion wave five" in subj["wave5"]
            and "Runde 177/CDXCIII" in notes[498]
            and "Non-Clifford" in notes[498]
            and "die Runden 176–180" in notes[498]
            and "l1wpd" not in notes[498]
            and sum(n.count("Non-Clifford")
                    for n in notes.values()) == 1
            and os.path.exists(os.path.join(
                HERE, "nonclifford_prime_probe.py"))
            and "r176-dBN-Instrumente" in notes[500]
            and "r179" not in notes[500].split(
                "r176-dBN-Instrumente")[0][-200:])
    check("G11-f2-round-numbering-drift", ok11,
          "canonical numbering pinned by the freeze-commit subjects "
          "(176 = bughunt7 .. 182 = alignment; corrections commit "
          "UNNUMBERED); CDXCVIII calls the corrections 'Runde 177/"
          "CDXCIII' and lists rounds 176-180 as 'BH7 + Manifold + "
          "dBN + Non-Clifford + CBJ-Frame' (l1wpd/r178 omitted; "
          "Non-Clifford = the independent session's untracked lane, "
          "exactly ONE mention in next.txt, no numbered note); note "
          "D attributes the dBN instruments to 'r176': BH8-F2 "
          "CONFIRMED [MINOR]")

    # G12 -- F3 vacuous-adjudication-gate scan (own flat-source scan)
    hits = {}
    for k in SHAS7:
        s = flat(srcs[k])
        hits[k] = re.findall(r'check\("(G[0-9a-zA-Z-]+)",True,', s)
    disclosure = {"G60-demand-audit", "G14-law-machinery-predefined",
                  "G54-tau-screen-smoke"}
    nondisc = {k: [h for h in v if h not in disclosure]
               for k, v in hits.items()}
    ok12 = (nondisc["alaw"] == ["G51-floor-form-same-wall"]
            and all(nondisc[k] == [] for k in
                    ("bh7", "mi", "l1wpd", "dbn", "cbj", "subdof"))
            and "orTrue" not in flat(srcs["alaw"])
            and 'check("G45-predef-rehash"' in srcs["alaw"])
    check("G12-f3-vacuous-adjudication-gate", ok12,
          "own flat-source scan of all seven probes: the only "
          "check(..., True) OUTSIDE the house disclosure family "
          "(G60-demand-audit x5, G14 declaration [enforced by the "
          "REAL G45 seal-rehash], smoke-only branches) is r182's "
          "G51-floor-form-same-wall -- the F1 adjudication riding a "
          "gate that cannot fail, inside 37/37: BH8-F3 CONFIRMED "
          "[MINOR, retype DEFINITIONAL/ADJUDICATION]")

    # G13 -- F4 r182 retype timeline (calibration-log reconstruction)
    cal = rd("calib_alaw_pass1.log")
    cal_alphas = dict(re.findall(r'CAL_ALPHA (\d+): "([0-9.]+)"', cal))
    al_ok = (tuple(cal_alphas.get(str(h), "") for h in ALPHA_H)
             == ALPHAS)
    avals = [float(a) for a in ALPHAS]
    band_ok = all(ALPHA_BAND[0] < a < ALPHA_BAND[1] for a in avals)
    wit_ok = ('CAL_WIT 5: ("5.3e-07", "-5.2069", "999.3")' in cal
              and 'CAL_WIT 8: ("8.2e-14", "-3.0214", "1000.9")' in cal)
    m46 = re.search(r"margins \['h7:([0-9.]+)', 'h13:([0-9.]+)'\]",
                    cal)
    ov7 = math.log10(float(m46.group(1)) / 2.14)
    ov13 = math.log10(float(m46.group(2)) / 3.05)
    ov_ok = abs(ov7 - 3.41) <= 0.01 and abs(ov13 - 10.14) <= 0.01
    ok13 = (al_ok and band_ok and wit_ok and ov_ok
            and fails_of(cal) == ALAW_CALIB_FAILS
            and fails_of(rd("alignment_law_probe.smoke1.log"))
            == ALAW_SMOKE1_FAILS
            and 'CAL_OVERSHOOT = {7: "3.41", 13: "10.14"}'
            in srcs["alaw"]
            and "record values below ARE the calibrated numbers"
            in nsp(srcs["alaw"])
            and abs(min(avals) - 0.3988) < 1e-9
            and abs(max(avals) - 0.5232) < 1e-9)
    check("G13-f4-retype-timeline", ok13,
          "r182 retype timeline reconstructed from the PRE-FREEZE "
          "calibration log (SPEC 74dd4432...): the five calibration "
          "FAILs are exactly the five placeholder gates; all 14 "
          "record alphas verbatim as CAL_ALPHA lines (min 0.3988 / "
          "max 0.5232 inside the band drawn at freeze); witness "
          "costs/tails verbatim; frozen overshoots {3.41, 10.14} "
          "derive OWN as log10(calib law-margin / r180 raw margin) "
          "= %.4f/%.4f: NOTHING retyped after record data -- "
          "calibration -> freeze -> record, disclosed; the record "
          "law-gates are REPLICATION-typed ('record values ... ARE "
          "the calibrated numbers'): BH8-F4 CONFIRMED [NOTE, "
          "timeline CLEAN]" % (ov7, ov13))

    # G14 -- F5 note/commit packaging (git-pinned diffs)
    def added_notes(commit: str) -> list:
        out = git(["show", commit, "--", "experiments/next.txt"])
        return re.findall(r"^\+# \d{4}-\d{2}-\d{2} \(([CDLXVIM]+)\)",
                          out, re.M)
    a177 = sorted(roman_to_int(x) for x in added_notes(COMMITS["r177"]))
    a181 = sorted(roman_to_int(x) for x in added_notes(COMMITS["r181"]))
    a182 = [roman_to_int(x) for x in added_notes(COMMITS["r182"])]
    a180 = [roman_to_int(x) for x in added_notes(COMMITS["r180"])]
    a178 = [roman_to_int(x) for x in added_notes(COMMITS["r178"])]
    numstat179 = git(["show", "--numstat", "--format=", 
                      COMMITS["r179"]]).split()
    wave5_next = added_notes(COMMITS["wave5"])
    ok14 = (a177 == [495, 496] and a181 == [498, 499]
            and a182 == [500] and a180 == [497] and a178 == [494]
            and "experiments/tfpt-discovery/dbn_heatflow_probe.py"
            in numstat179
            and "experiments/next.txt" not in numstat179
            and wave5_next == [])
    check("G14-f5-note-commit-packaging", ok14,
          "pinned git diffs: the r177 commit added CDXCV + CDXCVI "
          "(the dBN note rode there; the r179 commit is probe-only, "
          "note-before-probe order); the r181 commit added CDXCIX + "
          "CDXCVIII (wave five's note rode there; the wave-five "
          "surface commit touched no next.txt) -- the CDXCVII -> "
          "CDXCVIII slot is wave-five-owned, positions strictly "
          "descending, content integrity verified via the head "
          "reads: BH8-F5 CONFIRMED [NOTE]")

    # G15 -- F6 residue-form transport
    refined = "H-PIN == die eine"
    coarse = "L1 = TAIL bewiesen + H-pin offen, WPD offen"
    tex3 = rdr("tfpt_3_e8_audit_bootstrap.tex")
    ok15 = (refined in notes[494].replace("DIE EINE", "die eine")
            or "H-PIN == DIE EINE" in notes[494])
    ok15 = (ok15 and refined in notes[497] and refined in notes[499]
            and refined in notes[500]
            and coarse in notes[496]
            and refined not in notes[496]
            and "hier NICHT konsumiert" in notes[495]
            and "{L1, WPD}" in notes[498]
            and "$\\{$L1, WPD$\\}$" in tex3)
    check("G15-f6-residue-form-wobble", ok15,
          "residue transport r176 -> r182: CDXCIV refines the pair "
          "item (H-PIN the one lambda-uniform edge); CDXCV carries "
          "the canonical form + parallel-lane disclosure; CDXCVI "
          "(later than CDXCIV) reverts to the coarse pair form "
          "without that disclosure; CDXCVII/CDXCIX/D adopt the "
          "refined form; wave five carries the CDXCIII canonical "
          "form (correct for the promoted 171-175 arc): BH8-F6 "
          "CONFIRMED [NOTE, cardinality-identical wobble]")

    # G16 -- F7 price ladder measured-vs-proven split (own arithmetic)
    gaps = []
    margins = []
    for h in (4, 5, 8, 13, 16):
        gaps.append(math.log10(PRICE_EIGF_TAB[h]) - BSTAR_TAB[h])
    for h in (4, 5, 8, 13):
        margins.append(BSTAR_TAB[h] + 25.0)
    meas = [math.log10(PRICE_EIGF_TAB[h]) + 25.0
            for h in (4, 5, 8, 13, 16)]
    mi_nsp = nsp(srcs["mi"])
    ok16 = (all(abs(g - s) <= 0.02 for g, s in zip(gaps, CSGAP_STR))
            and all(abs(m - s) <= 0.02
                    for m, s in zip(margins, PROVEN_MARGINS))
            and all(30.0 <= m <= 33.05 for m in meas)
            and "30-33 ORDERS ABOVE THE 1e-25 BAR" in mi_nsp
            and "first-order optimality of the price minimum"
            in mi_nsp
            and "GEMESSEN" in notes[495]
            and "NOT FINITE at h = 16" in mi_nsp)
    check("G16-f7-price-measured-vs-proven", ok16,
          "own arithmetic from the frozen tabs: CS-gaps "
          "log10(price) - log10(b*) = %s == spec strings (abs "
          "0.02); the PROVEN b*-schedule margins above the 1e-25 "
          "bar are only %s orders at h = 4/5/8/13 (none at h >= "
          "16), the measured ladder margins are %s: the 30-33 "
          "figure is measured-first-order (honestly typed GEMESSEN "
          "+ scope-disclosed on every surface; the delivered DK "
          "theorem is ladder-independent): BH8-F7 CONFIRMED [NOTE, "
          "pair the two numbers in external citation]"
          % (["%.2f" % g for g in gaps],
             ["%.2f" % m for m in margins],
             ["%.1f" % m for m in meas]))

    # --------------------------------------------- S2 re-checks
    section("S2  CROSS-ROUND RE-CHECKS (X1-X5 + audit-the-auditor)")

    # G20 -- X3 SPEC_SHA integrity + correction blocks
    ok20 = True
    d20 = []
    for k, (f, want) in {**SHAS7, **SHAS5}.items():
        got = spec_sha_of(f)
        if got != want:
            ok20 = False
            d20.append("%s %s != %s" % (k, got, want))
    blocks = {k: srcs[k] for k in SHAS5}
    mark = "# CORRECTION OF RECORD (Bughunt VII, note CDXCII"
    def blk(k):
        s = blocks[k]
        i = s.find(mark)
        return s[i:i + 3000] if i >= 0 else ""
    okb = (all(mark in blocks[k] for k in SHAS5)
           and "BH7-F3" in blk("jmf") and "BH7-F1" not in blk("jmf")
           and "BH7-F1" in blk("tt") and "BH7-F4" not in blk("tt")
           and "BH7-F1" in blk("h3c") and "BH7-F4" in blk("h3c")
           and "BH7-F1" in blk("gp")
           and all(x in blk("tip") for x in
                   ("BH7-F1", "BH7-F2", "BH7-F7"))
           and all(("BH7-F%d" % n) not in blk(k)
                   for n in (5, 6, 8) for k in SHAS5)
           and all(SHAS5[k][1] in blk(k) for k in SHAS5))
    ok20 = ok20 and okb
    check("G20-x3-spec-sha-and-corrections", ok20,
          "all 12 SPEC_SHAs recomputed from the docstrings == "
          "claimed (7 round probes + 5 corrected r171-r175 probes: "
          "the correction blocks live OUTSIDE the hashed docstrings, "
          "byte-integrity machine-confirmed); block placement "
          "faithful to CDXCIII (F1 on r172/r173/r174/r175, F3 on "
          "r171 only, F4 on r173 only, F2/F7 on r175 only, F5/F6/F8 "
          "note-only), every block quotes its unchanged SHA: X3 "
          "CLEAN%s" % ("" if ok20 else " [" + "; ".join(d20) + "]"))

    # G21 -- lineage table + determinism (own diffs)
    ok21 = True
    d21 = []
    for lg, (sha, gates) in sorted(LOG_TAB.items()):
        t = rd(lg)
        m = re.search(r"SPEC_SHA ([a-f0-9]{16})", t)
        g = re.findall(r"GATES: (\d+/\d+) PASS", t)
        if not m or m.group(1) != sha or not g or g[-1] != gates:
            ok21 = False
            d21.append(lg)
    for k, (a, b, want_raw) in sorted(DIFF_PAIRS.items()):
        ta, tb = rd(a), rd(b)
        rdf = raw_diff_lines(ta, tb)
        ndf = raw_diff_lines(normalize_timing(ta), normalize_timing(tb))
        if rdf != want_raw or ndf != 0:
            ok21 = False
            d21.append("%s raw %d norm %d" % (k, rdf, ndf))
    r1, r3 = rd("cbj_subdof_probe.run1.log"), rd(
        "cbj_subdof_probe.run3.log")
    a1_cross = raw_diff_lines(normalize_timing(r1, sha=True),
                              normalize_timing(r3, sha=True))
    ok21 = ok21 and a1_cross == 0
    for lg, (sha, gates) in PROMO_LOGS.items():
        t = rd(lg)
        if (sha not in t) or (("GATES: %s PASS" % gates) not in t):
            ok21 = False
            d21.append(lg)
    check("G21-lineage-determinism", ok21,
          "all 30 kept smoke/calib/run logs match the disclosed "
          "SHA/gate lineage; all seven record pairs re-diffed OWN "
          "(raw 0/4/3/4/2/2/2, timing-normalized EMPTY); the r181 "
          "A1 spec-text amendment verified output-IDENTICAL (run1 "
          "vs run3, +SHA-normalized, diff 0: nothing executable "
          "moved); all five promo_rerun logs green at the record "
          "SHAs with record gate counts%s"
          % ("" if ok21 else " [" + "; ".join(d21) + "]"))

    # G22 -- audit the auditor: BH7 re-verified OWN
    th = {h: 10 ** v / (2 * math.pi * h) ** 4
          for h, v in YT_R172.items()}
    hs = sorted(th)
    D, arg = 0.0, None
    for i, h in enumerate(hs):
        for hp in hs[i + 1:]:
            d = th[h] - th[hp]
            if d > D:
                D, arg = d, (h, hp)
    bar = 2.0
    seq = [bar - 0.2 if i % 2 == 0 else bar + 0.9 for i in range(40)]
    cofinal = all(any(seq[j] <= bar for j in range(2 * k, 2 * k + 2))
                  for k in range(20))
    limsup_tail = max(seq[20:])
    chain = {"PF_DEEP": ["H1_DEEP", "H2_DEEP", "TRACE"],
             "WF_DEEP": ["GONEK_PRICED", "CENSUS_PER_K"],
             "RATE_DEEP": ["H3_DEEP", "RATE_DICT"],
             "JETMASS_DEEP": ["PF_DEEP", "WF_DEEP", "RATE_DEEP"],
             "SIGMAFLOOR_DEEP": ["JETMASS_DEEP"],
             "DTSTEP_DEEP": ["SIGMAFLOOR_DEEP"],
             "HCOF": ["DTSTEP_DEEP"]}
    grants_prose = {"H3_DEEP", "RATE_DICT", "GONEK_PRICED",
                    "CENSUS_PER_K", "TRACE"}
    fired_prose = and_fire(chain, grants_prose)
    fired_full = and_fire(chain, grants_prose | {"H1_DEEP", "H2_DEEP"})
    ok22 = (abs(D / D_STR - 1) <= STR_TOL and arg == D_ARG
            and cofinal and limsup_tail > bar
            and "JETMASS_DEEP" not in fired_prose
            and "HCOF" in fired_full
            and raw_diff_lines(rd("bughunt7_probe.run1.log"),
                               rd("bughunt7_probe.run2.log")) == 0
            and fails_of(rd("bughunt7_probe.smoke1.log"))
            == BH7_SMOKE1_FAILS
            and "BUGHUNT7-FINDINGS(8: 1 MAJOR / 3 MINOR / 4 NOTE)"
            in notes[492])
    check("G22-bh7-reverified", ok22,
          "AUDIT THE AUDITOR: own drawdown recompute from the cited "
          "r172 ladder D = %.6f at %s (BH7-F2 string rel 5e-3); own "
          "bar-cofinal-with-limsup>bar counterexample (different "
          "numbers); own AND-fire re-demonstration of BH7-F1 (prose "
          "grant set does NOT fire the deep floor, + {H1, H2} fires "
          "HCOF); BH7 run1/run2 raw diff 0 == the CDXCII claim; "
          "smoke1 fail set exactly the four disclosed instrument "
          "bugs: BUGHUNT7 CORRECT" % (D, str(arg)))

    # G23 -- wave five adoption verbatim
    v = {n: rdr("verification/" + f) for n, f in
         [(931, "v931_jetmass_floor_theorems.py"),
          (932, "v932_toproot_theta_statement.py"),
          (933, "v933_h3_cofinal_adjudication.py"),
          (934, "v934_gonek_pricing_unconditional.py"),
          (935, "v935_thetainf_landau_bridge.py")]}
    tex3n = nsp(tex3)
    pf = nsp(rdr("tfpt_prime_front.tex"))
    ok23 = (all("H1 AND H2 AND H3" in nsp(t) for t in v.values())
            and "DEFINITIONAL per the BH6-F3 convention" in nsp(v[931])
            and "D = 0.004183" in nsp(v[933])
            and "SCOPED to the DK radius" in nsp(v[933])
            and "gated h <= 13, measured to h = 20" in nsp(v[933])
            and "MEASURED-LAW EXTRAPOLATION" in nsp(v[935])
            and tex3n.count("H1 $\\wedge$ H2 $\\wedge$ H3") >= 3
            and "scoped to the DK radius" in tex3n
            and "mod the measured defect $D = 0.004183$" in tex3n
            and "measured-law" in tex3n
            and pf.count("H1 $\\wedge$ H2 $\\wedge$ H3") >= 2)
    check("G23-wave5-adoption", ok23,
          "wave-five surfaces adopt the BH7 corrections verbatim: "
          "all five modules carry the {H1 AND H2 AND H3} triple; "
          "v931 the F3 DEFINITIONAL retype; v933 the F2 mod-D "
          "qualifier + the F4 DK-radius scoping; v935 the F7 "
          "measured-law typing; tfpt_3 carries triple(x3+) + mod-D "
          "+ DK-scope + measured-law in the five veri blocks; "
          "tfpt_prime_front carries the triple twice: "
          "ADOPTION-VERBATIM CONFIRMED")

    # G24 -- r177 amendments legitimate + monotone-safe + DK scope
    import sympy as sp
    tau_s, off_s, z_s = sp.symbols("tau_s off_s z_s", positive=True)
    resid = (tau_s + off_s - z_s) / tau_s
    mono = sp.simplify(sp.diff(resid, z_s) + 1 / tau_s) == 0
    mi_r1 = rd("manifold_invariance_probe.run1.log")
    mi_r2 = rd("manifold_invariance_probe.run2.log")
    mi_r3 = rd("manifold_invariance_probe.run3.log")
    ok24 = (mono
            and fails_of(mi_r1) == {"G41-zmin-universal"}
            and fails_of(mi_r2) == {"G41-zmin-universal"}
            and fails_of(mi_r3) == {"G41-zmin-universal"}
            and "zmin/zm 2.065e+11" in mi_r1
            and "ba3min -1.918e+11" in mi_r1
            and "zmin/zm 3.394e-09" in mi_r2
            and "1.77e-02" in mi_r3
            and "FEASIBLE-UPPER-VALUE-OF-THE-MINIMUM" in nsp(srcs["mi"])
            and "MONOTONE in this upper value" in nsp(srcs["mi"])
            and "covers h <= 13 at frozen bar" in nsp(srcs["mi"])
            and "gegated h <= 13, gemessen bis h = 20"
            in nsp(srcs["h3c"]))
    check("G24-r177-amendments-monotone-safe", ok24,
          "r177 amendment lineage gate-exact (run1/2/3 fail EXACTLY "
          "G41; the A1/A2/A3 story numbers verbatim in the kept "
          "logs); the A3 retype is MONOTONE-SAFE own-checked: "
          "d/dz[(tau + OFF - z)/tau] == -1/tau < 0, so a smaller "
          "true minimum only INCREASES the BA3 residual, and the "
          "BA3-PASSING-REFUTER-EXISTS claim needs only the exhibited "
          "feasible point with its measured residual; the DK scope "
          "split (proven h <= 13 at the frozen bar / measured to "
          "h = 20 / h = 24 uncovered) carried on spec + note + "
          "correction block + v933: AMENDMENTS LEGITIMATE")

    # G25 -- r178 WPD == H-pin demonstrated + collision downstream
    rules = {"HPIN": ["EPSLOCK-G", "SPACREM-G", "H123M-COUNTS"],
             "WPD-BATTERY": ["HPIN", "THEOREM-A", "DCS-357"],
             "PF": ["ENVJ-H1", "CENSUS-H2", "TRACE"],
             "WF": ["GONEK-PRICED", "CENSUS-PER-K"],
             "RATE": ["QUARTIC-H3", "RATE-DICT"],
             "HCOF": ["PF", "WF", "RATE"]}
    pin_grants = {"EPSLOCK-G", "SPACREM-G", "H123M-COUNTS",
                  "THEOREM-A", "DCS-357"}
    jet_grants = {"ENVJ-H1", "CENSUS-H2", "TRACE", "QUARTIC-H3",
                  "RATE-DICT", "GONEK-PRICED", "CENSUS-PER-K"}
    f_pin = and_fire(rules, pin_grants)
    f_jet = and_fire(rules, jet_grants)
    down_clean = all("Theorem M" not in srcs[k]
                     for k in ("dbn", "cbj", "subdof", "alaw"))
    down_clean = down_clean and all(
        "Theorem M" not in t for t in v.values())
    ok25 = ("WPD-BATTERY" in f_pin and "HCOF" not in f_pin
            and "HCOF" in f_jet and "HPIN" not in f_jet
            and "WPD-BATTERY" not in f_jet
            and down_clean
            and "NAME COLLISION" in nsp(srcs["l1wpd"])
            and "x_0(HSW) == 121 AND x_0(BW25) == 112"
            in nsp(srcs["l1wpd"])
            and "ALL 357 cells" in nsp(srcs["l1wpd"])
            and "NAMENSKOLLISION offengelegt" in notes[494])
    check("G25-r178-wpd-hpin-and-collision", ok25,
          "own AND-fire on the r178-declared edges: the pin grants "
          "{EPSLOCK, SPACREM, H123M, THEOREM-A, DCS-357} fire HPIN "
          "-> WPD-BATTERY; the jet-triple grants fire PF/WF/RATE/"
          "HCOF but NOT HPIN/WPD (both directions distinct); the "
          "two load-bearing edges (Theorem A x_0 = 121/112, 357 "
          "D_cs cells) were replicated in-round: the consolidation "
          "is DEMONSTRATED-AT-DECLARED-EDGES, middle-a and tail "
          "legs carried separately; NAME COLLISION disclosed in "
          "r178 and CLEAN downstream (no r133 ball-matching family "
          "use in rounds 179-182 or v931-v935): CLEAN")

    # G26 -- r179 own exact layer + citation pins
    zz, ww, tt_ = sp.symbols("zz ww tt_", positive=True)
    a0, a1_, a2_, a3_, a4_ = sp.symbols("a0 a1 a2 a3 a4", real=True)
    p = a0 + a1_ * zz + a2_ * zz ** 2 + a3_ * zz ** 3 + a4_ * zz ** 4

    def heat(q, var, tv):
        out = q
        term = q
        for m in range(1, 5):
            term = sp.diff(term, var, 2)
            out = out + (-tv) ** m / sp.factorial(m) * term
        return sp.expand(out)
    lhs = heat(p, zz, tt_).subs(zz, 2 * ww)
    rhs = heat(p.subs(zz, 2 * ww), ww, tt_ / 4)
    fac4 = sp.simplify(sp.expand(lhs - rhs)) == 0
    # drift toy: gammas rational, x-zeros = {+-2g}; v_gamma == formula
    gs = [sp.Rational(1), sp.Rational(3, 2), sp.Rational(2)]
    x1 = 2 * gs[0]
    xs = [2 * g for g in gs] + [-2 * g for g in gs]
    vx = sum(sp.Rational(2) / (x1 - xk) for xk in xs if xk != x1)
    vg_form = sum(4 * gs[0] / (gs[0] ** 2 - gk ** 2)
                  for gk in gs[1:]) + 1 / gs[0]
    drift_ok = sp.simplify(2 * vx - vg_form) == 0
    # trace law own: quartic in y, T = 4y d^2 + 2 d
    yv = sp.symbols("yv", positive=True)
    b0, b1_, b2_, b3_ = sp.symbols("b0 b1 b2 b3", real=True)
    N = yv ** 4 + b3_ * yv ** 3 + b2_ * yv ** 2 + b1_ * yv + b0

    def Top(q):
        return sp.expand(4 * yv * sp.diff(q, yv, 2) + 2 * sp.diff(q, yv))
    Nt = N
    term = N
    for m in range(1, 5):
        term = Top(term)
        Nt = Nt + (-tt_) ** m / sp.factorial(m) * term
    Nt = sp.expand(Nt)
    tr0 = -b3_
    trt = -sp.Poly(Nt, yv).coeff_monomial(yv ** 3)
    trace_ok = sp.simplify(trt - (tr0 + 56 * tt_)) == 0
    dbn_n = nsp(srcs["dbn"])
    ok26 = (fac4 and drift_ok and trace_ok
            and "0.22/4 = 0.055" in dbn_n
            and "Res. Math. Sci. 6, 31" in dbn_n
            and "Forum Math. Pi 8, e6" in dbn_n
            and "not a claimed identity" in dbn_n
            and "transported EXACTLY to the derived census polynomial"
            in dbn_n)
    check("G26-r179-factor4-drift-trace-own", ok26,
          "r179 exact layer re-derived OWN: the polynomial heat "
          "operator satisfies E_t[p](2w) == E_{t/4}[p(2.)](w) on a "
          "generic quartic (factor-4 lemma; Polymath15 normalization "
          "web-pinned: H_t = int e^{tu^2} Phi cos(zu) du, Lambda <= "
          "0.22 unconditional, zeros at x = 2 gamma -- 0.22 is the "
          "CONSERVATIVE window, the 2020 improvement to 0.2 only "
          "strengthens every kill ratio); the gamma-unit drift "
          "formula equals the transported mirrored-zero ODE on an "
          "exact rational 3-zero toy (the factor 4 threads the "
          "drift); trace slope == 2d(2d-1) == 56 own; FLOW-P scoped "
          "to the DERIVED polynomial and FLOW-S typed DEFINED-AS-"
          "FORM in the spec itself: CLEAN")

    # G27 -- r180 own arithmetic: sieve/dof/MV/selector/Bertrand
    pps = prime_powers_upto(2 ** 19)
    blk12 = [(q, pr) for q, pr in pps if 2 ** 12 < q <= 2 ** 13]
    n12 = len(blk12)
    lams = sorted(math.log(q) for q, _p in blk12)
    span = lams[-1] - lams[0]
    dof = span * H_K12_R8 / math.pi
    link = sp.Rational(63, 20) * sp.pi
    mv_ratio = sp.simplify(3 * sp.pi / link)
    mv_margin = sp.simplify(1 - mv_ratio)
    Hs = sp.symbols("Hs", positive=True)
    link1_neg = sp.simplify(Hs * (1 - 3 * sp.pi)) \
        .subs(Hs, 1) < 0
    sel = []
    nonempty17 = True
    for k in range(2, 18):
        atoms = [q for q, pr in pps
                 if 2 ** k < q <= 2 ** (k + 1) and pr != 2]
        if not atoms:
            nonempty17 = False
        elif k <= 12:
            sel.append(max(atoms))
    cbj_n = nsp(srcs["cbj"])
    ok27 = (n12 == N_K12
            and abs(dof / DOF_K12_R8 - 1) <= 2e-2
            and mv_ratio == sp.Rational(20, 21)
            and mv_margin == sp.Rational(1, 21)
            and bool(link1_neg)
            and tuple(sel) == SELECTOR and nonempty17
            and "an odd prime lies in (2^k, 2^{k+1})" in cbj_n
            and "min over clusters of lam_min(B_C^T G_CC B_C)" in cbj_n
            and "min over clusters of lam_min(G_CC)" in cbj_n)
    check("G27-r180-sieve-dof-mv-bertrand", ok27,
          "own sieve: block k = 12 has n == %d prime-power atoms "
          "(claimed 474); own dof = span x H/pi == %.1f at H = 512 "
          "(claimed 112.8; the length-2H window makes span x 2H/"
          "(2 pi): NO off-by-2pi); own exact rationals: 3 pi/(63 pi"
          "/20) == 20/21, MV margin == 1/21, link-1 budget H(1 - "
          "3 pi) < 0; own selector ladder k = 2..12 == %s, nonempty "
          "through k = 17, Bertrand sufficient (any Bertrand prime "
          "in (2^k, 2^{k+1}) is odd for k >= 2, a valid non-2-power "
          "atom); c_intra/c_point defined on the SAME clusters and "
          "G_CC (like-with-like; jet-convention covariance of the "
          "107-dex rescue disclosed in the round's own lever (a)): "
          "CLEAN" % (n12, dof, str(sel)))

    # G28 -- r181: A1 + FEJ1 1/6 + OCS + cut predefinition
    xq = sp.symbols("xq", real=True)
    fej = (sp.sin(xq / 2) / (xq / 2)) ** 2
    ser = sp.series(fej, xq, 0, 4).removeO()
    c2 = ser.coeff(xq, 2)
    fpp0 = 2 * c2
    fej_ok = (sp.simplify(c2 + sp.Rational(1, 12)) == 0
              and sp.simplify(fpp0 + sp.Rational(1, 6)) == 0)
    sd_flat = flat(srcs["subdof"])
    sd_nsp = nsp(srcs["subdof"])
    ok28 = (fej_ok
            and fails_of(rd("calib_subdof_pass1.log"))
            == SUBDOF_CALIB_FAILS
            and "1/12 statt sympy-exakt 1/6" in notes[499]
            and "diag(1, 1/6) FEJ1" in sd_nsp
            and 'CUTS=("1e-6","1e-12","1e-24")' in sd_flat
            and "seal_src=repr(sel)+repr(fam)+repr(CUTS)+CUT_PRIMARY"
            in sd_flat
            and "Ann. of Math. (2) 155 (2002), no. 3, 789-806"
            in sd_nsp
            and "EQUIVALENT TO THE UPPER INEQUALITY ONLY" in sd_nsp)
    check("G28-r181-a1-fej-ocs-cut", ok28,
          "own sympy: for What == sinc^2(x/2) the series coefficient "
          "is -1/12 and -What''(0) == 1/6 -- the A1 amendment "
          "corrects a real transcription slip (and G21 verified the "
          "amendment moved NOTHING executable: run1 vs run3 "
          "output-identical); the subdof calibration fail set is "
          "exactly the disclosed placeholder tau-window; the 1e-12 "
          "cut is PREDEFINED on the source-free Gram spectrum and "
          "sealed pre-ward (seal includes CUTS; end-rehash gated "
          "in-round); the OCS02 citation (Ann. of Math. (2) 155 "
          "(2002), no. 3, 789-806) and its direction (box condition "
          "== UPPER inequality only) web-verified 2026-08-20: CLEAN")

    # G29 -- X5 measured-carries chain of custody
    cbj_r1 = rd("cbj_frame_probe.run1.log")
    sd_r3 = rd("cbj_subdof_probe.run3.log")
    al_r1 = rd("alignment_law_probe.run1.log")
    ok29 = ("margins delta/delta_req = 2.14 (h-hat 7) / 3.05 "
            "(h-hat 13)" in cbj_r1
            and "min over all rungs 1.40 >= 1.35" in cbj_r1
            and "min margin 1.405 at h = 4" in nsp(srcs["cbj"])
            and "1.405" in sd_r3 and "8.020e-03" in sd_r3
            and "1.142" in sd_r3
            and "['h7:2.14', 'h13:3.05']" in al_r1
            and "delta_req = SIGMA0/((1-slop) DC)" in nsp(srcs["cbj"])
            and "delta_req = SIGMA0/((1-slop) DC" in nsp(srcs["subdof"])
            and "delta_req = SIGMA0/((1-slop) DC)" in nsp(srcs["alaw"])
            and "SIGMA0 = 0.15" in srcs["cbj"]
            and "UNSCOPED-FLOOR-STILL-CARRIES-MEASURED" in notes[499])
    check("G29-x5-measured-carries-custody", ok29,
          "chain of custody: r180 MEASURES the unscoped floor "
          "(selector margins 2.14/3.05, min 1.405) on WFULL/"
          "gamma_7000 with the r169 SF1/SF2 recipe; r181 RE-MEASURES "
          "the same demand on the same instrument (its margin_sub "
          "table carries 1.405/1.142/8.020e-03 -- the sub-dof kill "
          "is a DIFFERENT scoped quantity, the unscoped carrier "
          "cited-not-stale); r182 RE-MEASURES the selector margins "
          "fresh (['h7:2.14', 'h13:3.05'] in its record log) and "
          "gates them against the replicated r180 strings: same "
          "frozen instrument, three independent measurements, "
          "NOTHING STALE: X5 CLEAN")

    # ------------------------------------------------ S9 verdict
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "BUGHUNT8-FINDINGS(7: 1 MAJOR / 2 MINOR / 4 NOTE)",
        "WALL-IDENTITY-CLASS-NOT-OBJECT(F1/X1: four distinct formal "
        "statements, one shared source object + quotient shape; "
        "correction of record on the r182/D surfaces)",
        "NO-NEW-EDGE-SURVIVES-VIA-EXCLUSION(X1: G44 ground, not "
        "identity)",
        "ROUND-NUMBERING-DRIFT(F2: CDXCVIII 'Runde 177' + "
        "'Non-Clifford' list; note D 'r176-dBN')",
        "VACUOUS-ADJUDICATION-GATE(F3: r182 G51 check-True)",
        "RETYPE-TIMELINE-CLEAN(F4: calibration -> freeze -> record)",
        "CROSS-RIDINGS-VERIFIED(F5/X2)",
        "RESIDUE-FORM-WOBBLE(F6/X4: CDXCVI coarse form)",
        "PRICE-LADDER-MEASURED-VS-PROVEN-SPLIT(F7: 30-33 measured "
        "vs 23.8/21.7/15.7/4.4 proven)",
        "CORRECTIONS-FAITHFULLY-APPLIED(r176) + "
        "WAVE-FIVE-ADOPTION-VERBATIM",
        "BH7-REVERIFIED-CORRECT(r176)",
        "AMENDMENTS-LEGITIMATE-MONOTONE-SAFE(r177)",
        "NAME-COLLISION-CLEAN-DOWNSTREAM + "
        "WPD-HPIN-CONSOLIDATION-DEMONSTRATED(r178)",
        "FACTOR-4-CORRECT(r179)", "DOF-MV-BERTRAND-CORRECT(r180)",
        "A1-CLEAN-FEJ1-ONE-SIXTH(r181)",
        "NUMERALS-CLEAN(X2)", "LINEAGE-CLEAN(X3)",
        "RESIDUE-TRANSPORT-CONSISTENT(X4)",
        "MEASURED-CARRIES-CUSTODY-CLEAN(X5)",
        "LITERATURE-PINS-EXACT"]
    for vv in verdicts:
        print("  " + vv)
    info("NO verdict of rounds 176-182 flips; corrections of record "
         "proposed at F1/F2 wording, F3 gate retype, F4/F7 citation "
         "typing.")
    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: " + " + ".join(vv.split("(")[0]
                                     for vv in verdicts))
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if npass == len(CHECKS) and not EDGE_FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
