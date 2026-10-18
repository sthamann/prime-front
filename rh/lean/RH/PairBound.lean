/-
RH/PairBound.lean -- the finite pair-bound theorem of the coupled-tau lane
(the r269/r271 fixed form c2PAIR as abstract finite algebra).

Provenance: round r271, contract PRIME.PORT.COUPLEDTAU.
UNIVERSAL_PAIR_THEOREM.01 (experiments only, no ledger row), probe
experiments/tfpt-discovery/universal_pair_theorem_probe.py
(SPEC_SHA 66f61c8a436af90e); the fixed form itself is the r269 winner
c2PAIR of phase_bulk_bound_probe.py (edge split F = 0.20 frozen, pairing
offset 0, no per-rung parameter).

THE OBJECT: the bulk remainder of the terminal border drive decomposes
into maximal same-sign runs; `l : List K` below is the list of EXACT
signed run sums `s_i` (machine ward r271 G21: `|s_i| = M_i` with `M_i`
the run mass, signs alternating).  The fixed pairing (offset 0) groups
adjacent runs into blocks; everything provable here is window-independent
finite algebra over a linearly ordered field -- exactly the layer the
r271 probe certifies numerically on 47 worlds (theorem validity, pair
identity, refinement chain, all exact).

Proved below (no `sorry`):
  * `blockSums_sum`     -- the exact pair-decomposition identity (i):
                           blocking preserves the total sum;
  * `abs_sum_le_absSum` -- the plain triangle |sum| <= sum of |.|;
  * `pairBound_eq`      -- pairBound = absSum after one blocking pass;
  * `abs_sum_le_pairBound`   -- the c2PAIR validity theorem (iii):
                           |sum l| <= pairBound l;
  * `pairBound_le_absSum`    -- the pairing never exceeds the abs
                           triangle (r269 G40 ward, exact);
  * `abs_sum_le_pairBound_level2` / `pairBound_level2_le` -- the r271
                           b2LEVEL2 refinement: valid and never worse;
  * `pair_exact`        -- the alternation pair identity (ii):
                           |sg*M1 - sg*M2| = |M1 - M2| for sg = +-1;
  * `boundary_triple_le` -- the r271 b1RAND boundary group is never
                           worse than pair + majorized tail.

The chain-specific hypothesis H5 (the certification margin
|Z_local| + eps < sqrt(5/7)) is since C1 a NAMED Prop
(`PairMarginLaw`, bottom of this file -- no truth commitment): it is
the entry door of the cofinal CERTIFICATE ROUTE (r271 lemma list
L1-L5), measured on the exception branch only as 5/7 (c2PAIR; b2LEVEL2
leaves kz39 at 0.002 dec and kz15 at 0.06 dec) -- asserting it as a
`sorry` overclaimed, so C1 retired the duplicate: the terminal hole is
`terminal_q_canonical` (RH/Canonical.lean) and the pair closure is a
PROVED corollary there through the named r263 dictionary.
r273 RETYPE: the former universal form `pair_margin_cofinal` (quantified
over the bare `PairSplitFamily`) is REFUTABLE -- the machine-checked
guard is `Counterexamples.pair_margin_not_universal` (model M = 1,
Z = Zloc = 2, runs = []: H1-H4 hold with equality, the margin would need
2 < 1; H5 can never follow from H1-H4 because the structure carries no
arithmetic).  H5 is now typed on the concrete window structure as
`pair_margin_main` (VonMangoldtWindow + the honest opaque `MainWindow`
predicate of RH/Window.lean).
r320 RETYPE (the R319 audit finding U3): the r273 form of
`pair_margin_main` still quantified `(Zloc, runs)` FREELY (bound only
by the split inequality) and was thereby refutable against ANY main
window -- the r273 disease one level up; conserved old type
machine-refuted in `Counterexamples.old_pair_margin_forces_empty`.
Since r320 the extraction is a DEFINITION (`signRuns`/`terminalDrive`/
`bulkRuns`/`edgeLocal`, with the split a PROVED property,
`canonical_split`) and the margin law is stated for the canonical
extraction only.  C1: the margin law is demoted from a `sorry` to the
named Prop `PairMarginLaw` -- the `sorry` census of this file is ZERO
(see the C1 demotion block below for the honest reason).

Claim boundary: research documentation.  NOT evidence for or against the
Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import Mathlib.Algebra.Order.AbsoluteValue.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Data.List.Basic
import Mathlib.Tactic.Linarith
import RH.Basic
import RH.Recursion
import RH.Window

namespace RH

namespace PairBound

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- the abs-sum `sum_i |l_i|` -- the r268 singleton triangle bound. -/
def absSum (l : List K) : K := (l.map fun x => |x|).sum

/-- one blocking pass of the FIXED pairing (offset 0): adjacent entries
are summed pairwise, an unpaired tail survives verbatim.  On the exact
signed run sums this realizes the r269 c2PAIR block structure; applied
twice it realizes the r271 b2LEVEL2 double-pair structure (radius 4). -/
def blockSums : List K → List K
  | [] => []
  | [a] => [a]
  | a :: b :: t => (a + b) :: blockSums t

/-- the r269 c2PAIR bound: block triangle after one blocking pass
(`eps = sum_pairs |s_odd + s_even| + |tail|`; on alternating runs
`|s_odd + s_even| = |M_odd - M_even|` by `pair_exact`). -/
def pairBound (l : List K) : K := absSum (blockSums l)

omit [IsStrictOrderedRing K] in
@[simp] theorem absSum_nil : absSum ([] : List K) = 0 := rfl

omit [IsStrictOrderedRing K] in
theorem absSum_cons (a : K) (l : List K) :
    absSum (a :: l) = |a| + absSum l := by
  simp [absSum]

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- **The exact pair-decomposition identity** (r271 Leg A (i)):
one blocking pass preserves the total sum -- the block structure is a
REGROUPING, never a loss. -/
theorem blockSums_sum : ∀ l : List K, (blockSums l).sum = l.sum
  | [] => rfl
  | [a] => rfl
  | a :: b :: t => by
      simp only [blockSums, List.sum_cons, blockSums_sum t]
      ring

/-- the plain triangle `|sum l| <= sum |l_i|` (list form). -/
theorem abs_sum_le_absSum (l : List K) : |l.sum| ≤ absSum l := by
  induction l with
  | nil => simp [absSum]
  | cons a t ih =>
      calc |(a :: t).sum| = |a + t.sum| := by simp
        _ ≤ |a| + |t.sum| := abs_add_le _ _
        _ ≤ |a| + absSum t := by linarith
        _ = absSum (a :: t) := (absSum_cons a t).symm

/-- **The c2PAIR validity theorem** (r271 Leg A (iii), r269 G40): the
fixed-form block triangle bounds the bulk remainder -- a two-line
consequence of the exact regrouping + the plain triangle. -/
theorem abs_sum_le_pairBound (l : List K) : |l.sum| ≤ pairBound l := by
  calc |l.sum| = |(blockSums l).sum| := by rw [blockSums_sum]
    _ ≤ absSum (blockSums l) := abs_sum_le_absSum _
    _ = pairBound l := rfl

/-- the pairing never exceeds the abs-sum triangle (the r269 G40
refinement ward, exact): `pairBound l <= absSum l`. -/
theorem pairBound_le_absSum : ∀ l : List K, pairBound l ≤ absSum l
  | [] => le_refl _
  | [a] => le_refl _
  | a :: b :: t => by
      have ih := pairBound_le_absSum t
      have htri : |a + b| ≤ |a| + |b| := abs_add_le a b
      simp only [pairBound, blockSums, absSum_cons] at *
      linarith

/-- **b2LEVEL2 validity** (r271 Leg B): the double-pair triangle bounds
the bulk remainder (radius 4, offset 0 at both levels). -/
theorem abs_sum_le_pairBound_level2 (l : List K) :
    |l.sum| ≤ pairBound (blockSums l) := by
  calc |l.sum| = |(blockSums l).sum| := by rw [blockSums_sum]
    _ ≤ pairBound (blockSums l) := abs_sum_le_pairBound _

/-- **b2LEVEL2 is never worse than c2PAIR** (r271 G40 sealed chain):
the double-pair bound refines the pair bound. -/
theorem pairBound_level2_le (l : List K) :
    pairBound (blockSums l) ≤ pairBound l :=
  pairBound_le_absSum (blockSums l)

omit [IsStrictOrderedRing K] in
/-- **The alternation pair identity** (r271 Leg A (ii)): on adjacent
runs of opposite sign the exact block sum is the exact mass gap:
`|sg*M1 + (-sg)*M2| = |M1 - M2|` for `sg = +-1`. -/
theorem pair_exact (sg M₁ M₂ : K) (hsg : sg = 1 ∨ sg = -1) :
    |sg * M₁ + (-sg) * M₂| = |M₁ - M₂| := by
  rcases hsg with h | h <;> subst h
  · ring_nf
  · rw [show (-1 : K) * M₁ + (-(-1 : K)) * M₂ = -(M₁ - M₂) by ring,
        abs_neg]

/-- **b1RAND boundary group** (r271 Leg B): evaluating the last three
runs as one signed group is never worse than the last pair + the
majorized unpaired tail. -/
theorem boundary_triple_le (a b c : K) :
    |a + b + c| ≤ |a + b| + |c| := by
  calc |a + b + c| = |(a + b) + c| := by ring_nf
    _ ≤ |a + b| + |c| := abs_add_le _ _

/-- the certification shape at the terminal (r263 two-branch strict +
the pair bound): if the local edge term plus the pair bound stays
strictly below the budget `M`, the target closes on that rung --
PROVED, the margin hypothesis is the input. -/
theorem pair_certifies {Z Zloc M : K} (l : List K) (hM : 0 < M)
    (hdec : |Z| ≤ |Zloc| + |l.sum|)
    (hmargin : |Zloc| + pairBound l < M) :
    Z ^ 2 / M ^ 2 < 1 := by
  have h1 : |Z| ≤ |Zloc| + pairBound l := by
    have := abs_sum_le_pairBound l
    linarith
  exact two_branch_cheap_strict hM h1 hmargin

/-- An abstract cofinal pair-split family: for every rung `i` the exact
run data of the F = 0.20 edge split (r271 H1-H4 as structure fields):
a local edge scalar `Zloc i`, the signed run-sum list `runs i`, and the
exact split `|Z i| <= |Zloc i| + |(runs i).sum|` (the triangle over the
exact decomposition `Z = Z_local + R`). -/
structure PairSplitFamily (K : Type*) [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] where
  Z : ℕ → K
  Zloc : ℕ → K
  runs : ℕ → List K
  /-- H1 + H2: the exact edge/bulk split (warded r271 G20/G23). -/
  split : ∀ i, |Z i| ≤ |Zloc i| + |(runs i).sum|
  /-- the budget scalar `sqrt(5/7)` in the corpus (r243 import). -/
  M : K
  M_pos : 0 < M

/-! ## r320: the canonical (Zloc, runs) extraction as a DEFINITION
(the U3 repair)

THE U3 FINDING (R319 audit, kernel-verified reproducible): the r273
form of `pair_margin_main` left `(Zloc, runs)` FREELY QUANTIFIED,
bound only by the split inequality -- the r273 disease one level up.
Adversarial instantiation (`Zloc = |F| + 1`, `runs = []` -- the split
holds trivially) refuted the margin against ANY main window: the
statement type was inconsistent with `∃ w, MainWindow w`.  The
conserved old type is machine-refuted in RH/Counterexamples.lean
(`old_pair_margin_forces_empty`).

THE REPAIR: the extraction is now a DEFINITION from the window data,
and the split inequality is a PROVED PROPERTY of the canonical
extraction (`canonical_split`), not a hypothesis over free pairs.

HONEST MODELING SCOPE: the measured r271 extraction (G20/G23) operates
on the probe-side drive decomposition (the F = 0.20 mesh-cell edge
split of the bulk remainder), which lives BELOW the window interface
-- `VonMangoldtWindow` carries only the border column `u`.  The Lean
extraction therefore models the split on the available data: the bulk
sequence is the pre-terminal border column `u_0 .. u_{cap-2}`,
aggregated into maximal same-sign runs (`signRuns` -- the r271 G21 run
structure), and the local edge scalar is the EXACT complement
`Z - Σ runs` (so H1+H2, the exact edge/bulk split, holds by
construction).  The identification of this canonical extraction with
the probe-side F = 0.20 extraction is MEASURED (r271, 42/42 warded),
not formalized -- it belongs to the border transcription TODO
(`SourceExact`, RH/Source.lean). -/

/-- maximal same-sign run aggregation (r271 G21 run structure): adjacent
entries of equal sign (product `>= 0`) are merged; a sign change starts
a new run. -/
noncomputable def signRuns : List ℝ → List ℝ
  | [] => []
  | a :: t =>
    match signRuns t with
    | [] => [a]
    | b :: r => if 0 ≤ a * b then (a + b) :: r else a :: b :: r

/-- run aggregation is a REGROUPING: the total sum is preserved exactly
(the H2 half of the split). -/
theorem signRuns_sum : ∀ l : List ℝ, (signRuns l).sum = l.sum
  | [] => rfl
  | a :: t => by
      have ih := signRuns_sum t
      simp only [signRuns]
      cases h : signRuns t with
      | nil =>
          rw [h] at ih
          simp only [List.sum_nil] at ih
          simp [← ih]
      | cons b r =>
          rw [h] at ih
          by_cases hab : 0 ≤ a * b
          · simp only [if_pos hab, List.sum_cons] at *
            rw [← ih]
            ring
          · simp only [if_neg hab, List.sum_cons] at *
            rw [← ih]

/-- **the terminal drive readout** `Z_w = F_{cap-1}` (r263 dictionary
`Z_w = r_{N-1}`). -/
noncomputable def terminalDrive (w : VonMangoldtWindow) : ℝ :=
  ((w.F (w.cap - 1) : ℚ) : ℝ)

/-- **the canonical bulk run list** (r320 definition; see the section
header for the honest modeling scope): the maximal same-sign run sums
of the pre-terminal border column `u_0 .. u_{cap-2}`. -/
noncomputable def bulkRuns (w : VonMangoldtWindow) : List ℝ :=
  signRuns (((List.range (w.cap - 1)).map fun k => ((w.u k : ℚ) : ℝ)))

/-- **the canonical local edge scalar**: the exact complement of the
bulk remainder in the terminal readout (H1: `Z = Zloc + Σ runs` holds
by construction). -/
noncomputable def edgeLocal (w : VonMangoldtWindow) : ℝ :=
  terminalDrive w - (bulkRuns w).sum

/-- **H1+H2 as a PROVED property of the canonical extraction** (the
r320 repair demand: the split inequality is a property of the
definition, never a hypothesis over free pairs). -/
theorem canonical_split (w : VonMangoldtWindow) :
    |terminalDrive w| ≤ |edgeLocal w| + |(bulkRuns w).sum| := by
  have hdec : terminalDrive w = edgeLocal w + (bulkRuns w).sum := by
    rw [edgeLocal]
    ring
  calc |terminalDrive w| = |edgeLocal w + (bulkRuns w).sum| := by
        rw [← hdec]
    _ ≤ |edgeLocal w| + |(bulkRuns w).sum| := abs_add_le _ _

/-- **H5, THE PAIR MARGIN LAW, retyped once more -- C1 DEMOTION to a
named Prop** (r273 -> r320 -> C1; no truth commitment).

Contract: PRIME.PORT.COUPLEDTAU.UNIVERSAL_PAIR_THEOREM.01 (r271,
experiments only -- no ledger row, no claim).

HISTORY.  r273: the pre-r273 form `pair_margin_cofinal` quantified over
the bare `PairSplitFamily` and is FALSE as a universal
(`Counterexamples.pair_margin_not_universal`).  r320 (the R319 audit
U3): the r273 form still quantified `(Zloc, runs)` freely -- refutable
against any main window (guard
`Counterexamples.old_pair_margin_forces_empty`); repaired by the
canonical extraction (`edgeLocal`/`bulkRuns` definitions, the split a
proved property).

C1 DEMOTION (the reviewer final-domain contract, goal 2 -- the pair
duplicate retired).  The r320 form `pair_margin_main` still asserted
the margin law as a `sorry` on all main windows.  That OVERCLAIMED:
the fixed pair form is measured to MISS on kz39 (0.002 dec) and kz15
(0.06 dec) under the b2LEVEL2 refinement (0.01/0.18 dec under plain
c2PAIR) -- the margin law is a CERTIFICATE ROUTE (35 cheap rungs +
both mains via the triangle, 5/7 exception rungs via the pair form),
not a faithful statement of the terminal hole.  Since C1 the hole
itself is `terminal_q_canonical` (RH/Canonical.lean, ONE statement),
the r263 dictionary `Z² = (5/7)·q_N` is the ONE named lemma
`pair_terminal_dictionary` there, and the pair CLOSURE
`pair_closes_main` is a PROVED corollary of the hole through it.
The margin law survives here as a NAMED Prop (the
`BorderedCompressionBridge` convention: statable, consumable, never
asserted), with the certificate direction proved below.  What a proof
of the law would still need is the r271 lemma list L1-L5 (L2 pair-sum
decay measured trending the wrong way, sp(N, eps) = +0.67, r272).
NO RH CLAIM. -/
def PairMarginLaw (w : VonMangoldtWindow) : Prop :=
  ∀ M : ℝ, 0 < M → M ^ 2 = 5 / 7 →
    |edgeLocal w| + pairBound (bulkRuns w) < M

/-- the conditional closure through the certificate route (PROVED; the
shape the r271 round certifies finitely): IF the named margin law holds
on a window, the terminal readout closes, `Z²/M² < 1` -- via the proved
`canonical_split`.  The unconditional closure on canonical windows is
`pair_closes_main` (RH/Canonical.lean), a corollary of the terminal
hole through the named r263 dictionary. -/
theorem pair_closes_of_marginLaw (w : VonMangoldtWindow)
    (h : PairMarginLaw w) {M : ℝ} (hM : 0 < M) (hM2 : M ^ 2 = 5 / 7) :
    terminalDrive w ^ 2 / M ^ 2 < 1 :=
  pair_certifies (bulkRuns w) hM (canonical_split w) (h M hM hM2)

end PairBound

end RH
