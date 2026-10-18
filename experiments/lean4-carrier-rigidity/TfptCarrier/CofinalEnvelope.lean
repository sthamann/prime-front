/-
  CofinalEnvelope — the form-convergence hypothesis of `cofinal_weil`,
  stated as the instantiated error envelope instead of an opaque
  assumption.
  ===================================================================

  `CofinalWeil.cofinal_weil` and `CofinalPredefinition.
  cofinal_weil_for_fixed_idx` both consume

      hconv : ∀ v, Tendsto (fun m => ladderForm A sample m v)
                           atTop (𝓝 (QW v))

  as a bare hypothesis.  Until now that hypothesis was OPAQUE: nothing
  in the kernel recorded WHERE it comes from, and the numeric side had
  only measured decay rates.  It is now a THEOREM of the paper side —
  per-element Galerkin form convergence with the explicit rate
  O(D² log(1/D)) = O(2^{-2j} j), machine-checked in
  `verification/v912_form_convergence_theorem.py` (35/35 checks,
  verdict FORMCONV-PROVEN).  This module carries that change into Lean.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`).

    (1) `mesh`, `mesh_sq`, `formErrorEnvelope` — the deployed dyadic
        mesh D_j = 2^{-j} and the explicit level-j envelope
        (c_log · j + c_const) · D_j², which is exactly the paper shape
        C · D² log(1/D) + C' · D² because log(1/D_j) = j · log 2.

    (2) `formErrorEnvelope_tendsto_zero` — the envelope tends to 0.
        This is the whole analytic content needed downstream, and it is
        PROVEN here (n · rⁿ → 0 for 0 ≤ r < 1), not assumed.

    (3) `FormEnvelope` — THE PREMISE, as a named structure: per-element
        constants (c_log, c_const), a per-element window level (the
        DELTA-B threshold from which (H-grid), (H-cap), (H-align) hold
        for the deployed instantiation), and the explicit bound
        |ladderForm A sample m v − QW v| ≤ envelope(m) for every
        m ≥ level v.

    (4) `tendsto_of_formEnvelope` — the discharge: the envelope premise
        IMPLIES `hconv`.  Consequently
        `cofinal_weil_of_envelope`,
        `cofinal_weil_for_fixed_idx_of_envelope` and
        `cofinal_weil_predefined_of_envelope` state the cofinal
        extraction theorem with the convergence hypothesis REPLACED by
        the instantiated envelope.  The chain's convergence edge is now
        visibly the quantitative statement that v912 proves.

    (5) `envelope_strictly_stronger_than_convergence` — the
        non-vacuity lock (the CCCXXXVI lesson: a premise that restates
        its conclusion pins nothing).  Bare convergence carries NO
        rate: the convergent scalar ladder q m = 1/(m+1) violates the
        envelope shape at arbitrarily late levels for EVERY choice of
        (c_log, c_const).  So `FormEnvelope` is a strict strengthening
        of `hconv`, not a renaming of it.

    (6) `witnessEnvelope` / `witness_tendsto` — an explicit inhabited
        instance with NONZERO error at exactly the envelope rate
        (a 1×1 ladder with form (1 + m·4^{-m})·v² and limit v²), so the
        structure is not vacuously satisfiable only by exact ladders,
        and `witness_cofinal_weil` runs the full assembly end to end.

  THE HONEST BOUNDARY — DELTA-A IS REDUCED, NOT CLOSED.  The envelope
  itself is NOT discharged inside the kernel: `FormEnvelope` is a
  hypothesis of every theorem below, and its proof lives in the paper
  plus the machine checks of v912 (exact-rational nodal-defect
  identities, the layerwise majorant chain, and the cited
  Rosser–Schoenfeld constant ψ(x) < 1.03883x for support uniformity).
  What changed is the SHAPE of the assumption: the convergence
  hypothesis is no longer an unstructured `Tendsto`, it is the
  instantiated explicit-rate envelope, so a reader can see precisely
  which quantitative statement the extraction chain rests on and match
  it against v912 line by line.  Nothing here proves, gates, or
  evaluates the cofinal positivity hypothesis (H_cof) — that remains
  the open, RH-hard item of the chain.  No RH statement is formalized
  or claimed.

  A NOTE ON THE CONTINUITY EDGE.  The extraction chain used to cite
  "C⁰-continuity of Q_W at fixed support" for the extension from the
  dense family to all admissible test functions.  That citation is
  FALSE in the pure sup norm (v912 control C5: the even Lipschitz
  family e_n(w) = (1/n)·min(1, w/e^{-n²})·(1 − w/2)_+ has ‖e_n‖_∞ → 0
  while |A[e_n]| grows linearly).  The correct hypothesis is uniform
  convergence PLUS an equi-Lipschitz/Dini condition at the origin,
  supplied by the admissible even compact BV class; v912 T5.2 verifies
  the corrected modulus.  That extension step is a citation on the
  paper side and is deliberately not formalized here.
-/
import TfptCarrier.CofinalPredefinition

namespace TfptCarrier
namespace CofinalEnvelope

open Filter Topology Matrix CofinalWeil

/-! ### (1) The dyadic mesh and the explicit level-j envelope -/

/-- The deployed dyadic mesh `D_j = 2^{-j}` of the Galerkin ladder.
This identification is what fixes the ORDER meant by "cofinal" in
`CofinalWeil`: the ladder index IS the mesh level, so (H_cof) demands
a ladder cofinal in the MESH-REFINEMENT order — never one cofinal only
in the window/cap parameter at fixed mesh, which converges to the
wrong limit. -/
noncomputable def mesh (j : ℕ) : ℝ := (1 / 2 : ℝ) ^ j

theorem mesh_pos (j : ℕ) : 0 < mesh j := by
  unfold mesh; positivity

/-- `D_j² = 4^{-j}` — the identification that turns the paper's
`O(D² log(1/D))` into a geometric-times-linear sequence in `j`. -/
theorem mesh_sq (j : ℕ) : mesh j ^ 2 = (1 / 4 : ℝ) ^ j := by
  rw [mesh, pow_two, ← mul_pow]
  norm_num

/-- **THE EXPLICIT ERROR ENVELOPE** of the form-convergence theorem at
ladder level `j`: `(c_log · j + c_const) · D_j²`.  Since
`log(1/D_j) = j · log 2`, this is verbatim the paper shape
`C · D² log(1/D) + C' · D²`; `c_log` absorbs `log 2` together with the
layer coefficients `(A₀ + A₂)` and `c_const` the remaining
support-uniform terms (`Θ₀ A₀`, the comb mass on `[0, B]`, the
`A₁ (1 + D)` interpolation term and the `κ₃` cell-Lipschitz tail, all
of which are level-independent or smaller order). -/
noncomputable def formErrorEnvelope (cLog cConst : ℝ) (j : ℕ) : ℝ :=
  (cLog * (j : ℝ) + cConst) * mesh j ^ 2

/-- The envelope vanishes in the limit — the only analytic fact the
extraction chain needs from the rate, proven here from
`n · rⁿ → 0` (`0 ≤ r < 1`). -/
theorem formErrorEnvelope_tendsto_zero (cLog cConst : ℝ) :
    Tendsto (formErrorEnvelope cLog cConst) atTop (𝓝 0) := by
  have h1 : Tendsto (fun j : ℕ => (j : ℝ) * (1 / 4 : ℝ) ^ j) atTop (𝓝 0) :=
    tendsto_self_mul_const_pow_of_lt_one (by norm_num) (by norm_num)
  have h0 : Tendsto (fun j : ℕ => (1 / 4 : ℝ) ^ j) atTop (𝓝 0) :=
    tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)
  have h : Tendsto
      (fun j : ℕ => cLog * ((j : ℝ) * (1 / 4 : ℝ) ^ j)
        + cConst * (1 / 4 : ℝ) ^ j) atTop (𝓝 (cLog * 0 + cConst * 0)) :=
    (h1.const_mul cLog).add (h0.const_mul cConst)
  rw [mul_zero, mul_zero, add_zero] at h
  refine h.congr fun j => ?_
  simp only [formErrorEnvelope, mesh_sq]
  ring

/-! ### (2) The premise: the instantiated envelope -/

section Envelope

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)] {V : Type*}

/-- **THE FORM-CONVERGENCE PREMISE**, as the paper proves it.

For every element `v` of the dense family there are constants
`(cLog v, cConst v)` — in the deployed instantiation built from the
support diameter `b_K`, the interior sup `κ_K = sup |K''|`, the `H¹`
seminorm `κ₂` and the cell-Lipschitz constant `κ₃` — and a window
level `level v` from which the deployed hypotheses (H-grid), (H-cap),
(H-align) hold (DELTA-B: for fixed `v` and a fixed two-sided support
window they hold for all large `m`, which is exactly what `atTop`
needs), such that the Galerkin form is within the explicit envelope of
the limit functional at every level beyond the window.

This structure is a HYPOTHESIS here.  It is a theorem on the paper
side, machine-checked in `verification/v912_form_convergence_theorem.py`
under the cited classical input Rosser–Schoenfeld `ψ(x) < 1.03883x`
(support uniformity only). -/
structure FormEnvelope (A : ∀ m, Matrix (κ m) (κ m) ℝ)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ) where
  /-- Coefficient of the `D² log(1/D)` layer. -/
  cLog : V → ℝ
  /-- Coefficient of the pure `D²` layer. -/
  cConst : V → ℝ
  /-- The window threshold (DELTA-B), per element. -/
  level : V → ℕ
  /-- The explicit bound beyond the window. -/
  bound : ∀ (v : V) (m : ℕ), level v ≤ m →
    |ladderForm A sample m v - QW v| ≤ formErrorEnvelope (cLog v) (cConst v) m

variable {A : ∀ m, Matrix (κ m) (κ m) ℝ} {sample : ∀ m, V → κ m → ℝ}
  {QW : V → ℝ}

/-- **THE DISCHARGE**: the instantiated envelope implies the bare
convergence hypothesis of `cofinal_weil`.  From here on, `hconv` need
never be assumed opaquely. -/
theorem tendsto_of_formEnvelope (E : FormEnvelope A sample QW) (v : V) :
    Tendsto (fun m => ladderForm A sample m v) atTop (𝓝 (QW v)) := by
  have hz : Tendsto (fun m => ladderForm A sample m v - QW v) atTop (𝓝 0) := by
    refine squeeze_zero_norm' ?_
      (formErrorEnvelope_tendsto_zero (E.cLog v) (E.cConst v))
    filter_upwards [eventually_ge_atTop (E.level v)] with m hm
    simpa [Real.norm_eq_abs] using E.bound v m hm
  simpa using hz.add_const (QW v)

end Envelope

/-! ### (3) The assembly with the hypothesis instantiated -/

section Assembly

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)] {V : Type*}

/-- **COFINAL WEIL FROM THE ENVELOPE** — `CofinalWeil.cofinal_weil`
with the convergence hypothesis replaced by the explicit-rate premise.
Only (H_cof) and the envelope enter; the envelope is the statement
v912 proves. -/
theorem cofinal_weil_of_envelope {A : ∀ m, Matrix (κ m) (κ m) ℝ}
    (H : CofinalHypothesis A) (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (E : FormEnvelope A sample QW) :
    (∀ j v, 0 ≤ ladderForm A sample (H.idx j) v) ∧
    (∀ v, Tendsto (fun j => ladderForm A sample (H.idx j) v)
      atTop (𝓝 (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  cofinal_weil H sample QW (tendsto_of_formEnvelope E)

/-- The same for an EXPLICIT FIXED ladder index — the signature the
audit asks for: the ladder is a parameter, the convergence input is the
instantiated envelope, and the only remaining mathematical hypothesis
is PSD at the given rungs (H_cof). -/
theorem cofinal_weil_for_fixed_idx_of_envelope
    (idx : ℕ → ℕ) (hmono : StrictMono idx)
    (A : ∀ m, Matrix (κ m) (κ m) ℝ) (hpsd : ∀ j, (A (idx j)).PosSemidef)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (E : FormEnvelope A sample QW) :
    (∀ j v, 0 ≤ ladderForm A sample (idx j) v) ∧
    (∀ v, Tendsto (fun j => ladderForm A sample (idx j) v)
      atTop (𝓝 (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  CofinalPredefinition.cofinal_weil_for_fixed_idx idx hmono A hpsd sample QW
    (tendsto_of_formEnvelope E)

/-- The hardened wrapper: the PREDEFINED/noninterference certificate is
untouched by this change; only the convergence input becomes explicit. -/
theorem cofinal_weil_predefined_of_envelope
    {contract : CofinalPredefinition.NoninterferenceContract κ}
    {A : CofinalPredefinition.MatrixFamily κ}
    (H : CofinalPredefinition.PredefinedCofinalHypothesis contract A)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (E : FormEnvelope A sample QW) :
    (∀ j v, 0 ≤ ladderForm A sample (H.core.idx j) v) ∧
    (∀ v, Tendsto (fun j => ladderForm A sample (H.core.idx j) v)
      atTop (𝓝 (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  CofinalPredefinition.cofinal_weil_predefined H sample QW
    (tendsto_of_formEnvelope E)

end Assembly

/-! ### (4) Non-vacuity: the envelope is strictly stronger than `hconv` -/

/-- **THE PREMISE IS NOT A RENAMING.**  Bare convergence carries no
rate: for the convergent scalar ladder `q m = 1/(m+1)` and ANY constants
`(cLog, cConst)`, the envelope is violated at arbitrarily late levels.
Hence `FormEnvelope` is strictly stronger than the `Tendsto` hypothesis
it replaces, and the strengthening is exactly the quantitative content
v912 supplies. -/
theorem envelope_strictly_stronger_than_convergence
    (cLog cConst : ℝ) (N : ℕ) :
    ∃ m, N ≤ m ∧ formErrorEnvelope cLog cConst m < 1 / (m + 1 : ℝ) := by
  have h2 : Tendsto (fun j : ℕ => (j : ℝ) ^ 2 * (1 / 4 : ℝ) ^ j)
      atTop (𝓝 0) :=
    tendsto_pow_const_mul_const_pow_of_lt_one 2 (by norm_num) (by norm_num)
  have h1 : Tendsto (fun j : ℕ => (j : ℝ) * (1 / 4 : ℝ) ^ j) atTop (𝓝 0) :=
    tendsto_self_mul_const_pow_of_lt_one (by norm_num) (by norm_num)
  have h0 : Tendsto (fun j : ℕ => (1 / 4 : ℝ) ^ j) atTop (𝓝 0) :=
    tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num) (by norm_num)
  have hsum : Tendsto
      (fun j : ℕ => cLog * ((j : ℝ) ^ 2 * (1 / 4 : ℝ) ^ j)
        + ((cLog + cConst) * ((j : ℝ) * (1 / 4 : ℝ) ^ j)
          + cConst * (1 / 4 : ℝ) ^ j))
      atTop (𝓝 (cLog * 0 + ((cLog + cConst) * 0 + cConst * 0))) :=
    (h2.const_mul cLog).add ((h1.const_mul (cLog + cConst)).add
      (h0.const_mul cConst))
  rw [mul_zero, mul_zero, mul_zero, add_zero, add_zero] at hsum
  have hprod : Tendsto
      (fun m : ℕ => ((m : ℝ) + 1) * formErrorEnvelope cLog cConst m)
      atTop (𝓝 0) := by
    refine hsum.congr fun m => ?_
    simp only [formErrorEnvelope, mesh_sq]
    ring
  have hev : ∀ᶠ m : ℕ in atTop,
      ((m : ℝ) + 1) * formErrorEnvelope cLog cConst m < 1 := by
    have := hprod.eventually (eventually_lt_nhds (by norm_num : (0 : ℝ) < 1))
    exact this
  obtain ⟨m, hmN, hm⟩ := ((eventually_ge_atTop N).and hev).exists
  refine ⟨m, hmN, ?_⟩
  have hpos : (0 : ℝ) < (m : ℝ) + 1 := by positivity
  rw [lt_div_iff₀ hpos, mul_comm]
  exact hm

/-! ### (5) An inhabited instance with genuinely nonzero error -/

section Witness

/-- A 1×1 ladder whose rung-`m` entry is `1 + m · 4^{-m}` — a genuine
(non-exact) approximation of the limit form, decaying at exactly the
envelope's leading rate. -/
noncomputable def witnessMatrix (m : ℕ) : Matrix (Fin 1) (Fin 1) ℝ :=
  Matrix.of fun _ _ => 1 + (m : ℝ) * (1 / 4 : ℝ) ^ m

/-- Sampling: the element `v : ℝ` is sampled as the constant vector. -/
noncomputable def witnessSample (_m : ℕ) (v : ℝ) : Fin 1 → ℝ := fun _ => v

/-- The limit functional of the witness ladder. -/
noncomputable def witnessQW (v : ℝ) : ℝ := v ^ 2

theorem witness_ladderForm (m : ℕ) (v : ℝ) :
    ladderForm witnessMatrix witnessSample m v
      = (1 + (m : ℝ) * (1 / 4 : ℝ) ^ m) * v ^ 2 := by
  simp [ladderForm, ExcessSkeleton.formAt, witnessMatrix, witnessSample,
    Matrix.mulVec, dotProduct]
  ring

/-- The witness satisfies the envelope with `cLog v = v²`, i.e. its
error is exactly the leading `D² log(1/D)` layer — the structure is
inhabited by a ladder that genuinely converges, not only by exact
ladders. -/
noncomputable def witnessEnvelope :
    FormEnvelope witnessMatrix witnessSample witnessQW where
  cLog := fun v => v ^ 2
  cConst := fun _ => 0
  level := fun _ => 0
  bound := by
    intro v m _
    rw [witness_ladderForm, witnessQW, formErrorEnvelope, mesh_sq]
    have h : (1 + (m : ℝ) * (1 / 4 : ℝ) ^ m) * v ^ 2 - v ^ 2
        = ((m : ℝ) * (1 / 4 : ℝ) ^ m) * v ^ 2 := by ring
    rw [h, abs_of_nonneg (by positivity)]
    have : v ^ 2 * (m : ℝ) + 0 = (m : ℝ) * v ^ 2 := by ring
    rw [this]
    nlinarith [sq_nonneg v, pow_pos (by norm_num : (0 : ℝ) < 1 / 4) m]

/-- The discharge fires on the witness: convergence is DERIVED from the
envelope, not assumed. -/
theorem witness_tendsto (v : ℝ) :
    Tendsto (fun m => ladderForm witnessMatrix witnessSample m v)
      atTop (𝓝 (witnessQW v)) :=
  tendsto_of_formEnvelope witnessEnvelope v

/-- The witness rungs are PSD, so the full assembly runs end to end on
an explicit instance: envelope + (H_cof) ⇒ nonnegativity of the limit
functional (here the true statement `0 ≤ v²`). -/
theorem witness_psd (m : ℕ) : (witnessMatrix m).PosSemidef := by
  have hherm : (witnessMatrix m).IsHermitian := by
    rw [Matrix.IsHermitian, Matrix.conjTranspose_eq_transpose_of_trivial]
    ext i j
    simp [witnessMatrix, Matrix.transpose]
  refine Matrix.PosSemidef.of_dotProduct_mulVec_nonneg hherm fun x => ?_
  rw [star_trivial]
  have hval : x ⬝ᵥ witnessMatrix m *ᵥ x
      = (1 + (m : ℝ) * (1 / 4 : ℝ) ^ m) * (x 0 * x 0) := by
    simp [witnessMatrix, Matrix.mulVec, dotProduct]
    ring
  rw [hval]
  have hc : (0 : ℝ) ≤ 1 + (m : ℝ) * (1 / 4 : ℝ) ^ m := by positivity
  nlinarith [mul_self_nonneg (x 0)]

theorem witness_cofinal_weil :
    (∀ j v, 0 ≤ ladderForm witnessMatrix witnessSample (id j) v) ∧
    (∀ v, Tendsto (fun j => ladderForm witnessMatrix witnessSample (id j) v)
      atTop (𝓝 (witnessQW v))) ∧
    (∀ v, 0 ≤ witnessQW v) :=
  cofinal_weil_for_fixed_idx_of_envelope id strictMono_id witnessMatrix
    (fun j => witness_psd (id j)) witnessSample witnessQW witnessEnvelope

end Witness

/-! ### (6) Self-audit: no extra axioms, no `sorry` -/

#print axioms formErrorEnvelope_tendsto_zero
#print axioms tendsto_of_formEnvelope
#print axioms cofinal_weil_of_envelope
#print axioms cofinal_weil_for_fixed_idx_of_envelope
#print axioms cofinal_weil_predefined_of_envelope
#print axioms envelope_strictly_stronger_than_convergence
#print axioms witness_cofinal_weil

end CofinalEnvelope
end TfptCarrier
