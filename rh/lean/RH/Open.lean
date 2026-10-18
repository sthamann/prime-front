/-
RH/Open.lean -- the ladder bookkeeping of the two former open edges
(r273 RETYPE: the open statements themselves moved to RH/Window.lean).

Provenance: the post-r259 endgame state, ledger rows
  * PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01  [O]  (edge A, fiber)
  * PRIME.PORT.FULLSOURCE.PREFIX_RESUMMATION.01   [O]  (edge B, base)
registered by verification/v959_coupledtau_terminal_dictionary.py; campaign
state r260-r267 (probes terminal_crossratio_probe.py, terminal_triangle_
probe.py, cancellation_adjudication_probe.py, quenched_opening_probe.py,
s_monotonicity_probe.py, border_resolvent_identity_probe.py,
ranktrace_adjudication_probe.py; charter SHA 7b9e751d, r264).

r273 RETYPE (reviewer repair).  This file formerly stated the two edges
as universally quantified `sorry` theorems over the bare `WindowLadder`
(`terminal_crossratio_cofinal`) and over an arbitrary source predicate
(`prefix_resummation_positivity`).  Both statements are REFUTABLE in
that form -- the machine-checked counterexamples are permanent guards in
RH/Counterexamples.lean (`terminal_crossratio_not_universal`,
`prefix_resummation_not_universal`): the ladder fields carry no coupling
between `F_k` and `h_k`, and an arbitrary predicate carries no
positivity.  The truth-capable forms now live in RH/Window.lean and
(since the r305 reconstruction) RH/Closure.lean:
  * master theorem `augmented_prefix_positive` (conditioned on the
    honest opaque predicate `MainWindow`; since r305 PROVED in
    RH/Closure.lean from the two true holes `lstar_subordination` +
    `terminal_positive_main` via `lstar_terminal_implies_master`),
  * former edge A  => corollary `terminal_crossratio_main` (PROVED from
    the master theorem, RH/Closure.lean),
  * former edge B  => corollary `prefix_chain_positive_main` (PROVED
    from the master theorem, RH/Closure.lean).
This file keeps the `WindowLadder` bookkeeping structure (it correctly
records the measured structural facts and feeds the counterexample
guards) and the campaign kill lists.  It states no open theorem anymore.

r556: a parallel conditional Gabor reduction lives in
RH/GaborSeparation.lean.  The historical wrapper
`gabor_inputs_to_mathlib_rh` (`GaborExplicitFormula` +
`GaborSeparationInequality` ⇒ mathlib `RiemannHypothesis`)
is VACUOUS (r600): it consumed positivity of
`gaborSpectralFormula`, which is not the Weil functional.
Live wrappers: `gabor_zeroSide_inputs_to_mathlib_rh` and
companions.  r605A `GaborZeroSideForAllZeros` = prescribed
`scalingGaborTest(a=σ²/64, ω=γ−πa/σ)` → FORALL_ZERO_OVERSPECIFIED;
`gabor_zeroSide_pure_criterion_iff_rh` takes `hsep`.
r605B+C `GaborExposedOrbit.lean` sorry-free; live endpoint
`gabor_zeroSide_pure_criterion_iff_rh_unconditional` :
`(∀ a ω ha, 0 ≤ gaborZeroSide (pureGaborTest a ω ha)) ↔ RiemannHypothesis`,
axioms propext/choice/Quot.sound.
RH ⇔ nonnegativity of the pure Gabor zero-side on the two-parameter family (a, ω). r634L: `gabor_explicitFormula_pure` is UNCONDITIONAL (both remainders `gaborContourLimitRemainder_holds` and `gabor_vertical_arithmetic_remainder` are theorems); sharpest live statement `gabor_primeSide_rational_criterion_iff_rh` : (∀ (a ω : ℚ) (ha : 0 < a), 0 ≤ gaborPoleSide − gaborPrimeComb + gaborArchSide of pureGaborTest a ω) ↔ RiemannHypothesis, axioms {propext, Classical.choice, Quot.sound}. Remaining EF brick: `GaborHatQuarticExplicitRemainder` (non-pure quartics only). Census stays 7. Not an RH proof: the Weil test space is reduced to a two-parameter pure Gabor family; positivity of gaborZeroSide itself remains open.
r605C-AUDIT STATEMENT_SOUND. Census 7 (r612: asserting
`gabor_separationForAllZeros` retired; Prop retained unasserted).
r612 `GaborCountableCriterion.lean` rung (b):
`gabor_zeroSide_rational_criterion_iff_rh` (takes `hcont`).
r612C: `gaborZeroSideContinuous_holds` proves
`GaborZeroSideContinuous`; the rational iff
`gabor_zeroSide_rational_criterion_iff_rh_unconditional`
is unconditional. Named-open list shrinks by one;
census stays 7; no new `sorry`.
r638L claim-boundary repair: the overstrong
`arch_gauss_mellin_digamma_identity` and gauge-mismatched
`standard_explicit_formula_identification` asserting theorems are
retired to unasserted Props.  Historical arch extraction APIs take
the former explicitly; the honest-contour identification stays
proved.  Project census 7 -> 5.  This is not an RH closure.
r607 experiments-only KILLED(RECOORDINATIZATION).
r610 rung (b): one named hypothesis `GaborLowHeightZeroFree 4`
(classically true, first zero at 14.1347, not in Mathlib);
`gaborSpectralFormula_refuted_of_lowHeight`.
This file still states no Gabor theorem; the
r487--r538 compact-Weil mincut comments below are status text only.
r541 `SEPARATION_GO_GABOR` is a numeric precheck against one synthetic
FE quadruple, not a discharged separation sorry.  r553 `WITNESS_LOSES`
is historical leftover-scale; r559 settled leftover as a non-faithful
Weil proxy, r560 sealed `HONEST_WITNESS_WINS`, r566/r567 canonicalised
the dominance rule (`CANONICAL_DOMINANCE_HOLDS` on 119 cells).  The
`∀Z` proof stays open.
r581: the Gabor EF remainder
`gabor_vertical_arithmetic_remainder` is a theorem
(no asserting sorry).  r582/r583: log-compatible
`GaborDominanceBoundLog2` is a theorem (finite/conditional
proxy).  r584–r588: tsum≤Closed attachment
`gaborLogThreeLobeMajorant_le_closed` is a theorem;
unrestricted On/Off-split `gaborZeroSideEqOffPlusOn_holds`
is a theorem; weighted Bridge-6 identification
`gaborWeightedQuadrupoleLimitEqOffLineMass_holds` is a
theorem (honest FD, weight 4; real-axis remainder
proved zero via ζ≠0 on (0,1)).  Unweighted
identification only `_of_simple`.  r589: every nonempty
weighted FD window is a BoundLog2 input
(`gaborWeightedTruncationNegLog_holds` theorem;
singleton card=1 supplies gammaDistinct+hostIsolated).
r589 L2: singleton Bridge A is RH-core, not a
translation lemma (`BRIDGE_A_IS_RH_CORE`); Bridge B has
no Isolation→Scaling monotonicity transfer.  r590:
existential arithmetic endpoint
`GaborArithmeticSeparatesOffCriticalZeros` plus a
parallel Mathlib chain without `scalingGaborTest`
(sorry-free logic; unasserted separator).  r591:
`GaborFixedPacketCofinalNegAt` is numerically tenable
only with an extremality gap (strict σ′≤σ−0.02 holds
9/9; tie / free σ′ break).  r592: window-adaptive
packets vs outer tail are CONDITIONAL (IEEE ω-floor
at extreme near-tie; host-σ-max retune per height/T).
r593/r594: outer-tail theorem (strip width beats
window distance; `GaborOuterTailTsumLeExp` and
`GaborOuterTailSmallerThanLocalMargin` are theorems).
r595: three-term window+tail glue and per-T
checkpoint are theorems; named gap
`GaborWindowAdaptiveUniformDelta` (T-uniform δ
missing because of lex host-retune — r592 condition,
not missing algebra).  r596–r598: L2 verdict
`ANKER_TEILWEISE`; log-glue theorem; witness ⇒
zeroSide < 0 at the own packet; Cover is the
remaining geometric rest.
`GaborSpectralToArithmetic` is a proved pole-sign
lemma (`GaborSpectralToArithmetic_holds`, ĥ(1) ≥ 0),
NOT RH-core.  RH-core is hpos* := ∀ F admissible,
0 ≤ `gaborZeroSide` F, equivalently the unasserted
Prop `GaborSeparationForAllZeros` (asserting theorem
retired r612).
`GaborAnchoredWitnessExists` is
NOT asserted (ordinate clusters / multi-point
window open).  L2 STOP: no UniformDelta /
separator / existence claims.  Remaining named
rest: `GaborAnchoredCoverAt` (ordinate isolation
of genuine zeros), `GaborAnchoredWitnessExists`,
`GaborWindowAdaptiveUniformDelta`,
`GaborTruncationUniformNeg` (does NOT follow from
BoundLog2 — packet retunes),
`GaborWeightedTruncationGammaDistinct`,
`GaborFixedPacketCofinalNegAt` (extremality gap),
and the unasserted Prop `GaborSeparationForAllZeros`
(asserting theorem retired r612).
r599/r600 vacuity audit (2026-09-01/02):
`gaborSpectralFormula` subtracts the pole ĥ(1);
for F₀ = `pureGaborTest 1 0` the zero-side sum is
≈ 3·10⁻⁴³ while Re ĥ(F₀,1) = π·e^{1/8} ≈ 3.5599,
so `gaborSpectralFormula F₀` ≈ −3.56 unconditionally.
Old hpos on `gaborSpectralFormula` is FALSE; live
object is `gaborZeroSide`.  Old Mathlib endpoints
marked VACUOUS (r600); live endpoints in the
r599/r600 census below.  r605A `GaborZeroSideForAllZeros` = prescribed
`scalingGaborTest(a=σ²/64, ω=γ−πa/σ)` → FORALL_ZERO_OVERSPECIFIED;
`gabor_zeroSide_pure_criterion_iff_rh` takes `hsep`.
r605B+C `GaborExposedOrbit.lean` sorry-free; live endpoint
`gabor_zeroSide_pure_criterion_iff_rh_unconditional` :
`(∀ a ω ha, 0 ≤ gaborZeroSide (pureGaborTest a ω ha)) ↔ RiemannHypothesis`,
axioms propext/choice/Quot.sound.
RH ⇔ nonnegativity of the pure Gabor zero-side on the two-parameter family (a, ω). r634L: `gabor_explicitFormula_pure` is UNCONDITIONAL (both remainders `gaborContourLimitRemainder_holds` and `gabor_vertical_arithmetic_remainder` are theorems); sharpest live statement `gabor_primeSide_rational_criterion_iff_rh` : (∀ (a ω : ℚ) (ha : 0 < a), 0 ≤ gaborPoleSide − gaborPrimeComb + gaborArchSide of pureGaborTest a ω) ↔ RiemannHypothesis, axioms {propext, Classical.choice, Quot.sound}. Remaining EF brick: `GaborHatQuarticExplicitRemainder` (non-pure quartics only). Census stays 7. Not an RH proof: the Weil test space is reduced to a two-parameter pure Gabor family; positivity of gaborZeroSide itself remains open.
r605C-AUDIT STATEMENT_SOUND. Census 7 (r612: asserting
`gabor_separationForAllZeros` retired; Prop retained unasserted).
r612 `GaborCountableCriterion.lean` rung (b):
`gabor_zeroSide_rational_criterion_iff_rh` (takes `hcont`).
r612C: `gaborZeroSideContinuous_holds` proves
`GaborZeroSideContinuous`; the rational iff
`gabor_zeroSide_rational_criterion_iff_rh_unconditional`
is unconditional. Named-open list shrinks by one;
census stays 7; no new `sorry`.
r607 experiments-only KILLED(RECOORDINATIZATION).
r610 rung (b): one named hypothesis `GaborLowHeightZeroFree 4`
(classically true, first zero at 14.1347, not in Mathlib);
`gaborSpectralFormula_refuted_of_lowHeight`.
Named open (no claim): on-line positivity for general even
quartics (beyond ⟨1,0,0⟩) so the iff holds without `hline`.
Tracked census stays 7.
NO RH CLAIM.

KILL LIST (measured no-gos any future proof of edge A must avoid):
  - mass majorants (sup / Cauchy-Schwarz / triangle on masses): 0/42
    coverage, median x490 excess, break locus 0.97N            (r258)
  - bordered spectral bound f^T (I-Q)^{-1} f < 1: measured FALSE,
    g(1) = 6.06..15.41 on 42/42                                 (r257/r265)
  - naive s-coordinate: exact restatement of the endpoint       (r265)
  - IIKS s-family: definite dynamics, WRONG endpoint criterion
    (DEFINITENESS_WALL_EQUIVALENT)                              (r265)
  - eventual triangle (exceptions vanish for large N): refuted --
    the deepest rung kz52 (N = 878) is itself an exception      (r263)
  - any root-scale bound on the border drive |t_{N-2}|: fires the
    PAIRCORR detector (demand 0.66..2.31 dec)                   (r262/r263)

KILL LIST (edge B):
  - saddle dominance / level crossing: branches cross 5-16 degrees
    too early; MAIN crosses 45x without a flip                  (r259)
  - k-swap truncation / one-swap statistics: gap distributions
    fully overlap between MAIN and controls                     (r259)
  - subtraction-free positivity (LGV): no-go at depth k = 1     (r261)
  - global block involution: 4 unpaired negative configurations
    at n = 2 already                                            (r261)
  - transfer cone: best certificate IS the terminal budget
    positivity -- wall-equivalent, no new mechanism             (r261)

Claim boundary: research documentation.  NOT evidence for or against the
Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Basic
import RH.Recursion

namespace RH

/-- An abstract cofinal window ladder: for every rung `i` a chain datum
`data i` with terminal degree `N i`, a budget in the r243 form
`B = S_{N-1} + m` with one fixed positive floor scalar `m` (the corpus
imports `m = 5/7`, typed FLOOR_IMPORTED -- its source-pure derivation is
part of edge A), and terminal degrees growing cofinally. -/
structure WindowLadder (K : Type*) [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] where
  data : ℕ → ChainData K
  N : ℕ → ℕ
  /-- the floor scalar (`5/7` in the corpus, FLOOR_IMPORTED per r258). -/
  m : K
  m_pos : 0 < m
  /-- terminal degrees are positive... -/
  N_pos : ∀ i, 0 < N i
  /-- ...and cofinal in the ladder. -/
  cofinal : ∀ n : ℕ, ∃ i, n ≤ N i
  /-- the r243 budget form `B = S_{N-1} + m` on every rung. -/
  budget_form : ∀ i, (data i).B = (data i).S (N i - 1) + m
  /-- the wall through the free window: the whole h-prefix is positive
  (the MAIN measurement; for the ladder this is itself only known
  finitely -- 42/42 rungs, N = 142..878). -/
  wall : ∀ i, ∀ k < N i, 0 < (data i).h k
  /-- the Chebyshev coefficients never vanish (by construction). -/
  cheb : ∀ i, ∀ k < N i, (data i).c k ≠ 0

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The terminal cross-ratio of rung `i`:
`q_N = rho_{N-1} / m` (r258 TERMINAL_Q_LAW). -/
def WindowLadder.q (L : WindowLadder K) (i : ℕ) : K :=
  (L.data i).rho (L.N i - 1) / L.m

/-!
## Where the two edges went (r273)

**EDGE A (fiber): the terminal cross-ratio inequality.**
Ledger: PRIME.PORT.COUPLEDTAU.TERMINAL_CROSSRATIO.01 [O].
Formerly stated here as `terminal_crossratio_cofinal : ∀ i, L.q i < 1`
over the bare ladder -- REFUTED as a universal by
`Counterexamples.terminal_crossratio_not_universal` (the model
`h = c = 1, F = 2, m = 1` satisfies every field and has `q_N = 4`).
The truth-capable form is `terminal_crossratio_main` in RH/Window.lean,
PROVED from the master theorem `augmented_prefix_positive`.
Measured support unchanged: 42/42 rungs, min margin 0.0139, trend FLAT
(r258); two-branch split r263: 35/42 rungs + both mains close by the
triangle certificate alone (`two_branch_cheap_strict`), the 7-rung
exception branch is the S6 requirement `|Z^RHP| + |E| < sqrt(m)`.

**EDGE B (base/orientation): globally oriented prefix resummation.**
Ledger: PRIME.PORT.FULLSOURCE.PREFIX_RESUMMATION.01 [O].
Formerly stated here as `prefix_resummation_positivity` over an
arbitrary source predicate -- REFUTED as a universal by
`Counterexamples.prefix_resummation_not_universal` (`MainSource := True`
and `h_0 = -1` give `tau_1 = -1`).  The truth-capable form is
`prefix_chain_positive_main` in RH/Window.lean (the wall derived from
the master positivity, not assumed); the missing DEFINITION of the main
source is exactly the opaque predicate `MainWindow` (r261: the object IS
the coherent sum; cancellation is ~5.7 decades deep at n = 6 already).

## r397 census (exact selected domain)

The C1 holes `lstar_canonical` / `terminal_q_canonical` are DEGRADED
to the alternative (rational-certificate) route: `CanonicalWindow`
may be empty after exact real transcription, and mesh-tolerance is
uncoupled from the L* margin.  They are kept as typed `sorry`s, not
deleted.  The load-bearing open kernel is the named Prop
`frequently_selected_augDualResolvent_ge_half`
(`RH/FrequentlySelected.lean`, r430):
`∃ᶠ k, (R†(W^ℝ_k) − ½·1).PosSemidef`.  The r397 Prop
`selected_augDualResolvent_gt_half` (`∀ᶠ`, `PosDef`) is the
stronger alternative, kept.  New named Props (not sorrys):
`SelectedMasterImpliesPlainReads`, `ExactArchAgreesWithArchRead`,
`SelectedSemidefImpliesPlainReads`.  Sorry census unchanged at 5.

## r417 census (source Schur sign)

The edge scalar `sch < 0` now has two closed formulae
(Woodbury `sch = den-2 + sᵀ(A₀+Ucd Ucdᵀ)⁻¹s` and the
unnormalized Sylvester chart).  Normalized `τ → 0` is a
census, not a theorem; the rate is `RATE_OPEN` (Uvarov / fold
identities do not force the observed slope).  Cofinal `sch < 0`
on the selected sequence is not proved and is not a new
`sorry` here -- it remains a named open of the selected
mincut `frequently_selected_augDualResolvent_ge_half`.
NO RH CLAIM.

## r418 census (phi_bb sign)

The border-border entry has the closed split
`φ_bb = (den-2) + sᵀ A₀⁻¹ s` and the r407 form
`A₀⁻¹ = 2(C+I)(C-I)⁻¹`.  Uniform `φ_bb < 0` on the
named living census is refuted (6/14 vacuous core
windows overflow).  Pole-dominance on living P1 is
refuted (3/28).  Two named mechanisms; selected
`a_k = 2^k` remains a negative census, not a new
`sorry`.  Mincut unchanged.
NO RH CLAIM.

## r419 census (vacuous overflow)

The r417/r418 tension is resolved as a named
reduction, not a theorem: H3 (vacuous family
empties) is refuted (VAC grows 3/14 → 7/14);
the razor-pole account of overflow is refuted
(s ⊥ C_min-mode); the six live by τ²>φ_bb at
finite N, but vacuous τ_un is the vanishing
one so a cofinal τ-floor fails.  Cofinal VAC
`sch < 0` reduces to `φ_bb < 0` on large-N
VAC (EXT/selected census).  No new `sorry`.
Mincut unchanged.
NO RH CLAIM.

## r420 census (c_J vs Sigma)

`den = 1 + ||b||²/B_w - v_t·s` is exact
(`B_w = S_{N-2}+5/7`).  `den<2` has an O(1) budget
gap, but the balance reserve `-φ_bb` is O(0.03) and
shrinks along `a_k=2^k`.  The naive occupied-max
`Σ`-bound is loose (200–24000×).  Cofinal
`c_J < -Σ` on large-N VAC is a census, not a new
`sorry`.  The whole edge is one `c_J`-vs-self-energy
balance.  Mincut unchanged.
NO RH CLAIM.

## r421 census (reserve limit)

Selected $a_k=2^k$ prefers a floor
`R_∞ ≈ 0.030` for `R = -φ_bb` (AIC vs `k`);
`R ~ c/log k` is killed.  `k=10` border-fails.
The T0–C_min linearisation is the r411
dictionary (ratio 1.0000 on vacuous).
Three saturation scales, not one exponent.
Cofinal `R_∞ > 0` is a census, not a new
`sorry`.  Mincut unchanged.
NO RH CLAIM.

## r422 census (Sigma limit)

`Σ = 2||s||² + 4 sᵀ(C-I)⁻¹s` is the r407
Stieltjes form.  A closed occupancy density
is refuted.  Near-`λ=1` mass stays `O(0.01)`
so `n_eff` growth is not pole-creep.
`den_∞` and `Σ_∞` are not constructed;
`limsup Σ < 2-den_∞` is a census, not a new
`sorry`.  Mincut unchanged.
NO RH CLAIM.

## r423 census (den limit)

`den = 1 + γ - v_t·s` is exact.
`γ < 1` on the named census (not a chain
theorem); `‖b‖²` is not a subsum of `S`.
`den_∞` is not constructed.
`den < 2` with gap `≥ 0.348` is a census,
not a new `sorry`.  Mincut unchanged.
NO RH CLAIM.

## r424 census (gamma chain)

`b_k = ⟨σ, π̂_k^μ⟩` and `‖b‖²` equals the
μ-side Parseval budget (SATZ).
Termwise `w_k = b_k²/ρ_k` is not uniform
(`~43%` of terms `>1`).
`‖b‖² ≤ 0.80 S` and `γ < 1` are a census
(max `γ = 0.724`); `γ < 1` is not a new
`sorry`.  Mincut unchanged.
NO RH CLAIM.

## r425 census (cross-chain gamma)

`‖b‖² ≤ S` is the kernel Loewner
`K_μ ≼ K_{μ-ν}` on `P_<N` (SATZ).
`‖b‖² < B_w` is that SATZ plus `q_N < 1`.
On the 42-rung `q_N < 1` census it composes
to `γ < 1`; cofinal `q_N` is not a new
`sorry`.  Mincut unchanged.
NO RH CLAIM.

## r426 census (edge-balance consolidation)

The r417–r424 identities are sorry-free finite
algebra in `RH/EdgeBalance.lean`: Woodbury-sch
is the r406 discriminant at `J = I`; the chart
trichotomy is the 3×3 Schur of a `{±1}`-signature;
vacuous `sch < 0 ↔ τ² > φ`; `den < 2 ↔ γ < 1 + v_t·s`.
Named Props `BorderIsMuParseval`, `BorderLoewnerLeS`,
`QNLtOne` (r425 remainder: cofinal `q_N < 1`).
Census unchanged at 5.  Mincut unchanged.
NO RH CLAIM.

## r430 census (semidefinite frequently selected)

Two quantifier wins, sorry-free except the existing
arch-channel sorry consumed by the FREQ extraction:
(1) `Rdagger_ge_half_iff_augmented_posSemidef` (A3 Loewner
face); (2) `weil_nonneg_of_frequently_selected` /
`internal_weil_nonneg_of_frequently_selected` (FREQ of `R† ⪰ ½I` plus the
named bridge `SelectedSemidefImpliesPlainReads`).
New mincut `frequently_selected_augDualResolvent_ge_half`;
`selected_augDualResolvent_gt_half` degraded to the
stronger alternative.  Density corollary and mean-value
trick proved.  Census unchanged at 5.
NO RH CLAIM.

## r434 census (quantifier mincut audit)

THE BYPASS HOLDS: `terminal_q_canonical` and
`lstar_canonical` are NOT consumed by the FREQ internal path
(`internal_weil_nonneg_of_frequently_selected` / `_of_A_cap`). They remain
typed `sorry`s as the alternative rational-certificate
route `L† ⟺ L* ∧ Terminal` on all `CanonicalWindow`s
(r397 degradation, now path-audited).  Also OFF PATH:
`pair_terminal_dictionary` (pair-closure corollary only),
`mainWindow_iff_builtFromPrimeSource` (historical Alt-Last
since C1).

MINCUT PATH (what Weil-nonnegativity actually consumes):

  * named mincut `frequently_selected_augDualResolvent_ge_half`
  * named remainder `SelectedACapPsdImpliesPlainReads`
    (`A_cap ⪰ 0` ⇒ plain `fullRead`; Hankel/Weil-read
    identification -- NOT the dual-resolvent cone)
  * sorry `arch_elementwise_stabilization` (classical
    kernel channel, already on the extraction)

PROVED ON THE PATH (r434): the L† ⟺ R† identification
on the real window
(`masterCap_posSemidef_iff_Rdagger_ge_half`,
`selectedWindowConeSemidef_implies_A_cap_posSemidef`);
`SelectedSemidefImpliesPlainReads` is a theorem of the
thinner remainder (`selectedSemidefImpliesPlainReads_of_A_cap`).
It was NOT provable from L† ⟺ R† alone: `fullRead` is the
three-channel Weil pairing, not the quadratic form of
`A_cap`.  Census unchanged at 5 (no sorry closed).
NO RH CLAIM.

## r463 census (Lean fidelity repair)

The selected window now uses the production-faithful object in
`RH/FaithfulFold.lean`: tent lags, `L=2(m+1)-2`, circulant
spectral density, grid fold, and sign split.  k=5/9/10 values
are pinned against Python.  `archRead` is a concrete lag read.
`FrequentlySelectedInternalMincut` visibly includes both the
FREQ cone and the AXIOM-CANDIDATE
`SelectedACapPsdImpliesPlainReads`; the endpoint is named
`internal_weil_nonneg_of_frequently_selected`.

Three previously absent external arrows are explicit `sorry`s in
`RH/ExternalBridges.lean`: dense extension, standard explicit-formula
identification, and the Weil criterion to mathlib
`RiemannHypothesis`. Census 5 -> 8. NO RH CLAIM.

## r464 census (inner bridges)

FINITE PSD HALF CLOSED: `RH/InnerBridges.lean` proves
`selectedACapPsdImpliesPlainReads_of_representation`.
The exact remaining channel seam is the named, unasserted Prop
`SelectedReadQuadraticRepresentation`; it retains the original
unbounded `GridElement.steps` quantifier (the old premise bounded
only `meshExp`).  `FrequentlySelectedInternalMincut` now exposes
this narrower remainder directly.

ARCH LAGS TRANSCRIBED: `productionArchLag` is no longer opaque.
Its near and far Gauss tent integrals are concrete.  The one
Elementwise `sorry` is now the named
`arch_gauss_mellin_digamma_identity`; Mathlib v4.29.1 explicitly
lists Gauss's digamma integral representation as TODO.  Census
unchanged at 8.  NO RH CLAIM.

## r473 census (extraction-joint redesign)

A-verdict ARTEFACT at the r470 k=5 witness: classical
Guinand--Weil `Q(g_f) = +0.0769078530458283` while
`fullRead = -0.0428854252772195`.  The gap is the arch tent
error `0.1197932783230478`; `ĝ ≥ 0` (true autocorrelation).
Proved inner bridge: `selectedACapPsdImpliesPolynomialReads`
(PSD `A_cap` ⇒ degree-`< cap` reads `≥ 0`; moment dictionary
`PrimeWindow.hankel_quadform`).  Proved arch-gap identity
`fullRead_weilForm_gap_eq_arch` (does not consume the digamma
sorry).  Named outer bridge
`SelectedPolynomialApproximatesGrid`.  Redesigned joint
`FrequentlySelectedPolynomialJoint`; fixed-`k` readout
`weilForm_ge_neg_two_archError_of_joint`.  Historical FREQ
endpoint retained.  Census stays 8.  No infinitely-many-`k`
statement.  NO RH CLAIM.

## r475 census (arch identity and rate)

F1(ii) not closed as exact equality: the r464 quantifier forces
`Δ = log a/(m+1) → ∞` at fixed mesh (proved
`productionArchDelta_tendsto_atTop`), and Mathlib v4.29.1 still
lists Gauss's integral as TODO.  Isolated as the named Prop
`GaussDigammaIntegralRepresentation` (not a sorry).
`weilArchSide` is now the concrete u-space pairing.
Selected-path rate `O(Δ_k²)` named
(`SelectedArchErrorQuadraticRate`);
`selectedArchError_tendsto_zero_of_rate` proved (fixed-`f`
convergence, not infinitely-many-`k` positivity).  Numerical
seal: err/Δ² = 3.9893 at k=5 and 3.8466 at k=9 on the r470
witness.  Census stays 8 (the exact-identity sorry is retained
for the historical FREQ consumer).  NO RH CLAIM.

## r487 census (outer bridges, lane start)

The full class is now typed as continuous, even, compactly supported
real autocorrelations with an explicit `L¹` witness.  Dense extension
is split into:

  * sorry `fullWeil_fixedSupport_grid_density`;
  * sorry `fullWeil_channel_continuity`.

The positivity-limit algebra and `grid_dense_extension` wrapper are
PROVED.  The standard explicit-formula normalization remains sorry
`standard_explicit_formula_identification`.

The zeta interface uses mathlib's literal zero predicate
`riemannZeta s = 0`; no `ZetaZero` enumeration exists in this
mathlib tag.  `standard_weil_criterion_to_mathlib_rh_of_separation`
is PROVED.  Its only classical remainder is sorry
`fullWeil_separates_offCritical_zeros`; the Guinand--Weil spectral
formula is named as `GuinandWeilExplicitFormula`.  Mathlib has no
ready Guinand--Weil theorem, but does provide `MellinTransform`,
`MellinInversion`, and `MellinEqDirichlet`.  Census 8 -> 9 because
the old dense-extension sorry was honestly split in two.

LATER (r556/r600): a parallel conditional Gabor route exists in
`RH/GaborSeparation.lean`.  Historical wrapper
`gabor_inputs_to_mathlib_rh` (`GaborExplicitFormula` +
`GaborSeparationInequality` ⇒ mathlib `RiemannHypothesis`)
is VACUOUS (r600): it consumed false hpos on
`gaborSpectralFormula`.  Live wrapper:
`gabor_zeroSide_inputs_to_mathlib_rh`.  r605A `GaborZeroSideForAllZeros` = prescribed
`scalingGaborTest(a=σ²/64, ω=γ−πa/σ)` → FORALL_ZERO_OVERSPECIFIED;
`gabor_zeroSide_pure_criterion_iff_rh` takes `hsep`.
r605B+C `GaborExposedOrbit.lean` sorry-free; live endpoint
`gabor_zeroSide_pure_criterion_iff_rh_unconditional` :
`(∀ a ω ha, 0 ≤ gaborZeroSide (pureGaborTest a ω ha)) ↔ RiemannHypothesis`,
axioms propext/choice/Quot.sound.
RH ⇔ nonnegativity of the pure Gabor zero-side on the two-parameter family (a, ω). r634L: `gabor_explicitFormula_pure` is UNCONDITIONAL (both remainders `gaborContourLimitRemainder_holds` and `gabor_vertical_arithmetic_remainder` are theorems); sharpest live statement `gabor_primeSide_rational_criterion_iff_rh` : (∀ (a ω : ℚ) (ha : 0 < a), 0 ≤ gaborPoleSide − gaborPrimeComb + gaborArchSide of pureGaborTest a ω) ↔ RiemannHypothesis, axioms {propext, Classical.choice, Quot.sound}. Remaining EF brick: `GaborHatQuarticExplicitRemainder` (non-pure quartics only). Census stays 7. Not an RH proof: the Weil test space is reduced to a two-parameter pure Gabor family; positivity of gaborZeroSide itself remains open.
r605C-AUDIT STATEMENT_SOUND. Census 7 (r612: asserting
`gabor_separationForAllZeros` retired; Prop retained unasserted).
r612 `GaborCountableCriterion.lean` rung (b):
`gabor_zeroSide_rational_criterion_iff_rh` (takes `hcont`).
r612C: `gaborZeroSideContinuous_holds` proves
`GaborZeroSideContinuous`; the rational iff
`gabor_zeroSide_rational_criterion_iff_rh_unconditional`
is unconditional. Named-open list shrinks by one;
census stays 7; no new `sorry`.
r607 experiments-only KILLED(RECOORDINATIZATION).
r610 rung (b): one named hypothesis `GaborLowHeightZeroFree 4`
(classically true, first zero at 14.1347, not in Mathlib);
`gaborSpectralFormula_refuted_of_lowHeight`.
r541 `SEPARATION_GO_GABOR`
is a numeric precheck against one synthetic FE quadruple (42/42, γ≤10⁴),
NOT a discharge of `gabor_separationForAllZeros`.  r553
`WITNESS_LOSES` is historical leftover-scale.  r559 settled leftover
as a non-faithful Weil proxy; r560 sealed `HONEST_WITNESS_WINS`
(all=52); r566/r567 canonicalised the dominance rule
(`CANONICAL_DOMINANCE_HOLDS`, 119 cells).  The `∀Z` proof stays
open.  Compact-Weil live mincut above is unchanged.  NO RH CLAIM.

## r489 census (outer bridges 2)

The bridge topology is now uniform convergence on the common fixed
support plus `L¹`; the autocorrelation witness is explicitly compactly
supported in `L²`.  PROVED:

  * global pointwise convergence from the support-uniform topology;
  * common finite-anchor reduction and comb-channel continuity;
  * continuity of the standard polar integral
    `∫ +2 cosh(u/2) g(u) du` (sign corrected in r491).

The r376 native-mesh pole read is not definitionally that integral.
Its finite-element identity is named
`GridPoleIntegralIdentification`.  Together with dyadic `L²` step
density/autocorrelation convergence and r475 u-space arch continuity,
it is one transparent conjunction
`FullWeilFixedSupportCompletion`, carrying the only dense-bridge
`sorry`.  Public density, channel-continuity, and positivity wrappers
are derived from it.  External sorries 4 -> 3; repository census
9 -> 8.  NO RH CLAIM.

## r491 census (outer bridges 3)

HIDDEN GAP FOUND: the r489 completion has three components, not the
two listed in the r491 prompt.  `FullWeilArchContinuity` is still
required, and was previously impossible to derive while
`fullWeilArchSide` was opaque.  It is now the concrete r475 u-space
pairing.

The r376 pole normalization is corrected: `polePotential'' =
-2 cosh(u/2)` and `polePairingZ` has an outer minus, hence the full
integral weight is `+2 cosh(u/2)`.  The one-cell check is
2.042015443302091 on both sides (difference 1.8e-15).

The L2 witness now carries a Lipschitz constant and support in an
interval of length `supportRadius`.  `dyadicSampleGrid` is explicit:
left samples, mesh `2^-m`, and `floor(R*2^m)` cells; its support bound
is PROVED.  Its convergence is isolated as
`FullWeilDyadicSampleConvergence`, which implies the previous
existential density interface.  The pole seam is reduced to the exact
finite-hat theorem `GridPoleHatIntegralIdentity`; its implication to
the sequence-level dictionary is PROVED.

Still open inside the one completion sorry: dyadic sampled
autocorrelation convergence, singular u-space arch continuity, and
the finite-hat pole integral.  Census remains 8 (external 3).
No density-bridge closure and NO RH CLAIM.

## r493a census (floor-free finite cell representation)

PROVED: `GridElement.toFun_eq_sum_linearCellPiece`.  The actual
`GridElement.toFun` is the even piecewise-linear interpolation of the
autocorrelation knots `acf d`, not the underlying step function with
values `x`.  It is now a finite sum over `Finset.range f.steps` of
explicit affine pieces supported on the half-open normalized cells
`[d,d+1)`.  The representation contains no floor; floor arithmetic is
used only in the proof to identify the unique active cell.  Outside
the cell range both sides vanish via `acf_eq_zero`.

This is the exact finite-sum input for r493b: distribute the interval
integral over the sum, split each affine cell, and identify its
`2 cosh(u/2)` integral with the corresponding second difference of
`polePotential`.  No new sorry; repository census remains 8.
NO RH CLAIM.

## r493c1 census (evenness split + dyadic cell decomposition)

PROVED: `GridElement.toFun_eq_affine_on_nonneg_cell`,
`GridElement.intervalIntegral_toFun_mul_two_cosh_eq_two_mul`,
`GridElement.intervalIntegral_toFun_mul_two_cosh_eq_sum_cell`,
`GridElement.intervalIntegral_toFun_mul_two_cosh_eq_two_mul_sum_cell`,
and the weight-normalized wrapper
`gridPoleIntegral_eq_two_mul_sum_cell`.  The even product
`toFun × 2 cosh(·/2)` splits as `∫_{-R}^{R} = 2 ∫_0^R`; the
nonnegative half decomposes as the adjacent-interval sum over the
native cells `[d D0, (d+1) D0]` for `d < steps`, with the tail
beyond `supportBound` vanishing.  Each cell integral is the r493b
affine integrand via the closed-cell identity
`toFun = cellIntercept d + cellSlope d · u`.  Step (iii) — rewrite
`polePairingZ` as the one-sided ACF knot sum and match the evaluated
primitives — is r493c2.  No new sorry; repository census remains 8.
NO RH CLAIM.

## r493c2 census (pole hat integral identity)

PROVED, sorry-free: `gridPoleHatIntegralIdentity` (the Prop
`GridPoleHatIntegralIdentity`).  Wörtlich:
`weilPoleSide f = ∫_{-R}^{R} 2 cosh(u/2) · toFun u du` whenever
`supportBound ≤ R`.  The three algebraic steps close without a
sign mismatch (r491 precedent does not recur: `Π'' = -2 cosh`,
outer minus on `polePairingZ`, weight `+2 cosh`).

  (1) each nonnegative cell evaluates by `integral_congr` plus
      `toFun_eq_affine_on_nonneg_cell` and
      `intervalIntegral_affine_mul_two_cosh_half` to an
      `affineCoshPrimitive` increment (`cellCoshIncrement`);
  (2) `polePairingZ` reindexes by evenness to the one-sided ACF
      knot sum (factor 2, zero-lag unhalved);
  (3) the primitive second difference is `poleΔ`, so the
      telescoped increment sum equals `weilPoleSide`.

Census remains 8: no new sorry; the pole conjunct leaves
`FullWeilFixedSupportCompletion`, which is now
`FullWeilDyadicSampleConvergence ∧ FullWeilArchContinuity`.
`fullWeil_channel_continuity` consumes the proved hat identity
directly.  Remaining density-bridge: dyadic `L²` / ACF transfer
and Dini / u-space arch continuity.  The pole piece of the
density bridge is closed.  NO RH CLAIM.

## r493d census (dyadic L² / ACF transfer)

PROVED, sorry-free: `fullWeil_dyadic_sample_convergence` (the Prop
`FullWeilDyadicSampleConvergence`).  The class question is closed
by the existing witness: `FullWeilTest.autocorrelation` already
requires `MemLp 2`, compact support, `LipschitzWith K`, and
vanishing off an interval of length `supportRadius`.  No
continuous-dense-in-`L²` detour.

Wörtlich the sampled-grid approximation
`FixedSupportGridApproximation (dyadicSampleGrid h a R)`:

  (i) knot error
  `|acf d − F.toFun (d · D)| ≤ 4 (K R)² D`
  by left-Riemann comparison of the Lipschitz product
  `φ(t)=h(t)h(t+d D)` (cell error `O(D)`, extra tail samples
  `O(D)`, integral tail `O(D)`);
  (ii) uniform ACF: Heine on `F.toFun` plus the piecewise-linear
  interpolant of the knots, so
  `|(grid m).toFun u − F.toFun u| → 0` uniformly on `|u|≤R`;
  (iii) `L¹` on `[-R,R]` from the uniform bound times `2R`.

`FullWeilFixedSupportCompletion` shrinks to
`FullWeilArchContinuity` alone.  Density and channel wrappers
consume the proved dyadic theorem and the remaining arch sorry.
Census remains 8 (external 3): the completion `sorry` is now
exactly Dini / u-space arch continuity (R493e).  NO RH CLAIM.

## r493e census (arch / Dini continuity)

PROVED, sorry-free: `fullWeil_arch_continuity` /
`fullWeil_arch_side_tendsto` (the Prop `FullWeilArchContinuity`).
The r475 pairing
`A(g) = C_b·g(0) + ∫₀^b w(u)(e^{−3u/2}g(0) − g(u)) du`
with `w(u) = 2e^{−u/2}/(1−e^{−2u})` is continuous along a
fixed-support approximation that carries a common Lipschitz
majorant (fifth conjunct of `FixedSupportGridApproximation`).

Wörtlich:
  (1) `FullWeilTest.lipschitz_toFun` — ACF of a Lipschitz
      compact witness is Lipschitz (`K² R²`);
      `GridElement.lipschitz_toFun_of_slope_bound` —
      uniform cell-slope bound implies `toFun` Lipschitz;
      `dyadicSampleGrid_uniform_lipschitz` — dyadic ACF
      interpolants share one constant;
  (2) `archIntegrand_dini_bound` — near 0, `w(u)·u ≤ e^{3u/2}`
      and `|e^{−3u/2}g(0) − g(u)| ≤ ((3/2)|g(0)| + K)·u`,
      so the product is dominated by an integrable constant;
  (3) `MeasureTheory.tendsto_integral_filter_of_dominated_convergence`
      on `Ioc 0 R` with that majorant, plus cutoff invariance
      `weilArchSide_eq_cutoff` (`A(g,b) = A(g,R)`).

`fullWeil_fixedSupport_completion` is now the proved arch
theorem.  Density bridge complete: first outer bridge fallen.
Census 8 → 7 (external 3 → 2).  Remaining outer bridges:
`standard_explicit_formula_identification` and
`fullWeil_separates_offCritical_zeros`.  NO RH CLAIM.

## r497 census (outer bridges 5, lane switch)

ORDER: prove bridge [2] (explicit-formula identification) before
bridge [3] (off-critical separation).  Mathlib
`RiemannHypothesis` is the quantified zero statement
`ζ(s)=0 ∧ nontrivial ∧ s≠1 → Re s = 1/2`.  The logical wrapper
`standard_weil_criterion_to_mathlib_rh_of_separation` is already
proved.  [3] is stated as
`∃ F, admissible ∧ standardExplicitFormula F < 0`.
`standardExplicitFormula` is opaque, so a negativity proof
requires the identification [2] (or a spectral-side definition,
which is the same work).  A contour/Mellin argument for one
test family is a special case of Guinand--Weil, not a bypass.

PROVED brick [2a], sorry-free:
`riemannZeta_analyticOrderAt_finite_pos` —
at every non-polar zero, `analyticOrderAt riemannZeta s`
is neither `0` nor `⊤`; `riemannZetaMultiplicity` is a
positive `ℕ`.  Uses `ζ(0) = -1/2`, identity on the
preconnected set `ℂ \ {1}`, and `differentiableAt_riemannZeta`.

Remaining named pieces of [2] (not extra sorries):
  [2b] meromorphic `ζ'/ζ` (simple poles, residue = order),
      ~2--4 rounds;
  [2c] local finiteness of zeros and absolute convergence of
      the spectral pairing, ~4--8 rounds;
  [2d] contour evaluation = three-channel form
      (`standard_explicit_formula_identification`), ~8--16
      rounds.
Bridge [3] after [2]: Gauss-like `FullWeilTest` family and
the off-critical sign, ~4--8 rounds.

Census stays 7 (external 2).  NO RH CLAIM.

## r498 census (outer bridges 6, [2b] first cut)

PROVED brick [2b] lemma (1), sorry-free: at every non-polar
zero, `ζ'/ζ = m/(z-s) + analytic` with
`m = riemannZetaMultiplicity s` (simple pole, residue = order).
Named lemmas:
  `exists_analytic_logDeriv_eq_order_div` (local calculus),
  `logDeriv_riemannZeta_eq_multiplicity_div_add_analytic`,
  `meromorphicAt_logDeriv_riemannZeta`,
  `meromorphicOn_logDeriv_riemannZeta_compl_one`
    (contour carrier on `ℂ \ {1}`; a strip rectangle is a
    subset),
  `meromorphicOrderAt_logDeriv_riemannZeta` (`= -1`),
  `tendsto_mul_logDeriv_riemannZeta` (`(z-s)·ζ'/ζ → m`).
The polar point `s = 1` (intended `ζ'/ζ = -1/(s-1) + analytic`)
is not in this cut; Mathlib supplies only
`riemannZeta_residue_one` as a punctured limit.

Remaining named pieces of [2] (not extra sorries):
  [2c] local finiteness of zeros and absolute convergence of
      the spectral pairing (needs the residue just proved so
      a contour of `ĥ·ζ'/ζ` picks up `∑ m_ρ ĥ(ρ)`),
  [2d] contour evaluation = three-channel form.
Census stays 7 (external 2).  NO RH CLAIM.

## r499 census (outer bridges 7, [2c] first cut)

PROVED brick [2c] lemmas (1)--(2), sorry-free: zeros of
`riemannZeta` on `ℂ \ {1}` are discrete / locally finite;
every compact `K ⊆ ℂ \ {1}` meets them finitely often
(`finite_riemannZeta_zeros_of_isCompact`); the residue at
`s = 1` excludes zeros from a punctured neighbourhood of the
pole, so the same holds on every compact in `ℂ`
(`finite_riemannZeta_zeros_of_isCompact_ne_one`).  A closed
strip rectangle `[σ₁,σ₂]×[-T,T]` therefore contains only
finitely many zeros
(`finite_riemannZeta_zeros_on_closedRect`) -- the [2d]
contour support is a finite residue sum, using the r498
residue lemma.  The polar decomposition of `ζ'/ζ` at `s = 1`
is not in this cut.

Remaining named pieces of [2] (not extra sorries):
  [2c] cut 2: absolute convergence of `∑ m_ρ ĥ(ρ)` for
      admissible tests,
  [2b] remainder: `ζ'/ζ = -1/(s-1) + analytic` at the pole,
  [2d] contour evaluation = three-channel form.
Census stays 7 (external 2).  NO RH CLAIM.

## r500 census (outer bridges 8, [2b] complete)

PROVED brick [2b] remainder, sorry-free: `(s-1)ζ(s)` extends
holomorphically through `s = 1` with value `1`
(`riemannZetaMulSubOne`, `analyticOnNhd_riemannZetaMulSubOne`);
equivalently `ζ(s) = 1/(s-1) + H(s)` with `H` analytic at `1`.
Logarithmic derivative: `ζ'/ζ = -1/(s-1) + analytic` near `1`
(`logDeriv_riemannZeta_eq_neg_one_div_add_analytic`), residue
`-1` (`tendsto_mul_logDeriv_riemannZeta_one`), meromorphic
order `-1` at the pole.  Combined with r498 this types
`MeromorphicOn (logDeriv riemannZeta) univ`
(`meromorphicOn_logDeriv_riemannZeta`): simple poles at
non-polar zeros (residue = multiplicity) and at `s = 1`
(residue `-1`).  [2b] is complete.

[2c] cut 2 interface only (no convergence): the r499 finite
rectangle witness as `riemannZetaZerosOnClosedRect` and the
indexed sum `spectralPartialSum`.

Remaining named pieces of [2] (not extra sorries):
  [2c] cut 2: absolute convergence of `∑ m_ρ ĥ(ρ)` (growth of
      `ĥ` vs zero-count; `T → ∞` of `spectralPartialSum`),
  [2d] contour evaluation = three-channel form (now has the
      full meromorphic integrand `ĥ · ζ'/ζ` on `ℂ`, including
      the pole residue `-ĥ(1)`).
Census stays 7 (external 2).  NO RH CLAIM.

## r501 census (outer bridges 9, [2c] hat exp-type)

SCOPING for `∑ m_ρ ĥ(ρ)` (honest, no claims):
  Mathlib v4.29.1 has NO `N(T)` / zero-count on
  `RiemannZeta` (only trivial zeros, FE, residue).
  `Analysis.Complex.Hadamard` is three-lines, NOT
  Hadamard factorization of finite-order entire
  functions -- no `ξ` product, no `∑ 1/|ρ|²` off
  the shelf.  `Analysis.Complex.JensenFormula`
  (`MeromorphicOn.circleAverage_log_norm`) IS
  present, with a logarithmic counting function.
  Fourier convolution (`fourier_convolution`) is
  Schwartz-only, so Bochner `ĝ = |ĥ|²` is not in
  the `FullWeilTest` class without approximation.

  Minimal bound that suffices: `1/t²` decay of
  `ĥ` on the strip plus `N(T+1)-N(T) = O(T^θ)`
  for `θ < 1`, or even classical `N(T) ≪ T log T`.
  A lone `1/t` decay does NOT beat `T log T`.
  `∑ 1/|ρ|² < ∞` is the cheapest zero-side target.

  Cheapest formal path to `∑ 1/|ρ|²`: Jensen on
  the entire filling `(s-1)ζ(s)` (r500), once a
  polynomial `|ζ|` bound on large circles is
  available.  That bound is NOT in Mathlib;
  the standard route is Dirichlet series on
  `Re = 2` + functional equation + three-lines
  (convexity).  Hadamard factorization of `ξ`
  would also give `∑ 1/|ρ|²` from order 1, but
  is a larger missing library (10+ rounds).

  Round estimate (not extra sorries):
    r503  Δ² of the ACF (this plan; Fourier
          strip translation may slip a cut);
    r504  Weierstrass → `1/t²` strip of `hat`;
    r505--r507  `|ζ|` convexity via three-lines
          (~3 rounds);
    r508  N=1 EM + `|ζ|` poly on `Re s>1`;
    r509  identity fill + `|ζ|` poly on `Re>δ`;
    r510  filling bound + centre + Jensen API;
    r511  disk card via `Real.circleAverage`;
    r512  dyadic `N(X) ≲ X log X` + FE-fold;
    r513  `∑ 1/|ρ|² < ∞` via dyadic blocks;
    then [2d] contour.
  Total remaining [2c] analysis: ~6--8 rounds,
  matching the original 4--8 band if the strip
  bound lands on the next cut.

PROVED this cut, sorry-free: spectral kernel
`FullWeilTest.hat s = ∫ g(t) e^{s t} dt` and the
compact-support envelope
`‖hat F s‖ ≤ C(F) exp((R+1)|Re s|)`
(`norm_hat_le_exp`).  Available regularity:
`g` is Lipschitz (already); `h` is Lipschitz
with compact support, so classically `Δ² g = O(δ²)`.
Bochner positivity on `iℝ` is not formal here.

Remaining named pieces of [2] (not extra sorries):
  [2c] `1/t²` strip bound, then zero-count /
      `∑ 1/|ρ|²`, then abs. conv. of
      `spectralPartialSum`;
  [2d] contour evaluation = three-channel form.
Census stays 7 (external 2).  NO RH CLAIM.

## r503 census (outer bridges 10, [2c] Δ² of ACF)

PROVED this cut, sorry-free: the second difference
of an autocorrelation with Lipschitz-compact
witness is classically O(δ²),
`|Δ²_δ g(u)| ≤ K² δ² (R + 2|δ|)`
(`autocorrelation_second_diff_eq`,
`autocorrelation_second_diff_le`,
`FullWeilTest.abs_second_diff_le`),
and the Laplace translation
`∫ g(t-δ) e^{st} dt = e^{sδ} hat`
(`FullWeilTest.hat_comp_sub`).
The consumer strip bound
`FullWeilTest.norm_hat_le_inv_sq` is NOT landed:
the Weierstrass identity
`hat · (1 - e^{sδ})² = ∫ Δ²g e^{st}`
(δ = π/|τ|) stuck on ℂ-coercion of
`s * (2δ)` vs `2*(s*δ)` and the
`exp (I * ±π) = -1` wiring.

ĥ-side of [2c] is therefore still missing
the `1/t²` decay (r501 exp-type is in).
Remaining named pieces of [2] (not extra sorries):
  [2c] Weierstrass → `‖hat s‖ ≤ C/(1+|Im s|²)`
      on `0 ≤ Re s ≤ 1`;
  [2c] `|ζ|` convexity → Jensen → `N(T)` →
      `∑ 1/|ρ|²`;
  [2d] contour evaluation = three-channel form.
Census stays 7 (external 2).  NO RH CLAIM.

## r504 census (outer bridges 11, strip bound)

Target `FullWeilTest.norm_hat_le_inv_sq` NOT landed.
Two-step translation IS in, sorry-free:
`∫ g(t-δ-δ) e^{st} = e^{sδ} e^{sδ} hat`
(`hat_comp_sub_twice`) -- the `2δ` coercion
is gone.  Third clamp: Bochner
`integral_add`/`integral_sub` will not match
`∫ (g0 - 2•gδ + g2)` (Pi.add vs pointwise),
and `e^{sδ} = -e^{σδ}` still fights
`ofReal_div` / `↑π * I` vs `I * ↑π`.
Consumer assembly `nlinarith` on the strip
constants timed out behind those.

ĥ-side of [2c] still missing `1/t²`.
Remaining named pieces of [2] (not extra sorries):
  [2c] Weierstrass identity +
      `‖hat s‖ ≤ C/(1+|Im s|²)` on the strip;
  [2c] `|ζ|` convexity → Jensen → `N(T)` →
      `∑ 1/|ρ|²`;
  [2d] contour evaluation = three-channel form.
Census stays 7 (external 2).  NO RH CLAIM.

## r505 census (outer bridges 12, strip parked + zeta)

STRIP PARKED as `FullWeilTest.NormHatLeInvSq` (named
Prop, no sorry).  Weierstrass identity
`hat*(1-e^{sδ})² = ∫ Δ²g e^{st}`
(`hat_mul_weierstrass`) and
`e^{sδ} = -e^{σδ}` / `|1-e^{sδ}| ≥ 2`
(`exp_mul_pi_div_abs_im`, `norm_one_sub_exp_pi`)
are sorry-free.  Remaining strip tactic: Δ²-support
width / `ofReal` second-diff / set-integral assembly.

ζ-side cut 1: termwise Dirichlet comparison
`|(n+1)^{-s}| ≤ |(n+1)^{-2}|` on Re s ≥ 2
(`norm_one_div_nat_succ_cpow_le_two`),
`‖ζ(2)‖ = π²/6` (`norm_riemannZeta_two`),
and `1/ζ = L(μ)` (`inv_riemannZeta_eq_LSeries_moebius`).
The tsum-consumer `|ζ| ≤ |ζ(2)|` and the Möbius
`|1/ζ| ≤ |ζ(2)|` are named Props
(`NormRiemannZetaLeZetaTwo`,
`NormInvRiemannZetaLeZetaTwo`).  Strip polynomial
bound parked: no vertical `Complex.Gamma`
(`RiemannZetaStripPolyBound`).

ĥ-side of [2c] still missing the `1/t²` consumer.
Remaining named pieces of [2] (not extra sorries):
  [2c] Δ²-assembly → `‖hat s‖ ≤ C/(1+|Im s|²)`;
  [2c] tsum-consumer `|ζ| ≤ |ζ(2)|`, then
      `|ζ|` convexity → Jensen → `N(T)`;
  [2d] contour evaluation = three-channel form.
Census stays 7 (external 2).  NO RH CLAIM.

## r506 census (outer bridges 13, strip + zeta majorants)

ĥ-Seite von [2c] KOMPLETT, sorry-free:
`‖hat s‖ ≤ C/(1+τ²)` on `0 ≤ Re s ≤ 1`
(`FullWeilTest.norm_hat_le_inv_sq`).  Assembly:
wide Δ²-support (three copies), ofReal of the
real second difference, set-integral envelope,
Weierstrass division by `|1-e^{sδ}| ≥ 2`.

ζ-side cut 1 PROVED: `|ζ(s)| ≤ |ζ(2)|` and
`|1/ζ(s)| ≤ |ζ(2)|` on `Re s ≥ 2`
(`normRiemannZetaLeZetaTwo`,
`normInvRiemannZetaLeZetaTwo`).  Remaining
[2c] analysis: three-lines convexity of `|ζ|`
on the strip (needs vertical `Complex.Gamma`,
`RiemannZetaStripPolyBound` still parked),
then Jensen → `N(T)` → `∑ 1/|ρ|²`.
  [2d] contour evaluation = three-channel form.
Census stays 7 (external 2).  NO RH CLAIM.

## r507 census (outer bridges 14, Γ-free counting path)

(a) FE-pairing KOMPLETT: `ζ(s)=0` and `0<Re s<1`
imply `ζ(1-s)=0` (`riemannZeta_one_sub_eq_zero_of`,
iff via `riemannZeta_zero_iff_one_sub`).  Uses
Mathlib `riemannZeta_one_sub` (cos form); no
Γ-growth and no `Gamma_ne_zero`.

(b) Mathlib has no complex N=1 Euler–Maclaurin
(`ZetaAsymp` is only `s→1` / real `term`).
Landed: FTC cell `∫_n^{n+1} x^{-s-1}`, discrete
telescoping, `{x}`-cell series `zetaFractIntegral`,
and cell majorant `|cell| ≤ ∫ x^{-σ-1}`.  The
assembled `ζ(s)=1/(s-1)+1-s∫_1^∞{x}x^{-s-1}`
on `Re s>1` (then identity theorem to `Re s>0`)
is r508.

(c) Strip `|ζ| ≤ C(δ)(1+|s|)` on `Re s≥δ>0` not
this round.  Jensen / `N(T)` / `∑ 1/|ρ|²` = r508–r509.
`RiemannZetaStripPolyBound` remains parked.
Census stays 7 (external 2).  NO RH CLAIM.

## r508 census (outer bridges 15, N=1 Euler–Maclaurin)

(1) Finite-N identity KOMPLETT (`finite_N_euler_maclaurin`):
`∑_{k=1}^N k^{-s} = s/(s-1)·(1-(N+1)^{1-s})
- s·∑_{n<N} cell(n) + N(N+1)^{-s}` for `s≠0,1`.

(2) N→∞ on `Re s>1` KOMPLETT:
`ζ(s) = s/(s-1) - s·zetaFractIntegral(s)`
(`riemannZeta_eq_s_div_sub_s_mul_fractIntegral`).

(3) KLEMME: holomorphy of `zetaFractIntegral` on
`{Re s>0}` + identity-theorem fill to `{Re s>0, s≠1}`.
Cell majorant and summability hold on `Re s>0`
(`norm_zetaFractCell_le_rpow`, `summable_zetaFractCell`).
Mathlib `differentiable_tsum'` wants a global
derivative majorant independent of `s`.  Prop
`ZetaFractIntegralHolomorphicOnRePos` is parked
(no new sorry).  Jensen radius 1.75 reaches
`Re=0.25`, so this fill is r509.

(4) Γ-free poly bound on the valid region of (2):
`|ζ(s)| ≤ (2+|ζ(2)|)·(1+|s|)` on `{Re s>1} ∩ {|s-1|≥1/2}`
(`norm_riemannZeta_le_of_re_gt_one`).
`RiemannZetaStripPolyBound` on `{Re s≥δ>0}` remains
parked until (3).  Jensen / `N(T)` = r509.
Census stays 7 (external 2).  NO RH CLAIM.

## r509 census (outer bridges 16, identity fill)

(1) Id-Fill KOMPLETT, sorry-free:
`ζ(s) = s/(s-1) − s·zetaFractIntegral(s)` on
`{Re s>0, s≠1}`
(`riemannZeta_eq_s_div_sub_s_mul_fractIntegral_of_re_pos`).
Path: each cell is entire (parametric FTC);
Weierstrass M-test
(`differentiableOn_tsum_of_summable_norm`) gives
holomorphy of `I` on every `{Re>δ}`; identity
theorem on three convex charts that avoid `s=1`
(upper/lower half of `{Re>δ}`, then the strip
`{δ<Re<1}` via a ball in the upper half).

(2) Γ-free poly bound KOMPLETT on the filled
region: `|ζ(s)| ≤ C(δ)(1+|s|)` on
`{Re s>δ} ∩ {|s-1|≥1/2}`
(`norm_riemannZeta_le_of_re_gt`), with
`C(δ) = 2 + ∑ (n+1)^{-δ-1}`.

(3) Jensen-Einstieg ehrlich geschnitten:
`JensenDiskZeroCountBound` is a named Prop
(no sorry).  Wiring
`MeromorphicOn.circleAverage_log_norm` plus
the poly bound and the r506 centre lower
bound `|ζ(2+iT)| ≥ 1/|ζ(2)|` is r510.
Census stays 7 (external 2).  NO RH CLAIM.

## r510 census (outer bridges 17, Jensen wiring)

(1) Füllungs-Schranke KOMPLETT, sorry-free:
`|(s-1)ζ(s)| ≤ |s| + |s|(|s|+1)∑(n+1)^{-δ-1}` on
`Re s>δ` without `|s-1|≥1/2`
(`norm_riemannZetaMulSubOne_le_of_re_gt`).

(2) Zentrum-Untergrenze KOMPLETT:
`|F(2+iT)| ≥ 1/|ζ(2)|`
(`norm_riemannZetaMulSubOne_center_ge`).

(3) Mathlib-Jensen-Lage: the mean-value form is
`MeromorphicOn.circleAverage_log_norm`; averages
live in `namespace Real` (`Real.circleAverage`).
The zero-free case is
`AnalyticOnNhd.circleAverage_log_norm_of_ne_zero`.
Restriction of meromorphy is `MeromorphicOn.mono_set`.
Disk Finset `riemannZetaZerosInClosedDisk` and
`F=0 ↔ ζ=0 ∧ z≠1` are in.  Weighted-sum vs card
assembly is r511.  `ZetaZeroCountUpToXBound`
remains a named Prop (no new sorry).
Census stays 7 (external 2).  NO RH CLAIM.

## r511 census (outer bridges 18, Jensen disk card)

(1) Disk-Zählung KOMPLETT, sorry-free:
`zetaZerosInDisk_card_le` —
`(riemannZetaZerosInClosedDisk (2+iT) (3/2)).card
≤ C · (1 + log(2+|T|))` with explicit
`C = (log K + log‖ζ(2)‖ + 2) / log(7/6)` and
`K = 2 + 6·∑(n+1)^{-9/8}`
(`zetaZerosInDiskCardBound`).  The named Prop
`jensenDiskZeroCountBound` is now a theorem.

(2) Clamp path: Jensen identity
(`riemannZetaMulSubOne_jensen_identity`);
`circleAverage ≤ log M` vs the constant
(`riemannZetaMulSubOne_jensen_avg_le`);
full divisor sum ≥ inner-disk subsum
(`zetaZerosInDisk_card_mul_log_le`);
circle majorant `M ≤ K(2+|T|)²` with `δ=1/8`.

(3) Height-count `N(X)` is r512.
Census stays 7 (external 2).  NO RH CLAIM.

## r512 census (outer bridges 19, height count)

Route (b)+inner lift, sorry-free.  Honest geometry:
`D(2+iT, 3/2)` only touches `β=1/2` at a point
(`w=0`).  Same Jensen circle `R=7/4`, inner
`r=13/8` gives window `w=5/8` on `β≥1/2`
(`(13/8)²-(3/2)²=25/64`).  FE pairing
(`riemannZeta_zero_iff_one_sub`) doubles
`0<β<1/2` onto `β>1/2`.

Proved: `zetaZeroCountUpToXBound` —
`(riemannZetaZerosOnClosedRect 0 1 X).card
≤ C·(1+X)·(1+log(2+X))` for `X≥0`, with
`C = 2·(16/5+5)·C_inner·(9/4)` and
`C_inner = (log K + log‖ζ(2)‖ + 2)/log(14/13)`.
`∑ 1/|ρ|²` dyadic assembly is r513.
Census stays 7 (external 2).  NO RH CLAIM.

## r513 census (outer bridges 20, [2c] counting complete)

[2c] ZÄHLTEIL KOMPLETT, sorry-free.
`zetaZeroCountUpToXBound` estimates Finset.card (not the
Jensen divisor sum).  Unweighted assembly is enough for
the named sum: dyadic blocks `B_j = {2^j ≤ |Im| < 2^{j+1}}`
plus the r499 compact `|Im|<1`, with
`#B_j ≤ N(2^{j+1})` and `|ρ| ≥ 2^j`, so the block is
`O((j+2) 2^{-j})`.  Geometric-polynomial comparison is
`summable_pow_mul_geometric_of_norm_lt_one`.

Proved: `summable_inv_sq_zetaZeros` —
`Summable fun ρ : {z // IsCriticalStripZetaZero z} => (‖ρ‖²)⁻¹`.
The weighted twin `∑ m_ρ/|ρ|²` is the same blocks once
`m_ρ ≤ D_F(ρ) ≤ C_inner(1+log(2+|γ|))` is recorded
(Jensen already bounds the divisor; card dropped the
weight).  [2d] remaining: contour integral, `T→∞`,
three-channel identification.  Census stays 7
(external 2).  NO RH CLAIM.

## r514 census (outer bridges 21, [2d] winding)

[2d] entry, sorry-free.  Mathlib has rectangle
Cauchy-Goursat (`integral_boundary_rect_eq_zero_of_differentiableOn`)
and circle residues, but no meromorphic residue
theorem on rectangles and no winding-number API.
Cheapest formalism: four-side sum, punch by the
r498 split `f = r/(z-p)+h`, Cauchy on `h`, and an
elementary arctan/log primitive for `∮ 1/(z-p)`.

Proved: `rectangleIntegral_inv_of_zero_mem` —
if `0` is in the open rectangle then
`rectangleIntegral (·)⁻¹ z w = 2πi`.  Horizontal
and vertical sides have closed-form integrals
(`integral_inv_add_I_mul`, `integral_inv_re_add_mul_I`);
the four arctan corners sum to `2π`
(`rectangle_inv_arctan_sum`).  One-pole wrap
(shift + holomorphic remainder) and the r499
Finset multi-pole are r515.

[2d] contour design: `Q_T = [-1/4, 2] × [-T, T]`.
A left edge at `Re>0` misses `0<β<ε` zeros; hat
pairing does not replace enclosure.  Right `Re=2`
uses `ζ'/ζ = -Σ Λ(n)n^{-s}` (r515 bound).  Left
`Re=-1/4` folds by FE onto `Re=5/4` plus `χ'/χ`.
Horizontals die from r506 `ĥ` decay times a
log-type `ζ'/ζ` bound.  Residue identity:
`∮ (ζ'/ζ) ĥ = spectralPartialSum ĥ - ĥ(1)`.
Census stays 7 (external 2).  NO RH CLAIM.

## r515 census (outer bridges 22, [2d] one-pole)

[2d] one-pole wrap, Finset multi-pole, and the
`Re ≥ 2` Dirichlet bound, sorry-free.
`rectangleIntegral_comp_add` is four real-side
substitutions (`p.re` horizontal, `p.im` vertical).
`rectangleIntegral_inv_of_mem` is the shifted
`∮ 1/(ζ-p) = 2πi`.  The residue lemma
`rectangleIntegral_simple_pole` takes the r498
split `f = r/(·-p)+h` with `h` holomorphic on
the closed rectangle as an explicit hypothesis.
The Finset form `rectangleIntegral_sum_simple_poles`
is the same split plus one Cauchy call on `h`.
On `Re s ≥ 2`, `‖ζ'/ζ(s)‖ ≤ ‖ζ'/ζ(2)‖` from
`ζ'/ζ = -L(Λ)` and termwise `n^{-Re s} ≤ n^{-2}`.
Remaining [2d]: assemble `∮ (ζ'/ζ) ĥ` on `Q_T`
(remainder glue is r516; apply r515 on `Q_T`,
then left-edge FE fold, horizontals, `T→∞`).
Census stays 7 (external 2).  NO RH CLAIM.

## r516 census (outer bridges 23, [2d] glue)

[2d] remainder glue, sorry-free.  The technical
core is `exists_analyticAt_update_of_meromorphicOrderAt_nonneg`:
meromorphic of order `≥ 0` fills by `update`
(`MeromorphicAt.analyticAt` + the r500 pattern).
r498/r500 × an analytic factor give the local
split `(ζ'/ζ)·F = r_p/(·-p) + H`; the punched
product has order `≥ 0`.  Product rule:
`ĥ(p) ≠ 0` keeps order `-1`; `ĥ(p) = 0`
cancels the pole.  Global `logDerivHatRemainder`
on the r499 Finset plus `s = 1` agrees with an
analytic germ at every pole, so it fills.
`ĥ` entire and `rectangleIntegral_sum_simple_poles`
on `Q_T` remain (r517).  Census stays 7
(external 2).  NO RH CLAIM.

## r517 census (outer bridges 24, [2d] contour identity)

[2d] fixed-T residue identity, sorry-free.
`FullWeilTest.hat` is entire (parametric DCT,
r509 majorant).  The r516 fill values assemble
to a global `H` on `Q_T` (finite poles:
r499 Finset + 1).  On sides that miss poles
(`T` not an ordinate; `Re = 2` and `Re = -1/4`
zero-free) the integrand is `Σ + H`, so
`rectangleIntegral_sum_simple_poles` gives
`contour_identity_fixed_T`.  Remaining: edge
bounds, `T → ∞`, three-channel id.  Census
stays 7 (external 2).  NO RH CLAIM.

## r518 census (outer bridges 25, [2d] outer bridges)

[2d] edge / T→∞ entry, honest cut, sorry-free.
PROVED: ĥ-decay on any compact Re-interval
(`norm_hat_le_inv_sq_on_Icc`, contour
`[-1/4, 2]`); Dirichlet `|ζ'/ζ|` for every
`Re ≥ σ > 1` (the 5/4 analog of r515);
zero-free strip `(-1/4, 0)`; Finset pigeonhole
and the unit-height Lücken-Lemma
(`exists_gap_height`, `exists_gap_sequence`)
from the r511 inner-disk count (two disks,
FE pairing on the left half).  Named, not
sorry: `HorizontalEdgeLandauBound` (classical
partial fraction / Borel–Carathéodory, 1–2
rounds), `LeftEdgeLogDerivBound` (FE fold +
digamma log on the fixed line Re = −1/4),
`ContourIdentityLimitAlongGaps`.  Remaining:
Landau on the gap edge, horizontals → 0,
left vertical, T→∞ of
`contour_identity_fixed_T`.  Census stays 7
(external 2).  NO RH CLAIM.

## r519 census (outer bridges 26, [2d] Landau kernel)

Mathlib already carries `Complex.borelCaratheodory`
(v4.29+ local pin).  PROVED, sorry-free: the
general-center wrappers `borelCaratheodory_ball`,
`_ball_zero`, `_closedBall_zero`; a holomorphic
log on a zero-free disk via
`DifferentiableOn.isExactOn_ball` (the primitive
`h` of `f'/f`, no branch); `Re h = log‖f‖ − log‖f(c)‖`;
and the Cauchy–BC bound
`norm_logDeriv_le_of_log_norm_le`.
`HorizontalEdgeLandauBound` stays a named Prop:
the ζ-assembly (`g = F/Π`, r510 on Re>δ, gap
sum `O(log² T)`) is the next cut.  Census stays 7
(external 2).  NO RH CLAIM.

## r520 census (outer bridges 27, [2d] Landau assembly)

Contour revision: r510 needs `Re > δ > 0`, so
`D(2+iT, R)` cannot cover `σ = -1/4` without FE.
`contour_identity_fixed_T` is hardcoded at
`σ₁ = -1/4` but the same hypotheses hold for every
`σ₁ ∈ (-1/4, 0)` (r518 zero-free).  Intended
contour `[-1/16, 2]`.  PROVED, sorry-free: the
logDeriv dictionary `ζ'/ζ = F'/F − 1/(s−1)`,
r510 poly bound on the inner disk `D(2+iT, 13/8)`,
`landauPoly` and its logDeriv, Jensen-weighted
`Σ m_ρ ≪ log T`, and the gap sum
`|Σ m_ρ/(s−ρ)| ≪ log² T`.  The Prop is weakened
to `σ ∈ [1/2, 2]` and `(1+log T)³`.  Remaining
clamp: holomorphic `g = F/Π` (dslope fold) +
r519 kernel, then the sliver `[-1/16, 1/2]`.
Census stays 7 (external 2).  NO RH CLAIM.

## r521 census (outer bridges 28, [2d] Landau wired)

`HorizontalEdgeLandauBound` is a theorem: on a
gap edge `Im = T ≥ 2`, for `σ ∈ [1/2, 2]`,
`|ζ'/ζ(σ+iT)| ≤ B (1+log T)³`.  PROVED,
sorry-free: r516 update-fill of `g = F/P` on
`D(2+iT, 13/8)` (orders cancel on
`landauInnerDisk`; fill ≠ 0), pigeonhole
mid-radius in `[49/32, 51/32]`, `|g|` on that
sphere then max modulus, center lower bound,
r519 kernel on `g`, plus r520 `P'/P` gap sum.
Remaining: sliver `[-1/16, 1/2]`, horizontals
→ 0, left edge, `T→∞`, three-channel id.
Census stays 7 (external 2).  NO RH CLAIM.

## r522 census (outer bridges 29, [2d] contour restated)

[2d] contour restated, honest cut, sorry-free.
PROVED: parametric `contour_identity_fixed_T_of`
on every `σ₁ ∈ (-1/4, 0)`, the `-1/16` instance,
and the r499 Finset bridge
(`riemannZetaZerosOnClosedRect_eq_critical`:
zeros in `Q_T(σ₁,2)` are the critical-strip
Finset).  Two-sided Lücken-Lemma
`exists_gap_height_abs` (`|Im|` window; FE
fold stays on a gap edge).  Horizontal
length×sup template
(`norm_horizontal_logDeriv_hat_integral_le`)
times ĥ-decay.  Named, not sorry:
`HorizontalEdgesTendstoZero`.  Remaining:
sliver `|ζ′/ζ|` via FE (`χ′/χ` + `|ψ|`),
Landau `A=1` vs r518 `ordinateGapConst`-gap,
left edge, `T→∞`, three-channel id.
Census stays 7 (external 2).  NO RH CLAIM.

## r523 census (outer bridges 30, horizontal clamps)

Honest cut, sorry-free.  PROVED: wide `[N-2, N+3]`
Lücken-Lemma `exists_gap_sequence_landau` (covers
the Landau disk `D(2+iT, 13/8)`; two-sided `|Im|`
gap for FE) and the `ψ` working lemmas
(`digamma_add_nat`, term bound, harmonic
`H_n ≤ 1+log(n+1)`, n-le-T kernel
`sum_digamma_kernel_norm_le`).  The r521 `A=1`
theorem is unchanged; general-A packing of Q'/Q
did not close this cut.  Named, not sorry:
`DigammaHorizontalLogBound` and
`HorizontalEdgesTendstoZero`.  Remaining:
general-A Landau, sliver FE (`cot` + `|ψ|`
identity + Landau at `-T`), left edge, `T→∞`.
Census stays 7 (external 2).  NO RH CLAIM.

## r524 census (outer bridges 31, Landau-A + ψ scope)

Honest cut, sorry-free.  PROVED: A-parametric
`horizontalEdgeLandauBound_of_gap` (A ≥ 1; B =
A · `landauHorizontalConst`; the A=1 Prop is the
instance) and the landau-gap wiring
`horizontalEdgeLandauBound_landauGap`.  Also the
n>T kernel tail `sum_digamma_kernel_tail_le`
(telescope Σ 1/(n(n+1))).  Mathlib Digamma is
`logDeriv Gamma` + recurrence + Euler `GammaSeq`;
no series / Stirling / Gauss.  Named, not sorry:
`DigammaHorizontalLogBound` (needs a `GammaSeq`
logDeriv anchor).  Remaining: `|ψ|` on the sliver,
FE/`cot`, horizontals→0, left edge, `T→∞`.
Census stays 7 (external 2).  NO RH CLAIM.

## r525 census (outer bridges 32, ψ-anchor)

Honest cut, sorry-free.  Route A chosen (cheaper than
GammaSeq-TLU): real `convexOn_log_Gamma` ⇒ monotone `ψ`,
series on `(1,2)`, identity on the sliver strip.  The
real-from-complex derivative bridge did not close.
`DigammaHorizontalLogBound` is narrowed to the FE
consumer `Re ∈ [1/2, 17/16]` and stays named.
Remaining: close that Prop (route A glue), FE/`cot`,
horizontals→0, left edge, `T→∞`.
Census stays 7 (external 2).  NO RH CLAIM.

## r526 census (outer bridges 33, ψ log bound)

Sorry-free.  Route A closed: `hasDerivAt_re_Gamma_ofReal`
(`real_of_complex` + `div_ofReal_re`, not `exact_mod_cast`)
gives real convexity ⇒ Weierstrass on `(1,2)` ⇒ identity
on `{1/4 < Re < 2}` ⇒ `|ψ| ≤ C(1+log(2+|Im z|))` on the
FE sliver `Re ∈ [1/2, 17/16]`, `|Im| ≥ 2`.
`DigammaHorizontalLogBound` is a theorem.
Remaining: cot-Schranke + `logDeriv` of the cos FE,
horizontals→0, left edge, `T→∞`.
Census stays 7 (external 2).  NO RH CLAIM.

## r527 census (outer bridges 34, FE sliver)

Sorry-free.  Tan bound `|tan z|² ≤ 1+1/sinh²(Im z)` on
`Im ≠ 0`, hence `|tan| ≤ √(1+1/sinh² 2)` for `|Im|≥2`.
`ψ` on the sliver via recurrence + the r526 log bound
on `Re ∈ [1/2, 3/2]`.  Cosine FE: `ζ(1-s)=G(s)ζ(s)`
and `(ζ′/ζ)(s) = −(ζ′/ζ)(1-s) − G′/G(s)`.
`sliverEdgeBound_negIm`: lower edge `σ−iT` via Landau
at the dual.  Upper edge `+iT` stays dual-Landau
(`sliverEdgeBound_of_dual`).  Horizontals not closed.
Census stays 7 (external 2).  NO RH CLAIM.

## r528 census (outer bridges 35, horizontals)

Sorry-free.  Schwarz reflection `ζ(conj s)=conj(ζ s)`
on `{1}ᶜ` (Dirichlet series on `Re>1`, identity
theorem).  Hence `|ζ′/ζ(σ+iT)|=|ζ′/ζ(σ−iT)|`.
Upper sliver and lower Landau by conjugation.
Glued bound `|ζ′/ζ| ≤ A·sliverEdgeConst·(1+log T)³`
on `σ ∈ [-1/16, 2]`, `|τ|=T≥2`.
`horizontalEdgesTendstoZero` along
`exists_gap_sequence_landau` (`log³/T² → 0`).
Left edge and three-channel `T→∞` assembly remain.
Census stays 7 (external 2).  NO RH CLAIM.

## r529 census (outer bridges 36, left edge)

Sorry-free.  `LeftEdgeLogDerivBound` restated to
`Re=-1/16`, `|Im|≥2`, and is a theorem:
`|ζ′/ζ| ≤ leftEdgeConst·(1+log(2+|τ|))` via FE,
Dirichlet at `17/16` (`norm_logDeriv_riemannZeta_le_of_re_ge`
is not hardcoded at `5/4`), and the sliver `ψ`/`tan`
anchor.  Gap-free: the dual is `Re=17/16>1`.
Right edge `Re=2` is the r515 Dirichlet bound.
Pointwise `ĥ` majorants for both verticals.
`ContourIdentityLimitAlongGaps` restated as the
intended `T→∞` identity; remaining clamp:
`Integrable` of the verticals and Finset exhaustion
of the r513 series.  Census stays 7 (external 2).
NO RH CLAIM.

## r530 census (outer bridges 37, LIMIT_IDENTITY)

Sorry-free.  Both vertical integrands of
`(ζ′/ζ) ĥ` are `Integrable` on `ℝ`.
Weighted `Summable (m_ρ ĥ(ρ))` via the
Jensen log-multiplicity times `ĥ ≤ C/(1+Im²)`,
majorized by dyadic `log/(1+t²)` blocks.
Rectangle Finsets along Landau `T_k` are
monotone and cofinal, so
`spectralPartialSum → tsum`.  Horizontals
`→ 0` (r528), verticals `→` improper
integrals, and the fixed-`T` identity along
gaps assemble to the theorem
`contourIdentityLimitAlongGaps`.  Census
stays 7 (external 2).  NO RH CLAIM.

## r531 census (outer bridges 38, HAT_INVERSION)

The r463 opaque `standardExplicitFormula` is
retired: it is now the r530 spectral pairing
`Re(∑ m_ρ ĥ(ρ) − ĥ(1))`.  The identification
`fullWeilForm = standardExplicitFormula`
remains a typed `sorry` (honest: three-channel
ℝ-form vs spectral, not a tautology).
Paley--Wiener kernel: `hatSlice σ t = g(t) e^{σ t}`,
`ĥ(σ − 2π ξ i) = 𝓕 (hatSlice σ) ξ`, and Mathlib
`Continuous.fourierInv_fourier_eq` gives
`𝓕⁻ (𝓕 (hatSlice σ)) = hatSlice σ`, and
the `2π`-frequency form
`∫ ĥ(σ+iτ) e^{-iτ u} dτ = 2π g(u) e^{σ u}`
is `hat_fourier_inversion`.  Right-edge
`integral_tsum`, left-edge FE fold, and
assembly against `combMass = 2Λ/√n` are
not claimed.  Census stays 7 (external 2).
NO RH CLAIM.

## r532 census (outer bridges 39, RIGHT_PRIME)

Sorry-free.  The right vertical of the r522
contour is the prime channel:
`rightVerticalIntegral_eq_prime_sum` gives
`∫ (ζ′/ζ)(2+iτ) ĥ(2+iτ) dτ = -2π ∑ Λ(n) g(log n)`.
Route: `logDeriv_riemannZeta_right_edge`
(Dirichlet series at `Re = 2`), termwise
`integral_term_mul_hat_eq_two_pi_vonMangoldt`
from r531 `hat_fourier_inversion`, and the
`integral_tsum` swap justified by
`summable_integral_norm_right_edge_term`
(Dirichlet weights times `C/(1+τ²)`).
`primeEval` is the bare `∑ Λ(n) g(log n)`,
finite because `g` dies past `fullAnchor`.
The gauge gap stays pinned and unclaimed:
`fullWeilCombSide_eq_two_div_sqrt_sum` shows
the corpus comb is `2Λ/√n`, so the left-edge
FE fold must supply the `2/√n` -- otherwise
the discrepancy is real.  Left edge and
assembly are not claimed.  Census stays 7
(external 2).  NO RH CLAIM.

## r533 census (outer bridges 40, LEFT_PRIME)

Sorry-free.  The left vertical of the r522
contour is the reflected prime channel minus
the archimedean clamp:
`leftVerticalIntegral_eq_reflected_prime_sub_arch`
gives
`∫ (ζ′/ζ)(-1/16+iτ) ĥ dτ
  = 2π ∑ Λ(n) n⁻¹ g(-log n)
    − ∫ (χ′/χ)(-1/16+iτ) ĥ dτ`.
Route: FE `logDeriv_riemannZeta_left_edge` on
the whole line (not only `|Im|≥2`), Dirichlet
at the dual `Re=17/16`, termwise inversion
`integral_dual_term_mul_hat_eq_two_pi_vonMangoldt_div_n`
from r531 `hat_fourier_inversion` at
`σ=-1/16`, `u=-log n`, and `integral_tsum`
justified by
`summable_integral_norm_left_edge_term`.
THE GAUGE: the FE fold produces `n⁻¹`, not
the corpus `2/√n`.  Combined contour pairing
is `∑ Λ(n)(1+n⁻¹)g(log n)`
(`contourPrimePairing_eq_one_add_inv_sum`);
`1+n⁻¹ ≥ 2/√n` with equality only at `n=1`
(where `Λ=0`).  Arch factor is explicit
(`logDeriv_zetaFEFactor_left_edge`); the
integral `leftEdgeArchIntegral` is the named
remaining clamp, not evaluated.  Assembly
against `combMass` is not claimed.  Census
stays 7 (external 2).  NO RH CLAIM.

## r534/r538 census (honest contour identification)

r534 completes the contour half of bridge 2:
`contourExplicitFormula_honest` identifies the exact spectral sum
with the arch clamp minus `Λ(n)(1+n⁻¹)`.  r538 packages that output as
`fullWeilFormHonest` and proves its identification with
`standardExplicitFormula`.  The original corpus form remains blocked,
with its discrepancy now explicit as `surplusComb + archGaugeDelta`;
the Mathlib RH endpoint still requires off-critical separation.
Census stays 7 (external 2).

PARALLEL (r556/r600): the Gabor class is a second, noncompact
conditional route.  Historical `gabor_inputs_to_mathlib_rh` is
VACUOUS (r600); live `gabor_zeroSide_inputs_to_mathlib_rh`.
Do not read r541 `SEPARATION_GO_GABOR` as closing
`fullWeil_separates_offCritical_zeros` or
`gabor_separationInequality`.  See the r556 and r599/r600
censuses.
NO RH CLAIM.

## r440 census (mean tau index)

Finite identities, no analytic bound, no new sorry.
T1 `κ† = ind₋(R† − ½I) = #{s ∈ (0,1): τ†(s)=0}` and
T2/MI2 (argument principle + linearity of the integrand)
are machine-checked; the Lean landing site
`exists_index_zero_of_block_mean_lt_one` is already
proved (r430).  The ½-cluster of `R†` maps to zeros of
`τ†` in a shrinking collar of `s = 1` (the contour-approach
cost).  Selected + core-42 have `κ† = 0` (block mean `0 < 1`);
dead χ have `κ† = 1`.  Unconditional block-mean bound
open (Reviewer-R439).  Census unchanged at 5.
NO RH CLAIM.

## r442 census (unconditional block mean)

One lemma, no new sorry: `κ† = 1{q† > 1}` (r433 last
pivot), so the block mean is the frequency of `q† > 1`.
Unsigned Chebyshev/Mertens majorants exceed 1.
Selected + core-42 stay pointwise living on the census
(`q† < 1`); the mean bound is open.  Census unchanged
at 5.  NO RH CLAIM.

## r443 census (selected delta floor)

One lemma, not proved: `liminf δ_k > 0` on Selected
(`δ = 1-q† = -sch`).  Chart identities are SATZ;
a floor is preferred only on the r421 k=5..9 slice
(`δ_∞ ≈ 0.027`).  kz16 sits below.  k=10 locked.
Census unchanged at 5.  NO RH CLAIM.

## r444 census (signed border mean)

Finite identities, no new sorry: the triple sum for
`q†` and the pole/regular split of `(I-C)^{-1}`.
The living mean is *not* a pole-weighted prime sum
(pole share `≤ 0.003` on Selected).  The diagonal
overflows from `k=7`; signed off-diagonal cancellation
is load-bearing.  Dead χ die by a pole overshoot.
The mean bound is circular: regular off-diagonal
cancellation against a window-dependent OP kernel
(second circularity verdict after r399).  Census
unchanged at 5.  NO RH CLAIM.

## r450 census (prefix mincut)

Definitional sharpening, no new sorry:
`frequently_selected_prefix_augDualResolvent_ge_half`
is `frequently_selected_augDualResolvent_ge_half`
(`frequently_prefix_mincut_ident` is `Iff.rfl`).
Python n_stab-δ is a different chart from full-window δ
(living windows disagree at relative gap ~1–3.6).
Census unchanged at 5.
NO RH CLAIM.

## r456 census (prefix vacuity red-team)

`Iff.rfl` is a naming of the full-cap cone, not an
`n_stab`-truncation.  The Python prefix is prime-blind
(MAIN = ARCH to machine precision for `n < J_P`;
`m_0` and `M_∂` are arch mass).  Arithmetic sits at
grades `≥ J_P` and in `combRead` of any `f` with
support past `log 2`.  r455 eventually-per-fixed-`n`
covers the blind zone, not depth `~ U_f/Δ`.
Mincut unchanged: still
`frequently_selected_augDualResolvent_ge_half` at
`W.cap`.  r449–r455 retyped as anatomy of the
prime-blind zone (r303 dictionary).  Census
unchanged at 5.
PARALLEL (r556): this mincut is the compact selected-window
cone, not the Gabor route.  See the r556 census.
NO RH CLAIM.

## r556 census (Gabor chain, documentation)

Documentation only; no new sorry, no code change.

PARALLEL CONDITIONAL ROUTE (not the compact-Weil / window-L*
mincut of r487--r538): `RH/GaborSeparation.lean` recorded the
logical wrapper
  `gabor_inputs_to_mathlib_rh` :
    `GaborExplicitFormula` →
    `GaborSeparationInequality` →
    (admissible Gabor spectral nonnegativity) →
    mathlib `RiemannHypothesis`.
That wrapper is VACUOUS (r600): the consumed hpos on
`gaborSpectralFormula` is FALSE.  Live wrapper:
`gabor_zeroSide_inputs_to_mathlib_rh` (hpos* on
`gaborZeroSide`).  The asserting theorem
`gabor_separationForAllZeros` is retired r612
(Prop retained unasserted).  r581 closed the EF hole:
`gabor_vertical_arithmetic_remainder` is a theorem
(no `sorryAx`).  Increment Path A is
already discharged: `GaborIncrementBound` /
`gaborIncrementBound_holds` (r546/r547,
`RH/ZeroIncrement.lean`) with constant
`2 * zetaZerosInDiskCardBoundInner`.

PROVED, sorry-free bricks (do not imply the inequality):
  * `RH/GaborIntegral.lean` (r543) Gaussian integral
    representation of the pure Gabor test;
  * `GaborIncrementBound` as above;
  * `RH/GaborThetaBound.lean` (r552)
    `gauss_online_mass_uniform`: on-line Gauss mass
    γ-uniform ≤ C · Θ_lobe.

EXPLICIT FORMULA: r548 sealed `EF_CONFIRMED` 36/36,
residuals ~1e-15, prime channel the classical comb
`2Λ(n)/√n` (r550).  Lean EF remainder closed r581
(`gabor_vertical_arithmetic_remainder` is a theorem).

QUANTIFIER WARNING (binding): r541 `SEPARATION_GO_GABOR`
is a certified numeric precheck against ONE synthetic FE
quadruple (42/42 cells, γ≤10⁴).  It does not discharge
`GaborSeparationForAllZeros`.  r553 `WITNESS_LOSES` is
historical leftover-scale (1- and 2-packet classes lose
the leftover game under pure counting control).  r559
settled leftover as a non-faithful Weil proxy and specified
`W_honest = Q_off + R_on`.  r560 sealed
`HONEST_WITNESS_WINS` (all=52).  r561 `DOMINANCE_UNIFORM`
was signed-refuted by r563/r566 (γ<0 double-count); r567
sealed `CANONICAL_DOMINANCE_HOLDS` (cells=119,
worst_margin=0.990408).  The `∀Z` Lean proof stays open
(`gabor_separationForAllZeros`).
r551: extremal selection alone is not enough (tie factor
e^{π²/128} ≈ 1.080 against a 141× counting-budget margin).
A spectral-gap hypothesis σ′/σ ≤ 0.9194 would compress
that budget; it is not assumed.

Window-L* / compact-Weil live mincut of r487--r538 is
unchanged.  Separation stays [O].  NO RH CLAIM.

## r582/r583 census (FE multiplicity + BoundLog2)

Documentation only; no new sorry, no census-gate change.

r582: `RH/GaborFEMultiplicity.lean` proves
`riemannZetaMultiplicity_eq_one_sub_all` (`m(z)=m(1-z)`
on the open strip via `Λ(s)=Λ(1-s)`) and
`sum_multiplicity_stripZerosWindow_le` (Jensen+FE fold:
unit window `∑m ≤ 2 C_inner(1+log(|N|+3))`).  Weighted
truncation compliance is a theorem.  Spectral-bridge
pack: `R_on_log = max((1+log)·proxy, ĥ-log majorant)`;
`GaborDominanceBoundLog2` packed sorry-free; remainder
was the budget.

r583: `GaborRemainderBudgetLog2` closed;
`GaborDominanceBoundLog2` is a theorem (both
`R_on_log/E` branches via `online_exp_le_log`; ĥ-side
closed linear-central+far-tail form
`gaborOnlineLogBudget = C_hat · gaborLogThreeLobeClosed`).
Axioms `[propext, Classical.choice, Quot.sound]`; no
`sorryAx`.

## r584–r588 census (spectral identifications)

Documentation only; no new sorry, no census-gate change.

r584: `gaborLogThreeLobeMajorant_le_closed` is a theorem
(Closed budget dominates the Finset-transfer majorant);
pure On/Off split `gaborZeroSide_eq_off_plus_on_pure` /
`_of_summable`.

r585: `riemannZetaMultiplicity_eq_conj` (`m(ρ̄)=m(ρ)`),
`gaborHat_star_pure`, `gaborHat_fe_quadrupole_eq_four_re`,
`gaborCriticalLineMassLeLogMajorant_holds`.  Honest:
weight-4 quadrupole tsum over all Im>0 double-counts.

r586: `gaborOffLineMassEqWeightedQuadrupoleTsum_holds` is
a theorem in honest FD form (Re>1/2 ∧ Im>0, weight 4,
+ real-axis remainder).  Double-count prop documented
dead.  Orbit toolkit (`stripStarEquiv` / `stripFEEquiv` /
`stripOrbitEquiv`).

r587: poly-in-t majorant `norm_gaborHat_le_poly_three_lobe`
and quartic summability are theorems.  Unrestricted
On/Off-split `gaborZeroSideEqOffPlusOn_holds` is a
theorem.

r588: `gaborWeightedQuadrupoleLimitEqFDTsum_holds`;
`riemannZeta_ne_zero_of_mem_Ioo` (ζ≠0 on (0,1) real,
via the r509 Euler–Maclaurin identity, not Eta);
`gaborOffLineRealAxisMass_eq_zero`.  Weighted Bridge-6
identification
`gaborWeightedQuadrupoleLimitEqOffLineMass_holds` is a
theorem.  Unweighted identification only `_of_simple`
(simple zeros); unconditional prop stays unasserted.
Living chain retargeted to the weighted form
(`gaborZeroSide_le_of_weighted_truncation_of_pure`).

Remaining named rest after r588 (not sorrys except the last):
`GaborTruncationUniformNeg` (uniform negativity of
weighted windows ≤ −δ — next analytic cut), close the
on-line majorant against the uniform off-line packet,
isolation / gammaDistinct / Dominance pack for genuine
zeros, and the unasserted Prop `GaborSeparationForAllZeros`
(asserting theorem retired r612).

## r589–r595 census (window→BoundLog2 + outer tail + glue)

Documentation only; no new sorry, no census-gate change.

r589: window→BoundLog2 bridge is a theorem — every nonempty
weighted FD window is BoundLog2 input
(`gaborWeightedTruncation_boundLog2_hyps`,
`gaborWeightedTruncationNegLog_holds`:
W_log(isolationShrink) < (9/10−η)·E < 0; lock margin
n-free via `gaborWeightedTruncation_lockMargin`).
Singleton card=1 supplies gammaDistinct+gammaHostIsolated.
`gabor_dominanceLog2_implies_separation` is pure logic on
two named bridge hypotheses.  Named, not proved:
`GaborWeightedTruncationGammaDistinct`,
`GaborTruncationUniformNeg` (does NOT follow from BoundLog2
— the isolation packet retunes with the window).

L2 adjudication r589: verdict `BRIDGE_A_IS_RH_CORE`.
The singleton route (W_honest(Singleton)<0 ⇒ arithmetic
formula<0) is not a translation lemma: it hides full
off-line tail control (foreign quadrupoles, factor
exp((σ′²−σ²)/2a), no fixed sign; R_on_log majorizes only
on-line).  Bridge B (Isolation a≤σ²/512 → Scaling a=σ²/64)
has no monotonicity transfer.

r590: `RH/GaborArithmeticSeparator.lean` records the
existential arithmetic endpoint
`GaborArithmeticSeparatesOffCriticalZeros` (∀ off-critical
zero ∃ admissible F: gaborArithmeticFormula F < 0).
Historical: `gabor_separation_of_arithmetic_separators`
(EF + separator ⇒ `GaborSeparatesOffCriticalZeros`) and
`gabor_arithmetic_inputs_to_mathlib_rh` (parallel Mathlib
chain without `scalingGaborTest`) are VACUOUS (r600).
Live: `gabor_arithmetic_zeroSide_inputs_to_mathlib_rh`
(GaborArithmeticSeparator.lean:68).
Named, unasserted: `GaborFixedPacketCofinalNegAt` and
`gabor_arithmetic_separator_of_cofinal_neg`.

r591: sealed probe `gabor_fixed_packet_cofinal_probe.py`
(FILE_SHA256 b614d583…, SPEC_SHA cd9af7ce…).  Fixed-packet
cofinal negativity is numerically tenable only with an
extremality gap: strict σ′≤σ−0.02 COFINAL_NEG_HOLDS 9/9
(worst −0.995); weak (tie allowed) and free σ′
COFINAL_NEG_BREAKS 0/9.  Not as r590 formulated without
the gap.

r592: sealed probe `gabor_window_adaptive_tail_probe.py`
(FILE_SHA256 1a77a650…, SPEC_SHA de35efea…).  Window-adaptive
packets (isolationShrink on W_R, a=min(σ²/512,shrink)) vs
outer tail 𝒯(a).  A MIXED (r591 center/merge/shrink holds;
near-tie δ=1e-8 float64 ω-collapse W_red=+1, IEEE artefact).
B/C/D HOLDS, 𝒯=0 ≪ margin, L2-numerator sup=−0.77 NOT_REACHED.
local-adaptive-global-fixed CONDITIONAL (IEEE ω-floor at
extreme near-tie; host-σ-max retune per height/T).

r593: `RH/GaborOuterTail.lean` — strip-width beats window
distance (`gaborOuterTail_num_le_neg_quarter`); exact ℝ
near-tie (`gaborWindowAdaptiveRule_exists`; no ℝ counterpart
of the r592 float64 collapse).  Historical endpoint
`gabor_window_adaptive_inputs_to_mathlib_rh` is VACUOUS
(r600).  Live: `gabor_window_adaptive_zeroSide_inputs_to_mathlib_rh`
(GaborOuterTail.lean:1299).
Named unasserted: `GaborWindowAdaptiveCofinalNeg`,
`gabor_arithmetic_separator_of_window_adaptive` (Bridge A
= RH-core).  Tail Props closed in r594.

r594: both tail Props are theorems —
`gaborOuterTail_tsum_le_exp` / `GaborOuterTailTsumLeExp_holds`
(FD indicator tsum over |Im ρ − ω| ≥ R);
`GaborOuterTailSmallerThanLocalMargin_holds`
(∀ε ∃a₀(ω,ε)≤1 ∀a<a₀: tail < ε·E(σ★,a)).  Multiplicity-
weighted Finset bound mass-independent, rate kept.
Axioms `[propext, Classical.choice, Quot.sound]`.

r595: `RH/GaborWindowGlue.lean` — three-term glue
(`gaborHonestWeil_window_add_outer`,
`gaborHonestWeil_le_window_plus_theta`);
catalog negativity
(`gaborCanonicalConfig_honestWeil_neg`,
`gaborHonestWeil_glue_neg_of_small_isolation`);
per-T checkpoint
(`gaborWeightedTruncation_windowAdaptive_existsDelta`,
`gaborWeightedTruncation_windowAdaptive_lockDelta`).
Named unasserted: `GaborWindowAdaptiveUniformDelta`
(T-uniform δ missing because of lex host-retune — r592
condition, not missing algebra) and
`gabor_window_adaptive_uniform_to_cofinal`.

Living sorry of this file retired r612
(`gabor_separationForAllZeros` deleted; Prop unasserted).
Tracked census stays 7
(Source 1, Elementwise 1, Canonical 3, ExternalBridges 2).  Finite/conditional proxy only.
Separation stays [O].
NO RH CLAIM.

## r596–r598 census (anchored witness)

Documentation only; no new sorry, no census-gate change.

L2 adjudication after r595: verdict `ANKER_TEILWEISE`.
A window frozen at a target fund-domain zero removes
host-retune of growing T-catalogs (r592) and the r592
float64 ω-collapse (no ℝ counterpart, r593).  Three
named gaps, not claimed: (i) window geometry must be
self-consistent relative to the *final* packet centre
ω; (ii) equal-ordinate σ-clusters (`gammaDistinct` of
genuine zeros) stay open; (iii) r595 glue used constant
`R_on`, the full transition needs the log budget.
L2 STOP: no UniformDelta / separator / existence claims.
Arithmetic identification (`GaborSpectralToArithmetic`) is
the pole-sign lemma ĥ(1) ≥ 0, NOT RH-core (proved r600 as
`GaborSpectralToArithmetic_holds`).  RH-core is hpos* on
`gaborZeroSide` / `gabor_separationForAllZeros`.

r596: `RH/GaborAnchoredWitness.lean` — type-bundle
`GaborAnchoredWindowWitnessAt` (all hyps explicit,
`hcover` ω-self-consistent).  Sorry-free log-glue
(`R_on → R_on_log`) and the conditional
`gaborAnchored_zeroSide_neg_of_isolationPacket`
(witness ⇒ spectral zero-side < 0 at shrink width).
Named unasserted at this cut:
`GaborBoundLog2AtAdmissibleWidth`,
`GaborAnchoredWitnessExists`,
`GaborSpectralToArithmetic` (then unasserted; r600
proved it as the pole-sign lemma ĥ(1) ≥ 0, NOT RH-core),
`gabor_anchored_to_arithmetic_separator`.

r597: `GaborBoundLog2AtAdmissibleWidth` discharged
(`gaborBoundLog2AtAdmissibleWidth_holds`).  Free-width
chain (`isolationShrinkOfConfig_admissible_of_le`,
`foreign_not_in_peakWindow_of_le`, the Log/Log2
`_of_le` majorants).  Main result
`gaborAnchored_zeroSide_neg`: witness ⇒ zeroSide < 0
at the OWN `(a,ω)`.  ω-lobe non-monotonicity absorbed
by existing ω≤γ caps; peak emptiness is a radius fact.

r598: singleton fragment + `htail` at retuned `ω(a)`
(`exists_gaborFundSingleton_htail`).  Cover isolated
as `GaborAnchoredCoverAt` (ordinate isolation);
`exists_gaborAnchored_of_cover` /
`gaborAnchoredCoverAt_to_nonempty` (Cover ⇒ nonempty
witness).  HONEST: `hcover` for genuine zeros open
(ordinate clusters); multi-point window open.
`GaborAnchoredWitnessExists` is NOT asserted.

Living sorry of GaborSeparation retired r612
(Prop `GaborSeparationForAllZeros` unasserted).
Tracked census stays 7.  Finite/conditional proxy only.
Separation stays [O].
NO RH CLAIM.

## r599/r600 census (vacuity audit)

Documentation only; no new sorry, no census-gate change.
Date 2026-09-01/02.  L3 verdict r599; Lean repair r600.

`gaborSpectralFormula` in GaborSeparation.lean is NOT the
Weil functional: it subtracts the pole term ĥ(1).  For
F₀ = `pureGaborTest 1 0` the zero-side sum is ≈ 3·10⁻⁴³
while Re ĥ(F₀,1) = π·e^{1/8} ≈ 3.5599, so
`gaborSpectralFormula F₀` ≈ −3.56 unconditionally.  Hence
the old hypothesis hpos := ∀ F admissible,
0 ≤ `gaborSpectralFormula` F is FALSE (not merely unproven),
and every Mathlib endpoint that consumed it was vacuous.

r600 Lean state (`lake build` green, tactic-sorry census 8
at that round; r612 census 7 after retiring
`gabor_separationForAllZeros`),
no `sorryAx`): live object is `gaborZeroSide` (spectral sum
without pole subtraction); hpos* := ∀ F admissible,
0 ≤ `gaborZeroSide` F is the true RH-core.  Theorems:
`gaborHat_criticalLine_nonneg`, `gaborHat_one_nonneg`
(pure family ⟨1,0,0⟩), `gaborSpectralFormula_eq`,
`gaborSpectralFormula_neg_of_small_zero_side`,
`gaborSpectralFormula_refuted_of_bound` (hypothesis form) and
r610 `gaborSpectralFormula_refuted_of_lowHeight` (rung (b):
`GaborLowHeightZeroFree 4`; classically true, first zero at
14.1347, not in Mathlib).  New
endpoints: `GaborZeroSideSeparatesOffCriticalZeros`,
`GaborZeroSideCriterionToMathlibRH`,
`gabor_zeroSide_criterion_to_mathlib_rh`,
`gabor_zeroSide_inputs_to_mathlib_rh`
(GaborSeparation.lean ~695–725),
`gabor_arithmetic_zeroSide_inputs_to_mathlib_rh`
(GaborArithmeticSeparator.lean:68),
`gabor_window_adaptive_zeroSide_inputs_to_mathlib_rh`
(GaborOuterTail.lean:1299); `rh_implies_gaborZeroSide_nonneg`
(pure), `gabor_zeroSide_pure_criterion_iff_rh` (pure family,
unconditional iff), `gabor_zeroSide_criterion_iff_rh`
(all F, carries extra hypothesis `hline`).

`GaborSpectralToArithmetic` is now a proved theorem
(`GaborSpectralToArithmetic_holds`,
GaborAnchoredWitness.lean:1227) — the pole-sign lemma
ĥ(1) ≥ 0, NOT the RH-core.  The RH-core is hpos*
(positivity of `gaborZeroSide`) resp. the unasserted
Prop `GaborSeparationForAllZeros` (asserting theorem
retired r612).

Old endpoints kept but marked VACUOUS (r600):
`GaborSeparatesOffCriticalZeros`,
`gabor_separation_of_inputs`,
`gabor_criterion_to_mathlib_rh`,
`gabor_inputs_to_mathlib_rh`,
`gabor_separation_of_arithmetic_separators`,
`gabor_arithmetic_inputs_to_mathlib_rh`,
`gabor_window_adaptive_inputs_to_mathlib_rh`.

Named open (no claim): on-line positivity for general even
quartics (beyond ⟨1,0,0⟩) so the iff holds without `hline`.
r610 discharged the F₀ tsum bound to the named hypothesis
`GaborLowHeightZeroFree 4`.

Tracked census stays 7.  Finite/conditional proxy only.
Separation stays [O].
NO RH CLAIM.

## r612 census (countable criterion; GaborSeparation sorry retired)

Documentation only of the r612 Lean cut.  Date 2026-09-02.

Asserting theorem `gabor_separationForAllZeros` deleted.
`GaborSeparationForAllZeros` remains an unasserted Prop:
OVERSPECIFIED prescribed packet, believed false by r605N T3,
superseded by `gabor_zeroSide_pure_criterion_iff_rh_unconditional`.
New module `RH/GaborCountableCriterion.lean`, rung (b):
`gabor_zeroSide_rational_criterion_iff_rh` (takes `hcont`;
local DCT of the ĥ-tsum).  No new `sorry`.
Tracked census 8 → 7 (Source 1, Elementwise 1, Canonical 3,
ExternalBridges 2).  NO RH CLAIM.

## r612C census (continuity holds; rational iff unconditional)

Documentation only of the r612C Lean cut.  Date 2026-09-02.
Module now 551 lines.  `gaborZeroSideContinuous_holds` proves
`GaborZeroSideContinuous` (joint continuity on `{a>0}×ℝ` via
local uniform Gaussian majorant
`‖ĥ‖ ≤ (π/a₀)exp((1/8+ω₁²/2)/a₀)exp(−t²/(4a₁))` and
`continuousOn_tsum`; summability via `summable_gauss_over_zeros`).
`gabor_zeroSide_rational_criterion_iff_rh_unconditional` :
(∀ (a ω : ℚ) (ha : 0 < (a:ℝ)),
0 ≤ gaborZeroSide (pureGaborTest a ω ha)) ↔ RiemannHypothesis —
UNCONDITIONAL; axioms propext / Classical.choice / Quot.sound.
Named-open list shrinks by one (`GaborZeroSideContinuous` is
proven).  Tracked census stays 7.  NO RH CLAIM.
-/

end RH
