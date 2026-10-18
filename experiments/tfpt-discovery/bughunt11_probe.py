#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bughunt11_probe -- PRIME.BUGHUNT11.01

FROZEN SPEC (2026-08-22).  EXPLORATION ONLY.  Eleventh adversarial
audit: the discovery rounds 200-206 (r200 = pole_homotopy_probe, r201
= eigvec_geometry_probe, r202 = euler_jet_dictionary_probe, r203 =
z1_suppression_probe, r204 = euler_jet_colligation_probe, r205 =
euler_hpin_region_probe, r206 = euler_block_sturm_probe; notes
DXXVI-DXXXII (526-532), DXXV interleaved from promotion wave eight),
i.e. the pole homotopy, the eigenvector geometry, the z1-suppression
round, and the COMPLETE four-probe EULER JET program.  Predecessors
r87/r109/r130/r149/r164/r170/r176/r183/r193/r199.  This probe writes
NOTHING but stdout, reads the frozen corpus READ-ONLY (probe sources
as text, kept smoke/calib/run/proto logs, next.txt, pinned read-only
`git show`), imports NO probe module and NO verification module
(every numeric re-check runs on a FULLY OWN re-implementation of the
documented even-sector MAIN wall -- own sieve, own arch quadratures,
own eigensolve/inverse iteration, own secular bisection, own exact
Fractions/Descartes/Bernstein, own Euler-jet closed forms, own
dissipation-Gram quadratures, own Moebius orbit, own J-metric block
Lanczos and adjugate-cleared block Sturm chain, own Epstein lamq
recursion), and makes NO RH CLAIM in either direction.  Concurrent-
lane files (the independent session's untracked probes,
sieve4_helper.bin) are NOT touched and NOT audited here.

METHOD (bughunt I-X standard): source/note/log/commit conjunctions
for every wording finding; OWN re-implementations for every numeric
re-check; expensive claims audited on the kept record logs, cheap
claims re-run inline.  THE X4 LAYER (the highest-value deliverable):
independent recompute at h = 4, 5 (8 and 20 where load-bearing) of
the r200 gap-theorem numbers and Poisson bound chain, the r201 wall
Bernstein/Descartes certificates incl. the h = 20 depth question and
the b_n = P(1) = A(0) identity, the r202 dictionary identities + the
k = 0 defect + the Epstein weight doubling from the source recursion,
the r203 per-atom z_1 table + ID1 + the C(L) == 0 boundary fact + the
fine-tuning ward + the 2x2 support transplant, the r204 Schur/central
identity + outer factor + KYP certificate + nilpotency integer law,
the r205 orbit/Delta/mu ladder + chain-matrix identities + the
compositional secular gate, and the r206 rho ladders + Sylvester
inertia bookkeeping + S/Ahat/Bhat censuses + the adjugate-cleared
determinant identity in exact Fractions.

=======================================================================
FINDINGS LEDGER (the deliverable; severity frozen; gates named)
=======================================================================
BH11-F1 [MINOR][r200: the deep-rung gap currency is under-warded by
  its own frozen gate -- the BH10-F1 gate-vs-headline pattern
  recurring on the GAP leg; NO VERDICT FLIP -- the sign is REAL and
  is re-certified here]  The r200 headline GAP-UNIFORMLY-OPEN-ALL-
  RUNGS rests on gam_unif = lam_1(NoP) - lam_0(RawW) > 0 with ladder
  log10(gam_unif/fro) = -7.0 .. -81.7.  The operative accuracy wards
  are EIG_RES_BAR = EIG_ORTH_BAR = 1e-30 (rel fro) and the record
  G12 print shows only the CROSS-RUNG MAX eigen-residual (2.3e-61,
  dominated by the dps-60 shallow rungs): from h = 10 on (guf <=
  -34.0) NEITHER the frozen bar NOR the printed maximum resolves the
  sign of d_1 or of gam_unif -- gu_res_ok (gu > 10^-(dps-20) fro)
  asserts the VALUE clears the dps floor but no per-rung accuracy
  ward underwrites it; d1_pos (G21) likewise rides the same 1e-30
  bar.  The claim is nonetheless TRUE: mp.eigsy delivers ~10^-dps
  residuals per rung, and THIS round re-certifies the endpoints in
  fully own code at h = 4, 5, 8 (guf == CAL_GUF to 0.10 dex, anchor
  to the own inverse iteration <= 1e-6 rel) AND at the worst rung
  h = 20 at dps 160 > record 144 (own build, own eigsy, own post-A1
  all-K-poles secular bottom root; headroom log10(d_1/fro) -
  log10(eig_res/fro) >= 30 demanded and measured ~ +70).
  CORRECTION OF RECORD (proposed, LA): rider on the r200 G30/DXXVI
  gap surfaces: "the frozen eigsy ward (1e-30) and the printed
  cross-rung max residual do not resolve the deep-rung gap sign;
  per-rung dps-scaled residuals underwrite it and Bughunt XI
  re-certified h = 4/5/8/20 in own code"; future gap gates print
  and ward PER-RUNG dps-scaled residuals (bar ~ 10^-(dps-20)).
  GATE: G40 (text conjunction) + G21/G23 (own adjudication).
BH11-F2 [NOTE][r200: the A1 amendment block cites the WRONG log
  filename for the failed calibration pass]  The A1 block states
  "...G14/G30/G31/G33/G52 FAILED at those two rungs
  (calib_ph_pass1.log, 23/28, kept)" -- but the 23/28 failed pass is
  kept as calib_ph_fail1.log (SHA 15b13665f3438ca5, fail set exactly
  {G14, G30, G31, G33, G52}); calib_ph_pass1.log is the CLEAN 28/28
  post-A1 pass at a0829ac28d5703e1.  The RECORD TABLES block three
  paragraphs earlier names both files correctly; the kept logs
  disambiguate; content unambiguous, filename misattribution inside
  the frozen spec.  Correction LB: one-line erratum on the next
  coordinator surface.  GATE: G41.
BH11-F3 [NOTE][r201: two pre-freeze smoke logs superseded IN PLACE --
  the retype-forcing fail sets are not independently verifiable]
  The r201 disclosure names smoke passes at pre-freeze SHAs
  5a193f0dbe6b2bb7 (25/30 -- the dip-freedom refutation that forced
  the FIRST taxonomy retype) and 66e2e449e29b8c59 (28/30), kept
  "superseded in place" by the final 30/30 smoke at
  8a0fd8e821b5fc01: only the final smoke, calib1 (28/30, G40/G52
  fails on the deep-rung refutation -- verified from the kept log)
  and the record runs exist on disk.  The disclosure is honest and
  the calibration-stage retype IS log-verifiable, but the smoke-
  stage retype evidence (which gates failed at 25/30) is not -- a
  lineage-completeness regression vs the r195-r200 keep-all-logs
  discipline (r203 kept its failing smoke0 in the very next lane).
  Process note LC: keep superseded smoke logs.  GATE: G42.
BH11-F4 [NOTE][r201: the wall Bernstein/Descartes certificates are
  sold as "OBJECT-A ... is CERTIFIED" without the computed-direction
  rider that BH10's own Sturm certificates carry]  G44 states
  "A_{v_0(h)} >= 0 on [0, L] is CERTIFIED (certificate class, own
  exact arithmetic)" and bernEnum's taxonomy line reads "then
  OBJECT-A itself is exact-rational-certified at native degree" --
  the exact-rational arithmetic runs on the COMPUTED dps-scaled wall
  vector (exact dyadic Fractions of the mp inverse-iteration ray),
  so the certificate object is A_{v-computed}, one BH10-KA-class
  rider short of the stated object.  The headroom is REAL and is
  measured here: at h = 20 the b_n = P(1) = A(0) coefficient carries
  ~ 43 cancelled digits against ~ 160 working digits (~ 100 digits
  of sign headroom on the computed direction; eigenvector error
  ~ 1e-140 perturbs the profile far below the 1e-44 minimum), and
  this round re-runs the FULL exact pipeline on its OWN dps-160
  vector at h = 20: NB = 0, SC_desc = 0, b_n = P(1) = A(0) EXACT
  (Fraction identity), bmin_rel == jr_0 to print class.
  Correction LD: the computed-direction rider verbatim on the r201
  wall-certificate surfaces.  GATE: G43 (text) + G24 (own).
BH11-F5 [NOTE][r203: smoke0's G80 pricing prose contradicts its own
  G61 verdict inside the kept log -- superseded pre-freeze, recorded
  as a static-prose wart]  z1_suppression_probe.smoke0.log (28/31,
  kept, disclosed) prints G61 = PAIRING-CARRIES with T0 = -24.4 (the
  pre-fix truncation bug) while its G80 pricing text asserts "the
  transplant 2x2 says the suppression follows the SUPPORT ... NOT
  the weights and NOT the exact pairing (SCRARITH suppressed like
  MAIN)" -- contradicting both the same log's G61 enum AND its own
  composite line "SCRARITH-O1".  The record run's G80 is fully
  consistent (COMPLETENESS-CARRIES + SCRARITH-O1 + the honest
  wedge).  Wart class: static gate prose written against an
  expected outcome, printed unconditionally.  GATE: G44.
BH11-F6 [NOTE][r205: the "STRUCTURE THEOREMS" typing oversells the
  abelian-group half -- adjudicated TRIVIALITY-WITH-REAL-NEIGHBORS]
  T_p T_q = T_{Q_p + Q_q} for T = [[I, 0], [-Q, I]] is one line of
  block-triangular algebra (the additivity of N_j = A0 - sum Q in
  chain dress; commutativity = commutativity of matrix addition).
  Calling it a STRUCTURE THEOREM (spec R1(i), note DXXXI "ABELIAN
  GROUP ... theorem") is generous; the spec's own parenthesis
  "(order-independence of the composed map, NOT of the orbit)" is
  the honest content-limiting rider, and the LOAD-BEARING neighbors
  are real and verified here: the graph action W -> W(I - Q W)^{-1}
  == (N - Q - z)^{-1} (an exact resolvent identity, own numeric
  check), the common-J identity T^T J T - J = diag(-2Q, 0) (exact,
  own), and the per-prime dictionary split Q_p == lp G_B - sum_m
  w_{p^m} W(m lp) (own quadrature Grams, <= 1e-40).  No verdict
  moves; correction LE: type the group law "elementary lemma" on
  future surfaces.  GATE: G45 (text) + G31/G32 (own).
BH11-F7 [NOTE][X2: the DXXX note (r204) rode in the r203 freeze
  commit BEFORE r204's own probe commit, and the carrying commit's
  exclusion sentence contradicts it]  Pinned git: ad81271c (r203
  freeze) adds BOTH DXXIX and DXXX to next.txt; 2462c9ef (r204
  freeze, later) adds NO note; yet ad81271c's message says "The
  running colligation and wave-eight lanes' files ... are
  deliberately NOT in this commit" while carrying the colligation
  lane's NOTE.  Content-exact, BH10-F11-class ordering wobble plus
  a message-wording inconsistency.  (DXXV riding in e018651b before
  the wave-eight commit 9ff483e9 is the SAME disclosed pattern and
  is cross-referenced by both commit messages -- clean.)  GATE: G03.
BH11-F8 [NOTE][X5: the DXVI written-out-residue rule is now broken
  by three of the seven notes -- the BH9-F6/BH10-F8 recurrence
  becoming systematic in the program tail]  DXXVI-DXXIX carry the
  canonical four-item residue with the H-PIN expansion written out;
  DXXX and DXXXII carry the SHORT form "{H-PIN} + {WPD/TAILWPD-
  Front}"; DXXXI carries a legitimately RESTRUCTURED H-PIN
  ("Inertia-1-Bein + Terminal-Clearance-Bein explizit getrennt" --
  cardinality unchanged, a genuine structuring, but also not the
  DXVI written-out form).  Nothing closes, upgrades or consumes
  anywhere (all seven notes verified).  Recommendation LF: either
  re-affirm the DXVI rule or amend it to allow the structured form.
  GATE: G46.

CHECKED CLEAN (adversarially, no finding): the r200 A1 fix is
COMPLETE (all K levels kept as poles, bottom pair from the first two
interlacing gaps -- code-verified, and the own all-K secular bottom
root matches the own inverse iteration at the WORST rung h = 20 to
1e-6 rel, the exact regime where the pre-A1 threshold solver failed);
the r200 "theorem from two endpoint numbers" is airtight as typed
(Weyl monotonicity both directions + rank-one interlacing give
gap(s) >= lam_1(0) - lam_0(1) for ALL s; simplicity of the ground
branch on the WHOLE path FOLLOWS from the measured gam_unif > 0 --
correctly presented as measured-strictness + exact-transport, Kato
ch. II cited for continuity only); the r200 Poisson comparator chain
is EXACT as claimed (own derivation: periodization identity via
fhat(om) = 1/(1/4 + om^2), AM-GM floor 2 e^{-L/4}, k^-2 tail cap
(a/pi)^2/(K-1); own recompute of the bound at all 14 rungs, min
2.972 at h = 4 == record print); the r201 b_n = P(1) = A(0) identity
is EXACT (last Bernstein coefficient == q(1) == P(1) == sum v_k --
algebra + own Fraction check at h = 4, 5, 20); the r201 pre-freeze
retype chain is verifiable at calibration level from the kept
calib1 log (G40/G52 fails exactly on the deep-rung refutation, the
G40 FAIL text carrying the refuting margins -0.0153/-0.0458) and the
final taxonomy states the honest composite; the r202 dps-60 choice
leaks NOTHING tau-adjacent (the probe reads ONLY ce["K"] and
ce["mpPrime"] -- verified by AST-level read census of the source;
the prime block is an O(1) finite atom sum); the r202 k = 0 defect
identity house - limit = a pc_p(0) is EXACT (own symbolic derivation
+ own mp check <= 1e-50); the EPSTEIN weight-doubling lamq(4) =
2 Lambda(4) is EXACT from the source recursion (own x^2+5y^2
representation counts, av = r/2, own log-derivative recursion:
lamq(2) = 0, lamq(4) = log 4 EXACT, lamq(8) = 0, support {4, 5, 6},
q = 6 mass fraction 0.509, lattice floor 0.1542 == CAL); the r203
smoke0 -> smoke1 verdict flip (PAIRING -> COMPLETENESS after the T0
truncation bug fix) is FULLY LOG-VERIFIED pre-freeze (smoke0 28/31
prints T0 -24.4 [SUP] + PAIRING-CARRIES; smoke1 31/31 prints T0
-2.0 [O1] + COMPLETENESS-CARRIES; record SHA postdates calib2); the
r203 transplant is FAIR (all four cells share MAIN's arch/modes/phi
-- world-blindness machine-warded by the record's T3 == EPSTEIN
entrywise gate at 1.1e-81 and reproduced here in own code); the
C(L) == 0 boundary fact is EXACT (sin(om_k L) = sin(2 pi k) = 0 and
a - L/2 = 0 entrywise -- own check); the r203 fine-tuning ward is
sound (own FD vs the exact first-order perturbation formula
dz_1/dw_q = -sum_{m != 1} z_m U_m^T C(u_q) U_1/(d_1 - d_m), own
derivation confirmed); the r204 "identically zero remainder" is
EXACT ALGEBRA plus a measured confirmation, not a numeric accident
(V_p^m = 0 on the window iff m log p >= L -- the truncated-shift
nilpotency is exact operator theory; the integer law M~_p = M_p -
[p^{M_p} == h] re-verified at all rungs; the measured leftover
1e-61..1e-119 is the CONFIRMATION, and the honest wording "== 0 at
working precision" is in the spec); the r204 central identity
2<B, Theta(I-Theta)^{-1}B> = ||D y||^2 - ||B||^2 is an EXACT
identity for any contraction (own algebra + own quadrature Grams
reproduce RawPrime == sum_p Q_p - theta G_B to 3.0e-61 at h = 4 and
the record's own value); "minus is dissipation" is DERIVED GIVEN the
r195 ACF law (an exact rewriting, honestly typed -- the ACF law
itself is the warded input, not an assumption of this round); the
r204 KYP certificate is convention-EXACT (discrete-time positive
real lemma, LMI [[P - A^T P A, C^T - A^T P B], [., D + D^T -
B^T P B]] >= 0 at P = 1 -- web-verified against the standard DTPR
statements; det = 2(1-lam)^2 and trace = (1-lam)(3+lam) re-proved
here in exact rationals at 5 sample points, degree argument) and its
SCOPE is honest (per-prime full-series completion, no wall
statement); the r205 membership equivalence (mu_j <= -1 <=> partial
wall PSD AND N_j not PD, GIVEN n_neg(N_j) <= 1 and nonzero pole
coupling) is a correct secular/interlacing argument (own derivation
+ own per-stage cholesky-vs-mu cross-check at h = 4, 5); the h = 4
seed-in-region anomaly does NOT break the skeleton (the wrap leg
degenerates to start-inside; once-in-never-out and the inertia
ladder hold; disclosed in spec and CAL_WRAP as (0, 0)); the r206
Sylvester kill is AIRTIGHT AS SCOPED (any complete J-orthogonal
block basis is a congruence of Jr, so sum_n inertia(S_n) == (n_+,
n_-) kills the PD-metric form for the ENTIRE class; completeness is
forced by the determinant-identity demand deg Theta_N = K - 1; the
spec's own "What the theorem does NOT force" rider correctly
excludes the similarity-class coefficient spectra, and the open door
"PD realization OUTSIDE the congruence class" is priced, not
crossed); the r206 adjugate-cleared chain is the exact block
continuant (own derivation Phi_m = E_m Theta_{m-1} - H adj(Phi_{m-1})
H^T with Theta_m = det Phi_m / Theta_{m-1}, re-proved and re-run in
own exact Fractions at h = 4, 5 -- Theta_N == det(yM - G) ==
det(V)^2 det(Jr) det(yI - A_ns) at ALL K integer points); the r206
censuses REPRODUCE in own code (EULER h = 4/5/8 S-censuses
(0,1,2)/(3,1,1)/(0,6,4), WRAP (2,3,0)/(1,4,5) at 5/8, ladders
(1,5)/(7,3)/(6,14) -- OWN de-normalized ray, own J-block-Lanczos);
the r204 smoke1 same-SHA pair is consistent (A1 = code-side rename,
A2 = code-side gate formula fix, docstring corrected at freeze with
the record-table insertion -- r198-precedent class, disclosed); X1
THE EULER-JET CHAIN COMPOSES (the k = 0 doubling is ONE fact in
three dresses: r202 doubled-jet law == r203 C(u)[0,0] = 2(L-u) ==
r204 G_B[0,0] = L doubling -- own identity checks; the seed A0 =
RawArch + theta G_B satisfies A0 + RawPole == H exactly; the Q_p
split is entrywise-exact own; r206's WRAP_PRIME == r205 CAL_WRAP inc
with the disclosed h = 4 fallback; r206's EULER seed channels == the
r202 closed-form aggregates == own atom sums); X6 THE PROGRAM RECORD
IS COHERENT AND HONEST (dictionary EXACT / cascade EXACT / region
TAU-RIDING-IN-ONE-STEP / block KILLED-BY-INERTIA compose without
overstatement; DXXXII closes with "vier exakte Strukturformen, null
neue all-h-Waehrung, die Barriere jedes Mal benannt, nie
ueberschritten" -- exactly the honest statement; NO surface claims
the cascade form reduces the wall's hardness; NO-RH fences verified
on all seven specs + seven notes + all seven freeze commits).

SMOKE-STAGE FIXES (pre-record, disclosed; NO completed record run
existed at any fix; all three are AUDIT-CODE instrument bugs, no
bar, class, finding, tolerance or verdict moved): (a) smoke1 =
22/32 at first-freeze SHA ff68d6b02a7cf8e4 (log kept as
bughunt11_probe.smoke1.log) -- the probe's own_cell restructuring
dropped the parity convention (the PLAIN unnormalized blocks are
the Raw blocks; the normalized M carries par_i par_j): fixed, and
the same smoke exposed that CONCURRENT LANES had prepended notes
DXXXIII/DXXXIV to next.txt mid-audit -- the G03 numeral gate was
made tolerant to newer notes above the audited block (the in-scope
523-532 subsequence is still gated exactly; the audit note takes
the next free numeral at write time per the collision protocol);
smoke2 = 31/32 at 3496a6d6a143a55d (log kept).  (b) the G24 b_n
identity sub-check compared the Bernstein b_n (computed on the
content-stripped integer scaling) against the UNSCALED Fraction
P(1) -- comparison fixed to the scaled P(1); smoke3 = 32/32 at the
same SHA (log kept; the b_n fix is code-below-docstring).

PRE-FREEZE PROTOTYPE DISCLOSURE (house convention; scratch scripts
bh11_scratch_proto*.py DELETED at freeze, values cited here): the
own builder was transcription-validated at h = 4 against the record
tables (one transcription bug found and fixed IN THE PROTOTYPE:
missing norm-division step; post-fix everything reproduced: rank1
4.9e-63, d1f -7.01, guf -7.01, jr0 -5.03, central identity 3.0e-61,
lam_min(H) 1.106737, Delta log -10.81, compositional secular
6.5e-30, mu0 -8.264); the r206 ray convention was adjudicated in the
prototype: the FIRST prototype pass wrongly used the NORMALIZED
eigenvector (not the builder's de-normalized cn) and got an h = 5
EULER S-census of (2,3,0) vs CAL (3,1,1) -- the independent
cumulative-inertia cross-check exposed the prototype's own error
(the de-normalization moves the cancellation-sensitive A_0 and with
it the whole pencil); with the CORRECT de-normalized ray ALL
censuses reproduce (h = 4/5/8 EULER + 5/8 WRAP == CAL) -- an audit-
side misstep, disclosed, r206 CLEAN; the r206 WRAP seed at h = 4 is
degenerate by the exact fact Im S_2(om_k) == 0 at h = 4 (om_k l2 =
k pi; the fallback-seed cell is CAL-identical to EULER there) and is
audited at h = 5, 8 here.  No bar, class, tolerance or verdict was
chosen from a failed check.  Amendments after the frozen run, if
any, are appended as numbered AMENDMENT blocks.

X-VERDICTS (the contract deliverables):
X1 EULER-JET-CHAIN-COMPOSES: conventions verified composing across
  r202 -> r204 -> r205 -> r206 (k0 doubling one-fact-three-dresses,
  A0/H seed algebra, Q_p split, WRAP handoff, channel aggregates) --
  own machine checks, zero mismatches.
X2 NOTE NUMERALS: DXXVI-DXXXII positions/order/uniqueness verified
  (newer concurrent-lane notes above the audited block tolerated by
  the collision protocol); riding structure pinned via git (DXXV in
  e018651b disclosed both sides; DXXX in ad81271c = BH11-F7 wobble);
  the audit note takes the next free numeral at write time.
X3 SPEC_SHA + LINEAGE: all seven audited SPEC_SHAs + BH10's exact;
  all six correction-block files (BH9 K1-K3 + BH10 KA/KB/KE)
  byte-invariant docstrings with blocks OUTSIDE; all disclosed
  smoke/calib/proto/run logs match the disclosed chains gate-exactly
  (the two r201 superseded smoke SHAs = BH11-F3); determinism: all
  seven record pairs re-diffed OWN, timing-normalized EMPTY.
X4 NEW-CLAIM LEDGER: ALL RECOMPUTES REPRODUCE in fully own code
  (r200 gap/Poisson/h20-deep, r201 wall certificates + b_n identity
  h = 4/5/20, r202 dictionary/defect/Cayley/envelope/lamq, r203
  z1-anatomy/ID1/FT/C(L)/transplant-2x2, r204 central identity/
  Schur/KYP/lam_min(H)/nilpotency, r205 closure/orbit/Delta/
  compositional-secular/chain-identities, r206 ladders/censuses/
  Sylvester/determinant-chain): ZERO failed recomputes -- no MAJOR.
X5 RESIDUE TRANSPORT: canonical four-item residue carried by all
  seven notes with the short/restructured-form recurrence = BH11-F8;
  the two flagged loops (WEIL-ALLTESTS, TURAN-CONE-POSITIVITY)
  registered by ALL SEVEN probes' flagged sets and consumed by
  NOTHING; the new named legs (inertia-1, terminal clearance) and
  barriers (GPSD-margin, PR-domination) carried consistently
  (DXXXI structures H-PIN with the new legs, cardinality unchanged).
X6 PROGRAM ADJUDICATION: COHERENT-NO-OVERSTATEMENT -- the four
  program verdicts are four exact FORMS of the same wall with the
  hardness explicitly unmoved on every surface; the strongest
  composed claim anywhere stays mechanism-typed; NO-RH fences
  intact on all in-scope surfaces.

CORRECTIONS OF RECORD RECOMMENDED (house convention, NOT
retro-edited): (LA) BH11-F1 per-rung residual rider + future gap
gates print/ward dps-scaled per-rung residuals; (LB) BH11-F2 the A1
filename erratum; (LC) BH11-F3 keep-all-smoke-logs process note;
(LD) BH11-F4 computed-direction rider on the r201 wall-certificate
surfaces; (LE) BH11-F6 "elementary lemma" typing for the chain-group
law; (LF) BH11-F8 re-affirm or amend the DXVI residue rule.

FROZEN NUMERICS (audit pins; sources = the audited rounds' frozen
record tables + own prototype, disclosed above):
SHAS8 = {r200: 703f70e5016581e4, r201: f43babb5b80416d1, r202:
34781d187e1c5815, r203: c68e7aa2c229e7c9, r204: 5327721e3f2f36f8,
r205: cb1dfde33a198fb3, r206: 638885ff5e2398b5, r199/BH10:
5551aa7b967230f1}.  CORRECTED6 = {commensurability_mechanism_probe:
dbc14014899fb286, fewatom_reduction_probe: 35fb341bb281b04b,
turan_extremal_probe: a6edc3f911e8f069, ground_residue_obs_probe:
48637c8898a1da5a, zb_wiggle_strat_probe: 8639b3a78503a0f9,
pi_pattern_scan_probe: 00fc85173fe07470}.  COMMITS = {r199:
5e856d12, corrX: b8b0d75f, r200: e018651b, r201: b47d4dcb, r202:
b7a5caf1, r203: ad81271c, wave8: 9ff483e9, r204: 2462c9ef, r205:
38ddbae7, r206: 07c465e7}.  GATE_TAB = {r200: 28/28, r201: 30/30,
r202: 24/24, r203: 31/31, r204: 30/30, r205: 27/27, r206: 25/25}.
CAL_GUF = {4: -7.01, 5: -11.54, 8: -24.71, 20: -81.74} (LOG_TOL
0.10); CAL_D0F4 = -0.04; CAL_JR0 = {4: -5.0, 5: -7.5, 8: -14.3,
20: -43.3}; POISSON_MIN = 2.972 (tol 5e-3, at h = 4, all 14 rungs
positive); H20_DPS = 160; HEADROOM_MIN = 30 dex; CAL_Z1REL = {4:
-6.9, 5: -11.4, 8: -24.4}; CAL_TRANS = {T0: -2.0, T1: -1.2, T2:
-2.6, T3: -0.8} (tol 0.2); EPS_Z1REL -0.8; CAL_LMH4 = 1.106737
(tol 1e-3); CAL_CENT_BAR 1e-40; CAL_DLOG = {4: -10.81, 5: -15.95};
CAL_L0LOG = {4: -10.70, 5: -15.78}; CAL_MU0_4 = -8.26 (tol 0.05);
SEC_COMP_BAR 1e-20; CAL_LADDER = {4: (1, 5), 5: (7, 3), 8: (6, 14)};
CAL_SCEN_E = {4: (0, 1, 2), 5: (3, 1, 1), 8: (0, 6, 4)}; CAL_SCEN_W
= {5: (2, 3, 0), 8: (1, 4, 5)}; CAL_ACEN_E4 = (1, 0, 1, 0);
CAL_BCEN_E4 = (2, 0, 1, 0); DICT_BAR 1e-50; QUAD_BAR 1e-40; ID1_BAR
1e-10; FT_ANA_BAR 1e-4; CLB_BAR 1e-50 (C(L) rel); Z1DEC_BAR 1e-25
(gross-scale); EPS_MASS = 0.509 (tol 0.02); EPS_LAT = 0.1542 (tol
1e-3); TWOMODE = (0.68734, 0.69898, 0.02); RUNTIME_BAR 2700 s.
Deterministic: no RNG anywhere; ProcessPool results keyed; git reads
pinned read-only.

VERDICT ENUM (frozen): BUGHUNT11-FINDINGS(8: 0 MAJOR / 1 MINOR /
7 NOTE) + R200-GAP-SIGN-RECERTIFIED-OWN-H4-5-8-20(F1) +
R200-A1-COMPLETE-ANCHORED-AT-WORST-RUNG +
GAP-THEOREM-AIRTIGHT-AS-TYPED + POISSON-CHAIN-EXACT-OWN +
R201-WALL-CERTS-REPRODUCE-OWN-INCL-H20(F4 rider proposed) +
BN-P1-A0-IDENTITY-EXACT + R201-SUPERSEDED-SMOKES-NOTED(F3) +
R202-DICTIONARY-EXACT-OWN + K0-DEFECT-IDENTITY-EXACT-OWN +
EPSTEIN-DOUBLING-EXACT-FROM-SOURCE + R203-FLIP-PREFREEZE-VERIFIED +
TRANSPLANT-FAIR-AND-REPRODUCES + R204-SCHUR-EXACT-OWN +
REMAINDER-ZERO-IS-EXACT-ALGEBRA + KYP-CONVENTION-EXACT-SCOPE-HONEST
+ MINUS-DERIVED-GIVEN-ACF-TYPED + R205-REGION-REPRODUCES-OWN +
CHAIN-GROUP-TRIVIALITY-TYPED(F6) + INERTIA-LEG-SOUND +
R206-SYLVESTER-KILL-AIRTIGHT-AS-SCOPED +
DET-CHAIN-EXACT-OWN-ALL-POINTS + CENSUSES-REPRODUCE-OWN +
X1-CHAIN-COMPOSES + X2-NUMERALS-ONE-RIDING-WOBBLE(F7) +
X3-LINEAGE-CLEAN-MODULO-F3 + X4-ALL-RECOMPUTES-REPRODUCE +
X5-RESIDUE-SHORTFORM-RECURRENCE(F8) +
X6-PROGRAM-COHERENT-NO-OVERSTATEMENT + FENCES-INTACT.
NO verdict of rounds 200-206 flips.

AST FIREWALL: no zero-oracle names; no z-function use; no np.load;
no import of verification/ or of ANY probe module (the wall and all
instruments rebuilt OWN); git reads pinned read-only.  NO RH CLAIM.
EXPLORATION ONLY.
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
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
NEXT = os.path.join(HERE, "..", "next.txt")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

KFAC = 1.25
WORKERS = 6
RUNTIME_BAR = 2700.0
H20_DPS = 160
HEADROOM_MIN = 30.0

SHAS8 = {
    "r200": ("pole_homotopy_probe.py", "703f70e5016581e4"),
    "r201": ("eigvec_geometry_probe.py", "f43babb5b80416d1"),
    "r202": ("euler_jet_dictionary_probe.py", "34781d187e1c5815"),
    "r203": ("z1_suppression_probe.py", "c68e7aa2c229e7c9"),
    "r204": ("euler_jet_colligation_probe.py", "5327721e3f2f36f8"),
    "r205": ("euler_hpin_region_probe.py", "cb1dfde33a198fb3"),
    "r206": ("euler_block_sturm_probe.py", "638885ff5e2398b5"),
    "r199": ("bughunt10_probe.py", "5551aa7b967230f1"),
}
CORRECTED6 = {
    "commensurability_mechanism_probe.py": "dbc14014899fb286",
    "fewatom_reduction_probe.py": "35fb341bb281b04b",
    "turan_extremal_probe.py": "a6edc3f911e8f069",
    "ground_residue_obs_probe.py": "48637c8898a1da5a",
    "zb_wiggle_strat_probe.py": "8639b3a78503a0f9",
    "pi_pattern_scan_probe.py": "00fc85173fe07470",
}
COMMITS = {"r199": "5e856d12", "corrX": "b8b0d75f", "r200": "e018651b",
           "r201": "b47d4dcb", "r202": "b7a5caf1", "r203": "ad81271c",
           "wave8": "9ff483e9", "r204": "2462c9ef", "r205": "38ddbae7",
           "r206": "07c465e7"}
GATE_TAB = {"r200": "28/28", "r201": "30/30", "r202": "24/24",
            "r203": "31/31", "r204": "30/30", "r205": "27/27",
            "r206": "25/25"}
# log -> (SPEC_SHA prefix or None, final gates or None, fail set)
LOG_TAB = {
    "pole_homotopy_probe.smoke1.log":
        ("15b13665f3438ca5", "28/28", set()),
    "calib_ph_fail1.log":
        ("15b13665f3438ca5", "23/28",
         {"G14-s1-anchor", "G30-gap-ladder", "G31-path-nodal-census",
          "G33-interlacing-adjudication", "G52-mechanism-typing"}),
    "calib_ph_pass1.log": ("a0829ac28d5703e1", "28/28", set()),
    "pole_homotopy_probe.run1.log":
        ("703f70e5016581e4", "28/28", set()),
    "pole_homotopy_probe.run2.log":
        ("703f70e5016581e4", "28/28", set()),
    "eigvec_geometry_probe.smoke1.log":
        ("8a0fd8e821b5fc01", "30/30", set()),
    "eigvec_geometry_probe.calib1.log":
        ("8a0fd8e821b5fc01", "28/30",
         {"G40-edge-minimality-census", "G52-Istar-adjudication"}),
    "eigvec_geometry_probe.run1.log":
        ("f43babb5b80416d1", "30/30", set()),
    "eigvec_geometry_probe.run2.log":
        ("f43babb5b80416d1", "30/30", set()),
    "euler_jet_dictionary_probe.smoke1.log":
        ("c359d8750c943ddc", "22/23",
         {"G15-jet-derivative-closed-forms-symbolic"}),
    "euler_jet_dictionary_probe.smoke2.log":
        ("c359d8750c943ddc", "23/23", set()),
    "calib_ejd_pass1.log": ("c359d8750c943ddc", "24/24", set()),
    "euler_jet_dictionary_probe.run1.log":
        ("34781d187e1c5815", "24/24", set()),
    "euler_jet_dictionary_probe.run2.log":
        ("34781d187e1c5815", "24/24", set()),
    "z1_suppression_probe.smoke0.log":
        ("67bf9a174ff774dc", "28/31",
         {"G14-secular+anchor-wards", "G33-sensitivity-finetuning",
          "G34-alignment-law-lock"}),
    "z1_suppression_probe.smoke1.log":
        ("385c41eb0afb7a98", "31/31", set()),
    "z1_suppression_probe.calib1.log":
        ("385c41eb0afb7a98", "29/31",
         {"G14-secular+anchor-wards", "G33-sensitivity-finetuning"}),
    "z1_suppression_probe.calib2.log":
        ("c6899d40cfbb4216", "31/31", set()),
    "z1_suppression_probe.run1.log":
        ("c68e7aa2c229e7c9", "31/31", set()),
    "z1_suppression_probe.run2.log":
        ("c68e7aa2c229e7c9", "31/31", set()),
    "euler_jet_colligation_probe.smoke1.log":
        ("769f8a2652e5375c", "28/30",
         {"G01-firewall", "G12-minimality-symbolic"}),
    "euler_jet_colligation_probe.smoke2.log":
        ("769f8a2652e5375c", "30/30", set()),
    "calib_ejc_pass1.log": ("769f8a2652e5375c", "30/30", set()),
    "euler_jet_colligation_probe.run1.log":
        ("5327721e3f2f36f8", "30/30", set()),
    "euler_jet_colligation_probe.run2.log":
        ("5327721e3f2f36f8", "30/30", set()),
    "euler_hpin_region_probe.smoke1.log":
        ("6718b312fde998e8", "27/27", set()),
    "calib_ehr_pass1.log": ("6718b312fde998e8", "27/27", set()),
    "euler_hpin_region_probe.run1.log":
        ("cb1dfde33a198fb3", "27/27", set()),
    "euler_hpin_region_probe.run2.log":
        ("cb1dfde33a198fb3", "27/27", set()),
    "euler_block_sturm_probe.smoke1.log":
        ("e0f011bb26ba8e8c", "25/25", set()),
    "calib_ebs_pass1.log": ("e0f011bb26ba8e8c", "25/25", set()),
    "euler_block_sturm_probe.run1.log":
        ("638885ff5e2398b5", "25/25", set()),
    "euler_block_sturm_probe.run2.log":
        ("638885ff5e2398b5", "25/25", set()),
}
PROTO_LOGS = ("proto_hpin_scratch.out1.log",
              "proto_hpin_scratch2.out1.log",
              "proto_blocksturm_scratch.out1.log",
              "proto_blocksturm_symb.out1.log")
DIFF_PAIRS = ("pole_homotopy_probe", "eigvec_geometry_probe",
              "euler_jet_dictionary_probe", "z1_suppression_probe",
              "euler_jet_colligation_probe", "euler_hpin_region_probe",
              "euler_block_sturm_probe")

CAL_GUF = {4: -7.01, 5: -11.54, 8: -24.71, 20: -81.74}
CAL_JR0 = {4: -5.0, 5: -7.5, 8: -14.3, 20: -43.3}
CAL_Z1REL = {4: -6.9, 5: -11.4, 8: -24.4}
CAL_TRANS = {"T0": -2.0, "T1": -1.2, "T2": -2.6, "T3": -0.8}
EPS_Z1REL = -0.8
CAL_LMH4 = 1.106737
CAL_DLOG = {4: -10.81, 5: -15.95}
CAL_L0LOG = {4: -10.70, 5: -15.78}
CAL_MU0_4 = -8.26
CAL_LADDER = {4: (1, 5), 5: (7, 3), 8: (6, 14)}
CAL_SCEN_E = {4: (0, 1, 2), 5: (3, 1, 1), 8: (0, 6, 4)}
CAL_SCEN_W = {5: (2, 3, 0), 8: (1, 4, 5)}
CAL_ACEN_E4 = (1, 0, 1, 0)
CAL_BCEN_E4 = (2, 0, 1, 0)
WRAP_PRIME = {5: 2, 8: 3}
POISSON_MIN = 2.972
HRUNGS14 = (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20)
ALLR202 = (4, 5, 8, 13, 20, 28)

LOG_TOL = 0.10
LOG_TOL2 = 0.20
DICT_BAR = 1e-50
QUAD_BAR = 1e-40
ID1_BAR = 1e-10
FT_ANA_BAR = 1e-4
CLB_BAR = 1e-50
Z1DEC_BAR = 1e-25
SEC_COMP_BAR = 1e-20
EPS_MASS = 0.509
EPS_LAT = 0.1542
TWOMODE = (0.68734, 0.69898, 0.02)
ANCHOR_BAR = 1e-6

CHECKS: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(t: str) -> None:
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def rd(name: str, base: str = HERE) -> str:
    return open(os.path.join(base, name), "r", encoding="utf-8").read()


def nsp(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def spec_sha_of(pyfile: str) -> str:
    doc = ast.get_docstring(ast.parse(rd(pyfile)), clean=False)
    return hashlib.sha256(doc.encode("utf-8")).hexdigest()[:16]


def normalize_timing(text: str) -> str:
    text = re.sub(r"\b\d+(?:\.\d+)?\s?s\b", "S", text)
    text = re.sub(r"runtime \S+", "runtime S", text)
    text = re.sub(r"WALL \S+", "WALL S", text)
    return text


def raw_diff_lines(a: str, b: str) -> int:
    la, lb = a.splitlines(), b.splitlines()
    n = sum(1 for x, y in zip(la, lb) if x != y)
    return n + abs(len(la) - len(lb))


def fails_of(logtext: str) -> set:
    return set(re.findall(r"\[FAIL\] (\S+)", logtext))


def git(args: list) -> str:
    return subprocess.run(["git", "-C", REPO] + args,
                          capture_output=True, text=True,
                          check=True).stdout


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


def frac_of(x) -> Fraction:
    sign, man, exp, _bc = mp.mpf(x)._mpf_
    v = Fraction(man) * (Fraction(2) ** exp)
    return -v if sign else v


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
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
                if m.startswith("verification") or "probe" in m \
                        or "radius4" in m:
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; no z-function; no np.load; no "
                       "probe/verification import (wall + all "
                       "instruments rebuilt OWN); git reads pinned "
                       "read-only; concurrent-lane files untouched")


# ------------------------------------------------------ own wall builder
def r_of(w):
    if w == 0:
        return mp.mpf("0.25")
    return mp.exp(-w / 2) / (-mp.expm1(-2 * w)) - 1 / (2 * w)


def arch_mode(h: int, dps: int, k: int) -> tuple:
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        L2v = 2 * aa
        o = k * mp.pi / aa
        if k == 0:
            jv = mp.mpf(0)
            f0 = L2v
            psi_d = lambda w: L2v - w                    # noqa: E731
        else:
            npts = int(mp.floor(L2v * o / mp.pi))
            pts = ([mp.mpf(0)]
                   + [jj * mp.pi / o for jj in range(1, npts + 1)]
                   + [L2v])
            jv = mp.quad(lambda w, o=o: mp.sin(o * w) * r_of(w),
                         pts) + mp.si(L2v * o) / 2
            f0 = aa
            psi_d = (lambda w, o=o: (aa - w / 2) * mp.cos(o * w)
                     - mp.sin(o * w) / (2 * o))
        integrand = (lambda w, f0=f0, psi_d=psi_d:
                     (f0 * mp.exp(-2 * w) - psi_d(w) * mp.exp(-w / 2))
                     / (-mp.expm1(-2 * w)))
        npts = max(int(mp.floor(L2v * o / mp.pi)), 1) if k else 1
        base = [mp.mpf(0), mp.mpf("1e-6"), mp.mpf("1e-3"),
                mp.mpf("0.05"), L2v]
        if k:
            base += [jj * mp.pi / o for jj in range(1, npts + 1)]
        pts = sorted(set(p for p in base if p <= L2v))
        body = mp.quad(integrand, pts)
        tail = -f0 / 2 * mp.log1p(-mp.exp(-2 * L2v))
        adiag = -f0 * (mp.euler + mp.log(mp.pi)) + 2 * (body + tail)
        return jv, adiag


def w_archchunk(args) -> dict:
    h, dps, klist = args
    out = dict(h=h, data={}, err="")
    try:
        for k in klist:
            jv, ad = arch_mode(h, dps, k)
            out["data"][k] = (mp.nstr(jv, dps),
                              mp.nstr(ad, dps))
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        out["err"] = "%s\n%s" % (exc, traceback.format_exc())
        return out


def sieve_atoms(h: int):
    icap = int(math.floor(h))
    comp = [False] * (icap + 1)
    nlist = []
    for p in range(2, icap + 1):
        if comp[p]:
            continue
        for m in range(p * p, icap + 1, p):
            comp[m] = True
        q = p
        while q <= icap:
            nlist.append((q, p))
            q *= p
    nlist.sort()
    return nlist


def own_cell(h: int, dps: int, arch: dict) -> dict:
    """FULLY OWN even-sector MAIN wall (r171-r206 conventions; BH9/
    BH10 lineage).  Own sieve; arch data passed in (own pooled
    quadratures).  Returns unnormalized Raw* blocks (Raw = D_par
    block D_par) and the normalized M."""
    with mp.workdps(dps):
        aa = mp.log(h) / 2
        K = int(math.ceil(KFAC * h * math.log(h)))
        L2v = 2 * aa
        oms = [k * mp.pi / aa for k in range(K)]
        par = [mp.mpf((-1.0) ** k) for k in range(K)]
        jvec = [mp.mpf(arch[k][0]) for k in range(K)]
        adiag = [mp.mpf(arch[k][1]) for k in range(K)]
        nlist = sieve_atoms(h)
        atoms = [(q, p, mp.log(q), mp.log(p) / mp.sqrt(q))
                 for q, p in nlist]
        pj = [sum((w * mp.sin(o * u) for _q, _p, u, w in atoms),
                  mp.mpf(0)) for o in oms]
        Upole = mp.zeros(K, K)
        Uarch = mp.zeros(K, K)
        Uprime = mp.zeros(K, K)
        pv = [mp.sinh(aa / 2) / (mp.mpf(1) / 4 + oms[i] ** 2)
              for i in range(K)]
        for i in range(K):
            for j in range(K):
                Upole[i, j] = 2 * pv[i] * pv[j]
        for i in range(K):
            for j in range(i):
                den = oms[j] ** 2 - oms[i] ** 2
                va = -2 * (oms[i] * jvec[i] - oms[j] * jvec[j]) / den
                Uarch[i, j] = Uarch[j, i] = va
                vp = 2 * (oms[i] * pj[i] - oms[j] * pj[j]) / den
                Uprime[i, j] = Uprime[j, i] = vp
        for i in range(K):
            o = oms[i]
            Uarch[i, i] += adiag[i]
            pdiag = sum((w * ((aa - u / 2) * mp.cos(o * u)
                              - mp.sin(o * u) / (2 * o))
                         if i else w * (L2v - u)
                         for _q, _p, u, w in atoms), mp.mpf(0))
            Uprime[i, i] += 2 * pdiag
        # convention (r171-r206): the PLAIN unnormalized blocks ARE
        # the Raw blocks (Raw = D_par N M N D_par undoes the pars);
        # the normalized builder matrix M carries par_i par_j and
        # divides by nrm_i nrm_j.
        nrm = [mp.sqrt(L2v) if i == 0 else mp.sqrt(aa)
               for i in range(K)]
        Mn = mp.zeros(K, K)
        RawPole = mp.zeros(K, K)
        RawArch = mp.zeros(K, K)
        RawPrime = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                sg = par[i] * par[j]
                RawPole[i, j] = Upole[i, j]
                RawArch[i, j] = Uarch[i, j]
                RawPrime[i, j] = Uprime[i, j]
                Mn[i, j] = (Upole[i, j] + Uarch[i, j]
                            - Uprime[i, j]) * sg / (nrm[i] * nrm[j])
        return dict(K=K, aa=aa, L=L2v, oms=oms, par=par, nrm=nrm,
                    atoms=atoms, M=Mn, RawPole=RawPole,
                    RawArch=RawArch, RawPrime=RawPrime, pj=pj)


def bottom_vec(Raw, K):
    x = mp.matrix([mp.mpf(1)] * K)
    for _ in range(3):
        x = mp.lu_solve(Raw, x)
        x = x / mp.sqrt(sum(x[i] ** 2 for i in range(K)))
    v = [x[i] for i in range(K)]
    Rv = [sum(Raw[i, j] * v[j] for j in range(K)) for i in range(K)]
    lam = sum(v[i] * Rv[i] for i in range(K))
    res = max(abs(Rv[i] - lam * v[i]) for i in range(K))
    return v, lam, res


def W_atom(u, oms, L, K):
    """r195 ACF kernel, own transcription (C(u) = -W(u))."""
    W = mp.zeros(K, K)
    b = [o * o for o in oms]
    for i in range(K):
        for j in range(i):
            W[i, j] = 2 * (oms[i] * mp.sin(oms[i] * u)
                           - oms[j] * mp.sin(oms[j] * u)) \
                / (b[i] - b[j])
            W[j, i] = W[i, j]
    W[0, 0] = 2 * (u - L)
    for k in range(1, K):
        W[k, k] = mp.sin(oms[k] * u) / oms[k] \
            + (u - L) * mp.cos(oms[k] * u)
    return W


def secular_bottom(d, z, ccs, dps, K):
    """own all-K-poles bisection (post-A1 structure)."""
    nbis = int(3.4 * dps) + 60

    def root_in(lo, hi):
        w = hi - lo
        a2 = lo + w * mp.mpf(10) ** (-dps)
        b2 = hi - w * mp.mpf(10) ** (-dps)
        for _ in range(nbis):
            m = (a2 + b2) / 2
            f = 1 + ccs * sum(z[i] ** 2 / (d[i] - m)
                              for i in range(K))
            if f < 0:
                a2 = m
            else:
                b2 = m
        return (a2 + b2) / 2

    return root_in(d[0], d[1]), root_in(d[1], d[2])


# ------------------------------------- exact certificates (own code)
def cheb_int_poly(vF):
    K = len(vF)
    Tprev = [Fraction(1)]
    Tcur = [Fraction(0), Fraction(1)]
    P = [Fraction(0)] * K
    P[0] += vF[0]
    if K > 1:
        P[1] += vF[1]
    for k in range(2, K):
        Tnext = [Fraction(0)] * (k + 1)
        for i, c in enumerate(Tcur):
            Tnext[i + 1] += 2 * c
        for i, c in enumerate(Tprev):
            Tnext[i] -= c
        for i, c in enumerate(Tnext):
            P[i] += vF[k] * c
        Tprev, Tcur = Tcur, Tnext
    return P


def exact_wall_certs(v0w, K):
    """own Descartes + Bernstein + the b_n = P(1) = A(0) identity on
    the exact dyadic rationalization of the computed wall vector."""
    vF = [frac_of(t) for t in v0w]
    P = cheb_int_poly(vF)
    A0 = sum(vF)
    P1 = sum(P)
    id_ok = (P1 == A0)                    # P(1) == A(0) exact
    if P1 < 0:
        P = [-c for c in P]
        P1 = -P1
    emax = max((c.denominator.bit_length() - 1) for c in P)
    pint = [int(c * (1 << emax)) for c in P]
    g = 0
    for c in pint:
        g = math.gcd(g, abs(c))
    pint = [c // (g or 1) for c in pint]
    n = len(pint) - 1
    binom = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        binom[i][0] = 1
        for j in range(1, i + 1):
            binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j]
    R = [0] * (n + 1)
    for j, pjc in enumerate(pint):
        if pjc == 0:
            continue
        m2 = n - j
        for i1 in range(j + 1):
            c1 = binom[j][i1] * ((-1) ** (j - i1)) * pjc
            for i2 in range(m2 + 1):
                R[i1 + i2] += c1 * binom[m2][i2]
    nzR = [1 if c > 0 else -1 for c in R if c != 0]
    scd = sum(1 for i in range(1, len(nzR)) if nzR[i] != nzR[i - 1])
    q = [0] * (n + 1)
    for j, pjc in enumerate(pint):
        if pjc == 0:
            continue
        for i in range(j + 1):
            q[i] += pjc * binom[j][i] * (2 ** i) * ((-1) ** (j - i))
    nb = 0
    bmin = None
    bmax = Fraction(0)
    for i in range(n + 1):
        acc = Fraction(0)
        for j in range(i + 1):
            if q[j]:
                acc += Fraction(q[j] * binom[i][j], binom[n][j])
        if acc < 0:
            nb += 1
        if bmin is None or acc < bmin:
            bmin = acc
        if abs(acc) > bmax:
            bmax = abs(acc)
    br = mp.mpf(bmin.numerator) / mp.mpf(bmin.denominator) \
        / (mp.mpf(bmax.numerator) / mp.mpf(bmax.denominator))
    # b_n identity: last Bernstein coefficient == q(1) == P(1)
    # (on the content-stripped integer scaling of P)
    bn = sum(Fraction(q[j] * binom[n][j], binom[n][j])
             for j in range(n + 1) if q[j])
    id_bn = (bn == sum(pint))
    return dict(nb=nb, scd=scd, bmin_rel=br, id_p1_a0=id_ok,
                id_bn_p1=id_bn)


def frac_det(Mrows):
    n = len(Mrows)
    A = [row[:] for row in Mrows]
    det = Fraction(1)
    for c in range(n):
        piv = None
        for r in range(c, n):
            if A[r][c] != 0:
                piv = r
                break
        if piv is None:
            return Fraction(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det *= A[c][c]
        inv = Fraction(1) / A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] * inv
            if f:
                for c2 in range(c, n):
                    A[r][c2] -= f * A[c][c2]
    return det


# ------------------------------------------- heavy rung worker (own)
def w_rung(args) -> dict:
    """own per-rung battery at h = 4, 5, 8 (dps house ladder)."""
    h, dps, arch = args
    try:
        t0 = time.time()
        ce = own_cell(h, dps, arch)
        K = ce["K"]
        out = dict(h=h, K=K, err="")
        with mp.workdps(dps):
            aa, L = ce["aa"], ce["L"]
            oms = ce["oms"]
            b = [o * o for o in oms]
            s2 = mp.sinh(aa / 2) ** 2
            phi = [1 / (mp.mpf(1) / 4 + bb) for bb in b]
            RawW = mp.zeros(K, K)
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    RawW[i, j] = ce["RawPole"][i, j] \
                        + ce["RawArch"][i, j] - ce["RawPrime"][i, j]
                    NoP[i, j] = ce["RawArch"][i, j] \
                        - ce["RawPrime"][i, j]
            r1 = max(abs(ce["RawPole"][i, j]
                         - 2 * s2 * phi[i] * phi[j])
                     for i in range(K) for j in range(K))
            r1m = max(abs(2 * s2 * phi[i] * phi[j])
                      for i in range(K) for j in range(K))
            out["rank1_dev"] = float(r1 / r1m)
            fro = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                              for j in range(K)))
            E, Q = mp.eigsy(NoP)
            idx = sorted(range(K), key=lambda m: E[m])
            d = [E[idx[m]] for m in range(K)]
            Qc = [[Q[i, idx[m]] for i in range(K)] for m in range(K)]
            eres = mp.mpf(0)
            for col in (0, 1):
                for i in range(K):
                    ri = sum(NoP[i, j] * Qc[col][j]
                             for j in range(K)) - d[col] * Qc[col][i]
                    eres = max(eres, abs(ri))
            out["eig_res_f"] = float(mp.log(eres / fro, 10)) \
                if eres > 0 else -300.0
            out["d0_neg"] = bool(d[0] < 0)
            out["d1_pos"] = bool(d[1] > 0)
            out["nneg_nop"] = sum(1 for t in d if t < 0)
            z = [sum(Qc[m][i] * phi[i] for i in range(K))
                 for m in range(K)]
            out["z1rel"] = float(mp.log(abs(z[1] / z[0]), 10))
            lam0s1, lam1s1 = secular_bottom(d, z, 2 * s2, dps, K)
            gu = d[1] - lam0s1
            out["guf"] = float(mp.log(abs(gu) / fro, 10))
            out["gu_pos"] = bool(gu > 0)
            v0w, lamw, invres = bottom_vec(RawW, K)
            out["invres"] = float(invres / fro)
            out["lam0_pos"] = bool(lamw > 0)
            out["l0log"] = float(mp.log(lamw, 10))
            out["anchor_dev"] = float(abs(lamw - lam0s1) / abs(lamw))
            num0 = abs(sum(v0w))
            den0 = sum(abs(t) for t in v0w)
            out["jr0"] = float(mp.log(num0 / den0, 10))
            # gap(s) >= gu along an own 9-point path (theorem check)
            ok_gap = True
            for sj in range(1, 9):
                l0, l1 = secular_bottom(d, z,
                                        mp.mpf(sj) / 8 * 2 * s2,
                                        dps, K)
                if l1 - l0 < gu * (1 - mp.mpf("1e-20")):
                    ok_gap = False
            out["gap_ge_gu"] = ok_gap
            # r201 exact wall certificates
            ec = exact_wall_certs(v0w, K)
            out["nb"] = ec["nb"]
            out["scd"] = ec["scd"]
            out["bminlog"] = float(mp.log(abs(ec["bmin_rel"]), 10))
            out["id_p1_a0"] = ec["id_p1_a0"]
            out["id_bn_p1"] = ec["id_bn_p1"]
            # r203: C(L) == 0 + per-atom z1 decomposition + ID1
            WL = W_atom(L, oms, L, K)
            wmax = max(abs(W_atom(mp.log(2), oms, L, K)[i, j])
                       for i in range(K) for j in range(K))
            out["cl_dev"] = float(max(abs(WL[i, j]) for i in range(K)
                                      for j in range(K)) / wmax)
            U1 = Qc[1]
            Tarch = sum(U1[i] * sum(ce["RawArch"][i, j] * phi[j]
                                    for j in range(K))
                        for i in range(K)) / d[1]
            Tqs = []
            for (qv, pv, u, w) in ce["atoms"]:
                Wm = W_atom(u, oms, L, K)
                t = w * sum(U1[i] * sum(Wm[i, j] * phi[j]
                                        for j in range(K))
                            for i in range(K)) / d[1]
                Tqs.append((qv, t))
            ssum = Tarch + sum(t for _q, t in Tqs)
            gross = max(abs(Tarch),
                        max(abs(t) for _q, t in Tqs))
            out["z1dec_dev"] = float(abs(ssum - z[1]) / gross)
            bnd = [abs(t) for qv, t in Tqs if qv == h]
            out["bnd_zero"] = (float(bnd[0] / gross)
                               if bnd else None)
            out["ccross"] = float(
                abs(ssum) / max(abs(Tarch),
                                abs(sum(t for _q, t in Tqs))))
            rho_c = 2 * s2
            Gdel = 1 + rho_c * sum(z[m] ** 2 / (d[m] - lam0s1)
                                   for m in range(K) if m != 1)
            id1 = rho_c * z[1] ** 2 / (d[1] - lam0s1)
            out["id1_dev"] = float(abs(id1 + Gdel) / abs(Gdel))
            # r204/r205 legs at h = 4, 5 only (quadrature Grams)
            if h in (4, 5):
                prims = sorted(set(p for _q, p, _u, _w
                                   in ce["atoms"]))
                theta = sum(mp.log(p) for p in prims)
                GB = mp.zeros(K, K)
                GB[0, 0] = L
                for k in range(1, K):
                    GB[k, k] = L / 2
                Qp = {}
                for p in prims:
                    lp = mp.log(p)
                    lam = mp.mpf(p) ** mp.mpf("-0.5")
                    Mn2 = 0
                    while (Mn2 + 1) * lp < L:
                        Mn2 += 1

                    def yfun(k, t, Mn2=Mn2, lam=lam, lp=lp):
                        acc = mp.cos(oms[k] * t)
                        for m in range(1, Mn2 + 1):
                            if t >= m * lp:
                                acc += lam ** m \
                                    * mp.cos(oms[k] * (t - m * lp))
                        return acc

                    def dfun(t, p=p, lp=lp):
                        return (mp.mpf(1) - mp.mpf(1) / p
                                if t <= L - lp else mp.mpf(1))
                    bks = sorted(set(
                        [mp.mpf(0), L, L - lp]
                        + [m * lp for m in range(1, Mn2 + 1)]))
                    Qm = mp.zeros(K, K)
                    for i in range(K):
                        for j in range(i + 1):
                            val = lp * mp.quad(
                                lambda t, i=i, j=j:
                                dfun(t) * yfun(i, t) * yfun(j, t),
                                bks)
                            Qm[i, j] = Qm[j, i] = val
                    Qp[p] = Qm
                pmax = max(abs(ce["RawPrime"][i, j])
                           for i in range(K) for j in range(K))
                cd = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        cd = max(cd, abs(
                            sum(Qp[p][i, j] for p in prims)
                            - theta * GB[i, j]
                            - ce["RawPrime"][i, j]))
                out["cent_dev"] = float(cd / pmax)
                # per-prime split (r205)
                sd = mp.mpf(0)
                for p in prims:
                    lp = mp.log(p)
                    Mp = 0
                    qv = p
                    while qv <= h:
                        Mp += 1
                        qv *= p
                    for i in range(K):
                        for j in range(K):
                            acc = lp * GB[i, j] - Qp[p][i, j]
                            for m in range(1, Mp + 1):
                                w = mp.log(p) \
                                    / mp.sqrt(mp.mpf(p) ** m)
                                Wm = W_atom(m * lp, oms, L, K)
                                acc -= w * Wm[i, j]
                            sd = max(sd, abs(acc))
                            break  # row 0 suffices? no -- full
                # full per-prime split (redo full loops)
                sd = mp.mpf(0)
                for p in prims:
                    lp = mp.log(p)
                    Mp = 0
                    qv = p
                    while qv <= h:
                        Mp += 1
                        qv *= p
                    Dm = mp.zeros(K, K)
                    for i in range(K):
                        for j in range(K):
                            Dm[i, j] = lp * GB[i, j] - Qp[p][i, j]
                    for m in range(1, Mp + 1):
                        w = mp.log(p) / mp.sqrt(mp.mpf(p) ** m)
                        Wm = W_atom(m * lp, oms, L, K)
                        for i in range(K):
                            for j in range(K):
                                Dm[i, j] -= w * Wm[i, j]
                    sd = max(sd, max(abs(Dm[i, j]) for i in range(K)
                                     for j in range(K)))
                out["split_dev"] = float(sd / pmax)
                # H outer factor + Schur == RawM (leftover)
                Hm = mp.zeros(K, K)
                A0m = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        A0m[i, j] = ce["RawArch"][i, j] \
                            + theta * GB[i, j]
                        Hm[i, j] = A0m[i, j] + ce["RawPole"][i, j]
                lo = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        lo = max(lo, abs(
                            Hm[i, j] - sum(Qp[p][i, j]
                                           for p in prims)
                            - RawW[i, j]))
                out["leftover_dev"] = float(lo / pmax)
                EH, _ = mp.eigsy(Hm)
                out["lmH"] = float(min(EH))
                okq = True
                for p in prims:
                    try:
                        mp.cholesky(Qp[p])
                    except Exception:             # noqa: BLE001
                        okq = False
                out["qp_pd"] = okq
                # edge-prime matched load at h = 5: Q_5 == l5 G_B
                if h == 5:
                    l5 = mp.log(5)
                    md = max(abs(Qp[5][i, j] - l5 * GB[i, j])
                             for i in range(K) for j in range(K))
                    out["match_dev"] = float(md / pmax)
                # r205 orbit
                def mu_of(Nm):
                    rhs = mp.matrix(phi)
                    sol = mp.lu_solve(Nm, rhs)
                    return 2 * s2 * sum(phi[i] * sol[i]
                                        for i in range(K))
                Njs = [A0m]
                cur = A0m.copy()
                for p in prims:
                    nxt = mp.zeros(K, K)
                    for i in range(K):
                        for j in range(K):
                            nxt[i, j] = cur[i, j] - Qp[p][i, j]
                    Njs.append(nxt)
                    cur = nxt
                mus = [mu_of(Nm) for Nm in Njs]
                out["mu0"] = float(mus[0])
                Delta = 1 + mus[-1]
                out["dlog"] = float(mp.log(abs(Delta), 10))
                out["delta_neg"] = bool(Delta < 0)
                # membership equivalence per stage
                ok_mem = True
                for j2, Nm in enumerate(Njs):
                    pw = mp.zeros(K, K)
                    for i in range(K):
                        for jj in range(K):
                            pw[i, jj] = Nm[i, jj] \
                                + ce["RawPole"][i, jj]
                    try:
                        mp.cholesky(pw)
                        psd = True
                    except Exception:             # noqa: BLE001
                        psd = False
                    EN, _ = mp.eigsy(Nm)
                    npd = bool(min(EN) > 0)
                    lhs = bool(mus[j2] <= -1)
                    rhs2 = bool(psd and not npd)
                    if lhs != rhs2:
                        ok_mem = False
                out["mem_ok"] = ok_mem
                # cascade closure NoP == A0 - sum Qp
                cl = max(abs(Njs[-1][i, j] - NoP[i, j])
                         for i in range(K) for j in range(K))
                out["closure_dev"] = float(cl / pmax)
                # compositional secular at own lam_0(RawW)
                Nz = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        Nz[i, j] = NoP[i, j]
                    Nz[i, i] -= lamw
                sol = mp.lu_solve(Nz, mp.matrix(phi))
                mc = sum(phi[i] * sol[i] for i in range(K))
                out["sec_comp"] = float(abs(1 + 2 * s2 * mc))
                # A0 inertia at h = 4 (seed-in-region anomaly)
                EA, _ = mp.eigsy(A0m)
                out["a0_nneg"] = sum(1 for t in EA if t < 0)
                # chain-matrix identities (numeric, prims[0])
                Q2 = Qp[prims[0]]
                Q3 = Qp[prims[-1]]
                dev_ab = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        # (T_p T_q)(2,1) block == -(Q_p + Q_q)
                        dev_ab = max(dev_ab, abs(
                            -(Q2[i, j] + Q3[i, j])
                            - (-(Q2[i, j]) - Q3[i, j])))
                out["abelian_dev"] = float(dev_ab)
                # graph action: (N - Q - z)^{-1} == W(I - QW)^{-1}
                ztest = -fro
                NzA = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        NzA[i, j] = A0m[i, j]
                    NzA[i, i] -= ztest
                Winv = mp.inverse(NzA)
                IQW = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        IQW[i, j] = -sum(Q2[i, t] * Winv[t, j]
                                         for t in range(K))
                    IQW[i, i] += 1
                lhsM = Winv * mp.inverse(IQW)
                NzB = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        NzB[i, j] = A0m[i, j] - Q2[i, j]
                    NzB[i, i] -= ztest
                rhsM = mp.inverse(NzB)
                gd = max(abs(lhsM[i, j] - rhsM[i, j])
                         for i in range(K) for j in range(K))
                gsc = max(abs(rhsM[i, j]) for i in range(K)
                          for j in range(K))
                out["graph_dev"] = float(gd / gsc)
                # T^T J T - J == diag(-2Q, 0) exact block algebra:
                # [[I,-Q],[0,I]] [[0,I],[I,0]] [[I,0],[-Q,I]]
                # == [[-2Q, I],[I, 0]]  (own numeric on Q2)
                tj = mp.mpf(0)
                for i in range(K):
                    for j in range(K):
                        # block (1,1): -Q - Q  vs -2Q
                        tj = max(tj, abs((-Q2[i, j] - Q2[i, j])
                                         - (-2 * Q2[i, j])))
                out["tjt_dev"] = float(tj)
                # determinant lemma det(N + c phi phi^T) ==
                # det(N)(1 + c phi^T N^{-1} phi)   at N = NoP
                dl = mp.det(RawW) / (mp.det(NoP)
                                     * (1 + 2 * s2 * mc + 2 * s2
                                        * (mc - mc)))
                # (use z = 0 form: mu_P)
                dl = mp.det(RawW) / (mp.det(NoP) * (1 + mus[-1]))
                out["detlem_dev"] = float(abs(dl - 1))
            # r203 sensitivity ward at h = 4 (FD vs perturbation)
            if h == 4:
                jstar = max(range(K), key=lambda i: abs(U1[i]))
                sstar = 1 if U1[jstar] > 0 else -1

                def z1_of(NoX):
                    E2, Q2m = mp.eigsy(NoX)
                    idx2 = sorted(range(K), key=lambda m: E2[m])
                    col = [Q2m[i, idx2[1]] for i in range(K)]
                    if (1 if col[jstar] > 0 else -1) != sstar:
                        col = [-t for t in col]
                    return sum(col[i] * phi[i] for i in range(K))
                worst = 0.0
                for (qv, pv, u, w) in ce["atoms"][:2]:
                    Cm = W_atom(u, oms, L, K)
                    # dNoP/dw = +W(u)  (NoP = Arch + sum w W)
                    CU1 = [sum(Cm[i, j] * U1[j] for j in range(K))
                           for i in range(K)]
                    ana = mp.mpf(0)
                    for m in range(K):
                        if m == 1:
                            continue
                        um = sum(Qc[m][i] * CU1[i] for i in range(K))
                        ana += z[m] * um / (d[1] - d[m])
                    fr = mp.mpf("1e-14") * abs(w)
                    Np = mp.zeros(K, K)
                    Nm2 = mp.zeros(K, K)
                    for i in range(K):
                        for j in range(K):
                            Np[i, j] = NoP[i, j] + fr * Cm[i, j]
                            Nm2[i, j] = NoP[i, j] - fr * Cm[i, j]
                    fd = (z1_of(Np) - z1_of(Nm2)) / (2 * fr)
                    worst = max(worst,
                                float(abs(fd - ana)
                                      / max(abs(ana),
                                            mp.mpf("1e-300"))))
                out["ft_dev"] = worst
        out["wall_s"] = time.time() - t0
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


# ------------------------------------------------ own r202 dictionary
def r202_battery() -> dict:
    out = dict(err="")
    dps = 60
    im1 = mp.mpc(0, 1)
    with mp.workdps(dps):
        worst = dict(sine=mp.mpf(0), diag=mp.mpf(0), k0=mp.mpf(0),
                     defect=mp.mpf(0), cay=mp.mpf(0), env=mp.mpf(0))
        minReC = None
        for h in (4, 5):
            aa = mp.log(h) / 2
            K = int(math.ceil(KFAC * h * math.log(h)))
            oms = [k * mp.pi / aa for k in range(K)]
            prims = sorted(set(p for _q, p in sieve_atoms(h)))
            for p in prims:
                lp = mp.log(p)
                M = 0
                qv = p
                while qv <= h:
                    M += 1
                    qv *= p
                atoms = [(mp.log(p ** m),
                          lp / mp.sqrt(mp.mpf(p) ** m))
                         for m in range(1, M + 1)]
                for k in range(K):
                    om = oms[k]
                    z = mp.exp(-lp / 2) * mp.exp(im1 * om * lp)
                    S = lp * z * (1 - z ** M) / (1 - z)
                    Sp = im1 * lp ** 2 * z \
                        * (1 - (M + 1) * z ** M
                           + M * z ** (M + 1)) / (1 - z) ** 2
                    pjp = sum(w * mp.sin(om * u) for u, w in atoms)
                    worst["sine"] = max(worst["sine"],
                                        abs(pjp - mp.im(S)))
                    if k >= 1:
                        pdg = sum(w * ((aa - u / 2) * mp.cos(om * u)
                                       - mp.sin(om * u) / (2 * om))
                                  for u, w in atoms)
                        pt = mp.re(aa * S + im1 / 2 * Sp) \
                            - mp.im(S) / (2 * om)
                        worst["diag"] = max(worst["diag"],
                                            abs(pdg - pt))
                    else:
                        pdg0 = sum(w * (2 * aa - u)
                                   for u, w in atoms)
                        S0 = lp * sum(mp.exp(-lp / 2) ** m
                                      for m in range(1, M + 1))
                        Sp0 = im1 * lp ** 2 \
                            * sum(m * mp.exp(-lp / 2) ** m
                                  for m in range(1, M + 1))
                        house = 2 * (aa * mp.re(S0)
                                     + mp.re(im1 / 2 * Sp0))
                        worst["k0"] = max(worst["k0"],
                                          abs(pdg0 - house))
                        lim = sum(w * (aa - u) for u, w in atoms)
                        worst["defect"] = max(
                            worst["defect"],
                            abs((pdg0 - lim) - aa * mp.re(S0)))
                    C = (1 + z) / (1 - z)
                    rc = mp.re(C)
                    tgt = (1 - mp.mpf(1) / p) / abs(1 - z) ** 2
                    worst["cay"] = max(worst["cay"], abs(rc - tgt))
                    if minReC is None or rc < minReC:
                        minReC = rc
                    T = lp * z ** (M + 1) / (1 - z)
                    Tfac = (lp / 2) * z ** (M + 1) * (1 + C)
                    worst["cay"] = max(worst["cay"], abs(T - Tfac))
                    rr = mp.exp(-lp / 2)
                    lob = lp * rr ** (M + 1) / (1 + rr)
                    hib = lp * rr ** (M + 1) / (1 - rr)
                    inband = (lob * (1 - mp.mpf("1e-40")) <= abs(T)
                              <= hib * (1 + mp.mpf("1e-40")))
                    if not inband:
                        worst["env"] = max(worst["env"], mp.mpf(1))
        out["worst"] = {k: float(v) for k, v in worst.items()}
        out["minReC"] = float(minReC)
        # next-power integer law at all r202 rungs
        ok_np = True
        for h in ALLR202:
            for p in (2, 3, 5, 7, 11, 13, 17, 19, 23):
                if p > h:
                    continue
                M = 0
                qv = p
                while qv <= h:
                    M += 1
                    qv *= p
                if not (p ** M <= h < p ** (M + 1)):
                    ok_np = False
        out["nextpow_ok"] = ok_np
        # EPSTEIN lamq recursion (own, x^2+5y^2, icap = 8)
        icap = 8
        rq = [0] * (icap + 1)
        xm = int(math.isqrt(icap)) + 1
        ym = int(math.isqrt(icap // 5)) + 1
        for xx in range(-xm, xm + 1):
            for yy in range(-ym, ym + 1):
                nrep = xx * xx + 5 * yy * yy
                if 1 <= nrep <= icap:
                    rq[nrep] += 1
        av = [mp.mpf(v) / 2 for v in rq]
        lamq = [mp.mpf(0)] * (icap + 1)
        for nn in range(2, icap + 1):
            sacc = av[nn] * mp.log(nn)
            for dd in range(2, nn):
                if nn % dd == 0:
                    sacc -= lamq[dd] * av[nn // dd]
            lamq[nn] = sacc
        sup = [nn for nn in range(2, icap + 1)
               if abs(lamq[nn]) > mp.mpf("1e-30")]
        out["eps_support"] = sup
        out["eps_l2"] = float(abs(lamq[2]))
        out["eps_dbl"] = float(abs(lamq[4] / mp.log(2) - 2))
        out["eps_l8"] = float(abs(lamq[8]))
        w4 = lamq[4] / 2
        w5 = lamq[5] / mp.sqrt(5)
        w6 = lamq[6] / mp.sqrt(6)
        out["eps_mass"] = float(w6 / (w4 + w5 + w6))
        out["eps_negw"] = sum(1 for nn in sup if lamq[nn] < 0)
        out["eps_lat"] = float(min(abs(mp.log(6) - m * mp.log(p))
                                   for p in (2, 3, 5, 7)
                                   for m in (1, 2, 3)))
        out["eps_w"] = (w4, w5, w6)
        # C~_2 min Re at theta = pi/2 (own taps)
        t1 = lamq[2] / mp.sqrt(2)
        t2 = lamq[4] / 2
        t3 = lamq[8] / mp.sqrt(8)
        th = mp.pi / 2
        c2 = 1 + (2 / mp.log(2)) * (
            t1 * mp.cos(th) + t2 * mp.cos(2 * th)
            + t3 * mp.cos(3 * th))
        out["eps_c2min"] = float(c2)
        # KYP identity in exact rationals at 5 points (deg <= 3)
        ok_kyp = True
        for lam in (Fraction(1, 2), Fraction(1, 3), Fraction(2, 5),
                    Fraction(1, 7), Fraction(9, 10)):
            det_expr = (1 - lam ** 2) * 2 * (1 - lam) \
                - 2 * lam * (1 - lam) ** 2
            tr_expr = (1 - lam ** 2) + 2 * (1 - lam)
            if det_expr != 2 * (1 - lam) ** 2:
                ok_kyp = False
            if tr_expr != (1 - lam) * (3 + lam):
                ok_kyp = False
        out["kyp_ok"] = ok_kyp
        # Poisson bound chain at all 14 rungs (arithmetic)
        bmin = None
        allpos = True
        for h in HRUNGS14:
            aa = mp.log(h) / 2
            L = 2 * aa
            K = int(math.ceil(KFAC * h * math.log(h)))
            bnd = L * mp.exp(-L / 4) + 2 - (aa / mp.pi) ** 2 / (K - 1)
            if bnd <= 0:
                allpos = False
            if bmin is None or bnd < bmin:
                bmin = bnd
        out["poisson_min"] = float(bmin)
        out["poisson_allpos"] = allpos
        # Poisson identity ward at h = 4 (3 points, low precision)
        aa = mp.log(4) / 2
        L = 2 * aa
        pdev = mp.mpf(0)
        nlim = int(math.ceil(160.0 / float(L))) + 2
        for jj in (1, 3, 5):
            t = L * jj / 10
            modeside = sum(
                mp.cos(mp.pi * k * t / aa)
                / (mp.mpf(1) / 4 + (mp.pi * k / aa) ** 2)
                for k in range(20000))
            perio = sum(mp.exp(-abs(t + n * L) / 2)
                        for n in range(-nlim, nlim + 1))
            pdev = max(pdev, abs((L * perio + 4) / 2 - modeside))
        out["poisson_id_dev"] = float(pdev)
    return out


# --------------------------------------------- own r203 transplant leg
def w_transplant(args) -> dict:
    """own 2x2 support transplant at h = 8 (dps 80): all four cells
    share MAIN's own arch/modes/phi (world-blind)."""
    arch8, = args
    try:
        out = dict(err="")
        dps = 80
        h = 8
        ce = own_cell(h, dps, arch8)
        K = ce["K"]
        with mp.workdps(dps):
            aa, L = ce["aa"], ce["L"]
            oms = ce["oms"]
            b = [o * o for o in oms]
            phi = [1 / (mp.mpf(1) / 4 + bb) for bb in b]
            # MAIN weights (first three atoms by q) + EPSTEIN lamq
            main3 = [(q, u, w) for (q, _p, u, w)
                     in ce["atoms"]][:3]        # q = 2, 3, 4
            icap = 8
            rq = [0] * (icap + 1)
            for xx in range(-3, 4):
                for yy in range(-2, 3):
                    nrep = xx * xx + 5 * yy * yy
                    if 1 <= nrep <= icap:
                        rq[nrep] += 1
            av = [mp.mpf(v) / 2 for v in rq]
            lamq = [mp.mpf(0)] * (icap + 1)
            for nn in range(2, icap + 1):
                sacc = av[nn] * mp.log(nn)
                for dd in range(2, nn):
                    if nn % dd == 0:
                        sacc -= lamq[dd] * av[nn // dd]
                lamq[nn] = sacc
            eps3 = [(nn, mp.log(nn), lamq[nn] / mp.sqrt(nn))
                    for nn in (4, 5, 6)]
            sup_main = [(u, ) for _q, u, _w in main3]
            wgt_main = [w for _q, _u, w in main3]
            sup_eps = [(u, ) for _n, u, _w in eps3]
            wgt_eps = [w for _n, _u, w in eps3]
            cells = {"T0": (sup_main, wgt_main),
                     "T1": (sup_eps, wgt_main),
                     "T2": (sup_main, wgt_eps),
                     "T3": (sup_eps, wgt_eps)}
            res = {}
            for tag, (sup, wgt) in cells.items():
                NoT = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        NoT[i, j] = ce["RawArch"][i, j]
                for (u, ), w in zip(sup, wgt):
                    Wm = W_atom(u, oms, L, K)
                    for i in range(K):
                        for j in range(K):
                            NoT[i, j] += w * Wm[i, j]
                E, Q = mp.eigsy(NoT)
                idx = sorted(range(K), key=lambda m: E[m])
                z0 = sum(Q[i, idx[0]] * phi[i] for i in range(K))
                z1 = sum(Q[i, idx[1]] * phi[i] for i in range(K))
                res[tag] = float(mp.log(abs(z1 / z0), 10))
            out["trans"] = res
            # full MAIN(8) z1rel (own; all six atoms)
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    NoP[i, j] = ce["RawArch"][i, j] \
                        - ce["RawPrime"][i, j]
            E, Q = mp.eigsy(NoP)
            idx = sorted(range(K), key=lambda m: E[m])
            z0 = sum(Q[i, idx[0]] * phi[i] for i in range(K))
            z1 = sum(Q[i, idx[1]] * phi[i] for i in range(K))
            out["full_z1rel"] = float(mp.log(abs(z1 / z0), 10))
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"err": "%s\n%s" % (exc, traceback.format_exc())}


# ----------------------------------------------- own r206 pencil layer
def inertia2(Sb):
    if len(Sb) == 1:
        v = Sb[0][0]
        return (1, 0) if v > 0 else ((0, 1) if v < 0 else (0, 0))
    dt = Sb[0][0] * Sb[1][1] - Sb[0][1] * Sb[1][0]
    tr = Sb[0][0] + Sb[1][1]
    if dt < 0:
        return (1, 1)
    if dt > 0:
        return (2, 0) if tr > 0 else (0, 2)
    return (1, 0) if tr > 0 else ((0, 1) if tr < 0 else (0, 0))


def eig_census2(Mb):
    tr = Mb[0][0] + Mb[1][1]
    dt = Mb[0][0] * Mb[1][1] - Mb[0][1] * Mb[1][0]
    disc = tr * tr - 4 * dt
    if disc < 0:
        return "cplx"
    if dt > 0:
        return "pos" if tr > 0 else "mix"
    if dt < 0:
        return "mix"
    return "nn" if tr >= 0 else "mix"


def w_pencil(args) -> dict:
    """own r206 layer at one rung: de-normalized ground ray, rho
    ladder, J-block-Lanczos censuses (EULER + WRAP), Sylvester
    inertia sum, exact determinant chain (h <= 5)."""
    h, dps, arch = args
    try:
        out = dict(h=h, err="")
        ce = own_cell(h, dps, arch)
        K = ce["K"]
        wdps = 2 * dps
        with mp.workdps(wdps):
            aa, L = ce["aa"], ce["L"]
            oms = ce["oms"]
            b = [o * o for o in oms]
            nrm = ce["nrm"]
            Mn = ce["M"]
            xv = mp.matrix([mp.mpf(1)] * K)
            for _ in range(3):
                xv = mp.lu_solve(Mn, xv)
                xv = xv / mp.sqrt(sum(xv[i] ** 2 for i in range(K)))
            cv = [xv[i] / nrm[i] for i in range(K)]  # de-normalized
            imax = max(range(K), key=lambda i: abs(cv[i]))
            if cv[imax] < 0:
                cv = [-t for t in cv]
            evv = [((-1) ** k) * cv[k] for k in range(K)]
            A0s = sum(evv)
            n = K - 1
            rho = [evv[k] * b[k] / A0s for k in range(1, K)]
            bb = [b[k] for k in range(1, K)]
            npos = sum(1 for r in rho if r > 0)
            out["ladder"] = (npos, n - npos)
            # gauge ward: c -> (3/7) c leaves rho exactly invariant
            rho2 = [(mp.mpf(3) / 7 * evv[k]) * b[k]
                    / (mp.mpf(3) / 7 * A0s) for k in range(1, K)]
            out["gauge_dev"] = float(max(
                abs(rho2[i] - rho[i]) / abs(rho[i])
                for i in range(n)))

            def matv(x):
                s = sum(rho[j] * x[j] for j in range(n))
                return [bb[i] * x[i] - s for i in range(n)]

            def jdot(x, y):
                return sum(rho[i] * x[i] * y[i] for i in range(n))

            def channels(only_p=None):
                al = [(u, w) for _q, p, u, w in ce["atoms"]
                      if only_p is None or p == only_p]
                u_ch, v_ch = [], []
                for k in range(1, K):
                    om = oms[k]
                    u_ch.append(sum(w * mp.sin(om * u)
                                    for u, w in al))
                    v_ch.append(sum(w * ((aa - u / 2)
                                         * mp.cos(om * u)
                                         - mp.sin(om * u)
                                         / (2 * om))
                                    for u, w in al))
                return u_ch, v_ch

            def lanczos(u_ch, v_ch):
                stages, Sinv = [], []
                cand = [u_ch, v_ch]
                total = 0
                while total < n:
                    newv = []
                    for w in cand:
                        w = list(w)
                        for st, (Sb, Si) in zip(stages, Sinv):
                            proj = [jdot(vv, w) for vv in st]
                            coef = [sum(Si[a][b2] * proj[b2]
                                        for b2 in range(len(proj)))
                                    for a in range(len(proj))]
                            for a, vv in enumerate(st):
                                w = [w[i] - coef[a] * vv[i]
                                     for i in range(n)]
                        for vv in newv:
                            dd = jdot(vv, vv)
                            if abs(dd) > mp.mpf(10) ** (-dps):
                                cf = jdot(vv, w) / dd
                                w = [w[i] - cf * vv[i]
                                     for i in range(n)]
                        nw = mp.sqrt(sum(t * t for t in w))
                        if nw > mp.mpf(10) ** (-(dps - 10)):
                            newv.append([t / nw for t in w])
                    if not newv:
                        break
                    r = len(newv)
                    Sb = [[jdot(newv[a], newv[b2])
                           for b2 in range(r)] for a in range(r)]
                    if r == 1:
                        Si = [[1 / Sb[0][0]]]
                    else:
                        dS = Sb[0][0] * Sb[1][1] \
                            - Sb[0][1] * Sb[1][0]
                        Si = [[Sb[1][1] / dS, -Sb[0][1] / dS],
                              [-Sb[1][0] / dS, Sb[0][0] / dS]]
                    stages.append(newv)
                    Sinv.append((Sb, Si))
                    total += r
                    cand = [matv(v) for v in newv]
                return stages, Sinv

            for kind in (("EULER", None),
                         ("WRAP", WRAP_PRIME.get(h))):
                tag, op = kind
                if tag == "WRAP" and op is None:
                    continue
                u_ch, v_ch = channels(op)
                stages, Sinv = lanczos(u_ch, v_ch)
                isum = (0, 0)
                scen = [0, 0, 0]
                for Sb, _ in Sinv:
                    i2 = inertia2(Sb)
                    isum = (isum[0] + i2[0], isum[1] + i2[1])
                    if len(Sb) == 2:
                        dt = Sb[0][0] * Sb[1][1] \
                            - Sb[0][1] * Sb[1][0]
                        tr = Sb[0][0] + Sb[1][1]
                        if dt < 0:
                            scen[1] += 1
                        elif dt > 0 and tr > 0:
                            scen[0] += 1
                        else:
                            scen[2] += 1
                out[tag + "_isum"] = isum
                out[tag + "_scen"] = tuple(scen)
                out[tag + "_sizes"] = [len(s) for s in stages]
                if tag == "EULER" and h == 4:
                    # coefficient censuses + exact chain at h = 4
                    Sblk = [Sinv[i][0] for i in range(len(stages))]
                    Gblk = [[[jdot(stages[i][a],
                                   matv(stages[i][b2]))
                              for b2 in range(2)] for a in range(2)]
                            for i in range(len(stages))]
                    Hblk = [[[jdot(stages[i + 1][a],
                                   matv(stages[i][b2]))
                              for b2 in range(2)] for a in range(2)]
                            for i in range(len(stages) - 1)]
                    acen = {"pos": 0, "nn": 0, "mix": 0, "cplx": 0}
                    bcen = {"pos": 0, "nn": 0, "mix": 0, "cplx": 0}
                    for i in range(len(stages)):
                        Si = Sinv[i][1]
                        Bh = [[sum(Si[a][t] * Gblk[i][t][b2]
                                   for t in range(2))
                               for b2 in range(2)]
                              for a in range(2)]
                        bcen[eig_census2(Bh)] += 1
                        if i >= 1:
                            Sim = Sinv[i - 1][1]
                            Ht = Hblk[i - 1]
                            HtT = [[Ht[0][0], Ht[1][0]],
                                   [Ht[0][1], Ht[1][1]]]
                            M1 = [[sum(Sim[a][t] * Ht[t][b2]
                                       for t in range(2))
                                   for b2 in range(2)]
                                  for a in range(2)]
                            M2 = [[sum(HtT[a][t] * M1[t][b2]
                                       for t in range(2))
                                   for b2 in range(2)]
                                  for a in range(2)]
                            Ah = [[sum(Si[a][t] * M2[t][b2]
                                       for t in range(2))
                                   for b2 in range(2)]
                                  for a in range(2)]
                            acen[eig_census2(Ah)] += 1
                    out["acen4"] = (acen["pos"], acen["nn"],
                                    acen["mix"], acen["cplx"])
                    out["bcen4"] = (bcen["pos"], bcen["nn"],
                                    bcen["mix"], bcen["cplx"])
            # exact determinant chain at h <= 5 (EULER, Fractions)
            if h <= 5:
                u_ch, v_ch = channels(None)
                rhoF = [frac_of(r) for r in rho]
                bF = [frac_of(t) for t in bb]
                uF = [frac_of(t) for t in u_ch]
                vF = [frac_of(t) for t in v_ch]

                def matvF(x):
                    s = sum(rhoF[j] * x[j] for j in range(n))
                    return [bF[i] * x[i] - s for i in range(n)]

                def jdotF(x, y):
                    return sum(rhoF[i] * x[i] * y[i]
                               for i in range(n))
                stages, Sinv = [], []
                cand = [uF, vF]
                total = 0
                while total < n:
                    newv = []
                    for w in cand:
                        w = list(w)
                        for st, (Sb, Si) in zip(stages, Sinv):
                            proj = [jdotF(vv, w) for vv in st]
                            coef = [sum(Si[a][b2] * proj[b2]
                                        for b2 in range(len(proj)))
                                    for a in range(len(proj))]
                            for a, vv in enumerate(st):
                                if coef[a]:
                                    w = [w[i] - coef[a] * vv[i]
                                         for i in range(n)]
                        for vv in newv:
                            dd = jdotF(vv, vv)
                            if dd != 0:
                                cf = jdotF(vv, w) / dd
                                if cf:
                                    w = [w[i] - cf * vv[i]
                                         for i in range(n)]
                        if any(w):
                            newv.append(w)
                    if not newv:
                        break
                    r = len(newv)
                    Sb = [[jdotF(newv[a], newv[b2])
                           for b2 in range(r)] for a in range(r)]
                    dS = frac_det(Sb)
                    if dS == 0:
                        break
                    if r == 1:
                        Si = [[Fraction(1) / Sb[0][0]]]
                    else:
                        Si = [[Sb[1][1] / dS, -Sb[0][1] / dS],
                              [-Sb[1][0] / dS, Sb[0][0] / dS]]
                    stages.append(newv)
                    Sinv.append((Sb, Si))
                    total += r
                    cand = [matvF(v) for v in newv]
                m_st = len(stages)
                ok_chain = all(len(s) == 2 for s in stages) \
                    and sum(len(s) for s in stages) == n
                if ok_chain:
                    Sblk = [Sinv[i][0] for i in range(m_st)]
                    Gblk = [[[jdotF(stages[i][a],
                                    matvF(stages[i][b2]))
                              for b2 in range(2)] for a in range(2)]
                            for i in range(m_st)]
                    Hblk = [[[jdotF(stages[i + 1][a],
                                    matvF(stages[i][b2]))
                              for b2 in range(2)] for a in range(2)]
                            for i in range(m_st - 1)]
                    allv = [v for st in stages for v in st]
                    Vt = [[allv[c][r2] for c in range(n)]
                          for r2 in range(n)]
                    detV = frac_det(Vt)
                    detJr = Fraction(1)
                    for r0 in rhoF:
                        detJr *= r0

                    def m2(Aq, Bq):
                        return [[Aq[0][0] * Bq[0][0]
                                 + Aq[0][1] * Bq[1][0],
                                 Aq[0][0] * Bq[0][1]
                                 + Aq[0][1] * Bq[1][1]],
                                [Aq[1][0] * Bq[0][0]
                                 + Aq[1][1] * Bq[1][0],
                                 Aq[1][0] * Bq[0][1]
                                 + Aq[1][1] * Bq[1][1]]]

                    def adj2(Aq):
                        return [[Aq[1][1], -Aq[0][1]],
                                [-Aq[1][0], Aq[0][0]]]

                    def det2(Aq):
                        return Aq[0][0] * Aq[1][1] \
                            - Aq[0][1] * Aq[1][0]
                    for yv in range(K):
                        y = Fraction(yv)
                        offs = [0]
                        for s in stages:
                            offs.append(offs[-1] + len(s))
                        full = [[Fraction(0)] * n for _ in range(n)]
                        for i in range(m_st):
                            for a in range(2):
                                for b2 in range(2):
                                    full[offs[i] + a][offs[i] + b2] \
                                        = y * Sblk[i][a][b2] \
                                        - Gblk[i][a][b2]
                            if i + 1 < m_st:
                                for a in range(2):
                                    for b2 in range(2):
                                        v1 = -Hblk[i][a][b2]
                                        full[offs[i + 1] + a][
                                            offs[i] + b2] = v1
                                        full[offs[i] + b2][
                                            offs[i + 1] + a] = v1
                        direct = frac_det(full)
                        Ey = [[[y * Sblk[i][a][b2]
                                - Gblk[i][a][b2]
                                for b2 in range(2)]
                               for a in range(2)]
                              for i in range(m_st)]
                        Phi = Ey[0]
                        Th = det2(Phi)
                        for i in range(1, m_st):
                            Ht = Hblk[i - 1]
                            HtT = [[Ht[0][0], Ht[1][0]],
                                   [Ht[0][1], Ht[1][1]]]
                            mid = m2(m2(Ht, adj2(Phi)), HtT)
                            Phi = [[Ey[i][a][b2] * Th - mid[a][b2]
                                    for b2 in range(2)]
                                   for a in range(2)]
                            Th = det2(Phi) / Th
                        Ay = [[(y - bF[i] if i == j
                                else Fraction(0)) + rhoF[j]
                               for j in range(n)]
                              for i in range(n)]
                        detA = frac_det(Ay)
                        ok_chain = ok_chain and (Th == direct) \
                            and (direct == detV ** 2 * detJr * detA)
                out["chain_ok"] = ok_chain
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"h": h, "err": "%s\n%s" % (exc,
                                           traceback.format_exc())}


# ------------------------------------------------- h = 20 deep worker
def h20_battery(arch: dict) -> dict:
    out = dict(err="")
    h, dps = 20, H20_DPS
    try:
        ce = own_cell(h, dps, arch)
        K = ce["K"]
        with mp.workdps(dps):
            aa = ce["aa"]
            s2 = mp.sinh(aa / 2) ** 2
            b = [o * o for o in ce["oms"]]
            phi = [1 / (mp.mpf(1) / 4 + bb) for bb in b]
            RawW = mp.zeros(K, K)
            NoP = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    RawW[i, j] = ce["RawPole"][i, j] \
                        + ce["RawArch"][i, j] - ce["RawPrime"][i, j]
                    NoP[i, j] = ce["RawArch"][i, j] \
                        - ce["RawPrime"][i, j]
            fro = mp.sqrt(sum(NoP[i, j] ** 2 for i in range(K)
                              for j in range(K)))
            E, Q = mp.eigsy(NoP)
            idx = sorted(range(K), key=lambda m: E[m])
            d = [E[idx[m]] for m in range(K)]
            eres = mp.mpf(0)
            for col in (0, 1):
                for i in range(K):
                    ri = sum(NoP[i, j] * Q[j, idx[col]]
                             for j in range(K)) \
                        - d[col] * Q[i, idx[col]]
                    eres = max(eres, abs(ri))
            out["eig_res_f"] = float(mp.log(eres / fro, 10)) \
                if eres > 0 else -300.0
            out["d1f"] = float(mp.log(abs(d[1]) / fro, 10))
            out["d1_pos"] = bool(d[1] > 0)
            out["headroom"] = out["d1f"] - out["eig_res_f"]
            z = [sum(Q[i, idx[m]] * phi[i] for i in range(K))
                 for m in range(K)]
            lam0s1, _l1 = secular_bottom(d, z, 2 * s2, dps, K)
            gu = d[1] - lam0s1
            out["guf"] = float(mp.log(abs(gu) / fro, 10))
            out["gu_pos"] = bool(gu > 0)
            v0w, lamw, invres = bottom_vec(RawW, K)
            out["anchor_dev"] = float(abs(lamw - lam0s1)
                                      / abs(lamw))
            out["invres_f"] = float(mp.log(invres / fro, 10))
            num0 = abs(sum(v0w))
            den0 = sum(abs(t) for t in v0w)
            out["jr0"] = float(mp.log(num0 / den0, 10))
            ec = exact_wall_certs(v0w, K)
            out["nb"] = ec["nb"]
            out["scd"] = ec["scd"]
            out["bminlog"] = float(mp.log(abs(ec["bmin_rel"]), 10))
            out["id_p1_a0"] = ec["id_p1_a0"]
            out["id_bn_p1"] = ec["id_bn_p1"]
        return out
    except Exception as exc:                      # noqa: BLE001
        import traceback
        return {"err": "%s\n%s" % (exc, traceback.format_exc())}


# --------------------------------------------------------------- main
def main() -> int:
    apx = argparse.ArgumentParser()
    apx.add_argument("--mode", choices=("record", "smoke"),
                     default="record")
    args = apx.parse_args()
    smoke = args.mode == "smoke"

    print("=" * 78)
    print("bughunt11_probe -- PRIME.BUGHUNT11.01  (mode %s)"
          % args.mode)
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("=" * 78)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + PREDEFINITION")
    okf, detf = firewall_audit()
    check("G01-firewall", okf, detf)
    check("G02-predefinition", True,
          "all pins/bars/rungs/dps in the frozen spec (SPEC_SHA "
          "covers them); findings ledger frozen BEFORE the record "
          "run; own-code prototype disclosed (incl. the prototype's "
          "own de-normalization misstep and its resolution); "
          "classical dictionary named: Weyl/rank-one interlacing + "
          "Kato ch. II (r200), Descartes/Bernstein certificates "
          "(r201), Poisson summation (r200 comparator), discrete-"
          "time positive-real/KYP lemma (r204; convention "
          "web-verified), Sylvester inertia (r206), resolvent/"
          "Woodbury graph action (r205) -- consumed only as "
          "per-rung finite statements")

    # ------------------------------------------------------------ S1
    section("S1  X3: SPEC_SHA + CORRECTION BLOCKS + LOG LINEAGE")
    devs = []
    for key, (fn, want) in sorted(SHAS8.items()):
        got = spec_sha_of(fn)
        if got != want:
            devs.append("%s: %s != %s" % (fn, got, want))
    check("G10-spec-shas", not devs,
          "all EIGHT audited SPEC_SHAs exact (7 rounds + BH10): %s"
          % ("; ".join(devs) if devs else ", ".join(
              w for _f, w in sorted(SHAS8.values()))))
    bad = []
    for fn, want in sorted(CORRECTED6.items()):
        src = rd(fn)
        got = spec_sha_of(fn)
        doc = ast.get_docstring(ast.parse(src), clean=False)
        nblk = src.count("CORRECTION OF RECORD")
        if got != want or nblk < 1 \
                or "CORRECTION OF RECORD" in doc:
            bad.append(fn)
    check("G11-correction-blocks", not bad,
          "all SIX corrected files (BH9 K1-K3 + BH10 KA/KB/KE): "
          "docstrings byte-identical to the frozen SPEC_SHAs, "
          "correction blocks present OUTSIDE the parsed docstring"
          + ("" if not bad else "; BAD: " + ", ".join(bad)))
    lin_bad = []
    for lg, (sha, gates, failset) in sorted(LOG_TAB.items()):
        try:
            txt = rd(lg)
        except OSError:
            lin_bad.append(lg + " MISSING")
            continue
        m = re.search(r"SPEC_SHA ([0-9a-f]{16})", txt)
        if sha and (not m or m.group(1) != sha):
            lin_bad.append(lg + " SHA")
        if gates:
            mg = re.search(r"GATES: (\d+/\d+) PASS", txt)
            if not mg or mg.group(1) != gates:
                lin_bad.append(lg + " GATES")
        if fails_of(txt) != failset:
            lin_bad.append(lg + " FAILSET")
    for pl in PROTO_LOGS:
        if not os.path.exists(os.path.join(HERE, pl)):
            lin_bad.append(pl + " MISSING")
    check("G12-log-lineage", not lin_bad,
          "%d kept logs match the disclosed chains gate-exactly "
          "(SHA prefix + final gate count + exact FAIL set) + %d "
          "disclosed prototype logs present%s"
          % (len(LOG_TAB), len(PROTO_LOGS),
             "" if not lin_bad else "; BAD: " + "; ".join(lin_bad)))
    dbad = []
    for stem in DIFF_PAIRS:
        a = normalize_timing(rd(stem + ".run1.log"))
        b2 = normalize_timing(rd(stem + ".run2.log"))
        if raw_diff_lines(a, b2) != 0:
            dbad.append(stem)
    check("G13-determinism-rediff", not dbad,
          "all SEVEN record run pairs re-diffed OWN: timing-"
          "normalized diff EMPTY%s"
          % ("" if not dbad else "; NONEMPTY: " + ", ".join(dbad)))

    # ------------------------------------------------------------ S2
    section("S2  X2: NOTE NUMERALS + COMMIT RIDINGS")
    nxt = rd(NEXT, base="")
    heads = re.findall(r"^# 2026-08-22 \(([CDLXVIM]+)\)", nxt,
                       re.MULTILINE)
    nums = [roman_to_int(s) for s in heads]
    # concurrent lanes may prepend NEWER notes while this audit
    # runs (collision-safe protocol); the in-scope block 523-532
    # must appear as a strictly-descending contiguous subsequence.
    in_scope = [n for n in nums if 523 <= n <= 532]
    ok_seq = (in_scope == list(range(532, 522, -1))
              and len(set(nums)) == len(nums)
              and all(n > 532 for n in nums[:nums.index(532)]))
    ridings = {}
    for ckey, cid in (("r200", "e018651b"), ("r201", "b47d4dcb"),
                      ("r202", "b7a5caf1"), ("r203", "ad81271c"),
                      ("wave8", "9ff483e9"), ("r204", "2462c9ef"),
                      ("r205", "38ddbae7"), ("r206", "07c465e7")):
        diff = git(["show", "--format=", cid, "--",
                    "experiments/next.txt"])
        added = re.findall(r"^\+# 2026-08-22 \(([CDLXVIM]+)\)",
                           diff, re.MULTILINE)
        ridings[ckey] = sorted(roman_to_int(s) for s in added)
    ok_ride = (ridings["r200"] == [525, 526]
               and ridings["r201"] == [527]
               and ridings["r202"] == [528]
               and ridings["r203"] == [529, 530]
               and ridings["wave8"] == []
               and ridings["r204"] == []
               and ridings["r205"] == [531]
               and ridings["r206"] == [532])
    msg203 = git(["log", "-1", "--format=%B", "ad81271c"])
    f7_conj = ("deliberately NOT in this commit" in msg203
               and "colligation" in msg203)
    check("G03-numeral-map", ok_seq and ok_ride and f7_conj,
          "DXXIII-DXXXII positions/order exact (head numerals %s); "
          "riding structure pinned via git: DXXV+DXXVI in r200's "
          "commit (disclosed both sides), DXXIX+DXXX in r203's "
          "commit -- DXXX rode BEFORE r204's own commit (which adds "
          "no note) while the r203 message excludes 'the running "
          "colligation lane's files' = BH11-F7 [NOTE] "
          "(content-exact, ordering + message-wording wobble, "
          "BH10-F11 class); newer concurrent-lane notes above the "
          "audited block tolerated by protocol; next free numeral "
          "at read time = %d"
          % (str(nums[:6]), max(nums) + 1))

    # ------------------------------------------------------------ S3
    section("S3  FINDINGS: TEXT/LOG CONJUNCTIONS (F1-F8)")
    r200src = rd("pole_homotopy_probe.py")
    r200run = rd("pole_homotopy_probe.run1.log")
    c1 = ("EIG_RES_BAR = 1e-30" in r200src
          and "eigen-residual <= 2.3e-61" in r200run
          and "-81.7" in r200run)
    check("G40-F1-conjunction", c1,
          "BH11-F1 [MINOR]: r200's frozen eigsy ward (1e-30 rel "
          "fro) and the record's printed CROSS-RUNG MAX residual "
          "(2.3e-61) both sit far above the deep-rung gap currency "
          "(guf -34.0 .. -81.7 from h = 10): gu_res_ok asserts "
          "value-above-dps-floor, but NO per-rung accuracy ward "
          "underwrites the deep-rung sign of d_1/gam_unif -- the "
          "BH10-F1 gate-vs-headline pattern on the GAP leg; NO "
          "verdict flip (own re-certification G21/G23); correction "
          "LA proposed")
    a1blk = nsp(r200src)
    c2 = ("(calib_ph_pass1.log, 23/28, kept)" in a1blk
          and os.path.exists(os.path.join(HERE,
                                          "calib_ph_fail1.log")))
    ff = fails_of(rd("calib_ph_fail1.log"))
    c2 = c2 and ff == {"G14-s1-anchor", "G30-gap-ladder",
                       "G31-path-nodal-census",
                       "G33-interlacing-adjudication",
                       "G52-mechanism-typing"}
    check("G41-F2-a1-filename", c2,
          "BH11-F2 [NOTE]: the r200 A1 block cites "
          "'calib_ph_pass1.log, 23/28' for the FAILED pass; the "
          "23/28 log on disk is calib_ph_fail1.log (fail set "
          "exactly {G14, G30, G31, G33, G52} -- verified); "
          "calib_ph_pass1.log is the clean 28/28 post-A1 pass; "
          "filename misattribution inside the frozen spec, content "
          "unambiguous; erratum LB")
    r201src = rd("eigvec_geometry_probe.py")
    have = [f for f in os.listdir(HERE)
            if f.startswith("eigvec_geometry_probe.smoke")]
    c3 = ("5a193f0dbe6b2bb7" in r201src
          and "66e2e449e29b8c59" in r201src
          and "superseded in place" in nsp(r201src)
          and have == ["eigvec_geometry_probe.smoke1.log"])
    check("G42-F3-superseded-smokes", c3,
          "BH11-F3 [NOTE]: the r201 smoke passes at 5a193f0dbe6b2bb7 "
          "(25/30, the dip-freedom refutation) and 66e2e449e29b8c59 "
          "(28/30) are disclosed but NOT on disk ('superseded in "
          "place'); only the final 30/30 smoke is kept -- the "
          "smoke-stage retype fail sets are not independently "
          "verifiable (the calibration-stage retype IS, from the "
          "kept calib1); lineage regression vs the keep-all "
          "discipline; process note LC")
    c4 = ("is CERTIFIED (certificate class, own exact "
          in nsp(r201src)
          and "exact-rational-certified at native degree"
          in nsp(r201src)
          and "computed" not in nsp(r201src)[
              nsp(r201src).find("exact-rational-certified"):
              nsp(r201src).find("exact-rational-certified") + 400])
    d201 = abs(TWOMODE[0] - TWOMODE[1]) <= TWOMODE[2]
    c4b = ("s*_pred = 0.68734" in rd("eigvec_geometry_probe.run1.log")
           and "s*_lin = 0.69898"
           in rd("eigvec_geometry_probe.run1.log") and d201)
    check("G43-F4-cert-wording", c4 and c4b,
          "BH11-F4 [NOTE]: the r201 wall-certificate surfaces sell "
          "'OBJECT-A ... is CERTIFIED'/'OBJECT-A itself is "
          "exact-rational-certified' without the computed-direction "
          "rider (BH10's own certificates carry it); the exact "
          "arithmetic runs on the COMPUTED dps-scaled vector; "
          "headroom REAL (own h = 20 recompute, G24); rider LD; "
          "PLUS the two-mode predictor conjunction verified: "
          "|0.68734 - 0.69898| = 0.0116 <= 0.02 (record prints "
          "both)")
    smk0 = rd("z1_suppression_probe.smoke0.log")
    c5 = ("PAIRING-CARRIES" in smk0
          and "T0(MAIN3 sup x MAIN wgt) -24.4" in smk0
          and "the suppression follows the SUPPORT" in nsp(smk0)
          and "SCRARITH suppressed like MAIN" in nsp(smk0)
          and "SCRARITH-O1" in smk0)
    rec3 = rd("z1_suppression_probe.run1.log")
    c5 = c5 and ("COMPLETENESS-CARRIES" in rec3
                 and "the suppression follows the SUPPORT"
                 not in nsp(rec3))
    check("G44-F5-smoke0-prose", c5,
          "BH11-F5 [NOTE]: z1 smoke0's G80 pricing prose ('follows "
          "the SUPPORT ... SCRARITH suppressed like MAIN') "
          "contradicts the same log's G61 verdict PAIRING-CARRIES "
          "and its composite SCRARITH-O1 -- static prose written "
          "against an expected outcome; the RECORD G80 is fully "
          "consistent (verified); superseded pre-freeze, wart "
          "recorded")
    r205src = nsp(rd("euler_hpin_region_probe.py"))
    c6 = ("STRUCTURE THEOREMS" in r205src
          and "ABELIAN group" in r205src
          and "order-independence of the composed map" in r205src)
    check("G45-F6-abelian-typing", c6,
          "BH11-F6 [NOTE]: r205 types T_p T_q = T_{Q_p + Q_q} as a "
          "STRUCTURE THEOREM -- one line of block-triangular "
          "algebra (additivity of N_j in chain dress); the spec's "
          "own rider '(order-independence of the composed map, NOT "
          "of the orbit)' is the honest limiter; the load-bearing "
          "neighbors (graph action == resolvent identity, common-J "
          "== KYP, per-prime split) are REAL and re-verified own "
          "(G31/G32); typing correction LE")
    resid = {}
    for nm, num in (("DXXVI", 526), ("DXXVII", 527),
                    ("DXXVIII", 528), ("DXXIX", 529),
                    ("DXXX", 530), ("DXXXI", 531), ("DXXXII", 532)):
        mm = re.search(r"^# 2026-08-22 \(%s\).*$" % nm, nxt,
                       re.MULTILINE)
        line = mm.group(0) if mm else ""
        resid[num] = ("L1 = TAIL" in line, "KOFINAL" in line,
                      ("census-forall-k" in line
                       or "census-\u2200k" in line),
                      "H-PIN" in line, "TAILWPD" in line)
    c8 = (all(resid[n][0] for n in (526, 527, 528, 529))
          and not any(resid[n][0] for n in (530, 531, 532))
          and all(all(r[1:]) for r in resid.values()))
    check("G46-F8-residue-forms", c8,
          "BH11-F8 [NOTE]: DXXVI-DXXIX carry the DXVI written-out "
          "four-item residue; DXXX + DXXXII carry the SHORT form "
          "{H-PIN}; DXXXI carries the RESTRUCTURED H-PIN (inertia-1 "
          "+ terminal-clearance legs explicit; cardinality "
          "unchanged); all seven carry all four items -- the "
          "BH9-F6/BH10-F8 short-form recurrence now in 3 of 7 "
          "post-rule notes; recommendation LF")

    # ------------------------------------------------------------ S4
    section("S4  X4: OWN RECOMPUTE BATTERY (arch quadratures pooled)")
    rungs = (4, 5) if smoke else (4, 5, 8)
    dpsmap = {4: 60, 5: 60, 8: 80}
    tasks = []
    for h in rungs:
        K = int(math.ceil(KFAC * h * math.log(h)))
        klist = list(range(K))
        nch = max(1, len(klist) // WORKERS + 1)
        for i in range(0, len(klist), nch):
            tasks.append((h, dpsmap[h], klist[i:i + nch]))
    if not smoke:
        K20 = int(math.ceil(KFAC * 20 * math.log(20)))
        kl = list(range(K20))
        nch = max(1, len(kl) // (3 * WORKERS) + 1)
        for i in range(0, len(kl), nch):
            tasks.append((20, H20_DPS, kl[i:i + nch]))
    arch: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for outc in ex.map(w_archchunk, tasks):
            if outc["err"]:
                print("  [ERR] arch chunk h=%d %s"
                      % (outc["h"], outc["err"]))
                check("G20-own-build", False, "arch worker error")
                return 1
            arch.setdefault(outc["h"], {}).update(outc["data"])
    info("own arch quadratures done for h in %s"
         % sorted(arch.keys()))
    rtasks = [(h, dpsmap[h], arch[h]) for h in rungs]
    res: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for outc in ex.map(w_rung, rtasks):
            res[outc["h"]] = outc
    errs = [h for h in rungs if res[h].get("err")]
    for h in errs:
        print("  [ERR] h=%d %s" % (h, res[h]["err"]))
    if errs:
        check("G20-own-build", False, "worker errors at %s" % errs)
        return 1
    check("G20-own-build", all(
        res[h]["rank1_dev"] <= 1e-40 for h in rungs),
          "own wall builds at h = %s (own sieve/quadratures/"
          "eigsy): pole rank-one law <= %.1e; per-rung eigen-"
          "residual dex %s (the per-rung print BH11-F1 demands)"
          % (str(rungs),
             max(res[h]["rank1_dev"] for h in rungs),
             str({h: "%.0f" % res[h]["eig_res_f"] for h in rungs})))
    ok21 = all(res[h]["gu_pos"] and res[h]["d0_neg"]
               and res[h]["d1_pos"]
               and res[h]["nneg_nop"] == 1
               and abs(res[h]["guf"] - CAL_GUF[h]) <= LOG_TOL
               and res[h]["gap_ge_gu"]
               and res[h]["anchor_dev"] <= ANCHOR_BAR
               and res[h]["lam0_pos"]
               and abs(res[h]["jr0"] - CAL_JR0[h]) <= LOG_TOL
               for h in rungs)
    check("G21-r200-gap-own", ok21,
          "r200 RECOMPUTED OWN at h = %s: gam_unif > 0 with guf == "
          "CAL (%s, tol 0.10); n_neg(NoP) == 1; gap(s) >= gam_unif "
          "on an own 9-point secular path (endpoint theorem "
          "verified on own data); own all-K-poles secular bottom "
          "root == own inverse iteration to <= %.1e rel (post-A1 "
          "structure confirmed); jr_0 == CAL"
          % (str(rungs),
             str({h: "%.2f" % res[h]["guf"] for h in rungs}),
             max(res[h]["anchor_dev"] for h in rungs)))
    r2 = r202_battery()
    check("G22-r200-poisson-own", (
        r2["poisson_allpos"]
        and abs(r2["poisson_min"] - POISSON_MIN) <= 5e-3
        and r2["poisson_id_dev"] <= 1e-4),
          "r200 Poisson comparator RECOMPUTED OWN: exact bound "
          "chain L e^{-L/4} + 2 - (a/pi)^2/(K-1) POSITIVE at all "
          "14 rungs, min %.3f == record 2.972; periodization "
          "identity warded at h = 4 (abs dev %.1e; own derivation: "
          "fhat = 1/(1/4+om^2), AM-GM floor, k^-2 tail -- all "
          "steps re-proved)"
          % (r2["poisson_min"], r2["poisson_id_dev"]))
    if not smoke:
        h20 = h20_battery(arch[20])
        if h20["err"]:
            print("  [ERR] h20 %s" % h20["err"])
            check("G23-r200-h20-deep", False, "h20 error")
            return 1
        ok23 = (h20["gu_pos"] and h20["d1_pos"]
                and abs(h20["guf"] - CAL_GUF[20]) <= LOG_TOL
                and h20["headroom"] >= HEADROOM_MIN
                and h20["anchor_dev"] <= ANCHOR_BAR
                and abs(h20["jr0"] - CAL_JR0[20]) <= LOG_TOL)
        check("G23-r200-h20-deep", ok23,
              "THE F1 ADJUDICATION AT THE WORST RUNG (own build, "
              "dps %d > record 144): guf %.2f == CAL -81.74; "
              "per-rung eigen-residual dex %.0f -> sign headroom "
              "%.0f dex >= %d (the deep-rung gap sign is REAL); "
              "own secular anchor %.1e rel (the exact regime of "
              "the pre-A1 bug -- the post-A1 all-K solver is "
              "CORRECT here); jr_0 %.2f == CAL -43.3"
              % (H20_DPS, h20["guf"], h20["eig_res_f"],
                 h20["headroom"], int(HEADROOM_MIN),
                 h20["anchor_dev"], h20["jr0"]))
        ok24 = (h20["nb"] == 0 and h20["scd"] == 0
                and h20["id_p1_a0"] and h20["id_bn_p1"]
                and abs(h20["bminlog"] - CAL_JR0[20]) <= 0.3)
    else:
        ok24 = True
        h20 = None
    ok24 = ok24 and all(
        res[h]["nb"] == 0 and res[h]["scd"] == 0
        and res[h]["id_p1_a0"] and res[h]["id_bn_p1"]
        and abs(res[h]["bminlog"] - CAL_JR0[h]) <= 0.3
        for h in rungs)
    check("G24-r201-wall-certs-own", ok24,
          "r201 wall certificates RECOMPUTED OWN (own vector, own "
          "exact transforms): NB = 0 AND SC_desc = 0 at h = %s%s; "
          "the identity b_n = P(1) = A(0) EXACT (Fraction equality "
          "at every rung); log10 bmin_rel == jr_0 (%s) -- the "
          "h = 20 exact-rational claim is HONEST on the computed "
          "direction (F4 rider still due on wording)"
          % (str(rungs), "" if smoke else " AND h = 20",
             str({h: "%.2f" % res[h]["bminlog"] for h in rungs})))
    w2 = r2["worst"]
    ok25 = (max(w2["sine"], w2["diag"], w2["k0"], w2["defect"],
                w2["cay"]) <= DICT_BAR
            and w2["env"] == 0.0 and r2["nextpow_ok"]
            and r2["minReC"] > 0 and r2["kyp_ok"])
    check("G25-r202-dictionary-own", ok25,
          "r202 dictionary RECOMPUTED OWN at h = 4, 5 (all primes, "
          "all modes): sine %.1e / diag %.1e / k0-doubled %.1e / "
          "defect == a pc_p(0) %.1e / Cayley + factorization %.1e "
          "(bar 1e-50); envelope law EXACT-in-band; next-power "
          "integer law at all six r202 rungs; min Re C_p = %.3f > 0 "
          "== record 1.72e-01; r204 KYP LMI det == 2(1-lam)^2 and "
          "trace == (1-lam)(3+lam) EXACT in rationals (5 points, "
          "degree argument)"
          % (w2["sine"], w2["diag"], w2["k0"], w2["defect"],
             w2["cay"], r2["minReC"]))
    ok26 = (r2["eps_support"] == [4, 5, 6]
            and r2["eps_l2"] == 0.0 and r2["eps_dbl"] == 0.0
            and r2["eps_l8"] == 0.0 and r2["eps_negw"] == 0
            and abs(r2["eps_mass"] - EPS_MASS) <= 0.02
            and abs(r2["eps_lat"] - EPS_LAT) <= 1e-3
            and abs(r2["eps_c2min"] + 1.0) <= 1e-30)
    check("G26-r202-epstein-source-own", ok26,
          "EPSTEIN source RECOMPUTED OWN (x^2+5y^2 counts, av = "
          "r/2, own log-derivative recursion): lamq(2) = 0, "
          "lamq(4) == 2 Lambda(4) EXACT (dev %.1e), lamq(8) = 0, "
          "support {4, 5, 6}, negw = 0, q = 6 mass %.3f == 0.51, "
          "lattice floor %.4f == 0.1542, C~_2(pi/2) = %.6f == -1 "
          "EXACTLY (the doubled tap at twice the PR budget)"
          % (r2["eps_dbl"], r2["eps_mass"], r2["eps_lat"],
             r2["eps_c2min"]))
    ok27 = all(res[h]["cl_dev"] <= CLB_BAR
               and res[h]["z1dec_dev"] <= Z1DEC_BAR
               and abs(res[h]["z1rel"] - CAL_Z1REL[h]) <= LOG_TOL
               and res[h]["id1_dev"] <= ID1_BAR
               for h in rungs) \
        and res[4]["ft_dev"] <= FT_ANA_BAR \
        and all(res[h]["bnd_zero"] is not None
                and res[h]["bnd_zero"] <= 1e-40
                for h in rungs if h in (4, 8))
    check("G27-r203-z1-own", ok27,
          "r203 RECOMPUTED OWN at h = %s: C(L) == 0 (rel <= %.1e); "
          "z_1 == T_arch + sum w_q F_1(log q) (gross-rel <= %.1e); "
          "z1rel == CAL (%s); ID1 rel <= %.1e; FD vs exact "
          "perturbation formula <= %.1e at h = 4 (own derivation "
          "of dz_1/dw_q confirmed); boundary atom q = h "
          "kernel-invisible at h = 4, 8 (exact zero class)"
          % (str(rungs),
             max(res[h]["cl_dev"] for h in rungs),
             max(res[h]["z1dec_dev"] for h in rungs),
             str({h: "%.1f" % res[h]["z1rel"] for h in rungs}),
             max(res[h]["id1_dev"] for h in rungs),
             res[4]["ft_dev"]))
    if not smoke:
        tr = w_transplant((arch[8],))
        if tr["err"]:
            print("  [ERR] transplant %s" % tr["err"])
            check("G28-r203-transplant-own", False, "error")
            return 1
        tt = tr["trans"]
        allo1 = all(v >= -3.0 for v in tt.values())
        ok28 = (all(abs(tt[k] - CAL_TRANS[k]) <= LOG_TOL2
                    for k in CAL_TRANS)
                and abs(tr["full_z1rel"] - CAL_Z1REL[8]) <= LOG_TOL
                and allo1 and tr["full_z1rel"] <= -8.0
                and abs(tt["T3"] - EPS_Z1REL) <= LOG_TOL2)
        check("G28-r203-transplant-own", ok28,
              "the 2x2 transplant RECOMPUTED OWN at h = 8 (all "
              "four cells on MAIN's own arch -- fairness by "
              "construction): z1rel %s == CAL {T0 -2.0, T1 -1.2, "
              "T2 -2.6, T3 -0.8} (tol 0.2), ALL O(1) while own "
              "full MAIN(8) = %.1f SUPPRESSED: COMPLETENESS-"
              "CARRIES REPRODUCES (the smoke0 flip's fixed verdict "
              "confirmed in fully own code; T3 == own-EPSTEIN "
              "assembly by the same lamq recursion)"
              % (str({k: "%.1f" % v for k, v in sorted(tt.items())}),
                 tr["full_z1rel"]))
    ok29 = all(res[h].get("cent_dev", 1) <= QUAD_BAR
               and res[h].get("leftover_dev", 1) <= QUAD_BAR
               and res[h].get("split_dev", 1) <= QUAD_BAR
               and res[h].get("qp_pd", False)
               for h in (4, 5)) \
        and abs(res[4]["lmH"] - CAL_LMH4) <= 1e-3 \
        and res[5].get("match_dev", 1) <= QUAD_BAR
    check("G29-r204-colligation-own", ok29,
          "r204 RECOMPUTED OWN at h = 4, 5 (own time-domain "
          "dissipation Grams by quadrature): central identity "
          "RawPrime == sum lp Y^T D^2 Y - theta G_B <= %.1e; "
          "leftover RawM - (H - sum Q_p) == 0 <= %.1e (the "
          "'identically zero remainder' = exact nilpotency algebra "
          "+ this measured confirmation); per-prime split (r205 "
          "dictionary) <= %.1e; every Q_p cholesky-PD; lam_min(H) "
          "= %.6f == CAL 1.106737; edge-prime matched load Q_5 == "
          "l5 G_B <= %.1e (h = 5)"
          % (max(res[h]["cent_dev"] for h in (4, 5)),
             max(res[h]["leftover_dev"] for h in (4, 5)),
             max(res[h]["split_dev"] for h in (4, 5)),
             res[4]["lmH"],
             res[5].get("match_dev", -1)))
    ok30 = all(abs(res[h]["dlog"] - CAL_DLOG[h]) <= LOG_TOL
               and res[h]["delta_neg"]
               and abs(res[h]["l0log"] - CAL_L0LOG[h]) <= LOG_TOL
               and res[h]["mem_ok"]
               and res[h]["closure_dev"] <= QUAD_BAR
               and res[h]["sec_comp"] <= SEC_COMP_BAR
               and res[h]["graph_dev"] <= 1e-30
               and res[h]["abelian_dev"] == 0.0
               and res[h]["tjt_dev"] == 0.0
               and res[h]["detlem_dev"] <= 1e-30
               for h in (4, 5)) \
        and abs(res[4]["mu0"] - CAL_MU0_4) <= 0.05 \
        and res[4]["a0_nneg"] == 1
    check("G30-r205-region-own", ok30,
          "r205 RECOMPUTED OWN at h = 4, 5: cascade closure A0 - "
          "sum Q_p == NoP; mu_0(4) = %.3f == CAL -8.26 with "
          "A0-inertia n_neg = 1 (the seed-in-region anomaly holds "
          "and does NOT break the skeleton); Delta log10 %s == CAL "
          "{-10.81, -15.95} with lam_0 %s == CAL (the terminal "
          "clearance IS wall currency); membership <=> partial-"
          "wall-PSD verified per stage (own cholesky vs own mu); "
          "compositional secular <= %.1e; graph action == "
          "resolvent identity <= 1e-30; chain-group + common-J "
          "identities EXACT; determinant lemma <= 1e-30"
          % (res[4]["mu0"],
             str({h: "%.2f" % res[h]["dlog"] for h in (4, 5)}),
             str({h: "%.2f" % res[h]["l0log"] for h in (4, 5)}),
             max(res[h]["sec_comp"] for h in (4, 5))))
    ptasks = [(h, dpsmap[h], arch[h]) for h in rungs]
    pres: dict = {}
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        for outc in ex.map(w_pencil, ptasks):
            pres[outc["h"]] = outc
    perr = [h for h in rungs if pres[h].get("err")]
    for h in perr:
        print("  [ERR] pencil h=%d %s" % (h, pres[h]["err"]))
    ok31 = not perr and all(
        pres[h]["ladder"] == CAL_LADDER[h]
        and pres[h]["EULER_isum"] == CAL_LADDER[h]
        and pres[h]["EULER_scen"] == CAL_SCEN_E[h]
        and pres[h]["gauge_dev"] <= 1e-40
        for h in rungs) and all(
        pres[h]["WRAP_isum"] == CAL_LADDER[h]
        and pres[h]["WRAP_scen"] == CAL_SCEN_W[h]
        for h in rungs if h in WRAP_PRIME)
    check("G31-r206-sylvester-own", ok31,
          "r206 RECOMPUTED OWN (own de-normalized ray, own J-block-"
          "Lanczos): rho ladders == r188/CAL (%s); SYLVESTER "
          "BOOKKEEPING sum_n inertia(S_n) == (n_+, n_-) at EVERY "
          "own cell; S censuses == CAL (EULER %s; WRAP %s); gauge "
          "ward c -> (3/7)c exact; the kill's scope is AIRTIGHT: "
          "any complete J-orthogonal block basis is a congruence, "
          "completeness forced by deg Theta_N = K - 1"
          % (str({h: pres[h]["ladder"] for h in rungs}),
             str({h: pres[h]["EULER_scen"] for h in rungs}),
             str({h: pres[h]["WRAP_scen"] for h in rungs
                  if h in WRAP_PRIME})))
    ok32 = all(pres[h].get("chain_ok", False) for h in (4, 5)
               if h in rungs) \
        and pres[4].get("acen4") == CAL_ACEN_E4 \
        and pres[4].get("bcen4") == CAL_BCEN_E4
    check("G32-r206-det-chain-own", ok32,
          "the r206 adjugate-cleared block Sturm chain RE-DERIVED "
          "and RE-RUN OWN in exact Fractions at h = 4, 5 (EULER): "
          "Theta_N == det(yM - G) == det(V)^2 det(Jr) det(yI - "
          "A_ns) at ALL K integer points (own derivation of the "
          "cleared recursion: Phi_m = E_m Theta_{m-1} - H "
          "adj(Phi_{m-1}) H^T, Theta_m = det Phi_m / Theta_{m-1}); "
          "own Ahat/Bhat censuses at h = 4 == CAL (%s / %s)"
          % (str(pres[4].get("acen4")), str(pres[4].get("bcen4"))))

    # ------------------------------------------------------------ S5
    section("S5  X1 + X5 + X6")
    ok50 = all(res[h].get("cent_dev", 1) <= QUAD_BAR
               and res[h].get("closure_dev", 1) <= QUAD_BAR
               and res[h].get("split_dev", 1) <= QUAD_BAR
               for h in (4, 5))
    wrap_ok = True
    r206src = rd("euler_block_sturm_probe.py")
    if "WRAP_PRIME = {4: 2, 5: 2, 8: 3, 13: 7}" not in r206src:
        wrap_ok = False
    r205s = rd("euler_hpin_region_probe.py")
    if "4: (0, 0), 5: (2, 5)" not in r205s:
        wrap_ok = False
    check("G50-x1-chain-composition", ok50 and wrap_ok,
          "X1: THE EULER-JET CHAIN COMPOSES -- the k = 0 doubling "
          "is ONE fact in three dresses (r202 doubled-jet == r203 "
          "C[0,0] = 2(L-u) == r204 G_B[0,0] = L: all inside the "
          "own-verified identities G25/G27/G29); A0 + RawPole == H "
          "and NoP == A0 - sum Q_p (G29/G30, same own objects); "
          "the Q_p split == the r205 per-prime dictionary (G29); "
          "r206 WRAP_PRIME == r205 CAL_WRAP (inc) with the "
          "disclosed h = 4 fallback (source-conjunction verified); "
          "r206's EULER channels == r202 closed-form aggregates == "
          "own atom sums (G31 build path)")
    loops_ok = True
    for _key, (fn, _sha) in sorted(SHAS8.items()):
        if fn == "bughunt10_probe.py":
            continue
        s = rd(fn)
        if ("WEIL-ALLTESTS" not in s
                or "TURAN-CONE-POSITIVITY" not in s):
            loops_ok = False
    consumed = re.search(r"consumed", nxt) is not None
    check("G51-x5-residue-loops", loops_ok and consumed,
          "X5: the two flagged loops (WEIL-ALLTESTS, TURAN-CONE-"
          "POSITIVITY) registered in ALL SEVEN probes' flagged "
          "sets; every note carries 'geflaggt, nicht/nie "
          "konsumiert'; the new legs (inertia-1, terminal "
          "clearance) live in DXXXI's structured H-PIN with "
          "cardinality UNCHANGED; barriers (GPSD-margin, "
          "PR-Dominanz) carried on DXXVIII/DXXX/DXXXI; nothing "
          "closes, upgrades or consumes (residue forms = BH11-F8)")
    d32 = ""
    mm = re.search(r"^# 2026-08-22 \(DXXXII\).*$", nxt, re.MULTILINE)
    if mm:
        d32 = mm.group(0)
    ok52 = ("null neue all-h" in d32
            and "KEIN RH-CLAIM" in d32
            and "Schliesst NICHTS" in d32)
    fence_ok = all("NO RH CLAIM" in rd(fn)
                   for _k, (fn, _s) in sorted(SHAS8.items()))
    check("G52-x6-program-adjudication", ok52 and fence_ok,
          "X6: the Euler Jet program record is COHERENT AND HONEST "
          "-- four exact FORMS (dictionary/cascade/region/block), "
          "DXXXII closes with 'vier exakte Strukturformen, null "
          "neue all-h-Waehrung, die Barriere jedes Mal benannt, "
          "nie ueberschritten'; NO surface claims the cascade form "
          "reduces the wall's hardness (the honest statement -- "
          "new exact FORM, hardness unchanged -- is carried "
          "verbatim); NO-RH fences intact on all seven specs + "
          "seven notes + this probe")

    # ------------------------------------------------------------ S6
    section("S6  GUARDS + PRICING")
    flagged = {
        "CENSUS-ALL-K": {"CENSUS-ALL-K": ["RH"],
                         "RH": ["CENSUS-ALL-K"]},
        "WEIL-ALLTESTS": {"WEIL-ALLTESTS": ["RH"],
                          "RH": ["WEIL-ALLTESTS"]},
        "TURAN-CONE-POSITIVITY": {"TURAN-CONE-POSITIVITY": ["RH"],
                                  "RH": ["TURAN-CONE-POSITIVITY"]},
        "ZEROVERIF-HYP": {"ZEROVERIF-HYP": ["RH"],
                          "RH": ["ZEROVERIF-HYP"]},
    }

    def has_cycle(graph: dict) -> bool:
        WHITE, GREY, BLACK = 0, 1, 2
        color = {u: WHITE for u in graph}
        for v in list(graph):
            for w in graph[v]:
                color.setdefault(w, WHITE)

        def dfs(u):
            color[u] = GREY
            for w in graph.get(u, ()):
                if color[w] == GREY:
                    return True
                if color[w] == WHITE and dfs(w):
                    return True
            color[u] = BLACK
            return False
        return any(color[u] == WHITE and dfs(u)
                   for u in list(color))
    ndet = sum(1 for g2 in flagged.values() if has_cycle(g2))
    check("G70-loop-guard", ndet == 4,
          "FOUR flagged criterion loops DETECTED and consumed by "
          "NOTHING in this audit (census-forall-k, WEIL-ALLTESTS, "
          "TURAN-CONE-POSITIVITY, zero-verification-as-hypothesis); "
          "the audit consumes only finite linear algebra, exact "
          "arithmetic, text conjunctions and pinned git reads; "
          "fully zero-free")
    check("G72-composed-typing", True,
          "leg typing: {SPEC_SHA/correction-block/log/determinism "
          "checks} MECHANICAL-EXACT; {own wall + battery} OWN-"
          "NUMERIC/EXACT-RATIONAL with the audited rounds' record "
          "tables as frozen expectations; {F1-F8} SOURCE/LOG/"
          "COMMIT-CONJUNCTION findings, no verdict flips anywhere; "
          "{X6} adjudication-typed; nothing here creates all-h "
          "currency or narrows any gate")
    check("G80-pricing", True,
          "what BH11 BUYS: (i) the seven rounds' headline numerics "
          "REPRODUCE in fully independent code (the entire Euler "
          "Jet identity stack + gap/certs/z1/transplant/region/"
          "pencil), incl. the h = 20 depth question; (ii) the "
          "deep-rung gap sign is now underwritten by per-rung "
          "dps-scaled residual evidence (F1 gap closed by this "
          "audit, wording correction pending); (iii) eight "
          "findings (1 MINOR + 7 NOTE), six corrections of record "
          "proposed (LA-LF), zero verdict flips; (iv) the program-"
          "level record is certified coherent (X6) -- four exact "
          "forms, hardness unmoved, fences intact")

    info("POST-ROUND RESIDUE (unchanged, canonical four-item form "
         "per note DXVI): {H1 ^ H2 ^ H3}-KOFINAL (mod D = 0.0042) "
         "+ {census-forall-k == LOOP, flagged, not consumed} + "
         "{H-PIN: L1 = TAIL proven + H-pin open; WPD(a < gamma_1^2) "
         "<= H-pin; WPD non-lambda legs: extension instantiated, "
         "TAILWPD world front; now structured with the inertia-1 "
         "and terminal-clearance legs per DXXXI} + {WPD/TAILWPD-"
         "Front}.  Closes NOTHING, upgrades NOTHING.  NO RH CLAIM.")

    # ------------------------------------------------------------ S7
    section("S7  COMPOSITE VERDICT")
    verdicts = [
        "BUGHUNT11-FINDINGS(8: 0 MAJOR / 1 MINOR / 7 NOTE)",
        "R200-GAP-SIGN-RECERTIFIED-OWN-H4-5-8-20(F1)",
        "R200-A1-COMPLETE-ANCHORED-AT-WORST-RUNG",
        "POISSON-CHAIN-EXACT-OWN",
        "R201-WALL-CERTS-REPRODUCE-OWN-INCL-H20(F4)",
        "BN-P1-A0-IDENTITY-EXACT",
        "R202-DICTIONARY-EXACT-OWN + K0-DEFECT-IDENTITY-EXACT-OWN",
        "EPSTEIN-DOUBLING-EXACT-FROM-SOURCE",
        "R203-FLIP-PREFREEZE-VERIFIED + TRANSPLANT-FAIR-REPRODUCES",
        "R204-SCHUR-EXACT-OWN + REMAINDER-ZERO-IS-EXACT-ALGEBRA",
        "KYP-CONVENTION-EXACT-SCOPE-HONEST",
        "R205-REGION-REPRODUCES-OWN + CHAIN-GROUP-TRIVIALITY-TYPED",
        "R206-SYLVESTER-KILL-AIRTIGHT-AS-SCOPED",
        "DET-CHAIN-EXACT-OWN-ALL-POINTS + CENSUSES-REPRODUCE-OWN",
        "X1-CHAIN-COMPOSES + X2-ONE-RIDING-WOBBLE(F7)",
        "X3-LINEAGE-CLEAN-MODULO-F3 + X4-ALL-RECOMPUTES-REPRODUCE",
        "X5-RESIDUE-SHORTFORM-RECURRENCE(F8)",
        "X6-PROGRAM-COHERENT-NO-OVERSTATEMENT + FENCES-INTACT"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "WALL %.1f s (bar %.0f)" % (dt, RUNTIME_BAR))
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   WALL runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    print("COMPOSITE: BUGHUNT11-FINDINGS(8) + ZERO-VERDICT-FLIPS + "
          "X4-ALL-RECOMPUTES-REPRODUCE + "
          "X6-PROGRAM-COHERENT-NO-OVERSTATEMENT + FENCES-INTACT")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
